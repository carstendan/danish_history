# -*- coding: utf-8 -*-
"""Chapter 34's second and third figures. The map is map_1864.py.

  svg_dybbol_1864.txt   the bombardment record, and six casualty returns
  svg_ceded_1864.txt    what was lost: counted figures against disputed ones

BOTH FIGURES ARE ABOUT THE SAME PROBLEM, which is that 1864 is one of the
best-documented events in Danish history and two of its headline numbers cannot
be established.

FIGURE 2 DOES NOT RECONCILE THE CASUALTY FIGURES, and refusing to is the point.
Six published returns for 18 April 1864 are in circulation and they differ by a
factor of nearly ten on the Danish dead. The temptation is to pick the official
Danish return because it is official, or to average, or to quote a range. All
three would be wrong, and the reason is visible once the returns are set beside
each other with THEIR CATEGORIES SHOWN: they are not six answers to one question.
One counts dead; one counts dead and wounded together; one counts dead, wounded
and missing; one counts total losses including unwounded prisoners. A range built
across those is arithmetic performed on incommensurable things.

So the figure prints, for each source, the number AND what the number counts, and
says on its face that the spread is a spread of definitions as much as of facts.
The plague-toll figure in Part G established the pattern; this is the same refusal
with a clearer cause.

The bombardment record beside it is included precisely because it CAN be
established. The shell counts, the dates, the range of the guns and the depth of
the parallels are all attested and consistent. That contrast is the argument: the
engineering of the siege is better recorded than the number of men it killed.

FIGURE 3 SEPARATES WHAT DANMARKS STATISTIK COMPUTED FROM WHAT THE SOURCES ARGUE
ABOUT, in the same way chapter 33's franchise figure separated counts from
published ratios. The two population figures for the territories exchanged under
the treaty are exact at the 1860 census and are drawn solid. The share of area
lost, the share of population lost and the number of Danish-speakers ceded are
not, and are drawn as the ranges the sources give, with the sources named.

The net figure is COMPUTED HERE and asserted, not typed: 20,864 - 13,053 = 7,811,
and the script refuses to write if that ever stops being true. It is a small
number and it makes a point that nothing else on the page makes - the border
adjustment, considered on its own, moved more people INTO the kingdom than out of
it, which is true and is no consolation whatever.

Run: python3 figs_34.py
"""
import re
import xml.etree.ElementTree as ET

import mapspine as M

PAPER = "#F0F2EE"
RULE = "#C9CDC4"
SLATE = "#4F6470"
QUIET = "#A9B6BD"
WARM = "#A98C5F"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ====================================================================== figure 2
SIEGE = [
    ("1861\u201362", "Ten redoubts built in a three-kilometre arc, Vemmingbund to Als Sund"),
    ("7 Feb", "First Danish troops arrive from the Dannevirke. The position is unfinished"),
    ("15 Mar", "Rifled breech-loading guns emplaced on Broager Land, across the water"),
    ("", "Danish artillery cannot reach them and does not reply again"),
    ("2 Apr", "Sønderborg shelled; much of the town is reduced to rubble"),
    ("11 Apr", "Four thousand shells fall on the redoubts in one day"),
    ("mid-Apr", "Parallel trenches dug forward to three hundred metres"),
    ("18 Apr", "Bombardment 04.00\u201310.00: more than eight thousand shells in six hours"),
    ("10.00", "Assault. The central and southern redoubts are gone in half an hour"),
    ("11.30", "The 8th Brigade counter-attack breaks after ninety minutes"),
]

RETURNS = [
    ("Danish official return", "379", "killed"),
    ("Nationalmuseet", "700", "dead"),
    ("150th anniversary", "1,669", "dead AND wounded together"),
    ("Dybb\u00f8l Banke", "~1,800", "killed, wounded OR missing"),
    ("German account", "3,600", "killed"),
    ("danmarkshistorien.dk", "~5,000", "total lost, prisoners included"),
]


