# -*- coding: utf-8 -*-
"""appcheck.py - does every word of a chapter's apparatus draft reach its page?

WHY THIS EXISTS. On 18 September 2026 a review of the built HTML found that
2,719 words of written myth-check prose - 49% of all the myth-check in the book -
were not on the pages. Seven chapters shipped the heading over an empty list.
Five shipped the claim and one sentence of a four-paragraph correction. Nine
printed each claim in the correction's type and each correction in the claim's.
The cause was a single parser in mkbody.py that understood one of the four
myth-check conventions the drafts actually use.

NOTHING IN THE SUITE COULD SEE IT. tidy.py reads file names. figcheck.py compares
figures to their sources. vignettes.py counts places and people. debuild.py verify
reconstructs the draft from the page and cannot detect prose that never reached
the page in the first place, because the page is its only witness. freshcheck.py
asks whether the draft is newer than the build. Every one of them passed on all
45 chapters while half the myth-check was missing.

SO THIS ASKS THE ONE QUESTION NONE OF THEM ASKED: for each apparatus block, how
many words are in the draft, and how many are on the page? A build that drops
prose is a build that failed, whatever else it reports. The check is crude on
purpose - word counts, not structure - because the fault it exists to catch was
invisible to every structural check in the project.

A shortfall is a REFUSAL. A page carrying more words than its draft is normal
(headings, labels and the section number are added at build time) and is not
reported unless it is extreme, which would mean a block was built twice.

    python3 appcheck.py             # every chapter that has a draft
    python3 appcheck.py 37 38 45    # named chapters only
"""
import os
import re
import sys

import dkpaths

TOL = 0.92          # a page must carry at least this share of its draft's words
FAT = 1.60          # and not this much more, which would mean a doubled block

PARTS = [
    ('Danish terms, by section', 'terms'),
    ('Meanwhile in Europe', 'meanwhile'),
    ('Myth-check', 'myth'),
    ('Carry-forward', 'forward'),
    ('Summary', 'summary'),
    ('Questions', 'questions'),
    ('Sources', 'sources'),
    ('Visit', 'visit'),
]

# NOT CHECKED, AND HERE IS WHY. 'Checkpoints' is not built from the draft. The
# draft states the answer; the build_part_X.py scripts ask the question, by hand
# - "About what proportion did not survive the crossing?" against the draft's
# "About one in five of them died on the crossing." Comparing the two counts a
# rewrite as a loss, on eight chapters, every run. A guard that cries wolf eight
# times is one people learn to skim, which is how the myth-check fault survived
# a suite that ran clean. So it is named here rather than left to be rediscovered.
UNCHECKED = {'Checkpoints': 'built by hand in build_part_X.py, not from the draft'}
TAIL_IDS = {'forward': 'forward', 'summary': 'summary', 'questions': 'questions',
            'sources': 'sources', 'visit': 'visit'}


def words(s):
    return len(re.sub(r'\s+', ' ', s).split())


