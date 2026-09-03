# PLAN_H — Part H, chapters 32 to 36, 1814 to 1901

Status: agreed at plan time, not yet drafted. Plans are agreed before prose is
written; nothing below has been researched to draft standard, and every claim
marked **verify** is a claim to check before it reaches a page.

Supersedes nothing. `HANDOFF.md` remains the governing ledger; where this plan
and the ledger disagree, the disagreements are listed in §10 and the ledger is
the thing that gets corrected.

---

## 1. The length model

### 1.1 What was wrong with the old one

`PLAN_G` §1 gave `page words ≈ Σ(section bands) + 2,800`. That constant came from
Part F page counts taken **before** the `pagecount.py` fix. The fix removed SVG
label text, which is figure text and therefore apparatus, so it took its cut
almost entirely out of the constant rather than out of the narrative bands.

An intermediate estimate of 2,389 was computed during this session from
`PLAN_G`'s own Part F narrative figures. **That estimate was also wrong**, because
those narrative figures were themselves measured pre-fix and on a broader basis
than the one used here. Computing from unverified inputs is the same failure as
typing a number; the arithmetic was sound and the inputs were not.

### 1.2 What it actually is

Measured directly across the seven Part G pages with `narrative.py`, which
imports `pagecount.pagewords` rather than reimplementing it, selects the
narrative region positively (first numbered section heading to `div.myth`) and
lets everything outside that region fall into apparatus by construction:

| ch | sections | narrative | page | apparatus |
|----|----------|-----------|------|-----------|
| 25 | 9  | 3,204 | 6,650 | 3,446 |
| 26 | 10 | 3,931 | 7,311 | 3,380 |
| 27 | 9  | 3,258 | 6,803 | 3,545 |
| 28 | 10 | 5,470 | 9,086 | 3,616 |
| 29 | 10 | 3,928 | 7,328 | 3,400 |
| 30 | 10 | 3,455 | 6,881 | 3,426 |
| 31 | 10 | 3,940 | 7,683 | 3,743 |

Mean narrative 3,884 · mean page 7,392 · **apparatus 3,508**.

Apparatus is **47 per cent of a chapter**. Section topic count governs slightly
less than half a page's length. The rest is fixed cost: three vignettes ~697
words, glossary ~366, three figures ~285, checkpoints ~165, Meanwhile ~205, and
~1,677 of header, six terminal units, rail, contents and footer.

Independent check that the measurement is sound: chapter 31's outside-region
apparatus is 2,039 against ~1,620 elsewhere, a difference of 419 words. Chapter
31 is the only Part G chapter carrying the part coda. Nothing told the script so.

### 1.3 The bands

`PLAN_G` gave light 200–280, medium 400–500, heavy 600–700. **Thirty-four of the
sixty-eight measured Part G sections fall in the gaps between those bands.**
Observed spread: min 154 · p25 275 · median 365 · p75 483 · max 742.

Terciles from the measured data:

| band | range | mean |
|------|-------|------|
| light | under 318 | **240** |
| medium | 318 – 449 | **376** |
| heavy | over 449 | **576** |

"Heavy" at 576 sits below `PLAN_G`'s heavy band entirely. The old model predicted
heavier sections than anyone actually writes.

### 1.4 The model used in this plan

> **page words ≈ Σ(section bands) + 3,508**, at light 240 · medium 376 · heavy 576
> **minutes = page words ÷ 210**
> The chapter carrying the part coda adds ~419 words (~2 minutes).

Reference shapes:

| shape | narrative | page | min |
|-------|-----------|------|-----|
| 9 sections, 3L/4M/2H | 3,378 | 6,886 | 33 |
| 10 sections, 3L/4M/3H | 3,952 | 7,460 | 36 |
| 10 sections, 2L/4M/4H | 4,288 | 7,796 | 37 |
| 11 sections, 4L/4M/3H | 4,194 | 7,702 | 37 |

**Nine or ten sections is the Part H shape.** Eleven is available where a chapter
needs it and still lands inside the advisory.

---

## 2. Decisions taken at plan time

Six, taken in dependency order, all agreed before any section list was drawn.

**2.1 Thresholds.** Band 25–50 unchanged. **Advisory moves from 30–42 to 28–40.**
The old advisory was set when every measurement ran two to three minutes high, so
in true reading time it has been 28–40 all along. The restatement is
behaviour-neutral: chapters 21 and 28 flagged before and flag now, and nothing
else moves. A floor of 30 would flag chapter 17 at 29 minutes, which is a
deliberate six-section chapter defended in the ledger — a false positive on a
settled decision, and false positives are how `debuild` became ignorable.

**2.2 Splits.** Chapter 21 (47 min) and chapter 28 (43 min) are both **retired as
split candidates**. Halved they give 23 and 21 minutes, both under the floor, so
splitting either is not division but a commitment to write ~5,000 new words into
a shipped and verified part. Chapter 28's candidacy rested on topic count, not
length (open item 20); it has ten sections, which is the standard heavy shape in
Part G — 26, 29, 30 and 31 all have ten. It is not exceptional on the metric its
candidacy rested on.

Chapter 32 was held open until its section list was drawn. Drawn, it lands at ten
sections and 37 minutes, inside the advisory. **32 stays one chapter.** The book
remains 43 chapters; Part H is 32–36; nothing renumbers.

