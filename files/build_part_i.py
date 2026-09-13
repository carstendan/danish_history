# -*- coding: utf-8 -*-
"""Build Part I. Same shape as build_part_h.py: per-chapter configs, one command,
self-verifying.

Checkpoints live here, keyed to section TITLE fragments rather than ids, so that
renaming a section breaks the build loudly instead of silently moving a checkpoint
somewhere else (lesson L10). Any checkpoint already sitting in the body is stripped
first, so the body and this file cannot disagree.

Part I is chapters 37-44, 1901-1953, and it is the last part. Only chapter 37 is
configured; 38 to 44 are planned but not drafted, and a config entry for a chapter
with no body fails loudly on the first run, which is intended. Chapter 44 will
carry the part coda via tail_extra, as 36 does for H - and, being the last chapter
of the book, will need a book coda as well, which no build script has yet had to
emit.

THE BAND COLOUR IS NEW. D and E are verdigris, F oxblood, G indigo, H slate; I is
moss, added to style.css as --moss for this part. THE BAND TITLE "The small state"
IS NOT IN PLAN_I - the plan names every chapter and never names the part. It is
one constant, BAND_TITLE below, and changing it changes the crumb, the footer and
the index together. Adding a token to the stylesheet is
precedented - --indigo went in for Part G - and `debuild.py` already handles the
consequence, which is that every page shipped before the token existed
reconstructs with a token it never had. Verify after building: 01-11 should stay
`style-only` and 12-36 `identical`. If 12-36 move to `style-only`, the drop list
in debuild.py has not picked the new token up and that must be fixed before
anything ships.

CHECKPOINTS ARE QUESTIONS, NOT PROSE. The chapter 32 draft writes its three
checkpoints as prose recaps - "where we are". Every part from A to G uses three
retrieval questions instead, and the .check rule in style.css is written for a
list. The questions below are derived from the draft's prose so they test what it
says is worth holding, but the prose itself is not reproduced. Changing that is a
change to every shipped part, not to Part H alone.

    python3 build_part_i.py            # strict: every figure must exist
    python3 build_part_i.py --stub     # missing figures become a loud placeholder

--stub exits non-zero even when everything else passes, so a stubbed page cannot be
mistaken for a finished one.
"""
import os
import re
import sys

from pagewords import pagewords   # one definition, shared

# Paths resolve relative to this script, not to wherever it is run from, and both
# can be overridden. The container paths that used to be hardcoded here meant the
# script only ran in one place; sources live beside it in files/ and built pages
# go to the parent, which is the layout on disk.
HERE = os.path.dirname(os.path.abspath(__file__))
G = os.environ.get('DK_SRC', HERE) + os.sep
OUT = os.environ.get('DK_OUT', os.path.dirname(HERE)) + os.sep
PART_I = '#4A5A46'          # --moss; D/E verdigris, F oxblood, G indigo, H slate
BAND_TITLE = 'The small state'   # not set by PLAN_I - see the docstring

CODA = ("coda", "", "What this part was about")

TAIL = [("myth", "", "Myth-check"), ("forward", "", "What to carry forward"),
        ("summary", "", "The page in five"), ("questions", "", "Questions &amp; discussion"),
        ("sources", "", "Sources"), ("visit", "", "Places you can visit")]

STUB = ('<svg viewBox="0 0 700 120" xmlns="http://www.w3.org/2000/svg" role="img" '
        'aria-label="Placeholder: this figure has not been drawn yet.">'
        '<rect x="1" y="1" width="698" height="118" fill="none" stroke="#2F4C7A" '
        'stroke-width="1.5" stroke-dasharray="7 5"/>'
        '<text x="350" y="58" text-anchor="middle" font-family="monospace" font-size="13" '
        'fill="#2F4C7A">FIGURE NOT YET DRAWN</text>'
        '<text x="350" y="78" text-anchor="middle" font-family="monospace" font-size="10" '
        'fill="#5F6157">%s</text></svg>')

