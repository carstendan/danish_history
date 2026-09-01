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
| G | 25–31 | 1660–1814 | planned and drafted complete; not yet built |
| H– | 32– | 1814– | not planned |

All of 01–24 are published to a web folder. Chapter pages carry two links back to
the index, inserted by `linkindex.py` — see Tools.

Part E as built:

```
16  Margrete I and the making of the union      ~7,800 words (~37 min)
17  The union at work, and the end of Margrete  ~6,300 words (~30 min)
18  Sound Dues, the Hanse, a straining union     7,387 words (~35 min)
19  Schleswig-Holstein and the union's collapse  7,663 words (~36 min)
20  Reformation and the Count's Feud             7,318 words (~35 min)
```

All five: 3 checkpoints · 3 vignettes · 2 meanwhile boxes · 10–12 glossary blocks;
3 figures except 17, which carries 2. Braces balanced, no placeholders left, every
internal anchor resolves, tags balanced including inside the SVGs, TAIL in both
rail and TOC, part colour `#2E6B5E`, no unicode escapes leaked. Chapter 20
additionally carries the part coda, via `tail_extra`.

Part F as built:

```
21  The Lutheran realm of the nobility            10,218 words (~49 min)
22  Christian 4.: ambition and the building years  7,104 words (~34 min)
23  Christian 4.: the wars that broke him          6,957 words (~33 min)
24  Losing the eastern provinces                   7,014 words (~33 min)
```

All four: 3 checkpoints · 3 vignettes · 2 meanwhile boxes · 3 figures · 9–10
glossary blocks. Part F colour `#8A2B2B`, the `--oxblood` token already in
`style.css`; parts D and E are both teal and F had to move away from them.
Chapter 24 carries the part coda, via `tail_extra`.

**Chapter 21 stays at 49 minutes.** It was drafted long and the Part F review
reversed the obvious diagnosis: sections 02 and 03 look heavy only because each
carries a vignette, and §02 has the second-*lightest* narrative in the chapter.
Trimming there would have cut Palladius in the parish. The real fault is that no
section is genuinely light — a rewrite, not a trim — and it is not worth doing to
save four minutes inside the band.

Size of the whole, measured rather than guessed (`bookstats.py`): nine built
chapters of E and F average about 7,500 words and 36 minutes, which projects to
roughly **300,000 words and 25 hours** at 42 chapters. Five chapters are still
flagged dense, so 43–45 is the realistic landing.

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
| `c16a_body.html`, `c16b_body.html`, `c17_body.html`, `c18_body.html`, `c19_body.html` | see below |

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
- `c16_body.html` — superseded by `c16a_body.html` and `c16b_body.html`.
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

   > **page words ≈ Σ(section narrative bands) + 2,800**

   with narrative bands of light 200–280, medium 400–500, heavy 600–700. A
   nine-section chapter at 2 light / 4 medium / 3 heavy lands near 7,000 page words
   and 33 minutes; a ten-section chapter at 2 / 4 / 4 near 7,700 and 37.

1a. **Reading time: hard band 25–50, soft target 30–42.** `build_all.py` fails
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
12. **Chapter 15's forward arrow is knowingly stale.** `15 → 36` should be
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
   rail, contents list and inlined `rail.js`. The tables in State record `text`; the
   build prints `page`. Neither is stale.

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

20. **Chapter 28 builds at 46 minutes** — inside the 25–50 band, outside the 30–42
   advisory, and flagged by the build. It is the longest in the part by 1,400 words and
   was already a split candidate. Splits get two numbers at plan time, so this is
   Part H's planning session, not a change to make now.


---

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
a census of the bodies is authoritative. `census_g.py` does it in one pass.

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

Part G now runs 32–43 minutes against a 30–42 advisory. Only chapter 28 is outside
it, by one minute rather than four.

**PARTS A TO F HAVE NOT BEEN REBUILT AND STILL CARRY THE OLD FIGURE.** The scripts
are correct; the pages are not. Every page in chapters 01–24 overstates its reading
time by roughly two to three minutes until it is rebuilt locally. Parts D, E and F
have retained bodies and can be rebuilt directly. **Parts A–C have no retained
bodies** — the path there is `debuild.py extract` first, which is now safe because
all twelve pages tested round-trip identical.

**Do not re-read the band thresholds against the old numbers.** The 25–50 band and
the 30–42 advisory were set when every measurement was two to three minutes high,
so in effect the advisory has been 28–40 all along. Whether to move the thresholds
or leave them is open, and it should be decided before Part H is planned, not
after.

**Chapter 28 is a one-minute overrun, not a four-minute one.** It remains a split
candidate on topic count, not on length.
