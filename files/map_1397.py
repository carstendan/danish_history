# -*- coding: utf-8 -*-
"""Territorial map 3 of 11: the Kalmar Union, 1397.

Same bbox, projection, palette and legend geometry as map_1050 and map_1250.
This is the first map on which the western panel carries anything: Iceland, the
Faroes, Orkney, Shetland and the Norse Eastern Settlement in Greenland all reach
Denmark THROUGH NORWAY, so they take DEP, never CORE.

Every polygon is verified by point-in-polygon test in verify_1397.py, not by eye.
The 1050 map swallowed Bohuslaen and looked perfectly fine.
"""
import mapspine as M

CORE_OP = .62
DEP_OP = .30
CLAIM_OP = .42

# ---------------------------------------------------------------- territory
# Denmark: the kingdom proper. Southern limit is the Kongeaa, which reaches the
# Wadden Sea below Ribe and rises east to Vamdrup - so Ribe is in, Haderslev is
# not. Eastern limit runs up the Halland-Smaaland border; Bohuslaen is Norwegian
# and Vaestergoetland's corridor to the sea at the Goeta aelv is Swedish.
DENMARK = [
    (7.0, 55.25), (8.6, 55.25), (9.2, 55.35), (9.75, 55.48), (10.05, 55.10),
    (10.9, 54.60), (12.7, 54.60), (14.0, 55.30), (15.95, 56.05), (15.40, 56.45),
    (14.20, 56.55), (13.20, 56.60), (13.10, 57.10), (12.90, 57.45), (12.40, 57.55),
    (11.92, 57.70), (11.60, 57.75), (10.70, 57.90), (9.50, 57.80), (8.00, 57.30), (7.00, 56.30),
]

# Schleswig: a Danish fief, held since 1386 by the counts of Holstein. Kongeaa to
# Eider, Als included, Kiel and Rendsburg outside.
# The northern edge is DENMARK's southern edge, vertex for vertex - 8.60, 9.20 and
# 9.75 are copied from it and must not be "tidied" apart. They disagreed until
# August 2026: Slesvig ran to (9.85, 55.50) against Denmark's (9.75, 55.48), and
# Denmark's (8.60, 55.25) sat 5 km inside Slesvig. The lens between the two lines
# was up to 27 km wide, and because both fills are translucent it printed as a
# dark stripe across Jutland on this map, on 1500 and on 1600. The coverage sweep
# cannot see a fault shaped like that at any affordable grid; seamcheck.py can.
SLESVIG = [
    (8.10, 55.25), (8.60, 55.25), (9.20, 55.35), (9.75, 55.48),
    (9.98, 55.05), (10.00, 54.88),
    (10.15, 54.55), (10.05, 54.45), (9.50, 54.32), (8.60, 54.28), (8.10, 54.55),
]

# Norway: mainland, with Bohuslaen down to the Goeta aelv and the bulge east
# around Haerjedalen and Jaemtland. North of Jaemtland the border returns west.
# The Haerjedalen stretch - (14.60,61.75) and (14.95,62.20) - was corrected in
# August 2026. It formerly cut the corner at a single (14.45,62.20), which put
# Sveg and Ytterhogdal in SWEDEN two and a half centuries before Broemsebro, on
# 1397, 1500 and 1600 alike. The border was SHARED EXACTLY and simply drawn in
# the wrong place, so the seam layer and the coverage sweep both passed it, and
# the curated Haerjedalen case sat at 13.50 - in the western half, inside the
# line either way. These are map_1660.py's NO_LOST vertices for the same ground.
NORWAY = [
    (11.92, 57.70), (12.05, 58.03), (11.95, 58.60), (11.65, 59.00), (12.05, 59.60),
    (12.55, 60.30), (12.35, 61.00), (12.45, 61.60), (13.05, 61.90), (14.60, 61.75), (14.95, 62.20),
    (14.65, 62.90), (15.45, 63.60), (14.35, 64.40), (14.55, 65.00), (15.55, 66.00),
    (16.35, 67.00), (18.15, 68.10), (20.25, 68.60), (21.90, 69.30), (25.00, 68.80),
    (26.00, 69.90), (28.00, 69.80), (30.50, 69.70), (31.00, 70.30), (31.00, 71.50),
    (3.00, 71.50), (0.50, 66.00), (1.80, 61.00), (3.20, 58.60), (5.00, 57.85),
    (7.05, 57.90), (9.00, 57.95), (11.00, 58.00),
]

