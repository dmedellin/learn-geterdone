---
format: short
lesson: code-complete-statements/controlling-loops
title: The loop that can never stop
---

@art skipping-bound
This loop looks fine, and it will never end.

@words text="for (int i = 0; i != 9; i += 2)"
Start at zero, step by two, and stop when i equals nine. But i only takes even values, and nine is odd. Even when it wraps round past the top of Java's int, it stays even.

@words text="i < 9 → stops after 5 passes"
Write less than instead, and it stops after five passes. So check that every loop ends, under every condition.

@end text="Full lesson on Learn"
The full lesson, with a lab that reads a loop's header, is on Learn.
