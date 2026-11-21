---
format: long
lesson: discrete-probability/computing-probabilities
title: Computing probabilities: count, count, divide
thumb: The hard part is counting
---

@chapter The method
@title text="Computing Probabilities" sub="Discrete Probability" art=thumb
When every outcome is equally likely, every probability is a ratio of two counts. Count the event, count the sample space, and divide. That means all of counting is now your toolkit for probability.

@math heading="Two rules" items="P(E) = |E| / |S|@the size of E;;P(Ē) = 1 − P(E)@one minus"
The probability of E is the size of E over the size of S. And the complement rule says the probability of not E is one minus the probability of E, because the outcomes outside E number the size of S minus the size of E.

@chapter A poker flush
@art card-fan
Deal five cards from a fifty-two card deck. What's the chance of a flush, five cards all of one suit? Start with the denominator. It's a count too, and often the easier one.

@math heading="P(flush)" items="|S| = C(52, 5) = 2 598 960@fifty-two choose five;;|E| = 4 · C(13, 5) = 4 · 1287 = 5148@choose the suit;;P = 5148 / 2 598 960 ≈ 0.00198@about zero point"
There are fifty-two choose five hands, which is two million, five hundred ninety-eight thousand, nine hundred sixty. For a flush, choose the suit, four ways, then five of its thirteen cards, which is twelve hundred eighty-seven. That's fifty-one forty-eight flushes. So the probability is about zero point zero zero one nine eight.

@words text="Includes straight flushes" sub="excluding them subtracts 40"
One detail. That count includes the straight flushes. If you want to exclude them, subtract forty.

@chapter At least one six
@art four-cubes
Now roll four dice. What's the chance of at least one six? Counting that directly is messy, because you'd need inclusion and exclusion over the four dice. The complement is one line.

@math heading="P(at least one 6)" items="= 1 − P(no 6)@one minus;;= 1 − (5/6)⁴@five sixths;;= 1 − 625/1296@six hundred twenty-five;;= 671/1296 ≈ 0.518@six hundred seventy-one"
It's one minus the chance of no six. That's one minus five sixths to the fourth, which is one minus six hundred twenty-five over twelve ninety-six. So you get six hundred seventy-one over twelve ninety-six, about zero point five one eight.

@art overlap-count
Most people's first answer is four times one sixth, which is two thirds. That adds the four events die i shows a six, but they overlap. A roll of six, six, one, two gets counted twice. With six dice the same reasoning would give a probability of one. Adding only gives an upper bound.

@chapter The birthday problem
@math heading="n people, 365 birthdays" items="P(shared) = 1 − (365 · 364 ⋯ (365 − n + 1)) / 365ⁿ@one minus"
Here's a famous one. With n people and three hundred sixty-five equally likely birthdays, the chance that some pair shares a birthday is one minus the product three sixty-five times three sixty-four and so on, down to three sixty-five minus n plus one, all over three sixty-five to the n.

@art birthday-curve
Plug in numbers. Ten people give about zero point one one seven. Twenty give about zero point four one one. At twenty-three it passes one half, at zero point five zero seven. Thirty give zero point seven zero six, and fifty give zero point nine seven.

@art pairs-web
Twenty-three surprises nearly everyone. The reason is that the question is about pairs. Twenty-three people form two hundred fifty-three pairs, and each pair has about a one in three sixty-five chance of matching. Compare two fifty-three with three sixty-five, not twenty-three.

@art pigeonholes
And notice it's a different claim from the pigeonhole principle. Three hundred sixty-seven people guarantee a match. Twenty-three make one likely. Certainty and high probability are different claims.

@chapter Unequal outcomes
@math heading="Not equally likely" items="P(s) ≥ 0,  Σ P(s) = 1@add up to one;;P(E) = Σ_{s ∈ E} P(s)@add up the probabilities"
And when the outcomes aren't equally likely? Then you assign a probability to each outcome directly. They must be non-negative and add up to one. Then, to get the probability of an event, you add up the probabilities of the outcomes in it. A loaded die, a biased coin and a weighted lottery all work this way.

@chapter Where people slip
@list heading="Common slips" items="Mixing ordered and unordered counts@ordered and unordered|Counting at least one directly@directly|Confusing certainty with high probability@certainty"
First, counting the event with a different model from the space. If the denominator counts ordered outcomes, the numerator must too, and mixing ordered and unordered counts is the commonest error. Second, counting at least one directly, which makes overlapping cases. Third, confusing certainty with high probability.

@words text="Outside [0, 1]? A counting error."
And there's a free check. Any probability below zero or above one is a counting error.

@chapter Try it
@words text="Five cards: P(exactly two aces)?" sub="C(4, 2) · C(48, 3) out of C(52, 5)"
Your turn. Find the chance of exactly two aces in a five card hand. Choose two of the four aces and three of the forty-eight other cards, and divide by all the hands. Then check yourself: summing over zero to four aces must give back every hand.

@end text="Count the space, count the event"
The full lesson, with practice and recall questions, is on Learn. That's learn dot get er done dot I O.
