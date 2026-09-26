# -*- coding: utf-8 -*-
"""pageguard.py - what build_part_g.py and build_part_h.py ask before writing a page.

One definition, shared, as pagewords.py is. Written in review session 10
(REVIEW-CONSISTENCY.md §14.6) after the checker of Part H's new guard got past it
in three ways, every one shown on a scratch copy with the build printing
"all five built clean":

  1. THE BODY THE BUILD READ WAS NOT THE BODY FRESHCHECK CHECKED. freshcheck
     compares files/cNN_body.html with its draft; the build reads the body from
     DK_SRC. With DK_SRC pointing at an old copy, the old body shipped. Now the
     body the build will read must be byte-identical to the one freshcheck
     witnessed (`same_body`).

  2. THE VOCABULARY CHECK READ TEXT, BUT NOT AS A READER DOES. Tags were removed
     with no separator ("entry</li><li>Forliget" became "entryForliget" and \\b
     failed); zero-width characters, full-width letters and Cyrillic look-alikes
     passed; "BAND C" passed (figure labels are upper case); "chapter-07",
     "ch 07", "chapter #07", "chapters 3 through 07" and "Era pages" passed; only
     lower-case, double-quoted aria-label/alt/title attributes were read. And the
     page was written before it was checked. `reader_text` and
     `stale_vocabulary` close each of those, and the build scripts now write a
     page only after it passes.

  3. A STALE FIGURE SHIPPED. The build reads svg_*.txt as it finds them; nothing
     asked whether the figure script still produces them. `figures_fresh` runs
     every script that produces a figure the part needs, in a scratch copy of
     this folder, and compares its output byte-for-byte with the file the build
     will read. That is the figure's own witness, not the builder's.

KNOWN LIMITS, by design. Homoglyphs are folded for the letters the retired words
use, not for every script in Unicode. A figure produced by no script in this
folder (Parts A-D's inline figures) is reported as sourceless, not stale, as
figcheck.py reports it.
"""
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

# Letters that look like the Latin ones the retired words are spelt with.
_CONFUSABLE = str.maketrans({
    'а': 'a', 'в': 'b', 'е': 'e', 'һ': 'h', 'і': 'i', 'ј': 'j', 'о': 'o',
    'р': 'p', 'с': 'c', 'у': 'y', 'х': 'x', 'ԁ': 'd', 'ɡ': 'g', 'ո': 'n',
    'А': 'A', 'В': 'B', 'Е': 'E', 'Н': 'H', 'І': 'I', 'К': 'K', 'М': 'M',
    'О': 'O', 'Р': 'P', 'С': 'C', 'Т': 'T', 'У': 'Y', 'Х': 'X',
    'α': 'a', 'ο': 'o', 'ρ': 'p', 'τ': 't', 'ν': 'v', 'ε': 'e', 'ι': 'i',
    'Α': 'A', 'Β': 'B', 'Ε': 'E', 'Η': 'H', 'Ι': 'I', 'Κ': 'K', 'Μ': 'M',
    'Ν': 'N', 'Ο': 'O', 'Ρ': 'P', 'Τ': 'T', 'Υ': 'Y', 'Χ': 'X',
})
_INVISIBLE = re.compile('[­͏᠎​-‏⁠-⁤﻿]')
_DASHES = re.compile('[‐-―−﹘﹣－]')
# Attributes whose text reaches a reader (or a screen reader): any case, any quoting.
_ATTR = re.compile(r'''\s(aria-[\w-]+|alt|title|placeholder|label|data-[\w-]+)\s*=\s*'''
                   r'''(?:"([^"]*)"|'([^']*)'|([^\s>"']+))''', re.I)


def reader_text(h):
    """The words a reader sees (and a screen reader speaks), for the vocabulary check."""
    raw = re.sub(r'<(script|style)\b.*?</\1\s*>', ' ', h, flags=re.S | re.I)
    raw = re.sub(r'<!--.*?-->', ' ', raw, flags=re.S)
    attrs = ' '.join(a or b or c for _, a, b, c in _ATTR.findall(raw))
    # Every tag becomes a space, so adjacent elements cannot fuse into one word.
    text = re.sub(r'<[^>]*>', ' ', raw) + ' ' + attrs
    text = html.unescape(html.unescape(text))
    text = unicodedata.normalize('NFKC', text)
    text = _INVISIBLE.sub('', text).translate(_CONFUSABLE)
    text = _DASHES.sub('-', text)
    return re.sub(r'\s+', ' ', text).strip()


PATTERNS = [
    # The letter must be a capital A-I: "a brass band a hundred strong" is not a Band.
    ('Band X', r'\b[Bb][Aa][Nn][Dd]\s*-?\s*[A-I]\b'),
    ('entry', r'(?i)\bentr(?:y|ies)\b'),
    ('Era page', r'(?i)\bera\s*-?\s*pages?\b'),
    # Each number is a whole number (no digit on either side), or "1803" splits into
    # "18" + "03" and "Chapter 30 1620 - 1803" fires (found on the first real run,
    # §14.6). Digit boundaries, not \b, so "chapter07" is still caught.
    ('padded', r'(?i)\b(?:chapters?|chs?\.?)\s*(?:no\.?\s*|#\s*|-\s*)?'
               r'(?:(?<!\d)\d+(?!\d)\s*(?:,|&|-|to|and|or|through)?\s*(?:and\s+|or\s+)?)*'
               r'(?<!\d)0\d+(?!\d)'),
]


