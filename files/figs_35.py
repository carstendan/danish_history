# -*- coding: utf-8 -*-
"""Chapter 35's three figures.

  svg_omlaegning_1875.txt   why Danish farming turned round: the dated chain
  svg_udvandring_1868.txt   who left, 1868-1900
  svg_andel_1882.txt        the four rules of the Hjedding contract

TWO OF THESE ARE NOT THE FIGURES PLAN_H ASKED FOR, and both changed for the same
reason: the series exist and I could not reach them.

FIGURE 1. The plan asked for "two price series crossing, from the published Danish
price statistics", carrying sections 02 to 04 in one image. The right series is the
kapitelstakst, the officially published average grain price computed by district
since the seventeenth century and still computed today. Its modern values are
published; the nineteenth-century run is in the printed Statistisk Tabelvaerk and
in the back-series of the statistics bank, and neither was obtained here.

THIS IS THE SAME UNFETCHED DOCUMENT AS CHAPTER 32's FIGURE 3, which carries the
note that "the continuous Zealand kapitelstakst for rye exists in print from 1651;
its year-by-year values were not obtained, and the figure says so instead of
estimating them." Two chapters now want the same table. Getting it once would let
both figures be redrawn as planned, and it is a library errand rather than an
archive one.

What is drawn instead is the causal chain with the dates the sources DO give,
which is what the plan actually wanted the two lines for - "carries 02 to 04 in one
image". A chain cannot be mistaken for measurement, which a hand-drawn price line
could be. That is the plantation-plat rule from Part G: a figure that looks like
data must be data.

FIGURE 2. The plan asked for emigration by year from the Copenhagen police
registers, "which are close to complete and are the right source rather than an
estimate." Correct on both counts, and out of reach: the registers are ninety
volumes, digitised and searchable by name, but the annual totals were not obtained.
Three points in the series are attested - 1882, 1885, 1891/92 - and a line through
three known values and thirty invented ones is exactly the thing the plan was
guarding against.

So the figure draws WHO LEFT rather than WHEN, on the occupational composition,
which is the better figure anyway because it is the one that answers the chapter's
myth-check: more than four in ten emigrants were agricultural labourers, and the
cooperative movement of figure 3 did not admit them. The three attested points are
marked as points, without a line between them, and the Nordic comparison is set
beside it.

CONSEQUENCE FOR L4, stated because the plan raised it. PLAN_H noted a "mild L4
tension" in having two time series and one diagram, and said that if a third series
crept in, one should become a map. The opposite happened: both series went, leaving
one chart and two diagrams. That is within L4 and needs no further correction, but
if the kapitelstakst is ever fetched, figure 1 becomes a time series and the
tension the plan predicted arrives after all.

FIGURE 3 IS THE ONE THE PLAN ASKED FOR. The four rules are quoted from the contract
itself. The fourth - unlimited joint liability - is the one usually left out of
popular accounts, and it is given the same weight as the others here because it is
what made the other three financeable and what fixed the boundary of who could be a
member at all.

Run: python3 figs_35.py
"""
import re
import xml.etree.ElementTree as ET

import mapspine as M

PAPER = "#F0F2EE"
RULE = "#C9CDC4"
SLATE = "#4F6470"
QUIET = "#A9B6BD"
WARM = "#A98C5F"
GREEN = "#6E8A72"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wrap(head, body, W, H):
    return (head % H) + '\n  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>\n  ' \
        % (W, H, PAPER) + "\n  ".join(body)


# ====================================================================== figure 1
# IN ORDER. The first draft opened at 1875 and then stepped back to 1864, which
# reads as a mistake on a figure whose whole form is a chain. Caught by looking.
CHAIN = [
    ("since 1864", "No land route south",
     "The German market now lies across a customs frontier at the Konge\u00e5."),
    ("from 1875", "World grain prices fall",
     "American plains opened by railways given the land; Russian grain; steam shipping."),
    ("late 1870s", "The continuous separator",
     "Milk from many suppliers can be handled together. Joint dairies stop failing."),
    ("1881", "Germany bans live cattle imports",
     "The nearest market for the animal itself closes. What is left is the milk."),
    ("1882", "Hjedding writes the rules",
     "Twenty-six farmers in \u00d8lgod; within twenty years more than a thousand dairies."),
    ("1887", "The first cooperative slaughterhouse",
     "Horsens, 14 July: 23,400 pigs and 1.1 million kilos of pork in the first year."),
    ("1901", "The state stamps the butter",
     "The Lur mark registered, and handed to the government as the quality stamp."),
]

