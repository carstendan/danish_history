# -*- coding: utf-8 -*-
"""
renumber.py — one-pass chapter renumbering for the Danish history series.

WHY THIS EXISTS
---------------
Chapter 16 was written, measured at 46 minutes, and split afterwards into 16a and
16b. That left every later reference to "chapter 16" ambiguous: it may mean the
making of the union (now 16) or the union at work (now 17). A blind numeric shift
would leave roughly half of them pointing at the wrong page, and a wrong link is
indistinguishable from a right one once it is written.

So this script does not guess. Ambiguous references must be listed in RESOLVE,
keyed by a snippet unique within its file. If any unresolved "chapter 16" survives
the pass, --apply refuses to write anything at all.

THE MAPPING
-----------
    01-15  unchanged        20 -> 21   Part F opens, one page
    16a -> 16               21 -> 22   Christian 4. becomes 22 AND 23
    16b -> 17               22 -> 24
    17  -> 18               23+ -> +2
    18  -> 19
    19  -> 20               42 chapters total; Part E is 16-20, Part F 21-24

USAGE
-----
    python3 renumber.py --census        # read-only, writes census.txt
    python3 renumber.py --apply --dry   # shows what would change, writes nothing
    python3 renumber.py --apply         # renames and rewrites, leaves .bak files

Run it in the folder holding the chapter pages; it also descends into files/.
Pages are renamed, never copied, so no stale NN*.html is left for
index_generator.py to glob.
"""
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SUBDIRS = ["", "files"]
FILE_EXT = (".html", ".md")


def newnum(old):
    """old is '16a', '16b' or a number as a string. None means ambiguous."""
    if old == "16a":
        return 16
    if old == "16b":
        return 17
    n = int(old)
    if n <= 15:
        return n
    if n == 16:
        return None
    if n <= 19:
        return n + 1
    if n == 20:
        return 21
    if n == 21:
        return 22
    return n + 2


# (label, pattern, which group holds the number)
# Arrow calls carry comma lists - "<b>→ 25, 27</b>", "<b>← 3, 4, 5</b>" - so the
# whole list is captured and every member renumbered. Catching only the first
# member silently leaves the rest pointing at the old scheme, which is worse than
# not running at all.
REFS = [
    ("prose",  re.compile(r"\bchapter (16[ab]|\d\d?)\b"), 1),
    ("Prose",  re.compile(r"\bChapter (16[ab]|\d\d?)\b"), 1),
    ("plural", re.compile(r"\bchapters (\d\d?(?:\s*[,\u2013-]\s*\d\d?)*)\b"), 1),
    ("call",   re.compile(r"([\u2190\u2192])\s*(\d\d?(?:\s*,\s*\d\d?)*)\b"), 2),
    ("next",   re.compile(r"(next:\s*(?:Part [A-I] \u2014 )?)(\d\d?)\b"), 2),
    # Parts A-D reference forward chapters as a bare number in brackets:
    # "the slave trade (25)", "1864 (31)", "the agrarian reforms of the 1780s (26)".
    # Chapters 11 and 12 contain ONLY this form, so without it they would be
    # left on the old scheme and would not even show up as changed files.
    # Restricted to 16+ because anything at or below 15 keeps its number anyway.
    ("paren",  re.compile(r"\((1[6-9]|[2-4]\d)\)"), 1),
    # Bare 16a/16b: page titles, crumbs, and the calls between the two halves.
    # Must run after "prose", or "chapter 16a" would be reduced to "chapter 16"
    # and then flagged as ambiguous by a pattern that has already gone past.
    ("ab",     re.compile(r"\b16[ab]\b"), 0),
]

MONTHS = ("January|February|March|April|May|June|July|August|September|"
          "October|November|December")

# Things the numeric rule must not touch blind. Census lists them; each is either
# resolved by hand into RESOLVE or confirmed harmless.
REVIEW = [
    # "the Reformation in 19", "the Napoleonic wars in 28" - a chapter reference
    # with no keyword in front of it
    ("bare-in",  re.compile(r"\bin (1[6-9]|[23]\d|4\d)\b(?!\s*(?:%s)|\d)" % MONTHS)),
    # "Genforeningen's story (35)"
    ("paren",    re.compile(r"\((1[6-9]|[23]\d|4\d)\)")),
    ("pagefile", re.compile(r"\b\d\d[ab]?-[a-z0-9-]+\.html")),
    ("bodyfile", re.compile(r"\bc\d\d[ab]?_body\.html")),
    ("ab",       re.compile(r"\b16[ab]\b")),
]

