---
format: long
lesson: combinatorics-and-counting/permutations
title: Permutations: counting arrangements where order matters
thumb: n down to n − r + 1
---

@chapter Order matters
@title text="Permutations" sub="Combinatorics and Counting" art=thumb
Ten runners, and three medals: gold, silver and bronze. How many ways can the podium be filled?

@art podium
Order matters here. The same three runners in a different order is a different outcome. That's what makes this a permutation, an ordered arrangement, rather than a combination.

@chapter Counting the positions
@art shrinking-stacks
Fill the positions in order. Gold has ten candidates. Whoever won it, silver has nine left, and then bronze has eight. The number of options at each stage doesn't depend on who was chosen earlier, so the product rule applies.

@math heading="Ten runners, three medals" items="P(10, 3) = 10 · 9 · 8 = 720@ten times nine times eight"
So P of ten, three is ten times nine times eight, which is seven hundred and twenty.

@math heading="r-permutations of n" items="P(n, r) = n(n − 1)(n − 2)⋯(n − r + 1)@n times n minus one;;= n! / (n − r)!@n factorial over"
In general, the number of ordered arrangements of r out of n distinct objects is n times n minus one, and so on, down to n minus r plus one. That's n factorial over n minus r factorial.

@words text="r factors: n down to n − r + 1" sub="stopping at n − r gives P(n, r + 1)"
Count the factors. There are exactly r of them, running from n down to n minus r plus one. Running down to n minus r is the standard off by one error, and it gives you P of n, r plus one instead.

@words text="0! = 1" sub="so P(n, n) = n!/0! = n!"
And zero factorial is one. It's a convention, the empty product, and it works: P of n, n comes out as n factorial, which is right, since that's all n objects arranged.

@chapter Around a circle
@art round-table
Now seat n people around a round table, where rotations count as the same seating. There are n factorial ways to arrange them in a line. Each circular seating matches exactly n of those, one for each choice of who's written first.

@math heading="Circular arrangements" items="n! / n = (n − 1)!@n factorial over n"
So the circular count is n factorial over n, which is n minus one factorial. Equivalently, fix one person's seat to break the symmetry, then arrange the other n minus one freely.

@art rotated-tables
That division is only legitimate because rotations were declared identical. If the chairs are numbered, moving everyone one seat along is a different seating, and the count is n factorial. The question decides which, not the shape of the table.

@words text="count them all, divide by the class size"
That's the pattern to remember. When several arrangements count as the same, count them all, then divide by the size of each group of equivalent ones.

@chapter A worked seating
@art glued-pair
Eight people at a round table, and two of them must sit together. Glue the pair into a single block. That leaves seven items around a circle.

@math heading="Eight at a round table, two together" items="all: (8 − 1)! = 5040@seven factorial;;together: (7 − 1)! · 2 = 720 · 2 = 1440@six factorial;;apart: 5040 − 1440 = 3600@three thousand six hundred"
Unrestricted, that's seven factorial, five thousand and forty. With the block, six factorial is seven hundred and twenty, times two for the pair's internal order: one thousand four hundred and forty. With the two apart, three thousand six hundred.

@words text="1440 / 5040 = 2/7" sub="fix one; 2 of the other 7 seats are beside them"
Here's a cheap check. One thousand four hundred and forty over five thousand and forty is two sevenths. Fix one of the pair. The other has seven seats to choose from, and exactly two of them are beside the first.

@chapter Factorials explode
@art growth-bars
Factorials grow explosively. Five factorial is a hundred and twenty. Ten factorial is three million, six hundred and twenty eight thousand, eight hundred. And fifty two factorial, the number of orders of a deck of cards, is about eight times ten to the sixty seven.

@words text="52! ≈ 8.07 × 10⁶⁷"
So any algorithm that examines every permutation of a modest input isn't slow. It's impossible.

@chapter Where people slip
@list heading="Common slips" items="Using P when order doesn't matter@The first|Miscounting the factors@The second|Forgetting to divide out a symmetry@The third"
The first slip is using P when order doesn't matter. A committee of three isn't an ordered triple. The second is miscounting the factors. And the third is forgetting to divide out a symmetry, or dividing by the wrong one. Name the symmetry before you divide.

@chapter Try it
@words text="6 at a round table, two people not adjacent" sub="by complement; why 5! and not 6!?"
Your turn. Count the ways to seat six people around a round table with two specific people not adjacent. Do it by complement. And say exactly why the circular count is five factorial, rather than six factorial.

@end text="List the permutations yourself"
You can list every permutation for small numbers, and watch the count stay exact for big ones, on Learn. That's learn dot get er done dot I O.
