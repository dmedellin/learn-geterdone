"""Sorting and Order Statistics, lessons 6-7 -- Chapters 8.3-8.4 and 9.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed.
(MIT Press, 2009): Chapter 8, Sorting in Linear Time, sections 8.3-8.4
(pp. 197-212), and Chapter 9, Medians and Order Statistics (pp. 213-227).
Every quotation is copied from the operator's copy with its printed page in
the comment beside the lesson. The keys and arrays are written for these
lessons; the book's figures, examples and exercises are named, not
reproduced.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    # CLRS sections 8.3-8.4, pp. 197-212.
    # Quote: p. 197, 17 words, quotes.py OK. Lesson total: 17 words.
    # Card sorters and least significant digit first (pp. 197-198); RADIX-
    # SORT, Lemma 8.3, Lemma 8.4 and the choice r = floor(lg n) (pp. 198-199);
    # radix sort against quicksort, not in place (p. 199); BUCKET-SORT,
    # E[n_i^2] = 2 - 1/n, linear if the squares of the bucket sizes sum to
    # O(n) (pp. 200-204).
    {
        "slug": "radix-sort-and-bucket-sort",
        "title": "Radix Sort and Bucket Sort",
        "module": "Chapter 8 · Sorting in Linear Time",
        "one_line": "Radix sort sorts multi-digit keys one digit at a time, least significant first, with a stable sort for each digit; bucket sort spreads keys from [0, 1) over n buckets and is linear on average when they are uniform.",
        "summary": (
            "Section 8.3 sorts d-digit keys by d passes of a stable sort, least significant "
            "digit first, in Θ(d(n + k)), and shows how to choose the digit size for b-bit keys. "
            "Section 8.4's bucket sort divides [0, 1) into n equal buckets, sorts each by "
            "insertion sort and concatenates, in expected linear time if the keys are uniformly "
            "distributed. Run radix sort on eight keys in the lab, then break it twice: with an "
            "unstable pass, and with the passes in the wrong order."
        ),
        "key": [
            "sort on the least significant digit first",
            "each digit pass must be stable",
            "d passes of n + k: Θ(d·(n + k))",
            "b-bit keys, r-bit digits: ⌈b/r⌉ passes",
            "bucket sort: n buckets over [0, 1)",
            "uniform keys: expected Θ(n)",
        ],
        "key_label": "Sections 8.3 and 8.4 in six lines",
        "concepts_intro": (
            "Three ideas: what a digit is for radix sort, the order of its passes, and the "
            "assumption bucket sort trades for its speed."
        ),
        "concepts": [
            ("Digit",
             "One position of a key written in some base. A three-digit decimal key has three "
             "digits, each with 10 possible values; a 30-bit key read 10 bits at a time has "
             "three digits with 1 024 possible values each. The base is a choice, and it sets "
             "both the number of passes and the cost of each."),
            ("Least significant digit first",
             "Radix sort's counterintuitive order. It sorts the whole array on the last digit, "
             "then on the next to last, and so on to the first. After the pass on digit t, the "
             "keys are sorted on their last t digits, provided each pass is stable."),
            ("Uniform distribution",
             "Bucket sort's assumption: the keys are drawn independently and uniformly from "
             "[0, 1). It is an assumption about the input, unlike the randomized quicksort's "
             "random pivots, and the expected time holds only when the input obeys it."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 8.3 and 8.4 in your own copy first. The lesson sets out both sorts "
            "and their analyses in its own words, runs radix sort in the lab, and carries "
            "bucket sort through one small example by hand."
        ),
        "body": [
            ("p", "&ldquo;Radix sort is the algorithm used by the card-sorting machines you now "
                  "find only in computer museums.&rdquo; Section 8.3 starts from those machines, "
                  "which dropped each punched card into one of several bins by the hole in one "
                  "column, and asks how to sort a deck on many columns with them. This lesson "
                  "reads sections 8.3 and 8.4: radix sort, which is counting sort applied digit "
                  "by digit, and bucket sort, which is linear on average under an assumption about "
                  "the input."),
            ("p", "The intuitive method sorts on the most significant digit first and then sorts "
                  "each bin separately, which leaves an operator with many piles to track. Radix "
                  "sort does the opposite. It sorts the whole deck on the least significant "
                  "digit, gathers it in order, then sorts the whole deck again on the next digit, "
                  "and so on: d passes for d-digit keys, with no piles set aside. The authors "
                  "insist on one condition, that each pass be stable. After the pass on a digit, "
                  "keys that agree on it stay in the order the earlier passes gave them, and that "
                  "order is correct on the less significant digits."),
            ("thm", ("Lemma 8.3, in short",
                     "Given n d-digit keys in which each digit takes up to k values, radix sort "
                     "with a stable `Θ(n + k)` sort for each digit, counting sort for instance, "
                     "sorts them in `Θ(d·(n + k))` time.")),
            ("p", "Correctness is an induction on the digits sorted so far, and the authors "
                  "leave its details to Exercise 8.3-3: two keys that differ in the current digit "
                  "are put in order by this pass, and two keys that agree on it are left in the "
                  "order the previous passes produced, which is right by the induction "
                  "hypothesis, only because the pass is stable."),
            ("p", "The digit is a choice, and Lemma 8.4 makes it. Take n keys of b bits and read "
                  "them r bits at a time: `⌈b/r⌉` digits, each with `2ʳ` values, so "
                  "`Θ((b/r)·(n + 2ʳ))` time. Small r means many cheap passes; large r means few "
                  "passes, each paying for a counter array of `2ʳ`. When b is at least `⌊lg n⌋`, "
                  "choosing `r = ⌊lg n⌋` gives `Θ(bn/lg n)`, which is best to within a constant "
                  "factor; when b is smaller, one pass with `r = b` is linear. The authors add a "
                  "caution: fewer passes need not mean a faster sort, since quicksort often uses "
                  "hardware caches better, and radix sort built on counting sort does not sort "
                  "in place."),
            ("math", [
                "the trade-off of Lemma 8.4, n = 1024 keys of b = 30 bits",
                "",
                "r      passes ⌈30/r⌉    n + 2ʳ        work",
                "1          30             1026         30780",
                "5           6             1056          6336",
                "8           4             1280          5120",
                "10          3             2048          6144",
                "15          2            33792         67584",
            ]),
            ("p", "At `r = ⌊lg 1024⌋ = 10` the work is 6 144, close to the best in the table, 5 120 "
                  "at r = 8, and far from either end. A comparison sort needs at least "
                  "`⌈lg(1024!)⌉ = 8770` comparisons on its worst input of this size; the units "
                  "differ, so the comparison is only suggestive, which is the authors' own "
                  "caution about constant factors."),
            ("p", "Section 8.4's bucket sort assumes the keys are uniform on [0, 1). It divides "
                  "that interval into n equal buckets, puts each key in the bucket "
                  "`⌊n·A[i]⌋`, sorts each bucket by insertion sort and concatenates them. "
                  "Everything but the insertion sorts is linear, and an insertion sort of a "
                  "bucket holding `nᵢ` keys costs `O(nᵢ²)`. With an indicator for each key "
                  "falling in bucket i, the authors show `E[nᵢ²] = 2 − 1/n`, so the expected "
                  "total is `Θ(n) + n·O(2 − 1/n) = Θ(n)`. They add that uniformity is more than "
                  "the proof needs: the sort is linear whenever the squares of the bucket sizes "
                  "add up to something linear in n."),
            ("example", ("Eight keys in eight buckets",
                         "Take `0.42, 0.07, 0.91, 0.33, 0.58, 0.12, 0.47, 0.76`. The bucket of "
                         "each key is `⌊8x⌋`: 3, 0, 7, 2, 4, 0, 3, 6. Buckets 0 and 3 hold two "
                         "keys each, buckets 2, 4, 6 and 7 one each, and 1 and 5 none. The sum of "
                         "the squared sizes is `4 + 4 + 1 + 1 + 1 + 1 = 12`, against an "
                         "expectation of `n·(2 − 1/n) = 15` for uniform keys.")),
            ("p", "Now the lab, the one the Algorithms Subject's lesson Radix Sort uses, where "
                  "more practice waits. It runs radix sort on the keys you type in the base you "
                  "choose, shows the array after each pass and checks the result against the "
                  "sorted array. Its tiles are the number of digit passes, the work per pass "
                  "`n + b` for base b, the elements moved and whether the result is sorted. The "
                  "lesson's keys are `512, 381, 145, 902, 267, 734, 158, 620` in base 10: 3 "
                  "passes of `8 + 10 = 18`, 54 units of work, 24 moves, sorted. After the first "
                  "pass the order is `620, 381, 512, 902, 734, 145, 267, 158`, by last digit with "
                  "512 still ahead of 902 as it arrived."),
            ("p", "Now break it. Choose passes that are least significant first but unstable, "
                  "reversing each bucket: the result is not sorted, and the last pass leaves 158 "
                  "ahead of 145, two keys that agree on the digit being read and were put in "
                  "the wrong order. Choose most significant first with no recursion: the first "
                  "pass sorts the array completely, and the next two scramble it, ending sorted "
                  "on the last digit only. Back on the stable variant, base 2 needs 10 passes of "
                  "`8 + 2`, since 902 needs ten bits; base 16 needs 3 passes of `8 + 16`."),
            ("h3", "Exercise"),
            ("p", "Radix sort `503, 87, 340, 512, 98, 305` by hand in base 10, writing 87 as 087 "
                  "and 98 as 098. Write the array after each of the three passes, then type the "
                  "keys into the lab and check each pass against its table."),
            ("p", "Sorting is one way to find the median: sort, then index. The next lesson, "
                  "Medians and Order Statistics, finds it in linear time without sorting, first "
                  "in expectation and then in the worst case."),
        ],
        "lab": ("sortkit", {
            "mode": "radix",
            "keys": "512, 381, 145, 902, 267, 734, 158, 620",
            "base": 10,
            "variant": "lsd",
            "pass": 1,
            "panel_title": "Sort eight keys digit by digit",
            "panel_intro": (
                "Each pass is run and its buckets drawn; the table gives the array after every "
                "pass and compares it with the sorted array, so a broken variant is seen failing. "
                "Change the base to change the number of digits."
            ),
        }),
        "steps_title": "Radix sort by hand",
        "steps_intro": "Pad every key to the same number of digits first.",
        "steps": [
            ("Pad the keys",
             "Write every key with d digits in the chosen base, adding leading zeros."),
            ("Sort on the last digit, stably",
             "Distribute the keys into bins by their last digit, keeping arrival order within "
             "each bin, and gather the bins in order."),
            ("Repeat toward the first digit",
             "Do the same on each digit from right to left, always starting from the order the "
             "previous pass left."),
            ("Count the work",
             "Each pass touches every key once and every bin once: n + k, d times over."),
            ("Do it on keys of your own",
             "Type eight four-digit keys of your own into the lab, predict the order after the "
             "second pass, then check; switch to the unstable variant and find the pair it puts "
             "in the wrong order."),
        ],
        "worked": {
            "title": "Eight keys, three passes",
            "intro": [
                "Sort the lab's keys `512, 381, 145, 902, 267, 734, 158, 620` by hand in base 10.",
            ],
            "lines": [
                "last digit:   620, 381, 512, 902, 734, 145, 267, 158",
                "middle digit: 902, 512, 620, 734, 145, 158, 267, 381",
                "first digit:  145, 158, 267, 381, 512, 620, 734, 902",
                "work: 3 passes of 8 + 10 = 54",
            ],
            "after": [
                "In the second pass 145 and 158 have middle digits 4 and 5, so this pass puts "
                "them in order. In the third pass they share the "
                "first digit 1, and the stable pass keeps 145 ahead of 158 because the second "
                "pass put it there. That is the induction of Lemma 8.3 on one pair.",
            ],
        },
        "quiz_title": "Digits, passes and buckets",
        "quiz": [
            {"q": "Radix sort `503, 087, 340, 512, 098, 305` in base 10, least significant digit "
                  "first. What is the order after the second pass?",
             "a": ["`503, 305, 512, 340, 087, 098`",
                   "`305, 503, 512, 340, 087, 098`",
                   "`340, 512, 503, 305, 087, 098`",
                   "`087, 098, 305, 340, 503, 512`"],
             "c": 0,
             "why": "The first pass, on the last digit, gives `340, 512, 503, 305, 087, 098`, the "
                    "third option. The second pass, on the middle digit, puts the two keys with "
                    "middle digit 0 first, and stability keeps them in their current order, 503 "
                    "then 305; then 512, 340, 087 and 098. Putting 305 first is what an unstable "
                    "pass might do. The sorted order appears only after the third pass."},
            {"q": "By Lemma 8.4, radix sort on n = 1024 keys of b = 30 bits with r = 10 bits per "
                  "digit makes how many passes, at what cost each?",
             "a": ["3 passes of `1024 + 2¹⁰ = 2048`",
                   "10 passes of `1024 + 3`",
                   "30 passes of `1024 + 2`",
                   "2 passes of `1024 + 2¹⁵`"],
             "c": 0,
             "why": "With r = 10 there are `⌈30/10⌉ = 3` digits, each with `2¹⁰ = 1024` values, so "
                    "three passes of `n + 2ʳ = 2048`. Thirty passes of 1026 is r = 1 and two "
                    "passes of 33 792 is r = 15. Ten passes swaps the roles of r and b/r. The "
                    "choice `r = ⌊lg n⌋` is best only to within a constant factor: r = 8 costs "
                    "5 120 here against 6 144."},
            {"q": "In the lab, base 16 sorts the lesson's eight keys in 3 passes and base 2 in "
                  "10. Why?",
             "a": ["The largest key, 902, has three digits in base 16 and ten in base 2",
                   "Base 16 is a power of 2, so it needs the same number of passes as base 10",
                   "Base 2 sorts one key per pass",
                   "Base 2 needs one pass per key, plus two"],
             "c": 0,
             "why": "902 is below `16³ = 4096` and at least `16² = 256`, so three hex digits; it "
                    "is below `2¹⁰ = 1024` and at least `2⁹ = 512`, so ten bits. The number of "
                    "passes is the number of digits of the largest key, whatever the number of "
                    "keys. Base 10 needs three passes too, but because 902 has three decimal "
                    "digits, not because 16 is a power of 2. That 10 is 8 keys plus 2 is a coincidence: add a "
                    "ninth key below 1024 and base 2 still needs 10 passes."},
            {"q": "Bucket sort, with insertion sort in each bucket, is given n keys that all lie "
                  "in `[0, 1/n)`. What is its running time?",
             "a": ["`Θ(n)`", "`Θ(n lg n)`", "`Θ(n²)` in the worst case", "`Θ(n + k)`"],
             "c": 2,
             "why": "Every key lands in bucket 0, so the whole sort is one insertion sort of n "
                    "keys, which is `Θ(n²)` in the worst case. The expected linear time assumed "
                    "keys spread uniformly over [0, 1), and these are not. Bucket sort has no "
                    "range parameter k, and nothing in it gives `n lg n`."},
        ],
        "mistakes": [
            ("Sorting on the most significant digit first",
             "It is the natural order for a person sorting by hand, and it works if each bin "
             "is then sorted separately. Run as whole-array passes, it fails: the last pass, on "
             "the least significant digit, overrides everything before it. In the lab, the "
             "variant that goes most significant first without recursing sorts the lesson's "
             "keys in its first pass and leaves them sorted only on the last digit after the "
             "third."),
            ("Using any sort for the digit passes",
             "The induction behind Lemma 8.3 needs each pass to keep keys with equal digits in "
             "the order the previous passes left. An unstable pass breaks that: in the lab, the "
             "unstable variant puts 158 ahead of 145 in its last pass, though the previous "
             "pass had ordered them, and the result is not sorted."),
            ("Expecting bucket sort to be linear on any input",
             "The expected `Θ(n)` rests on the keys being uniform on [0, 1), so that buckets "
             "stay small, or at least on the squares of the bucket sizes adding up to "
             "something linear. Keys bunched in one bucket leave one insertion sort to do all "
             "the work, in `Θ(n²)`. The assumption is about the input, and nothing in the "
             "algorithm enforces it."),
        ],
        "standard": (
            "Finish when you can run radix sort by hand and choose its digits.",
            "Sort six keys of three digits by radix sort with the array after each pass, say "
            "why each pass must be stable, compute passes and work for given n, b and r, and "
            "state what bucket sort assumes about its input."
        ),
        "note": (
            "The lab runs radix sort with counting passes in bases 2 to 16; it does not run "
            "bucket sort, which the example above carries out by hand. Its moves and work are "
            "counts on the keys you typed. Lemma 8.3 and Lemma 8.4 hold for every input of the "
            "stated sizes; bucket sort's expected linear time holds only for inputs that meet "
            "its assumption."
        ),
    },
    # ---------------------------------------------------------------- 07
    # CLRS Chapter 9, sections 9.1-9.3, pp. 213-227.
    # Quote: p. 213, 15 words, quotes.py OK. Lesson total: 15 words.
    # Order statistics, lower and upper median, the selection problem
    # (p. 213); minimum in n - 1 comparisons and the tournament argument,
    # simultaneous minimum and maximum in at most 3 floor(n/2) (pp. 214-215);
    # RANDOMIZED-SELECT, its worst case and expected linear time
    # (pp. 215-220); SELECT, groups of five, 3n/10 - 6, the recurrence and
    # the constant 140, no conflict with the sorting bound (pp. 220-222).
    {
        "slug": "medians-and-order-statistics",
        "title": "Medians and Order Statistics",
        "module": "Chapter 9 · Medians and Order Statistics",
        "one_line": "The ith smallest of n keys can be found without sorting: in expected linear time by partitioning around random pivots and keeping one side, and in worst-case linear time with a pivot chosen from medians of groups of five.",
        "summary": (
            "Chapter 9 finds order statistics. Section 9.1 finds the minimum in n − 1 "
            "comparisons, which is optimal, and the minimum and maximum together in at most "
            "3⌊n/2⌋. Section 9.2's RANDOMIZED-SELECT partitions around a random pivot and "
            "recurses into one side, in expected linear time. Section 9.3's SELECT chooses its "
            "pivot as the median of the medians of groups of five and is linear in the worst "
            "case. Find a median of 21 keys in the lab and set its comparisons beside the cost "
            "of sorting first."
        ),
        "key": [
            "minimum: n − 1 comparisons, optimal",
            "min and max together: 3⌊n/2⌋",
            "select: partition, keep one side",
            "random pivot: expected Θ(n)",
            "median of medians of five: worst Θ(n)",
            "1/5 + 7/10 < 1, so the sum is linear",
        ],
        "key_label": "Chapter 9 in six lines",
        "concepts_intro": (
            "Three ideas: the problem, the median that is its hardest case, and the one "
            "change that turns quicksort into a selection algorithm."
        ),
        "concepts": [
            ("Order statistic",
             "The ith order statistic of a set of n keys is its ith smallest: the minimum is "
             "the first, the maximum the nth. The selection problem is to find it, given the "
             "set and i. The chapter assumes the keys are distinct, for convenience."),
            ("Median",
             "The halfway point of the set. For odd n it is unique, at `i = (n + 1)/2`. For even "
             "n there are two, the lower median at `i = n/2` and the upper at `n/2 + 1`; "
             "&ldquo;the median&rdquo; in the book means the lower one, `i = ⌊(n + 1)/2⌋`."),
            ("Selection by partition",
             "Partition around a pivot as quicksort does. The pivot's rank k in the subarray "
             "says where the answer lies: it is the pivot if `i = k`, on the left if `i < k`, "
             "and on the right as the `(i − k)`th smallest there if `i > k`. Only one side is "
             "searched further."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read Chapter 9 in your own copy first. The lesson sets out the three sections in "
            "its own words, works the minimum and maximum and the groups-of-five arithmetic by "
            "hand, and then runs randomized selection in the lab."
        ),
        "body": [
            ("p", "&ldquo;The ith order statistic of a set of n elements is the ith smallest "
                  "element.&rdquo; Chapter 9 opens with that definition and an observation: "
                  "sorting and then indexing answers any such question in `O(n lg n)`, and the "
                  "chapter's business is to do better. This lesson reads the whole chapter, "
                  "sections 9.1 to 9.3: minimum and maximum, selection in expected linear time, "
                  "and selection in worst-case linear time."),
            ("p", "Section 9.1 starts with the minimum. Scanning the keys and keeping the "
                  "smallest so far takes n − 1 comparisons, and no algorithm can do better. "
                  "The authors argue it as a tournament: each key other than the winner has to lose "
                  "at least one comparison to be ruled out, and each comparison has only one "
                  "loser. Finding the minimum and the maximum separately would take `2n − 2`, but "
                  "together they need fewer. Take the keys in pairs, compare the two keys of a "
                  "pair with each other, then test the smaller against the minimum so far and the "
                  "larger against the maximum so far: three comparisons for every two keys, at "
                  "most `3⌊n/2⌋` in all."),
            ("p", "Section 9.2's RANDOMIZED-SELECT is randomized quicksort with one recursive "
                  "call removed. It calls RANDOMIZED-PARTITION on `A[p..r]`, computes the pivot's "
                  "rank k within the subarray, and either returns the pivot or recurses into the "
                  "single side that holds the answer, adjusting i when it goes right. Its worst "
                  "case is `Θ(n²)`, when every pivot happens to be the largest remaining key. "
                  "Its expected time is linear: the authors bound the expected size of the side "
                  "kept, set up a recurrence for the expectation and solve it by substitution, "
                  "assuming distinct keys."),
            ("p", "Why linear, when randomized quicksort is `n lg n`? Quicksort recurses into "
                  "both sides, so every level of its recursion tree costs about n. Selection "
                  "keeps one side, so the levels shrink: a pivot from the middle half of its "
                  "subarray, which happens with probability one half, leaves at most three "
                  "quarters of the keys. The expected costs form a series that falls "
                  "geometrically, and a geometric series is a constant times its first term."),
            ("p", "Section 9.3's SELECT removes the luck. It splits the n keys into groups of "
                  "five, with at most one smaller group; finds each group's median by insertion "
                  "sort; calls itself recursively to find the median x of those `⌈n/5⌉` medians; "
                  "partitions around x; and recurses into the side that holds the answer. The "
                  "pivot x is not the median of the whole set, but it cannot be far from it."),
            ("thm", ("The groups-of-five guarantee",
                     "At least half of the `⌈n/5⌉` group medians are at least x. Each of their "
                     "groups, except x's own and the possibly short last group, contributes "
                     "three keys greater than x, so at least `3·(⌈⌈n/5⌉/2⌉ − 2) ≥ 3n/10 − 6` "
                     "keys are greater than x, and as many are less. The recursion therefore "
                     "keeps at most `7n/10 + 6` keys.")),
            ("math", [
                "T(n) ≤ T(⌈n/5⌉) + T(7n/10 + 6) + O(n)",
                "",
                "the two recursive sizes, ignoring ceiling and + 6:",
                "1/5 + 7/10 = 9/10, which is less than 1",
                "",
                "level 0 of the tree:   cn",
                "level 1:               about (9/10)·cn",
                "level 2:               about (81/100)·cn",
                "total:                 about 10·cn",
            ]),
            ("p", "The two recursive calls together handle about nine tenths of the keys, plus a "
                  "constant, so each level of the recursion tree costs roughly nine tenths of "
                  "the level above and the whole tree is linear. That sketch ignores the ceiling "
                  "and the + 6, which only become negligible for large n, so the book proves the "
                  "bound by substitution instead, assuming inputs of fewer than 140 keys take "
                  "constant time and showing where that constant comes from. It also notes why this does not contradict Chapter 8: SELECT "
                  "and RANDOMIZED-SELECT compare keys but do not sort them, and the lower bound "
                  "is about sorting."),
            ("p", "Now the lab, the one the Algorithms Subject's lesson Quickselect uses; its "
                  "lesson Median of Medians practises Section 9.3. It runs randomized selection "
                  "on an array of n keys under a seeded pivot rule and counts comparisons, then "
                  "sorts the same array by merge sort and counts those. The tiles are the "
                  "comparisons to select, the comparisons to sort first, the value found, and the "
                  "number of partition steps, the last of them a one-key range that needs no "
                  "comparison. The table follows the range still in play."),
            ("p", "The lesson's setting is the median of 21 keys, i = 11, in a seeded shuffle, "
                  "with a random pivot from seed 9. Selection makes 65 comparisons in 8 steps "
                  "and finds 11; merge sort on the same array makes 70. The ranges shrink from "
                  "21 keys to 15, 12, 9, 8, 4, 3 and 1, and each partition of m keys costs "
                  "`m − 1` comparisons: `20 + 14 + 11 + 8 + 7 + 3 + 2 = 65`. Move the seed and "
                  "the count moves, from 33 at seed 8 to 77 at seeds 7 and 10. Set the rule to "
                  "the last element and the order to already sorted: 165 comparisons, the "
                  "quadratic worst case, since every range loses only its largest key."),
            ("h3", "Exercise"),
            ("p", "Use the pairing method on `17, 4, 29, 11, 2, 23, 8, 30, 15` to get its smallest and "
                  "largest keys, counting comparisons, and compare your count with `3⌊n/2⌋` "
                  "and with `2n − 2`. Then compute the groups-of-five guarantee at n = 60: how "
                  "many keys must be greater than the median of medians, and how many keys can "
                  "the recursive call receive?"),
            ("p", "That completes Part II. The next course, Data Structures, reads Part III, "
                  "beginning with the stacks, queues and linked lists of Chapter 10 and going on "
                  "to hash tables and search trees."),
        ],
        "lab": ("sortkit", {
            "mode": "select",
            "n": 21,
            "k": 11,
            "rule": "random",
            "order": "shuffle",
            "seed": 9,
            "panel_title": "Find a median and count the comparisons",
            "panel_intro": (
                "Selection partitions around the chosen pivot and keeps the side that holds the "
                "rank, counting every comparison. Merge sort's count on the same array is the "
                "cost of sorting first. The table shows the range still in play after each "
                "partition."
            ),
        }),
        "steps_title": "Selecting by hand",
        "steps_intro": "Four steps for one selection, and one on a size of your own.",
        "steps": [
            ("Fix the rank",
             "Decide which order statistic you want. For the median of n keys, i is "
             "`⌊(n + 1)/2⌋`."),
            ("Partition around a pivot",
             "Choose the pivot, partition as PARTITION does, and compute its rank k within the "
             "current range. Count `m − 1` comparisons for a range of m keys."),
            ("Keep one side",
             "If `i = k`, stop. If `i < k`, keep the left side with the same i. If `i > k`, keep "
             "the right side and replace i by `i − k`."),
            ("Total the comparisons",
             "Add the partitions' costs and compare with what sorting first would cost."),
            ("Do it at a size of your own",
             "Set the lab to 31 keys and the median, i = 16, and run five seeds. Note the "
             "smallest and largest comparison counts and set them beside merge sort's, which "
             "does not change with the seed."),
        ],
        "worked": {
            "title": "Minimum and maximum of nine keys",
            "intro": [
                "Find both extremes of `14, 6, 25, 9, 31, 3, 18, 12, 20` by pairs. With n odd, "
                "the first key starts as both minimum and maximum.",
            ],
            "lines": [
                "start: min = max = 14",
                "pair 6, 25: 6 < 25; 6 < 14; 25 > 14",
                "pair 9, 31: 9 < 31; 9 < 6? no; 31 > 25",
                "pair 3, 18: 3 < 18; 3 < 6; 18 > 31? no",
                "pair 12, 20: 12 < 20; 12 < 3? no; 20 > 31? no",
                "min 3, max 31, in 12 comparisons",
                "3⌊9/2⌋ = 12;  2n − 2 = 16",
            ],
            "after": [
                "Each pair costs three comparisons instead of four, because only the smaller of "
                "the two can be a new minimum and only the larger a new maximum. With n odd "
                "there is no initial comparison, so the count is exactly `3⌊n/2⌋`; with n even "
                "the first two keys are compared once to start, and the count is `3n/2 − 2`.",
            ],
        },
        "quiz_title": "Order statistics and selection",
        "quiz": [
            {"q": "How many comparisons does the pairing method make to locate the smallest "
                  "and the largest of 10 keys at once?",
             "a": ["13", "15", "18", "9"],
             "c": 0,
             "why": "With n even, the first two keys are compared once to set the minimum and the "
                    "maximum, and each of the remaining four pairs costs three: `1 + 4·3 = 13`, "
                    "which is `3n/2 − 2`. Fifteen is `3⌊n/2⌋`, the book's upper bound covering "
                    "both parities, not the exact count here. Eighteen is `2n − 2`, finding each "
                    "separately. Nine is `n − 1`, the minimum alone."},
            {"q": "In SELECT on n = 60 keys, at least how many keys are guaranteed to be greater "
                  "than the median of medians x?",
             "a": ["18", "12", "30", "6"],
             "c": 1,
             "why": "There are `⌈60/5⌉ = 12` group medians, and at least `⌈12/2⌉ = 6` of them are "
                    "at least x. Leaving out x's own group and the possibly short last group "
                    "leaves 4 groups, each with 3 keys greater than x: 12, which is "
                    "`3n/10 − 6 = 18 − 6`. Eighteen is `3n/10` without the correction; 30 would "
                    "make x the true median; 6 counts the groups, not the keys."},
            {"q": "In the lab, randomized selection of the median of 21 keys costs 65 "
                  "comparisons at seed 9 but 77 at seed 7, against merge sort's 70. What does "
                  "Section 9.2's theorem say about this?",
             "a": ["It is wrong at n = 21, since a linear-time algorithm should never cost more "
                   "than sorting",
                   "Its expectation is over the pivot choices: the average run is linear on every "
                   "input, and a particular run can cost more than sorting",
                   "Seed 7 must be a worst case, which costs `Θ(n²)`",
                   "The expected linear time holds only for shuffled input"],
             "c": 1,
             "why": "The theorem bounds the expected time, averaged over the random pivots, on "
                    "every input; it says nothing about every run being cheap, and a "
                    "comparison with sorting at one small n is not what it claims. The quadratic "
                    "worst case is 165 here, far above 77. The expectation is over the pivots, "
                    "so the input order does not matter."},
            {"q": "RANDOMIZED-SELECT is looking for the 9th smallest key of a range. After "
                  "partitioning, the pivot has rank 6 within the range. What happens next?",
             "a": ["It recurses into the right side looking for its 3rd smallest key",
                   "It recurses into the right side looking for its 9th smallest key",
                   "It recurses into the left side looking for its 9th smallest key",
                   "It recurses into both sides, as quicksort does"],
             "c": 0,
             "why": "Rank 6 means five keys are below the pivot and the pivot is the 6th, so the "
                    "9th smallest is on the right, and it is the `9 − 6 = 3`rd smallest there. "
                    "Keeping i = 9 forgets the six keys left behind. The left side holds only "
                    "five keys. Recursing into one side only is the whole difference from "
                    "quicksort."},
        ],
        "mistakes": [
            ("Believing a median needs a sort, and so Ω(n lg n)",
             "Sorting and indexing finds any order statistic, so it is natural to think the "
             "sorting lower bound applies. It does not: Chapter 8's bound is about producing the "
             "whole order, and selection needs only one rank. RANDOMIZED-SELECT is linear in "
             "expectation and SELECT in the worst case. In the lab, the median of 21 keys took "
             "65 comparisons at seed 9, and the count at any seed is about one input."),
            ("Assuming minimum and maximum together cost 2n − 2",
             "That is the price of two separate scans. Processing the keys in pairs, so that "
             "only the smaller of each pair is tried against the minimum and only the larger "
             "against the maximum, costs at most `3⌊n/2⌋`: 12 instead of 16 for the worked "
             "example's nine keys."),
            ("Expecting every run of an expected-linear algorithm to beat sorting",
             "The expectation is an average over the random pivots. Individual runs scatter "
             "around it: in the lab, seeds 7 and 10 cost 77 comparisons, above merge sort's 70, "
             "and seed 8 costs 33. The theorem promises the average's growth rate on every "
             "input, not a ceiling on every run."),
        ],
        "standard": (
            "Finish when you can select by hand and check the guarantee.",
            "Find the minimum and maximum of nine to twelve keys in `3⌊n/2⌋` comparisons or "
            "fewer, trace RANDOMIZED-SELECT through a given sequence of pivots, and compute "
            "the groups-of-five guarantee and recursive size for a given n."
        ),
        "note": (
            "The lab runs selection with a seeded pivot rule and counts one run at a time; the "
            "expected linear time is an average over pivot choices that one run only samples. "
            "SELECT's worst-case bound rests on the groups-of-five arithmetic, which the lesson "
            "works by hand and the Algorithms lesson Median of Medians runs."
        ),
    },
]
