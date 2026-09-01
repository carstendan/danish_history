# -*- coding: utf-8 -*-
#
# Vocabulary note: the CSS class names below are still .band / .entry / .entries.
# Renaming them is cosmetic and would touch every rule in the stylesheet, so they
# are deliberately left alone. What the reader sees, and every anchor, uses the
# settled vocabulary: part / chapter / section.
import glob
import html as H
import os
import re

# Chapter pages are discovered on disk rather than hard-coded, so a chapter gets
# a working link the moment it is built and never a broken one before that. Point
# this at wherever the built pages live.
CHAPTER_DIR = os.environ.get("DK_CHAPTERS", "/mnt/user-data/outputs")


def built_chapters(d=CHAPTER_DIR):
    """A chapter ships as one page. Until August 2026 a chapter that ran long could
    also ship as two lettered halves, 16a and 16b; that device is retired, and a
    chapter that needs two pages is now given two numbers when the part is
    planned. The suffix group is kept only so an old file is still recognised."""
    found = {}
    for f in sorted(glob.glob(os.path.join(d, "[0-9][0-9]*.html"))):
        m = re.match(r"(\d\d)([a-z]?)-", os.path.basename(f))
        if m:
            found.setdefault(int(m.group(1)), []).append(
                (m.group(2), os.path.basename(f)))
    return {k: [v for _, v in sorted(vs)] for k, vs in found.items()}


BUILT = built_chapters()

BANDS = [
 ("A","Stone Age","c. 13,000 – 1,700 BCE","#8E9182",
  "Ice, then forest, then fields. Three chapters for eleven thousand years."),
 ("B","Bronze and Iron Age","c. 1700 BCE – 750 CE","#B8761F",
  "The North joins a continental economy — amber out, bronze and Roman silver in."),
 ("C","Viking Age","c. 750 – 1050","#96591A",
  "Raiding, trading, town-building, and the assembly of a Christian kingdom."),
 ("D","High Middle Ages","1050 – 1375","#3E8474",
  "Church, law, crusade and crisis. The kingdom learns to survive its kings."),
 ("E","Union and late Middle Ages","1375 – 1536","#2E6B5E",
  "Denmark at its largest reach — and the two ruptures that ended it."),
 ("F","Early modern power","1536 – 1660","#8A2B2B",
  "A Baltic great power overreaches, and loses the eastern provinces for good."),
 ("G","Absolutism","1660 – 1814","#A9601C",
  "Enevælde, an overseas empire built on enslaved labour, reform, and catastrophe."),
 ("H","Nation-state","1814 – 1901","#5B7A4A",
  "A small country invents itself: constitution, defeat, cooperatives, democracy."),
 ("I","Twentieth century","1901 – 1955","#3A342A",
  "Neutrality, reunification, occupation, and the welfare state's foundations."),
]

# entries carrying several distinct stories; candidates to run long or to split in two
DENSE = {35, 41}

