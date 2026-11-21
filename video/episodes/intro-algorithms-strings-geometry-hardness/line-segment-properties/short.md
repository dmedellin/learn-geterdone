---
format: short
lesson: intro-algorithms-strings-geometry-hardness/line-segment-properties
title: Do two segments cross? No division needed
---

@art straddle
You can tell whether two segments cross without ever finding where.

@words text="x₁·y₂ − x₂·y₁"
The cross product's sign tells you which side of a line a point is on. Four of them tell you whether each segment's ends lie on opposite sides of the other.

@art boundary
And if one value is zero, a quick bounding box check settles the touching case.

@end text="Full lesson on Learn"
No division, no angles. Try it in the full lesson on Learn.
