# -*- coding: utf-8 -*-
"""Chapter 24's three figures.

  svg_icemarch.txt   the six crossings, 30 January to 8 February 1658
  svg_lost1658.txt   Roskilde against the Peace of Copenhagen
  svg_collapse.txt   thirty-two months, at the scale it happened on

Run: python3 figs_24.py
"""
import map_1397 as M97
import mapspine as M

INK = "#3C3E36"
PAPER = "#F0F2EE"
RULE = "#C9CDC4"
OX = "#8A2B2B"
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


def land_clip(f, polys, near, w, h, cid):
    return ('<clipPath id="%s"><path d="%s"/></clipPath>'
            % (cid, M.detail_land_path(f, polys, near, w, h)))


def validate(svg, name):
    import xml.etree.ElementTree as ET
    try:
        ET.fromstring(svg)
    except ET.ParseError as e:
        raise SystemExit("!! %s not well-formed at line %d: %s"
                         % (name, e.position[0], svg.splitlines()[e.position[0] - 1][:110]))


def overruns(svg, W):
    import re
    bad = []
    for m in re.finditer(r'<text x="([\d.]+)"(?![^>]*text-anchor="(?:end|middle)")[^>]*>([^<]*)<',
                         svg):
        if float(m.group(1)) + len(m.group(2)) * 5.55 > W - 6:
            bad.append(m.group(2)[:44])
    return bad


# ------------------------------------------------------------------ figure 1
# (lon, lat) waypoints of the actual march, with the dates of each crossing.
LEGS = [
    ((9.78, 55.30), (10.02, 55.38), "30 Jan", "Little Belt \u2014 Jutland to Funen"),
    ((10.02, 55.38), (10.35, 55.22), "", ""),
    ((10.35, 55.22), (10.61, 55.04), "", ""),
    ((10.61, 55.04), (10.80, 54.95), "5 Feb", "Funen to Langeland, by T\u00e5singe"),
    ((10.80, 54.95), (11.15, 54.83), "6 Feb", "Langeland to Lolland"),
    ((11.15, 54.83), (11.80, 54.80), "", ""),
    ((11.80, 54.80), (11.95, 54.80), "7 Feb", "Lolland to Falster"),
    ((11.95, 54.80), (11.90, 55.02), "8 Feb", "Falster to Zealand"),
    ((11.90, 55.02), (12.50, 55.64), "", ""),
]
IBOX = (9.0, 54.3, 13.3, 56.4)
INEAR = (4.0, 51.0, 18.0, 60.0)


