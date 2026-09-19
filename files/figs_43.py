# -*- coding: utf-8 -*-
"""Figures for chapter 43.

PLAN_I §13 LISTED THREE FIGURES AND TWO OF THEM WERE SCHEMATICS. The plan's own
note said the fix was to convert the schematics into data figures, and that is
what is built here. "Bornholm: liberated last, occupied longest" becomes an axis
in days computed from the dates; "Which way to lean, 1945-49" is dropped, because
a schematic of a decision is a diagram of an argument and not evidence for it,
and South Schleswig - which has real series - takes its place.

FIGURE 1 · What the 13,521 convictions were for.
  Source: lex.dk, "retsopgoeret i Danmark", the official table at final instance.
  German military service 7,277 (6,930 men / 347 women); German police service
  1,638; oekonomisk samarbejde 1,139 (1,114 / 25); angiveri 413 (306 / 107);
  about fifty prosecutions of Danish Nazi leaders. Total 13,521 (12,877 / 644).

  THE NAMED CATEGORIES DO NOT ADD TO THE TOTAL and this figure refuses to hide
  it. 7,277 + 1,638 + 1,139 + 413 + 50 is 10,517 against 13,521, so 3,004
  convictions - more than a fifth of the reckoning - are in categories the
  published summary does not name. The women's columns leave a residual too: 347
  + 25 + 107 is 479 against 644. Both residuals are COMPUTED below, asserted, and
  DRAWN as their own bar, hatched, rather than dropped so that the bars look like
  a whole. Item 119's rule: check a fetched table against its own total.

  The women's share is drawn as an inset inside each bar, because the argument of
  section 05 is a share and not a level: 107 of 413 is a quarter of the informing
  column from a group that is five per cent of the whole. Two of the six bars
  have NO figure for women in the source - police service and the Nazi leaders -
  and those two are drawn with no inset and marked, rather than with an inset of
  zero, which would assert something the source does not say.

FIGURE 2 · Bornholm: occupied 335 days longer.
  NOTHING IN THIS FIGURE IS A TYPED INTERVAL. Every length is a difference of two
  dates computed at build time: the occupation opens on 9 April 1940 for both
  bars; the mainland's ends on 5 May 1945; Bornholm's German phase ends when the
  Red Army lands on 9 May 1945 and the Soviet phase ends on 5 April 1946. The
  Danish note of 4 March 1946 is marked on the lower bar. D-8 says treat every
  "N years" as a claim; the cheapest way to keep that promise in a figure is to
  make the figure do the arithmetic.

FIGURE 3 · South Schleswig: members, meals and votes, 1945-1954.
  EVERY SERIES HERE HAS TWO READINGS, NOT A CURVE, and drawing two points joined
  by a line would assert a trajectory nobody measured. So the figure draws the
  MULTIPLIER between the two readings, on a log axis about 1, with both readings
  and both dates printed on the row. The argument survives the honesty: the
  membership and the food relief multiply by almost exactly the same factor over
  overlapping periods, and the vote then goes the other way.

  Readings: organisation 3,000 (May 1945) to 68,317 (January 1947); pupils 436
  (1945) to 13,212 (1950); food relief 3,700 (July 1945) to 79,000 (August 1947);
  Landtag vote 99,500 (1947) to 42,242 (1954). The periods are NOT the same
  length and the figure says so on every row rather than in a footnote.

D-11 THROUGHOUT: text colour is set with style=, never fill=. Item 105: CHAR_W is
under-measured and mapspine is NOT changed here; fold(), width(), stack() and
swatch_row() are copied from figs_42.py.
"""

from datetime import date
import math

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

MEASURED = {"mapt": 6.36, "mapx": 5.32, "mapl": 6.61}
CW = {k: max(M.CHAR_W[k], MEASURED[k]) for k in M.CHAR_W}


def fold(text, cls, x, avail):
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


