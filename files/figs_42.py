# -*- coding: utf-8 -*-
"""Figures for chapter 42.

THE FIGURE PLAN_I §13 ASKED FOR IS NOT THE FIGURE BUILT, and the substitution was
decided at the start of the session rather than after an afternoon of fetching,
which is HANDOFF 109's rule working.

  Planned 2 · Sabotage actions by MONTH, 1943-45, from a Frihedsmuseet series.
    NOT BUILT AS A MONTHLY SERIES. No monthly series is reachable. What exists in
    the accessible literature is the aggregate compiled by Jesper Vang Hansen,
    Esben Kjeldbæk and Bjarne Maurer (Industrisabotagen under besættelsen i tal
    og kommentarer, 1984), which danmarkshistorien.lex.dk reports only as two
    totals, and the per-year breakdown in Gyldendal og Politikens
    Danmarkshistorie. The ANNUAL series is therefore what figure 2 draws, and it
    is a better figure than the plan's: it carries the 1945 column as four
    months, which a monthly curve would have buried.

FIGURE 1 · October 1943: to Sweden, to Theresienstadt, and the difference.
  THE TWO QUANTITIES ARE NOT THE SAME KIND OF NUMBER and the figure says so on
  its face. The Theresienstadt figure is a NOMINAL COUNT: Silvia Goldbaum
  Tarabini Fracapane built 472 deported and 470 arrived from the transport
  registration lists in the Yad Vashem archives (file 0.64/275), can name the two
  men who are the difference, and demonstrates that the rival 481 double-counts
  the ten who arrived from Sachsenhausen and Ravensbrück in early 1944. It is
  drawn FILLED. The Sweden figure is an ESTIMATE WITH A RANGE: every account says
  "about 7,000"; Sofie Lene Bak states 7,056 Jews and 686 non-Jewish spouses as
  two separate facts and the 7,742 in circulation is other people's addition of
  them; the only figure attached to a named archive is the Danish Jewish Museum's
  Safe Haven database (Swedish police arrival protocols, Riksarkivet Stockholm),
  about 6,336 reports analysed, giving roughly 7,400 - and the museum says the
  material is incomplete. It is drawn OPEN, as a band from 7,000 to 7,742 with
  the archival estimate marked inside it. Drawing an estimate and a nominal count
  at the same visual confidence would be the lie this figure exists to avoid.

  The second row magnifies the 472. THE MAGNIFICATION FACTOR IS COMPUTED and
  printed, so that nobody reads the two rows as one scale.

FIGURE 2 · Sabotage by year, 1940-1945.
  Source: Gyldendal og Politikens Danmarkshistorie, "Sabotage og modterror", for
  73 industrial actions in 1940-42 together, 816 in 1943, 988 in 1944 and 924 in
  1945; and 2 railway actions in 1942, 111 in 1943, 311 in 1944 and 1,103 in
  1945. Totals double-witnessed against danmarkshistorien.lex.dk, "Sabotage,
  1940-1945", which gives 2,801 industrial and 1,526 railway and the 73-and-2 for
  1940-42.

  THE RAILWAY COLUMN DOES NOT ADD TO ITS OWN PUBLISHED TOTAL. 2+111+311+1103 is
  1,527 against 1,526. The industrial column adds exactly (73+816+988+924=2801).
  Item 119's rule is to check a fetched table against its own total, and the rule
  earns its keep here: the discrepancy of one is ASSERTED below and DRAWN as a
  marker, not averaged away and not silently corrected.

  THE 1945 COLUMN IS FOUR MONTHS and the axis label says so. A reader who takes
  924 and 1,103 as annual figures gets the shape of the last year wrong by a
  factor of three.

FIGURE 3 · The People's Strike, 22 June - 5 July 1944.
  A schematic on a real axis in days. Two things in this fortnight are NOT
  settled and both are drawn as bands rather than ticks, which is the same
  decision figure 2 of chapter 41 took about the two arrest counts:
    - the curfew is imposed on 25 June (Gyldendal og Politikens; Københavns
      Biblioteker) or 26 June (Arbejderen; sn.dk);
    - the return to work is 3 July (Gyldendal og Politikens), an order on the 4th
      obeyed on the 5th (Arbejderen), or the 5th (danmarkshistorien.lex.dk, which
      publishes the Council's 30 June and 1 July appeals and the 2 July
      counter-appeal but NOT the text of the final proclamation, which is why the
      question is open).
  Casualties from Gyldendal og Politikens Danmarkshistorie, "Folkestrejken": 23
  killed and 203 wounded on 1 July, and over 100 killed and more than 600 wounded
  over the whole strike. The 1 July pair is single-source and the figure's note
  says so.

D-11 THROUGHOUT: text colour is set with style=, never fill=. Item 105: CHAR_W is
under-measured and mapspine is NOT changed here; fold() and stack() are copied
from figs_41.py, which took them from figs_40.py and figs_39.py.
"""

