---
format: long
lesson: science-induction-and-causation/correlation-confounding-and-simpsons-paradox
title: Simpson's paradox: better in every group, worse overall
thumb: Wins every group, loses overall
---

@chapter Two treatments
@title text="Correlation, Confounding and Simpson's Paradox" sub="Science, Induction and Causation" art=thumb
One treatment does better for small kidney stones. It does better for large kidney stones. And overall, it does worse. That's not a mistake. It's Simpson's paradox, and here's why it happens.

@art two-treatments
A study compared two treatments for kidney stones. Open surgery, A, and a keyhole procedure, B. Patients had small stones or large ones, and the study counted successes over patients treated.

@math heading="Successes / treated" items="small:  A 81/87 = 27/29   B 234/270 = 13/15@small stones;;large:  A 192/263   B 55/80 = 11/16@large stones;;pooled:  A 273/350   B 289/350@Pooled"
For small stones, A succeeded eighty one times out of eighty seven, twenty seven twenty ninths, against thirteen fifteenths for B. For large stones, A had a hundred and ninety two out of two hundred and sixty three, against eleven sixteenths for B. A wins in both groups. Pooled, A has two hundred and seventy three out of three hundred and fifty, and B has two hundred and eighty nine. B wins.

@chapter Look at the denominators
@art mix-of-cases
There's no mistake in either comparison. The reason is in the denominators. A was given to two hundred and sixty three patients with large stones, and eighty seven with small. B was given to eighty with large stones, and two hundred and seventy with small.

@art hard-cases
And large stones are the harder cases, with lower success rates under both treatments. So A's pooled figure is pulled down by a mix that's mostly hard cases. The pooled rate also reflects who was treated.

@words text="Confounder" sub="changes both who gets which treatment and whether it succeeds"
A confounder is a variable that influences both which treatment a patient receives and whether it succeeds. Comparing the treatments without it compares different kinds of patient. Here, stone size is the confounder.

@chapter Give both the same mix
@math heading="Standardised: same weights for both arms" items="A:  634983/762700 ≈ 0.83@about nought point eight three;;B:  6231/8000 ≈ 0.78@nought point seven eight"
The way to remove the effect of the mix is to give both treatments the same mix. Weight each group by its share of all patients, the same weighting for both arms. Then A comes out at about nought point eight three, and B at nought point seven eight. The adjusted comparison agrees with both groups.

@art balanced-arms
And a reversal needs two things. The treatments were given to different proportions of the groups, and the groups differ in their rates. With balanced groups, where each arm treats the same number in each group, the pooled comparison can't disagree with the groups.

@chapter Berkeley, 1973
@art two-departments
The same pattern turns up in two of the largest departments in the nineteen seventy three admissions to the University of California at Berkeley. Women were admitted at a higher rate in each department, and at a lower rate over the two together, since they applied more to the department that admitted fewer.

@chapter Which table to believe?
@list heading="It depends what the groups are" items="Groups set who gets which arm: compare within groups@If severity|Groups are an effect of the treatment: compare pooled@If the grouping variable"
Which table to believe isn't something the counts can settle. If severity is the reason the doctors chose a treatment, then comparing within groups is right. If the grouping variable is itself an effect of the treatment, like a complication the treatment causes, then conditioning on it removes part of the very effect you're measuring. Then the pooled comparison is right.

@art pooled-reversal
So the same counts can support either answer, and the difference is a claim about what causes what. A correlation is a comparison of rates. Whether it reflects a cause is decided by a model of how the variables influence each other.

@chapter Where people slip
@list heading="Common slips" items="Thinking a higher overall rate means better@The first|Always trusting the within group comparison@The second|Treating the reversal as a trick@the third"
The first slip is thinking a higher overall rate means a better treatment. The second is always trusting the within group comparison. That's only right when the groups aren't caused by the treatment. And the third is treating the reversal as a trick of the numbers. Each comparison answers a different question, and the reversal is the sign that the questions have different answers.

@chapter Try it
@words text="Rate per group · pooled rate · compare · decide what the groups are"
Here's one to try. Take any two rates across groups. Compute the rate in each group, then the pooled rates. If the orders differ, look at the group sizes in each arm for the reason. Then decide whether the grouping causes the treatment, or results from it.

@end text="Change the counts, find the reversal"
You can change the counts and watch the reversal appear and vanish, on Learn. That's learn dot get er done dot I O.
