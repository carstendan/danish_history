# -*- coding: utf-8 -*-
"""sweep_arrows.py - every carry-forward points at a chapter that delivers it.

    python3 sweep_arrows.py            # the report
    python3 sweep_arrows.py --solvent  # also print the arrows that pass

Reads the built pages through reviewlib. LEDGER_PASS.md was the last arrow
census and it was done by grep handle and by hand; this reads every
<ul class="calls"> block and every "chapter N" in the prose, and checks:

  1. FORM. Every arrow parses as "<- N", "-> N", "-> N, M" or "-> Part X".
     "Thread" rows (Parts A-F name a running thread in the same list) are
     counted and skipped. A mix of numbers and letters in one arrow is parsed
     and reported, because HANDOFF's table of forms does not list it.
  2. DIRECTION. "->" targets a later chapter or part, "<-" an earlier one.
  3. D-1. A forward arrow names a chapter NUMBER only inside its own part or the
     next one; beyond that it names a part letter. A part letter for the next
     part is allowed and reported for information.
  4. TITLES. Parts A-D quote the target chapter's title in italics inside the
     arrow; that title must be the target's current <h1>. Titles changed at
     the renumbering and at D-10.
  5. SOLVENCY. Each arrow's anchors - its capitalised names, its Danish terms
     in <i class="dk">, its four-digit years - are looked for in the target
     chapter's reading text (any chapter of the part, for a part letter). An
     arrow whose anchors mostly do not appear in its target is listed with the
     missing ones. This is a reading list: an arrow may promise an idea rather
     than a name, and the list says which anchors were looked for, so the reading
     starts from evidence (L5: carry-forward lines must be solvent).
  6. EMPTY BLOCKS. A "What to carry forward" heading over no arrows.
  7. PROSE REFERENCES. "chapter N" / "chapters N and M" in reading text: N must
     exist, and a forward reference beyond the next part breaks D-1 as extended
     to prose (HANDOFF item 15).
  8. FOOTERS. "next: N - Title, span" must name the next chapter's current title.
  9. H1. The <h1> on the page against the <title> and index spine title, which
     are the ones arrows and footers quote.

Standard library only.
"""
import re
import sys

import reviewlib as R

YEAR = re.compile(r"\b(1\d{3}|[5-9]\d{2})\b")
CAP = re.compile(r"\b[A-ZÆØÅ][a-zæøåäöüé]{3,}(?:[-\s][A-ZÆØÅ][a-zæøåäöüé]+)?\b")
SKIP = set("""This That There These Those They Their What When Where Which While With Without
Within From Into Over Under After Before Between During Since Until Only Even Most Some Many
Much Each Every Both Neither Either Another Other Nothing Something Here Then Than Thus However
Although Because Denmark Danish Danes Chapter Part Section Part Also Just Still Once None
Whatever Whoever Like Such Same Nobody Everyone Anyone Somebody Everything Anything""".split())


def targets(spec):
    out = []
    for piece in re.split(r"\s*,\s*", spec.strip()):
        if not piece:
            continue
        m = re.match(r"^(\d+)\s*[–-]\s*(\d+)$", piece)
        if m:
            out.extend(range(int(m.group(1)), int(m.group(2)) + 1))
        elif piece.isdigit():
            out.append(int(piece))
        else:
            return None
    return out


def anchors(call):
    dk = {R.text(x) for x in re.findall(r'<i class="dk">(.*?)</i>', call["html"])}
    titles = {R.text(x) for x in re.findall(r"<i>(.*?)</i>", call["html"])}
    body = call["text"]
    for t in titles:
        body = body.replace(t, " ")
    caps = set()
    for m in CAP.finditer(body):
        w = m.group(0)
        # a capital at the start of the arrow text or after a full stop is a
        # sentence start, not a name, unless it recurs mid-sentence
        first = m.start() == 0 or re.search(r"[.!?:—]\s*$", body[:m.start()])
        if w.split()[0] in SKIP or (first and w.split()[0] not in body[m.end():]):
            continue
        caps.add(w)
    years = set(YEAR.findall(body))
    return caps, dk, years


def fold(s):
    return re.sub(r"\s+", " ", s.lower())


