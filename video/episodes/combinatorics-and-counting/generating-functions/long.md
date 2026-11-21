---
format: long
lesson: combinatorics-and-counting/generating-functions
title: Generating functions: counting by multiplying series
thumb: Multiply series, combine choices
---

@chapter A sequence in one object
@title text="Generating Functions" sub="Combinatorics and Counting" art=thumb
Here's a trick that turns counting problems into algebra. Take a whole counting sequence, a zero, a one, a two, and so on, and pack it into a single power series.

@math heading="Ordinary generating function" items="G(x) = a₀ + a₁x + a₂x² + ⋯ = Σ aₖxᵏ@G of x equals"
G of x equals a zero, plus a one times x, plus a two times x squared, and so on. The coefficient of x to the k is the count for size k. The whole sequence travels together.

@art coefficient-shelf
The series is formal. x never takes a value, and convergence doesn't matter. It's a bookkeeping symbol, and the series is a way of writing an infinite sequence. Each coefficient of a product depends on only finitely many others, so the algebra is always well defined.

@chapter The basic series
@math heading="Series to know" items="1/(1 − x) = 1 + x + x² + ⋯@One over one minus x;;(1 + x)ⁿ = Σ C(n, k) xᵏ@binomial coefficients;;1/(1 − x)ⁿ = Σ C(n + k − 1, k) xᵏ@stars and bars;;1 + x + ⋯ + xᵐ@at most m copies"
One over one minus x is one plus x plus x squared, and so on: any number of one type. One plus x, to the n, has the binomial coefficients: at most one of each type. One over one minus x, to the n, has the stars and bars counts. At most m copies is one plus x, up to x to the m.

@chapter Multiplying combines choices
@art two-sources-merge
Why multiply? If A of x counts ways to pick from one source, and B of x from another, then the coefficient of x to the k in their product sums over every split. Take j from the first source and k minus j from the second. That's the product rule and the sum rule, together.

@words text="multiply series ⟷ combine independent choices"
So each source contributes a factor, and the coefficients of the product count the combined selections.

@chapter Making change
@art coin-stacks
In how many ways can you make n cents from pennies, nickels and dimes? Each coin contributes one factor: one over one minus x for pennies, one over one minus x to the fifth for nickels, and one over one minus x to the tenth for dimes.

@art series-factors
The nickel factor only has powers that are multiples of five, because nickels come in fives, and the dime factor only multiples of ten. The answer for n cents is the coefficient of x to the n in the product.

@math heading="Making 25 cents" items="0 dimes: 0 to 5 nickels → 6 ways@no dimes;;1 dime: 0 to 3 nickels → 4 ways@one dime;;2 dimes: 0 to 1 nickel → 2 ways@two dimes;;6 + 4 + 2 = 12@Twelve"
For twenty five cents, split by dimes. With no dimes, zero to five nickels: six ways. With one dime, fifteen cents left: four ways. With two dimes, five cents left: two ways. Twelve in all. Extracting the coefficient amounts to exactly this case split.

@chapter Constraints live in the factors
@art capped-supply
How many ways are there to choose ten items from four types, with at most three of each? Each type contributes one plus x plus x squared plus x cubed. You want the coefficient of x to the tenth in that, raised to the fourth power.

@math heading="10 from 4 types, at most 3 each" items="[x¹⁰] (1 + x + x² + x³)⁴ = 10@Expanding gives ten;;check: 2 short of 12, over 4 types: C(5, 2) = 10@short of the maximum"
Expanding gives ten. Check it another way. A selection is short of the maximum, twelve, by two, spread over four types. Stars and bars counts those spreads as C of five, two, which is ten.

@chapter Solving a recurrence
@art recurrence-growth
Generating functions also solve recurrences. Take a n equals three times a n minus one, with a zero equal to one.

@math items="G(x) − 1 = 3x G(x)@G of x minus one;;G(x) = 1/(1 − 3x)@one over one minus three x;;aₙ = 3ⁿ@three to the n"
Multiply the recurrence by x to the n, and sum. You get G of x minus one equals three x times G of x. So G of x is one over one minus three x, whose coefficients are three to the n. With partial fractions, the same method recovers the Fibonacci formula.

@chapter Where people slip
@list heading="Common slips" items="Worrying about convergence@The first|Using the wrong factor for a constraint@The second|Using them on a small problem@The third"
The first slip is worrying about convergence; these are formal series. The second is using the wrong factor. At most m is a polynomial with m plus one terms, and multiples of d is one over one minus x to the d. The third is using them on a small problem. They pay off when you need every n at once.

@chapter Try it
@words text="pennies, nickels, quarters, at most 3 of each" sub="find the coefficient for n = 30"
Your turn. Write the generating function for making n cents from pennies, nickels and quarters, with at most three of each. Then extract the coefficient for thirty cents. The factors are where the constraints live.

@end text="Attach a constraint, watch the count change"
You can attach a constraint like at most three of each, and watch the count change, on Learn. That's learn dot get er done dot I O.
