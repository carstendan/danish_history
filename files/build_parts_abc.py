# -*- coding: utf-8 -*-
"""Build parts A, B and C - chapters 1-11 - from their recovered bodies.

Modelled on build_part_d.py: per-chapter configs in one dict, one command,
self-verifying. Two differences from Part D, both deliberate:

  * SVGs stay inline in the bodies. Chapters 12-15 externalise theirs to
    svg_*.txt because a Python script generates each one; the generators for
    1-11 are gone, so a placeholder would point at a file that can never be
    regenerated.
  * Checkpoints are stripped and re-inserted at build time, exactly as Part D
    does, so the title-anchoring convention keeps failing loudly if a section
    is renamed.
"""
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
        'Sea level stood about 120 m lower. What did that join Denmark to?',
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
        'Why are Stone Age sites inland in north Denmark but underwater in the south?',
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
        'Farming arrived with people rather than ideas. What evidence shows that?',
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
         ('s01', '01', 'A country with no ore'),
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
        'Denmark has no copper and no tin. So how was the bronze paid for?',
        'How far south did Danish amber actually travel?',
      ]),
      ('The sun', [
        'Why does organic material survive in some Bronze Age mounds and not others?',
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
        'What is <i class="dk">myremalm</i>, and why did it undermine the old elite?',
        'Why are poor graves not the same thing as a poor society?',
      ]),
      ('The ordinary dead', [
        'What was found at Hjortspring besides the boat, and what does it add up to?',
        'Why did the victors destroy the captured equipment rather than use it?',
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
        'Besides hides and amber, what did the north sell to the empire?',
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
        'What happened in 536, and what did it do to Scandinavia?',
        'Where does the peak of Danish gold deposition fall relative to that?',
      ]),
      ('What Part B leaves behind', [
        'Who first writes down the name of the Danes, and when?',
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
        'What does <i class="dk">viking</i> actually mean?',
        'Why can a religion with no central authority not resist a king who changes his mind?',
      ]),
      ('How a raid actually worked', [
        'What did Godfred do in 808, and what does it show about his power?',
        'Where was the border fixed in 811, and how long did it hold?',
      ]),
      ('The part that is hardest to look at', [
        'What turned seasonal raiding into conquest? Name the three stages.',
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
        'What tells us Ribe was laid out rather than grown?',
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
         ('s04', '04', "Poppo's glove"),
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
      ("Poppo's glove", [
        'What does each of the two Jelling stones say, and who raised them?',
        'Which word on the small stone is the first of its kind in Denmark?',
      ]),
      ('Reading the geometry', [
        'Why did Harald convert? Give the external reason and the internal one.',
        'What was built around 980, and how do we date it so precisely?',
      ]),
      ('What Jelling means now', [
        'What are the four candidate explanations for the ring fortresses?',
        "Which of Harald's three claims on the big stone is the weakest?",
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
         ('s08', '08', 'Seventeen years against Norway'),
         ('s09', '09', '1066'),
         ('s10', '10', 'What the Viking Age left'),
    ],
    checks=[
      ('1013', [
        "Why did paying Danegeld make England's position worse, not better?",
        "What happened on St Brice's Day 1002, and what followed from it?",
      ]),
      ('Seven years, then nothing', [
        'What did Cnut do with his army in 1018, and why?',
        'Where did Cnut actually live and govern from?',
      ]),
      ('What the Viking Age left', [
        'Why did the North Sea Empire dissolve within seven years?',
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

    rail = ['<nav class="rail" aria-label="Sections of this page">'
            '<p class="rail-h">On this page</p><ol>']
    toc = ['<details class="toc"><summary>Contents</summary><ol>']
    for sid, num, lab in [("intro", "", "Introduction")] + [tuple(x) for x in c['sec']] + TAIL:
        rail.append('<li><a href="#%s"><span class="rn">%s</span>%s</a></li>' % (sid, num, lab))
        toc.append('<li><a href="#%s">%s</a></li>' % (sid, lab))
    rail.append('</ol></nav>')
    toc.append('</ol></details>')

    style = open(G + 'style.css', encoding='utf-8').read()
    if '--part:#96591A;' not in style:
        raise SystemExit("!! part colour token missing from style.css")
    h = h.replace('{{STYLE}}', style.replace('--part:#96591A;',
                                             '--part:%s;' % PART_COLOUR[c['part']]))
    h = h.replace('{{RAIL}}', "\n".join(rail)).replace('{{TOC}}', "\n".join(toc))
    h = h.replace('{{JS}}', '<script>' + open(G + 'rail.js', encoding='utf-8').read() + '</script>')

    w = pagewords(h)
    h = re.sub(r'Era chapter \u00b7 about \d+ minutes',
               'Era chapter \u00b7 about %d minutes' % round(w / 210), h)
    open(OUT + c['name'], 'w', encoding='utf-8').write(h)
    return h


print("--- Parts A, B, C ---")
fail = 0
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
    # retired vocabulary must not survive outside the scroll-spy script
    prose = re.sub(r'<script>.*?</script>', '', h, flags=re.S)
    stale = {k: len(re.findall(p, prose)) for k, p in
             [('Band X', r'\bBand [A-I]\b'), ('entry', r'\b[Ee]ntr(?:y|ies)\b'),
              ('Era page', r'Era page'), ('padded', r'\b[Cc]hapters? 0\d\b')]}
    stale = {k: v for k, v in stale.items() if v}
    print("\nchapter %d  %s" % (n, c['name']))
    print("  braces %d | placeholders %d | anchors %s | tags %s"
          % (css.count('{') - css.count('}'), h.count('{{'),
             'ok' if links <= ids else 'BAD ' + str(links - ids), bad if bad else 'ok'))
    print("  checkpoints %d | vignettes %d | meanwhile %d | figures %d | terms %d"
          % (h.count('class="check"'), h.count('class="vig"'), h.count('class="meanwhile"'),
             h.count('<figure>'), h.count('class="terms"')))
    print("  part %s %s | vocabulary %s | words %d (~%d min)"
          % (c['part'],
             'ok' if '--part:%s;' % PART_COLOUR[c['part']] in h else 'BAD',
             'clean' if not stale else 'STALE ' + str(stale), w, round(w / 210)))
    fail += bool(bad) + bool(stale) + (links > ids) + bool(h.count('{{'))
print("\n%s" % ('all eleven built clean' if not fail else '!! %d problems' % fail))
