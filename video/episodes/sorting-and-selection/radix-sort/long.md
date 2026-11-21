---
format: long
lesson: sorting-and-selection/radix-sort
title: Radix sort: why you start with the least significant digit
thumb: Last digit first
---

@chapter The question
@title text="Radix Sort" sub="Sorting and Selection" art=thumb
Counting sort is great when the range is small. But what about three digit keys, or wider? Split the key into digits and sort one digit at a time. The surprise is which digit goes first, and the reason has nothing to do with arithmetic.

@chapter The algorithm
@art digit-passes
L S D radix sort takes n keys, each d digits in base b, and makes d passes. Each pass is a stable counting sort of the whole array on one digit, starting from the least significant. After the last pass, the array is sorted.

@math heading="Cost" items="one pass:  n + b@Each pass;;d passes:  d(n + b)@The whole sort costs"
Each pass is counting sort with k equal to b, so it costs n plus b. The whole sort costs d times n plus b. Nothing is compared, so the comparison lower bound has nothing to say. On seven keys it says thirteen comparisons, and this makes none.

@art bucket-row
In base ten, one pass is just ten buckets. Drop each key into the bucket for its current digit, in the order you meet them, and read the buckets back out.

@chapter Seven keys
@math heading="329 457 657 839 436 720 355" items="units, then tens, then hundreds@units;;3 passes × 17 = 51@fifty one"
Take three twenty nine, four fifty seven, six fifty seven, eight thirty nine, four thirty six, seven twenty, three fifty five. Three passes: units, then tens, then hundreds. Each costs seventeen, fifty one in all.

@art suffix-sorted
After the first pass, the keys are in order of their last digit. After the second, in order of their last two digits. Only after the third pass is the whole thing sorted. At each step, it's sorted on a suffix of the key.

@chapter Why it works
@words text="After pass i: sorted on digits 0 … i"
That's the invariant, proved by induction. Before any pass, it's about no digits at all, so it holds. Now suppose it holds for the digits below i, and run a stable pass on digit i.

@list heading="Two keys, x before y" items="Digit i differs: the pass put them in order@digit i differs|Digit i agrees: stable, so the old order stays@digit i agrees"
Take two keys, x before y in the output. If their digit i differs, the pass ordered them by it, and digit i outranks everything below. If their digit i agrees, the pass left them as it found them, which was in order on the lower digits. Either way, they're in order on digits zero to i.

@art stable-ties
Look at the second case again. The only fact used about the pass was stability, in exactly the case where the current digit decides nothing. So an unstable pass doesn't just weaken the result. It removes the argument.

@chapter Breaking it twice
@math heading="Two broken variants" items="unstable passes:  355 329 457 436 657 720 839@unstable passes;;most significant first:  720 355 436 457 657 329 839@most significant digit first"
The lab breaks it two ways. With unstable passes, the result is three fifty five, three twenty nine, and so on. Not sorted. With the most significant digit first, and no recursion, you get seven twenty, three fifty five, four thirty six, and so on. Also not sorted.

@art msd-overwrite
And look at that second one. Its units digits read zero, five, six, seven, seven, nine, nine. It's sorted on the units digit alone, because the pass that ran last read the units. The last pass decides the order, so the most important digit must go last.

@words text="MSD radix sort recurses into each bucket"
Most significant digit radix sort is a real algorithm. It just recurses into each bucket, which is exactly the step this variant leaves out.

@chapter Choosing the base
@math heading="Same seven keys" items="base 10:  3 × (7 + 10) = 51@base ten;;base 2:  10 × (7 + 2) = 90@base two;;base 16:  3 × (7 + 16) = 69@base sixteen"
The base is yours to pick, and it moves both terms. A bigger base means fewer digits, but more buckets per pass. In base ten, fifty one. In base two, ten passes, ninety. In base sixteen, sixty nine. There's no base that always wins. There's a product to evaluate.

@art base-tradeoff
So radix sort isn't linear in any useful sense. For keys from zero to n to the c, with base n, it's Theta of c n, and that statement carries its assumptions with it.

@chapter Where people slip
@list heading="Common slips" items="Starting from the most significant digit@The first|Treating the per-digit sort as interchangeable@The second|Calling radix sort linear@And the third"
The first slip is starting from the most significant digit. The second is treating the per digit sort as interchangeable. Any sort orders one digit, but only a stable one composes. And the third is calling radix sort linear without naming the passes and the base.

@chapter Try it
@words text="Radix sort 329 457 657 839 436 720 355" sub="write the array after each pass"
Your turn. Run the three passes by hand and write the array after each one. Check it's sorted on one digit, then two, then three.

@end text="Break radix sort"
You can make the passes unstable or flip the digit order, and watch it fail, on Learn. That's learn dot get er done dot I O.
