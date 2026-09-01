# -*- coding: utf-8 -*-
"""The standing fixture for the eleven territorial maps.

Written after the 1397 map shipped with south-west Norway unfilled. Thirty-six
point-in-polygon cases passed it, because none of them was in Rogaland. More
hand-written cases would not have helped; differently *placed* ones would. So
there are three layers here, and only the first is hand-written:

  1. CURATED   named places with their allegiance in a given map year. This is
               the layer that encodes historical judgement, and it is the one
               worth arguing about.
  2. COVERAGE  a grid swept over the frame. Every point that is on land and
               inside the year's envelope must belong to exactly one territory.
               Land belonging to nobody is the Rogaland failure; land belonging
               to two is the Ditmarschen-inside-Holstein failure. Neither is a
               case anybody has to remember to write.
  3. ASSERTED  every territory must carry at least MIN_CASES curated cases, so
               adding a polygon without testing it fails the build.
  4. SEAMS     where two neighbours share a border, neither may have a vertex
               strictly inside the other. Added August 2026 after three maps
               shipped with overlapping fills that printed as dark stripes: the
               Kongeaa lens was 27 km at its widest and the sweep never saw it,
               because a thin band ALONG a border is invisible to any affordable
               grid. See seamcheck.py.

Run it before every map ships:  python3 mapfixture.py
"""
import sys

from mapkit import load_land, simplify

MIN_CASES = 3
GRID = 0.20                      # degrees; ~13,000 sample points on the spine frame


# ---------------------------------------------------------------- geometry
def inside(poly, lon, lat):
    n, j, r = len(poly), len(poly) - 1, False
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if (yi > lat) != (yj > lat) and lon < (xj - xi) * (lat - yi) / (yj - yi) + xi:
            r = not r
        j = i
    return r


_LAND = None


def land_rings():
    global _LAND
    if _LAND is None:
        _LAND = [simplify(p, 0.05) for p in load_land("package/land-50m.json")]
    return _LAND


def on_land(lon, lat):
    return sum(inside(r, lon, lat) for r in land_rings()) % 2 == 1


# ---------------------------------------------------------------- envelopes
# A generous outline of what the map is *about*. Land inside it must be assigned
# to some territory; land outside it (Germany, Poland, the Baltic states, Russia,
# Scotland, the Netherlands) is deliberately uncoloured and not this map's
# business. The envelope is the only judgement in the coverage layer.
SCANDINAVIA = [
    (2.0, 57.0), (7.6, 54.9), (8.0, 54.3), (11.2, 54.45), (12.6, 54.75), (14.4, 54.85),
    (16.5, 55.9), (19.0, 58.5), (21.5, 59.2), (25.0, 59.6), (31.5, 61.0), (31.5, 71.6),
    (10.0, 71.6), (2.0, 66.0),
]
# 1500 adds the duchies, so the envelope has to reach the Elbe.
SCANDINAVIA_AND_DUCHIES = [
    (2.0, 57.0), (7.6, 54.9), (8.7, 53.98), (9.4, 53.80), (10.0, 53.62), (10.6, 53.82), (11.2, 54.45),
    (12.6, 54.75), (14.4, 54.85), (16.5, 55.9), (19.0, 58.5), (21.5, 59.2), (25.0, 59.6),
    (31.5, 61.0), (31.5, 71.6), (10.0, 71.6), (2.0, 66.0),
]

# 1600: Sweden is a separate kingdom and is not coloured, so it is no longer this
# map's business - as much outside the envelope as Poland or Scotland. The eastern
# edge therefore follows the Denmark-Sweden and Norway-Sweden borders, taken from
# the same vertex lists the map draws, and pulled 0.25 degrees INTO Danish and
# Norwegian territory so that a grid point cannot land ambiguously on the line
# itself. A thin untested strip along the border is a cheap price for that.
DENMARK_NORWAY_AND_DUCHIES = [
    (2.0, 57.0), (7.6, 54.9), (8.7, 53.98), (9.4, 53.80), (10.0, 53.62), (10.6, 53.82),
    (11.2, 54.45), (12.6, 54.75), (14.4, 54.85), (16.2, 55.9),
    # up the Denmark-Sweden border, offset west
    (15.70, 56.05), (15.15, 56.45), (13.95, 56.55), (12.95, 56.60), (12.85, 57.10),
    (12.65, 57.45), (12.15, 57.55),
    # up the Norway-Sweden border, offset west
    (11.70, 57.75), (11.80, 58.05), (11.70, 58.60), (11.40, 59.00), (11.80, 59.60),
    (12.30, 60.30), (12.10, 61.00), (12.20, 61.60), (12.80, 61.90), (14.20, 62.20),
    (14.40, 62.90), (15.20, 63.60), (14.10, 64.40), (14.30, 65.00), (15.30, 66.00),
    (16.10, 67.00), (17.90, 68.10), (20.00, 68.60),
    (21.90, 69.30), (25.00, 68.80), (26.00, 69.90), (28.00, 69.80), (30.50, 69.70),
    (31.00, 70.30), (31.00, 71.50), (3.00, 71.50), (2.0, 66.0),
]