PAGES = [
    ("19-reformation-and-the-counts-feud.html",
     "20-reformation-and-the-counts-feud.html"),
    ("18-schleswig-holstein-and-the-unions-collapse.html",
     "19-schleswig-holstein-and-the-unions-collapse.html"),
    ("17-sound-dues-the-hanse-and-a-straining-union.html",
     "18-sound-dues-the-hanse-and-a-straining-union.html"),
    ("16b-the-union-at-work.html", "17-the-union-at-work.html"),
    ("16a-margrete-i-and-the-making-of-the-union.html",
     "16-margrete-i-and-the-making-of-the-union.html"),
]

BODIES = [
    ("c19_body.html", "c20_body.html"),
    ("c18_body.html", "c19_body.html"),
    ("c17_body.html", "c18_body.html"),
    ("c16b_body.html", "c17_body.html"),
    ("c16a_body.html", "c16_body.html"),
]

# Ambiguous "chapter 16" references, resolved by hand against the text of both
# halves (see peek.py output). 16a became 16 and covers 1375-1397, ending at
# Kalmar; 16b became 17 and covers 1397-1412.
#
# Values use {16}/{17} rather than bare numerals so that the numeric sweep cannot
# see them and shift them again - braces are stripped at the very end. Two entries
# also correct a title and a date range that the split retired and nobody updated.
RESOLVE = {
    # --- chapter 15, pointing into Part E ---
    "the subject of chapter 16 and":
        "the subject of chapter {16} and",
    "Chapter 16, <i>Margrete I and the Kalmar Union</i>,":
        "Chapter {16}, <i>Margrete I and the making of the union</i>,",
    "<li><b>\u2192 16</b><span>Margrete, married at ten":
        "<li><b>\u2192 {16}</b><span>Margrete, married at ten",
    "next: Part E, chapter 16 \u2014 Margrete I and the Kalmar Union, 1375\u20131412":
        "next: Part E, chapter {16} \u2014 Margrete I and the making of the union, 1375\u20131397",

    # --- chapter 17 (becomes 18) ---
    # one sentence spanning both halves: enfeoffed 1386 in 16a, killed 1404 in 16b
    "chapter 16 left Gerhard 6. enfeoffed with the duchy":
        "chapter {16} left Gerhard 6. enfeoffed with the duchy",
    "in 1386 and killed in Ditmarsken in 1404.":
        "in 1386, and chapter {17} saw him killed in Ditmarsken in 1404.",
    "in chapter 16. He was in Denmark for the coup":
        "in chapter {17}. He was in Denmark for the coup",
    "deserted farms of chapter 16 had":
        "deserted farms of chapter {17} had",
    "<p>Chapter 16 left the Danish countryside":
        "<p>Chapter {17} left the Danish countryside",
    "<li><b>\u2190 16</b><span>The deserted farms become pasture":
        "<li><b>\u2190 {17}</b><span>The deserted farms become pasture",
    "shrine of chapter 16.":
        "shrine of chapter {17}.",

    # --- chapter 18 (becomes 19) ---
    "Tributary land, from chapter 16.":
        "Tributary land, from chapter {16}.",
    "In chapter 16 the western panel filled":
        "In chapter {16} the western panel filled",
    "process chapter 16 described":
        "process chapter {17} described",
    "Chapter 16 noted that it had killed Gerhard 6.":
        "Chapter {17} noted that it had killed Gerhard 6.",
    "out of chapter 16's deserted farms":
        "out of chapter {17}'s deserted farms",
    "<li><b>\u2190 16</b><span>Orkney and Shetland entered":
        "<li><b>\u2190 {16}</b><span>Orkney and Shetland entered",
    "Abraham Brodersen was beheaded in chapter 16.":
        "Abraham Brodersen was beheaded in chapter {17}.",

    # --- chapter 19 (becomes 20) ---
    "Chapter 16 watched the Danish peasantry":
        "Chapter {17} watched the Danish peasantry",
    "chapter 16 watched the pious gifts":
        "chapter {17} watched the pious gifts",
    "<li><b>\u2190 16</b><span>Four centuries of":
        "<li><b>\u2190 {17}</b><span>Four centuries of",

    # --- bare numbers in prose, chapter 06. Automating "in NN" is unsafe
    # ("in 17 years", "in 20 minutes"), so this one sentence is done by hand.
    "the Reformation in 19, the Napoleonic wars in 28,":
        "the Reformation in {20}, the Napoleonic wars in {30},",
}

# HANDOFF.md talks *about* the numbering rather than referring to chapters, so a
# substitution would produce nonsense - "Chapter 16 is 46 minutes, split at Kalmar"
# is a resolved open item, not a cross-reference. Rewritten by hand instead.
SKIP = {"HANDOFF.md"}


