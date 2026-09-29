The consistency review, session 19: what the page shows that the files do not

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the nineteenth session of the consistency review, which checks whether the book agrees with itself. Every part has been read at depth (sessions 3–12), D-17 (ask once) holds on all 45 pages, sessions 13–15 checked §16.5, §17.3 and §18.3 against sources, session 16 gave every figure label a halo (D-18), session 17 made the figure scripts' warnings visible and ran the text guards over the hand-drawn figures, and session 18 measured figure text in the page (D-19: `CHAR_W` mapt 6.10, mapx 5.46, mapl 6.95; the serif titles sized), and found by measuring the page that page 18's roads map had never drawn its bottom hundred units (a clip id shared by two figures; `pageguard.duplicate_ids()` now refuses that). No new chapters, no repartition.

Clone github.com/carstendan/danish_history. From files/, with DK_CHAPTERS, DK_OUT and DK_SRC unset, and with `cairosvg` installed (`pip install cairosvg`; without it every figure script prints `!!`), run the cold run first and report what fails rather than working around it:

git status --short
python3 tidy.py
python3 mapfixture.py
python3 seamcheck.py
python3 debuild.py verify ../[0-9][0-9]-*.html
python3 bookstats.py
python3 vignettes.py . ; python3 vignettes.py --selftest
python3 figcheck.py --regen
python3 narrative.py ../[0-9][0-9]-*.html
python3 draftnotes.py ../[0-9][0-9]-*.html
python3 draftnotes.py c3[2-9]_draft.md c4[0-5]_draft.md
python3 appcheck.py
python3 freshcheck.py
python3 build_parts_abc.py ; python3 build_part_d.py ; python3 build_part_e.py ; python3 build_part_f.py
python3 build_part_g.py ; python3 build_part_h.py ; python3 build_part_i.py
python3 sweep_glossary.py ; python3 sweep_names.py ; python3 sweep_facts.py ; python3 sweep_arrows.py
python3 linecheck.py svg_*.txt | tail -4
python3 linecheck.py c0[1-9]_body.html c1[01]_body.html | tail -1
python3 linecheck.py --bare svg_*.txt | tail -1

Expected, as run after item 156's rebuild. `mapfixture.py` takes a few minutes; do not kill it. `figcheck --regen` re-runs every figure script, maps included, so `git status --short` must still be clean after it — if a `svg_*.txt` changes, a generator was edited and never run; stop and say so. The part builds strip the index link, so run `python3 linkindex.py` and `python3 index_generator.py` after them, and then `git status --short` should be clean again.

- **git log:** the commit carrying item 156's patch **must carry pages 02, 08, 11, 16, 18, 30, 38, 39, 40, 41, 42, 43, 44 and 45**, the 23 regenerated `svg_*.txt` (aar_1920, bornholm_1946, domme_1945, folkestrejke_1944, gulv_1953, kanslergade_1933, kapsler_1921, krak_1922, kurs_1933, landsting_1953, morgen_1940, oktober_1943, papers, regel_1939, roads, sabotage_1945, sydslesvig_1954, ting_1924, titles, tobilletter_1953, udleveret_1941, valg_1943, zoner_1920), and the sources: bodies 02, 08, 11, `mapspine.py`, `pageguard.py`, `linecheck.py`, `fig_titles.py`, `figs_17.py`, `figs_23.py` to `figs_31.py`, `figs_39.py` to `figs_44.py`, `CONVENTIONS.md`, `HANDOFF.md`, `REVIEW-CONSISTENCY.md` and this `START_HERE_review_19.md`. The index does not change. If debuild reports BODY DRIFT, freshcheck a body STALE, figcheck a figure disagreeing with its source, any build a figure that is not fresh or a page NOT BUILT / NOT WRITTEN, they were not pushed; stop and say so.
- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **352,732 page words, 28.0 h**. Part A 21,534; B 26,496; C 26,820; D 32,666; E 36,912; F 30,481; G 54,240; H 43,460; I 80,123. **21 is 50 minutes** (10,559 words), 44 is 48, **45 is 50**.
- **vignettes:** 148 carry a place, 116 distinct; selftest passes; 01, 03, 04, 05 "[f] part"; no D-9 failure anywhere.
- **figcheck --regen:** every script "ok" with no warning lines under it; 98 match, 30 sourceless "(Parts A-C: expected, not a fault)", 0 disagree; **"the figure scripts printed 0 warning lines"**.
- **narrative:** five OVER — 16 §08 852, 21 §06 763, 42 §02 767, 43 §02 780, 44 §03 761. Not for cutting (D-16). 32 §09 is 749; 13 §06 is 466.
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** 167 blocks in 21 chapters. **freshcheck:** 21 fresh (25–45), no `!!` line.
- **builds:** A–C "all eleven built clean"; D "0 checked against their scripts, 12 sourceless, none stale", "all four built clean"; E 14 fresh, "all five built clean"; F 12, "all four built clean"; G 21, "all seven built clean"; H 15, "all five built clean"; I 24, "all nine built clean". Every chapter line "braces 0", "tags ok" (a duplicate id now fails "tags"), "vocabulary clean | questions asked once"; no `!` or `!!` line anywhere. `build_part_g.py --stub` refuses.
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses. **sweep_names:** Schleswig 317 in 32 chapters against Slesvig 4 in 3. **sweep_facts:** "impossible dates (…): 0"; section 5 lists 2. **sweep_arrows:** 254 arrows, 37 thread notes; form 7; 3b (D-1, for information) 11; solvency 38; the rest 0.
- **linecheck:** over `svg_*.txt`, **0 text(s) crossed**, with three "= … on purpose" lines (partition's HADERSLEV, the baltic and reconquest titles); over 01–11's bodies, **0**; `--bare`, **214** (213 before session 18's widths).
- **Questions (`claude/session12_qsmeasure.py` and `session12_qspairs.py` in the project, which take globs; save the first also as `qsmeasure.py` beside the second, which imports it):** on `../[0-9][0-9]-*.html`, qs 0/224, Causal 0/168, Recall 0/198; 0 opener–tier pairs.

Anything different: stop and say so.

Then read HANDOFF items 156 and 155, REVIEW-CONSISTENCY.md §22, CONVENTIONS D-18 and D-19, and `pageguard.duplicate_ids()`. Item 156's lesson: **each figure file was fine alone; the fault was in the page, where two of them met. A guard that reads the sources checks what was written; only the page shows what was drawn. And a workaround outlives the fault it worked around - measure the page, then delete what the measurement makes unnecessary.** Item 155's: a guard that runs only where a script runs is not a guard for what no script writes; a constant is a claim like a count. Item 154's: a brief's expectation is a claim too; before explaining a failure by the tool, try it without your change. Item 153's: a new guard's first run is a reading pass. Item 152's: a checker's correction is a claim too; a quotation is checked against the page it quotes, letter by letter. Item 151's: a flagged claim arrives with a reason, and the reason is a claim too. Item 150's: a number handed on is a claim until it is measured again. Item 147's: a correction is a claim that needs a source. Item 142's: before trusting a 0, find one case by hand the check should have caught. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit them — there is no draft, and freshcheck does not cover them); inline figures in 01–11 live in the bodies; Part D's twelve `svg_*.txt` have no generator (edit the `.txt`, and say so); Part E's to I's figures come from `fig_*.py`, `figs_*.py` and `map_*.py` — edit the script and re-run it, never the `.txt`. 25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py` (`DK_DRAFT=cNN_draft.md python3 mkbody.py NN` for 32–45). Figure text: D-18 and D-19. The text guards (`overruns`, `overflows`, `collisions`) run inside every figure script and, through `pageguard.figure_text()`, in the A–C and D builds; `duplicate_ids()` in every build.

THIS SESSION:

1. **The page, measured for what it paints (§22.3).** Session 18's order measure (`claude/session18_order.py`: every text moved to the end of its `<svg>`, pixels compared inside each text's box) found two shipped faults the file guards could not see. It is a script in the project, wired into nothing. Decide with Carsten whether it becomes a tool in `files/` (it needs Chromium; the builds do not), run it over all 45 pages as they stand, and read everything it lists, below its 6-pixel floor too (a floor is a claim: find one case by hand it should catch). Then say what else only the page can show — a `<use>`, a marker or pattern shared across figures, CSS that reaches into an SVG, a figure wider than the column at the phone width — and measure one of them.

