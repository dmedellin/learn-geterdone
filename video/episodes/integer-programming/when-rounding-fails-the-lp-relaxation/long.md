---
format: long
lesson: integer-programming/when-rounding-fails-the-lp-relaxation
title: Why you can't just round the LP answer
thumb: Rounding is a guess
---

@chapter The question
@title text="When Rounding Fails" sub="Integer Programming" art=thumb
You need a whole-number plan. The linear programme hands you an answer with fractions in it. Why not just round it? Here's a small example where rounding breaks rows, and where the best whole plan is somewhere rounding never looks.

@chapter The relaxation
@art bigger-region
Drop the requirement that the variables be whole, and you get a different problem, the relaxation. Every whole plan that was allowed is still allowed, plus many more. Nothing has been approximated. It's an easier problem with its own exact answer.

@words text="max: z_LP ≥ z_IP" sub="min: z_LP ≤ z_IP"
And because its region is bigger, a maximum over it can't be smaller. So for a maximisation, the relaxation's value is at least the integer optimum. For a minimisation, it's at most. That bound is the entire relationship.

@chapter The example
@math heading="The model" items="max 3x₁ + 4x₂@maximise;;2x₁ + x₂ ≤ 6@two x one plus x two;;2x₁ + 3x₂ ≤ 9@two x one plus three;;x₁, x₂ ≥ 0 and whole@whole"
Maximise three x one plus four x two. Two x one plus x two is at most six. Two x one plus three x two is at most nine. Both variables are non negative and whole.

@art lp-region
The relaxation stops at the corner nine quarters, three halves, worth fifty one quarters, which is twelve and three quarters. Both coordinates are fractional. The simplex method found that exactly, in fractions. So the question is what to do with it.

@chapter Four roundings
@art rounding-box
There's no such thing as the rounding. With two fractional coordinates there are four: floor or ceiling in each. Two, one. Two, two. Three, one. And three, two.

@math heading="Test each one" items="(2, 2):  2·2 + 3·2 = 10 > 9  ✗@two, two;;(3, 1):  2·3 + 1 = 7 > 6  ✗@three, one;;(3, 2):  2·3 + 2 = 8 > 6  ✗@three, two;;(2, 1):  feasible, worth 10  ✓@two, one"
Two, two breaks the second row: it wants ten where nine is allowed. Three, one breaks the first, wanting seven. Three, two breaks the first, wanting eight. Only two, one survives, and it's worth ten.

@chapter The best plan is far away
@art lattice-in-region
Feasible isn't the same as best, though. A rounding can pass every row and still be a poor plan, and that's the case to fear, because nothing complains. To know, you have to look at every whole point.

@art far-corner
Try every whole point in the box: there are thirty candidates, and ten are feasible. The best is zero, three, worth twelve. It isn't a rounding at all. It's at the other end of the region, with the first variable at zero. No amount of care about which way to round would find it, because rounding only looks at the corners of one little box.

@math heading="Three numbers" items="z_LP = 51/4 = 12.75@fifty one quarters;;z_IP = 12@twelve;;best rounding = 10@ten;;51/4 ≥ 12 ≥ 10@only the first"
So, fifty one quarters for the relaxation, twelve for the integer optimum, and ten for the best rounding. And only the first inequality is a theorem.

@art bound-ladder
The three quarters between twelve and three quarters and twelve is the integrality gap of this instance. It's the price of insisting on whole numbers. The two between twelve and ten is the price of rounding instead of solving.

@chapter Where people slip
@list heading="Common slips" items="Rounding to the nearest point and stopping@The first|Calling an infeasible rounding close enough@The second|Reading z_LP as an estimate of the answer@And the third"
The first slip is rounding to the nearest point and stopping. Here that's two, two, which breaks a row. The second is calling an infeasible rounding close enough. And the third is reading the relaxation's value as an estimate.

@words text="(2, 2) needs 10 where 9 exist" sub="not slightly wrong: not a plan"
On the second: two, two wants ten units of finishing capacity where nine exist. That isn't a plan that's slightly wrong. It isn't a plan. And on the third: the relaxation's value is a bound, and it predicts nothing. The same size of instance could have a gap of zero, or of a hundred.

@words text="Enumeration answers. Rounding guesses."
Enumeration worked here, with thirty candidates. At any interesting size it's hopeless, and that's what the rest of this course is for. But remember the difference: a number from enumeration is an answer, and a number from rounding is a guess with no bound attached.

@chapter Try it
@words text="Is (1, 2) feasible?" sub="2x₁ + x₂ ≤ 6 · 2x₁ + 3x₂ ≤ 9"
Your turn. Take the point one, two. Check both rows, and work out its value. Then try one, three, and say why the best plan, zero, three, still beats both.

@end text="Round, test and enumerate"
You can test every rounding and enumerate every whole plan yourself, on Learn. That's learn dot get er done dot I O.
