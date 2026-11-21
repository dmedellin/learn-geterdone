---
format: long
lesson: intro-algorithms-sorting/radix-sort-and-bucket-sort
title: Radix sort and bucket sort: linear time, with conditions
thumb: Last digit first, always stable
---

@chapter Museum machines
@title text="Radix Sort and Bucket Sort" sub="Introduction to Algorithms, Sections 8.3 and 8.4" art=thumb
Counting sort is fast when the keys are small. But what about big keys, with many digits? The answer comes from an old machine.

@quote text="Radix sort is the algorithm used by the card-sorting machines you now find only in computer museums." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 8.3"
Radix sort is the algorithm used by the card sorting machines you now find only in computer museums.

@art card-machine
Those machines dropped each punched card into one of several bins, by the hole in one column. The natural way to sort many columns is most significant digit first, then sort each bin separately. But that leaves the operator with lots of piles to track.

@chapter Least significant first
@art lsd-passes
Radix sort does the opposite. Sort the whole deck on the last digit. Gather it up in order. Then sort the whole deck again on the next digit, and so on. d digits, d passes, and no piles set aside.

@math heading="512, 381, 145, 902, 267, 734, 158, 620" items="after pass 1: 620, 381, 512, 902, 734, 145, 267, 158@after the first pass;;3 passes × (8 + 10) = 54 work@three passes"
Take five twelve, three eighty one, one forty five, nine oh two, two sixty seven, seven thirty four, one fifty eight and six twenty. After the first pass, they're in order of last digit, with five twelve still ahead of nine oh two, as they arrived. Three passes of eight plus ten is fifty four units of work, and the result is sorted.

@chapter Why each pass must be stable
@art stable-pass
The one condition is that every pass is stable. After a pass, keys that agree on that digit stay in the order earlier passes gave them, and that order is already right on the less significant digits. That's the induction behind lemma eight point three.

@math heading="Lemma 8.3" items="d digits, k values each@d digits;;Θ(d·(n + k))@d times n plus k"
With n keys of d digits, each digit taking up to k values, and a stable counting sort for each digit, radix sort takes theta of d times n plus k.

@words text="Unstable: 158 lands ahead of 145" sub="most significant first: sorted only on the last digit"
Break it, and it fails. Make each pass unstable, and the last pass puts one fifty eight ahead of one forty five. Go most significant first without recursing, and the first pass actually sorts everything, but the next two scramble it.

@chapter Choosing the digit
@art digit-tradeoff
The digit size is a choice. Read b bit keys r bits at a time. Small r means many cheap passes. Large r means few passes, each paying for a counter array of two to the r.

@math heading="n = 1024, b = 30" items="r = 1: 30 passes, 30,780@r equals one;;r = 8: 4 passes, 5,120@r equals eight;;r = 10: 3 passes, 6,144@r equals ten;;r = 15: 2 passes, 67,584@r equals fifteen"
For a thousand and twenty four keys of thirty bits, r equals one costs thirty thousand seven hundred and eighty. r equals eight costs five thousand one hundred and twenty, the best in the table. r equals ten, the log of n, costs six thousand one hundred and forty four. And r equals fifteen costs sixty seven thousand five hundred and eighty four.

@words text="Fewer passes ≠ always faster" sub="caches, and not in place"
The authors add a caution. Fewer passes needn't mean a faster sort. Quicksort often uses hardware caches better, and radix sort built on counting sort doesn't sort in place.

@chapter Bucket sort
@art buckets
Bucket sort assumes keys are uniform on zero to one. Divide that interval into n equal buckets, drop each key into its bucket, sort each bucket by insertion sort, and join them up. If keys spread evenly, the buckets stay tiny.

@math heading="Eight keys, eight buckets" items="0.42, 0.07, 0.91, 0.33, 0.58, 0.12, 0.47, 0.76@point four two;;buckets ⌊8x⌋: 3, 0, 7, 2, 4, 0, 3, 6@the floor of eight x;;Σ sizes² = 12   vs   expected 15@the squared sizes"
Take point four two, point oh seven, point nine one, point three three, point five eight, point one two, point four seven, point seven six. Their buckets, the floor of eight x, are three, zero, seven, two, four, zero, three and six. The squared sizes sum to twelve, against fifteen expected for uniform keys.

@art bunched
The expected time is theta of n, since each bucket's expected squared size is two minus one over n. But that rests on the input. Bunch the keys into one bucket, and one insertion sort does all the work, in theta of n squared.

@chapter Common slips
@list heading="Common slips" items="Most significant digit first@The first|Any sort for the digit passes@The second|Bucket sort linear on any input@the third"
The first slip is sorting on the most significant digit first, with whole array passes. The second is using any sort for the digit passes, when each must be stable. And the third is expecting bucket sort to be linear on any input.

@chapter Try it
@words text="503, 087, 340, 512, 098, 305" sub="three passes, base 10"
Your turn. Radix sort five oh three, eighty seven, three forty, five twelve, ninety eight and three oh five in base ten, writing eighty seven as oh eight seven. Write the array after each pass.

@end text="Break radix sort twice"
You can run radix sort, and break it twice, on Learn. That's learn dot get er done dot I O.
