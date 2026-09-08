# PLAN_I — Part I, chapters 37–44, 1901–1955

Drawn September 2026, after a cold run against commit `9e9700a`. Part I is the
last part. It is **eight chapters, not seven**; the book is **44, not 43**. That
decision and its reasons are §2.1.

This plan settles structure, weights, debts, vignettes and figures. It does not
draft. Nothing in §§5–12 is prose; the section lists are subjects with weights,
and the weight is a budget, not a description.

---

## 1. The length model

### 1.1 Why the old one could not be carried

`PLAN_H` §1 uses `page ≈ Σ(bands) + 3,508` at light 240 · medium 376 · heavy 576,
measured on Part G's seven chapters. Both halves have moved, and the handover's
stated reason for recomputing — that "every previous part plan assumed five or
fewer" chapters — is wrong: Part G is seven by decision D-2 and `PLAN_H`'s model
is calibrated on those seven. What has actually changed is the apparatus.

| | Part G | Part H | Δ |
|---|---|---|---|
| vignettes (3) | 697 | 817 | +120 |
| glossary | 366 (5.4 blocks) | 460 (**9.2 blocks**) | +94 |
| checkpoints (3) | 165 | 184 | +19 |
| Meanwhile (2) | 205 | 208 | +3 |
| figures (3) | 285 | 199 | −86 |
| outside (header, rail, contents, footer) | 1,796 | 1,960 | +164 |

The glossary nearly doubled in block count between one part and the next and
nobody decided that. **Part I keeps Part H's nine blocks** — see decision 2.6 —
but it keeps them as a decision rather than as drift.

### 1.2 The bands

Terciles of the 118 measured sections of Parts G and H:

| band | range | mean | n |
|---|---|---|---|
| light | under 336 | **258** | 39 |
| medium | 336 – 470 | **393** | 39 |
| heavy | 471 and over | **569** | 40 |

Part G's own cuts are 318/454 and Part H's 358/492; the pooled figures sit
between them. Median section 397. Longest in the book 759, chapter 32 §10.

These are now the thresholds inside `narrative.py`'s `band()`. **The plan and the
verifier use one scale.** Before this session they did not — see item 64 — and
that is why chapter 36's first draft could read 5L/5M/0H against the plan and
something else against the tool.

### 1.3 The model

> **page ≈ Σ(section bands) + 3,786**, at light 258 · medium 393 · heavy 569
> **minutes = page ÷ 210**, on `pagewords.py`, which is now the only counter
> The part coda is ~490 words and sits **inside** the constant, not on top of it

The constant is `bookstats` page words minus narrative-region words across
chapters 32–36, mean of five, on the unified counter. The coda figure is measured
directly off the shipped pages — chapter 31's coda block is 478 words and chapter
36's 495 — rather than inferred by subtraction, which is where `PLAN_H`'s 419
came from.

**Tested backwards against Part H**, predicted page words against actual: 32
−113, 33 −547, 34 +595, 35 +95, 36 +193. Mean absolute error 309 words, about a
minute and a half. The two large misses are apparatus, not narrative: chapter 33
carries 4,153 words of apparatus against a part mean of 3,786, chapter 34 only
3,521. The model predicts narrative well and apparatus to about ten per cent.

### 1.4 Reference shapes

| shape | narrative | page | min |
|---|---|---|---|
| 10 sections, 4L/4M/2H | 3,742 | 7,528 | 36 |
| 10 sections, 3L/4M/3H | 4,053 | 7,839 | **37** |
| 10 sections, 3L/5M/2H | 3,877 | 7,663 | 36 |
| 10 sections, 2L/4M/4H | 4,364 | 8,150 | 39 |
| 11 sections, 4L/4M/3H | 4,311 | 8,097 | 39 |
| 9 sections, 3L/3M/3H | 3,660 | 7,446 | 35 |

**Ten sections at 3L/4M/3H is the Part I shape**, landing at 37 minutes with
three minutes of headroom under the 40-minute advisory ceiling of decision 2.1
(Part H). Eleven sections is available and costs two minutes.

### 1.5 The part, and the book

Seven chapters at 3L/4M/3H and chapter 44 at 3L/5M/2H gives **62,536 page words**
for Part I. The book lands at **44 chapters, 322,062 page words, 25.6 hours**,
mean 7,320 a chapter. Part I's mean of 7,817 sits just under Part H's 7,963 and
above Part G's 7,354, which is right for a part carrying two wars and the ending.

---