# (num, band_index, title, datelabel, mid_year, gloss, markers)
E = [
(1,0,"Reindeer hunters and the retreating ice","c. 13,000 – 9,000 BCE",-11000,
 "Small bands follow reindeer herds onto tundra newly freed by the Weichsel ice. Denmark is not yet islands, and Britain is walkable.",
 ["Weichsel glaciation","Hamburgkultur","Brommekultur","Ahrensburgkultur","Doggerland"]),
(2,0,"Coast and forest: the hunter Stone Age","c. 9,000 – 3,950 BCE",-6475,
 "Five millennia of hunting, fishing and gathering along a rising sea. The richest hunter-gatherer archaeology in Europe sits in Danish shell middens.",
 ["Maglemosekultur","Kongemosekultur","Ertebøllekultur","køkkenmøddinger (shell middens)","Vedbæk graves"]),
(3,0,"First farmers and the megalith builders","c. 3,950 – 1,700 BCE",-2825,
 "Farming arrives in a couple of centuries and rebuilds the landscape. Some 25,000 megalithic tombs are raised; DNA now says the farmers largely replaced the hunters.",
 ["Tragtbægerkultur (Funnel Beaker)","dysser & jættestuer","Enkeltgravskultur","Sarup enclosures","flint mines at Stevns"]),
(4,1,"Bronze Age: amber, sun and the long road south","c. 1700 – 500 BCE",-1100,
 "No local copper or tin, yet Denmark fills with bronze — paid for in amber and traded down to the Mediterranean. A confident, sun-worshipping chiefdom society.",
 ["Solvognen (the sun chariot)","Egtvedpigen","lurer","gravhøje","amber route to Mycenae"]),
(5,1,"Pre-Roman Iron Age: bogs, war-boats and the Celtic world","c. 500 BCE – 1 CE",-250,
 "Bronze imports collapse; bog iron makes tools local and cheap. Weapons, cauldrons and people go into the bogs — sacrifices we can still look in the face.",
 ["Hjortspringbåden","Gundestrupkarret","Tollundmanden","myremalm (bog iron)","La Tène contacts"]),
(6,1,"Roman Iron Age: living beside the empire","c. 1 – 400 CE",200,
 "Denmark lies outside the limes but inside the Roman economy. Imported glass and silver mark new elites; war-booty deposits show organised armies of hundreds.",
 ["Illerup Ådal","Himlingøje graves","Roman imports","Tacitus' Germania","the limes"]),
(7,1,"Germanic Iron Age and the Migration Period","c. 400 – 750",575,
 "Rome's collapse reshuffles the North. Gold is buried in quantity, a people called the Dani is named, and the first Danevirke ramparts go up.",
 ["Guldhornene fra Gallehus","Gudme–Lundeborg","Jordanes names the Dani","Danevirke begun c. 700","gold hoards of 536"]),
(8,2,"Ships and raids: the Viking Age opens","c. 750 – 900",825,
 "A shipbuilding advance turns coastal raiders into transoceanic ones. Denmark's share of the Viking world points west and south: England, Frisia, Francia.",
 ["Lindisfarne 793","the Great Heathen Army 865","Danelaw","Rollo & Normandy 911","longship technology"]),
(9,2,"Towns, silver and the trade world","c. 700 – 1000",850,
 "The other Viking Age: Ribe and Hedeby as market towns wired into a network that reaches Baghdad. Arabic silver arrives by the tonne.",
 ["Ribe c. 700","Hedeby","Arabic dirhams","Birka & Kaupang","the Volga route"]),
(10,2,"One kingdom, one faith: Jelling","c. 950 – 1000",975,
 "Harald Bluetooth's stone claims Denmark, Norway and Christianity in one sentence. The ring fortresses show a state that could command real labour.",
 ["Gorm den Gamle","Harald Blåtand","Jellingstenen","trelleborge (Trelleborg, Fyrkat, Aggersborg)","Poppo's ordeal"]),
(11,2,"The North Sea Empire","c. 1000 – 1066",1035,
 "Sweyn conquers England; Cnut rules England, Denmark and Norway together. The largest state ever run from Denmark lasts barely a generation.",
 ["Svend Tveskæg","Knud den Store","Danegæld","Harald Hardrada","Stamford Bridge 1066"]),
(12,3,"Kingdom and church take shape","1050 – 1157",1100,
 "Dioceses, tithes and stone churches arrive. A murdered king becomes a saint, Lund gets its own archbishop, and the succession dissolves into civil war.",
 ["Svend Estridsen","Knud den Hellige 1086","Lund archbishopric 1104","Saxo Grammaticus","Grathe Hede 1157"]),
(13,3,"The Valdemar age and the Baltic crusades","1157 – 1241",1200,
 "A century of expansion east and south under Valdemar I, Absalon and Valdemar II. Denmark takes Estonia, founds Copenhagen, and then loses it all at Bornhøved.",
 ["Absalon & København 1167","Rügen 1169","Lyndanisse 1219 (Dannebrog legend)","Bornhøved 1227","Valdemar Sejr"]),
(14,3,"Law, regicide and the mortgaged realm","1241 – 1340",1290,
 "Jyske Lov opens with a line Danes still quote. Then a king is murdered in a barn, charters bind the crown, and the whole country is pawned to German counts.",
 ["Jyske Lov 1241","håndfæstning 1282","Finderup Lade 1286","Erik Klipping & Erik Menved","Grev Gert; the kingless years 1332–40"]),
(15,3,"Plague and reconquest: Valdemar Atterdag","1340 – 1375",1360,
 "A king with almost nothing buys, marries and fights the kingdom back together, through the Black Death and a losing war with the Hanse.",
 ["Black Death 1349","Skåne bought back 1360","sack of Visby 1361","Peace of Stralsund 1370","Valdemar Atterdag"]),
(16,4,"Margrete I and the making of the union","1375 – 1397",1386,
 "The most capable ruler in Danish history assembles three kingdoms without ever formally being queen of them, and it ends at Kalmar in 1397 — the high-water mark of Nordic unity.",
 ["Oluf & Håkon","Falsterbo 1387","Falköping 1389","Kalmar 1397","Margrete's statecraft"]),
(17,4,"The union at work, and the end of Margrete","1397 – 1412",1405,
 "What the union was day to day: an administration rather than a document. Norway slides from partner to province, the last ship sails from Greenland, and the deserted farms reshape who works the land.",
 ["Erik af Pommern","Norway from partner to province","Hvalsey 1408","ødegårde","Birgitta & sjælegave"]),
(18,4,"Sound Dues, the Hanse and a straining union","1412 – 1460",1435,
 "Erik of Pomerania starts charging every ship that passes Helsingør — an income that shapes Danish policy for 428 years — and picks a losing fight with Lübeck.",
 ["Øresundstolden 1429","Hansestæderne","Erik deposed 1439","Christoffer af Bayern","Christian I 1448 (Oldenburg)"]),
(19,4,"Schleswig-Holstein and the union's collapse","1460 – 1523",1490,
 "Ribebrevet ties the duchies to the crown with a phrase that will detonate in 1848. Sweden walks out after a bloodbath in Stockholm.",
 ["Ribebrevet 1460 ('up ewig ungedeelt')","Kong Hans","Ditmarsken 1500","Stockholms Blodbad 1520","Gustav Vasa 1523"]),
(20,4,"Reformation and the Count's Feud","1523 – 1536",1530,
 "A civil war fought over religion, a deposed king and burgher power ends with a Lutheran state church, a bankrupt nobility's rescue, and the bishops in prison.",
 ["Christian II deposed","Frederik I","Grevens Fejde 1534–36","Christian III","kirkeordinansen 1537"]),
(21,5,"The Lutheran realm of the nobility","1536 – 1588",1560,
 "Crown and nobility split a newly rich state between them. The first serious war with the new Sweden settles nothing and costs a fortune.",
 ["adelsvælden","Rigsrådet","Nordic Seven Years' War 1563–70","Tycho Brahe & Uraniborg","Peder Palladius"]),
(22,5,"Christian 4.: ambition and the building years","1588 – 1625",1606,
 "The king every Dane can name, in the half of his reign that worked: towns founded, spires raised, companies chartered, Norway governed hard — and one war with Sweden that settles nothing.",
 ["formynderregeringen 1588–96","Kalmarkrigen 1611–13","Frederiksborg, Rosenborg, Børsen","Christianshavn 1618","Trankebar 1620"]),
(23,5,"Christian 4.: the wars that broke him","1625 – 1648",1636,
 "Sixty years of building are undone in twenty. He enters the Thirty Years' War as a German prince, loses, and watches a Swedish army march into Jutland twice.",
 ["Lutter am Barenberge 1626","Wallenstein i Jylland 1627–29","Rundetårn 1637–42","Torstenssonkrigen 1643–45","Kolberger Heide 1644"]),
(24,5,"Losing the eastern provinces","1645 – 1660",1652,
 "Brømsebro takes a bite; then a Swedish army walks across the frozen Belts and Roskilde 1658 amputates Skåne, Halland and Blekinge. Copenhagen holds — barely.",
 ["Brømsebro 1645","Karl Gustav's march over the ice 1658","Roskilde 1658","Stormen på København 1659","Copenhagen 1660"]),
(25,6,"The kingdom made hereditary","1660 – 1670",1665,
 "An assembly called to settle a war debt hands the king more power than any monarch in Europe, and does it by a vote. What replaces the charter is a state of standing offices and a register that reduces every farm to one number.",
 ["Stændermødet 1660","Arvehyldning 18. oktober 1660","Kongeloven 1665","kollegier og amter","matriklen 1662 og 1664"]),
(26,6,"Law, rank, and the war for Skåne","1670 – 1699",1685,
 "Birth is replaced by a table of ranks and the realm gets one code of law. It also spends four years trying to take Skåne back, wins at sea, loses on land, and hands every conquest back on a French instruction.",
 ["rangforordningen 1671","Danske Lov 1683","Griffenfeld","Den Skånske Krig 1675–79","Køge Bugt 1677"]),
(27,6,"The last war for the Sound","1699 – 1721",1710,
 "The last Danish attempt to reverse 1658 fails, but Sweden's collapse ends the Swedish threat and closes the southern border. In between, plague takes something near a third of Copenhagen.",
 ["Poltava 1709","Helsingborg 1710","pesten 1711","Tordenskjold","Frederiksborgfreden 1720"]),
(28,6,"The bound countryside and the pious state","1721 – 1770",1745,
 "Half a century of peace in which Danish countrymen are not free. Every man of the peasantry is tied to the estate where he was born, and a pietist king puts one catechism into every parish in two kingdoms.",
 ["stavnsbånd 1733","hoveri","konfirmation 1736","Pontoppidan 1737","rytterskolerne"]),
(29,6,"Struensee, and the village taken apart","1770 – 1788",1779,
 "A German doctor governs Denmark for sixteen months through a king who cannot, and is executed for it. Then the state takes the village apart field by field and unties the bond of 1733.",
 ["kabinetsordrer","Struensee 1770–72","udskiftning","stavnsbåndet 1788","Frihedsstøtten"]),
(30,6,"The Danish Atlantic","1620 – 1803",1711,
 "Forts on the Gold Coast, three Caribbean islands and the ships between them. About a hundred thousand people were carried in Danish bottoms; in 1792 Denmark ordered the trade ended, with a ten-year delay written in.",
 ["Trankebar 1620","Christiansborg, Guldkysten","St. Thomas 1672 · St. Jan 1718 · St. Croix 1733","trekantshandelen","forordningen af 1792"]),
(31,6,"The flourishing trade and the wreck of it","1784 – 1814",1799,
 "Twenty years of neutrality make Copenhagen rich carrying other people's cargo. Then the British take the fleet, the currency is written down to a sixth, and Norway is signed away at Kiel.",
 ["den florissante handelsperiode","Slaget på Reden 1801","bombardementet 1807","statsbankerotten 1813","Kieltraktaten 1814"]),
(32,7,"Golden Age and national awakening","1814 – 1848",1830,
 "Bankrupt, shrunken and culturally extraordinary. Grundtvig, Kierkegaard, Andersen and Eckersberg build a national self-image just as absolutism starts to crack.",
 ["Guldalderen","N.F.S. Grundtvig","Søren Kierkegaard","H.C. Andersen","stænderforsamlinger 1834"]),
(33,7,"1848: constitution and the First Schleswig War","1848 – 1852",1850,
 "Absolutism ends without a shot in Copenhagen — and immediately a three-year war begins over Schleswig. The June Constitution is startlingly liberal for 1849.",
 ["Junigrundloven 5 June 1849","Treårskrigen 1848–50","Fredericia 1849","Isted 1850","London Protocol 1852"]),
(34,7,"1864","1863 – 1864",1864,
 "The defining national trauma. A constitution that broke the 1852 settlement, an abandoned Danevirke, Dybbøl, and the loss of a third of the state's territory.",
 ["Novemberforfatningen 1863","Danevirke abandoned Feb 1864","Dybbøl 18 April","Als June 1864","Vienna peace; 'hvad udad tabes...'"]),
(35,7,"Industry, cooperatives, emigration and labour","c. 1870 – 1901",1885,
 "Cheap American grain nearly kills Danish farming; the andelsbevægelse turns it into butter and bacon exports instead. Meanwhile the labour movement organises.",
 ["andelsbevægelsen","first andelsmejeri 1882","Louis Pio & the labour movement","Septemberforliget 1899","emigration to America"]),
(36,7,"Provisorietiden and the change of system","1875 – 1901",1895,
 "Estrup governs for two decades against a hostile majority using provisional laws. When it finally breaks in 1901, Denmark has parliamentary government.",
 ["J.B.S. Estrup","provisoriske love","Københavns befæstning","Systemskiftet 1901","parlamentarisme"]),
(37,8,"Reform, neutrality and the sale of the West Indies","1901 – 1917",1910,
 "Women get the vote in 1915. Denmark stays out of the war and gets rich on it — then sells its Caribbean islands to the United States for 25 million dollars.",
 ["1915 Grundlov (women's suffrage)","WWI neutrality","gullaschbaroner","sale of Dansk Vestindien 1917","Iceland's Act of Union 1918"]),
(38,8,"1920: Genforeningen and the Easter Crisis","1918 – 1920",1920,
 "Versailles lets North Schleswig vote itself home — and the king's attempt to grab more nearly ends the monarchy in the process.",
 ["the 1920 plebiscites","Zone 1 & Zone 2","Genforeningen","Påskekrisen 1920","Christian X at the border"]),
(39,8,"Depression, Stauning and the seeds of the welfare state","1929 – 1939",1934,
 "One long night's bargaining in Kanslergade produces the crisis deal and the social reform that later gets called the welfare state's foundation stone.",
 ["Thorvald Stauning","Kanslergadeforliget 1933","Socialreformen 1933 (K.K. Steincke)","'Stauning eller kaos'","non-aggression pact 1939"]),
(40,8,"9 April 1940 and samarbejdspolitikken","1940 – 1943",1941,
 "Occupied in six hours. Denmark then does something almost unique: it keeps its government, parliament and king, and cooperates — a choice still argued about.",
 ["Operation Weserübung","the 'model protectorate'","Erik Scavenius","Frikorps Danmark","the 1943 election"]),
(41,8,"1943–1945: rupture, rescue, resistance","1943 – 1945",1944,
 "Cooperation collapses in August 1943; the fleet scuttles itself; and in October almost all of Denmark's Jews are ferried to Sweden in three weeks.",
 ["Augustoprøret 1943","the fleet scuttled 29 Aug","rescue of the Danish Jews Oct 1943","Frihedsrådet","Shellhus March 1945; liberation 4–5 May"]),
(42,8,"Settling accounts and choosing a side","1945 – 1949",1947,
 "Retribution trials, a reintroduced death penalty, a Soviet garrison on Bornholm for eleven months, Marshall aid — and the end of 150 years of neutrality.",
 ["retsopgøret","Soviet Bornholm May 1945 – April 1946","Marshall aid","Scandinavian defence talks fail","NATO 4 April 1949"]),
(43,8,"1953: the new constitution and the modern realm","1949 – 1955",1952,
 "The Landsting goes, female succession comes, Greenland stops being a colony on paper, and the welfare state begins its long build-out.",
 ["Grundloven 1953","Landstinget abolished","female succession","Greenland made a county 1953","the welfare state expands"]),
]

