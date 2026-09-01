# -*- coding: utf-8 -*-
"""Chapter 22's three figures, deliberately in three different forms.

  svg_foundations.txt  a Denmark-Norway detail map: what he founded, and what took
  svg_koegechain.txt   the Koege naming chain, 1612-15, from the surviving list
  svg_ledger.txt       the building works against the toll and the wars, 1596-1630

The map uses mapspine's detail helpers rather than the spine frame, because at
spine scale Denmark is about 100px and six town markers would sit on top of each
other.

Run: python3 figs_22.py
"""
import mapspine as M

INK = "#3C3E36"
PAPER = "#F0F2EE"
RULE = "#C9CDC4"
OX = "#8A2B2B"
VERD = "#2E6B5E"
AMBER = "#A9601C"
MUTED = "#5F6157"


# ------------------------------------------------------------------ figure 1
# (lon, lat, name, year, took?, anchor, dy)
# dy nudges the label off the marker where two sites sit at nearly the same
# latitude: Christianopel and Christianstad are 0.2 degrees apart and their
# labels landed on top of each other.
FOUNDED = [
    (10.75, 59.91, "Christiania", 1624, True,  "start", 0),
    (9.65, 59.67, "Kongsberg", 1624, True,  "end", 0),
    (12.59, 55.67, "Christianshavn", 1618, True,  "start", 0),
    (14.16, 56.03, "Christianstad", 1614, True,  "start", 6),
    (9.43, 53.79, "Gl\u00fcckstadt", 1617, False, "start", 0),
    (16.05, 56.25, "Christianopel", 1599, False, "end", -12),
]
BBOX = (7.5, 53.4, 17.0, 60.4)
NEAR = (2.0, 50.0, 24.0, 64.0)
MW, MH = 424, 616


def foundations():
    W, H = 700, 640
    f = M.detail_frame(BBOX, MW, MH)
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Map of Denmark and southern Norway showing six towns founded by decree '
         'between 1599 and 1624. Christiania, Kongsberg, Christianshavn and Christianstad grew; '
         'Glueckstadt and Christianopel did not. The four that took sit on a harbour, an ore body '
         'or a population that had just lost its town to fire.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<g transform="translate(0,24)">')
    o.extend(M.detail_base(f, MW, MH, NEAR, scale=10, clip="fnd"))
    for lon, lat, name, yr, took, anc, ndy in FOUNDED:
        x, y = f.xy(lon, lat)
        if took:
            o.append('<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (x, y, OX))
        else:
            o.append('<circle cx="%.1f" cy="%.1f" r="5" fill="%s" stroke="%s" '
                     'stroke-width="1.6"/>' % (x, y, PAPER, OX))
        dx = 9 if anc == "start" else -9
        o.append('<text x="%.1f" y="%.1f" class="mapl" text-anchor="%s">%s</text>'
                 % (x + dx, y - 1 + ndy, anc, name))
        o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="%s">%d</text>'
                 % (x + dx, y + 11 + ndy, anc, yr))
    o.append('</g>')          # close the clip group opened by detail_base
    o.append('</g>')          # close the translate
    o.append('<text x="14" y="16" class="mapl">FOUNDED BY DECREE, 1599\u20131624</text>')

    # right-hand panel: why each one did or did not take
    px = 452
    o.append('<line x1="%d" y1="30" x2="%d" y2="%d" stroke="%s" stroke-width="1"/>'
             % (px - 16, px - 16, H - 30, RULE))
    o.append('<circle cx="%d" cy="46" r="5" fill="%s"/>' % (px, OX))
    o.append('<text x="%d" y="50" class="mapl">Took</text>' % (px + 12))
    rows = [("Christiania 1624",
             "Oslo burned for the fourteenth time; he moved the survivors under the "
             "guns of Akershus and gave them a grid."),
            ("Kongsberg 1624",
             "Silver found the year before. German miners imported within months; "
             "worked until 1958."),
            ("Christianshavn 1618",
             "A capital that needed a defended harbour quarter, on a Dutch plan, with "
             "the bastions still walkable."),
            ("Christianstad 1614",
             "Drained marsh in Sk\u00e5ne, replacing two towns he judged badly sited. "
             "Swedish since 1658 and still there.")]
    y = 70
    for name, why in rows:
        o.append('<text x="%d" y="%d" class="mapx">%s</text>' % (px, y, name))
        y += 14
        for line in wrap(why, 34):
            o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
            y += 12
        y += 8

    y += 10
    o.append('<circle cx="%d" cy="%d" r="5" fill="%s" stroke="%s" stroke-width="1.6"/>'
             % (px, y - 4, PAPER, OX))
    o.append('<text x="%d" y="%d" class="mapl">Did not</text>' % (px + 12, y))
    y += 24
    for name, why in [("Gl\u00fcckstadt 1617",
                       "Sited to take Hamburg's trade. Hamburg's trade rested on a "
                       "century of credit and connections that no charter could move "
                       "sixty kilometres downriver."),
                      ("Christianopel 1599",
                       "Built to watch the Swedish border. It is a village.")]:
        o.append('<text x="%d" y="%d" class="mapx">%s</text>' % (px, y, name))
        y += 14
        for line in wrap(why, 34):
            o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
            y += 12
        y += 8
    o.append('</svg>')
    return "\n  ".join(o)