TAIL1 = [
    "The reversal is the part that is easy to miss. A country that had exported grain for",
    "centuries ended the period importing it \u2014 buying foreign grain cheaply, feeding it to",
    "Danish animals, and exporting what the animals produced. The cheap American harvest",
    "that ruined the Danish grain farmer became the raw material of the Danish dairy farmer,",
    "and it arrived on the same ships that took the butter out.",
]


def omlaegning():
    W = 700
    head = ('<svg viewBox="0 0 %d %%d" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="Diagram of the chain of events by which Danish farming turned from '
            'grain to butter and bacon between 1875 and 1901. World grain prices fall from '
            'about 1875 under American and Russian competition carried by steam shipping. '
            'The loss of 1864 has already put a customs frontier on the land route south. '
            'The continuous cream separator arrives at the end of the 1870s and makes joint '
            'dairying workable. Germany bans imports of live cattle in 1881, closing the '
            'nearest market for the animal itself. In 1882 twenty-six farmers at Hjedding '
            'in \u00d8lgod parish write the rules that a thousand cooperative dairies then '
            'copy. In 1887 the first cooperative slaughterhouse opens at Horsens. In 1901 '
            'the Lur mark is registered as the official quality stamp for butter. The net '
            'effect is that Denmark stopped exporting grain and began importing it, to feed '
            'to animals whose product it exported instead.">' % W)
    o = []
    o.append('<text x="26" y="30" class="mapl">WHY DANISH FARMING TURNED ROUND</text>')
    o.append('<text x="26" y="46" class="mapt">the chain from falling grain prices to butter '
             'sold in England</text>')

    y = 82
    for i, (when, what, why) in enumerate(CHAIN):
        o.append('<text x="26" y="%d" class="mapx">%s</text> ' % (y, esc(when)))
        o.append('<rect x="118" y="%d" width="8" height="8" fill="%s"/>'
                 % (y - 7, WARM if i in (1, 3) else SLATE))
        o.append('<text x="138" y="%d" class="mapl">%s</text>' % (y, esc(what)))
        o.append('<text x="138" y="%d" class="mapt">%s</text>' % (y + 15, esc(why)))
        if i < len(CHAIN) - 1:
            o.append('<line x1="122" y1="%d" x2="122" y2="%d" stroke="%s" '
                     'stroke-width="1"/>' % (y + 3, y + 33, RULE))
        y += 46

    o.append('<text x="26" y="%d" class="mapt" opacity=".8">The two marked in the warmer '
             'tone were decided outside Denmark.</text>' % (y - 8))
    y += 14
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y, y, RULE))
    y += 20
    for line in TAIL1:
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (y, esc(line)))
        y += 14
    H = int(y + 6)
    o.append('</svg>')
    return wrap(head, o, W, H)


# ====================================================================== figure 2
OCCUPATIONS = [
    ("Agricultural labourers", 42, "more than four in ten"),
    ("Urban working class", 25, "about one in four; for women, above all servants"),
    ("Everyone else", 33, "farmers' sons without a farm, artisans, families, the devout"),
]

POINTS = [("1882", 11400, "the peak"),
          ("1885", 4200, "the trough three years later"),
          ("1891\u201392", 9700, "the second peak")]

NORDIC = [("Denmark", 309000), ("Norway", 754000), ("Sweden", 1105000)]