THREADS = [
 ("The border in the south",
  "Danevirke → Ribebrevet 1460 → 1848 → 1864 → 1920 → today",
  "Denmark's only land border has been the country's central political problem for 1,300 years. Following it explains more Danish history than any single reign."),
 ("Denmark and Sweden",
  "union partner → arch-enemy → neighbour",
  "Eleven wars between 1521 and 1814. The relationship swings from Kalmar to Roskilde to Nordic cooperation, and it defines what 'Denmark' territorially means."),
 ("The sea as income",
  "amber · Sound Dues · neutral shipping · Mærsk",
  "A small country astride the entrance to the Baltic. Tolls, freight and neutrality trade have paid Denmark's bills since the Bronze Age, and shaped its foreign policy."),
 ("The realm beyond Denmark",
  "Norway · Iceland · Faroes · Greenland · Skåne · Estonia · India · Ghana · the Caribbean",
  "For most of its history Denmark was a composite state, not a nation-state. Tracking the possessions — and how each was let go — is a history of the country's self-image."),
 ("From great power to small state",
  "1397 → 1658 → 1814 → 1864 → 1940 → 1949",
  "A four-century contraction, and the intellectual work done to make it feel like a virtue. This thread carries the myth-checks."),
 ("Faith and the state",
  "Norse cult → Catholic church → Lutheran state church → secular society",
  "Religion as instrument of state-building: Harald's conversion, the 1536 Reformation, Grundtvig's popular Christianity, and the folkekirke today."),
]

