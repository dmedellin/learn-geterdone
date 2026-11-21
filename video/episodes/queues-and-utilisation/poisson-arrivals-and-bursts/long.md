---
format: long
lesson: queues-and-utilisation/poisson-arrivals-and-bursts
title: Poisson arrivals and bursts: sizing for the tail, not the mean
thumb: A rate is not a schedule
---

@chapter The question
@title text="Poisson Arrivals and Bursts" sub="Queues and Utilisation" art=thumb
A thousand requests a second. Does that mean a thousand in every second? No. It's a mean, not a schedule. Consecutive seconds vary by tens without anything going wrong. So how much does a window really have to hold?

@art seconds-vary
Picture a thousand a second as a row of seconds. Each one carries a slightly different count, some above a thousand and some below. That's ordinary, not an incident.

@art window-chopped
Fix a window, and let m be the expected number of arrivals in it. Now chop the window into n equal opportunities, each carrying one arrival with probability m over n. The count is binomial, and its mean is exactly m.

@math heading="Binomial, then Poisson" items="P(X = k) = C(n, k)(m/n)ᵏ(1 − m/n)ⁿ⁻ᵏ@binomial;;n → ∞:  P(X = k) = e^(−m) mᵏ / k!@as n grows"
The binomial gives the chance of exactly k arrivals. As n grows, it converges to the Poisson count: e to the minus m, times m to the k, over k factorial. The binomial is exact arithmetic at any n. The Poisson is the shape it's heading for.

@chapter Ten expected
@math heading="m = 10,  n = 200 chances of 1/20" items="P(count > 15): binomial 0.0443556@binomial;;P(count > 15): Poisson 0.0487404@Poisson limit;;variance: 10 · 19/20 = 9.5  vs  10@the variance"
Expect ten in the window, chopped into two hundred chances of one in twenty. The binomial chance of more than fifteen is nought point nought four four three five five six. The Poisson limit says nought point nought four eight seven four nought four. And the variance is nine and a half for the binomial, and ten for the Poisson.

@art two-histograms
The difference isn't noise. A chopped window can hold at most n arrivals, while a Poisson count has no upper bound at all. Chop finer and the two converge. For the Poisson, the variance equals the mean.

@chapter Sizing for a burst
@art overflow-tail
The design question is rarely what the mean is. It's how much this window must hold so it overflows no more than one time in a hundred. That's a tail: the smallest capacity C with the chance of exceeding it at or below the target.

@art capacity-bucket
Think of the window as a bucket with a fixed size. Whatever arrives beyond that size spills over.

@math heading="m = 10" items="P(count > C) ≤ 1/100  →  C = 18@one window in a hundred;;P(count > C) ≤ 1/1000  →  C = 21@one in a thousand;;C = 10:  P(count > 10) ≈ 0.42@at the mean"
With ten expected, overflowing at most one window in a hundred needs a capacity of eighteen, eighty percent over the mean. One in a thousand needs twenty one. And a window sized at the mean, ten, overflows with probability about nought point four two. That's two windows in five.

@words text="headroom isn't a margin on the number; it is the number"
So sizing at the mean isn't conservative or even neutral. Headroom isn't a safety margin bolted onto a correct number. It is the number, and the target overflow fraction sets it. The three extra arrivals between fifteen and eighteen take you from four point four percent overflow down to one.

@chapter Big streams are smoother
@math heading="Spread = √m" items="m = 1000:  1000 ± 32@a thousand;;m = 10:  10 ± 3.2@ten"
Variance equals the mean, so the spread is the square root of m. A thousand a second has a standard deviation of about thirty two, a three percent wobble. Ten a second has about three point two, a thirty two percent wobble.

@art pooled-streams
So consolidating ten small streams into one big one doesn't change the mean load, but it does reduce the relative burstiness. That's a first look at the pooling argument that comes later in this course.

@chapter Where people slip
@list heading="Common slips" items="Reading a rate as a schedule@The first|Sizing a window at the mean@The second|Treating Poisson as the exact column@The third"
The first slip is reading a thousand a second as a thousand in each second. Seconds of ten fifty or nine forty are ordinary. The second is sizing a window at the mean. And the third is reading the Poisson column as exact. It's the limit, and here a rounded series as well.

@chapter Try it
@words text="m = 5 · target: 1 window in 100" sub="answer is above 5; relative headroom larger than at m = 10"
Your turn. Keep the target at one window in a hundred, and set m to five. The capacity must be above five, and the relative headroom will be larger than at ten, because the spread scales as the square root of m and the mean doesn't. Predict the capacity, then read it off.

@end text="Size the window for its tail"
You can set the expected count and the target and watch the binomial and Poisson tails, on Learn. That's learn dot get er done dot I O.
