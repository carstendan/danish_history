# -*- coding: utf-8 -*-
"""Build parts A, B and C - chapters 1-11 - from their recovered bodies.

Modelled on build_part_d.py: per-chapter configs in one dict, one command,
self-verifying. Two differences from Part D, both deliberate:

  * SVGs stay inline in the bodies. Chapters 12-15 externalise theirs to
    svg_*.txt; the generators for 1-11 are gone, so a placeholder would point at
    a file that can never be regenerated. (This said Part D's figures had a script
    each. They do not: no generator for any of the twelve is on disk - review
    session 12.)
  * Checkpoints are stripped and re-inserted at build time, exactly as Part D
    does, so the title-anchoring convention keeps failing loudly if a section
    is renamed.

GUARDS, given to Parts A-C in review session 12 (REVIEW-CONSISTENCY.md §16) from
pageguard.py, which Parts G-I share. Until then this script wrote each page inside
build() and read its text as a regular expression does. Each is asked BEFORE the page is
written, and a page that fails any of them, or any structural check, is not written:

  1. pageguard.same_sources: what this build reads through DK_SRC (the body, style.css,
     rail.js) is the file in this folder. (No freshcheck: Parts A-F have authored bodies,
     not drafts. No figures_fresh: the figures are inline in the bodies, no script.)
  2. pageguard.stale_vocabulary on reader_text (no ordinary "entry" in 01-11, by hand).
  3. pageguard.asked_twice (D-17).
"""
import os
import re
import sys

from pagewords import pagewords   # one definition, shared
import dkpaths
import pageguard    # body witness, reader's-text vocabulary, ask once

# Paths resolve relative to this script, not to wherever it is run from, and both
# can be overridden. The container paths that used to be hardcoded here meant the
# script only ran in one place; sources live beside it in files/ and built pages
# go to the parent, which is the layout on disk.
HERE = os.path.dirname(os.path.abspath(__file__))
G = dkpaths.resolve('DK_SRC', HERE, 'the folder holding the bodies and figures') + os.sep
OUT = dkpaths.resolve('DK_OUT', os.path.dirname(HERE), 'where built chapter pages are written') + os.sep

PART_COLOUR = {'A': '#8E9182', 'B': '#B8761F', 'C': '#96591A'}

TAIL = [("myth", "", "Myth-check"), ("forward", "", "What to carry forward"),
        ("summary", "", "The page in five"), ("questions", "", "Questions &amp; discussion"),
        ("sources", "", "Sources"), ("visit", "", "Places you can visit")]

