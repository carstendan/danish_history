# PART G — STATE, end of drafting session

*Written so that a new session can pick this up cold. Read `PLAN_G.md` (v18) first;
this file records what happened during drafting that the plan does not.*

---

## 1. What exists

| chapter | prose | vignettes | apparatus | figures |
|---|---|---|---|---|
| 25 The kingdom made hereditary, 1660–1670 | ✅ 9 §§ | ✅ 3 | ✅ | ✅ 3 |
| 26 Law, rank, and the war for Skåne, 1670–1699 | ✅ 10 §§ | ✅ 3 | ✅ | ✅ 3 |
| 27 The last war for the Sound, 1699–1721 | ✅ 9 §§ | ✅ 3 | ✅ | ✅ 3 |
| 28 The bound countryside and the pious state, 1721–1770 | ✅ 10 §§ | ✅ 3 | ✅ | ✅ 3 |
| 29 Struensee, and the village taken apart, 1770–1788 | ✅ 10 §§ | ⚠️ 2 of 3 | ✅ | ✅ 3 |
| 30 The Danish Atlantic, 1620–1803 | ✅ 10 §§ | ✅ 3 | ✅ | ✅ 3 |
| 31 The flourishing trade and the wreck of it, 1784–1814 | ⚠️ 5 of 10 §§ | ⚠️ 1 of 3 | ❌ | ❌ |

**Scripts written:** `map_1660.py`, `map_1721.py`, `figs_25.py`, `figs_26.py`,
`figs_27.py`, `figs_28.py`, `figs_29.py`, `figs_30.py`, `vignettes.py`.
**Scripts modified:** `mapfixture.py` and `seamcheck.py` — 1660 and 1721 registered,
with envelopes, curated cases and SETS entries. These overwrite the uploaded versions.

**Not yet written:** chapter 31 §§06–10 and the part coda, chapter 31's apparatus,
`figs_31.py`, `build_part_g.py`, the `--indigo` token in `style.css`.

---

## 2. Blocking items

**Two vignettes are unresolved and both are lookups, not searches.**

1. **Chapter 29's third vignette.** On 14 September 1788 the tenants of
   Brahetrolleborg on Funen received hereditary tenancy letters in the castle
   courtyard; six farms in one village got theirs that day. The Trolleborg parish
   history is digitised at `ronlev.dk/bibliotek/4102.pdf` and lists those farms and
   holders by name. Without a name from it, chapter 29 ships with three elite
   vignettes — the worst balance in the part.
2. **Chapter 28's confirmand.** Replaced by Christian 6. on the Dovre descent, which
   works, but leaves chapter 28 with two elite vignettes to one peasant. If anyone
   ever opens Arkivalieronline on a parish register from 1736–40, a named confirmand
   should displace the king.

**Two dates could not be settled from reference works** (chapter 27, both marked in
the draft): the Frederiksborg peace is given as 3 June, 3 July, and 3 July Julian /
14 July Gregorian by three academic sources — a disagreement about the *month*, which
D-6 does not resolve; and the Slesvig homage is 4 September 1721 in Lex's dedicated
article and 4 July in two general histories. Both need the documents.

---

## 3. Verification queue

Claims that are in the drafts and are **not** yet verified. Each is flagged in place.

- **25** — the Kongelov's signature date of 14 November 1665 is disputed (some argue
  it antedated); sealing was 1669.
- **26** — Christian 5. died after a hunting accident. Griffenfeld's mistress being
  Bielke's wife rests on one DBL sentence. *Jammers Minde* published 1867 or 1869.
  Casualty proportion at Lund.
- **27** — the horses killed on the beach at Helsingborg; Marie Grubbe's third
  husband and what she told Holberg, which should rest on Holberg's letter and not
  on Jacobsen's novel.
- **30** — the St Jan rising began 23 November per the specialist literature and 13
  November per Danish Wikipedia.
- **31** — the Christiansborg fire of 1794 and the city fire of 1795, both dates; the
  1807 governing commission for Norway, its constitution and dates.

**Two source errors found and recorded so they are not re-imported.** Lex's article
on the Kongelov says Frederik 3. signed it on his birthday (he was born 18 March) and
that it was first read at Christian 5.'s anointing in 1670 (the anointing was 7 June
1671). A popular source credits the Liberty Column to Frederik 7., born 1808.

---

## 4. Technical findings

**`overruns()` was under-reporting by about ten per cent.** The 5.55 units-per-character
constant inherited from `figs_24.py` is too low for this mono face; measured off the
raster it is about **6.1**. `figs_25.py` through `figs_30.py` use 6.1. **`figs_24.py`
still has 5.55, and Part F's four figure scripts should be re-run under the corrected
constant** — there is a real chance something shipped with text off the canvas.

What the guard still cannot see, and what only looking catches: text overflowing a
*container* rather than the canvas, and text crossing a column divider. Both happened
in chapter 26 and passed the guard clean.

