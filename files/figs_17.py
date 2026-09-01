# -*- coding: utf-8 -*-
"""Figures for chapter 17.

1. The Sound, and the machinery built to tax it.
2. One noble per ship - the toll's arithmetic, and who did not pay.
3. The road south: the other way Danish goods left the country.
"""
import mapspine as M

PART_E = "#2E6B5E"
INK = "#221E18"
MUTED = "#6C6E63"
RULE = "#C9CDC4"


# ------------------------------------------------------------------ figure 1
def sound():
    BBOX = (11.55, 55.25, 13.75, 56.32)
    W, H = 660, 600
    STRIP = 96
    NEAR = (9.0, 54.0, 16.0, 58.0)
    f = M.detail_frame(BBOX, W, H)
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Map of the Sound between Zealand and Skaane, both shores Danish, showing the '
         'toll line between Helsingor and Helsingborg where Erik of Pomerania began charging every '
         'foreign ship one noble in 1429, with the castle of Krogen at Helsingor, Kaernan at '
         'Helsingborg, Malmohus, the new town of Landskrona, and Copenhagen.">' % (W, H)]
    o += M.detail_base(f, W, H, NEAR)

    # the toll line
    x1, y1 = f.xy(12.615, 56.038)
    x2, y2 = f.xy(12.700, 56.046)
    dx, dy = x2 - x1, y2 - y1
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2.2" '
             'stroke-dasharray="6 4"/>' % (x1 - dx * .35, y1 - dy * .35,
                                           x2 + dx * .35, y2 + dy * .35, M.CLAIM))

    # the narrows, marked
    o.append('<text x="%.1f" y="%.1f" class="mapl" fill="%s" text-anchor="middle">'
             'four kilometres</text>' % ((x1 + x2) / 2, y1 - 16, M.CLAIM))

    for lon, lat, name, anchor, note in [
            (12.615, 56.038, "Helsing\u00f8r", "end", "Krogen, built for the toll"),
            (12.700, 56.046, "Helsingborg", "start", "K\u00e4rnan, strengthened"),
            (12.575, 55.676, "K\u00f8benhavn", "end", "the king's residence"),
            (13.000, 55.605, "Malm\u00f8", "start", "Malm\u00f8hus"),
            (12.830, 55.870, "Landskrona", "start", "founded 1413"),
            (13.193, 55.705, "Lund", "start", "the archbishop"),
            (12.850, 55.385, "Falsterbo", "start", "the herring market"),
            (12.675, 55.593, "Drag\u00f8r", "end", "")]:
        x, y = f.xy(lon, lat)
        ddx = 6 if anchor == "start" else -6
        o.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s"/>' % (x, y, INK))
        o.append('<text x="%.1f" y="%.1f" class="mapl" text-anchor="%s">%s</text>'
                 % (x + ddx, y + 3.4, anchor, name))
        if note:
            o.append('<text x="%.1f" y="%.1f" class="mapx" text-anchor="%s">%s</text>'
                     % (x + ddx, y + 15, anchor, note))

    for lon, lat, t in [(12.05, 55.95, "SJ\u00c6LLAND"), (13.45, 56.15, "SK\u00c5NE")]:
        o.append(M.note(f, lon, lat, t, cls="mapt"))
    o.append('</g>')

    o.append('<rect x="0" y="%d" width="%d" height="%d" fill="%s"/>' % (H, W, STRIP, M.PAPER))
    o.append('<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width=".8"/>'
             % (H, W, H, M.LAND_EDGE))
    o.append('<text x="14" y="%d" class="mapt" fill="%s">BOTH SHORES, ONE HAND</text>'
             % (H + 22, PART_E))
    for i, s in enumerate([
            "Valdemar Atterdag recovered Sk\u00e5ne in 1360 (chapter 15). Without that, none of this",
            "is possible: a toll on a strait needs both banks, or the ships simply hug the other one.",
            "Foreign ships were forbidden the Great and Little Belts, so there was no way round."]):
        o.append('<text x="14" y="%d" class="mapx" fill="%s">%s</text>' % (H + 44 + i * 16, MUTED, s))
    o.append('</svg>')
    return "\n  ".join(o), W, H + STRIP


