"""pagecount.py - SHIM. The one implementation now lives in pagewords.py.

This file existed to stop seven copies of the page-word rule drifting apart, and
then a second copy of the rule was written beside it. bookstats.py imported
pagewords, narrative.py imported this, and the two disagreed by about 42 words a
page - free-standing punctuation from the inlined rail script, which pagewords
excludes and this did not. Nothing imports this module any more; it is kept as a
shim so that any caller written against the old name still gets one answer, and
so that removing it is a separate decision from fixing the disagreement. See open
item 63.
"""
from pagewords import (WORDISH, WPM, body_after_style, minutes, pagewords,
                       textwords, words)

# Kept for callers that referenced it. The token test is now WORDISH, which is
# strictly stronger: it drops every separator this set listed and every other
# bare-punctuation token as well.
SEPARATORS = {'\u2014', '\u2013', '\u00b7', '-', '\u2192', '\u2190'}

__all__ = ['WORDISH', 'WPM', 'SEPARATORS', 'body_after_style', 'minutes',
           'pagewords', 'textwords', 'words']