def icemarch():
    W, H = 700, 470
    mw, mh = 468, 386
    f = M.detail_frame(IBOX, mw, mh)
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Map of the Danish islands showing the Swedish army\'s route across the '
         'frozen belts between 30 January and 8 February 1658: from Jutland to Funen over the '
         'Little Belt, then by Tasinge to Langeland, to Lolland, to Falster and finally to '
         'Zealand. The direct crossing of the Great Belt from Nyborg to Korsoer was not used."'
         '>' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="14" y="24" class="mapl">THE MARCH ACROSS THE BELT</text>')
    o.append('<text x="14" y="40" class="mapt">30 January \u2013 8 February 1658</text>')
    o.append('<g transform="translate(0,52)">')
    o.extend(M.detail_base(f, mw, mh, INEAR, scale=10, clip="ice"))

    # the route not taken: the direct Great Belt passage, too wide and broken
    ax, ay = f.xy(10.79, 55.31)          # Nyborg
    bx, by = f.xy(11.14, 55.33)          # Korsoer
    o.append('<path d="M %.1f %.1f L %.1f %.1f" fill="none" stroke="%s" stroke-width="1.6" '
             'stroke-dasharray="5 4" opacity=".7"/>' % (ax, ay, bx, by, MUTED))
    o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="middle">not used</text>'
             % ((ax + bx) / 2.0, ay + 16))

    for (a, b, date, _) in LEGS:
        x1, y1 = f.xy(*a)
        x2, y2 = f.xy(*b)
        col = OX if date else MUTED
        wdt = "2.4" if date else "1.6"
        o.append('<path d="M %.1f %.1f L %.1f %.1f" fill="none" stroke="%s" stroke-width="%s" '
                 'opacity=".9"/>' % (x1, y1, x2, y2, col, wdt))
        if date:
            o.append('<circle cx="%.1f" cy="%.1f" r="3.2" fill="%s"/>' % (x2, y2, OX))
    for lon, lat, t, a in [(9.3, 55.9, "JYLLAND", "middle"), (10.32, 55.28, "FYN", "middle"),
                           (11.9, 55.55, "SJ\u00c6LLAND", "middle"),
                           (10.88, 54.66, "Langeland", "middle"),
                           (11.42, 54.60, "Lolland", "middle"),
                           (12.18, 54.86, "Falster", "start")]:
        x, y = f.xy(lon, lat)
        cls = "mapl" if t.isupper() else "mapt"
        o.append('<text x="%.1f" y="%.1f" class="%s" text-anchor="%s">%s</text>'
                 % (x, y, cls, a, t))
    kx, ky = f.xy(12.57, 55.68)
    o.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="%s"/>' % (kx, ky, INK))
    o.append('<text x="%.1f" y="%.1f" class="mapx" text-anchor="end">K\u00f8benhavn</text>'
             % (kx - 5, ky + 3))
    o.append('</g>')
    o.append('</g>')

    px = 486
    o.append('<text x="%d" y="76" class="mapx">Six crossings in ten days</text>' % px)
    y = 96
    for (_, _, date, what) in LEGS:
        if not date:
            continue
        o.append('<circle cx="%d" cy="%d" r="3.2" fill="%s"/>' % (px + 4, y - 4, OX))
        o.append('<text x="%d" y="%d" class="mapx">%s</text>' % (px + 16, y, date))
        for line in wrap(what, 26):
            y += 13
            o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px + 16, y, line))
        y += 20
    o.append('<line x1="%d" y1="%d" x2="686" y2="%d" stroke="%s" stroke-width="1"/>'
             % (px, y, y, RULE))
    y += 18
    for line in wrap("The Great Belt was too wide and the ice too broken, so the army went "
                     "round by four islands instead. The ice held for about a fortnight.", 30):
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
        y += 13
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
SKAANE = [(12.45, 56.30), (13.20, 56.60), (14.20, 56.55), (14.55, 56.15),
          (14.30, 55.55), (13.40, 55.35), (12.90, 55.42), (12.55, 55.80)]
HALLAND = [(11.95, 57.70), (12.10, 57.10), (12.30, 56.70), (12.45, 56.30),
           (13.20, 56.60), (13.10, 57.10), (12.90, 57.45), (12.40, 57.55)]
BLEKINGE = [(14.55, 56.15), (14.60, 56.50), (15.60, 56.45), (16.10, 56.25), (15.30, 55.95)]
BOHUSLAN = [(11.30, 58.95), (11.95, 58.92), (12.05, 58.03), (11.92, 57.70),
            (11.50, 57.95), (11.20, 58.45)]
TRONDELAG = [(9.30, 63.05), (11.60, 63.00), (12.60, 64.05), (11.10, 64.55), (8.90, 63.85)]
LBOX = (7.0, 54.6, 17.5, 65.0)
LNEAR = (0.0, 50.0, 30.0, 70.0)
KEPT = [("Skåne", SKAANE), ("Halland", HALLAND), ("Blekinge", BLEKINGE),
        ("Bohuslän", BOHUSLAN)]
BACK = [("Trøndelag", TRONDELAG), ("Bornholm", M97.BORNHOLM)]


