# -*- coding: utf-8 -*-
"""Chapter 26's figures.

  svg_scania.txt    the Scanian theatre, 1675-79: what was taken and what it cost
  svg_mandebod.txt  who owed for a killing, 1241 and 1683

  svg_cell.txt      the Blue Tower room, at the scale she gives for it

The cell is drawn in HER unit. Leonora Christina had no rule and no tape, so she
measured the room by walking it: seven of her paces long and six wide, with two
beds, a table and two chairs. Every dimension in the figure is that measurement
and nothing else - no metres, because she had none, and converting them would be
substituting our confidence for her evidence. The four doors are hers too: her bed
stood facing them, and with all three open she could see as far as the stair door,
which was the fourth.

The mandebod figure was going to be "a fine in 1241, the gallows in 1683" and
that is wrong: Jyske Lov had already made premeditated killing an orbodemaal,
punishable by outlawry and not by any fine. The change over four hundred years is
not the severity but the debtor - a kin group that owed collectively, replaced by
one man who owes alone. That is this chapter's argument about the state, so the
figure is built on who pays rather than on how much.

Run: python3 figs_26.py
"""
import re
import xml.etree.ElementTree as ET

import map_1660 as M66
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
        if float(m.group(1)) + len(m.group(2)) * 6.1 > W - 6:
            bad.append(m.group(2)[:44])
    return bad


def land_clip(f, polys, near, w, h, cid):
    return ('<clipPath id="%s"><path d="%s"/></clipPath>'
            % (cid, M.detail_land_path(f, polys, near, w, h)))


# ------------------------------------------------------------------ figure 1
# Goeinge: the forest country of north-eastern Skaane where the resistance held.
GOINGE = [(13.62, 56.08), (14.35, 56.10), (14.48, 56.34), (14.05, 56.48), (13.60, 56.36)]
SBOX = (11.6, 55.1, 15.6, 56.9)
SNEAR = (8.0, 53.0, 20.0, 60.0)

# (lon, lat, label, year/date, kind) kind: b battle, t town taken, x atrocity, n naval
# (lon, lat, label, when, kind, anchor, dy)
MARKS = [
    (13.19, 55.70, "Lund", "4 Dec 1676", "b", "start", 0),
    (12.83, 55.87, "Landskrona", "14 Jul 1677", "b", "start", 0),
    (12.694, 56.046, "Helsingborg", "taken 1676", "t", "start", -14),
    (14.16, 56.03, "Kristianstad", "taken 1676", "t", "start", 0),
    (13.00, 55.60, "Malm\u00f6", "held out", "t", "end", 6),
    (14.10, 56.28, "\u00d6rkened", "burned 1678", "x", "start", 0),
    (12.75, 55.42, "K\u00f8ge Bugt", "1 Jul 1677", "n", "end", 0),
]


