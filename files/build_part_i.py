# -*- coding: utf-8 -*-
"""Build Part I. Same shape as build_part_h.py: per-chapter configs, one command,
self-verifying.

Checkpoints live here, keyed to section TITLE fragments rather than ids, so that
renaming a section breaks the build loudly instead of silently moving a checkpoint
somewhere else (lesson L10). Any checkpoint already sitting in the body is stripped
first, so the body and this file cannot disagree.

Part I is chapters 37-44, 1901-1953, and it is the last part. Only chapter 37 is
configured; 38 to 44 are planned but not drafted, and a config entry for a chapter
with no body fails loudly on the first run, which is intended. Chapter 44 will
carry the part coda via tail_extra, as 36 does for H - and, being the last chapter
of the book, will need a book coda as well, which no build script has yet had to
emit.

THE BAND COLOUR IS NEW. D and E are verdigris, F oxblood, G indigo, H slate; I is
moss, added to style.css as --moss for this part. THE BAND TITLE "The small state"
IS NOT IN PLAN_I - the plan names every chapter and never names the part. It is
one constant, BAND_TITLE below, and changing it changes the crumb, the footer and
the index together. Adding a token to the stylesheet is
precedented - --indigo went in for Part G - and `debuild.py` already handles the
consequence, which is that every page shipped before the token existed
reconstructs with a token it never had. Verify after building: 01-11 should stay
`style-only` and 12-36 `identical`. If 12-36 move to `style-only`, the drop list
in debuild.py has not picked the new token up and that must be fixed before
anything ships.

CHECKPOINTS ARE QUESTIONS, NOT PROSE. The chapter 32 draft writes its three
checkpoints as prose recaps - "where we are". Every part from A to G uses three
retrieval questions instead, and the .check rule in style.css is written for a
list. The questions below are derived from the draft's prose so they test what it
says is worth holding, but the prose itself is not reproduced. Changing that is a
change to every shipped part, not to Part H alone.

    python3 build_part_i.py            # strict: every figure must exist
    python3 build_part_i.py --stub     # missing figures become a loud placeholder

--stub exits non-zero even when everything else passes, so a stubbed page cannot be
mistaken for a finished one.
"""
import os
import re
import sys

from pagewords import pagewords   # one definition, shared
import dkpaths