**The Härjedalen fault in `map_1397.py` is real and untouched.** Sveg, Ytterhogdal and
the country east of about 14.5°E at 62°N fall inside `SWEDEN` and outside `NORWAY`.
Härjedalen was Norwegian until Brömsebro in 1645, so **1397, 1500 and 1600 each give
roughly the eastern half of a Norwegian province to Sweden two and a half centuries
early.** It is not a seam fault — the border is shared exactly, it is simply drawn in
the wrong place — which is why three verification layers and a shipped review all
missed it. `mapfixture.py` as delivered contains the Sveg case that catches it, but
registered only against 1660, so the standing fixture passes while three shipped maps
stay wrong. Fixing it means moving shared vertices in `NORWAY` and `SWEDEN` and
rebuilding Parts E and F.

**Scripted edits must assert and then be verified.** Assertions caught several silent
no-ops. But an assertion that aborts the script leaves the file unwritten while
*later* commands in the same shell line still print success — I read that as
confirmation three times running on `map_1721.py`. Grep for the new string after
editing; do not trust the run.

---

## 5. Figures that diverged from the plan, and why

Five of twenty-one figures are not what `PLAN_G.md` specifies. Each says so in its
script's docstring. The pattern is the same in every case: **the planned figure would
have required numbers the sources do not supply.**

- **27(b)** plague: the planned weekly burial curve is unbuildable — reference works
  differ by a factor of three or four on the same months. Replaced by the containment
  sequence plus the four published death tolls shown disagreeing.
- **28(a)** hoveri: not a calendar. The reckonings give annual totals and the
  spanddag/gangdag split, not dates. The figure counts 365 squares and says it is
  counting.
- **29(a)** village: schematic, and labelled as such. A named village needs its real
  enclosure map.
- **29(c)** the band: replaces the cohort staircase, because the 1788 ordinance did
  not release men by birth year — it reverted the bound ages to 14–36 at once and
  ended the bond on 1 January 1800.
- **30(b) and 30(c)**: the Christiansted plat and the *Fredensborg* in section both
  need measurements I could not source. Replaced by the three-surveys figure, which
  carries the cadastral thread, and the papers figure, which carries the archive
  asymmetry.

---

## 6. Threads the plan does not record

These emerged in drafting and are load-bearing across chapters.

- **The cadastral thread** runs 25 → 26 → 29 → 30 and lands in figure 30(b): the
  state converts every Danish farm to a number in 1662–64, measures every field in
  1682–83, ruled St Croix into lots in 1734, and takes the village apart in the
  1780s. The third is the only one never counted as an achievement of the
  enlightened state.
- **The two queens.** Sophie Amalie's reputation was made by Molesworth's hearsay and
  *Jammers Minde*; Sophie Magdalene's by Dorothea Biehl, published after 1864. Both
  demolitions were written by people with a national argument. 25 and 28 now make one
  claim about how Danish history got written.
- **The instrument, not the man.** Struensee ruled by cabinet order through a sick
  king; Guldberg overthrew him and ruled by cabinet order through that king's
  guardians. The constitutional hole is chapter 25's Kongelov, failing for the first
  time in 1770.
- **The two monuments.** Chapter 29's Liberty Column and chapter 30's 1792 ordinance
  are the same act of commemoration: a true first, told in a way that omits what it
  cost and what it did not do. Chapter 30's closing paragraph names the parallel.
- **Krieger** built about half the 241 rytterskoler and then the standard fire-houses
  after 1728 — one architect for the village schools and the burnt-out capital.

---

## 7. New carry-forwards opened in drafting

Not in the plan's debt table; add before the ledger pass.

- `25 → 27` — vornedskab, promised in 25, paid in 27 §08. **Was missing from the draft
  and added late.** The ledger caught it; reading the chapter would not have.
- `25 → 28` — the parish clergy as the state's reach into every village.
- `26 → 28` — Norske Lov of 1687 replaced the 1604 law, which corrects how the
  Norwegian apparatus is usually described.
- `27 → 30` and `28 → 30` — the Moravians reached the West Indies in 1732 and
  Greenland in 1733.
- `28 → 31` — the grain monopoly of 1735 becomes the Norwegian famine of 1807–14 and
  Wergeland's charge of 1816. — The Kurantbank of 1736 is what the 1813 bankruptcy
  destroys.
- `30 → 31` — Ernst Schimmelmann, who wrote the 1791 memorandum, presides over the
  bankruptcy of 1813.
- `27 → Part H` — the 1721 homage instruments were unclear about whether the Kongelov's
  female-line succession extended to Slesvig. That ambiguity is the legal origin of
  the Schleswig question.

---

## 8. Immediate next steps

1. Chapter 31 §§06–10 and the part coda. Research needed: the gunboat war, the
   bankruptcy of 5 January 1813, Kiel, Eidsvoll, and the school act of 1814.
2. Chapter 31's remaining two vignettes (Friederike Brun at Sophienholm, September
   1807; a schoolteacher under the 1814 act) and its apparatus.
3. `figs_31.py`.
4. `build_part_g.py`, `--indigo:#2F4C7A` in `style.css`, `index_generator.py`'s `E`
   table and its five hardcoded strings.
5. The ledger re-point pass across chapters 15, 19, 20, 21, 22, 23, 24, bundled with
   open items 5a and 7.
6. Update `HANDOFF.md`: the debt tally error, the spine-map list still saying 1658,
   D-1's sixth cross-reference form, D-6's calendar convention, and Lesson 1's
   narrative-plus-fixed-apparatus formula.
