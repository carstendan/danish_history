# -*- coding: utf-8 -*-
"""Chapter 36's three figures.

  svg_franchises_1866.txt   the two chambers and the two electorates
  svg_deadlock_1873.txt     what each power could do, and the box nobody filled
  svg_vestvold_1888.txt     the rampart the constitution was broken for

FIGURE 2 IS NOT WHAT PLAN_H ASKED FOR. The plan wanted "seats against votes,
1872-1901 - Venstre's Folketing majority against Hojre's Landsting control across
the conflict. The deadlock as a structure rather than a clash of two men."

The intent is exactly right and the form was wrong for the sources available. A
seats-and-votes series for thirty years of Danish elections exists - the results
were published at the time and are in the standard reference works - and it was not
obtained here. What I have is the direction and not the numbers: that Hojre never
came close to a Folketing majority in these years and that the Landsting franchise
protected it in the other chamber throughout. Drawing a thirty-year double series
from that would be inventing about sixty values, which is the third time in Part H
that a planned time series has had to be refused for the same reason. See HANDOFF
53 and figs_35.py.

But look at what the plan said the series was FOR: "the deadlock as a structure
rather than a clash of two men." A structure is drawable without a series, and on
this chapter's argument it is the better figure, because the chapter's claim is
that the fault was not in either party but in a silence. So figure 2 draws the
powers - what the Folketing could do, what the Landsting could do, what the king
could do - and then the empty box: the procedure for settling a disagreement
between them, which the constitution did not contain. THE BLANK IS THE ARGUMENT,
in the same way the empty Slesvig column is the argument in chapter 33's figure 1.

IF THE ELECTION SERIES IS EVER FETCHED it should be drawn as well, not instead.
Two figures, one showing that the majority never wavered and one showing that the
majority never mattered, would be better than either alone.

FIGURE 3 HAS NO COST FIGURE AND SAYS SO. The plan asked for the Vestvold "with its
cost". The construction quantities are well documented - length, dates, cubic
metres, workforce, method - and the money is not, at least not anywhere I reached.
Since the whole political point of the fortification is that it was paid for out of
a budget the elected chamber had refused, a cost figure would have been the single
most useful number on the page, and inventing or rounding one would have been the
worst possible place to do it. The figure carries the quantities, which are real,
and states the absence.

FIGURE 1 IS THE ONE THE PLAN ASKED FOR and it needs no apology: both franchises are
in the electoral law and the Landsting's composition is a list of small integers
that add to sixty-six. That total is asserted in code below.

Run: python3 figs_36.py
"""
import re
import xml.etree.ElementTree as ET

import mapspine as M

PAPER = "#F0F2EE"
RULE = "#C9CDC4"
SLATE = "#4F6470"
QUIET = "#A9B6BD"
WARM = "#A98C5F"
EARTH = "#8A7A5E"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def fold(text, n):
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


def wrap(head, body, W, H):
    return (head % H) + '\n  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>\n  ' \
        % (W, H, PAPER) + "\n  ".join(body)


# ====================================================================== figure 1
LANDSTING = [("chosen by the king, for life", 12),
             ("chosen by the Faroese Lagting", 1),
             ("chosen by Bornholm's amtsr\u00e5d", 1),
             ("chosen indirectly, through electors", 52)]
LANDSTING_TOTAL = 66

FOLKETING_RULES = [
    "Every man of unblemished reputation",
    "with Danish indf\u00f8dsret",
    "aged thirty",
    "with a household of his own",
    "not in another's service without one",
    "and never in receipt of unrepaid poor relief",
]

LANDSTING_RULES = [
    "Half the electors chosen by all those voters",
    "The other half chosen by the highest taxpayers alone",
    "Town and country seats fixed in the law itself,",
    "with no provision for future shifts of population",
]