# Paths resolve relative to this script, not to wherever it is run from, and both
# can be overridden. The container paths that used to be hardcoded here meant the
# script only ran in one place; sources live beside it in files/ and built pages
# go to the parent, which is the layout on disk.
HERE = os.path.dirname(os.path.abspath(__file__))
G = dkpaths.resolve('DK_SRC', HERE, 'the folder holding the bodies and figures') + os.sep
OUT = dkpaths.resolve('DK_OUT', os.path.dirname(HERE), 'where built chapter pages are written') + os.sep
PART_I = '#4A5A46'          # --moss; D/E verdigris, F oxblood, G indigo, H slate
BAND_TITLE = 'The small state'   # not set by PLAN_I - see the docstring

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
 37: dict(
    name='37-reform-neutrality-and-the-sale-of-the-west-indies.html',
    body='c37_body.html',
    svgs={'SVG_SYVF': 'svg_syvf_1915.txt',
          'SVG_SOEFOLK': 'svg_soefolk_1918.txt',
          'SVG_AFSTEMNING': 'svg_afstemning_1916.txt'},
    sec=[("s01", "01", 'What the change of system actually changed'),
         ("s02", "02", 'The Radicals, 1905, and the splitting of the left'),
         ("s03", "03", 'Alberti'),
         ("s04", "04", 'The defence question, and a fortress never fired'),
         ("s05", "05", '5 June 1915: the seven categories, minus two'),
         ("s06", "06", 'August 1914: neutrality, and the mines in the Belts'),
         ("s07", "07", 'Gulasch, rationing, and the ships that did not come back'),
         ("s08", "08", 'What the islands were: 1848, 1878, and labour under the '
                       'Danish flag'),
         ("s09", "09", 'Selling them: the treaty, the Rigsdag, the referendum of '
                       'December 1916'),
         ("s10", "10", '31 March 1917')],
    checks=[
      ("The defence question, and a fortress never fired", [
        "The change of system of 1901 altered no word of the constitution. What did it "
        "actually change, and name two of the laws of 1903.",
        "Venstre took office as one party and was three within five years. What split it, "
        "and which two groups did the Radicals go looking for?",
        "Alberti was warned about by the National Bank and protected anyway. By whom, and "
        "on what grounds?"]),
      ("Gulasch, rationing, and the ships that did not come back", [
        "Name the seven categories the franchise of 1849 excluded, and say which two were "
        "admitted in 1915.",
        "What did the conservatives charge for giving up the privileged franchise to the "
        "Landsting?",
        "Why did Denmark mine the Great Belt in August 1914, and why did Britain accept "
        "it?"]),
      ("Selling them: the treaty, the Rigsdag, the referendum of December 1916", [
        "Of about ten thousand Danish merchant seamen, how many died, and how did two "
        "hundred of them die?",
        "What was Contract Day, and what happened on Contract Day 1878?",
        "Who declared the enslaved of the Danish West Indies free in 1848, what happened "
        "to him for it, and who had actually forced the decision?"]),
    ]),
 38: dict(
    name='38-genforeningen-iceland-and-the-easter-crisis.html',
    body='c38_body.html',
    svgs={'SVG_ZONER': 'svg_zoner_1920.txt',
          'SVG_AAR': 'svg_aar_1920.txt',
          'SVG_FORBUND': 'svg_forbund_1918.txt'},
    sec=[("s01", "01", 'November 1918: the soldiers come home'),
         ("s02", "02", 'Iceland, 1 December 1918'),
         ("s03", "03", 'What Versailles said, and what Denmark asked for'),
         ("s04", "04", 'The zones, and the argument about Flensburg'),
         ("s05", "05", 'The commission, January to June 1920'),
         ("s06", "06", '10 February 1920'),
         ("s07", "07", '14 March 1920'),
         ("s08", "08", 'The king dismisses a government'),
         ("s09", "09", 'The strike that did not have to happen'),
         ("s10", "10", '10 July 1920'),
         ("s11", "11", 'What the border cost the people on both sides of it')],
    checks=[
      ("What Versailles said, and what Denmark asked for", [
        "Iceland became a sovereign state on 1 December 1918. Name two things Denmark "
        "kept doing for it, and say in what capacity.",
        "The Act of Union is the only settlement in this book that says how to end "
        "itself. What were the two dates, and what did each allow?",
        "What did the Aabenraa resolution ask for, and what was the Clausen line?"]),
      ("10 February 1920", [
        "Why did Denmark ask for the third zone to be dropped?",
        "Zone 1 was counted en bloc and Zone 2 commune by commune. Which rule would "
        "have kept T\u00f8nder German, and which would have made Flensburg Danish?",
        "Who governed the voting zones between January and June 1920, and why does that "
        "matter for whether the result was accepted?"]),
      ("The strike that did not have to happen", [
        "About 25,000 people in Zone 1 had voted German. What happened to them on "
        "15 June 1920?",
        "The king was entitled by the constitution of 1866 to dismiss the ministry. "
        "What made it impossible anyway, and how long did it take?",
        "Denmark held three general elections in 1920. Give the reason for each, and "
        "note that no two are the same."]),
    ]),
 39: dict(
    name='39-deflation-the-landmandsbank-crash-and-the-first-social-democratic-government.html',
    body='c39_body.html',
    svgs={'SVG_KAPSLER': 'svg_kapsler_1921.txt',
          'SVG_KRAK': 'svg_krak_1922.txt',
          'SVG_TING': 'svg_ting_1924.txt'},
    sec=[("s01", "01", 'The boom ends'),
         ("s02", "02", 'Marks and kroner: Sønderjylland pays for coming home'),
         ("s03", "03", 'Landmandsbanken, 1922'),
         ("s04", "04", 'Who paid for the rescue'),
         ("s05", "05", "The defence settlement of 1922, and Munch's argument"),
         ("s06", "06", '1924: the party in office'),
         ("s07", "07", 'Nina Bang'),
         ("s08", "08", "Steincke's plan, and the other half of it"),
         ("s09", "09", 'Madsen-Mygdal, and the return to gold'),
         ("s10", "10", 'What the twenties settled, and what they did not')],
    checks=[
      ("Who paid for the rescue", [
        "In 1954 the Statistical Department said that year's unemployment was the lowest "
        "since 1920. What does that tell you about every year in between?",
        "Were Sønderjylland's marks exchanged for kroner in 1920? If not, what happened to "
        "savings and debts written in marks?",
        "What happened on the weekend of 8 and 9 July 1922, and what was missing from the "
        "statement that followed?"]),
      ("Nina Bang", [
        "Who paid for the reconstruction of September 1922, and what did the state add in "
        "February 1923?",
        "What did the army law of 1922 do to the army the war had built, and what was Peter "
        "Munch's argument for it?",
        "How many seats did the Social Democrats and the Radicals hold together after "
        "11 April 1924, and why did that matter?"]),
      ("What the twenties settled", [
        "What was Nina Bang the first to be, and what is she wrongly said to be the first "
        "to be?",
        "Steincke's report of 1920 had two halves. Name both, and the law of 1929 that came "
        "from the second.",
        "What did the law of 27 December 1926 do, and why did it bear hardest on "
        "Sønderjylland?"]),
    ]),
 40: dict(
    name='40-depression-stauning-and-the-seeds-of-the-welfare-state.html',
    body='c40_body.html',
    svgs={'SVG_KANSLERGADE': 'svg_kanslergade_1933.txt',
          'SVG_KURS': 'svg_kurs_1933.txt',
          'SVG_REGEL': 'svg_regel_1939.txt'},
    sec=[("s01", "01", '1929: Stauning returns, with the Radicals'),
         ("s02", "02", 'The crash reaches a farming country'),
         ("s03", "03", 'The night at Kanslergade'),
         ("s04", "04", 'What was actually in the deal'),
         ("s05", "05", "Steincke's reform: four laws and a principle"),
         ("s06", "06", 'The vote given back'),
         ("s07", "07", 'Påskeblæsten: the border asked about again'),
         ("s08", "08", 'Eastern Greenland at The Hague, 1933'),
         ("s09", "09", 'Stauning eller kaos'),
         ("s10", "10", 'The Danish Nazis, and why they failed'),
         ("s11", "11", '1939: over ninety per cent, and not enough')],
    checks=[
      ("The night at Kanslergade", [
        "Denmark's depression began with the price of what, sold to whom?",
        "What did the Nakskov town council vote on 2 February 1931, and what did it do "
        "the next day?",
        "After the election of 16 November 1932, how many seats did the government "
        "parties hold of 149, and which chamber did they still not control?"]),
      ("The vote given back", [
        "Name three things the Kanslergade agreement contained, and say which party "
        "wanted each.",
        "The agreement forbade the lockout. What else did it forbid, and for how long?",
        "Name the four laws of the social reform and the sentence the whole of it "
        "rests on."]),
      ("1939: over ninety per cent", [
        "Why did the reform of 1933 not need to amend the constitution to give most "
        "recipients of relief their vote back?",
        "What was Påskeblæsten, and what had happened to the Slesvigsk Parti by 1935?",
        "The Social Democrats won 46 per cent in 1935 and still could not change the "
        "constitution. What changed on 22 September 1936?"]),
    ]),
 41: dict(
    name='41-9-april-1940-and-samarbejdspolitikken.html',
    body='c41_body.html',
    svgs={'SVG_MORGEN': 'svg_morgen_1940.txt',
          'SVG_UDLEVERET': 'svg_udleveret_1941.txt',
          'SVG_VALG': 'svg_valg_1943.txt'},
    sec=[("s01", "01", 'The winter of 1939'),
         ("s02", "02", 'The warnings'),
         ("s03", "03", "From four o'clock to a quarter past eight"),
         ("s04", "04", 'The choice, and who made it'),
         ("s05", "05", 'The realm comes apart'),
         ("s06", "06", 'The alsang summer'),
         ("s07", "07", 'The economy of accommodation'),
         ("s08", "08", 'Frikorps Danmark, and the Communists arrested by Danish police'),
         ("s09", "09", 'Scavenius'),
         ("s10", "10", "The king's telegram, and the wireless"),
         ("s11", "11", 'The election of March 1943')],
    checks=[
      ("From four o'clock", [
        "Which Nordic countries refused Hitler's offer of a non-aggression pact in 1939, "
        "and which one accepted it?",
        "Who warned Copenhagen on 4 April 1940, through which two neutral legations, and "
        "what did the Danish cabinet decide to do?",
        "What reason was given on 6 April for refusing to mobilise six year-classes?"]),
      ("The economy of accommodation", [
        "How long did the fighting of 9 April last, and how much of that time passed "
        "between the crossing of the border and the government's acceptance?",
        "Iceland, the Faroes and Greenland each left Danish control in a different way in "
        "1940 and 1941. Name the way in each case.",
        "How many Danes sang together on the evening of 1 September 1940, at how many "
        "places, and what share of the population was that?"]),
      ("The election of March 1943", [
        "On what legal authority did Danish police arrest Danish communists on 22 June "
        "1941, and what did the law of 22 August 1941 do about that?",
        "What did the War Ministry's order of 8 July 1941 promise Danish officers who "
        "joined Frikorps Danmark?",
        "Why did Denmark sign the Anti-Comintern Pact on 25 November 1941, and what did "
        "the government concede about the constitutionality of doing so?"]),
    ]),
 42: dict(
    name='42-1943-the-year-the-policy-broke.html',
    body='c42_body.html',
    svgs={'SVG_OKTOBER': 'svg_oktober_1943.txt'},
    sec=[("s01", "01", 'The strikes of August'),
         ("s02", "02", '29 August: the fleet'),
         ("s03", "03", 'The warning'),
         ("s04", "04", 'Three weeks in October'),
         ("s05", "05", 'Those who did not get away'),
         ("s06", "06", 'Danmarks Frihedsråd')],
    checks=[
      ("The warning", [
        "The strikes of August 1943 were called by nobody and could be stopped by nobody. What did that prove to the occupier, and what did it prove to the Danish government?",
        "Christian 10. refused to sign his government\'s resignation on 28 August. What did that deny the occupier?",
        "How many ships of the Danish navy were scuttled on 29 August 1943, how many reached Sweden, and who gave the order?"]),
      ("Those who did not get away", [
        "In his telegram of 8 September 1943, what reason did Werner Best give for acting against Denmark\'s Jews at that moment rather than later?",
        "Who warned whom on 28 September 1943, and how did the warning reach the congregation?",
        "About 7,400 people crossed the Sound. What did most of them pay, and why does that make the story better rather than worse?"]),
      ("Danmarks Frihedsr", [
        "How many people were deported from Denmark to Theresienstadt, how many arrived, and how many returned?",
        "About a hundred and fifty Danish communists went from Horserød to Stutthof on 2 October 1943. Who had interned them, and under what law?",
        "What did the Freedom Council have instead of a mandate, and who recognised it?"]),
    ]),
 43: dict(
    name='43-the-underground-and-the-liberation.html',
    body='c43_body.html',
    svgs={'SVG_SABOTAGE': 'svg_sabotage_1945.txt',
          'SVG_FOLKESTREJKE': 'svg_folkestrejke_1944.txt'},
    sec=[("s01", "01", 'How the underground was armed'),
         ("s02", "02", 'Sabotage, and the counter-terror'),
         ("s03", "03", 'The People\'s Strike, June 1944'),
         ("s04", "04", 'The policeless country'),
         ("s05", "05", 'Shellhus'),
         ("s06", "06", '4 May 1945 — and Bornholm')],
    checks=[
      ("Sabotage, and the counter-terror", [
        "Where did the resistance\'s weapons come from, and what did the deliveries cost the air forces that made them?",
        "What were the ventegrupper, roughly how many people did they number, and what were they told to do?",
        "Industrial sabotage went from 73 actions in three years to 816 in one. What changed?"]),
      ("The policeless country", [
        "What is a clearingmord, and where does the word come from?",
        "What did the People\'s Strike of June 1944 obtain, and what did it demonstrate that was not among its demands?",
        "Who asked Copenhagen to go back to work on 2 July 1944, and why did nobody listen?"]),
      ("4 May 1945", [
        "Why did the occupier deport the Danish police in September 1944, on its own stated reasoning?",
        "What replaced the police, and what was it forbidden to do?",
        "Why was the Gestapo headquarters in Copenhagen bombed, and what else was hit?"]),
    ]),
 44: dict(
    name='44-the-reckoning-and-the-accounts.html',
    body='c44_body.html',
    svgs={'SVG_DOMME': 'svg_domme_1945.txt',
          'SVG_BORNHOLM': 'svg_bornholm_1946.txt',
          'SVG_SYDSLESVIG': 'svg_sydslesvig_1954.txt'},
    sec=[("s01", "01", 'The first week'),
         ("s02", "02", 'The law made backwards'),
         ("s03", "03", 'Who was tried, and who was not'),
         ("s04", "04", 'The women'),
         ("s05", "05", 'Bornholm under the Soviets'),
         ("s06", "06", 'The border Denmark did not move'),
         ("s07", "07", 'Marshall aid, and the occupation\'s bill'),
         ("s08", "08", 'Iceland, the Faroes, Greenland')],
    checks=[
      ("Who was tried, and who was not", [
        "The resistance made about 21,800 arrests in eight days in May 1945. On what authority, and what proportion turned out to be chargeable?",
        "What date did the straffelovstillæg reach back to, and which acts before 29 August 1943 did it exempt?",
        "Which Danish constitutional requirement was actually breached in the retsopgør, and why is it not the one usually named?"]),
      ("Bornholm under the Soviets", [
        "Forty-six men were shot and seventy-five people imprisoned for building for the Wehrmacht. What in the statute produced that difference?",
        "107 women were convicted of informing. What share of the national total is that, and what share of the convicted were women?",
        "What was not a crime in Danish or German law, and was punished anyway?"]),
      ("Marshall aid", [
        "On what single condition did the Soviet Union leave Bornholm, and how far did Danish governments afterwards extend it?",
        "What did the British actually ask Denmark in September 1946, and what did Denmark answer?",
        "Was 1946 the first time a Danish government refused territory it could have had?"]),
    ]),
 45: dict(
    name='45-choosing-a-side-and-the-constitution.html',
    body='c45_body.html',
    svgs={'SVG_LANDSTING': 'svg_landsting_1953.txt',
          'SVG_GULV': 'svg_gulv_1953.txt',
          'SVG_TOBILLETTER': 'svg_tobilletter_1953.txt'},
    sec=[("s01", "01", 'The defence union that failed'),
         ("s02", "02", '4 April 1949'),
         ("s03", "03", 'Why anyone wanted a new constitution'),
         ("s04", "04", 'The commission, and the lawyers in it'),
         ("s05", "05", 'The Landsting votes itself out of existence'),
         ("s06", "06", 'A daughter who could inherit'),
         ("s07", "07", '§20: the door'),
         ("s08", "08", 'Greenland stops being a colony'),
         ("s09", "09", 'What Greenland got instead'),
         ("s10", "10", '28 May 1953'),
         ("s11", "11", 'The composite state, ended'),
         ("s12", "12", 'The last of the seven F\'s')],
    checks=[
      ("The Landsting votes itself out of existence", [
        "Why did the Scandinavian defence union fail, and which of the three governments could not move?",
        "What did Denmark attach to the Atlantic treaty in 1949, and what did it not attach?",
        "What did the forty-five per cent rule measure, and why did a revision supported by 91.85 per cent of voters fail under it in 1939?"]),
      ("Greenland stops being a colony", [
        "Why did ordinary Danes have an opinion about the succession clause when they had none about most of the document?",
        "What does §20 permit, what majority does it require, and what happens when that majority cannot be found?",
        "§29 of the 1953 constitution did not abolish the loss of the vote for poor relief. What did it do instead, and is that sentence still in force?"]),
      ("The composite state, ended", [
        "Greenland became a Danish county by a constitution approved in a referendum. Who voted in that referendum, and who did not?",
        "What argument did Denmark make to the United Nations about when a territory stops being non-self-governing?",
        "What was announced on 25 May 1953, and what happened three days afterwards?"]),
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
    if '--moss:%s;' % PART_I not in style:
        raise SystemExit("!! --moss:%s missing from style.css" % PART_I)
    h = h.replace('{{STYLE}}', style.replace('--band:#96591A;', '--band:%s;' % PART_I))
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
    print("--- Part I ---" + ("  [STUBBED FIGURES]" if stub else ""))
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
        print("  part %s | words %d (~%d min, %s)%s"
              % ('ok' if '--band:%s;' % PART_I in h else 'BAD', w, m, band, note))
        for mm in re.finditer(r'<div class="check">.*?</div>\s*<h2 id="(s\d\d)">(.*?)</h2>',
                              h, re.S):
            print("  checkpoint before %s  %s"
                  % (mm.group(1), re.sub(r'<[^>]+>', '', mm.group(2)).strip()))
        if stubbed:
            print("  !! STUBBED: %s" % ", ".join(stubbed))
        fail += (bool(bad) or h.count('{{') or not (links <= ids) or not tail_ok
                 or not (BAND[0] <= m <= BAND[1]) or bool(stubbed) or nfive != 5)
    sys.exit(1 if fail else 0)
