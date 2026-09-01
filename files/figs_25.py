# -*- coding: utf-8 -*-
"""Chapter 25's two non-map figures.

  svg_routing.txt    where a decision travelled, before 1660 and after 1665
  svg_hartkorn.txt   one farm's dues, reduced to a single number

Both carry what the prose cannot. The routing figure exists because "colleges
replaced the council" is a sentence that sounds like a change of furniture; the
shape shows that it was a change of topology - one body that discussed everything,
against several that each discussed one thing. The hartkorn figure exists because
the 1662 and 1664 registers did not measure anything, and the only way to make
that vivid is to run the arithmetic they actually ran.

Palette follows Part F's scripts with the part colour swapped to Part G's indigo.
validate() and overruns() are both here from the start: two of Part F's four
figure scripts shipped without the XML guard.

Run: python3 figs_25.py
"""
import re
import xml.etree.ElementTree as ET

import mapspine as M

INK = "#3C3E36"
PAPER = "#F0F2EE"
RULE = "#C9CDC4"
IND = "#2F4C7A"          # part G colour
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
        if float(m.group(1)) + len(m.group(2)) * 5.55 > W - 6:
            bad.append(m.group(2)[:44])
    return bad


# ------------------------------------------------------------------ figure 2
# Five questions of five different kinds. Before 1660 they all went to one body.
QUESTIONS = [
    "A town tax",
    "A fortress",
    "A warship",
    "An appeal",
    "A licence",
]
COLLEGES = [
    ("Skatkammeret", "revenue"),
    ("Krigskollegiet", "the army"),
    ("Admiralitetet", "the fleet"),
    ("H\u00f8jesteret", "appeals"),
    ("Kancelliet", "charters"),
]


