# -*- coding: utf-8 -*-
"""reviewlib.py - read the built pages for the consistency sweeps.

The four sweeps of the consistency review (glossary, names, dates-and-figures,
arrows) all read the BUILT pages, not the drafts, because the pages are what a
reader gets and chapters 01-24 have no drafts in the repository. This module is
the one place that knows the page anatomy, so the sweeps do not each carry their
own copy of it (pagewords.py's reason, and the same one).

WHAT IT RETURNS, positively selected (L15): a page is split at its numbered
<h2 id="sNN"> headings. Within the chapter it finds

  terms      every <div class="t"><dt>..</dt><dd>..</dd></div>, with the section
  calls      every <li><b>ARROW</b><span>..</span></li> inside <ul class="calls">
  vignettes  every <div class="vig"> with its <h4>
  prose      the text of each section with the glossary, vignettes, figures,
             Meanwhile boxes and SVG REMOVED, i.e. the narrative a reader reads
  alltext    the page's reading text: everything after </style>, minus SVG,
             script, nav and the contents list

Chapter numbers, file names and the part map come from the repository and from
bookstats.PARTS - nothing is typed here.

Standard library only: this runs on the author's machine as well.
"""
import glob
import html
import os
import re

import bookstats

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_HERE)
PARTS = bookstats.PARTS


def part_of(n):
    for name, a, b in PARTS:
        if a <= n <= b:
            return name
    return None


def part_range(letter):
    for name, a, b in PARTS:
        if name == letter:
            return a, b
    return None


def next_part(letter):
    names = [p[0] for p in PARTS]
    i = names.index(letter)
    return names[i + 1] if i + 1 < len(names) else None


def page_files():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "[0-9][0-9]-*.html"))):
        out.append((int(os.path.basename(f)[:2]), f))
    return out


TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")


def text(fragment):
    """Visible text of an HTML fragment, entities decoded, whitespace folded."""
    t = TAG.sub(" ", fragment)
    t = html.unescape(t)
    t = WS.sub(" ", t).strip()
    # a space the tag strip left before punctuation
    return re.sub(r" ([,.;:!?)’])", r"\1", t)


def _strip_blocks(h, patterns):
    for p in patterns:
        h = re.sub(p, " ", h, flags=re.S | re.I)
    return h


NON_NARRATIVE = [
    r"<svg\b.*?</svg>",
    r"<script\b.*?</script>",
    r'<div class="terms">.*?</dl>\s*</div>',
    r'<div class="vig">.*?</div>',
    r'<figure\b.*?</figure>',
    r'<aside\b.*?</aside>',
    r'<div class="meanwhile">.*?</div>',
    r'<div class="check">.*?</div>',
    r'<div class="myth"[^>]*>.*?</dl>\s*</div>',
]


class Page:
    def __init__(self, n, path):
        self.n = n
        self.path = path
        self.name = os.path.basename(path)
        with open(path, encoding="utf-8") as fh:
            self.html = fh.read()
        body = self.html.split("</style>", 1)[-1]
        self.body = body
        m = re.search(r"<h1>(.*?)</h1>", body, re.S)
        self.title = text(m.group(1)) if m else ""
        self._sections = None

    # -- structure --------------------------------------------------------
    def sections(self):
        """[(sid, heading, html)] for every <h2 id=..>: intro, sNN and the terminal units."""
        if self._sections is not None:
            return self._sections
        b = self.body
        heads = list(re.finditer(r'<h2 id="([a-z0-9]+)"[^>]*>(.*?)</h2>', b, re.S))
        out = []
        for i, m in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(b)
            head = text(re.sub(r'<span class="n">.*?</span>', " ", m.group(2)))
            out.append((m.group(1), head, b[m.end():end]))
        self._sections = out
        return out

    def section_of(self, pos):
        best = "front"
        for m in re.finditer(r'<h2 id="([a-z0-9]+)"', self.body):
            if m.start() <= pos:
                best = m.group(1)
        return best

    # -- blocks -----------------------------------------------------------
    def terms(self):
        out = []
        for m in re.finditer(r'<div class="t">\s*<dt>(.*?)</dt>\s*<dd>(.*?)</dd>\s*</div>',
                             self.body, re.S):
            out.append({"term": text(m.group(1)), "dd": text(m.group(2)),
                        "dd_html": m.group(2), "sid": self.section_of(m.start())})
        return out

    def calls(self):
        m = re.search(r'<ul class="calls">(.*?)</ul>', self.body, re.S)
        if not m:
            return None
        out = []
        for li in re.finditer(r"<li>\s*<b>(.*?)</b>\s*<span>(.*?)</span>\s*</li>", m.group(1), re.S):
            out.append({"arrow": text(li.group(1)), "text": text(li.group(2)),
                        "html": li.group(2)})
        return out

    def vignettes(self):
        out = []
        for m in re.finditer(r'<div class="vig">\s*<h4>(.*?)</h4>(.*?)</div>', self.body, re.S):
            out.append({"head": text(m.group(1)), "text": text(m.group(2)),
                        "sid": self.section_of(m.start())})
        return out

    def prose(self):
        """[(sid, heading, narrative text)] - section text minus apparatus."""
        out = []
        for sid, head, h in self.sections():
            if sid == "intro" or re.fullmatch(r"s\d+", sid):
                out.append((sid, head, text(_strip_blocks(h, NON_NARRATIVE))))
        return out

    def alltext(self):
        b = _strip_blocks(self.body, [r"<svg\b.*?</svg>", r"<script\b.*?</script>",
                                      r'<nav\b.*?</nav>', r'<details class="toc">.*?</details>'])
        return text(b)

    def blocks_text(self):
        """[(label, sid, text)] for every reader-facing unit, apparatus included.

        The dates-and-figures and names sweeps want everything a reader reads,
        each piece labelled with where it sits."""
        out = []
        hdr = re.search(r"<header\b.*?</header>", self.body, re.S)
        if hdr:
            out.append(("header", "front", text(hdr.group(0))))
        for sid, head, h in self.sections():
            out.append(("section", sid, head + ". " + text(_strip_blocks(h, [r"<svg\b.*?</svg>",
                                                                        r"<script\b.*?</script>"]))))
        return out


def load():
    return [Page(n, p) for n, p in page_files()]


SENT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÀ-Þ\"“(])")


def sentences(t):
    return [s.strip() for s in SENT.split(t) if s.strip()]
