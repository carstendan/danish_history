# -*- coding: utf-8 -*-
"""Rebuild the whole series, one command, and fail loudly.

Replaces the old build_all.py, which was not a runner at all: it was a one-off
retrofit that injected checkpoint CSS into entries 01-08, pointed at a working
directory that no longer exists, and rewrote 'Era page - about N minutes' in the
vocabulary the series has retired. It had not run for a long time.

This one runs the part builds in order and adds up what they produced. Each part
build does its own verification; this reports the aggregate and exits non-zero if
anything failed or is missing.

    python3 build_all.py            # build every part whose inputs are present
    python3 build_all.py e          # build one part
    python3 build_all.py --check    # report what is present, build nothing
"""
import glob
import os
import re
import subprocess
import sys

from pagewords import pagewords   # one definition, shared

G = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get('DK_OUT', os.path.dirname(G)) + os.sep

PARTS = [
    ("A-C", "build_parts_abc.py", "01-11", "Stone Age to the North Sea Empire"),
    ("D", "build_part_d.py", "12-15", "the High Middle Ages"),
    ("E", "build_part_e.py", "16-20", "union and late Middle Ages"),
]

# Everything a part build needs beyond its own bodies. If one of these is absent
# the build fails in a confusing way, so say so before starting.
SHARED = ["style.css", "rail.js", "mapkit.py", "mapspine.py"]

# Reading time, in minutes at ~210 wpm.
#
# BAND is the hard rule and the build fails outside it. 25-50 rather than the
# old 25-45 because 25-45 is not closed under splitting: a chapter at the old
# ceiling halves to 22.5, below the floor, so 45-50 was a dead zone where a
# chapter was at once too long to keep and too short to divide. Chapter 21
# landed exactly there. With a 2:1 band any chapter at the ceiling splits into
# two at the floor.
#
# TARGET is advisory and never fails. It is what the band used to do for us as a
# diagnostic: short has consistently meant a missing subject rather than thin
# prose, and long has meant the chapter is carrying more topics than one page
# should. Widening the hard rule without keeping this note would retire the most
# useful signal the build produces.
BAND = (25, 50)
TARGET = (28, 40)


def present(name):
    return os.path.exists(os.path.join(G, name))


def bodies_for(script):
    """The body files a part build reads, taken from the script itself rather
    than guessed, so this cannot drift out of step with the configs."""
    src = open(os.path.join(G, script), encoding='utf-8').read()
    return sorted(set(re.findall(r"body='([^']+)'", src)))


def check():
    print("shared inputs")
    missing = [f for f in SHARED if not present(f)]
    for f in SHARED:
        print("  %-16s %s" % (f, "ok" if present(f) else "MISSING"))
    if not present("package/land-50m.json"):
        print("  %-16s MISSING - run: npm pack world-atlas && tar xzf world-atlas-*.tgz"
              % "world-atlas")

    print("\nparts")
    runnable = []
    for part, script, span, label in PARTS:
        if not present(script):
            print("  Part %-4s %-22s MISSING - chapters %s not buildable" % (part, script, span))
            continue
        gone = [b for b in bodies_for(script) if not present(b)]
        if gone:
            print("  Part %-4s %-22s bodies missing: %s" % (part, script, ", ".join(gone)))
        else:
            print("  Part %-4s %-22s ok (%s, %s)" % (part, script, span, label))
            runnable.append((part, script))
    return runnable, missing


def run(part, script):
    print("\n" + "=" * 74)
    r = subprocess.run([sys.executable, script], cwd=G)
    if r.returncode:
        print("!! Part %s FAILED (exit %d)" % (part, r.returncode))
    return r.returncode == 0


def summarise():
    rows = []
    for f in sorted(glob.glob(OUT + "[0-9][0-9]*.html")):
        h = open(f, encoding='utf-8').read()
        w = pagewords(h)
        m = re.search(r'Era chapter \u00b7 about (\d+) minutes', h)
        rows.append((os.path.basename(f), w, int(m.group(1)) if m else 0,
                     h.count('class="check"'), h.count('class="vig"'),
                     h.count('class="meanwhile"'), h.count('<figure>')))
    if not rows:
        return 0
    print("\n" + "=" * 74)
    print("%-50s %7s %5s   %s" % ("page", "words", "min", "chk vig  mw fig"))
    bad = 0
    notes = []
    for name, w, m, c, v, mw, fig in rows:
        flag = ""
        if m and not (BAND[0] <= m <= BAND[1]):
            flag = "  <-- OUTSIDE THE %d-%d BAND" % BAND
            bad += 1
        elif m and not (TARGET[0] <= m <= TARGET[1]):
            flag = "  <-- note"
            notes.append((name, m))
        print("%-50s %7d %5d    %2d  %2d  %2d  %2d%s" % (name[:50], w, m, c, v, mw, fig, flag))
    print("%-50s %7d %5d" % ("total", sum(r[1] for r in rows), sum(r[2] for r in rows)))
    for name, m in notes:
        if m < TARGET[0]:
            print("note: %s runs %d min, under the %d target - short has meant a "
                  "missing subject, not thin prose" % (name[:44], m, TARGET[0]))
        else:
            print("note: %s runs %d min, over the %d target - check whether it is "
                  "carrying more than one page's topics" % (name[:44], m, TARGET[1]))
    return bad


if __name__ == "__main__":
    args = [a.lower() for a in sys.argv[1:]]
    runnable, missing = check()
    if "--check" in args:
        sys.exit(0)
    if missing:
        print("\n!! shared inputs missing; not building")
        sys.exit(1)
    wanted = [a for a in args if not a.startswith("-")]
    if wanted:
        runnable = [(p, s) for p, s in runnable if p.lower() in wanted]
        if not runnable:
            print("\n!! nothing matches %r; parts are: %s"
                  % (wanted, ", ".join(p for p, _, _, _ in PARTS)))
            sys.exit(1)
    ok = all(run(part, script) for part, script in runnable)
    bad = summarise()
    if bad:
        print("\n!! %d page(s) outside the %d-%d band" % (bad, BAND[0], BAND[1]))
    print("\n%s" % ("all parts built and verified" if ok else "!! at least one part failed"))
    sys.exit(0 if ok and not bad else 1)
