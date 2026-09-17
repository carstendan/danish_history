Part I: Draft chapter 42

I'm writing a long-form digital history of Denmark, 44 chapters, c. 13,000 BCE to 1953. Parts A–H are shipped, and chapters 37, 38, 39, 40 and 41 are shipped. Part I is chapters 37–44 and it is the last part. PLAN_I.md is agreed. This session drafts chapter 42 and nothing else.

Clone github.com/carstendan/danish_history. From files/, cold run first, reporting what fails rather than working around it:

git status --short
python3 tidy.py
python3 mapfixture.py
python3 seamcheck.py
export DK_CHAPTERS="$PWD/.."
python3 debuild.py verify ../[0-9][0-9]-*.html
python3 bookstats.py
python3 vignettes.py . ; python3 vignettes.py --selftest
python3 figcheck.py
python3 narrative.py ../[34][0-9]-*.html
python3 draftnotes.py ../[0-9][0-9]-*.html
for m in map_*.py ; do python3 "$m" ; done
python3 figs_37.py ; python3 figs_38.py ; python3 figs_39.py ; python3 figs_40.py ; python3 figs_41.py

Expected, as verified on a fresh clone at the end of the chapter 41 session. pip install cairosvg --break-system-packages first or the figure scripts warn. `mapfixture.py` takes several minutes; do not kill it at two.

- **tidy:** clean except Part D's ten unrecoverable figures and the fifteen A–D bodies a fresh clone also lacks. No orphans.
- **mapfixture and seamcheck:** pass.
- **debuild:** style-only for 01–11 and identical for 12–41 (11 and 30 respectively).
- **bookstats:** 41 of 44 built, **299,743 page words, 23.8 h**, 3 remaining of which 1 dense.
- **vignettes:** 78, selftest passes, D-9 balance ok on every tagged chapter.
- **figcheck:** 78 matched, 41 sourceless, 0 stale.
- **narrative:** 37 measures 4L/3M/3H at 4,207; 38 measures 4L/4M/3H at 4,197; 39 measures 3L/4M/3H at 4,082; 40 measures 3L/5M/3H at 4,318; 41 measures **4L/4M/3H at 4,429**.
- **Chapter lengths:** 37 is 7,902 (38 min); 38 is 7,824 (37); 39 is 7,455 (36); 40 is 8,358 (40); 41 is **8,678 (41)**.
- **draftnotes:** 33 notes on pages 25–32 and nothing else. Known (item 102), not a failure.
- **Figure scripts:** maps and figs_37/38/39/40/41 print nothing but their "wrote" lines and leave git status clean.

Anything different: stop and say so. **And if the book total disagrees, the ledger is wrong and not the repository — read item 112 before you go looking.** The 291,154 that three briefs carried was 89 too high because it was obtained by addition instead of being read off `bookstats.py`. The number above was read off a fresh clone.

Then read HANDOFF.md (open items 1–119, conventions D-1 to D-12), PLAN_I.md, and REVIEW-PART-G.md. Items 112–119 and D-12 are new. **116 and 118 will change how you plan this chapter and you should read them before you read PLAN_I §10.** 108 still reaches forward into chapter 44.

Before drafting, work the verification queue in PLAN_I §14 as far as it bears on chapter 42. The plan has flagged vignettes and dates that needed checking in every chapter of Parts H and I and has been right every time. It has also been *wrong* in every chapter of Part I: about a death place, a section title and a premise in 39; about what the 1933 reform did and how many sections the chapter needed in 40; and in 41 about a section title that asserted a duration no source supports, about a figure that could not be built, and about the number of sections again. Expect the same.

**Read item 116 before you accept PLAN_I §10's ten sections.** Two chapters running, the missing subject was a hole in the plan and not thin prose — chapter 40's parliamentary arithmetic, chapter 41's loss of the North Atlantic. The test that finds it is not "does the draft feel short"; it is **which later chapter is left with an event that has no cause in this one**. For chapter 42, ask that question about the Freedom Council, about how the saboteurs were armed, and about Bornholm.

**Chapter 42 opens a subject chapter 41 deliberately did not.** Chapter 41 carries the BBC — first Danish broadcast at 18.30 on 9 April 1940, and listening never banned in Denmark, alone among the occupied countries — and Christmas Møller broadcasting from London from September 1942. It carries no SOE, no parachute drops and no weapons, and says so in its Sources. **That is chapter 42's to open**, and PLAN_I §10 has no section for it either.

Chapter 42's section list and weights are in PLAN_I §10. Measure the draft against that profile BEFORE reading it for quality. A profile with no heavy sections is a defect regardless of word count (item 59).

**Decision 2.7 is live for this chapter and for no other.** Chapter 42 carries the dense flag. If its first draft runs over 8,400 page words the question of splitting it reopens; nothing else reopens it. Note that chapter 41 shipped at 8,678, so 8,400 is reachable and being over it is not automatic.

