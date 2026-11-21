---
format: short
lesson: intro-algorithms-foundations/solving-recurrences
title: The master theorem is a contest
---

@art root-vs-leaves
The master theorem is just a contest between a tree's root and its leaves.

@math items="leaves: n^(log_b a)@the leaves;;root: f(n)@the root"
For a T of n over b plus f of n, the leaves add up to n to the log base b of a. The root costs f of n.

@list items="Leaves win: Θ(n^(log_b a))@leaves win|Tie: times lg n@a tie|Root wins: Θ(f(n))@root wins"
If the leaves win by a polynomial factor, they set the answer. A tie multiplies by log n. If the root wins, and it's regular, it sets the answer.

@end text="Full lesson on Learn"
Watch it on real recurrences in the full lesson on Learn.
