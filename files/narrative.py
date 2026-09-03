# -*- coding: utf-8 -*-
"""narrative.py - measure the apparatus constant from built pages.

WHY. PLAN_G's length model is `page words ~ sum(section bands) + 2,800`. That
constant was derived from Part F page counts taken BEFORE the pagecount.py fix,
and the fix removed SVG label text, which is apparatus rather than narrative. So
the constant is too high and every chapter planned against it comes out about 400
words long. Recomputing it from Part F's old narrative figures gave 2,389, but
those narrative figures are pre-fix too, so that number is itself derived from
stale inputs. This measures it.

WHAT IT DOES. Page words come from pagecount.pagewords - the canonical definition,
imported and not reimplemented, because seven copies of one rule is how the 5.55
constant drifted. Narrative is what is left after every apparatus element is
removed. Apparatus is then page minus narrative, which cannot disagree with the
page count by construction.

HOW IT FAILS. Loudly. Every stripper must match at least once in every chapter. A
selector that matches nothing is a wrong guess about the markup, and a wrong guess
would otherwise silently inflate the narrative count and deflate the constant -
the exact shape of the fault it exists to correct. On any zero match it prints the
class census and refuses to report a constant.

USAGE
    python3 narrative.py ../2[5-9]-*.html ../3[01]-*.html      # Part G
    python3 narrative.py --census ../25-*.html                 # markup only
"""
import re
import sys
import glob
import os
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pagecount as PC


# In-section apparatus: blocks that sit inside the narrative region and are not
# narrative. Matched with a nesting-aware walker, not a non-greedy regex, so a
# nested tag of the same kind cannot truncate the block and under-strip it.
BLOCKS = [
    ('vignette',   'div', 'vig'),
    ('glossary',   'div', 'terms'),
    ('checkpoint', 'div', 'check'),
    ('meanwhile',  'div', 'meanwhile'),
]

END = r'<div class="myth"'    # the first terminal unit closes the region


def first_numbered_h2(body):
    """Offset of section 01's heading.

    NOT simply the first <h2>: that is the WHAT THIS PAGE ANSWERS block, which is
    header apparatus and was silently counted as narrative in every chapter before
    this was fixed, at roughly 113 words each. A numbered section heading is the
    first whose visible text begins with a digit.
    """
    for m in re.finditer(r'<h2[^>]*>', body):
        head = body[m.end():body.find('</h2>', m.end())]
        text = re.sub(r'<[^>]+>', ' ', head).strip()
        if text[:1].isdigit():
            return m.start()
    return None


def words(fragment):
    """Same rule as pagecount, applied to a fragment rather than a whole page."""
    return len([w for w in re.sub(r'<[^>]+>', ' ', fragment).split()
                if w not in PC.SEPARATORS])


def census(h):
    """Every tag-and-class pair on the page, with counts. Markup discovery only."""
    body = re.sub(r'<svg.*?</svg>', ' ', PC.body_after_style(h), flags=re.S)
    c = Counter()
    for tag, cls in re.findall(r'<(\w+)[^>]*\sclass="([^"]+)"', body):
        c['%s.%s' % (tag, cls)] += 1
    return c, re.findall(r'<section[^>]*\sid="([^"]+)"', body)


def strip_blocks(h, tag, cls):
    """Remove every <tag class="cls"> block, honouring nesting. Returns (html, n)."""
    open_re = re.compile(r'<%s[^>]*\sclass="%s"' % (tag, cls))
    step_re = re.compile(r'<(/?)%s\b' % tag)
    out, pos, n = [], 0, 0
    while True:
        m = open_re.search(h, pos)
        if not m:
            out.append(h[pos:])
            return ''.join(out), n
        out.append(h[pos:m.start()])
        depth, i = 0, m.start()
        for s in step_re.finditer(h, m.start()):
            depth += -1 if s.group(1) else 1
            if depth == 0:
                i = s.end() + h[s.end():].find('>') + 1
                break
        else:
            raise SystemExit('!! unclosed <%s class="%s"> - markup is malformed' % (tag, cls))
        pos, n = i, n + 1


