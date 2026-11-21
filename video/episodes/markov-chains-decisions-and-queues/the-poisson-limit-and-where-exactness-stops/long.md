---
format: long
lesson: markov-chains-decisions-and-queues/the-poisson-limit-and-where-exactness-stops
title: The Poisson limit, and the one number that can't be a fraction
thumb: Where exactness stops
---

@chapter Where Poisson comes from
@title text="The Poisson Limit, and Where Exactness Stops" sub="Markov Chains, Decisions and Queues" art=thumb
Every queue in this course assumed Poisson arrivals. So where do Poisson arrivals actually come from? And why is this the one place the arithmetic can't stay exact?

@art sliced-time
Cut one unit of time into n independent slots. Each one holds an arrival with probability lambda over n. Many small chances, none likely on its own, adding up to a fixed expected number. That's the shape of a lot of real arrival processes.

@math heading="The construction" items="count ~ Binomial(n, λ/n)@binomial;;mean = λ,  variance = λ(1 − λ/n)@with mean;;n → ∞:  P(k) → e^(−λ) λᵏ / k!@grows"
The count is binomial, with mean lambda whatever n is. Its variance is lambda times one minus lambda over n. As n grows with lambda fixed, the probabilities tend to e to the minus lambda, times lambda to the k, over k factorial. That's the Poisson distribution, whose variance equals its mean.

@chapter The exact column
@math heading="A recurrence, not the formula" items="P(0) = (1 − p)ⁿ@P of zero;;P(k+1) = P(k) · (n − k)/(k + 1) · p/(1 − p)@each next"
The binomial is computed as exact fractions, but not term by term. P of zero is one minus p, to the n. Each next term is the last one, times n minus k over k plus one, times p over one minus p.

@words text="λ = 3 · n = 40 · p = 3/40" sub="P(0) = (37/40)⁴⁰, over 65 digits"
Take lambda three with forty slots, so p is three fortieths. P of zero is thirty seven fortieths to the fortieth power: an exact fraction over a sixty five digit denominator.

@art bars-and-dots
Beside each exact bar sits the Poisson value. At three arrivals, the binomial is about point two three three, and the Poisson about point two two four. That's the biggest gap, about eight point nine thousandths.

@chapter The irrational column
@words text="e^(−λ) is irrational" sub="for every rational λ except 0"
And the Poisson column can't be exact. Every entry carries e to the minus lambda, which is irrational for every rational lambda except zero. No amount of care turns that into a fraction. So the page names the function, names the method, and prints the gap.

@words text="1 / (positive-term series for e^λ)"
The method matters too. The alternating series for e to the minus lambda can cancel away most of its digits. So it sums the all positive series for e to the lambda and inverts it at the end. Nothing cancels, and it's right to the rounding of a double.

@chapter The limit, measured
@art finer-slices
Now watch the word limit as a measurement. Keep lambda at three, and slice the same unit of time more and more finely.

@art shrinking-gap
At eight slots, the largest gap is nearly six percent. At forty, under one percent. At four hundred, under a thousandth. It falls roughly like one over n.

@math heading="Variance shortfall" items="λ(1 − λ/n) = 111/40@a hundred and eleven;;short of λ by λ²/n = 9/40@nine fortieths"
The variance gives the gap a name. At forty slots it's a hundred and eleven fortieths, short of three by exactly lambda squared over n, nine fortieths.

@words text="n = 400: P(0) over 1041 digits"
But more slots cost something. At four hundred, the exact P of zero has a denominator of a thousand and forty one digits. The approximation improves like one over n, and the exact fraction grows like n. That's a trade, not a fix.

@chapter Where the shape fails
@art wrong-shape
Set lambda eight with only twenty slots, so p is two fifths. That chance isn't small. The exact P of zero is about thirty seven millionths, against the Poisson's three hundred thirty five millionths. The variance is twenty four fifths against a mean of eight, so the shapes genuinely differ.

@art head-heavy
And at lambda a half, with twenty slots, over ninety one percent of the mass sits in the first two counts, and the columns differ by under six thousandths. That's where most arrival models live, and where the approximation is best.

@chapter Where people slip
@list heading="Common slips" items="Saying approximate without saying how@The first|Using Poisson when p isn't small@The second|Adding slots without noticing the cost@And the third"
The first slip is calling the Poisson column approximate without saying how. The second is using the Poisson shape when the chance per slot isn't small. And the third is pushing n up without noticing what the exact column costs.

@chapter Try it
@words text="λ = 3 · n = 120" sub="variance shortfall?"
Your turn. With lambda three and a hundred and twenty slots, find p, the variance, and how far it falls short of the mean. You should get a fortieth, a hundred seventeen fortieths, and three fortieths.

@end text="Measure the limit"
You can slide the number of slots and watch the exact column close on the Poisson, on Learn. That's learn dot get er done dot I O.
