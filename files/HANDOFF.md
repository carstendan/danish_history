# HANDOFF

A digital history of Denmark, c. 13,000 BCE to 1953. Self-contained downloadable
HTML chapters, written in English with Danish terms kept and glossed, narrative
in the manner of Hastings and Beevor: individual people at named moments carrying
the argument.

---

## Vocabulary — settled, do not drift

- **Part** — a lettered span, A to I. Part E is chapters 16–20; Part F is 21–24.
- **Chapter** — a numbered page, 01 upward. There are 45: Part G took seven
  chapters rather than six (decision D-2, Aug 2026), so everything from the old 29
  upward shifted by one; Part I was planned at eight (D-10, Sept 2026) and the
  boundary pass made it nine (item 136).
- **Section** — a numbered unit inside a chapter, 01 to about 12.

*Band* and *entry* are retired, in the index too as of August 2026. The only
survivals are the CSS class names `.band` / `.entry` in the index stylesheet and
the `--band` token in `style.css`, all deliberate: renaming them is cosmetic and
touches every rule.

**Lettered chapters are retired.** 16a and 16b are now 16 and 17. A chapter that
needs two pages is given two numbers **when the part is planned**, before it is
written — see Lessons.

---

## State

| Part | Chapters | Span | Status |
|---|---|---|---|
| A–C | 01–11 | to 1050 | built; bodies recovered via `debuild.py` |
| D | 12–15 | 1050–1375 | built, reviewed, revised |
| E | 16–20 | 1375–1536 | built, reviewed, revised; renumbered Aug 2026 |
| F | 21–24 | 1536–1660 | **built, reviewed, revised, closed; online** |
| G | 25–31 | 1660–1814 | **built, reviewed, revised; all seven round-trip clean** |
| H | 32–36 | 1814–1901 | **built, verified, indexed, closed — see `PLAN_H.md`** |
| I | 37–45 | 1901–1955 | **NINE CHAPTERS, ALL BUILT, VERIFIED AND INDEXED. The boundary pass is done — item 136 — and item 128 is CLOSED.** The 1943–1955 run was repartitioned from three chapters into four at the material's own seams; no chapter in the part is outside the 25–50 band |

