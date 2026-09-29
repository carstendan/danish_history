# -*- coding: utf-8 -*-
"""Build Part D. Per-chapter configs, one command, self-verifying - as build_all.py
does for Parts A to C.

GUARDS, given to Part D in review session 12 (REVIEW-CONSISTENCY.md §16) from
pageguard.py, which Parts G-I share. Until then this script wrote each page inside
build() and read its text as a regular expression does. Each is asked BEFORE the page is
written, and a page that fails any of them, or any structural check, is not written:

  1. pageguard.same_sources: what this build reads through DK_SRC (the body, style.css,
     rail.js and the twelve figures) is the file in this folder; a missing body is NOT
     BUILT. (No freshcheck: Parts A-F have authored bodies, not drafts.)
  2. pageguard.figures_fresh: asked, but Part D's twelve figures have no generator, so
     each is reported SOURCELESS; their content cannot be witnessed.
  3. pageguard.stale_vocabulary on reader_text (no ordinary "entry" in 12-15, by hand).
  4. pageguard.asked_twice (D-17).
"""
import os
import re

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
PART_D = '#3E8474'

TAIL = [("myth", "", "Myth-check"), ("forward", "", "What to carry forward"),
        ("summary", "", "The page in five"), ("questions", "", "Questions &amp; discussion"),
        ("sources", "", "Sources"), ("visit", "", "Places you can visit")]