import mapspine as M

PAPER = "#F4F1EA"
INK   = "#2A2A28"
DK    = "#2E6B5E"
DE    = "#8C5A3C"
OX    = "#9A3B2E"
IND   = "#2F4C7A"
GREY  = "#5F6157"
W     = 700
SWATCH = 14


# Item 105. mapspine.CHAR_W under-states mapt by about a tenth. mapspine is NOT
# changed here - that is the ledger decision in HANDOFF 105 - so this folds at the
# larger of the measured and table widths, exactly as figs_39 to figs_41 do.
MEASURED = {"mapt": 6.36, "mapx": 5.32, "mapl": 6.61}
CW = {k: max(M.CHAR_W[k], MEASURED[k]) for k in M.CHAR_W}


def fold(text, cls, x, avail):
    """Wrap to the width that fits, at the larger of measured and table width."""
    room = int((avail - x - 6) / CW[cls])
    out, line = [], ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > room:
            out.append(line)
            line = word
        else:
            line = (line + " " + word).strip()
    if line:
        out.append(line)
    return out


def width(text, cls):
    return len(text) * CW[cls]


def header(o, title, sub, note):
    o.append('<text x="14" y="24" class="mapl">%s</text>' % title)
    o.append('<text x="14" y="40" class="mapt">%s</text>' % sub)
    o.append('<text x="14" y="62" class="mapx" opacity=".75">%s</text>' % note)


def stack(labels, rows_gap, cls, left=12, right=W - 12):
    """Place labels in rows by SEARCH against the boxes already placed (item 76).

    labels is [(x, anchor, text)]; returns [(x, row, text)] where no two texts in
    one row overlap and every box is inside the canvas. Nothing here reasons about
    where a label ought to go: it tries row 0, and if the box hits one already
    there it tries the next row.
    """
    placed, out = [], []
    for x, anchor, t in labels:
        w = width(t, cls)
        x0 = x if anchor == "start" else (x - w / 2 if anchor == "middle" else x - w)
        x0 = min(max(x0, left), right - w)        # slide inside the canvas
        row = 0
        while any(r == row and not (x0 + w + 8 < a or a + aw + 8 < x0)
                  for r, a, aw in placed):
            row += 1
        placed.append((row, x0, w))
        out.append((x0, row, t))
    assert all(x0 >= left - 0.01 and x0 + width(t, cls) <= right + 0.01
               for x0, _, t in out), out
    return out, (max(r for _, r, _ in out) + 1) * rows_gap


def esc(text):
    """Escape for markup at the point of EMISSION, never in the data.

    `Burmeister & Wain` broke the XML parse on this script's first run. Putting
    `&amp;` in the data instead is the item 76 trap wearing different clothes:
    `width()` would measure five characters where the reader sees one, and every
    centring and collision decision downstream would be made on a string that is
    not the string being drawn.

    But escaping at emission is not sufficient either, and the second run proved
    it: `mapspine.check` reads the emitted markup, so IT measures `&amp;` as five
    characters while `stack()` measured one, and it reported a seven-unit
    collision that does not exist on the page. Two rulers for one rule, which is
    the fault item 64 named. The resolution is not to pick a ruler but to keep
    entities out of drawn text altogether - figure 3's label reads "Burmeister
    and Wain" - and to leave this function in place as the guard for any text
    that acquires one later.
    """
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def swatch_row(o, x, y, col, op, text):
    """A legend entry is a swatch and a label (item 118). Never a bare name."""
    o.append('<rect x="%.1f" y="%.1f" width="%d" height="8" fill="%s" opacity="%s"/>'
             % (x, y - 8, SWATCH, col, op))
    o.append('<text x="%.1f" y="%.1f" class="mapx" opacity=".9">%s</text>'
             % (x + SWATCH + 6, y, text))
    return x + SWATCH + 6 + width(text, "mapx")


