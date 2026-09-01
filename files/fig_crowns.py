# -*- coding: utf-8 -*-
"""Figure 1, chapter 16: ten years, nine places.

Not a territorial map - chapter 16 already carries the 1397 spine map for that.
This one carries the sequence, which the spine map cannot: where each of the
three crowns was actually acquired, in what order, between 1387 and 1398.
"""
import mapspine as M
from mapkit import Frame, simplify, load_land

BBOX = (6.6, 54.1, 20.4, 60.6)
W, H = 660, 560
KEY_H = 142          # strip under the map; the key does not sit on the country


NEAR = (2.0, 50.0, 26.0, 64.0)      # generous margin around the view

STOPS = [
    (1, 12.85, 55.38, "Falsterbo", "start", 0, 13,
     "3 Aug 1387 \u00b7 King Oluf dies at seventeen"),
    (2, 13.19, 55.70, "Lund", "start", 0, 0,
     "a week later \u00b7 hailed <i>fuldm\u00e6gtig frue og husbond</i>"),
    (3, 10.75, 59.91, "Oslo", "start", 0, 0,
     "early 1388 \u00b7 Norway, and for life"),
    (4, 12.60, 58.90, "Dalaborg", "end", 0, 0,
     "Palm Sunday 1388 \u00b7 the Swedish lords change sides"),
    (5, 13.55, 58.17, "\u00c5sle", "end", 0, 0,
     "24 Feb 1389 \u00b7 King Albrecht beaten and taken"),
    (6, 13.28, 55.52, "Lindholmen", "end", 0, 2,
     "1389\u201395 \u00b7 a king kept in a Sk\u00e5ne castle"),
    (7, 9.40, 56.45, "Viborg", "end", 0, 0,
     "Jan 1396 \u00b7 Erik elected king of Denmark"),
    (8, 16.36, 56.66, "Kalmar", "start", 0, 0,
     "17 June 1397 \u00b7 crowned over all three"),
    (9, 18.07, 59.33, "Stockholm", "start", 0, 0,
     "1398 \u00b7 the last German garrison goes"),
]

CODA = [
    (12.32, 56.06, "S\u00f8borg", "start", "b. 1353"),
    (12.57, 55.68, "K\u00f8benhavn", "end", "married 1363"),
    (9.44, 54.78, "Flensborg", "start", "d. 1412"),
    (14.89, 58.45, "Vadstena", "start", "Birgitta"),
]


def build():
    f = Frame(*BBOX, W, H, pad=0)
    polys = [simplify(p, 0.013) for p in load_land("package/land-10m.json")]
    out = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
           'aria-label="Map of Denmark, southern Norway and southern Sweden marking nine '
           'places in order between 1387 and 1398: Falsterbo where King Oluf died, Lund '
           'where Margrete was hailed, Oslo, Dalaborg, Asle near Falkoping, Lindholmen, '
           'Viborg, Kalmar where Erik was crowned in 1397, and Stockholm.">' % (W, H + KEY_H),
           '<defs><clipPath id="fr"><rect x="0" y="0" width="%d" height="%d"/></clipPath></defs>'
           % (W, H),
           '<g clip-path="url(#fr)">',
           '<rect x="0" y="0" width="%d" height="%d" fill="%s" opacity=".7"/>' % (W, H, M.SEA),
           '<path d="%s" fill="%s" stroke="%s" stroke-width=".8"/>'
           % (M.detail_land_path(f, polys, NEAR, W, H), M.LAND, M.LAND_EDGE)]

    # the coda places sit under the numbered ones, in a quieter register
    for lon, lat, name, anchor, note in CODA:
        x, y = f.xy(lon, lat)
        dx = 4.5 if anchor == "start" else -4.5
        out.append('<circle cx="%.1f" cy="%.1f" r="1.9" fill="%s" fill-opacity=".55"/>'
                   '<text x="%.1f" y="%.1f" class="mapt" text-anchor="%s">%s \u00b7 %s</text>'
                   % (x, y, M.INK, x + dx, y + 3.2, anchor, name, note))

    for n, lon, lat, name, anchor, ddx, ddy, _ in STOPS:
        x, y = f.xy(lon, lat)
        dx = (9 if anchor == "start" else -9) + ddx
        out.append('<circle cx="%.1f" cy="%.1f" r="7.2" fill="%s" fill-opacity=".92"/>'
                   '<text x="%.1f" y="%.1f" class="mapl" fill="%s" text-anchor="middle">%d</text>'
                   % (x, y, M.CORE, x, y + 3.6, M.PAPER, n))
        out.append('<text x="%.1f" y="%.1f" class="mapl" text-anchor="%s">%s</text>'
                   % (x + dx, y + ddy + 3.6, anchor, name))

    for lon, lat, t in [(8.4, 59.9, "NORGE"), (16.6, 59.9, "SVERIGE"), (9.55, 55.95, "DANMARK")]:
        out.append(M.note(f, lon, lat, t, cls="mapl"))
    out.append('</g>')

    # key: a strip under the map, so nothing is printed over the country
    out.append('<rect x="0" y="%d" width="%d" height="%d" fill="%s"/>' % (H, W, KEY_H, M.PAPER))
    out.append('<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width=".8"/>'
               % (H, W, H, M.LAND_EDGE))
    out.append('<text x="14" y="%d" class="mapt">TEN YEARS, NINE PLACES</text>' % (H + 22))
    for i, st in enumerate(STOPS):
        col, row = (0, i) if i < 5 else (1, i - 5)
        out.append('<text x="%d" y="%d" class="mapx">%d \u00b7 %s</text>'
                   % (14 + col * 330, H + 44 + row * 16, st[0],
                      st[7].replace("<i>", "").replace("</i>", "")))
    out.append('</svg>')
    return "\n  ".join(out)


if __name__ == "__main__":
    svg = build()
    open("svg_crowns.txt", "w", encoding="utf-8").write(svg)
    M.rasterise(svg, "look_crowns.png")
    print("wrote svg_crowns.txt (%d chars)" % len(svg))
