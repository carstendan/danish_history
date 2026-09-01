# -*- coding: utf-8 -*-
"""Chapter 31's three figures.

  svg_1807.txt     the campaign of August-September 1807
  svg_fleet.txt    what sailed away
  svg_daler.txt    one kurantdaler, 5 January 1813

THE FIRST IS NOT THE CITY-SCALE FIRE MAP THE PLAN ASKED FOR. Drawing the extent of
the burnt quarter needs the line of the ramparts and the boundary of the fire, and
neither is available here; a plausible-looking fire boundary over a real city would
be an invention of exactly the kind this part has been refusing. The campaign at
Zealand scale is buildable, keeps the chapter's one map, and carries the thing the
city map could not: that the British walked ashore twenty kilometres up the coast
and took three weeks to set up, in a country whose army was in Holstein.

Run: python3 figs_31.py
"""
import re
import xml.etree.ElementTree as ET

import mapspine as M

INK = "#3C3E36"
PAPER = "#F0F2EE"
RULE = "#C9CDC4"
IND = "#2F4C7A"
VERD = "#2E6B5E"
AMBER = "#A9601C"
MUTED = "#5F6157"
OX = "#8A2B2B"


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


# ------------------------------------------------------------------ figure 1
ZBOX = (10.6, 54.8, 13.4, 56.3)
ZNEAR = (7.0, 53.0, 17.0, 59.0)
SIEGE_KM = 8.0                   # Svanemoellen to Kalveboderne, end to end
KM_PER_DEG_LAT = 111.2
STAGES = [
    ("6 Aug", "The ultimatum reaches the crown prince, with the army in Holstein. He refuses."),
    ("16 Aug", "British troops land at Vedb\u00e6k. Almost no resistance: the army is elsewhere."),
    ("late Aug", "Batteries set up in an arc round the city, Svanem\u00f8llen to Kalveboderne."),
    ("2 Sep", "Fire opened at half past seven in the evening."),
    ("2\u20135 Sep", "Three nights. The target is the city, not the defences."),
    ("7 Sep", "Peymann capitulates. The fleet is handed over."),
]


def campaign():
    W, H = 700, 500
    mw, mh = 356, 396
    f = M.detail_frame(ZBOX, mw, mh)
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Map of Zealand and the Sound in 1807. British troops landed at Vedbaek '
         'north of Copenhagen on 16 August and set up batteries in an arc around the city; the '
         'bombardment ran from 2 to 5 September and the city capitulated on 7 September, after '
         'which the captured Danish fleet sailed for England. A panel gives the sequence of '
         'events and the losses.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="14" y="24" class="mapl">AUGUST\u2013SEPTEMBER 1807</text>')
    o.append('<text x="14" y="40" class="mapt">they landed twenty kilometres up the coast and '
             'took three weeks</text>')
    o.append('<g transform="translate(0,52)">')
    o.extend(M.detail_base(f, mw, mh, ZNEAR, scale=10, clip="z07"))

    # the landing and the march south
    ax, ay = f.xy(12.80, 55.88)
    bx, by = f.xy(12.58, 55.855)
    o.append('<path d="M %.1f %.1f L %.1f %.1f" fill="none" stroke="%s" stroke-width="2.4"/>'
             % (ax, ay, bx, by, OX))
    o.append('<path d="M %.1f %.1f l 8 -4 l 0 8 Z" fill="%s"/>' % (bx, by, OX))
    cx, cy = f.xy(12.57, 55.70)
    o.append('<path d="M %.1f %.1f L %.1f %.1f" fill="none" stroke="%s" stroke-width="2" '
             'stroke-dasharray="5 4"/>' % (bx, by, cx, cy, OX))

    # The arc of batteries. The siege line ran Svanemoellen to Kalveboderne, about
    # SIEGE_KM end to end; the arc is a semicircle on that chord, so its radius in
    # pixels is half of it. Derived from the frame and never typed: the first
    # version was drawn at 34 px, which on this frame is 34 km, four times the
    # line it was captioned as.
    kx, ky = f.xy(12.57, 55.68)
    _, y1 = f.xy(12.57, 55.68 + SIEGE_KM / 2.0 / KM_PER_DEG_LAT)
    r = abs(ky - y1)
    o.append('<path d="M %.1f %.1f A %.1f %.1f 0 0 0 %.1f %.1f" fill="none" stroke="%s" '
             'stroke-width="1.6" stroke-dasharray="3 3" opacity=".85"/>'
             % (kx - 2, ky - r, r, r, kx - 2, ky + r, OX))
    o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="end" fill="%s">the '
             'batteries</text>' % (kx - r - 4, ky + r + 14, OX))

    # the fleet leaving
    fx, fy = f.xy(12.62, 56.10)
    gx, gy = f.xy(11.30, 56.20)
    o.append('<path d="M %.1f %.1f C %.1f %.1f, %.1f %.1f, %.1f %.1f" fill="none" stroke="%s" '
             'stroke-width="2.2"/>' % (kx, ky - 10, fx + 20, fy, gx + 40, gy - 10, gx, gy, IND))
    o.append('<path d="M %.1f %.1f l 9 -4 l 0 8 Z" fill="%s"/>' % (gx - 9, gy, IND))
    o.append('<text x="%.1f" y="%.1f" class="mapx" text-anchor="start" fill="%s">the fleet, to '
             'England</text>' % (gx + 6, gy - 8, IND))

    for lon, lat, t, a, dy in [(12.57, 55.68, "K\u00f8benhavn", "end", 4),
                               (12.57, 55.855, "Vedb\u00e6k", "end", -6),
                               (12.62, 56.04, "Helsing\u00f8r", "start", 12),
                               (11.37, 55.97, "Sj\u00e6llands Odde", "start", 0)]:
        x, y = f.xy(lon, lat)
        o.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s"/>' % (x, y, INK))
        dx = -8 if a == "end" else 8
        o.append('<text x="%.1f" y="%.1f" class="mapx" text-anchor="%s">%s</text>'
                 % (x + dx, y + dy, a, t))
    o.append('</g>')
    o.append('</g>')

    px = 396
    y = 76
    for when, what in STAGES:
        o.append('<text x="%d" y="%d" class="mapx" fill="%s">%s</text>' % (px, y, OX, when))
        for line in wrap(what, 36):
            y += 13
            o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
        y += 18

    o.append('<line x1="%d" y1="%d" x2="686" y2="%d" stroke="%s" stroke-width="1"/>'
             % (px, y, y, RULE))
    y += 20
    o.append('<text x="%d" y="%d" class="mapx">The damage</text>' % (px, y))
    for line in ["about 300 buildings destroyed",
                 "more than 1,500 damaged",
                 "the dead: about 400 by recent",
                 "research, about 1,600 by tradition"]:
        y += 14
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
# The prize of September 1807, by rate. Counted, not estimated.
# (name, count, mark size). Sizes are chosen so the widest row fits the canvas:
# 17 marks at 22+4 is exactly the 442px available from x=232 to the margin.
PRIZE = [("Ships of the line", 17, 22), ("Frigates", 17, 16),
         ("Smaller vessels", 19, 12), ("Gunboats", 26, 8)]


