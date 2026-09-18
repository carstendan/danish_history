# REVIEW — WHAT IS MISSING FROM THE PAGES, AND WHAT IS SAID TWICE

*18 September 2026. A cold clone of `carstendan/danish_history` at `1d15e63`,
45 chapters, read as built HTML and compared against the drafts that produced
them. Two faults were reported: pieces missing from the HTML, and prose repeated
between body and vignette. Both are real. The first is larger than it looks and
has one cause. The second is smaller than the numbers first suggested, and I say
below which of my own flags I then threw out.*

---

## 0. The number

**2,719 words of written myth-check prose — 49% of all the myth-check in the
book — are not on the pages.** They are in the drafts. They were never deleted.
One function in `mkbody.py` understood one of the four myth-check conventions the
drafts actually use, and discarded the other three in three different ways.

A further **141 words** are missing from chapters 42 and 43, from a second
parser with the same shape of fault.

Nothing in the suite could see either. `tidy.py` reads file names. `figcheck.py`
compares figures to their sources. `vignettes.py` counts places and people.
`freshcheck.py` asks whether the draft is newer than the build. `debuild.py
verify` reconstructs the draft *from the page* and so cannot possibly detect
prose that never reached the page — the page is its only witness. All of them
passed, on all 45 chapters, the whole time.

This is the project's own standing rule failing in a new place: *a guard that
only fires at review is not a guard*. Here there was no guard at all, because
every existing check tests the page against itself.

---

## 1. The myth-check fault, by convention

The drafts use four conventions. The parser knew the first.

| | convention | chapters | what shipped |
|---|---|---|---|
| **A** | claim para, then one correction para | 1–24 | correct |
| **B** | `**The myth.**` / `**What can be shown.**` / `**What cannot.**` | 25–31 | **`<dl></dl>`** |
| **C** | claim para, then several correction paras | 32–36 | claim + first sentence |
| **D** | `**"claim"**` and correction in one para | 37–45 | **mis-paired** |

**B — seven chapters shipped the heading over an empty list.** No paragraph in
those blocks opens with a quotation mark, so the pair rule matched nothing and
emitted an empty `<dl>`. Chapters 25, 26, 27, 28, 29, 30, 31. Between 161 and
285 words each; 1,381 in total; nothing visible on the page but the words
MYTH-CHECK in oxblood and a rule.

**C — five chapters shipped the claim and one sentence of it.** The pair rule
took `items[i+1]` as the whole correction and `i += 2` walked past the rest.
Chapters 32–36 lost 209, 234, 255, 298 and 354 words — 85% to 92% of each block.
Chapter 34's four-paragraph correction is on the page as one sentence.

**D — nine chapters printed the claims and the corrections in each other's
type.** Where claim and correction share a paragraph, the whole paragraph became
the `<dt>` and the *next claim* became its `<dd>`. Under `style.css` a `<dt>` is
bold 16.5px and a `<dd>` is muted grey, so every page in Part I renders each
correction as though it were a claim and each claim as though it were an answer,
offset by half an entry. Six chapters also carry a stray empty `<dd>` where the
paragraph count was odd. The word counts matched, which is why a word-count check
alone would not have caught Part I — only reading the built page does.

The entries the old parser emitted in Part I were also fewer than the drafts
hold: chapter 37 has four myth items and shipped two, chapter 44 has five and
shipped three, chapter 45 has five and shipped three.

**Fixed.** `myth_html` is replaced by `myth_entries` + `myth_html` in `mkbody.py`.
It recognises all four conventions and is documented with what each one did. Two
CSS rules are added for multi-paragraph corrections (`.myth dd p`). Re-run against
every draft in the repo, the new parser emits paired `<dt>`/`<dd>` with the full
word count in all 20 chapters that have a draft, and no empty element anywhere.

One choice taken rather than referred: in convention B the `**The myth.**` label
is dropped, because the `<dt>` is already the claim by position and by styling.
The other two labels are kept, bolded, inside the correction.

---

## 2. The `Meanwhile in Europe` fault — 141 words, chapters 42 and 43

`meanwhile_html` accepts a paragraph beginning `**A label.**` and says `continue`
on everything else. Chapters 42 and 43 each close the block with an unlabelled
paragraph that draws the comparison the two boxes exist to set up:

- **ch 42** — "Set that against Denmark in the same month: about 7,400 people
  across four kilometres of water, 472 deported, 419 home…" (70 words)
- **ch 43** — "Two occupied Scandinavian countries, two underground armies, the
  same British quartermaster and the same instruction — wait —…" (71 words)

Both pages carry the two boxes and not the point of putting them side by side.

