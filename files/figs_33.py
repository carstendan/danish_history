# -*- coding: utf-8 -*-
"""Chapter 33's three figures.

  svg_descent_1848.txt    two succession laws, one king, and an empty column
  svg_sprog_1839.txt      P.C. Koch's language count of 1839, by his categories
  svg_franchise_1849.txt  who could vote in 1849: counts and published ratios

FIGURE 2 IS NOT THE ONE PLAN_H ASKED FOR, and the divergence is deliberate.
PLAN_H §6 asked for "the language boundary in Slesvig - from a named
nineteenth-century survey with surveyor and date on the face of the figure,
because these surveys were themselves instruments of the argument. The figure
must show it is a claim."

The intent is right and the form was wrong, for two reasons.

First, drawing a boundary needs the boundary. The project has no polygon source
for a nineteenth-century Slesvig language line, and mapkit/mapspine work from
Natural Earth coastlines and hand-entered lon/lat, neither of which contains one.
Tracing a line by eye off a photograph of Koch's map and calling it Koch's line
would be the plantation-plat failure from Part G: it would look like data and a
reader would have no way to tell that it was not.

Second, and better: the sources do supply something stronger. There are TWO maps,
a year apart, and they disagree - Franz Heinrich Julius Geerz, the German-minded
cartographer and officer, in 1838, and P.C. Koch, the Danish editor of Dannevirke
in Haderslev, in 1839, published as an answer. They disagree partly because they
asked different questions: Geerz asked where Danish or German was superior, Koch
worked with mixed areas. A single line, however honestly sourced, hides that. The
categories do not.

So the figure draws KOCH'S OWN LEGEND: six categories and six populations, from
his printed key, with his own total. Every number is his. The argument is in the
categories - he did not count Danes and Germans, he counted the language of the
kitchen against the language of the church and the school - and the figure shows
that the same survey yields 33, 43 or 57 per cent Danish depending on where a
reader draws the line. That is the "it is a claim" the plan wanted, made out of a
partisan's own arithmetic rather than asserted in a caption.

KOCH'S TOTAL RECONCILES EXACTLY. 110,213 + 23,392 + 10,630 + 47,207 + 119,935 +
26,815 = 338,192, which is the figure printed on his key. That is checked in code
below and the script refuses to write if it ever stops being true. The percentages
on the figure are computed, never typed.

IF A USABLE BOUNDARY SOURCE TURNS UP - a georeferenced Koch or Geerz, or the
sogn-level assignments behind either - the map version becomes possible and should
be drawn ALONGSIDE this, not instead of it. Two lines on one frame, labelled with
their surveyors, is the figure the plan was reaching for.

FIGURE 3 SEPARATES COUNTS FROM RATIOS ON ITS FACE. The census total and the 1849
election returns are counts and are drawn solid. The 15 per cent of the population
and the 72.8 per cent of men over thirty are published proportions, and deriving a
count of men over thirty by dividing one by the other would be exactly L14's
"computing from numbers someone else typed". They are drawn in outline and
labelled as ratios, and no count is derived from them.

FIGURE 1 CARRIES A DELIBERATE BLANK. The middle column is empty because the
sources are empty: the incorporation of 1721 was carried through without
introducing the kingdom's law, and nothing between then and 1846 settled which
succession ran in Slesvig. Filling it with either answer would be taking a side in
a dispute that Erslev reopened in 1901 and that is still open. The blank is the
finding.

Run: python3 figs_33.py
"""
import re
import xml.etree.ElementTree as ET

import mapspine as M

