The consistency review, session 12: D-17 (ask once) in Parts A–F, and the guard for the first four builds

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the twelfth session of the consistency review, which checks whether the book agrees with itself. Every part has now been read at depth (sessions 3–11). No new chapters, no repartition.

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
python3 build_part_f.py ; python3 build_part_g.py ; python3 build_part_h.py ; python3 build_part_i.py
python3 sweep_glossary.py ; python3 sweep_names.py ; python3 sweep_facts.py ; python3 sweep_arrows.py

Expected, as run after item 149's rebuild. `mapfixture.py` takes a few minutes; do not kill it. The part builds strip the index link, so run `python3 linkindex.py` and `python3 index_generator.py` after them, and then `git status --short` should be clean again.

- **git log:** the commit carrying item 149's patch **must carry its rebuilt pages** (25–45 and `danish-history-index.html`) and the regenerated `svg_*.txt` of figs_34 and figs_37 to figs_44. If debuild reports BODY DRIFT, figcheck a figure disagreeing with its source, freshcheck a STALE body in 25–45, or build G, H or I a figure that is not fresh or a page NOT WRITTEN, they were not pushed; stop and say so.
- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** every map's curated mainland and panel cases all correct; FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **350,394 page words, 27.8 h**. Part A 21,397; B 26,326; C 26,228; D 32,106; E 36,388; F 30,153; G 54,240; H 43,460; I 80,096. 21 is 50 minutes, 44 is 48, **45 is 50**.
- **vignettes:** **148 carry a place, 116 distinct**; selftest passes; 01, 03, 04, 05 "[f] part"; **no D-9 failure anywhere.**
- **figcheck:** 98 match, 30 sourceless, 0 disagree.
- **narrative:** **four OVER** — 16 §08 *Kalmar, 17 June* 852 (known), 42 §02 767, 43 §02 780, 44 §03 761 (grown by correction in session 11). Not for cutting (D-16). 32 §09 is 749.
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** **167 blocks in 21 chapters**. **freshcheck:** **21 fresh (25–45)**.
- **builds:** F "all four built clean"; G "figures: 21 … all fresh", "all seven built clean"; H "figures: 15 … all fresh", "all five built clean"; **I "figures: 24 … all fresh", "all nine built clean"**, every line "vocabulary clean | questions asked once". No `!!`.
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses.
- **sweep_names:** **Schleswig 316 in 31 chapters against Slesvig 4 in 3** (32 and 33 Danish book titles; 38 the plebiscite commission's French name and a Danish article title).
- **sweep_facts:** section 5 lists **2** (both false pairings: Dybbøl's misread 3,600 with 42's rescuers' 4,000; 1895's 114 seats with 1924's 149).
- **sweep_arrows:** **254 arrows**, 37 thread notes. Form 7; direction 0; D-1 0; quoted titles 0; **solvency 39 listed**; prose references 0; footers 0; `<h1>` 0; 9b 0.

Anything different: stop and say so.

Then read HANDOFF items 148 and 149, CONVENTIONS.md (**D-17 is new**) and REVIEW-CONSISTENCY.md §15. Item 149's lesson: **a measure finds the fault it was written for and no other; and a correction is checked by someone who did not write it, however small it is** (the reader's version of "asked twice" turned up forty-five times where the measure could not see it, and the lead's own five-to-four correction cited a source for a claim the source did not make). Item 148's: a guard that reads text must read it as the reader does, and the output a build trusts must have a witness of its own; a session's work lives in its saves. Item 147's: a correction is a claim that needs a source. Item 146's: a clean result from a search you wrote is a search you have not yet checked. Item 142's: before trusting a 0, find one case by hand the check should have caught. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit them — there is no draft and freshcheck does not cover them). 25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py`. Checkpoints live in the build scripts' configs (`build_parts_abc.py`, `build_part_d.py`, `build_part_e.py`, `build_part_f.py` for 01–24). Check how each of those four builds treats checkpoints, questions and the body before assuming it works like G–I.

THIS SESSION:

1. **D-17 in Parts A–F (01–24).** Measure first, as session 11 did for 25–45: `claude/session11_qsmeasure.py` and `qspairs.py` (take globs; calibrate them on 25–45 first — they must give 0 there), then `pageguard.asked_twice` on every page 01–24. Session 11's checker found three already: **20** (checkpoint 2.3 ≈ Recall 4), **23** (checkpoint 3.1 ≈ Causal 2), **24** (checkpoint 3.2 ≈ Recall 4). Then read every page for the repeats the measure cannot see (in 25–36 there were about forty-five). The opener keeps its question; the checkpoint or end-tier question is rewritten, true, on the page, and a checkpoint only from what comes before its anchor. Check also that every checkpoint and end question you keep is true and answerable — in 25–45 several were not.

2. **Give the four early builds the guard.** `build_parts_abc.py`, `build_part_d.py`, `build_part_e.py`, `build_part_f.py` have not had `pageguard.py`. Decide, per check, what applies to authored bodies: `asked_twice` and `stale_vocabulary` on `reader_text` do; `figures_fresh` for the scripted figures (Parts A–D's inline figures are sourceless, by design); `same_body` if the build reads bodies through `DK_SRC`; freshcheck does not. **Before trusting a clean first run, find by hand every "entry" in 01–24** (text, figure text and attributes, whitespace joined, case ignored — session 9 found two in Part G), and allow by phrase only what is really there. Show each build passing on the real pages and firing on planted cases (a restored old `svg_*.txt`, a padded chapter number in a checkpoint, a checkpoint copying an opener), with the pages left untouched. Every page is written only after every check passes, and each build ends with a summary line.

3. **Cheap, while A–F are open** (from §15.4 and earlier): CONVENTIONS' conflict 2 (D-6's calendar line never added to the index's *Decisions already made*) and conflict 3 (the two arrow forms missing from HANDOFF's cross-reference table); 38's → 40 promises both minorities, 40 carries the German only — fix the arrow.

4. **Before handing over, have an agent that has not seen the work check every hunk**; if the fixes change, a second agent checks the changes; and if those change, a third (session 11 needed all three, and the third found one of the lead's own).

5. **Save state to the project at intervals** (`claude/session12_state.md` and a WIP patch against the commit you cloned): after the cold run, after each part, after each check. If usage runs long, stop at a save and write the next START_HERE.

For Carsten's read of the book, not for this session: 45 is at 50 minutes, the top of the band, and can take nothing more; the four OVER sections; 40 §11's "11 March 1939" and 41's minority 1,500 (inside or beside the 12,000), both unverified; the library items in §14.4.

Delivery as always: source files only, as one `git format-patch`, never generated pages or generated `svg_*.txt` or generated bodies (01–24's bodies are sources). Carsten downloads it to `~/Downloads/`.

Carsten commits, builds and pushes, **pages in the same commit as the sources**, and **he builds only when told to**: the handover ends with the exact shell commands, in order, and names the pages that change. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter. If any line prints `!!`, NOT BUILT or NOT WRITTEN, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, `build_part_e.py` for 16–20, `build_part_f.py` for 21–24, `build_part_g.py` for 25–31, `build_part_h.py` for 32–36, `build_part_i.py` for 37–45) — and a part whose pages use a changed map is rebuilt too — then `linkindex.py`, then `index_generator.py`, **after every part build, since a part build strips the index link `linkindex.py` adds.** End the session with a HANDOFF item (150) and the next START_HERE.