def targets():
    for sub in SUBDIRS:
        d = os.path.join(ROOT, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith(FILE_EXT) and not f.startswith(".") and f not in SKIP:
                yield os.path.join(d, f)


def context(line, m, width=70):
    s = line.strip()
    if len(s) <= 150:
        return s
    a = max(0, m.start() - width)
    return "..." + line[a:m.end() + width].strip() + "..."


def maplist(s):
    """'25, 27' -> '27, 29'. Returns None if any member is ambiguous."""
    parts = re.split(r"(\s*[,\u2013-]\s*)", s)
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(p)
            continue
        n = newnum(p.strip())
        if n is None:
            return None
        out.append(str(n))
    return "".join(out)


def census():
    rows, ambig, review = [], [], []
    for path in targets():
        rel = os.path.relpath(path, ROOT)
        text = open(path, encoding="utf-8", errors="replace").read()
        for i, line in enumerate(text.splitlines(), 1):
            for _, pat, g in REFS:
                for m in pat.finditer(line):
                    old = m.group(g)
                    new = maplist(old) if "," in old or "\u2013" in old else (
                        None if newnum(old) is None else str(newnum(old)))
                    ctx = context(line, m)
                    if new is None:
                        ambig.append((ctx, rel, i))
                        rows.append("%-44s L%-5d %s  <<< AMBIGUOUS" % (rel, i, ctx))
                    else:
                        rows.append("%-44s L%-5d %s  -> %s" % (rel, i, ctx, new))
            for label, pat in REVIEW:
                for m in pat.finditer(line):
                    review.append(("[%s] %s" % (label, context(line, m)), rel, i))

    def dedupe(items):
        seen, out = set(), []
        for ctx, rel, i in items:
            if ctx in seen:
                continue
            seen.add(ctx)
            out.append("%-44s L%-5d %s" % (rel, i, ctx))
        return out

    amb_u, rev_u = dedupe(ambig), dedupe(review)
    write("census.txt", rows)
    write("census-ambiguous.txt", amb_u)
    write("census-review.txt", rev_u)
    print("%d references; %d ambiguous (%d unique); %d for review (%d unique)"
          % (len(rows), len(ambig), len(amb_u), len(review), len(rev_u)))
    print("-> census.txt, census-ambiguous.txt, census-review.txt")


def write(name, lines):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def rewrite(text):
    """RESOLVE first, writing {16}/{17} which the numeric sweep cannot match;
    then the sweep; then unwrap the braces. Doing RESOLVE first with bare
    numerals would let the sweep shift a just-resolved 17 to 18."""
    for old, new in RESOLVE.items():
        text = text.replace(old, new)

    unresolved = []

    def one(m, g):
        new = maplist(m.group(g))
        if new is None:
            unresolved.append(m.group(0))
            return m.group(0)
        whole, base = m.group(0), m.start(0)
        # keep whatever follows the number as well as whatever precedes it -
        # the bracket pattern has a ")" after the group, and dropping it turned
        # "(25)" into "(27".
        return whole[:m.start(g) - base] + new + whole[m.end(g) - base:]

    for _, pat, g in REFS:
        text = pat.sub(lambda m, g=g: one(m, g), text)

    text = re.sub(r"\{(\d\d)\}", r"\1", text)
    return text, unresolved


def apply_all(dry):
    problems, plan = {}, {}
    for path in targets():
        text = open(path, encoding="utf-8").read()
        new, un = rewrite(text)
        if un:
            problems[os.path.relpath(path, ROOT)] = sorted(set(un))
        if new != text:
            plan[path] = new

    if problems:
        print("REFUSING TO WRITE - unresolved ambiguous references:\n")
        for f, un in problems.items():
            print("  %-44s %s" % (f, ", ".join(un)))
        print("\nAdd each to RESOLVE, then re-run.")
        return 1

    print("%d files to rewrite; %d pages and %d bodies to rename."
          % (len(plan), len(PAGES), len(BODIES)))
    if dry:
        for p in sorted(plan):
            print("  would rewrite %s" % os.path.relpath(p, ROOT))
        return 0

    for path, new in plan.items():
        shutil.copy2(path, path + ".bak")
        open(path, "w", encoding="utf-8").write(new)
    for sub in SUBDIRS:
        d = os.path.join(ROOT, sub)
        for old, new in PAGES:
            o = os.path.join(d, old)
            if os.path.exists(o):
                os.rename(o, os.path.join(d, new))
                print("  %s -> %s" % (os.path.join(sub, old), new))
    d = os.path.join(ROOT, "files")
    for old, new in BODIES:
        o = os.path.join(d, old)
        if os.path.exists(o):
            os.rename(o, os.path.join(d, new))
            print("  files/%s -> %s" % (old, new))

    print("\nDone; .bak beside every rewritten file.")
    print("Still by hand: build_part_e.py CFG keys, index_generator.py E table "
          "and DENSE set, HANDOFF.md ledger, then regenerate the index.")
    return 0


if __name__ == "__main__":
    if "--census" in sys.argv:
        census()
    elif "--apply" in sys.argv:
        sys.exit(apply_all("--dry" in sys.argv))
    else:
        print(__doc__)
