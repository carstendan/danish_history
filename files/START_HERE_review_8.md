The consistency review, session 8: Part E's missing vignettes, then Part F read

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the eighth session of the consistency review, which checks whether the book agrees with itself. No new chapters, no repartition.

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

Expected, as run after item 145's rebuild. `mapfixture.py` takes a few minutes; do not kill it.

- **git log:** the commit carrying item 145's patch **must carry its rebuilt pages** (12–21). If debuild reports BODY DRIFT on exactly those, the pages were not pushed; stop and say so.
- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** curated panel all correct; FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **339,260 page words, 26.9 h**. Part A 21,397; Part B 26,326; Part C 26,228; Part D 32,106; Part E 35,086; Part F 29,497; Part I 74,403.
- **vignettes:** **139 carry a place, 109 distinct**; selftest passes. Balance: 01, 03, 04, 05 "[f] part"; **D-9 FAILURES: 16, 17, 18, 20** (R-10 to R-14) unless they have been carried out; 21 onwards untagged.
- **figcheck:** 98 match, 30 sourceless, 0 disagree.
- **narrative:** one OVER, 16 §08 *Kalmar, 17 June*, 852. Known; not for cutting (D-16).
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** 159 blocks. **freshcheck:** 14 fresh (32–45).
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses.
- **sweep_names:** Schleswig 178 in 26 chapters against Slesvig 99 in 9.
- **sweep_facts:** 5 rows to read.
- **sweep_arrows:** 254 arrows, 37 thread notes. Form 7; direction 0; D-1 0; quoted titles 0; solvency 41 listed; prose references 0; footers 0; `<h1>` 0; 9b 0.

Anything different: stop and say so.

Then read HANDOFF items 144 and 145, CONVENTIONS.md and REVIEW-CONSISTENCY.md §11. Item 145's lesson: **a fix is prose too, and a guard is a claim too — run both against the real thing before trusting either** (three of session 7's corrections were wrong intervals, one written while removing an unsourced date; the new guard failed the first honest page it met). Item 144's: a correction is sourced from the best thing that says it, not the first. Item 143's: a decision records what was agreed, not what is true, so its facts are checked again when it is carried out. Item 142's: before trusting a 0, find one case by hand the check should have caught. Item 141's: read the ledger before carrying out a START_HERE. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit it). 25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py`. **Checkpoints live in the build scripts' configs — `build_parts_abc.py` (01–11), `build_part_d.py` (12–15), `build_part_e.py` (16–20) and `build_part_f.py` (21–24) all strip any checkpoint in a body and insert their own: change a checkpoint in the config.** The body blocks in 16–20 are dead text (§11.4).

THIS SESSION:

1. **R-10 to R-14 (REVIEW-CONSISTENCY §11.9). R-10 was answered 23 September as recommended: Margrete at the Lund landsting, about 10 August 1387, re-scoped from 16 §04's acclamation paragraphs, `[f]`. R-11 the same day: the Victual Brothers at Bergen, 1393, in 16 §06, `[n]`. R-12 the same day: Margrete's gift letter, Kalundborg, 8 December 1411, in 17 §05, `[f]`. R-13 the same day: the Reventlow vignette re-scoped to the peasants at Sankt Jørgensbjerg, 1441, in 18 §08, `[n]`. R-14 as Carsten has answered it.** Carry out only what Carsten has answered, as answered; if one is unanswered, leave its chapter failing. Source every detail before writing it, and check the recommendation's own facts first — §11.9 says they are a first search, not a text (R-13's date, May or 6 June 1441, is already in doubt). Who-lines person · place · date · tag. D-13 applies: R-10 re-scopes 16 §04's acclamation paragraphs and R-13 the Reventlow vignette rather than duplicating them. Then `vignettes.py` should report no D-9 failure in Parts A–E, or only the chapters whose decisions are still open.

2. **Part F's reading pass, chapters 21–24.** Errors of fact, repetition within and across chapters (including back into 20: 20 → 21 promises "a crown with the Sound Dues, half the land, a fleet and no bishops in the council"; 19 → 24 promises Sweden as a separate kingdom with "eleven wars" to 1814 — count them), and drag, against CONVENTIONS.md and the sweeps. **Compute every interval (D-8)**: Part C had nine wrong, Part D sixteen, Part E thirty-four. Known for Part F: 21's Dithmarschen and its Norway clause were fixed in session 7 (§11.2); 20's land-share figure has no source, and 20 → 21 promises "half the land" on the strength of it (§11.4) — check 21 against Den Store Danske's crown share (a tenth before 1536, 40–50 per cent after); **D-6** (Julian before 1 March 1700) applies to every date in Part F. Apply D-15 (Schleswig 9 in 21; check the Skåne towns — Danish in prose before 1658, Swedish in visit blocks); decide any D-13 vignette. D-9 backfill is due: tag Part F. Measure Recall as §11.5 did. Put findings in a new §12 of REVIEW-CONSISTENCY.md. Any decision goes to Carsten one at a time, with a recommendation.

3. **Cheap, while Part F is open.** Check whether `build_part_f.py` has the padded-chapter guard the other part builds now have (§9.6, §10.6, §11.6); if not, give it the same one and **show it passing on the real pages and firing on a planted case** before trusting it — session 7's fired falsely on a real "entry".

4. **Before handing over, have an agent that has not seen the work check every hunk** against sources and against the rest of the book. In sessions 3 to 7 it found ten, eight, seven, fourteen and twelve slips in the fixes themselves.

Delivery as always: source files only, as `git format-patch` or whole files, never generated pages.

Carsten commits, builds and pushes, **pages in the same commit as the sources**. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter (`DK_DRAFT=cNN_draft.md python3 mkbody.py NN` for 32–45). If any line prints `!!`, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, `build_part_e.py` for 16–20, `build_part_f.py` for 21–24, and so on), then `linkindex.py`, then `index_generator.py` — **after every part build, since a part build strips the index link `linkindex.py` adds.** End the session with a HANDOFF item and the next START_HERE.
