---
format: long
lesson: ethics-and-welfare/priority-equality-and-levelling-down
title: Priority vs equality: the levelling down test
thumb: More equal, better for no one?
---

@chapter The question
@title text="Priority, Equality and Levelling Down" sub="Ethics and Welfare" art=thumb
Plenty of views say we should favour the worse off. But there are two quite different reasons you might do that. One weights people by how low they start. The other cares about the gap between people. And one simple case pulls them apart.

@chapter A priority rule
@art bent-curve
A priority rule gives a gain more weight the lower the recipient starts. Here's the simplest version. Choose a knee. Welfare counts in full up to the knee, and only half of what lies above it counts.

@art knee-slider
That's the simplest weighting with the right shape. A unit of welfare counts for less, the more a person already has. A smoother curve would shift the numbers, but keep the structure.

@math heading="Prioritarian weighting" items="g(x) = x  for x ≤ knee@counts in full;;g(x) = knee + (x − knee)/2  above@above the knee;;score = sum of g over everyone@the score"
So g of x is x, up to the knee, and it counts in full. Above the knee, g is the knee plus half the excess. The score of a distribution is the sum of g over everyone. The knee is a parameter you move, not a fact.

@math heading="Knee at 8" items="A = 6, 14:  g = 6, 11,  score 17@A is six;;B = 9, 9:  g = 17/2 each,  score 17@B is nine;;totals 20 and 18, yet a tie@a tie"
With the knee at eight, A is six and fourteen. Six counts in full, and fourteen becomes eight plus three, eleven. The score is seventeen. B is nine and nine, and each becomes seventeen halves, so its score is seventeen too. It's a tie, even though the totals are twenty and eighteen.

@chapter Measuring the spread
@art spread-dots
An equality rule looks instead at the spread. The Gini coefficient adds the gaps between every ordered pair of people, then divides by two times n squared times the mean. It's zero when everyone has the same, and grows as welfare spreads out.

@math heading="Gini of 1, 30, 2" items="gaps: 29, 1, 28@the gaps;;ordered sum: 116@counting both orders;;divisor: 2 · 9 · 11 = 198@the divisor;;Gini = 58/99@fifty eight"
For one, thirty and two, the gaps are twenty nine, one and twenty eight. Counting both orders gives a hundred and sixteen. The divisor is two times nine times eleven, a hundred and ninety eight. So the Gini is fifty eight over ninety nine.

@chapter Blind to the level
@art equal-low-high
Here's what the Gini doesn't measure. Ten, ten, ten and five, five, five both have a Gini of zero. So a rule that ranks by inequality alone has no preference between them. Priority prefers the tens, twenty seven to fifteen, because everyone is better off.

@chapter Levelling down
@art levelling-down
Now the case that separates the views. In levelling down, the better off are brought down to the worst off, and no one gains. A is ten and two. B is two and two.

@math heading="A = 10, 2  vs  B = 2, 2" items="Gini:  A 1/3,  B 0  → B wins@one third;;priority:  A 11,  B 4  → A wins@eleven;;no one is better off under B@no one"
A has a Gini of one third, and B has zero. Ranked by inequality alone, B wins. Priority scores A at eleven and B at four, and prefers A. And no one is better off under B. The person at two stays at two, and the person at ten is worse off.

@words text="Equality: one good among several?" sub="worse all things considered, better in one respect"
That's the levelling down objection. The egalitarian has a reply. Equality is one good among several, so a levelled outcome can be worse all things considered, while still better in that one respect. The lab ranks by one thing at a time, and can't say how to combine them.

@chapter Where people slip
@list heading="Common slips" items="Treating priority as egalitarianism@The first|Reading a Gini of 0 as a good outcome@The second|Taking the knee as a fact@And the third"
The first slip is treating priority as egalitarianism. Priority weights a person's level, not the gap. The second is reading a Gini of zero as a good outcome. Everyone at five has the same Gini as everyone at ten. And the third is taking the knee as a fact. Move it, and the tie moves with it.

@chapter Try it
@art two-scales
Rework the example yourself. Knee at eight, A is six and fourteen, B is nine and nine. Weight each number, add them, then compute both Ginis. The answers are one fifth for A, and zero for B. Then say which rule prefers which.

@end text="Weight the worse off"
You can move the knee and watch the scores change, on Learn. That's learn dot get er done dot I O.