CFG = {
  1: dict(
    part='A',
    name='01-reindeer-hunters-and-the-retreating-ice.html',
    body='c01_body.html',
    sec=[
         ('s01', '01', 'The ice that made the country'),
         ('s02', '02', 'A country that was not islands'),
         ('s03', '03', 'The first arrivals'),
         ('s04', '04', 'Flint: the only wealth'),
         ('s05', '05', 'A climate that would not settle'),
         ('s06', '06', 'How we know any of this'),
         ('s07', '07', 'Federmesser, Bromme, and an argument'),
         ('s08', '08', 'The cold comes back'),
         ('s09', '09', 'What we do not have'),
         ('s10', '10', 'Not settlement. Visits.'),
    ],
    checks=[
      ('The first arrivals', [
        'What is the <i class="dk">hovedopholdslinje</i>, and which side of it has the better soil?',
        'Sea level stood some 80–100 m lower. What did that join Denmark to?',
      ]),
      ('A climate that would not settle', [
        'What is a <i class="dk">zinken</i>, and which culture does it identify?',
        'How did the antler at Slotseng reveal the <em>season</em> of the hunt?',
      ]),
      ('The cold comes back', [
        'Name the four cultures in order, and the climate phase each belongs to.',
        'What does the Laacher See hypothesis claim about the Bromme culture?',
      ]),
    ]),

  2: dict(
    part='A',
    name='02-coast-and-forest-the-hunter-stone-age.html',
    body='c02_body.html',
    sec=[
         ('s01', '01', 'The forest arrives'),
         ('s02', '02', 'Maglemose: lake and woodland'),
         ('s03', '03', 'The sea takes the country'),
         ('s04', '04', 'Kongemose: move to the shore'),
         ('s05', '05', 'Ertebølle: the rich coast'),
         ('s06', '06', 'Vedbæk: people we can look at'),
         ('s07', '07', 'Amber, ornament and the dog'),
         ('s08', '08', 'How we know'),
         ('s09', '09', 'Who they were'),
         ('s10', '10', 'The limits of the idyll'),
         ('s11', '11', 'Why it ended'),
    ],
    checks=[
      ('Kongemose: the move to the shore', [
        'What is a <i class="dk">mikrolit</i>, and why is an edge of several of them better than one large point?',
        'What drowned Doggerland — the Storegga tsunami, or something slower?',
      ]),
      ('Vedbæk: people we can look at', [
        'What is a køkkenmødding, and why does bone survive in one?',
        'What did Ertebølle people make that a non-farming society is not supposed to have?',
      ]),
      ('The limits of the idyll', [
        'What was found in the grave of the eighteen-year-old at Bøgebakken?',
        "What did Lola's chewing gum turn out to contain, and what did she look like?",
      ]),
    ]),

  3: dict(
    part='A',
    name='03-first-farmers-and-the-megalith-builders.html',
    body='c03_body.html',
    sec=[
         ('s01', '01', 'Two hundred years'),
         ('s02', '02', 'Who arrived'),
         ('s03', '03', 'Landnam: unmaking the forest'),
         ('s04', '04', 'The farm'),
         ('s05', '05', 'The megalith explosion'),
         ('s06', '06', 'Sarup: gathering places'),
         ('s07', '07', 'Flint, amber and first metal'),
         ('s08', '08', 'Collapse'),
         ('s09', '09', 'The second turnover'),
         ('s10', '10', 'Dagger time'),
         ('s11', '11', 'What it cost'),
         ('s12', '12', 'What we inherited'),
    ],
    checks=[
      ('The farm', [
        'What is <i class="dk">landnam</i>, and how does it show up in a pollen core?',
        'What did Iversen\'s clearance experiment in Draved Skov show about polished flint axes?',
      ]),
      ('Flint, amber and the first metal', [
        'What is the difference between a <i class="dk">dysse</i> and a <i class="dk">jættestue</i>?',
        'Roughly how many megalithic tombs were built, and how many still stand?',
      ]),
      ('Dagger time', [
        'Where do Single Grave barrows cluster, and why is that location familiar?',
        'What happened to the Funnel Beaker world <em>before</em> the newcomers arrived?',
      ]),
    ]),

  4: dict(
    part='B',
    name='04-bronze-age-amber-sun-and-the-long-road-south.html',
    body='c04_body.html',
    sec=[
         ('s01', '01', 'A country with no copper or tin'),
         ('s02', '02', 'Amber: what Denmark sold'),
         ('s03', '03', 'The mound landscape'),
         ('s04', '04', 'The oak coffins'),
         ('s05', '05', 'The sun'),
         ('s06', '06', 'Sound and spectacle'),
         ('s07', '07', 'Swords, chiefs and travel'),
         ('s08', '08', 'The farm behind it'),
         ('s09', '09', 'Fire, urns and hoards'),
         ('s10', '10', 'Were they local?'),
         ('s11', '11', 'The end'),
    ],
    checks=[
      ('The mound landscape', [
        'What happened to Denmark when the eastern Mediterranean world collapsed around 1,200 BCE?',
        'What did Danish smiths do with the metal that came north, and how can their work be recognised?',
      ]),
      ('The sun', [
        'Roughly how many burial mounds still stand, and how many were probably built?',
        'What did the sprig of yarrow in the Egtved coffin tell us?',
      ]),
      ('Were they local? A scientific feud', [
        'How does the sun chariot work, and why are there two faces to the disc?',
        'Why does almost everything we have from the Late Bronze Age come from bogs?',
      ]),
    ]),

  5: dict(
    part='B',
    name='05-bogs-war-boats-and-the-celtic-world.html',
    body='c05_body.html',
    sec=[
         ('s01', '01', 'A colder, wetter world'),
         ('s02', '02', 'Iron out of the meadow'),
         ('s03', '03', 'The village behind the fence'),
         ('s04', '04', 'Hjortspring: the oldest army'),
         ('s05', '05', 'The ordinary dead'),
         ('s06', '06', 'The bog people'),
         ('s07', '07', 'Naming the dead'),
         ('s08', '08', 'The Celtic connection'),
         ('s09', '09', 'Entering the written record'),
         ('s10', '10', 'Rome arrives'),
    ],
    checks=[
      ('The village behind the fence', [
        'What happened to the climate around 600–500 BCE, and what did it do to the land?',
        'Where in Denmark does bog iron form, and why does that reverse the old ranking of the soils?',
      ]),
      ('The ordinary dead', [
        'What was found at Hjortspring besides the boat, and what does it add up to?',
        'What practice does the Hjortspring deposit begin, and where does a Roman writer describe something like it?',
      ]),
      ('The Celtic connection', [
        'Why do bogs preserve skin and hair but dissolve bone?',
        'Who was the Haraldskær woman thought to be, and who settled it?',
      ]),
    ]),

  6: dict(
    part='B',
    name='06-roman-iron-age-living-beside-the-empire.html',
    body='c06_body.html',
    sec=[
         ('s01', '01', 'The empire next door but one'),
         ('s02', '02', 'What went south'),
         ('s03', '03', 'What came north'),
         ('s04', '04', 'Hoby: a Roman service'),
         ('s05', '05', 'Himlingøje'),
         ('s06', '06', 'Illerup: an army in a lake'),
         ('s07', '07', 'Reading an army'),
         ('s08', '08', 'Nydam: the boat'),
         ('s09', '09', 'The first writing'),
         ('s10', '10', 'The farm that moved'),
         ('s11', '11', 'Gudme: where the gold went'),
         ('s12', '12', 'The end of the Roman order'),
    ],
    checks=[
      ('Hoby: a Roman dinner service on Lolland', [
        'Roughly how far was Denmark from the Roman frontier?',
        'What was in the Juellinge woman\'s right hand, and how does the National Museum read it?',
      ]),
      ('Nydam: the boat that changed everything', [
        'How can the Illerup material be sorted by rank?',
        'Whose name is scratched under the Hoby cups, and why does it matter?',
      ]),
    ]),

  7: dict(
    part='B',
    name='07-gold-catastrophe-and-a-people-with-a-name.html',
    body='c07_body.html',
    sec=[
         ('s01', '01', 'The gold century'),
         ('s02', '02', 'Vindelev'),
         ('s03', '03', 'The Golden Horns'),
         ('s04', '04', '536: the sun fails'),
         ('s05', '05', 'Everybody left. Did they?'),
         ('s06', '06', 'The long recovery'),
         ('s07', '07', 'Halls'),
         ('s08', '08', 'The Dani get a name'),
         ('s09', '09', 'Three things that need a state'),
         ('s10', '10', 'What Part B leaves behind'),
    ],
    checks=[
      ('536: the year the sun failed', [
        'What is a bracteate, and what was it originally copying?',
        'What does the Vindelev inscription say, and why is the date startling?',
      ]),
      ('Halls', [
        'Danish villages were still moving between the catastrophe and the Viking Age. What did they acquire then that the map still shows?',
        'Where does the peak of Danish gold deposition fall relative to the catastrophe of 536?',
      ]),
      ('What Part B leaves behind', [
        'What are <i class="dk">guldgubber</i>, and where have they been found in their thousands?',
        'Name the three works of the early 700s that imply a state.',
      ]),
    ]),

  8: dict(
    part='C',
    name='08-ships-and-raids-the-viking-age-opens.html',
    body='c08_body.html',
    sec=[
         ('s01', '01', 'The customs officer at Portland'),
         ('s02', '02', 'Why then?'),
         ('s03', '03', "What 'viking' means"),
         ('s04', '04', 'What they believed'),
         ('s05', '05', 'Godfred'),
         ('s06', '06', 'The ships'),
         ('s07', '07', 'How a raid worked'),
         ('s08', '08', 'From raiding to conquest'),
         ('s09', '09', 'Francia: up the rivers'),
         ('s10', '10', 'The hardest part to look at'),
         ('s11', '11', 'Written by the victims'),
         ('s12', '12', 'Meanwhile, at home'),
    ],
    checks=[
      ('Godfred, the first Danish king we can see', [
        "Why did Charlemagne's conquest of Saxony make raiding <em>more</em> likely?",
        'Which way did Danish fleets go, and which way did Norwegian and Swedish ones?',
        'Why can a religion with no central authority not resist a king who changes his mind?',
      ]),
      ('How a raid actually worked', [
        'What did Godfred do in 808, and what does it show about his power?',
        'Where was the border fixed in 811, and how long did it hold?',
      ]),
      ('The part that is hardest to look at', [
        'What did Charles the Simple grant Rollo in 911, and on what conditions?',
        'What was the Danelaw, and what did it leave in the English language?',
      ]),
    ]),

  9: dict(
    part='C',
    name='09-towns-silver-and-the-trade-world.html',
    body='c09_body.html',
    sec=[
         ('s01', '01', 'The other half'),
         ('s02', '02', 'Ribe: the first town'),
         ('s03', '03', 'Hedeby: the machine'),
         ('s04', '04', 'What a king wanted'),
         ('s05', '05', 'The road east'),
         ('s06', '06', 'What the towns made'),
         ('s07', '07', 'The country behind the town'),
         ('s08', '08', 'Money that is not money'),
         ('s09', '09', 'Seen from outside'),
         ('s10', '10', 'Living in one'),
         ('s11', '11', 'Christianity arrives'),
         ('s12', '12', 'The end of the emporia'),
    ],
    checks=[
      ('What a king wanted with a town', [
        "What did Ribe's workshops make, and where did their raw materials come from?",
        'Why is Hedeby where it is? Name the two routes that cross there.',
      ]),
      ('Seen from outside', [
        'What is hacksilver, and why did merchants carry folding scales?',
        'Which part of a longship took longest to make — and who made it?',
      ]),
      ('The end of the emporia', [
        'Who was Ottar, and why is his account unlike every other source here?',
        'Where did Christianity establish itself first in Denmark, and why there?',
      ]),
    ]),

 10: dict(
    part='C',
    name='10-one-kingdom-one-faith-jelling.html',
    body='c10_body.html',
    sec=[
         ('s01', '01', 'What Harald inherited'),
         ('s02', '02', 'The monuments'),
         ('s03', '03', 'The two stones'),
         ('s04', '04', "Poppo's iron"),
         ('s05', '05', 'Why a king converts'),
         ('s06', '06', 'The building programme'),
         ('s07', '07', 'Reading the geometry'),
         ('s08', '08', 'Who lived in them'),
         ('s09', '09', 'What was it all for?'),
         ('s10', '10', 'How much is true?'),
         ('s11', '11', 'The son'),
         ('s12', '12', 'What Jelling means now'),
    ],
    checks=[
      ("Poppo's iron", [
        'What does each of the two Jelling stones say, and who raised them?',
        'Which word on the small stone is the first of its kind in Denmark?',
      ]),
      ('Reading the geometry', [
        "What does the picture of Christ on Harald's stone show, and what is unusual about it?",
        'What was built around 980, and how do we date it so precisely?',
      ]),
      ('What Jelling means now', [
        'What are the four candidate explanations for the ring fortresses?',
        'What did strontium in the teeth of the Trelleborg dead show about where they grew up?',
      ]),
    ]),

 11: dict(
    part='C',
    name='11-the-north-sea-empire.html',
    body='c11_body.html',
    sec=[
         ('s01', '01', 'The son who overthrew his father'),
         ('s02', '02', 'Why England could be taken'),
         ('s03', '03', 'The machine'),
         ('s04', '04', '1013'),
         ('s05', '05', 'Cnut'),
         ('s06', '06', 'Ruling from Winchester'),
         ('s07', '07', 'Seven years, then nothing'),
         ('s08', '08', 'Against Norway, 1047–64'),
         ('s09', '09', '1066'),
         ('s10', '10', 'What the Viking Age left'),
    ],
    checks=[
      ('1013', [
        'How long did the reconstructed Skuldelev 2 take from Roskilde to Dublin, and what does that mean for a fleet bound for England?',
        "What happened on St Brice's Day 1002, and what followed from it?",
      ]),
      ('Seven years, then nothing', [
        'What did Cnut do with his army in 1018, and what did he keep?',
        'Where did Cnut actually live and govern from?',
      ]),
      ('What the Viking Age left', [
        'How did Harold Godwinson deal with Harald Hardrada, and how far did his army march to do it?',
        'Why did Harald Hardrada sail for England in 1066, and why did Sweyn Estridsen not?',
      ]),
    ]),

}



