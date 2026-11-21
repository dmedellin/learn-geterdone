---
format: long
lesson: paradoxes-and-their-exits/sleeping-beauty
title: Sleeping Beauty: one half or one third?
thumb: Same rule, two likelihoods
---

@chapter The experiment
@title text="Sleeping Beauty" sub="Paradoxes and Their Exits" art=thumb
On Sunday evening, Beauty is told the plan, and put to sleep. A fair coin is tossed. If it lands heads, she's woken on Monday, and the experiment ends.

@art wakings
If it lands tails, she's woken on Monday, put back to sleep with a drug that erases the memory, and woken again on Tuesday. Each time she's woken, she's asked: how likely is it that the coin landed heads? She can't tell Monday's waking from Tuesday's.

@chapter Two answers
@list heading="Two answers" items="Halfer: one half@The halfer|Thirder: one third@The thirder"
The halfer answers one half. She knew on Sunday she'd be woken, so being woken tells her nothing new. The thirder answers one third. Over many repetitions, a third of her wakings follow heads, and she can't tell which waking this is.

@art same-machine
Both answers can be written as an update by Bayes' rule. Two hypotheses, heads and tails, each with prior one half. Both sides agree on that. What differs is the likelihood of the evidence.

@chapter The halfer's model
@math heading="Evidence: I am awake" items="P(awake | H) = 1@if the coin is heads;;P(awake | T) = 1@if it's tails;;Bayes factor = 1@Bayes factor;;P(H | awake) = 1/2@posterior"
The halfer says the evidence is, I am awake. That has probability one if the coin is heads, and one if it's tails, since she's woken either way. So the Bayes factor is one, and the posterior for heads stays at one half.

@chapter The thirder's model
@math heading="Evidence: this waking" items="P(this waking | H) = 1/2@Under heads;;P(this waking | T) = 1@Under tails;;Bayes factor = 1/2@Bayes factor;;P(H | this waking) = 1/3@posterior"
The thirder says the evidence is that this waking is occurring. Consider a day she might be woken. Under heads, only one of the two days has a waking, so the chance is one half. Under tails, both days do, so it's one. The Bayes factor is one half, and the posterior for heads is one third.

@art two-scales
The rule that produced both answers is the same, and so is the prior. Only the likelihood of the word awake changed. Neither side made a mistake in the arithmetic.

@chapter Told it's Monday
@math heading="Beauty learns it's Monday" items="likelihood:  H 1,  T 1/2@likelihood of Monday;;thirder:  1/3  →  1/2@The thirder;;halfer:  1/2  →  2/3@The halfer"
Here's where the models part. Suppose Beauty learns it's Monday. The likelihood of Monday is one under heads, and one half under tails. The thirder starts from one third, and moves to one half. The halfer starts from one half, and moves to two thirds.

@art untossed-coin
That's the halfer's cost. In the version where the coin is tossed on Monday night, a fair coin that hasn't been tossed yet moves to two thirds on the news that it's Monday. The thirder's cost is a credence of one third in a coin she knows is fair, reached by evidence that isn't about the coin in the ordinary sense.

@chapter Not the usual exit
@art self-location
So the exit isn't the usual one. There are two valid arguments, from the Sunday prior and a likelihood, to credences that can't both be held. The only premise that differs is the likelihood. Whether a self locating fact, this is a waking, counts as evidence about the coin is what the two answers divide on.

@art betting-slips
And a bet doesn't settle it, unless it says what's scored. If a stake is paid for each waking, tails pays twice as often, and betting on tails is better whichever model you hold. If one stake is paid for the whole experiment, the bet is even.

@chapter Where people slip
@list heading="Common slips" items="Thinking a fair coin means the answer must be one half@The first|Taking one answer as an arithmetic error@The second|Expecting a bet to settle it@And the third"
The first slip is thinking that because the coin is fair, the answer must be one half. Fairness fixes the prior, which nobody disputes. The second is taking one answer as an arithmetic error. Each is a correct update. And the third is expecting a bet to settle it. The best bet follows from the scoring.

@chapter Try it
@words text="told it's Monday" sub="prior 1/3, then prior 1/2"
Run the Monday update twice. Start from the thirder's prior of one third, then from the halfer's one half, with likelihoods one under heads and one half under tails. Say which cost you find harder to pay.

@end text="Same rule, two likelihoods"
You can change the likelihoods and compare the answers, on Learn. That's learn dot get er done dot I O.
