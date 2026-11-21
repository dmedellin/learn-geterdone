---
format: long
lesson: justice-and-collective-choice/the-original-position-and-maximin
title: Rawls's veil of ignorance as a decision table
thumb: Choose before you know your place
---

@chapter The question
@title text="The Original Position and Maximin" sub="Justice and Collective Choice" art=thumb
Suppose you must pick how a society is arranged, before learning which place in it will be yours. You might be among the worst off, in the middle, or among the best off. What would you choose?

@art veil
Rawls called that chooser's situation the original position, and the ignorance of your own place, the veil. His claim is that principles chosen under the veil are fair, because no one can tailor them to their own advantage. The argument is only worth testing if it can be written down. And it can.

@chapter The table
@math heading="Two societies, three places" items="equal:  5,  5,  5@everyone has five;;unequal:  2,  8,  20@the worst place has two"
Take two societies. In one, everyone has five units of welfare. In the other, the worst place has two, the middle has eight, and the best has twenty. The unknown is your place, so the table has three states: bottom, middle and top.

@chapter Maximin
@art floor-bars
Maximin scores each act by its worst payoff, and chooses the act whose worst payoff is largest. So you read off each society's worst entry, and ignore the rest of the row.

@math heading="Maximin" items="equal:  worst 5@five for;;unequal:  worst 2@two for;;choose equal@chooses the equal"
The worst is five for the equal society, and two for the unequal one. The larger worst case is five, so maximin chooses the equal society. Nothing about the eight or the twenty entered the calculation.

@chapter Equal chances
@math heading="Laplace: each place 1/3" items="equal:  average 5@averages five;;unequal:  (2 + 8 + 20) / 3 = 10@two plus eight;;choose unequal@this rule chooses"
Now give each place the same chance, as Laplace's rule does. The equal society averages five. The unequal one averages two plus eight plus twenty, over three, which is ten. So this rule chooses the unequal society.

@art two-rules-split
Same table, same chooser, opposite verdicts. The difference lies wholly in what each rule is willing to ignore. The rules differ about one thing: whether a gain of fifteen at the top can make up for a loss of three at the bottom.

@chapter Rawls and Harsanyi
@list heading="Rawls: when maximin is reasonable" items="No trustworthy basis for probabilities@no trustworthy basis|Little care for gains above the minimum@cares little|The worst outcome is hardly bearable@hardly bearable"
Rawls's case for maximin isn't that people dislike risk. It's that the choice has three features. The chooser has no trustworthy basis for probabilities. The chooser cares little for gains above the guaranteed minimum. And the worst outcome of a rejected society would be hardly bearable. Where those hold, looking only at the floor is reasonable.

@words text="No reason to favour any place" sub="so give each an equal weight"
Harsanyi's reply denies the first feature. A chooser who knows nothing about their place has no reason to favour one place over another. Equal weights, he argued, are what that ignorance amounts to. Each side argues validly from its premises. The lab computes both, and can't say which premise is right.

@chapter Lifting the veil
@art lifting-veil
What would it be worth to peek?

@math heading="The value of lifting the veil" items="know your place:  (5 + 8 + 20) / 3 = 11@learned their place;;behind the veil:  10@the best;;difference:  1@The difference"
One more figure. A chooser who learned their place before choosing would take the equal society at the bottom, where it pays five against two, and the unequal one anywhere else. That's five plus eight plus twenty, over three, which is eleven. The best without that knowledge is ten. The difference, one, is the value of lifting the veil.

@art close-call
In a close call, the unequal society pays five, six and seven, against five, five and five. Maximin finds the same worst case in both, and can't separate them. The average separates them at once, six against five. A tie under maximin means the rule has run out of information.

@chapter Where people slip
@list heading="Common slips" items="Thinking Rawls assumes risk aversion about money@The first|Reading the veil as ignorance of everything@The second|Taking a maximin tie for equality@And the third"
The first slip is thinking Rawls assumes people are risk averse about money. Maximin never adds, so it doesn't use the other entries at all. The second is reading the veil as ignorance of everything. The chooser knows the table, just not their place. And the third is taking a maximin tie for equality.

@chapter Try it
@art weighted-places
Now try the lesson's suggestion. Make the bottom place much more likely: four fifths, then one tenth, and one tenth. Work out expected utility for each society. You should get five against twenty two fifths, so the verdict moves to the equal society, while maximin stays put.

@end text="Choose behind the veil"
You can change the table and the rule yourself, on Learn. That's learn dot get er done dot I O.