def fleet():
    W, H = 700, 452
    total = sum(n for _, n, _ in PRIZE)
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="A tally of the Danish fleet taken by Britain in September 1807: seventeen '
         'ships of the line, seventeen frigates, nineteen smaller vessels and twenty-six '
         'gunboats, seventy-nine hulls in all, each drawn as a mark sized by rate. The British '
         'also stripped the naval establishments and destroyed the ships standing on the '
         'stocks.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">WHAT SAILED AWAY</text>')
    o.append('<text x="26" y="46" class="mapt">the prize of September 1807, by rate</text>')

    y = 90
    for name, n, size in PRIZE:
        o.append('<text x="26" y="%d" class="mapx">%s</text>' % (y, name))
        o.append('<text x="212" y="%d" class="mapl" text-anchor="end">%d</text>' % (y, n))
        x = 232
        for i in range(n):
            o.append('<path d="M %d %d l %d %d l %d %d Z" fill="%s" opacity=".62"/>'
                     % (x, y - size / 2, size, size / 2, -size, size / 2, IND))
            x += size + 4
        y += 62

    b = y - 24
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    o.append('<text x="26" y="%d" class="mapl">%d hulls</text>' % (b + 26, total))
    o.append('<text x="200" y="%d" class="mapt">sailed for England, together with nearly '
             'everything in the naval</text>' % (b + 26))
    o.append('<text x="200" y="%d" class="mapt">stores. The ships standing on the stocks were '
             'destroyed where they</text>' % (b + 39))
    o.append('<text x="200" y="%d" class="mapt">stood, so that what remained could not be '
             'rebuilt quickly.</text>' % (b + 52))
    o.append('<text x="26" y="%d" class="mapt">Denmark had been a naval power since the fifteenth '
             'century. It stopped being one in six weeks.</text>' % (b + 78))
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
OLD_PER_NEW = 6
PROPERTY_TAX_PCT = 6
MORTGAGE_PCT = 6.5
CAP_TOTAL = 46
CAP_EXCHANGE = 27
CAP_WAR = 15
CAP_REST = CAP_TOTAL - CAP_EXCHANGE - CAP_WAR   # computed, not typed: 4
COURSE_PCT = 6


