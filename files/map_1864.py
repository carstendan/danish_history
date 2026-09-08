# -*- coding: utf-8 -*-
"""Territorial map 9 of 11: 1864. The duchies gone, and a stream made a frontier.

Same bbox, projection, palette and legend geometry as 1050 through 1814.

Nothing here is new geometry. Denmark, Bornholm, Slesvig, Holsten and Ditmarsken
come from map_1660 by way of map_1814, and the seams DK_SL and SL_HO come from
map_1397 and map_1660, so none of them can drift from their originals.

Five decisions:

  - THE DUCHIES ARE DRAWN, IN THE LOST TONE. This is the series' standing rule and
    its third application: 1660 drew the Scanian provinces in the lost tone because
    a part opening on what was left could not be silent about what went; 1814 drew
    Norway the same way for the same reason. 1864 is the wound of this chapter, so
    Slesvig, Holsten and Lauenborg are drawn as lost rather than omitted. LOST is
    imported, as always, so there is one such colour in the series and not four.

  - NORWAY IS NOT DRAWN. Fifty years is long enough. The 1721 map dropped the
    Scanian provinces once they were a settled fact rather than a wound, and the
    same test retires Norway here. The consequence for the fixture is real and it
    is the reason map_1814's curated Norwegian cases exist: Oslo, Trondhjem,
    Bergen, Tromsø and Røros must now resolve to NOTHING, and they are pinned to
    None for 1864 so that dropping a territory is a deliberate act with a test
    behind it rather than a silent omission.

  - THE NEW STATE FRONTIER NEEDS NO NEW GEOMETRY, BECAUSE IT IS ALREADY HERE. The
    Kongeå had divided kingdom from duchy since the fourteenth century, and on this
    frame it is DK_SL, which has been in the series since the 1397 map. In 1864 it
    stops being an internal administrative line and becomes an international
    border, and it is drawn heavier and labelled for that reason. This is exactly
    what map_1814 found about the Eider: the constitutional line and the old ducal
    line are the same line, and showing that they are identical costs nothing and
    is most of the argument. The inherited polygons already put Ribe, Kolding and
    Vejle on the Danish side and Haderslev, Aabenraa and Sønderborg on the other,
    which is the check the fixture now makes explicitly.

  - THE BORDER ADJUSTMENTS ARE NOT DRAWN, AND THE NOTE SAYS SO WITH NUMBERS. The
    treaty moved ground both ways: the royal enclaves inside Slesvig went south,
    and Ribe Herred, Nørre Tyrstrup Herred and Ærø came north. None of it can be
    drawn on this frame. The enclaves were scattered parcels of the kind map_1721
    refused to draw for Gottorp, on the ground that it would be a map of something
    that did not exist; Ærø resolves to no territory at all on the inherited
    geometry, so it cannot be shown changing hands without first inventing an
    island; and Nørre Tyrstrup Herred is eight parishes. Rather than assert
    outlines nobody has measured, the note carries the two figures Danmarks
    Statistik computed at the 1860 census: 13,053 people in the territory ceded and
    20,864 in the territory received. That is the whole exchange, stated exactly,
    in the one place on the map where it can be stated honestly.

  - LAUENBORG KEEPS ITS MARKER AND CHANGES COLOUR. map_1814 marked it with a dot
    rather than an outline because no measured boundary for a 1,200 km2 duchy
    exists in this project. That has not changed, so the dot stays and moves to the
    lost tone with everything else that went at Vienna. Ratzeburg still resolves to
    no territory, and the curated case is still pinned to None.
"""
import map_1397 as M97
import map_1660 as M66
import map_1814 as M14
import mapspine as M

CORE_OP = .62
DEP_OP = .30
LOST = M66.LOST
LOST_OP = M66.LOST_OP

DENMARK = M14.DENMARK
BORNHOLM = M14.BORNHOLM
SLESVIG = M14.SLESVIG
HOLSTEN = M14.HOLSTEN
DITMARSKEN = M14.DITMARSKEN

GREENLAND = M97.GREENLAND
ICELAND = M97.ICELAND
FAROES = M97.FAROES

DK_SL = M97.DK_SL
SL_HO = M66.SL_HO

LAUENBURG_AT = M14.LAUENBURG_AT


