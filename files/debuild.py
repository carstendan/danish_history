# -*- coding: utf-8 -*-
"""Recover the source body of a built chapter, and prove the recovery is lossless.

A built page is a superset of its body: the build only ever injects into four
placeholders. Reversing it is four substitutions. Verified byte-identical on
chapter 11.

Usage:
    python3 debuild.py verify  /path/to/*.html     # round-trip every file, change nothing
    python3 debuild.py extract /path/to/*.html     # write cNN_body.html + print the SEC config

Deliberate choice: SVGs stay INLINE in the recovered bodies. Chapters 12-15
externalise them to svg_*.txt because a Python script generates each one; for
1-11 those generator scripts are gone, so a placeholder would point at a file
that can never be regenerated.
"""
import re
import sys
import glob
import os

STYLE = 'style.css'
RAIL = 'rail.js'


def debuild(html):
    """Built page -> source body."""
    h = re.sub(r'<style>.*?</style>', '<style>{{STYLE}}</style>', html, flags=re.S)
    h = re.sub(r'<script>.*?</script>', '{{JS}}', h, flags=re.S)
    h = re.sub(r'<nav class="rail".*?</nav>', '{{RAIL}}', h, flags=re.S)
    h = re.sub(r'<details class="toc">.*?</details>', '{{TOC}}', h, flags=re.S)
    return h


def sections(html):
    """Read the section list back off the page's own rail.

    build_all.py holds SEC for chapters 2-11 only, and chapter 1 never had one.
    Deriving it from the artifact means the recovery does not depend on that file
    at all.
    """
    nav = re.search(r'<nav class="rail".*?</nav>', html, re.S)
    if not nav:
        raise SystemExit('!! no rail found - was this page built by the current pipeline?')
    out = []
    for sid, num, lab in re.findall(
            r'<li><a href="#([a-z0-9]+)"><span class="rn">(\d*)</span>(.*?)</a></li>', nav.group(0)):
        out.append((sid, num, lab))
    return out


TAIL_IDS = {'myth', 'forward', 'summary', 'questions', 'sources', 'visit'}


BAND_SRC = '--band:#96591A;'


def part_colour(html):
    """The part colour the page was built with, or None.

    From Part D onward the build rewrites --band in style.css to the part's own
    colour, and Part G also injects an --indigo token. debuild.py was verified on
    chapter 11 and never taught about either, so every page from D to G reported
    DIFFERS on the style block alone. That made the tool useless exactly where it
    was needed: four artifact-only corrections went unnoticed in Part G because
    nothing was round-tripping these pages.
    """
    m = re.search(r'--band:(#[0-9A-Fa-f]{6});', html)
    return m.group(1) if m else None


def rebuild(body, sec, band=None, extra_tokens=''):
    rail = ['<nav class="rail" aria-label="Sections of this page">'
            '<p class="rail-h">On this page</p><ol>']
    toc = ['<details class="toc"><summary>Contents</summary><ol>']
    for sid, num, lab in sec:
        rail.append('<li><a href="#%s"><span class="rn">%s</span>%s</a></li>' % (sid, num, lab))
        toc.append('<li><a href="#%s">%s</a></li>' % (sid, lab))
    rail.append('</ol></nav>')
    toc.append('</ol></details>')
    style = open(STYLE, encoding='utf-8').read()
    if band and band != BAND_SRC[7:-1]:
        style = style.replace(BAND_SRC, extra_tokens + '--band:%s;' % band)
    h = body.replace('{{STYLE}}', style)
    h = h.replace('{{RAIL}}', "\n".join(rail)).replace('{{TOC}}', "\n".join(toc))
    h = h.replace('{{JS}}', '<script>' + open(RAIL, encoding='utf-8').read() + '</script>')
    return h



def _normalise(h):
    """Strip what build() injects into the body beyond the four placeholders.

    The build also inserts checkpoint blocks and rewrites the reading-time line,
    so a body recovered from a page never matches the retained source raw. Both
    are removed from both sides before comparing, leaving the prose, which is the
    thing an artifact-only edit would change.
    """
    h = re.sub(r'<div class="check">.*?</div>\n\n', '', h, flags=re.S)
    h = re.sub(r'Era chapter \u00b7 about \d+ minutes',
               'Era chapter \u00b7 about N minutes', h)
    # Figures are the fifth injection. debuild() leaves them inline on purpose;
    # a retained body holds {{SVG_NAME}}. Reduce both to one marker so the
    # comparison is about prose, which is what an artifact-only edit changes.
    h = re.sub(r'<svg\b.*?</svg>', '{{FIG}}', h, flags=re.S)
    h = re.sub(r'\{\{SVG_[A-Z0-9_]+\}\}', '{{FIG}}', h)
    return h.strip()