# 1721: the ceded provinces are no longer drawn, so the envelope's eastern edge
# comes back to the border of 1660 rather than the border of 1397. Both edges are
# offset INTO Danish and Norwegian ground by about a quarter-degree, the same way
# DENMARK_NORWAY_AND_DUCHIES is, so that no point of the border itself is tested.
# The Sound stretch needs no offset worth speaking of because it is water.
DENMARK_NORWAY_1721 = [
    (2.0, 57.0), (7.6, 54.9), (8.7, 53.98), (9.4, 53.80), (10.0, 53.62), (10.6, 53.82),
    (11.2, 54.45), (12.60, 54.75),
    # up the Sound and the Kattegat, west of the 1660 line
    (12.70, 55.20), (12.70, 55.55), (12.55, 55.85), (12.45, 56.05), (12.15, 56.25),
    (11.90, 57.20),
    # up the Norway-Sweden border of 1660, offset west
    (11.55, 57.75), (11.05, 59.25), (11.55, 59.60), (11.80, 59.60), (12.30, 60.30),
    (12.10, 61.00), (12.20, 61.60), (11.90, 61.90), (11.80, 62.60), (11.90, 63.40),
    (13.35, 64.10), (14.30, 65.00), (15.30, 66.00),
    (16.10, 67.00), (17.90, 68.10), (20.00, 68.60),
    (21.90, 69.30), (25.00, 68.80), (26.00, 69.90), (28.00, 69.80), (30.50, 69.70),
    (31.00, 70.30), (31.00, 71.50), (3.00, 71.50), (2.0, 66.0),
]

# Land inside the envelope that is genuinely nobody's on a given map. Each entry
# is a reason, not just an exemption: if you add one, say why in the string.
KNOWN_UNCLAIMED = {
    1397: [((10.4, 53.4, 11.0, 54.3), "Lübeck and its territory, a free imperial city"),
           ((27.5, 59.5, 31.5, 68.5), "Karelia and the White Sea lands east of the border"),
           ((8.0, 53.9, 10.9, 55.3), "Schleswig is DEP, Holstein is not on this map at all"),
           ((24.0, 68.0, 31.5, 71.6), "no fixed border in the far north; the map says so")],
    1500: [((10.55, 53.4, 11.2, 54.3), "Lübeck, a free imperial city, capped out of Holstein"),
           ((27.5, 59.5, 31.5, 68.5), "Karelia and the White Sea lands east of the border"),
           ((24.0, 68.0, 31.5, 71.6), "no fixed border in the far north")],
    1600: [((10.55, 53.4, 11.2, 54.3), "Lübeck, a free imperial city, capped out of Holstein"),
           ((27.5, 59.5, 31.5, 68.5), "Karelia and the White Sea lands east of the border"),
           ((24.0, 68.0, 31.5, 71.6), "no fixed border in the far north")],
    1721: [((10.55, 53.4, 11.2, 54.3), "Lübeck, a free imperial city, capped out of Holstein"),
           ((27.5, 59.5, 31.5, 68.5), "Karelia and the White Sea lands east of the border"),
           ((24.0, 68.0, 31.5, 71.6), "no fixed border in the far north")],
    1660: [((10.55, 53.4, 11.2, 54.3), "Lübeck, a free imperial city, capped out of Holstein"),
           ((27.5, 59.5, 31.5, 68.5), "Karelia and the White Sea lands east of the border"),
           ((24.0, 68.0, 31.5, 71.6), "no fixed border in the far north")],
}


