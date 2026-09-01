# -*- coding: utf-8 -*-
"""Territorial map 5 of 11: 1600. The realm the settlement of 1536 handed on.

Same bbox, projection, palette and legend geometry as 1050, 1250, 1397 and 1500.

Four decisions, each of which could have gone the other way:

  - SWEDEN IS NOT DRAWN. It has been a separate kingdom since 1523, and 1570
    settled that in law even while both kings went on quartering three crowns.
    Drawing it would say the union was dormant; leaving it uncoloured says it was
    over. The envelope in mapfixture.py is narrowed to match, because Sweden is
    now as much "not this map's business" as Poland or Scotland.

  - THE DUCHIES ARE ONE COLOUR, not three. The partition of 1544 divided the
    revenue and not the territory: each brother's third was assembled from
    districts scattered the length of both duchies, interleaved parish by parish.
    There is no honest way to draw that as three areas, and drawing it as three
    areas would be a map of something that did not exist. One fill, a note, and
    the chapter's second figure carries the interleaving.

  - DITMARSCHEN IS IN. Conquered in June 1559 by Johan Rantzau, fifty-nine years
    after the army that went in at Hemmingstedt did not come out. It was divided
    in three like everything else, so it takes the same fill as the duchies -
    where on the 1500 map it was CLAIM, and correctly so.

  - GREENLAND STAYS CLAIM, per the table in mapspine.py. The Norse are a century
    gone; the claim is not, and it is worth something in 1721.

Oesel is drawn because the Northern Seven Years' War is unintelligible without
it: Denmark bought the bishopric in 1559, and the quarrel that looked like
heraldry was about who held the eastern Baltic ports. Held until 1645.
"""
import map_1397 as M97
import mapspine as M

CORE_OP = .62
DEP_OP = .30
CLAIM_OP = .42

DENMARK = M97.DENMARK
NORWAY = M97.NORWAY
BORNHOLM = M97.BORNHOLM
GOTLAND = M97.GOTLAND          # Danish since 1449, and still Danish in 1600
SLESVIG = M97.SLESVIG

# Holstein as on the 1500 map: Eider to Elbe, capped east of 10.6 so that
# Luebeck, a free imperial city, stays outside.
HOLSTEN = [
    (9.35, 54.3133), (9.50, 54.32), (10.05, 54.45), (10.60, 54.42), (10.60, 53.95),
    (10.20, 53.60), (9.40, 53.55), (9.35, 53.90),
]

# Ditmarschen: no longer CLAIM. Taken in 1559 and split three ways.
# North edge lies on Slesvig's southern edge - the Eider - rather than 3-4 km
# over it. Ditmarschen is south of the Eider; it was drawn north of it.
DITMARSKEN = [(8.68, 53.88), (9.35, 53.88), (9.35, 54.3133), (8.72, 54.2853)]

# Oesel / Saaremaa. Bought for Duke Magnus in 1559 out of the wreck of the
# Teutonic Order; Danish until Broemsebro in 1645.
# Eastern edge at 23.05 caught a strip of the Estonian mainland; 22.95 keeps
# Saaremaa and Muhu, which belonged with it, and drops the mainland.
OESEL = M97.box(21.78, 57.86, 22.95, 58.66)

# ---------------------------------------------------------------- the west
GREENLAND = M97.GREENLAND
ICELAND = M97.ICELAND
FAROES = M97.FAROES
# ORKNEY and SHETLAND still absent, and now for the fourth map running.

DK_SE = M97.DK_SE
NO_SE = M97.NO_SE
DK_SL = M97.DK_SL
SL_HO = [(8.60, 54.28), (9.20, 54.30), (9.50, 54.32), (10.05, 54.45)]


