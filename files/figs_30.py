# -*- coding: utf-8 -*-
"""Chapter 30's three figures.

  svg_triangle.txt   the three legs, with what went on each
  svg_surveys.txt    three cadastral acts of one state, 1662-1734
  svg_papers.txt     what the Fredensborg's papers record, and what they do not

TWO OF THESE ARE NOT THE PLANNED FIGURES, and the reason is the same in both
cases. The plan called for a cadastral plat of Christiansted quarter and for the
Fredensborg drawn in section. Both would require measurements I cannot source -
the plantation lot dimensions, the deck heights, the number of people carried on
that voyage - and inventing them in a chapter about people recorded as numbers
would be the worst possible place to guess.

What replaced them are figures the sources do support. The survey figure carries
the cadastral thread the part has been building since chapter 25, which is what
the plat was there to do. The papers figure carries the archive asymmetry, which
is the argument the ship was there to make.

Run: python3 figs_30.py
"""
import re
import xml.etree.ElementTree as ET

import mapspine as M

INK = "#3C3E36"
PAPER = "#F0F2EE"
RULE = "#C9CDC4"
IND = "#2F4C7A"
VERD = "#2E6B5E"
AMBER = "#A9601C"
MUTED = "#5F6157"
OX = "#8A2B2B"


def wrap(text, n):
    out, line = [], ""
    for w in text.split():
        if len(line) + len(w) + 1 > n:
            out.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    if line:
        out.append(line)
    return out


def validate(svg, name):
    try:
        ET.fromstring(svg)
    except ET.ParseError as e:
        raise SystemExit("!! %s not well-formed at line %d: %s"
                         % (name, e.position[0], svg.splitlines()[e.position[0] - 1][:110]))


def overruns(svg, W):
    bad = []
    for m in re.finditer(r'<text x="([\d.]+)"(?![^>]*text-anchor="(?:end|middle)")[^>]*>([^<]*)<',
                         svg):
        if float(m.group(1)) + len(m.group(2)) * 6.1 > W - 6:
            bad.append(m.group(2)[:44])
    return bad


# ------------------------------------------------------------------ figure 1
CARRIED_LO, CARRIED_HI = 100000, 111000
VOYAGES = 430
ALL_EUROPEAN = 12500000
DIED_PCT = 20
CROSSING_LO, CROSSING_HI = 2, 3


