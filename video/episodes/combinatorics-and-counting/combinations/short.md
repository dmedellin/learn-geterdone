---
format: short
lesson: combinatorics-and-counting/combinations
title: 120 orders, only 20 committees
---

@art orderings-collapse
Pick three of six people. A hundred and twenty orders, but only twenty committees.

@math items="P(6, 3) = 6 · 5 · 4 = 120@six times five times four;;each committee: 3! = 6 orders@three factorial;;120 / 6 = 20 = C(6, 3)@So a hundred and twenty over six"
In order, it's six times five times four, a hundred and twenty. But each committee shows up once for every order of its members, and there are three factorial, six, of those. So a hundred and twenty over six is twenty.

@words text="C(n, r) = P(n, r) / r!"
That's the whole formula. Count in order, then divide by r factorial to forget the order.

@end text="Full lesson on Learn"
The full lesson, with every subset listed, is on Learn.
