---
format: long
lesson: randomised-algorithms/repetition-and-the-probability-it-buys
title: How many times should you rerun a randomised algorithm?
thumb: Failures multiply
---

@chapter A bad single run
@title text="Repetition, and the Probability It Buys" sub="Randomised Algorithms" art=thumb
An algorithm that's right only thirty seven per cent of the time isn't useful. Run it a few times, though, and it can be. Here's exactly how many times.

@art bridge-graph
The lab's hardest graph is two triangles joined by a single edge, the bridge from three to four. Six vertices, seven edges, and a unique minimum cut of one edge. That one edge has to survive all four contractions.

@words text="p = 13/35 ≈ 0.371" sub="120 seeds: 41 hits, 79 misses"
It does with probability thirteen thirty fifths, about point three seven one. Over a hundred and twenty seeds, Karger's algorithm succeeded forty one times and missed seventy nine. The very first seed missed, returning a cut of two edges.

@chapter Failures multiply
@art independent-runs
Run it t times, with independent randomness, and keep the smallest cut any run returned. The kept answer is wrong only if every run was wrong. Independent failures multiply.

@math heading="Amplification" items="P(all t fail) ≤ (1 − p)ᵗ@all t runs fail;;P(success) ≥ 1 − (1 − p)ᵗ@one minus;;bridge:  1 − (22/35)ᵗ@twenty two"
So all t runs fail with probability at most one minus p, to the t. Success is at least one minus that. On the bridge graph, that's one minus twenty two thirty fifths, to the t. Each extra run multiplies the failure by twenty two thirty fifths. Failure shrinks geometrically, while the work grows linearly.

@chapter The table
@art failure-decay
Here's what that looks like, run by run. Every bar is the last one times twenty two thirty fifths. The panel prints each as an exact fraction, with a decimal beside it.

@math heading="Bridge graph" items="t = 1:  0.371429@one run;;t = 2:  741/1225 ≈ 0.605@two runs;;t = 5:  0.901876@five runs;;t = 10:  0.990372@ten runs"
One run, point three seven one. Two runs, seven forty one over twelve twenty five, about point six oh five. Five runs, point nine oh one eight seven six. Ten runs, point nine nine oh three seven two.

@list heading="Smallest t" items="9/10:  5 runs@nine tenths|99/100:  10 runs@ninety nine hundredths|999/1000:  15 runs@nine nine nine"
So the smallest t to reach nine tenths is five. For ninety nine hundredths, ten. For nine nine nine thousandths, fifteen. The panel finds each by multiplying until the failure drops below target, not by taking a logarithm.

@words text="ln(100)/p ≈ 12.4" sub="exact answer: 10"
Why not use the logarithm estimate? Because at these sizes it's off. The log of a hundred over p gives about twelve point four, suggesting thirteen runs where ten suffice. That's thirty per cent more work.

@chapter An easier graph
@art two-edge-graph
Switch to two triangles joined by two edges, where one run succeeds nineteen thirty fifths of the time. Now three runs reach nine tenths, six reach ninety nine hundredths, and nine reach nine nine nine thousandths. Compare five, ten, fifteen. Roughly halve p, and you roughly double the runs. And on the four cycle, p is one, so one run always does.

@chapter What it doesn't buy
@art one-sided
Keeping the best answer only works if a wrong answer is never better than a right one. Karger's algorithm always returns a genuine cut, so a smaller cut is always better. If an algorithm could err in both directions, the best of t answers would be the most extreme error, and repetition would make it worse.

@art shared-seed
Independence is a hypothesis, and it's the one a real implementation most often breaks. The generator behind every lab on this course is a prime modulus stream with a mixed seed for exactly that reason.

@list heading="Repetition never buys" items="Certainty: no finite t reaches 1@Certainty|Help for runs that share randomness@share randomness|Two-sided error turned one-sided@two sided"
It never buys certainty: fifteen runs give about point nine nine nine one, not one. It doesn't help if runs share randomness, through a reused seed, or seeds derived from one another so they're correlated. And it doesn't turn a two sided error into a one sided one. Next lesson, a primality test with the same structure.

@chapter Where people slip
@list heading="Common slips" items="Adding success probabilities@The first|Amplifying a two-sided error@The second|Trusting the logarithm@And the third"
The first slip is adding success probabilities. Ten times thirteen thirty fifths is more than three, which isn't a probability. Failures multiply. The second is amplifying an algorithm whose error goes both ways. And the third is trusting the logarithm estimate without checking it.

@end text="Failures multiply"
Pick a target and find the exact number of runs on Learn. That's learn dot get er done dot I O.
