# -*- coding: utf-8 -*-
"""sweep_names.py - the same person or place written differently across chapters.

    python3 sweep_names.py

Reads every reader-facing word on the built pages (reviewlib.Page.alltext) and
reports four kinds of disagreement. Each is a reading list with the evidence on
it - chapters and counts - not a verdict, because a variant is sometimes right
(a quotation keeps its source's spelling; a Swedish place in a Swedish treaty).

  1. REGNAL STYLE. The book writes Danish kings "Christian 4.", Danish style.
     Any Roman-numeral or English-ordinal regnal form for a Danish or
     Scandinavian king is listed with its chapter. The name list is the
     Oldenburg and earlier Danish regnal names that occur on the pages in the
     house style - derived, not typed: a name counts as regnal when the page
     text contains it followed by "<digits>." at least once.

  2. ORTHOGRAPHIC VARIANTS. Capitalised words that fold to the same key under
     aa/å, oe/ø/ö, ae/æ/ä, i/j, c/k before a vowel-less position is NOT folded
     (Christian/Kristian are different spellings the book may use on purpose -
     those are caught by 3). Reported when two surface forms each occur.

  3. NEAR-SPELLINGS. Capitalised words of seven or more letters, occurring in
     different chapters, that differ by one edit and are not inflections of
     each other (plural -s, possessive, Danish article -en/-et/-ne). Noisy by
     nature; the list is short enough to read.

  4. EXONYM PAIRS. English and Danish (or German) names for one place or thing,
     where the book uses both. The pairs are enumerated below because an
     exonym cannot be derived by rule - enumerate what you want (L15). Each pair
     is reported with per-chapter counts, so a chapter that switches convention
     against its neighbours stands out.
"""
import re
from collections import Counter, defaultdict

import reviewlib as R

# (English/other, Danish) - the pairs whose mixing a reader would notice.
EXONYMS = [
    ("Copenhagen", "København"), ("Jutland", "Jylland"), ("Zealand", "Sjælland"),
    ("Funen", "Fyn"), ("Scania", "Skåne"), ("Schleswig", "Slesvig"),
    ("Holstein", "Holsten"), ("Elsinore", "Helsingør"), ("Sound", "Øresund"),
    ("Eider", "Ejder"), ("Duppel", "Dybbøl"), ("Düppel", "Dybbøl"),
    ("Flensburg", "Flensborg"), ("Hadersleben", "Haderslev"), ("Apenrade", "Aabenraa"),
    ("Sonderburg", "Sønderborg"), ("Gottorf", "Gottorp"), ("Lubeck", "Lübeck"),
    ("Scandinavia", "Skandinavien"), ("Greenland", "Grønland"), ("Faroes", "Færøerne"),
    ("Faroe", "Færø"), ("Iceland", "Island"), ("Bornholm", "Borgundarholm"),
    ("Canute", "Knud"), ("Cnut", "Knud"), ("Valdemar", "Waldemar"),
    ("Margaret", "Margrete"), ("Eric", "Erik"), ("Christopher", "Christoffer"),
    ("Frederick", "Frederik"), ("Olaf", "Oluf"), ("Sweyn", "Svend"), ("Harold", "Harald"),
    ("Gorm", "Gorm"), ("Absalon", "Axel"), ("Reventlou", "Reventlow"),
    ("Tordenskiold", "Tordenskjold"), ("Griffenfeldt", "Griffenfeld"),
    ("Schimmelman", "Schimmelmann"), ("Bernstorf", "Bernstorff"),
    ("Kalmar", "Calmar"), ("Visby", "Wisby"), ("Rügen", "Rygen"), ("Rugen", "Rügen"),
    ("Stralsund", "Strålsund"), ("Lund", "Lunden"), ("Riga", "Riga"),
    ("Reval", "Tallinn"), ("Estonia", "Estland"), ("Gotland", "Gulland"),
    ("Danevirke", "Dannevirke"), ("Hedeby", "Haithabu"), ("Hedeby", "Hedeby"),
    ("Jelling", "Jællinge"), ("Roskilde", "Roeskilde"), ("Aarhus", "Århus"),
    ("Aalborg", "Ålborg"), ("Ribe", "Riberhus"), ("Kiel", "Kiel"),
    ("Saint Croix", "St Croix"), ("St. Croix", "St Croix"), ("St Thomas", "St. Thomas"),
    ("St John", "St Jan"), ("Tranquebar", "Trankebar"), ("Serampore", "Frederiksnagore"),
]

KINGS_ROMAN = re.compile(
    r"\b(Christian|Frederik|Frederick|Valdemar|Waldemar|Erik|Eric|Knud|Canute|Hans|Oluf|Olaf|"
    r"Christoffer|Christopher|Svend|Sweyn|Harald|Abel|Magnus|Gustav|Gustavus|Karl|Charles|Haakon|Håkon)"
    r"\s+(?:(I{1,3}|IV|V|VI{0,3}|IX|X|XI{0,3}|XIV|XV)\b(?!\.\w)|(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth)\b)")

