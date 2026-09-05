# -*- coding: utf-8 -*-
"""apply_session_h1.py — apply the source edits from the Part H tooling session.

Run once, from `files/`:

    python3 apply_session_h1.py            # apply
    python3 apply_session_h1.py --dry      # report what would change, write nothing

WHY A SCRIPT AND NOT A SET OF FILES. Two `.txt` figure files handed over as
downloads earlier in this session came back carrying an injected C2PA
content-credentials manifest — 7,736 bytes of base64 welded into the `<svg>`
root, on both files, invisible in a diff viewer. Anything that is generated
should be regenerated locally rather than round-tripped through a download. That
covers every `.html` page in this change: they are build outputs.

Chapters 01, 03 and 06 are the exception and are patched here directly, because
Parts A–C have no retained bodies. There is nothing upstream to edit and nothing
a rebuild could regenerate, which is the same reasoning that made chapter 15's
arrow safe to edit in place (open item 12).

EVERY EDIT IS VALIDATED BEFORE ANY FILE IS WRITTEN. An assertion that aborts
midway leaves some files changed and some not, and the shell command after it
still reports success. So this collects all anchors first, checks every one, and
only then writes — then greps for the new string afterwards, independently.

This script was verified by applying it to a pristine clone of the commit it
targets and running the full build pipeline: the result was byte-identical to
the tree it was written from.
"""
import io
import os
import sys

EM = '\u2014'
DRY = '--dry' in sys.argv

EDITS = {}

# ---------------------------------------------------------------- figs_27.py
EDITS['figs_27.py'] = [
    # The grid draws twenty per district, which was the order of 23 August 1721.
    # The built distribution varied, between about ten and twenty-five per
    # district, while the total held. The header claimed an outcome the sources
    # do not support.
    ("""    o.append('<text x="26" y="80" class="mapx">TWELVE DISTRICTS, TWENTY SCHOOLS EACH</text>')""",
     """    o.append('<text x="26" y="80" class="mapx">TWELVE DISTRICTS, TWENTY SCHOOLS EACH AS ORDERED</text>')"""),
    ("""         'Twelve districts at twenty schools each were planned, two hundred and forty in all, and '
         'two hundred and forty were built between 1722 and 1727, and one more on Bog\\u00f8 by '""",
     """         'Twelve districts at twenty schools each were planned, two hundred and forty in all, and '
         'two hundred and forty were built between 1722 and 1727, though not twenty to every '
         'district: the number built per district varied while the total held. One more went up '
         'on Bog\\u00f8 by '"""),
    # The docstring still named the file this script used to write, which is
    # chapter 15's Black Death map.
    ("""  svg_plague.txt   what the state did, and what it could not count
  svg_schools.txt  two hundred and forty-one schools in six years""",
     """  svg_plague_1711.txt  what the state did, and what it could not count
  svg_schools.txt      two hundred and forty-one schools in six years

NOTE, Sept 2026. This script once wrote the first figure to `svg_plague.txt` and
was renamed to `svg_plague_1711.txt` to stop it colliding with chapter 15's
Black Death map, which `build_part_d.py` inlines from `svg_plague.txt`. The
rename was made; the damage was not undone, and `svg_plague.txt` still holds a
copy of the 1711 figure. Do not point this script back at that name."""),
]

# ---------------------------------------------------------------- debuild.py
EDITS['debuild.py'] = [
    ("""    h = re.sub(r'<svg\\b.*?</svg>', '{{FIG}}', h, flags=re.S)
    h = re.sub(r'\\{\\{SVG_[A-Z0-9_]+\\}\\}', '{{FIG}}', h)
    return h.strip()""",
     """    h = re.sub(r'<svg\\b.*?</svg>', '{{FIG}}', h, flags=re.S)
    h = re.sub(r'\\{\\{SVG_[A-Z0-9_]+\\}\\}', '{{FIG}}', h)
    # The SIXTH injection, and the one that made this tool contradict the build
    # routine (open item 8). linkindex.py is a post-processor: it walks finished
    # pages and adds two links back to the index, a crumb span and a footer tail.
    # A retained body has never seen either. So a page that has been through the
    # documented sequence - build, linkindex, index_generator, upload - drifted
    # against its own source by construction, and every chapter with a body
    # reported BODY DRIFT.
    #
    # That never surfaced because linkindex was not re-run after the Parts E-G
    # rebuilds, so chapters 16-31 shipped with no index links and matched their
    # bodies for the wrong reason. Running it as documented turned the whole
    # book red at once.
    #
    # These are furniture, not prose. Strip them from both sides, exactly as the
    # checkpoints and the reading-time line are stripped above.
    h = re.sub(r'\\n\\s*<span><a href="[^"]*#c\\d\\d"[^>]*>[^<]*</a></span>', '', h)
    h = re.sub(r'\\s*&middot;\\s*<a href="[^"]*#c\\d\\d"[^>]*>[^<]*</a>', '', h)
    return h.strip()"""),
]

