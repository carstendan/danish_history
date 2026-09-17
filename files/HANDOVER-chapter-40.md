Part I: Draft chapter 40

I'm writing a long-form digital history of Denmark, 44 chapters, c. 13,000 BCE to 1953. Parts A–H are shipped, and chapters 37, 38 and 39 are shipped. Part I is chapters 37–44 and it is the last part. PLAN_I.md is agreed. This session drafts chapter 40 and nothing else.

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
python3 narrative.py ../3[8-9]-*.html
python3 draftnotes.py ../[0-9][0-9]-*.html
for m in map_*.py ; do python3 "$m" ; done
python3 figs_37.py ; python3 figs_38.py ; python3 figs_39.py

Expected, as verified on a fresh clone of 9a820e4 at the end of the chapter 39 session. pip install cairosvg first or the figure scripts warn.

- **tidy:** clean except Part D's ten unrecoverable figures and the fifteen A–D bodies a fresh clone also lacks. No orphans.
- **mapfixture and seamcheck:** pass.
- **debuild:** style-only for 01–11 and identical for 12–39 (11 and 28 respectively).
- **bookstats:** 39 of 44 built, 282,707 page words, 22.4 h, 5 remaining of which 1 dense.
- **vignettes:** 72, selftest passes.
- **figcheck:** 72 matched, 41 sourceless, 0 stale.
- **narrative:** chapter 38 measures 4L/4M/3H at 4,194; chapter 39 measures 3L/4M/3H at 4,082.
- **Chapter lengths:** chapter 38 is 7,824 page words (37 min); chapter 39 is 7,455 (36 min).
- **draftnotes:** reports 33 notes on pages 25–32 and nothing else. That is known (item 102), not a failure.
- **Figure scripts:** maps and figs_37/38/39 print nothing but their "wrote" lines and leave git status clean.

Anything different: stop and say so.

Then read HANDOFF.md (open items 1–106, conventions D-1 to D-10), PLAN_I.md, and REVIEW-PART-G.md. Items 102–106 are new. 102 and 105 are toolchain faults you will hit again if you do not read them.

Before drafting, work the verification queue in PLAN_I §14 as far as it bears on chapter 40. The plan has flagged vignettes and dates that needed checking in every chapter of Parts H and I and has been right every time; in chapter 39 it was wrong about a death place, a section title and a premise. Expect the same.

Chapter 40's section list and weights are in PLAN_I §8. Measure the draft against that profile BEFORE reading it for quality. A profile with no heavy sections is a defect regardless of word count (item 59). A draft that lands short is missing a subject, not thin paragraphs. This has now held for seven consecutive chapters (items 72, 83, 106), so treat it as a rule and ask which subject is absent.

The build path for Part I exists and chapter 40 needs three things added: a HAND entry in mkbody.py, a CFG entry in build_part_i.py, and figs_40.py. Chapter 39 is the worked example for all three. Then:

python3 figs_40.py
DK_DRAFT=c40_draft.md python3 mkbody.py 40
python3 build_part_i.py
python3 linkindex.py
python3 index_generator.py
python3 narrative.py ../40-*.html
python3 bookstats.py

Take the chapter's length from bookstats.py after linkindex.py (build_part_i.py prints six words short, every time). Never take it from PLAN_I's model and never from the markdown (item 96, PLAN_I §1.6).

Standing rules:
- Compute numbers, never type them, and treat every "N years later" as a claim (D-8).
- Assert on every scripted replacement, then confirm by whitespace-normalised search, not grep (item 69).
- Predict the symptom before making a change.
- Rasterise and look at every figure. The raster found two faults in chapter 39 that every guard passed (items 47, 105).
- Compute every dimension in a figure script, including canvas height and bar origins.
- Place a label by search against the other text boxes, never by reasoning about it (item 76).
- Read the block before you write the rule that edits it (item 101).
- Never hand over or commit a generated file: patch of source only, proved against a fresh clone. Save the patch OUTSIDE the repo.

I am not a historian. Historical judgement is yours to make and defend; tell me where you differ from the standard account and why. Flag errors precisely and don't soften them. I do not have opinions on design questions but I can decide if one genuinely needs me; otherwise take the decision and tell me what you took and why. I will read the whole book when it is finished and run consistency reviews then, so conventions you settle mid-book must be written into HANDOFF.md where that pass can overrule them in one place. If you need something from me, say what it blocks. I won't read the prose until the chapter is finished, so don't hold the build waiting on me.

What chapter 40 inherits

**A plan gap to decide first.** Chapter 38's carry-forward, corrected in the chapter 39 session, now reads "→ 40. The two minorities created in 1920 … spend the 1930s being used by people who did not make them." PLAN_I §8 has no section for them. Either §08 (the Danish Nazis, and why they failed) carries the Nazification of the German minority in Nordslesvig and the border-revision agitation, or chapter 38's arrow is re-pointed and the change recorded. Decide it, and amend PLAN_I §8 either way.

**Forward arrows chapter 40 must pay**, from chapter 39:
- Steincke's plan of 1920 becomes the social reform of 1933, after a night in Kanslergade.
- Norway occupies part of eastern Greenland in 1931, and The Hague decides the claim of 1921 in 1933.
- The unemployment that never returned to its 1920 level becomes the depression.