# ------------------------------------------------------------------ figure 1
# The nominal counts. Fracapane, from the transport registration lists.
DEPORTED      = 472        # left Denmark
ARRIVED       = 470        # reached Theresienstadt; the 2 are named in the docstring
DIED_THER     = 51         # in the camp, over eighteen months
DIED_ELSEWHERE = 2         # the two who never arrived
INFANTS       = 2          # born in the camp, died there; Fracapane counts separately
RETURNED      = 419        # of the original 472

# The estimate. Not a count, and drawn as a band.
SW_LOW        = 7000       # "more than 7,000", every account
SW_ARCHIVE    = 7400       # Safe Haven, ~6,336 Swedish arrival reports, incomplete
SW_HIGH       = 7742       # 7,056 + 686: other people's addition of Bak's two facts
SW_PROTESTANT = 1000       # ">1,000 gave their religion as Protestant/Lutheran/Christian"

# The crossing's own dead. Bak, who declines to split drowning from suicide.
CROSSING_DEAD = 104        # "at least"; of which at least 42 and 2 shot by German police


def october():
    assert DEPORTED - ARRIVED == DIED_ELSEWHERE
    assert DIED_THER + DIED_ELSEWHERE == 53, DIED_THER + DIED_ELSEWHERE
    assert RETURNED + DIED_THER + DIED_ELSEWHERE == DEPORTED
    assert SW_LOW < SW_ARCHIVE < SW_HIGH

    x0, x1 = 120, W - 26
    row1_y, bar_h = 104, 26
    total = SW_ARCHIVE + DEPORTED          # the denominator drawn, and it is a sum
    sc = (x1 - x0) / float(total)          # units per person, row 1
    w_sw   = SW_ARCHIVE * sc
    w_dep  = DEPORTED * sc
    band_l = SW_LOW * sc
    band_h = SW_HIGH * sc
    assert abs(w_sw + w_dep - (x1 - x0)) < 0.01

    # Row 2 magnifies the 472 to the full width. THE FACTOR IS COMPUTED.
    # The gap must clear the whisker (bar_h + 11), its caps, and two label rows.
    row2_y = row1_y + bar_h + 104
    sc2 = (x1 - x0) / float(DEPORTED)
    factor = sc2 / sc
    assert factor > 1

    note = ("The two bars are not the same kind of number. The 472 is a nominal count, "
            "built by Fracapane from the transport registration lists, and it is drawn "
            "filled. The crossing to Sweden is an estimate and is drawn open: every "
            "account says about 7,000, the only figure attached to a named archive is "
            "roughly %s from the Danish Jewish Museum's Safe Haven database of Swedish "
            "arrival reports, and the %s in circulation is an addition performed on two "
            "separate statements. More than %s of those registering in Sweden gave their "
            "religion as Protestant, Lutheran or Christian. At least %d people died "
            "getting out or failing to, and they are in neither bar. Note what the "
            "whisker shows: the spread on the Sweden figure is %d people, which is "
            "wider than the entire deported count of %d."
            % ("{:,}".format(SW_ARCHIVE), "{:,}".format(SW_HIGH),
               "{:,}".format(SW_PROTESTANT), CROSSING_DEAD,
               SW_HIGH - SW_LOW, DEPORTED))
    note_lines = fold(note, "mapx", 14, W)

    LEG_Y = row2_y + bar_h + 38
    NOTE_TOP = LEG_Y + 20
    H = NOTE_TOP + len(note_lines) * 13 + 8        # HEIGHT COMPUTED

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="October 1943. Roughly seven thousand four hundred people reached '
         'Sweden, an estimate drawn as a band between seven thousand and seven thousand '
         'seven hundred and forty-two; four hundred and seventy-two were deported, a '
         'nominal count, of whom four hundred and nineteen came home and fifty-three did '
         'not.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "OCTOBER 1943",
           "to Sweden, to Theresienstadt, and the difference between the two numbers",
           "An estimate and a count, drawn differently on purpose.")

    # ---- row 1: the whole, at one scale
    o.append('<text x="14" y="%d" class="mapt" style="fill:%s">%s</text>'
             % (row1_y + bar_h // 2 + 5, INK, "crossed or taken"))

    # Sweden: OPEN, drawn to the archival estimate.
    #
    # THE RANGE IS A WHISKER AND NOT A BAND, and the raster is why. Drawn first as
    # a pale block between 7,000 and 7,742 inside the bar, it read as a THIRD
    # SEGMENT - pale block, then red block - so the figure appeared to show three
    # categories where it has two and an uncertainty. That is item 118's class
    # exactly, and validate, overruns and collisions all passed it. A whisker with
    # end caps below the bar cannot be read as a quantity.
    o.append('<rect x="%d" y="%d" width="%.1f" height="%d" fill="none" stroke="%s" '
             'stroke-width="1.1"/>' % (x0, row1_y, w_sw, bar_h, DK))

    # deported: FILLED
    o.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>'
             % (x0 + w_sw, row1_y, w_dep, bar_h, OX))

    wy = row1_y + bar_h + 11
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
             'stroke-width="1.1" opacity=".8"/>'
             % (x0 + band_l, wy, x0 + band_h, wy, DK))
    for e in (band_l, band_h):
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width="1.1" opacity=".8"/>'
                 % (x0 + e, wy - 4, x0 + e, wy + 4, DK))
    o.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="%s"/>' % (x0 + w_sw, wy, DK))

    lab1, gap1 = stack(
        [(x0 + w_sw / 2, "middle",
          "reached Sweden - estimate, about %s" % "{:,}".format(SW_ARCHIVE)),
         (x1, "end", "deported: %d" % DEPORTED)], 14, "mapx")
    for (lx, row, t), col in zip(lab1, (DK, OX)):
        o.append('<text x="%.1f" y="%.1f" class="mapx" style="fill:%s">%s</text>'
                 % (lx, wy + 20 + row * 14, col, t))

    rng = "the range in circulation: %s to %s" % ("{:,}".format(SW_LOW),
                                                  "{:,}".format(SW_HIGH))
    rw = width(rng, "mapx")
    rx = min(max(x0 + (band_l + band_h) / 2 - rw / 2, 14), W - 14 - rw)
    o.append('<text x="%.1f" y="%.1f" class="mapx" style="fill:%s" opacity=".8">%s</text>'
             % (rx, wy + 20 + (gap1 // 14) * 14, DK, rng))

    # ---- row 2: the 472 at its own scale
    seg = [(RETURNED, DK, ".85", "came home: %d" % RETURNED),
           (DIED_THER, OX, ".9", "died at Theresienstadt: %d" % DIED_THER),
           (DIED_ELSEWHERE, INK, ".9", "died after transfer: %d" % DIED_ELSEWHERE)]
    assert sum(n for n, _, _, _ in seg) == DEPORTED

    o.append('<text x="14" y="%d" class="mapt" style="fill:%s">the 472</text>'
             % (row2_y + bar_h // 2 + 5, INK))
    o.append('<text x="14" y="%d" class="mapx" opacity=".75">x%.0f scale</text>'
             % (row2_y + bar_h // 2 + 19, factor))

    cx = x0
    for n, col, op, _ in seg:
        w = n * sc2
        o.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" opacity="%s"/>'
                 % (cx, row2_y, w, bar_h, col, op))
        cx += w
        if cx < x1 - 0.5:
            o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
                     'stroke-width=".8"/>' % (cx, row2_y, cx, row2_y + bar_h, PAPER))
    assert abs(cx - x1) < 0.01, (cx, x1)

    # ---- legend: swatches, never bare names (item 118)
    lx = 14
    for _, col, op, t in seg:
        lx = swatch_row(o, lx, LEG_Y, col, op, t) + 22
    assert lx <= W - 12, lx

    fy = NOTE_TOP
    for ln in note_lines:
        o.append('<text x="14" y="%d" class="mapx" opacity=".85">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H + 13, (fy, H)
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
# (label, industrial, railway). 1945 is FOUR MONTHS and the label says so.
YEARS = [("1940 - 42", 73, 2),
         ("1943", 816, 111),
         ("1944", 988, 311),
         ("1945*", 924, 1103)]
IND_TOTAL_PUB  = 2801      # danmarkshistorien.lex.dk
RAIL_TOTAL_PUB = 1526      # danmarkshistorien.lex.dk


def sabotage():
    ind = sum(i for _, i, _ in YEARS)
    rail = sum(r for _, _, r in YEARS)
    assert ind == IND_TOTAL_PUB, (ind, IND_TOTAL_PUB)
    # THE ONE THAT DOES NOT RECONCILE. Asserted so that a future edit cannot make
    # the discrepancy disappear without this line failing (item 119).
    gap = rail - RAIL_TOTAL_PUB
    assert gap == 1, (rail, RAIL_TOTAL_PUB, gap)

    x0, x1 = 58, W - 26
    top, plot_h = 96, 168
    peak = max(max(i, r) for _, i, r in YEARS)
    assert peak == 1103, peak
    sc = plot_h / float(peak)

    n = len(YEARS)
    slot = (x1 - x0) / float(n)
    bw = slot * 0.30
    base_y = top + plot_h

    note = ("* 1945 is FOUR MONTHS, to the capitulation on 5 May. Read as a year it "
            "understates the last winter by a factor of three. The industrial column "
            "adds to its own published total of %s exactly. The railway column adds to "
            "%s against a published %s, and the missing one is marked rather than "
            "averaged away: a series quietly adjusted to its own total is worth less "
            "than one that has not been."
            % ("{:,}".format(IND_TOTAL_PUB), "{:,}".format(rail),
               "{:,}".format(RAIL_TOTAL_PUB)))
    note_lines = fold(note, "mapx", 14, W)
    LEG_Y = base_y + 44
    NOTE_TOP = LEG_Y + 20
    H = NOTE_TOP + len(note_lines) * 13 + 8        # HEIGHT COMPUTED

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Sabotage actions in Denmark by period. Industrial sabotage: '
         'seventy-three in 1940 to 1942 together, 816 in 1943, 988 in 1944 and 924 in the '
         'four months of 1945. Railway sabotage: two, 111, 311 and 1,103 over the same '
         'periods.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "SABOTAGE BY YEAR, 1940 - 1945",
           "industrial and railway actions, as the compilers counted them",
           "The graph does not rise. It starts - and then the railways overtake.")

    # gridlines and the value axis, computed
    step = 250
    v = 0
    while v <= peak:
        gy = base_y - v * sc
        o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" '
                 'stroke-width=".5" opacity=".45"/>' % (x0, gy, x1, gy, GREY))
        o.append('<text x="%d" y="%.1f" class="mapx" text-anchor="end" opacity=".7">%s'
                 '</text>' % (x0 - 6, gy + 4, "{:,}".format(v)))
        v += step

    for k, (lab, i, r) in enumerate(YEARS):
        cx = x0 + slot * (k + 0.5)
        for j, (val, col) in enumerate(((i, DE), (r, IND))):
            bx = cx - bw - 2 + j * (bw + 4)
            bh = val * sc
            o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" '
                     'opacity=".88"/>' % (bx, base_y - bh, bw, bh, col))
            t = "{:,}".format(val)
            tw = width(t, "mapx")
            tx = min(max(bx + bw / 2 - tw / 2, 14), W - 14 - tw)
            o.append('<text x="%.1f" y="%.1f" class="mapx" style="fill:%s">%s</text>'
                     % (tx, base_y - bh - 5, col, t))
        lw = width(lab, "mapt")
        o.append('<text x="%.1f" y="%d" class="mapt" style="fill:%s">%s</text>'
                 % (cx - lw / 2, base_y + 20, INK, lab))

    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width=".9"/>'
             % (x0, base_y, x1, base_y, INK))

    # The discrepancy. Its natural home is over the 1945 column it belongs to, and
    # that is exactly where the 1,103 bar's own value label sits: the first run put
    # it there and `collisions` reported 28 units of overlap. Placed instead over
    # the short columns on the left, which is the only region of this band with
    # nothing in it, and asserted against the tallest bar that could reach it.
    mark = "railway column adds to %s, published total %s" % ("{:,}".format(rail),
                                                              "{:,}".format(RAIL_TOTAL_PUB))
    mw = width(mark, "mapx")
    mx = 14
    reach = max(v for _, i, r in YEARS[:2] for v in (i, r))
    assert base_y - reach * sc > top + 4, (reach, base_y - reach * sc, top)
    assert mx + mw < x0 + slot * 2, (mw, x0 + slot * 2)
    # GREY, not OX: OX is the industrial series' own colour in this figure, and a
    # note about the railway column printed in the industrial colour contradicts
    # itself. An annotation gets the annotation colour.
    o.append('<text x="%.1f" y="%d" class="mapx" style="fill:%s">%s</text>'
             % (mx, top - 10, GREY, mark))

    lx = 14
    lx = swatch_row(o, lx, LEG_Y, DE, ".88", "industrial sabotage") + 22
    lx = swatch_row(o, lx, LEG_Y, IND, ".88", "railway sabotage")
    assert lx <= W - 12, lx

    fy = NOTE_TOP
    for ln in note_lines:
        o.append('<text x="14" y="%d" class="mapx" opacity=".85">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H + 13, (fy, H)
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
# Days from 22 June 1944, which is day 0. NOTHING below is a typed interval.
def d(june_day):
    return june_day - 22 if june_day <= 30 else (30 - 22) + (june_day - 30)


AX_LO, AX_HI = d(22), d(35)          # 22 June to 5 July
STRIKE_ON    = d(26)                 # B&W walk out
CURFEW_A, CURFEW_B = d(25), d(26)    # imposed: two dates in the sources
BACK_A, BACK_B     = d(33), d(35)    # 3 to 5 July: not settled
SIEGE        = d(31)                 # 1 July, state of siege
KILLED_1JUL, WOUNDED_1JUL = 23, 203
KILLED_ALL,  WOUNDED_ALL  = 100, 600

MARKS = [(d(22), "22 Jun", "BOPA destroys Riffelsyndikatet", OX),
         (d(23), "23 Jun", "eight resistance men executed", INK),
         (d(26), "26 Jun", "Burmeister and Wain walk out", DK),
         (d(29), "29 Jun", "the Hvidsten eight shot at Ryvangen", INK),
         (d(30), "30 Jun", "executions announced; general strike", DK),
         (d(31), "1 Jul", "state of siege; water, gas and power cut", OX),
         (d(32), "2 Jul", "mayors and unions appeal, and are ignored", IND)]


def daylabel(idx):
    """Index back to a date. d() is not invertible by eye, so it is inverted here.

    The first raster of this figure had an axis of fourteen unlabelled ticks: the
    reader could not find a date on it at all, and every guard passed, because an
    unlabelled tick is valid markup that collides with nothing.
    """
    return "%d Jun" % (22 + idx) if idx <= 8 else "%d Jul" % (idx - 8)


BANDS = [(DK, ".30", "the strike"),
         (DK, ".14", "the return to work, not settled"),
         (GREY, ".35", "the curfew's disputed start")]


def strike():
    assert AX_LO < STRIKE_ON < SIEGE < AX_HI
    assert CURFEW_A < CURFEW_B <= STRIKE_ON
    assert BACK_A < BACK_B <= AX_HI
    assert KILLED_1JUL < KILLED_ALL and WOUNDED_1JUL < WOUNDED_ALL
    # The inverse must agree with the forward map at both ends and across the join.
    for j in (22, 26, 30):
        assert daylabel(d(j)) == "%d Jun" % j, (j, daylabel(d(j)))
    for j, lab in ((31, "1 Jul"), (35, "5 Jul")):
        assert daylabel(d(j)) == lab, (j, daylabel(d(j)))

    x0, x1 = 40, W - 26
    ax = lambda t: x0 + (t - AX_LO) / float(AX_HI - AX_LO) * (x1 - x0)
    axis_y = 158

    labels, gap = stack([(ax(t), "middle", "%s  %s" % (tag, txt))
                         for t, tag, txt, _ in MARKS], 14, "mapx")
    LAB_TOP = axis_y + 42
    note = ("Two dates in this fortnight are not settled and both are drawn as bands. "
            "The curfew is imposed on 25 or 26 June depending on the source. The return "
            "to work is 3 July on one standard account, an order on the 4th obeyed on the "
            "5th on another, and the 5th on the site that publishes the Council's own "
            "appeals - and which does not publish the text of the final proclamation, "
            "which is why the question is open. On 1 July alone %d people were killed and "
            "%d wounded; over the whole strike more than %d were killed and more than %d "
            "wounded. The single-day pair rests on one source."
            % (KILLED_1JUL, WOUNDED_1JUL, KILLED_ALL, WOUNDED_ALL))
    note_lines = fold(note, "mapx", 14, W)
    LEG_Y = LAB_TOP + gap + 20
    NOTE_TOP = LEG_Y + 20
    H = NOTE_TOP + len(note_lines) * 13 + 8        # HEIGHT COMPUTED

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="The Copenhagen People\'s Strike on an axis of days from 22 June to '
         '5 July 1944, from the destruction of Riffelsyndikatet to the return to work, '
         'with the disputed curfew date and the disputed return date drawn as bands.">'
         % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "THE PEOPLE'S STRIKE, JUNE - JULY 1944",
           "an axis in days: the two disputed dates are bands, not ticks",
           "A city stopped when a council with no legal existence asked it to.")

    # the strike itself, as a bar with a duration
    o.append('<rect x="%.1f" y="%d" width="%.1f" height="12" fill="%s" opacity=".30"/>'
             % (ax(STRIKE_ON), axis_y - 12, ax(BACK_A) - ax(STRIKE_ON), DK))
    # the unsettled tail of it
    o.append('<rect x="%.1f" y="%d" width="%.1f" height="12" fill="%s" opacity=".14"/>'
             % (ax(BACK_A), axis_y - 12, ax(BACK_B) - ax(BACK_A), DK))
    # the curfew's disputed start
    o.append('<rect x="%.1f" y="%d" width="%.1f" height="7" fill="%s" opacity=".35"/>'
             % (ax(CURFEW_A), axis_y - 24, ax(CURFEW_B) - ax(CURFEW_A), GREY))

    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width=".8"/>'
             % (x0, axis_y, x1, axis_y, GREY))
    for t in range(AX_LO, AX_HI + 1):
        major = (t % 2 == 0)
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
                 'stroke-width=".6"/>'
                 % (ax(t), axis_y, ax(t), axis_y + (8 if major else 4), GREY))
        if major:
            lab = daylabel(t)
            lw = width(lab, "mapx")
            lx = min(max(ax(t) - lw / 2, 14), W - 14 - lw)
            o.append('<text x="%.1f" y="%d" class="mapx" opacity=".8">%s</text>'
                     % (lx, axis_y + 22, lab))

    for t, _, _, col in MARKS:
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
                 'stroke-width="1.8"/>' % (ax(t), axis_y - 26, ax(t), axis_y, col))

    for (lx, row, txt), (_, _, _, col) in zip(labels, MARKS):
        o.append('<text x="%.1f" y="%d" class="mapx" style="fill:%s">%s</text>'
                 % (lx, LAB_TOP + row * 14, col, esc(txt)))

    # the two bands get named where they are, by search against the marks
    band_lab, band_gap = stack(
        [((ax(CURFEW_A) + ax(CURFEW_B)) / 2, "middle", "curfew imposed: 25 or 26 June"),
         ((ax(BACK_A) + ax(BACK_B)) / 2, "middle", "back to work: 3 to 5 July")],
        14, "mapx")
    for lx, row, t in band_lab:
        o.append('<text x="%.1f" y="%d" class="mapx" style="fill:%s">%s</text>'
                 % (lx, 104 + row * 14, GREY, t))

    # The three shaded bands get swatches (item 118). The first raster showed a
    # green block, a paler green block and a grey block with nothing anywhere
    # saying which was the strike.
    lx = 14
    for col, op, t in BANDS:
        lx = swatch_row(o, lx, LEG_Y, col, op, t) + 20
    assert lx <= W - 12, lx

    fy = NOTE_TOP
    for ln in note_lines:
        o.append('<text x="14" y="%d" class="mapx" opacity=".85">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H + 13, (fy, H)
    o.append('</svg>')
    return "\n  ".join(o)


FIGS = [("svg_oktober_1943.txt", october),
        ("svg_sabotage_1945.txt", sabotage),
        ("svg_folkestrejke_1944.txt", strike)]

if __name__ == "__main__":
    for name, fn in FIGS:
        svg = fn()
        M.validate(svg, name)
        for bad in (M.check(svg, name) or []):
            print("  !! %s" % (bad,))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