def block(qs):
    return ('<div class="check">\n  <h4>Checkpoint</h4>\n  <ul>'
            + "".join("\n    <li>%s</li>" % q for q in qs) + '\n  </ul>\n</div>\n\n')


def build(n, c):
    h = open(G + c['body'], encoding='utf-8').read()

    # strip and re-insert, so a renamed section fails the build rather than
    # silently losing its checkpoint
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
    for sid, num, lab in [("intro", "", "Introduction")] + [tuple(x) for x in c['sec']] + TAIL:
        rail.append('<li><a href="#%s"><span class="rn">%s</span>%s</a></li>' % (sid, num, lab))
        toc.append('<li><a href="#%s">%s</a></li>' % (sid, lab))
    rail.append('</ol></nav>')
    toc.append('</ol></details>')

    style = open(G + 'style.css', encoding='utf-8').read()
    # Open item 4: the token was renamed --band in style.css and this replace
    # silently no-oped. Now it refuses, as build_part_e.py does.
    if '--band:#96591A;' not in style:
        raise SystemExit("!! part colour token missing from style.css")
    h = h.replace('{{STYLE}}', style.replace('--band:#96591A;',
                                             '--band:%s;' % PART_COLOUR[c['part']]))
    h = h.replace('{{RAIL}}', "\n".join(rail)).replace('{{TOC}}', "\n".join(toc))
    h = h.replace('{{JS}}', '<script>' + open(G + 'rail.js', encoding='utf-8').read() + '</script>')

    w = pagewords(h)
    h = re.sub(r'Era chapter \u00b7 about \d+ minutes',
               'Era chapter \u00b7 about %d minutes' % round(w / 210), h)
    return h


