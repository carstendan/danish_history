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

### D-6 · Calendar: the Danish state's style at the time — in force, not fully carried out

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
- *"One line in the index's conventions list"* — **not done.** The index's
  *Decisions already made* list (`index_generator.py`, the `ul.conv` block) has
  six entries and none mentions the calendar. Recorded as a finding in
  `REVIEW-CONSISTENCY.md`.

**Known limit.** It does not resolve the Frederiksborg peace of 1720 (3 June or 3
July — a disagreement about the month, not the style). See E4 in *REQUIRES
PHYSICAL / ARCHIVE ACCESS*.

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
"thirteen months").

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
session 9; until it is carried out, `vignettes.py` reports 21 as a D-9 failure, correctly.

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

**State.** Thirty legacy figures remain cosmetically non-compliant; the twenty
legibility failures were fixed (item 129).

**Defined.** `HANDOFF.md` item 110 and its correction in item 129.

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
(§12.5). 20's Rantzau vignette was not moved (20 was opened only for R-14).

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
Fehmarn (23); Malmø before 1658 and Malmö after, as the rule says (§12.5). Maps (`map_*.py`)
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

**Applied.** 44 (44 min) and 45 (45 min) are kept as they are: both read as the
story needs, and neither has material that belongs elsewhere. This is the defence
item 138 said they lacked.

**Defined.** Here. It qualifies L1a: the hard band still binds; the soft advisory
is diagnostic only.

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
2. **D-6's index line was never added** (above). Open; a one-line change to
   `index_generator.py` when the index is next regenerated for a reason of its own.
3. **The cross-reference table lists six forms; the pages use eight.** `→ 10,
   Part H` (number and letter) and `→ Part H, Part I` (two letters) appear in 6, 15
   and 19. They read correctly; add them to the table in `HANDOFF.md`, *How a
   cross-reference is written*.
