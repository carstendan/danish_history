# -*- coding: utf-8 -*-
"""Build Part H. Same shape as build_part_g.py: per-chapter configs, one command,
self-verifying.

Checkpoints live here, keyed to section TITLE fragments rather than ids, so that
renaming a section breaks the build loudly instead of silently moving a checkpoint
somewhere else (lesson L10). Any checkpoint already sitting in the body is stripped
first, so the body and this file cannot disagree.

Part H is chapters 32-36, 1814-1901, all five configured and built from
`c32_draft.md` ... `c36_draft.md` through mkbody.py. Chapter 36 carries the part
coda, which mkbody places in the body.

GUARDS, given to Part H in review session 10 (REVIEW-CONSISTENCY.md §14.6). Until
then this script had no vocabulary check at all, and no summary line. Each is asked
BEFORE the page is written, and a page that fails any of them is not written:

  1. freshcheck.check(n): the body on disk is what the draft builds. If not
     (mkbody refused, or nobody ran it), NOT BUILT.
  2. pageguard.same_body: the body this build reads (DK_SRC) is the body
     freshcheck checked. With DK_SRC at an old copy, an old body shipped "clean".
  3. pageguard.figures_fresh: every figure is what its script writes, run in a
     scratch copy. A hand-restored svg_*.txt shipped "clean".
  4. pageguard.stale_vocabulary: retired vocabulary in the reader's text of the
     page - every tag a space, attributes a reader or screen reader gets (any
     case, any quoting), entities decoded, NFKC, invisible characters removed,
     look-alike letters folded, dashes folded. Otherwise NOT WRITTEN.

Part G got 1 in session 9 (§13.6) and 2-4 in session 10, from the same module.

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
import html
import os
import re
import sys

from pagewords import pagewords   # one definition, shared
import dkpaths
import freshcheck   # the body-against-draft comparison, run before every page
import pageguard    # body witness, figure freshness, reader's-text vocabulary (§14.6)

# Paths resolve relative to this script, not to wherever it is run from, and both
# can be overridden. The container paths that used to be hardcoded here meant the
# script only ran in one place; sources live beside it in files/ and built pages
# go to the parent, which is the layout on disk.
HERE = os.path.dirname(os.path.abspath(__file__))
G = dkpaths.resolve('DK_SRC', HERE, 'the folder holding the bodies and figures') + os.sep
OUT = dkpaths.resolve('DK_OUT', os.path.dirname(HERE), 'where built chapter pages are written') + os.sep
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
        "How many of Grundtvig's writings did the censorship actually suppress, and what "
        "did it cost him instead?"]),
      ("Two nations in one duchy", [
        "In the kingdom just under three people in a hundred could vote for the assemblies. "
        "Who could not vote whatever they owned, and who could vote there but not be elected?",
        "The Bondecirkul\u00e6re of November 1845 was meant to keep peasants out of politics. "
        "What did it do instead, and how long did that take?",
        "The assemblies were designed to keep the political argument dispersed. Where did "
        "the argument break out, and in what year?"]),
    ]),

 33: dict(
    name='33-1848-constitution-and-the-first-schleswig-war.html',
    body='c33_body.html',
    svgs={'SVG_DESCENT': 'svg_descent_1848.txt',
          'SVG_SPROG': 'svg_sprog_1839.txt',
          'SVG_FRANCHISE': 'svg_franchise_1849.txt'},
    sec=[("s01", "01", 'A king with no heir'),
         ("s02", "02", 'What Schleswig legally was'),
         ("s03", "03", 'March 1848'),
         ("s04", "04", 'The war begins'),
         ("s05", "05", "The soldier's war"),
         ("s06", "06", '5 June 1849'),
         ("s07", "07", 'A church for the people'),
         ("s08", "08", 'Isted, 25 July 1850'),
         ("s09", "09", 'London, 8 May 1852'),
         ("s10", "10", 'What the constitution could not cover')],
    checks=[
      ("The war begins", [
        "Christian 8. asked his successor for three things on 9 January 1848. What were "
        "they, and which one was never done?",
        "The rescript of 28 January offered kingdom and duchies equal representation. Why "
        "did that satisfy neither side?",
        "Put these in order: the Casino meeting, the fall of the ministry, the provisional "
        "government at Kiel, the seizure of Rendsburg."]),
      ("5 June 1849", [
        "Prussian and Schleswig-Holstein troops crossed into Jutland in May 1848 and were "
        "taken back. Who made Prussia withdraw, and what was that power's interest?",
        "Before 1849 conscription fell on one class only. Which, and how had everybody else "
        "got out of it?",
        "The Law on Universal Conscription of 12 February 1849 drew its line by birth year. "
        "Which year, and what did that leave untouched until 1867?"]),
      ("London, 8 May 1852", [
        "Fifteen per cent of the population could vote in 1849 and all of it could worship "
        "as it chose. How can both be true of one document?",
        "What did the constitution say about Schleswig on its first page, and where did it "
        "never come into force?",
        "Isted was the largest battle in Danish history and Denmark won it. What did the "
        "victory settle?"]),
    ]),

 34: dict(
    name='34-1864.html',
    body='c34_body.html',
    svgs={'SVG_TERR_1864': 'svg_terr_1864.txt',
          'SVG_DYBBOL': 'svg_dybbol_1864.txt',
          'SVG_CEDED': 'svg_ceded_1864.txt'},
    sec=[("s01", "01", 'A king three days on the throne'),
         ("s02", "02", 'Why the powers did not come'),
         ("s03", "03", 'Dannevirke, 5\u20136 February'),
         ("s04", "04", 'Dybb\u00f8l'),
         ("s05", "05", 'The London Conference'),
         ("s06", "06", 'Als, and Jutland occupied'),
         ("s07", "07", 'Vienna, 30 October'),
         ("s08", "08", 'What was ceded, and who'),
         ("s09", "09", 'The constitution of 1866'),
         ("s10", "10", 'What was to be won inward')],
    checks=[
      ("Dybb\u00f8l", [
        "Christian 9. had been king for three days when he signed. What did the signature "
        "break, and why was he the worst-placed man in Denmark to sign it?",
        "Prussia and Austria crossed the Eider on 1 February 1864 without the German "
        "Confederation. Why did they have to step outside it?",
        "The War Ministry's instruction of 13 January told de Meza what mattered most. "
        "What was it, and what did the war minister telegraph him on 6 February?"]),
      ("Vienna, 30 October", [
        "Dybb\u00f8l is remembered as a storm. What had already happened to the redoubts "
        "before a single Prussian went forward?",
        "Denmark won the fleet action off Heligoland on 9 May. Why did it change "
        "nothing?",
        "At the London conference the neutral powers proposed arbitration and Denmark refused. What "
        "was the reasoning, and what did it cost?"]),
      ("The constitution of 1866", [
        "To whom did the king renounce the duchies at Vienna \u2014 and what did the "
        "Augustenborg claimant, whose right was the pretext, actually receive?",
        "What was an optant, and what did the Treaty of Vienna allow the people of the "
        "ceded duchies to choose?",
        "Article 5 of the Peace of Prague promised a vote in North Schleswig. Who made the "
        "promise, who cancelled it, and in what year?"]),
    ]),

 35: dict(
    name='35-industry-cooperatives-emigration-and-labour.html',
    body='c35_body.html',
    svgs={'SVG_OMLAEGNING': 'svg_omlaegning_1875.txt',
          'SVG_UDVANDRING': 'svg_udvandring_1868.txt',
          'SVG_ANDEL': 'svg_andel_1882.txt'},
    sec=[("s01", "01", 'Two chapters over one span'),
         ("s02", "02", 'The grain that stopped paying'),
         ("s03", "03", 'The cooperative dairy'),
         ("s04", "04", 'Butter, bacon and the English breakfast'),
         ("s05", "05", 'Mission and meeting-house'),
         ("s06", "06", 'Leaving'),
         ("s07", "07", 'The city outside the walls'),
         ("s08", "08", 'F\u00e6lleden, 5 May 1872'),
         ("s09", "09", '1899'),
         ("s10", "10", 'North Schleswig under Prussia')],
    checks=[
      ("Mission and meeting-house", [
        "Grain stopped paying from about 1875. What did Danish farms start doing with "
        "grain instead of selling it, and where did the grain come from?",
        "Two things outside Denmark's control set the timing of the change. What were "
        "they, and which year did the second one happen?",
        "What did every member of the Hjedding dairy promise to deliver, and which clause "
        "made the bank willing to lend to farmers with no capital?"]),
      ("F\u00e6lleden, 5 May 1872", [
        "Indre Mission and the Grundtvigians came out of the same revival. What did each "
        "build in a village, and what decided which one took hold?",
        "More than four in ten Danish emigrants between 1868 and 1900 had the same "
        "occupation. Which, and why does that matter for the previous three sections?",
        "Why does Denmark have unusually complete records of who emigrated?"]),
      ("North Schleswig under Prussia", [
        "The meeting on N\u00f8rre F\u00e6lled was called for a reason that had nothing to "
        "do with revolution. What was it?",
        "The lockout of 1899 ended without either side winning. What did they sign "
        "instead, and what is left of it?",
        "What did the September Compromise concede to the employers, and what did it "
        "concede to the unions?"]),
    ]),

 36: dict(
    name='36-provisorietiden-and-the-change-of-system.html',
    body='c36_body.html',
    svgs={'SVG_FRANCHISES': 'svg_franchises_1866.txt',
          'SVG_DEADLOCK': 'svg_deadlock_1873.txt',
          'SVG_VESTVOLD': 'svg_vestvold_1888.txt'},
    sec=[("s01", "01", 'Two chambers, two countries'),
         ("s02", "02", 'The question nobody had answered'),
         ("s03", "03", 'Estrup'),
         ("s04", "04", 'Ruling without a budget, 1885'),
         ("s05", "05", 'The gendarmes'),
         ("s06", "06", 'A wall around Copenhagen'),
         ("s07", "07", '21 October 1885'),
         ("s08", "08", 'The other opposition'),
         ("s09", "09", 'The settlement of 1894'),
         ("s10", "10", '1901')],
    # The Part H coda is on the page (mkbody writes it, id="coda") and was missing from
    # the rail and the contents until review session 10; 20, 24 and 31 list theirs.
    tail_extra=[CODA],
    checks=[
      ("Ruling without a budget, 1885", [
        "The 1866 revision left two chambers returning two different countries. Which was "
        "which, and what did Venstre demand from 1873?",
        "What did \u00a725 of the constitution (in 1849, \u00a730) allow, and how often "
        "had it been used for a finance law before 1877?",
        "What was the visnepolitik meant to achieve, and what did it achieve instead?"]),
      ("21 October 1885", [
        "On 31 March and 1 April 1885 two things happened in sequence. What were they?",
        "The Folketing rejected the provisional finance law in January 1886. What "
        "followed from the rejection?",
        "Name three of the provisional laws of 1885 that were not finance laws, and say "
        "what each was for."]),
      ("1901", [
        "What was the Vestvold, when was it built, and what eventually became of it?",
        "Why did the attempt on Estrup's life strengthen his position?",
        "The settlement of 1894 ended the provisional laws. What did it leave "
        "unanswered?"]),
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
    # Not written here: __main__ writes the page only after its guards pass (\u00a714.6).
    return h, stubbed


BAND = (25, 50)
TARGET = (28, 40)
# Part H's ordinary uses of "entry": none. Found by hand in review session 10 (§14.6) on
# the built pages, markup, figure text and attributes included, whitespace joined, case
# ignored: the only matches were the JavaScript's `entries` (the script is not read).
# The pages as they stood before the session had one, 35's Visit "Free entry", which the
# reading pass rephrased. An allowed phrase goes here, per chapter, as in build_part_g.py;
# one that is no longer on the page is itself reported.
ALLOWED_ENTRY = {}


def stale_vocabulary(n, h):
    """Retired vocabulary in the reader's text of the page (pageguard.py, §14.6)."""
    return pageguard.stale_vocabulary(h, ALLOWED_ENTRY.get(n, []))