2. **The roads legend (page 18).** With the map drawn to 700, its legend sits on the Elbe and the Frisian coast (haloed, legible). Give it its own ground, or say why not; look at it in the page.

3. **What check 1 saw that was not session 18's (§22.5).** 43's "924" and "988" on the 1,000 gridline; 21's "Gottorp" a unit above "Ditmarsken"; 16's "The title fell…" past the header rule's end; 18's Helsingborg 0.2 units from the strip line; 39's "RESCUE TWO … share capital." about 7 units from the edge on the Mac. Fix what reads better fixed; look at each in the page.

4. **For Carsten, not for this session:** the order measure as a tool (task 1); whether dark `ON_BAR_INK` on the three grey bars of 01–03 is right (white there is 3.2:1); whether `linecheck` is wired into the builds; the D-11 legacy colours; 10's opener 3; 15's opener 4; 21 and 45 at 50 minutes; the five OVER; the maps' "Ditmarschen" aria-labels (`svg_terr_1500/1600/1660`, pages 19, 21, 25) against D-15; Lindholmen named in 16's key only; the Sound strip's last line near the caption; `maps-contact-sheet.html`'s repeated (identical) ids.

5. **Before handing over, have an agent that has not seen the work check every hunk** — every changed figure looked at in the page, in a browser (Chromium: `/opt/pw-browsers/chromium`), not only in its PNG; every claim written into a comment or docstring tried; if the fixes change, a second agent checks the changes; and a third if those change.

6. **Save state to the project at intervals** (`claude/session19_state.md` and a WIP patch against the commit you cloned; `git diff -U0` keeps it small): after the cold run, after each task, after each check. If usage runs long, stop at a save and write the next START_HERE. The project's knowledge store is about half full; keep saves small, and ask before deleting anything from it.

Delivery as always: source files only, as one `git format-patch`, never generated pages or generated `svg_*.txt` or generated bodies (01–24's bodies and Part D's twelve `svg_*.txt` are sources). Carsten downloads it to `~/Downloads/`.

Carsten commits, builds and pushes, **pages in the same commit as the sources**, and **he builds only when told to**: the handover ends with the exact shell commands, in order, and names the pages that change. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter. If any line prints `!!`, NOT BUILT or NOT WRITTEN, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, `build_part_e.py` for 16–20, `build_part_f.py` for 21–24, `build_part_g.py` for 25–31, `build_part_h.py` for 32–36, `build_part_i.py` for 37–45) — and a part whose pages use a changed map is rebuilt too — then `linkindex.py`, then `index_generator.py`, **after every part build, since a part build strips the index link `linkindex.py` adds.** End the session with a HANDOFF item (157) and the next START_HERE.