def udvandring():
    W = 700
    head = ('<svg viewBox="0 0 %d %%d" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="Chart of Danish overseas emigration between 1868 and 1900. About '
            '309,000 Danes left, against 754,000 Norwegians and 1,105,000 Swedes. By '
            'occupation, more than four in ten were agricultural labourers and about one in '
            'four were urban working class, among women above all servants. Three points in '
            'the annual series are attested: about 11,400 emigrants in 1882, about 4,200 in '
            '1885, and about 9,700 at the second peak in 1891 and 1892. The occupational '
            'figures are the argument of the chart: the people leaving were not the '
            'freeholders who founded the cooperative dairies.">' % W)
    o = []
    o.append('<text x="26" y="30" class="mapl">WHO LEFT</text>')
    o.append('<text x="26" y="46" class="mapt">Danish overseas emigration, 1868\u20131900: '
             'about 309,000 people out of some two million</text>')

    y = 78
    o.append('<text x="26" y="%d" class="mapx">BY OCCUPATION \u2014 THE POINT OF THIS '
             'CHART</text>' % y)
    y += 22
    bx, bw = 250, 300
    for lbl, pct, note in OCCUPATIONS:
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (y, esc(lbl)))
        # TONE BY MEANING, NOT BY SIZE. The first version picked the emphasis tone
        # for any bar over 30 per cent, which put the residual "everyone else" row
        # in the same dark tone as the row the chart is about. Caught by looking.
        o.append('<rect x="%d" y="%d" width="%.1f" height="12" fill="%s"/>'
                 % (bx, y - 10, bw * pct / 100.0 + 0.0,
                    QUIET if lbl.startswith("Everyone") else SLATE))
        o.append('<text x="%d" y="%d" class="mapl">%d%%</text>' % (bx + bw + 12, y, pct))
        y += 15
        o.append('<text x="26" y="%d" class="mapt" opacity=".75">%s</text>' % (y, esc(note)))
        y += 22

    o.append('<text x="26" y="%d" class="mapt">Read that against figure 3. The cooperative '
             'admitted men who owned land and cows.</text>' % y)
    y += 22
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y, y, RULE))

    y += 22
    o.append('<text x="26" y="%d" class="mapx">THE THREE YEARS THAT CAN BE ATTESTED</text>' % y)
    y += 16
    o.append('<text x="26" y="%d" class="mapt">Drawn as points and not joined. The '
             'year-by-year run exists in the Copenhagen police</text>' % y)
    y += 14
    o.append('<text x="26" y="%d" class="mapt">registers and was not obtained; a line '
             'through three known values would invent thirty.</text>' % y)
    y += 20
    # THE AXIS MAXIMUM IS THE AXIS MAXIMUM, not the data maximum. The first
    # version scaled to the largest point and then labelled the end of the line
    # 12,000, so the axis said one thing and the geometry said another. Caught by
    # looking, and it is the kind of error that makes a chart quietly lie.
    top = 12000.0
    o.append('<line x1="110" y1="%d" x2="370" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y, y, RULE))
    o.append('<text x="110" y="%d" class="mapt" opacity=".7">0</text>' % (y + 12))
    o.append('<text x="370" y="%d" class="mapt" opacity=".7" text-anchor="end">12,000 in a '
             'year</text>' % (y + 12))
    y += 26
    for when, n, note in POINTS:
        o.append('<text x="26" y="%d" class="mapx">%s</text> ' % (y, esc(when)))
        o.append('<circle cx="%.1f" cy="%d" r="5" fill="%s"/>'
                 % (110 + 260 * n / float(top) + 0.0, y - 4, WARM))
        o.append('<text x="410" y="%d" class="mapl">%s</text> ' % (y, "{:,}".format(n)))
        o.append('<text x="486" y="%d" class="mapt">%s</text>' % (y, esc(note)))
        y += 20

    y += 8
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y, y, RULE))
    y += 22
    o.append('<text x="26" y="%d" class="mapx">AND FOR SCALE, 1868\u20131900</text>' % y)
    y += 22
    top2 = max(n for _, n in NORDIC)
    for lbl, n in NORDIC:
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (y, esc(lbl)))
        o.append('<rect x="%d" y="%d" width="%.1f" height="11" fill="%s" opacity=".8"/>'
                 % (bx, y - 9, bw * n / float(top2) + 0.0, GREEN))
        o.append('<text x="%d" y="%d" class="mapl">%s</text>'
                 % (bx + bw + 12, y, "{:,}".format(n)))
        y += 19
    H = int(y + 8)
    o.append('</svg>')
    return wrap(head, o, W, H)


