---
format: long
lesson: combinatorics-and-counting/combinations
title: Combinations: n choose r, and why you divide by r factorial
thumb: Count in order, then forget it
---

@chapter Order stops mattering
@title text="Combinations" sub="Combinatorics and Counting" art=thumb
A committee of three isn't a podium. Pick the same three people in any order, and it's the same committee. So how do you count selections when order doesn't matter?

@art committee-circle
An r combination of a set is just a subset of size r. The number of them is written C of n, r, and read n choose r.

@chapter Divide by r factorial
@art orderings-collapse
Here's the derivation. Count ordered selections of r distinct objects in two ways. Directly, there are P of n, r. Or first choose which r objects to use, that's C of n, r ways, and then arrange them, r factorial ways.

@math heading="n choose r" items="P(n, r) = C(n, r) · r!@P of n, r equals;;C(n, r) = P(n, r) / r!@Dividing;;= n! / (r! (n − r)!)@n factorial over"
Both count the same set, so P of n, r equals C of n, r times r factorial. Dividing gives C of n, r as P of n, r over r factorial, which is n factorial over r factorial times n minus r factorial.

@math heading="C(10, 3)" items="10 · 9 · 8 / 3! = 720 / 6 = 120@seven hundred and twenty over six"
For example, C of ten, three is ten times nine times eight, over three factorial. That's seven hundred and twenty over six, or a hundred and twenty. Each committee appeared six times among the ordered selections, once for every order.

@words text="one set, counted two ways" sub="a double count"
That proof is a double count: one set counted two ways, so the two expressions must be equal. It's the cleanest route to the formula, and later in the course it becomes a way to prove identities.

@chapter Symmetry
@art complement-split
Choosing r to include is the same as choosing n minus r to leave out. Send each subset to its complement. That pairing is a bijection, because a set is determined by its complement.

@math heading="Symmetry" items="C(n, r) = C(n, n − r)@C of n, r equals;;C(30, 28) = C(30, 2) = 435@thirty, two"
So C of n, r equals C of n, n minus r. It's also a shortcut. C of thirty, twenty eight is C of thirty, two, which is four hundred and thirty five. Two multiplications instead of twenty eight.

@words text="Σ C(n, r) = 2ⁿ" sub="every subset has exactly one size"
And if you add C of n, r over every size r, you get two to the n. Every subset has exactly one size, so the sum counts each subset once. Directly, each element is either in or out: two to the n.

@chapter Two examples
@art card-fan
A five card hand from fifty two cards: the order the cards arrive in doesn't matter, so it's C of fifty two, five, which is two million, five hundred and ninety eight thousand, nine hundred and sixty. Hands with all four aces: one way to take the aces, and forty eight choices for the fifth card.

@art lattice-path
Or take paths on a grid, from zero, zero to m, n, using unit steps right and up. Each path is m plus n steps, and m of them are right. Choosing which steps go right fixes the path completely, so there are C of m plus n, m paths.

@chapter Committees with structure
@art two-groups
From eight mathematicians and six physicists, choose five, with at least three mathematicians. Split by how many mathematicians there are. The cases are disjoint, because a committee has one definite make up.

@math heading="5 from 8 maths, 6 physics, at least 3 maths" items="3 + 2: C(8,3)·C(6,2) = 56 · 15 = 840@Three mathematicians;;4 + 1: C(8,4)·C(6,1) = 70 · 6 = 420@Four and one;;5 + 0: C(8,5)·C(6,0) = 56 · 1 = 56@Five and none;;total = 1316@one thousand three hundred and sixteen"
Three mathematicians and two physicists: fifty six times fifteen, eight hundred and forty. Four and one: seventy times six, four hundred and twenty. Five and none: fifty six. Total, one thousand three hundred and sixteen.

@words text="1316 < C(14, 5) = 2002" sub="product inside a case, sum across cases"
As a sanity check, all committees of five from fourteen number two thousand and two, and our answer is smaller. Inside each case the two choices are independent, so they multiply. The sum rule only combines the cases.

@chapter Where people slip
@list heading="Common slips" items="Using C where order matters@The first|Adding the parts of one case@The second|Computing the large side@And the third"
The first slip is using C where order matters. A three digit code isn't a three element subset. The second is adding the parts of one case, when three mathematicians and two physicists is a product. And the third is computing the large side of a symmetric coefficient.

@chapter Try it
@words text="5-card hands with at least two aces" sub="by cases, and by complement"
Your turn. Count the five card hands with at least two aces. Once by cases, exactly two, three or four aces, each a product of C of four, k and C of forty eight, five minus k. And once by complement. The two totals must agree.

@end text="Compare the C row and the P row"
You can list the subsets and watch C and P differ by exactly r factorial, on Learn. That's learn dot get er done dot I O.
