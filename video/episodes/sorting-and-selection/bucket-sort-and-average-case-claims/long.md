---
format: long
lesson: sorting-and-selection/bucket-sort-and-average-case-claims
title: Bucket sort's linear time is a promise about your data
thumb: Expected, if the keys agree
---

@chapter The question
@title text="Bucket Sort and Average-Case Claims" sub="Sorting and Selection" art=thumb
Bucket sort is called linear. Randomised quicksort is called expected n log n. Both use the word expected. Only one of them can keep its promise on its own, and the difference is the most useful idea in this course.

@chapter The algorithm
@art scatter
Over a key range from zero to U, with b buckets: put each key x into bucket floor of b x over U. Insertion sort each bucket. Then concatenate the buckets in order. The buckets are equal in width. Nothing makes them equal in how full they are.

@words text="scatter Θ(n) · concatenate Θ(n + b)" sub="the rest is the insertion sorts"
Scattering is one pass, and concatenating is another. Everything else is the insertion sorts, and their cost depends on how many keys land in each bucket. So the analysis is about where the keys fall, not about the algorithm.

@chapter The expected work
@math heading="If every bucket holds n/b keys" items="one bucket:  (n/b)(n/b − 1)/2@A bucket of;;all b:  n(n/b − 1)/2@summed over;;n = 48, b = 12:  48 · 3/2 = 72@forty eight;;n = 48, b = 48:  0@b equal to n"
A bucket of n over b keys costs at most n over b, times n over b minus one, over two. Summed over b buckets, that's n times n over b minus one, over two. At forty eight keys and twelve buckets, it's exactly seventy two. And with b equal to n, it's zero, which is why bucket sort is called linear.

@words text="if the keys are uniform"
But that whole calculation assumed the keys are spread evenly over the range. That's an assumption about the input. The algorithm doesn't check it, and can't.

@chapter Three distributions
@math heading="48 keys, 12 buckets" items="uniform draw:  90@uniform;;clustered in a twentieth:  592@clustered;;confined to one bucket:  582@confined"
Here's the lab, forty eight keys, twelve buckets. A uniform draw costs ninety comparisons, against an expectation of seventy two. Keys clustered in a twentieth of the range put all forty eight into one bucket, and cost five ninety two. Keys confined to the first bucket cost five eighty two.

@art one-bucket
In the clustered case, every key lands in the same bucket. The sort has become one insertion sort over all forty eight keys, with eleven empty buckets beside it.

@art uneven-buckets
All three outputs are sorted. Only the cost moved, and the code didn't change. And look at the uniform draw. Its buckets went four, four, nine, two, three, zero, and so on. One empty, one holding nine. That's what uniform looks like at forty eight keys, so ninety against seventy two isn't a refutation.

@art quadratic-climb
On the clustered family, double n and the work roughly quadruples. A hundred and forty at twenty four keys, five ninety two at forty eight, two thousand two hundred and eighty two at ninety six. That's quadratic, measured.

@chapter Two kinds of expected
@art two-dice
Put the two side by side. Randomised quicksort: for every array, the average over the algorithm's own pivots. Bucket sort: for uniformly drawn keys, the average over the draw. The first averages over coins it controls. The second controls nothing.

@art adversary-keys
That's why one survives a hostile input and the other doesn't. An adversary who picks the array can't move quicksort's expectation, because it never mentioned the array. An adversary who picks the keys puts them all in one bucket, and bucket sort goes quadratic.

@words text="A conditional bound, with a checkable condition"
That doesn't make bucket sort bad. It makes its bound conditional. Hash values and uniformly generated IDs often satisfy it. Prices, word lengths and timestamps of human activity usually don't.

@chapter Where people slip
@list heading="Common slips" items="Quoting O(n) without the hypothesis@The first|Confusing inputs with coin flips@The second|Reading a measured count as the worst case@And the third"
The first slip is quoting linear without the hypothesis. The second is confusing an average over inputs with one over coin flips. And the third is reading five eighty two as the worst case. The worst for forty eight keys is n times n minus one over two, eleven twenty eight, reached only on a reversed bucket.

@chapter Try it
@words text="Build the input that makes it quadratic" sub="n = 48, b = 12"
Your turn. State bucket sort's assumption in one sentence, compute the expected work for your own n and b, and then write down forty eight keys that put everything in one bucket. Say where real keys of that shape might come from.

@end text="Skew the keys yourself"
You can switch the key distribution and watch bucket sort's cost jump, on Learn. That's learn dot get er done dot I O.
