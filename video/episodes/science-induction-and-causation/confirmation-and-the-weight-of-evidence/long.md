---
format: long
lesson: science-induction-and-causation/confirmation-and-the-weight-of-evidence
title: When does evidence confirm a theory? Surprise, and the Bayes factor
thumb: Predicted isn't confirmed
---

@chapter What confirmation is
@title text="Confirmation and the Weight of Evidence" sub="Science, Induction and Causation" art=thumb
Your theory predicted it, and it happened. So the evidence confirms your theory, right? Not necessarily. It depends on something people forget to ask.

@math heading="Confirmation" items="confirms:  P(H | E) > P(H)@confirms;;disconfirms:  P(H | E) < P(H)@disconfirms;;neutral:  P(H | E) = P(H)@neutral"
Here's a reasonable rule. Evidence supports a hypothesis if, and only if, the hypothesis is more probable afterwards than before. So E confirms H when the posterior is above the prior. It disconfirms H when the posterior is below. And it's neutral when they're equal.

@art probability-raise
That's a comparison of two numbers, not a property of the evidence alone. It tells you whether the evidence supports. To say how strongly, you need a measure of weight.

@chapter The weight of evidence
@math heading="Odds form of Bayes' rule" items="posterior odds = BF · prior odds@posterior odds;;BF = P(E | H) / P(E | ¬H)@the Bayes factor"
The usual measure is the factor by which the evidence multiplies the odds. Posterior odds equal the Bayes factor times the prior odds. And the Bayes factor is the probability of the evidence if the hypothesis is true, over its probability if the hypothesis is false. It doesn't depend on the prior.

@words text="BF > 1 confirms · BF = 1 neutral · BF < 1 disconfirms"
So evidence confirms exactly when the factor is above one. A factor of one is neutral. And below one, it disconfirms.

@art odds-multiplier
Think of the factor as a stretch applied to the odds. A factor of ten makes the odds ten times longer in favour of the hypothesis. A factor of one leaves them alone. And because it doesn't depend on the prior, two people who start in different places can still agree on how much the evidence weighed.

@chapter Three cases
@math heading="Prior 1/2,  P(E | H) = 1" items="surprising:  P(E | ¬H) = 1/10,  BF 10,  P(H | E) = 10/11@surprising;;expected:  P(E | ¬H) = 9/10,  BF 10/9,  P(H | E) = 10/19@expected;;neutral:  P(E | ¬H) = 1,  BF 1,  P(H | E) = 1/2@neutral"
Three cases share a prior of a half, and in each, H makes the evidence certain. They differ only in how probable E is if H is false. Surprising: a tenth. The factor is ten, and the posterior ten elevenths. Expected: nine tenths. The factor is ten ninths, and the posterior ten nineteenths. Neutral: one. The factor is one, and the posterior stays at a half.

@art surprise-weight
In every row, the evidence is perfectly consistent with H. Yet the verdicts differ. In the first, the evidence would rarely occur unless H were true, so seeing it is strong support. In the second, it would very probably have happened anyway. In the third, it would have happened whatever.

@art sunrise-everyone
That third row corrects an easy mistake. That a hypothesis predicts the evidence isn't the same as the evidence confirming it. The sun rose this morning is predicted by every theory of the heavens anyone takes seriously, and so it confirms none of them against the others.

@chapter The alternative decides
@art alternative-mixture
So the weight depends on the alternative. And the probability of the evidence if H is false is an average over every way H could be false, weighted by their priors. It's a number you chose. That's why two scientists can agree on the observation, and disagree on what it shows.

@chapter The method
@list heading="Four steps" items="State H and its negation@State the hypothesis|Find both likelihoods@find both likelihoods|Take the ratio@take the ratio|Apply it to the prior odds@apply it"
So, four steps. State the hypothesis and its negation, because evidence has weight only against an alternative. Find both likelihoods. Take the ratio. And apply it to the prior odds, converting back to a probability if you need one.

@chapter Where people slip
@list heading="Common slips" items="Thinking consistent evidence confirms@The first|Measuring confirmation without an alternative@The second|Treating the factor as the probability@the third"
The first slip is thinking evidence consistent with a hypothesis confirms it. Consistency only says the likelihood isn't zero. The second is measuring confirmation without an alternative. The same likelihood of one gives a factor of ten, ten ninths, or one. And the third is treating the factor as the probability. A factor of ten from a prior of one in a hundred gives ten over a hundred and nine, nowhere near certain.

@art factor-from-low-prior
The factor multiplies the odds, and the odds started somewhere. From a prior of a half, a factor of ten takes you to ten elevenths. From one in a hundred, it barely gets you off the ground.

@chapter Try it
@words text="prior 1/2 · BF 3" sub="posterior odds?"
Here's one to try. A hypothesis with prior a half meets evidence with a Bayes factor of three. What are its posterior odds? And what's its posterior probability?

@end text="Change the alternative, watch the weight"
You can change both likelihoods and watch the same evidence change weight, on Learn. That's learn dot get er done dot I O.
