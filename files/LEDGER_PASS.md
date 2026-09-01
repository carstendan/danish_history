# LEDGER PASS — work order

*Concrete instructions for re-pointing the forward arrows in shipped chapters, now
that Part G is 25–31 rather than 25–30.*

**What I can specify:** every arrow's content, its current target, its new target,
and the reason. **What I cannot:** the literal wording in the files, because I have
not seen `c15`, `c20`, `c21`, `c22`, `c23` or `c24`. Each row below therefore gives
a grep handle rather than a find/replace string. Locate the arrow, confirm it is the
one described, then change the target.

---

## Method

1. In each file, `grep -n` for the carry-forward block and for any chapter number
   ≥ 25 appearing anywhere in the prose. Arrows live in the carry-forward block, but
   the series also uses inline references like "the Atlantic slave trade (27)", and
   **those move too**.
2. Change targets per the table.
3. `renumber.py` handles nothing here on its own. Six of the twelve rows are content
   changes rather than a uniform shift, so run it only for the mechanical ≥29 shift
   and do the rest by hand — or skip it entirely and do all twelve by hand, which
   for twelve arrows is probably faster and definitely safer.
4. After editing, `grep` for the **new** target string in each file to confirm the
   write landed. An assertion that aborts leaves the file untouched while the rest
   of the command still reports success.
5. Rebuild the affected parts → `linkindex.py` → `index_generator.py` → upload.
   Rebuilt pages lose their index links.

---

## The twelve arrows

| file | grep handle | arrow | now | becomes | kind |
|---|---|---|---|---|---|
| c21 | "adelsvælde" | the noble regime dismantled | → 25 | **→ 25** | no change |
| c24 | "estates" / "Kongelov" | the estates meeting and the Kongelov | → 25 | **→ 25** | no change |
| c23 | "Leonora Christina" / "Jammers" | her imprisonment and the book | → 26 | **→ 26** | no change |
| c21 | "Gottorp" | the Gottorp line closed 1720–21 | → 26 | **→ 27** | content: Gottorp is settled in 27 |
| c24 | "snaphane" / "Skåne" | the snaphaner and the last attempt on Skåne | → 29 | **→ 26, 27** | content: snaphaner in 26, Helsingborg 1710 in 27 |
| c22 | "Trankebar" | Trankebar and the chartered company | → 27 | **→ 30** | content: the Atlantic chapter is 30 |
| c21 | "hoveri" / "bondens" | labour services and the bound peasantry | → 28 | **→ 28, 29** | content: the bond in 28, the reforms in 29 |
| c20 | "1536" / "Norge" | the Norway clause of the 1536 recess, to 1814 | → 28 | **→ 31** | content: a mechanical shift would wrongly say 29 |
| c22 | "1604" / "stattholder" | Norwegian law 1604, governor, mines | → 30 | **→ 28, 31** | content: apparatus in 28 §07, separation in 31 |
| c21 | "Glücksburg" | the Glücksburg line, a king from it in 1863 | → 32 | **→ Part H** | D-1 |
| c19 | "Ribe" / "1460" | Ribe 1460 to 1848, 1864, 1920 | → 32 | **→ Part H** | D-1 |
| ~~c15~~ | — | Estonia 1346 answered by the West Indies 1917 | → 36 | **deferred** | see below |

**Files touched:** c19, c20, c21, c22, c23, c24 — Parts E and F. **Eleven of the
twelve arrows.**

### Chapter 15 is deferred, deliberately

`ls files/` shows authored bodies for chapters 16–24 only. There is no
`c15_body.html`; Part D has never been re-run since the build script was renamed,
and its pages carry the old `--band` token and an `e` prefix from
`build_part_d.py` (open items 3 and 4). Editing a file the build does not read
would change nothing.

So `15 → 36` stays wrong for now, and it is the right one to leave: it points into
Part I, two parts away, and nothing shipping in Part G or Part H depends on it. Fix
it at the next Part D rebuild, which Part D needs anyway for the CSS token and the
prefix — three problems, one job.

**Add to `HANDOFF.md`'s open items** so a later session finds it as a known
deferral rather than rediscovering it as a fault: *chapter 15's forward arrow
points at 36 and should point at 30 and Part I; deferred because Part D has no
authored bodies in `files/`.*

---

## Carry-backs to add

These are new. Part G chapters point *back* at shipped chapters, which is the
chapter 21 → 19 Ditmarschen pattern. Nothing changes in the shipped files; these are
recorded here so the Part G build inserts them.

- `27 ← 23` — Sweden's Sound-toll exemption from Brömsebro 1645, abolished at
  Frederiksborg 1720. Chapter 23 argued the toll had become negotiable rather than a
  fact of geography.
- `25 ← 24` — Bornholm, which handed itself to the crown in 1658, is the one part of
  the kingdom left out of the 1662 land register.
- `26 ← 24` — Corfitz Ulfeldt's treason put his wife in the Blue Tower for
  twenty-two years without a charge.
- `30 ← 24` — Jens Kofoed's island rising is told as a liberation; Breffu's rising on
  St Jan is the same beat, and chapter 30 names the earlier one deliberately.

---

## New forward arrows opened in drafting

Not in the plan's original table. Add to the ledger when `HANDOFF.md` is updated.

- `25 → 27` — vornedskab, promised in 25 and paid in 27 §08. **This one was missing
  from the draft and added late.** The ledger caught it; reading the chapter would
  not have.
- `25 → 28` — the parish clergy as the state's reach into every village.
- `26 → 28` — Norske Lov of 1687 replaced the 1604 law.
- `27 → 30`, `28 → 30` — the Moravians reached the West Indies in 1732 and Greenland
  in 1733.
- `28 → 31` — the grain monopoly of 1735 becomes the Norwegian famine of 1807–14 and
  Wergeland's indictment of 1816; the Kurantbank of 1736 is what fails in 1813.
- `30 → 31` — Ernst Schimmelmann, author of the 1791 memorandum, presides over the
  1813 bankruptcy.
- `27 → Part H` — the 1721 homage instruments were unclear whether the Kongelov's
  female-line succession extended to Slesvig. That ambiguity is the legal origin of
  the Schleswig question.

---

## Bundle these into the same pass

Both force work on the same files, so doing them separately means rebuilding twice.

**Open item 7 — chapter 20's footer.** It says Part F runs to 1721; Part F ends in
1660. Its *Faith and the state* thread also promises pietism "in Part F"; pietism is
chapter 28.

**Open item 5a — Part E's shipped maps.** Chapters 16–19 carry pre-fix seam geometry
inlined. The re-point forces a Part E rebuild anyway, so the corrected maps ship at
the same time at no extra cost.

---

## Not in this pass

**The Härjedalen fault in `map_1397.py`.** Sveg and the country east of about 14.5°E
at 62°N sit inside `SWEDEN` on 1397, 1500 and 1600. It is real and documented in
`STATE_G.md` §4, and fixing it means moving shared vertices in `NORWAY` and `SWEDEN`
and rebuilding Parts E and F. It is a separate decision and should not be folded in
without being asked for.