**Recorded for the ledger:** chapter 28's apparatus is normal (3,616 against a
mean of 3,508). Its narrative is 5,470, thirty-nine per cent above any other
chapter in the part, at a mean of 547 words a section against ~380 elsewhere. It
is not over-sectioned; it is written heavy in every section. That is chapter 21's
signature exactly, and it is the third instance of L1's "vary the weight, not
just the count" — and the first time it has been measured rather than inferred.

**2.3 Where the Slesvig question is assembled.** Five of the seven arrows into
Part H promise the same thing. The full legal case — Ribe 1460, the two legal
orders, the Kongelov's female line against Holstein's agnatic succession, and the
1721 blank — runs to roughly 1,500 words and cannot be built three times.
**Chapter 33 assembles it.** Chapter 32 states the condition without arguing the
law. Chapter 34 spends the assembled case and carries a back-arrow to 33.

**2.4 The 1864–1901 Slesvig hole.** Chapter 26's arrow promises Jyske Lov holding
in Sønderjylland until 1900, a terminus inside Part H's span, in a part that as
originally scoped had no chapter discussing Slesvig after the war.
**Chapter 35 takes a Nordslesvig section** — its 1870–1901 span fits exactly and
its subjects (association-building, emigration, popular organisation) are what the
Danish minority was doing under German rule in the same decades. Chapter 34 stays
at one year; Part I is not asked to absorb a debt it cannot yet promise to pay.

**2.5 The insolvent `15 → 36` arrow.** Chapter 15's carry-forward promises the
sale of the West Indies and points at chapter 36, which is Provisorietiden and
cannot carry it. Open item 12 records the correct target as `→ 30, Part I` and
records it as unfixable because Part D has no retained bodies.
**Resolution: edit chapter 15's built page directly.** The back-port rule exists
because `mkbody.py` regenerates bodies downward and destroys artifact-only edits.
Chapter 15 has no body and no generator, so there is nothing upstream that could
destroy the edit. This is the one case where editing a built page is safe.
Conditions: assert on the match count before writing, grep for the new string
after, re-run `debuild.py verify` on chapter 15 (expect `identical`), close open
item 12. `linkindex.py` does not need re-running — the page is edited in place,
not rebuilt.

**2.6 Vignette balance.** `vignettes.py` reports rosters, place counts and
repeated surnames. It does not check gender or class; both ledger claims about
chapters 25 and 31 came from a hand audit in `REVIEW-PART-G.md` §2, not from the
tool. Its place check is exact-string and reports Copenhagen five times when the
true figure, counting variants, is **thirteen of forty-eight**.

Adopted:
- **Convention D-9.** The vignette `(who)` line gains a trailing bracket:
  `person · place · date · [f][n]` — `f` where a woman is the agent, `n` where the
  subject is non-elite, both omitted where neither applies. Two flags only; a
  third turns tagging into an argument rather than a check.
- **Backfill is lazy.** The forty-eight existing vignettes are tagged as each part
  is next touched. The balance layer reports `untagged` for 16–31 until then.
  Tagging them now from one-line roster summaries would mean asserting class and
  gender from a summary, which is the inference this project has been burned by.
- **The place check is normalised** so that variants of one place count as one.

---

## 3. The debt table

Taken from a census of the bodies, not from the ledger. `HANDOFF.md`'s debt
section covers arrows opened by Part F; **Part G's own forward arrows were not in
any ledger**, and `census_g.py`, which the ledger says does this in one pass, is
not in `files/`. The census below was run directly over `c25`–`c31`.

**Seven arrows into Part H, not the five the handover listed.** Chapters 29 and 31
each carry a `→ Part H` that appeared in no record. That is the Part F census
failure repeating — twelve recorded where the files carried sixteen — and it is
the second time the same lesson has paid for itself.

| from | what it promises | paid in |
|------|------------------|---------|
| 19 | Ribe 1460, *up ewig ungedeelt*, to 1848, 1864 and 1920 | 32 §01 as condition; 33 §02 as argument; 1920 to Part I |
| 21 | the 1544 partition produces the Glücksburg line and a king from it in 1863 | 33 §02, 34 §01 |
| 25 | absolutism has no mechanism for changing its mind — the problem taken to 1848 | 32 §06, 33 §03 |
| 26 | one code that could not cross the Kongeå; Jyske Lov in Sønderjylland to 1900 | **used** in 33 §02, **paid** in 35 §10 |
| 27 | whether the Kongelov's female-line succession ran in Slesvig — the legal origin | 33 §02 |
| 29 | the 1788 tie ends with universal conscription in 1848; towns exempt to 1849 | 33 §05 |
| 31 | the German-speaking share rises to about two fifths; Slesvig becomes the only question | 32 §01 |

**Chapters 28 and 30 open nothing into Part H.** Part I already carries two debts,
from 30 and 31, before it is planned.

**Chapter 35 inherited no arrow at all.** Part G's own argument set up its
ancestry and never pointed at it: the freeholders created by the 1788 reforms are
chapter 29's subject and the cooperative movement's grandparents. **35 carries a
`← 29`.** If the connection is to be made from both ends, chapter 29's body needs
an arrow added and back-ported to `PART_G_DRAFT.md` before any Part G rebuild —
recorded in §10, not done here.

---

## 4. Vignette roster for the part

Fifteen vignettes, balance checked at plan time rather than at review.