def measure(path):
    h = open(path, encoding='utf-8').read()
    page = PC.pagewords(h)
    body = re.sub(r'<svg.*?</svg>', ' ', PC.body_after_style(h), flags=re.S)

    s = first_numbered_h2(body)
    e = re.search(END, body)
    if s is None or not e:
        raise SystemExit('!! %s: no %s' % (os.path.basename(path),
                                           'numbered section heading' if s is None
                                           else 'div.myth'))
    if e.start() < s:
        raise SystemExit('!! %s: myth block precedes section 01' % path)

    region = body[s:e.start()]
    before_all = words(region)          # before ANY in-region stripping
    hits, removed = {}, {}
    nfig = len(re.findall(r'<figure', region))
    region = re.sub(r'<figure.*?</figure>', ' ', region, flags=re.S)
    hits['figure'] = nfig
    removed['figure'] = before_all - words(region)
    for label, tag, cls in BLOCKS:
        before = words(region)
        region, n = strip_blocks(region, tag, cls)
        hits[label], removed[label] = n, before - words(region)

    narrative = words(region)
    outside = page - before_all   # header, tail, rail, contents, footer, script
    return page, narrative, hits, removed, region, outside


def sections(rest):
    """Narrative words per numbered section, for the weight bands."""
    parts = re.split(r'(<h2[^>]*>)', rest)
    out = []
    for i in range(1, len(parts), 2):
        head = re.sub(r'<[^>]+>', ' ', parts[i] + parts[i + 1][:200]).split()
        label = ' '.join(head[:6])
        out.append((label, words(parts[i + 1])))
    return out


def band(n):
    if n < 340:
        return 'light'
    if n < 560:
        return 'medium'
    if n < 760:
        return 'heavy'
    return 'OVER'


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    only_census = '--census' in sys.argv
    files = []
    for pat in args:
        files.extend(sorted(glob.glob(pat)))
    if not files:
        raise SystemExit('!! no files matched')

    if only_census:
        for f in files:
            classes, ids = census(open(f, encoding="utf-8").read())
            print('\n== %s' % os.path.basename(f))
            for k, v in sorted(classes.items(), key=lambda x: -x[1]):
                print('   %-28s %3d' % (k, v))
            print('   section ids: %s' % ', '.join(ids))
        return

    rows, bad = [], False
    print('%-6s %7s %10s %10s %9s %6s' % ('ch', 'page', 'narrative', 'apparatus', 'outside', 'min'))
    print('-' * 56)
    for f in files:
        page, narr, hits, removed, rest, outside = measure(f)
        ch = re.match(r'(\d+)', os.path.basename(f)).group(1)
        miss = [k for k, v in hits.items() if v == 0]
        if miss:
            bad = True
            print('%-6s  MISSING: %s' % (ch, ', '.join(miss)))
        else:
            print('%-6s %7d %10d %10d %9d %6d'
                  % (ch, page, narr, page - narr, outside, PC.minutes(page)))
        rows.append((ch, page, narr, hits, removed, rest, outside))

    if bad:
        print('\n!! a block selector matched nothing in at least one chapter.')
        print('   Re-run with --census and send the class list.')
        return

    print('-' * 56)
    n = len(rows)
    tp = sum(r[1] for r in rows) / float(n)
    tn = sum(r[2] for r in rows) / float(n)
    print('%-6s %7d %10d %10d %9d'
          % ('mean', tp, tn, tp - tn, sum(r[6] for r in rows) / float(n)))
    print('\nAPPARATUS CONSTANT: %d   (PLAN_G uses 2,800; 2,400 was the estimate)'
          % round(tp - tn))

    print('\nApparatus breakdown, mean words per chapter:')
    for label, _, _ in BLOCKS:
        print('   %-12s %6.0f words   %4.1f blocks'
              % (label, sum(r[4][label] for r in rows) / float(n),
                 sum(r[3][label] for r in rows) / float(n)))
    print('   %-12s %6.0f words          (header, tail, rail, contents, footer)'
          % ('outside', sum(r[6] for r in rows) / float(n)))
    print('   %-12s %6.0f words   %4.1f blocks'
          % ('figure', sum(r[4]['figure'] for r in rows) / float(n),
             sum(r[3]['figure'] for r in rows) / float(n)))

    print('\nNarrative weight per section, observed:')
    counts = Counter()
    for ch, page, narr, hits, removed, rest, _out in rows:
        secs = sections(rest)
        print('\n  ch %s  (%d sections, %d narrative)' % (ch, len(secs), narr))
        for label, w in secs:
            counts[band(w)] += 1
            print('     %-52s %5d  %s' % (label[:52], w, band(w)))
    print('\n  observed distribution: %s' % dict(counts))


if __name__ == '__main__':
    main()
