# -*- coding: utf-8 -*-
"""The eleven territorial maps: one bbox, one projection, one legend, one palette.

Also the shared helpers for the Denmark-scale thematic maps each chapter carries
on top of its spine map - see "detail maps" at the foot of this file.

Decision (Band D): one wide frame for all eleven, sized so the Kalmar Union and
Denmark-Norway are honest. Denmark comes out small - about 100px on the page -
and that is accepted: each entry carries its own Denmark-scale thematic map on
top, which is what the index promises anyway.

Palette and text classes follow the entries. The SVG carries no <style> of its
own; .mapt/.mapl/.mapx are styled by the page stylesheet, as in entries 01-11.
"""
import math
import re

from mapkit import load_land, Frame, simplify

# ---------------------------------------------------------------- palette
SEA        = "#B9CDD6"   # drawn at .7, as in entry 11
LAND       = "#D6DBCE"
LAND_EDGE  = "#9CA294"
CORE       = "#2E6B5E"   # ruled directly
DEP        = "#2E6B5E"   # dependency / vassal, lower opacity
CLAIM      = "#8A2B2B"
INK        = "#3C3E36"
PAPER      = "#F0F2EE"
GRAT       = "#A9B7BC"

# ---------------------------------------------------------------- the halo
# REVIEW SESSION 16. Every figure placed its labels at a point whatever lay under them,
# and linecheck.py's first reading found about 214 of its 220 flags real: coastlines,
# borders and routes through town and territory names in all 31 figures it listed.
# Carsten chose a halo (28 September 2026): every .mapt/.mapl/.mapx text is painted
# over a thin stroke of paper, so a thin line under a label stops at the letters. It
# lives in style.css as one rule, which every page carries; these constants are the
# same numbers, for rasterise() and linecheck.py.
#
# A light text (on a bar, a marker, a dark tint) takes no halo. HALO_EXEMPT lists the
# light fills in use, and ON_BAR_INK, the one dark ink kept for text on a mid-grey bar
# (three bars on pages 01-03, #8E9182, where white reaches only 3.2:1 - D-11's companion
# rule asks 4.5); style.css exempts exactly these, spelt style="fill:#XXXXXX"
# in capitals - an attribute selector matches the spelling, not the colour. A fill="..."
# ATTRIBUTE is no use: by D-11 the class rule beats it and the text draws dark. Fourteen
# bar labels on pages 01-03 were written fill="#FFF" and had shipped dark on dark bars;
# they are style="fill:#FFFFFF" now. A NEW LIGHT COLOUR MUST BE ADDED TO BOTH LISTS;
# linecheck.py reports a light text that would get a light halo, and a light fill=.
#
# The halo does not help a THICK line (a route, an attack line, a heavy border: wider
# than HALO_THIN) or a marker through a label. Those still show between the letters,
# and the label is moved. See linecheck.py.
HALO_W      = 2.6        # px, the whole stroke: 1.3 each side of the glyph
HALO_OP     = ".8"
HALO_COL    = PAPER
ON_BAR_INK  = "#1C1B18"   # dark text set on a mid-grey bar, where white is 3.2:1 and this 5.3:1
HALO_EXEMPT = ("#F0F2EE", "#FFFFFF", "#F4F1EA", ON_BAR_INK)
HALO_THIN   = 1.4        # a stroke this wide or less is hidden by the halo


def haloed(attrs):
    """True if a <text> with these attributes takes the halo in style.css."""
    if not re.search(r'class="map[tlx]"', attrs):
        return False
    return not any(('fill:%s' % c) in attrs for c in HALO_EXEMPT)


def halo_underlay(svg):
    """FOR RASTERS ONLY. cairosvg ignores paint-order and paints the stroke over the
    letters, so a PNG made from the page's rule would show washed-out text the page
    never shows. Emulate it: a stroked copy of each haloed text, drawn first. Never
    write the result into a figure - the page does this with one CSS rule."""
    def rep(m):
        if not haloed(m.group(1)):
            return m.group(0)
        a = re.sub(r'\s(?:fill|style)="[^"]*"', '', m.group(1))
        return ('<text%s style="fill:none;stroke:%s;stroke-opacity:%s;stroke-width:%spx;'
                'stroke-linejoin:round">%s</text>%s'
                % (a, HALO_COL, HALO_OP, HALO_W, m.group(2), m.group(0)))
    return re.sub(r'<text\b([^>]*)>(.*?)</text>', rep, svg, flags=re.S)

