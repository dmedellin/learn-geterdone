---
format: short
lesson: data-structures/building-a-heap-in-linear-time
title: n nodes times log n levels is the wrong sum
---

@art height-layers
Building a heap costs n log n, right? Only if every node is as high as the root.

@math items="16·0 + 8·1 + 4·2 + 2·3 + 1·4@sixteen are leaves;;= 26  ·  not 31 × 4 = 124@twenty six"
With thirty one keys, sixteen are leaves and sift nowhere. Add up the real heights and you get twenty six. Not a hundred and twenty four.

@words text="Θ(n)" sub="under 2n, every time"
Most nodes sit near the bottom, so most sifts are short, and the total stays under two n.

@end text="Full lesson on Learn"
The full lesson, with both builds racing, is on Learn.