def stale_vocabulary(h, allowed=()):
    """Counts of retired vocabulary in the reader's text of page `h`. Each allowed
    phrase is removed once first; one no longer on the page is itself reported."""
    prose = reader_text(h)
    gone = []
    for ok in allowed:
        if ok in prose:
            prose = prose.replace(ok, '', 1)
        else:
            gone.append(ok)
    stale = {k: len(re.findall(p, prose)) for k, p in PATTERNS}
    stale = {k: v for k, v in stale.items() if v}
    if gone:
        stale['allow-list phrase not on the page'] = len(gone)
    return stale


# ---------------------------------------------------------------------------------------
# ASK ONCE (D-17, decided by Carsten in review session 11, REVIEW-CONSISTENCY.md §15).
# A page asks each question once, across the five WHAT-THIS-PAGE-ANSWERS questions, the
# checkpoints and the four end tiers. Session 11 measured 20 openers repeating a checkpoint in
# 13 of 21 chapters, and 17 openers repeated in the end tiers, 9 of them word for word. The
# measure is session 10's Recall measure: content-word Jaccard >= 0.4. It cannot see the
# same question asked in different words; that is still the reading pass's job.
_QSTOP = set("the a an and or of to in on at for by with from was were is are be been it its "
             "this that which what who whom why how did does do had has have not but as into "
             "than then there their they them he his she her one two three four five six "
             "seven eight nine ten one's would could should will can may might more most many "
             "much other same did".split())
ASK_ONCE = 0.4


def _qwords(s):
    s = html.unescape(re.sub(r'<[^>]+>', ' ', s)).lower()
    return {w for w in re.findall(r"[a-zæøåéü]+", s) if len(w) > 2 and w not in _QSTOP}


def page_questions(h):
    """[(label, text)] for every question a reader is asked on page `h`."""
    out = []
    m = re.search(r'<ol class="qs">(.*?)</ol>', h, re.S)
    for i, q in enumerate(re.findall(r'<li>(.*?)</li>', m.group(1), re.S) if m else []):
        out.append(('opener %d' % (i + 1), q))
    for k, d in enumerate(re.findall(r'<div class="check">(.*?)</div>', h, re.S)):
        for i, q in enumerate(re.findall(r'<li>(.*?)</li>', d, re.S)):
            out.append(('checkpoint %d.%d' % (k + 1, i + 1), q))
    for name, body in re.findall(r'<div class="qgroup">\s*<p class="qlabel">(.*?)</p>(.*?)</div>',
                                 h, re.S):
        for i, q in enumerate(re.findall(r'<li>(.*?)</li>', body, re.S)):
            out.append(('%s %d' % (re.sub(r'<[^>]+>', '', name).strip(), i + 1), q))
    return out


def asked_twice(h, threshold=ASK_ONCE):
    """Pairs of questions on page `h` that ask the same thing by the measure:
    [(label_a, label_b, jaccard)], highest first."""
    qs = [(lab, _qwords(q)) for lab, q in page_questions(h)]
    hits = []
    for i in range(len(qs)):
        for j in range(i + 1, len(qs)):
            a, b = qs[i][1], qs[j][1]
            if a and b:
                jac = len(a & b) / len(a | b)
                if jac >= threshold:
                    hits.append((qs[i][0], qs[j][0], round(jac, 2)))
    return sorted(hits, key=lambda x: -x[2])


def same_body(src_dir, here, body):
    """True if the body the build reads (src_dir/body) is the body freshcheck checked
    (here/body)."""
    a, b = os.path.join(src_dir, body), os.path.join(here, body)
    if os.path.realpath(a) == os.path.realpath(b):
        return True
    try:
        return open(a, 'rb').read() == open(b, 'rb').read()
    except IOError:
        return False


def producers(here, svg_files):
    """{svg file: the figs_*/map_* script in `here` that writes it, or None}."""
    scripts = sorted(f for f in os.listdir(here)
                     if re.match(r'(figs|map)_\w+\.py$', f))
    src = {s: open(os.path.join(here, s), encoding='utf-8').read() for s in scripts}
    return {f: next((s for s in scripts if '"%s"' % f in src[s] or "'%s'" % f in src[s]),
                    None) for f in svg_files}


def figures_fresh(here, src_dir, svg_files):
    """Run each script that produces one of `svg_files` in a scratch copy of `here`
    and compare what it writes with src_dir/<file>. Returns
    ({file: 'STALE' | 'SOURCELESS' | 'SCRIPT FAILED: ...'}, n_checked)."""
    prod = producers(here, svg_files)
    out, checked = {}, 0
    tmp = tempfile.mkdtemp(prefix='pageguard_')
    try:
        work = os.path.join(tmp, 'files')
        shutil.copytree(here, work, ignore=shutil.ignore_patterns(
            'svg_*.txt', 'look_*.png', '*.html', '__pycache__', '.git'))
        env = dict(os.environ, PYTHONPATH=work, MPLBACKEND='Agg')
        for s in sorted({p for p in prod.values() if p}):
            r = subprocess.run([sys.executable, s], cwd=work, env=env,
                               capture_output=True, text=True, timeout=600)
            if r.returncode != 0:
                for f, p in prod.items():
                    if p == s:
                        out[f] = 'SCRIPT FAILED: %s exited %d' % (s, r.returncode)
        for f, p in prod.items():
            if p is None:
                out[f] = 'SOURCELESS'
                continue
            if f in out:
                continue
            checked += 1
            made = os.path.join(work, f)
            try:
                if open(made, 'rb').read() != open(os.path.join(src_dir, f), 'rb').read():
                    out[f] = 'STALE (%s writes something else)' % p
            except IOError as e:
                out[f] = 'STALE (%s)' % e
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return out, checked
