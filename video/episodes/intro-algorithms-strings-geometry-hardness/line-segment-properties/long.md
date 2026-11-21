---
format: long
lesson: intro-algorithms-strings-geometry-hardness/line-segment-properties
title: Do two segments cross? One cross product at a time
thumb: No division, no angles
---

@chapter A promise
@title text="Line-Segment Properties and Intersection" sub="Introduction to Algorithms, Sections 33.1–33.2" art=thumb
Chapter thirty three works with points in the plane. Its first section makes a promise, and keeps it.

@quote text="We need neither division nor trigonometric functions, both of which can be computationally expensive and prone to problems with round-off error." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 33.1"
We need neither division nor trigonometric functions, both of which can be computationally expensive and prone to problems with round off error. Every question gets answered with adds, subtracts, multiplies and comparisons.

@chapter The cross product
@art parallelogram
The cross product of two vectors is x one times y two, minus x two times y one. Read it as the signed area of the parallelogram they span. Positive means the first is clockwise from the second. Negative, counterclockwise. Zero, colinear.

@art turn-test
Which way does a path from p zero through p one to p two turn? Take p two minus p zero, cross p one minus p zero. In the book's convention, negative is a left turn, positive is a right turn, and zero means the three points lie on one line.

@chapter Do two segments meet?
@art straddle
A segment straddles a line when its endpoints lie strictly on opposite sides of it. Two segments cross when each straddles the line through the other. So the test computes four orientations, one for each endpoint against the other segment.

@art boundary
If some value is zero, that endpoint is colinear with the other segment, and the signs decide nothing. Then a bounding box check decides whether the point actually lies within the segment. That boundary case is half the procedure, not a footnote.

@art parallel-miss
The lab's presets cover these cases. Two colinear segments sharing a stretch, two sharing only an endpoint, and a single point lying on a segment all touch, and so they meet. Colinear segments with a gap, or parallel ones, never meet, and their boxes don't overlap.

@chapter The lesson's segments
@math heading="(1, 1)–(7, 5) and (2, 6)–(6, 0)" items="orientations: −26, 26, 26, −26@minus twenty six;;each pair opposite in sign ⇒ proper crossing@each pair"
Take the segment from one, one to seven, five, and the one from two, six to six, zero. The lab prints minus twenty six, twenty six, twenty six, minus twenty six. Each pair has opposite signs, so the crossing is proper.

@math heading="Now (4, 3)–(4, 8)" items="third orientation = 0@becomes zero;;(4, 3) on the line, halfway along@halfway along;;touching: yes · proper: no@touching"
Now move the second segment to run from four, three up to four, eight. The third orientation becomes zero, because four, three lies on the line through the first segment, halfway along. The sign test alone decides nothing. The boundary case finds the point inside the segment, so they're touching, not crossing properly.

@words text="lab: orient = (b − a) × (c − a)" sub="the negative of the book's DIRECTION"
One warning about signs. The lab's orientation is the negative of the book's direction. A rule like positive means a left turn is true in one convention and false in the other. The verdicts don't change, because the test compares signs in pairs.

@chapter Any two of n
@art sweep-line
Section thirty three point two asks whether any two of n segments meet. Testing every pair is theta of n squared. A sweep does it in n log n. A vertical line moves left to right, stopping at endpoints, and a red black tree keeps the segments it cuts, ordered by height.

@words text="Test only new neighbours" sub="O(n lg n) · yes or no"
At a left endpoint, insert the segment, and test it against the ones just above and below. At a right endpoint, test those two neighbours against each other, and delete it. The leftmost crossing, if any, is between two segments that become neighbours first. It answers yes or no, not every crossing.

@chapter Where people slip
@list heading="Common slips" items="Testing only for straddling@The first|Mixing sign conventions@The second|Solving for the intersection point@the third"
The first slip is testing only for straddling. A zero value needs the boundary case. The second is mixing the two sign conventions. And the third is solving for the intersection point with slopes, which needs division and fails for vertical segments.

@chapter Try it
@code block=1 lines=1-2 focus="1@zero, zero|2@three, one"
Your turn. Take the segment from zero, zero to six, zero, and the one from three, one to eleven, minus one. Compute the book's four values by hand, say which segment straddles which line, and decide whether they meet.

@end text="Test two segments"
You can type four points and see every orientation, on Learn. That's learn dot get er done dot I O.