# ---------------------------------------------------------------- geometry
# Shetland (Norwegian until 1468) is left outside the frame and noted in the
# caption on the years where it matters; carrying it cost 18% of the width.
BBOX = (3.0, 53.0, 31.0, 71.5)
W, H = 660, 700

_CACHE = {}


def land(scale):
    if scale not in _CACHE:
        tol = 0.013 if scale == 10 else 0.05
        _CACHE[scale] = [simplify(p, tol) for p in load_land("package/land-%dm.json" % scale)]
    return _CACHE[scale]


def frame():
    return Frame(*BBOX, W, H, pad=0)


# ---------------------------------------------------------------- drawing
def base(f, polys, sea=True):
    out = []
    if sea:
        out.append('<rect x="0" y="0" width="%d" height="%d" fill="%s" opacity=".7"/>' % (W, H, SEA))
    out.append('<path d="%s" fill="%s" stroke="%s" stroke-width=".8"/>'
               % (f.land_path(polys), LAND, LAND_EDGE))
    return "\n  ".join(out)


def graticule(f, lons=(5, 10, 15, 20, 25, 30), lats=(55, 60, 65, 70)):
    lo0, la0, lo1, la1 = BBOX
    out = []
    for lo in lons:
        d = f.path([(lo, la0 + (la1 - la0) * i / 40) for i in range(41)], close=False)
        if d:
            out.append('<path d="%s" fill="none" stroke="%s" stroke-width=".5" opacity=".55"/>' % (d, GRAT))
    for la in lats:
        d = f.path([(lo0 + (lo1 - lo0) * i / 40, la) for i in range(41)], close=False)
        if d:
            out.append('<path d="%s" fill="none" stroke="%s" stroke-width=".5" opacity=".55"/>' % (d, GRAT))
    return "\n  ".join(out)


def clip_defs(f, polys, cid="landclip"):
    return '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (cid, f.land_path(polys))


def territory(f, poly, fill=CORE, opacity=.55, cid="landclip", edge=None, dash=None):
    d = f.path(poly, close=True)
    if not d:
        return ""
    a = ' stroke="%s" stroke-width="1.3"' % edge if edge else ' stroke="none"'
    if dash:
        a += ' stroke-dasharray="%s"' % dash
    return ('<g clip-path="url(#%s)"><path d="%s" fill="%s" fill-opacity="%s"%s/></g>'
            % (cid, d, fill, opacity, a))


def dot(f, lon, lat, name, anchor="start", cls="mapx", dx=None, dy=None, r=2.4):
    x, y = f.xy(lon, lat)
    dx = dx if dx is not None else (4.5 if anchor == "start" else (-4.5 if anchor == "end" else 0))
    dy = dy if dy is not None else (-5 if anchor == "middle" else 3.2)
    return ('<circle cx="%.1f" cy="%.1f" r="%s" fill="%s"/>'
            '<text x="%.1f" y="%.1f" class="%s" text-anchor="%s">%s</text>'
            % (x, y, r, INK, x + dx, y + dy, cls, anchor, name))


def note(f, lon, lat, text, cls="mapl", anchor="middle"):
    x, y = f.xy(lon, lat)
    return '<text x="%.1f" y="%.1f" class="%s" text-anchor="%s">%s</text>' % (x, y, cls, anchor, text)


def legend(items, x=18, y=None):
    """items: (label, fill, opacity); fill None draws the label alone."""
    y = y if y is not None else H - 20 - 17 * len(items)
    out = []
    for i, (lab, fill, op) in enumerate(items):
        yy = y + i * 17
        if fill:
            out.append('<rect x="%d" y="%d" width="19" height="10.5" fill="%s" fill-opacity="%s" '
                       'stroke="%s" stroke-width="1"/>' % (x, yy - 9, fill, op, fill))
        out.append('<text x="%d" y="%d" class="mapx">%s</text>' % (x + 26, yy, lab))
    return "\n  ".join(out)


