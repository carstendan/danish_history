# START HERE — Part I, chapter 38

Paste the block below as the opening message of the next session. It is written to
be self-contained; nothing in it assumes the previous session is in context.

---

Part I: Draft
I'm writing a long-form digital history of Denmark, 44 chapters, c. 13,000 BCE to
1953. Parts A–H are shipped and chapter 37 is shipped. Part I is chapters 37–44
and it is the last part. PLAN_I.md is agreed. This session drafts chapter 38 and
nothing else.

Clone github.com/carstendan/danish_history. From files/, cold run first, reporting
what fails rather than working around it:

  git status --short
  python3 tidy.py
  python3 mapfixture.py
  python3 seamcheck.py
  python3 debuild.py verify ../[0-9][0-9]-*.html
  python3 bookstats.py
  python3 vignettes.py . ; python3 vignettes.py --selftest
  python3 figcheck.py
  python3 narrative.py ../3[3-7]-*.html
  for m in map_*.py ; do python3 "$m" ; done

Expected as of the end of the chapter 37 session: tidy clean except Part D's ten
unrecoverable figures; seven maps pass; style-only for 01–11 and identical for
12–37 (11 and 26 respectively); 37 of 44 built, 267,428 page words, 21.2 h, 7
remaining of which 1 dense; 66 vignettes, selftest passes; figcheck 66 matched, 41
sourceless, 0 stale; chapter 37 measures 3L/4M/3H at 4,219 narrative and 7,896 page
words; maps print nothing but their "wrote" lines and regenerate byte-identical.
pip install cairosvg first or they warn. Anything different: stop and say so.

Then read HANDOFF.md (open items 1–75, conventions D-1 to D-10), PLAN_I.md, and
REVIEW-PART-G.md. Items 67–75 are new this session and 67, 69, 70 and 71 are
toolchain faults you will hit again if you do not read them.

Before drafting, work the verification queue in PLAN_I §14 as far as it bears on
chapter 38. In Parts H and I the plan has flagged vignettes that needed checking
and has been right every time; expect the same.

Also try, before anything else, the two research debts that are now located but not
fetched — item 73. Both are on the proven dst.dk route:
  - the Folketing election results 1872–1901, in six hæfter named in item 73
    (closes item 60, and makes chapter 36's figure 2 drawable as planned)
  - the kapitelstakst back-series (closes item 53, and chapter 32's figure 3)
Each of these retires a figure that had to be honestly redrawn as something else.
If either transcribes cleanly, say so before drafting — it changes what chapter 38
can draw too.

Chapter 38's section list and weights are in PLAN_I §6. Measure the draft against
that profile BEFORE reading it for quality; a profile with no heavy sections is a
defect regardless of word count (item 59). A draft that lands short is missing a
subject, not thin paragraphs — this has now held for five consecutive chapters
(item 72), so treat it as a rule and ask which subject is absent.

The build path for Part I now exists and chapter 38 needs three things added:
a HAND entry in mkbody.py, a CFG entry in build_part_i.py, and figs_38.py.
Chapter 37 is the worked example for all three. Then:

  python3 figs_38.py
  DK_DRAFT=c38_draft.md python3 mkbody.py 38
  python3 build_part_i.py
  python3 linkindex.py
  python3 index_generator.py
  python3 narrative.py ../38-*.html

Standing rules: compute numbers, never type them; assert on every scripted
replacement then confirm by whitespace-normalised search, not grep (item 69);
predict the symptom before making a change; rasterise and look at every figure —
four fault classes are invisible to every automated check and obvious in the PNG
(items 47, 50, 61, 70, 71); compute every dimension in a figure script; never hand
over or commit a generated file — patch of source only, proved against a fresh
clone.

I am not a historian. Historical judgement is yours to make and defend; tell me
where you differ from the standard account and why. Flag errors precisely and
don't soften them. If you need something from me, say what it blocks. I won't read
the prose until the chapter is finished, so don't hold the build waiting on me.

---

## What the chapter 37 session left undone

- **`mw_at` in `mkbody.py` still places exactly two `Meanwhile` blocks.** The guard
  added in item 67 refuses the build rather than dropping a third silently.
  Generalising the placement is a layout decision and is open.
- **Figure 1 of chapter 37 is not the figure PLAN_I asked for**, pending the
  *Valgene til Rigsdagen* fetch. If item 73 is discharged, draw the planned
  before-and-after as well, not instead.
- **The Part I band title "The small state" was chosen at build time**, not by the
  plan. One constant, `BAND_TITLE` in `build_part_i.py`.
- **Chapter 37 shipped at 38 minutes against a planned 37** (item 75). If that
  should be brought to 37, it is about 22 page words out of §05.