| ch | § | who | place | date | tags |
|----|---|-----|-------|------|------|
| 32 | 03 | Peter Larsen Skræppenborg | a farmhouse near Kolding | early 1840s | `[n]` |
| 32 | 05 | Johanne Luise Pätges, later Heiberg | Det Kongelige Teater | 1826 | `[f][n]` |
| 32 | 09 | Peter Hiort Lorenzen | the Slesvig estates assembly | 11 Nov 1842 | — |
| 33 | 03 | Orla Lehmann | the Casino, Copenhagen | 20 Mar 1848 | — |
| 33 | 05 | *a named conscript* — **needs a source** | Fredericia | 6 Jul 1849 | `[n]` |
| 33 | 06 | Mathilde Fibiger | Thoreby, Lolland | Dec 1850 | `[f]` |
| 34 | 01 | Christian 9. | Copenhagen | 18 Nov 1863 | — |
| 34 | 04 | Niels Kjeldsen | near Vorbasse | 28 Feb 1864 | `[n]` |
| 34 | — | Ilia Fibiger — **verify** | a military hospital | 1864 | `[f]` |
| 35 | 03 | *a founder at Hjedding* — **needs a source** | Hjedding, Vestjylland | Jun 1882 | `[n]` |
| 35 | 09 | Olivia Nielsen | Copenhagen | 1901 | `[f][n]` |
| 35 | 10 | H.P. Hanssen | Aabenraa | 1898 | — |
| 36 | 07 | Julius Rasmussen | Copenhagen | 21 Oct 1885 | `[n]` |
| 36 | 08 | Line Luplau — **verify place** | Varde | 1889 | `[f]` |
| 36 | 10 | J.C. Christensen | Stadil, Vestjylland | 1901 | `[n]` |

**Balance: five women, seven non-elite. No chapter without at least one of each.**
Four of fifteen in Copenhagen, against a running rate of thirteen in forty-eight.

**Rejections, recorded so they are not re-proposed:**
- *Louise Rasmussen, Countess Danner* (33) — `[f][n]` and vivid, rejected on L3.
  Part G already ran Vibeke Kruse and Caroline Mathilde; a third woman defined by
  her position beside a king is the beat repeating across a part boundary. She
  goes in prose at 33 §01.
- *Christian 9. in 1901* (36) — a good bookend to his 1863 vignette, rejected
  because `vignettes.py` flags repeated people for a reason and the part is
  stronger ending on a schoolteacher. He gets the moment in 36 §10's prose.

**Two better vignettes exist if they can be sourced**, and would displace the
named holder:
- A young man leaving Nordslesvig to avoid Prussian military service (35) — it
  would serve §06 and §10 in one person, and displace H.P. Hanssen. The police
  emigration registers may supply a name.
- A named woman of the *gudelige forsamlinger* (32) — would fix the geography and
  the class balance at once and displace Heiberg. The names are in local parish
  and court records. **Archive task; not blocking.**

---

## 5. Chapter 32 — Golden Age and national awakening, 1814–1848

| § | section | weight |
|---|---------|--------|
| 01 | The realm that was left | light |
| 02 | Paying for the war | medium |
| 03 | The awakening in the parishes | heavy |
| 04 | Grundtvig | medium |
| 05 | What the Golden Age was for | heavy |
| 06 | Four assemblies, 1831–1835 | heavy |
| 07 | The countryside gets rich | medium |
| 08 | Bondevennerne | medium |
| 09 | Two nations in one duchy | heavy |
| 10 | The Open Letter, 1846 | light |

**2L / 4M / 4H → 4,288 narrative + 3,508 → 7,796 → 37 minutes.**

**§01** pays chapter 31's arrow and adds what 31 could not: Holstein entering the
German Confederation in 1815, Lauenburg acquired in exchange for Swedish
Pomerania. The realm now has a province inside another country's constitutional
order, and that fact is the whole part.

**§02** does not re-run the bankruptcy — chapter 31 §07 has 5 January 1813. This is
the aftermath: Rigsbanken becoming Nationalbanken in 1818, the deflation, and the
agricultural crisis of 1818–28 that broke estates the boom of §07 then rebuilt.

**§03 and §04 stay separate.** The lay awakening is a popular movement with
non-elite agents; Grundtvig is one man, censored individually from 1826. Merging
them would make the awakening a preamble to a famous name, which inverts what
happened. This is L2's religion at real weight and it is where the chapter's
non-elite subjects live.

**§05 must be an argument, not a canon.** The risk is a list of names. The
argument available: a bankrupt state that had just lost a third of its territory
produced Oehlenschläger, Eckersberg, Thorvaldsen, Ørsted, Andersen and
Kierkegaard, through a small number of state institutions funded by a treasury
that could not pay its debts. The Golden Age was subsidised.

**§06** pays chapter 25's arrow. Lornsen's pamphlet of November 1830 opens it; four
advisory assemblies follow — Roskilde and Viborg for the kingdom, Slesvig and
Itzehoe for the duchies, all consultative. The structural point is that the
constitutional question and the national question are given the same institution
to argue in, which is why they become one question.

**§09 states the condition; it does not argue the law.** Language rescripts of
1840, Hiort Lorenzen refusing German in 1842, *Danmark til Ejderen*, the
Slesvig-Holsten movement, Rødding folk high school opening in November 1844 near
the language boundary. Two national movements forming against each other, both
convinced they are defending something that already exists.

