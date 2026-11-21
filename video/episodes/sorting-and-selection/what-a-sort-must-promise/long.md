---
format: long
lesson: sorting-and-selection/what-a-sort-must-promise
title: Stable, in place, adaptive: what a sort really promises
thumb: Minor key first
---

@chapter The question
@title text="What a Sort Must Promise" sub="Sorting and Selection" art=thumb
Two sorts, both n log n, both give you the keys in order. Are they interchangeable? Not even close. Getting the order right is the least a sort promises. There are three more promises, and they're independent.

@chapter Stability
@art stable-ties
A sort is stable if, whenever two records have equal keys, the one that came first in the input also comes first in the output. That's a claim about the algorithm, on every input, not about one run.

@art tagged-records
Stability only talks about equal keys. A sort that mixes up unequal keys isn't unstable, it's broken. So to see stability, you need repeats, and something the key doesn't decide. Here, that's the starting position, called a tag.

@math heading="7 3 7 1 9 3 5 1, tagged" items="input:  7#1 3#2 7#3 1#4 9#5 3#6 5#7 1#8@tag the list;;insertion, merge:  1#4 1#8 3#2 3#6 5#7 7#1 7#3 9#5@insertion sort;;selection:  1#4 1#8 3#6 3#2 5#7 7#3 7#1 9#5@selection sort"
Tag the list seven, three, seven, one, nine, three, five, one by position. Insertion sort and merge sort return the threes as two then six, and the sevens as one then three. Selection sort returns the threes as six then two, and the sevens as three then one. Both pairs reversed.

@art long-swap
Why? Selection sort puts the minimum in place with a long range swap, and that swap can jump one equal key right over its twin.

@words text="One counterexample refutes · zero proves nothing" sub="8! = 40 320 lists of length 8"
And notice the asymmetry. One reversed pair refutes stability. Zero reversed pairs on one list proves nothing, because there are forty thousand three hundred and twenty lists of that length. Stability is proved from the algorithm. Insertion sort never moves past an equal key, and merge takes from the left run on a tie.

@chapter In place, and adaptive
@list heading="Two more promises" items="In place: Θ(1) extra memory@In place|Adaptive: cheaper when nearly sorted@Adaptive"
In place means the extra memory is constant, the input aside. Adaptive means input that's already nearly sorted costs less. Insertion sort is linear on sorted input, and quadratic on reversed.

@art promise-grid
These cut across everything. Merge sort is stable, but not in place or adaptive. Heapsort is in place, but not stable or adaptive. Insertion sort is all three, and quadratic. Nothing in n log n implies any of them, so name the promise you need before you pick.

@chapter What it may look at
@words text="Comparison sort: only asks a ≤ b" sub="needs at least ⌈log₂ n!⌉ comparisons"
The fourth promise is about what a sort can look at. A comparison sort only asks whether one key is at most another. No such sort can handle every array of n keys in fewer than the ceiling of log two of n factorial comparisons. A sort that reads the key itself, like counting sort, is outside that bound, not better than it.

@chapter Two keys, two passes
@art two-passes
Here's what stability is for. Say you want records ordered by a major key, with ties broken by a minor key. Sort by the minor key first, then by the major key, both stable.

@list heading="Why it works" items="Second pass orders the major keys@orders the major|Stable, so ties keep the first pass's order@stable|First pass put minor keys in order@first pass"
The second pass orders the major keys. Inside a tie, it's stable, so it keeps the order the first pass left. And the first pass sorted everything by minor key. So within each major key, minor keys ascend. The only thing used was stability.

@art tie-order
Run them the other way and the last pass orders the whole list by minor key. You get a correct sort of a different thing. The key whose order survives is the one sorted last. That's also the whole correctness argument of radix sort.

@chapter Where people slip
@list heading="Common slips" items="Reading stability off the complexity class@The first|Sorting by the primary key first@The second|Taking zero violations as proof@And the third"
The first slip is reading stability off the complexity class. Merge sort and heapsort share a class and disagree on both promises. The second is sorting by the primary key first, which is exactly backwards. And the third is taking a clean run as proof. The lab says no reordering seen, not stable.

@chapter Try it
@words text="Sort by department, then by name" sub="two stable passes, which first?"
Your turn. Take a few records with a department and a name. Order them by department, with names in order inside each. Say which pass runs first, and why, then try it the wrong way round.

@end text="Catch an unstable sort"
You can tag your own lists and watch which sorts keep the tags in order, on Learn. That's learn dot get er done dot I O.
