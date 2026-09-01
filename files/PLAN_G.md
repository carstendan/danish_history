# PART G — PLAN, v19 · settled

**The absolute state, 1660–1814.** Chapters 25–31, seven pages.

All decisions closed. **[v5]** applies the vignette roster check against Parts E and F
(`vignettes.py`), which forced changes in chapters 25, 26, 28 and 29 and added two
carry-backs. Earlier v4 marks retained where they explain a choice. Page count frozen by this document, per Lesson 1b.

---

## 1. Why seven

The case rests on one ground. Two others were offered in earlier drafts and are
withdrawn: the Lesson 1 ceiling does not bite (eleven sections at these bands is
nine substantial plus two light; the lesson bars twelve substantial), and the
headroom argument is thin (six pages at 39 minutes leaves three minutes, and a
missing subject costs 400–700 narrative words, which is roughly three minutes).

**The Danish Atlantic will not slice.** Its arc runs 1620 to 1803, its weight falls
after 1733, and it has no clean decade seam — the company's charter, the Crown's
buy-out, the plantation boom and the ordinance sit across four of the six
chronological chapters and belong to none. `22 → 27` already promises it a chapter.
Once it has its own page, seven is subtraction, not judgement:

| | sections |
|---|---|
| total topic count, 1660–1814 | 64–69 |
| the Atlantic chapter | 10 |
| **residue, over six chronological chapters** | **54–59 → 9.0–9.8 each** |

Which is Part F's demonstrated shape. The other six fall out at nine and ten
sections without being forced.

### The length model

Apparatus is close to fixed per chapter and does not scale with section count.
Measured on Part F:

| ch | sections | narrative | page | apparatus |
|---|---|---|---|---|
| 21 | 9 | 7,137 | 10,218 | 3,081 |
| 22 | 9 | 4,383 | 7,104 | 2,721 |
| 23 | 10 | 4,350 | 6,957 | 2,607 |
| 24 | 10 | 4,020 | 7,014 | 2,994 |

Chapter 21's overrun is entirely narrative — 793 per section against 402–487 —
which is why including it lifts page-words-per-section from 727 to 823. Neither
figure is wrong; words-per-section is the wrong unit.

> **page words ≈ Σ(section bands) + 2,800**

**Cost of the seventh page.** Twelve forward arrows move; nine move on merit
regardless, so the marginal cost is three. The rebuild it forces on Part E retires
open item 5a — the seam still inlined in shipped 16–19 — at no extra cost. Book
total becomes 43, inside `HANDOFF.md`'s own 43–45 projection.

---

## 2. Chapter allocation

**Weight bands** — narrative words, excluding vignettes, glossary blocks, figure
captions, checkpoints and terminal apparatus:

| band | words |
|---|---|
| light | 200–280 |
| medium | 400–500 |
| heavy | 600–700 |

Nine-section shape: 2 light · 4 medium · 3 heavy → ~4,230 narrative → ~7,030 page.
Ten-section shape: 2 light · 4 medium · 4 heavy → ~4,880 narrative → ~7,680 page.

Reading times at 210 wpm, confirmed against Part F (208.5–213).

| # | title | span | sections | words | min |
|---|---|---|---|---|---|
| 25 | The kingdom made hereditary | 1660–1670 | 9 | ~7,000 | 33 |
| 26 | Law, rank, and the war for Skåne | 1670–1699 | 10 | ~7,700 | 37 |
| 27 | The last war for the Sound | 1699–1721 | 9 | ~7,000 | 33 |
| 28 | The bound countryside and the pious state | 1721–1770 | 10 | ~7,700 | 37 |
| 29 | Struensee, and the village taken apart | 1770–1788 | 10 | ~7,700 | 37 |
| 30 | The Danish Atlantic | 1620–1803 | 10 | ~7,700 | 37 |
| 31 | The flourishing trade and the wreck of it | 1784–1814 | 10 | ~7,900 | 38 |

~52,700 words, ~252 minutes. Chapter 31 includes the part coda (~350 words) via
`tail_extra`.

**Part colour** `--indigo:#2F4C7A`. Add to `style.css`. `build_part_g.py` must raise
on a missing token as `build_part_e.py` does, not no-op as ABC and D still do.

### Ordering **[v4 — settled, see D-7]**

The Atlantic chapter follows the reform chapter. The reader meets Reventlow,
Bernstorff and Schimmelmann in office in 29, freeing the peasant in June 1788, and
then meets the same men's other ledger in 30, abolishing the trade in March 1792
with a delay the planters used. Chapter 29 closes on the husmand who got nothing;
chapter 30 opens by asking the same question at a larger scale, and carries a `← 29`.

---

## 3. The chapters

Per chapter: three vignettes, two meanwhile boxes, three checkpoints, three figures,
9–12 glossary blocks, the countryside and religion (Lesson 2), a named woman with
agency (7a).

### 25 · The kingdom made hereditary, 1660–1670

| § | section | weight |
|---|---|---|
| 01 | The city that had just survived | light |
| 02 | The estates meet, 10 September 1660 | heavy |
| 03 | Hereditary, then absolute | heavy |
| 04 | The Kongelov, 14 November 1665 | medium |
| 05 | Colleges instead of a council, amter instead of len | medium |
| 06 | The land written down — matriklen, hartkorn, ryttergods | heavy |
| 07 | The council disappears | light |
| 08 | A church of royal officers | medium |
| 09 | What the fortress cost | medium |

Does not re-run the siege; that is chapter 24's, and 25 opens after it.

**§06 links forward to 26 §02. [v9]** Christian 5.'s rank system of 1671 set the
threshold for a count at 2,500 tønder hartkorn and for a friherre at 1,000. The unit
this chapter invents to price a farm is the unit the next chapter uses to price a
nobleman. Neither chapter has to reach for the connection; it is simply the same number.

**§06 corrected. [v6 — research]** 1662 and 1664 did **not** survey anything. The
Landgildematrikel of 1662 covered every property in the kingdom except Bornholm and
worked by converting the tenants' many kinds of landgilde into a single unit, hartkorn;
it was full of errors and was redone on the same principles as the Amtstuematrikel of
1664. The section's argument is therefore not measurement but *reduction* — the new
state's first act was to render every farm in the kingdom as one comparable number —
which is sharper than the survey framing and makes figure (c) carry the section exactly,
since the arithmetic on the page **is** the conversion. Units for the figure and
glossary: one tønde hartkorn = a tønde of rye or barley, or two of oats; 8 skæpper to
the tønde, 4 fjerdingkar to the skæppe, 3 album to the fjerdingkar. It was the official
basis of Danish land valuation from 1662 to 1903.

**Bornholm is left out of the 1662 register** — the island that had just handed itself
to the crown in chapter 24. One sentence, and a `← 24`.

