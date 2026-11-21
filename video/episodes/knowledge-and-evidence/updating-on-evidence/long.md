---
format: long
lesson: knowledge-and-evidence/updating-on-evidence
title: Updating on evidence: priors, likelihoods and the Bayes factor
thumb: Multiply, add, divide
---

@chapter Two urns
@title text="Updating on Evidence" sub="Knowledge and Evidence" art=thumb
How much should one piece of evidence change your mind? There's an exact answer, and it takes three moves: multiply, add, divide.

@art two-urns
Two urns hold four balls each. Urn one has three red and one blue. Urn two has one red and three blue. A fair coin chooses one, you can't see which, and a ball is drawn from it. Your prior credence in each urn is a half.

@chapter One red ball
@math heading="A red ball is drawn" items="urn 1:  1/2 · 3/4 = 3/8@urn one;;urn 2:  1/2 · 1/4 = 1/8@urn two;;total:  3/8 + 1/8 = 1/2@add;;posterior, urn 1:  (3/8) / (1/2) = 3/4@divide"
A red ball comes out. It's red with probability three quarters on urn one, and a quarter on urn two. Those are the likelihoods. Multiply each prior by its likelihood. Urn one: a half times three quarters, three eighths. Urn two: one eighth. Add them, a half. Then divide, and the posterior for urn one is three quarters.

@math heading="Posterior" items="P(H | E) = P(E | H) · P(H) / P(E)@the posterior credence"
In symbols, the posterior credence in a hypothesis given the evidence is the likelihood times the prior, over the probability of the evidence. And that denominator is just the total of the products, over every hypothesis.

@art likelihood-not-credence
Keep one thing straight. A likelihood isn't a credence in the hypothesis. It's how probable the observation is, if the hypothesis is true. A hypothesis that makes the observation probable gains on one that makes it improbable.

@chapter The Bayes factor
@math heading="Bayes factor and odds" items="factor = P(E | H) / P(E | ¬H) = (3/4) / (1/4) = 3@three quarters over a quarter;;posterior odds = prior odds · factor:  1 to 1 → 3 to 1@one to one"
The red ball moved urn one from a half to three quarters. A summary of how much it moved, without the prior in it, is the Bayes factor. Three quarters over a quarter, which is three. Odds multiply by the factor. One to one becomes three to one, and odds of three to one are a credence of three quarters.

@art balance-shift
With two hypotheses, the factor doesn't depend on the prior. So the same red ball multiplies the odds by three, whatever they were. And a factor of one would leave your credence exactly where it was. The factor is the weight of the evidence.

@chapter A second draw
@math heading="Put it back, draw again: red" items="urn 1:  3/4 · 3/4 = 9/16@three quarters times;;urn 2:  1/4 · 1/4 = 1/16@a quarter times a quarter;;posterior, urn 1:  9/10@nine tenths;;odds:  1 to 1 → 3 to 1 → 9 to 1@nine to one"
Put the ball back and draw again. Red again. Now the prior is the previous posterior. Three quarters times three quarters is nine sixteenths. A quarter times a quarter is one sixteenth. So the posterior is nine tenths. The factors multiply, three times three is nine, and the odds go to nine to one.

@art odds-bars
Watch the odds grow. One to one before any draw. Three to one after the first red. Nine to one after the second. Each red ball multiplies by three. But the credence never reaches one, because urn two can still produce red.

@art sequence-order
Had the second ball been blue, the factor for urn one would have been a third, and the credence would have gone back to a half. The same two balls in the other order give the same answer. Updating twice and updating once on both balls are the same arithmetic.

@chapter Fit is not proof
@art two-headed-coin
A coin is either two headed or fair, and the prior for two headed is one in a hundred. Three heads in a row. They're certain on the two headed coin, and have probability one eighth on the fair one. That's a Bayes factor of eight.

@math heading="Three heads" items="prior: 1/100@one in a hundred;;factor: 8@factor of eight;;posterior: 8/107, under 8%@eight over a hundred and seven"
Start from one in a hundred, apply a factor of eight, and the posterior is eight over a hundred and seven. Under eight percent. The evidence confirms the two headed coin, and fits it perfectly. It doesn't prove it. The rival makes three heads improbable, not impossible, so it keeps its share.

@words text="One tails → posterior 0"
The reverse is stricter. One tails makes the likelihood of the two headed coin zero, and its posterior zero, whatever the prior was.

@chapter Where people slip
@list heading="Common slips" items="Thinking a perfect fit proves it@The first|Reading the factor as the posterior@The second|Counting the same observation twice@the third"
The first slip is thinking evidence that fits a hypothesis proves it. The second is reading the Bayes factor as the posterior. A factor of nine gives nine tenths only from even odds. And the third is using the same observation twice. Start each update from the last posterior, not by adding the old ball again.

@chapter Try it
@words text="factor 9 · prior 1/5" sub="posterior?"
Here's one to try. The data carry a Bayes factor of nine for a hypothesis, and the prior credence was a fifth. Turn the prior into odds, multiply, and turn the odds back into a credence.

@end text="Change the prior, watch the posterior"
You can change the priors, the likelihoods and the draws yourself, on Learn. That's learn dot get er done dot I O.
