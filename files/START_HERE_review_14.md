The consistency review, session 14: what §17.3 left, against sources; and the G–I builds' guard

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the fourteenth session of the consistency review, which checks whether the book agrees with itself. Every part has been read at depth (sessions 3–12), D-17 (ask once) holds on all 45 pages, and session 13 checked every item of §16.5 against a source. No new chapters, no repartition.

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

Expected, as run after item 151's rebuild. `mapfixture.py` takes a few minutes; do not kill it. The part builds strip the index link, so run `python3 linkindex.py` and `python3 index_generator.py` after them, and then `git status --short` should be clean again.

- **git log:** the commit carrying item 151's patch **must carry its rebuilt pages** (01, 04, 07–13, 15–17, 19–24) and the regenerated `svg_atlantic.txt`, `svg_crowns.txt` and `svg_hemming.txt`. If debuild reports BODY DRIFT, figcheck a figure disagreeing with its source, any build a figure that is not fresh or a page NOT BUILT / NOT WRITTEN, they were not pushed; stop and say so.
- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** every map's curated mainland and panel cases all correct; FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **351,926 page words, 27.9 h**. Part A 21,445; B 26,496; C 26,643; D 32,334; E 36,733; F 30,452; G 54,240; H 43,460; I 80,123. **21 is 50 minutes** (10,559 words), 44 is 48, **45 is 50**.
- **vignettes:** 148 carry a place, 116 distinct; selftest passes; 01, 03, 04, 05 "[f] part"; no D-9 failure anywhere.
- **figcheck:** 98 match, 30 sourceless "(Parts A-C: expected, not a fault)", 0 disagree.
- **narrative:** **five OVER** — 16 §08 852, **21 §06 763**, 42 §02 767, 43 §02 780, 44 §03 761. Not for cutting (D-16). 32 §09 is 749.
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** 167 blocks in 21 chapters. **freshcheck:** 21 fresh (25–45).
- **builds:** A–C "figures: inline in the bodies, no scripts", "all eleven built clean"; D "figures: 0 checked against their scripts, 12 sourceless (content not checkable), none stale", "all four built clean"; E "figures: 14 … all fresh", "all five built clean"; F "figures: 12 … all fresh", "all four built clean"; G 21 fresh, "all seven"; H 15, "all five"; I 24, "all nine". Every chapter line in every part "vocabulary clean | questions asked once". No `!!`.
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses.
- **sweep_names:** **Schleswig 316 in 31 chapters against Slesvig 4 in 3.**
- **sweep_facts:** section 5 lists 2 (both false pairings: Dybbøl's misread 3,600 with 42's rescuers' 4,000; 1895's 114 seats with 1924's 149).
- **sweep_arrows:** 254 arrows, 37 thread notes. Form 7; direction 0; D-1 0; quoted titles 0; solvency 38 listed; prose references 0; footers 0; `<h1>` 0; 9b 0.
- **Questions (`claude/session12_qsmeasure.py` and `session12_qspairs.py` in the project, which take globs; save the first also as `qsmeasure.py` beside the second, which imports it):** on `../[0-9][0-9]-*.html`, qs 0/224, Causal 0/168, Recall 0/198; 0 opener–tier pairs.

Anything different: stop and say so.

Then read HANDOFF item 151, REVIEW-CONSISTENCY.md §17 (above all §17.3) and CONVENTIONS.md. Item 151's lesson: **a flagged claim arrives with a reason, and the reason is a claim too — check it against the source as hard as the page; and when a correction touches a fact, the questions that ask it are part of the correction** (eight of §16.5's reasons were wrong; two would have broken right pages by D-8's forbidden subtraction). Item 150's: a number handed on is a claim until it is measured again; a witness covers only the files its search was written to find. Item 147's: a correction is a claim that needs a source. Item 142's: before trusting a 0, find one case by hand the check should have caught. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit them — there is no draft, and freshcheck does not cover them); inline figures in 01–11 live in the bodies; Part D's twelve `svg_*.txt` have no generator (edit the `.txt`, and say so); Part E's and F's figures come from `fig_*.py`, `figs_*.py` and `map_*.py` — edit the script and re-run it, never the `.txt`. 25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py`.

THIS SESSION:

1. **§17.3, against sources.** Each item gets a source before a change, as in session 13: 10's "in three years" (an opener changes only if false) and the Skåne ring forts; 11's Estrid (DBL: half-sister); 12's leding before c. 1170 (hedge if the page states it flatly); 13 §11's hostages ("ti gidsler"); 16 Fig. 2's September 1398; 18's "In 1437 or 1438 he left for Gotland"; 19 Fig. 2's "six of the Buchwald" (unsourced — a figure is built only from sourceable numbers) and Meldorf 13 or 14 February; 20 Fig. 3's schematic bars against the tenth the caption cites; 22's Glückstadt; 02 §07 "among the oldest representational art". Re-read each changed page's questions.

2. **Tooling:** `build_part_g.py`, `build_part_h.py`, `build_part_i.py` still write a page before its structural checks (the A–F builds write only after all pass) — bring them to the A–F order and plant cases to prove it; no build counts the CSS brace imbalance it prints; `figcheck` does not run `map_*.py`.

3. **For Carsten, not for this session:** 15 opener 4 ("the richest king Denmark had seen in a century" — the page says "He had no treasury"); 21 and 45 at 50 minutes, the top of the band; the five OVER sections; whether the maps' "Ditmarschen" aria-labels follow D-15.

4. **Before handing over, have an agent that has not seen the work check every hunk**, and every correction against its source; if the fixes change, a second agent checks the changes; and a third if those change.

5. **Save state to the project at intervals** (`claude/session14_state.md` and a WIP patch against the commit you cloned): after the cold run, after each task, after each check. If usage runs long, stop at a save and write the next START_HERE. The project is near full; keep saves small, and ask before deleting anything from it.

Delivery as always: source files only, as one `git format-patch`, never generated pages or generated `svg_*.txt` or generated bodies (01–24's bodies are sources). Carsten downloads it to `~/Downloads/`.

Carsten commits, builds and pushes, **pages in the same commit as the sources**, and **he builds only when told to**: the handover ends with the exact shell commands, in order, and names the pages that change. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter. If any line prints `!!`, NOT BUILT or NOT WRITTEN, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, `build_part_e.py` for 16–20, `build_part_f.py` for 21–24, `build_part_g.py` for 25–31, `build_part_h.py` for 32–36, `build_part_i.py` for 37–45) — and a part whose pages use a changed map is rebuilt too — then `linkindex.py`, then `index_generator.py`, **after every part build, since a part build strips the index link `linkindex.py` adds.** End the session with a HANDOFF item (152) and the next START_HERE.
