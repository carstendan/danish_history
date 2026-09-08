# Part H complete — chapters 33, 34, 35, 36

Two commits, source only. Everything generated rebuilds from them.

## Apply

```
git clone https://github.com/carstendan/danish_history.git
cd danish_history
git am ../part-h-complete.patch
```

Verified: applies cleanly to `main` at `2c7fe71`.

## Rebuild

From `files/`, in this order. The last two are not optional — rebuilt pages
lose their index links until `linkindex.py` runs.

```
python3 map_1660.py                     # item 43 fix; rebuilds ch 25's map
python3 map_1864.py                     # new spine map, 9 of 11
python3 figs_33.py ; python3 figs_34.py ; python3 figs_35.py ; python3 figs_36.py

for n in 32 33 34 35 36 ; do DK_DRAFT=c${n}_draft.md python3 mkbody.py $n ; done

python3 build_part_g.py                 # ch 25 needs it, for the 1660 map
python3 build_part_h.py

DK_CHAPTERS="$PWD/.." python3 linkindex.py
DK_CHAPTERS="$PWD/.." DK_OUT="$PWD/.." python3 index_generator.py
```

`cairosvg` is needed only for `rasterise()`. Without it the SVGs still get
written and the guards still run; you just get no PNG to look at. On macOS:
`brew install cairo && pip install cairosvg`.

## What you should see

```
tidy.py            no collisions, no orphans, no two-generations
mapfixture.py      seven maps — FIXTURE PASSES
seamcheck.py       seven maps — SEAM LAYER PASSES
map_*.py guards    nothing fires anywhere in the book
debuild.py verify  11 style-only (01–11) · 25 identical (12–36)
figcheck.py        63 figures match their source · 0 stale
vignettes.py       selftest PASSES · 63 total · 32–36 all 3/3, [f] yes, [n] yes
bookstats.py       36 of 43 built, 259,560 page words, 20.6 h
build exit codes   Part G 0 · Part H 0
```

| ch | title | words | min |
|----|-------|-------|-----|
| 33 | 1848: constitution and the First Schleswig War | 8,504 | 40 |
| 34 | 1864 | 7,538 | 36 |
| 35 | Industry, cooperatives, emigration and labour | 7,862 | 37 |
| 36 | Provisorietiden and the change of system | 7,670 | 37 |

Chapter 36 carries the Part H coda.

## Deliberately not in the patch

The built pages, the `c*_body.html` files, all `svg_*.txt`, and the index. They
are artifacts. **Verified rather than assumed**: both patches were applied to a
fresh clone of `main`, the sequence above was run, and the result compared file
by file against my working tree. Byte-identical, no differences at all.

## Still needing you

- **The kapitelstakst back-series** and **the Folketing election results
  1872–1901** (items 53 and 60). Four planned figures across Parts G and H had
  to be redrawn because these series could not be fetched, and the result is
  that **Part H ships fifteen figures and not one time series.** Both are
  library errands, and between them they would redraw four figures.
- **Cohen's roll**, entry 1848/98, for Morten Jørgensen Aldahl (ch 33 §05).
- **The 1907 optant convention**, for the stateless figures in ch 35 §10.
- **Ærø** (item 48): drawn as Danish crown territory since the 1660 map, and it
  belonged to Slesvig. Fixing it edits `DENMARK`'s vertex list, which four maps
  and four shipped chapters inherit. Your call.
- **Chapters 25, 26 and 27 still render four Summary items** (item 19). The new
  guard fails their build the moment it is ported into `build_part_g.py`, which
  is why it has not been.
- **Two guard gaps worth building together** (items 46, 61, 62): an exact
  pixel-width check where cairosvg is present, and rect-over-text in
  `collisions()`, which was blind four times in one session.
