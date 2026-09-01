# REVIEW — PART G

*Chapters 25–31, 1660–1814. Seven pages, 55,197 page words, 4.4 hours' reading.
Written to set up the review, not to conduct it: everything already known to be
wrong is listed here so the review does not spend itself rediscovering it, and the
things I think are actually weak are separated from the things that are merely
unfinished.*

---

## 0. Read this first: an error I made and did not catch by any guard

The Leonora Christina vignette said *Jammers Minde* appeared "a hundred and
eighty-four years after she wrote it". 1869 − 1674 is **195**. Worse, the
publication year is itself in the verification queue as 1867 or 1869, so a precise
interval should never have hung off it at all. Fixed — the interval is now "nearly
two centuries", which survives either date.

It is recorded at the top because it is the project's own standing rule failing in
a new place. *Compute numbers, do not type them* has been applied all session to
figure scripts, where the arithmetic is in code and gets checked. This number was
in prose, where nothing checks it. **Every derived interval in Part G's prose is
unguarded in the same way**, and the review should treat "N years after" and "N
years later" constructions as claims to verify rather than as connective tissue.

One other derived number is flagged in place: Wessel's age at Dynekilen is
twenty-five, computed from the draft's own "twenty-eight in December 1718". If that
is wrong both are.

---

## 1. What the review must decide, because I would not

Five things, each left alone because deciding would mean asserting something
unsourced or rewriting drafted argument.

**1.1 The ceiling bar in `figs_31.py`.** 27 + 15 = 42 under a caption reading 46
million rigsbankdaler. Four million is neither drawn nor labelled, and the bar has
no full-width track — unlike the "fallen to 6%" bar two blocks above it, which
does. So the figure reads as though 42 is the whole. Either name what the balance
was for, or give the bar a 46 m track so the shortfall shows.

**1.2 The schools figure in `figs_27.py`.** 241 built against 240 planned, then
"a thirteenth district on Møn from 1726, ten more schools". A reader adding up gets
250. The `aria-label` says 241 and never mentions Møn, so the spoken and visual
versions of the figure tell different stories.

**1.3 The Marie Grubbe vignette is in the wrong section.** It sits at the foot of
chapter 27 §05, Tordenskjold, but her scene is summer 1711 and what strands Holberg
at her ferry house is the plague — §04. With Wessel now in §05 that section carries
two vignettes and §04 none, one of them out of its own chronology.

**1.4 The 1788 mechanism is stated in halves in four places.** The ordinance settles
it and both drafted versions are half right: the band reverted to 14–36 at once,
those already too old or discharged got passes immediately, **and** a cohort was
released in each following year to 1800. `svg_band.txt` has the first half; §08, the
Summary and `svg_column.txt` have the second. What is actually wrong is
`STATE_G.md` §5's reason for dropping the cohort staircase. Fixing this means making
all four passages carry all three mechanisms.

**1.5 Chapter 28 at 46 minutes.** Inside the band, outside the advisory, longest in
the part by 1,400 words, and already a split candidate. Splits get two numbers at
plan time, so this is Part H's planning session.

---

## 2. Vignette balance — the part's weakest apparatus, and worse than recorded

All seven chapters carry three. `STATE_G.md` recorded one problem, chapter 29's
missing third. Auditing all twenty-one turns up two it did not.

**2.1 Chapter 25 has no woman as an agent.** Gersdorff, Nansen, the Amager farmers.
This is the same fault that chapter 26 had before Leonora Christina was promoted out
of prose, and nobody looked at 25. By the standing rule it is a blocking issue. The
chapter has candidates in its own material — the estates meeting is thick with
Copenhagen's burgher households, and the 1662 register runs on widows holding farms.

**2.2 Chapter 31 has three elite vignettes and no non-elite subject at all.**
Willemoes, a naval officer; Kamma Rahbek, a salon; Bourke, a diplomat at Kiel. This
is now the worst balance in the part — the position chapter 29 held before
Brahetrolleborg. The chapter covers a bombardment that destroyed about 300 buildings
and damaged 1,500, a currency that took every house in the realm as security, and a
school act for every child in the country. It is not short of ordinary people; it is
short of one written up.

**2.3 Chapter 28's confirmand is still the king.** Sophie Magdalene, Anders
Pedersen, Christian 6. on the Dovre descent — two elite to one peasant. Recorded in
`STATE_G.md` §2 and unresolved. A named confirmand from a parish register of 1736–40
would displace the king and fix it.

The part as a whole runs 7 women of 21, one per chapter except 25. Non-elite
subjects run to about 7 of 21, concentrated in 25, 27, 28, 29 and 30.

---

## 3. Apparatus gaps, deliberately left visible

**3.1 The glossary covers 53 of 68 sections.** ~~38 of 67~~ — **this figure in the
first issue of this brief was wrong, and the error was mine.** Glossary headers are
ranged (`§05–07 — the islands`), and `mkbody.py` read only the leading number, so
every ranged block was attached to its first section and the rest counted as
unglossed. Fifteen of the twenty-nine "gaps" were phantoms, and the same bug put
"Danish terms in this section" on blocks covering three. Parser and heading both
fixed; the part rebuilt.

Real coverage: 25: 5 of 9 · 26: 8 of 10 · 27: 8 of 9 · 28: 7 of 10 · 29: 7 of 10 ·
30: **10 of 10** · 31: 8 of 10. Chapter 30, which the first issue called an outlier,
is the only chapter with full coverage. **Chapter 25 at five of nine is the real
gap.** Whether an unglossed §01 is the opening-section convention is an open
question — it is unglossed in 25, 26, 28 and 29 and glossed in 27, 30 and 31, so it
is currently neither.