**§04, from research. [v7]** The drafting chain: constitutional clauses first appear once
generalfiskal Søren Kornerup (1624–1674) is consulted, in a short Latin draft titled
*Lex Regia Frederici Tertii*; the final wording is Frederik 3. working with his
kammersekretær Peder Schumacher, later Griffenfeld, who returns in chapter 26. Denmark
is the only absolutist state to give itself a written constitution, and why is
guesswork — the håndfæstning tradition is the usual explanation. Apart from the
succession, the ruler's confession and the realm's indivisibility, the law placed no
real limit on the king at all.

**Hedge (Lesson 8):** the sealing did not happen until 1669, and the signature date of
14 November 1665 is disputed — some have argued it antedated; this is generally
rejected, and there is no decisive proof either way. Say so, since the date is in the
section title.

**Two source errors found, recorded so they are not re-imported.** The Lex article on
the Kongelov states that Frederik 3. signed it on his birthday; he was born 18 March
1609. The same article says it was first read aloud at Christian 5.'s anointing in 1670;
Frederik 3. died in February 1670 and the anointing was at Frederiksborg Slotskirke on
7 June 1671. Both would have gone onto the page unchecked.

**The actual survey moves to 26** — see the cadastral thread at 30.

**§02's trigger, from research. [v8]** The deadlock is over a stamp duty falling on the
burghers alone. Copenhagen's mayors refused on **7 October** to publish the ordinance;
Nansen put the hereditary-kingdom proposal to the burgher representatives on **8
October**. The constitution arrives the day after a tax revolt by the city's
magistrates. The nobility had already refused equal taxation at the joint meeting of 19
September, where rigsråd Otte Krag told Nansen that nobody prescribes anything to the
nobility.

**Carry-forward opened. [v8]** The burghers' own earlier programme included abolishing
*vornedskab* and *ægt*. Vornedskab is abolished in 1702 — chapter 27. `→ 27`.

**§05 rebuilt from research. [v9]** The section was thin and is now two halves of one
act. **The centre:** Statskollegiet by instruction of 18 November 1660, with
Skatkammerkollegiet, the Kancelli, Krigskollegiet and Admiralitetskollegiet under it,
their presidents sitting in it; Højesteret in final form February 1661, its composition
specified as **half noble, half learned and burgher, all appointed by the king
himself**; Kommercekollegiet 1668. Statskollegiet is abolished in 1676, absorbed into
the Gehejmekonseil with Griffenfeld as its secretary — which hands to 26. **The
provinces:** the ordinance of **19 February 1662** stripped the lensmænd of their
authority; the len became amter under royal amtmænd. Without this the chapter has no
account of how the new state reached past Copenhagen.

**Krigskollegiet was created in 1658, two years before the coup.** The college system
therefore predates absolutism, which is a better and truer story than colleges simply
replacing a council: the machinery was already being built during the war, and 1660
finished it.

**Gabel opens the section. [v9]** Not the originator of the revolution but the chief
intermediary between Frederik 3. and the estates; enriched, ennobled, governor of
Copenhagen 1664, and the most influential man at court from 1660 to 1670. His father
was a cartographer who became recorder of Glückstadt and was killed at the siege there
in 1628. The man who brokered absolutism was a mapmaker's son — in a chapter whose
figure is a land register. He and Schumacher are the two commoners who knew about the
Kongelov; §05 and §07 are the same argument, and the closing object completes it.
Gabel died 13 October 1673.

*Unreliable source noted:* roskildehistorie.dk has Gersdorff and Christian Rantzau both
dying in 1663. Gersdorff died 19 April 1661.

**Vignettes. [v6 — dated and re-anchored from research]** Hans Nansen, borgmester ·
Copenhagen's rådhus, then the burgher estate · **8 October 1660** — the day the
magistrat adopted his hereditary-kingdom proposal, after which he and bishop Hans Svane
carried it to their two estates, which adopted it at once. v5 had him on 8 September,
which is a month early: that was the date the deputies were ordered to appear ·
Joachim Gersdorff, rigshofmester · the great hall, Copenhagen Castle · **10 September
1660**, and again 13 December · **[v8] the Amager farmers fetched to swear for the
peasant estate · the square between Copenhagen Castle and the Børsen · 18 October 1660**.

**The third vignette, replaced. [v8]** The matrikel widow is dropped: her name would
have to come out of the scanned 1664 register parish by parish, and the absence would
have carried no argument. The Amager farmers do. The fourth estate was not invited to
the meeting at all; at the homage a small group was called in at the last minute so
that it could be said the whole Danish people had made the king their hereditary lord;
and the Enevoldsarveregeringsakt of 10 January 1661 was signed over the winter by
representatives of every estate **except** the peasantry. Fetched to swear aloud in
October, not asked to sign in January.

**This is where 9a is spent.** The men are unnamed because nobody thought four-fifths
of the population worth recording — the absence *is* the argument, which is the false
Oluf precedent. It follows that chapter 30's *Fredensborg* captive must be named from
the ship's papers or replaced, since two uses in one part is one too many, and there
the namelessness is a fact about the archive rather than a point the chapter is making.

**Gersdorff is stronger than v5 assumed and needs the fuller arc.** He negotiated
Roskilde — chapter 24's treaty — and lost his own Scanian estates by it. He opened the
estates meeting on the king's behalf and in his presence, blaming the war on the
officers and on supply failure while praising the king's vigilance and Copenhagen's
loyalty. In October the king made him rigsdrost and president of Statskollegiet, the
top post in the machinery that replaced his own office. On 13 December a royal letter
ordered him to have Statskollegiet work out how a register of the realm should be
arranged — so the vignette hands straight into §06. He was dead on 19 April 1661. `← 24`.

**Not to be used without a real source:** English Wikipedia states his wife Øllegaard
Huitfeldt and a servant were convicted of poisoning him. Danish sources say he died
after an illness and mention only rumour. Leave it out unless it can be sourced.

**Sophie Amalie moves to prose. [v5]** She was v4's second vignette and would have
been the sixth court woman manoeuvring near a throne in nine chapters — Part F ran
that beat five times (Sophie of Mecklenburg, Johanne Tommesis, Vibeke Kruse, Dina
Vinhofvers, Leonora Christina) — and she would have stood at Copenhagen Castle, where
chapter 24 already put Dina Vinhofvers.

**7a rests on her, in §01. [v8]** Her conduct through the siege drew agreed praise —
she and the king refused to leave the city and showed themselves in the streets — and
that is undisputed. Her role in the coup is not. The chapter uses the same woman at two
evidential standings and says which is which, rather than dropping her or overclaiming
her.

