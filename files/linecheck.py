# -*- coding: utf-8 -*-
"""What collisions() cannot see: a line or a shape printed through a text.

usage: python3 linecheck.py svg_crowns.txt [svg_hemming.txt ...]          (from files/)
       python3 linecheck.py c0[1-9]_body.html c1[01]_body.html  the inline figures, one by one
       python3 linecheck.py --bare svg_*.txt     the session-15 reading, halo ignored

Review session 15 wrote this to find a coastline, an attack line or a marker printed
through a label (mapspine.collisions() compares text with text only). It rendered the
figure without its text and flagged every text whose box was not one flat ground: 220
texts in 31 figures. Its docstring said most were "labels set on purpose across a border
or a tinted territory". REVIEW SESSION 16 READ ALL 220 AGAINST THE PNGs, and that was
wrong: about 214 were real - coasts, borders and routes through town and territory
names in every figure listed. Six were false (a text that also appears on a flat panel;
the match is by string), and on a second look three are kept on purpose (ON_PURPOSE).

Carsten chose a halo for every .mapt/.mapl/.mapx text (mapspine, "the halo"; one rule in
style.css). A thin line - a coast, a dashed border, the graticule, anything up to
mapspine.HALO_THIN - now stops at the letters, and a label may straddle two grounds.
So the default reading asks only what the halo cannot fix:

  a haloed text is CROSSED if a THICK stroke (wider than HALO_THIN: a route, an attack
  line, a heavy border) or a MARKER (a circle of r <= 8) puts ink in its box. The test
  renders the bare figure twice, with and without those strokes and markers, and
  counts the pixels that differ.
  a text with no halo (a fill in HALO_EXEMPT: light, or ON_BAR_INK) is read as in
  session 15: its box must be one flat ground.
  a light fill that is NOT in HALO_EXEMPT is reported: it would get a light halo.

A numeral printed on its own marker is not a crossing (two characters, on a disc of
r >= 4). AN AID TO LOOKING, still wired into nothing: read what it lists in the PNG.
Planted (session 16): the shipped versions of the figures it fixed, and session 15's
svg_hemming and svg_crowns before their fix (dd27400) - every crossing fires, except
svg_reconquest's: its numerals drew dark (D-11), take the halo, and were moved onto their
territories for reading, not for this check. Light-text spellings style.css would not
exempt (fill:#f0f2ee, "fill: #F0F2EE", #FFF) and a light fill= attribute are reported.
BLIND SPOTS. As for mapspine.text_items(), which this reads since review session 17 (a
text with markup inside, a rotated text and a class or text-anchor set on a <g> are now
measured; a rotated text is tested inside its own corners, not its box; since review
session 18 a font-size in style is read, and CHAR_W is measured in the page, D-19). A
text whose class is not exactly one of mapt/mapl/mapx (say class="mapx big") takes the
page's halo but is read here as unhaloed. Here: a small
FILLED shape drawn as its own element - a closed-path arrowhead, a square marker - counts
as ground, not as a mark (arrowheads drawn with <marker> are marks). And the check is by
pixel, not by glyph: the box is shrunk a unit, so a line that ends against the edge of a
letter can pass.
"""
import re, sys, io
sys.path.insert(0, ".")
import mapspine as M

MARKER_R = 8.0
# a dashed route crossing a label on the diagonal covers little of its box: "the bishop's
# seat" in svg_atlantic was 1.4%, missed at the flat-ground floor of 3%. At 0.8% seven more
# were listed (1807 København, sound Helsingør and Helsingborg, 1721 Gottorp, 1814 and
# 1864 Slesvig, the bishop's seat) and all seven were real when looked at. Below 0.8% is
# unread: a lower floor is a new reading pass.
MARK_FLOOR = 0.008

# LEFT ON PURPOSE, looked at in review session 16. Listed, not counted. A new entry needs
# its reason, and whoever adds it looks at the PNG first.
ON_PURPOSE = {
    ("svg_partition.txt", "HADERSLEV"):
        "the refused partition is struck out; figs_21 draws the X under the labels",
    ("svg_baltic.txt", "Sixty years east"):
        "a 21px title with a thin coast behind it; the letters read (Part D, no halo class)",
    ("svg_reconquest.txt", "Buying a kingdom back"):
        "a 21px title with a thin coast behind it; the letters read (Part D, no halo class)",
}
# MEASURED WRONG, not crossed. Listed, not counted. Empty since review session 17: 06's
# "the great majority" took text-anchor="end" from its <g>, which text_boxes() did not read,
# and was measured into the pyramid; text_items() reads it.
KNOWN_FALSE = {}


def _hex6(h):
    """#fff, #FFF and #ffffff all come back as #FFFFFF."""
    h = h.lstrip("#")
    return "#" + (("".join(c * 2 for c in h)) if len(h) == 3 else h).upper()


def _lum(h):
    """WCAG relative luminance: #F0F2EE is .88, the mid greens and #C2704F about .2."""
    def lin(c):
        return c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    h = _hex6(h)
    r, g, b = [lin(int(h[i:i + 2], 16) / 255) for i in (1, 3, 5)]
    return .2126 * r + .7152 * g + .0722 * b