# "entry" in its ordinary sense, found by hand in review session 12 (built pages 01-11,
# text, figure text and attributes, whitespace joined, case ignored): none. (10's
# "carpentry" holds the letters and is not the word.)
ALLOWED_ENTRY = {}

print("--- Parts A, B, C ---")
# Parts A-C's figures are inline in their bodies and have no script; there is nothing for
# pageguard.figures_fresh to run, so it is not asked here.
print("  figures: inline in the bodies, no scripts (nothing to witness)")
fail = 0
warned = 0
for n in sorted(CFG):
    c = CFG[n]
    # No freshcheck: Parts A-F have authored bodies, not drafts. Everything this build
    # reads through DK_SRC - the body, style.css, rail.js - must be the file in this folder.
    if not os.path.exists(G + c['body']):
        print("\nchapter %d  %s\n  !! NOT BUILT: no body %s in %s" % (n, c['name'], c['body'], G))
        fail += 1
        continue
    differ = pageguard.same_sources(G, HERE, [c['body'], 'style.css', 'rail.js'])
    if differ:
        print("\nchapter %d  %s\n  !! NOT BUILT: %s missing from %s or %s, or the two copies differ (DK_SRC)." % (n, c['name'], ', '.join(differ), G, HERE))
        fail += 1
        continue
    h = build(n, c)
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
    # Every structural check is asked before the page is written too. Until review
    # session 12 the anchor check here was `links > ids` - a proper superset - so a link
    # to a missing id never failed; and the part colour was printed but never counted.
    # The brace imbalance was printed and never counted until review session 14.
    braces = css.count('{') - css.count('}')
    page_fail = (bool(bad) + (not links <= ids) + bool(h.count('{{'))
                 + bool(braces)
                 + ('--band:%s;' % PART_COLOUR[c['part']] not in h))
    if not page_fail:
        open(OUT + c['name'], 'w', encoding='utf-8').write(h)
    print("\nchapter %d  %s%s" % (n, c['name'], '' if not page_fail else '  !! NOT WRITTEN'))
    print("  braces %d | placeholders %d | anchors %s | tags %s"
          % (braces, h.count('{{'),
             'ok' if links <= ids else 'BAD ' + str(links - ids), bad if bad else 'ok'))
    print("  checkpoints %d | vignettes %d | meanwhile %d | figures %d | terms %d"
          % (h.count('class="check"'), h.count('class="vig"'), h.count('class="meanwhile"'),
             h.count('<figure>'), h.count('class="terms"')))
    print("  part %s %s | vocabulary clean | questions asked once | words %d (~%d min)"
          % (c['part'],
             'ok' if '--band:%s;' % PART_COLOUR[c['part']] in h else 'BAD', w, round(w / 210)))
    # The figures' text, measured (review session 17): these figures have no script, so
    # mapspine's guards never ran on them. Printed, not refused - the boxes are estimates.
    said = pageguard.figure_text(h)
    warned += len(said)
    for s in said:
        print("  ! " + s)
    if said:
        print("  !! figure text: %d line(s) above - read them in the page" % len(said))
    fail += page_fail
print("\n%s" % pageguard.summary('eleven', fail, warned))
sys.exit(1 if fail else 0)