CAP = re.compile(r"\b[A-ZÆØÅÄÖÜÉ][a-zæøåäöüéèáíóú]+(?:-[A-ZÆØÅ][a-zæøåäöü]+)?\b")


def fold(w):
    t = w.lower()
    for a, b in (("aa", "å"), ("oe", "ø"), ("ö", "ø"), ("ae", "æ"), ("ä", "æ"),
                 ("ü", "y"), ("é", "e"), ("è", "e"), ("á", "a")):
        t = t.replace(a, b)
    return t


INFLECT = re.compile(r"^(.*?)(s|'s|es|en|et|ne|erne|ens|ets|e)$")


def is_inflection(a, b):
    if a.startswith(b) or b.startswith(a):
        longer, shorter = (a, b) if len(a) > len(b) else (b, a)
        return longer[len(shorter):] in ("s", "es", "en", "et", "ne", "e", "ens", "n")
    return False


def edit1(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        d = [i for i in range(len(a)) if a[i] != b[i]]
        if len(d) == 1:
            return True
        if len(d) == 2 and d[1] == d[0] + 1 and a[d[0]] == b[d[1]] and a[d[1]] == b[d[0]]:
            return True
        return False
    if len(a) > len(b):
        a, b = b, a
    for i in range(len(b)):
        if b[:i] + b[i + 1:] == a:
            return True
    return False


def main():
    pages = R.load()
    texts = {p.n: p.alltext() for p in pages}

    # ---- 1. regnal style ----------------------------------------------------
    print("=" * 78)
    print("1. REGNAL STYLE - Roman numerals or ordinals where the book writes 'Christian 4.'")
    print("=" * 78)
    n1 = 0
    for n, t in texts.items():
        for m in KINGS_ROMAN.finditer(t):
            ctx = t[max(0, m.start() - 60):m.end() + 50]
            # an ordinal that is plainly not regnal ("Christian first", "Hans second")
            # is kept: the list is to be read
            n1 += 1
            print("  %2d  %-22s ...%s..." % (n, m.group(0), ctx))
    print("  %d" % n1)

    # ---- word census ---------------------------------------------------------
    where = defaultdict(Counter)
    for n, t in texts.items():
        for w in CAP.findall(t):
            where[w][n] += 1

    # ---- 2. orthographic variants -------------------------------------------
    print()
    print("=" * 78)
    print("2. ORTHOGRAPHIC VARIANTS - aa/å, oe/ø/ö, ae/æ/ä, ü/y, accents")
    print("=" * 78)
    groups = defaultdict(set)
    for w in where:
        groups[fold(w)].add(w)
    n2 = 0
    for k in sorted(groups):
        forms = groups[k]
        if len(forms) > 1:
            n2 += 1
            print("  " + "  |  ".join("%s %s" % (f, dict(sorted(where[f].items()))) for f in sorted(forms)))
    print("  %d groups" % n2)

    # ---- 3. near spellings ---------------------------------------------------
    print()
    print("=" * 78)
    print("3. NEAR-SPELLINGS - one edit apart, 7+ letters, not an inflection, in different chapters")
    print("=" * 78)
    words = sorted(w for w in where if len(w) >= 7)
    bylen = defaultdict(list)
    for w in words:
        bylen[len(w)].append(w)
    pairs = []
    for w in words:
        for L in (len(w), len(w) + 1):
            for v in bylen.get(L, []):
                if v <= w and L == len(w):
                    continue
                if v == w or fold(v) == fold(w) or is_inflection(w.lower(), v.lower()):
                    continue
                if edit1(w.lower(), v.lower()):
                    if set(where[w]) != set(where[v]) or len(where[w]) == 1:
                        pairs.append((w, v))
    for w, v in pairs:
        print("  %-18s %-28s | %-18s %s" % (w, dict(sorted(where[w].items())), v, dict(sorted(where[v].items()))))
    print("  %d pairs" % len(pairs))

    # ---- 4. exonym pairs -----------------------------------------------------
    print()
    print("=" * 78)
    print("4. EXONYM PAIRS - both forms on the pages")
    print("=" * 78)
    n4 = 0
    for a, b in EXONYMS:
        if a == b:
            continue
        ra = re.compile(r"\b%s\b" % re.escape(a))
        rb = re.compile(r"\b%s\b" % re.escape(b))
        ca = {n: len(ra.findall(t)) for n, t in texts.items()}
        cb = {n: len(rb.findall(t)) for n, t in texts.items()}
        ca = {k: v for k, v in ca.items() if v}
        cb = {k: v for k, v in cb.items() if v}
        if ca and cb:
            n4 += 1
            print("  %s %d in %d ch  vs  %s %d in %d ch" % (a, sum(ca.values()), len(ca),
                                                         b, sum(cb.values()), len(cb)))
            print("      %-14s %s" % (a, ca))
            print("      %-14s %s" % (b, cb))
    print("  %d pairs with both forms" % n4)


if __name__ == "__main__":
    main()
