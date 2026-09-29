# -*- coding: utf-8 -*-
"""What is painted over a figure's text, measured in the page.

usage: python3 ordercheck.py ../[0-9][0-9]-*.html        (from files/)

Every top-level <svg> of each page is screenshotted in Chromium as built, then again with
every <text> moved to the end of its <svg> (so nothing can be painted over any text), and
the pixels that differ inside each text's box are counted. Whatever is listed was painted
after the text and over it - a line, a marker, a tint - or clipped away from it. Each line
names the elements drawn after the text whose box meets it.

WHY THIS EXISTS. The file guards (overruns, overflows, collisions, linecheck) read one
figure file at a time. Review session 18 wrote this measure (claude/session18_order.py) and
it found what they could not: page 18's roads map had never drawn its bottom hundred units,
because two figures in one page shared a clip id (pageguard.duplicate_ids() now refuses
that), and page 45's 1936 leader was drawn through "a quarter". Review session 19 made it a
tool, on a recommendation to Carsten, standalone like linecheck: it needs Chromium and Playwright, and the
builds do not.

THE FLOOR, TRIED (review session 19). Session 18's version counted a pixel when its
luminance changed by more than 40 of 255, inside the band from .2 to .85 of the text's
height less 2 device px at its left and right ends, and listed a text from 6 such pixels. Six marks were planted
in a copy of page 43: a 0.6 dark line, a 0.3 grey hairline, a dot of r 0.8, a 1-unit
vertical, a paper wash at .35 and a rust tint at .12 over a label. The first five were
caught; the tint changed nothing by more than 40 and was not. Check 1 then found the band
too narrow: a line through the ascenders or a descender's tail was missed, and so was a
shipped fault - page 11's red dot on the S of "Sweyn Estridsen", whose pixels fell in the
2 px trimmed off the left end. So a pixel now counts when any one channel changes by more
than DIFF (4), inside the text's whole box and the halo round it (HALO_PAD, at the figure's
scale), and a text is listed from FLOOR (1) pixel. Check 2 planted a 0.4 line just under a
label's descenders, over its halo, and it was missed; check 3 found why: the boxes were read
from the svg's fractional top while the screenshot starts at a whole CSS pixel, so every box
sat up to 1 CSS px above its pixels. Both are fixed. All
the plants are caught, and the book gives no noise: the two renders differ only where
something is painted over a text. On the book as review session 19 found it, seven texts
in three figures: 03's "flint daggers" line through white "farmer" and "steppe-derived
ancestry" (linecheck's 3 per cent floor for unhaloed text passes it: about 2 per cent of
the box), 11's dot, and 12's event lines through four labels over their halos (linecheck's
halo reading ignores what is drawn after) - all fixed in that session. Its first run also
listed 06's grade names, the measure's own fault: the moved copy lost the halo's
stroke-linejoin, which a class on a <g> gives. JS_MOVE copies the stroke and font
properties the page's CSS sets, multiplies in the opacity of every enclosing <g>, and drops
a clip on the text itself, so a text its own clip cuts is listed.

BLIND SPOTS. A text painted over by a LATER TEXT is not seen: the texts keep their order
when moved (collisions() compares text with text). A text outside the canvas is cut the
same way in both renders (overruns() and overflows() measure that). A text with no box
(inside <defs>, a <marker>, display:none) is skipped. A marker at a line's end is caught
but not named: a line's box leaves its markers out, so the line reads "nothing drawn after
it". The screenshot is 2x, so a mark finer than half a CSS pixel may change nothing, and a
mark within about half a CSS pixel of a halo may share a device pixel with it and be listed
as touching.
Measured in Chromium on Linux; on another machine the renders are still compared with each
other, not with a stored image. Without Playwright, Pillow or a Chromium to launch, it
prints SKIPPED and exits 2; it exits 1 when it lists anything, 0 when it lists nothing.
"""
import sys, os, glob, io

DIFF = 4          # a pixel counts when some channel changes by more than this (of 255)
FLOOR = 1         # a text is listed from this many counted pixels
SCALE = 2
HALO_PAD = 1.3    # user units: half the halo's 2.6 stroke (style.css), added round each box
                  # at the figure's scale (1.0 CSS px at viewBox 900 in the 1200 page, 2.1 at 430)

JS_BOXES = r"""(si) => {
 const svg=[...document.querySelectorAll('svg')].filter(s=>!s.parentElement.closest('svg'))[si];
 // the screenshot starts at a whole CSS pixel, so the boxes are read from there (check 3:
 // measured from the svg's fractional top they sat up to 1 CSS px above their pixels)
 const r0=svg.getBoundingClientRect(), r={left:Math.floor(r0.left), top:Math.floor(r0.top)};
 const k=svg.getScreenCTM().a;
 const marks=[...svg.querySelectorAll('path,line,polyline,polygon,rect,circle,ellipse,image')]
   .filter(e=>!e.closest('defs,marker,clipPath,mask,symbol'));
 return [...svg.querySelectorAll('text')].map(t=>{
   const b=t.getBoundingClientRect();
   const after=marks.filter(e=>(t.compareDocumentPosition(e) & Node.DOCUMENT_POSITION_FOLLOWING)).filter(e=>{
     const q=e.getBoundingClientRect(), p=1.5;
     return q.left<=b.right+p && q.right>=b.left-p && q.top<=b.bottom+p && q.bottom>=b.top-p; })
     .slice(0,3).map(e=>{ const a=[...e.attributes].filter(x=>!['d','points','fill-rule'].includes(x.name))
       .map(x=>x.name+'='+x.value).join(' '); return '<'+e.tagName+' '+a.slice(0,90)+'>'; });
   return [t.textContent.replace(/\s+/g,' ').trim().slice(0,50), b.left-r.left, b.top-r.top, b.width, b.height, after, k]; }); }"""

