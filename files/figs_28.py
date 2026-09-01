# -*- coding: utf-8 -*-
"""Chapter 28's three figures.

  svg_hovyear.txt   a bound man's year, counted rather than dated
  svg_norway.txt    what Norway sent south
  svg_catechism.txt seven hundred and fifty-nine questions, fifty of them asked

THE FIRST FIGURE IS NOT A CALENDAR, and the plan called for one. A calendar wheel
would have to place the hoveri days in particular weeks, and the sources do not
record that: the reckonings prepared for Christian 7.'s commission give annual
totals and the split between spanddage and gangdage, nothing more. Drawing 110
days in specific months would be inventing the one thing a reader would take from
the figure. So the figure counts and says it is counting, and the seasonal
concentration is stated in words, where it can be hedged.

Run: python3 figs_28.py
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
    bad = []
    for m in re.finditer(r'<text x="([\d.]+)"(?![^>]*text-anchor="(?:end|middle)")[^>]*>([^<]*)<',
                         svg):
        if float(m.group(1)) + len(m.group(2)) * 6.1 > W - 6:
            bad.append(m.group(2)[:44])
    return bad


def land_clip(f, polys, near, w, h, cid):
    return ('<clipPath id="%s"><path d="%s"/></clipPath>'
            % (cid, M.detail_land_path(f, polys, near, w, h)))


# ------------------------------------------------------------------ figure 1
DAYS = 365
SPAND, GANG = 40, 70            # the Zealand reckoning: 110 days
ALT_SPAND, ALT_GANG = 34, 88    # the Antvorskov reckoning: 122 days


def hovyear():
    owed = SPAND + GANG
    alt = ALT_SPAND + ALT_GANG
    W, H = 700, 516
    cols, cell, gap = 25, 15, 3
    rows = (DAYS + cols - 1) // cols
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="A grid of three hundred and sixty-five squares, one for each day of the '
         'year. One hundred and ten of them are marked as days a Zealand tenant owed his '
         'landlord: forty requiring a wagon and a team, seventy on foot. A second reckoning from '
         'another estate gives a hundred and twenty-two days. The marked squares are grouped '
         'together for counting and do not show which days of the year were owed, because the '
         'sources give annual totals and not dates.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">A BOUND MAN\'S YEAR</text>')
    o.append('<text x="26" y="46" class="mapt">every square is one day; the marked ones belong '
             'to somebody else</text>')

    top = 74
    for i in range(DAYS):
        r, c = divmod(i, cols)
        x = 26 + c * (cell + gap)
        y = top + r * (cell + gap)
        if i < SPAND:
            fill, op = IND, ".72"
        elif i < owed:
            fill, op = IND, ".34"
        else:
            fill, op = MUTED, ".13"
        o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="1.5" fill="%s" opacity="%s"/>'
                 % (x, y, cell, cell, fill, op))

    b = top + rows * (cell + gap) + 10
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))

    y = b + 22
    o.append('<rect x="26" y="%d" width="15" height="15" rx="1.5" fill="%s" opacity=".72"/>'
             % (y - 12, IND))
    o.append('<text x="48" y="%d" class="mapx">%d spanddage \u2014 a wagon and a team</text>'
             % (y, SPAND))
    y += 22
    o.append('<rect x="26" y="%d" width="15" height="15" rx="1.5" fill="%s" opacity=".34"/>'
             % (y - 12, IND))
    o.append('<text x="48" y="%d" class="mapx">%d gangdage \u2014 a person on foot; a girl or a '
             'boy would do</text>' % (y, GANG))
    y += 22
    o.append('<rect x="26" y="%d" width="15" height="15" rx="1.5" fill="%s" opacity=".13"/>'
             % (y - 12, MUTED))
    o.append('<text x="48" y="%d" class="mapx">%d days that were his own</text>' % (y, DAYS - owed))

    px = 430
    o.append('<text x="%d" y="%d" class="mapl">%d of %d</text>' % (px, b + 22, owed, DAYS))
    o.append('<text x="%d" y="%d" class="mapt">roughly two days in seven</text>' % (px, b + 38))
    o.append('<text x="%d" y="%d" class="mapt">A second reckoning, from an estate at</text>'
             % (px, b + 58))
    o.append('<text x="%d" y="%d" class="mapt">Antvorskov, gives %d \u2014 %d and %d.</text>'
             % (px, b + 71, alt, ALT_SPAND, ALT_GANG))
    o.append('<text x="26" y="%d" class="mapt">The squares are grouped for counting. Which days '
             'of the year were owed is not recorded: the</text>' % (b + 96))
    o.append('<text x="26" y="%d" class="mapt">figures come from specimen reckonings made when '
             'the government tried to regulate hoveri,</text>' % (b + 109))
    o.append('<text x="26" y="%d" class="mapt">and they give totals. What is agreed is that the '
             'demand fell hardest at ploughing, sowing</text>' % (b + 122))
    o.append('<text x="26" y="%d" class="mapt">and harvest \u2014 the only weeks when a man\'s own '
             'crop could not wait.</text>' % (b + 135))
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
NBOX = (4.0, 57.6, 14.2, 64.6)
NNEAR = (0.0, 54.0, 22.0, 68.0)
# (lon, lat, name, what, kind) kind: s silver, c copper, t town, m mint
# (lon, lat, name, what, kind, anchor, dy). Anchors are set per site, not derived
# from longitude: the first version put Bergen's label off the left of the canvas
# and stacked Kongsberg on Christiania.
SITES = [
    (9.65, 59.67, "Kongsberg", "silver from 1623", "s", "end", 4),
    (11.38, 62.57, "R\u00f8ros", "copper from 1644", "c", "start", 0),
    (9.72, 63.11, "L\u00f8kken", "copper from 1654", "c", "end", 0),
    (10.00, 62.13, "Folldal", "copper from 1748", "c", "end", 0),
    (10.75, 59.91, "Christiania", "mint 1628\u201386", "m", "start", -14),
    (10.40, 63.43, "Trondhjem", "the copper burghers", "t", "start", -14),
    (5.32, 60.39, "Bergen", "the largest town", "t", "start", 0),
]


def norway():
    W, H = 700, 520
    mw, mh = 400, 438
    f = M.detail_frame(NBOX, mw, mh)
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Map of southern and central Norway marking the mining places that supplied '
         'the Danish crown: the silver works at Kongsberg from 1623, the copper works at Roeros '
         'from 1644, Loekken from 1654 and Folldal from 1748, with the mint at Christiania and '
         'later Kongsberg, and the towns of Trondhjem and Bergen. A panel lists what went south '
         'and what Norway received in return.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="14" y="24" class="mapl">WHAT NORWAY SENT SOUTH</text>')
    o.append('<text x="14" y="40" class="mapt">and what came back the other way</text>')
    o.append('<g transform="translate(0,52)">')
    o.extend(M.detail_base(f, mw, mh, NNEAR, scale=50, clip="no"))

    for lon, lat, name, what, kind, anc, ndy in SITES:
        x, y = f.xy(lon, lat)
        if kind == "s":
            o.append('<circle cx="%.1f" cy="%.1f" r="6" fill="%s" opacity=".85"/>' % (x, y, IND))
        elif kind == "c":
            o.append('<circle cx="%.1f" cy="%.1f" r="5" fill="%s" opacity=".75"/>' % (x, y, AMBER))
        elif kind == "m":
            o.append('<rect x="%.1f" y="%.1f" width="9" height="9" fill="%s" opacity=".75"/>'
                     % (x - 4.5, y - 4.5, VERD))
        else:
            o.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s"/>' % (x, y, MUTED))
        dx = 9 if anc == "start" else -9
        o.append('<text x="%.1f" y="%.1f" class="mapx" text-anchor="%s">%s</text>'
                 % (x + dx, y - 1 + ndy, anc, name))
        o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="%s">%s</text>'
                 % (x + dx, y + 11 + ndy, anc, what))
    o.append('</g>')
    o.append('</g>')

    px = 424
    y = 76
    o.append('<text x="%d" y="%d" class="mapx">SOUTH</text>' % (px, y))
    for line in ["silver, coined at Kongsberg",
                 "copper, iron, timber",
                 "regiments, when there was a war",
                 "carting duty, hauling the ore",
                 "taxes, collected under threat"]:
        y += 15
        o.append('<circle cx="%d" cy="%.1f" r="2.4" fill="%s"/>' % (px + 4, y - 4, IND))
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px + 14, y, line))

    y += 28
    o.append('<text x="%d" y="%d" class="mapx">NORTH</text>' % (px, y))
    for line in ["Danish grain, and after 1735",
                 "no other kind was allowed",
                 "Norske Lov, 1687",
                 "a governor, when the sea closed"]:
        y += 15
        o.append('<circle cx="%d" cy="%.1f" r="2.4" fill="%s"/>' % (px + 4, y - 4, VERD))
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px + 14, y, line))

    y += 30
    o.append('<line x1="%d" y1="%d" x2="686" y2="%d" stroke="%s" stroke-width="1"/>'
             % (px, y, y, RULE))
    y += 20
    o.append('<text x="%d" y="%d" class="mapl">4,075</text>' % (px, y))
    for line in wrap("people employed at Kongsberg in 1770, with a couple of thousand farmers "
                     "besides in seasonal work. It was the largest enterprise in either kingdom, "
                     "and the town was the second in Norway after Bergen.", 28):
        y += 14
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
    y += 22
    for line in wrap("Norway kept its own law, its own coin and its own regiments. It was not a "
                     "colony. The metal still went south.", 28):
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
        y += 14
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
QUESTIONS = 759
ASKED = 50
AUTHORISED = [(1738, "Christian 6."), (1748, "Frederik 5."), (1768, "Christian 7.")]


def catechism():
    W = 700
    cols = 33
    rows = (QUESTIONS + cols - 1) // cols
    cell, gap = 11, 3
    top = 96
    H = top + rows * (cell + gap) + 148
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Seven hundred and fifty-nine small squares, one for each question in '
         'Pontoppidan\'s catechism of 1737. Fifty of them are marked, being the number a '
         'candidate could be asked at the public examination in church. The marked ones are '
         'scattered through the whole set, because the candidate did not know which would be '
         'chosen and had to learn them all.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">SEVEN HUNDRED AND FIFTY-NINE QUESTIONS</text>')
    o.append('<text x="26" y="46" class="mapt">Pontoppidan, <tspan font-style="italic">Sandhed '
             'til Gudfrygtighed</tspan>, 1737 \u2014 the required book for every child in two '
             'kingdoms</text>')
    o.append('<text x="26" y="72" class="mapx">Any fifty of them, in front of the congregation. '
             'You did not know which fifty.</text>')

    # A seeded draw, not modular arithmetic. The first version stepped by a fixed
    # interval and produced neat diagonal stripes across the grid, which implied a
    # pattern in the examination that did not exist. Seeded so the figure is
    # reproducible; the seed is the year of publication.
    import random
    marked = set(random.Random(1737).sample(range(QUESTIONS), ASKED))
    for i in range(QUESTIONS):
        r, c = divmod(i, cols)
        x = 26 + c * (cell + gap)
        y = top + r * (cell + gap)
        if i in marked:
            o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="1" fill="%s" '
                     'opacity=".85"/>' % (x, y, cell, cell, IND))
        else:
            o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="1" fill="%s" '
                     'opacity=".16"/>' % (x, y, cell, cell, MUTED))

    b = top + rows * (cell + gap) + 12
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    y = b + 22
    o.append('<text x="26" y="%d" class="mapx">Re-authorised by three kings in succession</text>'
             % y)
    for i, (yr, who) in enumerate(AUTHORISED):
        o.append('<text x="%d" y="%d" class="mapt">%d \u2014 %s</text>'
                 % (26 + i * 150, y + 18, yr, who))
    y += 46
    for line in wrap("Required by law until 1794. Used in Danish religious teaching through the "
                     "whole eighteenth century and in Norway through the nineteenth as well. It "
                     "is probably the book by a Danish author that has been printed in more "
                     "copies than any other. Confirmation became compulsory in 1736; the state "
                     "was obliged to provide the teaching by the school ordinance of 1739.", 96):
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (y, line))
        y += 14
    o.append('</svg>')
    return "\n  ".join(o)


if __name__ == "__main__":
    for name, fn in (("svg_hovyear.txt", hovyear),
                     ("svg_norway.txt", norway),
                     ("svg_catechism.txt", catechism)):
        svg = fn()
        validate(svg, name)
        w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
        bad = overruns(svg, w)
        if bad:
            print("   ! overruns in %s: %s" % (name, bad))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
