Part I: Draft chapter 41

I'm writing a long-form digital history of Denmark, 44 chapters, c. 13,000 BCE to 1953. Parts A–H are shipped, and chapters 37, 38, 39 and 40 are shipped. Part I is chapters 37–44 and it is the last part. PLAN_I.md is agreed. This session drafts chapter 41 and nothing else.

Clone github.com/carstendan/danish_history. From files/, cold run first, reporting what fails rather than working around it:

git status --short
python3 tidy.py
python3 mapfixture.py
python3 seamcheck.py
python3 debuild.py verify ../[0-9][0-9]-*.html
python3 bookstats.py
python3 vignettes.py . ; python3 vignettes.py --selftest
python3 figcheck.py
python3 narrative.py ../[34][0-9]-*.html
python3 draftnotes.py ../[0-9][0-9]-*.html
for m in map_*.py ; do python3 "$m" ; done
python3 figs_37.py ; python3 figs_38.py ; python3 figs_39.py ; python3 figs_40.py

Expected, as verified on a fresh clone at the end of the chapter 40 session. pip install cairosvg first or the figure scripts warn.

- **tidy:** clean except Part D's ten unrecoverable figures and the fifteen A–D bodies a fresh clone also lacks. No orphans.
- **mapfixture and seamcheck:** pass.
- **debuild:** style-only for 01–11 and identical for 12–40 (11 and 29 respectively).
- **bookstats:** 40 of 44 built, 291,154 page words, 23.1 h, 4 remaining of which 1 dense.
- **vignettes:** 75, selftest passes.
- **figcheck:** 75 matched, 41 sourceless, 0 stale.
- **narrative:** 37 measures 4L/3M/3H at 4,207; 38 measures 4L/4M/3H at **4,197**; 39 measures 3L/4M/3H at 4,082; 40 measures 3L/5M/3H at 4,318.
- **Chapter lengths:** 37 is 7,902 (38 min); 38 is 7,824 (37); 39 is 7,455 (36); 40 is 8,358 (40).
- **draftnotes:** 33 notes on pages 25–32 and nothing else. Known (item 102), not a failure.
- **Figure scripts:** maps and figs_37/38/39/40 print nothing but their "wrote" lines and leave git status clean.

Anything different: stop and say so. Note that chapter 38's narrative is 4,197 and not the 4,194 earlier briefs gave — that was corrected this session, item 107, and PLAN_I §6 now agrees.

Then read HANDOFF.md (open items 1–111, conventions D-1 to D-11), PLAN_I.md, and REVIEW-PART-G.md. Items 107–111 are new. 109 and 110 are toolchain faults you will hit again if you do not read them; 108 reaches forward into chapter 44 and you should read it even though it is not your chapter.

Before drafting, work the verification queue in PLAN_I §14 as far as it bears on chapter 41. The plan has flagged vignettes and dates that needed checking in every chapter of Parts H and I and has been right every time; in chapter 39 it was wrong about a death place, a section title and a premise, and in chapter 40 it was wrong about what the 1933 reform did and about how many sections the chapter needed. Expect the same.

Chapter 41's section list and weights are in PLAN_I §9. Measure the draft against that profile BEFORE reading it for quality. A profile with no heavy sections is a defect regardless of word count (item 59). A draft that lands short is missing a subject, not thin paragraphs. This has now held for eight consecutive chapters (items 72, 83, 106, 111), so treat it as a rule, and ask which subject is absent rather than thickening the paragraphs you have. In chapter 40 the absent subject was the parliamentary arithmetic, and the chapter could not explain its own ending without it.

The build path for Part I exists and chapter 41 needs three things added: a HAND entry in mkbody.py, a CFG entry in build_part_i.py, and figs_41.py. Chapter 40 is the worked example for all three. Then:

python3 figs_41.py
DK_DRAFT=c41_draft.md python3 mkbody.py 41
python3 build_part_i.py
python3 linkindex.py
python3 index_generator.py
python3 narrative.py ../41-*.html
python3 bookstats.py

Take the chapter's length from bookstats.py after linkindex.py (build_part_i.py prints six words short, every time). Never take it from PLAN_I's model and never from the markdown (item 96, PLAN_I §1.6).

Standing rules:
- Compute numbers, never type them, and treat every "N years later" as a claim (D-8).
- Assert on every scripted replacement, then confirm by whitespace-normalised search, not grep (item 69).
- Predict the symptom before making a change.
- Rasterise and look at every figure. The raster found the fill= fault in chapter 40 that every guard passed (items 47, 105, 110).
- Compute every dimension in a figure script, including canvas height and bar origins. Chapter 40 typed two canvas heights and an assertion caught one of them.
- **A figure sets text colour with `style=`, never `fill=` (D-11, item 110).**
- Place a label by search against the other text boxes, never by reasoning about it (item 76).
- Read the block before you write the rule that edits it (item 101).
- Never hand over or commit a generated file: patch of source only, proved against a fresh clone. Save the patch OUTSIDE the repo.
- A draft needs a `# Chapter N — apparatus` heading before the glossary or mkbody.py will not find it. The Summary must be exactly five paragraphs; a sixth is silently dropped under a heading that promises five.

I am not a historian. Historical judgement is yours to make and defend; tell me where you differ from the standard account and why. Flag errors precisely and don't soften them. I do not have opinions on design questions but I can decide if one genuinely needs me; otherwise take the decision and tell me what you took and why. I will read the whole book when it is finished and run consistency reviews then, so conventions you settle mid-book must be written into HANDOFF.md where that pass can overrule them in one place. If you need something from me, say what it blocks. I won't read the prose until the chapter is finished, so don't hold the build waiting on me.