# ---------------------------------------------------------------- western panel
# The conic projection wastes the top-left corner: the geographic box's NW corner
# lands at x=166, and its left edge is still at x=122 by y=199. The panel sits in
# that dead wedge, and it points in the direction the territory actually lies.
#
# These places reach Denmark THROUGH NORWAY, so they take DEP, never CORE.
#
# Greenland needs deciding per map, not once:
#   1397  DEP    - Norse Eastern Settlement still inhabited
#   1500  CLAIM  - claimed, nobody there; the Norse are gone
#   1600  CLAIM  - same
#   1721  DEP    - Hans Egede lands, and it is a possession again
# Getting that wrong is the Bohuslaen error in a colder place.
WEST_BBOX = (-48.0, 58.0, 0.0, 67.5)
WEST_BOX = (6, 22, 158, 88)          # x, y, w, h on the main canvas


def west_frame():
    return Frame(*WEST_BBOX, WEST_BOX[2], WEST_BOX[3], pad=0)


def western_panel(polys, fills=(), label="THE WESTERN REALM"):
    """fills: list of (poly, colour, opacity). Empty draws the panel with no territory,
    which is the point on 1050 and 1250 - the box is there and nothing is in it."""
    x, y, w, h = WEST_BOX
    wf = west_frame()
    land = wf.land_path(polys, min_pts=2)
    out = ['<g transform="translate(%d,%d)">' % (x, y),
           '<rect x="0" y="0" width="%d" height="%d" fill="%s" opacity=".7"/>' % (w, h, SEA),
           '<clipPath id="wclip"><rect x="0" y="0" width="%d" height="%d"/></clipPath>' % (w, h),
           '<g clip-path="url(#wclip)">',
           '<path d="%s" fill="%s" stroke="%s" stroke-width=".6"/>' % (land, LAND, LAND_EDGE)]
    if fills:
        out.append('<clipPath id="wland"><path d="%s"/></clipPath>' % land)
        for poly, col, op in fills:
            d = wf.path(poly, close=True)
            if d:
                out.append('<g clip-path="url(#wland)"><path d="%s" fill="%s" fill-opacity="%s" '
                           'stroke="%s" stroke-width="1"/></g>' % (d, col, op, col))
    out.append('</g>')
    out.append('<rect x="0" y="0" width="%d" height="%d" fill="none" stroke="%s" '
               'stroke-width="1"/>' % (w, h, INK))
    out.append('<text x="4" y="-4" class="mapt">%s</text>' % label)
    out.append('</g>')
    return "\n  ".join(out)


# ---------------------------------------------------------------- detail maps
# For the Denmark-scale thematic map each chapter carries on top of the spine map.
#
# These exist because mapkit.land_path runs Sutherland-Hodgman per ring, and where
# a ring exits and re-enters the frame it walks the frame edge from the exit point
# to the re-entry point. On the spine frame that is harmless. On a closer frame
# whose western edge sits in open water it bridges the Eurasian ring across the
# mouth of the North Sea and prints the sea as land - which looked entirely
# plausible until it was rasterised.
#
# The fix is to project each ring whole and let an SVG clip do the trimming, so
# no ring is ever rewritten to follow a frame edge. Whole rings are expensive
# (the Eurasian one runs to Kamchatka), so points far from the view are thinned:
# the ring stays closed, and the detail is kept where it can be seen.

def detail_frame(bbox, w, h):
    return Frame(*bbox, w, h, pad=0)


def _thin_far(ring, near, every=25):
    lo0, la0, lo1, la1 = near
    return [(x, y) for i, (x, y) in enumerate(ring)
            if (lo0 <= x <= lo1 and la0 <= y <= la1) or i % every == 0]


def detail_land_path(f, polys, near, w, h):
    """near is a generous lon/lat window around the view: rings with no point in
    it are dropped, and points outside it are thinned."""
    lo0, la0, lo1, la1 = near
    out = []
    for ring in polys:
        if len(ring) < 4 or not any(lo0 <= x <= lo1 and la0 <= y <= la1 for x, y in ring):
            continue
        pts = [f.xy(*q) for q in _thin_far(ring, near)]
        xs = [q[0] for q in pts]
        ys = [q[1] for q in pts]
        if max(xs) < -60 or min(xs) > w + 60 or max(ys) < -60 or min(ys) > h + 60:
            continue
        # NEGATIVE ZERO. "%.1f" % -0.00004 is "-0.0" and "%.1f" % 0.00004 is
        # "0.0", so a coordinate that rounds to nothing carries the sign of the
        # float underneath it - and that sign can differ between platforms for
        # the same input. It made map_1814.py emit 109,561 characters in one
        # place and 109,569 in another from identical source, which looked like
        # a mystery until the first differing character turned out to be a minus.
        # Adding 0.0 after rounding collapses -0.0 to 0.0; it is the only
        # non-determinism in the whole map pipeline.
        out.append("M" + " L".join("%.1f %.1f" % (round(a, 1) + 0.0, round(b, 1) + 0.0)
                                   for a, b in pts) + " Z")
    return " ".join(out)


