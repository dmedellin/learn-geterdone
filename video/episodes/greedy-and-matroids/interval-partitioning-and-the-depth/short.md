---
format: short
lesson: greedy-and-matroids/interval-partitioning-and-the-depth
title: The number that proves your schedule is optimal
---

@art alive-at-t
How do you prove no schedule could use fewer rooms?

@words text="t = 2:  A 0–3 · B 1–4 · C 2–5"
Find a moment where the most intervals are alive. At time two, three lectures are all running. They all overlap, so no two can share a room.

@words text="depth 3 = rooms 3"
So every schedule needs at least three rooms. Greedy used three. The bound and the schedule meet, and that's the proof.

@end text="Full lesson on Learn"
Find the certificate for your own lectures on Learn.
