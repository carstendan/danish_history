# CONVENTIONS — the rules the book is checked against

*Collected 19 September 2026 for the consistency review, from `HANDOFF.md`,
`PLAN_G.md`, `PLAN_H.md` and `PLAN_I.md`. This file does not replace those
records; it gathers them so that the review checks the book against one list and
Carsten overrules in one place. Where a rule is quoted it is quoted from the
place named; where two places disagree, both are given.*

*Status words: **in force** — the book must obey it; **spent** — a structural
decision that was carried out and is not a rule about prose; **superseded** — later
decisions replaced it; **proposed** — not yet agreed.*

---

## The D-series

### D-1 · Forward arrows beyond the next part name a part letter — in force

**Rule.** A forward arrow may name a chapter *number* only inside the next part.
Beyond that it names a part letter: `→ Part H`.

**Reason.** Three of Part F's twelve arrows pointed two parts ahead and were wrong
within a year, because the chapters they aimed at moved when Part G took seven
chapters instead of six. A part letter cannot go stale.

**Extended.** Item 15 applied D-1's reasoning to prose as well: `c21`'s "chapter
32" became "Part H" rather than a mechanically incremented number, because the
target was unplanned.

**Defined.** `PLAN_G.md` §6; `HANDOFF.md`, *How a cross-reference is written*
(with the table of the six cross-reference forms).

**Checked by.** The arrow sweep (`REVIEW-CONSISTENCY.md` §4). Check 7 reads prose references in
every section a reader reads, in both forms ("chapter N" and "(N)"), since review
session 4 (§8.6, §8.8).

### D-2 · Part G is seven chapters — spent

**Rule.** Part G, 1660–1814, is seven pages, 25–31.

**Reason.** The Danish Atlantic, 1620–1803, has no decade seam and belongs to none
of the chronological chapters; given its own page, the residue divides into six
chapters of nine to ten sections. "Seven is subtraction, not judgement." The
other two grounds first offered were withdrawn.

**Defined.** `PLAN_G.md` §1 and §6. "43 chapters" in its heading was superseded by
D-10 and then item 136 (45).

### D-3 · The spine map is 1660, not 1658 — spent

**Rule.** The Part G spine map is dated 1660.

**Reason.** Roskilde (February 1658) also took Bornholm and Trøndelag, and the
Peace of Copenhagen gave both back in May 1660; a map dated 1658 draws a
settlement that lasted twenty months.

**Defined.** `PLAN_G.md` §6; `HANDOFF.md`, spine-map list.

### D-4 · Chapter 30's declared span stays 1620–1803 — spent

**Rule.** The index fan draws chapter 30 at its true span even though it overlaps
its neighbours.

**Reason.** The crossing is about 4 px on the 1000-unit viewBox, invisible at any
rendered size; honesty about the span costs nothing.

**Defined.** `PLAN_G.md` §6 only.

### D-5 · Part G's colour is `--indigo:#2F4C7A` — spent

**Rule.** As stated; `build_part_g.py` raises on a missing token.

**Reason.** Not recorded beyond "Adopted".

**Defined.** `PLAN_G.md` §6 only (and the part-colour line in §3).

### D-6 · Calendar: the Danish state's style at the time — in force

**Rule.** Dates are given in the style the Danish state used at the time —
**Julian before 1 March 1700, Gregorian after** — with the foreign style in
parentheses at the first divergence in a chapter. Helsingborg is 10 March 1710
(28 February, Swedish style); Poltava 8 July 1709 (27 June, Russian style).

**Reason.** Parts A–F are Old Style and nothing said so; a reader checking Lutter
am Barenberge against a German source finds 17 August or 27 August depending on
which state printed it. *Corrected in review session 8:* the example had "27 August or
6 September", and chapter 23 printed the battle as 27 August — the new style. It is
17 August (27 August, new style), and the page now says so (`REVIEW-CONSISTENCY.md` §12).

**The fix the decision named, and whether it happened.**
- *A `gammel og ny stil` glossary entry in chapter 27* — **done**, on the page.
- *"One line in the index's conventions list"* — **done in review session 12.** The
  index's *Decisions already made* list (`index_generator.py`, the `ul.conv` block) had
  six entries and none mentioned the calendar; it now has a seventh, *Calendar*
  (`REVIEW-CONSISTENCY.md` §16).

**Known limit.** It does not resolve the Frederiksborg peace of 1720 (3 June or 3
July — a disagreement about the month, not the style). See E4 in *REQUIRES
PHYSICAL / ARCHIVE ACCESS*. *Review session 9:* chapter 27 now gives 3 July 1720
(Danish style), ratified 23 July, and states both rival readings — Schou's 3 June, and
the English reference works' 3 July Julian, 14 July in the Danish style.

