# -*- coding: utf-8 -*-
"""apply_handoff_h1.py — record the Part H tooling session in HANDOFF.md.

Run from `files/`:

    python3 apply_handoff_h1.py            # apply
    python3 apply_handoff_h1.py --dry      # validate anchors, write nothing

Adds open items 30 to 36 and corrects three existing entries. Anchors are all
validated before anything is written; the new strings are grepped afterwards.

Everything here was found by running the tools, not by reading the ledger. Two of
the corrections are to entries that record work as done which was not done, which
is the failure mode this file exists to prevent, so they are corrected in place
rather than appended.
"""
import io
import os
import sys

DRY = '--dry' in sys.argv
P = 'HANDOFF.md'

NEW_ITEMS = """
30. **`linkindex.py` and `debuild.py verify` contradicted each other, and the
   project had been resolving it by skipping step two.** `linkindex` is a
   post-processor: it adds two links back to the index to a finished page, a crumb
   span and a footer tail, neither of which a retained body has ever seen. So any
   page taken through the documented sequence — build, `linkindex`,
   `index_generator`, upload — drifted against its own source by construction, and
   every chapter with a body reported `BODY DRIFT`. This never surfaced because
   `linkindex` was not re-run after the Parts E–G rebuilds. **Chapters 16–31 had
   been shipping with no index links at all.** Running it as documented turned the
   whole book red at once. Fixed Sept 2026: `_normalise` in `debuild.py` now strips
   the two link forms alongside the checkpoints and the reading-time line — a sixth
   injection added to the five it already knew about. Verified: 01–11 `style-only`,
   12–31 `identical`.

31. **`svg_plague.txt` holds the wrong figure, and every existing guard passes
   it.** `figs_27.py` once wrote its first figure to `svg_plague.txt`. That is
   chapter 15's filename: `build_part_d.py` maps `SVG_PLAGUE` → `svg_plague.txt`
   for the Black Death arrival map. The script was renamed to write
   `svg_plague_1711.txt`; nothing put chapter 15's figure back, and the two files
   are now byte-identical copies of the 1711 Copenhagen panel. `tidy.py` sees a
   file that exists and that a build script wants — findings 2, 3 and 5 all pass.
   `debuild.py verify` never opens a figure source, and chapter 15's body holds
   `{{SVG_PLAGUE}}`, a placeholder, which cannot disagree with anything. It has not
   shipped only because `build_part_d.py` cannot run at all (item 4). **The day
   item 4 is fixed and Part D is rebuilt, chapter 15 loses its figure silently, in
   a part with no retained bodies to restore from.** `recover_svg_plague.py`
   extracts the surviving copy from the shipped page and refuses to overwrite
   without `--replace`. Decision pending. `figs_27.py`'s docstring now carries a
   warning against pointing it back at that name.

32. **`figcheck.py`, new Sept 2026.** Compares the SVG inlined in each shipped
   page against what its generator currently produces — the gap that let chapter
   27 carry a superseded schools figure while `verify` reported `identical`
   throughout. Figures are matched by **aria-label**, not by filename guessing: the
   first version of the script matched on substrings and cried `STALE` forty-two
   times, all of them Parts A–D figures with no source on disk. Current state: 48
   matched, 41 sourceless, 0 stale. It found item 31 on its first clean run, by
   noticing two files claiming one identity. **Parts A–C reference no figure
   sources at all** — `build_parts_abc.py` contains not one `svg_*.txt` — so
   thirty-one figures exist only inside their pages. That is expected, not a fault,
   and the count is printed so a change in it is visible.

33. **Do not commit an SVG that has been through a download.** Two `.txt` figure
   files handed over as downloads came back carrying an injected **C2PA
   content-credentials manifest**: 7,736 bytes of base64 welded into the `<svg>`
   root, the same on both files, invisible in a diff viewer. It does not corrupt
   word counts — `pagewords` strips whole `<svg>` blocks — and the file stays
   well-formed, but it would have inlined 15.5 KB of base64 into chapter 27 and
   made `figcheck` flag it in perpetuity. **Anything generated should be
   regenerated locally rather than round-tripped.** That covers every `.html` page
   as well: they are build outputs. Source edits travel as a patch script instead;
   see `apply_session_h1.py`, which was verified by applying it to a pristine clone
   and rebuilding — byte-identical to the tree it was written from.

34. **Chapter 12 will flag as too long under the new advisory, on a number that is
   wrong.** `build_all.py` reads the `about N minutes` stamp off the page rather
   than recomputing it, so for chapters 01–15 it judges pre-fix figures. Chapter 12
   stamps 41; its corrected page count is 8,335 words, which is 40 and inside
   28–40. It has no body and cannot be rebuilt to clear the stamp. Changing
   `build_all.py` to judge the recomputed count is a few lines and would also make
   chapter 10 flag low at 27, which is a real signal on a real number. **Left alone
   by decision, Sept 2026.** Recorded so it is not rediscovered as a fault.

35. **Chapter 32's plan needed nine corrections, found by research.** Recorded
   because the pattern is now four parts old: §01 dropped Lauenburg from the
   German Confederation and missed the 2.6 million daler that came with the swap of
   4 June 1815; §03's vignette placed Skræppenborg near Kolding in the early 1840s,
   after he had moved there and grown rich, when the prosecutions and the fines
   were the 1830s on Funen; §04 called the censorship individual and lifelong when
   it was automatic under the 1799 ordinance and lasted eleven years; §05's
   vignette put Pätges at Det Kongelige Teater when the 12 February 1826 evening
   was at the Hofteatret; §06's title said 1831–1835 when Viborg and Slesvig did
   not sit until 1836; §08 had no date for Bondevennerne (5 May 1846) and no cause
   (the Bondecirkulære of 8 November 1845); §09 omitted that Hiort Lorenzen's
   demonstration was planned by Flor; §10 dropped Lauenburg again and missed that
   the Open Letter refused the Ejderpolitik in the same breath as the Augustenborg
   claim. Only the ten-section structure and the 18-month closing interval survived
   unaltered.

36. **Two data gaps block figures in chapter 32.** Figure (b) needs the Slesvig
   and Itzehoe seat counts; Roskilde (70 = 60 elected + 10 royal) and Viborg (55 =
   48 + 7) are sourced and the arithmetic reconciles. Figure (c) needs the
   year-by-year values of the Zealand *kapitelstakst* for a tønde of rye, 1815–48,
   after Scharling; the series is published and **there is a currency break at
   1813/14**, so the chart must not be extended back across it. Neither is a
   judgement; both are document fetches.
"""


