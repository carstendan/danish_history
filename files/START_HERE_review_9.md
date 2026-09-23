The consistency review, session 9: R-15 if answered, then Part G read

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the ninth session of the consistency review, which checks whether the book agrees with itself. No new chapters, no repartition.

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

Expected, as run after item 146's rebuild. `mapfixture.py` takes a few minutes; do not kill it.

- **git log:** the commit carrying item 146's patch **must carry its rebuilt pages** (16–24) and the regenerated `svg_*.txt` of figs_22, 23 and 24. If debuild reports BODY DRIFT on those pages, or figcheck reports a figure disagreeing with its source, they were not pushed; stop and say so.
- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** curated panel all correct; FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **340,724 page words, 27.0 h**. Part A 21,397; Part B 26,326; Part C 26,228; Part D 32,106; Part E 36,388; Part F 29,659; Part I 74,403.
- **vignettes:** **143 carry a place, 114 distinct**; selftest passes. Balance: 01, 03, 04, 05 "[f] part"; **D-9 FAILURE: 21** (R-15) unless it has been carried out; 25 onwards untagged.
- **figcheck:** 98 match, 30 sourceless, 0 disagree.
- **narrative:** one OVER, 16 §08 *Kalmar, 17 June*, 852. Known; not for cutting (D-16).
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** 159 blocks. **freshcheck:** 14 fresh (32–45).
- **build_part_f.py** prints "all four built clean" (new in session 8, §12.6).
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses.
- **sweep_names:** Schleswig 178 in 26 chapters against Slesvig 99 in 9.
- **sweep_facts:** 5 rows to read.
- **sweep_arrows:** 254 arrows, 37 thread notes. Form 7; direction 0; D-1 0; quoted titles 0; solvency 41 listed; prose references 0; footers 0; `<h1>` 0; 9b 0.

Anything different: stop and say so.

Then read HANDOFF items 145 and 146, CONVENTIONS.md and REVIEW-CONSISTENCY.md §12. Item 146's lesson: **a rule's example is a claim too, and a clean result from a search you wrote is a search you have not yet checked** (CONVENTIONS D-6 illustrated the calendar with a wrong date, and chapter 23 printed the only new-style date in six parts; my own grep said Part F had no "entry", and the guard found four). Item 145's: a fix is prose too, and a guard is a claim too — run both against the real thing (session 8's checker again found five wrong intervals in the fixes, one written while removing another). Item 144's: a correction is sourced from the best thing that says it. Item 143's: a decision records what was agreed, not what is true. Item 142's: before trusting a 0, find one case by hand the check should have caught. Item 141's: read the ledger before carrying out a START_HERE. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit it). **25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py`: edit the draft, never the generated body, and rebuild with `mkbody.py`.** Checkpoints live in the build scripts' configs (`build_parts_abc.py`, `build_part_d.py`, `build_part_e.py`, `build_part_f.py`, `build_part_g.py`): change a checkpoint in the config. Check how `build_part_g.py` and `mkbody.py` treat checkpoints before assuming.

THIS SESSION:

1. **R-15 (REVIEW-CONSISTENCY §12.9).** If Carsten has answered it, carry it out as answered; if not, leave 21 failing. The recommendation (Rasmus Pedersen, the Roskilde-canonry tenant Tycho Brahe put in irons on Hven in 1590, who won in the king's court in 1591) rests on Dreyer (1890); **find the village and the Danish wording first** (Kancelliets Brevbøger 1588–92; *Danske Magazin* 4. rk. IV; Thoren; Christianson) and check every date. Who-line person · place · date · `[n]`. D-13: it replaces 21 §08's "a documented case" sentence rather than duplicating it. Then `vignettes.py` should report no D-9 failure in Parts A–F.

2. **Part G's reading pass, chapters 25–31** (from `PART_G_DRAFT.md`). Errors of fact, repetition within and across chapters (including back into 24: 24 → 25 promises the estates of 1660, the hereditary crown and the *Kongelov* of 1665; 24 → 26 Leonora Christina and *Jammersminde*; 24 → 26, 27 the snaphane war and the last attempt on Skåne; 21 → 27 the Gottorp question to 1720–21), and drag, against CONVENTIONS.md and the sweeps. **Compute every interval (D-8)**: Part C had nine wrong, D sixteen, E thirty-four, F sixty-six. **D-6 bites here for the first time on a date in the text:** Julian to 1 March 1700, Gregorian after, Sweden's own reckoning 1700–12; the foreign style in parentheses at the first divergence in a chapter; chapter 27 has the *gammel og ny stil* gloss — check every date in 25–31 against its style, and check the Frederiksborg peace of 1720 (3 June or 3 July, E4). **D-13: four of the seven cases are Part G's** — 26 §09 Leonora Christina, 27 §05 Tordenskjold, 27 §09 Gertrud Rask, 29 §03 Caroline Mathilde: decide each. Known, from session 8: chapter 30 has Trankebar held "two hundred and twenty-five years" (1620 to 1845 is 224 years 11 months: name the years). Apply D-15 (Skåne towns Swedish after 1658; the adjective "Scanian" is Part G's). D-9 backfill is due: tag Part G (25's missing woman and 31's missing non-elite subject were found by hand at drafting — CONVENTIONS D-9; check they are still there). Measure Recall as §12.3 did. Put findings in a new §13 of REVIEW-CONSISTENCY.md. Any decision goes to Carsten one at a time, with a recommendation.

3. **Cheap, while Part G is open.** Check whether `build_part_g.py` has the padded-chapter guard the other part builds now have (§9.6, §10.6, §11.6, §12.6); it does not print "built clean" at present. If it lacks the guard, give it the same one and **show it passing on the real pages and firing on a planted case** — and before trusting a clean first run, find by hand every "entry" in 25–31 (a multi-line-aware search), because session 8's grep missed four.

4. **Before handing over, have an agent that has not seen the work check every hunk** against sources and against the rest of the book. In sessions 3 to 8 it found ten, eight, seven, fourteen, twelve and twenty-two slips in the fixes themselves.

5. **Save state to the project at intervals** (`claude/session9_state.md` and a WIP patch), as session 8 did: after the cold run, after the vignette, after each chapter, after the check.

Delivery as always: source files only, as `git format-patch` or whole files, never generated pages or generated `svg_*.txt`.

Carsten commits, builds and pushes, **pages in the same commit as the sources**. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter (`python3 mkbody.py NN` for 25–31 from `PART_G_DRAFT.md`; `DK_DRAFT=cNN_draft.md python3 mkbody.py NN` for 32–45). If any line prints `!!`, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, `build_part_e.py` for 16–20, `build_part_f.py` for 21–24, `build_part_g.py` for 25–31, and so on), then `linkindex.py`, then `index_generator.py` — **after every part build, since a part build strips the index link `linkindex.py` adds.** End the session with a HANDOFF item and the next START_HERE.
