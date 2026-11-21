---
format: long
lesson: strings-and-pattern-matching/the-suffix-array-and-what-it-answers
title: The suffix array: sort every suffix, then read off the answers
thumb: Neighbours hold the repeats
---

@chapter The question
@title text="The Suffix Array, and What a Sorted Order Answers" sub="Strings and Pattern Matching" art=thumb
What's the longest substring that appears twice in a text? And how many different substrings does it have? Both questions sound like they need every pair of positions. Sort the text's suffixes, and both answers fall out.

@art suffix-stack
A suffix is everything from some position to the end. The suffix array lists the starting positions of all the suffixes, in sorted, dictionary order. Beside it, the LCP array records, for each suffix, how long a prefix it shares with the one just above it.

@chapter Banana
@math heading="Suffixes of banana, sorted" items="a · ana · anana · banana · na · nana@a, a n a;;sa = 5, 3, 1, 0, 4, 2@starting at;;lcp = 0, 1, 3, 0, 0, 2@overlaps"
Take banana. Its six suffixes, sorted, are a, a n a, a n a n a, banana, n a, and n a n a, starting at five, three, one, zero, four and two. The overlaps with the suffix above are zero, one, three, zero, zero, and two.

@art neighbour-overlap
For example, a n a and a n a n a share a n a, three characters. Banana and n a share nothing. Every entry is a comparison between neighbours only.

@chapter The longest repeat
@words text="longest repeated substring = max LCP" sub="banana: 3 → ana"
Here's the first theorem. The longest repeated substring has length equal to the largest LCP entry. On banana, that's three, and the substring is a n a.

@art contiguous-block
Why? If w occurs at two positions, it's a prefix of two suffixes. In sorted order, every string starting with w sits in one contiguous block. So some adjacent pair in that block shares w. You never need to compare suffixes that aren't neighbours. That word, adjacent, turns every pair into n minus one comparisons.

@chapter Counting distinct substrings
@math heading="Distinct substrings" items="all substrings, with repeats:  n(n + 1)/2@n times n plus one;;distinct = n(n + 1)/2 − Σ lcp@Subtract the sum;;banana: 21 − 6 = 15@twenty one minus six"
The second theorem counts distinct substrings. With repeats, a text of length n has n times n plus one, over two substrings. Subtract the sum of the LCP array, and you get the number of distinct ones. On banana, that's twenty one minus six, fifteen.

@art new-prefixes
Here's why. Each suffix's prefixes are substrings. Credit each substring to the first suffix in sorted order that has it. The prefixes a suffix shares with the one above were already credited, and there are exactly LCP of them. So each suffix adds its length minus its LCP. On banana, that's one, two, two, six, two and two, again fifteen.

@list heading="Two extremes" items="abcdefgh: LCP all 0 → 36 of 36 distinct@a b c d e f g h|aaaaaaaa: LCP sum 28 → 8 of 36 distinct@eight a's"
Two extremes. With a b c d e f g h, every LCP is zero, and all thirty six substrings are distinct. With eight a's, the LCP array is a staircase from zero to seven, summing to twenty eight, and only eight are distinct, the runs of length one to eight.

@art staircase-lcp
Those two are the limits of the identity. No sharing at all keeps every substring distinct. A single repeated letter gives the most sharing a text can have, and the fewest distinct substrings.

@chapter Building it by doubling
@art doubling-rounds
Prefix doubling builds the array fast. Round one sorts positions by their first character. Each later round sorts by a pair of ranks from the round before, which orders the suffixes correctly to twice as many characters, comparing small integers instead of strings.

@math heading="banana" items="round 1:  5, 1, 3, 0, 2, 4@Round one;;round 2:  5, 3, 1, 0, 4, 2@Round two"
On banana, round one gives five, one, three, zero, two, four: the a's, then the b, then the n's. Round two separates everything, giving five, three, one, zero, four, two. Two rounds, twenty one comparisons, matching a sort of the whole strings.

@words text="rounds ≤ ⌈log₂ n⌉" sub="abcdefgh: 1 round"
It stops as soon as every rank is distinct, so it needs at most log two of n rounds, rounded up, and often fewer. Mississippi needs three. A b c d e f g h needs just one, because a single character already separates all eight suffixes.

@chapter Where people slip
@list heading="Common slips" items="Looking for repeats between non-adjacent suffixes@The first|Subtracting the LCP sum from n²@The second|Taking the round count as log₂ n@The third"
The first slip is comparing suffixes that aren't neighbours. It can't help. The second is subtracting the LCP sum from n squared instead of n times n plus one over two. The third is taking the round count as a measurement of log n. It's at most the ceiling, and often less.

@chapter Try it
@words text="mississippi" sub="longest repeat: issi (4)"
Your turn. Sort the eleven suffixes of mississippi, write the LCP array, and check that its largest entry is four, for i s s i. Then subtract the LCP sum from sixty six, and check that fifty three substrings are distinct.

@end text="Sort the suffixes yourself"
You can type any text and watch the suffix array and LCP array answer both questions, on Learn. That's learn dot get er done dot I O.