def build():
    f = M.frame()
    polys = M.land(50)
    out = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
           'aria-label="Territorial map of 1600. Denmark and Norway are ruled by one king, with '
           'Skaane, Halland, Blekinge, Bornholm and Gotland Danish. Schleswig, Holstein and '
           'Ditmarschen are held as duchies, divided since 1544 into three interleaved revenue '
           'shares rather than three territories. Oesel in the eastern Baltic is Danish from '
           '1559. Sweden is a separate kingdom and is not coloured. The western panel carries '
           'Iceland and the Faroes as dependencies and Greenland as a claim; Orkney and '
           'Shetland are gone.">' % (M.W, M.H),
           M.base(f, polys),
           M.graticule(f),
           M.clip_defs(f, polys)]

    for poly in (DENMARK, BORNHOLM, GOTLAND, NORWAY):
        out.append(M.territory(f, poly, fill=M.CORE, opacity=CORE_OP))
    for poly in (SLESVIG, HOLSTEN, DITMARSKEN):
        out.append(M.territory(f, poly, fill=M.DEP, opacity=DEP_OP, edge=M.DEP, dash="4 3"))
    out.append(M.territory(f, OESEL, fill=M.DEP, opacity=DEP_OP, edge=M.DEP, dash="4 3"))

    for line in (DK_SE, NO_SE, DK_SL):
        d = f.path(line, close=False)
        if d:
            out.append('<path d="%s" fill="none" stroke="%s" stroke-width="1" '
                       'stroke-dasharray="3 3" opacity=".75"/>' % (d, M.PAPER))

    fills = [(GREENLAND, M.CLAIM, CLAIM_OP), (ICELAND, M.DEP, DEP_OP), (FAROES, M.DEP, DEP_OP)]
    out.append(M.western_panel(M.land(50), fills=fills))
    out.append('<text x="%d" y="%d" class="mapx" text-anchor="start">Greenland: a claim, '
               'nobody there</text>'
               % (M.WEST_BOX[0] + 4, M.WEST_BOX[1] + M.WEST_BOX[3] + 12))

    for lon, lat, t in [(9.3, 56.4, "DANMARK"), (8.6, 61.5, "NORGE")]:
        out.append(M.note(f, lon, lat, t, cls="mapl"))
    out.append(M.note(f, 16.2, 60.6, "SVERIGE", cls="mapt"))
    out.append(M.note(f, 16.2, 60.05, "a separate kingdom", cls="mapt"))
    for lon, lat, t, a in [(24.5, 62.5, "FINLAND", "middle"),
                           (9.95, 54.95, "Slesvig", "middle"),
                           (10.05, 53.80, "Holsten", "middle"),
                           (18.7, 57.5, "Gotland", "start"),
                           (14.90, 54.78, "Bornholm", "middle"),
                           (22.42, 57.72, "\u00d8sel", "middle")]:
        out.append(M.note(f, lon, lat, t, cls="mapt", anchor=a))

    # The Sound is about 12px wide at this frame and carries three labels, so
    # each is pushed to a different quadrant of its dot rather than left to the
    # default. They collided on the first rasterisation.
    for lon, lat, t, a, dx, dy in [(12.57, 55.68, "K\u00f8benhavn", "end", -5, 4),
                                   (12.62, 56.04, "Helsing\u00f8r", "start", 5, -4),
                                   (12.70, 55.90, "Hven", "start", 5, 9),
                                   (10.75, 59.91, "Oslo", "start", 5, 3),
                                   (9.56, 54.52, "Gottorp", "end", -5, 3)]:
        out.append(M.dot(f, lon, lat, t, anchor=a, dx=dx, dy=dy))

    lx, ly = f.xy(8.02, 54.05)
    tx, ty = f.xy(8.86, 54.12)
    out.append('<path d="M %.1f %.1f L %.1f %.1f" fill="none" stroke="%s" stroke-width=".8" '
               'opacity=".8"/>' % (lx + 3, ly - 3, tx, ty, M.INK))
    out.append('<circle cx="%.1f" cy="%.1f" r="1.6" fill="%s"/>' % (tx, ty, M.INK))
    out.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="end">Ditmarsken</text>'
               % (lx, ly))

    out.append(M.legend([("Ruled directly", M.CORE, CORE_OP),
                         ("The duchies: king and dukes together", M.DEP, DEP_OP),
                         ("Divided 1544 by revenue, not by land", None, 0),
                         ("Sweden: separate since 1523", None, 0)], x=14, y=196))
    out.append(M.note(f, 27.9, 68.35, "no fixed border", cls="mapt", anchor="middle"))
    out.append(M.note(f, 27.0, 54.6, "1600", cls="mapl", anchor="middle"))
    out.append('</svg>')
    return "\n  ".join(out)


if __name__ == "__main__":
    svg = build()
    open("svg_terr_1600.txt", "w", encoding="utf-8").write(svg)
    M.rasterise(svg, "look_1600.png")
    print("wrote svg_terr_1600.txt (%d chars)" % len(svg))
