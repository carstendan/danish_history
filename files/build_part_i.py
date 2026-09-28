# -*- coding: utf-8 -*-
"""Build Part I. Same shape as build_part_h.py: per-chapter configs, one command,
self-verifying.

Checkpoints live here, keyed to section TITLE fragments rather than ids, so that
renaming a section breaks the build loudly instead of silently moving a checkpoint
somewhere else (lesson L10). Any checkpoint already sitting in the body is stripped
first, so the body and this file cannot disagree.

Part I is chapters 37-45, 1901-1953, all nine configured and built from
`c37_draft.md` ... `c45_draft.md` through mkbody.py. Chapter 45 is the last page of the
book and declares no carry-forward (no_forward=True, decision D-C).

GUARDS, given to Part I in review session 11 (REVIEW-CONSISTENCY.md §15), from the
module Parts G and H share (pageguard.py, §14.6). Until then this script had no
vocabulary check and no summary line, and wrote each page inside build(). Each is
asked BEFORE the page is written, and a page that fails any of them is not written:

  1. freshcheck.check(n): the body on disk is what the draft builds. Else NOT BUILT.
  2. pageguard.same_body: the body this build reads (DK_SRC) is the one freshcheck
     checked.
  3. pageguard.figures_fresh: every figure is what its script writes, run in a
     scratch copy.
  4. pageguard.stale_vocabulary on reader_text: retired vocabulary ("entry", Band X,
     Era page, a zero-padded chapter number) in what a reader or screen reader gets.
     The one ordinary "entry" in 37-45, found by hand, is in ALLOWED_ENTRY.
  5. pageguard.asked_twice: a page asks each question once, across the five opening
     questions, the checkpoints and the four end tiers (D-17, content-word Jaccard
     >= 0.4). Otherwise NOT WRITTEN.

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

There is no --stub here (review session 15). Every figure in this part has a script, and
a missing or stale one stops its chapter (NOT BUILT) before the page is assembled: the
answer is to run the script, not to preview a placeholder. --stub is refused, so asking
for it cannot be mistaken for a run. build_part_f.py keeps --stub, with its exemption and
its refusal to write a stubbed page inside the repository.
"""
import os
import re
import sys

from pagewords import pagewords   # one definition, shared
import dkpaths
import freshcheck   # the body-against-draft comparison, run before every page
import pageguard    # body witness, figure freshness, reader's-text vocabulary, ask once

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