def in_boxes(boxes, lon, lat):
    return any(a <= lon <= c and b <= lat <= d for (a, b, c, d), _ in boxes)


# ---------------------------------------------------------------- curated layer
# (place, lon, lat, region key or None for "in none of them")
CURATED = {
 1397: [
    ("Ribe", 8.76, 55.33, "DENMARK"), ("Kolding", 9.47, 55.49, "DENMARK"),
    ("Viborg", 9.40, 56.45, "DENMARK"), ("København", 12.57, 55.68, "DENMARK"),
    ("Odense", 10.39, 55.40, "DENMARK"), ("Lund", 13.19, 55.70, "DENMARK"),
    ("Falsterbo", 12.85, 55.38, "DENMARK"), ("Halmstad", 12.86, 56.67, "DENMARK"),
    ("Blekinge", 15.20, 56.20, "DENMARK"), ("Skagen", 10.60, 57.74, "DENMARK"),
    ("R\u00f8nne, Bornholm", 14.70, 55.10, "BORNHOLM"),
    ("Hasle, Bornholm", 14.71, 55.19, "BORNHOLM"),
    ("Nex\u00f8, Bornholm", 15.13, 55.06, "BORNHOLM"),
    ("Haderslev", 9.49, 55.25, "SLESVIG"), ("Flensborg", 9.44, 54.78, "SLESVIG"),
    ("Slesvig by", 9.56, 54.52, "SLESVIG"), ("Husum", 9.05, 54.48, "SLESVIG"),
    ("Kiel", 10.13, 54.32, None), ("Rendsburg", 9.66, 54.29, None),
    ("Hamburg", 10.00, 53.55, None), ("Lübeck", 10.69, 53.87, None),
    ("Oslo", 10.75, 59.91, "NORWAY"), ("Bergen", 5.32, 60.39, "NORWAY"),
    ("Trondheim", 10.40, 63.43, "NORWAY"), ("Stavanger", 5.73, 58.97, "NORWAY"),
    ("Lindesnes", 7.05, 57.98, "NORWAY"), ("Egersund", 6.00, 58.45, "NORWAY"),
    ("Kristiansand", 8.00, 58.15, "NORWAY"), ("Bohuslän", 11.60, 58.30, "NORWAY"),
    ("Uddevalla", 11.94, 58.35, "NORWAY"), ("Jämtland", 14.20, 63.20, "NORWAY"),
    ("Härjedalen", 13.50, 62.30, "NORWAY"), ("Tromsø", 18.95, 69.65, "NORWAY"),
    ("Sveg, Härjedalen", 14.36, 62.04, "NORWAY"),
    ("Lillhärdal, Härjedalen", 14.08, 61.85, "NORWAY"),
    ("Göteborg", 12.00, 57.75, "SWEDEN"), ("Stockholm", 18.07, 59.33, "SWEDEN"),
    ("Kalmar", 16.36, 56.66, "SWEDEN"), ("Uppsala", 17.64, 59.86, "SWEDEN"),
    ("Öland", 16.50, 56.70, "SWEDEN"), ("Vadstena", 14.89, 58.45, "SWEDEN"),
    ("Ångermanland", 17.50, 63.50, "SWEDEN"), ("Åbo", 22.27, 60.45, "SWEDEN"),
    ("Vyborg", 28.73, 60.71, "SWEDEN"), ("Umeå", 20.30, 63.80, "SWEDEN"),
    ("Reval", 24.75, 59.44, None), ("Riga", 24.11, 56.95, None),
    ("Gotland", 18.30, 57.63, "GOTLAND"), ("Fårö", 19.05, 57.90, "GOTLAND"),
    ("Visby", 18.29, 57.64, "GOTLAND"),
 ],
 1500: [
    ("Ribe", 8.76, 55.33, "DENMARK"), ("Viborg", 9.40, 56.45, "DENMARK"),
    ("København", 12.57, 55.68, "DENMARK"), ("Halland", 12.86, 56.67, "DENMARK"),
    ("Lund", 13.19, 55.70, "DENMARK"), ("Skagen", 10.60, 57.74, "DENMARK"),
    ("R\u00f8nne, Bornholm", 14.70, 55.10, "BORNHOLM"),
    ("Hasle, Bornholm", 14.71, 55.19, "BORNHOLM"),
    ("Nex\u00f8, Bornholm", 15.13, 55.06, "BORNHOLM"),
    ("Haderslev", 9.49, 55.25, "SLESVIG"), ("Flensborg", 9.44, 54.78, "SLESVIG"),
    ("Husum", 9.05, 54.48, "SLESVIG"), ("Slesvig by", 9.56, 54.52, "SLESVIG"),
    ("Kiel", 10.13, 54.32, "HOLSTEN"), ("Rendsburg", 9.66, 54.29, "HOLSTEN"),
    ("Itzehoe", 9.51, 53.92, "HOLSTEN"), ("Segeberg", 10.31, 53.94, "HOLSTEN"),
    ("Meldorf", 9.07, 54.09, "DITMARSKEN"), ("Heide", 9.10, 54.20, "DITMARSKEN"),
    ("Hemmingstedt", 9.07, 54.14, "DITMARSKEN"), ("Brunsbüttel", 9.14, 53.90, "DITMARSKEN"),
    ("Lübeck", 10.69, 53.87, None), ("Hamburg", 10.00, 53.55, None),
    ("Oslo", 10.75, 59.91, "NORWAY"), ("Bergen", 5.32, 60.39, "NORWAY"),
    ("Stavanger", 5.73, 58.97, "NORWAY"), ("Bohuslän", 11.60, 58.30, "NORWAY"),
    ("Jämtland", 14.20, 63.20, "NORWAY"), ("Trondheim", 10.40, 63.43, "NORWAY"),
    ("Sveg, Härjedalen", 14.36, 62.04, "NORWAY"),
    ("Lillhärdal, Härjedalen", 14.08, 61.85, "NORWAY"),
    ("Stockholm", 18.07, 59.33, "SWEDEN"), ("Kalmar", 16.36, 56.66, "SWEDEN"),
    ("Göteborg", 12.00, 57.75, "SWEDEN"), ("Åbo", 22.27, 60.45, "SWEDEN"),
    ("Gotland", 18.30, 57.63, "GOTLAND"), ("Visby", 18.29, 57.64, "GOTLAND"),
    ("Fårö", 19.05, 57.90, "GOTLAND"),
 ],
 1721: [
    ("Ribe", 8.76, 55.33, "DENMARK"), ("Aarhus", 10.20, 56.16, "DENMARK"),
    ("Odense", 10.39, 55.40, "DENMARK"), ("Aalborg", 9.92, 57.05, "DENMARK"),
    ("K\u00f8benhavn", 12.57, 55.68, "DENMARK"), ("Helsing\u00f8r", 12.615, 56.035, "DENMARK"),
    ("R\u00f8nne, Bornholm", 14.70, 55.10, "BORNHOLM"),
    ("Hasle, Bornholm", 14.71, 55.19, "BORNHOLM"),
    ("Svaneke, Bornholm", 15.14, 55.14, "BORNHOLM"),
    ("Oslo", 10.75, 59.91, "NORWAY"), ("Trondhjem", 10.40, 63.43, "NORWAY"),
    ("Bergen", 5.32, 60.39, "NORWAY"), ("Troms\u00f8", 18.96, 69.65, "NORWAY"),
    ("R\u00f8ros", 11.38, 62.57, "NORWAY"),
    # the whole of Slesvig is the king's from 1721; Holsten is still shared
    ("Haderslev", 9.49, 55.25, "SLESVIG"), ("Flensburg", 9.44, 54.78, "SLESVIG"),
    ("T\u00f8nder", 8.87, 54.94, "SLESVIG"), ("Slesvig by", 9.57, 54.52, "SLESVIG"),
    ("Kiel", 10.14, 54.32, "HOLSTEN"), ("Rendsburg", 9.66, 54.30, "HOLSTEN"),
    ("Itzehoe", 9.52, 53.92, "HOLSTEN"),
    ("Meldorf", 9.07, 54.09, "DITMARSKEN"), ("Heide", 9.10, 54.20, "DITMARSKEN"),
    ("Brunsb\u00fcttel", 9.14, 53.90, "DITMARSKEN"),
    # renounced in 1720 and no longer coloured on this map
    ("Malm\u00f6", 13.00, 55.60, None), ("Helsingborg", 12.694, 56.046, None),
    ("Halmstad", 12.86, 56.67, None), ("Uddevalla", 11.94, 58.35, None),
    ("\u00d6stersund", 14.64, 63.18, None), ("Visby", 18.29, 57.64, None),
    ("Stockholm", 18.07, 59.33, None), ("Kalmar", 16.36, 56.66, None)],
 1660: [
    # the kingdom, after the Scanian provinces are gone
    ("Ribe", 8.76, 55.33, "DENMARK"), ("Aarhus", 10.20, 56.16, "DENMARK"),
    ("Odense", 10.39, 55.40, "DENMARK"), ("Aalborg", 9.92, 57.05, "DENMARK"),
    ("K\u00f8benhavn", 12.57, 55.68, "DENMARK"), ("Skagen", 10.59, 57.72, "DENMARK"),
    # Helsing\u00f8r keeps the toll; Helsingborg, 6 km away, does not. The tightest
    # pair on any map in the series - 0.08 deg apart across the Sound.
    ("Helsing\u00f8r", 12.615, 56.035, "DENMARK"),
    ("Helsingborg", 12.694, 56.046, "SCANIA"),
    ("R\u00f8nne, Bornholm", 14.70, 55.10, "BORNHOLM"),
    # ceded 1645-1658
    ("Malm\u00f6", 13.00, 55.60, "SCANIA"), ("Lund", 13.19, 55.70, "SCANIA"),
    ("Landskrona", 12.83, 55.87, "SCANIA"), ("Kristianstad", 14.16, 56.03, "SCANIA"),
    ("Kullen", 12.45, 56.30, "SCANIA"), ("Halmstad", 12.86, 56.67, "SCANIA"),
    ("Karlskrona, Blekinge", 15.59, 56.16, "SCANIA"),
    ("Uddevalla, Bohusl\u00e4n", 11.94, 58.35, "NO_LOST"),
    ("\u00d6stersund, J\u00e4mtland", 14.64, 63.18, "NO_LOST"),
    # Sveg: the case that map_1397 never had. H\u00e4rjedalen is Norwegian until 1645,
    # and on 1397, 1500 and 1600 this point falls inside SWEDEN. Lesson 12.
    ("Sveg, H\u00e4rjedalen", 14.36, 62.04, "NO_LOST"),
    ("Fun\u00e4sdalen", 12.55, 62.54, "NO_LOST"),
    ("Visby, Gotland", 18.29, 57.64, "GOTLAND"),
    ("Kuressaare, \u00d8sel", 22.48, 58.25, "OESEL"),
    # Norway, with Trondhjem restored in 1660
    ("Oslo", 10.75, 59.91, "NORWAY"), ("Trondhjem", 10.40, 63.43, "NORWAY"),
    ("Bergen", 5.32, 60.39, "NORWAY"), ("Troms\u00f8", 18.96, 69.65, "NORWAY"),
    ("Kristiansand", 8.00, 58.15, "NORWAY"), ("R\u00f8ros", 11.38, 62.57, "NORWAY"),
    # the duchies
    ("Haderslev", 9.49, 55.25, "SLESVIG"), ("Flensburg", 9.44, 54.78, "SLESVIG"),
    ("Kiel", 10.14, 54.32, "HOLSTEN"), ("Rendsburg", 9.66, 54.30, "HOLSTEN"),
    ("Itzehoe", 9.52, 53.92, "HOLSTEN"),
    ("Meldorf", 9.07, 54.09, "DITMARSKEN"), ("Heide", 9.10, 54.20, "DITMARSKEN"),
    ("Brunsb\u00fcttel", 9.14, 53.90, "DITMARSKEN"),
    ("T\u00f8nder", 8.87, 54.94, "SLESVIG"), ("Slesvig by", 9.57, 54.52, "SLESVIG"),
    ("Hasle, Bornholm", 14.71, 55.19, "BORNHOLM"),
    ("Svaneke, Bornholm", 15.14, 55.14, "BORNHOLM"),
    ("Visby N, Gotland", 18.60, 57.90, "GOTLAND"),
    ("Gotland S", 18.30, 57.10, "GOTLAND"),
    ("Muhu, \u00d8sel", 22.90, 58.55, "OESEL"), ("\u00d8sel W", 22.00, 58.30, "OESEL"),
    # Sweden proper is not coloured on this map
    ("Stockholm", 18.07, 59.33, None), ("Kalmar", 16.36, 56.66, None),
    ("Jokkmokk", 19.83, 66.61, None), ("Mora", 14.54, 61.00, None),
    ("V\u00e4nersborg", 12.32, 58.38, None)],
 1600: [
    ("Ribe", 8.76, 55.33, "DENMARK"), ("Viborg", 9.40, 56.45, "DENMARK"),
    ("København", 12.57, 55.68, "DENMARK"), ("Helsingør", 12.62, 56.04, "DENMARK"),
    ("Hven", 12.70, 55.90, "DENMARK"), ("Halmstad", 12.86, 56.67, "DENMARK"),
    ("Lund", 13.19, 55.70, "DENMARK"), ("Blekinge", 15.20, 56.20, "DENMARK"),
    ("Skagen", 10.60, 57.74, "DENMARK"),
    ("R\u00f8nne, Bornholm", 14.70, 55.10, "BORNHOLM"),
    ("Hasle, Bornholm", 14.71, 55.19, "BORNHOLM"),
    ("Nex\u00f8, Bornholm", 15.13, 55.06, "BORNHOLM"),
    ("Haderslev", 9.49, 55.25, "SLESVIG"), ("Flensborg", 9.44, 54.78, "SLESVIG"),
    ("Gottorp", 9.56, 54.52, "SLESVIG"), ("Husum", 9.05, 54.48, "SLESVIG"),
    ("Kiel", 10.13, 54.32, "HOLSTEN"), ("Rendsburg", 9.66, 54.29, "HOLSTEN"),
    ("Itzehoe", 9.51, 53.92, "HOLSTEN"), ("Segeberg", 10.31, 53.94, "HOLSTEN"),
    # conquered 1559: what was CLAIM on the 1500 map is held here
    ("Meldorf", 9.07, 54.09, "DITMARSKEN"), ("Heide", 9.10, 54.20, "DITMARSKEN"),
    ("Hemmingstedt", 9.07, 54.14, "DITMARSKEN"), ("Brunsbüttel", 9.14, 53.90, "DITMARSKEN"),
    ("Lübeck", 10.69, 53.87, None), ("Hamburg", 10.00, 53.55, None),
    ("Oslo", 10.75, 59.91, "NORWAY"), ("Bergen", 5.32, 60.39, "NORWAY"),
    ("Stavanger", 5.73, 58.97, "NORWAY"), ("Bohuslän", 11.60, 58.30, "NORWAY"),
    ("Jämtland", 14.20, 63.20, "NORWAY"), ("Trondheim", 10.40, 63.43, "NORWAY"),
    ("Sveg, Härjedalen", 14.36, 62.04, "NORWAY"),
    ("Lillhärdal, Härjedalen", 14.08, 61.85, "NORWAY"),
    ("Gotland", 18.30, 57.63, "GOTLAND"), ("Visby", 18.29, 57.64, "GOTLAND"),
    ("Fårö", 19.05, 57.90, "GOTLAND"),
    ("Kuressaare, Ösel", 22.49, 58.25, "OESEL"), ("Ösel north", 22.40, 58.50, "OESEL"),
    ("Ösel west", 22.05, 58.30, "OESEL"),
    # Sweden is a separate kingdom and holds nothing on this map
    ("Stockholm", 18.07, 59.33, None), ("Kalmar", 16.36, 56.66, None),
    ("Göteborg", 12.00, 57.75, None), ("Åbo", 22.27, 60.45, None),
    ("Reval", 24.75, 59.44, None),
 ],
}

