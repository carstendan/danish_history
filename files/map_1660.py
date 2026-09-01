# -*- coding: utf-8 -*-
"""Territorial map 6 of 11: 1660. The realm Part G inherits.

Same bbox, projection, palette and legend geometry as 1050, 1250, 1397, 1500
and 1600.

Five decisions, each of which could have gone the other way:

  - THE YEAR IS 1660, NOT 1658. The spine list said 1658. Roskilde in February
    1658 took Bornholm and Trondhjem as well, and Copenhagen in May 1660 gave
    both back; a map dated 1658 therefore draws a settlement that lasted twenty
    months. 1660 draws the one that lasted. Bornholm is Danish here because the
    islanders made it so - chapter 24 - and Trondhjem is Norwegian again.

  - THE CEDED PROVINCES ARE DRAWN, in their own tone. The 1600 map leaves Sweden
    uncoloured to say the union is over, and that stays true: Sweden proper,
    Finland and the old Swedish mainland are still blank. But a map at the head
    of a part about what was left cannot be silent about what went. Skaane,
    Halland, Blekinge, Bohuslaen, Jaemtland, Haerjedalen, Gotland and Oesel carry
    LOST - drawn, outlined, and named with the year they went. Everything else
    Swedish stays uncoloured, so the tone means "ceded 1645-1658" and not
    "Sweden".

  - LOST IS A LOCAL COLOUR, not CLAIM. CLAIM is already on this map, on
    Greenland. Reusing oxblood for the ceded provinces would put two meanings on
    one fill in one legend. LOST is a muted ink-violet at low opacity with a
    dashed edge, defined here and not in mapspine, in the same way that 1600
    defines its own opacities.

  - THE DUCHIES STAY ONE COLOUR, for the reason the 1600 map gives: the 1544
    partition split revenue and not territory, and the shares were interleaved
    parish by parish. What changes is the legend. Since 1658 the ducal share is
    held sovereign rather than of the Danish crown, which is the whole of the
    Gottorp problem and is chapter 27's business.

  - GREENLAND STAYS CLAIM. Egede does not sail until 1721, which is where it
    becomes DEP.

The eastern boundary is defined ONCE, as SOUND, and used forward in DENMARK and
reversed in SCANIA. The same for NO_SE_1660 between Norway and the ceded
Norwegian provinces. Do not "tidy" them apart - that is the hairline the
Norway-Sweden border cost, and seamcheck.py exists because of it.
"""
import map_1397 as M97
import mapspine as M

CORE_OP = .62
DEP_OP = .30
CLAIM_OP = .42

LOST = "#6B5A78"          # ink-violet; not CLAIM, which Greenland is using
LOST_OP = .26

# ---------------------------------------------------------------- the seam
# The Sound and the Kattegat, south to north. Threaded between Helsingoer
# (12.615) and Helsingborg (12.694), and west of Kullen (12.45, 56.30) so that
# the headland falls to Sweden. Out in open water the line runs generously,
# because the fill is clipped to land and a wide sea boundary costs nothing.
SOUND = [
    (12.70, 54.60), (12.90, 55.20), (12.90, 55.55), (12.75, 55.85),
    (12.65, 56.05), (12.35, 56.25), (12.10, 57.20), (11.75, 57.72),
]

# Norway's new eastern edge: Bohuslaen gone in 1658, Jaemtland and Haerjedalen
# in 1645. South of Jaemtland the line runs near 12.1-12.5; north of it the
# border returns to the old vertices from 66 degrees up, which did not move.
NO_SE_1660 = [
    (11.45, 59.12), (11.80, 59.60), (12.05, 59.60), (12.55, 60.30),
    (12.35, 61.00), (12.45, 61.60), (12.15, 61.90), (12.05, 62.60),
    (12.15, 63.40), (13.60, 64.10), (14.55, 65.00), (15.55, 66.00),
]

# Norway's south-eastern closing edge and the ceded block's north-western one are
# the same two vertices. The first fixture run found eight land points on the
# Bohuslaen coast belonging to nobody, because the two rings closed on lines that
# were near each other and not the same. Do not tidy them apart.
BOHUS_NW = [(10.90, 59.20)]

