---
format: short
lesson: geometric-algorithms/do-two-segments-meet
title: Overlapping boxes don't mean the segments meet
---

@art box-overlap
Two segments, overlapping bounding boxes, and they still don't meet.

@math items="(0, 0)–(4, 4)  and  (2, 0)–(4, 1)@zero, zero;;signs: 1, 1, −1, −1@one, one"
Take zero, zero to four, four, against two, zero to four, one. The boxes overlap. But the four orientation signs are one, one, minus one, minus one, not opposite in pairs.

@words text="Boxes are a filter, never an answer"
Non overlapping boxes prove a miss. Overlapping boxes prove nothing at all.

@end text="Full lesson on Learn"
The full lesson on segment intersection is on Learn.
