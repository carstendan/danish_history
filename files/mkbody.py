# -*- coding: utf-8 -*-
"""mkbody.py — turn a chapter of PART_G_DRAFT.md into a cNN_body.html.

The draft carries everything except the things a body needs and prose does not:
the hook, the key-term chips, the five opening questions, and where the figures
sit with what caption. Those are in HAND below, one entry per chapter, and they
are the only hand-written part. Everything else is lifted from the draft, so the
body cannot drift from the prose that was reviewed.

WHAT IS DELIBERATELY NOT EMITTED: checkpoints. build_part_g.py injects those from
its own config, keyed to section title fragments, and strips any it finds in the
body first (lesson 10). A checkpoint written here would be silently deleted.

    python3 mkbody.py 25          # one chapter to stdout-named file
    python3 mkbody.py             # all seven
"""
import html
import os
import re
import sys

import draftnotes

# The draft to read. Overridable, because this script was written against Part G
# and Part H's chapters live in their own files: DK_DRAFT=c32_draft.md.
DRAFT = os.environ.get("DK_DRAFT", "PART_G_DRAFT.md")

# ---------------------------------------------------------------- hand-authored
# name, title, dates, people, hook, keys, five questions, figures.
# figures: (after_section_id, placeholder, caption_title, caption_body)
HAND = {
 25: dict(
   file='c25_body.html',
   part='Part G', band='Absolutism', num=25, dates='1660 – 1670',
   title='The kingdom made hereditary',
   people='Frederik 3. · Hans Nansen · Hans Svane · Joachim Gersdorff · Peder Schumacher',
   hook="In ten days in October 1660 an assembly called to settle a war debt handed the "
        "king of Denmark more power than any monarch in Europe, and did it by a vote. "
        "Nobody stormed anything. What replaced the charter was a state of standing "
        "offices, a register that reduced every farm in the kingdom to a single number, "
        "and a law kept in a silver casket and not printed for more than forty years.",
   keys=['stændermøde 1660', 'arvehyldning 18. oktober 1660', 'enevælde',
         'Kongeloven 1665', 'kollegier', 'amter og amtmænd',
         'matriklen 1662 og 1664', 'hartkorn', 'rangforordningen 1671'],
   qs=["Denmark's estates met to raise a tax. How did that end with an absolute monarchy?",
       "The proposal came from the burghers and the clergy, not from the king. Why would "
       "townsmen hand a king unlimited power?",
       "Hereditary did not have to mean absolute. Where, in five days, did the one become "
       "the other?",
       "What did the <i class=\"dk\">Kongelov</i> of 1665 actually say, and why was it kept "
       "out of print for so long?",
       "How do you tax a kingdom whose land you have never measured — and what did the "
       "answer cost the people on it?"],
   figs=[("s03", "SVG_TERR1660",
          "Figure 1 · The realm in 1660",
          "What was left after Roskilde and Copenhagen. Skåne, Halland, Blekinge, Bohuslän, "
          "Jämtland, Härjedalen, Gotland and Øsel are drawn in their own tone as provinces "
          "ceded to Sweden between 1645 and 1658; Sweden itself is not coloured, because "
          "since 1523 it has not been this map's business. Bornholm is Danish because the "
          "islanders made it so, and Trøndelag is Norwegian again — both returned in 1660, "
          "which is why this map is dated 1660 and not 1658."),
         ("s05", "SVG_ROUTING",
          "Figure 2 · Where a decision travelled, before 1660 and after 1665",
          "The same five questions — a town tax, a fortress, a warship, an appeal, a trading "
          "licence — before and after. On the left they all go to one body; on the right "
          "each goes to an office of its own. This is not a change of furniture but a change "
          "of topology, and the council of the realm has no place in the second diagram."),
         ("s07", "SVG_HARTKORN",
          "Figure 3 · One farm, reduced to a number",
          "What a tenant actually owed, and what the commissioners of 1662 and 1664 wrote "
          "down instead: grain, dairy, livestock and labour, each converted and then added "
          "into one figure. The quantities here are a worked example built from the "
          "conversion rules, not a transcription of one entry."),],
 ),

 26: dict(
   file='c26_body.html',
   part='Part G', band='Absolutism', num=26, dates='1670 – 1699',
   title='Law, rank, and the war for Skåne',
   people='Christian 5. · Peder Griffenfeld · Niels Juel · Leonora Christina · Svend Poulsen',
   hook="A new king puts the crown on his own head, replaces birth with a table of ranks, "
        "and gives Denmark a single code of law that lasted into the twentieth century. "
        "He also spends four years and a generation of men trying to take Skåne back, wins "
        "at sea, loses on land, and hands every conquest back on a French instruction. What "
        "the war settles is not the border but the province: Skåne stops being Danish here.",
   keys=['enevoldsarvekonge', 'salving 1671', 'rangforordningen 1671',
         'Danske Lov 1683', 'Christian 5.s matrikel 1688', 'Skånske Krig 1675–79',
         'slaget i Køge Bugt 1677', 'snaphaner', 'forsvenskningen',
         'Jammers Minde'],
   qs=["Christian 5. was crowned by nobody. What is the difference between a coronation and "
       "an anointing, and why did it matter in 1671?",
       "The <i class=\"dk\">rangforordning</i> replaced birth with rank. What did that "
       "actually change, and for whom?",
       "Denmark won the naval war of 1675–79 outright and gained nothing. Why?",
       "What were the <i class=\"dk\">snaphaner</i>, and why does the argument about what to "
       "call them still matter?",
       "Two women's reputations in this part were made by books published long after they "
       "died. What does that do to what we can say about them?"],
   figs=[("s06", "SVG_SCANIA",
          "Figure 1 · The theatre, 1675–79",
          "Four years, and the border did not move. Denmark landed in Skåne in 1676 and most "
          "of the province came over within weeks; Lund on 4 December decided the land war "
          "and Køge Bugt on 1 July 1677 decided the sea. Neither decided the province. At "
          "Fontainebleau in 1679 Louis XIV ended the war and required every conquest to be "
          "given back."),
         ("s04", "SVG_MANDEBOD",
          "Figure 2 · Who owed for a killing, 1241 and 1683",
          "The change between the two codes is not severity. Jyske Lov priced a man, priced "
          "the parts of him as fractions of that, and split the debt three ways between the "
          "killer, his father's kin and his mother's kin — a family owed for what a member "
          "had done. Danske Lov has no tariff of body parts and no shares. The killer answers "
          "alone. About a third of Danske Lov's provisions came from the old provincial "
          "laws; the kin's share of the debt was not among them."),
         ("s09", "SVG_CELL",
          "Figure 3 · Seven of my paces long and six broad",
          "The room as Leonora Christina measured it, having nothing to measure it with. Two "
          "beds, a table, two chairs; newly whitewashed when she came in, and a floor so "
          "thick with filth she took it for clay. Her bed faced the doors, and with all three "
          "open she could see as far as the stair door, which was the fourth. She was in the "
          "tower 7,955 days."),],
 ),

 27: dict(
   file='c27_body.html',
   part='Part G', band='Absolutism', num=27, dates='1699 – 1721',
   title='The last war for the Sound',
   people='Frederik 4. · Peter Wessel Tordenskjold · Marie Grubbe · Hans Egede · Gertrud Rask',
   hook="Denmark enters the Great Northern War to get Skåne back and comes out of it with "
        "none of it — and with a southern border closed for the first time since 1544, a "
        "Sound toll that Sweden now paid, two hundred and forty village schools, and a "
        "mission in Greenland. In between, plague takes something from a third to over forty per cent of "
        "Copenhagen, and the state counts the measures it took but not the dead.",
   keys=['Travendalfreden 1700', 'Poltava 1709', 'pesten 1711',
         'Dynekilen 1716', 'Frederiksborgfreden 1720', 'arvehyldningen 1721',
         'rytterskoler', 'vornedskabets ophævelse 1702', 'landmilitsen 1701'],
   qs=["Denmark went to war twice in this chapter for the same province and got it neither "
       "time. What changed in 1709 that made the second attempt look sensible?",
       "Why is the absence of a <i class=\"dk\">snaphane</i> rising in 1710 the best measure "
       "of what happened to Skåne after 1679?",
       "The state could date every measure it took against the plague of 1711 and could not "
       "say how many died. What does that tell you about what it was built to do?",
       "What did Denmark actually gain at Frederiksborg in 1720, and why is a border worth "
       "more than a province?",
       "The instruments of the 1721 homage were left vague. Why did nobody mind at the time, "
       "and what did the vagueness cost a century later?"],
   figs=[("s07", "SVG_TERR1721",
          "Figure 1 · The realm in 1721",
          "The southern border closed. The whole of Schleswig is now the king's, the Gottorp "
          "share having been taken in 1713 and confirmed in 1720; Holstein is not, and the "
          "ducal and royal parcels there are interleaved parish by parish, which is why the "
          "legend carries the distinction the map cannot. The eastern provinces are no longer "
          "drawn in their own tone: by 1721 they are not a loss being absorbed but a settled "
          "fact, and no Danish army went for them again. Greenland stops being a claim in "
          "July of this year."),
         ("s04", "SVG_PLAGUE",
          "Figure 2 · What the state did, and what it could not count",
          "The upper panel is what can be established: a dated sequence of measures, from the "
          "Saltholm quarantine of 1709 to the reopening of the gates in April 1712. The lower "
          "panel is what cannot. Four published death tolls are shown disagreeing rather than "
          "averaged, against a city of about sixty thousand. The planned weekly burial curve is not drawn, because reference works "
          "differ by a factor of three or four on the same months and inventing weekly values "
          "for real deaths is the one place a plausible-looking figure would do most harm."),
         ("s08", "SVG_SCHOOLS",
          "Figure 3 · Two hundred and forty-one, 1722–27",
          "Twelve cavalry districts at twenty schools each were planned and two hundred and "
          "forty-one were built between 1722 and 1727, every one to the same drawing, the "
          "builders paid 550 to 600 rigsdaler for each. The plan of the standard building is "
          "drawn to scale."),],
 ),

 28: dict(
   file='c28_body.html',
   part='Part G', band='Absolutism', num=28, dates='1721 – 1770',
   title='The bound countryside and the pious state',
   people='Christian 6. · Frederik 5. · Erik Pontoppidan · Ludvig Holberg · Anders Pedersen',
   hook="For half a century the Danish state is at peace and its countrymen are not free. "
        "In 1733 the young men of the peasantry are tied to the estates where they were born, "
        "to solve a problem of army recruitment and a landowners' crisis at one stroke. At the "
        "same time a pietist king keeps the theatre shut, makes confirmation compulsory, and "
        "puts a book of seven hundred and fifty-nine questions into every parish in two "
        "kingdoms.",
   keys=['stavnsbånd 1733', 'hoveri', 'spanddag og gangdag', 'konfirmation 1736',
         'Pontoppidans katekismus 1737', 'skoleforordningen 1739', 'kvægpesten',
         'Herrnhuterne', 'Kongsberg', 'kornmonopolet 1735'],
   qs=["The <i class=\"dk\">stavnsbånd</i> of 1733 is usually explained as serfdom. What "
       "problem was it actually built to solve, and for whom?",
       "How much of a bound man's year belonged to somebody else, and why can we not say "
       "which days?",
       "Confirmation became compulsory in 1736 and the state was obliged to teach for it in "
       "1739. Why does that order matter?",
       "Norway kept its own law, its own coin and its own regiments. In what sense was it "
       "nonetheless being governed for Denmark's benefit?",
       "What did the cattle plague do to a countryside where a farm's value was already "
       "written down as a single number?"],
   figs=[("s04", "SVG_HOVYEAR",
          "Figure 1 · A bound man's year",
          "A schematic. Three hundred and sixty-five squares, one for each day, with the "
          "hundred and ten days of one commonly quoted reckoning for a Zealand tenant with a "
          "full holding marked: forty requiring a wagon and a team, seventy on foot, where a "
          "girl or a boy would do. The reckoning has not been traced here to the returns, and "
          "the unmarked squares include Sundays and holy days. Nor is this a calendar: the "
          "figure gives a total and a split, not dates, and drawing the days in particular "
          "months would invent the one thing a reader would take from it. What is agreed is "
          "that the demand fell hardest at ploughing, sowing and harvest — the only weeks when "
          "a man's own crop could not wait."),
         ("s07", "SVG_NORWAY",
          "Figure 2 · What Norway sent south",
          "Silver from Kongsberg, copper from Røros, Løkken and Folldal, timber, iron, "
          "regiments and carting duty. Kongsberg employed 4,075 people in 1770 and was "
          "Norway's largest mine, its town second in the country only to Bergen. What came "
          "the other way was Danish grain — and after 1735 southern Norway was meant to buy "
          "no other kind, though the ban was relaxed in bad years. Norway kept its own law, its own coin and its own regiments. It was not "
          "a colony. The metal still went south."),
         ("s02", "SVG_CATECHISM",
          "Figure 3 · Seven hundred and fifty-nine questions",
          "Pontoppidan's Sandhed til Gudfrygtighed of 1737, the required "
          "book for every child in two kingdoms: one square for each question and answer, "
          "every one of them to be had by heart before the public examination in front of "
          "the congregation. Prescribed by royal order in 1738 and required by law until "
          "1794; it is probably the book by a Danish author printed in more copies than any "
          "other."),],
 ),

 29: dict(
   file='c29_body.html',
   part='Part G', band='Absolutism', num=29, dates='1770 – 1788',
   title='Struensee, and the village taken apart',
   people='Christian 7. · J.F. Struensee · Caroline Mathilde · C.D.F. Reventlow · Hans Knudsen',
   hook="A German doctor governs Denmark for sixteen months through a king who cannot, "
        "issues more than a thousand cabinet orders, and is executed for it. The men who "
        "overthrow him rule the same way. Then, in the 1780s, the state takes the Danish "
        "village apart field by field and unties the bond of 1733 — and Copenhagen raises a "
        "column to the king for doing it while the last bound men are still waiting to be free.",
   keys=['kabinetsordrer', 'trykkefrihed 1770', 'indfødsretten 1776',
         'Den Store Landbokommission 1786', 'udskiftning', 'stjerneudskiftning',
         'udflytning', 'arvefæste', 'stavnsbåndets ophævelse 1788', 'Frihedsstøtten'],
   qs=["Struensee ruled by cabinet order through a sick king. Guldberg overthrew him and "
       "ruled by cabinet order through that king's guardians. What does that tell you about "
       "the constitution of 1665?",
       "What was <i class=\"dk\">udskiftning</i>, and why did it break up villages that had "
       "stood in one place since the Middle Ages?",
       "The ordinance of 20 June 1788 did three things at once. Name them, and say which one "
       "the monument commemorates.",
       "Who was left out of the reforms, and how many of the rural population were they?",
       "The Liberty Column is a true first told in a way that omits what it cost. What does "
       "it omit?"],
   figs=[("s07", "SVG_VILLAGE",
          "Figure 1 · One village, twice",
          "The same six households before and after. Before, every household held strips in "
          "all three open fields, so good land and bad were shared out and the risk with them "
          "— at the price that nobody could decide anything alone. After, each farmed one "
          "piece and could do as it liked with it; where the land would not take the wedge "
          "shape, the farmstead itself was pulled down and rebuilt out on its own ground. "
          "Both diagrams are schematic and are not a map of any particular village."),
         ("s08", "SVG_BAND",
          "Figure 2 · The bound years",
          "The ages at which a countryman could not leave the estate he was born on. The bond "
          "was imposed on 4 February 1733 for men of fourteen to thirty-six, widened to nine "
          "to forty in 1742 and four to forty in 1764. After the ordinance of 20 June 1788 "
          "nobody entered it: the wedge is the closed set of birth-years left bound, "
          "growing older year by year and released one birth-year a year until 1 January "
          "1800. Men discharged from service also went free, so the wedge is the most the rule "
          "could hold: it is drawn from the rule, not from a count of men."),
         ("s09", "SVG_COLUMN",
          "Figure 3 · What the column says",
          "*Frihedsstøtten* on Vesterbrogade, 1792–97: twenty metres of Bornholm sandstone, "
          "paid for by a collection among Copenhagen's citizens while the landowners were "
          "pushing back. The inscription is given here line by line with what each line leaves "
          "out. The king it credits was incapable; the free peasant it promises is the "
          "*gårdmand*, not the cottager; and the bond it says shall cease still held men when "
          "the column was finished."),],
 ),

 30: dict(
   file='c30_body.html',
   part='Part G', band='Absolutism', num=30, dates='1620 – 1803',
   title='The Danish Atlantic',
   people='Christian Runge · Breffu · Philip Gardelin · Heinrich Carl Schimmelmann · Ernst Schimmelmann',
   hook="Between 1658 and 1803 Denmark came to run forts on the Gold Coast, islands in the "
        "Caribbean and the ships between them. About a hundred and eleven thousand people were "
        "carried in Danish bottoms. In 1792 Denmark became the first slave-trading nation to "
        "decide to end its trade — with a ten-year delay written into the ordinance, during "
        "which Danish ships fetched more people from Africa than ever before.",
   keys=['Trankebar 1620', 'Christiansborg på Guldkysten', 'Sankt Thomas 1672',
         'Vestindisk-guineisk Kompagni', 'Sankt Jan 1733', 'Sankt Croix 1733',
         'Gardelins reglement', 'trekantshandelen', 'Fredensborg', 'forordningen af 16. marts 1792'],
   qs=["Danish ships ran the triangular trade from the 1660s to 1803. What were its three "
       "legs, and what went on each?",
       "The rising on St Jan in 1733 and the rising on Bornholm in 1658 are told very "
       "differently in Danish history. Why?",
       "What did the ordinance of 16 March 1792 actually order, and what happened in the ten "
       "years that followed?",
       "Why is the company's grid on St Croix so seldom set beside the Danish land surveys of "
       "1662 and 1681, and what does the comparison show?",
       "Of the slave ships found as wrecks, the <i class=\"dk\">Fredensborg</i> is the best "
       "documented. What do its papers record, and what do they not?"],
   figs=[("s03", "SVG_TRIANGLE",
          "Figure 1 · The triangle, weighed",
          "The triangle as the traders' books saw it: goods out, people across, sugar home. "
          "The legs are drawn by what they carried, not to scale. The figures at the foot count "
          "all Danish slave voyages from the 1660s to 1803, set against the whole Atlantic "
          "trade as the SlaveVoyages database estimates it for 1501–1866."),
         ("s06", "SVG_SURVEYS",
          "Figure 2 · The same habit, three times",
          "Three ways of writing land down: converting (1662–64), measuring (1681–83) and "
          "dividing (from 1734). The emblems are schematic. The lots on St Croix were each two "
          "thousand by three thousand Danish feet, a hundred and fifty of the island's acres, "
          "and the survey that fixed them ran on into the 1740s."),
         ("s04", "SVG_PAPERS",
          "Figure 3 · What the papers keep",
          "The *Fredensborg*'s papers, 1767–68, set beside what they leave "
          "out. The captain's journal and the assistant's protocol are in Rigsarkivet in "
          "Copenhagen and have been transcribed by KUBEN in Arendal, which also shows what "
          "divers raised from the wreck."),],
 ),

 31: dict(
   file='c31_body.html',
   part='Part G', band='Absolutism', num=31, dates='1784 – 1814',
   title='The flourishing trade and the wreck of it',
   people='Frederik 6. · Ernst Schimmelmann · Peter Willemoes · Kamma Rahbek · Edmund Bourke',
   hook="From the American war to 1807, neutrality makes Copenhagen rich carrying other "
        "people's cargo. Then the British take the fleet after three nights of bombardment, "
        "the state currency is written down to a sixth in a single ordinance, and Norway — "
        "more than four hundred years in the same realm — is signed away in one treaty at "
        "Kiel. In the same year Denmark orders "
        "seven years of school for every child in the country.",
   keys=['den florissante handelsperiode', 'væbnet neutralitet',
         'slaget på Reden 1801', 'Københavns bombardement 1807', 'kanonbådskrigen',
         'statsbankerotten 1813', 'rigsbankdaler', 'Kieltraktaten 1814',
         'Eidsvoll 1814', 'skoleloven 1814'],
   qs=["What was a neutral bottom worth between the American war and 1807, and why did "
       "that make Copenhagen rich?",
       "The British attacked a neutral country and took its fleet. On what argument — and "
       "what would Denmark have had to do to avoid it?",
       "The reform of 5 January 1813 is remembered as the state bankruptcy. Why is that name "
       "wrong, and what actually happened to people holding notes?",
       "Norway was ceded at Kiel and refused to go. What did the Norwegians do instead, and "
       "what did they keep?",
       "In the same year as Kiel, Denmark ordered seven years of school for every child. How "
       "does a state that has just written down its own money do that, and why then?"],
   figs=[("s05", "SVG_1807",
          "Figure 1 · August–September 1807",
          "They landed twenty kilometres up the coast and took three weeks. The ultimatum "
          "reached the crown prince on 6 August with the army in Holstein; British troops came "
          "ashore at Vedbæk on 16 August against almost no resistance; batteries went up in an "
          "arc round the city, and fire was opened at half past seven in the evening of "
          "2 September. Three nights, and the target was the city rather than the defences. "
          "Peymann capitulated on the 7th and the fleet sailed for England."),
         ("s06", "SVG_FLEET",
          "Figure 2 · What sailed away",
          "The prize of September 1807: forty-five hulls, each drawn as a mark sized by its "
          "rate, from the ships of the line down to the smaller craft. The naval stores that "
          "went with them are not drawn."),
         ("s07", "SVG_DALER",
          "Figure 3 · Six for one, 5 January 1813",
          "Six old *kurantdaler* notes exchanged for one new *rigsbankdaler*, against a note "
          "that had already fallen to about six per cent of face value in silver. The new "
          "issue was capped at forty-six million, and the ordinance says where all of it was "
          "to go: twenty-seven million to take in the old notes, the other nineteen million "
          "partly to lending and partly to a reserve fund for the state's extraordinary "
          "expenses."),],
 ),
 32: dict(
   file='c32_body.html',
   part='Part H', band='The national century', num=32, dates='1814 \u2013 1848',
   title='Golden Age and national awakening',
   people='Christian 8. \u00b7 N.F.S. Grundtvig \u00b7 Peter Larsen Skr\u00e6ppenborg \u00b7 '
          'Johanne Luise P\u00e4tges \u00b7 Peter Hiort Lorenzen \u00b7 Christian Flor',
   hook="A state that has just lost Norway and written its paper money down to a sixth "
        "hands control of its money to a bank it does not run, prosecutes farm servants for "
        "praying in the wrong room, and pays for the finest art it will ever produce. Then "
        "it concedes four assemblies, chosen, in the kingdom, by fewer than three people in a hundred and "
        "with no power at all \u2014 and in one of them a merchant from Haderslev stands up "
        "and speaks Danish.",
   keys=['guldalder', 'gudelige forsamlinger', 'Konventikelplakaten', 'Nationalbanken',
         'st\u00e6nderforsamling', 'hartkorn', 'kornsalgsperioden',
         'Bondevennernes Selskab', 'sprogreskript', 'sprogpatent',
         'slesvig-holstenisme', 'Ejderpolitik', 'folkeh\u00f8jskole', 'Det \u00e5bne Brev'],
   qs=["Denmark traded Swedish Pomerania to Prussia for Lauenburg in 1815 and took cash as "
       "well. Why was the smaller duchy worth more than the larger province?",
       "An absolute monarchy gave away control of its currency in 1818 and control of "
       "nothing else. What was it buying, and from whom?",
       "The Konventikelplakat and the Bondecirkul\u00e6re were both used to stop people "
       "organising, and both failed the same way. What was the mistake they shared?",
       "The Golden Age was paid for by a state that had just written down its own paper "
       "money. Does that explain the art, or merely accompany it?",
       "Christian 8.'s Open Letter of 1846 was meant to settle the succession. Why did it "
       "leave both national movements angrier than it found them?"],
   figs=[("s01", "SVG_TERR_1814",
          "Figure 1 \u00b7 The realm after Kiel",
          "Norway is gone. What is left includes two duchies \u2014 Holstein, and Lauenburg "
          "from 1815 \u2014 that are simultaneously member states of the German "
          "Confederation, whose northern limit is the Eider. The line across the bottom of "
          "this map is the whole of Part H's problem."),
         ("s06", "SVG_ASSEMBLIES",
          "Figure 2 \u00b7 Four assemblies, 1834",
          "Seats and franchise from the four decrees of 15 May 1834. Two Danish bodies and "
          "two German ones, with the same powers and no power. In the kingdom just under three "
          "people in a hundred could vote; women could not, whatever they owned, and only "
          "Christians could be elected: Jews could vote in the kingdom but not in the duchies."),
         ("s07", "SVG_RYE",
          "Figure 3 \u00b7 A quarter to a third of what it had been",
          "The collapse of 1818\u201328 and the recovery after it, drawn from the ratio the "
          "sources state and one estate's two sale prices rather than from an annual price "
          "line. The continuous "
          "Zealand kapitelstakst for rye exists in print from 1651; its year-by-year values "
          "were not obtained, and the figure says so instead of estimating them.")],
 ),

 33: dict(
   file='c33_body.html',
   part='Part H', band='The national century', num=33, dates='1848 \u2013 1852',
   title='1848: constitution and the First Schleswig War',
   people='Frederik 7. \u00b7 Orla Lehmann \u00b7 D.G. Monrad \u00b7 Wilhelm Beseler \u00b7 '
          'Mathilde Fibiger \u00b7 A.D. Cohen',
   hook="A king dies leaving no heir and a succession that Danish and German law answer "
        "differently. By the end of March absolutism has ended in Copenhagen without a shot, "
        "a provisional government has taken a fortress by railway timetable, and the two "
        "halves of the monarchy are at war. Denmark wins the war. The peace is written in "
        "London, and it is the trap that 1864 springs.",
   keys=['helstat', 'forfatningsreskriptet 28. januar 1848', 'Casinom\u00f8det',
         'Martsministeriet', 'provisorisk regering', 'tre\u00e5rskrigen',
         'l\u00e6gdsrulle', 'almindelig v\u00e6rnepligt 1849', 'Grundloven 1849',
         'de syv F-er', 'folkekirke', 'Isted 1850', 'Londontraktaten 1852'],
   qs=["Christian 8. left three instructions and no grandson. Which of the three could not "
       "be carried out, and what did that do to the monarchy?",
       "Schleswig and Holstein were held by the same man under two different legal orders. "
       "What were they, and why did a childless king make the difference fatal?",
       "The meeting that ended Danish absolutism was called on a report of a rising that "
       "had not yet begun. Does that change what happened in March 1848?",
       "Before 1849 the army was recruited from one class. What changed, where exactly was "
       "the line drawn, and what could a man still buy his way out of?",
       "Denmark won the great battles against the Schleswig-Holsteiners and lost every "
       "point in the settlement. Who decided the peace, and what did they require in "
       "writing?"],
   figs=[("s02", "SVG_DESCENT",
          "Figure 1 \u00b7 Two laws, one king, and a column nobody could fill",
          "The succession as it stood when Frederik 7. came to the throne. The kingdom "
          "follows the Kongelov of 1665, which is agnatic but opens the female line when "
          "the male line fails; Holstein follows an agnatic law with no such opening, which "
          "carries it to Augustenborg. Schleswig's column is empty, because the incorporation "
          "of 1721 was carried through without introducing the kingdom's law. The blank is "
          "the argument, and the Treaty of London filled it by choosing a third rule."),
         ("s02", "SVG_SPROG",
          "Figure 2 \u00b7 How many Danes were there in Schleswig?",
          "P.C. Koch's own count of 1839, from the legend of his language map of the duchy "
          "\u2014 published by a Danish partisan as an answer to Franz Geerz's German map of "
          "the year before. Koch did not count Danes and Germans. He counted the language "
          "of the kitchen against the language of the church and the school, and three of "
          "his six categories are people who spoke Danish at home and heard German on "
          "Sunday. The answer to the title is 33, 43 or 57 per cent depending where the "
          "line is drawn \u2014 which is why both sides drew their own."),
         ("s06", "SVG_FRANCHISE",
          "Figure 3 \u00b7 Who could vote in 1849",
          "Counted figures in solid tone, published proportions in outline, so the two are "
          "not confused. The 1850 census and the returns of the first Folketing election are "
          "counts; the 15 per cent of the population and 72.8 per cent of men over thirty "
          "are published ratios. In forty-three of the hundred seats no ballot was held.")],
 ),

 34: dict(
   file='c34_body.html',
   part='Part H', band='The national century', num=34, dates='1863 \u2013 1864',
   title='1864',
   people='Christian 9. \u00b7 D.G. Monrad \u00b7 C.J. de Meza \u00b7 Otto von Bismarck \u00b7 '
          'Niels Kjeldsen \u00b7 J.B.S. Estrup',
   hook="A king three days on the throne signs a constitution he knows breaks the promise "
        "made beside the treaty that made him king. Within a year Denmark has lost the duchies, the army that "
        "abandoned an indefensible rampart has been vilified for saving itself, and the "
        "bronze lion over the graves at Flensburg has been taken down. The bill for the second loss is paid at home, in 1866, by Danes.",
   keys=['Novemberforfatningen 1863', 'forbundseksekution', 'Dannevirke',
         'skanserne ved Dybb\u00f8l', 'Helgoland 9. maj 1864', 'Londonkonferencen',
         'Als 29. juni 1864', 'Wienerfreden', 'optanter', 'Pragfredens artikel 5',
         'Den gennemsete Grundlov 1866', 'privilegeret valgret', 'Hedeselskabet'],
   qs=["Christian 9. owed his throne to the Treaty of London and his first act broke the "
       "undertaking that came with it. "
       "Why did he sign, and what did he think would happen?",
       "In 1848 Russia made Prussia take its troops out of Jutland. In 1864 "
       "nobody did. What changed between those two wars \u2014 and whose doing was it?",
       "The general who abandoned the Dannevirke was destroyed for it and had been "
       "following his written orders. Who needed him blamed?",
       "Denmark won the fleet action off Heligoland in May 1864. Why did it not matter?",
       "Denmark lost territory to Prussia and Austria in October 1864 and lost the "
       "franchise of its upper house in July 1866. Which loss shaped the next forty years?"],
   figs=[("s07", "SVG_TERR_1864",
          "Figure 1 \u00b7 The realm after Vienna",
          "The frontier of 30 October 1864, on the same frame and projection as every other "
          "map in this series. Schleswig, Holstein and Lauenburg are renounced to two monarchs "
          "personally; the Konge\u00e5, the old line between kingdom and duchy, becomes a "
          "state border. The exchanges ran both ways: the royal enclaves south of it were "
          "ceded with the duchies, all but Ribe Herred, and a string of border parishes "
          "south of Kolding and \u00c6r\u00f8 came north."),
         ("s04", "SVG_DYBBOL",
          "Figure 2 \u00b7 What fell on the redoubts",
          "The bombardment record for the Dybb\u00f8l position, and four Danish reference "
          "returns for 18 April, drawn side by side because they do not count the same "
          "things. The shell counts are attested; the returns differ chiefly in what they "
          "count as a loss, and this figure shows the disagreement rather than choosing or "
          "averaging."),
         ("s08", "SVG_CEDED",
          "Figure 3 \u00b7 Counted, and disputed",
          "What Denmark lost in 1864, separating the figures Danmarks Statistik computed "
          "from the ones the sources argue about. The populations of the territories "
          "exchanged under the treaty are exact at the 1860 census. The share of area, the "
          "share of population and the number of Danish-speakers ceded are not, and are "
          "drawn as the ranges the sources actually give.")],
 ),

 35: dict(
   file='c35_body.html',
   part='Part H', band='The national century', num=35, dates='c. 1870 \u2013 1901',
   title='Industry, cooperatives, emigration and labour',
   people='Niels Hansen Uhd \u00b7 Vilhelm Beck \u00b7 Louis Pio \u00b7 Olivia Nielsen \u00b7 '
          'Ernst Matthias von K\u00f6ller',
   hook="Grain stops paying, and a parish in west Jutland answers it by writing a "
        "constitution: deliver everything, be paid alike for it, let the general meeting "
        "decide, and stand behind your neighbours' debts with all you own. By 1894 more "
        "than nine hundred dairies run on rules like those. The people they did "
        "not admit went to Nebraska, or to N\u00f8rrebro.",
   keys=['andelsbevægelsen', 'andelsmejeri', 'Hjedding 1882', 'centrifuge',
         'brugsforening', 'husmand', 'tyende', 'Indre Mission', 'forsamlingshus',
         'udvandringen', 'Slaget p\u00e5 F\u00e6lleden 1872', 'Septemberforliget 1899',
         'optanter', 'de hjeml\u00f8se', 'K\u00f8llerpolitikken'],
   qs=["Grain prices fell all over Europe. Why did Denmark answer with cooperatives when "
       "countries with the same problem did not?",
       "The cooperative dairies came to give every member one vote regardless of his herd. "
       "Who was not a member, and why could they not be?",
       "In the same parishes, the dairy ran on the vote of its general meeting and the "
       "mission house belonged to an association that refused its own members a vote. "
       "How did both come out of one revival?",
       "More than four in ten Danish emigrants were farm labourers. What does that say "
       "about the cooperative story told beside it?",
       "A movement whose leaders were sent to prison after 1872 signed an agreement with "
       "the employers in 1899 whose principles still hold. What happened in between?"],
   figs=[("s02", "SVG_OMLAEGNING",
          "Figure 1 \u00b7 Why Danish farming turned round",
          "The chain from falling grain prices to butter sold in England, with the dates "
          "the sources give and the two outside events that set the timing: the continuous "
          "separator at the end of the 1870s, and Germany closing its border to live Danish "
          "cattle in 1881. Drawn as a chain rather than as the two crossing price lines the "
          "plan asked for \u2014 see the note in figs_35.py."),
         ("s06", "SVG_UDVANDRING",
          "Figure 2 \u00b7 Who left",
          "The composition of Danish overseas emigration, 1868\u20131900, with the two "
          "points in the year-by-year series that could be attested and Denmark's share of "
          "Scandinavian emigration. The occupations are the argument: the people leaving "
          "were not the people founding the dairies of figure 1."),
         ("s03", "SVG_ANDEL",
          "Figure 3 \u00b7 How a cooperative was owned",
          "The four rules of the Hjedding contract of 1882 and what each of them did, "
          "including the one usually left out. Unlimited joint liability is what let "
          "farmers with no capital buy a steam engine, and it is also what fixed the "
          "boundary of the membership.")],
 ),

 37: dict(
   file='c37_body.html',
   part='Part I', band='The small state', num=37, dates='1901 \u2013 1917',
   title='Reform, neutrality and the sale of the West Indies',
   people='P.A. Alberti \u00b7 C.Th. Zahle \u00b7 Jutta Bojsen-M\u00f8ller \u00b7 '
          'Kresten Andresen \u00b7 D. Hamilton Jackson',
   hook="The change of system altered no word of the constitution. Within seven years the "
        "man who embodied it had stolen fifteen million kroner and walked to a police "
        "station to say so, and the system survived him. Then a constitution admitted two "
        "of the seven groups it had excluded for sixty-six years, a neutral country mined "
        "its own straits at Germany's request, and thirty-seven per cent of Danes voted to "
        "sell twenty-seven thousand people who had no vote at all.",
   keys=['Systemskiftet', 'Det Radikale Venstre', 'Alberti', 'Retsplejeloven 1908',
         'de syv F\u2019er', 'Grundloven 1915', 'Augustlovene', 'minerne i B\u00e6lterne',
         'gullaschbaroner', 'Arbejdsregulativet 1849', 'Fireburn 1878',
         'folkeafstemningen 1916'],
   qs=["The constitution of 1915 is called the introduction of universal suffrage. How "
       "many of the seven excluded categories did it actually admit?",
       "The Landsting had to vote away the privileged franchise that made it powerful. "
       "What made that rational for the men voting?",
       "Denmark laid mines against Britain at Germany's request and Britain did not treat "
       "it as an act of war. Why not?",
       "Denmark grew rich on neutrality and one civilian trade lost seven per cent of its "
       "men. How are both consequences of the same policy?",
       "Who freed the enslaved of the Danish West Indies in 1848, and why is the usual "
       "Danish answer wrong?"],
   figs=[("s05", "SVG_SYVF",
          "Figure 1 \u00b7 The seven categories, and the year each was let in",
          "The groups the franchise of 1849 excluded, with the year each was admitted. "
          "Five dates are exact, one disqualification lapsed without a franchise act, and "
          "two categories are still excluded. Not the before-and-after electorate the plan "
          "asked for; see the note in figs_37.py."),
         ("s07", "SVG_SOEFOLK",
          "Figure 2 \u00b7 The price of a neutral flag, 1914\u201318",
          "Danish merchant seamen against the size of the merchant service: 702 dead of "
          "about ten thousand, one man in fourteen, in a country where nobody was "
          "conscripted and no foreign soldier crossed the border. Ships lost are not drawn "
          "and the figure says why."),
         ("s09", "SVG_AFSTEMNING",
          "Figure 3 \u00b7 14 December 1916, and the people it was about",
          "The referendum on selling the Danish West Indies: those who voted to sell, "
          "those who voted not to, the larger number who did not vote at all, and beside "
          "them the 27,086 inhabitants of the islands, who had no vote. The abstainers "
          "outnumber the islanders about twenty-seven to one.")],
 ),
 36: dict(
   file='c36_body.html',
   part='Part H', band='The national century', num=36, dates='1875 \u2013 1901',
   title='Provisorietiden and the change of system',
   coda_part='Part H', coda_span='1814 \u2013 1901',
   people='J.B.S. Estrup \u00b7 Christian 9. \u00b7 Julius Rasmussen \u00b7 Line Luplau \u00b7 '
          'J.C. Christensen',
   hook="The constitution of 1849 never said whether a government answers to the king or "
        "to the elected chamber. For nineteen years two sides read that silence differently; "
        "for nine of them Denmark was governed on emergency decrees, with a military police force in "
        "its villages and a fortress going up round its capital that would never be fired. "
        "The rule that settled it was not written down until 1953.",
   keys=['H\u00f8jre og Venstre', 'parlamentarisme', 'provisorisk lov', 'finanslov',
         'grundlovens § 25', 'visnepolitikken', 'Provisorietiden', 'Riffelloven 1885',
         'gendarmerne', 'Vestvolden', 'Forliget 1894', 'Systemskiftet 1901'],
   qs=["The 1849 constitution is silent about who a ministry answers to. How did two "
       "honest readings of that silence produce nineteen years of conflict?",
       "The Folketing formally rejected the provisional finance law in January 1886 and "
       "nothing at all happened. Why not?",
       "Venstre spent years voting down expenditure to starve the government. What did "
       "that do to the treasury, and why does it change what the fight was about?",
       "One man fired two shots at Estrup in 1885. Why did everything that followed help "
       "Estrup?",
       "Denmark got parliamentary government in 1901 and did not write it into the "
       "constitution until 1953. What held it in place from 1901 to 1953?"],
   figs=[("s01", "SVG_FRANCHISES",
          "Figure 1 \u00b7 Two chambers, two electorates",
          "The Folketing and the Landsting side by side as the electoral laws left them "
          "after 1866: universal manhood suffrage on one side, and on the other a chamber "
          "of sixty-six in which twelve were appointed by the king for life and half the "
          "electors who chose the rest were themselves chosen by the highest taxpayers "
          "alone. The chapter's central fact in one image."),
         ("s02", "SVG_DEADLOCK",
          "Figure 2 \u00b7 What each chamber could do, and what nobody could do",
          "The deadlock drawn as a structure rather than as a quarrel between two sides: "
          "what the Folketing could do, what the Landsting could do, what the king could "
          "do \u2014 and the empty box, which is the procedure the constitution did not "
          "contain for settling a disagreement between them."),
         ("s06", "SVG_VESTVOLD",
          "Figure 3 \u00b7 The rampart the constitution was broken for",
          "The Vestvold in quantities: fourteen kilometres from Utterslev Mose "
          "to K\u00f8ge Bugt, built 1888\u201392, some 3.15 million cubic metres of earth "
          "and chalk moved by about two thousand men with shovels and wheelbarrows. Never "
          "fired in anger; abolished in 1920.")],
 ),
 38: dict(
   file='c38_body.html',
   part='Part I', band='The small state', num=38, dates='1918 \u2013 1920',
   title='Genforeningen, Iceland and the Easter Crisis',
   people='H.P. Hanssen \u00b7 H.V. Clausen \u00b7 Ernst Christiansen \u00b7 '
          'Christian 10. \u00b7 Johanne Marie Braren',
   hook="In one year Denmark let Iceland go by agreement, got a border by asking the "
        "people where it should be, and very nearly lost its monarchy over the part of "
        "the answer it did not like. The border it got runs within a few kilometres of a "
        "line a Copenhagen schoolmaster had walked out on foot thirty years earlier. The "
        "king who objected to it dismissed a government with a majority, and gave way in "
        "three days to a strike that was called and never struck.",
   keys=['Forbundsloven 1918', 'Versaillestraktaten \u00a7\u00a7109\u2013114',
         'Aabenraa-resolutionen', 'Clausen-linjen', 'zone 1 og zone 2',
         'afstemningen 10. februar 1920', 'afstemningen 14. marts 1920',
         'Den Internationale Kommission', 'P\u00e5skekrisen', 'Genforeningen',
         'hjemmetyskere', 'de hjeml\u00f8se'],
   qs=["Iceland left by agreement and Norway left by treaty after a lost war. What had "
       "changed in Denmark between 1814 and 1918 to make the difference?",
       "Denmark could plausibly have claimed as far south as the Danevirke and asked for "
       "less. Give the reason that is about the previous four hundred years.",
       "Zone 1 voted en bloc and Zone 2 commune by commune. Show how that one asymmetry "
       "settled the border before a vote was cast.",
       "About 25,000 people in Zone 1 voted German and became Danish anyway. What is the "
       "argument that this was right, and what is the argument against it?",
       "The king dismissed a ministry that had a majority, and the constitution of 1866 "
       "allowed it. What stopped him, and where is that rule written down?"],
   figs=[("s02", "SVG_FORBUND",
          "Figure 1 \u00b7 The Act of Union, 1 December 1918",
          "What Iceland gained, what Denmark kept, and the clock the act carries: "
          "revision on demand after 1940, and termination three years later by "
          "two-thirds vote confirmed by referendum. The only constitutional settlement "
          "in this book that specifies how to undo itself."),
         ("s06", "SVG_ZONER",
          "Figure 2 \u00b7 The two zones, 1920",
          "Zone 1, counted whole on 10 February, and Zone 2, counted commune by commune "
          "on 14 March. One red line is both the zone boundary and the border, which is "
          "the argument. Four German-voting towns sit inside the zone that went to "
          "Denmark. Not drawn parish by parish, and the figure says why."),
         ("s09", "SVG_AAR",
          "Figure 3 \u00b7 1920",
          "The year on one axis: two plebiscites, a dismissed ministry, a general strike "
          "called and not struck, a border, a king on a horse, a referendum, and three "
          "general elections held for three different constitutional reasons. Party "
          "totals are deliberately absent; see the note in figs_38.py.")],
 ),
 39: dict(
   file='c39_body.html',
   part='Part I', band='The small state', num=39, dates='1920 \u2013 1929',
   title='Deflation, the Landmandsbank crash and the first Social Democratic government',
   people='Emil Glückstadt \u00b7 Holmer Green \u00b7 Thorvald Stauning \u00b7 Nina Bang \u00b7 '
          'K.K. Steincke \u00b7 Peter Munch',
   hook="The war boom ended in 1920, and for the next thirty-three years unemployment "
        "never fell below eight per cent. Two years later the largest bank in Scandinavia "
        "was rescued twice, after two ministers had kept their own inspector's figure "
        "quiet. In 1924 "
        "the party that had entered the Folketing with two seats formed a government on a "
        "majority of one, and fell over the price of making the krone worth what it had "
        "been before the war.",
   keys=['lavkonjunkturen 1920', 'Udligningskassen for Sønderjylland', 'postskillemønt',
         'Landmandsbanken 1922', 'Bankkommissionen af 1922', 'statsgarantien 1923',
         'hærordningen 1922', 'Stauning I 1924', 'Nina Bang', 'Fremtidens Forsørgelsesvæsen',
         'steriliseringsloven 1929', 'guldindløseligheden 1927'],
   qs=["Sønderjylland joined the kingdom without its marks being exchanged. Why did that "
       "make the German inflation the new province's problem?",
       "Two ministers stood behind a bank's own figure against their inspector's. What did "
       "they fear, and what did it cost?",
       "Denmark's army was cut to a border guard with the Rigsdag's broad agreement. Was that "
       "realism or a failure of nerve?",
       "The first Social Democratic government rested on a majority of one. What could it do "
       "with that, and what could it not?",
       "Everyone agreed the krone should go back to its old gold value. Who paid for "
       "agreeing?"],
   figs=[("s02", "SVG_KAPSLER",
          "Figure 1 \u00b7 Small change in a capsule, 1921\u201322",
          "Postage stamps sealed in iron and celluloid and used as coins in the new province: "
          "how many of each value went out, how many came back, and where the four market "
          "towns stood. About a quarter were never handed back. One source, whose counts and "
          "totals agree to the øre."),
         ("s03", "SVG_KRAK",
          "Figure 2 \u00b7 Two rescues and a guarantee, 1922\u201323",
          "Landmandsbanken from the inspector's secret review to the final settlement. Every "
          "date is confirmed twice. The loss estimates and the split of the new capital are "
          "left in the text, because each rests on a single account."),
         ("s06", "SVG_TING",
          "Figure 3 \u00b7 The Folketing of 11 April 1924",
          "One square a seat. Social Democrats and Radicals together fill the first three "
          "rows, seventy-five of 149, which is a majority of one. Forty years earlier the "
          "Social Democrats had two.")],
 ),
 40: dict(
   file='c40_body.html',
   part='Part I', band='The small state', num=40, dates='1929 \u2013 1939',
   title='Depression, Stauning and the seeds of the welfare state',
   people='Thorvald Stauning \u00b7 K.K. Steincke \u00b7 Augusta Erichsen \u00b7 '
          'Thomas Madsen-Mygdal \u00b7 Peter Munch \u00b7 Frits Clausen',
   hook="Denmark met the depression through the price of bacon in Britain. One night in "
        "January 1933, in the prime minister's flat, three parties traded a devaluation "
        "for a social reform and called off a lockout of a hundred thousand men. The "
        "reform did not give the poor back the vote: it redefined them out of the clause "
        "that took it. And in 1939 a proposal that nine voters in ten approved of failed, "
        "because only half of them came.",
   keys=['Kanslergadeforliget 1933', 'devalueringen 1933', 'Lov om offentlig Forsorg 1933',
         'socialreformen 1933', 'fattighjælp og valgret', 'aandssvageloven 1934',
         'Påskeblæsten 1933', 'Slesvigsk Parti', 'Østgrønlandssagen 1933',
         'Stauning eller kaos 1935', 'landstingsvalget 1936', 'DNSAP',
         'folkeafstemningen 23. maj 1939'],
   qs=["A lockout of a hundred thousand men was called off by statute. What else did that "
       "statute suspend, and who had spent thirty-four years insisting it never should?",
       "The social reform of 1933 did not amend the constitution. How did it give most "
       "recipients of public help their vote back without doing so?",
       "Steincke wrote the principle that help should cost a man nothing, and the law that "
       "sterilised the people it did not cover. Were those one idea or two?",
       "A border settled by plebiscite in 1920 was challenged in 1933 by a campaign of "
       "newspapers. What did Denmark do about it, and what did that cost or save?",
       "Nine voters in ten approved the constitutional reform of 1939 and it failed. "
       "Explain the rule that defeated it."],
   figs=[("s03", "SVG_KANSLERGADE",
          "Figure 1 \u00b7 What was in Kanslergade, 29\u201330 January 1933",
          "Three parties, what each arrived wanting, what each signed for, and what each "
          "gave up to get it. A schematic: no quantity is drawn that the text does not "
          "carry. The Conservatives were not in the room."),
         ("s04", "SVG_KURS",
          "Figure 2 \u00b7 The pound in kroner, January 1933",
          "The rate before the agreement is drawn as a band rather than a point, because "
          "the two accounts of it differ. Every percentage is computed from the rates, and "
          "none of the published percentages matches them, which is why the figure gives "
          "the rates instead."),
         ("s11", "SVG_REGEL",
          "Figure 3 \u00b7 23 May 1939: the rule that counted silence",
          "The whole electorate as one bar rather than the votes cast. Of those who voted, "
          "91.85 per cent said yes; measured against everyone entitled to vote it was "
          "44.5, and the constitution of 1915 required 45.")],
 ),
 41: dict(
   file='c41_body.html',
   part='Part I', band='The small state', num=41, dates='1939 \u2013 1943',
   title='9 April 1940 and samarbejdspolitikken',
   people='Peter Munch \u00b7 Erik Scavenius \u00b7 Carl Gunnar J\u00f8rgensen \u00b7 '
          'Kate Fleron \u00b7 Henrik Kauffmann \u00b7 Christian 10.',
   hook="Denmark signed a non-aggression pact with Germany in May 1939 and was invaded "
        "314 days later. The fighting lasted four hours and a quarter and the decision "
        "took one hour and forty-five minutes of it. What followed was three years in "
        "which a Danish parliament passed a retroactive law so that its own police could "
        "keep the men they had already arrested, and a Danish ministry promised the men "
        "going to the Eastern Front their jobs back.",
   keys=['ikke-angrebspagten 1939', 'advarslerne 1940', '9. april 1940',
         'Lundtoftbjerg', 'samarbejdspolitikken', 'Kauffmann-traktaten 1941',
         'alsang 1940', 'clearingkontoen', 'kommunistloven 1941',
         'Frikorps Danmark', 'Antikominternpagten 1941', 'telegramkrisen 1942',
         'folketingsvalget 23. marts 1943'],
   qs=["A government was told five days in advance, by a German officer, that it was "
       "about to be invaded, and did nothing. What was the argument for doing nothing, "
       "and whose argument was it?",
       "Sixteen Danes were killed on 9 April 1940. How many of them were soldiers, and "
       "why does almost every account get this wrong?",
       "Danish police arrested Danish communists in June 1941 with no law to do it under. "
       "What did the Rigsdag do about that two months later?",
       "The realm came apart in the North Atlantic in the thirteen months after 9 April "
       "1940. Name the three territories and the three different ways they went.",
       "Turnout in March 1943 was the highest at any Danish general election and the Danish Nazi party "
       "kept its three seats on a larger vote than in 1939. Explain both facts at once."],
   figs=[("s03", "SVG_MORGEN",
          "Figure 1 \u00b7 9 April 1940, hour by hour",
          "A time axis in minutes. Every duration printed on it is computed from the clock "
          "times, including the four hours and a quarter of fighting and the hour and "
          "three-quarters in which the decision was taken."),
         ("s08", "SVG_UDLEVERET",
          "Figure 2 \u00b7 Who was handed over, 1941 \u2013 1943",
          "Four different kinds of quantity on one scale and deliberately not one cohort: "
          "one day's arrests, a stock on the date the law was passed, a flow through a "
          "camp over two years, and one transport. The divergence between two sources on "
          "the first of them is drawn rather than averaged away."),
         ("s11", "SVG_VALG",
          "Figure 3 \u00b7 23 March 1943: the whole electorate as one bar",
          "The same denominator chapter 40 used for the referendum of 1939, where the yes "
          "vote reached 44.46 per cent of it and needed 45. Here turnout is 89.5 and the "
          "Danish Nazi party is the segment a swatch is needed to find.")],
 ),
 42: dict(
   file='c42_body.html',
   part='Part I', band='The small state', num=42, dates='1943',
   title='1943: the year the policy broke',
   people='Werner Best \u00b7 Georg Ferdinand Duckwitz \u00b7 Ellen Wilhelmine Nielsen \u00b7 '
          'Paul Aron Sandfort \u00b7 Vice Admiral Vedel \u00b7 Christian 10.',
   hook="The cooperation policy was ratified in March 1943 by the largest turnout in "
        "Danish history and was finished by the end of August, and what broke it was a "
        "strike. Three weeks after the government stopped functioning the occupier moved "
        "against the Jews of Denmark, on the stated ground that there was no longer a "
        "government to lose. Most of them were across the Sound within a fortnight, and "
        "the year ended with a council nobody had elected claiming to speak for the "
        "country.",
   keys=['augustopr\u00f8ret 1943', '29. august 1943', 'fl\u00e5dens s\u00e6nkning',
         'departementschefstyret', 'j\u00f8deaktionen 1943', 'Theresienstadt',
         'Horser\u00f8d og Stutthof', 'Danmarks Frihedsr\u00e5d'],
   qs=["The German ultimatum of 28 August 1943 made one demand that was about Danes "
       "rather than about Germans. What was it, and what would signing it have committed "
       "the Danish state to?",
       "Why did the occupier leave Denmark's Jews alone for three and a half years, and "
       "what changed in September 1943? Use Best's own argument.",
       "Four hundred and seventy-two people were deported and about seven thousand "
       "crossed to Sweden. Which of those two numbers is a count and which is an "
       "estimate, and how can you tell?",
       "Christian 10. declined to sign his government's resignation. What did that deny "
       "the occupier, and what did it cost?",
       "What was Danmarks Frihedsr\u00e5d, who recognised it, and what did it have "
       "instead of a mandate?"],
   figs=[("s04", "SVG_OKTOBER",
          "Figure 1 \u00b7 October 1943: to Sweden, to Theresienstadt, and the difference",
          "An estimate and a count, drawn differently on purpose. The 472 is a nominal "
          "count from the transport registration lists and is drawn filled; the crossing "
          "to Sweden is an estimate and is drawn open, with the range in circulation as a "
          "whisker. The spread on the larger number is wider than the whole of the "
          "smaller one.")],
 ),
 43: dict(
   file='c43_body.html',
   part='Part I', band='The small state', num=43, dates='1943 \u2013 1945',
   title='The underground and the liberation',
   people='Monica Wichfeld \u00b7 Kim Malthe-Bruun \u00b7 Kaj Munk \u00b7 '
          'Kristian L. Rasmussen \u00b7 G\u00fcnther Pancke \u00b7 Mogens Fog',
   hook="The resistance had no weapons in 1943 and about sixty thousand armed people by "
        "May 1945, and every gun came from outside. What it did with them was mostly not "
        "fight: it blew up factories and railways, absorbed a counter-terror aimed at "
        "prominent Danes rather than at saboteurs, stopped the capital for a fortnight "
        "over a curfew, and then waited. In September 1944 the occupier deported the "
        "Danish police and handed the underground five thousand trained men.",
   keys=['SOE og nedkastningerne', 'ventegrupper', 'Hvidstengruppen',
         'clearingmord', 'schalburgtage', 'folkestrejken 1944',
         'politiaktionen 19. september 1944', 'vagtv\u00e6rn', 'Shellhuset',
         'Bornholm, maj 1945'],
   qs=["Where did the Danish resistance's weapons come from, and what did delivering "
       "them cost the air forces that dropped them?",
       "What was a clearingmord, where does the word come from, and how did the occupier "
       "make Danish newspapers reinforce it?",
       "What did the People's Strike of June 1944 obtain, and what did it demonstrate "
       "that was not among its demands?",
       "The Danish police were deported in September 1944. Why, on the occupier's own "
       "reasoning, and what did it hand the resistance?",
       "Ten Danes were killed when 387 buildings were destroyed in R\u00f8nne and Nex\u00f8 "
       "on 7 and 8 May 1945. Explain the number."],
   figs=[("s02", "SVG_SABOTAGE",
          "Figure 1 \u00b7 Sabotage by year, 1940 \u2013 1945",
          "The annual series, because no monthly one is reachable. The 1945 column is "
          "four months. The industrial column adds to its own published total exactly and "
          "the railway column overshoots its own by one, which is marked on the figure "
          "rather than averaged away."),
         ("s03", "SVG_FOLKESTREJKE",
          "Figure 2 \u00b7 The People's Strike, 22 June \u2013 5 July 1944",
          "An axis in days. The two dates the sources do not agree on \u2014 when the "
          "curfew was imposed and when the city went back to work \u2014 are drawn as "
          "bands rather than ticks.")],
 ),
 44: dict(
   file='c44_body.html',
   part='Part I', band='The small state', num=44, dates='1944 \u2013 1948',
   coda_part='Part I', coda_span='1901 \u2013 1955',
   title='The reckoning, and the accounts',
   people='Flemming Helweg-Larsen \u00b7 Anna Lund Lorentzen \u00b7 Fanny Jensen \u00b7 '
          'Hal Koch \u00b7 Carl Madsen \u00b7 Knud Kristensen',
   hook="The reckoning began before the law did. An organisation with no legal existence "
        "arrested about twenty-two thousand people in eight days, and two in three of "
        "them turned out to be chargeable with nothing; the statute to try them under was "
        "passed three weeks later and reached back five years. Forty-six men were shot. "
        "Seventy-five went to prison for building the German war. Then Denmark totted up "
        "what the occupation had actually cost, and somebody else paid it.",
   keys=['retsopg\u00f8ret', 'straffelovstill\u00e6gget 1945',
         'd\u00f8dsstraffens genindf\u00f8relse', 'v\u00e6rnemagersagerne',
         'tyskerpiger', 'Bornholm 1945-46', 'Sydslesvig efter 1945',
         'Marshallhj\u00e6lpen', 'Islands l\u00f8srivelse 1944',
         'den f\u00e6r\u00f8ske folkeafstemning 1946'],
   qs=["The law under which Denmark tried collaborators was passed after most of the "
       "arrests had been made. What did it reach back to, and what did it exempt?",
       "Forty-six men were executed and seventy-five people went to prison for a year or "
       "more for building for the Wehrmacht. Explain the difference using the statute.",
       "Why can nobody say to within ten thousand how many people were interned in "
       "Denmark in May 1945?",
       "On what condition did the Soviet Union leave Bornholm in 1946, and how did Danish "
       "governments read that condition afterwards?",
       "Denmark declined a frontier further south in 1946. Was that the first time a "
       "Danish government refused territory it could have had?"],
   figs=[("s03", "SVG_DOMME",
          "Figure 1 \u00b7 What the 13,521 convictions were for",
          "The official table at final instance, by category, with the women's share "
          "drawn inside each bar. Service in the German forces is more than half of the "
          "whole reckoning. Informing is 413 convictions in the entire country, which is "
          "the figure \u00a704 needs and the one usually misquoted."),
         ("s05", "SVG_BORNHOLM",
          "Figure 2 \u00b7 Bornholm: occupied 335 days longer",
          "Two bars on one axis in days, computed from the dates rather than from any "
          "source's rounding. The mainland's occupation ran 1,852 days; Bornholm's ran "
          "2,187, of which the last 331 were Soviet. The gap between the Danish request "
          "and the Soviet departure is 32 days, and is marked."),
         ("s06", "SVG_SYDSLESVIG",
          "Figure 3 \u00b7 South Schleswig: members, meals and votes, 1945\u20131954",
          "Three series that are not on one scale and are not drawn as though they were. "
          "Each is indexed to its own first reading, and the food line is dashed because "
          "its endpoints are two years apart from the others'. The argument is the shape, "
          "not the levels.")],
 ),
 45: dict(
   file='c45_body.html',
   part='Part I', band='The small state', num=45, dates='1948 \u2013 1955',
   coda_part='Part I', coda_span='1901 \u2013 1955',
   title='Choosing a side, and the constitution',
   people='Max S\u00f8rensen \u00b7 Helga Pedersen \u00b7 Gustav Rasmussen \u00b7 '
          'Hans Hedtoft \u00b7 Helene Thiesen \u00b7 Frederik 9.',
   hook="Denmark spent 1948 trying not to choose, and the Scandinavian answer failed in "
        "Oslo in January 1949 because Sweden would not join a bloc tied to the west and "
        "Norway would not join one that was not. Ten weeks later Denmark signed the "
        "Atlantic pact. Four years after that it replaced a constitution by nineteen "
        "thousand votes \u2014 abolishing the upper house, writing down parliamentary "
        "government, giving a princess a place behind every brother, and installing the "
        "paragraph it would walk through into Europe in 1973.",
   keys=['skandinavisk forsvarsforbund', 'Atlantpagten 1949',
         '45-procents-reglen', 'Forfatningskommissionen af 1946',
         'Landstingets afskaffelse', 'parlamentarisme i grundloven',
         'betinget kvindelig arvef\u00f8lge', 'grundlovens \u00a7 20',
         'Gr\u00f8nland som amt 1953', 'eksperimentb\u00f8rnene 1951',
         'Thulesagen 1953', 'folkeafstemningen 28. maj 1953',
         'grundloven af 5. juni 1953'],
   qs=["Why did the Scandinavian defence union fail, and what did each of the three "
       "governments want that the other two could not give?",
       "A revision supported by 91.85 per cent of those who voted failed in 1939 and one "
       "supported by 78.76 per cent passed in 1953. What was the rule, and what was it "
       "actually measuring?",
       "The Landsting voted for its own abolition. What had each reform since 1866 done "
       "to it that left it without an argument?",
       "\u00a7 20 was drafted in 1952 for the United Nations and the Atlantic alliance. "
       "How did it come to be the clause Denmark joined the European Communities under?",
       "Greenland stopped being a colony in 1953. Who decided that, and who was not "
       "asked?"],
   figs=[("s05", "SVG_LANDSTING",
          "Figure 1 \u00b7 The Landsting, 1849\u20131953: who chose it",
          "Three franchise regimes on one axis, every span computed from its two dates "
          "rather than from anybody's rounding. The chamber's life runs constitution to "
          "constitution, 5 June 1849 to 5 June 1953 \u2014 exactly 104 years; its last "
          "sitting is three weeks earlier."),
         ("s10", "SVG_GULV",
          "Figure 2 \u00b7 1939 and 1953 against the forty-five per cent floor",
          "Each bar is the whole electorate, because that is the denominator the rule "
          "used. The third block is everyone who did not vote yes or no, which a "
          "threshold on the electorate treats as a no. The 1939 electorate is not "
          "published in any source reached and is derived from its own percentage; it is "
          "drawn hatched and labelled as derived."),
         ("s12", "SVG_TOBILLETTER",
          "Figure 3 \u00b7 Two ballots, one Thursday",
          "The same day, two questions and two different registers. The voting-age ballot "
          "was open to 229,300 more people than the constitutional one, because it was "
          "open to those the lower age would have enfranchised. Its own components "
          "overshoot its published total by 200 votes, which is marked rather than "
          "averaged away.")],
 ),
}


