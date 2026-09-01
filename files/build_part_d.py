# -*- coding: utf-8 -*-
"""Build Band D. Per-entry configs, one command, self-verifying - as build_all.py
does for bands A to C."""
import os
import re

from pagewords import pagewords   # one definition, shared

# Paths resolve relative to this script, not to wherever it is run from, and both
# can be overridden. The container paths that used to be hardcoded here meant the
# script only ran in one place; sources live beside it in files/ and built pages
# go to the parent, which is the layout on disk.
HERE = os.path.dirname(os.path.abspath(__file__))
G = os.environ.get('DK_SRC', HERE) + os.sep
OUT = os.environ.get('DK_OUT', os.path.dirname(HERE)) + os.sep
PART_D = '#3E8474'

TAIL = [("myth", "", "Myth-check"), ("forward", "", "What to carry forward"),
        ("summary", "", "The page in five"), ("questions", "", "Questions &amp; discussion"),
        ("sources", "", "Sources"), ("visit", "", "Places you can visit")]

CFG = {
 12: dict(
    name='12-kingdom-and-church-take-shape.html',
    body='e12_body.html',
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
        "Who was Herman, and what would have happened in 1133 without him?"]),
      ("Haraldsted, 7 January 1131", [
        "The Danish <i class=\"dk\">tiende</i> was split three ways. Which share did the rest of "
        "Europe give to the poor, and who got it in Denmark?",
        "Two thousand churches over a hundred and fifty years is how many a year?",
        "What does a village named Hastrup tell you that a village named Gudme does not?"])]),

 13: dict(
    name='13-the-valdemar-age-and-the-baltic-crusades.html',
    body='e13_body.html',
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
        "What is a <i class=\"dk\">havne</i>, and what did it owe from about 1200?",
        "The Sk\u00e5ne farmers lost the fighting. What did they nevertheless win?"]),
      ("Bornh", [
        "What did the Emperor give Valdemar Sejr in 1214, and why could he afford to give it?",
        "Which contemporary chronicler describes the Estonian campaigns \u2014 and what does he "
        "never mention?",
        "How many men did it take to bring down the Danish Baltic empire, and where were they when "
        "they did it?"])]),
 14: dict(
    name='14-law-regicide-and-the-mortgaged-realm.html',
    body='e14_body.html',
    svgs={'SVG_DESCENT': 'svg_descent.txt', 'SVG_PAWN': 'svg_pawn.txt'},
    sec=[("s01", "01", "Vordingborg, 1241"), ("s02", "02", "The last thralls"),
         ("s03", "03", "Slien, 1250"), ("s04", "04", "An archbishop in a cap"),
         ("s05", "05", "Nyborg, 1282"), ("s06", "06", "Finderup, 1286"),
         ("s07", "07", "The most expensive reign"), ("s08", "08", "Towns, friars and herring"),
         ("s09", "09", "The country with no king"), ("s10", "10", "Randers, 1340"),
         ("s11", "11", "What it was actually for")],
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
        "Name the two main promises of the 1282 charter \u2014 and say who they actually "
        "protected.",
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
    body='e15_body.html',
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
        "What did Valdemar actually hold in 1340, and how did he propose to enlarge it?",
        "Estonia was sold in 1346. To whom, for how much, and to pay for what?",
        "The soul-masses at Ribe went from about one a year to seventeen in 1350. Why is that "
        "<em>not</em> a death toll?"]),
      ("1360", [
        "What is an <i class=\"dk\">\u00f8deg\u00e5rd</i>, and which villages produced most of "
        "them?",
        "After 1350 rents fell and wages rose. Who gained, who lost, and why?",
        "Most Danish village churches were altered in the same two ways after the plague. Which "
        "two, and what paid for it?"]),
      ("Stralsund", [
        "Why did recovering Sk\u00e5ne in 1360 matter for the next four hundred years of Danish "
        "state finance?",
        "Who died outside Visby's east wall in 1361, and what did the town itself do?",
        "Who was Niels Bugge, and what is the honest answer about his death?"])]),
}


def block(qs):
    return ('<div class="check">\n  <h4>Checkpoint</h4>\n  <ul>'
            + "".join("\n    <li>%s</li>" % q for q in qs) + '\n  </ul>\n</div>\n\n')


