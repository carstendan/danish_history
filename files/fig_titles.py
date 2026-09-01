# -*- coding: utf-8 -*-
"""Figure 2, chapter 16: the ladder of titles.

Part D used a reign timeline, a three-stage process diagram, a family tree and a
two-column ledger. This is none of those: it is the words themselves, rung by
rung, each set against what it granted and what it withheld. The argument of the
chapter in one image - the title goes up and down, the power only goes up.
"""
import mapspine as M

PART_E = "#2E6B5E"
INK = "#221E18"
MUTED = "#6C6E63"
RULE = "#C9CDC4"
W = 900

RUNGS = [
    ("1375", "days after Valdemar Atterdag dies, she signs herself",
     ["Norges og Sveriges dronning og hr. Valdemars",
      "datter og rette arving"],
     "Queen of Norway and Sweden, and Sir Valdemar's daughter and rightful heir",
     ["A claim, put in writing before", "anyone else could put one"],
     ["No office in Denmark at all.", "Denmark elected its kings."]),

    ("1376", "at the assembly in Slagelse, 3 May",
     ["~Oluf, aged five, is elected king; his parents",
      "~and the council govern in his name"],
     "She is inside the regency, not above it",
     ["A hand on the machinery, and", "seven years to learn it"],
     ["The authority was her son's,", "and it was shared."]),

    ("1387", "at the Lund assembly, a week after Oluf died",
     ["fuldm\u00e6gtig frue og husbond og det ganske",
      "rige Danmarks formynder"],
     "Plenipotentiary lady and husband, and guardian of the whole realm of Denmark",
     ["Everything a king did, under", "a formula nobody had used"],
     ["The crown. She was not made", "queen of Denmark, then or ever."]),

    ("1388", "in Norway, and at Dalaborg on Palm Sunday",
     ["Norges m\u00e6gtige frue og retm\u00e6ssige husbond",
      "Sveriges fuldm\u00e6gtige frue og rette husbond"],
     "The same words again, twice, in the other two kingdoms",
     ["One standing in all three", "realms \u2014 in Norway, for life"],
     ["Sweden still had a crowned", "king, and Albrecht had an army."]),

    ("1397", "at Kalmar, 17 June",
     ["~Erik is crowned over all three; she is",
      "vor n\u00e5dige frue dronning Margrete"],
     "Our gracious lady, Queen Margrete — a courtesy, and a step down on paper",
     ["A crowned king of her choosing,", "and her holdings secured for life"],
     ["Nothing she had been doing.", "The title fell; the power did not."]),
]

TOP = 78
STEP = 92
H = TOP + STEP * len(RUNGS) + 46


def t(x, y, s, cls="mapx", fill=MUTED, anchor="start", extra=""):
    return ('<text x="%.1f" y="%.1f" class="%s" fill="%s" text-anchor="%s"%s>%s</text>'
            % (x, y, cls, fill, anchor, extra, s))


def build():
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Diagram of the five titles Margrete was hailed by between 1375 and '
         '1397, each set against what the words granted her and what they withheld. The '
         'sequence runs from a written claim in 1375, through the regency of 1376, the '
         'unprecedented formula of plenipotentiary lady and husband taken at Lund in 1387 '
         'and repeated in Norway and Sweden in 1388, to Kalmar in 1397, where the title '
         'goes down to gracious lady while the power stays where it was.">' % (W, H),
         '<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, M.PAPER)]

    o.append(t(26, 34, "THE WORDS", "mapt", PART_E))
    o.append(t(496, 34, "WHAT THEY GRANTED", "mapt", PART_E))
    o.append(t(700, 34, "WHAT THEY WITHHELD", "mapt", PART_E))
    o.append('<line x1="26" y1="46" x2="%d" y2="46" stroke="%s" stroke-width=".8"/>'
             % (W - 26, RULE))

    # the ladder itself: a spine with a rung at each step
    y0 = TOP + 6
    y1 = TOP + STEP * (len(RUNGS) - 1) + 6
    o.append('<line x1="14" y1="%.1f" x2="14" y2="%.1f" stroke="%s" stroke-width="1.2" '
             'opacity=".5"/>' % (y0, y1, PART_E))

    for i, (year, when, danish, gloss, gave, held) in enumerate(RUNGS):
        y = TOP + i * STEP
        o.append('<rect x="10" y="%.1f" width="8" height="8" fill="%s"/>' % (y + 2, PART_E))
        o.append(t(26, y + 10, year, "mapl", PART_E))
        o.append(t(72, y + 10, when, "mapx", MUTED))
        for k, line in enumerate(danish):
            # a leading ~ marks description rather than quotation: only the Danish
            # words themselves are set in italic, as they are in the prose
            plain = line.startswith("~")
            o.append(t(26, y + 30 + k * 15, line.lstrip("~"), "mapx", INK,
                       extra="" if plain else ' font-style="italic"'))
        o.append(t(26, y + 30 + len(danish) * 15 + 3, gloss, "mapt", MUTED))
        for k, line in enumerate(gave):
            o.append(t(496, y + 12 + k * 14, line, "mapx", MUTED))
        for k, line in enumerate(held):
            o.append(t(700, y + 12 + k * 14, line, "mapx", MUTED))
        if i < len(RUNGS) - 1:
            o.append('<line x1="26" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" '
                     'stroke-width=".6" opacity=".8"/>' % (y + STEP - 16, W - 26,
                                                           y + STEP - 16, RULE))

    o.append('<line x1="26" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width=".8"/>'
             % (H - 40, W - 26, H - 40, RULE))
    o.append(t(26, H - 22,
               "husbond is husband in the older sense \u2014 the head of a household, the one who "
               "runs the estate. No woman in Scandinavia had been given the word before.",
               "mapt", MUTED))
    o.append('</svg>')
    return "\n  ".join(o)


if __name__ == "__main__":
    svg = build()
    open("svg_titles.txt", "w", encoding="utf-8").write(svg)
    M.rasterise(svg, "look_titles.png")
    print("wrote svg_titles.txt (%d chars), %dx%d" % (len(svg), W, H))