LIGHT_NAMES = {"white": "#FFFFFF", "snow": "#FFFAFA", "ivory": "#FFFFF0",
               "whitesmoke": "#F5F5F5", "ghostwhite": "#F8F8FF", "floralwhite": "#FFFAF0",
               "linen": "#FAF0E6", "seashell": "#FFF5EE", "mintcream": "#F5FFFA",
               "azure": "#F0FFFF", "aliceblue": "#F0F8FF", "honeydew": "#F0FFF0"}


def _colour(v):
    """A CSS colour as #XXXXXX, or None if it is not one this can read."""
    v = v.strip().strip("'\"").strip().lower()
    if re.fullmatch(r"#[0-9a-f]{3}|#[0-9a-f]{6}", v):
        return _hex6(v)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[\s,]+(\d+)[\s,]+(\d+)(?:[\s,/]+[\d.%]+)?\s*\)", v)
    if m:
        return "#%02X%02X%02X" % tuple(min(255, int(x)) for x in m.groups())
    return LIGHT_NAMES.get(v)


def light_fault(a):
    """What is wrong with a text's fill for the halo, or None.

    ONE SPELLING. style.css exempts a text from the halo by an attribute selector, which
    matches the spelling and not the colour, and haloed() does the same: fill:#XXXXXX,
    capitals, no space, inside style="...". So a fill in a map-class text's style that is
    spelt any other way (#fff, "fill: #", FILL:, rgb(), a name, !important) is reported,
    dark or light - a misspelt ON_BAR_INK would get a halo as surely as a misspelt white.
    All 121 such fills were written this way when this was added (review session 16).
    Then: a canonical light colour not in HALO_EXEMPT would get a light halo. And a light
    fill="..." ATTRIBUTE, with no fill in the style, loses to the class rule (D-11) and is
    drawn dark, as fourteen bar labels on pages 01-03 were until review session 16."""
    if not re.search(r'class="map[tlx]"', a):
        return None
    style = re.search(r'(?<![\w-])style\s*=\s*(["\'])(.*?)\1', a)
    decls = [d for d in (style.group(2).split(";") if style else [])
             if d.split(":")[0].strip().lower() == "fill"]
    if len(decls) > 1:        # the exemption can match one while the last one draws
        return "%d fills in one style: write one" % len(decls)
    for d in decls:
        val = d.split(":", 1)[1].strip() if ":" in d else ""
        if val.lower() == "none" or val.lower().startswith("url("):
            continue
        if not re.fullmatch(r"fill:#[0-9A-F]{6}", d.strip()):
            return ("fill spelt %r: write fill:#XXXXXX (capitals, no space) - style.css and "
                    "haloed() read that spelling only" % d.strip())
        c = d.strip()[5:]
        if _lum(c) > .5 and c not in M.HALO_EXEMPT:
            return ("light text %s would get a light halo: list it in mapspine.HALO_EXEMPT "
                    "and style.css" % c)
    if decls:
        return None
    attr = re.search(r'(?<![\w-])fill\s*=\s*(["\'])(.*?)\1', a)
    if attr:
        c = _colour(attr.group(2))
        if c and _lum(c) > .5:
            return ("light fill=%r loses to the class rule (D-11) and draws dark: write "
                    "style=\"fill:%s\"" % (attr.group(2), c))
    return None


def _render(svg, scale):
    import cairosvg
    from PIL import Image
    png = cairosvg.svg2png(bytestring=svg.encode("utf-8"), scale=scale)
    return Image.open(io.BytesIO(png)).convert("RGB")


def _pixels(im, box):
    c = im.crop(box)
    return list(c.get_flattened_data()) if hasattr(c, 'get_flattened_data') else list(c.getdata())


def _unmarked(bare):
    """The bare figure with every thick stroke and every marker taken out."""
    def thin(m):
        w = float(m.group(1))
        return 'stroke-width="0"' if w > M.HALO_THIN else m.group(0)
    s = re.sub(r'stroke-width="([\d.]+)(?:px)?"', thin, bare)
    s = re.sub(r'stroke-width:\s*([\d.]+)(?:px)?',
               lambda m: 'stroke-width:0' if float(m.group(1)) > M.HALO_THIN else m.group(0), s)
    # arrowheads are marks too, and taking them out here also keeps cairosvg from a
    # zero-scale marker matrix on a path whose stroke-width was just set to 0
    s = re.sub(r'\smarker-(?:start|mid|end)="[^"]*"', '', s)
    return re.sub(r'<circle\b[^>]*\br="([\d.]+)"[^>]*?(?:/>|>\s*</circle>)',
                  lambda m: '' if float(m.group(1)) <= MARKER_R else m.group(0), s)