def dybbol():
    W = 700
    o = []
    head = ('<svg viewBox="0 0 %d %%d" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="Chart of the siege of the Dybb\u00f8l position in 1864 and of the '
            'six published casualty returns for the assault of 18 April. The siege record '
            'is consistent across sources: ten redoubts built in 1861 and 1862 in a '
            'three-kilometre arc, rifled breech-loading guns emplaced on Broager Land on 15 '
            'March which Danish artillery could not reach, four thousand shells on 11 April, '
            'parallels dug forward to three hundred metres, and more than eight thousand '
            'shells between four and ten in the morning of 18 April before the assault. The '
            'casualty returns are not consistent: the Danish official return gives 379 '
            'killed, Nationalmuseet 700 dead, a 150th-anniversary reckoning 1,669 dead and '
            'wounded together, Dybb\u00f8l Banke about 1,800 killed, wounded or missing, a '
            'German account 3,600 killed, and danmarkshistorien about 5,000 lost in total. '
            'They differ because they count different things as well as because both sides '
            'understated their own losses.">' % W)
    o.append('<text x="26" y="30" class="mapl">WHAT FELL ON THE REDOUBTS</text>')
    o.append('<text x="26" y="46" class="mapt">the siege of the Dybb\u00f8l position, '
             'February to 18 April 1864</text>')

    y = 74
    o.append('<text x="26" y="%d" class="mapx">ATTESTED, AND CONSISTENT ACROSS SOURCES</text>'
             % y)
    y += 22
    for when, what in SIEGE:
        if when:
            o.append('<text x="26" y="%d" class="mapx">%s</text> ' % (y, esc(when)))
        o.append('<text x="112" y="%d" class="mapt">%s</text>' % (y, esc(what)))
        y += 17

    y += 14
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y, y, RULE))
    y += 22
    o.append('<text x="26" y="%d" class="mapx">DISPUTED \u2014 SIX RETURNS FOR ONE '
             'MORNING</text>' % y)
    y += 20
    o.append('<text x="26" y="%d" class="mapt">The spread is a spread of definitions as much '
             'as of facts. These are not six</text>' % y)
    y += 15
    o.append('<text x="26" y="%d" class="mapt">answers to one question, so no range is drawn '
             'across them and none should be.</text>' % y)
    y += 26

    for src, n, counts in RETURNS:
        o.append('<rect x="26" y="%d" width="9" height="9" fill="%s"/>' % (y - 8, WARM))
        o.append('<text x="44" y="%d" class="mapl">%s</text> ' % (y, esc(n)))
        o.append('<text x="120" y="%d" class="mapt">%s</text> ' % (y, esc(counts)))
        o.append('<text x="446" y="%d" class="mapx">%s</text>' % (y, esc(src)))
        y += 19

    y += 10
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y, y, RULE))
    y += 18
    o.append('<text x="26" y="%d" class="mapt">Both sides understated their own losses and '
             'overstated the enemy\u2019s, which historians</text>' % y)
    y += 14
    o.append('<text x="26" y="%d" class="mapt">give as the reason for the rest of the gap. '
             'The engineering of the siege is better</text>' % y)
    y += 14
    o.append('<text x="26" y="%d" class="mapt">recorded than the number of men it '
             'killed.</text>' % y)

    H = int(y + 12)
    o.append('</svg>')
    return (head % H) + '\n  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>\n  ' \
        % (W, H, PAPER) + "\n  ".join(o)


# ====================================================================== figure 3
CEDED_POP = 13053      # Ribe Amt parishes ceded, at the 1860 census
GAINED_POP = 20864     # Ærø and mainland stretches received, at the 1860 census
KINGDOM_1860 = 1600551
KINGDOM_1870 = 1784741

DISPUTED = [
    ("Share of the monarchy's area lost", "a third", "two fifths",
     "Nationalmuseet gives both, on different pages"),
    ("Share of its population lost", "about 40 per cent", "",
     "widely repeated; no census breakdown found"),
    ("Danish-speakers ceded", "170,000", "200,000",
     "Nationalmuseet against other accounts"),
]


