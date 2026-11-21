---
format: long
lesson: science-induction-and-causation/enumerative-induction-and-humes-problem
title: Will the sun rise tomorrow? Hume's problem of induction
thumb: The past doesn't prove the next
---

@chapter Ten sunrises
@title text="Enumerative Induction and Hume's Problem" sub="Science, Induction and Causation" art=thumb
The sun has risen on each of the last ten days. So it'll rise on the eleventh. That's the plainest inductive argument there is. Is it valid?

@math heading="The bad row" items="day 1 … day 10:  T … T@every premise true;;day 11:  F@conclusion false"
Test it the way you'd test any argument. Look for a row where every premise is true and the conclusion is false. Here it is: every premise true, ten sunrises, and the conclusion false, no sunrise on day eleven.

@art sunrise-row
Nothing in the ten premises mentions day eleven, so that sentence is free to be false. And replace ten by ten thousand, and the row is still there. The premises grow. The conclusion never moves into them.

@words text="Enumerative induction" sub="all observed F were G, so the next F will be G"
That's enumerative induction: from all observed cases of F have been G, to the next case of F will be G. As a form, it's invalid. So whatever force it has comes from a premise it doesn't state.

@chapter The missing premise, as a prior
@art five-chances
You can write that missing premise as a probability. Suppose the sun rises each day with some fixed chance, and consider five hypotheses about it: one, three quarters, a half, a quarter, and zero. Put an equal prior of a fifth on each.

@math heading="Weights after ten sunrises, in units of 1/1048576" items="chance 1:  1048576@chance one;;chance 3/4:  59049@three quarters;;chance 1/2:  1024@a half;;chance 1/4:  1;;chance 0:  0@zero"
Ten sunrises have probability chance to the tenth under each hypothesis, so they favour the high chances heavily. Chance one keeps all its weight. Three quarters keeps a small fraction. A half, much less. A quarter, almost nothing. And zero is ruled out.

@art weights-collapse
So the data reweight the prior. The hypothesis that the sun always rises ends up with most of the posterior. But not all of it. Three quarters to the power of ten isn't zero, and three quarters to any power never will be.

@math heading="The predictive probability" items="P(next | data) = Σ P(h | data) · chance(h)@To predict the next day;;uniform prior:  43735/44346, just under 1@just under one"
To predict the next day, weight each hypothesis's chance by its posterior and add them up. Under the uniform prior, the probability of an eleventh sunrise is forty three thousand, seven hundred and thirty five over forty four thousand, three hundred and forty six. Just under one, and never exactly one.

@chapter Same data, another prior
@art skeptic-prior
Now give a skeptic a different prior: one in a thousand on a chance of one, a tenth each on three quarters, a half and a quarter, and six hundred and ninety nine thousandths on a chance of zero.

@words text="P(next sunrise) ≈ 0.78" sub="same ten sunrises"
The ten sunrises are the same. The likelihoods are the same. And the predictive probability falls from just under one to about nought point seven eight. The data didn't change. The prior did.

@chapter Hume's argument
@art future-gap
So the prior does the work that the ten sunrises can't. It's a premise about how the unobserved relates to the observed. And the question Hume asked is what could ever justify a premise like that.

@list heading="Hume's argument" items="Either deductive, or assumes the unobserved resembles the observed@is either deductive|It isn't deductive@It isn't deductive|Resemblance isn't a necessary truth@isn't a necessary truth|Any argument from experience already assumes it@already assumes it|So nothing non-circular supports induction@nothing non circular"
That's the force of Hume's point. An argument from observed cases to an unobserved one is either deductive, or rests on the assumption that the unobserved resembles the observed. It isn't deductive. Resemblance isn't a necessary truth, since a world where the sun stops is describable. So only experience could support it, and any argument from experience already assumes it. So nothing non circular supports enumerative induction.

@art circle-arrow
The calculation doesn't answer Hume. It shows exactly where an answer would have to go. Reject the third premise, and you owe an account of a third source of support. Reject the fourth, and you owe an account of why a circular defence isn't vicious. Accept the conclusion, and you owe an account of why anyone should expect the sun at all.

@chapter Where people slip
@list heading="Common slips" items="Thinking a large sample makes it valid@The first|Reading the posterior as produced by the data alone@The second|Thinking the problem is that induction fails@the third"
The first slip is thinking a large sample makes induction valid. It raises the probability under a prior. It never makes a deduction. The second is reading the posterior as if the data produced it alone. The posterior is the prior, reweighted. And the third is thinking the problem is that induction fails. It's worked every time we've checked. Hume's point is about justification.

@chapter Try it
@words text="Find the row · name the premise · write the prior · vary it"
Here's one to try. Take any argument from past cases to a new one. Find the bad row. Name the missing premise. Write it as a prior, then change the prior and see how much the conclusion moves. That gap is how much the conclusion owes to the premise.

@end text="Change the prior, keep the sunrises"
You can change the prior and watch the same sunrises predict differently, on Learn. That's learn dot get er done dot I O.