def franchises():
    tot = sum(n for _, n in LANDSTING)
    assert tot == LANDSTING_TOTAL, "the Landsting sums to %d, not %d" % (tot, LANDSTING_TOTAL)

    W = 700
    head = ('<svg viewBox="0 0 %d %%d" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="Diagram comparing the two chambers of the Danish Rigsdag as the '
            'constitutional revision of 1866 left them. The Folketing was elected by every '
            'man of unblemished reputation with Danish citizenship, aged thirty, with a '
            'household of his own, not in another\u2019s service without one, and never in '
            'receipt of unrepaid poor relief. The Landsting had sixty-six members: twelve '
            'chosen by the king for life, one by the Faroese Lagting, one by Bornholm\u2019s '
            'county council and fifty-two chosen indirectly through electors, of whom half '
            'were chosen by the ordinary voters and half by the highest taxpayers alone, '
            'with the distribution of seats between town and country frozen into the law. '
            'From 1872 the Folketing was carried by Venstre and the Landsting by '
            'H\u00f8jre.">' % W)
    o = []
    o.append('<text x="26" y="30" class="mapl">TWO CHAMBERS, TWO ELECTORATES</text>')
    o.append('<text x="26" y="46" class="mapt">the Rigsdag as the revision of 28 July 1866 '
             'left it</text>')

    colw, x1, x2 = 310, 26, 364
    for x, name, party, rules in ((x1, "FOLKETINGET", "carried by Venstre from 1872",
                                   FOLKETING_RULES),
                                  (x2, "LANDSTINGET", "carried by H\u00f8jre",
                                   LANDSTING_RULES)):
        o.append('<rect x="%d" y="66" width="%d" height="30" fill="%s" opacity="%s"/>'
                 % (x, colw, SLATE if x == x1 else EARTH, ".8"))
        o.append('<text x="%d" y="86" class="mapl" fill="%s">%s</text>'
                 % (x + 12, PAPER, name))
        o.append('<text x="%d" y="114" class="mapx">%s</text>' % (x, esc(party)))
        yy = 138
        for r in rules:
            o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (x, yy, esc(r)))
            yy += 15

    # the sixty-six, as blocks
    y = 224
    o.append('<text x="%d" y="%d" class="mapx">ITS SIXTY-SIX MEMBERS</text>' % (x2, y))
    y += 20
    BOX, GAP, PER = 9, 4, 24
    tones = []
    for lbl, n in LANDSTING:
        tones += [(lbl, EARTH if "indirectly" in lbl else QUIET)] * n
    for i, (lbl, tone) in enumerate(tones):
        r, c = divmod(i, PER)
        o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s"/>'
                 % (x2 + c * (BOX + GAP), y + r * (BOX + GAP), BOX, BOX, tone))
    y += 3 * (BOX + GAP) + 12
    for lbl, n in LANDSTING:
        o.append('<rect x="%d" y="%d" width="8" height="8" fill="%s"/>'
                 % (x2, y - 7, EARTH if "indirectly" in lbl else QUIET))
        o.append('<text x="%d" y="%d" class="mapl">%2d</text> ' % (x2 + 16, y, n))
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (x2 + 44, y, esc(lbl)))
        y += 16

    # TWO FIXES HERE, BOTH FOUND BY LOOKING. First, this prose shared a baseline with
    # the right column's heading (the guard caught that one, at 8 units). Second, and
    # invisible to every guard, the lines then ran straight under the block grid at
    # x2: collisions() compares text with text and a <rect> over a <text> is not
    # tested. Fourth time this session. Folded to the column width instead.
    yy = 246
    for line in fold("Neither chamber was unrepresentative. That is the difficulty: both "
                     "reflected exactly the electorate they were designed to reflect, and "
                     "those two electorates wanted opposite things.", 45):
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (x1, yy, esc(line)))
        yy += 15
    o.append('<text x="%d" y="%d" class="mapx">AND NEITHER COULD DISSOLVE,</text>'
             % (x1, yy + 14))
    o.append('<text x="%d" y="%d" class="mapx">DISMISS OR OUTVOTE THE OTHER</text>'
             % (x1, yy + 30))

    H = int(max(y, 330) + 16)
    o.append('</svg>')
    return wrap(head, o, W, H)


# ====================================================================== figure 2
POWERS = [
    ("THE FOLKETING", "could", [
        "reject the finance bill",
        "reject a provisional law afterwards",
        "vote down any expenditure it chose",
        "be re-elected on the same majority"], SLATE),
    ("THE LANDSTING", "could", [
        "reject anything the Folketing passed",
        "keep its composition regardless of",
        "how the country's population moved"], EARTH),
    ("THE KING", "could", [
        "appoint whichever ministers he chose",
        "dissolve the Rigsdag",
        "sign a provisional law under \u00a725"], WARM),
]