def ceded():
    net = GAINED_POP - CEDED_POP
    assert net == 7811, "the exchange nets %d, not 7,811" % net

    W = 700
    o = []
    head = ('<svg viewBox="0 0 %d %%d" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="Chart separating the figures for Denmark\u2019s losses in 1864 that '
            'Danmarks Statistik computed from the figures the sources disagree about. '
            'Counted at the census of 1860: the parishes of Ribe Amt ceded under the treaty '
            'held 13,053 people, and the territory received in exchange, \u00c6r\u00f8 and '
            'smaller mainland stretches, held 20,864, so the border adjustment considered on '
            'its own moved 7,811 more people into the kingdom than out of it. The kingdom '
            'held 1,600,551 people in 1860 and 1,784,741 in 1870. Disputed: whether the '
            'monarchy lost a third or two fifths of its area, and whether 170,000 or 200,000 '
            'Danish-speakers passed under German rule.">' % W)
    o.append('<text x="26" y="30" class="mapl">COUNTED, AND DISPUTED</text>')
    o.append('<text x="26" y="46" class="mapt">what Denmark lost in 1864, and which of the '
             'figures can be stood behind</text>')

    y = 76
    o.append('<text x="26" y="%d" class="mapx">COUNTED \u2014 DANMARKS STATISTIK, AT THE '
             'CENSUS OF 1860</text>' % y)
    y += 24
    # Labels shortened and the bars moved right after looking: the longer of the two
    # ran under its own bar, and collisions() compares text with text and cannot see a
    # <rect> laid over a <text>. Same blind spot as chapter 33's franchise key.
    rows = [("Ceded to the duchies: Ribe Amt parishes", CEDED_POP),
            ("Received from Slesvig: \u00c6r\u00f8 and mainland", GAINED_POP)]
    bw, bx = 236, 342
    top = max(n for _, n in rows)
    for lbl, n in rows:
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (y, esc(lbl)))
        o.append('<rect x="%d" y="%d" width="%.1f" height="12" fill="%s"/>'
                 % (bx, y - 10, bw * n / float(top) + 0.0, SLATE))
        o.append('<text x="674" y="%d" class="mapl" text-anchor="end">%s</text>'
                 % (y, "{:,}".format(n)))
        y += 24
    o.append('<text x="26" y="%d" class="mapt">The exchange therefore moved this many MORE '
             'people into the kingdom</text>' % y)
    o.append('<text x="674" y="%d" class="mapl" text-anchor="end">+%s</text>'
             % (y, "{:,}".format(net)))
    y += 22
    for lbl, n in (("Kingdom of Denmark, census of 1860", KINGDOM_1860),
                   ("Kingdom of Denmark, census of 1870", KINGDOM_1870)):
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (y, esc(lbl)))
        o.append('<text x="674" y="%d" class="mapl" text-anchor="end">%s</text>'
                 % (y, "{:,}".format(n)))
        y += 19

    y += 12
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y, y, RULE))
    y += 22
    o.append('<text x="26" y="%d" class="mapx">DISPUTED \u2014 DRAWN AS RANGES, WITH THE '
             'SOURCES NAMED</text>' % y)
    y += 26
    for lbl, a, b, who in DISPUTED:
        o.append('<rect x="26" y="%d" width="9" height="9" fill="none" stroke="%s" '
                 'stroke-width="1"/>' % (y - 8, WARM))
        o.append('<text x="44" y="%d" class="mapt">%s</text> ' % (y, esc(lbl)))
        val = a if not b else "%s \u2014 %s" % (a, b)
        o.append('<text x="352" y="%d" class="mapl">%s</text>' % (y, esc(val)))
        y += 15
        o.append('<text x="44" y="%d" class="mapt" opacity=".75">%s</text>' % (y, esc(who)))
        y += 22

    y += 2
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y, y, RULE))
    y += 18
    o.append('<text x="26" y="%d" class="mapt">No total is computed from the disputed rows '
             'and none should be. Multiplying a share</text>' % y)
    y += 14
    o.append('<text x="26" y="%d" class="mapt">nobody counted by a population nobody agreed '
             'on produces a number that looks</text>' % y)
    y += 14
    o.append('<text x="26" y="%d" class="mapt">counted and is not.</text>' % y)

    H = int(y + 12)
    o.append('</svg>')
    return (head % H) + '\n  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>\n  ' \
        % (W, H, PAPER) + "\n  ".join(o)


if __name__ == "__main__":
    for name, fn in (("svg_dybbol_1864.txt", dybbol),
                     ("svg_ceded_1864.txt", ceded)):
        svg = fn()
        ET.fromstring(svg)
        w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
        h = int(re.search(r'viewBox="0 0 \d+ (\d+)', svg).group(1))
        for bad in (M.check(svg, name) or []):
            print("  !! %s: %s" % (name, bad))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars, %dx%d)" % (name, len(svg), w, h))
