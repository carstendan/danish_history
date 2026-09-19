The consistency review, session 4: Part B read

I'm writing a long-form digital history of Denmark: 45 chapters, c. 13,000 BCE to 1953. Every chapter is built and every page passes every check. This is the fourth session of the consistency review, which checks whether the book agrees with itself. No new chapters, no repartition.

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

Expected, as run after item 141's rebuild. `mapfixture.py` takes several minutes; do not kill it.

- **tidy:** reports, deletes nothing. No collisions, no orphans, **no missing figures**; all 45 bodies present.
- **mapfixture / seamcheck:** curated panel all correct; FIXTURE PASSES; SEAM LAYER PASSES.
- **debuild:** **45 identical**, all round-trip.
- **bookstats:** 45 of 45, **336,699 page words, 26.7 h**, 0 remaining. Part A 21,392; Part B 25,666; Part I 74,403.
- **vignettes:** 114 carry a place, 84 distinct; selftest passes. (It reads bodies, so 01–15 count now.)
- **figcheck:** 98 match, 30 sourceless (A–C, expected), 0 disagree.
- **narrative:** one OVER, 17 §08 *Kalmar, 17 June*, 849. Known; not for cutting (D-16).
- **draftnotes:** none in 45 pages, none in 14 drafts.
- **appcheck:** 159 blocks, every one reaches its page. **freshcheck:** 14 fresh (32–45); 25–31 skipped and named.
- **sweep_glossary:** 2 pointer entries, 0 insolvent; **no same-page double glosses**.
- **sweep_names:** Schleswig 170 in 26 chapters against Slesvig 104 in 11 (12, 19, 26–29, 31–34, 36); none in Parts A–C or I.
- **sweep_facts:** 5 rows to read, as before.
- **sweep_arrows:** 254 arrows, 37 thread notes. Form 7 (all mixed or two-letter forms, all parsed); direction 0; **D-1 0**; quoted titles 0; solvency 40 listed for reading; prose references 0; footers 0; `<h1>` 0; **9b (`<title>` number) 0**.

Anything different: stop and say so.

Then read HANDOFF item 141, CONVENTIONS.md (D-13 to D-16 in force; D-14 still marked proposed and fully applied), and REVIEW-CONSISTENCY.md §7. Item 141's lesson: **a START_HERE is a plan made before the session; read the ledger it points at before carrying it out.** Item 138's still governs: **before building a check, run the one the project has; before disputing a claim, read what the chapter already has for it, including its figures and its neighbour.** D-16 governs length: **never propose a cut for the sake of time.**

Since item 141, **01–24 are authored bodies** (`cNN_body.html` is the source; edit it). 25–31 come from `PART_G_DRAFT.md`, 32–45 from `cNN_draft.md`, through `mkbody.py`.

THIS SESSION:

1. **R-1, if Carsten has not answered it** (REVIEW-CONSISTENCY §7.9): D-9 tags and L9a who-lines in chapters whose evidence names no one. Put it once, with its recommendation. If answered, apply it to Part A before anything else, as its own commit.

2. **Part B's reading pass, chapters 04–07.** Read for errors of fact, repetition within and across chapters (including back into Part A: 04 repeats several of 03's lines), and drag, against CONVENTIONS.md and the sweeps. Check every date arithmetic and every "N years later" (D-8) by computing it; Part A had twenty-six factual errors and most were intervals. Apply D-15 to Part B as you go (Schleswig appears in 06 and 07), and decide any D-13 vignette that falls in it (none of the seven named cases does). Chapter 07's Recall repeats all five of its checkpoints; decide whether that is the book's pattern or a fault. Put findings in a new §8 of REVIEW-CONSISTENCY.md. Any decision goes to Carsten one at a time, with a recommendation.

3. **Before handing over, have an agent that has not seen the work check every hunk** against sources and against the rest of the book. In session 3 it found ten slips in the fixes themselves.

Delivery as always: source files only, as `git format-patch` or whole files, never generated pages.

Carsten commits, builds and pushes. **Rebuild order is the fix, not a convention:** figure scripts that changed first, then `mkbody.py` for each changed generated chapter (`DK_DRAFT=cNN_draft.md python3 mkbody.py NN` for 32–45). If any line prints `!!`, stop: the part build would wrap the old body and still report `part ok`. Then the parts (`build_parts_abc.py` for 01–11, `build_part_d.py` for 12–15, and so on), then `linkindex.py`, then `index_generator.py`. End the session with a HANDOFF item and the next START_HERE.
