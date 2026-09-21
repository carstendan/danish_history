The consistency review, session 6: 08's and 10's missing tags, then Part D read

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built. This is the sixth session of the consistency review, which checks whether the book agrees with itself. No new chapters, no repartition.

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

Expected, as run after item 143's rebuild. `mapfixture.py` takes a few minutes; do not kill it.

- **git log:** the commit carrying item 143's patch **must carry its rebuilt pages** (06, 08–14, 19, 20, 24). If debuild reports BODY DRIFT on exactly those, the pages were not pushed — item 143's first cold run; stop and say so.
- **tidy:** reports, deletes nothing. No collisions, no orphans, no missing figures; all 45 bodies present.
- **mapfixture / seamcheck:** curated panel all correct; FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **337,491 page words, 26.8 h**. Part A 21,397; Part B 26,326; Part C 25,619; Part D 30,990; Part I 74,403.
- **vignettes:** **134 carry a place, 102 distinct**; selftest passes. Balance: 01, 03, 04, 05 "[f] part"; **D-9 FAILURES: 08 and 10** (R-4, R-5); 12 onwards untagged.
- **figcheck:** 98 match, 30 sourceless, 0 disagree.
- **narrative:** one OVER, 17 §08 *Kalmar, 17 June*, 849. Known; not for cutting (D-16).
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** 159 blocks. **freshcheck:** 14 fresh (32–45).
- **sweep_glossary:** 2 pointer entries, 0 insolvent; no same-page double glosses.
- **sweep_names:** Schleswig 169 in 26 chapters against Slesvig 104 in 11.
- **sweep_facts:** 5 rows to read.
- **sweep_arrows:** 254 arrows, 37 thread notes. Form 7; direction 0; D-1 0; quoted titles 0; solvency 40 listed; prose references 0; footers 0; `<h1>` 0; 9b 0.

Anything different: stop and say so.

Then read HANDOFF items 142 and 143, CONVENTIONS.md and REVIEW-CONSISTENCY.md §9. Item 143's lesson: **a decision records what was agreed, not what is true — the facts it rests on are checked again when it is carried out** (R-3's "c. 200 CE" and "ladle and strainer" were both wrong). Item 142's still governs: before trusting a 0, find one case by hand the check should have caught. Item 141's: read the ledger before carrying out a START_HERE. D-16: never propose a cut for the sake of time.

01–24 are authored bodies (`cNN_body.html`; edit it). 25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py`. **For 01–11, `build_parts_abc.py` re-inserts every checkpoint from its own config: change a checkpoint there as well as in the body.**

THIS SESSION:

1. **R-4 and R-5, as Carsten answered them (REVIEW-CONSISTENCY §9.9).** If as recommended: (a) **Ragnhild at Glavendrup** in 08 §04 *What they believed* — `[f]`; the stone, the ship setting, Alle the *goði*, Thor, the curse; first half of the tenth century. (b) **The garrison's dead at Trelleborg** in 10 §08 *Who lived in them* — `[n]`; the cemetery, the mass graves, the strontium results (Price, Frei et al., *Antiquity* 85, 2011). Source every detail before writing it, and check the recommendation's own facts first. Who-lines person · place · date · tag. D-13 applies. Then `vignettes.py` should report no D-9 failure in Parts A–C.

2. **Part D's reading pass, chapters 12–15.** Errors of fact, repetition within and across chapters (including back into 11: 11 → 12 promises Sweyn Estridsen's dioceses, a written church law and a saint), and drag, against CONVENTIONS.md and the sweeps. **Compute every interval (D-8)**: Part C had nine wrong. Known for Part D: **14's Jyske Lov vignette** reads the law at "the Viborg assembly" and says "a hundred and sixty chapters" — the law was given at Vordingborg in March 1241; check both. **12 gives Sweyn Estridsen 1047–1074**; 11 now follows it — confirm. Apply D-15 (Part D is where Schleswig and Slesvig first meet in number: 12 has 9 and 3, 14 has 12); decide any D-13 vignette. D-9 backfill is due: tag Part D. Measure Recall as §8.5 and §9.5 did (Jaccard of content words ≥ 0.4). Put findings in a new §10 of REVIEW-CONSISTENCY.md. Any decision goes to Carsten one at a time, with a recommendation.

3. **Cheap, while Part D is open.** `build_part_d.py` has no padded-chapter guard (only `build_parts_abc.py` does, §9.6); give it the same one, and show it firing on a planted case before trusting it.

4. **Before handing over, have an agent that has not seen the work check every hunk** against sources and against the rest of the book. In sessions 3, 4 and 5 it found ten, eight and seven slips in the fixes themselves.

Delivery as always: source files only, as `git format-patch` or whole files, never generated pages.

Carsten commits, builds and pushes, **pages in the same commit as the sources**. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter (`DK_DRAFT=cNN_draft.md python3 mkbody.py NN` for 32–45). If any line prints `!!`, stop. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, and so on), then `linkindex.py`, then `index_generator.py` — **after every part build, since a part build strips the index link `linkindex.py` adds.** End the session with a HANDOFF item and the next START_HERE.
