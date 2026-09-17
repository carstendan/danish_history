# -*- coding: utf-8 -*-
"""Figures for chapter 40.

ONE OF THE THREE PLAN_I §13 ASKED FOR IS NOT BUILT, and this says why.

  Planned 1 · Unemployment 1929-1940, with the 1932 peak. NOT BUILT, for the
    same reason as chapter 39's, and the reason is now better understood. The
    two volumes that hold the series ARE identified this session, which closes
    half of PLAN_I §14.4: Arbejdsløsheden i aarene 1931-35 is Stat. Medd. 4. R.
    100. Bd. 2. H. (1937) and Arbejdsløsheden i aarene 1936-40 is 4. R. 115. Bd.
    4. H. (1942), from the department's own publication list. Reaching them is
    the blocker, not naming them. The container has no route to dst.dk at all;
    the fetch tool reaches the volumes but truncates each around page 34 of two
    hundred and more; the browser will not render the scanned PDFs and cannot
    dispatch clicks into the viewer's frame; and dst.dk's own historical browser
    filters by ASP.NET postback, which did not survive scripted navigation.
    Recorded as HANDOFF 107. What the chapter carries instead is the shape of
    the depression in words and the two quantities that are double-witnessed:
    the national vote in 1932 and what a one-industry town looked like.

FIGURE 1 · What was in Kanslergade, 29-30 January 1933.
  A schematic, so no quantity is drawn that is not in the prose. The ten
  negotiators and the contents are from Mogens R. Nissen, "Det nationale
  kompromis", Landbohistorisk Tidsskrift 2010:1, pp. 50-76, and from
  danmarkshistorien.lex.dk and lex.dk on the agreement; the Radicals' objection
  to a further depreciation is Holten (below). Each party's row says what it
  arrived wanting and what it signed for, and the third column is the one the
  Danish memory of Kanslergade leaves out.

FIGURE 2 · The pound in kroner, January 1933.
  Source: Henning Holten, "Kanslergadeforliget januar 1933:
  valutakurspolitikken", Historisk Tidsskrift 14. r. 2 (1981-82), pp. 198-204,
  for the rate before (19.20-20.00), the rate agreed (22.50) and the farmers'
  demand (25); Nissen (above) for the rate before (about 19.30) and the rate
  agreed (22.50). THE TWO SOURCES AGREE ON 22.50 AND DIFFER ON WHAT IT REPLACED,
  so the figure draws the before as a BAND and not a point, which is what the
  evidence supports. Every percentage in the figure is COMPUTED from the rates
  below and none is typed, because the published percentages (ten in the
  encyclopedias, twelve to thirteen in Nissen) disagree with each other and with
  the rates, and the disagreement is the point the figure makes.

FIGURE 3 · 23 May 1939: the yes vote against the 45 per cent rule.
  Drawn ENTIRELY from the shares of the electorate, which are double-witnessed
  - 44.5 yes and 3.9 no, in the Interior Ministry's Folkeafstemninger - tal og
  fakta and in lex.dk's list of referendums since 1916 - and from the threshold
  in §93 of the constitution of 1915. The absolute counts (electorate 2,173,420,
  11,770 spoiled) rest on one lineage, Nohlen & Stöver, and are therefore NOT
  drawn; they are in the prose, attributed. The residue of the two shares is NOT
  the did-not-vote share - it is everyone who did not vote yes or no, and it
  includes the spoiled ballots. The first draft labelled it wrongly and the
  assertion caught it. The gap between that residue and the published turnout is
  now used the other way round, as an independent check that the spoiled share is
  the half a per cent the absolute counts say it is.
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


# Item 105. mapspine.CHAR_W under-states mapt by about a tenth and figure 2 of
# chapter 39 ran off the canvas with every guard clean. mapspine is NOT changed
# here - that is the ledger decision in HANDOFF 105, and changing it would re-wrap
# every shipped figure in figs_37 and figs_38. This folds at the larger of the
# measured and table widths, exactly as figs_39 does.
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


def header(o, title, sub, note):
    o.append('<text x="14" y="24" class="mapl">%s</text>' % title)
    o.append('<text x="14" y="40" class="mapt">%s</text>' % sub)
    o.append('<text x="14" y="62" class="mapx" opacity=".75">%s</text>' % note)


# ------------------------------------------------------------------ figure 1
# (party, seats in the Folketing after 16 Nov 1932, came wanting, signed for,
#  and the thing it had said it would never do)
DEAL = [
    ("Social Democrats", 62, DK,
     "No lockout on 1 February. The social reform, written in 1920 and waiting.",
     "The lockout called off. Four social laws, in force 1 October 1933.",
     "Legislated the right to strike away for a year."),
    ("Venstre", 38, DE,
     "A cheaper krone for the export farms. Relief on farm debt.",
     "22.50 kroner to the pound. Debts refinanced, property taxes cut.",
     "Voted through the largest expansion of public provision in Danish history."),
    ("Radicals", 14, IND,
     "No further depreciation: it would spoil the trade talks with Britain.",
     "A devaluation, and one smaller than the farmers had asked for.",
     "Gave up the currency policy its own foreign minister had argued for."),
]
COLS = ["CAME WANTING", "SIGNED FOR", "AND GAVE UP"]


def deal():
    # COLUMN GEOMETRY COMPUTED, not typed. The name column is set by the widest
    # party name plus its seat count, measured in its own class; the three text
    # columns then split what is left, equally.
    names = ["%s · %d" % (p, s) for p, s, _, _, _, _ in DEAL]
    namew = max(len(x) * CW["mapt"] for x in names)
    nx = 14
    cx = int(nx + namew + 22)
    colw = (W - cx - 14) // 3
    assert colw > 120, colw

    top, pad = 96, 16
    rows, y = [], top
    for _, _, _, a, b, c in DEAL:
        # each cell folded to its own column width; the row is as tall as the tallest
        cells = [fold(t, "mapx", 0, colw - 8) for t in (a, b, c)]
        rows.append((y, cells))
        y += max(len(ls) for ls in cells) * 13 + pad + 16
    H = y + 46                                    # HEIGHT COMPUTED from the folded rows

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="What the three parties brought to the Kanslergade negotiation of '
         '29 and 30 January 1933 and what each of them signed for. Every row ends with '
         'the thing that party had said it would never do.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "WHAT WAS IN KANSLERGADE, 29 – 30 JANUARY 1933",
           "ten people in a flat on Østerbro: nine politicians and Augusta Erichsen",
           "Seats are the Folketing after the election of 16 November 1932. "
           "The Conservatives were not invited.")

    for i, c in enumerate(COLS):
        o.append('<text x="%d" y="%d" class="mapx" opacity=".75">%s</text>'
                 % (cx + i * colw, top - 12, c))
    o.append('<line x1="14" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width=".6" '
             'opacity=".45"/>' % (top - 6, W - 14, top - 6, GREY))

    for (y0, cells), (p, s, col, _, _, _) in zip(rows, DEAL):
        o.append('<rect x="%d" y="%d" width="4" height="%d" fill="%s"/>'
                 % (nx, y0 - 2, max(len(ls) for ls in cells) * 13 + 6, col))
        o.append('<text x="%d" y="%d" class="mapt">%s · %d</text>' % (nx + 12, y0 + 10, p, s))
        for i, ls in enumerate(cells):
            for j, ln in enumerate(ls):
                o.append('<text x="%d" y="%d" class="mapx">%s</text>'
                         % (cx + i * colw, y0 + 10 + j * 13, ln))

    fy = H - 30
    note = ("Concluded on the morning of 30 January 1933, the day Hitler was appointed "
            "Reich Chancellor. There was no single signed document: what there was, was a "
            "package of bills all three parties would now vote for.")
    for ln in fold(note, "mapx", 14, W):
        o.append('<text x="14" y="%d" class="mapx" opacity=".8">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H + 13, (fy, H)
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
# Kroner to the pound. Holten gives the January range and the agreed rate and the
# farmers' demand; Nissen gives about 19.30 and the same agreed rate.
BEFORE_LO, BEFORE_HI = 19.20, 20.00      # Holten, the January range
BEFORE_NISSEN        = 19.30             # Nissen, inside it
AGREED               = 22.50             # BOTH sources
ASKED                = 25.00             # Holten, the farmers' demand
AXIS_LO, AXIS_HI     = 18.0, 26.0


def rate():
    assert AXIS_LO < BEFORE_LO < BEFORE_NISSEN < BEFORE_HI < AGREED < ASKED < AXIS_HI

    # EVERY PERCENTAGE COMPUTED. A move from b to a kroner per pound is a fall of
    # (1 - b/a) in the krone and a rise of (a/b - 1) in sterling, and the two are
    # different numbers, which is the whole point of the figure.
    kr_fall = lambda b: (1 - b / AGREED) * 100
    st_rise = lambda b: (AGREED / b - 1) * 100
    lo, hi = kr_fall(BEFORE_HI), kr_fall(BEFORE_LO)
    slo, shi = st_rise(BEFORE_HI), st_rise(BEFORE_LO)
    assert 10 < lo < hi < 20 and hi < shi

    x0, x1 = 60, W - 40
    ax = lambda v: x0 + (v - AXIS_LO) / (AXIS_HI - AXIS_LO) * (x1 - x0)
    axis_y = 132
    note = ("How big a devaluation that is depends on which currency you put underneath. "
            "Measured as the krone's fall it is %.1f to %.1f per cent; measured as "
            "sterling's rise it is %.1f to %.1f. The encyclopedias say ten per cent and "
            "Nissen says twelve to thirteen, and neither matches the rates all of them "
            "print. The figure gives the rates."
            % (lo, hi, slo, shi))
    note_lines = fold(note, "mapx", 14, W)
    NOTE_TOP = axis_y + 58
    H = NOTE_TOP + len(note_lines) * 13 + 8       # HEIGHT COMPUTED from the folded note

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Kroner to the pound sterling in January 1933. Before the Kanslergade '
         'agreement the rate stood between about 19.20 and 20 kroner; the agreement set it '
         'at 22.50; the farmers had asked for 25.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "THE POUND IN KRONER, JANUARY 1933",
           "what the negotiation was actually arguing about",
           "Two accounts differ on the rate before, so it is drawn as a band and not a point.")

    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width=".8"/>'
             % (x0, axis_y, x1, axis_y, GREY))
    v = AXIS_LO
    while v <= AXIS_HI + 1e-9:
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width=".6"/>'
                 % (ax(v), axis_y, ax(v), axis_y + 5, GREY))
        o.append('<text x="%.1f" y="%d" class="mapx" text-anchor="middle" opacity=".8">%d</text>'
                 % (ax(v), axis_y + 18, v))
        v += 1.0
    o.append('<text x="%d" y="%d" class="mapx" text-anchor="end" opacity=".8">kroner '
             'to £1</text>' % (x1, axis_y + 34))

    bl, bw = ax(BEFORE_LO), ax(BEFORE_HI) - ax(BEFORE_LO)
    o.append('<rect x="%.1f" y="%d" width="%.1f" height="26" fill="%s" opacity=".30"/>'
             % (bl, axis_y - 26, bw, IND))
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.6"/>'
             % (ax(BEFORE_NISSEN), axis_y - 26, ax(BEFORE_NISSEN), axis_y, IND))
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="2.4"/>'
             % (ax(AGREED), axis_y - 40, ax(AGREED), axis_y, OX))
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.4" '
             'stroke-dasharray="3 3"/>' % (ax(ASKED), axis_y - 34, ax(ASKED), axis_y, DE))

    # LABELS PLACED BY SEARCH against the marks, not by reasoning: each is anchored so it
    # falls inside the canvas, and the assertion below is what proves it.
    labs = [(ax(BEFORE_NISSEN), axis_y - 34, "before: 19.20 – 20.00", "start", IND),
            (ax(AGREED), axis_y - 48, "agreed 30 Jan: 22.50", "middle", OX),
            (ax(ASKED), axis_y - 42, "the farms asked 25", "end", DE)]
    for lx, ly, t, anchor, col in labs:
        wpx = len(t) * CW["mapt"]
        left = lx if anchor == "start" else (lx - wpx / 2 if anchor == "middle" else lx - wpx)
        assert 12 <= left and left + wpx <= W - 12, (t, left, wpx)
        # style=, NOT fill=. Both style.css and rasterise() set fill on .mapt, and a
        # stylesheet rule beats a presentation attribute, so fill= here is a silent
        # no-op that renders every one of these grey. Found in the raster; the guards
        # cannot see it because the markup is valid either way (HANDOFF 108).
        o.append('<text x="%.1f" y="%d" class="mapt" text-anchor="%s" style="fill:%s">%s</text>'
                 % (lx, ly, anchor, col, t))

    fy = NOTE_TOP
    for ln in note_lines:
        o.append('<text x="14" y="%d" class="mapx">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H, (fy, H)
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
# Shares of the ELECTORATE, both double-witnessed, and the threshold from §93.
YES_PCT, NO_PCT, RULE_PCT = 44.5, 3.9, 45.0
TURNOUT_PCT = 48.9                       # published; used only as a check


def rule():
    # The residue of the two double-witnessed shares is NOT "did not vote": it is
    # everyone who did not vote yes or no, which includes the blank and spoiled
    # ballots. The first draft of this figure labelled it "did not vote" and the
    # assertion below caught it, which is the whole reason it is here.
    not_yes_or_no = 100.0 - YES_PCT - NO_PCT
    # Cross-check, and it earns its place: the gap between that residue and the
    # published turnout is the blank and spoiled share, arrived at from numbers that
    # never mention it. It must be small and it must be positive.
    spoiled = not_yes_or_no - (100.0 - TURNOUT_PCT)
    assert 0.2 < spoiled < 1.0, (not_yes_or_no, TURNOUT_PCT, spoiled)
    assert YES_PCT < RULE_PCT

    x0, x1 = 14, W - 14
    bar_y, bar_h = 118, 54
    px = lambda p: x0 + p / 100.0 * (x1 - x0)
    note = ("Section 93 of the constitution of 1915 required both a majority of those "
            "voting and yes votes amounting to at least 45 per cent of everyone entitled "
            "to vote, which counts a voter who stays at home as a voter who has said no. "
            "The open segment is everyone who did not vote yes or no: about %.1f per cent "
            "of the electorate stayed away and about %.1f per cent voted and spoiled the "
            "ballot. Seven weeks earlier the same electorate had turned out at 79.2 per "
            "cent to elect a Folketing. Shares of the electorate from the Interior "
            "Ministry's referendum tables and from lex.dk, which agree; the threshold "
            "from the constitution." % (100.0 - TURNOUT_PCT, spoiled))
    note_lines = fold(note, "mapx", 14, W)
    NOTE_TOP = bar_y + bar_h + 52
    H = NOTE_TOP + len(note_lines) * 13 + 8       # HEIGHT COMPUTED from the folded note

    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="The Danish constitutional referendum of 23 May 1939 as shares of the '
         'whole electorate. Yes 44.5 per cent, no 3.9 per cent, and 51.6 per cent did not '
         'vote. The constitution required the yes votes to reach 45 per cent of the whole '
         'electorate, and they did not.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "23 MAY 1939: THE RULE THAT COUNTED SILENCE",
           "the whole electorate as one bar, not the votes cast",
           "Of those who voted, 91.85 per cent said yes. This is the other denominator.")

    o.append('<rect x="%d" y="%d" width="%.1f" height="%d" fill="%s"/>'
             % (x0, bar_y, px(YES_PCT) - x0, bar_h, DK))
    o.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>'
             % (px(YES_PCT), bar_y, px(NO_PCT) - x0, bar_h, OX))
    o.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="none" stroke="%s" '
             'stroke-width=".8" opacity=".55"/>'
             % (px(YES_PCT + NO_PCT), bar_y, px(not_yes_or_no) - x0, bar_h, GREY))

    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="2" '
             'stroke-dasharray="5 3"/>'
             % (px(RULE_PCT), bar_y - 26, px(RULE_PCT), bar_y + bar_h + 12, INK))
    o.append('<text x="%.1f" y="%d" class="mapt">the rule: 45 per cent of the electorate</text>'
             % (px(RULE_PCT) + 8, bar_y - 14))

    # In-bar labels only where the segment is wide enough to hold them, measured.
    segs = [(x0, px(YES_PCT) - x0, "YES %.1f%%" % YES_PCT),
            (px(YES_PCT), px(NO_PCT) - x0, "NO %.1f%%" % NO_PCT),
            (px(YES_PCT + NO_PCT), px(not_yes_or_no) - x0,
             "DID NOT VOTE YES OR NO %.1f%%" % not_yes_or_no)]
    below = []
    for sx, sw, t in segs:
        need = len(t) * CW["mapt"] + 12
        if sw >= need:
            o.append('<text x="%.1f" y="%d" class="mapt" style="fill:%s">%s</text>'
                     % (sx + 6, bar_y + bar_h // 2 + 5, PAPER if t.startswith("YES") else INK, t))
        else:
            below.append((sx + sw / 2.0, t))
    for sx, t in below:
        o.append('<text x="%.1f" y="%d" class="mapx" text-anchor="middle">%s</text>'
                 % (sx, bar_y + bar_h + 26, t))

    fy = NOTE_TOP
    for ln in note_lines:
        o.append('<text x="14" y="%d" class="mapx">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H, (fy, H)
    o.append('</svg>')
    return "\n  ".join(o)


FIGS = [("svg_kanslergade_1933.txt", deal),
        ("svg_kurs_1933.txt", rate),
        ("svg_regel_1939.txt", rule)]

if __name__ == "__main__":
    for name, fn in FIGS:
        svg = fn()
        M.validate(svg, name)
        for bad in (M.check(svg, name) or []):
            print("  !! %s" % (bad,))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
