---
format: short
lesson: induction-and-recursion/recursive-definitions
title: This recursive definition defines nothing
---

@art runaway-chain
Here's a recursive definition that defines absolutely nothing.

@words text="f(0) = 1,   f(n) = f(n+1) − 1"
f of zero is one, and f of n is f of n plus one, minus one. Try computing f of one.

@art runaway-chain zoom=in
You need f of two. That needs f of three. It never gets back to the base, so no value is ever determined.

@words text="The recursion must decrease"
A recursive clause has to move toward the base.

@end text="Full lesson on Learn"
The full lesson on recursive definitions is on Learn.
