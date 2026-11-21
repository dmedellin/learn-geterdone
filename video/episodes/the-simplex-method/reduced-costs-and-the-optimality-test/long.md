---
format: long
lesson: the-simplex-method/reduced-costs-and-the-optimality-test
title: Reduced costs: why the steepest column isn't the best one
thumb: Rate times step
---

@chapter The question
@title text="Reduced Costs and the Optimality Test" sub="The Simplex Method" art=thumb
At each corner, the simplex method asks two things. Which column should come in? And can I stop? Both answers are written in the objective row.

@art price-row
For a nonbasic column, its entry in the objective row is a rate. If that variable rises by one unit, and every basic variable adjusts to keep the equations true, how much does z change? It changes by minus that entry.

@chapter Reduced cost
@math heading="Reduced cost" items="z_j = c_Bᵀ B⁻¹ A_j − c_j@c j;;improving (maximise):  z_j < 0@negative;;rate = −z_j@the rate"
The reduced cost of column j is c B transpose, B inverse, A j, minus c j. Here c j is what one unit earns directly, and the other term is what the basic variables give up to make room for it. For a maximisation, a negative reduced cost is improving, and the rate is minus z j.

@words text="Initial tableau: z_j = −c_j"
In the first tableau of an at most programme, the basis is the slacks and their costs are zero. So the reduced costs are just the negated objective coefficients. That's a special case, not the definition.

@chapter Choosing a column
@list heading="Entering rules" items="Dantzig: most negative reduced cost@Dantzig's rule|Bland: lowest-index improving column@Bland's rule|Greatest improvement: largest rate × step@greatest improvement"
Any improving column may enter. Dantzig's rule takes the most negative reduced cost. Bland's rule takes the lowest index improving column. Greatest improvement works out the step for every improving column, and takes the largest rate times step. They all reach the same optimal value. They differ in the path.

@art three-rules
Every rule ends at the same optimal value when it ends at all. What changes is how many corners it stands at on the way.

@chapter Steepest isn't best
@math heading="max 5x₁ + 9x₂ + 3x₃" items="3x₁ + 2x₂ ≤ 20@twenty;;x₁ + 3x₂ ≤ 12@twelve;;4x₁ + 4x₂ + x₃ ≤ 20@plus x three"
Take maximise five x one plus nine x two plus three x three. Subject to three x one plus two x two at most twenty, x one plus three x two at most twelve, and four x one plus four x two plus x three at most twenty.

@math heading="At the origin:  rate × step" items="x₁:  5 × 5 = 25@twenty five;;x₂:  9 × 4 = 36@thirty six;;x₃:  3 × 20 = 60@sixty"
At the origin the rates are five, nine and three. The ratio test allows steps of five, four and twenty. So x one moves z by twenty five. x two, the steepest, moves it by thirty six. And x three, with a third of the rate, moves it by sixty, which is the entire optimum.

@art rate-bars
Put the two numbers side by side. The rate is how steep a column is. The step is how far the ratio test lets it run. The improvement is the product, and the tallest rate isn't attached to the longest step.

@words text="Pivots to z* = 60" sub="Dantzig 3 · Bland 4 · greatest improvement 1"
Dantzig's rule takes x two and needs three pivots. Bland's rule needs four. Greatest improvement takes x three and needs just one.

@art steep-vs-long
So why does anyone use Dantzig's rule? Because it's cheap. Greatest improvement costs a ratio test per column, every pivot. On a real problem, that's more arithmetic than the extra pivots it saves. It's a cheap approximation to what you want.

@chapter Stopping
@words text="Every z_j ≥ 0  →  optimal"
Here's the optimality test. If every reduced cost in a feasible tableau is at least zero, the corner it reads is optimal.

@art corner-to-region
Separate the two halves. That no edge out of this corner improves z is arithmetic on one row. That no point in the whole region improves it is the convexity result. Quote that when you stop. A tableau alone only tells you about its own corner.

@chapter Minimising
@math heading="minimise 2x₁ − 3x₂" items="x₁ + x₂ ≤ 8,  2x₁ + x₂ ≤ 10@at most eight;;internal: maximise −2x₁ + 3x₂@maximise minus;;objective row starts (2, −3)@two, minus three;;tableau reads 24 → answer −24@minus twenty four"
To minimise, maximise the negative and flip the answer. Take minimise two x one minus three x two, with x one plus x two at most eight, and two x one plus x two at most ten. Internally, you maximise minus two x one plus three x two. The objective row starts at two, minus three. One pivot brings x two in at eight, the tableau reads twenty four, and the answer is minus twenty four.

@art sign-flag
Nothing about the test flips. Only the sign you report. So write down your convention before the first pivot. And a zero reduced cost on a nonbasic column means a tie: another corner with the same value.

@chapter Where people slip
@list heading="Common slips" items="Most negative means biggest improvement@The first|Flipping the test for a minimisation@The second|Optimality as a property of the tableau@The third"
The first slip is believing the most negative reduced cost gives the biggest improvement. It gives the biggest rate. The second is expecting the stopping test to flip on a minimisation. And the third is reporting optimality as just a property of the tableau, rather than a proof that uses convexity.

@end text="Compare the entering rules"
You can run each entering rule on the same programme and count the pivots, on Learn. That's learn dot get er done dot I O.
