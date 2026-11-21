---
format: short
lesson: algorithms-and-complexity/divide-and-conquer
title: Three multiplications instead of four
---

@art four-to-three
Multiplying big numbers by halves takes four products. Karatsuba noticed you only need three.

@math items="ad + bc = (a + b)(c + d) − ac − bd@the middle;;3 products:  ac,  bd,  (a + b)(c + d)@three products"
The middle part, a d plus b c, equals a plus b times c plus d, minus a c, minus b d. So three products are enough.

@words text="Θ(n²) → Θ(n^1.585)"
Four products gives Theta of n squared. Three gives n to the one point five eight five, because log two of three is less than two.

@end text="Full lesson on Learn"
The full lesson on divide and conquer is on Learn.
