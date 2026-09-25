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

**Answered 23 September 2026: as recommended.** 15 §12's vignette extended with the *nødbrev* of
c. 1370 and retagged `[f]`, to be sourced, drafted and checked in review session 7.

Until they are answered and carried out, `vignettes.py` reports 12, 13, 14 and 15 as D-9 failures,
and that is correct.

**All four carried out in review session 7 (§11.1): no D-9 failure in Parts A–D.**


## 11. Session 7 — Part D's missing women, and Part E read (chapters 16–20)

*23 September 2026, from `START_HERE_review_7.md`.*

**The cold run matched every line.** A fresh clone of `eed5803`: git status clean; tidy reports and
deletes nothing, 45 bodies; fixture and seams pass; debuild 45 identical; 45 of 45, 338,244 page
words, 26.8 h, parts A 21,397 · B 26,326 · C 26,228 · D 31,136 · E 35,042 · I 74,403; vignettes
136/105, D-9 failures 12–15, selftest passes; figcheck 98/30/0; one OVER, *Kalmar, 17 June* at 849 — 16 §08, which START_HERE
called 17; draftnotes clean in 45 pages and 14 drafts; appcheck 159; freshcheck 14; sweeps: 2 pointers, 0
insolvent, 0 same-page glosses; Schleswig 172 in 26 against Slesvig 101 in 10; sweep_facts 5; arrows
254 and 37 thread notes, form 7, direction 0, D-1 0, titles 0, solvency 41, prose references 0,
footers 0, `<h1>` 0, 9b 0. **One difference, harmless:** item 144's pages are in their own commit,
`5a60c3b Build pages`, not in `dcc12f7` with the sources; debuild shows no drift.

Two research agents sourced the four vignettes; five fact-checked chapters 16–20, one each; a
sixth, which had not seen the work, checked all 145 hunks (§11.8); a seventh made the first search
for §11.9.

### 11.1 R-6 to R-9 carried out — and the recommendations' facts checked first

| the recommendation said | the sources say | ground |
|---|---|---|
| R-6: Bodil went with Erik "on the pilgrimage of 1103" | they left in 1102 or early 1103; Knud (Lavard) left with Skjalm Hvide at Fjenneslev, the kingdom with Asser and Harald Kesja (Erik's son by a concubine, not his brother) | DBL *Skjalm Hvide*, *Knud Lavard*, *Harald Kesja*; danmarkshistorien *Erik Ejegod* |
| R-6: she "died on the Mount of Olives" | right, year only (1103); buried in the valley of Jehoshaphat. The ending comes through late tradition, and the page says so | DBL *Bodil*; Kvindebiografisk *Bodil* |
| R-6: (not in the recommendation) | she and Erik stand together on Durham's list of benefactors; she is of Asser's kin on Saxo's account (lex: uncertain); one historian calls her going on "unique for a woman of the time" | Kvindebiografisk *Bodil*; DBL; lex |
| R-7: married August 1193, repudiated the day after | married 14 August at Amiens; *she* was crowned the next day and repudiated straight after the coronation | DBL *Ingeborg – dronning*; Fenger (Gyldendal og Politikens) |
| R-7: "she refused to go home" | she *and her escort* refused | DBL |
| R-7: "Philip took her back in 1213" | as queen, "uden ægteskabelige rettigheder" | danmarkshistorien *Ingeborg* |
| R-7: (dates the page needed) | interdict proclaimed December 1199, lifted 7 September 1200; Étampes from 1200; letters to Celestine III (1195) and Innocent III (1203) quoted from Epistolae; died 1237 or 1238 at Corbeil | Catholic Encyclopedia; DBL; Epistolae 430, 24140; lex |
| R-8: regent "for a ten-year-old" | nine or ten (born 1249, month unknown) | DBL *Erik Klipping* |
| R-8: "beaten and taken prisoner at Lohede with the boy, freed" | she *commanded* at Lohede, 28 July 1261; she was freed in 1262 through Albrecht of Brunswick, the boy only at the peace of 1264 | lex *Margrete Sambiria*; DBL |
| R-8: 14 §04's paragraph | "archbishop in exile appealing to Rome" (he was in prison when she took over; Rome in 1264); "got them both released" (see above); "northern Estonia as her dower" (Estonia and Virland for life, 13 May 1266, run from Nykøbing Falster); *Sprænghest* "the pace at which she travelled" (the name first found some sixty years after her death, "the violent rider", with a legend) | DBL; lex; Kvindebiografisk |
| R-8: (beside it) 14 §04's Jakob Erlandsen vignette | "arrested at Hagenskov" (seized outside Lund on 5 February 1259, imprisoned at Hagenskov); "the interdict came down" (declared, patchily kept); "went into exile" (freed that summer; Rome 1264); the poison rumour, "never proved" (DBL: late tradition) | DBL *Jakob Erlandsen*; lex; roskildehistorie.dk |
| R-9: "the *nødbrev* … she, about seventeen, writes that she and her household lack food" | right: Akershus, St Luke's day (18 October), the year archive-dated c. 1370; "jeg og mine tjenere lider stor nød på mat og drikke"; she asks for credit with the merchant Vestfal; written by a secretary on parchment in a Swedish-Norwegian mixture; Håkon probably in Bohuslän; Riksarkivet AM fasc. 98 nr. 5 | Arkivverket; NDLA (Riksarkivet's translation); SNL |

**(a) Queen Bodil, 12 §06 *Lund, 1103*, `[f]`.** After "died on Cyprus in July 1103", which lost its
one-line Bodil; the vignette is her going on alone from Paphos. Who-line *Bodil, queen of the Danes ·
Paphos, Cyprus · July 1103*. About 280 words. Not D-13: the section is named for Lund.

**(b) Ingeborg, 13 §09 *The north German years*, `[f]`.** After the Knud 6. paragraph. Who-line
*Ingeborg, queen of France · Amiens · 15 August 1193*. About 330 words.

**(c) Margrete Sambiria, 14 §04, `[f]`, by re-scoping (D-13).** The paragraph that said she "gets
roughly a line in most accounts" is now one sentence of body and a vignette at Lohede, 28 July 1261.
About 330 words. **Niels Ebbesen retagged `[n]`**, on the page's own ground, and recorded as the
weakest `[n]` in the book.

**(d) 15 §12's vignette extended with the letter, `[f]`.** The two paragraphs that disposed of her
are kept in shorter form; the letter is added, and the vignette ends where it did. Who-line
*Margrete, queen of Norway · Akershus · 18 October, c. 1370*. Found beside it: 15 had Oluf "the
five-year-old son" at Valdemar's death (October 1375, and Oluf was born at Christmas 1370): four.

`vignettes.py`: **no D-9 failure in Parts A–D.** 139 vignettes carry a place, 109 distinct.

### 11.2 Part E, read — errors of fact and of the book against itself, fixed

