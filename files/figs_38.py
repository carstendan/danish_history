# -*- coding: utf-8 -*-
"""Figures for chapter 38.

FIGURE 1 — the two plebiscite zones, 10 February and 14 March 1920.

NOT DRAWN PARISH BY PARISH, and the reason is on the face of the figure as well
as here. PLAN_I §13 asked for a parish choropleth. The repo's only geography is
Natural Earth at 1:50m and 1:10m, which carries coastlines and nothing else — no
parish, commune or amt boundaries at any resolution. Drawing them by eye from a
printed historical map would be an invented measurement, and a polygon that is
wrong and self-consistent passes every check in this toolchain. So the zones are
drawn as they were legally defined — as areas bounded by three lines — and the
commune evidence is carried as dots, which needs no boundary data at all.

The design argument, which is also the chapter's: Zone I voted en bloc and Zone II
commune by commune, and that asymmetry decided the border before a vote was cast.
A choropleth would bury it under colour. Four German-majority towns inside the
zone that went to Denmark, and a zone that was one-fifth Danish going to Germany
with no Danish commune in it but three polling places on Før, is the whole of it.

SOURCED NUMBERS, and which of them survived a second appearance.
  Zone I, 10 February 1920
    75,431 Danish / 25,329 German, of 101,652 ballots cast, turnout 91.5 per cent
    74.9/25.1 is the share of VALID votes; 74.2/24.9 the share of all ballots.
    The 892-ballot gap between the two denominators is the spoiled papers.
  Zone II, 14 March 1920
    about 64,000 voted; about 80 per cent German; a German majority in every
    voting district but three small polling places on Før.
  Communes — CONFIRMED by two independent appearances agreeing digit for digit:
    Aabenraa    2,224 Danish / 2,725 German   (4,949 voting)
    Sønderborg  2,029 Danish / 2,601 German   (4,630 voting)
    Højer         219 Danish /   581 German   (  800 voting)
  Tønder — NOT CONFIRMED, and therefore carries no digits on the figure.
    One source gives 761 of 3,265, another 750 of 3,198. They disagree in both
    the numerator and the denominator, which is not a rounding difference. The
    town is marked as a German majority, because every source agrees it was the
    heaviest one, and the count is left off until the published returns settle it.

The three lines are drawn from the Clausen line as described — south of Tønder
and Tinglev, north of Flensburg — and from the zones' legal definition, not
traced from a scanned map. They are approximations of a legal boundary at a
scale where the line is about two pixels wide, and the caption says so. Every
dimension below is computed from the frame; none is typed.
"""

import mapspine as M

PAPER = "#F4F1EA"
INK    = "#2A2A28"
DK     = "#2E6B5E"          # the Danish side, as CORE elsewhere in the book
DE     = "#8C5A3C"
OX     = "#9A3B2E"


def fold(text, cls, x, avail):
    """Wrap to the width that actually fits, computed from CHAR_W for the class
    in use, with the fixed six-unit cushion mapspine asks for at the canvas edge
    rather than a percentage on the per-character width."""
    room = int((avail - x - 6) / M.CHAR_W[cls])
    out, line = [], ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > room:
            out.append(line); line = word
        else:
            line = (line + " " + word).strip()
    if line:
        out.append(line)
    return out


LEGEND_A = ("Zone 1 went to Denmark whole, carrying four German-voting towns with it. "
            "No commune in Zone 2 returned a Danish majority \u2014 three small polling "
            "places on F\u00f8r did, and stayed in Germany.")
LEGEND_B = ("Lines are the legal zone boundaries at a scale where the border is two "
            "pixels wide, not traced survey. T\u00f8nder is marked German and carries no "
            "count: two sources give 761 of 3.265 and 750 of 3.198, and they do not "
            "reconcile.")

# ------------------------------------------------------------------ figure 1
ZBOX  = (8.05, 54.35, 10.35, 55.55)
ZNEAR = (6.0, 53.0, 13.0, 57.5)

# The 1864 border along the Kongeå, from the North Sea to Kolding Fjord.
B1864 = [(8.20, 55.47), (8.62, 55.44), (9.05, 55.46), (9.38, 55.52), (9.62, 55.49)]

