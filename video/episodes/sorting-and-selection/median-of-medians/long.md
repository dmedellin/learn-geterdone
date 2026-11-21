---
format: long
lesson: sorting-and-selection/median-of-medians
title: Median of medians: linear-time selection with no luck needed
thumb: Why groups of five
---

@chapter The question
@title text="Median of Medians" sub="Sorting and Selection" art=thumb
Quickselect is linear, in expectation. Can you get linear time on every input, with no randomness at all? You can, by choosing a pivot that's guaranteed to be close to the middle. And the reason it uses groups of five is the best part.

@chapter Choosing the pivot
@art groups-of-five
Split the array into groups of five consecutive elements. Sort each little group and take its median. That's linear work, since five is a constant.

@list heading="Median of medians" items="Groups of 5, median of each@Groups of five|Select the median of those medians, recursively@recursively|Partition around it@Partition|Recurse into the surviving side@surviving side"
So that's groups of five, a median of each. Then find the median of those medians, by running the whole selection algorithm on them, recursively. That's the pivot. Partition around it. If its rank is the one you want, stop. Otherwise recurse into the surviving side. That's two recursive calls in all.

@chapter The guarantee
@art three-below
Why is this pivot good? Half the group medians are at most p, by definition of a median. In each of those groups, the median is at most p, and so are the two elements below it. That's three elements per group.

@math heading="Groups of five" items="at least 3(⌈⌈n/5⌉/2⌉ − 2) on each side@three times;;≈ 3n/10 discarded@three n over ten;;≤ 7n/10 survive@seven n over ten"
Set aside two groups, the one containing p and a last group that might not be full. So at least three times the ceiling of half the group count, minus two, lie on each side. About three n over ten are discarded, and at most seven n over ten survive.

@art middle-band
So the pivot is guaranteed to sit in the middle forty percent. It isn't the true median, and it doesn't need to be. The proof only uses a guaranteed fraction on each side.

@chapter Solving the recurrence
@art two-calls
So each round makes two recursive calls. One on the medians, a fifth of the array. And one on the survivors, at most seven tenths. Together, they're a little smaller than the original.

@math heading="T(n) ≤ T(n/5) + T(7n/10) + cn" items="level 0:  cn@level zero;;level 1:  c(1/5 + 7/10)n = c(9/10)n@level one;;level 2:  c(9/10)²n@level two;;total:  cn · 1/(1 − 9/10) = 10cn@In total"
With two different fractions, the master theorem doesn't fit. A recursion tree does. Level zero costs c n. Level one costs a fifth plus seven tenths, which is nine tenths of that. Level two, nine tenths squared. In total, ten c n.

@art shrinking-levels
The whole argument is one comparison: do the fractions add to less than one? A fifth plus seven tenths is nine tenths. The lab computes that as an exact fraction, because nought point eight nine nine recurring isn't an argument.

@chapter One round at 45
@math heading="n = 45, seeded shuffle" items="medians:  24 35 21 27 14 38 8 16 25@nine group medians;;median of medians:  24@is twenty four;;23 below · 21 above@twenty three below"
Here's one round at forty five elements. The nine group medians are twenty four, thirty five, twenty one, twenty seven, fourteen, thirty eight, eight, sixteen and twenty five. Their median is twenty four. Partitioning leaves twenty three below and twenty one above.

@words text="promised 9 · discarded 21" sub="true median of 1…45 is 23"
The guarantee at this size was nine. The round discarded twenty one. That gap is the slack a proof about every input gives away, and the lab prints both. Notice too, the pivot is twenty four, while the true median is twenty three.

@chapter Why five
@math heading="Group size g" items="g = 3:  1/3 + 2/3 = 1@groups of three;;g = 5:  1/5 + 7/10 = 9/10@groups of five;;g = 7:  1/7 + 5/7 = 6/7@groups of seven"
The group size sets both fractions. With groups of three, they're a third and two thirds, summing to exactly one. With groups of five, nine tenths. With groups of seven, six sevenths.

@art flat-levels
And exactly one is a disaster. The tree's levels stop shrinking. Every level costs n, and there are about log n of them. That's n log n, the same as sorting. Three isn't slightly worse. It's a different complexity class. Five is the smallest odd size that works.

@words text="299 vs 131 comparisons" sub="median of medians vs quickselect, n = 45"
The guarantee isn't free. On the same forty five elements, median of medians spends two hundred and ninety nine comparisons, and quickselect a hundred and thirty one. That's the price of removing the word expected.

@chapter Where people slip
@list heading="Common slips" items="Believing the pivot is the true median@The first|Reaching for the master theorem@The second|Treating group size as a small change@And the third"
The first slip is believing the pivot is the true median. The second is reaching for the master theorem, which doesn't fit two different fractions. And the third is treating the group size as a detail. Three loses everything.

@chapter Try it
@words text="Level sums for g = 3, 5, 7" sub="n = 45"
Your turn. For groups of three, five and seven, write the two fractions, add them, and say which recurrences are linear. Then check the total for groups of five comes to ten n.

@end text="Change the group size"
You can set the group size and watch the level sums converge or not, on Learn. That's learn dot get er done dot I O.