# The western panel is a separate frame and gets its own cases.
PANEL = {
 1397: [("Qaqortoq", -46.03, 60.72, "GREENLAND"), ("Nuuk", -51.72, 64.18, "GREENLAND"),
        ("NE Greenland", -22.00, 67.40, "GREENLAND"),
        ("Reykjavík", -21.94, 64.15, "ICELAND"), ("Akureyri", -18.09, 65.68, "ICELAND"),
        ("Látrabjarg", -24.54, 65.50, "ICELAND"),
        ("Tórshavn", -6.77, 62.01, "FAROES"),
        ("Lerwick", -1.15, 60.15, "SHETLAND"), ("Kirkwall", -2.96, 58.98, "ORKNEY"),
        ("Dunnet Head", -3.37, 58.67, None), ("Thurso", -3.52, 58.59, None),
        ("Bergen", 5.32, 60.39, None)],
 1500: [("Qaqortoq", -46.03, 60.72, "GREENLAND"), ("Nuuk", -51.72, 64.18, "GREENLAND"),
        ("NE Greenland", -22.00, 67.40, "GREENLAND"),
        ("Reykjavík", -21.94, 64.15, "ICELAND"), ("Akureyri", -18.09, 65.68, "ICELAND"),
        ("Látrabjarg", -24.54, 65.50, "ICELAND"),
        ("Tórshavn", -6.77, 62.01, "FAROES"),
        # gone in 1468-69, so they must belong to nothing on this map
        ("Lerwick", -1.15, 60.15, None), ("Kirkwall", -2.96, 58.98, None),
        ("Dunnet Head", -3.37, 58.67, None)],
 1721: [("Qaqortoq", -46.03, 60.72, "GREENLAND"), ("Nuuk", -51.72, 64.18, "GREENLAND"),
    ("Reykjav\u00edk", -21.94, 64.15, "ICELAND"), ("T\u00f3rshavn", -6.77, 62.01, "FAROES"),
    ("Lerwick", -1.15, 60.15, None), ("Kirkwall", -2.96, 58.98, None)],
 1660: [("Qaqortoq", -46.03, 60.72, "GREENLAND"), ("Nuuk", -51.72, 64.18, "GREENLAND"),
    ("Reykjav\u00edk", -21.94, 64.15, "ICELAND"), ("T\u00f3rshavn", -6.77, 62.01, "FAROES"),
    ("Lerwick", -1.15, 60.15, None), ("Kirkwall", -2.96, 58.98, None)],
 1600: [("Qaqortoq", -46.03, 60.72, "GREENLAND"), ("Nuuk", -51.72, 64.18, "GREENLAND"),
        ("NE Greenland", -22.00, 67.40, "GREENLAND"),
        ("Reykjavík", -21.94, 64.15, "ICELAND"), ("Akureyri", -18.09, 65.68, "ICELAND"),
        ("Látrabjarg", -24.54, 65.50, "ICELAND"),
        ("Tórshavn", -6.77, 62.01, "FAROES"),
        ("Lerwick", -1.15, 60.15, None), ("Kirkwall", -2.96, 58.98, None),
        ("Dunnet Head", -3.37, 58.67, None)],
}


