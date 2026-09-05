# -*- coding: utf-8 -*-
"""Chapter 32's non-map figures.

  svg_assemblies.txt  four advisory assemblies, 1834: seats, franchise, exclusions
  svg_rye.txt         what the collapse of 1818-28 did, and to what

THE RYE FIGURE IS NOT THE ONE THAT WAS PLANNED. PLAN_H asked for the Zealand
kapitelstakst for a tonde of rye as a continuous annual line, 1815-1848. That
series exists: Scharling, Pengenes synkende Vaerdi (1869), and Danmarks
Statistik's own "Kapitelstakster i aeldre og nyere Tid", Statistiske Meddelelser
4. Raekke, 15. Bind, Haefte I. It is digitised. I could not obtain the
year-by-year values from here, and a line chart needs every year.

The chapter 27 precedent applies exactly. A worked example can be labelled as
constructed and still be honest; a fabricated annual price series cannot, because
it would look like data and there is no way for a reader to tell. So this figure
draws only what the sources actually state - two ratios and a chronology - and
says on its face that the continuous series exists and is not reproduced here.

What IS attested: grain at about one fifth of the 1814-17 level by 1820-25; farm
property down to a third or a quarter of its former price; the 1812 Zealand takst
at 61 rigsdaler 72 skilling, nearly twenty times the 1790s; prices nearly
quadrupling from 1811 to 1812; the collapse running from 1818 and the recovery
from about 1828 into the kornsalgsperiode. That is a shape, and the shape is the
point of the section. The missing thing is resolution, not direction.

IF THE VALUES ARE OBTAINED, replace this with the line and delete this note.

THE FOURTH SEAT COUNT IS WEAKER THAN THE OTHER THREE, and the figure says so on
its face rather than only here. Roskilde (70) and Viborg (55) come from Danish
accounts of the four decrees of 15 May 1834 and both reconcile to their own
sub-totals: Roskilde 12 Copenhagen + 11 provincial towns + 17 landowners + 20
farmers = 60 elected, plus 10 royally appointed = 70; Viborg 12 + 14 + 22 = 48
elected, plus 7 appointed = 55. Schleswig (44) is given directly by the published
list of the 1836 membership. Holstein (48) is COUNTED BY HAND from the published
list of the 1835/36 membership, not stated by any source I could reach, and a
membership list can be incomplete where a decree cannot. It is drawn with an
open marker and labelled as counted, so a reader is not told it has the same
standing as the others.

Corroboration, such as it is: the German accounts say Holstein had more deputies
than Schleswig in proportion to its larger population, and 48 > 44. That is
consistent, which is not the same as confirmed.

TO CLOSE THIS PROPERLY, read the seat provisions out of the 15 May 1834 decree
for Holstein. Until then the number carries a caveat in the figure and in the
chapter's sources block.

WHAT THE FIGURE ARGUES. Two Danish bodies and two German ones, constituted the
same week under the same law, with the same powers and no power. The franchise
attached to them was the widest in Europe at the time - about one inhabitant in
forty - and excluded every woman regardless of property. Both halves are the
point, so both are drawn at the same size.

Run: python3 figs_32.py
"""
import re
import xml.etree.ElementTree as ET

import mapspine as M

# NOTE on the guards. `overruns` tests text against the CANVAS EDGE and nothing
# else. The first version of this figure set the franchise text in two columns at
# x=26 and x=380; the left column ran to x=423 and printed straight through the
# right one, and every guard passed because 423 is inside 700. There is no
# collision guard. Measured character widths, taken off the raster rather than
# assumed: mapt 5.68, mapx 5.63, mapl 6.98 units. The 6.1 the guard uses is
# conservative for mapt and mapx and TOO SMALL FOR mapl, so a long mapl line can
# overrun without being flagged. The blocks below are stacked, not columned.
INK = "#3C3E36"
PAPER = "#F0F2EE"
RULE = "#C9CDC4"
SEAT = "#7C8CA8"
SEAT_ROYAL = "#A8B2C2"

# (city, region, language of business, elected, appointed, total, sourcing, first sitting)
ASSEMBLIES = [
    ("Roskilde", "the islands",      "Danish", 60,  10, 70, "decree",  "1 Oct 1835"),
    ("Viborg",   "north Jutland",    "Danish", 48,   7, 55, "decree",  "1836"),
    ("Slesvig",  "Schleswig",        "German", None, None, 44, "list", "11 Apr 1836"),
    ("Itzehoe",  "Holstein",         "German", None, None, 48, "counted", "1 Oct 1835"),
]

PER_ROW = 12
BOX, GAP = 7, 3


