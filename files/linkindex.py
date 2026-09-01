# -*- coding: utf-8 -*-
"""linkindex.py — add a link back to the index from every built chapter page.

    python3 linkindex.py            # run in the folder holding the pages
    python3 linkindex.py --dry
    DK_INDEX=index.html python3 linkindex.py

Two links per page: one in the crumb bar at the top, one in the footer. Both
point at the chapter's own row in the spine (`#cNN`), not the top of the index,
so the reader lands where they were.

WHY THIS IS A POST-PROCESSOR and not a change to the build scripts: Parts A-C
have no retained bodies - they exist only as built pages, recovered through
debuild.py if at all. A build-script change could not reach chapters 01-11
without a rebuild nobody wants to risk. This walks the finished pages instead
and needs no source.

It is idempotent: a page that already has the links is skipped. Re-run it after
any rebuild, because a rebuilt page comes out of the build script without them.
"""
import os
import re
import sys

DIR = os.environ.get("DK_CHAPTERS", os.getcwd())
INDEX = os.environ.get("DK_INDEX", "danish-history-index.html")

# The crumb's own styling: band colour, semibold, as `.crumb-in b` already uses.
# Left unstyled it would come out verdigris from the global `a` rule and fight
# the part colour on every page.
CRUMB = ('<span><a href="%s#c%02d" style="color:var(--band);font-weight:600;'
         'text-decoration:none">\u2190 Index</a></span>')
FOOT = ' &middot; <a href="%s#c%02d">back to the index</a>'


def main(dry):
    pages = sorted(f for f in os.listdir(DIR)
                   if re.match(r"^\d\d[-.]", f) and f.endswith(".html"))
    if not pages:
        raise SystemExit("no chapter pages found in %s" % DIR)

    done = skipped = failed = 0
    for f in pages:
        n = int(f[:2])
        p = os.path.join(DIR, f)
        h = open(p, encoding="utf-8").read()

        if INDEX in h:
            print("  %-50s already linked" % f[:50])
            skipped += 1
            continue

        new = h
        m = re.search(r'(<div class="crumb"><div class="crumb-in">)', new)
        if m:
            new = new[:m.end()] + "\n  " + (CRUMB % (INDEX, n)) + new[m.end():]
        else:
            print("  %-50s !! no crumb found" % f[:50])
            failed += 1
            continue

        m = re.search(r"(<footer>)(.*?)(</footer>)", new, re.S)
        if m:
            new = (new[:m.start(2)] + m.group(2).rstrip()
                   + (FOOT % (INDEX, n)) + "\n" + new[m.end(2):])
        else:
            print("  %-50s !! no footer found" % f[:50])
            failed += 1
            continue

        if not dry:
            open(p, "w", encoding="utf-8").write(new)
        print("  %-50s linked -> %s#c%02d" % (f[:50], INDEX, n))
        done += 1

    print("\n%d linked, %d already done, %d failed%s"
          % (done, skipped, failed, "  (--dry: nothing written)" if dry else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main("--dry" in sys.argv))
