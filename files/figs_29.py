# -*- coding: utf-8 -*-
"""Chapter 29's three figures.

  svg_village.txt   one village, before and after the udskiftning
  svg_column.txt    the Liberty Column, and what it says
  svg_band.txt      the bound years, 1733-1800

THE VILLAGE FIGURE IS A SCHEMATIC AND SAYS SO ON ITS FACE. Drawing a named
village would need its actual udskiftningskort, and inventing plausible field
boundaries for a real place is the failure this part has been avoiding. The
precedent is chapter 21's partition figure, which uses a deliberately schematic
outline "so that nobody measures it". The reader is sent to a real map in the
visit block.

THE BAND FIGURE REPLACES the cohort staircase the plan called for. The ordinance
of 1788 did not release men by year of birth: it reverted the bound ages to the
original 1733 range at once, gave immediate freedom passes to those too old for
service and to those already discharged, and ended the bond altogether on 1
January 1800. What that history actually looks like is a band that widens twice,
snaps back, and stops - which is a better figure and a truer one.

Run: python3 figs_29.py
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


# ------------------------------------------------------------------ figure 1
HOUSEHOLDS = 6
TONES = [IND, VERD, AMBER, MUTED, "#7A5C86", "#8A6F3B"]


def village():
    W, H = 700, 496
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Two schematic diagrams of a village. On the left, before the reform: six '
         'households each hold many narrow strips scattered through three great open fields, so '
         'that every household has land of every quality and none can farm on its own judgement. '
         'On the right, after: each household\'s land is consolidated into one wedge running out '
         'from the village, and two farms have been demolished and rebuilt out on their own '
         'ground. The diagrams are schematic and are not a map of any particular '
         'village.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">ONE VILLAGE, TWICE</text>')
    o.append('<text x="26" y="46" class="mapt">the same six households, before and after the '
             'udskiftning</text>')

    o.append('<text x="26" y="78" class="mapx">BEFORE \u2014 three open fields, strips shared '
             'out</text>')
    o.append('<text x="382" y="78" class="mapx">AFTER \u2014 one holding each</text>')

    # ---- left: three fields of scattered strips
    lx, ly, lw, lh = 26, 92, 296, 210
    o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" opacity=".06"/>'
             % (lx, ly, lw, lh, INK))
    band = lh / 3.0
    k = 0
    for f in range(3):
        y0 = ly + f * band
        o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1"/>'
                 % (lx, y0, lx + lw, y0, RULE))
        strips = 18
        for i in range(strips):
            x = lx + 4 + i * ((lw - 8) / float(strips))
            col = TONES[(k * 5 + f * 2) % HOUSEHOLDS]
            k += 1
            o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" '
                     'opacity=".55"/>'
                     % (x, y0 + 5, (lw - 8) / float(strips) - 2, band - 10, col))
    o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s" '
             'stroke-width="1.2"/>' % (lx, ly, lw, lh, INK))
    o.append('<circle cx="%d" cy="%d" r="16" fill="%s"/>' % (lx + lw / 2, ly + lh / 2, PAPER))
    o.append('<circle cx="%d" cy="%d" r="16" fill="%s" opacity=".22"/>'
             % (lx + lw / 2, ly + lh / 2, INK))
    o.append('<text x="%d" y="%d" class="mapt" text-anchor="middle">village</text>'
             % (lx + lw / 2, ly + lh / 2 + 4))

    # ---- right: wedges from the centre, two farms moved out
    rx, ry, rw, rh = 382, 92, 292, 210
    cx, cy = rx + rw / 2, ry + rh / 2
    o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" opacity=".06"/>'
             % (rx, ry, rw, rh, INK))
    import math
    for i in range(HOUSEHOLDS):
        a0 = -math.pi / 2 + i * 2 * math.pi / HOUSEHOLDS
        a1 = -math.pi / 2 + (i + 1) * 2 * math.pi / HOUSEHOLDS
        r = 240
        p = ["M %.1f %.1f" % (cx, cy)]
        steps = 8
        for s in range(steps + 1):
            a = a0 + (a1 - a0) * s / float(steps)
            p.append("L %.1f %.1f" % (cx + r * math.cos(a), cy + r * math.sin(a)))
        p.append("Z")
        o.append('<clipPath id="v%d"><rect x="%d" y="%d" width="%d" height="%d"/></clipPath>'
                 % (i, rx, ry, rw, rh))
        o.append('<path d="%s" fill="%s" opacity=".45" clip-path="url(#v%d)"/>'
                 % (" ".join(p), TONES[i], i))
    o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s" '
             'stroke-width="1.2"/>' % (rx, ry, rw, rh, INK))
    o.append('<circle cx="%.1f" cy="%.1f" r="16" fill="%s"/>' % (cx, cy, PAPER))
    o.append('<circle cx="%.1f" cy="%.1f" r="16" fill="%s" opacity=".22"/>' % (cx, cy, INK))
    o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="middle">village</text>'
             % (cx, cy + 4))
    for dx, dy in ((-96, -62), (104, 58)):
        o.append('<rect x="%.1f" y="%.1f" width="11" height="9" fill="%s" stroke="%s" '
                 'stroke-width="1"/>' % (cx + dx, cy + dy, PAPER, INK))
    o.append('<text x="%.1f" y="%.1f" class="mapt">two farms moved out</text>'
             % (cx + 6, cy + 82))

    b = 322
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    y = b + 20
    for line in wrap("Before, every household held strips in all three fields, so good land and "
                     "bad were shared out and the risk with them. The price was that nobody could "
                     "decide anything alone: the village agreed when to plough, when to sow and "
                     "when to turn the animals onto the stubble, and a man who wanted to try "
                     "something new could not, because his neighbours' strips lay between his.",
                     104):
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (y, line))
        y += 14
    y += 6
    for line in wrap("After, each household farmed one piece and could do as it liked with it. "
                     "Where the land would not take the wedge shape, the farmstead itself was "
                     "pulled down and rebuilt out on its own ground, which broke up villages that "
                     "had stood in one place since the Middle Ages.", 104):
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (y, line))
        y += 14
    o.append('<text x="26" y="%d" class="mapt" fill="%s">Both diagrams are schematic. They '
             'are not a map of any particular village;</text>' % (y + 8, MUTED))
    o.append('<text x="26" y="%d" class="mapt" fill="%s">for a real one, see the visit '
             'block.</text>' % (y + 22, MUTED))
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
DA = ["Kongen bød", "Stavnsbaandet skal ophøre", "Landboe Lovene gives Orden og Kraft",
      "at den frie Bonde kan vorde", "kiek og oplyst, flittig og god", "hæderlig Borger", "lykkelig"]
EN = ["The King commanded", "that the stavnsb\u00e5nd shall cease",
      "that the agrarian laws be given order and force",
      "so that the free peasant may become", "bold and enlightened, industrious and good",
      "an honourable citizen", "happy"]
CORRECTIONS = [
    ("\u201cThe King commanded\u201d",
     "Christian 7. was incapable. It was done by Reventlow, Colbjørnsen, Bernstorff "
     "and a crown prince of twenty."),
    ("\u201cshall cease\u201d",
     "By cohort, over twelve years. The last men were free on 1 January 1800, three "
     "years after the column was finished."),
    ("\u201cthe free peasant\u201d",
     "The gårdmænd. The cottagers got the hoveri limits of 1799 only for holders, and "
     "a weaker ordinance of their own in 1807."),
    ("not on the stone",
     "The subscription opened in 1791, among Copenhagen burghers; the crown prince laid "
     "the foundation stone on 31 July 1792. The landowners were pushing back and the "
     "government had stopped reforming."),
]


def column():
    W, H = 700, 604
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="The Liberty Column on Vesterbrogade, drawn in outline, with the seven '
         'lines of its principal inscription in Danish and English beside it, and four notes. '
         'Three set a claim of the inscription against what the record shows; the fourth is '
         'not from the stone and is labelled as such.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">WHAT THE COLUMN SAYS</text>')
    o.append('<text x="26" y="46" class="mapt">Frihedsst\u00f8tten, Vesterbrogade, 1792\u201397 '
             '\u2014 twenty metres of Bornholm sandstone</text>')
    o.append('<text x="26" y="60" class="mapt">subscription opened 1791 \u00b7 foundation '
             'stone 31 July 1792 \u00b7 finished September 1797</text>')

    # the obelisk in outline, to its own proportions
    bx, by, bh = 92, 86, 268
    o.append('<path d="M %d %d L %d %d L %d %d L %d %d Z" fill="%s" opacity=".16"/>'
             % (bx - 9, by, bx + 9, by, bx + 17, by + bh, bx - 17, by + bh, IND))
    o.append('<path d="M %d %d L %d %d L %d %d L %d %d Z" fill="none" stroke="%s" '
             'stroke-width="1.3"/>' % (bx - 9, by, bx + 9, by, bx + 17, by + bh, bx - 17,
                                       by + bh, INK))
    o.append('<rect x="%d" y="%d" width="%d" height="26" fill="%s" opacity=".22"/>'
             % (bx - 30, by + bh, 60, INK))
    o.append('<rect x="%d" y="%d" width="%d" height="26" fill="none" stroke="%s" '
             'stroke-width="1.3"/>' % (bx - 30, by + bh, 60, INK))
    o.append('<text x="%d" y="%d" class="mapt" text-anchor="middle">20 m</text>'
             % (bx, by + bh + 44))

    px = 168
    y = 100
    for da, en in zip(DA, EN):
        o.append('<text x="%d" y="%d" class="mapx">%s</text>' % (px, y, da))
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y + 13, en))
        y += 34

    b = by + bh + 62
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    y = b + 20
    for claim, note in CORRECTIONS:
        o.append('<text x="26" y="%d" class="mapx" fill="%s">%s</text>' % (y, IND, claim))
        for line in wrap(note, 68):
            o.append('<text x="212" y="%d" class="mapt">%s</text>' % (y, line))
            y += 13
        y += 8
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
# (year the rule began, lowest age bound, highest age bound, label)
BANDS = [
    (1733, 14, 36, "1733"),
    (1742, 9, 40, "1742"),
    (1764, 4, 40, "1764"),
    (1788, 14, 36, "1788"),
    (1800, None, None, "1800"),
]
Y0, Y1 = 1728, 1806
AGE_MAX = 44


def band():
    W, H = 700, 448
    L, R = 96, 646
    T, B = 96, 300
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="A chart of the ages at which a man of the Danish peasantry was bound to '
         'the estate of his birth. From February 1733 the band ran from fourteen to thirty-six; '
         'in 1742 it widened to nine to forty; in 1764 to four to forty; the ordinance of 20 '
         'June 1788 returned it at once to fourteen to thirty-six, and the bond ended altogether '
         'on 1 January 1800.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">THE BOUND YEARS</text>')
    o.append('<text x="26" y="46" class="mapt">the ages at which a countryman could not leave '
             'the estate he was born on</text>')

    def X(yr):
        return L + (R - L) * (yr - Y0) / float(Y1 - Y0)

    def Y(age):
        return B - (B - T) * age / float(AGE_MAX)

    for age in (0, 10, 20, 30, 40):
        o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width=".6"/>'
                 % (L, Y(age), R, Y(age), RULE))
        o.append('<text x="%d" y="%.1f" class="mapt" text-anchor="end">%d</text>'
                 % (L - 8, Y(age) + 4, age))
    o.append('<text x="%d" y="%d" class="mapt" text-anchor="end">age</text>' % (L - 8, T - 12))

    for i, (yr, lo, hi, lab) in enumerate(BANDS):
        if lo is None:
            continue
        nxt = BANDS[i + 1][0]
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" opacity=".45"/>'
                 % (X(yr), Y(hi), X(nxt) - X(yr), Y(lo) - Y(hi), IND))
        o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="middle">%d\u2013%d</text>'
                 % ((X(yr) + X(nxt)) / 2, Y(hi) - 7, lo, hi))

    for yr, lo, hi, lab in BANDS:
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1" '
                 'stroke-dasharray="3 3" opacity=".7"/>' % (X(yr), T - 6, X(yr), B + 6, MUTED))
        o.append('<text x="%.1f" y="%d" class="mapt" text-anchor="middle">%s</text>'
                 % (X(yr), B + 22, lab))

    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.2"/>'
             % (L, B, R, B, INK))

    y = B + 60
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (y - 18, y - 18, RULE))
    for line in wrap("The bond was imposed on 4 February 1733 and ended on 1 January 1800. The "
                     "ordinance of 20 June 1788 did not free anybody at a stroke. It put the "
                     "bound ages back to the range of 1733, gave immediate freedom passes to men "
                     "already too old for service and to those discharged from it, and set the "
                     "end at 1 January 1800 \u2014 three years after the Liberty Column was "
                     "finished. Conscription itself was moved onto the new censuses instead of "
                     "the land assessment, and it went on falling only on country youth: young "
                     "men in the market towns were exempt until 1849.", 104):
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (y, line))
        y += 14
    o.append('</svg>')
    return "\n  ".join(o)


if __name__ == "__main__":
    for name, fn in (("svg_village.txt", village),
                     ("svg_column.txt", column),
                     ("svg_band.txt", band)):
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