INK = "#3C3E36"
PAPER = "#F0F2EE"
RULE = "#C9CDC4"
SLATE = "#4F6470"          # Part H band colour
# SIX CATEGORIES NEED SIX TONES. The first version gave the three Danish-vernacular
# bands one colour and the two German-vernacular bands another, so the proportional
# band at the top read as four segments and the swatches could not be matched to it.
# The segment edges that were visible came from adjacent translucent fills, which is
# a rendering artefact and not a designed boundary. This is the Part G village figure
# exactly - six households drawn in five colours, and the whole claim was "the same
# six households". Shades within a family, so the grouping survives.
DANE1, DANE2, DANE3 = "#6E809E", "#8B9BB4", "#A8B4C6"
GERM1, GERM2 = "#A98C5F", "#C6AF8A"
MIXED = "#9AA39B"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ====================================================================== figure 1
# Each column: (heading, rule, [steps]). A step of None is a deliberate gap.
COLS = [
    ("KONGERIGET", "Kongeloven 1665.", [
        "Agnatic \u2014 but the female",
        "line opens if the male",
        "line fails. It failed.",
        None,
        "Frederik 7., no children",
        "Prince Ferdinand, none",
        "Louise Charlotte, d. 1824",
        "m. Wilhelm of Hesse",
        "Louise of Hesse",
        "\u2192 her husband Christian",
        "of Gl\u00fccksburg",
    ]),
    ("SLESVIG", "No instrument says.", [
        "A fief of the Danish crown,",
        "not of the Empire.",
        None,
        "1721: the Gottorp share",
        "incorporated \u2014 without the",
        "kingdom's law, its courts",
        "or its language.",
        None,
        "1846: the Open Letter",
        "asserts the Kongelov runs",
        "here. It asserts it.",
    ]),
    ("HOLSTEN", "Agnatic, and only that.", [
        "Man to man. No female",
        "line, no opening, no",
        "exception.",
        None,
        "Frederik 7., no children",
        "the nearest agnates are",
        "the dukes of Augustenborg",
        None,
        "\u2192 Christian August 2.",
        "of Augustenborg",
        "",
    ]),
]

TAIL1 = [
    "How it was actually settled: not by either law. The Treaty of London of 8 May",
    "1852 excluded women from the succession in all the king's lands \u2014 which is the",
    "Holstein rule \u2014 and then gave the whole inheritance to the one man whose claim",
    "came through his wife. Louise renounced in favour of Christian of Gl\u00fccksburg.",
    "Both cases were conceded and both were defeated, in a single sentence.",
]


def descent():
    W, H = 700, 556
    x0, colw, gap = 26, 208, 8
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Diagram of the Danish succession crisis as it stood in 1848. Three '
         'columns: the kingdom of Denmark, the duchy of Slesvig and the duchy of Holstein. '
         'The kingdom followed the Kongelov of 1665, which was agnatic but opened the female '
         'line when the male line failed; with Frederik 7. childless and Prince Ferdinand '
         'without legitimate children, the claim ran through his aunt Louise Charlotte and '
         'her daughter Louise of Hesse to Louise\u2019s husband Christian of Gl\u00fccksburg. '
         'Holstein followed a purely agnatic law, under which the nearest heirs were the '
         'dukes of Augustenborg. The Slesvig column is empty, because the incorporation of '
         '1721 was carried through without introducing the kingdom\u2019s law, courts or '
         'language, and nothing before the Open Letter of 1846 settled which succession '
         'applied there. The Treaty of London of 8 May 1852 resolved it by neither law: it '
         'excluded women from the succession in all the king\u2019s lands, the Holstein rule, '
         'and then settled the whole inheritance on the one claimant who held his claim '
         'through his wife.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">TWO LAWS, ONE KING, AND A COLUMN NOBODY '
             'COULD FILL</text>')
    o.append('<text x="26" y="46" class="mapt">the succession as it stood when Frederik 7. '
             'came to the throne, January 1848</text>')

    # the common root
    ry = 74
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (ry, ry, RULE))
    o.append('<text x="26" y="%d" class="mapx">BOTH LAWS COUNT FROM FREDERIK 3., D. 1670 '
             '\u2014 AND IN 1848 HIS MALE LINE IS ABOUT TO RUN OUT</text>' % (ry + 18))

    top = ry + 40
    for i, (head, rule, steps) in enumerate(COLS):
        cx = x0 + i * (colw + gap)
        blank = (head == "SLESVIG")
        # column frame
        o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s" '
                 'stroke-width="1"%s/>'
                 % (cx - 8, top - 2, colw, 300, SLATE if not blank else INK,
                    '' if not blank else ' stroke-dasharray="5 4" opacity=".55"'))
        o.append('<text x="%d" y="%d" class="mapl">%s</text>' % (cx, top + 18, head))
        o.append('<text x="%d" y="%d" class="mapx">%s</text>' % (cx, top + 34, esc(rule)))
        yy = top + 58
        for s in steps:
            if s is None:
                o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
                         'stroke-width="1"/>' % (cx, yy - 8, cx + colw - 24, yy - 8, RULE))
                yy += 8
                continue
            if s:
                o.append('<text x="%d" y="%d" class="mapt">%s</text> ' % (cx, yy, esc(s)))
            yy += 15
        if blank:
            o.append('<text x="%d" y="%d" class="mapl" opacity=".7">UNSETTLED</text>'
                     % (cx, top + 286))

    b = top + 316
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (b, b, RULE))
    for k, line in enumerate(TAIL1):
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (b + 20 + k * 14, esc(line)))
    o.append('</svg>')
    return "\n  ".join(o)