# ---------------------------------------------------------------- draft parsing
def load():
    return open(DRAFT, encoding="utf-8").read()


# A SEGMENT'S PREAMBLE - everything between its `# Chapter NN` line and its first `##` -
# is never emitted, whichever kind of segment it heads. Review session 9 (§13.6) found
# two things there that were meant for the reader and never reached a page: chapter 25's
# Nansen vignette (258 words, in a continuation preamble) and chapter 30's "note on
# language" (70 words, in the APPARATUS preamble, which the first guard did not look at).
# So every preamble is held to its structural shape: the `# Chapter NN` line itself, which
# carries the chapter's title from HAND and nothing after it but its dates (or the word
# "apparatus"); blank lines and rules; and italic header notes that begin "*Draft" or
# "*Notes", of at most PREAMBLE_HEADER_WORDS words together - a header states what the
# segment holds, and anything longer is prose that would vanish.
PREAMBLE_HEADER_WORDS = 60


def preamble_leftover(preamble, n):
    """Lines of a segment preamble that are not structure. [] means the preamble is clean."""
    lines = preamble.splitlines()
    left = []
    if lines:
        m = re.match(r'^# Chapter %d — (.*?)\s*$' % n, lines[0])
        rest0 = m.group(1) if m else None
        title = HAND[n]['title'] if n in HAND else None
        if rest0 == 'apparatus':
            pass
        elif (rest0 is None or title is None or not rest0.startswith(title)
              or not re.fullmatch(r'(?:,\s*(?:c\.\s*)?\d{4}\s*[–-]\s*\d{4})?', rest0[len(title):])):
            left.append(lines[0])
    rest = "\n".join(ln for ln in lines[1:] if ln.strip() and not re.match(r'^\s*-{3,}\s*$', ln))
    if rest:
        spans = re.fullmatch(r'(?:\s*\*(?:Draft|Notes)\b[^*]*\*)+\s*', rest, re.S)
        if not spans:
            left += [ln for ln in rest.splitlines() if ln.strip()]
        elif len(rest.split()) > PREAMBLE_HEADER_WORDS:
            left.append("%d words of italic header notes (the limit is %d): %s"
                        % (len(rest.split()), PREAMBLE_HEADER_WORDS, " ".join(rest.split())[:60]))
    return left