def esc(text):
    """Escape at EMISSION, never in the data. See figs_42.esc for the two traps."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def header(o, title, sub, note):
    o.append('<text x="14" y="24" class="mapl">%s</text>' % title)
    o.append('<text x="14" y="40" class="mapt">%s</text>' % sub)
    o.append('<text x="14" y="62" class="mapx" opacity=".75">%s</text>' % note)


def swatch_row(o, x, y, col, op, text):
    o.append('<rect x="%.1f" y="%.1f" width="%d" height="8" fill="%s" opacity="%s"/>'
             % (x, y - 8, SWATCH, col, op))
    o.append('<text x="%.1f" y="%.1f" class="mapx" opacity=".9">%s</text>'
             % (x + SWATCH + 6, y, text))
    return x + SWATCH + 6 + width(text, "mapx")


def n(v):
    return "{:,}".format(v)


# ------------------------------------------------------------------ figure 1
TOTAL, TOTAL_M, TOTAL_W = 13521, 12877, 644

# (label, total, women or None when the source gives no women's figure, colour)
# ONE COLOUR FOR THE DATA BARS. The first raster gave each category its own -
# brown, oxblood, indigo, grey - and the categories are not a scale, an ordering
# or a grouping, so the colour was decoration standing where meaning should be,
# with a legend swatch in one of the four implying that it meant something. The
# only colour distinction the figure earns is data against residual.
CATS = [("service in the German forces",     7277, 347,  DE),
        ("service in the German police",     1638, None, DE),
        ("building for the Wehrmacht",       1139, 25,   DE),
        ("informing",                         413, 107,  DE),
        ("the Danish Nazi leadership",         50, None, DE)]


def domme():
    named = sum(c[1] for c in CATS)
    rest = TOTAL - named
    named_w = sum(c[2] for c in CATS if c[2] is not None)
    rest_w = TOTAL_W - named_w
    # Both residuals are asserted so that a later edit to the table cannot make
    # either of them vanish without this line failing (item 119).
    assert named == 10517 and rest == 3004, (named, rest)
    assert named_w == 479 and rest_w == 165, (named_w, rest_w)
    assert TOTAL_M + TOTAL_W == TOTAL, (TOTAL_M, TOTAL_W, TOTAL)

    rows = list(CATS) + [("categories the published summary does not name",
                          rest, rest_w, GREY)]

    x0, x1 = 14, W - 14
    lab_w = max(width(t, "mapt") for t, _, _, _ in rows)
    bar_x = x0 + lab_w + 12
    val_room = width(n(TOTAL), "mapx") + 10
    bar_max = x1 - bar_x - val_room
    assert bar_max > 180, bar_max
    sc = bar_max / float(max(v for _, v, _, _ in rows))

    top = 88
    gap = 26
    bh = 15

    note = ("The named categories add to %s of %s. The remaining %s convictions - more "
            "than a fifth of the whole reckoning - are in categories the published "
            "summary does not itemise, and they are drawn rather than dropped. The "
            "women's insets do the same: %s of the %s women convicted are inside the "
            "three categories with a published women's figure, and %s are not. Two bars "
            "carry a dashed mark instead of an inset because the source gives no "
            "women's figure for them, which is not the same as a figure of none; and "
            "the 25 women among the Wehrmacht's builders are two per cent of that bar "
            "and are drawn to scale, which at this width is a hairline."
            % (n(named), n(TOTAL), n(rest), n(named_w), n(TOTAL_W), n(rest_w)))
    note_lines = fold(note, "mapx", 14, W)
    base_y = top + gap * len(rows)
    LEG_Y = base_y + 26
    NOTE_TOP = LEG_Y + 20
    H = NOTE_TOP + len(note_lines) * 13 + 8            # HEIGHT COMPUTED

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="What the 13,521 convictions of the Danish retsopgoer were for. '
         'Service in the German forces 7,277; service in the German police 1,638; '
         'building for the Wehrmacht 1,139; informing 413; the Danish Nazi leadership '
         'about fifty; and 3,004 in categories the published summary does not name.">'
         % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "WHAT THE 13,521 CONVICTIONS WERE FOR",
           "the official table at final instance, with the women's share inset",
           "More than half of the reckoning is service in a uniform.")

    for k, (lab, val, wom, col) in enumerate(rows):
        y = top + gap * k
        lw = width(lab, "mapt")
        o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="end" '
                 'style="fill:%s">%s</text>' % (bar_x - 8, y + bh - 3, INK, esc(lab)))
        assert bar_x - 8 - lw >= x0 - 0.01, (lab, lw)
        bw = val * sc
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="%s" '
                 'opacity=".85"/>' % (bar_x, y, bw, bh, col))
        if lab.startswith("categories"):
            # The residual is not a category. Hatched, so it cannot be read as one.
            for hx in range(int(bar_x) + 4, int(bar_x + bw), 7):
                o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" '
                         'stroke-width=".7" opacity=".55"/>'
                         % (hx, y + bh, hx - bh, y, PAPER))
        if wom is not None:
            o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="%s"/>'
                     % (bar_x, y, wom * sc, bh, INK))
        else:
            # NOT an inset of zero. The source publishes no women's figure for
            # these two, and drawing nothing at all would assert that it does and
            # that the answer is none.
            # Never wider than the bar it marks: on the fifty-conviction row a
            # fixed 7-unit box was four times the bar and read as the bar.
            mw = min(7.0, bw - 1)
            if mw >= 2:
                o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="none" '
                         'stroke="%s" stroke-width="1" stroke-dasharray="2 2" '
                         'opacity=".85"/>' % (bar_x + 0.5, y + 0.5, mw, bh - 1, INK))
        vt = n(val) if val != 50 else "about 50"
        o.append('<text x="%.1f" y="%.1f" class="mapx" style="fill:%s">%s</text>'
                 % (bar_x + bw + 6, y + bh - 3, INK, vt))
        assert bar_x + bw + 6 + width(vt, "mapx") <= x1 + 0.01, (lab, val)

    lx = 14
    lx = swatch_row(o, lx, LEG_Y, DE, ".85", "convictions") + 20
    lx = swatch_row(o, lx, LEG_Y, INK, "1", "women, where the source gives a figure") + 20
    o.append('<rect x="%.1f" y="%.1f" width="%d" height="8" fill="none" stroke="%s" '
             'stroke-width="1" stroke-dasharray="2 2"/>'
             % (lx, LEG_Y - 8, SWATCH, INK))
    lt = "no women's figure published"
    o.append('<text x="%.1f" y="%.1f" class="mapx" opacity=".9">%s</text>'
             % (lx + SWATCH + 6, LEG_Y, lt))
    lx = lx + SWATCH + 6 + width(lt, "mapx")
    assert lx <= W - 12, lx

    fy = NOTE_TOP
    for ln in note_lines:
        o.append('<text x="14" y="%d" class="mapx" opacity=".85">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H + 13, (fy, H)
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
INVADED   = date(1940, 4, 9)
MAINLAND  = date(1945, 5, 5)
RED_ARMY  = date(1945, 5, 9)
DK_NOTE   = date(1946, 3, 4)
SOVIET_GO = date(1946, 4, 5)


def days(a, b):
    return (b - a).days


def bornholm():
    main_d = days(INVADED, MAINLAND)
    german_d = days(INVADED, RED_ARMY)
    total_d = days(INVADED, SOVIET_GO)
    soviet_d = days(RED_ARMY, SOVIET_GO)
    note_d = days(INVADED, DK_NOTE)
    extra = total_d - main_d
    after_note = days(DK_NOTE, SOVIET_GO)
    waited = days(MAINLAND, DK_NOTE)
    assert german_d + soviet_d == total_d, (german_d, soviet_d, total_d)
    assert (main_d, total_d, soviet_d, extra) == (1852, 2187, 331, 335), \
        (main_d, total_d, soviet_d, extra)
    assert (note_d, after_note, waited) == (2155, 32, 303), (note_d, after_note, waited)

    x0, x1 = 128, W - 20
    sc = (x1 - x0) / float(total_d)
    top = 96
    bh = 26
    gap = 52

    note = ("Days, computed from the dates and not from anybody's rounding. Denmark was "
            "occupied for %s days and Bornholm for %s, a difference of %s. The Soviet "
            "occupation itself ran %s days - but Denmark did not ask for the island back "
            "until %s days after its own liberation, and the Red Army was gone %s days "
            "after the note. Nine tenths of the wait was Danish."
            % (n(main_d), n(total_d), n(extra), n(soviet_d), n(waited), n(after_note)))
    note_lines = fold(note, "mapx", 14, W)
    # base_y clears the lower bar AND the date label hung under it (nty below).
    base_y = top + gap + bh + 36
    LEG_Y = base_y + 8
    NOTE_TOP = LEG_Y + 22
    H = NOTE_TOP + len(note_lines) * 13 + 8            # HEIGHT COMPUTED

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Two bars in days from 9 April 1940. The Danish mainland was '
         'occupied 1,852 days, to 5 May 1945. Bornholm was occupied 2,187 days, of '
         'which the last 331 were Soviet, to 5 April 1946 - 335 days longer.">'
         % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "BORNHOLM: OCCUPIED 335 DAYS LONGER",
           "days from 9 April 1940, computed from the dates",
           "The island was not liberated last by a week. It was liberated last by "
           "eleven months.")

    BARS = [("the mainland", [(main_d, DE, ".85", "German")], MAINLAND, "5 May 1945"),
            ("Bornholm", [(german_d, DE, ".85", "German"),
                          (soviet_d, OX, ".85", "Soviet")], SOVIET_GO, "5 April 1946")]
    for k, (lab, segs, end, endlab) in enumerate(BARS):
        y = top + gap * k
        o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="end" '
                 'style="fill:%s">%s</text>' % (x0 - 10, y + bh - 8, INK, lab))
        assert x0 - 10 - width(lab, "mapt") >= 14, lab
        run = 0
        for val, col, op, _ in segs:
            o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="%s" '
                     'opacity="%s"/>' % (x0 + run * sc, y, val * sc, bh, col, op))
            run += val
        t = "%s days, to %s" % (n(run), endlab)
        tw = width(t, "mapx")
        tx = x0 + run * sc + 8
        if tx + tw > x1:
            tx = x0 + run * sc - 8 - tw
        o.append('<text x="%.1f" y="%.1f" class="mapx" style="fill:%s">%s</text>'
                 % (tx, y + bh + 14, INK, t))
        assert 14 <= tx and tx + tw <= W - 14, (t, tx, tw)

    # the gap between the two bars' ends
    gx0 = x0 + main_d * sc
    gx1 = x0 + total_d * sc
    gy = top - 12
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
             'stroke-width=".9"/>' % (gx0, gy, gx1, gy, INK))
    for gx in (gx0, gx1):
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width=".9"/>' % (gx, gy - 4, gx, gy + 4, INK))
    gt = "%s days" % n(extra)
    gtw = width(gt, "mapx")
    gtx = min(max((gx0 + gx1) / 2 - gtw / 2, 14), W - 14 - gtw)
    o.append('<text x="%.1f" y="%.1f" class="mapx" style="fill:%s">%s</text>'
             % (gtx, gy - 8, INK, gt))

    # the Danish note, on the lower bar
    nx = x0 + note_d * sc
    ny = top + gap
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
             'stroke-width="1.2"/>' % (nx, ny - 6, nx, ny + bh + 6, INK))
    nt = "Denmark asks, 4 March 1946"
    ntw = width(nt, "mapt")
    ntx = min(nx - ntw - 8, W - 14 - ntw)
    nty = ny + bh + 28
    assert ntx >= 14, (ntx, ntw)
    assert nty < base_y, (nty, base_y)
    o.append('<text x="%.1f" y="%.1f" class="mapt" style="fill:%s">%s</text>'
             % (ntx, nty, INK, nt))

    # LEG_Y, not LEG_Y + 14. The first raster drew the swatches fourteen units
    # below the row NOTE_TOP had been computed from, so the legend sat on the
    # footnote's first line - and collision checking did not see it, because both
    # were valid text at different y. The guard below is the fix for the class.
    lx = 14
    lx = swatch_row(o, lx, LEG_Y, DE, ".85", "German occupation") + 22
    lx = swatch_row(o, lx, LEG_Y, OX, ".85", "Soviet occupation of Bornholm")
    assert lx <= W - 12, lx
    assert NOTE_TOP - LEG_Y >= 18, (LEG_Y, NOTE_TOP)

    fy = NOTE_TOP
    for ln in note_lines:
        o.append('<text x="14" y="%d" class="mapx" opacity=".85">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H + 13, (fy, H)
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
# (row label, first reading, its date, second reading, its date, colour)
# One colour, as in figure 1: the direction of each bar already carries the only
# distinction there is, so a second encoding in hue would be decoration.
SLESVIG = [("members of the Danish organisation", 3000, "May 1945", 68317,
            "Jan 1947", DK),
           ("pupils in Danish schools", 436, "1945", 13212, "1950", DK),
           ("people fed by Danish relief", 3700, "Jul 1945", 79000, "Aug 1947", DK),
           ("votes for the Danish list", 99500, "1947", 42242, "1954", DK)]

# The axis is logarithmic and the first raster did not say so anywhere: x 30.3 sat
# barely longer than x 22.8 and x 0.42 ran further than either, so a reader
# comparing lengths would have read every ratio wrong. These are the stops.
STOPS = [0.5, 1, 2, 5, 10, 20, 50, 100]


def sydslesvig():
    mults = [b / float(a) for _, a, _, b, _, _ in SLESVIG]
    # The three that rise do so by factors within a third of one another; the one
    # that falls loses more than half. Asserted, because that IS the figure.
    assert all(m > 20 for m in mults[:3]) and mults[3] < 0.5, mults
    # Padding is DERIVED from the widest value label, not guessed: the first run
    # used a symmetric 0.12 decades and the longest bar's label ran 34 units off
    # the right edge while the falling bar's label reached back into the gutter.
    vts = [("x %.1f" % m) if m >= 1 else ("x %.2f" % m) for m in mults]
    vmax = max(width(v, "mapx") for v in vts)
    lo = min(math.log10(m) for m in mults) - 0.30
    hi = max(math.log10(m) for m in mults) + 0.06

    # x0 is DERIVED from the widest label and its date line, not typed: the first
    # run set it to 236 and the longest row label ran four units off the canvas.
    gutter = max(max(width(l, "mapt") for l, _, _, _, _, _ in SLESVIG),
                 max(width("%s (%s) to %s (%s)" % (n(a), ad, n(b), bd), "mapx")
                     for _, a, ad, b, bd, _ in SLESVIG))
    x0, x1 = 14 + gutter + 12, W - 20 - vmax - 6
    assert x1 - x0 > 200, (x0, x1)
    zero = x0 + (0 - lo) / (hi - lo) * (x1 - x0)
    sc = (x1 - x0) / (hi - lo)
    # top clears the header's third line at y=62 AND the 'no change' caption,
    # which hangs 32 above it. At 100 the two overlapped by 51 units.
    top = 114
    gap = 34
    bh = 15

    note = ("Each row is a MULTIPLIER between two readings, not a curve: every series "
            "here has two published points and joining them with a line would draw a "
            "trajectory nobody measured. The periods differ and are printed on each "
            "row. The membership and the food relief multiply by %.1f and %.1f over "
            "overlapping periods, which is the coincidence section 06 is about; the "
            "vote then falls to %.2f of itself in seven years."
            % (mults[0], mults[2], mults[3]))
    note_lines = fold(note, "mapx", 14, W)
    base_y = top + gap * len(SLESVIG)
    NOTE_TOP = base_y + 14
    H = NOTE_TOP + len(note_lines) * 13 + 8            # HEIGHT COMPUTED

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="South Schleswig, 1945 to 1954, as multipliers between two readings. '
         'Members of the Danish organisation multiply about twenty-three times, pupils '
         'about thirty, people fed by Danish relief about twenty-one - and the Danish '
         'vote falls to about four tenths of itself.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "SOUTH SCHLESWIG: MEMBERS, MEALS AND VOTES",
           "the multiplier between each series' two published readings, "
           "on a logarithmic scale",
           "Three things multiplied by about the same amount. Then one of them "
           "went back.")

    shown = [s for s in STOPS if lo <= math.log10(s) <= hi]
    assert len(shown) >= 4, shown
    for s in shown:
        gx = x0 + (math.log10(s) - lo) * sc
        if abs(s - 1.0) < 1e-9:
            continue
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width=".5" opacity=".35"/>' % (gx, top - 12, gx, base_y, GREY))
        st = ("x %g" % s)
        stw = width(st, "mapx")
        o.append('<text x="%.1f" y="%d" class="mapx" opacity=".6">%s</text>'
                 % (gx - stw / 2, top - 18, st))
        assert gx - stw / 2 >= 14 and gx + stw / 2 <= W - 14, (s, gx)
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" '
             'stroke-width=".9" opacity=".8"/>' % (zero, top - 12, zero, base_y, INK))
    zt = "no change"
    ztw = width(zt, "mapx")
    o.append('<text x="%.1f" y="%d" class="mapx" opacity=".75">%s</text>'
             % (zero - ztw / 2, top - 32, zt))

    for k, (lab, a, ad, b, bd, col) in enumerate(SLESVIG):
        y = top + gap * k
        m = b / float(a)
        o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="end" '
                 'style="fill:%s">%s</text>' % (x0 - 10, y + bh - 3, INK, lab))
        assert x0 - 10 - width(lab, "mapt") >= 14, lab
        end = x0 + (math.log10(m) - lo) * sc
        bx, bw = (zero, end - zero) if end >= zero else (end, zero - end)
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="%s" '
                 'opacity=".85"/>' % (bx, y, bw, bh, col))
        vt = vts[k]
        vtw = width(vt, "mapx")
        vtx = end + 6 if end >= zero else end - 6 - vtw
        o.append('<text x="%.1f" y="%.1f" class="mapx" style="fill:%s">%s</text>'
                 % (vtx, y + bh - 3, INK, vt))
        assert 14 <= vtx and vtx + vtw <= W - 14, (lab, vtx, vtw)
        sub = "%s (%s) to %s (%s)" % (n(a), ad, n(b), bd)
        o.append('<text x="%.1f" y="%.1f" class="mapx" text-anchor="end" '
                 'opacity=".75">%s</text>' % (x0 - 10, y + bh + 11, sub))
        assert x0 - 10 - width(sub, "mapx") >= 14, sub

    fy = NOTE_TOP
    for ln in note_lines:
        o.append('<text x="14" y="%d" class="mapx" opacity=".85">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H + 13, (fy, H)
    o.append('</svg>')
    return "\n  ".join(o)


FIGS = [("svg_domme_1945.txt", domme),
        ("svg_bornholm_1946.txt", bornholm),
        ("svg_sydslesvig_1954.txt", sydslesvig)]

if __name__ == "__main__":
    for name, fn in FIGS:
        svg = fn()
        M.validate(svg, name)
        for bad in (M.check(svg, name) or []):
            print("  !! %s" % (bad,))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