# --------------------------------------------------- bodies: chapters 19, 21
# D-1: a forward arrow names a chapter number only inside the next part.
# Chapters 32-43 are unbuilt and their numbers can still move, so they take a
# part letter. Chapter 19 promises 1848, 1864 AND the 1920 plebiscite, so
# Part H alone would leave the line insolvent (L5).
EDITS['c19_body.html'] = [
    ("<b>\u2192 32</b><span>The Ribe settlement is the root of the Schleswig-Holstein question: 1848,",
     "<b>\u2192 Part H, Part I</b><span>The Ribe settlement is the root of the Schleswig-Holstein question: 1848,"),
]
EDITS['c21_body.html'] = [
    ("<b>\u2192 32</b><span>The partitioned-off dukes of 1544 and after produce the S\u00f8nderborg and",
     "<b>\u2192 Part H</b><span>The partitioned-off dukes of 1544 and after produce the S\u00f8nderborg and"),
    ("The slogan's national career belongs to the 1840s and is\n  chapter 32's business.",
     "The slogan's national career belongs to the 1840s and is\n  Part H's business."),
]

# ------------------------------------------------- pages: chapters 01, 03, 06
# Chapters 1 and 3 pointed at 34 while naming chapter 35's subject; chapter 6
# pointed at 33 while naming 1864, which is 34. All three were already wrong,
# which is exactly what D-1 predicts of a number aimed into an unbuilt part.
PAGES = os.environ.get('DK_CHAPTERS', '..')
EDITS[os.path.join(PAGES, '01-reindeer-hunters-and-the-retreating-ice.html')] = [
    ("<b>\u2192 34</b><span><i>Industry, cooperatives, emigration and labour</i> " + EM +
     " West Jutland's sand is the reason for the heath, and therefore for the",
     "<b>\u2192 Part H</b><span>West Jutland's sand is the reason for the heath, and therefore for the"),
]
EDITS[os.path.join(PAGES, '03-first-farmers-and-the-megalith-builders.html')] = [
    ("<b>\u2192 34</b><span><i>Industry, cooperatives, emigration and labour</i> " + EM +
     " The sandy west is now visibly poorer country. That difference runs all the",
     "<b>\u2192 Part H</b><span>The sandy west is now visibly poorer country. That difference runs all the"),
]
EDITS[os.path.join(PAGES, '06-roman-iron-age-living-beside-the-empire.html')] = [
    ("<b>\u2192 10, 33</b><span><i>One kingdom, one faith: Jelling</i> \u00b7 <i>1864</i> " + EM +
     " The Nydam boat is the ancestor of the longship " + EM + " and it sits in a German\n"
     "    museum today because of the war in chapter 33.</span>",
     "<b>\u2192 10, Part H</b><span><i>One kingdom, one faith: Jelling</i> " + EM +
     " The Nydam boat is the ancestor of the longship " + EM + " and it sits in a German\n"
     "    museum today because of the war of 1864.</span>"),
]


def main():
    # ---- phase 1: read everything and validate every anchor ----------------
    loaded, total = {}, 0
    for path, edits in EDITS.items():
        if not os.path.exists(path):
            print('!! missing: %s' % path)
            return 1
        s = io.open(path, encoding='utf-8').read()
        for i, (old, new) in enumerate(edits, 1):
            n = s.count(old)
            if n != 1:
                print('!! %s edit %d: expected exactly 1 match, found %d'
                      % (path, i, n))
                print('   nothing has been written. Is the file already patched?')
                return 1
        loaded[path] = s
        total += len(edits)
    print('validated %d edits across %d files' % (total, len(EDITS)))
    if DRY:
        print('--dry: nothing written')
        return 0

    # ---- phase 2: write ----------------------------------------------------
    for path, edits in EDITS.items():
        s = loaded[path]
        for old, new in edits:
            s = s.replace(old, new, 1)
        io.open(path, 'w', encoding='utf-8').write(s)
        print('  wrote %s' % path)

    # ---- phase 3: grep, independently of the write -------------------------
    bad = 0
    for path, edits in EDITS.items():
        s = io.open(path, encoding='utf-8').read()
        for i, (old, new) in enumerate(edits, 1):
            if new not in s:
                print('!! %s edit %d did NOT land' % (path, i))
                bad += 1
            if old in s:
                print('!! %s edit %d: old string still present' % (path, i))
                bad += 1
    if bad:
        return 1
    print('all %d edits verified present' % total)

    print("""
Now, in files/, in this order:

    python3 figs_27.py
    python3 build_part_e.py
    python3 build_part_f.py
    python3 build_part_g.py
    DK_CHAPTERS="$PWD/.." python3 linkindex.py
    DK_CHAPTERS="$PWD/.." python3 index_generator.py
    python3 debuild.py verify ../0?-*.html ../1?-*.html ../2?-*.html ../3?-*.html
    python3 figcheck.py

Expected: chapters 16-31 rebuild byte-identical except 19, 21 and 27, plus a
one-minute drop in the stamped reading time on 24, 25 and 31 as the corrected
word counter reaches them. linkindex reports 16 newly linked - Parts E to G have
been shipping without index links. verify: style-only for 01-11, identical for
12-31. figcheck: 48 matched, 41 sourceless, 0 stale.

Then upload. That part needs you.
""")
    return 0


if __name__ == '__main__':
    sys.exit(main())