def chapter(src, n):
    """(prose, apparatus) for chapter n.

    A CONTINUATION SEGMENT'S PREAMBLE IS NOT PROSE. PART_G_DRAFT.md is several
    per-chapter files concatenated, and a chapter written in two sittings appears
    as two `# Chapter NN` segments. Joining them kept the second one's preamble -
    the `<!-- ===== cNN_draft_04-09.md ===== -->` marker the concatenation left
    behind, the repeated `# Chapter NN —` line, its `*Draft, sections 04-09 of
    09.*` header and any placement note under it.

    Nothing downstream removed it. `sections()` splits on `##`, so a preamble
    sitting between the previous segment's last `##` and the next one belongs, as
    far as the splitter is concerned, to the section that was already open. It
    shipped: chapter 25 §03 carries a draft-file header and a placement note
    mid-narrative on the live page, and chapter 26 §05 the same, both between two
    paragraphs of the book's own prose. HANDOFF item 102 recorded this in the
    chapter 39 session and it was never traced to the line that causes it.

    So a continuation segment starts at its first `##`. The FIRST segment needs
    no such treatment - everything before the first `##` was already outside
    every section and was never emitted.

    The concatenation markers themselves are dropped wherever they fall, not only
    in a preamble: one lands at the END of a chapter's last segment, ahead of the
    next `# Chapter` line, which is how chapters 25, 26, 27, 29, 30 and 31 each
    carry one in their final section too. A marker is a comment naming a file on
    disk. It is never prose, in any position.

    Author notes are a different thing and are deliberately not swept up here:
    `draftnotes.py` must go on refusing a draft that still contains them, so they
    are resolved rather than quietly dropped. Removing the markers is what lets
    that refusal mean something - of the 28 notes it reported in this file, 14
    were these markers, and a guard whose output is half artefact is one nobody
    reads to the end.
    """
    src = re.sub(r'^[ \t]*<!--\s*=+\s*c\d\d_draft[^\n]*-->[ \t]*\n?', '', src, flags=re.M)
    ms = [m for m in re.finditer(r'^# Chapter (\d+)(.*)$', src, re.M)]
    # THE FILE'S OWN HEAD is not emitted either: everything before the first `# Chapter`
    # line. It may hold a `# PART ...` title and italic notes about the file, and nothing
    # else (the second checker of session 9 found it unguarded).
    head = src[:ms[0].start()] if ms else ''
    left = [ln for ln in head.splitlines()
            if ln.strip() and not re.match(r'^\s*(?:# PART [A-Z]\b.*|\*[^*]+\*|-{3,})\s*$', ln)]
    if left:
        raise SystemExit(
            "!! %s: %d line(s) before the first `# Chapter` line that are not a title or an "
            "italic file note. Nothing there is emitted. Move it into a chapter:\n%s"
            % (DRAFT, len(left), "\n".join("   - %s" % ln[:70] for ln in left[:5])))
    body = app = None
    for i, m in enumerate(ms):
        if int(m.group(1)) != n:
            continue
        end = ms[i + 1].start() if i + 1 < len(ms) else len(src)
        seg = src[m.start():end]
        kind = ('apparatus' if 'apparatus' in m.group(2)
                else 'first body' if body is None else 'continuation')
        first = re.search(r'^## ', seg, re.M)
        preamble = seg[:first.start()] if first else seg
        # AND REFUSE PROSE, in every kind of segment (see preamble_leftover above).
        # draftnotes only knows what an author note looks like, and chapter 25's
        # continuation preamble carried something else: a whole vignette, dropped on
        # every build since the chapter was drafted and never missed, because no guard
        # counts what is not emitted. Chapter 30's apparatus preamble did the same with
        # its note on language. Anything beyond the structural lines stops the build.
        left = preamble_leftover(preamble, n)
        if left:
            raise SystemExit(
                "!! chapter %d: the %s segment's preamble carries %d line(s) of text "
                "before its first `##`. The preamble is not emitted, so this would be "
                "dropped rather than shipped. Move it into a section:\n%s"
                % (n, kind, len(left), "\n".join("   - %s" % ln[:70] for ln in left[:5])))
        if kind == 'apparatus':
            # ONE APPARATUS SEGMENT. A second `# Chapter NN — apparatus` line used to
            # replace the first here (`app = seg`), silently: the checker of review
            # session 9 planted one in chapter 27 and the page lost its terms, both
            # Meanwhiles and the whole Myth-check while mkbody, the part build and
            # appcheck all passed.
            if app is not None:
                raise SystemExit(
                    "!! chapter %d: two `# Chapter %d — apparatus` segments. The build keeps "
                    "one; merge them." % (n, n))
            app = seg
        elif body is None:
            body = seg
        else:
            # REFUSE RATHER THAN DISCARD. The preamble is structural and is
            # dropped - but chapter 25's carried a real placement note, and
            # dropping that silently would be the very fault this function is
            # being fixed for. Anything in it that reads as an author note stops
            # the build instead.
            notes = draftnotes.find(preamble)
            if notes:
                raise SystemExit(
                    "!! chapter %d: the continuation segment's preamble carries %d "
                    "author note(s). The preamble is not emitted, so these would be "
                    "dropped rather than shipped. Resolve each and delete it from the "
                    "preamble, or move it into the prose:\n%s"
                    % (n, len(notes),
                       "\n".join("   - %s%s..." % (m, c[:60]) for m, c in notes)))
            body += seg[first.start():] if first else ''
    return body, app


