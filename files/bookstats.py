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

DIR = os.environ.get("DK_CHAPTERS", os.getcwd())
WPM = 210
TOTAL_PLANNED = 43
DENSE = {35, 41}

PARTS = [("A", 1, 3), ("B", 4, 7), ("C", 8, 11), ("D", 12, 15), ("E", 16, 20),
         ("F", 21, 24), ("G", 25, 31), ("H", 32, 36), ("I", 37, 43)]


def part_of(n):
    for name, a, b in PARTS:
        if a <= n <= b:
            return name
    return "?"


def counts(html):
    """Both measures now come from pagecount.py, so this file cannot drift from
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
        found[n] = counts(html) + (f,)

    if not found:
        raise SystemExit("no chapter pages found in %s" % DIR)

    print("%-4s %-46s %8s %8s %6s" % ("ch", "file", "page", "text", "min"))
    print("-" * 76)
    bypart = {}
    for n in sorted(found):
        page, text, f = found[n]
        p = part_of(n)
        bypart.setdefault(p, [0, 0, 0])
        bypart[p][0] += page
        bypart[p][1] += text
        bypart[p][2] += 1
        print("%-4d %-46s %8d %8d %6d" % (n, f[:46], page, text, round(page / WPM)))

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
    print("remaining: %d chapters, of which %d are flagged dense" % (left, dense_left))
    for label, extra in (("if none of the dense chapters splits", 0),
                         ("if half of them do", dense_left // 2),
                         ("if all of them do", dense_left)):
        total = TOTAL_PLANNED + extra
        print("  %-38s %2d chapters  %7d page words  %7d text  %5.1f h"
              % (label, total, total * mp, total * mt, total * mp / WPM / 60))


if __name__ == "__main__":
    sys.exit(main())
