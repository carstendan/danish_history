# -*- coding: utf-8 -*-
"""pagecount.py — one definition of "how many words is this page".

WHY THIS IS A MODULE AND NOT A LINE IN EACH BUILD SCRIPT. The expression it
replaces was copied into build_parts_abc.py, build_part_d.py, build_part_e.py,
build_part_f.py, build_part_g.py, build_all.py and bookstats.py — seven copies of
one rule. The units-per-character constant in the figure scripts was duplicated the
same way and drifted from 5.55 to 6.1 in six of seven copies without anyone
noticing, which is exactly the failure this avoids.

WHAT WAS WRONG. The old expression stripped tags and counted what was left:

    len(re.sub(r'<[^>]+>', ' ', h.split('</style>')[1]).split())

Stripping tags leaves the text INSIDE <svg> — every axis label, every timeline
date, every figure's own caption lines — and .split() counts a free-standing em
dash or middot as a word. Both were counted as prose; neither is read as prose.
Measured across Part G: 3,589 words over seven pages, mean 512, about 2.4 minutes
each. Chapter 28 read as a 46-minute split candidate and is 43.

WHAT THIS DOES NOT DO. It still counts the rail, the contents list and the inlined
rail.js, because that is what `page` has always meant and what the band is measured
against. bookstats.py's `text` measure is the one that strips navigation. The gap
between them is about 215 words a page and is a separate question — see open item
14 in HANDOFF.md.
"""
import re

# Free-standing punctuation that .split() returns as tokens. Not an exhaustive
# list of dashes: only the ones the series actually uses as separators.
SEPARATORS = {'\u2014', '\u2013', '\u00b7', '-', '\u2192', '\u2190'}

WPM = 210


def body_after_style(h):
    """Everything after the closing </style>, which is what all the callers meant.

    split('</style>')[1] and split('</style>', 1)[-1] agree while a page carries
    exactly one style block, which every page in the series does. This uses the
    second form so a second style block could not silently change the answer.
    """
    return h.split('</style>', 1)[-1]


def pagewords(h):
    """Prose words on a built page: no markup, no SVG label text, no bare dashes."""
    body = re.sub(r'<svg.*?</svg>', ' ', body_after_style(h), flags=re.S)
    return len([w for w in re.sub(r'<[^>]+>', ' ', body).split()
                if w not in SEPARATORS])


def textwords(h):
    """pagewords minus the navigation furniture: rail, contents list, script.

    The rail and the contents list are the same list rendered twice, so `page`
    counts every section title three times over — once as a heading and twice as
    navigation.
    """
    t = re.sub(r'<svg.*?</svg>', ' ', body_after_style(h), flags=re.S)
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S)
    t = re.sub(r'<nav class="rail".*?</nav>', ' ', t, flags=re.S)
    t = re.sub(r'<details class="toc">.*?</details>', ' ', t, flags=re.S)
    return len([w for w in re.sub(r'<[^>]+>', ' ', t).split()
                if w not in SEPARATORS])


def minutes(w):
    return round(w / float(WPM))
