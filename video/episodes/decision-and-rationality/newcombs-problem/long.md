---
format: long
lesson: decision-and-rationality/newcombs-problem
title: Newcomb's problem: one box or two?
thumb: Two valid arguments, two answers
---

@chapter Two boxes
@title text="Newcomb's Problem" sub="Decision and Rationality" art=thumb
Here's a problem where two perfectly valid arguments recommend opposite acts. It's Robert Nozick's version of William Newcomb's problem.

@art two-boxes
Two boxes sit in front of you. Box A is open, and holds a thousand dollars. Box B is closed, and holds either a million dollars or nothing. You may take both boxes, or box B alone.

@art predictor
A predictor, who has been right in the past, has already decided what to put in B. The million, if it forecast you'd take only B. Nothing, if it forecast you'd take both. The boxes are filled. Now you choose.

@math heading="The table, in dollars" items="one-box:  full 1,000,000,  empty 0@one box;;two-box:  full 1,001,000,  empty 1,000@both boxes"
Write it as a table with two states, box full and box empty. Take one box: a million if full, nothing if empty. Take both boxes: a million and a thousand if full, a thousand if empty. Dollars are scored at face value here.

@art empty-and-full
So the closed box is in one of two states, and you can't see which. Full, or empty. Everything turns on how you treat that state when you choose: as already settled, or as something your choice tells you about.

@chapter The dominance argument
@art row-ahead
The first argument is dominance. The boxes are already filled, and what you do now can't change them. Whichever state you're in, the two box row is a thousand higher than the one box row. So two boxing is better in every state. That's a valid argument.

@chapter The evidential argument
@math heading="Accuracy a" items="EU(one-box) = a · 1,000,000@one boxer;;EU(two-box) = (1 − a) · 1,001,000 + a · 1,000@two boxer"
The second argument uses the predictor's record. Let a be the chance the predictor is right about whoever stands before it. Then a one boxer finds a full box with probability a, and a two boxer finds a full box with probability one minus a. Score each act with those probabilities.

@math heading="At accuracy 9/10" items="EU(one-box) = 900,000@nine hundred thousand;;EU(two-box) = 101,000@a hundred and one thousand"
At an accuracy of nine tenths, one boxing scores nine hundred thousand. Two boxing scores a hundred and one thousand. So the evidential rule says take one box, while dominance, on the same table, says take two.

@chapter Where they part
@math heading="The tie" items="a · 1,000,000 = 1,001,000 − a · 1,000,000@Set the scores equal;;a = 1001/2000@a thousand and one over two thousand"
Where does the evidential verdict turn? Set the scores equal, and a comes out at a thousand and one over two thousand. Just above a half. At a coin flip, a half, one boxing scores five hundred thousand and two boxing five hundred and one thousand, so both rules say two boxes.

@art accuracy-dial
So the rules agree below the threshold, and part above it. And the threshold is a hair over a half, because the extra thousand is small beside the million. A predictor right fifty one times in a hundred already favours one boxing, on the evidential rule. The problem doesn't need a near perfect predictor.

@chapter What's really at issue
@words text="Look at who ends up rich." sub="The money is there or not already."
The one boxer says: look at who ends up rich. The two boxer says: the money's there or not already, and a rational chooser takes what she can. Each says a valid thing.

@art fixed-vs-news
Dominance takes the states as fixed, whatever you do. The evidential argument treats the act as news about the state. Whether the act can be treated as independent of what's in the box is the premise the whole problem exists to test.

@chapter Two quick answers that fail
@list heading="Two quick answers" items="The record is irrelevant: the boxes are filled@One says|High accuracy settles it@The other says"
Two quick answers fail. One says the record is irrelevant because the boxes are already filled. That confuses what the act causes with what it's evidence for, and the record does move the evidential figure from a hundred and one thousand to nine hundred thousand. The other says a high accuracy settles the question. It settles only the evidential rule, which is the rule in dispute.

@chapter Where people slip
@list heading="Common slips" items="Treating the record as irrelevant, or decisive@The first|Thinking one argument is invalid@The second|Expecting a high accuracy to be needed@the third"
The first slip is treating the predictor's record as irrelevant, or as decisive. The second is thinking one of the two arguments is invalid. Both are valid. The disagreement is over a premise, not a step. And the third is expecting a high accuracy to be needed. The switch is just above a half.

@end text="Move the accuracy, switch the rule"
You can move the predictor's accuracy and switch between the two rules, on Learn. That's learn dot get er done dot I O.
