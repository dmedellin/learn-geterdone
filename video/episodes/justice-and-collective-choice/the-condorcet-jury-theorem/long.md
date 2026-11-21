---
format: long
lesson: justice-and-collective-choice/the-condorcet-jury-theorem
title: The Condorcet jury theorem: when crowds are wise, and when they aren't
thumb: Better than chance, then better together
---

@chapter The question
@title text="The Condorcet Jury Theorem" sub="Justice and Collective Choice" art=thumb
Does a group vote better than a person? Condorcet found a case where you can compute the answer exactly. A jury, deciding a question of fact, like whether the accused did it.

@art jury-box
Suppose each of n jurors is right with probability p, whatever the others think. And the verdict is whatever more than half of them say. Then the chance that the majority is right is just a sum you can work out.

@chapter Three jurors
@math heading="Three jurors, each right with 3/5" items="all three right:  (3/5)·(3/5)·(3/5) = 27/125@All three;;exactly two:  3·(3/5)·(3/5)·(2/5) = 54/125@Exactly two;;majority right:  81/125@So the majority"
Take three jurors, each right with probability three fifths. The majority is right when at least two are. All three are right with probability twenty seven over a hundred and twenty five. Exactly two are right in three ways, depending on who's wrong, for fifty four over a hundred and twenty five. So the majority is right with probability eighty one over a hundred and twenty five.

@words text="81/125 = 0.648" sub="a single juror: 3/5 = 75/125"
That's point six four eight. A single juror is right with three fifths, which is seventy five over a hundred and twenty five. So the jury is better than its members, by a little.

@chapter More voters
@art rising-curve
With eleven jurors, still at three fifths each, the majority is right about seventy five percent of the time. The pattern is general. If p is above one half, every added pair of jurors raises the chance, and it tends to certainty.

@art falling-curve
But it reverses on the other side. Three jurors each right with two fifths make a majority right with forty four over a hundred and twenty five, which is less than two fifths. Eleven such jurors get about a quarter. Below one half, the bigger the crowd, the worse it does.

@art coin-flip
And at exactly one half, the crowd gains nothing. Eleven jurors, each a coin flip, are right with probability one half. The size of the group just magnifies whatever competence is already there.

@chapter What it needs
@art shared-newspaper
Two strong assumptions carry the result. The first is independence. Voters who read the same newspaper aren't independent. If each follows a newspaper that's right with three fifths, a million voters are right together with three fifths, and no higher.

@words text="A fact to be right about" sub="not a tax rate, not a way of life"
The second is that there's a fact to be right about, and voters are better than chance at finding it. A vote on a tax rate, or a way of life, isn't an estimate of anything. The theorem's weight rests on the question being of the first kind.

@chapter The pivotal voter
@math heading="One juror decides" items="three jurors:  2·(3/5)·(2/5) = 12/25@two times;;eleven at 3/5:  about 0.20@eleven jurors;;eleven coin flips:  63/256, about 0.25@coin flipping"
The chance that one juror decides the verdict is a different quantity. With three jurors, you decide only if the other two split, which happens two ways: two times three fifths times two fifths, twelve twenty fifths. With eleven jurors at three fifths it's about point two. With eleven coin flipping jurors, sixty three over two hundred and fifty six.

@art tiny-pivot
That probability shrinks as the electorate grows, and in a national election it's very small. That's the paradox of the pivotal voter. A vote's benefit is the chance it decides, times what's at stake. The lab computes the first factor, not the second.

@chapter Where people slip
@list heading="Common slips" items="A large electorate is wise whatever its competence@The first|Reading the theorem as about preferences@The second|A small pivotal chance makes a vote worthless@And the third"
The first slip is believing a large electorate is wise whatever its competence. Below one half, size makes it worse. The second is reading the theorem as being about preferences. It's about a fact. And the third is concluding that a small pivotal probability makes a vote worthless. That needs a premise about the stakes.

@chapter Try it
@words text="n = 11:  p = 3/5 vs p = 2/5" sub="compare the pivotal probabilities"
Try the lesson's check. First set n to one, and see that a majority of one is just the voter. Then compare the pivotal probabilities of eleven jurors at three fifths, and at two fifths. They're the same. Work out why.

@end text="Compute a jury"
You can compute any jury up to a hundred and one, on Learn. That's learn dot get er done dot I O.