## 2. Decisions taken at plan time — not to be reopened

**2.1 Part I is eight chapters and the book is 44.** The 1917–1929 gap in the
spine was real and visible to a reader on the published index page, which showed
`1918 – 1920` followed by `1929 – 1939`. The twenties are not a linking passage:
the postwar slump, Landmandsbanken, the defence settlement of 1922, Stauning's
first government and Nina Bang, Madsen-Mygdal and the return to gold, the mark
conversion in Sønderjylland, the Greenland sovereignty declaration of 1921 and
kulturradikalisme are ten sections. Forced into a 1920–1939 chapter they become
two sections of throat-clearing before the crash, and what gets cut is
disproportionately the women and the non-elite subjects — the D-9 material. The
thirties alone are equally full and include the 1939 referendum, on which chapter
44's argument depends. **Recorded as D-10.**

The cost was measured rather than assumed. Nothing built references a chapter
number above 36 — the only occurrences of `c37`–`c43` anywhere in the repository
were in the generated index. The functional hardcodes of 43 were two lines in
`bookstats.py`. No renumbering script was needed and no shipped page changed.

*The handover's ground for rejecting an epilogue — that it "breaks a 43-chapter
spine that every tool in the build assumes" — is therefore false. The decision to
end at 1953 stands on its own better ground (§2.2) and the false premise is
struck from the ledger rather than carried forward.*

**2.2 The book ends in 1953, on a mechanism and not a truncation.** Settled
before this plan and worked from, not reopened. §20 of the 1953 constitution
specifies how Denmark may transfer sovereignty to international authorities, and
it was written because the UN, NATO, OEEC and the coming European communities
existed or were in the making. 1973 is the first exercise of a mechanism the last
chapter installs. Chapter 44 must say so. No epilogue.

**2.3 Chapter 38 takes Iceland.** The Act of Union of 1 December 1918 sat in
chapter 37's key list, two years outside its own span. Moved. It gives 38 a
spine rather than a date range: three years, three answers to one question —
Slesvig by plebiscite, Iceland by treaty, the crown by the threat of a strike.

**2.4 Chapter 41's span opens in 1939, not 1940**, so the phoney-war winter and
the ignored warnings have a home and the spine has no hole.

**2.5 Chapter 37 is one chapter, not two.** It was the other candidate for the
eighth chapter, because it pays both West Indies debts and must tell the islands'
story as well as Denmark's transaction. Drawn out it lands at exactly ten
sections (§5). The islands get two of them.

**2.6 Nine glossary blocks a chapter, as Part H.** Part I is the densest Danish
terminology stretch in the book — *samarbejdspolitik*, *retsopgør*, *stikker*,
*værnemager*, *Genforening*, *hjemmetysker*, *afstemningszone*, *provisorisk*
returning. Nine is honest for it. Recorded because it is a 94-word budget line
that arrived by accident in Part H.

**2.7 Chapter 42 stays one chapter.** It carries the dense flag (`DENSE = {42}`,
inherited from the old 41) and it is a genuine split candidate: August 1943, the
fleet, the rescue, the Freedom Council, the strike, Shellhus, liberation. It
stays whole because the material is one arc with one question — what a country
does when cooperation stops being possible — and because the part has already
grown by one. **If its first draft runs over 8,400 page words the decision
reopens; nothing else reopens it.**

**2.8 Chapter 44 gets a wider budget.** It carries the part coda *and* the ending
of the book. Planned at 3L/5M/2H — one notch light on narrative — so that a coda
of up to ~700 words still lands it at 38 minutes rather than 41.

**2.9 Chapter 44 lands on a person, not a signature.** Not the signing
photograph. The book's best endings are the Isted Lion in a foreign cemetery, a
stateless boy in Haderslev, wreaths from the typographers of Aalborg at a
suicide's funeral. The 1953 equivalent is a woman voting in the referendum that
abolished the chamber her grandmother was excluded from by name. That vignette
has no subject yet and it is the one item in Part I that may need physical
access — see §12.

---

## 3. The debt table

**Built from the `→` markers inside the `id="forward"` blocks, not from a text
search for "Part I".** The book carries 110 forward arrows; searching for the
destination string finds nine of these ten plus one piece of chapter 36 coda
prose, and misses the tenth — which read `→ a later part` precisely because it
carried no part letter.

