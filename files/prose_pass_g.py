# -*- coding: utf-8 -*-
"""Part G prose pass: corrections agreed in REVIEW-PART-G-FINDINGS and the work order.

Two-phase write gate. Every replacement is validated against every file before any
file is written, so a bad pattern aborts with nothing on disk half-edited. Each edit
carries the reason it is being made.

Run: python3 prose_pass_g.py [--dry]
"""
import re
import sys

DRY = "--dry" in sys.argv

# (file, why, old, new). old must appear exactly once.
EDITS = [

    # ---------------------------------------------------------------- c25
    ("c25_body.html",
     "Interval does not compute against any anchor. Bornholm expelled Printzenskold in "
     "December 1658; the register is 1662, so the gap is three and a half years, not "
     "eighteen months. The chapter's own visit block already gives December 1658, so "
     "naming the date rather than an interval makes the page agree with itself.",
     "Swedish governor eighteen months earlier and handed itself back",
     "Swedish governor in December 1658 and handed itself back"),

    ("c25_body.html",
     "Estates assembled 10 September 1660; Frederik 3. died 9 February 1670. Nine years "
     "five months.",
     "in the castle where the estates had assembled ten years before.",
     "in the castle where the estates had assembled nine and a half years before."),

    # ---------------------------------------------------------------- c26
    ("c26_body.html",
     "Restores the vignette correction that was applied to the built page and never came "
     "back to the body, and fixes the release interval with it. Sophie Amalie died 20 "
     "February 1685; Leonora Christina was released 19 May. Publication year kept at "
     "1869, which three independent sources now settle.",
     "She would be let out in 1685, two months after the queen died, and the book would "
     "not be printed until 1869. When it appeared it made her reputation and destroyed "
     "Sophie Amalie's \u2014 a verdict delivered by a prisoner, a hundred and eighty-four "
     "years after she wrote it and two centuries after both women were dead.",
     "She would be let out in 1685, three months after the queen died, and the book would "
     "not be printed until 1869. When it appeared it made her reputation and destroyed "
     "Sophie Amalie's \u2014 a verdict delivered by a prisoner, published nearly two "
     "centuries after she wrote it and long after both women were dead."),

    ("c26_body.html",
     "Same interval in the body prose. The date 19 May 1685 is already asserted in this "
     "chapter's own figure 3 caption, so using it here costs no new claim.",
     "Leonora Christina was let out two months after Sophie Amalie died, on a petition",
     "Leonora Christina was let out on 19 May 1685, three months after Sophie Amalie "
     "died, on a petition"),

    ("c26_body.html",
     "Promotion artefact: when the vignette was lifted out of the prose the prose was not "
     "cut behind it. This paragraph restates four of the vignette's sentences at a few "
     "words' distance, with 'cell' changed to 'room'. The vignette says it better.",
     "<p>It is a strange book, and the strangest thing about it is its composure. She "
     "accuses nobody. Every humiliation is a trial divinely appointed; she calls herself "
     "Christ's cross-bearer, chosen to carry it. The narrative almost never leaves the "
     "room.</p>\n\n",
     ""),

    ("c26_body.html",
     "Sophie Amalie died 1685, Leonora Christina 1698, publication 1869: 184 and 171 "
     "years. This is the error the review opens with, surviving in the prose below the "
     "vignette that was fixed.",
     "and was not read by anybody until two hundred years after both women were dead.",
     "and was not read by anybody until both women had been dead for the better part of "
     "two centuries."),

    ("c26_body.html",
     "Born 8 July 1621, died 16 March 1698, four months short of her birthday.",
     "She was seventy-seven, and she had spent",
     "She was seventy-six, and she had spent"),

    ("c26_body.html",
     "The page gives her death as 1698 six paragraphs earlier and his as March 1699. That "
     "is a year, not a few months \u2014 and the coincidence is sharper stated correctly.",
     "he died in March 1699, a few months after Leonora Christina died at Maribo.",
     "he died in March 1699, a year after Leonora Christina died at Maribo, in the same "
     "week of the same month."),

    # ---------------------------------------------------------------- c29
    ("c29_body.html",
     "Rescript 14 September 1770, pull-back October 1771. Thirteen months.",
     "reintroduced a form of it fourteen months later",
     "reintroduced a form of it thirteen months later"),

    ("c29_body.html",
     "The subhead frames a paragraph in which part of the effect was immediate, and the "
     "paragraph carries only one of the ordinance's three mechanisms. All three now.",
     "<p><strong>It was not immediate.</strong> The release ran by cohort, and the last "
     "men were not free until 1800 \u2014 twelve years, which is the same mechanism by "
     "which Frederik 4. had ended vornedskab from 1702, one birth-year at a time.</p>",
     "<p><strong>It was immediate for some and slow for most.</strong> The bound ages went "
     "back at once to the fourteen-to-thirty-six of 1733, and men already too old for "
     "service or discharged from it were given their passes there and then. Everyone else "
     "was released by cohort, one birth-year at a time, and the last of them were not "
     "free until 1800 \u2014 twelve years, which is the same mechanism by which Frederik "
     "4. had ended vornedskab from 1702.</p>"),

    ("c29_body.html",
     "Fifth passage of the same mechanism, not in the review's list of four. The "
     "figcaption states it in the same halves.",
     "The ordinance of 20 June 1788 put the band back to the range of 1733 and set the "
     "end at 1 January 1800 \u2014 three years after the column was finished.",
     "The ordinance of 20 June 1788 worked three ways at once: it put the band back to "
     "the range of 1733, gave immediate freedom passes to men already too old for service "
     "and to those discharged from it, and released one cohort in each following year, "
     "the last on 1 January 1800 \u2014 three years after the column was finished."),

    ("c29_body.html",
     "Summary item 4 carries the cohort staircase and neither of the immediate effects.",
     "on 20 June 1788 the stavnsb\u00e5nd was ended \u2014 by cohort, over twelve years, "
     "with the landowners relieved of conscription in the same stroke,",
     "on 20 June 1788 the stavnsb\u00e5nd was ended \u2014 the bound ages put back at once "
     "to the range of 1733, the over-age and the discharged freed on the spot, everyone "
     "else released a cohort a year until 1800 \u2014 with the landowners relieved of "
     "conscription in the same stroke,"),

    # ---------------------------------------------------------------- c30
    ("c30_body.html",
     "Chapter 30 reaches back into Part F and nothing on the page prepares the reader for "
     "it. Orientation sentence at the head of the first narrative section, per review "
     "\u00a74.",
     "<p>Denmark went east before it went west, and",
     "<p>A word before the story, because this chapter does not follow the one before it "
     "in time. It runs from 1620 to 1803: chapter 29 stopped at 1788 and chapter 31 will "
     "open in 1784. The Danish Atlantic was one institution working continuously for a "
     "hundred and eighty years, and cutting it into chronological slices would break the "
     "thing it has to show. So the clock goes back here, once, and then forward again.</p>"
     "\n\n<p>Denmark went east before it went west, and"),
]


