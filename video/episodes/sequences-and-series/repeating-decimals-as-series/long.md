---
format: long
lesson: sequences-and-series/repeating-decimals-as-series
title: Repeating decimals are geometric series, and 0.999… is 1
thumb: Every repeat is a fraction
---

@chapter A decimal is a series
@title text="Repeating Decimals as Series" sub="Sequences and Series" art=thumb
Why is zero point nine recurring equal to one? The answer isn't a trick. It comes from noticing that a decimal was a series all along.

@art place-value
That's what place value means. Zero point two five is two tenths plus five hundredths, which is a quarter: a sum of two terms. Zero point three recurring is the same kind of sum with no last term.

@math heading="Decimal expansion" items="0.d₁d₂d₃… = d₁/10 + d₂/100 + d₃/1000 + …@d one over ten"
In general, zero point d one d two d three means d one over ten, plus d two over a hundred, plus d three over a thousand, and so on. Its value is the number the partial sums approach.

@chapter A repeating block is geometric
@art repeating-beads
Take zero point four five four five recurring. The block forty five fills the first two places, then the next two, then the next two. Each term is the one before, divided by a hundred.

@math heading="0.454545…" items="45/100 + 45/100² + 45/100³ + …@forty five over a hundred;;a₁ = 45/100,   r = 1/100@r is one over a hundred;;S∞ = (45/100)/(99/100) = 45/99 = 5/11@five elevenths"
So it's forty five over a hundred, plus forty five over a hundred squared, and so on. a one is forty five over a hundred, and r is one over a hundred, so there's a sum. It's forty five over ninety nine, which is five elevenths.

@words text="block B of p digits  →  B / (10ᵖ − 1)" sub="p nines underneath"
That works for any repeating block. A block of p digits gives a ratio of one over ten to the p, always less than one. Clear the fractions and the value is the block over ten to the p minus one, which is p nines. So every repeating decimal is a fraction.

@chapter The school method, explained
@math heading="x = 0.BBB…" items="10ᵖx = B.BBB…@multiply by ten to the p;;10ᵖx − x = B@the tails cancel;;x = B/(10ᵖ − 1)@divide"
The method you may have learned is this proof, compressed. Call the number x, multiply by ten to the p, and the whole tail shifts one block left. Subtract x, and the tails cancel exactly, leaving the block. Divide, and you have the fraction.

@art shift-subtract
It's the same move as S n minus r S n for a geometric sum, with the shift running the other way. There, the second line was r times the first. Here, it's one over r times.

@chapter A head before the repeat
@math heading="0.2454545…" items="1000x = 245.4545…@a thousand x;;10x = 2.4545…@ten x;;990x = 243@subtract;;x = 243/990 = 27/110@twenty seven"
Now zero point two four five four five recurring. One digit, the two, comes before the repeat. A thousand x is two hundred forty five point four five recurring, and ten x is two point four five recurring. Subtract, and nine hundred ninety x is two hundred forty three. So x is twenty seven over a hundred and ten.

@words text="245/990 = 0.2474747…  ✗" sub="subtract the head: (245 − 2)/990"
The slip is leaving the head in. Two hundred forty five over nine hundred ninety is zero point two four seven four seven recurring, a different number, close enough to survive a glance.

@chapter Zero point nine recurring
@math heading="0.999… = 1, three ways" items="(9/10)/(1 − 1/10) = 1@the formula;;9/9 = 1@the block rule;;3 × 0.333… = 3 × 1/3 = 1@by thirds"
By the formula, a one is nine tenths and r is one tenth, so the sum is one. By the block rule, it's nine over nine. And by thirds: zero point three recurring is a third, so three times it is one.

@art nines-approach
The objection is that zero point nine, zero point nine nine, and so on, are all less than one. They are, each by exactly one over ten to the n. But the sum isn't one of them. It's the number they approach, and no positive number is smaller than every one of those gaps.

@art two-names
So zero point nine recurring and one are two names for the same number, like a half and two quarters. Every terminating decimal has a second name ending in nines: zero point two five is zero point two four nine nine recurring.

@chapter Which fractions repeat
@art remainder-loop
Divide by q by hand and each step leaves a remainder smaller than q. Either you hit zero and the decimal stops, or a remainder comes round again and the digits repeat. A seventh repeats a block of six. Three fortieths stops at zero point zero seven five.

@words text="rational  ⇔  terminates or repeats" sub="0.101001000100001…  never repeats"
Put both directions together. A number is rational exactly when its decimal terminates or repeats. So zero point one zero one zero zero one, with one more zero in each gap, can never be a fraction.

@chapter Try it
@words text="0.18333…" sub="head 18/100 ·  tail a₁ = 3/1000,  r = 1/10"
Your turn. Take zero point one eight three recurring. The head is eighteen hundredths. The tail starts at three thousandths with ratio one tenth. Sum the tail, add the head, and reduce. Then do it again by shifting and subtracting.

@end text="Digits in, fraction out"
You can type a repeating decimal and watch its partial sums close in on the fraction, on Learn. That's learn dot get er done dot I O.
