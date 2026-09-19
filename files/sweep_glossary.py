# -*- coding: utf-8 -*-
"""sweep_glossary.py - the same Danish term glossed differently across the book.

    python3 sweep_glossary.py            # report
    python3 sweep_glossary.py --all      # also list every term glossed in 2+ chapters

Reads the built pages through reviewlib. Four findings, in this order:

  1. POINTER ENTRIES. A glossary <dd> that is not a definition but a note -
     "glossed in chapter N - reference, do not re-gloss." Each is checked for
     solvency: does chapter N gloss the term at all? These are reported first
     because they are on the page as written and read as an instruction to the
     author, not as a meaning.

  2. HEAD DISAGREEMENTS. For every term glossed in two or more chapters, the
     "head" of each gloss - its opening English equivalent, up to the first
     full stop, semicolon, colon, dash or comma - is compared. Where the heads
     share no content word, the term is listed with every chapter's head. That
     is how "fæste: Tenancy" (17) against "fæste: copyhold" (32) is found. A
     different head is not necessarily a fault - a gloss may define a term by
     what it did in that chapter - so this is a reading list with the evidence
     on it, not a verdict.

  3. SPELLING VARIANTS OF ONE TERM. <dt>s that fold to the same key under the
     Danish orthographic variants (aa/å, oe/ø, ae/æ, case, a trailing -en/-et/
     -erne article) but are written differently.

  4. REPEATED GLOSS INSIDE ONE CHAPTER. The same term glossed twice on one page.

Terms are matched on a folded key: lower case, italics and brackets dropped,
whitespace collapsed. Nothing is typed: chapters come from the directory.
"""
import re
import sys
from collections import defaultdict

import reviewlib as R

STOP = set("""a an the of to in and or for by on at with as from is was be it its
that this which who what when where how one two three first also any all not no
used term word danish literally lit usually often called here there under into
out than then their his her he she they them i e g""".split())


def key(term):
    t = term.lower()
    t = re.sub(r"[()\[\]'‘’\"“”*]", "", t)
    t = re.sub(r"\s+", " ", t).strip(" .,;:")
    return t


def fold(term):
    t = key(term)
    t = t.replace("aa", "å").replace("oe", "ø").replace("ae", "æ")
    t = t.replace("ö", "ø").replace("ä", "æ")
    t = re.sub(r"(erne|ene|en|et|ne|n)$", "", t)
    t = t.replace("-", "").replace(" ", "")
    return t


POINTER = re.compile(r"^\s*(?:see|glossed in|as in)\b.*?\bchapters?\s+([\d ,and]+)", re.I)


def members(term):
    parts = re.split(r",\s*|\s+/\s+|\s+and\s+|\s+og\s+", term)
    return [key(x) for x in parts if len(parts) > 1 and key(x)]


def head(dd):
    h = re.split(r"\.\s|;|:|\s[—–-]\s|,|\(", dd, maxsplit=1)[0]
    return h.strip(" .")


def content_words(s):
    return {w for w in re.findall(r"[a-zà-ÿ]+", s.lower()) if w not in STOP and len(w) > 2}


def main():
    show_all = "--all" in sys.argv
    pages = R.load()
    by_key = defaultdict(list)          # key -> [(ch, sid, term, dd)]
    pointers = []
    per_page_dupes = []
    for p in pages:
        seen = defaultdict(list)
        for t in p.terms():
            k = key(t["term"])
            m = POINTER.match(t["dd"])
            if m:
                nums = [int(x) for x in re.findall(r"\d+", m.group(1))]
                pointers.append((p.n, t["sid"], t["term"], t["dd"], nums))
            else:
                # a compound <dt> - "Rigsdagen, Folketinget, Landstinget" - glosses
                # each member; index it under every one of them as well as whole
                for kk in {k} | set(members(t["term"])):
                    by_key[kk].append((p.n, t["sid"], t["term"], t["dd"]))
            seen[k].append(t["sid"])
        for k, sids in seen.items():
            if len(sids) > 1:
                per_page_dupes.append((p.n, k, sids))

    # ---- 1. pointer entries -------------------------------------------------
    print("=" * 78)
    print("1. POINTER ENTRIES - a glossary definition that is a note, not a meaning")
    print("=" * 78)
    insolvent = 0
    for n, sid, term, dd, nums in pointers:
        k = key(term)
        # a gloss under the same key, or under a variant spelling or article form
        f = fold(term)
        hits = {c for kk, v in by_key.items() if kk == k or fold(kk) == f for c, _, _, _ in v}
        ok = [x for x in nums if x in hits]
        verdict = "target glosses it" if len(ok) == len(nums) else \
                  "TARGET DOES NOT GLOSS IT (glossed in: %s)" % (", ".join(map(str, sorted(hits))) or "nowhere")
        if len(ok) != len(nums):
            insolvent += 1
        print("  %2d %-4s %-26s -> %-8s %s" % (n, sid, term[:26], ",".join(map(str, nums)), verdict))
        print("          dd: %s" % dd)
    print("  %d pointer entries on %d pages; %d point at a chapter that does not gloss the term"
          % (len(pointers), len({p[0] for p in pointers}), insolvent))

    # ---- 2. head disagreements ---------------------------------------------
    print()
    print("=" * 78)
    print("2. ONE TERM, DIFFERENT HEADS - glossed in 2+ chapters, heads share no content word")
    print("=" * 78)
    multi = {k: v for k, v in by_key.items() if len({c for c, _, _, _ in v}) > 1}
    flagged = 0
    for k in sorted(multi, key=lambda k: min(c for c, _, _, _ in multi[k])):
        rows = multi[k]
        heads = [(c, sid, head(dd)) for c, sid, _, dd in rows]
        words = [content_words(h) for _, _, h in heads]
        disjoint = any(not (words[i] & words[j]) for i in range(len(words))
                       for j in range(i + 1, len(words)) if heads[i][0] != heads[j][0])
        if disjoint or show_all:
            flagged += disjoint
            print("  %s%s" % (k, "" if disjoint else "   (heads agree)"))
            for c, sid, h in heads:
                print("      %2d %-4s %s" % (c, sid, h[:90]))
    print("  %d terms glossed in more than one chapter; %d with heads that share no content word"
          % (len(multi), flagged))

    # ---- 3. spelling variants ----------------------------------------------
    print()
    print("=" * 78)
    print("3. ONE TERM, SPELT DIFFERENTLY in the <dt>")
    print("=" * 78)
    by_fold = defaultdict(set)
    where = defaultdict(set)
    for k, rows in by_key.items():
        for c, _, term, _ in rows:
            by_fold[fold(k)].add(term.strip())
            where[term.strip()].add(c)
    nvar = 0
    for f, forms in sorted(by_fold.items()):
        lower = {x.lower() for x in forms}
        if len(lower) > 1:
            nvar += 1
            print("  " + "  |  ".join("%s (%s)" % (x, ",".join(map(str, sorted(where[x]))))
                                      for x in sorted(forms)))
    print("  %d groups" % nvar)

    # ---- 4. same page twice -------------------------------------------------
    print()
    print("=" * 78)
    print("4. ONE TERM GLOSSED TWICE ON ONE PAGE")
    print("=" * 78)
    for n, k, sids in per_page_dupes:
        print("  %2d  %-30s %s" % (n, k, ", ".join(sids)))
    print("  %d" % len(per_page_dupes))


if __name__ == "__main__":
    main()