def wrap(text, n):
    out, line = [], ""
    for word in text.split():
        if len(line) + len(word) + 1 > n:
            out.append(line)
            line = word
        else:
            line = (line + " " + word).strip()
    if line:
        out.append(line)
    return out


# ------------------------------------------------------------------ figure 2
# From the surviving list. fate: B burned, S suicide, A convicted in absentia.
KOEGE = [
    ("Johanne Tommesis", "24 Aug 1612", "B", "named four others under torture"),
    ("Kirstine Lauridsdatter", "11 Sep 1612", "B", "Johanne's own servant"),
    ("Mette Banghors", "7 Dec 1612", "B", "said she met the Devil as a rat"),
    ("Volborg B\u00f8dkers", "7 Jun 1613", "A", "escaped; convicted anyway"),
    ("Annike Christoffersdatter", "14 Jun 1613", "B", "named five others"),
    ("Anne Olufs", "26 Jun 1613", "B", ""),
    ("Karen Eriks", "30 Aug 1613", "S", "in prison"),
    ("Maren Muremester", "1613", "B", ""),
    ("Maren of Ringsbjerg", "1613", "B", ""),
    ("Maren Bysvende", "1613", "S", "in her own well, the day the summons came"),
    ("Kirsten V\u00e6verkvinde", "1613", "B", ""),
    ("Birgitte Rokkemager", "18 Sep 1615", "B", ""),
    ("Else Holtug", "6 Nov 1615", "B", ""),
    ("Mette Navns", "1615", "B", ""),
    ("Johanne Muremester", "1615", "B", ""),
    ("Magdalene, S\u00f8ren Skr\u00e6dder's wife", "1615", "B", ""),
]


def koegechain():
    W = 700
    H = 96 + len(KOEGE) * 26 + 80
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="A list of the sixteen women who died in the Koege witch trials between '
         'August 1612 and 1615, with their dates and fates. Fourteen were burned, two took their '
         'own lives, one was convicted after escaping. Two of them are recorded as having named '
         'further women under torture, which is what continued the chain.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">K\u00d8GE, AUGUST 1612 \u2013 NOVEMBER 1615</text>')
    o.append('<text x="26" y="46" class="mapt">one household\'s accusation, and everyone it '
             'reached</text>')
    o.append('<text x="26" y="72" class="mapx">Hans Bartsk\u00e6r accuses a neighbour, '
             'August 1612</text>')

    top = 96
    o.append('<line x1="38" y1="%d" x2="38" y2="%d" stroke="%s" stroke-width="1.5" '
             'opacity=".55"/>' % (top - 12, top + len(KOEGE) * 26 - 12, MUTED))
    for i, (name, date, fate, note) in enumerate(KOEGE):
        y = top + i * 26
        if fate == "B":
            o.append('<circle cx="38" cy="%d" r="4.5" fill="%s"/>' % (y - 4, OX))
        elif fate == "S":
            o.append('<rect x="33.5" y="%d" width="9" height="9" fill="%s" opacity=".55"/>'
                     % (y - 8.5, MUTED))
        else:
            o.append('<circle cx="38" cy="%d" r="4.5" fill="%s" stroke="%s" '
                     'stroke-width="1.5"/>' % (y - 4, PAPER, MUTED))
        o.append('<text x="56" y="%d" class="mapx">%s</text>' % (y, name))
        o.append('<text x="320" y="%d" class="mapt">%s</text>' % (y, date))
        if note:
            o.append('<text x="404" y="%d" class="mapt">%s</text>' % (y, note))

    b = top + len(KOEGE) * 26 + 6
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    # counted from the list, never typed: the first draft said "fourteen" burned
    # and there are thirteen, which is the kind of error nobody re-checks.
    n = {k: sum(1 for r in KOEGE if r[2] == k) for k in "BSA"}
    word = {13: "thirteen", 14: "fourteen", 15: "fifteen", 2: "two", 1: "one"}
    o.append('<circle cx="32" cy="%d" r="4.5" fill="%s"/>' % (b + 18, OX))
    o.append('<text x="44" y="%d" class="mapt">burned \u2014 %s</text>'
             % (b + 22, word.get(n["B"], n["B"])))
    o.append('<rect x="211" y="%d" width="9" height="9" fill="%s" opacity=".55"/>' % (b + 14, MUTED))
    o.append('<text x="228" y="%d" class="mapt">took her own life \u2014 %s</text>'
             % (b + 22, word.get(n["S"], n["S"])))
    o.append('<circle cx="430" cy="%d" r="4.5" fill="%s" stroke="%s" stroke-width="1.5"/>'
             % (b + 18, PAPER, MUTED))
    o.append('<text x="442" y="%d" class="mapt">escaped, convicted anyway \u2014 %s</text>'
             % (b + 22, word.get(n["A"], n["A"])))
    o.append('<text x="26" y="%d" class="mapt">A confession was not complete until the accused '
             'named others. That is what carried it forward.</text>' % (b + 44))
    o.append('<text x="26" y="%d" class="mapt">Who named whom is only partly recoverable. The '
             'names and the dates are not in doubt.</text>' % (b + 58))
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
# (label, start, end, kind) kind: w work, f fleet/fortification, x after this chapter
WORKS = [
    ("Frederiksborg", 1600, 1620, "w"),
    ("Copenhagen fortifications", 1606, 1625, "f"),
    ("Rosenborg", 1606, 1624, "w"),
    ("Bremerholm, enlarged", 1600, 1625, "f"),
    ("Christianshavn", 1618, 1625, "f"),
    ("B\u00f8rsen", 1619, 1624, "w"),
    ("Kongsberg", 1624, 1630, "w"),
    ("Nyboder", 1631, 1641, "x"),
    ("Rundet\u00e5rn", 1637, 1642, "x"),
]
WARS = [("Kalmar War", 1611, 1613), ("the German war", 1625, 1629)]
Y0, Y1 = 1596, 1645