**After item 140 the book is 336,690 page words, 26.7 h; Part I 74,233** —
read off `bookstats.py` on a fresh clone of the pushed repository, 19 September
2026. (Item 139's 336,857 fell by the cuts of I-1 and I-3.) The figures below are
item 138's.

**BOOK COMPLETE: 45 of 45, 336,231 page words, 26.7 h; 0 remaining.** Read off
`bookstats.py` after `linkindex.py` on 19 September 2026, after the item 138
rebuild. The rise from item 136's 333,337 is prose that was always in the drafts
and had never reached the pages — the myth-checks of Parts G and H and two
Meanwhile paragraphs — not new writing. Part G is 53,013, Part H 41,035, Part I
73,949.

Part I as built:

```
37  Reform, neutrality, the sale of the West Indies  7,902 page (38 min)  3L/4M/3H
38  Genforeningen, Iceland and the Easter Crisis     7,824 page (37 min)  4L/4M/3H
39  Deflation, Landmandsbanken, the first government 7,455 page (36 min)  3L/4M/3H
40  Depression, Stauning, the welfare state's seeds  8,358 page (40 min)  3L/5M/3H
41  9 April 1940 and samarbejdspolitikken            8,707 page (41 min)  4L/4M/3H
42  1943: the year the policy broke                  7,577 page (36 min)  0L/1M/5H
43  The underground and the liberation               7,728 page (37 min)  0L/1M/3H/2 OVER
44  The reckoning, and the accounts                  9,044 page (43 min)  0L/3M/5H
45  Choosing a side, and the constitution            9,354 page (45 min)  5L/6M/1H + coda
```

Profiles for 42–45 are read off `narrative.py` on a fresh clone of the item 138
build, per item 120; 37–41 are as recorded at their build. **Chapter 43 has two
of the book's three sections over `narrative.py`'s heavy ceiling** (834 and 820
words; the third is chapter 16's Kalmar, 849), and 42 and 44 have no light
section at all. Nothing fails — the band is 25–50 — but the part item 136
describes as cut at the material's own seams carries its weight very unevenly,
and the consistency review should look at that before anything else in Part I.

**Six chapters are over the 40-minute advisory of decision 2.1, not one:** 21 (47),
28 (44), 33 (42), 41 (41), 44 (43) and 45 (45). 41 is the one with a defended cut,
item 118. 44 and 45 have no defence on record yet. 28 and 33 rose from 43 and 41
in the item 138 rebuild, because their myth-checks are now on the page.

All of 01–24 are published to a web folder. Chapter pages carry two links back to
the index, inserted by `linkindex.py` — see Tools. **`freshcheck.py` joins the cold run and must pass before any commit: it is the only check that compares a
build output with its source rather than with another build output — item 133.**
**`appcheck.py` joins it (item 138): freshcheck asks whether a page is newer than
its draft, appcheck asks whether the draft's words reached the page. Neither can see
what the other catches.**

Part E as built:

```
16  Margrete I and the making of the union      7,191 page / 7,033 text (34 min)
17  The union at work, and the end of Margrete  6,026 page / 5,880 text (29 min)
18  Sound Dues, the Hanse, a straining union     7,240 page / 7,063 text (34 min)
19  Schleswig-Holstein and the union's collapse  7,463 page / 7,274 text (36 min)
20  Reformation and the Count's Feud             7,079 page / 6,896 text (34 min)
```

All five: 3 checkpoints · 3 vignettes · 2 meanwhile boxes · 10–12 glossary blocks;
3 figures except 17, which carries 2. Braces balanced, no placeholders left, every
internal anchor resolves, tags balanced including inside the SVGs, TAIL in both
rail and TOC, part colour `#2E6B5E`, no unicode escapes leaked. Chapter 20
additionally carries the part coda, via `tail_extra`.

Part F as built:

```
21  The Lutheran realm of the nobility            9,812 page / 9,619 text (47 min)
22  Christian 4.: ambition and the building years  6,619 page / 6,444 text (32 min)
23  Christian 4.: the wars that broke him          6,422 page / 6,244 text (31 min)
24  Losing the eastern provinces                   6,592 page / 6,394 text (31 min)
```

All four: 3 checkpoints · 3 vignettes · 2 meanwhile boxes · 3 figures · 9–10
glossary blocks. Part F colour `#8A2B2B`, the `--oxblood` token already in
`style.css`; parts D and E are both teal and F had to move away from them.
Chapter 24 carries the part coda, via `tail_extra`.

**Chapter 21 stays at 47 minutes.** (49 was a pre-fix page count; measured,
it is 9,812 page / 9,619 text words.) It was drafted long and the Part F review
reversed the obvious diagnosis: sections 02 and 03 look heavy only because each
carries a vignette, and §02 has the second-*lightest* narrative in the chapter.
Trimming there would have cut Palladius in the parish. The real fault is that no
section is genuinely light — a rewrite, not a trim — and it is not worth doing to
save four minutes inside the band.

Size of the whole, measured rather than guessed (`bookstats.py`): nine built
chapters of E and F average about 7,500 words and 36 minutes, which projects to
roughly **300,000 words and 25 hours** at 43 chapters. Re-measured Sept 2026 on
the corrected counter: 31 built chapters run 219,617 page / 214,234 text words,
17.4 hours, mean 34 minutes. **The split candidates are all retired** (21, 28 and
32).

**Re-measured again at the Part I planning session, Sept 2026: the landing is 44,
not 43.** Part I takes eight chapters by decision D-10, and `bookstats.py`'s
`TOTAL_PLANNED` and part table now say so. The dense flags were `{35, 41}` in two
files; 35 shipped at 37 minutes and is not a split candidate, and 41 renumbered to
42 when the twenties took a chapter, so both files now carry `{42}` — the 1943–45
chapter, which `PLAN_I` 2.7 keeps whole unless its first draft passes 8,400 page
words. 36 built chapters run 259,526 page / 253,321 text words, 20.6 hours; the
projection at 44 chapters is 317,198 page words and 25.2 hours, and `PLAN_I` §1.5
puts it at 322,062 and 25.6 on Part I's own planned weights rather than on the
book's running mean.

The Christian 4. seam is at 1625 — where he stops founding things and starts
losing wars. Brømsebro 1645 belongs to 24, not 23, which ends at his death in
1648.

Twelve figures in Part E. Four are the spine maps' business (1397 and 1500, plus
their verification); the rest are chapter-scale maps and non-map diagrams.

---

## Files

### In project knowledge — the things that cannot be recovered

| File | Why it must survive |
|---|---|
| `mapkit.py` | projection and geometry primitives |
| `mapspine.py` | the eleven-map frame, palette, western panel, **and the detail-map helpers** |
| `map_1397.py` | lon/lat polygons for Denmark, Norway, Sweden, Schleswig, Gotland |
| `map_1500.py` | 1500, importing its base polygons from `map_1397.py` |
| `mapfixture.py` | the standing test fixture for all eleven maps. **Run before any map ships.** |
| `build_parts_abc.py`, `build_part_d.py`, `build_part_e.py` | the section manifests and the checkpoint text |
| `build_all.py` | the runner |
| `debuild.py` | recovery from a built page |
| `index_generator.py` | the index |
| `style.css`, `rail.js` | extracted from chapter 11, byte-identical to what it ships |
| `c16_body.html` … `c45_body.html` | see below. Thirty retained bodies, 16–45; the `c16a`/`c16b` names are retired. **They are build inputs, regenerated by `mkbody.py` — a part build never reads a draft (item 138)** |

**Why the bodies are kept.** `debuild.py` recovers a working body from any
shipped page, but with the SVGs **inlined** rather than as `{{SVG_*}}`
placeholders — chapter 19 comes back as 150 KB with three frozen blobs against
the 46 KB authored source. Debuild is a recovery path of last resort, which is
the role it played when the canonical template was lost. It is not a substitute
for keeping the sources.

**Why the map scripts are kept.** A built page carries only projected path data.
The lon/lat polygons exist nowhere else, `map_1500.py` already imports them from
`map_1397.py`, and the seven remaining spine maps — 1600, 1660, 1721, 1814, 1864,
1920, 1945 — will do the same.

### Local only, not project knowledge

`figs_17.py`, `figs_18.py`, `figs_19.py`, `fig_crowns.py`, `fig_titles.py`, and
the `svg_*.txt` they emit. Chapter-specific and rerunnable. `figs_16b.py` too. If one is lost the
figure still survives inside the shipped page; only editing it gets expensive.
This matches the Part D precedent, where the ten figure scripts were not kept.

### Delete, do not just replace

- `verify_1397.py` — superseded by `mapfixture.py`.
- `figkit.py` — folded into `mapspine.py`; nothing imports it.
- the old `build_all.py` and the old `HANDOFF.md` — both replaced.
- ~~`c16_body.html` — superseded by `c16a_body.html` and `c16b_body.html`.~~
  **STRUCK, Sept 2026. Do not do this.** After the renumbering, 16a and 16b
  *became* chapters 16 and 17, and `c16_body.html` is the live chapter 16 body
  that `tidy.py` reports present. Following that line would destroy a working
  source. The companion instruction below, deleting
  `16-margrete-i-and-the-kalmar-union.html`, is already done.
- **`16-margrete-i-and-the-kalmar-union.html` in the chapter folder.** This one
  matters: `index_generator.py` discovers pages by globbing `NN*.html`, so a
  leftover chapter 16 file is found alongside 16a and 16b and the index will show
  three pages for chapter 16, with the title linking to the stale one.

### Retired

- `figkit.py` — folded into `mapspine.py` as `detail_frame`, `detail_land_path`,
  `detail_base`. Delete it; nothing imports it.
- the old `build_all.py` — it was never a runner. It was a one-off retrofit that
  injected checkpoint CSS into entries 01–08, pointed at `/home/claude/geo/`, and
  rewrote `Era page · about N minutes` in the retired vocabulary. Replaced.

---

## Building

```
npm pack world-atlas && tar xzf world-atlas-*.tgz     # provides package/land-*.json
pip install cairosvg --break-system-packages          # only needed to rasterise

python3 build_all.py --check    # what is present, builds nothing
python3 build_all.py            # every part whose inputs are present
python3 build_all.py e          # one part
```

Each part build verifies itself and exits non-zero on failure. `build_all.py`
adds up the result and fails any chapter outside the 25–50 minute band
(`BAND` in `build_all.py`; widened from 25–45 in August 2026).

Figures are regenerated by running their scripts, which write `svg_*.txt` next to
themselves; the part build inlines those. Rasterise and **look at** anything
before shipping it.

---

## Lessons

*Numbered `L1`–`L12`. The prefix exists because this list and the open-items
list both ran to 11 and 12, and a scripted edit anchored on the wrong section.
Open items stay bare numbers; lessons carry the L.*

L1. **First drafts land short, and short means a missing subject, not thin prose.**
   Chapter 20 came in at 28 minutes; what was missing was the monasteries. Adding
   the subject fixed the length. *Part E:* chapter 16 landed **long**, at 47 minutes,
   and three passes of rewriting recovered only 700 words — because paraphrasing is
   not cutting. Length is governed by topic count. Twelve substantial sections will
   not fit the band; decide the count before writing.

   *Part F:* chapter 21 landed at 46 minutes with **nine** sections, not twelve — so
   topic count is necessary but not sufficient. The failure was that every section
   was written at full weight, averaging 858 words against chapter 20's 590, with no
   light connective sections at all. Chapter 20 breathes because three of its nine do
   their job in about 260 words. Vary the weight, not just the count.

   *Part G:* **words-per-section is the wrong unit, and using it produced a 60%
   error in the first version of the Part G plan.** Apparatus does not scale with
   section count: three vignettes, two meanwhile boxes, three figures, the glossary
   blocks, the checkpoints and the terminal units cost 2,600–3,000 words whether a
   chapter has nine sections or ten. Only narrative scales. Measured on Part F —
   ch 21: 7,137 narrative of 10,218 page words; ch 22: 4,383 of 7,104; ch 23: 4,350
   of 6,957; ch 24: 4,020 of 7,014. Chapter 21's overrun is *entirely* narrative,
   which is why including it lifts page-words-per-section from 727 to 823. The
   formula is:

   > **page words ≈ Σ(section narrative bands) + 3,508**

   with narrative bands of **light 240 · medium 376 · heavy 576**. A nine-section
   chapter at 2 light / 4 medium / 3 heavy lands near 7,200 page words and 34
   minutes; a ten-section chapter at 2 / 4 / 4 near 7,800 and 37.

   *Part H:* **both the constant and the bands above are corrections, made Sept
   2026 by measuring rather than estimating.** The 2,800 was derived from Part F
   page counts taken before the word-counter fix, which removed SVG label text —
   figure text, and therefore apparatus — so the fix took its cut almost entirely
   out of the constant. A replacement estimate of 2,400, computed during the Part
   H session from this ledger's own Part F narrative figures, was **also wrong**,
   because those figures were pre-fix too. Measured directly across the seven Part
   G pages with `narrative.py`: mean narrative 3,884, mean page 7,392, apparatus
   **3,508** — 47 per cent of a chapter. The old bands describe half the data:
   **34 of the 68 measured Part G sections fall in the gaps between them.**
   Observed spread: min 154, p25 275, median 365, p75 483, max 742; the bands
   above are its terciles. "Heavy" at 576 sits below the old heavy band entirely —
   the model was predicting heavier sections than anyone writes. Nine or ten
   sections is the working shape. Derivation in `PLAN_H.md` §1.

1a. **Reading time: hard band 25–50, soft advisory 28–40.** *(Advisory moved from
30–42 in Sept 2026 — see below. The band is unchanged.)* `build_all.py` fails
   outside the band and prints a note outside the target. The band was 25–45 until
   August 2026 and was widened because **25–45 is not closed under splitting**: a
   chapter at the old ceiling halves to 22.5, below the floor, so 45–50 was a dead
   zone where a chapter was at once too long to keep and too short to divide. Chapter
   21 landed exactly there. A 2:1 band has no dead zone — anything at the ceiling
   splits into two at the floor. **Do not narrow it again without checking that
   property holds.** The soft target exists because the old ceiling was doing double
   duty as the diagnostic in lesson 1, and widening the hard rule alone would have
   retired the most useful signal the build produces.

1b. **Page count is decided when a part is planned, and frozen once it is built.**
   Chapter 16 split because it was written first and measured second, which forced
   the renumbering of August 2026. Chapter 21 did the same thing and was kept whole
   rather than split, precisely to avoid a second renumber. Christian 4. was given
   two numbers at plan time instead. Lettered halves are retired: a chapter needing
   two pages gets two numbers before a word is written. A split discovered afterwards
   is what costs an afternoon.
L2. **The countryside and religion are the two subjects that get forgotten.** Every
   chapter needs both. Deserted farms and the ox road in 16–17, the bound
   peasantry in 18, the monasteries in 19.
L3. **Do not repeat the previous part's beats.** Part D used a child's wedding, an
   arrest, a murdered king. Part E used a captive king, an execution outside a
   castle, an impostor at a market, a banner-bearer, a standard-bearer's town.
L4. **Vary the figure forms.** Part E added: a stepped ladder of titles, a rule
   block, a voyage map with a key strip, a fealty diagram, a battle schematic
   that is deliberately not a map, a proportional band chart, a twelve-week
   timeline.
L5. **Carry-forward lines must be solvent.** Every `→` must point at a chapter that
   will actually carry the promised content.
L6. **Terminal apparatus must appear in rail and TOC.** Guarded by the build.
L7. **Vignettes are a named person at a named place and hour.** *7a:* women must
   appear as agents. Part E: Margrete, Philippa, Kristina Gyllenstierna, Sigbrit
   Villumsdatter. *9a:* the `(who)` line names a person, or says on the page why
   it cannot — the false Oluf has no name because the only one he offered was
   somebody else's.
L8. **Hedge live controversies explicitly.** The union letter, the 1460 clause, the
   Dannebrog legend, the 1536 land shares.
L9. **Close on something that lands.** Chapter 15's ending is the model. Chapter 16
   closes on an object, 17 on an argument, 18 on two kings leaving, 19 on what the
   whole part was about. Do not close two consecutive chapters the same way.
L10. **Checkpoints live in the build script, keyed to section title fragments**, so
    a renamed section breaks the build loudly. Any checkpoint left in a body is
    stripped and reinserted.
L11. **Set the part colour from `style.css`'s `--band:#96591A;` token.** The token
    is still named `--band`; the CSS has not been renamed.
L12. **Looking has caught a real error in every part.** Point-in-polygon tests are
    necessary and not sufficient. In Part E, rasterising caught: a legend printed
    across Jutland; a conic projection turning a four-corner Greenland box into a
    diagonal slash; an Orkney box that would have tinted mainland Scotland; a seam
    where two translucent fills overlapped; sea printing as land; and — the worst —
    **south-west Norway unfilled in the 1397 map, which had already shipped**,
    because none of the thirty-six test cases was in Rogaland. When a polygon is
    corrected, add the case that would have caught it.

L13. **Length that comes entirely from narrative is a weight fault, not a topic-count
    fault — and it is now measurable.** Chapter 28's apparatus is 3,616 against a
    Part G mean of 3,508: normal. Its narrative is 5,470, thirty-nine per cent above
    any other chapter in the part, at a mean of 547 words a section against roughly
    380 elsewhere. It is not over-sectioned; it is written heavy in every section,
    with five of ten above 560 and no genuinely light one after §01. **That is
    chapter 21's signature exactly** — third instance of "vary the weight, not just
    the count" (L1), and the first measured rather than inferred. `narrative.py`
    separates the two cases in one run. Test a split candidate against it before
    opening it.

L14. **A constant derived from unverified inputs is a typed number.** The apparatus
    constant of 2,800 was wrong because it was measured before the word-counter fix.
    The replacement estimate of 2,400, computed from this ledger's own Part F
    narrative figures, was **also wrong**, because those figures were pre-fix too.
    The measured constant is 3,508. The arithmetic was sound both times. **"Compute,
    do not type" is not satisfied by computing from numbers someone else typed.**

L15. **Enumerate what you want, not what you want removed.** The first version of
    `narrative.py` stripped apparatus by listing its selectors. It missed the page
    header entirely and got two of nine selector names wrong — and the header miss
    would have been silent, because it inflates narrative and deflates the constant,
    the direction that matters. Rewritten to select the narrative region positively,
    everything unnamed falls into apparatus by construction and no selector has to be
    guessed. **Where a measurement can be defined by what it includes rather than by
    what it excludes, define it that way.** The excluded set is where silent misses
    live.

L16. **A guard that only fires at review is not a guard.** Both recorded
    vignette-balance faults — chapter 25's missing woman, chapter 31's missing
    non-elite subject — came from a hand audit in `REVIEW-PART-G.md` §2, after the
    chapters were drafted. `vignettes.py` never checked either, and nobody had
    noticed that it did not. See D-9.


---

## The land-path trap, recorded so it is not rediscovered

`mapkit.land_path` runs Sutherland–Hodgman per ring, and where a ring exits and
re-enters the frame it walks the frame edge between the two points. On the spine
frame this is harmless. On a closer frame whose western edge sits in open water it
bridges the Eurasian ring across the mouth of the North Sea and **prints the sea
as land**.

Use `mapspine.detail_base` / `detail_land_path` for any Denmark-scale map. They
project each ring whole and let an SVG clip trim it, thinning points far from the
view so the file stays reasonable — 174 KB rather than 1.5 MB on the chapter 16
map.

---


## Settled during the Part E review

- **A chapter may carry its own terminal units** beyond the standard six. `build_part_e.py`
  takes `tail_extra` per chapter, and only chapter 19 uses it, for the part coda. The rail
  and TOC check covers the extras too, so a coda cannot go missing.
- **The sources block is two-tier**, everywhere in Part E: `WORKED FROM` for documents,
  editions, archives and reference sites; `WHERE THE ARGUMENT STANDS` for named historians
  as positions rather than as reading. This settles by construction the question of whether
  the chapters claim to rest on monographs they have not read. Retro-fit to A–D when those
  parts are next touched.
- **A figure must not summarise prose the reader has just read.** Two dated bands were cut
  during the review — chapter 17's 1497/1567/1857 band and chapter 18's Dahlmann/Neuber band —
  because both retold their own chapter's sections. The one kept, in chapter 19, quotes a
  primary text the prose only paraphrases. That is the test: a figure may carry what the
  prose cannot, not a digest of what it already did.
- **Part-closing material is a coda, not a section.** A numbered section labelled
  `NARRATIVE` that carries only conclusions makes a promise the anatomy does not keep, and
  it stacks a fourth retrospective unit in front of the myth-check, carry-forward and
  summary. Chapter 19's coda sits after the visit block, unnumbered, with its own kicker.

## The map fixture

`mapfixture.py` replaces the per-map case lists, which were ad hoc: each map could
only fail in ways somebody thought of while writing that map. The 1397 map shipped
with south-west Norway unfilled and thirty-six cases passed it, because none was in
Rogaland. Three layers now:

1. **Curated** — named places with their allegiance in a given map year. The layer
   that carries historical judgement, and the one worth arguing about.
2. **Coverage** — a 0.2° grid swept over the frame. Every point that is on land and
   inside the year's envelope must belong to **exactly one** territory. Land belonging
   to nobody is the Rogaland failure; land belonging to two is the
   Ditmarschen-inside-Holstein failure. Neither is a case anyone has to remember to
   write. The envelope is the only judgement in this layer: a generous outline of what
   the map is about, so that Germany and Scotland are not reported as gaps.
3. **Asserted** — every territory must carry at least three curated cases, so adding a
   polygon without testing it fails.

Run it, and *look at* the rasterised map as well: the sweep cannot see a legend printed
across Jutland.

**What it found on first run,** on maps that had already shipped and passed their old
tests:

- **Bornholm was missing from both maps.** Danish, held by the archbishop of Lund since
  the twelfth century, and simply not in any polygon.
- **Schwansen**, between the Schlei and Eckernförde, was outside both duchy polygons.
- **A hairline of unclaimed land the whole length of the Norway–Sweden border**, because
  the two polygons had near-identical but not identical vertices. Sweden's western edge
  is now Norway's eastern edge copied exactly — do not "tidy" them apart.
- The same at the Göta älv between Denmark and Sweden, and a Denmark/Schleswig overlap
  off southern Funen.
- Four outer Norwegian islands just outside the offshore boundary, which now runs well
  out to sea. The fill is clipped to land, so a generous sea boundary costs nothing.

Reintroducing the Rogaland bug makes the fixture fail three curated cases and report six
unclaimed land points, which is what it was built for.

## Open items

1. ~~Chapter 16 is 46 minutes.~~ ~~Split at Kalmar.~~ **Closed, and renumbered.**
   The two halves are now chapters 16 (1375–1397, the making, 8 sections, ~37 min)
   and 17 (1397–1412, the union at work, 6 sections, ~30 min). A straight cut would
   have left the second five minutes below the floor, so the headroom went on two new
   sections — Norway from partner to province, and the end of Norse Greenland — plus a
   vignette about two Icelanders married at Hvalsey in 1408, the part's first non-elite
   vignette. Chapter 17 carries two figures rather than three; chapters 10 and 14 set
   that precedent.

2. ~~The index has not been regenerated.~~ **Done, and again after the renumbering.**
   `index_generator.py` discovers built chapters on disk (`DK_CHAPTERS`) and writes
   beside them (`DK_OUT`, defaulting to the same place). Both used to be hardcoded to
   the container; the second only surfaced in August 2026, when the script built the
   whole document and then failed on its last line. **The first did exactly the same
   thing in September 2026 and is now fixed at the source** — both default to this
   repository, derived from `__file__`, and `dkpaths.py` refuses a default that does
   not exist instead of failing at the write. See item 137: this paragraph had
   described the failure a month before it recurred. Anchors are `part-*` and
   `c01`–`c45`; counts are computed. **Run it from `files/` with `DK_CHAPTERS`
   unset** — it derives the chapter folder from its own location (item 137), and
   an exported variable is what sent the item 138 rebuild into `~/Documents`.
3. **`build_part_d.py` reads `e12_body.html`–`e15_body.html`** on the old `e`
   prefix, while A–C and E use `c`. Harmless until someone tries to rebuild D and
   has the files under the other name. `build_all.py --check` reports it.
4. **`build_parts_abc.py` and `build_part_d.py` cannot currently rebuild.** Both do
   `style.replace('--part:#96591A;', ...)` against a `style.css` whose token is named
   `--band:`. The replace silently no-ops and the verify step then reports the part
   colour as BAD. `build_part_e.py` raises loudly on a missing token instead, which is
   the better behaviour; copy it into the other two. One line each.
5. **The project mirror has been stale before**, and was again in August 2026:
   `/mnt/project` held a `build_part_e.py` with chapter 16 unsplit and no coda.
   **The working folder is the source of truth, and on 18 September 2026 it MOVED OUT
   OF iCLOUD**: it is now `~/Documents/Danish History`, not
   `~/Library/Mobile Documents/com~apple~CloudDocs/Documents/Danish History`. If any
   copy still exists at the old path it is not the book — check the git log before
   believing a file found there. If two copies disagree, the shipped chapters are the
   tiebreaker.
5a. ~~**Chapters 16–19 as published still carry the seam.**~~ **CLOSED, August 2026**,
   in the ledger pass. Parts E and F were rebuilt; 1397 and 1500 were regenerated from
   source and passed all four fixture layers, and chapters 17, 18 and 23 came out
   byte-identical to what shipped, which is what proved the rebuild lossless. The
   original entry follows.

   **Chapters 16–19 as published still carry the seam.** They were built before the
   fix, so their inlined 1397 and 1500 maps hold the old geometry — the source is
   correct, the shipped pages are not. The lens is one or two pixels at reading size,
   which is why it survived so long, so this is not urgent; but it is real, and the
   only way to clear it is to re-run Part E's figure scripts, rebuild, re-run
   `linkindex.py` and re-upload. Worth doing the next time Part E is touched for any
   other reason.
5b. **`map_1050.py` and `map_1250.py` no longer exist**, in either folder, and Part D's
   bodies with them. Those two spine maps survive only inlined in built pages, so
   `seamcheck.py` structurally cannot see them. They were inspected by eye via
   `mapdump.py` in August 2026 and are clean — on the early maps Denmark is a single
   fill with no pale-green neighbour touching it, so there is nothing to overlap.
   **If either map is ever redrawn, it has to be rebuilt from scratch.**
6. **Part D revisions**, if any remain outstanding from its review.
7. ~~**Chapter 20's footer** says Part F runs to 1721.~~ **CLOSED, August 2026.**
   The footer now reads 1536–1660 and the *Faith and the state* thread now says Part G.
   Both were fixed in the ledger pass and shipped with the Part E rebuild.
8. **`linkindex.py` must be re-run after any rebuild.** A rebuilt page comes out of
   the build script without its index links. The routine is build → `linkindex.py`
   → `index_generator.py`, then upload.
9. **Two figure-economy calls, deliberately left open by the Part F review.**
   Whether chapter 23 needs three figures or two, and whether chapter 24's fan
   should keep the event text or drop to dates only. Both are judgement, neither
   is a fault.
10. **`overruns()` has been under-reporting by about ten per cent.** The constant of
   5.55 units per character is wrong for this mono face; measured off the raster it
   is about **6.1**. `figs_25.py` through `figs_31.py` use the corrected value;
   **`figs_24.py` still has 5.55**, and Part F's four figure scripts should be re-run
   under 6.1 — there is a real chance something shipped with text off the canvas.
   Note also what the guard cannot see at any constant: text overflowing a *container*
   rather than the canvas, and text crossing a column divider. Both happened in Part G
   and passed clean. Looking is still the check.
11. ~~**`map_1397.py` places Sveg and eastern Härjedalen inside `SWEDEN`.**~~
   **CLOSED, August 2026.** The border was moved east across Härjedalen; 1397, 1500 and
   1600 were regenerated and Parts E and F rebuilt. **The corrected vertices were not
   invented.** `map_1660.py`'s `NO_LOST` already drew that stretch as `(14.65,62.90) →
   (14.95,62.20) → (14.60,61.75) → (13.05,61.90)`, and its docstring claimed that edge
   *was* 1397's Norway. It was not: 1397 cut the corner at a single `(14.45,62.20)`.
   1660's line is the verified one, so it was propagated back rather than redrawn.
   `NORWAY`, `SWEDEN` and the dashed `NO_SE` moved together; fixture and seam layer pass
   on all five maps.

   **Why the fixture missed it, which is the part worth keeping.** 1397 already carried a
   curated Härjedalen case — at `13.50, 62.30`, in the *western* half of the province,
   inside the line whether the line was right or wrong. A case can name the right place
   and test nothing. Sveg and Lillhärdal are now registered on 1397, 1500 and 1600; both
   sit east of where the old border ran, so either would have failed it. Ytterhogdal was
   tried and dropped — it clears the corrected border by 600 m, too fine a margin for a
   standing test. The original entry follows.

   **`map_1397.py` places Sveg and eastern Härjedalen inside `SWEDEN`.** Härjedalen
   was Norwegian until Brömsebro in 1645, so 1397, 1500 and 1600 each hand roughly
   half a Norwegian province to Sweden two and a half centuries early. It is **not** a
   seam fault — the border is shared exactly and simply drawn in the wrong place,
   which is why three verification layers and a shipped review all missed it; only a
   curated case east of the existing ones exposes it, and none was ever written.
   `mapfixture.py` now carries the Sveg case, registered against 1660 only, so the
   standing fixture passes while three shipped maps stay wrong. Fixing it means moving
   shared vertices in `NORWAY` and `SWEDEN` and rebuilding Parts E and F.
12. ~~**Chapter 15's forward arrow is knowingly stale.**~~ **CLOSED, Sept 2026 — decision only; the edit was not actually made
   until 5 Sept 2026, when the arrow was found still reading `→ 36`. It now
   reads `→ 30, Part I` and chapter 15 verifies `identical`.** **An item
   recorded as closed is one nobody looks at again, so a decision must not be
   written up in the past tense of the work.** The back-port rule exists because
   `mkbody.py` regenerates bodies downward and destroys artifact-only edits.
   Chapter 15 has **no body and no generator**, so there is nothing upstream that
   could destroy the edit — this is the one case where editing a built page is
   safe, and it is not a precedent for any page that has a source. Conditions:
   assert on match count before writing, grep for the new string after, re-run
   `debuild.py verify` on chapter 15 and expect `identical`. `linkindex.py` does
   **not** need re-running — the page is edited in place, not rebuilt. Left
   unfixed, chapter 15 sends a reader to chapter 36, which is Provisorietiden and
   cannot carry the West Indies. The original entry follows.

   **Chapter 15's forward arrow is knowingly stale.** `15 → 36` should be
   `→ 30, Part I`. It was not fixed in the Part G ledger pass because there is no
   `c15_body.html` — Part D has no authored bodies in `files/` — and editing a file
   the build does not read changes nothing. Fix it at the next Part D rebuild, which
   Part D needs anyway for items 3 and 4. It points into Part I, so nothing shipping
   now depends on it.

13. ~~**`overruns()` in `mapspine.py` also carries 5.55.**~~ **CLOSED, August 2026,
   and the item's premise was wrong in both directions.** No figure script calls
   `emit()`. All seven define a local `overruns()` and call `M.rasterise()` directly,
   so `mapspine.overruns()` never reached a Part G figure and correcting it alone would
   have changed nothing. Six of seven already used 6.1; **`figs_25.py` alone still had
   5.55**, so item 10's claim was wrong about exactly one script rather than all of
   them. Both are now 6.1. Chapter 25's two figures were re-checked under both
   constants and overran under neither, so nothing shipped off the canvas.

   **What the item missed entirely.** `overruns()` tests width and nothing tested
   height. A sweep of all 24 figures found `svg_band.txt` with its last caption line at
   `y=430` in a 430-high canvas — cut off, invisible to the XML validator and to the
   width guard, and caught only by rasterising and looking. `mapspine.overflows()` now
   makes that check, `emit()` calls it, and all seven figure scripts call it. 24
   figures: 0 horizontal, 0 vertical.
14. ~~**The built word counts disagree with the tables in State.**~~ **CLOSED,
   August 2026. Both are right; they measure different things.** On byte-identical
   input the build's count and `bookstats.py`'s **`page`** agree exactly — chapter 24
   at 6,714 both ways, delta zero. The gap is `page` against **`text`**: 215 words of
   rail, contents list and inlined `rail.js`. ~~The tables in State record `text`; the build prints `page`.~~ **This half is
   wrong** (found Sept 2026): the State tables held old **page** counts, not `text`.
   Chapter 24 was listed at 7,014 against a text count of 6,394. Both tables have
   now been replaced with measured page and text figures.

   **One thing follows and is not yet decided.** The `about N minutes` stamped on every
   shipped page is computed from `page`, so every chapter overstates its reading time by
   about a minute — and the rail and the contents list are the same list counted twice.
   Switching the stamp to `text` would move some chapters against the 30–42 advisory and
   is a change to shipped pages, so it is Carsten's call.
15. **`c21`'s "chapter 32" was stale by one and is now "Part H".** Under D-2 the
   mechanical answer was 33, but Part H is unplanned, so a number there would have been
   invented. D-1's reasoning was applied to prose as well as to arrows.

16. **Four content calls left open in the Part G build**, each because deciding it
   would mean asserting something unsourced:
   - **`figs_31.py`'s ceiling bar.** `CAP_EXCHANGE` 27 + `CAP_WAR` 15 = 42 under a
     caption reading 46 million rigsbankdaler. Four million — 9% — is neither drawn
     nor labelled, and unlike the "fallen to 6%" bar two blocks above it the ceiling
     bar has no full-width track, so it reads as a complete quantity. Either the
     balance gets a third labelled segment, which means naming what it was for, or the
     bar gets a 46 m track so the shortfall is visible.
   - **`figs_27.py`'s schools figure.** Headline 241 built against 240 planned, with a
     side note reading "a thirteenth district on Møn from 1726, ten more schools". A
     reader adding up gets 250 or 251. The `aria-label` says 241 and never mentions
     Møn, so the accessible and visual versions of the figure disagree.
   - **The Marie Grubbe vignette is in the wrong section.** It sits at the foot of
     chapter 27 §05, "Tordenskjold", but her scene is the summer of 1711 and what
     strands Holberg at her ferry house is the plague — §04. With the new Wessel
     vignette in §05, that section now carries two and §04 none, one of them out of
     its own chronology.
   - **The stavnsbånd mechanism is stated in halves in four places.** See item 17.

17. ~~**The 1788 mechanism is stated in halves.**~~ **CLOSED, August 2026.** All four
   passages now carry all three mechanisms: chapter 29 §08, the band figcaption, the
   Summary and the checkpoint prose. The wording came from the review pass and was
   back-ported into `PART_G_DRAFT.md`, so it survives a rebuild. The original finding,
   kept because `STATE_G.md` §5 still needs correcting: The ordinance text settles it and both drafted versions are half-right.
   §2 ends the bond entirely from 1 January 1800; those already too old for war
   service, and those discharged from it, get freedom passes **at once**; the bound
   band reverts to 14–36; **and then one cohort is released in each following year**.
   So `svg_band.txt`'s caption ("did not free anybody at a stroke") has the first half
   and chapter 29 §08, its Summary and `svg_column.txt` ("by cohort, over twelve
   years") have the second. Neither is false. `STATE_G.md` §5's reason for dropping the
   cohort staircase — "the ordinance did not release men by birth year" — **is** false;
   it did, after the reversion. The staircase was still right to drop, but because it
   would have shown only the annual cohorts and hidden the reversion and the immediate
   passes. Fixing this means making all four passages carry all three mechanisms, which
   is a rewrite of drafted prose and was left alone.

18. **Part G's checkpoints were converted from prose to questions.** The draft wrote
   them as prose recaps — "three things are worth holding". Every part from A to F uses
   three retrieval questions and `.check` in `style.css` is written for a list, so
   `build_part_g.py` carries 63 questions derived from the draft's prose. If the prose
   form is wanted it is a change to six shipped parts, not to Part G. Recorded because
   the drafted prose is good and is now unused.

   **Chapter 30's third checkpoint had nowhere to go.** Drafted "after §10", the last
   narrative section, with no following heading to anchor to and no page left to check
   back over. It is anchored on §10 instead, so it appears after §09 and sets up the
   1792 ordinance rather than recapping it. The drafted prose for it — "was Denmark
   first" against "was Denmark good" — makes the chapter's closing argument and belongs
   in the myth-check or the summary.

19. **Part G's apparatus is short in two places, left visible for the reviewer.**
   The glossary covers **38 of 67 sections** (25: 5 of 9 · 26: 6 of 10 · 27: 7 of 9 ·
   28: 7 of 10 · 29: 4 of 10 · 30: 4 of 10 · 31: 5 of 10), against chapter 24's one
   block per section. And the Summary runs to **four items rather than five** in
   chapters 25, 26 and 27, so `ol.five` renders 01–04. Neither was papered over:
   inventing glossary entries or splitting a paragraph to reach five would hide a
   drafting gap in the built page.

20. ~~**Chapter 28 builds at 46 minutes**~~ **CLOSED, Sept 2026. Retired as a
   split candidate, and the diagnosis in this item was wrong.** It builds at **43**,
   not 46. Halved it gives two chapters of 21 minutes, both under the floor, so
   splitting is not division but a commitment to write ~5,000 new words into a
   shipped and verified part. Its candidacy rested on topic count; it has ten
   sections, which is the standard heavy shape in Part G — 26, 29, 30 and 31 all
   have ten. **It is not exceptional on the metric its candidacy rested on.** See
   L13 for what the measurement actually shows. Chapters 21 and 32 are retired for
   the same reason; the book stays at 43 chapters and nothing renumbers. The
   original entry follows.

   **Chapter 28 builds at 46 minutes** — inside the 25–50 band, outside the 30–42
   advisory, and flagged by the build. It is the longest in the part by 1,400 words and
   was already a split candidate. Splits get two numbers at plan time, so this is
   Part H's planning session, not a change to make now.


21. **Chapter 29's second vignette is malformed in the shipped body.** The heading
   reads `**Vignette · Johann Friedrich Struensee, Christiansborg, before dawn on
   17` — truncated mid-date and carrying a literal `**`. The `date` field has
   swallowed a sentence about Caroline Mathilde's arrest and `opens` reads
   `January 1772**`. Something in `c29_body.html` has a line break inside the
   vignette heading. **The page round-trips cleanly, so no automated check will
   ever find it.** Fix in the body and back-port to `PART_G_DRAFT.md`.

22. **Chapter 23's first vignette has no place.** Ellen Marsvin's `place` field
   reads `1629`, and it appears in the place census as though it were a location.
   The `person · place · date` form is broken there.

23. **Chapter 29 needs a `→ 35` added.** Chapter 35 inherited no forward arrow from
   any shipped chapter, although Part G set up its ancestry directly: the
   freeholders created by the 1788 reforms are chapter 29's subject and the
   cooperative movement's grandparents. Add to `c29_body.html` and back-port
   **before** any Part G rebuild.

24. **CLOSED at the Part I planning session.** ~~The forward arrow to 1953 has no
   part letter.~~ The premise was wrong: **1953 is inside Part I, not beyond it** —
   Part I already ran to 1953 under the old spine. The arrow did not need a new
   part letter, it needed the one its two neighbours in the same block already
   used. Fixed in `c36_draft.md`, body regenerated by `mkbody.py`, page rebuilt:
   the 33-word italic exception note comes out with it, chapter 36 drops 34 page
   words to 7,642 and from 37 minutes to 36, and `debuild.py verify` reports every
   other chapter unchanged. **The symptom was predicted before the edit and came
   out to the word.**

25. **`svg_plague_1711.txt` is missing and *does* have a generator.** Wanted by
   chapter 27, remade by `figs_27.py`. Chapter 27's page is unaffected because the
   SVG is inline, but `files/` cannot currently rebuild it. The only regenerable
   artifact missing from the tree; everything else `tidy.py` lists is Part D's ten
   unrecoverable figures.

26. **`pagewords.py` sits beside `pagecount.py`** and is unclassified by `tidy.py`,
   while this ledger names `pagecount.py` as holding the only definition. Probable
   superseded duplicate. `tidy.py` finding 5 applies: check before deleting either.

27. **`vignettes.py` place matching is exact-string and under-reports badly.** It
   reports Copenhagen five times. Counting variants — *Copenhagen castle*, *outside
   Copenhagen Castle*, *the great hall, Copenhagen Castle*, *Copenhagen's rådhus*,
   *the square before Copenhagen Castle*, *Blåtårn*, *Flådebatteri nr. 1,
   Kongedybet*, *Nørregade* — the true figure was **thirteen of forty-eight**.
   ~~thirteen~~ **Recount, Sept 2026: fourteen of fifty-one after chapter 32, and
   fifteen of fifty-four after chapter 33. See item 44.**
   Normalise the match. It also checks no balance at all: see D-9.

28. **The advisory constant is hardcoded in three scripts, not six.** `build_all.py`,
   `build_part_f.py` and `build_part_g.py` carry `TARGET`. `build_parts_abc.py`,
   `build_part_d.py` and `build_part_e.py` compute and stamp a reading time but
   never judge it against anything — no `TARGET`, no `BAND`. Moved to 28–40 on
   5 Sept 2026; nothing was missed, because there was nothing there. Unrelated and
   also unrecorded: `build_all.py`'s `PARTS` list contains only A–C, D and E, so
   it does not build F or G at all.

29. **Cosmetic, low priority.** Four Meanwhile summaries in `vignettes.py` output
   terminate at a regnal ordinal — "The years Christian 4.", "In September 1683,
   while the commissioners of Christian 5." A first-sentence splitter breaking on
   the period in the ordinal, not damaged prose; entries truncated by length carry
   an ellipsis and these do not, which makes the report look corrupt when it is
   not. Separately: maps 1600 and 1660 both sweep exactly 3,108 land points,
   probably a shared envelope, worth one look given what the fixture is for.


---
30. **`linkindex.py` and `debuild.py verify` contradicted each other, and the
   project had been resolving it by skipping step two.** `linkindex` is a
   post-processor: it adds two links back to the index to a finished page, a crumb
   span and a footer tail, neither of which a retained body has ever seen. So any
   page taken through the documented sequence — build, `linkindex`,
   `index_generator`, upload — drifted against its own source by construction, and
   every chapter with a body reported `BODY DRIFT`. This never surfaced because
   `linkindex` was not re-run after the Parts E–G rebuilds. **Chapters 16–31 had
   been shipping with no index links at all.** Running it as documented turned the
   whole book red at once. Fixed Sept 2026: `_normalise` in `debuild.py` now strips
   the two link forms alongside the checkpoints and the reading-time line — a sixth
   injection added to the five it already knew about. Verified: 01–11 `style-only`,
   12–31 `identical`.

31. ~~**`svg_plague.txt` holds the wrong figure**~~ **CLOSED, Sept 2026** — `recover_svg_plague.py --replace` restored chapter 15's Black Death map from the shipped page, the two files no longer collide, and `figcheck` reports 0 stale. Part D still cannot rebuild, so nothing ships from it yet, but the landmine under open item 4 is gone. Original entry follows.

   **`svg_plague.txt` held the wrong figure, and every existing guard passes
   it.** `figs_27.py` once wrote its first figure to `svg_plague.txt`. That is
   chapter 15's filename: `build_part_d.py` maps `SVG_PLAGUE` → `svg_plague.txt`
   for the Black Death arrival map. The script was renamed to write
   `svg_plague_1711.txt`; nothing put chapter 15's figure back, and the two files
   are now byte-identical copies of the 1711 Copenhagen panel. `tidy.py` sees a
   file that exists and that a build script wants — findings 2, 3 and 5 all pass.
   `debuild.py verify` never opens a figure source, and chapter 15's body holds
   `{{SVG_PLAGUE}}`, a placeholder, which cannot disagree with anything. It has not
   shipped only because `build_part_d.py` cannot run at all (item 4). **The day
   item 4 is fixed and Part D is rebuilt, chapter 15 loses its figure silently, in
   a part with no retained bodies to restore from.** `recover_svg_plague.py`
   extracts the surviving copy from the shipped page and refuses to overwrite
   without `--replace`. Decision pending. `figs_27.py`'s docstring now carries a
   warning against pointing it back at that name.

32. **`figcheck.py`, new Sept 2026.** Compares the SVG inlined in each shipped
   page against what its generator currently produces — the gap that let chapter
   27 carry a superseded schools figure while `verify` reported `identical`
   throughout. Figures are matched by **aria-label**, not by filename guessing: the
   first version of the script matched on substrings and cried `STALE` forty-two
   times, all of them Parts A–D figures with no source on disk. Current state: 48
   matched, 41 sourceless, 0 stale. It found item 31 on its first clean run, by
   noticing two files claiming one identity. **Parts A–C reference no figure
   sources at all** — `build_parts_abc.py` contains not one `svg_*.txt` — so
   thirty-one figures exist only inside their pages. That is expected, not a fault,
   and the count is printed so a change in it is visible.

33. **Do not commit an SVG that has been through a download.** Two `.txt` figure
   files handed over as downloads came back carrying an injected **C2PA
   content-credentials manifest**: 7,736 bytes of base64 welded into the `<svg>`
   root, the same on both files, invisible in a diff viewer. It does not corrupt
   word counts — `pagewords` strips whole `<svg>` blocks — and the file stays
   well-formed, but it would have inlined 15.5 KB of base64 into chapter 27 and
   made `figcheck` flag it in perpetuity. **Anything generated should be
   regenerated locally rather than round-tripped.** That covers every `.html` page
   as well: they are build outputs. Source edits travel as a patch script instead;
   see `apply_session_h1.py`, which was verified by applying it to a pristine clone
   and rebuilding — byte-identical to the tree it was written from.

34. **Chapter 12 will flag as too long under the new advisory, on a number that is
   wrong.** `build_all.py` reads the `about N minutes` stamp off the page rather
   than recomputing it, so for chapters 01–15 it judges pre-fix figures. Chapter 12
   stamps 41; its corrected page count is 8,335 words, which is 40 and inside
   28–40. It has no body and cannot be rebuilt to clear the stamp. Changing
   `build_all.py` to judge the recomputed count is a few lines and would also make
   chapter 10 flag low at 27, which is a real signal on a real number. **Left alone
   by decision, Sept 2026.** Recorded so it is not rediscovered as a fault.

35. **Chapter 32's plan needed nine corrections, found by research.** Recorded
   because the pattern is now four parts old: §01 dropped Lauenburg from the
   German Confederation and missed the 2.6 million daler that came with the swap of
   4 June 1815; §03's vignette placed Skræppenborg near Kolding in the early 1840s,
   after he had moved there and grown rich, when the prosecutions and the fines
   were the 1830s on Funen; §04 called the censorship individual and lifelong when
   it was automatic under the 1799 ordinance and lasted eleven years; §05's
   vignette put Pätges at Det Kongelige Teater when the 12 February 1826 evening
   was at the Hofteatret; §06's title said 1831–1835 when Viborg and Slesvig did
   not sit until 1836; §08 had no date for Bondevennerne (5 May 1846) and no cause
   (the Bondecirkulære of 8 November 1845); §09 omitted that Hiort Lorenzen's
   demonstration was planned by Flor; §10 dropped Lauenburg again and missed that
   the Open Letter refused the Ejderpolitik in the same breath as the Augustenborg
   claim. Only the ten-section structure and the 18-month closing interval survived
   unaltered.

36. ~~**Two data gaps block figures in chapter 32.**~~ **PARTLY CLOSED, Sept 2026.** Figure (b) is built: Schleswig's 44 came from the published 1836 membership list, and Holstein's 48 is COUNTED from the 1835/36 list rather than taken from the decree — the figure says `counted, not decreed` on its face and `figs_32.py` records what would close it. Figure (c) is REPLACED: the Zealand kapitelstakst exists in Statistiske Meddelelser 4. Raekke, 15. Bind, Haefte I and was not obtainable, so the figure draws the attested ratios and a chronology and states that the series exists and is not plotted here. Both remain worth closing properly. Original entry follows.

   **Two data gaps blocked figures in chapter 32.** Figure (b) needs the Slesvig
   and Itzehoe seat counts; Roskilde (70 = 60 elected + 10 royal) and Viborg (55 =
   48 + 7) are sourced and the arithmetic reconciles. Figure (c) needs the
   year-by-year values of the Zealand *kapitelstakst* for a tønde of rye, 1815–48,
   after Scharling; the series is published and **there is a currency break at
   1813/14**, so the chart must not be extended back across it. Neither is a
   judgement; both are document fetches.

37. **Adding a token to `style.css` requires the exact `"; "` spacing, or
   `debuild.py`'s drop list silently misses it.** Part H needed a band colour, so
   `--slate:#4F6470` went in beside `--indigo`. The first insertion was
   `--indigo:#2F4C7A;--slate:...`, without the space. `debuild` drops tokens the
   page never had by matching `(--[a-z]+:#[0-9A-Fa-f]{6}; )` — with a trailing
   space — so removing `--slate` from the reconstruction left
   `--indigo:#2F4C7A;--band` where all thirty-one shipped pages have
   `--indigo:#2F4C7A; --band`. One character. **Verify went from 20 `identical`
   to 31 `style-only` in a single edit**, and the only reason it was caught in
   minutes rather than shipped is that `build_part_h.py`'s docstring had been
   written to predict exactly that symptom before the token was added. Corrected;
   back to 21 `identical`, 11 `style-only`. Write the prediction down before
   making the change, not after.

38. **`files/danish-history-index.html` was a corrupt shadow of the real index,
   committed.** It announced **"0 pages written"** and marked all forty-three
   chapters unwritten, because it had been generated in a folder holding no
   chapter pages — open item 2's container-path bug, fossilised. The live index is
   at the chapter-folder root, which is where `index_generator.py` writes and what
   every page links to. `tidy.py` finding 5 could not see it: that check compares
   names within `files/` only, and this was the same name in two directories.
   Finding 5 now walks both. **Delete `files/danish-history-index.html`** — it is
   tracked, so git keeps it.

39. ~~**Figure output is not byte-identical across machines.**~~ **CLOSED, Sept 2026 — NEGATIVE ZERO.** `"%.1f" % -0.00004` is `-0.0` and `"%.1f" % 0.00004` is `0.0`, so a coordinate that rounds to nothing keeps the sign of the float beneath it, and that sign is not guaranteed to match on two machines. Eight of them accounted for the entire 109,561-versus-109,569 discrepancy in `map_1814.py`. Fixed in both formatters — `mapspine` and `mapkit` — by adding 0.0 after rounding. All six maps and all 51 figures now regenerate byte-identical on both machines, verified against a fresh clone. Blast radius was eleven stale figures, all in chapters 16 to 32, every one with a retained body; nothing in Parts A to D, which cannot be rebuilt. **Check that before applying a change of this shape, not after.** Original entry follows.

   **Figure output was not byte-identical across machines.** `map_1814.py`
   produced 109,561 characters in the container and 109,569 on the Mac, from the
   same source and the same atlas. Coordinates are formatted `%.1f`, which is
   deterministic, so it is not float drift and the cause is not established.
   Consequence, and the reason it does not matter much: the generated figures that
   go into the pages are the ones generated on the machine that runs the build,
   and `figcheck.py` compares page against disk on that same machine, so both
   sides agree. **It is a further reason never to hand over or commit a generated
   file** — only the generator. See item 33.

40. **`cairosvg` is not installed on the Mac, so `M.rasterise` writes nothing
   there and every figure script prints that figures were NOT visually checked.**
   The three chapter 32 figures were rasterised and looked at in the container
   instead, and looking caught two faults no guard did: a two-column layout in
   `figs_32.py` where the left column printed straight through the right one while
   both sat inside the canvas, and three colliding labels on the 1814 map.
   `overruns` tests the canvas edge and nothing else; **there is no collision
   guard**. `mapdump.py` builds a browser contact sheet without cairosvg and is
   the fallback until `brew install cairo && pip3 install cairosvg` is done.

   Measured while fixing it, off the raster rather than assumed: **mapt 5.68,
   mapx 5.63, mapl 6.98 units per character.** The single 6.1 the guard used was
   conservative for the two small classes and **too small for `mapl`**, so a long
   heading could overrun unflagged. RESOLVED Sept 2026: `mapspine.CHAR_W` now
   carries the measured value per class, with no percentage margin on top and a
   fixed six-unit cushion at the canvas edge instead. Re-measure if style.css
   changes a font-size or the --mono stack; do not adjust by eye.

41. **The guards existed and were not connected.** `figs_23` through `figs_32`
   called `validate` and `overruns`. They did not call `overflows` — written after
   chapter 29's stavnsband figure shipped a caption cut off at the canvas edge —
   and the **eleven map scripts called none of them at all**, so no territorial map
   in the series had ever been width-checked. All four now run from a single
   `check()` inside `mapspine.rasterise()`, which every script already calls, and
   **before** the cairosvg availability test, because otherwise the checks are
   skipped on exactly the machine that has no rasteriser and therefore cannot look
   instead.

   It found the stavnsband fault repeated. `svg_invasions.txt` had its second
   caption line at baseline y=462 in a 452-high canvas, so chapter 23 had been
   shipping the figure **without its final sentence** — "Neither crossed the
   water, and neither had to: taking Jutland was enough to dictate terms both
   times", which is the whole point of a two-panel comparison. Canvas raised to
   472, chapter 23 rebuilt, looked at. **A guard that is written and not wired in
   is worth nothing**, and this one cost three years of figures.

42. **`collisions()`, new: two pieces of text printing through each other.**
   Nothing tested for this, which is how a two-column layout in `figs_32.py` got
   through every check with the left column running to x=423 straight across a
   right column beginning at x=380 — both comfortably inside a 700 canvas.
   `overruns` tests the canvas edge and nothing else.

   Two things learned building it. Text inside a transformed group is in a
   different coordinate space, and the first version compared raw coordinates and
   reported the 1807 figure's subtitle as colliding with a map label 52 units
   away; it now tracks `translate()`. And **a percentage margin on a
   per-character estimate compounds with line length** — at five per cent above
   measured, a 149-character line in `svg_titles.txt` accumulated forty units of
   phantom width and was reported as overrunning a canvas it fits inside. The
   cushion belongs at the canvas edge, where it is a fixed six units and does not
   grow with the sentence.

43. ~~**Open, cosmetic, needs a decision.**~~ **CLOSED, Sept 2026.** Both labels
   moved and chapter 25 rebuilt. **The positions were solved, not nudged.** A
   label moved off a collision can land outside its own province, which is a worse
   fault than the one being fixed and one no guard tests for, so candidates were
   required to satisfy two conditions at once: point-in-polygon inside the label's
   own territory, and collision-free on regeneration. `Skåne` moves from
   (14.15, 55.62) to **(14.00, 55.40)**, still inside `SCANIA`; `Jämtland`
   from (14.15, 63.35) to **(14.30, 63.10)**, still inside `NO_LOST` and well
   north of the Härjedalen label. An earlier candidate that cleared the
   collision handsomely, Jämtland at (15.40, 63.20), was rejected because the
   membership test put it **outside `NO_LOST`** — it would have printed the name of
   a lost Norwegian province onto uncoloured Sweden. Nothing now fires anywhere in
   the book: all six map scripts run clean, fixture and seam layer pass, chapter 25
   rebuilds and verifies `identical`, and the map was rasterised and looked at.
   Original entry follows.

   **Open, cosmetic, needs a decision. `svg_terr_1660.txt` prints Helsingborg
   and Skaane into each other**, and Jamtland into Trondhjem, by 28 and 17 units.
   Found by the new collision guard on a map that has been shipped since Part F.
   It is legible but wrong, and fixing it means nudging two labels in
   `map_1660.py` and rebuilding chapter 25's page. Left alone deliberately rather
   than folded into an unrelated pass.


63. **There were three implementations of "how many words is this page", and two of
   them disagreed.** `pagecount.py` opens with a docstring explaining that it exists
   because the rule had been copied into seven files and drifted. `pagewords.py` sat
   beside it as a second copy, and `narrative.py` reimplemented the token test inline
   as a third. `bookstats.py` imported `pagewords`; `narrative.py` imported
   `pagecount`; **across the 36 built pages `pagecount` read 42 words high on
   average, up to 58** — free-standing punctuation from the inlined rail script,
   which `pagewords` excludes and `pagecount` did not. `bookstats.py`'s own docstring
   said it imported `pagecount`, and it did not. This is precisely the failure
   `pagecount.py` was written to prevent, recurring inside the fix.

   Fixed at the Part I planning session. `pagewords.py` is the one implementation and
   now also exposes `body_after_style()` and `words()`; `narrative.py` imports it;
   `pagecount.py` is a shim that re-exports, kept so that removing it is a separate
   decision. The two now agree to the word on every page. **Report-only code; no
   artifact could change, and none did.**

64. **The plan's weight bands and the verifier's weight bands were different
   scales.** `narrative.py`'s `band()` was a fixed `<340 / <560 / <760`, which was
   neither `PLAN_G`'s bands (318/454) nor `PLAN_H`'s terciles (358/492). Chapter 36
   measures 4L/5M/1H on the old tool scale and 3L/3M/4H on the plan's — the same
   chapter, two verdicts, and only the second would have caught the 5L/5M/0H first
   draft that item 59 is about. **Item 59's rule was unenforceable while this held.**
   `band()` now carries the pooled terciles of the 118 measured sections of Parts G
   and H (336/471), which is the scale `PLAN_I` is written in, and `PLAN_I` quotes
   `band()` rather than restating numbers.

65. **Ærø (item 48) is now on Part I's critical path.** Chapter 38 wants a map of the
   1920 plebiscite zones — the eighth map, and the only new one Part I needs. It
   inherits `DENMARK`'s vertex list, which is what fixing Ærø edits. **If Ærø is to
   be fixed at all, fix it before the 1920 map is built rather than after**, or the
   fix propagates into five maps instead of four.

66. **The scanned back-catalogue on `dst.dk` fetches, with OCR text.** The 1954
   unemployment volume of *Statistiske Meddelelser* (4. række, 160. bind, 4. hæfte)
   yields annual average unemployment percentages directly, and lists its
   predecessors by series and volume: 1910–40 in five-year volumes, 1940–53 annually.
   **The annual unemployment series 1910–1954 is obtainable**, which is the first
   genuine time series available to this book and the answer to item 60 for at least
   two figures. Three qualifications: the OCR is lossy and visibly so — the column
   headers of the very table used render 1952 as "1962" and 1945 as "1946", so every
   digit needs a second appearance before it goes into a figure; only that one volume
   has been fetched, and the identifiers for the earlier ones are still to be found;
   and the container's own network cannot reach `dst.dk`, so the numbers travel as a
   cited literal block and everything derived is computed.

   **This bears on items 53 and 60.** Both wanted material published by the same
   department in the same series. Neither has been confirmed present, but the
   probability has changed enough that **the library trip should wait until the fetch
   route has been tried on them.** If they are there, four figures across Parts G and
   H that were honestly redrawn as something else become redrawable as planned.


67. **`mkbody.py` silently dropped a `Meanwhile in Europe` block, and the diagnostic
   said everything was fine.** The placement is `mw_at = {secs[2]: 0, secs[6]: 1}` —
   a two-key dict. Chapter 37's draft carried three blocks; `meanwhile_html()` built
   all three and the page emitted two. The count printed by `mkbody` counts
   `class="meanwhile"` in the OUTPUT, so it reported 2, which is what a correct
   chapter reports. Every chapter from A to H happened to carry exactly two, so this
   has been latent since the function was written. **A build step that discards
   authored prose without saying so is the worst class of fault in this toolchain**,
   because the draft and the page disagree and nothing compares them. Fixed by a
   guard that refuses the build and names both numbers. `mw_at` STILL HOLDS TWO —
   generalising it to place N blocks is a layout decision and was not taken. Chapter
   37 was cut to two (the Norway/Sweden block went; Washington and Petrograd/Berlin
   stayed).

   Writing that guard I reached for `num_arg`, which does not exist in `build(n)`.
   It would have raised `NameError` at the one moment it was needed. Caught by
   predicting the symptom before running it, which is the rule paying for itself.

68. **A draft-level narrative counter exists, and its bias is not constant.**
   `narrative.py` measures built pages, so it cannot run until the part build script
   and the `HAND` entry exist — by which time the prose is written and the weight
   profile is expensive to fix. For chapter 37 the profile was measured from the
   markdown instead, using `narrative.py`'s own definition (section prose minus the
   vignette blockquotes), calibrated against chapter 36 where the built answer is
   known. **It is reliable for band classification and not for totals.** Calibrated
   on 36 it ran 22 words low; on 37 it ran 51 low. Every section landed in the band
   it predicted, and the projected page-word total was 110 out. Use it to catch an
   L1 profile early; do not cut prose against it.