**Her hedge, settled. [v6 — research]** This is not a vague "historians disagree". The
tradition that she drove the king toward absolutism rests on Copenhagen hearsay
collected by the English envoy Robert Molesworth around 1690 — late, second-hand,
hostile — and Danish historians formerly credited her as the moving force without real
evidence. What is not in doubt is her conduct during the siege, which drew agreed
praise. The character assassination is Leonora Christina's and took hold after *Jammers
Minde* was published in 1869. Naming the channel is a better Lesson 8 hedge than naming
a disagreement, and it sets up chapter 26.

**Figures.** (a) **Spine map 1660** — the realm Part G inherits; heads the chapter.
(b) **Where a decision travelled** — rigsråd routing against college routing, one
question, two paths. (c) **One village's hartkorn** — a rendered 1664 matrikel entry
with the arithmetic exposed.

**Meanwhile.** The Restoration in England, 1660 · Louis XIV takes personal rule, 1661.

**Myth-check.** That absolutism was seized. It was voted, by the two estates with
least to lose.

**Glossary (10).** stænderforsamling · arvekongedømme · enevælde · Kongeloven ·
håndfæstning (and its end) · kollegium · matrikel · hartkorn · ryttergods · rigsråd.

**Closes on** the Kongelov as an object, with the detail research supplied. **[v7]** Two
original parchments in Schumacher's hand, gold seals, silver caskets — one now in the
Rigsarkiv, one at Rosenborg. Kept so close that on contemporary accounts only two men
knew it existed before Frederik 3.'s death: Christoffer Gabel, the king's confidential
intermediary during the coup, and Schumacher, its author and keeper — **both of
non-noble birth**. The constitution that ended the nobility's power was known to two
commoners. When it was finally published on 4 September 1709 under Frederik 4., the
whole text was reproduced as copperplate engraving in a folio of 500 copies, given away
and not for sale. A law engraved rather than typeset, in an edition nobody could buy.

---

### 26 · Law, rank, and the war for Skåne, 1670–1699

| § | section | weight |
|---|---|---|
| 01 | A king who crowned himself | light |
| 02 | Rank instead of blood — the ordinance of 1671 | medium |
| 03 | Griffenfeld | heavy |
| 04 | The law and the land written down, 1681–88 | heavy |
| 05 | The war to take Skåne back, 1675–79 | heavy |
| 06 | Køge Bugt, 1 July 1677 | medium |
| 07 | The snaphaner in the Göinge woods | medium |
| 08 | Making Skåne Swedish | medium |
| 09 | The Blue Tower | heavy |
| 10 | Fontainebleau, and Munkholmen | light |

**[v6] §04 absorbs the land survey.** Christian 5.'s Store Matrikel, in force 1688, was
built from scratch on a measurement of all cultivated land in 1681–83 — every field
measured, its area calculated, its soil graded — **on a Swedish model**, which in a part
that opens with half the kingdom lost to Sweden is not a neutral fact. Merging it with
Danske Lov 1683 and Norske Lov 1687 keeps the chapter at ten sections and makes one
argument instead of two: this reign writes everything down, the law and the ground.

*Vignette candidate, not taken:* the 1681 instruction required four peasants per herred,
experienced in the soil, to accompany the surveyors and assess the land on oath. It is
the best non-elite countryside vignette available in 26, and the chapter has none. Not
taken because the three slots are full and the Göinge priest carries a debt. If
Griffenfeld at his desk underperforms in draft, this replaces him.

**Third vignette resolved. [v12]** The Göinge priest is out and Örkened is prose,
not a vignette: an anonymous Örkened who-line would have been a second use of 9a, and
chapter 25's Amager farmers hold the part's allowance. The slot goes to **Svend
Poulsen** — named, documented, and better than the legend. He lost Lundbygård in 1673
over tax arrears assessed in chapter 25's hartkorn, was commissioned major on 13 July
1676 at about sixty-eight, went to Skåne to recruit, fell ill that November and
disappears from the record. `← 25`.

**Vignettes. [v11 — dated from research]** Peder **Schumacher**, not yet Griffenfeld ·
Copenhagen · **25 May 1671** — the rank order, the Gemaksordinans and the counts' and
barons' privileges were all issued on that one day, so this is a single act of design,
not a drafting scene. He was ennobled that July, two months after writing the ladder he
then climbed. The 1671 ordinance listed 55 offices and named persons, and the old
nobility of birth did not appear in it at all — the commoner inventing a nobility, which is the chapter's argument
rather than its most famous anecdote · Leonora Christina writing · Blåtårn · 1674 · a
Skåne parish priest ordered to preach the Swedish liturgy · a named parish in Göinge ·
1680s *(to verify)*.

**Dates settled. [v11]** He became **rigskansler in June 1674**, on Peter Reedtz's
death, and president of Højesteret with it — not 1673. The widely repeated 1673 is the
26 November ennoblement (count of Griffenfeld, knight of the Elephant) with the office
folded into it; the office was occupied until Reedtz died. Arrested on the morning of
11 March 1676 at Copenhagen Castle, condemned, reprieved at the block, four years in
Kastellet, then Munkholmen until 1698. Died 12 March 1699, buried at Vær church near
Horsens.

**Two chains back to 25. [v11]** He married Karen Nansen, granddaughter of the mayor,
in 1670; she died in childbirth at sixteen in 1672. And in March 1674 he bought Samsø
from Jørgen Bielke — his mistress's husband, and the husband of Magdalene Sybille
Gersdorff, Joachim Gersdorff's daughter, who had inherited the island from her father's
estate. Both of chapter 25's commoners are tied to him by household. `← 25`.

**Chapter 25's Meanwhile boxes are now load-bearing. [v11]** Schumacher was in England
at the Restoration in 1660 and in France when Louis 14. took personal power in 1661. The
man who wrote the Kongelov watched both of the events chapter 25 sets beside 1660, in
person, as a student. 25's boxes should name him; 26 §03 picks it up.

**Why the block is out. [v5]** Part F burned Johanne Tommesis at Køge (22) and
executed Dina Vinhofvers outside Copenhagen Castle (24). Griffenfeld reprieved at the
block would have been the third scaffold vignette in six chapters, and chapter 29 had a
fourth. His fall goes in prose, where the chapter ends at Munkholmen regardless.

**Leonora Christina appears twice in the series, deliberately.** Chapter 24 has her at
Malmö in 1659, its who line already reading *seventeen months' imprisonment, and not
her last* — an unwritten carry-forward this chapter pays. She is the only person with
two vignettes, which is defensible only if the beats differ: 24's is endurance, she
follows and is held. **26's must be authorship** — the act of making the book that
outlives everyone in it. If the vignette shows her enduring again, cut it and carry her
in prose and the cell-plan figure instead.

