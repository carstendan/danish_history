# -*- coding: utf-8 -*-
"""Reusable base-map toolkit for the Danish history series.

Natural Earth land polygons (via the world-atlas npm package) -> Lambert conformal
conic projection -> clipped SVG path data. Same projection settings across every
map in the series so the 11 territorial maps stack correctly.
"""
import json, math

# ---------------------------------------------------------------- topojson

def load_land(path):
    d = json.load(open(path))
    sx, sy = d["transform"]["scale"]
    tx, ty = d["transform"]["translate"]
    arcs = []
    for arc in d["arcs"]:
        x = y = 0
        pts = []
        for dx, dy in arc:
            x += dx; y += dy
            pts.append((x * sx + tx, y * sy + ty))
        arcs.append(pts)
    obj = d["objects"]["land"]
    polys = []
    geoms = obj["geometries"] if obj["type"] == "GeometryCollection" else [obj]
    for g in geoms:
        if g["type"] == "Polygon":
            rings = [g["arcs"]]
        elif g["type"] == "MultiPolygon":
            rings = g["arcs"]
        else:
            continue
        for poly in rings:
            for ring in poly:
                pts = []
                for i in ring:
                    a = arcs[~i][::-1] if i < 0 else arcs[i]
                    pts.extend(a if not pts else a[1:])
                polys.append(pts)
    return polys


# ---------------------------------------------------------------- projection

class LCC:
    """Lambert conformal conic. Good for 50-65N; keeps Denmark's shape honest."""
    def __init__(self, lon0=10.0, lat0=56.0, lat1=52.0, lat2=62.0):
        r = math.radians
        self.lon0 = lon0
        p1, p2, p0 = r(lat1), r(lat2), r(lat0)
        t = lambda p: math.tan(math.pi / 4 + p / 2)
        self.n = math.log(math.cos(p1) / math.cos(p2)) / math.log(t(p2) / t(p1))
        self.F = math.cos(p1) * t(p1) ** self.n / self.n
        self.r0 = self.F / t(p0) ** self.n

    def __call__(self, lon, lat):
        r = math.radians
        p = max(min(lat, 89.0), -89.0)
        rho = self.F / math.tan(math.pi / 4 + r(p) / 2) ** self.n
        th = self.n * r(lon - self.lon0)
        return (rho * math.sin(th), self.r0 - rho * math.cos(th))


# ---------------------------------------------------------------- clipping

def _clip_edge(pts, inside, isect):
    out = []
    if not pts:
        return out
    for i, cur in enumerate(pts):
        prv = pts[i - 1]
        ci, pi = inside(cur), inside(prv)
        if ci:
            if not pi:
                out.append(isect(prv, cur))
            out.append(cur)
        elif pi:
            out.append(isect(prv, cur))
    return out


def clip_rect(pts, x0, y0, x1, y1):
    """Sutherland-Hodgman against the viewport."""
    def cut(pts, key, lim, keep_ge):
        k = 0 if key == "x" else 1
        ins = (lambda p: p[k] >= lim) if keep_ge else (lambda p: p[k] <= lim)
        def isc(a, b):
            if abs(b[k] - a[k]) < 1e-12:
                return (lim, a[1]) if k == 0 else (a[0], lim)
            t = (lim - a[k]) / (b[k] - a[k])
            return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
        return _clip_edge(pts, ins, isc)
    pts = cut(pts, "x", x0, True)
    pts = cut(pts, "x", x1, False)
    pts = cut(pts, "y", y0, True)
    pts = cut(pts, "y", y1, False)
    return pts


# ---------------------------------------------------------------- frame

class Frame:
    """Maps a lon/lat window onto an SVG viewBox, preserving aspect."""
    def __init__(self, lon_min, lat_min, lon_max, lat_max, width, height,
                 proj=None, pad=0):
        self.proj = proj or LCC(lon0=(lon_min + lon_max) / 2,
                                lat0=(lat_min + lat_max) / 2,
                                lat1=lat_min + (lat_max - lat_min) * .2,
                                lat2=lat_min + (lat_max - lat_min) * .8)
        cs = [self.proj(lo, la)
              for lo in (lon_min, (lon_min + lon_max) / 2, lon_max)
              for la in (lat_min, (lat_min + lat_max) / 2, lat_max)]
        self.px0 = min(c[0] for c in cs); self.px1 = max(c[0] for c in cs)
        self.py0 = min(c[1] for c in cs); self.py1 = max(c[1] for c in cs)
        self.W, self.H, self.pad = width, height, pad
        sx = (width - 2 * pad) / (self.px1 - self.px0)
        sy = (height - 2 * pad) / (self.py1 - self.py0)
        self.s = min(sx, sy)
        self.ox = pad + ((width - 2 * pad) - (self.px1 - self.px0) * self.s) / 2
        self.oy = pad + ((height - 2 * pad) - (self.py1 - self.py0) * self.s) / 2

    def xy(self, lon, lat):
        px, py = self.proj(lon, lat)
        return (self.ox + (px - self.px0) * self.s,
                self.oy + (self.py1 - py) * self.s)

    def path(self, lonlats, close=True, prec=1):
        pts = [self.xy(*p) for p in lonlats]
        if close:
            pts = clip_rect(pts, 0, 0, self.W, self.H)
        if len(pts) < 2:
            return ""
        d = "M" + " L".join(f"{x:.{prec}f} {y:.{prec}f}" for x, y in pts)
        return d + " Z" if close else d

    def land_path(self, polys, min_pts=4, prec=1):
        out = []
        for ring in polys:
            d = self.path(ring, close=True, prec=prec)
            if d and d.count("L") >= min_pts:
                out.append(d)
        return " ".join(out)


def simplify(pts, tol):
    """Cheap point-decimation; tol in degrees."""
    if len(pts) < 3:
        return pts
    out = [pts[0]]
    for p in pts[1:-1]:
        if abs(p[0] - out[-1][0]) > tol or abs(p[1] - out[-1][1]) > tol:
            out.append(p)
    out.append(pts[-1])
    return out
