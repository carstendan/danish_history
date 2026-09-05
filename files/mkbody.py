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
   people='Frederik 3. · Hans Nansen · Hans Svane · Joachim Gersdorff · Peder Griffenfeld',
   hook="In six days in October 1660 an assembly called to settle a war debt handed the "
        "king of Denmark more power than any monarch in Europe, and did it by a vote. "
        "Nobody stormed anything. What replaced the charter was a state of standing "
        "offices, a register that reduced every farm in the kingdom to a single number, "
        "and a law sealed in a casket that almost nobody read for forty years.",
   keys=['stændermøde 1660', 'arvehyldning 18. oktober 1660', 'enevælde',
         'Kongeloven 1665', 'kollegier', 'amter og amtmænd',
         'matriklen 1662 og 1664', 'hartkorn', 'rangforordningen 1671'],
   qs=["Denmark's estates met to raise a tax. How did that end with an absolute monarchy?",
       "The proposal came from the burghers and the clergy, not from the king. Why would "
       "townsmen hand a king unlimited power?",
       "Hereditary did not have to mean absolute. Where, in six days, did the one become "
       "the other?",
       "What did the <i class=\"dk\">Kongelov</i> of 1665 actually say, and why did so few "
       "people read it?",
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
          "licence — before and after. On the left they all go to one body of about twenty "
          "noblemen who met when summoned and discussed everything. On the right each goes "
          "to a standing office with one subject, staffed by men who came in every day. This "
          "is not a change of furniture but a change of topology, and the council of the "
          "realm has no place in the second diagram."),
         ("s07", "SVG_HARTKORN",
          "Figure 3 · One farm, reduced to a number",
          "What a tenant actually owed, and what the commissioners of 1662 and 1664 wrote "
          "down instead. Nothing was measured and no commissioner walked a field: the "
          "registers took the landlords' own estate books and converted grain, dairy, "
          "livestock and labour into one artificial unit, so that a farm on Funen and a farm "
          "in Vendsyssel could be added together. The quantities here are a worked example "
          "built from the conversion rules, not a transcription of one entry. Denmark "
          "measured its ground for the first time in 1682; land was valued in "
          "<i class=\"dk\">hartkorn</i> until 1903."),],
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
          "Fontainebleau in 1679 Louis 14. ended the war and required every conquest to be "
          "given back, so the map at the end is the map at the start."),
         ("s04", "SVG_MANDEBOD",
          "Figure 2 · Who owed for a killing, 1241 and 1683",
          "The change between the two codes is not severity. Jyske Lov priced a man, priced "
          "the parts of him as fractions of that, and split the debt three ways between the "
          "killer, his father's kin and his mother's kin — a family owed for what a member "
          "had done. Danske Lov has no tariff of body parts and no shares. The killer answers "
          "alone. Roughly two thirds of Jyske Lov was carried forward into the new code; the "
          "kin's share of the debt was not."),
         ("s09", "SVG_CELL",
          "Figure 3 · Seven of my paces long and six broad",
          "The room as Leonora Christina measured it, having nothing to measure it with. Two "
          "beds, a table, two chairs; newly whitewashed when she came in, and a floor so "
          "thick with filth she took it for clay. Her bed faced the doors, and with all three "
          "open she could see as far as the stair door, which was the fourth. She was there "
          "from 8 August 1663 to 19 May 1685 — 7,955 days — and no charge was ever brought "
          "and no trial ever held."),],
 ),

 27: dict(
   file='c27_body.html',
   part='Part G', band='Absolutism', num=27, dates='1699 – 1721',
   title='The last war for the Sound',
   people='Frederik 4. · Peter Wessel Tordenskjold · Marie Grubbe · Hans Egede · Gertrud Rask',
   hook="Denmark enters the Great Northern War to get Skåne back and comes out of it with "
        "none of it — and with a southern border closed for the first time in two hundred "
        "years, a restored toll, two hundred and forty village schools, and a mission in "
        "Greenland. In between, plague takes something between a third and two fifths of "
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
          "The southern border closed. The whole of Slesvig is now the king's, the Gottorp "
          "share having been taken in 1713 and confirmed in 1720; Holstein is not, and the "
          "ducal and royal parcels there are interleaved parish by parish, which is why the "
          "legend carries the distinction the map cannot. The eastern provinces are no longer "
          "drawn in their own tone: by 1721 they are not a loss being absorbed but a settled "
          "fact, formally renounced. Greenland stops being a claim in July of this year."),
         ("s04", "SVG_PLAGUE",
          "Figure 2 · What the state did, and what it could not count",
          "The upper panel is what can be established: a dated sequence of measures, from the "
          "Saltholm quarantine of 1709 to the reopening of the gates in April 1712. The lower "
          "panel is what cannot. Four published death tolls are shown disagreeing rather than "
          "averaged, against a city whose population is itself given as sixty or sixty-nine "
          "thousand. The planned weekly burial curve is not drawn, because reference works "
          "differ by a factor of three or four on the same months and inventing weekly values "
          "for real deaths is the one place a plausible-looking figure would do most harm."),
         ("s08", "SVG_SCHOOLS",
          "Figure 3 · Two hundred and forty-one, in six years",
          "Twelve cavalry districts at twenty schools each were planned and two hundred and "
          "forty-one were built between 1722 and 1727, every one to the same drawing and every "
          "one at 550 rigsdaler. The districts were where the crown held land, so West Jutland "
          "and north-west Zealand got none at all. Attendance was compulsory from five, girls "
          "as well as boys; reading and Christian learning were free, and writing and "
          "arithmetic cost eight skilling a month, which many could not find."),],
 ),

 28: dict(
   file='c28_body.html',
   part='Part G', band='Absolutism', num=28, dates='1721 – 1770',
   title='The bound countryside and the pious state',
   people='Christian 6. · Frederik 5. · Erik Pontoppidan · Ludvig Holberg · Anders Pedersen',
   hook="For half a century the Danish state is at peace and its countrymen are not free. "
        "In 1733 every man of the peasantry is tied to the estate where he was born, to solve "
        "a problem of army recruitment and landlord debt at one stroke. At the same time a "
        "pietist king closes the theatres, makes confirmation compulsory, and puts a book of "
        "seven hundred and fifty-nine questions into every parish in two kingdoms.",
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
          "Three hundred and sixty-five squares, one for each day, with the hundred and ten a "
          "Zealand tenant owed his landlord marked: forty requiring a wagon and a team, "
          "seventy on foot, where a girl or a boy would do. A second reckoning from an estate "
          "at Antvorskov gives a hundred and twenty-two. This is not a calendar. The "
          "reckonings give annual totals and the split, not dates, and drawing the days in "
          "particular months would invent the one thing a reader would take from it. What is "
          "agreed is that the demand fell hardest at ploughing, sowing and harvest — the only "
          "weeks when a man's own crop could not wait."),
         ("s07", "SVG_NORWAY",
          "Figure 2 · What Norway sent south",
          "Silver from Kongsberg, copper from Røros, Løkken and Folldal, timber, iron, "
          "regiments and carting duty. Kongsberg employed 4,075 people in 1770 and was the "
          "largest enterprise in either kingdom, its town second in Norway only to Bergen. "
          "What came the other way was Danish grain — and after 1735 no other kind was "
          "permitted. Norway kept its own law, its own coin and its own regiments. It was not "
          "a colony. The metal still went south."),
         ("s02", "SVG_CATECHISM",
          "Figure 3 · Seven hundred and fifty-nine questions",
          "Pontoppidan's <i class=\"dk\">Sandhed til Gudfrygtighed</i> of 1737, the required "
          "book for every child in two kingdoms. Any fifty of them could be asked at the "
          "public examination in front of the congregation, and you did not know which fifty, "
          "so you learned them all. Re-authorised by three kings in succession and required by "
          "law until 1794; it is probably the book by a Danish author printed in more copies "
          "than any other."),],
 ),

 29: dict(
   file='c29_body.html',
   part='Part G', band='Absolutism', num=29, dates='1770 – 1788',
   title='Struensee, and the village taken apart',
   people='Christian 7. · J.F. Struensee · Caroline Mathilde · C.D.F. Reventlow · Hans Knudsen',
   hook="A German doctor governs Denmark for sixteen months through a king who cannot, "
        "issues something like a thousand cabinet orders, and is executed for it. The men who "
        "overthrow him rule the same way. Then, in the 1780s, the state takes the Danish "
        "village apart field by field and unties the bond of 1733 — and raises a column to "
        "itself for doing it, three years before the last man was actually free.",
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
          "to forty in 1742 and four to forty in 1764. The ordinance of 20 June 1788 worked "
          "three ways at once: it put the band back to the range of 1733, gave immediate "
          "freedom passes to men already too old for service and to those discharged from "
          "it, and released one cohort in each following year, the last on 1 January 1800 "
          "— three years after the column was finished. Conscription itself was not "
          "abolished but moved on "
          "to the new censuses, and it went on falling only on country youth: young men in the "
          "market towns were exempt until 1849."),
         ("s09", "SVG_COLUMN",
          "Figure 3 · What the column says",
          "<i class=\"dk\">Frihedsstøtten</i> on Vesterbrogade, 1792–97: twenty metres of "
          "Bornholm sandstone, raised by public subscription in 1791 while the landowners were "
          "pushing back and the government had stopped reforming. The inscription is given "
          "here line by line with what each line leaves out. The king it credits was incapable; "
          "the free peasant it promises is the <i class=\"dk\">gårdmand</i>, not the cottager; "
          "and the bond it says shall cease had twelve years to run."),],
 ),

 30: dict(
   file='c30_body.html',
   part='Part G', band='Absolutism', num=30, dates='1620 – 1803',
   title='The Danish Atlantic',
   people='Frederik 5. · Ernst Schimmelmann · Hans Egede Saabye · Breffu · Espen Kønig',
   hook="For a hundred and eighty years Denmark ran forts on the Gold Coast, islands in the "
        "Caribbean and ships between them. About a hundred thousand people were carried in "
        "Danish bottoms. In 1792 Denmark became the first state in Europe to order the trade "
        "ended — with a ten-year delay written into the ordinance, during which the traffic "
        "was larger than it had ever been.",
   keys=['Trankebar 1620', 'Christiansborg på Guldkysten', 'Sankt Thomas 1672',
         'Vestindisk-guineisk Kompagni', 'Sankt Jan 1733', 'Sankt Croix 1733',
         'plantageloven', 'trekantshandelen', 'Fredensborg', 'forordningen af 16. marts 1792'],
   qs=["Denmark held Atlantic possessions for a hundred and eighty years. What were the three "
       "legs of the trade, and what went on each?",
       "The rising on St Jan in 1733 and the rising on Bornholm in 1658 are told very "
       "differently in Danish history. Why?",
       "What did the ordinance of 16 March 1792 actually order, and what happened in the ten "
       "years that followed?",
       "The state measured every Danish farm in 1662, every Danish field in 1682, and ruled St "
       "Croix into lots in 1734. Why is only the third never counted as an achievement of the "
       "enlightened state?",
       "The <i class=\"dk\">Fredensborg</i> is the best-documented slave ship in the world. "
       "What do its papers record, and what do they not?"],
   figs=[("s03", "SVG_TRIANGLE",
          "Figure 1 · The triangle, weighed",
          "Every Danish voyage began and ended in Copenhagen. Out went Indian cotton above "
          "all, then other textiles, firearms, gunpowder and brandy; across went people, two "
          "to three months, about one in five of whom did not arrive; home came raw sugar, "
          "refined in Copenhagen under monopoly and sold in two kingdoms. Between the 1660s "
          "and 1803, something between a hundred thousand and a hundred and eleven thousand "
          "people were carried in Danish ships on about 430 voyages — 2.3 per cent of the "
          "Atlantic traffic, which made Denmark the seventh largest of the nations that did it."),
         ("s06", "SVG_SURVEYS",
          "Figure 2 · The same habit, three times",
          "One state, seventy years, three ways of writing land down. In 1662–64 every farm in "
          "the kingdom was converted into one unit, <i class=\"dk\">hartkorn</i>, without "
          "anything being measured. In 1682–83 every cultivated field was walked and measured "
          "and its soil graded, four sworn peasants per district going with the surveyors. In "
          "1734 an island bought the year before was ruled into uniform lots on a grid and "
          "handed to shareholders, who cleared it and planted cane. The first two are told in "
          "Denmark as the state learning to see itself. The third is the same instrument in the "
          "same century."),
         ("s04", "SVG_PAPERS",
          "Figure 3 · What the papers keep",
          "The <i class=\"dk\">Fredensborg</i>, 1767–68, is the best-documented slave ship in "
          "the world. Its papers record the master, the carpenter who died on 4 January 1768, "
          "the other thirty-odd of the crew by name, the wind and the ship's position every "
          "day, and the cargo itemised. They do not record the names of the people in the hold, "
          "where in Africa they were taken from, what languages they spoke, who among them was "
          "related to whom, or anything any of them said. The asymmetry is not a gap in the "
          "archive. It is what the archive was for."),],
 ),

 31: dict(
   file='c31_body.html',
   part='Part G', band='Absolutism', num=31, dates='1784 – 1814',
   title='The flourishing trade and the wreck of it',
   people='Frederik 6. · Ernst Schimmelmann · Peter Willemoes · Kamma Rahbek · Edmund Bourke',
   hook="Twenty years of neutrality make Copenhagen rich carrying other people's cargo. Then "
        "the British take the fleet in three nights of bombardment, the state currency is "
        "written down to a sixth in a single ordinance, and Norway — four hundred years in the "
        "same realm — is signed away in an afternoon at Kiel. In the same year Denmark orders "
        "seven years of school for every child in the country.",
   keys=['den florissante handelsperiode', 'væbnet neutralitet',
         'slaget på Reden 1801', 'Københavns bombardement 1807', 'kanonbådskrigen',
         'statsbankerotten 1813', 'rigsbankdaler', 'Kieltraktaten 1814',
         'Eidsvoll 1814', 'skoleloven 1814'],
   qs=["What was a neutral bottom worth between 1793 and 1807, and why did that make "
       "Copenhagen rich?",
       "The British attacked a neutral country and took its fleet. On what argument — and "
       "what would Denmark have had to do to avoid it?",
       "The reform of 5 January 1813 is remembered as the state bankruptcy. Why is that name "
       "wrong, and what actually happened to people holding notes?",
       "Norway was ceded at Kiel and refused to go. What did the Norwegians do instead, and "
       "what did they keep?",
       "In the same year as Kiel, Denmark ordered seven years of school for every child. How "
       "does a bankrupt state do that, and why then?"],
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
          "The prize of September 1807, by rate: seventeen ships of the line, seventeen "
          "frigates, nineteen smaller vessels and twenty-six gunboats — seventy-nine hulls, "
          "together with nearly everything in the naval stores. The ships standing on the "
          "stocks were destroyed where they stood, so that what remained could not be rebuilt "
          "quickly. Denmark had been a naval power since the fifteenth century. It stopped "
          "being one in six weeks."),
         ("s07", "SVG_DALER",
          "Figure 3 · Six for one, 5 January 1813",
          "Six old <i class=\"dk\">kurantdaler</i> notes exchanged for one new "
          "<i class=\"dk\">rigsbankdaler</i>: five sixths of the paper money written off at a "
          "stroke, against a note that had already fallen to about six per cent of face value "
          "in silver. What backed the new one was a charge of six per cent on the value of all "
          "fixed property in Denmark, Norway, Slesvig and Holstein, payable in silver or "
          "standing as a first mortgage at 6.5 per cent a year. Every house, farm and workshop "
          "in the realm was made security for the new notes."),],
 ),
 32: dict(
   file='c32_body.html',
   part='Part H', band='The national century', num=32, dates='1814 \u2013 1848',
   title='Golden Age and national awakening',
   people='Christian 8. \u00b7 N.F.S. Grundtvig \u00b7 Peter Larsen Skr\u00e6ppenborg \u00b7 '
          'Johanne Luise P\u00e4tges \u00b7 Peter Hiort Lorenzen \u00b7 Christian Flor',
   hook="A bankrupt state that has just lost Norway hands control of its money to a bank it "
        "does not run, prosecutes farm servants for praying in the wrong room, and pays for "
        "the finest art it will ever produce. Then it concedes four assemblies with the "
        "widest franchise in Europe and no power at all \u2014 and in one of them a merchant "
        "from Haderslev stands up and speaks Danish.",
   keys=['guldalder', 'gudelige forsamlinger', 'Konventikelplakaten', 'Nationalbanken',
         'st\u00e6nderforsamling', 'hartkorn', 'kornsalgsperioden',
         'Bondevennernes Selskab', 'sprogreskript', 'sprogpatent',
         'slesvig-holstenisme', 'Ejderpolitik', 'folkeh\u00f8jskole', 'Det \u00e5bne Brev'],
   qs=["Denmark swapped Swedish Pomerania for Lauenburg in 1815 and took cash as well. Why "
       "was the smaller duchy worth more than the larger province?",
       "An absolute monarchy gave away control of its currency in 1818 and control of "
       "nothing else. What was it buying, and from whom?",
       "The Konventikelplakat and the Bondecirkul\u00e6re were both used to stop people "
       "organising, and both failed the same way. What was the mistake they shared?",
       "The Golden Age was produced by a state that could not pay its debts. Does that "
       "explain the art, or merely accompany it?",
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
          "two German ones, with the same powers and no power. About one Dane in forty "
          "could vote, a wider share than any country in Europe; women could not, whatever "
          "they owned, and Jews could vote but not be elected."),
         ("s07", "SVG_RYE",
          "Figure 3 \u00b7 The price of a t\u00f8nde of rye, 1815\u20131848",
          "The Zealand kapitelstakst in rigsbankdaler. The collapse to the late 1820s is "
          "\u00a702's crisis and the recovery is \u00a707's boom, and no prose in the "
          "chapter can do what one line does here.")],
 ),
}


