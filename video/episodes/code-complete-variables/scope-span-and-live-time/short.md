---
format: short
lesson: code-complete-variables/scope-span-and-live-time
title: Moving one line cut this variable's life from 16 lines to 9
---

@art vulnerability-window
Move one declaration, and a variable lives for nine lines instead of sixteen.

@words text="live time = last − first + 1"
Live time is the stretch from a variable's first reference to its last. Declared at the top on line three and last used on line eighteen, it's sixteen lines.

@art near-use
Declare it just before its loop, on line ten, and it's nine. Same program, less to hold in your head.

@end text="Full lesson on Learn"
The full lesson, with a lab to measure your own routines, is on Learn.