CFG = {
 12: dict(
    name='12-kingdom-and-church-take-shape.html',
    body='c12_body.html',
    svgs={'SVG_TERR1050': 'svg_terr_1050.txt', 'SVG_DIOCESES': 'svg_dioceses.txt',
          'SVG_REIGNS': 'svg_reigns.txt'},
    sec=[("s01", "01", "The king Adam came to see"), ("s02", "02", "Eight dioceses"),
         ("s03", "03", "Paying for a kingdom"), ("s04", "04", "Odense, 10 July 1086"),
         ("s05", "05", "Making a martyr useful"), ("s06", "06", "Lund, 1103"),
         ("s07", "07", "What a tithe cost"), ("s08", "08", "The parish and the priest"),
         ("s09", "09", "Two thousand churches"), ("s10", "10", "The land fills up"),
         ("s11", "11", "Haraldsted, 1131"), ("s12", "12", "Grathe Hede")],
    checks=[
      ("Odense, 10 July 1086", [
        "How many dioceses were laid out around 1060, and which one lasted six years?",
        "Adam of Bremen is our main source, and Svend Estridsen was his informant. Why is that a "
        "problem from <em>both</em> directions?",
        "A Danish king around 1075 had no annual tax. So what did he live on?"]),
      ("The parish and the priest", [
        "What did Knud den Hellige do after the fleet of 1085 dispersed, and what did it start?",
        "What did Rome want in exchange for the archbishopric at Lund \u2014 and how long before it "
        "can be shown to have been paid?",
        "Who was Herman, and what had been done in 1133 that his embassy to Rome undid?"]),
      ("Haraldsted, 7 January 1131", [
        "The Danish <i class=\"dk\">tiende</i> was split three ways. Which share did canon law "
        "assign to the poor, and who got it in Denmark instead?",
        "Two thousand churches over a hundred and fifty years is how many a year?",
        "What does a village named Hastrup tell you that a village with a <i class=\"dk\">-lev</i> "
        "name does not?"])]),

 13: dict(
    name='13-the-valdemar-age-and-the-baltic-crusades.html',
    body='c13_body.html',
    svgs={'SVG_BALTIC': 'svg_baltic.txt', 'SVG_LEDING': 'svg_leding.txt',
          'SVG_TERR1250': 'svg_terr_1250.txt'},
    sec=[("s01", "01", "Off Grathe Hede"), ("s02", "02", "Ringsted, 1170"),
         ("s03", "03", "Arkona, 1169"), ("s04", "04", "Was it a crusade?"),
         ("s05", "05", "A castle at Havn"), ("s06", "06", "How a fleet became a tax"),
         ("s07", "07", "Sk\u00e5ne says no"), ("s08", "08", "Saxo"),
         ("s09", "09", "The north German years"), ("s10", "10", "Reval, 1219"),
         ("s11", "11", "Ly\u00f8, 1223"), ("s12", "12", "Bornh\u00f6ved, and the book")],
    checks=[
      ("Was it a crusade?", [
        "Valdemar den Store did one thing in 1162 that Danish accounts hurry past. What?",
        "Two ceremonies took place at Ringsted in 1170. What did each of them convert, and from "
        "what into what?",
        "What happened to R\u00fcgen after 1169, and for how long did it last?"]),
      ("Saxo", [
        "Roughly how many ships was the full <i class=\"dk\">leding</i>, and what fraction of it "
        "remained after 1169?",
        "What is a <i class=\"dk\">havne</i>, and what did it owe once the duty was commuted into "
        "money?",
        "Absalon is said to have founded Copenhagen in 1167. What did he actually do at Havn, and "
        "what was there already?"]),
      ("Bornh", [
        "What did the Emperor give Valdemar Sejr in 1214, and why could he afford to give it?",
        "Which contemporary chronicler describes the Estonian campaigns \u2014 and what does he "
        "never mention?",
        "Who brought down the Danish Baltic empire, with how large a party, and where?"])]),
 14: dict(
    name='14-law-regicide-and-the-mortgaged-realm.html',
    body='c14_body.html',
    svgs={'SVG_DESCENT': 'svg_descent.txt', 'SVG_HERRING': 'svg_herring.txt',
          'SVG_PAWN': 'svg_pawn.txt'},
    sec=[("s01", "01", "Vordingborg, 1241"), ("s02", "02", "The last thralls"),
         ("s03", "03", "Slien, 1250"), ("s04", "04", "An archbishop in a cap"),
         ("s05", "05", "Nyborg, 1282"), ("s06", "06", "Finderup, 1286"),
         ("s07", "07", "The most expensive reign"), ("s08", "08", "Towns, friars and herring"),
         ("s09", "09", "The country with no king"), ("s10", "10", "Randers, 1340")],
    checks=[
      ("Slien, August 1250", [
        "Which part of Denmark did <i class=\"dk\">Jyske Lov</i> apply to, and what did the rest "
        "have instead?",
        "Nobody abolished thralldom. So what ended it?",
        "A freed thrall became a <i class=\"dk\">landbo</i>. What did he gain, and what did he "
        "still owe?"]),
      ("The most expensive reign", [
        "What did the bishops agree at Vejle in 1256, and what did it do when Jakob Erlandsen was "
        "arrested?",
        "Who commanded the Danish army at Lohede in 1261, and what became of the commander and "
        "the boy king?",
        "Nine men were outlawed for Finderup. What is the difference between that and knowing who "
        "killed the king?"]),
      ("Randers, 1 April 1340", [
        "What is <i class=\"dk\">pantsætning</i>, and why did it raise taxes rather than lower "
        "them?",
        "Why did the friars settle in towns when the Cistercians had deliberately avoided them?",
        "Why was salted herring worth so much \u2014 and what does that have to do with the church "
        "calendar?"])]),
 15: dict(
    name='15-plague-and-reconquest-valdemar-atterdag.html',
    body='c15_body.html',
    svgs={'SVG_PLAGUE': 'svg_plague.txt', 'SVG_ARITHMETIC': 'svg_arithmetic.txt',
          'SVG_RECONQUEST': 'svg_reconquest.txt'},
    sec=[("s01", "01", "A quarter of Jutland"), ("s02", "02", "Selling Estonia"),
         ("s03", "03", "1350"), ("s04", "04", "What it did to the land"),
         ("s05", "05", "What the survivors built"), ("s06", "06", "Redeeming a kingdom"),
         ("s07", "07", "The road from Middelfart"), ("s08", "08", "1360"),
         ("s09", "09", "Visby, 1361"), ("s10", "10", "Losing to a league"),
         ("s11", "11", "Stralsund, 1370"), ("s12", "12", "The ten-year-old")],
    checks=[
      ("What it did to the land", [
        "Who put Valdemar on the throne in 1340, and why did they want a Danish king at all?",
        "Estonia was sold in 1346. To whom, for how much, and to pay for what?",
        "The soul-masses at Ribe went from about one a year to seventeen a year. Why is that "
        "<em>not</em> a death toll?"]),
      ("1360", [
        "What is an <i class=\"dk\">\u00f8deg\u00e5rd</i>, and which villages produced most of "
        "them?",
        "After 1350 rents fell and wages rose. Who gained, who lost, and why?",
        "After the plague most Danish village churches were altered in the same way. How, and what "
        "paid for it?"]),
      ("Stralsund", [
        "Why did recovering Sk\u00e5ne in 1360 matter for the next four hundred years of Danish "
        "state finance?",
        "Who died outside Visby's east wall in 1361, and what did the town itself do?",
        "Who was Niels Bugge, and what is the honest answer about his death?"])]),
}


def block(qs):
    return ('<div class="check">\n  <h4>Checkpoint</h4>\n  <ul>'
            + "".join("\n    <li>%s</li>" % q for q in qs) + '\n  </ul>\n</div>\n\n')