def scania():
    W, H = 700, 486
    mw, mh = 452, 400
    f = M.detail_frame(SBOX, mw, mh)
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Map of Scania and the Sound during the Scanian War. A Danish army crossed '
         'from Zealand in 1676 and took Helsingborg, Landskrona and Kristianstad, but was beaten '
         'at Lund on 4 December 1676. Niels Juel destroyed the Swedish fleet in the water between '
         'Stevns and Falsterbo on 1 July 1677. The forest country of Goeinge in the north-east, '
         'shaded, was where the irregular resistance held, and the parish of Oerkened in it was '
         'burned on royal order in 1678.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="14" y="24" class="mapl">THE THEATRE, 1675\u201379</text>')
    o.append('<text x="14" y="40" class="mapt">four years, and the border did not move</text>')
    o.append('<g transform="translate(0,52)">')
    o.extend(M.detail_base(f, mw, mh, SNEAR, scale=10, clip="sc"))
    o.append(land_clip(f, M.land(50), SNEAR, mw, mh, "scl"))

    d = f.path(M66.SCANIA, close=True)
    if d:
        o.append('<g clip-path="url(#scl)"><path d="%s" fill="%s" fill-opacity=".16"/></g>'
                 % (d, IND))
    d = f.path(GOINGE, close=True)
    if d:
        o.append('<g clip-path="url(#scl)"><path d="%s" fill="%s" fill-opacity=".30" '
                 'stroke="%s" stroke-width="1" stroke-dasharray="3 3"/></g>' % (d, VERD, VERD))

    # the crossing: Zealand to Skaane, summer 1676
    ax, ay = f.xy(12.28, 56.13)
    bx, by = f.xy(12.58, 56.06)
    o.append('<path d="M %.1f %.1f L %.1f %.1f" fill="none" stroke="%s" stroke-width="2.2" '
             'opacity=".85"/>' % (ax, ay, bx, by, IND))
    o.append('<path d="M %.1f %.1f l -8 -3 l 2 6 Z" fill="%s"/>' % (bx, by, IND))

    for lon, lat, name, when, kind, anc, mdy in MARKS:
        x, y = f.xy(lon, lat)
        if kind == "b":
            o.append('<path d="M %.1f %.1f l 5 5 M %.1f %.1f l -5 5" stroke="%s" '
                     'stroke-width="2"/>' % (x - 2.5, y - 2.5, x + 2.5, y - 2.5, IND))
        elif kind == "x":
            o.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s"/>' % (x, y, AMBER))
        elif kind == "n":
            o.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="none" stroke="%s" '
                     'stroke-width="1.8"/>' % (x, y, VERD))
        else:
            o.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s"/>' % (x, y, MUTED))
        dx = -8 if anc == "end" else 8
        o.append('<text x="%.1f" y="%.1f" class="mapx" text-anchor="%s">%s</text>'
                 % (x + dx, y - 1 + mdy, anc, name))
        o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="%s">%s</text>'
                 % (x + dx, y + 11 + mdy, anc, when))

    for lon, lat, t in [(13.9, 55.35, "SK\u00c5NE"), (11.95, 55.62, "SJ\u00c6LLAND")]:
        x, y = f.xy(lon, lat)
        o.append('<text x="%.1f" y="%.1f" class="mapl" text-anchor="middle">%s</text>' % (x, y, t))
    gx, gy = f.xy(13.98, 56.56)
    o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="middle" fill="%s">G\u00f6inge'
             '</text>' % (gx, gy, VERD))
    o.append('</g>')
    o.append('</g>')

    px = 470
    y = 76
    o.append('<text x="%d" y="%d" class="mapx">The order of it</text>' % (px, y))
    y += 20
    for when, what in [("1675", "Christian 5. declares war"),
                       ("1676", "the army crosses; most of Sk\u00e5ne comes over"),
                       ("4 Dec 1676", "Lund. The province is decided"),
                       ("1 Jul 1677", "K\u00f8ge Bugt. The sea is decided"),
                       ("1678", "\u00d6rkened burned"),
                       ("1679", "Fontainebleau. Everything returned")]:
        o.append('<text x="%d" y="%d" class="mapx" fill="%s">%s</text>' % (px, y, IND, when))
        for line in wrap(what, 28):
            y += 13
            o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
        y += 20

    o.append('<line x1="%d" y1="%d" x2="686" y2="%d" stroke="%s" stroke-width="1"/>'
             % (px, y, y, RULE))
    y += 18
    for line in wrap("Denmark won at sea and lost the province. Louis 14. ended the war and "
                     "required every conquest given back.", 30):
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
        y += 13
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
# Jyske Lov's tariff of injury, as fractions of a full mandebod.
TARIFF = [
    ("Tongue, or nose", "full"),
    ("Both eyes, hands or feet", "full"),
    ("One eye, hand or foot", "half"),
    ("An ear", "quarter"),
]
FRACTION = {"full": 1.0, "half": 0.5, "quarter": 0.25}
MARK = 18          # a full mandebod under Jyske Lov is three times eighteen marks
SALE = [("The killer himself", "1/3"),
        ("His father's kin", "1/3"),
        ("His mother's kin", "1/3")]


