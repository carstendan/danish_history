# START HERE — Part H, chapter 33

**Paste everything below the line into a new chat. Attach nothing yet.**

---

I'm writing a long-form digital history of Denmark: 43 chapters, c. 13,000 BCE to
1953, as self-contained HTML pages for Danish readers at gymnasium level. Parts A–G
are shipped and **chapter 32 is now shipped too**. Part H is chapters 32 to 36.
**This session drafts and builds chapter 33.** It does not re-plan Part H.

The project is in a git repository at `github.com/carstendan/danish_history`, and it
is public. The current version of a file is what is committed, not what happens to
be in the folder. **Clone it** — the whole toolchain runs in a container, and a
session that can run its own verifiers is worth several that cannot.

## First: the cold run

**Before reading a single planning document.** From `files/`, reporting what fails
rather than working around it:

```
git status --short
python3 tidy.py
python3 mapfixture.py
python3 seamcheck.py
python3 debuild.py verify ../[0-9][0-9]-*.html
DK_CHAPTERS="$PWD/.." python3 bookstats.py
python3 vignettes.py .
python3 vignettes.py --selftest
python3 figcheck.py
python3 narrative.py ../2[5-9]-*.html ../3[0-2]-*.html
```

**Expected, as of the end of the chapter 32 session:**

- `tidy.py` — no collisions, **no orphans**, no two-generations. Missing: **ten**
  Part D figures, which have no generators and cannot be remade. Nothing else.
- `mapfixture.py`, `seamcheck.py` — pass on **six** maps; 1814 was added.
- `debuild.py verify` — `style-only` for 01–11, `identical` for **12–32**.
  `style-only` is not damage. **Anything reporting `BODY DRIFT` is serious.**
- `bookstats.py` — 43 in the spine, **32 built**, 227,813 page words, 18.1 h.
- `vignettes.py` — three per chapter for 16–32, **51 total**. Copenhagen normalises
  to **13**. D-9: chapter **32 passes** (`3/3 tagged, [f] yes, [n] yes`); 16–31
  report `untagged`, which is the lazy backfill and not a fault.
- `figcheck.py` — **51 matched, 41 sourceless, 0 stale.** The 41 are Parts A–D,
  whose figures exist only inside their pages.
- `narrative.py` — apparatus constant **3524**; chapter 32 reports ten sections.

**Also expected, and not a fault:** every figure script now runs four guards via
`mapspine.check()`, and exactly one thing fires anywhere in the book —
`svg_terr_1660.txt` collides `Skåne`/`Helsingborg` and `Jämtland`/`Trondhjem`. That
is **open item 43**, left deliberately.

**If any of these differs, stop and say so before doing anything else.** A verifier
that disagrees with the ledger is either a real fault or a stale ledger, and both
matter more than the work.

## Then read, in this order

1. `HANDOFF.md` — the governing ledger, **open items 1 to 43**. Bare numbers are
   items; lessons carry an `L` prefix. Conventions D-1 to D-9 are closed. **D-9 was
   amended in September 2026** to add the `[-]` sentinel — read that entry, because
   without it the check cannot see its own founding case.
2. `PLAN_H.md` — §6 is chapter 33. §2 records six decisions taken at plan time that
   are **not** to be reopened.
3. `REVIEW-PART-G.md` — what a part gets wrong, and how it was found.

## What this session does, in order

**1. Research chapter 33 against the plan.** Chapter 32's research moved something
in nine of its ten sections; expect the same. Three findings belong to 33 and are
not in the plan, because they were found after it was written:

- The **language patent of 29 March 1844**, granting the right to speak Danish in
  the Slesvig assembly only to members who did not consider themselves sufficiently
  master of German. Aimed at Hiort Lorenzen, and it hit him exactly: he spoke
  German, so he could not speak Danish.
- The **Danish walkout** that followed, leaving the Schleswig-Holstein majority
  unopposed, and the banning of the Slesvigske Forening with prosecution of its
  board.
- The **second Skamlingsbanke meeting, 4 July 1844** — twelve thousand people,
  Grundtvig speaking, twice the previous year's crowd.

Chapter 32 sets all three up and stops. Chapter 33 assembles the Slesvig legal case
(PLAN_H §2, not to be reopened).

**2. Draft chapter 33.** Prose only, into `c33_draft.md`. Follow `c32_draft.md`'s
shape: one file, apparatus appended, questions as numbered lists under each tier
heading — prose paragraphs there parse as zero questions and the build says so.

**3. Build it.** `mkbody.py` needs a `HAND` entry for 33 and runs as
`DK_DRAFT=c33_draft.md python3 mkbody.py 33`. `build_part_h.py` needs a `CFG` entry
with three checkpoints keyed to section title fragments. Copy chapter 32's and
change everything.

## What this session does not do

- Re-plan Part H. The six decisions in `PLAN_H.md` §2 are made.
- Touch Parts A–D. No retained bodies for 01–15, no figure generators for 12–15.
  Documented, accepted, not a fault to rediscover. **Any change that makes a Part
  A–D figure stale cannot be undone** — check the blast radius before applying, as
  item 39 now records.
- Draft 34 to 36.

## Open, and needing me

- **Item 43** — the 1660 map's label collisions. Cosmetic, real, and fixing them
  rebuilds chapter 25's page. My call.
- **Nobody has looked at chapter 32's three figures on my machine.** `cairosvg` is
  not installed; `python3 mapdump.py` builds a browser contact sheet. Looking has
  caught something in every part so far, twice in the last session alone.
- **Two document fetches**, both needing a library or a browser, neither blocking:
  the Holstein seat count from the 15 May 1834 decree, which would let chapter 32's
  figure 2 drop its `counted, not decreed` caveat; and the Zealand kapitelstakst
  values from *Statistiske Meddelelser* 4. Række, 15. Bind, Hæfte I, which would
  let figure 3 become the price line it was planned as.

## Standing rules

- **Compute numbers, do not type them** — and not from numbers someone else typed
  either. Treat every "N years after" in a draft as a claim to verify (D-8).
- **Verify before writing.** One chapter 32 vignette had its man in the right place
  a decade after the thing that made him worth writing about.
- **Rasterise and look at every figure.** The guards run automatically now and still
  cannot see everything a reader would.
- **A guard that is written and not wired in is worth nothing.** `overflows` existed
  for three years and was never called by the script whose figure it would have
  fixed.
- **Assert on every scripted replacement, then grep for the new string.** A refused
  edit does not stop the commands chained after it. This fired twice last session
  and caught both.
- **Predict the symptom before making the change.** Adding a `style.css` token was
  written up beforehand as "if 12–31 move to style-only, the drop list has not
  picked it up" — which is exactly what happened, and why it took minutes.
- **Enumerate what you want, not what you want removed.**
- **Never hand over or commit a generated file.** Downloads inject a C2PA manifest
  into SVGs (item 33). Source travels; artifacts regenerate.

## How I work

Flag errors precisely and don't soften them. I would rather be told a plan is wrong
than have it worked around. If you need something from me, say so explicitly and say
what it blocks. If something needs me physically — an archive, a browser, a decision
only I can make — mark it as such and do not wait on it silently.

I am not a historian. Historical judgement is yours to make and defend, not mine to
sign off; tell me where you differ from the standard account and why, so I can see
the reasoning rather than just the conclusion. What I can tell you is whether a
chapter is too long, whether a section is dull, and where an explanation lost me.

**I will not read the prose until the chapter is finished**, so do not hold the
build waiting on my review.