**3.2 The Summary runs to four items, not five, in chapters 25, 26 and 27.**
`ol.five` numbers with decimal-leading-zero, so those pages render 01–04 against
01–05 everywhere else in the book.

Neither was papered over. Inventing glossary entries or splitting a paragraph to
reach five would have hidden a drafting gap inside a built page, which is the
failure mode this project keeps finding.

---

## 4. Structure: one thing worth arguing about

**Chapter 30 breaks the part's chronological spine and reaches back into Part F.**
Its date range is 1620–1803, sitting between chapter 29 at 1770–1788 and chapter 31
at 1784–1814. A reader who has come forward through eight chapters arrives at 30 and
jumps back a hundred and fifty years, into a period Part F already covered in
chapters 22 and 23.

The thematic case for it is strong and the chapter makes it: the Atlantic is one
continuous institution and cutting it into three chronological pieces would destroy
the argument, particularly the cadastral thread that runs 25 → 26 → 29 → 30 and lands
in the three-surveys figure. But the reader experience is a jolt, and nothing in the
page prepares them for it. The cheapest fix is a sentence at the head of §01 saying
plainly that this chapter runs the length of the part and starts before it. The
index will show `1620 – 1803` against its neighbours regardless.

---

## 5. Figures — 24 built, 0 overruns, five deliberate divergences

Every figure validates as XML, passes the width guard at 6.1 and the new height
guard, and was rasterised and looked at. Five diverge from `PLAN_G.md` and each
says so in its script's docstring; the pattern is the same every time — **the planned
figure needed numbers the sources do not supply**. That is a good record and the
review should not treat the divergences as failures.

Worth a second look:

- **The battery arc in `svg_1807.txt` is now honest and nearly invisible.** It was
  drawn at 17 km radius against a siege line of about 8 km, four times too large and
  contradicting its own caption. Corrected to 8 km, which at this frame is 16 px. It
  now reads as a tight hook against the city — which is the true finding — but you
  may prefer to drop the arc and let the stage text carry it.
- **The plague figure has an unexplained colour.** The 1709 quarantine dot is green
  and the other nine indigo, with no key.
- **The 1660 map has two label collisions**, "Trondhjem" over "Jämtland" and
  "Helsingborg" over "Skåne". Not fixed; cosmetic but visible.
- **The village figure's six households** were drawn in five colours until this
  session, `VERD` appearing twice in `TONES`. Fixed, but it is the clearest example
  of a fault no guard could see: the figure's whole claim is "the same six
  households" and a reader counting colours got five.

---

## 6. Verification queue — still open

From `STATE_G.md` §3, unchanged by this session except where noted:

- **25** — the Kongelov's signature date of 14 November 1665 is disputed; sealing
  was 1669.
- **26** — Christian 5.'s hunting accident. Griffenfeld's mistress as Bielke's wife,
  resting on one DBL sentence. *Jammers Minde* published 1867 or 1869 — **now
  load-bearing for nothing, since the vignette's interval was removed**. Casualty
  proportion at Lund.
- **27** — the horses killed on the beach at Helsingborg; Marie Grubbe's third
  husband and what she told Holberg, which should rest on Holberg's letter and not on
  Jacobsen's novel.
- **30** — the St Jan rising began 23 November per the specialist literature and 13
  November per Danish Wikipedia.
- **31** — the Christiansborg fire of 1794 and the city fire of 1795; the 1807
  governing commission for Norway. **Add to this list**: "about 400 by recent
  research, about 1,600 by tradition" for the 1807 dead, which is a contested-numbers
  claim of the same shape as the plague tolls and was not in the queue.

Two dates that *were* in the queue are now closed and should come off it. The
Frederiksborg peace is 14 July 1720 Gregorian, 3 July Julian; the "3 June" in one
source is the **Treaty of Stockholm**, a separate Dano-Swedish instrument, as the
Treaty of Kiel's article 27 shows by naming both. The Slesvig homage is 4 September
1721 at Gottorp. One loose end: the Frederiksborg ratification, recorded as 23 July,
has not been checked for style and may be Julian, in which case it is 3 August.

---

## 7. What I think is strong, since a review brief that only lists faults is useless

- **The refusals.** Five figures declined to invent data and said so in their own
  docstrings. The plague figure in particular — showing four published tolls
  disagreeing rather than averaging them, and stating that nobody in the chapter has
  counted the bills — is the best thing in the part's apparatus.
- **The archive-asymmetry figure in chapter 30** closes on the right sentence: the
  asymmetry is not a gap in the archive, it is what the archive was for. That is the
  part's argument in one line.
- **The threads hold.** The cadastral thread lands where `STATE_G.md` §6 says it
  should. The two-monuments parallel between the Liberty Column and the 1792
  ordinance is made explicitly and is the sharpest thing in the part.
- **Hans Knudsen.** A man receives the hereditary title the Liberty Column
  commemorates and within five years sells it, and what he buys with it is his son's
  exemption from conscription. That is chapter 29's whole argument standing in one
  contract, and it came out of a parish history rather than out of the drafting.

---

## 8. Not for this review

`build_part_f.py` still says "lesson 10" against the renumbered `L10`; it is a
shipped Part F file. `figs_24.py` and Part F's four figure scripts have not been
re-checked under 6.1 or under the new height guard. Chapters 12–15 still carry the
old `--band` token. `danish-history-index.html` still uses the old
`band`/`entry`/`Era page` vocabulary. All are recorded in `HANDOFF.md`.