**Debts from PLAN_I §8:**
- §06 pays the residue of debt 3, but only if the 1933 reform is what removed the poor-relief franchise disqualification.
- §04 pays the second half of debt 7: collective agreements extended by law, and a lockout prohibited.
- Both claims need verifying before drafting.

**Verification queue for chapter 40, in order:**
1. **The 1939 referendum arithmetic** (§14.1). The plan says over ninety per cent yes, 44.5 per cent of the electorate, against a 45 per cent rule from 1915. Chapter 44 §03 turns on the same threshold. The DST route that reached the 1924 election volume in the chapter 39 session (dst.dk GetPubFile, sid=valg1924) is the first thing to try.
2. **Whether the 1933 social reform restored the franchise to poor-relief recipients** (§14.2), and in which act.
3. **The contents of Kanslergade**, from two sources: the export and currency measures, the extension of agreements, and the lockout ban.
4. **"Four laws and a principle":** name the four.
5. **The roster.**
   - 40[-] (Kanslergade 10, 29–30 January 1933) is marked sourced; verify the date and who was in the room anyway.
   - 40[n] (Nakskov, 1931) needs a subject, and its charges need verifying.
   - 40[f] needs a subject. The plan's second option, a woman who lost her vote to poor relief and got it back in 1933, needs no archive if item 2 holds.

**Leads already gathered in the chapter 39 session.** Each still needs its second witness where one is not given.
- **Stauning II and the Radicals:** Stauning II took office on 30 April 1929 with the Radicals inside the government. Munch was foreign minister from that day to 8 July 1940, and Steincke became social minister (lex.dk; Wikipedia).
- **Sterilisation law:** passed on 1 June 1929 as an experiment with a revision clause. It was replaced by a 1935 law that widened it and added compulsory castration (Nordisk Tidsskrift for Strafferet). Lene Koch calls the 1929 law Europe's first national eugenic sterilisation law.
- **End of gold convertibility:** 29 September 1931 (Galster, Nordisk Numismatisk Årsskrift 1953).
- **Eastern Greenland:** Norway's proclamation of 10 July 1931, Denmark's application to the court on 12 July 1931, and judgment on 5 April 1933 (lex.dk, Østgrønlandssagen).
- **Sønderjylland farms:** 484 forced auctions in 1932 (Grænseforeningen, Pengevæsen i Sønderjylland). This is single-source so far.
- **Cornelius Petersen's movement:** faded by 1928, and he died in Tønder in 1935 (Galster). Chapter 39 §09 introduced him.
- **Unemployment:** 1932's peak is given by Arbejdermuseet. That is single-source and not yet checked against DST.

**The unemployment figure is blocked the same way chapter 39's was.** The fetch tool refuses constructed URLs, and search did not surface the DST five-year volumes. Chapter 39 identified the volumes to 1930: 4. R. 48. Bd. 5. H., 61. Bd. 4. H., 74. Bd. 2. H., 88. Bd. 4. H. The 1931–35 and 1936–40 volumes still need identifying from the same publication lists. **If I paste direct dst.dk links for those volumes into the brief, the figure is buildable; if not, plan its replacement at the start rather than discovering the block halfway.**

**Toolchain, from the chapter 39 session.**
- **CHAR_W (item 105).** `mapspine.CHAR_W['mapt']` under-estimates the rendered width by about a tenth: measured 6.36 against 5.68, with mapx 5.32 and mapl 6.61. The mapspine table is unchanged. figs_40.py should copy figs_39.py's measured-width `fold()` rather than use the table, until a dedicated session fixes mapspine and regenerates every affected figure.
- **Drafting notes (item 102).** mkbody.py now refuses any drafting note in any wording the pattern knows, through draftnotes.py. Resolve notes or move them to Sources as questions addressed to the reader. Do not name scripts or tools on a reader page (item 103).
- **Coastlines (item 86).** Closing a polygon on a straight line between two coastal endpoints loses islands. If chapter 40 draws a band across Sønderjylland, clip against the land polygon and check Als and Ærø in the raster.
- **Apparatus is not a constant.** It measured 3,695 on chapter 37, 3,632 on chapter 38 and 3,373 on chapter 39. Do not predict page length from 3,786.
- **Markdown estimator.** In chapter 39, the section count with blockquotes and em-dashes stripped read 73 words under the built narrative (4,009 against 4,082). It is good enough for finding a missing subject and not for anything else.
- **Two Meanwhile blocks.** mw_at still places exactly two, at the third and seventh sections. A ten-section chapter fits it.

**Open and needing me. None of these blocks chapter 40.**
- A session to correct CHAR_W and regenerate and re-inspect every figure (item 105). `svg_titles.txt` already crosses the canvas edge at measured widths.
- A cleanup session for the 33 drafting notes on pages 25–32 (item 102). Five of them are research questions.
- Chapter 37 says Munch held the foreign ministry for twenty years; it was eleven (item 103).
- Chapter 38's Still unresolved list, and a figure caption naming figs_38.py (item 103).
- Twice now, source was pushed before its build output was committed. After applying a session's patch, run the build sequence and commit the pages, bodies, SVGs and index in the same push.
