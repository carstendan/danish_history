# -*- coding: utf-8 -*-
"""Figures for chapter 16b.

1. The western realm at proper scale. The spine map's panel is 158x88 px and can
   only say that these places exist; this one can say how far apart they are and
   what was in them.
2. Broendum, 1400 or 1401: forty-eight squares, thirty-four of them empty. A
   pictogram rather than a chart, because there is one estate's worth of data and
   a trend line would imply a series that does not exist.
"""
import mapspine as M

PART_E = "#2E6B5E"
INK = "#221E18"
MUTED = "#6C6E63"
RULE = "#C9CDC4"
OX = "#8A2B2B"


def t(x, y, s, cls="mapx", fill=MUTED, anchor="start", extra=""):
    return ('<text x="%.1f" y="%.1f" class="%s" fill="%s" text-anchor="%s"%s>%s</text>'
            % (x, y, cls, fill, anchor, extra, s))


# ------------------------------------------------------------------ figure 1
def atlantic():
    BBOX = (-52.0, 57.5, 14.0, 68.0)
    W, H, STRIP = 900, 400, 104
    NEAR = (-60.0, 50.0, 25.0, 75.0)
    f = M.detail_frame(BBOX, W, H)
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Map of the North Atlantic possessions of the Norwegian crown around 1400: '
         'Bergen and Nidaros in Norway, Shetland and Orkney off Scotland, the Faroes, Iceland with '
         'Skalholt and Holar, and in Greenland the Eastern Settlement with Gardar and Hvalsey, '
         'where the last recorded event took place in 1408. The Western Settlement is already '
         'abandoned.">' % (W, H + STRIP)]
    o += M.detail_base(f, W, H, NEAR, scale=50)

    # the sailing route east-west, as it was actually run: Bergen to Iceland to Greenland
    ROUTE = [(5.32, 60.39), (-6.80, 62.00), (-13.50, 64.30), (-22.00, 64.15), (-30.00, 61.80),
             (-42.00, 60.20), (-45.50, 60.85)]
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="6 5" '
             'opacity=".8"/>' % (f.path(ROUTE, close=False), PART_E))

    for lon, lat, name, note, anchor, dy in [
            (5.32, 60.39, "Bergen", "the staple", "end", 0),
            (10.40, 63.43, "Nidaros", "the archbishop", "start", 0),
            (-1.20, 60.20, "Shetland", "Norwegian until 1469", "start", 0),
            (-3.00, 58.98, "Orkney", "Norwegian until 1468", "end", 0),
            (-6.80, 62.02, "F\u00e6r\u00f8erne", "", "start", 0),
            (-20.30, 63.66, "Sk\u00e1lholt", "bishopric", "end", 0),
            (-19.30, 65.73, "H\u00f3lar", "bishopric", "start", 0),
            (-45.40, 60.99, "Gar\u00f0ar", "the bishop's seat", "start", 0),
            (-45.78, 60.83, "Hvalsey", "a wedding, 16 Sept 1408", "start", 30),
            (-51.70, 64.18, "Western Settlement", "abandoned by c. 1360", "start", 0)]:
        x, y = f.xy(lon, lat)
        y = y + dy
        dx = 5 if anchor == "start" else -5
        col = OX if "abandoned" in note else INK
        o.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s"/>' % (x, y, col))
        o.append('<text x="%.1f" y="%.1f" class="mapl" text-anchor="%s">%s</text>'
                 % (x + dx, y + 3.4, anchor, name))
        if note:
            o.append('<text x="%.1f" y="%.1f" class="mapx" text-anchor="%s">%s</text>'
                     % (x + dx, y + 15, anchor, note))

    o.append(M.note(f, -28.0, 66.8, "THE NORTH ATLANTIC", cls="mapt"))
    o.append('</g>')

    o.append('<rect x="0" y="%d" width="%d" height="%d" fill="%s"/>' % (H, W, STRIP, M.PAPER))
    o.append('<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width=".8"/>'
             % (H, W, H, M.LAND_EDGE))
    o.append(t(20, H + 24, "REACHED THROUGH NORWAY", "mapt", PART_E))
    for i, l in enumerate([
            "All of this came to Denmark in 1380, when a ten-year-old inherited two crowns, and none of it",
            "was ever governed from Copenhagen. Bergen to Gar\u00f0ar is about 3,000 km \u2014 further than Copenhagen to",
            "Baghdad. One or two ships a year made the crossing in a good decade, and by the 1400s not even that."]):
        o.append(t(20, H + 48 + i * 16, l, "mapx", MUTED))
    o.append('</svg>')
    return "\n  ".join(o), W, H + STRIP


# ------------------------------------------------------------------ figure 2
def brondum():
    W, H = 900, 380
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Pictogram of the Broendum estate in north-west Himmerland in 1400 or 1401: '
         'forty-eight farms, of which thirty-four were lying waste and fourteen were still worked.">'
         % (W, H),
         '<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, M.PAPER)]
    o.append(t(26, 34, "THE BR\u00d8NDUM ESTATE, 1400 OR 1401", "mapt", PART_E))
    o.append('<text x="26" y="64" style="font-family:\'Iowan Old Style\',Palatino,Georgia,serif;'
             'font-size:19px;fill:%s">Forty-eight farms. Thirty-four of them empty.</text>' % INK)

    # 48 squares, 12 across; the worked ones first so the block reads left to right
    side, gap, x0, y0, per = 34, 10, 26, 96, 12
    for i in range(48):
        col, row = i % per, i // per
        x = x0 + col * (side + gap)
        y = y0 + row * (side + gap)
        worked = i < 14
        if worked:
            o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" fill-opacity=".8"/>'
                     % (x, y, side, side, PART_E))
        else:
            o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s" '
                     'stroke-width="1.1" stroke-dasharray="3 3" opacity=".8"/>'
                     % (x, y, side, side, OX))
    yb = y0 + 4 * (side + gap) + 8
    o.append('<rect x="26" y="%d" width="16" height="16" fill="%s" fill-opacity=".8"/>' % (yb, PART_E))
    o.append(t(50, yb + 13, "14 still worked", "mapx", MUTED))
    o.append('<rect x="190" y="%d" width="16" height="16" fill="none" stroke="%s" '
             'stroke-width="1.1" stroke-dasharray="3 3"/>' % (yb, OX))
    o.append(t(214, yb + 13, "34 lying waste \u2014 \u00f8deg\u00e5rde", "mapx", MUTED))

    o.append('<line x1="26" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width=".8"/>'
             % (yb + 34, W - 26, yb + 34, RULE))
    for i, l in enumerate([
            "One estate in one poor district of north-west Himmerland, and it must not be made a national average.",
            "But deserted farms peak across Denmark in the twenty years after 1400, not in the plague decades \u2014 and",
            "this is the kind of document a landlord was reading when he decided what rent he could still ask."]):
        o.append(t(26, yb + 58 + i * 16, l, "mapx", MUTED))
    o.append('</svg>')
    return "\n  ".join(o), W, H


if __name__ == "__main__":
    for name, fn in [("svg_atlantic", atlantic), ("svg_brondum", brondum)]:
        svg, w, h = fn()
        open(name + ".txt", "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.split("_")[1] + ".png")
        print("%-14s %d chars  %dx%d" % (name, len(svg), w, h))