**Where this differs from the standard account.** Two of ten sections go to
religion. Most popular accounts give the awakening a paragraph and the Golden Age
three chapters. The weighting here holds that a movement which put tens of
thousands of ordinary people into farmhouse meetings, and got them prosecuted for
it, did more to shape what Denmark became than Thorvaldsen did. **That is a
position, not a fact**, and it should be visible as one.

**Figures**
- (a) **Spine map 1814** — the realm after Kiel, with Holstein and Lauenburg drawn
  inside the German Confederation boundary. The Confederation outline is a new
  element and `mapfixture.py` needs curated cases for it, minimum three per
  territory. Heads the chapter.
- (b) **Four assemblies, 1834** — seat counts and franchise thresholds for
  Roskilde, Viborg, Slesvig and Itzehoe side by side, from the ordinances. Not a
  map, per L4. Two Danish and two German bodies with the same powers and no power.
- (c) **The price of a tønde of rye, 1815–1848** — one series from the published
  price statistics, the collapse to 1828 and the recovery. Carries §02 and §07
  together, and no prose in the chapter can do it.

The Slesvig language-boundary map is deliberately **not** here; it belongs in 33
where the case is assembled.

**Meanwhile** — Paris, July 1830, with Lornsen's pamphlet four months downstream ·
The Corn Laws repealed in 1846, the market §07's boom was already selling into.

**Myth-check** — that the Golden Age was a flowering of national confidence. It
runs alongside a state bankruptcy, the loss of Norway, a decade of agricultural
collapse, and the lifetime censorship of its most famous preacher.

**Glossary (10)** — guldalder · gudelige forsamlinger · Konventikelplakaten ·
folkehøjskole · Ejderpolitik · slesvig-holstenisme · Det åbne Brev ·
Bondevennernes Selskab · Nationalbanken · sprogreskript.
`stænderforsamling` is glossed in chapter 25 — reference, do not re-gloss. `fæste`
and `selveje` need checking against Parts F and G before §07 uses them.

**Carry-forward** — `← 31` the settlement of 1814 and the German share · `← 19`
Ribe 1460 as condition · `← 29` the freehold peasantry §07 and §08 are built on ·
`→ 33` the assemblies, the Open Letter, both national movements · `→ 35`
Grundtvig's school idea and the grain economy · `→ 36` Bondevennernes Selskab and
what becomes of it.

**Closes on** — the Open Letter of 8 July 1846 as an object, and Christian 8. dead
on 20 January 1848 with nothing settled. Eighteen completed months, computed; per
D-8 both dates go on the page and the interval does not.

---

## 6. Chapter 33 — 1848: constitution and the First Schleswig War, 1848–1852

| § | section | weight |
|---|---------|--------|
| 01 | A king with no heir | light |
| 02 | *Up ewig ungedeelt* — what Slesvig legally was | heavy |
| 03 | March 1848 | heavy |
| 04 | The war begins | medium |
| 05 | The soldier's war | medium |
| 06 | 5 June 1849 | heavy |
| 07 | A church for the people | medium |
| 08 | Isted, 25 July 1850 | medium |
| 09 | The London Protocol, 1852 | medium |
| 10 | What the constitution could not cover | light |

**2L / 5M / 3H → 4,088 narrative + 3,508 → 7,596 → 36 minutes.**

**§02 is the assembly point and the chapter's biggest bet.** Four inherited arrows
land in one heavy section: Ribe 1460 and *up ewig ungedeelt* (`← 19`); the two
legal orders, Slesvig a fief of the Danish crown and Holstein a fief of the Empire
and from 1815 a member state of the German Confederation; the 1665 Kongelov
allowing female-line succession in the kingdom against Holstein's agnatic
succession, so that a childless Frederik 7. sends the two territories to two
different men; and Slesvig as the blank, left unclear in the homage instruments of
1721 (`← 27`), with the inheriting Glücksburg line descending from the 1544
partition (`← 21`).

**Where this differs from the standard account.** Most popular treatments give the
dynastic law a paragraph and foreground the clash of nationalisms. This gives it a
full heavy section, because 1864 is unintelligible without it: the great powers do
not go to war over sentiment, and Denmark loses in 1864 because it breaks a legal
settlement, not because it offends German feeling.

Chapter 26's arrow — Jyske Lov holding in Sønderjylland to 1900 — is **used** here
as evidence that Slesvig was legally distinct and **paid in 35 §10**, where its
terminus falls. Two chapters must not both discharge it.

**§03** puts both revolutions in one section: the Casino meeting of 20 March, the
deputation of the 21st, Frederik 7. accepting a national-liberal ministry — and
the provisional government proclaimed at Rendsburg on the 24th. Absolutism ends in
Copenhagen and the duchies rise in the same week for opposite reasons. Splitting
them would let a reader think one caused the other in sequence.

**§05** pays chapter 29's arrow: the tie of countrymen to their birthplace,
transferred to the state in 1788, ends with universal conscription in 1848, and
town-dwellers stay exempt until 1849. The war is fought by the men the 1788
ordinance had bound.

**§07 is the section most accounts skip.** The 1849 constitution created *den
danske folkekirke* and granted religious freedom, ending a state church monopoly
running since 1536 — chapter 20's settlement, undone here. L2's religion, and the
reason §06's "democracy" claim needs qualifying: the document that excluded most
of the population from voting was genuinely liberating in a different dimension.

**§08 and §09 are the chapter's real argument.** Isted was the largest battle
fought in Scandinavia to that date and Denmark won it. The London Protocol then
settled the war on terms Denmark had not won: the powers guaranteed the monarchy's
integrity, designated Christian of Glücksburg as heir, and required that Slesvig
not be bound to Denmark more closely than Holstein. A military victory converted
into a legal trap.

