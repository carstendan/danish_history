# -*- coding: utf-8 -*-
"""recover_svg_plague.py — put chapter 15's Black Death map back in svg_plague.txt.

    python3 recover_svg_plague.py            # write svg_plague.recovered.txt
    python3 recover_svg_plague.py --replace  # overwrite svg_plague.txt itself

DO NOT RUN --replace UNTIL YOU HAVE LOOKED AT THE RECOVERED FILE.

WHAT HAPPENED. `figs_27.py` once wrote its first figure to `svg_plague.txt`.
That is chapter 15's filename: `build_part_d.py` maps `SVG_PLAGUE` ->
`svg_plague.txt` for `15-plague-and-reconquest-valdemar-atterdag.html`, where it
is the map of the Black Death's arrival years across Europe. The script was
later renamed to write `svg_plague_1711.txt`, but nothing put chapter 15's
figure back, so `svg_plague.txt` on disk is a byte-identical copy of chapter
27's 1711 Copenhagen plague panel.

WHY NOTHING CAUGHT IT. `tidy.py` sees a file that exists and that a build script
asks for: not missing, not an orphan, and not two generations of one *name*, so
findings 3, 2 and 5 all pass. `debuild.py verify` never opens a figure source;
chapter 15's body holds `{{SVG_PLAGUE}}`, and a placeholder cannot disagree with
anything. The fault is only visible by comparing what a figure SAYS IT IS
against what the page shows, which is what `figcheck.py` now does — it found
this on its first clean run, by noticing that two `.txt` files claim the same
aria-label.

WHY THIS HAS NOT SHIPPED. `build_part_d.py` cannot currently run at all (open
item 4: it replaces a `--part:` token against a stylesheet that names it
`--band:`). The day that is fixed and Part D is rebuilt, chapter 15's Black
Death map is replaced by chapter 27's plague timeline, silently, in a part that
has no retained bodies to restore from.

WHERE THE RECOVERY COMES FROM. The shipped page. Part D's figures have no
generators — that is documented, accepted debt — so the inlined copy in
`15-plague-and-reconquest-valdemar-atterdag.html` is the only surviving version
and therefore the best available source. This is the same position as
`map_1050.py` and `map_1250.py` in open item 5b.

AFTER RUNNING WITH --replace, rasterise and look:

    python3 -c "import io,mapspine as M; \\
      M.rasterise(io.open('svg_plague.txt',encoding='utf-8').read(),'look.png')"

and expect a map of Europe titled 'Thirty-three months / FROM SICILY TO
JUTLAND', with Messina 1347 at the bottom and Bergen 1349 at the top.
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.environ.get('DK_CHAPTERS', os.path.dirname(HERE))
PAGE = '15-plague-and-reconquest-valdemar-atterdag.html'

SVG = re.compile(r'<svg\b.*?</svg>', re.S)


def main():
    path = os.path.join(PAGES, PAGE)
    if not os.path.exists(path):
        print('!! not found: %s' % path)
        return 1
    html = io.open(path, encoding='utf-8').read()

    hits = [s for s in SVG.findall(html) if 'Black Death' in s]
    if len(hits) != 1:
        print('!! expected exactly 1 Black Death figure in %s, found %d'
              % (PAGE, len(hits)))
        return 1
    svg = hits[0]

    lab = re.search(r'aria-label="([^"]*)"', svg)
    if not lab or not lab.group(1).lower().startswith('map of europe'):
        print('!! recovered figure does not look like the Black Death map:')
        print('   aria-label: %s' % (lab.group(1)[:90] if lab else '(none)'))
        return 1

    # Guard against recovering the wrong thing: the file we are about to
    # replace currently holds the 1711 figure, and the two must not match.
    cur = os.path.join(HERE, 'svg_plague.txt')
    if os.path.exists(cur):
        a = re.sub(r'\s+', ' ', io.open(cur, encoding='utf-8').read()).strip()
        b = re.sub(r'\s+', ' ', svg).strip()
        if a == b:
            print('svg_plague.txt already holds the Black Death map: nothing to do')
            return 0

    if '--replace' in sys.argv:
        out = cur
    else:
        out = os.path.join(HERE, 'svg_plague.recovered.txt')

    io.open(out, 'w', encoding='utf-8').write(svg)
    print('wrote %s  (%d bytes)' % (os.path.basename(out), len(svg)))
    print('aria-label: %s...' % lab.group(1)[:70])

    check = io.open(out, encoding='utf-8').read()
    if 'Black Death' not in check or not check.rstrip().endswith('</svg>'):
        print('!! the write did not land intact')
        return 1
    print('verified: file on disk contains the Black Death map and is well formed')

    if '--replace' not in sys.argv:
        print('\nThis was a dry recovery. Look at it, then re-run with --replace.')
    else:
        print('\nNow rasterise and look at it before trusting it. Part D still '
              'cannot rebuild (open item 4), so nothing ships from this yet.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
