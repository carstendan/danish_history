# -*- coding: utf-8 -*-
"""dkpaths.py - resolve DK_OUT / DK_CHAPTERS / DK_SRC, and refuse a stale one.

WHY THIS EXISTS. On 18 September 2026 the working folder moved out of iCloud to
~/Documents/Danish History. The scripts were all fine - every one of them derives
its own location from __file__ - but `DK_CHAPTERS` and `DK_OUT` were still
exported in the shell from the old path, because the START_HERE documents set
them with `export DK_CHAPTERS="$PWD/.."`, which is correct when you run it and
stale for the rest of the session. Part H, Part I and linkindex.py all died with
FileNotFoundError pointing at a folder that no longer existed.

THAT FAILURE WAS THE LUCKY ONE. The dangerous version of the same mistake is the
variable pointing at a folder that DOES still exist - an old copy, a mirror, a
duplicate - in which case nothing crashes, the build writes chapters into the
wrong tree, and the shipped book quietly stops matching its source. HANDOFF's
known-issue 5 records that this has already happened once to this project.

SO: a missing target is a REFUSAL, and a target outside this repository is a
LOUD WARNING rather than a silent success. Building into another folder is
sometimes legitimate - index_generator.py's own default is a container path - so
it is not forbidden, only made impossible to do by accident.
"""
import os
import sys


def resolve(var, default, what):
    """The directory for `var`, defaulting to `default`. Refuses a stale value."""
    raw = os.environ.get(var)
    if not raw:
        return default
    path = os.path.abspath(os.path.expanduser(raw))
    if not os.path.isdir(path):
        sys.exit(
            "!! %s points at a directory that does not exist:\n"
            "     %s\n"
            "   It is set in your shell and is probably left over from a folder that\n"
            "   has since moved. Fix it or unset it:\n"
            "     unset %s\n"
            "   (%s)" % (var, path, var, what))
    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(here)
    if os.path.commonpath([path, repo]) != repo:
        sys.stderr.write(
            "\n   !! WARNING: %s points OUTSIDE this repository.\n"
            "      %s = %s\n"
            "      this repo  = %s\n"
            "   If that is not deliberate, the build is about to write into the wrong\n"
            "   tree and the shipped book will stop matching its source.\n\n"
            % (var, var, path, repo))
    return path
