# -*- coding: utf-8 -*-
"""Chapter 23's three figures.

  svg_invasions.txt    the two occupations of Jutland, 1627-29 and 1643-45
  svg_sonsinlaw.txt    the morganatic marriage that became a government
  svg_losses1645.txt   what Broemsebro took

Two of the three are maps, which is one more than a chapter usually wants. The
justification is that they do different jobs at different scales: the first is an
argument about a peninsula and a sea, repeated twice to make the repetition the
point, and the third is a change to a frame the reader already met at the head of
chapter 21. The middle one is a family tree because nothing else shows a claim
travelling sideways.

Run: python3 figs_23.py
"""
import map_1397 as M97
import map_1600 as M16
import mapspine as M

INK = "#3C3E36"
PAPER = "#F0F2EE"
RULE = "#C9CDC4"
OX = "#8A2B2B"
VERD = "#2E6B5E"
AMBER = "#A9601C"
MUTED = "#5F6157"


def land_clip(f, polys, near, w, h, cid):
    return ('<clipPath id="%s"><path d="%s"/></clipPath>'
            % (cid, M.detail_land_path(f, polys, near, w, h)))


# ------------------------------------------------------------------ figure 1
# The occupied ground: the peninsula from the Elbe to Skagen. Both armies came
# the same way and neither crossed water, which is the whole argument.
OCCUPIED = [
    (8.10, 53.60), (9.40, 53.55), (10.20, 53.62), (10.60, 54.10), (10.55, 54.60),
    (10.30, 55.05), (10.10, 55.40), (10.05, 56.00), (10.60, 56.40), (10.85, 57.00),
    (10.60, 57.75), (10.35, 57.30), (9.60, 57.30), (8.60, 57.20), (8.30, 57.00),
    (8.10, 56.40), (8.10, 56.00),
    (8.05, 55.20), (8.35, 54.50),
]
JBOX = (7.4, 53.3, 13.4, 58.2)
JNEAR = (2.0, 50.0, 20.0, 62.0)


def invasions():
    W, H = 700, 452
    pw, ph = 322, 372
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Two maps of Denmark side by side. In 1627 to 1629 imperial armies under '
         'Tilly and Wallenstein occupied the Jutland peninsula from the Elbe to Skagen. In 1643 '
         'to 1645 a Swedish army under Torstensson occupied the same ground by the same route. '
         'In neither war were Zealand, Funen or Scania touched, because the Danish fleet held the '
         'water.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))

    panels = [(14, "1627\u201329", "Tilly and Wallenstein", OX, True),
              (364, "1643\u201345", "Torstensson", VERD, False)]
    for px, years, who, col, glueck in panels:
        f = M.detail_frame(JBOX, pw, ph)
        o.append('<text x="%d" y="24" class="mapl">%s</text>' % (px, years))
        o.append('<text x="%d" y="40" class="mapt">%s</text>' % (px, who))
        o.append('<g transform="translate(%d,52)">' % px)
        o.extend(M.detail_base(f, pw, ph, JNEAR, scale=50, clip="p%s" % years[:4]))
        o.append(land_clip(f, M.land(50), JNEAR, pw, ph, "l%s" % years[:4]))
        d = f.path(OCCUPIED, close=True)
        o.append('<g clip-path="url(#l%s)"><path d="%s" fill="%s" fill-opacity=".45"/></g>'
                 % (years[:4], d, col))
        # the route: up the peninsula from the Elbe
        ax, ay = f.xy(9.6, 53.8)
        bx, by = f.xy(9.8, 57.0)
        o.append('<path d="M %.1f %.1f C %.1f %.1f, %.1f %.1f, %.1f %.1f" fill="none" '
                 'stroke="%s" stroke-width="2.2" opacity=".85"/>'
                 % (ax, ay, ax - 14, (ay + by) / 2.0, bx + 14, (ay + by) / 2.0, bx, by, col))
        o.append('<path d="M %.1f %.1f l -4.5 9 l 9 0 Z" fill="%s"/>' % (bx, by - 9, col))
        if glueck:
            gx, gy = f.xy(9.43, 53.79)
            o.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s" stroke="%s" '
                     'stroke-width="1.6"/>' % (gx, gy, PAPER, INK))
            o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="end">Gl\u00fcckstadt '
                     'held</text>' % (gx - 9, gy - 5))
        for lon, lat, t, a in [(11.85, 55.55, "never occupied", "middle"),
                               (13.0, 55.9, "", "middle")]:
            if t:
                x, y = f.xy(lon, lat)
                o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="%s">%s</text>'
                         % (x, y, a, t))
        o.append('</g>')      # close detail_base clip group
        o.append('</g>')      # close translate

    b = 52 + ph + 24
    o.append('<line x1="14" y1="%d" x2="686" y2="%d" stroke="%s" stroke-width="1"/>'
             % (b - 14, b - 14, RULE))
    o.append('<text x="14" y="%d" class="mapt">Sixteen years apart, two different enemies took '
             'the same ground by the same road.</text>' % b)
    o.append('<text x="14" y="%d" class="mapt">Neither crossed the water, and neither had to: '
             'taking Jutland was enough to dictate terms both times.</text>' % (b + 14))
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 2
DAUGHTERS = [
    ("Anne Cathrine", "1618\u201333", "Frands Rantzau", ""),
    ("Sophie Elisabeth", "1619\u201357", "Christian von Pentz", "governor, Gl\u00fcckstadt"),
    ("Leonora Christina", "1621\u201398", "Corfitz Ulfeldt", "steward of the realm 1643"),
    ("Elisabeth Augusta", "1623\u201377", "Hans Lindenov", ""),
    ("Christiane", "1626\u201370", "Hannibal Sehested", "governor of Norway 1642"),
]


