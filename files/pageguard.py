# -*- coding: utf-8 -*-
"""pageguard.py - what every part's build asks before writing a page.

Parts G and H from review session 10, I from session 11, and A-F (build_parts_abc.py,
build_part_d.py, build_part_e.py, build_part_f.py) from session 12. Parts A-F have
authored bodies and no drafts, so freshcheck does not apply to them; the other checks do.

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
folder is reported as sourceless, not stale: Parts A-C's figures are inline in their
bodies, and Part D's twelve svg_*.txt have no generator on disk. Nothing can witness
their content; `same_sources` can still witness that the build reads the copies in this
folder. `producers` takes the first script (in name order) that quotes a figure's name
or stem anywhere, a comment included, so the producer it reports can be the wrong one.
That never passes a stale figure: every producer found is run in the same scratch copy,
and a figure passes only if the file there is byte-identical to the one the build reads
(review session 12, checks 1 and 2).
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


def summary(count_word, fail, warned):
    """A part build's last line. "all four built clean" only when nothing failed and nothing
    warned; a warning still writes the page, but the last line says "!!" (review session 17,
    check 1: the builds printed the figure scripts' warnings and then "built clean")."""
    if fail:
        return '!! %d problem(s)%s' % (fail, ', and %d warning line(s) above' % warned if warned else '')
    if warned:
        return ('!! all %s built, with %d warning line(s) above - read them'
                % (count_word, warned))
    return 'all %s built clean' % count_word


# Every warning figures_fresh() has printed in this run, so a build's last line can say so:
# a "!!" in the middle of a long log is read by nobody (review session 17, check 1).
WARNINGS = []


def figure_text(h):
    """What mapspine's text guards - overruns(), overflows(), collisions() - say about every
    figure in a built page, as ['figure k: ...']. Empty when they say nothing.

    WHY (review session 17). Those guards run only inside the figure scripts, through
    rasterise(). Parts A-C's thirty figures are written by hand in their bodies and Part D's
    twelve svg_*.txt have no script, so no guard had ever measured their text: the first run
    found "Vedbaek" cut off 02's third map, "Maglemose (Mullerup)" through "Tybrind Vig", 03's
    three captions printed into each other, 08's caption off the edge and 10's two captions
    below the canvas - all shipped. build_parts_abc.py and build_part_d.py ask this for every
    page and print what it says; Parts E-I's figures are guarded where their scripts write
    them (figures_fresh prints the scripts' warnings)."""
    import contextlib
    import io
    import mapspine as M
    out = []
    for k, svg in enumerate(re.findall(r'<svg\b.*?</svg>', h, re.S), 1):
        if 'viewBox="' not in svg:
            continue
        with contextlib.redirect_stdout(io.StringIO()):
            over = M.overruns(svg, '')
            under = M.overflows(svg, '')
            hit = M.collisions(svg, '')
        out += ['figure %d: text may overrun the canvas: %s' % (k, t) for t in over]
        out += ['figure %d: text past the top or bottom of the canvas: %s' % (k, t) for t in under]
        out += ['figure %d: text collides (%.0f units): %r over %r' % (k, o, a, b)
                for a, b, o in hit]
    return out


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


def same_sources(src_dir, here, names):
    """The names among `names` whose copy in src_dir (what the build reads, DK_SRC) is
    not the one in `here` - or is missing from either. Review session 12: a build of Parts
    A-F reads its body, style.css, rail.js and (Part D) sourceless figures through DK_SRC,
    and a checker shipped a planted figure through it with the build printing clean.
    A file missing from src_dir is reported even when src_dir is `here` (same_body alone
    says True there, and the build then died with a traceback - check 2)."""
    return [f for f in names if not os.path.exists(os.path.join(src_dir, f))
            or not same_body(src_dir, here, f)]


def producers(here, svg_files):
    """{svg file: the fig_*/figs_*/map_* script in `here` that writes it, or None}.

    A script names its output either whole ("svg_x.txt") or by stem ("svg_x", with
    `name + ".txt"` at the write). Until review session 12 only figs_*/map_* scripts were
    read, and only for the whole name, so twelve of Part E's fourteen figures read as
    SOURCELESS: two written by fig_crowns.py and fig_titles.py (missed by the prefix) and
    ten written by stem in figs_16b/17/18/19.py. A stale svg_fealty.txt (figs_18.py moved
    two labels to style= under D-11 and was never re-run) had no witness at all
    (REVIEW-CONSISTENCY.md §16)."""
    scripts = sorted(f for f in os.listdir(here)
                     if re.match(r'(figs?|map)_\w+\.py$', f))
    src = {s: open(os.path.join(here, s), encoding='utf-8').read() for s in scripts}

    def named(f, s):
        stem = f[:-4] if f.endswith('.txt') else f
        return any(q % x in src[s] for q in ('"%s"', "'%s'") for x in (f, stem))
    return {f: next((s for s in scripts if named(f, s)), None) for f in svg_files}


def figures_fresh(here, src_dir, svg_files):
    """Run each script that produces one of `svg_files` in a scratch copy of `here`
    and compare what it writes with src_dir/<file>. Returns
    ({file: 'STALE' | 'SOURCELESS' | 'SCRIPT FAILED: ...'}, n_checked).

    It also PRINTS what the scripts warn (review session 17). Every script runs mapspine's
    overruns(), overflows() and collisions() through rasterise(), each printing a "!" line;
    until then this threw those lines away with the rest of the output, as figcheck --regen
    did, and the builds said "all fresh" over page 18's cut-off Sound strip. Each "!" line
    and each stderr line of a script that exits 0 is printed under the script's name, then
    one "!!" count line, and each is kept in WARNINGS for the build's last line. Freshness
    is unchanged: a warned figure can still be exactly what its script writes."""
    prod = producers(here, svg_files)
    out, checked = {}, 0
    warned = 0
    tmp = tempfile.mkdtemp(prefix='pageguard_')
    try:
        work = os.path.join(tmp, 'files')
        shutil.copytree(here, work, ignore=shutil.ignore_patterns(
            'svg_*.txt', 'look_*.png', '*.html', '__pycache__', '.git'))
        env = dict(os.environ, PYTHONPATH=work, MPLBACKEND='Agg')
        for s in sorted({p for p in prod.values() if p}):
            r = subprocess.run([sys.executable, s], cwd=work, env=env,
                               capture_output=True, text=True, timeout=600)
            if r.returncode == 0:
                said = [l.strip() for l in r.stdout.splitlines() if l.strip().startswith('!')]
                said += ['(stderr) ' + l.strip() for l in r.stderr.splitlines() if l.strip()]
                for l in said:
                    print('  %s: %s' % (s, l))
                warned += len(said)
                WARNINGS.extend('%s: %s' % (s, l) for l in said)
            if r.returncode != 0:
                for f, p in prod.items():
                    if p == s:
                        out[f] = 'SCRIPT FAILED: %s exited %d: %s' % (
                            s, r.returncode, ((r.stderr or r.stdout).strip().splitlines()
                                              or ['(no output)'])[-1][:100])
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
    if warned:
        print('  !! the figure scripts printed %d warning line(s), above: read them' % warned)
    return out, checked


VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param',
        'source', 'track', 'wbr'}
