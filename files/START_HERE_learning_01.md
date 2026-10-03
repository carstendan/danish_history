The learning pass, session 1: chapter 01, and how an addendum works

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built, and the consistency review is closed (twenty-five sessions; the last, item 163, settled its open lists online and recorded what is left for this pass in REVIEW-CONSISTENCY.md §29.7). I now work through the book chapter by chapter to learn from it, using its questions and discussing them with Claude. Under **D-21**, each chapter's discussion is summarised on a **separate addendum page**; the chapter page changes **only when the discussion finds an error**, and then by the review's rules. I will not fact-check myself or fetch print sources: a claim stands if an online source supports it, otherwise it is hedged to what online sources support or cut for want of one (never for length, D-16).

Clone github.com/carstendan/danish_history. From files/, with DK_CHAPTERS, DK_OUT and DK_SRC unset, `cairosvg` installed (`pip install cairosvg`) and Playwright with a Chromium for `ordercheck.py` (in the container: `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, found by the tool itself, or `DK_CHROMIUM=`), run the short cold run and report what fails rather than working around it:

git status --short
python3 tidy.py
python3 debuild.py verify ../[0-9][0-9]-*.html
python3 bookstats.py
python3 figcheck.py --regen
python3 narrative.py ../[0-9][0-9]-*.html
python3 draftnotes.py ../[0-9][0-9]-*.html
python3 build_parts_abc.py ; python3 build_part_d.py ; python3 build_part_e.py ; python3 build_part_f.py
python3 build_part_g.py ; python3 build_part_h.py ; python3 build_part_i.py
python3 linkindex.py ; python3 index_generator.py
python3 sweep_glossary.py ; python3 sweep_arrows.py
python3 ordercheck.py ../[0-9][0-9]-*.html | tail -1
python3 ordercheck.py --width 390 ../[0-9][0-9]-*.html | tail -1

Expected, as run after item 163:

- **git log:** the commit carrying item 163's patch must carry pages 01–10 and 12–15 with their bodies `c01_body.html` … `c10_body.html`, `c12_body.html` … `c15_body.html`, and `CONVENTIONS.md`, `HANDOFF.md`, `REVIEW-CONSISTENCY.md` and this file — 32 files, in one commit. No figure and not the index.
- **git status** clean after the builds and the two index scripts; `figcheck --regen` changes no `svg_*.txt` (if one changes, a generator was edited and never run: stop and say so).
- **tidy:** no collisions, orphans or missing figures; 45 bodies. **debuild:** 45 identical.
- **bookstats:** 45 of 45, **357,661 page words, 28.4 h**; A 22,950; B 27,455; C 27,898; D 34,094; E 36,953; F 30,481; G 54,240; H 43,467; I 80,123; "outside the 25-50 minute band …: none".
- **figcheck:** 98 match, 30 sourceless, 0 disagree, 0 warning lines. **narrative:** "OVER: 5, of which kept (D-16): 5, not kept: 0". **draftnotes:** none in 45.
- **builds:** every part "all … built clean", every chapter line "braces 0 | placeholders 0 | anchors ok | tags ok", no `!` or `!!` line.
- **sweep_glossary:** 0 same-page double glosses. **sweep_arrows:** 254 arrows, 216 pass, 38 listed; §7 (prose references) 0.
- **ordercheck:** all zeros, 128 figures on 45 pages, at 1200 and at 390.

The full cold run of START_HERE_review_25 (mapfixture, seamcheck, vignettes, appcheck, freshcheck, sweep_names, sweep_facts, linecheck, the question and width measures in `claude/`) is for every few chapters, not every session. Anything different: stop and say so.

Then read CONVENTIONS D-21 (new), D-16 and D-17, HANDOFF item 163, and REVIEW-CONSISTENCY §29.7. Item 163's lesson: **a Sources entry is a claim too — write it from the source, open beside it, and check it as you would the sentence it grounds.** Item 162's: a qualifier has a scope; "no source found" is a claim about a search. Item 147's: a correction is a claim that needs a source.

THIS SESSION:

1. **Settle with me, before anything else, D-21's open questions** — ask, one at a time, each with a recommendation: what the addendum page is (file name, source format — a hand-authored `aNN_addendum.html`, a markdown source built to a page, or an artifact outside the repo), how it is built and styled, whether anything links to it (a link from the chapter page changes the page; the index may be the better place), and how an addendum records a correction it caused. Then write D-21's answers into CONVENTIONS.md.

2. **Chapter 01.** I read the page and bring questions; we discuss. Answer from the page first and say where it says so; where the page is silent or I push past it, say so and look it up online, citing what you read. When the discussion shows the page is **wrong**, stop, say exactly what is wrong and on what online source, and propose the correction (old → new, with its Sources entry, and every other place the claim is stated — grep the bodies, drafts, configs, figures). Correct only when I agree. Nothing else on the page changes. REVIEW-CONSISTENCY §29.7 lists nothing for 01; later chapters have items waiting there.

3. **The addendum for 01**: a summary of what we discussed, what I took from it, and any correction, written to the format settled in task 1.

4. If the page changed: rebuild Part A–C (`python3 build_parts_abc.py`, then `linkindex.py`, `index_generator.py`), run `debuild.py verify`, `narrative.py`, `sweep_arrows.py` and `ordercheck.py` on page 01 at 1200 and 390, and look at any changed region in a browser at both widths. Have an agent that has not seen the change check it against its source before handing over.

5. Save state to the project at intervals (`claude/learning01_state.md`); keep saves small, and ask before deleting anything from the knowledge store.

Delivery as always: source files only, as one `git format-patch`, never generated pages (01–24's bodies are sources). I download it to `~/Downloads/`, commit, build and push, **pages in the same commit as the sources**, and **build only when told to**: the handover ends with the exact shell commands, in order, names the pages that change, and if a part build runs, `linkindex.py` then `index_generator.py` after it. End with a HANDOFF item (164) and the next START_HERE.