**And read item 118 before you write the apparatus.** Chapter 41's first build came in at fifty minutes with a narrative only 292 words over chapter 40's; the overrun was almost entirely a Sources block written at 2,046 words against a Part I norm of about 700. Five rounds of sentence-tightening then recovered 274 words in total, which is L1 from the other end. **When a chapter is long, measure the Sources block first and the prose last.**

The build path for Part I exists and chapter 42 needs three things added: a HAND entry in mkbody.py, a CFG entry in build_part_i.py, and figs_42.py. Chapter 41 is the worked example for all three. Then:

python3 figs_42.py
DK_DRAFT=c42_draft.md python3 mkbody.py 42
python3 build_part_i.py
python3 linkindex.py
python3 index_generator.py
python3 narrative.py ../42-*.html
python3 bookstats.py

`linkindex.py` and `index_generator.py` both take the chapter directory from `DK_CHAPTERS` and default to the working directory, so export it before you run them or they will report no chapters found and write the index into the container. Take the chapter's length from bookstats.py after linkindex.py (build_part_i.py prints six words short, every time). Never take it from PLAN_I's model and never from the markdown (item 96, PLAN_I §1.6).

**Check the index blurb at source.** `index_generator.py` carries a one-line blurb and a key list for every chapter in the 44-chapter spine, written before the chapters were. Chapter 41's said "Occupied in six hours", which is false and had been published. Read chapter 42's entry against what you have actually drafted and correct it in `index_generator.py`, not on the page (item 117).

Standing rules:
- Compute numbers, never type them, and treat every "N years later" as a claim (D-8). **A section title is a claim too** (item 117).
- Assert on every scripted replacement, then confirm by whitespace-normalised search, not grep (item 69). **And check that the search proves what you think it proves**: a scripted edit to `mkbody.py` this session deleted 408 lines while a grep for the new entry and a check that the file ended in `}` both passed.
- Predict the symptom before making a change.
- Rasterise and look at every figure. The raster found `fill=` in chapter 40 and "1 hours 45 minutes" in chapter 41, both of which `validate`, `overruns` and `collisions` passed.
- Compute every dimension in a figure script, including canvas height and bar origins.
- **A figure sets text colour with `style=`, never `fill=` (D-11, item 110).**
- **A figure that needs a legend gets swatches, not a list of names under a bar** (item 118). Three segments at one colour and one opacity showed four blocks under six labels until the raster was looked at.
- Place a label by search against the other text boxes, never by reasoning about it (item 76), **and measure the string you are actually going to draw** — chapter 41's first timeline measured the label and drew the label plus its time prefix.
- Read the block before you write the rule that edits it (item 101).
- **Never write draft prose through a shell heredoc (D-12).** `mkbody.py` now refuses a draft containing literal `\uXXXX`, which is the guard that would have caught thirty-six of them shipping in chapter 41.
- Never hand over or commit a generated file: patch of source only, proved against a fresh clone. Save the patch OUTSIDE the repo.
- A draft needs a `# Chapter N — apparatus` heading before the glossary or mkbody.py will not find it. The Summary must be exactly five paragraphs; a sixth is silently dropped under a heading that promises five.

I am not a historian. Historical judgement is yours to make and defend; tell me where you differ from the standard account and why. Flag errors precisely and don't soften them. I do not have opinions on design questions but I can decide if one genuinely needs me; otherwise take the decision and tell me what you took and why. I will read the whole book when it is finished and run consistency reviews then, so conventions you settle mid-book must be written into HANDOFF.md where that pass can overrule them in one place. If you need something from me, say what it blocks. I won't read the prose until the chapter is finished, so don't hold the build waiting on me.

What chapter 42 inherits

**Forward arrows chapter 42 must pay**, from chapter 41:
- The cooperation policy is ratified by the largest turnout in Danish history in March 1943 and is finished by the end of August, and what breaks it is a strike and not an election.
- Horserød, filled with Danes by Danish police, passes into German hands in August 1943 and the men in it go east. The Jews of Denmark, untouched while the occupier judged the cost too high, are next.
- Two Danish voices with a claim to speak for the country, one cooperating in Copenhagen and one in London telling people to stop. Chapter 42 is about who listened to the second, and how they were armed.

**A finding chapter 42 hands on rather than pays.** Chapter 41's largest claim is that the retroactive justice of the *retsopgør* was not forced on Denmark by the liberation: the Rigsdag passed a retroactive criminal statute in August 1941, unanimously, to cover arrests its own police had already made without authority, and the men it covered are the ones sent to Stutthof in October 1943. Chapter 42 carries the Stutthof transport; chapter 43 carries the argument. Don't spend it early.

**Numbers chapter 41 established that chapter 42 will want.** 195 communists arrested by Danish police on 22 June 1941 on a German list of 72 names; 116 still interned on 22 August 1941; about 600 through Horserød; about 90 escaped when the Germans took the camp in August 1943; about 150 to Stutthof in October 1943; 22 dead, being six in the camp, nine on the death marches and seven afterwards. All from lex.dk's *Kommunistinterneringerne under besættelsen, 1941-1945*, which is itemised and good. Roughly 7,000 Danes served in German formations and about 3,300 were sentenced to two to four years afterwards; about 7,500 of the German minority in North Schleswig — some thirty thousand people — were in German front or labour service by 1943.