def sections(body):
    """[(id, num, title, markdown)] over ## headings, skipping the coda."""
    out = []
    hs = [m for m in re.finditer(r'^## (.+)$', body, re.M)]
    k = 0
    for i, m in enumerate(hs):
        t = m.group(1).strip()
        end = hs[i + 1].start() if i + 1 < len(hs) else len(body)
        chunk = body[m.end():end]
        if t.lower().startswith('coda'):
            out.append(('coda', '', t, chunk))
            continue
        k += 1
        out.append(('s%02d' % k, '%02d' % k, t, chunk))
    return out


def apparatus_part(app, heading):
    """The markdown under `## heading`, up to the next `##`.

    A `---` RULE IS NOT TEXT, and it is removed here rather than in each
    builder. The drafts close every apparatus block with a markdown rule before
    the next heading. The Questions builder appends any unnumbered line to the
    question above it, and the Sources builder splits items on `- ` and `**`,
    which `---` is neither - so the rule was printed as the end of the last
    question on twenty pages and the end of the last source on twenty-one, as a
    literal "---". `paras()` already skipped a bare rule, which is why the other
    blocks never showed it.
    """
    m = re.search(r'^## %s\s*$' % re.escape(heading), app, re.M)
    if not m:
        return ""
    nxt = re.search(r'^## ', app[m.end():], re.M)
    blk = app[m.end():m.end() + (nxt.start() if nxt else len(app))]
    return re.sub(r'^[ \t]*-{3,}[ \t]*$', '', blk, flags=re.M)


