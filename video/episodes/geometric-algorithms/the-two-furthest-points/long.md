---
format: long
lesson: geometric-algorithms/the-two-furthest-points
title: Finding the two furthest points with rotating calipers
thumb: Four pairs, not 120
---

@chapter The question
@title text="The Two Furthest Points" sub="Geometric Algorithms" art=thumb
Which two points in a set are furthest apart? The obvious answer checks every pair. A better one throws most of the points away before measuring anything.

@art cloud-rectangle
The lab's cloud is sixteen points: the four corners of a twelve by nine rectangle, and twelve more scattered inside. Checking every pair means sixteen times fifteen over two, a hundred and twenty pairs.

@chapter Only hull vertices
@art interior-average
Here's the first idea. A point strictly inside the hull is a weighted average of hull vertices. And for any other point r, at least one of those vertices is at least as far from r. So an interior point can never be an endpoint of the longest segment.

@words text="diameter of the set = diameter of its hull"
So the diameter of the set is the diameter of its hull. On this cloud, that discards twelve points before a single distance is computed.

@chapter Antipodal pairs
@art parallel-rulers
Second idea. Two hull vertices can only be the diameter if you can lay a ruler against the hull at each of them, with the two rulers parallel. Lines like that touch the hull with all of it on one side. Such a pair is called antipodal.

@art perpendicular-lines
Why? Take the furthest pair, u and v, and draw lines through each, perpendicular to the segment between them. If any point lay beyond one of those lines, it would be further from the other end than the diameter. Impossible. So both lines support the hull, and u and v are antipodal.

@words text="exhaustive search over a set proved to contain the answer"
That's what makes the method confident rather than heuristic. The diameter is guaranteed to be among the antipodal pairs, so checking all of them is enough.

@chapter The calipers
@art calipers-walk
The rotating calipers walk two indices round the hull in step, like the two jaws of a caliper turning together. That lists every antipodal pair in linear time. There are order h of them, not h times h minus one over two.

@chapter Sixteen points
@math heading="The cloud" items="hull: the rectangle, h = 4@the hull is;;4 antipodal pairs  vs  120 pairs@four antipodal pairs;;12² + 9² = 225@twelve squared;;(0, 0)–(12, 9)  and  (12, 0)–(0, 9)@two different pairs"
On the cloud, the hull is the rectangle, so h is four. The calipers examine four antipodal pairs, against a hundred and twenty. Twelve squared plus nine squared is two hundred and twenty five, the squared diameter. And two different pairs attain it: zero, zero to twelve, nine, and twelve, zero to zero, nine.

@words text="Squared distances, never a root"
Notice the answer is a squared distance, an integer. Comparing squares orders pairs exactly like comparing distances, so nothing ever rounds. And with a tie, the answer is a value, and the printed pair is just one of several.

@art cloud-rectangle
The brute force runs too, on every redraw, over all one hundred and twenty pairs, and returns the same two hundred and twenty five. That's on purpose. An algorithm that visits the wrong pairs returns a distance that's real and simply not the largest. Nothing inside it looks inconsistent, so the check has to be a different computation, not a second opinion from the same one.

@chapter What it costs
@art convex-circle
The hull wasn't free. It cost a sort. So the diameter costs n log n in total, against n squared for the scan.

@words text="h is a property of the input" sub="8 in convex position: 8 pairs vs 28"
And h depends on the input. Eight points in convex position give eight antipodal pairs against twenty eight. Points on a circle make h equal n, and the hull discards nothing. So four and a hundred and twenty are true about this cloud. Order n log n is the claim about every input, and it's proved, not measured.

@chapter Where people slip
@list heading="Common slips" items="Taking the square root@The first|Treating O(h) as a bound for your data@The second|Trusting the walk without a check@And the third"
The first slip is taking the square root, turning an exact integer into an approximation for no benefit. The second is treating order h as a promise, when h can be n. And the third is trusting the walk unchecked. One step too few returns a real distance that isn't the largest. That's why the lab runs the brute force on every redraw.

@end text="Four pairs, not a hundred and twenty"
Drag the points and watch the calipers walk, on Learn. That's learn dot get er done dot I O.
