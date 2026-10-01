The consistency review, session 22: what Carsten has left open

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the twenty-second session of the consistency review, which checks whether the book agrees with itself. Every part has been read at depth (sessions 3–12), D-17 (ask once) holds on all 45 pages, sessions 13–15 checked §16.5, §17.3 and §18.3 against sources, sessions 16–20 made the figures' text legible and measured them in the page (D-18, D-19, D-20, D-11), and session 21 carried out Carsten's six decisions: every `fill=` on a figure text deleted (357; the two page 06 honoured, SILVER and BRONZE, moved into `style=`) and refused in the builds (`pageguard.text_fills()`); the colour measure taken into `ordercheck.py`, which also lists a figure whose new scroll line ("Wider than the screen — scroll sideways →", shown where a figure scrolls on a narrow screen) disagrees with its scrolling; the width queries written classic and range; the breakout caption at the figure's padding; `pageguard.figure_widths()` cut back to finding each width's two lines. It also fixed figs_19's key, the Sound strip's repeated line, Lindholmen's label and the maps' "Dithmarschen", and measured ON_BAR_INK (kept). No new chapters, no repartition.

Clone github.com/carstendan/danish_history. From files/, with DK_CHAPTERS, DK_OUT and DK_SRC unset, and with `cairosvg` installed (`pip install cairosvg`; without it every figure script prints `!!`) and Playwright with a Chromium for `ordercheck.py` (in the container: `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, which the tool finds itself, or `DK_CHROMIUM=`), run the cold run first and report what fails rather than working around it:

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
python3 ordercheck.py ../[0-9][0-9]-*.html | tail -1
python3 ordercheck.py --width 390 ../[0-9][0-9]-*.html | tail -1

Expected, as run after item 159's rebuild. `mapfixture.py` takes a few minutes; do not kill it. `figcheck --regen` re-runs every figure script, maps included, so `git status --short` must still be clean after it — if a `svg_*.txt` changes, a generator was edited and never run; stop and say so. The part builds strip the index link, so run `python3 linkindex.py` and `python3 index_generator.py` after them, and then `git status --short` should be clean again.

- **git log:** the commit carrying item 159's patch **must carry all 45 pages** (`style.css` changed), the 26 regenerated `svg_*.txt` (1807, aar_1920, afstemning_1916, atlantic, brondum, column, crowns, daler, fealty, feud, hemming, krak_1922, ledger, papers, plague_1711, scania, sound, terr_1500, terr_1600, terr_1660, titles, toll, transfer, village, weeks, zoner_1920), and the sources: `style.css`, `pageguard.py`, `ordercheck.py`, bodies 01, 06, 07, 08 and 11, Part D's `svg_arithmetic.txt`, `svg_descent.txt`, `svg_herring.txt`, `svg_leding.txt`, `svg_pawn.txt`, `svg_plague.txt`, `svg_reconquest.txt` and `svg_reigns.txt` (sources, edited by hand), `fig_crowns.py`, `fig_titles.py`, `figs_16b.py`, `figs_17.py`, `figs_18.py`, `figs_19.py`, `figs_22.py`, `figs_26.py`, `figs_27.py`, `figs_29.py`, `figs_30.py`, `figs_31.py`, `figs_37.py`, `figs_38.py`, `figs_39.py`, `map_1500.py`, `map_1600.py`, `map_1660.py`, `CONVENTIONS.md`, `HANDOFF.md`, `REVIEW-CONSISTENCY.md` and this `START_HERE_review_22.md`. The index does not change. If debuild reports BODY DRIFT, freshcheck a body STALE, figcheck a figure disagreeing with its source, any build a figure that is not fresh or a page NOT BUILT / NOT WRITTEN, they were not pushed; stop and say so.
- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **352,732 page words, 28.0 h**. Part A 21,534; B 26,496; C 26,820; D 32,666; E 36,912; F 30,481; G 54,240; H 43,460; I 80,123. **21 is 50 minutes** (10,559 words), 44 is 48, **45 is 50**.
- **vignettes:** 148 carry a place, 116 distinct; selftest passes; 01, 03, 04, 05 "[f] part"; no D-9 failure anywhere.
- **figcheck --regen:** every script "ok" with no warning lines under it; 98 match, 30 sourceless "(Parts A-C: expected, not a fault)", 0 disagree; **"the figure scripts printed 0 warning lines"**.
- **narrative:** five OVER — 16 §08 852, 21 §06 763, 42 §02 767, 43 §02 780, 44 §03 761. Not for cutting (D-16). 32 §09 is 749; 13 §06 is 466.
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** 167 blocks in 21 chapters. **freshcheck:** 21 fresh (25–45), no `!!` line.
- **builds:** A–C "all eleven built clean"; D "0 checked against their scripts, 12 sourceless, none stale", "all four built clean"; E 14 fresh, "all five built clean"; F 12, "all four built clean"; G 21, "all seven built clean"; H 15, "all five built clean"; I 24, "all nine built clean". Every chapter line "braces 0", "tags ok" (a duplicate id, a figure width with no phone or scroll line, or a `fill=` on a figure text now fails "tags"), "vocabulary clean | questions asked once"; no `!` or `!!` line anywhere. `build_part_g.py --stub` refuses.
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses. **sweep_names:** Schleswig 317 in 32 chapters against Slesvig 4 in 3. **sweep_facts:** "impossible dates (…): 0"; section 5 lists 2. **sweep_arrows:** 254 arrows, 37 thread notes; form 7; 3b (D-1, for information) 11; solvency 38; the rest 0.
- **linecheck:** over `svg_*.txt`, **0 text(s) crossed**, with three "= … on purpose" lines (partition's HADERSLEV, the baltic and reconquest titles); over 01–11's bodies, **0**; `--bare`, **213** (Lindholmen is the one more).
- **ordercheck:** "0 text(s) painted over, in 0 of 128 figure(s) on 45 page(s), at 1200 px; 0 figure(s) under 0.8 of their viewBox; 0 scroll line(s) wrong; 0 text(s) drawn in another colour than they ask", and the same "at 390 px"; without Playwright or a Chromium it prints SKIPPED and exits 2 - say so rather than count it a pass.
- **Questions (`claude/session12_qsmeasure.py` and `session12_qspairs.py` in the project, which take globs; save the first also as `qsmeasure.py` beside the second, which imports it):** on `../[0-9][0-9]-*.html`, qs 0/224, Causal 0/168, Recall 0/198; 0 opener–tier pairs.
- **Widths (`claude/session19_phone.py`, `python3 phone.py .. 390`):** no PAGE OVERFLOWS line; **128 "WIDER THAN ITS BOX" lines, as meant** (D-20); every figure's smallest text 6.80 px (123) or 7.60 (5). And `claude/session21_widths.py` (`python3 session21_widths.py ..`): every one of its 24 widths "ok", the scroll line where the figure scrolls.

Anything different: stop and say so.

Then read HANDOFF items 159 and 158, REVIEW-CONSISTENCY.md §25, CONVENTIONS D-11 and D-20, and `ordercheck.py`'s docstring. Item 159's lesson: **a deletion is a claim about what was drawn - count the markup and measure the page, and act on the difference; and before writing a rule for a range, plant a case in each part of the range.** Item 158's: a plan is a claim too; measure at the widths between the ones decided, and re-plant a tool when what it measures changes size. Item 157's: a floor is a claim, and so is a box: plant what the check should catch, at the edge of what it measures, before trusting its silence. Item 156's: only the page shows what was drawn; measure the page. Item 155's: a guard that runs only where a script runs is not a guard for what no script writes. Item 154's: a brief's expectation is a claim too. Item 153's: a new guard's first run is a reading pass. Item 152's: a checker's correction is a claim too. Item 150's: a number handed on is a claim until it is measured again. Item 147's: a correction is a claim that needs a source. Item 142's: before trusting a 0, find one case by hand the check should have caught. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit them — there is no draft, and freshcheck does not cover them); inline figures in 01–11 live in the bodies; Part D's twelve `svg_*.txt` have no generator (edit the `.txt`, and say so); Part E's to I's figures come from `fig_*.py`, `figs_*.py` and `map_*.py` — edit the script and re-run it, never the `.txt`. 25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py` (`DK_DRAFT=cNN_draft.md python3 mkbody.py NN` for 32–45). Figure text: D-18, D-19 and D-20; a meant colour only in `style=` (D-11; `fill=` on a text is refused). A new viewBox width needs its min-width line and its scroll line in `style.css` (a multiple of 5; D-20 gives the bands; 785 to 820 has none yet). `ordercheck.py` (standalone, Chromium) lists, at a width, what is painted over a text, any figure under 0.8 of its viewBox, any scroll line that disagrees with its figure, and any text drawn in another colour than it asks.

THIS SESSION:

1. **Carsten's open items from §25.8, one at a time, each with a recommendation:** the Sound strip's two remaining lines, which repeat the prose above the figure on page 18; whether `linecheck` is wired into the builds, and whether it should read drawing order; 10's opener 3; 15's opener 4; 21 and 45 at 50 minutes; the five OVER (not for cutting). Whatever he chooses that is work, plan it before doing it, and measure the result in the page at 390 and 1200.

2. **Before handing over, have an agent that has not seen the work check every hunk** — every changed figure looked at in the page, in a browser (Chromium), at the desktop and the phone width; every claim written into a comment or docstring tried; `ordercheck.py` run over all 45 pages at 1200 and 390; if the fixes change, a second agent checks the changes; and a third if those change.

3. **Save state to the project at intervals** (`claude/session22_state.md` and a WIP patch against the commit you cloned; `git diff -U0` keeps it small): after the cold run, after each task, after each check. If usage runs long, stop at a save and write the next START_HERE. The project's knowledge store is filling; keep saves small, and ask before deleting anything from it.

Delivery as always: source files only, as one `git format-patch`, never generated pages or generated `svg_*.txt` or generated bodies (01–24's bodies and Part D's twelve `svg_*.txt` are sources). Carsten downloads it to `~/Downloads/`.

Carsten commits, builds and pushes, **pages in the same commit as the sources**, and **he builds only when told to**: the handover ends with the exact shell commands, in order, and names the pages that change. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter. If any line prints `!!`, NOT BUILT or NOT WRITTEN, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, `build_part_e.py` for 16–20, `build_part_f.py` for 21–24, `build_part_g.py` for 25–31, `build_part_h.py` for 32–36, `build_part_i.py` for 37–45) — and a part whose pages use a changed map is rebuilt too — then `linkindex.py`, then `index_generator.py`, **after every part build, since a part build strips the index link `linkindex.py` adds.** End the session with a HANDOFF item (160) and the next START_HERE.