| # | from | the debt, as the shipped page states it | discharged in |
|---|---|---|---|
| 1 | ← 15 (with 30) | Selling an overseas province that costs more than it yields: Estonia 1346, the West Indies 1917 | **37** |
| 2 | ← 30 | Slavery in the West Indies ends in 1848 after a rising; the islands sold 31 March 1917 | **37** |
| 3 | ← 33 | The seven categories the 1849 franchise excluded, and the year each was let in | **37**, residue **40**, closed **44** |
| 4 | ← 36 | Women's suffrage and 1915 — Line Luplau's association outliving her by twenty-four years | **37** |
| 5 | ← 19 (with H) | Ribe 1460 as the root of the question: 1848, 1864, and the plebiscite of 1920 | **38** |
| 6 | ← 34 | Article 5 of the Peace of Prague, abrogated 1878, and the plebiscite that finally happens | **38** |
| 7 | ← 35 | The plebiscite of 1920, given up in 1907; **and** a labour settlement outlasting its century | **38** / **40** |
| 8 | ← 36 | The Social Democrats from two seats to government | **39** |
| 9 | ← 31 | Greenland, Iceland and the Faroes stay with Denmark by a parenthesis in article four | **38**, **43**, closed **44** |
| 10 | ← 36 | Parliamentarism written into the constitution in 1953 | **44** |

**Debt 8 is why chapter 39 exists.** Stauning takes office in 1924. Under the old
spine this arrow would have been paid five years late or not at all.

**Three arrows pay out more than once.** Debt 9 is the realm thread: Iceland's
Act of Union in 38, Iceland's republic and the annulled Faroese referendum in 43,
Greenland's reclassification in 44. 38 and 43 make partial payments in their own
carry-forward blocks and **44 closes it**, because the point is that three
territories kept by one clause left by three different routes and only the last
chapter can say that. Debt 3 is the same shape: women and servants in 1915,
poor-relief recipients with the social reform of 1933, the voting age in 1953.
Debt 7 is two debts in one arrow — plebiscite to 38, the September Compromise to
Kanslergade in 40, where the 1899 system is honoured and overridden at once.

**Two continuities that are not arrows** and would be lost if this table were the
only record: the two hundred thousand — or a hundred and seventy thousand — carried
in chapter 36's coda as "a government that will conscript their sons in 1914", which
37 conscripts and 38 brings home; and Article 80, **not** an outstanding debt (item
59 records it discharged in chapter 36 by the parish council law of 1903) but with a
residue for 44: the law was expressly temporary and the final settlement has still
never been made.

**Item 24 is closed by this plan.** Its premise was wrong: 1953 is inside Part I,
not beyond it. The arrow now reads `→ Part I`, like its two neighbours in the same
block. Source edit to `c36_draft.md`, body regenerated, page rebuilt; chapter 36
drops 34 page words to 7,642 and from 37 minutes to 36, and nothing else moves.

---

## 4. Vignette roster — twenty-four across eight chapters

Balance across the part: **9 [n], 8 [f], 7 [-]**. Every chapter carries at least
one `[f]` and one `[n]`, as D-9 requires. Lazy backfill permitted.

| ch | tag | who | status |
|---|---|---|---|
| 37 | [n] | Kresten Andresen · the Somme · August 1916 | verify from the published letters |
| 37 | [f] | Jutta Bojsen-Møller · Amalienborg · 5 June 1915 | verify she led it; crowd figure disputed |
| 37 | [n] | David Hamilton Jackson · Frederiksted, St Croix · 1915–16 | verify trip, paper, holiday |
| 38 | [f] | Johanne Marie Braren · Frederikshøj · 10 July 1920 | **sourced** |
| 38 | [n] | *unnamed* · Flensburg · 14 March 1920 | **needs a subject** |
| 38 | [-] | C.Th. Zahle · Amalienborg · 29 March 1920 | verify the two audiences |
| 39 | [-] | Emil Glückstadt · Vestre Fængsel · 1923 | verify death date and place |
| 39 | [f] | Nina Bang · Ministry of Education · 23 April 1924 | **sourced** |
| 39 | [n] | *unnamed* · Sønderjylland · 1920–21, marks into kroner | **needs a subject** |
| 40 | [-] | Stauning and the negotiators · Kanslergade 10 · 29–30 January 1933 | sourced |
| 40 | [n] | *unnamed* · Nakskov · 1931 | **needs a subject**; verify charges |
| 40 | [f] | *unnamed* · a Mødrehjælpen case · 1939, **or** a woman who lost her vote to poor relief and got it back in 1933 | **needs a subject**; the second needs no archive |
| 41 | [n] | one of the sixteen · Bredevad or Lundtoftbjerg · 9 April 1940 | verify name, place, total |
| 41 | [-] | Erik Scavenius · Berlin · November 1941 | verify what he signed |
| 41 | [f] | *unnamed* · 1940–42 | **needs a subject** |
| 42 | [f] | Ellen Nielsen · Dragør · October 1943 | verify camp and arrest date |
| 42 | [n] | Kim Malthe-Bruun · Vestre Fængsel · April 1945 | verify execution date |
| 42 | [-] | Georg Ferdinand Duckwitz · Copenhagen · 28 September 1943 | verify; rests on his own diary |
| 43 | [f] | Fanny Jensen · Christiansborg · 1947 | **sourced** |
| 43 | [n] | *unnamed* · Rønne · 7–8 May 1945 | **needs a subject** |
| 43 | [-] | the first man executed under the retroactive law · 1946 | verify name and date |
| 44 | [n] | Helene Thiesen · Nuuk, then a colony near Faxe · May 1951 | **sourced** |
| 44 | [f] | *unnamed* · a polling station · 28 May 1953 | **needs a subject — this is the ending** |
| 44 | [-] | the commission's adviser on §20 · 1952–53 | **needs a name** |

