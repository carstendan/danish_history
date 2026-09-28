# -*- coding: utf-8 -*-
"""What collisions() cannot see: a line or a shape printed through a text.

Render the figure with its text removed, then look inside every text box: if
the box is not one flat ground (land, sea or paper), something is drawn through
where the text will sit - a coastline, an attack line, a marker. Reports the
share of the box that is not the box's dominant colour.

usage: python3 linecheck.py svg_crowns.txt [svg_hemming.txt ...]   (from files/)

Review session 15. mapspine.collisions() compares text with text, so a coastline, an
attack line or a marker printed through a label passes it; that is how fig_crowns.py
shipped "1" over "Lindholmen" and København and Flensborg crossed by coastline, and
figs_18.py "the bank" crossed by an attack line. This is AN AID TO LOOKING, NOT A GUARD:
it is wired into nothing, because a label that sits on purpose across a border or a
tinted territory is flagged too (220 texts in 31 figures over every svg_*.txt after this
session's two fixes, most of them on the territorial maps). Read what it lists against the PNG.
"""
import re, sys, io
sys.path.insert(0, ".")
import mapspine as M


def crossings(svg, name, floor=0.03, scale=2):
    import cairosvg
    from PIL import Image
    bare = re.sub(r'<text\b[^>]*>.*?</text>', '', svg, flags=re.S)
    vb = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"', svg)
    ox, oy = float(vb.group(1)), float(vb.group(2))
    png = cairosvg.svg2png(bytestring=bare.encode("utf-8"), scale=scale)
    im = Image.open(io.BytesIO(png)).convert("RGB")
    W, H = im.size
    # a numeral printed on its own marker is not a crossing
    discs = [(float(a), float(b), float(r)) for a, b, r in re.findall(
        r'<circle cx="([\d.-]+)" cy="([\d.-]+)" r="([\d.]+)"', svg) if float(r) >= 4]
    bad = []
    for x0, y0, x1, y1, cls, t in M.text_boxes(svg):
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        if any((cx - a) ** 2 + (cy - b) ** 2 <= r * r for a, b, r in discs) and len(t) <= 2:
            continue
        # shrink the generous estimate a little: the guard is for real crossings
        bx0, bx1 = int((x0 - ox + 1) * scale), int((x1 - ox - 1) * scale)
        by0, by1 = int((y0 - oy + 1.5) * scale), int((y1 - oy - 0.5) * scale)
        bx0, by0 = max(bx0, 0), max(by0, 0)
        bx1, by1 = min(bx1, W), min(by1, H)
        if bx1 <= bx0 or by1 <= by0:
            continue
        px = list(im.crop((bx0, by0, bx1, by1)).get_flattened_data()) if hasattr(im, 'get_flattened_data') else list(im.crop((bx0, by0, bx1, by1)).getdata())
        counts = {}
        for p in px:
            k = (p[0] // 6, p[1] // 6, p[2] // 6)
            counts[k] = counts.get(k, 0) + 1
        top = sorted(counts.values(), reverse=True)
        # two flat grounds (a label half on land, half on sea) is itself a crossing
        other = 1 - top[0] / len(px)
        if other > floor:
            bad.append((t[:40], other))
    for t, o in bad:
        print("   ! %s: something drawn through the text (%.0f%% of its box): %r" % (name, 100 * o, t))
    return bad


if __name__ == "__main__":
    n = 0
    for p in sys.argv[1:]:
        n += len(crossings(open(p, encoding="utf-8").read(), p))
    print("%d text(s) crossed" % n)
