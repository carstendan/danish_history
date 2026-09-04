#!/usr/bin/env python3
"""
vignettes.py — pull the vignette and meanwhile roster out of chapter bodies.

Run from the folder holding c*_body.html (or pass a folder / file list):

    python3 vignettes.py                 # every c??_body.html in the cwd
    python3 vignettes.py 21 22 23 24     # just those chapters
    python3 vignettes.py /path/to/files  # a folder
    python3 vignettes.py --selftest      # check the normaliser and the tag parser

Reads the authored bodies. If a body is missing it falls back to the shipped
page (NN-*.html), which carries the same markup with the SVGs inlined.

Output is deliberately compact: it is meant to be read in a terminal and
checked against a plan, not parsed.

------------------------------------------------------------------------------
Sept 2026 — two additions: open item 27, and convention D-9.

1. THE PLACE MATCH IS NORMALISED (open item 27). It was exact-string and
   reported Copenhagen five times against a true figure of thirteen of
   forty-eight, because "Blaataarn, Copenhagen Castle" and "the square before
   Copenhagen Castle" and "her father's house in Noerregade, Copenhagen" each
   counted as a place of its own.

   The normaliser works from an explicit gazetteer of anchors — L15, enumerate
   what you want rather than what you want removed. A place matching no anchor
   keeps its own string and appears exactly as it did before, so a gazetteer
   gap under-merges visibly instead of merging something wrongly and silently.

   Matching is on WORD BOUNDARIES, not substrings. "Falsterbo" contains
   "Falster"; "Aalborghus" would contain "Aalborg". A substring gazetteer is a
   silent-fault generator and this project has paid for that shape of bug more
   than once. A place matching two anchors is reported AMBIGUOUS and left
   unmerged rather than assigned by guess.

   Every merge is printed under its anchor, so a wrong merge is caught by
   looking and not only by testing. --selftest asserts the Copenhagen figure
   and the Falsterbo trap.

2. THE D-9 BALANCE LAYER. The (who) line may carry a trailing tag bracket,
   person . place . date . [f][n]: f where a woman is the agent, n where the
   subject is non-elite, both omitted where neither applies. The layer reports,
   per chapter, whether a woman and a non-elite subject are present.

   THE [-] SENTINEL, added Sept 2026. As first written, D-9 omitted both
   brackets where neither flag applied, which made a chapter of three elite
   male vignettes — chapter 25 exactly, the fault D-9 was written to catch
   — textually identical to a chapter nobody had tagged yet. The check could
   not see its own founding case.

   A vignette to which neither flag applies now carries [-]: "considered, and
   neither applies". There are still only two CLAIMS, f and n; [-] asserts
   nothing about the subject, it records that the question was asked. A
   chapter with no bracket at all is untagged; one where every vignette
   carries a bracket and none carries [f] is a failure and says so.

   [-] alongside [f] or [n] is a contradiction, and is reported as malformed.
------------------------------------------------------------------------------
"""

import glob
import html
import os
import re
import sys
from collections import Counter, defaultdict

VIG = re.compile(r'<div class="vig">(.*?)</div>', re.S)
H4 = re.compile(r'<h4[^>]*>(.*?)</h4>', re.S)
WHO = re.compile(r'<p class="who">(.*?)</p>', re.S)
MEANWHILE = re.compile(r'<div class="meanwhile">(.*?)</div>', re.S)
MYTH = re.compile(r'<div class="myth">(.*?)</div>', re.S)
PARA = re.compile(r'<p[^>]*>(.*?)</p>', re.S)
TAG = re.compile(r'<[^>]+>')

# D-9: a trailing run of [f] and/or [n], with or without a leading separator.
# A place field that is only a year or a date is a broken (who) line: see
# open item 22, where Ellen Marsvin's place reads '1629'.
DATEISH = re.compile(r'^\d{3,4}$|^\d{1,2}\s+\w+\s+\d{3,4}$|^\w+\s+\d{3,4}$')
TAGRUN = re.compile(r'(?:\s*\u00b7)?\s*((?:\[[fn-]\])+)\s*$')

