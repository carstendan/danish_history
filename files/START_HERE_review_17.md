The consistency review, session 17: the warnings nobody reads, and the texts nobody measures

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the seventeenth session of the consistency review, which checks whether the book agrees with itself. Every part has been read at depth (sessions 3–12), D-17 (ask once) holds on all 45 pages, sessions 13–15 checked §16.5, §17.3 and §18.3 against sources, and session 16 read the figures' crossings and gave every figure label a halo (D-18). No new chapters, no repartition.

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
python3 linecheck.py c0[1-9]_body.html c1[01]_body.html | tail -2
python3 linecheck.py --bare svg_*.txt | tail -1

Expected, as run after item 154's rebuild. `mapfixture.py` takes a few minutes; do not kill it. `figcheck --regen` re-runs every figure script, maps included, so `git status --short` must still be clean after it — if a `svg_*.txt` changes, a generator was edited and never run; stop and say so. The part builds strip the index link, so run `python3 linkindex.py` and `python3 index_generator.py` after them, and then `git status --short` should be clean again.

- **git log:** the commit carrying item 154's patch **must carry all 45 rebuilt pages** (the halo is in `style.css`), the regenerated `svg_1807.txt`, `svg_atlantic.txt`, `svg_feud.txt`, `svg_icemarch.txt`, `svg_roads.txt`, `svg_sound.txt`, `svg_terr_1721.txt`, `svg_terr_1814.txt`, `svg_terr_1864.txt`, `svg_zoner_1920.txt`, and the sources `svg_baltic.txt`, `svg_reconquest.txt` and bodies 01, 02, 03, 06, 07, 08, 09, 10. The index does not change. If debuild reports BODY DRIFT, freshcheck a body STALE, figcheck a figure disagreeing with its source, any build a figure that is not fresh or a page NOT BUILT / NOT WRITTEN, they were not pushed; stop and say so.
- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **352,732 page words, 28.0 h**. Part A 21,534; B 26,496; C 26,820; D 32,666; E 36,912; F 30,481; G 54,240; H 43,460; I 80,123. **21 is 50 minutes** (10,559 words), 44 is 48, **45 is 50**.
- **vignettes:** 148 carry a place, 116 distinct; selftest passes; 01, 03, 04, 05 "[f] part"; no D-9 failure anywhere.
- **figcheck --regen:** every script "ok"; 98 match, 30 sourceless "(Parts A-C: expected, not a fault)", 0 disagree.
- **narrative:** five OVER — 16 §08 852, 21 §06 763, 42 §02 767, 43 §02 780, 44 §03 761. Not for cutting (D-16). 32 §09 is 749; 13 §06 is 466.
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** 167 blocks in 21 chapters. **freshcheck:** 21 fresh (25–45).
- **builds:** as START_HERE_review_16: A–C "all eleven built clean"; D "0 checked against their scripts, 12 sourceless, none stale", "all four"; E 14 fresh, "all five"; F 12, "all four"; G 21, "all seven"; H 15, "all five"; I 24, "all nine". Every chapter line "braces 0", "tags ok", "vocabulary clean | questions asked once"; no NOT WRITTEN; no `!!`. `build_part_g.py --stub` refuses.
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses. **sweep_names:** Schleswig 317 in 32 chapters against Slesvig 4 in 3. **sweep_facts:** section 5 lists 2. **sweep_arrows:** 254 arrows, 37 thread notes; form 7; 3b (D-1, for information) 11; solvency 38; the rest 0.
- **linecheck:** over `svg_*.txt`, **0 text(s) crossed**, with three "= … on purpose" lines (partition's HADERSLEV, the baltic and reconquest titles); over 01–11's bodies, **0**, with one "= … measured wrong" (06's "the great majority"); `--bare`, **213**.
- **Questions (`claude/session12_qsmeasure.py` and `session12_qspairs.py` in the project, which take globs; save the first also as `qsmeasure.py` beside the second, which imports it):** on `../[0-9][0-9]-*.html`, qs 0/224, Causal 0/168, Recall 0/198; 0 opener–tier pairs.

Anything different: stop and say so.

Then read HANDOFF item 154, REVIEW-CONSISTENCY.md §20 and CONVENTIONS.md (D-18 is new). Item 154's lesson: **a brief's expectation is a claim too ("most are set on purpose" was the opposite of what reading the 220 found); and before explaining a failure by the tool, try it without your change ("cairosvg cannot draw these arrowheads" was this session's own zeroed stroke).** Item 153's: a new guard's first run is a reading pass — run a new check over everything before trusting its 0 (linecheck's first run over 01–11 found fourteen); a checker's report of an absence is a claim like any other. Item 152's: a checker's correction is a claim too; a quotation is checked against the page it quotes, letter by letter, by whoever changes it last. Item 151's: a flagged claim arrives with a reason, and the reason is a claim too. Item 150's: a number handed on is a claim until it is measured again. Item 147's: a correction is a claim that needs a source. Item 142's: before trusting a 0, find one case by hand the check should have caught. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit them — there is no draft, and freshcheck does not cover them); inline figures in 01–11 live in the bodies; Part D's twelve `svg_*.txt` have no generator (edit the `.txt`, and say so); Part E's and F's figures come from `fig_*.py`, `figs_*.py` and `map_*.py` — edit the script and re-run it, never the `.txt`. 25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py` (`DK_DRAFT=cNN_draft.md python3 mkbody.py NN` for 32–45). Figure text: D-18 — a thin line under a label is the halo's; a thick line or a marker through a label is moved; a light or `ON_BAR_INK` text is written `style="fill:#XXXXXX"`.

THIS SESSION:

1. **The warnings nobody reads.** Page 18's Sound figure shipped without its explanatory strip for as long as `overflows()` had been printing so on every run of `figs_17.py`: `figcheck --regen` runs every figure script and shows none of their `!` lines. Make `figcheck --regen` report every `!`/`!!` line a script prints, by script, and say at the end how many (0 today, after item 154 — confirm by running each script alone first). Plant one overflow and one collision in a scratch copy of a script and show both reach the report. Then look for other places the project runs a tool and discards what it says (the builds call the figure checks; tidy, freshcheck, the sweeps) — list them, fix what is cheap, and say which.

2. **The texts nobody measures.** `mapspine.text_boxes()` — which `collisions()`, `overruns()`, `overflows()` and `linecheck.py` all use — skips a text with markup inside (5, in 4 files), measures a rotated text unrotated (13), and does not see a `text-anchor` set on a `<g>` (2 groups; 06's "the great majority" is in `linecheck.KNOWN_FALSE` for it). Read each of these twenty against its figure in the page. Then either teach `text_boxes()` the `<g>` anchor (and the `transform="rotate(...)"` if it is cheap), or say why not; if it changes what any guard reports, that is a reading pass — read it before trusting it. Plant one case of each.

3. **For Carsten, not for this session:** whether dark `ON_BAR_INK` on the three grey bars of 01–03 is right (white there is 3.2:1); whether `linecheck` is wired into the builds; the D-11 legacy colours (`fill=` attributes that draw grey — "four kilometres", zoner's counts, DANELAW, NORMANDY, GERMANIA LIBERA and the rest); 10's opener 3; 15's opener 4; 21 and 45 at 50 minutes; the five OVER; the maps' "Ditmarschen" aria-labels (`svg_terr_1500/1600/1660`, pages 19, 21, 25) against D-15; Lindholmen named in 16's key only; the Sound strip's last line near the caption.

4. **Before handing over, have an agent that has not seen the work check every hunk** — every changed figure looked at in the page, in a browser (Chromium: `/opt/pw-browsers/chromium`), not only in its PNG; every claim written into a comment or docstring tried; if the fixes change, a second agent checks the changes; and a third if those change.

5. **Save state to the project at intervals** (`claude/session17_state.md` and a WIP patch against the commit you cloned): after the cold run, after each task, after each check. If usage runs long, stop at a save and write the next START_HERE. The project is near full; keep saves small, and ask before deleting anything from it.

Delivery as always: source files only, as one `git format-patch`, never generated pages or generated `svg_*.txt` or generated bodies (01–24's bodies and Part D's twelve `svg_*.txt` are sources). Carsten downloads it to `~/Downloads/`.

Carsten commits, builds and pushes, **pages in the same commit as the sources**, and **he builds only when told to**: the handover ends with the exact shell commands, in order, and names the pages that change. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter. If any line prints `!!`, NOT BUILT or NOT WRITTEN, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, `build_part_e.py` for 16–20, `build_part_f.py` for 21–24, `build_part_g.py` for 25–31, `build_part_h.py` for 32–36, `build_part_i.py` for 37–45) — and a part whose pages use a changed map is rebuilt too — then `linkindex.py`, then `index_generator.py`, **after every part build, since a part build strips the index link `linkindex.py` adds.** End the session with a HANDOFF item (155) and the next START_HERE.
