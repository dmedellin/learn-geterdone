---
format: long
lesson: geometric-algorithms/four-zero-signs-and-two-different-answers
title: Same four signs, opposite answers: the collinear segment case
thumb: Same signs, opposite answers
---

@chapter Two inputs
@title text="Four Zero Signs and Two Different Answers" sub="Geometric Algorithms" art=thumb
Here are two pairs of segments with exactly the same four orientation signs. One pair meets. The other doesn't. So no rule built on those signs can ever tell them apart.

@math heading="Both on the line y = 0" items="(0, 0)–(6, 0)  and  (4, 0)–(10, 0):  meet@zero, zero to six;;(0, 0)–(4, 0)  and  (6, 0)–(10, 0):  miss@zero, zero to four;;signs in both:  0, 0, 0, 0@zero, zero, zero, zero"
First pair: zero, zero to six, zero, against four, zero to ten, zero. They share everything from four to six, so they meet. Second pair: zero, zero to four, zero, against six, zero to ten, zero. There's a gap from four to six, so they miss. And in both, the signs are zero, zero, zero, zero.

@art overlap-vs-gap
A function of the four signs gives one answer on one sign vector. It can't be both true and false. So any intersection test computed from the signs alone is wrong on at least one of these. That's a proof, not a warning.

@chapter Why there's no signal
@art zero-on-line
This isn't a defect of the orientation test. It's what the test means. A zero says c is on the line through a and b, with no information about where. Once all four points are collinear, every determinant stays zero however you slide the points along the line. There's simply no more signal to extract.

@chapter Finish it in one dimension
@art projection
So finish it as a one dimensional question. Let r be p two minus p one, the direction of the first segment. Project every point onto r with a dot product.

@math heading="Projection coordinates" items="t₀ = (q₁ − p₁)·r@t nought;;t₁ = t₀ + (q₂ − q₁)·r@t one;;first segment: [0, r·r]@zero to r dot r;;meet ⟺ max(t₀, t₁) ≥ 0  and  min(t₀, t₁) ≤ r·r@they meet when"
t nought is q one minus p one, dotted with r. t one is t nought plus q two minus q one, dotted with r. The first segment runs from zero to r dot r. And they meet when the larger of t nought and t one is at least zero, and the smaller is at most r dot r.

@words text="integer dot products, two comparisons" sub="no normalising, no division"
Every one of those is an integer dot product. No unit vectors, no division. The whole collinear branch is a handful of multiplications and two comparisons, and it turns a test that's right in general position into one that's right on everything.

@chapter The boxes, here
@art boxes-on-line
Here's a surprise. On these two inputs, the bounding boxes do separate them: overlapping, and not. Along a line, the coordinates move steadily with the parameter. So for collinear segments, overlapping boxes and overlapping intervals are the same condition. Across one hundred ninety seven thousand, five hundred and six random collinear pairs, the two never disagree.

@words text="exact when collinear, a filter otherwise"
But that's a narrow result. The moment segments aren't collinear, boxes are only a filter. Zero, zero to four, four, against two, zero to four, one has overlapping boxes and no crossing. The projection is worth learning because it's the same computation in every case.

@chapter A segment that is a point
@art degenerate-point
Here's a third family of four zeros. A segment whose endpoints coincide is just a point. The point three, two against the segment from zero, zero to six, four, which passes through it. All four determinants are zero, the proper test says no, and the right answer is yes. A route that divided by r dot r would fail here.

@chapter Where people slip
@list heading="Common slips" items="Hunting for a cleverer combination of signs@The first|Deciding the box test is enough@The second|Testing only on crossings@And the third"
The first slip is hunting for a cleverer combination of the signs. The information was never in them. The second is deciding the box test is enough. It decides the collinear branch and only filters the rest. And the third is testing only on crossings. A suite of crossings and clear misses passes with no collinear branch at all.

@chapter Try it
@art test-suite
The usual reason the collinear branch is missing from an implementation isn't cost. It's that the author never built an input that reaches it.

@words text="Build the seven" sub="crossing · T-junction · shared endpoint · parallel · point · overlap · gap"
Write a test suite of your own: a proper crossing, a T junction, a shared endpoint, a parallel pair, a degenerate segment, and the two collinear cases with the same signs and opposite answers.

@end text="Same signs, opposite answers"
Switch between the two collinear examples and watch every row change but one, on Learn. That's learn dot get er done dot I O.
