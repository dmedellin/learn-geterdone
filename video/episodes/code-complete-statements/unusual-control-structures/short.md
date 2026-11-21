---
format: short
lesson: code-complete-statements/unusual-control-structures
title: Recursive Fibonacci makes millions of calls
---

@art recursion-tree
Fibonacci of thirty, recursively, takes over two and a half million calls.

@math items="recursion: 2,692,537 calls@two million;;loop: 29 passes@twenty nine"
Two million, six hundred and ninety two thousand, five hundred and thirty seven, to be exact. A loop reaches the same answer in twenty nine passes.

@words text="The depth was never the problem"
It's never more than thirty deep. Each call just makes two more, and they recompute the same small values again and again.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the calls, is on Learn.
