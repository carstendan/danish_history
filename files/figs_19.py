# -*- coding: utf-8 -*-
"""Figures for chapter 19."""
import mapspine as M

PART_E = "#2E6B5E"
INK = "#221E18"
MUTED = "#6C6E63"
RULE = "#C9CDC4"
OX = "#8A2B2B"
AMBER = "#A9601C"


def t(x, y, s, cls="mapx", fill=MUTED, anchor="start", extra=""):
    return ('<text x="%.1f" y="%.1f" class="%s" fill="%s" text-anchor="%s"%s>%s</text>'
            % (x, y, cls, fill, anchor, extra, s))


# ------------------------------------------------------------------ figure 1
def feud():
    BBOX = (7.6, 54.5, 14.2, 57.9)
    W, H, STRIP = 660, 600, 116
    NEAR = (5.0, 53.0, 17.0, 59.5)
    f = M.detail_frame(BBOX, W, H)
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Map of Denmark during the Count\'s Feud, 1534 to 1536. Count Christoffer '
         'lands on Zealand in June 1534 and takes Zealand and Skaane. Skipper Clement raises the '
         'peasants of North Jutland and beats the nobility at Svenstrup in October 1534. Johan '
         'Rantzau marches north through Jutland, storms Aalborg in December 1534, crosses to Funen '
         'and wins at Oeksnebjerg in June 1535, then besieges Copenhagen until July 1536. Also '
         'marked are the towns where evangelical preaching began: Haderslev, Viborg, Malmoe and '
         'Copenhagen.">' % (W, H + STRIP)]
    o += M.detail_base(f, W, H, NEAR)

    # Rantzau's campaign
    RANTZAU = [(9.75, 54.90), (8.90, 55.55), (8.75, 56.20), (9.20, 56.45), (9.40, 56.45),
               (9.75, 56.85), (9.93, 57.05)]
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" opacity=".9"/>'
             % (f.path(RANTZAU, close=False), PART_E))
    FYN = [(9.90, 54.90), (10.08, 55.27), (10.39, 55.40), (11.20, 55.35), (12.30, 55.55),
           (12.55, 55.68)]
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-dasharray="7 5" '
             'opacity=".9"/>' % (f.path(FYN, close=False), PART_E))
    # the count's landing
    LAND = [(11.60, 54.75), (12.20, 55.30), (12.55, 55.68), (13.00, 55.60)]
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-dasharray="3 4" '
             'opacity=".9"/>' % (f.path(LAND, close=False), OX))

    # preaching towns, the quieter layer
    for lon, lat, name, year, anchor in [
            (9.49, 55.25, "Haderslev", "1528", "end"),
            (9.40, 56.45, "Viborg", "1526", "end"),
            (13.00, 55.60, "Malm\u00f8", "1529", "start"),
            (10.39, 55.40, "Odense", "1527", "start")]:
        x, y = f.xy(lon, lat)
        dx = 5 if anchor == "start" else -5
        o.append('<circle cx="%.1f" cy="%.1f" r="4.6" fill="none" stroke="%s" '
                 'stroke-width="1.4"/>' % (x, y, AMBER))
        o.append('<text x="%.1f" y="%.1f" class="mapx" fill="%s" text-anchor="%s">%s %s</text>'
                 % (x + dx, y - 7, AMBER, anchor, name, year))

    for lon, lat, name, note, anchor, dy in [
            (9.93, 57.05, "Aalborg", "stormed 18 Dec 1534", "start", -10),
            (9.85, 56.93, "Svenstrup", "16 Oct 1534", "end", 12),
            (10.08, 55.27, "\u00d8ksnebjerg", "11 June 1535", "start", 0),
            (12.57, 55.68, "K\u00f8benhavn", "besieged to 29 July 1536", "end", -12)]:
        x, y = f.xy(lon, lat)
        dx = 6 if anchor == "start" else -6
        o.append('<circle cx="%.1f" cy="%.1f" r="3.2" fill="%s"/>' % (x, y, INK))
        o.append('<text x="%.1f" y="%.1f" class="mapl" text-anchor="%s">%s</text>'
                 % (x + dx, y + dy + 3.4, anchor, name))
        o.append('<text x="%.1f" y="%.1f" class="mapx" text-anchor="%s">%s</text>'
                 % (x + dx, y + dy + 16, anchor, note))
    o.append('</g>')

    o.append('<rect x="0" y="%d" width="%d" height="%d" fill="%s"/>' % (H, W, STRIP, M.PAPER))
    o.append('<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width=".8"/>'
             % (H, W, H, M.LAND_EDGE))
    for i, (col, dash, lab) in enumerate([
            (OX, "3 4", "Count Christoffer, June 1534 \u2014 Zealand and Sk\u00e5ne in six weeks"),
            (PART_E, "", "Rantzau north through Jutland, autumn 1534"),
            (PART_E, "7 5", "Rantzau to Funen and Zealand, 1535\u201336"),
            (AMBER, "dot", "where evangelical preaching began, with the year")]):
        y = H + 26 + i * 21
        if dash == "dot":
            o.append('<circle cx="30" cy="%d" r="4.6" fill="none" stroke="%s" '
                     'stroke-width="1.4"/>' % (y - 4, col))
        else:
            o.append('<line x1="18" y1="%d" x2="44" y2="%d" stroke="%s" stroke-width="2.4"%s/>'
                     % (y - 4, y - 4, col, ' stroke-dasharray="%s"' % dash if dash else ''))
        o.append(t(56, y, lab, "mapx", MUTED))
    o.append('</svg>')
    return "\n  ".join(o), W, H + STRIP