MISSING = [
    "No procedure existed for settling a disagreement between the two chambers.",
    "No procedure existed for removing a ministry the elected chamber did not want.",
    "The Folketing could say no. Nothing made the no mean anything.",
]


def deadlock():
    W = 700
    head = ('<svg viewBox="0 0 %d %%d" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="Diagram of the Danish constitutional deadlock between 1873 and '
            '1901, drawn as a structure. The Folketing could reject the finance bill, '
            'reject a provisional law after the fact, vote down any expenditure and be '
            're-elected on the same majority. The Landsting could reject anything the '
            'Folketing passed and keep its composition regardless of population change. '
            'The king could appoint whichever ministers he chose, dissolve the Rigsdag and '
            'sign a provisional law under article 25. What did not exist was any procedure '
            'for settling a disagreement between the two chambers or for removing a '
            'ministry the elected chamber did not want: the Folketing could say no, and '
            'nothing made the no mean anything. The empty box is the argument of the '
            'chapter.">' % W)
    o = []
    o.append('<text x="26" y="30" class="mapl">WHAT EACH COULD DO \u2014 AND WHAT NOBODY '
             'COULD</text>')
    o.append('<text x="26" y="46" class="mapt">the deadlock of 1873\u20131901 as a '
             'structure, not as a quarrel between two men</text>')

    x, w, gap = 26, 208, 8
    top = 74
    # THE BOX HEIGHT IS COMPUTED, NOT TYPED. It was hardcoded to 132 and two of the
    # three columns overflowed it, spilling their last lines out through the bottom
    # border and into the dashed box below. Nothing fired: overruns() tests the
    # canvas, not a rectangle drawn inside it. Caught by looking. Fold each column
    # first, take the tallest, then draw all three boxes to that.
    cols = []
    for name, verb, items, tone in POWERS:
        lines = []
        for it in items:
            lines += fold(it, 30) + ['']
        cols.append((name, verb, lines, tone))
    boxh = 62 + max(len(c[2]) for c in cols) * 14 + 10

    for i, (name, verb, lines, tone) in enumerate(cols):
        cx = x + i * (w + gap)
        o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s" '
                 'stroke-width="1"/>' % (cx, top, w, boxh, tone))
        o.append('<rect x="%d" y="%d" width="%d" height="24" fill="%s" opacity=".8"/>'
                 % (cx, top, w, tone))
        o.append('<text x="%d" y="%d" class="mapl" fill="%s">%s</text>'
                 % (cx + 10, top + 17, PAPER, name))
        yy = top + 44
        o.append('<text x="%d" y="%d" class="mapx">%s</text>' % (cx + 10, yy, verb))
        yy += 18
        for line in lines:
            if line:
                o.append('<text x="%d" y="%d" class="mapt">%s</text>'
                         % (cx + 10, yy, esc(line)))
            yy += 14

    y = top + boxh + 24
    o.append('<rect x="26" y="%d" width="648" height="112" fill="none" stroke="%s" '
             'stroke-width="1.5" stroke-dasharray="6 5" opacity=".7"/>' % (y, SLATE))
    o.append('<text x="46" y="%d" class="mapl" opacity=".8">THE BOX THE CONSTITUTION DID '
             'NOT CONTAIN</text>' % (y + 28))
    yy = y + 54
    for line in MISSING:
        o.append('<text x="46" y="%d" class="mapt">%s</text>' % (yy, esc(line)))
        yy += 16

    y = y + 132
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y, y, RULE))
    y += 20
    for line in ("Estrup did not break a rule that existed. He stood in the place where one "
                 "should have been,",
                 "and stayed there for nineteen years. The gap was the fault. That is the "
                 "chapter's argument,",
                 "and it is why this figure is a structure and not a scoreboard."):
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (y, esc(line)))
        y += 14
    H = int(y + 8)
    o.append('</svg>')
    return wrap(head, o, W, H)


