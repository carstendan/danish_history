# -*- coding: utf-8 -*-
"""Build Part E. Per-chapter configs, one command, self-verifying - as
build_part_d.py does for Part D and build_parts_abc.py for A to C.

Checkpoints live here, keyed to section TITLE fragments rather than ids, so that
renaming a section breaks the build loudly instead of silently moving a
checkpoint somewhere else (lesson 10). Any checkpoint already sitting in the body
is stripped first, so the body and this file cannot disagree.

GUARDS, given to Part E in review session 12 (REVIEW-CONSISTENCY.md §16) from
pageguard.py, which Parts G-I share. Until then this script wrote each page inside
build() and read its text as a regular expression does. Each is asked BEFORE the page is
written, and a page that fails any of them, or any structural check below, is not written:

  1. pageguard.same_sources: what this build reads through DK_SRC (the body, style.css,
     rail.js) is the file in this folder. (No freshcheck: authored bodies, not drafts.)
  2. pageguard.figures_fresh: every figure is what its script writes, run in a scratch
     copy. All fourteen of Part E's are scripted.
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
PART_E = '#2E6B5E'

TAIL = [("myth", "", "Myth-check"), ("forward", "", "What to carry forward"),
        ("summary", "", "The page in five"), ("questions", "", "Questions &amp; discussion"),
        ("sources", "", "Sources"), ("visit", "", "Places you can visit")]

# A chapter may add its own terminal units after the standard set. Chapter 20
# closes the part, so it carries a coda; nothing else does.
CODA = ("coda", "", "Closing Part E")

# Keys are the chapter numbers. They were '16a'/'16b'/'17'/'18'/'19' until the
# renumbering of August 2026, which folded the two halves of the old chapter 16
# into 16 and 17 and pushed the rest up by one. Integer keys also make sorted()
# order them numerically rather than lexically, which the strings did only by
# accident.
CFG = {
 16: dict(
    name='16-margrete-i-and-the-making-of-the-union.html',
    body='c16_body.html',
    svgs={'SVG_TITLES': 'svg_titles.txt', 'SVG_CROWNS': 'svg_crowns.txt',
          'SVG_TERR1397': 'svg_terr_1397.txt'},
    sec=[("s01", "01", "The succession nobody had settled"),
         ("s02", "02", "A daughter, sent away"),
         ("s03", "03", "Norway, and what came with it"),
         ("s04", "04", "Falsterbo, 3 August 1387"),
         ("s05", "05", "Dalaborg and \u00c5sle"),
         ("s06", "06", "A king in a Sk\u00e5ne castle"),
         ("s07", "07", "Viborg, January 1396"),
         ("s08", "08", "Kalmar, 17 June 1397")],
    checks=[
      ("Falsterbo", [
        "Denmark was a <i class=\"dk\">valgrige</i>. Given that, why did it matter that Margrete "
        "wrote her claim down in December 1375?",
        "What did Oluf's election in 1376 have in common with the charter of 1282 \u2014 and what "
        "does that tell you about who was really being paid?",
        "What was settled over Schleswig in 1386, and at what price?"]),
      ("A king in a Sk\u00e5ne castle", [
        "What title was Margrete hailed by at Lund in 1387, and what does "
        "<i class=\"dk\">husbond</i> mean?",
        "What did the Dalaborg agreement of 1388 give each side \u2014 and why is 'contract' a better "
        "word for it than 'conquest'?",
        "Whose will, and whose executors, set the Swedish revolt going?"]),
      ("Kalmar, 17 June", [
        "Albrecht lost at \u00c5sle in February 1389. Why did the war go on for another nine years, "
        "and what finally ended it?",
        "The 1396 ordinance dates its confiscations from 1368. What happened in 1368, and what had "
        "been happening to crown land since?",
        "Why was a seven-year-old Pomeranian the right heir, from Margrete's point of view?"])]),

 17: dict(
    name='17-the-union-at-work.html',
    body='c17_body.html',
    svgs={'SVG_ATLANTIC': 'svg_atlantic.txt', 'SVG_BRONDUM': 'svg_brondum.txt'},
    sec=[("s01", "01", "What the union actually was"),
         ("s02", "02", "Norway, from partner to province"),
         ("s03", "03", "The last ship to Greenland"),
         ("s04", "04", "The land behind the union"),
         ("s05", "05", "Birgitta, and what piety bought"),
         ("s06", "06", "The alabaster and the gown")],
    checks=[
      ("Norway, from partner", [
        "What could the three kingdoms say of the years 1389 to 1412 that none of the preceding "
        "three generations could, and against which three powers did they act as one?",
        "Who was the man from Graudenz, and why is he in this chapter rather than the last one?",
        "Why did a schism with two rival popes make a ruler's church appointments easier?"]),
      ("The land behind the union", [
        "Which castle was the most important appointment in Norway, and why?",
        "What happened at Hvalsey on 16 September 1408, and why does a wedding certificate survive "
        "when nothing else does?",
        "What was a <i class=\"dk\">skattland</i>, and which ones did Denmark hold through "
        "Norway?"]),
      ("The alabaster and the gown", [
        "When did Danish deserted farms peak \u2014 and what happened to rents afterwards?",
        "What replaced the <i class=\"dk\">bryde</i>, the <i class=\"dk\">landbo</i> and the "
        "<i class=\"dk\">g\u00e5rds\u00e6de</i>, and who gained in the long run?",
        "By 1500 the church held roughly a third of Danish land. Which later chapter does that "
        "debt fall due in?"])]),

 18: dict(
    name='18-sound-dues-the-hanse-and-a-straining-union.html',
    body='c18_body.html',
    svgs={'SVG_SOUND': 'svg_sound.txt', 'SVG_ROADS': 'svg_roads.txt',
          'SVG_TOLL': 'svg_toll.txt'},
    sec=[("s01", "01", "What Erik inherited"),
         ("s02", "02", "The verdict at Ofen, 1424"),
         ("s03", "03", "A toll at Helsing\u00f8r"),
         ("s04", "04", "The towns declare war"),
         ("s05", "05", "Vordingborg, 1435"),
         ("s06", "06", "Engelbrekt, 1434"),
         ("s07", "07", "The deposition, 1439"),
         ("s08", "08", "Christoffer, and the price of a crown"),
         ("s09", "09", "Oxen, and the road south"),
         ("s10", "10", "The Oldenburg begins, 1448"),
         ("s11", "11", "What the toll bought")],
    checks=[
      ("Vordingborg", [
        "Erik inherited three kingdoms in 1412. What had he been doing for the fifteen years "
        "before that?",
        "What did Philippa agree with L\u00fcbeck, Hamburg, L\u00fcneburg and Wismar in October 1424, and "
        "on whose authority?",
        "Why did Copenhagen, rather than any other town, become Erik's seat of government?"]),
      ("Christoffer, and the price", [
        "Which six towns declared war in 1426, and what were their two grievances at the start?",
        "What happened at Copenhagen in April 1428, and what happened there in June?",
        "Who was Engelbrekt, what class did he come from, and why did the Swedish council join a "
        "rising it had every reason to fear?"]),
      ("What the toll bought", [
        "Why did the Danish council refuse Erik's cousin Bogislav as his successor?",
        "What did Christoffer of Bavaria concede to get three crowns \u2014 and what did he manage "
        "<em>not</em> to concede?",
        "What did the treaty concluded at Bergen in 1450 settle, and how long did it hold?"]),
    ]),
 19: dict(
    name='19-schleswig-holstein-and-the-unions-collapse.html',
    body='c19_body.html',
    svgs={'SVG_FEALTY': 'svg_fealty.txt', 'SVG_HEMMING': 'svg_hemming.txt',
          'SVG_TERR1500': 'svg_terr_1500.txt'},
    sec=[("s01", "01", "A childless uncle, 1459"),
         ("s02", "02", "Ribe, 5 March 1460"),
         ("s03", "03", "What one sentence became"),
         ("s04", "04", "A dowry never paid"),
         ("s05", "05", "Brunkeberg, 1471"),
         ("s06", "06", "A fleet, a university, and a bound peasantry"),
         ("s07", "07", "Hemmingstedt, 17 February 1500"),
         ("s08", "08", "Denmark in 1500"),
         ("s09", "09", "Christian 2., and the woman who kept the accounts"),
         ("s10", "10", "Stockholm, November 1520"),
         ("s11", "11", "1523: two kings leave")],
    checks=[
      ("A dowry never paid", [
        "What was Adolf 8. to Christian 1., and what had he done in 1448?",
        "What did German practice and Danish law each say about a fief left without male heirs, and "
        "which way did each point in 1459?",
        "What was <i class=\"dk\">Ejderpolitikken</i>, and what did it lead to?"]),
      ("Denmark in 1500", [
        "Who beat Christian 1. at Brunkeberg in 1471, and how did the victor turn the battle into "
        "a story afterwards?",
        "What was the ground at Hemmingstedt, and what did the Dithmarschers do with it?",
        "What was lost with Hans von Ahlefeldt, and why does chapter 13 care?"]),
      ("Stockholm, November 1520", [
        "What was <i class=\"dk\">vornedskab</i>, where did it apply, and where did it not?",
        "Name three things Christian 2.'s laws of 1521\u201322 did, and say whom each of them "
        "annoyed.",
        "Who was Sigbrit Villoms, and what office did she hold?"]),
    ]),
 20: dict(
    name='20-reformation-and-the-counts-feud.html',
    body='c20_body.html',
    svgs={'SVG_FEUD': 'svg_feud.txt', 'SVG_WEEKS': 'svg_weeks.txt',
          'SVG_TRANSFER': 'svg_transfer.txt'},
    sec=[("s01", "01", "A promise not kept"),
         ("s02", "02", "The preachers and the towns"),
         ("s03", "03", "A throne left empty"),
         ("s04", "04", "The count lands, June 1534"),
         ("s05", "05", "Skipper Clement and the Jutland rising"),
         ("s06", "06", "\u00d8ksnebjerg, and a year outside Copenhagen"),
         ("s07", "07", "The night of 12 August 1536"),
         ("s08", "08", "Where the land went"),
         ("s09", "09", "A reformation without martyrs")],
    tail_extra=[CODA],
    checks=[
      ("A throne left empty", [
        "What did Duke Christian do at Haderslev in 1528, and what did it show?",
        "Why did the Danish Reformation arrive through the market towns?",
        "What was the <i class=\"dk\">Confessio Hafniensis</i>, and what was decided about it?"]),
      ("\u00d8ksnebjerg", [
        "What did the council of the realm do in 1533 instead of electing a king, and why?",
        "Why did the Jutland bishops in July 1534 vote for a king they knew was a Lutheran?",
        "What happened at Svenstrup on 16 October 1534, and at Aalborg two months later?"]),
      ("Where the land went", [
        "What happened to the peasants of the rebel districts after the rising \u2014 and what did it "
        "do to how they held their land?",
        "Why were the bishops arrested <em>before</em> the assembly of 30 October rather than "
        "after?",
        "What did Christian 3.'s accession charter of 1536 say about Norway, and was it carried "
        "out?"]),
    ]),
}


def block(qs):
    return ('<div class="check">\n  <h4>Checkpoint</h4>\n  <ul>'
            + "".join("\n    <li>%s</li>" % q for q in qs) + '\n  </ul>\n</div>\n\n')


def build(n, c):
    h = open(G + c['body'], encoding='utf-8').read()

    h = re.sub(r'<div class="check">.*?</div>\n\n', '', h, flags=re.S)
    heads = [(m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip())
             for m in re.finditer(r'<h2 id="(s\d\d)">(.*?)</h2>', h, re.S)]
    for frag, qs in c['checks']:
        hit = [sid for sid, t in heads if frag.lower() in t.lower()]
        if len(hit) != 1:
            raise SystemExit("!! chapter %s: anchor %r matched %d sections" % (n, frag, len(hit)))
        a = '<h2 id="%s">' % hit[0]
        h = h.replace(a, block(qs) + a, 1)

    # the section list in the config must match the page, or the rail lies
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
    h = h.replace('{{STYLE}}', style.replace('--band:#96591A;', '--band:%s;' % PART_E))
    h = h.replace('{{RAIL}}', "\n".join(rail)).replace('{{TOC}}', "\n".join(toc))
    h = h.replace('{{JS}}', '<script>' + open(G + 'rail.js', encoding='utf-8').read() + '</script>')
    for k, f in c['svgs'].items():
        h = h.replace('{{%s}}' % k, open(G + f, encoding='utf-8').read())

    w = pagewords(h)
    h = re.sub(r'Era chapter \u00b7 about \d+ minutes',
               'Era chapter \u00b7 about %d minutes' % round(w / 210), h)
    return h


# "entry" in its ordinary sense, found by hand in review session 12 (built pages 16-20,
# text, figure text and attributes, whitespace joined, case ignored): only chapter 18's
# two, a line in the Sound toll register. Each phrase is removed once, exactly as the
# reader's text has it; a phrase no longer on the page is itself reported.
ALLOWED_ENTRY = {18: ['That is the whole entry', 'the entries get longer']}

print("--- Part E ---")
fail = 0
# EVERY FIGURE MUST BE WHAT ITS SCRIPT WRITES, witnessed by running the script in a scratch
# copy (pageguard, review session 12, §16). Part E's figures are all scripted; until this
# session none of them was checked, and svg_fealty.txt was stale.
figs, nfigs = pageguard.figures_fresh(
    HERE, G, sorted({f for c in CFG.values() for f in c['svgs'].values()}))
print("  figures: %d checked against their scripts, %s"
      % (nfigs, 'all fresh' if not figs else '%d NOT' % len(figs)))
for n in sorted(CFG):
    c = CFG[n]
    # Parts A-F have authored bodies and no drafts, so there is no freshcheck here. What
    # this build reads through DK_SRC - the body, style.css, rail.js - must be the file in
    # this folder (the figures are witnessed against their scripts above).
    if not os.path.exists(G + c['body']):
        print("\nchapter %s  %s\n  !! NOT BUILT: no body %s in %s" % (n, c['name'], c['body'], G))
        fail += 1
        continue
    differ = pageguard.same_sources(G, HERE, [c['body'], 'style.css', 'rail.js'])
    if differ:
        print("\nchapter %s  %s\n  !! NOT BUILT: %s missing from %s or %s, or the two copies differ (DK_SRC)." % (n, c['name'], ', '.join(differ), G, HERE))
        fail += 1
        continue
    # SOURCELESS fails here too, unlike Parts D and G-I: every Part E figure has a script,
    # so a figure that loses it has lost its witness.
    stalefigs = {f: v for f, v in figs.items() if f in c['svgs'].values()}
    if stalefigs:
        print("\nchapter %s  %s\n  !! NOT BUILT: figures not what their scripts write: %s"
              % (n, c['name'], '; '.join('%s %s' % (k, 'MISSING' if 'Errno 2' in v else v)
                                for k, v in sorted(stalefigs.items()))))
        fail += 1
        continue
    h = build(n, c)
    # Retired vocabulary in the reader's text (pageguard.reader_text): text, figure text,
    # attributes a screen reader speaks, tags as spaces, entities and look-alikes folded.
    stale = pageguard.stale_vocabulary(h, ALLOWED_ENTRY.get(n, []))
    if stale:
        print("\nchapter %s  %s\n  !! NOT WRITTEN: retired vocabulary %s" % (n, c['name'], stale))
        fail += 1
        continue
    # D-17: a page asks each question once.
    twice = pageguard.asked_twice(h)
    if twice:
        print("\nchapter %s  %s\n  !! NOT WRITTEN: a question asked twice (D-17): %s"
              % (n, c['name'], '; '.join('%s = %s (%.2f)' % t for t in twice)))
        fail += 1
        continue
    css = h.split('<style>')[1].split('</style>')[0]
    ids = set(re.findall(r'id="([a-z0-9]+)"', h))
    links = set(re.findall(r'href="#([a-z0-9]+)"', h))
    bad = [t for t in ['div', 'ol', 'li', 'ul', 'nav', 'details', 'svg', 'p', 'h2', 'h4', 'dl',
                       'dt', 'dd', 'a', 'figure', 'figcaption', 'text', 'g', 'tspan', 'clipPath', 'h1', 'h3', 'i', 'b', 'em', 'strong', 'span', 'summary', 'header', 'footer']
           if len(re.findall(r'<%s[\s>]' % t, h)) != h.count('</' + t + '>')]
    # (review session 14: openings counted by pattern, so '<i' before a line break is
    # one; and the inline and heading tags added, since an unclosed <em> was written)
    w = pagewords(h)
    rail = re.search(r'<nav class="rail".*?</nav>', h, re.S).group(0)
    toc = re.search(r'<details class="toc">.*?</details>', h, re.S).group(0)
    tail_ok = all(('#%s' % t[0]) in rail and ('#%s' % t[0]) in toc
                  for t in TAIL + c.get('tail_extra', []))
    # The brace imbalance was printed and never counted until review session 14.
    braces = css.count('{') - css.count('}')
    page_fail = (bool(bad) + (not links <= ids) + bool(h.count('{{'))
                 + bool(braces)
                 + (not tail_ok) + ('--band:%s;' % PART_E not in h))
    if not page_fail:
        open(OUT + c['name'], 'w', encoding='utf-8').write(h)
    print("\nchapter %s  %s%s" % (n, c['name'], '' if not page_fail else '  !! NOT WRITTEN'))
    print("  braces %d | placeholders %d | anchors %s | tags %s"
          % (braces, h.count('{{'),
             'ok' if links <= ids else 'BAD ' + str(links - ids), bad if bad else 'ok'))
    print("  checkpoints %d | vignettes %d | meanwhile %d | figures %d | terms %d | tail in rail+toc %s"
          % (h.count('class="check"'), h.count('class="vig"'), h.count('class="meanwhile"'),
             h.count('<figure>'), h.count('class="terms"'), 'ok' if tail_ok else 'BAD'))
    print("  part %s | vocabulary clean | questions asked once | words %d (~%d min)"
          % ('ok' if '--band:%s;' % PART_E in h else 'BAD', w, round(w / 210)))
    for m in re.finditer(r'<div class="check">.*?</div>\s*<h2 id="(s\d\d)">(.*?)</h2>', h, re.S):
        print("  checkpoint before %s  %s"
              % (m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip()))
    fail += page_fail
print("\n%s" % ('all five built clean' if not fail else '!! %d problems' % fail))
sys.exit(1 if fail else 0)
