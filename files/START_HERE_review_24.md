The consistency review, session 24: the fact-check's open lists

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the twenty-fourth session of the consistency review, which checks whether the book agrees with itself and with its sources. Every part has been read at depth (sessions 3–11), D-17 (ask once) holds on all 45 pages, and the figures' text is legible and measured in the page (sessions 16–21; D-18, D-19, D-20, D-11). Session 23 fact-checked chapters 01–15 against sources, one checker per chapter, as 16–45 had been in sessions 7–11: 268 corrections, 61 intervals and ages wrong (D-8); Carsten decided 04's opener and §01 heading ("no copper or tin"), "the Schlei" in 14 (D-15), Lola's date from the paper, and that the checkpoint copies in the bodies of 01–20 be synced to what ships (D-17 now says where a checkpoint lives). The web-search allowance ran out during that fact-check, so each of its fifteen reports (`claude/session23_factcheck_01..15.md` in the project) ends with a §H of claims a checker could not reach, and the check reports (`claude/session23_check1_A.md`, `_B.md`, `_C.md`, `claude/session23_check2.md`) each have a "could not check" list.

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

Expected, as run after item 161's rebuild. `mapfixture.py` takes a few minutes; do not kill it. `figcheck --regen` re-runs every figure script, maps included, so `git status --short` must still be clean after it — if a `svg_*.txt` changes, a generator was edited and never run; stop and say so. The part builds strip the index link, so run `python3 linkindex.py` and `python3 index_generator.py` after them, and then `git status --short` should be clean again.