**Figures.** (a) **The Scanian theatre** — Denmark-scale detail map. (b) **The same
offence, 1241 and 1683** — one named offence and its penalty under Jyske Lov and
under Danske Lov, side by side, with what changed and what did not. Reaches back to
Part D. *(Offence chosen in research; fallback is the convergence figure — four
provincial codes and the town laws collapsing into one jurisdiction.)* (c) **A room,
measured** — the Blue Tower cell to scale, with its dimensions.

**Meanwhile.** Vienna besieged, 1683 · the Edict of Nantes revoked, 1685.

**Myth-check.** Svend Poulsen as Carit Etlar wrote him. Hedge the snaphane record;
the Danish and Swedish traditions do not agree and the chapter says so.

**Glossary (11).** rangforordning · greve · friherre · Danske Lov · Norske Lov ·
snaphane · försvenskning · Blåtårn · Jammersminde · kaperi · uniformitet.

**Closes on** the window at Munkholmen, and what Griffenfeld could see from it. A place.

---

### 27 · The last war for the Sound, 1699–1721

| § | section | weight |
|---|---|---|
| 01 | Travendal, 1700 — out in three months | light |
| 02 | Poltava changes the arithmetic, 1709 | medium |
| 03 | Helsingborg, 10 March 1710 | heavy |
| 04 | The plague, 1711 | heavy |
| 05 | Tordenskjold | medium |
| 06 | The Gottorp share taken, 1713–1721 | heavy |
| 07 | Frederiksborg, 1720 — the Sound kept, Skåne not | medium |
| 08 | Two hundred and forty schoolhouses | medium |
| 09 | Egede sails, 3 May 1721 | light |

§03 dated New Style per D-6. **§07 discharges a carry-back to 23:** chapter 23
argued that Sweden's Sound-toll exemption at Brømsebro made the toll negotiable
rather than a fact of geography. Frederiksborg abolished the exemption. `← 23`.