**Figures**
- (a) **Two lines and a blank column** — a descent diagram from Frederik 3.: the
  kingdom's cognatic line to Glücksburg, Holstein's agnatic line to Augustenborg,
  Slesvig's column empty. The blank is the argument.
- (b) **The language boundary in Slesvig** — from a named nineteenth-century survey
  with surveyor and date on the face of the figure, because these surveys were
  themselves instruments of the argument. The figure must show it is a claim.
- (c) **Who could vote in 1849** — total population, adult men, men over thirty,
  independent householders, actual electorate. From the census and the electoral
  law.

Forms: genealogy, map, proportion. L4 holds.

**Meanwhile** — Paris, February 1848: Denmark's March Days fall inside the same
eight weeks as Paris, Vienna and Berlin, and Denmark is the only one where the
king hands power over and keeps his throne · Frankfurt, September 1848: the Malmö
armistice ratified by a parliament that had claimed Schleswig-Holstein as its
first act of foreign policy and could not enforce anything.

**Myth-check** — that the Three Years' War was a Danish victory. It was won in the
field and settled by the great powers on terms that left the central question open
and made 1864 possible.

**Glossary (11)** — *up ewig ungedeelt* · agnatisk og kognatisk arvefølge ·
helstat · ejderstat · Grundloven · Rigsdagen, Folketinget, Landstinget ·
folkekirke · Martsministeriet · provisorisk regering · Londonprotokollen ·
treårskrigen.

**Carry-forward** — `← 19` `← 21` `← 25` `← 27` `← 29` `← 32` · `→ 34` the
Protocol, the designated heir, the question still open · `→ 36` two chambers with
different franchises · `→ Part I` the seven categories the 1849 franchise excluded
and when each of them ends.

**Closes on** — the war cemetery at Flensburg, and the men buried there in 1850, in
a town that will be on the other side of a border in 1864. Both years named, no
interval stated: Isted to the Vienna peace is fourteen completed years but the
London Protocol to Vienna is twelve rather than the thirteen a reader gets by
subtraction. D-8 applies across the section.

---

## 7. Chapter 34 — 1864, 1863–1864

| § | section | weight |
|---|---------|--------|
| 01 | A king three days on the throne | light |
| 02 | Why the powers did not come | medium |
| 03 | Dannevirke, 5–6 February | heavy |
| 04 | Dybbøl | heavy |
| 05 | The London Conference | medium |
| 06 | Als, and Jutland occupied | medium |
| 07 | Vienna, 30 October | medium |
| 08 | Two hundred thousand Danes | heavy |
| 09 | The constitution of 1866 | medium |
| 10 | What was to be won inward | light |

**2L / 5M / 3H → 4,088 narrative + 3,508 → 7,596 → 36 minutes.** Length is
governed by topic count, not span; a one-year chapter at the same weight as a
thirty-four-year one is the rule working, not an anomaly.

**Where this differs from the standard account.** The familiar shape is Dannevirke
and Dybbøl as national trauma, then a coda. Here the battles get three sections
and about a third of the chapter — enough for what happened and not enough for the
mythology. §08 and §09 get a heavy and a medium, because **the 1866 revision is
usually a footnote** and it rewrote the Landsting's franchise to privilege large
landowners, which is the direct mechanism of Provisorietiden. Chapter 36 is
unintelligible without it, and placing it here shows 1864 as a domestic
constitutional cost as well as a territorial one.

**§01** — Frederik 7. dies 15 November 1863; Christian 9. signs the November
Constitution on the 18th, three days later, knowing it breaches the settlement of
1852. A Glücksburg king designated by the powers, breaking the powers' own terms
in his first week. Pays `← 21` and `← 33` in one scene.

**§02 makes the rest make sense.** Denmark had breached the London Protocol;
Prussia and Austria moved first as executors of the German Confederation and then
on their own account; Britain would not act alone, Russia had no interest, France
wanted something in return. **No one came because Denmark had put itself in the
wrong.** That is harder to tell a Danish reader than betrayal, and it is what the
documents support.

**§08** — around two hundred thousand Danish-speakers pass under Prussian rule; the
optant question opens; Article 5 of the Peace of Prague promises a North Slesvig
plebiscite in 1866 and is abrogated in 1878. **All population and territory
figures must be computed from the 1860 census and the treaty text**, not carried
from secondary accounts. This is where typed numbers would be easiest and worst.

**§10** — Dalgas, the Heath Society founded in 1866, and the phrase about what is
lost outward being won inward. **Verify the attribution**: it is usually credited
to Dalgas and appears to originate with H.P. Holst.

**Figures**
- (a) **Spine map 1864** — before and after the cession, shared frame and
  projection. `mapfixture.py` needs curated cases for the new border.
- (b) **What was ceded** — area, population and share, before and after, from the
  1860 census and the Vienna treaty.
- (c) **The Dybbøl redoubts** — the ten positions and the bombardment record.
  **Contingent on sourcing.** If the daily rounds-fired figures cannot be got from
  the published siege record, this becomes a comparison of the two armies' rifles
  and artillery, which is sourceable and explains the outcome without appealing to
  fate. Per the standing rule, a figure is built only from sourceable numbers.