| ch | the page said | it is | ground |
|---|---|---|---|
| 16 tagline, Five, fig. crowns | Oluf "dies at seventeen" | sixteen (born at Christmas 1370) | DBL *Oluf 2.* |
| 16 tagline | "Twenty-two years later three kingdoms" (from 1387) | "By 1397" | D-8 |
| 16 §01, glossary, ← 14 | a *håndfæstning* "at every accession … 1396, 1448, 1460" | none in 1396; Christoffer promised one and never sealed it; 1460 is the duchies'. "Most accessions" | danmarkshistorien *Håndfæstning* |
| 16 §01 | "Both grandmothers' families" | both boys' — they had one grandmother | |
| 16 §01 | Oluf "aged five" at Valdemar's death | four | DBL |
| 16 §02 | canonisation "later in this chapter" | chapter 17 | |
| 16 §02 | Oluf "aged ten" at Håkon's death, 1380 | nine | DBL |
| 16 §03, glossary | the Atlantic lands "for a century and a half"; the North Atlantic "does not leave until 1944 and 1948" | Greenland 1261, Iceland 1262–64: "a century and more"; the Faroes and Greenland are still in the realm | |
| 16 §03; 17 §02 | Orkney and Shetland "until 1468" | 1468 and 1469 | 19's own dates |
| 16 §04 | Oluf died "as the herring season began … in front of witnesses from a dozen countries" | the timing is not sourced either way (14 has the market from 24 August; Swedish sources from late July) and the crowd rests on it: "at the castle above the herring ground". The rumours' sentence now names 1402. Myth-check likewise | 14; DBL |
| 16 §05 | Bo Jonsson died "in 1387" | August 1386, as the vignette says (SBL: 20 August; not reachable) | the page |
| 16 §05 | "In October 1389 she was formally installed as regent of Sweden" | not found; DBL: after Åsle all Sweden but Stockholm was hers | DBL *Margrete 1.* |
| 16 Meanwhile | Kosovo "eight months before Åsle"; Åsle "killed almost nobody of note" | nearly four months after; Henrik Parow, her commander, fell | Britannica; DBL *Henrik Parow* |
| 16 fig. 2 | "Ten years … 1387–1398" | eleven | |
| 16 vignette | "the fifteenth century housed captive kings" (1389); Albrecht's son "died in captivity here in 1397" | fourteenth; Erik was freed with his father in 1395 and died on Gotland in 1397 | NE *Erik av Mecklenburg* |
| 16 §07, glossary | *Dronning Margretes Fred*, "recorded at the assemblies of 1396" | no source uses the name; the ordinance lists six peaces — church, women, house, farmyard, plough, assembly | danmarkshistorien, the 1396 ordinance |
| 16 §08 | "at least a month" (17 June to 13 July is 26 days); seals "hung" | "some four weeks at least"; the passage now says the seals are impressed in paper once, below | Gyldendal og Politikens *Kalmar sommeren 1397* |
| 16 §08, Five, Contested, Sources | Erslev "1892", who "treated the union letter as the real settlement"; "Bagh (2003)"; "a hundred and thirty years" | 1882, and he thought Margrete let the letter go unratified rather than accept its limits; the recent reading is Markus Hedemann's (*Scandia*, 2011); Christensen 1980; "more than a hundred and forty years" | Hedemann, *Scandia*; Historisk Tidsskrift |
| 16 Causal | her power became "*more* secure after her son died" | against §04 and the Myth-check; reworded | |
| 16 fig. titles | 1375 claim "days after" Valdemar's death | six weeks, as §01 says | |
| 17 intro, §03, Myth | the colony "stopped existing" in these years; "nobody in Copenhagen noticed for three hundred more"; "nobody … asked until Hans Egede" | fell silent; kings sent ships from 1472/73 (Pining and Pothorst), 1579, 1581; Christian 4.'s of 1605 and 1606 found Inuit | lex *Grønlandsekspeditioner* |
| 17 §03 | "four or five thousand"; ivory "returned through Portuguese trade" | at most about three thousand; elephant ivory was reaching Europe from the thirteenth century | Trap Grønland; Barrett et al. 2020 (Cambridge) |
| 17 Myth | "a wedding certificate from 1408" | the wedding of 1408, certified in April 1409 (as Sources said) | |
| 17 §02 | "the recess of 1536 declares that Norway …" | §3 of Christian 3.'s accession charter (also 20 §07, Myth, arrow, fig. weeks; and 21) | snl *Norgesparagrafen* |
| 17 glossary | *fæste* "until the 1780s" | the commonest way well into the nineteenth century (43 % of peasant land in 1835; abolished 1919) | lex *fæste* |
| 17 §04, fig. 2, Five | the deserted-farm peak "in the twenty years after 1400" | around 1400 (the glossary's own date) | Gyldendal og Politikens *Den store landbrugskrise* |
| 17 §05 | Margrete and her women "embroidered altar cloths" | not found; cut | |
| 17 §06 | Lodehat's "stated ground … too Danish"; "the monks called it what it was" | Roskilde's own account: Sorø "for lille og for tæt forbundet med danske monarker"; he took her "næsten med vold mod munkene" | roskildedomkirke.dk |
| 17 §06 | "What he built over her, and what Erik paid for in 1423" | Lodehat died 1416; Erik had the tomb made | DBL; roskildedomkirke.dk |
| 17 §06, Sources | "Only the coffin and most of the effigy are medieval … reconstructed between 1862 and 1912" | the figure is original except the crown; the side figures c. 1900 | roskildedomkirke.dk |
| 17 §06 | the gown "gilded silver thread on purple silk, probably woven at Lucca" | red and gold silk, woven in Italy | ROMU |
| 17 visit | "the unbroken line of royal burials" | almost unbroken | roskildedomkirke.dk |
| 17 Meanwhile | Gotland "taken from her in 1398"; "briefly three" popes | taken in 1398 and sold to her in 1408; three from 1409 | DBL; 16 |
| 17 vignette | the false Oluf burned "in front of merchants from across northern Europe, which was the point" | unsourced; "at Falsterbo" | |
| 18 §01 | "Over forty-seven years he founded towns" | twenty-six years of rule (1412–39) | D-8 |
| 18 §03, glossary, Myth, visit | Krogen "pulled down" for Kronborg | rebuilt from 1574, and much of it is inside Kronborg's walls | Trap *Kronborg* |
| 18 §03, fig. 1, Five, figs_17 | Erik "strengthened Kärnan"; "closed the Great and Little Belts to foreign shipping altogether" | Kärnan is Erik Menved's, c. 1313; the Belts were tolled — a ship that took the Great Belt paid at Nyborg | Helsingborg stadslexikon; lex *Sundtolden*; danmarkshistorien |
| 18 §03 | "Both shores … Danish since 1360" (15 → 18 promises the Hanse's Sound castles) | the Hanse held the Skåne castles from 1370 to 1385; now said, and 15's arrow is solvent | 15 §11 |
| 18 §04 | grievances "the toll … his attempt to stir up opposition inside Lübeck"; islands plundered in 1427 | the war began in 1426, before the toll is documented; Lübeck intrigue and island list unsourced: Schleswig and the Dutch, "the toll, once it came, was one more"; "Bornholm among them" | danmarkshistorien; Wikipedia (pointer) |
| 18 vignette | Sorø "forty kilometres"; "first battle … artillery at range"; queen "for twenty-four years" | about seventy; unsourced, cut; twenty-three (1406–1430) | DBL *Philippa* |
| 18 §05, visit | Flensborg; "outlast … the sailing ship" | Flensburg (D-15); cut | |
| 18 vignette | Engelbrekt took complaints "to the council, twice" | to the king | |
| 18 §07 | "In 1438 … Visborg since 1408"; Erik "very nearly outliving the man after that" | 1437 or 1438; Gotland since 1408; Christian 1. lived to 1481 — cut | danmarkshistorien; SNL |
| 18 §08 | Katarina "one of the two Pomeranian grandchildren Margrete had brought south … in chapter 17" | Erik's sister, called north like him, married into the Wittelsbach house; 17 does not tell it | DBL *Catharina* |
| 18 vignette | 1441 grievances "the tithe … reimposed after his coronation"; executed "six days later, on 12 June" | coronation 1 January 1443, after the rising; dues pressed by nobles, prelates and crown; "about a week later"; the bishop's tithe came in 1443 | DBL *Reventlow*, *Christoffer 3.* |
| 18 §10 | Dorothea "eighteen" in 1449 | about nineteen | DBL *Dorothea* |
| 18 §11 | 33½ million rigsdaler, "fourteen years' income"; the Dutch "in 1650" | 30,476,325 rigsdaler, which the treaty's editors call fourteen years' income; 1649. *First changed to "twelve years'" from a secondary page's 33½ million; corrected from the treaty (§11.8a)* | danmarkshistorien *Øresundstraktaten, 14. marts 1857*, art. 4 |
| 18 Meanwhile | 1453 "closing the eastern Mediterranean to Genoese and Venetian trade" | "unsettling" | |
| 18 Five | Engelbrekt "a mine-owner" | a minor nobleman from the mining country, as the vignette says | |
| 18 §09 | *vornedskab* "formalised later in this century" | a custom that takes hold later in the century | lex *vornedskab* |
| 18 fig. toll | aria-label describes a panel the figure no longer has | removed | the figure |
| 19 §02, Five | "At Ribe on 5 March 1460 the knighthood elected"; a reserved right of resistance "since 1282" | elected 2 March, charter sealed 5 March; no resistance clause — no tax without consent, native officials, annual courts | danmarkshistorien *Ribebrevet* |
| 19 §01 | Holstein reverting to "the Emperor" | to a lord inside the Empire | |
| 19 §04 | married "in 1468"; Norse "for five hundred years"; Norn "over the next two hundred years" | agreed 1468, wedding 1469; some six centuries; three | |
| 19 §05 | Notke's saint "is Sweden", princess Stockholm | the saint is Sten Sture, the princess Sweden | Stockholm konst |
| 19 Meanwhile | Henry VI "deposed and restored twice"; 1494 "began forty years of war" | deposed twice; the Italian Wars ran to 1559 | |
| 19 §06, glossary | *vornedskab* "Zealand and the islands", "formally bound"; Hans "hired Scottish and Dutch captains" | Zealand, Møn and Lolland-Falster, by custom from the late 1400s; unsourced, cut | lex *vornedskab* |
| 19 §07 | Holstein count beaten "in 1309"; enfeoffed "in 1473"; Meldorf "on 14 February" | 1319; 1474 (as §02); date unsourced, dropped | geschichte-s-h.de; DBL *Christian 1.* |
| 19 §07, Five | Dithmarschers "perhaps two thousand"; lost "fewer than a hundred"; "eleven Ahlefeldts, six Buchwalds"; "forty years earlier" | barely a thousand at the bank; losses unrecorded; seven Ahlefeldts or eleven by different counts, Buchwalds unsourced; 1460 (39 years 11 months: D-8) | dithmarschen-wiki; de.wikipedia (pointer) |
| 19 vignette | Ahlefeldt "born about 1440"; "a road eight metres wide"; "Slesvig cathedral" | unsourced, cut; Schleswig (D-15) | |
| 19 §08 | Sweden "held for four years out of a possible sixty" | "fewer than ten of the fifty-two years since 1448" | 18's Myth-check |
| 19 §09, config | "Sigbrit Villumsdatter"; a court "where subjects could sue their lords"; who-line "keeper of the king's accounts" against a checkpoint answering "none" | Sigbrit Villoms (DBL); unsourced, cut; "the king's financier without an office" | DBL *Sigbrit Villoms* |
| 19 §10 | burgomasters "hanged" and then "beheaded … So were fourteen members of the council, burgomasters" | the second list trimmed to what the first allows | Historisk tidskrift 2019:3 |
| 19 vignette | Kristina held "until September"; "Ten weeks later"; imprisoned "with her mother-in-law … who dies there"; released 1524 | 5 September; nine weeks; with her mother and daughters — her half-sister Cecilia (Gustav Vasa's mother) and her own daughter died; released 1523 | SKBL |
| 19 §11, glossary | sailed "20 April 1523"; "twenty-seven years" in captivity | 13 April; twenty-six (1 July 1532 – 25 January 1559) | DBL *Christian 2.* |
| 19 §11 | Sweden governed "for eleven years out of seventy-five" between 1448 and 1520 | three spells, 1457–64, 1497–1501, 1520–21: about a dozen of seventy-five (to 1523) | 18 |
| 19 Sources | Svaning "appointed in 1553 by Christian 3." as crown historian; Olaus Petri written "for" Gustav Vasa's regime | "with the government's approval but without an office" (DBL); "under" | DBL *Hans Svaning* |
| 19 visit | "Gottorp Slot, Slesvig" | Schleswig (D-15) | |
| 20 intro, Causal, Contested | Christian 2. deposed "thirteen years earlier"; "a prisoner for eleven years"; "in prison since 1523" | eleven; gone eleven years; in exile, then prison from 1532 | DBL |
| 20 §03 | Christian 3. "thirty-nine" in April 1533 | twenty-nine (born 12 August 1503) | DBL |
| 20 §03, glossary, config | the 1533 council did "something no Danish council had done before"; "the only time it ever tried" | it postponed the election a year and governed itself; the checkpoint asks what it did instead of electing | DBL *Christian 3.* |
| 20 §03 | "Chapter 18 followed the town … to its defeat by Kong Hans in 1512" | chapters 18 and 19 | 19 |
| 20 §04 | Ry: "the Jutland nobility and bishops"; Rantzau "put down Ditmarschen's neighbours"; peace with Lübeck in November 1534 "separating the town from its own expedition" | the councillors of Jutland and Funen; Lund, 1525; Stockelsdorf bound Lübeck in Holstein only, and the final peace was February 1536 (← 18 now 1536) | DBL *Rantzau*; milhist.dk; danmarkshistorien *Grevens Fejde* |
| 20 §05, glossary | Clement born "to a farming family in Aaby parish"; recognised "at Storvorde"; "something over a hundred" manors | "by late tradition a man of Vendsyssel"; place and number unsourced, dropped | DBL *Clement* |
| 20 §05, vignette, Myth, Five | "perhaps two thousand" dead at Aalborg (five times) | "many hundreds, perhaps as many as two thousand" | Nordjyske Museer |
| 20 §06 | "Funen was over in a day"; "Copenhagen surrendered … and Malmø with it" | decided in a day, Odense hailed Christian on 3 July; Malmø gave up in April | Gyldendal og Politikens; danmarkshistorien |
| 20 vignette | Rantzau "fifty-two … fought in Italy"; "his son Henrik built Breitenburg" | forty-two (born 12 November 1492); pilgrimage to Jerusalem; he built it himself | DBL *Johan Rantzau* |
| 20 vignette | Rønnow "the man who had just prosecuted him" | argued for banishment rather than death, and carried it | danmarkshistorien *Rønnow* |
| 20 §07, Myth, Five, fig. weeks | the bishops arrested "in one night, across the country"; "Twelve weeks" | begun that night in Copenhagen, carried through across the country; thirteen weeks (29 July – 30 October) | DBL *Christian 3.*; danmarkshistorien |
| 20 §07 | Ove Bille "served three kings as chancellor"; "eighteen more" | King Hans's chancellor and, after Mogens Gøye, the leading statesman from 1523; nearly eighteen | DBL *Ove Bille* |
| 20 §07, glossary | the Church Ordinance "three hundred years", "into the nineteenth century" | until the law code of 1683 | DBL *Christian 3.* |
| 20 §09 | "Two of the arrested bishops went on to serve the new church" | none did; cut | DBL *Torben Bille* |
| 20 §09, Causal | the images stayed, "which is why Danish churches still have their wall paintings while English ones do not" | they stayed until whitewashed in the next two centuries, which is how so many survived to be uncovered | kristendom.dk |
| 20 Five, Myth | "all church property"; "the crown took the church's third" | the bishops' at once, the monasteries' by attrition (Sources already called "all" a myth) | danmarkshistorien *Reformationen* |
| 20 Meanwhile | Henry VIII "in 1534 … began dissolving the monasteries"; Münster "1534–35"; Trent "two years from being summoned" | supremacy 1534, dissolution from 1536; fell 1535, cages 1536; summoned in 1536, opened 1545 | Britannica |
| 20 visit | Tausen preached "from 1526" at Viborg Domkirke; Malmø in a visit block | from 1525, in his Johannite house; Malmö (D-15: Swedish form in visit blocks) | DBL *Hans Tausen* |
| 20 header | "Ten years later" | "A decade later" | |

**Thirty-four intervals and ages were wrong in Part E** (D-8, computed; one of them, 16's "aged
five", found by the fixes' checker, which also found three wrong intervals in my own fixes, §11.8):
16's "seventeen" (three places), "aged ten", "aged five", "twenty-two years later", "a century and a
half", "eight months before", "thirty more to run", "a hundred and thirty years", "at least a month",
"ten years"; 17's "fifteen years" (three places), "some years"; 18's "forty-seven years",
"twenty-four years", "eighteen", "very nearly outliving", "six days later"; 19's "forty years
earlier", "five hundred years", "two hundred years", "four of sixty", "eleven of seventy-five",
"forty years of war", "ten weeks", "twenty-seven years" (twice), "three days later"; 20's "thirteen
years", "thirty-nine", "fifty-two", "a prisoner for eleven years", "twelve weeks", "eighteen more",
"three hundred years", "ten years later". Part C had nine, Part D sixteen.

**The 15 → 16 and 15 → 18 promises (START_HERE).** 16 has Oluf's election of 1376 and opens on the
realm reassembled: solvent. 18 had Erik's toll but not the Hanse's Sound castles; §03 now says the
Hanse held the Skåne castles 1370–85, which is also the qualification its "both shores since 1360"
needed.

**The D-B carry-over, 19–21.** "Ditmarschen" is Dithmarschen in prose: 11 in 19, 1 in 20, 6 in 21,
and the config's checkpoint; 16, 17 and 18 had the Danish "Ditmarsken" in English prose (three),
now Dithmarschen as 13's was. Danish words stay Danish: 19's glossary term and 21's key
*Ditmarsken 1559*. 24 and 25 have none.

### 11.3 Part E — repetition and drag, fixed

- **16 told Erik's selection twice** — §06's close and the §07 vignette, down to a near-identical
  sentence about the name "Erik". §06 keeps the fact (February 1388, a small boy from Pomerania) and
  points to the vignette.
- **16 told the Lindholm terms twice** (§06 and the Albrecht vignette). The vignette points back.
- **16 described the union letter as an object twice in §08** before the Myth-check and Five did it
  again. The first description is gone; "described below".
- **16's two Meanwhile boxes both had the truce and the schism.** Once, in the second.
- **17 said "the men she trusted were increasingly Danish" in §01 and §02**, nearly word for word.
  §01 points to §02.
- **17 repeated 16's Iceland sentence** ("its own law and its own assembly …"). Cut in 17.
- **17's vignette and Myth-check both told Oluf's death "transformed within a week … fifteen years
  later"**. The Myth-check points to §01.
- **17's figure 2 caption repeated §04's "one estate … not a national average"** (and the figure
  itself says it a third time — recorded, §11.4). The caption is cut to what the figure adds.
- **20's two Meanwhile boxes both had the Peasants' War and the Schmalkaldic League.** Once, in the
  first.
- **Recall repeated checkpoints word for word** in 17 (one), 18 (two) and 19 (one). Replaced with
  questions no checkpoint asks (§11.5).

**Found, kept.** 17's Greenland monopoly "since 1294" is in §03, the Myth-check and Five — the
Myth-check and Five restate by design. 18's Krogen/Kronborg runs through the glossary, §11, the
Myth-check and the visit block, each for its own reason. 19's partition of 1490 is the chapter's
argument and recurs as one. 16 and 17 both gloss *skattland*: the rule is first use in each page.

### 11.4 Found, recorded, not changed

- **20's figure 3 land shares have no source.** The bars (crown 16 → 49 per cent, church 33,
  nobility 43, freeholders 8) were not found in any reference work reached; Den Store Danske gives
  the crown "ca. 10 %" before and "40–50 %" after, to 1660, counting the rebels' forfeited farms. The
  Contested question now reports it; `figs_19.py`'s docstring says the shares are schematic and
  unsourced. **For the library (E-series): a sourced breakdown of Danish landholding c. 1525 and
  c. 1560.** The prose's "roughly a sixth" stands on the figure and should move with it.
- **Margrete Sambiria and the pope.** DBL: she "har … været langt i at opnå" papal authorisation of
  female succession; lex: "imødekom paven gerne, og brevet er i dag stadig bevaret". The vignette
  follows lex, which names the surviving letter.
- **The herring market's dates.** 14's figure has 24 August – 9 October (session 6); the checker
  found Swedish accounts that open it at the end of July, and danmarkshistorien gives "august–oktober".
  16 no longer times Oluf's death against it. 14 is not changed without a better source.
- **Bo Jonsson Grip's share of Sweden**: 16 says "close to a third"; Kalmar läns museum says two
  thirds, including all Finland. SBL was not reachable.
- **The Sankt Jørgensbjerg date.** 18 has 6 June 1441 (DBL *Reventlow*); Skalk reports two
  engagements in May. Kept to DBL.
- **Dead checkpoint blocks in 16–20's bodies.** `build_part_e.py` strips every `<div
  class="check">` in a body and inserts its config's. The body blocks are dead text, several
  differ from what ships — 17's asks about Kalmar, which is 16's — and 20's coda block is lost
  entirely. They do not reach a page. Remove them when Part E is next opened, or teach tidy to
  report them.
- **16 §08 is still OVER** (852 words, from 849: the historiography sentence is longer). D-16.
- **Maps keep Danish labels** (D-15): `svg_terr_1397` says Slesvig; `svg_roads` Flensborg and
  Hamborg.
- **`figs_19.py` makes chapter 20's figures** and `figs_17.py` chapter 18's (pre-renumbering names);
  the docstring of the first now says so.

### 11.5 D-15, D-13 and Recall in Part E

**D-15.** 19 had Slesvig twice, both the town: *Schleswig cathedral*, *Gottorp Slot, Schleswig*. 18
had "Flensborg" once in prose. 20's visit block had Malmø: Malmö. 15's new vignette says Bohuslän.
**Schleswig 178 in 26 chapters, Slesvig 99 in 9**: Parts A–F no longer use the Danish form in prose.
18's *Sønderjylland* is glossed and deliberate.

**D-13.** No case needing a change. 18 §06 *Engelbrekt, 1434* is named for its vignette's subject,
and the vignette adds his background and death to a body about the rising; 19 §07 *Hemmingstedt* and
§10 *Stockholm, November 1520* are named for their vignettes' moments and give the context before and
the consequence after. 20's Rantzau vignette (18 December 1534) sits in §06 after events of 1536;
out of order, and it retells §05's Aalborg — a candidate for moving when 20 is next opened.

**Recall** (content-word Jaccard ≥ 0.4 against the page's shipped checkpoints, measured on pages
built in a scratch copy). Before: 16 1/5, 17 2/5, 18 2/6, 19 2/6, 20 1/6, four of them exact repeats
(Jaccard 1.0). After replacing the four: **16 1/5, 17 1/5, 18 0/6, 19 1/6, 20 1/6.**

### 11.6 The padded-chapter guard, given to Part E

`build_part_e.py` had none. It now runs `build_parts_abc.py`'s retired-vocabulary check — "Band X",
"entry", "Era page", the padded chapter number with `\s+` — counts failures, prints "all five built
clean" or "!! N problems", and exits non-zero on either a problem or a failure its old checks
already counted. **It fired on the first run, falsely:** 18 §11 uses "entry" twice for a line in the
toll register. The two phrases, and only they, are allowed (`LEDGER_ENTRY`); each is removed once
before counting. **Tested in scratch copies:** "chapter\n07" and "this entry" planted in
`c17_body.html` gave `STALE {'entry': 1, 'padded': 1}`, `!! 1 problems`, exit 1; a third "entry" in 18
gave `STALE {'entry': 1}`, exit 1; the real bodies, "vocabulary clean" five times.

### 11.7 D-9 in Part E — tagged

| ch | vignette | tag | why |
|---|---|---|---|
| 16 | Bo Jonsson Grip, drots | `[-]` | a magnate |
| 16 | Albrecht of Mecklenburg | `[-]` | a king |
| 16 | Erik of Pomerania, aged seven | `[-]` | a king-to-be |
| 17 | the false Oluf | `[n]` | poor, sick, unnamed |
| 17 | Thorstein Olafsson and Sigrid Björnsdóttir | `[-]` | the vignette is about the paperwork; she does nothing the page can name, and Icelandic families who could keep certificates were not poor |
| 17 | Abraham Brodersen Baad | `[-]` | a knight and councillor |
| 18 | Philippa | `[f]` | |
| 18 | Engelbrekt | `[-]` | lower nobility |
| 18 | Henrik Tagesen Reventlow | `[-]` | a nobleman, whatever army he led |
| 19 | Hans von Ahlefeldt | `[-]` | a knight |
| 19 | Sigbrit Villoms | `[f][n]` | a commoner woman running the royal finances |
| 19 | Kristina Gyllenstierna | `[f]` | she negotiated the surrender |
| 20 | Hans Tausen | `[-]` | a monk and royal chaplain |
| 20 | Skipper Clement | `[n]` | a skipper leading a peasant rising |
| 20 | Johan Rantzau | `[-]` | |

**D-9 failures: 16 (neither), 17 (no `[f]`), 18 (no `[n]`), 20 (no `[f]`).** True, not tagged away.
None is a chapter whose evidence names no one. §11.9 puts them to Carsten.

### 11.8 Checked by a separate agent

An agent that had not seen the work checked all 145 hunks against sources and the rest of the book,
confirmed the four vignettes and most of §11.2, and ran the guard. It found twelve slips, and two
contradictions outside the diff. Eleven were mine or survived my rewriting, and all twelve are
resolved:

- **13: Ingeborg "crowned beside him"** — only she was crowned; Philip had been since 1179.
- **15: the who-line said 1370** while the prose said "probably in 1370": "c. 1370". *Båhuslen*:
  Bohuslän.
- **16: "Oluf, aged five"** in October 1375 (four); **"a woman of thirty-six"** once I had anchored
  the sentence to February 1388 (mid-thirties); **"three weeks before the market opened"** — which I
  had written while correcting the herring season, from 14's date alone (§11.4); **"four months after
  Åsle"** (nearly four).
- **17: "nearly two centuries before a Danish king sent ships"** — Christian 1. sent Pining and
  Pothorst in 1472/73 for this purpose; and "1605–07" is 1605 and 1606.
- **18: "twenty-seven years of rule"** — October 1412 to 1439 is twenty-six; **the toll as a
  grievance of 1426**, which I had kept while rewriting the sentence, three years before the toll is
  documented; §03's "immediately, why the towns went to war" with it; **Katarina "brought north with
  him"** — like him, not with him.
- **20: Ove Bille** — I had cut "three kings" to two; DBL has him chancellor to Hans and the leading
  statesman under Frederik 1. The page says that. **Tausen preached from 1525.**
- **Outside the diff:** 21 had the Norway clause in "the recess of 1536", and Ditmarschen six times.
  Both fixed (§11.2).

**Declined, with a reason:** that Margrete Sambiria's request was only nearly granted, as I first
wrote from DBL — the checker's lex, which names the surviving letter, is the better source, and DBL's
dissent is recorded (§11.4). **Also taken, from its minor list:** Krogen was walled about 1400 and
built up by Erik in the 1420s (Trap), not built by him; the gloss, §03 and the Myth-check say so.

**Verified** in a scratch clone: the five changed figure scripts, `build_part_d.py`,
`build_part_e.py`, `build_part_f.py` (no `!!`, no STALE), `linkindex`, `index_generator`, then the
suite: **debuild 45 identical; 45 of 45, 339,260 page words, 26.9 h (Part D 32,106, Part E 35,086,
Part F 29,497); vignettes 139/109, D-9 failures 16, 17, 18, 20, selftest passes; figcheck 98/30/0;
draftnotes clean; appcheck 159; freshcheck 14; tidy clean; seams pass; sweeps: 2 pointers solvent, 0
same-page glosses, Schleswig 178 / Slesvig 99, sweep_facts 5, arrows form 7, D-1 0, prose references
0, solvency 41.** One OVER, 16 §08, 852. mapfixture not re-run: no map script changed.

**11.8a. Found after the check, in a second pass (session restarted).** A second set of
fact-check agents, run over the unedited Part E, reported three things the patch had not settled:

- **18 §11: the buy-out.** The treaty, art. 4, gives **30,476,325 rigsdaler**, and danmarkshistorien's
  edition calls it fourteen years' income. The first pass had kept a secondary page's 33½ million and
  changed "fourteen" to "twelve" to fit it — the right figure made wrong to match the wrong one. Now
  "thirty and a half million … fourteen years' income". Item 144's lesson, a second time.
- **17 and 19, visit blocks: Christian 2. at Sønderborg "seventeen years".** 9 August 1532 (DBL) to February
  1549 (sonderborghistorier.dk; DBL gives the year only) is sixteen and a half (D-8): both now name the years, 1532 to 1549.
- **20 and the config: *Confessio Hafnica*.** lex's headword, and the standard name, is *Confessio
  Hafniensis*: four uses and one checkpoint.

### 11.9 Decisions for Carsten — Part E, one at a time

Each recommendation is a first search, not a text; its facts are checked again when it is carried out
(item 143).

**R-10. 16 has no woman as agent** — in the one chapter whose subject is a woman. *Recommendation:*
**Margrete at the Lund landsting, about 10 August 1387, 16 §04, `[f]`, by re-scoping the acclamation
paragraphs already there** (D-13, as R-8): a week after Oluf's death, taken and acclaimed
*fuldmægtig frue og husbond og det ganske rige Danmarks formynder* (Kvindebiografisk *Margrete 1.*),
the coup-or-crisis argument moving into the vignette's close. About 300 words. *Alternative:* her
letter of 7 December 1375 in §01 — the same D-13 re-scope, and thinner. (The Akershus letter is 15's
now.)

**Answered 23 September 2026: as recommended.** Margrete at the Lund landsting, about 10 August
1387, as 16 §04's `[f]` vignette, by re-scoping the acclamation paragraphs already there, to be
sourced, drafted and checked in review session 8.

**R-11. 16 has no non-elite subject.** *Recommendation:* **the Victual Brothers at Bergen, after
Easter 1393, 16 §06, `[n]`** — eighteen ships from Wismar and Rostock, a landing on Nordnes, a fight
with the townsmen at Vågsbunnen, the town plundered and burned (SNL *vitaliebrødrene*; Bergen
byleksikon; Icelandic annals). §06 gives the privateers one general sentence; this is the particular.
No leader is securely named. About 250 words. *Alternative:* the Käpplinge burning of Stockholm
burghers, 1389 — its date and even its reality are argued.

**Answered 23 September 2026: as recommended.** The Victual Brothers at Bergen, 1393, as 16 §06's
`[n]` vignette, to be sourced, drafted and checked in review session 8.

**R-12. 17 has no woman as agent.** *Recommendation:* **Margrete's gift letter, Kalundborg, 8 December
1411, 17 §05, `[f]`** — masses, 130 pilgrims to more than fifty shrines, and payment "til gengæld for
det, som er sket i krigen", including to women violated in her Swedish wars (danmarkshistorien, the
letter's text). §05's "gave land and money on a scale that shows plainly in the records" becomes the
pointer. About 300 words. *Alternative:* her instruction to Erik of 1405, in §02 (danmarkshistorien,
the text): 53 points, "du maa ikke gøre noget før jeg kommer" — but §02 already paraphrases it.

**Answered 23 September 2026: as recommended.** Margrete's gift letter of 8 December 1411 as 17 §05's
`[f]` vignette, to be sourced, drafted and checked in review session 8.

**R-13. 18 has no non-elite subject.** *Recommendation:* **re-scope the Reventlow vignette to the
peasants at Sankt Jørgensbjerg, June 1441, `[n]`** — the rising's subject was the peasantry, and the
mass grave excavated in 1964 and Huitfeldt's "600 … others say 1800" (Skalk) put them on the page;
Reventlow stays inside it. The May/June dating is checked first. *Alternative:* Bartholomeus Voet's
sack of Bergen, 1429 (Bergen byleksikon) — a hired pirate captain, whose own origins are
undocumented.

**Answered 23 September 2026: as recommended.** The Reventlow vignette in 18 §08 re-scoped to the
peasants at Sankt Jørgensbjerg, 1441, `[n]`, with Reventlow inside it and the May/June date checked
first, to be sourced, drafted and checked in review session 8.

**R-14. 20 has no woman as agent.** *Recommendation:* **Anne Meinstrup, Ringsted, 20 January 1535,
20 §06, `[f]`** — a woman who held Højstrup on Stevns as a royal fief from 1507, sided with Count
Christoffer against her own son, and was cut down at the Ringsted assembly by Copenhagen burgher
soldiers of the count's following (Kvindebiografisk *Anne Meinstrup*; lex). The vignette must show
her holding the fief and taking the side, not only her death. About 300 words. *Alternative:* Queen
Elisabeth, Christian 2.'s wife, taking communion in both kinds at Nürnberg in 1524 while pleading his
cause (Kvindebiografisk) — outside Denmark, inside the span.

**Answered 23 September 2026: as recommended.** Anne Meinstrup at Ringsted, 20 January 1535, as 20
§06's `[f]` vignette, showing her holding the fief and taking the side, to be sourced, drafted and
checked in review session 8. **All five are now answered.**

Until they are answered and carried out, `vignettes.py` reports 16, 17, 18 and 20 as D-9 failures,
and that is correct.

**Carried out in session 8 (§12.1): no D-9 failure in Parts A–E.**

## 12. Session 8 — Part E's missing vignettes, and Part F read (chapters 21–24)

*23–24 September 2026, from `START_HERE_review_8.md`.*

**The cold run matched every line.** A fresh clone of `0ea812a`: git status clean; tidy reports and
deletes nothing, 45 bodies; FIXTURE PASSES; SEAM LAYER PASSES; debuild 45 identical; 45 of 45,
339,260 page words, 26.9 h, parts A 21,397 · B 26,326 · C 26,228 · D 32,106 · E 35,086 · F 29,497 ·
I 74,403; vignettes 139/109, selftest passes, 01, 03, 04, 05 "[f] part", D-9 failures 16, 17, 18, 20;
figcheck 98/30/0; one OVER, 16 §08, 852; draftnotes clean in 45 pages and 14 drafts; appcheck 159;
freshcheck 14; 2 pointers, 0 insolvent, 0 same-page glosses; Schleswig 178 in 26 against Slesvig 99 in
9; sweep_facts 5; arrows 254, 37 thread notes, form 7, direction 0, D-1 0, titles 0, solvency 41, prose
references 0, footers 0, `<h1>` 0, 9b 0. **One difference, harmless, as in session 7:** item 145's
pages are in their own commit (`e3232f3`), not in `2a2ede4` with the sources; no drift.

Four research agents sourced R-10 to R-14; four fact-checked chapters 21–24, one each; a ninth, which
had not seen the work, checked every hunk (§12.8); a tenth made the first search for R-15 (§12.9).
The session saved its state to the project at each stage (`claude/session8_*`).

### 12.1 R-10 to R-14 carried out — and the recommendations' facts checked first

| the recommendation said | the sources say | ground |
|---|---|---|
| R-10: Lund "about 10 August 1387" | exactly 10 August, St Laurence's day, a Saturday, one week to the day after Oluf's death; in Lund cathedral and, the same day, at the landsting | danmarkshistorien, *Margretes valg til fuldmægtig frue, 10. august 1387* (DRB 4:3 nr. 322); DBL *Margrete 1.* |
| R-10: acclaimed by Skåne | the letter's first name is Vinald, archbishop of Trondheim; then the bishop of Aarhus, the drost Henning Podebusk, knights (Henrik Parow among them) and squires, "with many more … and common folk from all Denmark's lands"; in Danish, not Latin | the letter |
| R-10: (page) "not 'queen', which she never was in Denmark" | the letter styles her queen of Norway and Sweden; now "not 'queen of Denmark'" | the letter |
| R-10: coup or crisis | named: Christensen (DBL, "improviseret rigsmøde"), Dahlerup ("næsten kupagtig"), Hørby ("uden nogen hjemmel", yet unchallenged) | DBL; Gyldendal og Politikens |
| R-11: "No leader is securely named" | the annal names the commander, Enis, Albrecht's kinsman, and a second, Mækinborg, killed; Jon Darre, the king's treasurer, led the defence and was mortally wounded; the banner-bearer Henrik Aslaksson shot through the face; churches robbed; the anchor Langbein left; gone within eight days; parts of the town burned (SNL) | Icelandic annal (heimskringla extract); SNL *vitaliebrødrene*; Bergen byleksikon |
| R-11: "after Easter 1393" | landing 22 April 1393; the annal's arrival "in Easter week" is a variant reading, so the page says "in the spring … on 22 April they land" | annal; de.wikipedia (pointer) |
| R-11: (page) 16 §06 | Gotland taken in 1394 by a Mecklenburg captain with their help; Lindholm's core term a ransom of 60,000 marks, which the Albrecht vignette presupposed | SBL *Albrekt*; de.wikipedia (pointer) |
| R-12: "Margrete's gift letter" | five receipts, written by the recipients; her will is lost; about 2,356 kg of silver; about 130 pilgrims to more than fifty shrines; "til gengæld for det, som er sket i krigen" attaches to 5,000 marks east of the Sound; the women "krænkede og fornedrede øst for Øresund" — "voldtaget" is the editors' word; the dead "whether they were with the realm or against it" | danmarkshistorien, *Margrete 1.s testamentariske gaver 1411* |
| R-12: (page) 17 §05 | Lodehat "the executor of her will" (the will is lost; he administered the 1411 gift); "the abbey she had chosen" (not found; "Sorø"); *sjælegave* "the largest single transfer of land" (the gifts were silver) | DBL *Peder Jensen Lodehat* |
| R-13: "near Aalborg"; "May or 6 June" | Sankt Jørgensbjerg is in Han Herred, some forty kilometres west of Aalborg; the decisive fight is 6 or 8 June 1441 (Whitsun week), sources divided; the first, 3 May, killed Eske Brock; Skalk does not report two May engagements | DBL *Henrik Tagesen Reventlow*; Skalk 1967:5; Trap; Fabricius (HT 1899) |
| R-13: the dead and the grave | Huitfeldt: "Af den gemene mand blev slagen 600. Andre vil sige 1800"; the 1964 dig: a pit ten by six metres, scattered bone, "Ikke en knap, ikke et spænde"; executions at Aalborg 12 June, on the wheel | Skalk; DBL |
| R-13: (page) 18 §08 | *vendelboer* is Vendsyssel only; Christoffer born 1416 (22 or 23, not "twenty-two"); "About a week later" is 12 June; the Reventlow name is disputed (Hau 2016); his estates did not simply go "to the crown" | DBL; Hau |
| R-14: "held Højstrup as a royal fief from 1507" | by 1507, as a *pantelen* against a loan to King Hans; lost in 1518 after her peasants complained, regained after 1523; mistress of the household to three queens | Kvindebiografisk *Anne Meinstrup*; DBL |
| R-14: "sided with the count against her own son" | true of the sides; her son Holger fell at Svenstrup in October 1534, three months before Ringsted | DBL |
| R-14: her death | "hugget ned af kbh.ske borgersoldater i grevens følge" after "uforsigtige ord" against Christian 2.'s men; her granddaughters saved in the church tower; her killers excluded from the amnesty of 1536; gravestone at Hornslet | Kvindebiografisk; DBL; Gyldendal og Politikens |
| R-14: (page) 20 §06 | the Skåne nobility threw off the count in January 1535, not "meanwhile" after July | Gyldendal og Politikens |

**(a) 16 §04, Margrete at Lund, `[f]`, by re-scoping (D-13).** The acclamation paragraphs are now
the vignette; the body keeps one sentence and Norway's grant of 2 February 1388. Who-line *Margrete,
daughter of Valdemar 4. · Lund cathedral and landsting · 10 August 1387*. About 330 words.

**(b) 16 §06, the Victual Brothers at Bergen, `[n]`.** Between the privateers paragraph and
Lindholm. Who-line *The townsmen of Bergen, and the Victual Brothers' crews · Vågsbunnen, Bergen ·
22 April 1393*. The crews left no names; the page says so. About 280 words.

**(c) 17 §05, Kalundborg, `[f]`.** After the Lodehat paragraph; §05's "gave land and money on a
scale" is now the pointer. Who-line *Queen Margrete · Kalundborg · 8 December 1411*. About 300 words.

**(d) 18 §08, the peasants at Sankt Jørgensbjerg, `[n]`, by re-scoping (D-13).** The Reventlow
vignette is now the peasants', with Henrik Tagesen inside it; the political consequence moved into
the body. Recall, Contested and the visit block follow. Who-line *The peasants of the Jutland rising ·
Sankt Jørgensbjerg, Han Herred · June 1441*. No peasant is known by name; the page says so.

**(e) 20 §06, Anne Meinstrup, `[f]`.** At the head of §06, after a new paragraph that puts the Skåne
nobility's break in January 1535. Who-line *Anne Meinstrup, called fru Anne Holgers, holder of
Højstrup · Ringsted · 20 January 1535*. About 330 words.

`vignettes.py`: **no D-9 failure in Parts A–E.** 143 vignettes carry a place, 114 distinct.

### 12.2 Part F, read — errors of fact and of the book against itself, fixed

| ch | the page said | it is | ground |
|---|---|---|---|
| 21 §01, Five, → 22, 20 coda and → 21 | the crown's land "from roughly a sixth to roughly a half in a single autumn" | about a tenth to between two-fifths and a half — the bishops' estates at once, the monasteries' over decades | Den Store Danske *krongods* |
| 21 §01 | the 1536 charter "the most restrictive in Danish history and the longest-lived" | it laid *fewer* limits on the king than earlier ones and was the model for 1559, 1596 and 1648 | danmarkshistorien *Håndfæstning* |
| 21 §01 | the council "filling its own vacancies by nomination" (1536) | not found for 1536; cut | |
| 21 §01, Myth | "roughly two hundred *len*", the *tjenestelen* "the commonest form … for most of the century", "a fixed rent"; Oxe's conversions the cause | some sixty great fiefs and many small; accounting fiefs already three-quarters of the land by 1559 | Gyldendal og Politikens *Lensadministrationen* |
| 21 §02, checkpoint | Bugenhagen "in his first fortnight"; ordained "immediately afterwards"; the university reopened "on 2 September" | arrived 5 July; ordination 2 September, three weeks after the coronation; the university that autumn | DBL *Bugenhagen* |
| 21 §02 | Palladius "a Ribe weaver's son" | a Ribe burgher's son | DBL *Palladius* |
| 21 §03, glossary, Causal | Iceland: the Reformation "not by Danes"; Skriver killed "that spring"; "Nobody was ever punished"; "executed three men for [heresy]"; the encyclopedia "unfriendly" | Icelandic officials and Danish ships; killed early in 1551 at Kirkjuból on Reykjanes; the farmer and one of his men beheaded; a bishop and his sons, as outlaws; the encyclopedia calls him devoted to the Church | ferlir.is; Catholic Encyclopedia |
| 21 §04 | "two half-brothers"; Dithmarschen "settled by the same three men … in June 1559"; Rantzau "sixty-seven" | three (Frederik had bishoprics); Frederik 2. and his uncles Hans and Adolf, 22 May 1559; sixty-six | DBL *Adolf*; DBL *Johan Rantzau* |
| 21 §05, glossary | oxen "forty to fifty thousand", "by law a noble monopoly"; selvejere "perhaps a fifth" around 1500 | some forty thousand; landowners and merchants shared it, the 1550 law kept fattening for export to the manors; about a sixth c. 1536 | Den Store Danske *studehandel*; danmarkshistorien *Selvejerbønder* |
| 21 §06, Myth, Five | Oxe abroad "seventeen years" in five countries; quarrelled with "Frederik 2." in 1557; "eleven younger siblings"; the author of the 1567 reform; Christina "the surviving daughter"; a "rose noble"; the registers "continuous" from 1497 | about five years, four countries; Christian 3.; unsourced; tradition's attribution, which DBL finds no source for; the younger daughter; a noble; long runs after 1536 | DBL *Peder Oxe*; Den Store Danske *Sundtolden* |
| 21 §07 | Trolle "mortally wounded … off Mecklenburg"; Herlufsholm "for noble boys"; "Ivan 4." | wounded 4 June 1565 between Fehmarn and Mecklenburg, died three weeks later; noble and other honourable families' children; Ivan IV (D-14) | DBL *Herluf Trolle*, *Birgitte Gøye* |
| 21 §08 | "Dutch and Flemish architects"; Stjerneborg "beneath" Uraniborg; Tycho famous "four years earlier"; guns in 1658; a tenant imprisoned "and his family" | Flemish; just south, half underground; his book of 1573; both castles Swedish in 1658; a tenant of his Roskilde canonry, held on Hven six weeks (§12.9) | lex *Kronborg*; DBL *Tyge Brahe*; Dreyer 1890 |
| 21 vignette | Sophie Brahe: Tycho "seventeen years older", "the last thirteen months", "Uraniborg … three years", widowed "at twenty-nine", "told her not to take up astronomy" | nine or twelve; since the new star of November 1572; its foundation stone nearly three years off; widowed 1588; warned her off astrology, which she learned with Latin books translated | Kvindebiografisk *Sophie Brahe* |
| 21 §09 | heir "ten"; the four regents for eight years; "some thirty warships" | a week short of eleven (D-8); Kaas died 1594, Rosenkrantz led after; unsourced, cut | DBL |
| 21 visit | Ven "in summer"; Immervad a sixteenth-century bridge; Hólar's "sixteenth-century" church | all year; 1716/1786; the stone cathedral of 1763 | Trap *Immervad Bro* |
| 22 §01, Five, Recall, checkpoints | a son "of ten"; Sophie excluded "for being German and a woman"; "the council had Christian declared of age" in 1593; the 1596 charter added "one thing more"; she "thirty-six" | a week short of eleven; grounds unsourced, cut; the emperor, for the duchies; word for word his father's; thirty-six or thirty-seven | DBL *Christian 4.*, *Sophie*; Kvindebiografisk |
| 22 §02, §05 | Norway "seven times"; Bremerholm "the largest industrial establishment in the north", Kongsberg the largest in the northern kingdoms | probably some twenty-five visits, more than all other union kings together; unsourced superlatives cut | SNL *Christian 4* |
| 22 §03, figs_22 | Børsen 1619–24; toll "raised repeatedly" before 1625 | 1619–23, spire 1624–25; the steep rises are 1638–40 (chapter 23) | lex *Børsen*; DBL |
| 22 §04, fig. 1 | Christianstad "to replace two older towns he thought badly placed"; Oslo "for the fourteenth time"; Glückstadt "sixty kilometres"; the caption's fortress, mining and shipbuilding marks | a border fortress replacing Vä, burned 1612; "yet again"; fifty down the Elbe; the figure has none, cut | Britannica |
| 22 §06 | Gjedde "about three hundred men", "two years to Ceylon", "sixty men left"; → "chapter 27"; Munk "Jutland-born", "sixty-five" (×3), died "of wounds"; Dansborg "two hundred and twenty-five years" | about four hundred; a year and a half; unsourced, cut; chapter 30; born near Arendal, sixty-four, cause unknown; 1620 to 1845 (D-8) | danmarkshistorien; DBL *Jens Munk*, *Ove Giedde* |
| 22 §07, §09, Myth, Five, checkpoint, → 23 | 1611 "he declared war in his own name as duke … It did not"; "It worked twice"; "Charles 9."; Gustav Adolf "seventeen"; "fifteen years building a fleet"; Göteborg built "to trade without paying at Helsingør" | the council gave way to the *threat*, and Denmark declared war in April; carried out only in 1625; Karl 9.; sixteen; fourteen; Swedish ships were already exempt — a port no closure of the Sound could shut | danmarkshistorien *Christian 4.*; lex *Kalmarkrigen* |
| 22 §08, fig. 2, Five, sources | see §12.5 (D-13); the alt text "Fourteen were burned … sixteen women who died"; "Hans Bartskær accuses a neighbour, August 1612"; Kruckow "twenty-five years … two separate scandals"; "in four months"; Brunsmand "sixty years later" | generated from the data (thirteen; sixteen accused, one escaped); the Egøje women named her, winter 1611–12; twenty-four years, accusations of 1596–97 and 1611; under a year; 1674 | Køge Arkiverne (after Kjeldsen); DBL *Christence Kruckow* |
| 22 James, Henri, Meanwhile | "James 6.", "Henri 4."; Galileo "using the observational tradition Tycho Brahe had built" | James VI, Henri IV (D-14); Kepler's first two laws from Tycho's observations, 1609 | |
| 23 §02 heading, body, Five, config | Lutter "27 August 1626" | **17 August (27 August, new style)** — the only off-style date in Parts A–F; CONVENTIONS D-6's example corrected | de.wikipedia *Schlacht bei Lutter* |
| 23 §01, §02 | the German princes "chose Christian" as cheaper; the army "perhaps a fifth" Danish; Scots and English at Lutter; Tilly fighting "since 1618"; "a third to a half" lost; "his horse was shot under him"; "takes one paragraph" | England and the Dutch backed him as cheaper, the Circle elected him; unsourced, cut; they came after the battle; since 1620; a quarter to a third; he lost his horse and rode off on another's; cut | St Andrews SSNE; en/de.wikipedia (pointers); Gyldendal og Politikens |
| 23 §03, fig. 1 | "from the Kongeå to Skagen"; cattle trade broken "for a generation"; fig. 1: Scania never touched in either war | the Elbe to Skagen; cut; Horn took most of Skåne in 1644 | en.wikipedia *Torstenson War* (pointer) |
| 23 §04 | Lübeck's mildness Wallenstein's alone | and Ulvsbäck, February 1629 | lex *Kejserkrigen* |
| 23 §05, fig. 2, Myth, Five | Kirsten Munk "eighteen"; "twelve children. Then …"; sons-in-law "Ulfeldt, Sehested, Lindenov, Pentz, Rantzau" | seventeen; eleven, then the twelfth; Frands Rantzau was only betrothed and drowned in 1632 — the fifth is Hedevig's husband, Ebbe Ulfeldt | Kvindebiografisk *Kirsten Munk*; DBL *Frants Rantzau*, *Hedevig* |
| 23 vignette | Ellen Marsvin "the greatest landowner on Funen", "respected by the king … as a businesswoman", "raised the royal grandchildren herself"; Vibeke "nineteen years" | unsourced, cut; she was removed from Dorothea Elisabeth's upbringing; eighteen | Kvindebiografisk |
| 23 §06 | Rundetårn "an observatory on top of a church on top of a university library", "Tycho Brahe's instruments were meant for it" | library above the church's vault; meant to succeed Stjerneborg | lex *Rundetårn* |
| 23 §07, vignette | "the Dutch, who joined in"; "fifteen years"; "Femern"; Ewald "the same verse" | a fleet hired in the Netherlands by Louis de Geer; seventeen; Fehmarn (D-15); the same song | SNL *Hannibalfeiden*; lex |
| 23 §08 | Sehested "thirty-three"; "Swedish Jämtland"; "negotiated in Copenhagen" | 32 or 33; Västergötland and Värmland; at Brømsebro, by Danes | SNL |
| 23 §09, fig. 3 | Gotland Danish "since the fifteenth century"/"1449"; Jämtland "six hundred years"; "Four of the five losses are permanent" | 1361 (chapter 15's own date); nearly 470 years; all proved permanent | lex *Gotland*; SNL *Jämtland* |
| 23 §10, Meanwhile, vignette | "ruled for fifty-two years"; "a fortnight" in 1660; "Denmark's nobility hands its king absolute power"; Ulfeldt *and Kirsten Munk* sealed Vibeke's estates; Ulrik Christian a defender "in 1659"; her daughter "twenty-one" | king for nearly sixty years, fifty-one in his own right; a few weeks; the estates; Ulfeldt; died December 1658; twenty or twenty-one | DBL *Ulrik Christian Gyldenløve*; Kvindebiografisk *Vibeke Kruse* |
| 23 visit, Contested | "Sankt Paals Gade"; Boller "a private care home"; Tøjhusmuseet; "all three readings" | Sankt Pauls Gade; private; Krigsmuseet since 2018; two | |
| 24 standfirst, §03–§05, fig. 1, fig. 3, Five, Myth | "thirty-two months"; "seven hundred years"; the ice march "30 January to 8 February", Falster–Zealand "8 February", "six crossings in ten days", ice "for a fortnight"; "eighteen days"; "six months after Roskilde"; "Jutland Swedish for the third time"; "eight hundred kilometres in six weeks"; fig. 3 "Thirty-two months … less than three years … five weeks" | twenty months (the events it lists); as long as there had been a Denmark; Zealand reached **11 February**, Lolland–Falster 8 February, twelve days; unsourced, cut; about two weeks; less than six; occupied a third time, by Swedes a second; unsourced, cut; forty months, three years four months, four weeks | danmarkshistorien *Tabet af Skåne*; Populär Historia; Den Store Danske *Karl Gustav-krigene* |
| 24 §02, vignette | "eighteen months"; Dina "thirty", Gertzen her employer, she told Leonora Christina; executed "the seventh and the eleventh"; Ulfeldt left "a few days before"; party finished "within three years"; Ulfeldt to "the Netherlands, then … Karl 10. Gustav" | about half a year; about thirty, her stepfather, she told Ulfeldt; 11 July; three nights after; three and a half; he served Queen Christina first, Karl Gustav from 1657 | DBL *Dina Vinhofvers*, *Corfitz Ulfeldt* |
| 24 §05 | Skåne "a third of the realm's population"; "the archbishopric at Lund" | a third of the land (the Scanian lands); the old see | danmarkshistorien |
| 24 §06 | the storm "against the western wall", "the ditch … flooded and refrozen"; "lost every field engagement of both wars" | several points; the moats kept hacked free of ice; nearly every fight of the first war | en.wikipedia *Assault on Copenhagen* (pointer) |
| 24 §07, vignette | Trøndelag "in the autumn"; the Malmö oath "in front of Corfitz Ulfeldt"; Printzensköld "shot in the street by Villum Clausen"; the gift "on the condition … never again be pledged" | by December; unsourced, cut; taken prisoner, then shot — Villum Clausen in tradition, Villum Kelou in DBL; a deed of 29 December, as a hereditary possession — the condition unsourced, cut | DBL *Jens Kofoed*; Den Store Danske *Bornholms historie* |
| 24 §08, vignette | Dutch shipping "roughly half … passed the Sound"; "Obdam was killed later; Bjelke was in the line"; Nyborg's "imperial troops"; "five years"; Leonora Christina "watched him negotiate at Roskilde", "seventeen months", "four more years", "twenty-two years" | Dutch ships the greater part of the traffic; de With and Floriszoon killed, the Danish ships held in by the wind; unsourced, cut; four and a half; unsourced, cut; more than a year; Hammershus to the end of 1661; nearly twenty-two | en.wikipedia *Battle of the Sound* (pointer); DBL *Leonora Christina* |
| 24 §09 | Bornholm and Trøndelag simply "recovered" | Bornholm paid for with 912 farms in Skåne and Blekinge | danmarkshistorien *Tabet af Skåne* |
| 24 §10, Myth, Five, coda | tax exemption "held since 1536"; "within three weeks" (×3); "a hundred and twenty-four years"; "half the land"; "found one twice, in 1611 and 1625"; Lund archbishopric "five hundred years"; *Jammersminde* "decades later"; the Meanwhile's "chapter 27"; Aurangzeb | medieval, confirmed since 1536; about a month, with the gates shut; 1536 to 1660 (D-8); the church's land; threatened in 1611, worn in 1625; four hundred; some fifteen years; chapter 30; took the throne in 1658 | danmarkshistorien *Enevældens indførelse* |
| 19 → 24 | "Eleven wars follow between 1521 and 1814" | 1523: from 1521 the war of liberation makes twelve (eleven counts the Great Northern War as two and leaves out 1666) | en.wikipedia *List of wars between Denmark and Sweden* (pointer) |
| 20 → 21, coda, Myth, Five, fig. 3 caption | "half the land", "a third of the land", "a sixth to a half", "a hundred and twenty-four years"; pietism "in Part F" | between two-fifths and half; the church's land; the bars now called schematic, the prose at Den Store Danske's figures; until 1660; Part G | §11.4 |

**Sixty-six intervals and ages were wrong in Part F** (D-8, computed): 21 twelve, 22 fifteen, 23
sixteen, 24 twenty-three. Part C had nine, D sixteen, E thirty-four. The checker found five more in my
own fixes (§12.8).

**The 20 → 21 promise.** The Sound Dues and "no bishops in the council" are delivered (the council,
"with the bishops gone, was noble and only noble"); "half the land" is now "between two-fifths and
half" in both chapters; the fleet is thin in 21 — mentioned, never built — and is recorded (§12.4).
**The 19 → 24 promise.** Eleven is right from 1523, on the book's count (the Great Northern War as two
Danish wars, 1666 left out); 24 calls the Karl Gustav wars the fourth and fifth, as 21–23 number them.
19 said "1521" and now says 1523. **21 → 22** said "sixty years … the next chapter"; the reign is
nearly sixty and runs over two chapters, and 21 promised a council "that can stop him", which is
22's thesis reversed: now "a council whose consent he needs for anything the toll cannot pay for".
**22 → 23**'s Älvsborg promise was never picked up in 23; 24 §03 does, so the arrow is now → 24.

### 12.3 Part F — repetition and drag, fixed

- **22 §01 retold 21 §09** — the coronation, the charter, "the most expensive", the regents'
  surplus, the "advertisement". 22 now points back in two sentences.
- **23 §01 repeated 22 §09's council reasoning** near-verbatim. It points back.
- **22 §09 told the 1625 manoeuvre twice** in consecutive paragraphs. Once.
- **22's Glückstadt sentence** ("no charter could move it sixty kilometres") was in §04, fig. 1 and
  the Myth-check. The Myth-check points to §04.
- **22's Meanwhile repeated §01's Anne and James "against the council"**. Cut there.
- **21's Greenland** ("a claim and nothing more … nobody the crown could reach") was in fig. 1's
  caption and §03. §03 keeps the fact and points to the map.
- **21's Kronborg** "designed to be seen by someone who has just paid" was in §08 and the visit
  block. The visit block points back.
- **23's "Both halves are true, and neither is the whole story"** and **s02's "takes one paragraph,
  which is roughly the right proportion"**. Cut.
- **24's "ice for a fortnight"** four times, unsourced. Gone.
- **Recall** (content-word Jaccard ≥ 0.4 against the shipped checkpoints, measured on pages built in a
  scratch copy). Before: **21 1/6, 22 1/5, 23 2/5, 24 2/5**, no exact repeat. Six replaced with
  questions no checkpoint asks. After: **21 0/6, 22 0/5, 23 0/5, 24 1/5.**

**Found, kept.** 24's "Bornholm and Trøndelag took themselves back" in §07, §09, fig. 2, Five and
Recall, and "a third of the realm" throughout: the chapter's argument, restated by design in Five and
the Myth-check. 24's Part F coda re-runs 21–24 — it is the part's close, and the one place that does.
21's "revenue divided, not territory" in §04, fig. 2, Myth and Five, likewise.

### 12.4 Found, recorded, not changed

- **20's figure 3 bars** (crown 16 → 49 per cent) remain unsourced (§11.4). The caption now calls them
  schematic and gives Den Store Danske's figures; 20's prose follows Den Store Danske. **For the
  library (E-series): a sourced breakdown of Danish landholding c. 1525 and c. 1560.**
- **The Køge list.** Figure 2's sixteen names and dates match Olga Ravn's memorial list (Paris Review,
  2022) exactly; Køge Arkiverne, after Børge Kjeldsen (1995), counts fourteen burned and has Johanne
  sentenced on 24 August and burned on 11 September with her servant. The page and figure now say
  accounts differ. **For the library: the court record, or J.C.V. Johansen's count.**
- **21's fleet** — the → 21 promise's "a fleet" is mentioned in 21 and never built there.
- **21 is 48 minutes** (9,975 page words), inside the band, over the advisory. D-16: kept.
- **Maps keep Danish labels** (D-15): `map_1600` has Slesvig, Holsten, Ditmarsken, Øsel; figs_24 JYLLAND,
  FYN, SJÆLLAND.
- **Outside Part F, found by the checker:** chapter 30 (from `PART_G_DRAFT.md`) still has Trankebar
  held "two hundred and twenty-five years" (224 years 11 months: D-8, name the years) — for Part G's
  reading; `map_1500.py` and `map_1600.py` carry a comment "Danish since 1449" for Gotland (it does not
  print); `fixindex.py`, a spent one-off, still holds 23's old index summary (`index_generator.py`,
  which is live, is corrected).
- **"Two hundred and fifty families"** (21's standfirst, 24's coda) — not found in a reference work.
- **The Hven tenant** (§12.9) rests on Dreyer (1890), citing the judgment and the king's letter in
  *Danske Magazin*; the Danish text was not reached.

### 12.5 D-15, D-13, D-6 and D-14 in Part F

**D-15.** Part F has no Slesvig in prose; Dithmarschen is right (21's key *Ditmarsken 1559* is a
Danish term). The Skåne towns: Malmø and Helsingør in prose before 1658, Malmö only after; no Skåne town
in a Part F visit block before 1658 needed changing. "Scania" as a noun (21, twice; 23, once) is now
Skåne; the adjective "Scanian" stays, as in Part G. "Femern" is Fehmarn (23, three places).
Schleswig 178 / Slesvig 99.

**D-13. 22 §08, one of the seven cases (D-D), decided by re-scoping.** The vignette was the figure
written out as prose: every note in figure 2, the counts in the body a third time. Now the section is
*Witchcraft and the state* (config and page); the body carries the household, the Egøje hunt, the
figure, 1617 and Kruckow; the vignette is Johanne alone, from the quarrel to her burning; the figure
alone carries the list and the totals; the caption takes the "ordinary document" observation.
**20's Rantzau vignette** (out of order in §06, §11.5) is still there; 20 §06 now opens with Anne
Meinstrup in January 1535, which puts Rantzau's December 1534 second — recorded, not moved.

**D-6.** Every Part F date is Julian except one: Lutter, now 17 August 1626 (27 August, new style).
24 now gives the first divergence in parentheses (the Sound, 29 October 1658 — 8 November by the
Dutch reckoning). 21 and 22 have none to give.

**D-14.** James VI, Henri IV and Ivan IV for 22's and 21's non-Scandinavian rulers; Karl 9. and
Gustav 2. Adolf for 22's Swedes.

### 12.6 The padded-chapter guard, given to Part F

`build_part_f.py` had none, and no summary line. It now runs the same retired-vocabulary check as
parts A–E, prints "all four built clean" or "!! N problems", and exits non-zero on either a problem or
any failure its old checks counted. **It fired on the first real run, as Part E's had:** four ordinary
uses of "entry" — Munk's journal in 22 (twice) and a ledger in 23 (twice). A grep of the bodies had
told me there were none: the pattern needed forty characters before the word on the same line, and
the four sit near line starts. Item 142's lesson — find by hand the case a 0 should have caught — in
my own check of the guard. Those four phrases, and only they, are allowed (`ALLOWED_ENTRY`). **Tested
in a scratch copy:** "chapter\n07" and "this entry" planted in 22 and "The entries go on" in 23 gave
`STALE {'entry': 1, 'padded': 1}` and `STALE {'entry': 1}`, `!! 2 problems`, exit 1; the real bodies,
"vocabulary clean" four times. The checker planted "chapter\n07" in 21 and "chapters 5 and\n 07":
both caught.

### 12.7 D-9 in Part F — tagged

| ch | vignette | tag | why |
|---|---|---|---|
| 21 | Peder Palladius | `[-]` | a superintendent; the parish is any of four hundred |
| 21 | Þórunn Jónsdóttir | `[f]` | she holds land and debts and brings her dead home; her hand in the Kirkjuból killing is tradition, and the page says so — the weakest `[f]` in Part F |
| 21 | Sophie Brahe | `[f]` | |
| 22 | Sophie of Mecklenburg | `[f]` | |
| 22 | Jens Munk | `[-]` | a captain in royal service |
| 22 | Johanne Tommesis | `[n]` | a widow of a market town |
| 23 | Ellen Marsvin | `[f]` | |
| 23 | Christian 4. at Kolberger Heide | `[-]` | |
| 23 | Vibeke Kruse | `[n]` | a chambermaid |
| 24 | Dina Vinhofvers | `[f][n]` | a silk-ironer who made the accusation |
| 24 | Jens Kofoed | `[n]` | a farmer and militia captain |
| 24 | Leonora Christina | `[f]` | she conducted the defence at Malmö |

Who-lines trimmed to person · place · date · tag; what they carried besides is in the vignettes.
**D-9 failure: 21 (no `[n]`)** — true, not tagged away. §12.9 puts it to Carsten.

### 12.8 Checked by a separate agent

An agent that had not seen the work checked every hunk against sources and the rest of the book and
ran the guard. It found **twenty-two slips**, most of them mine, and three contradictions elsewhere.
All are resolved except the three recorded in §12.4:

- **Intervals in my fixes, again:** Sophie Brahe's brother famous "since the new star of last
  November" — written while removing "thirteen months", and wrong by a year; "two weeks after Easter"
  for the Victual Brothers' arrival (22 April is the landing); *Jammersminde* "some ten years later"
  (fifteen, from Malmö); Jämtland "some 450 years" (nearly 470); Christoffer "twenty-three" attached
  to the council's search of 1438 (now "born in 1416").
- **Facts in my fixes:** Frederik 2. and his *uncles* made "the next generation's three"; "Adolf, as
  the youngest of the three" two lines after Frederik was the youngest; the Icelandic "three men"
  beheaded just after the page added two more; the selvejere "holding a sliver of the land" (a misread
  of the 1688 figure); Louis de Geer "Dutch-born" (Liège); Huitfeldt "wrote in 1599" (Christoffer's
  reign is in the volume of 1603 — the year is dropped); Sophie Brahe teaching herself "from books in
  German and Latin" (she had the Latin translated); Henrik Tagesen "whom later genealogists made a
  Reventlow" (unsourced) and "land in Thy" (his seat was Bjørnholm); Anne Meinstrup's "unguarded"
  words were against Christian 2.'s men, and "the only noble there" is one account.
- **Prose:** 22 "That winter" with no winter named; the Egøje naming told in body and vignette (D-13
  again, in the re-scope); 23's Meanwhile left "occupation … they were … are"; 17 "one week" for a
  vignette of one day, and "So did many other houses" following nothing; Darre "wounded" (mortally).
- **Figures:** figs_24's shaded band drawn from month 7 to 8.7 while labelled four weeks (now
  7.97–8.87); figs_22's ledger alt text still said building "stops"; the Køge alt text printed "16".
- **Elsewhere:** 20 still said "a sixth to a half" in three places after its coda and arrow changed;
  `index_generator.py` still had 23's "Sixty years … undone in twenty" and "a Swedish army … twice";
  22's new checkpoint asked who governed until 1596, which 22 no longer says.

**Verified** in a scratch clone: the three changed figure scripts (rendered and looked at: Køge,
sons-in-law, forty months, the ice march, the foundations), `build_part_e.py`, `build_part_f.py` (no
`!!`, no STALE), `linkindex`, `index_generator`, then the suite: **debuild 45 identical; 45 of 45,
340,724 page words, 27.0 h (Part E 36,388, Part F 29,659); vignettes 143/114, D-9 failure 21 only,
selftest passes; figcheck 98/30/0; one OVER, 16 §08, 852; draftnotes clean; appcheck 159; freshcheck
14; tidy clean; seams pass; sweeps: 2 pointers solvent, 0 same-page glosses, Schleswig 178 / Slesvig
99, sweep_facts 5, arrows 254, form 7, D-1 0, titles 0, prose references 0, solvency 41.** mapfixture
not re-run: no map script changed.

### 12.9 Decisions for Carsten — Part F, one at a time

Each recommendation is a first search, not a text; its facts are checked again when it is carried out
(item 143).

**R-15. 21 has no non-elite subject.** *Recommendation:* **Rasmus Pedersen, a tenant of Tycho Brahe's
Roskilde canonry, 1590–92, 21 §08, `[n]`** — Tycho took his farm in October 1590, had him put in irons
and held on Hven "six weeks or more"; a court of four noblemen refused the eviction; the king's court
in July 1591 found six weeks' prison punishment enough and forbade the eviction from a farm whose lease
he had bought four years before and on which he had built a house; in November 1592 he complained that
he was still kept out and his brother and servant still held, and the king ordered the Zealand
*landsdommer* to settle it. Nothing more is known of him (Dreyer 1890, from *Danske Magazin* 4. rk.
IV). It sits where §08 now says "a documented case", and makes §05's "his lord was increasingly also
his judge" particular — the lord jailed him and the king's court still found for him. About 280 words.
The village and the Danish wording are to be found first (Kancelliets Brevbøger 1588–92; Thoren;
Christianson). *Alternative:* the peasants of Tuna on Hven and the commission of April 1597 — no one
named, and after the chapter's end.

**Answered 24 September 2026: as recommended.** Rasmus Pedersen, Tycho Brahe's tenant, 1590–92, as
21 §08's `[n]` vignette, replacing "a documented case", to be sourced, drafted and checked in review
session 9.

Until it is carried out, `vignettes.py` reports 21 as a D-9 failure, and that is correct.

## 13. Session 9 — 21's missing tenant, and Part G read (chapters 25–31)

*24–25 September 2026, from `START_HERE_review_9.md`.*

**The cold run matched every line.** A fresh clone of `af7352e`: git status clean; tidy reports and
deletes nothing, 45 bodies; FIXTURE PASSES; SEAM LAYER PASSES; debuild 45 identical; 45 of 45,
340,724 page words, 27.0 h, parts A 21,397 · B 26,326 · C 26,228 · D 32,106 · E 36,388 · F 29,659 ·
I 74,403; vignettes 143/114, selftest passes, 01, 03, 04, 05 "[f] part", D-9 failure 21, 25–31
untagged (32–45 tagged); figcheck 98/30/0; one OVER, 16 §08, 852; draftnotes clean in 45 pages and 14
drafts; appcheck 159; freshcheck 14; `build_part_f.py` "all four built clean"; 2 pointers, 0
insolvent, 0 same-page glosses; Schleswig 178 in 26 against Slesvig 99 in 9; sweep_facts 5; arrows
254, 37 thread notes, form 7, direction 0, D-1 0, titles 0, solvency 41, prose references 0, footers
0, `<h1>` 0, 9b 0. Item 146's pages and svg files are in its own commit (`765067b`), with the sources.

**The session ran twice.** The first run (24 September, evening) carried out R-15, read Part G with
one fact-checker and one fixer per chapter, and had its fixes checked by a separate agent; it was
lost before the handover. Its state, its work as a patch and the checker's report had been saved to
the project (`claude/session9_*`), as item 145's instruction asked. The second run (25 September)
cloned afresh, re-ran the cold run, applied the saved patch, found what the patch did not carry (an
`appcheck.py` change made after the last save), applied the checker's report, and had the result
checked by a second agent that had seen neither. Both reports are in §13.8.

### 13.1 R-15 carried out — and the recommendation's facts checked first

| the recommendation said | the sources say | ground |
|---|---|---|
| *Danske Magazin* "4. rk. IV" for the 1592 letter | **3. række** IV pp. 263–64; the 1591 judgment is in the first series, II (1746) pp. 271–79 | the volumes (archive.org); Dreyer's own footnote |
| "the king's court in July 1591 found six weeks' prison punishment enough and forbade the eviction" | that was the **four commissioners'** judgment, Copenhagen, 20 April 1591; the *retterting* of 10 July 1591 heard **Tycho's appeal against the four**, found they had done him no wrong and let their judgment stand in full | DM II pp. 273–78 |
| "a court of four noblemen refused the eviction" | Erik Valkendorf, Niels Parsberg, Christen Friis of Borreby, Oluf Bille; Friis became chancellor in 1596 and was given the Roskilde prebend after Tycho left | DM II p. 274; DBL *Christian Friis* |
| village to be found | **Gundsømagle**, Sømme herred: "Rassmus Pederssen vdi Gunssemagle"; a farm of the Hellig Tre Kongers prebend | DM 3.IV p. 263; Trap |
| "on which he had built a house" | a life lease Tycho himself granted, bought "for fire Aar siden" for 220 daler, and a house of forty bays (OCR) | DM II p. 275 |
| "put in irons … six weeks or more" | irons "ved hans Bord-Ende", carried to Hven, "6. Ugers Fongsel", as Tycho's punishment for Rasmus's refusal to appear; the four horses hauled on Hven about a month and two died | DM II pp. 274–76 |
| the bond | signed in prison; the commissioners freed him from it so far as it reached beyond the main case — the first draft had this backwards, as the bond's own words (§13.8) | DM II p. 276 |
| "in November 1592 … the king ordered the Zealand *landsdommer* to settle it" | a **draft** royal letter ("Concept"), repeating Rasmus's complaint that he still could not go onto his farm and that his brother and farmhand were held, and ordering the case before Lage Beck with other men | DM 3.IV pp. 263–64 |

**21 §08.** Sophie Brahe's vignette moved up to follow the Uraniborg paragraphs it belongs to;
"a documented case" became the pointer ("his quarrel with one of its tenants went as far as the
king's court") and the vignette follows it (D-13). Who-line *Rasmus Pedersen, tenant at Gundsømagle ·
Copenhagen Castle · 10 July 1591 · [n]*. The Sources carry the two volumes. About 420 words.
**`vignettes.py`: no D-9 failure in Parts A–F.**

### 13.2 Part G, read — errors of fact and of the book against itself, fixed

Seven fact-checks (one per chapter) and seven fixers; their full tables are in the project
(`claude/session9_factcheck_25..31.md`, `claude/session9_fixlogs.md`). The principal corrections:

| ch | the page said | it is | ground |
|---|---|---|---|
| 25 §01 | "half the kingdom in three weeks"; the Swedes "three miles away"; privileges "granted … that no Danish king had granted a town before"; the night of "10 February 1659" | a third of the realm; Karl Gustav on Valby Bakke; *promised* privileges on a footing with the nobility; 10–11 February (20–21, new style) — the part's first D-6 divergence | lex *Roskildefreden*, *Københavns belejring*; DBL *Nansen* |
| 25 §02–§03 | "four-fifths of the country", "half the land"; an unnamed councillor's retort; a 7 October stamp-paper refusal; Nansen "sixty-two", "mayor for sixteen years", defending the rampart | "most of the country"; Otte Krag and Nansen on 19 September; the stamp paper found nowhere, cut; sixty-one, mayor since 1644, senior since 1654, and in the siege a withdrawn role, so the rampart is cut (and 24's "organised the city's defence" with it) | GP *Uden stands forskel*; DBL *Nansen* |
| 25 §03 | **the Nansen vignette had never shipped**: it sat in a continuation segment's preamble, which mkbody drops | placed in §03; the guard that would have caught it is §13.6 | |
| 25 §03 | *håndfæstning* "since 1320", "at his election" (the fixer's) | before his coronation; three in the fourteenth century and every king from 1448 (Christian 4., chosen in 1580, signed in 1596) | lex *håndfæstning*; DBL *Christian 4.* |
| 25 §04 | Schumacher "thirty-one", "wrote out both fair copies"; the third restriction "the succession must run in his house"; seals "not attached until 1669" | thirty; the parchment is in his hand; he must keep the law as it stands; the Rigsarkiv copy probably written in 1669 and antedated; the succession clauses now said to fill much of the law | GP *Kongeloven*; Gottschalck, *Aigis*; lex *Kongeloven* |
| 25 §05–§09 | Kommercekollegiet 1668; Gabel "a mapmaker's son"; the land tax "on noble and peasant land alike"; "fourteen minutes past four"; "two originals read aloud"; "forty-four years" | 1670; a surveyor's son; tenant farms taxed, home farms exempt; cut; the reading of 1671 is 26's, and 25 points to it; not printed in Frederik 3.'s or his son's lifetime | lex; DBL *Gabel*; GP *Tronskifte* |
| 26 §01 | the Kongelov "on the altar … that almost nobody in the church had read" | read aloud "fra begyndelsen til enden … lydeligen for alle" before the anointing; he crowned himself before entering the church | GP *Tronskifte* |
| 26 §03 | Griffenfeld chancellor "in June 1674"; "four years in Kastellet … eighteen more"; Karen Nansen "died in childbirth" | the sources split (November 1673 or 1674), both given; Kastellet to 1680, Munkholmen to 1698; the cause is not in DBL | DBL *Griffenfeld*, *Reedtz* |
| 26 §06 | Møn "1 June … eight ships lost"; Juel's orders "not to engage before Tromp arrived"; Køge Bugt 29 June; "destroyed" Horn's fleet; statue "Kongens Nytorv", "1878" | the end of May, Sjöblad's surrender; not to engage a superior enemy; 1 July, the Swedes sighted 30 June; seven of the largest ships taken; Holmens Kanal, **unveiled 1881** (the second checker) | DBL *Juel*; lex *Køge Bugt*; Trap *Niels Juel-statuen* |
| 26 §08–§09 | seven thousand Scanian conscripts, a *uniformitetsinspektör*, fifteen thousand fled; Leonora Christina "not once outside"; released "on a petition written in verse" | cut or softened (no reference work has them); cut; after Sophie Amalie's death, with Louis XIV and Gyldenløve interceding, 19 May 1685; Otto Sperling, tried and condemned, now beside her | DBL; Kvindebiografisk; DLH *Jammers Minde* |
| 27 §01–§03 | Frederik 4. "twenty-eight"; "out in three months"; Karl 12. "did not come back for nine years"; "a few hundred" escaped Poltava; Rantzau "the Danish commander"; Sweden "reverted in 1712 … eleven days"; horses killed "on the beach" | twenty-seven; one campaign; Denmark stayed out nine years; a few thousand; Reventlow was ill and the army Rantzau's; Sweden one day ahead of Julian 1700–12, ten days from Gregorian; in Helsingborg | DBL; DSD *Poltava*, *Hestemassakren* |
| 27 §04–§05 | the plague "a fifth to two fifths", population "sixty or sixty-nine thousand"; Marie Grubbe "about sixty", husband "in prison for manslaughter"; Tordenskjold "a tailor's son", "tenth of eighteen"; Dynekilen "ended the invasion" | from a third to over forty per cent of about sixty thousand; about sixty-eight, her husband awaiting the courts for a killing that May; a merchant's son, fourteenth; Karl 12. was already preparing to go and went the next day | danmarkshistorien; DBL *Marie Grubbe*, *Tordenskiold*; SNL |
| 27 §07–§09 | "formally renounced" Skåne; the peace date; *vornedskab* "the burghers' programme of 1660" and "women as well"; "Krieger and a brickworks owner put up 149"; Egede "since 1711"; Visit "Kangeq" | no renunciation clause — not recovered; §13.5; unsourced, cut, and Møn's went in 1696; Lars Eriksen built more than half, Krieger possibly the designer; since 1710; Illuerunnerit, Egede's Håbets Ø | danmarkshistorien *Frederiksborgfreden*; lex *vornedskab*; Historiske Huse; navn.ku.dk |
| 28 §01, §09 | "a king who closed the theatres"; the playhouse "burned in 1728" | it kept the theatre shut; Grønnegade was undamaged and did not play again | Teaterleksikon |
| 28 §03–§05 | the *lægd* "twenty barrels"; *vornedskab* "women as well"; hoveri "two days in seven", Antvorskov 122 days; rinderpest "two million", "95 per cent" | one man per sixty (1733), forty (1741); men only; the 110-day reckoning labelled untraced and figure 1 schematic; more than a million across the century, most of the cattle it reached | G&P (Feldbæk); lex *kvægpest* |
| 28 §08 | the 1728 fire "28 per cent" of the town; Árni's collection in the Trinitatis loft; "both Fagrskinna manuscripts in his collection" | two in five by the old count; the university library was in the loft, Árni's in his house, and he saved most of the oldest vellums; Kringla lost bar a leaf | lex *Københavns brande*; arnastofnun; handritinheima |
| 29 §01–§02 | Christian 7. "seventeen"; Struensee "thirty-one", met on the tour; council dissolved "in the autumn"; "never held an office" | 29 January 1749 to 14 January 1766, dates named (D-8); thirty, engaged at Altona in April 1768; December 1770; cabinet minister July 1771 | DBL *Struensee*, *Christian 7.* |
| 29 §02 | Struensee "considered abolishing stavnsbånd"; hoveri ordinance "20 January 1771" | unsourced, cut; the 1769 returns, the agrarian commission and the ordinance of **20 February 1771** (danmarkshistorien prints the document; DBL says 20.1 — the document wins) | danmarkshistorien *Hoveri* |
| 29 §07–§09 | the 1788 ordinance "at once back to fourteen-to-thirty-six"; walk-out "the day after the king signed"; the column "a subscription of 1791", stone "on his wedding day" | boys three months, the over-age and discharged at once, the rest by birth-year to 1 January 1800; Schack-Rathlou on 6 June, a fortnight before; a collection among Copenhagen's citizens, stone on 31 July 1792, the second anniversary of the wedding | danmarkshistorien (ordinance §§1–4); DBL *Schack-Rathlou*; dengang.dk |
| 30 §01, §03 | Christiansborg "taken in 1661"; "all voyages began and ended in Copenhagen"; 100,000–111,000 carried; "seventh largest" | Carolusborg 1658, Frederiksborg 1659, Christiansborg bought 1661; most voyages; about 111,000; the smallest of the seven national carriers SlaveVoyages distinguishes, and a carrier in its own right (the first fix, "one of only seven", was false: Brandenburg and Sweden carried too) | duda.dk; danmarkshistorien *Den danske slavehandel*; SlaveVoyages |
| 30 §04–§10 | Kønig captain of the crossing; mortality "one in five"; "the harshest slave code in Danish history"; "the Crown bought out the company, from 1754"; "waived the import duty on women"; Schimmelmann "presided over the bankruptcy" | Kønig died on the Gold Coast, Ferentz commanded; one in six to one in five; cut; bought out 1754, crown rule from 1755; the head tax; finance minister of the 1813 reform, and dismissed after it | KUBEN; danmarkshistorien *VGK*, *Forordning om negerhandelen* |
| 31 §03–§08 | "near the northern end" for the Willemoes battery; seventeen ships of the line and 79 hulls taken; the Rahbeks "had to leave" Bakkehuset; "Friday 2 September"; Bourke "sixty-three … forty years" | between *Sjælland* and *Dannebrog*; 45 hulls and 92 merchantmen of stores; unsourced, cut; Wednesday; fifty-two, twenty-four years | DBL *Willemoes*, *Bourke*; milhist *Flådens ran* |
| 31 §04, §07 | the grain monopoly as the famine's cause; Schimmelmann and Reventlow "out of office" | the ban went in 1788, the dependence did not; both dismissed, both keeping a council seat | lex *kornmonopolet*; DBL |
| 24 (for 25–26) | *Jammersminde*; *stænderforsamling*; the council "voted itself out of existence"; "twenty-one months"; "nearly twenty-two years" | *Jammers Minde*; *stændermøde* (and 32's back-reference); gave way and surrendered the charter; the peace of May 1660 and 1663 to 1685 named (D-8) | DBL; GP |

**Ninety-five intervals and ages were wrong in Part G** (D-8, computed, by the fixers' counts): 25
seventeen, 26 seventeen, 27 sixteen, 28 eight, 29 fourteen, 30 fourteen, 31 nine. Part C had nine, D
sixteen, E thirty-four, F sixty-six. The first checker found four more in the fixes (a "twenty-one
months" within a fortnight of twenty-two, Maria Theresa's "eight years", Christian 7.'s "sixteen" a
fortnight from seventeen, Hans Knudsen "sixty-five or more"), and the second found my repair of
Christian 7.'s age restating an interval where D-8 asks for the dates. I wrote one more myself — "three
months before" for 15 June to 5 September — and caught it before the build.

**The promises into Part G.** **24 → 25** (the estates of 1660, the hereditary crown, the Kongelov of
1665) is delivered in 25 §02–§04; 24's own §10 retells the assembly briefly, which 25's Myth-check
takes further — kept, as 24's close. **24 → 26** (Leonora Christina and *Jammers Minde*) is delivered
in 26 §09, and the two chapters now agree on 1663 to 1685 and on the spelling. **24 → 26, 27** (the
snaphane war and the last attempt on Skåne) is delivered in 26 §07–§08 and 27 §02–§03. **21 → 27**
(the Gottorp question to 1720–21) is delivered in 27 §01, §06 and §07. Inside the part: 26 → 27 lost
"Griffenfeld is on Munkholmen until 1698" (27 has nothing to hang it on); 27 → 30 (the Moravians) was
insolvent and is gone, the Greenland rivalry now in 27 §09's body; 28 → 31 lost Wergeland (31 does not
carry him); 28 → 29 and 28 §04 now match 29 on hoveri (fixed 1771, unlimited again 1773, rules 1799);
30 → 31 and 31 ← 30 now agree that Schimmelmann was dismissed after the 1813 reform, not that he
"presided over a bankruptcy" 31 says was not one.

### 13.3 Part G — repetition and drag, fixed

- **25's 8 October** was told six times (body, glossary, Myth-check, Summary, a question and the
  unshipped vignette); now once, in the vignette, with pointers.
- **The 1671 reading of the Kongelov** was told in full in both 25 and 26; now in 26 §01, and 25 points.
- **27's plague toll, Tordenskjold and Egede**; **29's aftermath of 1788** (told about ten times; now in
  §09 and the Summary); **30's 2.3 per cent and rank** (six times); **31's Bourke myth** (three times) and
  Willemoes's death (twice): each now told once, pointers elsewhere.
- **26's Svend Poulsen Myth-check** précised the §07 vignette (the first checker); now "the §07 vignette
  gives the record". **30's "filed the proposal"**, three times in five paragraphs; once.
- **27 §08 and 28 §03** made the same *vornedskab*/*stavnsbånd* comparison; 28 keeps it.
- **Recall** (content-word Jaccard ≥ 0.4 against the shipped checkpoints, measured on built pages).
  Before: **25 1/4, 29 1/4, 31 1/4** (31 2/4 after the fixers, whose new checkpoint question on what
  the British took in 1807 matched Recall 3); the rest 0/4. Four replaced with questions no checkpoint
  asks (Gersdorff and Roskilde; who paid for the Liberty Column and when its stone was laid; what
  Floating Battery No. 1 was; the two death tolls of 1807). After: **0/4 in all seven.**

**Found, kept.** Saltholm and the forty days (27; event, term, sequence, place); "Lund decided the land,
Køge Bugt the sea" (26, the argument); the Guldberg "same instrument" irony (29); the school series from
1721 to 1814 (27, 28, 31, the part's thread); 31's coda, the part's close.

### 13.4 Found, recorded, not changed

- **21 is now 50 minutes** (10,491 page words) with the Rasmus Pedersen vignette — inside the band, at
  its top. D-16: kept; anything added to 21 later must be paid for inside it.
- **28 is 44 minutes**, as before; D-16, kept.
- **The per-chapter fragment files** (`c25_draft_01-03.md` … `c31_draft_apparatus.md`) are read by no
  build and by no check now that `appcheck.py` reads `PART_G_DRAFT.md`. They have drifted. Candidates for
  deletion — Carsten's call, since two generations of one file is how this project has lost work.
- **Maps keep Danish labels** (D-15): `map_1721` has "Slesvig: wholly the king's, 1721" in its legend.
- **Not verified, kept hedged or as they were:** Frederik Rostgaard as the 1709 edition's editor (25);
  the 1747 Funen tax relief (28, local chronicle only); Hans Knudsen's age (29, from a parish history);
  the Stadsarkiv plague anecdotes (27); the Kiel art. 27 dating (27, marked in Sources); DLH's 18 against
  DBL's 19 May 1685 for the release (26); the Asiatic Company's cargoes "roughly equal to the entire state
  revenue" (31 §01, probably Feldbæk — **for the library**); the rytterskole schoolmasters (27, no life
  found).
- **`build_part_h.py` has no retired-vocabulary guard** and no summary line either. For Part H's reading.
- **The same Band/Era/padded regexes** as Part G's first version are in `build_parts_abc.py`,
  `build_part_d.py`, `build_part_e.py` and `build_part_f.py`, with the gaps §13.6 closed in Part G.
  They pass on their real pages; they should get Part G's text normalisation when next opened.
- **24 → 25** still calls 1660 "the most complete absolutism in Europe"; 25 no longer says so. An arrow's
  superlative, recorded.

### 13.5 D-15, D-13, D-6 and D-14 in Part G

**D-15.** Every Slesvig in Part G prose is Schleswig (26, 27, 29, 31; figure texts and captions too);
Tönning, Glücksburg; Christiania on the maps of 1660, 1721 and 1814 (Oslo was renamed in 1624). The
Skåne towns are Swedish after 1658 and "Scanian" is the adjective. **Schleswig 212 in 29 chapters,
Slesvig 65 in 4 (32–34, 36), none in Part G.**

**D-13 — the four Part G cases of the seven, decided by re-scoping.** **26 §09** is now *The state's
prisoners*: the body argues the Blue Tower as state prison (Griffenfeld and Otto Sperling had courts;
Leonora Christina never did); the vignette, in 1674, is her writing. **27 §05** is *The war at sea*:
the body says why Tordenskjold is remembered; the vignette is Dynekilen. **27 §09** is *The Greenland
mission*: the body keeps the petitions, the backing and the Moravian rivalry; the landing, the children
and the fourteen years are Gertrud Rask's. **29 §03** is *The court under Struensee* (and §04 *The fall,
1772–75*): the body is the regime as a household; the vignette is Caroline Mathilde's summer of 1771.
Also re-scoped: 30 §05 *The Akwamu rising on St Jan, 1733–34* and 31 §08 *Norway ceded*, both named for
their vignettes' moments. **With 42 §03 (Part I) and 22 §08 (Part F), six of the seven are decided;
35 §03 waits for Part H.**

**D-6.** The part's first divergence is 25 §01's assault on Copenhagen (10–11 February 1659, 20–21 new
style). Each chapter gives its own first: 26 Vienna, 2 September 1683 (12 September, new style); 27
Travendal, 18 August 1700 (8 August, Swedish style); 31 Tsar Paul's murder (23–24 March 1801, 11–12
Russian style); 25's Meanwhile gives Mazarin in Danish style (27 February 1661). 28–30 have no divergent
day date. **One exception kept:** 27 §07 gives Stockholm as 14 June (3 June, Swedish style) although it
is not the chapter's first divergence, because the argument about the Frederiksborg date needs the
Swedish date on the page. **The Frederiksborg peace (E4)** is given as 3 July 1720, ratified 23 July,
with Schou's 3 June and the English reference works' 3 July Julian (14 July) both stated; HANDOFF E4 is
updated.

**D-14.** Louis XIV, Charles II and George III; Christian 5., Karl 12., Gustav 4. Adolf; no numerals for
the tsars.

### 13.6 The padded-chapter guard, given to Part G — and what else the build could not see

`build_part_g.py` had no retired-vocabulary check and no summary line. It now has both, and exits
non-zero on a problem. **Before trusting its clean first run, every "entry" in 25–31 was found by hand**
— on the built pages, figure text and attributes included, whitespace joined and case ignored: two,
both in 25's figure 3 about a register ("not a transcription of one entry", "the seven entries are
added"), plus the JavaScript's `entries`. Those two phrases are `ALLOWED_ENTRY`.

The first checker found the guard matched markup rather than text, and three more places where the Part
G build could not see what it lost. The second checker, given the repairs, found five more. All closed,
each **planted in a scratch copy and shown firing**, and the real pages built clean afterwards:

| hole | now |
|---|---|
| prose in a segment's preamble is dropped silently — **chapter 25's Nansen vignette (258 words) never shipped, and chapter 30's "note on language" (70 words, in the apparatus preamble) never shipped either**; the second was found by hand while writing this guard | `mkbody.preamble_leftover()` checks every segment (first, continuation, apparatus): the `# Chapter` line must carry HAND's title and dates only; italic `*Draft`/`*Notes` headers up to 60 words; the file's own head likewise. The note on language is now in 30's Sources |
| a second `# Chapter NN — apparatus` segment replaced the first | refused |
| a Summary of fewer than five items printed `!!` and exited 0 | exits |
| `appcheck.py` read `cNN_draft_apparatus.md` files no build reads (six false shortfalls), then — in the first run's repair — mkbody's own reader | reads `PART_G_DRAFT.md` itself, every apparatus segment, never falls back; reports unknown headings, and known headings used twice (a `## Visit` renamed `## Sources` dropped the whole Visit list) |
| when mkbody refused, the part build went on from the old body and said "built clean"; the first repair asked only after writing the page | `freshcheck.check(n)` runs **before** each page is built; a stale body is "NOT BUILT"; `freshcheck.py` now covers 25–31, preferring `PART_G_DRAFT.md` (a stray `c27_draft.md` had become the witness) |
| the vocabulary check read raw HTML: `chapter&#160;07`, `Chapter <i>07</i>`, "chapters 5, 6, and 07", `ch. 07`, `Era&#8209;page`, `Band&#160;C`, `entr&shy;y` all passed | it reads the text: tags dropped (aria-label, alt, title kept), entities decoded, dashes, spaces and soft hyphens folded; an allow-listed phrase no longer on the page is itself reported |

**Known limits, by design:** up to 60 words of italic `*Draft` notes pass; an HTML comment in the
concatenation-marker shape is stripped wherever it is. Parts H and I (32–45) build unchanged.

### 13.7 D-9 in Part G — tagged

| ch | vignette | tag | why |
|---|---|---|---|
| 25 | Joachim Gersdorff | `[-]` | *rigshofmester* |
| 25 | Hans Nansen | `[-]` | senior mayor, a rich merchant |
| 25 | the Amager farmers | `[n]` | |
| 26 | Peder Schumacher | `[-]` | at the top of the state |
| 26 | Svend Poulsen | `[n]` | a border fighter who lost his farm to arrears; a major's commission makes it weaker than a peasant |
| 26 | Leonora Christina | `[f]` | the writer |
| 27 | Marie Grubbe | `[f]` | born high; not tagged `[n]`, which would be tagging to pass |
| 27 | Tordenskjold | `[-]` | |
| 27 | Gertrud Rask | `[f]` | |
| 28 | Sophie Magdalene | `[f]` | founder of Vallø |
| 28 | Anders Pedersen | `[n]` | a farmer |
| 28 | Christian 6. on the Dovre road | `[-]` | |
| 29 | Caroline Mathilde | `[f]` | |
| 29 | Struensee | `[-]` | |
| 29 | Hans Knudsen | `[n]` | a tenant farmer |
| 30 | Christian Runge | `[n]` | a sailor, third mate and steward |
| 30 | Breffu | `[f][n]` | |
| 30 | H.C. Schimmelmann | `[-]` | |
| 31 | Peter Willemoes | `[-]` | a naval officer |
| 31 | Kamma Rahbek | `[f]` | |
| 31 | Edmund Bourke | `[-]` | |

**D-9 failures: 25 (no `[f]`), 27 (no `[n]`), 31 (no `[n]`)** — true, not tagged away. 25's and 31's
are the two CONVENTIONS D-9 names as found by hand at drafting; they are still there. §13.9 puts all
three to Carsten.

### 13.8 Checked by separate agents

**First checker** (first run; the fixers' hunks): **some seventy slips in Part G's fixes (79 rows, a few
of them one slip seen from two chapters), eleven holes in the tooling, eight slips in 21's vignette and
five in 24 and elsewhere**, among them *håndfæstning* "at his election" (a correct phrase made wrong), a Recall question
the page no longer answered, 27's back-pointers to a vornedskab claim 25 had cut and to a succession
clause 25 no longer carried, Gersdorff called a commoner in 26, the D-13 repeats left in 26 §09 and 27 §09,
Dynekilen "ended" the invasion, "between a third and two fifths" against the page's own 41.7 per cent, the
1799 "cap" 29 does not describe, the Kurantbank "destroyed" by a bankruptcy 31 denies, "seventh largest"
meaning seventh of seven, the 1682 survey against 26's 1681, a "wedding day" two years after the wedding,
the discharged men missing from the 1788 release, and 28's and 30's built bodies stale in the commit; in
21, the case reversed in the Sources, "the man he is appealing against", the letter a draft, the order of
irons and seizure asserted. All applied in the second run.

**Second checker** (second run; the repairs): **fifteen slips and five tooling holes** — among them
**my "one of only seven" carrier nations, which was false**; Schack-Rathlou's walk-out dated after the
king signed when DBL has it two weeks before; the Rasmus bond's wording invented from the judgment's
limit on it, and the irons' cause; Gersdorff compensated before the compensation; the Juel statue's
1878 (unveiled 1881); an arrow left half insolvent by a deletion; "freed again" for hoveri made unlimited;
a "because" that turned an observation into a cause. All applied (§13.6 for the tooling).

**Verified** in the working clone after every fix: figs 25–31, maps 1660/1721/1814, mkbody 25–32, build
F, G and H (no `!!`, no STALE), `linkindex`, `index_generator`, then the suite: **debuild 45 identical; 45
of 45, 340,840 page words, 27.1 h (Part F 30,153, Part G 52,644, Part H 41,195); vignettes 145/114, D-9
failures 25, 27, 31, selftest passes; figcheck 98/30/0; one OVER, 16 §08, 852; draftnotes clean in 45
pages and 14 drafts; appcheck 167 blocks in 21 chapters; freshcheck 21 fresh (25–45); tidy clean; seams
pass; sweeps: 2 pointers solvent, 0 same-page glosses, Schleswig 212 / Slesvig 65, sweep_facts 5, arrows
253 (27 → 30 dropped), 37 thread notes, form 7, D-1 0, titles 0, prose references 0, solvency 40.**
mapfixture not re-run: map scripts changed only labels and comments; seams pass.

### 13.9 Decisions for Carsten — Part G, one at a time

Each recommendation is a first search, not a text; its facts are checked again when it is carried out
(item 143). Research in `claude/session9_research_R16.md`, `_R17.md`, `_R18.md`.

**R-16. 25 has no woman as agent.** *Recommendation:* **Charlotte Amalie of Hesse-Kassel · Nykøbing
Slot, Falster · 25 June 1667 · `[f]`, in 25 §08 *A church of royal officers*.** The crown prince's bride,
seventeen, refused to become a Lutheran; the Hessian side made her free Reformed worship a condition,
and Denmark gave way reluctantly — her own chaplain, her household and their families, but no baptisms
or weddings; she had learned Danish before she came. Kvindebiografisk: this cost her the clergy's
goodwill, which "probably" explains the modest wedding at Nykøbing and her not being anointed with
Christian 5. in 1671. It makes §08's state church particular from inside the royal house, and links to
26 §01's anointing. About 280 words. *Alternative:* Sophie Amalie at the window during the execution of
Kaj Lykke's effigy on the castle square, 5 September 1661 (the new Højesteret's first great case) — a
strong scene, but her agency is "seems to have pressed" (DBL) and it risks the malicious-queen picture
26 takes apart.

**R-17. 27 has no non-elite subject.** *Recommendation:* **Kari Rasmusdatter Hiran, cottar's wife ·
Nordkleiva, Krokskogen (Ringerike) · April 1716 · `[f][n]`, in 27 §05, re-scoped as *Norway, and the war at
sea*.** After the skirmish at Nordkleiva on 16 April 1716 she went to the Swedish post at Jonsrud, was
seized and questioned, and told them more than a thousand Norwegian peasants and soldiers held the pass;
Karl 12. gave up the attempt there. We have only her word, in her petition of 1717 for a reward (two
rigsdaler); the page would say so, and keep the 1905 rediscovery apart from the record. It gives Norway,
half the monarchy, a person in a chapter that has it only as a coastline, and the body gains three
general sentences on the invasion of 1716 (Christiania taken, Akershus and the Gjellebekk line held, the
levies called out) before Dynekilen. About 300 words (SNL *Kari Hiran*; SNL on the invasion of 1716).
*Alternative:* the brewer Poul Olsen of Helsingør, who buried his wife and seven children between 25 July
and 20 August 1711 (27 §04) — powerful, but from one newspaper feature, to be checked against Frandsen
(2010) first.

**R-18. 31 has no non-elite subject.** *Recommendation:* **Hans Andersen, shoemaker · Odense ·
1812–January 1813 · `[n]`, in 31 §07 *5 January 1813*.** A *friskomager* who in 1812 was paid to enlist
as a musketeer in place of a farmer's son — the sum "presumably about 1,000 rigsdaler" (the H.C. Andersen
Centre; to be confirmed before drafting, and kept hedged) — and saw it written down to a sixth by the
ordinance of 5 January 1813; his regiment got no further than Holstein, and he came home sick in January
1814. It is §07's "a wage earner's savings" as one man's price for his body, and it adds the substitute
system the section does not mention. His son is one line. *Alternative:* the three Jutland brothers of
*Prins Christian Frederik*, the hulk *Bahama* at Chatham, 1808–10 (31 §06) — the stronger story and a
real gap (the prison hulks), but the brothers' names are in a 1963 *Fra Holbæk Amt* article no one has
yet read.

**R-16 answered 25 September 2026: as recommended.** Charlotte Amalie at Nykøbing Slot, 25 June 1667,
as 25 §08's `[f]` vignette, to be sourced, drafted and checked in review session 10.

**R-17 answered 25 September 2026: as recommended.** Kari Rasmusdatter Hiran at Nordkleiva,
Krokskogen, April 1716, as 27 §05's `[f][n]` vignette, §05 re-scoped as *Norway, and the war at sea*,
to be sourced, drafted and checked in review session 10.

**R-18 answered 25 September 2026: as recommended.** Hans Andersen, shoemaker, Odense, 1812 to January
1813, as 31 §07's `[n]` vignette, to be sourced, drafted and checked in review session 10.

Until they are carried out, `vignettes.py` reports 25, 27 and 31 as D-9 failures, and that is correct.

**Carried out in review session 10** (§14.1): no D-9 failure in the book.

## 14. Session 10 — Part G's last three vignettes, and Part H read (chapters 32–36)

*25 September 2026, from `START_HERE_review_10.md`.*

**The cold run matched every line** on a fresh clone of `f856117`: git status clean; tidy clean, 45 bodies; FIXTURE PASSES; SEAM LAYER PASSES; debuild
45 identical; 45 of 45, 340,840 page words, 27.1 h; vignettes 145/114, D-9 failures 25, 27, 31;
figcheck 98/30/0; one OVER, 16 §08, 852; draftnotes clean; appcheck 167 in 21 chapters; freshcheck
21; F and G "built clean"; 2 pointers, 0 same-page glosses; Schleswig 212 in 29 against Slesvig 65
in 4; sweep_facts 5; arrows 253, form 7, D-1 0, solvency 40. Item 147's pages are in its own commit.

**The session ran in four stretches, and lived in its saves.** Run 1 carried out R-16 to R-18, read
Part H with one fact-checker and fixer per chapter (`claude/session10_factcheck_32..36.md`), and had
the work checked by a separate agent (`claude/session10_checker_report.md`). Run 2 applied that report
with six fixers (`claude/session10_run2_fixlog_*.md`), made the shared-file edits itself and wrote
`pageguard.py`; Carsten stopped it to split the usage. Part A had two new agents check run 2's repairs
(`claude/session10_check2_A.md`, `_B.md`) and applied what they found. Part B — this write-up — made
one verification run and no edits to the book. Each stretch began from a fresh clone and the last
saved patch (`claude/session10_wip.patch`), never from memory.

**Verified, part B**, on a fresh clone of `f856117` with the final patch, `cairosvg` installed, DK_*
unset: figs 32–36 and map_1864; mkbody 25–31 and 32–36; build G "figures: 21 checked against their
scripts, all fresh", "all seven built clean"; build H "figures: 15 … all fresh", "all five built
clean"; no `!!`; `linkindex`, `index_generator`; then the whole suite, **mapfixture included**:

- **tidy:** no collisions, orphans or missing figures; 45 bodies; nothing deleted.
- **mapfixture:** every map's curated mainland and panel cases all correct (14 lines); coverage and
  seams hold; no unclaimed land, no overlap; **FIXTURE PASSES**. **seamcheck:** SEAM LAYER PASSES.
- **debuild:** 45 identical.
- **bookstats:** 45 of 45, **344,488 page words, 27.3 h.** A 21,397 · B 26,326 · C 26,228 · D 32,106 ·
  E 36,388 · F 30,153 · **G 54,165** · **H 43,322** · I 74,403. 21 is 50 minutes; 33 is 44.
- **vignettes:** **148 carry a place, 116 distinct**; selftest passes; 01, 03, 04, 05 "[f] part";
  **no D-9 failure.**
- **figcheck:** 98 match, 30 sourceless, 0 disagree.
- **narrative:** one OVER, 16 §08 *Kalmar, 17 June*, 852 (D-16, kept); 32 §09 749, heavy.
- **draftnotes:** none in 45 pages, none in 14 drafts. **appcheck:** 167 blocks in 21 chapters.
  **freshcheck:** 21 fresh (25–45).
- **build_part_f:** "all four built clean". **build_part_g:** as above.
- **sweep_glossary:** 2 pointer entries, 0 insolvent; 0 same-page double glosses.
- **sweep_names:** **Schleswig 297 in 31 chapters, Slesvig 2 in 2** (32, 33: both Danish titles in
  Sources).
- **sweep_facts:** section 5 lists **6** (was 5). The new row pairs 36 §09's 114 Folketing seats
  (1895) with 39's 149 (1929): different years, a false pairing.
- **sweep_arrows:** 253 arrows, 37 thread notes; form 7, direction 0, D-1 0, quoted titles 0,
  solvency 40, prose references 0, footers 0, `<h1>` 0, 9b 0.
- **git status** after the builds: the 16 sources, their bodies, the 13 regenerated `svg_*.txt`, and
  pages 25, 27, 29, 31 and 32–36. 26, 28, 30 and the index rebuild byte-identical.

### 14.1 R-16 to R-18 carried out — and the recommendations' facts checked first

| the recommendation said | the sources say | ground |
|---|---|---|
| R-16: Hesse "made her free Reformed worship a condition … her own chaplain, her household and their families" | Hesse demanded worship for her **and her household**, with a chaplain and a place; **the families were in what Denmark granted**, hesitantly; the chaplain could not baptise or marry | DBL (Laursen): "ikke alene for sig selv, men også for sine betjente" / "hendes hofbetjente og deres familier"; Kvindebiografisk (Hein): "Tøvende" |
| R-16: "she had learned Danish before she came" | a **wish** the Danish side expressed in the negotiations, which she met; German stayed her daily language — not a bargain ("in return" was cut) | DBL: "udtalt ønske"; Hein: "hendes daglige sprog forblev tysk" |
| R-16: the clergy's ill will "probably" explains the modest wedding and no anointing in 1671 | as recommended; the page keeps "probably" and says whose word it is | Hein: "Det forklarer formentlig …" |
| R-16: seventeen, Nykøbing Slot, 25 June 1667 | right (born 27 April 1650) | DBL |
| R-17: Kari "went to the Swedish post at Jonsrud … Karl 12. gave up the attempt there" on her word | sent by Captain de Coucheron "a few days" after the skirmish; seized at a tarn, taken to Bærums Verk and questioned by a general; the Swedes gave up **on reports** that the pass was reinforced — hers was one; whether it decided it, nobody can say | SNL *Kari Hiran*; SNL *Den svenske invasjonen av Norge i 1716* |
| R-17: "her petition of 1717" (the page first said *she wrote it*) | May 1717, in a clear, practised hand — **someone probably wrote and signed it for her**; the fogd who endorsed it is unnamed (not "the same Lars Michelsen") | SNL: "har fått noen til å skrive og undertegne dokumentet for seg"; "Fogden bekreftet" |
| R-17: two rigsdaler | from the deputy viceroy Frederik Krag, **for her and her husband**, beyond the three years' tax relief everyone war-damaged got | SNL |
| R-17: the body's new sentences on 1716 | Christiania taken, Akershus held; the Gjellebekk line; **the Norderhov raid of late March**, which the first draft's "again" presupposed and did not tell; Moss; Fredriksten above **Fredrikshald, now Halden** | SNL *Den svenske invasjonen* |
| START_HERE_review_10: "Norway Gregorian, **Sweden one day ahead of Julian in 1716**" | **false.** Sweden ran its own calendar, one day ahead of the Julian, from 1700 to 1712, and was **Julian from 1712 to 1753**. In 1716 Sweden was eleven days behind Norway. SNL's 16 April is Gregorian — 5 April in the Swedish style — as its campaign dates show against the Swedish accounts (Fredriksten: night to 4 July; the Swedes' 22 June). The page's own glossary (27 §03) had it right | PART_G_DRAFT 27 *gammel og ny stil*; aksf.se; SNL |
| R-18: "the sum 'presumably about 1,000 rigsdaler'" | the H.C. Andersen Centre's "antagelig … ca. 1.000 rdl" for what he received; Petterson (Museum Odense) supposes **the farmer paid** 1,000–1,300 to be let off; neither says where its figure comes from. Levnedsbogen and Topsøe-Jensen not consulted — the page says the sum is not known exactly | Andersen Centre, *1812*; museumodense.dk |
| R-18: "his regiment got no further than Holstein" (the draft: "peace came before it fought") | Andersen wrote that the regiment got no further than Holstein before peace; DBL (Topsøe-Jensen) that he never fought; **Petterson thinks it likely that he did**, while granting it cannot be settled. The page gives the dispute | *Mit Livs Eventyr* ch. 1; DBL; Petterson |
| R-18: (the draft) the money "meant to see his wife and son through"; his son "remembered his mother walking beside the company" | invented purpose, cut; Andersen's own motive given ("in the hope of coming home a lieutenant"). The son **lay sick with measles and heard the drums** as his mother followed his father out of the town gate | *Mit Livs Eventyr* ch. 1 |
| R-18: 1 June 1812, a farmer's son | from Måle on Hindsholm; born 14 September 1782, so "about thirty" (29 y 8 m) | Petterson; DBL |

**25 §08, 27 §05, 31 §07.** Who-lines *Charlotte Amalie of Hesse-Kassel, crown princess · Nykøbing
Slot, Falster · 25 June 1667 · [f]*; *Kari Rasmusdatter Hiran, cottar's wife · Nordkleiva and
Jonsrud, Krokskogen · April 1716 · [f][n]*; *Hans Andersen, shoemaker · Odense · 1812 to January 1813
· [n]*. 27 §05 is *Norway, and the war at sea* (build_part_g.py follows); its body points to Kari
("what happened there is in the first vignette below") and does not tell the skirmish or her errand
(D-13). His son is one line. **`vignettes.py`: no D-9 failure in the book.**

### 14.2 Part H, read — errors of fact and of the book against itself, fixed

Five fact-checks and fixers (run 1); the checker's report applied by six fixers (run 2); two more
checkers on the repairs (part A). The principal corrections:

| ch | the page said | it is | ground |
|---|---|---|---|
| 32 §01–§02 | the 1815 treaty signed "by Prussia, Sweden and Denmark"; Pomerania "four hundred kilometres" away; "2.6 million daler in cash"; "the state had **defaulted** on 5 January 1813" (and "insolvent" four times) | Denmark and Prussia only; across the water, never handed over; a sum of money, two million thaler by one Swedish account; the paper money written down to a sixth (chapter 31: not a bankruptcy) | runeberg *Sverige på kongressen i Wien*; de.wikipedia; PART_G 31 §07 |
| 32 §02 | grain "a fifth", property "a third or a quarter"; estates "taken for unpaid tax"; Torstedlund "112,250 → 12,050" | a quarter to a third by 1822–25; 53 estates the state had lent to since 1818; 1817 was 112,250 in silver **and 35,000 in notes** — the figure's 11 is silver to silver, "the real fall was steeper" | GP vol. 10 |
| 32 §03–§04 | lay preachers "the class that owned between nothing and forty acres … hostile sources … irritation"; Grundtvig "42", "September", "thirty pages in two or three days", "the Exchange emptied", "humiliated daily for eleven years"; resigned "on 8 May, after an earlier ruling" | craftsmen and cottagers above all, and women came forward; August 1825, an early copy, a few days, out 5 September; a letter of the time; "a hundred rigsbankdaler, which his friends paid"; what censorship cost him was **delay**, and one work seized; resigned in May **with the case still pending** and his hymns banned from the Ansgar jubilee | GP; KB tekstportal; Grundtvigsk Forum; DBL |
| 32 §05–§06 | Thorvaldsen "stayed forty years"; Heiberg's mother "from outside Copenhagen"; eligibility "thirty-five"; "clergymen could not be elected"; "one Dane in forty … the broadest franchise on the continent"; Jews "could vote but not be elected" | reached Rome 1797, home 1819–20, back for good 1838; from round Frankfurt; thirty; the clergy, **the teachers of the grammar schools and the university and the higher officials** without land had no vote or seat by right; 32,000, just under three in a hundred; **in the kingdom** Jews could vote, in the duchies not at all | DBL; Indenrigsministeriet; Tønnesen; GP *Fra reskript til forordning* |
| 32 §07–§09 | the kornsalgsperiode "to the late 1850s"; Bondevennerne founded "by tenants"; their programme "a constitution" and "better terms for tenants"; the 1840 rescript binding "every official"; the Hiort Lorenzen vignette's king "turning him down" in 1842; *Dannevirke* subscriptions; the Slesvigske Forening banned; 1844 "twelve thousand" | mid-1840s to late 1870s; liberals and peasant leaders; six points, **cottagers**, no constitution; officials who knew enough Danish from 1 January, a report on the rest; the rescript of 2 December 1842 upheld the Danish speakers — the grounds belonged to the 1844 patent, which the body tells; cut (not found); cut (not found); nine or ten thousand | GP; DH (text of the rescript; the Stændertidende extract); DBL; Grænseforeningen; Trap |
| 32 Visit, Meanwhile | Skamlingsbanke column "blown up in 1844"; the statue "by Haderslev Dam"; Peel "fell within weeks" | obelisk to eighteen civilian champions, 1863, blown up by Prussian engineers 21 March 1864, re-erected 1866; the former højskolehjem's garden (now Hotel Norden); resigned four days after 25 June | Trap; Grænseforeningen; DBL |
| 33 §01–§03 | "sat up in bed"; Louise Charlotte "dead in 1824"; the March ministry with Scheel-Plessen and without Hvidt, Lehmann, Zahrtmann; Rendsburg "an hour or so later … fire bell … largest garrison"; absolutism "ended in a week" | blood poisoning after a bloodletting; **born 1789**, alive in 1848; Moltke (finance minister since 1831) and Bardenfleth kept on, Knuth, Bluhme, Zahrtmann, Monrad, Hvidt, Lehmann, Tscherning; the 7 a.m. train, the church bells, the garrison assembled unarmed, without bloodshed; in two days | danmarkshistorien; lex *Martsministeriet*; DBL |
| 33 §04 | Bov "a sixth taken"; Wrangel "32,000 and 74 guns"; the Danes "went back to Als"; Nybøl and Dybbøl Danish victories; **1849 absent** | 923 of 6,150; one reckoning of about 27,000; fell back north; a bridgehead won and held; Eckernförde, Kolding lost, Fredericia's sortie, the second armistice — 34's Ilia Fibiger vignette's "in the war of the previous chapter" now has something to point to | milhist.dk; Grænseforeningen; lex *de slesvigske krige* |
| 33 §05–§07 | Cohen "a bookseller … first history of the Jews … his son continued"; Fibiger's "120 rigsdaler … twenty"; "enters the language"; "the first free election"; a 1853 commission "reported eleven years later" | catechist to the Jews of Funen and Lolland-Falster; half of the fee (DBL); cut; the first Folketing election; drafts in 1853–54 and five times since, none law | DBL; Kvindebiografisk; lex *folkekirken*; Rigsarkivet |
| 33 §08–§10 | Isted "on Danish ground", "from two in the morning"; "Frederiksstad"; London Protocol "signed by Prussia and Austria because Russia required it"; the 1851–52 promise "that Schleswig would not be bound more closely than Holstein … the public was not told"; the Lion to Berlin "two years later" | the largest battle in Danish history; first shots early on the 24th, the main battle from the night; Friedrichstadt; Britain, Russia, France, Sweden-Norway, Austria later, **Prussia not**; a promise **not to incorporate Schleswig**, made in notes **beside** the treaty, of doubtful legal standing; taken down February 1864, set up in Berlin 1868 | danmarkshistorien; lex *Londonprotokollen*; *Kongelig erklæring 28. januar 1852* |
| 34 §01–§03 | Augustenborg "a government in exile at Gotha"; the constitution "broke the Treaty of London" (Summary, hook, question); the Dannevirke "thirty kilometres, twice the army"; the instruction "of 22 January"; de Meza "dismissed within days … a language teacher … his clothes" | proclaimed himself from Gotha, came to Kiel 30 December; broke **the promise made beside the treaty**; needed at least fifty thousand, held by under forty; 13 January (both dates in Sources); the war minister called him to Copenhagen on 6 February, and on 28 February the king agreed to remove him from the high command | DBL; G&P; danmarkshistorien; Grænseforeningen |
| 34 §04 | Kjeldsen "twenty-three", "the first issue of *Vort Forsvar*", the painting down "1912"; "four thousand shells on 11 April"; **the casualty paragraph** ("official return 379 killed … German accounts 3,600 killed") | twenty-four; an article of 1881; 1913; on 8 April the Broager batteries alone fired 1,150 rounds, perhaps 200–300 on the town (from a **letter** of Sønderborg's mayor to his wife, not a diary); four reference sets, each with what it counts — the "3,600 killed" is a misreading of a total, the 379/646 traced to no return | DBL; Housted (1864.dk); Natmus; Grænseforeningen; Naturstyrelsen |
| 34 §05–§09 | the conference "two days after Dybbøl"; "the war's only fleet action"; "the blockade held"; "Britain proposed arbitration"; "said at the table"; Monrad's half-and-half "who had just resigned"; Estrup "one of the twelve royal seats … with one interruption" | 25 April, a week after; the larger of two (Jasmund); a tactical and moral victory that changed nothing; **the neutral powers**; most historians think it likely; dismissed in July 1864; elected for the 9th district 1864 and 1866, royal appointee from 1900 | Hansard 27 June 1864; milhist.dk; lex; DBL |
| 35 §03 | **Hjedding's contract gave "one vote regardless of cows"**; the general meeting "the highest authority"; "twenty-six farmers"; "more than a thousand within twenty years" | **§12 counts votes by cows: "eller 1 Stemme for hver Ko"**; one member one vote was the movement's principle, and the encyclopaedias credit Hjedding with it — the page gives both and follows the document; "highest authority" is the encyclopaedia's, and said so; the number dropped; 244 in 1888, 907 in 1894, 1,168 by 1914 | the contract (danmarkshistorien, from *Mælkeritidende* 1902); lex; Trap |
| 35 §05–§06 | Indre Mission "founded by a blacksmith"; 1861 "renamed"; Beck "ten thousand … a survival of absolutism"; "309,000 emigrants 1868–1900" | a lay association of 1853 at Stenlille, Jens Larsen one of its founders; at the meeting of 13 September 1861 the priests captured it and a new association was formed with a self-filling board; cut; more than 172,000 before 1900, nine in ten to the United States | DBL; lex; Beck (1901); Gyldendal |
| 35 §08–§10 | the International "banned in 1872 as high treason"; the lockout "four months"; the September Compromise "still in force", "the oldest in the world"; Olivia Nielsen born 1854, a "bottle-washer"; associations "dissolved in series"; "ten thousand children" given a nationality in 1907 | leaders convicted of high treason in 1873; the International dissolved 14 August 1873; more than three months; revised in 1960, its principles still frame the labour market; 1852, probably a washerwoman; declared political and their meetings broken up (DBL Köller); most of about ten thousand stateless covered in 1907, **the *hjemløse* left out until 1916**; Jyske Lov in Schleswig until 1900 | DBL; danmarkshistorien; FAOS; KVINFO; dengang.dk; Grænseforeningen |
| 36 §02–§05 | §25 used "exactly once … a gap of weeks"; Estrup "a Zealand landowner … tubercular all his life"; the 1877 law "followed shortly by a proper one"; Pontoppidan "four months … a priest"; Brønderslev "sabres … meetings banned across Vendsyssel" | for money once before Estrup (1853: §30 of the 1849 text), a stopgap to 31 August at the latest; born at Sorø, Skaføgård; tuberculosis from his mid-teens; rejected 7 November, a temporary law of the 8th; a højskole principal, three months; the gendarmes in the inn, the town under siege two days later, twenty-eight tried | Himmelstrup (1948); DBL; Nordjyske |
| 36 §06–§10, coda | the Vestvold "designed by Sommerfeldt … known abroad"; fifty thousand "to hold it … four years"; the Reform party formed before 9 April 1895; Christensen "a schoolmaster six years earlier"; Hørup's appointment; "settles" Article 80; a silence "neither side had noticed"; "two-fifths of the territory"; "defaulted" | built under Sommerfeldt's directorate from 1886, 13.2 million kroner by Bahnson's figures; a security force called up to the whole fortress, scaled down from 1915 and gone in 1919; formed "during April", the page says "that month"; still at Stadil; Christensen gave way to a threat; a step towards what chapter 33 left open; "neither side had thought about" (§02's own words); the duchies, all three; written down its money | DBL; vestvolden.info; lex; danmarkshistorien |
| map_1864 | aria-label and legend: "since the fourteenth century", "Slesvig, Holsten, Lauenborg", "Ribe Herred … came north", "eight parishes" | since the Middle Ages; Schleswig, Holstein, Lauenburg (legend "Lauenborg (Lauenburg)", to match the Danish label on the map); the enclaves ceded all but Ribe Herred, which stayed; **a string** of border parishes south of Kolding (lex says seven, Grænseforeningen eight) | lex *Wienerfreden*; Grænseforeningen |

**Ninety-three intervals and ages were wrong in Part H** (D-8, computed, by the fact-checkers'
counts): **32 nineteen, 33 twenty-four, 34 twenty-three, 35 thirteen, 36 fourteen**, and four more went
with claims that were cut. Part C had nine, D sixteen, E thirty-four, F sixty-six, G ninety-five. The
first checker found five more in the fixes (34's "within a week" where the dates were known, 18 → 25
April; 35's "within a year" for 1875 → 1876; 36's "two days before" the session — 3 October 1884 was a
Friday and the session opened on Monday the 6th; "when he was fifteen" for "fra det 15. år"; and a
hook's "nineteen years … on emergency decrees", which were nine); the second checker one more exposed
by a fix (31 §10's "the same summer" it gave up a kingdom, after the section now dates Kiel to 14
January) and a false sequence ("within months" read after the verdict of 31 May 1831, when the
ordinances were of the 28th).

**The promises into Part H.** 31 → Part H's "German-speaking share … rising sharply" was, on the
only figures found, the duchies' share of the population; 31 now says two in five of the king's
subjects and points to 33's 1848 numbers. 31 → Part H (the Schleswig question from 1721) and 27 →
Part H (the Kongelov's female line in Schleswig) are delivered in 33 §02. 29 → Part H (the tie to the
home district until 1848–49) is delivered in 33 §05, once now. 26 → 35 (Jyske Lov in Sønderjylland
until 1900) was insolvent and is now in 35 §10. 34 → 35's "war debt" and "the heath" were insolvent
and are gone from 34 (35's own ← 34 still names the heath: §14.4). 32 ← 31 now says what 32 opens on.

### 14.3 Part H — repetition and drag, fixed

- **32:** the 1844 patent (vignette and body), Grundtvig's censorship (§04 and Myth-check), the
  Golden Age names (§05 and Myth-check) — each once now. **32 §09 trimmed** of three things it said
  twice (Nis Lorenzen's motion restating the rescript; "nearly half voted against"; an unsourced
  causal sentence on the crowds): 797 → 749 words. That was repetition, and D-16 allows it; nothing was
  cut for time.
- **33:** Frankfurt's powerlessness (§04 and Meanwhile); §06's closing line retelling the Fibiger
  vignette; the 1788 tie and the 1849 freedom to move, each twice in §05.
- **34:** the Myth-check retold §03 almost line for line; now a paragraph and a pointer. The Isted
  Lion is 33's; 34 points.
- **35:** the four Hjedding rules (vignette, figure, checkpoint, Summary) — body once and the figure;
  §09's party paragraph (36 §08 is its home); Askov three times; the war dead twice.
- **36:** the German model (§05 and Meanwhile); §07 restating §05's laws; the Alberti story and the
  1903 school law, which are 37's (pointers now); the coda's echo of 34 §09's close.
- **Recall** (content-word Jaccard ≥ 0.4 against the shipped checkpoints, on the built pages, with
  `claude/session10_recall.py`, which reproduces §13.3's Part G result of 0/4 in all seven — its
  calibration). **Before: 33 1/3, 34 1/3**, the rest 0/3. The fact-checkers had found more by eye, at
  a looser standard — all three of 34's and 36's, two of 33's and 35's, one of 32's — and replaced them. **After: 0/3 in
  all five**, re-measured in part B on the final build: 25–31 0/4, 32–36 0/3.

**Found, kept.** The 1851–52 promise in 33 (§09, §10, glossary, Myth-check, Summary, → 34), each place
doing a different job; the 1866 Landsting composition in 34 §09 (how it was made) and 36 §01 (why it
deadlocked); the Vestvold's end in 36 §06, because checkpoint 3.1 asks it before §10.

### 14.4 Found, recorded, not changed

**For Part I (START_HERE_review_11):**
- **37's "the 'universal suffrage' of chapter 33"** — 33 never uses the phrase (it says "universal
  conscription" and gives 15 per cent).
- **"Nordslesvig" in English prose:** 37 three times, 38 fifteen — North Schleswig under D-15;
  *Vælgerforeningen for Nordslesvig* and similar names stay Danish.
- **37 §01: "the parish council law of 1903 put local government on an elected footing."** The
  councils of 1903 were *menighedsråd*, church councils (36 §10 has them right; Kirkehistoriske
  Samlinger; lex *menighedsråd*).
- **37 §05: "Her association outlived her by twenty-four years and won."** 10 September 1891 to 5 June
  1915 is 23 years 9 months (D-8: name the years), and Kvindevalgretsforeningen was dissolved in 1898.
- **45: the poor's vote "in 1961"** (three places) against danmarkshistorien *De 7 F'er*'s 1933. 33 no
  longer names any year after 1915, so the book does not yet contradict itself; 45 has to be sourced.
- **38: "around thirty-five thousand men from Nordslesvig called up"** (twice) against Grænseforeningen's
  30,000 and 37's thirty thousand; 38's "more than six thousand did not come back" against about 5,300.
  35 now says "more than five thousand", which agrees with both of 38's death counts.

**Also found, not changed:**
- **The 1900 US census.** 35 gives danmarkshistorien's 159,000 born in Denmark, as "more than a
  hundred and fifty thousand"; a checker recalled about 153,700 from the census table, which could not be
  reached. The page's bound holds on either, and its Sources say the table was not checked. For the
  library.
- **Figure 32 §2's seat counts**, Schleswig 44 and Holstein 48, against da.wikipedia's 43 and 47. Neither
  checked against the decrees; the figure keeps its own caveat. For the library.
- **36's `qs[3]` duplicates checkpoint 3.2** (the attempt on Estrup: why did it help him?), and 36 asks
  the January 1886 rejection three times (Causal 1, `qs[1]`, checkpoint 2.2) and the treasury twice; 35's
  checkpoint 1.3 and Causal 2 share an answer. All predate the session. Whether a WHAT-THIS-PAGE-ANSWERS
  question may preview a checkpoint is a book-wide rule, so it goes to review 11 to be measured across
  the book, as Recall was — not patched page by page.
- **Run 1's 33 agent reported "Frederiksstad" three times in Part G**, for D-15 (Friedrichstadt).
  **False**: all three are in chapter 28 and are *Frederiksstaden* (PART_G_DRAFT 2859, 3056, 3148
  now), the Copenhagen quarter laid out from 1749, whose Danish name is right. 33's own
  "Frederiksstad" was the Schleswig town, and is Friedrichstadt.
- **Danevirke / Dannevirke.** The earthwork is *Danevirke* in 7–13, 19 and 38 and *Dannevirke* in 33
  and 34 (a section title in 34). D-15's English-exonym clause gives Danevirke; 32's *Dannevirke* is the
  newspaper and stays. For review 11, with `build_part_h.py`'s section title.
- **Unverified and hedged or kept:** Rendsburg's force (two sources differ; the page says "the Kiel
  garrison and armed volunteers"); the Isted wounded; Cohen's totals; the first election's figures; the
  provisional finance laws' wording; the Venstrereformparti's founding day in April 1895 against the
  poll on the 9th; which chamber rejected the 1877 law.
- **35's ← 34 promises "the heath"**, which nothing in 35 carries (34's → 35 dropped it in this
  session). Drop the two words when 35 is next opened.
- **`map_1864.py`'s docstring** still has Danish forms and "Nørre Tyrstrup Herred" in comments. Off
  the page.

### 14.5 D-15, D-13, D-6 and D-14 in Part H

**D-15.** Every Slesvig in Part H's prose, figure text, captions and questions is Schleswig; Nordslesvig
is North Schleswig (35's §10 title and its build anchors follow); Flensborg is Flensburg; the Slien is the
Schlei in 33 and 34; Frederiksstad is Friedrichstadt; Mysunde is Missunde. Danish names stay Danish:
*Slumrer sødt i Slesvigs Jord*, *Flensborg Gamle Kirkegård*, *Vælgerforening for Nordslesvig*.
**Schleswig 297 in 31 chapters, Slesvig 2 in 2** — both Danish titles in Sources: *Tidende for
forhandlingerne ved provindsialstænderne for Hertugdømmet Slesvig* (32) and Koch's *Udkast til et
Sprog-Kort over Hertugdømmet Slesvig eller Sønderjylland* (33). No Slesvig is left in the book's
English. The maps keep their Danish labels; `map_1864`'s aria-label and legend, which a reader hears or
reads as prose, are English.

**D-13 — 35 §03 decided by re-scoping, so all seven are decided.** The section *Hjedding, 1882* told the
founding, and the vignette told it again from inside while holding the rules the body then commented
on. It is now ***The cooperative dairy***: the body carries why joint dairies had failed (Kaslunde), a
member's four obligations, the vote, the liability, the women's lost trade and the spread; the vignette
carries Uhd, the unnamed young man, the statutes written in a night, Stilling-Andersen and 10 June 1882.
The body no longer mentions the building (run 2 cut the last overlap, which the first checker found). **With 42 §03, 22 §08, 26 §09,
27 §05, 27 §09 and 29 §03, all seven cases are decided.** Also re-scoped in Part H: 34 §01 (the body's
Treaty-of-London sentence was the vignette's point); 36 §09/§10 (§09 keeps the Reform party and the seat
count, the vignette Christensen); 32 §09's vignette lost its paragraph on the 1844 patent; 33 §06's
closing line was cut.

**D-6.** Every date in 32–36 is Gregorian on both sides; there is no Russian date in the part, so
nothing to add. **START_HERE_review_10's calendar remark was wrong** (§14.1): Sweden was Julian from
1712 to 1753, not one day ahead in 1716. 27's Sources now say its 16 April is the Danish-Norwegian style
(5 April, Swedish), with Fredriksten as the check.

**D-14.** 32's Meanwhile "Charles 10." is Charles X. The ship *Christian VIII* keeps its painted name.
Nothing else to change.

### 14.6 The guard: `pageguard.py`, shared by Part G and Part H

`build_part_h.py` had no retired-vocabulary guard and no summary line (§13.4). It now has Part G's, and
both builds import one module, `pageguard.py`, as every word counter imports `pagewords.py`. **Four
checks, each asked before the page is written**, and a page that fails one is not written at all:

1. **freshcheck** — the body on disk is exactly what its draft builds.
2. **`same_body`** — the body the build will read (from `DK_SRC`) is byte-identical to the body
   freshcheck read. This is the body's own witness.
3. **`figures_fresh`** — every `figs_*`/`map_*` script that produces a figure the part needs is run in
   a scratch copy of `files/`, and its output is compared byte for byte with the `svg_*.txt` the build
   will read. This is the figure's own witness.
4. **`stale_vocabulary`** on **`reader_text`** — the words a reader sees or a screen reader speaks:
   every tag becomes a space; scripts, styles and comments go; attributes that reach a reader
   (`aria-*`, `alt`, `title`, `placeholder`, `label`, `data-*`) are read in any case and any quoting;
   entities are decoded twice; NFKC; invisible characters removed; look-alike letters folded; dashes
   folded. Band X in any case (with a capital A–I, so "a brass band" passes), entry/entries, Era
   page(s), and a zero-padded chapter number however it is joined ("chapter-07", "ch 07", "chapter
   #07", "chapters 3 through 07").

**The checker's holes.** Run 1's guard read text with the gaps §13.6 had closed for markup, and the
checker got past it three ways, each shown on a scratch copy with the build printing "all five built
clean": **a stale body** (with `DK_SRC` pointing at an old copy, freshcheck checked `files/` and the
build read the other — inside the repository, with no warning at all); **the vocabulary** (tags removed
with no separator, so "entry</li><li>Forliget" read "entryForliget"; zero-width characters; "BAND C" in a
figure; the padded forms above; "Era pages"; only lower-case double-quoted attributes; homoglyphs; and
the page written before the check); **a stale figure** (an old `svg_vestvold_1888.txt` restored,
unnoticed, because nothing asked whether the script still wrote it). Checks 2–4 are the answers.

**The false positive on the first real run.** Page 30's header reads "Chapter 30 1620 – 1803" once its
tags are spaces and its dash folded, and the new padded pattern read "18" and "03" out of 1803. Numbers now need digit boundaries on both sides,
not `\b`, so "chapter07" is still caught and a year is not split.

**"entry" by hand, before trusting the clean run.** On the built pages 32–36 — text, figure text and
attributes, whitespace joined, case ignored — **none**. The only matches are the JavaScript's `entries`,
and `reader_text` drops scripts. Part H's `ALLOWED_ENTRY` is empty, and correctly so. (Part G keeps its
two, §13.6.) Re-searched in part B on the final build: the same.

**Tested.** `claude/session10_guardcases.py`: **42 of 42 unit cases right** — 31 that must fire (every
hole above, plus the §13.6 forms) and 11 that must stay quiet (the year range, "a brass band",
"entrenched", "centre", a new era, script `entries`, a style rule, a comment, "chapter 31, 1807") —
re-run in part B. **Six planted end-to-end cases**, on a scratch copy — in H a stale `DK_SRC` body, the
old `svg_vestvold` restored, and mkbody's key 'Vestvolden entry'; in G "chapter-07" in 29, a hand-edited
`svg_norway`, and a `DK_SRC` pointing at an old c27 body — **all fired, and the pages were left
untouched.** On the real pages both parts build clean: G 21 figures fresh, H 15.

**Known limits, by design.** Homoglyphs are folded for the letters the retired words use, not for every
script in Unicode. A figure no script in `files/` produces (Parts A–D's inline figures) is reported
sourceless, as figcheck does. Parts A–F and I build as before; Part I's build has no vocabulary guard
and no summary line yet (for review 11).

### 14.7 D-9 — none in the book

Part H was tagged at drafting; every tag was checked against its vignette. **36's J.C. Christensen
retagged `[-]`**: by 1901 he had sat in the Folketing for eleven years and led a party, and the
vignette's moment is his entry into the ministry. 36 keeps `[n]` in Julius Rasmussen and `[f]` in Line
Luplau. 35's who-line is now *washerwoman and union president* (KVINFO: her trade "cannot be
established with certainty"). 32 carries Peter Larsen `[n]` (a farmer, and the weakest `[n]` in the part,
recorded as such), Johanne Luise Pätges `[f][n]`; 33 Morten Jørgensen `[n]`, Mathilde Fibiger `[f]`; 34
Niels Kjeldsen `[n]`, Ilia Fibiger `[f]`; 35 Uhd `[n]`, Olivia Nielsen `[f][n]`. With R-16 to R-18
carried out, **`vignettes.py` reports no D-9 failure anywhere in the book.**

### 14.8 Checked by separate agents

**Run 1's checker** (`claude/session10_checker_report.md`), given the fixers' hunks and logs as
claims: **98 rows** — Part G's three vignettes 17, 32 eighteen, 33 ten, 34 fifteen, 35 eighteen, 36
twenty, the last three of them tooling holes (§14.6) and one a pointer to a §14 that did not yet exist.
Among them: Hjedding §12 read three times and **the fixer was right** — the contract counts votes by
cows; Torstedlund's notes left out; Jews voting only in the kingdom; "insolvent" left three times after
"defaulted" went; Kari Hiran "wrote" a petition someone else wrote; Andersen "remembering" what he heard
from a sickbed; the Treaty of London still "broken" in 34's Summary, hook and question after 33 had put
the promise beside it; 36's coda "still in force" against 35's 1960; a stale map beside a corrected
caption. All applied in run 2 by six fixers, and the shared files by the lead.

**Part A's two checkers** (`claude/session10_check2_A.md`, `_B.md`), given run 2's diff only: **18
findings** — A seven, all minor; B eleven, one substantive: **35's Hanssen vignette still said his
associations were being "dissolved"**, 25 lines below the body, glossary and Summary that run 2 had
corrected. Fourteen applied, and one of A's "not verified" (32 §05's "a state that had no credit left",
unsourced, and the 1825 London loan argues against it — cut). The one new fact, de Meza called to
Copenhagen on 6 February, was checked against Grænseforeningen by the reviewer. **Rejected, with
reasons:** B7 and B8 (questions asked twice or three times on a page; they predate the session and are a
book-wide rule, §14.4); B11 (unwrapped source lines; mkbody joins lines, and only lines an edit touched
were rewrapped). Neither report asked for any run-2 fact to be reverted. **Log errors, page right:**
fixlog_G's Christiania date, fixlog_32's missing §09 trim, fixlog_34's "diary" and its "a string of"
parishes that went into the map as "eight", fixlog_36's inference about the 1895 count. No third check:
the changes were about twenty lines of prose, one aria phrase and one legend line.

### 14.9 Decisions for Carsten

**None.** D-13 is closed, D-9 has no failure, and everything found in §14.4 is either Part I's reading
(review 11) or a rule already in CONVENTIONS to apply. The one open question of practice — may a
WHAT-THIS-PAGE-ANSWERS question preview a checkpoint? — is measured across the book in review 11 first;
if it needs a rule, it comes to Carsten then, with the numbers.
