# -*- coding: utf-8 -*-
"""Figures for chapter 44.

PLAN_I §13 asked for three and called the first "the key figure". It is, and it
is built as asked. The third was a schematic — "What §20 installed, and what
walked through it in 1973" — and is NOT built, for the reason chapter 43 gave
when it dropped its own: a schematic of a decision is a diagram of an argument
and not evidence for it. What replaces it is the second ballot of 28 May 1953,
which is data, which nobody draws, and which makes §08's point better.

FIGURE 1 · 1939 and 1953 against the forty-five per cent floor.
  THE WHOLE POINT IS THAT THE MORE POPULAR PROPOSAL IS THE ONE THAT FAILED. In
  1939, 91.85 per cent of those voting said yes and the revision died; in 1953,
  78.76 per cent said yes and it carried. So the figure does NOT draw the share
  of votes cast, which would show 1939 winning. It draws each result against the
  denominator that actually decided it - the WHOLE ELECTORATE - with the 45 per
  cent floor as a line across both. Yes, no and the people who did not vote are
  drawn as one bar summing to 100 per cent of the electorate, because the
  argument is that a threshold on the electorate silently counts an abstention
  as a no, and that is only visible if the abstentions are on the picture.

  1953 returns: electorate 2,585,800, yes 1,183,292, no 319,135, invalid 25,231,
  cast 1,527,658 (Nohlen and Stover). They reconcile exactly, which is why they
  are used. 1939: yes 966,277, no 85,717, yes 44.46 per cent of the electorate
  (Interior Ministry tables via lex.dk, verified at open item 108). THE 1939
  ELECTORATE IS NOT PUBLISHED IN ANY SOURCE REACHED, so it is DERIVED from the
  yes count and the published percentage, the derivation is asserted to round
  back to 44.46, and the figure marks that bar as derived rather than passing it
  off as counted.

FIGURE 2 · The Landsting, 1849-1953: 104 years in four regimes.
  A time axis in years, every span computed from the dates. What changes at each
  node is WHO CHOSE THE CHAMBER, which is the only thing that ever mattered about
  it: electors from men over forty in 1849; Estrup's privileged franchise with
  twelve royal appointees in 1866; ordinary voters over thirty-five in 1915 with
  a quarter co-opted by the outgoing chamber. The 1936 alignment of its majority
  with the Folketing's and the self-abolition of 13 May 1953 are marked.

FIGURE 3 · Two ballots, one Thursday.
  The same voters, the same day, two questions, and TWO DIFFERENT ELECTORATES -
  2,585,800 for the constitution and 2,815,100 for the voting age, a difference
  of 229,300. The gap is drawn, because it is the figure's whole content: the
  second question was open to the people the second question was about, they
  turned out, and they lost 840,815 to 700,122.

D-11 THROUGHOUT: text colour is set with style=, never fill=. fold(), width(),
header() and swatch_row() are copied from figs_43.py, which took them from
figs_42.py; item 105's CHAR_W is still under-measured and mapspine is NOT changed.
"""

from datetime import date

import mapspine as M

PAPER = "#F4F1EA"
INK   = "#2A2A28"
DK    = "#2E6B5E"
DE    = "#8C5A3C"
OX    = "#9A3B2E"
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
    return "{:,}".format(int(round(v)))


def notes(o, lines, top):
    y = top
    for ln in lines:
        o.append('<text x="14" y="%d" class="mapx" opacity=".85">%s</text>' % (y, ln))
        y += 13
    return y


# ------------------------------------------------------------------ figure 1
E53, Y53, N53, I53, C53 = 2585800, 1183292, 319135, 25231, 1527658
Y39, N39, PCT39 = 966277, 85717, 0.4446
FLOOR = 0.45