def main():
    if not os.path.exists(P):
        print('!! %s not found — run this from files/' % P)
        return 1
    s = io.open(P, encoding='utf-8').read()

    edits = []

    # --- correction 1: item 12 is marked closed and the work was not done ------
    edits.append((
        "**CLOSED, Sept 2026 \u2014\n   resolved by editing the built page directly.**",
        "**CLOSED, Sept 2026 \u2014 decision only; the edit was not actually made\n"
        "   until 5 Sept 2026, when the arrow was found still reading `\u2192 36`. It now\n"
        "   reads `\u2192 30, Part I` and chapter 15 verifies `identical`.** **An item\n"
        "   recorded as closed is one nobody looks at again, so a decision must not be\n"
        "   written up in the past tense of the work.**"))

    # --- correction 2: item 28 says six scripts; there are three --------------
    edits.append((
        "**The advisory constant is hardcoded in six scripts.** `build_all.py` and the\n"
        "   five `build_part_*.py` files print against 30\u201342. It is now 28\u201340. All six move\n"
        "   together.",
        "**The advisory constant is hardcoded in three scripts, not six.** `build_all.py`,\n"
        "   `build_part_f.py` and `build_part_g.py` carry `TARGET`. `build_parts_abc.py`,\n"
        "   `build_part_d.py` and `build_part_e.py` compute and stamp a reading time but\n"
        "   never judge it against anything \u2014 no `TARGET`, no `BAND`. Moved to 28\u201340 on\n"
        "   5 Sept 2026; nothing was missed, because there was nothing there. Unrelated and\n"
        "   also unrecorded: `build_all.py`'s `PARTS` list contains only A\u2013C, D and E, so\n"
        "   it does not build F or G at all."))

    # --- the new items --------------------------------------------------------
    edits.append((
        "\n\n## What Part G taught",
        NEW_ITEMS + "\n\n## What Part G taught"))

    loaded = []
    for i, (old, new) in enumerate(edits, 1):
        n = s.count(old)
        if n != 1:
            print('!! edit %d: expected 1 match, found %d' % (i, n))
            print('   nothing written. Already patched, or the ledger has moved on.')
            return 1
        loaded.append((old, new))
    print('validated %d edits' % len(loaded))
    if DRY:
        print('--dry: nothing written')
        return 0

    for old, new in loaded:
        s = s.replace(old, new, 1)
    io.open(P, 'w', encoding='utf-8').write(s)
    print('wrote %s' % P)

    check = io.open(P, encoding='utf-8').read()
    bad = 0
    for probe in ('30. **`linkindex.py` and `debuild.py verify` contradicted',
                  '31. **`svg_plague.txt` holds the wrong figure',
                  '32. **`figcheck.py`, new Sept 2026.**',
                  '33. **Do not commit an SVG that has been through a download.**',
                  '34. **Chapter 12 will flag as too long',
                  '35. **Chapter 32\u2019s plan needed nine corrections'.replace('\u2019', "'"),
                  '36. **Two data gaps block figures',
                  'hardcoded in three scripts, not six',
                  'a decision must not be',
                  'does not build F or G at all'):
        if probe not in check:
            print('!! did NOT land: %s' % probe[:52])
            bad += 1
    if bad:
        return 1
    print('all new entries verified present')
    return 0


if __name__ == '__main__':
    sys.exit(main())