def detail_base(f, w, h, near, scale=10, clip="fr"):
    """Opens a clipped group. The caller must close it with </g> before drawing
    anything that should sit outside the map area, such as a legend strip."""
    return ['<defs><clipPath id="%s"><rect x="0" y="0" width="%d" height="%d"/></clipPath></defs>'
            % (clip, w, h),
            '<g clip-path="url(#%s)">' % clip,
            '<rect x="0" y="0" width="%d" height="%d" fill="%s" opacity=".7"/>' % (w, h, SEA),
            '<path d="%s" fill="%s" stroke="%s" stroke-width=".8"/>'
            % (detail_land_path(f, land(scale), near, w, h), LAND, LAND_EDGE)]


def validate(svg, name):
    """Parse before writing. A bare & in a label produces a file that looks fine
    in the editor and fails at the rasteriser, after it has already been saved.
    Lifted here from figs_23.py: it was added after the incident and only to the
    two scripts written afterwards, leaving five figures written unchecked."""
    import xml.etree.ElementTree as ET
    try:
        ET.fromstring(svg)
    except ET.ParseError as e:
        line = svg.splitlines()[e.position[0] - 1][:120]
        raise SystemExit("!! %s is not well-formed XML at line %d: %s"
                         % (name, e.position[0], line))


# Advance width per character, in user units, PER CLASS. Measured in Sept 2026 by
# rendering a known string through rasterise() and reading the ink bounding box,
# rather than assumed: mapt 5.68, mapx 5.63, mapl 6.98. The single constant 6.1
# that stood here before was conservative for the two small classes and 13 per
# cent TOO SMALL for mapl, so a long heading could run off the canvas without
# being flagged. The values below carry roughly a tenth of slack above the
# measurement, because a guard that under-estimates is worse than one that nags.
#
# If style.css changes a font-size or the --mono stack, re-measure. Do not adjust
# these by eye.
# THE MEASURED VALUES, with no percentage margin on top, because a percentage
# margin on a per-character estimate compounds with line length: at 5.95 a
# 149-character line in svg_titles.txt accumulated forty units of phantom
# width and was reported as overrunning a canvas it fits inside. The cushion
# belongs at the canvas edge instead, where it is a fixed six units and does
# not grow with the sentence. Regression: the two-column collision in
# figs_32.py still fires at these values, and it is the fault this exists for.
#
# MEASURED IN THE PAGE (review session 17), NOT APPLIED: HANDOFF item 105 is still Carsten's
# decision, because every fold() that reads CHAR_W re-wraps (19 figures in Part I). In
# Chromium, every figure text on all 45 pages as they stood (2,903; rendered width over
# length, the median per class): mapt 6.07, mapx 5.43, mapl 6.92 - what style.css asks
# for, a monospace advance of about 0.6 em plus the class's letter-spacing (9.5 x .64,
# 8.5 x .64, 10.5 x .66). At the table's 5.68, about 6 per cent short, page 23's invasions
# caption shipped cut at "both tim" and overruns() passed it (fixed in figs_23 by
# wrapping). At the page values the guards list one more near miss, 02's third map
# caption, which reads.
CHAR_W = {'mapl': 6.98, 'mapt': 5.68, 'mapx': 5.63}
CHAR_H = {'mapl': 10.5, 'mapt': 9.5, 'mapx': 8.5}
DEFAULT_W, DEFAULT_H = 6.3, 9.5
# --------------------------------------------------------------- contrast
# Convention D-11 says a figure sets text colour with style=, never fill=,
# because a stylesheet rule beats a presentation attribute and .mapt/.mapl/.mapx
# all carry one. D-11 fixes the MECHANISM. It does not say WHICH colour, and the
# chapter 42 session found that the difference matters: of the twenty near-white
# labels that the dead fill= attribute was suppressing, honouring the request
# would have FIXED eleven and MADE NINE WORSE.
#
# The reason is that figure grounds are drawn at opacity, so the colour a label
# actually sits on is the fill composited over what is under it - a slate rect at
# .75 over paper is #778890, not #4F6470 - and near-white on that is 3.27:1,
# under the floor. Nothing in the project computed that; the colours were chosen
# by eye against the raw constant.
#
# 10.5px at weight 600 is NOT WCAG large text (that needs 18.66px bold), so the
# threshold here is 4.5:1 and not 3:1.
INK_DARK = "#221E18"       # the darkest ink already in the palette