**What is sourced, and what it gives.** Johanne Marie Braren was nine, the foster
daughter of the vicar's household at Aastrup; her mother lifted her up to hand
over flowers and the king took her onto the horse. It arrives with its own
myth-check: the white horse was ridden to fulfil Jomfru Fanny's prophecy of 1881,
the horse was borrowed and destroyed soon after, and the most reproduced image of
the Genforening is a photograph of an accident. Nina Bang arrives with a second:
she is routinely called the world's first woman minister and was not — Aleksandra
Kollontai held office in Russia from 1917 — she was the first appointed by a
parliamentary government, which is a smaller claim and a better one. Fanny Jensen
was a factory worker at Kirks Telefonfabrikker in Horsens and union chair from
1912, minister without portfolio in Hedtoft's government "with special regard to
the interests of homes, housekeeping and children"; Denmark's second woman
minister, twenty-three years after the first, and the portfolio is the argument.
Helene Thiesen was seven, her father dead of tuberculosis three months before the
ship sailed, her mother refused twice and was worn down; one of twenty-two
children sent to Denmark to be made into Danes, returned unable to speak
Greenlandic to her own mother, then placed in a Danish-speaking orphanage in Nuuk
until 1960. Two years before the constitution ended the colony.

**Six have no named subject: 38[n], 39[n], 40[f], 41[f], 43[n], 44[f].** Five of
the six are `[f]` or `[n]`. That is not a coincidence and it is the whole reason
D-9 exists: `[-]` subjects name themselves, because ministers and bank directors
are indexed. Every hour of research this roster needs falls on the two categories
the convention protects.

---

## 5. Chapter 37 — Reform, neutrality and the sale of the West Indies, 1901–1917

| § | section | weight |
|---|---------|--------|
| 01 | What the change of system actually changed | light |
| 02 | The Radicals, 1905, and the splitting of the left | medium |
| 03 | Alberti | heavy |
| 04 | The defence question, and a fortress never fired | light |
| 05 | 5 June 1915: the seven categories, minus two | heavy |
| 06 | August 1914: neutrality, and the mines in the Belts | medium |
| 07 | Gulasch, rationing, and the ships that did not come back | medium |
| 08 | What the islands were: 1848, 1878, and labour under the Danish flag | heavy |
| 09 | Selling them: the treaty, the Rigsdag, the referendum of December 1916 | medium |
| 10 | 31 March 1917 | light |

**3L / 4M / 3H → 4,053 narrative + 3,786 → 7,839 → 37 minutes.**

**Where this differs from the standard account.** The Danish telling of 1917 is a
transaction: a price, a strategic argument about Germany, and a referendum. Here
§08 gets a heavy *before* the sale is described, so that the reader meets the
islands as a place with a history — a rising that ended slavery in 1848, the
Fireburn of 1878, and labour conditions that produced Jackson's newspaper — rather
than as an asset. The closing irony is the book's thread in one sentence:
**Denmark held a referendum on whether to sell twenty-seven thousand people who
were not asked.** §10 lands there and stops.

**§05 pays debt 3 and debt 4 in one scene** and must be precise about what 1915
did and did not do: women and servants in, the rest of the seven categories still
out, and the first election under it not until 1918.

---

## 6. Chapter 38 — Genforeningen, Iceland and the Easter Crisis, 1918–1920

