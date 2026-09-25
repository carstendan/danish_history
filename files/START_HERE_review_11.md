The consistency review, session 11: Part I read again, at the depth Parts A–H got (chapters 37–45)

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the eleventh session of the consistency review, which checks whether the book agrees with itself. No new chapters, no repartition.

Clone github.com/carstendan/danish_history. From files/, with DK_CHAPTERS, DK_OUT and DK_SRC unset, and with `cairosvg` installed (`pip install cairosvg`; without it every figure script prints `!!`), run the cold run first and report what fails rather than working around it:

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
python3 build_part_f.py ; python3 build_part_g.py ; python3 build_part_h.py
python3 sweep_glossary.py ; python3 sweep_names.py ; python3 sweep_facts.py ; python3 sweep_arrows.py

Expected, as run after item 148's rebuild. `mapfixture.py` takes a few minutes; do not kill it. The part builds strip the index link, so run `python3 linkindex.py` and `python3 index_generator.py` after them, and then `git status --short` should be clean again.

- **git log:** the commit carrying item 148's patch **must carry its rebuilt pages** (25, 27, 29, 31 and 32–36) and the regenerated `svg_*.txt` of figs_32 to figs_36 and map_1864 (thirteen files), and `files/pageguard.py`. If debuild reports BODY DRIFT on those pages, figcheck a figure disagreeing with its source, freshcheck a STALE body in 25–36, or build G or H a figure that is not fresh, they were not pushed; stop and say so.
- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** every map's curated mainland and panel cases all correct; FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **344,488 page words, 27.3 h**. Part A 21,397; Part B 26,326; Part C 26,228; Part D 32,106; Part E 36,388; Part F 30,153; Part G 54,165; Part H 43,322; Part I 74,403. 21 is 50 minutes.
- **vignettes:** **148 carry a place, 116 distinct**; selftest passes. Balance: 01, 03, 04, 05 "[f] part"; **no D-9 failure anywhere.**
- **figcheck:** 98 match, 30 sourceless, 0 disagree.
- **narrative:** one OVER, 16 §08 *Kalmar, 17 June*, 852. Known; not for cutting (D-16). 32 §09 is 749.
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** **167 blocks in 21 chapters**. **freshcheck:** **21 fresh (25–45)**.
- **build_part_f.py** prints "all four built clean"; **build_part_g.py** "figures: 21 checked against their scripts, all fresh" and "all seven built clean"; **build_part_h.py** "figures: 15 … all fresh" and "all five built clean". No `!!`.
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses.
- **sweep_names:** **Schleswig 297 in 31 chapters against Slesvig 2 in 2** (32 and 33, both Danish book titles in Sources).
- **sweep_facts:** section 5 lists **6** (the new one pairs 36's 114 seats of 1895 with 39's 149 of 1929 — different years, a false pairing).
- **sweep_arrows:** **253 arrows**, 37 thread notes. Form 7; direction 0; D-1 0; quoted titles 0; **solvency 40 listed**; prose references 0; footers 0; `<h1>` 0; 9b 0.

Anything different: stop and say so.

Then read HANDOFF items 147 and 148, CONVENTIONS.md, REVIEW-CONSISTENCY.md §6 (Part I's first reading, in session 1, before the method below existed) and §14. Item 148's lesson: **a guard that reads text must read it as the reader does, and the output a build trusts must have a witness of its own: the body, the figure and the words. And a session's work lives in its saves, not in the session.** Item 147's: a guard must have its own witness, not the builder's; and a correction is a claim that needs a source, not only a better sentence. Item 146's: a rule's example is a claim too, and a clean result from a search you wrote is a search you have not yet checked (session 10 proved it on its own brief: START_HERE_review_10's calendar remark was false). Item 143's: a decision records what was agreed, not what is true. Item 142's: before trusting a 0, find one case by hand the check should have caught. Item 141's: read the ledger before carrying out a START_HERE. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit it). **25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py`: edit the draft, never the generated body, and rebuild with `mkbody.py`.** Checkpoints live in the build scripts' configs. Check how `build_part_i.py` and `mkbody.py` treat Part I's checkpoints and questions before assuming.

THIS SESSION:

