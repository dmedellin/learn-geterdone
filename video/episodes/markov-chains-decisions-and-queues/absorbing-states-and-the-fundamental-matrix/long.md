---
format: long
lesson: markov-chains-decisions-and-queues/absorbing-states-and-the-fundamental-matrix
title: Absorbing chains and the fundamental matrix: how long, and where
thumb: N counts the visits
---

@chapter Chains that stop
@title text="Absorbing States and the Fundamental Matrix" sub="Markov Chains, Decisions and Queues" art=thumb
Some chains end. A gambler goes broke or hits a target. Two questions then: how long until it stops, and which way does it end? One matrix answers both.

@art gambler-line
A state is absorbing when the chance of staying is one, so the chain can never leave. That's a property of the matrix, not a label. Here's the lesson's gambler, with zero to four units, betting one at even odds. Zero and four are absorbing.

@words text="P[i][i] = 1" sub="checked, not declared"
So the lab checks it against the matrix you typed. Declare a state absorbing when its diagonal entry is three quarters, and it refuses. Calling that a boundary condition would produce numbers for a chain that doesn't actually stop there.

@chapter The blocks
@art canonical-blocks
Put the transient states first, and the matrix splits into blocks. Q goes from transient to transient. R goes from transient to absorbing. Then a zero block, and an identity.

@math heading="The fundamental matrix" items="N = (I − Q)⁻¹@fundamental matrix;;t = N·1@expected steps;;B = N·R@N times R"
The fundamental matrix N is the inverse of I minus Q. Then t, the row sums of N, gives the expected steps before absorption. And B, N times R, gives the probability of finishing in each absorbing state.

@chapter What N counts
@math heading="A sum of powers" items="N = I + Q + Q² + ⋯@I plus Q;;(I − Q)(I + Q + ⋯ + Qᵏ) = I − Qᵏ⁺¹@telescoping"
Usually N is introduced as an inverse. It's really a count. N is I plus Q plus Q squared, and so on. Multiply a partial sum by I minus Q and everything in between cancels, the same telescoping as a geometric series.

@art visit-counts
And Q to the k, entry i, j, is the chance of being at j after exactly k steps from i. Add those over every k, and you've counted the expected visits to j. That's what N means, counting the start.

@art partial-sums
On the gambler, the probability still wandering after k steps is one at the start, a half at step two, an eighth at step six, and one over a thousand twenty four at step twenty. Halving every two steps.

@chapter The gambler with four units
@math heading="N for the gambler" items="row 1:  3/2  1  1/2@three halves;;row 2:  1  2  1@one, two, one;;row 3:  1/2  1  3/2@a half"
Here's N. Row one: three halves, one, a half. Row two: one, two, one. Row three: a half, one, three halves. Starting at two, you're at two twice on average, counting the start. Starting at one, you're at one one and a half times. Those are counts of visits, which is why the row sums mean total steps.

@math heading="How long, and where" items="t = (3, 4, 3)@three, four, three;;from 1:  ruin 3/4, win 1/4@from one;;from 2:  1/2, 1/2@from two;;from 3:  1/4, 3/4@from three"
Add the rows: expected times three, four, three. Then B. From one, you're ruined three times in four. From two, it's even, as the symmetry says. From three, ruined once in four. Every row of B sums to one, and the page checks it.

@art biased-walk
Now tilt the odds: two thirds up, one third down. The expected times become seventeen fifths, eighteen fifths and eleven fifths. From the top transient state, you now finish at the far end fourteen times in fifteen. The drift shortens every journey and skews every destination, from the same N.

@chapter When there's no inverse
@art trapped-pair
Take this chain, and declare only the first state absorbing. States two and three trap each other, so absorption never happens. I minus Q is singular, and the lab says so. That means the model has a second closed class, often a transition that was left out.

@chapter Where people slip
@list heading="Common slips" items="Using N without asking what it counts@The first|Forgetting N counts the start@The second|Skipping the row sums of B@And the third"
The first slip is using N as a formula without asking what it counts. The second is forgetting that N includes the starting visit, which causes off by one disagreements. And the third is reporting absorption probabilities without checking that each row of B sums to one.

@chapter Try it
@words text="Gambler, up ⅔ · down ⅓" sub="find N, t and B"
Your turn. Set up Q and R for the biased gambler, invert I minus Q exactly, and check that you get the times seventeen fifths, eighteen fifths and eleven fifths, and B rows that each sum to one.

@end text="Count the visits"
You can slide the number of steps and watch the partial sums close on N, on Learn. That's learn dot get er done dot I O.
