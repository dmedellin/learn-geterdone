---
format: short
lesson: intro-algorithms-algebraic-topics/number-theoretic-algorithms
title: The worst input for Euclid's algorithm is Fibonacci
---

@art fibonacci-worst
Want to make Euclid's algorithm work as hard as possible? Feed it Fibonacci numbers.

@math items="1147, 851: 4 divisions@four divisions;;89, 55: 9 divisions@take nine"
The lesson's pair, eleven forty seven and eight fifty one, takes four divisions. But eighty nine and fifty five take nine, every quotient one until the last.

@words text="O(lg b) calls" sub="Lamé's theorem"
Fibonacci numbers grow exponentially, so even the worst case takes only logarithmically many steps. That's Lamay's theorem.

@end text="Full lesson on Learn"
Run Euclid yourself in the full lesson on Learn.
