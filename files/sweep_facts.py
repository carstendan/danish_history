# -*- coding: utf-8 -*-
"""sweep_facts.py - dates and figures that appear in more than one chapter must agree.

    python3 sweep_facts.py

Reads every reader-facing unit of the built pages (prose, vignettes, glossary,
figure captions, Meanwhile, myth-check, summaries, questions, sources) through
reviewlib and reports four kinds of candidate disagreement. Every row carries
both sentences, so the reading is done against the evidence and not from memory.

  1. NAMED EVENTS, DIFFERENT YEARS. "Peace of Roskilde", "Battle of Dybbøl",
     "Treaty of Kiel" ... - an event name followed within a few words by a year.
     The same event dated to two different years is listed.

  2. LIFE DATES. "Name (1234-1290)" or "(b. 1234)" - the same name given
     different life dates.

  A distinctive name is one that appears in two to eight chapters. Every date,
  year and count is tied to the distinctive names within ten words of it in
  the same sentence. Then, for each name:

  3. NEAR-MISS FULL DATES. Two full dates within 31 days of each other that
     never appear together in one chapter - the shape of one event dated twice.

  4. NEAR-MISS YEARS. "Kanslergade 1933", "Landmandsbanken in 1922" - a name
     directly followed by a year; two years at most two apart, never together.

  5. DIFFERENT COUNTS. The same name and the same noun ("7,400 Jews") with
     numbers that differ by less than half and do not agree to two significant
     figures (so 21,800 and 22,000 is rounding, not a disagreement). Numbers
     written in words with a scale word ("twenty-two thousand", "a hundred and
     eighty-four") are converted to digits first; the prose writes most of its
     counts that way.

A candidate is not a verdict. A treaty signed in one year and ratified in the
next, a date given in two calendar styles (D-6), a count that genuinely changed
- all of these are listed and then read. The report says so row by row in
REVIEW-CONSISTENCY.md, not here.
"""
import re
from collections import defaultdict
from itertools import combinations

import reviewlib as R

MONTHS = ("January February March April May June July August September October "
          "November December").split()
MON = {m: i + 1 for i, m in enumerate(MONTHS)}
DATE = re.compile(r"\b(\d{1,2})\s+(%s)\s+(\d{3,4})\b" % "|".join(MONTHS))
YEAR = re.compile(r"\b(1\d{3}|[5-9]\d{2})\b")

EVENT = re.compile(
    r"\b((?:Peace|Treaty|Battle|Siege|Diet|Recess|Union|Ordinance|Act|Constitution|Congress|"
    r"Convention|Agreement|Declaration|Rescript|Charter|Settlement|Truce|Armistice|Conference|"
    r"Fire|Plague|Bombardment|Election|Referendum)\s+of\s+(?:the\s+)?"
    r"[A-ZÆØÅ][\wÀ-ɏ]+(?:[\s-][A-ZÆØÅ][\wÀ-ɏ]+)?)")

LIFE = re.compile(r"\b([A-ZÆØÅ][\wÀ-ɏ.]+(?:\s+[A-ZÆØÅ][\wÀ-ɏ.]+){0,3})\s*"
                  r"\((?:c\.\s*)?(\d{3,4})\s*[–-]\s*(?:c\.\s*)?(\d{2,4})\)")

NUMNOUN = re.compile(r"(?<![\d.,])(\d{1,3}(?:,\d{3})+|\d{3,})(?:\s+(?:per\s+cent|percent))?\s+"
                     r"(?:(?:more|fewer|of|the|Danish|German|Swedish|Norwegian|Jewish|new|old)\s+){0,2}"
                     r"([A-Za-zæøå]{4,})")

CAPWORD = re.compile(r"\b[A-ZÆØÅ][a-zæøåäöüé]{3,}\b")
COMMON = set("""This That There These Those They Their What When Where Which While With Without
Within From Into Over Under After Before Between During Since Until Only Even Most Some Many
Much Each Every Both Neither Either Another Other Others Nothing Something Everything Here
Then Than Thus However Although Because Denmark Danish Danes Sweden Swedish Norway Norwegian
Germany German Germans England English Copenhagen Chapter Part Section Figure Meanwhile
Vignette Narrative Questions Sources Summary Checkpoint January February March April June
July August September October November December King Queen Church Crown Council North South
East West Europe European Baltic Christian Frederik Jutland Zealand Holstein Schleswig Slesvig
Skåne Also Just Still Once None""".split())


UNITS = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
    "fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {w: 10 * i for i, w in enumerate("_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()) if w != "_"}
SCALE = {"hundred": 100, "thousand": 1000, "million": 1000000}
NUMWORD = r"(?:%s)" % "|".join(sorted(list(UNITS) + list(TENS) + list(SCALE) + ["a", "and"], key=len, reverse=True))
NUMRUN = re.compile(r"\b(?:%s)(?:[\s-]+(?:%s))*\b" % (NUMWORD, NUMWORD), re.I)