**Debts from PLAN_I §10.** Read them in the plan; none of them was disturbed this session.

**Verification queue for chapter 42, in order:**
1. **The October 1943 figures.** The plan says around four hundred and seventy deported to Theresienstadt and about seven thousand reaching Sweden, and warns that this is exactly the kind of round number that arrives pre-rounded. Verify both against a named source before either goes into prose or a figure, and if they cannot be double-witnessed, say so in the Sources block rather than rounding.
2. **42[f] Ellen Nielsen · Dragør · October 1943** — verify the camp and the arrest date.
3. **42[n] Kim Malthe-Bruun · Vestre Fængsel · April 1945** — verify the execution date.
4. **42[-] Georg Ferdinand Duckwitz · 28 September 1943** — verify. The plan notes it rests on his own diary, which is a problem to state and not to hide.
5. **The *clearingmord***. PLAN_I §10 says §07 must carry them or the sabotage reads as costless. Get named victims and dates.
6. **The sabotage series by month, 1943–45**, which is a figure the plan calls for and marks "needs source". Frihedsmuseet is named. Decide early whether it is reachable — item 109's rule, applied at the start and not after an afternoon.
7. **Bornholm.** PLAN_I §11 gives chapter 43 "Bornholm under the Soviets", and chapter 42 §10 gives it "4 May 1945 — and Bornholm". Work out which chapter owns the bombing of 7–8 May before you draft either, because 43[n] is an unnamed vignette at Rønne on those two days and it will be easier to place once this is settled.

**Toolchain, carried forward.**
- **`fill=` is dead on classed figure text (item 110, D-11).** Use `style="fill:…"`. Thirty-three shipped figures have the dead attribute and are deliberately not fixed; four of them — `svg_andel_1882`, `svg_crowns`, `svg_deadlock_1873`, `svg_franchises_1866` — ask for near-white text and are probably rendering dark on dark right now.
- **CHAR_W (item 105)** is unchanged and still wrong. Copy `figs_41.py`'s measured-width `fold()`, which is `figs_40.py`'s, which is `figs_39.py`'s. `figs_41.py` also has a `stack()` that places labels in rows by searching against the boxes already placed; reuse it rather than writing a third one.
- **dst.dk (item 119, revising item 109).** The container cannot reach dst.dk at all and the browser will not render the scanned PDFs, but **the `VisPub?cid=` publication page gives a `dst.dk/pubfile/<cid>/<name>` link that fetches**, and that route returned the 1943 election volume and table 1 on page 11 of the 1940 census this session. It is untested on the two unemployment volumes item 109 names. **Try it before anybody goes to a reading room.** And check any fetched table against its own totals: the 1943 volume's OCR gives two party counts that overshoot its own total of valid votes by 5,972.
- **Apparatus is not a constant and it does not only grow.** 3,695 on 37, 3,627 on 38, 3,373 on 39, 4,040 on 40, 4,249 on 41 — and chapter 41's was 5,837 on its first build before the Sources block came back to the Part I norm. Do not predict page length from any of them; build and measure.
- **Markdown estimator.** On chapter 41 the section count with blockquotes stripped read 4,462 against a built narrative of 4,429, 33 over. On chapter 40 it read one under. Good enough for finding a missing subject and not for anything else.
- **Two Meanwhile blocks.** `mw_at` placed them at the third and seventh sections of an eleven-section chapter, as it does for ten.

**Open and needing me. None of these blocks chapter 42.**
- **A session to correct CHAR_W and the thirty-three `fill=` figures together** (items 105, 110), regenerating and re-inspecting every affected figure. `svg_titles.txt` already crosses the canvas edge at measured widths, and four figures may be unreadable.
- A cleanup session for the 33 drafting notes on pages 25–32 (item 102). Five of them are research questions.
- Chapter 37's "twenty years" for Munch, which is eleven (item 103).
- Chapter 38's Still unresolved list, and a figure caption naming figs_38.py (item 103).
- **Chapter 44 §03 has to be rewritten** on item 108: 1953 delegates the poor-relief disqualification to ordinary law rather than abolishing it, and the sentence is in the constitution today.
- **Chapter 41 is 41 minutes**, one over the advisory ceiling of decision 2.1, deliberately. Item 118 names the cut if you want it at 40: delete §07, *The economy of accommodation*, and gloss *værnemager* in chapter 43 instead.
- **The unemployment series** (item 119). If the pubfile route fails on the two named volumes, opening the two PDFs and pasting the annual tables, or attaching the files, unblocks chapter 40's figure gap retrospectively.
- Twice now, source was pushed before its build output was committed. After applying a session's patch, run the build sequence and commit the pages, bodies, SVGs and index in the same push.
