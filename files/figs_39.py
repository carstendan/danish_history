# -*- coding: utf-8 -*-
"""Figures for chapter 39.

NONE OF THESE IS THE FIGURE PLAN_I §13 ASKED FOR, and each says why here.

  Planned 1 · Unemployment 1910-1930, annual. NOT BUILT. The four five-year
    volumes are identified - Stat. Medd. 4. R. 48. Bd. 5. H., 61. Bd. 4. H.,
    74. Bd. 2. H. and 88. Bd. 4. H. - and confirmed three times, in the 1954
    volume's own list, in the list of a later volume and in the department's
    publication register in Statistisk Aarbog 1936. The tables themselves could
    not be reached: the fetch tool refuses a constructed URL and no search
    surfaced the volumes. Item 73's gap, recorded as item 104. What the chapter
    carries instead is the one sentence the department did publish in reach:
    1954's 8.0 per cent was the lowest since 1920.

  Planned 2 · Social Democratic seats 1884-1924. NOT BUILT. Every copy of the
    series found descends from one lineage (Mackie & Rose; Nohlen & Stöver),
    which is one witness under item 88's rule, and item 80 already showed the
    department's own nineteenth-century volumes carry no party column. The 1924
    end of it is primary and is figure 3.

  Planned 3 · Landmandsbanken, what the state guaranteed and what it lost.
    NOT BUILT AS PLANNED. The split of the September capital between the state,
    ØK, the National Bank and Great Northern rests on one account, and the
    total losses (500-600 million) on one account. Redrawn as figure 2, a
    calendar whose every date appears twice and whose only quantities, 30 and
    about 70 million, appear twice.

FIGURE 1 · Stamps as small change, Sønderjylland 1921-22.
  Source: J. Sømod, "Sønderjylland umiddelbart efter 1920", Skilling 1995 (rev.
  1999). ONE SOURCE, and the figure carries it only because the source gives
  every count twice over: as piece counts and as face-value totals, and the two
  reconcile to the øre. That is asserted below, and if a digit were wrong the
  assertion would fail. The four towns are the source's own table.

FIGURE 2 · Landmandsbanken, two rescues and a guarantee, 1922-23.
  Dates, each in two of: danmarkshistorien.lex.dk (Sørensen); Gyldendal og
  Politikens Danmarkshistorie (Christiansen); da.wikipedia; lex.dk; Dansk
  Biografisk Leksikon; skibsrederen.dk. 30 million: Christiansen and L.
  Christensen (1928). About 70 million: the same two.

FIGURE 3 · The Folketing of 11 April 1924, seat by seat.
  Source: Stat. Medd. 4. R. 71. Bd. 1. H., pp. 17-18. The by-party table sums to
  148, and the re-elected/newly-elected table sums to 148 again, party by party;
  the Faroese member, returned unopposed, is from the same volume. A cell grid,
  so item 70 applies: the cell counts are asserted against the seat counts, and
  the government's base is asserted to fill exactly the first three rows.
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


# MEASURED in this session by rendering 100 characters of each class through the
# same CSS rasterise() injects: mapt 6.36, mapx 5.32, mapl 6.61 units a character.
# mapspine.CHAR_W has mapt at 5.68, which cannot be right on any machine - mapt is
# 9.5px against mapx's 8.5px with the same letter-spacing, so it must be about a
# ninth wider - and figure 2's first draft ran off the canvas with every guard
# clean. mapspine is NOT changed here, because every fold() in figs_37 and figs_38
# would re-wrap and their figures would stop regenerating byte-identical; that is a
# ledger decision (HANDOFF 105). This script folds at the larger of the two.
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


def n(v):
    return "{:,}".format(v)


# ------------------------------------------------------------------ figure 1
ISSUED   = {"10": 474234, "25": 467583}
RETURNED = {"10": 340129, "25": 358452}
VALUE_ISSUED, VALUE_RETURNED = 16431915, 12362590          # in øre, as printed
TOWNS = [("Haderslev", 52694, 49686), ("Sønderborg", 35100, 40898),
         ("Aabenraa", 31900, 38204), ("Tønder", 31700, 37480)]


def kapsler():
    # The source prints both counts and both totals. They must agree.
    assert sum(int(k) * v for k, v in ISSUED.items()) == VALUE_ISSUED
    assert sum(int(k) * v for k, v in RETURNED.items()) == VALUE_RETURNED
    total = sum(ISSUED.values())
    towns = [(t, a + b) for t, a, b in TOWNS]
    rest = total - sum(v for _, v in towns)
    assert rest > 0
    kept = {k: ISSUED[k] - RETURNED[k] for k in ISSUED}
    share_kept = sum(kept.values()) / float(total)

    # BAR ORIGIN COMPUTED from the widest left-hand label. It was typed as 130 and
    # "25 øre · Christian 10." ran under its own bar, which no guard can see because
    # collisions() is text against text (item 47). Found in the raster.
    LABELS = ["10 øre · Kronborg", "25 øre · Christian 10."]
    widest = max(max(len(x) * CW["mapt"] for x in LABELS),
                 max(len(t) * CW["mapx"] for t, _, _ in TOWNS))
    bx = int(14 + widest + 24)                    # a 24-unit gutter; 14 rendered flush
    bw = W - bx - 20
    scale = bw / float(max(ISSUED.values()))
    top, bar, gap = 104, 18, 46
    # The town bars carry their count at the right-hand end, so the scale leaves room for
    # the widest label, measured, plus the six-unit gap before it.
    lab = max(len(n(v)) for _, v in towns) * CW["mapx"] + 6
    tscale = (bw - lab) / float(max(v for _, v in towns))
    t0 = top + 2 * gap + 44
    H = t0 + len(towns) * 30 + 70                # HEIGHT COMPUTED from the rows
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Postage stamps sealed in iron and celluloid capsules and used as '
         'small change in Soenderjylland in 1921 and 1922. %s ten-oere and %s twenty-five-oere '
         'pieces were issued; about a quarter of them were never handed back. Haderslev '
         'received the most of the four market towns.">' % (W, H, n(ISSUED["10"]), n(ISSUED["25"]))]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "SMALL CHANGE IN A CAPSULE, 1921 – 1922",
           "a stamp under celluloid, passed from hand to hand in the new province",
           "Solid: handed back when called in. Open: never came back.")
    for i, (k, title) in enumerate(zip(("10", "25"), LABELS)):
        y = top + i * gap
        wi, wr = ISSUED[k] * scale, RETURNED[k] * scale
        assert 0 < wr < wi <= bw + 0.01
        o.append('<text x="14" y="%d" class="mapt">%s</text>' % (y + 13, title))
        o.append('<rect x="%d" y="%d" width="%.1f" height="%d" fill="none" stroke="%s" '
                 'stroke-width="1"/>' % (bx, y, wi, bar, DE))
        o.append('<rect x="%d" y="%d" width="%.1f" height="%d" fill="%s"/>' % (bx, y, wr, bar, DE))
        o.append('<text x="%d" y="%d" class="mapx">%s issued · %s back · %s kept</text>'
                 % (bx, y + bar + 12, n(ISSUED[k]), n(RETURNED[k]), n(kept[k])))
    o.append('<text x="14" y="%d" class="mapt">Where they went: the four market towns, both '
             'values</text>' % (t0 - 16))
    for i, (t, v) in enumerate(towns):
        y = t0 + i * 30
        o.append('<text x="14" y="%d" class="mapx">%s</text>' % (y + 11, t))
        o.append('<rect x="%d" y="%d" width="%.1f" height="14" fill="%s"/>' % (bx, y, v * tscale, DK))
        o.append('<text x="%.1f" y="%d" class="mapx">%s</text>' % (bx + v * tscale + 6, y + 11, n(v)))
    fy = t0 + len(towns) * 30 + 14
    note = ("The other %s went out through the province's other post offices. Face value "
            "issued %s kroner, returned %s: the source's counts and totals agree to the øre. "
            "About %d per cent were never handed back."
            % (n(rest), "164,319.15", "123,625.90", round(share_kept * 100)))
    for ln in fold(note, "mapx", 14, W):
        o.append('<text x="14" y="%d" class="mapx">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
KRAK = [
    ("May–Jul 1922", "Holmer Green, the state's first bank inspector, goes through "
                     "the bank's books in secret.", "state"),
    ("9 Jul", "RESCUE ONE — 30 million of extra reserve from the National Bank, and a "
              "statement that follows the bank's own figures.", "bank"),
    ("17 Sep", "RESCUE TWO — the bank is reconstructed with about 70 million kroner of "
               "new share capital.", "bank"),
    ("19 Sep", "The Rigsdag, recalled for an extraordinary session, approves it "
               "unanimously.", "law"),
    ("Sep", "A commission is appointed to find out what happened.", "law"),
    ("5 Feb 1923", "THE GUARANTEE — the state stands behind the bank's obligations, "
                   "deposits included.", "state"),
    ("Mar", "Emil Glückstadt is remanded in custody.", "law"),
    ("23 Jun", "Glückstadt dies in hospital, before judgement.", "law"),
    ("1928", "The bank's affairs are finally settled.", "state"),
]
TONE = {"bank": DE, "state": OX, "law": IND}


def krak():
    left, top, row = 150, 96, 34
    axis = left - 26
    lines = [fold(t, "mapt" if t.startswith(("RESCUE", "THE GUAR")) else "mapx", left, W)
             for _, t, _ in KRAK]
    ys, y = [], top
    for ls in lines:
        ys.append(y)
        y += row + 12 * (len(ls) - 1)
    H = y + 50                                   # HEIGHT COMPUTED from the folded rows
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="A calendar of the Landmandsbank crisis, May 1922 to 1928: a secret '
         'inspection, a first rescue in July with extra reserve from the National Bank, a '
         'second in September with about seventy million kroner of new capital approved '
         'unanimously by the Rigsdag, a commission, a state guarantee in February 1923, the '
         'arrest and death of the bank\'s director, and the final settlement in 1928.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "LANDMANDSBANKEN, 1922 – 1923",
           "two rescues and a guarantee for the largest bank in Scandinavia",
           "Loss estimates and the split of the new capital are in the text, not here: "
           "each rests on one account.")
    o.append('<path d="M %d %d L %d %d" stroke="%s" stroke-width="1.2" opacity=".45"/>'
             % (axis, top - 12, axis, ys[-1] + 8, INK))
    for (date, text, kind), ls, y in zip(KRAK, lines, ys):
        big = text.startswith(("RESCUE", "THE GUAR"))
        col = TONE[kind]
        o.append('<circle cx="%d" cy="%d" r="%s" fill="%s"/>' % (axis, y - 4, "4.2" if big else "2.6", col))
        o.append('<text x="%d" y="%d" class="mapx" text-anchor="end">%s</text>' % (axis - 10, y, date))
        cls = "mapt" if big else "mapx"
        for j, ln in enumerate(ls):
            o.append('<text x="%d" y="%d" class="%s" fill="%s">%s</text>'
                     % (left, y + j * 12, cls, col if big else INK, ln))
    fy = ys[-1] + 34
    for ln in fold("Brown: the bank. Red: the state. Blue: the courts and the Rigsdag.",
                   "mapx", 14, W):
        o.append('<text x="14" y="%d" class="mapx">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
SEATS = [("Social Democrats", 55, OX, 1.0), ("Radicals", 20, DE, 1.0),
         ("Venstre", 44, DK, 1.0), ("Venstre, Faroes", 1, DK, .45),
         ("Conservatives", 28, IND, 1.0), ("Slesvig Party", 1, GREY, 1.0)]
PER_ROW = 25


def ting():
    total = sum(s for _, s, _, _ in SEATS)
    mainland = total - 1
    assert mainland == 148 and total == 149              # the department's two totals
    base = SEATS[0][1] + SEATS[1][1]
    assert base == 75 and base > total / 2.0 and total - base == 74
    assert base == 3 * PER_ROW                           # the base fills three rows exactly

    cell, gap = 20, 4
    step = cell + gap
    gx = (W - PER_ROW * step + gap) // 2                 # centred, computed
    gy = 110
    rows = -(-total // PER_ROW)
    cells = []
    for name, s, col, op in SEATS:
        cells += [(col, op)] * s
    assert len(cells) == total                           # item 70: cells are the seats
    counted = {}
    for name, s, col, op in SEATS:
        counted[(col, op)] = counted.get((col, op), 0) + s
    for key, v in counted.items():
        assert cells.count(key) == v
    split = gy + 3 * step - gap / 2.0
    ly = gy + rows * step + 30
    H = ly + 22 * ((len(SEATS) + 1) // 2) + 64          # HEIGHT COMPUTED from grid and legend
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="The Folketing elected on 11 April 1924, drawn as 149 squares, one per seat: '
         '55 Social Democrats, 20 Radicals, 44 Venstre plus one Venstre member for the Faroes, '
         '28 Conservatives and one member for the Slesvig Party. Social Democrats and Radicals '
         'together fill the first three rows, 75 seats, a majority of one. In 1884 the Social '
         'Democrats had two seats.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    header(o, "THE FOLKETING OF 11 APRIL 1924",
           "one square a seat: the party of two seats in 1884 is now the largest",
           "Stauning governed with the Radicals outside the cabinet. Together: the first three rows.")
    for i, (col, op) in enumerate(cells):
        r, c = divmod(i, PER_ROW)
        o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" opacity="%s"/>'
                 % (gx + c * step, gy + r * step, cell, cell, col, op))
    o.append('<path d="M %d %.1f L %d %.1f" stroke="%s" stroke-width="1.6"/>'
             % (gx - 8, split, gx + PER_ROW * step, split, INK))
    o.append('<text x="%d" y="%.1f" class="mapx" text-anchor="end">75</text>' % (gx - 12, split - 4))
    o.append('<text x="%d" y="%.1f" class="mapx" text-anchor="end">74</text>' % (gx - 12, split + 12))
    for i, (name, s, col, op) in enumerate(SEATS):
        cx = 14 + (i % 2) * (W // 2)
        cy = ly + (i // 2) * 22
        o.append('<rect x="%d" y="%d" width="12" height="12" fill="%s" opacity="%s"/>'
                 % (cx, cy - 10, col, op))
        o.append('<text x="%d" y="%d" class="mapx">%s · %d</text>' % (cx + 20, cy, name, s))
    fy = ly + 22 * ((len(SEATS) + 1) // 2) + 8
    note = ("148 seats on the mainland and one for the Faroes. Turnout 78.6 per cent. "
            "Source: the Statistical Department's count, whose two tables agree.")
    for ln in fold(note, "mapx", 14, W):
        o.append('<text x="14" y="%d" class="mapx">%s</text>' % (fy, ln))
        fy += 13
    assert fy < H
    o.append('</svg>')
    return "\n  ".join(o)


FIGS = [("svg_kapsler_1921.txt", kapsler),
        ("svg_krak_1922.txt", krak),
        ("svg_ting_1924.txt", ting)]

if __name__ == "__main__":
    for name, fn in FIGS:
        svg = fn()
        M.validate(svg, name)
        for bad in (M.check(svg, name) or []):
            print("  !! %s" % (bad,))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
