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
        out.append("M" + " L".join("%.1f %.1f" % q for q in pts) + " Z")
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


def overruns(svg, name):
    """Left-anchored text whose estimated width runs past the viewBox. Caught by
    eye four times in Part F before it was written down."""
    import re
    w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
    bad = [m.group(2)[:44] for m in
           re.finditer(r'<text x="([\d.]+)"(?![^>]*text-anchor="(?:end|middle)")[^>]*>([^<]*)<',
                       svg)
           if float(m.group(1)) + len(m.group(2)) * 6.1 > w - 6]
    for t in bad:
        print("   ! %s: text may overrun the canvas: %s" % (name, t))
    return bad



def overflows(svg, name):
    """Text whose baseline falls below the viewBox. overruns() tests width only,
    and nothing tested height until chapter 29's stavnsband figure shipped its
    last caption line cut off at y=430 in a 430-high canvas. The automated guard
    could not see it and neither could the XML validator; only rasterising and
    looking did. This is that check, so it does not depend on looking."""
    import re
    m = re.search(r'viewBox="0 0 [\d.]+ ([\d.]+)"', svg)
    h = float(m.group(1))
    bad = [t.group(2)[:44] for t in
           re.finditer(r'<text[^>]*\by="([\d.]+)"[^>]*>([^<]*)<', svg)
           if float(t.group(1)) > h - 4]
    for t in bad:
        print("   ! %s: text below the bottom of the canvas: %s" % (name, t))
    return bad

def emit(svg, name, png=None):
    """validate, check, write, rasterise. The one entry point figure scripts use."""
    validate(svg, name)
    overruns(svg, name)
    overflows(svg, name)
    open(name, "w", encoding="utf-8").write(svg)
    rasterise(svg, png or "look_" + name.replace("svg_", "").replace(".txt", ".png"))
    print("wrote %s (%d chars)" % (name, len(svg)))


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
    test = svg.replace(">", ">" + css, 1)
    cairosvg.svg2png(bytestring=test.encode("utf-8"), write_to=path,
                     output_width=1320, background_color=PAPER)
