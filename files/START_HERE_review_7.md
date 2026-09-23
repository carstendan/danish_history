The consistency review, session 7: Part D's missing women, then Part E read

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the seventh session of the consistency review, which checks whether the book agrees with itself. No new chapters, no repartition.

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

Expected, as run after item 144's rebuild. `mapfixture.py` takes a few minutes; do not kill it.

- **git log:** the commit carrying item 144's patch **must carry its rebuilt pages** (08, 10–16). If debuild reports BODY DRIFT on exactly those, the pages were not pushed; stop and say so.
- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** curated panel all correct; FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **338,244 page words, 26.8 h**. Part A 21,397; Part B 26,326; Part C 26,228; Part D 31,136; Part E 35,042; Part I 74,403.
- **vignettes:** **136 carry a place, 105 distinct**; selftest passes. Balance: 01, 03, 04, 05 "[f] part"; **D-9 FAILURES: 12, 13, 14, 15** (R-6 to R-9) unless they have been carried out; 16 onwards untagged.
- **figcheck:** 98 match, 30 sourceless, 0 disagree.
- **narrative:** one OVER, 17 §08 *Kalmar, 17 June*, 849. Known; not for cutting (D-16).
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** 159 blocks. **freshcheck:** 14 fresh (32–45).
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses.
- **sweep_names:** Schleswig 172 in 26 chapters against Slesvig 101 in 10.
- **sweep_facts:** 5 rows to read.
- **sweep_arrows:** 254 arrows, 37 thread notes. Form 7; direction 0; D-1 0; quoted titles 0; solvency 41 listed; prose references 0; footers 0; `<h1>` 0; 9b 0.

Anything different: stop and say so.

Then read HANDOFF items 143 and 144, CONVENTIONS.md and REVIEW-CONSISTENCY.md §10. Item 144's lesson: **a correction is a claim like any other — source it from the best thing that says it, not from the first** (a fallback summary put "under torture" where the letter says "without coercion"). Item 143's still governs: a decision records what was agreed, not what is true, so its facts are checked again when it is carried out. Item 142's: before trusting a 0, find one case by hand the check should have caught. Item 141's: read the ledger before carrying out a START_HERE. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit it). 25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py`. **Checkpoints live in the build scripts' configs, for 01–11 (`build_parts_abc.py`) and for 12–15 (`build_part_d.py`) alike: change a checkpoint there as well as in the body.** Check how `build_part_e.py` handles them before editing 16–20.

THIS SESSION:

1. **R-6 to R-9 (REVIEW-CONSISTENCY §10.9). R-6 was answered 22 September as recommended: Queen Bodil in 12 §06, `[f]`. R-7 the same day: Ingeborg, queen of France, in 13 §09, `[f]`. R-8 on 23 September, both parts: Margrete Sambiria re-scoped into 14 §04's vignette, `[f]`, and Niels Ebbesen retagged `[n]`. R-9 as Carsten has answered it.** Carry out only what he agreed; if one is unanswered, leave its chapter failing. Source every detail before writing it, and check the recommendation's own facts first — §10.9 says they are a first search, not a text. Who-lines person · place · date · tag. D-13 applies (R-8 re-scopes 14 §04's paragraph rather than duplicating it). Then `vignettes.py` should report no D-9 failure in Parts A–D, or only the chapters whose decisions are still open.

2. **Part E's reading pass, chapters 16–20.** Errors of fact, repetition within and across chapters (including back into 15: 15 → 16 promises Margrete's son elected in 1376 and a union built on the realm reassembled; 15 → 18 promises the Hanse's Sound castles and Erik of Pomerania's toll of 1429), and drag, against CONVENTIONS.md and the sweeps. **Compute every interval (D-8)**: Part C had nine wrong, Part D sixteen. Known for Part E: **D-B's "Dithmarschen"** for "Ditmarschen" in 19–21 was agreed and never carried out (about seventeen uses in 19–25; 24 and 25 wait for their parts); **16 §02's Oluf** now dies "as the herring season began" on 3 August 1387 — check that against 14's market dates (24 August–9 October); **Schleswig/Slesvig**: 19 has 19 and 2. Apply D-15; decide any D-13 vignette. D-9 backfill is due: tag Part E. Measure Recall as §10.5 did. Put findings in a new §11 of REVIEW-CONSISTENCY.md. Any decision goes to Carsten one at a time, with a recommendation.

3. **Cheap, while Part E is open.** Check whether `build_part_e.py` has the padded-chapter guard `build_parts_abc.py` and now `build_part_d.py` have (§9.6, §10.6); if not, give it the same one and show it firing on a planted case before trusting it.

4. **Before handing over, have an agent that has not seen the work check every hunk** against sources and against the rest of the book. In sessions 3 to 6 it found ten, eight, seven and fourteen slips in the fixes themselves.

Delivery as always: source files only, as `git format-patch` or whole files, never generated pages.

Carsten commits, builds and pushes, **pages in the same commit as the sources**. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter (`DK_DRAFT=cNN_draft.md python3 mkbody.py NN` for 32–45). If any line prints `!!`, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, `build_part_e.py` for 16–20, and so on), then `linkindex.py`, then `index_generator.py` — **after every part build, since a part build strips the index link `linkindex.py` adds.** End the session with a HANDOFF item and the next START_HERE.