def triangle():
    W, H = 700, 560
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="A diagram of the triangular trade. From Copenhagen, ships carried Indian '
         'cotton, other textiles, firearms, gunpowder, brandy and small goods to the Danish forts '
         'on the Gold Coast. From there they carried people across the Atlantic to the Danish '
         'West Indies, a crossing of two to three months on which about one in five died. From '
         'the islands they carried raw sugar home to Copenhagen, where it was refined under '
         'monopoly. Between the 1660s and 1803 Danish ships carried about 100,000 to 111,000 '
         'people on some 430 voyages.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">THE TRIANGLE, WEIGHED</text>')
    o.append('<text x="26" y="46" class="mapt">every Danish voyage began and ended in '
             'Copenhagen</text>')

    import math
    R = 48
    nodes = [("K\u00d8BENHAVN", 150, 130), ("GULDKYSTEN", 550, 190), ("VESTINDIEN", 250, 320)]
    legs = [(0, 1, IND, "2.4"), (1, 2, OX, "3.6"), (2, 0, AMBER, "2.4")]
    for i, j, col, wdt in legs:
        x1, y1 = nodes[i][1], nodes[i][2]
        x2, y2 = nodes[j][1], nodes[j][2]
        a = math.atan2(y2 - y1, x2 - x1)
        sx, sy = x1 + (R + 4) * math.cos(a), y1 + (R + 4) * math.sin(a)
        ex, ey = x2 - (R + 12) * math.cos(a), y2 - (R + 12) * math.sin(a)
        o.append('<path d="M %.1f %.1f L %.1f %.1f" fill="none" stroke="%s" stroke-width="%s" '
                 'opacity=".85"/>' % (sx, sy, ex, ey, col, wdt))
        o.append('<path d="M %.1f %.1f l %.1f %.1f l %.1f %.1f Z" fill="%s"/>'
                 % (ex, ey,
                    -10 * math.cos(a) - 5.5 * math.sin(a), -10 * math.sin(a) + 5.5 * math.cos(a),
                    11 * math.sin(a), -11 * math.cos(a), col))
    for name, x, y in nodes:
        o.append('<circle cx="%d" cy="%d" r="%d" fill="%s" opacity=".14"/>' % (x, y, R, IND))
        o.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="1.3"/>'
                 % (x, y, R, INK))
        o.append('<text x="%d" y="%d" class="mapt" text-anchor="middle">%s</text>'
                 % (x, y + 4, name))

    b = 396
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (b - 12, b - 12, RULE))
    cols = [(IND, "FIRST LEG", ["Indian cotton above all,", "then other textiles,",
                                "firearms, gunpowder,", "brandy; mirrors, coral,",
                                "hats, tobacco pipes"]),
            (OX, "THE MIDDLE PASSAGE", ["%d\u2013%d months." % (CROSSING_LO, CROSSING_HI),
                                       "About one in five of",
                                       "the people put aboard", "did not arrive."]),
            (AMBER, "THIRD LEG", ["raw sugar, refined in", "Copenhagen under",
                                  "monopoly and sold in", "two kingdoms"])]
    for i, (col, head, lines) in enumerate(cols):
        px = 26 + i * 218
        o.append('<rect x="%d" y="%d" width="22" height="9" fill="%s" opacity=".75"/>'
                 % (px, b + 2, col))
        o.append('<text x="%d" y="%d" class="mapx" fill="%s">%s</text>' % (px + 30, b + 10,
                                                                          col, head))
        for k, line in enumerate(lines):
            o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, b + 30 + k * 13, line))

    y = b + 104
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y - 14, y - 14, RULE))
    o.append('<text x="26" y="%d" class="mapl">%s\u2013%s</text>'
             % (y, format(CARRIED_LO, ",d"), format(CARRIED_HI, ",d")))
    o.append('<text x="210" y="%d" class="mapt">people carried in Danish ships, on about %d '
             'voyages, 1660s\u20131803</text>' % (y, VOYAGES))
    y += 20
    o.append('<text x="26" y="%d" class="mapl">2.3%%</text>' % y)
    o.append('<text x="210" y="%d" class="mapt">of the Atlantic traffic \u2014 which made Denmark '
             'the seventh largest</text>' % y)
    o.append('<text x="210" y="%d" class="mapt">of the nations that did it.</text>' % (y + 13))
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
SURVEYS = [
    ("1662 / 1664", "DENMARK", "Every farm in the kingdom converted into one unit, hartkorn. "
     "Nothing measured; the landlords' own books turned into a number that could be added up "
     "in Copenhagen.", "convert", IND),
    ("1682\u201383", "DENMARK", "Every cultivated field walked and measured, its area "
     "calculated and its soil graded, four sworn peasants per district going with the "
     "surveyors. On a Swedish model.", "measure", VERD),
    ("1734", "ST CROIX", "An island bought the year before, ruled into uniform lots on a grid "
     "and handed to the company's shareholders, who cleared it and planted cane.", "divide",
     AMBER),
]


def surveys():
    W, H = 700, 452
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Three panels showing the same state surveying land three times in seventy '
         'years: the Danish land register of 1662 and 1664, which converted dues into a single '
         'unit without measuring anything; the field survey of 1682 to 1683, which measured every '
         'cultivated field in Denmark; and the division of St Croix in 1734 into uniform '
         'plantation lots on a grid. The third is the only one never counted as an achievement '
         'of the enlightened state.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">THE SAME HABIT, THREE TIMES</text>')
    o.append('<text x="26" y="46" class="mapt">one state, seventy years, three ways of writing '
             'land down</text>')

    pw = 200
    for i, (yr, where, what, kind, col) in enumerate(SURVEYS):
        px = 26 + i * (pw + 16)
        o.append('<text x="%d" y="78" class="mapl" fill="%s">%s</text>' % (px, col, yr))
        o.append('<text x="%d" y="94" class="mapx">%s</text>' % (px, where))

        # a small emblem for each act, all on the same square
        ex, ey, es = px, 108, 150
        o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" opacity=".08"/>'
                 % (ex, ey, es, es, INK))
        if kind == "convert":
            for r in range(5):
                o.append('<text x="%d" y="%d" class="mapt">%s</text>'
                         % (ex + 8, ey + 26 + r * 24, ["3 tdr rye", "2 tdr barley", "1 pig",
                                                       "4 cart days", "2 geese"][r]))
                o.append('<text x="%d" y="%d" class="mapt" text-anchor="end">\u2192</text>'
                         % (ex + es - 34, ey + 26 + r * 24))
            o.append('<rect x="%d" y="%d" width="24" height="%d" fill="%s" opacity=".45"/>'
                     % (ex + es - 30, ey + 12, es - 24, col))
        elif kind == "measure":
            import random
            rnd = random.Random(1682)
            for _ in range(26):
                x = ex + 6 + rnd.random() * (es - 34)
                y = ey + 6 + rnd.random() * (es - 30)
                o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" '
                         'opacity=".40" stroke="%s" stroke-width=".5"/>'
                         % (x, y, 12 + rnd.random() * 18, 10 + rnd.random() * 14, col, col))
        else:
            for r in range(5):
                for c in range(5):
                    o.append('<rect x="%d" y="%d" width="24" height="24" fill="%s" '
                             'opacity=".40" stroke="%s" stroke-width=".6"/>'
                             % (ex + 10 + c * 26, ey + 10 + r * 26, col, col))

        y = ey + es + 20
        for line in wrap(what, 30):
            o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
            y += 13

    b = 396
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    o.append('<text x="26" y="%d" class="mapt">The first two are told in Denmark as the state '
             'learning to see itself: the foundation of</text>' % (b + 20))
    o.append('<text x="26" y="%d" class="mapt">modern administration. The third is the same '
             'instrument, in the same century, and it</text>' % (b + 33))
    o.append('<text x="26" y="%d" class="mapt">has never been counted as an achievement of the '
             'enlightened state.</text>' % (b + 46))
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
# (text, is_continuation). Continuation lines take no bullet: the first version
# gave the three-line date entry three bullets and it read as three records.
RECORDED = [
    ("Espen K\u00f8nig, master", False),
    ("Christian Runge, sailor, of Arendal", False),
    ("Axel Antoni, carpenter \u2014 died 4 January 1768", False),
    ("the other thirty-odd of the crew, by name", False),
    ("the wind, every day", False),
    ("the ship's position, every day", False),
    ("the cargo, itemised", False),
    ("the dates: Copenhagen 19 June 1767; the Gold", False),
    ("Coast 1 October; sailed 23 April 1768; St Croix", True),
    ("9 July; sailed 15 September; wrecked 1 December", True),
]
NOT_RECORDED = [
    "the names of the people in the hold",
    "where in Africa they were taken from",
    "what languages they spoke",
    "who among them was related to whom",
    "what any of them said",
]