# Sweden: kingdom and Finland. Western edge follows Norway's; Gotland is cut out
# and Oeland is kept; the eastern limit runs behind Vyborg.
# The first twenty vertices are NORWAY's, copied exactly. Do not "tidy" them
# apart: the fixture's sweep reports the resulting sliver as unclaimed land.
SWEDEN = [
    (11.92, 57.70), (12.05, 58.03), (11.95, 58.60), (11.65, 59.00), (12.05, 59.60),
    (12.55, 60.30), (12.35, 61.00), (12.45, 61.60), (13.05, 61.90), (14.60, 61.75), (14.95, 62.20),
    (14.65, 62.90), (15.45, 63.60), (14.35, 64.40), (14.55, 65.00), (15.55, 66.00),
    (16.35, 67.00), (18.15, 68.10), (20.25, 68.60), (21.90, 69.30), (25.00, 68.80),
    (27.50, 68.50), (29.50, 67.50), (30.50, 66.00), (31.00, 64.00), (31.00, 62.00),
    (30.00, 61.00), (28.50, 60.50), (27.00, 60.40), (24.00, 59.80), (22.00, 59.60),
    (21.00, 59.00), (19.30, 59.60), (18.60, 59.20), (18.00, 58.60), (17.40, 57.50),
    (17.00, 56.40), (15.95, 56.05), (15.40, 56.45), (14.20, 56.55), (13.20, 56.60),
    (13.10, 57.10), (12.90, 57.45), (12.40, 57.55),
]

# Bornholm: Danish, held by the archbishop of Lund since the twelfth century.
BORNHOLM = [(14.62, 54.95), (15.25, 54.95), (15.25, 55.40), (14.62, 55.40)]

# Gotland: Mecklenburg's, then the Teutonic Order's from 1398. Claimed from
# Kalmar, bought and not delivered, and not handed over until 1408.
GOTLAND = [(17.95, 56.80), (19.55, 56.80), (19.55, 58.10), (17.95, 58.10)]

# ---------------------------------------------------------------- the west
# These are lon/lat boxes, but the panel is a conic projection over 48 degrees of
# longitude, so a box drawn from four corners comes out as a diagonal slash across
# Greenland. Every edge is densified before projection.
def densify(verts, n=24):
    out = []
    for i in range(len(verts)):
        a, b = verts[i], verts[(i + 1) % len(verts)]
        for k in range(n):
            out.append((a[0] + (b[0] - a[0]) * k / n, a[1] + (b[1] - a[1]) * k / n))
    return out


def box(lon0, lat0, lon1, lat1, n=24):
    pts = []
    for i in range(n + 1):
        pts.append((lon0 + (lon1 - lon0) * i / n, lat0))
    for i in range(n + 1):
        pts.append((lon1, lat0 + (lat1 - lat0) * i / n))
    for i in range(n + 1):
        pts.append((lon1 - (lon1 - lon0) * i / n, lat1))
    for i in range(n + 1):
        pts.append((lon0, lat1 - (lat1 - lat0) * i / n))
    return pts


# One ring, not two boxes: overlapping translucent fills print a darker seam.
# The eastern edge steps out at 66.8N - which clears Grimsey, the northernmost
# scrap of Iceland, by a quarter-degree - so the ring takes the whole north-east
# coast without touching Iceland anywhere.
GREENLAND = densify([(-56.0, 55.0), (-24.80, 55.0), (-24.80, 66.80),
                     (-20.00, 66.80), (-20.00, 72.0), (-56.0, 72.0)])
ICELAND = box(-25.5, 62.5, -12.5, 67.2)
FAROES = box(-7.90, 61.20, -6.10, 62.60)
SHETLAND = box(-2.10, 59.60, -0.40, 61.10)
# Orkney's south limit is South Ronaldsay at 58.72N; Dunnet Head, the top of the
# Scottish mainland, is 58.67N. Scotland was never in the union, so this edge
# matters more than its two pixels suggest.
ORKNEY = box(-3.60, 58.71, -2.20, 59.45)


# ---------------------------------------------------------------- internal lines
# The union is one fill; these dashed lines carry the internal geography, which
# the series has been careful about for fifteen chapters.
DK_SE = [(12.40, 57.55), (12.90, 57.45), (13.10, 57.10), (13.20, 56.60),
         (14.20, 56.55), (15.40, 56.45), (15.95, 56.05)]
NO_SE = [(11.95, 57.70), (12.05, 58.05), (11.95, 58.60), (11.65, 59.00),
         (12.05, 59.60), (12.55, 60.30), (12.35, 61.00), (12.45, 61.60),
         (13.05, 61.90), (14.60, 61.75), (14.95, 62.20), (14.65, 62.90), (15.45, 63.60),
         (14.35, 64.40), (14.55, 65.00), (15.55, 66.00), (16.35, 67.00),
         (18.15, 68.10), (20.25, 68.60)]