def build():
    f = M.frame()
    polys = M.land(50)
    out = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
           'aria-label="Territorial map of 1864. By the Peace of Vienna of 30 October 1864 '
           'the king of Denmark renounced the duchies of Slesvig, Holsten and Lauenborg to '
           'the Emperor of Austria and the King of Prussia, and they are drawn here in the '
           'lost tone rather than omitted. What is left is Jutland, the islands and '
           'Bornholm. The Kongeå, which had divided the kingdom from the duchy of Slesvig '
           'since the fourteenth century, becomes an international frontier and is drawn '
           'heavier for that reason. Norway, ceded fifty years earlier, is no longer shown. '
           'The border adjustments made by the treaty ran both ways and are too small to '
           'draw at this scale: the royal enclaves inside Slesvig went south, and Ribe '
           'Herred, Nørre Tyrstrup Herred and the island of Ærø came north, the ceded '
           'territory holding 13,053 people at the census of 1860 and the received '
           'territory 20,864. The western panel carries Greenland, Iceland and the Faroes, '
           'which are unaffected.">' % (M.W, M.H),
           M.base(f, polys),
           M.graticule(f),
           M.clip_defs(f, polys)]

    for poly in (DENMARK, BORNHOLM):
        out.append(M.territory(f, poly, fill=M.CORE, opacity=CORE_OP))
    for poly in (SLESVIG, HOLSTEN, DITMARSKEN):
        out.append(M.territory(f, poly, fill=LOST, opacity=LOST_OP, edge=LOST, dash="2 3"))

    # The old ducal seam, drawn heavy: from 30 October 1864 it is a state frontier.
    # Same vertices as every map since 1397. That identity is the point.
    d = f.path(DK_SL, close=False)
    if d:
        out.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" '
                   'opacity=".85"/>' % (d, M.INK))

    d = f.path(SL_HO, close=False)
    if d:
        out.append('<path d="%s" fill="none" stroke="%s" stroke-width="1" '
                   'stroke-dasharray="3 3" opacity=".55"/>' % (d, M.PAPER))

    fills = [(GREENLAND, M.DEP, DEP_OP), (ICELAND, M.DEP, DEP_OP), (FAROES, M.DEP, DEP_OP)]
    out.append(M.western_panel(M.land(50), fills=fills))
    out.append('<text x="%d" y="%d" class="mapx" text-anchor="start">Unaffected. Denmark '
               'keeps all three.</text>'
               % (M.WEST_BOX[0] + 4, M.WEST_BOX[1] + M.WEST_BOX[3] + 12))

    out.append(M.note(f, 9.3, 56.4, "DANMARK", cls="mapl"))
    out.append(M.note(f, 17.5, 60.6, "SVERIGE", cls="mapt"))
    out.append(M.note(f, 8.5, 61.5, "NORGE", cls="mapt"))
    out.append(M.note(f, 24.5, 62.5, "FINLAND", cls="mapt", anchor="middle"))

    for lon, lat, t, a in [(10.55, 54.95, "Slesvig", "middle"),
                           (9.55, 53.95, "Holsten", "middle"),
                           (14.90, 54.78, "Bornholm", "middle")]:
        out.append(M.note(f, lon, lat, t, cls="mapt", anchor=a))

    # BOTH BLOCKS SIT NEXT TO WHAT THEY DESCRIBE. The first version put them
    # where the collision guard was happiest, which was out in the North Sea and
    # the eastern Baltic, and the rasterised map was unreadable: the note about
    # the Konge\u00e5 was three hundred kilometres from the Konge\u00e5. Guards can see
    # overlap and cannot see meaning. Positions found by search, then looked at.
    out.append(M.note(f, 11.70, 54.35, "CEDED AT VIENNA, 1864", cls="mapx",
                      anchor="start"))
    out.append(M.note(f, 11.70, 53.93, "to two monarchs personally", cls="mapt",
                      anchor="start"))
    out.append(M.note(f, 11.70, 53.51, "\u2014 not to Germany", cls="mapt",
                      anchor="start"))

    # The explanation moved into the legend and only the label stayed on the map.
    # Three lines of note would not fit anywhere in Jutland without colliding, and
    # every position that satisfied the guard put them out in the North Sea, where
    # one of them ran off the left edge of the canvas without anything firing:
    # overruns() tests the right edge and the bottom, not the left. Caught by
    # looking. HANDOFF item 49.
    out.append(M.note(f, 6.60, 55.60, "THE KONGE\u00c5", cls="mapx", anchor="start"))

    for lon, lat, t, a, dx, dy in [(12.57, 55.68, "K\u00f8benhavn", "end", -5, 4),
                                   (9.47, 55.49, "Kolding", "end", -6, 11),
                                   (9.44, 54.78, "Flensburg", "end", -6, 11),
                                   (LAUENBURG_AT[0], LAUENBURG_AT[1], "Lauenborg",
                                    "end", -5, 11)]:
        out.append(M.dot(f, lon, lat, t, anchor=a, dx=dx, dy=dy))

    out.append(M.legend([("Ruled directly", M.CORE, CORE_OP),
                         ("Ceded at Vienna, 1864", LOST, LOST_OP),
                         ("Heavy line: the Konge\u00e5, an internal border", None, 0),
                         ("since the 1300s and a state frontier from 1864", None, 0),
                         ("Lauenborg: ceded too, marked not drawn", None, 0),
                         ("Adjustments both ways: too small to draw", None, 0)],
                        x=14, y=190))
    out.append(M.note(f, 27.9, 68.35, "no fixed border", cls="mapt", anchor="middle"))
    out.append(M.note(f, 27.0, 54.6, "1864", cls="mapl", anchor="middle"))
    out.append('</svg>')
    return "\n  ".join(out)


if __name__ == "__main__":
    svg = build()
    for bad in (M.check(svg, "svg_terr_1864.txt") or []):
        print("  !! %s" % (bad,))
    open("svg_terr_1864.txt", "w", encoding="utf-8").write(svg)
    M.rasterise(svg, "look_1864.png")
    print("wrote svg_terr_1864.txt (%d chars)" % len(svg))