def report(path):
    orig = open(path, encoding='utf-8').read()
    body = debuild(orig)
    sec = sections(orig)
    band = part_colour(orig)
    # Part G injects --indigo alongside the rewritten --band.
    extra = ''
    m = re.search(r'(--indigo:#[0-9A-Fa-f]{6}; )', orig)
    if m and m.group(1) not in open(STYLE, encoding='utf-8').read():
        extra = m.group(1)
    # And the reverse case, which adding --indigo to style.css created: a page
    # shipped BEFORE the token existed reconstructs with a token it never had.
    # That is every page in Parts A-F, so the tool went from useless on D-G to
    # useless on A-F the moment Part G's colour was added to the stylesheet.
    drop = [m.group(1) for m in re.finditer(r'(--[a-z]+:#[0-9A-Fa-f]{6}; )',
                                            open(STYLE, encoding='utf-8').read())
            if m.group(1) not in orig]
    back = rebuild(body, sec, band, extra)
    for tok in drop:
        back = back.replace(tok, '', 1)
    ok = back == orig
    # chapters 1-11 ship a raw ampersand in the rail; the current build emits &amp;
    amp = (not ok) and back.replace('&amp; discussion', '& discussion') == orig

    # WHERE the difference is, which is the whole question. A page built against an
    # older style.css differs on the style block and nowhere else, and that is not
    # damage: it means the page predates a stylesheet change and cannot be rebuilt
    # without one. A difference in the BODY is the serious case - something in the
    # page that its source does not contain. Reporting both as "DIFFERS" made the
    # tool useless on chapters 01-11, which have no retained bodies and so can
    # never match the current stylesheet.
    kind = 'identical' if ok else ('amp-only' if amp else 'DIFFERS')
    note = ''
    if not (ok or amp):
        cut = lambda t: (t.split('</style>', 1) + [''])[:2]
        o_style, o_body = cut(orig)
        b_style, b_body = cut(back)
        if o_body == b_body:
            kind, note = 'style-only', '  stylesheet differs; body is intact'
        else:
            note = '  <-- inspect'

    # THE CHECK THAT ACTUALLY CATCHES AN ARTIFACT-ONLY EDIT.
    #
    # verify alone cannot. debuild() derives the body FROM the page, so a prose
    # edit made directly to a built page is present on both sides of the
    # comparison and round-trips perfectly. verify only proves that the four
    # injected regions - style, rail, toc, script - are reversible.
    #
    # The edit shows up only against the RETAINED body, which is the source the
    # next build will use. If they disagree, the page contains something the
    # rebuild will silently discard. That is exactly how four corrections went
    # unnoticed in Part G.
    kept = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'c%02d_body.html' % int(re.match(r'(\d+)', os.path.basename(path)).group(1))) \
        if re.match(r'\d\d', os.path.basename(path)) else None
    drift = None
    if kept and os.path.exists(kept):
        drift = _normalise(open(kept, encoding='utf-8').read()) != _normalise(body)

    if drift:
        kind = 'BODY DRIFT'
        note = '  <-- page disagrees with its retained body; a rebuild would lose this'
    elif drift is False and kind == 'style-only':
        note = '  stylesheet differs; body matches the retained source'

    name = os.path.basename(path)
    print("%-52s %-12s sections %2d  svg %d %s"
          % (name[:52], kind, len(sec), body.count('<svg'), note))
    return body, sec, (not drift) and (ok or amp or kind == 'style-only')


def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    mode, files = sys.argv[1], []
    for pat in sys.argv[2:]:
        files.extend(sorted(glob.glob(pat)))
    if not files:
        raise SystemExit('!! no files matched')
    allok = True
    for f in files:
        body, sec, ok = report(f)
        allok &= ok
        if mode == 'extract':
            n = int(re.match(r'(\d+)', os.path.basename(f)).group(1))
            open('c%02d_body.html' % n, 'w', encoding='utf-8').write(body)
            print("    sec=%r" % (sec,))
    print("\n%s" % ("all files round-trip cleanly - safe to start editing"
                    if allok else "!! at least one file did not round-trip; do not edit yet"))


if __name__ == '__main__':
    main()