def sonsinlaw():
    W, H = 700, 452
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Family diagram. Christian the Fourth\'s first marriage produced Frederik the '
         'Third, who inherited the throne in 1648. His second, morganatic marriage to Kirsten Munk '
         'produced daughters who could not inherit, but who married five of the greatest noblemen '
         'in Denmark, including Corfitz Ulfeldt, steward of the realm, and Hannibal Sehested, '
         'governor of Norway.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="28" class="mapl">ONE KING, TWO MARRIAGES, TWO KINDS OF CLAIM</text>')

    o.append('<rect x="286" y="46" width="128" height="30" rx="3" fill="%s" opacity=".14"/>'
             % INK)
    o.append('<text x="350" y="66" class="mapl" text-anchor="middle">Christian 4.</text>')

    # left: the succession, straight down
    # the descender used to run to y=126 and struck through the label at y=122
    o.append('<path d="M 330 76 L 330 100 L 150 100" fill="none" stroke="%s" '
             'stroke-width="1.2"/>' % MUTED)
    o.append('<text x="150" y="118" class="mapt" text-anchor="middle">Anne Catherine, m. 1597'
             '</text>')
    o.append('<path d="M 150 126 L 150 158" fill="none" stroke="%s" stroke-width="1.2"/>' % MUTED)
    o.append('<rect x="86" y="160" width="128" height="30" rx="3" fill="%s" opacity=".18"/>'
             % VERD)
    o.append('<text x="150" y="180" class="mapl" text-anchor="middle">Frederik 3.</text>')
    o.append('<text x="150" y="206" class="mapt" text-anchor="middle">king, 1648</text>')
    o.append('<text x="150" y="220" class="mapt" text-anchor="middle">the claim goes down</text>')

    # right: the morganatic line, turning sideways
    # The spine drops on the LEFT of the rows. Running it down the right meant
    # every connector crossed its own row and struck the names through.
    o.append('<path d="M 370 76 L 370 100 L 470 100" fill="none" stroke="%s" '
             'stroke-width="1.2"/>' % OX)
    o.append('<text x="470" y="118" class="mapt" text-anchor="middle">Kirsten Munk, m. 1615 '
             '\u2014 morganatic</text>')
    o.append('<text x="470" y="134" class="mapt" text-anchor="middle">twelve children; no claim '
             'to the throne</text>')

    top = 182
    o.append('<path d="M 470 142 L 470 160 L 250 160 L 250 %d" fill="none" stroke="%s" '
             'stroke-width="1.2"/>' % (top + (len(DAUGHTERS) - 1) * 42 - 8, OX))
    for i, (name, yrs, husband, office) in enumerate(DAUGHTERS):
        y = top + i * 42
        o.append('<path d="M 250 %d L 262 %d" fill="none" stroke="%s" stroke-width="1"/>'
                 % (y - 8, y - 8, OX))
        o.append('<circle cx="262" cy="%d" r="4" fill="%s"/>' % (y - 8, OX))
        o.append('<text x="274" y="%d" class="mapx">%s</text>' % (y - 4, name))
        o.append('<text x="274" y="%d" class="mapt">%s</text>' % (y + 9, yrs))
        o.append('<text x="424" y="%d" class="mapx">m. %s</text>' % (y - 4, husband))
        if office:
            o.append('<text x="424" y="%d" class="mapt">%s</text>' % (y + 9, office))

    b = top + len(DAUGHTERS) * 42 + 12
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>' % (b, b, RULE))
    o.append('<text x="26" y="%d" class="mapt">Barred from the succession, the claim travelled '
             'sideways instead \u2014 through their husbands\' offices.</text>' % (b + 18))
    o.append('<text x="26" y="%d" class="mapt">From 1648 to 1651 these men were the government '
             'of Denmark.</text>' % (b + 32))
    o.append('</svg>')
    return "\n  ".join(o)


