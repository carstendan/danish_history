# -*- coding: utf-8 -*-
"""Figures 1 and 2 for chapter 18.

1. Held of whom: the constitutional knot tied at Ribe in 1460, drawn as a
   fealty diagram. A new form for the series - not a timeline, a process, a
   family tree, a ledger, a stepped ladder or a rule-block.
2. Hemmingstedt, 17 February 1500, as a schematic. Deliberately not a
   coastline map: the thing that decided the battle was a road, a bank and a
   sluice, and a real map at that scale shows none of them.
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
def fealty():
    W, H = 900, 404
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Diagram of who held what of whom after the Treaty of Ribe in 1460. One man, '
         'Christian the First, is at once elected king of Denmark, duke of Schleswig held of the '
         'Danish crown, and count of Holstein held of the Holy Roman Emperor. The duchies are '
         'promised to remain forever undivided and may not be annexed to Denmark.">' % (W, H),
         '<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, M.PAPER)]

    o.append(t(26, 34, "HELD OF WHOM, AFTER 1460", "mapt", PART_E))

    # the two overlords
    boxes = [(60, 66, 300, 62, "THE DANISH CROWN", "elective; the council chooses"),
             (540, 66, 300, 62, "THE HOLY ROMAN EMPIRE", "Holstein is an imperial fief")]
    for x, y, w, h, head, sub in boxes:
        o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s" '
                 'stroke-width="1.2"/>' % (x, y, w, h, MUTED))
        o.append(t(x + w / 2, y + 26, head, "mapl", INK, "middle"))
        o.append(t(x + w / 2, y + 44, sub, "mapx", MUTED, "middle"))

    # the two territories
    ter = [(60, 226, 300, 74, "SLESVIG", "a duchy, held of the Danish crown",
            "Danish law, Danish fief \u2014 and", "may not be joined to Denmark"),
           (540, 226, 300, 74, "HOLSTEN", "a county, from 1474 a duchy",
            "German law, imperial fief \u2014 and", "the Emperor's business, not the council's")]
    for x, y, w, h, head, sub, l1, l2 in ter:
        o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" fill-opacity=".14" '
                 'stroke="%s" stroke-width="1.2"/>' % (x, y, w, h, PART_E, PART_E))
        o.append(t(x + w / 2, y + 24, head, "mapl", INK, "middle"))
        o.append(t(x + w / 2, y + 40, sub, "mapx", MUTED, "middle"))
        o.append(t(x + w / 2, y + 56, l1, "mapx", MUTED, "middle"))
        o.append(t(x + w / 2, y + 68, l2, "mapx", MUTED, "middle"))

    # the man in the middle
    o.append('<rect x="330" y="140" width="240" height="62" fill="%s" fill-opacity=".92"/>' % PART_E)
    o.append(t(450, 168, "CHRISTIAN 1.", "mapl", M.PAPER, "middle"))
    o.append(t(450, 186, "one man, three hats", "mapx", M.PAPER, "middle"))

    for x1, y1, x2, y2 in [(210, 128, 400, 140), (690, 128, 500, 140),
                           (400, 202, 210, 226), (500, 202, 690, 226)]:
        o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.1" '
                 'opacity=".7"/>' % (x1, y1, x2, y2, MUTED))

    o.append('<line x1="200" y1="326" x2="700" y2="326" stroke="%s" stroke-width="1.6" '
             'stroke-dasharray="6 4"/>' % OX)
    o.append('<line x1="210" y1="300" x2="210" y2="326" stroke="%s" stroke-width="1" '
             'opacity=".6"/>' % OX)
    o.append('<line x1="690" y1="300" x2="690" y2="326" stroke="%s" stroke-width="1" '
             'opacity=".6"/>' % OX)
    o.append(t(450, 348, "dat se bliven ewich tosamende ungedelt", "mapl", OX, "middle",
               ' font-style="italic"'))
    o.append(t(450, 366, "\u2014 and the knighthood may resist if he breaks it", "mapx",
               MUTED, "middle"))

    # the dated band that used to sit here retold section 03 — Dahlmann, Neuber, 1845 —
    # which the prose does at length and better. Cutting it lets the title's one idea stand.
    o.append('</svg>')
    return "\n  ".join(o), W, H


# ------------------------------------------------------------------ figure 2
def hemmingstedt():
    W, H = 900, 430
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Schematic of the battle of Hemmingstedt on 17 February 1500. A royal army '
         'of about twelve thousand advances along a single raised road through the marsh towards '
         'Heide. The Ditmarschers block the road with an earth bank, attack the head of the column '
         'from both sides, and open the sluices so that the marsh floods. Some four thousand of '
         'the royal army die, many by drowning.">' % (W, H),
         '<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, M.PAPER)]

    o.append(t(26, 34, "17 FEBRUARY 1500", "mapt", PART_E))
    o.append('<text x="26" y="62" style="font-family:\'Iowan Old Style\',Palatino,Georgia,serif;'
             'font-size:19px;fill:%s">One road, and no room to turn round.</text>' % INK)

    # marsh
    o.append('<rect x="26" y="92" width="848" height="180" fill="#B9CDD6" fill-opacity=".55"/>')
    o.append(t(40, 112, "MARSH \u2014 below sea level, drained, and diked", "mapx", MUTED))

    # the road
    o.append('<rect x="26" y="170" width="848" height="26" fill="%s" fill-opacity=".35"/>' % M.LAND)
    o.append('<line x1="26" y1="170" x2="874" y2="170" stroke="%s" stroke-width="1"/>' % M.LAND_EDGE)
    o.append('<line x1="26" y1="196" x2="874" y2="196" stroke="%s" stroke-width="1"/>' % M.LAND_EDGE)

    # the column
    for i in range(9):
        x = 60 + i * 46
        o.append('<rect x="%d" y="176" width="34" height="14" fill="%s" fill-opacity=".85"/>'
                 % (x, PART_E))
    o.append(t(60, 164, "the royal army, about 12,000, strung out along the causeway",
               "mapx", MUTED))
    o.append(t(60, 216, "Meldorf, taken 14 February", "mapx", MUTED))

    # the bank
    o.append('<rect x="516" y="150" width="16" height="66" fill="%s" fill-opacity=".9"/>' % OX)
    o.append(t(524, 142, "the bank", "mapl", OX, "middle"))
    o.append(t(524, 288, "thrown up overnight", "mapx", OX, "middle"))

    # the attack
    for y in (128, 238):
        for x in (470, 500, 560, 590):
            dy = 34 if y < 170 else -34
            o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.6" '
                     'opacity=".85"/>' % (x, y, x + 10, y + dy, OX))
    o.append(t(620, 132, "Ditmarschers, perhaps 2,000", "mapx", OX))
    o.append(t(620, 258, "sluices opened \u2014 the marsh floods", "mapx", OX))

    o.append('<text x="874" y="188" class="mapl" fill="%s" text-anchor="end">to Heide \u2192</text>'
             % MUTED)

    o.append('<line x1="26" y1="300" x2="%d" y2="300" stroke="%s" stroke-width=".8"/>'
             % (W - 26, RULE))
    for i, (head, body) in enumerate([
            ("The force", "Danish and Holstein nobility, levies from both, and the Great Guard \u2014 "
                          "4,000 mercenaries under Thomas Slentz"),
            ("The ground", "A single raised road through drained marsh in February. Artillery went "
                           "into the ditch and stayed there"),
            ("The loss", "Around 4,000 dead, many drowned. Eleven of the Ahlefeldt family, six of "
                         "the Buchwald. Ditmarschen lost under 100"),
            ("The banner", "The royal Dannebrog was taken. Frederik 2. got it back in 1559, "
                           "\u2018almost destroyed by damp and age\u2019")]):
        o.append(t(26, 326 + i * 24, head, "mapl", PART_E))
        o.append(t(150, 326 + i * 24, body, "mapx", MUTED))
    o.append('</svg>')
    return "\n  ".join(o), W, H


if __name__ == "__main__":
    for name, fn in [("svg_fealty", fealty), ("svg_hemming", hemmingstedt)]:
        svg, w, h = fn()
        open(name + ".txt", "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.split("_")[1] + ".png")
        print("%-12s %d chars  %dx%d" % (name, len(svg), w, h))
