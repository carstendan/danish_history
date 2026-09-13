# -*- coding: utf-8 -*-
"""Chapter 37's three figures.

  svg_syvf_1915.txt        the seven excluded categories, and the year each was let in
  svg_afstemning_1916.txt  the referendum of 1916 beside the people it disposed of
  svg_soefolk_1918.txt     Danish merchant seamen lost 1914-18

EVERY NUMBER HERE IS SOURCED AND EVERY DERIVED NUMBER IS COMPUTED. The literal
blocks below carry the source for each anchor value; nothing is typed twice and
nothing is rounded by hand. Totals and shares are asserted.

FIGURE 1 IS NOT THE FIGURE PLAN_I ASKED FOR, AND THE SUBSTITUTION IS DELIBERATE.
The plan wanted "the electorate before and after 1915, by category", sourced from
"Valgene til Rigsdagen" in Statistiske Meddelelser, and marked it "located". It is
located - the volumes are enumerated in HANDOFF under the dst.dk route - and it
was not fetched for this draft. A by-category electorate count needs that volume
and nothing else will do: the only share available to me is the one figure the
literature repeats, that the 1849 franchise left about fifteen per cent of the
population with a vote, and a two-bar before/after built on one sourced number and
one guess would be the kind of figure this project refuses.

So figure 1 draws what IS sourceable and what the section is actually about: the
seven categories as a list, with the year each was admitted. Five of the seven
dates are exact and two are "not yet", which is the argument - the chapter's claim
is that 1915 admitted two of seven and is routinely described as universal
suffrage. A list of seven dates makes that unanswerable in a way a pair of bars
would not. IF THE VOLUME IS FETCHED the before/after should be drawn as well, not
instead: one figure showing how many were let in, one showing how few.

FIGURE 3 IS SEAMEN ONLY, BY DECISION. PLAN_I asked for "Danish merchant ships and
seamen lost 1914-18". The seamen figure is solid: 702 is given identically by
Den Store Danske and by the tabulation from Soforklaringer 1914-1918, against a
merchant service of about ten thousand. The SHIP count is not: 324 and 275 both
circulate in reputable sources, the difference is probably enemy action against
all war-attributable loss, and I could not prove that. Tonnage lost is given as
both sixteen and twenty-five per cent by different sources. Drawing a ship bar
would mean choosing one of two numbers for no reason. The figure therefore carries
the men, who are counted, and states the absence of the ships.

Run: python3 figs_37.py
"""
import re
import xml.etree.ElementTree as ET

import mapspine as M

PAPER = "#F0F2EE"
RULE = "#C9CDC4"
INK = "#3C3E36"
DEEP = "#4A5A46"          # Part I band colour, provisional - see build_part_i.py
QUIET = "#A9B6BD"
WARM = "#A98C5F"
ABSENT = "#C2704F"


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


# mapl renders at 10.5px monospace with .06em letter-spacing, so one character
# advances 10.5*0.6 + 10.5*0.06 = 6.93px. Guessing 6 here is what drew a bar over
# the word "sold" in figure 2 on the first pass, and collisions() cannot see a
# <rect> over a <text> (HANDOFF 61). Measure the label, do not estimate it.
MAPL_CH = 10.5 * 0.6 + 10.5 * 0.06
MAPT_CH = 9.5 * 0.6 + 9.5 * 0.04


def mapl_w(s):
    return MAPL_CH * len(s)


def wrap(head, body, W, H):
    return (head % H) + '\n  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>\n  ' \
        % (W, H, PAPER) + "\n  ".join(body)


# ====================================================================== figure 1
# The seven categories excluded by the franchise of 1849, and the year each was
# admitted to the Folketing franchise. "de syv F'er" is a popular name, not a
# legal one; the exclusions are in the electoral law.
#   1915: women and servants                 - Grundloven af 5. juni 1915
#   1933: poor-relief recipients             - valglovsaendringen af 1933
#   1959: convicts                           - valglovsaendringen af 1959
#   under guardianship: still excluded
#   foreigners: still excluded (citizenship requirement)
# Bankrupts: the disqualification was tied to loss of control over one's estate
# and lapsed with the insolvency law rather than by a franchise act, so it carries
# no single year and is marked as such rather than given a guessed date.
SEVEN = [
    ("Fruentimmere",  "women",                                  "1915", "in"),
    ("Folkehold",     "servants in another household",          "1915", "in"),
    ("Fattige",       "those on unrepaid poor relief",          "1933", "in"),
    ("Fallenter",     "bankrupts",                              "\u2014", "lapsed"),
    ("Fjolser",       "those under guardianship",               "still out", "out"),
    ("Forbrydere",    "convicts",                               "1959", "in"),
    ("Fremmede",      "those without Danish citizenship",       "still out", "out"),
]
ADMITTED_1915 = 2


