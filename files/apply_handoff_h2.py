# -*- coding: utf-8 -*-
"""apply_handoff_h2.py — record the chapter 32 build session in HANDOFF.md.

Run from `files/`:

    python3 apply_handoff_h2.py            # apply
    python3 apply_handoff_h2.py --dry      # validate anchors, write nothing

Adds open items 37 to 40 and closes 31 and 36. Anchors validated before any
write; new strings grepped afterwards.
"""
import io
import os
import sys

DRY = '--dry' in sys.argv
P = 'HANDOFF.md'

NEW = """
37. **Adding a token to `style.css` requires the exact `"; "` spacing, or
   `debuild.py`'s drop list silently misses it.** Part H needed a band colour, so
   `--slate:#4F6470` went in beside `--indigo`. The first insertion was
   `--indigo:#2F4C7A;--slate:...`, without the space. `debuild` drops tokens the
   page never had by matching `(--[a-z]+:#[0-9A-Fa-f]{6}; )` — with a trailing
   space — so removing `--slate` from the reconstruction left
   `--indigo:#2F4C7A;--band` where all thirty-one shipped pages have
   `--indigo:#2F4C7A; --band`. One character. **Verify went from 20 `identical`
   to 31 `style-only` in a single edit**, and the only reason it was caught in
   minutes rather than shipped is that `build_part_h.py`'s docstring had been
   written to predict exactly that symptom before the token was added. Corrected;
   back to 21 `identical`, 11 `style-only`. Write the prediction down before
   making the change, not after.

38. **`files/danish-history-index.html` was a corrupt shadow of the real index,
   committed.** It announced **"0 pages written"** and marked all forty-three
   chapters unwritten, because it had been generated in a folder holding no
   chapter pages — open item 2's container-path bug, fossilised. The live index is
   at the chapter-folder root, which is where `index_generator.py` writes and what
   every page links to. `tidy.py` finding 5 could not see it: that check compares
   names within `files/` only, and this was the same name in two directories.
   Finding 5 now walks both. **Delete `files/danish-history-index.html`** — it is
   tracked, so git keeps it.

39. **Figure output is not byte-identical across machines.** `map_1814.py`
   produced 109,561 characters in the container and 109,569 on the Mac, from the
   same source and the same atlas. Coordinates are formatted `%.1f`, which is
   deterministic, so it is not float drift and the cause is not established.
   Consequence, and the reason it does not matter much: the generated figures that
   go into the pages are the ones generated on the machine that runs the build,
   and `figcheck.py` compares page against disk on that same machine, so both
   sides agree. **It is a further reason never to hand over or commit a generated
   file** — only the generator. See item 33.

40. **`cairosvg` is not installed on the Mac, so `M.rasterise` writes nothing
   there and every figure script prints that figures were NOT visually checked.**
   The three chapter 32 figures were rasterised and looked at in the container
   instead, and looking caught two faults no guard did: a two-column layout in
   `figs_32.py` where the left column printed straight through the right one while
   both sat inside the canvas, and three colliding labels on the 1814 map.
   `overruns` tests the canvas edge and nothing else; **there is no collision
   guard**. `mapdump.py` builds a browser contact sheet without cairosvg and is
   the fallback until `brew install cairo && pip3 install cairosvg` is done.

   Measured while fixing it, off the raster rather than assumed: **mapt 5.68,
   mapx 5.63, mapl 6.98 units per character.** The 6.1 the guard uses is
   conservative for the two small classes and **too small for `mapl`**, so a long
   heading can overrun without being flagged. That is a live under-detection, and
   it belongs with open item 10.
"""

CLOSES = [
    ("31. **`svg_plague.txt` holds the wrong figure",
     "31. ~~**`svg_plague.txt` holds the wrong figure**~~ **CLOSED, Sept 2026** — "
     "`recover_svg_plague.py --replace` restored chapter 15's Black Death map from "
     "the shipped page, the two files no longer collide, and `figcheck` reports 0 "
     "stale. Part D still cannot rebuild, so nothing ships from it yet, but the "
     "landmine under open item 4 is gone. Original entry follows.\n\n   **`svg_plague.txt` held the wrong figure"),
    ("36. **Two data gaps block figures in chapter 32.",
     "36. ~~**Two data gaps block figures in chapter 32.**~~ **PARTLY CLOSED, Sept "
     "2026.** Figure (b) is built: Schleswig's 44 came from the published 1836 "
     "membership list, and Holstein's 48 is COUNTED from the 1835/36 list rather "
     "than taken from the decree — the figure says `counted, not decreed` on its "
     "face and `figs_32.py` records what would close it. Figure (c) is REPLACED: "
     "the Zealand kapitelstakst exists in Statistiske Meddelelser 4. Raekke, 15. "
     "Bind, Haefte I and was not obtainable, so the figure draws the attested "
     "ratios and a chronology and states that the series exists and is not plotted "
     "here. Both remain worth closing properly. Original entry follows.\n\n   "
     "**Two data gaps blocked figures in chapter 32."),
]


def main():
    if not os.path.exists(P):
        print('!! %s not found — run this from files/' % P)
        return 1
    s = io.open(P, encoding='utf-8').read()

    edits = list(CLOSES)
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
    for probe in ('37. **Adding a token to `style.css`',
                  '38. **`files/danish-history-index.html` was a corrupt shadow',
                  '39. **Figure output is not byte-identical across machines.**',
                  '40. **`cairosvg` is not installed on the Mac',
                  'mapt 5.68',
                  'too small for `mapl`',
                  '31. ~~**`svg_plague.txt` holds the wrong figure**~~',
                  '36. ~~**Two data gaps block figures in chapter 32.**~~'):
        if probe not in check:
            print('!! did NOT land: %s' % probe[:54])
            bad += 1
    if bad:
        return 1
    print('all entries verified present')
    print('\nNow, from files/:  rm danish-history-index.html   (item 38)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
