---
format: short
lesson: number-theory-and-cryptography/chinese-remainder-theorem
title: A third-century riddle with one answer
---

@words text="÷3 → 2,  ÷5 → 3,  ÷7 → 2" sub="how many things?"
Divided by three, two left over. By five, three. By seven, two. How many?

@math items="140 + 63 + 30 = 233@a hundred and forty;;233 ≡ 23 (mod 105)@twenty three"
Build one term for each modulus, each invisible to the other two. A hundred and forty, plus sixty three, plus thirty, is two hundred and thirty three. Reduce mod a hundred and five, and you get twenty three.

@art invisible-terms
Because three, five and seven are coprime, that answer is unique, mod a hundred and five.

@end text="Full lesson on Learn"
The full lesson, with a lab, is on Learn.