**Applied to Part G, review session 9.** The part's first divergence is 25 §01 (10–11
February 1659, 20–21 new style); each chapter gives its own first (26 Vienna, 27
Travendal, 31 Tsar Paul's murder; 28–30 have none). **One exception, decided in session
9:** a second parenthesis is allowed where the chapter's argument needs the foreign date
on the page — 27 §07's Stockholm preliminaries, 14 June (3 June, Swedish style), without
which the Frederiksborg dating cannot be followed (`REVIEW-CONSISTENCY.md` §13.5).

**Part H, review session 10:** every date in 32–36 is Gregorian on both sides and there is no Russian
date; nothing to add. **START_HERE_review_10's calendar remark was wrong**: it said Sweden was "one
day ahead of Julian in 1716". Sweden ran that calendar from 1700 to 1712 and was **Julian from 1712 to
1753**, eleven days behind Norway in 1716 — as chapter 27's own *gammel og ny stil* entry says. 27's
Sources now give its 16 April 1716 as the Danish-Norwegian style (5 April, Swedish), checked against
Fredriksten (night to 4 July; the Swedes' 22 June) (`REVIEW-CONSISTENCY.md` §14.1, §14.5).

**Part I, review session 11:** no Russian date before February 1918 on any page (37's Meanwhile
gives Russia's 1917 by year); nothing to add (`REVIEW-CONSISTENCY.md` §15.5).

**Part F, review session 13:** its two divergences — 23's Lutter (17 August, 27 new style) and 24's
battle of the Sound (29 October 1658, 8 November Dutch) — were set off by a dash; both now in
parentheses, each clause kept whole (`REVIEW-CONSISTENCY.md` §17.2).

**Defined.** `PLAN_G.md` §6; `HANDOFF.md`, *Dates: old style and new style*.

### D-7 · The Atlantic chapter is 30, after the reforms — spent

**Rule.** Chapter 30 (the Danish Atlantic) follows chapter 29 (Struensee and the
reforms).

**Reason.** Under the old order both chapters had to introduce Reventlow, the
Bernstorffs and Schimmelmann-in-office; the swap pays that setup once, and "a
reader meeting an act before the government that made it is a comprehension
fault, not a preference".

**Defined.** `PLAN_G.md` §6 only.

### D-8 · Prose intervals are completed intervals — in force

**Rule.** Count whole years elapsed, not the difference between the two
year-numbers. Where the completed count falls within a month of the next one up,
**name the two years instead of stating an interval.** Treat every "N years
after" and "N years later" in a draft as a claim to verify.

**Reason.** An interval written in prose is guarded by nothing; four were wrong or
misleading in Part G at first build.

**Defined.** `HANDOFF.md`, *Convention D-8*; applied in `PLAN_H.md`.

**Checked by.** Nothing mechanical. `sweep_facts.py` compares dates and counts
across chapters but does not test intervals; the reading pass does. Part C's pass (session 5)
found nine wrong intervals, and the fixes' checker found one of them re-broken by the fix. Part D's
(session 6) found sixteen, and the checker two more in the fixes ("seven weeks", "for two years").
Part E's (session 7) found thirty-four, and the checker three more in the fixes ("thirty-six",
"twenty-seven years of rule", "four months"). Part F's (session 8) found sixty-six, and the checker
five more in the fixes (among them "since the new star of last November", written while removing
"thirteen months"). Part G's (session 9) found ninety-five; the two checkers found five more in the
fixes, and the reviewer wrote and caught a sixth ("three months before" for 15 June to 5 September).
Part H's (session 10) found ninety-three (32 nineteen, 33 twenty-four, 34 twenty-three, 35 thirteen,
36 fourteen), and four more went with claims that were cut; the first checker found five more in the
fixes (among them "two days before" the session of 1884, which opened three days later, and "when he
was fifteen" for DBL's "fra det 15. år"), and the second a sixth that a fix exposed ("the same summer"
for a treaty of 14 January) (`REVIEW-CONSISTENCY.md` §14.2). Part I's (session 11) found ninety-eight
(37 six, 38 twenty-one, 39 five, 40 ten, 41 eleven, 42 seven, 43 nine, 44 thirteen, 45 sixteen), and
the three rounds of checking at least seven more in the fixes — among them a girl written "nine" and
then "not quite nine" who was eight years and eleven months old (§15.2).

### D-9 · Vignette balance tags — in force

**Rule.** The vignette `(who)` line ends in a bracket: `[f]` where a woman is the
agent, `[n]` where the subject is non-elite, `[-]` where neither applies. Every
chapter carries at least one `[f]` and one `[n]`. Backfill is lazy — tagged when
a part is next touched.

**Reason.** Lesson L7a (women as agents) had no check behind it, and both
recorded failures — chapter 25's missing woman, chapter 31's missing non-elite
subject — were found by hand after drafting. `[-]` exists so a chapter of
untagged elite men does not look like a chapter nobody tagged.

**Defined.** `HANDOFF.md`, *Convention D-9*; `PLAN_H.md` §4 (the Part H roster);
restated in `PLAN_I.md`.

**Where the evidence names no one (R-1, agreed by Carsten 20 September 2026).**
In a chapter whose evidence names no individual, the `[f]` requirement is met by
the part, not by the chapter, and the who-line may name the find instead of a
person (L9a). `[n]` is still required of every chapter. The chapters it covers
are listed, closed, in `vignettes.py` (`NAMES_NO_ONE`): **01 and 03**, whose part
carries its `[f]` in 02 (Lola). A chapter joins the list by a decision recorded
here, never to make the check pass. Part A tagged on the same day.
**Extended to 04 and 05 (R-2, agreed by Carsten 21 September 2026)**, whose part carries
its `[f]` in 07 (Kirsten Svendsdatter). 06 is not covered: its evidence names people.
**06 carried out (R-3), review session 5:** the Juellinge woman `[f]` and a smith's household at
Vorbasse `[n]`; Parts A and B have no D-9 failure. **Part C tagged the same day:** 09 and 11 carry
both; **08 lacks `[f]` and 10 lacks `[n]`** — true failures, put to Carsten as R-4 and R-5
(`REVIEW-CONSISTENCY.md` §9.9), not tagged away. **Both answered 21 September 2026 as
recommended:** Ragnhild at Glavendrup (08 §04, `[f]`) and the Trelleborg garrison's dead (10 §08,
`[n]`), for review session 6. **Carried out in session 6: no D-9 failure in Parts A–C.** **Part D
tagged the same day: no chapter carries `[f]`, and 14 carries no `[n]`** — R-6 to R-9
(`REVIEW-CONSISTENCY.md` §10.9), not tagged away. **R-6 answered 22 September 2026 as
recommended:** Queen Bodil (12 §06, `[f]`), for review session 7. **R-7 answered the same day
as recommended:** Ingeborg, repudiated by Philip II (13 §09, `[f]`), for review session 7. **R-8
answered 23 September as recommended, both parts:** Margrete Sambiria re-scoped into a vignette
(14 §04, `[f]`) and Niels Ebbesen retagged `[n]`, the weakest in the book and recorded as such.
**R-9 answered the same day as recommended:** 15 §12's vignette extended with Margrete's letter of
c. 1370 and retagged `[f]`. All four are for review session 7; until they are carried out,
`vignettes.py` reports 12, 13, 14 and 15 as D-9 failures, correctly. **Carried out in session 7: no
D-9 failure in Parts A–D** (`REVIEW-CONSISTENCY.md` §11.1). **Part E tagged the same day: 16 carries
neither, 17 and 20 no `[f]`, 18 no `[n]`** — R-10 to R-14 (§11.9), not tagged away.
**R-10 answered 23 September 2026 as recommended:** Margrete at the Lund landsting, 1387, re-scoped
from 16 §04's acclamation paragraphs (`[f]`), for review session 8. **R-11 answered the same day as
recommended:** the Victual Brothers at Bergen, 1393 (16 §06, `[n]`), for review session 8. **R-12 answered the same day
as recommended:** Margrete's gift letter of 8 December 1411 (17 §05, `[f]`), for review session 8. **R-13 answered the same day as
recommended:** the Reventlow vignette re-scoped to the peasants at Sankt Jørgensbjerg, 1441 (18 §08,
`[n]`), for review session 8. **R-14 answered the same day as recommended:** Anne Meinstrup at
Ringsted, 20 January 1535 (20 §06, `[f]`), for review session 8. All five are for session 8; until
they are carried out, `vignettes.py` reports 16, 17, 18 and 20 as D-9 failures, correctly. **Carried
out in session 8: no D-9 failure in Parts A–E** (`REVIEW-CONSISTENCY.md` §12.1). **Part F tagged the
same day: 21 carries no `[n]`** — R-15 (§12.9), not tagged away. **R-15 answered 24 September 2026
as recommended:** Rasmus Pedersen, Tycho Brahe's tenant, Hven 1590–92 (21 §08, `[n]`), for review
session 9; until it is carried out, `vignettes.py` reports 21 as a D-9 failure, correctly. **Carried
out in session 9** (Gundsømagle; the king's court, 10 July 1591): **no D-9 failure in Parts A–F**
(`REVIEW-CONSISTENCY.md` §13.1). **Part G tagged the same session: 25 carries no `[f]`, 27 and 31 no
`[n]`** — 25's and 31's are the two failures this entry names as found by hand at drafting, still
there — R-16 to R-18 (§13.9), not tagged away. **R-16 answered 25 September 2026 as recommended:**
Charlotte Amalie at Nykøbing Slot, 25 June 1667 (25 §08, `[f]`), for review session 10; until it is
carried out, `vignettes.py` reports 25 as a D-9 failure, correctly. **R-17 answered the same day as
recommended:** Kari Rasmusdatter Hiran at Nordkleiva, Krokskogen, April 1716 (27 §05, `[f][n]`, §05
re-scoped as *Norway, and the war at sea*), for review session 10; until then 27 is a D-9 failure, correctly. **R-18 answered the same day as
recommended:** Hans Andersen, shoemaker, Odense, 1812 to January 1813 (31 §07, `[n]`), for review
session 10; until then 31 is a D-9 failure, correctly. **R-16 to R-18 carried out in session 10**,
their facts checked first (`REVIEW-CONSISTENCY.md` §14.1): Charlotte Amalie at Nykøbing Slot, 25 June
1667 (25 §08, `[f]`); Kari Rasmusdatter Hiran at Nordkleiva and Jonsrud, Krokskogen, April 1716 (27
§05, `[f][n]`, §05 re-scoped); Hans Andersen, shoemaker, Odense, 1812 to January 1813 (31 §07, `[n]`).
**Part H, tagged at drafting, checked the same session:** 36's J.C. Christensen retagged `[-]` (§14.7).
**No D-9 failure in the book.** **Part I, checked in session 11 (§15.5–15.6):** 43's Rasmussen `[n]`,
44's Anna Lund Lorentzen `[f][n]`, 42's Ellen Nielsen `[f][n]`; **38's only `[f]` was Johanne Martine
Braren, lifted onto a horse — R-19, answered by Carsten 27 September 2026 as recommended: Elna Munch at
Amalienborg, 3 April 1920 (38 §08, `[f]`), carried out the same session**; Braren `[-]` (a pastor's
adopted daughter, not the farm girl the recommendation assumed). No D-9 failure in the book.

**Checked by.** `vignettes.py` balance layer, which reports such a chapter as
"[f] part" — and still as FAIL if no chapter of its part carries `[f]`.

### D-10 · Part I takes eight chapters — superseded by item 136 (nine; book is 45)

**Rule as it stands.** Part I is nine chapters, 37–45; the book is 45 and ends in
1953.

**Reason.** The spine had a visible 1920–1929 hole on the index page; the twenties
are a chapter's worth of material, and forcing them into the thirties cuts the
D-9 material first. Item 136 then found no three-way division of 1943–1953
works (each apparatus set costs ~5,000 page words) and four lands every chapter
at 36–45 minutes. The book's end at 1953 stands on its own ground: §20 of the
last chapter installs the mechanism 1973 exercises. The earlier ground (a
43-chapter spine "every tool assumes") was false and is struck.

**Defined.** `HANDOFF.md`, *Decision D-10* and item 136; `PLAN_I.md` §1.

### D-11 · A figure sets text colour with `style=`, never `fill=` — in force

**Rule.** As stated. Companion rule: `mapspine.text_on()` picks the colour against
the composited ground and the script asserts on the returned contrast — "D-11
fixes the mechanism, `text_on` picks the colour, and neither is sufficient alone."
Threshold 4.5:1 (`.mapl` is not WCAG large text).

**Reason.** A stylesheet rule beats a presentation attribute, so every `fill=` on
a classed `<text>` renders in the class colour. Found in the raster of chapter 40's
figure 3 and nowhere else.

**State.** The twenty legibility failures were fixed (item 129). Review session 20 measured
the colours in the page (the computed fill of every figure text against what its markup asks,
all 45 pages): 616 texts ask a colour and 449 drew another, every one a `fill=` on a classed
text, in 47 figures - page 12's red "killed, Odense" drew grey. **Where the colour names a
category, a key or a coloured mark it now draws: 109 texts in 32 figures**, in `style=`, and
where the asked hue is under 4.5:1 beside the letters (on the halo over its measured ground)
in the same hue darker (amber `#915218`, teal `#377668`, olive `#6F6223`, slate `#48667A`,
terracotta `#A35738`, and brown `#835438` on 38's zone map). **Recorded, not changed: 340** -
256 ask one grey and draw another (a hierarchy of inks, not a meaning), 79 ask a hue as an
accent (Part E's verdigris headers, 13's red headers, dates in a list),
and 14's five pawn-map labels, which in their own hue on their own region read worse than in
the class grey. **Review session 21 deleted every `fill=` on a figure text** (Carsten), 357 on 23
pages: 354 on classed texts, each drawing its class colour already, and page 06's three inside a
`<g class="mapl">` with no class of their own, which the page honoured (a text's own attribute
beats what it inherits) - SILVER and BRONZE moved into `style=`, IRON asked the class grey. No
text's computed colour changed (measured on all 2,911 texts and 5 coloured tspans, shipped pages
against new, at 1200 and 390), and after the deletion alone every figure was pixel-identical to the shipped one at 1200,
1100 and 390 (at 390 with the new scroll line hidden: it moves the figures down the page).

**Guard.** `pageguard.text_fills()`, from `nesting()`, in every part build, reading the page as
HTML does: a `fill=` on any `<text>` or `<tspan>`, on an element with a map class, or on any
element round a text outside the map class it has or takes from a `<g>`, up to the figure's svg
(through a nested one; but `fill="none"`, meant for the shapes beside it), is refused, in any case or quoting (planted through a
build: page 03 NOT WRITTEN; the shipped pages, 357 refusals on 23). In the page, `ordercheck.py` lists every
figure text drawn in another colour than its markup asks (it took in
`claude/session20_colours.py`): the shipped book 340, the book now 0, at 1200 and at 390.

**Defined.** `HANDOFF.md` item 110 and its correction in item 129; items 158 and 159 and
`REVIEW-CONSISTENCY.md` §24.

### D-12 · Draft prose is never written through a shell heredoc — in force

**Rule.** Write draft prose with the file-editing tools. A script that must
generate prose reads its text from a UTF-8 file.

**Reason.** Thirty-six literal `ø` and `→` sequences entered
`c41_draft.md` through a quoted heredoc and passed every guard.

**Guard.** `mkbody.build()` refuses a draft containing a backslash-u escape.

**Defined.** `HANDOFF.md`, *Convention D-12*.

### D-13 · A vignette is the particular inside a general section — in force

**Rule.** A vignette is the particular inside a general section. **When the
section is named for the vignette's subject or its exact moment, the vignette
restates the body.** Either the vignette moves to a section about the process it
illustrates, or the section is re-scoped so the vignette has somewhere to stand.

**Reason.** Unwritten, and obeyed 126 times out of 132. The six that break it are
the six verified repetitions: 27 §05 Tordenskjold, 27 §09 Gertrud Rask, 29 §03
Caroline Mathilde, 26 §09 Leonora Christina, 35 §03 Uhd, 22 §08 Tommesis (against
the figure beside it). Every healthy case is "section named for the process,
vignette supplies a person inside it".

**Defined.** `HANDOFF.md` item 138; `REVIEW-BUILD-FAULTS.md` §4. A seventh case
was found in the Part I reading (item 139): 42 §03 *The warning* and its Duckwitz
vignette, which repeats the section's sourcing paragraph.

**Agreed** by Carsten, 19 September 2026 (review session 2, decision D-D). The
seven cases are decided under it as each part's review reaches them: 42 §03 with
Part I; 22 §08 with Part F; 26 §09, 27 §05, 27 §09 and 29 §03 with Part G; 35 §03
with Part H. **Part A, read in review session 3: no case** (`REVIEW-CONSISTENCY.md`
§7.7; 02 §06 is named for its vignette's place but restates nothing, and is kept). **Part B, review session 4: one case, 05 §04 *Hjortspring*, decided by
re-scoping the body to the army** (§8.4); 07 §02 and §03 are named for their vignettes'
subjects but restate nothing, and are kept. **06 §10, session 5:** the new Vorbasse vignette
showed the list the body had given, and the body was re-scoped around it (§9.1). **Part C,
session 5: no case** — 08 §01 and 10 §04 are named for their vignettes but restate nothing (§9.5).
**Part D, session 6: no case** — six sections are named for their vignettes' moments and none
restates it (§10.5); 14 §04's Margrete Sambiria paragraph is proposed for re-scoping under R-8.
**Re-scoped in session 7** (§11.1). **Part E, session 7: no case** (§11.5); 20's Rantzau vignette sits
out of order in §06 and retells §05's Aalborg — for moving when 20 is next opened. **Re-scoped in
session 8:** 16 §04 (Margrete at Lund) and 18 §08 (the peasants at Sankt Jørgensbjerg), under R-10 and
R-13 (§12.1). **Part F, session 8: 22 §08, one of the seven, decided by re-scoping** — the section is
now *Witchcraft and the state*, the vignette Johanne Tommesis alone, the list in the figure only
(§12.5). 20's Rantzau vignette was not moved (20 was opened only for R-14). **Part G, session 9: the
four remaining Part G cases decided by re-scoping** — 26 §09 *The state's prisoners*, 27 §05 *The war
at sea*, 27 §09 *The Greenland mission*, 29 §03 *The court under Struensee* (with 29 §04 *The fall,
1772–75*); also 30 §05 *The Akwamu rising on St Jan, 1733–34* and 31 §08 *Norway ceded*, which were
named for their vignettes' moments (§13.5). Six of the seven are decided; 35 §03 waits for Part H.
**Part H, session 10: 35 §03 decided by re-scoping** — *Hjedding, 1882* is now *The cooperative
dairy*: the body is the institution (Kaslunde, a member's obligations, the vote, the liability, the
spread), the vignette Uhd and the founding. **All seven cases are decided.** Also re-scoped in Part H:
34 §01, 36 §09/§10; 32 §09's and 33 §06's overlaps cut (§14.5). **Part I, session 11: 42 §03 had
drifted back** — body and vignette both told the 11th, Berlin, the 19th and the 28th; re-scoped again
(the body the dated chronology, the vignette the man and the Hedtoft hand-over). 38 §08 re-scoped for
R-19 (§15.3, §15.6).

**Checked by.** Reading. `REVIEW-BUILD-FAULTS.md` §4's overlap measure is a way of
choosing what to read, not a test — it scores healthy vignettes about the same
subject as high as broken ones.

### D-14 · Regnal numbers in the Danish style for Scandinavian rulers — PROPOSED, and already applied

**Rule.** Danish, Norwegian and Swedish rulers take the Danish ordinal: Christian
4., Frederik 7., Karl 12., Gustav 4. Adolf, Haakon 7. Other rulers take Roman
numerals: Frederick II of Prussia, George III.

**Reason.** It is what the book does — 409 Danish-style regnal numbers on the
pages at `c5775cf`, counted, not estimated — and it has never been written down. The review found seven Roman forms for Scandinavian kings in Parts G and I
and fixed them to the majority; four more — not five, recounted — were on pages 05,
07 and 10 and were fixed in review session 3, when those pages could be rebuilt. 13's
two "Frederick II" are the Emperor and are right. No page now has a Roman form for a
Scandinavian ruler. The converse was found in session 6: 14 and 15 wrote the Holstein counts
"Gerhard 3." and "Johann 3." in prose while their own figure captions said III; the prose now
follows the rule.

**Defined.** Here. Evidence in `REVIEW-CONSISTENCY.md` §2.1.

### D-15 · Place names — in force

**Rule as proposed.** *Schleswig* for the duchy and the region throughout; Danish
forms only where they are Danish words or names (*Sydslesvig*, *Slesvigsk Parti*,
*Sønderjylland*, *Flensborg Avis*). A town takes the form of the country it is in
today (Flensburg; Haderslev, Aabenraa, Sønderborg). The Skåne towns in their
Danish form in prose before 1658 and their Swedish form in visit blocks.
English exonyms where English has one in common use (Copenhagen, Jutland, Zealand,
Funen, the Sound). Viking-age kings under their English names, from Knud the Holy
under their Danish ones, as now. *Corrected in review session 6:* "as now" is the rule, and
the practice switches at the page, not at Knud — Sweyn through chapter 11, Svend from chapter 12, so
Svend Estridsen (1047–74) is Sweyn in 11 and Svend in 12, where his first mention gives both
(`REVIEW-CONSISTENCY.md` §2.3, §10.5).

**Reason.** The pages use the bare word Schleswig 105 times and Slesvig 129 (counted by
`sweep_names.py`'s reader at `c5775cf`), switching by
drafting session rather than by rule (§2.2 of the review), and the same drift runs
through Flensburg/Flensborg, Holstein/Holsten and the rest. An English-language book
whose chapter titles and index already say "Schleswig" should say it in the prose.

**Agreed** by Carsten, 19 September 2026 (decision D-B), with "Dithmarschen"
for the misspelling "Ditmarschen" in 19–21. Party and newspaper names keep their
Danish form: *Slesvigsk Parti* (not "Slesvig Party"), *Flensborg Avis*.

**Applied** to Part I on the day it was agreed: 37, 38, 44 and 45 in prose, 39's
"Slesvig Party", and three figures — `figs_38` (map labels Flensburg, Schleswig),
`figs_39` (Slesvigsk Parti), `figs_43` (South Schleswig, and a stale "section 07"
that is §06). Every other part takes it in its own reading pass. **Part A, review
session 3: read, and nothing needed changing.** **Part B, review session 4:** one wrong use (06's
Nydam boat "in Schleswig ever since" — it was in Kiel; now "in Germany"); the rest right. **Part C, review session 5:** four uses, all
the German town; nothing to change. **Part D, review session 6:** 12's three Slesvig and one Århus
are Schleswig and Aarhus; 12's "Fyn" is Funen, 13's "Mølln" Mölln; the diagrams follow the prose,
the maps keep Danish. Schleswig 172 in 26 chapters, Slesvig 101 in 10, none of them in Part D. **Part E, review session 7:**
19's two Slesvig (both the town) are Schleswig, 18's Flensborg Flensburg, 20's visit-block Malmø
Malmö; and **D-B's Dithmarschen is carried out** in 19 (eleven), 20 (one), 21 (six) and the config,
with 16–18's "Ditmarsken" in English prose (three) as 13's was — Danish words such as a glossary
term stay Danish. Schleswig 178 in 26 chapters, Slesvig 99 in 9: none in Parts A–F. **Part F, review session 8:** no
Slesvig; the noun "Scania" is Skåne (three), the adjective "Scanian" stays as in Part G; "Femern" is
Fehmarn (23); Malmø before 1658 and Malmö after, as the rule says (§12.5). **Part G, review session
9:** every Slesvig in prose is Schleswig (26, 27, 29, 31, figure texts and captions); Tönning,
Glücksburg; Christiania on the maps of 1660, 1721 and 1814. Schleswig 212 in 29 chapters, Slesvig 65
in 4, none in Parts A–G (§13.5). **Part H, review session 10:** every Slesvig in prose, figure
text, captions and questions is Schleswig; Nordslesvig is North Schleswig (35 §10's title and anchors
follow), Flensborg Flensburg, the Slien the Schlei, Frederiksstad Friedrichstadt, Mysunde Missunde;
`map_1864`'s aria-label and legend are English, its map-face labels Danish. **Schleswig 297 in 31
chapters, Slesvig 2 in 2 — both Danish book titles in Sources (32, 33). No Slesvig in the book's
English** (§14.5). **Part I, review session 11:** every "Nordslesvig" in English prose is North Schleswig; Før is Föhr;
Danevirke in 33 and 34 too (34 §03's title with it); 32's *Dannevirke* is the newspaper. **Schleswig
316 in 31 chapters, Slesvig 4 in 3 — all names** (two Danish book titles; in 38 the plebiscite
commission's French name and a Danish article title) (§15.5).
Maps (`map_*.py`)
label in Danish throughout and are left for a decision of their own when Part A–D
maps are next touched.

### D-16 · Length is never a reason to cut — in force

**Rule.** Inside the 25–50 minute band, a chapter is not cut to meet the 28–40
advisory. What decides a change is the story:

1. if it makes sense for the story, keep it;
2. if restructuring, or moving material between chapters, makes sense, do it;
3. if it is good as it is, keep it — it is within limits.

Cuts that remove repetition, or move method out of the prose into Sources, are
made because they improve the reading, and say so. The advisory is a reason to
*read* a long chapter closely, never a reason to shorten it.

**Reason.** Carsten, 19 September 2026, answering I-5 (chapters 44 and 45 over
the advisory): "do not trim for the sake of time."

**Applied** (19 September 2026). 44 (then 44 min) and 45 (then 45 min) are kept as they
are: both read as the story needs, and neither has material that belongs elsewhere. This
is the defence item 138 said they lacked. (Since then 44 is 48 and 45 is 50.)

**Closed** (Carsten, review session 22). The hard band is read in whole minutes: every
part build stamps a page "about N minutes", N = `round(words / 210)` on the words it counts
before `linkindex.py` adds the index link (6 words); `build_part_f/g/h/i.py` refuse a page
whose N is outside the band, A-E's builds do not, and `build_all.py`'s summary flags any
page whose stamp is. 21 (50.25 minutes by the builds' count) and 45 (50.15) are stamped 50,
inside.
`bookstats.py` now prints, for the whole book and in every cold run, the chapters whose
stamp is outside the band ("none"); its "min" column counts the page as shipped, so it can
say 51 of a page stamped 50 (planted: page 20 built at 10,605 words is stamped 50 and not
listed, at 10,606 stamped 51 and listed). The five narrative sections over 760 words (16
§08, 21 §06, 42 §02, 43 §02, 44 §03) are kept, as read in the review (21 §06 OVER since
session 13): `narrative.py` prints each "OVER, kept" at or under the count it was kept at,
and a sixth, or one of the five grown, plain OVER (planted both ways).

**Defined.** Here. It qualifies L1a: the hard band still binds; the soft advisory
is diagnostic only.

### D-17 · A page asks each question once — in force

**Rule.** Across the five WHAT-THIS-PAGE-ANSWERS questions (`qs` in `mkbody.py`), the checkpoints
(`checks` in the build scripts) and the four end tiers (Recall, Causal, Counterfactual, Contested), a
page asks each question once. **The opener keeps its question** — it is the page's promise; a later
checkpoint or end-tier question that repeats it is rewritten to test something else that is true and
on the page. A checkpoint asks only what the page has said before its anchor section.

**Reason.** Measured in review session 11 across 25–45, as Recall is (content-word Jaccard ≥ 0.4
against the shipped checkpoints): an opener repeated a checkpoint 20 times in 13 of 21 chapters, a
Causal question 4 times, and 17 openers were asked again in the end tiers, 9 word for word. Carsten,
25 September 2026: "ask once", as recommended.

**Carried out** in 25–45 (`REVIEW-CONSISTENCY.md` §15.1): 76 questions in Parts G and H, and in Part I
every end-tier repeat and 35 checkpoints. After: no pair at 0.4 on any page 25–45. **Carried out in
Parts A–F in review session 12** (`REVIEW-CONSISTENCY.md` §16.1): this note had said pages 20, 23 and
24 failed it; measured, **twenty of the twenty-four did**. 244 questions changed in 01–24 (53
checkpoints, 190 end-tier, one false opener in 17). After: no pair at 0.4 on any page 01–45.

**Guard.** `pageguard.asked_twice`, asked before a page is written by every part's build —
`build_parts_abc.py`, `build_part_d.py`, `build_part_e.py`, `build_part_f.py` (review 12) and
`build_part_g.py`, `build_part_h.py`, `build_part_i.py`: NOT WRITTEN on any pair at ≥ 0.4. It cannot see
one question asked in other words; the reading passes found about forty-five such in 25–36 and, by the
fixers' counts, about a hundred and forty in 01–24.

**Defined.** Here; `HANDOFF.md` items 149 and 150.

### D-18 · Figure text carries a halo; a thick line or a marker never crosses a label — in force

**Rule.** Every `.mapt`, `.mapl` and `.mapx` text is painted over a thin stroke of paper (one rule
in `style.css`: `paint-order:stroke`, `#F0F2EE` at .8, 2.6px), so a thin line under a label - a
coast, a border, the graticule, anything up to 1.4 wide - stops at the letters, and a label may
straddle land and sea. Text set on a solid ground takes no halo: the light fills in
`mapspine.HALO_EXEMPT` and `ON_BAR_INK`, and only when written `style="fill:#XXXXXX"` in capitals
(a CSS attribute selector matches the spelling; a `fill=` attribute loses to the class, D-11). A
thick line (a route, an attack line, a heavy border) or a marker through a label is not fixed by
the halo: the label is moved. A new light text colour goes into `HALO_EXEMPT` and `style.css`
together. *Under* means drawn before: a line drawn after a label crosses it whatever its width
(page 45's 1936 leader through "a quarter", review session 18), so a leader or tick near a label
is drawn before the label.

**Reason.** Review session 16 read all 220 texts `linecheck.py` listed in 31 figures: about 214
had a coast, border or route through them, because labels were placed at a point whatever lay under
them. Carsten, 28 September 2026, chose the halo over moving some two hundred labels.

**Guard.** `linecheck.py`, halo-aware, over `svg_*.txt` and over the bodies' inline figures:
0 crossed, three kept on purpose, each listed with its reason (the one measured wrong, 06's "the
great majority", is measured right since review session 17: `mapspine.text_items()` reads a
`<g>`'s text-anchor and class, markup and rotation). It reports a fill spelt any other way and a
light `fill=` attribute. An aid to looking, wired into no build; the text guards it shares its
measure with (overruns, overflows, collisions) run in every build since session 17. linecheck
does not read drawing order; `ordercheck.py` does, in the page (Chromium): it lists a text when
a later mark or a clip changes pixels in its box or its halo (review session 19; 0 in 128
figures; a later text over it is not seen), and is wired into no build either: Carsten kept it
standalone (review session 20), a fixed step of every cold run and handover at 1200 px and, with
`--width 390`, at a phone's. **The two are kept as they are, and both questions closed** (Carsten,
review session 22): linecheck stays out of the builds and a fixed step of every cold run and
handover, which every build follows (A-D's builds do not need `cairosvg`, which it does; E-I's
already do, through their figure scripts), and it does not learn drawing order, which
ordercheck reads in the page. Each catches what the other cannot: planted on page 18, a 3-unit
line through "Lund" drawn *before* the label shows round its halo and is listed by linecheck
alone; drawn *after*, by both; and a 1-unit line drawn after it, under linecheck's thickness
for a crossing, by ordercheck alone.

**Defined.** Here; `HANDOFF.md` items 154, 157, 158 and 160; `REVIEW-CONSISTENCY.md` §20, §23,
§24 and §26.

---

### D-19 · Figure text is measured in the page — in force

**Rule.** The text widths and heights the figure guards use, and every `fold()` that wraps to a
width (figs_38 to 44, fig_titles; figs_35 to 37 fold to a character count, which the guards check),
come from the page as a browser draws it, on the machine the reader uses, never from a raster and
never by eye. `mapspine.CHAR_W` is the page's monospace advance plus each class's letter-spacing,
the wider of Chromium on Linux and the Claude desktop app on Carsten's Mac: **mapt 6.10, mapx 5.46,
mapl 6.95** (Linux 6.07, 5.43, 6.92). A text with its own font-size is measured at that size, the
serif by `mapspine.SERIF_EM` (per em, rounded up from the page on both machines). No script keeps a
width table of its own. If `style.css` changes a font-size, a letter-spacing or the `--mono` stack,
the values are measured again in the page and every figure script re-run and read.

**Reason.** The table was "measured, not assumed" - in `rasterise()`'s raster, where mapt came out
six per cent narrower than the page draws it, and page 23's caption shipped cut with every guard
passing (review session 17). Seven scripts folded at the larger of the table and a second
raster measure, and eight (figs_24 to 31) checked their text at one number of their own for every
class, so the book measured one class four ways and never the page's. Carsten agreed the page values on 29
September 2026 (HANDOFF 105, closed).

**Guard.** The text guards (`overruns`, `overflows`, `collisions`) and `linecheck.py` read
`text_items()`, which reads `CHAR_W`, `SERIF_EM` and a text's own font-size; they run in every
figure script and, through `pageguard.figure_text()`, in the A-D builds. The values themselves are
checked only by measuring the page again (`REVIEW-CONSISTENCY.md` §22 says how).

**Defined.** Here; `HANDOFF.md` items 105 and 156; `REVIEW-CONSISTENCY.md` §22.

---

### D-20 · A figure never draws its text smaller than a 700 figure at 0.8 — in force

**Rule.** Below 1000 px a figure keeps 0.8 of its viewBox width and scrolls sideways inside its
box (`style.css`, one `min-width` line per viewBox width), so no text class draws smaller than
on a 700 figure at 0.8 (`.mapx` 6.8 CSS px): at 390 px every figure scrolls; from 721 to 999
only the 900-wide ones do, by 95 px at most. From 1000 px a figure drawn at viewBox 900 leaves
the column to draw at its own width - both ways where there is no section rail (1000 to 1239),
rightward only beside it - and its caption keeps the column's measure and starts at the figure's
padding, where every caption does (review session 21; it had kept the column's indent). On a
screen only: paper cannot scroll, and in print a figure shrinks to the page as before. While a
figure scrolls its caption stays in view under it (`position:sticky`) and opens with a line
saying so ("Wider than the screen — scroll sideways →", not read aloud), at exactly the widths
where that figure scrolls. Up to 720 px a figure's box is the viewport less 64 px, from 721 less
96 and at most 694, and less than half a pixel over does not scroll: so, a viewBox width being a
multiple of 5, a figure up to 780 wide scrolls below 0.8 W + 64, one from 825 to 865 below
0.8 W + 96, one 870 or wider below 1000 (and needs the 900s' breakout above), and one from 785 to
820 in two bands, for which no line is written yet (review session 21, checks 1 to 3; planted at
775, 780, 825, 865 and 870 and measured at every width from 600 to 1000; the book measured on all
45 pages at 24 widths from 320 to 1440: the line is there if and only if the figure scrolls). A fraction of a pixel at a browser zoom (999.5) drew a 900 figure at .771 and now at
.800 (check 1 measured it). Each pair of width queries that meet
(999/1000, 1239/1240) is written classic and range (`(max-width:999px), (width < 1000px)`), so a
fraction of a pixel between the two at a browser zoom falls in one of them, and a browser without
range syntax keeps the classic one (planted: with the range form unreadable, the classic one still
applies). The scroll lines are range only; 720 has no partner. A new
viewBox width needs its line in `style.css`, and its scroll line.

**Reason.** Measured in the page (review session 19): at 390 px 127 of 128 figures drew their
smallest text under 5 CSS px (3.1 in the 900-wide), and at the desktop column the 23 figures at
viewBox 900 (pages 01-20) drew every class 22 per cent smaller than the 68 at 700. Carsten chose
the scroll box over pinch-to-zoom and the breakout over redrawing 23 figures, 30 September 2026.

**Guard.** `pageguard.figure_widths()`, from `nesting()`, in every part build, for the plausible
fault - a figure at a width with no line: a figure must hold one `<svg viewBox="0 0 W H">`, first;
W a multiple of 5; no svg may stand outside a figure; and the page's style must hold, outside a
comment, the caption's hidden line and, for each W, `figure svg[viewBox^="0 0 W "]{min-width:0.8Wpx}`
and its scroll line under the query its band gives (a W from 785 to 820 is refused). It finds the
lines as `style.css` spells them, runs of white space and quotes aside, and refuses any other
spelling; not whether the browser applies them: review
session 20 made it read CSS as a browser does, four checks each found a style the browser read
otherwise, and Carsten had it cut back (review session 21). The proof is `ordercheck.py`, which
lists, at the width it runs (1200 and 390 in every cold run), any figure drawn under 0.8 of its
viewBox and any whose scroll line is shown when it does not scroll, or the reverse. What the phone draws is measured in the page
(`claude/session19_phone.py`, `claude/session21_widths.py` in the project).

**Defined.** Here; `HANDOFF.md` items 158 and 159; `REVIEW-CONSISTENCY.md` §24 and §25.

---

## Standing rules that are not numbered

The D-series is not the whole rulebook. These are the other written rules a
consistency review checks prose against. Each is quoted briefly; the full text is
where it is named.

| rule | where |
|---|---|
| Carry-forward lines must be solvent: every `→` points at a chapter that carries what it promises. | L5 |
| Vignettes are a named person at a named place and hour; women appear as agents; the `(who)` line names a person or says on the page why it cannot. | L7, L7a, L9a |
| Hedge live controversies explicitly. | L8 |
| Close on something that lands; do not close two consecutive chapters the same way. | L9 |
| Do not repeat the previous part's beats. | L3 |
| The countryside and religion are in every chapter. | L2 |
| Reading time: hard band 25–50 minutes, soft advisory 28–40. | L1a |
| A figure must not summarise prose the reader has just read. | *Settled during the Part E review* |
| Sources are two-tier: WORKED FROM, and WHERE THE ARGUMENT STANDS. | *Settled during the Part E review* |
| A section title is a claim and is checked like one. | item 117 |
| A reference to a chapter that has since been split is resolved by reading, not by inference. | *How a cross-reference is written* |
| Lettered chapter numbers are retired. | L1b |
| **Danish terms are glossed on first use in each page.** | index, *Decisions already made* |

### Conflicts found while collecting

1. **The glossary rule on the index and the practice in Part I disagreed, and the
   practice shipped a drafting instruction.** The index promises every Danish term
   is "glossed on first use in each page". Eighteen glossary entries on pages 40,
   41, 43, 44 and 45 had as their whole definition *"glossed in chapter 39 —
   reference, do not re-gloss."* **Resolved in favour of the written rule**: each
   now carries a one-line definition and "(chapter N)" for the full one, and
   `draftnotes.py` refuses the phrase. Detail in `REVIEW-CONSISTENCY.md` §1.1.
2. **D-6's index line was never added** (above). **Resolved in review session 12**: the
   index's *Decisions already made* now has a *Calendar* line (`index_generator.py`).
3. **The cross-reference table listed six forms; the pages use eight.** `→ 10,
   Part H` (number and letter) and `→ Part H, Part I` (two letters). This note said they
   appear in 6, 15 and 19; **they appear on seven arrows in six chapters** — the first form
   in 02, 06 (twice) and 14, the second in 04, 15 and 19. They read correctly. **Resolved in
   review session 12**: both are in the table in `HANDOFF.md`, *How a cross-reference is
   written*.