def words_to_int(run):
    """'twenty-two thousand' -> 22000, 'a hundred and eighty-four' -> 184, else None."""
    toks = [t for t in re.split(r"[\s-]+", run.lower()) if t]
    while toks and toks[0] == "and":
        toks.pop(0)
    while toks and toks[-1] in ("and", "a"):
        toks.pop()
    if not toks or not any(t in SCALE for t in toks):
        return None                    # "twenty-two" alone is not a count worth comparing
    total, cur, seen = 0, 0, False
    for t in toks:
        if t == "a":
            cur = cur or 1
        elif t == "and":
            continue
        elif t in UNITS:
            cur += UNITS[t]; seen = True
        elif t in TENS:
            cur += TENS[t]; seen = True
        elif t == "hundred":
            cur = (cur or 1) * 100; seen = True
        else:
            total += (cur or 1) * SCALE[t]; cur = 0; seen = True
    return total + cur if seen else None


def digits_for_words(s):
    """Rewrite number-word runs as digits so prose counts can be compared."""
    def rep(m):
        v = words_to_int(m.group(0))
        if v is None:
            return m.group(0)
        lead = re.match(r"(?i)(and\s+)", m.group(0))
        return (lead.group(1) if lead else "") + format(v, ",")
    return NUMRUN.sub(rep, s)


def norm_num(s):
    return int(s.replace(",", ""))


def same_to_2sf(a, b):
    def sf(x):
        if x == 0:
            return 0
        k = len(str(abs(x))) - 2
        return round(x / 10 ** k) * 10 ** k if k > 0 else x
    return sf(a) == sf(b)