# ---------------------------------------------------------------- inline md
def inline(t):
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t, flags=re.S)
    t = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i class="dk">\1</i>', t, flags=re.S)
    t = re.sub(r'`([^`]+?)`', r'<i class="dk">\1</i>', t)
    return re.sub(r'\s+', ' ', t).strip()


def paras(md):
    """Markdown block -> list of ('p'|'vig'|'rule', payload)."""
    out = []
    for blk in re.split(r'\n\s*\n', md):
        b = blk.strip()
        if not b or b == '---':
            continue
        if b.startswith('>'):
            out.append(('vig', "\n".join(re.sub(r'^>\s?', '', l) for l in b.split('\n'))))
        elif b.startswith('- ') or b.startswith('* '):
            out.append(('ul', b))
        else:
            out.append(('p', b))
    return out


def vig_html(md):
    """A vignette block.

    THE TITLE MAY WRAP. This took the first line as the whole title, and a title
    long enough to wrap in the markdown - `**Vignette · Johann Friedrich
    Struensee, Christiansborg, before dawn on 17 / January 1772**` in
    c29_draft_01-10.md - was cut at the line break. Chapter 29 shipped with
    literal asterisks in its <h4>, the heading ending "on 17", and a stray
    paragraph reading `January 1772**` as the vignette's first line. It is the
    only leaked markdown in the 45 built pages, which is the only reason it went
    unnoticed: one instance looks like a typo rather than a parser.

    So the title is taken as however many lines it needs to close its `**`.
    """
    lines = [l for l in md.split('\n')]
    take = 1
    if lines and lines[0].lstrip().startswith('**'):
        while take < len(lines) and lines[take - 1].count('**') % 2:
            take += 1
    head = inline(' '.join(lines[:take])).replace('<strong>', '').replace('</strong>', '')
    rest = "\n".join(lines[take:]).strip()
    ps = [p for k, p in paras(rest) if k == 'p']
    who = ps.pop() if len(ps) > 1 else ''
    o = ['<div class="vig">', '<h4>%s</h4>' % head]
    for p in ps:
        o.append('<p>%s</p>' % inline(p))
    if who:
        o.append('<p class="who">%s</p>' % inline(who))
    o.append('</div>')
    return "\n".join(o)


