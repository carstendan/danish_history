# -*- coding: utf-8 -*-
"""Build Part G. Same shape as build_part_f.py: per-chapter configs, one command,
self-verifying.

Checkpoints live here, keyed to section TITLE fragments rather than ids, so that
renaming a section breaks the build loudly instead of silently moving a checkpoint
somewhere else (lesson L10). Any checkpoint already sitting in the body is stripped
first, so the body and this file cannot disagree.

Part G is chapters 25-31, 1660-1814. Chapter 31 carries the part coda via
tail_extra, as chapter 24 does for Part F.

TWO DIVERGENCES FROM THE DRAFT, both deliberate and both worth knowing about:

  1. The draft's checkpoints are prose recaps - "three things are worth holding".
     Every part from A to F uses three retrieval QUESTIONS instead, and the .check
     rule in style.css is written for a list. The questions below are derived from
     the draft's prose so they test exactly what it says is worth holding, but the
     prose itself is not reproduced. If the prose form is wanted, it is a change to
     block() here and to the shipped parts, not to Part G alone.

  2. Chapter 30's third checkpoint is drafted "after §10" - after the last narrative
     section, where there is no following heading to anchor it to and no page left
     to check back over. It is anchored on §10 here instead, so it appears after §09
     and sets up the ordinance of 1792 rather than recapping it. The drafted prose
     for it makes the chapter's closing argument and belongs in the myth-check or
     the summary, not in a mid-page pause.

    python3 build_part_g.py            # strict: every figure must exist
    python3 build_part_g.py --stub     # missing figures become a loud placeholder

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
PART_G = '#2F4C7A'          # --indigo; D and E are teal, F is oxblood, G moves again

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
 25: dict(
    name='25-the-kingdom-made-hereditary.html',
    body='c25_body.html',
    svgs={'SVG_TERR1660': 'svg_terr_1660.txt', 'SVG_ROUTING': 'svg_routing.txt',
          'SVG_HARTKORN': 'svg_hartkorn.txt'},
    sec=[("s01", "01", 'The city that had just survived'),
         ("s02", "02", 'The estates meet, 10 September 1660'),
         ("s03", "03", 'Hereditary, then absolute'),
         ("s04", "04", 'The Kongelov, 14 November 1665'),
         ("s05", "05", 'Colleges instead of a council, amter instead of len'),
         ("s06", "06", 'The land written down'),
         ("s07", "07", 'The council disappears'),
         ("s08", "08", 'A church of royal officers'),
         ("s09", "09", 'What the fortress cost')],
    checks=[
      ("The Kongelov", [
        "What did the estates actually meet to settle in September 1660, and who was not "
        "summoned?",
        "The proposal to make the crown hereditary came from the burghers and the clergy, not "
        "from the king's side of the room. Why would townsmen do that?",
        "Hereditary did not have to mean absolute. In which six days did the one become the "
        "other, and what survives to tell us why?"]),
      ("The council disappears", [
        "The visible revolution took six weeks. What took four years, and what did it "
        "produce?",
        "What is <i class=\"dk\">hartkorn</i>, and what did the registers of 1662 and 1664 "
        "measure?",
        "Name three later things in this part that could not have been done without the "
        "arithmetic of the 1660s."]),
      ("What the fortress cost", [
        "How many people were executed for opposing the change of 1660, and what happened to "
        "the nobility's land?",
        "If absolutism was neither imposed by force nor resisted, what makes 1660 difficult "
        "to write about?",
        "Who paid for it, and were they in the room?"]),
    ]),
 26: dict(
    name='26-law-rank-and-the-war-for-skaane.html',
    body='c26_body.html',
    svgs={'SVG_SCANIA': 'svg_scania.txt', 'SVG_MANDEBOD': 'svg_mandebod.txt',
          'SVG_CELL': 'svg_cell.txt'},
    sec=[("s01", "01", 'A king who crowned himself'),
         ("s02", "02", 'Rank instead of blood'),
         ("s03", "03", 'Griffenfeld'),
         ("s04", "04", 'The law and the land written down, 1681\u201388'),
         ("s05", "05", 'The war to take Sk\u00e5ne back, 1675\u201379'),
         ("s06", "06", 'K\u00f8ge Bugt, 1 July 1677'),
         ("s07", "07", 'The snaphaner in the G\u00f6inge woods'),
         ("s08", "08", 'Making Sk\u00e5ne Swedish'),
         ("s09", "09", 'The Blue Tower'),
         ("s10", "10", 'Fontainebleau, and Munkholmen')],
    checks=[
      ("The law and the land", [
        "Griffenfeld was a commoner who built a state in which commoners could rise. What "
        "else was he doing while he built it?",
        "Who destroyed him, and what did they want that he thought Denmark could not "
        "afford?",
        "He was right about the war. Should that have saved him?"]),
      ("The snaphaner", [
        "Lund on 4 December 1676 and K\u00f8ge Bugt on 1 July 1677 point opposite ways. What "
        "did each decide?",
        "How does a country win command of the sea and lose the war it was fighting?",
        "What was happening to the population of Sk\u00e5ne while the two armies fought over "
        "it?"]),
      ("The Blue Tower", [
        "Name the six things the <i class=\"dk\">f\u00f6rsvenskning</i> of Sk\u00e5ne took: a "
        "university, a war, and four more.",
        "How long did it take, and how do we know it had worked by 1720?",
        "What does the Sk\u00e5ne case suggest about national identity generally \u2014 found, "
        "or made?"]),
    ]),
 27: dict(
    name='27-the-last-war-for-the-sound.html',
    body='c27_body.html',
    svgs={'SVG_TERR1721': 'svg_terr_1721.txt', 'SVG_PLAGUE': 'svg_plague_1711.txt',
          'SVG_SCHOOLS': 'svg_schools.txt'},
    sec=[("s01", "01", 'Travendal, 1700 \u2014 out in three months'),
         ("s02", "02", 'Poltava changes the arithmetic, 1709'),
         ("s03", "03", 'Helsingborg, 10 March 1710'),
         ("s04", "04", 'The plague, 1711'),
         ("s05", "05", 'Tordenskjold'),
         ("s06", "06", 'The Gottorp share taken, 1713\u20131721'),
         ("s07", "07", 'Frederiksborg, 1720 \u2014 the Sound kept, Sk\u00e5ne not'),
         ("s08", "08", 'Two hundred and forty schoolhouses'),
         ("s09", "09", 'Egede sails')],
    checks=[
      ("The plague", [
        "Denmark rejoined the war in 1709 to recover a province. How long did that purpose "
        "survive, and what ended it?",
        "What changed at Poltava that made a second Danish attempt look sensible?",
        "Everything after March 1710 is a war fought without prospect of its own aim. What "
        "does that do to how you should read the settlement of 1720?"]),
      ("The Gottorp share", [
        "The army lost the only battle that mattered in this war. What did it do to its own "
        "horses on the beach at Helsingborg, and why?",
        "What did Tordenskjold destroy at Dynekilen on 8 July 1716, and what did that end?",
        "Two ways of measuring the same twenty years. Which of Denmark's two services was "
        "the problem in this period, and which was not?"]),
      ("Two hundred and forty", [
        "Frederik 4. was a poor commander. Name two things he nonetheless finished his reign "
        "holding that he did not start with.",
        "Which wound in the southern border did he close, and how many previous reigns had "
        "failed to close it?",
        "A reign can be a failure by its own stated aim and a success by almost any other. "
        "Make the case both ways."]),
    ]),
 28: dict(
    name='28-the-bound-countryside-and-the-pious-state.html',
    body='c28_body.html',
    svgs={'SVG_HOVYEAR': 'svg_hovyear.txt', 'SVG_NORWAY': 'svg_norway.txt',
          'SVG_CATECHISM': 'svg_catechism.txt'},
    sec=[("s01", "01", 'A king who closed the theatres'),
         ("s02", "02", 'The parish under pietism \u2014 1735, 1736, 1737'),
         ("s03", "03", 'Stavnsb\u00e5nd, 1733 \u2014 and why'),
         ("s04", "04", 'A week of hoveri'),
         ("s05", "05", 'The cattle plague'),
         ("s06", "06", 'The Brethren'),
         ("s07", "07", 'How Norway was governed, and what it sent south'),
         ("s08", "08", "Holberg's Copenhagen, and the fire of 1728"),
         ("s09", "09", 'The loosening, 1746'),
         ("s10", "10", 'A state that could not price its own grain')],
    checks=[
      ("The cattle plague", [
        "The two famous facts about the Danish countryside here are the bond and the labour. "
        "Popular memory ranks them one way and the specialists the other. Which way, and "
        "why?",
        "Name three things that were true of <i class=\"dk\">hoveri</i> and not of the bond: "
        "no ceiling, and two more.",
        "Why did rising grain prices from mid-century make the labour service worse rather "
        "than better for the man performing it?"]),
      ("How Norway was governed", [
        "Two pietisms reached Denmark. Which one could be administered through parishes, and "
        "what three compulsory things did it become?",
        "The Moravians met in farmhouses and were banned. Why did the same state import a "
        "whole Moravian town thirty years later?",
        "What does that reversal tell you about what the state's interest in religion "
        "actually was?"]),
      ("A state that could not price", [
        "Describe the 1740s and 1750s as they look from Copenhagen \u2014 three things.",
        "Describe the same decades as they look from the countryside, where four-fifths of "
        "Danes lived.",
        "Which of the two has Danish popular memory kept, and what follows from that?"]),
    ]),
 29: dict(
    name='29-struensee-and-the-village-taken-apart.html',
    body='c29_body.html',
    svgs={'SVG_VILLAGE': 'svg_village.txt', 'SVG_BAND': 'svg_band.txt',
          'SVG_COLUMN': 'svg_column.txt'},
    sec=[("s01", "01", 'A sick king and his doctor'),
         ("s02", "02", 'Sixteen months of cabinet orders'),
         ("s03", "03", 'Caroline Mathilde, governing'),
         ("s04", "04", '17 January 1772'),
         ("s05", "05", "Guldberg's Denmark, and indf\u00f8dsret 1776"),
         ("s06", "06", 'The commission, 1786'),
         ("s07", "07", 'Udskiftning'),
         ("s08", "08", '20 June 1788'),
         ("s09", "09", 'The column, 1792\u201397'),
         ("s10", "10", 'Who was left out')],
    checks=[
      ("Guldberg's Denmark", [
        "Name four of the things abolished or changed in Struensee's sixteen months.",
        "Almost none of it was in force when he fell. Give both reasons.",
        "What is the defence available to a man who rules on a sick king's signature, when "
        "somebody else obtains that signature at four in the morning?"]),
      ("Udskiftning", [
        "Struensee ruled by cabinet order. Guldberg overthrew him and ruled by cabinet order. "
        "What does the repetition tell you?",
        "Three regimes in twelve years. How did each of them actually get its hands on the "
        "king's authority?",
        "What is the constitutional problem underneath all three, and which chapter built "
        "it?"]),
      ("The column", [
        "The ordinance of 20 June 1788 did three things at once. Name them.",
        "Which of the three does the monument commemorate, and which one explains why the "
        "landowners did not fight it?",
        "The tie to the home district was moved rather than removed. Moved to whom, and "
        "until when?"]),
    ]),
 30: dict(
    name='30-the-danish-atlantic.html',
    body='c30_body.html',
    svgs={'SVG_TRIANGLE': 'svg_triangle.txt', 'SVG_SURVEYS': 'svg_surveys.txt',
          'SVG_PAPERS': 'svg_papers.txt'},
    sec=[("s01", "01", 'Before the Atlantic \u2014 Trankebar 1620, the Gold Coast 1661'),
         ("s02", "02", 'St Thomas, 1672'),
         ("s03", "03", 'The triangle, in tons and in people'),
         ("s04", "04", 'The crossing'),
         ("s05", "05", 'St Jan, November 1733'),
         ("s06", "06", 'St Croix bought, 1733'),
         ("s07", "07", 'The law of the plantation'),
         ("s08", "08", 'The Crown takes the islands, 1754'),
         ("s09", "09", 'What the sugar built in Copenhagen'),
         ("s10", "10", 'The ordinance of 16 March 1792')],
    checks=[
      ("St Jan, November 1733", [
        "Roughly how many people did Denmark carry across the Atlantic, and on about how many "
        "voyages?",
        "About what proportion did not survive the crossing?",
        "The enslaved population of the islands never once reproduced itself in a hundred and "
        "seventy years. What follows from that, both for the ships and for the trade's "
        "ending?"]),
      ("The Crown takes the islands", [
        "Three things happened in 1733. Put them in order and say which came first.",
        "What penalties did the September code make legal for resistance?",
        "The Akwamu took the fort at Coral Bay in November and held most of St Jan for six "
        "months. Why does the order of the three events matter to how you read the rising?"]),
      ("The ordinance of 16 March", [
        "What did the sugar of these islands pay for in Copenhagen \u2014 name three things "
        "still standing?",
        "Who was Ernst Schimmelmann, and what did his family own?",
        "Denmark is about to become the first slave-trading nation to legislate against the "
        "trade. Before you read how, predict what a state with these interests would write "
        "into the ordinance."]),
    ]),
 31: dict(
    name='31-the-flourishing-trade-and-the-wreck-of-it.html',
    body='c31_body.html',
    svgs={'SVG_1807': 'svg_1807.txt', 'SVG_FLEET': 'svg_fleet.txt',
          'SVG_DALER': 'svg_daler.txt'},
    tail_extra=[CODA],
    sec=[("s01", "01", 'Neutral bottoms'),
         ("s02", "02", 'A city rebuilt twice, 1794 and 1795'),
         ("s03", "03", '2 April 1801'),
         ("s04", "04", 'The Norwegian half'),
         ("s05", "05", 'September 1807'),
         ("s06", "06", 'The gunboat war'),
         ("s07", "07", '5 January 1813'),
         ("s08", "08", 'Kiel, 14 January 1814'),
         ("s09", "09", 'Eidsvoll, and the refusal'),
         ("s10", "10", 'Every child, 29 July 1814')],
    checks=[
      ("The Norwegian half", [
        "What was a neutral flag worth between 1793 and 1807, and what was Denmark carrying "
        "under it?",
        "Denmark knew the practice was against the conventions and did it anyway, with the "
        "state's protection. What was the battle of 1801 the bill for?",
        "Denmark's escape in 1801 had nothing to do with the fighting. What ended the "
        "crisis, and where did it happen?"]),
      ("Kiel, 14 January 1814", [
        "Name the four things the British took or destroyed in September 1807 besides the "
        "ships that sailed.",
        "What replaced the fleet, and what kind of war could it fight?",
        "The reform of 5 January 1813 is remembered as the state bankruptcy. What was "
        "actually declared, and what was made security for the new notes?"]),
      ("Every child", [
        "Norway was ceded at Kiel in January 1814. What did the Norwegians do between then "
        "and November?",
        "What did Norway keep, and what did it not?",
        "Four hundred years in one realm ended in an afternoon's treaty. Which article of "
        "Kiel did the Norwegians treat as void, and on what argument?"]),
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
    if '--indigo:%s;' % PART_G not in style:
        raise SystemExit("!! --indigo:%s missing from style.css" % PART_G)
    h = h.replace('{{STYLE}}', style.replace('--band:#96591A;', '--band:%s;' % PART_G))
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
    print("--- Part G ---" + ("  [STUBBED FIGURES]" if stub else ""))
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
              % ('ok' if '--band:%s;' % PART_G in h else 'BAD', w, m, band, note))
        for mm in re.finditer(r'<div class="check">.*?</div>\s*<h2 id="(s\d\d)">(.*?)</h2>',
                              h, re.S):
            print("  checkpoint before %s  %s"
                  % (mm.group(1), re.sub(r'<[^>]+>', '', mm.group(2)).strip()))
        if stubbed:
            print("  !! STUBBED: %s" % ", ".join(stubbed))
        fail += (bool(bad) or h.count('{{') or not (links <= ids) or not tail_ok
                 or not (BAND[0] <= m <= BAND[1]) or bool(stubbed))
    sys.exit(1 if fail else 0)
