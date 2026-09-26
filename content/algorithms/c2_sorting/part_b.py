"""Sorting and Selection, lessons 07-12 - radix, bucket, selection, lower bounds, scale."""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "radix-sort",
        "title": "Radix Sort",
        "module": "Not comparing at all",
        "one_line": "Run LSD radix sort on three-digit keys, and break it two ways to see what its correctness rests on.",
        "summary": (
            "A key too wide for one counting sort can be split into `d` digits in base `b` "
            "and sorted one digit at a time, least significant first, each pass a stable "
            "counting sort over `b` buckets. The cost is `Θ(d(n + b))`, and the reason the "
            "passes compose into a sorted array is not arithmetic: it is that every pass "
            "leaves its own ties in the order the pass before it produced."
        ),
        "key": [
            "for digit position 0, 1, …, d−1:   stable counting sort on that digit",
            "least significant digit FIRST, and every pass stable",
            "work = d(n + b)     7 keys, base 10, 3 digits:  3 × 17 = 51",
            "                    the same keys in base 2:   10 × 9 = 90",
            "one unstable pass undoes every pass before it",
        ],
        "key_label": "The loop, the cost, and the property the whole thing rests on",
        "concepts_intro": (
            "The hard idea is the invariant across passes, and it is where a reader's "
            "intuition about significance runs exactly backwards."
        ),
        "concepts": [
            ("After the pass on digit d, the array is sorted on digits 0 through d",
             "That is the invariant, and it is what has to be preserved. Pass `d` puts the "
             "keys in order of digit `d`. Two keys that agree in digit `d` are left in the "
             "order the previous pass gave them, which by the invariant was order on digits "
             "`0 … d−1`. So they come out ordered on digits `0 … d`, which is the invariant "
             "again one digit wider. After the last pass the array is sorted on the whole key."),
            ("Stability is the composition, not a nicety",
             "The step above used exactly one property of the pass: that it leaves its ties "
             "alone. Take it away and the argument has nothing. The lab supplies a variant "
             "whose passes reverse their buckets, and on the standard seven keys the result "
             "is `355 329 457 436 657 720 839` &mdash; not sorted, and the pass that broke "
             "it is any of them."),
            ("Most significant first, with no recursion, sorts by the last pass alone",
             "Running the digits from the most significant down feels right and is wrong "
             "unless each bucket is then sorted recursively. Without that, the final pass is "
             "the one on the units digit and it rearranges the whole array, so everything the "
             "earlier passes arranged is overwritten. The lab's output is "
             "`720 355 436 457 657 329 839`, whose units digits read `0 5 6 7 7 9 9`: sorted "
             "on the least significant digit and on nothing else."),
        ],
        "read_title": "One counting sort per digit, and the two ways to break the composition",
        "read_intro": "The passes, the invariant that makes them compose, and the two variants the lab lets you watch fail.",
        "body": [
            ("def", ("LSD radix sort",
                     "<strong>Least-significant-digit radix sort</strong> sorts `n` keys, each "
                     "of `d` digits in base `b`, by performing `d` passes. Pass `i` is a "
                     "<strong>stable</strong> counting sort of the whole array on digit `i`, "
                     "counting digits from the least significant, which is digit zero. After "
                     "the last pass the array is sorted.")),
            ("p", "Each pass is counting sort with `k = b`, so a pass "
                  "costs `n + b` and the whole sort costs `d(n + b)`. Nothing is compared, so "
                  "the comparison lower bound is as silent here as it was there: on seven keys "
                  "it says 13 comparisons are necessary for any comparison sort, and this "
                  "algorithm makes none."),
            ("example", ("Seven three-digit keys, base ten",
                         "The keys are `329 457 657 839 436 720 355`. Three passes, 17 units "
                         "of work each, 51 in all. Pass one reads the units digit, pass two "
                         "the tens, pass three the hundreds, and the array after each pass is "
                         "in the worked example below. Only after the third pass is it "
                         "sorted, and after the first two it is sorted on a suffix of the "
                         "key.")),
            ("thm", ("The passes compose",
                     "If every pass is a stable sort on its digit, then after the pass on "
                     "digit `i` the array is in increasing order of the number formed by "
                     "digits `0` through `i` of each key.")),
            ("proof", ("By induction on `i`. Before any pass, the claim is about no digits at "
                       "all and holds vacuously.",
                       "Suppose it holds after the pass on digit `i−1`, and run a stable pass "
                       "on digit `i`. Take two keys `x` and `y` with `x` before `y` in the "
                       "output. If their digits `i` differ, the pass placed them in increasing "
                       "order of that digit, and digit `i` outranks all the digits below it, "
                       "so the numbers formed by digits `0 … i` are in increasing order.",
                       "If their digits `i` agree, the pass left them in the order it found "
                       "them, which by the inductive hypothesis was increasing order of digits "
                       "`0 … i−1`. Since their digits `i` are equal, that is increasing order "
                       "of digits `0 … i` as well. The claim holds after pass `i`, and after "
                       "pass `d−1` it is the whole key.")),
            ("p", "Read the second paragraph of that proof again: the only fact used about the "
                  "pass was stability, and it was used in the case where the current digit "
                  "decides nothing. That is why an unstable pass does not merely degrade the "
                  "result &mdash; it removes the argument entirely, and the lab shows the "
                  "array that comes out."),
            ("h3", "Choosing the base"),
            ("p", "The base is free and it moves both terms. Larger `b` means fewer digits "
                  "`d = ⌈log_b U⌉` for keys below `U`, and a bigger bucket array per pass. The "
                  "same seven keys cost `3 × (7 + 10) = 51` in base ten, `10 × (7 + 2) = 90` "
                  "in base two, and `3 × (7 + 16) = 69` in base sixteen. There is no rule that "
                  "one base always wins; there is a product to evaluate, and the lab "
                  "evaluates it as you move the control."),
            ("p", "The honest form of the cost is therefore `Θ(d(n + b))` with `d` depending "
                  "on the key width and the base, which is why radix sort is not `Θ(n)` in any "
                  "useful sense. For `n` keys drawn from `0 … n^c − 1` and base `b = n`, it is "
                  "`Θ(cn)`, and that statement carries its hypotheses in it."),
            ("example", ("The two broken variants, side by side",
                         "Unstable passes, least significant first: "
                         "`355 329 457 436 657 720 839` &mdash; not sorted. Most significant "
                         "first with no recursion: `720 355 436 457 657 329 839` &mdash; not "
                         "sorted, and sorted on the units digit alone, because the pass that "
                         "ran last read the units. The lab checks both against the sorted "
                         "array rather than asserting failure.")),
            ("p", "Neither variant is a strawman. The first is what happens when the per-digit "
                  "sort is replaced by something convenient that happens not to be stable. The "
                  "second is what happens when a reader reasons from significance: the most "
                  "important digit should be settled first. Most-significant-digit radix sort "
                  "is a real and useful algorithm &mdash; it recurses into each bucket, which "
                  "is precisely the step whose absence the lab is demonstrating."),
        ],
        "lab": ("sortkit", {
            "mode": "radix",
            "keys": "329, 457, 657, 839, 436, 720, 355",
            "base": 10,
            "variant": "lsd",
            "pass": 1,
            "panel_title": "Choose the keys, the base and the pass order",
            "panel_intro": "Each pass is run and its buckets are shown. The verdict under the "
                           "array compares what came out against the sorted array, so a broken "
                           "variant is seen failing rather than described as failing.",
        }),
        "steps_title": "Running the passes, and checking the invariant between them",
        "steps_intro": "The check between passes is the whole discipline: after pass `i` the array is sorted on a suffix of the key, and you can verify that.",
        "steps": [
            ("Fix the base, then count the digits",
             "`d = ⌈log_b U⌉` where `U` bounds the keys. Write down `d(n + b)` before running "
             "anything, and compare it with the same product at another base. This is the "
             "sizing step, and it is the one that decides whether radix sort is worth the "
             "bucket array."),
            ("Sort on digit zero, stably",
             "Bucket by the least significant digit, and inside each bucket keep the input "
             "order. Concatenating the buckets in order gives the array after pass one."),
            ("After each pass, check the suffix claim",
             "After pass `i`, the array must be in order of the last `i + 1` digits of each "
             "key. This is checkable by eye on seven keys and it is how you find the pass that "
             "went wrong, rather than discovering at the end that the output is not sorted."),
            ("Watch what a pass does inside its own ties",
             "In the base-ten example, the third pass leaves `329` before `355` because both "
             "have hundreds digit `3` and the second pass had already put them in that order. "
             "That single observation is the correctness proof in miniature; if you can see it "
             "once you will not run the passes in the other order."),
            ("Break it deliberately, once",
             "Switch the variant to unstable passes and then to most-significant-first, and "
             "read the outputs. The second one is the more instructive: the array comes out "
             "ordered by its units digit, which is the signature of the last pass having "
             "overwritten everything."),
        ],
        "worked": {
            "title": "Three passes on seven keys, base ten",
            "intro": [
                "The keys are the lab's defaults. Each pass buckets the whole array by one "
                "digit, keeping the order inside each bucket, and concatenates the buckets "
                "from digit zero upwards.",
            ],
            "lines": [
                "input           329  457  657  839  436  720  355",
                "",
                "PASS 1, units digit",
                "  bucket 0  720          bucket 5  355         bucket 6  436",
                "  bucket 7  457, 657     bucket 9  329, 839",
                "  after     720  355  436  457  657  329  839",
                "",
                "PASS 2, tens digit",
                "  bucket 2  720, 329     bucket 3  436, 839    bucket 5  355, 457, 657",
                "  after     720  329  436  839  355  457  657",
                "",
                "PASS 3, hundreds digit",
                "  bucket 3  329, 355     bucket 4  436, 457    bucket 6  657",
                "  bucket 7  720          bucket 8  839",
                "  after     329  355  436  457  657  720  839      sorted",
                "",
                "work            3 passes × (n + b) = 3 × (7 + 10) = 51 units",
                "comparisons     0",
                "⌈log₂ 7!⌉       13, which every comparison sort needs and this one is outside",
            ],
            "after": [
                "The load-bearing line is bucket `3` of pass three. It holds `329` and `355`, "
                "which agree in the hundreds digit, and it holds them in that order because "
                "pass two put `329` before `355` and pass three did not disturb its own ties. "
                "Every correctly ordered pair of keys that agree in the hundreds digit is "
                "there for the same reason.",
                "Notice also what pass one and pass two produced: arrays that are not sorted "
                "and are not meant to be. After pass one the array is in order of units "
                "digits; after pass two, in order of the two-digit number formed by tens and "
                "units, which you can read off as `20 29 36 39 55 57 57`. The invariant is "
                "checkable at every stage.",
                "For a faded rehearsal, set the base to 2 and predict two things before "
                "looking: the number of passes, and the total work. The supplied first move is "
                "that `839` needs ten binary digits, so `d = 10`; work out `d(n + b)` and then "
                "check it, and say which of base 2, 10 and 16 you would choose for these seven "
                "keys and why the answer would change for seven million of them.",
            ],
        },
        "quiz_title": "Passes, and what composes them",
        "quiz": [
            {"q": "Radix sort is run most-significant-digit first, with no recursion into the buckets. What comes out?",
             "a": ["The sorted array, more slowly",
                   "An array sorted on the least significant digit alone, because the last pass rearranges everything",
                   "An array sorted on the most significant digit alone",
                   "The input, unchanged"],
             "c": 1,
             "why": "Each pass rearranges the entire array, so the last one to run is the last "
                    "word, and running the digits downwards makes the units pass last. The "
                    "lab's output is `720 355 436 457 657 329 839`, whose units digits read "
                    "`0 5 6 7 7 9 9`."},
            {"q": "One of the `d` passes is replaced by an unstable sort on the same digit. What is the consequence?",
             "a": ["The output is off by one position",
                   "The correctness argument is gone, because the only property of a pass the proof used was that it leaves its ties alone",
                   "The output is still sorted, but the work rises",
                   "Only keys sharing that digit are affected, and only among themselves"],
             "c": 1,
             "why": "The induction step handles two keys agreeing in the current digit by "
                    "appealing to the order the previous pass left them in, and an unstable "
                    "pass may not preserve it. The lab's unstable variant returns "
                    "`355 329 457 436 657 720 839`, which is not sorted at all."},
            {"q": "The same seven keys cost `3 × (7 + 10) = 51` in base ten and `10 × (7 + 2) = 90` in base two. What is the trade?",
             "a": ["A larger base is always cheaper",
                   "A larger base means fewer digits and a bigger bucket array, so the product `d(n + b)` is what to compare",
                   "Base two is wrong for decimal keys",
                   "The number of passes does not depend on the base"],
             "c": 1,
             "why": "`d = ⌈log_b U⌉` falls as `b` rises and the per-pass cost `n + b` rises with "
                    "it, so neither term decides alone. Base sixteen on these keys costs "
                    "`3 × 23 = 69`, worse than base ten, which is what &ldquo;always "
                    "cheaper&rdquo; would not predict."},
            {"q": "Radix sort spent 51 units of work on seven keys, while `⌈log₂ 7!⌉ = 13` comparisons are necessary for any comparison sort. Which reading is right?",
             "a": ["Radix sort is worse, since 51 is more than 13",
                   "The units are not comparisons: radix sort makes none, so the bound describes a model it is not in",
                   "Radix sort beat the bound by not comparing",
                   "The bound applies only to sorts of numbers, not of digits"],
             "c": 1,
             "why": "A digit extraction and a bucket append are not comparisons, so the two "
                    "figures are in different units and neither beats nor loses to the other. "
                    "&ldquo;Beat the bound&rdquo; is the same error in a friendlier tone: the "
                    "theorem's hypothesis simply does not hold here."},
        ],
        "mistakes": [
            ("Starting from the most significant digit",
             "The intuition is that the important digit should be settled first, and the "
             "arithmetic says otherwise: whichever pass runs last determines the order, so the "
             "most significant digit must be sorted last. Most-significant-first is a real "
             "algorithm, but only with a recursive sort inside each bucket, which is exactly "
             "the part the lab omits in order to show what it was doing."),
            ("Treating the per-digit sort as interchangeable",
             "Any sort will order one digit; only a stable one composes. If a pass is "
             "implemented with something convenient and unstable, the array can come out "
             "sorted on some inputs by luck &mdash; and the lab says so on its face, because "
             "a variant that sometimes works is harder to distrust than one that never does."),
            ("Calling radix sort linear",
             "`Θ(d(n + b))` is linear in `n` for a fixed `d` and `b`, and `d` is `⌈log_b U⌉`, "
             "which depends on how wide the keys are. Quoting `Θ(n)` hides two choices and one "
             "property of the data. State the number of passes and the base, as the lab's two "
             "counters do."),
        ],
        "standard": ("Finish when you can say which property of a pass the correctness argument uses, and check it between passes.",
                     "You should be able to run three digit passes by hand, verify after each "
                     "one that the array is sorted on the digits seen so far, compute "
                     "`d(n + b)` at two bases, and explain both failure modes from the "
                     "induction rather than from the output."),
        "note": ("Counting sort and radix sort escape the comparison bound by reading the key. "
                 "“Bucket Sort and Average-Case Claims” looks at an algorithm that "
                 "compares after all and still "
                 "claims to be linear &mdash; and the claim turns out to rest on an "
                 "assumption about where the keys come from, which is a different kind of "
                 "promise from anything made so far."),
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "bucket-sort-and-average-case-claims",
        "title": "Bucket Sort and Average-Case Claims",
        "module": "Not comparing at all",
        "one_line": "State bucket sort's distributional assumption, compute the expected work, and build the input that makes it quadratic.",
        "summary": (
            "Scatter `n` keys into `b` equal-width buckets, insertion-sort each bucket, and "
            "concatenate. If the keys are uniform over the range, the expected work inside "
            "the buckets is `n(n/b − 1)/2`, which is linear when `b` is about `n`. That "
            "expectation is over the input distribution, not over anything the algorithm "
            "does, so it stops being true exactly when the keys stop being uniform &mdash; "
            "and the algorithm cannot tell."
        ),
        "key": [
            "scatter into b equal-width buckets, insertion-sort each, concatenate",
            "E[work inside the buckets] = n(n/b − 1)/2   IF the keys are uniform",
            "48 keys, 12 buckets:   expected 72,   measured 90 on a uniform draw",
            "the same 48 keys clustered in a twentieth of the range:   592",
            "worst possible for 48 keys:  n(n − 1)/2 = 1128",
        ],
        "key_label": "The expectation, its hypothesis, and what happens when the hypothesis fails",
        "concepts_intro": (
            "The hard idea is a distinction, and it is the reason this lesson sits four after "
            "randomised quicksort rather than next to the other linear-time sorts."
        ),
        "concepts": [
            ("This expectation is over the input, not over the algorithm",
             "Randomised quicksort's `2(n+1)Hₙ − 4n` averages over the pivots the algorithm "
             "draws, so it holds for every array. Bucket sort's linear bound averages over a "
             "distribution the input is assumed to follow, and the algorithm makes no random "
             "choices at all: run it twice on the same keys and it does exactly the same "
             "thing. An assumption about the data is a promise somebody else has to keep."),
            ("The work is all inside the buckets",
             "Scattering is one pass and concatenating is another, so the interesting term is "
             "the insertion sorts. A bucket holding `m` keys costs up to `m(m − 1)/2` "
             "comparisons, and summing that over buckets with `n/b` keys each gives "
             "`n(n/b − 1)/2` &mdash; zero when every bucket holds one key, and `n(n − 1)/2` "
             "when one bucket holds all of them. The whole range of behaviour is in how the "
             "keys divide."),
            ("The bound fails exactly when the distribution does",
             "Nothing about the algorithm changes when you change the distribution; the same "
             "code runs. At 48 keys in 12 buckets a uniform draw measures 90 comparisons, "
             "keys clustered in a twentieth of the range measure 592, and keys confined to "
             "one bucket measure 582. Double `n` on the clustered family and the count goes "
             "from 140 at 24 keys to 592 at 48 to 2282 at 96: roughly four times the work for "
             "twice the keys, which is what a quadratic cost looks like when it is measured."),
        ],
        "read_title": "A linear expectation, and the hypothesis it is standing on",
        "read_intro": "Where the expected work comes from, what it assumes, and what the same algorithm costs when the assumption is false.",
        "body": [
            ("def", ("Bucket sort",
                     "<strong>Bucket sort</strong> over a key range `[0, U)` with `b` buckets: "
                     "place each key `x` into bucket `⌊bx/U⌋`, sort each bucket with insertion "
                     "sort, and concatenate the buckets in order. The buckets are equal in "
                     "<em>width</em>; nothing makes them equal in <em>occupancy</em>.")),
            ("p", "The scatter is `Θ(n)` and the concatenation is `Θ(n + b)`. Everything else "
                  "is the insertion sorts, and their cost depends on the bucket sizes, which "
                  "depend on the keys. So the analysis is not about the algorithm at all: it "
                  "is about a random variable determined by where the keys fall."),
            ("math", [
                "if every bucket holds n/b keys, insertion sort inside one costs",
                "    (n/b)(n/b − 1)/2      at worst",
                "summed over b buckets:",
                "    b · (n/b)(n/b − 1)/2  =  n(n/b − 1)/2",
                "",
                "n = 48, b = 12:   48 · (4 − 1)/2  =  72        exactly",
                "n = 96, b = 12:   96 · (8 − 1)/2  =  336",
                "n = 48, b = 48:   48 · (1 − 1)/2  =  0",
            ]),
            ("p", "With `b = n` the expected inner work is zero, which is the sense in which "
                  "bucket sort is called linear: the remaining cost is the scatter and the "
                  "concatenation. The lab evaluates the expression as an exact rational, "
                  "because the point of printing it beside a measurement is that the two are "
                  "different kinds of number and can be subtracted."),
            ("example", ("Forty-eight keys, three distributions, one algorithm",
                         "Twelve buckets throughout. A uniform draw fills them "
                         "`4 4 9 2 3 0 3 4 3 1 8 7` and costs 90 comparisons against an "
                         "expectation of 72. Keys clustered in a twentieth of the range put "
                         "all 48 into one bucket and cost 592. Keys confined to the first "
                         "bucket cost 582. All three outputs are sorted; only the cost moved, "
                         "and the code did not.")),
            ("p", "The gap between 72 and 90 on the uniform draw is worth a sentence of its "
                  "own, because it is the honest half of the lesson. 72 is an expectation "
                  "over the distribution; 90 is one draw from it. The bucket sizes above are "
                  "visibly uneven &mdash; one bucket empty, one holding nine &mdash; and that "
                  "unevenness is what a uniform draw looks like at `n = 48`. A measurement "
                  "above the expectation is not a refutation of it."),
            ("h3", "Two expectations, side by side"),
            ("p", "Put the two claims of this course in the same sentence and the difference "
                  "is unmissable. Randomised quicksort: for every array, the average over the "
                  "algorithm's pivots is `2(n+1)Hₙ − 4n`. Bucket sort: for keys drawn "
                  "uniformly, the average over the draw is `n(n/b − 1)/2`. The first "
                  "quantifies over inputs and averages over coins the algorithm controls; the "
                  "second averages over inputs and controls nothing."),
            ("p", "That is why one of them survives a hostile input and the other does not. An "
                  "adversary who picks the array cannot move randomised quicksort's "
                  "expectation, because the expectation never mentioned the array. An "
                  "adversary who picks the keys moves bucket sort's cost to `Θ(n²)` by putting "
                  "them all in one bucket, and the lab ships exactly that input."),
            ("p", "None of which makes bucket sort a bad algorithm. It makes its bound a "
                  "conditional one, and the condition is checkable: where do the keys come "
                  "from, and is the range they are spread over the range the buckets divide? "
                  "Hash values, uniformly generated identifiers and quantised sensor readings "
                  "often satisfy it. Prices, word lengths and timestamps of human activity "
                  "usually do not."),
            ("p", "One last discipline. The measured 582 on the one-bucket input is not the "
                  "worst case; `n(n − 1)/2 = 1128` is, and insertion sort only reaches it on a "
                  "reversed bucket. The measured column is one input's cost and the proved "
                  "column is about all of them, and this page keeps them apart on purpose."),
        ],
        "lab": ("sortkit", {
            "mode": "bucket",
            "dist": "uniform",
            "n": 48,
            "buckets": 12,
            "seed": 7,
            "panel_title": "Choose the distribution, the size and the buckets",
            "panel_intro": "Keys come off the seeded stream under the distribution you pick, "
                           "and every comparison is counted inside the bucket it happened in. "
                           "The algorithm does not change when the distribution does.",
        }),
        "steps_title": "Reading an average-case claim",
        "steps_intro": "Every average-case bound has a hypothesis. Find it before you find the bound.",
        "steps": [
            ("Say what the expectation is over",
             "Over the algorithm's own random choices, or over a distribution the input is "
             "assumed to follow? Write the sentence out in full. If the answer is the second, "
             "the bound is a conditional statement and the condition belongs in every "
             "quotation of it."),
            ("Compute the expected work before measuring anything",
             "`n(n/b − 1)/2` at your `n` and `b`. At 48 keys over 12 buckets it is exactly 72. "
             "This is the number the measurement will be compared against, and having it "
             "first stops the measurement from becoming the claim."),
            ("Measure a draw, and expect it to differ",
             "90 against 72 on the uniform draw. A single draw is a sample of the "
             "distribution the expectation is over, so it moves when the seed moves. Watch it "
             "move."),
            ("Now break the hypothesis on purpose",
             "Switch to the clustered keys and read the count: 592 for the same 48 keys "
             "through the same code. Then change `n` and check the growth. Roughly four times "
             "the work for twice the keys is quadratic behaviour on this family &mdash; "
             "measured, not proved."),
            ("Report the bound with its condition attached",
             "&ldquo;Linear if the keys are uniform over the bucketed range, quadratic in the "
             "worst case&rdquo; is the whole claim. `Θ(n)` on its own is the misconception, "
             "and it is the one the lab's distribution control exists to break."),
        ],
        "worked": {
            "title": "Forty-eight keys through twelve buckets, three ways",
            "intro": [
                "The bucket count, the key count and the code are identical in all three rows. "
                "Only where the keys fall is different, and the expectation in the second "
                "column is the same number throughout because it is computed from `n` and `b` "
                "alone.",
            ],
            "lines": [
                "expected inner work, if uniform:   n(n/b − 1)/2 = 48 · 3/2 = 72   (exact)",
                "",
                "  distribution                 bucket sizes            measured   per key",
                "  uniform over the range       4 4 9 2 3 0 3 4 3 1 8 7      90      1.88",
                "  clustered in a twentieth     0 48 0 0 0 0 0 0 0 0 0 0     592     12.33",
                "  all inside the first bucket  48 0 0 0 0 0 0 0 0 0 0 0     582     12.13",
                "",
                "growth of the clustered family, twelve buckets throughout",
                "  n = 24    140",
                "  n = 48    592        4.2 × the work for 2 × the keys",
                "  n = 96   2282        3.9 ×",
                "",
                "worst possible at n = 48:   n(n − 1)/2 = 1128",
                "all three outputs were checked against the sorted array: all three sorted",
            ],
            "after": [
                "The middle column is the only thing that changed, and it is not part of the "
                "algorithm. That is the entire content of &ldquo;an average-case bound is a "
                "claim about the input&rdquo;, and it is why the row for the clustered keys "
                "is the same code costing six and a half times as much.",
                "Two figures are deliberately not equal to anything. 90 is not 72, because one "
                "draw is not an expectation. And 592 is not 1128, because the worst case needs "
                "the one full bucket to be in reverse order as well as full &mdash; the "
                "measured column is this input and the proved column is all of them.",
                "For a faded rehearsal, keep the clustered keys and raise the bucket count from "
                "12 to 32. The supplied first move is the prediction: the buckets are "
                "equal-width, and the keys occupy a twentieth of the range, so widening the "
                "bucket count divides that twentieth among at most two buckets. Say whether "
                "the cost falls by much, then check &mdash; and then say what bucket count "
                "would actually fix this input, and whether you could have known it without "
                "seeing the keys.",
            ],
        },
        "quiz_title": "Which expectation, over what",
        "quiz": [
            {"q": "Is bucket sort `O(n)`?",
             "a": ["Yes",
                   "It is `O(n)` in expectation when the keys are uniform over the bucketed range, and `Θ(n²)` in the worst case",
                   "No: it is `Θ(n log n)` like every other comparison sort",
                   "Yes, provided the number of buckets is at least `n`"],
             "c": 1,
             "why": "The bound has a hypothesis and the lab breaks it: 48 clustered keys cost "
                    "592 comparisons through the same code that costs 90 on a uniform draw. "
                    "More buckets do not save it either &mdash; equal-width buckets do not "
                    "help when every key falls inside one of them."},
            {"q": "Which of these two expectations survives an adversary who chooses the input?",
             "a": ["Both, since both are expectations",
                   "Neither",
                   "Randomised quicksort's, because its randomness is in the pivot; bucket sort's assumption is about the data",
                   "Bucket sort's, because insertion sort is adaptive"],
             "c": 2,
             "why": "`2(n+1)Hₙ − 4n` never mentions the array, so choosing the array cannot "
                    "move it &mdash; the lab confirms this by enumeration on five different "
                    "arrays. Bucket sort makes no random choices at all, so an adversary who "
                    "puts every key in one bucket gets quadratic behaviour with certainty."},
            {"q": "All 48 keys in one bucket cost 582 comparisons; 96 such keys cost 2282. What does that support?",
             "a": ["That the cost is `Θ(n)` with a large constant",
                   "That the count roughly quadrupled when `n` doubled, the signature of a quadratic cost on this family &mdash; measured, not proved",
                   "That 582 is the worst case at 48 keys",
                   "That the bucket count was chosen badly"],
             "c": 1,
             "why": "Two measurements at two sizes are evidence about this family and nothing "
                    "more, which is why the answer says so. The worst case at 48 keys is "
                    "`n(n − 1)/2 = 1128`, which needs the full bucket to be in reverse order "
                    "as well; 582 is under it."},
            {"q": "The expected inner work at 48 keys over 12 buckets is exactly 72, and the uniform draw measured 90. What does the gap mean?",
             "a": ["The formula is wrong",
                   "One draw is a sample of the distribution the expectation is over",
                   "The keys were not uniform after all",
                   "The buckets were unequal in width"],
             "c": 1,
             "why": "The bucket sizes on that draw were `4 4 9 2 3 0 3 4 3 1 8 7` &mdash; "
                    "uneven, which is what a uniform draw of 48 keys into 12 buckets looks "
                    "like. The buckets are equal in width by construction; it is occupancy "
                    "that varies, and the expectation averages over exactly that variation."},
        ],
        "mistakes": [
            ("Quoting `O(n)` without the hypothesis",
             "The bound is conditional and the condition is about where the keys come from. "
             "Repeating the conclusion without it is how an algorithm gets chosen for data it "
             "was never analysed on, and the failure is silent: the output is still correct, "
             "just six times dearer, and it gets dearer faster as `n` grows."),
            ("Confusing an average over inputs with an average over coin flips",
             "Randomised quicksort's expectation holds for each input separately because the "
             "randomness belongs to the algorithm. Bucket sort's holds for a distribution of "
             "inputs and says nothing about the input you have. Both sentences begin "
             "&ldquo;expected&rdquo;, and only one of them is a promise the algorithm can keep "
             "on its own."),
            ("Reading a measured quadratic count as the worst case",
             "582 comparisons on 48 keys in one bucket is a measurement; the worst case is "
             "`n(n − 1)/2 = 1128`, reached only when that bucket is also in reverse order. "
             "This course prints the measured and the proved figure side by side for exactly "
             "this reason, and a count on one input never becomes a bound by being large."),
        ],
        "standard": ("Finish when you can state an average-case bound with its hypothesis and then break it.",
                     "You should be able to derive `n(n/b − 1)/2`, evaluate it exactly at a "
                     "given `n` and `b`, say what the expectation is over, produce an input "
                     "that makes the algorithm quadratic, and explain why randomised "
                     "quicksort's expectation is a different kind of claim."),
        "note": ("That closes the sorts. The next two lessons ask for less than a sorted array "
                 "&mdash; a single order statistic &mdash; and find that less work is needed "
                 "for it. &ldquo;Quickselect&rdquo; recurses into one side only, and the "
                 "recurrence loses a term, which turns out to be the whole difference between "
                 "`n log n` and linear."),
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "quickselect",
        "title": "Quickselect",
        "module": "Selection, bounds and scale",
        "one_line": "Find the k-th smallest element without sorting, and give the argument for why a random pivot makes it expected linear.",
        "summary": (
            "Partition, then look at where the pivot landed: if its rank is the one you "
            "wanted you are finished, and otherwise the answer is on one known side and the "
            "other side can be discarded entirely. One recursive call instead of two turns "
            "`n log n` into expected linear, because a pivot in the middle half occurs with "
            "probability one half and leaves at most three quarters of the range."
        ),
        "key": [
            "partition; if the pivot's rank is k, stop; else recurse into the ONE side holding k",
            "T(n) = T(size of that side) + (n − 1)      one recursive term, not two",
            "a pivot in the middle half:  probability ½, and at most 3n/4 survives",
            "E[comparisons] < 4n        at n = 24 that reference line is 96",
            "24 keys, seed 5:   35 comparisons;  sorting first:  83",
        ],
        "key_label": "One recursive call, and the bound it buys",
        "concepts_intro": (
            "The hard idea is that discarding one side changes the recurrence's shape, and "
            "that a pivot does not have to be good to be good enough."
        ),
        "concepts": [
            ("One recursive term is the entire difference",
             "Quicksort's recurrence has two recursive terms because both sides still have to "
             "be sorted. Quickselect's has one, because the rank you want lies on exactly one "
             "side and the other side is thrown away, unexamined. Summing the sizes down a "
             "single chain that shrinks by a constant factor gives a geometric series and a "
             "linear total, where summing over a branching tree gives `n` per level and "
             "`log n` levels."),
            ("A good pivot is one in the middle half, and half of them are",
             "Call a pivot good if its rank lies between `n/4` and `3n/4`. A uniformly random "
             "pivot is good with probability one half, and a good pivot leaves at most `3n/4` "
             "elements for the next call. So the expected number of partitions before the "
             "range shrinks by a quarter is two, and the sizes fall geometrically. The "
             "substitution method sharpens the constant to `4n`, which is the reference line "
             "the lab prints."),
            ("Expected linear is not a promise about the run in front of you",
             "On the lab's 24-key array, seed 5 costs 35 comparisons and seed 1 costs 108, "
             "against merge sort's 83 for sorting the whole array. So one draw can lose to "
             "sorting, and one draw can exceed `4n = 96`. Over 200 seeds the mean is 59.6. "
             "The claim is about that mean; a single count is one sample of it, and the lab "
             "says so in the sentence under the plot."),
        ],
        "read_title": "Discarding a side, and what a random pivot is worth",
        "read_intro": "The algorithm, the recurrence with one term, the expected-linear argument, and the spread a single run can show.",
        "body": [
            ("def", ("Order statistic",
                     "The <strong>k-th order statistic</strong> of `n` values is the `k`-th "
                     "smallest of them. The first is the minimum, the `n`-th is the maximum, "
                     "and the median is the `⌈n/2⌉`-th. Finding one is the "
                     "<strong>selection</strong> problem.")),
            ("def", ("Quickselect",
                     "<strong>Quickselect</strong> finds the `k`-th smallest of "
                     "`a[lo..hi]`. Partition the range; let `q` be the pivot's index and `r` "
                     "its rank within the range. If `r = k`, return the pivot. If `k &lt; r`, "
                     "recurse on `a[lo..q−1]` for the same `k`; otherwise recurse on "
                     "`a[q+1..hi]` for `k − r`. The other side is never looked at again.")),
            ("p", "Everything about the partition is unchanged, so a call on a range of `m` "
                  "elements still costs `m − 1` comparisons. What changed is that only one of "
                  "the two pieces is visited."),
            ("math", [
                "quicksort      T(n) = T(k) + T(n − k − 1) + (n − 1)      two terms",
                "quickselect    T(n) = T(one side)         + (n − 1)      one term",
                "",
                "if every pivot were exactly median:",
                "    T(n) = T(n/2) + n  =  n + n/2 + n/4 + …  <  2n",
                "if every pivot were worst:",
                "    T(n) = T(n − 1) + (n − 1)  =  n(n − 1)/2",
            ]),
            ("thm", ("Randomised quickselect is expected linear",
                     "With the pivot of each call drawn uniformly at random from that call's "
                     "range, the expected number of comparisons quickselect makes on `n` "
                     "elements is less than `4n`, for every input and every `k`.")),
            ("proof", ("Call a pivot good if its rank within the range lies in the middle half. "
                       "A uniformly drawn pivot is good with probability at least one half, and "
                       "a good pivot leaves a range of at most `3n/4` for the next call.",
                       "So the expected number of calls spent before the range first drops to "
                       "`3n/4` or below is at most two, and each of those calls costs less than "
                       "`n`. Charging that to a size class, the expected total is at most "
                       "`2n(1 + 3/4 + 9/16 + …) = 8n`, which is already linear.",
                       "The constant is loose because a bad pivot still shrinks the range. "
                       "Solving `T(n) ≤ (1/n)Σ T(m) + (n − 1)`, with the sum over the "
                       "`m` from `⌈n/2⌉` to `n − 1` that a pivot can leave, by substitution "
                       "gives `T(n) ≤ 4n`, and that is the line the lab draws.")),
            ("example", ("The twelfth smallest of twenty-four, seed 5",
                         "The array is a seeded shuffle of `1 … 24`, and the twelfth smallest "
                         "is `12`. Three partitions find it: the range `1–24` shrinks to "
                         "`12–24`, then to a single element. 35 comparisons, against merge "
                         "sort's 83 for sorting the array and indexing into it &mdash; a "
                         "baseline counted by an implementation written for another course "
                         "that has never heard of this one.")),
            ("p", "Change the seed and the count moves: 108 at seed 1, 57 at seed 2, 86 at "
                  "seed 3, 35 at seed 5. Over 200 seeds the mean is 59.6 and the extremes are "
                  "23 and 118. Two of those draws are above the `4n = 96` reference line, "
                  "which is allowed: `4n` bounds the expectation, not each run. A reader who "
                  "takes a single count as the bound will see it violated and conclude the "
                  "wrong thing."),
            ("h3", "A deterministic rule fails here in the same way it failed for sorting"),
            ("p", "Take the first element as the pivot and ask for the median of an already "
                  "sorted array of 24: the pivot is the smallest key every time, one element "
                  "is discarded per call, and the lab measures 210 comparisons against merge "
                  "sort's 52 on the same array. Selection lost, badly, and for exactly the "
                  "reason &ldquo;Quicksort and Its Worst Case&rdquo; gave. “Median of "
                  "Medians” removes the randomness instead of relying on it."),
            ("p", "One place this matters outside the course: System Design's "
                  "&ldquo;Percentiles from a Sample&rdquo; finds the `⌈qn⌉`-th sorted value of "
                  "a latency sample by sorting the sample and indexing into it. That is "
                  "`Θ(n log n)` for a single order statistic, and selection would do it in "
                  "expected linear time &mdash; the same answer, the same rank, one recursive "
                  "call per level instead of a full sort."),
        ],
        "lab": ("sortkit", {
            "mode": "select",
            "n": 24,
            "k": 12,
            "rule": "random",
            "order": "shuffle",
            "seed": 5,
            "panel_title": "Choose the rank, the array and the pivot rule",
            "panel_intro": "The comparisons are counted as quickselect makes them, and the "
                           "baseline beside them is merge sort's own total on the same array. "
                           "The bars show the range still in play after each partition.",
        }),
        "steps_title": "Selecting, and reporting what the count means",
        "steps_intro": "The procedure is short. The discipline is in what you say about the number it produces.",
        "steps": [
            ("Partition once and read the pivot's rank",
             "The rank is the pivot's position within the range, not within the whole array, "
             "and getting that wrong is the commonest implementation bug. Compare it with the "
             "`k` you are looking for."),
            ("Discard the side that cannot hold the answer",
             "If `k` is below the rank, everything from the pivot rightwards is gone; "
             "otherwise everything leftwards is, and `k` is reduced by the rank. Write the new "
             "`k` down explicitly. The lab draws the surviving range as a bar so the "
             "discarding is visible."),
            ("Recurse on the one side until the range is a single element",
             "Or until the pivot's rank is `k` exactly, which can happen at any depth. Count "
             "the partitions: three on the worked run, and the lab's calls counter reports "
             "them."),
            ("Put the count beside a baseline that did not come from quickselect",
             "Merge sort's total on the same array, counted by running it. 35 against 83 on "
             "the worked run. If selection is not beating a full sort, say so: on a "
             "deterministic pivot rule and the wrong array it will not, and 210 against 52 is "
             "what that looks like."),
            ("Move the seed before you draw a conclusion",
             "One seed is one draw. Over 200 of them the count ranges from 23 to 118 with a "
             "mean of 59.6, and two of those numbers straddle the `4n` reference line. Report "
             "the mean as the expectation's neighbour and the single run as a sample."),
        ],
        "worked": {
            "title": "The twelfth smallest of twenty-four, with the ranges that disappear",
            "intro": [
                "The array is the lab's seeded shuffle of `1 … 24`, the pivot rule is a seeded "
                "random element, and the seed is 5. The rank asked for is 12, which on this "
                "array is the median, and the value is `12`.",
            ],
            "lines": [
                "array   24 16  1 10 15  2 13 21  6 19 18  7 12 11  5  4 17  8 22 20 23  9  3 14",
                "want    the 12th smallest",
                "",
                " call   range in play   size   pivot rank   k after   comparisons",
                "   1      1 – 24         24        11         12          23",
                "   2     12 – 24         13        13         12          12",
                "   3     12 – 12          1         —          —           0",
                "",
                "found   12          measured    35 comparisons, 3 partitions",
                "",
                "sorting the array first and indexing:   83 comparisons (merge sort)",
                "4n, the reference line for the expectation:   96",
                "⌈log₂ 24!⌉, what a comparison SORT would need:   80",
                "",
                "the same array and rank, over 200 seeds:  low 23, mean 59.6, high 118",
            ],
            "after": [
                "The first call discarded eleven elements and the second discarded twelve, and "
                "neither discarded side was ever examined again. That is the one recursive "
                "term made concrete: 23 + 12 comparisons rather than the 83 a full sort "
                "spends, and the saving is not in the partition, which is identical, but in "
                "the half of the work that never happens.",
                "Three of those numbers deserve to be kept apart. 35 is a measurement on one "
                "array with one seed. 59.6 is a mean over 200 seeds, which is a sample of the "
                "expectation. 96 is `4n`, a bound on the expectation, and the high draw of 118 "
                "is above it, as a single run is entitled to be.",
                "For a faded rehearsal, keep the array and change the rank to 1, the minimum. "
                "The supplied first move is a prediction about the shape: the answer is always "
                "in the left piece unless the pivot is the minimum itself, so the ranges "
                "should shrink from the right. Predict whether selecting the minimum is "
                "cheaper than selecting the median, then check it over a few seeds &mdash; and "
                "say why the expected-linear argument does not care which `k` was asked for.",
            ],
        },
        "quiz_title": "One side, and what the expectation covers",
        "quiz": [
            {"q": "Does finding the median of `n` values require sorting them?",
             "a": ["Yes: the median is defined by the sorted order",
                   "No: quickselect finds it in expected linear time, and median of medians in linear time on every input",
                   "Only when `n` is even",
                   "No, but only if the values are integers in a small range"],
             "c": 1,
             "why": "The median is defined by the sorted order and does not require producing "
                    "it. The lab found the twelfth smallest of 24 in 35 comparisons where "
                    "sorting the array cost 83, and “Median of Medians” removes the word "
                    "&ldquo;expected&rdquo; from that sentence."},
            {"q": "What is the one change from quicksort's recurrence to quickselect's?",
             "a": ["The partition is cheaper",
                   "There is one recursive term instead of two",
                   "The pivot rule is different",
                   "The comparisons are counted per level rather than per call"],
             "c": 1,
             "why": "The partition is identical and costs `m − 1` either way. Only one side can "
                    "contain the rank you want, so the other is discarded, and summing sizes "
                    "down one shrinking chain gives a geometric series where a branching tree "
                    "gives `n` per level."},
            {"q": "On the same array and rank, seed 1 cost 108 comparisons where sorting costs 83, and `4n` is 96. Does that refute the expected-linear bound?",
             "a": ["Yes: the count exceeded `4n`",
                   "No: `4n` bounds the mean over pivot choices, and one draw is not the mean",
                   "Yes, for that array",
                   "No, because 108 is still under `4n`"],
             "c": 1,
             "why": "A bound on an expectation constrains the average, not every outcome; over "
                    "200 seeds on this array the mean is 59.6, comfortably under 96. The last "
                    "answer is false arithmetic as well as a false principle: 108 is above 96."},
            {"q": "A service computes its 99th-percentile latency by sorting a sample of 10 000 measurements and indexing at position 9 900. What does this lesson offer?",
             "a": ["Nothing: the percentile is defined by the sorted order, so the sort is required",
                   "Selection: the `⌈qn⌉`-th value can be found in expected linear time without producing the sorted array",
                   "A faster sorting algorithm for the same job",
                   "A bound on how many samples are needed"],
             "c": 1,
             "why": "It is one order statistic, which is exactly what selection returns. "
                    "System Design's &ldquo;Percentiles from a Sample&rdquo; does it by "
                    "sorting, which is `Θ(n log n)` for a single value; nothing else about "
                    "that lesson changes if the sort is replaced."},
        ],
        "mistakes": [
            ("Sorting to get one value",
             "It is the default move and it does `Θ(n log n)` work for a `Θ(n)` question. The "
             "test is whether anything downstream needs the whole ordering: a median, a "
             "percentile, a top-`k` threshold do not. If several order statistics are wanted, "
             "the arithmetic changes and sorting can win again &mdash; that is a comparison of "
             "counts, not a default."),
            ("Reading expected linear as a per-run guarantee",
             "Seed 1 cost 108 comparisons on an array where `4n` is 96, and that is not a bug. "
             "The bound is on the mean over the pivot draws; individual runs scatter, from 23 "
             "to 118 over 200 seeds here. Quote the bound with the word "
             "&ldquo;expected&rdquo; in it, or quote the measured spread."),
            ("Forgetting to shift `k` when recursing right",
             "Recursing into the right side means the elements to the left of the pivot are "
             "gone, so the rank you are now looking for is `k` minus the pivot's rank within "
             "the range. Leaving `k` unchanged returns a plausible wrong answer rather than an "
             "error, which is the worst kind. The lab prints the value found beside the "
             "sorted array's entry at that rank, so a mismatch is visible."),
        ],
        "standard": ("Finish when you can select by hand and say exactly what the linear claim covers.",
                     "You should be able to run quickselect on paper with the ranks and the "
                     "shifted `k` written down, state the recurrence with one term, give the "
                     "good-pivot argument, and distinguish a single measured count from the "
                     "mean over seeds and from the bound on the expectation."),
        "note": ("The word &ldquo;expected&rdquo; is doing real work in that bound, and it can "
                 "be removed. &ldquo;Median of Medians&rdquo; chooses a pivot that is "
                 "guaranteed to be near the middle rather than likely to be, and the price is "
                 "a recurrence with two recursive terms that is still linear &mdash; because "
                 "the fractions in it sum to less than one."),
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "median-of-medians",
        "title": "Median of Medians",
        "module": "Selection, bounds and scale",
        "one_line": "Choose a pivot with a guarantee, solve the two-term recurrence by its level sums, and explain the group size.",
        "summary": (
            "Break the array into groups of five, take each group's median, and take the "
            "median of those medians as the pivot &mdash; recursively. The pivot is then "
            "guaranteed to lie in the middle forty per cent, so at least `3n/10` elements are "
            "discarded and the recurrence is `T(n) ≤ T(n/5) + T(7n/10) + cn`. That is linear "
            "because `1/5 + 7/10` is less than one, and with groups of three the same two "
            "fractions sum to exactly one and it is not."
        ),
        "key": [
            "groups of 5, median of each, pivot = median of those medians (recursively)",
            "guaranteed: at least 3n/10 discarded, so at most 7n/10 survives",
            "T(n) ≤ T(n/5) + T(7n/10) + cn      1/5 + 7/10 = 9/10 < 1   ⟹   linear",
            "n = 45, groups of 5:   the level sums total exactly 450 = 10n",
            "groups of 3:   1/3 + 2/3 = 1       every level costs n, so n log n",
        ],
        "key_label": "The pivot rule, the guarantee, and the sum that decides linearity",
        "concepts_intro": (
            "The hard idea is that the two fractions of a two-term recurrence decide "
            "everything, and that they are decided in turn by the group size."
        ),
        "concepts": [
            ("The pivot only has to be near the middle",
             "Let `p` be the median of the `⌈n/5⌉` group medians. At least half of those "
             "medians are at most `p`, and each of their groups contributes three elements at "
             "most `p` &mdash; its median and the two below it. So at least "
             "`3⌈⌈n/5⌉/2⌉` elements are at most `p`, which is about `3n/10`, and symmetrically "
             "about `3n/10` are at least `p`. The pivot is not the median and does not need to "
             "be: it is guaranteed to sit in the middle forty per cent."),
            ("Linearity is decided by whether the fractions sum to under one",
             "The recurrence has two recursive terms &mdash; one call on the `n/5` medians to "
             "find the pivot, one on the at most `7n/10` survivors &mdash; so the master "
             "theorem does not apply. The recursion tree does: level zero costs `cn`, level "
             "one costs `c(1/5 + 7/10)n`, level two `c(9/10)²n`, and the sum is geometric "
               "with ratio `9/10`, giving `10cn`. The lab evaluates those level sums as exact "
               "fractions, and at `n = 45` they total exactly `450 = 10n`."),
            ("The guarantee costs a constant, and the constant is visible",
             "On the lab's 45-element array, median of medians spends 299 comparisons and "
             "quickselect spends 131 for the same rank. That is the price of removing the "
             "word &ldquo;expected&rdquo;: quickselect is linear in expectation with a small "
             "constant, median of medians is linear on every input with a large one. In "
             "practice the two are combined, and the theoretical value of this one is that it "
             "makes the deterministic bound available at all."),
        ],
        "read_title": "A pivot with a guarantee, and the recurrence it buys",
        "read_intro": "The counting argument for the discard, the level sums that solve a two-term recurrence, and what group size three does to them.",
        "body": [
            ("def", ("Median of medians",
                     "To choose a pivot of `a[1..n]` by <strong>median of medians</strong> "
                     "with group size `g`: split the array into `⌈n/g⌉` groups of `g` "
                     "consecutive elements, find each group's median by direct sorting, and "
                     "return the median of those `⌈n/g⌉` medians, found by applying the whole "
                     "selection algorithm to them recursively.")),
            ("ol", [
                "Split into groups of `g`; sort each group and take its median. Cost `Θ(n)`, since `g` is a constant.",
                "Recursively select the median of the `⌈n/g⌉` medians. This is the first recursive term.",
                "Partition the array around that pivot.",
                "If the pivot's rank is the one wanted, return it; otherwise recurse into the surviving side. This is the second recursive term.",
            ]),
            ("thm", ("The discard guarantee",
                     "With groups of five, the median of medians `p` has at least "
                     "`3(⌈⌈n/5⌉/2⌉ − 2)` elements at most `p` and at least as many at least "
                     "`p`. Asymptotically that is `3n/10`, so at most `7n/10` elements survive "
                     "the partition.")),
            ("proof", ("Half of the `⌈n/5⌉` group medians are at most `p`, by the definition of "
                       "a median. Take any such group: its own median is at most `p`, and so "
                       "are the two elements of that group below its median. That is three "
                       "elements at most `p` from each of those groups.",
                       "Two groups have to be set aside: the group containing `p` itself, and "
                       "the last group if it is not full. That is where the `− 2` comes from. "
                       "Everything else is symmetric for the elements at least `p`.",
                       "So at least about `3n/10` elements are on each side of the pivot, and "
                       "the side that survives the partition holds at most `n − 3n/10 = 7n/10` "
                       "of them.")),
            ("math", [
                "T(n) ≤ T(n/5) + T(7n/10) + cn",
                "",
                "level 0      cn",
                "level 1      c(1/5 + 7/10)n  =  c(9/10)n",
                "level 2      c(9/10)²n",
                "…",
                "total        cn · 1/(1 − 9/10)  =  10cn",
                "",
                "groups of 3:   1/3 + 2/3 = 1     every level costs cn, and there are log n",
            ]),
            ("p", "So the whole argument is one comparison of a sum with one, and the lab does "
                  "it as a comparison of integers: `1/5 + 7/10 = 9/10` and `1/3 + 2/3 = 1` are "
                  "computed as exact rationals, because `0.8999999999999999` is not an "
                  "argument. Groups of seven give `1/7 + 5/7 = 6/7`, which also converges, and "
                  "at `n = 45` the level sums total `315 = 7n`."),
            ("example", ("One round at forty-five elements",
                         "The lab's array at `n = 45` is a seeded shuffle of `1 … 45`. Its nine "
                         "group medians are `24 35 21 27 14 38 8 16 25`, and the median of "
                         "those is `24`. Partitioning around `24` leaves 23 elements below and "
                         "21 above. The guarantee for this size and group is 9, so the round "
                         "discarded 21 where it had promised 9 &mdash; and the promise is the "
                         "part that holds for every array of 45 elements.")),
            ("p", "That gap between 9 and 21 is the slack a proof about every input gives away, "
                  "and the lab prints both numbers on every round rather than only the one that "
                  "flatters the algorithm. Note also that the pivot `24` is not the median of "
                  "`1 … 45`, which is `23`. It never had to be."),
            ("h3", "Why five, and what three costs"),
            ("p", "The group size `g` fixes both fractions: the median recursion is on `n/g` "
                  "elements, and the guaranteed discard is `(g+1)/(4g)`, so the survivor "
                  "fraction is `1 − (g+1)/(4g)`. At `g = 3` those are `1/3` and `2/3`, summing "
                  "to exactly one, and a recursion tree whose levels do not shrink costs `n` "
                  "at each of about `log n` levels. At `g = 5` they sum to `9/10` and the tree "
                  "is geometric. Three is not slightly worse; it is a different complexity "
                  "class."),
            ("p", "Larger groups keep the sum below one &mdash; seven gives `6/7` &mdash; while "
                  "raising the constant cost of sorting each group, so five is the smallest "
                  "odd size that works and is the one everybody uses. The lab lets you set all "
                  "three and prints the level sums for each, so the claim is checkable rather "
                  "than received."),
        ],
        "lab": ("sortkit", {
            "mode": "mom",
            "n": 45,
            "group": "5",
            "k": 23,
            "panel_title": "Choose the size, the group and the rank",
            "panel_intro": "The two fractions in the recurrence are computed from the group "
                           "size as exact rationals, and the level sums of the recursion tree "
                           "are evaluated as fractions too, so the comparison with one is a "
                           "comparison of integers.",
        }),
        "steps_title": "Working one round, then solving the recurrence",
        "steps_intro": "The pivot selection is mechanical. The part worth slowing down for is the level sums.",
        "steps": [
            ("Group, sort each group, and collect the medians",
             "Groups of five, in order, and sort each one by hand &mdash; five elements is a "
             "handful of comparisons and the constant is why the group size cannot grow much. "
             "Write the medians out as their own list."),
            ("Select the median of that list, recursively",
             "This is the same problem on a fifth of the data, which is the first recursive "
             "term. On 45 elements the list of medians has nine entries and its median is the "
             "pivot."),
            ("Partition, and compare the actual discard with the guarantee",
             "Count how many elements fell on each side. The lab prints the guarantee for that "
             "round beside the smaller side; the actual figure is normally far larger, and "
             "that difference is the price of a claim that covers every array rather than this "
             "one."),
            ("Write the recurrence and sum its levels",
             "`T(n) ≤ T(n/g) + T(1 − (g+1)/(4g))n + cn`. Add the two fractions. If the sum is "
             "below one, the level sums are geometric and total `n/(1 − sum)`; if it is one, "
             "every level costs `n` and there are about `log n` of them."),
            ("Compare the measured cost with quickselect's on the same array",
             "299 against 131 at 45 elements. Both are one input's cost. The claim that "
             "distinguishes the two algorithms is not in those numbers: it is that one of them "
             "holds for every array and the other holds in expectation."),
        ],
        "worked": {
            "title": "Forty-five elements, groups of five, one round by hand",
            "intro": [
                "The array is the lab's seeded shuffle of `1 … 45`, taken in order, nine groups "
                "of five. Each group is sorted and its median taken; the median of the nine "
                "medians is the pivot.",
            ],
            "lines": [
                " group   as they appear        sorted                 median",
                "   1     31 40 22 24 15        15 22 24 31 40           24",
                "   2     13 23 35 43 42        13 23 35 42 43           35",
                "   3     21 20 10 41 34        10 20 21 34 41           21",
                "   4     19 37  3 30 27         3 19 27 30 37           27",
                "   5      1 14  2 17 18         1  2 14 17 18           14",
                "   6     39 11 28 38 44        11 28 38 39 44           38",
                "   7      7 32  8  4 33         4  7  8 32 33            8",
                "   8      6 29  5 16 45         5  6 16 29 45           16",
                "   9      9 26 25 12 36         9 12 25 26 36           25",
                "",
                "medians          24 35 21 27 14 38 8 16 25",
                "sorted            8 14 16 21 24 25 27 35 38",
                "median of them                  24        ← the pivot",
                "",
                "partition around 24:   23 elements below, 21 above",
                "guaranteed for n = 45, g = 5:   9 on the thin side",
                "the true median of 1 … 45 is 23, so the pivot is NOT the median",
                "",
                "1/5 + 7/10 = 9/10 < 1     level sums at n = 45:  45, 40.5, 36.45, …",
                "                          total exactly 450 = 10n",
            ],
            "after": [
                "Check the guarantee against the round. Five of the nine medians are at most "
                "`24`, and each of their groups contributes three elements at most `24`; "
                "setting aside the group holding the pivot leaves four groups, so twelve "
                "elements are guaranteed below, and the lab's per-round figure of 9 is the "
                "same count with the partial-group allowance made. The round actually "
                "delivered 23. The guarantee is the number that survives being asked about "
                "every array.",
                "The level sums are the other half. `45, 40.5, 36.45, …` is a geometric "
                "sequence with ratio `9/10`, and `45/(1 − 9/10) = 450`. Switch the group size "
                "to three in the lab and the level sums become `45, 45, 45, …` &mdash; the "
                "column stops shrinking, and there is no total to print.",
                "For a faded rehearsal, set the group size to seven and predict two things "
                "before reading them: the two fractions, and whether the tree converges. The "
                "supplied first move is the discard formula `(g+1)/(4g)`, which at `g = 7` is "
                "`8/28 = 2/7`. Work out the survivor fraction and the sum, then say why seven "
                "is not used in practice even though its sum is smaller than five's.",
            ],
        },
        "quiz_title": "Guarantees, and the sum that decides",
        "quiz": [
            {"q": "In the worked round the pivot was `24` and the true median of `1 … 45` is `23`. What does that show?",
             "a": ["That the group medians were computed wrongly",
                   "Nothing is wrong: the pivot is only guaranteed to lie in the middle forty per cent, which is enough for the recurrence",
                   "That the group size should have been larger",
                   "That median of medians is approximate and can return the wrong order statistic"],
             "c": 1,
             "why": "The pivot is a partitioning device, not the answer; what matters is that "
                    "a guaranteed fraction is discarded. The algorithm still returns the exact "
                    "`k`-th smallest &mdash; the lab checks its result against the sorted "
                    "array at that rank on every run."},
            {"q": "Why are the groups of five rather than three?",
             "a": ["Three elements are too few to have a median",
                   "With groups of three the two fractions are `1/3` and `2/3`, which sum to exactly one, so every level of the recursion tree costs `n` and the total is `n log n`",
                   "The median of three is not well defined for even-sized arrays",
                   "Five is the smallest odd number greater than three"],
             "c": 1,
             "why": "The recursion tree only shrinks when the fractions sum to under one. The "
                    "lab computes both sums as exact rationals and prints "
                    "&ldquo;it does not converge&rdquo; for groups of three, where the level "
                    "sums stay at `n` forever."},
            {"q": "Median of medians spent 299 comparisons on the 45-element array where quickselect spent 131. Why use it?",
             "a": ["It should not be used; quickselect is better",
                   "It is linear on every input, where quickselect is linear in expectation &mdash; the extra constant buys a guarantee",
                   "299 is asymptotically smaller than 131",
                   "Quickselect cannot select from an array whose length is odd"],
             "c": 1,
             "why": "Both counts are one input each and neither is a bound. The difference "
                    "between the algorithms is in what can be claimed: no input makes median of "
                    "medians superlinear, whereas quickselect's bound is over the pivot draws "
                    "and a bad seed on this array costs more than sorting it."},
            {"q": "At 45 elements with groups of five the lab reports a per-round guarantee of 9, and the round discarded 21. What is the 9?",
             "a": ["A measurement of a different round",
                   "The number the counting argument proves for every array of this size; 21 is what this array happened to give",
                   "The number of groups",
                   "`3n/10` rounded down, which is 13"],
             "c": 1,
             "why": "It is `⌈(g+1)/2⌉(⌈⌈n/g⌉/2⌉ − 2)`, the exact form of the counting argument "
                    "with the two set-aside groups accounted for; `3n/10` is its asymptotic "
                    "shape, and at `n = 45` the exact count is 9 rather than 13. The gap "
                    "between 9 and 21 is the slack a claim about all inputs gives away."},
        ],
        "mistakes": [
            ("Believing the pivot is the true median",
             "It is the median of the group medians, which is a different element: `24` where "
             "the true median is `23` in the worked round. The algorithm does not need it to "
             "be the median &mdash; it needs a guaranteed fraction on each side, and that is "
               "all the proof uses."),
            ("Reaching for the master theorem",
             "`T(n) ≤ T(n/5) + T(7n/10) + cn` has two recursive terms with different fractions "
             "and no `af(n/b)` shape, so the master theorem does not apply to it. What solves "
             "it is the recursion tree: sum each level, notice the ratio, and sum the "
             "geometric series. Discrete Mathematics' &ldquo;Recursion Trees and Amortised "
             "Analysis&rdquo; is where that technique was proved."),
            ("Assuming a smaller group size is a small change",
             "Groups of three make the two fractions sum to exactly one, and the recursion "
             "tree stops shrinking: `n` per level, about `log n` levels, `Θ(n log n)` in "
             "total. That is the same class as sorting, so the entire point of the algorithm "
             "is lost. The lab prints the level sums for group sizes three, five and seven "
             "side by side."),
        ],
        "standard": ("Finish when you can defend the group size with the two fractions rather than with a convention.",
                     "You should be able to run one round of the pivot selection on paper, "
                     "state the discard guarantee and where the `− 2` comes from, solve the "
                     "two-term recurrence by its level sums, and say what changes at group "
                     "size three and why it is a change of class."),
        "note": ("Two lessons have now beaten sorting by asking for less. The last two ask what "
                 "cannot be beaten at all. &ldquo;Adversary Arguments&rdquo; proves lower "
                 "bounds for the maximum, for both ends at once and for the second largest, "
                 "and every one of them is met exactly by an algorithm you can run."),
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "adversary-arguments",
        "title": "Adversary Arguments",
        "module": "Selection, bounds and scale",
        "one_line": "Prove three lower bounds by answering comparisons to keep the most outcomes alive, then meet each one with an algorithm.",
        "summary": (
            "A lower bound cannot be measured, because a measurement is about one algorithm "
            "and a bound is about all of them. It is proved instead by an adversary who holds "
            "no array and answers each comparison so as to keep the largest number of "
            "outcomes possible. That argument gives `n − 1` comparisons for the maximum, "
            "`⌈3n/2⌉ − 2` for the minimum and maximum together, and `n + ⌈log₂ n⌉ − 2` for the "
            "second largest, and each of the three is met exactly."
        ),
        "key": [
            "the adversary holds no array; it answers to keep the most outcomes alive",
            "maximum                n − 1                every element but one must lose",
            "minimum and maximum    ⌈3n/2⌉ − 2           at n = 8:  10, met exactly",
            "second largest         n + ⌈log₂ n⌉ − 2     at n = 8:   9, met exactly",
            "and Discrete Mathematics' ⌈log₂ n!⌉ is the same kind of claim, for sorting",
        ],
        "key_label": "Three bounds, each proved against every algorithm and met by one",
        "concepts_intro": (
            "The hard idea is the quantifier. Everything else on this course measured one "
            "algorithm; this proves something about all of them at once."
        ),
        "concepts": [
            ("A lower bound is about every algorithm, so it cannot be measured",
             "Running an algorithm tells you what that algorithm did on that input. A lower "
             "bound says no algorithm can do better on its worst input, which quantifies over "
             "a set no lab can enumerate. The adversary supplies the quantifier: because it "
             "answers whatever it is asked, its argument covers every strategy, including "
             "ones nobody has written."),
            ("The adversary's rule is to keep the most candidates alive",
             "It never commits to an array. It keeps a set of arrays consistent with every "
             "answer it has given, and each new answer is chosen to leave the larger set. For "
             "the maximum, it answers so that exactly one element is eliminated per "
             "comparison: any algorithm stopping before `n − 1` comparisons has left two "
             "elements unbeaten, and the adversary can still name an array making either of "
             "them the maximum, so the answer was not determined."),
            ("A bound is tight only when an algorithm meets it",
             "The adversary gives a floor; an algorithm gives a ceiling; when they coincide "
             "the question is closed. All three bounds here are met. Pairing the elements "
             "before scanning finds both ends of eight keys in exactly 10 comparisons, and the "
             "tournament finds the second largest of eight in exactly 9 &mdash; and the lab "
             "verifies the second of those on every one of the 40 320 arrangements."),
        ],
        "read_title": "Three bounds, proved by the same manoeuvre",
        "read_intro": "How an adversary argument works, the three bounds it gives here, and the algorithms that meet them.",
        "body": [
            ("def", ("Adversary argument",
                     "An <strong>adversary argument</strong> proves a lower bound on the "
                     "number of comparisons any algorithm needs. The adversary answers each "
                     "comparison the algorithm makes, without fixing the input in advance, "
                     "subject only to consistency: there must always remain at least one "
                     "input agreeing with every answer given. If, after fewer than `B` "
                     "comparisons, two different answers are still consistent with everything "
                     "said, the algorithm cannot have determined the result, so `B` is a lower "
                     "bound.")),
            ("thm", ("Finding the maximum needs `n − 1` comparisons",
                     "Any comparison-based algorithm that reports the maximum of `n` elements "
                     "makes at least `n − 1` comparisons in the worst case.")),
            ("proof", ("Call an element unbeaten if it has not yet lost a comparison. Initially "
                       "all `n` are unbeaten. The algorithm can only report a maximum when "
                       "exactly one element is unbeaten: if two were, the adversary could "
                       "consistently make either of them the largest, so the reported answer "
                       "would not be determined.",
                       "The adversary answers every comparison between two unbeaten elements "
                       "arbitrarily but consistently, and every other comparison in whatever "
                       "way keeps its options open. Each comparison eliminates at most one "
                       "element from the unbeaten set, since only the loser leaves it.",
                       "Going from `n` unbeaten elements to one therefore takes at least "
                       "`n − 1` comparisons. A single scan makes exactly that many, so the "
                       "bound is tight.")),
            ("thm", ("Both ends together need `⌈3n/2⌉ − 2`",
                     "Finding the minimum and the maximum of `n` elements requires at least "
                     "`⌈3n/2⌉ − 2` comparisons in the worst case, and an algorithm achieves it.")),
            ("p", "The algorithm is the more instructive half. Pair the elements and compare "
                  "within each pair, which costs `⌊n/2⌋` comparisons and settles, for each "
                  "pair, which member can still be the minimum and which can still be the "
                  "maximum. Then find the minimum among the `⌈n/2⌉` losers and the maximum "
                  "among the winners, at `⌈n/2⌉ − 1` comparisons each. A pair therefore costs "
                  "three comparisons for two ends rather than four, and at `n = 8` the total "
                  "is `4 + 3 + 3 = 10` against the 14 of two independent scans."),
            ("thm", ("The second largest needs `n + ⌈log₂ n⌉ − 2`",
                     "Any algorithm reporting the second largest of `n` elements makes at "
                     "least `n + ⌈log₂ n⌉ − 2` comparisons in the worst case, and the "
                     "tournament meets it.")),
            ("p", "The second largest must have lost to the maximum, because it lost to "
                  "nobody else. So the algorithm has to find the maximum first, at `n − 1` "
                  "comparisons, and then find the largest among those the maximum beat. A "
                  "knockout tournament beats the fewest possible: the winner plays "
                  "`⌈log₂ n⌉` rounds, so only `⌈log₂ n⌉` elements ever lost to it, and picking "
                  "the best of those costs `⌈log₂ n⌉ − 1` more. At `n = 8` that is "
                  "`7 + 3 − 1 = 9`, which is the lab's measured count, and it never exceeds it "
                  "on any of the 40 320 arrangements the sweep runs."),
            ("p", "The misconception the tournament breaks is the natural one: scan the array "
                  "keeping the best two, which compares each new element with the second best "
                  "and sometimes with the best as well, and costs up to `2n − 3` &mdash; 13 at "
                  "`n = 8`, measured at 11 on the lab's array. The tournament's saving is "
                  "structural rather than clever: it remembers <em>who</em> lost to the "
                  "winner, so the candidate set is `⌈log₂ n⌉` instead of `n − 1`."),
            ("p", "One row of the lab's table is different in kind from every other figure on "
                  "this course. At sizes up to eight it runs the tournament on every "
                  "arrangement of `1 … n` &mdash; 40 320 of them at `n = 8` &mdash; and reports "
                  "the worst count found, whether any exceeded the bound, and whether any "
                  "returned the wrong element. None exceeded and none was wrong, and the worst "
                  "equals the bound. That is a claim about every input of that size, which is "
                  "as close to a quantifier as a measurement gets, and it is still not a claim "
                  "about every algorithm."),
            ("h3", "The bound this course cites and does not reprove"),
            ("p", "Discrete Mathematics' &ldquo;Searching and Sorting&rdquo; proves that "
                  "sorting `n` elements by comparisons needs at least `⌈log₂ n!⌉` of them, by "
                  "counting the leaves a decision tree must have. That is the same kind of "
                  "statement as the three above and it is used here as a thing to reduce to "
                  "rather than reproved: every panel on this course prints it beside a "
                  "measured count, and Geometric Algorithms will later reduce sorting to "
                  "convex hull in order to inherit it."),
        ],
        "lab": ("sortkit", {
            "mode": "adversary",
            "game": "max",
            "n": 8,
            "left": 1,
            "right": 2,
            "panel_title": "Choose the bound and play",
            "panel_intro": "The adversary holds no array. It answers each comparison so as to "
                           "leave the most possibilities open, and the bound that falls out is "
                           "a statement about every algorithm rather than about the one you "
                           "played.",
        }),
        "steps_title": "Proving a bound by playing against it",
        "steps_intro": "Take the adversary's side. The question is never what your algorithm does, but what it has not yet ruled out.",
        "steps": [
            ("Name the quantity the answer depends on",
             "For the maximum it is the number of elements that have not yet lost. For the "
             "second largest it is the number of elements that could still be second. The "
             "bound comes from how fast a single comparison can move that quantity, which for "
             "the maximum is by one."),
            ("Fix the adversary's answering rule and check it is consistent",
             "The rule must never contradict an earlier answer: there has to remain at least "
             "one array agreeing with everything said. An adversary that cheats proves "
             "nothing, and the lab's is consistent by construction &mdash; at any point it "
             "can name an array matching every answer it gave."),
            ("Count how many comparisons the algorithm needs to finish",
             "It can only stop when one candidate is left. Divide the distance by the most one "
             "comparison can cover, and that is the bound. Play the lab's game and watch the "
             "counter rise to `n − 1` however cleverly you choose your pairs."),
            ("Then find the algorithm that meets it",
             "A bound with no matching algorithm is a floor of unknown height. Pair-then-scan "
             "meets `⌈3n/2⌉ − 2`; the tournament meets `n + ⌈log₂ n⌉ − 2`. Run each and check "
             "the measured count against the bound on the panel."),
            ("Say which of your numbers is a measurement and which is a proof",
             "The count you ran up is a measurement of one game. The bound is a proof about "
             "every algorithm. The sweep over all arrangements is neither: it is a complete "
             "statement about one algorithm at one size, and the lab labels it as the one "
             "figure on the page that is not about a single input."),
        ],
        "worked": {
            "title": "Both ends of eight keys in ten comparisons",
            "intro": [
                "The array is the lab's seeded shuffle, `2 5 4 3 7 8 6 1`. The strategy is to "
                "pair first, so that one comparison per pair decides which member can still be "
                "the minimum and which can still be the maximum.",
            ],
            "lines": [
                "array        2  5  4  3  7  8  6  1",
                "",
                "step 1, pair and compare within each pair          4 comparisons",
                "   (2, 5)  →  low 2, high 5",
                "   (4, 3)  →  low 3, high 4",
                "   (7, 8)  →  low 7, high 8",
                "   (6, 1)  →  low 1, high 6",
                "",
                "step 2, minimum among the lows  2 3 7 1            3 comparisons",
                "   2 vs 3 → 2;   2 vs 7 → 2;   2 vs 1 → 1          minimum = 1",
                "",
                "step 3, maximum among the highs 5 4 8 6            3 comparisons",
                "   5 vs 4 → 5;   5 vs 8 → 8;   8 vs 6 → 8          maximum = 8",
                "",
                "total        4 + 3 + 3 = 10",
                "the bound    ⌈3 · 8/2⌉ − 2 = 10                    met exactly",
                "two scans    (n − 1) + (n − 1) = 14                4 comparisons wasted",
            ],
            "after": [
                "The saving is entirely in step one. Without it, every element is a candidate "
                "for both ends and each has to be tested against both running extremes. With "
                "it, one comparison per pair halves both candidate sets at once, so two "
                "elements cost three comparisons rather than four &mdash; `3n/2` rather than "
                "`2n`, and the `− 2` is the two extremes that need no final comparison.",
                "Now switch the lab to the second-largest game at the same size. The "
                "tournament costs 9, the bound is `8 + 3 − 2 = 9`, and keeping the best two in "
                "one scan costs 11 against a worst case of `2n − 3 = 13`. Only three elements "
                "ever lost to the winner, which is `⌈log₂ 8⌉`, and that is the whole reason "
                "the second largest is nearly free once the largest is known.",
                "For a faded rehearsal, play the maximum game at `n = 8` and try to finish in "
                "six comparisons. The supplied first move is the invariant to watch: the "
                "panel's unbeaten count starts at 8 and falls by at most one per comparison. "
                "Say, before you start, how many comparisons you will need, then verify that "
                "no ordering of your questions changes it.",
            ],
        },
        "quiz_title": "Bounds, and who they are about",
        "quiz": [
            {"q": "Finding the second largest of `n` elements: how many comparisons does the best algorithm need?",
             "a": ["About `2n`, since two running best values must be maintained",
                   "`n + ⌈log₂ n⌉ − 2`, because only the elements that lost to the winner can be second",
                   "`n − 1`, the same as the maximum",
                   "`⌈log₂ n!⌉`, the comparison sorting bound"],
             "c": 1,
             "why": "The second largest must have lost to the maximum and to nobody else, and a "
                    "knockout tournament leaves only `⌈log₂ n⌉` such elements. Keeping the best "
                    "two in one scan is the `2n − 3` answer: 13 at `n = 8`, against the "
                    "tournament's 9."},
            {"q": "Why can a lower bound not be established by running algorithms in the lab?",
             "a": ["Because the lab's counters are approximate",
                   "Because a measurement is about one algorithm on one input, and the bound quantifies over every algorithm",
                   "Because the lab cannot enumerate all `n!` inputs",
                   "It can, if every algorithm is run on every input"],
             "c": 1,
             "why": "The counters are exact and the lab does enumerate all 40 320 arrangements "
                    "at `n = 8`. What it cannot enumerate is the algorithms, which is why the "
                    "adversary argument exists: it answers whatever it is asked, so it covers "
                    "strategies nobody has written."},
            {"q": "The lab ran the tournament on all 40 320 arrangements of eight keys: the worst cost 9, none exceeded 9, none returned the wrong element. What has been established?",
             "a": ["That no algorithm can find the second largest of eight keys in fewer than 9 comparisons",
                   "That this algorithm never exceeds 9 at `n = 8` &mdash; a complete claim about every input of that size, and not a claim about other algorithms",
                   "That the bound is 9 for every `n`",
                   "Nothing, because eight is a small size"],
             "c": 1,
             "why": "The sweep quantifies over inputs, and that is genuinely more than any other "
                    "measurement on this course provides. The first answer is the adversary "
                    "argument's job, and it is proved rather than measured; the two halves "
                    "together are what make the bound tight."},
            {"q": "Two separate scans find both ends of eight keys in 14 comparisons; pairing first does it in 10. Where does the saving come from?",
             "a": ["The pairs end up sorted, which helps the later scans",
                   "The first comparison of each pair settles which member can still be the minimum and which can still be the maximum, so a pair costs three comparisons for two ends rather than four",
                   "Fewer elements are examined overall",
                   "The minimum is found for free once the maximum is known"],
             "c": 1,
             "why": "Every element is still examined; what changes is that one comparison "
                    "removes each element from one of the two candidate sets. Four pairs cost "
                    "`4 + 3 + 3 = 10` against `7 + 7 = 14`, and the pattern generalises to "
                    "`⌈3n/2⌉ − 2`."},
        ],
        "mistakes": [
            ("Assuming the second largest costs about `2n`",
             "That is the cost of the obvious algorithm, which keeps the best two as it scans "
             "and compares each new element with the second best. `2n − 3` is 13 at eight keys "
             "and the tournament pays 9. The difference is that the tournament remembers which "
             "elements lost to the winner, leaving only `⌈log₂ n⌉` candidates instead of "
             "`n − 1`."),
            ("Trying to prove a lower bound by testing algorithms",
             "No number of algorithms establishes that a better one does not exist. The "
             "adversary argument is the technique that quantifies over strategies, and it does "
             "it by answering rather than by enumerating. A measurement can refute a claimed "
             "upper bound; nothing measured can establish a lower one."),
            ("Suspecting the adversary of cheating",
             "It never contradicts itself: at every point there is at least one array "
             "consistent with all its answers, and at the end it can produce one. That is "
             "exactly why the bound is real &mdash; the algorithm was playing against a "
             "legitimate input all along, it just was not chosen yet. An adversary allowed to "
             "contradict an earlier answer would prove nothing at all."),
        ],
        "standard": ("Finish when you can state an adversary argument and then meet its bound with an algorithm.",
                     "You should be able to give the unbeaten-set argument for `n − 1`, "
                     "describe the pairing strategy and count it to `⌈3n/2⌉ − 2`, explain why "
                     "only the winner's losers can be second, and distinguish a sweep over all "
                     "inputs from a claim about all algorithms."),
        "note": ("“k-Way Merging and Sorting in Practice” changes the cost model. "
                 "Everything so far counted "
                 "comparisons, because a comparison was the only operation the model charged "
                 "for. When the data does not fit in memory, the unit becomes a pass over the "
                 "data, and an algorithm making more comparisons can be the right one, which "
                 "is exactly what happens there."),
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "k-way-merge-and-external-sorting",
        "title": "k-Way Merging and Sorting in Practice",
        "module": "Selection, bounds and scale",
        "one_line": "Merge k runs through a heap, count the passes a disk sort needs, and choose an insertion-sort cutoff from a measured crossover.",
        "summary": (
            "A heap of `k` run heads merges `k` sorted runs in one pass over the data. It "
            "makes more comparisons than merging the runs two at a time, not fewer &mdash; a "
            "sift-down examines both children &mdash; and what it buys is the pass count: one "
            "instead of `k − 1`. When the data lives on disk, a pass is the cost, which gives "
            "the external sort's pass formula; and the same runs-then-merges shape with "
            "insertion sort below a cutoff is what Timsort is."
        ),
        "key": [
            "heap of k run heads: one extract and one insert per item, one pass over the data",
            "64 items in 8 runs:  heap 302 comparisons, pairwise 180  —  1 pass against 7",
            "n log₂ k = 192 is the order; a sift down compares both children, so about 2×",
            "N records, M in memory, B to a block:  1 + ⌈log_(M/B)(N/M)⌉ passes",
            "10⁹ records, 10⁶ in memory, blocks of 4:  fan-in 250 000, 1000 runs, 2 passes",
            "the same records with blocks of 500:  fan-in 2, and 21 passes",
        ],
        "key_label": "One pass through a heap, and the pass count on disk",
        "concepts_intro": (
            "The hard idea is that the cost model changes, and the algorithm that wins under "
            "the new one loses under the old."
        ),
        "concepts": [
            ("One pass through a heap, or k − 1 passes over the data",
             "Load the head of each of the `k` runs into a min-heap, then repeatedly extract "
             "the smallest and push the next item from the run it came from. Every item is "
             "popped once, so the whole merge is a single sequential sweep of all `n` items. "
             "Merging two runs at a time instead needs `k − 1` rounds, and every round rereads "
             "the whole accumulated prefix: on eight runs of eight that is seven passes over "
             "the data against one."),
            ("The heap makes more comparisons, not fewer",
             "This is the figure that surprises. On eight runs of eight, the heap merge makes "
             "302 comparisons and the pairwise merges make 180. A two-way merge compares once "
             "per item taken; a sift-down compares the moved key with both children at every "
             "level, so the heap's count is about `2n log₂ k` rather than `n log₂ k`. "
             "`n log₂ k` here is 192 and the measured 302 sits between that and 384, exactly "
             "as the extra child comparison predicts."),
            ("When the unit is a pass, a comparison count is not the cost",
             "Sorting `N` records with `M` fitting in memory means writing `N/M` sorted runs "
             "and then merging them with a fan-in of `M/B`, where `B` is the block size, which "
             "gives `1 + ⌈log_(M/B)(N/M)⌉ passes`. A billion records with a million in memory "
             "and four to a block takes two passes. The same billion with blocks of five "
             "hundred leaves a fan-in of two and takes twenty-one. Nothing about the "
             "comparison count changed."),
        ],
        "read_title": "One heap against k − 1 passes, and what a pass costs on disk",
        "read_intro": "The k-way merge and its real comparison count, the external sort's pass formula, and the cutoff that makes a hybrid.",
        "body": [
            ("def", ("k-way merge",
                     "To <strong>merge</strong> `k` sorted runs holding `n` items in total: "
                     "place the first item of each run into a min-heap of size `k`, tagged "
                     "with the run it came from. Repeatedly extract the minimum, append it to "
                     "the output, and insert the next item of that run. Each item is inserted "
                     "once and extracted once.")),
            ("p", "The heap holds `k` items, not `n`, so the extra memory is the fan-in rather "
                  "than the data. Each extract costs a sift-down of depth `⌊log₂ k⌋`, so the "
                  "order of the comparison count is `n log k` &mdash; but the constant "
                  "deserves to be measured rather than assumed, and the lab measures it."),
            ("example", ("Eight runs of eight, both ways",
                         "64 items. Through one heap: 302 comparisons, 64 pops, one pass over "
                         "the data. Merging two runs at a time: 180 comparisons and seven "
                         "passes, because each of the `k − 1` rounds walks the whole "
                         "accumulated prefix again. Both produce the same 64 items in the same "
                         "order, and the lab checks that they agree rather than assuming it.")),
            ("p", "So in the comparison model the heap loses. `n log₂ k = 192` at these sizes "
                  "and the heap spends 302, which is between `n log₂ k` and `2n log₂ k = 384` "
                  "&mdash; the extra factor being the comparison between the two children that "
                  "a sift-down makes at every level before comparing with the parent. "
                  "Heapsort paid the same factor in exactly the same place."),
            ("h3", "Why anyone uses the heap anyway"),
            ("def", ("External merge sort",
                     "When `N` records do not fit in the `M` of memory available, sort in two "
                     "phases. <strong>Run formation</strong>: read `M` records at a time, sort "
                     "them in memory, write them back as a sorted run, giving `N/M` runs. "
                     "<strong>Merging</strong>: repeatedly merge runs `F` at a time, where the "
                     "<strong>fan-in</strong> `F` is `M/B` for a block size of `B`, since each "
                     "open run needs one block of buffer.")),
            ("math", [
                "runs      = N/M",
                "fan-in    F = M/B",
                "passes    = 1 + ⌈log_F(N/M)⌉        one to make the runs, then the merges",
                "",
                "N = 10⁹, M = 10⁶, B = 4      F = 250 000, runs = 1000     2 passes",
                "N = 10⁹, M = 10³, B = 4      F = 250, runs = 10⁶          4 passes",
                "N = 10⁹, M = 10³, B = 500    F = 2,   runs = 10⁶         21 passes",
                "N = 10⁷, M = 10⁷             everything fits              1 pass, 0 merges",
            ]),
            ("p", "Read the third line against the second. The data is the same size, the "
                  "algorithm is the same algorithm, and the pass count went from four to "
                  "twenty-one because the fan-in &mdash; the base of the logarithm &mdash; "
                  "fell from 250 to 2. A pass over a billion records is the expensive thing "
                  "here, and the comparison count does not appear in the formula at all."),
            ("p", "That is why the heap wins on disk and loses in the lab's comparison column: "
                  "it makes `k` runs into one in a single pass, so the number of passes is the "
                  "logarithm of the run count in base `F` rather than in base two. System "
                  "Design's &ldquo;Sequential versus Random I/O&rdquo; prices exactly this "
                  "count &mdash; it is the same number of sequential passes over the same "
                  "data &mdash; and nothing on this page depends on that pricing."),
            ("h3", "The cutoff, and the shape of a real library sort"),
            ("p", "Merging singleton runs is wasteful: at the bottom of any merge sort the "
                  "runs are tiny and insertion sort, which is `Θ(m²)` but with a small "
                  "constant and no allocation, beats it there. A hybrid insertion-sorts blocks "
                  "of size `c` and then merges them. On 64 shuffled keys the lab measures 594 "
                  "comparisons at a cutoff of 1, 500 at 4, 448 at 11 and 527 at 20: the "
                  "cheapest cutoff is strictly inside the range, which is what a crossover "
                  "looks like."),
            ("p", "Eleven is a measurement on one array, not a constant of nature. What "
                  "generalises is the shape &mdash; form runs, insertion-sort below a cutoff, "
                  "merge the runs &mdash; and that shape is Timsort's, which is the sort in "
                  "the standard libraries of several languages. Timsort finds runs already "
                  "present in the data rather than cutting fixed blocks, and merges them under "
                  "a stack policy with galloping; neither of those is covered here."),
            ("p", "Three figures on this page are of three different kinds, and the panel keeps "
                  "them apart. 302 and 180 are comparison counts measured by running two "
                  "merges on the same runs. `1 + ⌈log_F(N/M)⌉` is arithmetic: a count of passes "
                  "over records, computed rather than measured, and refused outright when "
                  "memory is too small to hold two blocks. And 11 is the low point of a curve "
                  "sampled at twenty cutoffs on one array."),
        ],
        "lab": ("heap", {
            "mode": "kway",
            "preset": "eight-runs",
            "panel_title": "Merge the runs both ways, then choose a cutoff",
            "panel_intro": "A heap of `k` run heads does one extract and one insert per item, "
                           "so `k` runs merge in one pass. Merging them two at a time makes "
                           "FEWER comparisons and rereads the accumulated prefix on every one "
                           "of `k − 1` passes. The pass count for `N` items with `M` of memory "
                           "and blocks of `B` is counted here, not computed from a logarithm.",
        }),
        "steps_title": "Sizing a sort that does not fit in memory",
        "steps_intro": "The first question is not which algorithm. It is what the cost model charges for.",
        "steps": [
            ("Decide what the unit is",
             "In memory, a comparison. On disk, a pass over the data. The two rank the same two "
             "algorithms in opposite orders here, which is why naming the unit first is not "
             "pedantry: the heap merge makes 302 comparisons against 180 and is still the one "
             "to use."),
            ("Merge the runs both ways and count",
             "Set `k` and the run lengths and read the two comparison columns, then the pass "
             "column. The heap's advantage is entirely in the last of those, and the lab "
             "checks that both methods produce the same merged sequence."),
            ("Compute the pass count from `N`, `M` and `B`",
             "Runs are `N/M`, the fan-in is `M/B`, and the passes are `1 + ⌈log_F(N/M)⌉`. Do it "
             "for two block sizes before choosing one; the block size enters only through the "
             "fan-in, and it is the base of a logarithm, which is where large changes come "
             "from."),
            ("Check that the memory can hold two blocks at all",
             "If `M/B` is below two there is no merge to perform, and the lab refuses rather "
             "than returning a number. A formula that keeps producing pass counts for a "
             "configuration that cannot run is worse than an error."),
            ("Find the cutoff by measuring, and report it as a measurement",
             "Sweep the cutoff and read the total. The best value on the lab's 64-key array is "
             "11; on another array it will be another number. Quote the shape as general and "
             "the number as local."),
        ],
        "worked": {
            "title": "Eight runs of eight, and a billion records on disk",
            "intro": [
                "The runs are eight interleaved arithmetic sequences covering `1 … 64`, so "
                "every run is sorted and no run dominates another. The two merges below are "
                "run on the same eight runs and produce the same 64 items.",
            ],
            "lines": [
                "runs      8 runs of 8, 64 items in all",
                "",
                "  method                     comparisons   passes over the data",
                "  one heap of 8 run heads         302             1",
                "  pairwise, two runs at a time    180             7   (= k − 1)",
                "",
                "  n log₂ k  = 64 × 3 = 192        the order of the heap merge",
                "  2n log₂ k = 384                 a sift down compares both children",
                "  measured  302                   between the two, as that predicts",
                "",
                "ON DISK,  passes = 1 + ⌈log_(M/B)(N/M)⌉",
                "",
                "  N              M          B      fan-in     runs      passes",
                "  1 000 000 000  1 000 000  4      250 000    1 000        2",
                "  1 000 000 000  1 000      4      250        1 000 000    4",
                "  1 000 000 000  1 000      500    2          1 000 000   21",
                "     10 000 000  10 000 000 4      2 500 000  1            1",
                "",
                "THE CUTOFF, 64 shuffled keys, insertion sort below c then merge",
                "  c =  1   594          c =  4   500          c = 11   448",
                "  c = 20   527          cheapest at c = 11, strictly inside the range",
            ],
            "after": [
                "The first table is the whole lesson in two rows. The heap loses the "
                "comparison column by 122 and wins the pass column by six, and which of those "
                "two facts is the cost depends on where the data lives. In memory the pairwise "
                "merge is the better choice; on disk seven passes over a billion records is "
                "not a choice at all.",
                "The second table's third row is the one to keep. Same data, same memory, same "
                "algorithm, and five times the passes, because a block size of 500 leaves room "
                "for only two buffers and the fan-in is the base of the logarithm. The last "
                "row is the degenerate case worth checking a formula against: data that fits "
                "takes one pass and no merges at all.",
                "For a faded rehearsal, work out the pass count for a hundred million records "
                "with ten thousand in memory and blocks of twenty. The supplied first move is "
                "the fan-in: `M/B = 500`. Compute the run count, then the logarithm, then the "
                "passes &mdash; and then say what block size would bring it down by one, and "
                "whether that is a change you could actually make.",
            ],
        },
        "quiz_title": "Comparisons, passes and cutoffs",
        "quiz": [
            {"q": "Merging eight sorted runs pairwise made 180 comparisons where one heap made 302. Why is the heap used for external sorting?",
             "a": ["Because the heap is faster in comparisons once `k` is large",
                   "Because the pairwise merge makes `k − 1 = 7` passes over the data, and on disk a pass is the cost",
                   "Because the heap needs less memory than a pairwise merge",
                   "Because the pairwise merge is not stable"],
             "c": 1,
             "why": "The comparison count is genuinely worse for the heap and stays worse as "
                    "`k` grows, since a sift-down examines both children. What the heap buys is "
                    "one sequential sweep instead of `k − 1`, which is the quantity the "
                    "external sort's pass formula counts."},
            {"q": "A billion records, a million fitting in memory, four records to a block. How many passes?",
             "a": ["1", "2", "1 000", "21"],
             "c": 1,
             "why": "The runs are `N/M = 1000` and the fan-in is `M/B = 250 000`, so one merge "
                    "pass suffices: `1 + ⌈log₂₅₀₀₀₀ 1000⌉ = 1 + 1 = 2`. One pass writes the "
                    "runs and one merges them all at once."},
            {"q": "The same billion records with a thousand in memory take four passes at a block size of four and twenty-one at a block size of five hundred. What changed?",
             "a": ["The data got larger",
                   "The fan-in `M/B` fell from 250 to 2, and the fan-in is the base of the logarithm",
                   "The runs got shorter",
                   "The heap became too large to hold"],
             "c": 1,
             "why": "`N` and `M` are identical in both rows, so the run count is a million "
                    "either way. Larger blocks mean fewer of them fit in memory, and with room "
                    "for only two buffers the merge is binary: `log₂` of a million is twenty, "
                    "plus the run-forming pass."},
            {"q": "The cheapest cutoff for the hybrid on 64 keys was 11, giving 448 comparisons against 594 at a cutoff of 1. What kind of figure is 11?",
             "a": ["A proved optimum for merge-then-insertion hybrids",
                   "A measured crossover on this array: the shape generalises, the number does not",
                   "The block size the machine happens to use",
                   "`log₂ 64` rounded up"],
             "c": 1,
             "why": "It is the low point of a curve sampled at twenty cutoffs on one array of "
                    "64 keys, and another array gives another number. What does generalise is "
                    "that the curve has an interior minimum at all, because insertion sort wins "
                    "on small blocks and loses on large ones."},
        ],
        "mistakes": [
            ("Expecting the heap merge to make fewer comparisons",
             "It makes more: 302 against 180 on eight runs of eight, and the gap grows with "
             "`k`. A two-way merge compares once per item taken, while a sift-down compares "
             "the two children with each other before comparing the winner with the parent. "
             "The heap's case rests entirely on the pass count, and saying so out loud is what "
             "keeps the argument honest."),
            ("Reading `n log k` as a comparison count you can quote",
             "It is the order, and the constant is about two for a binary heap. At 64 items in "
             "eight runs, `n log₂ k` is 192 and the measured count is 302. The lesson prints "
             "both because the gap is not noise: it is the second child comparison, the same "
             "constant heapsort paid."),
            ("Treating the pass formula as a comparison count",
             "`1 + ⌈log_(M/B)(N/M)⌉` counts passes over records, and nothing in it mentions "
             "comparisons. That is the point of this lesson: the cost model "
             "changed, and an algorithm that is worse under the old unit is the right one "
             "under the new."),
        ],
        "standard": ("Finish when you can say which unit a sort is being charged in, and choose accordingly.",
                     "You should be able to merge `k` runs through a heap by hand, explain why "
                     "its comparison count is about twice `n log₂ k`, compute the pass count "
                     "for given `N`, `M` and `B` and say what a change of block size does to "
                     "it, and report a measured cutoff as the local number it is."),
        "note": ("That closes the course. It began with four promises that no complexity class "
                 "supplies, worked through a randomised expectation that is exact and holds on "
                 "every input, left the comparison model twice, found one order statistic "
                 "without sorting, proved three bounds against every algorithm, and ended by "
                 "changing the unit the cost is charged in. The habit worth keeping is the one "
                 "every panel enforced: print the measured count and the proved bound side by "
                 "side, and say which of the two is a claim about all inputs."),
    },
]