# The Zone I/II line: the Clausen line, south of Tønder and Tinglev, north of
# Flensburg, out into Flensburg Fjord. This is ALSO the 1920 border, and the
# figure says so with one line and two labels rather than two lines, because
# that identity is the point of the chapter.
ZLINE = [(8.42, 55.00), (8.88, 54.91), (9.24, 54.87), (9.47, 54.86), (9.72, 54.83),
         (10.02, 54.86)]

# Zone II's southern limit, the Husum–Schlei line.
ZSOUTH = [(8.85, 54.49), (9.30, 54.51), (9.66, 54.52), (10.05, 54.53)]

# name, lon, lat, danish, german, anchor.  danish None = counted, not confirmed.
TOWNS = [
    ("Haderslev",  9.49, 55.25, None, None, "start", DK),
    ("Aabenraa",   9.42, 55.04, 2224, 2725, "start", DE),
    ("Sønderborg", 9.79, 54.91, 2029, 2601, "start", DE),
    ("Tønder",     8.87, 54.94, None, None, "start", DE),
    ("Højer",      8.62, 54.99,  219,  581, "end",   DE),
    ("Flensborg",  9.44, 54.78, None, None, "start", DE),
    ("Slesvig",    9.57, 54.56, None, None, "start", DE),
]


def zones():
    W = 700
    mw, mh = 700, 470
    # HEIGHT IS COMPUTED. The legend wraps to whatever width the text needs, so
    # the canvas cannot be a typed number: the first version was 596 and the last
    # legend line fell 16 units off the bottom, which M.check() caught. Header 52,
    # map mh, 20 to the legend head, 15 to the first line, 13 per line, 3 between
    # the blocks, 14 of bottom margin.
    A = fold(LEGEND_A, "mapx", 14, W)
    B = fold(LEGEND_B, "mapx", 14, W)
    H = 52 + mh + 20 + 15 + 13 * len(A) + 3 + 13 * len(B) + 14
    f = M.detail_frame(ZBOX, mw, mh)
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Map of Slesvig showing the two plebiscite zones of 1920. Zone one, '
         'between the old 1864 border on the Kongeaa and a line running south of Toender '
         'and Tinglev and north of Flensburg, voted on 10 February as a single unit and '
         'returned about three-quarters for Denmark. Zone two, from that line south to a '
         'line between Husum and the Schlei, voted commune by commune on 14 March and '
         'returned about four-fifths for Germany. Four towns inside zone one returned '
         'German majorities and went to Denmark anyway.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="14" y="24" class="mapl">THE TWO ZONES, 1920</text>')
    o.append('<text x="14" y="40" class="mapt">one zone counted whole, one counted '
             'commune by commune — and that decided it</text>')
    o.append('<g transform="translate(0,52)">')
    o.extend(M.detail_base(f, mw, mh, ZNEAR, scale=10, clip="z20"))

    def band(top, bottom, fill, op):
        """A zone is the strip between two lines. Closed by running the upper line
        east and the lower line back west; no vertex is typed twice."""
        pts = list(top) + list(reversed(bottom))
        return '<path d="%s" fill="%s" fill-opacity="%s" stroke="none"/>' % (
            f.path(pts, close=True), fill, op)

    # CLIPPED TO LAND. The first render filled the North Sea and the Little Belt
    # with zone colour and read as one enormous quadrilateral laid over the map,
    # because a band closed between two lines has straight ends and detail_base,
    # unlike the territory maps, opens no land clip of its own. Nothing in the
    # toolchain can see this: validate() parses it, check() finds no collision and
    # no overrun, and the numbers on the face are all correct. It is visible in
    # the PNG and nowhere else, which is HANDOFF 47, 50, 61, 70 and 71 again.
    # AND EXTENDED PAST THE COAST AT BOTH ENDS BEFORE CLIPPING. A band closed
    # between two lines that stop at the coast has straight diagonal ends, and on
    # the first clipped render that diagonal cut Als out of Zone 1 - the island
    # voted on 10 February and Sønderborg is on it. Als falling out of a polygon
    # because an outline was drawn generously enough for the mainland and not for
    # the island is HANDOFF 78, four days old, in a new figure. The ends now run
    # well out to sea and the land clip decides where the colour stops, which is
    # the only arrangement in which no island can be lost by accident.
    def out_w(pts, west, east):
        return [west] + list(pts) + [east]

    # The eastern end runs down the Little Belt, not straight out to lon 10.6.
    # Extending east on a single point put FUNEN inside Zone 1 - the band's top
    # edge sits at lat 55.45 and Funen begins at 55.049, so a horizontal
    # extension swallows it. Als and Funen overlap in longitude (Als reaches
    # 10.060, Funen begins at 9.859), so no cutoff meridian separates them and
    # the closure has to follow the water. Checked by point-in-polygon against
    # the atlas rings, not by eye: every Als vertex in, every Funen vertex out.
    BELT = [(9.72, 55.35), (9.80, 55.10), (10.10, 54.95), (10.26, 54.88)]
    band_1864 = [(7.70, 55.47)] + list(B1864) + BELT
    band_zone = [(7.70, 55.04)] + list(ZLINE) + [(10.30, 54.85)]
    band_south = [(7.70, 54.47)] + list(ZSOUTH) + [(10.40, 54.54)]

    lp = M.detail_land_path(f, M.land(10), ZNEAR, mw, mh)
    o.append('<clipPath id="z20land"><path d="%s"/></clipPath>' % lp)
    o.append('<g clip-path="url(#z20land)">')
    o.append(band(band_1864, band_zone, DK, ".38"))
    o.append(band(band_zone, band_south, DE, ".34"))
    o.append('</g>')

    def line(pts, col, w, dash=None, op="1"):
        d = f.path(pts, close=False)
        a = ' stroke-dasharray="%s"' % dash if dash else ''
        return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s" opacity="%s"%s '
                'stroke-linejoin="round"/>' % (d, col, w, op, a))

    o.append(line(B1864, INK, "1.6", dash="6 4", op=".8"))
    o.append(line(ZSOUTH, INK, "1.3", dash="3 3", op=".65"))
    o.append(line(ZLINE, OX, "2.6"))

    # town dots, with the confirmed counts and without the unconfirmed one
    for name, lo, la, da, de, anc, col in TOWNS:
        x, y = f.xy(lo, la)
        dx = 5.5 if anc == "start" else -5.5
        o.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="%s"/>' % (x, y, col))
        # name above the dot where the count hangs below it, so a town with a
        # count occupies one block instead of two that can meet a neighbour's.
        ny = y - 7.0 if da is not None else y + 3.0
        o.append('<text x="%.1f" y="%.1f" class="mapx" text-anchor="%s" fill="%s">%s</text>'
                 % (x + dx, ny, anc, INK, name))
        if da is not None:
            o.append('<text x="%.1f" y="%.1f" class="mapx" text-anchor="%s" fill="%s">'
                     '%s dansk · %s tysk</text>'
                     % (x + dx, ny + 11.0, anc, col,
                        "{:,}".format(da).replace(",", "."),
                        "{:,}".format(de).replace(",", ".")))

    # zone labels, placed off the frame's own geometry rather than by eye
    for lo, la, head, sub, col in (
            (8.55, 55.22, "ZONE 1 · 10 February",
             "counted en bloc · 75.431 dansk, 25.329 tysk", DK),
            (8.60, 54.66, "ZONE 2 · 14 March",
             "counted commune by commune · about 80 pct. tysk", DE)):
        x, y = f.xy(lo, la)
        o.append('<text x="%.1f" y="%.1f" class="mapt" fill="%s">%s</text>' % (x, y, col, head))
        o.append('<text x="%.1f" y="%.1f" class="mapx" fill="%s">%s</text>'
                 % (x, y + 12, col, sub))

    # TWO groups are open here, not one: the translate wrapper above and the
    # clip group detail_base opens and documents that the caller must close.
    # Closing one left the legend inside the map clip and produced an SVG that
    # validate() rejected before anything reached disk.
    o.append('</g></g>')

    # legend strip, below the clipped map group
    ly = 52 + mh + 20
    o.append('<text x="14" y="%d" class="mapt" fill="%s">the red line is both the zone '
             'boundary and the border. That is the argument.</text>' % (ly, OX))
    y = ly + 15
    for ln in A:
        o.append('<text x="14" y="%d" class="mapx">%s</text>' % (y, ln)); y += 13
    y += 3
    for ln in B:
        o.append('<text x="14" y="%d" class="mapx" opacity=".75">%s</text>' % (y, ln)); y += 13
    o.append('</svg>')
    return "\n  ".join(o)


FIGS = [("svg_zoner_1920.txt", zones)]

if __name__ == "__main__":
    for name, fn in FIGS:
        svg = fn()
        M.validate(svg, name)
        for bad in (M.check(svg, name) or []):
            print("  !! %s" % (bad,))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