- **git log:** the commit carrying item 161's patch **must carry pages 01–15 and 34**, the regenerated `c34_body.html`, and the sources: `c01_body.html` … `c20_body.html`, `c34_draft.md`, Part D's seven hand `svg_*.txt` (`svg_dioceses`, `svg_terr_1250`, `svg_descent`, `svg_herring`, `svg_pawn`, `svg_arithmetic`, `svg_reconquest`), `build_parts_abc.py`, `build_part_d.py`, `CONVENTIONS.md`, `HANDOFF.md`, `REVIEW-CONSISTENCY.md` and this `START_HERE_review_24.md` — 51 files against `f9f380a`, and nothing else. The index does not change. If debuild reports BODY DRIFT, freshcheck a body STALE, figcheck a figure disagreeing with its source, any build a figure that is not fresh or a page NOT BUILT / NOT WRITTEN, they were not pushed; stop and say so.
- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **355,295 page words, 28.2 h**. Part A 22,122; B 26,978; C 27,541; D 33,431; E 36,912; F 30,481; G 54,240; H 43,467; I 80,123. 21 is 50 minutes (10,559 words), 44 is 48, 45 is 50; "outside the 25-50 minute band (each page's own stamp, as the builds wrote it): none".
- **vignettes:** 148 carry a place, 116 distinct; selftest passes; 01, 03, 04, 05 "[f] part"; no D-9 failure anywhere.
- **figcheck --regen:** every script "ok" with no warning lines under it; 98 match, 30 sourceless "(Parts A-C: expected, not a fault)", 0 disagree; "the figure scripts printed 0 warning lines".
- **narrative:** (it prints the section number and title, not the chapter; the chapters are in page order) the five print "OVER, kept (D-16, at N)" — 16 §08 852, 21 §06 763, 42 §02 767, 43 §02 780, 44 §03 761 — and "OVER: 5, of which kept (D-16): 5, not kept: 0". A plain OVER is new: stop and say so. 32 §09 is 749; 13 §06 is 466.
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** 167 blocks in 21 chapters. **freshcheck:** 21 fresh (25–45), no `!!` line.
- **builds:** A–C "all eleven built clean"; D "0 checked against their scripts, 12 sourceless, none stale", "all four built clean"; E 14 fresh, "all five built clean"; F 12, "all four built clean"; G 21, "all seven built clean"; H 15, "all five built clean"; I 24, "all nine built clean". Every chapter line "braces 0 | placeholders 0 | anchors ok | tags ok"; no `!` or `!!` line in any build. `build_part_g.py --stub` refuses, with its own `!!` line ("--stub is not offered in Part G"), as meant.
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses. **sweep_names:** **Schleswig 318 in 32 chapters** against Slesvig 4 in 3. **sweep_facts:** "impossible dates (…): 0"; section 5 lists 2. **sweep_arrows:** 254 arrows, 37 thread notes; form 7; 3b (D-1, for information) 11; solvency 38; the rest 0.
- **linecheck:** over `svg_*.txt`, 0 text(s) crossed, with three "= … on purpose" lines (partition's HADERSLEV, the baltic and reconquest titles); over 01–11's bodies, 0; `--bare`, 213.
- **ordercheck:** "0 text(s) painted over, in 0 of 128 figure(s) on 45 page(s), at 1200 px; 0 figure(s) under 0.8 of their viewBox; 0 scroll line(s) wrong; 0 text(s) drawn in another colour than they ask", and the same "at 390 px"; without Playwright or a Chromium it prints SKIPPED and exits 2 - say so rather than count it a pass.
- **Questions (`claude/session12_qsmeasure.py` and `session12_qspairs.py` in the project, which take globs; save the first also as `qsmeasure.py` beside the second, which imports it):** on `../[0-9][0-9]-*.html`, qs 0/224, Causal 0/168, Recall 0/198; 0 opener–tier pairs. And every body 01–20's checkpoint copy equals its page's checkpoints, block for block and before the same section (D-17, "Where a checkpoint lives"): for each NN, the `<div class="check">…</div>` blocks with the `<h2 id="sNN">` that follows each, taken from `cNN_body.html` and from the page, are the same list (`re.findall(r'(<div class="check">.*?</div>)\s*<h2 id="(s\d\d)">', h, re.S)`).
- **Widths (`claude/session19_phone.py`, `python3 phone.py .. 390`):** no PAGE OVERFLOWS line; 128 "WIDER THAN ITS BOX" lines, as meant (D-20); every figure's smallest text 6.80 px (123) or 7.60 (5). And `claude/session21_widths.py` (`python3 session21_widths.py ..`): every one of its 24 widths "ok".

Anything different: stop and say so.

Then read HANDOFF items 161, 160 and 159, REVIEW-CONSISTENCY.md §27, CONVENTIONS D-8, D-15, D-16 and D-17. Item 161's lesson: **a correction's ground reaches further than its hunk, and a copy nobody builds from is a claim nobody checks: carry a correction to every place its ground holds, and edit what ships.** Item 160's: before recommending, find what already does the thing; before correcting a record, read the record you correct. Item 159's: a deletion is a claim about what was drawn - count the markup and measure the page; before writing a rule for a range, plant a case in each part of the range. Item 157's: plant what the check should catch, at the edge of what it measures, before trusting its silence. Item 156's: only the page shows what was drawn; measure the page. Item 150's: a number handed on is a claim until it is measured again. Item 147's: a correction is a claim that needs a source. Item 142's: before trusting a 0, find one case by hand the check should have caught. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit them — there is no draft, and freshcheck does not cover them); inline figures in 01–11 live in the bodies; Part D's twelve `svg_*.txt` have no generator (edit the `.txt`, and say so); Part E's to I's figures come from `fig_*.py`, `figs_*.py` and `map_*.py` (a script's number is not always its chapter's: `figs_17.py` draws page 18's) — edit the script and re-run it, never the `.txt`. 25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py` (`DK_DRAFT=cNN_draft.md python3 mkbody.py NN` for 32–45). **Checkpoints live in the build scripts' `checks`**; the bodies of 01–20 carry a copy: edit the config, then the copy (D-17). Figure text: D-18, D-19 and D-20; a meant colour only in `style=` (D-11). A new viewBox width needs its min-width line and its scroll line in `style.css` (D-20).

THIS SESSION:

1. **Recommended in §27.8, for Carsten to confirm first:** read the fifteen reports' §H lists (`claude/session23_factcheck_01..15.md`, section H) and the check reports' "could not check" lists (`claude/session23_check1_A.md`, `_B.md`, `_C.md`, `claude/session23_check2.md`) with a fresh search allowance, and settle, hedge or record each claim — among them Skuldelev 2's stage (which decides 11's "sunk c. 1070"), 12's 1053 Adalbert sentence (Wikipedia alone), Worsaae's first printing, 03's Gjerrild details, 09's Frideborg (Rimbert), 14's Jyske Lov and thralls, 15's Golden Bull line. Ask Carsten before doing anything; if he chooses otherwise, plan what he chooses. Measure the result in the page at 390 and 1200. Never propose a cut for the sake of time (D-16).

2. **Before handing over, have an agent that has not seen the work check every hunk** — every changed figure looked at in the page, in a browser (Chromium), at the desktop and the phone width; every claim written into a comment, docstring or record tried; `ordercheck.py` run over all 45 pages at 1200 and 390; if the fixes change, a second agent checks the changes; and a third if those change.

3. **Save state to the project at intervals** (`claude/session24_state.md` and a WIP patch against the commit you cloned; `git diff -U0` keeps it small): after the cold run, after each task, after each check. The project's knowledge store is filling (about 1.6 of 2 MB after session 23; `project_info` gives the figure): keep saves small, and ask Carsten before deleting anything from it (superseded `sessionNN_wip.patch` files are the obvious candidates).

Delivery as always: source files only, as one `git format-patch`, never generated pages or generated `svg_*.txt` or generated bodies (01–24's bodies and Part D's twelve `svg_*.txt` are sources). Carsten downloads it to `~/Downloads/`.

Carsten commits, builds and pushes, **pages in the same commit as the sources**, and **he builds only when told to**: the handover ends with the exact shell commands, in order, and names the pages that change. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter. If any line prints `!!`, NOT BUILT or NOT WRITTEN, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, `build_part_e.py` for 16–20, `build_part_f.py` for 21–24, `build_part_g.py` for 25–31, `build_part_h.py` for 32–36, `build_part_i.py` for 37–45) — and a part whose pages use a changed map is rebuilt too — then `linkindex.py`, then `index_generator.py`, **after every part build, since a part build strips the index link `linkindex.py` adds.** End the session with a HANDOFF item (162) and the next START_HERE.
