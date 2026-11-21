---
format: long
lesson: geometric-algorithms/do-two-segments-meet
title: Do two segments meet? Four signs, and the zeros they miss
thumb: Four signs, then the zeros
---

@chapter The question
@title text="Do Two Segments Meet" sub="Geometric Algorithms" art=thumb
Do two line segments meet? Four orientation signs answer the case everybody draws. The hard part is every case where one of those signs is zero.

@chapter Three words
@list heading="Three words" items="Cross properly: each has the other's ends strictly on opposite sides@cross properly|Touch: an endpoint of one lies on the other@touch|Meet: share at least one point@meet"
Let's fix three words. Two segments cross properly when each one has the other's endpoints strictly on opposite sides. They touch when an endpoint of one lies on the other. And they meet when they share at least one point, which means they cross properly or touch.

@chapter Straddling, both ways
@art straddle-one
Segment p one p two crosses the line through q one and q two when p one and p two are strictly on opposite sides of it. That's two orientation tests with different signs. But that alone isn't enough.

@art straddle-miss
The segments might cross each other's lines in places neither segment reaches. So ask the same question the other way round too. Do q one and q two sit on opposite sides of the line through p one and p two? Four tests, opposite signs in pairs.

@words text="no zero among the four  ⟹  meet ⟺ cross properly"
When none of the four determinants is zero, that's exactly right: the segments meet if and only if they cross properly. Two distinct lines meet in at most one point, and that point is inside both segments.

@chapter The crossing everybody draws
@math heading="(0, 0)–(6, 6)  and  (0, 6)–(6, 0)" items="determinants: −36, 36, 36, −36@minus thirty six;;signs: −1, 1, 1, −1@the signs are;;|orient| = 36  ⟹  triangle area 18@area eighteen"
Take zero, zero to six, six, against zero, six to six, zero. The four determinants are minus thirty six, thirty six, thirty six, minus thirty six. So the signs are minus one, one, one, minus one, opposite in each pair. And thirty six means each triangle has area eighteen, which the test throws away.

@art x-crossing
Everything agrees here: the proper test, the parametric solve, the bounding boxes. Which is exactly why it's the wrong example to test an implementation on.

@chapter Where the zeros come from
@art t-junction
A zero means three of the points are collinear. Then the answer depends on where along the line things sit, and a determinant can't see that, because it's zero for every point on the line. Rectilinear layouts, grids, shared endpoints: real data is full of zeros. Four of the lab's seven examples are cases the proper test alone gets wrong.

@words text="right in general position" sub="wrong on the inputs people actually have"
So the no zeros hypothesis is doing all the work, and it almost never holds on real data. An implementation that ships the proper test alone is correct in general position, and wrong on the inputs people actually have. The zero cases have to be finished along the segment, by comparing coordinates.

@chapter Boxes filter, never decide
@art box-overlap
Bounding boxes that don't overlap prove the segments miss. It's four comparisons with no multiplication, worth doing first.

@math heading="(0, 0)–(4, 4)  and  (2, 0)–(4, 1)" items="bounding boxes overlap@boxes overlap;;signs: 1, 1, −1, −1@one, one;;they do not meet@do not meet"
But overlap proves nothing. Type zero, zero to four, four, against two, zero to four, one. The boxes overlap, the signs are one, one, minus one, minus one, and the segments do not meet.

@chapter The check
@math heading="The parametric route" items="p₁ + t(p₂ − p₁) = q₁ + u(q₂ − q₁)@p one plus t;;meet ⟺ 0 ≤ t ≤ 1 and 0 ≤ u ≤ 1@between zero and one"
The lab checks the verdict another way. Write a point on each segment as p one plus t times its direction, and q one plus u times its direction, and set them equal. The segments meet when both t and u are between zero and one.

@art parametric-check
t and u are ratios of determinants. Force the denominator positive, and you compare numerators against it, with no division. If the denominator is zero, the segments are parallel, and the collinear case becomes an interval overlap, checked with a dot product. It shares no logic with the four signs, so it really is a check.

@chapter Where people slip
@list heading="Common slips" items="Shipping the proper test as the whole test@The first|Using bounding boxes as a decision@The second|Dividing to find the crossing point@And the third"
The first slip is shipping the proper test as the whole intersection test. The second is using bounding boxes as a decision. And the third is dividing to find the crossing point. The moment t and u become decimals, comparing them with zero and one stops being exact. Get the verdict exactly first.

@end text="Four signs, then finish the zeros"
Try all seven worked examples, and your own, on Learn. That's learn dot get er done dot I O.
