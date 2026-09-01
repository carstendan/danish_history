# -*- coding: utf-8 -*-
"""Build Part F. Same shape as build_part_e.py: per-chapter configs, one command,
self-verifying.

Checkpoints live here, keyed to section TITLE fragments rather than ids, so that
renaming a section breaks the build loudly instead of silently moving a
checkpoint somewhere else (lesson 10). Any checkpoint already sitting in the body
is stripped first, so the body and this file cannot disagree.

Chapter numbers are those settled by the renumbering of August 2026: Part F is
21-24. Chapter 24 will carry the part coda via tail_extra, as chapter 20 does for
Part E; nothing in this part carries one yet.

    python3 build_part_f.py            # strict: every figure must exist
    python3 build_part_f.py --stub     # missing figures become a loud placeholder

--stub exits non-zero even when everything else passes, so a stubbed page cannot
be mistaken for a finished one.
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
PART_F = '#8A2B2B'          # --oxblood; D and E are both teal, F has to move away

# Chapter 24 closes the part and carries a coda after the standard tail, as
# chapter 20 does for Part E.
CODA = ("coda", "", "What this part was about")

TAIL = [("myth", "", "Myth-check"), ("forward", "", "What to carry forward"),
        ("summary", "", "The page in five"), ("questions", "", "Questions &amp; discussion"),
        ("sources", "", "Sources"), ("visit", "", "Places you can visit")]

STUB = ('<svg viewBox="0 0 700 120" xmlns="http://www.w3.org/2000/svg" role="img" '
        'aria-label="Placeholder: this figure has not been drawn yet.">'
        '<rect x="1" y="1" width="698" height="118" fill="none" stroke="#8A2B2B" '
        'stroke-width="1.5" stroke-dasharray="7 5"/>'
        '<text x="350" y="58" text-anchor="middle" font-family="monospace" font-size="13" '
        'fill="#8A2B2B">FIGURE NOT YET DRAWN</text>'
        '<text x="350" y="78" text-anchor="middle" font-family="monospace" font-size="10" '
        'fill="#5F6157">%s</text></svg>')

CFG = {
 21: dict(
    name='21-the-lutheran-realm-of-the-nobility.html',
    body='c21_body.html',
    svgs={'SVG_TERR1600': 'svg_terr_1600.txt',
          'SVG_PARTITION': 'svg_partition.txt',
          'SVG_TOLLGAME': 'svg_tollgame.txt'},
    sec=[("s01", "01", "What the winner owed"),
         ("s02", "02", "The church the crown built"),
         ("s03", "03", "The edges: Norway, Iceland, the Faroes"),
         ("s04", "04", "Three brothers, one duchy"),
         ("s05", "05", "The land, the lord and the grain"),
         ("s06", "06", "Peder Oxe and the price of a passing ship"),
         ("s07", "07", "The Northern Seven Years' War, 1563\u201370"),
         ("s08", "08", "Kronborg, Hven, and what the toll built"),
         ("s09", "09", "What Christian 4. inherited")],
    checks=[
      ("The edges", [
        "The crown came out of 1536 holding about half the land of Denmark. Name three "
        "reasons that did not translate into three times the income.",
        "What did the charter of 30 October 1536 forbid the king to do without the council's "
        "consent \u2014 four things?",
        "Bugenhagen was not a bishop. Why did Christian 3. have him perform the coronation "
        "anyway, and what did he do a fortnight later?"]),
      ("Peder Oxe", [
        "Norway kept three things after the recess of 1536 said it was no longer a kingdom. "
        "What were they?",
        "Why were three men beheaded at Sk\u00e1lholt in November 1550 without a trial \u2014 and "
        "what does the reason tell you about how Iceland was governed?",
        "The duchies were divided in 1544 without dividing the territory. How, and who chose "
        "first?"]),
      ("Kronborg, Hven", [
        "What is <i class=\"dk\">hoveri</i>, and why did the European grain price make it "
        "worse rather than better for the man performing it?",
        "What was the Sound toll before 1567, what did it become, and what stopped a skipper "
        "from understating his cargo?",
        "Denmark and Sweden fought for seven years. Name the two real questions underneath "
        "the quarrel about coats of arms."]),
    ]),
 22: dict(
    name='22-christian-4-ambition-and-the-building-years.html',
    body='c22_body.html',
    svgs={'SVG_FOUNDATIONS': 'svg_foundations.txt',
          'SVG_KOEGECHAIN': 'svg_koegechain.txt',
          'SVG_LEDGER': 'svg_ledger.txt'},
    sec=[("s01", "01", "The boy, his mother, and the charter"),
         ("s02", "02", "The king in his own hand"),
         ("s03", "03", "Building as policy"),
         ("s04", "04", "Towns made by decree"),
         ("s05", "05", "Norway governed hard"),
         ("s06", "06", "The companies and the sea road east"),
         ("s07", "07", "The Kalmar War, 1611\u201313"),
         ("s08", "08", "The devil in K\u00f8ge"),
         ("s09", "09", "What the money was doing")],
    checks=[
      ("Building as policy", [
        "Why was Sophie of Mecklenburg refused a place on the regency council, and what "
        "position did she hold instead from 1590?",
        "What did the accession charter of 1596 add to what earlier kings had conceded?",
        "Roughly how many of Christian 4.'s letters in his own hand survive, and what makes "
        "them an unusual source?"]),
      ("The companies", [
        "Name three of the towns founded between 1599 and 1624, and say what each was meant "
        "to do.",
        "Glückstadt and Christiania were both founded by decree. Why did one work and the "
        "other not?",
        "What was the <i class=\"dk\">Norske Lov</i> of 1604, and why do Danish and Norwegian "
        "historians read it differently?"]),
      ("What the money", [
        "How did Christian 4. make war in 1611 despite a charter forbidding it without the "
        "council's consent?",
        "What did Sweden pay at Kn\u00e4red in 1613, and what did it get back?",
        "What did the ordinance of 1617 do, and what happened to the number of trials "
        "afterwards?"]),
    ]),
 23: dict(
    name='23-christian-4-the-wars-that-broke-him.html',
    body='c23_body.html',
    svgs={'SVG_INVASIONS': 'svg_invasions.txt',
          'SVG_SONSINLAW': 'svg_sonsinlaw.txt',
          'SVG_LOSSES1645': 'svg_losses1645.txt'},
    sec=[("s01", "01", "Why a Danish king went to Germany"),
         ("s02", "02", "Lutter am Barenberge, 27 August 1626"),
         ("s03", "03", "The occupation, 1627\u201329"),
         ("s04", "04", "The Peace of L\u00fcbeck, 1629"),
         ("s05", "05", "Kirsten Munk, Ellen Marsvin, and the sons-in-law"),
         ("s06", "06", "Building on a raised toll"),
         ("s07", "07", "Torstensson's war, 1643\u201345"),
         ("s08", "08", "Hannibal Sehested's Norway"),
         ("s09", "09", "Br\u00f8msebro, 13 August 1645"),
         ("s10", "10", "1648")],
    checks=[
      ("The occupation", [
        "In what capacity did Christian 4. enter the German war in 1625, and why did that let "
        "him ignore the council?",
        "What was he counting on to pay for it, and how much of it arrived?",
        "What did Lutter am Barenberge on 27 August 1626 cost him?"]),
      ("Building on a raised toll", [
        "Why did the Peace of L\u00fcbeck take no territory from Denmark?",
        "Why was Jutland occupied while Zealand and Scania were not touched?",
        "What did Ellen Marsvin do in 1629, and what are the two readings of why?"]),
      ("Br\u00f8msebro", [
        "How did raising the Sound toll in the 1630s contribute to a Dutch fleet fighting "
        "beside Sweden in 1644?",
        "Name the territories ceded at Br\u00f8msebro, and the one clause that carried no "
        "territory at all.",
        "What did the accession charter of 1648 require of Frederik 3.?"]),
    ]),
 24: dict(
    name='24-losing-the-eastern-provinces.html',
    body='c24_body.html',
    svgs={'SVG_ICEMARCH': 'svg_icemarch.txt',
          'SVG_LOST1658': 'svg_lost1658.txt',
          'SVG_COLLAPSE': 'svg_collapse.txt'},
    tail_extra=[CODA],
    sec=[("s01", "01", "Frederik 3. and the hardest charter"),
         ("s02", "02", "The fall of Corfitz Ulfeldt"),
         ("s03", "03", "The war Denmark chose, 1657"),
         ("s04", "04", "The march across the ice"),
         ("s05", "05", "Roskilde, 26 February 1658"),
         ("s06", "06", "The second war, and the siege"),
         ("s07", "07", "Bornholm and Tr\u00f8ndelag"),
         ("s08", "08", "The Dutch in the Sound"),
         ("s09", "09", "The Peace of Copenhagen, 27 May 1660"),
         ("s10", "10", "What was left")],
    checks=[
      ("The war Denmark chose", [
        "What did the accession charter of 1648 leave Frederik 3. able to do on his own?",
        "What did Dina Vinhofvers accuse Corfitz Ulfeldt of, what did the court decide, and "
        "what happened to each of them?",
        "Who was governing Denmark in the first three years of the reign?"]),
      ("The second war", [
        "Why did Denmark declare war in June 1657, and which three facts from chapter 23 had "
        "been left out of the calculation?",
        "Trace the crossing of the belts island by island, and say why the direct route was "
        "not used.",
        "Name the six territories ceded at Roskilde on 26 February 1658."]),
      ("What was left", [
        "Why did Karl Gustav's second attack bring the Dutch in, and what did they insist on?",
        "How did Bornholm come back to Denmark, and on what condition?",
        "What did the burghers argue in September 1660, and why could the nobility not answer "
        "it?"]),
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
    h = h.replace('{{STYLE}}', style.replace('--band:#96591A;', '--band:%s;' % PART_F))
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
TARGET = (30, 42)

if __name__ == "__main__":
    stub = "--stub" in sys.argv
    print("--- Part F ---" + ("  [STUBBED FIGURES]" if stub else ""))
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
              % ('ok' if '--band:%s;' % PART_F in h else 'BAD', w, m, band, note))
        for mm in re.finditer(r'<div class="check">.*?</div>\s*<h2 id="(s\d\d)">(.*?)</h2>',
                              h, re.S):
            print("  checkpoint before %s  %s"
                  % (mm.group(1), re.sub(r'<[^>]+>', '', mm.group(2)).strip()))
        if stubbed:
            print("  !! STUBBED: %s" % ", ".join(stubbed))
        fail += (bool(bad) or h.count('{{') or not (links <= ids) or not tail_ok
                 or not (BAND[0] <= m <= BAND[1]) or bool(stubbed))
    sys.exit(1 if fail else 0)