| § | section | weight |
|---|---------|--------|
| 01 | November 1918: the soldiers come home | light |
| 02 | Iceland, 1 December 1918 | medium |
| 03 | What Versailles said, and what Denmark asked for | medium |
| 04 | The zones, and the argument about Flensburg | heavy |
| 05 | 10 February 1920 | heavy |
| 06 | 14 March 1920 | medium |
| 07 | The king dismisses a government | heavy |
| 08 | The strike that did not have to happen | medium |
| 09 | 10 July 1920 | light |
| 10 | What the border cost the people on both sides of it | light |

**3L / 4M / 3H → 7,839 → 37 minutes.**

This is the pivot chapter of the whole book. In 1920 the *territory* question is
answered by asking the people; the *authority* question is answered when the king
backs down. Everything after is the third term — who counts as a member, and what
the state owes them.

**§04 is where the plan expects the most argument and gives it the most room.**
The Danish movement was not united: the Flensburg question split it, and the
line that was drawn is the line the votes drew, not the line the nationalists
wanted. **Closes debt 5, the longest in the book — outstanding since chapter 19
and the Ribe settlement of 1460 — and debt 6.**

**§10 is the section most likely to be cut and must not be.** A border drawn by
asking people still leaves minorities on both sides: *hjemmetyskere* north of it,
the Danish minority south of it, and the *hjemløse* with no passport from any
country. The chapter cannot end on the white horse.

---

## 7. Chapter 39 — Deflation, the Landmandsbank crash and the first Social Democratic government, 1920–1929

| § | section | weight |
|---|---------|--------|
| 01 | The boom ends | light |
| 02 | Marks into kroner: Sønderjylland pays for coming home | medium |
| 03 | Landmandsbanken, 1922 | heavy |
| 04 | Who paid for the rescue | medium |
| 05 | The defence settlement of 1922, and Munch's argument | medium |
| 06 | 1924: the party in office | heavy |
| 07 | Nina Bang | medium |
| 08 | Steincke writes a plan nobody asks for yet | light |
| 09 | Madsen-Mygdal, and the return to gold | heavy |
| 10 | What the twenties settled, and what they did not | light |

**3L / 4M / 3H → 7,839 → 37 minutes.**

**The new chapter, and the case for it is §05 and §08 as much as §03 and §06.**
§05 is the direct ancestor of 9 April: Munch's position — that a country which
cannot defend itself should not pretend to — is a considered argument and not a
failure of nerve, and chapter 41 is unintelligible if it appears there for the
first time. §08 is the seed the chapter's successor is named for: **verify that
Steincke's *Fremtidens Forsørgelsesvæsen* is 1920**; if it is, the intellectual
blueprint of the 1933 reform predates the decade it is usually credited to.

**§06 closes debt 8.** From two seats in 1884 to a government in 1924, on a
minority in the Folketing and no majority at all in the Landsting — which is the
Landsting doing again what chapter 36 showed it doing, and points at 44.

---

## 8. Chapter 40 — Depression, Stauning and the seeds of the welfare state, 1929–1939

| § | section | weight |
|---|---------|--------|
| 01 | 1929: Stauning returns, with the Radicals | light |
| 02 | The crash reaches a farming country | medium |
| 03 | The night at Kanslergade | heavy |
| 04 | What was actually in the deal | medium |
| 05 | Steincke's reform: four laws and a principle | heavy |
| 06 | The vote given back | medium |
| 07 | Stauning eller kaos | medium |
| 08 | The Danish Nazis, and why they failed | light |
| 09 | Eastern Greenland at The Hague, 1933 | light |
| 10 | 1939: over ninety per cent, and not enough | heavy |

**3L / 4M / 3H → 7,839 → 37 minutes.**

**§05's principle is the chapter's argument**, and it is the thing most often
lost: relief as a right with a legal basis, not a discretionary charity that cost
the recipient his standing as a citizen. §06 is the half of that which is almost
never told and which **pays the residue of debt 3** — *verify that the 1933
reform is what removed the franchise disqualification for poor relief, and not a
separate act.* If it was separate, the residue moves and the closing chapter does
not.

**§10 is load-bearing for chapter 44 and must be verified before drafting.** The
1939 attempt to abolish the Landsting failed with over ninety per cent voting yes,
because the yes votes were only 44.5 per cent of the electorate and the 1915 rule
required 45. Chapter 44 §03 turns on the same threshold being cleared.