def ledger():
    W, H = 700, 386
    L, R = 178, 674
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Timeline of Christian the Fourth\'s major building works from 1596 to 1645, '
         'with the Kalmar War of 1611 to 1613 and the German war from 1625 shaded. Almost every '
         'major work was under construction simultaneously before 1625; after 1625 building on '
         'that scale stops.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="28" class="mapl">WHAT WAS BEING BUILT, AND WHEN</text>')

    def X(yr):
        return L + (R - L) * (yr - Y0) / (Y1 - Y0)

    top = 56
    for name, a, b_ in WARS:
        o.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" opacity=".13"/>'
                 % (X(a), top - 12, X(b_) - X(a), len(WORKS) * 26 + 16, OX))
        o.append('<text x="%.1f" y="%d" class="mapt" text-anchor="middle" fill="%s">%s</text>'
                 % ((X(a) + X(b_)) / 2, top - 18, OX, name))
    for yr in range(1600, Y1 + 1, 10):
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width=".6" '
                 'opacity=".8"/>' % (X(yr), top - 12, X(yr), top + len(WORKS) * 26, RULE))
        o.append('<text x="%.1f" y="%d" class="mapt" text-anchor="middle">%d</text>'
                 % (X(yr), top + len(WORKS) * 26 + 16, yr))

    for i, (name, a, b_, kind) in enumerate(WORKS):
        y = top + i * 26
        col = {"w": OX, "f": VERD, "x": MUTED}[kind]
        op = ".28" if kind == "x" else ".62"
        o.append('<rect x="%.1f" y="%d" width="%.1f" height="13" rx="2" fill="%s" '
                 'opacity="%s"/>' % (X(a), y - 10, max(4, X(b_) - X(a)), col, op))
        o.append('<text x="%d" y="%d" class="mapx" text-anchor="end" fill="%s">%s</text>'
                 % (L - 10, y, MUTED if kind == "x" else INK, name))

    f = top + len(WORKS) * 26 + 34
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (f, f, RULE))
    o.append('<rect x="26" y="%d" width="19" height="10" fill="%s" opacity=".62"/>' % (f + 12, OX))
    o.append('<text x="52" y="%d" class="mapt">palaces and public works</text>' % (f + 21))
    o.append('<rect x="238" y="%d" width="19" height="10" fill="%s" opacity=".62"/>' % (f + 12, VERD))
    o.append('<text x="264" y="%d" class="mapt">fleet and fortification</text>' % (f + 21))
    o.append('<rect x="440" y="%d" width="19" height="10" fill="%s" opacity=".28"/>' % (f + 12, MUTED))
    o.append('<text x="466" y="%d" class="mapt">after this chapter</text>' % (f + 21))
    o.append('<text x="26" y="%d" class="mapt">Paid for from the Sound toll: an annual foreign '
             'cash flow, owed by nobody in Denmark, and stoppable by</text>' % (f + 42))
    o.append('<text x="26" y="%d" class="mapt">anyone who could close the Sound.</text>'
             % (f + 56))
    o.append('</svg>')
    return "\n  ".join(o)


if __name__ == "__main__":
    for name, fn in (("svg_foundations.txt", foundations),
                     ("svg_koegechain.txt", koegechain),
                     ("svg_ledger.txt", ledger)):
        svg = fn()
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
