# -*- coding: utf-8 -*-
"""bookstats.py — how big is this thing, and how big will it be.

    python3 bookstats.py                # run in the folder holding the pages
    DK_CHAPTERS=/path python3 bookstats.py

Reports two counts per chapter, because they answer different questions:

  page    everything after </style>, the same measure build_all.py bands on.
          Includes the rail, the contents list, figure text and the rail script.
  text    the same minus navigation and <script>. This is the one to use for
          "how long is the book", because nobody reads the rail twice.

Then projects the remainder from the measured mean of what is built, and gives a
range rather than a number, because five chapters are still flagged dense and a
dense chapter that gets planned as two pages adds a chapter to the total.
"""
import os
import re
import sys

from pagewords import pagewords, textwords
import dkpaths

# The default is this repository, not the current directory: run from files/ by
# mistake and a cwd default finds no chapters and reports an empty book rather
# than refusing.
_HERE = os.path.dirname(os.path.abspath(__file__))
DIR = dkpaths.resolve("DK_CHAPTERS", os.path.dirname(_HERE), "the folder holding the chapter pages")
WPM = 210
# L1a's hard band, read in whole minutes (review session 22: 21 and 45 are 50.25 and 50.15 minutes
# by the builds' count, and are stamped 50). The band line reads each page's own stamp, "Era
# chapter · about N minutes", as build_all.py's summary does: every part build writes it,
# round(words / 210), from the words it counts BEFORE linkindex.py adds the index link (6 words),
# and build_part_f/g/h/i.py refuse a page whose N is outside the band; A-E's builds write it and
# do not refuse. So the line agrees with the builds by construction, where this file's "min"
# column, counted on the page as shipped, can say 51 of a page built at 50 (check 1 of review
# session 22 planted one). It reads what the build wrote: a page edited after its build keeps its
# old stamp (debuild and freshcheck guard that), and build_all.py reads a missing stamp as 0 where
# this line lists it.
BAND = (25, 50)
STAMP = re.compile(r"Era chapter · about (\d+) minutes")
TOTAL_PLANNED = 45
DENSE = {42}

PARTS = [("A", 1, 3), ("B", 4, 7), ("C", 8, 11), ("D", 12, 15), ("E", 16, 20),
         ("F", 21, 24), ("G", 25, 31), ("H", 32, 36), ("I", 37, 45)]


def part_of(n):
    for name, a, b in PARTS:
        if a <= n <= b:
            return name
    return "?"


def counts(html):
    """Both measures now come from pagewords.py, so this file cannot drift from
    the build scripts the way it did while each carried its own expression."""
    return pagewords(html), textwords(html)


def main():
    found = {}
    for f in sorted(os.listdir(DIR)):
        m = re.match(r"^(\d\d)[-.]", f)
        if not m or not f.endswith(".html"):
            continue
        n = int(m.group(1))
        html = open(os.path.join(DIR, f), encoding="utf-8", errors="replace").read()
        m = STAMP.search(html)
        found[n] = counts(html) + (f, int(m.group(1)) if m else None)

    if not found:
        raise SystemExit("no chapter pages found in %s" % DIR)

    print("%-4s %-46s %8s %8s %6s" % ("ch", "file", "page", "text", "min"))
    print("-" * 76)
    bypart = {}
    for n in sorted(found):
        page, text, f, _stamp = found[n]
        p = part_of(n)
        bypart.setdefault(p, [0, 0, 0])
        bypart[p][0] += page
        bypart[p][1] += text
        bypart[p][2] += 1
        print("%-4d %-46s %8d %8d %6d" % (n, f[:46], page, text, round(page / WPM)))

    outside = ["%02d (%s)" % (n, "no minutes stamp" if found[n][3] is None
                              else "%d min" % found[n][3])
               for n in sorted(found)
               if found[n][3] is None or not BAND[0] <= found[n][3] <= BAND[1]]
    print("outside the %d-%d minute band (each page's own stamp, as the builds wrote it): %s"
          % (BAND[0], BAND[1], ", ".join(outside) if outside else "none"))

    tp = sum(v[0] for v in bypart.values())
    tt = sum(v[1] for v in bypart.values())
    nb = len(found)
    print("-" * 76)
    for name, a, b in PARTS:
        if name in bypart:
            page, text, k = bypart[name]
            print("part %-2s %2d of %2d chapters %28d %8d" % (name, k, b - a + 1, page, text))
    print("-" * 76)
    print("built  %2d of %2d chapters %28d %8d  (%.1f h)"
          % (nb, TOTAL_PLANNED, tp, tt, tp / WPM / 60))

    mp, mt = tp / nb, tt / nb
    left = TOTAL_PLANNED - nb
    dense_left = len([d for d in DENSE if d not in found])
    print("\nmean per chapter: %d page words, %d text words, %d min" % (mp, mt, round(mp / WPM)))
    print("remaining: %d chapters, of which %d %s flagged dense"
          % (left, dense_left, "is" if dense_left == 1 else "are"))
    for label, extra in (("if none of the dense chapters splits", 0),
                         ("if half of them do", dense_left // 2),
                         ("if all of them do", dense_left)):
        total = TOTAL_PLANNED + extra
        print("  %-38s %2d chapters  %7d page words  %7d text  %5.1f h"
              % (label, total, total * mp, total * mt, total * mp / WPM / 60))


if __name__ == "__main__":
    sys.exit(main())
