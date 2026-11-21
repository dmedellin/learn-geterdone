---
format: long
lesson: randomised-algorithms/where-the-7m-8-argument-stops
title: When 7m/8 is wrong: the hypothesis hiding in a closed form
thumb: Keep the sum, not the formula
---

@chapter One changed clause
@title text="Where the 7m/8 Argument Stops" sub="Randomised Algorithms" art=thumb
Seven m over eight is a closed form, and a closed form has hypotheses. Change one clause, and a correct formula quietly becomes a wrong one.

@art repeated-literal
Start from last lesson's four clauses and change one. x one or not x two or x three becomes x one or x one or x two. It's still three literals. It's still a legal clause. It looks like every other clause on the page. But it isn't on three distinct variables, and that was a hypothesis.

@chapter Width and variables
@words text="width 3 · distinct variables 2"
A clause has a width, how many literals it contains, and a count of distinct variables, how many different variables those literals mention. Usually they're equal. Here the width is three and there are two variables. It's the second number that decides the clause's share.

@math heading="A clause on d distinct variables" items="P(satisfied) = (2ᵈ − 1)/2ᵈ@two to the d;;d = 3:  7/8@seven eighths;;d = 2:  3/4@three quarters"
A clause on d distinct variables, with no variable appearing both plain and negated, is satisfied with probability two to the d minus one, over two to the d. Exactly one setting of its variables makes every literal false. For three variables that's seven eighths. For two, it's three quarters.

@art four-squares
And if a clause contains a variable and its negation, like x one or not x one, it's satisfied by everything, with share one. The lab gets that right too, because it enumerates each clause over its own variables instead of applying a formula.

@chapter Clause by clause
@math heading="The edited formula" items="x₁ ∨ x₂ ∨ ¬x₃:  7/8@first;;¬x₁ ∨ x₂ ∨ x₃:  7/8@second;;x₁ ∨ x₁ ∨ x₂:  3/4@third;;¬x₂ ∨ ¬x₃ ∨ ¬x₁:  7/8@fourth;;total 27/8  ≠  7m/8 = 7/2@the total"
Clause by clause. The first is seven eighths. The second, seven eighths. The third has two variables, so three quarters. The fourth, seven eighths. The total is twenty seven eighths, and enumerating all eight assignments gives twenty seven eighths too. But seven m over eight says seven halves.

@art sum-bars
Lay the four shares end to end and you can see it.

@words text="27/8 = 3.375 · 7/2 = 3.5" sub="short by exactly 1/8"
The gap is one eighth, exactly how much the third clause fell short. Nothing subtle happened. One term in a sum of four was smaller than assumed, and the sum was smaller by precisely that much.

@chapter Linearity didn't fail
@art clause-table
So linearity of expectation didn't fail. It's unconditional, and the shares still add up to the mean, exactly. What failed was a substitution: replacing every term with seven eighths. The hypothesis stopped holding while the formula kept being applied. The panel prints does not agree, and colours the clause that did it.

@chapter What still holds
@list heading="On the edited formula" items="Some assignment satisfies ⌈27/8⌉ = 4@the ceiling|Distribution: one gives 2, three give 3, four give 4@one assignment|Ratio: (27/8)/4 = 27/32 ≈ 0.844@the ratio"
The existence argument survives in its general form. Some assignment satisfies at least the ceiling of twenty seven eighths, which is four, and the optimum is indeed four. The shape changed too: one assignment satisfies only two, three satisfy three, and four satisfy four. And the ratio, against that optimum of four, is twenty seven thirty seconds, about point eight four four.

@art distribution-shift
The measured mean moved with it: over a hundred and twenty coin flips, three point three, against an exact mean of three point three seven five. The algorithm didn't change. The instance did, and it's outside the class the seven eighths guarantee was about.

@art preprocess
The honest fix is cheap. x one or x one or x two is just x one or x two. Keep the general bound, the sum of each clause's share. It's weaker for smaller clauses, three quarters instead of seven eighths, and it's correct.

@chapter Keep the sum
@words text="Σⱼ P(clause j satisfied)" sub="right for every formula"
So here's the habit. Keep the sum before you collapse it. The sum over clauses of each clause's chance of being satisfied is right for every formula. It costs one row per clause, and turns into seven m over eight by itself when the hypothesis holds.

@chapter Where people slip
@list heading="Common slips" items="Blaming linearity@The first|Counting literals, not variables@The second|Carrying a ratio outside its class@And the third"
The first slip is blaming linearity, the one step where nothing is wrong. The second is counting literals instead of distinct variables. A parser that checks width alone accepts exactly the formulas that break the bound. And the third is quoting the seven eighths ratio on an instance outside its class.

@end text="Keep the sum before you collapse it"
Edit a clause and watch the table name the culprit, on Learn. That's learn dot get er done dot I O.