**Meanwhile** — Geneva, 22 August 1864: the first Convention signed while this war
is still being settled, proposing what §04 and the third vignette are about · the
last year of the American Civil War, and the country a generation of Danes is
about to leave for.

**Myth-check** — de Meza. He abandoned the Dannevirke without a fight on the night
of 5–6 February, was vilified as a coward and dismissed within days, and the
retreat saved an army that would otherwise have been destroyed in a position it
could not hold in that winter. He never recovered his reputation and it was the
correct decision.

**Glossary (10)** — Novemberforfatningen · forbundseksekution · Dannevirke ·
skanse · optant · Wienerfreden · Pragfredens artikel 5 · Den gennemsete Grundlov ·
Hedeselskabet · dannebrogsmand.

**Carry-forward** — `← 19` Ribe 1460, spent at last · `← 21` the Glücksburg line
and the king it produced · `← 33` the Protocol and the question left open ·
`→ 35` the two hundred thousand, the heath, the emigration · `→ 36` the Landsting
the 1866 revision created · `→ Part I` Article 5 abrogated in 1878, and the
plebiscite that finally happens.

**Closes on** — the Isted Lion, raised over the graves at Flensburg in 1862, taken
down after the cession and carried to Berlin. Chapter 33 closes at that cemetery;
this closes with the monument being removed from it.

---

## 8. Chapter 35 — Industry, cooperatives, emigration and labour, c. 1870–1901

| § | section | weight |
|---|---------|--------|
| 01 | Two chapters over one span | light |
| 02 | The grain that stopped paying | medium |
| 03 | Hjedding, 1882 | heavy |
| 04 | Butter, bacon and the English breakfast | medium |
| 05 | Mission and meeting-house | heavy |
| 06 | Leaving | medium |
| 07 | The city outside the walls | medium |
| 08 | Fælleden, 5 May 1872 | heavy |
| 09 | 1899 | medium |
| 10 | Nordslesvig under Prussia | heavy |

**1L / 5M / 4H → 4,424 narrative + 3,508 → 7,932 → 38 minutes.** The longest in
Part H, with two minutes' headroom.

**Overrun valve, named in advance.** This chapter carries four subjects and an
imported fifth. If the draft overruns, **§07 is the section to cut** — Danish
industry proper belongs as much to Part I as here, and losing it brings the
chapter to 36 minutes without touching the argument.

**§01 opens the 35/36 overlap and says so**, as chapter 30 §01 now does: the two
chapters run over the same thirty years and divide by subject, this one taking the
country and the next the politics.

**§02–§04 are one causal chain in three sections.** World grain prices collapse
from the later 1870s under American and Russian competition; Danish farms stop
selling grain and start selling what they can feed grain to; the cooperative dairy
is the institution that lets small farmers do it. The mechanical enabler is the
cream separator and the market is Britain.

**§05 is L2's religion and it is not decoration.** Indre Mission and
Grundtvigianism divided the Danish countryside — different meeting-houses,
different schools, often different cooperative societies in one parish. The social
geography of the cooperative movement runs along that line. Folk high schools
flourish here, with Askov founded in 1865 as successor to Rødding, left on the
wrong side of the border. That closes chapter 32's school arrow with the war in
between.

**§08 and §09 are the labour arc** — Pio, Brix and Geleff, the International, the
Fælled meeting broken up on 5 May 1872 and the arrests that followed; then the
party, the unions, the federation of 1898, the lockout of 1899 and the September
Compromise that ended it and still frames the Danish labour market. Women's
organising belongs in §09, not in a section of its own.

**§10 is decision 4 arriving.** It pays chapter 26's arrow at its 1900 terminus and
takes the aftermath 34 hands on: the optants and Article 5 abrogated in 1878; *de
hjemløse*, children of optants born in Slesvig and left without citizenship; the
language ordinances; *Flensborg Avis* and *Hejmdal*; the Køller policy from 1898.
It sits last because it is the thread Part I picks up directly, and because ending
there rather than on a Danish success is the honest shape.

**Figures**
- (a) **Grain and butter, 1870–1901** — two price series crossing, from the
  published Danish price statistics. Carries §02 to §04 in one image.
- (b) **Emigration by year, 1868–1901** — from the Copenhagen police emigration
  registers, which are close to complete and are the right source rather than an
  estimate.
- (c) **How a cooperative was owned** — a structural diagram: who supplied, who
  owned, how milk was paid for, one member one vote regardless of herd size.

**Mild L4 tension, stated:** (a) and (b) are both time series; (c) is deliberately
a different form to break that. If a third series creeps in during drafting, one
of them becomes a map.

**Meanwhile** — Berlin, 1883–1889: Bismarck's insurance laws, and the Danish
old-age relief act of 1891 that follows the argument rather than the model · the
American plains, and what the emigrants of §06 actually found.

**Myth-check** — that the cooperative movement was classless. It was a movement of
freeholders. The *husmænd* and the *tyende* were largely outside it, and the
one-member-one-vote rule that made it egalitarian among members drew a hard line
around who counted as one.

**Glossary (11)** — andelsbevægelse · andelsmejeri · brugsforening · centrifuge ·
husmand · tyende · Indre Mission · valgmenighed · optant · Septemberforliget ·
Køllerpolitikken.