# ====================================================================== figure 2
# P.C. Koch, Udkast til et Sprog-Kort over Hertugdommet Slesvig eller
# Sonderjylland, 1839. Categories and populations are his printed key, verbatim
# in substance; the translation is mine and the arithmetic is computed below.
KOCH = [
    ("Danish at home, Danish in church and school", 110213, DANE1),
    ("Danish at home, Danish and German by turns", 23392, DANE2),
    ("Danish at home, German in church and school", 10630, DANE3),
    ("Danish and Low German mixed, German in church", 47207, MIXED),
    ("Low German at home, German in church and school", 119935, GERM1),
    ("Frisian at home, German in church and school", 26815, GERM2),
]
KOCH_TOTAL = 338192          # printed on Koch's own key

NOTES2 = [
    "Koch's own footnotes, kept because they are the argument in miniature: the language",
    "of court proceedings was German everywhere except the districts under Ribe Amt; and",
    "Christiansfeld was left uncoloured, because \"by its nature it does not concern the",
    "present national cause\" \u2014 a Moravian town that fitted no category on either map.",
]


def sprog():
    tot = sum(n for _, n, _ in KOCH)
    assert tot == KOCH_TOTAL, "Koch's categories sum to %d, his key says %d" % (tot, KOCH_TOTAL)

    danish_only = sum(n for lbl, n, _ in KOCH if lbl.startswith("Danish at home"))
    danish_church = KOCH[0][1]
    danish_wide = danish_only + KOCH[3][1]

    readings = [
        ("Danish in church and school", danish_church),
        ("Danish spoken at home", danish_only),
        ("Danish at home, counting the mixed band", danish_wide),
    ]

    W, H = 700, 512
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Chart of P.C. Koch\u2019s language count for the duchy of Slesvig, '
         'published in 1839 as a Danish answer to Franz Geerz\u2019s German language map of '
         '1838. Koch divided the duchy\u2019s 338,192 inhabitants into six categories by '
         'setting the language spoken at home against the language of church and school. '
         'Danish at home with Danish in church and school, 110,213; Danish at home with '
         'Danish and German by turns, 23,392; Danish at home with German in church and '
         'school, 10,630; Danish and Low German mixed with German in church, 47,207; Low '
         'German at home with German in church and school, 119,935; Frisian at home with '
         'German in church and school, 26,815. Depending which of those categories are '
         'counted as Danish, the same survey makes the duchy 33, 43 or 57 per cent Danish.">'
         % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">HOW MANY DANES WERE THERE IN SLESVIG?</text>')
    o.append('<text x="26" y="46" class="mapt">P.C. Koch\u2019s own count, 1839 \u2014 published '
             'to answer Franz Geerz\u2019s map of 1838</text>')

    # proportional band
    bx, bw, by, bh = 26, 648, 68, 26
    x = float(bx)
    for lbl, n, tone in KOCH:
        w = bw * n / float(tot)
        o.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" opacity=".8"/>'
                 % (x + 0.0, by, w + 0.0, bh, tone))
        x += w
    o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s" '
             'stroke-width="1"/>' % (bx, by, bw, bh, RULE))
    o.append('<text x="26" y="%d" class="mapt">338,192 inhabitants, in the six categories '
             'Koch printed on his key</text>' % (by + bh + 15))

    # the six rows
    ry = by + bh + 40
    o.append('<text x="26" y="%d" class="mapx">HIS CATEGORIES, IN HIS ORDER</text>' % ry)
    yy = ry + 22
    for lbl, n, tone in KOCH:
        o.append('<rect x="26" y="%d" width="10" height="10" fill="%s" opacity=".8"/>'
                 % (yy - 8, tone))
        o.append('<text x="44" y="%d" class="mapx">%7s</text> ' % (yy, "{:,}".format(n)))
        o.append('<text x="108" y="%d" class="mapx">%4.1f%%</text> ' % (yy, 100.0 * n / tot))
        o.append('<text x="156" y="%d" class="mapt">%s</text>' % (yy, esc(lbl)))
        yy += 19

    # the three readings
    b = yy + 12
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (b, b, RULE))
    o.append('<text x="26" y="%d" class="mapx">THREE ANSWERS FROM ONE SURVEY</text>' % (b + 22))
    yy = b + 44
    for lbl, n in readings:
        pct = 100.0 * n / tot
        o.append('<text x="26" y="%d" class="mapl">%2.0f%%</text> ' % (yy, pct))
        o.append('<text x="72" y="%d" class="mapx">%s</text> ' % (yy, "{:,}".format(n)))
        o.append('<text x="140" y="%d" class="mapt">%s</text>' % (yy, esc(lbl)))
        yy += 20

    b2 = yy + 8
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (b2, b2, RULE))
    for k, line in enumerate(NOTES2):
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (b2 + 18 + k * 14, esc(line)))
    o.append('</svg>')
    return "\n  ".join(o)


