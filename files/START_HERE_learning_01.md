The learning pass: chapter NN

(Session 1 was chapter 01, item 164. For each later chapter, use this prompt with NN set to the chapter's two-digit number.)

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built, and the consistency review is closed (twenty-five sessions; the last, item 163, recorded what is left for this pass in REVIEW-CONSISTENCY.md §29.7). I now work through the book chapter by chapter to learn from it, discussing it with Claude. Under **D-21**, each chapter's discussion is recorded on a **study page**, `studies/NN-study.md` at the repository root; the chapter page changes **only when the discussion finds an error**, and then by the review's rules. I will not fact-check myself or fetch print sources: a claim stands if an online source supports it, otherwise it is hedged to what online sources support or cut for want of one (never for length, D-16).

Clone github.com/carstendan/danish_history. From files/, run only the start check and report what differs rather than working around it:

git status --short
git log -1 --oneline
python3 debuild.py verify ../[0-9][0-9]-*.html

Expected: status clean; the last commit is the previous chapter's study page (and its HANDOFF item if that chapter changed); debuild 45 identical. Anything different: stop and say so.

Then read CONVENTIONS D-21 (as amended 4 October 2026), D-16 and D-17, and REVIEW-CONSISTENCY §29.7 for what it lists for chapter NN; anything listed is taken up first under Work the material. Carry four lessons: **a Sources entry is a claim too**, so write it from the source, open beside it (item 163); a qualifier has a scope, and "no source found" is a claim about a search (item 162); a correction is a claim that needs a source (item 147); **read the fix against the source as closely as the error**, because a correction for scope needs its own scope checked (item 164).

THIS SESSION:

1. **Chapter NN.** Open page NN and create `studies/NN-study.md` in the clone (the repository root, beside the chapter pages), with D-21's sections, empty: Checkpoints, Work the material, Parked, Findings. Then:
   - **Checkpoints, lightly.** I answer the page's checkpoints. For each, you say briefly whether it is right or wrong, and name the one thing missing and the section that says it. You do not write my answers for me. Keep it short: the time goes to the next part.
   - **Work the material** is a dialogue and the main part of the session; the aim is that I retain it, not speed. Talk as a teacher would: two to four sentences, one point at a time, and ask back ("we know X, so would you not call it Y?", "what would follow from that?"). Raise the most important problem in an answer first, not all of them. Offer new material as a hook, not unasked. Use the page's end questions as starting points, not a form. Answer from the page first and say where it says so; where the page is silent or I push past it, say so and look it up online, citing what you read. Your points may change as we talk, and you may be the one who is wrong.
   - **The study page records a summary**, not the conversation: where each thread ended (what was settled, what changed, what stays open), with section references and sources. The depth goes there, not into the chat.
   - **Stay on the chapter.** A tangent is fine if it comes back to NN. If it belongs to another chapter, say so, put it under Parked with the chapter it belongs to, and bring us back.
   - Keep the study page current as we go; I should be able to stop at any point and find it up to date.

2. **If the page is wrong.** Stop, say exactly what is wrong and on what online source, and propose the correction: old → new, its Sources entry, and every other place the claim is stated (grep the bodies, drafts, configs, figures). Correct only when I agree. Nothing else on the page changes. **Before touching any source, run the short cold run** (below) and report it. Record the finding under Findings as D-21 says (old → new, source, every other place, the HANDOFF item). Then rebuild the chapter's part (the part build, then `linkindex.py`, then `index_generator.py`), run `debuild.py verify`, `narrative.py`, `sweep_arrows.py` and `ordercheck.py` on page NN at 1200 and 390, look at the changed region in a browser at both widths, and have an agent that has not seen the change check it against its source. If that agent queries text the correction did not touch, record it under Work the material as an open question and do not act on it.

   Short cold run (only when a correction is agreed; with DK_CHAPTERS, DK_OUT and DK_SRC unset, `cairosvg` and Playwright installed (`pip install --break-system-packages cairosvg playwright`), and Playwright's Chromium (in the container `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, or `DK_CHROMIUM=`):

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

   Expected as after item 164 (or after the latest chapter that changed the book; its HANDOFF item gives the words): git status clean after the builds; figcheck --regen changes no `svg_*.txt`; tidy no collisions, orphans or missing figures, 45 bodies; bookstats 45 of 45, 357,674 page words, 28.4 h, none outside the band; figcheck 98 match, 30 sourceless, 0 disagree; narrative OVER 5, kept 5; draftnotes none; every build clean; sweep_glossary 0; sweep_arrows 254 arrows, 216 pass, 38 listed, §7 0; ordercheck all zeros, 128 figures on 45 pages, at 1200 and 390.

3. Save state to the project at intervals (`claude/learningNN_state.md`, and a `claude/learningNN_wip.patch` once anything is changed); keep saves small, and ask before deleting anything from the knowledge store.

Delivery: source files only, as one `git format-patch`, never generated pages. I download it to `~/Downloads/`, commit and push. **If the page did not change**, the patch carries `studies/NN-study.md` alone, with no HANDOFF item and no build. **If it did**, the patch also carries the corrected sources and pages (in the same commit), and the next HANDOFF item naming the study page; the handover ends with the exact shell commands in order, names the pages that change, and builds only when told to, with `linkindex.py` then `index_generator.py` after the part build.

Chapter 01 changed this procedure (item 164: the myth check, carry-forward and five are dropped; checkpoints are tested lightly). After chapter 02 the procedure becomes a skill.
