# -*- coding: utf-8 -*-
"""figcheck.py - does every shipped figure still match the script that draws it?

    python3 figcheck.py                # check every built page
    python3 figcheck.py 27 28          # just those chapters
    python3 figcheck.py --regen        # re-run the generators first, then check

WHY THIS EXISTS.

`debuild.py verify` catches an ARTIFACT-ONLY edit: a correction made to a built
page and never carried back to its body, which the next build silently destroys.
It does not catch the same fault running the other way.

In September 2026 `figs_27.py` was found to contain a corrected schools figure -
240 in the twelve districts plus one on Bogoe by royal resolution of 11 June
1727, making 241 - while chapter 27's shipped page still carried the superseded
version, with a thirteenth district on Moen and arithmetic that came to 250 or
251. The generator had been fixed and never re-run. `debuild.py verify` reported
chapter 27 `identical` throughout, because the page round-tripped perfectly
against its own body; the body holds `{{SVG_SCHOOLS}}`, a placeholder, and a
placeholder cannot disagree with anything.

So there was no verifier anywhere in the toolchain comparing what a figure
script draws today against what is actually inlined in the page a reader sees.
This is that verifier.

WHAT IT REPORTS

    identical   the inline SVG matches the .txt on disk
    STALE       they differ - the page predates a change to the figure
    MISSING     the page wants a figure whose .txt is not on disk
    unmatched   an inline SVG that matches no .txt (Part D's lost figures)

`--regen` re-runs every `figs_*.py` first, so a generator edited but never run is
caught too. Without it, the check compares against the .txt files as they stand,
which is what the build would actually inline.

NOTE ON WHAT THIS CANNOT SEE. Parts A-D have no retained bodies and ten of their
figures have no generator at all. Those inline SVGs report `unmatched` and that
is correct, not a fault: there is nothing on disk to compare them to and never
will be. The count of them is printed so a change in it is visible.
"""
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.environ.get('DK_CHAPTERS', os.path.dirname(HERE))

SVG = re.compile(r'<svg\b.*?</svg>', re.S)


def norm(s):
    """Whitespace-insensitive comparison.

    The build reindents an inlined SVG, so a byte comparison would report every
    figure in the book as stale. Collapsing runs of whitespace compares what the
    figure draws rather than how the builder laid it out.
    """
    return re.sub(r'\s+', ' ', s).strip()


ARIA = re.compile(r'aria-label="([^"]*)"')


def aria(svg):
    m = ARIA.search(svg)
    return m.group(1).strip() if m else None


def load_txts():
    out = {}
    for p in sorted(glob.glob(os.path.join(HERE, 'svg_*.txt'))):
        out[os.path.basename(p)] = norm(open(p, encoding='utf-8').read())
    return out


def load_labels(txts):
    """aria-label -> filename, for the .txt files on disk.

    A figure is identified by what it says it is. Two .txt files sharing a
    label would make this ambiguous, so that is reported rather than resolved.
    """
    out, dupes = {}, []
    for k, v in txts.items():
        lab = aria(v)
        if not lab:
            continue
        if lab in out:
            dupes.append((out[lab], k))
        out[lab] = k
    for a, b in dupes:
        print('!! %s and %s share an aria-label; figcheck cannot tell them apart'
              % (a, b))
    return out


def regen():
    """Re-run every figure generator, so a stale .txt is caught as well."""
    scripts = sorted(glob.glob(os.path.join(HERE, 'figs_*.py')))
    print('regenerating from %d scripts' % len(scripts))
    for s in scripts:
        r = subprocess.run([sys.executable, os.path.basename(s)],
                           cwd=HERE, capture_output=True, text=True)
        if r.returncode != 0:
            print('  !! %s exited %d' % (os.path.basename(s), r.returncode))
            print('     ' + (r.stderr or r.stdout).strip().splitlines()[-1][:100])
        else:
            print('  ok  %s' % os.path.basename(s))
    print()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if '--regen' in sys.argv:
        regen()

    txts = load_txts()
    labels = load_labels(txts)
    wanted = {a.zfill(2) for a in args if a.isdigit()}

    pages = sorted(glob.glob(os.path.join(PAGES, '[0-9][0-9]-*.html')))
    if wanted:
        pages = [p for p in pages if os.path.basename(p)[:2] in wanted]
    if not pages:
        print('no pages found in %s' % PAGES)
        return 1

    stale, missing, unmatched, same = [], [], 0, 0
    print('%-52s %-11s %s' % ('page', 'figure', 'verdict'))
    print('-' * 84)

    for path in pages:
        name = os.path.basename(path)
        html = open(path, encoding='utf-8').read()
        for inline in SVG.findall(html):
            n = norm(inline)
            hit = next((k for k, v in txts.items() if v == n), None)
            if hit:
                same += 1
                continue
            # No exact match. Two very different cases, and the first version of
            # this script conflated them and cried STALE forty-two times.
            #
            # Identify the figure by its ARIA-LABEL, not by guessing at
            # filenames. The label is the figure's identity: it survives a
            # change to the drawing and it is unique per figure. If some .txt
            # shares this label, the figure has a source and the two disagree -
            # that is real staleness. If no .txt claims the label, the figure
            # has no source on disk and never will.
            #
            # That is the whole of Parts A-C, whose build script references no
            # .txt files at all, plus Part D's ten lost generators. Thirty-one
            # figures live only inside their shipped pages. Reporting those as
            # STALE would bury the one line that matters.
            lab = aria(inline)
            shown = (lab[:44] + '...') if lab else '(no aria-label)'
            owner = labels.get(lab) if lab else None
            if owner:
                print('%-52s %-11s %s' % (name[:52], 'STALE', shown))
                stale.append((name, owner, shown))
            else:
                unmatched += 1

    for path in pages:
        html = open(path, encoding='utf-8').read()
        for m in re.finditer(r'\{\{SVG_([A-Z0-9_]+)\}\}', html):
            f = 'svg_%s.txt' % m.group(1).lower()
            if f not in txts:
                missing.append((os.path.basename(path), f))

    print('-' * 84)
    print('%d figures match their source' % same)
    if unmatched:
        print('%d inline figures have no source on disk '
              '(Parts A-D: expected, not a fault)' % unmatched)
    if missing:
        for n, f in missing:
            print('MISSING  %s wants %s' % (n, f))
    if stale:
        print()
        for n, owner, lab in stale:
            print('STALE    %s  <-  %s' % (n, owner))
        print('\n!! %d figure(s) STALE - the page disagrees with the generator.'
              % len(stale))
        print('   Rebuild the part, then linkindex.py, then index_generator.py.')
        return 1
    print('\nno figure on any page disagrees with its source')
    return 0


if __name__ == '__main__':
    sys.exit(main())