# ------------------------------------------------------------------ figure 2
def toll():
    W, H = 900, 372
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Diagram of the Sound toll as introduced about 1429: one English noble per '
         'ship with a topmast, paid at Helsingor, with small craft exempt, Hanseatic towns '
         'exempt by privilege, and union subjects not foreign. Below, what the toll became: a '
         'cargo duty from 1567 and an income lasting to 1857.">' % (W, H),
         '<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, M.PAPER)]

    o.append('<text x="26" y="34" class="mapt" fill="%s">THE RULE, c. 1429</text>' % PART_E)
    o.append('<text x="26" y="62" style="font-family:\'Iowan Old Style\',Palatino,Georgia,serif;'
             'font-size:19px;fill:%s">One noble per ship. Not per cargo, not per ton.</text>' % INK)

    rows = [("Who paid", ["Every foreign ship with a mast-top \u2014 that is,",
                          "every ship big enough to be worth taxing"]),
            ("Who did not", ["Small craft and lighters; subjects of the three",
                             "kingdoms, who were not foreign; and by privilege",
                             "a number of Hanseatic towns, later Dutch ones too"]),
            ("Where", ["At Helsing\u00f8r, under the guns of Krogen \u2014 moved there",
                       "from Helsingborg, where the Sk\u00e5ne toll had been taken"]),
            ("Why it worked", ["Both banks Danish since 1360, and the Belts closed",
                               "to foreigners. There was no other door into the Baltic"])]
    y = 96
    for i, (head, lines) in enumerate(rows):
        o.append('<text x="26" y="%d" class="mapl" fill="%s">%s</text>' % (y, PART_E, head))
        for k, l in enumerate(lines):
            o.append('<text x="200" y="%d" class="mapx" fill="%s">%s</text>' % (y + k * 15, MUTED, l))
        y += 20 + 15 * len(lines) + 14
        if i < len(rows) - 1:
            o.append('<line x1="26" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width=".6"/>'
                     % (y - 22, W - 26, y - 22, RULE))

    # the dated band that used to sit here retold section 11's 1497/1567/1857 numbers.
    # A figure should not summarise prose the reader has just read.
    o.append('</svg>')
    return "\n  ".join(o), W, H


# ------------------------------------------------------------------ figure 3
def roads():
    BBOX = (7.4, 53.3, 14.2, 57.9)
    W, H = 660, 700
    NEAR = (5.0, 52.0, 18.0, 60.0)
    f = M.detail_frame(BBOX, W, H)
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Map of Jutland and the western Baltic showing the two ways Danish goods '
         'left the country in the fifteenth century: the ox road overland down the spine of '
         'Jutland to Hamburg and the Rhine towns, and the sea route through the Sound past '
         'Helsingor. Luebeck, Hamburg, Ribe, Kolding, Viborg and Aalborg are marked.">' % (W, H)]
    o += M.detail_base(f, W, H, NEAR)

    OXROAD = [(9.93, 57.05), (9.40, 56.45), (9.35, 56.10), (9.40, 55.72), (9.47, 55.49),
              (9.35, 55.20), (9.40, 54.90), (9.55, 54.51), (9.66, 54.30), (9.98, 53.55)]
    d = f.path(OXROAD, close=False)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.6" opacity=".85"/>' % (d, M.CLAIM))

    SEA = [(14.10, 54.55), (13.30, 54.95), (12.80, 55.30), (12.65, 55.62), (12.62, 56.04),
           (12.30, 56.55), (11.30, 57.35), (10.30, 57.80), (8.60, 57.72)]
    d = f.path(SEA, close=False)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="7 5" '
             'opacity=".85"/>' % (d, PART_E))

    for lon, lat, name, anchor in [
            (9.93, 57.05, "Aalborg", "start"), (9.40, 56.45, "Viborg", "end"),
            (9.47, 55.49, "Kolding", "start"), (8.76, 55.33, "Ribe", "end"),
            (9.44, 54.78, "Flensborg", "start"), (9.66, 54.30, "Rendsborg", "start"),
            (9.99, 53.55, "Hamborg", "start"), (10.69, 53.87, "L\u00fcbeck", "start"),
            (12.62, 56.04, "Helsing\u00f8r", "start"), (12.57, 55.68, "K\u00f8benhavn", "start"),
            (10.39, 55.40, "Odense", "start")]:
        x, y = f.xy(lon, lat)
        ddx = 5 if anchor == "start" else -5
        o.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="%s"/>' % (x, y, INK))
        o.append('<text x="%.1f" y="%.1f" class="mapx" text-anchor="%s">%s</text>'
                 % (x + ddx, y + 3.2, anchor, name))

    o.append(M.note(f, 8.15, 55.90, "THE OX ROAD", cls="mapl"))
    o.append(M.note(f, 13.85, 55.30, "THE SOUND", cls="mapl"))
    o.append(M.note(f, 13.55, 54.35, "to Danzig and the Baltic", cls="mapt", anchor="middle"))
    o.append(M.note(f, 8.45, 57.50, "to Amsterdam", cls="mapt", anchor="middle"))
    o.append('</g>')

    o.append(M.legend([("Cattle, driven south on the hoof", M.CLAIM, .85),
                       ("Grain and goods, taxed at Helsing\u00f8r", PART_E, .85)],
                      x=18, y=H - 46))
    o.append('</svg>')
    return "\n  ".join(o), W, H


if __name__ == "__main__":
    for name, fn in [("svg_sound", sound), ("svg_toll", toll), ("svg_roads", roads)]:
        svg, w, h = fn()
        open(name + ".txt", "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.split("_")[1] + ".png")
        print("%-12s %d chars  %dx%d" % (name, len(svg), w, h))
