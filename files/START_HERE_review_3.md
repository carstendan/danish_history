The consistency review, session 3: unblocking chapters 01–15, then Part A read

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built and every page passes every check. This is the third session of the consistency review, which checks whether the book agrees with itself. No new chapters, no repartition.

Clone github.com/carstendan/danish_history. From files/, with DK_CHAPTERS, DK_OUT and DK_SRC unset, run the cold run first and report what fails rather than working around it:

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
python3 sweep_glossary.py ; python3 sweep_names.py ; python3 sweep_facts.py ; python3 sweep_arrows.py

Expected, as run on a fresh clone of the pushed repository after item 140. `mapfixture.py` takes several minutes; do not kill it.

- **tidy:** reports, deletes nothing.
- **mapfixture / seamcheck:** curated panel all correct; SEAM LAYER PASSES.
- **debuild:** 30 identical, 15 style-only, all round-trip. 01–15 are the style-only ones, and that is what this session fixes.
- **bookstats:** 45 of 45, **336,690 page words, 26.7 h**, 0 remaining. Part I 74,233.
- **vignettes:** 89 carry a place, 61 distinct; selftest passes.
- **figcheck:** 87 match, 41 sourceless (A–D, expected), 0 disagree.
- **narrative:** one OVER, 17 §08 *Kalmar, 17 June*, 849. It is known and is not for cutting (D-16).
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** 159 blocks, every one reaches its page. **freshcheck:** 14 fresh (32–45); 25–31 skipped and named.
- **sweep_glossary:** 2 pointer entries, 0 insolvent; same-page double glosses in 03 (twice) and 14.
- **sweep_names:** Schleswig 169 in 26 chapters against Slesvig 104 in 11, none of the 11 in Part I (D-15 has been applied there only).
- **sweep_arrows:** 254 arrows, 37 thread notes; 0 direction faults; 11 D-1 breaks, all on pages 02–17.

Anything different: stop and say so.

Then read HANDOFF items 139 and 140, CONVENTIONS.md (D-13, D-15 and D-16 are now in force) and REVIEW-CONSISTENCY.md §5 and §6.4. Item 138's lesson still governs: **before building a check, run the one the project has; before disputing a claim, read what the chapter already has for it, including its figures and its neighbour.** D-16 governs length: **never propose a cut for the sake of time.** Keep what the story needs. Move material between chapters where that serves the story. Leave what is good.

THIS SESSION:

1. **Unblock 01–15 (decision D-A, agreed).** Run `debuild.py extract` for 01–15, which writes the bodies and prints each SEC config. Part D (12–15) also needs its ten inline SVGs written out as `svg_*.txt`, because `build_part_d.py` expects `e12`–`e15` bodies and external SVGs. A–C keep theirs inline, as `debuild.py`'s docstring decides, since their generators are gone. Write build scripts for A–C from the printed configs in the pattern of `build_part_d.py`, and point `build_part_d.py` at what was recovered. Then rebuild all fifteen, and **`debuild verify` must report every one identical before a single word in them is edited.** Deliver this as one commit that changes no page, before any fix, so the recovery can be checked on its own. Run the whole suite on it.

2. **Then the fifteen A–D findings of REVIEW-CONSISTENCY §5 D-A:**
   - five stale arrows and prose references (04, 06 twice, 07 twice);
   - four Roman regnal numbers (05 twice, 07, 10; D-14);
   - three `<h1>`s that are not their title (05, 06, 07);
   - three same-page glosses (03 twice, 14).

   Also fix the D-1 breaks of §4.3 while the pages are open, each read against its target before it is re-pointed. Commit this separately from step 1.

3. **My three carried items from Part I**, in HANDOFF item 140:
   - 38's Sønderborg arithmetic (2,029 − 349 is 1,680, not 1,672) and its Tønder figure. Open *Statistiske Efterretninger* 1920 nr. 23 first; if it cannot be reached from here, say so and hedge the prose rather than guess.
   - 38 §04's Ribe clause, which is stated as a territorial promise when chapter 19 says that reading is disputed.
   - 42's Sources, which list 43's open questions. Move them to 43.

4. **Then Part A's reading pass**, chapters 01–03. Read for errors of fact, repetition within and across chapters, and drag, against CONVENTIONS.md and the sweeps. Apply D-15 to Part A as you go, and decide there any D-13 vignette that falls in it. Put findings in a new §7 of REVIEW-CONSISTENCY.md. Any decision goes to Carsten one at a time, with a recommendation.

Delivery as always: source files only, as `git format-patch` or whole files, never generated pages. After step 1:
- For 01–15, the recovered `cNN_body.html` (or `eNN_body.html`) is the authored source and may be edited, as for 16–24.
- For 25–45, `cNN_body.html` is generated.

Carsten commits, builds and pushes. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed chapter. If any line prints `!!`, stop: the part build would wrap the old body and still report `part ok`. Then the parts, then `linkindex.py`, then `index_generator.py`. End the session with a HANDOFF item and the next START_HERE.
