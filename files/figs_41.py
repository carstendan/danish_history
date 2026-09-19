# -*- coding: utf-8 -*-
"""Figures for chapter 41.

ONE OF THE THREE PLAN_I §13 ASKED FOR IS NOT BUILT, and it was abandoned before
it was attempted rather than after, which is HANDOFF 109's rule working.

  Planned 2 · Danish exports by destination, 1938-1943, from Statistisk Aarbog.
    NOT BUILT. The series needs a trade-by-country table, which in those volumes
    sits far past the point where the fetch truncates, and the container has no
    route to dst.dk at all. What is reachable is two round shares from one
    encyclopaedic source - about a quarter of Danish exports to Germany in 1939,
    about four fifths from 1941 - which is not a series and would have been a
    figure drawn from two numbers by the same hand. The chapter carries those two
    shares in the prose, attributed, and the figure slot goes to the internment
    counts instead, which the chapter needed more and which are itemised in a
    named source.

  NOTE FOR THE VOLUME HUNT (HANDOFF 109). Two dst.dk fetches succeeded this
  session by the pubfile route rather than the pukora one: the election volume
  below, and the census of 5 November 1940, from which table 1 on page 11 came
  back. That is further into a volume than item 109 records as reachable, so the
  unemployment volumes may be worth one more attempt by that route before anybody
  goes to a reading room.

FIGURE 1 · 9 April 1940, hour by hour.
  A schematic on a real time axis: no quantity is drawn that the prose does not
  carry, but the axis is minutes and the two spans are measured on it. Times from
  lex.dk's "9. april 1940" (04.15 at Kruså, Padborg, Rens and Sæd; 05.30 the king
  and the government; 06.00 the capitulation; 08.15 the last firing in
  Haderslev), from tvsyd.dk and dengang.dk for the shooting of the three gendarmes
  at the Padborg viaduct at about four o'clock, from Gjermansen's 1940 letter by
  way of Grænseforeningen for Lundtoftbjerg at about 04.50 and the half hour it
  lasted, and from danmarkshistorien.dk for the BBC's first Danish broadcast at
  18.30 the same evening. EVERY SPAN IS COMPUTED from those clock times: the
  figure prints no duration that is not derived here.

FIGURE 2 · Who was handed over, 22 June 1941 - October 1943.
  Source: lex.dk, "Kommunistinterneringerne under besættelsen, 1941-1945", for the
  195 arrested on 22 June 1941 as 60 in Copenhagen and 135 in the provinces, the
  German list of 72 names, the 116 still interned on 22 August 1941, the roughly
  150 sent to Stutthof in October 1943 and the 22 dead as six in the camp, nine on
  the death marches and seven afterwards. THE FOUR BARS ARE NOT ONE COHORT and the
  figure says so on its face: a single day, a stock on a single date, a flow over
  two years, and a transport. danmarkshistorien.dk's article on the Communist Law
  says about 300 arrested, against lex.dk's 195; that divergence is drawn, as a
  marker, rather than averaged away. The figure of about 600 through the camp
  rests on two popular sources and is drawn open, not filled, for that reason.

FIGURE 3 · 23 March 1943: the whole electorate as one bar.
  Deliberately the same construction as chapter 40's figure 3, because the two
  chapters are arguing with the same denominator: in 1939 the yes vote reached
  44.46 per cent of the electorate and needed 45, and in 1943 the turnout was 89.5.
  Source: Statistiske Meddelelser 4. R. 120. Bd. 1. H., Rigsdagsvalgene i marts og
  april 1943, for the electorate of 2,280,716, the 2,040,583 who voted and the
  29,800 blank and invalid; THE PARTY COUNTS ARE NOT FROM THAT VOLUME, whose OCR
  renders the DNSAP as 48,809 and Dansk Samling as 43,867 and thereby overshoots
  its own total of valid votes by 5,972. They are lex.dk's Folketingsvalget 1943,
  which reconcile with the volume's total to within 28 votes; the 28 are drawn
  into the other-parties segment and the assertion below is what proves the bar
  adds up to the electorate. Every percentage is computed.
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
# larger of the measured and table widths, exactly as figs_39 and figs_40 do.
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
    where a label ought to go: it tries row 0, and if the box hits one that is
    already there it tries the next row.
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


# ------------------------------------------------------------------ figure 1
# Clock times, in minutes from midnight. NOTHING below is a typed duration.
def hm(h, m):
    return h * 60 + m


T_GEND    = hm(4, 0)      # the three gendarmes at the Padborg viaduct, "about four"
T_BORDER  = hm(4, 15)     # Kruså, Padborg, Rens, Sæd; and Langelinie
T_FIGHT   = hm(4, 50)     # Lundtoftbjerg, the first engagement
T_FIGHT_E = T_FIGHT + 30  # "held the road for half an hour"
T_MEET    = hm(5, 30)     # the king, the crown prince and the government
T_TERMS   = hm(6, 0)      # the terms accepted
T_LAST    = hm(8, 15)     # the last firing, Haderslev
T_BBC     = hm(18, 30)    # the BBC's first broadcast in Danish
AX_LO, AX_HI = hm(4, 0), hm(8, 30)

MARKS = [(T_GEND,   "04.00", "three border gendarmes shot at the Padborg viaduct", OX),
         (T_BORDER, "04.15", "the border crossed; landings at Langelinie", INK),
         (T_FIGHT,  "04.50", "Lundtoftbjerg: the first engagement", OX),
         (T_MEET,   "05.30", "the king and the government meet", IND),
         (T_TERMS,  "06.00", "the German terms accepted", IND),
         (T_LAST,   "08.15", "the last firing stops, Haderslev", INK)]


def clock(t):
    return "%02d.%02d" % (t // 60, t % 60)


def plural(n, word):
    return "%d %s%s" % (n, word, "" if n == 1 else "s")


def span(a, b):
    """A duration in words, computed. Used for both brackets and the footnote.

    The plural is computed too. The first raster of this figure read "1 hours 45
    minutes", which validate, overruns and collisions all passed: it is valid
    markup, it fits, and nothing collides. The look-at-it rule caught it.
    """
    h, m = divmod(b - a, 60)
    if h and m:
        return "%s %s" % (plural(h, "hour"), plural(m, "minute"))
    if h:
        return plural(h, "hour")
    return plural(m, "minute")


def morning():
    assert AX_LO <= T_GEND < T_BORDER < T_FIGHT < T_FIGHT_E < T_MEET < T_TERMS < T_LAST <= AX_HI
    decision = T_TERMS - T_BORDER
    whole    = T_LAST - T_GEND
    assert decision < whole

    x0, x1 = 40, W - 26
    ax = lambda t: x0 + (t - AX_LO) / float(AX_HI - AX_LO) * (x1 - x0)
    axis_y = 150

    # The label that is measured must be the label that is drawn, prefix and all:
    # measuring `txt` and then drawing "04.15  " + txt is how the first run of this
    # script pushed the last mark off the right-hand edge.
    labels, gap = stack([(ax(t), "middle", "%s  %s" % (hhmm, txt))
                         for t, hhmm, txt, _ in MARKS], 14, "mapx")
    LAB_TOP = axis_y + 40
    note = ("The fighting lasted %s, from the shooting at the viaduct to the last rounds "
            "in Haderslev. The decision took %s of it, from the crossing of the border to "
            "the government's acceptance of the German terms. Sixteen Danes were killed: "
            "thirteen soldiers and the three gendarmes. At %s the same evening, %s after "
            "the terms were accepted, the BBC broadcast in Danish for the first time, and "
            "Denmark never banned listening to it."
            % (span(T_GEND, T_LAST), span(T_BORDER, T_TERMS), clock(T_BBC),
               span(T_TERMS, T_BBC)))
    note_lines = fold(note, "mapx", 14, W)
    NOTE_TOP = LAB_TOP + gap + 18
    H = NOTE_TOP + len(note_lines) * 13 + 8       # HEIGHT COMPUTED from the folded note

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="The morning of 9 April 1940 on a time axis from four o\'clock to '
         'half past eight. Three border gendarmes were shot at about four, the border was '
         'crossed at a quarter past four, the first engagement was at Lundtoftbjerg at ten '
         'minutes to five, the king and government met at half past five, the German terms '
         'were accepted at six, and the last firing stopped at a quarter past eight.">'
         % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "9 APRIL 1940, HOUR BY HOUR",
           "a time axis in minutes: every span below is measured on it",
           "Times as the sources give them. The first two are “about four” and exact.")

    # the axis, with a tick every half hour
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width=".8"/>'
             % (x0, axis_y, x1, axis_y, GREY))
    t = AX_LO
    while t <= AX_HI:
        major = (t % 60 == 0)
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width=".6"/>'
                 % (ax(t), axis_y, ax(t), axis_y + (7 if major else 4), GREY))
        if major:
            o.append('<text x="%.1f" y="%d" class="mapx" text-anchor="middle" '
                     'opacity=".8">%s</text>' % (ax(t), axis_y + 21, clock(t)))
        t += 30

    # the engagement, which has a duration and is therefore a bar and not a tick
    o.append('<rect x="%.1f" y="%d" width="%.1f" height="10" fill="%s" opacity=".35"/>'
             % (ax(T_FIGHT), axis_y - 10, ax(T_FIGHT_E) - ax(T_FIGHT), OX))

    for t, _, _, col in MARKS:
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.8"/>'
                 % (ax(t), axis_y - 24, ax(t), axis_y, col))

    # the two brackets, drawn above the marks
    for (a, b, txt, y, col) in [
            (T_BORDER, T_TERMS, "the decision: " + span(T_BORDER, T_TERMS), 104, IND),
            (T_GEND, T_LAST, "the fighting: " + span(T_GEND, T_LAST), 82, INK)]:
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width=".9"/>'
                 % (ax(a), y, ax(b), y, col))
        for e in (a, b):
            o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
                     'stroke-width=".9"/>' % (ax(e), y, ax(e), y + 6, col))
        mid = (ax(a) + ax(b)) / 2.0
        tw = width(txt, "mapt")
        left = min(max(mid - tw / 2, 14), W - 14 - tw)
        assert 12 <= left and left + tw <= W - 12, (txt, left, tw)
        o.append('<text x="%.1f" y="%d" class="mapt" style="fill:%s">%s</text>'
                 % (left, y - 6, col, txt))

    for (x, row, txt), (_, _, _, col) in zip(labels, MARKS):
        o.append('<text x="%.1f" y="%d" class="mapx" style="fill:%s">%s</text>'
                 % (x, LAB_TOP + row * 14, col, txt))

    fy = NOTE_TOP
    for ln in note_lines:
        o.append('<text x="14" y="%d" class="mapx" opacity=".85">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H + 13, (fy, H)
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
LIST_NAMES   = 72          # the German list, lex.dk
ARR_CPH      = 60          # 22 June 1941, Copenhagen
ARR_PROV     = 135         # 22 June 1941, the provinces
ARR_OTHER    = 300         # danmarkshistorien.dk's figure, drawn as a divergence
INTERNED_AUG = 116         # still inside on 22 August 1941
THROUGH      = 600         # over the whole period; two popular sources only
STUTTHOF     = 150         # October 1943
DIED_CAMP, DIED_MARCH, DIED_AFTER = 6, 9, 7


def handed():
    arrested = ARR_CPH + ARR_PROV
    assert arrested == 195, arrested
    died = DIED_CAMP + DIED_MARCH + DIED_AFTER
    assert died == 22, died
    assert arrested > LIST_NAMES and THROUGH > arrested and STUTTHOF > died

    # (date, what it counts, total, [(part, colour, opacity)], filled?)
    # The two- and three-part bars are explained by their own caption line, because
    # a colour nobody has been told the meaning of is a decoration. The raster is
    # what showed that: the 60 and the 135 were two tones and no text said which.
    ROWS = [("22 June 1941",
             "arrested by Danish police in one day: %d in Copenhagen, %d in the provinces"
             % (ARR_CPH, ARR_PROV), arrested,
             [(ARR_CPH, DK), (ARR_PROV, IND)], True),
            ("22 Aug 1941", "still interned when the Rigsdag legalised it", INTERNED_AUG,
             [(INTERNED_AUG, DK)], True),
            ("1941 – 1943", "passed through Horserød", THROUGH,
             [(THROUGH, GREY)], False),
            ("Oct 1943", "sent from Horserød to Stutthof", STUTTHOF,
             [(STUTTHOF, OX)], True),
            ("", "of whom died: %d in the camp, %d on the death marches, %d after they "
                 "got home" % (DIED_CAMP, DIED_MARCH, DIED_AFTER), died,
             [(DIED_CAMP, OX), (DIED_MARCH, DE), (DIED_AFTER, GREY)], True)]
    SCALE = max(r[2] for r in ROWS)
    assert SCALE == THROUGH, SCALE

    datew = max(width(r[0], "mapt") for r in ROWS)
    x0 = int(14 + datew + 16)
    x1 = W - 150
    bw = lambda n: (x1 - x0) * n / float(SCALE)

    top, rowh = 100, 34
    H_ROWS = len(ROWS) * rowh
    note = ("Four different kinds of quantity, on one scale and not in one cohort: a single "
            "day, a stock on a single date, a flow over two years and one transport. The "
            "arrests of 22 June 1941 were made on a German list of %d names, without any "
            "Danish law permitting them; the law came two months later and was retroactive. "
            "danmarkshistorien.dk gives about %d arrested rather than %d, marked above; "
            "the reading here is that %d is the day and %d is the following weeks. The "
            "Horserød total is drawn open because it rests on two popular sources. The "
            "%d dead are %d in the camp, %d on the death marches and %d of what the camp "
            "had done to them, after they got home."
            % (LIST_NAMES, ARR_OTHER, arrested, arrested, ARR_OTHER,
               died, DIED_CAMP, DIED_MARCH, DIED_AFTER))
    note_lines = fold(note, "mapx", 14, W)
    NOTE_TOP = top + H_ROWS + 26
    H = NOTE_TOP + len(note_lines) * 13 + 8       # HEIGHT COMPUTED from the folded note

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Danish communists arrested and interned between June 1941 and October '
         '1943. One hundred and ninety-five were arrested by Danish police on 22 June 1941 '
         'on a German list of seventy-two names; one hundred and sixteen were still '
         'interned when the Communist Law was passed on 22 August; about six hundred passed '
         'through the camp at Horserød; about one hundred and fifty were sent to '
         'Stutthof in October 1943; twenty-two died.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "WHO WAS HANDED OVER, 1941 – 1943",
           "Danes arrested by Danish police for a foreign government",
           "Counts, not shares. The four bars are not one cohort — see the note below.")

    y = top
    for date, what, total, parts, filled in ROWS:
        if date:
            o.append('<text x="14" y="%d" class="mapt">%s</text>' % (y + 15, date))
        cx = x0
        for n, col in parts:
            if filled:
                o.append('<rect x="%.1f" y="%d" width="%.1f" height="18" fill="%s" '
                         'opacity=".85"/>' % (cx, y, bw(n), col))
            else:
                o.append('<rect x="%.1f" y="%d" width="%.1f" height="18" fill="none" '
                         'stroke="%s" stroke-width=".9" opacity=".7"/>'
                         % (cx, y, bw(n), col))
            cx += bw(n)
        o.append('<text x="%.1f" y="%d" class="mapt">%s</text>' % (cx + 8, y + 14, total))
        o.append('<text x="%d" y="%d" class="mapx" opacity=".8">%s</text>'
                 % (x0, y + 30, what))
        y += rowh

    # the divergence, marked on the bar it disagrees with and not averaged into it
    dx = x0 + bw(ARR_OTHER)
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.2" '
             'stroke-dasharray="3 3"/>' % (dx, top - 6, dx, top + 22, INK))
    dtxt = "danmarkshistorien: about %d" % ARR_OTHER
    dw = width(dtxt, "mapx")
    dleft = min(dx + 6, W - 14 - dw)
    assert dleft + dw <= W - 12, (dleft, dw)
    o.append('<text x="%.1f" y="%d" class="mapx" opacity=".85">%s</text>'
             % (dleft, top - 10, dtxt))

    fy = NOTE_TOP
    for ln in note_lines:
        o.append('<text x="14" y="%d" class="mapx" opacity=".85">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H + 13, (fy, H)
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
ELECTORATE = 2280716
CAST       = 2040583
VALID      = 2010783
SPOILT     = CAST - VALID
SOC, KONS, VEN, RAD = 894632, 421523, 376850, 175179
DANSK_SAMLING, DNSAP, RETS, BONDE = 43367, 43309, 31323, 24572
DNSAP_1939 = 31032         # chapter 40's figure


def electorate():
    four = SOC + KONS + VEN + RAD
    named = four + DANSK_SAMLING + DNSAP + RETS + BONDE
    rest_valid = VALID - four - DANSK_SAMLING - DNSAP        # Retsforbundet, Bondepartiet
    stayed = ELECTORATE - CAST                               # and the residue of 28
    # (votes, colour, name, opacity). The three grey segments are three DIFFERENT
    # opacities: at one opacity the bar showed four blocks and the legend named six.
    segs = [(four, DK, "the four cooperating parties", ".85"),
            (DANSK_SAMLING, IND, "Dansk Samling", ".85"),
            (DNSAP, OX, "DNSAP", ".85"),
            (rest_valid, GREY, "other parties", ".55"),
            (SPOILT, GREY, "blank and invalid", ".34"),
            (stayed, GREY, "did not vote", ".16")]
    # THE BAR MUST BE THE ELECTORATE. This is the assertion that proves it, and it
    # is also what catches the 28 votes by which the party counts and the volume's
    # total of valid votes disagree: they are inside rest_valid.
    assert sum(n for n, _, _, _ in segs) == ELECTORATE, sum(n for n, _, _, _ in segs)
    assert VALID - named == 28, VALID - named
    assert rest_valid == RETS + BONDE + 28, rest_valid

    pc = lambda n: 100.0 * n / ELECTORATE
    turnout = pc(CAST)
    four_of_valid = 100.0 * four / VALID
    dnsap_of_valid = 100.0 * DNSAP / VALID
    dnsap_growth = 100.0 * (DNSAP - DNSAP_1939) / DNSAP_1939
    gap = DANSK_SAMLING - DNSAP
    assert 89.0 < turnout < 90.0 and 0 < gap < 100 and dnsap_growth > 0

    x0, x1 = 14, W - 14
    bar_y, bar_h = 118, 54
    px = lambda n: x0 + n / float(ELECTORATE) * (x1 - x0)

    # in-bar labels only where the segment is measurably wide enough; the rest
    # are placed below by search, never by reasoning about them (item 76). Each
    # one below carries a swatch in its own segment's colour and opacity, because
    # the first raster showed six names under a bar with four visible blocks:
    # three of the six segments were the same grey at the same opacity.
    below_src, below_col, cx = [], [], x0
    inbar = []
    for n, col, name, op in segs:
        w = px(n) - x0
        t = "%s %.1f%%" % (name.upper(), pc(n))
        if w >= width(t, "mapt") + 14:
            inbar.append((cx + 6, t, PAPER if col == DK else INK))
        else:
            below_src.append((cx + w / 2.0, "middle", "%s %s (%.1f%%)"
                              % (name, format(n, ","), pc(n))))
            below_col.append((col, op))
        cx += w
    below, gap_h = stack(below_src, 15, "mapx", left=12 + SWATCH + 6)

    LAB_TOP = bar_y + bar_h + 26
    note = ("Turnout %.2f per cent of the electorate, the highest at any Danish general election. The "
            "four cooperating parties took %.2f per cent of the valid votes. The Danish "
            "Nazi party took %.2f per cent of them and the same three seats it had won in "
            "1939 — on a vote that had risen from %s to %s, by %.1f per cent, in the "
            "years a German army stood in the country. What held it to three seats was that "
            "everyone else came out. Dansk Samling, founded against the occupation, "
            "finished %d votes ahead of it. The German minority's party, which had held a "
            "seat since 1920, did not stand."
            % (turnout, four_of_valid, dnsap_of_valid, format(DNSAP_1939, ","),
               format(DNSAP, ","), dnsap_growth, gap))
    note_lines = fold(note, "mapx", 14, W)
    NOTE_TOP = LAB_TOP + gap_h + 14
    H = NOTE_TOP + len(note_lines) * 13 + 8       # HEIGHT COMPUTED from the folded note

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="The Danish general election of 23 March 1943 drawn as shares of the '
         'whole electorate of 2,280,716. The four cooperating parties took 81.9 per cent of '
         'the electorate, Dansk Samling and the Danish Nazi party 1.9 per cent each, and '
         '10.5 per cent did not vote. Turnout was 89.5 per cent, the highest in Danish '
         'history.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "23 MARCH 1943: THE WHOLE ELECTORATE AS ONE BAR",
           "the same denominator chapter 40 used for the referendum of 1939",
           "In 1939 the yes vote reached 44.46 per cent of this bar and needed 45.")

    cx = x0
    for n, col, _, op in segs:
        w = px(n) - x0
        o.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" opacity="%s"/>'
                 % (cx, bar_y, w, bar_h, col, op))
        cx += w
        if cx < x1 - 0.5:
            o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
                     'stroke-width=".8"/>' % (cx, bar_y, cx, bar_y + bar_h, PAPER))
    o.append('<rect x="%d" y="%d" width="%.1f" height="%d" fill="none" stroke="%s" '
             'stroke-width=".8" opacity=".55"/>' % (x0, bar_y, x1 - x0, bar_h, GREY))

    for lx, t, col in inbar:
        assert lx + width(t, "mapt") <= W - 12, (t, lx)
        o.append('<text x="%.1f" y="%d" class="mapt" style="fill:%s">%s</text>'
                 % (lx, bar_y + bar_h // 2 + 5, col, t))
    for (lx, row, t), (col, op) in zip(below, below_col):
        y = LAB_TOP + row * 15
        o.append('<rect x="%.1f" y="%d" width="%d" height="8" fill="%s" opacity="%s"/>'
                 % (lx - SWATCH - 6, y - 8, SWATCH, col, op))
        o.append('<text x="%.1f" y="%d" class="mapx" opacity=".9">%s</text>' % (lx, y, t))

    fy = NOTE_TOP
    for ln in note_lines:
        o.append('<text x="14" y="%d" class="mapx" opacity=".85">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H + 13, (fy, H)
    o.append('</svg>')
    return "\n  ".join(o)


FIGS = [("svg_morgen_1940.txt", morning),
        ("svg_udleveret_1941.txt", handed),
        ("svg_valg_1943.txt", electorate)]

if __name__ == "__main__":
    for name, fn in FIGS:
        svg = fn()
        M.validate(svg, name)
        for bad in (M.check(svg, name) or []):
            print("  !! %s" % (bad,))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