**Vignettes.** Peter Tordenskjold · Dynekilen · 8 July 1716 · Gertrud Rask ·
Håbets Ø, Greenland · summer 1721 · Marie Grubbe at the ferry house, and the student
Holberg who sheltered there in the plague year · Borrehuset, Falster · summer 1711
*(verify Holberg's own account and its date)*.

Marie Grubbe earns the slot on merit, not as the required woman: born to the highest
nobility, twice divorced under a law chapter 26 has just explained, ending as a
ferryman's wife. She crosses the whole social distance the series describes.

**[v5] Tordenskjold is the weakest of the three and is flagged, not cut.** Chapter 23
put Christian 4. aboard *Trefoldigheden* at Kolberger Heide, and chapter 31 puts
Willemoes on a floating battery — three sea vignettes in the run. Dynekilen survives
because it is a raid up a fjord against a supply convoy rather than a fleet action, and
because the other two are a king watching and a boy of seventeen. If it reads as a
third at review, the replacement is a Gottorp official handing over the duchy in 1721.
Gertrud Rask against Jens Munk in Hudson Bay (22) is a near miss that holds: Munk is
death and failure, Rask is arrival and staying.

**Figures.** (a) **Spine map 1721** — royal Slesvig entire, Gottorp still in Holstein
until 1773, Greenland `CLAIM` → `DEP`. (b) **The burial weeks of 1711** — Copenhagen
interments by week from the parish bills. (c) **Two hundred and forty, in six years**
— the school build-out by year, the standard cost, and the cavalry-district revenue
that paid.

Two quantitative figures and no artefact, deliberately: a city losing a third of
itself in 1711 and a school in 240 parishes by 1727 are the same state, counted
twice, ten years apart. The prose puts them against each other rather than leaving
the juxtaposition to the figures.

**Meanwhile.** Poltava, 8 July 1709 · the South Sea Bubble, 1720.

**Myth-check.** Tordenskjold at Marstrand, and the beer barrels.

**Glossary (11).** kaper · orlogsskib · lægd · pesthus · dødeliste · rytterskole ·
det gottorpske · stadfæstelsestraktat · missionær · Håbets Ø · gammel og ny stil.

**Closes on** the burial ledger's total for one Copenhagen parish. A number, and a cost.

---

### 28 · The bound countryside and the pious state, 1721–1770

| § | section | weight |
|---|---|---|
| 01 | A king who closed the theatres | light |
| 02 | The parish under pietism — 1735, 1736, 1737 | heavy |
| 03 | Stavnsbånd, 1733 — and why | heavy |
| 04 | A week of hoveri | heavy |
| 05 | The cattle plague | medium |
| 06 | The Brethren | medium |
| 07 | How Norway was governed and what it sent south | heavy |
| 08 | Holberg's Copenhagen, and the fire of 1728 | medium |
| 09 | The loosening, 1746 | medium |
| 10 | A state that could not price its own grain | light |

§07 discharges the apparatus half of 22 → 30: the 1604 law, the stattholder,
Kongsberg and Røros, the timber, the regiments.

**Vignettes. [v16 — resolved]** Christian 6. on the Dovre descent, 16 July 1733,
replaces the confirmand. Reasoning below.

**Why the confirmand was dropped.** It cannot be named from published sources. Parish registers record confirmands from 1736, but the
transcriptions online run 1737–1891 without isolating the first cohort, and inventing a
plausible name is exactly the failure this part has been avoiding. Three ways out, in
order of preference:

1. **Arkivalieronline.** One parish register, one page, one name and her father's name
   and farm. This is a ten-minute lookup for someone with the site open and it would
   give the part its best possible vignette: the first Danish generation legally
   required to be examined on 759 questions before being counted an adult.
2. **Change the subject to Norway.** The part has no Norwegian face in any of its
   vignettes so far, and §07 is the section that most needs one — a Kongsberg miner or
   a farmer under the hauling obligation.
3. **Change the subject to the bond.** §03 is the chapter's most famous subject and
   has no person in it.

Not an option: a second use of 9a, which chapter 25 holds.

**What was chosen, and its cost.** Option 1 needs Arkivalieronline and option 2 needs a
Kongsberg roll — both are archive lookups, not searches. The one Norwegian subject that
is fully documented and inside the span is the royal progress of 1733: four months and
eleven days, 3,270 km, 188 people, a surviving journal printed in 1992, and the Dovre
descent recorded as the most dangerous stage. It binds §01, §03 and §07 in one image —
the king who closed the theatres, in the year he bound the peasantry, on a road worked
by men under the hauling obligation.

**The cost is that chapter 28 now has two elite vignettes** (Sophie Magdalene and
Christian 6.) against one peasant. That is the weakest balance in the part and it should
be recorded as such. At part level the roster still holds — the Amager farmers, Svend
Poulsen, Marie Grubbe, Anders Pedersen, the *Fredensborg* captive, the gårdmand and the
schoolteacher are all non-elite. If the Arkivalieronline lookup is ever done, the
confirmand should displace Christian 6. ·
**Sophie Magdalene · Vallø · 28 November 1737** — founded that day, inaugurated 14 May
1738; twelve stiftsfrøkener, sixteen quarterings required until 1799, her own sister
installed as abbess on 16,600 thalers while the queen was writing to the king asking
him to send that sister home because she believed her a rival. Caroline Mathilde took
the protectorate in March 1771, which hands to 29 · **Anders Pedersen, farmer · Ørsted, Oksenvad sogn,
Haderslev Amt · about 1750** — he kept a notebook through the cattle plague, printed in
Poulsen and Biehl Hansen, *Med egen hånd: Optegnelser fra Fladsten og Ørsted 1592–1809*
(1994), with the Ørsted evidence studied in *Sønderjydske Årbøger* 102 (1990). A named
non-elite Danish farmer writing in his own hand inside the disaster — the best
non-elite vignette in the part so far, and it needs no 9a provision.

**Why Pontoppidan is out.** Part F 21 opens with Peder Palladius in a Zealand village
church, quoting his own *Visitatsbog*. v4 had Pontoppidan examining a parish, quoting
his own catechism — the same man in the same room with the same source-type, seven
chapters later. The vignette becomes the child being examined instead, which is also
the better history: the novelty of 1736 is not that a bishop tests a parish but that
the state now requires every person in the country to be tested on a book. Pontoppidan
stays in prose and in figure (c).

**Why the lægdsrulle boy is out.** With the confirmand in, he became the second
fourteen-year-old written into a register in the same chapter. He survives as the
chapter's closing object, which is where he was always strongest.

*Name collision, noted not fixed:* Sophie Magdalene here and Sophie of Mecklenburg in
22. Different beats — an endowment against a manoeuvre — and both are real. Write each
with her full style on every mention.

**[v14] A thread back to 25.** Sophie Magdalene's posthumous reputation — the cold
German princess turned extravagant queen — was made by Dorothea Biehl, writing for the
Copenhagen bourgeoisie's emerging nationalism and published in the wake of 1864. That
is the same mechanism chapter 25 identifies behind Sophie Amalie's blackening: a
hostile later account serving a later politics, read since as fact. Two queens, two
posthumous demolitions, both by writers with a national argument to make. The chapter
should say so, and 25's hedge should point forward to it. `← 25`.

**Figures.** (a) **A bound man's year** — calendar wheel, hoveri days against the
farm's own work, from a surviving hoverireglement. (b) **Norway, what it sent** —
Norway-scale detail map: mines, sawmills, regiments, stiftamtmænd. (c) **Question
447** — a spread of Pontoppidan's *Sandhed til Gudfrygtighed*, one question and
answer in full. Now one of only two document renderings in the part; substitute
(cattle-plague herd counts) stays available if it reads as a repeat at review.

**Meanwhile.** Lisbon, 1 November 1755 · the Seven Years' War Denmark bought its way
out of, 1757–62.

**Myth-check.** That stavnsbånd was serfdom. It was not, and the difference is the
chapter's argument.

**Glossary (12).** stavnsbånd · hoveri · fæste · fæstebrev · godsejer · herregård ·
pietisme · konfirmation · katekismus · Brødremenigheden · stiftamtmand · kvægpest.

**Closes on** the lægdsrulle entry binding a named boy of fourteen to an estate he
had not chosen. An object.

---

### 29 · Struensee, and the village taken apart, 1770–1788 **[v4 — moved from 30]**

| § | section | weight |
|---|---|---|
| 01 | A sick king and his doctor | medium |
| 02 | Sixteen months of cabinet orders | heavy |
| 03 | Caroline Mathilde, governing | heavy |
| 04 | 17 January 1772 | heavy |
| 05 | Guldberg's Denmark, and indfødsret 1776 | medium |
| 06 | The commission, 1786 | medium |
| 07 | Udskiftning | heavy |
| 08 | 20 June 1788 | medium |
| 09 | The column, 1792–97 | light |
| 10 | Who was left out | light |

**[v4]** §05–06 now carry the sole introduction of Reventlow, the Bernstorffs and
Schimmelmann-in-office. Under the old order both this chapter and the Atlantic
chapter had to set them up; that duplication is gone, and the words go to the
ordinance instead.

**Vignettes. [v5 — second changed]** Caroline Mathilde · Hirschholm · summer 1771 ·
Johann Friedrich Struensee arrested · Christiansborg, before dawn · 17 January 1772 · a
named gårdmand at the udskiftning of his village · a named sogn · 1780s *(to verify
from a surviving udskiftningskort)*.

**The execution moves to prose**, for the reason given at 26: it would have been the
fourth scaffold vignette in six chapters. The arrest is the stronger scene anyway.

**Caroline Mathilde must be shown governing**, not in the romance. Part F's dominant
register is the woman near the throne, and she is a candidate to become the sixth
instance of it. The vignette shows her transacting state business — signing, ordering,
receiving — or it is cut.

**Figures.** (a) **One village, twice** — strips before, star pattern after, from a
real 1780s enclosure map. (b) **The column, read** — the Frihedsstøtten with one
face's inscription in full and translated. (c) **Freed by year of birth** — the
staircase by which stavnsbånd released in cohorts to 1800, the fact the prose most
reliably gets wrong.

**Meanwhile.** Philadelphia, 1776 · Paris, 1789.

**Myth-check.** Struensee and Caroline Mathilde as a romance rather than a
government; and the 1,069 orders, a number that circulates without its denominator.

**Glossary (11).** kabinetsordre · trykkefrihed · indfødsret · landbokommission ·
udskiftning · stjerneudskiftning · selveje · fæstebonde · husmand · gårdmand ·
Frihedsstøtten.

**Closes on** the husmand not named on the column, and the acreage he did not get.
A cost — and the question chapter 30 opens by asking again.

---

### 30 · The Danish Atlantic, 1620–1803 **[v4 — moved from 29]**

| § | section | weight |
|---|---|---|
| 01 | Before the Atlantic — Trankebar 1620, the Gold Coast 1661 | medium |
| 02 | St Thomas, 1672 | medium |
| 03 | The triangle, in tons and in people | medium |
| 04 | The crossing | heavy |
| 05 | St Jan, November 1733 | heavy |
| 06 | St Croix bought, 1733 | light |
| 07 | The law of the plantation | heavy |
| 08 | The Crown takes the islands, 1754–55 | medium |
| 09 | What the sugar built in Copenhagen | light |
| 10 | The ordinance of 16 March 1792 | heavy |

§01 carries the `← 29` hinge: the chapter opens on the question chapter 29 closed on,
asked at a larger scale.

**[v5] §05 carries a second carry-back, `← 24`.** Chapter 24's Jens Kofoed leads an
island rising against a distant power and the series tells it as a liberation. Breffu's
rising on St Jan is the same beat and must not be allowed to arrive as an accident: the
chapter names the earlier one and lets the two stand against each other. Same move as
the cadastral thread — a repeat converted into an argument rather than avoided.

**[v5] Two unwritten carry-forwards land here.** Part F's meanwhile boxes in 21 and 24
both promise the Atlantic trading empires — *the years Denmark spent fighting Sweden
over a coat of arms are the years the Atlantic economy is being built*, and *the
trading empires that will matter for the next two centuries*. Neither was ever written
as an arrow. This chapter is what they were pointing at, and should acknowledge it.

**Vignettes.** Breffu · St Jan · November 1733 — a woman named in the trial record as
an actor in the rising, not its victim *(verify the record; hedge what it can
carry)* · **[v17]** **Christian Runge, sailor, of Arendal · the middle passage aboard the
*Fredensborg* · April to July 1768.** The planned vignette was an unnamed captive
falling back on 9a. It is not needed: the *Fredensborg* is the best-documented slave
ship in the world — journal and protocol saved from the 1768 wreck, digitised and
transcribed, wreck found by divers in 1974 — and those papers name the captain, the
forty crew and the carpenter who died, and enter the people in the hold as numbers.
The vignette is the named sailor, and the argument is that it is the same archive,
the same hand and the same page. No 9a required, which keeps the part's single
allowance with chapter 25's Amager farmers. · **[v18, date corrected]** **Heinrich Carl Schimmelmann,
treasurer · Copenhagen · 1763.** Not 1759 — that was Ahrensburg, the Holstein estate
that made him a Danish subject. He advised the crown to sell its property, named the
four West Indian plantations among it, and bought them himself in 1763 at an
advantageous price together with Denmark's largest sugar refinery. Owned the Hellebæk
gun factory from 1768, so the guns that bought the people, the people who cut the cane,
and the works that refined it were all his. 1,028 enslaved on the four estates at his
death in 1782.

**Figures.** (a) **The triangle, weighed** — flow figure with real tonnage and real
numbers of people on the arrows. (b) **Christiansted quarter** — the surveyed
plantation grid from the cadastral plats, plantation numbers and acreages. (c) **The
*Fredensborg* in section** — from her own recorded dimensions and manifest, not from
the Brookes print.

**The cadastral thread. [v6 — corrected]** The state measures Denmark in **1681–83**
(26 §04), the village in the 1780s (29), the sugar islands in 1734 (30). All three are
genuine measurements, which the v4 version was not: 1662 and 1664 converted dues rather
than measuring ground, so the thread's Danish term is the Store Matrikel survey and sits
in 26, not 25. The reader still meets the three out of chronological order, which is
better: the plantation plat arrives immediately after the same instrument has been
celebrated as a liberation. One habit of mind, applied three times, praised once. This
must be stated in the prose or it reverts to being a repeated figure.

Every number in every `aria-label` here is generated from the same table as the
visible legend. This is the chapter where the chapter 22 Køge failure would do the
most damage.

**Meanwhile.** The Asiento and the scale of the British trade · Saint-Domingue, and
what "small" means in this business.

**Myth-check.** That Denmark was first to abolish slavery. The 1792 ordinance banned
the *trade*, took effect in 1803, was drafted expecting planters to import heavily
first, and slavery itself ran to 1848.

**Glossary (12).** oktroj · kompagni · Vestindisk-guineisk Kompagni · trekantshandel
· mellempassage · plantage · sukkerraffinaderi · Guldkysten · frihavn · negerhandel
*(historical term, glossed as such)* · fribrev · emancipation.

**Closes on** a woman named in the Christiansted records, and what the record does
and does not say about her. A person.

---

### 31 · The flourishing trade and the wreck of it, 1784–1814

| § | section | weight |
|---|---|---|
| 01 | Neutral bottoms | medium |
| 02 | A city rebuilt twice, 1794 and 1795 | light |
| 03 | 2 April 1801 | heavy |
| 04 | The Norwegian half | heavy |
| 05 | September 1807 | heavy |
| 06 | The gunboat war | medium |
| 07 | 5 January 1813 | medium |
| 08 | Kiel, 14 January 1814 | heavy |
| 09 | Eidsvoll, and the refusal | medium |
| 10 | Every child, 29 July 1814 | light |
| — | **part coda** (`tail_extra`) | — |

**[v4]** §01 now follows directly on chapter 30's close: the ordinance's ten-year
delay ran to 1803, straight through the neutral-carrying boom — the same years, and
largely the same merchant houses. The join should be made, not left implicit.

**Vignettes.** Peter Willemoes · **Flådebatteri nr. 1** · 2 April 1801 — seventeen and
commanding a floating battery, which is the reason the story is told at all.
*Prøvestenen* was a blockship under Lorentz Fisker · **[v19 — replaced; the plan was wrong from v1]** **Kamma Rahbek · her father's house
in Nørregade, Copenhagen · 2–5 September 1807.** Friederike Brun could not have
watched the bombardment from Sophienholm: she was living in Rome from 1807 to 1810.
Kamma Rahbek was in the city — the Rahbeks had to leave Bakkehuset because the
British lines ran through Frederiksberg — and stayed almost alone in her father's
house through the three nights until it burned. · a village schoolteacher
appointed under the 1814 act · a named sogn · 1815 *(to verify)*.

**Figures.** (a) **Three nights** — the bombardment mapped on the city, the fire's
extent by the morning of 5 September. (b) **What sailed away** — the fleet of 1807 by
rate, silhouettes with tonnage, against what was left in 1814. (c) **One rigsdaler**
— the 1813 reform as arithmetic, the conversion shown rather than asserted.

**Meanwhile.** Trafalgar, 1805 · Vienna, 1815.

**Myth-check.** That the bombardment was unprovoked, and that Danish neutrality was
neutral in fact. Both the British and the Danish case are on the record; the chapter
gives both.

**Glossary (12).** florissante handelsperiode · neutralitetsforbund · Asiatisk
Kompagni · orlogsflåde · kanonbåd · kaperfart · statsbankerot · rigsbankdaler ·
Kielerfreden · almueskole · Eidsvoll · helstat.

**Closes on** the schoolroom the 1814 act required in every parish, in the year the
kingdom lost half of itself. An object.

**Coda:** a crown that took everything in 1660 and by 1814 had spent it, leaving
behind the two things it built without meaning to — a surveyed freehold countryside
and a literate one. **The coda must acknowledge the ledger chapter 30 keeps.** Left
alone it states a domestic arc the part has already contradicted, and it does so in
the direction of self-congratulation — the same failure chapter 30's own myth-check
is about. This is the highest drafting risk in the part, because the coda gets
written last and quickly.

**Closing sequence check (Lesson 9).** 25 object · 26 place · 27 number · 28 object ·
29 cost · 30 person · 31 object. No two consecutive alike.

---

## 4. Figure forms

**Distribution.** Every chapter carries exactly one map and two non-map figures.
Seven maps: spine 1660 (25) · Scanian theatre (26) · spine 1721 (27) · Norway detail
(28) · village enclosure pair (29) · Christiansted plat (30) · city fire map (31).

**The repeated move.** Sorting the fourteen non-map figures by *mode* rather than by
form exposed a rut the form list hid — "here is a real thing, drawn accurately, with
words on it". Before correction, seven of fourteen sat in the artefact modes, and the
distribution was not one per chapter: 26 carried two and 31 carried none, which put
the cheapest cut in 26 rather than only in 27. Two figures were replaced — 26b became
the 1241/1683 penalty comparison, 27c the school build-out:

| mode | figures | count |
|---|---|---|
| document rendered with its text | hartkorn (25), catechism (28) | 2 |
| object measured and drawn | cell plan (26), *Fredensborg* (30), column (29) | 3 |
| data or process | routing (25), penalty comparison (26), burials (27), build-out (27), calendar wheel (28), staircase (29), triangle (30), fleet tally (31), rigsdaler (31) | 9 |

Five of fourteen, and chapters 27 and 31 carry none, so the per-chapter regularity is
broken as well as the count reduced.

**Residual, flagged not solved.** The three measured objects fall in 26, 29 and 30 —
29 and 30 consecutive. Cutting either costs more than the adjacency does: the ship
section is the strongest figure in the part, and the column carries chapter 29's
closing. Watch it at review; if it reads as a pattern, 29b is the one to move,
because the inscription can be quoted in prose.

**Repeat check against earlier parts.** Part E used a stepped title ladder, rule
block, voyage map with key strip, fealty diagram, battle schematic that is not a map,
proportional band chart, twelve-week timeline. Part F used a partition tree, ledger,
toll game, territorial map, foundations chart, the Køge chain, ice-march map,
invasions map, losses map, sons-in-law genealogy, the 1645 fan. Part G avoids another
genealogy or partition tree — the Gottorp line rides on the 1721 spine map — another
ledger, another proportional band, another linear timeline, another stepped ladder,
and any second battle schematic.

---

## 5. The debt table **[v4 — retargeted for the swap]**

**Mechanical** = target moves only because a chapter was inserted.
**Content** = the shipped target was a guess made before Part G existed.

| arrow | as shipped | new target | kind | reason |
|---|---|---|---|---|
| 21 → 25 | adelsvælde dismantled | **25** | — | unchanged |
| 24 → 25 | estates meeting, Kongelov 1665 | **25** | — | unchanged |
| 23 → 26 | Leonora Christina, *Jammersminde* | **26** | — | unchanged |
| 21 → 26 | Gottorp line closed 1720–21 | **27** | content | Gottorp settles in 27 |
| 24 → 29 | snaphaner, last attempt on Skåne | **26, 27** | content | snaphaner 26; Helsingborg 1710 in 27 |
| 22 → 27 | Trankebar, the chartered company | **30** | content | the Atlantic chapter |
| 21 → 28 | labour services, bound peasantry, 1780s reforms | **28, 29** | content | the bond in 28, the reforms in 29 |
| 20 → 28 | Norway clause of the 1536 recess, to 1814 | **31** | content | Norway's end is 31 |
| 22 → 30 | Norwegian law 1604, stattholder, mines, to 1814 | **28, 31** | content | apparatus 28 §07, separation 31 |
| 21 → 32 | Glücksburg line, a king from it in 1863 | **Part H** | D-1 | |
| 19 → 32 | Ribe 1460 to 1848, 1864, 1920 | **Part H** | D-1 | |
| 15 → 36 | Estonia 1346 answered by the West Indies 1917 | **30, Part I** | content + D-1 | islands acquired and worked in 30; sale in I |

**Carry-back:** `27 ← 23` — Sweden's Sound-toll exemption from Brømsebro 1645,
abolished at Frederiksborg 1720. Chapter 23 argued the toll had become negotiable
rather than a fact of geography; 27 §07 closes it. Precedent is chapter 21's
Ditmarschen carry-back to 19.

**Internal hinge:** `30 ← 29`, at 30 §01.

Chapters touched by the pass: 15, 19, 20, 21, 22, 23, 24 — Parts D, E, F.
`renumber.py` handles the uniform shift; content changes and comma forms are hand
edits.

**Bundle with this pass:** open item 7 (chapter 20's footer says Part F runs to 1721;
its *Faith and the state* thread promises pietism "in Part F" — pietism is chapter
28) and open item 5a (Part E's shipped 16–19 carry the pre-fix map seam; the re-point
forces the rebuild anyway).

**Routine:** re-point → rebuild → `linkindex.py` → `index_generator.py` with
`DK_CHAPTERS` at the chapter folder → upload.

### Opened by Part G

- 25 → 28 — the parish clergy as the state's reach into every village, taken up by the
  pietist machinery of the 1730s **[v10, opened in draft §08]**
- 25 → Part H — absolutism's own logic, and why it ended in 1848 without a revolution
- 26 → Part H — Skåne stays Swedish; the last Danish claim lapses
- 28 → Part H — the parish school of 1721 and 1814 to Grundtvig and the folk high schools
- 29 → Part H — the husmænd, landless after 1788, and the franchise of 1849
- 30 → Part I — the islands to emancipation in 1848 and the sale of 1917
- 31 → Part H — the helstat as the only composite question left, Slesvig-Holstein inside it
- 31 → Part H — the bankruptcy of 1813 and the credit system of the 1830s

---

## 6. Decisions — all closed

**D-1 · Numbered arrows only into the next part; letters beyond.** Adopted. Needs a
sixth cross-reference form in `HANDOFF.md`'s table and a pattern in
`renumber.py --census`.

**D-2 · Seven pages, 43 chapters.** Confirmed, on the Atlantic ground alone.

**D-3 · The spine map is 1660, not 1658.** Adopted. `HANDOFF.md`'s spine-map list
still says 1658 and must be updated in the same edit.

**D-4 · Chapter 30's declared span, 1620–1803.** Kept honest. The fan draws
`tx(mid)` → `bx(i)` with no sort and no monotonicity assumption, so a crossing is
cosmetic. The top axis runs 0.059 px per year on the 1000-unit viewBox and chapters
25–31 occupy 7.9 px in total; under the v4 order the crossing is about 4 px. **[v4]**
Invisible at any rendered size. No code change.

**D-5 · `--indigo:#2F4C7A`.** Adopted.

**D-6 · Calendar convention, whole series.** **Dates are given in the style the
Danish state used at the time — Julian before 1 March 1700, Gregorian after — with
the foreign style in parentheses at first divergence in a chapter.** Helsingborg is
10 March 1710 (28 February, Swedish style); Poltava 8 July 1709 (27 June, Russian
style). Everything in Parts A–F is Old Style and nothing currently says so: Part F is
internally consistent, since Sweden was on Julian in 1658 too, but a reader checking
Lutter am Barenberge against a German source finds 27 August or 6 September depending
which state printed it. **Fix: one line in the index's conventions list** — a single
edit touching no chapter — plus a `gammel stil / ny stil` glossary entry in chapter
27, where the divergence first bites a date on the page. Add the rule to
`HANDOFF.md`'s settled vocabulary.

**D-7 · The Atlantic chapter is 30, after the reforms. [v4 — closed]** The deciding
reason is not the two joins argued earlier, which are taste. Under the old order both
chapters had to introduce Reventlow, the Bernstorffs and Schimmelmann-in-office —
chapter 29 for the ordinance, chapter 30 for the commission — so two chapters already
at ten sections each paid the same setup cost. The swap pays it once, in 29. A reader
meeting an act before the government that made it is a comprehension fault, not a
preference, and the fix buys back length.

The ground for the old order survives but weakens: *Who was left out* moves to 29 and
closes on the husmand, and 30 opens asking the same question at a larger scale. Asked
twice at rising cost is at least as strong as primed once, and 30's own close — a
woman named in the Christiansted records — never needed the help. The cadastral
thread improves (see 30).

---

## 7. Build work

New: `build_part_g.py` (from `build_part_f.py`), `map_1660.py`, `map_1721.py`,
`figs_25.py` … `figs_31.py`. `style.css` gains `--indigo`.

`mapfixture.py` gains 1660 and 1721 across all four layers. New territorial facts
needing curated cases: Skåne, Halland, Blekinge, Bohuslän Swedish from 1658; Bornholm
and Trøndelag Danish again from 1660; Gottorp's Slesvig share royal from 1721 while
Gottorp Holstein runs to 1773; Greenland `CLAIM` → `DEP` at 1721. Every new territory
needs three curated cases or the assert layer fails. `seamcheck.py` runs on both maps
before either ships — the Slesvig / Holstein / Gottorp boundary in 1721 is exactly the
thin-lens geometry that produced the 27 km Kongeå fault.

Denmark- and Norway-scale figures use `mapspine.detail_base` / `detail_land_path`.
Never `mapkit.land_path` — chapter 31's city-scale bombardment map is the worst case
for the Eurasian-ring bridge and the one most likely to be drawn in a hurry. Every
figure script calls `mapspine.emit()`.

Rasterise and look at all twenty-one. `mapdump.py` for the spine pair.

### `index_generator.py`

The routine above runs the generator but nothing edits what it generates *from*.

1. **The `E` table**: six Part G rows replaced by seven — number, band index, title,
   date label, mid-year, gloss, markers — and every entry from old 29 upward shifted
   by one. Mid-years under the v4 order: 25 ≈ 1665 · 26 ≈ 1685 · 27 ≈ 1710 · 28 ≈ 1745
   · 29 ≈ 1779 · 30 ≈ 1711 · 31 ≈ 1799.
2. **`DENSE = {27, 28, 30, 34, 40}` → `{35, 41}`.** Old 27, 28 and 30 were Part G's
   dense flags and are resolved by this plan; 34 → 35 and 40 → 41 under the shift.
3. **Hardcoded strings that drift silently** — the chapter 22 Køge `aria-label`
   failure in a different file:
   - `PAGETYPES`: `"42"` → `"43"`, "Five are flagged dense" → "Two".
   - fan `aria-label`: "42 chapters" → "43", "83 percent of the chapters" → "84".
   - SVG axis label: "1,200 yrs → 35 chapters" → "36 chapters".
   - stat block: "83%" → "84%".
   - reading-plan list: "Five chapters are flagged dense" → "Two".

   The header line already computes `len(E)` and `len(DENSE)`, which is why this is
   invisible: the top of the page stays right while everything below it goes wrong.
   **Compute them, do not retype them.**
4. Adjacent: the stat block says "6 chapters for 1901–1955" while the title says 1953.
5. Under D-6, the conventions list gains the calendar line.

Also while the build scripts are open: open item 3 (`build_part_d.py` on the `e`
prefix) and open item 4 (the `--part` / `--band` no-op in ABC and D).

---

## 8. Work order

1. **`HANDOFF.md` edits** — the debt tally (it says four at 25 and one at 28; there
   are two and two, and 22 → 30 is dropped entirely); the Part G state row; the
   spine-map list, which still says 1658; the sixth cross-reference form (D-1); the
   date convention (D-6); Lesson 1 amended with the narrative-plus-fixed-apparatus
   formula, since words-per-section is what produced the v1 error.
2. **The ledger pass** — `renumber.py` for the shift, then the content retargets and
   comma forms by hand across 15, 19, 20, 21, 22, 23, 24; bundle open items 5a and 7;
   then rebuild → `linkindex.py` → `index_generator.py` → upload.
3. **`index_generator.py`** — the `E` table, `DENSE`, and the five hardcoded strings
   computed rather than typed.
4. **Maps** — `map_1660.py`, `map_1721.py`, fixture cases, `seamcheck.py`, rasterise
   and look.
5. **Research and figures**, chapter by chapter.
6. **Prose.**

**7. [v5] Two faults in shipped chapters, found by `vignettes.py`** — fold into the
   ledger pass, which touches 21–24 anyway:
   - **Chapter 23's Ellen Marsvin vignette has no place.** Its who line reads
     `Ellen Marsvin, of Dalum and Rosenvold · 1629 · born 1572, died 1649 · …`, so the
     middle field is a year, and its `<h4>` is the only vignette heading in nine
     chapters without a location. Lesson 7 requires person · place · date. Dalum or
     Rosenvold, whichever 1629 finds her at.
   - **`vignettes.py`'s sentence splitter breaks on regnal numbers** — "Christian 4."
     reads as a sentence end, so two meanwhile summaries truncate to four words. One
     line: require the character after `". "` to be upper-case *and* the preceding
     token not to be a digit.

### Open before drafting

- **The vignette roster check is done.** `vignettes.py` against 16–24 forced four
  changes, recorded in place above. What the probe cannot see is the *beat* — a
  preacher facing a hostile assembly and a burgher carrying a decisive meeting look
  nothing alike in a who line — so the openings were read as well as the fields.
- **Seven vignette subjects marked *to verify*** — the matrikel widow in 25, the
  Göinge priest in 26, Holberg at Borrehuset in 27, the confirmand and the
  cattle-plague farmer in 28, the gårdmand in 29, Breffu and the *Fredensborg* captive
  in 30, the schoolteacher in 31. Any that will not carry a name falls to the 9a
  provision. Two using it in one part would be one too many.
- **Two figures need their subject chosen in research** — 26b's offence, and 27c's
  cost and revenue figures for the rytterskoler.