# --------------------------------------------------------------------------
# Place gazetteer. Each entry is (anchor, [alternate spellings]); the anchor is
# always matched too. Matching is word-boundary and case-insensitive over a
# string with possessives stripped, so "Copenhagen's raadhus" reaches the
# anchor.
#
# Only settlements and islands are anchored. Provinces deliberately are not:
# rolling Falsterbo and Lindholmen up into Skaane would answer a different
# question from the one this check asks, which is whether two vignettes happen
# in the same place.
#
# Add an anchor when a place acquires a second variant. An unanchored place is
# not an error; it is reported under its own name.
# --------------------------------------------------------------------------
GAZETTEER = [
    ('Copenhagen',     ['K\u00f8benhavn', 'Kj\u00f8benhavn']),
    ('Stockholm',      []),
    ('Aalborg',        ['\u00c5lborg']),
    ('Viborg',         []),
    ('Kiel',           []),
    ('Helsingborg',    []),
    ('Helsing\u00f8r', []),
    ('Malm\u00f6',     ['Malm\u00f8']),
    ('K\u00f8ge',      []),
    ('Falsterbo',      []),
    ('Nyk\u00f8bing',  []),
    ('R\u00f8nne',     []),
    ('Hirschholm',     ['H\u00f8rsholm']),
    ('Christiansborg', []),
    ('Vall\u00f8',     []),
    ('Hemmingstedt',   []),
    ('Hvalsey',        []),
    ('S\u00f8nderborg', []),
    ('Herrevad',       []),
    ('Fredericia',     []),
    ('Aabenraa',       ['\u00c5benr\u00e5']),
    ('Flensburg',      ['Flensborg']),
    ('Dybb\u00f8l',    []),
    ('Hjedding',       []),
    ('Askov',          []),
    ('R\u00f8dding',   []),
    ('Varde',          []),
    ('Kolding',        []),
]

_WORD = re.compile(r'[^\W\d_]+', re.UNICODE)


def _words(s):
    """Lowercased word tokens, possessives dropped."""
    s = s.replace('\u2019', "'")
    s = re.sub(r"'s\b", '', s, flags=re.I)
    return set(w.lower() for w in _WORD.findall(s))


def normalise_place(place):
    """Return (anchor_or_place, was_merged)."""
    toks = _words(place)
    hits = []
    for anchor, alts in GAZETTEER:
        for name in [anchor] + alts:
            if name.lower() in toks:
                hits.append(anchor)
                break
    if len(hits) == 1:
        return hits[0], True
    if len(hits) > 1:
        return ('%s   << AMBIGUOUS: matches %s' % (place, ', '.join(hits))), False
    return place, False


def flat(s):
    """Strip tags, unescape entities, collapse whitespace."""
    return re.sub(r'\s+', ' ', html.unescape(TAG.sub('', s))).strip()


def split_who(raw):
    """Flatten a (who) line into (fields, tags).

    Accepts the D-9 bracket either as its own separated field or appended to
    the date.
    """
    s = flat(raw)
    tags = set()
    m = TAGRUN.search(s)
    if m:
        tags = set(re.findall(r'\[([fn-])\]', m.group(1)))
        s = s[:m.start()].rstrip().rstrip('\u00b7').rstrip()
    return [p.strip() for p in s.split('\u00b7')], tags


def first_sentence(s, limit=110):
    s = flat(s)
    cut = s.find('. ')
    if 0 < cut < limit:
        return s[:cut + 1]
    return s[:limit] + ('\u2026' if len(s) > limit else '')


def find_files(args):
    """Resolve arguments to a sorted list of (chapter_number, path)."""
    args = [a for a in args if not a.startswith('--')]
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
            print('!  chapter %s: no body and no shipped page found' % n)
        found = {n: p for n, p in found.items() if n in wanted}
    return sorted(found.items())