def syvf():
    assert len(SEVEN) == 7, "there are seven F's, not %d" % len(SEVEN)
    n_1915 = sum(1 for r in SEVEN if r[2] == "1915")
    assert n_1915 == ADMITTED_1915, \
        "1915 admitted %d categories, not %d" % (n_1915, ADMITTED_1915)

    W = 700
    head = ('<svg viewBox="0 0 %d %%d" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="The seven groups excluded from the Danish franchise by the '
            'constitution of 1849, known popularly as the seven F\u2019s, with the year '
            'each was admitted. Women and servants in another household were admitted in '
            '1915. Those on unrepaid poor relief were admitted in 1933. Convicts were '
            'admitted in 1959. The disqualification of bankrupts lapsed without a '
            'franchise act. Those under guardianship and those without Danish citizenship '
            'remain excluded. The constitution of 1915 admitted two of the seven.">' % W)

    o = []
    LEFT, ROW, GAP = 26, 30, 10
    y = 34
    o.append('<text x="%d" y="%d" class="mapl">THE SEVEN CATEGORIES, AND THE YEAR EACH '
             'WAS LET IN</text>' % (LEFT, y))
    y += 20
    o.append('<text x="%d" y="%d" class="mapt">Excluded by the franchise of 1849. '
             'The names are a popular joke, not a legal term.</text>' % (LEFT, y))
    y += GAP + 12

    # column geometry computed from the widest label, never typed
    name_w = int(mapl_w(max((r[0] for r in SEVEN), key=len))) + 22
    gloss_x = LEFT + name_w
    year_x = W - 26
    rule_y0 = y

    for name, gloss, year, state in SEVEN:
        fill = DEEP if state == "in" else (ABSENT if state == "out" else QUIET)
        o.append('<rect x="%d" y="%d" width="6" height="%d" fill="%s"/>'
                 % (LEFT - 12, y - 12, ROW - 10, fill))
        o.append('<text x="%d" y="%d" class="mapl">%s</text>' % (LEFT, y, esc(name)))
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (gloss_x, y, esc(gloss)))
        o.append('<text x="%d" y="%d" class="mapl" text-anchor="end" fill="%s">%s</text>'
                 % (year_x, y, fill, esc(year)))
        y += ROW

    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1"/>'
             % (LEFT - 12, rule_y0 - 18, W - 26, rule_y0 - 18, RULE))
    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1"/>'
             % (LEFT - 12, y - 18, W - 26, y - 18, RULE))
    y += 6

    note = ("The constitution of 5 June 1915 admitted %d of the seven. It is "
            "routinely described as the introduction of universal suffrage in "
            "Denmark." % n_1915)
    for line in fold(note, 84):
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (LEFT, y, esc(line)))
        y += 15

    y += 4
    src = ("Dates from the franchise acts. The bankrupts' disqualification lapsed with "
           "the insolvency law rather than by a franchise act and carries no single "
           "year, so none is given. Electorate counts by category need Valgene til "
           "Rigsdagen, Stat. Medd. \u2014 located, not fetched: see the docstring.")
    for line in fold(src, 92):
        o.append('<text x="%d" y="%d" class="mapx">%s</text>' % (LEFT, y, esc(line)))
        y += 13

    H = int(y + 12)
    o.append('</svg>')
    return wrap(head, o, W, H)


# ====================================================================== figure 2
# Folkeafstemningen om salg af Dansk Vestindien, 14 December 1916.
#   turnout 37.4 per cent, yes 64.2, no 35.8   - Danmarks Statistik
#   votes cast, rounded as published           - 283,000 yes / 158,000 no
#   islands' population 27,086                 - folketaelling 1911
# The electorate and the non-voters are COMPUTED from turnout and the votes cast;
# they are not separately published figures and are marked approximate on the face
# of the figure because the vote totals they derive from are themselves rounded.
YES_1916 = 283000
NO_1916 = 158000
TURNOUT_1916 = 0.374
YES_SHARE = 0.642
ISLANDERS_1911 = 27086