def prose_html(md):
    o = []
    for kind, p in paras(md):
        if kind == 'vig':
            o.append(vig_html(p))
        elif kind == 'ul':
            items = [inline(re.sub(r'^[-*]\s+', '', l)) for l in p.split('\n') if l.strip()]
            o.append('<ul class="plain">' + "".join('<li><span class="ds">%s</span></li>' % i
                                                    for i in items) + '</ul>')
        else:
            o.append('<p>%s</p>' % inline(p))
    return "\n\n".join(o)


# ---------------------------------------------------------------- terms
def terms_by_section(app):
    """{'01': ([(term, gloss)], ['01','02'])} from the 'Danish terms, by section' list.

    HEADERS ARE RANGED. A block headed "**§05-07 - the islands**" glosses three
    sections, not one. The first version of this parser read only the leading number,
    so every ranged block was attached to its first section and the rest counted as
    unglossed - which put fifteen phantom gaps into the review and made the block's
    "in this section" heading wrong on every ranged block in the part.

    THE RANGE SEPARATOR IS TIGHT AND THE DESCRIPTIVE ONE IS SPACED, and the second
    version of this parser did not distinguish them: it allowed whitespace around
    the separator, so "**§01 - 1939**" parsed as sections 01 to 1939 and
    "**§03 - 9 April**" as sections 03 to 09. ELEVEN IMPOSSIBLE HEADINGS SHIPPED -
    "Danish terms in sections 01-1939" in chapter 41, "09-1899" in 35, "10-1901"
    in 36, "06-1924" in 39 and three in 40 - and TWO MORE SHIPPED THAT LOOK LEGAL
    AND ARE NOT: chapter 38's "sections 06-10" and chapter 41's "sections 03-09"
    are each one section's block. Nothing could see any of it. The markup is valid,
    the heading fits, and `span` is used ONLY for this heading - placement keys off
    the leading number alone - so every block sat in the right place and only the
    label lied. Item 110's class, and item 117's: a heading is a claim.

    The fix requires the range separator to be ADJACENT, which is how the example
    above writes it and which no descriptive header uses."""
    blk = apparatus_part(app, 'Danish terms, by section')
    out = {}
    cur = None
    for m in re.finditer(r'^\*\*§(\d+)(?:[\u2013\u2014-](\d+))?[^\n]*\*\*\s*$'
                         r'|^-\s+\*\*(.+?)\*\*\s+—\s+(.+?)(?=\n(?:-|\*\*|\Z))',
                         blk, re.M | re.S):
        if m.group(1):
            a = int(m.group(1))
            b = int(m.group(2)) if m.group(2) else a
            # A range running backwards or past any plausible chapter is a parse
            # failure, not a range. Loud, because the old one was silent.
            assert a <= b <= 30, ('implausible glossary range', m.group(0), a, b)
            span = ['%02d' % i for i in range(a, b + 1)]
            cur = (m.group(1), span)
            out[m.group(1)] = ([], span)
        elif cur:
            out[cur[0]][0].append((m.group(3).strip(),
                                   re.sub(r'\s+', ' ', m.group(4)).strip()))
    return out


