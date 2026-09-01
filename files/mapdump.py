# -*- coding: utf-8 -*-
"""mapdump.py - pull every spine map out of the built pages so it can be looked at.

    python3 mapdump.py          # writes maps-contact-sheet.html; open it in a browser

No dependencies. The earlier version rasterised with cairosvg, which on macOS
wants the cairo C library installed; the SVG is already in the page, so it only
needs lifting out and giving somewhere to render.

The sheet shows each map twice: whole, and zoomed to the Kongea and the Eider,
which is where the August 2026 seam bug printed. Two translucent fills laid over
each other print strictly darker than either alone, so a seam shows as a band of
darker green along a border.

WHY LOOKING, AND NOT A CHECKER
------------------------------
seamcheck.py tests polygons and is exact, but it can only see maps that still
have a map_YYYY.py. Chapters 01-15 carry spine maps whose scripts no longer exist
- map_1050.py and map_1250.py are gone, and Part D's bodies with them.

Five attempts at detecting the fault automatically inside a built page were all
wrong: matching the composite colour caught coastline strokes lying under a fill,
13 units from a real overlap; testing polygon vertices missed it, because the
offending vertices sit over water even when the lens between the lines is over
land; isolating each <path> lost its enclosing <g clip-path> and <g transform>
and so measured geometry rather than ink; and probing pixels along the border hit
labels, dots and dashed strokes, all darker than any overlap. A built page is a
picture, and inferring geometry back out of it buys false confidence. The eye
finds this in about a second.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.environ.get("DK_CHAPTERS") or os.path.dirname(HERE) or os.getcwd()
ZOOM = "120 430 250 250"          # southern Jutland and the duchies, in frame px

CSS = """
.mapt{font-family:ui-monospace,Menlo,monospace;font-size:9.5px;fill:#5F6157}
.mapl{font-family:ui-monospace,Menlo,monospace;font-size:10.5px;fill:#3C3E36;font-weight:600}
.mapx{font-family:ui-monospace,Menlo,monospace;font-size:8.5px;fill:#4A4C44}
body{background:#F0F2EE;color:#3C3E36;margin:0;padding:28px 32px;
     font-family:ui-monospace,Menlo,monospace;font-size:12px}
h1{font-size:15px;letter-spacing:.08em;margin:0 0 4px}
p.note{color:#5F6157;max-width:74ch;line-height:1.5}
section{border-top:1px solid #C9CDC4;margin-top:26px;padding-top:14px}
h2{font-size:12px;letter-spacing:.06em;margin:0 0 2px}
h2 span{color:#5F6157;font-weight:400}
.pair{display:flex;gap:22px;align-items:flex-start;flex-wrap:wrap}
.pair figure{margin:0}
.pair figcaption{color:#5F6157;margin-top:4px}
svg{background:#F0F2EE;border:1px solid #C9CDC4}
"""


def spine_maps(html):
    for m in re.finditer(r"<svg\b.*?</svg>", html, re.S):
        s = m.group(0)
        if 'viewBox="0 0 660 700"' in s:
            lab = re.search(r'aria-label="([^"]{0,150})', s)
            yield s, (lab.group(1) if lab else "")


def resize(svg, w, h, viewbox=None):
    head = re.match(r"<svg\b[^>]*>", svg).group(0)
    new = head
    if viewbox:
        new = re.sub(r'viewBox="[^"]*"', 'viewBox="%s"' % viewbox, new)
    new = re.sub(r'\s(?:width|height)="[^"]*"', "", new)
    new = new[:-1] + ' width="%d" height="%d">' % (w, h)
    return new + svg[len(head):]


def main():
    pages = sorted(f for f in os.listdir(DIR)
                   if re.match(r"^\d\d[-.]", f) and f.endswith(".html"))
    if not pages:
        raise SystemExit("no chapter pages found in %s" % DIR)

    out = ["<!DOCTYPE html><html><head><meta charset='utf-8'>",
           "<title>Spine maps &mdash; seam inspection</title>",
           "<style>%s</style></head><body>" % CSS,
           "<h1>SPINE MAPS, AS SHIPPED</h1>",
           "<p class='note'>Each map whole, then zoomed to southern Jutland and the "
           "duchies. Two translucent fills laid over each other print strictly darker "
           "than either alone, so a seam shows as a darker band along a border &mdash; "
           "look at the Konge&aring; between Denmark and Slesvig, and at the Eider "
           "between Slesvig and Ditmarschen. Maps with a surviving "
           "<code>map_YYYY.py</code> are already checked exactly by "
           "<code>seamcheck.py</code>; these are the ones that are not.</p>"]

    n = 0
    for f in pages:
        html = open(os.path.join(DIR, f), encoding="utf-8", errors="replace").read()
        for k, (svg, lab) in enumerate(spine_maps(html), 1):
            n += 1
            out.append("<section><h2>%s <span>&mdash; map %d</span></h2>"
                       "<p class='note'>%s</p><div class='pair'>" % (f, k, lab))
            out.append("<figure>%s<figcaption>whole</figcaption></figure>"
                       % resize(svg, 330, 350))
            out.append("<figure>%s<figcaption>Konge&aring; and Eider</figcaption></figure>"
                       % resize(svg, 460, 460, ZOOM))
            out.append("</div></section>")

    out.append("<p class='note' style='margin-top:30px'>%d spine map(s) found in %d "
               "page(s).</p></body></html>" % (n, len(pages)))
    dest = os.path.join(DIR, "maps-contact-sheet.html")
    open(dest, "w", encoding="utf-8").write("\n".join(out))
    print("wrote %s" % dest)
    print("%d spine map(s) from %d pages. Open it and look at the two borders."
          % (n, len(pages)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