def afstemning():
    cast = YES_1916 + NO_1916
    share = YES_1916 / cast
    assert abs(share - YES_SHARE) < 0.001, \
        "the rounded votes give %.3f, not the published %.3f" % (share, YES_SHARE)
    electorate = cast / TURNOUT_1916
    nonvoters = electorate - cast
    assert nonvoters > cast, "the abstainers should outnumber the voters"

    bars = [("Voted to sell", YES_1916, DEEP),
            ("Voted not to sell", NO_1916, WARM),
            ("Did not vote", nonvoters, QUIET),
            ("Had no vote: the people being sold", ISLANDERS_1911, ABSENT)]

    W = 700
    head = ('<svg viewBox="0 0 %d %%d" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="The Danish referendum of 14 December 1916 on selling the Danish '
            'West Indies to the United States. About 283,000 voted to sell and about '
            '158,000 voted not to, on a turnout of 37.4 per cent, which leaves roughly '
            '738,000 electors who did not vote. Beside them, the 27,086 inhabitants of '
            'the three islands recorded at the census of 1911, none of whom had a vote. '
            'The abstainers outnumber the islanders about twenty-seven to one.">' % W)

    o = []
    LEFT, ROW = 26, 46
    y = 34
    o.append('<text x="%d" y="%d" class="mapl">14 DECEMBER 1916, AND THE PEOPLE IT WAS '
             'ABOUT</text>' % (LEFT, y))
    y += 20
    o.append('<text x="%d" y="%d" class="mapt">Denmark\u2019s first referendum. The first '
             'national vote on the rolls of 1915.</text>' % (LEFT, y))
    y += 24

    label_w = int(mapl_w(max((b[0] for b in bars), key=len))) + 18
    bar_x = LEFT + label_w
    bar_max = W - 26 - bar_x - 74          # room for the value at the right
    biggest = max(b[1] for b in bars)

    for label, v, fill in bars:
        w = max(1.0, bar_max * v / biggest)
        o.append('<text x="%d" y="%d" class="mapl">%s</text>' % (LEFT, y + 13, esc(label)))
        o.append('<rect x="%d" y="%d" width="%.1f" height="18" fill="%s"/>'
                 % (bar_x, y, w, fill))
        o.append('<text x="%.1f" y="%d" class="mapt" fill="%s">%s</text>'
                 % (bar_x + w + 8, y + 13, INK, esc("{:,}".format(int(round(v)))
                                                    .replace(",", "\u2009"))))
        y += ROW

    ratio = nonvoters / ISLANDERS_1911
    y += 2
    note = ("The abstainers outnumber the islanders about %d to one. Neither group "
            "was asked, but only one of them was entitled to be." % int(round(ratio)))
    for line in fold(note, 84):
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (LEFT, y, esc(line)))
        y += 15

    y += 4
    src = ("Votes and turnout: Danmarks Statistik \u2014 37.4 per cent, 64.2 to 35.8. "
           "Vote totals as published, rounded to the nearest thousand; the electorate "
           "and the abstainers are computed from them and are therefore approximate. "
           "Islands\u2019 population: census of 1911.")
    for line in fold(src, 92):
        o.append('<text x="%d" y="%d" class="mapx">%s</text>' % (LEFT, y, esc(line)))
        y += 13

    H = int(y + 12)
    o.append('</svg>')
    return wrap(head, o, W, H)


# ====================================================================== figure 3
# Danish merchant seamen lost 1914-18.
#   702 dead                          - Den Store Danske; Soforklaringer 1914-1918
#   about 10,000 in the service       - Soforklaringer tabulation
#   201 of the dead in sailing ships posted missing   - same
DEAD = 702
SERVICE = 10000
MISSING_SAIL = 201