def mandebod():
    W, H = 700, 470
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Diagram comparing who owed for a killing under Jyske Lov of 1241 and under '
         'Danske Lov of 1683. On the left, a full mandebod of three times eighteen marks, with a '
         'tariff pricing injuries as fractions of it, and the sum divided in three: one third '
         'from the killer, one third from his father\'s kin, one third from his mother\'s kin. On '
         'the right, the killer alone owes, premeditated killing is capital, and the offence is '
         'owed to God and the king rather than to the dead man\'s family.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">WHO OWED FOR A KILLING</text>')
    o.append('<text x="26" y="46" class="mapt">the change between the two codes is not the '
             'severity. It is the debtor.</text>')
    o.append('<line x1="350" y1="64" x2="350" y2="392" stroke="%s" stroke-width="1"/>' % RULE)

    # ---- left: 1241
    o.append('<text x="26" y="86" class="mapl">JYSKE LOV, 1241</text>')
    o.append('<text x="26" y="102" class="mapt">a full mandebod: 3 \u00d7 18 marks,</text>')
    o.append('<text x="26" y="116" class="mapt">and 3 more to the king \u2014 about an ox</text>')

    y = 146
    o.append('<text x="26" y="%d" class="mapx">PRICED AS A FRACTION OF IT</text>' % y)
    y += 8
    for what, frac in TARIFF:
        y += 22
        wpx = 96 * FRACTION[frac]
        o.append('<rect x="26" y="%d" width="%.1f" height="10" fill="%s" opacity=".55"/>'
                 % (y - 8, wpx, IND))
        o.append('<text x="130" y="%d" class="mapt">%s</text>' % (y, what))
    y += 10
    o.append('<text x="26" y="%d" class="mapt">An ear is a quarter, the law says,</text>'
             % (y + 14))
    o.append('<text x="26" y="%d" class="mapt">because it can be covered with a cap.</text>'
             % (y + 27))

    y += 56
    o.append('<text x="26" y="%d" class="mapx">AND PAID IN THREE SHARES</text>' % y)
    for i, (who, share) in enumerate(SALE):
        yy = y + 20 + i * 20
        o.append('<rect x="26" y="%d" width="52" height="12" fill="%s" opacity=".45"/>'
                 % (yy - 9, IND))
        o.append('<text x="88" y="%d" class="mapt">%s \u2014 %s</text>' % (yy, share, who))
    o.append('<text x="26" y="%d" class="mapt">A family owed for what a member had done.</text>'
             % (y + 92))

    # ---- right: 1683
    o.append('<text x="382" y="86" class="mapl">DANSKE LOV, 1683</text>')
    o.append('<text x="382" y="102" class="mapt">no tariff of body parts, and no shares</text>')

    o.append('<rect x="382" y="132" width="290" height="46" rx="3" fill="%s" opacity=".14"/>'
             % IND)
    o.append('<rect x="382" y="132" width="290" height="46" rx="3" fill="none" stroke="%s" '
             'stroke-width="1.2"/>' % IND)
    o.append('<text x="527" y="152" class="mapl" text-anchor="middle">The killer alone</text>')
    o.append('<text x="527" y="169" class="mapt" text-anchor="middle">The kin owe nothing</text>')

    y = 208
    for line in wrap("Danske Lov finally established what Jyske Lov had been reaching for: that "
                     "the man who did it answers for it, and nobody else. Premeditated killing "
                     "was already beyond any fine in 1241, punishable with outlawry. What "
                     "survived four hundred years was the collective debt, and 1683 ended it.",
                     52):
        o.append('<text x="382" y="%d" class="mapt">%s</text>' % (y, line))
        y += 14

    y += 14
    o.append('<text x="382" y="%d" class="mapx">AND OWED TO WHOM</text>' % y)
    y += 8
    for line in wrap("A crime now offended God as well as the realm. The criminal law was fitted "
                     "to the law of Moses, and the penalties were built on retribution and "
                     "deterrence, to appease Him. Compensation to a family is not part of that "
                     "arrangement anywhere.", 45):
        y += 14
        o.append('<text x="382" y="%d" class="mapt">%s</text>' % (y, line))

    b = 406
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    o.append('<text x="26" y="%d" class="mapt">Roughly two thirds of Jyske Lov was carried '
             'forward into Danske Lov, and a few</text>' % (b + 20))
    o.append('<text x="26" y="%d" class="mapt">of its provisions are still in force. The kin\'s '
             'share of the debt was not.</text>' % (b + 34))
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
# Her own measurement, in her own unit. Nothing here is converted.
PACES_L, PACES_W = 7, 6
IN_FROM = (1663, 8, 8)
OUT_ON = (1685, 5, 19)