if __name__ == "__main__":
    stub = "--stub" in sys.argv
    print("--- Part H ---" + ("  [STUBBED FIGURES]" if stub else ""))
    fail = 0
    # EVERY FIGURE MUST BE WHAT ITS SCRIPT WRITES, witnessed by running the script in a
    # scratch copy, not by trusting the svg_*.txt on disk (§14.6).
    figs, nfigs = pageguard.figures_fresh(
        HERE, G, sorted({f for c in CFG.values() for f in c['svgs'].values()}))
    print("  figures: %d checked against their scripts, %s"
          % (nfigs, 'all fresh' if not figs else '%d NOT' % len(figs)))
    for n in sorted(CFG):
        c = CFG[n]
        # THE BODY MUST BE WHAT THE DRAFT BUILDS, asked BEFORE the page is written, as
        # build_part_g.py has asked since review session 9 (§13.6).
        fresh = freshcheck.check(n)
        if fresh[0] != 'FRESH':
            print("\nchapter %s  %s\n  !! NOT BUILT: the body is %s against its draft (%s). "
                  "Run DK_DRAFT=c%s_draft.md python3 mkbody.py %s and read what it says."
                  % (n, c['name'], fresh[0], fresh[1], n, n))
            fail += 1
            continue
        # AND THE BODY THIS BUILD READS MUST BE THE ONE FRESHCHECK READ: with DK_SRC set
        # to an old copy, an old body shipped "clean" (§14.6).
        if not pageguard.same_body(G, HERE, c['body']):
            print("\nchapter %s  %s\n  !! NOT BUILT: %s%s is not the body freshcheck checked "
                  "(%s%s%s). Unset DK_SRC or copy the fresh body there."
                  % (n, c['name'], G, c['body'], HERE, os.sep, c['body']))
            fail += 1
            continue
        stalefigs = {f: v for f, v in figs.items()
                     if f in c['svgs'].values() and v != 'SOURCELESS'}
        if stalefigs:
            print("\nchapter %s  %s\n  !! NOT BUILT: figures not what their scripts write: %s"
                  % (n, c['name'], '; '.join('%s %s' % kv for kv in sorted(stalefigs.items()))))
            fail += 1
            continue
        h, stubbed = build(n, c, stub)
        stale = stale_vocabulary(n, h)
        if stale:
            print("\nchapter %s  %s\n  !! NOT WRITTEN: retired vocabulary %s"
                  % (n, c['name'], stale))
            fail += 1
            continue
        open(OUT + c['name'], 'w', encoding='utf-8').write(h)
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
        print("  part %s | vocabulary %s | words %d (~%d min, %s)%s"
              % ('ok' if '--band:%s;' % PART_H in h else 'BAD',
                 'clean' if not stale else 'STALE ' + str(stale), w, m, band, note))
        for mm in re.finditer(r'<div class="check">.*?</div>\s*<h2 id="(s\d\d)">(.*?)</h2>',
                              h, re.S):
            print("  checkpoint before %s  %s"
                  % (mm.group(1), re.sub(r'<[^>]+>', '', mm.group(2)).strip()))
        if stubbed:
            print("  !! STUBBED: %s" % ", ".join(stubbed))
        fail += (bool(bad) + bool(h.count('{{')) + (not links <= ids) + (not tail_ok)
                 + (not BAND[0] <= m <= BAND[1]) + bool(stubbed) + (nfive != 5)
                 + bool(stale) + ('--band:%s;' % PART_H not in h))
    print("\n%s" % ('all five built clean' if not fail else '!! %d problems' % fail))
    sys.exit(1 if fail else 0)
