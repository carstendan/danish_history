# HANDOFF

A digital history of Denmark, c. 13,000 BCE to 1953. Self-contained downloadable
HTML chapters, written in English with Danish terms kept and glossed, narrative
in the manner of Hastings and Beevor: individual people at named moments carrying
the argument.

---

## Vocabulary — settled, do not drift

- **Part** — a lettered span, A to I. Part E is chapters 16–20; Part F is 21–24.
- **Chapter** — a numbered page, 01 upward. There are 43: Part G took seven
  chapters rather than six (decision D-2, Aug 2026), so everything from the old 29
  upward shifted by one.
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
| H | 32–36 | 1814–1901 | **planned, Sept 2026 — see `PLAN_H.md`**; not drafted |
| I– | 37– | 1901– | not planned |

All of 01–24 are published to a web folder. Chapter pages carry two links back to
the index, inserted by `linkindex.py` — see Tools.

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
32), so 43 is the landing, not 43–45. `bookstats.py` still flags two chapters as
dense and its 43/44/45 projection is now wrong — take the flags out of the spine.

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
| `c16_body.html` … `c31_body.html` | see below. Sixteen retained bodies, 16–31; the `c16a`/`c16b` names are retired |

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
adds up the result and flags any chapter outside the 25–45 minute band.

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
   whole document and then failed on its last line. Anchors are `part-*` and
   `c01`–`c42`; counts are computed. **Run it with `DK_CHAPTERS` pointed at the folder
   holding the chapter files**, or the link count will be wrong.
3. **`build_part_d.py` reads `e12_body.html`–`e15_body.html`** on the old `e`
   prefix, while A–C and E use `c`. Harmless until someone tries to rebuild D and
   has the files under the other name. `build_all.py --check` reports it.
4. **`build_parts_abc.py` and `build_part_d.py` cannot currently rebuild.** Both do
   `style.replace('--part:#96591A;', ...)` against a `style.css` whose token is named
   `--band:`. The replace silently no-ops and the verify step then reports the part
   colour as BAD. `build_part_e.py` raises loudly on a missing token instead, which is
   the better behaviour; copy it into the other two. One line each.
5. **The project mirror has been stale before**, and was again in August 2026:
   `/mnt/project` held a `build_part_e.py` with chapter 16 unsplit and no coda. The
   iCloud folder is the source of truth. If the two disagree, the shipped chapters are
   the tiebreaker.
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

24. **The forward arrow to 1953 has no part letter.** Chapter 36's myth-check turns
   on parliamentarism not being written into the constitution until 1953. Under D-1
   an arrow that far out names a part letter, and the parts after I are unplanned,
   so the letter does not exist yet. Assign when they are planned.

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
   Kongedybet*, *Nørregade* — the true figure is **thirteen of forty-eight**.
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

39. **Figure output is not byte-identical across machines.** `map_1814.py`
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
   mapx 5.63, mapl 6.98 units per character.** The 6.1 the guard uses is
   conservative for the two small classes and **too small for `mapl`**, so a long
   heading can overrun without being flagged. That is a live under-detection, and
   it belongs with open item 10.


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
three faults: text overflowing a container in chapter 26 (Lesson L?, recorded in
`STATE_G.md` §4), and twice in `figs_29.py`'s column figure, where a 36-character
label was written into a 23-character label column and the guard passed it clean.

A naive check flags every full-width subtitle that legitimately spans both columns.
Doing it properly needs the figure scripts to declare their column geometry, which
none of them currently do. **Infrastructure task, not a quick fix.**

---

## REQUIRES PHYSICAL / ARCHIVE ACCESS — cannot be done from this end

*Three blocking apparatus gaps in Part G need a person at a screen reading gothic
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