def terms_html(pairs, span=None):
    if not pairs:
        return ""
    cls = ' class="one"' if len(pairs) == 1 else ''
    head = ('Danish terms in this section' if not span or len(span) == 1
            else 'Danish terms in sections %s\u2013%s' % (span[0], span[-1]))
    o = ['<div class="terms">', '  <h4>%s</h4>' % head, '  <dl%s>' % cls]
    for t, g in pairs:
        o.append('    <div class="t"><dt>%s</dt><dd>%s</dd></div>' % (inline(t), inline(g)))
    o.append('  </dl>')
    o.append('</div>')
    return "\n".join(o)


# ---------------------------------------------------------------- tail pieces
def meanwhile_html(app, n='?'):
    """The 'Meanwhile in Europe' boxes.

    A paragraph opening with **A label.** opens a box. A paragraph without one
    CONTINUES the box above it, which is how the drafts use it: chapters 42 and
    43 each end the block with an unlabelled paragraph that draws the comparison
    the two boxes exist to set up - Rome against Denmark in October 1943, Milorg
    against the Danish underground. The version of this function shipped before
    18 September 2026 said `continue` on those paragraphs, and 141 words of
    authored prose were dropped from two pages without a word in any log.

    The refusal below this function already says 'refuse rather than discard
    authored prose'. It was written for the count of boxes and did not cover the
    paragraphs between them, so the same leak stayed open in the same function.
    A paragraph that arrives before any box has nowhere to go and is refused.
    """
    blk = apparatus_part(app, 'Meanwhile in Europe')
    boxes = []
    for _, p in [x for x in paras(blk) if x[0] == 'p']:
        m = re.match(r'\*\*(.+?)\*\*\s*(.*)', p, re.S)
        if m:
            boxes.append([inline(m.group(1)), [inline(m.group(2))]])
        elif boxes:
            boxes[-1][1].append(inline(p))
        else:
            raise SystemExit(
                "!! chapter %s: a 'Meanwhile in Europe' paragraph appears before any "
                "**Label.** paragraph, so there is no box to put it in. Give it a "
                "label or move it - do not let the build drop it:\n     %s"
                % (n, ' '.join(p.split())[:90]))
    return ['<div class="meanwhile">\n<h4>Meanwhile · %s</h4>\n%s\n</div>'
            % (lab, "\n".join('<p>%s</p>' % x for x in ps)) for lab, ps in boxes]


def _myth_opens_entry(p):
    """True if this paragraph starts a new myth-check entry (a quoted claim)."""
    s = p.lstrip()
    return bool(re.match(r'\*\*\s*["\u201c]', s) or re.match(r'["\u201c]', s))


def myth_entries(items):
    """Paragraph list -> [(claim_md, [correction_md, ...])].

    WHY THIS IS NOT A ONE-LINER. Four myth-check conventions are in use in this
    book, and the version of this function shipped before 18 September 2026
    understood only the first of them. It read paragraphs in strict pairs -
    claim, correction, claim, correction - and advanced by two. What that did to
    the other three was silent and total:

      A  claim para, then ONE correction para                      ch 1-24   ok
      B  **The myth.** / **What can be shown.** / **What cannot.**  ch 25-31  DROPPED
         No paragraph opened with a quote, so nothing matched and the chapter
         shipped with <dl></dl> - the heading over an empty list, seven times.
      C  claim para, then SEVERAL correction paras                  ch 32-36  TRUNCATED
         The pair rule took the first correction paragraph and the += 2 walked
         past the rest, losing 85-92% of the block.
      D  **"claim"** correction, both in ONE para                   ch 37-45  MIS-PAIRED
         The whole paragraph became the <dt> and the NEXT claim became its
         <dd>, so every page in Part I printed each correction in the claim's
         type and each claim in the correction's, offset by half an entry.

    2,719 words of written myth-check prose - 49% of all of it - were not on the
    pages. Nothing caught it: the words were in the drafts, the files built, the
    verifiers passed, and the fault only shows if you compare draft against page
    or read the built HTML. Hence the rule this is filed under: a guard that only
    fires at review is not a guard. `debuild.py verify` still cannot see this;
    the check that can is a draft-to-page word-count diff, and it belongs in the
    suite.
    """
    items = [i.strip() for i in items if i.strip()]
    if not items:
        return []

    # B - the labelled triple. No quoted claim anywhere in the block.
    if any(re.match(r'\*\*\s*The myth\.?\s*\*\*', i) for i in items):
        out, cur = [], None
        for p in items:
            m = re.match(r'\*\*\s*The myth\.?\s*\*\*\s*(.*)', p, re.S)
            if m:
                if cur:
                    out.append(cur)
                cur = (m.group(1).strip(), [])
            elif cur:
                cur[1].append(p)
        if cur:
            out.append(cur)
        return out

    # A / C / D - an entry begins at a quoted claim and runs to the next one.
    out, cur = [], None
    for p in items:
        if _myth_opens_entry(p):
            if cur:
                out.append(cur)
            m = re.match(r'\*\*(.+?)\*\*\s*(.*)', p, re.S)   # D: claim and correction share a para
            if m:
                claim, tail = m.group(1).strip(), m.group(2).strip()
            else:                                            # A / C: the claim para stands alone
                claim, tail = p.strip(), ''
            cur = (claim, [tail] if tail else [])
        elif cur:
            cur[1].append(p)
    if cur:
        out.append(cur)
    return out


def myth_html(app):
    blk = apparatus_part(app, 'Myth-check')
    o = ['<div class="myth" id="myth">', '<h4>Myth-check</h4>', '<dl>']
    for claim, corrections in myth_entries([p for k, p in paras(blk) if k == 'p']):
        dt = inline(claim).replace('<strong>', '').replace('</strong>', '')
        o.append('  <dt>%s</dt>' % dt)
        if corrections:
            o.append('  <dd>%s</dd>'
                     % ''.join('<p>%s</p>' % inline(c) for c in corrections))
    o += ['</dl>', '</div>']
    return "\n".join(o)


def calls_html(app):
    blk = apparatus_part(app, 'Carry-forward')
    o = ['<ul class="calls">']
    for _, p in [x for x in paras(blk) if x[0] == 'p']:
        m = re.match(r'\*\*(←|→)\s*([^.]+)\.\*\*\s*(.*)', p, re.S)
        if m:
            o.append('  <li><b>%s %s</b><span>%s</span></li>'
                     % (m.group(1), m.group(2).strip(), inline(m.group(3))))
    o.append('</ul>')
    return "\n".join(o)


def five_html(app):
    blk = apparatus_part(app, 'Summary')
    ps = [p for k, p in paras(blk) if k == 'p']
    o = ['<ol class="five">']
    for p in ps[:5]:
        o.append('  <li><p>%s</p></li>' % inline(p))
    o.append('</ol>')
    return "\n".join(o), len(ps)


TIERS = [('Recall', 'Did the facts land?'),
         ('Causal', 'Why did it happen that way?'),
         ('Counterfactual', 'What if it had gone otherwise?'),
         ('Contested', 'Where do historians disagree?')]


