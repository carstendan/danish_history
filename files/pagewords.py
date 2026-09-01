# -*- coding: utf-8 -*-
"""Reading-time word count, shared by every build_part_*.py and by bookstats.py.

The counter this replaces was one line:

    w = len(re.sub(r'<[^>]+>', ' ', h.split('</style>')[1]).split())

It strips tags but keeps everything between them, so SVG <text> and <tspan> labels
were counted as prose, and .split() made a word of every free-standing em-dash and
middot. Measured on the built Part G pages it put each chapter about three minutes
over: chapter 28 read as 46 and is 43.

Figure labels are read at a glance and not in sequence, so they are not reading
time. Punctuation is not a word.

WHY IT IS A MODULE. The expression it replaces had been copied into all six build
scripts and bookstats.py — seven copies of one rule. The units-per-character
constant in the figure scripts was duplicated the same way and drifted from 5.55 to
6.1 in six of seven copies without anyone noticing.
"""
import re

WORDISH = re.compile(r'[0-9A-Za-z\u00c0-\u024f]')

WPM = 210


def _body(h):
    return re.sub(r'<svg\b.*?</svg>', ' ', h.split('</style>')[1], flags=re.S | re.I)


def pagewords(h):
    """Prose words on a built page: no markup, no SVG label text, no bare punctuation."""
    return len([t for t in re.sub(r'<[^>]+>', ' ', _body(h)).split() if WORDISH.search(t)])


def textwords(h):
    """pagewords minus the navigation furniture: rail, contents list, script.

    The rail and the contents list are the same list rendered twice, so `page`
    counts every section title three times over — once as a heading and twice as
    navigation. About 215 words a page. See open item 14 in HANDOFF.md.
    """
    t = _body(h)
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S)
    t = re.sub(r'<nav class="rail".*?</nav>', ' ', t, flags=re.S)
    t = re.sub(r'<details class="toc">.*?</details>', ' ', t, flags=re.S)
    return len([x for x in re.sub(r'<[^>]+>', ' ', t).split() if WORDISH.search(x)])


def minutes(w):
    return round(w / float(WPM))