# ====================================================================== figure 3
RULES = [
    ("Deliver everything",
     "All the milk your cows give goes to the dairy, clean, unskimmed, none from a sick "
     "cow and none from a newly calved one before the seventh milking.",
     "Adulterate it and you are expelled and fined ten kroner a cow. These clauses read "
     "as fussiness and are the product specification: England paid for sameness."),
    ("Be paid alike",
     "The same price per kande of milk for every supplier, whatever the quantity.",
     "The small farmer gets the large farmer's price. This is what made joining worth "
     "anything to a man with eight cows."),
    ("One member, one vote",
     "Each member has one vote at the general meeting regardless of how many cows he "
     "owns. In Danish: not by heads of cattle, but by heads.",
     "The general meeting is the highest authority. The wording was taken from the "
     "rules of the parish savings bank and fire-insurance association."),
    ("Stand behind each other",
     "All the members are liable for the debts of all, alle som \u00e9n og \u00e9n som alle, "
     "with the whole of their property.",
     "USUALLY LEFT OUT, AND IT CARRIES THE REST. The bank was not lending against the "
     "dairy; it was lending against every farm in the parish."),
]


def andel():
    W = 700
    head = ('<svg viewBox="0 0 %d %%d" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="Diagram of the four rules of the Hjedding cooperative dairy '
            'contract of 1882. First, every member delivers all his milk, clean and '
            'unskimmed and not from a sick cow, on pain of expulsion and a fine of ten '
            'kroner a cow. Second, every supplier is paid the same price per measure '
            'whatever the quantity. Third, every member has one vote at the general meeting '
            'regardless of the size of his herd, the wording taken from the rules of the '
            'parish savings bank and fire-insurance association. Fourth, and usually left '
            'out of popular accounts, all the members are jointly and unlimitedly liable '
            'for the debts of all with the whole of their property, which is what allowed '
            'farmers without capital to borrow for a steam engine and a separator, and '
            'which also fixed the boundary of who could be admitted as a member at all.">'
            % W)
    o = []
    o.append('<text x="26" y="30" class="mapl">HOW A COOPERATIVE WAS OWNED</text>')
    o.append('<text x="26" y="46" class="mapt">the four rules of the Hjedding contract, '
             '\u00d8lgod parish, 1882</text>')

    y = 80
    for i, (title, what, why) in enumerate(RULES):
        o.append('<rect x="26" y="%d" width="26" height="26" fill="%s" opacity="%s"/>'
                 % (y - 18, WARM if i == 3 else SLATE, ".9" if i == 3 else ".75"))
        o.append('<text x="39" y="%d" class="mapl" text-anchor="middle" fill="%s">%d</text>'
                 % (y, PAPER, i + 1))
        o.append('<text x="68" y="%d" class="mapl">%s</text>' % (y - 6, esc(title)))
        yy = y + 10
        for line in _fold(what, 74):
            o.append('<text x="68" y="%d" class="mapt">%s</text>' % (yy, esc(line)))
            yy += 14
        yy += 4
        for line in _fold(why, 74):
            o.append('<text x="68" y="%d" class="mapt" opacity=".75">%s</text>'
                     % (yy, esc(line)))
            yy += 14
        y = yy + 20

    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y - 12, y - 12, RULE))
    o.append('<text x="26" y="%d" class="mapt">A member was therefore a man who owned land '
             'and cows and could pledge them. The</text>' % (y + 8))
    o.append('<text x="26" y="%d" class="mapt">husm\u00e6nd and the tyende could not be '
             'admitted even in principle: see figure 2.</text>' % (y + 22))
    H = int(y + 34)
    o.append('</svg>')
    return wrap(head, o, W, H)


def _fold(text, n):
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


if __name__ == "__main__":
    for name, fn in (("svg_omlaegning_1875.txt", omlaegning),
                     ("svg_udvandring_1868.txt", udvandring),
                     ("svg_andel_1882.txt", andel)):
        svg = fn()
        ET.fromstring(svg)
        w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
        h = int(re.search(r'viewBox="0 0 \d+ (\d+)', svg).group(1))
        for bad in (M.check(svg, name) or []):
            print("  !! %s: %s" % (name, bad))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars, %dx%d)" % (name, len(svg), w, h))