CFG = {
 37: dict(
    name='37-reform-neutrality-and-the-sale-of-the-west-indies.html',
    body='c37_body.html',
    svgs={'SVG_SYVF': 'svg_syvf_1915.txt',
          'SVG_SOEFOLK': 'svg_soefolk_1918.txt',
          'SVG_AFSTEMNING': 'svg_afstemning_1916.txt'},
    sec=[("s01", "01", 'What the change of system actually changed'),
         ("s02", "02", 'The Radicals, 1905, and the splitting of the left'),
         ("s03", "03", 'Alberti'),
         ("s04", "04", 'The defence question, and a fortress never fired'),
         ("s05", "05", '5 June 1915: the seven categories, minus two'),
         ("s06", "06", 'August 1914: neutrality, and the mines in the Belts'),
         ("s07", "07", 'Gulasch, rationing, and the ships that did not come back'),
         ("s08", "08", 'What the islands were: 1848, 1878, and labour under the '
                       'Danish flag'),
         ("s09", "09", 'Selling them: the treaty, the Rigsdag, the referendum of '
                       'December 1916'),
         ("s10", "10", '31 March 1917')],
    checks=[
      ("The defence question, and a fortress never fired", [
        "The change of system of 1901 altered no word of the constitution. What did it "
        "actually change, and name two of the laws of 1903.",
        "Venstre took office as one party and was three within five years. What split it, "
        "and which two groups did the Radicals go looking for?",
        "Alberti was warned about by the National Bank and protected anyway. By whom, and "
        "on what grounds?"]),
      ("Gulasch, rationing, and the ships that did not come back", [
        "Name the seven categories the franchise of 1849 excluded, and say which two were "
        "admitted in 1915.",
        "What did the conservatives charge for giving up the privileged franchise to the "
        "Landsting?",
        "Why did Denmark mine the Great Belt in August 1914, and why did Britain accept "
        "it?"]),
      ("Selling them: the treaty, the Rigsdag, the referendum of December 1916", [
        "Of about ten thousand Danish merchant seamen, how many died, and how did two "
        "hundred of them die?",
        "What was Contract Day, and what happened on Contract Day 1878?",
        "Who declared the enslaved of the Danish West Indies free in 1848, what happened "
        "to him for it, and who had actually forced the decision?"]),
    ]),
}

def block(qs):
    return ('<div class="check">\n  <h4>Checkpoint</h4>\n  <ul>'
            + "".join("\n    <li>%s</li>" % q for q in qs) + '\n  </ul>\n</div>\n\n')


def build(n, c, stub):
    h = open(G + c['body'], encoding='utf-8').read()
    stubbed = []

    h = re.sub(r'<div class="check">.*?</div>\n\n', '', h, flags=re.S)
    heads = [(m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip())
             for m in re.finditer(r'<h2 id="(s\d\d)">(.*?)</h2>', h, re.S)]
    for frag, qs in c['checks']:
        hit = [sid for sid, t in heads if frag.lower() in t.lower()]
        if len(hit) != 1:
            raise SystemExit("!! chapter %s: anchor %r matched %d sections" % (n, frag, len(hit)))
        a = '<h2 id="%s">' % hit[0]
        h = h.replace(a, block(qs) + a, 1)

    page = [(sid, re.sub(r'<[^>]+>', '', t).strip()) for sid, t in heads]
    want = [(sid, lab) for sid, num, lab in c['sec']]
    got = [(sid, re.sub(r'^\d\d\s*/\s*NARRATIVE', '', t).strip()) for sid, t in page]
    if got != want:
        for w, g in zip(want, got):
            if w != g:
                raise SystemExit("!! chapter %s: config says %r, page says %r" % (n, w, g))
        raise SystemExit("!! chapter %s: %d sections in config, %d on page"
                         % (n, len(want), len(got)))

    rail = ['<nav class="rail" aria-label="Sections of this page">'
            '<p class="rail-h">On this page</p><ol>']
    toc = ['<details class="toc"><summary>Contents</summary><ol>']
    for sid, num, lab in ([("intro", "", "Introduction")] + c['sec']
                          + TAIL + c.get('tail_extra', [])):
        rail.append('<li><a href="#%s"><span class="rn">%s</span>%s</a></li>' % (sid, num, lab))
        toc.append('<li><a href="#%s">%s</a></li>' % (sid, lab))
    rail.append('</ol></nav>')
    toc.append('</ol></details>')

    style = open(G + 'style.css', encoding='utf-8').read()
    if '--band:#96591A;' not in style:
        raise SystemExit("!! part colour token missing from style.css")
    if '--moss:%s;' % PART_I not in style:
        raise SystemExit("!! --moss:%s missing from style.css" % PART_I)
    h = h.replace('{{STYLE}}', style.replace('--band:#96591A;', '--band:%s;' % PART_I))
    h = h.replace('{{RAIL}}', "\n".join(rail)).replace('{{TOC}}', "\n".join(toc))
    h = h.replace('{{JS}}', '<script>' + open(G + 'rail.js', encoding='utf-8').read() + '</script>')
    for k, f in c['svgs'].items():
        try:
            svg = open(G + f, encoding='utf-8').read()
        except IOError:
            if not stub:
                raise SystemExit("!! chapter %s: missing figure %s (use --stub to preview)"
                                 % (n, f))
            svg = STUB % f
            stubbed.append(f)
        h = h.replace('{{%s}}' % k, svg)

    w = pagewords(h)
    h = re.sub(r'Era chapter \u00b7 about \d+ minutes',
               'Era chapter \u00b7 about %d minutes' % round(w / 210), h)
    open(OUT + c['name'], 'w', encoding='utf-8').write(h)
    return h, stubbed