69. **`grep` is not a valid post-replacement confirmation on hard-wrapped prose.**
   The standing rule is "assert on every scripted replacement, then grep for the new
   string." On a markdown draft wrapped at 80 columns, any inserted string longer
   than a few words spans a line break, and a line-oriented `grep` returns 0 for a
   replacement that landed correctly. This fired once in the chapter 37 session: the
   assertion was true and the grep was the liar. Worse than the false alarm is the
   false confidence in reverse — a replacement that genuinely failed would look the
   same. **Confirmation must be whitespace-normalised** (`re.sub(r'\s+', ' ', text)`
   on both sides) or the rule is checking nothing.

70. **A cell grid must round, and must assert what the shaded cells claim.** Chapter
   37's figure 3 draws a hundred-square grid, one square per hundred merchant
   seamen, shading the share who died. 702 of 10,000 is 7.02 per cent, and
   `i < rate * 100` shades EIGHT cells. The chart said 800 men where the number is
   702. Nothing in the guard suite can see a chart that lies — `collisions()`,
   `overruns()` and the XML parse were all satisfied. The script now rounds and
   asserts that the shaded cells misstate the number by less than one cell. **Any
   future proportional-cell figure needs the same assertion**, and the general rule
   is that a figure's arithmetic needs a guard of its own because the layout guards
   cannot reach it.

71. **Undefined SVG text classes fail silently and only rasterising catches them.**
   `mapspine` defines exactly three: `mapt`, `mapl`, `mapx`. Chapter 37's figures
   were first written against `maph`, `mapc` and `mapn`, which do not exist. An
   undefined class is valid SVG, so the XML parse passed, `M.check()` passed, and the
   text rendered at the browser default of 16px sans and ran off the right edge of
   all three figures. **The only thing that found it was looking at the PNG.** This is
   the fourth distinct fault class in two parts that is invisible to every automated
   check and visible immediately on rasterising, alongside items 47, 50, 61 and 70.
   Rasterise-and-look is not a courtesy step.

72. **L1 has now held for five consecutive chapters and item 59's condition is met.**
   Chapter 37's first draft came in at 3,529 narrative words against a 4,053 budget,
   profile 6L/3M/1H — short, and with one heavy section where the plan wanted three.
   The cause was five missing subjects, not thin paragraphs: how the 1915
   constitution actually passed, the Social Democrats' convergence with the Radicals,
   the strategic geometry of the Belts, the rationing arithmetic, and the three
   islands' separate economies. Naming them took less time than writing them.
   **L1 should be promoted from observation to rule**: a first draft landing more
   than ~400 short is missing a subject, and the correct response is to ask what
   subject, never to thicken what is there.

73. **§14.5 is answered: items 53 and 60 are both reachable, and the library trip is
   retired.** The `dst.dk` route of item 66 works on both series. *Kapitelstakster*
   and *Valg til folketing og landsting og rigsdag* are named series inside the
   digitised 1852–1959 window. For item 60, a bibliography inside 4. rk. 35. bd.
   names every Folketing election volume: 1869/1872/1873 → 2.R. 12.Bd. H.III;
   1876/1879 → 3.R. 3.Bd. H.II; 1881/1884 → 3.R. 8.Bd. H.I; 1887/1890/1892 →
   3.R. 13.Bd.; 1895/1898 → 4.R. 3.Bd. H.IV; 1901 → 4.R. 10.Bd. H.II — six hæfter
   for the whole span. For item 53, *Det Statistiske Departements Publikationer*
   carries a year-by-year reference list from 1850 to 1917 and beyond in
   `række,bind,hæfte` form, and individual volumes carry ready-made 5-, 10- and
   20-year means. Separately, Scharling's *Pengenes synkende Værdi* (1869) gives the
   Zealand rye kapitelstakst as a continuous series 1651–1850, which is closer to
   what chapter 32's figure wanted than the annual hæfter are.

   **Identifiers located, tables not transcribed.** The OCR caveat of item 66 stands
   in both series. **Chapter 37's figure 1 is the first casualty of the gap**: the
   plan wanted the electorate before and after 1915 by category, the volume is
   located and was not fetched, and the figure was redrawn as the seven categories
   with their admission dates. It should be drawn as planned as well, not instead —
   see the docstring in `figs_37.py`.

74. **PLAN_I names all eight chapters and never names Part I.** The crumb, the footer
   and the index all need a band title. **"The small state"** was chosen at build
   time and is `BAND_TITLE` in `build_part_i.py`, one line, flagged in the docstring.
   The band colour is `--moss:#4A5A46`, added to `style.css`; `debuild.py`'s drop
   list is generic over `--name:#hex; ` tokens, so adding it did not disturb any
   shipped page — verified 11 style-only (01–11) and 26 identical (12–37) after the
   build. The warning in `build_part_h.py`'s docstring about the drop list can be
   treated as discharged.

75. **Chapter 37 shipped at 7,902 page words and 38 minutes against a planned 7,839
   and 37.** The profile is 3L/4M/3H, exactly as PLAN_I §5 specified. About 190 words
   were cut in three passes chasing the 37-minute line, which holds to 7,874 page
   words; the last 28 were not taken, on the judgement that the prose was already
   tighter than was good for it and the remaining gap is a boundary in
   `round(w/210)` rather than a real difference.

   **CORRECTED, chapter 38 session.** This entry first recorded 7,896 and a
   remaining gap of 22. 7,896 is `build_part_i.py`'s count, printed BEFORE
   `linkindex.py` adds the index links; `bookstats.py` on the shipped page gives
   7,902. The outstanding cut to reach 37 minutes is therefore 28 page words, not
   22, and chapter 37 is 63 over plan, not 57. This is the exact fault the
   START_HERE prompt warns about, committed in the entry that exists to record a
   measured decision. **Take every length from `bookstats.py`, after linking.** **Chapter 33's 41-against-40 is a
   different case** — that was a ceiling, and PLAN_I sets no ceiling for 37. Flagged
   here so the ledger records a decision rather than a drift.


## What Part G taught

**Verify before writing, not after.** Nearly every section researched during Part G
turned up a load-bearing claim that would otherwise have gone in wrong: Nansen's
proposal was a month out, the matrikel of 1662–64 measured nothing, Griffenfeld's
chancellorship was a year out, the Kongelov's secrecy was overstated, the abolition of
vornedskab was gradual rather than immediate. None of these were obscure details —
each was the central claim of its section, and each read perfectly plausibly before it
was checked.

**The worst error survived nineteen plan revisions.** A vignette had Friederike Brun
watching the bombardment of 1807 from Sophienholm. She was living in Rome from 1807 to
1810. It was caught only because the *setting* was being verified, not the claim, and
it had been reviewed repeatedly without anyone doubting it.

**An assertion that aborts leaves the file unwritten while later commands still print
success.** This produced three consecutive false confirmations on `map_1721.py`.
Assert on every scripted replacement *and then grep for the new string*. The assertion
prevents the bad write; only the grep proves the good one.

**When a planned figure needs numbers the sources do not supply, change the figure.**
Five of Part G's twenty-one diverge from the plan for that reason and each says so in
its script's docstring. A weekly mortality curve invented for real deaths, or a
plantation plat with invented lot sizes, would have been the worst failures in the
part. What replaced them — the spread of published death tolls shown disagreeing, the
archive asymmetry of a slave ship's papers — carried more than the originals would.

**The ledger catches what reading cannot.** The `25 → 27` arrow promised vornedskab
and the chapter never mentioned it; that was found by checking the debt table against
the draft, not by reading the draft.

---

## What Part F taught

**A verifier can pass while three maps print a dark stripe.** `mapfixture.py` had
three layers and all three passed for months while Denmark and Slesvig overlapped
by up to 27 km at the Kongeå, Ditmarschen sat 3–4 km north of the Eider, and
Holstein poked into Slesvig. Both fills are translucent, so the lens printed
*darker than either territory* — a stripe across Jutland on 1397, 1500 and 1600,
two of them already shipped.

The reason the sweep could not see it: **a fault shaped like a thin band along a
border is invisible to any affordable grid.** GRID is 0.2° and the lens is 0.04°
thick. Finer grids do not fix this; a different *kind* of test does. Where two
neighbours share a border, neither may have a vertex strictly inside the other —
exactly the property `map_1397.py` had been stating in prose for Norway and Sweden
("copied exactly; do not tidy them apart") without ever checking it. That is
`seamcheck.py`, now the fourth layer of the fixture, and it self-verifies: restore
the old Ditmarschen and it reports two faults, put the fix back and it reports
none.

When a seam does disagree, **decide which line is authoritative rather than
splitting the difference.** At the Kongeå it is Denmark's, because that polygon
carries the design intent in its comment; at the Eider it is Slesvig's, because
Ditmarschen lies south of the Eider by definition.

**Check the rendered pixels, not the geometry.** The fix was confirmed by sampling
the PNG across both borders and finding nothing darker than Denmark's own fill.
Geometry that verifies can still render wrong, and the reverse.

**The `aria-label` is where numbers go to drift.** Chapter 22's Køge figure said
"fourteen burned" and "sixteen women who died" in its label while the legend beside
it said thirteen and the list showed one who escaped — a screen-reader user got
worse numbers, stated with more confidence, than a sighted one. Nobody proofs the
alt text. **Generate it from the same data as the visible legend**, never type it.

**A guard added after an incident must be applied backwards.** `validate()` and
`overruns()` were written into `figs_23.py` after a bare `&` broke a file, and only
the two scripts written afterwards got them — leaving five earlier figures
unchecked. They now live in `mapspine.emit()` and every figure script calls it.

**Length is not the same problem as weight.** Chapter 21 ran 49 minutes with nine
sections and the obvious fix — trim the two longest — was wrong: both look heavy
only because each carries a vignette, and §02 has the second-lightest narrative in
the chapter. Measure *narrative* words per section, excluding vignettes, glossary
blocks and figures, before deciding anything is too long.

**Rewrite a figure that fights its data rather than nudging it.** Chapter 24's
timeline had fourteen events, three of them inside five weeks, on a linear axis; no
amount of label-nudging fixes that. It became a fan — real elapsed time on the
left, equal spacing on the right, curves between — which is the device the index
already uses for the chapters themselves, and the clustering became the argument
instead of the obstacle.

---

**Two verifiers, because they see different things.** `seamcheck.py` tests polygons
and is exact, but only reaches maps that still have a `map_YYYY.py`. For maps that
exist only inside built pages, `mapdump.py` lifts every spine map out into one
HTML contact sheet — whole, and zoomed to the Kongeå and the Eider — and you look.

Five attempts to automate that second case were all wrong and are worth not
repeating: matching the composite colour caught coastline strokes lying under a
fill, which land 13 units from a genuine overlap; testing polygon vertices missed
the fault entirely, because the offending vertices sit over water even when the
lens between the two lines is over land; isolating each `<path>` dropped its
enclosing `<g clip-path>` and `<g transform>`, so it measured geometry rather than
ink and reported chapter 23's two side-by-side panels as 69,000 shared pixels; and
probing pixels along the border hit labels, dots and dashed strokes, all darker
than any overlap. **A built page is a picture. Inferring geometry back out of it
buys false confidence.**

What to judge, since "clean" is useless on its own: at every place two coloured
territories touch, ask whether any colour is **darker than the darker of the two**.
A translucent fill over another is always darker than either alone, and nothing
else on the map can produce that. Ignore the grey-brown coastline, the dashed
green duchy outlines and the white dashed internal borders — none of them is darker
than a fill.

---

## The renumbering of August 2026

16a and 16b became 16 and 17; 17–19 became 18–20; old 20 became 21; old 21 became
**22 and 23** (Christian 4., planned as two pages from the start); old 22 became 24;
and 23–40 became 25–42. Done by `renumber.py`, kept in `files/` as the template for
the Part G boundary.

**`renumber.py` is not idempotent. Never re-run it against already-swept files** — it
would shift everything a second time, and `--census` will now report false ambiguity
because references to "chapter 16" are legitimate again.

### Dates: old style and new style

**Decision D-6, August 2026.** Dates are given in the style the Danish state used at
the time — **Julian before 1 March 1700, Gregorian after** — with the foreign style
in parentheses at the first divergence in a chapter.

Everything in Parts A–F is therefore Old Style, and nothing currently says so. Part F
happens to be internally consistent, because Sweden was on the Julian calendar in
1658 too, so no divergence arises; but a reader checking Lutter am Barenberge against
a German source will find 27 August or 6 September depending which state printed it.
**Fix: one line in the index's conventions list**, which touches no chapter.

Part G is where it first bites on a date in the text. Sweden kept its own reckoning
until 1712 and then reverted to the Julian, so the battle outside Helsingborg is 28
February 1710 in Swedish papers and **10 March** in Danish ones; Poltava is 27 June
1709 Russian and **8 July** Danish. Chapter 27 carries a `gammel og ny stil` glossary
entry.

The convention does not resolve everything. The Frederiksborg peace of 1720 is given
as 3 June by one academic source and 3 July by another — a disagreement about the
*month*, not the calendar — and it needs the treaty itself.

### How a cross-reference is written

The series points at another chapter in **six** different ways. The first five were
never written down, so each cost a bug during the sweep; the sixth was added by
decision D-1 to stop the churn that caused:

| form | example | where |
|---|---|---|
| `chapter N` | "the deserted farms of chapter 17" | prose, glossaries |
| `→ N` / `← N` | `<li><b>→ 21</b>` | carry-forward blocks |
| `→ N, M` | `<li><b>→ 27, 29</b>` | carry-forward, multiple targets |
| `(N)` | "the Atlantic slave trade (27)" | prose, Parts A–D especially |
| `next: N` | footers | end of every chapter |
| `→ Part X` | `<li><b>→ Part H</b>` | carry-forward, targets beyond the next part |

**Decision D-1, August 2026.** A forward arrow may name a chapter *number* only
inside the next part. Beyond that it names a **part letter**. Three of Part F's
twelve arrows pointed two parts ahead and were wrong within a year, because the
chapter they aimed at moved when Part G took seven chapters instead of six. Naming
the part costs nothing and cannot go stale. `renumber.py --census` needs a pattern
for this form.

The comma form was matching only its first member. The bracket form matched nothing
at all — **chapters 11 and 12 use only that form**, so they would have been left on
the old numbering without even appearing in the list of changed files. Titles and
date ranges travel with numbers in footers and carry-forward blocks and need checking
too: chapter 15 was pointing at "Margrete I and the Kalmar Union, 1375–1412", a title
and a span that stopped existing when 16 was split, and nobody had noticed.

A reference to a chapter that has since been split is **ambiguous and must be resolved
by reading, not by inference**. Twenty such references were resolved by checking which
half actually contains the subject. Reasoning from checkpoint questions got at least
one wrong: `skattland` is glossed in 17's checkpoint but introduced in 16's text, and
the reference meant the latter.

---

## Debts — Part F closed, Part G open

Part F's inherited debts are all discharged: 18 → 21 (the Sound Dues as fiscal
base, and Peder Oxe's reform of 1567), 20 → 21 (a crown with a fleet, no bishops
and land it did not ask for), 19 → 24 (Sweden as a separate kingdom with a
founding grievance, and the fourth and fifth of the eleven wars). Chapter 21 also
carried back to 19: Ditmarschen, which destroyed a royal army at Hemmingstedt in
1500, is conquered in 1559 by the commander who won the Count's Feud.

Opened by Part F, and now owed:

**Sixteen forward arrows, as they now stand in the shipped files.** The ledger
pass of August 2026 re-pointed them; this is the state on disk, not the plan.

- 20 → **Part G** — the nobility's position after 1536, the `adelsvælde` 1660 dismantles
- 20 → **Part G** — the Norway clause of the 1536 recess, on the books until 1814
- 21 → 25 — the `adelsvælde` at its most functional is what 1660 dismantles
- 21 → **27** — the Gottorp line created by the 1544 partition, closed 1720–21
- 21 → **28, 29** — labour services and the bound peasantry: the bond in 28, the
  reforms in 29
- 21 → **Part H** — the partitioned-off dukes of 1544 produce the Glücksburg line,
  and a king from it in 1863
- 22 → 25 — "the king's own money" as against the realm's, and its collapse
- 22 → **30** — Trankebar 1620 and the chartered company: the shape of the Danish
  overseas enterprise before it turned to the Atlantic and the slave trade
- 22 → **28, 31** — the Norwegian law of 1604, the resident governor and the mines:
  the apparatus in 28 §07, the separation in 31
- 23 → 25 — the charter of 1648, the `adelsvælde`'s high-water mark and last document
- 23 → 26 — Leonora Christina, married to Ulfeldt in 1636, twenty-two years in the
  Blue Tower
- 24 → 25 — the estates meeting of September 1660, the hereditary crown and the
  `Kongelov` of 1665: the most complete absolutism in Europe, created by consent
- 24 → 26 — Leonora Christina in the Blue Tower from 1663, and the
  `Jammersminde` she wrote there
- 24 → **26, 27** — Skåne is not quietly Swedish: the `snaphane` war in 26, the last
  Danish attempt on it in 27
- 24 → **30** — a state with no land revenue left has to find income somewhere; the
  Atlantic trade and the slave forts
- 19 → **Part H** — Ribe 1460 to 1848, 1864 and the plebiscite of 1920
- 15 → 36 — the overseas-province debt is **chapter 15's**, from Part D: Estonia
  sold in 1346, to be answered by the West Indies in 1917. It was once listed as a
  chapter 16 debt in error; the Part D ledger already carries it.

**The ledger was short by five arrows, and it took a census of the files to find
it.** The list formerly held twelve bullets; the six shipped bodies actually carry
**sixteen** forward arrows into 25 or beyond. The four missing ones that needed no
change were `20 → 25`, `22 → 25`, `23 → 25` and `24 → 26`. **The fifth was wrong:**
`24 → 27` sent the Atlantic trade and the slave forts to the Sound-war chapter, when
the Atlantic chapter is 30 — the same error the ledger caught in `c22`'s Trankebar
arrow and missed one file over. It is now `24 → 30`.

**One bullet was attributed to the wrong file.** What this list called `23 → 26`
quotes, word for word, the arrow that is in `c24`. `c23` carries a Leonora Christina
arrow too, but a different sentence. Both are correct at 26; the misattribution is why
`LEDGER_PASS.md`'s `Jammers` grep handle returned nothing in `c23`.

**Ten of the sixteen moved**, not twelve. The six that were already right and stayed
are `21 → 25`, `22 → 25`, `23 → 25`, `23 → 26`, `24 → 25` and `24 → 26`. Do not work
from a count; count the file.

**Lesson: the debt list is a record, not an inventory.** It held what was written down
when an arrow was opened, and five arrows were opened without being written down. Only
a census of the bodies is authoritative. ~~`census_g.py` does it in one pass.~~ **`census_g.py` does not exist** — not in
`files/`, not listed by `tidy.py` (Sept 2026). The Part H debt table was built by
an ad-hoc census over `c25`–`c31`. Either write the script or drop the reference:
a ledger pointing at a tool that is not there is worse than no reference.
**And the lesson paid out again.** That census found **seven** arrows into Part H
where the handover note listed five; chapters 29 and 31 each carry a `→ Part H`
that appeared in no record. Second time, same lesson.

Chapter 25 is the heaviest: it has to explain why an assembly of subjects voluntarily
created the most complete absolutism in Europe.

The spine maps still to draw: **1814, 1864, 1920, 1945**. 1600 ships at the head of
chapter 21; **1660 and 1721 are drawn** and ship in chapters 25 and 27.

**The year is 1660, not 1658** (decision D-3). Roskilde in February 1658 took
Bornholm and Trøndelag as well, and the Peace of Copenhagen gave both back in May
1660; a map dated 1658 draws a settlement that lasted twenty months. The 1660 map
also draws the ceded provinces in their own tone, because a part opening on what was
left cannot be silent about what went; the 1721 map drops them again, Sweden being
uncoloured as on 1600, because by then they had been formally renounced. The western panel decisions are per map
and must be made deliberately each time: 1600 Greenland `CLAIM`, 1721 `DEP` again
once Hans Egede lands. Orkney and Shetland are gone from 1468–69 onward and must
not reappear.

---

## Decision D-10: Part I takes eight chapters; the book is 44 — SUPERSEDED by item 136: nine, and 45

*Taken at the Part I planning session, Sept 2026, and parallel to D-2, which is how
Part G got its seventh.*

The published spine ran `1918 – 1920` then `1929 – 1939`. **The nine-year hole was
visible to a reader on the index page**, not merely a planning inconvenience, so it
had to be closed in `index_generator.py` whatever the answer was.

The twenties are a chapter, not a linking passage: the postwar slump, the
Landmandsbank collapse of 1922, the defence settlement, Stauning's first government
and Nina Bang, Madsen-Mygdal and the return to gold, the mark conversion in
Sønderjylland, the Greenland declaration of 1921. Forced into a 1920–1939 chapter
they become two sections before the crash, and what gets cut is disproportionately
the women and the non-elite subjects — the D-9 material. The thirties alone are
equally full and include the 1939 referendum, on which chapter 44 depends.

**The cost was measured, not assumed.** Nothing built referenced a chapter number
above 36; the only occurrences of `c37`–`c43` in the repository were in the generated
index. The functional hardcodes of 43 were two lines in `bookstats.py`. No renumber
script, no rebuild of any part, no shipped page touched. It was the cheapest
structural change the project has made, and cheap only because Part I was unwritten.

**A consequence for the ledger.** The recorded ground for rejecting an epilogue past
1953 — that it "breaks a 43-chapter spine that every tool in the build assumes" — is
false: one script assumed it, in two lines. **The decision to end at 1953 stands on
its own better ground** — §20 installs the mechanism 1973 exercises, so the book ends
by building the door rather than stopping mid-sentence — but the false premise is
struck rather than carried forward, because that is the kind of premise that gets
reused.

Spine changes made with it: 38 takes Iceland's Act of Union from 37's key list, where
it sat two years outside its own span; 41's span opens in 1939 so the phoney-war
winter has a home and no hole is left; 39 is new; 40–44 are the old 39–43.

**REOPENED FOR PART I'S INTERNAL BOUNDARIES, Sept 2026 — see item 128.** D-10's
reasoning stands and its method is the point: the 1917–1929 hole was found by
looking at what the spine actually contained, not at what the plan said it
contained. The same test applied to 1943–1955 says the boundaries there were also
drawn before the research — chapter 42 built at 55 minutes against a 40-minute
advisory, and the plan's section list has been wrong in every chapter of the part
since 39. **The book's ending at 1953 is not reopened. The number of chapters
between August 1943 and 1953 is**, and it is settled once the part is drafted
rather than one chapter at a time.

---

## Convention D-9: vignette balance tags

*Added at the Part H planning session, Sept 2026, because L7a had no check behind
it and both recorded failures were found by hand after drafting.*

The vignette `(who)` line gains a trailing bracket:

    person · place · date · [f][n]

`f` where a woman is the agent. `n` where the subject is non-elite. `[-]` where
neither applies. **Two claims only** — a third would turn tagging into an argument
rather than a check. `[-]` is not a third claim: it asserts nothing about the
subject and records only that the question was asked.

**Amended Sept 2026, at the Part H tooling session.** As first written the
convention omitted both brackets where neither flag applied, which made a chapter
of three elite male vignettes textually identical to a chapter nobody had tagged
yet. That is chapter 25 exactly — one of the two failures D-9 was written to
catch — so the check could not see its own founding case. A vignette with neither
flag now carries `[-]`, and a chapter with no bracket on any vignette is the only
thing that reads as untagged. `[-]` beside `[f]` or `[n]` is a contradiction and
`vignettes.py` reports it as malformed. Verified against a five-chapter fixture
covering pass, both-missing, one-missing, partial and malformed: the real corpus
exercises only the untagged branch, so the branches that matter are tested there
and not on live chapters.

`vignettes.py` gains a balance layer reading the tags and reporting, per chapter,
whether a woman and a non-elite subject are present.

**Backfill is lazy.** The forty-eight existing vignettes are tagged as each part is
next touched; the balance layer reports `untagged` for chapters 16–31 until then.
Confirmed Sept 2026: there are zero brackets anywhere in the corpus, so all sixteen
report `untagged` and none of them is a false pass.
Tagging them from the roster summaries would mean asserting class and gender from a
one-line précis, which is the kind of inference this project has been burned by.

Part H's fifteen vignettes are tagged in `PLAN_H.md` §4: five women, seven
non-elite, no chapter without one of each. The roster's `—` entries are written
`[-]` on the page, not left blank.


## Convention D-8: how intervals are counted

*Added after the Part G review pass, which found three interval errors in prose and
one apparent error that was correct.*

Prose intervals are **completed** intervals: count whole years elapsed, not the
difference between the two year-numbers. Where the completed count falls within a
month of the next one up, **name the two years instead of stating an interval** —
the sentence is more useful and cannot go stale.

The rule exists because `overruns()`, `overflows()` and the build's assertions all
guard numbers that live in code. **An interval written in prose is guarded by
nothing.** Four were wrong or misleading in Part G at first build:

- chapter 25 §02, "the last one had met eight years before" — the last stændermøde
  was Odense, early 1657. Three years. Now names Odense.
- chapter 27 §04, Holberg "thirty years later" — Epistel 89 is in the second volume
  of the *Epistler*, 1748. Thirty-seven years. Now names the epistle.
- chapter 26 §09, *Jammers Minde* "a hundred and eighty-four years after she wrote
  it" — 1869 − 1674 is 195, and the publication year was itself disputed at the
  time of writing. Interval removed rather than corrected.
- chapter 28 §03, "Thirty-one years later" from 22 February 1701 to 4 February 1733
  — **correct** by completed years and looks wrong by subtraction. Left alone.

Applied to the two passages the review left waiting: the Bastille is twelve months
after 20 June 1788, not thirteen; and Mazarin's death is given as March 1661, five
months after the Copenhagen homage of October 1660, rather than as an interval.

**Treat every "N years after" and "N years later" in a draft as a claim to verify.**

---

## Note: a guard that does not exist yet

`overruns()` tests text against the canvas edge and `overflows()` against the canvas
foot. Neither can see text crossing an internal column divider, which has now caused
three faults: text overflowing a container in chapter 26 (never given a lesson number; recorded in
`STATE_G.md` §4), and twice in `figs_29.py`'s column figure, where a 36-character
label was written into a 23-character label column and the guard passed it clean.

A naive check flags every full-width subtitle that legitimately spans both columns.
Doing it properly needs the figure scripts to declare their column geometry, which
none of them currently do. **Infrastructure task, not a quick fix.**

---

## REQUIRES PHYSICAL / ARCHIVE ACCESS — cannot be done from this end

*Three blocking apparatus gaps in Part G, and one non-blocking date (E4) need a person at a screen reading gothic
handwriting. None of them can be reached by web search, and the container's network
allowlist is npm and PyPI only. Listed with exactly where to look so the work is
one sitting rather than a search.*

**E1 — chapter 25 needs a woman as an agent.** A named widow holding a farm at the
point her holding is converted to hartkorn would land on §06, which is the chapter's
argument. **Where:** Arkivalieronline, Rentekammeret: Matriklen af 1662, browsable
by len and herred. The amtstuematrikel of 1664 is preserved for most of Denmark and
gives, herred by herred, sogn by sogn and by by by, the names of owners, users and
fæstere with their landgilde and its hartkorn. **Why not from here:** the matrikel is
scanned images in gothic script, not text-indexed; genealogists working it recommend
a primer on reading the hand.

**E3 — chapter 28's third vignette is a second king.** A named confirmand from a
parish register of 1736–40 would displace Christian 6. on the Dovre descent and fix
the two-elite-to-one-peasant balance. **Where:** Arkivalieronline, kirkebøger,
1736–40, any parish. Confirmation became compulsory in 1736, so the first cohorts
are the ones to want. **Why not from here:** same — scans, gothic hand, no index.

**E2 — chapter 31 has no non-elite subject.** *A lead, not a finished answer.*
Adresseavisen and the Copenhagen papers of 10–11 September 1807 carry notices from
the burnt streets. One extended account, dated 11 September 1807, concerns
hørkræmmer **Thomas Giørup**, of a gård at Dyrkøb 5 / Skindergade and adjutant to
General Peymann: he found his house in flames, tried to save his chatoller, learned
afterwards that his wife had emptied them and hidden the contents in a chest which
was then hit by a bomb, and only later got word of where his wife and six children
were. **Caveats, and they are real:** this reached me through a secondary blog
quoting the newspaper, the name spelling is unconfirmed, and a hørkræmmer with his
own gård and an adjutant's post is bourgeois rather than non-elite — he shifts the
balance without giving the chapter a labouring subject. **Do not write the vignette
from this note.** Confirm against the newspaper first; the project has already had
one vignette survive nineteen revisions describing a woman who was in Rome at the
time.

**E4 — the date of the peace of Frederiksborg, chapter 27 §07.** *Added 19 Sept
2026, item 138.* Near-universally 3 July 1720, and the Treaty of Kiel, art. 27,
names it so. danmarkshistorien.lex.dk prints the treaty's own subscript as
"undertegnet til Friderichsborg den 3 Jun. og ratificeret den 23 Jul. 1720" with
the editorial note "Ved en Trykfeil er den trykte Freds-Tractat dateret: 3 Jul." —
possibly a confusion with the Stockholm preliminaries of 3 June, which Kiel names
separately. Also unsettled: whether 3 July is Gregorian (as a Danish instrument
would be, and as Kiel implies) or Julian with 14 July Gregorian (as English
reference works have it, and as the chapter used to say). **Where:** the printed
treaty in Schou's *Forordninger*, 2. del, 1699–1730, and the Rigsarkivet original.
**The chapter no longer depends on the answer** — §07 was rewritten to assert only
what is documented — so this is a correction to make when found, not a block.


---

## The merge of August 2026, and what it cost

**`mkbody.py` regenerates bodies from `PART_G_DRAFT.md`. Any correction made to a
body or to a built page and not back-ported to the draft is destroyed by the next
build.** This happened once already and was caught only because the review pass
sent its bodies back.

Thirteen review corrections were recovered from `c25`, `c26`, `c27`, `c29` and
`c30` and written into the draft: the December 1658 date and the nine-and-a-half
years in 25; the 19 May 1685 release, the confirmed 1869 publication, the deleted
composure paragraph, Leonora Christina's age at death and Griffenfeld dying a year
later in the same week of the same month in 26; the Marie Grubbe vignette moved
from §05 to §04 in 27; the three-mechanism wording in four places and the thirteen
months of press freedom in 29; and the chronological-jump paragraph in 30. `c28`
and `c31` were confirmed untouched.