def main():
    show_ok = "--solvent" in sys.argv
    pages = R.load()
    P = {p.n: p for p in pages}
    TXT = {p.n: fold(p.alltext()) for p in pages}
    # The canonical title is the one in <title> and on the index spine, without
    # its number and span; the <h1> is compared with it separately (check 9).
    def doc_title(p):
        m = re.search(r"<title>(.*?)</title>", p.html, re.S)
        t = R.text(m.group(1)) if m else p.title
        t = re.sub(r"^\d+\s*\u00b7\s*", "", t)
        return re.sub(r",\s*(?:c\.\s*)?[\d,]+(?:\s*BCE)?\s*[\u2013-].*$|,\s*\d{4}$", "", t).strip()
    TITLE = {p.n: doc_title(p) for p in pages}
    h1_rows = [(p.n, p.title, TITLE[p.n]) for p in pages if fold(p.title) != fold(TITLE[p.n])]
    last = max(P)

    rows = {k: [] for k in ("form", "direction", "d1", "d1info", "title", "solvency", "empty",
                            "prose", "footer")}
    n_arrows = 0
    n_threads = 0
    solvent = []

    for p in pages:
        calls = p.calls()
        if calls is None:
            if p.n != max(P):
                rows["empty"].append((p.n, "no carry-forward block at all"))
            # the last chapter leaves an empty carry-forward out by design (D-C)
            continue
        if not calls:
            rows["empty"].append((p.n, "heading over an empty list"))
        mypart = R.part_of(p.n)
        nxt = R.next_part(mypart)
        for c in calls:
            n_arrows += 1
            if c["arrow"] == "Thread":
                n_threads += 1           # a thread note, Parts A-F: not an arrow
                n_arrows -= 1
                continue
            m = re.match("^(\u2190|\u2192)\\s*(.+)$", c["arrow"])
            if not m:
                rows["form"].append((p.n, c["arrow"], c["text"][:90]))
                continue
            fwd = m.group(1) == "\u2192"
            nums, letters, bad = [], [], False
            for piece in re.split(r"\s*,\s*", m.group(2)):
                pm = re.fullmatch(r"Part\s+([A-I])", piece)
                if pm:
                    letters.append(pm.group(1))
                else:
                    t = targets(piece)
                    if t is None:
                        bad = True
                    else:
                        nums.extend(t)
            if bad:
                rows["form"].append((p.n, c["arrow"], c["text"][:90]))
                continue
            if nums and letters:
                rows["form"].append((p.n, c["arrow"], "mixed number and part letter - parsed, checked as both"))
            elif len(letters) > 1:
                rows["form"].append((p.n, c["arrow"], "two part letters in one arrow - parsed"))
            tgt = list(nums)
            for letter in letters:
                a, b = R.part_range(letter)
                tgt.extend(range(a, b + 1))
                if fwd and a <= p.n:
                    rows["direction"].append((p.n, c["arrow"], "forward to Part %s, which is not later "
                                              "(this chapter is in Part %s)" % (letter, mypart)))
                if not fwd and b >= p.n:
                    rows["direction"].append((p.n, c["arrow"], "backward to a part that is not earlier"))
                if fwd and letter == nxt:
                    rows["d1info"].append((p.n, c["arrow"], "next part named by letter - allowed"))
            label = ", ".join([str(x) for x in nums] + ["Part " + x for x in letters])
            for t in nums:
                if t not in P:
                    rows["direction"].append((p.n, c["arrow"], "chapter %d does not exist" % t))
                elif fwd and t <= p.n:
                    rows["direction"].append((p.n, c["arrow"], "forward arrow to %d" % t))
                elif not fwd and t >= p.n:
                    rows["direction"].append((p.n, c["arrow"], "backward arrow to %d" % t))
                if fwd and R.part_of(t) not in (mypart, nxt):
                    rows["d1"].append((p.n, c["arrow"], "chapter %d is in Part %s; this is Part %s, next %s"
                                       % (t, R.part_of(t), mypart, nxt)))
            # 4. quoted titles, matched to numbered targets in order
            quoted = [R.text(x) for x in re.findall(r"<i>(.*?)</i>", c["html"])]
            if quoted and not letters and len(nums) == len(quoted):
                for t, q in zip(nums, quoted):
                    if t in TITLE and fold(q) != fold(TITLE[t]):
                        rows["title"].append((p.n, c["arrow"], q, TITLE[t]))
            # 5. solvency
            caps, dk, years = anchors(c)
            pool = " ".join(TXT[t] for t in tgt if t in TXT)
            look = [(w, "name") for w in sorted(caps)] + [(w, "term") for w in sorted(dk)] + \
                   [(y, "year") for y in sorted(years)]
            if not look:
                rows["solvency"].append((p.n, c["arrow"], label, [], [], c["text"]))
                continue
            miss = []
            for w, kind in look:
                probe = fold(w)
                # Danish definite forms and genitives: try the stem as well
                stems = {probe, re.sub(r"(ens|ets|ernes|en|et|erne|s)$", "", probe)}
                if not any(s and s in pool for s in stems):
                    miss.append((w, kind))
            if len(miss) * 2 > len(look):
                rows["solvency"].append((p.n, c["arrow"], label, look, miss, c["text"]))
            else:
                solvent.append((p.n, c["arrow"], label, look, miss))

        # 7. prose references
        for sid, head, t in p.prose():
            for m in re.finditer(r"\b[Cc]hapters?\s+((?:\d{1,2})(?:(?:,\s*|\s+and\s+|\s*[–-]\s*)\d{1,2})*)", t):
                nums = [int(x) for x in re.findall(r"\d+", m.group(1))]
                for x in nums:
                    ctx = t[max(0, m.start() - 70):m.end() + 50]
                    if x not in P:
                        rows["prose"].append((p.n, sid, "chapter %d does not exist" % x, ctx))
                    elif x > p.n and R.part_of(x) not in (mypart, nxt):
                        rows["prose"].append((p.n, sid, "forward to %d, Part %s, beyond the next part" %
                                              (x, R.part_of(x)), ctx))

        # 8. footer
        fm = re.search(r"<footer>(.*?)</footer>", p.body, re.S)
        if fm:
            ft = R.text(fm.group(1))
            nm = re.search(r"next:\s*(\d+)\s*[—-]\s*(.*?),\s*(c\.\s*)?[\d,]", ft)
            if nm:
                t = int(nm.group(1))
                if t != p.n + 1:
                    rows["footer"].append((p.n, ft[:120], "next is %d, not %d" % (t, p.n + 1)))
                elif fold(nm.group(2)) != fold(TITLE.get(t, "")):
                    rows["footer"].append((p.n, ft[:120], "title of %d is now: %s" % (t, TITLE.get(t))))

    # ---- report ------------------------------------------------------------
    def section(title, key, fmt):
        print()
        print("=" * 78)
        print(title)
        print("=" * 78)
        for r in rows[key]:
            print(fmt(r))
        print("  %d" % len(rows[key]))

    print("%d arrows and %d thread notes in %d carry-forward blocks"
          % (n_arrows, n_threads, sum(1 for p in pages if p.calls())))
    section("1. FORM - does not parse", "form", lambda r: "  %2d  %-10s %s" % r)
    section("2. DIRECTION / EXISTENCE", "direction", lambda r: "  %2d  %-10s %s" % r)
    section("3. D-1 - forward number beyond the next part", "d1", lambda r: "  %2d  %-10s %s" % r)
    section("3b. D-1, for information - next part named by letter", "d1info", lambda r: "  %2d  %-10s %s" % r)
    section("4. QUOTED TITLE is not the target's current title", "title",
            lambda r: "  %2d  %-8s quoted: %s\n                now: %s" % r)
    section("5. SOLVENCY - most anchors absent from the target", "solvency",
            lambda r: "  %2d  %-8s -> %-8s missing %s of %s\n        %s" % (
                r[0], r[1], r[2],
                ", ".join("%s" % w for w, _ in r[4]) or "-",
                ", ".join(w for w, _ in r[3]) or "(no anchors to test - read it)",
                r[5][:200]))
    section("6. EMPTY CARRY-FORWARD", "empty", lambda r: "  %2d  %s" % r)
    section("7. PROSE REFERENCES", "prose", lambda r: "  %2d  %-4s %s\n        ...%s..." % r)
    section("8. FOOTERS", "footer", lambda r: "  %2d  %s\n        %s" % r)
    print()
    print("=" * 78)
    print("9. <h1> differs from <title> and the index")
    print("=" * 78)
    for r in h1_rows:
        print("  %2d  h1: %s\n      title: %s" % r)
    print("  %d" % len(h1_rows))
    if show_ok:
        print()
        print("SOLVENT")
        for n, a, label, look, miss in solvent:
            print("  %2d %-8s -> %-8s %d/%d anchors found" % (n, a, label, len(look) - len(miss), len(look)))
    print()
    print("%d arrows; %d pass the anchor test, %d listed for reading" %
          (n_arrows, len(solvent), len(rows["solvency"])))


if __name__ == "__main__":
    main()