def cell():
    import datetime
    days = (datetime.date(*OUT_ON) - datetime.date(*IN_FROM)).days
    W, H = 700, 452
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="A plan of Leonora Christina\'s room in the Blue Tower, drawn to the '
         'measurement she gives in Jammers Minde: seven of her paces long and six wide, '
         'containing two beds, a table and two chairs. Four doors are marked in sequence between '
         'her bed and the stair. She was held in the tower for %d days without once going '
         'outside.">' % (W, H, days)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">SEVEN OF MY PACES LONG AND SIX BROAD</text>')
    o.append('<text x="26" y="46" class="mapt">the room as she measured it, having nothing to '
             'measure it with</text>')

    # the plan. One pace = 34px, so the room is 238 x 204.
    U = 34
    ox, oy = 40, 86
    rw, rh = PACES_L * U, PACES_W * U
    o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" opacity=".10"/>'
             % (ox, oy, rw, rh, IND))
    o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s" '
             'stroke-width="2"/>' % (ox, oy, rw, rh, INK))
    # grid of paces, so the unit is visible and countable
    for i in range(1, PACES_L):
        o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width=".5" '
                 'opacity=".6"/>' % (ox + i * U, oy, ox + i * U, oy + rh, RULE))
    for j in range(1, PACES_W):
        o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width=".5" '
                 'opacity=".6"/>' % (ox, oy + j * U, ox + rw, oy + j * U, RULE))

    # what was in it: two beds, a table, two chairs
    o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="2" fill="%s" opacity=".45"/>'
             % (ox + 6, oy + 8, U * 2, U + 6, MUTED))
    o.append('<text x="%d" y="%d" class="mapt">bed</text>' % (ox + 14, oy + 30))
    o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="2" fill="%s" opacity=".45"/>'
             % (ox + 6, oy + rh - U - 14, U * 2, U + 6, MUTED))
    o.append('<text x="%d" y="%d" class="mapt">bed</text>' % (ox + 14, oy + rh - 26))
    o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="2" fill="%s" opacity=".45"/>'
             % (ox + rw - U * 2 - 10, oy + rh / 2 - 18, U + 10, 36, AMBER))
    o.append('<text x="%d" y="%d" class="mapt">table</text>' % (ox + rw - U * 2 - 4, oy + rh / 2 + 4))
    for k in (-1, 1):
        o.append('<circle cx="%d" cy="%d" r="7" fill="none" stroke="%s" stroke-width="1.4"/>'
                 % (ox + rw - 26, oy + rh / 2 + k * 30, MUTED))
    o.append('<text x="%d" y="%d" class="mapt" text-anchor="middle">chairs</text>'
             % (ox + rw - 26, oy + rh + 16))

    # the scale, in her unit
    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1"/>'
             % (ox, oy - 14, ox + rw, oy - 14, MUTED))
    o.append('<text x="%d" y="%d" class="mapt" text-anchor="middle">7 paces</text>'
             % (ox + rw / 2, oy - 20))
    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1"/>'
             % (ox - 14, oy, ox - 14, oy + rh, MUTED))
    o.append('<text x="%d" y="%d" class="mapt" text-anchor="middle" '
             'transform="rotate(-90 %d %d)">6 paces</text>'
             % (ox - 20, oy + rh / 2, ox - 20, oy + rh / 2))

    # the four doors, in sequence, out to the stair
    dx0 = ox + rw
    for i in range(4):
        x = dx0 + 18 + i * 34
        o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2.4"/>'
                 % (x, oy + rh / 2 - 13, x, oy + rh / 2 + 13, IND))
        o.append('<text x="%d" y="%d" class="mapt" text-anchor="middle">%d</text>'
                 % (x, oy + rh / 2 + 28, i + 1))
    o.append('<text x="%d" y="%d" class="mapt">to the stair</text>' % (dx0 + 18, oy + rh / 2 - 22))

    px = 470
    y = 96
    for line in wrap("She had no rule and no tape, so she paced it. Two beds, a table and two "
                     "chairs. Newly whitewashed when she came in, and it stank; the floor was so "
                     "thick with filth she took it for clay.", 30):
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
        y += 14
    y += 12
    for line in wrap("Her bed faced the doors. With all three open she could see as far as the "
                     "stair door, which was the fourth.", 30):
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
        y += 14

    y += 18
    o.append('<line x1="%d" y1="%d" x2="686" y2="%d" stroke="%s" stroke-width="1"/>'
             % (px, y, y, RULE))
    y += 24
    o.append('<text x="%d" y="%d" class="mapl">%s DAYS</text>' % (px, y, format(days, ",d")))
    y += 16
    for line in wrap("8 August 1663 to 19 May 1685. She counted it herself as 21 years, 9 months "
                     "and 11 days, and never once went outside in any of them.", 30):
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
        y += 14

    b = oy + rh + 74
    o.append('<line x1="26" y1="%d" x2="440" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    o.append('<text x="26" y="%d" class="mapt">No charge was ever brought and no trial was '
             'ever held.</text>' % (b + 20))
    o.append('</svg>')
    return "\n  ".join(o)


if __name__ == "__main__":
    for name, fn in (("svg_scania.txt", scania),
                     ("svg_mandebod.txt", mandebod),
                     ("svg_cell.txt", cell)):
        svg = fn()
        validate(svg, name)
        w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
        bad = overruns(svg, w)
        if bad:
            print("   ! overruns in %s: %s" % (name, bad))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))