# ------------------------------------------------------------------ figure 3
HALLAND = [(11.95, 57.70), (12.10, 57.10), (12.30, 56.70), (12.45, 56.30),
           (13.20, 56.60), (13.10, 57.10), (12.90, 57.45), (12.40, 57.55)]
JAMTLAND = [(12.10, 61.30), (13.05, 61.90), (14.45, 62.20), (14.65, 62.90),
            (15.45, 63.60), (14.35, 64.40), (13.10, 63.70), (12.30, 62.40)]
SBOX = (8.0, 54.4, 25.0, 65.5)
SNEAR = (0.0, 50.0, 34.0, 70.0)
CEDED = [("J\u00e4mtland &amp; H\u00e4rjedalen", JAMTLAND, "from Norway, held 600 years"),
         ("Gotland", M97.GOTLAND, "Danish since 1449"),
         ("\u00d6sel", M16.OESEL, "bought 1559"),
         ("Halland", HALLAND, "pledged 30 years; never returned")]


def losses1645():
    W, H = 700, 556
    pw, ph = 384, 512
    f = M.detail_frame(SBOX, pw, ph)
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Map of Scandinavia marking the territories Denmark ceded at Broemsebro in '
         '1645: Jaemtland and Haerjedalen from Norway, the islands of Gotland and Oesel, and '
         'Halland pledged for thirty years and never returned.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="14" y="24" class="mapl">CEDED AT BR\u00d8MSEBRO, 13 AUGUST 1645</text>')
    o.append('<g transform="translate(14,36)">')
    o.extend(M.detail_base(f, pw, ph, SNEAR, scale=50, clip="br"))
    o.append(land_clip(f, M.land(50), SNEAR, pw, ph, "brl"))
    for name, poly, _ in CEDED:
        d = f.path(poly, close=True)
        if d:
            o.append('<g clip-path="url(#brl)"><path d="%s" fill="%s" fill-opacity=".55" '
                     'stroke="%s" stroke-width="1.2"/></g>' % (d, OX, OX))
    for lon, lat, t, a in [(9.2, 61.6, "NORGE", "middle"), (10.6, 56.0, "DANMARK", "middle"),
                           (19.2, 60.3, "SVERIGE", "middle")]:
        x, y = f.xy(lon, lat)
        o.append('<text x="%.1f" y="%.1f" class="mapl" text-anchor="%s">%s</text>' % (x, y, a, t))
    for lon, lat, t, a in [(16.4, 63.3, "J\u00e4mtland &amp;", "start"),
                           (16.4, 62.8, "H\u00e4rjedalen", "start"),
                           (19.9, 57.6, "Gotland", "start"),
                           (23.5, 58.4, "\u00d6sel", "start"),
                           (11.65, 57.05, "Halland", "end")]:
        x, y = f.xy(lon, lat)
        o.append('<text x="%.1f" y="%.1f" class="mapt" text-anchor="%s" fill="%s">%s</text>'
                 % (x, y, a, OX, t))
    o.append('</g>')
    o.append('</g>')

    px = 424
    y = 60
    for i, (name, poly, why) in enumerate(CEDED):
        o.append('<text x="%d" y="%d" class="mapx" fill="%s">%s</text>' % (px, y, OX, name))
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y + 14, why))
        y += 44

    y += 12
    o.append('<line x1="%d" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (px, y, y, RULE))
    y += 22
    o.append('<text x="%d" y="%d" class="mapx">And one clause with no map</text>' % (px, y))
    for line in ["Swedish shipping exempted from the",
                 "Sound toll. The charge Erik of Pomerania",
                 "invented in 1429 was now something",
                 "another state could negotiate a share of",
                 "rather than a fact of geography."]:
        y += 14
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (px, y, line))
    y += 26
    o.append('<text x="%d" y="%d" class="mapt">Outlines are approximate: J\u00e4mtland and</text>'
             % (px, y))
    o.append('<text x="%d" y="%d" class="mapt">H\u00e4rjedalen had no surveyed border.</text>'
             % (px, y + 14))
    o.append('</svg>')
    return "\n  ".join(o)


def validate(svg, name):
    """Parse before writing. A bare & in a label produces a file that looks fine
    in the editor and fails at the rasteriser, after it has already been saved."""
    import xml.etree.ElementTree as ET
    try:
        ET.fromstring(svg)
    except ET.ParseError as e:
        line = svg.splitlines()[e.position[0] - 1][:120]
        raise SystemExit("!! %s is not well-formed XML at line %d: %s"
                         % (name, e.position[0], line))


if __name__ == "__main__":
    for name, fn in (("svg_invasions.txt", invasions),
                     ("svg_sonsinlaw.txt", sonsinlaw),
                     ("svg_losses1645.txt", losses1645)):
        svg = fn()
        validate(svg, name)
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