**Two of the recovered corrections fixed errors that were mine**: Leonora Christina
was seventy-six, not seventy-seven, and Griffenfeld died a year after her rather
than a few months. Both were introduced in the vignette-promotion pass and neither
was caught by any guard, because both are prose arithmetic. See D-8.

**Standing rule from here: after any edit to a body or a built page, back-port to
the draft before the next `mkbody.py` run, or the edit is lost.** Run
`debuild.py verify` as the last step of every build; it is the only check that sees
an artifact-only edit, and it now works on Part G.

**One conflict resolved in the review's favour against D-8.** The Bastille sentence
in chapter 29's Meanwhile reads "thirteen months after the Danish ordinance of 20
June 1788". The true interval is 389 days, twelve months and twenty-four days.
D-8 says round to completed intervals and, where the count falls within a month of
the next one up, name the two years instead of stating an interval. Both dates are
already in the sentence, so the interval is redundant. **Recommendation: cut
"thirteen months after" entirely.** Left standing pending Carsten's decision.

## CLOSED: the four artifact-only corrections

**All twelve pages of Parts F and G round-trip identical.** There are no
artifact-only edits left in chapters 20-31: the four were propagated into the
bodies before the review sent them back, and are among the thirteen recovered in
the merge above. Nothing is missing.

Getting to that answer took three runs and two tool faults, both worth recording:

1. The first run used the **unpatched `debuild.py`**, which reports DIFFERS on
   every page from Part D onward on the style block alone. Twelve DIFFERS, no
   signal.
2. The second used the patched file, and Parts F still failed — because **adding
   `--indigo` to `style.css` broke the mirror case**. The patch taught the tool
   about a token the page has and the stylesheet lacks; the new token created a
   token the stylesheet has and the page lacks, which is true of every page
   shipped before Part G, i.e. all of Parts A-F. `report()` now drops any
   `--xxx:#hexhex; ` present in the stylesheet and absent from the page before
   comparing.

**Rename `debuild_patched.py` to `debuild.py`.** The first of the three runs was
lost purely to the wrong file being on the path.

**A tool that returns a false positive on every page is worse than no tool**: it
trains the reader to ignore it, which is how four corrections went unnoticed in
the first place. `debuild verify` belongs in the standard sequence, after
`linkindex.py` and before upload.

### CORRECTION: what `verify` could and could not see

**An earlier note in this ledger said `debuild verify` is the only check that
catches an artifact-only edit. That was wrong**, and the error was found by trying
to write a test for it. `debuild()` derives the body FROM the page, so a prose edit
made directly to a built page is present on both sides of the comparison and
round-trips perfectly. `verify` only ever proved that the four injected regions -
style, rail, contents, script - were reversible. It was blind to exactly the thing
it was being trusted for.

`report()` now also compares the recovered body against the **retained**
`cNN_body.html`, which is the source the next build will use. Both sides are
normalised first, because the build injects five things and not four: the style
block, the rail, the contents, the script, **and the figures**, plus it inserts
checkpoints and rewrites the reading-time line. Normalising all of those leaves the
prose, which is what an artifact-only edit changes.

Three outcomes now, and the distinction matters:

- `identical` - page, body and current stylesheet all agree.
- `style-only` - the page was built against an older `style.css`; the body is
  intact. **Chapters 01-11 report this and it is not damage**: they have no
  retained bodies and cannot be rebuilt, so they can never match the current
  stylesheet. Their prose is fine.
- `BODY DRIFT` - the page disagrees with its retained body. **A rebuild would
  silently discard whatever the difference is.** This is the serious one, and it
  is the case that was invisible before.

Verified by simulation: a clean Part G page reports `identical`; the same page with
a single word altered reports `BODY DRIFT`.

## (was: STILL OPEN)

`debuild.py`'s docstring records that four corrections in Part G went unnoticed
because nothing was round-tripping the pages. The thirteen above were recovered
from the *bodies*. Whether the four are among them, or are a separate set living
only in the built HTML, is **not established**.

**One command settles it**, run locally with the review's pages and bodies in place:

    python3 debuild.py verify 2?-*.html 3?-*.html

Anything reporting `DIFFERS` carries an artifact-only edit. All seven `identical`
means the four were already propagated and nothing is missing.

---

## The word counter, corrected — August 2026

`pagecount.py` is new and now holds the only definition of "how many words is this
page". `build_parts_abc.py`, `build_part_d.py`, `build_part_e.py`,
`build_part_f.py`, `build_part_g.py`, `build_all.py` and `bookstats.py` all import
it. The expression it replaces had been copied into all seven, which is how the
units-per-character constant in the figure scripts drifted from 5.55 to 6.1 in six
of seven copies without anyone noticing.

**What was wrong.** Stripping tags left the text inside `<svg>` — axis labels,
timeline dates, the figures' own caption lines — and `.split()` returned a
free-standing em dash or middot as a word. Both were counted as prose. Part G lost
3,589 words across seven pages, a mean of 512, about 2.4 minutes each.

| ch | before | after | minutes |
|---|---|---|---|
| 25 | 7,129 | 6,650 | 34 → 32 |
| 26 | 7,913 | 7,311 | 38 → 35 |
| 27 | 7,298 | 6,803 | 35 → 32 |
| 28 | 9,589 | 9,129 | **46 → 43** |
| 29 | 7,805 | 7,328 | 37 → 35 |
| 30 | 7,321 | 6,881 | 35 → 33 |
| 31 | 8,141 | 7,683 | 39 → 37 |

Part G runs 32–43 minutes against the 28–40 advisory. Only chapter 28 is outside
it, by three minutes.

**One row in the table above no longer reconciles.** Six of the seven `after`
figures match `bookstats.py` exactly today. Chapter 28 does not: this table says
9,129 and the current build says **9,086**, a gap of 43 words. Either `c28` was
edited after the table was written — in which case check it was back-ported to
`PART_G_DRAFT.md` — or the figure was typed. It has not been established which.

**PARTS A TO F HAVE NOT BEEN REBUILT AND STILL CARRY THE OLD FIGURE.** The scripts
are correct; the pages are not. Every page in chapters 01–24 overstates its reading
time by roughly two to three minutes until it is rebuilt locally. Parts D, E and F
have retained bodies and can be rebuilt directly. **Parts A–C have no retained
bodies** — the path there is `debuild.py extract` first, which is now safe because
all twelve pages tested round-trip identical.

**Do not re-read the band thresholds against the old numbers.** The 25–50 band and
the 30–42 advisory were set when every measurement was two to three minutes high,
so in effect the advisory has been 28–40 all along. **DECIDED, Sept 2026: the advisory moves to 28–40. The band stays 25–50.** The
restatement is behaviour-neutral — chapters 21 and 28 flagged before and flag now,
and nothing else moves. A floor of 30 would flag chapter 17 at 29 minutes, a
deliberate six-section chapter defended in open item 1: a false positive on a
settled decision, and false positives are how `debuild` became ignorable.

Note on L1a's closure property: 50 splits into two 25s, but 47 splits into two
23.5s. The band is closed under splitting **at the ceiling only** — which is
correct, since splitting is forced only above 50, and it is why chapters 21, 28
and 32 were all retired rather than divided.

**Chapter 28 is a three-minute overrun against the 28–40 advisory.** ~~It remains a
split candidate on topic count, not on length.~~ **Retired, Sept 2026 — see item
20 and L13.**


44. **The Copenhagen vignette count was stale, and the handover note carried it
   forward.** Item 27 and `PLAN_H` §2.6 both say "thirteen of forty-eight". That
   was right for a 48-vignette corpus and the corpus is no longer 48. Chapter 32
   added one Copenhagen vignette (Pätges at the Hofteatret) and took the total to
   51; the handover note for the chapter 33 session updated the total to 51 and
   left the Copenhagen figure at 13. Measured on the corpus at the start of the
   chapter 33 session: **fourteen of fifty-one**. With chapter 33's Lehmann
   vignette it is now **fifteen of fifty-four**. Corrected in both files.
   *The standing rule failing in its usual place: a number typed forward from an
   older count instead of recomputed. Compute the place census, do not carry it.*

45. **Chapter 32 ships a one-item "page in five".** `mkbody.py`'s `five_html`
   builds `<ol class="five">` from the paragraphs of the draft's Summary block,
   and `c32_draft.md`'s Summary is a single paragraph. The shipped page therefore
   renders a heading reading IF YOU REMEMBER FIVE THINGS above a list containing
   one item, numbered `01`. Item 19 records 25, 26 and 27 running to four items;
   **chapter 32 at one is worse and was not recorded at all.** Found because
   `mkbody.py` prints `summary items N (of M paragraphs)` and chapter 33's first
   build said `1 (of 1)`. Chapter 33's Summary is now five paragraphs and reports
   `5 (of 5)`. **CLOSED, Sept 2026, and guarded in two places.** `c32_draft.md`'s
   Summary is now five paragraphs, chapter 32 rebuilds at 8,246 words and 39
   minutes and verifies `identical`. `mkbody.py` prints a `!!` line when a Summary
   yields fewer than five items, and **`build_part_h.py` counts the rendered
   `<li><p>` items and exits non-zero** — a warning would have been ignored, which
   is how this survived a session. Verified by crippling a copy of `c33_body.html`
   to a single item: the build printed `SUMMARY IS 1 ITEM, NOT FIVE` and exited 1,
   and returned to 0 when the body was restored. **Chapters 25, 26 and 27 still
   render four items each (item 19) and will now fail their own part build the next
   time Part G is rebuilt with the check ported across.** Porting it into
   `build_part_g.py` and the earlier part scripts is a small job left undone here.

46. **`CHAR_W` is wrong for every class, and wrong in the dangerous direction for
   the one that matters.** Measured off the raster during the chapter 33 session
   by rendering eighty monospace glyphs and taking the ink extent:

   | class | `mapspine` | measured | direction |
   |---|---|---|---|
   | `mapt` | 5.68 | **6.36** | under-reports by 11% — unsafe |
   | `mapl` | 6.98 | 6.61 | over-reports — noisy, safe |
   | `mapx` | 5.63 | 5.33 | over-reports — noisy, safe |

   `mapt` is the body class in every figure in the book, so `overruns()` has been
   under-reporting on the most-used class since item 40 declared it resolved.
   **Blast radius checked before anything was changed, per item 39: `CHAR_W` is
   read only by the guards and never by layout, so correcting it cannot alter one
   byte of any `svg_*.txt` and cannot make a Part A–D figure stale.** It can only
   make the guard stricter.

   **It was not changed, and here is why.** Run non-destructively across all 54
   figures, the measured values fire three times — twice in `svg_mandebod.txt` and
   once in `svg_titles.txt` — and **all three are false positives.** Settled on the
   pixels rather than on the constant: rasterised at 3× and scanned for the
   rightmost ink column, `svg_mandebod` reaches 683.3 of 700 and `svg_titles`
   reaches 899.7 of 900. Both fit. This is exactly item 42's finding about margins
   compounding with line length, and false positives are how `debuild` became
   ignorable.

   **The deeper point, which is new.** There is no single true constant. `monospace`
   resolves to whatever face the renderer has — DejaVu Sans Mono in the container,
   Menlo in a Mac browser — and the advance differs. A per-character estimate can
   therefore only ever be an upper bound across plausible faces, and item 40's
   instruction to "re-measure" is not sufficient, because a point measurement on
   one machine is not the thing being guarded.

   **What to do instead, and it is cheap.** Where cairosvg is present, the width
   check needs no constant at all: rasterise, scan for the rightmost ink column,
   compare against the canvas. Twelve lines, exact, and it settled the three
   flagged figures in one run. Proposal: add it to `check()` as an exact pass when
   cairosvg imports, keeping the estimate as the fallback where it does not — which
   is the Mac. **Infrastructure task, not done here**, because item 41's lesson is
   that a guard is worth nothing until it is wired in properly, and wiring it in
   deserves its own pass. Note also that `svg_titles.txt` clears its canvas by
   **0.3 units** against a documented six-unit cushion, which an exact check would
   fail and which is worth a look on its own account.

47. **`collisions()` compares text against text and nothing else.** A `<rect>` laid
   over a `<text>` is invisible to it. Found in chapter 33's franchise figure,
   where a two-entry key set on one line put the second swatch straight through the
   first label; every guard passed and it was caught by looking. Item 42 says
   `overruns` tests the canvas edge and nothing else; the same sentence is now true
   one level up. Keys are stacked in `figs_33.py` rather than columned, which
   avoids the case without fixing it.


48. **Part of Ærø has been drawn as Danish crown territory since the 1660 map, and
   it belonged to the duchy of Slesvig.** Found by the fixture, on the first run
   of the 1864 map, and only because the 1864 treaty gave me a reason to write a
   curated case for the island — which is the Rogaland lesson again: the fixture
   checks what somebody thought to test.

   The series has never carried an Ærø polygon. The southern lobe of the
   `DENMARK` hull reaches far enough south-east that **Ærøskøbing and Marstal fall
   inside it, while western Ærø falls inside nothing.** So the island is half
   Danish and half unclaimed, by accident of a coarse outline, on the 1660, 1721
   and 1814 maps — where it should have been Slesvig's throughout. On the **1864**
   map the same artefact gives the *right* answer, because the treaty did bring
   Ærø into the kingdom, and the curated case is pinned to `DENMARK` with a comment
   saying it is right for the wrong reason.

   **CLOSED, chapter 38 session, and item 48 understated it twice.** Measured
   against the atlas rings before anything was touched: Ærø was 4 of 9 ring
   vertices inside `DENMARK` on **all seven maps**, not four. The 1397 spine
   carries the same southern lobe, so 1397, 1500 and 1600 have the fault too and
   the blast radius is **seven shipped chapters - 16, 19, 21, 25, 27, 32, 34** -
   not the four this entry named. All seven have retained bodies; nothing in
   Parts A-D is touched.

   **The sweep could never have caught it.** At `GRID = 0.20` no sample point
   lands on Ærø at all. This entry called it 'the fixture checks what somebody
   thought to test'; it is worse than that - the generated layer was structurally
   blind here, not merely unlucky.

   The fix. `DENMARK`'s lobe re-threaded from one run (10.05,55.10)-(10.9,54.60)
   to (10.05,55.10)-(10.56,55.02)-(10.56,54.60)-(10.9,54.60); the vertical at
   10.56 passes between Ærø's east end at 10.503 and Langeland's west end at
   10.629, which is the Sound's trick between Helsingør and Helsingborg. `AERO`
   is a generous box defined once in `map_1397.py`; fills are clipped to land, so
   its edge is entirely at sea and never draws. **Two names, one geometry:**
   `AERO_SL` on 1397-1814 and `AERO_DK` on 1864, because the fixture tests the
   NAME a point resolves to - a single `AERO` region would let a future edit draw
   the island in the wrong fill loop and still pass every case. 21 curated cases
   added (Søby, Ærøskøbing, Marstal, spread along 30 km so a partial polygon
   fails). After: Ærø 0/9 in `DENMARK` and 9/9 in `AERO` on every map, Langeland
   still 9/9 in `DENMARK`, Funen unchanged at 19/21. Original entry follows.

   ~~**Not fixed here, deliberately.**~~ Correcting it means editing `DENMARK`'s
   vertex list, which is shared with `SLESVIG` through `DK_SL` and is inherited
   unchanged by four maps and four shipped chapters (25, 27, 32, 34). That is a
   seam edit with a four-chapter blast radius, and item 39's rule is to check the
   radius before applying, not after. It also needs a decision I should not take
   alone: whether to add an Ærø ring at all, given that the island is about the
   size of the label that would name it.

49. **`overruns()` tests the right edge and the bottom, not the left.** Item 42
   recorded that it tests the canvas edge and not neighbours; that was only
   two-thirds true. While placing the 1864 map's notes, a line of text ran off the
   **left** side of the canvas and was silently clipped, and every guard passed.
   Caught by looking. The fix in `map_1864.py` was to move the text; the fix in
   `mapspine.py` is one comparison and is not made here, because the exact
   pixel-width pass proposed in item 46 would cover this case too and the two
   should be done together.

50. **`collisions()` was blind twice in one session, and the second time I already
   knew.** It compares text with text; a `<rect>` over a `<text>` is invisible to
   it. Chapter 33's franchise key hit this (item 47), and then chapter 34's
   `svg_ceded_1864.txt` hit it again with a bar printed over its own label, in a
   figure written *after* item 47 was recorded. Knowing about a blind spot is not
   the same as checking for it. Both were caught by looking, which is the only
   thing that has caught this class all series.

51. **The 1864 map's notes were placed twice.** The first placement satisfied the
   collision guard by putting the Kongeå note three hundred kilometres out into
   the North Sea, and the rasterised map was unreadable: a note explaining a
   frontier, nowhere near the frontier. **A guard that scores overlap cannot score
   meaning**, and a search that optimises only against the guard will happily
   produce a legible-but-senseless layout. The second pass moved the explanation
   into the legend, which had room, and left a two-word label at the line. Worth
   generalising: search for candidate positions by regeneration, then look at the
   winner before keeping it.

52. **Stale comment in `mapfixture.py`, unrelated to this session's work.** The
   1814 cfg block still says of Lauenburg that "its ground falls inside HOLSTEN
   here and is assigned there, so coverage is not left with a hole." That is the
   version `map_1814.py`'s own docstring records as **wrong and corrected**:
   Ratzeburg resolves to no territory, and the curated case is pinned to `None`,
   which is what actually passes. One of the two texts should go. Left alone here
   because it is documentation rather than behaviour, and because editing the
   fixture's comments in the same session that adds a map to it makes the diff
   harder to read.


53. **Two chapters now want the same unfetched table, and that is the argument for
   fetching it.** Chapter 32's figure 3 could not be drawn as a price line because
   the nineteenth-century run of the Zealand kapitelstakst was not obtained.
   Chapter 35's figure 1 was planned as two crossing price series and has just hit
   the same wall for the same reason. **The kapitelstakst is a library errand, not
   an archive one** — the modern values are published and the back-series is in the
   printed `Statistisk Tabelværk` and in the statistics bank's older tables.
   Getting it once redraws two figures, both currently drawn as something else with
   a docstring explaining why. This is now the highest-value outstanding fetch in
   the project.

54. **`figs_35.py` records the same L1 diagnosis for the third chapter running.**
   Chapter 34's draft came in 872 words short, chapter 35's 959. Both times the
   fix was a missing subject, not thin paragraphs, and both times naming the
   subject took less than a search. The pattern is now strong enough to state as
   a working rule rather than an observation: **if a Part H draft lands more than
   about 500 words short, stop and ask what has been left out, before touching a
   single existing paragraph.** In 34 it was that Denmark won a naval battle and
   the draft did not mention it; in 35 it was that the cooperative contract took
   butter-making out of the farmhouse and away from women.

55. **`mkbody.py`'s vignette count has now caught a missing vignette three times**
   — chapters 34 and 35 both drafted with two where the plan had three, and in 35
   the missing one was §10's, the chapter's own closing section. The line
   `vignettes N` in the build output is doing more work than the D-9 balance check,
   because D-9 tests the tags of the vignettes that exist and this tests whether
   they exist at all. Both are needed and only one was designed on purpose.

56. **Three figure faults in chapter 35, none of which any guard can see, and one
   of them would have made the chart lie.** Recorded together because they are one
   class:
   - The causal chain in figure 1 opened at 1875 and then stepped back to 1864,
     on a figure whose entire form is chronological order.
   - Figure 2 chose its emphasis tone with `if pct > 30`, which put the residual
     "everyone else" row in the same dark tone as the row the chart exists to make.
     **Tone by meaning, not by size.**
   - Figure 2's point scale used the data maximum while its axis was labelled
     12,000, so the axis said one thing and the geometry said another. That is not
     an aesthetic fault; a reader measuring off it would have been wrong.

   All three were caught by opening the PNG. The running count for the series is
   that looking has found something in every part, and in Part H it has found
   something in every chapter.


57. **PART H IS COMPLETE.** Chapters 32 to 36 built, verified and indexed; the part
   coda is on 36. 63 figures, 63 vignettes, every chapter 3/3 tagged with `[f]` and
   `[n]` present.

   *Corrected at the Part I planning session.* The lengths recorded here were 39,
   40, 36, 38 and 37 minutes, "all inside the advisory band". Measured on the
   shipped bytes they are **39, 41, 36, 37, 37**: chapter 33 is 8,510 page words
   and **41 minutes, one over the 28-40 ceiling of decision 2.1**. A 110-word
   overshoot is not worth reopening a shipped chapter for, but the ledger should
   say 41 and flag it rather than say 40 and claim compliance. Totals after the
   item 24 fix: **36 of 44 chapters built, 259,526 page words, 20.6 hours.**

58. **The part coda was hardcoded to Part G and is now data-driven.** `mkbody.py`
   built the coda's kicker and band from string literals, because chapter 31 was
   the only chapter that had ever carried one. Both now come from `HAND` as
   `coda_part` and `coda_span`, defaulting to the Part G pair. **The symptom was
   predicted before the change** — chapter 31 must rebuild byte-identical — and it
   did; the only line in its diff is the index-link stripping of item 8.

59. **L1 has now held for four consecutive chapters and should be promoted from
   observation to procedure.** Short-draft deficits: 33 came in near target, 34 by
   872 words, 35 by 959, 36 by **1,270**. Every time the cause was missing
   subjects and never thin paragraphs, and every time naming them took less than a
   search. Chapter 36 is the sharpest case because the plan had *already warned*
   about it: PLAN_H §9 records that its own first section list was discarded for
   being 1L/6M/3H, "a flat chapter — chapter 28's fault wearing different
   clothes." My first draft came out **5L/5M/0H**, which is worse, and the
   measurement said so immediately. What was missing was substantive: that the
   provisional finance laws merely authorised the government to meet the state's
   necessary expenses as it judged them; that elections went on being held and
   lost throughout; and J.C. Christensen's parish council law of 1903, which
   discharges chapter 33's Article 80 after fifty-four years.

   **Proposed rule for Part I planning: measure the draft against the plan's
   weight profile before reading it for quality. A profile with no heavy sections
   is a defect regardless of the word count.**

60. **Three planned time series have now been refused in one part, all for the same
   reason.** Chapter 32's figure 3 (kapitelstakst), chapter 35's figure 1 (grain
   and butter prices) and figure 2 (emigration by year), and chapter 36's figure 2
   (seats against votes, 1872–1901). In every case the series genuinely exists and
   was not obtained, and in every case the figure was redrawn as something the
   sources do support with a docstring saying what was wanted and why it was not
   drawn.

   That is the right behaviour and it is also a pattern worth acting on. **Part H
   has shipped fifteen figures and not one of them is a time series.** For a part
   covering ninety years of economic and political change that is a real gap in
   the book's visual repertoire, not just a run of individual refusals. Item 53
   names the kapitelstakst as the highest-value fetch; the Folketing election
   results 1872–1901 are the second, and both are library errands.

61. **`collisions()` was blind four times in one session.** Items 47 and 50 record
   the first two; chapter 35's ceded figure was the third; chapter 36's franchise
   figure was the fourth, where the left column's prose ran clean under the
   sixty-six-block grid. A `<rect>` over a `<text>` is invisible to it, every time,
   and knowing that has not once been enough to prevent the next occurrence.
   **This is no longer a note; it is a missing feature.** The fix is to add the
   rects to the box list in `collisions()` with a flag so that rect-over-text is
   reported separately from text-over-text. Not done here for the same reason as
   item 46: it belongs with the exact-width pass and the two should be built and
   tested together.

62. **A second box-height fault of the same family as item 41.** Chapter 36's
   deadlock figure drew three panels at a typed height of 132 units and two of them
   overflowed, spilling their last lines through the border into the dashed box
   below. Nothing fired, because `overruns()` tests the canvas edge and not a
   rectangle drawn inside it. The fix was the same one chapter 33's franchise
   figure needed for the canvas: fold the content first, take the tallest column,
   then draw the boxes to that. **Any dimension typed as a literal in a figure
   script is a latent version of this fault.**


76. **The `Slesvig` label sat on Ærø on five maps, and no guard could see it.**
   Found by rasterising after the Ærø ring went in, then confirmed by arithmetic
   rather than by a second look: `Slesvig` is 7 mapt characters at `CHAR_W` 5.68,
   so 39.8 units wide, anchor=middle; Ærø's printed land runs x 186.0-191.8 and
   its top edge is y 620.3, and the label's baseline sat at 619.5 with descenders
   to about 621.9. On 1600, 1660 and 1721 the label was at (9.95, 54.95) and its
   descenders clipped the island's north coast. On **1814 and 1864 it was at
   (10.55, 54.95), centred over the island** - so the 1864 map was about to print
   the word *Slesvig* across the one island the 1864 treaty took OUT of Slesvig.
   `collisions()` is text-against-text and cannot see text over a fill.

   **The position was computed, not typed.** A search over the duchy's interior,
   scoring each candidate against every other text box in that map's own SVG and
   against Ærø's land box, returned 166/166/166/155/64 clean positions on the
   five maps; the one nearest the `SLESVIG` centroid is **(9.20, 54.85)** and is
   clean on all five. My two hand-picked positions before that - (9.10, 54.95) and
   (8.90, 54.65) - both collided, with `Kolding` and with `Gottorp`. **Do not
   place a label by reasoning about it. Place it by search.**

77. **`M.check()` was wired into one of seven map scripts.** `map_1864.py` has
   called it since it shipped; 1397, 1500, 1600, 1660, 1721 and 1814 never have.
   That is item 41 exactly - the guards existed and were not connected - and it is
   why the Kolding collision only surfaced when I happened to be editing the map
   that calls it. Now wired into all seven, same pattern as 1864's. All seven are
   clean, and the maps still print nothing but their `wrote` lines.

78. **CLOSED, same session. Als is 9 of 9 now.** The eastern lobe - Fynshav,
   Mommark, the whole east coast - was outside the duchy on every map in the
   series and inside nothing at all. Als gets no ring of its own: Alssund is
   200 m wide and the island reads as contiguous, so `SLESVIG`'s eastern edge
   moved instead, from (9.98,55.05)-(10.00,54.88) to (9.98,55.10)-(10.14,55.05)-
   (10.14,54.86). 10.14 clears Als's easternmost point at 10.060 and stays west
   of `DENMARK`, which begins at 10.37 at lat 55.05 and 10.56 further south; the
   (9.98,55.10) vertex is what holds the run down from (9.75,55.48) clear of
   `DENMARK`'s lobe, which reaches 10.05 at that latitude. Verified by a dense
   0.01-degree sweep of the whole box: zero overlap samples. A `Fynshav, Als`
   curated case added to all seven maps, on the lobe that used to be outside -
   the existing Sønderborg case sat in the covered half and could not have
   caught this, which is the same shape as Ærø's case sitting in the covered
   half of a half-covered island. Original entry follows.

   ~~**Als is 5 of 9 ring vertices inside `SLESVIG`, and this is Ærø's family.**~~
   Measured in passing while verifying the Ærø fix. Pre-existing on every map,
   much smaller than Ærø's fault because the curated Sønderborg case sits in the
   covered part, and invisible to the sweep for the same reason Ærø was. **Not
   fixed, and it is on chapter 38's path**: Als voted in Zone I in 1920 and the
   new plebiscite map inherits this outline. Decide before that map is built.

79. **`tidy.py` could not see Part I.** `BUILDS` listed A-H and `build_all` and
   stopped, so chapter 37's three figures reported as ORPHANS and `c37_body.html`
   was absent from the bodies table - a diagnostic returning a clean result about
   a chapter outside its field of view, which is item 67's shape. One line. It
   would have degraded by one chapter per Part I session. Fixed.

80. **Items 53 and 60 do not close the way item 73 assumed, and 73's premise was
   wrong in kind.** The `dst.dk` route works and the six Folketing hæfter fetch;
   *Folkethingsvalgene i Aarene 1869, 1872 og 1873* (2. rk. 12. bd. 3. h.) was
   opened in full. It is a constituency-by-constituency, commune-by-commune table
   of *Vælgernes Antal*, *Af 100 Vælgere stemte*, and votes per named candidate -
   candidates given by name, town and occupation, **with no party column
   anywhere**. Seats-against-votes by party is a reconstruction of these returns,
   not a statistic the department published, so chapter 36's figure 2 cannot be
   built from these hæfter however many are fetched. The OCR on the nineteenth-
   century tables is also far below the second-appearance standard: election dates
   render as 'Den 99de Septbr. 1869' and 'Den 14de Novbr. 1893' for 1873.

   **One identifier correction.** The catalogue lists *Folkethingsvalgene i Aarene
   1876 og 1879* at reference **3. 3. 4**, not 3. rk. 3. bd. H. II. Every printed
   bibliography inside the later volumes says H. II and has copied it forward for
   seventy years; hæfte 2 of that bind is *Kapitelstaksterne for Aaret 1879*. The
   other five identifiers in item 73 are confirmed exactly.

   **Item 53 is out of range, not out of reach.** Statistiske Meddelelser begins
   in 1852 and chapter 32 covers 1814-1848, so the annual *Kapitelstaxterne for
   Aaret N* hæfter cannot reach the period at all. The one retrospective hæfte
   that looks back past 1852 (1. rk. 1. bd. 11) gives four overlapping twenty-year
   means, not a series. Scharling's *Pengenes synkende Værdi* (1869) stays the
   only named route and is not on `dst.dk`. **Reclassify item 53: not the
   highest-value outstanding fetch, and a library errand the fetch route does not
   retire.**

   What the route does give cleanly, and it is worth having. The kapitelstakst
   hæfter carry a prose paragraph with the national mean per commodity for the
   year, the prior year and the preceding ten-year mean, checkable against the
   table opposite - 1873 rye 8 Rd. 38,9 β, 1872 6 Rd. 54,4 β, 1863-72 mean
   6 Rd. 40,8 β - so a national rye series from 1852 is buildable at one fetch per
   year with a real second-appearance check. And the franchise share of men over
   30 is a series in the volumes' own introductions: about 90.5 per cent in 1910
   against 86 in 1901, 83.5 in 1892 and 78 in 1881, with the 1913 volume revising
   1901-1910 downward by half a point and saying why. The department correcting
   itself, caught by second appearance, belongs on the figure's face.

81. **Chapter 38's figures are better sourced than PLAN_I §13 has them.** All
   three 1920 elections are identified: Folketingsvalget 26 April 1920 = 4. rk.
   60. bd. 3. h.; Rigsdagsvalgene juli-august 1920 = 4. rk. 61. bd. 1. h. (the
   6 July Folketing election and the 30 July Valgmand elections, turnout 74.9 per
   cent); Rigsdagsvalgene sept.-okt. 1920 = 4. rk. 62. bd. 1. h. That is §6's
   figure 2 fully sourced. **And the plebiscite returns are a Danmarks Statistik
   publication, not only the Commission's:** *Folkeafstemningen 1920* is
   **Statistiske Efterretninger 1920, nr. 23**, and Statistiske Efterretninger
   1909-1982 is a separately digitised series on the same site. PLAN_I §13 lists
   figure 1's source as 'International Commission returns'. Not yet opened.


