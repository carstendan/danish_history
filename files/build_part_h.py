# -*- coding: utf-8 -*-
"""Build Part H. Same shape as build_part_g.py: per-chapter configs, one command,
self-verifying.

Checkpoints live here, keyed to section TITLE fragments rather than ids, so that
renaming a section breaks the build loudly instead of silently moving a checkpoint
somewhere else (lesson L10). Any checkpoint already sitting in the body is stripped
first, so the body and this file cannot disagree.

Part H is chapters 32-36, 1814-1901. Only chapter 32 is configured; 33 to 36 are
drafted but not written, and a config entry for a chapter with no body would fail
loudly on the first run, which is the intended behaviour and not a bug to route
around. Chapter 36 will carry the part coda via tail_extra, as 31 does for G.

THE BAND COLOUR IS NEW. D and E are verdigris, F oxblood, G indigo; H is slate,
added to style.css as --slate for this part. Adding a token to the stylesheet is
precedented - --indigo went in for Part G - and `debuild.py` already handles the
consequence, which is that every page shipped before the token existed
reconstructs with a token it never had. Verify after building: 01-11 should stay
`style-only` and 12-31 `identical`. If 12-31 move to `style-only`, the drop list
in debuild.py has not picked the new token up and that must be fixed before
anything ships.

CHECKPOINTS ARE QUESTIONS, NOT PROSE. The chapter 32 draft writes its three
checkpoints as prose recaps - "where we are". Every part from A to G uses three
retrieval questions instead, and the .check rule in style.css is written for a
list. The questions below are derived from the draft's prose so they test what it
says is worth holding, but the prose itself is not reproduced. Changing that is a
change to every shipped part, not to Part H alone.

    python3 build_part_h.py            # strict: every figure must exist
    python3 build_part_h.py --stub     # missing figures become a loud placeholder

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
PART_H = '#4F6470'          # --slate; D and E verdigris, F oxblood, G indigo, H again

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
 32: dict(
    name='32-golden-age-and-national-awakening.html',
    body='c32_body.html',
    svgs={'SVG_TERR_1814': 'svg_terr_1814.txt',
          'SVG_ASSEMBLIES': 'svg_assemblies.txt',
          'SVG_RYE': 'svg_rye.txt'},
    sec=[("s01", "01", 'The realm that was left'),
         ("s02", "02", 'Paying for the war'),
         ("s03", "03", 'The awakening in the parishes'),
         ("s04", "04", 'Grundtvig'),
         ("s05", "05", 'What the Golden Age was for'),
         ("s06", "06", 'Four assemblies, 1831\u20131836'),
         ("s07", "07", 'The countryside gets rich'),
         ("s08", "08", 'Bondevennerne'),
         ("s09", "09", 'Two nations in one duchy'),
         ("s10", "10", 'The Open Letter, 1846')],
    checks=[
      ("Grundtvig", [
        "Denmark took Lauenburg in 1815 and gave up a larger province to get it. What did "
        "it give up, and what else came with the exchange?",
        "An absolute monarchy chartered an independent bank in 1818 and wrote that "
        "independence into the charter. What was the bank told to put first?",
        "The gudelige forsamlinger broke a law from 1741. What did that law actually "
        "forbid, and what did the prosecutions produce?"]),
      ("Four assemblies, 1831\u20131836", [
        "Grundtvig spent eleven years having his manuscripts read by a policeman. Who "
        "sentenced him to that, and what does the answer tell you about the state?",
        "Name three of the institutions the Golden Age ran through, and say who paid for "
        "them.",
        "Two prosecutions in this chapter produced the opposite of what they intended. "
        "Which two, and what did the state get instead?"]),
      ("Two nations in one duchy", [
        "About one Dane in forty could vote for the assemblies. Why is that figure "
        "surprising, and who could not vote whatever they owned?",
        "The Bondecirkul\u00e6re of November 1845 was meant to keep peasants out of politics. "
        "What did it do instead, and how long did that take?",
        "The assemblies were designed to keep the political argument dispersed. Where did "
        "the argument break out, and how many years after they were set up?"]),
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
    if '--slate:%s;' % PART_H not in style:
        raise SystemExit("!! --slate:%s missing from style.css" % PART_H)
    h = h.replace('{{STYLE}}', style.replace('--band:#96591A;', '--band:%s;' % PART_H))
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
    print("--- Part H ---" + ("  [STUBBED FIGURES]" if stub else ""))
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
        print("  part %s | words %d (~%d min, %s)%s"
              % ('ok' if '--band:%s;' % PART_H in h else 'BAD', w, m, band, note))
        for mm in re.finditer(r'<div class="check">.*?</div>\s*<h2 id="(s\d\d)">(.*?)</h2>',
                              h, re.S):
            print("  checkpoint before %s  %s"
                  % (mm.group(1), re.sub(r'<[^>]+>', '', mm.group(2)).strip()))
        if stubbed:
            print("  !! STUBBED: %s" % ", ".join(stubbed))
        fail += (bool(bad) or h.count('{{') or not (links <= ids) or not tail_ok
                 or not (BAND[0] <= m <= BAND[1]) or bool(stubbed))
    sys.exit(1 if fail else 0)
