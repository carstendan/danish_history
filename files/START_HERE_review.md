The consistency review: Part I first, then Parts A to H

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built and every page passes every check. This session starts the consistency review — whether the book agrees with itself — and nothing else. No new chapters, no repartition.

Clone github.com/carstendan/danish_history. From files/, with DK_CHAPTERS, DK_OUT and DK_SRC unset (every script finds the repository from its own location; an exported variable is what sent a rebuild into ~/Documents on 18 September — item 138), cold run first, reporting what fails rather than working around it:

git status --short
python3 tidy.py
python3 mapfixture.py
python3 seamcheck.py
python3 debuild.py verify ../[0-9][0-9]-*.html
python3 bookstats.py
python3 vignettes.py . ; python3 vignettes.py --selftest
python3 figcheck.py
python3 narrative.py ../[0-9][0-9]-*.html
python3 draftnotes.py ../[0-9][0-9]-*.html
python3 appcheck.py
python3 freshcheck.py

Expected, as run on a fresh clone of c5775cf on 19 September 2026. `mapfixture.py` takes several minutes; do not kill it.

- **tidy:** reports, deletes nothing.
- **seamcheck:** SEAM LAYER PASSES.
- **debuild:** 21 identical, 24 style-only, all round-trip. **01–24 are style-only and that is known, not a fault:** `style.css` gained two `.myth dd p` rules on 18 September and those pages were not rebuilt. Their myth blocks do not use the rules. Rebuilding E and F (then `linkindex.py`) makes 16–24 identical; Part D cannot be rebuilt (item 3), so 12–15 stay style-only either way.
- **bookstats:** 45 of 45, **336,231 page words, 26.7 h**, 0 remaining.
- **vignettes:** 89 carry a place, 61 distinct; selftest passes.
- **figcheck:** 87 match, 41 sourceless (A–D, expected), 0 disagree.
- **draftnotes:** no drafting notes in 45 files.
- **appcheck:** 159 blocks checked, every apparatus block reaches its page.
- **freshcheck:** 14 fresh (32–45); 25–31 skipped and named, because Part G is one combined draft.

Anything different: stop and say so. If the book total disagrees, the ledger is wrong and not the repository — item 112.

Then read HANDOFF.md items 136–138 and REVIEW-BUILD-FAULTS.md. **Item 138's lesson governs this whole review: before building a check, run the one the project has; before disputing a claim, read what the chapter already cites for it.** It was broken four times in the session that wrote it.

THE PLAN, agreed 19 September 2026:

1. **Conventions first, in one file.** The D-series is scattered: D-1, D-2, D-3, D-6 in HANDOFF and PLAN_G; D-4, D-5, D-7 in PLAN_G only; D-2 again in PLAN_I; D-8 to D-12 in HANDOFF; D-9 again in PLAN_H. Collect every one, with its rule, its reason and where it is defined, into a new `CONVENTIONS.md`. Add the vignette rule from item 138 as a proposal: *a vignette is the particular inside a general section; when the section is named for the vignette's subject or exact moment, the vignette restates the body.* The review checks the book against this file, and Carsten overrules in one place.

2. **Mechanical sweeps, all 45 chapters.** Cheap, and every finding is concrete:
   - **Glossary:** the same Danish term glossed differently. Known: *fæste* is "Tenancy" in 17 and "copyhold" in 32.
   - **Names and spellings:** the same person or place written differently across chapters.
   - **Dates and figures** that appear in more than one chapter must agree.
   - **Arrows:** every carry-forward (← n / → n) points at a chapter that delivers what it promises. LEDGER_PASS.md is the last arrow census.
   Write each sweep as a script that reads the built pages, not as a reading exercise. Findings go in `REVIEW-CONSISTENCY.md`, one section per sweep.

3. **Reading pass, Part I first, then A to H in order.** Part I is the newest prose and the least read, and HANDOFF's State section names its first question: chapter 43 carries two of the book's three sections over `narrative.py`'s heavy ceiling, 42 and 44 have no light section, and 44 and 45 are over the 40-minute advisory with no cut on record. Read for errors of fact, repetition within and across chapters, and drag. Historical judgement is mine to make and defend; Carsten's is when something is too long, dull, or loses him.

4. **Decisions batched per part, one at a time, each with a recommendation.** Already waiting: the six vignettes that repeat their section (item 138 lists them), chapter 45's empty carry-forward, chapter 32's missing figure (c).

This session: steps 1 and 2, then as much of the Part I reading as fits. Each later session takes one part.

Delivery as always: source files only, as `git format-patch` or whole files. Never generated pages or `cNN_body.html`. Carsten commits, builds and pushes. **Rebuild order is the fix, not a convention: `mkbody.py` for each changed chapter first, and if any line prints `!!`, stop — the part build will wrap the old body and report `part ok`.** End the session with a HANDOFF item and the next START_HERE.