82. **The 1920 map cannot be drawn parish by parish, and PLAN_I §13 says it
   should be.** The repo's only geography is Natural Earth at 1:50m, which has
   coastlines and nothing else - no parish, commune or amt boundaries at any
   resolution. A parish-level plebiscite map would require boundary polygons that
   do not exist here, and drawing them by eye from a printed historical map is
   exactly the invented measurement the standing rule forbids.

   **Recommendation, and it needs Carsten.** Draw the zones as bands rather than
   as parishes: the 1864 border at the Kongea, the Zone I/II line north of
   Flensburg, Zone II's southern limit north of Slesvig town, and the 1920 border
   itself running through Zone I - four lines, two bands, and the aggregate result
   on each. Then carry a small number of individually sourced commune results as
   dots, which needs no boundary data at all: Tønder and Højer voting German
   inside Zone I, Flensburg voting German inside Zone II, and two or three
   Danish-voting communes to set against them. That draws the chapter's actual
   argument - the en bloc rule against the commune rule - which a parish choropleth
   would bury under colour. The figure's docstring must say that parish polygons
   were not drawn and why.

   Als, item 78, was fixed before this map was started rather than after, which is
   the position item 48 was in and the reason it cost seven chapters to repair.


83. **Chapter 38 is eleven sections, not ten, and the commission is why.** PLAN_I
   §6 specified ten at 3L/4M/3H. The subject that was missing from the first
   draft - the International Commission's five months of government over both
   zones - went into §05 and took it to 808 words against a heavy band of 569.
   Cutting it back would have meant removing sourced material to preserve a
   section count. It is now its own section, light, between the zones argument and
   the first vote: **eleven sections at 4L/4M/3H, 4,251 narrative against 4,311.**
   Every section is within 90 words of band and the heavy that carries the
   10 February vote lands at 562 against 569. Decision taken by me under the
   standing delegation; PLAN_I §6 should be amended rather than the chapter.

84. **The 37-minute target has now missed upward twice, in the same direction.**
   Chapter 37 shipped at 38 (item 75) and chapter 38 projects 8,034 page words,
   which is 38. The length model in PLAN_I §5 derives its ~37 from ten sections at
   3L/4M/3H plus an apparatus constant of 3,783; an eleven-section chapter at the
   same bands cannot land at 37 and should not be trimmed until it does. **Two
   consecutive misses in one direction is a model fault, not two chapter faults.**
   Recompute the target from the bands actually in use before chapter 39 is
   planned, or Part I will spend eight chapters shaving 20-word cuts out of good
   prose to hit a number that was derived for a different shape.

85. **Three errors in the first chapter 38 draft, all caught by checking rather
   than by reading.** (a) The draft said the Aabenraa resolution came a week after
   H. P. Hanssen's Reichstag statement of 23 October 1918. It was 16-17 November,
   three and a half weeks, and it was the Vælgerforening for Nordslesvig at
   Folkehjem. The resolution also named the **Clausen line** - after H. V. Clausen,
   a Copenhagen schoolmaster who had walked Slesvig parish by parish in the 1890s
   recording where Danish was spoken at home - which the draft did not have at all
   and which is the best fact in the section. (b) The draft had Tinglev among the
   German-voting towns of Zone I. The German majorities were Aabenraa, Sønderborg,
   Tønder and Højer, plus small districts around Tinglev and Tønder, not the town.
   (c) The draft said that nowhere in Zone II did the Danish minority hold a
   district. **Three small polling places on Før returned Danish majorities** and
   stayed in Germany with everything else, which is a better fact than the
   generalisation it replaces.

   And one that is not an error but is worth writing down: the Zone I result is
   published both as 74.9/25.1 and as 74.2/24.9, and both are correct. 74.9 is the
   share of valid votes, 74.2 the share of all 101,652 ballots cast; the gap is
   892 spoiled papers. The chapter says so rather than picking one.

86. **Chapter 38's figure 1 is built, on the item 82 design, and it took four
   renders that no automated check could have shortened.** `validate()` caught an
   unclosed group before anything reached disk - `detail_base` opens a clip group
   the caller must close, and the translate wrapper is a second one. `M.check()`
   caught two legend lines running off the canvas, and then the wrapped legend
   falling off the bottom; the canvas height is now COMPUTED from the folded line
   count rather than typed. Everything after that was visible only in the PNG:
   the bands filled the North Sea and the Little Belt because `detail_base`, unlike
   the territory maps, opens no land clip; extending the bands past the coast to
   fix that put **Funen inside Zone 1**; and the first clipped render cut **Als**
   out of Zone 1 on the band's closing diagonal. Als and Funen overlap in
   longitude - Als reaches 10.060, Funen begins at 9.859 - so no cutoff meridian
   separates them and the closure had to follow the Little Belt. Verified by
   point-in-polygon against the atlas rings: Als 9/9 in, Funen 0/21, Ærø 0/9,
   Langeland 0/9.

   Als falling out of a figure because an outline was generous enough for the
   mainland and not for the island is item 78, four days after item 78. **The
   island is not the problem. Closing a polygon on a straight line between two
   coastal endpoints is the problem, and it will recur in every figure that draws
   a band across this coast.**

87. **Tønder carries no count on figure 1 and should not until the returns are
   read.** Two sources give 761 Danish of 3,265 and 750 of 3,198. They disagree in
   both numerator and denominator, which is not rounding. Aabenraa (2,224/2,725),
   Sønderborg (2,029/2,601) and Højer (219/581) each appear twice and agree digit
   for digit, and those three carry their figures on the face. Tønder is marked as
   a German majority, which every source agrees on, with no number.

88. **Figure 2 does not carry party totals, and PLAN_I §13 asked for election
   statistics.** The seat arithmetic for the three 1920 Folketing elections is
   findable but does not survive a second appearance. The two pages giving July's
   changes - Venstre +3 to 51, Radikale -1 to 16, Konservative -2 to 26 - are the
   same text on two hosts, which is one witness, not two; and September's Radical
   figure is truncated in every copy found. The derived totals do not reconcile
   either: April sums to 139 of 140 seats and September to 149 against a Folketing
   said to have grown by 8 from 140.

   So the figure is a calendar of the year instead, and it is the better figure.
   The chapter's argument about 1920 is not the seat count - it is that Denmark
   held **three general elections in one calendar year for three different
   constitutional reasons**: the first because the crown tried to use a power it
   formally had, the second because the caretaker's whole brief was to pass an
   electoral law and call a vote, the third because the constitution required a
   fresh Rigsdag once Sønderjylland could send members to it. Twelve dated
   entries, every date confirmed twice, and one quantity: the Folketing grew by
   eight seats on 21 September. Party totals can go in the prose, where a flag
   carries the doubt. A number on the face of a figure cannot.

89. **Two more of item 73's six identifiers are confirmed, from inside the
   April 1920 volume itself.** Its bibliography lists *Folketingsvalgene 1895 og
   1898* at 4. R., 3. Bd., H. IV and *Folketingsvalgene 1901* at 4. R., 10. Bd.,
   H. II - both exactly as item 73 has them. That is four of the six now confirmed
   from a primary listing, with the 1876/1879 reference still the one the printed
   bibliographies get wrong (item 80).

90. **A separator convention, decided rather than drifted into.** Figures 1 and 2
   both carry thousands. Danish-language labels on figure 1 use Danish separators
   (75.431 dansk) because the phrase around them is Danish; English text uses
   English ones (164,000 people). This is deliberate and should stay that way, or
   be changed everywhere at once - it is exactly the sort of thing a consistency
   pass at the end of the book will otherwise flag as an error.

91. **Chapter 38's build path exists: `HAND[38]` and `CFG[38]` written, orphans
   cleared.** `tidy.py` reported the three figures as orphans from the moment
   `figs_38.py` ran and reports none now, which was the predicted symptom and the
   only one that matters here. Eleven sections in `CFG[38]['sec']`, three figures
   in `HAND[38]['figs']`.

   **Figure numbering is NOT PLAN_I's.** The plan lists the zones map as figure 1,
   the elections as 2 and Iceland as 3. Figures are numbered in reading order and
   Iceland is section 02, so the chapter carries Iceland as figure 1, the zones as
   figure 2 and the year as figure 3. The plan's numbering was written before the
   section order was fixed. Reading order wins; PLAN_I §13 should be amended.

   **`mw_at` is satisfied without being touched.** With eleven sections it places
   the two Meanwhile blocks at `s03` and `s07` - `secs[2]` and `secs[min(6, n-1)]`
   - so the open item from the chapter 37 session does not block this chapter. It
   is still open: the guard added in item 67 refuses a third block, and that is
   still a layout decision nobody has taken.

92. **Two vignettes are still missing and the chapter cannot ship without them.**
   PLAN_I §4 rosters three for chapter 38 and the draft has one - Johanne Marie
   Braren at Frederikshøj, which was sourced. Outstanding: **38[n]**, unnamed,
   Flensburg, 14 March 1920, which §14.6 puts last of six in the verification
   queue and which still has no subject; and **38[-]**, C.Th. Zahle at Amalienborg,
   29 March 1920, flagged in the roster as *verify the two audiences* and not
   drafted at all. §08 covers the dismissal in prose with no vignette block.
   Under D-9 the roster needs a woman as agent and a non-elite subject, and at
   present the chapter has the first and not the second.

93. **Item 92 closed: all three vignettes are drafted, and 38[n] is not in
   Flensburg.** PLAN_I §4 rostered it as *unnamed · Flensburg · 14 March 1920* and
   §14.6 put it last of six in the queue. It has no subject and I do not think it
   can get one honestly: the only Flensburg Danes who left usable records that
   week are the organisers, and an organiser is not a non-elite subject. **It is
   relocated to Amalienborg Slotsplads at Easter**, an unnamed man in the crowd,
   which is sourced - the demonstrations, the strike notice behind them, the
   Copenhagen slogan that rhymes, and the fact that the men organising him were
   working that week to make sure the republican motion was never put. D-9's
   non-elite requirement is met; Flensburg stays in the prose. PLAN_I §4 should be
   amended.

   38[-] is drafted as the 11:45 audience on 29 March. On the roster's *verify the
   two audiences*: there was **one** audience with Zahle, on the morning of
   29 March. The decision had been taken the previous day, Palm Sunday, in
   conversation with H. N. Andersen, who held no office. That is what the second
   occasion was, and it was not an audience.

94. **The Easter Crisis dates in the first draft were wrong.** It ran **29 March
   to 4 April**, not three days to 31 March. Liebe was appointed about a day after
   the dismissal; the folketog organised by Elna Munch, Jesper Simonsen and
   Stauning went to the king on Easter Saturday, 3 April, and by every account is
   what moved him; the Liebe ministry went and Friis came in on Easter Sunday,
   4 April. The strike was set for 6 April throughout. Figure 2 had the 6 April
   date right and the prose did not, which is the wrong way round.

95. **Chapter 38 now projects 8,437 page words and 40 minutes against a planned
   37, and this is no longer only item 84's model fault.** The chapter has grown
   for three legitimate reasons - the commission was a missing subject, there are
   three vignettes rather than two, and the corrections added sourced material -
   and it is now about fifteen per cent over plan. **Decision needed, and it is a
   real one.** Either 40 stands for the pivot chapter of the part, or roughly 340
   words come out; if they come out I would take them from §03, which is 57 over
   band and where the Versailles argument still restates the Clausen-line
   paragraph, and from §10, which is 58 over and is the white-horse section that
   can afford to be shorter than it is. I would not touch §08 or §09: they carry
   two of the three vignettes and both land within band now that the crowd
   vignette sits with the strike rather than with the dismissal.

96. **Chapter 38 ships at 7,844 page words and 37 minutes, against a planned 37 —
   and item 95's decision was taken on a number I had got wrong.** I told Carsten
   the chapter projected 8,437 and 40 minutes, he accepted 40, and the built page
   is 7,844 and 37. The estimate was 593 page words too high. **Stop estimating
   page length from the markdown.** Two things were wrong with it at once: the
   markdown word count of the prose came to 4,654 where `narrative.py` on the
   built page gives **4,421** (blockquote markers, the vignette attribution lines
   and the em-dashes all counted as words that do not survive the build), and the
   apparatus for this chapter is **3,423**, not the 3,783 that held over chapters
   33-37. The apparatus constant is not a constant; it tracked a ten-section
   chapter with two vignettes, and eleven sections with three vignettes shifts
   words from the apparatus into the prose without adding them to the page.

   The only honest length number is `bookstats.py` on the linked page. That was
   already the rule, from item 75, and I broke it in the other direction — item 75
   was a number taken too early in the pipeline, this was a number taken before
   the pipeline ran at all. Use the estimate to decide whether a subject is
   missing, which is what item 72 wants it for, and never to decide whether to
   cut.

   The linkindex gap held exactly: `build_part_i.py` printed 7,838 and `bookstats`
   gives 7,844.

97. **The shipped profile is 4L/2M/5H, not the 4L/3M/4H the draft was measured
   at.** `narrative.py` bands the built sections and disagrees with my markdown
   estimator on three of them: §03 reads heavy at 491, §07 heavy at 506, §09 medium
   at 363. Five heavy sections is not a defect under item 59 - the defect that
   rule names is a profile with none - but the planned profile and the shipped one
   should not be described as the same thing. PLAN_I §6 records ten sections at
   3L/4M/3H; the chapter shipped eleven at 4L/2M/5H. Amend the plan to what was
   built.

98. **Chapter 38 is shipped.** 11 sections, 3 vignettes, 2 Meanwhile, 3 figures,
   9 glossary blocks, 3 checkpoints, 5 summary items, 12 questions. Book total
   **38 of 44, 275,272 page words, 21.8 h**. Verifiers after the build: figcheck
   clean, tidy clean with no orphans, vignettes 69 with selftest passing, debuild
   11 style-only and 27 identical, fixture and seam pass.

   Outstanding against this chapter, all flagged in the prose or here: the
   commission's membership and handover date including the Claudel detail; the
   date the Conference of Ambassadors fixed the line, plus concrete departures
   from the parish result; the Jomfru Fanny prophecy's date; the rural Danish
   share, 83.5 or 83.8; Tønder's commune return; the 1920 party seat totals; and
   *Statistiske Efterretninger* 1920 nr. 23, which is the Danish official
   publication of the plebiscite returns and has still not been opened.

99. **SEVEN DRAFTING FLAGS SHIPPED ONTO THE LIVE CHAPTER 38 PAGE, and every
   verifier said clean.** The drafts have always carried italic notes addressed to
   the author, and every draft header says they are not copy. Nothing enforced it.
   Chapter 38 was built, linked, indexed and counted with seven of them on the
   page; `mkbody`, `build_part_i`, `figcheck`, `tidy`, `narrative` and `bookstats`
   all passed. About 230 words of notes-to-self were inside the shipped page word
   count, and the reader would have seen *"Flag: confirm the membership, the
   chairman's name and the handover date before this goes in as copy."*

   `mkbody.py` now REFUSES the build while any flag remains, and names each one.
   It refuses rather than stripping, for item 67's reason: a flag is an unresolved
   question and silently deleting it loses the question. The seven are now an
   explicit **Still unresolved** list in the chapter's own Sources block, which is
   where a question the chapter is carrying belongs.

   Check Parts A-H for the same fault before chapter 39. I checked the built pages
   and only chapter 38 carries `Flag:`, but the convention is older than this
   chapter and other wordings may exist.

100. **Two numbers I reported were inflated by the flags, and the profile was one
   of them.** Item 97 recorded the shipped profile as 4L/2M/5H and called the
   difference from the drafted 4L/4M/3H a disagreement between my estimator and
   `narrative.py`. It was not. The flags sat inside §03, §07 and §09 and pushed
   each into a heavier band. With them gone the built page reads **4L/4M/3H**,
   which is what the markdown said all along. My estimator was right and the
   built page was wrong, and I attributed it the other way round.

   Item 96 stands but its arithmetic shifts: the chapter is **7,826 page words and
   37 minutes**, narrative 4,194, apparatus 3,632. The linkindex gap held again -
   7,820 printed before linking, 7,826 after.

101. **I damaged the draft twice fixing this, by pattern-matching without
   looking.** The first strip used a DOTALL regex that ran past a heading and cost
   a section; the second used a line rule that mis-found the closing `*`. Both
   were caught only because `mkbody` reports its section and term counts, and both
   were repaired from the previous commit. The flag blocks needed reading first:
   one of the seven had prose spliced onto its closing line, so any rule that
   deletes whole lines silently deletes a sentence of the chapter. **Read the
   blocks, then write the rule.** The working version prints what it removed and
   asserts the heading count is unchanged before it writes.

102. **Drafting notes shipped on eight more pages, 25 to 32, and the item 99 guard
   could not have caught them.** A scan of every `<i class="dk">` span of eight
   words or more, then a wording scan, found 33 distinct author notes on live
   pages: in chapter 25 §03 a whole draft-file header (`<!-- ===== c25_draft_
   04-09.md ===== -->`, the markdown title, "Draft, sections 04–09 of 09." and a
   placement note); the same file separators as visible text on every Part G
   page, the last one on each naming the next chapter's file; four `*Drafting
   flag:` notes in chapter 32; a "Style note" citing D-6 in 27 §07; "should be
   checked" in 30 and "before this ships" twice in 31; "Attributions need checking
   … before publication" in the Sources of 25 to 31; "needs settling" in 26.
   The guard matched the literal `*Flag:` case-sensitively, so `*Drafting flag:`
   passed it and chapter 32 would have rebuilt with all four notes.

   **Fixed: the guard.** `draftnotes.py` holds one pattern, matched on
   whitespace-normalised text (one of chapter 32's notes wraps a line) and counted
   once per note; `mkbody.py` imports it and now refuses chapter 32 with five
   notes named. `python3 draftnotes.py ../[0-9][0-9]-*.html` scans the pages and
   should join the cold run; it also prints, as advisory, every long italic span
   the wording list does not match. Chapter 38's body rebuilt byte-identical under
   the new guard.

   **Not fixed: the prose.** Five of the notes are open research questions (the
   1794/1795 fire dates, the 1807 Norwegian commission, the St Jan date, the 1838
   vote, the Frederiksborg ratification's style). Parts G and H need a cleanup
   session before the final pass, and until then chapters 25–32 cannot be rebuilt
   through `mkbody.py`, which is the intended effect.

103. **Chapter 38 corrected in place, and three faults found in it that are
   recorded rather than fixed.** Corrected: three of the five carry-forward arrows
   pointed one chapter early, still on the pre-D-10 spine (the 1930s minorities to
   39, 9 April to 40, Iceland 1944 to 41), and all five used "Chapter N"; they now
   read `→ 40`, `→ 41`, `→ 43`, `→ 44`, `→ 44`. The prose said the strike was called
   off "on 31 March" and figure 3 had the king giving way on 31 March; lex.dk and
   Arbejdermuseet agree the crisis ended in the compromise of Easter Sunday,
   4 April, which is also what the chapter's own prose says two paragraphs
   earlier. Page 7,826 → 7,824; minutes unchanged.

   Recorded, not fixed: (a) the **Still unresolved** list in Sources is not the
   list the chapter 38 brief described. It has the Zone III request and the Braine
   tablets, lacks Tønder's commune return, and ends with an Easter chronology that
   is settled fact rather than a question. Its preamble also names `mkbody.py` on a
   reader page. (b) Figure 3's caption tells readers to "see the note in
   figs_38.py". Both are item 99's class in milder form. (c) **Chapter 37 says
   Munch "would hold the foreign ministry for twenty years".** He held it from
   30 April 1929 to 8 July 1940, eleven years; lex.dk, the Norwegian national
   encyclopedia and Wikipedia agree. **FIXED, item 130** - and the sweep that
   fixed it found a second error in the same chapter.

   **A house form, settled rather than drifted into.** Forward arrows inside the
   current part use `→ N`, the form the cross-reference table already gives.
   Chapter 37 uses `→ Part I` for targets inside its own part; D-1 permits both.
   The final pass can choose one.

104. **Chapter 39's verification queue, and what it overturned.**
   - **Item 81 closes wrong in kind.** *Statistiske Efterretninger* 1920 nr. 23 is
     the Danish constitutional referendum of 6 September 1920, not the Slesvig
     plebiscite: three DST election volumes (1939, 1947, 1961) cite it, and two
     give the date. The only Slesvig item in that year's *Efterretninger* is an
     area return, filed under *Areal*. None of chapter 38's six items is closed by
     it; the Commission's own publication is still the route.
   - **39[-] Glückstadt** died at Kommunehospitalet, not in Vestre Fængsel (DBL,
     da.wikipedia), on 23 June 1923 after an operation; he had been remanded in
     March and held at Vestre Fængsel. Convicted after his death.
   - **Steincke 1920 confirmed**, but the Interior Ministry *asked* for it in 1919,
     so §08's working title was wrong; and the same report carries the eugenic
     programme behind the sterilisation law of 1 June 1929.
   - **§02's premise was wrong.** There was no exchange of marks into kroner.
     Danish reckoning began on 20 May 1920 at about a seventh of a krone and mark
     debts stayed in marks (Sømod). 39[n] relocated to the encased-stamp small
     change at Haderslev, April 1921.
   - **Nina Bang confirmed** (23 April 1924 – 14 December 1926; Kollontai
     correction), and the Norwegian national encyclopedia still prints the myth.
   - **Unemployment 1910–1930:** identifiers 4. R. 48. Bd. 5. H., 61. Bd. 4. H.,
     74. Bd. 2. H., 88. Bd. 4. H., confirmed three times; the tables were not
     reachable (the fetch tool refuses constructed URLs; search did not surface
     them). **Direct dst.dk links from Carsten would unblock the figure.**
   - **Seats 1884–1924 refused:** every copy is one lineage (Mackie & Rose), one
     witness under item 88. The 1924 Folketing is primary and is figure 3.
   - **Landmandsbanken's capital split and total loss** each rest on one account
     (Christiansen in G&P); the calendar figure carries only double-witnessed
     dates and quantities.
   - **Open disagreements carried in the chapter's Sources:** Stauning I dated
     23 April 1924 almost everywhere and 24 April in lex.dk's Stauning article;
     twelve fined (lex.dk) against three fined and the rest acquitted (G&P);
     Glückstadt's conviction dated only by da.wikipedia.

105. **`mapspine.CHAR_W['mapt']` under-estimates the class by about a tenth, and
   it shipped one overrun.** Measured this session by rendering 100 characters
   through `rasterise()`'s own CSS: mapt 6.36, mapx 5.32, mapl 6.61 units per
   character, against the table's 5.68, 5.63 and 6.98. The table cannot be right
   anywhere: mapt is 9.5px and mapx 8.5px at the same letter-spacing, so mapt must
   be about a ninth wider, and the table has them nearly equal. Chapter 39's
   figure 2 ran off the canvas with every guard clean, and was found in the
   raster. At measured widths, one shipped figure crosses the canvas edge:
   `svg_titles.txt`, the *husbond* line. **CONFIRMED AND FIXED, item 131** - it
   was losing "re." off "before." on the shipped page. A sweep of every figure now
   returns zero. **The CHAR_W correction itself is still open and is now the only
   thing left in this session**, item 129 having closed the `fill=` half.

   **Not changed in `mapspine`, and it needs a decision.** Every `fold()` in
   `figs_37.py` and `figs_38.py` reads `CHAR_W`; correcting it re-wraps their text
   and breaks byte-identical regeneration for shipped figures. `figs_39.py` folds
   at the larger of measured and table width and says so. Recommendation: correct
   the table in one session that regenerates and re-inspects every affected figure
   at once, and measure in the Mac's environment too, since the fonts differ.

106. **Chapter 39 is shipped.** 10 sections, 3 vignettes, 2 Meanwhile, 3 figures,
   9 glossary blocks, 3 checkpoints, 5 summary items, 12 questions.
   **7,455 page words and 36 minutes** on `bookstats.py` after linking
   (`build_part_i.py` printed 7,449; the six-word gap held). Profile
   **3L/4M/3H at 4,082 narrative** against 4,053 planned; apparatus **3,373**.
   The page is 384 words under PLAN_I's 7,839, and all of that is apparatus,
   which is what §1.6 now says to expect; nothing was cut or padded.

   The first draft measured 5L/3M/2H at 3,705. Three subjects were missing, per
   items 72 and 83: the electoral machinery of 1920 (§06), Sønderjylland's entry
   into Danish administration and politics (§02), and Nina Bang's career before
   1924 (§07). Seventh chapter running.

   Book: **39 of 44, 282,707 page words, 22.4 h; 5 remaining, 1 dense.** After the
   build: tidy clean apart from Part D's ten and the fifteen A–D bodies a fresh
   clone also lacks; no orphans; fixture and seam pass; debuild 11 style-only and
   28 identical; vignettes 72, selftest passing, chapter 39 fully tagged;
   figcheck 72 matched, 41 sourceless, 0 stale; draftnotes clean on 33–39; maps,
   `figs_37`, `figs_38` and `figs_39` regenerate byte-identical.

   Figures were rasterised and looked at; the raster found two faults the guards
   passed: a label under its own bar in figure 1 (item 47's class; the bar origin
   is now computed from the widest label), and figure 2's overrun (item 105).

   **Where chapter 39 differs from the standard account:** Glückstadt as the
   scapegoat of a closed system rather than a lone villain; Munch's 1922 position
   as a considered one, read forwards rather than from 9 April; the return to gold
   as a policy whose cost fell on debtors and on the newest province; Steincke's
   plan as one programme with two halves; the disarmament bill as a Folketing
   majority that never became law.

   The index blurb for chapter 39 said the Social Democrats "struck against the
   king"; the strike was the unions', and never struck. Corrected in
   `index_generator.py`.

107. **Chapter 38's measured numbers went stale when chapter 39's session edited
   it, and PLAN_I still carries the old pair.** The chapter 40 cold run found
   chapter 38's narrative at **4,197**, not the 4,194 in item 100 and in PLAN_I
   §6. The cause is fully accounted for: commit `9a820e4` changed chapter 38 in
   three places and re-measured none of them. "called off on 31 March" became
   "called off after the settlement of Easter Sunday", **+3 narrative**; the five
   forward arrows lost the word "Chapter", **−5 outside**; and the `svg_aar_1920`
   timeline changed a date. +3 and −5 is the −2 that took the page from 7,826 to
   7,824. Item 103 recorded the page correction and nobody re-ran `narrative.py`.

   **Corrected in PLAN_I §6 to 7,824 and 4,197.** Item 100 is left as written,
   because it is a dated record of what was reported then, and item 103 already
   carries the page correction. **The rule this earns: editing a shipped chapter
   means re-running `bookstats.py` and `narrative.py` on it and amending PLAN_X
   in the same session, not only the ledger.**

108. **The 1939 arithmetic holds, and the 1933 reform does not do what PLAN_I §8
   says it does. Debt 3's residue is paid, but not by a restoration, and chapter
   44 does not close it by an abolition.** This is the chapter's largest finding
   and it reaches forward.

   - **1939 verified.** Yes 966,277, no 85,717, twice (the Interior Ministry's
     referendum tables; lex.dk). Yes was **91.85 per cent of valid votes and
     44.46 per cent of the electorate**, against **§93 of the constitution of
     1915**: a majority of those voting *and* "mindst 45 pCt. af samtlige
     Vælgere". PLAN_I §8's "over ninety per cent" and "44.5" both stand.
   - **§93, not §94.** The plan did not name a section; the section is 93.
   - **The 1933 reform never touched the disqualification.** The 1915 §30(b)
     disqualified anyone who "nyder eller har nydt Understøttelse af
     Fattigvæsenet, som ikke er enten eftergivet eller tilbagebetalt", and it
     cost *valgret og valgbarhed* to the Rigsdag **and** the municipal councils,
     plus permission to marry and authority over one's children. The Lov om
     offentlig Forsorg of 20 May 1933 left §30 standing and provided instead, in
     **§1 stk. 3**, that "Modtagelse af offentlig Hjælp medfører kun
     Indskrænkninger i Modtagerens borgerlige Retsstilling i de Tilfælde og i det
     Omfang, nærværende Lov udtrykkelig bestemmer." Assistance was split three
     ways and only the residual *fattighjælp* still carried the loss. **A
     redefinition, not a restoration.** PLAN_I §8's test — "if it was separate,
     the residue moves" — is answered: it was not a separate act, so the residue
     stays in 40, but the claim changes.
   - **1953 does not abolish it either, and this is what chapter 44 must be told.**
     §29 stk. 1 of the constitution of 1953 reads "…medmindre vedkommende er
     umyndiggjort. **Det bestemmes ved lov, i hvilket omfang straf og
     understøttelse, der i lovgivningen betragtes som fattighjælp, medfører tab
     af valgret.**" Confirmed twice (danskelove.dk; the EU Fundamental Rights
     Agency's text). **The sentence is in the Danish constitution today.** So 44
     closes debt 3 by **delegation** — the constitution ceasing to name the poor
     itself — and not by abolition. Chapter 44 §03 needs rewriting to that, and
     it is a better ending than the one the plan expected.
   - **When it actually ended is not established** and is chapter 44's to find:
     the trail runs through whatever later statute stopped defining anything as
     *fattighjælp*.

109. **The unemployment volumes are identified at last, and the blocker is not
   the one we thought.** PLAN_I §14.4 and item 104 have wanted these since
   chapter 39: **Arbejdsløsheden i aarene 1931–35 is 4. R. 100. Bd. 2. H. (1937)
   and 1936–40 is 4. R. 115. Bd. 4. H. (1942)**, from the department's own
   publication list. Half of §14.4 is therefore closed — naming them was never
   the hard part.

   **Reaching them is, and the reason is now precise rather than vague.** Item
   104 said "the fetch tool refuses constructed URLs". That is not it. A dst.dk
   volume surfaced by search fetches perfectly well — the 1939 election volume
   was read this session — but **the fetch truncates every volume around page 34**
   of two hundred and more, and the tables sit deeper. The container has no route
   to dst.dk at all (the egress proxy rejects it). The browser pane opens the
   PDFs and the viewer will not render the scanned pages, and clicks cannot be
   dispatched into its frame. dst.dk's own historical browser filters by ASP.NET
   postback, which did not survive scripted navigation.

   **What would unblock it:** the PDF opened at the right page and the table
   pasted in, or those two volumes downloaded and attached. Nothing else tried
   this session works. Chapter 40 ships without the series and says so in
   `figs_40.py`.

110. **`fill=` on classed figure text is a silent no-op, and it has been shipping
   since Part D. Thirty-three figures are affected.** Both `style.css` and
   `mapspine.rasterise()` set `fill` on `.mapt`, `.mapl` and `.mapx`. **A
   stylesheet rule beats a presentation attribute**, so every
   `<text class="mapt" fill="#…">` in this repository renders in the class colour
   and not the one the script asked for. No guard can see it: the markup is valid,
   `overruns` and `collisions` are geometric, and `figcheck` compares the page
   against the source, which carries the same dead attribute.

   Found in chapter 40's figure 3, where "YES 44.5%" was written in paper-white
   for a dark green bar and rendered in `#5F6157` grey on it — **found in the
   raster and nowhere else**, which is item 47's class again and the third time
   the look-at-it rule has paid.

   **Convention D-11, settled here: a figure sets text colour with `style=`, never
   `fill=`.** `figs_40.py` does. The thirty-three shipped figures are **not**
   changed, for item 105's reason — regenerating them breaks byte-identical
   rebuild across four parts — and they belong in the same session that fixes
   `CHAR_W`. **The four worst are `svg_andel_1882`, `svg_crowns`,
   `svg_deadlock_1873` and `svg_franchises_1866`**, which each ask for `#F0F2EE`
   on `.mapl`: near-white text that is almost certainly sitting on a dark shape
   and is now rendering `#3C3E36` dark on dark. Those should be looked at first.

   **CORRECTED AND CLOSED, item 129.** They were looked at. The count is
   **thirty-five** figures and not thirty-three; there is a **fifth** near-white
   figure, `svg_fealty`; only **twenty** of the 334 affected text elements are
   legibility failures; the repair is **separable from CHAR_W**; and honouring the
   requested colours would have **fixed eleven and broken nine**, because the
   grounds are drawn at opacity and nobody had composited them. All five are
   fixed. The thirty remaining are cosmetic.

