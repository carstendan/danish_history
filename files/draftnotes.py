#!/usr/bin/env python3
"""Drafting notes must not ship. One pattern, used by mkbody.py and runnable
over the shipped pages.

Item 99 added a guard to mkbody.py that matched the literal string `*Flag:`.
It was case-sensitive and anchored on the asterisk, so `*Drafting flag:` --
the wording chapter 32 uses four times -- passed it, and chapter 32 would have
rebuilt with all four on the page. A sweep of the 38 built pages at the start
of the chapter 39 session found author-directed notes on eight pages outside
chapter 38 (HANDOFF item 102): a whole draft-file header inside chapter 25's
section 03, 'Style note:' citing decision D-6 in chapter 27, 'needs checking
before this section ships' twice in chapter 31, and 'Attributions need
checking ... before publication' in the Sources of every Part G chapter.

The pattern is matched on WHITESPACE-NORMALISED text (item 69): a note wrapped
across a line break in the markdown is otherwise invisible to it, and one of
chapter 32's four was.

It is a wording list, and a wording list is only as good as the wordings
someone has already seen. The page scan therefore also reports every italic
span of LONG_ITALIC words or more, which is how the notes in this entry were
found: drafts render *...* as <i class="dk">, and a genuine Danish term or
title is rarely that long. That half is advisory -- titles and quotations
legitimately exceed it -- and is printed, not failed.

    python3 draftnotes.py ../[0-9][0-9]-*.html      pages: exit 1 on any match
    python3 draftnotes.py c39_draft.md               drafts: the same pattern
"""
import html
import re
import sys

PATTERN = re.compile(
    r"(?:\b(?:drafting\s+)?flag\s*:"
    r"|\bplacement\s+note\s*:"
    r"|\bstyle\s+note\s*:"
    r"|\bbefore\s+publication\b"
    r"|\bbefore\s+this\s+(?:section\s+)?(?:ships|goes\s+in)\b"
    r"|\bneeds?\s+(?:checking|settling|verifying)\b"
    r"|\bshould\s+be\s+(?:checked|verified)\b"
    r"|\bstill\s+to\s+be\s+(?:obtained|confirmed|checked|verified)\b"
    r"|<!--\s*=+\s*c\d\d_draft"
    r"|\bTODO\b|\bTBD\b|\bFIXME\b)",
    re.I)

LONG_ITALIC = 8
SAME_NOTE = 120


def normalise(text):
    return re.sub(r"\s+", " ", text)


# ONE BLOCK IS EXEMPT, AND ONLY ONE. The Sources apparatus ends with "Where the
# argument stands", and in Part G and H it opens with a caveat to the reader -
# "Attributions below need checking against the works themselves before
# publication; they are set down here as the shape of the debate, not as reading
# claimed." That sentence is true, it is addressed to the reader rather than the
# author, and it sits exactly where mkbody's own refusal tells an author to put
# an unresolved question ("move it to the Sources block as a question addressed
# to the reader"). The pattern refused it anyway, in all seven Part G chapters,
# and a guard that refuses the disposition it recommends leaves no way through
# but rewording true sentences until they stop matching.
#
# Decided 18-19 September 2026: that block is not scanned. It runs from the
# words "Where the argument stands" to the end of the Sources block - a `---`
# rule or a `#`/`##` heading in a draft, the next <h2> on a built page. The cost
# is known and accepted: a genuine note parked inside that block will pass. Every
# other block, including the rest of Sources, is scanned exactly as before.
EXEMPT = re.compile(
    r"Where the argument stands.*?(?=^[ \t]*---[ \t]*$|^#{1,2} |<h2\b|\Z)",
    re.S | re.M)


def find(text, width=70):
    """Return (match, following context) for every drafting note in text."""
    flat = normalise(EXEMPT.sub(" ", text))
    out, last = [], -10 ** 9
    for m in PATTERN.finditer(flat):
        # one note often trips two wordings ("need checking ... before
        # publication"); count a note once, not once per phrase in it
        if m.start() - last > SAME_NOTE:
            out.append((m.group(0), flat[m.end():m.end() + width]))
        last = m.end()
    return out


def page_text(raw):
    body = raw[raw.find("<body"):]
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    return html.unescape(body)


def long_italics(raw):
    spans = re.findall(r'<i class="dk">(.*?)</i>', raw, re.S)
    out = []
    for s in spans:
        plain = normalise(html.unescape(re.sub(r"<[^>]+>", "", s))).strip()
        if len(plain.split()) >= LONG_ITALIC:
            out.append(plain)
    return out


def main(paths):
    bad = 0
    for p in paths:
        raw = open(p, encoding="utf-8").read()
        is_page = p.endswith(".html")
        hits = find(page_text(raw) if is_page else raw)
        name = p.rsplit("/", 1)[-1][:48]
        if hits:
            bad += len(hits)
            print("%-48s %d drafting note(s)" % (name, len(hits)))
            for m, ctx in hits:
                print("    %s%s" % (m, ctx))
        if is_page:
            for s in long_italics(raw):
                if not PATTERN.search(s):
                    print("    advisory, long italic: %s" % s[:90])
    print("-" * 70)
    print("%d drafting note(s) in %d file(s)" % (bad, len(paths)) if bad
          else "no drafting notes in %d file(s)" % len(paths))
    return 1 if bad else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