**Carry-forward** — `← 26` paid at its 1900 terminus · `← 29` the freeholders the
1788 reforms made · `← 32` Grundtvig's school idea, the grain economy,
Bondevennerne · `← 34` the two hundred thousand, the heath, the emigration ·
`→ 36` the cooperative farmers as an electorate and the party founded on the
Fælled · `→ Part I` the plebiscite that answers §10, and a labour settlement that
outlasts the century.

**Closes on** — a child born in Nordslesvig to optant parents and holding no
citizenship at all: Danish by descent, Prussian by birthplace, recognised by
neither.

---

## 9. Chapter 36 — Provisorietiden and the change of system, 1875–1901

| § | section | weight |
|---|---------|--------|
| 01 | Two chambers, two countries | light |
| 02 | The question nobody had answered | medium |
| 03 | Estrup | heavy |
| 04 | Ruling without a budget, 1885 | heavy |
| 05 | The gendarmes | heavy |
| 06 | A wall around Copenhagen | medium |
| 07 | 21 October 1885 | light |
| 08 | The other opposition | medium |
| 09 | The settlement of 1894 | light |
| 10 | 1901 | heavy |

**3L / 3M / 4H → 4,152 narrative + 3,508 + 419 part coda → 8,079 → 38 minutes.**

**This chapter carries Part H's coda** and must be planned with the ~419 words
included, not have them discovered at build. Chapter 31 is the precedent.

**On the weight profile.** The first version of this list came out 1L / 6M / 3H.
It was discarded. Six mediums is a flat chapter — chapter 28's fault wearing
different clothes: not uniformly heavy but uniformly middling, with no section a
reader can move quickly through and none that opens out. The version above has
three genuinely short sections and four carrying real weight.

**§01 spends chapter 34's arrow.** From 1872 Venstre holds the Folketing and Højre
holds the Landsting, and the two chambers represent two different countries.

**§02 is the real subject.** The 1849 constitution never said whether a ministry
answers to the king or to the Folketing. Christian 9. read it one way, Venstre the
other, and both readings were defensible from the text. The nineteen-year conflict
is a gap in a document.

**§04 must not caricature Estrup.** The provisional laws had a textual basis in the
constitution's emergency provision, and he used it in a way it was plainly never
meant for. Both halves need saying; the section is weaker if he is a
straightforward usurper.

**§05 is where the conflict stops being parliamentary** — the light-blue gendarmes
posted into villages, press prosecutions, restrictions on the rifle clubs, the
boycotts. L2's countryside, and the section a reader will remember.

**§06 is the thing the fight was about.** The fortification of Copenhagen was built
by provisional law while the Folketing refused to fund it. The constitutional
crisis was, underneath, a defence-spending argument.

**§08 carries L2's religion** alongside the Social Democrats entering the Folketing
in 1884 and the women's suffrage association of 1889. Venstre's rural base was
substantially Grundtvigian and made heavy use of the free-congregation law of
1868, while the state church hierarchy sat with Højre. The religious split and the
political one ran along much the same line.

**Figures**
- (a) **Two chambers, two electorates** — the Folketing and Landsting franchises
  side by side, from the electoral laws. The chapter's central fact in one image.
- (b) **Seats against votes, 1872–1901** — Venstre's Folketing majority against
  Højre's Landsting control across the conflict. The deadlock as a structure
  rather than a clash of two men.
- (c) **The Vestvold** — the fortification ring built by provisional law, with its
  cost. A plan rather than a chart, and still standing, so it feeds the visit
  block directly.

**Meanwhile** — Berlin, 1862–1866: Bismarck governed Prussia without an approved
budget on a reading of a constitutional gap, and the man who took Slesvig is the
model for the man who ruled Denmark by decree · Kristiania, 1884: Norway
establishes parliamentary government seventeen years before Denmark, by
impeaching a ministry rather than waiting one out.

**Myth-check** — that 1901 gave Denmark parliamentary government. It established it
as practice, and it was not written into the constitution until 1953, where this
book ends. For fifty-two years the rule everyone obeyed had no text behind it.

**Glossary (10)** — provisorisk lov · finanslov · Provisorietiden ·
parlamentarisme · Højre · Venstre · gendarm · Vestvolden · Forliget 1894 ·
Systemskiftet. `Landstinget` and `Folketinget` are glossed in chapter 33 —
reference, do not re-gloss.

**Carry-forward** — `← 32` Bondevennernes Selskab, 1846 · `← 33` two chambers with
different franchises · `← 34` the revision of 1866 · `← 35` the cooperative farmers
as an electorate and the party founded on the Fælled · `→ Part I` women's suffrage
and the constitution of 1915 · `→ Part I` the Social Democrats from four seats to
government.

**One arrow cannot be written yet.** The myth-check points at 1953, when
parliamentarism is finally written down. That is beyond Part I and under D-1 needs
a part letter, which does not exist until the later parts are planned. Open item,
§10.4.

**Closes on** — the ministry list of 24 July 1901: a professor of law at its head
and a parish clerk from a Vestjylland village holding the church and education
portfolio. The first Danish government with no great landowner and no royal
favourite in it.

---

## 10. Open items

### 10.1 Needs an archive, a library or a reader — not blocking the plan

- **33 §05** — a named conscript at Fredericia, 6 July 1849, from the published
  Three Years' War letter collections.
- **35 §03** — the Hjedding founder's name, from the society's own founding record
  rather than a secondary account.
- **34** — Ilia Fibiger's 1864 service and the specific hospital. She dies in 1867,
  so the window is narrow.
- **36 §08** — whether Line Luplau's campaigning in Varde is documented. If not,
  the vignette is Copenhagen, which would put five of fifteen there.
