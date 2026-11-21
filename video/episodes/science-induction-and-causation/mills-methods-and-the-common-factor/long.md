---
format: long
lesson: science-induction-and-causation/mills-methods-and-the-common-factor
title: Mill's methods: which dish made them ill?
thumb: A candidate, not yet a cause
---

@chapter The dinner
@title text="Mill's Methods and the Common Factor" sub="Science, Induction and Causation" art=thumb
Five people ate at the same dinner, and two of them fell ill. Which dish was it? Mill gave us methods for answering questions like that, and a table makes them mechanical.

@art dinner-table
The table records which of five dishes each person ate: oysters, soup, bread, wine and cake. One for eaten, zero for not. And the verdict: one for ill. Ann and Ben fell ill. Cy, Di and Eve stayed well.

@chapter Agreement
@math heading="The ill diners" items="Ann ate:  O, S, B, C@Ann ate;;Ben ate:  O, B, W@Ben ate;;in both:  O, B@both ate"
Start with Mill's method of agreement, which looks only at the cases with the effect. Ann ate oysters, soup, bread and cake. Ben ate oysters, bread and wine. The dishes both ate are oysters and bread. So soup, wine and cake are eliminated.

@art agreement-overlap
That's the method of agreement. Take the cases where the effect occurred, and ask which factor appeared in all of them. A factor missing from even one such case is out.

@chapter The well diners
@art no-matching-pair
Now the well diners. Mill's method of difference would look for a pair of cases alike in everything but one dish. The table has none. Ann and Cy, the closest pair, differ in the oysters and in the wine.

@math heading="Eliminate by the well diners" items="Cy ate bread and stayed well:  B out@Cy ate bread;;no well diner ate oysters:  O stays@No well diner"
What the well diners offer instead is elimination. Cy ate bread and didn't fall ill. So, if one dish is responsible, bread isn't it. No well diner ate oysters. Oysters survive both steps, and nothing else does.

@art elimination-sieve
So the two steps work like a sieve. The ill diners keep only what they share. The well diners knock out anything they ate. Whatever is left in the sieve is what the table can't rule out.

@words text="Joint method: agrees with the verdict on every row"
Mill's joint method applies agreement twice. The cases with the effect agree in having the factor, and the cases without it agree in lacking it. In table terms, that's a definition that agrees with the verdict on every row.

@chapter Two fits
@math heading="Formulas that fit every row" items="O@oysters;;O ∧ B@oysters together with bread"
Search every formula of one or two factors, and two fit: oysters, and oysters together with bread. Both ill diners ate bread. Cy ate bread without oysters, so bread alone fails. But bread with oysters hasn't been excluded.

@art missing-column
So the table can't separate oysters from oysters with bread. To tell them apart, you'd need a case with oysters and no bread. And the table's other limits aren't visible in it at all. The knife, the water, the oysters' source aren't columns, and a table can't eliminate a factor it doesn't contain.

@words text="A fit is a candidate."
So a formula that fits every row is only a candidate. If the table lists every relevant factor, and the effect has a single cause, then a one factor formula that fits is that cause. Each of those conditions can fail.

@chapter Two causes
@art two-routes
Here's the second condition failing. In another dinner, prawns or eggs made a diner ill, and no diner ate both. No single factor fits. Prawns miss Ben. Eggs miss Ann and Eve. The method of agreement returns nothing common to the ill. The pair search finds prawns or eggs. Mill called this a plurality of causes, and his methods weren't designed for it.

@chapter Where people slip
@list heading="Common slips" items="Thinking the common factor is the cause@The first|Expecting one factor for every effect@The second|Treating a surviving candidate as proved@the third"
The first slip is thinking the factor common to the cases is the cause. Bread was common to both ill diners, and Cy ruled it out. The second is expecting every effect to have one factor that explains it. And the third is treating a candidate that survives as proved. One more well diner who ate the oysters would remove it.

@chapter Try it
@words text="Agreement · eliminate · list the fits · say what's missing"
Here's one to try. Take any table of cases and an effect. Apply agreement to the positive cases. Eliminate by the negative ones. List every formula that fits. Then name a factor the table doesn't list, and a case that would separate the fits.

@end text="Test a suspect against the table"
You can change the table and watch the list of fitting formulas follow, on Learn. That's learn dot get er done dot I O.