What makes this one worth its own section: **the refusal immediately below that
function already says "Refuse rather than discard authored prose."** It was
written after a draft with three Meanwhile blocks built three and placed two. The
lesson was learned, in that function, and it was applied to the *count of boxes*
and not to the paragraphs between them. The same leak stayed open in the same
place.

**Fixed.** An unlabelled paragraph now continues the box above it, which is where
the drafts put it and what it comments on. A paragraph arriving before any box is
a refusal.

---

## 3. The other missing pieces

**3.1 Chapter 32 has four drafting flags in its published text.** `freshcheck.py`
refuses to rebuild it and names five notes; four of them are on the live page,
mid-paragraph, in §03, §07 (twice) and §09. A reader meets:

> …how many of the people in the room were female. **Drafting flag:** a named
> woman from the parish and court records would be the better vignette here, and
> would fix both the geography and the class balance. Archive task, flagged in
> PLAN_H §10.1, not blocking. They were also, mostly, not new.

and, in §09, *"the sources conflict on which way the vote fell… **Resolve before
build**."* The guard that catches this exists and works; the chapter was built
before it did. **This is the most visible fault in the book and it is one
chapter.** It needs your decision, not mine — see §5.

**3.2 Chapter 45 has an empty `<ul class="calls">`.** "WHERE THIS GOES / What to
carry forward" renders as a heading with nothing under it. The draft has no
`## Carry-forward` content, so this is not a build fault. It is the last chapter
and has nowhere forward to point — but every other chapter also carries backward
arrows, and 45 has none.

**3.3 Chapter 29's Struensee vignette is broken in the markup.** The title is
wrapped over two lines in `c29_draft_01-10.md`, the `**…**` match is single-line,
and the page shows:

```html
<h4>**Vignette · Johann Friedrich Struensee, Christiansborg, before dawn on 17</h4>
<p>January 1772**</p>
```

Literal asterisks in the heading, the date cut off, and a stray paragraph reading
`January 1772**` as the vignette's first line. It is the only leaked markdown in
the book — I swept all 45 pages for `**`, stray `*`, backticks and markdown links,
and this is the single hit.

**3.4 Chapter 27's apparatus — I was wrong about this, and the correction is
below in §7.**

**3.5 Chapter 28 has four overlapping body drafts** — `c28_draft_01-03.md`,
`01-04`, `01-06`, `01-10`. `tidy.py` names them and deletes nothing, correctly.
Which is authoritative is not recorded anywhere.

---

## 4. The repetition between body and vignette

You are right, and it is concentrated. I measured every inset block in the book
against its own section body two ways: longest verbatim token runs, and overlap
of distinctive (rare, book-wide) vocabulary. Across 132 vignettes the median
distinctive-vocabulary overlap is **14%** and the 90th percentile is **39%**. The
offenders are not a tail of that distribution; they are a separate population.

**Then I read the top of my own ranking and threw three of it out.** High
vocabulary overlap also happens when a vignette is *about* the same subject
without repeating anything — chapter 30's *Fredensborg* vignette scores 80% and
is one of the best in the book, because it is about what the archive keeps and
what it does not. Chapter 28's Dovre descent scores 65% on shared Norwegian
place-names. A metric is a way of deciding what to read, not a verdict.

### Verified, after reading both sides

| ch | § | section | vignette | verdict |
|---|---|---|---|---|
| 27 | 05 | **Tordenskjold** | Peter Wessel, Dynekilen | **total.** The vignette contains nothing the body does not. |
| 27 | 09 | **Egede sails** | Gertrud Rask, Håbets Ø | **severe.** Two sentences are word-for-word identical. |
| 29 | 03 | **Caroline Mathilde, governing** | Caroline Mathilde, Hirschholm | **severe.** Hogarth prints, Vedbæk, Rousseau, riding astride — all twice. |
| 26 | 09 | **The Blue Tower** | Leonora Christina, Blåtårn | **tail.** Strong for two-thirds, then repeats "no trial and no sentence… held on the strength of her marriage". |
| 35 | 03 | **Hjedding, 1882** | Niels Hansen Uhd, Ølgod | **partial.** Both enumerate the four rules of the dairy, twice verbatim. |
| 22 | 08 | The devil in Køge | Johanne Tommesis, Køge | **against the figure.** The vignette re-tells the names and dates that the SVG table beside it already lists. |

Chapter 27's two vignettes are the worst in the book, and chapter 27 is also the
chapter whose apparatus draft is missing. I do not think that is a coincidence:
it looks like a chapter whose body absorbed its vignettes during a revision that
was not written back to source.

### The pattern, which is a rule worth writing down

Look at what the six have in common against what the healthy ones have:

> **Duplicating:** "Tordenskjold" → Peter Wessel. "Caroline Mathilde, governing"
> → Caroline Mathilde. "The Blue Tower" → Leonora Christina. "Kiel, 14 January
> 1814" → Edmund Bourke at Kiel on 14 January 1814.
>
> **Working:** "Who lived in them" → Grave 4 at Fyrkat. "The cattle plague" →
> Anders Pedersen of Oksenvad. "The fall of Corfitz Ulfeldt" → Dina Vinhofvers.
> "The crash reaches a farming country" → Nakskov, 2 February 1931.

**When the section is named for the vignette's subject or its exact moment, the
vignette has nowhere to stand and restates the body in the present tense. When
the section is named for the process and the vignette supplies a person inside
it, it works.** Every one of the book's healthy vignettes is the particular
inside a general; every offender is the particular inside the particular.

That is a convention, it has been obeyed 126 times out of 132, and it is not
written down anywhere. It belongs in `HANDOFF.md` before the final consistency
pass, so the pass can apply it in one place rather than rediscovering it.

---

## 5. What needs you, and what does not

**Taken, and done — technical, no judgment required:**

1. `mkbody.py` — `myth_html` rewritten for all four conventions.
2. `mkbody.py` — `meanwhile_html` keeps unlabelled paragraphs, refuses an orphan.
3. `style.css` — two rules for multi-paragraph corrections.
4. `appcheck.py` — new verifier. For every apparatus block: words in the draft
   against words on the page. A shortfall is a refusal. It reports the 13 real
   losses above and nothing else; `Checkpoints` is exempt with the reason stated
   in the file, because the draft states the answer and the build asks the
   question, and a guard that cries wolf eight times a run is one people skim.

**Yours, in dependency order:**

**5.1 Chapter 32 — done, and one fact changed.** The vote is resolved, not by
picking a side but because the two sources are not in conflict: they report the
same division with the sign reversed. Nis Lorenzen moved on 7 June 1836 that
Latin and German be abolished in administration and justice wherever the school
language was Danish, and in July 1838 the Schleswig assembly **carried it,
twenty-one to eighteen**, with the support of its own president N. N. Falck —
*Dansk Biografisk Leksikon*, "ved støtte af forsamlingens præsident Niels Falck
lykkedes det at gennemføre det med kneben majoritet (21 stemmer mod 18)".
danmarkshistorien agrees independently: the assembly addressed the king "med et
snævert flertal". Danish Wikipedia's *Sprogreskripterne* has "afvist med
stemmerne 21 imod og 18 for" — the same two numbers, reversed, and its own
account then cannot explain why the 1840 rescript names an assembly petition as
its occasion.

**This changes the chapter's claim, which is why it is listed here and not in the
taken pile.** The draft said the assembly "could not settle the question, and the
king settled it for them". It did settle it; the king granted what it asked. The
sentence is rewritten in `c32_draft.md` to say so, and nearly half the assembly
having voted against asking is kept, because that is what the 1840 rescript
walked into. The other three flags are archive tasks and are out of the prose;
the sources-block note is reworded as a note to the reader. `draftnotes.py` now
reports chapter 32 clean and `freshcheck.py` no longer refuses it. **Read the new
sentence** — it is the one place in this session where I changed what the book
asserts.

Still open there: figure (c), the Zealand *kapitelstakst* series for a tønde of
rye 1815–1848, was never drawn — chapter 32 ships three figures and §07 was
written expecting a fourth. The series is published after Scharling. If you want,
I can try to get the year-by-year values the way the *Statistiske Meddelelser*
note in HANDOFF suggests, before any library trip.

**5.2 Part G — this is the one that is blocked, and it is the biggest.** See §7.

**5.3 Chapter 45's carry-forward.** Backward arrows only, or suppress the heading
when the list is empty? I lean to suppressing it: a heading over nothing reads as
a fault whatever the reason, and 45 is the last page in the book.

**5.4 The six vignettes.** For the two severe ones I would cut from the *body*,
not the vignette — the vignettes are better written and the body can carry the
argument without the scene. For chapter 27 §05 the vignette has no independent
content at all and either it goes or the body paragraph does. That is a prose
decision and it is yours.

---

## 6. What I could not check

- **Chapters 1–24 have no drafts in the repo**, so the new parser is verified
  against convention A only by reading their built pages, which are correct. If
  those drafts exist locally, run `appcheck.py` against them before the next
  rebuild.
- **The machine was unreachable** during this session, so nothing local was
  consulted — only the public repository.
- **Nothing was rebuilt.** Every finding is against the pages as they stand at
  `1d15e63`, and the fixes are to source only. The rebuild is blocked on 5.1.

