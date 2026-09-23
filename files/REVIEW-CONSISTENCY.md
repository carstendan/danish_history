# REVIEW — DOES THE BOOK AGREE WITH ITSELF

*19 September 2026. Step 2 of the consistency review (START_HERE_review.md). A
fresh clone at `c5775cf` + the START_HERE commit, cold run matching every expected
figure. Four sweeps, each a script that reads the **built pages** through
`reviewlib.py`, standard library only:*

| sweep | script | reads | rows to read | confirmed faults |
|---|---|---|---|---|
| glossary | `sweep_glossary.py` | every `<dt>`/`<dd>` | 20 pointers, 7 head clashes, 6 spellings, 3 same-page | **20 + 2 + 3** |
| names | `sweep_names.py` | all reading text | 17 regnal, 8 orthographic, 121 near, 29 exonym | **see §2** |
| dates & figures | `sweep_facts.py` | all reading text | 1 event, 2 dates, 0 years, 5 counts | **0** |
| arrows | `sweep_arrows.py` | 254 arrows, prose refs, footers, titles | 44 solvency, 14 D-1, 5 direction, 4 titles, 4 prose, 3 h1 | **22 + 3** |

*A script row is a reason to read, not a verdict (`REVIEW-BUILD-FAULTS.md` §4: "a
metric is a way of deciding what to read"). Every verdict below was made against
the page text, and where it cites the ledger, against `HANDOFF.md`.*

**Where a fix can go.** This decides everything else, so it comes first.

| chapters | source | a fix goes into | state |
|---|---|---|---|
| 01–11 | none in the repo | — | ~~**blocked**: no body (`tidy` §4)~~ **unblocked, session 3**: `c01`–`c11_body.html`, authored; `build_parts_abc.py` |
| 12–15 | none; `e12`–`e15` missing, ten SVGs with no generator | — | ~~**blocked** (open item 3)~~ **unblocked, session 3**: `c12`–`c15_body.html`, authored, and eleven `svg_*.txt` written out of the pages; `build_part_d.py` |
| 16–24 | `cNN_body.html`, **authored**, no draft exists | the body | fixable; rebuild E and F |
| 25–31 | `PART_G_DRAFT.md` | the draft | fixable; `mkbody` then G |
| 32–45 | `cNN_draft.md` | the draft | fixable; `mkbody` then H/I |

For 16–24 the body *is* the source — `LEDGER_PASS.md` calls them "authored bodies",
and `debuild` reports them as matching "the retained source". START_HERE's "never
`cNN_body.html`" is about bodies that `mkbody.py` generates; these are not. I have
edited them and say so in item 139, because it is the one place this delivery
touches a file named `cNN_body.html`.

**Pages 01–15 can be unblocked.** `debuild.py extract` exists to recover a body
from its page losslessly (verified byte-identical on chapter 11, per its
docstring), with SVGs kept inline. Every finding against 01–15 below is recorded
and waits on that decision (§5, D-A).

---

## 1. Glossary

### 1.1 Twenty pointer entries — eighteen of them are an author's note on the page

The index promises: *"Danish terms kept where they carry meaning … and glossed on
first use in each page."* Part I stopped doing that. On pages 40, 41, 43, 44 and 45,
eighteen glossary entries have as their **entire definition**:

> *glossed in chapter 39 — reference, do not re-gloss.*

That is an instruction to whoever drafts the next chapter, printed in the place the
reader looks for a meaning. `draftnotes.py` does not look for it; `appcheck.py`
counts it as prose. Two more (34 *Ejderpolitik*, 35 *optant*) are pointers too, but
written to the reader ("glossed in chapter 34; the consequences arrive here") —
those two are fine as prose and still break the index rule.

**Two of the eighteen point at the wrong chapter:**

| ch | term | says | actually glossed in |
|---|---|---|---|
| 45 §03 | *grundlovsændring* | chapter 33 | **40** (33 glosses *Grundloven*, not the amendment) |
| 45 §05 | *fattighjælp* | chapter 35 | **40** (35 never uses the word) |

**Fixed in source:** all eighteen now carry a one-line definition taken from the
chapter that glosses the term in full, followed by "(chapter N)". The two
insolvent pointers now say 40. `draftnotes.py` gains the phrase `do not re-gloss`
as a drafting note, so it cannot ship again. No decision needed: the index rule is
already written and the pages broke it.

**The guard found nine more the moment it existed**, in drafts 32, 33, 34, 36,
37, 38, 39 (two) and 40 — the same note written as a free-standing list item
rather than a glossary entry. `mkbody` drops free-standing items, so none of them
was on a page; each marks a term the page uses and does not gloss. Two were
written across a line break and my own grep missed them; `draftnotes.py`
normalises whitespace (item 69) and did not. Resolved:

| ch | note | done |
|---|---|---|
| 32 §06 | *stænderforsamling* "glossed in chapter 25" | **Glossed.** The note was wrong twice: 24 glosses it, not 25, and 24's is the one-off estates meeting of 1660 while 32's are the four advisory provincial assemblies of the 1830s — a different institution under one word. |
| 33 §02 | *Kongeloven* in 25, *up ewig ungedeelt* "in 19" | **Both glossed.** 19 never glosses *up ewig ungedeelt*. |
| 36 §01 | *Folketinget*, *Landstinget* in 33 | **Glossed**, against 36's own figure. |
| 34, 37, 38, 39, 40 | *helstat*; *Systemskiftet* etc.; *Slesvig* etc.; *gullaschbaron*, *sikringsstyrke*; *Septemberforliget* | **Removed, pages unchanged.** The terms stay unglossed on those pages — a breach of the index rule the pages already carried. Left for each part's reading pass rather than written blind. |

And one pointer inside a real gloss was wrong: 33's *Rigsdagen, Folketinget,
Landstinget* said the privileged Landsting franchise "came in 1866 (chapter 36)".
It came in 1866 in **34**, whose §09 is *The constitution of 1866*; 36 describes
its consequences. Fixed.

**After the rebuild** (scratch copy, E–I, `linkindex`, `index_generator`):
`sweep_glossary.py` reports 2 pointers, both written for the reader (34, 35).

### 1.2 One term, glossed to mean different things

Seven terms have glosses whose heads share no content word. Read against each
other:

| term | where | verdict |
|---|---|---|
| ***fæste*** | 17 "Tenancy" · 32 "copyhold" | **Fault, fixed in 32.** *Copyhold* is English manorial tenure by copy of the court roll; *fæste* is a contracted tenancy under a *fæstebrev* (28 glosses the letter). 17, 21, 28 and 29 all say tenancy or tenant; 32 alone said copyhold, five times. `PLAN_H.md` had asked for exactly this check — "`fæste` and `selveje` need checking against Parts F and G before §07 uses them" — and it was not made. 32's gloss and its prose now say tenancy, or *fæste*. |
| ***håndfæstning*** | 14 "Literally 'hand-fastening' … The first is 1282 … one at almost every accession" · 25 "literally a handshake … **Every** Danish king **from 1320** signed one" | **Fault, fixed in 25.** Two disagreements: the literal meaning, and the start and universality of the series (14, 16 and 18 all say 1282 and "almost every"). 25 now says "hand-fastening", keeps 1320 as the first *accession* charter proper — which is a sharper statement than 14's, not a contradiction of it — and says "almost every". |
| *vornedskab* | 19, 21, 27, 28 | Consistent. 28's "ended by attrition from 1702" refines 19's and 27's "abolished 1702" rather than contradicting them. |
| *hovedgård* | 9 "magnate's farm" · 17 "a manor" · 21 "manor farm" | Consistent — 9 is Iron Age usage. |
| *Dannebrog* | 13 "flag" · 19 "banner" | Consistent; 19's is the object lost at Hemmingstedt. |
| *herremand* | 19 · 21 | Consistent. |
| *husmand* | 28, 29, 35 "cottager" · 37 "smallholder" | **Minor.** 37 contrasts with *gårdmand* and "smallholder" suits that sentence. Left. |

### 1.3 Spelling of one term in the `<dt>`

*helstat* (31, 33) / *helstaten* (20); *rigsråd* (15–25) / *rigsrådet* (21, 24);
*lagting* (21) / *Lagtinget* (44). All are the definite and indefinite forms of one
word, and the book has no rule for which form a `<dt>` uses. **Not worth a
convention.** Recorded so the whole-book read does not rediscover it.

### 1.4 The same term glossed twice on one page

03 *landnam* (§01, §03), 03 *langhus* (§04, §10), 14 *Danehof* (§04, §05 — the first
entry even says "It becomes central in the next section", which then glosses it
again). All three are on blocked pages. **Fixed, session 3**: in each pair the gloss that
stands at the term's first use in prose was kept and the other folded into it — *landnam* §03
(it is not used in §01's prose at all), *langhus* §04, *Danehof* §05 (the §04 entry was a
forward note: "It becomes central in the next section").

---

## 2. Names and spellings

### 2.1 Regnal numbers — the house style is "Christian 4.", and Part I breaks it

The book writes Danish and Scandinavian kings in the Danish style — "Christian 4.",
"Frederik 7.", "Karl 12." — and foreign rulers in Roman ("Frederick II" of Prussia,
"George III"). **This is not written down anywhere**; proposed as D-14 in
`CONVENTIONS.md`.

| ch | Roman form | beside it on the same page | fix |
|---|---|---|---|
| 41 | Christian X ×2 | Christian 10. ×1 | **fixed** |
| 42 | Christian X ×3 | Christian 10. ×4 | **fixed** |
| 44 | Christian X ×2 | — | **fixed** |
| 41 | Haakon VII | (Karl 12., Karl 10. Gustav elsewhere) | **fixed**: Haakon 7. |
| 31 | Gustav IV Adolf | | **fixed**: Gustav 4. Adolf |
| 05 | Frederik VI ×2 | | **fixed**, session 3 |
| 07 | Christian IV | | **fixed**, session 3 |
| 10 | Frederik VII | | **fixed**, session 3 |

Chapter 22's hit ("Jens Christian V. Johansen", a historian) is a name, not a king.

### 2.2 Place names — the book has two conventions and switches between them by session

**Schleswig / Slesvig** is the largest disagreement in the book. Counting the bare
word (not *Schleswig-Holstein*, not *First Schleswig War*):

```
Parts A–F   Schleswig in every chapter; Slesvig in 12 (3) and 19 (2)
Part G      Slesvig in 26, 27, 28, 29, 31 — Schleswig only in a visit block
Part H      32: Schleswig 26, Slesvig 1   ← the odd one out
            33–36: Slesvig
Part I      37–39: Slesvig · 40, 41: Schleswig · 44: both
```

It follows the drafting sessions, not a rule. The same drift, smaller:

| pair | where both appear |
|---|---|
| Flensburg / Flensborg | 33, 34, 38 each use both in prose |
| Holstein / Holsten, Lauenburg / Lauenborg, Kongeåen / Kongåen | 34 — the map caption uses the Danish forms, the prose the German |
| Danevirke / Dannevirke | 34 writes Dannevirke (12×), every other chapter Danevirke. 32's *Dannevirke* is the newspaper, correctly. |
| Malmø / Malmö | 19, 20 Danish; 15, 24, 33 Swedish |
| Skanør / Skanör, Brømsebro / Brömsebro | prose Danish, visit blocks Swedish — this one looks deliberate |
| Helgoland / Heligoland | 34 uses both |
| Lagting / Løgting | 34 and 44 Danish, 41 Faroese |

And one plain misspelling: **"Ditmarschen"**, fourteen times in 19, 20 and 21. It
is neither the German *Dithmarschen* nor the Danish *Ditmarsken*, both of which
chapter 19's own glossary uses.

Chapter 38 is the one place with a stated rule of its own: its glossary says the
chapter "uses whichever one the person speaking would have used" — Slesvig or
Sønderjylland. That is a good rule for quotation and a hard one for narration,
and no other chapter follows it.

**This needs one decision** (§5, D-B), because the fix is a hundred-odd edits in one
direction or the other and the direction is editorial. My recommendation is in §5.

### 2.3 English and Danish forms of people's names

Cnut (8–13) against Knud (12 onward), Sweyn (8–11) against Svend (12 onward),
Harold (11, English kings) against Harald: **deliberate and right** — Viking-age
kings under their English names, from Knud the Holy on under their Danish ones.
Margrete (14–20) against Margrethe (45, the princess of 1953): right. Nothing to do.

### 2.4 Near-spellings that are the same person

None confirmed. The 121 pairs are distinct people or places (Clemmesen the
historian in 39, Clemmensen the editor in 44; Magnussen/Magnusson/Magnússon; Laurids,
Laurits, Lauritz). Read and discarded.

---

## 3. Dates and figures

**No cross-chapter disagreement found.** The candidates, read:

- *Peace of Prague*, 1866 and 1878 in 34 — the peace, and the annulment of its
  article 5. Correct.
- Rønne, 8 and 9 May 1945 (43, 44) — the bombing and the Soviet landing. Correct.
- Rønne, 8 and 23 May 1945 — the bombing and the Hotel Dana. Different events.
- Five count pairs on "Danes" and "Germans" — different populations.

**What this sweep can and cannot see.** The book writes most counts in words
("about twenty-two thousand"), so the script converts number words with a scale
word to digits before comparing; without that it found nothing at all. It compares
facts tied to a name that recurs in two to eight chapters. It **cannot** see a fact
stated in two chapters with no shared name nearby, a count with no scale word
("forty-six men"), or a disagreement *inside* one chapter — chapter 42 gives the
October crossing as "about 7,000" in its checkpoint and "about 7,400" in its prose
and Meanwhile box, which is rounding in one direction and not a fault, but it is the
kind of thing the reading pass will meet. A zero here means "none that the method
reaches", and the reading pass is the other half of it.

---

## 4. Arrows

254 arrows and 37 "Thread" notes in 44 carry-forward blocks. 210 arrows pass the
anchor test; 44 were listed and read.

### 4.1 THE AUGUST LEDGER PASS IS NOT IN THE REPOSITORY

`HANDOFF.md`, *Debts — Part F closed*, lists sixteen forward arrows from 20–24
"as they now stand in the shipped files … this is the state on disk, not the
plan". **Eight of the sixteen are not on disk.** The bodies and the pages at
`c5775cf` carry the arrows from before the pass:

| arrow | ledger says | on disk | on disk is |
|---|---|---|---|
| 20, *adelsvælde* after 1536 | → Part G | → 25 | D-1 break (20 is Part E) |
| 20, Norway clause to 1814 | → Part G | **→ 28** | wrong: 1814 is 31 |
| 21, the Gottorp line to 1720–21 | → 27 | **→ 26** | wrong: Gottorp is settled in 27 |
| 21, labour services and the bond | → 28, 29 | → 28 | half: the reforms are 29 |
| 22, Trankebar and the company | → 30 | **→ 27** | wrong: 27 is the Great Northern War |
| 22, Norwegian law of 1604 | → 28, 31 | **→ 30** | wrong: 30 is the Atlantic |
| 24, the Atlantic and the slave forts | → 30 | **→ 27** | wrong — the very arrow the ledger says it caught |
| 24, Skåne not quietly Swedish | → 26, 27 | **→ 29** | wrong: 29 is Struensee |

The repository's first commit is 1 September 2026 and the pass is dated August, so
the edits were made to a copy that never reached it, and the ledger recorded the
plan as the result. **Item 112's rule applies with the sign reversed: here the
repository is right about what it contains and the ledger is wrong about it.**
Fixed in the bodies to exactly what the ledger records; each was read against its
target first (item 101).

### 4.2 Stale numbers the pass never reached — Parts A–E

The same Part G shift (six chapters became seven) left these pointing one or two
chapters short. Each read against its target:

| page | arrow or prose | points at | should be | state |
|---|---|---|---|---|
| 04 | → 27, 29 "The overseas empire…", "The flourishing trade period…" | the Sound war; Struensee | 30, 31 → **Part G** | **fixed**, session 3: the arrow's own text names the Sound Dues and the neutrality trade, so `→ Part E, Part G` |
| 06 | → 27 "The overseas empire and the slave trade" | the Sound war | 30 → **Part G** | **fixed**, session 3 |
| 07 | → 31 "Golden Age and national awakening" | the Napoleonic wars | 32 → **Part H** | **fixed**, session 3 — and it was insolvent at any number: 32 names Oehlenschläger once, at the head of a list, and never the horns. The arrow and 07 §03 now promise only that the Golden Age is Part H's subject |
| 06 §01 | "the Napoleonic wars in 30" | the Atlantic | **31** | **fixed**, session 3: the numbers dropped from the whole list (18, 20, 30), which is D-1 extended to prose |
| 07 §03 | "chapter 31 will pick the thread up when it deals with the Golden Age" | | **32** | **fixed**, session 3, as the arrow above |
| 18 | → 28 "The Bergen treaty of 1450 ties Norway to Denmark until 1814" | the bound countryside | → **Part G** | **fixed** |
| 18 §10 | "until 1814, which is chapter 28" | | Part G | **fixed** |

Chapter 15's `→ 30, Part I` (Estonia 1346, the West Indies 1917) is `LEDGER_PASS`'s
deferred row, now correct in content and in the mixed form below.

### 4.3 D-1 breaks that point at the right chapter

`2 → 5, 8`; `6 → 9, 18`; `9 → 18`; `14 → 20, 24, 25`; `15 → 30`; `17 → 27`
(Egede, correctly); `20 → 25`, `20 → 28`. All predate D-1 and all but `20 → 28`
land on the right page today. **D-1 is a rule about arrows going stale, and these
did not.** Rewriting correct arrows to part letters buys nothing now; rewriting
them when their pages are next rebuilt is free. The two in chapter 20 are fixed
with 4.1 because the ledger already prescribes them. The rest are listed for when
Parts A–D are unblocked.

**Fixed, session 3**, each read against its target first: `2 → 5, Part C`; `6 → 9,
Part E`; `9 → Part E`; `14 → 20, Part F, Part G` (and its quoted "title", which was a
description, is now 20's title; "every Danish king" is "nearly every", as 14's own
glossary says); `15 → Part G, Part I` (30 does carry the Tranquebar and Guinea sales);
`17 → Part G`. Two more the sweep cannot see, because they sit in Thread notes: 07 and
08 both said 1864 was "chapter 33". It is 34; both now say Part H. And 08's discussion
question pointed at "the colonial period of chapter 27", now Part G.

### 4.4 Chapter 37 points at its own part five times

`→ Part I` ×5 in chapter 37, which is itself in Part I — written when 37 closed
Part H, before D-10 moved it. Each read and re-pointed to a number, which D-1
allows inside a part:

| arrow | → |
|---|---|
| Nordslesvig's conscripts come home in 1920 | **38** |
| The twenty-five million dollars and Greenland; "chapter 44 settles what that was worth" | **44** |
| The seven categories: poor relief restored 1933, voting age 1953 | **40, 45** |
| The Landsting's quarter and its age of thirty-five; both go in 1953 | **45** |
| Zahle's ministry meets the king in 1920 | **38** |

### 4.5 Quoted titles, footers and headings

Parts A–D quote the target's title inside the arrow. Four quote a title that
belongs to a different chapter now — the four stale arrows of 4.2. The footers
`next: N — title` all agree with `<title>`.

**Pages 05, 06 and 07 have an `<h1>` that is not their title.** The `<title>`,
the index spine, the footer of the previous page and every arrow into them say
"Pre-Roman Iron Age: bogs, war-boats and the Celtic world"; the page's own heading
says "Bogs, war-boats and the Celtic world". Same for 06 and 07. That looks like a
retitling made on the heading only. Blocked pages; recorded.

**Fixed, session 3, in the direction of the title**: the title is what the index, the
footers and every arrow use, and every other page's `<h1>` is its title. Chapter 07's
filename (`gold-catastrophe-and-a-people-with-a-name`) keeps the heading's wording; it
is a URL and is not renamed.

**Found beside it, session 3: pages 18, 19 and 20 carried the wrong number in
`<title>`** — "17 ·", "18 ·", "19 ·", the browser tab only; crumb, footer and index were
right. Residue of the August renumbering. Check 9 strips the number before comparing,
so it could not see this; `sweep_arrows.py` now has a check 9b for it. Fixed in the
three authored bodies.

### 4.6 Forms the cross-reference table does not list

`6 → 10, Part H`, `15 → 30, Part I` (number and letter in one arrow) and `19 → Part
H, Part I` (two letters). HANDOFF's table of six forms has neither. They read fine
and the sweep parses them; **add them to the table as the seventh and eighth
forms** rather than rewrite them.

### 4.7 Solvency

The 44 arrows the anchor test listed, read: 31 have no testable anchor (a title and
an idea — "the taste for metal established here becomes the amber trade") and
deliver. Of the 13 with anchors, 8 are the stale arrows above. The remaining five:

- `29 → 31` "Neutral Denmark's trade boom begins under Guldberg during the American
  war" — **31 never names Guldberg or the American war.** 31 opens in 1784 and the
  boom it describes is the 1790s. Either the arrow promises the wrong thing or 31
  does not pick the thread up. **For the Part G reading pass.**
- `21 → 25`, `23 → 25` *adelsvælde* — 25 never uses the word; it delivers the thing
  (the council's end in 1660). Solvent.
- `8 → 10` Harald Klak — 10 delivers Harald Bluetooth, which is the second half of
  the arrow's sentence. Solvent.
- `22 ← 20` "the Devil, 1617" — backward, and chapter 22 is the one with 1617.
  Solvent.

### 4.8 Chapter 45's carry-forward

A heading over an empty list, as known (`REVIEW-BUILD-FAULTS.md` §5.3). In §5 as a
decision.

### 4.9 The spine has an eleven-year hole

Not an arrow fault, found by the same read of declared spans. **33 is 1848–1852 and
34 is 1863–1864.** Nothing declares 1852–1863 — the helstat constitution of 1855,
the end of the Sound Dues in 1857, the 1858 suspension for Holstein — and the index
shows the gap exactly as it showed 1920–1929 before D-10, which called that "visible
to a reader … not merely a planning inconvenience". 34 §01 opens on 1863 and looks
back. **For the Part H reading pass**: whether 33 or 34 carries those years in
prose, and if so, whether the declared span should say so.

---

## 5. Decisions this opens — for Carsten, one at a time, each with a recommendation

*All four answered on 19 September 2026, with Part I's five: see §6.4.*

**D-A. Unblock chapters 01–15?** `debuild.py extract` recovers their bodies
losslessly; Part D also needs its ten SVGs written out from the pages. Without it,
fifteen findings above stay on the pages for good: five stale arrows and prose
references (04, 06 twice, 07 twice), four Roman regnal numbers (05 twice, 07, 10),
three `<h1>`s (05, 06, 07) and three same-page glosses (03 twice, 14).
*Recommendation: yes, as its own short session before the Part A reading pass —
extract, rebuild, confirm `debuild verify` reports identical, then fix.*

**D-B. Schleswig or Slesvig?** And with it Flensburg/Flensborg and the other 34
pairs. *Recommendation: **Schleswig** for the duchy and the region, throughout —
it is an English-language book; the chapter titles, the index and the war names
already say Schleswig; Parts A–F use it; and English historiography of the
question uses it. Danish forms stay where they are Danish words or names:*
Sydslesvig, Slesvigsk Parti, Sønderjylland, Flensborg Avis. *German-form town
names for towns that are German today (Flensburg, Schleswig the town), Danish-form
for towns that are Danish today (Haderslev, Aabenraa, Sønderborg). The Swedish
Skåne towns in their Swedish form in visit blocks and their Danish form before
1658 in prose, which is what the book already mostly does.* This is proposed as
D-15 in `CONVENTIONS.md`; the edits go chapter by chapter with each part's reading
pass, not in one sweep.

**D-C. Chapter 45's empty carry-forward.** *Recommendation, as before: suppress
the heading when the list is empty.* It is the last page, and backward arrows
there would duplicate its own summary.

**D-D. D-13, the vignette rule.** Agree it as written in `CONVENTIONS.md`, and the
six vignettes are decided under it part by part. The Part I reading found a
seventh (§6.3, I-3).

---

## 6. Part I, read — chapters 37 to 45

*Every section of all nine chapters read in the drafts, against the chapters'
own Sources and each other. Errors of fact and of the book's own consistency are
fixed below and listed; cuts, moves and anything else that changes what a reader
meets are Carsten's, in §6.3.*

### 6.1 The boundary pass left its old numbers behind

Item 136 re-cut 42–45 at the material's seams and re-pointed fifteen arrows and
six prose references by hand. Nine more references inside the prose and
apparatus were never on its list, because they are section and chapter numbers
written into sentences rather than arrows. **All are fixed.**

| ch | said | now | why |
|---|---|---|---|
| 45 §01 | "occupied in **six hours**" | "between four and eight one morning" | item 117 struck "six hours" from chapter 41 and the index; it survived here |
| 45 §02 | "formed **eighteen months** earlier, and it contained something Denmark had seen once before, **twenty-three years and six months** earlier" | **paragraph removed** | a set-up for Fanny Jensen, whose vignette moved to 44 in item 136; the page never paid it off. And Hedtoft's government of 13 November 1947 was sixteen completed months old on 4 April 1949, not eighteen (D-8) |
| 45 §04 | "§04 is about what she lost" / "the subject of §05" | §06 / §07 | section numbers from the three-chapter draft |
| 45 §05 | "and §10 says so" | §12 | the same |
| 45 §11 | "**forty-three** chapters" | forty-four | the book had 43 chapters before D-10 |
| 45 coda | "Fifty-four years, **eight** chapters" | nine | Part I has nine since item 136 |
| 45 myth-check, Sources | "§07 exists to put", "§06 turns on" | §08 and §09, §08 | the Greenland sections |
| 43 glossary | *stikker* "the other column of **§08**'s ledger" | §02 | 43 has six sections |
| 40 §11 | "Chapter **44** has that vote" (1953) | 45 | |
| 44 §01 | "**What that produced** is not measurable…" | "What seven and a half months without a police force produced…" | the antecedent is the last section of 43; a reader who opens 44 had nothing for "that" to point at |

### 6.2 Errors of fact and of the book against itself — fixed

- **45 §03 and §06 — the succession.** The chapter said Frederik 9.'s daughters
  were barred "under the royal law of 1665", which "was agnatic and emphatic".
  Chapter 33's own gloss says the Kongelov was *agnatic with a cognatic fallback*,
  which is the whole of the 1848 crisis; what barred women in 1953 was **the
  succession law of 1853**, written to end that crisis on Christian 9.'s male
  line (danmarkshistorien.lex.dk, *Grundlovsændringen 1953*: "den hidtidige
  tronfølgelov"). §06 rewritten to say so — it keeps its argument, which is
  sharper now: Denmark answered the crisis of 1848 in 1853 by shutting women out,
  and took a century to let one in half way. The aside that Margrethe's
  thirty-seven years were "rather longer than the male line managed between 1863
  and 1947" is cut: Christian 9. reigned forty-two.
- **45 §11 — "twice declined when it was offered again."** Chapter 44 §06 spends
  a section establishing that 1946 was *not* an offer. Now: "twice Denmark has
  declined to move it when more was within reach."
- **45, Helga Pedersen's vignette.** "Four years old when Danish women got the
  vote": born 24 June 1911, she was three on 5 June 1915 — now "not quite four".
  Max Sørensen "dies in it himself twenty-one months later": 27 January 1980 to
  11 October 1981 is twenty completed months; now "in October 1981" (D-8; lex.dk
  for both dates).
- **45 §07 and 41 §11 — two turnout records that could not both hold.** 41 called
  1943's 89.5 per cent "the highest turnout in Danish history before or since";
  45 called 1972's 90.1 "the highest participation in any Danish vote in this
  book" — and chapter 38 prints Zone I's 91.5. Now 41 says "at any Danish general
  election" (in the prose, the summary, `mkbody.py`'s hook and `figs_41.py`'s
  figure note, which is re-rendered and was looked at), and 45 says "in any Danish
  referendum". Both are true.
- **42 §05 and 41 §08, §11 — the Horserød transport.** 42 said "two ships out of
  Copenhagen in one week"; 41 said the communists went to Stutthof "on a train".
  **They sailed on 2 October 1943 in the hold of the same ship as the Jews taken in
  the raids**, to Swinemünde, then by cattle truck (Horserød-Stutthof Foreningen).
  42's sentence is now the stronger one the facts allow: *one ship out of
  Copenhagen, and only half of what it carried is in the story Denmark tells.* 41's
  "seven months after the election" (23 March to 2 October is six) is replaced by
  the date.
- **42 §05 — the Theresienstadt visit.** "A Danish and Swedish Red Cross
  delegation": it was Maurice Rossel of the ICRC and two Danish officials, Juel
  Henningsen and Hvass (USHMM). Fixed, with the source added.
- **44 §03 — "eight billion", and 44 §07's "three billion".** Both are right and
  the page never said why. lex.dk, *Danmarks historie 1940–1945*: about three
  billion of unpaid exports on the clearing account and about five billion
  advanced for the Wehrmacht's building. §03 now says so; Sources cite it. The
  same Sources said the "end of self-sufficiency" argument rested on "chapter
  **30**'s material" — the Atlantic chapter. It rests on 35's. And "§05's reading"
  of the women's figures is §04's.
- **40 §03 — Kanslergade.** The prose names ten negotiators (from Nissen); the
  vignette said "ten people in the flat and nine of them are politicians". Now
  eleven and ten. The vignette also had Hartvig Frisch asking for the decanter
  "when it is over"; Erichsen's own account, as danmarkshistorien prints it, has
  him ask the next day. And "seventy-six of a hundred and forty-nine, a majority of
  one" — chapter 39 uses the same words for seventy-five; now "one more than the
  bare seventy-five a majority needs".
- **38 §07–§09 — Easter 1920.** "The settlement of 31 March" contradicted the
  chapter's own Easter Sunday, 4 April; "a king who discovered on a Wednesday"
  matched no date in the chapter; and "read the constitution of **1866**" — in
  1920 the constitution in force was 1915's, and the myth-check and summary said
  1866 too. All fixed.
- **37's carry-forward** sent the reader to 40 and 45 for "poor relief restored in
  1933". Chapter 40 says in terms that 1933 was "not a restoration but a
  redefinition", and 45 that the vote came back in 1961. The arrow now says so.
- **33's new gloss of *up ewig ungedeelt*** follows chapter 19: Neuber's slogan of
  1841, made from a clause whose 1460 meaning is disputed.

**Checked independently.** A separate agent that had not seen the work read the
patch against its claims and the web. It confirmed the succession, the Horserød
ship, the Theresienstadt delegation, Pedersen's and Sørensen's dates, the eight
billion, the 1915 constitution and both turnout records, and it found five things
I had got wrong in the fixing, now corrected: the new 42 sentence opened "The
same transport" straight after a paragraph about Auschwitz; 38 still said 1866 in
two places; 45's Sources still cited the Kongelov; 45 now said "occupied in a
morning" twice in one section; and 32's new gloss cited chapter 28 for a term 28
does not gloss. **And one I should not have made at all:** I had changed Kristian
Rasmussen's "a fortnight's warning" in 43 to "three days'", on the reasoning that
Duckwitz passed the date on 28 September. Chapter 42 says "a fortnight's warning"
three times, because it counts from the 17th, when Duckwitz began warning
people — as its own §03 says. Reverted. Item 138's lesson, a third time in two
days.
- **37.** "There was also no election" directly after an election on 7 May 1915 —
  now "no election on the new rolls". "Two-thirds of a two-fifths turnout" three
  lines after the chapter scolds the rounding of 37.4 to forty — now "a turnout
  under two-fifths". "Held three islands for two hundred and fifty years" — St
  Thomas from 1672 is 245, St Croix from 1733 is 184; now "the better part of".

### 6.3 Decisions for Carsten — Part I, one at a time

**I-1. Chapter 43's two sections over the heavy ceiling, and what 43 repeats
of 44.** §01 is 834 narrative words and §02 820. Three things in them are said
again elsewhere:

- §01's last paragraph (the 21,800 arrested "by men who had been civilians four
  days earlier") is 44 §01's subject, and 44 says "the week before";
- §02's list of *schalburgtage* targets — Tivoli's concert hall, the student
  residence, Borgernes Hus, the porcelain factory — is repeated word for word in
  §03, where it belongs, because it is what started the strike;
- §05 ends Bornholm with the Soviet landing, the seven and a half thousand from
  Kolberg and "they stayed eleven months" — 44 §05 opens with the same three
  facts.

*Recommendation: cut all three from 43, and move two methodological paragraphs
to Sources — the four disagreeing tonnages (§01) and the railway column that does
not add up (§02). That takes both sections under the ceiling without losing a
fact, and ends 43's Bornholm on the radio ban, which is the better last line.*

**I-2. Chapter 43's order.** §06, *The policeless country*, is September 1944 and
comes after §05, May 1945. It was placed last so 44 could open on it; 44's
opener now stands on its own (§6.1). *Recommendation: move it to follow §03, so
the chapter runs June 1944, September 1944, March 1945, May 1945, and ends on
Bornholm. Rasmussen's vignette moves with it.*

**I-3. A seventh vignette that restates its section (D-13).** 42 §03, *The
warning*, is about Duckwitz; its vignette is Duckwitz on 28 September, and its
fourth paragraph repeats the section's sourcing almost word for word — the visa
records, the sealing until 2048, "a calendar and not a diary". *Recommendation:
cut that paragraph. What is left is the particular — a shipping clerk handing a
date to a party office and going back to his desk — and it is good.*

**I-4. Chapter 45's last section is named for something it no longer contains.**
*The woman at the polling station* was planned around an anonymous voter
(PLAN_I §12, decision 2.9); she became Helga Pedersen at Christiansborg, by
agreement, and the title stayed. So did its last line, "That evening the count
came in at forty-five point seven six per cent", which now follows a paragraph
about 1961 and points at no evening. *Recommendation: retitle it* The last of the
seven F's *(one entry in `build_part_i.py`), and anchor the line: "On the
evening of 28 May the count had come in at forty-five point seven six per cent,
and the thing had passed by nineteen thousand votes."*

**I-5. 44 and 45 over the 40-minute advisory, with no cut on record.** After this
session 44 is 44 minutes and 45 is 45. Having read both: 45 does not drag — its
twelve sections are short and it carries the coda for the whole part. 44's
longest section, South Slesvig (§06, 738 words), is the one I would cut from if
anything is cut, by compressing the British enquiry to its conclusion. *Recommendation:
accept both as they stand and record the defence: they are the end of the book,
inside the band, and I-1 and I-3 already take words out of the part.*

**Not decisions — open, and mine for the next session:**

- **38 §06, Sønderborg.** 2,029 Danish less 349 outvoters is 1,680, not the
  printed 1,672 — which turns "ten votes apart" into two. Either a figure or the
  subtraction is wrong, and the chapter does not source the 349/919 split.
  Chapter 38's Sources also say the Tønder return is *unresolved* while §06 prints
  761 against 2,504 as fact, and the Sources on the page still read "**not yet
  opened**" against *Statistiske Efterretninger* 1920 nr. 23 — the Danish official
  publication of the returns, which Danmarks Statistik may have online. Open it
  first.
- **38 §04 states the Ribe clause as a promise of territorial indivisibility** —
  "bound Slesvig and Holstein to be *up ewig ungedeelt* — forever undivided" —
  and builds its paragraph on it. Chapter 19 says the 1460 meaning is disputed,
  that the slogan is Neuber's of 1841, and that the nineteenth-century reading
  "is the one with the least support". 38 should either hedge or say it is
  following the reading 1920 believed.
- **42's Sources list 43's open questions** (the railway column, the July 1944
  return to work, Kim Malthe-Bruun's "Niels"): a leftover from the three-chapter
  draft. Move them to 43.
- **39 §10 and 40 §01 say the same four facts** (Stauning's second government,
  Munch for eleven years, Steincke, the law of 1 June 1929), one as a close and one
  as an opening. Normal at a seam; noted, not recommended for a cut.
- **37 §09** calls the case for keeping the West Indies "the better argument"
  without saying why. A judgement the book should either defend or drop — for the
  Part I prose read Carsten has said he will do.

### 6.4 What was decided — session 2, 19 September 2026

Each decision was put on its own, with its recommendation, and applied before
the next one was put. One commit each, all pushed.

| decision | answer | where it landed |
|---|---|---|
| **D-D** agree D-13 | **yes** | `CONVENTIONS.md`: D-13 in force. The seven cases it names are decided part by part: 42 §03 now (I-3); 22 §08 (F), 26 §09, 27 §05, 27 §09, 29 §03 (G), 35 §03 (H) wait for their parts' reading passes |
| **I-1** 43 repeats 44 | **yes** | the three repeats cut; the tonnages and the railway column moved to 43's Sources; Bornholm ends on the radio ban |
| **I-2** 43's order | **yes** | *The policeless country* follows the strike: June 1944, September 1944, March 1945, May 1945. The checks in `build_part_i.py` were re-keyed so none asks about a section not yet read |
| **I-3** the seventh vignette | **yes** | 42 §03's Duckwitz vignette lost its sourcing paragraph. What is left is the clerk and the date |
| **I-4** 45's last section | **yes** | retitled *The last of the seven F's*; the closing line anchored to the evening of 28 May |
| **I-5** 44 and 45 over the advisory | **accepted, and more than accepted** | Carsten's rule, now **D-16**: length is never a reason to cut. Keep what the story needs; move material between chapters where that is better; leave what is good. The 40-minute figure is an advisory, not a limit. No cut was made to 44 or 45 |
| **D-C** 45's empty carry-forward | **yes** | `mkbody.py` leaves the heading out when the draft has no arrows; `build_part_i.py` requires `no_forward=True` on that chapter and refuses a page where declaration and body disagree, in either direction. Tested both ways |
| **D-B** Schleswig or Slesvig | **Schleswig**, as recommended | **D-15 in force.** Applied to Part I: 23 prose changes in 37, 38, 44, 45; "Slesvigsk Parti" in 39 and its figure; `figs_38` (Flensburg, Schleswig), `figs_43` (South Schleswig, and a stale section number). Bare "Slesvig" remains in 12, 19, 26–29, 31–34 and 36, 104 times: each part's own pass. The spine maps (`map_*.py`) still label in Danish: a separate decision, not taken |
| **D-A** unblock 01–15 | **yes** | its own session, next, before the Part A reading. `START_HERE_review_3.md` |

**Still open, and mine** — carried to session 3, unchanged from §6.3: 38's
Sønderborg arithmetic and Tønder figure (*Statistiske Efterretninger* 1920 nr. 23
not yet opened); 38 §04's Ribe clause stated as territorial when chapter 19 says
the reading is disputed; 42's Sources listing 43's open questions.

**Book after the session:** 45 of 45, **336,690 page words**, 26.7 h; Part I
74,233. The fall from 336,857 is I-1 and I-3.

**All three closed in session 3** — §7.3.

---

## 7. Session 3 — chapters 01–15 unblocked, and Part A read

*19 September 2026, from `START_HERE_review_3.md`. Cold run on a fresh clone of
`6aed653`: every figure as expected. Four commits: the recovery alone, then the A–D
fixes, then the Part I items, then Part A.*

### 7.1 The recovery (D-A)

`debuild.py extract` for 01–15 gave fifteen bodies, now `c01`–`c15_body.html`,
**authored source from here on**, as 16–24 are. Four things the recovery found on
the way, none of them in the plan:

- **`build_parts_abc.py` already existed.** START_HERE asked for A–C build scripts
  to be written; there was one, with every section list already matching the pages.
  It could not run for the reason HANDOFF open item 4 gives: it replaced a `--part`
  token that `style.css` had renamed `--band`, and so did `build_part_d.py`. Both
  now refuse on a missing token, as `build_part_e.py` does. Open items 3 and 4 close.
- **Page 14 has three figures; `build_part_d.py` knew two.** The Skåne herring
  market diagram is now `svg_herring.txt`: eleven SVGs written out, not ten.
  `svg_plague.txt` already matched page 15 byte for byte.
- **Chapter 14's config listed an eleventh section**, "What it was actually for",
  that the page has never had. Both builders now refuse a config whose section ids
  disagree with the body.
- **Chapter 12's third checkpoint had been corrected on the page and never in
  the script** — an artifact-only edit, the class HANDOFF has closed four of before.
  The page's wording is kept.

The rebuilt pages differ from what shipped in two places only: the stylesheet
(current `style.css`; it renders the same, except that 01–11's "← Index" crumb
now gets its part colour, which `var(--band)` could not give a page that defined
`--part`) and the "about N minutes" stamp, recomputed by `pagewords` and one or two
minutes lower. **debuild: 45 identical.** Verified again by applying the commit
to a fresh clone and rebuilding: byte-identical to the working tree.

`vignettes.py` reads bodies, so it saw 01–15 for the first time: 109 vignettes
with a place, 79 distinct (was 89/61). `figcheck` 98 match, 30 sourceless (was
87/41): the eleven Part D figures now have sources.

### 7.2 The A–D findings

All fifteen fixed; the state columns in §1.4, §2.1, §4.2 and §4.5 say how, and
§4.3 lists the D-1 re-pointings. Three things beyond the list:

- **07's Golden Horns arrow was insolvent at any number.** Chapter 32 names
  Oehlenschläger once, at the head of a list, and never the horns. Arrow and
  prose now promise only that the Golden Age is Part H's subject.
- **07 and 08 both called 1864 "chapter 33"** inside Thread notes, where the
  arrow sweep does not look. It is 34; both now say Part H.
- **Pages 18, 19 and 20 carried "17 ·", "18 ·", "19 ·" in `<title>`** since the
  August renumbering. `sweep_arrows.py` check 9 stripped the number before
  comparing; check 9b now compares it, and reports three on the old tree, none now.

`14 → 20, Part F, Part G` and `4 → Part E, Part G` are combinations of the seventh
and eighth forms in CONVENTIONS' conflict 3; the sweep parses both.

### 7.3 The three Part I items — closed

- **38 §06, Sønderborg: two votes, not ten.** *Statistiske Efterretninger* 1920
  nr. 23 is the constitutional referendum of 6 September 1920 (item 104 found
  this; START_HERE_review_3 and 38's Sources had not caught up). The town totals,
  2,029 and 2,601, are confirmed again. The 349/919 outvoter split is Sønderborg
  Lokalhistoriske Arkiv's booklet on the vote, which prints the Danish total as
  2,021 — whence 1,672 — while its own district table sums to 2,029. 1,680 to
  1,682. Its German column also sums 200 over the confirmed 2,601; the 919 is on
  its district-6 row, in its text, and fits its "tilrejsende i alt 28%". All of this
  is now in 38's Sources.
- **38 §06, Tønder** is still two returns, 761 of 3,265 and 750 of 3,198. The prose
  no longer prints one as fact: it gives both and what they agree on.
- **38 §04's Ribe clause** now quotes 1460's words, says the meaning is disputed
  and that chapter 19 leaves it open, and keeps its argument.
- **42's Sources:** three of its eight open questions were 43's (the July 1944
  return to work and the final proclamation, the Malthe-Bruun "Niels", the railway
  column). They are in 43's Sources now; 42 keeps its own four.

### 7.4 Part A, read — errors of fact, fixed

Each checked against a source before it was changed; the sources are in the
research note behind item 141, and an agent that had not seen the work checked
every hunk afterwards (§7.8).

| ch | the page said | it is | ground |
|---|---|---|---|
| 01 §03 | the Hamburg culture "is named for the Ahrensburg tunnel valley"; glossary "named after Meiendorf" | named after finds at Hamburg; Meiendorf and Stellmoor are its type sites in that valley | the Ahrensburg culture is the one named for the valley |
| 01 §04 | flint mines "in four thousand years" | eight thousand | Hov is Early Neolithic (Trap: 3950–3301 BCE); Jels c. 12,100 |
| 01 §05 | "Denmark's first contribution to world science" was the Bølling/Allerød chronology | "a fitting Danish contribution" | Tycho, Steno, Rømer and Ørsted all came first |
| 01 §06 | radiocarbon and calendar years "differ by thousands of years"; 13,008 BP is "fifteen thousand years old" | nearly two thousand; thirteen thousand | the page's own Trollesgave figures |
| 01 §06–08, myth | Laacher See "a century and a half" before the Younger Dryas (four places); the cold at 10,900 BCE | about two hundred years; 10,850 | Reinig et al. 2021: 13,006 and 12,807 BP. **Figure 3 still draws the old gap** (§7.6) |
| 01 §10 | "Four thousand years separate" Slotseng from the last Ahrensburg camps, "the distance to Stonehenge", "a hundred and sixty generations" | about two and a half thousand; the distance to Plato; about a hundred | c. 12,100 to c. 9,700 BCE |
| 01 §03 | the Slotseng box sat on a shelf "for thirty years"; Danes had hoped for a Hamburg site "for half a century" | more than twenty; more than thirty | collected 1962, shown to Holm 1985; Rust dug in the 1930s, Fynbo's find 1968 |
| 01 §10 | the herd came "in the second half of October" | in late autumn | §03's own season, mid-October to early December |
| 02 header | five thousand years is "an eighth of the whole span" | a third | 5,050 of 14,950 years |
| 02 §02 | Hammelev gives "the first identifiable Dane", said of Åmosen | the oldest grave, which is elsewhere | chapter 1's myth-check rejects "the first Danes"; Hammelev is in Jutland |
| 02 §03 | "the next ten thousand years of Danish history" | eight thousand | from c. 6,500 BCE |
| 02 §07 | dogs "ten thousand years before" livestock | four thousand | §02 says four; Maglemose to 3,950 BCE |
| 02 §07 | amber is "found in quantity nowhere else in northern Europe" | only on these shores and the eastern Baltic's | Sambia |
| 02 §08 | "In 1850 the government appointed a commission"; Mejlgård in 1851; "three professors" | 1848, the Royal Danish Academy; 1850–51; three scholars | DBL on Steenstrup and Worsaae; Worsaae was titular professor from 1854 |
| 02 §09 | Lola's genome was "the oldest yet recovered in Denmark"; her meal included eel | neither | Allentoft 2024 includes Koelbjerg, c. 8,500 BCE; the study found mallard and hazelnut |
| 02 §06 | "an infant who never drew breath" | who may never have | the same page: "born or unborn" |
| 03 intro, fig. 3 | the ice line becomes a frontier "three thousand years later" | seventeen thousand | c. 20,000 BCE to c. 2,850 |
| 03 fig. 1 | Funnel Beaker and Single Grave overlapped "perhaps fifty years" | fifty in west Jutland, a couple of centuries on the islands | §09 and §11 of the same page |
| 03 §04 | Barkær "dug in the 1930s" | 1931–49; the village reading is the late 1940s' | lex.dk |
| 03 §05 | about 1,800 twelfth-century churches | more than two thousand, after 1100 | chapter 12 |
| 03 §05 | Bronze Age burials "a thousand years" after, Viking "three thousand" | more than a thousand; four thousand | the myth-check says four |
| 03 §07, §10, Meanwhile | copper first appears "at the very end of the Funnel Beaker period"; imported "for eight hundred years"; Denmark "only just beginning to import" it in Ötzi's day | it came with the first farmers, c. 4,000 BCE; imports all but stopped c. 3,300–2,350 | Gebauer et al., PLOS ONE 2023; the Lønt crucible |
| 03 §10 | "heirs to five thousand years" of flint working | ten thousand | c. 12,100 to c. 2,000 BCE |
| 03 Meanwhile | the first Danish written word "more than four thousand years away" | some three and a half thousand | Vimose, c. 160 CE — chapter 6 |
| 03 §11 | Indo-European, "the ancestor of the language this page is *not* written in" | is written in | English is Indo-European |
| 03 Sources | Allentoft 2024 is "the backbone of sections 02, 07 and 11" | 02, 04, 08 and 11 | section numbers from an older order |

### 7.5 Part A — repetition and drag, fixed

Each cut removes something the reader has just read, and says so (D-16).

- **02 §10 said its violence paragraph twice** — the triple grave, Skateholm and the
  bone point, in two consecutive paragraphs. Merged into one.
- **02 §07 repeated §04 and §05**: the Værebro Å axe-haft, the daggers and the
  paddles, "none of this is necessary"; then §06's ochre, "heaviest around the
  head", and the colour of blood. The decoration paragraph is gone; the ochre keeps
  what is new (the clothing, and the religious reading).
- **03 §08 had the Yersinia sentence twice**, end of one paragraph and start of the
  next. Merged.
- **03 §12 gave the 2,500 surviving tombs twice** in adjacent paragraphs, and "the
  Vikings of chapter 10 sometimes buried their own dead in them" for the third time
  on the page (§05 and the myth-check also have it) — and the only D-1 prose break
  left in the book. Both gone.
- **03 §05 described the rollers, levers and ramps twice** in adjacent paragraphs.
  The first is trimmed to the scale.
- **01 §03**: the body restated the schoolteacher vignette's half-century wait and
  pre-empted the 21 May 2001 vignette's vertebra. Trimmed from the body; the
  shoulder blade moved into the vignette.
- **03 §07's "Instead they were given away"** followed a paragraph about axes
  being traded — a mines paragraph had been inserted between it and "never used".
  Now "Many of the finest were given away".
- **"chapter 01"** twice (02 §02, 03 §05), padded; now "chapter 1".
- **02's Recall asked about "the double grave at Bøgebakken"**; the page's double
  grave is Gøngehusvej. Now asks about Gøngehusvej, which also stops it duplicating
  the checkpoint.
- **Who-lines**: five had two fields where `vignettes.py` expects three. Separated.

### 7.6 Found, recorded, not changed

- **01 Figure 3 draws the Younger Dryas at c. 10,900 BCE**, a 150-year gap after
  Laacher See where the prose now says two hundred. It is an inline SVG with no
  generator, and its caption says the boundaries "carry real uncertainty".
  Hand-editing typed coordinates is what "compute, never type" forbids; if a figure
  script is ever written for Part A, draw it from Reinig 2021.
- **01 §04 names Trollesgave and the Bromme culture three sections before §07
  introduces them.** Order, not error.
- **03's *kulthus* is glossed in §05 and used only in §06's vignette.**
- **Recall questions that repeat the checkpoints** run through the whole book (3 of
  5 in 01, 5 of 5 in 07, none in 26–32): a pattern through A–F that stops in Part G,
  which reads like deliberate spaced repetition. Not a Part A fault. Chapter 07's 5 of 5 is for the Part B reading.
- **01's Dansgaard "at the Niels Bohr Institute"** is the institution's present name,
  not his. **01's "A 2025 study … 13,008 ± 8"** could not be opened to check.
  **Hammelev's "young woman"**: Trap Danmark says young, ZBSA "adult, presumably
  female". **01's Lascaux "about four thousand years old"** at Jels depends on which
  Lascaux date is used (three to five thousand).

### 7.7 D-15 and D-13 in Part A

**D-15: nothing to change.** Part A names no Schleswig and no Skåne town; its
places are Jutland, Zealand, Funen, Skåne as a region, Aarhus and the rest in the
forms D-15 prescribes. "Schleswig-Holstein" in 01 §08 is the modern German state.

**D-13: no case.** Every vignette in 01–03 sits in a section named for a process.
The nearest is **02 §06, *Vedbæk: people we can look at***, named for the place
its vignette is set: but the vignette is the finding of the cemetery in 1975 and
the body is the graves, so nothing is restated. Kept as it is.

### 7.8 Checked by a separate agent

An agent that had not seen the work checked every hunk of the Part A and Part I
diffs against sources and against the rest of the book. It confirmed the facts in
§7.4 and found eleven slips, ten in my own edits: the "shoulder blade" left in 01
§10 after §03 was changed; the Rome comparison (2,780 years against 2,400); 02's
glossary still saying "government-appointed"; "three professors"; an ambiguous
"the first person"; 03's new overlap clashing with its own glossary dates; "began
to make its own" when local copper-working existed before 3,300 BCE; "the twelfth
century" against chapter 12's "after 1100 … more than two thousand"; 43's "the
railway column" when the tonnages are also unsettled; 38's "last digits" for a
67-vote gap. All corrected. The eleventh is 01 Figure 3 (§7.6).

### 7.9 A decision for Carsten — R-1

**R-1. D-9 and L9a in the prehistoric chapters.** Part A has never been tagged.
D-9 says tag a part when it is next touched, and every chapter must carry an `[f]`
and an `[n]`. L9a says the who-line names a person or says on the page why it
cannot. In 01–03:

- **01 has no woman anywhere in its evidence** — not a single human bone survives
  from its four thousand years. Its two vignettes are the modern finders, both men.
- **03's three vignettes are Iversen, a building and a stone cist.** No woman.
- **Four who-lines name a thing**: Tybrind Vig 1, the Bøgebakken cemetery, the
  Tustrup kulthus, the Gjerrild cist. None says on the page why it cannot name a
  person, because in prehistory the reason is the period.

*Recommendation:* **tag Part A now, and record in CONVENTIONS that in a chapter
whose evidence names no one, the `[f]` requirement is met by the part, not by the
chapter, and a who-line may name the find.** Part A would then carry its `[f]` in
02 (Lola; the young mother at Bøgebakken is in the body, not a vignette). The
alternative is a new vignette in 01 and 03 built round a woman — in 01 it could
only be a modern archaeologist, which would be a vignette written for its tag.

**Answered 20 September 2026: as recommended.** Recorded under D-9 in
`CONVENTIONS.md` and built into `vignettes.py` (`NAMES_NO_ONE` = 01, 03; "[f]
part" only when the part really has an `[f]` — tested by removing Lola's tag, when
01, 02 and 03 all fail). Part A tagged:

| ch | vignette | tag | why |
|---|---|---|---|
| 01 | Jørn Fynbo, the schoolteacher | `[n]` | an amateur, and the find is his |
| 01 | Jørgen Holm, 21 May 2001 | `[-]` | a professional excavator |
| 02 | Tybrind Vig 1 | `[n]` | the boat's makers, anonymous hunter-fishers |
| 02 | Bøgebakken | `[n]` | the amateurs who stopped the bulldozer, and the dead |
| 02 | the Kitchen Midden Commission | `[-]` | three academics |
| 02 | Lola | `[f][n]` | a woman, and the agent of her own vignette |
| 03 | Iversen at Draved | `[-]` | a professional scientist |
| 03 | the Tustrup kulthus | `[-]` | a building; nobody in it is identified |
| 03 | the Gjerrild cist | `[n]` | five ordinary people |

Balance: 01 `[f]` part, `[n]` yes; 02 both; 03 `[f]` part, `[n]` yes.

## 8. Session 4 — Part B read (chapters 04–07)

*21 September 2026, from `START_HERE_review_4.md`. Cold run on a fresh clone of
`b528394`: every figure as expected — tidy clean, fixture and seams pass, debuild 45
identical, 336,704 page words, vignettes 114/84, figcheck 98/30/0, one OVER (17 §08),
draftnotes clean, appcheck 159, freshcheck 14, sweeps as listed.*

Every claim below was checked against a source before it was changed; three research
agents gathered the sources, and a fourth agent that had not seen the work checked every
hunk afterwards (§8.8).

### 8.1 Part B, read — errors of fact and of the book against itself, fixed

| ch | the page said | it is | ground |
|---|---|---|---|
| 04 §02 | amber: "Chapter 3 saw it carved into small animals" | chapters 2 and 3, carved and strung | 02 §07; 03 §07 |
| 04 Meanwhile | Nebra and Trundholm "four hundred kilometres" apart | about 515 | computed from the find spots |
| 04 §04 | the coffins' contents "survived for three and a half thousand years"; the yarrow "three and a half thousand years on" | some 3,300 (c. 1400–1300 BCE to 1871–1935); nearly 3,400 to now | D-8; the same page gives Trundholm "three thousand three hundred" |
| 04 §04 | Borum Eshøj "opened in 1875" | first dug into 1871 (the woman); the men 1875 | natmus; lex |
| 04 §05 | a wheel piece found "in 1996" by a detectorist, more "in 1998" | one campaign, November 1998, 21 pieces | natmus, *New parts for the sun chariot* |
| 04 §07 | "the Copenhagen school associated with Kristian Kristiansen" | Kristiansen has been at Gothenburg since 1994 | gu.se |
| 04 §07 | the isotope evidence "under dispute in section 09" | section 10 | the page |
| 04 §08 | the three-aisled house "appears in the later Bronze Age", dominant "for the next two thousand years" | early Bronze Age (period II — Bjerre, cited in the same paragraph, is period II); until the end of the Viking Age, some 2,500 | lex *langhus*; Bech & Mikkelsen |
| 04 §08 + glossary | "one end housed people, the other end cattle", of the type as a whole | stall traces in some Late Bronze Age houses, commonness uncertain | Trap, *Bronzealderens huse*; 05 §03 |
| 04 §10, Contested | the strontium exchange "has run for a decade" | since 13 March 2019 | *Science Advances* |
| 04 myth-check | the lur "about two thousand years older" than the longships | 1,500–2,000 | lex: lurs 1300–600 BCE, most after 1000 |
| 04 ← 2 | the Hjortspring boat "the first one we can actually examine" | the first plank-built one; 02's Tybrind Vig logboat is examined in a vignette | 02 |
| 05 §03 | Hodde held "perhaps a hundred and fifty to two hundred people" | two to three hundred | Danmarks Oldtid |
| 05 §03 + glossary | stall partitions "the first hard evidence that cattle were housed" | present in some Late Bronze Age houses; standard now | Trap |
| 05 §04 | the vignette's "three or four others" against the body's "probably four boats" | probably three others | the page |
| 05 §04 | "around fifty wooden shields; swords" | at least 64 shields (probably 80–100); eleven swords; some 170 spearheads, 138 of iron | danmarkshistorien (the page's own source) |
| 05 Meanwhile | at Hjortspring (c. 350) "Rome was fighting Carthage" | the first war with Carthage is 264; in 348 they renewed a treaty | |
| 05 Meanwhile | "Rome becomes an empire in the decades after this chapter closes" | 27 BCE, inside the chapter | |
| 05 §07 | Worsaae, 1842, "had studied bog finds in England" | his British journey was 1846–47; he argued from Danish Early Iron Age bog finds | DBL; Wikipedia |
| 05 §08 | the deposition rule "three thousand years old" by the cauldron's day | nearly four thousand | 03 §07's own "four thousand" |
| 05 §10 | the Hoby burial "within a few generations of the turn of the era" | within one or two | 06 §04: "within a generation" of Silius's command, 14–21 |
| 05 myth-check | Haraldskær "roughly fourteen centuries before Gunhild" | more than fourteen (1,454) | D-8 |
| 05 Contested | Tacitus "writing a century later", "a near-contemporary outside source", of the Tollund Man | some five centuries later | the page's own dates |
| 05 intro, Five | "the first Danes we can look at" | the first faces from Danish ground | 01's myth-check; §7.4's Hammelev precedent |
| 05 → 7, 10 | the Nydam boat's chapter | 6 (§08) | 06 |
| 06 §02 | "The overseas empire (27)" | chapter 30; Part G under D-1 | §8.6 |
| 06 §04 | the Hoby cups show "scenes from the *Iliad*" | Priam is the *Iliad*; Philoctetes is not — the Trojan War | |
| 06 §04 | isotopes "say he grew up on Lolland" | "most probably of local origin" | *Danish Journal of Archaeology* 2021 |
| 06 §04 | "He cannot have known what the pictures meant" | may never have (L8: hedge) | |
| 06 §06 | "Moesgaard Museum sent P.V. Glob" in 1950 | Forhistorisk Museum, Aarhus; Moesgaard from 1970 | lex, *P.V. Glob* |
| 06 §06 | the second campaign "ran for eleven years" (1975–85) | ran until 1985 | D-8 |
| 06 §06 | 15,000 objects from 40 per cent, so "thirty thousand or more are still down there" | 22,500 on the page's own ratio: more than twenty thousand | arithmetic |
| 06 §06 | "nearly two hundred swords", "over three hundred spear and lance heads", "124 combs", "fire-strikers, one per soldier" | c. 150 swords; at least 869 spears and lances; c. 300 shields; c. 140 combs; c. 130 fire-strikers — one man in eight | Moesgaard; danmarkshistorien |
| 06 §06 | Illerup's deposit shows "what they gambled with" | the gaming pieces are Vimose's, as the same paragraph says | the page |
| 06 §08 | a mast "for another three hundred years" after Nydam | four hundred | 07 §06: Nydam c. 310, the sail c. 700 |
| 06 §08 | Dybbøl "some fifteen kilometres from the bog" | about six | coordinates |
| 06 §08 | the boat "has been in Schleswig ever since" | Flensburg, then Kiel (Holstein) from 1877, Gottorf since the late 1940s: in Germany | de.wikipedia *Nydamboot*; lex |
| 06 §08, visit | Gottorf "a little over an hour" / "an hour" from the border | 35–40 km: under an hour | |
| 06 §08 | "another twenty-five chapters. 1864 (33)" | 28 chapters; 34; Part H under D-1 | §8.6 |
| 06 visit | Nydam and Thorsberg "both were Danish finds in 1863" | Thorsberg was dug 1858–61: Engelhardt dug both before 1864 | geschichte-s-h.de |
| 06 §09 | Illerup's "nine runic inscriptions"; WAGNIJO "once scratched, once in raised relief", "the same name appears at Vimose" | about ten; both stamped at manufacture; the Vimose one is a third lance head | Imer; Ilkjær |
| 06 fig. 2 | war west, wealth east "is, once again, the ice-margin line of chapter 1" | Illerup, Vimose and Nydam all lie east of the ice margin; the line is the Great Belt | 01 |
| 06 §12 | the armies "get, if anything, larger"; "The deposits do not get smaller. They get bigger." | Illerup A (205) is by far the largest (§06 says so); D is a dozen objects | Danmarks Oldtid |
| 06 Meanwhile | Denmark's population "would have fitted comfortably inside Teotihuacan" | Teotihuacan 100–200,000; later Iron Age Denmark a few hundred thousand, perhaps half a million — removed | Gyldendal/Politiken, *Befolkningen* |
| 06 ← 5 | Hjortspring "six centuries earlier" than Illerup | 554 years: more than five | D-8 |
| 07 §01 | "Lotte Hedeager's figure … over fifty kilograms — more than … the entire Bronze Age, … Viking Age … and … Middle Ages combined" | neither the attribution nor the comparison could be found; Jensen (Danmarks Oldtid, in Sources): nearly 50 kg, the largest group of gold finds from any single period | lex, *En nordisk Guldalder* |
| 07 §02 | Schytz: "It was the first time he had used it" | he "hadn't been out ten times" | tvSyd |
| 07 §02 | Vejlemuseerne excavated "in August 2021" | March and August 2021 | Vejlemuseerne |
| 07 §02, §10 | the reading: "thirty-four runes, eight words"; §10's "gold disc the size of a saucer with eight words on it" | about 34 runes, no clean word count; on IK 738, a 5 cm disc — not the 13.8 cm one | Imer & Vasshus, *NOWELE* 2023 |
| 07 §02, myth, Five | Odin named "in the early 400s"; "four hundred years before the Viking Age"; "eight hundred" before the Icelandic texts | the paper dates IK 738 to 450–490 (Axboe): the fifth century; three centuries and more; eight centuries | *NOWELE* 2023 |
| 07 §03 | "Ninety-five years later" (20 July 1639 → 21 April 1734) | 94 years 9 months: nearly ninety-five | D-8 |
| 07 §03 | the king "awarded him 200 rigsdaler" | the sources disagree whether Lassen or the count got the 200: "Lassen was rewarded" | en/no Wikipedia; natmus |
| 07 §03 | "the historian Ole Worm recorded … people were drinking out of it" | physician and antiquarian; his letter says he was handed it full of wine | Worm's letter |
| 07 §03 | Heidenreich a "convicted forger"; "five pounds of melted metal at his sister's house"; two earrings, "probably the last surviving gold", "in a museum on Funen" | convicted of coin counterfeiting (1788); the gold became counterfeit coins and jewellery; two *pairs*, presumed not proved, one at Ringe, one at the National Museum | lex, *Niels Heidenreich*; natmus |
| 07 §03 | Oehlenschläger's poem "within weeks" | written 1802, out at the year's end (*Digte*, dated 1803) | danmarkshistorien |
| 07 Meanwhile | at 750 "Christian kingdoms lie immediately south of Denmark, and Charlemagne's grandfather is in power" | the pagan Saxons lay between; Charles Martel died 741; Pepin was crowned 751 | |
| 07 §07 | Lejre's halls "the largest around fifty metres"; *Beowulf* "places Heorot" there | up to c. 61 m; the poem names no Lejre — the identification is scholars' | Lejre Museum |
| 07 §08 | Jordanes says the Dani were "of notable height", "quoted for the next fifteen centuries" | the clause is generally read as the Heruli's — removed | Mierow's translation |
| 07 §08, myth | *Danmark* "not attested until chapter 10, on a stone at Jelling and in a king's mouth in England"; "for another four hundred years" | first in the Old English Orosius (Ohthere, c. 890), then Gorm's stone; more than three centuries | *Etymology of Denmark* |
| 07 §10 | "Everything in the next thirty-three chapters" | thirty-eight | |
| 07 §10 | "the three permanent facts that chapter 1 identified: … a position on the water that everyone else has to pass through" | chapter 1's third is the far northern end of a continental system; the water is Part B's addition (06 §05) | 01 |
| 07 §10 | Jelling's monuments "three centuries after this page ends" | about two | |
| 07 §10 | Vindelev buried "around the year 500"; "between the hoard and the stones lie the two centuries this chapter has just described" | first half of the sixth century (§04 of the same page ties it to 536); four centuries lie between, two of them this chapter's | Vejlemuseerne |
| 07 §10 | "A rhombus of oak posts laid out around a grave" among this chapter's finds | the Jelling palisade, c. 968, chapter 10 — replaced by Sorte Muld's gold foils | |
| 07 §10 | the three dates "known to the year" | Ribe is 704–710 | lex |
| 07 visit | "Genforeningen's story (37)" | 38; Part I under D-1 | §8.6 |
| 07 Sources | Bede "three centuries after the events" | 449 → 731: nearly three | D-8 |
| 07 glossary | the sail "the single most consequential technical change in this series" | a series that reaches steam and the co-operative dairy: "of the period" | |

### 8.2 Part B — repetition and drag, fixed

Each cut removes something the reader has just read, and says so (D-16).

- **05 §04, the D-13 case (§8.4).** The body after the Hjortspring vignette restated its
  landing, loss, holing and sinking, and put the lake "three or four kilometres" inland
  where the vignette had said three. The body now carries the inventory and the count —
  "four boatloads, at twenty paddlers a boat" — and nothing the vignette has told.
- **06 §05 said its two Himlingøje arguments twice** in five paragraphs: the same
  workshops, and the redistribution "exactly as Rome had done", each stated and then
  restated under "Two details carry most of the weight"; "If that is right" twice. The
  first statements are gone.
- **06 §04's Hoby vignette listed §03's drinking service item for item.** It now points
  back to it.
- **06 §06 counted the combs, fire-strikers and horses in one paragraph and described
  them in the next.** Once each, with the counts where the description is.
- **06 §12 re-listed §06's four deposition dates.** Now "its four deposits".
- **04 Figure 3's caption gave the evidence the body gives next, and the vignette's
  two-face mechanics** ("A figure must not summarise prose the reader has just read").
  The caption is a label now.
- **07 §10 said "from here on there are documents, mostly by foreigners" twice** in the
  same section. Once.
- **07 §10's "kings who claim descent from gods"** — the Vindelev reading is belonging,
  not descent. "Rulers who claim a god's backing", as Five Things says.

### 8.3 Found, recorded, not changed

- **The "valuables in wet ground" thread** is in every Part B carry-back (04 ← 3, 05 ← 3, 4,
  07 ← 3, 4, 5) as well as 03 §07 and 03 → 4, 5, 6. It is threading, and each states
  what the chapter adds. Kept. This is most of what START_HERE meant by "04 repeats
  several of 03's lines"; the one that was wrong (the amber) is fixed.
- **04 §11 and its myth-check both say the Vikings buried their dead in the mounds** —
  two on the page, as 03 keeps for the tombs after session 3's trim. Kept.
- **04 §04's lead-in names "the contents of a birch-bark bucket and the flowers"** before
  the Egtved vignette does. Slight; kept.
- **Not verifiable online, kept:** *Tilia Alsie*'s Polish lime and "nearly fifty
  kilometres in five hours" (the 1999 launch is confirmed); Hjortspring "three kilometres
  inland"; Schytz and Antonsen "friends since childhood"; Imer's "hardest inscription in
  twenty years" (the Golden Horns comparison is confirmed); the long horn's "litre and a
  quarter"; "melted down within days".
- **Source ranges the page now sits inside:** Hjortspring's bone and antler spearheads,
  38 (danmarkshistorien) or 31 (lex, Wikipedia) — the page says "some 170, 138 of them
  iron". Illerup's swords, 100 (Danmarks Oldtid), c. 150 (Moesgaard), over 200
  (danmarkshistorien) — the page follows Moesgaard. Illerup's objects, 15,000+ or
  22,000+ (Trap).
- **02 §07's Engesvang amber as Ertebølle**, checked because popular sources say
  Maglemose: Trap and Danmarks Oldtid both say Ertebølle. Correct.
- **Parts C and D: thirteen who-lines in 08–14 have two fields** (`vignettes.py` lists
  them). For those parts' passes, with their D-9 backfill.

### 8.4 D-15 and D-13 in Part B

**D-15.** Part B names Schleswig four times: 06's "duchy of Schleswig" (right);
06's "in Schleswig ever since" (wrong in fact — the boat spent seventy years in Kiel —
now "in Germany"); 06's and 07's "Schloss Gottorf, Schleswig" and "Danevirke Museum,
Schleswig" (the German town, right). 07's Angeln "between Flensburg and the Schlei" is
right. Schleswig 170 → 169. Nothing else.

**D-13.** One case, decided. **05 §04, *Hjortspring: the oldest army***, is named for
its vignette's subject, and the body restated the vignette (§8.2). The vignette is the
boat's making and fate; the section is re-scoped so that the body is the army. The
others: **07 §02 *Vindelev*** and **07 §03 *The Golden Horns*** are named for their
vignettes' subjects but restate nothing — the bodies carry the inscription and the poem —
and are kept, as 02 §06 was. **06 §04 *Hoby*** is named for its subject; the body is the
Silius argument, kept (the vignette's repeat of §03's list is §8.2's). 04 §04, 04 §05,
05 §07, 06 §06 and 06 §08 are process-named or add without restating.

### 8.5 07's Recall — a fault, not the pattern

Measured (a Recall question counts as a checkpoint repeat at token overlap ≥ 0.4): 01
2/5, 02 2/5, 03 3/5, 04 3/5, 05 2/5, 06 3/5, **07 5/5**, 08 3/5, then 0–2 through the rest
of the book (15 is 4/6). §7.6's reading — spaced repetition through A–F — holds at two
or three of five; five of five is the outlier. Two questions replaced with ones on
material no checkpoint asks: the Golden Horns, and the sail. 07 is 3/5 now.

### 8.6 Check 7 could not see the parenthetical form

Parts A–D refer forward as "the Viking Age (8)". `sweep_arrows.py` check 7 read only
"chapter N", in the narrative only, so **twelve such references were invisible to it —
eleven to numbers the renumbering had made wrong**, all breaking D-1:

| ch | said | is |
|---|---|---|
| 06 §02 | the overseas empire (27) | 30 → Part G |
| 06 §08 | 1864 (33) | 34 → Part H |
| 07 visit | Genforeningen's story (37) | 38 → Part I |
| 08 §12 | Iceland's Act of Union (36), the realm of 1953 (42) | 38, 45 → Part I |
| 11 Contested | the slave trade (27) | 30 → Part G |
| 12 §10 | the agrarian reforms of the 1780s (28) | 29 → Part G |
| 13 myth-check | the Atlantic slave trade (27) | 30 → Part G |
| 14 §02 | the Atlantic slave trade (27) | 30 → Part G |
| 15 §02 | the sale of the West Indies (36) | 37 → Part I |
| 15 §04 | the Lutheran nobility (21), the agrarian reforms (28) | Part F; 29 → Part G |
| 17 §03 vignette | Hans Egede "— chapter 27 —" (found by §8.8) | Part G |

All re-pointed to part letters; 08–15 were read for these lines only, not for their
passes. **Check 7 now reads "(N)" and "(N–M)" everywhere a reader reads, apparatus
included**, and reported exactly these twelve on the shipped pages before the fix; 0
after. Same class as §4.1's Thread notes: a check that passes because it looks in fewer
places than the book writes.

### 8.7 R-1 in Part B — tagged

Seven of the nine who-lines had two fields, or a place where the person belongs; all now
person · place · date · tag.

| ch | vignette | tag | why |
|---|---|---|---|
| 04 | Peter Platz, Egtved | `[n]` | a farmer, and the find is his decision |
| 04 | Frederik Willumsen, Trundholm | `[n]` | a smallholder at the plough |
| 05 | Gustav Rosenberg, Hjortspring | `[-]` | a museum professional |
| 05 | the Haraldskær woman, and Worsaae | `[n]` | an ordinary woman is the subject — the point of the vignette — but not its agent, so not `[f]` |
| 06 | the Hoby man | `[-]` | an elite burial |
| 06 | Glob, Andersen, Ilkjær at Illerup | `[-]` | professional excavators |
| 06 | Conrad Engelhardt at Nydam | `[-]` | a professional |
| 07 | Schytz and Antonsen, Vindelev | `[n]` | a detectorist and a farmer |
| 07 | Svendsdatter, Lassen, Heidenreich | `[f][n]` | the girl who found the horn; a smallholder |

Balance: **04 `[f]` NO, `[n]` yes; 05 `[f]` NO, `[n]` yes; 06 `[f]` NO, `[n]` NO;
07 both.** `vignettes.py` reports D-9 FAILURES 04, 05, 06 — true, and not to be made to
pass by tagging. §8.9 puts it to Carsten.

### 8.8 Checked by a separate agent

An agent that had not seen the work checked every hunk against sources and against the
rest of the book. It confirmed the facts in §8.1 and §8.6 and found twelve slips — eight in
my own edits, as in session 3. All corrected:

- **04 §05: the 1996 find was real.** I had dropped it on the National Museum's page,
  which mentions only 1998; Trap Danmark has both (a detectorist's wheel piece in 1996,
  then Odsherreds Museum and the National Museum's detector survey in 1998). Restored.
- **04 §05: Willumsen was not a smallholder** (the old text's word, which I had copied
  into the who-line) but the overseer of the state's drained bog, employed since 1897; land
  of his own came in 1922. Body and who-line corrected; `[n]` stands.
- **04 §04: "nearly three and a half thousand years on"** — 3,395 years; D-8 wants the
  completed count: "some three thousand four hundred".
- **05 §04: "probably three others"** — the source says *at least* four boats. "At least
  three others"; "at least four boatloads".
- **06 §06: "Some three hundred shields, belts, scabbards …"** read as three hundred of
  each; and "the battle behind it" had lost its antecedent when "the deposit" became
  plural. Both mended. A four-dash sentence in the vignette untangled.
- **07 §02: "a disc about five centimetres across"** — the research gave 5.2 cm for IK 738,
  Wikipedia gives 11.8; I could not settle it and the size is gone. §10's "a smaller one
  that names Odin" is true on either figure.
- **07 §02: "by about a century and a half"** went with the press release's early-400s
  dating that I had dropped; on the paper's 450–490, about a century.
- **07 Five things still said "a first-time detectorist"** after §02 was corrected.
- **07 Meanwhile: "only by the pagan Saxons"** — the Obodrites and free Frisia also lay
  between. "Chiefly".
- **Check 7 still missed "chapter N" outside the narrative.** `c17` §03's vignette sends
  Hans Egede "— chapter 27 —" from Part E: a D-1 break. Check 7 now reads both forms, and
  "(N, M)", "(N and M)", "chapters N to M" and a number after a closing quotation mark,
  in every section a reader reads. It reports exactly that one on the old pages; 17 now
  says Part G.
- **Two glossary pointers were wrong by the renumbering** — a class no check can test,
  because check 7 asks only whether a target exists and obeys D-1: **34's *Dannevirke*
  "begun in the eighth century (chapter 5)"** — 7; **41's *hjemmetysker* "became Danish
  in 1920 (chapter 40)"** — 38. Fixed in the drafts and rebuilt through `mkbody.py`.

**Found by following that up, not changed** (for those parts' passes): a heuristic —
does the glossed term appear on the chapter its entry points to? — lists a dozen, most of
them inflection. Three are real: **24's *Hammershus* "from chapter 14"** (the name is on
no page but 24), **20's *krongods* "run through this series since chapter 14"** (the
phrase is on 12 and 16, not 14), and **19's *orlogsflåde*** pointing at 22 (to read).

### 8.9 Decisions for Carsten — Part B, one at a time

**R-2. 04 and 05: does R-1 extend to them?** Neither chapter's evidence names an
individual. 04's women — the Egtved girl, the Skrydstrup woman, Borum Eshøj's — are known
and unnamed; 05's names are Roman ones for peoples whose origin is itself in doubt. Women
are present in both as subjects, never as agents, because Part B's vignettes are the
modern finders'. *Recommendation:* **add 04 and 05 to `NAMES_NO_ONE`, with Part B's `[f]`
in 07** — the same ground as 01 and 03. The alternative is a modern woman: 04 has one
ready in Karin Frei, who led the 2015 study, but §10 already tells her study, so the
vignette would restate the body (D-13) — a vignette written for its tag.

**Answered 21 September 2026: as recommended.** `NAMES_NO_ONE` now holds 01, 03, 04 and
05; `vignettes.py` reports 04 and 05 as "[f] part", and 06 alone as a D-9 failure.

**R-3. 06 is outside R-1 and fails both flags.** Its evidence names people — Silius,
*harja*, WAGNIJO, *Nithijo* — all men, and its three vignettes are an elite burial and two
excavations. *Recommendation:* **two new vignettes, drafted in a later session:** the
**Juellinge woman** (Lolland, c. 200 CE), buried holding the ladle and strainer of the
Roman wine service §03 describes — `[f]`, the particular inside a process-named section;
and an **ordinary Vorbasse household** in §10, *The farm that moved* — `[n]`. About 600
words; 06 stays near 34 minutes. The alternative is to record 06 as a known D-9 failure
until then.

**Answered 21 September 2026: as recommended.** Two vignettes for 06 — the Juellinge woman
in §03 (`[f]`) and an ordinary Vorbasse household in §10 (`[n]`) — to be drafted, sourced
and checked in review session 5. Until then `vignettes.py` reports 06 as its one D-9
failure, and that is correct.

## 9. Session 5 — 06's two vignettes, and Part C read (chapters 08–11)

*21 September 2026, from `START_HERE_review_5.md`.*

**The first cold run failed, and the failure was the ledger's, not the book's.** On a fresh
clone of `2baf157`: debuild 32 identical, 13 BODY DRIFT (04, 05, 06, 07, 08, 11, 12, 13,
14, 15, 17, 34, 41); 336,704 page words, Part C 25,532; Schleswig 170; check 7, 13 prose
references. The thirteen are exactly the chapters that commit's source patch touched: it
had been pushed without its rebuilt pages. A rebuild in a throwaway copy reproduced every
figure START_HERE expected, so the cause was that and nothing else. Carsten built and pushed
(`43b98f8`); a second fresh clone matched every line — tidy clean, fixture and seams pass,
debuild 45, 336,720, vignettes 119/88 with 06 the one D-9 failure, figcheck 98/30/0, one
OVER (17 §08), draftnotes clean, appcheck 159, freshcheck 14, sweeps as listed.

Three research agents gathered sources; a fourth, which had not seen the work, checked every
hunk afterwards (§9.8).

### 9.1 R-3 carried out — and two of its premises were wrong

R-3 described the Juellinge woman as "c. 200 CE", "buried holding the ladle and strainer",
"excavated 1909". The sources say otherwise, and the vignette follows the sources:

| R-3 said | the sources say | ground |
|---|---|---|
| c. 200 CE | just after the birth of Christ; the same period as Hoby, early first century | natmus, *The woman from Juellinge*; Jensen, *Danmarks Oldtid*, "En lollandsk storhøvding"; Trap. Jensen's "Kostbarheder fra Syden" says the second century; McGovern's press release "200 BC" is a slip |
| holding the ladle and strainer | the strainer in her right hand; the ladle lay in the cauldron | Jensen: "I kedlen lå en langskaftet øse af bronze. Den tilhørende bronzesi havde man derimod givet den døde i hånden"; McGovern et al. 2013 |
| excavated 1909 | found 1908, by railway workers building the sugar-beet line; four graves, three women and a girl | natmus, *The discovery of the women from Juellinge* |

Neither changes what the vignette is for. The residue matters more than either: Bille Gram's
microscopy for Müller's 1911 publication found a fermented drink of barley, lingonberry,
cranberry and bog myrtle, and McGovern's 2013 chemistry probably grape wine as well — a Roman
strainer and a northern drink, which is §03's "the wine service matters more than the wine"
made particular without restating it.

**(a) The Juellinge woman, 06 §03 *What came north*, `[f]`.** After the paragraph on the wine
service; the service is not re-listed. Every detail is from Jensen, the National Museum's four
pages on her, and McGovern. The reading that she served drink is the museum's ("She had perhaps
used these utensils to serve drinks for her fine guests"), and the vignette hedges it as such
(L8).

**(b) An ordinary Vorbasse household, 06 §10 *The farm that moved*, `[n]`.** No numbered
Roman Iron Age farm is online: Hvass's farm-by-farm plans are in *Acta Archaeologica* 49
(1978), which is not. What is online, in two sources that agree, is one farm: of the fourth
century's twenty, **two farms of average size had a smithy**, with the smelting furnaces just
outside the fence and "sporene efter smedens færdsel mellem ovn og værksted" (Hedeager,
*Gyldendal og Politikens Danmarkshistorie*; Jensen, *Danmarks Oldtid*). The vignette is one of
them. Nobody on it has a name, and the vignette says so (L9a).

**D-13.** §10's fourth paragraph was the list the vignette now shows — "a fenced farmstead with a
longhouse of perhaps thirty metres, a byre for twenty or more cattle …" — so the section is
re-scoped: the list goes, the body leads into the vignette ("Here the ordinary unit is
legible") and after it says only what the vignette does not: iron was made here from the
first century. Three errors in §10 went with it: iron smelting "in the later phases" (four
furnaces stood outside the first-century fences — Hvass 1983); "silverwork on the premises"
(no source; none found); "a well" (attested for the eighth century, not the Roman). §10's
"gulf" between farms is now measured: the largest fourth-century farm, a 45-metre house on
almost 4,000 m², about twice the average.

`vignettes.py`: **no D-9 failure in Parts A–B.** 06 is 35 minutes.

### 9.2 Part C, read — errors of fact and of the book against itself, fixed

| ch | the page said | it is | ground |
|---|---|---|---|
| 08 §04 | offerings in "chapters 3 to\n07"; "Gudme, in chapter\n07" | 3 to 7; Gudme is 06 §11 | the pages; §9.6 |
| 08 §04 | Adam of Bremen "wrote a century later" | in the 1070s — two centuries after this chapter | |
| 08 §04 | Odin named on gold "around the year 400" | the fifth century (07 since session 4) | 07 §02 |
| 08 §04 | hammer amulets "by a wide margin the commonest religious object" in Denmark | no count supports a ranking; they are found across the Viking world, most densely in Denmark and southern Sweden | medieval.eu, *Thor's hammer* |
| 08 §05 | "The Frankish chronicler … called Godfred the mad king" | no source calls him mad: Einhard, *Vita Karoli* 14, "adeo vana spe inflatus"; RFA 810 "inflatus" | Einhard |
| 08 §07 | Repton: "around two hundred and fifty people"; the army "had lost a quarter of itself"; the men "still away three winters later" | at least 264; the quarter assumes an army of about a thousand, which §07 itself doubts; the army had been in England since 865 | Jarman et al., *Antiquity* 2018 |
| 08 fig. 3 | Godfred fortifies "three years after" Saxony | 804 → 808: four | the figure's own dates |
| 08 §09 | Charles the Fat "deposed within two years" of 886 | November 887: the next year | |
| 08 §09 | William crossed "six days after" Stamford Bridge | 25 → 28 September: three | 11 §09 |
| 08 Meanwhile | Faroes and Iceland "the first permanent human occupation of either" | the Faroes have earlier traces; Iceland's first permanent population | Church et al. 2013 |
| 08 Sources | the RFA "for everything in section 04" | section 05 | the page |
| 09 intro | three towns "at once" | 704, c. 800, the tenth century: within two centuries | the page |
| 09 §02 | Ribe "with a rampart around it by the ninth century" | a low ditch in the ninth; a rampart in the tenth | Trap, *Ribes historie* |
| 09 §03 | "under fifteen kilometres" to the Treene (also fig. 1, Five things) | about 16 km to Hollingstedt | haithabu-danewerk.de |
| 09 §03 | 340,000 objects "from an area of twenty-four hectares" | from about five per cent of it | lex *Hedeby*; de.wikipedia |
| 09 §04 | Aarhus "appears in the tenth century … fortified from early on"; three towns "all royal" | a settlement from c. 750–800, a town and rampart in the first half of the tenth; "probably all royal" — the page's own Contested question doubts Ribe | Trap, *Aarhus' historie*; Linaa, DJA 2024 |
| 09 §05 | Ibn Fadlan's "bead necklaces, one bead bought for each ten thousand dirhams" | neck-rings, one for each 10,000 | Ibn Fadlan |
| 09 §07 | Vorbasse "west Jutland"; "by the tenth century … seven or eight farmsteads … workshops for iron and precious metal … bigger" | central Jutland (06); seven farms from the 720s (dendro); a smithy, no precious metal; fewer farms than the fourth century | Hvass 1983; Jensen; Sawyer, *Vorbasse 700–1050* |
| 09 §07 | "the bog-iron industry of chapter 5 has gone industrial … thousands of furnace pits" | the great sites belong to 200–700; in the Viking Age imports largely replace home production | Grænseforeningen, *Jernudvinding*; Snorup |
| 09 §09 | Ottar "described paying tribute in furs, feathers, whalebone and ship-rope" | the Sami paid it to him | the Old English Orosius |
| 09 §09, Meanwhile | al-Tartushi "from Córdoba" | from Tortosa; Córdoba was the caliph's capital | |
| 09 §10 | "from the tenth century … one princely burial … the dead man and two companions … some twenty metres" | three men; a ship of at least 16 m (the east end is gone); end of the ninth or start of the tenth century | de.wikipedia *Bootkammergrab* |
| 09 Meanwhile | Hedeby "perhaps one to fifteen hundred" | a thousand to fifteen hundred | |
| 09 §12 | Hardrada "according to the sagas, sent fire-ships"; charred boats in the Schlei | Heimskringla says he took the town and burned it; the burnt Hedeby 1 wreck was built c. 985 and belongs to an attack c. 1000 — removed (and see §9.3 on 11) | Heimskringla, *Haralds saga* 34 |
| 09 myth | Ribe "roughly eighty years before Lindisfarne"; Hedeby "struck the first Scandinavian coins" | 704 → 793: nearly ninety (D-8); §03 itself says the claim is contested | |
| 10 §01 | "the present queen" | king, since January 2024 | |
| 10 §02 | the palisade "in 2007 and after", "unknown until 2007"; "dated in 2013" | found 2006; the date is the dendrochronology's, not a year of publication | lex *Harald Blåtands palisade* |
| 10 §03 | the large stone "text on one face and pictures on the other two"; "section 09 comes back to why" | the text runs onto both picture faces; section 10 | the stone; the page |
| 10 §04 | "Poppo's glove": "An iron glove was heated … Poppo put his hand into it" | Widukind: he carried a heated iron; the glove is later, on the Tamdrup plates | Widukind III.65 (danmarkshistorien); Gyldendal, *Poppo og gudsdommen* |
| 10 §06, §11, Five, ← 9 | "Ramparts thrown around Hedeby, Ribe and Aarhus" around 980, "all of it within a few seasons"; "Harald then walled all three" | Hedeby's is mid-tenth century (09 §03 says so), Aarhus's first half of the century, Ribe's tenth; none dated as closely as the fortresses | lex; Trap; Haithabu museum |
| 10 §08 | Aggersborg's village "cleared to make room" | built on top of an older, abandoned settlement | lex *Aggersborg* |
| 10 §08 | grave 4: "Foreign jewellery", "a bronze bowl", "Two toes from a bird" | silver toe rings; two bronze bowls, possibly Central Asian; owl pellets and small bird and mammal bones | natmus, *A seeress from Fyrkat* |
| 10 §09 | Sweyn's campaigns "begin within a decade" of 980–81 | the 990s | |
| 10 §09 | the reason "is on the next page but one" | two sections on, in the same page | |
| 10 §12, Meanwhile | the stone's inscription "reproduced on Danish passports"; movable type "within decades of Jelling" | the Christ image; Bi Sheng, 1040s: within a century | |
| 10 Sources | "Holst, Jessen, Andersen & Pedersen 2014" | Jessen, Holst, Lindblom, Bonde & Pedersen, NAR 47 (2014) | |
| 11 header | "For nineteen years a Dane governed England, Denmark and Norway" | England nineteen; all three seven (the page's own figure 1) | |
| 11 intro | "Two of the three claimants … of Norse descent" | four claimants (§09), and Harold's mother was Ulf's sister: both invaders | |
| 11 §04 | "a decade of ferocious instability" after 1014 | three years | |
| 11 §03 | Skuldelev 2 from "a Danish-ruled shipyard in Ireland"; sunk "thirty years later" | Norse Dublin; 1042 → c. 1070: nearly thirty | |
| 11 §06 | Cnut "paid compensation to the church and to his own sister" | Heimskringla: land to the church; Estrid's share is only in modern literature | Heimskringla |
| 11 §08, §09 fig. 3 | "step-nephew"; "the two who actually fought at Stamford Bridge and Hastings" | nephew by marriage; the two with no blood link met at Stamford Bridge | |
| 11 §09 | Harold marched "four hundred kilometres in under a week" | London to Yorkshire, about 300 km in four or five days | |
| 11 §09, myth, Five | fleets "launched … as late as 1085", "kept sailing until 1085"; the last planned invasion "twenty years after Hastings" | 1069, 1070, 1075; Cnut IV's 1085 fleet never sailed; 1066 → 1085: eighteen (D-8) | ASC 1075 |
| 11 §10 | "a hereditary Christian monarchy" | §03 of the same page: elected, "not straightforwardly hereditary" — "held within one dynasty" | |
| 11 §10 | Sweyn Estridsen "will reign for nearly thirty years" from 1066 | until 1074 (12's date) | 12 |
| 11 vignette | titled *Tóki, who went west*; Tóki is nowhere in it; "Around a tenth of Danish stones were raised by women"; "the century this chapter covers"; "Nobody higher up wrote a word about them" | *Skarthi, who went west*; the share is unverified — "some"; the decades either side of 1000; Skarthi's stone was raised by a king — "no chronicler" | Imer, DJA; DR 1, 3, 55 |
| 11 visit | "Forty Danish monarchs" at Roskilde | forty kings and queens | roskildedomkirke.dk |

### 9.3 Part C — repetition and drag, fixed

- **09 §02 re-argued 07 §09's Ribe** — "laid out … not a settlement that grew; it is a
  decision" is 07's paragraph, a chapter later. 09 now opens by pointing back to it and goes
  straight to what filled the plots; the checkpoint and Recall question on "laid out rather
  than grown" are replaced (the checkpoint in `build_parts_abc.py`, which is where it lives —
  §9.6).
- **08 §12 and 09 §11 both told Ansgar's churches** (with different dates, c. 850 and c. 848)
  and both said he converted almost nobody. 08 now leaves the churches to 9.
- **08 §12 re-deferred Ribe "properly to the trading towns (9)"**, as 07 had. Once.
- **08's Meanwhile said Verdun and the weak successors, and §09 said them again at once.** The
  box keeps the coronation.
- **10 §05 restated 08 §04's close almost word for word** ("hierarchical by construction",
  "abolished at a stroke"). 08 set it up for Jelling; 10 now says so and states it once.
- **09 §12 and 11 §08 both told the burning of Hedeby with the fire-ships.** The fire-ships were
  wrong (§9.2); the burning is 11's, and 09 points there.
- **11 §01 and §02 both said Sweyn was first to put his name on a coin.** Once.
- **11 §07 had "Three Scottish kings submitted to him in 1031" stranded** between the
  succession and Cnut's sons. Moved to §05, where his reach is.
- **11 §07 and §10 both gave Sweyn Estridsen "nearly thirty years".** §10 now says until 1074.

**Found, kept.** 07 → 8, 9 promises Kanhave; neither chapter tells it beyond 08's carry-back —
the arrow's claim is that the three works are infrastructure, and 08 ← 7 says so. 11 §10 lists
the Danelaw's names and ridings after 08 §08 did, and says "Chapter 8 listed some" — kept.

### 9.4 Found, recorded, not changed

- **Not verifiable online, kept:** Ravning Enge's "about five tonnes"; Hedeby's 340,000 objects
  (lex gives it; nothing else found); 06's Vorbasse gates, which Jensen describes for the third
  century, applied to the fourth-century farm.
- **12's and 14's who-lines** had two fields (§8.3); now three. **14's vignette places
  Jyske Lov's reading at "the Viborg assembly"**, and says "a hundred and sixty chapters" — the
  law was given at Vordingborg in March 1241, and its chapter count wants checking. For Part D.
- **The build's "padded chapter" guard exists only in `build_parts_abc.py`** (§9.6); parts D–I
  have no such check. A scan of every body found one more case, 13's "chapters\n07 and 10"
  (fixed), and none after 13.

### 9.5 D-15, D-13 and Recall in Part C

**D-15.** Part C names Schleswig four times, all the German town (08 visit, 09 §12 twice, 09
visit). Danevirke, Hedeby, Aarhus throughout. Viking-age kings under their English names.
Nothing to change. Schleswig stays 169.

**D-13.** No case. **08 §01** *The customs officer at Portland* and **10 §04** *Poppo's iron*
are named for their vignettes' subjects and restate nothing — the bodies go on to Lindisfarne
and to Widukind's reliability — and are kept, as 07 §02 was. The rest are process-named.

**Recall.** Measured as §8.5 did (a Recall question is a checkpoint repeat at Jaccard overlap of
content words ≥ 0.4 — which reproduces §8.5's figures for seven of its nine chapters): **08 2/5,
09 2/5, 10 1/5, 11 1/5**. Within the book's norm; 09's Ribe question replaced for §9.3's reason,
not this one.

### 9.6 The padded-chapter guard could not see a line break

`build_parts_abc.py` refuses "chapter 07" — but with a space, so 08's "chapter\n07" and
"chapters 3 to\n07", where the line wrap falls inside the phrase, passed it for as long as it
existed. The guard now reads `\s+` and the "N to/and/or 0M" form. **Tested:** it reports
`padded: 2` on 08 as shipped and nothing on any body now. The checker notes it still misses a
list form ("chapters 7, 8 and 09"); none exists.

The same reading found that **`build_parts_abc.py` strips every body's checkpoints and
re-inserts them from its config.** A checkpoint edited in a body alone is overwritten by the next
build. 09's changed checkpoint and 10's renamed §04 are in both.

### 9.7 D-9 in Part C — tagged

Eleven who-lines in 08–11 had two fields (§8.3 counted thirteen in 08–14; two of them are 12's
and 14's). All now person · place · date · tag.

| ch | vignette | tag | why |
|---|---|---|---|
| 08 | Beaduheard at Portland | `[-]` | a royal official |
| 08 | Godfred, 808 | `[-]` | a king |
| 08 | the Repton dead | `[n]` | the army's rank and file, unnamed |
| 09 | Ibn Fadlan | `[-]` | an envoy |
| 09 | Ottar | `[-]` | a wealthy man, by his own account |
| 09 | al-Tartushi | `[-]` | a merchant-diplomat |
| 09 | Frideborg and Catla | `[f][n]` | a widow disposing of her own property, her daughter carrying it out; the page itself calls her "an ordinary northerner … not a king" |
| 10 | Widukind on Poppo | `[-]` | a chronicler, a priest, a king |
| 10 | the woman in grave 4, Fyrkat | `[f]` | a religious specialist; a woman of standing, so not `[n]` |
| 11 | St Brice's Day | `[-]` | the king's order |
| 11 | Skuldelev 2 | `[-]` | a ship; builders and crews unnamed |
| 11 | Emma | `[f]` | |
| 11 | Skarthi, Erik and Tófa | `[f][n]` | Tófa raised her stone; a king's retainer and a shipmaster are the vignette's subject. The weakest `[n]` in the part: Skarthi's stone is a king's |

Balance: **08 `[f]` NO; 10 `[n]` NO.** 09 and 11 both. `vignettes.py` reports D-9 FAILURES 08,
10 — true, and not to be made to pass by tagging. §9.9 puts them to Carsten.

### 9.8 Checked by a separate agent

An agent that had not seen the work checked every hunk against sources and the rest of the book.
It confirmed the facts in §9.1 and §9.2 and found nine slips, seven in my own edits. All
corrected:

- **08: the Repton vignette's heading still said "two hundred and fifty"** after the body said
  260.
- **11: "he will reign another ten years"** — 12 gives Sweyn Estridsen 1074. "Until 1074".
- **11: "nineteen years after Hastings"** — October 1066 to 1085 is eighteen completed years
  (D-8), and I had written the interval I was correcting.
- **10 §11: "with town walls besides"** undercut §06's new hedge. "On top of the town ramparts of
  the same decades".
- **08: "the Faroes in the first half of the century"** — the box names no century. "The ninth,
  by the traditional dating".
- **10: "a bronze cup"** — the museum says two bronze bowls.
- **06: Juellinge and Hoby told the same find story a paragraph apart** — workmen, then the
  National Museum. Juellinge's is a clause now. And the Vorbasse vignette opened by repeating
  "about twenty farms" from the sentence above it.
- Three lost antecedents: Einhard's "him"; "Hollingstedt, which flows"; Aarhus's "its first half".

The two D-9 failures it listed are §9.7's. It could not find the National Museum's "hostess"
reading on the English pages; it is on *The hospitable housewife from Juellinge* ("She had
perhaps used these utensils to serve drinks for her fine guests"), checked.

**The three glossary pointers (§8.8), for their parts but done now.** **24's *Hammershus* "from
chapter 14"**: the name is on no page but 24. The entry now says who built it and when (the
archbishops of Lund, probably the 1290s — lex), and the ← 14 arrow points at the struggle
between church and crown that 14 does tell. **20's *krongods* "run through this series since
chapter 14"**: the thing runs from 12's *kongelev*, the word first appears in 16; the entry says
both. **19's *orlogsflåde*** pointed at "the navy of chapters 22 and 24": the navy is in 21
(thirty warships at Bremerholm), 22 and 23; 24 has only the Dutch fleet. "21 to 23".

### 9.9 Decisions for Carsten — Part C, one at a time

**R-4. 08 has no woman as agent.** Its evidence is Frankish and English annals and an army's
bones; 08 is not a chapter whose evidence names no one, so R-1 does not reach it. *Recommendation:*
**a vignette for 08 §04 *What they believed*: Ragnhild at Glavendrup** — on north Funen, in the
first half of the tenth century, a woman raised the longest runic inscription in Denmark, 210
runes, inside a sixty-metre ship setting, for Alle, *goði* of the sanctuary and thegn of the
king's retinue; she called on Thor to hallow the runes and cursed whoever moved the stone (lex,
*Glavendrupstenen*). It is the particular inside a section about cult led by chieftains, it is
Danish, and she is the agent. It sits a generation after 08's span, as §04's Adam and Snorri
already do. About 250 words.

**Answered 21 September 2026: as recommended.** Ragnhild at Glavendrup in 08 §04, `[f]`, to be
sourced, drafted and checked in review session 6.

**R-5. 10 has no non-elite subject.** Its vignettes are a chronicler's miracle and a seeress
buried as a woman of standing. *Recommendation:* **a vignette for 10 §08 *Who lived in them*:
the garrison's dead at Trelleborg** — a cemetery of young men, a few women and children, with
mass graves of five and eleven; strontium isotopes put much of it abroad, in Norway and the
Slav lands (Price, Frei et al., *Antiquity* 85, 2011). `[n]`: the rank and file of the ring
fortresses, which §09's reading of them turns on. To be sourced detail by detail before
drafting, as R-3 was. About 300 words.

**Answered 21 September 2026: as recommended.** The Trelleborg garrison's dead in 10 §08, `[n]`,
to be sourced, drafted and checked in review session 6. Until then `vignettes.py` reports 08 and 10
as D-9 failures, and that is correct.


---

## 10. Session 6 — 08's and 10's missing tags, and Part D read (chapters 12–15)

*22 September 2026, from `START_HERE_review_6.md`.*

**The cold run matched every line.** A fresh clone of `a14a5e1`; the commit before it, `d56a15b`,
carries item 143's rebuilt pages (06, 08–14, 19, 20, 24). git status clean; tidy reports and deletes
nothing, 45 bodies; fixture and seams pass; debuild 45 identical; 45 of 45, 337,491 page words,
26.8 h, parts A 21,397 · B 26,326 · C 25,619 · D 30,990 · I 74,403; vignettes 134/102, D-9 failures
08 and 10, selftest passes; figcheck 98/30/0; one OVER, 17 §08; draftnotes clean in 45 pages and 14
drafts; appcheck 159; freshcheck 14; sweeps: 2 pointers, 0 insolvent, 0 same-page glosses;
Schleswig 169 in 26 against Slesvig 104 in 11; sweep_facts 5 count rows; arrows 254 and 37 thread
notes, form 7, direction 0, D-1 0, titles 0, solvency 40, prose references 0, footers 0, `<h1>` 0,
9b 0.

Two research agents sourced the vignettes, two fact-checked about fifty of Part D's claims, and a
fifth, which had not seen the work, checked every hunk afterwards (§10.8).

### 10.1 R-4 and R-5 carried out — and two of R-5's premises were wrong

Item 143's lesson, applied: the recommendations' facts were checked before the vignettes were
written.

| the recommendation said | the sources say | ground |
|---|---|---|
| R-4: the longest runic inscription in Denmark, 210 runes | right — the longest on a Danish runestone; 210 counted (with one uncertain rune) | lex *Glavendrupstenen*; DR 209 (runer.ku.dk) |
| R-4: a sixty-metre ship setting | 45 m (Trap, *Skåltegn … Glavendrup-stenen*), 55–60 m (Trap; natmus), 60 m (lex; *Danmarks Oldtid*), 70 m between the prows as reconstructed (Trap). The page says "about sixty metres by most measurements" | as listed |
| R-4: Alle the *goði*, thegn of the king's retinue | *goði vía*, "priest of the sanctuary", and *liðs þegn*, "thegn of the retinue" — no king named. "Salhaugar" is a different stone, Snoldelev | DR 209; Trap *Glavendrupstenen* |
| R-4: first half of the tenth century | right: DR 900–950 | DR |
| R-5: mass graves "of five and eleven" | **three** mass graves: eleven, five and five | Price et al., *Antiquity* 85 (2011) 476–89 |
| R-5: "a cemetery of young men, a few women and children" | right, with a hedge the recommendation lacked: some of the 157 may belong to the settlement before the fortress | Price et al.; *Danmarks Oldtid*, *Ringborgene* |
| R-5: strontium puts much of it "in Norway and the Slav lands" | 32 of 48 non-local; the four highest values fit Norway or central Sweden; the rest could come from several regions. The authors' own hedge ("perhaps from Norway or the Slavic regions"), and the later dispute over limed Danish farmland, go on the page | Price et al.; Frei & Price 2012; Thomsen & Andreasen 2019; Price, DJA 2021 |

**(a) Ragnhild at Glavendrup, 08 §04 *What they believed*, `[f]`.** After the place-name paragraph
("they are addresses"), so that Alli's *vi* follows Odense's. It shows the section's argument — cult
and lordship held by one man — in one inscription, and adds the Thor formula and the curse. The
Tryggevælde stone is given with the runologists' hedge. It sits a generation after 08's span, and
says so. About 300 words.

**(b) The dead outside Trelleborg's east gate, 10 §08 *Who lived in them*, `[n]`.** Between the
Fyrkat paragraph and "So these were garrisoned places". **Not D-13**: §08 is named for its question,
not the vignette's subject — but the vignette qualified the body, so the body moved with it. Its first
sentence said the graves "do not support" a picture of barracks; Trelleborg's graves partly do, and
it now says "support it only in part". "Garrisoned the way a lord's household is" keeps its point and
adds "and, at Trelleborg, with outsiders". §09's "section 08 found households rather than barracks"
still holds. The lime dispute points back to chapter 4, which tells it. About 330 words.

**Found beside it:** grave 4 at Fyrkat was "buried in the 970s or 980s" in the cemetery of a fortress
felled in 980–81, "within a decade" of a stone that lex dates only to after c. 965. Now "around 980,
in the first years of a fortress". The vignette also opened "One burial in that cemetery", which after
the new vignette pointed at Trelleborg; now "in the Fyrkat cemetery".

`vignettes.py`: **no D-9 failure in Parts A–C.**

### 10.2 Part D, read — errors of fact and of the book against itself, fixed

| ch | the page said | it is | ground |
|---|---|---|---|
| 12 intro, §05, Five | Knud a saint "fifteen years later" | 10 July 1086 → 19 April 1101 is fourteen (D-8): "by 1101", "less than fifteen years after" | |
| 12 §02 | Svend "failed. His son's son succeeded" | his son, Erik Ejegod (§06 of the same page) | |
| 12 §02, fig. 2, ← 9 | Slesvig; Århus | Schleswig; Aarhus (D-15) | |
| 12 §03 | "around twenty sons, none of them born of a marriage the church would recognise" | at least eighteen children, one by his wife Gunhild | lex *Svend Estridsen* |
| 12 §04, Sources | the 1085 gift charter "survives and is the oldest original document preserved in Scandinavia … the period's own handwriting" | original and seal lost; the text survives in a copy, the oldest coherent text of Danish origin | danmarkshistorien, *Knud den Helliges gavebrev* |
| 12 §04 | Knud "thirty-three or so" in 1086 | born c. 1042: about forty-four | lex *Knud den Hellige* |
| 12 §06 | Hamburg-Bremen "nearly three hundred years" | 831 → 1104: more than two and a half centuries | |
| 12 §06, §07 | "Erik agreed to [the tithe] in 1103"; "Thirty years elapsed" to 1135; "Erik's promise in 1103" | introduced shortly before the archbishopric, no source names Erik; 1103 → 1135 is more than thirty | danmarkshistorien, *Tiende* |
| 12 §06 | "Archbishop Adalbert" obtained the bulls of 1133; Herman "a failed abbot" undid it | Adalbero (Adalbert died 1072); Herman was refused an abbacy more than once; his embassy's year is unknown and his biographer calls the matter "overmåde vigtig" — hedged | DBL *Herman*, *Asser* |
| 12 glossary, §09; 13 §05 | brick arrives "in the second half of the 1100s, first in southern Jutland" (12) against "the middle of the twelfth century" (13) | around the middle of the century, possibly first at the Danevirke | lex *Kirker i Danmark ca. 850–1250*; lex *Valdemarsmuren* |
| 12 §09 | "more than two thousand stone churches … Nearly all of them are still standing"; "the standard Danish account … about fifteen a year" | 1,800 to 2,000 built; 1,516 Romanesque village churches survive inside today's Denmark; 2,000 ÷ 150 is 13 (also Five things and 15 §03) | lex *Kirker i Danmark*; Kristeligt Dagblad |
| 12 §09, visit | Gjellerup "the only one that carries a date"; "a semicircular granite slab" | the oldest dated building in Denmark, "one of the only" precisely dated Romanesque churches; a stone over the south door | Trap, lex *Gjellerup Kirke* |
| 12 Meanwhile | Herrevad "the first Cistercian house in Scandinavia" | the first in Denmark; Alvastra and Nydala are 1143 | lex *Herrevad*; SFV |
| 12 §11 | "the Emperor Lothar" in 1129 | king; emperor from 1133 | DBL *Knud Lavard* |
| 12 fig. 3 caption and alt | "six of the eleven rulers … dying violently" | the chart shows five | the chart |
| 12 §12 | "Eleven weeks later, on 23 October" | 9 August → 23 October is ten weeks and five days: the date alone | D-8 |
| 12 §12 | Valdemar "king of a whole country for the first time in twenty-six years" | Erik Emune and Erik Lam were sole kings to 1146: "the first man in eleven years" | the page |
| 12 §12 | "He brought the Cistercians to Denmark in 1144" — repeated from the Meanwhile box | once | |
| 12 thread | Schleswig in 1157 "a duchy with its own dynasty" | held by a royal prince; the dynasty is Abel's, from 1250 (14 §03) | 14 |
| 12 visit | Ringsted, "where his son buried him" | Valdemar was born a week after the killing; Knud was buried there, and canonised by his son in 1170 | |
| 12 §10 | chapter 15 "arrives in 1349" | 1349–50, as 15 §03 and its Myth-check put it | 15 |
| 13 intro | Valdemar "wounded … riding away from a battlefield" | wounded at Roskilde; he rode off Grathe Hede as victor | 12 |
| 13 §01 | "rule for twenty-five years" | 1157 → May 1182 is twenty-four: "until 1182" | D-8 |
| 13 §01 | Absalon "a year or two older" | born c. 1128: about three | DBL; natmus |
| 13 §01 | "a monk … wrote the history" | Saxo, "a cleric in Absalon's household" (§08) | |
| 13 §01 | "the king whose statue now sits on horseback in the middle of Copenhagen" | the Højbro Plads statue is Absalon's | lex *Absalon* |
| 13 §03 | Jaromar's line "three hundred years of standing" | a century and a half, as the paragraph above it says | |
| 13 §04 | "An archbishop of Lund would later die on campaign in Estonia" | none did; Anders Sunesen sailed to Lyndanisse and died on Ivø in 1228 | DBL *Anders Sunesen* |
| 13 Meanwhile | Becket "five months after Ringsted" | 25 June → 29 December: six | |
| 13 glossary | the ring fortresses "three centuries dead" by the 1160s | nearly two | |
| 13 glossary, §05, visit | the Valdemarsmur "around 1170", "the largest brick structure in northern Europe", "nearly seven metres … almost four kilometres" | the 1160s; "among the largest" (as §05 already hedged); 5–7 m high, about 4 km | Danevirke Museum; Grænseforeningen |
| 13 §05 | "In 1167 Valdemar granted the village of Havn" | around 1160; the castle by 1167 (lex ties the gift to 1167 — the sources disagree) | natmus; Trap *Middelalderen i København* |
| 13 §05 | "every chapter from here to 1920 will return to it" | the thread does | |
| 13 §07 | the assembly "the same institution that will produce Jyske Lov" | Jyske Lov was given at a royal meeting at Vordingborg; "the same legal culture" | lex *Jyske Lov* |
| 13 §07, Myth, Five, checkpoint, counterfactual | Skåne 1180: "Absalon did not get his bishop's tithe"; "they lost, and they won"; "in the end were not made to pay it" | he gave it up in the 1181 settlement and restored it after the 1182 rising, without reprisals: they won for a year or so, then lost. The checkpoint "what did they nevertheless win?" is now "what did it take to make them pay?" (config and body); the counterfactual reversed | lex *Det Skånske Oprør*; DBL *Absalon* |
| 13 §08 | "Grammaticus … three centuries later" | first in the Compendium Saxonis, c. 1345: a century and a half | medieval.wiki.uib.no |
| 13 §08, Sources | "Nearly every specific thing on this page comes … from one man"; checked against "Henry of Livonia" | Saxo ends in 1185: "in the first half of this page"; Henry does not overlap him | |
| 13 glossary, Myth | Dannebrog "first attested in a source of 1380"; oldest picture "1370s or 1380s" | *Denenbroec*, Bellenville armorial, mid-fourteenth century; the oldest coloured picture in Gelre, after 1370 | lex *Dannebrog*; navn.ku.dk |
| 13 Meanwhile | the Mongols "within twenty years … two hundred kilometres from territory Valdemar had claimed" | 1219 → 1241 is twenty-two; the distance unsourced: "by 1241" | |
| 13 §11, Recall | "two hundred kilometres from any frontier"; "held for nearly three years"; "a prisoner … for three years" | unsourced; 7 May 1223 → 25 December 1225: two and a half | DBL *Valdemar 2. Sejr* |
| 13 §11, checkpoint | "a minor count with a grudge and thirty men" | "a handful of men" (Gyldendal); the checkpoint reworded to match | Gyldendal, *Jagten på Lyø* |
| 13 §12 | 1219 "is a public holiday" | a flag day | lex *valdemarsdag* |
| 13 §12, fig. 3 | "lived another fourteen years"; "Eighty years of campaigning" | 22 July 1227 → 28 March 1241: thirteen; 1159 → 1227: nearly seventy | D-8 |
| 13 §12 | the provincial laws "were written down" after Bornhöved | Skånske Lov is c. 1202–16 | 14 §01 |
| 13 Contested | "Ditmarsken" | Dithmarschen (D-15, decision D-B) | |
| 14 §01 | Jyske Lov "carried afterwards to the assembly at Viborg and adopted there"; the vignette at "the Viborg assembly" | no source; the preamble has it given at Vordingborg with the consent of the king's sons, the bishops and "the best men". The who-line now reads Vordingborg · March 1241 | lex; danmarkshistorien, *Jyske Lovs fortale* |
| 14 §01, Sources | "a hundred and sixty chapters"; "the other 160-odd chapters" | three books; the chapter count varies by manuscript (235 and 239 in two descriptions) and no reference work gives one: "over three books" | |
| 14 §03 | "so does 1848 and 1864" | so do | |
| 14 §04 | Jakob Erlandsen "died in 1274 [in Rome] still archbishop and still unreconciled" | a settlement in 1272 with large concessions from him; died on Rügen on the way home, 18 February 1274 | DBL *Jakob Erlandsen* |
| 14 §04 | "remarkable people in this band" | this century | |
| 14 §05 | "chapters 18 to 19 are largely a story about what kings had to sign" | Part E keeps coming back to it | the pages |
| 14 §06, Myth | the ballads evidence of "the fifteenth century" (§06), "the fourteenth century" (Myth), "within a generation or two of 1286" (§06) | the oldest trace is c. 1454; scholars doubt they reach back to 1286: "later centuries", "later opinion" | lex *Marsk Stig-viserne* |
| 14 §07 | 1313: "twenty-five leaders … every one of them was a farmer" | the peasants' leaders and implicated magnates were sentenced at the Viborg landsting | Gyldendal, *Guldkorn i Nørrejylland* |
| 14 §07 | Grev Gert's "young cousin" | nephew, his sister's son | lex *Gerhard 3.* |
| 14 §07, §09, §10; 15 §01 | "Gerhard 3.", "Johann 3." | Gerhard III, Johann III (D-14: German counts take Roman numerals, as the page's own figure captions already did) | |
| 14 fig. 3 | "Ten weeks", "St Bartholomew to St Martin"; the bar ran 1 August–12 November | 24 August – 9 October, about six weeks; the bar recomputed from the dates in the script, not typed | en.wikipedia *Scania Market*; danmarkshistorien *Skånemarkedet* ("august-oktober") |
| 14 §10 | "A chronicle puts it at eleven thousand men … nothing … could have fed a force that size" | 4,000 in Randers and 11,000 across Jutland | DBL *Niels Ebbesen*; Gyldendal |
| 14 §10 | "the ballad says forty-seven men" | the Jutland chronicle; a Lübeck chronicle says sixty | DBL *Niels Ebbesen* |
| 14 §10 | the Holsteiners married Valdemar "to the sister of the king of Sweden" | to Helvig, sister of the duke of Schleswig (15 §01 has it right) — and the whole 1340 deal is 15's opening; 14 now points there | DBL *Helvig* |
| 14 Five | "Every king to 1660 signed something like it" | nearly every (the glossary's own "almost every accession") | |
| 14 visit | Niels Ebbesen "on horseback" | a standing figure (E. F. Ring, 1882) | natmus; DBL |
| 15 §01 | Helvig "bore Valdemar six children"; "spent her last years at Søborg … and she died there in 1374" | at least three documented (Gyldendal says six); she died at Esrum Abbey c. 1374; the Søborg confinement is later tradition | DBL *Helvig* |
| 15 §03, Myth, checkpoint | Ribe "to seventeen in 1350" | "from about one a year to seventeen a year", not tied to 1350 (config and body) | danmarkshistorien, *Pest i middelalderen* |
| 15 §03, ← 12 | "In 1357, building a castle at Randers, he took the stone from eleven demolished churches" | Randershus stood by 1357 (Trap); the eleven churches are a local tradition — hedged | Trap *Randers' historie*; historiskranders.dk |
| 15 §04 | "ninety-eight farms and mills and seventy-one houses" vacant in Roskilde diocese | unsourced: the bishop's estates "full of deserted holdings" | Gyldendal, *Landbrugskrisen* |
| 15 Meanwhile | Danish unrest through "noble-led risings, as in chapters 13 and 14" | 1180 and 1313 were farmers' risings; the noble one is this chapter's | 13, 14 |
| 15 Meanwhile | Avignon "until 1377", twice in one chapter | once | |
| 15 Meanwhile | Visby "burned nine people … confessions … given freely …" | nine arrested; at least one burned (Tidericus, 2 July 1350); letter to Rostock; the letters' authenticity questioned | executedtoday; sehepunkte (Cole) |
| 15 §06, fig. 2 | redemption order "north Jutland, the rest of the peninsula, Funen, then Zealand" | north Jutland; Zealand (Copenhagen, August 1343); by 1348 eastern Funen, the islands, eastern Jutland; all Jutland 1354; western Funen 1365 | lex; AU; DBL |
| 15 §07 | "A settlement was reached; the terms included concessions on taxation and … an annual assembly" — before Bugge's death | the Kalundborg peace of 24 May 1360, after it | danmarkshistorien, *Landefredsforordningen 1360* |
| 15 §07 vignette | killed by "Middelfart ferrymen"; Valdemar "paid compensation to Niels Bugge's family" | a couple of local fishermen were sentenced; the burghers of Middelfart paid the annual *Buggespenge* until 1874 | danmarkshistorien; DBL *Niels Bugge* |
| 15 §08 | "the whole of the old kingdom west of the Sound" by 1360 | almost: western Funen until 1365 | |
| 15 §09 | "eighteen hundred bodies that can be measured"; "Every other vignette in this series is one named person at one named hour" | at least 1,185 excavated; 1,500–1,800 dead; and the claim is false — 08, 10 and 06 have unnamed vignettes | SO-rummet; Populär Historia |
| 15 §09 | "Gotland was a Hanseatic town"; taken "three months after taking Skåne" | Visby was; a year after (summer 1360 → July 1361) | |
| 15 §10 | "a association" | an | |
| 15 §12 | "killing eighteen hundred farmers" | as many as | |
| 15 → | "→ Part G, Part I … Estonia 1346, the Danish West Indies 1917" | Part G's claim is Tranquebar, sold 1845 (30 says so): named | 30 |
| 16 §02 | Oluf died "in the middle of the herring season" on 3 August 1387 | the market opened on 24 August (14's figure): "as the herring season began" | 14 |

**Sixteen intervals were wrong in Part D** (D-8, computed): 12's "fifteen years" (three times),
"thirty years elapsed", "nearly three hundred", "eleven weeks", "the first time in twenty-six";
13's "twenty-five years", "five months", "three centuries dead", "three centuries later", "three
hundred years of standing", "within twenty years", "nearly three years", "fourteen years", "eighty
years"; 14's "ten weeks"; 15's "three months". Part C had nine.

**The 11 → 12 promise (START_HERE).** 11 promised "dioceses, stone churches, a written church law, and
a saint" and "the English clergy Cnut sent north start it". 12 has the dioceses, the churches and the
saint; no church law (the Skåne and Zealand church laws are Valdemarian and neither page tells them),
and no English clergy. The arrow now promises "dioceses, stone churches, a tithe, and a saint". 12
gives Sweyn Estridsen 1047–1074, and 11 now follows it (§9.8): confirmed, both pages.

### 10.3 Part D — repetition and drag, fixed

- **14 §10 and 15 §01 both told the 1340 settlement** — king, marriage, quarter of Jutland — and 14's
  version had the wrong bride. 14 now hands over in a sentence: "it is where chapter 15 begins".
- **15 §05 and §12 both said Margrete was brought up by Birgitta's daughter Merete.** §12 keeps "in the
  household of Birgitta's daughter".
- **12 §12 repeated the Meanwhile box's Cistercians of 1144.** Once.
- **15 had Avignon "until 1377" in both Meanwhile boxes.** Once.
- **15's Recall repeated a checkpoint word for word** ("What is an ødegård …", Jaccard 1.0). Replaced
  with a question on Helvig, which no checkpoint asks.

**Found, kept.** 13 has Estonia's "127 years" twice (§10 and the Meanwhile box) and 15 §02 once more;
the chapters are a part apart in reading terms and 15 needs it. 14 §01's two corrections and its first
two Myth-checks make the same points — the Myth-check form restates by design. 12's Myth-check calls
Saxo "a house historian", and 13 §08 says it at length and acknowledges the series has said it before.
The "country that had already stopped growing" runs 12 → 14 → 15, each time as a pointer, and is the
part's argument.

### 10.4 Found, recorded, not changed

- **13's leding figures are unsourced.** The prose "between six and eight hundred ships", the figure's
  "c. 600–800" and "c. 150–200" (`svg_leding.txt`) and "about three marks a year per *havne*" were not
  found in any reference work reached. Gyldendal gives one ship per *herred*, "knap 200", and Saxo 260
  ships in 1159 — which would make the full levy smaller than the figure's reduced one. The figure
  says "Totals are modern estimates, and disputed"; it is not rebuilt from a number nobody can cite.
  **For the library (E-series): Erslev and the *Jordebog* on the *leding***. The checkpoint "Roughly
  how many ships was the full leding" stands on it.
- **Arkona: 1168 or 1169.** lex gives 15 June 1168, DBL "1169 (or rather 1168)". The page keeps the
  traditional 1169 in its heading and figures, with "1168–69" in §03's body. A Danish
  historiographical choice; the page states it.
- **Havn's grant: c. 1160 or 1167** — natmus and Trap c. 1160, lex 1167. The page now says around
  1160, the castle by 1167.
- **Saxo's sixteen books: eight and eight** (lex) or nine and seven (other scholarship). The page's
  eight and eight has lex behind it.
- **Helvig's children: three (DBL) or six (Gyldendal).** "At least three".
- **Trelleborg: 133 graves (Price et al., after Nørlund) or 135 (Slots- og Kulturstyrelsen).** The
  vignette follows Price, which it is built on.
- **"Ditmarschen" in 19–25** (about seventeen uses) is D-B's misspelling, for Parts E–F's own
  reading; 13 now has the agreed Dithmarschen.
- **Maps keep Danish labels** (D-15): `svg_dioceses` and `svg_terr_1050` still say Slesvig and Århus,
  `svg_pawn` and `svg_reconquest` HOLSTEN. The diagrams — `svg_reigns`, `svg_descent`,
  `svg_arithmetic` — now follow the prose.
- **Solvency 40 → 41.** The one new row is 11 → 12, which after its rewording has no anchor the sweep
  can test. Read: 12 carries all four things it promises.

### 10.5 D-15, D-13 and Recall in Part D

**D-15.** 12 had Slesvig three times and Århus once: all four now Schleswig and Aarhus. 12 also had
"Fyn" twice against Funen everywhere else (the checker's), and 13 "Mølln" for the German town Mölln.
**Schleswig 172 in 26 chapters, Slesvig 101 in 10** (was 169 / 104 in 11): Part D no longer uses the
Danish form. **Sweyn and Svend:** D-15 as written says "Viking-age kings under their English names,
from Knud the Holy under their Danish ones", which would make 12's Svend Estridsen (1047–74) Sweyn.
But the rule records practice ("as now"), and §2.3 found the practice — Sweyn in 8–11, Svend from 12 —
"deliberate and right". The pages keep it; 12's first mention now says "(Sweyn, in chapter 11's
English form)", both of 12's figure descriptions say Svend, and CONVENTIONS' wording is corrected to
the page boundary. No decision: the rule's own reason is the practice.

**D-13.** No case. 12 §04 *Odense, 10 July 1086*, 13 §03 *Arkona, June 1169*, 13 §11 *Lyø, a night in
May 1223*, 14 §10 *Randers, 1 April 1340*, 15 §09 *Visby, 27 July 1361* and 15 §12 *The ten-year-old*
are named for their vignettes' moments, and none restates the vignette: each body gives the context
before and the consequence after, as 08 §01 does. 14 §04's Margrete Sambiria paragraph is a vignette
in all but name — see R-8.

**Recall** (content-word Jaccard ≥ 0.4 against the page's checkpoints). **12 2/6, 13 0/6, 14 2/6, 15
3/6** — 15 was 4/6, §8.5's figure, and the exact repeat is replaced (§10.3). Within the norm. This
session's tokenizer gives 08 3/5 and 09 1/5 where §9.5 had 2/5 and 2/5, so the method is not
bit-identical to §8.5's; the Part D figures are relative to its own count.

### 10.6 The padded-chapter guard, given to Part D

`build_part_d.py` now runs the same retired-vocabulary check as `build_parts_abc.py` (§9.6) —
"Band X", "entry", "Era page" and the padded chapter number, with `\s+` — counts failures, prints
"all four built clean" or "!! N problems", and exits non-zero on a problem. Its own "Band D" and
"entry" labels are gone. **Tested:** with "chapter\n07" planted in a scratch copy of `c13_body.html`
it printed `vocabulary STALE {'padded': 1}` and `!! 1 problems`, exit 1; on the real bodies,
`vocabulary clean` for all four.

### 10.7 D-9 in Part D — tagged

Every who-line in 12–15 is now person · place · date · tag.

| ch | vignette | tag | why |
|---|---|---|---|
| 12 | Adam of Bremen at the Danish court | `[-]` | a canon, and a king |
| 12 | Knud den Hellige, in Ælnoth's telling | `[-]` | a king |
| 12 | an unnamed stonemason, Gjellerup | `[n]` | a craftsman, unnamed |
| 13 | Jaromar, prince of the Rani | `[-]` | a prince |
| 13 | Harald Skrænk and the farmers of Skåne | `[n]` | the farmers at their assembly |
| 13 | Valdemar Sejr and Henry of Schwerin | `[-]` | a king and a count |
| 14 | Gunner, bishop of Viborg | `[-]` | a bishop |
| 14 | Jakob Erlandsen | `[-]` | an archbishop |
| 14 | Niels Ebbesen of Nørreris | `[-]` | a squire — the page calls him "a person of no importance", but a *væbner* is of the armed landholding class; see R-8 |
| 15 | Niels Bugge of Hald | `[-]` | one of the greatest landowners in Jutland |
| 15 | the farmers of Gotland | `[n]` | |
| 15 | Margrete, aged ten | `[-]` | the vignette's own point is that she is disposed of, not acting: "neither of whom expected the bride to matter" |

**Balance: no chapter of Part D carries `[f]`, and 14 carries no `[n]`.** `vignettes.py` reports D-9
FAILURES 12, 13, 14, 15. True, not to be tagged away; none of the four is a chapter whose evidence
names no one. §10.9 puts them to Carsten.

### 10.8 Checked by a separate agent

An agent that had not seen the work checked all 118 hunks against sources and the rest of the book. It
confirmed the Glavendrup and Trelleborg facts and most of §10.2, and found eighteen items. Fourteen
were slips, nine of them in my own edits. All corrected:

- **15: Visby's poisoners "confessed under torture"** — I had taken it from a fallback source; the
  surviving letter records confession "without coercion". Now as the letters have it, with their
  authenticity questioned.
- **13: the checkpoint "How many men did it take …" had lost its answer** when "thirty men" became "a
  handful". Reworded (config and body).
- **14: "Seven weeks"** for 24 August–9 October, which is six complete weeks (D-8), and 16's Oluf dying
  "in the middle of the herring season" on 3 August, three weeks before the market opened. The figure
  says six, and 16 "as the herring season began".
- **10: "157 people in some 135 graves"** — Price et al., the vignette's own source, say 133; and
  "laid out as part of the fortress's plan" sat badly beside "some of the graves may be older". Now
  133, "laid out, it seems, with the fortress", and the lime dispute points to chapter 4.
- **08: "between forty-five and sixty metres"** (Trap also gives 70 between the reconstructed prows),
  "no grave goods" (Trap: burnt bone and a piece of iron), the vignette's date outside the page's span
  unremarked, and *vé* in a section that glosses *vi*. All fixed.
- **12: "the thirty-year gap between the promise of 1103"** — I had hedged the promise two paragraphs
  up and hardened it here. "More than thirty years … about 1103".
- **13: "So they won, for two years"** — spring 1181 to 1182 is a year or so.
- **15: "Through the 1340s and 1350s … western Funen not until 1365."** "And into the 1360s".
- **`build_part_d.py` still said "Band D" and "entry"**, the vocabulary its new guard retires.
- Beside hunks, not in them: `svg_reigns`' alt text "Six of the eleven" (the caption now five); 12's
  figure-3 caption "Svend Estridsen and five of his sons, ruling … for sixty years" (Svend and his
  sons are eighty-seven); 15's "Gotland was a Hanseatic town"; 12's "Fyn" twice; 13's "Mølln".

**Declined, with reasons:** that Part D's D-9 failures are a slip (they are the finding; §10.9); that
Svend should be Sweyn (§10.5); that 12's "1349–50" contradicts 15 (15 says "1349 or 1350 — the standard
date is 1350" and its Myth-check "1349–50"); that "Dithmarschen" should follow the pages' majority
"Ditmarschen" (D-B decided Dithmarschen; 19–25 are unread).

### 10.9 Decisions for Carsten — Part D, one at a time

Each recommendation is a subject to be sourced detail by detail before drafting, as R-3, R-4 and R-5
were; the facts below are what a first search found, not what will be written.

**R-6. 12 has no woman as agent.** Its three vignettes are a German canon, a murdered king and an
unnamed mason. *Recommendation:* **Queen Bodil, 12 §06 *Lund, 1103*, `[f]`** — Erik Ejegod's queen, who
went with him on the pilgrimage of 1103, went on to the Holy Land after he died on Cyprus, and died on
the Mount of Olives. The page already gives her one line (§06's close); the vignette would be the
particular inside a section about the price of an archbishopric, and the one woman the section names. About 250 words. *Alternative:* Ingeborg of Kiev naming her posthumous
son after her grandfather, 12 §11 — agency in one act, and thinner.

**Answered 22 September 2026: as recommended.** Queen Bodil in 12 §06, `[f]`, to be sourced,
drafted and checked in review session 7.

**R-7. 13 has no woman as agent.** *Recommendation:* **Ingeborg, Knud 6.'s sister, 13 §09 *The north
German years*, `[f]`** — married to Philip II of France in August 1193, repudiated the day after the
wedding, she refused to go home, refused the annulment, appealed to Rome and outlasted him; Philip took
her back in 1213. Danish royal marriage policy in the reign the section covers, and a woman who would
not be disposed of. About 300 words.

**Answered 22 September 2026: as recommended.** Ingeborg, queen of France, in 13 §09, `[f]`, to
be sourced, drafted and checked in review session 7.

**R-8. 14 has neither.** *Recommendation, in two parts:* (a) **`[f]`: Margrete Sambiria, 14 §04, by
re-scoping the paragraph that is already there** (D-13's "re-scoped so the vignette has somewhere to
stand") — regent from 1259 for a ten-year-old, beaten and taken prisoner at Lohede in 1261 with the
boy, freed, and handing over a working monarchy in 1266. The paragraph says she "gets roughly a line
in most accounts"; the vignette would be the fix. (b) **`[n]`: tag the Niels Ebbesen vignette `[n]`**
on the page's own ground — "a landowner of no great standing and no royal blood whatever … a person of
no importance" — as 09's Frideborg was tagged on "not a king". *Against (b):* a *væbner* is of the
armed landholding class, and `[n]` would be the weakest in the book. *If (b) is refused:* a vignette
for §02 *The last thralls* from Jyske Lov's thrall provisions, which name no one — the part's
evidence here really is thin.

**Answered 23 September 2026: as recommended, both parts.** Margrete Sambiria as 14 §04's `[f]`
vignette, by re-scoping the paragraph already there, and the Niels Ebbesen vignette retagged `[n]`
on the page's own ground — the weakest `[n]` in the book, and recorded as such. For review
session 7.

**R-9. 15 has no woman as agent.** *Recommendation:* **extend 15 §12's vignette with Margrete's own
letter from Akershus, c. 1370** — the *nødbrev* in the Norwegian National Archives, in which the
queen, about seventeen, writes to Håkon that she and her household lack food. It turns the vignette
from a girl disposed of into a young woman managing a household in her own words, inside 15's span and
before 16's story begins; 16 does not use it. Retag `[f]`. About 150 words added.

Until they are answered and carried out, `vignettes.py` reports 12, 13, 14 and 15 as D-9 failures,
and that is correct.
