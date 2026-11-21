---
format: long
lesson: duality-and-sensitivity-analysis/parametric-objectives-and-the-pareto-front
title: Two objectives, no single optimum: the Pareto front, exactly
thumb: The weights are the decision
---

@chapter The question
@title text="Parametric Objectives and the Pareto Front" sub="Duality and Sensitivity Analysis" art=thumb
What if you have two objectives that pull in different directions? There's no single best answer. But there is a short list of answers worth considering, and you can compute it exactly.

@chapter A weighted sum
@math heading="Weight λ on the second objective" items="maximise (1 − λ)f₁ + λf₂@one minus lambda;;λ = 0:  f₁ alone@lambda equals zero;;λ = 1:  f₂ alone@lambda equals one"
Maximise one minus lambda times f one, plus lambda times f two. At lambda equals zero, you're maximising f one alone. At lambda equals one, f two alone. Everything between is a trade.

@art jumping-corner
And the answer doesn't change smoothly. The chosen corner stays fixed over an interval of weights, then jumps to the next one.

@words text="Reduced costs: a + λ(b − a)"
Why? Fix a basis. Every reduced cost is a plus lambda times b minus a, where a and b are that column's reduced costs under each objective alone. That's linear in lambda. So each basis owns an interval of weights, and a breakpoint is where some reduced cost hits exactly zero.

@chapter The example
@math heading="The region and objectives" items="x₁ ≤ 8,  x₁ + x₂ ≤ 10,  2x₁ + x₂ ≤ 16@at most eight;;3x₁ + 2x₂ ≤ 24,  3x₁ + x₂ ≤ 21@twenty four;;f₁ = 4x₁ + x₂,   f₂ = x₁ + 4x₂@f one"
Here's the region. x one at most eight, x one plus x two at most ten, two x one plus x two at most sixteen, three x one plus two x two at most twenty four, and three x one plus x two at most twenty one. The objectives are f one, four x one plus x two, and f two, x one plus four x two.

@math heading="The sweep" items="0 to 1/12:  (7, 0),  scores (28, 7)@seven, zero;;1/12 to 1/3:  (6, 3),  scores (27, 18)@six, three;;1/3 to 1/2:  (4, 6),  scores (22, 28)@four, six;;1/2 to 1:  (0, 10),  scores (10, 40)@zero, ten"
Sweep lambda. Up to one twelfth, the answer is seven, zero, scoring twenty eight and seven. Then six, three, scoring twenty seven and eighteen, up to one third. Then four, six, scoring twenty two and twenty eight, up to a half. Then zero, ten, scoring ten and forty.

@math heading="First breakpoint" items="28 − 21λ = 27 − 9λ@twenty eight minus;;1 = 12λ@one equals;;λ = 1/12@one twelfth"
Each breakpoint is where two corners score the same weighted total. Seven, zero scores twenty eight minus twenty one lambda. Six, three scores twenty seven minus nine lambda. Set them equal: one equals twelve lambda, so lambda is one twelfth. The others, one third and a half, come the same way.

@art grid-miss
Here's why you compute them. Lambda point oh eight picks seven, zero, and point oh nine picks six, three. A slider in hundredths never lands on one twelfth. And a corner whose interval is shorter than the grid could be missed entirely.

@chapter Efficient points
@art front-staircase
A point is efficient when no feasible point is at least as good on both objectives, and strictly better on one. The set of efficient points is the Pareto front. All four corners here are efficient.

@math heading="A smaller region" items="front:  (8, 0),  (6, 4),  (4, 6)@the front;;(0, 6) scores (6, 18)@zero, six scores;;(4, 6) scores (18, 22)  →  beats it on both@beats it"
On a smaller region, with f one three x one plus x two, and f two x one plus three x two, the front is eight, zero, then six, four, then four, six. The corner zero, six scores six and eighteen. But four, six scores eighteen and twenty two, which beats it on both. So zero, six isn't on the front.

@art dominated-corner
Reachable isn't the same as worth considering. A point that isn't efficient is one nobody should choose under any weights at all.

@chapter The weights are the decision
@art weights-outside
A two objective problem doesn't have an optimum. The weights aren't a technical detail on the way to one. They are the decision, made outside the model, by whoever is entitled to make it. What the mathematics delivers is the front, with the exact weight where each corner takes over.

@art sweep-slider
And in a linear programme, every efficient point is a combination of efficient corners, so the corners describe the whole front. That stops being true for integer problems.

@chapter Where people slip
@list heading="Common slips" items="Treating it as having one optimum@The first|Sweeping the weight on a grid@The second|Confusing reachable with efficient@The third"
The first slip is treating a two objective problem as having an optimum. The second is sweeping the weight on a grid and reporting what turns up. And the third is confusing a reachable corner with an efficient one.

@end text="Sweep the weight, read the front"
You can sweep the weight and see each exact breakpoint and the front, on Learn. That's learn dot get er done dot I O.
