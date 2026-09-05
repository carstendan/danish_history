# -*- coding: utf-8 -*-
"""Territorial map 8 of 11: 1814. Norway gone, and a border inside the realm.

Same bbox, projection, palette and legend geometry as 1050 through 1721.

Geometry is inherited wherever nothing changed, which is nearly everything:
Denmark, Bornholm, Slesvig, Holsten, Ditmarsken and Norway are all imported from
map_1660 by way of map_1721 rather than restated, so they cannot drift from their
originals. The shared seams DK_SL and SL_HO are imported for the same reason.

Four decisions:

  - NORWAY IS DRAWN, IN THE LOST TONE. The 1660 map established that a part
    opening on what was left cannot be silent about what went, and drew the ceded
    provinces in ink-violet; the 1721 map dropped them once they were a settled
    fact rather than a wound. Norway in 1814 is the wound. It heads a chapter
    whose first section is called "The realm that was left", and a map of that
    realm which simply omitted four hundred years of union would be answering a
    different question. LOST is imported from map_1660 so there is one such
    colour in the series, not two.

  - THE CONFEDERATION BOUNDARY NEEDS NO NEW GEOMETRY, because on this frame it
    IS the Eider. Holstein and Lauenburg entered the German Confederation on
    8 June 1815; Slesvig did not. The line between them is SL_HO, which has been
    in this series since the 1500 map. It is drawn here a second time in a
    heavier weight and labelled, so the reader sees that the constitutional
    border and the old ducal border are the same line. That identity is the
    whole of Part H's problem and it costs nothing to show.

  - LAUENBURG IS A MARKER, NOT AN AREA. It came to Denmark by the treaty of
    4 June 1815 and was taken into possession in 1816, and at 1,200 km2 on a map
    that runs from the Elbe to the North Cape it is smaller than the dot that
    names it. No polygon for it exists in this project and none can be derived
    from the Natural Earth atlas, which carries modern countries only; inventing
    one would also mean editing HOLSTEN's vertex list to keep the shared seam
    exact, which is a second invention to cover the first. map_1721 refused to
    draw the interleaved Gottorp parcels as areas for the same reason - that it
    would be a map of something that did not exist. A marker and a legend line
    state the fact without asserting an outline nobody has measured.

    CONSEQUENCE FOR THE FIXTURE, and I had this wrong until the fixture said so.
    I wrote first that Lauenburg's ground falls inside HOLSTEN and is assigned
    there. It does not. Ratzeburg resolves to no territory at all, because
    Lauenburg was a duchy in its own right east of Holstein and the HOLSTEN
    polygon correctly excludes it. The marker therefore stands on uncoloured
    ground - which is the honest result, since the map is asserting a place and
    not an extent - and the curated case is pinned to None so that anyone who
    later digitises a Lauenburg polygon has to come and change it deliberately.
    The point sits inside the known-unclaimed box that also excuses Lubeck, and
    that box now says so.

  - THE WESTERN PANEL IS THE POINT, NOT DECORATION. Greenland, Iceland and the
    Faroes stayed with Denmark when Norway went, though they had been governed
    from Norway for centuries. The panel carries them as dependencies exactly as
    it did in 1721, and the note says what changed, because a reader comparing
    the two maps would otherwise see no difference at all.
"""
import map_1397 as M97
import map_1660 as M66
import mapspine as M

CORE_OP = .62
DEP_OP = .30
LOST = M66.LOST
LOST_OP = M66.LOST_OP

DENMARK = M66.DENMARK
BORNHOLM = M66.BORNHOLM
SLESVIG = M66.SLESVIG
HOLSTEN = M66.HOLSTEN
DITMARSKEN = M66.DITMARSKEN
NORWAY = M66.NORWAY

GREENLAND = M97.GREENLAND
ICELAND = M97.ICELAND
FAROES = M97.FAROES

DK_SL = M97.DK_SL
SL_HO = M66.SL_HO

# Ratzeburg, the seat of the duchy of Lauenburg. A marker, not an area: see the
# third decision above.
LAUENBURG_AT = (10.77, 53.70)