# ====================================================================== figure 3
VOLD = [
    ("Built", "1888\u20131892; the wider land defences from 1886"),
    ("Length", "14 km, Utterslev Mose to K\u00f8ge Bugt, continuous except where an"),
    ("", "existing road or railway passed through"),
    ("Designed by", "Lieutenant-Colonel E.J. Sommerfeldt \u2014 a saw-toothed plan with the"),
    ("", "guns in protected caponiers, known abroad as the Danish Front"),
    ("Directed by", "J.J. Bahnson, Estrup's war minister"),
    ("Earth moved", "about 3,150,000 cubic metres of earth and chalk"),
    ("Workforce", "about 2,000 local contractors and day labourers"),
    ("Method", "shovels, wheelbarrows and tip-wagons; concrete mixed by hand in"),
    ("", "tubs, because mixing machines did not yet exist; a railway laid"),
    ("", "along the rampart road on worn-out track cast off by the state"),
    ("Paid for by", "provisional finance law, against the vote of the Folketing"),
]

AFTER = [
    ("1894", "The settlement stops further building"),
    ("1909", "Decided that the land fortification be abolished from 1922"),
    ("1914", "A security force of 50,000 called up to hold it"),
    ("1918", "Four years later, having seen no fighting, they go home"),
    ("1920", "Abolished on 1 April, two years early"),
]


def vestvold():
    W = 700
    head = ('<svg viewBox="0 0 %d %%d" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="Table of the Vestvold, the western rampart of the Copenhagen land '
            'fortification. Built between 1888 and 1892, fourteen kilometres long from '
            'Utterslev Mose to K\u00f8ge Bugt, designed by Lieutenant-Colonel E.J. '
            'Sommerfeldt and directed by Estrup\u2019s war minister J.J. Bahnson. About '
            '3,150,000 cubic metres of earth and chalk were moved by some two thousand men '
            'using shovels, wheelbarrows and tip-wagons, with the concrete mixed by hand '
            'because mixing machines did not yet exist. It was paid for by provisional '
            'finance law against the vote of the Folketing. Further building stopped with '
            'the settlement of 1894; in 1909 it was decided to abolish the land '
            'fortification from 1922; fifty thousand men were called up to hold it in 1914 '
            'and saw no fighting; and it was abolished on 1 April 1920. Its money cost was '
            'not obtained and is not given here.">' % W)
    o = []
    o.append('<text x="26" y="30" class="mapl">THE RAMPART THE CONSTITUTION WAS BROKEN '
             'FOR</text>')
    o.append('<text x="26" y="46" class="mapt">Vestvolden, and what became of it</text>')

    y = 76
    for k, v in VOLD:
        if k:
            o.append('<text x="26" y="%d" class="mapx">%s</text> ' % (y, esc(k)))
        o.append('<text x="140" y="%d" class="mapt">%s</text>' % (y, esc(v)))
        y += 16

    y += 10
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y, y, RULE))
    y += 22
    o.append('<text x="26" y="%d" class="mapx">AND THEN</text>' % y)
    y += 22
    for k, v in AFTER:
        o.append('<text x="26" y="%d" class="mapl">%s</text> ' % (y, esc(k)))
        o.append('<rect x="90" y="%d" width="8" height="8" fill="%s"/>'
                 % (y - 7, EARTH if k in ("1894", "1909", "1920") else QUIET))
        o.append('<text x="112" y="%d" class="mapt">%s</text>' % (y, esc(v)))
        y += 19

    y += 8
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y, y, RULE))
    y += 20
    o.append('<text x="26" y="%d" class="mapt">The money cost is not given here because it '
             'was not obtained. Since the political point of</text>' % y)
    y += 14
    o.append('<text x="26" y="%d" class="mapt">this rampart is that it was paid for out of '
             'a budget the elected chamber had refused, the</text>' % y)
    y += 14
    o.append('<text x="26" y="%d" class="mapt">figure in kroner would be the most useful '
             'number on the page, and the worst one to guess.</text>' % y)
    H = int(y + 14)
    o.append('</svg>')
    return wrap(head, o, W, H)


if __name__ == "__main__":
    for name, fn in (("svg_franchises_1866.txt", franchises),
                     ("svg_deadlock_1873.txt", deadlock),
                     ("svg_vestvold_1888.txt", vestvold)):
        svg = fn()
        ET.fromstring(svg)
        w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
        h = int(re.search(r'viewBox="0 0 \d+ (\d+)', svg).group(1))
        for bad in (M.check(svg, name) or []):
            print("  !! %s: %s" % (name, bad))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars, %dx%d)" % (name, len(svg), w, h))
