# -*- coding: utf-8 -*-
"""Territorial map 7 of 11: 1721. The southern border closed.

Same bbox, projection, palette and legend geometry as 1050 through 1660.

Geometry is inherited from map_1660 wherever nothing changed, which is most of
it: Denmark, Norway and Bornholm are untouched between 1660 and 1721, and the
shared seams - SOUND, NO_SE_1660, BOHUS_NW - are imported rather than restated so
that they cannot drift apart from their originals.

Four decisions:

  - THE CEDED PROVINCES ARE NO LONGER DRAWN. The 1660 map gives Skaane, Halland,
    Blekinge, Bohuslaen, Jaemtland, Haerjedalen, Gotland and Oesel their own tone,
    because a part opening on what was left cannot be silent about what went. By
    1721 they are not a loss being absorbed but a settled fact: Denmark renounced
    them formally at Frederiksborg in 1720, and the last army that tried to take
    them back came home in 1710. Sweden is uncoloured here exactly as on the 1600
    map, and the legend says the renunciation is what changed, so that a reader
    comparing the two maps is not left to guess.

  - SLESVIG IS ONE COLOUR AND SO IS HOLSTEN, but they no longer mean the same
    thing. The Gottorp share of Slesvig was taken in 1713 and confirmed in 1720;
    Slesvig is now wholly the king's. Holstein is not: the great powers made
    Frederik 4. evacuate the Holstein possessions, and the Gottorp dukes keep them
    until 1773. The legend carries that distinction because the map cannot: the
    ducal and royal parcels in Holstein are interleaved parish by parish, exactly
    as the 1544 partition left them, and drawing them as two areas would be a map
    of something that did not exist. This is the same decision the 1600 map made,
    for the same reason, and it is why the Gottorp problem is so hard to see.

  - GREENLAND BECOMES DEP. Egede landed on 3 July 1721. The claim that has been
    on these maps since 1500 stops being a claim.

  - TRONDHJEM IS MARKED. Griffenfeld was on Munkholmen in the fjord until 1698,
    and Denmark's hold on Norway is about to matter for a century. It is a cheap
    dot and it earns its place.
"""
import map_1397 as M97
import map_1660 as M66
import mapspine as M

CORE_OP = .62
DEP_OP = .30

DENMARK = M66.DENMARK
NORWAY = M66.NORWAY
BORNHOLM = M66.BORNHOLM
SLESVIG = M66.SLESVIG
HOLSTEN = M66.HOLSTEN
DITMARSKEN = M66.DITMARSKEN

# ---------------------------------------------------------------- the west
GREENLAND = M97.GREENLAND          # DEP from this year, not CLAIM
ICELAND = M97.ICELAND
FAROES = M97.FAROES

DK_SL = M97.DK_SL


def build():
    f = M.frame()
    polys = M.land(50)
    out = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
           'aria-label="Territorial map of 1721. Denmark is Jutland, the islands and Bornholm, '
           'and Norway keeps Trondhjem. The whole of Schleswig is now held by the king, the '
           'ducal share having been taken in 1713 and confirmed by the peace of 1720; Holstein '
           'is still shared with the dukes of Gottorp, whose parcels are interleaved with the '
           'royal ones and cannot honestly be drawn as an area. Sweden is not coloured: the '
           'eastern provinces were formally renounced in 1720. The western panel carries '
           'Greenland, Iceland and the Faroes as dependencies, Greenland for the first time, '
           'Hans Egede having landed in July 1721.">' % (M.W, M.H),
           M.base(f, polys),
           M.graticule(f),
           M.clip_defs(f, polys)]

    for poly in (DENMARK, BORNHOLM, NORWAY):
        out.append(M.territory(f, poly, fill=M.CORE, opacity=CORE_OP))
    for poly in (SLESVIG, HOLSTEN, DITMARSKEN):
        out.append(M.territory(f, poly, fill=M.DEP, opacity=DEP_OP, edge=M.DEP, dash="4 3"))

    d = f.path(DK_SL, close=False)
    if d:
        out.append('<path d="%s" fill="none" stroke="%s" stroke-width="1" '
                   'stroke-dasharray="3 3" opacity=".75"/>' % (d, M.PAPER))

    fills = [(GREENLAND, M.DEP, DEP_OP), (ICELAND, M.DEP, DEP_OP), (FAROES, M.DEP, DEP_OP)]
    out.append(M.western_panel(M.land(50), fills=fills))
    out.append('<text x="%d" y="%d" class="mapx" text-anchor="start">Greenland: a claim no '
               'longer, from July 1721</text>'
               % (M.WEST_BOX[0] + 4, M.WEST_BOX[1] + M.WEST_BOX[3] + 12))

    for lon, lat, t in [(9.3, 56.4, "DANMARK"), (7.9, 61.5, "NORGE")]:
        out.append(M.note(f, lon, lat, t, cls="mapl"))
    out.append(M.note(f, 17.5, 60.6, "SVERIGE", cls="mapt"))
    out.append(M.note(f, 17.5, 60.05, "the eastern provinces", cls="mapt"))
    out.append(M.note(f, 17.5, 59.5, "renounced, 1720", cls="mapt"))

    for lon, lat, t, a in [(24.5, 62.5, "FINLAND", "middle"),
                           (9.95, 54.95, "Slesvig", "middle"),
                           (10.05, 53.80, "Holsten", "middle"),
                           (14.90, 54.78, "Bornholm", "middle")]:
        out.append(M.note(f, lon, lat, t, cls="mapt", anchor=a))

    for lon, lat, t, a, dx, dy in [(12.57, 55.68, "K\u00f8benhavn", "end", -5, 4),
                                   (10.75, 59.91, "Oslo", "start", 5, 3),
                                   (10.40, 63.43, "Trondhjem", "start", 5, 3),
                                   (9.56, 54.52, "Gottorp", "end", -5, 3),
                                   (8.95, 54.32, "T\u00f8nning", "end", -5, 10)]:
        out.append(M.dot(f, lon, lat, t, anchor=a, dx=dx, dy=dy))

    out.append(M.legend([("Ruled directly", M.CORE, CORE_OP),
                         ("Slesvig: wholly the king's, 1721", M.DEP, DEP_OP),
                         ("Holsten: shared with Gottorp to 1773", None, 0),
                         ("Sweden: the east renounced, 1720", None, 0)], x=14, y=190))
    out.append(M.note(f, 27.9, 68.35, "no fixed border", cls="mapt", anchor="middle"))
    out.append(M.note(f, 27.0, 54.6, "1721", cls="mapl", anchor="middle"))
    out.append('</svg>')
    return "\n  ".join(out)


if __name__ == "__main__":
    svg = build()
    open("svg_terr_1721.txt", "w", encoding="utf-8").write(svg)
    M.rasterise(svg, "look_1721.png")
    print("wrote svg_terr_1721.txt (%d chars)" % len(svg))