def build():
    f = M.frame()
    polys = M.land(50)
    out = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
           'aria-label="Territorial map of 1814. Norway, four hundred years in the same '
           'realm, was ceded to Sweden at Kiel on 14 January 1814 and is drawn here in the '
           'lost tone rather than omitted. What is left is Jutland, the islands and '
           'Bornholm, with the duchies of Slesvig and Holsten and, from the treaty of '
           '4 June 1815, the small duchy of Lauenburg, taken in exchange for Swedish '
           'Pomerania. Holsten and Lauenburg entered the German Confederation on 8 June '
           '1815; Slesvig did not, so the Confederation boundary on this map is the Eider, '
           'the same line that has divided the two duchies since the middle ages. Lauenburg '
           'is marked with a dot rather than an outline, because at twelve hundred square '
           'kilometres it is smaller at this scale than its own label and no measured '
           'boundary for it was available. The western panel carries Greenland, Iceland and '
           'the Faroes, which stayed with Denmark although they had been governed from '
           'Norway.">' % (M.W, M.H),
           M.base(f, polys),
           M.graticule(f),
           M.clip_defs(f, polys)]

    for poly in (DENMARK, BORNHOLM):
        out.append(M.territory(f, poly, fill=M.CORE, opacity=CORE_OP))
    for poly in (SLESVIG, HOLSTEN, DITMARSKEN):
        out.append(M.territory(f, poly, fill=M.DEP, opacity=DEP_OP, edge=M.DEP, dash="4 3"))
    out.append(M.territory(f, NORWAY, fill=LOST, opacity=LOST_OP, edge=LOST, dash="2 3"))

    d = f.path(DK_SL, close=False)
    if d:
        out.append('<path d="%s" fill="none" stroke="%s" stroke-width="1" '
                   'stroke-dasharray="3 3" opacity=".75"/>' % (d, M.PAPER))

    # The Confederation's northern limit. Same vertices as the ducal seam, drawn
    # heavier, because they are the same line and that is the point.
    d = f.path(SL_HO, close=False)
    if d:
        out.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" '
                   'opacity=".85"/>' % (d, M.INK))

    fills = [(GREENLAND, M.DEP, DEP_OP), (ICELAND, M.DEP, DEP_OP), (FAROES, M.DEP, DEP_OP)]
    out.append(M.western_panel(M.land(50), fills=fills))
    out.append('<text x="%d" y="%d" class="mapx" text-anchor="start">Governed from Norway '
               'for centuries. They stay.</text>'
               % (M.WEST_BOX[0] + 4, M.WEST_BOX[1] + M.WEST_BOX[3] + 12))

    out.append(M.note(f, 9.3, 56.4, "DANMARK", cls="mapl"))
    out.append(M.note(f, 7.9, 61.5, "NORGE", cls="mapl"))
    out.append(M.note(f, 7.9, 60.9, "to Sweden, 14 January 1814", cls="mapt"))
    out.append(M.note(f, 17.5, 60.6, "SVERIGE", cls="mapt"))
    out.append(M.note(f, 24.5, 62.5, "FINLAND", cls="mapt", anchor="middle"))

    for lon, lat, t, a in [(10.55, 54.95, "Slesvig", "middle"),
                           (9.55, 53.95, "Holsten", "middle"),
                           (14.90, 54.78, "Bornholm", "middle")]:
        out.append(M.note(f, lon, lat, t, cls="mapt", anchor=a))

    out.append(M.note(f, 12.55, 54.35, "THE GERMAN CONFEDERATION", cls="mapx", anchor="start"))
    out.append(M.note(f, 12.55, 54.12, "begins at the Eider, 8 June 1815", cls="mapt",
                      anchor="start"))

    for lon, lat, t, a, dx, dy in [(12.57, 55.68, "K\u00f8benhavn", "end", -5, 4),
                                   (10.75, 59.91, "Oslo", "start", 5, 3),
                                   (9.44, 54.78, "Flensburg", "end", -6, 11),
                                   (LAUENBURG_AT[0], LAUENBURG_AT[1], "Lauenborg",
                                    "start", 5, 3)]:
        out.append(M.dot(f, lon, lat, t, anchor=a, dx=dx, dy=dy))

    out.append(M.legend([("Ruled directly", M.CORE, CORE_OP),
                         ("The duchies", M.DEP, DEP_OP),
                         ("Norway: ceded to Sweden, 1814", LOST, LOST_OP),
                         ("Lauenborg: acquired 1815, marked not drawn", None, 0)],
                        x=14, y=190))
    out.append(M.note(f, 27.9, 68.35, "no fixed border", cls="mapt", anchor="middle"))
    out.append(M.note(f, 27.0, 54.6, "1814", cls="mapl", anchor="middle"))
    out.append('</svg>')
    return "\n  ".join(out)


if __name__ == "__main__":
    svg = build()
    open("svg_terr_1814.txt", "w", encoding="utf-8").write(svg)
    M.rasterise(svg, "look_1814.png")
    print("wrote svg_terr_1814.txt (%d chars)" % len(svg))
