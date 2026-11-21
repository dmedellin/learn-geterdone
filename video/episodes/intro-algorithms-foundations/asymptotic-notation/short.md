---
format: short
lesson: intro-algorithms-foundations/asymptotic-notation
title: This big O claim passes 10,000 tests and is false
---

@art witness-breaks
This big O claim passes ten thousand checks. It's still false.

@math items="n lg n ≤ 100·n@n log n;;holds for every n up to 10,001@ten thousand;;fails once lg n > 100@log n passes a hundred"
Claim n log n is O of n, with c a hundred. Check every n up to ten thousand and one, and it holds. But it fails once log n passes a hundred, near two to the hundred.

@words text="Checks refute; only proofs prove"
A finite check can refute a witness. It can never prove a bound.

@end text="Full lesson on Learn"
Test your own witnesses in the full lesson on Learn.
