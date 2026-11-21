---
format: long
lesson: the-simplex-method/the-ratio-test
title: The ratio test: how far can the entering variable go?
thumb: Only positive entries count
---

@chapter The question
@title text="The Ratio Test" sub="The Simplex Method" art=thumb
You've chosen a column to enter the basis. Now which row leaves? Pick wrong and the tableau happily walks you right out of the feasible region.

@art rising-variable
Here's the setup. The entering variable, x j, rises from zero to some amount, theta. Every other nonbasic variable stays at zero. And as x j rises, every basic variable moves.

@chapter How the basic variables move
@math heading="Row i" items="x_B(i) = bᵢ − aᵢⱼ·θ@b i minus;;need  bᵢ − aᵢⱼ·θ ≥ 0@at least zero"
Row i says the basic variable in that row equals b i minus a i j times theta. Each basic variable moves at the rate given by its entry in the entering column. And feasibility needs every one of them to stay at least zero.

@list heading="Read the sign of aᵢⱼ" items="aᵢⱼ > 0: falls, hits zero at bᵢ ÷ aᵢⱼ@positive|aᵢⱼ = 0: doesn't move@zero|aᵢⱼ < 0: grows@negative"
So read the sign. If the entry is positive, the basic variable falls, and reaches zero at b i over a i j. If it's zero, the variable doesn't move at all. If it's negative, the variable grows. Only a positive entry imposes a limit.

@art three-rows
And those last two rows aren't left out for tidiness. A negative entry would give a negative ratio, which looks like the smallest and isn't a step at all. A zero entry would mean dividing by zero. Strike them out, and write the reason beside them.

@chapter The test
@math heading="The ratio test" items="θ* = min { bᵢ ÷ aᵢⱼ : aᵢⱼ > 0 }@smallest;;that row leaves@leaves"
So the step is the smallest ratio, b i over a i j, over the rows with a positive entry. At that step, the winning row's basic variable is exactly zero, so it leaves, and x j takes its place. Go any further and that variable turns negative.

@art interval-intersection
Why is the minimum exactly right? Each positive row allows theta in an interval from zero to its ratio. The other rows allow anything. The feasible steps are where all those intervals overlap, which is zero up to the smallest ratio.

@chapter The plants tableau
@math heading="Column x₂ = (0, 2, 2),  rhs (4, 12, 18)" items="row 1:  entry 0, no limit@zero entry;;row 2:  12 ÷ 2 = 6@twelve over two;;row 3:  18 ÷ 2 = 9@eighteen over two;;min 6: row 2 leaves@minimum is six"
On the starting plants tableau, column x two is zero, two, two, and the right hand side is four, twelve, eighteen. Row one has a zero entry, so no limit. Row two gives twelve over two, six. Row three gives eighteen over two, nine. The minimum is six, so row two leaves.

@math heading="After the step" items="x₂ = 6@x two enters;;s₃ = 18 − 2(6) = 6@drops from eighteen;;s₁ = 4@stays at four"
x two enters at six, and the new point is zero, six. s three drops from eighteen to eighteen minus two times six, which is six. And s one stays at four. Exactly what the formula predicts.

@chapter The other choice
@math heading="Take ratio 9 instead" items="x₂ = 9@nine;;s₂ = 12 − 2(9) = −6@minus six;;z = 45@forty five"
Now pivot on row three, taking nine instead of six. Then x two is nine, and s two is twelve minus two times nine, minus six. The bottom right reads forty five, higher than the true optimum of thirty six.

@art negative-slack
That's the objective at a point outside the region. Zero, nine uses eighteen of plant B's twelve hours. A negative right hand entry is the signature, and the broken constraint is the one whose slack went negative.

@art outside-corner
The tableau is still a perfectly correct system of equations. What it's stopped describing is a feasible point.

@chapter No limit at all
@art open-ray
Sometimes no row has a positive entry. On maximise x one plus x two, with x one minus x two at most four and x one minus two x two at most six, after x one enters, the x two column has no positive entry anywhere.

@words text="No candidates → unbounded"
That isn't a broken tableau. It's a diagnosis. x two can rise forever with every basic variable staying non negative, so the objective is unbounded. And a tie between two rows leaves a basic variable at zero. That's degeneracy, coming later.

@chapter Where people slip
@list heading="Common slips" items="Taking the minimum over every row@The first|Reading a zero entry as a zero ratio@The second|Calling an unlimited column broken@The third"
The first slip is taking the minimum over every row. A negative entry gives a negative ratio, which wins, and gives the most convincing wrong answer in the course. The second is reading a zero entry as a ratio of zero. It's a division by zero, and the row doesn't restrict anything. The third is reading a column with no positive entry as a broken tableau.

@end text="Strike out the ineligible rows"
You can compute every ratio with its reason, and try the wrong row to see what breaks, on Learn. That's learn dot get er done dot I O.