def floor_fig():
    assert Y53 + N53 + I53 == C53, (Y53, N53, I53, C53)
    # The 1939 electorate is NOT published in any source reached. Derived, and the
    # derivation asserted to round back to the published percentage.
    e39 = Y39 / PCT39
    assert abs(Y39 / e39 - PCT39) < 1e-9
    assert abs(round(100 * Y39 / e39, 2) - 44.46) < 0.005, round(100 * Y39 / e39, 2)

    # ONE DEFINITION FOR BOTH ROWS. The first raster computed the 1953 third block
    # as cast - yes - no, which is only the 25,231 spoiled ballots, while 1939 used
    # electorate - yes - no. The two bars were drawn to different denominators, the
    # 1953 bar stopped three quarters of the way across, and the figure understated
    # the thing it exists to show. The third block is everyone who did not vote yes
    # or no - non-voters and spoiled papers together - because that is exactly what
    # a threshold on the electorate treats as a no.
    rows = [("1953", E53, Y53, N53, E53 - Y53 - N53, False),
            ("1939", e39, Y39, N39, e39 - Y39 - N39, True)]
    for lab, elec, yes, no, abst, _ in rows:
        assert abs((yes + no + abst) - elec) < 0.5, (lab, yes + no + abst, elec)

    x0 = 14 + max(width("1953", "mapl"), width("1939", "mapl")) + 14
    x1 = W - 16
    span = x1 - x0
    top, bh, gap = 108, 34, 74

    note = ("Each bar is the WHOLE ELECTORATE, not the votes cast, because that is the "
            "denominator the rule used. The floor is 45 per cent of it. In 1939 the yes "
            "vote was %s per cent of those who voted and the revision FAILED; in 1953 it "
            "was %s per cent and it PASSED. The difference is the third block - the "
            "people who did not vote - which a threshold on the electorate counts as a "
            "no - %s of them in 1953 alone. 1953 cleared the line by %s votes. The 1939 "
            "electorate is DERIVED from "
            "its published 44.46 per cent and is drawn hatched; every other quantity here "
            "is counted."
            % ("%.2f" % (100.0 * Y39 / (Y39 + N39)), "%.2f" % (100.0 * Y53 / (Y53 + N53)),
               n(E53 - Y53 - N53), n(Y53 - FLOOR * E53)))
    nl = fold(note, "mapx", 14, W)
    base = top + gap * len(rows)
    LEG_Y = base + 6
    NOTE_TOP = LEG_Y + 24
    H = NOTE_TOP + len(nl) * 13 + 8                     # HEIGHT COMPUTED

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="The Danish constitutional referendums of 1939 and 1953 measured '
         'against a floor of 45 per cent of the whole electorate. In 1939 the yes vote '
         'reached 44.46 per cent and failed. In 1953 it reached 45.76 per cent and '
         'passed, by 19,682 votes.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "1939 AND 1953 AGAINST THE FORTY-FIVE PER CENT FLOOR",
           "yes, no and those who did not vote, as shares of the whole electorate",
           "The more popular proposal is the one that failed.")

    fx = x0 + FLOOR * span
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.4" '
             'stroke-dasharray="4 3"/>' % (fx, top - 22, fx, base - gap + bh + 6, INK))
    ft = "45% floor"
    o.append('<text x="%.1f" y="%d" class="mapt" style="fill:%s">%s</text>'
             % (fx + 6, top - 26, INK, ft))
    assert fx + 6 + width(ft, "mapt") <= W - 14

    for k, (lab, elec, yes, no, abst, derived) in enumerate(rows):
        y = top + gap * k
        o.append('<text x="14" y="%.1f" class="mapl" style="fill:%s">%s</text>'
                 % (y + bh - 10, INK, lab))
        run = 0.0
        for val, col, op in ((yes, DK, ".88"), (no, OX, ".80"), (abst, GREY, ".28")):
            wpx = span * val / elec
            o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="%s" '
                     'opacity="%s"/>' % (x0 + span * run / elec, y, wpx, bh, col, op))
            run += val
        if derived:
            for hx in range(int(x0) + 5, int(x1), 9):
                o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" '
                         'stroke-width=".6" opacity=".5"/>' % (hx, y + bh, hx - bh, y, PAPER))
        pct = 100.0 * yes / elec
        t = "yes %s = %.2f%% of the electorate" % (n(yes), pct)
        o.append('<text x="%.1f" y="%.1f" class="mapx" style="fill:%s">%s</text>'
                 % (x0, y + bh + 14, INK, t))
        assert x0 + width(t, "mapx") <= W - 14, t
        verdict = "PASSED" if pct >= 100 * FLOOR else "FAILED"
        vw = width(verdict, "mapt")
        o.append('<text x="%.1f" y="%.1f" class="mapt" style="fill:%s">%s</text>'
                 % (x1 - vw, y + bh + 14, DK if verdict == "PASSED" else OX, verdict))

    lx = 14
    lx = swatch_row(o, lx, LEG_Y, DK, ".88", "yes") + 18
    lx = swatch_row(o, lx, LEG_Y, OX, ".80", "no") + 18
    lx = swatch_row(o, lx, LEG_Y, GREY, ".28", "did not vote (counts as no)") + 18
    o.append('<rect x="%.1f" y="%.1f" width="%d" height="8" fill="none" stroke="%s" '
             'stroke-width=".8" stroke-dasharray="2 2"/>' % (lx, LEG_Y - 8, SWATCH, INK))
    lt = "electorate derived, not counted"
    o.append('<text x="%.1f" y="%.1f" class="mapx" opacity=".9">%s</text>'
             % (lx + SWATCH + 6, LEG_Y, lt))
    assert lx + SWATCH + 6 + width(lt, "mapx") <= W - 12
    assert NOTE_TOP - LEG_Y >= 18, (LEG_Y, NOTE_TOP)

    end = notes(o, nl, NOTE_TOP)
    assert end < H + 13, (end, H)
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
BORN = date(1849, 6, 5)
R1866 = date(1866, 7, 28)
R1915 = date(1915, 6, 5)
ALIGN = date(1936, 1, 1)          # the year its majority matched the Folketing's
SELFKILL = date(1953, 5, 13)
LASTSAT = date(1953, 5, 15)
# The chamber's life runs constitution to constitution - 5 June 1849 to 5 June
# 1953, exactly 104 years. Its LAST SITTING is three weeks earlier, on 15 May,
# and measuring the span to that date gives 103.94 years, which is what the
# assertion below caught on the first run and what the prose had to be checked
# against. Both facts are true and they are not the same fact.
ABOLISHED = date(1953, 6, 5)

