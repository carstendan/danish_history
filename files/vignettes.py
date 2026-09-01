#!/usr/bin/env python3
"""
vignettes.py — pull the vignette and meanwhile roster out of chapter bodies.

Run from the folder holding c*_body.html (or pass a folder / file list):

    python3 vignettes.py                 # every c??_body.html in the cwd
    python3 vignettes.py 21 22 23 24     # just those chapters
    python3 vignettes.py /path/to/files  # a folder

Reads the authored bodies. If a body is missing it falls back to the shipped
page (NN-*.html), which carries the same markup with the SVGs inlined.

Output is deliberately compact: it is meant to be read in a terminal and
checked against a plan, not parsed.
"""

import glob
import html
import os
import re
import sys
from collections import Counter

VIG = re.compile(r'<div class="vig">(.*?)</div>', re.S)
H4 = re.compile(r'<h4[^>]*>(.*?)</h4>', re.S)
WHO = re.compile(r'<p class="who">(.*?)</p>', re.S)
MEANWHILE = re.compile(r'<div class="meanwhile">(.*?)</div>', re.S)
MYTH = re.compile(r'<div class="myth">(.*?)</div>', re.S)
PARA = re.compile(r'<p[^>]*>(.*?)</p>', re.S)
TAG = re.compile(r'<[^>]+>')


def flat(s):
    """Strip tags, unescape entities, collapse whitespace."""
    return re.sub(r'\s+', ' ', html.unescape(TAG.sub('', s))).strip()


def first_sentence(s, limit=110):
    s = flat(s)
    cut = s.find('. ')
    if 0 < cut < limit:
        return s[:cut + 1]
    return s[:limit] + ('…' if len(s) > limit else '')


def find_files(args):
    """Resolve arguments to a sorted list of (chapter_number, path)."""
    if len(args) == 1 and os.path.isdir(args[0]):
        root, args = args[0], []
    else:
        root = '.'

    wanted = {a.zfill(2) for a in args if a.isdigit()}
    explicit = [a for a in args if os.path.isfile(a)]
    if explicit:
        return [(os.path.basename(p)[1:3], p) for p in sorted(explicit)]

    found = {}
    for p in sorted(glob.glob(os.path.join(root, 'c[0-9][0-9]_body.html'))):
        found[os.path.basename(p)[1:3]] = p
    for p in sorted(glob.glob(os.path.join(root, '[0-9][0-9]*.html'))):
        n = os.path.basename(p)[:2]
        found.setdefault(n, p)          # shipped page only if no body

    if wanted:
        missing = wanted - set(found)
        for n in sorted(missing):
            print(f'!  chapter {n}: no body and no shipped page found')
        found = {n: p for n, p in found.items() if n in wanted}
    return sorted(found.items())


def main():
    files = find_files(sys.argv[1:])
    if not files:
        print('no chapter files found — run this from the folder holding '
              'c??_body.html, or pass one as an argument')
        return 1

    places, people, counts = Counter(), [], []

    for num, path in files:
        src = open(path, encoding='utf-8').read()
        tag = '' if path.endswith('_body.html') else '   [shipped page]'
        print(f'\n{"=" * 72}\nCHAPTER {num}{tag}\n{"=" * 72}')

        vigs = VIG.findall(src)
        counts.append((num, len(vigs)))
        if not vigs:
            print('  (no vignettes found — check the markup)')

        for i, block in enumerate(vigs, 1):
            head = H4.search(block)
            who = WHO.search(block)
            print(f'\n  {i}. {flat(head.group(1)) if head else "(no h4)"}')
            if who:
                parts = [p.strip() for p in flat(who.group(1)).split('·')]
                if len(parts) >= 3:
                    person, place, date = parts[0], parts[1], ' · '.join(parts[2:])
                    print(f'     who    {person}')
                    print(f'     place  {place}')
                    print(f'     date   {date}')
                    places[place] += 1
                    people.append((num, person))
                else:
                    print(f'     who    {flat(who.group(1))}   << not 3 fields')
            else:
                print('     who    << MISSING (Lesson 9a)')
            body = PARA.findall(block)
            opening = next((p for p in body if 'class="who"' not in p), None)
            if opening:
                print(f'     opens  {first_sentence(opening)}')

        mw = MEANWHILE.findall(src)
        if mw:
            print(f'\n  meanwhile ({len(mw)}):')
            for block in mw:
                paras = PARA.findall(block)
                if paras:
                    print(f'     · {first_sentence(paras[0])}')

        my = MYTH.findall(src)
        for block in my:
            head = H4.search(block)
            paras = PARA.findall(block)
            label = flat(head.group(1)) if head else 'myth-check'
            print(f'\n  {label}: {first_sentence(paras[0]) if paras else ""}')

    print(f'\n{"=" * 72}\nSUMMARY\n{"=" * 72}')
    print('  vignettes per chapter: ' +
          '  '.join(f'{n}:{c}' for n, c in counts))
    print(f'  total: {sum(c for _, c in counts)}')

    print('\n  places used (repeats first):')
    for place, n in places.most_common():
        mark = '  << repeated' if n > 1 else ''
        print(f'     {n}  {place}{mark}')

    surnames = Counter(p.split(',')[0].split()[-1] for _, p in people if p)
    dupes = [s for s, n in surnames.items() if n > 1]
    if dupes:
        print('\n  people appearing more than once: ' + ', '.join(sorted(dupes)))

    return 0


if __name__ == '__main__':
    sys.exit(main())
