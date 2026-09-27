The consistency review, session 13: the prose and figure faults found in Parts A–F, checked against sources

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the thirteenth session of the consistency review, which checks whether the book agrees with itself. Every part has been read at depth (sessions 3–12), and D-17 (ask once) now holds on all 45 pages. No new chapters, no repartition.

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
python3 build_parts_abc.py ; python3 build_part_d.py ; python3 build_part_e.py ; python3 build_part_f.py
python3 build_part_g.py ; python3 build_part_h.py ; python3 build_part_i.py
python3 sweep_glossary.py ; python3 sweep_names.py ; python3 sweep_facts.py ; python3 sweep_arrows.py

Expected, as run after item 150's rebuild. `mapfixture.py` takes a few minutes; do not kill it. The part builds strip the index link, so run `python3 linkindex.py` and `python3 index_generator.py` after them, and then `git status --short` should be clean again.

- **git log:** the commit carrying item 150's patch **must carry its rebuilt pages** (01–24, 38 and `danish-history-index.html`) and the regenerated `svg_fealty.txt` and `c38_body.html`. If debuild reports BODY DRIFT, figcheck a figure disagreeing with its source, freshcheck a STALE body, or any build a figure that is not fresh or a page NOT BUILT / NOT WRITTEN, they were not pushed; stop and say so.
- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** every map's curated mainland and panel cases all correct; FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **351,041 page words, 27.9 h**. Part A 21,438; B 26,439; C 26,375; D 32,167; E 36,480; F 30,319; G 54,240; H 43,460; I 80,123. **21 is 50 minutes** (10,530 words), 44 is 48, **45 is 50**.
- **vignettes:** 148 carry a place, 116 distinct; selftest passes; 01, 03, 04, 05 "[f] part"; no D-9 failure anywhere.
- **figcheck:** 98 match, **30 sourceless "(Parts A-C: expected, not a fault)"**, 0 disagree.
- **narrative:** four OVER — 16 §08 852, 42 §02 767, 43 §02 780, 44 §03 761. Not for cutting (D-16). 32 §09 is 749.
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** 167 blocks in 21 chapters. **freshcheck:** 21 fresh (25–45).
- **builds:** A–C "figures: inline in the bodies, no scripts", "all eleven built clean"; D "figures: 0 checked against their scripts, 12 sourceless (content not checkable), none stale", "all four built clean"; E "figures: 14 … all fresh", "all five built clean"; F "figures: 12 … all fresh", "all four built clean"; G 21 fresh, "all seven"; H 15, "all five"; I 24, "all nine". **Every chapter line in every part "vocabulary clean | questions asked once".** No `!!`.
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses.
- **sweep_names:** **Schleswig 315 in 31 chapters against Slesvig 4 in 3.**
- **sweep_facts:** section 5 lists 2 (both false pairings: Dybbøl's misread 3,600 with 42's rescuers' 4,000; 1895's 114 seats with 1924's 149).
- **sweep_arrows:** 254 arrows, 37 thread notes. Form 7; direction 0; D-1 0; quoted titles 0; **solvency 38 listed**; prose references 0; footers 0; `<h1>` 0; 9b 0.
- **Questions (the session-12 measures, `claude/session12_qsmeasure.py` and `session12_qspairs.py` in the project, which take globs):** on `../[0-9][0-9]-*.html`, qs 0/224, Causal 0/168, Recall 0/198; 0 opener–tier pairs.

Anything different: stop and say so.

Then read HANDOFF item 150, REVIEW-CONSISTENCY.md §16 (above all §16.5) and CONVENTIONS.md. Item 150's lesson: **a number handed on is a claim until it is measured again; and a witness covers only the files its search was written to find — so find, by hand, what it should have found** (the brief's "20, 23 and 24" were twenty pages; `pageguard` had never seen twelve of Part E's figures, one of them stale). Item 149's: a measure finds the fault it was written for and no other; a correction is checked by someone who did not write it, however small (session 12's own Dates sentence was false, and check 3 caught it). Item 147's: a correction is a claim that needs a source. Item 142's: before trusting a 0, find one case by hand the check should have caught. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit them — there is no draft, and freshcheck does not cover them); inline figures in 01–11 live in the bodies; Part D's twelve `svg_*.txt` have no generator (edit the `.txt`, and say so); Part E's and F's figures come from `fig_*.py`, `figs_*.py` and `map_*.py` — edit the script and re-run it, never the `.txt`. 25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py`.

THIS SESSION:

1. **§16.5, checked against sources.** Every item in REVIEW-CONSISTENCY §16.5 — the five the checkers were surest of and the thirty-one "to verify" — gets a source before it gets a change: lex.dk, danmarkshistorien.dk, Nationalmuseet, DBL, the standard works the pages already cite. Where the page is wrong, correct the prose (or figure) and its Sources line; where it is right, say so in the ledger with the source; where it cannot be settled, hedge on the page or record it. D-8 for intervals, D-15 for names, D-6 for dates. Changes to prose can change a question's answer: re-read each page's questions after its edits (the builds refuse a question asked twice, not a question made false).

2. **D-6's form in Part F.** 23 (Lutter) and 24 (the Sound) set the foreign style off with a dash; D-6 and the index say parentheses. Decide whether to bring them to the parenthesis form (a two-line body edit) — recommend, do not ask, unless it changes meaning.

3. **For Carsten, not for this session:** 15 opener 4 ("the richest king Denmark had seen in a century" — the page says "He had no treasury"); 21 and 45 at 50 minutes, the top of the band; the four OVER sections.

4. **Tooling, only if the session has room:** `build_part_g.py`, `build_part_h.py`, `build_part_i.py` still write a page before its structural checks (the A–F builds now write only after all pass); no build counts the CSS brace imbalance it prints.

5. **Before handing over, have an agent that has not seen the work check every hunk**, and every correction against its source; if the fixes change, a second agent checks the changes; and a third if those change.

6. **Save state to the project at intervals** (`claude/session13_state.md` and a WIP patch against the commit you cloned): after the cold run, after each part, after each check. If usage runs long, stop at a save and write the next START_HERE. The project was full in session 12; keep saves small, and ask before deleting anything from it.

Delivery as always: source files only, as one `git format-patch`, never generated pages or generated `svg_*.txt` or generated bodies (01–24's bodies are sources). Carsten downloads it to `~/Downloads/`.

Carsten commits, builds and pushes, **pages in the same commit as the sources**, and **he builds only when told to**: the handover ends with the exact shell commands, in order, and names the pages that change. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter. If any line prints `!!`, NOT BUILT or NOT WRITTEN, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, `build_part_e.py` for 16–20, `build_part_f.py` for 21–24, `build_part_g.py` for 25–31, `build_part_h.py` for 32–36, `build_part_i.py` for 37–45) — and a part whose pages use a changed map is rebuilt too — then `linkindex.py`, then `index_generator.py`, **after every part build, since a part build strips the index link `linkindex.py` adds.** End the session with a HANDOFF item (151) and the next START_HERE.
