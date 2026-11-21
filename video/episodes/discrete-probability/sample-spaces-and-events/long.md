---
format: long
lesson: discrete-probability/sample-spaces-and-events
title: Sample spaces and events: get the outcomes right first
thumb: Pairs, not sums
---

@chapter The question
@title text="Sample Spaces and Events" sub="Discrete Probability" art=thumb
Before you can say how likely something is, you have to say what can happen. A probability model is just that: a set of outcomes, and a probability for each one.

@words text="Most mistakes are about the outcomes"
And here's the warning that runs through this whole course. Almost every mistake in probability is a mistake about what the outcomes are. Not the arithmetic. The outcomes.

@chapter Three words
@math heading="The vocabulary" items="S = all possible outcomes@the sample space;;s ∈ S  one outcome@An outcome;;E ⊆ S  an event@an event"
So let's pin down three words. The sample space, written S, is the set of all possible outcomes of an experiment. An outcome is one element of S. And an event is a subset of S, the outcomes you're asking about.

@list heading="Outcomes must be" items="Mutually exclusive: no two happen together@mutually exclusive|Exhaustive: at least one happens@exhaustive"
The outcomes have two jobs. They must be mutually exclusive, so no two happen together. And they must be exhaustive, so at least one happens. Put together, exactly one outcome happens every time. Overlap nowhere, cover everything.

@chapter Two dice, two models
@art two-dice-grid
Roll two dice. In model A, the sample space is the thirty-six ordered pairs, from one, one up to six, six, and all of them are equally likely.

@art sums-bars
In model B, the sample space is the eleven possible sums, two through twelve. That's a perfectly legitimate sample space too. But its outcomes are not equally likely. A sum of seven arises six ways. A sum of two arises only one way.

@words text="Keep outcomes fine" sub="fine enough that symmetry justifies equal likelihood"
That's the granularity trap. Treat the sums as equally likely and your answers come out wrong. The fix is to keep your outcomes fine enough that symmetry justifies calling them equally likely. For dice, that means pairs, not sums.

@chapter Events are sets
@art venn-events
Since an event is a subset, everything you know about sets carries straight over, with no changes at all. Here are two events, A and B, inside the sample space, and the overlap where both happen at once. Every way of combining them in words has a name in sets.

@math heading="Words to sets" items="A or B  =  A ∪ B@Or is union;;A and B  =  A ∩ B@and is intersection;;not A  =  Ā = S \ A@not A;;A but not B  =  A \ B@A but not B;;A ∩ B = ∅  mutually exclusive@cannot both happen"
Or is union. And is intersection. Not A is S minus A. A but not B is the set difference. And when A and B cannot both happen, their intersection is empty, and we call them mutually exclusive.

@art complement-region
De Morgan's law gets used all the time. Not A or B is the same as neither A nor B, and that's often the easier event to count.

@chapter Probability as a ratio
@math heading="Equally likely outcomes" items="P(E) = |E| / |S|@divided by"
When the outcomes of a finite sample space are equally likely, the probability of an event E is the number of outcomes in E divided by the number of outcomes in S. Every probability in the early lessons of this course is that ratio, worked out with the tools from counting.

@chapter Worked example
@art coin-triples
Flip three coins. What's the probability of exactly two heads? Take the outcomes as ordered triples. There are eight, all equally likely.

@math heading="Exactly two heads" items="|S| = 8 ordered triples@eight;;E = {HHT, HTH, THH}@three of them;;P(E) = 3/8@three eighths;;✗  1/4  from number of heads@one quarter"
Out of those eight, three of them qualify: heads heads tails, heads tails heads, and tails heads heads. So the answer is three eighths. If you'd used number of heads as your outcomes, you'd have four possibilities and might answer one quarter. That's exactly the error the fine model prevents.

@chapter Where people slip
@list heading="Common slips" items="Choosing outcomes too coarse@too coarse|Assuming equal likelihood without a symmetry@without a symmetry|Treating mutually exclusive as independent@as independent"
First, choosing outcomes too coarse. Sums of dice, numbers of heads and unordered pairs are all fine descriptions, and none of them is equally likely. Second, assuming equal likelihood without a symmetry. A loaded die has the same sample space with different probabilities. Third, treating mutually exclusive as independent.

@art disjoint-circles
Those last two are nearly opposite. If two exclusive events both have positive probability, knowing one happened tells you the other didn't. That's strong dependence, not independence.

@chapter Try it
@words text="A: sum is 7 · B: a double · C: first die 4" sub="each has 6 of the 36 pairs"
Your turn. With two dice, let A be the sum is seven, B be a double, and C be the first die is four. Each holds six of the thirty-six pairs. Which pairs of events are mutually exclusive? Then find the probability of A or C, remembering the outcome they share.

@end text="Model it with fine outcomes"
The full lesson, with practice and recall questions, is on Learn. That's learn dot get er done dot I O.