def selftest():
    """Assert the things the normaliser and the tag parser exist to get right."""
    ok = True

    cases = [
        ('Copenhagen', 'Copenhagen'),
        ('Copenhagen castle', 'Copenhagen'),
        ('outside Copenhagen Castle', 'Copenhagen'),
        ('the great hall, Copenhagen Castle', 'Copenhagen'),
        ("Copenhagen's r\u00e5dhus", 'Copenhagen'),
        ('the square before Copenhagen Castle', 'Copenhagen'),
        ('Bl\u00e5t\u00e5rn, Copenhagen Castle', 'Copenhagen'),
        ('Fl\u00e5debatteri nr. 1, Kongedybet, Copenhagen', 'Copenhagen'),
        ("her father's house in N\u00f8rregade, Copenhagen", 'Copenhagen'),
        # The substring trap: Falsterbo must not reach a Falster anchor, and
        # "Nykoebing Slot, Falster" must not reach Falsterbo.
        ('the market at Falsterbo, Sk\u00e5ne', 'Falsterbo'),
        ('Nyk\u00f8bing Slot, Falster', 'Nyk\u00f8bing'),
        # Unanchored places pass through untouched.
        ('an island in Lake Hj\u00e4lmaren', 'an island in Lake Hj\u00e4lmaren'),
        ('the Churchill River, Hudson Bay', 'the Churchill River, Hudson Bay'),
    ]
    for raw, want in cases:
        got, _ = normalise_place(raw)
        if got != want:
            print('  FAIL  %r -> %r, wanted %r' % (raw, got, want))
            ok = False

    tagcases = [
        ('Peter Larsen \u00b7 Kolding \u00b7 1843 \u00b7 [n]', 3, {'n'}),
        ('Johanne Luise \u00b7 Teatret \u00b7 1826 \u00b7 [f][n]', 3, {'f', 'n'}),
        ('Orla Lehmann \u00b7 Casino \u00b7 20 Mar 1848', 3, set()),
        ('Ilia Fibiger \u00b7 a hospital \u00b7 1864 [f]', 3, {'f'}),
        ('Orla Lehmann \u00b7 Casino \u00b7 1841 \u00b7 [-]', 3, {'-'}),
        ('A N Other \u00b7 Varde \u00b7 1843 \u00b7 [-][f]', 3, {'-', 'f'}),
    ]
    for raw, nfields, want in tagcases:
        fields, tags = split_who(raw)
        if tags != want or len(fields) != nfields:
            print('  FAIL  %r -> fields=%r tags=%r, wanted %d fields and %r'
                  % (raw, fields, tags, nfields, want))
            ok = False

    print('  selftest PASSES' if ok else '  selftest FAILS')
    return 0 if ok else 1