**§04 pays the second half of debt 7:** Kanslergade extended collective
agreements by law and prohibited a lockout — the settlement of 1899 honoured and
overridden in one night.

---

## 9. Chapter 41 — 9 April 1940 and samarbejdspolitikken, 1939–1943

| § | section | weight |
|---|---------|--------|
| 01 | The winter of 1939 | light |
| 02 | The warnings | medium |
| 03 | Six hours | heavy |
| 04 | The choice, and who made it | heavy |
| 05 | The alsang summer | medium |
| 06 | The economy of accommodation | medium |
| 07 | Frikorps Danmark, and the Communists arrested by Danish police | heavy |
| 08 | Scavenius | medium |
| 09 | The king's telegram | light |
| 10 | The election of March 1943 | light |

**3L / 4M / 3H → 7,839 → 37 minutes.**

**Where this differs from the standard account.** *Samarbejdspolitikken* is
usually argued as a moral question with two positions. Here §04 and §07 make it a
question about *who was handed over*: the Communist arrests of June 1941 were
carried out by Danish police under a Danish law passed by a Danish parliament,
and Frikorps Danmark was recruited with official acquiescence. The chapter does
not have to reach a verdict — §10, an election with 89 per cent turnout in which
the Nazi party got almost nothing, is evidence for the defence — but it must put
the cost in the reader's hands before chapter 43 tries anybody for less.

---

## 10. Chapter 42 — 1943–1945: rupture, rescue, resistance, 1943–1945

| § | section | weight |
|---|---------|--------|
| 01 | The strikes of August | medium |
| 02 | 29 August: the fleet | heavy |
| 03 | The warning | medium |
| 04 | Three weeks in October | heavy |
| 05 | Those who did not get away | medium |
| 06 | The Freedom Council | light |
| 07 | Sabotage, and the counter-terror | heavy |
| 08 | The People's Strike, June 1944 | medium |
| 09 | Shellhus | light |
| 10 | 4 May 1945 — and Bornholm | light |

**3L / 4M / 3H → 7,839 → 37 minutes.** Flagged dense; see decision 2.7.

**§05 exists so that §04 cannot be told as a triumph.** Around four hundred and
seventy people were deported to Theresienstadt; most survived and some did not,
and the difference between them and the seven thousand who reached Sweden is
often a matter of hours and of who owned a boat. **Verify the figures against a
named source; this is exactly the kind of round number that arrives pre-rounded.**

**§07 must carry the *clearingmord*** — the reprisal murders of named Danes by
the occupier for each act of sabotage — or the sabotage reads as costless.

---

## 11. Chapter 43 — Settling accounts and choosing a side, 1945–1949

| § | section | weight |
|---|---------|--------|
| 01 | The first week | light |
| 02 | The law made backwards | heavy |
| 03 | Who was tried, and who was not | heavy |
| 04 | The women | medium |
| 05 | Bornholm under the Soviets | medium |
| 06 | South Slesvig: the border Denmark declined to move | heavy |
| 07 | Marshall aid, and the end of self-sufficiency | medium |
| 08 | Iceland gone, the Faroes refused | medium |
| 09 | The Scandinavian defence union that failed | light |
| 10 | 4 April 1949 | light |

**3L / 4M / 3H → 7,839 → 37 minutes.**

**§02 and §03 are the chapter's spine and its problem.** A death penalty
abolished in practice was reintroduced and applied retroactively; the people
executed were overwhelmingly informers and Danish employees of the German
security apparatus, and the large firms that built for the occupier were largely
not touched. That asymmetry is the finding, and it should be stated as one rather
than implied.

**§06 pays the Slesvig thread its last instalment.** In 1945–47 Denmark was
offered, or could have taken, a border further south, and declined — the first
time in the book that a Danish government refuses territory it could have had.
**That is the thread of the whole book turning over**, and it belongs here rather
than in 44.

**§08 makes a partial payment on debt 9:** Iceland's republic in 1944 and the
Faroese independence referendum of 1946, annulled by the king.

---

## 12. Chapter 44 — 1953: the new constitution and the modern realm, 1949–1955

| § | section | weight |
|---|---------|--------|
| 01 | Why anyone wanted a new constitution | medium |
| 02 | The commission, and the lawyers in it | medium |
| 03 | The Landsting votes itself out of existence | heavy |
| 04 | A daughter who could inherit | medium |
| 05 | §20: the door | heavy |
| 06 | Greenland stops being a colony | medium |
| 07 | What Greenland got instead | medium |
| 08 | 28 May 1953 | light |
| 09 | The composite state, ended | light |
| 10 | The woman at the polling station | light |