def lost1658():
    W, H = 700, 560
    mw, mh = 392, 512
    f = M.detail_frame(LBOX, mw, mh)
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Map of Scandinavia showing the territories Denmark ceded at Roskilde in '
         '1658. Skaane, Halland, Blekinge and Bohuslaen were permanent losses and form the '
         'Danish-Swedish border today. Trondelag and Bornholm were returned at the Peace of '
         'Copenhagen in 1660, both having been retaken by their own inhabitants.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="14" y="24" class="mapl">CEDED AT ROSKILDE, 26 FEBRUARY 1658</text>')
    o.append('<g transform="translate(14,36)">')
    o.extend(M.detail_base(f, mw, mh, LNEAR, scale=50, clip="ro"))
    o.append(land_clip(f, M.land(50), LNEAR, mw, mh, "rol"))
    for name, poly in KEPT:
        d = f.path(poly, close=True)
        if d:
            o.append('<g clip-path="url(#rol)"><path d="%s" fill="%s" fill-opacity=".58" '
                     'stroke="%s" stroke-width="1.1"/></g>' % (d, OX, OX))
    for name, poly in BACK:
        d = f.path(poly, close=True)
        if d:
            o.append('<g clip-path="url(#rol)"><path d="%s" fill="%s" fill-opacity=".30" '
                     'stroke="%s" stroke-width="1.3" stroke-dasharray="4 3"/></g>'
                     % (d, VERD, VERD))
    for lon, lat, t, a, c in [(8.6, 61.4, "NORGE", "middle", "mapl"),
                              (10.2, 56.3, "DANMARK", "middle", "mapl"),
                              (15.6, 60.0, "SVERIGE", "middle", "mapl"),
                              (13.6, 55.6, "Sk\u00e5ne", "middle", "mapt"),
                              (11.62, 57.30, "Halland", "end", "mapt"),
                              (16.4, 56.2, "Blekinge", "start", "mapt"),
                              (10.7, 58.7, "Bohusl\u00e4n", "end", "mapt"),
                              (13.2, 63.9, "Tr\u00f8ndelag", "start", "mapt"),
                              (15.4, 54.9, "Bornholm", "start", "mapt")]:
        x, y = f.xy(lon, lat)
        o.append('<text x="%.1f" y="%.1f" class="%s" text-anchor="%s">%s</text>'
                 % (x, y, c, a, t))
    o.append('</g>')
    o.append('</g>')

    px = 424
    o.append('<rect x="%d" y="52" width="16" height="11" fill="%s" fill-opacity=".58" '
             'stroke="%s" stroke-width="1.1"/>' % (px, OX, OX))
    o.append('<text x="%d" y="62" class="mapx">Lost for good</text>' % (px + 24))
    y = 82
    for line in wrap("Sk\u00e5ne, Halland, Blekinge and Bohusl\u00e4n. The line drawn here is "
                     "the Danish\u2013Swedish border today. Sk\u00e5ne alone held something "
                     "near a third of the realm's people.", 30):
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
        y += 13
    y += 20
    o.append('<rect x="%d" y="%d" width="16" height="11" fill="%s" fill-opacity=".30" '
             'stroke="%s" stroke-width="1.3" stroke-dasharray="4 3"/>' % (px, y - 9, VERD, VERD))
    o.append('<text x="%d" y="%d" class="mapx">Returned in 1660</text> ' % (px + 24, y))
    y += 20
    for line in wrap("Tr\u00f8ndelag and Bornholm. Neither was recovered by treaty first: both "
                     "were taken back by the people living in them, and the treaty followed.", 30):
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
        y += 13
    y += 22
    o.append('<line x1="%d" y1="%d" x2="686" y2="%d" stroke="%s" stroke-width="1"/>'
             % (px, y, y, RULE))
    y += 18
    for line in wrap("Denmark also gave up the right to bar foreign fleets from the Baltic, and "
                     "undertook to pay for the Swedish army to leave.", 30):
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
        y += 13
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
# (months after June 1657, label, detail, above?)
EVENTS = [
    (0, "Jun 1657", "Denmark declares war", True),
    (1, "Jul 1657", "Karl Gustav leaves Poland", False),
    (4, "24 Oct 1657", "Frederiksodde stormed", True),
    (7, "30 Jan 1658", "the Little Belt", False),
    (8, "5\u20138 Feb 1658", "four islands to Zealand", True),
    (8.7, "26 Feb 1658", "Roskilde", False),
    (14, "Aug 1658", "Sweden attacks again", True),
    (16, "29 Oct 1658", "Dutch force the Sound", False),
    (18, "8 Dec 1658", "Bornholm rises", True),
    (20, "11 Feb 1659", "the storm fails", False),
    (29, "14 Nov 1659", "Nyborg", True),
    (32, "13 Feb 1660", "Karl Gustav dies", False),
    (35, "27 May 1660", "Peace of Copenhagen", True),
    (39, "Sep\u2013Oct 1660", "the estates; hereditary crown", False),
]
SPAN = 40.0


