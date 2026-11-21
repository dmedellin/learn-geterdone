---
format: short
lesson: integer-programming/the-travelling-salesman-problem
title: There are not n factorial travelling salesman tours
---

@art city-tour
Seven cities. Five thousand and forty tours? No. Three hundred and sixty.

@math items="7! = 5040  orderings@orderings;;6!/2 = 360  distinct tours@three hundred and sixty"
Seven factorial counts orderings. But the starting city doesn't change a tour, and nor does the direction. So it's six factorial over two, three hundred and sixty.

@words text="Overcount: 2 × 7 = 14"
That's an overcount of fourteen, at exactly the size where you decide whether to enumerate.

@end text="Full lesson on Learn"
The full lesson, with tours to bound and cut, is on Learn.