def body_of(c):
    # Open item 3: this script asked for e12_body.html while every other part used
    # the cNN convention. The bodies recovered in September 2026 are cNN, and the
    # config now says so. Either is still accepted, so a rebuild does not depend on
    # which generation of the filename is on disk.
    body = c['body']
    if not os.path.exists(G + body):
        alt = 'c' + body[1:] if body[0] == 'e' else 'e' + body[1:]
        if os.path.exists(G + alt):
            print("   note: %s not found, using %s" % (body, alt))
            body = alt
    return body


def build(n, c, body):
    h = open(G + body, encoding='utf-8').read()

    h = re.sub(r'<div class="check">.*?</div>\n\n', '', h, flags=re.S)
    heads = [(m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip())
             for m in re.finditer(r'<h2 id="(s\d\d)">(.*?)</h2>', h, re.S)]
    for frag, qs in c['checks']:
        hit = [sid for sid, t in heads if frag.lower() in t.lower()]
        if len(hit) != 1:
            raise SystemExit("!! chapter %d: anchor %r matched %d sections" % (n, frag, len(hit)))
        a = '<h2 id="%s">' % hit[0]
        h = h.replace(a, block(qs) + a, 1)

    # the section list in the config must match the page, or the rail lies.
    # After build_part_e.py, but on ids only: in these parts the rail label is a
    # shortened form of the heading, so labels cannot be compared. Chapter 14's
    # config carried an eleventh section the page has never had, and nothing
    # here noticed.
    want = [sid for sid, num, lab in c['sec']]
    got = [sid for sid, t in heads]
    if got != want:
        raise SystemExit("!! chapter %s: config has sections %s, page has %s"
                         % (n, want, got))

    rail = ['<nav class="rail" aria-label="Sections of this page">'
            '<p class="rail-h">On this page</p><ol>']
    toc = ['<details class="toc"><summary>Contents</summary><ol>']
    for sid, num, lab in [("intro", "", "Introduction")] + c['sec'] + TAIL:
        rail.append('<li><a href="#%s"><span class="rn">%s</span>%s</a></li>' % (sid, num, lab))
        toc.append('<li><a href="#%s">%s</a></li>' % (sid, lab))
    rail.append('</ol></nav>')
    toc.append('</ol></details>')

    style = open(G + 'style.css', encoding='utf-8').read()
    if '--band:#96591A;' not in style:
        raise SystemExit("!! part colour token missing from style.css")
    h = h.replace('{{STYLE}}', style.replace('--band:#96591A;', '--band:%s;' % PART_D))
    h = h.replace('{{RAIL}}', "\n".join(rail)).replace('{{TOC}}', "\n".join(toc))
    h = h.replace('{{JS}}', '<script>' + open(G + 'rail.js', encoding='utf-8').read() + '</script>')
    for k, f in c['svgs'].items():
        h = h.replace('{{%s}}' % k, open(G + f, encoding='utf-8').read())

    w = pagewords(h)
    h = re.sub(r'Era chapter \u00b7 about \d+ minutes',
               'Era chapter \u00b7 about %d minutes' % round(w / 210), h)
    return h


# "entry" in its ordinary sense, found by hand in review session 12 (built pages 12-15,
# text, figure text and attributes, whitespace joined, case ignored): none.
ALLOWED_ENTRY = {}

print("--- Part D ---")
fail = 0
warned = 0
# FIGURES. Part D's twelve svg_*.txt have no generator on disk, so pageguard reports them
# SOURCELESS and there is nothing to run them against: their content cannot be witnessed,
# only that the build reads the copies in this folder (same_sources, below). figures_fresh
# is still asked, so a figure that regains a script is witnessed.
figs, nfigs = pageguard.figures_fresh(
    HERE, G, sorted({f for c in CFG.values() for f in c['svgs'].values()}))
nsrcless = sum(v == 'SOURCELESS' for v in figs.values())
print("  figures: %d checked against their scripts, %d sourceless (content not checkable), %s"
      % (nfigs, nsrcless,
         'none stale' if nsrcless == len(figs) else '%d NOT' % (len(figs) - nsrcless)))