def assemblies():
    W, H = 700, 534
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Diagram of the four advisory provincial assemblies established for the '
         'Danish monarchy by two ordinances of 28 May 1831 and four decrees of 15 May 1834. '
         'Roskilde sat for the islands with seventy members, Viborg for north Jutland with '
         'fifty-five, the town of Schleswig for the duchy of Schleswig with forty-four, and '
         'Itzehoe for Holstein with forty-eight. Two conducted business in Danish and two in '
         'German. All four were advisory only: they could be shown draft laws and could '
         'propose laws, and the king could ignore them. About one inhabitant in forty could '
         'vote, a wider share than any other country in Europe at the time, but every voter '
         'had to own land, women were excluded whatever they owned, Jews could vote but not '
         'be elected, and clergy could not be elected but could be appointed by the king. '
         'The Holstein figure is counted from a membership list rather than taken from the '
         'decree, and is marked on the figure as such.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">FOUR ASSEMBLIES, TWO LANGUAGES, NO POWER</text>')
    o.append('<text x="26" y="46" class="mapt">ordinances of 28 May 1831; decrees of 15 May '
             '1834; first sittings 1835 and 1836</text>')

    x0, y0 = 26, 78
    colw = 162
    for i, (city, region, lang, el, ap, tot, src, first) in enumerate(ASSEMBLIES):
        cx = x0 + i * colw
        o.append('<text x="%d" y="%d" class="mapx">%s</text>' % (cx, y0, city.upper()))
        o.append('<text x="%d" y="%d" class="mapt">%s \u00b7 %s</text>'
                 % (cx, y0 + 14, region, lang))
        # seats: filled for elected, open for royally appointed where the split is known
        for n in range(tot):
            r, c = divmod(n, PER_ROW)
            sx = cx + c * (BOX + GAP)
            sy = y0 + 26 + r * (BOX + GAP)
            if el is not None and n >= el:
                o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" '
                         'stroke="%s" stroke-width="1"/>' % (sx, sy, BOX, BOX, SEAT))
            elif el is None:
                o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" '
                         'opacity=".55"/>' % (sx, sy, BOX, BOX, SEAT))
            else:
                o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s"/>'
                         % (sx, sy, BOX, BOX, SEAT))
        rows = (tot + PER_ROW - 1) // PER_ROW
        by = y0 + 26 + rows * (BOX + GAP) + 12
        o.append('<text x="%d" y="%d" class="mapl">%d</text>' % (cx, by, tot))
        if el is not None:
            o.append('<text x="%d" y="%d" class="mapt">%d elected, %d appointed</text>'
                     % (cx, by + 13, el, ap))
        elif src == "counted":
            o.append('<text x="%d" y="%d" class="mapt">counted, not decreed</text>' % (cx, by + 13))
        else:
            o.append('<text x="%d" y="%d" class="mapt">split not established</text>' % (cx, by + 13))
        o.append('<text x="%d" y="%d" class="mapt">first sat %s</text>' % (cx, by + 26, first))

    b1 = 246
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (b1, b1, RULE))
    o.append('<text x="26" y="%d" class="mapx">WHO COULD VOTE</text>' % (b1 + 22))
    for k, line in enumerate([
            "Every voter a landowner. In the country, four t\u00f8nder hartkorn; five on",
            "hereditary lease. In a market town, property worth a thousand rigsdaler.",
            "Twice that to stand. Vote at twenty-five, stand at thirty-five.",
            "About one inhabitant in forty \u2014 a wider share than any country in Europe."]):
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (b1 + 40 + k * 14, line))

    o.append('<text x="26" y="%d" class="mapx">AND WHO COULD NOT</text>' % (b1 + 114))
    for k, line in enumerate([
            "Women \u2014 whatever they owned, and with no exception.",
            "Jews could vote. They could not be elected.",
            "Clergy could not be elected either: a priest was to",
            "attend to his teaching office and not to politics.",
            "The king could appoint one."]):
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (b1 + 132 + k * 14, line))

    b2 = H - 70
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (b2, b2, RULE))
    o.append('<text x="26" y="%d" class="mapt">They could be shown draft laws and could propose '
             'laws. They could pass none, and the king</text>' % (b2 + 18))
    o.append('<text x="26" y="%d" class="mapt">could ignore them. Sittings were closed. Eleven '
             'years on, the argument the arrangement was</text>' % (b2 + 32))
    o.append('<text x="26" y="%d" class="mapt">built to disperse broke out inside the one at '
             'Slesvig.</text>' % (b2 + 46))
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
# Every number below is attested; see the docstring. Ranges are drawn as ranges
# because that is what the sources give, and narrowing them would be inventing.
BASE = "1814\u201317, the war-inflated level"
BARS = [
    (BASE,                                  100, 100),
    ("Grain, 1820\u201325",                  20,  20),
    ("Farm property, the 1820s",              25,  33),
]
CHRONOLOGY = [
    ("5 Jan 1813",  "currency reform; the rigsbankdaler replaces the kurantdaler"),
    ("1818",        "grain prices and grain exports begin falling together"),
    ("4 Jul 1818",  "Nationalbanken chartered; note circulation halves by the mid-1830s"),
    ("1820\u201325",  "the trough. Estates to forced auction, others taken for unpaid tax"),
    ("c. 1828",     "recovery begins. The kornsalgsperiode runs to the late 1850s"),
    ("Jun 1846",    "Britain repeals the Corn Laws"),
]


