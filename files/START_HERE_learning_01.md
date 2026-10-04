The learning pass, session 1: chapter 01

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built, and the consistency review is closed (twenty-five sessions; the last, item 163, recorded what is left for this pass in REVIEW-CONSISTENCY.md §29.7). I now work through the book chapter by chapter to learn from it, discussing it with Claude. Under **D-21**, each chapter's discussion is recorded on a **study page**, `studies/NN-study.md`; the chapter page changes **only when the discussion finds an error**, and then by the review's rules. I will not fact-check myself or fetch print sources: a claim stands if an online source supports it, otherwise it is hedged to what online sources support or cut for want of one (never for length, D-16).

Clone github.com/carstendan/danish_history. From files/, run only the start check and report what differs rather than working around it:

git status --short
git log -1 --oneline
python3 debuild.py verify ../[0-9][0-9]-*.html

Expected: status clean; the last commit is the one carrying this file and CONVENTIONS D-21 (study pages); debuild 45 identical. Anything different: stop and say so.

Then read CONVENTIONS D-21, D-16 and D-17, and REVIEW-CONSISTENCY §29.7 (nothing listed for 01). Carry three lessons from the review: **a Sources entry is a claim too** — write it from the source, open beside it (item 163); a qualifier has a scope, and "no source found" is a claim about a search (item 162); a correction is a claim that needs a source (item 147).

THIS SESSION:

1. **Chapter 01.** Open page 01 and create `studies/01-study.md` with D-21's sections, empty: Checkpoints, The myth check, What to carry forward, The page in five, Work the material, Parked, Findings. Then:
   - **The four note sections are mine.** I answer the page's checkpoints, write my myth check and my carry-forward, and write my five **from memory before rereading the page's five**. You test each against the page and say plainly where it is thin or wrong. You do not write them for me.
   - **Work the material** is the open discussion. Answer from the page first and say where it says so; where the page is silent or I push past it, say so and look it up online, citing what you read.
   - **Stay on the chapter.** A tangent is fine if it comes back to 01. If it belongs to another chapter, say so, put it under Parked with the chapter it belongs to, and bring us back.
   - Keep the study page current as we go; I should be able to stop at any point and find it up to date.

2. **If the page is wrong.** Stop, say exactly what is wrong and on what online source, and propose the correction: old → new, its Sources entry, and every other place the claim is stated (grep the bodies, drafts, configs, figures). Correct only when I agree. Nothing else on the page changes. **Before touching any source, run the short cold run** (below) and report it. Record the finding under Findings as D-21 says (old → new, source, every other place, the HANDOFF item). Then rebuild Part A–C (`python3 build_parts_abc.py`, `linkindex.py`, `index_generator.py`), run `debuild.py verify`, `narrative.py`, `sweep_arrows.py` and `ordercheck.py` on page 01 at 1200 and 390, look at the changed region in a browser at both widths, and have an agent that has not seen the change check it against its source.

   Short cold run (only when a correction is agreed; with DK_CHAPTERS, DK_OUT and DK_SRC unset, `cairosvg` and Playwright's Chromium installed — in the container `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, or `DK_CHROMIUM=`):

   python3 tidy.py
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

   Expected as after item 163: git status clean after the builds; figcheck --regen changes no `svg_*.txt`; tidy no collisions, orphans or missing figures, 45 bodies; bookstats 45 of 45, 357,661 page words, 28.4 h, none outside the band; figcheck 98 match, 30 sourceless, 0 disagree; narrative OVER 5, kept 5; draftnotes none; every build clean; sweep_glossary 0; sweep_arrows 254 arrows, 216 pass, 38 listed, §7 0; ordercheck all zeros, 128 figures on 45 pages, at 1200 and 390.

3. Save state to the project at intervals (`claude/learning01_state.md`); keep saves small, and ask before deleting anything from the knowledge store.

Delivery: source files only, as one `git format-patch`, never generated pages. I download it to `~/Downloads/`, commit and push. **If the page did not change**, the patch carries `studies/01-study.md` alone, with no HANDOFF item and no build. **If it did**, the patch also carries the corrected sources and pages (in the same commit), and a HANDOFF item (164) naming the study page; the handover ends with the exact shell commands in order, names the pages that change, and builds only when told to, with `linkindex.py` then `index_generator.py` after the part build.

No START_HERE_learning_02: chapter 02 uses this prompt with the chapter number changed, unless session 1 changes the procedure, in which case update this file. After chapter 02 the procedure becomes a skill.