REGIMES = [(BORN, R1866, "electors, from men over 40 with an income", DE),
           (R1866, R1915, "Estrup's privileged franchise; 12 of 66 named by the king", OX),
           (R1915, ABOLISHED, "voters over 35; a quarter co-opted by the outgoing chamber", DK)]


def landsting():
    total = (ABOLISHED - BORN).days
    years = total / 365.2425
    assert abs(years - 104) < 0.01, years
    assert (LASTSAT - BORN).days < total, 'last sitting must precede abolition'
    spans = [(b - a).days for a, b, _, _ in REGIMES]
    assert sum(spans) == total, (sum(spans), total)

    # ONE INTERIOR MARKER ONLY. The first raster drew two ticks, and 13 May 1953
    # falls at 99.9 per cent of the span - indistinguishable from the bar's own
    # right edge - so it marked nothing while its label sat hundreds of units away
    # pointing at open paper. A tick that cannot be told from the end of the bar is
    # not a tick. The abolition is carried by the end label instead.
    MARKS = [(ALIGN, "1936: its majority matches the Folketing's")]

    note = ("Days on one axis, every span computed from its two dates. The chamber sat "
            "%s days - %.1f years - and each reform made it more like the Folketing and "
            "less able to say why it was separate. By 1936 its majority matched the lower "
            "house's. On 13 May 1953, at the first reading of the bill abolishing it, it "
            "voted for its own abolition, and it sat for the last time two days later."
            % (n(total), years))
    nl = fold(note, "mapx", 14, W)

    # HEIGHT COMPUTED ONCE, BEFORE ANYTHING IS EMITTED. The first version of this
    # function moved LEG_Y while drawing and then rewrote the viewBox afterwards,
    # which is the item 47 family again: the picture and the number describing it
    # produced by two different passes. The deepest regime caption sets the block.
    x0, x1 = 16, W - 16
    span = x1 - x0
    top, bh = 112, 30
    cap_lines = max(len(fold(lab, "mapx", 0, max(span * d / total, 96)))
                    for (_, _, lab, _), d in zip(REGIMES, spans))
    CAP_TOP = top + bh + 15
    MARK_TOP = CAP_TOP + cap_lines * 12 + 12
    NOTE_TOP = MARK_TOP + (len(MARKS) + 1) * 14 + 10   # +1 for the end label
    H = NOTE_TOP + len(nl) * 13 + 8

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="The Danish Landsting from 1849 to 1953 in three franchise regimes: '
         'indirect election from men over forty, then Estrup\'s privileged franchise with '
         'twelve royal appointees, then voters over thirty-five with a quarter co-opted. '
         'It voted for its own abolition on 13 May 1953.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "THE LANDSTING, 1849 - 1953: WHO CHOSE IT",
           "three franchise regimes on one axis, spans computed from the dates",
           "Each reform answered the objection and removed a reason to exist.")

    run = 0
    for (a, b, lab, col), d in zip(REGIMES, spans):
        bx = x0 + span * run / total
        bw = span * d / total
        o.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" opacity=".85"/>'
                 % (bx, top, bw, bh, col))
        o.append('<text x="%.1f" y="%d" class="mapt" style="fill:%s">%d</text>'
                 % (bx, top - 8, INK, a.year))
        for i, ln in enumerate(fold(lab, "mapx", 0, max(bw, 96))):
            lx = min(bx, W - 14 - width(ln, "mapx"))
            o.append('<text x="%.1f" y="%d" class="mapx" opacity=".85">%s</text>'
                     % (lx, CAP_TOP + i * 12, ln))
            assert lx >= 14, (ln, lx)
        run += d

    o.append('<text x="%.1f" y="%d" class="mapt" text-anchor="end" style="fill:%s">1953'
             '</text>' % (x1, top - 8, INK))

    my = MARK_TOP
    for when, lab in MARKS:
        mx = x0 + span * (when - BORN).days / total
        assert 0.02 < (mx - x0) / span < 0.98, (lab, (mx - x0) / span)
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
                 'stroke-width="1.2"/>' % (mx, top - 4, mx, top + bh + 4, INK))
        # a leader from the tick to its own label, so the label points at something
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width=".7" opacity=".6"/>' % (mx, top + bh + 4, mx, my - 9, INK))
        tw = width(lab, "mapx")
        tx = min(max(mx - tw / 2, 14), W - 14 - tw)
        o.append('<text x="%.1f" y="%d" class="mapx" style="fill:%s">%s</text>'
                 % (tx, my, INK, lab))
        assert tx >= 14 and tx + tw <= W - 14, lab
        my += 14

    # the end of the chamber, carried by the end of the bar
    endlab = "13 May 1953: votes to abolish itself; last sits on the 15th"
    ew = width(endlab, "mapx")
    o.append('<text x="%.1f" y="%d" class="mapx" style="fill:%s">%s</text>'
             % (W - 14 - ew, my, INK, endlab))
    my += 14

    end = notes(o, nl, NOTE_TOP)
    assert end < H + 13, (end, H)
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
EA, A23, A21, IA, CA = 2815100, 840815, 700122, 67888, 1608625


