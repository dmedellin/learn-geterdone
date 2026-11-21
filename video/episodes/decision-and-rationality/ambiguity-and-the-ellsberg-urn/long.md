---
format: long
lesson: decision-and-rationality/ambiguity-and-the-ellsberg-urn
title: The Ellsberg urn: why we prefer the odds we know
thumb: Known odds, twice
---

@chapter The urn
@title text="Ambiguity and the Ellsberg Urn" sub="Decision and Rationality" art=thumb
Would you rather bet on odds you know, or odds you don't? Most people pick the known odds. Here's an urn that shows that preference fits no single guess about the unknown.

@art ninety-balls
Daniel Ellsberg described this urn in nineteen sixty one. It holds ninety balls. Thirty are red. The other sixty are black or yellow, in a mix nobody's told you. One ball will be drawn. A bet pays if its colour comes up, so on a scale where winning is one, a bet is worth its probability.

@list heading="Two decisions" items="I: bet on red, or bet on black@In the first|II: bet on red or yellow, or on black or yellow@In the second"
In the first decision, you choose between a bet on red and a bet on black. In the second, between a bet on red or yellow and a bet on black or yellow. Most people choose red in the first, and black or yellow in the second.

@art known-chance
In both, the pick is the bet whose chance is known. Red is exactly thirty in ninety. Black or yellow is exactly sixty in ninety.

@chapter Score the bets
@math heading="Let p be the chance of black" items="red:  1/3@red is a third;;black:  p@black is p;;red or yellow:  1/3 + (2/3 − p) = 1 − p@one minus p;;black or yellow:  p + (2/3 − p) = 2/3@two thirds"
Let p be your credence that the ball is black. Then yellow is two thirds minus p. Score each bet by its chance of winning. Red is a third. Black is p. Red or yellow is one minus p. And black or yellow is two thirds.

@math heading="The two choices as inequalities" items="red over black:  1/3 > p@a third is greater than p;;black or yellow over red or yellow:  2/3 > 1 − p,  so p > 1/3@greater than a third"
Red beats black exactly when a third is greater than p. Black or yellow beats red or yellow exactly when two thirds is greater than one minus p, which means p is greater than a third.

@art no-overlap
So the popular pair needs p below a third and above a third. No credence does both. And at exactly a third, the bets tie in both decisions. The pattern is inconsistent with any probability of black, and so with expected utility, whatever the utilities.

@chapter Not risk aversion
@words text="Same prize, same terms"
It's tempting to call this risk aversion. It isn't. Red and black pay the same prize on the same terms, so any utility for the prize multiplies both scores by the same factor, and leaves their order alone. The preference is for a known probability. That's called ambiguity aversion.

@math heading="Black at a quarter" items="I:  red 1/3 beats black 1/4@In the first decision;;II:  red or yellow 3/4 beats black or yellow 2/3@In the second"
Suppose you believe black is a quarter. Then in the first decision, red at a third beats black at a quarter. In the second, red or yellow at three quarters beats black or yellow at two thirds. A believer in a quarter bets on red twice. The popular pattern bets on red once.

@chapter A rule that fits
@art three-mixes
One rule does reproduce the pattern. Let the possible mixes be zero, thirty or sixty black balls, and score each bet by its worst case. Red wins a third in every mix. Black can win nothing. Red or yellow can fall to a third, while black or yellow wins two thirds in every mix.

@art worst-case-pick
So the worst case rule picks red in the first decision, and black or yellow in the second. But give each mix probability a third and average, and red ties black, and the two pairs tie too. Averaging erased the difference between known and unknown.

@chapter Which view?
@art frosted-window
So the real question is what to do behind a frosted window. You don't know the mix. Should you act as if you had a credence anyway, or treat not knowing as something different?

@words text="Is ignorance a credence of one third?"
A defender of the pattern says ignorance isn't the same as a credence of a third, and someone with no basis for any p has no reason to average. A critic answers that a credence is what betting behaviour reveals, and that refusing to assign one is declining to treat the bets as bets.

@chapter Where people slip
@list heading="Common slips" items="Treating ambiguity aversion as risk aversion@The first|Assuming ignorance means a credence of 1/3@The second|Reading it as a fact about psychology@the third"
The first slip is treating ambiguity aversion as risk aversion. The second is assuming ignorance means a credence of a third. That's a choice, and it turns the unknown into a known. And the third is reading the inconsistency as a fact about psychology. It's a statement about the pair of choices, not about how many people choose that way, or why.

@end text="Try every credence for black"
You can try every credence for black and switch to the worst case rule, on Learn. That's learn dot get er done dot I O.
