# -*- coding: utf-8 -*-
"""Territorial map 4 of 11: 1500. The union fraying; the duchies attached.

Same bbox, projection, palette and legend geometry as 1050, 1250 and 1397.

Three things changed in the western panel since 1397, and each is a decision:
  - Orkney and Shetland are GONE, pledged to Scotland in 1468-69 against a dowry
    that was never paid. They are simply not coloured.
  - Greenland drops from DEP to CLAIM. The Norse are gone; the claim is not.
  - Iceland and the Faroes stay DEP, still reached through Norway.

Sweden is drawn as held, because in 1500 it was: Hans was crowned in 1497 and
lost it again in 1501. The dashed edge and the note say so.
"""
import map_1397 as M97
import mapspine as M

CORE_OP = .62
DEP_OP = .30
CLAIM_OP = .42

DENMARK = M97.DENMARK
NORWAY = M97.NORWAY
SWEDEN = M97.SWEDEN
SLESVIG = M97.SLESVIG
GOTLAND = M97.GOTLAND          # Danish since 1449
BORNHOLM = M97.BORNHOLM

# Holstein: Eider to Elbe. Capped east of 10.6 so that Luebeck, a free imperial
# city and no part of Holstein, stays outside the polygon.
# The western edge stops at 9.35, because the marsh beyond it is Ditmarschen and
# Ditmarschen is exactly what Holstein did not hold.
HOLSTEN = [
    (9.35, 54.3133), (9.50, 54.32), (10.05, 54.45), (10.60, 54.42), (10.60, 53.95),
    (10.20, 53.60), (9.40, 53.55), (9.35, 53.90),
]

# Ditmarschen: claimed, invaded and not held. The army that went in on
# 17 February 1500 did not come out.
# North edge lies on Slesvig's southern edge - the Eider - rather than 3-4 km
# over it. Ditmarschen is south of the Eider; it was drawn north of it.
DITMARSKEN = [(8.68, 53.88), (9.35, 53.88), (9.35, 54.3133), (8.72, 54.2853)]

# ---------------------------------------------------------------- the west
GREENLAND = M97.GREENLAND
ICELAND = M97.ICELAND
FAROES = M97.FAROES
# ORKNEY and SHETLAND deliberately absent: pledged to Scotland 1468-69.

DK_SE = M97.DK_SE
NO_SE = M97.NO_SE
DK_SL = M97.DK_SL
SL_HO = [(8.60, 54.28), (9.20, 54.30), (9.50, 54.32), (10.05, 54.45)]


def build():
    f = M.frame()
    polys = M.land(50)
    out = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
           'aria-label="Territorial map of 1500. Denmark, Norway and Sweden under King Hans, with '
           'Sweden recovered in 1497 and lost again in 1501; the duchies of Schleswig and Holstein '
           'now held by the king himself; Ditmarschen claimed but not held; Gotland Danish. The '
           'western panel carries Iceland and the Faroes as dependencies and Greenland as a claim, '
           'while Orkney and Shetland have gone to Scotland.">' % (M.W, M.H),
           M.base(f, polys),
           M.graticule(f),
           M.clip_defs(f, polys)]

    for poly in (DENMARK, BORNHOLM, NORWAY):
        out.append(M.territory(f, poly, fill=M.CORE, opacity=CORE_OP))
    out.append(M.territory(f, GOTLAND, fill=M.CORE, opacity=CORE_OP))
    out.append(M.territory(f, SWEDEN, fill=M.CORE, opacity=CORE_OP))
    for poly in (SLESVIG, HOLSTEN):
        out.append(M.territory(f, poly, fill=M.DEP, opacity=DEP_OP, edge=M.DEP, dash="4 3"))
    out.append(M.territory(f, DITMARSKEN, fill=M.CLAIM, opacity=CLAIM_OP))

    for line in (DK_SE, NO_SE, DK_SL, SL_HO):
        d = f.path(line, close=False)
        if d:
            out.append('<path d="%s" fill="none" stroke="%s" stroke-width="1" '
                       'stroke-dasharray="3 3" opacity=".75"/>' % (d, M.PAPER))

    wf = M.west_frame()
    fills = [(GREENLAND, M.CLAIM, CLAIM_OP), (ICELAND, M.DEP, DEP_OP), (FAROES, M.DEP, DEP_OP)]
    out.append(M.western_panel(M.land(50), fills=fills))
    out.append('<text x="%d" y="%d" class="mapx" text-anchor="start">Orkney and Shetland '
               'pledged to Scotland, 1468\u201369</text>'
               % (M.WEST_BOX[0] + 4, M.WEST_BOX[1] + M.WEST_BOX[3] + 12))

    for lon, lat, t in [(9.3, 56.4, "DANMARK"), (8.6, 61.5, "NORGE"), (16.2, 60.6, "SVERIGE")]:
        out.append(M.note(f, lon, lat, t, cls="mapl"))
    for lon, lat, t, a in [(24.5, 62.5, "FINLAND", "middle"),
                           (9.6, 54.75, "Slesvig", "middle"),
                           (10.25, 53.80, "Holsten", "middle"),
                           (8.05, 54.05, "Ditmarsken", "end"),
                           (18.6, 57.5, "Gotland", "start")]:
        out.append(M.note(f, lon, lat, t, cls="mapt", anchor=a))

    for lon, lat, t, a in [(12.57, 55.68, "K\u00f8benhavn", "end"),
                           (12.62, 56.04, "Helsing\u00f8r", "start"),
                           (18.07, 59.33, "Stockholm", "start"),
                           (10.75, 59.91, "Oslo", "start"),
                           (8.87, 55.47, "Ribe", "end"),
                           (13.19, 55.70, "Lund", "start")]:
        out.append(M.dot(f, lon, lat, t, anchor=a))

    out.append(M.legend([("Ruled directly", M.CORE, CORE_OP),
                         ("Held by the king as duke", M.DEP, DEP_OP),
                         ("Claimed, not held", M.CLAIM, CLAIM_OP),
                         ("Sweden: taken 1497, lost 1501", None, 0)], x=14, y=196))
    out.append(M.note(f, 27.0, 54.6, "1500", cls="mapl", anchor="middle"))
    out.append('</svg>')
    return "\n  ".join(out)


if __name__ == "__main__":
    svg = build()
    open("svg_terr_1500.txt", "w", encoding="utf-8").write(svg)
    M.rasterise(svg, "look_1500.png")
    print("wrote svg_terr_1500.txt (%d chars)" % len(svg))