# ---------------------------------------------------------------- territory
# Denmark: Jutland to the Kongeaa, the islands, and Bornholm. The Scanian
# provinces are gone. West and north the coast is 1397's, unchanged.
DENMARK = [
    (7.0, 55.25), (8.6, 55.25), (9.2, 55.35), (9.75, 55.48), (10.05, 55.10),
    (10.9, 54.60),
] + SOUND + [
    (11.60, 57.75), (10.70, 57.90), (9.50, 57.80), (8.00, 57.30), (7.00, 56.30),
]

# The ceded Danish provinces. Western edge is SOUND reversed, vertex for vertex.
# Eastern edge is the old Denmark-Sweden line from 1397, which is where the
# Scanian provinces always ended.
SCANIA = list(SOUND) + [
    (12.40, 57.55), (12.90, 57.45), (13.10, 57.10), (13.20, 56.60),
    (14.20, 56.55), (15.40, 56.45), (15.95, 56.05), (14.0, 55.30),
]

# Norway: Trondhjem restored 1660. Bohuslaen, Jaemtland and Haerjedalen gone.
NORWAY = list(NO_SE_1660) + [
    (16.35, 67.00), (18.15, 68.10), (20.25, 68.60), (21.90, 69.30), (25.00, 68.80),
    (26.00, 69.90), (28.00, 69.80), (30.50, 69.70), (31.00, 70.30), (31.00, 71.50),
    (3.00, 71.50), (0.50, 66.00), (1.80, 61.00), (3.20, 58.60), (5.00, 57.85),
    (7.05, 57.90), (9.00, 57.95),
] + BOHUS_NW

# The ceded Norwegian provinces: Bohuslaen 1658, Jaemtland and Haerjedalen 1645.
# Western edge is NO_SE_1660, vertex for vertex; eastern edge is 1397's Norway.
NO_LOST = list(NO_SE_1660) + [
    (14.35, 64.40), (15.45, 63.60), (14.65, 62.90),
    (14.95, 62.20), (14.60, 61.75), (13.05, 61.90), (12.45, 61.60), (12.35, 61.00),
    (12.55, 60.30), (12.05, 59.60), (11.65, 59.00), (11.95, 58.60),
    (12.05, 58.03), (11.92, 57.70), (11.75, 57.72),
    (11.20, 58.20), (10.95, 58.72),
] + BOHUS_NW

BORNHOLM = M97.BORNHOLM        # Danish again, May 1660, on the islanders' terms
SLESVIG = M97.SLESVIG

HOLSTEN = [
    (9.35, 54.3133), (9.50, 54.32), (10.05, 54.45), (10.60, 54.42), (10.60, 53.95),
    (10.20, 53.60), (9.40, 53.55), (9.35, 53.90),
]
DITMARSKEN = [(8.68, 53.88), (9.35, 53.88), (9.35, 54.3133), (8.72, 54.2853)]

GOTLAND = M97.GOTLAND          # Swedish since Broemsebro, 1645
OESEL = M97.box(21.78, 57.86, 22.95, 58.66)   # Swedish since 1645

# ---------------------------------------------------------------- the west
GREENLAND = M97.GREENLAND
ICELAND = M97.ICELAND
FAROES = M97.FAROES
# ORKNEY and SHETLAND still absent, and now for the fifth map running.

DK_SL = M97.DK_SL
SL_HO = [(8.60, 54.28), (9.20, 54.30), (9.50, 54.32), (10.05, 54.45)]