MAPS = [
 ("1050","Cnut's empire has just dissolved; the kingdom's medieval shape appears"),
 ("1250","Valdemar expansion at maximum, Estonia held"),
 ("1397","The Kalmar Union — the largest extent ever ruled from Denmark"),
 ("1500","Union fraying; the duchies attached"),
 ("1600","Christian IV's Denmark-Norway, Skåne still Danish, the Sound closed on both sides"),
 ("1658","Roskilde: the eastern provinces gone"),
 ("1721","Post-Great Northern War; Gottorp settled"),
 ("1814","Norway lost at Kiel"),
 ("1864","Schleswig, Holstein and Lauenburg gone — the smallest Denmark"),
 ("1920","Genforeningen; the present border drawn"),
 ("1945","Iceland independent, the West Indies sold, Greenland and the Faroes remaining"),
]

# Counts that used to be typed into the prose below and drifted every time the
# spine changed: the header line computed len(E) and stayed right while the fan
# caption, the aria-label and the stat block all went stale. Compute them.
NUMWORD = {0: "No", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six"}
AFTER_750 = len([r for r in E if r[1] >= 2])          # Viking Age onward
PCT_AFTER = round(100.0 * AFTER_750 / len(E))


PAGETYPES = [
 ("Era", str(len(E)), "The chronological spine listed below. Each chapter is self-contained but carries callbacks to earlier chapters. %s are flagged dense and are likely to be planned as two." % NUMWORD[len(DENSE)], "#2E6B5E"),
 ("Thread", "6 pages", "One question followed across all eras — the border, Sweden, the sea, the realm, contraction, faith.", "#A9601C"),
 ("Spotlight", "open-ended", "A single object, ship, battle or person, examined closely. Queued: Fregatten Jylland.", "#8A2B2B"),
 ("Place", "open-ended", "One location followed through every era it appears in. Queued: Bornholm.", "#5B7A4A"),
]

ANATOMY = [
 ("Header block","Dates, 4–6 key names, and one line on why the period matters. Makes the page usable as reference later."),
 ("Introduction","The 3–4 questions this page answers. Primes what to look for."),
 ("Narrative","The main text. Danish terms kept and glossed on first use."),
 ("Vignette","A named person at a specific hour in a specific place. One to three per page. In prehistory these are usually the excavators; from the Viking Age on, people inside the events."),
 ("Meanwhile in Europe / the world","A distinct box so the wider context doesn't get swallowed by the Danish story."),
 ("Maps","SVG, inline, no external files. Real Natural Earth coastlines, one shared projection."),
 ("Checkpoint","Two or three recall questions dropped mid-page, next to what they test — not saved for the end, when attention is lowest."),
 ("Myth-check","Where the schoolbook version is wrong, and what replaced it."),
 ("Callbacks","Two or three pointers back to earlier chapters, so the whole spine reads as one story."),
 ("Summary","If you remember five things from this page, these. Closes the loop opened by the introduction."),
 ("Questions & discussion","Recall · causal · counterfactual · contested. The last kind is where the real work is."),
 ("Sources & places to visit","A light source line, plus what still stands that you can go and look at."),
]

SOURCES = [
 ("danmarkshistorien.dk","https://danmarkshistorien.dk","Aarhus University. Nine period chapters, c. 45 pages each, from c. 790 to the present — the academic backbone."),
 ("lex.dk","https://lex.dk","Den Store Danske, Trap Danmark and Danmarks Oldtid (Jørgen Jensen) in one searchable place."),
 ("Nationalmuseet","https://natmus.dk","Prehistory and the object record — the authority for anything before c. 800."),
 ("Danmarks Oldtid","https://danmarksoldtid.lex.dk","Jørgen Jensen's four volumes, online. The standard work on prehistory."),
]

# ---------- geometry for the signature diagram ----------
Y0, Y1 = -13000.0, 1953.0
SPAN = Y1 - Y0
X0, X1 = 62.0, 946.0
W = X1 - X0

def tx(y):
    return X0 + (y - Y0) / SPAN * W

n = len(E)
def bx(i):
    return X0 + i * (W / (n - 1))

fan = []
for i, e in enumerate(E):
    num, bi, title, dl, mid, gloss, marks = e
    col = BANDS[bi][3]
    x_top, x_bot = tx(mid), bx(i)
    fan.append(
      f'<path d="M{x_top:.1f} 62 C{x_top:.1f} 96, {x_bot:.1f} 104, {x_bot:.1f} 138" '
      f'fill="none" stroke="{col}" stroke-width="1.1" opacity=".72"/>'
    )
    fan.append(f'<circle cx="{x_top:.1f}" cy="61" r="1.7" fill="{col}"/>')
    fan.append(f'<rect x="{bx(i)-0.6:.1f}" y="138" width="1.2" height="7" fill="{col}"/>')

topticks = []
for y, lab in [(-13000,"13,000 BCE"),(-10000,"10,000"),(-5000,"5,000"),(-2000,"2,000"),
               (1,"1 CE"),(1000,"1000"),(1953,"1953")]:
    x = tx(y)
    topticks.append(f'<rect x="{x-0.5:.1f}" y="48" width="1" height="6" fill="#9A9C90"/>')
    anc = "start" if y == -13000 else ("end" if y == 1953 else "middle")
    dx = 0 if anc == "middle" else (2 if anc == "start" else -2)
    topticks.append(
      f'<text x="{x+dx:.1f}" y="42" class="ax" text-anchor="{anc}">{lab}</text>')

botticks = []
for i in range(0, n, 5):
    botticks.append(f'<text x="{bx(i):.1f}" y="160" class="ax" text-anchor="middle">{i+1:02d}</text>')
botticks.append(f'<text x="{bx(n-1):.1f}" y="160" class="ax" text-anchor="end">40</text>')

x750 = tx(750)
band_hl = (f'<rect x="{x750:.1f}" y="46" width="{X1-x750:.1f}" height="10" fill="#2E6B5E" opacity=".13"/>')

FAN = "\n      ".join(topticks + [band_hl] + fan + botticks)

# ---------- html ----------
def esc(s): return H.escape(s, quote=False)

bandnav = "\n".join(
  f'<a class="bn" href="#part-{b[0]}"><span class="bn-l" style="color:{b[3]}">{b[0]}</span>{esc(b[1])}</a>'
  for b in BANDS)

spine = []
for bi, b in enumerate(BANDS):
    letter, name, dates, col, blurb = b
    ents = [e for e in E if e[1] == bi]
    yrs = []
    for e in ents:
        pass
    spine.append(f'''
<section class="band" id="part-{letter}" style="--bc:{col}">
  <header class="band-h">
    <div class="band-l">{letter}</div>
    <div class="band-t">
      <h2>{esc(name)}</h2>
      <p class="band-d">{esc(dates)} <span class="sep">·</span> {len(ents)} {"chapter" if len(ents)==1 else "chapters"}</p>
      <p class="band-b">{esc(blurb)}</p>
    </div>
  </header>
  <ol class="entries">''')
    for e in ents:
        num, _, title, dl, mid, gloss, marks = e
        mk = "".join(f'<li>{esc(m)}</li>' for m in marks)
        flag = ' <span class="dense">dense</span>' if num in DENSE else ''
        pages = BUILT.get(num) or []
        if len(pages) == 1:
            heading = f'<a class="e-link" href="{esc(pages[0])}">{esc(title)}</a>'
        elif len(pages) > 1:
            bits = " ".join(
                f'<a class="e-link e-part" href="{esc(p)}">{chr(97 + i)}</a>'
                for i, p in enumerate(pages))
            heading = (f'<a class="e-link" href="{esc(pages[0])}">{esc(title)}</a>'
                       f' <span class="split">split: {bits}</span>')
        else:
            heading = f'{esc(title)} <span class="unbuilt">not yet written</span>'
        href = pages[0] if pages else None
        spine.append(f'''
    <li class="entry{' is-built' if href else ''}" id="c{num:02d}">
      <div class="e-num">{num:02d}</div>
      <div class="e-body">
        <h3>{heading}{flag}</h3>
        <p class="e-date">{esc(dl)}</p>
        <p class="e-gloss">{esc(gloss)}</p>
        <ul class="e-marks">{mk}</ul>
      </div>
    </li>''')
    spine.append("\n  </ol>\n</section>")
SPINE = "".join(spine)

THR = "\n".join(f'''
  <li class="thread">
    <h3>{esc(t)}</h3>
    <p class="th-path">{esc(p)}</p>
    <p class="th-b">{esc(d)}</p>
  </li>''' for t, p, d in THREADS)

MAPL = "\n".join(f'''
  <li class="map"><span class="map-y">{y}</span><span class="map-d">{esc(d)}</span></li>'''
  for y, d in MAPS)

PT = "\n".join(f'''
  <li class="ptype" style="--pc:{c}">
    <h3>{esc(n_)} <span class="pt-c">{esc(cnt)}</span></h3>
    <p>{esc(d)}</p>
  </li>''' for n_, cnt, d, c in PAGETYPES)

AN = "\n".join(f'''
  <li class="an"><span class="an-n">{esc(n_)}</span><span class="an-d">{esc(d)}</span></li>'''
  for n_, d in ANATOMY)

SRC = "\n".join(f'''
  <li><a href="{u}" rel="noopener">{esc(n_)}</a><span>{esc(d)}</span></li>'''
  for n_, u, d in SOURCES)

DOC = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Denmark, 13,000 BCE – 1953 · A reading plan</title>
<style>
  :root {{
    --ground:#E4E7E4;
    --paper:#F0F2EE;
    --peat:#221E18;
    --muted:#6C6E63;
    --rule:#C9CDC4;
    --verdigris:#2E6B5E;
    --amber:#A9601C;
    --oxblood:#8A2B2B;
    --serif:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua","URW Palladio L",Georgia,serif;
    --mono:"IBM Plex Mono",ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;
  }}
  *{{box-sizing:border-box}}
  html{{-webkit-text-size-adjust:100%}}
  body{{
    margin:0;background:var(--ground);color:var(--peat);
    font-family:var(--serif);font-size:17px;line-height:1.62;
    text-rendering:optimizeLegibility;
  }}
  .wrap{{max-width:1060px;margin:0 auto;padding:0 28px}}
  a{{color:var(--verdigris)}}
  a:focus-visible,.bn:focus-visible{{outline:2px solid var(--amber);outline-offset:3px}}

  /* ---- sticky band nav ---- */
  nav.bands{{
    position:sticky;top:0;z-index:20;background:rgba(228,231,228,.94);
    backdrop-filter:blur(6px);border-bottom:1px solid var(--rule);
  }}
  .bands-in{{max-width:1060px;margin:0 auto;padding:0 28px;display:flex;gap:0;overflow-x:auto;
    scrollbar-width:none}}
  .bands-in::-webkit-scrollbar{{display:none}}
  .bn{{
    font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;
    color:var(--muted);text-decoration:none;white-space:nowrap;padding:11px 15px 10px 0;
    display:flex;gap:7px;align-items:baseline;
  }}
  .bn:hover{{color:var(--peat)}}
  .bn-l{{font-weight:700;font-size:11.5px}}

  /* ---- hero ---- */
  header.hero{{padding:74px 0 8px}}
  .eyebrow{{
    font-family:var(--mono);font-size:11px;letter-spacing:.22em;text-transform:uppercase;
    color:var(--amber);margin:0 0 22px;
  }}
  h1{{
    font-size:clamp(42px,8vw,86px);line-height:.94;margin:0;font-weight:400;
    letter-spacing:-.025em;
  }}
  h1 em{{font-style:italic;color:var(--verdigris)}}
  .range{{
    font-family:var(--mono);font-size:13px;letter-spacing:.1em;color:var(--muted);
    margin:20px 0 0;
  }}
  .thesis{{max-width:60ch;font-size:19px;margin:26px 0 0}}
  .scope{{max-width:62ch;color:var(--muted);font-size:16px;margin:16px 0 0}}

  /* ---- signature diagram ---- */
  .sig{{margin:56px 0 0;padding:26px 0 22px;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}}
  .sig h2{{
    font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;
    color:var(--muted);font-weight:500;margin:0 0 4px;
  }}
  .sig p.cap{{max-width:64ch;color:var(--muted);font-size:15px;margin:0 0 18px}}
  .sig svg{{width:100%;height:auto;display:block;overflow:visible}}
  .ax{{font-family:var(--mono);font-size:9.5px;fill:#7D8074;letter-spacing:.04em}}
  .axlab{{font-family:var(--mono);font-size:9.5px;fill:#7D8074;letter-spacing:.1em;text-transform:uppercase}}
  .sig .stat{{
    display:flex;flex-wrap:wrap;gap:34px;margin:18px 0 0;
    font-family:var(--mono);font-size:11px;letter-spacing:.05em;color:var(--muted);
  }}
  .sig .stat b{{color:var(--oxblood);font-size:20px;font-weight:600;display:block;letter-spacing:-.01em}}

  /* ---- generic section ---- */
  section.blk{{padding:66px 0 0}}
  .kicker{{
    font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;
    color:var(--amber);margin:0 0 10px;
  }}
  .blk > h2{{font-size:31px;font-weight:400;letter-spacing:-.015em;margin:0 0 12px}}
  .lede{{max-width:64ch;color:var(--muted);margin:0 0 26px}}

  /* ---- spine ---- */
  .band{{margin:0 0 46px;padding:26px 0 0;border-top:1px solid var(--rule)}}
  .band-h{{display:flex;gap:20px;align-items:flex-start;margin:0 0 22px}}
  .band-l{{
    font-family:var(--mono);font-size:27px;font-weight:600;color:var(--bc);
    line-height:1;width:42px;flex:none;padding-top:5px;
  }}
  .band-t h2{{font-size:27px;font-weight:400;margin:0;letter-spacing:-.015em}}
  .band-d{{font-family:var(--mono);font-size:11.5px;letter-spacing:.08em;color:var(--muted);margin:6px 0 0}}
  .sep{{opacity:.5;padding:0 3px}}
  .band-b{{max-width:60ch;color:var(--muted);font-size:15.5px;margin:9px 0 0}}

  ol.entries{{list-style:none;margin:0;padding:0;display:grid;gap:2px}}
  .entry{{
    display:flex;gap:18px;background:var(--paper);padding:18px 20px;
    border-left:2px solid var(--bc);
  }}
  .entry:hover{{background:#F6F7F3}}
  .entry.is-built{{background:#F6F7F3}}
  .entry.is-built:hover{{background:#EFF1EC}}
  .e-link{{color:inherit;text-decoration:none;border-bottom:1.5px solid var(--bc)}}
  .e-link:hover{{border-bottom-width:3px}}
  .unbuilt{{font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;
    text-transform:uppercase;color:var(--muted);opacity:.65;vertical-align:2px}}
  .split{{font-family:var(--mono);font-size:10px;letter-spacing:.06em;color:var(--muted)}}
  .e-part{{padding:0 3px;font-weight:600}}
  .e-num{{
    font-family:var(--mono);font-size:12px;color:var(--bc);font-weight:600;
    padding-top:3px;width:24px;flex:none;letter-spacing:.03em;
  }}
  .e-body{{min-width:0}}
  .e-body h3{{font-size:19px;font-weight:600;margin:0;letter-spacing:-.008em;line-height:1.28}}
  .e-date{{font-family:var(--mono);font-size:11px;letter-spacing:.07em;color:var(--muted);margin:5px 0 0}}
  .dense{{font-family:var(--mono);font-size:9px;letter-spacing:.14em;text-transform:uppercase;
    color:var(--oxblood);border:1px solid var(--oxblood);border-radius:2px;padding:1px 5px;
    vertical-align:middle;font-weight:600;white-space:nowrap}}
  .e-gloss{{margin:9px 0 0;max-width:66ch;font-size:16px}}
  ul.e-marks{{list-style:none;display:flex;flex-wrap:wrap;gap:6px;margin:12px 0 0;padding:0}}
  ul.e-marks li{{
    font-family:var(--mono);font-size:10.5px;letter-spacing:.03em;color:var(--muted);
    border:1px solid var(--rule);border-radius:2px;padding:2.5px 7px;background:transparent;
  }}

  /* ---- threads ---- */
  ol.threads{{list-style:none;margin:0;padding:0;display:grid;gap:2px;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}
  .thread{{background:var(--paper);padding:20px 22px;border-top:2px solid var(--amber)}}
  .thread h3{{font-size:19px;font-weight:600;margin:0;letter-spacing:-.008em}}
  .th-path{{font-family:var(--mono);font-size:10.5px;letter-spacing:.03em;color:var(--amber);margin:8px 0 0;line-height:1.6}}
  .th-b{{margin:10px 0 0;font-size:15.5px;color:var(--muted)}}

  /* ---- maps ---- */
  ol.maps{{list-style:none;margin:0;padding:0;border-top:1px solid var(--rule)}}
  .map{{display:flex;gap:22px;padding:11px 0;border-bottom:1px solid var(--rule);align-items:baseline}}
  .map-y{{font-family:var(--mono);font-size:15px;font-weight:600;color:var(--verdigris);width:62px;flex:none}}
  .map-d{{color:var(--muted);font-size:15.5px}}

  /* ---- page types ---- */
  ol.ptypes{{list-style:none;margin:0;padding:0;display:grid;gap:2px;
    grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}}
  .ptype{{background:var(--paper);padding:18px 20px;border-top:2px solid var(--pc)}}
  .ptype h3{{font-size:18px;font-weight:600;margin:0;display:flex;justify-content:space-between;
    align-items:baseline;gap:10px}}
  .pt-c{{font-family:var(--mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;
    color:var(--muted);font-weight:400}}
  .ptype p{{margin:9px 0 0;font-size:15px;color:var(--muted)}}

  /* ---- anatomy ---- */
  ol.anat{{list-style:none;margin:0;padding:0;counter-reset:a;border-top:1px solid var(--rule)}}
  .an{{display:flex;gap:20px;padding:11px 0;border-bottom:1px solid var(--rule);align-items:baseline}}
  .an-n{{font-family:var(--mono);font-size:11.5px;letter-spacing:.06em;color:var(--peat);
    width:210px;flex:none;font-weight:600;text-transform:uppercase}}
  .an-d{{color:var(--muted);font-size:15.5px}}

  /* ---- conventions + sources ---- */
  ul.conv{{list-style:none;margin:0;padding:0;display:grid;gap:2px;
    grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}}
  ul.conv li{{background:var(--paper);padding:16px 18px}}
  ul.conv b{{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.13em;
    text-transform:uppercase;color:var(--amber);margin:0 0 7px;font-weight:600}}
  ul.conv span{{font-size:15px;color:var(--muted)}}

  ul.src{{list-style:none;margin:0;padding:0;border-top:1px solid var(--rule)}}
  ul.src li{{display:flex;gap:22px;padding:11px 0;border-bottom:1px solid var(--rule);
    align-items:baseline;flex-wrap:wrap}}
  ul.src a{{font-family:var(--mono);font-size:12.5px;letter-spacing:.03em;width:190px;flex:none}}
  ul.src span{{color:var(--muted);font-size:15px;flex:1;min-width:220px}}

  footer{{margin:76px 0 0;padding:24px 0 66px;border-top:1px solid var(--rule);
    font-family:var(--mono);font-size:11px;letter-spacing:.06em;color:var(--muted)}}

  @media (max-width:720px){{
    body{{font-size:16px}}
    .wrap{{padding:0 20px}}
    .bands-in{{padding:0 20px}}
    header.hero{{padding:46px 0 0}}
    .entry{{flex-direction:column;gap:6px;padding:16px 16px}}
    .e-num{{padding-top:0}}
    .band-h{{gap:14px}}
    .band-l{{width:30px;font-size:22px}}
    .an{{flex-direction:column;gap:2px}}
    .an-n{{width:auto}}
    ul.src li{{flex-direction:column;gap:3px}}
    ul.src a{{width:auto}}
    .sig .stat{{gap:22px}}
  }}
  @media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}
  @media print{{
    nav.bands{{display:none}} body{{background:#fff}} .entry,.thread,.ptype{{background:#fff}}
  }}
</style>
</head>
<body>

<nav class="bands" aria-label="Periods">
  <div class="bands-in">
    {bandnav}
  </div>
</nav>

<div class="wrap">

<header class="hero">
  <p class="eyebrow">A reading plan · index</p>
  <h1>Denmark,<br>from the ice to the <em>welfare state</em></h1>
  <p class="range">c. 13,000 BCE — 1953 · {len(E)} chapters, {len(DENSE)} flagged for possible split · {len(THREADS)} threads · {len(MAPS)} maps · <b>{sum(len(v) for v in BUILT.values())} pages written</b></p>
  <p class="thesis">The history of the land we now call Denmark, set in its European and global
  frame at every step: the Roman economy, the Baltic crusades, the Hanse, the Atlantic slave
  trade, the Napoleonic wars, and the two world wars.</p>
  <p class="scope">Written in English, with Danish terms kept and glossed on first use. A layman's
  book, not a university syllabus. Chapters run <b>25–50 minutes</b> — a band, not a target: length
  follows the number of distinct stories a chapter has to carry, not the number of years it
  covers.</p>
</header>

<section class="sig" aria-labelledby="sig-h">
  <h2 id="sig-h">Where the detail goes</h2>
  <p class="cap">Top axis: the {len(E)} chapters placed by real elapsed time. Bottom axis: the same {len(E)}
  chapters given equal space on the page. The fan between them is the whole editorial argument —
  resolution widens as evidence does.</p>
  <svg viewBox="0 0 1000 172" role="img"
       aria-label="Diagram: {len(E)} chapters plotted by real time on the top axis fan out to equal spacing on the bottom axis, showing that the last 1,200 years occupy 8 percent of the timeline but {PCT_AFTER} percent of the chapters.">
      <text x="62" y="24" class="axlab">By elapsed time</text>
      <text x="946" y="24" class="axlab" text-anchor="end">1,200 yrs → {AFTER_750} chapters</text>
      <line x1="62" y1="51" x2="946" y2="51" stroke="#9A9C90" stroke-width="1"/>
      <line x1="62" y1="145" x2="946" y2="145" stroke="#9A9C90" stroke-width="1"/>
      {FAN}
  </svg>
  <div class="stat">
    <div><b>8%</b>of the timeline is after 750 CE</div>
    <div><b>{PCT_AFTER}%</b>of the chapters cover it</div>
    <div><b>3</b>chapters for the 11,300-year Stone Age</div>
    <div><b>6</b>chapters for 1901–1955</div>
  </div>
</section>

<section class="blk">
  <p class="kicker">The spine</p>
  <h2>Nine parts, {len(E)} chapters</h2>
  <p class="lede">Chronological, self-contained, and cross-linked. Boundaries follow standard Danish
  periodisation; where historians disagree about a boundary, that disagreement goes on the page
  itself rather than being smoothed over here.</p>
  {SPINE}
</section>

<section class="blk">
  <p class="kicker">The threads</p>
  <h2>Six questions that outlive any single era</h2>
  <p class="lede">Chronology alone hides the continuities. Each thread gets its own overview page,
  and each era page carries a short section on whichever threads it touches.</p>
  <ol class="threads">
{THR}
  </ol>
</section>

<section class="blk">
  <p class="kicker">The map spine</p>
  <h2>Eleven territorial maps, one projection</h2>
  <p class="lede">Same projection, same style, same legend, drawn as inline SVG. Flipped in
  sequence they are the argument of the whole project: expansion to 1397, then four centuries of
  contraction. Era chapters carry their own maps on top of these — trade routes, campaigns,
  site distributions.</p>
  <ol class="maps">
{MAPL}
  </ol>
</section>

<section class="blk">
  <p class="kicker">Page types</p>
  <h2>Four shapes, one library</h2>
  <p class="lede">Special interests slot in without disturbing the spine. A ship is not a place and
  neither is an era, so they get different treatments.</p>
  <ol class="ptypes">
{PT}
  </ol>
</section>

<section class="blk">
  <p class="kicker">Page anatomy</p>
  <h2>How every era page is built</h2>
  <p class="lede">Prime, tell, consolidate, retrieve. The introduction poses the questions the
  summary answers, so the loop closes.</p>
  <ol class="anat">
{AN}
  </ol>
</section>

<section class="blk">
  <p class="kicker">Conventions</p>
  <h2>Decisions already made</h2>
  <ul class="conv">
    <li><b>Language</b><span>English throughout. Danish terms kept where they carry meaning —
      <i>stavnsbånd</i>, <i>enevælde</i>, <i>retsopgøret</i> — and glossed on first use in each page.</span></li>
    <li><b>Baseline</b><span>Assumes Danish gymnasium history somewhere in the past. Key figures
      get a one-line reintroduction, not a full biography.</span></li>
    <li><b>Delivery</b><span>Self-contained HTML files. No CDN, no external fonts, no network at
      view time. Download once and they keep working.</span></li>
    <li><b>Length</b><span>25–50 minutes per chapter. Governed by how many separate stories a page
      must carry, not by how many years it spans. {NUMWORD[len(DENSE)]} chapters are flagged <i>dense</i> in the spine
      above; those are the ones likely to run to the top of the band or to split in two.</span></li>
    <li><b>Sourcing</b><span>Light — a source line per page, plus inline links where a claim is
      contested or surprising.</span></li>
    <li><b>Historiography</b><span>The Viking Age, the colonial period, 1864 and the cooperation
      policy have all been substantially rewritten since the schoolbooks. Pages follow current
      scholarship and say where it changed.</span></li>
  </ul>
</section>

<section class="blk">
  <p class="kicker">Sources</p>
  <h2>What this is built on</h2>
  <ul class="src">
{SRC}
  </ul>
</section>

<footer>
  Index v3 · {n} chapters on the spine, {len(BUILT)} of them written as {sum(len(v) for v in BUILT.values())} pages · {len(DENSE)} flagged dense ·
  {len(THREADS)} threads · {len(MAPS)} maps · the spine count is provisional and will move if a
  dense chapter splits
</footer>

</div>
</body>
</html>
'''

# Written next to the chapter pages by default, so that generating the index and
# discovering the chapters use the same folder unless deliberately separated.
# Override with DK_OUT. Hardcoding the container path here was the counterpart of
# the CHAPTER_DIR default, and failed the same way when run anywhere else.
OUT_DIR = os.environ.get("DK_OUT", CHAPTER_DIR)
_out = os.path.join(OUT_DIR, "danish-history-index.html")
open(_out, "w", encoding="utf-8").write(DOC)
print("wrote %s" % _out)
print("  %d chapters in the spine, %d built and linked" % (len(E), len(BUILT)))
print("  discovered in %s" % CHAPTER_DIR)
print("written", len(DOC), "chars")