# ---------------------------------------------------------------- draft parsing
def load():
    return open(DRAFT, encoding="utf-8").read()


def chapter(src, n):
    """(prose, apparatus) for chapter n."""
    ms = [m for m in re.finditer(r'^# Chapter (\d+)(.*)$', src, re.M)]
    body = app = None
    for i, m in enumerate(ms):
        if int(m.group(1)) != n:
            continue
        end = ms[i + 1].start() if i + 1 < len(ms) else len(src)
        seg = src[m.start():end]
        if 'apparatus' in m.group(2):
            app = seg
        else:
            body = (body or "") + seg
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
    m = re.search(r'^## %s\s*$' % re.escape(heading), app, re.M)
    if not m:
        return ""
    nxt = re.search(r'^## ', app[m.end():], re.M)
    return app[m.end():m.end() + (nxt.start() if nxt else len(app))]


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
    lines = [l for l in md.split('\n')]
    head = inline(lines[0]).replace('<strong>', '').replace('</strong>', '')
    rest = "\n".join(lines[1:]).strip()
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
    "in this section" heading wrong on every ranged block in the part."""
    blk = apparatus_part(app, 'Danish terms, by section')
    out = {}
    cur = None
    for m in re.finditer(r'^\*\*§(\d+)(?:\s*[\u2013\u2014-]\s*(\d+))?[^\n]*\*\*\s*$'
                         r'|^-\s+\*\*(.+?)\*\*\s+—\s+(.+?)(?=\n(?:-|\*\*|\Z))',
                         blk, re.M | re.S):
        if m.group(1):
            a = int(m.group(1))
            b = int(m.group(2)) if m.group(2) else a
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
def meanwhile_html(app):
    blk = apparatus_part(app, 'Meanwhile in Europe')
    out = []
    for _, p in [x for x in paras(blk) if x[0] == 'p']:
        m = re.match(r'\*\*(.+?)\*\*\s*(.*)', p, re.S)
        if not m:
            continue
        out.append('<div class="meanwhile">\n<h4>Meanwhile · %s</h4>\n<p>%s</p>\n</div>'
                   % (inline(m.group(1)), inline(m.group(2))))
    return out


def myth_html(app):
    blk = apparatus_part(app, 'Myth-check')
    o = ['<div class="myth" id="myth">', '<h4>Myth-check</h4>', '<dl>']
    items = [p for k, p in paras(blk) if k == 'p']
    i = 0
    while i < len(items):
        claim = items[i].strip()
        if claim.startswith('**"') or claim.startswith('**\u201c') or claim.startswith('"'):
            dt = inline(claim)
            dd = inline(items[i + 1]) if i + 1 < len(items) else ''
            o.append('  <dt>%s</dt>' % dt.replace('<strong>', '').replace('</strong>', ''))
            o.append('  <dd>%s</dd>' % dd)
            i += 2
        else:
            i += 1
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

    mw = meanwhile_html(app)
    mw_at = {secs[2][0]: 0, secs[min(6, len(secs) - 1)][0]: 1} if len(mw) >= 2 else {}

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

    o += ['<hr class="div">', '', myth_html(app), '',
          '<p class="kicker">Threads and links</p>',
          '<h2 id="forward" style="margin-top:0"><span class="n">WHERE THIS GOES</span>'
          'What to carry forward</h2>', calls_html(app), '',
          '<p class="kicker">Summary</p>',
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
        o += ['<p class="kicker">Closing Part G</p>',
              '<h2 id="coda" style="margin-top:0"><span class="n">1660 – 1814</span>'
              'What this part was about</h2>', '', prose_html(coda[0][3]), '']

    o += ['<footer>', '  Chapter %d · %s · %s' % (n, h['part'], h['dates']), '</footer>',
          '', '</div>', '{{JS}}', '</body>', '</html>', '']

    out = "\n".join(o)
    open(h['file'], 'w', encoding='utf-8').write(out)

    nsec = len([s for s in secs if s[0] != 'coda'])
    print("chapter %d -> %s" % (n, h['file']))
    print("  sections %d | terms %d | vignettes %d | meanwhile %d | figures %d"
          % (nsec, out.count('class="terms"'), out.count('class="vig"'),
             out.count('class="meanwhile"'), out.count('<figure>')))
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
