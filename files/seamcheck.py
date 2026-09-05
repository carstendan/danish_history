# -*- coding: utf-8 -*-
"""Seam layer for mapfixture: catches near-but-not-exactly-shared borders.

WHY THIS EXISTS
---------------
The coverage sweep sees an overlap only when a grid point lands inside it. GRID
is 0.2 deg. The Schleswig/Ditmarschen overlap is 0.045 deg thick and the
Denmark/Schleswig one is about 0.04 deg at any given longitude, so both are
invisible to the sweep - not because the grid is too coarse but because the
failure is a thin lens ALONG a border rather than a region, and no affordable
grid catches those reliably.

The test that needs no grid: where two neighbours share a border, neither may
have a vertex lying strictly inside the other. That is the property map_1397.py
already states in prose for Norway and Sweden - "copied exactly; do not tidy
them apart" - and it is checkable exactly.

TOLERANCE. Ray casting is undefined on the boundary itself, so a vertex that IS
the shared vertex reports as inside about half the time. Depth is therefore
measured perpendicular to the neighbour's boundary, and anything shallower than
TOL is treated as on the line. TOL = 0.002 deg, about 200 m: far below any real
seam and far above float noise. Without this the layer reports every one of
Norway and Sweden's correctly shared vertices, and a verifier that reports false
positives is worse than no verifier.
"""
import math

from mapfixture import inside

TOL = 0.002


def _seg_dist(p, a, b):
    px, py = p
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))


def depth(poly, lon, lat):
    """Perpendicular distance from the point to the polygon's boundary."""
    return min(_seg_dist((lon, lat), poly[i - 1], poly[i]) for i in range(len(poly)))


def intruding(a_name, a, b_name, b):
    out = []
    for lon, lat in a:
        if inside(b, lon, lat):
            d = depth(b, lon, lat)
            if d > TOL:
                out.append((a_name, b_name, lon, lat, d))
    return out


def check_seams(mod, regions):
    polys = {k: getattr(mod, k) for k in regions}
    out = []
    for i, a in enumerate(regions):
        for b in regions[i + 1:]:
            out += intruding(a, polys[a], b, polys[b])
            out += intruding(b, polys[b], a, polys[a])
    return out


SETS = {
    1397: ["DENMARK", "BORNHOLM", "SLESVIG", "NORWAY", "SWEDEN", "GOTLAND"],
    1500: ["DENMARK", "BORNHOLM", "SLESVIG", "HOLSTEN", "DITMARSKEN", "NORWAY",
           "SWEDEN", "GOTLAND"],
    1600: ["DENMARK", "BORNHOLM", "SLESVIG", "HOLSTEN", "DITMARSKEN", "NORWAY",
           "GOTLAND", "OESEL"],
    1660: ["DENMARK", "BORNHOLM", "SLESVIG", "HOLSTEN", "DITMARSKEN", "NORWAY",
           "SCANIA", "NO_LOST", "GOTLAND", "OESEL"],
    1721: ["DENMARK", "BORNHOLM", "SLESVIG", "HOLSTEN", "DITMARSKEN", "NORWAY"],
    # 1814 inherits every polygon unchanged from 1660 by way of 1721, so the seams
    # cannot have drifted - but that is the reason to test them, not to skip them.
    # Lauenburg is absent because map_1814 marks it rather than drawing it and it
    # therefore has no border to share.
    1814: ["DENMARK", "BORNHOLM", "SLESVIG", "HOLSTEN", "DITMARSKEN", "NORWAY"],
}


def main():
    import map_1397 as m97, map_1500 as m00, map_1600 as m16, map_1660 as m66, map_1721 as m21
    import map_1814 as m14
    fail = 0
    for year, mod in ((1397, m97), (1500, m00), (1600, m16), (1660, m66), (1721, m21),
                      (1814, m14)):
        bad = check_seams(mod, SETS[year])
        print("MAP %d   %s" % (year, "every shared border is shared exactly"
                               if not bad else "FAIL, %d vertices inside a neighbour" % len(bad)))
        for a, b, lon, lat, d in sorted(bad, key=lambda r: -r[4]):
            print("    %-11s vertex %7.3f,%6.3f is %5.3f deg (~%4.1f km) inside %s"
                  % (a, lon, lat, d, d * 111, b))
        fail += len(bad)
    print("=" * 62)
    print("SEAM LAYER PASSES" if not fail else "!! SEAM LAYER FAILS (%d)" % fail)
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