**3L / 5M / 2H → 3,877 narrative + 3,786 → 7,663 → 36 minutes**, with room for a
coda of up to ~700 words at 38. See decision 2.8.

**What 1953 closes, and why the chapter is structured by it.** The Landsting is
abolished and Denmark becomes unicameral, which discharges chapters 34 and 36
completely — Estrup's privileged franchise, the deadlock nobody wrote a procedure
for, and the nine years of provisional government all end when the upper house
does. Parliamentarism is written into the constitution, completing chapter 36's
myth-check in as many words. Conditional female succession pays chapter 33 §02 on
the Kongelov's agnatic rule and pays chapter 34, a war fought over a woman's
inability to transmit a crown. Greenland ceases to be a colony, closing debt 9.
§20, §55 on the ombudsman, §75 on the social obligation, and an express ban on
deprivation of liberty for descent, religion or political conviction — the last
of which is the occupation of chapters 41 to 43 answering itself.

**§03 carries the fact this plan most wants verified.** In 1953 Frederik 9. had
three daughters and no sons, and the succession clause is credited with supplying
just enough extra turnout to clear the 45 per cent threshold that defeated the
1939 attempt. If it holds up: **the constitution that abolished the upper house
and legalised parliamentarism got over the line because voters wanted Margrethe
to be queen.** It is load-bearing and it is exactly the kind of good story that
turns out to be tidier than the record. Verify properly, and if it does not hold,
§03 says so and the chapter is better for it.

**§07 is the chapter's irony and the reason it is not triumphal.** Greenland's
colonial status was ended by legal reclassification decided in Copenhagen, and
the same decade produced the Thule relocation and the experiment children. **The
composite state was abolished by an act that was itself the composite state doing
what it had always done.**

**§09 is the book's argument, stated once and briefly.** Denmark spends its
entire recorded history as a composite state, governing territory that was not
Denmark and people who were not Danes — Skåne, Estonia, Norway, Iceland, the
Faroes, Greenland, Slesvig, Holstein, Lauenburg, the West Indies — and the
argument is always the same three things failing to coincide: a territory, a
people, and an authority. By 1953 the three roughly coincide for the first time.

**§10 is a person, and it is the last thing in the book.** See decision 2.9.

---

## 13. Figures — twenty-four, with the source named

Nine are data figures, of which **five are time series**. Part H shipped fifteen
figures and not one series (item 60); a part covering two wars, a depression and
the building of a welfare state could not repeat that.

| ch | figure | source | status |
|---|---|---|---|
| 37 | The electorate before and after 1915, by category | *Valgene til Rigsdagen*, Stat. Medd. | located |
| 37 | The 1916 referendum, beside the population that did not vote | referendum returns; islands' census | needs source |
| 37 | Danish merchant ships and seamen lost 1914–18 | *Handelsflådens krigsforlis* | needs source |
| 38 | The two zones, parish by parish | International Commission returns | located; **new map** |
| 38 | Three elections in one year, 1920 | election statistics | located |
| 38 | Iceland 1918: what the Act of Union transferred | schematic | n/a |
| 39 | **Unemployment 1910–1930, annual** | Stat. Medd. 4. rk., five-year volumes | **fetchable** |
| 39 | Two seats to government: Social Democratic seats 1884–1924 | election statistics | located |
| 39 | Landmandsbanken: what the state guaranteed and what it lost | Bankkommission report | needs source |
| 40 | **Unemployment 1929–1940**, with the 1932 peak | as above | fetchable |
| 40 | What was in Kanslergade | schematic | n/a |
| 40 | **1939: the yes vote, and the 45 per cent rule** | referendum returns | **verify first** |
| 41 | The morning of 9 April, hour by hour | schematic | n/a |
| 41 | Danish exports by destination, 1938–1943 | *Statistisk Årbog* | located |
| 41 | March 1943: turnout, and what the Nazi party got | election statistics | located |
| 42 | October 1943: to Sweden, to Theresienstadt, and the difference | museum/Yad Vashem figures | needs source |
| 42 | Sabotage actions by month, 1943–45 | Frihedsmuseet series | needs source |
| 42 | The People's Strike, five days | schematic | n/a |
| 43 | The retsopgør: charged, convicted, executed | official retsopgør statistics | needs source |
| 43 | Bornholm: liberated last, occupied longest | schematic | n/a |
| 43 | Which way to lean, 1945–49 | schematic | n/a |
| 44 | **1953 against 1939: the same threshold, cleared** | referendum returns | **the key figure** |
| 44 | Two chambers to one: the Landsting 1849–1953 | Rigsdag statistics | located |
| 44 | What §20 installed, and what walked through it in 1973 | schematic | n/a |

