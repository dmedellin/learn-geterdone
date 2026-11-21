---
format: short
lesson: strings-and-pattern-matching/shifting-by-more-than-one
title: The string search that never reads most of the text
---

@art never-read
This string search finds the match without reading most of the text.

@words text="compare from the right, then jump"
Horspool's algorithm compares the window from its right end. Then it jumps, by how far back the last character under the window appears in the pattern.

@words text="66 characters · 48 never read"
Searching sixty six characters of English for mainly, forty eight characters are never compared to anything. The worst case, though, is no better than naive.

@end text="Full lesson on Learn"
Watch it skip on Learn.