def rye():
    W, H = 700, 470
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Diagram of the Danish agricultural collapse of 1818 to 1828 and the '
         'recovery after it. Taking the war-inflated level of 1814 to 1817 as one hundred, '
         'grain had fallen to about twenty by 1820 to 1825, and farm property to between '
         'twenty-five and thirty-three of its former price. A dated list runs from the '
         'currency reform of 5 January 1813 through the chartering of Nationalbanken in July '
         '1818 and the trough of the early 1820s to the recovery from about 1828 and the '
         'repeal of the British Corn Laws in June 1846. The continuous annual series of '
         'Zealand rye prices exists in print and is not reproduced here, because the '
         'year-by-year values were not obtained; the figure says so rather than estimating '
         'them.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">A FIFTH OF WHAT IT HAD BEEN</text>')
    o.append('<text x="26" y="46" class="mapt">the war level of 1814\u201317 taken as 100</text>')

    x0, y = 250, 84
    xw = 400
    for lab, lo, hi in BARS:
        o.append('<text x="%d" y="%d" class="mapt" text-anchor="end">%s</text>'
                 % (x0 - 10, y + 9, lab))
        o.append('<rect x="%d" y="%d" width="%.1f" height="11" fill="%s" opacity=".55"/>'
                 % (x0, y, xw * lo / 100.0, SEAT))
        if hi != lo:
            o.append('<rect x="%.1f" y="%d" width="%.1f" height="11" fill="%s" opacity=".30"/>'
                     % (x0 + xw * lo / 100.0, y, xw * (hi - lo) / 100.0, SEAT))
            txt = "%d\u2013%d" % (lo, hi)
        else:
            txt = "%d" % lo
        o.append('<text x="%.1f" y="%d" class="mapt">%s</text>'
                 % (x0 + xw * hi / 100.0 + 8, y + 9, txt))
        y += 30

    o.append('<text x="26" y="%d" class="mapt">Ranges are drawn as ranges: the sources give '
             '"about a fifth" and "a third or a quarter",</text>' % (y + 14))
    o.append('<text x="26" y="%d" class="mapt">and narrowing them would be inventing a '
             'precision nobody recorded.</text>' % (y + 28))

    b = y + 56
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (b, b, RULE))
    o.append('<text x="26" y="%d" class="mapx">WHAT HAPPENED, AND WHEN</text>' % (b + 22))
    yy = b + 44
    for when, what in CHRONOLOGY:
        o.append('<circle cx="34" cy="%d" r="3" fill="%s"/>' % (yy - 4, SEAT))
        o.append('<text x="48" y="%d" class="mapx">%s</text>' % (yy, when))
        o.append('<text x="152" y="%d" class="mapt">%s</text>' % (yy, what))
        yy += 20

    b2 = H - 46
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (b2, b2, RULE))
    o.append('<text x="26" y="%d" class="mapt">The Zealand kapitelstakst for a t\u00f8nde of '
             'rye survives as an unbroken annual series from 1651.</text>' % (b2 + 18))
    o.append('<text x="26" y="%d" class="mapt">Nobody in this chapter has plotted it.</text>'
             % (b2 + 32))
    o.append('</svg>')
    return "\n  ".join(o)


if __name__ == "__main__":
    for name, fn in (("svg_assemblies.txt", assemblies), ("svg_rye.txt", rye)):
        svg = fn()
        ET.fromstring(svg)
        w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
        h = int(re.search(r'viewBox="0 0 \d+ (\d+)', svg).group(1))
        for bad in (M.overruns(svg, w) or []):
            print("  !! overrun: %s" % (bad,))
        for bad in (M.overflows(svg, h) or []):
            print("  !! overflow: %s" % (bad,))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