111. **Chapter 40 is shipped.** 11 sections, 3 vignettes, 2 Meanwhile, 3 figures,
   9 glossary blocks, 3 checkpoints, 5 summary items, 12 questions.
   **8,358 page words and 40 minutes** on `bookstats.py` after linking
   (`build_part_i.py` printed 8,352; the six-word gap held). Profile
   **3L/5M/3H at 4,318 narrative** against 4,446 planned; apparatus **4,040**.

   **It sits exactly on decision 2.1's 40-minute advisory ceiling, and the
   narrative is not why.** Narrative came in 128 words *under* plan. The weight is
   in `outside`, 2,487 against Part I's previous mean of 1,993: an eleventh
   section's worth of contents and headers, and a Sources block that is the
   longest in the book because this chapter carries more contested numbers than
   any before it. Sources was compressed from 816 words to 722 without dropping a
   single attribution, which took the page from 8,447 to 8,358, and it was not
   compressed further because what is left is all attribution. **If the final pass
   wants the chapter under 40 minutes, the place to look is `outside`, not the
   prose.**

   The first draft measured **7L/3M/1H at 3,577**, 869 short. Item 72's rule held
   for the eighth consecutive chapter and the missing subject was real and
   load-bearing: **the parliamentary arithmetic**. The draft never said what the
   election of 16 November 1932 left the parties with, and — worse — it went from
   "the government still did not have the Landsting" in 1935 straight to "both
   chambers passed it" in 1939, with nothing in between. **The Landsting election
   of 22 September 1936, won 38 seats to 37, is what made the 1939 referendum
   possible at all**, and without it the chapter could not explain its own ending.
   Added to §03 and §09; the profile then came out at exactly 3L/5M/3H.

   Figures were rasterised and looked at. The raster found the `fill=` fault
   (item 110). An assertion found a second: figure 3's residue of the two
   published shares was labelled "did not vote" when it is everyone who did not
   vote **yes or no**, a segment that silently includes the spoiled ballots. The
   assertion that caught it now runs the other way and uses the gap against the
   published turnout as an independent check that the spoiled share is the half a
   per cent the absolute counts claim.

   **Where chapter 40 differs from the standard account:** Kanslergade as a trade
   rather than a founding, in which the social reform was Venstre's price and not
   the point; the reform of 1933 as a redefinition of poverty rather than a
   restoration of the franchise; Steincke's principle and Steincke's sterilisation
   laws as one programme and not two, thirteen months apart; Danish Nazism as
   something that came out of Danish nationalism rather than across the border,
   with Frits Clausen — who wanted the border at the Eider — as the proof; and the
   1939 referendum as a failure of attendance rather than a defeat.

   **The plan gap in chapter 38's → 40 arrow is closed by a new section, not by
   re-pointing the arrow.** PLAN_I §8 gains §07, *Påskeblæsten*: the press
   offensive of March–April 1933 against the 1920 border, and the nazification of
   the German minority that followed it. Re-pointing to 41 would have duplicated
   chapter 38's existing → 41 arrow, and "spend the 1930s" is this chapter's
   decade. **Chapter 40 is therefore eleven sections, not ten**, and PLAN_I §8 is
   amended to 3L/5M/3H.

   **The roster changed, and the plan is amended.** PLAN_I §4 had 40[-] as
   "Stauning and the negotiators · Kanslergade 10" and 40[f] unnamed. They are
   swapped. **40[f] is Augusta Erichsen**, Stauning's live-in partner, the only
   person in the flat who was not a politician, and the author — *Mit liv med
   Thorvald Stauning* (1967), pp. 45–47 — of the account historians use for what
   that room was like, since no minute was taken. **40[-] moves to Frits Clausen
   at Bovrup**, which puts the `[-]` where the chapter's argument about Danish
   Nazism needs it. **40[n] stays unnamed at Nakskov**, on the 38[n] precedent:
   the events are triple-witnessed but no source consulted gives the provision the
   nine were charged under, so the vignette names none.

   Book: ~~**40 of 44, 291,154 page words**~~ **291,065** — see item 112; the
   291,154 was 282,707 plus chapter 40's *pre-correction* 8,447 and was never
   recomputed. **23.1 h; 4 remaining, 1 dense.** After the
   build: tidy clean apart from Part D's ten and the fifteen A–D bodies a fresh
   clone also lacks; no orphans; fixture and seam pass; debuild 11 style-only and
   29 identical; vignettes 75, selftest passing, chapter 40 fully tagged;
   figcheck 75 matched, 41 sourceless, 0 stale; draftnotes clean on 33–40; maps,
   `figs_37`, `figs_38`, `figs_39` and `figs_40` regenerate byte-identical.

112. **The book total was carried forward by addition for the third time in four
   sessions, and it was 89 too high.** The chapter 41 cold run read
   **291,065** page words on a fresh clone against the 291,154 in this ledger and
   in `START_HERE_part_I_c41.md`. Nothing in the repository was wrong. The chapter
   40 entry recorded the chapter cut **from 8,447 to 8,358** by a late fix to an
   attribution, and then recorded the book as 282,707 + 8,447. The chapter was
   corrected; the total it had already been added to was not.

   The same failure had already happened once and self-corrected: the 38-of-44
   total of 275,272 used chapter 38's pre-correction 7,844, and the chapter 39
   session recomputed from the pages and got 282,707, which is right.

   **Rule: a book total is read off `bookstats.py` on a fresh clone, never
   obtained by adding this chapter to the last one.** The same applies to the
   figure in any `START_HERE`. Corrected in place above.

113. **The sixteen dead of 9 April: the number is right and the sentence everyone
   writes around it is wrong.** Thirteen were soldiers. **Three were border
   gendarmes** — J. P. Birk, A. S. Albertsen and A. A. Hansen — shot at the
   Padborg railway viaduct at about four o'clock, a quarter of an hour *before*
   the army crossed at Kruså, by three men of *Regiment Brandenburg* in civilian
   clothes who had walked up and asked the way to the station. Birk died where he
   fell; Hansen lived long enough to describe it to a police assistant named
   Petersen, which is the only reason the circumstances are known.

   The sources disagree and the disagreement is the finding. Grænseforeningen's
   *Niende april 1940* says sixteen **soldiers** killed and 23 wounded. lex.dk's
   *9. april 1940* enumerates thirteen soldiers and then mentions the three
   gendarmes separately without adding them in. historienet.dk gives sixteen and
   names the gendarmes among them. krigendagfordag.dk lists thirteen soldiers by
   name, unit and place. **Thirteen plus three is the only reading consistent with
   all four**, and it is what chapter 41 uses, in the prose and in the myth-check.

114. **41[-]: what Scavenius signed in Berlin cannot be read, and the vignette
   says so instead of paraphrasing it.** Denmark acceded to the Anti-Comintern
   Pact on 25 November 1941 under an ultimatum delivered on the 23rd, after
   Renthe-Fink's note of the 20th and his remark on the 21st that a refusal
   "would not be understood in Berlin", and after Scavenius broke a cabinet
   majority against signing by threatening to resign. **The four Danish
   reservations are referred to by every mainstream account and their text is in
   none of the accessible sources**; dengang.dk has Ribbentrop attempting to
   ignore them and a night of argument attaching them; the communist account
   (kpnet.dk) denies there were any reservations at all. What *is* primary and
   reachable is the Foreign Ministry's press release of that day
   (krigendagfordag.dk), which told Danes the pact bound Denmark neither
   militarily nor politically and rested the decision on the Communist Law
   already passed — and the government's own acceptance that signing breached the
   constitution and was a *nødretsforanstaltning*.

115. **41[f] is Kate Fleron, and the move that found her is the one that found
   Augusta Erichsen: look for the person keeping records nobody asked for.**
   Journalist at *Nationaltidende* from 1930; her editor Aage Schoch removed on
   German demand on 1 January 1942 and she squeezed out weeks later; on the
   editorial board of *Frit Danmark* — first published **9 April 1942, two years
   to the day** — by mid-year, as *frøken Krog*; betrayed in September 1944,
   Vestre Fængsel, Frøslev, out days before the capitulation; and in 1945 the
   compiler of *Kvinder i Modstandskampen*, because the accounts of the resistance
   were being written by the men who had been in it. She is the only vignette
   subject in Part I who is also one of the part's sources.

