---
format: short
lesson: geometric-algorithms/the-vertex-a-rounded-determinant-deletes
title: The hull that's perfectly valid and still wrong
---

@art stack-pop
One rounded determinant, and a convex hull silently loses a corner.

@math items="exact:  +1  ⟹  3 vertices@plus one;;double:  0  ⟹  pop  ⟹  2 vertices@rounds to zero"
On the needle triple, the exact determinant is plus one, a left turn, so all three points stay. In double precision it rounds to zero, the monotone chain pops the middle point, and only two come back.

@art well-formed-wrong
The result is still a perfectly valid convex polygon. Nothing downstream can tell a corner is missing.

@end text="Full lesson on Learn"
The full lesson, with both traces, is on Learn.