def papers():
    W, H = 700, 470
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Two columns comparing what the surviving papers of the slave ship '
         'Fredensborg record and what they do not. The left column lists the master, the crew by '
         'name including the carpenter who died, the daily wind and position, the itemised cargo '
         'and the dates of every stage of the voyage. The right column lists what is absent: the '
         'names of the people in the hold, where they were taken from, their languages, their '
         'relationships, and anything any of them said.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">WHAT THE PAPERS KEEP</text>')
    o.append('<text x="26" y="46" class="mapt">the <tspan font-style="italic">Fredensborg</tspan>, '
             '1767\u201368 \u2014 the best-documented slave ship in the world</text>')
    o.append('<line x1="350" y1="70" x2="350" y2="390" stroke="%s" stroke-width="1"/>' % RULE)

    o.append('<text x="26" y="92" class="mapx" fill="%s">RECORDED</text>' % IND)
    y = 116
    for line, cont in RECORDED:
        if not cont:
            o.append('<circle cx="32" cy="%d" r="2.6" fill="%s"/>' % (y - 4, IND))
        o.append('<text x="44" y="%d" class="mapt">%s</text>' % (y, line))
        y += 20 if not cont else 14

    o.append('<text x="382" y="92" class="mapx" fill="%s">NOT RECORDED</text>' % MUTED)
    y = 116
    for line in NOT_RECORDED:
        o.append('<rect x="382" y="%d" width="%d" height="13" fill="%s" opacity=".10"/>'
                 % (y - 10, 268, MUTED))
        o.append('<text x="388" y="%d" class="mapt" fill="%s">%s</text>' % (y, MUTED, line))
        y += 20
    y += 8
    for line in wrap("They are in the documents. They are entered as a count, and when they die "
                     "they are entered as a loss.", 44):
        o.append('<text x="382" y="%d" class="mapt">%s</text>' % (y, line))
        y += 14

    b = 400
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    o.append('<text x="26" y="%d" class="mapt">The journals were carried ashore when the ship '
             'struck off Troms\u00f8ya on 1 December 1768.</text>' % (b + 20))
    o.append('<text x="26" y="%d" class="mapt">The wreck was found by divers in 1974. Both are '
             'now transcribed and public. The asymmetry</text>' % (b + 33))
    o.append('<text x="26" y="%d" class="mapt">above is not a gap in the archive. It is what the '
             'archive was for.</text>' % (b + 46))
    o.append('</svg>')
    return "\n  ".join(o)


if __name__ == "__main__":
    for name, fn in (("svg_triangle.txt", triangle),
                     ("svg_surveys.txt", surveys),
                     ("svg_papers.txt", papers)):
        svg = fn()
        validate(svg, name)
        w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
        bad = overruns(svg, w)
        if bad:
            print("   ! overruns in %s: %s" % (name, bad))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
