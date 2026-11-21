---
format: long
lesson: simulation-and-variance-reduction/random-numbers-and-inverse-transform-sampling
title: Random numbers and inverse-transform sampling, in exact fractions
thumb: The table is the sampler
---

@chapter No randomness inside
@title text="Random Numbers and Inverse-Transform Sampling" sub="Simulation and Variance Reduction" art=thumb
Here's something surprising about simulation: there's no randomness in it. There's a recurrence, a seed, and a table. And that's exactly what makes a simulation useful.

@math heading="Linear congruential generator" items="xₙ₊₁ = (a·xₙ + c) mod m@x n plus one"
The recurrence is a linear congruential generator. x n plus one is a times x n plus c, mod m. The multiplier, the increment and the modulus fix the whole sequence, starting from a seed.

@art lcg-loop
So the seed is all of it. Fix the parameters and the seed, and every draw is determined. That makes a run reproducible and debuggable, and comparable with a second run. Its period, the number of values before it repeats, is at most m.

@math heading="a = 25173 · c = 13849 · m = 65536 · seed 1" items="39022, 61087, 20196, 45005@the first four;;U = 39022/65536 = 19511/32768@a fraction"
With the lesson's parameters, the first four integers are thirty nine thousand and twenty two, sixty one thousand and eighty seven, twenty thousand one hundred ninety six, and forty five thousand and five. Divide by m for U. The first is nineteen five eleven over thirty two seven sixty eight, a fraction, never a decimal.

@chapter The table is the sampler
@art cdf-bands
Now sampling. Take a distribution: values zero to four, with probabilities one, four, six, four and one sixteenths. Build the cumulative table: a sixteenth, five sixteenths, eleven sixteenths, fifteen sixteenths, one.

@art draw-lands
To sample, draw U and return the first value whose cumulative probability is above it. U lands in each band with probability equal to the band's width, which is that value's own probability. That's inverse transform sampling.

@words text="U < F(k)  ⇔  x·d < n·m" sub="whole numbers on both sides"
And the comparison is done in whole numbers. U less than n over d is the same as x times d less than n times m. Nothing becomes a decimal, so no rounding can decide a tie.

@art near-edge
That matters. The fourth draw, forty five thousand and five, is just fifty one short of the band edge at forty five thousand and fifty six. In integers, that's settled. In floating point, it comes down to the last bit.

@words text="One draw per value · monotone in U"
Two properties matter later. Each sampled value uses exactly one draw, which makes common random numbers possible. And a larger U never gives a smaller value, which is what antithetic variates stand on.

@chapter Periods
@words text="Full period ⇔ gcd(c, m) = 1 · primes of m divide a − 1 · 4 | m ⇒ 4 | a − 1"
A generator has full period from every seed exactly when c and m share no factor, every prime dividing m divides a minus one, and if four divides m, it divides a minus one too. This course quotes that condition and checks it.

@art short-cycle
Set a two, c four, m sixteen. From seed one the stream is six, zero, four, twelve, then twelve forever. All three conditions fail. The sampler returns two, zero, one, three, three, three. That's not a sample of anything. It's a dead stream with a frequency column that looks like data.

@chapter What the run produced
@math heading="200 draws" items="counts: 10, 42, 86, 49, 13@ten;;mean 413/200 = 2.065 · true 2@the mean;;largest gap 11/200, at value 2@eleven"
Two hundred draws give counts of ten, forty two, eighty six, forty nine and thirteen. The mean is four thirteen over two hundred, two point oh six five, against a true two. The largest gap is eleven two hundredths, at the value two. That's what two hundred draws look like, not an error.

@chapter Where people slip
@art uniform-shortcut
The first slip is the index shortcut: floor of k times U, plus one. It never looks at the probabilities, so it samples each of the five values a fifth of the time. The middle value is under sampled by seven fortieths, and no number of draws fixes it.

@list heading="Two more slips" items="Treating a short period as a small inaccuracy@The second|Storing U as a decimal@And the third"
The second slip is treating a short period as a small inaccuracy. It produces no sample at all. And the third is storing U as a decimal because the fraction is unreadable. Keep the fraction, and print a decimal beside it.

@chapter Try it
@words text="a = 2 · c = 4 · m = 16" sub="check all three conditions"
Your turn. Check the full period conditions for a two, c four, m sixteen, and say which fail. Then try a seed other than one and see whether the stream escapes twelve.

@end text="Let the table decide"
You can set your own generator and watch each draw land in its band, on Learn. That's learn dot get er done dot I O.