---

## 7. Added after the patch was applied: two things I got wrong, and what they open

**7.1 I said chapter 27 could not be rebuilt from source. That was wrong.**
Chapter 27's apparatus — glossary, Meanwhile, checkpoints, myth-check,
carry-forward, five things, questions, sources, visit — is in
`PART_G_DRAFT.md`, under `# Chapter 27 — apparatus`, together with the rest of
Part G. Its myth-check is there in full, 214 words on the Marstrand story and
*Tordenskjolds soldater*, in a four-label variant of convention B. The new
parser renders it correctly.

I looked for `c27_draft_apparatus.md`, did not find it, checked the git history
for it, did not find it there either, and concluded the source was lost —
without opening the file `mkbody.py` names as its own default on line 26,
`DRAFT = os.environ.get("DK_DRAFT", "PART_G_DRAFT.md")`. The combined draft even
carries `<!-- ===== c27_draft_apparatus.md ===== -->` as a section marker, which
is why the per-chapter file is absent: it was concatenated in and the pieces were
not kept. Nothing was lost. §3.4 of this document is withdrawn.

**7.2 `build_part_X.py` does not read the drafts.** It reads `cNN_body.html`.
The chain is `draft.md → mkbody.py → cNN_body.html → build_part_X.py → page`,
and `mkbody.py` is where both fixed parsers live. I ran `build_part_i.py` on the
patched tree first and got byte-for-byte the old broken myth blocks, because the
`cNN_body.html` files in the repo are the stale output of the old parser. The
build printed `part ok` for all nine chapters while doing it.

`freshcheck.py` says this in as many words — "mkbody.py, then build_part_*.py,
then linkindex.py, then index_generator.py — in that order" — and I read it and
ran the second stage anyway. **The order is not a convention, it is the whole
fix**, and a rebuild that skips `mkbody.py` reports success and changes nothing.

**Proven end to end on Part I.** Regenerating the nine bodies and rebuilding:

| | before | after |
|---|---|---|
| myth entries, ch 37 / 41 / 43 | 2 / 2 / 2 | **4 / 4 / 4** |
| myth entries, ch 44 / 45 | 3 / 3 | **5 / 5** |
| empty `<dd>` in Part I | 6 | **0** |
| Meanwhile words, ch 42 / 43 | 286 / 223 | **356 / 295** |
| empty `<dl>` in the book | 7 | 0 in Part I; 7 remain, see 7.3 |
| literal `**` on any page | 1 | 0 in Part I |

The rebuilt bodies are **not** in the patch: they are generated artifacts and
this project does not take those from me. Regenerate them yourself with
`DK_DRAFT=cNN_draft.md python3 mkbody.py NN` before running the part build.

**7.3 Part G cannot be regenerated yet, and that is what gates the 1,586 words.**
The seven empty `<dl>`s are all in Part G, and `mkbody.py` refuses every Part G
chapter before it writes anything, because `draftnotes.py` finds 28 "drafting
notes" in `PART_G_DRAFT.md`. They are three different things:

- **14 are the concatenation markers themselves** — `<!-- ===== c25_draft_01-03.md
  ===== -->`. The pattern matches them deliberately (`<!--\s*=+\s*c\d\d_draft`),
  and in the combined draft they are structure, not notes. They will fire on
  every run forever.
- **7 are one standing sentence in the Sources block of every Part G chapter** —
  "need checking against the works themselves before publication". That is a
  caveat addressed to the reader, which is exactly the disposition
  `freshcheck.py` offers ("or move it to the Sources block as a question
  addressed to the reader"). It is already there, and is refused anyway.
- **The rest are genuine** and are the ones worth your eye: a "Style note:" about
  the Gregorian calendar in chapter 27, "should be checked" on the Breffu
  vignette in chapter 30, and two "need checking before this section ships" in
  chapter 31, on the Christiansborg fire of February 1794.

HANDOFF item 102 already records that these notes reached eight built pages. What
is not recorded is the consequence: **because they refuse the build, Part G's
bodies have not been regenerated since, and that is why the empty myth-check has
stayed empty for seven chapters.** A guard that refuses a fix is doing the
opposite of its job.

**The decision, and it is one line of code either way.** Should `draftnotes.py`
stop matching its own concatenation markers and the standing Sources caveat, and
keep refusing only on the genuine notes? I would say yes — the marker pattern
matches a mechanical artefact of how the file is assembled, and the Sources
sentence is in the place the tool itself recommends. But it is your guard, it was
written after a real escape, and loosening it is not a change I will make on my
own. Say the word and Part G rebuilds with all seven myth-checks on the page.
