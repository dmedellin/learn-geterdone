---
format: short
lesson: code-complete-code-improvements/boundaries-and-bad-data
title: The test value that finds the bug is never fifty
---

@art typical-passes
A typical value passes a wrong check every time.

@math items="qty > 0 && qty < 99@less than ninety nine;;50 → valid ✓ · 99 → refused ✗@ninety nine"
Orders of one to ninety nine are valid. This check says above zero and less than ninety nine. An order of fifty passes. But ninety nine, the largest valid order, is refused.

@words text="Below, on, and above each boundary"
So test every boundary three times: just below it, on it, and just above it.

@end text="Full lesson on Learn"
The full lesson, with a boundaries lab, is on Learn.