def main():
    if '--selftest' in sys.argv:
        return selftest()

    files = find_files(sys.argv[1:])
    if not files:
        print('no chapter files found - run this from the folder holding '
              'c??_body.html, or pass one as an argument')
        return 1

    places, people, counts = Counter(), [], []
    malformed = []
    variants = defaultdict(Counter)
    balance = []

    for num, path in files:
        src = open(path, encoding='utf-8').read()
        tag = '' if path.endswith('_body.html') else '   [shipped page]'
        print('\n%s\nCHAPTER %s%s\n%s' % ('=' * 72, num, tag, '=' * 72))

        vigs = VIG.findall(src)
        counts.append((num, len(vigs)))
        if not vigs:
            print('  (no vignettes found - check the markup)')

        n_tagged = 0
        has_f = has_n = False

        for i, block in enumerate(vigs, 1):
            head = H4.search(block)
            who = WHO.search(block)
            print('\n  %d. %s' % (i, flat(head.group(1)) if head else '(no h4)'))
            if who:
                parts, tags = split_who(who.group(1))
                if tags:
                    n_tagged += 1
                    has_f = has_f or 'f' in tags
                    has_n = has_n or 'n' in tags
                if len(parts) >= 3:
                    person, place = parts[0], parts[1]
                    date = ' \u00b7 '.join(parts[2:])
                    anchor, merged = normalise_place(place)
                    print('     who    %s' % person)
                    print('     place  %s%s' % (
                        place, ('   -> %s' % anchor) if merged and anchor != place else ''))
                    print('     date   %s' % date)
                    shown = ''.join('[%s]' % t for t in 'fn-' if t in tags)
                    if '-' in tags and (tags & {'f', 'n'}):
                        shown += '   << MALFORMED: [-] means neither applies'
                        malformed.append(num)
                    print('     tags   %s' % (shown if tags else '(no bracket — untagged)'))
                    places[anchor] += 1
                    variants[anchor][place] += 1
                    people.append((num, person))
                else:
                    print('     who    %s   << not 3 fields' % flat(who.group(1)))
            else:
                print('     who    << MISSING (Lesson 9a)')
            body = PARA.findall(block)
            opening = next((p for p in body if 'class="who"' not in p), None)
            if opening:
                print('     opens  %s' % first_sentence(opening))

        balance.append((num, len(vigs), n_tagged, has_f, has_n))

        mw = MEANWHILE.findall(src)
        if mw:
            print('\n  meanwhile (%d):' % len(mw))
            for block in mw:
                paras = PARA.findall(block)
                if paras:
                    print('     . %s' % first_sentence(paras[0]))

        my = MYTH.findall(src)
        for block in my:
            head = H4.search(block)
            paras = PARA.findall(block)
            label = flat(head.group(1)) if head else 'myth-check'
            print('\n  %s: %s' % (label, first_sentence(paras[0]) if paras else ''))

    print('\n%s\nSUMMARY\n%s' % ('=' * 72, '=' * 72))
    print('  vignettes per chapter: ' +
          '  '.join('%s:%d' % (n, c) for n, c in counts))
    print('  total: %d' % sum(c for _, c in counts))

    # ---- D-9 balance layer ------------------------------------------------
    print('\n  D-9 balance (woman as agent . non-elite subject):')
    failures, partials, untagged = [], [], []
    for num, n_vigs, n_tagged, has_f, has_n in balance:
        if n_vigs == 0:
            continue
        if n_tagged == 0:
            print('     %s   %d/%d tagged   untagged' % (num, n_tagged, n_vigs))
            untagged.append(num)
            continue
        miss = []
        if not has_f:
            miss.append('no woman as agent')
        if not has_n:
            miss.append('no non-elite subject')
        line = ('     %s   %d/%d tagged   [f] %s   [n] %s   %s'
                % (num, n_tagged, n_vigs,
                   'yes' if has_f else 'NO ',
                   'yes' if has_n else 'NO ',
                   'ok' if not miss else 'FAIL'))
        if miss:
            line += '   << ' + ', '.join(miss)
        if n_tagged < n_vigs:
            line += ('   (partial: %d untagged, so a missing flag may be '
                     'absent or merely untagged)' % (n_vigs - n_tagged))
            partials.append(num)
        print(line)
        if miss:
            failures.append(num)

    if untagged:
        print('\n     untagged chapters: %s  - lazy backfill per D-9, not a fault'
              % ', '.join(untagged))
    if partials:
        print('     partially tagged: %s' % ', '.join(partials))
    if failures:
        print('     D-9 FAILURES: %s' % ', '.join(failures))
    if malformed:
        print('     MALFORMED TAGS: %s  — [-] cannot sit beside [f] or [n]'
              % ', '.join(sorted(set(malformed))))

    # ---- places -----------------------------------------------------------
    print('\n  places used, normalised (repeats first):')
    for place, n in places.most_common():
        forms = variants[place]
        # Collapse to the anchor only when there is something to collapse.
        label = place if len(forms) > 1 else next(iter(forms))
        mark = '  << repeated' if n > 1 else ''
        if DATEISH.match(label.strip()):
            mark += '   << PLACE LOOKS LIKE A DATE (item 22)'
        print('     %d  %s%s' % (n, label, mark))
        if len(forms) > 1:
            for raw, k in forms.most_common():
                print('            %d  %s' % (k, raw))

    print('\n  %d vignettes carry a place; %d distinct places after normalisation'
          % (sum(places.values()), len(places)))

    surnames = Counter(p.split(',')[0].split()[-1] for _, p in people if p)
    dupes = [s for s, n in surnames.items() if n > 1]
    if dupes:
        print('\n  people appearing more than once: ' + ', '.join(sorted(dupes)))

    return 0


if __name__ == '__main__':
    sys.exit(main())