# ---------------------------------------------------------------- the maps
def maps():
    import map_1397 as m97
    import map_1500 as m00
    import map_1600 as m16
    import map_1660 as m66
    import map_1721 as m21
    return [
        dict(year=1397, mod=m97, envelope=SCANDINAVIA, bbox=(3.0, 53.0, 31.0, 71.5),
             regions=["DENMARK", "BORNHOLM", "SLESVIG", "NORWAY", "SWEDEN", "GOTLAND"],
             panel=["GREENLAND", "ICELAND", "FAROES", "SHETLAND", "ORKNEY"]),
        dict(year=1500, mod=m00, envelope=SCANDINAVIA_AND_DUCHIES, bbox=(3.0, 53.0, 31.0, 71.5),
             regions=["DENMARK", "BORNHOLM", "SLESVIG", "HOLSTEN", "DITMARSKEN", "NORWAY",
                      "SWEDEN", "GOTLAND"],
             panel=["GREENLAND", "ICELAND", "FAROES"]),
        dict(year=1600, mod=m16, envelope=DENMARK_NORWAY_AND_DUCHIES,
             bbox=(3.0, 53.0, 31.0, 71.5),
             regions=["DENMARK", "BORNHOLM", "SLESVIG", "HOLSTEN", "DITMARSKEN", "NORWAY",
                      "GOTLAND", "OESEL"],
             panel=["GREENLAND", "ICELAND", "FAROES"]),
        # 1660: the ceded provinces are drawn, so they are territories the coverage
        # layer must assign. Sweden proper stays outside the envelope, exactly as on
        # 1600 - the envelope's eastern edge is the old border offset west, which is
        # also the ceded provinces' eastern edge, so nothing falls in the gap.
        dict(year=1660, mod=m66, envelope=DENMARK_NORWAY_AND_DUCHIES,
             bbox=(3.0, 53.0, 31.0, 71.5),
             regions=["DENMARK", "BORNHOLM", "SLESVIG", "HOLSTEN", "DITMARSKEN", "NORWAY",
                      "SCANIA", "NO_LOST", "GOTLAND", "OESEL"],
             panel=["GREENLAND", "ICELAND", "FAROES"]),
        # 1721: the ceded provinces are no longer drawn, so the envelope narrows back
        # to the 1600 shape - Sweden is simply not this map's business any more.
        dict(year=1721, mod=m21, envelope=DENMARK_NORWAY_1721,
             bbox=(3.0, 53.0, 31.0, 71.5),
             regions=["DENMARK", "BORNHOLM", "SLESVIG", "HOLSTEN", "DITMARSKEN", "NORWAY"],
             panel=["GREENLAND", "ICELAND", "FAROES"]),
    ]