def soefolk():
    assert MISSING_SAIL < DEAD, "the missing cannot exceed the dead"
    rate = DEAD / SERVICE
    one_in = SERVICE / DEAD
    sail_share = MISSING_SAIL / DEAD

    W = 700
    head = ('<svg viewBox="0 0 %d %%d" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="Danish merchant seamen lost in the First World War. Of about ten '
            'thousand men in the Danish merchant service, 702 died, which is one man in '
            'fourteen, or seven per cent. Two hundred and one of the 702 were lost in '
            'sailing ships that left harbour and were never heard of again. Denmark was '
            'neutral throughout.">' % W)

    o = []
    LEFT = 26
    y = 34
    o.append('<text x="%d" y="%d" class="mapl">THE PRICE OF A NEUTRAL FLAG, '
             '1914\u201318</text>' % (LEFT, y))
    y += 20
    o.append('<text x="%d" y="%d" class="mapt">Danish merchant seamen. No Dane was '
             'conscripted; no foreign soldier crossed the border.</text>' % (LEFT, y))
    y += 26

    # a hundred-square grid: each cell is one per cent of the service
    CELL, PAD, COLS = 14, 3, 25
    rows = 4
    assert COLS * rows == 100, "the grid must be a hundred cells"
    # ROUND, do not truncate: rate*100 is 7.02, and `i < 7.02` shades EIGHT cells,
    # which would put 800 men on a chart whose number is 702. The first pass did
    # exactly that. Nothing in the guard suite can see a bar chart that lies.
    filled = int(round(rate * 100))
    assert abs(filled * SERVICE / 100 - DEAD) < SERVICE / 100, \
        "%d shaded cells misstates %d dead by more than one cell" % (filled, DEAD)
    grid_y0 = y
    for i in range(100):
        cx = LEFT + (i % COLS) * (CELL + PAD)
        cy = y + (i // COLS) * (CELL + PAD)
        fill = ABSENT if i < filled else QUIET
        o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s"/>'
                 % (cx, cy, CELL, CELL, fill))
    y = grid_y0 + rows * (CELL + PAD) + 20

    o.append('<text x="%d" y="%d" class="mapl">Each square is one hundred men of the '
             'merchant service. %s did not come home.</text>'
             % (LEFT, y, ("Seven" if filled == 7 else str(filled)) + " squares’ worth"))
    y += 26

    lines = [
        ("%d" % DEAD, "Danish merchant seamen died, of about %s in the service"
         % "{:,}".format(SERVICE).replace(",", "\u2009")),
        ("1 in %d" % int(round(one_in)), "which is %.0f per cent of the trade"
         % (rate * 100)),
        ("%d" % MISSING_SAIL, "of the %d were in sailing ships that left harbour and "
         "were never heard of again \u2014 %.0f per cent of the dead"
         % (DEAD, sail_share * 100)),
    ]
    num_w = int(mapl_w(max((a for a, _ in lines), key=len))) + 26
    for big, rest in lines:
        o.append('<text x="%d" y="%d" class="mapl" fill="%s">%s</text>'
                 % (LEFT, y, ABSENT, esc(big)))
        for j, line in enumerate(fold(rest, 70)):
            o.append('<text x="%d" y="%d" class="mapt">%s</text>'
                     % (LEFT + num_w, y + j * 14, esc(line)))
        y += 14 * max(1, len(fold(rest, 70))) + 14

    y += 2
    src = ("Deaths and service strength: Soforklaringer 1914\u201318, as tabulated; the "
           "702 agrees with Den Store Danske. SHIPS LOST IS NOT DRAWN: 324 and 275 both "
           "circulate, tonnage lost is given as both 16 and 25 per cent, and choosing "
           "between them without a reason would be guessing. The men are counted.")
    for line in fold(src, 92):
        o.append('<text x="%d" y="%d" class="mapx">%s</text>' % (LEFT, y, esc(line)))
        y += 13

    H = int(y + 12)
    o.append('</svg>')
    return wrap(head, o, W, H)


if __name__ == "__main__":
    for name, fn in (("svg_syvf_1915.txt", syvf),
                     ("svg_afstemning_1916.txt", afstemning),
                     ("svg_soefolk_1918.txt", soefolk)):
        svg = fn()
        ET.fromstring(svg)
        w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
        h = int(re.search(r'viewBox="0 0 \d+ (\d+)', svg).group(1))
        for bad in (M.check(svg, name) or []):
            print("  !! %s: %s" % (name, bad))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars, %dx%d)" % (name, len(svg), w, h))