# ------------------------------------------------------------------ figure 2
def transfer():
    W, H = 900, 486
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Two diagrams of what the Reformation transferred. Above, the share of Danish '
         'land held by crown, church, nobility and freeholding peasants before and after 1536: the '
         'church\'s roughly one third passes to the crown, which goes from about a sixth to about '
         'half. Below, the Danish tithe, which was divided in three between bishop, parish priest '
         'and church fabric: after 1536 the crown takes the bishop\'s third.">' % (W, H),
         '<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, M.PAPER)]

    o.append(t(26, 34, "WHO HELD THE LAND", "mapt", PART_E))
    o.append(t(700, 34, "shares, roughly", "mapt", MUTED))

    bars = [("BEFORE 1536", 70, [("Crown", 16, PART_E, .45), ("Church", 33, OX, .55),
                                 ("Nobility", 43, INK, .30), ("Free peasants", 8, AMBER, .45)]),
            ("AFTER 1536", 160, [("Crown", 49, PART_E, .78), ("Nobility", 43, INK, .30),
                                 ("Free peasants", 8, AMBER, .45)])]
    for lab, y, segs in bars:
        o.append(t(26, y + 16, lab, "mapl", INK))
        x = 190
        for name, pct, col, op in segs:
            w = pct * 6.6
            o.append('<rect x="%.1f" y="%d" width="%.1f" height="34" fill="%s" fill-opacity="%s" '
                     'stroke="%s" stroke-width=".8"/>' % (x, y, w, col, op, col))
            if w > 60:
                o.append(t(x + w / 2, y + 16, name, "mapx", INK, "middle"))
                o.append(t(x + w / 2, y + 28, "~%d%%" % pct, "mapx", MUTED, "middle"))
            x += w
    o.append('<path d="M 296 108 L 296 152" stroke="%s" stroke-width="1.6" '
             'stroke-dasharray="4 3"/>' % OX)
    o.append(t(304, 134, "the church's third, transferred", "mapx", OX))
    o.append(t(874, 216, "the last sliver is freeholding peasants,", "mapx", MUTED, "end"))
    o.append(t(874, 230, "about 8 per cent, and shrinking", "mapx", MUTED, "end"))
    o.append(t(26, 262, "The nobility gained little land in 1536 and a great deal of security: no "
               "more bishops in the council, and a crown that owed them the war.", "mapx", MUTED))

    o.append('<line x1="26" y1="288" x2="%d" y2="288" stroke="%s" stroke-width=".8"/>'
             % (W - 26, RULE))
    o.append(t(26, 312, "AND THE TITHE", "mapt", PART_E))
    o.append(t(26, 334, "Chapter 12 established that the Danish tithe was divided three ways, not "
               "four: there was no share for the poor.", "mapx", MUTED))

    for lab, y, segs in [("BEFORE", 356, [("Bishop", OX, .55), ("Parish priest", INK, .30),
                                          ("Church fabric", AMBER, .45)]),
                         ("AFTER", 412, [("THE CROWN", PART_E, .78), ("Parish priest", INK, .30),
                                         ("Church fabric", AMBER, .45)])]:
        o.append(t(26, y + 20, lab, "mapl", INK))
        for i, (name, col, op) in enumerate(segs):
            x = 190 + i * 220
            o.append('<rect x="%d" y="%d" width="200" height="34" fill="%s" fill-opacity="%s" '
                     'stroke="%s" stroke-width=".8"/>' % (x, y, col, op, col))
            o.append(t(x + 100, y + 21, name, "mapx", INK, "middle"))
    o.append('<path d="M 290 390 L 290 412" stroke="%s" stroke-width="1.6" '
             'stroke-dasharray="4 3"/>' % OX)
    o.append('</svg>')
    return "\n  ".join(o), W, H