def _srgb(h):
    c = [int(h[i:i + 2], 16) / 255.0 for i in (1, 3, 5)]
    return [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]


def luminance(h):
    r, g, b = _srgb(h)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    """WCAG contrast ratio between two #rrggbb colours."""
    la, lb = luminance(a), luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def composite(fill, opacity=1.0, under=PAPER):
    """The colour a label actually sits on: fill drawn at opacity over `under`."""
    f = [int(fill[i:i + 2], 16) for i in (1, 3, 5)]
    u = [int(under[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02X%02X%02X" % tuple(
        int(round(opacity * f[i] + (1 - opacity) * u[i])) for i in range(3))


def text_on(fill, opacity=1.0, under=PAPER, floor=4.5):
    """Pick the label colour with the better contrast against a composited ground.

    Returns (colour, ratio). The caller decides what to do when the ratio is
    under `floor` - this does not silently pick an unreadable colour, and it does
    not assert, because two shipped grounds cannot reach 4.5 with any ink in the
    palette and refusing to draw them is not the answer.
    """
    bg = composite(fill, opacity, under)
    best = max((contrast(c, bg), c) for c in (PAPER, INK_DARK))
    return best[1], best[0]

TEXT_RE = re.compile(r'<text x="([\d.-]+)" y="([\d.-]+)"[^>]*?'
                     r'(?:class="([a-z]+)")?[^>]*>([^<]*)</text>')


def _class_of(tag):
    """The first CHAR_W class name in a tag's class attribute, or None."""
    c = [k for k in (_attr(tag, 'class') or '').split() if k in CHAR_W]
    return c[0] if c else None


def _attr(tag, name):
    """An attribute's value by its whole name - not data-x for x, not data-class for class
    (check 2 of review session 17) - or None."""
    m = re.search(r'(?<![\w-])%s="([^"]*)"' % re.escape(name), tag)
    return m.group(1) if m else None


def text_items(svg):
    """Every <text> as a dict: box (x0, y0, x1, y1), quad (its four corners, which differ
    from the box only when the text is rotated), cls, text, attrs. text_boxes() is the boxes.

    Boxes are estimates. The anchor decides which side of x the string sits on;
    the vertical extent is taken as three quarters of the font size above the
    baseline and a quarter below, which is close enough for overlap testing and
    deliberately generous.

    WHAT THE PAGE INHERITS, THIS INHERITS (review session 17). Until then a text was measured
    by its own attributes only, and three kinds were measured wrong or not at all:
      - a text with markup inside (a <tspan>, italic for a title or a Danish word) was
        skipped - five in four figures, never checked by collisions(), overruns(),
        overflows() or linecheck.py. Now the markup is stripped and the string measured
        (every <tspan> in the book only changes the style, not the position);
      - a rotated text (transform="rotate(a cx cy)", 08's timeline and svg_cell's "6
        paces") was measured flat. Now the box is the rotated rectangle's bounding box,
        and quad carries its corners (linecheck reads the quad, not the box: a -30 degree
        label's box is mostly empty paper and the ruled lines beside it);
      - a class or a text-anchor set on an enclosing <g> was not seen, so 06's "the great
        majority" was measured from the wrong side (text-anchor="end" on its <g>) and the
        texts in <g class="mapx"> groups (01-03, 06, 09) at the default width and as
        unhaloed. Now the nearest <g> that sets one is used, as the browser does.
    Also now: entities count as one character (&amp; drew as "&" and was measured as five),
    and whitespace is collapsed as SVG draws it (a leading space takes no room).
    Still not read: a font-size set in style (Part D's serif titles, 15-34px, are measured
    at the default size); on a <g>, any transform but one translate(); on a <text>, anything
    but ONE rotate() or ONE translate() - "translate(5,5) rotate(-30)" is measured flat; dx
    and dy; a <tspan> with its own x or y (none of these is in the book, review session 17).
    A class with more than one name, say class="big mapl", is SIZED by its first map class,
    but haloed() and linecheck.py want class="mapl" exactly and read it as unhaloed.
    """
    import html as _html
    # TEXT INSIDE A TRANSFORMED GROUP IS IN A DIFFERENT COORDINATE SPACE, and the
    # first version of this ignored that and reported the 1807 figure's subtitle
    # as colliding with a label 52 units below it on the map. Panels here are
    # wrapped in a single <g transform="translate(dx,dy)">, so track that one form
    # and apply it. Anything more elaborate is not produced by this project, and
    # if it ever is, this needs to grow rather than to guess.
    # a self-closed <g .../> opens nothing (check 1 of review session 17: it leaked its class)
    events = [(m.start(), m.group(0), m.group(1)) for m in re.finditer(r'<g\b([^>]*)>|</g>', svg)
              if not m.group(0).endswith('/>')]

    def context_at(i):
        """(dx, dy, class, text-anchor) that the enclosing <g>s give a text at offset i."""
        stack = []
        for st, tag, attrs in events:
            if st > i:
                break
            if tag == '</g>':
                if stack:
                    stack.pop()
            else:
                stack.append(attrs or '')
        dx = dy = 0.0
        cls = anchor = None
        for attrs in stack:                      # outermost first; the nearest wins
            t = re.fullmatch(r'\s*translate\(\s*([-\d.]+)(?:[,\s]+([-\d.]+))?\s*\)\s*',
                             _attr(attrs, 'transform') or '')
            if t:
                dx += float(t.group(1))
                dy += float(t.group(2) or 0)
            # only a text class is inherited: a <g class="land"> inside a <g class="mapx">
            # does not change the letters' font, which CSS inherits from the mapx group
            cls = _class_of(attrs) or cls
            anchor = _attr(attrs, 'text-anchor') or anchor
        return dx, dy, cls, anchor

    out = []
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', svg, re.S):
        attrs = m.group(1)
        # collapse as SVG does: ASCII whitespace only (a no-break space keeps its width)
        txt = ' '.join(t for t in re.split(r'[ \t\r\n]+', _html.unescape(re.sub(r'<[^>]+>', '', m.group(2))))
                       if t)
        mx = re.fullmatch(r'\s*([-\d.]+)\s*', _attr(attrs, 'x') or '')
        my = re.fullmatch(r'\s*([-\d.]+)\s*', _attr(attrs, 'y') or '')
        if not (mx and my and txt):
            continue
        gdx, gdy, gcls, ganchor = context_at(m.start())
        x, y = float(mx.group(1)), float(my.group(1))
        cls = _class_of(attrs) or gcls
        cw = CHAR_W.get(cls, DEFAULT_W)
        ch = CHAR_H.get(cls, DEFAULT_H)
        w = len(txt) * cw
        anchor = _attr(attrs, 'text-anchor') or ganchor or 'start'
        if anchor == 'end':
            x0, x1 = x - w, x
        elif anchor == 'middle':
            x0, x1 = x - w / 2.0, x + w / 2.0
        else:
            x0, x1 = x, x + w
        y0, y1 = y - ch * 0.75, y + ch * 0.25
        quad = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        tf = _attr(attrs, 'transform')
        if tf:
            r = re.match(r'\s*rotate\(\s*([-\d.]+)(?:[,\s]+([-\d.]+)[,\s]+([-\d.]+))?\s*\)\s*$',
                         tf)
            t = re.match(r'\s*translate\(\s*([-\d.]+)(?:[,\s]+([-\d.]+))?\s*\)\s*$', tf)
            if r:
                a = math.radians(float(r.group(1)))
                cx, cy = float(r.group(2) or 0), float(r.group(3) or 0)
                ca, sa = math.cos(a), math.sin(a)
                quad = [(cx + (px - cx) * ca - (py - cy) * sa, cy + (px - cx) * sa + (py - cy) * ca)
                        for px, py in quad]
            elif t:
                tx, ty = float(t.group(1)), float(t.group(2) or 0)
                quad = [(px + tx, py + ty) for px, py in quad]
        quad = [(px + gdx, py + gdy) for px, py in quad]
        xs, ys = [q[0] for q in quad], [q[1] for q in quad]
        eff = attrs
        if gcls and not _class_of(attrs):
            eff += ' class="%s"' % gcls
        if ganchor and _attr(attrs, 'text-anchor') is None:
            eff += ' text-anchor="%s"' % ganchor
        out.append({'box': (min(xs), min(ys), max(xs), max(ys)), 'quad': quad, 'cls': cls,
                    'text': txt, 'attrs': eff})
    return out


def text_boxes(svg):
    """Every <text> as (x0, y0, x1, y1, cls, string): text_items()' boxes (see there for
    what is inherited from a <g>, rotation, and markup)."""
    return [it['box'] + (it['cls'], it['text']) for it in text_items(svg)]


def overruns(svg, name):
    """Text whose estimated width runs past the viewBox. Caught by eye four times
    in Part F before it was written down. Now per-class; see CHAR_W."""
    # Tolerate a viewBox with a non-zero origin. Every figure this project ships
    # starts at "0 0", but check() now runs from rasterise() on whatever it is
    # handed, including a cropped copy made to inspect one corner - and crashing
    # on the inspection is a poor way to reward someone for looking.
    vb = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"', svg)
    if not vb:
        return []
    ox, w = float(vb.group(1)), float(vb.group(1)) + float(vb.group(3))
    # THE LEFT EDGE TOO (review session 16). Item 49 recorded that this "tests the right
    # edge and the bottom, not the left" (the bottom is in fact overflows()). Moving
    # Hvalsey's label to the left of its dot in figs_16b put "a wedding, 16 Sept 1408"
    # about 20 units off the canvas (x0 -19.7), and nothing fired.
    # Past the edge, not near it. (This said a rotated text is measured unrotated and
    # svg_cell's vertical "6 paces" would read as starting at 0.1; since review session 17
    # a rotated text is measured by its rotated box, and "6 paces" starts at 12.9.)
    bad = [t[:44] for (x0, y0, x1, y1, cls, t) in text_boxes(svg) if x1 > w - 6 or x0 < ox]
    for t in bad:
        print("   ! %s: text may overrun the canvas: %s" % (name, t))
    return bad


def collisions(svg, name, pad=1.0):
    """Two pieces of text printing through each other.

    THIS GUARD EXISTS BECAUSE overruns() CANNOT SEE THIS. In Sept 2026 the
    assemblies figure was laid out in two columns at x=26 and x=380; the left
    column ran to x=423 and printed straight through the right one, and every
    check passed, because 423 is inside a 700-wide canvas. It was found by
    looking at the raster, which is not a method that scales to 51 figures.

    Overlap is only reported when boxes intersect on BOTH axes by more than pad,
    so labels that merely sit close, or share a line, are left alone.

    A ROTATED TEXT IS TESTED BY ITS CORNERS (review session 17): its box, the bounding box
    of a -30 degree label, is mostly paper, and 08's timeline would report seven pairs of
    neighbours that never touch. Where either text is rotated the two quads are tested on
    their own axes (separating axes) and the overlap reported is the smallest depth.
    """
    items = text_items(svg)
    bad = []
    for i in range(len(items)):
        ax0, ay0, ax1, ay1 = items[i]['box']
        at = items[i]['text']
        for j in range(i + 1, len(items)):
            bx0, by0, bx1, by1 = items[j]['box']
            bt = items[j]['text']
            ox = min(ax1, bx1) - max(ax0, bx0)
            oy = min(ay1, by1) - max(ay0, by0)
            if not (ox > pad and oy > pad):
                continue
            if _rotated(items[i]['quad']) or _rotated(items[j]['quad']):
                ox = _depth(items[i]['quad'], items[j]['quad'])
                if ox <= pad:
                    continue
            bad.append((at[:34], bt[:34], ox))
    for a, b, ox in bad:
        print("   ! %s: text collides (%.0f units): %r over %r" % (name, ox, a, b))
    return bad


def _rotated(quad):
    """True if a quad's edges are not on the axes (a text rotated by other than 90°)."""
    return len({round(q[0], 3) for q in quad}) > 2 or len({round(q[1], 3) for q in quad}) > 2


def _depth(p, q):
    """How far two convex quads overlap: the smallest overlap of their projections on the
    edge normals of either (0 if some axis separates them)."""
    best = float('inf')
    for poly in (p, q):
        for k in range(4):
            (x1, y1), (x2, y2) = poly[k], poly[(k + 1) % 4]
            nx, ny = y1 - y2, x2 - x1
            n = math.hypot(nx, ny) or 1.0
            nx, ny = nx / n, ny / n
            a = [x * nx + y * ny for x, y in p]
            b = [x * nx + y * ny for x, y in q]
            best = min(best, min(max(a), max(b)) - max(min(a), min(b)))
            if best <= 0:
                return 0.0
    return best



def overflows(svg, name):
    """Text whose baseline falls below the viewBox. overruns() tests width only,
    and nothing tested height until chapter 29's stavnsband figure shipped its
    last caption line cut off at y=430 in a 430-high canvas. The automated guard
    could not see it and neither could the XML validator; only rasterising and
    looking did. This is that check, so it does not depend on looking."""
    # Same tolerance as overruns, and the same reason. Also: this now measures
    # against the BOTTOM OF THE TEXT BOX rather than the baseline, and counts
    # transformed groups, so a line whose descenders fall off the edge is caught
    # even though its baseline sits inside. That is what svg_invasions.txt had.
    # THE TOP EDGE TOO (review session 17). Nothing tested it; a label rotated to rise from
    # its baseline (08's timeline, at -30 degrees) is the likely way to lose one there now
    # that text_items() measures rotation. Within 2 units, as the bottom is tested.
    vb = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"', svg)
    if not vb:
        return []
    oy = float(vb.group(2))
    h = oy + float(vb.group(4))
    bad = []
    for (x0, y0, x1, y1, cls, t) in text_boxes(svg):
        if y1 > h - 2:
            bad.append(t[:44])
            print("   ! %s: text below the bottom of the canvas: %s" % (name, t[:44]))
        elif y0 < oy + 2:          # the bottom's margin: a Danish capital's ring rises past
                                   # the 0.75 em box (check 2 of review session 17)
            bad.append(t[:44])
            print("   ! %s: text above the top of the canvas: %s" % (name, t[:44]))
    return bad

def emit(svg, name, png=None):
    """validate, check, write, rasterise. The one entry point figure scripts use."""
    validate(svg, name)
    overruns(svg, name)
    overflows(svg, name)
    open(name, "w", encoding="utf-8").write(svg)
    rasterise(svg, png or "look_" + name.replace("svg_", "").replace(".txt", ".png"))
    print("wrote %s (%d chars)" % (name, len(svg)))


def check(svg, name):
    """Every automated guard, in one call, run before anything is written.

    THE GUARDS WERE ONLY EVER WIRED INTO THE FIGURE SCRIPTS. `figs_23` through
    `figs_32` call validate and overruns; the eleven map scripts call neither, so
    no territorial map in the series has ever been width-checked. That is how
    `svg_terr_1660.txt` came to ship with Helsingborg and Skaane printed into each
    other, found in Sept 2026 by a collision guard written the same afternoon.

    Call this from rasterise(), which every script already calls, and do it BEFORE
    the cairosvg availability test - otherwise the checks are skipped on exactly
    the machine that has no rasteriser and therefore cannot look instead.
    """
    validate(svg, name)
    return overruns(svg, name) + overflows(svg, name) + collisions(svg, name)


def rasterise(svg, path, extra=""):
    """Write a PNG for visual inspection. NOT needed to build a page.

    cairosvg wants the cairo C library, which is a separate install on macOS and is
    not there by default. It used to raise ImportError on the last line of every
    figure script, after the .txt had been written but before the loop reached the
    next figure - so a run half succeeded and looked like a total failure.

    Missing cairosvg is now a loud warning, not a stop. The .txt files are written
    either way and the build only needs those. But the standing rule is that every
    figure is looked at before it ships, and this is the step that makes that
    possible: if you see this warning, inspect the SVGs another way. mapdump.py
    builds an HTML contact sheet that opens in a browser and needs no cairo.
    """
    check(svg, path)
    try:
        import cairosvg
    except ImportError:
        if not getattr(rasterise, "_warned", False):
            print("   !! cairosvg not installed: no PNGs written, figures NOT visually checked.")
            print("      To install:  brew install cairo && pip3 install cairosvg")
            print("      Or inspect in a browser:  python3 mapdump.py")
            rasterise._warned = True
        return
    css = ('<style>'
           '.mapt{font-family:monospace;font-size:9.5px;fill:#5F6157;letter-spacing:.04em}'
           '.mapl{font-family:monospace;font-size:10.5px;fill:#3C3E36;letter-spacing:.06em;font-weight:600}'
           '.mapx{font-family:monospace;font-size:8.5px;fill:#4A4C44;letter-spacing:.04em}'
           + extra + '</style>')
    # the page's halo, as a raster can show it
    test = halo_underlay(svg).replace(">", ">" + css, 1)
    cairosvg.svg2png(bytestring=test.encode("utf-8"), write_to=path,
                     output_width=1320, background_color=PAPER)