def two_ballots():
    # THE VOTING-AGE TABLE DOES NOT ADD TO ITS OWN TOTAL, and the constitutional
    # one does. 840,815 + 700,122 + 67,888 is 1,608,825 against a published
    # 1,608,625 - an overshoot of exactly 200. The published total is the figure
    # that is internally consistent with the published turnout (57.1 per cent of
    # 2,815,100), so it is the one drawn; the gap is ASSERTED so a later edit
    # cannot make it vanish, and it is PRINTED on the figure rather than averaged
    # away. Item 119, and the same decision chapter 42 took about the railway
    # column.
    gap200 = (A23 + A21 + IA) - CA
    assert gap200 == 200, gap200
    assert abs(100.0 * CA / EA - 57.1) < 0.05, 100.0 * CA / EA
    diff = EA - E53
    assert diff == 229300, diff

    x0 = 14 + width("the voting age", "mapt") + 12
    x1 = W - 16
    big = float(max(EA, E53))
    top, bh, gap = 108, 30, 62

    note = ("Two questions, one Thursday, and two different electorates. The voting-age "
            "ballot was open to %s more people than the constitutional one, because it "
            "was open to those who would be enfranchised if the lower age won. They came, "
            "and twenty-three beat twenty-one %s to %s. On the day Denmark abolished the "
            "chamber of property it declined to admit the twenty-one-year-olds. Note that "
            "the age ballot's own components overshoot its published total by %d votes - "
            "the constitutional ballot's reconcile exactly - and the discrepancy is marked "
            "rather than averaged away."
            % (n(diff), n(A23), n(A21), gap200))
    nl = fold(note, "mapx", 14, W)
    base = top + gap * 2
    NOTE_TOP = base + 46
    H = NOTE_TOP + len(nl) * 13 + 8                     # HEIGHT COMPUTED

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="The two ballots of 28 May 1953. The constitution had an electorate '
         'of 2,585,800; the voting-age question had 2,815,100, a difference of 229,300. '
         'Twenty-three beat twenty-one by 840,815 to 700,122.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "TWO BALLOTS, ONE THURSDAY",
           "28 May 1953: the constitution, and the voting age",
           "The second question was open to the people it was about.")

    ROWS = [("the constitution", E53, C53, "turnout %.1f%%" % (100.0 * C53 / E53)),
            ("the voting age", EA, CA, "turnout %.1f%%" % (100.0 * CA / EA))]
    for k, (lab, elec, cast, sub) in enumerate(ROWS):
        y = top + gap * k
        o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="end" '
                 'style="fill:%s">%s</text>' % (x0 - 8, y + bh - 9, INK, lab))
        ew = (x1 - x0) * elec / big
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="none" '
                 'stroke="%s" stroke-width=".9" opacity=".7"/>' % (x0, y, ew, bh, GREY))
        cw = (x1 - x0) * cast / big
        if k == 0:
            o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="%s" '
                     'opacity=".85"/>' % (x0, y, cw, bh, DK))
        else:
            # THE RESULT, DRAWN. The first raster showed two registers and two
            # turnouts and left the outcome - 23 beating 21 - in the caption only,
            # which is the one thing the row exists to report.
            run = 0.0
            for val, col, op in ((A23, DK, ".85"), (A21, OX, ".80"), (IA, GREY, ".45")):
                o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="%s" '
                         'opacity="%s"/>' % (x0 + (x1 - x0) * run / big,
                                             y, (x1 - x0) * val / big, bh, col, op))
                run += val
        t = "%s on the register, %s voted - %s" % (n(elec), n(cast), sub)
        o.append('<text x="%.1f" y="%.1f" class="mapx" style="fill:%s">%s</text>'
                 % (x0, y + bh + 13, INK, t))
        assert x0 + width(t, "mapx") <= W - 14, t

    # the difference between the two registers
    gx0 = x0 + (x1 - x0) * E53 / big
    gx1 = x0 + (x1 - x0) * EA / big
    gy = top - 12
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
             'stroke-width=".9"/>' % (gx0, gy, gx1, gy, INK))
    for gx in (gx0, gx1):
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width=".9"/>' % (gx, gy - 4, gx, gy + 4, INK))
    gt = "%s more on the register" % n(diff)
    gtw = width(gt, "mapx")
    gtx = min(max((gx0 + gx1) / 2 - gtw / 2, 14), W - 14 - gtw)
    o.append('<text x="%.1f" y="%.1f" class="mapx" style="fill:%s">%s</text>'
             % (gtx, gy - 8, INK, gt))

    lx = 14
    lx = swatch_row(o, lx, base + 4, DK, ".85", "voted; on the age ballot, 23 years") + 18
    lx = swatch_row(o, lx, base + 4, OX, ".80", "21 years") + 18
    lx = swatch_row(o, lx, base + 4, GREY, ".45", "spoiled")
    assert lx <= W - 12, lx

    mark = "age ballot components overshoot its published total by %d" % gap200
    mw = width(mark, "mapx")
    o.append('<text x="%.1f" y="%.1f" class="mapx" style="fill:%s">%s</text>'
             % (14, base + 24, GREY, mark))
    assert 14 + mw <= W - 14, mark

    end = notes(o, nl, NOTE_TOP)
    assert end < H + 13, (end, H)
    o.append('</svg>')
    return "\n  ".join(o)


FIGS = [("svg_gulv_1953.txt", floor_fig),
        ("svg_landsting_1953.txt", landsting),
        ("svg_tobilletter_1953.txt", two_ballots)]

if __name__ == "__main__":
    for name, fn in FIGS:
        svg = fn()
        M.validate(svg, name)
        for bad in (M.check(svg, name) or []):
            print("  !! %s" % (bad,))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