def check_curated(cfg, cases, keys):
    polys = {k: getattr(cfg['mod'], k) for k in keys}
    bad = []
    for name, lon, lat, want in cases:
        hits = [k for k, p in polys.items() if inside(p, lon, lat)]
        ok = (hits == [want]) if want else (hits == [])
        if not ok:
            bad.append((name, want or "nothing", hits or ["nothing"]))
    return len(cases), bad


def check_coverage(cfg):
    polys = {k: getattr(cfg['mod'], k) for k in cfg['regions']}
    lo0, la0, lo1, la1 = cfg['bbox']
    known = KNOWN_UNCLAIMED.get(cfg['year'], [])
    unclaimed, overlapping, tested = [], [], 0
    lat = la0
    while lat <= la1:
        lon = lo0
        while lon <= lo1:
            if inside(cfg['envelope'], lon, lat) and on_land(lon, lat):
                tested += 1
                hits = [k for k, p in polys.items() if inside(p, lon, lat)]
                if len(hits) == 0 and not in_boxes(known, lon, lat):
                    unclaimed.append((round(lon, 2), round(lat, 2)))
                elif len(hits) > 1:
                    overlapping.append((round(lon, 2), round(lat, 2), hits))
            lon += GRID
        lat += GRID
    return tested, unclaimed, overlapping


