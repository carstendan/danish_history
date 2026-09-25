The consistency review, session 10: R-16 to R-18 if answered, then Part H read

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the tenth session of the consistency review, which checks whether the book agrees with itself. No new chapters, no repartition.

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
python3 build_part_f.py ; python3 build_part_g.py
python3 sweep_glossary.py ; python3 sweep_names.py ; python3 sweep_facts.py ; python3 sweep_arrows.py

Expected, as run after item 147's rebuild. `mapfixture.py` takes a few minutes; do not kill it. `build_part_f.py` and `build_part_g.py` strip the index link, so run `python3 linkindex.py` and `python3 index_generator.py` after them, and then `git status --short` should be clean again.

- **git log:** the commit carrying item 147's patch **must carry its rebuilt pages** (21, 24, 25–31, 32 and the index) and the regenerated `svg_*.txt` of figs_25 to figs_31 and of map_1660, map_1721 and map_1814. If debuild reports BODY DRIFT on those pages, figcheck reports a figure disagreeing with its source, or freshcheck reports a STALE body in 25–32, they were not pushed; stop and say so.
- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** curated panel all correct; FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **340,840 page words, 27.1 h**. Part A 21,397; Part B 26,326; Part C 26,228; Part D 32,106; Part E 36,388; Part F 30,153; Part G 52,644; Part H 41,195; Part I 74,403. 21 is 50 minutes.
- **vignettes:** **145 carry a place, 114 distinct**; selftest passes. Balance: 01, 03, 04, 05 "[f] part"; **D-9 FAILURES: 25, 27, 31** (R-16 to R-18) unless they have been carried out; 32 onwards tagged.
- **figcheck:** 98 match, 30 sourceless, 0 disagree.
- **narrative:** one OVER, 16 §08 *Kalmar, 17 June*, 852. Known; not for cutting (D-16).
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** **167 blocks in 21 chapters** (25–31 now read from PART_G_DRAFT.md). **freshcheck:** **21 fresh (25–45)**.
- **build_part_f.py** prints "all four built clean"; **build_part_g.py** prints "all seven built clean" (new in session 9, §13.6).
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses.
- **sweep_names:** **Schleswig 212 in 29 chapters against Slesvig 65 in 4** (32, 33, 34, 36 — Part H's, for this session).
- **sweep_facts:** 5 rows to read.
- **sweep_arrows:** **253 arrows**, 37 thread notes. Form 7; direction 0; D-1 0; quoted titles 0; **solvency 40 listed**; prose references 0; footers 0; `<h1>` 0; 9b 0.

Anything different: stop and say so.

Then read HANDOFF items 146 and 147, CONVENTIONS.md and REVIEW-CONSISTENCY.md §13. Item 147's lesson: **a guard must have its own witness, not the builder's; and a correction is a claim that needs a source, not only a better sentence** (two vignettes' worth of prose sat in segment preambles mkbody never emits, and the repaired appcheck read through mkbody's own reader; my fix of 30's "seventh largest" was a false "one of only seven"). Item 146's: a rule's example is a claim too, and a clean result from a search you wrote is a search you have not yet checked. Item 145's: a fix is prose too, and a guard is a claim too — run both against the real thing. Item 144's: a correction is sourced from the best thing that says it. Item 143's: a decision records what was agreed, not what is true. Item 142's: before trusting a 0, find one case by hand the check should have caught. Item 141's: read the ledger before carrying out a START_HERE. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit it). **25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py`: edit the draft, never the generated body, and rebuild with `mkbody.py`.** The per-chapter fragment files beside PART_G_DRAFT.md (`c25_draft_01-03.md` … `c31_draft_apparatus.md`) are read by nothing; do not edit them (§13.4). Checkpoints live in the build scripts' configs. Check how `build_part_h.py` and `mkbody.py` treat Part H's checkpoints before assuming.

THIS SESSION:

1. **R-16 to R-18 (REVIEW-CONSISTENCY §13.9), each only if Carsten has answered it.** Carry out each as answered; **find the facts first** — the research is a first search (`claude/session9_research_R16.md`, `_R17.md`, `_R18.md` in the project), and item 143 applies: R-15's recommendation had the court and the volume wrong. R-16 (Charlotte Amalie at Nykøbing, 25 June 1667, 25 §08, `[f]`): the clergy link is "formentlig" in Kvindebiografisk — keep it "probably". R-17 (Kari Hiran, Krokskogen, April 1716, 27 §05, `[f][n]`): one source, her own petition of 1717 — the page says so; check the style of SNL's "16 April" (Norway Gregorian, Sweden one day ahead of Julian in 1716); §05's re-scoping and the body's new sentences on the 1716 invasion must not retell the vignette (D-13). R-18 (Hans Andersen, Odense, 1812–January 1813, 31 §07, `[n]`): confirm the "about 1,000 rigsdaler" (the H.C. Andersen Centre's "antagelig"; Levnedsbogen or Topsøe-Jensen) and keep his son to one line. Who-line person · place · date · tag. Then `vignettes.py` should report no D-9 failure in Parts A–G for each one carried out.

2. **Part H's reading pass, chapters 32–36** (from `c32_draft.md` … `c36_draft.md`). Errors of fact, repetition within and across chapters (including back into 31: 31 → Part H promises the German-speaking share of the realm rising sharply after 1814, and the Schleswig question from 1721; 29 → Part H the tie to the home district until universal conscription in 1848–49; 27 → Part H the Kongelov's female line in Schleswig), and drag, against CONVENTIONS.md and the sweeps. **Compute every interval (D-8)**: Part C had nine wrong, D sixteen, E thirty-four, F sixty-six, G ninety-five. D-6: every date in 32–36 is Gregorian on both sides, so the rule bites only on Russian dates. **D-13: 35 §03 (Uhd) is the last of the seven** — decide it. **D-15: Part H holds all 65 remaining Slesvig** (32 one, 33 thirty-seven, 34 twenty-three, 36 four) — Schleswig in prose; *Slesvigsk Parti*, *Sydslesvig* and similar names keep their Danish form; the maps keep Danish labels. D-9 backfill is due only if Part H is untagged (it is tagged; check each tag). Measure Recall as §13.3 did. Put findings in a new §14 of REVIEW-CONSISTENCY.md. Any decision goes to Carsten one at a time, with a recommendation.

3. **Cheap, while Part H is open.** `build_part_h.py` has no retired-vocabulary guard and no summary line (§13.4). Give it Part G's version (§13.6: it reads text, not markup, and asks freshcheck before writing each page) and **show it passing on the real pages and firing on planted cases** — and before trusting a clean first run, find by hand every "entry" in 32–36 (text, figure text and attributes, whitespace joined, case ignored).

4. **Before handing over, have an agent that has not seen the work check every hunk** against sources and against the rest of the book. In sessions 3 to 9 it found ten, eight, seven, fourteen, twelve, twenty-two, and some seventy plus fifteen slips in the fixes themselves — and in session 9 one of them was the reviewer's own "fact". If the fixes are then changed, have a second agent check the changes.

5. **Save state to the project at intervals** (`claude/session10_state.md` and a WIP patch), as sessions 8 and 9 did: after the cold run, after each vignette, after each chapter, after each check. Session 9's first run was lost and the second finished it from these saves.

Delivery as always: source files only, as `git format-patch` or whole files, never generated pages or generated `svg_*.txt` or generated bodies.

Carsten commits, builds and pushes, **pages in the same commit as the sources**. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter (`python3 mkbody.py NN` for 25–31 from `PART_G_DRAFT.md`; `DK_DRAFT=cNN_draft.md python3 mkbody.py NN` for 32–45). If any line prints `!!`, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, `build_part_e.py` for 16–20, `build_part_f.py` for 21–24, `build_part_g.py` for 25–31, `build_part_h.py` for 32–36, `build_part_i.py` for 37–45) — and a part whose pages use a changed map (map_1814 is in 32) is rebuilt too — then `linkindex.py`, then `index_generator.py` — **after every part build, since a part build strips the index link `linkindex.py` adds.** End the session with a HANDOFF item and the next START_HERE.