# ====================================================================== figure 3
SEAT_QUIET = "#A9B6BD"     # uncontested seats; see the note in franchise()
SEATS_TOTAL = 100
SEATS_UNCONTESTED = 43
ENTITLED_57 = 116553
VOTED_57 = 37903
POP_1850 = 1414648           # census of 1 February 1850, Danmarks Statistik

RATIOS = [
    ("15%", "of the whole population could vote"),
    ("72.8%", "of all men over thirty could vote"),
]

SEVEN_F = [
    ("fruentimmere", "women, whatever they owned"),
    ("folkehold", "servants without a household of their own"),
    ("fattige", "anyone who had taken poor relief and not repaid it"),
    ("fremmede", "those without Danish indf\u00f8dsret"),
    ("fallenter", "bankrupts"),
    ("fjolser", "those declared incapable of managing their affairs"),
    ("forbrydere", "the convicted"),
]


def franchise():
    contested = SEATS_TOTAL - SEATS_UNCONTESTED
    turnout = 100.0 * VOTED_57 / ENTITLED_57

    W = 700
    o = []
    head = ('<svg viewBox="0 0 %d %%d" xmlns="http://www.w3.org/2000/svg" role="img" ' % W +
         'aria-label="Chart of the Danish franchise under the constitution of 5 June 1849. '
         'The kingdom held 1,414,648 people at the census of 1 February 1850. At the first '
         'Folketing election, on 4 December 1849, a hundred seats were filled; in '
         'forty-three of them there was no ballot at all and the single candidate was '
         'carried by acclamation. In the fifty-seven contested seats, 37,903 men voted out '
         'of 116,553 entitled, a turnout of about thirty-three per cent. Published '
         'proportions, shown separately because they are ratios and not counts, give the '
         'electorate as fifteen per cent of the whole population and 72.8 per cent of all '
         'men over thirty. The excluded were known as the seven F\u2019s: women, servants '
         'without their own household, those who had taken poor relief, foreigners, '
         'bankrupts, those declared incapable of managing their affairs, and the '
         'convicted.">')
    o.append('<text x="26" y="30" class="mapl">WHO COULD VOTE IN 1849</text>')
    o.append('<text x="26" y="46" class="mapt">counted figures solid; published proportions '
             'in outline, because they are ratios and not counts</text>')

    o.append('<text x="26" y="76" class="mapx">COUNTED</text>')
    o.append('<text x="26" y="98" class="mapt">Population of the kingdom, census of 1 '
             'February 1850</text>')
    o.append('<text x="536" y="98" class="mapl">%s</text>' % "{:,}".format(POP_1850))

    # the hundred seats
    sy = 122
    o.append('<text x="26" y="%d" class="mapt">Seats filled at the first Folketing election, '
             '4 December 1849</text>' % sy)
    o.append('<text x="536" y="%d" class="mapl">%d</text>' % (sy, SEATS_TOTAL))
    gy = sy + 14
    BOX, GAP, PER = 9, 4, 25
    for n in range(SEATS_TOTAL):
        r, c = divmod(n, PER)
        gx = 26 + c * (BOX + GAP)
        yy = gy + r * (BOX + GAP)
        # AN OUTLINE MEANS ONE THING ON THIS FIGURE AND ONLY ONE: a published ratio
        # rather than a count. The first version also drew the uncontested seats as
        # outlines, so the same encoding carried two unrelated meanings in one
        # picture and a reader had no way to know which. Both kinds of seat are now
        # filled, in two tones, with a key.
        o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s"/>'
                 % (gx, yy, BOX, BOX, SEAT_QUIET if n < SEATS_UNCONTESTED else SLATE))
    ly = gy + 4 * (BOX + GAP) + 16
    # STACKED, NOT SIDE BY SIDE. Set on one line, the second swatch printed straight
    # through the first label. collisions() compares text against text and does not
    # see a <rect> laid over a <text>, so nothing fired; this was caught by looking.
    o.append('<rect x="26" y="%d" width="9" height="9" fill="%s"/>' % (ly - 8, SEAT_QUIET))
    o.append('<text x="42" y="%d" class="mapt">%d seats: no ballot at all \u2014 one candidate, '
             'carried by acclamation</text>' % (ly, SEATS_UNCONTESTED))
    o.append('<rect x="26" y="%d" width="9" height="9" fill="%s"/>' % (ly + 7, SLATE))
    o.append('<text x="42" y="%d" class="mapt">%d seats contested</text>'
             % (ly + 15, SEATS_TOTAL - SEATS_UNCONTESTED))

    # turnout bar for the contested seats
    ty = ly + 45
    o.append('<text x="26" y="%d" class="mapt">In the %d contested seats: entitled to '
             'vote</text>' % (ty, contested))
    o.append('<text x="536" y="%d" class="mapl">%s</text>' % (ty, "{:,}".format(ENTITLED_57)))
    barx, barw, barh = 26, 648, 18
    o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s" '
             'stroke-width="1"/>' % (barx, ty + 10, barw, barh, RULE))
    o.append('<rect x="%d" y="%d" width="%.1f" height="%d" fill="%s" opacity=".85"/>'
             % (barx, ty + 10, barw * VOTED_57 / float(ENTITLED_57) + 0.0, barh, SLATE))
    o.append('<text x="26" y="%d" class="mapt">of whom %s actually voted \u2014 %.0f per '
             'cent</text>' % (ty + 44, "{:,}".format(VOTED_57), turnout))

    # published ratios, outline
    py = ty + 68
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (py, py, RULE))
    o.append('<text x="26" y="%d" class="mapx">PUBLISHED PROPORTIONS, NOT COUNTS</text>'
             % (py + 22))
    yy = py + 44
    for val, lbl in RATIOS:
        o.append('<rect x="26" y="%d" width="10" height="10" fill="none" stroke="%s" '
                 'stroke-width="1"/>' % (yy - 8, SLATE))
        o.append('<text x="44" y="%d" class="mapl">%s</text> ' % (yy, val))
        o.append('<text x="112" y="%d" class="mapt">%s</text>' % (yy, esc(lbl)))
        yy += 19
    o.append('<text x="26" y="%d" class="mapt">No head-count of men over thirty is derived '
             'from these here. Dividing one published ratio by</text>' % (yy + 4))
    o.append('<text x="26" y="%d" class="mapt">another produces a number that looks counted '
             'and is not.</text>' % (yy + 18))

    # the seven F's
    fy = yy + 44
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (fy, fy, RULE))
    o.append('<text x="26" y="%d" class="mapx">AND WHO COULD NOT \u2014 THE SEVEN F\u2019S</text>'
             % (fy + 22))
    yy = fy + 42
    for word, gloss in SEVEN_F:
        o.append('<text x="26" y="%d" class="mapx">%s</text> ' % (yy, esc(word)))
        o.append('<text x="150" y="%d" class="mapt">%s</text>' % (yy, esc(gloss)))
        yy += 15
    # THE CANVAS IS COMPUTED, NOT TYPED. The first version ended at 560 and the
    # overflow guard caught the last two lines of the seven F's sitting below it -
    # the svg_band / svg_invasions failure a third time. A height derived from the
    # last baseline cannot drift when a line is added.
    H = int(yy + 10)
    o.append('</svg>')
    return (head % H) + '\n  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>\n  ' \
        % (W, H, PAPER) + "\n  ".join(o)


if __name__ == "__main__":
    for name, fn in (("svg_descent_1848.txt", descent),
                     ("svg_sprog_1839.txt", sprog),
                     ("svg_franchise_1849.txt", franchise)):
        svg = fn()
        ET.fromstring(svg)
        w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
        h = int(re.search(r'viewBox="0 0 \d+ (\d+)', svg).group(1))
        for bad in (M.check(svg, name) or []):
            print("  !! %s: %s" % (name, bad))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars, %dx%d)" % (name, len(svg), w, h))
