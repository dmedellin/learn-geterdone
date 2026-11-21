---
format: long
lesson: knowledge-and-evidence/reference-classes-and-statistical-evidence
title: What's your chance? It depends which group you're in
thumb: A rate belongs to a group
---

@chapter A smoker who cycles
@title text="Reference Classes and Statistical Evidence" sub="Knowledge and Evidence" art=thumb
What's the chance that one particular person gets ill? A statistic can't tell you on its own. A statistic is a rate in a group, and it only reaches a person through the group you choose.

@art many-groups
Take a man of sixty who smokes and cycles daily. How likely is he to die of heart disease before seventy five? A doctor can consult tables. The counts here are invented, so every rate is a clean fraction.

@math heading="Smokers" items="all smokers:  200 / 1000 = 1/5@He's a smoker;;who cycle:  5 / 100 = 1/20@a smoker who cycles;;who don't:  195 / 900 = 13/60@who don't"
He's a smoker, so one in five applies. He's a smoker who cycles, so one in twenty applies. And for comparison, smokers who don't cycle: a hundred and ninety five out of nine hundred, which is thirteen sixtieths.

@art nested-classes
But he's also a person who cycles, a person of sixty, a person who lives in his city, and each of those has a rate of its own. All of these are statements about groups he belongs to. And the two rates for smokers differ by a factor of four.

@chapter The reference class problem
@words text="Reference class" sub="the group whose rate is used for one case"
The group whose rate you take as the probability for one case is called the reference class. And the reference class problem is that a case belongs to many such groups, with different rates, and the counts don't say which to use.

@art small-sample
A practical rule is to use the narrowest class that has enough data. But there's a cost on both sides. Smokers who cycle give one in twenty, but that rests on a hundred people and five deaths. All smokers give one in five, on ten times as many people, and ignore the cycling.

@chapter Pooling
@math heading="Pool by adding counts" items="deaths:  5 + 195 = 200@add the deaths;;people:  100 + 900 = 1000@add the totals;;rate:  200 / 1000 = 1/5@and divide;;✗ average of 1/20 and 13/60 = 2/15@not the average"
The rate for smokers is the pooled rate of the two groups beneath it. Add the deaths, five plus a hundred and ninety five, two hundred. Add the totals, a thousand. And divide: one in five. It's not the average of the two rates, two fifteenths, which would ignore that nine in ten smokers here don't cycle.

@art pooled-weight
That's why the pooled rate sits close to the larger group's rate. The larger group supplies most of the counts. And nothing makes the pooled rate the probability. It's the right answer for a smoker chosen at random, and the wrong one for a man known to cycle.

@chapter When pooling points the wrong way
@math heading="Kidney stones: open against keyhole" items="small stones:  81/87  against  234/270@small stones;;large stones:  192/263  against  55/80@large stones;;pooled:  273/350  against  289/350@Pooled"
It can be worse than a difference in size. In a well known set of counts, two treatments for kidney stones are compared. The open operation does better for small stones, eighty one out of eighty seven against two hundred and thirty four out of two hundred and seventy. And for large stones, a hundred and ninety two out of two hundred and sixty three against fifty five out of eighty. Pooled, the keyhole procedure is ahead.

@art pooled-reversal
Pooled, the open operation has two hundred and seventy three out of three hundred and fifty. The keyhole procedure has two hundred and eighty nine out of three hundred and fifty. Ahead in each group, and behind overall.

@art large-stone
A patient with a large stone asks which to choose. The pooled figures answer a question about patients whose stones might be either size, and he isn't one of them. Why pooling reverses, called Simpson's paradox, comes later in the subject. Here it shows that the choice of class can change which treatment looks better.

@chapter Where people slip
@list heading="Common slips" items="Treating the pooled rate as the probability@The first|Averaging rates instead of adding counts@The second|Thinking the data can choose the class@the third"
The first slip is treating the pooled rate as the probability. The second is averaging two rates instead of adding counts. And the third is thinking the data can choose the class. The counts print a rate for each class and are silent on which is right. Choosing is a judgement about relevance, and about how much data each class has.

@chapter Try it
@words text="“1 in 20 of smokers who cycle”" sub="not “his chance is 1 in 20”"
Here's the habit to practise. State the class with the rate. Say one in twenty of smokers who cycle, not his chance is one in twenty. Then try it on yourself: list three classes you belong to, and ask which one a statistic about you was really about.

@end text="Change the counts, compare the classes"
You can change the counts and see which comparison moves, on Learn. That's learn dot get er done dot I O.
