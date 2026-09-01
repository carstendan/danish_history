# -*- coding: utf-8 -*-
"""
fixindex.py — bring index_generator.py onto the new chapter numbering.

Not a simple shift. Two entries become two rows each:

    old 16  Margrete I and the Kalmar Union   -> 16 + 17
    old 21  Christian 4.                      -> 22 + 23

Everything else moves: 17-20 by +1, 22-40 by +2. Total 40 -> 42.

    python3 fixindex.py --dry     # report, write nothing
    python3 fixindex.py           # rewrite, leaving a .bak
"""
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "index_generator.py")

NEW_16 = '''(16,4,"Margrete I and the making of the union","1375 - 1397",1386,
 "The most capable ruler in Danish history assembles three kingdoms without ever formally being queen of them, and it ends at Kalmar in 1397 - the high-water mark of Nordic unity.",
 ["Oluf & Hakon","Falsterbo 1387","Falkoping 1389","Kalmar 1397","Margrete's statecraft"]),'''

NEW_17 = '''(17,4,"The union at work, and the end of Margrete","1397 - 1412",1405,
 "What the union was day to day: an administration rather than a document. Norway slides from partner to province, the last ship sails from Greenland, and the deserted farms reshape who works the land.",
 ["Erik af Pommern","Norway from partner to province","Hvalsey 1408","odegarde","Birgitta & sjaelegave"]),'''

NEW_22 = '''(22,5,"Christian 4.: ambition and the building years","1588 - 1625",1606,
 "The king every Dane can name, in the half of his reign that worked: towns founded, spires raised, companies chartered, Norway governed hard - and one war with Sweden that settles nothing.",
 ["formynderregeringen 1588-96","Kalmarkrigen 1611-13","Rundetarn, Borsen, Christianshavn","Trankebar 1620","Christiania and the Norwegian mines"]),'''

NEW_23 = '''(23,5,"Christian 4.: the wars that broke him","1625 - 1648",1636,
 "Sixty years of building are undone in twenty. He enters the Thirty Years' War as a German prince, loses, and watches a Swedish army march into Jutland twice.",
 ["Lutter am Barenberge 1626","Wallenstein in Jutland 1627-29","the debts","Torstenssonkrigen 1643-45","Kolberger Heide 1644"]),'''

DENSE_NEW = "DENSE = {27, 28, 30, 34, 40}"


def newnum(n):
    if n <= 15:
        return n
    if n <= 20:
        return n + 1
    return n + 2


def main(dry):
    src = open(PATH, encoding="utf-8").read()

    if re.search(r'"1660[^"]{1,8}1814"', src):
        src = re.sub(r'"1660[^"]{1,8}1814"', '"1660 \u2013 1814"', src)
        print("fixed: Part G date label")

    m = re.search(r"\nE = \[\n(.*?)\n\]\n", src, re.S)
    if not m:
        raise SystemExit("!! could not find the E table")
    body = m.group(1)

    starts = [mm.start() for mm in re.finditer(r"(?m)^\(\d+,", body)]
    if not starts:
        raise SystemExit("!! no entries matched inside the E table")
    starts.append(len(body))
    entries = [body[starts[i]:starts[i + 1]].rstrip("\n")
               for i in range(len(starts) - 1)]
    print("read %d entries" % len(entries))

    out = []
    for e in entries:
        n = int(re.match(r"\((\d+),", e).group(1))
        if n == 16:
            out += [NEW_16, NEW_17]
            print("  16 -> 16 + 17  (split)")
        elif n == 21:
            out += [NEW_22, NEW_23]
            print("  21 -> 22 + 23  (split)")
        else:
            t = newnum(n)
            if t != n:
                e = re.sub(r"^\(\d+,", "(%d," % t, e)
                print("  %d -> %d" % (n, t))
            out.append(e)

    src = src[:m.start(1)] + "\n".join(out) + src[m.end(1):]
    print("wrote %d entries" % len(out))

    src = re.sub(r"(?m)^DENSE = \{[^}]*\}", DENSE_NEW, src)
    print("set %s" % DENSE_NEW)

    print("\nliterals still to check by hand:")
    lines = src.splitlines()
    for pat, why in [(r"\b40\b", "old chapter total"),
                     (r"25.{1,3}45", "old reading band"),
                     (r"\bentries\b", "retired vocabulary"),
                     (r"\bentry\b", "retired vocabulary"),
                     (r"16a|16b", "retired split")]:
        for mm in re.finditer(pat, src):
            ln = src[:mm.start()].count("\n") + 1
            ctx = lines[ln - 1].strip()
            if ctx.startswith("#") or "class" in ctx:
                continue
            print("  L%-5d [%s] %s" % (ln, why, ctx[:96]))

    if dry:
        print("\n--dry: nothing written")
        return
    shutil.copy2(PATH, PATH + ".bak")
    open(PATH, "w", encoding="utf-8").write(src)
    print("\nwritten; .bak alongside")


if __name__ == "__main__":
    main("--dry" in sys.argv)