def tail_of(c):
    """The terminal units this chapter has: all of TAIL, less the carry-forward
    for a chapter that declares no_forward (decision D-C)."""
    return [t for t in TAIL if not (t[0] == 'forward' and c.get('no_forward'))]


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
        "Name the seven categories the franchise of 1849 excluded, and give the one piece "
        "of reasoning that had kept out women and servants alike.",
        "What did the conservatives charge for giving up the privileged franchise to the "
        "Landsting?",
        "Some thirty thousand men south of the Kongeå were conscripted "
        "into the German army. Why could the Danish government not ask for any of them back?"]),
      ("Selling them: the treaty, the Rigsdag, the referendum of December 1916", [
        "Of about ten thousand Danish merchant seamen, how many died, and how did two "
        "hundred of them die?",
        "What was Contract Day, and what happened on Contract Day 1878?",
        "Who calculated Denmark's rations in 1917, and on what did each person's ration "
        "depend?"]),
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
        "About how many men from North Schleswig were called up into the German army, and why do counts of the dead differ?"]),
      ("10 February 1920", [
        "Who was entitled to vote in the plebiscites, and what made that franchise strange?",
        "Which towns inside Zone 1 had German majorities, and in which town of Zone 2 "
        "was the Danish minority thickest?",
        "Who governed the voting zones between January and June 1920, and why does that "
        "matter for whether the result was accepted?"]),
      ("The strike that did not have to happen", [
        "Why did the Danish quarter of Flensburg vote when the result was not in doubt?",
        "Who went to the king on Easter Saturday, and on whose initiative?",
        "What did the Easter Sunday settlement give each side, and what did it cost the campaign for Flensburg?"]),
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
        "How did the new province take to Danish politics? Compare its turnout at the "
        "election of 1924 with the rest of Jutland's.",
        "What happened on the weekend of 8 and 9 July 1922, and what was missing from the "
        "statement that followed?"]),
      ("Nina Bang", [
        "Who paid for the reconstruction of September 1922, and what did the state add in "
        "February 1923?",
        "What did the army law of 1922 do to the army the war had built, and what was Peter "
        "Munch's argument for it?",
        "Who were the Social Democrats' first two members of the Folketing, and what had "
        "the party become at the election of 11 April 1924?"]),
      ("What the twenties settled", [
        "What was Nina Bang the first to be, and what is she wrongly said to be the first "
        "to be?",
        "Steincke's report of 1920 had two halves. Name both, and the law of 1929 that came "
        "from the second.",
        "What did the law of 27 December 1926 do, and how did Cornelius Petersen answer "
        "the rising krone?"]),
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
         ("s06", "06", 'The vote given back, to most'),
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
        "What rate did the Kanslergade agreement set for the pound, and why do the published sizes of the devaluation disagree?",
        "Name the four laws of the social reform and the sentence the whole of it "
        "rests on."]),
      ("1939: over ninety per cent", [
        "What had Norway claimed in eastern Greenland in July 1931, and what did the "
        "court at The Hague decide on 5 April 1933?",
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
        "What did Scavenius's declaration of 8 July 1940 say Denmark's task was, and how "
        "much public protest was there?",
        "How many Danes sang together on the evening of 1 September 1940, at how many "
        "places, and what share of the population was that?"]),
      ("The election of March 1943", [
        "What did Christian 10. reply to Hitler's birthday telegram of September 1942, "
        "and what did the reply cost?",
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
        "Who ran Denmark from September 1943 to May 1945, and how could they make law?",
        "How many ships of the Danish navy were scuttled on 29 August 1943, how many reached Sweden, and who gave the order?"]),
      ("Those who did not get away", [
        "Best put the Jews of Denmark at about six thousand. What did Danish accounts give, and why is the number unstable?",
        "Who warned whom on 28 September 1943, and how did the warning reach the congregation?",
        "Most of those who crossed the Sound paid for the boats. What did the Swedish police registers show about how many of them gave their religion as Christian?"]),
      ("Danmarks Frihedsr", [
        "How many people were deported from Denmark to Theresienstadt, how many arrived, and how many returned?",
        "About a hundred and fifty Danish communists went from Horserød to Stutthof on 2 October 1943. Who had interned them, and under what law?",
        "How many people died in the crossing or in connection with the action, and why does Bak not separate the causes?"]),
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
        "What happened to Carl Johan Bruhn on the night of 27 to 28 December 1941, and what did it cost SOE?",
        "What were the ventegrupper, roughly how many people did they number by May 1945, and what did they do on 5 May?",
        "What happened to the Hvidsten group between March 1943 and June 1944?"]),
      ("The policeless country", [
        "What did Hitler order on 30 December 1943, and why did he reject public hostage executions?",
        "How did a walk-out at Burmeister & Wain turn into a general strike by 30 June 1944?",
        "Who asked Copenhagen to go back to work on 2 July 1944, and why did it have so little effect?"]),
      ("4 May 1945", [
        "What did the air-raid sirens signal at eleven on 19 September 1944, and where were the men seized that day taken?",
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
        "Who opposed the straffelovstillæg when it was passed, and what was Hal Koch's objection in 1947?",
        "Which Danish constitutional requirement was actually breached in the retsopgør, and why is it not the one usually named?"]),
      ("Bornholm under the Soviets", [
        "Why was the case against Wright, Thomsen & Kier dropped, and whose policy served the contractors as a defence?",
        "107 women were convicted of informing. What share of the national total is that, and what share of the convicted were women?",
        "What was not a crime in Danish or German law, and was punished anyway?"]),
      ("Marshall aid", [
        "Why did the Soviet occupation of Bornholm last almost eleven months, and whose delay was most of it?",
        "What did the British actually ask Denmark in September 1946, and why is it misdescribed as an offer?",
        "Why were the Danish-minded in South Schleswig a majority of the natives but a minority of the inhabitants?"]),
    ]),
 45: dict(
    name='45-choosing-a-side-and-the-constitution.html',
    no_forward=True,      # the last page: nothing to carry forward (decision D-C)
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
        "Name three things the constitutional commission chose not to write into the constitution.",
        "What did Denmark attach to the Atlantic treaty in 1949, and what did it not attach?",
        "What barred Frederik 9.'s daughters from the throne before 1953: the Kongelov of 1665, or something else?"]),
      ("Greenland stops being a colony", [
        "Why did ordinary Danes have an opinion about the succession clause when they had none about most of the document?",
        "What does §20 permit, what majority does it require, and what happens when that majority cannot be found?",
        "§29 of the 1953 constitution did not abolish the loss of the vote for poor relief. What did it do instead, and is that sentence still in force?"]),
      ("The composite state, ended", [
        "What did the Greenland laws of 1950 change, and to which audience besides Greenland were they addressed?",
        "What argument did Denmark make to the United Nations about when a territory stops being non-self-governing?",
        "What was announced on 25 May 1953, and what happened three days afterwards?"]),
    ]),
}

