---
format: short
lesson: code-complete-software-craftsmanship/self-documenting-code
title: A routine with 100% comments that says nothing
---

@art repeat-comments
This routine has a comment for every statement, and it tells you nothing.

@code block=1 lines=1-12 label=Java comments=keep focus="3-10@restates"
Set sum to zero. Loop over the values. Each comment restates the line under it. None says what happens to an empty array.

@words text="Say what the code can't"
A good comment says what the code can't. Its intent, or a promise like the caller guarantees at least one value.

@end text="Full lesson on Learn"
The full lesson, with a comment counting lab, is on Learn.