# elements a browser will not keep inside a <p>
BLOCK = {'address', 'article', 'aside', 'blockquote', 'details', 'div', 'dl', 'fieldset',
         'figcaption', 'figure', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header',
         'hr', 'main', 'nav', 'ol', 'p', 'pre', 'section', 'table', 'ul',
         'li', 'dd', 'dt', 'summary', 'menu'}


def nesting(h):
    """Tags that do not nest, as a reader's browser would have to repair them.

    THE BUILDS' TAG CHECK COUNTS, IT DOES NOT NEST (review session 14, §18.3): it compares
    the number of openings with the number of closings, so "<em><b>x</em></b>" passes, and
    a self-closed "<b/>" - which HTML does not close, so everything after it is bold - is
    never counted at all. This walks the page with a stack. Returns a list of problems,
    empty when every element is closed, in order, by its own end tag. Self-closing is
    allowed on void elements and inside <svg>, where it is XML; a block element opened
    inside a <p> is reported too, since a browser ends the paragraph there and leaves the
    </p> closing nothing (review session 15; its checker found the first version allowed
    self-closing by tag name anywhere, and did not see a <div> inside a <p>)."""
    from html.parser import HTMLParser
    problems, stack = [], []

    def in_svg():
        return any(t == 'svg' for t, _ in stack)

    class P(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag in BLOCK and not in_svg() and any(t == 'p' for t, _ in stack):
                problems.append('<%s> at line %d inside a <p> (a browser ends the paragraph)'
                                % (tag, self.getpos()[0]))
            if tag not in VOID:
                stack.append((tag, self.getpos()[0]))

        def handle_startendtag(self, tag, attrs):
            if tag not in VOID and not in_svg() and tag != 'svg':
                problems.append('<%s/> at line %d (HTML does not self-close it)'
                                % (tag, self.getpos()[0]))

        def handle_endtag(self, tag):
            if tag in VOID:
                return
            if stack and stack[-1][0] == tag:
                stack.pop()
                return
            line = self.getpos()[0]
            if any(t == tag for t, _ in stack):
                while stack[-1][0] != tag:
                    t, l = stack.pop()
                    problems.append('<%s> (line %d) still open at </%s> (line %d)'
                                    % (t, l, tag, line))
                stack.pop()
            else:
                problems.append('</%s> at line %d closes nothing' % (tag, line))

    p = P(convert_charrefs=True)
    p.feed(h)
    p.close()
    problems += ['<%s> (line %d) never closed' % (t, l) for t, l in stack]
    return problems + duplicate_ids(h) + figure_widths(h) + text_fills(h)


def duplicate_ids(h):
    """An id given twice in one page. A browser resolves url(#x), href="#x" and every
    anchor to the FIRST element with that id, so the second is silently someone else's.

    Review session 18 found page 18 shipped with two <clipPath id="fr">: figs_17's Sound
    map (600 high) and its roads map (700 high) both took mapspine.detail_base()'s default
    clip id, and the roads map was clipped by the Sound's rectangle - its bottom hundred
    units, with Hamborg, Luebeck and the end of the ox road, were never drawn. Every guard
    passed: each figure file is fine alone, and nothing looked at two in one page. Found by
    measuring the page (what is painted over each text), not the files. Called from
    nesting(), so every part build refuses such a page."""
    import collections
    seen = collections.Counter(re.findall(r'(?<![\w-])id="([^"]+)"', h))
    return ['id="%s" given %d times in the page (url(#%s) and #%s reach only the first)'
            % (k, n, k, k) for k, n in sorted(seen.items()) if n > 1]


def _top_svgs(markup):
    """The <svg> elements not inside another <svg>, as (start, end) offsets."""
    out, depth, start = [], 0, 0
    for m in re.finditer(r'<(/?)svg\b[^>]*?(/?)>', markup, re.I):
        if m.group(1):
            depth = max(depth - 1, 0)
            if depth == 0:
                out.append((start, m.end()))
        elif m.group(2):
            if depth == 0:
                out.append((m.start(), m.end()))
        else:
            if depth == 0:
                start = m.start()
            depth += 1
    return out


def figure_widths(h):
    """A figure whose viewBox width has no phone line, or no scroll line, in the page's style.

    Below 1000 px on a screen a figure scrolls sideways in its box and its svg keeps 0.8 of its
    viewBox width (D-20), one style.css line per width, since CSS cannot read a number out of an
    attribute; and where it scrolls its caption opens with a line saying so, one query per width
    (review session 21). The plausible fault is a figure at a new width with neither: it would
    shrink to the screen again, or scroll unannounced, and nothing would say so. So every
    <figure> must open with one top-level <svg viewBox="0 0 W H">, W a multiple of 5; no <svg>
    may stand outside a figure; and the page's <style> must hold, as style.css writes them (runs
    of white space aside, either quote), the caption's hidden line
      figure figcaption::before{display:none;... content:"Wider ..."...}
    and for each W
      figure svg[viewBox^="0 0 W "]{min-width:Xpx}                        X = 0.8 W exactly
      figure:has(> svg[viewBox^="0 0 W "]) figcaption::before{display:block}
    the second inside `@media screen and (width < Tpx)` where its band gives one.

    THE BANDS, measured in the page (review session 21, checks 2 and 3): up to 720 px a figure's
    box is the viewport less 64 px, from 721 less 96 and at most 694 px, and an overflow under
    half a pixel does not scroll. So, W a multiple of 5 (0.8 W whole; at 778 or 823 the line
    showed a width before the figure scrolled): up to 780 wide a figure scrolls below
    T = 0.8 W + 64; from 825 to 865 below T = 0.8 W + 96; from 870 at every width under 1000 (its
    line goes in the phone block, and it needs the 900s' breakout too, or it draws under 0.8 from
    1000, which `ordercheck.py` lists at 1200); from 785 to 820 in two bands, below 0.8 W + 64 and
    from 721 to 0.8 W + 96, which no line here gives - refused, until it has both lines and this
    guard is taught them.

    A TRIPWIRE, NOT A PROOF. It finds the lines as style.css spells them and refuses any other
    spelling, however valid, rather than guess how CSS reads it (check 3: a space it had taken
    out made ":has(" of " :has(", which CSS reads otherwise); a line under another media or
    overridden later passes. Review session 20 had this guard read CSS as a browser does, some
    150 lines, and four checks each found a style the browser read otherwise; Carsten cut it back
    (review session 21). What the page draws is measured by `ordercheck.py`, at the width it runs
    (1200 and 390 in every cold run): any figure drawn under 0.8 of its viewBox, and any whose
    scroll line disagrees with its scrolling - that is the check of record. Called from
    nesting(), so every part build refuses such a page."""
    body = re.sub(r'<!--.*?-->|<(script|template)\b.*?</\1\s*>', '', h, flags=re.S | re.I)
    css = ' '.join(re.sub(r'/\*.*?\*/', '', c, flags=re.S)
                   for c in re.findall(r'<style\b[^>]*>(.*?)</style\s*>', body, re.S | re.I))
    css = re.sub(r'\s+', ' ', css).replace("'", '"')
    widths = {int(w): x for w, x in re.findall(
        r'figure svg\[viewBox\^="0 0 (\d+) "\]\{min-width:([\d.]+)px\}', css)}
    hint = lambda w: (r'figure:has\(> svg\[viewBox\^="0 0 %d "\]\) figcaption::before'
                      r'\{display:block\}' % w)
    figs = re.findall(r'<figure\b[^>]*>(.*?)</figure\s*>', body, re.S | re.I)
    problems, inside, seen = [], 0, set()
    if figs and not re.search(r'figure figcaption::before\{display:none;[^}]*content:"Wider ', css):
        problems.append('the style has no hidden scroll line '
                        '(figure figcaption::before{display:none;... content:"Wider ..."})')
    for n, fig in enumerate(figs, 1):
        svgs = _top_svgs(fig)
        inside += len(svgs)
        m = re.match(r'\s*<svg\b[^>]*?\sviewBox\s*=\s*["\']0 0 ([1-9]\d*) [\d.]+["\']', fig, re.I)
        if len(svgs) != 1 or not m:
            problems.append('figure %d does not hold one <svg viewBox="0 0 W H">, first' % n)
            continue
        w = int(m.group(1))
        if w % 5:
            problems.append('figure %d is %d wide, not a multiple of 5: where it scrolls is not '
                            'known to a whole pixel (D-20)' % (n, w))
            continue
        if widths.get(w) is None or float(widths[w]) != w * .8:
            problems.append('figure %d is %d wide and the style has no line '
                            'figure svg[viewBox^="0 0 %d "]{min-width:%gpx}' % (n, w, w, w * .8))
        if w in seen:
            continue
        seen.add(w)
        t = w * .8 + 64 if w <= 780 else w * .8 + 96
        line = 'figure:has(> svg[viewBox^="0 0 %d "]) figcaption::before{display:block}' % w
        if 780 < w <= 820:
            problems.append('figure %d is %d wide: it scrolls below %gpx and again from 721 to %gpx, '
                            'and figure_widths() knows no line for two bands' % (n, w, w * .8 + 64, t))
        elif w < 870 and not re.search(r'@media screen and \(width < %gpx\)\{%s\}' % (t, hint(w)), css):
            problems.append('figure %d is %d wide and the style has no scroll line for it: '
                            '@media screen and (width < %gpx){%s}' % (n, w, t, line))
        elif w >= 870 and not re.search(hint(w), css):
            problems.append('figure %d is %d wide and the phone block has no scroll line for it: %s'
                            % (n, w, line))
    if len(_top_svgs(body)) > inside:
        problems.append('%d <svg>(s) outside any <figure>: no phone line reaches them'
                        % (len(_top_svgs(body)) - inside))
    return problems


def text_fills(h):
    """A figure text's colour given by a fill= attribute (D-11).

    A stylesheet rule beats a presentation attribute, so on a <text> with a .mapt, .mapl or
    .mapx class a fill= is never drawn, and from an enclosing element it is never inherited by
    such a text. Review session 20 measured 449 texts drawing another colour than they asked;
    review session 21 deleted the 354 that remained (each drew its class colour) and moved the
    three that did draw into style=. A meant colour goes in style="fill:#XXXXXX". This refuses a
    fill= on any <text> or <tspan>, on any element with a map class, and on any element round a
    text outside the map class it has or takes from a <g>, up to the figure's svg and through a
    nested one - but for fill="none", which is meant for the shapes beside the text (review
    session 21, checks 2 and 3). A fill given in style= on an enclosing element is not read here:
    `ordercheck.py` lists it if the text does not draw it. It reads the page as HTML does (html.parser: tag and attribute names
    in any case, any quoting, a ">" inside an attribute; comments, <script> and <template> not
    read) - after check 1 of review session 21 passed a FILL=, a single-quoted class and an
    <a class="mapx" fill=...>. It reads markup, not the cascade: what the page draws is
    `ordercheck.py`'s colour measure. Called from nesting(), so every part build refuses it."""
    from html.parser import HTMLParser
    out, stack = [], []
    VOIDS = VOID | {'path', 'line', 'rect', 'circle', 'ellipse', 'polyline', 'polygon', 'use',
                    'stop', 'image'}
    mapped = lambda a: bool(re.search(r'\bmap[tlx]\b', a.get('class') or ''))

    class P(HTMLParser):
        skip = 0

        def handle_starttag(self, tag, attrs):
            if tag in ('script', 'template'):
                self.skip += 1
            if self.skip:
                return
            a = dict(attrs)
            line = self.getpos()[0]
            has = 'fill' in a
            if has and (tag in ('text', 'tspan') or mapped(a)):
                out.append('<%s> at line %d sets its colour with fill="%s" (D-11: style="fill:...")'
                           % (tag, line, a['fill']))
            elif tag == 'text':
                # up the stack to the figure's own svg, through any nested one (inheritance
                # crosses it): once a map class is met - on the text, or on a <g> round it
                # (check 3) - a fill= further out is never drawn on it; one nearer is. A
                # fill="none" is meant for the shapes beside the text (check 2)
                outer = next((k for k, (t, _, _, _) in enumerate(stack) if t == 'svg'), 0)
                classed = mapped(a)
                for t, l, f, c in reversed(stack[outer:]):
                    if classed and f is not None and f.strip().lower() != 'none':
                        out.append('<%s fill="%s"> at line %d is round a classed text (line %d): '
                                   'the class wins (D-11)' % (t, f, l, line))
                        break
                    classed = classed or c
            if tag not in VOIDS:
                stack.append((tag, line, a.get('fill'), mapped(a)))

        def handle_startendtag(self, tag, attrs):
            if self.skip:
                return
            a = dict(attrs)
            if 'fill' in a and (tag in ('text', 'tspan') or mapped(a)):
                out.append('<%s/> at line %d sets its colour with fill="%s" (D-11)'
                           % (tag, self.getpos()[0], a['fill']))

        def handle_endtag(self, tag):
            if tag in ('script', 'template'):
                self.skip = max(self.skip - 1, 0)
                return
            if self.skip:
                return
            if any(t == tag for t, _, _, _ in stack):
                while stack and stack.pop()[0] != tag:
                    pass

    p = P(convert_charrefs=True)
    p.feed(h)
    p.close()
    return out