def build(n, c):
    # Open item 4: this script asks for e12_body.html while every other part uses
    # the cNN convention, a leftover from before it was renamed. Accept either, so
    # a rebuild does not depend on which generation of the filename is on disk.
    body = c['body']
    if not os.path.exists(G + body):
        alt = 'c' + body[1:] if body[0] == 'e' else 'e' + body[1:]
        if os.path.exists(G + alt):
            print("   note: %s not found, using %s" % (body, alt))
            body = alt
    h = open(G + body, encoding='utf-8').read()

    h = re.sub(r'<div class="check">.*?</div>\n\n', '', h, flags=re.S)
    heads = [(m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip())
             for m in re.finditer(r'<h2 id="(s\d\d)">(.*?)</h2>', h, re.S)]
    for frag, qs in c['checks']:
        hit = [sid for sid, t in heads if frag.lower() in t.lower()]
        if len(hit) != 1:
            raise SystemExit("!! entry %d: anchor %r matched %d sections" % (n, frag, len(hit)))
        a = '<h2 id="%s">' % hit[0]
        h = h.replace(a, block(qs) + a, 1)

    rail = ['<nav class="rail" aria-label="Sections of this page">'
            '<p class="rail-h">On this page</p><ol>']
    toc = ['<details class="toc"><summary>Contents</summary><ol>']
    for sid, num, lab in [("intro", "", "Introduction")] + c['sec'] + TAIL:
        rail.append('<li><a href="#%s"><span class="rn">%s</span>%s</a></li>' % (sid, num, lab))
        toc.append('<li><a href="#%s">%s</a></li>' % (sid, lab))
    rail.append('</ol></nav>')
    toc.append('</ol></details>')

    style = open(G + 'style.css', encoding='utf-8').read()
    if '--part:#96591A;' not in style:
        raise SystemExit("!! band colour token missing from style.css")
    h = h.replace('{{STYLE}}', style.replace('--part:#96591A;', '--part:%s;' % PART_D))
    h = h.replace('{{RAIL}}', "\n".join(rail)).replace('{{TOC}}', "\n".join(toc))
    h = h.replace('{{JS}}', '<script>' + open(G + 'rail.js', encoding='utf-8').read() + '</script>')
    for k, f in c['svgs'].items():
        h = h.replace('{{%s}}' % k, open(G + f, encoding='utf-8').read())

    w = pagewords(h)
    h = re.sub(r'Era page \u00b7 about \d+ minutes',
               'Era page \u00b7 about %d minutes' % round(w / 210), h)
    open(OUT + c['name'], 'w', encoding='utf-8').write(h)
    return h


print("--- Band D ---")
for n in sorted(CFG):
    c = CFG[n]
    h = build(n, c)
    css = h.split('<style>')[1].split('</style>')[0]
    ids = set(re.findall(r'id="([a-z0-9]+)"', h))
    links = set(re.findall(r'href="#([a-z0-9]+)"', h))
    bad = [t for t in ['div', 'ol', 'li', 'ul', 'nav', 'details', 'svg', 'p', 'h2', 'h4', 'dl',
                       'dt', 'dd', 'a', 'figure', 'figcaption', 'text', 'g', 'tspan']
           if h.count('<' + t + ' ') + h.count('<' + t + '>') != h.count('</' + t + '>')]
    w = pagewords(h)
    print("\nentry %d  %s" % (n, c['name']))
    print("  braces %d | placeholders %d | anchors %s | tags %s"
          % (css.count('{') - css.count('}'), h.count('{{'),
             'ok' if links <= ids else 'BAD ' + str(links - ids), bad if bad else 'ok'))
    print("  checkpoints %d | vignettes %d | meanwhile %d | figures %d | terms %d"
          % (h.count('class="check"'), h.count('class="vig"'), h.count('class="meanwhile"'),
             h.count('<figure>'), h.count('class="terms"')))
    print("  band %s | words %d (~%d min)"
          % ('ok' if '--part:%s;' % PART_D in h else 'BAD', w, round(w / 210)))
    for m in re.finditer(r'<div class="check">.*?</div>\s*<h2 id="(s\d\d)">(.*?)</h2>', h, re.S):
        print("  checkpoint before %s  %s"
              % (m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip()))
