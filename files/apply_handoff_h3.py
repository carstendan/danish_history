# -*- coding: utf-8 -*-
"""apply_handoff_h3.py — record the figure-guard pass in HANDOFF.md.

Run from `files/`:

    python3 apply_handoff_h3.py            # apply
    python3 apply_handoff_h3.py --dry      # validate anchors, write nothing

Adds open items 41 to 43, closes 39, and corrects item 40's measured constants.
Anchors validated before any write; new strings grepped afterwards.
"""
import io
import os
import sys

DRY = '--dry' in sys.argv
P = 'HANDOFF.md'

NEW = """
41. **The guards existed and were not connected.** `figs_23` through `figs_32`
   called `validate` and `overruns`. They did not call `overflows` — written after
   chapter 29's stavnsband figure shipped a caption cut off at the canvas edge —
   and the **eleven map scripts called none of them at all**, so no territorial map
   in the series had ever been width-checked. All four now run from a single
   `check()` inside `mapspine.rasterise()`, which every script already calls, and
   **before** the cairosvg availability test, because otherwise the checks are
   skipped on exactly the machine that has no rasteriser and therefore cannot look
   instead.

   It found the stavnsband fault repeated. `svg_invasions.txt` had its second
   caption line at baseline y=462 in a 452-high canvas, so chapter 23 had been
   shipping the figure **without its final sentence** — "Neither crossed the
   water, and neither had to: taking Jutland was enough to dictate terms both
   times", which is the whole point of a two-panel comparison. Canvas raised to
   472, chapter 23 rebuilt, looked at. **A guard that is written and not wired in
   is worth nothing**, and this one cost three years of figures.

42. **`collisions()`, new: two pieces of text printing through each other.**
   Nothing tested for this, which is how a two-column layout in `figs_32.py` got
   through every check with the left column running to x=423 straight across a
   right column beginning at x=380 — both comfortably inside a 700 canvas.
   `overruns` tests the canvas edge and nothing else.

   Two things learned building it. Text inside a transformed group is in a
   different coordinate space, and the first version compared raw coordinates and
   reported the 1807 figure's subtitle as colliding with a map label 52 units
   away; it now tracks `translate()`. And **a percentage margin on a
   per-character estimate compounds with line length** — at five per cent above
   measured, a 149-character line in `svg_titles.txt` accumulated forty units of
   phantom width and was reported as overrunning a canvas it fits inside. The
   cushion belongs at the canvas edge, where it is a fixed six units and does not
   grow with the sentence.

43. **Open, cosmetic, needs a decision. `svg_terr_1660.txt` prints Helsingborg
   and Skaane into each other**, and Jamtland into Trondhjem, by 28 and 17 units.
   Found by the new collision guard on a map that has been shipped since Part F.
   It is legible but wrong, and fixing it means nudging two labels in
   `map_1660.py` and rebuilding chapter 25's page. Left alone deliberately rather
   than folded into an unrelated pass.
"""

CLOSES = [
    ("39. **Figure output is not byte-identical across machines.**",
     "39. ~~**Figure output is not byte-identical across machines.**~~ **CLOSED, "
     "Sept 2026 — NEGATIVE ZERO.** `\"%.1f\" % -0.00004` is `-0.0` and "
     "`\"%.1f\" % 0.00004` is `0.0`, so a coordinate that rounds to nothing keeps "
     "the sign of the float beneath it, and that sign is not guaranteed to match "
     "on two machines. Eight of them accounted for the entire "
     "109,561-versus-109,569 discrepancy in `map_1814.py`. Fixed in both "
     "formatters — `mapspine` and `mapkit` — by adding 0.0 after rounding. All six "
     "maps and all 51 figures now regenerate byte-identical on both machines, "
     "verified against a fresh clone. Blast radius was eleven stale figures, all "
     "in chapters 16 to 32, every one with a retained body; nothing in Parts A to "
     "D, which cannot be rebuilt. **Check that before applying a change of this "
     "shape, not after.** Original entry follows.\n\n   "
     "**Figure output was not byte-identical across machines.**"),
]

FIX40 = ("**mapt 5.68,\n   mapx 5.63, mapl 6.98 units per character.** The 6.1 the guard uses is\n"
         "   conservative for the two small classes and **too small for `mapl`**, so a long\n"
         "   heading can overrun without being flagged. That is a live under-detection, and\n"
         "   it belongs with open item 10.")
FIX40_NEW = ("**mapt 5.68,\n   mapx 5.63, mapl 6.98 units per character.** The single 6.1 the guard used was\n"
             "   conservative for the two small classes and **too small for `mapl`**, so a long\n"
             "   heading could overrun unflagged. RESOLVED Sept 2026: `mapspine.CHAR_W` now\n"
             "   carries the measured value per class, with no percentage margin on top and a\n"
             "   fixed six-unit cushion at the canvas edge instead. Re-measure if style.css\n"
             "   changes a font-size or the --mono stack; do not adjust by eye.")


def main():
    if not os.path.exists(P):
        print('!! %s not found — run this from files/' % P)
        return 1
    s = io.open(P, encoding='utf-8').read()

    edits = list(CLOSES)
    edits.append((FIX40, FIX40_NEW))
    edits.append(("\n\n## What Part G taught", NEW + "\n\n## What Part G taught"))

    for i, (old, new) in enumerate(edits, 1):
        n = s.count(old)
        if n != 1:
            print('!! edit %d: expected 1 match, found %d' % (i, n))
            print('   nothing written. Already patched?')
            return 1
    print('validated %d edits' % len(edits))
    if DRY:
        print('--dry: nothing written')
        return 0

    for old, new in edits:
        s = s.replace(old, new, 1)
    io.open(P, 'w', encoding='utf-8').write(s)
    print('wrote %s' % P)

    check = io.open(P, encoding='utf-8').read()
    bad = 0
    for probe in ('41. **The guards existed and were not connected.**',
                  '42. **`collisions()`, new',
                  '43. **Open, cosmetic, needs a decision.',
                  'CLOSED, Sept 2026 — NEGATIVE ZERO.',
                  'RESOLVED Sept 2026: `mapspine.CHAR_W` now',
                  'A guard that is written and not wired in'):
        if probe not in check:
            print('!! did NOT land: %s' % probe[:50])
            bad += 1
    return 1 if bad else (print('all entries verified present') or 0)


if __name__ == '__main__':
    sys.exit(main())