for n in sorted(CFG):
    c = CFG[n]
    # The body is resolved once (the cNN/eNN fallback in body_of), and a missing body is
    # NOT BUILT, not a traceback.
    body = body_of(c)
    if not os.path.exists(G + body):
        print("\nchapter %d  %s\n  !! NOT BUILT: no body %s in %s" % (n, c['name'], body, G))
        fail += 1
        continue
    # No freshcheck: Parts A-F have authored bodies, not drafts. Everything this build reads
    # through DK_SRC - the body, style.css, rail.js and the sourceless figures - must be the
    # file in this folder. A checker shipped a planted figure through DK_SRC before this.
    differ = pageguard.same_sources(G, HERE, [body, 'style.css', 'rail.js']
                                    + sorted(c['svgs'].values()))
    if differ:
        print("\nchapter %d  %s\n  !! NOT BUILT: %s missing from %s or %s, or the two copies differ (DK_SRC)." % (n, c['name'], ', '.join(differ), G, HERE))
        fail += 1
        continue
    stalefigs = {f: v for f, v in figs.items()
                 if f in c['svgs'].values() and v != 'SOURCELESS'}
    if stalefigs:
        print("\nchapter %d  %s\n  !! NOT BUILT: figures not what their scripts write: %s"
              % (n, c['name'], '; '.join('%s %s' % kv for kv in sorted(stalefigs.items()))))
        fail += 1
        continue
    h = build(n, c, body)
    # Retired vocabulary in the reader's text (pageguard.reader_text), and D-17.
    stale = pageguard.stale_vocabulary(h, ALLOWED_ENTRY.get(n, []))
    if stale:
        print("\nchapter %d  %s\n  !! NOT WRITTEN: retired vocabulary %s" % (n, c['name'], stale))
        fail += 1
        continue
    twice = pageguard.asked_twice(h)
    if twice:
        print("\nchapter %d  %s\n  !! NOT WRITTEN: a question asked twice (D-17): %s"
              % (n, c['name'], '; '.join('%s = %s (%.2f)' % t for t in twice)))
        fail += 1
        continue
    css = h.split('<style>')[1].split('</style>')[0]
    ids = set(re.findall(r'id="([a-z0-9]+)"', h))
    links = set(re.findall(r'href="#([a-z0-9]+)"', h))
    bad = [t for t in ['div', 'ol', 'li', 'ul', 'nav', 'details', 'svg', 'p', 'h2', 'h4', 'dl',
                       'dt', 'dd', 'a', 'figure', 'figcaption', 'text', 'g', 'tspan', 'h1', 'h3', 'i', 'b', 'em', 'strong', 'span', 'summary', 'header', 'footer']
           if len(re.findall(r'<%s[\s>]' % t, h)) != h.count('</' + t + '>')]
    # (review session 14: openings counted by pattern, so '<i' before a line break is
    # one; and the inline and heading tags added, since an unclosed <em> was written)
    # (review session 15: and they must nest. '<em><b>x</em></b>' counts even, and a
    # self-closed '<b/>' is never counted; pageguard.nesting walks the page with a stack)
    bad += pageguard.nesting(h)
    w = pagewords(h)
    # The brace imbalance was printed and never counted until review session 14.
    braces = css.count('{') - css.count('}')
    page_fail = (bool(bad) + (not links <= ids) + bool(h.count('{{'))
                 + bool(braces)
                 + ('--band:%s;' % PART_D not in h))
    if not page_fail:
        open(OUT + c['name'], 'w', encoding='utf-8').write(h)
    print("\nchapter %d  %s%s" % (n, c['name'], '' if not page_fail else '  !! NOT WRITTEN'))
    print("  braces %d | placeholders %d | anchors %s | tags %s"
          % (braces, h.count('{{'),
             'ok' if links <= ids else 'BAD ' + str(links - ids), bad if bad else 'ok'))
    print("  checkpoints %d | vignettes %d | meanwhile %d | figures %d | terms %d"
          % (h.count('class="check"'), h.count('class="vig"'), h.count('class="meanwhile"'),
             h.count('<figure>'), h.count('class="terms"')))
    print("  part colour %s | vocabulary clean | questions asked once | words %d (~%d min)"
          % ('ok' if '--band:%s;' % PART_D in h else 'BAD', w, round(w / 210)))
    # The figures' text, measured (review session 17): Part D's twelve svg_*.txt have no
    # script, so mapspine's guards never ran on them. Printed, not refused - estimates.
    said = pageguard.figure_text(h)
    warned += len(said)
    for s in said:
        print("  ! " + s)
    if said:
        print("  !! figure text: %d line(s) above - read them in the page" % len(said))
    fail += page_fail
    for m in re.finditer(r'<div class="check">.*?</div>\s*<h2 id="(s\d\d)">(.*?)</h2>', h, re.S):
        print("  checkpoint before %s  %s"
              % (m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip()))
print("\n%s" % pageguard.summary('four', fail, warned + len(pageguard.WARNINGS)))
if fail:
    raise SystemExit(1)