def _mask(quad, box, ox, oy, scale):
    """For a rotated text: which pixels of `box` lie inside its quad, shrunk a unit toward
    its centre as the box is. None when the quad is the box (not rotated, or by 90°)."""
    xs, ys = sorted({round(q[0], 3) for q in quad}), sorted({round(q[1], 3) for q in quad})
    if len(xs) <= 2 and len(ys) <= 2:
        return None
    from PIL import Image, ImageDraw
    cx, cy = sum(q[0] for q in quad) / 4, sum(q[1] for q in quad) / 4
    pts = []
    for px, py in quad:
        d = ((px - cx) ** 2 + (py - cy) ** 2) ** .5 or 1
        px, py = px - (px - cx) / d, py - (py - cy) / d
        pts.append(((px - ox) * scale - box[0], (py - oy) * scale - box[1]))
    m = Image.new("L", (box[2] - box[0], box[3] - box[1]), 0)
    ImageDraw.Draw(m).polygon(pts, fill=255)
    return list(m.get_flattened_data()) if hasattr(m, 'get_flattened_data') else list(m.getdata())


def crossings(svg, name, floor=0.03, scale=2, bare_mode=False):
    bare = re.sub(r'<text\b[^>]*>.*?</text>', '', svg, flags=re.S)
    vb = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"', svg)
    ox, oy = float(vb.group(1)), float(vb.group(2))
    im = _render(bare, scale)
    un = None if bare_mode else _render(_unmarked(bare), scale)
    W, H = im.size
    discs = [(float(a), float(b), float(r)) for a, b, r in re.findall(
        r'<circle cx="([\d.-]+)" cy="([\d.-]+)" r="([\d.]+)"', svg) if float(r) >= 4]
    # text_items(), not a second parser (review session 17): attrs carry the class and
    # text-anchor a <g> gives, and a rotated text brings its corners
    bad = []
    for it in M.text_items(svg):
        (x0, y0, x1, y1), t, a = it['box'], it['text'], it['attrs']
        lf = light_fault(a)
        if lf:
            print("   !! %s: %r: %s" % (name, t[:40], lf))
            bad.append((t[:40], 1.0))
            continue
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        if any((cx - p) ** 2 + (cy - q) ** 2 <= r * r for p, q, r in discs) and len(t) <= 2:
            continue
        # shrink the generous estimate a little: this is for real crossings
        bx0, bx1 = int((x0 - ox + 1) * scale), int((x1 - ox - 1) * scale)
        by0, by1 = int((y0 - oy + 1.5) * scale), int((y1 - oy - 0.5) * scale)
        bx0, by0 = max(bx0, 0), max(by0, 0)
        bx1, by1 = min(bx1, W), min(by1, H)
        if bx1 <= bx0 or by1 <= by0:
            continue
        box = (bx0, by0, bx1, by1)
        px = _pixels(im, box)
        keep = _mask(it['quad'], box, ox, oy, scale)
        if keep is not None:
            px = [p for p, k in zip(px, keep) if k]
            if not px:
                continue
        if bare_mode or not M.haloed(a):
            counts = {}
            for p in px:
                q = (p[0] // 6, p[1] // 6, p[2] // 6)
                counts[q] = counts.get(q, 0) + 1
            # two flat grounds (half on land, half on sea) is itself a crossing - unhaloed
            other = 1 - max(counts.values()) / len(px)
            why = "not one flat ground"
        else:
            qx = _pixels(un, box)
            if keep is not None:
                qx = [q for q, k in zip(qx, keep) if k]
            other = sum(1 for p, q in zip(px, qx) if max(abs(p[i] - q[i]) for i in range(3)) > 20) / len(px)
            why = "a thick line or a marker"
        if other > (floor if (bare_mode or not M.haloed(a)) else MARK_FLOOR):
            key = (name.split("/")[-1], t.strip())
            why_not = ON_PURPOSE.get(key)
            if why_not and not bare_mode:
                print("   = %s: on purpose: %r - %s" % (name, t[:40], why_not))
                continue
            if key in KNOWN_FALSE and not bare_mode:
                print("   = %s: measured wrong: %r - %s" % (name, t[:40], KNOWN_FALSE[key]))
                continue
            bad.append((t[:40], other))
            print("   ! %s: %s through the text (%.0f%% of its box): %r" % (name, why, 100 * other, t[:40]))
    return bad


if __name__ == "__main__":
    args = sys.argv[1:]
    bare_mode = "--bare" in args
    n = 0
    for p in [a for a in args if a != "--bare"]:
        src = open(p, encoding="utf-8").read()
        if p.endswith(".html"):
            # a body or a page: every inline figure in it, named by its place (Parts A-C
            # keep their figures here, with no svg_*.txt - review session 16)
            svgs = re.findall(r'<svg\b.*?</svg>', src, re.S)
            for k, svg in enumerate(svgs):
                if 'viewBox="' not in svg:
                    continue
                if "xmlns=" not in svg[:400]:     # inline in a page it needs none; cairosvg does
                    svg = svg.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"', 1)
                nm = "%s#svg%d" % (p, k + 1)
                try:
                    n += len(crossings(svg, nm, bare_mode=bare_mode))
                except Exception as e:           # say so, never skip in silence
                    print("   !! %s: not rendered, not read: %s" % (nm, str(e)[:80]))
                    n += 1
        else:
            n += len(crossings(src, p, bare_mode=bare_mode))
    print("%d text(s) crossed" % n)