DK_SL = [(8.10, 55.25), (8.60, 55.25), (9.20, 55.35), (9.75, 55.48)]


def build():
    f = M.frame()
    polys = M.land(50)
    out = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
           'aria-label="Territorial map of the Kalmar Union in 1397. Denmark, Norway and '
           'Sweden with Finland are ruled by one crowned king, Erik of Pomerania, with Queen '
           'Margrete governing. Schleswig is held of the Danish crown by the counts of '
           'Holstein. Gotland is claimed but held by others. A panel at the upper left shows '
           'the North Atlantic dependencies reached through Norway: Greenland\'s Eastern '
           'Settlement, Iceland, the Faroes, Shetland and Orkney.">' % (M.W, M.H),
           M.base(f, polys),
           M.graticule(f),
           M.clip_defs(f, polys)]

    for poly in (DENMARK, BORNHOLM, NORWAY, SWEDEN):
        out.append(M.territory(f, poly, fill=M.CORE, opacity=CORE_OP))
    out.append(M.territory(f, SLESVIG, fill=M.DEP, opacity=DEP_OP, edge=M.DEP, dash="4 3"))
    out.append(M.territory(f, GOTLAND, fill=M.CLAIM, opacity=CLAIM_OP))

    for line in (DK_SE, NO_SE, DK_SL):
        d = f.path(line, close=False)
        if d:
            out.append('<path d="%s" fill="none" stroke="%s" stroke-width="1" '
                       'stroke-dasharray="3 3" opacity=".75"/>' % (d, M.PAPER))

    # western panel: everything here is held through Norway, so DEP throughout
    wf = M.west_frame()
    wpolys = [p for p in M.land(50)]
    fills = [(GREENLAND, M.DEP, DEP_OP), (ICELAND, M.DEP, DEP_OP),
             (FAROES, M.DEP, DEP_OP), (SHETLAND, M.DEP, DEP_OP),
             (ORKNEY, M.DEP, DEP_OP)]
    out.append(M.western_panel(wpolys, fills=fills))
    out.append('<text x="%d" y="%d" class="mapx" text-anchor="start">through Norway</text>'
               % (M.WEST_BOX[0] + 4, M.WEST_BOX[1] + M.WEST_BOX[3] + 12))

    # names
    for lon, lat, t in [(9.15, 56.55, "DANMARK"), (8.6, 61.5, "NORGE"), (16.2, 60.6, "SVERIGE")]:
        out.append(M.note(f, lon, lat, t, cls="mapl"))
    for lon, lat, t, a in [(24.5, 62.5, "FINLAND", "middle"),
                           (13.0, 56.1, "Sk\u00e5ne", "middle"),
                           (12.6, 56.9, "Halland", "middle"),
                           (11.6, 58.4, "Bohusl\u00e4n", "middle"),
                           (14.2, 63.3, "J\u00e4mtland", "middle"),
                           (8.30, 54.75, "Slesvig", "end")]:
        out.append(M.note(f, lon, lat, t, cls="mapt", anchor=a))

    for lon, lat, t, a in [(12.57, 55.68, "K\u00f8benhavn", "end"),
                           (16.36, 56.66, "Kalmar", "start"),
                           (18.07, 59.33, "Stockholm", "start"),
                           (10.75, 59.91, "Oslo", "start"),
                           (9.44, 54.78, "Flensborg", "start"),
                           (18.30, 57.63, "Visby", "start")]:
        out.append(M.dot(f, lon, lat, t, anchor=a))

    # legend goes in the open Norwegian Sea, not on Jutland: at this frame
    # Denmark is about 110px and anything laid over it is laid over the country
    out.append(M.legend([("Three kingdoms, one king", M.CORE, CORE_OP),
                         ("Held of the Danish crown", M.DEP, DEP_OP),
                         ("Claimed, held by others", M.CLAIM, CLAIM_OP),
                         ("Internal borders", None, 0)], x=14, y=196))
    out.append(M.note(f, 27.9, 68.35, "no fixed border", cls="mapt", anchor="middle"))
    out.append(M.note(f, 27.0, 54.6, "1397", cls="mapl", anchor="middle"))
    out.append('</svg>')
    return "\n  ".join(out)


if __name__ == "__main__":
    svg = build()
    open("svg_terr_1397.txt", "w", encoding="utf-8").write(svg)
    M.rasterise(svg, "look_1397.png")
    print("wrote svg_terr_1397.txt (%d chars) and look_1397.png" % len(svg))