def move_marie_grubbe(h):
    """Chapter 27 \u00a71.3: the vignette sits at the foot of \u00a705, Tordenskjold, but the
    scene is summer 1711 and what strands Holberg at the ferry house is the plague, which
    is \u00a704. Moving it gives \u00a704 a vignette and leaves \u00a705 with one."""
    a = h.find('<div class="vig">\n<h4>Vignette \u00b7 Marie Grubbe')
    if a < 0:
        raise SystemExit("!! c27: Marie Grubbe vignette block not found")
    end = h.find('</div>', h.find('class="who"', a))
    if end < 0:
        raise SystemExit("!! c27: could not find the end of the vignette block")
    b = end + len('</div>')
    block = h[a:b]
    # it must currently sit after the s05 heading and before the s06 heading
    s05, s06 = h.find('<h2 id="s05"'), h.find('<h2 id="s06"')
    if not (s05 < a < s06):
        raise SystemExit("!! c27: vignette is not where the review says it is; stopping")
    anchor = '<figure>\n{{SVG_PLAGUE}}'
    if h.count(anchor) != 1:
        raise SystemExit("!! c27: plague figure anchor matched %d times" % h.count(anchor))
    if not (h.find('<h2 id="s04"') < h.find(anchor) < s05):
        raise SystemExit("!! c27: plague figure is not inside \u00a704; stopping")
    h = h[:a].rstrip('\n') + '\n\n' + h[b:].lstrip('\n')
    return h.replace(anchor, block + '\n\n' + anchor, 1)


# ---------------------------------------------------------------- phase 1: validate
loaded, plan = {}, []
for path, why, old, new in EDITS:
    if path not in loaded:
        loaded[path] = open(path, encoding='utf-8').read()
    n = loaded[path].count(old)
    if n != 1:
        raise SystemExit("!! %s: pattern matched %d times, expected 1\n   %s"
                         % (path, n, old[:100]))
    plan.append((path, why, old, new))
print("phase 1: %d replacements validated across %d files" % (len(plan), len(loaded)))

# ---------------------------------------------------------------- phase 2: apply
out = dict(loaded)
for path, why, old, new in plan:
    out[path] = out[path].replace(old, new, 1)

if 'c27_body.html' not in out:
    out['c27_body.html'] = open('c27_body.html', encoding='utf-8').read()
out['c27_body.html'] = move_marie_grubbe(out['c27_body.html'])

if DRY:
    print("dry run: nothing written")
    sys.exit(0)
for path, text in out.items():
    open(path, 'w', encoding='utf-8').write(text)
print("phase 2: wrote %s" % ", ".join(sorted(out)))
