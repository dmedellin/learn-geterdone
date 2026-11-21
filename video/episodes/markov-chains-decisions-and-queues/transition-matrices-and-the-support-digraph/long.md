---
format: long
lesson: markov-chains-decisions-and-queues/transition-matrices-and-the-support-digraph
title: Transition matrices: rows, arcs and n steps at once
thumb: Every row sums to one
---

@chapter More than a table
@title text="Transition Matrices and the Support Digraph" sub="Markov Chains, Decisions and Queues" art=thumb
A transition matrix looks like a square table of numbers. It's more specific than that, and getting it slightly wrong produces numbers that mean nothing at all.

@art matrix-rows
Entry i, j is the probability that the chain is at j next, given it's at i now. So every row is a probability distribution: where the chain goes next from that state. Entries are between zero and one, and every row sums to exactly one.

@words text="Memoryless" sub="the next step depends only on where you are now"
And the chain is memoryless. The row used at each step depends on the current state, and on nothing earlier.

@chapter Check every row
@art two-state-weather
Here's the lesson's two state chain, fine and wet. From fine, it's a half and a half. From wet, a quarter to fine and three quarters to wet. Both rows sum to one, so this is a chain.

@art bad-row
Now type one half, one quarter in the first row. It sums to three quarters. The lab stops and names the row. Everything would still compute, but it would describe a chain that vanishes a quarter of the time, and that isn't a Markov chain.

@words text="Check each row, not the total"
And check row by row. One row over by a quarter and another under by a quarter gives the right total, and it still isn't a chain.

@chapter The digraph
@art support-digraph
From the matrix you can draw the support digraph. Draw an arc from i to j exactly when the entry is positive. An arc of one in a thousand is as much an arc as one of a half. The digraph is about which, not how much.

@chapter Distributions move on the left
@math heading="One step" items="(vP)ⱼ = Σᵢ vᵢ · P[i][j]@the chance"
A distribution is a row vector, and you multiply it on the left. Read the sum aloud: the chance of being at j next is the chance of being at each i now, times the chance of stepping from i to j, added over every i.

@art left-multiply
That's why the steady state solves pi P equals pi, as a left eigenvector. If you've met eigenvectors as columns, notice the transpose. P times v is a fine product. It's just not the next distribution.

@math heading="Start certainly fine" items="step 0:  (1, 0)@step zero;;step 1:  (1/2, 1/2)@step one;;step 2:  (3/8, 5/8)@step two;;step 3:  (11/32, 21/32)@step three"
Start certainly fine. Step zero is one, zero. Step one, a half and a half. Step two, three eighths and five eighths. Step three, eleven thirty seconds and twenty one thirty seconds.

@chapter Powers of P
@math heading="Powers compose" items="P^(m+n) = Pᵐ · Pⁿ@m plus n;;Pⁿ[i][j] = P(at j after n steps | from i)@n steps at once"
And P to the m plus n is P to the m times P to the n. To go from i to j in m plus n steps, the chain is at exactly one state k at step m. Add over k, and that's the matrix product. So P to the n is n steps at once.

@art bars-settle
Push the step count up, and the bars stop moving long before the fractions stop growing. Those are two different facts, and only one of them is about probability.

@chapter Where decimals fail
@words text="203244268876273 / 1024000000000000" sub="one entry of P¹²"
The five state example has every entry over twenty. By the twelfth power, numerators are fifteen digits long, over sixteen digit denominators. That's past what a double can hold, so a decimal would store a nearby number and call it the answer.

@chapter Where people slip
@list heading="Common slips" items="Checking the total, not each row@The first|Treating small arcs as zero@The second|Multiplying on the wrong side@And the third"
The first slip is checking that the whole matrix sums to n instead of each row. The second is treating a tiny probability as zero, which changes the structure, not just the precision. And the third is multiplying the distribution on the wrong side.

@chapter Try it
@words text="1/2 1/2 ; 1/4 3/4" sub="compute steps 4 and 5 from (1, 0)"
Your turn. Push the fine and wet chain two more steps by hand. You should get forty three over one twenty eight, then one seventy one over five twelve, for fine. Then try the starting distribution one, one, and say why it's refused.

@end text="Check every row, then take the steps"
You can type your own matrix, see its digraph, and take n steps at once in exact fractions, on Learn. That's learn dot get er done dot I O.