# ------------------------------------------------------------------ figure 3
def weeks():
    W, H = 900, 300
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Timeline of twelve weeks in 1536: Copenhagen surrenders on 29 July, the '
         'bishops are arrested on 12 August, and the assembly of 30 October transfers the church '
         'to the crown and declares that Norway shall be a limb of Denmark.">' % (W, H),
         '<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, M.PAPER)]
    o.append(t(26, 34, "TWELVE WEEKS", "mapt", PART_E))
    o.append('<text x="26" y="62" style="font-family:\'Iowan Old Style\',Palatino,Georgia,serif;'
             'font-size:19px;fill:%s">A siege ends, and a church is nationalised.</text>' % INK)

    o.append('<line x1="60" y1="118" x2="760" y2="118" stroke="%s" stroke-width="1.4"/>' % MUTED)
    stops = [(60, "29 July", ["Copenhagen surrenders after", "a year. The city has been", "eating horses."]),
             (320, "12 August", ["The bishops are arrested on", "one night, in a coup agreed", "with the nobility."]),
             (500, "30 October", ["The assembly transfers all", "church property to the crown", "and abolishes the bishops."]),
             (720, "1537", ["Bugenhagen crowns the", "king and ordains seven", "superintendents."])]
    for x, date, lines in stops:
        o.append('<circle cx="%d" cy="118" r="6" fill="%s"/>' % (x, PART_E))
        o.append(t(x, 100, date, "mapl", PART_E))
        for i, l in enumerate(lines):
            o.append(t(x, 142 + i * 15, l, "mapx", MUTED))
    o.append('<line x1="26" y1="212" x2="%d" y2="212" stroke="%s" stroke-width=".8"/>'
             % (W - 26, RULE))
    o.append(t(26, 240, "In the same recess: \u2018Norway shall hereafter be and remain under the "
               "crown of Denmark, like one of the other lands,", "mapx", MUTED))
    o.append(t(26, 256, "Jutland, Funen, Zealand or Sk\u00e5ne.\u2019 It was not enforced as written, "
               "and Norway kept its own law \u2014 but the sentence stood", "mapx", MUTED))
    o.append(t(26, 272, "in the constitution of the realm until 1814, and Norwegians have never "
               "stopped quoting it.", "mapx", MUTED))
    o.append('</svg>')
    return "\n  ".join(o), W, H


if __name__ == "__main__":
    for name, fn in [("svg_feud", feud), ("svg_transfer", transfer), ("svg_weeks", weeks)]:
        svg, w, h = fn()
        open(name + ".txt", "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.split("_")[1] + ".png")
        print("%-14s %d chars  %dx%d" % (name, len(svg), w, h))