BAND = (25, 50)
TARGET = (28, 40)

if __name__ == "__main__":
    stub = "--stub" in sys.argv
    print("--- Part I ---" + ("  [STUBBED FIGURES]" if stub else ""))
    fail = 0
    for n in sorted(CFG):
        c = CFG[n]
        h, stubbed = build(n, c, stub)
        css = h.split('<style>')[1].split('</style>')[0]
        ids = set(re.findall(r'id="([a-z0-9]+)"', h))
        links = set(re.findall(r'href="#([a-z0-9]+)"', h))
        bad = [t for t in ['div', 'ol', 'li', 'ul', 'nav', 'details', 'svg', 'p', 'h2', 'h4',
                           'dl', 'dt', 'dd', 'a', 'figure', 'figcaption', 'text', 'g', 'tspan',
                           'clipPath']
               if h.count('<' + t + ' ') + h.count('<' + t + '>') != h.count('</' + t + '>')]
        w = pagewords(h)
        m = round(w / 210)
        five = len(re.findall(r'<ol class="five">.*?</ol>', h, re.S))
        nfive = len(re.findall(r'<li><p>', re.search(r'<ol class="five">.*?</ol>', h, re.S).group(0))) \
            if five else 0
        rail = re.search(r'<nav class="rail".*?</nav>', h, re.S).group(0)
        toc = re.search(r'<details class="toc">.*?</details>', h, re.S).group(0)
        tail_ok = all(('#%s' % t[0]) in rail and ('#%s' % t[0]) in toc
                      for t in TAIL + c.get('tail_extra', []))
        print("\nchapter %s  %s" % (n, c['name']))
        print("  braces %d | placeholders %d | anchors %s | tags %s"
              % (css.count('{') - css.count('}'), h.count('{{'),
                 'ok' if links <= ids else 'BAD ' + str(links - ids), bad if bad else 'ok'))
        print("  checkpoints %d | vignettes %d | meanwhile %d | figures %d | terms %d | "
              "tail in rail+toc %s"
              % (h.count('class="check"'), h.count('class="vig"'), h.count('class="meanwhile"'),
                 h.count('<figure>'), h.count('class="terms"'), 'ok' if tail_ok else 'BAD'))
        band = 'ok' if BAND[0] <= m <= BAND[1] else 'OUTSIDE BAND'
        note = '' if TARGET[0] <= m <= TARGET[1] else '  <-- note'
        if nfive != 5:
            print("  !! SUMMARY IS %d ITEM%s, NOT FIVE \u2014 the heading promises five"
                  % (nfive, "" if nfive == 1 else "S"))
        print("  part %s | words %d (~%d min, %s)%s"
              % ('ok' if '--band:%s;' % PART_I in h else 'BAD', w, m, band, note))
        for mm in re.finditer(r'<div class="check">.*?</div>\s*<h2 id="(s\d\d)">(.*?)</h2>',
                              h, re.S):
            print("  checkpoint before %s  %s"
                  % (mm.group(1), re.sub(r'<[^>]+>', '', mm.group(2)).strip()))
        if stubbed:
            print("  !! STUBBED: %s" % ", ".join(stubbed))
        fail += (bool(bad) or h.count('{{') or not (links <= ids) or not tail_ok
                 or not (BAND[0] <= m <= BAND[1]) or bool(stubbed) or nfive != 5)
    sys.exit(1 if fail else 0)