# Part I's ordinary uses of "entry" - found by hand in review session 11 (REVIEW §15) on the
# built pages 37-45, text, figure text and attributes, whitespace joined, case ignored. An
# allowed phrase goes here per chapter, exactly as the reader's text has it; one that is no
# longer on the page is itself reported. The only one: Kresten Andresen's letters and diary
# entries (37 §06). The JavaScript's `entries` is not reader text.
ALLOWED_ENTRY = {37: ['letters and diary entries home']}


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
    has_fwd = '<h2 id="forward"' in h
    if has_fwd == bool(c.get('no_forward')):
        raise SystemExit("!! chapter %s: no_forward=%s in CFG but the body %s a carry-forward"
                         % (n, bool(c.get('no_forward')), 'has' if has_fwd else 'lacks'))
    for sid, num, lab in ([("intro", "", "Introduction")] + c['sec']
                          + tail_of(c) + c.get('tail_extra', [])):
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
            raise SystemExit("!! chapter %s: missing figure %s (run its script)" % (n, f))
        h = h.replace('{{%s}}' % k, svg)

    w = pagewords(h)
    h = re.sub(r'Era chapter \u00b7 about \d+ minutes',
               'Era chapter \u00b7 about %d minutes' % round(w / 210), h)
    return h


BAND = (25, 50)
TARGET = (28, 40)

if __name__ == "__main__":
    if "--stub" in sys.argv:
        raise SystemExit("!! --stub is not offered in Part I (review session 15): every figure "
                         "has a script, so run the script")
    print("--- Part I ---")
    fail = 0
    # EVERY FIGURE MUST BE WHAT ITS SCRIPT WRITES, witnessed by running the script in a
    # scratch copy, not by trusting the svg_*.txt on disk (pageguard, §14.6).
    figs, nfigs = pageguard.figures_fresh(
        HERE, G, sorted({f for c in CFG.values() for f in c['svgs'].values()}))
    print("  figures: %d checked against their scripts, %s"
          % (nfigs, 'all fresh' if not figs else '%d NOT' % len(figs)))
    for n in sorted(CFG):
        c = CFG[n]
        # THE BODY MUST BE WHAT THE DRAFT BUILDS, asked before the page is written.
        fresh = freshcheck.check(n)
        if fresh[0] != 'FRESH':
            print("\nchapter %s  %s\n  !! NOT BUILT: the body is %s against its draft (%s). "
                  "Run DK_DRAFT=c%s_draft.md python3 mkbody.py %s and read what it says."
                  % (n, c['name'], fresh[0], fresh[1], n, n))
            fail += 1
            continue
        # AND THE BODY THIS BUILD READS MUST BE THE ONE FRESHCHECK READ (DK_SRC).
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
        h = build(n, c)
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
                           'clipPath', 'h1', 'h3', 'i', 'b', 'em', 'strong', 'span', 'summary', 'header', 'footer']
               if len(re.findall(r'<%s[\s>]' % t, h)) != h.count('</' + t + '>')]
        # (review session 14: openings counted by pattern, so '<i' before a line break is
        # one; and the inline and heading tags added, since an unclosed <em> was written)
        # (review session 15: and they must nest. '<em><b>x</em></b>' counts even, and a
        # self-closed '<b/>' is never counted; pageguard.nesting walks the page with a stack)
        bad += pageguard.nesting(h)
        w = pagewords(h)
        m = round(w / 210)
        five = len(re.findall(r'<ol class="five">.*?</ol>', h, re.S))
        nfive = len(re.findall(r'<li><p>', re.search(r'<ol class="five">.*?</ol>', h, re.S).group(0))) \
            if five else 0
        rail = re.search(r'<nav class="rail".*?</nav>', h, re.S).group(0)
        toc = re.search(r'<details class="toc">.*?</details>', h, re.S).group(0)
        tail_ok = all(('#%s' % t[0]) in rail and ('#%s' % t[0]) in toc
                      for t in tail_of(c) + c.get('tail_extra', []))
        # Every structural check is asked BEFORE the page is written, as the A-F builds ask
        # it (review session 14). Until then this build wrote the page first and counted
        # the failures after, so a page with a broken anchor, an unclosed tag, a stray
        # placeholder, a summary that is not five or an unbalanced stylesheet reached the
        # repository while the run said only "!! N problems".
        braces = css.count('{') - css.count('}')
        page_fail = (bool(bad) + bool(h.count('{{')) + (not links <= ids) + (not tail_ok)
                     + (not BAND[0] <= m <= BAND[1]) + bool(braces) + (nfive != 5)
                     + ('--band:%s;' % PART_I not in h))
        if not page_fail:
            open(OUT + c['name'], 'w', encoding='utf-8').write(h)
        print("\nchapter %s  %s%s" % (n, c['name'], '' if not page_fail else '  !! NOT WRITTEN'))
        print("  braces %d | placeholders %d | anchors %s | tags %s"
              % (braces, h.count('{{'),
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
        print("  part %s | vocabulary clean | questions asked once | words %d (~%d min, %s)%s"
              % ('ok' if '--band:%s;' % PART_I in h else 'BAD', w, m, band, note))
        for mm in re.finditer(r'<div class="check">.*?</div>\s*<h2 id="(s\d\d)">(.*?)</h2>',
                              h, re.S):
            print("  checkpoint before %s  %s"
                  % (mm.group(1), re.sub(r'<[^>]+>', '', mm.group(2)).strip()))
        fail += page_fail
    print("\n%s" % ('all nine built clean' if not fail else '!! %d problems' % fail))
    sys.exit(1 if fail else 0)
