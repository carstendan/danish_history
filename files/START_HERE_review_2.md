The consistency review, session 2: Part I's decisions, then unblocking Parts A–D

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built and every page passes every check. This is the second session of the consistency review — whether the book agrees with itself. No new chapters, no repartition.

Clone github.com/carstendan/danish_history. From files/, with DK_CHAPTERS, DK_OUT and DK_SRC unset, cold run first, reporting what fails rather than working around it:

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
python3 draftnotes.py c3[2-9]_draft.md c4[0-5]_draft.md
python3 appcheck.py
python3 freshcheck.py
python3 sweep_glossary.py ; python3 sweep_names.py ; python3 sweep_facts.py ; python3 sweep_arrows.py

Expected, as run on a container rebuild of item 139's patch from a fresh clone. `mapfixture.py` takes several minutes; do not kill it.

- **tidy:** reports, deletes nothing.
- **seamcheck:** SEAM LAYER PASSES.
- **debuild:** 30 identical, 15 style-only, all round-trip. **01–15 are style-only and that is known**: they cannot be rebuilt until decision D-A below.
- **bookstats:** 45 of 45, **336,857 page words, 26.7 h**, 0 remaining. Part I 74,400.
- **vignettes:** 89 carry a place, 61 distinct; selftest passes.
- **figcheck:** 87 match, 41 sourceless (A–D, expected), 0 disagree.
- **draftnotes:** no drafting notes in 45 pages; none in the 14 drafts either — the phrase "do not re-gloss" is now a pattern.
- **appcheck:** 159 blocks, every one reaches its page.
- **freshcheck:** 14 fresh (32–45); 25–31 skipped and named.
- **sweep_glossary:** 2 pointer entries (34, 35, both written to the reader), 0 insolvent.
- **sweep_arrows:** 254 arrows, 37 thread notes; 0 direction faults; 11 D-1 breaks, all on pages 02–17 and all listed in REVIEW-CONSISTENCY §4.3.

If Carsten has not yet rebuilt item 139, debuild will say 21 identical / 24 style-only, the book will be 336,231, and the sweeps will show the eighteen pointer glosses and the chapter 37 arrows. That is not a fault; say which state you found and go on from it. Anything else different: stop and say so.

Then read HANDOFF item 139, CONVENTIONS.md and REVIEW-CONSISTENCY.md §5–§6. Item 138's lesson still governs, and item 139 records it catching me once more: **before building a check, run the one the project has; before disputing a claim, read what the chapter already has for it — including its figures.**

THIS SESSION:

1. **Decisions, one at a time, each with its recommendation, in this order:** D-D (agree D-13, the vignette rule), then Part I's I-1 to I-5, then D-C (45's empty carry-forward), then D-B (Schleswig or Slesvig, which becomes D-15), then D-A (unblocking 01–15). Take each answer before presenting the next. Apply the Part I answers to the drafts.

2. **Part I's open items that are mine, not Carsten's:** chapter 38's Sønderborg arithmetic (2,029 − 349 is 1,680, not 1,672) and its Tønder figure — open *Statistiske Efterretninger* 1920 nr. 23 first, which the chapter's Sources still call "not yet opened"; and move 42's list of 43's open questions to 43.

3. **If D-A is yes: unblock Parts A–D.** `debuild.py extract` for 01–15, the ten Part D SVGs written out from the pages, the build scripts pointed at them, and a rebuild that `debuild verify` reports **identical** before anything in them is edited. Then the fifteen A–D findings in REVIEW-CONSISTENCY §5 D-A, and the D-1 breaks of §4.3 while the pages are open.

4. **Then Part A's reading pass**, if the session has room: chapters 01–03, for errors of fact, repetition within and across chapters, and drag, against CONVENTIONS.md and the sweeps. Findings to a new §7 of REVIEW-CONSISTENCY.md.

Delivery as always: source files only, as `git format-patch` or whole files. Never generated pages. For 16–24 the body is the source and may be edited; for everything else `cNN_body.html` is generated. Carsten commits, builds and pushes. **Rebuild order is the fix, not a convention: figure scripts that changed, then `mkbody.py` for each changed chapter, and if any line prints `!!`, stop — the part build will wrap the old body and report `part ok`. Then the parts, then `linkindex.py`, then `index_generator.py`.** End the session with a HANDOFF item and the next START_HERE.
