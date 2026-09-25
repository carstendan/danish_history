# -*- coding: utf-8 -*-
"""freshcheck.py - is the built body on disk what the draft would build?

WHY THIS EXISTS. On 18 September 2026 the repository passed the entire verifier
suite - `debuild.py verify` clean, `figcheck.py` 81/41/0, `seamcheck.py` passing,
`draftnotes.py` finding nothing - while shipping a date in chapter 41 that the
draft had corrected two commits earlier, and while chapter 43 existed as a draft
with no page at all. Nothing noticed, and nothing could have:

  - `debuild.py verify` round-trips a PAGE against its own BODY. Both were stale
    together, so the round trip agreed with itself. This is item 110's trap: a
    comparison of a thing with itself always passes.
  - `figcheck.py` compares a page's figures against the SVG sources on disk. The
    figures were fine. The prose was wrong.
  - `bookstats.py` counted 42 of 44 and read as "43 is not written yet" when the
    truth was "43 is written and was never built".

  The cause is structural and will recur: this project hands over PATCHES OF
  SOURCE ONLY, by standing rule, but the repository TRACKS the build outputs. So
  every source-only patch leaves the tree internally inconsistent until somebody
  remembers to rebuild, and until now nothing in the suite could tell the
  difference between "not written" and "written, not built".

WHAT IT DOES. For every chapter with a single-file draft and an entry in
`mkbody.HAND`, it rebuilds the body from the draft into a scratch directory and
compares it byte-for-byte with the body committed on disk. It reports three
states, and only two of them are acceptable:

  FRESH    the committed body is exactly what the draft builds
  STALE    the draft has moved and the body has not - THE FAULT
  MISSING  the draft exists and no body does - THE OTHER FAULT
  REFUSED  mkbody will not build this draft at all, so the page on disk can no
           longer be reproduced from its source. Chapter 32 is in this state and
           has been since the drafting-flag guard was wired in (item 102): its
           five unresolved flags were not in the guard's pattern when its page
           was built, and are now. Reported separately from STALE because the
           remedy is different - resolve the flags, not press rebuild.

It also checks that every chapter with a body has a PAGE, because a body with no
page is the same fault one stage later.

HOW IT FAILS. Exit 1 on STALE, MISSING or NO PAGE — the faults a rebuild fixes.
This is meant to run before a commit and before a handover, and to refuse.

REFUSED IS DELIBERATELY NOT FATAL, and the reason matters. Chapter 32 has been
REFUSED since item 102 wired the drafting-flag guard, and it stays REFUSED until
five open research questions are answered. A rebuild cannot clear it. If that set
the exit code, the pre-commit hook would refuse every commit in the repository,
`--no-verify` would become reflex within a day, and the guard would be dead — so
a standing condition nobody can act on today would have disabled the check for
the faults people CAN act on. REFUSED is printed loudly on every run instead.

WHAT IT DELIBERATELY DOES NOT DO. It does not rebuild pages, because
`build_part_*.py` injects checkpoints from its own config and a page comparison
would fail for reasons that are not staleness. Body-level is where the draft's
prose lives, and prose drift is the fault being hunted.

Chapters 25-31 are built from PART_G_DRAFT.md, and are checked against it since
review session 9 (the per-chapter fragment files beside it are not read by any
build). Chapters 1-24 predate the draft convention entirely and are SKIPPED and
NAMED, because a checker that silently covers less than it appears to is worse
than no checker (item 64). `check(n)` is also called by build_part_g.py before it
builds each page.

USAGE
    python3 files/freshcheck.py            # from the repository root
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import mkbody  # noqa: E402  - for HAND only


def page_for(n, name_hint):
    """The shipped page for chapter n, by its numeric prefix."""
    pre = "%02d-" % n
    hits = [f for f in os.listdir(ROOT) if f.startswith(pre) and f.endswith(".html")]
    return hits[0] if len(hits) == 1 else None


def draft_for(n):
    """The draft chapter n is built from, or None.

    Chapters 25-31 are built from PART_G_DRAFT.md (mkbody's default draft) and were
    skipped here until review session 9, when the part's own build learned to ask this
    question before every page (REVIEW-CONSISTENCY section 13.6): a page could be built
    from a body its draft no longer produced, because mkbody refused and nothing
    downstream noticed."""
    # PART_G_DRAFT.md FIRST for 25-31, because it is what mkbody builds them from (its
    # default draft). A stray c27_draft.md used to win here and become the witness while
    # the page was built from PART_G_DRAFT.md - the second checker of session 9 made one
    # and every check passed while an edit never reached the page.
    if 25 <= n <= 31 and os.path.exists(os.path.join(HERE, "PART_G_DRAFT.md")):
        return os.path.join(HERE, "PART_G_DRAFT.md")
    single = os.path.join(HERE, "c%d_draft.md" % n)
    if os.path.exists(single):
        return single
    return None


def check(n):
    """(state, detail) for chapter n: FRESH, STALE, MISSING, REFUSED or SKIPPED."""
    cfg = mkbody.HAND[n]
    draft = draft_for(n)
    body = os.path.join(HERE, cfg["file"])
    if draft is None:
        return "SKIPPED", "no single-file draft (c%d_draft.md)" % n
    if not os.path.exists(body):
        return "MISSING", "draft exists, %s does not" % cfg["file"]

    tmp = tempfile.mkdtemp(prefix="freshcheck")
    try:
        # mkbody writes HAND[n]['file'] relative to the working directory, so
        # it is run in a scratch directory and cannot touch the repository.
        shutil.copy(draft, os.path.join(tmp, os.path.basename(draft)))
        env = dict(os.environ)
        env["DK_DRAFT"] = os.path.basename(draft)
        env["PYTHONPATH"] = HERE + os.pathsep + env.get("PYTHONPATH", "")
        r = subprocess.run([sys.executable, os.path.join(HERE, "mkbody.py"), str(n)],
                           cwd=tmp, env=env, capture_output=True, text=True)
        built = os.path.join(tmp, cfg["file"])
        if r.returncode != 0 or not os.path.exists(built):
            first = ([l for l in (r.stdout + r.stderr).splitlines()
                      if l.strip().startswith("!!")] or ["mkbody exited %d"
                                                         % r.returncode])[0]
            return "REFUSED", first.strip().lstrip("! ")
        a = open(built, "rb").read()
        b = open(body, "rb").read()
        if a == b:
            return "FRESH", ""
        return "STALE", "%s is %d bytes, the draft builds %d" % (cfg["file"], len(b), len(a))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    fresh, stale, missing, refused, skipped = [], [], [], [], []

    for n in sorted(mkbody.HAND):
        state, why = check(n)
        if state == "FRESH":
            fresh.append(n)
        else:
            {"STALE": stale, "MISSING": missing, "REFUSED": refused,
             "SKIPPED": skipped}[state].append((n, why))

    # A body with no page is the same fault one stage later.
    pageless = [n for n in fresh if page_for(n, mkbody.HAND[n]["file"]) is None]

    print()
    print("  fresh    %d chapter(s): %s"
          % (len(fresh), ", ".join(str(x) for x in fresh) or "-"))
    for n, why in stale:
        print("  !! STALE   chapter %s - %s" % (n, why))
    for n, why in missing:
        print("  !! MISSING chapter %s - %s" % (n, why))
    for n, why in refused:
        print("  !! REFUSED chapter %s - %s" % (n, why))
    for n in pageless:
        print("  !! NO PAGE chapter %s - body is fresh but no NN-*.html exists" % n)
    if skipped:
        print()
        print("  skipped, and named rather than silently passed:")
        for n, why in skipped:
            print("     chapter %-3s %s" % (n, why))
    print()

    # See the docstring: REFUSED is loud but does not set the exit code.
    bad = len(stale) + len(missing) + len(pageless)
    if bad or refused:
        if bad:
            print("  %d chapter(s) whose page does not follow from its draft." % bad)
        if stale or missing or pageless:
            print("  Rebuild before committing: mkbody.py, then build_part_*.py,")
            print("  then linkindex.py, then index_generator.py - in that order.")
        if refused:
            print("  A REFUSED chapter does not rebuild. Resolve what mkbody names.")
    else:
        print("  every checked body is exactly what its draft builds")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