def routing():
    W, H = 700, 480
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Diagram comparing how a decision was made before and after 1660. On the '
         'left, five different kinds of question - a tax, a fortress, a ship, an appeal, a '
         'trading licence - all go to the single Council of the Realm, twenty noblemen who '
         'discussed everything, and only then to the king. On the right, each question goes to '
         'its own standing college of full-time officials, the colleges report to the Council of '
         'State, and the king decides alone. The council of noblemen has no place in the second '
         'diagram.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">WHERE A DECISION TRAVELLED</text>')
    o.append('<text x="26" y="46" class="mapt">the same five questions, before 1660 and after '
             '1665</text>')

    o.append('<text x="26" y="76" class="mapl">BEFORE</text>')
    o.append('<text x="382" y="76" class="mapl">AFTER</text>')
    o.append('<line x1="352" y1="64" x2="352" y2="410" stroke="%s" stroke-width="1"/>' % RULE)

    # ---- left: everything funnels into one body
    qy0, qgap = 104, 26
    for i, q in enumerate(QUESTIONS):
        y = qy0 + i * qgap
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (y, q))
        o.append('<path d="M 116 %d C 168 %d, 190 %d, 236 %d" fill="none" stroke="%s" '
                 'stroke-width="1" opacity=".55"/>'
                 % (y - 4, y - 4, 240, 240, MUTED))

    o.append('<rect x="236" y="222" width="98" height="38" rx="3" fill="%s" opacity=".16"/>' % INK)
    o.append('<rect x="236" y="222" width="98" height="38" rx="3" fill="none" stroke="%s" '
             'stroke-width="1.2"/>' % INK)
    o.append('<text x="285" y="238" class="mapl" text-anchor="middle">Rigsr\u00e5det</text>')
    o.append('<text x="285" y="252" class="mapt" text-anchor="middle">c. 20 noblemen</text>')
    o.append('<path d="M 285 260 L 285 292" fill="none" stroke="%s" stroke-width="1.2"/>' % MUTED)
    o.append('<rect x="236" y="294" width="98" height="30" rx="3" fill="%s" opacity=".18"/>' % VERD)
    o.append('<text x="285" y="314" class="mapl" text-anchor="middle">the king</text>')
    for i, line in enumerate(wrap("One body, meeting when summoned, deliberating every kind of "
                                  "business. It also chose the king and wrote the charter he "
                                  "signed.", 40)):
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (352 + i * 13, line))

    # ---- right: each question to its own standing office
    cx0, cgap = 382, 26
    for i, (name, what) in enumerate(COLLEGES):
        y = qy0 + i * cgap
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (cx0, y, QUESTIONS[i]))
        o.append('<path d="M 452 %d L 486 %d" fill="none" stroke="%s" stroke-width="1" '
                 'opacity=".7"/>' % (y - 4, y - 4, IND))
        o.append('<rect x="490" y="%d" width="128" height="18" rx="2" fill="%s" opacity=".16"/>'
                 % (y - 17, IND))
        o.append('<text x="496" y="%d" class="mapx">%s</text>' % (y - 4, name))
        o.append('<path d="M 618 %d L 646 %d L 646 218" fill="none" stroke="%s" '
                 'stroke-width=".9" opacity=".45"/>' % (y - 8, y - 8, IND))

    o.append('<rect x="520" y="222" width="150" height="38" rx="3" fill="%s" opacity=".16"/>' % IND)
    o.append('<rect x="520" y="222" width="150" height="38" rx="3" fill="none" stroke="%s" '
             'stroke-width="1.2"/>' % IND)
    o.append('<text x="595" y="238" class="mapl" text-anchor="middle">Statskollegiet</text>')
    o.append('<text x="595" y="252" class="mapt" text-anchor="middle">18 November 1660</text>')
    o.append('<path d="M 595 260 L 595 292" fill="none" stroke="%s" stroke-width="1.2"/>' % MUTED)
    o.append('<rect x="546" y="294" width="98" height="30" rx="3" fill="%s" opacity=".18"/>' % VERD)
    o.append('<text x="595" y="314" class="mapl" text-anchor="middle">the king</text>')
    for i, line in enumerate(wrap("Standing offices, each with one subject, staffed by men who "
                                  "came in every day. Half of H\u00f8jesteret's judges were not "
                                  "noble, and the king appointed all of them.", 40)):
        o.append('<text x="382" y="%d" class="mapt">%s</text>' % (352 + i * 13, line))

    b = 410
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    o.append('<text x="26" y="%d" class="mapt">The council was never abolished. It stopped being '
             'summoned, and after a while it had not met</text>' % (b + 20))
    o.append('<text x="26" y="%d" class="mapt">for long enough that it was clear it was not going '
             'to be.</text>' % (b + 34))
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
# What one farm paid, and what the commissioners turned it into.
# Values in ALBUM, the smallest unit: 1 toende = 8 skaepper = 32 fjerdingkar = 96 album.
# Totals are computed, never typed - chapter 22's Koege count is why.
ALB_TDR = 96
DUES = [
    ("Rye", "3 barrels", "1 barrel of rye = 1 barrel hartkorn", 3 * ALB_TDR),
    ("Barley", "2 barrels", "1 barrel of barley = 1 barrel hartkorn", 2 * ALB_TDR),
    ("Oats", "5 barrels", "2 barrels of oats = 1 barrel hartkorn", 5 * ALB_TDR // 2),
    ("Butter", "1 lispund", "valued and converted", 108),
    ("A pig", "one", "valued and converted", 48),
    ("Geese", "two", "valued and converted", 14),
    ("Carting", "4 days", "valued and converted", 24),
]


def split(alb):
    """album -> (toender, skaepper, fjerdingkar, album)"""
    t, r = divmod(alb, ALB_TDR)
    s, r = divmod(r, 12)
    fj, a = divmod(r, 3)
    return t, s, fj, a


def hartkorn():
    W = 700
    top = 118
    gap = 30
    H = top + len(DUES) * gap + 176
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="A worked example of the 1664 land register. The left column lists what one '
         'tenant farm actually owed its landlord: rye, barley, oats, butter, a pig, two geese and '
         'four days of carting. The middle column gives the conversion rule applied. The right '
         'column gives the result in hartkorn. At the foot the seven entries are added into a '
         'single figure in barrels, skaepper, fjerdingkar and album. The register did not measure '
         'any land; it converted obligations into one comparable number.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">ONE FARM, REDUCED TO A NUMBER</text>')
    o.append('<text x="26" y="46" class="mapt">what the tenant owed, and what the commissioners '
             'wrote down instead</text>')

    o.append('<text x="26" y="80" class="mapx">WHAT WAS ACTUALLY PAID</text>')
    o.append('<text x="266" y="80" class="mapx">THE RULE APPLIED</text>')
    o.append('<text x="674" y="80" class="mapx" text-anchor="end">IN HARTKORN</text>')
    o.append('<line x1="26" y1="90" x2="674" y2="90" stroke="%s" stroke-width="1"/>' % RULE)

    total = 0
    for i, (what, qty, rule, alb) in enumerate(DUES):
        y = top + i * gap
        total += alb
        t, s, fj, a = split(alb)
        parts = []
        if t:
            parts.append("%d tdr" % t)
        if s:
            parts.append("%d skp" % s)
        if fj:
            parts.append("%d fjk" % fj)
        if a:
            parts.append("%d alb" % a)
        o.append('<circle cx="32" cy="%d" r="3" fill="%s" opacity=".7"/>' % (y - 4, IND))
        o.append('<text x="44" y="%d" class="mapx">%s</text>' % (y, what))
        o.append('<text x="150" y="%d" class="mapt">%s</text>' % (y, qty))
        o.append('<text x="266" y="%d" class="mapt">%s</text>' % (y, rule))
        o.append('<text x="674" y="%d" class="mapx" text-anchor="end">%s</text>'
                 % (y, " ".join(parts)))

    b = top + len(DUES) * gap
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1.4"/>'
             % (b, b, INK))
    t, s, fj, a = split(total)
    o.append('<text x="44" y="%d" class="mapl">THE FARM</text>' % (b + 24))
    o.append('<rect x="470" y="%d" width="204" height="26" rx="3" fill="%s" opacity=".16"/>'
             % (b + 6, IND))
    o.append('<text x="674" y="%d" class="mapl" text-anchor="end">%d tdr %d skp %d fjk %d alb'
             '</text>' % (b + 24, t, s, fj, a))

    y = b + 58
    o.append('<text x="26" y="%d" class="mapx">THE LADDER</text>' % y)
    o.append('<text x="150" y="%d" class="mapt">1 t\u00f8nde = 8 sk\u00e6pper &#183; '
             '1 sk\u00e6ppe = 4 fjerdingkar &#183; 1 fjerdingkar = 3 album</text>' % y)
    y += 24
    for line in wrap("Nothing here was measured. No commissioner walked a field. The register of "
                     "1662, redone in 1664, took the landlords' own estate books and turned every "
                     "kind of obligation - grain, dairy, livestock, labour - into one artificial "
                     "unit, so that a farm on Funen and a farm in Vendsyssel could be added "
                     "together and taxed at the same rate. Denmark measured its ground for the "
                     "first time in 1682. Land was valued in hartkorn until 1903.", 96):
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (y, line))
        y += 14
    y += 6
    o.append('<text x="26" y="%d" class="mapt" fill="%s">The quantities are a worked example '
             'built from the conversion rules, not a transcription of one entry.</text>'
             % (y, MUTED))
    o.append('</svg>')
    return "\n  ".join(o)


if __name__ == "__main__":
    for name, fn in (("svg_routing.txt", routing),
                     ("svg_hartkorn.txt", hartkorn)):
        svg = fn()
        validate(svg, name)
        w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
        bad = overruns(svg, w)
        if bad:
            print("   ! overruns in %s: %s" % (name, bad))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
