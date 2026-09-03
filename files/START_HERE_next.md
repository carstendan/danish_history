# START HERE — Part H drafting, tooling first, then chapter 32

**Paste everything below the line into a new chat. Attach nothing yet.**

---

I'm writing a long-form digital history of Denmark: 43 chapters, c. 13,000 BCE to
1953, as self-contained HTML pages for Danish readers at gymnasium level. Parts A–G
are shipped. **Part H is chapters 32 to 36 and it is planned. This session does the
tooling work the plan depends on, then drafts chapter 32. It does not re-plan.**

The project is in a git repository. The current version of a file is what is
committed, not what happens to be in the folder.

## First: the cold run

**Before reading a single planning document.** Every environment assumption this
project has hit was found by running everything cold at the start, and every one
that was not cost hours later. From `files/`, reporting what fails rather than
working around it:

```
python3 tidy.py
python3 mapfixture.py
python3 seamcheck.py
python3 debuild.py verify ../0?-*.html ../1?-*.html ../2?-*.html ../3?-*.html
DK_CHAPTERS="$PWD/.." python3 bookstats.py
python3 vignettes.py .
python3 narrative.py ../2[5-9]-*.html ../3[01]-*.html
```

**Expected, as of the end of Part H planning:**

- `tidy.py` — no collisions, no orphans. Missing: **ten** Part D figures, which have
  no generators and cannot be remade. `svg_plague_1711.txt` should **no longer** be
  listed; if it is, `figs_27.py` was not run.
- `mapfixture.py`, `seamcheck.py` — pass on all five territorial maps.
- `debuild.py verify` — `style-only` for chapters 01–11, `identical` for 12–31.
  `style-only` is not damage. **Anything reporting `BODY DRIFT` is serious.**
- `bookstats.py` — 43 in the spine, 31 built. Chapters 01–15 still carry reading
  times two to three minutes high and cannot be rebuilt.
- `vignettes.py` — three per chapter for 16–31. It does **not** check balance; that
  is this session's work.
- `narrative.py` — apparatus constant close to 3,508. It should report nine or ten
  sections per chapter, **not** ten or eleven; if it reports one extra per chapter,
  the WHAT THIS PAGE ANSWERS fix is not in the committed copy.

**If any of these differs, stop and say so before doing anything else.** A verifier
that disagrees with the ledger is either a real fault or a stale ledger, and both
matter more than the work.

## Then read, in this order

1. `HANDOFF.md` — the governing ledger. Open items are bare numbers; lessons carry
   an `L` prefix. Conventions D-1 to D-9 are closed; do not reopen them. **D-9 is
   new** — vignette balance tags.
2. `PLAN_H.md` — the plan for chapters 32 to 36. §1 is the corrected length model;
   §2 records six decisions taken at plan time that are **not** to be reopened; §10
   is the open-item list this session works from.
3. `REVIEW-PART-G.md` — what the last part got wrong and how it was found.

## What this session does, in order

**1. The tooling in `PLAN_H.md` §10.5.** These come first because two of them are
checks that are worthless if they arrive after the prose.

- `vignettes.py` — add the D-9 balance layer, reading the `[f]` and `[n]` tags and
  reporting per chapter whether a woman and a non-elite subject are present.
  Chapters 16–31 are untagged and should report `untagged`, not `fail`.
- `vignettes.py` — normalise the place match so variants of one place count as one.
  It currently reports Copenhagen five times where the true figure is thirteen of
  forty-eight.
- The advisory constant moves from 30–42 to **28–40** in `build_all.py` and the five
  `build_part_*.py` scripts. All six together.

**2. Research chapter 32 against the plan.** Ten sections, 1814–1848. Every
researched claim in Part G corrected the draft; expect the same. The plan's §10.1
lists what needs an archive and what needs a library — those are marked and are not
blocking.

**3. Draft chapter 32.** Prose only, into a draft file. `mkbody.py` and the build
come after the draft is reviewed, not during.

## What this session does not do

- Re-plan. The six decisions in `PLAN_H.md` §2 are made: thresholds 28–40; splits
  on 21, 28 and 32 retired; the Slesvig legal case assembled in 33; chapter 35
  carries the Nordslesvig section; chapter 15's arrow edited in the built page;
  D-9 adopted with lazy backfill.
- Draft 33 to 36. One chapter, reviewed, before the shape is replicated.
- Touch Parts A–D. No retained bodies for 01–15, no figure generators for 12–15.
  Documented, accepted, not a fault to rediscover.

## Standing rules

- **Compute numbers, do not type them** — and not from numbers someone else typed
  either. Two apparatus constants in a row were wrong because the arithmetic was
  applied to unverified inputs. Treat every "N years after" in a draft as a claim to
  verify (D-8).
- **Verify before writing.** Nearly every researched claim in Part G corrected the
  plan. One vignette survived nineteen revisions describing a woman who was
  somewhere else at the time.
- **Rasterise and look at every figure.** Three Part G faults were invisible to every
  automated guard and visible in one glance. If `cairosvg` is missing, `mapdump.py`
  builds a browser contact sheet.
- **A curated test case can name the right place and test nothing.** The 1814 and
  1864 spine maps need curated cases for their new borders, minimum three per
  territory.
- **Assert on every scripted replacement, then grep for the new string.** A refused
  edit does not stop the commands chained after it.
- **Enumerate what you want, not what you want removed.** Where a measurement can be
  defined by what it includes, define it that way; the excluded set is where the
  silent misses live.
- **Back-port before rebuilding.** A correction made to a body or a page and not
  carried back to the draft is destroyed by the next build. Git makes this visible;
  it does not make it impossible.

## How I work

Flag errors precisely and don't soften them. I would rather be told a plan is wrong
than have it worked around. If you need something from me, say so explicitly and
say what it blocks. If something needs me physically — an archive, a browser, a
decision only I can make — mark it as such and do not wait on it silently.

I am not a historian. Historical judgement is yours to make and defend, not mine to
sign off; tell me where you differ from the standard account and why, so I can see
the reasoning rather than just the conclusion. What I can tell you is whether a
chapter is too long, whether a section is dull, and where an explanation lost me.
