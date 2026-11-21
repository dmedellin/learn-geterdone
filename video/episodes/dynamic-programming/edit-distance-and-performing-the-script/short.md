---
format: short
lesson: dynamic-programming/edit-distance-and-performing-the-script
title: Kitten to sitting takes seven steps but costs three
---

@art tile-rows
Turning kitten into sitting takes seven steps, and costs three.

@math items="k → s · keep i t t · e → i · keep n · insert g@swap k for s"
Here's the script: swap k for s, keep i, t, t, swap e for i, keep n, insert g.

@words text="7 steps · distance 3"
Keeps cost nothing, so the distance is three. And because each step names its character, you can run the script on kitten and check you really get sitting.

@end text="Full lesson on Learn"
Run it yourself on Learn.
