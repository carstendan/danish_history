# -*- coding: utf-8 -*-
"""Chapter 27's two non-map figures. The third is the 1721 spine map.

  svg_plague.txt   what the state did, and what it could not count
  svg_schools.txt  two hundred and forty-one schools in six years

THE PLAGUE FIGURE IS NOT THE ONE THAT WAS PLANNED. The plan called for a weekly
burial curve from the parish bills. The bills are in Koebenhavns Stadsarkiv and
the reference works do not agree with each other closely enough to reconstruct one
from them: the same period is given as over a hundred deaths a day and as two to
three thousand a week, and the total as 20,000, as about 25,000, as a third of the
city and as forty per cent, against a population itself put at 60,000 or 69,000.

A worked example can be labelled as constructed and still be honest, as the
hartkorn page in chapter 25 is. A mortality curve cannot: inventing weekly values
for real deaths is the one place where a plausible-looking data figure would do
the most damage. So the figure draws what can be established - the sequence of
measures, which is well dated - and shows the toll as the spread of estimates it
actually is. The uncertainty is the finding, and hiding it would be the error.

Run: python3 figs_27.py
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
    # 6.1 units per character, measured off the raster. The 5.55 inherited from
    # figs_24.py under-reports by about ten per cent and passed two figures in
    # chapter 26 that had text off the canvas.
    bad = []
    for m in re.finditer(r'<text x="([\d.]+)"(?![^>]*text-anchor="(?:end|middle)")[^>]*>([^<]*)<',
                         svg):
        if float(m.group(1)) + len(m.group(2)) * 6.1 > W - 6:
            bad.append(m.group(2)[:44])
    return bad


# ------------------------------------------------------------------ figure 2
# (label, date, what, held?) held: the period the quarantine kept it out
MEASURES = [
    ("1709", "Quarantine on Saltholm: forty days for anyone from an infected port. "
             "Ships turned away.", True),
    ("May 1711", "In the city anyway.", False),
    ("31 May", "All seventeen residents of one house in Lille Gr\u00f8nnegade taken to "
               "Saltholm.", False),
    ("late June", "Mortality climbing steeply.", False),
    ("3 July", "Placard: no funeral processions; death for sheltering fugitives from "
               "Helsing\u00f8r.", False),
    ("7 July", "Extraordinary health commission given emergency powers. It meets twice a "
               "day.", False),
    ("July", "Two plague hospitals outside the ramparts. Coffins run out; burial without "
             "one permitted.", False),
    ("Aug\u2013Sep", "Convicts released to dig. The army opens mass graves beyond "
                     "\u00d8sterport.", False),
    ("2 Apr 1712", "The gates open for normal traffic.", False),
    ("29 Apr 1712", "A national day of thanksgiving.", False),
]
# Every published figure I could find, with its source, and the population it is
# a proportion of. Nothing here is averaged: they are shown disagreeing.
ESTIMATES = [
    ("K\u00f8benhavns Stadsarkiv", 25000, 25000),
    ("\"about 20,000\"", 20000, 20000),
    ("\"every third inhabitant\"", 20000, 23000),
    ("\"about 40 per cent\"", 24000, 27600),
]
POP_LO, POP_HI = 60000, 69000


def plague():
    W = 700
    top = 118
    gap = 30
    H = top + len(MEASURES) * gap + 214
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Two panels on the Copenhagen plague of 1711. The upper panel is a dated '
         'sequence of the measures the state took, from the Saltholm quarantine of 1709 through '
         'the health commission of July 1711 to the reopening of the gates in April 1712. The '
         'lower panel shows four published estimates of the death toll as bars, ranging from '
         'twenty thousand to about twenty-seven thousand six hundred, against a city whose '
         'population is itself given as between sixty and sixty-nine thousand. The estimates are '
         'shown disagreeing rather than averaged.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">WHAT THE STATE DID</text>')
    o.append('<text x="26" y="46" class="mapt">the first time the machinery of 1660 was turned '
             'on a disease</text>')
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (top - 26, top - 26, RULE))

    for i, (when, what, held) in enumerate(MEASURES):
        y = top + i * gap
        col = VERD if held else IND
        o.append('<circle cx="34" cy="%d" r="3.6" fill="%s"/>' % (y - 4, col))
        if i < len(MEASURES) - 1:
            o.append('<line x1="34" y1="%d" x2="34" y2="%d" stroke="%s" stroke-width="1" '
                     'opacity=".45"/>' % (y - 1, y + gap - 8, MUTED))
        o.append('<text x="50" y="%d" class="mapx" fill="%s">%s</text>' % (y, col, when))
        lines = wrap(what, 62)
        o.append('<text x="150" y="%d" class="mapt">%s</text>' % (y, lines[0]))
        for k, line in enumerate(lines[1:]):
            o.append('<text x="150" y="%d" class="mapt">%s</text>' % (y + 13 * (k + 1), line))

    b = top + len(MEASURES) * gap + 16
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    o.append('<text x="26" y="%d" class="mapl">WHAT IT COULD NOT COUNT</text>' % (b + 24))
    o.append('<text x="26" y="%d" class="mapt">four published figures for the same five months, '
             'shown disagreeing</text>' % (b + 40))

    x0, xw = 210, 400
    hi = 30000.0
    for i, (who, lo, hii) in enumerate(ESTIMATES):
        y = b + 62 + i * 22
        o.append('<text x="%d" y="%d" class="mapt" text-anchor="end">%s</text>'
                 % (x0 - 10, y, who))
        o.append('<rect x="%d" y="%d" width="%.1f" height="11" fill="%s" opacity=".50"/>'
                 % (x0, y - 9, xw * hii / hi, IND))
        if lo != hii:
            o.append('<rect x="%d" y="%d" width="%.1f" height="11" fill="%s" opacity=".30"/>'
                     % (x0, y - 9, xw * lo / hi, IND))
        lab = format(hii, ",d") if lo == hii else "%s\u2013%s" % (format(lo, ",d"),
                                                                  format(hii, ",d"))
        o.append('<text x="%.1f" y="%d" class="mapt">%s</text>'
                 % (x0 + xw * hii / hi + 8, y, lab))

    yy = b + 62 + len(ESTIMATES) * 22 + 16
    o.append('<text x="26" y="%d" class="mapt">Population of the city: given as %s in some '
             'accounts and %s in others.</text>'
             % (yy, format(POP_LO, ",d"), format(POP_HI, ",d")))
    o.append('<text x="26" y="%d" class="mapt">The bills of mortality survive in the city '
             'archive. Nobody in this chapter has counted them.</text>' % (yy + 14))
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
DISTRICTS = 12
PER_DISTRICT = 20
BUILT = 241     # 240 in the twelve districts, plus Bogoe outside them, 11 June 1727
PRICE = 550                      # rigsdaler, every school the same
YEARS = [1722, 1723, 1724, 1725, 1726, 1727]
LEN_M, WID_M, HGT_M = 13.2, 7.5, 2.8


def schools():
    W, H = 700, 506
    planned = DISTRICTS * PER_DISTRICT
    total = BUILT * PRICE
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Diagram of the royal cavalry-district schools ordered in March 1721. '
         'Twelve districts at twenty schools each were planned, two hundred and forty in all, and '
         'two hundred and forty were built between 1722 and 1727, and one more on Bog\u00f8 by '
         'royal resolution of 11 June 1727, outside the twelve districts, making two hundred '
         'and forty-one. Every one was to the same drawing, 13.2 metres by 7.5, and the budget '
         'figure was 550 rigsdaler each, though a costing of March 1722 put a single building '
         'at 651. A plan of the standard building is shown with the sandstone '
         'tablet that went over its door.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">TWO HUNDRED AND FORTY-ONE, IN SIX YEARS</text>')
    o.append('<text x="26" y="46" class="mapt">signed 28 March 1721; tendered that winter; '
             'built 1722\u201327</text>')

    # twelve districts of twenty, drawn as twelve blocks of twenty marks
    o.append('<text x="26" y="80" class="mapx">TWELVE DISTRICTS, TWENTY SCHOOLS EACH</text>')
    n = 0
    for d in range(DISTRICTS):
        col, row = d % 4, d // 4
        bx = 26 + col * 108
        by = 96 + row * 52
        for k in range(PER_DISTRICT):
            x = bx + (k % 10) * 9
            y = by + (k // 10) * 10
            o.append('<rect x="%d" y="%d" width="6" height="7" fill="%s" opacity=".55"/>'
                     % (x, y, IND))
            n += 1
        o.append('<text x="%d" y="%d" class="mapt">district %d</text>' % (bx, by + 32, d + 1))
    o.append('<text x="466" y="%d" class="mapx">%d planned</text>' % (100, planned))
    o.append('<text x="466" y="%d" class="mapt">%d built in them</text>' % (116, DISTRICTS * PER_DISTRICT))
    o.append('<text x="466" y="%d" class="mapx">and one more on Bog\u00f8</text>' % 140)
    o.append('<text x="466" y="%d" class="mapt">by royal resolution of</text>' % 156)
    o.append('<text x="466" y="%d" class="mapt">11 June 1727, outside</text>' % 169)
    o.append('<text x="466" y="%d" class="mapt">the twelve districts</text>' % 182)
    o.append('<text x="466" y="%d" class="mapl">%d in all</text>' % (206, BUILT))

    # the standard building, to scale, against the cottage it replaced
    y0 = 274
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y0 - 16, y0 - 16, RULE))
    o.append('<text x="26" y="%d" class="mapx">ONE DRAWING, ONE PRICE</text>' % y0)
    px_m = 11.0
    o.append('<rect x="26" y="%d" width="%.1f" height="%.1f" fill="%s" opacity=".18"/>'
             % (y0 + 26, LEN_M * px_m, WID_M * px_m, IND))
    o.append('<rect x="26" y="%d" width="%.1f" height="%.1f" fill="none" stroke="%s" '
             'stroke-width="1.4"/>' % (y0 + 26, LEN_M * px_m, WID_M * px_m, INK))
    o.append('<text x="%.1f" y="%d" class="mapt" text-anchor="middle">%.1f m</text>'
             % (26 + LEN_M * px_m / 2, y0 + 20, LEN_M))
    o.append('<text x="%.1f" y="%.1f" class="mapt">%.1f m</text>'
             % (26 + LEN_M * px_m + 8, y0 + 26 + WID_M * px_m / 2, WID_M))
    o.append('<text x="26" y="%.1f" class="mapt">brick walls, tiled roof, %.1f m floor to '
             'ceiling</text>' % (y0 + 42 + WID_M * px_m, HGT_M))
    o.append('<text x="26" y="%.1f" class="mapt">in a countryside of clay daub and thatch</text>'
             % (y0 + 55 + WID_M * px_m))

    px = 380
    o.append('<text x="%d" y="%d" class="mapx">%d rigsdaler each, budgeted</text>' % (px, y0 + 20, PRICE))
    o.append('<text x="%d" y="%d" class="mapl">%s rigsdaler</text>'
             % (px, y0 + 42, format(total, ",d")))
    o.append('<text x="%d" y="%d" class="mapt">at the budget rate. A costing of</text>' % (px, y0 + 58))
    o.append('<text x="%d" y="%d" class="mapt">March 1722 put one at 651.</text>' % (px, y0 + 71))
    yy = y0 + 92
    for line in wrap("Krieger, the royal architect, and a brickworks owner at Niv\u00e5 put up a "
                     "hundred and forty-nine of them between them. Attendance compulsory from "
                     "five, girls as well as boys. Reading and Christian learning free; writing "
                     "and arithmetic eight skilling a month, which many could not find.", 48):
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, yy, line))
        yy += 13

    b = H - 44
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    o.append('<text x="26" y="%d" class="mapt">The districts were where the crown held land, so '
             'West Jutland and north-west Zealand got</text>' % (b + 18))
    o.append('<text x="26" y="%d" class="mapt">none at all. The design was still being copied for '
             'village schools in the 1890s.</text>' % (b + 32))
    o.append('</svg>')
    return "\n  ".join(o)


if __name__ == "__main__":
    for name, fn in (("svg_plague_1711.txt", plague),
                     ("svg_schools.txt", schools)):
        svg = fn()
        validate(svg, name)
        w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
        bad = overruns(svg, w)
        if bad:
            print("   ! overruns in %s: %s" % (name, bad))
        M.overflows(svg, name)
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