def detag(t):
    t = re.sub(r'<(script|style)\b.*?</\1>', ' ', t, flags=re.S)
    t = re.sub(r'<!--.*?-->', ' ', t, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    for a, b in (('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'), ('&nbsp;', ' ')):
        t = t.replace(a, b)
    return re.sub(r'\s+', ' ', t).strip()


def apparatus_part(app, heading):
    m = re.search(r'^## %s\s*$' % re.escape(heading), app, re.M)
    if not m:
        return ''
    nxt = re.search(r'^## ', app[m.end():], re.M)
    return app[m.end():m.end() + (nxt.start() if nxt else len(app))]


def div_block(h, cls):
    """All <div class="cls"> blocks, brace-counted so nested divs do not truncate.

    The class="..." is matched with its optional trailing attributes, because
    the myth block carries id="myth" and an earlier version of this file, which
    matched only `<div class="myth">`, reported every Part I myth block as zero
    words and would have sent somebody to fix a parser that was working.
    """
    out = []
    for m in re.finditer(r'<div class="%s"(?:\s[^>]*)?>' % cls, h):
        j, depth = m.end(), 1
        while depth and j < len(h):
            n = re.search(r'<(/?)div\b', h[j:])
            if not n:
                break
            j += n.end()
            depth += -1 if n.group(1) else 1
        out.append(h[m.end():max(j - 6, m.end())])
    return out


def tail_block(h, tid):
    idx = [(m.start(), m.group(1)) for m in re.finditer(r'<h2 id="([^"]+)"', h)]
    for i, (p, t) in enumerate(idx):
        if t == tid:
            return h[p:idx[i + 1][0] if i + 1 < len(idx) else len(h)]
    return ''


def page_words(h, key):
    if key in TAIL_IDS:
        return words(detag(tail_block(h, TAIL_IDS[key])))
    if key == 'myth':
        return sum(words(detag(b)) for b in div_block(h, 'myth'))
    return sum(words(detag(b)) for b in div_block(h, key))


def draft_text(src, ch):
    for name in ('c%d_draft_apparatus.md' % ch, 'c%d_draft.md' % ch):
        p = os.path.join(src, name)
        if os.path.exists(p):
            t = open(p, encoding='utf-8').read()
            if re.search(r'^## Summary\s*$', t, re.M):
                return t, name
    return None, None


def page_path(out, ch):
    for f in sorted(os.listdir(out)):
        if f.endswith('.html') and re.match(r'^%02d-' % ch, f):
            return os.path.join(out, f)
    return None


def main():
    src = os.path.dirname(os.path.abspath(__file__))
    out = dkpaths.resolve('DK_CHAPTERS', os.path.join(src, '..'),
                          'the folder the built chapters are written to')
    want = [int(a) for a in sys.argv[1:] if a.isdigit()] or list(range(1, 46))

    bad, skipped, checked = [], [], 0
    print('%-4s %-26s %8s %8s   %s' % ('ch', 'block', 'draft', 'page', 'verdict'))
    print('-' * 74)
    for ch in want:
        app, name = draft_text(src, ch)
        page = page_path(out, ch)
        if app is None:
            skipped.append((ch, 'no apparatus draft in the repo'))
            continue
        if page is None:
            skipped.append((ch, 'no built page'))
            continue
        h = open(page, encoding='utf-8').read()
        for heading, key in PARTS:
            blk = apparatus_part(app, heading)
            if key == 'terms':
                # Compared by entry, not by word: the draft carries **\u00a701 \u2014 the
                # trade** section labels that the page renders as structure rather
                # than as text, so a word count reads the difference as a loss.
                dw = len(re.findall(r'^\s*-\s+\*\*', blk, re.M))
                pw = sum(len(re.findall(r'<dt>', b)) for b in div_block(h, 'terms'))
                unit = 'entries'
            else:
                dw = words(re.sub(r'[*>`#|-]', ' ', blk))
                pw = page_words(h, key)
                unit = 'words'
            if not dw:
                continue
            checked += 1
            if pw < dw * TOL:
                bad.append((ch, heading, dw, pw))
                print('%-4d %-26s %8d %8d   !! %d %s did not reach the page'
                      % (ch, heading, dw, pw, dw - pw, unit))
            elif pw > dw * FAT:
                bad.append((ch, heading, dw, pw))
                print('%-4d %-26s %8d %8d   !! page carries %.1fx its draft - built twice?'
                      % (ch, heading, dw, pw, pw / dw))
    print('-' * 74)
    print('  %d apparatus block(s) checked in %d chapter(s)'
          % (checked, len(want) - len(skipped)))

    if skipped:
        print('\n  skipped, and named rather than silently passed:')
        for ch, why in skipped:
            print('     chapter %-3d %s' % (ch, why))

    if bad:
        print('\n!! %d block(s) do not survive the build. A build that drops prose is a'
              '\n   build that failed. Fix the parser in mkbody.py - not the page, which'
              '\n   the next build would overwrite - and rebuild.' % len(bad))
        return 1
    print('\n  every apparatus block reaches its page')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
