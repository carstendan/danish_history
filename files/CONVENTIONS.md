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

**Checked by.** The arrow sweep (`REVIEW-CONSISTENCY.md` §4).

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
am Barenberge against a German source finds 27 August or 6 September depending on
which state printed it.

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
across chapters but does not test intervals; the reading pass does.

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

**Checked by.** `vignettes.py` balance layer.

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

### D-13 · A vignette is the particular inside a general section — PROPOSED

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

**Needs.** Carsten's agreement. Once agreed, the six are decided under it in Part
G/H/E–F order as each part's review comes up.

### D-14 · Regnal numbers in the Danish style for Scandinavian rulers — PROPOSED, and already applied

**Rule.** Danish, Norwegian and Swedish rulers take the Danish ordinal: Christian
4., Frederik 7., Karl 12., Gustav 4. Adolf, Haakon 7. Other rulers take Roman
numerals: Frederick II of Prussia, George III.

**Reason.** It is what the book does — 409 Danish-style regnal numbers on the
pages at `c5775cf`, counted, not estimated — and it has never been written down. The review found seven Roman forms for Scandinavian kings in Parts G and I
and fixed them to the majority; five more are on pages 05, 07 and 10, which cannot
be rebuilt yet.

**Defined.** Here. Evidence in `REVIEW-CONSISTENCY.md` §2.1.

### D-15 · Place names — PROPOSED, needs Carsten (REVIEW-CONSISTENCY D-B)

**Rule as proposed.** *Schleswig* for the duchy and the region throughout; Danish
forms only where they are Danish words or names (*Sydslesvig*, *Slesvigsk Parti*,
*Sønderjylland*, *Flensborg Avis*). A town takes the form of the country it is in
today (Flensburg; Haderslev, Aabenraa, Sønderborg). The Skåne towns in their
Danish form in prose before 1658 and their Swedish form in visit blocks.
English exonyms where English has one in common use (Copenhagen, Jutland, Zealand,
Funen, the Sound). Viking-age kings under their English names, from Knud the Holy
under their Danish ones, as now.

**Reason.** The pages use the bare word Schleswig 105 times and Slesvig 129 (counted by
`sweep_names.py`'s reader at `c5775cf`), switching by
drafting session rather than by rule (§2.2 of the review), and the same drift runs
through Flensburg/Flensborg, Holstein/Holsten and the rest. An English-language book
whose chapter titles and index already say "Schleswig" should say it in the prose.

**Defined.** Here, once agreed. Applied part by part with each reading pass.

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
