---
format: short
lesson: code-complete-statements/using-conditionals
title: Your if-else chain is testing in the wrong order
---

@art chain-steps
Your status classifier makes over twice the tests it needs to.

@math items="as written: 3.50 tests@three point five;;success first: 1.50 tests@one point five"
Server errors are five percent, successes seventy. Test success last, and the chain makes three point five tests per status. Test it first, and it makes one point five.

@words text="Common case first" sub="and a final else for the rest"
Put the common case first, so readers and the code both meet it sooner, and keep a final else to catch what you didn't plan for.

@end text="Full lesson on Learn"
The full lesson, with a lab that weighs a chain, is on Learn.
