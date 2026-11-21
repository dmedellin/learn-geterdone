---
format: short
lesson: code-complete-code-improvements/refactoring-safely
title: Count this before you extract a method
---

@art block-in-out
Before you extract a block into a method, count two things.

@words text="In → parameters · Out → results"
Ins are what the block reads that was set before it. They become parameters. Outs are what it sets that's read after it. They're the results.

@art two-results
A Java method returns one value. So a loop that leaves both a balance and its fees won't extract cleanly. It needs a small class, or two routines.

@end text="Full lesson on Learn"
The full lesson, with an extraction lab, is on Learn.