What chapter 41 inherits

**Forward arrows chapter 41 must pay**, from chapter 40:
- The minority nazified in 1933 has an army on its side of the argument on 9 April 1940, and the Danish state that would not ban its party has to decide what to do about its members.
- Munch's foreign policy, eleven years old by 1940, meets the thing it was designed to avoid.

And from chapter 38:
- On 9 April 1940 the border drawn by asking is crossed by an army that did not ask, and both minorities have to decide what they are for.

And from chapter 39:
- Munch's argument that Denmark could not fight is tested on 9 April 1940.

**A correction chapter 41 must not repeat.** Chapter 37 says Munch "would hold the foreign ministry for twenty years". He held it from 30 April 1929 to 8 July 1940, **eleven years** (item 103, still unfixed on the page). Chapter 40 says eleven. Do not inherit the twenty.

**Debts from PLAN_I §9.** Read them in the plan; none of them was disturbed this session.

**Verification queue for chapter 41, in order:**
1. **The sixteen dead of 9 April**, and the roster entry 41[n] — one of them at Bredevad or Lundtoftbjerg. The plan says verify name, place and total, and the total is the part of it I would least trust.
2. **What Scavenius signed in Berlin in November 1941** (41[-]), which the plan says to verify because the standard account compresses it.
3. **41[f] needs a subject and has none.** It is one of the six the plan flagged, and it is the only Part I vignette still unsubjected apart from 43[n], 44[f] and 44[-]. Chapter 40's 40[f] was solved by looking for the person in the room who was not a politician — Augusta Erichsen, whose 1967 memoir is the only account of the Kanslergade night, because no minute was taken. The same move may work here: for 1940–42 the obvious candidates are the people who kept records nobody asked them to keep.
4. **The election of 23 March 1943** — turnout and what the Nazi party got — is figure 3 of chapter 41 in PLAN_I §13 and is the chapter's best data figure. Danish election volumes fetch from dst.dk when a search surfaces them; the 1939 one did this session. The election tables sit in the FRONT of those volumes, inside the fetch tool's reach, unlike the deeper tables that defeated the unemployment series.

**Leads already gathered, each still needing its second witness where one is not given.**
- **Munch** was foreign minister from 30 April 1929 to 8 July 1940 (lex.dk; Wikipedia; and chapter 40 uses it).
- **The German minority** was nazified through 1933; the Slesvigsk Parti was taken over by its own National Socialists that year and became a foreign branch of the NSDAP in 1935; it held one Folketing seat throughout, 12,617 votes in 1935 and 15,016 in 1939 (danmarkshistorien.dk; lex.dk on the elections).
- **The DNSAP** took 1,028 votes in 1932, 16,257 and no seats in 1935, and 31,032 and three seats in 1939, with about five thousand members at the outbreak of war (lex.dk; danmarkshistorien.dk). Frits Clausen led it from a coup in July 1933 until his party expelled him in November 1944; he was arrested at the liberation and died in prison on 5 December 1947 (Grænseforeningen).
- **The 1939 Folketing election** was on 3 April: electorate 2,159,356, turnout 79.2 per cent (lex.dk).

**Toolchain, from the chapter 40 session.**
- **`fill=` is dead on classed figure text (item 110, D-11).** Use `style="fill:…"`. Thirty-three shipped figures have the dead attribute and are deliberately not fixed; four of them — `svg_andel_1882`, `svg_crowns`, `svg_deadlock_1873`, `svg_franchises_1866` — ask for near-white text and are probably rendering dark on dark right now.
- **CHAR_W (item 105)** is unchanged and still wrong. Copy `figs_40.py`'s measured-width `fold()`, which is `figs_39.py`'s.
- **dst.dk (item 109).** Volumes surfaced by search fetch fine; the fetch truncates them around page 34. The container cannot reach dst.dk at all. The browser pane will not render the scanned PDFs. Plan any figure that needs a deep table as unbuildable from this end, at the start.
- **Apparatus is not a constant, and it is growing.** 3,695 on 37, 3,627 on 38, 3,373 on 39, 4,040 on 40. The last is `outside` — an eleventh section and the longest Sources block in the book. Do not predict page length from any of them.
- **Markdown estimator.** On chapter 40 the section count with blockquotes and em-dashes stripped read one word under the built narrative, 4,317 against 4,318. On chapter 39 it read 73 under. Good enough for finding a missing subject and not for anything else.
- **Two Meanwhile blocks.** `mw_at` placed them at the third and seventh sections of an eleven-section chapter, as it does for ten.

**Open and needing me. None of these blocks chapter 41.**
- **A session to correct CHAR_W and the thirty-three `fill=` figures together** (items 105, 110), regenerating and re-inspecting every affected figure. `svg_titles.txt` already crosses the canvas edge at measured widths, and four figures may be unreadable.
- A cleanup session for the 33 drafting notes on pages 25–32 (item 102). Five of them are research questions.
- Chapter 37's "twenty years" (item 103).
- Chapter 38's Still unresolved list, and a figure caption naming figs_38.py (item 103).
- **Chapter 44 §03 has to be rewritten** on item 108: 1953 delegates the poor-relief disqualification to ordinary law rather than abolishing it, and the sentence is in the constitution today.
- **The unemployment series** (item 109). Both volumes are named. If you can open the two PDFs and paste the annual tables, or attach the files, chapter 41 or a later session can draw the depression properly and chapter 40's figure gap can be filled retrospectively.
- Twice now, source was pushed before its build output was committed. After applying a session's patch, run the build sequence and commit the pages, bodies, SVGs and index in the same push.
