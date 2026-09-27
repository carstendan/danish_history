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
                                       # (needs DK_OUT outside the repository)

--stub exits non-zero even when everything else passes, so a stubbed page cannot
be mistaken for a finished one.

GUARDS, given to Part F in review session 12 (REVIEW-CONSISTENCY.md §16) from
pageguard.py, which Parts G-I share. Until then this script wrote each page inside
build() and read its text as a regular expression does. Each is asked BEFORE the page is
written, and a page that fails any of them, or any structural check, is not written:

  1. pageguard.same_sources: what this build reads through DK_SRC (the body, style.css,
     rail.js) is the file in this folder. (No freshcheck: authored bodies, not drafts.)
  2. pageguard.figures_fresh: every figure is what its script writes, run in a scratch copy.
  3. pageguard.stale_vocabulary on reader_text, with ALLOWED_ENTRY found by hand.
  4. pageguard.asked_twice (D-17).
"""
import os
import re
import sys

from pagewords import pagewords   # one definition, shared
import dkpaths
import pageguard    # body witness, figure freshness, reader's-text vocabulary, ask once

# Paths resolve relative to this script, not to wherever it is run from, and both
# can be overridden. The container paths that used to be hardcoded here meant the
# script only ran in one place; sources live beside it in files/ and built pages
# go to the parent, which is the layout on disk.
HERE = os.path.dirname(os.path.abspath(__file__))
G = dkpaths.resolve('DK_SRC', HERE, 'the folder holding the bodies and figures') + os.sep
OUT = dkpaths.resolve('DK_OUT', os.path.dirname(HERE), 'where built chapter pages are written') + os.sep
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
        "Whom did Christian 3. owe money to when Copenhagen surrendered in July 1536, and who "
        "had lent him part of the fleet that closed the Sound?",
        "What did the charter of 30 October 1536 forbid the king to do without the council's "
        "consent \u2014 four things?",
        "Bugenhagen was not a bishop. Why did Christian 3. have him perform the coronation "
        "anyway, and what did he do three weeks later?"]),
      ("Peder Oxe", [
        "Norway kept three things after Christian 3.'s charter of 1536 said it was no longer a kingdom. "
        "What were they?",
        "The Faroes went Lutheran in 1540 without recorded resistance. What lasting consequence "
        "did that have for the Faroese language?",
        "Of the three who shared the duchies in 1544, which chose first, why him, and what is his "
        "line called ever after?"]),
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
         ("s08", "08", "Witchcraft and the state"),
         ("s09", "09", "What the money was doing")],
    checks=[
      ("Building as policy", [
        "Sophie of Mecklenburg was kept off the regency council. What position did she hold "
        "instead from 1590, and what ended it?",
        "Where did Sophie of Mecklenburg withdraw to in 1594, and what did she hold as her dower?",
        "Roughly how many of Christian 4.'s letters in his own hand survive, and what makes "
        "them an unusual source?"]),
      ("The companies", [
        "Name three of the towns founded between 1599 and 1624, and say what each was meant "
        "to do.",
        "What was found at Kongsberg in 1623, and how did Christian 4. make sure it flowed to "
        "the crown?",
        "What was the <i class=\"dk\">Norske Lov</i> of 1604, and why do Danish and Norwegian "
        "historians read it differently?"]),
      ("What the money", [
        "How did Christian 4. get his war in 1611 despite a charter forbidding it without the "
        "council's consent?",
        "What did Sweden pay at Kn\u00e4red in 1613, and what did it get back?",
        "How many of Jens Munk's sixty-four men were alive at the Churchill River in June 1620, "
        "and what had killed the rest?"]),
    ]),
 23: dict(
    name='23-christian-4-the-wars-that-broke-him.html',
    body='c23_body.html',
    svgs={'SVG_INVASIONS': 'svg_invasions.txt',
          'SVG_SONSINLAW': 'svg_sonsinlaw.txt',
          'SVG_LOSSES1645': 'svg_losses1645.txt'},
    sec=[("s01", "01", "Why a Danish king went to Germany"),
         ("s02", "02", "Lutter am Barenberge, 17 August 1626"),
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
        "What did Lutter am Barenberge on 17 August 1626 cost him?"]),
      ("Building on a raised toll", [
        "Which of Christian 4.'s own foundations held out through the occupation, and why was "
        "that a surprise?",
        "Why was Jutland occupied while Zealand and Funen were not touched?",
        "What did Ellen Marsvin do in 1629, and what are the two readings of why?"]),
      ("Br\u00f8msebro", [
        "How did raising the Sound toll in the 1630s help Sweden hire a fleet in the "
        "Netherlands in 1644?",
        "How did Torstensson's war begin in December 1643, and what were his orders?",
        "Besides raising the toll, how did Christian 4. pay his way in the 1630s? Name three "
        "means."]),
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
        "What kind of man was Frederik 3., what had he been raised for, and what did most people "
        "in Copenhagen mistake his manner for?",
        "What did Dina Vinhofvers accuse Corfitz Ulfeldt of, what did the court decide, and "
        "what happened to each of them?",
        "Who was governing Denmark in the first three years of the reign?"]),
      ("The second war", [
        "What was Frederiksodde, and where did its fall on 24 October 1657 leave the Swedish "
        "army?",
        "Besides territory, what did Denmark undertake at Roskilde? Name three things.",
        "Name the six territories ceded at Roskilde on 26 February 1658."]),
      ("What was left", [
        "What happened in the Sound on 29 October 1658, and what did it mean for the siege of "
        "Copenhagen?",
        "How did Bornholm come back to Denmark, and on what condition?",
        "Who got Ulfeldt and Leonora Christina out of Swedish arrest at Malmö, and where "
        "were they held once back in Denmark?"]),
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
                raise SystemExit("!! chapter %s: missing figure %s (use --stub with DK_OUT outside the repository to preview)"
                                 % (n, f))
            svg = STUB % f
            stubbed.append(f)
        h = h.replace('{{%s}}' % k, svg)

    w = pagewords(h)
    h = re.sub(r'Era chapter \u00b7 about \d+ minutes',
               'Era chapter \u00b7 about %d minutes' % round(w / 210), h)
    return h, stubbed


BAND = (25, 50)
TARGET = (28, 40)
# "entry" in its ordinary sense: Munk's journal (22) and a ledger (23). Found by the old
# guard's first run in review session 8 (\u00a712.6), after a grep had said there were none, and
# found again by hand in review session 12 (built pages 21-24, text, figure text and
# attributes, whitespace joined, case ignored): these four and no others. Each phrase is
# removed once, exactly as the reader's text has it; one no longer on the page is reported.
ALLOWED_ENTRY = {22: ['the entries thin out', 'daily entries are the source'],
                 23: ['small entry in that ledger', 'small entry in a much']}

if __name__ == "__main__":
    stub = "--stub" in sys.argv
    # A stubbed page is a preview. It must never land where the shipped pages are: with
    # DK_OUT unset, --stub overwrote page 22 in the repository with a placeholder figure
    # (review session 12, check 2).
    repo = os.path.realpath(os.path.dirname(HERE))
    if stub and (os.path.realpath(OUT) + os.sep).startswith(repo + os.sep):
        raise SystemExit("!! --stub writes preview pages: set DK_OUT to a folder outside "
                         "the repository")
    print("--- Part F ---" + ("  [STUBBED FIGURES]" if stub else ""))
    fail = 0
    # EVERY FIGURE MUST BE WHAT ITS SCRIPT WRITES, witnessed by running the script in a
    # scratch copy (pageguard, review session 12, \u00a716). All twelve are scripted, so a
    # figure reported SOURCELESS fails as well.
    figs, nfigs = pageguard.figures_fresh(
        HERE, G, sorted({f for c in CFG.values() for f in c['svgs'].values()}))
    print("  figures: %d checked against their scripts, %s"
          % (nfigs, 'all fresh' if not figs else '%d NOT' % len(figs)))
    for n in sorted(CFG):
        c = CFG[n]
        # No freshcheck: Parts A-F have authored bodies, not drafts. What this build reads
        # through DK_SRC - the body, style.css, rail.js - must be the file in this folder.
        if not os.path.exists(G + c['body']):
            print("\nchapter %s  %s\n  !! NOT BUILT: no body %s in %s"
                  % (n, c['name'], c['body'], G))
            fail += 1
            continue
        differ = pageguard.same_sources(G, HERE, [c['body'], 'style.css', 'rail.js'])
        if differ:
            print("\nchapter %s  %s\n  !! NOT BUILT: %s missing from %s or %s, or the two copies differ (DK_SRC)." % (n, c['name'], ', '.join(differ), G, HERE))
            fail += 1
            continue
        # Under --stub a figure that is not on disk yet is left to the stub (a preview; the
        # run still fails). Without this, figures_fresh reported it STALE and --stub could
        # never stub (review session 12, check 1).
        stalefigs = {f: v for f, v in figs.items() if f in c['svgs'].values()
                     and not (stub and not os.path.exists(G + f))}
        if stalefigs:
            print("\nchapter %s  %s\n  !! NOT BUILT: figures not what their scripts write: %s"
                  % (n, c['name'], '; '.join('%s %s' % (k, 'MISSING (use --stub with DK_OUT outside the repository to preview)'
                                                if 'Errno 2' in v else v)
                                for k, v in sorted(stalefigs.items()))))
            fail += 1
            continue
        h, stubbed = build(n, c, stub)
        # Retired vocabulary in the reader's text (pageguard.reader_text), and D-17.
        stale = pageguard.stale_vocabulary(h, ALLOWED_ENTRY.get(n, []))
        if stale:
            print("\nchapter %s  %s\n  !! NOT WRITTEN: retired vocabulary %s"
                  % (n, c['name'], stale))
            fail += 1
            continue
        twice = pageguard.asked_twice(h)
        if twice:
            print("\nchapter %s  %s\n  !! NOT WRITTEN: a question asked twice (D-17): %s"
                  % (n, c['name'], '; '.join('%s = %s (%.2f)' % t for t in twice)))
            fail += 1
            continue
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
        # Every structural check below is asked before the page is written too. A stubbed
        # page is the one exception: --stub exists to preview a page with a placeholder,
        # so it is written, and the run still fails.
        page_fail = (bool(bad) + bool(h.count('{{')) + (not links <= ids) + (not tail_ok)
                     + (not BAND[0] <= m <= BAND[1]) + ('--band:%s;' % PART_F not in h))
        if not page_fail:
            open(OUT + c['name'], 'w', encoding='utf-8').write(h)
        print("\nchapter %s  %s%s" % (n, c['name'], '' if not page_fail else '  !! NOT WRITTEN'))
        print("  braces %d | placeholders %d | anchors %s | tags %s"
              % (css.count('{') - css.count('}'), h.count('{{'),
                 'ok' if links <= ids else 'BAD ' + str(links - ids), bad if bad else 'ok'))
        print("  checkpoints %d | vignettes %d | meanwhile %d | figures %d | terms %d | "
              "tail in rail+toc %s"
              % (h.count('class="check"'), h.count('class="vig"'), h.count('class="meanwhile"'),
                 h.count('<figure>'), h.count('class="terms"'), 'ok' if tail_ok else 'BAD'))
        band = 'ok' if BAND[0] <= m <= BAND[1] else 'OUTSIDE BAND'
        note = '' if TARGET[0] <= m <= TARGET[1] else '  <-- note'
        print("  part %s | vocabulary clean | questions asked once | words %d (~%d min, %s)%s"
              % ('ok' if '--band:%s;' % PART_F in h else 'BAD', w, m, band, note))
        for mm in re.finditer(r'<div class="check">.*?</div>\s*<h2 id="(s\d\d)">(.*?)</h2>',
                              h, re.S):
            print("  checkpoint before %s  %s"
                  % (mm.group(1), re.sub(r'<[^>]+>', '', mm.group(2)).strip()))
        if stubbed:
            print("  !! STUBBED: %s" % ", ".join(stubbed))
        fail += page_fail + bool(stubbed)
    print("\n%s" % ('all four built clean' if not fail else '!! %d problems' % fail))
    sys.exit(1 if fail else 0)