1. **Part I's reading pass, chapters 37–45** (from `c37_draft.md` … `c45_draft.md`), one fact-checker and one fixer per chapter, as in sessions 3–10. Errors of fact, repetition within and across chapters (including back into Part H: 36 → Part I's arrows, 35 → Part I's plebiscite and labour settlement, and 36 §06's Vestvold against 37 §04's), and drag, against CONVENTIONS.md and the sweeps. **Compute every interval (D-8)**: Part C had nine wrong, D sixteen, E thirty-four, F sixty-six, G ninety-five, H ninety-three. **Start from what session 10 found in Part I and did not change (§14.4):**
   - 37's "the 'universal suffrage' of chapter 33" — 33 never says it (it says universal conscription, and 15 per cent);
   - "Nordslesvig" in English prose — 37 three times, 38 fifteen: North Schleswig (D-15); *Vælgerforeningen for Nordslesvig* and similar names stay Danish;
   - 37 §01's "the parish council law of 1903 put local government on an elected footing" — the councils of 1903 were *menighedsråd*, church councils (36 §10 has them right);
   - 37 §05's "Her association outlived her by twenty-four years and won" — 10 September 1891 to 5 June 1915 is 23 years 9 months, and Kvindevalgretsforeningen was dissolved in 1898;
   - 45's poor's vote "in 1961" (three places) against danmarkshistorien *De 7 F'er*'s 1933 — source it; 33 names no year after 1915;
   - 38's "around thirty-five thousand men from Nordslesvig called up" (twice) against Grænseforeningen's 30,000 and 37's thirty thousand, and 38's "more than six thousand" dead against about 5,300 (35 now says "more than five thousand").
   **D-6:** Part I is Gregorian throughout, so the rule bites only on Russian dates before February 1918; check each. **D-13:** 42 §03 was decided in session 1 — check it still holds, and check every section named for its vignette's subject or moment. **D-15:** as above, and the maps keep Danish labels. **D-9:** Part I is tagged; check each tag against its vignette. Measure Recall as §14.3 did, with `claude/session10_recall.py` (it reproduces Part G's 0/4 — calibrate it on 25–36 first, then point it at 37–45). Put findings in a new §15 of REVIEW-CONSISTENCY.md. Any decision goes to Carsten one at a time, with a recommendation.

2. **One rule to measure, not to patch** (§14.4). In 35 and 36 a WHAT-THIS-PAGE-ANSWERS question (`mkbody.py`'s `qs`) asks what a checkpoint asks, and 36 asks the January 1886 rejection three times (Causal 1, `qs[1]`, checkpoint 2.2). Measure it across all twenty-one generated chapters (25–45) as Recall is measured: `qs` and Causal against the shipped checkpoints, content-word Jaccard ≥ 0.4, counts per chapter. If it is common, it is a rule for Carsten, with the numbers and a recommendation; if it is rare, fix the cases.

3. **Cheap, while Part I is open.** `build_part_i.py` has no retired-vocabulary guard and no summary line. **Give it `pageguard.py`, as `build_part_g.py` and `build_part_h.py` use it** (§14.6: freshcheck, `same_body`, `figures_fresh`, `stale_vocabulary` on `reader_text`, all asked before a page is written). **Before trusting a clean first run, find by hand every "entry" in 37–45** (text, figure text and attributes, whitespace joined, case ignored), and allow by phrase only what is really there. Show it passing on the real pages and firing on planted cases (a stale `DK_SRC` body, a restored old `svg_*.txt`, a padded chapter number in a checkpoint), with the pages left untouched. Also, in Part H, two small things §14.4 recorded: 35's ← 34 still promises "the heath", which 35 does not carry; and the earthwork is Danevirke in 7–13, 19 and 38 but Dannevirke in 33 and 34 (D-15's English exonym gives Danevirke; 34 §03's title and its `build_part_h.py` section title change together; 32's *Dannevirke* is the newspaper and stays).

4. **Before handing over, have an agent that has not seen the work check every hunk** against sources and against the rest of the book. In sessions 3 to 10 it found ten, eight, seven, fourteen, twelve, twenty-two, some seventy plus fifteen, and ninety-eight rows plus eighteen in the fixes — in session 10 the second check found the substantive one (35's vignette still "dissolving" what the body had corrected). If the fixes are then changed, have a second agent check the changes.

5. **Save state to the project at intervals** (`claude/session11_state.md` and a WIP patch against the commit you cloned): after the cold run, after each chapter, after each check. Session 10 was stopped twice and finished from these saves. If usage runs long, stop at a save and write the next part's START_HERE, as session 10 did.

Delivery as always: source files only, as one `git format-patch`, never generated pages or generated `svg_*.txt` or generated bodies. Carsten downloads it to `~/Downloads/`.

Carsten commits, builds and pushes, **pages in the same commit as the sources**, and **he builds only when told to**: the handover ends with the exact shell commands, in order, and names the pages that change. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter (`python3 mkbody.py NN` for 25–31 from `PART_G_DRAFT.md`; `DK_DRAFT=cNN_draft.md python3 mkbody.py NN` for 32–45). If any line prints `!!`, NOT BUILT or NOT WRITTEN, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, `build_part_e.py` for 16–20, `build_part_f.py` for 21–24, `build_part_g.py` for 25–31, `build_part_h.py` for 32–36, `build_part_i.py` for 37–45) — and a part whose pages use a changed map is rebuilt too — then `linkindex.py`, then `index_generator.py`, **after every part build, since a part build strips the index link `linkindex.py` adds.** End the session with a HANDOFF item (149) and the next START_HERE.
