The consistency review, session 5: 06's two vignettes, then Part C read

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the fifth session of the consistency review, which checks whether the book agrees with itself. No new chapters, no repartition.

Clone github.com/carstendan/danish_history. From files/, with DK_CHAPTERS, DK_OUT and DK_SRC unset, run the cold run first and report what fails rather than working around it:

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

Expected, as run after item 142's rebuild. `mapfixture.py` takes several minutes; do not kill it.

- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** curated panel all correct; FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **336,720 page words, 26.7 h**. Part A 21,397; Part B 25,666; Part C 25,535; Part I 74,403.
- **vignettes:** **119 carry a place, 88 distinct**; selftest passes. Balance: 01, 03, 04, 05 "[f] part"; **D-9 FAILURES: 06 only** (R-3, below); 08 onwards untagged.
- **figcheck:** 98 match, 30 sourceless, 0 disagree.
- **narrative:** one OVER, 17 §08 *Kalmar, 17 June*, 849. Known; not for cutting (D-16).
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** 159 blocks. **freshcheck:** 14 fresh (32–45).
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses.
- **sweep_names:** **Schleswig 169 in 26 chapters** against Slesvig 104 in 11.
- **sweep_facts:** 5 rows to read.
- **sweep_arrows:** 254 arrows, 37 thread notes. Form 7; direction 0; D-1 0; quoted titles 0; solvency 40 listed; **prose references 0 — check 7 now reads "chapter N" and "(N)" in every section, vignettes and apparatus included**; footers 0; `<h1>` 0; 9b 0.

Anything different: stop and say so.

Then read HANDOFF items 141 and 142, CONVENTIONS.md (D-9 now names 01, 03, 04 and 05 under R-1; D-13 to D-16 in force) and REVIEW-CONSISTENCY.md §8. Item 142's lesson: **a check that reports 0 has only looked where it was told to look — before trusting a 0, find one case by hand that it should have caught.** Item 141's still governs: read the ledger before carrying out a START_HERE. Item 138's: run the check the project has before building one; read what the chapter and its neighbour already say before disputing a claim. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit it). 25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py`.

THIS SESSION:

1. **R-3, agreed 21 September: two vignettes for chapter 06.** (a) **The Juellinge woman** (Lolland, c. 200 CE, excavated 1909), buried holding the ladle and strainer of the Roman wine service — `[f]`, in §03 *What came north*, as the particular inside that section; §04's Hoby vignette now points back to §03's list, so do not re-list the service. (b) **An ordinary Vorbasse household** in §10 *The farm that moved* — `[n]`; a named farmstead or phase from Hvass's excavation, not the whole sequence §10 already tells. Source every detail before writing it (natmus, lex, Danmarks Oldtid, Hvass). Who-lines person · place · date · tag. D-13 applies: neither may restate its section. Then `vignettes.py` should report no D-9 failure in Parts A–B.

2. **Part C's reading pass, chapters 08–11.** Read for errors of fact, repetition within and across chapters (including back into 07: 07 §09's Ribe, Kanhave and Danevirke are promised to 8 and 9), and drag, against CONVENTIONS.md and the sweeps. **Compute every interval and every "N years later" (D-8)**: Part A had twenty-six errors of fact and Part B about seventy, most of them intervals, distances and counts. Apply D-15 as you go; decide any D-13 vignette that falls in Part C. D-9 backfill is due: tag Part C, and fix the who-lines `vignettes.py` flags as "not 3 fields" (eleven in 08–11; one each in 12 and 14 for Part D). Measure Recall against the checkpoints as §8.5 did. Put findings in a new §9 of REVIEW-CONSISTENCY.md. Any decision goes to Carsten one at a time, with a recommendation.

3. **Three glossary pointers found in session 4, for their parts but cheap now** (§8.8): 24's *Hammershus* "from chapter 14", 20's *krongods* "since chapter 14", 19's *orlogsflåde* and 22. Read each target; fix or record.

4. **Before handing over, have an agent that has not seen the work check every hunk** against sources and against the rest of the book. In sessions 3 and 4 it found ten and eight slips in the fixes themselves.

Delivery as always: source files only, as `git format-patch` or whole files, never generated pages.

Carsten commits, builds and pushes. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter (`DK_DRAFT=cNN_draft.md python3 mkbody.py NN` for 32–45). If any line prints `!!`, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, and so on), then `linkindex.py`, then `index_generator.py`. End the session with a HANDOFF item and the next START_HERE.