- **36 §07** — the detail about the bullet stopped by a button, against the trial
  record rather than the retelling.
- **34 §10** — the attribution of the phrase about what is won inward.
- **32, optional** — a named woman of the *gudelige forsamlinger*, from local parish
  and court records. Would displace Heiberg and improve both geography and class
  balance.
- **35 §06/§10, optional** — a named young man leaving Nordslesvig to avoid Prussian
  military service, from the police emigration registers. Would displace Hanssen
  and serve two sections in one vignette.

### 10.2 Ledger corrections found by the cold run

- `svg_plague_1711.txt` is missing and **has** a generator. Run `figs_27.py` and
  commit. Chapter 27's page is fine — the SVG is inline — but `files/` cannot
  currently rebuild it.
- **Ten** Part D figures have no generator, not eight: ch12 dioceses, reigns,
  terr_1050 · ch13 baltic, leding, terr_1250 · ch14 descent, pawn · ch15
  arithmetic, reconquest.
- Chapters **12–15 report `identical`, not `style-only`**. The split is 01–11
  `style-only`, 12–15 `identical`, which means `style.css` still carries `--band`
  unrenamed and `build_part_e.py` still asserts on it.
- **Part E and F word tables in `HANDOFF.md` are pre-fix.** Chapter 21 is listed at
  10,218 words / 49 min; it is 9,619 text, 9,812 page, 47 min. Open item 14's claim
  that those tables record `text` is itself wrong — chapter 24 is listed at 7,014
  against a text count of 6,394.
- **Chapter 28 appears as 46 (item 20), 43 (counter table) and 44 (handover).** It
  is 43.
- **"Delete `c16_body.html`" is now dangerous.** After the renumbering, 16a and 16b
  became chapters 16 and 17, and `c16_body.html` is the live chapter 16 body that
  `tidy.py` reports present. Following that line would delete a working source. The
  companion instruction, deleting the stale
  `16-margrete-i-and-the-kalmar-union.html`, is already done.
- **`census_g.py` does not exist** in `files/`, though `HANDOFF.md` says it does the
  arrow census in one pass. The Part H census in §3 was run ad hoc.
- **`pagewords.py` sits beside `pagecount.py`** and is unclassified by `tidy.py`.
  Probable superseded duplicate; finding 5's warning applies.

### 10.3 Two defects in shipped bodies

- **Chapter 29, vignette 2 is malformed.** The heading reads `**Vignette · Johann
  Friedrich Struensee, Christiansborg, before dawn on 17` — truncated mid-date and
  carrying literal `**`. The `date` field has swallowed a sentence about Caroline
  Mathilde's arrest and `opens` reads `January 1772**`. The page round-trips, so
  nothing automated will catch it. Something in `c29_body.html` has a line break
  inside the vignette heading.
- **Chapter 23, vignette 1 has no place.** Ellen Marsvin's `place` field reads
  `1629`, and it appears in the place census as a location.

Neither is Part H's work. Both belong in the ledger.

Cosmetic: four Meanwhile summaries in `vignettes.py` output terminate at a regnal
ordinal — a first-sentence splitter breaking on the period in "Christian 4." and
the like, not damaged prose. Low priority: maps 1600 and 1660 both sweep exactly
3,108 land points, probably a shared envelope, worth one glance.

### 10.4 Decisions deferred

- **The forward arrow to 1953** from chapter 36's myth-check has no part letter,
  because the parts after I are unplanned. It must be assigned when they are.
- **Chapter 29 needs a `→ 35` added** and back-ported to `PART_G_DRAFT.md` before
  any Part G rebuild, so that 35's inheritance is stated from both ends.

### 10.5 Tooling, before the first Part H build

1. `narrative.py` — anchor `START` on the numbered section heading. The first
   `<h2>` is the five-questions block, and it is currently counted as narrative in
   every chapter, about 113 words each.
2. `vignettes.py` — add the D-9 balance layer and normalise the place match so
   variants of one place count as one.
3. The advisory constant moves from 30–42 to **28–40** in `build_all.py` and the
   five `build_part_*.py` scripts.
4. `figs_27.py` re-run and committed.
5. Chapter 15's arrow edited in the built page per decision 2.5 — assert on match
   count, write, grep for the new string, re-run `debuild.py verify`, close item 12.
6. `index_generator.py`'s vocabulary still says `band`, `entry` and `Era page`
   where the series says part and chapter. Pre-existing, unchanged by this plan.

**Build sequence remains** build → `linkindex.py` → `index_generator.py` → upload.

---

## 11. Standing rules this plan was drawn under

- Compute numbers, do not type them. Every length figure here came from a script
  and the apparatus constant was measured, not inherited. Two estimates were wrong
  before the measurement — one in `PLAN_G`, one made during this session.
- Verify before writing. Every **verify** mark in §10.1 is a claim that would
  otherwise reach a draft on trust.
- Rasterise and look at every figure. Three Part G faults were invisible to every
  automated guard and visible in one glance.
- A curated test case can name the right place and test nothing. The 1814 and 1864
  spine maps need curated cases for their new borders, minimum three per territory.
- Assert on every scripted replacement, then grep for the new string.
- Figures are built only from sourceable numbers. 34's third figure is explicitly
  contingent on sourcing and has a named fallback.
- Vary the weight, not just the count. 36's first section list was discarded for
  being uniformly medium.