def questions_html(app):
    blk = apparatus_part(app, 'Questions')
    groups, cur = [], None
    for line in blk.split('\n'):
        s = line.strip()
        h = re.match(r'\*\*(Recall|Causal|Counterfactual|Contested)\b.*\*\*', s)
        if h:
            cur = (h.group(1), [])
            groups.append(cur)
        elif cur is not None and re.match(r'^\d+\.\s+', s):
            cur[1].append(re.sub(r'^\d+\.\s+', '', s))
        elif cur is not None and cur[1] and s and not s.startswith('**'):
            cur[1][-1] += ' ' + s
    o = []
    notes = dict(TIERS)
    for name, qs in groups:
        o.append('<div class="qgroup">')
        o.append('  <p class="qlabel">%s</p>' % name)
        o.append('  <p class="qnote">%s</p>' % notes.get(name, ''))
        o.append('  <ul>')
        for q in qs:
            o.append('    <li>%s</li>' % inline(q))
        o.append('  </ul>')
        o.append('</div>')
    return "\n".join(o), sum(len(q) for _, q in groups)


def plain_html(app, heading):
    blk = apparatus_part(app, heading)
    o = ['<ul class="plain">']
    for line in re.split(r'\n(?=-\s|\*\*)', blk):
        s = line.strip()
        if not s:
            continue
        m = re.match(r'\*\*(.+?)\*\*\s*(.*)', s, re.S)
        if m:
            o.append('  <li><span class="nm">%s</span>\n    <span class="ds">%s</span></li>'
                     % (inline(m.group(1)), inline(m.group(2))))
            continue
        m = re.match(r'-\s+(?:\*\*(.+?)\*\*[.:]?\s*)?(.*)', s, re.S)
        if m:
            nm = inline(m.group(1)) if m.group(1) else '—'
            o.append('  <li><span class="nm">%s</span>\n    <span class="ds">%s</span></li>'
                     % (nm, inline(m.group(2))))
    o.append('</ul>')
    return "\n".join(o)


# ---------------------------------------------------------------- assembly
def build(n):
    h = HAND[n]
    src = load()
    body_md, app = chapter(src, n)
    if body_md is None or app is None:
        raise SystemExit("!! chapter %d: prose or apparatus not found in %s" % (n, DRAFT))

    # DRAFTING FLAGS MUST NOT SHIP. The drafts carry italic notes addressed to the
    # author - "*Flag: confirm the membership...*" - and the header of every draft
    # says they are not copy. Nothing enforced it. Chapter 38 was built, linked,
    # indexed and counted with seven of them on the page: mkbody, build_part_i,
    # figcheck, tidy, narrative and bookstats all reported clean, and about two
    # hundred words of notes-to-self went into the shipped page word count.
    #
    # This REFUSES rather than stripping, for the reason item 67 gives: a flag is
    # an unresolved question, and silently deleting it loses the question. Resolve
    # it, or move it to the Sources block where the apparatus already carries an
    # "unresolved" list, and then build.
    #
    # The pattern lives in draftnotes.py and is shared with the page scan. The
    # first version here matched the literal "*Flag:", case-sensitively, and
    # "*Drafting flag:" - chapter 32's wording, four times - passed it (item 102).
    flags = draftnotes.find((body_md or "") + "\n" + (app or ""))
    if flags:
        raise SystemExit(
            "!! chapter %s: %d drafting note(s) still in the draft. They are not copy "
            "and must not ship. Resolve each, or move it to the Sources block as a "
            "question addressed to the reader, then rebuild.\n%s"
            % (n, len(flags),
               "\n".join("   - %s%s..." % (m, ctx[:60]) for m, ctx in flags)))
    # LITERAL UNICODE ESCAPES MUST NOT SHIP (convention D-12). Four apparatus
    # blocks of chapter 41 were written to the draft by a script inside a shell
    # heredoc, where a doubled backslash survives, and thirty-six "ø" and
    # "→" sequences went in as TEXT. Every guard passed them: the markup is
    # valid, the tag balance is fine, and debuild round-trips the page against
    # itself, so "identical" means nothing here. Item 110's class exactly - valid
    # output, wrong content - and the only thing that caught it was reading the
    # file. This is the cheap permanent check that would have caught it at once.
    esc = re.findall(r'\\u[0-9a-fA-F]{4}', (body_md or "") + "\n" + (app or ""))
    if esc:
        raise SystemExit(
            "!! chapter %s: %d literal unicode escape(s) in the draft (%s). A draft "
            "holds characters, not escapes - see convention D-12. Write draft prose "
            "with an editor or from a UTF-8 file, never through a heredoc, then "
            "rebuild." % (n, len(esc), ", ".join(sorted(set(esc))[:6])))

    secs = sections(body_md)
    tb = terms_by_section(app)
    figs = {}
    for sid, ph, ct, cb in h['figs']:
        figs.setdefault(sid, []).append((ph, ct, cb))

    o = ['<!DOCTYPE html>', '<html lang="en">', '<head>', '<meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width, initial-scale=1">',
         '<title>%d · %s, %s</title>' % (n, h['title'], h['dates'].replace(' – ', '–')),
         '<style>{{STYLE}}</style>', '</head>', '<body>', '',
         '<div class="crumb"><div class="crumb-in">',
         '  <span><b>%s</b> · %s</span><span>Chapter %d</span><span>%s</span>'
         % (h['part'], h['band'], n, h['dates']),
         '</div></div>', '', '{{RAIL}}', '', '<div class="wrap">', '',
         '<header class="hd">',
         '  <p class="eyebrow">Era chapter · about 36 minutes</p>',
         '  <h1>%s</h1>' % html.escape(h['title']),
         '  <p class="dates">%s · %s</p>' % (h['dates'], inline(h['people'])),
         '  <p class="why">%s</p>' % inline(h['hook']),
         '  <ul class="keys">']
    o.append('    ' + "".join('<li>%s</li>' % html.escape(k) for k in h['keys']))
    o += ['  </ul>', '</header>', '', '{{TOC}}', '',
          '<p class="kicker">Introduction</p>',
          '<h2 id="intro" style="margin-top:0"><span class="n">WHAT THIS PAGE ANSWERS</span>'
          'Five questions</h2>', '<ol class="qs">']
    for q in h['qs']:
        o.append('  <li>%s</li>' % q)
    o += ['</ol>', '', '<hr class="div">', '']

    mw = meanwhile_html(app, n)
    mw_at = {secs[2][0]: 0, secs[min(6, len(secs) - 1)][0]: 1} if len(mw) >= 2 else {}
    # This placement holds exactly two. A draft with three built three and emitted
    # two, silently, and the count printed below counts what was PLACED, so the
    # diagnostic said 2 and looked right. Every chapter to date happened to have
    # two, so it never fired. Refuse rather than discard authored prose.
    if len(mw) != len(mw_at):
        raise SystemExit(
            "!! chapter %s: %d 'Meanwhile in Europe' blocks in the draft but the "
            "placement holds %d. Cut the draft to %d, or generalise mw_at - do not "
            "let the build drop one." % (n, len(mw), len(mw_at), len(mw_at)))

    for sid, num, title, md in secs:
        if sid == 'coda':
            continue
        o.append('<h2 id="%s"><span class="n">%s / NARRATIVE</span>%s</h2>'
                 % (sid, num, inline(title)))
        o.append('')
        entry = tb.get(num)
        t = terms_html(entry[0], entry[1]) if entry else ""
        if t:
            o += [t, '']
        o += [prose_html(md), '']
        for ph, ct, cb in figs.get(sid, []):
            o += ['<figure>', '{{%s}}' % ph,
                  '<figcaption><b>%s</b>' % ct, inline(cb) + '</figcaption>', '</figure>', '']
        if sid in mw_at:
            o += [mw[mw_at[sid]], '']

    o += ['<hr class="div">', '', myth_html(app), '']
    # AN EMPTY CARRY-FORWARD IS LEFT OUT, NOT PRINTED EMPTY (decision D-C, 19 Sept
    # 2026). Chapter 45 is the last page and has nothing to carry forward; it
    # shipped a heading over an empty list. The build script must agree: a chapter
    # whose body has no carry-forward declares no_forward=True in its CFG, and
    # build_part_i.py refuses a page where the declaration and the body disagree,
    # so a list lost by accident cannot pass as a list left out on purpose.
    calls = calls_html(app)
    if '<li>' in calls:
        o += ['<p class="kicker">Threads and links</p>',
              '<h2 id="forward" style="margin-top:0"><span class="n">WHERE THIS GOES</span>'
              'What to carry forward</h2>', calls, '']
    else:
        print("  carry-forward: no arrows in the draft; heading left out")
    o += ['<p class="kicker">Summary</p>',
          '<h2 id="summary" style="margin-top:0"><span class="n">IF YOU REMEMBER FIVE THINGS'
          '</span>The page in five</h2>']
    fh, nfive = five_html(app)
    o += [fh, '',
          '<p class="kicker">Questions &amp; discussion</p>',
          '<h2 id="questions" style="margin-top:0"><span class="n">FOUR KINDS</span>'
          'Work the material</h2>', '']
    qh, nq = questions_html(app)
    o += [qh, '',
          '<p class="kicker">Sources</p>',
          '<h2 id="sources" style="margin-top:0"><span class="n">LIGHT SOURCING</span>'
          'What this is built on</h2>', plain_html(app, 'Sources'), '',
          '<p class="kicker">Go and look</p>',
          '<h2 id="visit" style="margin-top:0"><span class="n">STILL THERE</span>'
          'Places you can visit</h2>', plain_html(app, 'Visit'), '']

    coda = [s for s in secs if s[0] == 'coda']
    if coda:
        # The kicker and the band were hardcoded to Part G, because chapter 31 was
        # the only chapter that had ever carried a part coda. Chapter 36 carries
        # Part H's. Both now come from HAND, and the defaults are the Part G pair,
        # so chapter 31 rebuilds byte-identical - predicted before the change and
        # checked after it.
        o += ['<p class="kicker">Closing %s</p>' % h.get('coda_part', 'Part G'),
              '<h2 id="coda" style="margin-top:0"><span class="n">%s</span>'
              'What this part was about</h2>'
              % h.get('coda_span', '1660 – 1814'),
              '', prose_html(coda[0][3]), '']

    o += ['<footer>', '  Chapter %d · %s · %s' % (n, h['part'], h['dates']), '</footer>',
          '', '</div>', '{{JS}}', '</body>', '</html>', '']

    out = "\n".join(o)
    open(h['file'], 'w', encoding='utf-8').write(out)

    nsec = len([s for s in secs if s[0] != 'coda'])
    print("chapter %d -> %s" % (n, h['file']))
    print("  sections %d | terms %d | vignettes %d | meanwhile %d | figures %d"
          % (nsec, out.count('class="terms"'), out.count('class="vig"'),
             out.count('class="meanwhile"'), out.count('<figure>')))
    # THE HEADING PROMISES FIVE. `ol.five` numbers with a decimal leading zero, so a
    # Summary of four paragraphs renders 01-04 under "IF YOU REMEMBER FIVE THINGS"
    # and a Summary of one renders a single item numbered 01. Chapters 25, 26 and 27
    # shipped with four (open item 19) and chapter 32 shipped with ONE, which nobody
    # noticed for a session, because this line printed the number and judged nothing.
    # It printed and exited 0 until review session 9, when the checker renamed a Summary
    # heading and the body was written with an empty "five things" and the part build
    # still said "built clean". A body that breaks the heading's promise is a failed
    # build, so it now stops (the body is already written, and says what is wrong).
    if nfive < 5:
        raise SystemExit("  !! chapter %d: Summary yields %d item(s); the heading promises five"
                         % (n, nfive))
    print("  summary items %d (of %d paragraphs) | questions %d | placeholders %s"
          % (min(5, nfive), nfive, nq, sorted(set(re.findall(r'\{\{([A-Z0-9_]+)\}\}', out)))))
    bad = [t for t in ['div', 'p', 'h2', 'h4', 'ul', 'ol', 'li', 'dl', 'dt', 'dd',
                       'figure', 'figcaption', 'span', 'header', 'footer']
           if out.count('<' + t + ' ') + out.count('<' + t + '>') != out.count('</' + t + '>')]
    print("  tag balance: %s" % (bad if bad else 'ok'))
    if out.count('class="check"'):
        print("  !! body contains checkpoints; the build strips them")
    return out


if __name__ == "__main__":
    ns = [int(a) for a in sys.argv[1:] if a.isdigit()] or sorted(HAND)
    for n in ns:
        build(n)
