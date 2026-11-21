---
format: long
lesson: decision-and-rationality/expected-value-and-expected-utility
title: Expected utility: weigh each outcome by its chance, and find the tipping point
thumb: Where the choice flips
---

@chapter Adding probabilities
@title text="Expected Value and Expected Utility" sub="Decision and Rationality" art=thumb
When you know roughly how likely each state is, you can do better than planning for the worst or the best. You can weigh every state by its chance.

@art weighted-states
Suppose your credence in rain is a third, and so two thirds in no rain. Those two numbers are the new ingredient. With them, the umbrella table can be scored in a way the rules for ignorance couldn't.

@math heading="Expected utility" items="EU(a) = Σ P(s) · u(a, s)@the sum;;choose the largest@largest"
The expected utility of an act is the sum, over the states, of the probability of each state times the act's payoff in it. The rule recommends an act with the largest expected utility.

@chapter The umbrella, scored
@math heading="Rain at 1/3" items="EU(take) = 2 · 1/3 + 1 · 2/3 = 4/3@For take;;EU(leave) = −3 · 1/3 + 3 · 2/3 = 1@For leave"
For take: two times a third, plus one times two thirds, which is four thirds. For leave: minus three times a third, plus three times two thirds, which is one. Take scores higher, so at a third the rule recommends the umbrella.

@art not-a-payoff
But the word expected misleads. No single outing with the umbrella pays four thirds. It pays two, or one. Four thirds is what the average would be if you faced this decision many times with the same odds. For one decision, it's a score, a number that ranks acts by weighing every state in proportion to how likely you think it is.

@chapter The tipping point
@math heading="Let p be the chance of rain" items="EU(take) = 1 + p@one plus p;;EU(leave) = 3 − 6p@three minus six p;;1 + p = 3 − 6p,  so 7p = 2,  p = 2/7@two sevenths"
Now let p be the probability of rain. Take scores one plus p. Leave scores three minus six p. Each score is a straight line in p, so the lines cross once. They tie when one plus p equals three minus six p, so seven p is two, and p is two sevenths.

@art crossing-lines
Above two sevenths, the umbrella is recommended. Below it, leaving is. And that separates two questions. How likely is rain is a question about the world. Whether the answer matters is a question about the table. If you're sure rain is more likely than two sevenths, your exact estimate is irrelevant.

@art narrow-margin
At a third, the umbrella wins, but not by much. Only a twenty first of probability separates them. A forecaster who revised rain from a third to a fifth would reverse the advice.

@chapter Bets and tickets
@math heading="A fair bet" items="bet:  1 · 1/2 + (−1) · 1/2 = 0@betting scores;;don't bet:  0@not betting"
A fair bet: win one or lose one, each with probability a half, against not betting. Betting scores zero, and not betting scores zero. They tie, and the tipping point is a half. A bet is worth taking when your probability of winning is above that.

@art fair-coin
So a fair bet is exactly a tie. The rule has nothing to say between betting and not betting. Move the odds even slightly in your favour, and it says bet. Move them against you, and it says don't.

@math heading="A lottery ticket" items="buy:  499 · 1/1000 − 1 · 999/1000 = −1/2@buying scores;;skip:  0@skipping;;tie at a chance of 1/500@one in five hundred"
A ticket costs one and pays five hundred if it wins, with probability one in a thousand. Buying scores four hundred and ninety nine thousandths, minus nine hundred and ninety nine thousandths, which is minus a half. Skipping scores zero. They'd tie at a chance of one in five hundred, where the prize exactly matches the odds against it.

@art lottery-house
A lottery that sold tickets there would be paying out more than it took in. So skipping is recommended, every time.

@chapter Utilities, not money
@words text="Payoffs are utilities."
One caution. The payoffs in these tables are utilities, numbers for how much you value each outcome. For money, the two can come apart, and that's the next lesson.

@chapter Where people slip
@list heading="Common slips" items="Reading expected value as the value you expect@The first|Treating the probability as a fact@The second|Thinking a tie means it doesn't matter@the third"
The first slip is reading expected value as the value you expect. The second is treating the probability as a fact rather than an estimate. Report the recommendation with the tipping point. And the third is thinking a tie means the choice doesn't matter. The averages are equal, but the payoffs still differ state by state.

@chapter Try it
@words text="rain at 1/5" sub="EU(take)?  EU(leave)?"
Here's one to try. Change the chance of rain to a fifth. Work out both expected utilities, and check that leave now wins, just as the tipping point says it should.

@end text="Find where the choice flips"
You can change the probabilities and find the tipping point yourself, on Learn. That's learn dot get er done dot I O.