def main():
    pages = R.load()
    sents = []                           # (ch, sid, sentence)
    for p in pages:
        for label, sid, t in p.blocks_text():
            for s in R.sentences(t):
                # apparatus lists run for hundreds of words without a full stop;
                # their items are separated by a spaced dash
                for piece in (re.split(r"\s[\u2014\u00b7]\s", s) if len(s) > 300 else [s]):
                    if piece.strip():
                        sents.append((p.n, sid, digits_for_words(piece.strip())))

    # ---- 1. named events ----------------------------------------------------
    ev = defaultdict(lambda: defaultdict(set))
    ev_ctx = {}
    for ch, sid, s in sents:
        for m in EVENT.finditer(s):
            tail = s[m.end():m.end() + 24]
            y = YEAR.search(tail)
            if y and not re.search(r"[.;\u2014\u2190\u2192]", tail[:y.start()]):
                name = re.sub(r"\s+", " ", m.group(1))
                ev[name][int(y.group(1))].add(ch)
                ev_ctx[(name, int(y.group(1)), ch)] = s
    print("=" * 78)
    print("1. NAMED EVENTS GIVEN DIFFERENT YEARS")
    print("=" * 78)
    n1 = 0
    for name in sorted(ev):
        if len(ev[name]) > 1:
            n1 += 1
            print("  " + name)
            for y in sorted(ev[name]):
                for ch in sorted(ev[name][y]):
                    print("      %d  ch %2d  %s" % (y, ch, ev_ctx[(name, y, ch)][:150]))
    print("  %d" % n1)

    # ---- 2. life dates ------------------------------------------------------
    life = defaultdict(lambda: defaultdict(set))
    for ch, sid, s in sents:
        for m in LIFE.finditer(s):
            a, b = m.group(2), m.group(3)
            if len(b) == 2:
                b = a[:2] + b
            if int(b) < int(a) or int(b) - int(a) > 110:
                continue
            nm = m.group(1).split()[-1]      # key on the surname
            life[nm][(int(a), int(b))].add((ch, m.group(1)))
    print()
    print("=" * 78)
    print("2. ONE NAME, DIFFERENT LIFE DATES (keyed on the last word of the name)")
    print("=" * 78)
    n2 = 0
    for nm in sorted(life):
        if len(life[nm]) > 1:
            n2 += 1
            print("  " + nm)
            for span in sorted(life[nm]):
                print("      %d-%d  %s" % (span[0], span[1],
                                          "; ".join("ch %d %s" % x for x in sorted(life[nm][span]))))
    print("  %d names (a surname shared by two people is listed too - read it)" % n2)

    # ---- anchors ----------------------------------------------------------------
    # A distinctive name appears in two to eight chapters: common enough to recur,
    # rare enough that two mentions are probably of one thing.
    chapters_of = defaultdict(set)
    for ch, sid, s in sents:
        for w in set(CAPWORD.findall(s)):
            chapters_of[w].add(ch)
    distinctive = {w for w, c in chapters_of.items()
                   if 2 <= len(c) <= 8 and w not in COMMON}

    # Every fact is tied to the distinctive names within WINDOW words of it,
    # inside the same sentence.
    WINDOW = 10
    fdate = defaultdict(lambda: defaultdict(set))   # anchor -> date -> {(ch, sid, ctx)}
    fyear = defaultdict(lambda: defaultdict(set))   # anchor -> year (adjacent only)
    fcount = defaultdict(lambda: defaultdict(set))  # (anchor, noun) -> value
    for ch, sid, s in sents:
        toks = [(m.start(), m.group(0)) for m in re.finditer(r"\S+", s)]
        starts = [t[0] for t in toks]

        def near(pos, width):
            i = max(0, min(range(len(starts)), key=lambda k: abs(starts[k] - pos)) if starts else 0)
            lo, hi = max(0, i - width), min(len(toks), i + width + 1)
            return {w for _, t in toks[lo:hi] for w in CAPWORD.findall(t) if w in distinctive}

        for m in DATE.finditer(s):
            d = (int(m.group(1)), MON[m.group(2)], int(m.group(3)))
            for a in near(m.start(), WINDOW):
                fdate[a][d].add((ch, sid, s))
        alts = "|".join(re.escape(w) for w in set(CAPWORD.findall(s)) if w in distinctive)
        if alts:
            for m in re.finditer(r"\b(%s)\s+(?:in\s+|of\s+|\()?(1\d{3})\b" % alts, s):
                fyear[m.group(1)][int(m.group(2))].add((ch, sid, s))
        for m in NUMNOUN.finditer(s):
            v = norm_num(m.group(1))
            if 1000 <= v <= 2100 and "," not in m.group(1):
                continue
            noun = m.group(2).rstrip("s")
            anchors = near(m.start(), WINDOW)
            if m.group(2)[0].isupper():
                anchors.add("(%s)" % noun)          # "7,056 Jews": the noun is its own anchor
            for a in anchors:
                fcount[(a, noun)][v].add((ch, sid, s))

    def chs(rows):
        return {r[0] for r in rows}

    def show(r):
        return "ch %2d %-7s %s" % (r[0], r[1], r[2][:230])

    # ---- 3. dates -------------------------------------------------------------
    print()
    print("=" * 78)
    print("3. ONE NAME, NEAR-MISS FULL DATES - within 31 days, never together in one chapter")
    print("=" * 78)
    import datetime
    rows3 = []
    for a, dd in fdate.items():
        for d1, d2 in combinations(sorted(dd), 2):
            c1, c2 = chs(dd[d1]), chs(dd[d2])
            if c1 & c2:
                continue
            try:
                gap = abs((datetime.date(d1[2], d1[1], d1[0]) - datetime.date(d2[2], d2[1], d2[0])).days)
            except ValueError:
                continue
            if 0 < gap <= 31:
                rows3.append((a, d1, d2, dd[d1], dd[d2]))
    for a, d1, d2, r1, r2 in rows3:
        print("  %s: %d %s %d  vs  %d %s %d" % (a, d1[0], MONTHS[d1[1] - 1], d1[2], d2[0], MONTHS[d2[1] - 1], d2[2]))
        print("      " + show(sorted(r1)[0]))
        print("      " + show(sorted(r2)[0]))
    print("  %d" % len(rows3))

    # ---- 4. years ---------------------------------------------------------------
    print()
    print("=" * 78)
    print("4. ONE NAME, NEAR-MISS YEARS - 'Kanslergade 1933', within two years, never together")
    print("=" * 78)
    rows4 = []
    for a, yy in fyear.items():
        for y1, y2 in combinations(sorted(yy), 2):
            c1, c2 = chs(yy[y1]), chs(yy[y2])
            if 0 < y2 - y1 <= 2 and not (c1 & c2):
                rows4.append((a, y1, y2, yy[y1], yy[y2]))
    for a, y1, y2, r1, r2 in rows4:
        print("  %s: %d (%s)  vs  %d (%s)" % (a, y1, ",".join(map(str, sorted(chs(r1)))),
                                            y2, ",".join(map(str, sorted(chs(r2))))))
        print("      " + show(sorted(r1)[0]))
        print("      " + show(sorted(r2)[0]))
    print("  %d" % len(rows4))

    # ---- 5. counts -------------------------------------------------------------
    print()
    print("=" * 78)
    print("5. ONE NAME, ONE NOUN, DIFFERENT COUNTS - within half, not equal to 2 s.f.")
    print("=" * 78)
    rows5 = []
    for (a, noun), vv in fcount.items():
        for v1, v2 in combinations(sorted(vv), 2):
            c1, c2 = chs(vv[v1]), chs(vv[v2])
            if c1 & c2 or same_to_2sf(v1, v2):
                continue
            if (v2 - v1) / v2 < 0.5:
                rows5.append((a, noun, v1, v2, vv[v1], vv[v2]))
    seen = set()
    for a, noun, v1, v2, r1, r2 in rows5:
        k = (noun, v1, v2)
        if k in seen:
            continue
        seen.add(k)
        print("  %s %s: %s vs %s" % (a, noun, format(v1, ","), format(v2, ",")))
        print("      " + show(sorted(r1)[0]))
        print("      " + show(sorted(r2)[0]))
    print("  %d" % len(seen))


if __name__ == "__main__":
    main()