def daler():
    # H was 486. The ceiling note now runs to two lines, so the canvas grows by one
    # line height rather than the closing rule being moved up onto the text.
    W, H = 700, 502
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="A diagram of the Danish currency reform of 5 January 1813. Six old '
         'kurantdaler notes were exchanged for one new rigsbankdaler, writing off five sixths of '
         'the paper money. The new issue was capped at forty-six million rigsbankdaler, of which '
         'twenty-seven million were for the exchange and fifteen million a war fund; the '
         'remaining four million is not accounted for in the sources used here. The silver '
         'behind it was raised by a charge of six per cent on the value of all fixed property in '
         'the realm.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">SIX FOR ONE</text>')
    o.append('<text x="26" y="46" class="mapt">the money reform of 5 January 1813, called the '
             'state bankruptcy afterwards</text>')

    o.append('<text x="26" y="86" class="mapx">BEFORE</text>')
    for i in range(OLD_PER_NEW):
        o.append('<rect x="%d" y="100" width="52" height="30" rx="2" fill="%s" opacity=".28" '
                 'stroke="%s" stroke-width=".8"/>' % (26 + i * 58, MUTED, MUTED))
        o.append('<text x="%d" y="119" class="mapt" text-anchor="middle">1 kur.</text>'
                 % (26 + i * 58 + 26))
    o.append('<text x="392" y="120" class="mapl">\u2192</text>')
    o.append('<rect x="424" y="100" width="72" height="30" rx="2" fill="%s" opacity=".45"/>'
             % IND)
    o.append('<text x="460" y="119" class="mapx" text-anchor="middle">1 rbd.</text>')
    o.append('<text x="424" y="148" class="mapt">five sixths of the paper money, gone</text>')

    o.append('<text x="26" y="176" class="mapx">THE OLD NOTE HAD ALREADY FALLEN TO</text>')
    o.append('<rect x="26" y="188" width="440" height="18" fill="%s" opacity=".14"/>' % MUTED)
    o.append('<rect x="26" y="188" width="%.1f" height="18" fill="%s" opacity=".55"/>'
             % (440 * COURSE_PCT / 100.0, OX))
    o.append('<text x="480" y="202" class="mapx">%d%% of face value in silver</text>' % COURSE_PCT)

    o.append('<text x="26" y="248" class="mapx">WHAT BACKED THE NEW ONE</text>')
    y = 268
    for line in ["A charge of %d per cent on the value of all fixed property in Denmark, Norway,"
                 % PROPERTY_TAX_PCT,
                 "Slesvig and Holstein, payable in silver \u2014 at once, or standing as a first",
                 "mortgage on the property at %.1f per cent a year." % MORTGAGE_PCT]:
        o.append('<text x="26" y="%d" class="mapt">%s</text>' % (y, line))
        y += 14
    y += 10
    o.append('<text x="26" y="%d" class="mapt" fill="%s">Every house, farm and workshop in the '
             'realm was made security for the new notes.</text>' % (y, IND))

    y += 44
    o.append('<text x="26" y="%d" class="mapx">AND A CEILING</text>' % y)
    y += 16
    barw = 500
    # Full-width track, as the course bar above has, so that the part of the
    # ceiling neither figure accounts for reads as a shortfall and not as absent.
    o.append('<rect x="26" y="%d" width="%d" height="22" fill="%s" opacity=".14"/>'
             % (y, barw, MUTED))
    o.append('<rect x="26" y="%d" width="%.1f" height="22" fill="%s" opacity=".50"/>'
             % (y, barw * CAP_EXCHANGE / float(CAP_TOTAL), IND))
    o.append('<rect x="%.1f" y="%d" width="%.1f" height="22" fill="%s" opacity=".50"/>'
             % (26 + barw * CAP_EXCHANGE / float(CAP_TOTAL), y,
                barw * CAP_WAR / float(CAP_TOTAL), OX))
    o.append('<text x="%.1f" y="%d" class="mapt" text-anchor="middle">%d m \u2014 the '
             'exchange</text>' % (26 + barw * CAP_EXCHANGE / float(CAP_TOTAL) / 2, y + 15,
                                  CAP_EXCHANGE))
    o.append('<text x="%.1f" y="%d" class="mapt" text-anchor="middle">%d m \u2014 war</text>'
             % (26 + barw * (CAP_EXCHANGE + CAP_WAR / 2.0) / CAP_TOTAL, y + 15, CAP_WAR))
    o.append('<text x="%.1f" y="%d" class="mapt" text-anchor="middle">%d m</text>'
             % (26 + barw * (CAP_EXCHANGE + CAP_WAR + CAP_REST / 2.0) / CAP_TOTAL,
                y + 15, CAP_REST))
    o.append('<text x="%d" y="%d" class="mapt">%d million rigsbankdaler, and never more \u2014 of '
             'which %d m is not accounted</text>' % (26, y + 40, CAP_TOTAL, CAP_REST))
    o.append('<text x="%d" y="%d" class="mapt">for in the sources used here.</text>'
             % (26, y + 54))

    b = H - 52
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    o.append('<text x="26" y="%d" class="mapt">It was not a bankruptcy: nothing was declared '
             'insolvent and no creditor\'s claim was</text>' % (b + 20))
    o.append('<text x="26" y="%d" class="mapt">extinguished. It was a write-down and a forced '
             'postponement, imposed on people with no vote.</text>' % (b + 33))
    o.append('</svg>')
    return "\n  ".join(o)


if __name__ == "__main__":
    for name, fn in (("svg_1807.txt", campaign),
                     ("svg_fleet.txt", fleet),
                     ("svg_daler.txt", daler)):
        svg = fn()
        validate(svg, name)
        w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
        bad = overruns(svg, w)
        if bad:
            print("   ! overruns in %s: %s" % (name, bad))
        M.overflows(svg, name)
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
