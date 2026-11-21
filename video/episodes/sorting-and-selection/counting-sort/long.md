---
format: long
lesson: sorting-and-selection/counting-sort
title: Counting sort: linear time, as long as you name k
thumb: Work is n plus k
---

@chapter The question
@title text="Counting Sort" sub="Sorting and Selection" art=thumb
No comparison sort can beat n log n. So how does counting sort run in linear time? It doesn't beat the bound. It steps around it, by never comparing two keys at all.

@chapter Keys as indices
@art tally-bins
If the keys are integers from zero to k minus one, you can use them as array indices. That's the whole idea. Tally them, turn the tally into running totals, then place each record where its total says.

@art index-jump
A record with key three goes straight to counter three. No search and no comparison. The key itself is the address.

@list heading="Three passes" items="Tally: k counters, one increment per record@Tally|Prefix: replace each counter with a running total@Prefix|Place: back to front, one write each@Place"
Tally: zero k counters, then add one for each record. Prefix: replace each counter with the running total, so counter i holds how many keys are at most i. Place: walk the records from back to front, writing each into the slot its counter names, then decrement the counter.

@chapter Twelve keys
@math heading="4 1 3 4 3 0 2 4 1 3 4 2" items="tally:  1 2 2 3 4@the tally;;prefix:  1 3 5 8 12@prefix sums;;out:  0 1 1 2 2 3 3 3 4 4 4 4@placing from the back;;work:  n + k = 17@seventeen"
Twelve keys from zero to four. The tally is one, two, two, three, four: one zero, two ones, and so on. The prefix sums are one, three, five, eight, twelve. Placing from the back gives zero, one, one, two, two, three, three, three, four, four, four, four. The work is n plus k, seventeen.

@art prefix-slots
The prefix sum says where each run ends. The four records with key four own slots nine to twelve, and prefix of four is twelve, the last of them. That's why the placement counts down.

@words text="No two keys are ever compared" sub="⌈log₂ 12!⌉ = 29 doesn't apply"
And no step ever looks at two keys together. The lower bound is about algorithms whose only access to keys is a comparison. For twelve keys it says twenty nine. Counting sort makes none. It's outside the theorem, not a counterexample to it.

@chapter The second term
@math heading="12 keys" items="k = 5:  12 + 5 = 17@a range of five;;n log₂ n ≈ 43@n log two n"
Here's the catch. The cost is linear in n plus k, which isn't the same as linear in n. Twelve keys over a range of five costs seventeen, against n log two n of about forty three. Counting sort wins comfortably.

@words text="32-bit key: 12 + 2³² = 4 294 967 308" sub="16-bit key: 12 + 65 536"
Now declare a sixteen bit key, and it's twelve plus sixty five thousand five hundred and thirty six. A thirty two bit key, and it's over four billion, with four billion counters for twelve records.

@art wide-range
So you choose it by comparing the terms. It's the right sort when k is about n or smaller: ages, bytes, digits, grades. It's the wrong sort when k is n squared, a machine word, or unknown.

@chapter Why backwards
@art back-to-front
Now the direction. Take all the records with one key value, in input order. Before any are placed, that key's counter points at the last slot of its run. Walking backwards, the last record takes the last slot, the one before takes the one before, and so on. Input order survives. That's stability.

@art forward-flip
Walk forwards with the same bookkeeping, and every run comes out reversed. On the same twelve keys, that's eleven reordered pairs, against zero. The output is sorted both ways. Only the order inside the ties differs, and that's exactly what radix sort depends on.

@words text="Not in place" sub="n output slots + k counters"
One more property. Counting sort isn't in place. It needs n output slots and k counters. It trades memory for the comparisons it doesn't make.

@chapter Where people slip
@list heading="Common slips" items="Calling it linear without naming k@The first|Taking the largest key present as k@The second|Expecting stability for free@And the third"
The first slip is calling it linear without naming k. The second is taking the largest key you happen to have as k. The counters must cover the range keys are drawn from. And the third is expecting stability for free. The placement direction is the only line where it lives.

@chapter Try it
@words text="Sort 2 0 2 1 0 with k = 3" sub="tally, prefix, place from the back"
Your turn. Tag a short list of small keys by position. Tally, prefix sum and place from the back, and check the tags ascend inside every run. Then place forwards and watch them flip.

@end text="Widen the range"
You can declare a wider range and watch the second term take over, on Learn. That's learn dot get er done dot I O.
