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
