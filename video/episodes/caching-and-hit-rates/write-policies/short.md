---
format: short
lesson: caching-and-hit-rates/write-policies
title: Write-back is only faster if your writes repeat
---

@art distinct-trace
Write back caching is faster, right? Only if your writes repeat.

@math items="A B A C A | B A D A B  →  6 backend writes@A B A;;A B C D E | F G H I J  →  10 backend writes@A through J"
Flush every five writes. On A, B, A, C, A, then B, A, D, A, B, ten writes become six. On A through J, all different, ten stay ten.

@words text="Same loss window either way"
And both still carry a loss window, whatever was dirty when the process died. Count your own trace first.

@end text="Full lesson on Learn"
The full lesson, with your own trace, is on Learn.