def main():
    fail = 0
    for cfg in maps():
        y = cfg['year']
        print("=" * 70)
        print("MAP %d" % y)

        n, bad = check_curated(cfg, CURATED[y], cfg['regions'])
        print("  curated, mainland   %3d cases   %s" % (n, "all correct" if not bad else "FAIL"))
        for name, want, hits in bad:
            print("      %-16s expected %-12s got %s" % (name, want, hits))
        fail += len(bad)

        pn, pbad = check_curated(cfg, PANEL[y], cfg['panel'])
        print("  curated, panel      %3d cases   %s" % (pn, "all correct" if not pbad else "FAIL"))
        for name, want, hits in pbad:
            print("      %-16s expected %-12s got %s" % (name, want, hits))
        fail += len(pbad)

        counts = {k: 0 for k in cfg['regions']}
        for _, _, _, want in CURATED[y]:
            if want:
                counts[want] = counts.get(want, 0) + 1
        thin = [k for k, v in counts.items() if v < MIN_CASES]
        print("  coverage assertion              %s"
              % ("every territory has >= %d cases" % MIN_CASES if not thin
                 else "FAIL, too few cases: %s" % thin))
        fail += len(thin)

        from seamcheck import check_seams, SETS as SEAM_SETS
        seams = check_seams(cfg['mod'], SEAM_SETS[y])
        print("  seam layer                      %s"
              % ("every shared border is shared exactly" if not seams
                 else "FAIL, %d vertices inside a neighbour" % len(seams)))
        for a, b, lon, lat, d in sorted(seams, key=lambda r: -r[4]):
            print("      %-11s %7.3f,%6.3f is %5.3f deg (~%.1f km) inside %s"
                  % (a, lon, lat, d, d * 111, b))
        fail += len(seams)

        tested, unclaimed, overlapping = check_coverage(cfg)
        print("  generated sweep    %4d land points inside the envelope" % tested)
        if unclaimed:
            print("      FAIL  %d land points belong to no territory, e.g. %s"
                  % (len(unclaimed), unclaimed[:6]))
        else:
            print("      no unclaimed land")
        if overlapping:
            print("      FAIL  %d land points belong to two territories, e.g. %s"
                  % (len(overlapping), overlapping[:4]))
        else:
            print("      no overlapping territory")
        fail += bool(unclaimed) + bool(overlapping)

    print("=" * 70)
    print("FIXTURE PASSES" if not fail else "!! FIXTURE FAILS (%d problems)" % fail)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