116. **Chapter 41 needed an eleventh section and PLAN_I had no home for it
   anywhere.** The realm came apart in the thirteen months after 9 April 1940 —
   Iceland's Alþingi taking the king's powers on 10 April, Britain taking the
   Faroes that week and recognising *Merkið* on 25 April, Britain taking Iceland
   on 10 May, and **Henrik Kauffmann signing away Greenland base rights to the
   United States on 9 April 1941, a year to the day, in the king's name and
   without authority, being recalled on the 12th, dismissed on the 16th and
   charged with treason — and the Rigsdag ratifying his treaty on 12 May 1945,
   seven days after the liberation.** PLAN_I §11 gives chapter 43 "Iceland gone,
   the Faroes refused" and 4 April 1949, and both arrive without a cause unless
   this is told where it happened. New §05, *The realm comes apart*.

   **This is the second consecutive chapter whose missing subject was a hole in
   the plan and not thin prose** (chapter 40's was the parliamentary arithmetic).
   The planning lesson is not "drafts land short"; it is that the plan's section
   list is the thing to distrust, and the test is to ask which later chapter is
   left with an uncaused event.

117. **"Six hours" was a section title asserting a duration no source supports,
   and it had propagated to the published index.** From the shooting at the
   viaduct (about 04.00) to the last firing in Haderslev (08.15) is **four hours
   and fifteen minutes**; from the crossing of the border (04.15) to the
   government's acceptance of the German terms (06.00) is **one hour and
   forty-five minutes**. §03 is renamed *From four o'clock to a quarter past
   eight*, and `index_generator.py`'s blurb for chapter 41, which read "Occupied
   in six hours", is corrected at source. **A section title is a claim and belongs
   in the verification queue with the rest of them.**

118. **Chapter 41 ships at 8,678 page words and 41 minutes, one over the advisory
   ceiling, and how it got there is the useful part.** 11 sections, 3 vignettes, 2
   Meanwhile, 3 figures, 9 glossary blocks, 3 checkpoints, 5 summary items, 12
   questions. `narrative.py` reads **4L/4M/3H at 4,429**.

   The first build was **10,447 words and fifty minutes**. The narrative was only
   292 words above chapter 40's. **The apparatus was 1,821 over, and 1,339 of that
   was the Sources block**, written at 2,046 words against chapter 40's 707 — a
   research log with a sources heading on it. Cutting the tail blocks back to Part
   I norms took the chapter to 8,777.

   **Then five rounds of sentence-tightening recovered 274 words in total.** That
   is L1 exactly — *paraphrasing is not cutting* — demonstrated from the other end,
   on a chapter that needed to lose and not to gain. The remaining 278 words are
   not available except by deleting a subject. **Rule: when a chapter is long, the
   apparatus is the first place to look and the Sources block is the first thing
   to measure; the prose is the last.** A Part I Sources block is about 700 words.

   Left at 41 deliberately. **If it must come to 40, the section to delete is §07,
   *The economy of accommodation*** — the weakest-sourced in the chapter, already
   down to 295 words, and chapter 43 needs only *værnemager* from it.

119. **Two dst.dk volumes were fetched this session by a route item 109 does not
   record, and the unemployment series may be worth one more attempt.** Item 109
   says the fetch truncates every volume around page 34. The 1943 election volume
   (*Stat. Medd.* 4. R. 120. Bd. 1. H.) and the census of 5 November 1940 (4. R.
   113. Bd. 3. H.) both came back this session **through `dst.dk/pubfile/<cid>/<name>`,
   reached from the `VisPub?cid=` publication page** rather than the `pukora`
   path — and the census returned **table 1 on page 11** with the population of
   3,844,312. That is not deep, but the route is different and untested on the two
   volumes item 109 names. **Try `VisPub?cid=` → `pubfile` on 4. R. 100. Bd. 2. H.
   and 4. R. 115. Bd. 4. H. before anybody goes to a reading room.**

   **And the OCR is lossier than item 109 records.** The 1943 volume renders the
   DNSAP as 48,809 and Dansk Samling as 43,867; those two overshoot the volume's
   own total of valid votes by 5,972. lex.dk's figures reconcile with that total
   to within 28 votes. **Check a fetched table against its own total before using
   any number in it** — the arithmetic caught this, not the eye.

120. **The chapter 37 weight profile was transposed in the ledger's own summary
   block and had propagated through two START_HERE briefs.** The chapter 42 cold
   run measured chapter 37 at **3L/4M/3H**, against the 4L/3M/3H carried by the
   "Part I as built" table above, by `START_HERE_part_I_c41.md` and by
   `START_HERE_part_I_c42.md`. Narrative words matched exactly (4,207), and the
   sections are nowhere near a band edge — §04 is 248 words and §09 is 400
   against a light/medium threshold of 336 — so nothing was flipping on a
   rounding boundary.

   **Item 75, written in the chapter 37 session, records 3L/4M/3H "exactly as
   PLAN_I §5 specified", and PLAN_I §5 specifies 3L/4M/3H.** The contemporaneous
   record and the plan agree with the tool; the summary table disagreed with all
   three. Corrected in place above.

   This is item 112 in a different column: a number copied into a summary instead
   of read off the tool that produces it. **Rule, extending 112: the profile
   column of the "Part I as built" block is read off `narrative.py` on a fresh
   clone, exactly as the book total is read off `bookstats.py`.** Neither is ever
   carried forward from the previous brief.

121. **Chapter 42's verification queue, and what it overturned. Two of the three
   vignettes carried a wrong label and the third rests on sealed papers.**

   - **42[n] was not executed where the plan says.** Kim Malthe-Bruun was
     sentenced by court-martial on 4 April 1945 and **shot at Ryvangen on the
     6th**; Vestre Fængsel is the dateline of the farewell letter and **was never
     an execution site**. Dansk Biografisk Leksikon, lex.dk, Frihedsmuseet's
     catalogue and the Mindelunden memorial roll agree. This is item 117's class
     again — a place asserted in a label — and it is the second consecutive
     chapter in which the plan's own vignette line carried an unverified claim.
     A myth-check comes free with it: the letter names the three sentenced with
     him as "Jørgen, Niels og Ludvig", and the Ryvangen roll for 6 April gives
     Jørgen Frederik Winther, Ludvig Alfred Otto Reventlow and **Peter Wessel
     Fyhn**. No source reconciles the Niels. Most likely a cover name; nobody has
     shown it.
   - **42[f] did not sail and was not arrested in 1943.** Ellen Wilhelmine
     Nielsen sheltered people at Rønne Allé 42 in Dragør and arranged passage
     with fishermen she had known all her life; **no source says she owned or
     sailed a boat and none names one.** Arrested **27 July 1944** with eleven
     Dragør fishermen; Vestre Fængsel, Frøslev, **Ravensbrück as prisoner
     94,315**, then the Jugendlager at Uckermark; out by white bus on 8 April
     1945. Not Horserød and not Theresienstadt.

     **The number she is credited with is undocumented and the sources are one
     source.** Published figures run from two to seven hundred; four of the most
     cited web accounts are by the same author, who gives three different
     numbers; the 700 is the total for everyone who left from Dragør and is
     routinely printed as hers. The family account says fifty to seventy-five.
     The scholarly treatment — Cherine Munkholt's two papers on dragoerhistorie.dk
     — is **blocked at the egress proxy** and would probably settle the one date
     that remains open, the Ravensbrück transport of 11 or 14 December 1944.
   - **42[-] is worse than "rests on his own diary", which is what the plan
     warned.** The 28 September date holds and is well attested. But Gunnar
     Paulsson (*Journal of Contemporary History* 30, 1995) reports that the
     opened Swedish archives show Duckwitz issued a visa on 19 March 1943 and
     another on 15 January 1944 **and nothing between them** — so the Stockholm
     errand to Per Albin Hansson, the most repeated detail in the story, may not
     have happened. The papers went from Rigsarkivet to USHMM, where the
     catalogue lists a **calendar** for 1943–44 rather than a diary, and the
     collection is **restricted until 2048**. The chapter prints Kirchhoff's
     chronology by name with Paulsson's challenge beside it.

122. **The October 1943 figures: one of them is exact and the famous one is an
   addition somebody else performed.**

   - **472 deported from Denmark, of whom 470 reached Theresienstadt.** Silvia
     Goldbaum Tarabini Fracapane built this from the transport registration lists
     (Yad Vashem Archives 0.64/275) and can name the two men who are the
     difference — Michael Singerowitz, sent on to Majdanek and dead there on
     21 January 1944, and one man held at Sachsenhausen and moved to Mauthausen
     with the banknote-forging unit. **The rival 481 is a demonstrable double
     count** of the ten who arrived from Sachsenhausen and Ravensbrück in early
     1944. 464 is superseded and "knap 500" is 472 rounded by people without the
     lists. This is a nominal count, not an estimate, and it is the most solid
     arithmetic in the chapter.
   - **"About seven thousand to Sweden" is exactly the pre-rounded number PLAN_I
     §10 feared, and 7,742 is a construction.** Sofie Lene Bak states 7,056 Jews
     and 686 non-Jewish spouses as two separate facts; others add them; where the
     sum appears alone it is unsourced and relabels all 7,742 as Jews, which
     inverts what the 686 means. **The only figure attached to a named archive**
     is Dansk Jødisk Museum's *Safe Haven* database — Swedish police arrival
     protocols from Riksarkivet Stockholm, about 6,336 reports analysed, giving
     roughly **7,400** — and the museum states the material is incomplete, so it
     is a floor.
   - **The Safe Haven database gave up something better than a number.** More
     than a thousand of those registering in Sweden **gave their religion as
     Protestant, Lutheran or Christian.** The tidy partition into Jews and
     non-Jewish spouses does not survive the registers, and what it dissolves
     into is the chapter's best paragraph.
   - **"53 died" has two incompatible derivations that land on the same number.**
     Fracapane's 53 is 51 dead at Theresienstadt plus the two who died after
     transfer, with the two camp-born infants counted **separately** (so 55 on
     her accounting). The popular 53 is 51 plus the infants. **Print the
     definition with the number or do not print it.** Her survivor figures are
     419 of the original 472 and 423 home on the white buses, the gap being
     spouses and children born in the camp — and that gap is where most of the
     published confusion comes from.
   - Arrests reconcile: about **284** on and around the night of 1–2 October (202
     in Copenhagen, 82 west of the Great Belt), the rest taken later, for 472.
     Gilleleje church loft is the night of 6–7 October and the number is given as
     60, 80 or 90; the informer was never established, the one conviction being
     overturned on appeal.

123. **Bornholm: chapter 42 owns the bombing, chapter 43 owns the occupation —
   and 43[n] therefore has to move.** PLAN_I gave 42 §10 "4 May 1945 — and
   Bornholm" and 43 §05 "Bornholm under the Soviets", and the question of who
   owned 7–8 May was open.

   **Settled: 42 carries 4 May, the raids of 7 and 8 May and the Soviet landing
   of the 9th; 43 carries the eleven months and the withdrawal.** Splitting it
   the other way leaves 42 §10 with nothing to say and opens 43 §05 on Soviets
   already ashore. And 43's half is where the value is: the Soviet note of
   5 March 1946 conceded withdrawal only if Denmark held the island *"uden nogen
   som helst deltagelse af fremmede tropper"*, and Gustav Rasmussen told the
   Americans (FRUS 1946 V, doc. 259) that this was **the only condition**. That
   sentence governs Danish policy on Bornholm into the 1980s and it is what
   43 §09 and §10 need.

   **Consequence: PLAN_I §4's 43[n], an unnamed vignette at Rønne on 7–8 May, is
   now inside chapter 42's span.** Either it becomes a 42 vignette or 43 takes a
   subject from the *russertid* instead. The strongest candidate found is
   **Wilhelmine Heinø**, evacuated from Rønne hospital and dead at 22:50 in an
   overcrowded ward at Aakirkeby, with her husband Charles Carlsen Heinø's
   account — **and she is not one of the ten counted dead**, which is the
   interesting part and also the trap.

   **The ten dead have a cause and it is not luck.** Nine died in Rønne on the
   7th and one in Nexø; **nobody died on the 8th**, the day the towns were
   destroyed, because Danish officials began evacuating both at 04:00 that
   morning. 212 buildings destroyed in Rønne and 175 in Nexø.

124. **PLAN_I §10's ten sections do not hold, and it is the third consecutive
   chapter whose missing subject was a hole in the plan.** Chapter 40's was the
   parliamentary arithmetic, chapter 41's was the loss of the North Atlantic, and
   chapter 42 has **two**, found by item 116's test — which later chapter is left
   with an uncaused event.

   - **How the underground was armed has no section anywhere.** Chapter 41
     carries no SOE, no drops and no weapons and says so in its Sources; PLAN_I
     §10 has no section for it either, only "Sabotage, and the counter-terror".
     So SOE's Danish section from October 1940, Bruhn dead on the first drop when
     his parachute failed over Haslev on the night of 27/28 December 1941, Muus
     from March 1943, the reception groups and Hvidsten, Toldstrup's 289 fields,
     600–700 tonnes in something like 6,500 containers, 7,500 Husqvarna weapons
     out of Sweden, and **an underground army near 60,000 in May 1945** are all
     homeless. Chapter 43 cannot tell the *retsopgør* without them: the 21,800
     interned after 5 May were arrested by those people.
   - **The Freedom Council at "light" cannot carry what chapter 43 needs.**
     Founded 16 September 1943, a fortnight after the government stopped
     functioning; recognised de facto by the Soviet Union in 1944 and never by
     the Western allies; it ran the People's Strike by proclamation; and it took
     **nine of the eighteen seats** in the liberation government. Promoted to
     medium.
   - **And drafting found a third: the Danish police.** On 19 September 1944 the
     Germans arrested the police and deported some two thousand of them, and
     **Denmark had no police from that day to the liberation.** No section in
     PLAN_I §10 or §11 carries it, and chapter 43's *retsopgør*, the informer
     killings and the rise in crime all need it. **Not yet verified in detail** —
     it was found at drafting, after the verification queue had closed, and the
     numbers above are the ones to check first.

   **The planning lesson, stated for the third time and now with a count:** the
   plan's section list has been wrong in the same direction in every chapter of
   Part I since 39. It is not that drafts land short. It is that a section list
   written before the research cannot know which causes a later chapter will
   need, and the only test that finds the gap is to read the *next* chapter's
   section list and ask what arrives in it without a cause.

125. **Decision 2.7 tripped, and the two-pass tightening evidence is the useful
   part.** The first draft of chapter 42's eleven sections measured **7,801
   narrative words** on the markdown estimator, against 4,429 for chapter 41 and
   a plan of about 4,900 — with the profile at 0L/1M/7H and **three sections past
   the 760 band ceiling entirely**, which is item 59's defect inverted.

   - **Pass 1**, deleting whole paragraphs and moving evidence into the Sources
     block and the figure docstrings: 7,801 → 6,743. **1,058 words.**
   - **Pass 2**, sentence-level work on the two longest sections: 6,743 → 6,679.
     **64 words.**

   That second number is item 118's lesson demonstrated a second time and from
   the same end: **paraphrasing is not cutting**, and the recovery curve
   collapses after the first pass. There is no fifth round that finds 1,800
   words.

   **BUILT AND MEASURED, because 2.7's trigger is a page length and item 96 says
   never to estimate one.** `bookstats.py` after `linkindex.py` gives **11,608
   page words and 55 minutes**, against a trigger of 8,400 and an advisory ceiling
   of 40. `build_part_i.py` printed 11,602 and the six-word gap held for the
   fourth time. Narrative measured **6,688** against the markdown estimator's
   6,679, nine words out — the estimator is fine and the chapter is not.

   **And the diagnosis is the opposite of chapter 41's, which is the useful
   part.** Chapter 41 was long because its Sources block was a research log;
   the apparatus was the culprit and the prose was innocent. Chapter 42's
   apparatus is 4,920 against chapter 41's 4,249, and nearly all of that
   difference is `outside` — 3,057 against 2,487 — which is the eleventh section's
   share of the contents, the rail and the tail. **The Sources block came in at
   the Part I norm on the first build.** So item 118's rule was applied, the
   apparatus was measured first, and it cleared: this chapter is long because it
   has too many subjects, not because its tail is fat. There is nothing to
   recover by tightening and the profile says so — **0L/1M/8H with two sections
   still over the band ceiling**, after two passes.

   **DECIDED: the chapter is not split now, and the question is not "split 42".**
   Carsten's call, and it reframes the problem correctly. The seam proposed here
   — between "Those who did not get away" and "Danmarks Frihedsråd" — was chosen
   with only one side of it drafted, and the material on the far side is chapter
   43's, which does not exist yet. **The partition is deferred to a boundary pass
   over the whole 1943–1955 run, once the rest of Part I is drafted: see item
   128.** Chapter 42 stands at eleven sections and 55 minutes in the meantime,
   deliberately and on the record.

126. **`figs_42.py` is built and the raster found three faults that every guard
   passed. Fourth chapter running.** `validate`, `overruns` and `collisions` were
   clean on all three before a human eye saw any of them.

   - **Figure 1's uncertainty band read as a third segment of the bar.** The
     range on the Sweden estimate, 7,000 to 7,742, was drawn as a pale block
     inside the bar; on the raster it read as pale block, then red block — three
     categories where the figure has two and an uncertainty. **Redrawn as a
     whisker with end caps below the bar**, which cannot be read as a quantity.
     This is item 118's legend fault in a new dress: the guards are geometric and
     cannot see a shape that means the wrong thing. *(Pointer checked 19 Sept
     2026: item 118 is chapter 41's length and says nothing about legends, and no
     item in this ledger records a legend fault under any number. The nearest
     recorded lesson is item 47, a key swatch run through by a line. The rule the
     sentence means is real; the reference is not.)*
   - **Figure 3 shipped an axis of fourteen unlabelled ticks.** A reader could
     not find a date on it. An unlabelled tick is valid markup that collides with
     nothing, so nothing complained. Day labels added, and the index-to-date
     inverse is **asserted against the forward map at both ends and across the
     June/July join** rather than trusted.
   - **Figure 3's three shaded bands had no legend at all** — a green block, a
     paler green block and a grey block, with nothing saying which was the
     strike. Swatches added, per item 118.

   **And a new one worth a rule: `&` in drawn text needs two rulers or none.**
   `Burmeister & Wain` broke the XML parse. Putting `&amp;` in the data makes
   `width()` measure five characters where the reader sees one — item 76's trap.
   Escaping only at emission is not enough either, because **`mapspine.check`
   reads the emitted markup and therefore measures the entity too**, and it
   reported a seven-unit collision that does not exist on the page. That is item
   64's "two rulers for one rule" in miniature. **Resolution: keep entities out
   of drawn text** — the label reads "Burmeister and Wain" — and an `esc()`
   helper stays in the script as the guard for any string that acquires one
   later.

   **The figure PLAN_I §13 asked for was not built and the decision was taken at
   the start.** No monthly sabotage series is reachable; the compiled aggregate
   (Hansen, Kjeldbæk and Maurer, 1984) surfaces only as two totals. The annual
   series is built instead and is the better figure, because it carries 1945 as
   **four months** — read as a year it understates the last winter threefold.
   Item 119's rule earned its keep on it: the industrial column adds to its
   published total of 2,801 exactly, and **the railway column adds to 1,527
   against a published 1,526**. The discrepancy of one is asserted in the script
   and drawn on the figure rather than smoothed.

127. **`mkbody.py` has been printing false glossary headings since Part H, and
   thirteen of them shipped.** Found while checking chapter 42's own build output
   by eye, not by any guard.

   `terms_by_section` accepts a ranged header — `**§05-07 - the islands**` glosses
   three sections — and its regex allowed **whitespace around the range
   separator**. So a descriptive header of the form `**§01 — 1939**` parsed as
   "sections 01 to 1939", and `**§03 — 9 April**` as "sections 03 to 09". The
   heading printed on the page was built from that span.

   **Eleven impossible headings were live on the site:** *Danish terms in sections
   01–1939* and *08–1941* and *11–1943* in chapter 41, *01–1929*, *09–1935* and
   *11–1939* in chapter 40, *06–1924* in 39, *09–1899* in 35, *10–1901* in 36,
   and chapter 38's *07–14* in an eleven-section chapter. **And two more were
   live that look perfectly legal and are not:** chapter 38's *sections 06–10* and
   chapter 41's *sections 03–09* are each a single section's glossary block. Those
   two are the dangerous ones — a reader cannot tell, and neither could I until I
   compared every heading against its chapter's section count.

   **Why nothing caught it.** The markup is valid, so `validate` passed. The
   heading fits, so nothing overran. `debuild.py` round-trips the page against
   itself, so `identical` proved only that the false heading survived a round
   trip. And `span` is used for **nothing except this heading** — placement keys
   off the leading number alone — so every glossary block sat against the right
   section and only the label lied. Item 110's class exactly: valid output, wrong
   content, invisible to every guard the project owns. It is also item 117's: a
   heading is a claim, and thirteen of them were false.

   **Fixed at source.** The range separator must now be *adjacent*, which is how
   the docstring's own example writes it and which no descriptive header uses; and
   an implausible range — running backwards, or past thirty — now fails an
   assertion instead of silently producing a span of nineteen hundred entries.

   **Rebuilt: chapters 35, 36, 38, 39, 40 and 41.** The diff is **twelve heading
   strings and nothing else** — `git diff` on the six bodies shows zero
   non-heading changes — and every page word count is unchanged, because "Danish
   terms in sections 01–1939" and "Danish terms in this section" are both five
   words. `debuild` still reads 11 style-only and 31 identical; `figcheck`
   81/41/0; `draftnotes` still 33 and still only on 25–32.

   **Chapters 25 to 32 are not affected** and did not need rebuilding, which is
   fortunate, because item 102's guard refuses them. Their only ranged headers are
   tight-written and correct.

   **The rule this earns:** a label computed from parsed input is a claim and
   needs the same treatment as a section title. The cheap check is the one that
   found it — compare every generated heading against the thing it claims to
   describe, once, per part.

128. **CLOSED by item 136. ~~OPEN, AND THE LARGEST THING IN THE PART:~~ the Part I boundary pass.**
   Carsten's decision, taken after chapter 42 was built and measured. It is not
   "split chapter 42". **It is to draft the rest of Part I and then partition the
   whole 1943–1955 run at the seams the material actually has**, rather than at
   the seams PLAN_I drew before the research existed.

   **Why it is the right shape.** PLAN_I's section lists have been wrong in every
   chapter of Part I since 39 — 40 was missing the parliamentary arithmetic, 41
   the loss of the North Atlantic, 42 both the arming and the Freedom Council's
   weight, and 42 found a third hole at drafting (the police, item 124). The
   chapter boundaries were drawn by the same hand, at the same time, on the same
   information, and there is no reason to trust them further than the section
   lists have earned. Splitting 42 on its own would fix the line between "the
   underground and the liberation" and "the reckoning" **before anyone has seen
   what is on the far side of it** — and those two bodies of material are
   adjacent, not separate. The Freedom Council, the counter-terror and the
   liberation sit directly against the *retsopgør*, Bornholm under the Soviets and
   the choice of a side. While it is all one pool, material moves freely; once it
   is two chapters with two apparatus sets, it does not.

   **What the pass must do, in order.**
   1. Draft the remaining material to the end of the part, against chapter 42's
      *content* rather than its numbering — the content is the same whatever the
      partition, so nothing here is blocked.
   2. Then partition the run 1943–1955 on the material's own seams, deciding
      Part I's chapter count once, with every chapter drafted and on the page.
   3. Then renumber once, fix every cross-reference once, rebuild once.

   **It must happen BEFORE the book-wide consistency review, not inside it.** A
   renumber during a consistency review invalidates the review.

   **What it will cost, costed rather than guessed.** Renumbering above 42 touches
   **twelve forward arrows and seven prose cross-references across shipped
   chapters 37–41** — all in drafts whose pages rebuild through `mkbody.py` —
   plus `TOTAL_PLANNED` and the part ranges in `bookstats.py`, the spine and the
   blurbs in `index_generator.py`, and PLAN_I §§10–12. Chapters 25–32 cannot be
   rebuilt while item 102's guard stands, so **nothing above 32 may be made to
   depend on rebuilding anything below 33.**

   **This is a large mechanical edit, which is where this project's failures
   cluster** — item 101 damaged a draft twice by pattern-matching without
   reading, item 112 carried a wrong total through four sessions, and a scripted
   edit deleted 408 lines of `mkbody.py` while a grep and a closing-brace check
   both passed. The pass wants a fresh clone, an assertion on every replacement,
   a whitespace-normalised confirmation, and the whole diff read by eye before
   anything is pushed.

   **What the partition will owe, whatever it decides.** Recorded now so it is
   specified rather than rediscovered:

   - **D-9.** Every chapter carries at least one `[f]` and one `[n]`. The 1943–45
     material currently holds exactly three vignettes — Duckwitz `[-]`, Ellen
     Wilhelmine Nielsen `[f]` and Kim Malthe-Bruun `[n]` — so **any partition of
     it into two chapters needs three more subjects**: an `[n]` for the
     rupture-and-rescue half, and an `[f]` and a `[-]` for the other. **Kaj Munk
     is the `[-]` and needs no research** — he is already in chapter 42 §08's
     prose, taken from Vedersø on 4 January 1944 and found at Hørbylunde the next
     morning, and he is the one elite subject in the part whose death is the
     chapter's hinge. The other two are open. Note that PLAN_I §4's 43`[n]`, the
     unnamed subject at Rønne on 7–8 May, is already moot under item 123.
   - **Figures, three a chapter.** The 1943–45 material currently holds three:
     October 1943, sabotage by year, and the People's Strike. **A partition into
     two chapters needs three more.** Candidates identified and not yet built:
     **August 1943 as a day axis** (Odense 30 July, Esbjerg 10–11, Odense 18–23,
     Aalborg 23–29, the ultimatum on the 28th, the 29th), which the day-axis code
     in `figs_42.py` already supports; **the fleet on 29 August** (52 vessels: 32
     scuttled, 13 to Sweden, 14 taken — and the arithmetic wants checking, because
     those three do not sum to 52); and **Bornholm** (Rønne 3,200 properties with
     212 destroyed and 2,900 damaged, Nexø 959 with 175 and 856 — against ten
     dead, nine of them on the first day and none on the second, which is the
     evacuation made visible).

   **A TRAP THIS LEAVES ARMED, and it caught me the same session.**
   `build_part_i.py` **exits 1 while any chapter is outside the band**, and
   chapter 42 is and will stay outside it until this pass runs. So the standard
   chain `python3 build_part_i.py && python3 linkindex.py` **short-circuits, and
   `linkindex.py` never runs** — leaving every page in the part rebuilt without
   its index links, six words short each. Six pages, thirty-six words, and
   `bookstats.py` reads 311,315 instead of 311,351, which looks exactly like a
   real change to the prose. It is not. **Run `linkindex.py` unconditionally, on
   its own line, and check `git status` afterwards**, until the band is clear
   again.

   **Until the pass runs, chapter 42 is live at 11,608 page words and 55
   minutes** — fifteen over decision 2.1's advisory and fourteen over the
   longest other chapter in the book. That is a real defect on a real page and it
   is being carried deliberately, not overlooked. **It is not to go quiet.**
   Carrying a known defect silently is how the 89-word error of item 112 survived
   four sessions.

129. **The `fill=` figures are fixed, and the thing item 110 assumed about them
   was wrong in the direction that mattered.** Item 110 said the four worst
   figures "each ask for `#F0F2EE` on `.mapl`: near-white text that is almost
   certainly sitting on a dark shape and is now rendering `#3C3E36` dark on
   dark. Those should be looked at first." They were. The diagnosis was right and
   the implied remedy was not.

   **First, the population is bigger than recorded.** **Thirty-five** figures
   carry `fill=` on classed text, not thirty-three, across **334 text elements**.
   And there are **five** near-white figures, not four: item 110's list misses
   **`svg_fealty`**, in chapter 19, where the two labels in the centre box name
   the figure's subject.

   **Second, only twenty of the 334 are legibility failures**, and the triage is
   clean: a requested colour with luminance above 0.5 was meant for a dark ground
   and is a failure; everything below it is a dark colour rendering as a slightly
   different dark on a light ground, which is a tint shift and not a readability
   problem. Every one of the twenty is a `#F0F2EE` request. **That bounds item
   110's session to five figures, not thirty-five.**

   **Third, the colour repair is separable from CHAR_W and item 110 bundled two
   independent things.** Colour does not affect text wrapping; `CHAR_W` does.
   Nothing about correcting a fill requires re-wrapping a line.

   **Fourth, the stated blocker is weaker than believed.** Four of the five
   generators reproduce their shipped figure **byte-identically** today. The
   fifth, `fig_crowns.py`, differs in **two coordinates that print `-0.0` where
   the shipped file has `0.0`** — signed zero, geometrically identical. `cmp -l`
   called that **75,047 differing bytes**, because a two-byte length shift early
   in a 173 KB file cascades through every offset after it. **A byte count is not
   a change count**, and the two-minute check that settles it is to compare
   element counts, text content and path tokens rather than bytes.

   **Fifth, and this is the finding: honouring the requested colour would have
   fixed eleven labels and made nine worse.** Figure grounds are drawn at
   opacity — `.75`, `.8`, `.9`, `.92` — so the colour a label actually sits on is
   the fill **composited over what is under it**. A slate rect at `.75` over
   paper is `#778890`, not `#4F6470`, and near-white on that is **3.27:1**, under
   the floor. The original colours were chosen by eye against the raw constant
   and nothing in the project had ever computed the composite. Measured:

   ```
   ground (composited)     near-white   #221E18   chosen
   crowns    #3B7467          4.80         3.06    near-white  (was 2.01)
   fealty    #3E766A          4.66         3.16    near-white  (was 2.07)
   andel 1-3 #778890          3.27         4.51    #221E18
   andel 4   #B0966D          2.51         5.86    #221E18
   slate hdr #6F8089          3.64         4.05    #221E18  <- best available
   brown hdr #9E927B          2.72         5.41    #221E18
   tan hdr   #B7A07C          2.24         6.58    #221E18
   ```

   **`.mapl` is 10.5px at weight 600, which is NOT WCAG large text** (that needs
   18.66px bold), so the threshold throughout is **4.5:1** and not 3:1.

   **Fixed, and the choice is computed rather than typed.** `mapspine` gains
   `luminance`, `contrast`, `composite` and `text_on(fill, opacity, under)`, which
   returns the better of paper and the palette's darkest ink against the
   composited ground, with its ratio. `figs_35.py`, `figs_36.py`, `fig_crowns.py`
   and `figs_18.py` now call it and assert on the result. **D-11 gains a
   companion: D-11 fixes the mechanism, `text_on` picks the colour, and neither
   is sufficient alone.**

   **Rebuilt: chapters 16, 19, 35 and 36.** The diff is **twenty label colours
   and two signed zeros** and nothing else. Book total unchanged at 311,351;
   debuild 11 style-only and 31 identical; figcheck 81/41/0; vignettes 81;
   draftnotes still 33 on 25–32.

   **Residue, recorded not hidden.** The two slate headers — `THE FOLKETING` and
   `FOLKETINGET` — reach **4.05:1**, the best any ink in the palette can do on
   `#6F8089`. Closing that last gap needs either pure black, which is outside the
   book's ink palette, or drawing the header rect at full opacity, which changes
   its visual weight. **Both are design calls and neither is a defect fix**, so
   they are left for Carsten. Everything else is at or above 4.5:1.

   **Also still open, and cheap:** `fig_crowns.py` reports `'1' over
   'Lindholmen'`, a seven-unit collision, on every run. It is pre-existing, it is
   not a colour fault, and it wants item 76's treatment — place the label by
   search against the other boxes, not by adjusting an offset by eye.

   **The remaining thirty figures** still carry `fill=` on classed text and are
   still cosmetically wrong in the way D-11 describes. None of them is a
   legibility failure, so they can wait for the CHAR_W session — which is now the
   only thing that session has to do.

130. **Item 103's Munch error is fixed, and sweeping the rest of chapter 37 under
   D-8 found a second one.**

   - **Munch held the foreign ministry for eleven years, not twenty.** 30 April
     1929 to 8 July 1940 is 11 years and 4,087 days, computed. The other reading
     anyone might have meant does not rescue it either: defence ministry June
     1913 to March 1920 is six years, so his whole ministerial service is
     seventeen. Corrected in `c37_draft.md`; chapter 37 rebuilt.
   - **NEW: the *mellemskole* was four years, not three.** Chapter 37's §01
     glossary said "three years between the primary school and the gymnasium".
     The *Lov om højere Almenskoler* of 24 April 1903 created a **fireårig**
     middle school, entered by examination normally after the fifth class of the
     folkeskole, with the *mellemskoleeksamen* after 4. mellem giving access to
     the gymnasium or to the **one-year** realklasse (lex.dk, *mellemskole*).
     Corrected.

   Both changes are one word each, so chapter 37's page and narrative counts are
   unchanged at 7,902 and 4,207 and the profile stays 3L/4M/3H.

   **The sweep, and why it is not finished.** D-8 says treat every "N years" as a
   claim. There are **350 such claims in years, decades or centuries across 29
   drafts**, so auditing the book is a session of its own and not a line item.
   Chapter 37's own **29** were checked because the chapter was being rebuilt
   anyway. Most compute exactly and several are better than they look: the seven
   F's "lasted sixty-six years" is 1849 to 1915 exactly; Alberti resigned "seven
   years to the day" after his appointment, 24 July 1901 to 24 July 1908; "the
   system of 1901 was seven years old"; "nineteen years in which almost nothing
   had passed" is Estrup, June 1875 to August 1894.

   **Three in chapter 37 are roundings rather than errors, and they are Carsten's
   call because changing them changes the cadence of his prose, not its truth.**
   Recorded with the computed figure so the decision is not taken twice:

   - *"Viggo Hørup, dead in 1902 after **thirty years** of asking what a Danish
     army was for."* He joined *Morgenbladet* in **October 1873** and died
     **15 February 1902** — **28 years**. And the specific question, *Hvad skal
     det nytte?*, is his Rigsdag speech of **29 March 1883**, which is **19**.
     Thirty is defensible only for "in politics", not for "asking that".
   - *"Denmark held **three islands** for **two hundred and fifty years**."*
     St Thomas from 1672 is **245** years to 1917; St John from 1718 is **199**;
     St Croix from 1733 is **184**. Denmark held *three* islands for **184**
     years. The 250 works only for the enterprise as a whole, rounded up from 245.
   - *"The regulation was meant to be temporary. It **ran for thirty years**."*
     The Labour Act is 1849 and Contract Day 1878 — **29 years**. The same
     paragraph's "the rising began thirty years later" is right, because that one
     counts from emancipation in 1848.

   **The rule this earns, and it is cheap:** when a chapter is being rebuilt for
   any reason, sweep its own duration claims. Twenty-nine of them took a few
   minutes and turned up an error that had been shipped since Part I opened, in a
   glossary block nobody would have re-read. The book-wide audit of all 350 is a
   separate task and is **not** urgent — chapter 37 was the one with a known fault
   pointing at it.

131. **`svg_titles.txt` was clipped on the shipped page and is fixed. One figure
   in the book had the fault — and the way I nearly got it wrong twice is the
   more useful half of this entry.**

   **The fault.** Chapter 16's figure 2 ended with an unfolded footnote at
   `class="mapt"`, 149 characters from x=26 on a 900-unit canvas. It ran past the
   viewBox and the last three characters were cut: the page read *"...had been
   given the word befo"*. What was lost is the point of the sentence — the
   footnote exists to say that no woman in Scandinavia had been given the word
   *before*.

   **The fix.** `fig_titles.py` now folds the note, at the larger of the table and
   measured widths, and **derives the canvas height from the number of folded
   lines** instead of the constant 46 that assumed one. Both are asserted: every
   line fits the available width, and the last baseline plus descender sits inside
   `H`. The canvas grew 584 to 597; chapter 16 rebuilt; page words unchanged,
   because folding a line does not change its words.

   **A sweep of every figure at measured widths now returns zero.** It returned
   exactly one before, which is this one, so item 105's prediction was right and
   its scope was right.

   **Now the part worth keeping. I reached the right conclusion twice by wrong
   routes, and each is a trap that will catch the next person.**

   **First: a bare `svg2png` of a `.txt` figure is not what the page renders.**
   `mapspine.rasterise()` injects the `.mapt/.mapl/.mapx` stylesheet before
   rendering, because the figures carry no styles of their own — they inherit them
   from `style.css` on the page. I cropped the footnote with a plain
   `cairosvg.svg2png` call, got no stylesheet, and cairosvg fell back to a ~16px
   default. The line then appeared to lose **45** characters instead of three, and
   the crop showed it cut mid-word at *"No woman i"*. **Right conclusion, wrong
   magnitude, entirely wrong reason.** Anything that inspects a figure outside
   `rasterise()` must inject the same CSS or it is looking at a different picture.
   Measured: with the stylesheet the glyphs are 9px tall, without it 12px.

   **Second: an ink bounding box that stops short of the canvas edge is not proof
   that the text fits.** I measured the footnote's ink at 27..893 on a 900-unit
   canvas and read it as fitting with seven units to spare. That is exactly what a
   clip looks like when the final visible glyph is itself partly cut — the ink
   ends a little before the boundary because the boundary is where it was
   severed. **The only reliable check is to read the last characters and compare
   them with the string**, which is what finally settled it.

   Both failures are the same species as item 47 and item 110: a number that
   passes while the picture is wrong. The difference here is that the number was
   mine and the picture was also mine, and neither was of the thing on the page.

   **A note for item 105, which is still open.** Its measurement of `mapt` at
   6.36 units per character reproduces exactly in this container — rendering 100
   characters through `rasterise()`'s own CSS gives 6.360, and `mapl` 6.610 and
   `mapx` 5.320, all three as recorded. But the *effective* advance in this real
   149-character line works out near **5.95**, between the table's 5.68 and the
   measured 6.36. So the table under-estimates and the measured value
   over-estimates, and the true figure depends on the string. **That is an argument
   for keeping the conservative `max(table, measured)` fold** that figs_39 onward
   use and that `fig_titles.py` now uses too: wrapping early costs a short line,
   wrapping late costs a sentence its ending. Fixing `CHAR_W` properly is still
   item 105's job, and it is now the only thing left in that session.

132. **Chapter 43 is drafted, built and verified at 10,514 page words and 50
   minutes — inside the band by four words. Six things came out of it that the
   next chapter needs, and two of them are corrections to my own draft.**

   **What was built, against what PLAN_I §11 planned.** Four divergences, all
   deliberate:

   - **Eleven sections, not ten.** The police action of 19 September 1944 got a
     section of its own (item 124). It earns it: the country had no police for
     seven and a half months, and the arrests of May 1945 are unintelligible
     without that.
   - **The chapter opens in 1944, not 1945.** Title dates and the index spine
     both corrected to `1944 – 1949`.
   - **Profile 1L/5M/5H against a planned 3L/4M/3H.** The plan wanted three light
     sections and the material has one. Section 10, the defence union, is the
     only one that is genuinely a hinge rather than an argument.
   - **§06 is a fifty-year doctrine, not a first refusal.** PLAN_I called the
     1946 South Slesvig decision "the first time in the book that a Danish
     government refuses territory it could have had" and **that is wrong.** On
     17 May 1919 the Danish envoy to the peace conference asked for the third
     plebiscite zone — already in the draft treaty — to be struck out, and it
     was. 1919, 1920, 1945 and 1946 are one doctrine with a primary document at
     every node. The thread still turns over; it turns over in 1919.

   **THE FIGURES ARE NOT THE PLAN'S AND THE SUBSTITUTION IS THE POINT.** PLAN_I
   §13 listed three, two of them schematics, with its own note that the fix was
   to convert them into data figures. Built instead: the official conviction
   table; Bornholm's occupation in days computed from the dates; and South
   Slesvig's three series as multipliers. **"Which way to lean, 1945–49" was
   dropped outright** — a schematic of a decision is a diagram of an argument,
   not evidence for it.

   **Two corrections to my own draft, both found by sourcing rather than by
   re-reading.**

   - **The best objection to the retroactive law is Hal Koch's, and I had
     attributed it to a jurist called K. Anker Jensen** — that the politicians
     who urged cooperation could not afterwards make a crime of it. Koch
     published it in **November 1947** under the title *Jeg anklager Rigsdagen*.
     I could not source Anker Jensen at all. The argument was right and the name
     was invented somewhere upstream; it is now attributed and dated.
   - **The internment chain in §02 does not add up, and the draft now says so.**
     lex.dk's *Interneringerne efter befrielsen 1945* gives about 22,000
     interned, more than 15,000 released at once, about 9,000 handed to the
     police, 2,000 of those released, about 7,000 chargeable. Fifteen plus nine
     is twenty-four, against a base of twenty-two. *Gyldendal og Politikens*
     puts the number held by 13 May nearer **34,000**. No source reconciles it,
     so the chapter states the discrepancy instead of picking a number — and the
     discrepancy makes §02's own point better than a clean figure would.

   **THE DISPUTE ABOUT THE CONVICTED WOMEN LOOKS RESOLVABLE, AND THE RESOLUTION
   IS MINE AND IS FLAGGED AS MINE.** Ditlev Tamm gives 107 women convicted of
   informing; Anette Warring has written that around four hundred of the 644
   were. The official table at final instance (lex.dk, *retsopgøret i Danmark*)
   records **413 informing convictions in the whole country, 306 of them men**.
   Four hundred women cannot sit beside 413 total, and it cannot sit beside the
   same table's 347 women convicted of German military service either, because
   347 and 400 exceed 644. **The likeliest reading is that the national total
   413 has at some point been taken for the women's figure.** It is an inference
   and the Sources block says so in those words.

   **THE OFFICIAL TABLE DOES NOT ADD TO ITS OWN TOTAL EITHER, and figure 1 draws
   the residual rather than hiding it.** The named categories — 7,277 + 1,638 +
   1,139 + 413 + about 50 — come to **10,517 against 13,521**, so **3,004
   convictions, more than a fifth of the reckoning, are in categories the
   published summary does not itemise.** The women's columns leave 165
   unaccounted the same way. Both are computed, asserted and drawn as a hatched
   bar. Item 119's rule, earning its keep for the third time.

   **THE INDEX BLURB WAS WRONG IN TWO WAYS AND ITEM 117 CAUGHT BOTH.** It dated
   the chapter 1945–1949, and it said the chapter ends "150 years of
   neutrality". **No start date makes 150 work:** 1814 to 1949 is 135 years and
   1864 to 1949 is 85. Rewritten to name 1864. A blurb is a claim and D-8
   applies to it exactly as it applies to prose — which is what item 117 says,
   and this is the first time it has actually returned anything.

   **A NEW SHAPE OF FIGURE FAULT, AND IT IS THE ITEM 47 FAMILY AGAIN.** Figure 2
   drew its legend at `LEG_Y + 14` while the canvas height had been computed
   from `LEG_Y`, so the legend sat on top of the footnote's first line.
   **`mapspine.check` did not see it and could not**: both are valid text at
   different y, and the collision checker compares text runs, not the blocks the
   layout arithmetic promised would not meet. Only the raster showed it. The
   guard added is one line — `assert NOTE_TOP - LEG_Y >= 18` — and the general
   rule is: **if a y-coordinate is used to compute the canvas height, nothing may
   be drawn at that coordinate plus an offset.** Two further faults in the same
   figure family were also raster-only: four bar colours in figure 1 that
   encoded nothing while a legend swatch in one of them implied they did, and a
   logarithmic axis in figure 3 with no tick anywhere saying it was logarithmic,
   so a reader comparing bar lengths would have got every ratio wrong.

   **The apparatus was 5,140 words on first assembly and is 4,026 now, and that
   is where the whole 53-to-50-minute reduction came from.** The prose was not
   cut to make the band. Sources alone came in at 1,991 words against the book's
   ~965 norm, and the glossary at 44 terms against a norm of 24. **A chapter that
   is over band because its apparatus is over norm is not a partition problem and
   must not be sent to the boundary pass as one.** Chapter 42 at 11,684 is a
   partition problem; chapter 43 was not, and the check is to measure the
   apparatus against the norm before concluding anything about the prose.
133. **The repository passed every verifier while shipping a wrong date in
   chapter 41, both of item 130's corrections still uncorrected on chapter 37's
   page, and no chapter 43 at all. `freshcheck.py` is the guard that closes it.**

   **What was actually wrong at `caadf9e`, found by cold-running the push.**

   - **Chapter 37's page still said "three years" for the *mellemskole* and
     "twenty years" for Munch's foreign ministry.** Both were corrected in
     `c37_draft.md` at `b8d55c8`, committed, and **never built**. Item 130 is
     written as closed. It was closed in the draft and open on the page, for two
     commits.
   - **Chapter 41's page still said the Kauffmann treaty was ratified on 12 May
     1945, seven days after the liberation.** The draft says 16 May, eleven days,
     unanimously in both chambers, with the FRUS citation. Shipped page: the old,
     wrong version.
   - **Chapter 43 had a draft, a figure script and config entries, and no body,
     no page and no index entry.** `danish-history-index.html` still carried the
     old blurb with its two faults — the 1945 date and "150 years of neutrality".

   **THE POINT IS NOT THE THREE FAULTS. IT IS THAT NOTHING COULD HAVE CAUGHT
   THEM,** and I confirmed that by running the whole suite against the pushed
   tree before rebuilding anything:

   - `debuild.py verify` — **clean.** It round-trips a PAGE against its own BODY.
     Both were stale together, so the comparison agreed with itself. **This is
     item 110's trap in its purest form: a thing compared with itself always
     passes.**
   - `figcheck.py` — **81 figures match, nothing disagrees.** It compares figures
     against their SVG sources. The figures were fine. The prose was wrong.
   - `draftnotes.py`, `seamcheck.py` — clean, and correctly so; neither looks at
     this.
   - `bookstats.py` — "42 of 44", which **reads as "43 is not written yet"** when
     the truth was "43 is written and was never built". The one number that could
     have hinted at it says the opposite of what was true.

   **THE CAUSE IS STRUCTURAL AND WILL RECUR EVERY SINGLE HANDOVER.** The standing
   rule is *patch of source only, never a generated file*. The repository
   **tracks the generated files**. Those two facts are both right and together
   they guarantee that every accepted patch leaves the tree internally
   inconsistent until somebody remembers to rebuild — and until now nothing could
   tell the difference between a chapter that was never written and a chapter
   that was never built.

   **The guard: `files/freshcheck.py`.** For every chapter with a single-file
   draft and a `mkbody.HAND` entry it rebuilds the body from the draft in a
   scratch directory and compares byte-for-byte with the body on disk. Four
   states, three of them faults: **FRESH**, **STALE** (draft moved, body did
   not), **MISSING** (draft with no body), **REFUSED** (`mkbody` will not build
   this draft at all). It also reports **NO PAGE** for a fresh body with no
   `NN-*.html`. Exit 1 on any fault. **Chapters 25–31 and 1–24 are skipped and
   NAMED rather than silently passed** — item 64's rule, that a checker which
   covers less than it appears to is worse than none.

   **It should join the cold run, and it should run before every commit and every
   handover.** It is the only check in the suite that compares a build output
   with its source rather than with another build output.

   **CORRECTED SAME DAY: REFUSED must not set the exit code, and the first
   version did.** `freshcheck.py` exited 1 on a perfectly clean tree, because
   chapter 32 is REFUSED and stays REFUSED until five open research questions are
   answered. A pre-commit hook built on that would have refused *every* commit in
   the repository, `--no-verify` would have become reflex, and the guard would
   have been dead inside a day — **a standing condition nobody can act on today
   disabling the check for the faults people can act on.** Exit 1 is now STALE,
   MISSING and NO PAGE only; REFUSED prints loudly on every run. Verified both
   ways: clean tree exits 0, and sixteen bytes appended to `c43_body.html` is
   caught as STALE and exits 1.

   **A FOURTH THING IT FOUND, WHICH I WAS NOT LOOKING FOR: chapter 32 can no
   longer be rebuilt at all.** `mkbody` refuses it over the five unresolved
   drafting flags that item 102 wired the guard for — the guard did not exist
   when chapter 32's page was built, so the page on disk **cannot be reproduced
   from its own source**. That is not staleness and pressing rebuild will not fix
   it; it is reported as REFUSED for exactly that reason. Item 102's "not fixed:
   the prose" now has a harder consequence than it did when it was written:
   **until those five flags are resolved, chapter 32 is a page with no
   reproducible source.** It is the only such chapter in the book.

   **After rebuilding 37, 41, 42 and 43 the tree is clean**: freshcheck 11 fresh
   and only 32 refused; figcheck 84 match, 0 disagree; D-9 3/3 on 40–43; seams
   pass; debuild clean; **43 of 44, 321,970 page words, 25.6 h**.
134. **The scripts were never wrong about the path. The shell was, and the loud
   failure was the lucky one.**

   The working folder moved out of iCloud to `~/Documents/Danish History` on
   18 September 2026 and Part H, Part I and `linkindex.py` all died with
   `FileNotFoundError` pointing at the old location. **Nothing in the repository
   held that path.** Every script derives its own location from `__file__`. What
   held it was `DK_CHAPTERS` and `DK_OUT`, still exported in the shell, because
   the START_HERE documents set them with `export DK_CHAPTERS="$PWD/.."` — which
   is correct at the moment you run it and stale for the rest of the session.

   **The crash was the good outcome.** The same mistake with a folder that still
   exists — an old copy, a mirror, a duplicate — does not crash. It builds the
   chapters into the wrong tree and the shipped book quietly stops matching its
   source. **Known-issue 5 records that this has already happened to this project
   once**, and it took a `build_part_e.py` with chapter 16 unsplit to notice.

   **The guard: `files/dkpaths.py`,** wired into all seven `build_part_*` scripts
   plus `linkindex.py`, `bookstats.py` and `index_generator.py` — 18 call sites.
   `DK_SRC`, `DK_OUT` and `DK_CHAPTERS` now go through `dkpaths.resolve()`:

   - **a target that does not exist is a refusal**, naming the variable and
     printing `unset DK_OUT` rather than a traceback;
   - **a target outside this repository is a loud warning** on stderr, not a
     silent success. It is not forbidden — `index_generator.py`'s own default is
     a container path and building elsewhere is sometimes deliberate — but it can
     no longer happen by accident.

   Both paths were tested against the real stale value that caused the crash and
   against an existing-but-foreign directory, and **a clean rebuild afterwards was
   byte-identical: no built page changed.**

   **The START_HERE documents are the root cause and should stop teaching the
   pattern.** `export DK_CHAPTERS="$PWD/.."` bakes a moment into a shell. Prefer
   running the scripts from the repository with the variables unset — every one
   of them defaults correctly to its own location — and reach for the variables
   only when deliberately building somewhere else.
135. **Chapter 44 is built and the book is complete at 44 of 44, 330,473 page
   words, 26.2 hours. PLAN_I §12's load-bearing claim did not survive
   verification, which is what the plan asked for.**

   **THE CLAIM THE PLAN MOST WANTED TESTED IS NOT ESTABLISHED.** PLAN_I §12 said
   the succession clause supplied just enough turnout to clear the 45 per cent
   threshold, and that if it held, "the constitution that abolished the upper
   house and legalised parliamentarism got over the line because voters wanted
   Margrethe to be queen." It also said: *verify properly, and if it does not
   hold, §03 says so and the chapter is better for it.* It does not hold.

   - **The succession was not a separate ballot.** It was one clause inside the
     constitutional package. The second ballot that day was on the **voting
     age**, 23 against 21.
   - ***Gyldendal og Politikens Danmarkshistorie* addresses the story directly
     and declines it**: it is difficult to confirm or deny the speculation, and
     the article points instead at the opposition campaigns — Knud Kristensen's
     and the communists' — as what brought people out at all.
   - The regional pattern does not rescue it. Yes took **52.6 per cent of the
     electorate on the islands** against 43.6 in Copenhagen and 41.8 in Jutland,
     and nobody has shown the islands were the more monarchist.

   The chapter states it as a claim that may well be true and has never been
   demonstrated. **It is repeated everywhere as though it had been**, which is
   the myth-check entry.

   **WHAT REPLACED IT IS BETTER, AND IT RECONCILES.** The full 1953 returns —
   electorate 2,585,800, yes 1,183,292, no 319,135, invalid 25,231, cast
   1,527,658 — **add up exactly**, which is why they are used. Yes is 45.76 per
   cent of the electorate against a floor of 45, so the constitution of Denmark
   **passed by 19,682 votes, computed**, which reproduces the "about 20,000" the
   Danish sources assert without showing their working. Set against 1939, where
   **91.85 per cent of those voting said yes and the revision failed**, the whole
   logic of §93 falls out: **a threshold counted against the electorate measures
   attendance, not agreement, and counts every abstention as a no.** That is the
   chapter's spine and figure 2.

   **ITEM 108'S OPEN QUESTION IS ANSWERED: 1961.** It asked when the poor-relief
   disqualification actually ended and left the trail to this chapter. lex.dk's
   *Danmark - social sikring*: "indskrænkningerne blev dog først totalt afskaffet
   med Lov om offentlig forsorg i 1961." So the chain is 1915 §30(b) → 1933
   redefines → **1953 delegates** (§29's sentence is in the constitution today,
   unused) → **1961 abolishes**. The third of the seven F's got the vote back
   **forty-six years after two of them did and eight years after the constitution
   stopped naming them**, and debt 3 closes on a social statute rather than a
   constitution, which is a better ending than the plan expected.

   **THE THREE VIGNETTE SUBJECTS ARE NAMED AND NONE NEEDED ARCHIVE ACCESS.**
   PLAN_I flagged 44[f] and 44[-] as unnamed and 2.9 warned that the ending
   "may need physical access". It did not.

   - **44[-] Max Sørensen.** Not merely "the commission's adviser on §20" — he
     **put the provision to the commission himself**, in a written response, aged
     thirty-nine. In 1973, the year Denmark walked through §20 into the European
     Communities, he became **Denmark's first judge at its Court of Justice.**
   - **44[n] Helene Thiesen**, as planned.
   - **44[f] Helga Pedersen**, and this is a **DEPARTURE FROM DECISION 2.9**,
     taken with Carsten's agreement. 2.9 wanted an unnamed woman voting at a
     polling station. Rather than invent an anonymous subject, the ending is
     Denmark's first woman justice minister, who argued inside the commission for
     **unconditional** female succession and was beaten to the conditional
     version, and who became the **first woman judge of the European Court of
     Human Rights** in 1971. 2.9's real requirement — a person, not a
     signature — is met.
   - **A connection worth having, and it is an inference.** Helga Pedersen held
     the Danish seat at Strasbourg until her death in January 1980; Max Sørensen
     held it from 1980 until his own in October 1981. **That the seat passed from
     one to the other is deduced from two date ranges that meet** and is not
     stated in either source. Flagged as such in the chapter's Sources.

   **THE THIRD FIGURE WAS DROPPED, FOR CHAPTER 43'S REASON.** PLAN_I §13's "What
   §20 installed, and what walked through it in 1973" was a schematic, and a
   schematic of a decision is a diagram of an argument rather than evidence for
   it. Replaced by **the two ballots of 28 May 1953** — two questions, one day,
   and **two different registers**, the voting-age one 229,300 larger because it
   was open to the people the question was about. They turned out and lost.
   **That table does not reconcile: its components overshoot its published total
   by exactly 200**, where the constitutional ballot's reconcile exactly. Marked
   on the figure, not averaged away.

   **TWO FIGURE FAULTS THAT ONLY THE RASTER SHOWED, both the item 47 family.**
   Figure 2 drew 1953's third block as *cast minus yes minus no* — the 25,231
   spoiled ballots — while 1939's used *electorate minus yes minus no*. **Two
   denominators in one figure**: the 1953 bar stopped three quarters of the way
   across and the picture understated the very quantity it exists to show. Fixed,
   with an assertion that each row's blocks sum to its electorate. And figure 1's
   second marker fell at 99.9 per cent of the span, indistinguishable from the
   bar's own right edge, so it marked nothing while its label sat far away
   pointing at blank paper; **a tick that cannot be told from the end of the bar
   is not a tick**, and it was replaced by an end label.

   **An assertion also caught the prose.** The Landsting's span was written as
   104 years and asserted as such; measured to its **last sitting** on 15 May 1953
   it is 103.94. Both facts are true and they are not the same fact: the chamber
   ran **constitution to constitution, 5 June 1849 to 5 June 1953 — exactly
   104 years** — and stopped sitting three weeks early. The figure now says so.

   **The apparatus stayed at house norms this time**, which item 132 asked for:
   Sources 904 words against the ~965 norm, where chapter 43's first assembly
   came in at 1,991 and had to be cut twice. **Chapter 44 needed no length
   surgery at all** — 8,503 page words, 40 minutes, first build.
136. **The Part I boundary pass is done. Item 128 is closed. The book is 45
   chapters and every one of them is inside the band.**

   Carsten chose four chapters over three, on measured grounds: the run 42–44 was
   32 sections and 15,697 narrative words, and **no three-way cut works**, because
   each apparatus set costs a measured ~5,000 page words and three chapters means
   ~5,230 narrative each — at least one chapter at 65 minutes whatever the seams.
   Four lands them all at 36 to 45.

   ```
   42  1943: the year the policy broke        6 sec   7,508 page (36 min)
   43  The underground and the liberation     6 sec   7,659 page (36 min)
   44  The reckoning, and the accounts        8 sec   9,044 page (43 min)
   45  Choosing a side, and the constitution 13 sec   9,354 page (45 min)
   ```

   **Book: 45 of 45, 333,337 page words, 26.5 h. No chapter in parts D to I is
   outside the 25–50 band.** Chapter 42's 56 minutes, which has been the open
   complaint since it was built, is gone.

   **THE SEAMS ARE THE MATERIAL'S.** 1943 ends where the occupation stops being a
   policy and becomes an organisation — the Freedom Council constituting itself.
   The second chapter runs from the arming to the liberation and **takes the
   police deportation of 19 September 1944 back from the reckoning**, where it had
   been put only because the May 1945 arrests need it; chronologically it belongs
   with the occupation's last year. The third ends with the accounts rather than
   the choice. The fourth is the choice and its constitution.

   **THE PARTITION BROKE D-9 IN THREE CHAPTERS OF FOUR, AND THAT WAS NOT IN THE
   COSTING I GAVE.** Nine vignettes do not divide into four chapters that each
   need `[f]`, `[n]` and `[-]`. One fix was free: **Fanny Jensen moved from "4
   April 1949" to "Marshall aid"**, which is where her November 1947 appointment
   and her household-supply portfolio belonged anyway. The other three had to be
   researched and written from nothing:

   - **42[n] Paul Aron Sandfort** — born Paul Efim Rabinowitsch in Hamburg in
     1930, brought to Copenhagen in 1936 to get him away from Germany, trumpet in
     the Tivoli Boys' Guard; caught fleeing to Sweden, Horserød on 4 October 1943,
     Theresienstadt on the 13th at thirteen, into the ghetto orchestra and more
     than fifty performances of *Brundibár*; out on the Red Cross buses on 15
     April 1945. **He escaped Germany as a small boy and Denmark sent him back
     into it at thirteen.**
   - **43[f] Monica Wichfeld** — born Massy-Beresford in London in 1894, married
     to a Lolland landowner, running the underground's weapons work on
     Lolland-Falster from early 1943. Taken at Engestofte in January 1944,
     condemned in May, **refused to petition for mercy** and gave way only for her
     family, writing it in English on lavatory paper. Died at Waldheim on 27
     February 1945; her grave has never been found.
   - **43[-] Kristian L. Rasmussen** — an Odense policeman taken on 19 September
     1944, Frøslev to Neuengamme to Buchenwald, who kept a forbidden diary of
     weather, rations and the dead, and one entry recording **fourteen hundred
     Jews arriving from Auschwitz, a hundred already dead**. Neither resistance
     nor collaborator, in a camp for the uniform a Danish state had told him it
     was responsible to wear.

   **Sandfort and Rasmussen speak across the new seam** — one goes into
   Theresienstadt, the other watches Auschwitz arrive — which is what a partition
   at the material's own joints produces rather than something arranged.

   **Two new *Meanwhile* entries were needed and both earn their place.** Rome,
   16 October 1943: the community raised fifty kilograms of gold and delivered it
   **at midday on 28 September — the same day Duckwitz warned Hedtoft** — and was
   taken anyway; 1,259 seized, sixteen came back, against Denmark's 7,400 across
   the water. *That the two events fall on one day is arithmetic on two separately
   sourced dates and is flagged in Sources as such.* And Norway's Milorg: forty
   thousand trained and supplied by 8 May 1945, held back for the same reason and
   used at the liberation to keep order — the direct Scandinavian control for the
   waiting groups.

   **FIFTEEN FORWARD ARROWS AND SIX PROSE REFERENCES WERE RE-TARGETED
   INDIVIDUALLY, AND THE NUMBER WAS NEVER THE ANSWER.** A `→ 42` in chapter 41
   pointing at "who listened, and how they were armed" now goes to **43**, because
   the arming moved; a `→ 43` about Fanny Jensen goes to **44**, because she did;
   a `→ 43` about Iceland and the Faroes goes to **44**. Item 101's rule held:
   every one was read before it was changed, and a blanket increment would have
   been wrong on at least four of them.

   **The assertions did their job four times.** A title replacement was lost
   because a *later* assertion in the same script failed before the write — which
   is the behaviour wanted, not a bug. Three edits failed to match because the
   phrase spanned a line break, and were re-matched against the real text rather
   than forced. The confirmation pass is whitespace-normalised, per item 69.

   **What did not change:** the prose. 33 sections in, 33 out, none duplicated or
   dropped, asserted on assembly. The only prose written for this pass is the
   three vignettes, two *Meanwhile* entries, four carry-forward sets, four
   summaries and the questions — apparatus, not argument.
---

137. **`dkpaths.py` checked the variable and not the default, so the one script
   whose default was still a container path went on failing after the move. The
   docstring named that default as an example and walked past it.**

   The boundary pass would not commit. The pre-commit hook was right to refuse
   and was refusing the true state of the tree: `freshcheck.py` reported **NO
   PAGE for chapters 42, 43, 44 and 45** — four fresh bodies with no page built
   from them. The cause was three steps back. `index_generator.py` had died with
   a bare `FileNotFoundError` on
   `/mnt/user-data/outputs/danish-history-index.html`, and the chain that was
   supposed to run after it never did.

   **THE BUG IS IN THE FIX FOR ITEM 134.** `dkpaths.resolve()` validated
   `DK_CHAPTERS` / `DK_OUT` / `DK_SRC` when they were set and **returned an unset
   default unlooked at**:

   ```python
   raw = os.environ.get(var)
   if not raw:
       return default          # <- never checked
   ```

   Every call site but one defaults to something derived from `__file__`, so this
   was invisible. `index_generator.py` line 16 defaulted to
   `/mnt/user-data/outputs`, left in the source from the era when this book was
   built in a container. After the move out of iCloud the correct thing to do was
   **unset the variables** — item 134's own advice — and doing the correct thing
   is what re-armed the fault: with `DK_CHAPTERS` unset the script aimed at a
   folder that does not exist on the author's machine, found no chapters, built a
   full index anyway, and died seven hundred lines later at the write.

   **THE DOCSTRING CITED THE FAULT AS A REASON NOT TO FIX IT.** `dkpaths.py` as
   written said a path outside the repository is a warning rather than a refusal
   because "building into another folder is sometimes legitimate — *index_
   generator.py's own default is a container path*". The one line in the project
   that names the defect names it as justification. Seeing a thing and
   classifying it is not the same as checking it, and the check is cheap.

   **FOUR EDITS.**

   - `dkpaths.resolve()` now resolves variable-or-default to one path and
     `isdir`-checks both, with **two different refusals**: a set variable is the
     author's shell and says `unset`, an unset one is the script's own default
     and says the default is wrong and which script asked for it. A bare
     `FileNotFoundError` at a write is now a named refusal at import.
   - `index_generator.py` defaults to the repository, from `__file__`, like
     everything else here.
   - `linkindex.py` and `bookstats.py` defaulted to `os.getcwd()`, which is not a
     stale-path bug but the same family: run either from `files/` by mistake and
     a cwd default **finds no chapters and reports an empty book** rather than
     refusing. Both now derive the repository from `__file__`.

   **WHAT THE HOOK IS WORTH.** This is the first time `freshcheck.py` and the
   pre-commit hook have caught something in anger, and they caught exactly what
   they were written for in item 133: a tree whose pages do not follow from its
   source, passing every other verifier. `debuild verify` was clean throughout —
   it compares a page with its own body, and here there were no pages at all.
   Without the hook the boundary pass would have committed 45 chapters of source
   with 41 chapters of built book and an index still listing 44.

   **REBUILT AND RE-VERIFIED ON THE AUTHOR'S MACHINE**, not in a container: 45 of
   45, **333,337 page words, 26.5 h**, identical to the fresh-clone figures taken
   before delivery. freshcheck 13 fresh, exit 0, chapter 32 the only REFUSED.
   figcheck 87 match / 0 disagree. Seams pass. debuild clean.

   ~~**STILL OPEN, AND IT IS ITEM 134's TAIL.** The START_HERE documents still
   teach `export DK_CHAPTERS="$PWD/.."`.~~ **CLOSED in item 138** — after it fired
   a third time.


138. **Half the book's myth-check prose had never reached the pages, and nothing
   in the suite could see it. Found 18 September 2026, fixed and rebuilt by the
   morning of the 19th. Every page 01–45 now passes every check. Full detail in
   `REVIEW-BUILD-FAULTS.md`; this is the ledger's record of it.**

   Carsten reported two things: pieces missing from the HTML, and the same text
   repeated in body and vignette. Both were real.

   **2,719 WORDS OF WRITTEN MYTH-CHECK — 49% OF IT — WERE NOT ON THE PAGES.** One
   function in `mkbody.py`, `myth_html`, read claim/correction in strict pairs.
   The drafts use four conventions and it understood one:

   - **25–31** (`**The myth.**` / `**What can be shown.**` / `**What cannot.**`):
     nothing matched. Seven pages shipped the MYTH-CHECK heading over `<dl></dl>`.
   - **32–36** (one claim, several correction paragraphs): the first sentence of
     the correction shipped and 85–92% of each block was dropped.
   - **37–45** (claim and correction in one paragraph): the whole paragraph became
     the `<dt>` and the *next claim* its `<dd>` — every Part I page printed claims
     in the correction's type and corrections in the claim's, offset by half an
     entry, with six stray empty `<dd>`s. Word counts matched, so only reading the
     page shows it.

   **A second parser, `meanwhile_html`, dropped 141 words** — the unlabelled
   closing paragraph of chapters 42's and 43's Meanwhile block, which is the
   paragraph that draws the comparison the two boxes exist for. The refusal
   directly beneath that function already said "refuse rather than discard
   authored prose". It covered the count of boxes and not the paragraphs between
   them.

   **Chapters 25, 26 and 27 carried draft-file headers mid-narrative.** A chapter
   written in two sittings is two `# Chapter NN` segments in `PART_G_DRAFT.md`;
   `chapter()` joined them keeping the second segment's preamble, and `sections()`
   splits on `##`, so the concatenation marker, the repeated title, `*Draft,
   sections 04–09 of 09.*` and a placement note landed inside whichever section
   was open — chapter 25 §03, chapter 26 §05. Item 102 recorded the symptom in
   the chapter 39 session; it had never been traced to the line. **Chapter 32**
   carried four "Drafting flag:" notes on the page, including "Resolve before
   build".

   **Smaller, same family:** chapter 29's Struensee vignette title wrapped in the
   draft and shipped with literal `**`, cut at "on 17", with "January 1772**" as
   its first paragraph (`vig_html` took one line as the title); and every page
   25–45 ended its Questions and its Sources with a literal `---`, the markdown
   rule glued to the last item (fixed once, in `apparatus_part`).

   **WHY NOTHING SAW IT.** Every verifier the project owns compares a page with
   itself or with another build output. `debuild verify` reconstructs the draft
   *from the page*, so prose that never reached the page is invisible to it by
   construction. All of them passed, on all 45 chapters, throughout.

   **THE NEW GUARD: `appcheck.py`,** in the cold run beside `freshcheck.py`. For
   every apparatus block it compares the draft's words with the page's and
   refuses a shortfall. Terms are compared by entry; Checkpoints are exempt, named
   in the file, because the build scripts rewrite them as questions and a guard
   that cries wolf eight times a run gets skimmed. It reported exactly the 13 real
   losses and nothing else, and reports nothing now.

   **THE REBUILD ORDER IS THE FIX, NOT A CONVENTION.** `build_part_X.py` reads
   `cNN_body.html`, not the drafts. The first rebuild of Part I re-wrapped the
   stale bodies byte-for-byte and printed `part ok` nine times; the first rebuild
   of Part G did the same because `mkbody` was refusing and the build ran anyway.
   **`mkbody.py` for each chapter first; if any line prints `!!`, stop** — the part
   build will wrap the old body and report success.

   **THE STALE VARIABLE FIRED A THIRD TIME,** in this session: `DK_CHAPTERS`
   resolved to `~/Documents` and the build wrote the chapters beside the
   repository. `dkpaths.py` warned, as designed. The export is now removed from
   all four START_HERE documents, closing item 137's tail.

   **FACTS CHANGED IN THE PROSE — read these two:**

   - **Chapter 32 §09, the 1838 language vote.** The draft said the Schleswig
     assembly "could not settle the question, and the king settled it for them",
     and flagged a conflict between sources. There was no conflict: Nis Lorenzen's
     motion of 7 June 1836 **carried in July 1838, 21 to 18**, with the support of
     the assembly's president N. N. Falck (*Dansk Biografisk Leksikon*: "lykkedes
     det at gennemføre det med kneben majoritet (21 stemmer mod 18)";
     danmarkshistorien agrees). Danish Wikipedia reverses the sign. The rescript
     of 1840 granted what the assembly asked for.
   - **Chapter 31, the 1807 governing commission.** The draft said the machinery
     "did not have to be dismantled afterwards, because seven years later Norway
     kept it". It was dismantled: the Regjeringskommisjonen ran **24 August 1807
     to 1810** and Frederik 6. dissolved it partly because it "fremmet norske
     selvstendighetstanker" (Store norske leksikon; norgeshistorie.no). What ran
     on to 1814 was the *stattholder* office, revived in 1809.

   **Resolved from sources, no change to the argument:** Christiansborg burned 26
   February 1794 and the city 5–7 June 1795, 941 houses (ch 31); *Jammers Minde*
   was first published in 1869, ed. Sophus Birket Smith, per Det Kgl. Bibliotek
   (ch 26) — REVIEW-PART-G §0's "nearly two centuries" can be made exact again;
   the St Jan attack was 23 November 1733, as the chapter had it (ch 30); chapter
   25's placement note was spent. **Chapter 27 §07** no longer asserts a calendar
   style for the Frederiksborg date — see E4 in REQUIRES ARCHIVE ACCESS.

   **DECIDED BY CARSTEN:** `draftnotes.py` does not scan the "Where the argument
   stands" block, whose standing caveat to the reader sits where mkbody's own
   refusal tells authors to put unresolved questions. Tested both sides of the
   boundary. The accepted cost: a genuine note parked in that block will pass.

   **LESSON, AND IT IS MINE FOUR TIMES OVER.** In one session I built a bespoke
   check and skipped the tool that already existed, four times: I reported
   chapter 27's apparatus lost without opening `PART_G_DRAFT.md`, which `mkbody`
   names as its default; I ran the second build stage after reading the
   instruction that names the first; I called chapter 32's flags "one chapter"
   without running `draftnotes.py` on the pages, whose docstring describes chapter
   25's header; and I raised the Frederiksborg date without reading chapter 27's
   own Sources, which cite the Treaty of Kiel against the reading I was pressing.
   **Before building a check, run the one the project has. Before disputing a
   claim, read what the chapter already cites for it.**

   **STILL OPEN, in the order I would take them:**

   - **The consistency review**, item 128's successor, now that nothing is
     missing from the pages. Start with Part I's profile (State, above).
   - **Six vignettes repeat their own section body** — 27 §05 Tordenskjold (the
     vignette holds nothing the body does not), 27 §09 Gertrud Rask (two sentences
     identical), 29 §03 Caroline Mathilde, 26 §09 Leonora Christina (its last
     third), 35 §03 Uhd (the four dairy rules, twice), 22 §08 Tommesis (against
     the figure beside it). **The rule they break is unwritten and has held 126
     times out of 132: a vignette is the particular inside a general section. When
     the section is named for the vignette's subject or its exact moment, the
     vignette has nowhere to stand and restates the body in the present tense.**
     Write it down as a convention before the review, so the review applies it in
     one place.
   - **Chapter 45's carry-forward** renders as a heading over an empty list.
   - **Chapter 32's figure (c)**, the Zealand kapitelstakst for rye 1815–1848, was
     never drawn; the section was written expecting it.
   - **`cNN_body.html` for chapters 01–24 have no drafts in the repository,** so
     the four-convention parser is verified against their pages only. Their pages
     are correct; nothing is known to be wrong. Worth knowing before anyone
     rebuilds them from source.
   - **Chapter 28 has four overlapping body drafts** (`01-03`, `01-04`, `01-06`,
     `01-10`); which is authoritative is not recorded.