def build():
    f = M.frame()
    polys = M.land(50)
    out = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
           'aria-label="Territorial map of 1660. Denmark is Jutland, the islands and Bornholm; '
           'Norway keeps Trondhjem, restored in 1660. Skaane, Halland, Blekinge, Bohuslaen, '
           'Jaemtland, Haerjedalen, Gotland and Oesel are shown in a separate tone as provinces '
           'ceded to Sweden between 1645 and 1658. Sweden itself is a separate kingdom and is '
           'not coloured. Schleswig, Holstein and Ditmarschen are held as duchies, the ducal '
           'share sovereign since 1658. The western panel carries Iceland and the Faroes as '
           'dependencies and Greenland as a claim.">' % (M.W, M.H),
           M.base(f, polys),
           M.graticule(f),
           M.clip_defs(f, polys)]

    for poly in (DENMARK, BORNHOLM, NORWAY):
        out.append(M.territory(f, poly, fill=M.CORE, opacity=CORE_OP))
    for poly in (SLESVIG, HOLSTEN, DITMARSKEN):
        out.append(M.territory(f, poly, fill=M.DEP, opacity=DEP_OP, edge=M.DEP, dash="4 3"))
    for poly in (SCANIA, NO_LOST, GOTLAND, OESEL):
        out.append(M.territory(f, poly, fill=LOST, opacity=LOST_OP, edge=LOST, dash="2 3"))

    for line in (DK_SL,):
        d = f.path(line, close=False)
        if d:
            out.append('<path d="%s" fill="none" stroke="%s" stroke-width="1" '
                       'stroke-dasharray="3 3" opacity=".75"/>' % (d, M.PAPER))

    fills = [(GREENLAND, M.CLAIM, CLAIM_OP), (ICELAND, M.DEP, DEP_OP), (FAROES, M.DEP, DEP_OP)]
    out.append(M.western_panel(M.land(50), fills=fills))
    out.append('<text x="%d" y="%d" class="mapx" text-anchor="start">Greenland: still a claim, '
               'sixty years on</text>'
               % (M.WEST_BOX[0] + 4, M.WEST_BOX[1] + M.WEST_BOX[3] + 12))

    for lon, lat, t in [(9.3, 56.4, "DANMARK"), (7.9, 61.5, "NORGE")]:
        out.append(M.note(f, lon, lat, t, cls="mapl"))
    out.append(M.note(f, 17.5, 60.6, "SVERIGE", cls="mapt"))

    for lon, lat, t, a in [(24.5, 62.5, "FINLAND", "middle"),
                           (9.95, 54.95, "Slesvig", "middle"),
                           (10.05, 53.80, "Holsten", "middle"),
                           (14.15, 55.62, "Sk\u00e5ne", "middle"),
                           (12.95, 56.90, "Halland", "middle"),
                           (15.35, 56.08, "Blekinge", "middle"),
                           (11.95, 58.55, "Bohusl\u00e4n", "middle"),
                           (14.15, 63.35, "J\u00e4mtland", "middle"),
                           (13.65, 62.35, "H\u00e4rjedalen", "middle"),
                           (18.7, 57.5, "Gotland", "start"),
                           (14.90, 54.78, "Bornholm", "middle"),
                           (22.42, 57.72, "\u00d8sel", "middle")]:
        out.append(M.note(f, lon, lat, t, cls="mapt", anchor=a))

    for lon, lat, t, a, dx, dy in [(12.57, 55.68, "K\u00f8benhavn", "end", -5, 4),
                                   (12.615, 56.035, "Helsing\u00f8r", "end", -5, -4),
                                   (12.70, 56.05, "Helsingborg", "start", 6, 11),
                                   (10.75, 59.91, "Oslo", "start", 5, 3),
                                   (10.40, 63.43, "Trondhjem", "start", 5, 3),
                                   (9.56, 54.52, "Gottorp", "end", -5, 3)]:
        out.append(M.dot(f, lon, lat, t, anchor=a, dx=dx, dy=dy))

    out.append(M.legend([("Ruled directly", M.CORE, CORE_OP),
                         ("The duchies: ducal share sovereign since 1658", M.DEP, DEP_OP),
                         ("Ceded to Sweden 1645 and 1658", LOST, LOST_OP),
                         ("Sweden itself: not coloured", None, 0)], x=14, y=190))
    out.append(M.note(f, 27.9, 68.35, "no fixed border", cls="mapt", anchor="middle"))
    out.append(M.note(f, 27.0, 54.6, "1660", cls="mapl", anchor="middle"))
    out.append('</svg>')
    return "\n  ".join(out)


if __name__ == "__main__":
    svg = build()
    open("svg_terr_1660.txt", "w", encoding="utf-8").write(svg)
    M.rasterise(svg, "look_1660.png")
    print("wrote svg_terr_1660.txt (%d chars)" % len(svg))