# Each text is moved to the end of the root <svg> inside a <g> carrying its full transform,
# with every property the page's CSS may set on it or give it from a <g> copied onto it.
JS_MOVE = r"""(si) => {
 const svg=[...document.querySelectorAll('svg')].filter(s=>!s.parentElement.closest('svg'))[si];
 const P=['fontFamily','fontSize','fontStyle','fontVariant','fontWeight','letterSpacing','wordSpacing',
   'fill','fillOpacity','stroke','strokeWidth','strokeOpacity','strokeLinejoin','strokeLinecap',
   'strokeMiterlimit','strokeDasharray','paintOrder','opacity','dominantBaseline','textDecoration','visibility'];
 for (const t of [...svg.querySelectorAll('text')]) {
   const m=svg.getScreenCTM().inverse().multiply(t.getScreenCTM());
   const c=t.cloneNode(true), cs=getComputedStyle(t);
   const g=document.createElementNS('http://www.w3.org/2000/svg','g');
   g.setAttribute('transform',`matrix(${m.a},${m.b},${m.c},${m.d},${m.e},${m.f})`);
   for (const k of P) c.style[k]=cs[k];
   // a <g>'s opacity multiplies into its texts; carried, or the moved copy draws darker
   let op=parseFloat(cs.opacity); for (let e=t.parentElement; e && e!==svg; e=e.parentElement) op*=parseFloat(getComputedStyle(e).opacity);
   c.style.opacity=op;
   // a clip on the text itself would cut the copy the same way: dropped, so a cut text is listed
   c.removeAttribute('clip-path'); c.style.clipPath='none';
   c.setAttribute('text-anchor', cs.textAnchor); c.removeAttribute('transform');
   g.appendChild(c); svg.appendChild(g); t.remove(); } }"""


def chromium_path():
    for p in (os.environ.get('DK_CHROMIUM'), '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'):
        if p and os.path.exists(p):
            return p
    return None


def main(args):
    pages = sorted({f for a in args for f in glob.glob(a)})
    if not pages:
        print("usage: python3 ordercheck.py ../[0-9][0-9]-*.html"); return 2
    try:
        from playwright.sync_api import sync_playwright
        from PIL import Image, ImageChops
    except ImportError as e:
        print("SKIPPED, nothing measured: %s (pip install playwright pillow; a Chromium, "
              "or DK_CHROMIUM=/path/to/chrome)" % e)
        return 2
    listed = 0; figs = set()
    with sync_playwright() as p:
        exe = chromium_path()
        try:
            br = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        except Exception as e:
            print("SKIPPED, nothing measured: no Chromium to launch (%s; set DK_CHROMIUM=/path/to/chrome)"
                  % str(e).strip().splitlines()[0])
            return 2
        pg = br.new_page(viewport={'width': 1200, 'height': 900}, device_scale_factor=SCALE)
        nfig = 0
        for f in pages:
            url = 'file://' + os.path.abspath(f); pre = os.path.basename(f)[:2]
            pg.goto(url)
            n = pg.locator('svg:not(svg svg)').count()
            for si in range(n):
                nfig += 1
                pg.goto(url)
                loc = pg.locator('svg:not(svg svg)').nth(si)
                loc.scroll_into_view_if_needed()
                a = Image.open(io.BytesIO(loc.screenshot())).convert('RGB')
                boxes = pg.evaluate(JS_BOXES, si)
                pg.evaluate(JS_MOVE, si)
                b = Image.open(io.BytesIO(loc.screenshot())).convert('RGB')
                if a.size != b.size:
                    print("!! %s svg%d: the figure changed size when its texts moved" % (pre, si))
                    listed += 1; figs.add((pre, si)); continue
                # the largest change in any one channel, not a luminance (check 1)
                r, g, bl = ImageChops.difference(a, b).split()
                d = ImageChops.lighter(ImageChops.lighter(r, g), bl).point(lambda v: 255 if v > DIFF else 0)
                for txt, x, y, w, h, after, k in boxes:
                    if w <= 0 or h <= 0:
                        continue
                    # the whole box (review session 19, check 1): session 18's version kept
                    # only the band from .2 to .85 of the height, less 2 px at each end, and
                    # missed page 11's red dot on the S of "Sweyn Estridsen" and a line
                    # through the ascenders or a descender
                    # and the halo round it (checks 2 and 3): a line over the halo but under
                    # no letter is a crossing (D-18)
                    pad = HALO_PAD * k * SCALE
                    box = (int(SCALE * x - pad), int(SCALE * y - pad),
                           int(SCALE * (x + w) + pad) + 1, int(SCALE * (y + h) + pad) + 1)
                    cnt = d.crop(box).histogram()[255]
                    if cnt >= FLOOR:
                        listed += 1; figs.add((pre, si))
                        print("   ! %s svg%d %4d px  %r" % (pre, si, cnt, txt))
                        for e in after:
                            print("        drawn after it: %s" % e)
                        if not after:
                            print("        nothing drawn after it meets its box: a clip, a mask, or a marker "
                                  "at a line's end (a line's box leaves its markers out)?")
        br.close()
    print("%d text(s) painted over, in %d of %d figure(s) on %d page(s)" % (listed, len(figs), nfig, len(pages)))
    return 1 if listed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