def collapse():
    W = 700
    rows = len(EVENTS)
    top, gap = 74, 31
    H = top + rows * gap + 76
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Fourteen events between June 1657 and October 1660. A time ribbon on the '
         'left places each at its true distance in months; the list on the right gives each equal '
         'space, and lines connect the two. The events cluster: the march across the ice and the '
         'Treaty of Roskilde fall within five weeks of each other in early 1658.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="28" class="mapl">THIRTY-TWO MONTHS</text>')
    o.append('<text x="26" y="44" class="mapt">left: real elapsed time \u2014 right: equal '
             'space, so the labels can be read</text>')

    t0, t1 = top, top + (rows - 1) * gap

    def T(m):
        return t0 + (t1 - t0) * m / SPAN

    o.append('<line x1="60" y1="%d" x2="60" y2="%d" stroke="%s" stroke-width="1.4"/>'
             % (t0 - 12, t1 + 12, MUTED))
    o.append('<rect x="47" y="%.1f" width="26" height="%.1f" fill="%s" opacity=".22"/>'
             % (T(7), T(8.7) - T(7), OX))
    for yr, m in (("1657", 0), ("1658", 7), ("1659", 19), ("1660", 31)):
        o.append('<text x="44" y="%.1f" class="mapt" text-anchor="end">%s</text>' % (T(m) + 3, yr))
        o.append('<line x1="54" y1="%.1f" x2="66" y2="%.1f" stroke="%s" stroke-width=".8" '
                 'opacity=".7"/>' % (T(m), T(m), MUTED))

    for i, (m, date, what, _) in enumerate(EVENTS):
        y = top + i * gap
        o.append('<path d="M 68 %.1f C 110 %.1f, 140 %.1f, 182 %.1f" fill="none" stroke="%s" '
                 'stroke-width="1" opacity=".5"/>' % (T(m), T(m), y, y, OX))
        o.append('<circle cx="60" cy="%.1f" r="3" fill="%s"/>' % (T(m), OX))
        o.append('<circle cx="186" cy="%d" r="3" fill="%s"/>' % (y, OX))
        o.append('<text x="200" y="%d" class="mapx">%s</text>' % (y + 4, date))
        o.append('<text x="320" y="%d" class="mapt">%s</text>' % (y + 4, what))

    b = t1 + 44
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    o.append('<text x="26" y="%d" class="mapt">The shaded band is five weeks: the Little Belt on '
             '30 January, four islands to Zealand by 8 February,</text>' % (b + 20))
    o.append('<text x="26" y="%d" class="mapt">and Roskilde signed on 26 February. A third of the '
             'realm went in that band.</text>' % (b + 34))
    o.append('</svg>')
    return "\n  ".join(o)


if __name__ == "__main__":
    for name, fn in (("svg_icemarch.txt", icemarch),
                     ("svg_lost1658.txt", lost1658),
                     ("svg_collapse.txt", collapse)):
        svg = fn()
        validate(svg, name)
        import re
        w = int(re.search(r'viewBox="0 0 (\d+)', svg).group(1))
        bad = overruns(svg, w)
        if bad:
            print("   ! overruns in %s: %s" % (name, bad))
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