139. **The consistency review, session 1: conventions collected, four sweeps
   built and run, Part I read. The August ledger pass was never in the
   repository, and eighteen author's notes were on the Part I pages as glossary
   definitions. Full record in `REVIEW-CONSISTENCY.md`; the rules it checks
   against are in the new `CONVENTIONS.md`.** 19 September 2026.

   **Cold run on a fresh clone of `c5775cf`: every figure matched START_HERE_review.**

   **STEP 1 — `CONVENTIONS.md`.** D-1 to D-12, each with rule, reason, status and
   where defined, plus the unnumbered rules (L-lessons, the Part E settlements,
   the index's own conventions list). Three proposals: **D-13** the vignette rule
   of item 138; **D-14** regnal numbers in the Danish style for Scandinavian
   rulers (409 on the pages, counted; seven Roman forms in G and I, now fixed);
   **D-15** place names, which needs Carsten (REVIEW-CONSISTENCY §5, D-B). Found
   while collecting: **D-6's "one line in the index's conventions list" was never
   added**, and the index promises Danish terms "glossed on first use in each
   page", which Part I had stopped doing.

   **STEP 2 — four sweeps, each a script over the built pages** (`reviewlib.py`,
   `sweep_glossary.py`, `sweep_names.py`, `sweep_facts.py`, `sweep_arrows.py`,
   standard library only). Findings in `REVIEW-CONSISTENCY.md` §1–§4; the ones that
   matter:

   - **THE AUGUST LEDGER PASS IS NOT ON DISK.** *Debts — Part F closed* lists
     sixteen arrows from 20–24 "as they now stand in the shipped files … the state
     on disk, not the plan". **Eight of them were not** — the bodies and pages
     carried the pre-pass targets: Trankebar to the Great Northern War, the
     Atlantic trade to 27, Skåne's snaphaner to Struensee. Item 112's rule with the
     sign reversed: the repository was right about itself and the ledger was
     wrong. Fixed in `c20`–`c24_body.html` to exactly what the ledger records,
     each read against its target; `c18`'s Bergen arrow and "which is chapter 28"
     with them.
   - **EIGHTEEN GLOSSARY ENTRIES IN 40–45 READ "glossed in chapter N — reference,
     do not re-gloss."** as the whole definition — an instruction to the next
     drafter, on the page. Two pointed at the wrong chapter. All now carry a
     one-line definition and "(chapter N)". **`draftnotes.py` refuses the phrase**,
     and on its first run found nine more in drafts 32–40 that `mkbody` had
     silently dropped — two of them wrapped across a line break my own grep missed.
     Those in 32, 33 and 36 are now real glosses; 32's pointed at the wrong
     chapter *and* the wrong institution.
   - ***fæste* was "tenancy" in 17, 21, 28 and 29 and "copyhold" in 32** — PLAN_H
     had asked for exactly that check and it was not made. 32 now says tenancy.
     *Håndfæstning* is "hand-fastening" and "almost every" king in 14, "a
     handshake" and "every Danish king from 1320" in 25; 25 aligned.
   - **Schleswig / Slesvig drifts by drafting session** (105 against 129), with
     Flensburg/Flensborg and five smaller pairs; **"Ditmarschen"**, 14 times in 19–21,
     is neither language. Decision D-B.
   - **Dates and figures: no cross-chapter disagreement the method reaches**,
     and REVIEW-CONSISTENCY §3 says what the method cannot reach.
   - **Chapter 37 pointed `→ Part I` five times from inside Part I**; re-pointed.
     Pages 04, 06, 07 carry stale Part G numbers the pass never reached, and 05–07
     have an `<h1>` that is not their title — blocked pages, decision D-A.

   **STEP 3 — Part I read in full, 37 to 45.** Nine boundary-pass leftovers fixed
   (section numbers from the three-chapter draft, "forty-three chapters", "eight
   chapters", a Fanny Jensen set-up whose pay-off had moved to 44, and **"occupied
   in six hours" — item 117's struck claim, alive in 45**). Twenty-one corrections
   of fact or of the book against itself, of which **three change what the book
   asserts — read these**:

   - **45: the 1953 succession.** Women were barred by the **succession law of
     1853**, not "the royal law of 1665", which chapter 33 rightly says had a
     cognatic fallback. §06 rewritten on that basis; its argument survives and is
     sharper.
   - **42: the Horserød prisoners went in the same ship as the Jews**, not a
     second ship (42) or a train (41). "One ship out of Copenhagen, and only half
     of what it carried is in the story Denmark tells."
   - **42: the Theresienstadt visit** was the ICRC and two Danish officials, not "a
     Danish and Swedish Red Cross delegation".

   The rest — turnout records that contradicted each other across 38/41/45, the
   8-billion/3-billion clearing figures, 38's "constitution of 1866" in 1920,
   Kanslergade's head-count, three D-8 intervals — are listed in §6.2.

   **VERIFIED:** fresh clone, the patch applied, `figs_41.py` → `mkbody` for 25,
   31–34, 36–45 (no `!!`) → `build_part_e` to `_i` → `linkindex` →
   `index_generator`, then the whole suite: **debuild 30 identical / 15
   style-only; 45 of 45, 336,857 page words, 26.7 h; vignettes 89/61, selftest
   passes; figcheck 87/41/0; draftnotes clean on pages and drafts; appcheck 159;
   freshcheck 14; seams pass.** The one changed figure, `svg_valg_1943`, was
   rasterised and looked at.

   **`cNN_body.html` WAS EDITED FOR 18 AND 20–24, AND THAT IS DELIBERATE.** For
   16–24 the body is the only source there is (`LEDGER_PASS.md`: "authored
   bodies"); START_HERE's rule is about the bodies `mkbody` generates.

   **DECISIONS WAITING, in REVIEW-CONSISTENCY §5 and §6.3:** D-A unblock 01–15 via
   `debuild.py extract`; D-B Schleswig; D-C 45's empty carry-forward; D-D agree
   D-13; I-1 cut 43's repetitions of 44; I-2 move 43 §06; I-3 the seventh
   vignette; I-4 45's last section title; I-5 accept 44 and 45 over the advisory.

   **CHECKED BY A SEPARATE AGENT** that had not seen the work: it confirmed every
   factual claim put to it and found five slips in the fixing, all corrected
   (REVIEW-CONSISTENCY §6.2, last paragraph).

   **LESSON, and it is the same one, twice.** I changed chapter 45's "June 1849 to
   June 1953" to agree with its last sitting in May, and then found the figure
   caption beside it defining the 104 years as constitution to constitution. And I
   changed 43's "a fortnight's warning" to "three days'" without reading chapter
   42, which says a fortnight three times and counts from Duckwitz's first
   warnings on the 17th. Both reverted; the second only because the independent
   check caught it. *Before disputing a claim, read what the chapter already has
   for it — including its figures and its neighbour.*

140. **The consistency review, session 2: all nine decisions answered and
   applied. D-13 and D-15 are in force; D-16 is new — length is never a reason to
   cut. Chapters 01–15 are to be unblocked next, as their own session.** 19
   September 2026. Full table in `REVIEW-CONSISTENCY.md` §6.4.

   **Cold run on a fresh clone after item 139's rebuild: every figure matched
   START_HERE_review_2.** Each decision was then put on its own, answered, applied,
   verified from a fresh clone and pushed before the next was put. Nine commits.

   - **D-D, yes:** D-13 in force. Six of its seven vignettes wait for their
     parts (22 §08; 26 §09, 27 §05, 27 §09, 29 §03; 35 §03).
   - **I-1 to I-4, yes:** 43 no longer repeats 44 (two methodological columns
     moved to its Sources); *The policeless country* moved into chronological
     order, with its checks re-keyed; 42's Duckwitz vignette lost the paragraph
     that restated its section; 45's last section retitled *The last of the seven
     F's* and its closing line anchored to 28 May.
   - **I-5, and more: D-16.** Carsten, verbatim: *"do not trim for the sake of
     time. 1. if it makes sense for the story, keep it. 2. If restructuring /
     moving between chapters, makes sense, do it 3. if it is good as is, keep it.
     It is within limits."* The 40-minute advisory is not a reason to cut, and
     no future session should propose a cut on length alone.
   - **D-C, yes:** an empty carry-forward is left out, and the build refuses a
     chapter where the `no_forward` declaration and the body disagree.
   - **D-B, Schleswig: D-15 in force**, applied to Part I prose and figures.
     The rest of the book is fixed in each part's pass (104 bare "Slesvig" in
     eleven chapters). The spine maps still label in Danish: undecided.
   - **D-A, yes:** next session.

   **Book: 45 of 45, 336,690 page words, 26.7 h.** debuild 30 identical / 15
   style-only; figcheck 87/41/0; vignettes 89/61; draftnotes clean; appcheck 159;
   freshcheck 14; seams pass.

   **NOT DONE, carried to session 3:** 38's Sønderborg arithmetic (2,029 − 349 is
   1,680, not 1,672) and Tønder figure; 38 §04's Ribe clause; 42's Sources listing
   43's open questions. And **narrative.py marks 17 §08, *Kalmar, 17 June*, OVER
   at 849 narrative words.** That was there before this review and nothing in it
   has changed. Under D-16 it is a matter for the Part E reading, not a cut.

---


## Convention D-12: draft prose is never written through a shell heredoc

Four apparatus blocks of `c41_draft.md` were written by a Python script inside a
quoted heredoc, using `\uXXXX` escapes for the Danish characters and the arrows.
Inside a normal Python string the doubled backslash survives, and **thirty-six
literal `ø` and `→` sequences were written into the draft as text**.
`mkbody.py` built them, the tag-balance check passed, `build_part_i.py` passed,
and `debuild.py verify` round-tripped the page **identical** — because the markup
is valid and the round trip compares the page with itself. The page shipped
reading `Horserød` and `**→ 42.**` until an unrelated assertion refused
and the file was read by eye.

This is item 110's class again: valid output, wrong content, invisible to every
guard the project owns. **Write draft prose with the file-editing tools, where the
characters that go in are the characters. If a script must generate prose, it
reads its text from a UTF-8 file rather than from a heredoc.**

**The guard is wired in, not merely written.** `mkbody.build()` now refuses any
draft containing a backslash-u followed by four hex digits, names the escapes it
found, and does not strip them — the same shape as the drafting-flag refusal above
it, and for the same reason. Tested by putting one back into `c41_draft.md`,
watching the build refuse, and restoring.