### 13.1 The source route, which is new

`dst.dk` hosts the scanned back-catalogue of *Statistiske Meddelelser* with OCR
text, and it fetches. The 1954 unemployment volume (4. række, 160. bind, 4.
hæfte) gives annual average unemployment percentages directly: **1945 13.4, 1946
8.9, 1947 8.9, 1948 8.6, 1949 9.6, 1950 8.7, 1951 9.7, 1952 12.5, 1953 9.2, 1954
8.0** — and the note that 1954's 8.0 was the lowest since **1920**. The same
volume lists its predecessors by series and volume number: 1910–40 in five-year
volumes, 1940–53 annually. **The annual series 1910–1954 is obtainable from the
department that computed it.**

Three qualifications. The OCR is lossy — the column headers of that very table
render 1952 as "1962" and 1945 as "1946" — so every digit must be confirmed by a
second appearance, and each figure script's docstring records volume, table and
page rather than "Danmarks Statistik". Only the 1954 volume has been fetched;
identifiers for the earlier volumes are still to be found. And the container's own
network cannot reach `dst.dk` — only the fetch tool can — so the numbers travel
into the scripts as a cited literal block and everything derived is computed.

### 13.2 Eight schematics is more than any previous part

A third of Part I's figures carry no numbers. That is deliberate for occupation
and constitution chapters, where the honest thing to draw is a structure rather
than a measurement, and it is the plantation-plat rule working. If it reads thin,
the fix is to convert the two 1943–45 schematics into the data figures above
them, not to invent numbers for the constitutional ones.

### 13.3 The map

Chapter 38 wants a map of the two plebiscite zones. It would be the eighth map;
`mapfixture.py`, `seamcheck.py` and the shared-seam rule all apply, and the 1920
border is a different line from the 1864 border already drawn. It is the only new
map Part I needs, and it **collides with item 48, Ærø**, which edits `DENMARK`'s
vertex list that the new map would inherit. If Ærø is to be fixed at all, fix it
before the 1920 map is built.

---

## 14. The verification queue

In this order, before any drafting.

1. **The 1939 and 1953 referendum arithmetic** (§8 §10, §12 §03). Load-bearing
   twice over.
2. **Whether the 1933 social reform restored the franchise to poor-relief
   recipients** (debt 3's residue, §8 §06, and a vignette).
3. **Steincke 1920** (§7 §08).
4. **The unemployment volumes 1910–1940** — find the identifiers, confirm the
   tables fetch, transcribe with a second-appearance check.
5. **Whether the same route reaches the Folketing election results 1872–1901 and
   the kapitelstakst back-series** — items 53 and 60. If it does, four figures
   across Parts G and H become redrawable as planned and two library errands are
   retired. **Do this before any trip to a reading room.**
6. The six unnamed vignettes, in the order 44[f], 43[n], 40[f], 41[f], 39[n],
   38[n] — the first is the ending and the hardest.
7. The Sønderjysk war dead: the commonly cited range is 5,300–6,200 and the plan
   will not use a round number without a source.

---

## 15. Open, and needing Carsten

- **The ending vignette, 44[f].** Likely sources are local newspapers from the
  week of 28 May 1953 or a local archive's referendum material. Not blocking the
  plan; blocking the last section of the last chapter.
- **Ærø, item 48**, and now before the 1920 map rather than after.
- **Chapters 25, 26 and 27 render four Summary items** under a heading promising
  five (item 19). Unchanged by this plan; still his call.
- **Items 53 and 60**, but see §14.5 — do not travel until the fetch route has
  been tried.

## 16. Standing rules this plan was drawn under

Compute numbers, do not type them, and treat every "N years after" as a claim
(D-8). Verify before writing. Rasterise and look at every figure. Compute every
dimension in a figure script. A guard that is written and not wired in is worth
nothing. Assert on every scripted replacement, then grep for the new string.
Predict the symptom before making the change. Enumerate what you want, not what
you want removed. Never hand over or commit a generated file. And measure each
draft's weight profile against this plan **before** reading it for quality: a
profile with no heavy sections is a defect regardless of word count (item 59),
and `narrative.py` now reports on the same scale this plan is written in.
