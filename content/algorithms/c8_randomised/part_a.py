"""Randomised Algorithms, lessons 01-07 - sampling, the cost as a distribution,
and what linearity of expectation does not assume."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "uniform-sampling-and-the-shuffle-that-is-not",
        "title": "Uniform Sampling, and the Shuffle That Is Not",
        "module": "Randomness as a resource",
        "one_line": "Enumerate every tape of two shuffles, and refute the plausible one with a divisibility argument that needs no sample at all.",
        "summary": (
            "A shuffle that looks right and is wrong is the cleanest introduction to this "
            "course, because the distribution it produces is small enough to write down "
            "completely. The naive swap on four items has 256 equally likely runs and 24 "
            "possible answers, and 24 does not divide 256. That single remainder refutes "
            "uniformity before any run happens, and the enumeration then shows exactly how "
            "far off it is."
        ),
        "key": [
            "a TAPE is one complete run: the sequence of draws the algorithm made",
            "Fisher–Yates draws j in 0..i going down       n! tapes, one per permutation",
            "the naive swap draws j in 0..n−1 every time   nⁿ tapes, n! permutations",
            "n = 4:  256 tapes, 24 permutations, 256 = 24·10 + 16",
            "so some permutation gets more tapes than another, whatever a sample shows",
            "total variation from uniform: 25/384, exactly",
        ],
        "key_label": "Two shuffles, and the counting argument that separates them",
        "concepts_intro": (
            "One hard idea: a run is a tape, and the distribution is over tapes. The other "
            "two are what that buys &mdash; a proof of uniformity for one shuffle and a "
            "refutation of it for the other."
        ),
        "concepts": [
            ("A run is a tape, and the tapes are what you count",
             "Fix the algorithm and fix the input, and the only thing that can still vary is "
             "the sequence of random draws it makes. Call that sequence a <strong>tape</strong>. "
             "Every draw is uniform and independent, so every tape of the same length is equally "
             "likely, and the probability of an outcome is the number of tapes producing it "
             "divided by the number of tapes there are. That reduces a probability question to a "
             "counting question, and the lab answers it by listing all of them: 256 tapes at "
             "`n = 4` for the naive swap, 24 for Fisher&ndash;Yates."),
            ("Fisher–Yates is uniform because the map is a bijection",
             "Fisher&ndash;Yates draws `j` in `0..i` at step `i`, counting down, so a tape is one "
             "choice out of `n`, then one out of `n − 1`, and so on: `n!` tapes in all. Each "
             "produces a different permutation and there are `n!` permutations, so the "
             "correspondence is one to one and every permutation has probability exactly `1/n!`. "
             "The lab prints `1/24` in every row at `n = 4` and a total variation distance from "
             "uniform of `0`."),
            ("Divisibility refutes the other one without a single run",
             "The naive swap draws `j` in `0..n − 1` at every step, so it has `nⁿ` tapes. If it "
             "were uniform, each of the `n!` permutations would come from exactly `nⁿ/n!` tapes "
             "&mdash; and that has to be a whole number. At `n = 4` it is `256/24`, which is `10` "
             "with `16` left over. There is no arrangement of 256 tapes into 24 equal piles, so "
             "the shuffle is not uniform, and nothing about that argument mentions a sample."),
        ],
        "read_title": "Every tape, and the remainder that settles it",
        "read_intro": "Two shuffles that differ by one character, a proof for one, a refutation of the other, and a sample that can establish neither.",
        "body": [
            ("def", ("A tape, and the distribution over tapes",
                     "A <strong>tape</strong> for a randomised algorithm on a fixed input is the "
                     "sequence of values its random draws returned. If every draw is uniform over "
                     "`k` values and independent of the others, then each tape of `t` draws has "
                     "probability `1/kᵗ`, and the probability that the algorithm produces a given "
                     "output is the number of tapes producing it over the number of tapes there "
                     "are. Both halves are integers, so the probability is a fraction.")),
            ("p", "This is the whole of the lab's method, and it is what lets a page print "
                  "probabilities rather than estimates. It only works while the tapes can be "
                  "listed &mdash; `3125` of them at `n = 5`, `46656` at `n = 6` &mdash; which is "
                  "why the panel refuses above `n = 6` for the naive swap and above `n = 7` for "
                  "Fisher&ndash;Yates. Those are different limits because the two shuffles have "
                  "different numbers of tapes, and the refusal says which."),
            ("def", ("The two shuffles",
                     "Both start from the identity and walk the array once. "
                     "<strong>Fisher&ndash;Yates</strong>, going down from `i = n − 1`, draws `j` "
                     "uniformly from `0..i` and swaps positions `i` and `j`. The "
                     "<strong>naive swap</strong>, going up from `i = 0`, draws `j` uniformly from "
                     "`0..n − 1` &mdash; the whole array, every time &mdash; and swaps positions "
                     "`i` and `j`. The second is the one people write from memory, and it is the "
                     "one that is wrong.")),
            ("thm", ("Fisher–Yates produces every permutation with probability 1/n!",
                     "The map from tapes to permutations is a bijection, so each of the `n!` "
                     "permutations arises from exactly one of the `n!` equally likely tapes.")),
            ("proof", ("Injective. Run two different tapes. Let `i` be the largest index at which "
                       "they differ, and consider the state just before step `i`, which is the "
                       "same for both because every earlier step agreed. Step `i` places the "
                       "element then at position `j` into position `i`, and positions `0..i` still "
                       "hold distinct elements, so two different `j` put different elements at "
                       "position `i`. Nothing after step `i` touches position `i`, so the two "
                       "outputs differ.",
                       "Surjective, and therefore bijective, by counting: there are `n!` tapes and "
                       "`n!` permutations, and an injection between two finite sets of the same "
                       "size is a bijection. Every permutation therefore has exactly one tape, and "
                       "every tape has probability `1/n!`.")),
            ("p", "That proof is the reason the lab's Fisher&ndash;Yates column reads `1/24` in "
                  "all 24 rows and the total variation distance is `0` exactly rather than a small "
                  "number. The measured column beside it still wanders &mdash; 120 seeds at "
                  "`n = 4` produced 23 of the 24 permutations, and one of them never appeared. "
                  "That is what a sample from a uniform distribution looks like."),
            ("thm", ("The naive swap cannot be uniform for any n ≥ 3",
                     "The naive swap has `nⁿ` equally likely tapes and `n!` possible outputs. If "
                     "it were uniform, `n!` would divide `nⁿ`. It does not for any `n ≥ 3`, so it "
                     "is not uniform.")),
            ("proof", ("Suppose the shuffle were uniform. Every tape is equally likely and produces "
                       "exactly one permutation, so the `nⁿ` tapes are partitioned by the "
                       "permutation they produce, and uniformity says every part has the same size "
                       "`s`. Then `n! · s = nⁿ`, so `n!` divides `nⁿ`.",
                       "It does not. Take any prime `p` with `n/2 &lt; p &lt; n`, which exists for "
                       "`n ≥ 3` by Bertrand's postulate. Then `p` divides `n!`, since `p ≤ n`. But "
                       "`p &lt; n &lt; 2p`, so `n` is not a multiple of `p`, and `p` does not divide `nⁿ` "
                       "either. A divisor of `n!` that is not a divisor of `nⁿ` is a contradiction, "
                       "so no such `s` exists.")),
            ("p", "The lab does not take Bertrand's postulate on trust and it does not need to: it "
                  "computes `nⁿ` and `n!` as arbitrary-precision integers and prints the remainder "
                  "for the `n` on screen. The slider reaches `3`, `4` and `5`, where the remainders "
                  "are `3`, `16` and `5`; the repository's arithmetic check runs the same function "
                  "as far as `n = 7`, where they come out `576` and `2023`. Any one of those is a "
                  "complete refutation for that `n`, and none of them is a measurement."),
            ("h3", "What the enumeration adds once uniformity is already refuted"),
            ("p", "The divisibility argument says the shuffle is not uniform. It does not say how "
                  "far off it is, which permutation is favoured, or whether the bias matters. For "
                  "that the lab enumerates. At `n = 4` the most likely permutation is `1032` with "
                  "15 of the 256 tapes, probability `15/256`; the least likely has 8 tapes, "
                  "probability `1/32`, and two permutations are tied at that value. The spread of "
                  "tape counts is `8, 9, 10, 11, 14, 15` &mdash; the favoured outcome is almost "
                  "twice as likely as the neglected one."),
            ("p", "The single number for that is the <strong>total variation distance</strong> from "
                  "uniform: half the sum of `|p(σ) − 1/n!|` over all `n!` permutations. At `n = 4` "
                  "it is `25/384`, exactly, and it is `0` for Fisher&ndash;Yates. It is the largest "
                  "amount by which the two distributions can disagree about the probability of any "
                  "event, so it is the right single summary of how wrong the shuffle is."),
            ("h3", "More swaps do not wash the bias out"),
            ("p", "The intuition that a longer shuffle mixes better predicts that the bias shrinks "
                  "with `n`. It grows. The total variation distance is `1/18` at `n = 3`, `25/384` "
                  "at `n = 4`, and `3157/37500` at `n = 5` &mdash; about `0.056`, `0.065` and "
                  "`0.084`. Move the slider and watch it climb. The extra swaps are extra "
                  "opportunities for the same asymmetry rather than a correction of it."),
            ("p", "And the measurement becomes less useful as `n` grows, in the other direction. At "
                  "`n = 4`, 120 seeds cover 23 of the 24 permutations and the counts are already "
                  "too noisy to rank; at `n = 5` they cover 80 of the 120 and forty permutations "
                  "have no evidence at all. A sample large enough to detect a total variation "
                  "distance of `0.084` across 120 outcomes is much larger than a lesson can run in "
                  "a browser, and this is the general shape of the problem: refuting uniformity by "
                  "sampling is expensive, and refuting it by counting costs one division."),
        ],
        "lab": ("random", {"mode": "shuffle", "preset": "naive4"}),
        "steps_title": "Reading a distribution you can see all of",
        "steps_intro": "Do the arithmetic before the experiment. The experiment is the part that cannot settle it.",
        "steps": [
            ("Count the tapes before you count anything else",
             "How many independent draws does the algorithm make, and how many values can each "
             "take? The product is the number of tapes, and every probability on the page is a "
             "count of tapes over that number. Get it wrong and every fraction after it is wrong "
             "by the same factor."),
            ("Divide, and look at the remainder",
             "Number of tapes over number of outcomes. If the division is not exact, uniformity is "
             "already refuted and nothing else on the page can rescue it. If it is exact, you have "
             "learned nothing either way &mdash; which is worth knowing, because the counting "
             "argument is one-directional."),
            ("Read the exact column and the measured column as different things",
             "The exact column is the enumeration and will not move when the seed slider does. The "
             "measured column is a sample and will. If a claim you are about to make changes when "
             "you move the seeds, it was a claim about the sample."),
            ("Change n before generalising",
             "The bias of the naive swap is not a quirk of one size. Run `n = 3`, `n = 4` and "
             "`n = 5` and watch the total variation distance grow rather than shrink; the "
             "direction of that movement is the thing most readers guess wrong, and it takes two "
             "slider positions to settle."),
        ],
        "worked": {
            "title": "All 27 tapes of the naive swap at n = 3",
            "intro": [
                "Three items, three draws, three choices each: 27 tapes, and six permutations to "
                "share them between. 27 divided by 6 is 4 with 3 left over, so the shuffle is "
                "already refuted. Here is what the enumeration finds.",
            ],
            "lines": [
                "permutation   tapes  the tapes themselves          probability",
                "  012           4    012  021  102  210               4/27",
                "  021           5    011  022  101  120  200          5/27",
                "  102           5    002  112  121  201  220          5/27",
                "  120           5    001  020  111  122  202          5/27",
                "  201           4    000  110  211  222               4/27",
                "  210           4    010  100  212  221               4/27",
                "                --                                    ----",
                "               27                                     27/27",
                "",
                "three permutations at 5/27 and three at 4/27",
                "total variation from uniform = 1/18",
                "Fisher-Yates on the same three items: 6 tapes, one each, 1/6",
            ],
            "after": [
                "The split is three and three, not four and two: three permutations get five tapes "
                "and three get four, and `3·5 + 3·4 = 27`. Any other split of 27 into six parts "
                "with two distinct sizes would have to add to 27 as well, which is the only "
                "arithmetic check this table needs and the one worth doing before trusting any "
                "table like it.",
                "Notice what the bias is not. It is not that one item is stuck at the front, and "
                "it is not visible in the first few draws. `012`, the identity, is one of the "
                "<em>less</em> likely outcomes. A reader looking for a pattern in the output will "
                "not find one; the asymmetry lives in the tape counts, and only the enumeration "
                "sees it.",
                "For a faded rehearsal, predict the Fisher&ndash;Yates row before switching the "
                "lab over. The supplied first move is this: Fisher&ndash;Yates at `n = 3` makes "
                "two draws, one from `{0, 1, 2}` and one from `{0, 1}`, so it has six tapes. Say "
                "what each permutation's probability must be and what the total variation distance "
                "has to be, then switch and check &mdash; and then say why the same argument gives "
                "nothing at all about the naive swap at `n = 2`.",
            ],
        },
        "quiz_title": "Tapes, counting, and what a sample settles",
        "quiz": [
            {"q": "The lab reports that the naive swap at `n = 4` is not uniform. Which statement is established, and by what?",
             "a": ["Not uniform, established by the 120-seed measured column being uneven",
                   "Not uniform, established by 24 not dividing 256",
                   "Not uniform on this run only; another seed might come out uniform",
                   "Nothing is established, because 256 tapes is too small a sample"],
             "c": 1,
             "why": "The counting argument is a proof and needs no run: if the shuffle were "
                    "uniform the 256 equally likely tapes would split into 24 equal piles, and 256 "
                    "leaves 16 over. The measured column is uneven for a uniform shuffle too "
                    "&mdash; Fisher–Yates over 120 seeds reaches only 23 of the 24 permutations "
                    "&mdash; so unevenness in a sample establishes nothing either way."},
            {"q": "For which `n` does the divisibility argument refute the naive swap?",
             "a": ["Only when `n` is not a prime",
                   "Only for the values the lab happens to offer",
                   "Every `n ≥ 3`",
                   "Only when `n` is even, where `nⁿ` has too many factors of two"],
             "c": 2,
             "why": "There is always a prime `p` with `n/2 < p < n` for `n ≥ 3`, and such a `p` "
                    "divides `n!` but not `nⁿ`, since `p` does not divide `n`. The lab prints the "
                    "remainder for the `n` on screen — 3, 16, 5, 576 and 2023 at `n = 3` to "
                    "`n = 7` — and every one of them is nonzero."},
            {"q": "The total variation distance from uniform reads `1/18`, `25/384` and `3157/37500` at `n = 3`, `4` and `5`. What does that sequence say?",
             "a": ["The bias grows with `n`, so more swaps do not fix it",
                   "The bias shrinks with `n`, as more swaps mix better",
                   "Nothing: the three numbers are measurements on three different seeds",
                   "The bias is constant and the fractions are three ways of writing one number"],
             "c": 0,
             "why": "As decimals those are about 0.056, 0.065 and 0.084, so the distance from "
                    "uniform increases. All three are exact enumerations rather than samples, so "
                    "the comparison is meaningful. The common intuition that extra swaps wash the "
                    "bias out predicts the opposite of what happens."},
            {"q": "Suppose a shuffle were found for which `n!` does divide the number of tapes. What would follow?",
             "a": ["It would be uniform",
                   "It would be uniform for that `n` only",
                   "Nothing about uniformity; the argument only refutes, never confirms",
                   "It would have a total variation distance of exactly zero"],
             "c": 2,
             "why": "Divisibility is necessary for uniformity, not sufficient. The tapes could "
                    "still be distributed unevenly among the permutations in a way that happens to "
                    "have a whole-number average. The lab says exactly this when the division "
                    "comes out exact: the counting argument says nothing, and the enumeration is "
                    "then the only thing that can answer."},
        ],
        "mistakes": [
            ("Testing uniformity by shuffling a lot and looking at the counts",
             "A sample from a uniform distribution is uneven, and a sample from a distribution "
             "`25/384` away from uniform is uneven in a way that looks the same at 120 runs. The "
             "lab shows both columns side by side precisely so this is visible: Fisher&ndash;Yates "
             "over 120 seeds reaches 23 of 24 permutations with lopsided counts, and it is "
             "provably uniform. The sample cannot separate the two hypotheses at any sample size a "
             "lesson can run."),
            ("Reading the bias off the output rather than the tape counts",
             "Nobody can look at `1032` and see why it is favoured, and the identity permutation "
             "is one of the less likely outcomes at `n = 3`, not the most likely. The asymmetry is "
             "a property of how many tapes lead where, and the only way to see it is to count them "
             "&mdash; which is why the lab prints the tape count in its own column beside the "
             "probability."),
            ("Assuming more randomness makes a biased procedure fairer",
             "The naive swap makes `n` draws from `n` values, which is more raw randomness than "
             "Fisher&ndash;Yates uses, and it is the one that is wrong. What matters is whether "
             "the number of equally likely runs is compatible with the number of answers, and "
             "adding draws multiplies the tape count by `n` while the number of permutations does "
             "not move."),
        ],
        "standard": ("Finish when you can refute a sampling procedure on paper, before running it once.",
                     "You should be able to count the tapes of a procedure from its loop, divide "
                     "by the number of outcomes, and say what a nonzero remainder proves and what "
                     "a zero remainder does not; and you should be able to say why the measured "
                     "column of a provably uniform shuffle still looks uneven."),
        "note": ("Everything after this is the same distinction applied to a quantity rather than "
                 "to an outcome. &ldquo;The Cost Is a Distribution&rdquo; enumerates every "
                 "execution of a sorting algorithm instead of every tape of a shuffle, and gets a "
                 "distribution over comparison counts; the enumeration is the same idea and the "
                 "recursion that performs it is the only new machinery."),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-cost-is-a-distribution",
        "title": "The Cost Is a Distribution",
        "module": "Randomness as a resource",
        "one_line": "Print the cost on one input three ways — always, in expectation, and measured — and watch only one of them move when the input changes.",
        "summary": (
            "Randomised quicksort on a sorted array of eight keys costs 28 comparisons with a "
            "fixed pivot, has an expectation of `2369/140` with a random one, and averaged "
            "`415/24` over 120 seeds. Those are three different kinds of number and the "
            "lesson is that none of them is either of the others. The exact distribution is "
            "computed by recursion over subproblem sizes, checked against the closed form, "
            "and checked again against running the algorithm on every input order."
        ),
        "key": [
            "fixed pivot on a sorted array:  28 comparisons, every time",
            "E[C] = 2369/140 = 16.9214…      over every execution, exactly",
            "closed form  2(n+1)Hₙ − 4n      a second definition, same number",
            "mean over 120 seeds: 415/24     a MEASUREMENT, and it moves",
            "support 13 ≤ C ≤ 28             an ALWAYS claim, with 28 = n(n−1)/2",
            "Var(C) = 160599/19600           exact, and the next lesson needs it",
        ],
        "key_label": "One input, one algorithm, and three numbers that are not each other",
        "concepts_intro": (
            "The hard idea is that the second number is not an average of runs. The other two "
            "are what changes when the input moves and what changes when the seeds move."
        ),
        "concepts": [
            ("A randomised algorithm has a cost per execution, not a cost",
             "Fix the input and the fixed-pivot rule and there is one number: on a sorted array of "
             "eight keys, 28 comparisons, and running it again gives 28 again. Fix the input and "
             "randomise the pivot and there is no single number &mdash; there is a "
             "<strong>distribution</strong>, and on this input it puts weight on every count from "
             "13 to 28. The lab draws it as bars. `E[C] = 2369/140` is one summary of that shape, "
             "and `P(C = 16) = 73/360` is another."),
            ("The expectation is computed, not averaged",
             "`rqsPmf` builds the distribution by recursion on subproblem <em>sizes</em>: "
             "`D(k) = (k − 1) + (1/k)·Σᵢ D(i) ⊛ D(k − 1 − i)`, with every weight an exact "
             "rational. No run is involved and no seed is consulted, so the answer does not move "
             "when the seed slider does. It is checked twice &mdash; against the closed form "
             "`2(n + 1)Hₙ − 4n`, which is a different definition, and at small `n` against running "
             "the fixed-pivot algorithm on all `n!` input orders, which is a different experiment."),
            ("Which numbers the input moves, and which it does not",
             "Change the array from sorted to alternating high and low and the fixed-pivot count "
             "drops from 28 to 16. The exact distribution does not move at all: not the "
             "expectation, not the variance, not a single bar. A uniformly random pivot "
             "<em>position</em> selects a uniformly random <em>rank</em> whatever order the keys "
             "arrived in, so the randomness is the algorithm's and not the data's, and that is the "
             "entire content of randomising the pivot."),
        ],
        "read_title": "Three numbers in one row, and what each one is about",
        "read_intro": "The count on one input, the expectation over every execution, the mean over the seeds shown — and two checks that the middle one is right.",
        "body": [
            ("def", ("The two pivot rules, and what a partition costs",
                     "Quicksort on a block of length `L` chooses a pivot, partitions the block "
                     "against it at a cost of `L − 1` comparisons, and recurses on the two pieces. "
                     "The <strong>fixed rule</strong> always takes the last element of the block. "
                     "The <strong>random rule</strong> takes a uniformly random position in the "
                     "block, independently at every call. The comparison count `C` is the total "
                     "over all partitions, and it is the only cost this lesson measures.")),
            ("p", "On a sorted array the fixed rule pays the worst case. Every pivot is the "
                  "largest remaining key, so every partition splits a block of length `L` into one "
                  "of length `L − 1` and one of length `0`, and the total is "
                  "`7 + 6 + 5 + 4 + 3 + 2 + 1 = 28`, which is `n(n − 1)/2`. It is 28 on the "
                  "reversed array too, for the mirror-image reason. On the alternating array it is "
                  "16. One rule, three inputs, three different counts &mdash; and every one of "
                  "them is that rule's cost on that input for ever."),
            ("def", ("The distribution of the random rule's cost",
                     "For each `n`, `D(n)` is the probability mass function of the comparison "
                     "count when every pivot is uniformly random. `D(0)` and `D(1)` are the point "
                     "mass at `0`. For `k ≥ 2`, the first partition costs `k − 1`, and the pivot's "
                     "rank is uniform on `1..k`, leaving blocks of sizes `i` and `k − 1 − i` whose "
                     "costs are independent. So `D(k)` is `k − 1` plus the average over `i` of the "
                     "convolution of `D(i)` and `D(k − 1 − i)`.")),
            ("p", "That recursion is over sizes rather than over tapes, which is what makes it "
                  "cheap: the cost of an execution depends only on how the pivots split the "
                  "blocks, not on which elements they were. At `n = 8` it produces sixteen "
                  "probabilities, one for each attainable count from 13 to 28, and they add to `1` "
                  "&mdash; a check the panel performs and prints rather than assuming."),
            ("example", ("The distribution at n = 8, in full",
                         "`P(C = 13) = 1/24`, `P(14) = 13/72`, `P(15) = 3/20`, `P(16) = 73/360`, "
                         "`P(17) = 29/840`, `P(18) = 59/420`, `P(19) = 31/420`, `P(20) = 5/84`, "
                         "`P(21) = 1/36`, `P(22) = 11/252`, `P(23) = 17/1260`, `P(24) = 1/63`, "
                         "`P(25) = 2/315`, `P(26) = 1/210`, `P(27) = 1/630` and `P(28) = 1/315`. "
                         "The most likely count is 16 and the mean is `2369/140 ≈ 16.92`, so the "
                         "two are not the same number; and the shape is not a smooth hump &mdash; "
                         "`P(17)` is a sixth of `P(16)` and a quarter of `P(18)`.")),
            ("p", "That jaggedness is worth a second look, because it is the first thing a reader "
                  "expecting a bell curve will try to explain away. It is real. A comparison count "
                  "is a sum over partitions of `L − 1`, and the attainable sums at small `n` are "
                  "constrained by arithmetic rather than by anything smooth: some totals have many "
                  "ways to arise and some have few. Nothing about the expectation requires the "
                  "shape around it to be well behaved, which is exactly why the next lesson's "
                  "bounds are stated for every distribution and not for nice ones."),
            ("thm", ("The closed form",
                     "For `n ≥ 1`, the expected number of comparisons made by randomised quicksort "
                     "on `n` distinct keys is `2(n + 1)Hₙ − 4n`, where `Hₙ` is the `n`-th harmonic "
                     "number. It does not depend on the input.")),
            ("p", "The derivation is Sorting and Selection's, by indicator variables: the `i`-th "
                  "and `j`-th smallest keys are compared exactly when one of them is the first "
                  "pivot drawn from the stretch of sorted order between them, which has "
                  "probability `2/(j − i + 1)`, and linearity adds the indicators up. This course "
                  "uses it as an <em>oracle</em> rather than re-deriving it. `H₈ = 761/280`, so "
                  "the closed form gives `2·9·761/280 − 32 = 2369/140`, and the panel prints it "
                  "beside the recursion's answer with the word agrees or the word DISAGREES."),
            ("h3", "A third route, and the check a comparison count cannot perform"),
            ("p", "At `n ≤ 7` the lab does something different again: it runs the "
                  "<em>fixed</em>-pivot algorithm on every one of the `n!` input orders and tallies "
                  "what it counted. At `n = 5` that is 120 runs, and the resulting distribution "
                  "agrees with the recursion value by value, with an expectation of `37/5` from "
                  "both. The agreement is a theorem, not a coincidence: randomising the pivot on a "
                  "fixed input and fixing the pivot on a uniformly random input are the same "
                  "experiment."),
            ("p", "That pass also checks something no comparison count can. Every one of those 120 "
                  "runs is required to have returned a sorted array that is a permutation of its "
                  "input, and the seeded runs are checked the same way. An unsorted array has a "
                  "comparison count too, and a sorting arm whose only assertion is a count will "
                  "report a confident number about a broken sort. The panel's last figure reads "
                  "yes, all 120 for exactly that reason."),
            ("h3", "The measured column, and what moving a slider proves"),
            ("p", "Over seeds 1 to 120 on the sorted array the mean comes out `415/24`, which is "
                  "`17.2917`, against an expectation of `16.9214`: high by `311/840`. On the "
                  "reversed array the same 120 seeds give `1031/60`, and on the alternating array "
                  "`1003/60`, which is <em>below</em> the expectation. The exact distribution is "
                  "identical in all three cases. Three different measured means, one expectation, "
                  "and the only thing that changed was an input the expectation does not depend on."),
            ("p", "The observed range is the other half of the story: 13 to 27 over those 120 "
                  "seeds on the sorted array, 13 to 26 on the reversed one, 13 to 28 on the "
                  "alternating one. The support of the true distribution is 13 to 28 in every "
                  "case. A measured range is a subset of the support and it is a different object "
                  "from it &mdash; the 120 seeds that never produced 28 do not make 28 impossible, "
                  "and `P(C = 28) = 1/315` says how impossible it is not."),
            ("h3", "The one claim here that holds always"),
            ("p", "`C ≤ n(n − 1)/2` on every execution, because each partition compares the pivot "
                  "with each other element of its block at most once and each pair of elements "
                  "ends up in the same block for at most one partition. The panel checks that the "
                  "support of the exact distribution sits inside that bound rather than quoting "
                  "it. That is the only always claim on this page; the expectation is not one, and "
                  "neither is the mean."),
        ],
        "lab": ("random", {"mode": "costs", "preset": "sorted8"}),
        "steps_title": "Reading three columns without mixing them up",
        "steps_intro": "Name the kind of each number before you compare any two of them.",
        "steps": [
            ("Ask what the number ranges over",
             "Over one execution on one input, over every execution on one input, or over the "
             "seeds on screen. The fixed count is the first, the expectation and the variance are "
             "the second, the mean and the observed range are the third. Two numbers of different "
             "kinds are never in conflict, however far apart they sit."),
            ("Move the input and see what follows",
             "Switch between sorted, reversed and alternating. The fixed count moves from 28 to 28 "
             "to 16; the whole exact distribution stays put. Anything that moved with the input "
             "was a property of the input, and this lab is built so the split is visible in one "
             "click."),
            ("Move the seeds and see what follows",
             "The measured mean and the measured range move; nothing else does. If a sentence you "
             "were about to write changes when the seed slider moves, it was a sentence about 120 "
             "runs, and it should say so."),
            ("Check the expectation against something that is not it",
             "The closed form and the enumeration over every input order are two independent "
             "routes to the same number, and the panel prints both with a verdict. An expectation "
             "computed one way and checked nowhere is the easiest thing on this course to get "
             "confidently wrong."),
        ],
        "worked": {
            "title": "One input, eight keys, three numbers",
            "intro": [
                "The array is `1 2 3 4 5 6 7 8`, already sorted, and the two rules are run on it. "
                "The first column is one execution; the second is all of them; the third is 120 of "
                "them.",
            ],
            "lines": [
                "FIXED PIVOT, last element, on 1..8",
                "  [0..7] len 8 pivot 8    7 comparisons",
                "  [0..6] len 7 pivot 7    6",
                "  [0..5] len 6 pivot 6    5",
                "  [0..4] len 5 pivot 5    4",
                "  [0..3] len 4 pivot 4    3",
                "  [0..2] len 3 pivot 3    2",
                "  [0..1] len 2 pivot 2    1",
                "                        ---",
                "                         28   every time, = n(n-1)/2",
                "",
                "RANDOM PIVOT, over every execution",
                "  E[C]      = 2369/140 = 16.921428…     = 2(n+1)H_n - 4n, H_8 = 761/280",
                "  Var(C)    = 160599/19600 = 8.1938…",
                "  support   = 13 .. 28,  P(C = 28) = 1/315",
                "",
                "RANDOM PIVOT, measured over seeds 1..120",
                "  seed 1: 23    seed 2: 13    seed 3: 19    seed 4: 19    seed 5: 18",
                "  mean      = 415/24 = 17.29166…        range 13 .. 27",
                "  gap above the expectation = 311/840 = 0.37023…",
            ],
            "after": [
                "Seed 2 costs 13 comparisons and seed 1 costs 23, on the same array, with the same "
                "algorithm. Neither is the expectation and neither is an error. The distribution "
                "puts `1/24` on 13 and `17/1260` on 23, and both events happened in the first "
                "two seeds, which is roughly what those probabilities predict.",
                "The gap between `415/24` and `2369/140` is `311/840`, about `0.37` comparisons. "
                "It is not evidence that the expectation is wrong, and it is not evidence that it "
                "is right: with a variance of `8.19` and 120 samples, a gap of that size is "
                "ordinary. The next lesson makes that sentence precise without ever taking a "
                "square root.",
                "For a faded rehearsal, set the input to alternating and predict all three numbers "
                "before the page redraws. The supplied first move is this: the fixed count is a "
                "property of the arrangement and will change, and the exact expectation is a "
                "property of the algorithm and will not. Say what the measured mean is likely to "
                "do &mdash; and then say why &ldquo;likely&rdquo; is the strongest word available "
                "for it.",
            ],
        },
        "quiz_title": "Which number is which",
        "quiz": [
            {"q": "The panel reads: fixed pivot 28, exact expectation `2369/140`, measured mean `415/24`. Which of these changes if you switch the array to alternating high and low?",
             "a": ["All three, since the input changed",
                   "The expectation only, since it averages over inputs",
                   "The fixed count and the measured mean; the exact distribution does not move",
                   "The fixed count only"],
             "c": 2,
             "why": "The fixed rule's cost is a function of the arrangement and drops to 16. The "
                    "exact distribution is a function of `n` alone, because a uniformly random "
                    "pivot position picks a uniformly random rank whatever order the keys arrived "
                    "in. The measured mean moves as well — it came out `1003/60` — because it is a "
                    "sample of runs and the runs are different runs."},
            {"q": "Over 120 seeds the observed counts ran from 13 to 27, and the exact distribution has support 13 to 28. What follows?",
             "a": ["The distribution is wrong: 28 was never observed",
                   "Nothing follows about 28; `P(C = 28) = 1/315` and 120 seeds is a small sample",
                   "28 is impossible on a sorted input",
                   "The measured range is the support, and the exact support is an over-estimate"],
             "c": 1,
             "why": "A measured range is the set of values that happened to appear, and the "
                    "support is the set of values with positive probability. At `1/315` an "
                    "outcome is absent from 120 seeds most of the time. The alternating array's "
                    "120 seeds did reach 28, with the same distribution behind them, which makes "
                    "the point from the other side."},
            {"q": "Why does the lab compute the distribution by recursion on subproblem sizes rather than by enumerating pivot tapes?",
             "a": ["Tapes would give a different answer",
                   "The cost depends only on the sizes the pivots split the blocks into, and there are far fewer size patterns than tapes",
                   "Tapes cannot be enumerated for any `n`",
                   "The recursion is an approximation that is close enough at these sizes"],
             "c": 1,
             "why": "Two executions that split the blocks the same way cost the same, so the sizes "
                    "are the right state and the recursion is exact rather than approximate. "
                    "Enumerating tapes would give the same answer much more slowly, which is why "
                    "the lab uses a different enumeration — the fixed rule over all `n!` input "
                    "orders — as its independent check at `n ≤ 7`."},
            {"q": "Which claim on this page is an ALWAYS claim?",
             "a": ["`C ≤ n(n − 1)/2`",
                   "`E[C] = 2369/140`",
                   "the mean over 120 seeds is `415/24`",
                   "`P(C = 16) = 73/360`"],
             "c": 0,
             "why": "The bound holds on every execution, and the panel verifies that the exact "
                    "distribution's support sits inside it. The expectation and the individual "
                    "probabilities are exact statements about the distribution, not about any one "
                    "run, and the mean is a measurement over 120 particular runs."},
        ],
        "mistakes": [
            ("Running an algorithm many times and calling the average the expectation",
             "The average over 120 seeds on the sorted array is `415/24` and the expectation is "
             "`2369/140`; on the alternating array the same 120 seeds give `1003/60`, which is "
             "below it. Three measurements, one expectation, and no amount of extra seeds turns "
             "the first kind of number into the second. The expectation is computed from the "
             "algorithm's structure, and the lab does it two independent ways."),
            ("Treating the expectation as the typical cost",
             "`E[C] = 16.92` at `n = 8`, and the single most likely count is 16 while 17 has less "
             "than a fifth of 16's probability. The distribution is jagged at this size and the "
             "expectation is a weighted average of a lumpy thing, not a description of a typical "
             "run. Look at the bars before saying what a run costs."),
            ("Quoting a worst case and an expectation as if they compete",
             "28 and `2369/140` are both correct about the same algorithm on the same input. The "
             "first is an upper bound that holds on every execution and is attained with "
             "probability `1/315`; the second is the average over all of them. A sentence that "
             "puts them in tension has confused a guarantee with a summary."),
        ],
        "standard": ("Finish when you can say, of every number on a randomised algorithm's page, what it ranges over.",
                     "You should be able to name the three kinds apart, predict which of them a "
                     "change of input moves and which a change of seed moves, explain why the "
                     "expectation does not depend on the arrangement, and give at least two "
                     "independent routes to the same expectation."),
        "note": ("The variance in the corner of this panel is not decoration. "
                 "&ldquo;From an Expectation to a Probability&rdquo; uses it to bound the chance "
                 "that a run costs far more than average, and it does so with an inequality that "
                 "assumes nothing about the jagged shape above &mdash; which is the property that "
                 "makes it worth proving."),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "from-an-expectation-to-a-probability",
        "title": "From an Expectation to a Probability",
        "module": "Randomness as a resource",
        "one_line": "Prove Markov's inequality from the definition of expectation, get Chebyshev's by applying it to the squared deviation, and measure the slack in both.",
        "summary": (
            "An expectation on its own promises nothing about any run. Markov's inequality "
            "turns a mean into a tail bound in three lines, and Chebyshev's follows by "
            "applying Markov to `(X − μ)²`. Both hold for every distribution with the stated "
            "moments &mdash; no shape assumed, no independence used &mdash; and the price of "
            "that generality is slack, which this page measures rather than describes. On a "
            "ten-key quicksort, Markov's bound at 24 comparisons is `30791/30240`, which is "
            "greater than one."
        ),
        "key": [
            "Markov:     X ≥ 0, a > 0   ⟹   P(X ≥ a) ≤ E[X]/a",
            "Chebyshev:  P(|X − μ| ≥ t) ≤ Var(X)/t²      Markov applied to (X − μ)²",
            "with t = kσ this reads   P(|X − μ| ≥ kσ) ≤ 1/k²",
            "n = 10:  E = 30791/1260, Var = 4913659/317520",
            "P(C ≥ 24) = 332/675, Markov says ≤ 30791/30240 — above 1, true and useless",
            "P(C ≥ 45) = 2/14175, Markov says ≤ 30791/56700 — loose by a factor near 3849",
        ],
        "key_label": "Two inequalities, their proofs, and the slack they leave",
        "concepts_intro": (
            "The hard idea is that one inequality gives the other by substitution. The other "
            "two are what each assumes and what each costs in accuracy."
        ),
        "concepts": [
            ("A mean bounds a tail, because mass far out is expensive",
             "If `X` is never negative, every unit of probability sitting at or above `a` "
             "contributes at least `a` to the expectation, and nothing contributes less than zero. "
             "So `E[X] ≥ a·P(X ≥ a)`, and dividing gives <strong>Markov's inequality</strong>: "
             "`P(X ≥ a) ≤ E[X]/a`. Non-negativity is the only hypothesis, which is why the bound "
             "is often weak &mdash; it is consistent with everything the mean allows, including a "
             "distribution that is all at `0` and `a`."),
            ("Chebyshev is Markov applied to the squared deviation",
             "`(X − μ)²` is never negative, whatever `X` is, and its expectation is `Var(X)` by "
             "definition. The event `|X − μ| ≥ t` is the same event as `(X − μ)² ≥ t²`, because "
             "squaring is increasing on the non-negatives. So Markov on `(X − μ)²` at `a = t²` "
             "gives `P(|X − μ| ≥ t) ≤ Var(X)/t²` immediately. That is the whole derivation, and it "
             "is why Discrete Probability can state Chebyshev and leave the proof here."),
            ("Generality is paid for in slack, and the slack is a number",
             "Neither inequality assumes a shape, a symmetry, or independence, so both hold for the "
             "jagged comparison-count distribution as readily as for anything smooth. The price is "
             "visible: at `a = 24` on ten keys the true tail is `332/675 ≈ 0.4919` and Markov "
             "allows `30791/30240 ≈ 1.0182`. A bound above one is true and carries no information, "
             "and the lab prints it rather than hiding it."),
        ],
        "read_title": "Two proofs, and the distance between a bound and the truth",
        "read_intro": "The inequalities the rest of this course quotes, proved here, with their slack measured against an exactly known distribution.",
        "body": [
            ("thm", ("Markov's inequality",
                     "Let `X` be a random variable taking only non-negative values, with finite "
                     "expectation, and let `a > 0`. Then `P(X ≥ a) ≤ E[X]/a`.")),
            ("proof", ("Write the expectation as a sum over the values `X` can take: "
                       "`E[X] = Σ x·P(X = x)`, where every term has `x ≥ 0` and "
                       "`P(X = x) ≥ 0`, so every term is non-negative.",
                       "Throw away the terms with `x &lt; a`. Discarding non-negative terms can "
                       "only decrease the sum, so `E[X] ≥ Σ` over `x ≥ a` of `x·P(X = x)`.",
                       "In what is left, every `x` is at least `a`, so replacing each `x` by `a` "
                       "can only decrease the sum again: `E[X] ≥ a·Σ` over `x ≥ a` of "
                       "`P(X = x) = a·P(X ≥ a)`. Divide by `a > 0`.")),
            ("p", "Two features of that argument are worth naming because they are what the rest "
                  "of the course relies on. It never looks at the shape of the distribution, so it "
                  "applies to any non-negative `X` at all; and it is tight, in the sense that a "
                  "variable taking value `a` with probability `E[X]/a` and `0` otherwise meets it "
                  "with equality. A bound that is attained by some distribution cannot be improved "
                  "without adding a hypothesis, and the next theorem is what one extra hypothesis "
                  "buys."),
            ("thm", ("Chebyshev's inequality",
                     "Let `X` have finite mean `μ` and finite variance `Var(X)`, and let `t > 0`. "
                     "Then `P(|X − μ| ≥ t) ≤ Var(X)/t²`. Writing `t = kσ` with `σ` the standard "
                     "deviation and `k > 0` gives the form Discrete Probability states: "
                     "`P(|X − μ| ≥ kσ) ≤ 1/k²`.")),
            ("proof", ("Let `Y = (X − μ)²`. A square is never negative, so Markov's inequality "
                       "applies to `Y`, and `E[Y] = Var(X)` is the definition of the variance.",
                       "The events are the same: `|X − μ| ≥ t` holds exactly when "
                       "`(X − μ)² ≥ t²`, because both sides of `|X − μ| ≥ t` are non-negative and "
                       "squaring preserves order there. So "
                       "`P(|X − μ| ≥ t) = P(Y ≥ t²) ≤ E[Y]/t² = Var(X)/t²` by Markov at `a = t²`.",
                       "For the second form, put `t = kσ`. Then `Var(X)/t² = σ²/(k²σ²) = 1/k²`, "
                       "provided `σ > 0`; if `σ = 0` then `X` is constant and both sides are `0` "
                       "for every `t > 0`.")),
            ("p", "That is the proof the Simulation course of the Operations Research path points "
                  "at when it states Chebyshev and applies it to a sample mean. It is two lines "
                  "because Markov did the work, and it is worth noticing which line carries the "
                  "generality: nothing above assumed the distribution was symmetric, unimodal, or "
                  "anything else. A confidence interval built on Chebyshev is valid for a "
                  "simulation whose output distribution nobody has written down, and that is the "
                  "property being bought."),
            ("h3", "The slack, measured against a distribution that is known exactly"),
            ("p", "Randomised quicksort on ten keys is the ideal test, because the lab knows the "
                  "whole distribution: `E[C] = 30791/1260 ≈ 24.4373` and "
                  "`Var(C) = 4913659/317520 ≈ 15.4751`, both exact. So every bound can be printed "
                  "beside the quantity it bounds rather than beside a guess at it. Slide the "
                  "threshold and the panel recomputes both columns."),
            ("math", [
                "  a      P(C >= a) exactly        Markov, E/a           ratio",
                " 24      332/675    = 0.49185      30791/30240 = 1.0182    2.07",
                " 30      6283/56700 = 0.11081      30791/37800 = 0.8146    7.35",
                " 36      13/945     = 0.01376      30791/45360 = 0.6788   49.34",
                " 45      2/14175    = 0.00014      30791/56700 = 0.5431 3848.88",
            ]),
            ("p", "At `a = 24` the bound exceeds one, and a probability is at most one anyway, so "
                  "the inequality is true and says nothing whatsoever. That is not a defect in the "
                  "lab or a badly chosen slider position: it is what Markov does when `a` is near "
                  "the mean, and a reader who has never seen it will eventually quote a vacuous "
                  "bound as though it were evidence. Further out the bound becomes informative in "
                  "form and steadily worse in accuracy, until at the worst case it overstates the "
                  "truth by a factor near 3849."),
            ("h3", "What the second moment buys"),
            ("math", [
                "  t      P(|C - E| >= t) exactly   Chebyshev, Var/t^2",
                "  3      1751/3780  = 0.46323      4913659/2857680  = 1.7195",
                "  6      1637/18900 = 0.08661      4913659/11430720 = 0.4299",
                "  9      1571/56700 = 0.02771      4913659/25719120 = 0.1911",
                " 12      44/4725    = 0.00931      4913659/45722880 = 0.1075",
                " 15      19/9450    = 0.00201      4913659/71442000 = 0.0688",
            ]),
            ("p", "Chebyshev decays as `1/t²` where Markov decays as `1/a`, so it is the sharper "
                  "tool once `t` is a few standard deviations out: at `t = 15` it allows `0.069` "
                  "against a truth of `0.002`, a factor of 34, where Markov at the comparable "
                  "threshold was out by a factor of thousands. It also goes vacuous, at `t = 3`, "
                  "for the same reason &mdash; `σ ≈ 3.93` here, so `t = 3` is less than one "
                  "standard deviation and `1/k²` exceeds one."),
            ("p", "And it bounds a two-sided event. `P(|C − μ| ≥ t)` includes runs that were "
                  "unusually cheap as well as unusually expensive, which is often not the event "
                  "you care about. Using Chebyshev for a one-sided question is legitimate and "
                  "wasteful: it throws away half the bound. The lab prints the two-sided exact "
                  "probability beside it so the comparison is like for like."),
            ("h3", "Why not measure the tail instead"),
            ("p", "Over seeds 1 to 120 the panel counts 60 runs at or above 24 comparisons, which "
                  "is `1/2`, against an exact tail of `332/675 ≈ 0.492`. Eleven runs reached 30, "
                  "against `0.111`. One run reached 36, against `0.0138`. The measurements are "
                  "close and they are measurements: they move with the slider, they say nothing "
                  "about the values no seed reached, and they are about this instance rather than "
                  "about every instance. The bounds are about every instance and they hold for "
                  "instances nobody has enumerated, which is the only reason to prove them."),
            ("p", "The honest summary is that this page has three ways to answer &ldquo;how likely "
                  "is a bad run?&rdquo; and they are ranked by what they cost and what they cover. "
                  "The enumeration is exact and available only when the distribution can be "
                  "computed. The measurement is available always and establishes nothing about "
                  "unobserved outcomes. The bound is available from two numbers, holds for every "
                  "distribution with those numbers, and is loose by a factor this page prints."),
        ],
        "lab": ("random", {"mode": "costs", "preset": "sorted10"}),
        "steps_title": "Applying a tail bound without overclaiming",
        "steps_intro": "Check the hypothesis, then the event, then the slack — in that order.",
        "steps": [
            ("Check that the variable is non-negative before reaching for Markov",
             "Comparison counts, running times, sizes and loads are non-negative and Markov "
             "applies directly. A deviation, a profit, or a difference of two counts is not, and "
             "applying Markov to it produces a statement that is simply false. Chebyshev has no "
             "such restriction because it squares first."),
            ("Write down the event you actually care about",
             "`C ≥ a` is one-sided; `|C − μ| ≥ t` is two-sided and includes the cheap runs. Using "
             "the second to bound the first is valid and loses a factor of about two. Using the "
             "first to bound the second is not valid at all."),
            ("Compare the bound with one and stop if it is bigger",
             "At `a = 24` on this instance Markov returns `1.0182`. A bound above one is true, "
             "carries no information, and should not appear in a conclusion. Move the threshold "
             "out until the bound drops below one before quoting it."),
            ("Put the bound beside the exact tail where you can compute it",
             "This lab can, so use it to calibrate: Markov is out by a factor of 2 near the mean "
             "and by thousands at the worst case, and Chebyshev by about 34 at fifteen "
             "comparisons out. Those factors are what you are accepting when you use a bound on an "
             "instance you cannot enumerate."),
        ],
        "worked": {
            "title": "Chebyshev on the ten-key distribution, by hand",
            "intro": [
                "The lab supplies `E[C] = 30791/1260` and `Var(C) = 4913659/317520`, both exact. "
                "The question: bound the probability that a run costs 36 comparisons or more, and "
                "compare with the truth.",
            ],
            "lines": [
                "E[C]   = 30791/1260   = 24.43730…",
                "Var(C) = 4913659/317520 = 15.47511…",
                "",
                "MARKOV, one-sided, at a = 36",
                "  P(C >= 36) <= E/a = (30791/1260)/36 = 30791/45360 = 0.67881",
                "  exact                               = 13/945      = 0.01376",
                "  the bound is 49.3 times the truth",
                "",
                "CHEBYSHEV, two-sided.  36 - E = 11.5627, so C >= 36 implies |C - E| >= 11",
                "  P(|C - E| >= 11) <= Var/121 = 4913659/38419920 = 0.12789",
                "  exact                        = 13/945           = 0.01376",
                "  the bound is 9.3 times the truth",
                "",
                "  and P(C >= 36) <= P(|C - E| >= 11) is the one-sided consequence,",
                "  so Chebyshev bounds the same event at 0.12789 where Markov gave 0.67881",
                "",
                "MEASURED, seeds 1..120",
                "  runs with C >= 36: 1 of 120 (seed 83)",
            ],
            "after": [
                "Chebyshev beats Markov here by a factor of five, and it does so using one extra "
                "number about the distribution. That is the trade in general: each further moment "
                "you are willing to compute buys a faster decay in the tail, and this library "
                "stops at the second because the next step is Chernoff's bound and this course "
                "excludes it.",
                "Notice the step that turned a two-sided bound into a one-sided claim, and notice "
                "the arithmetic in it. `36 − E = 11.5627`, so `C ≥ 36` implies `|C − E| ≥ 11` but "
                "<em>not</em> `|C − E| ≥ 12`: at `C = 36` the deviation is `11.56`, and using "
                "`t = 12` would have been a bound on a smaller event than the one asked about. The "
                "containment runs one way only and it is easy to write down backwards.",
                "Here it happens to be an equality rather than a containment. `|C − E| ≥ 11` means "
                "`C ≥ 35.44` or `C ≤ 13.44`, and the distribution's support starts at 19, so the "
                "lower half is empty and `P(|C − E| ≥ 11) = P(C ≥ 36) = 13/945` exactly. Chebyshev "
                "is bounding precisely the event in question on this instance, and it is still out "
                "by a factor of nine.",
                "For a faded rehearsal, do the same at `a = 30` and predict which of the two "
                "inequalities wins before computing either. The supplied first move is this: `30` "
                "is about `1.4` standard deviations above the mean, and Chebyshev at `k` standard "
                "deviations allows `1/k²`. Work out what `1/k²` is there, compare it with "
                "`E/a = 0.8146`, and then check both against the exact `6283/56700`.",
            ],
        },
        "quiz_title": "Bounds, hypotheses, and slack",
        "quiz": [
            {"q": "Which hypothesis does Markov's inequality need?",
             "a": ["That `X` is non-negative",
                   "That `X` has finite variance",
                   "That the distribution is symmetric about its mean",
                   "That the draws are independent"],
             "c": 0,
             "why": "Non-negativity and a finite mean, and nothing else. The proof discards the "
                    "terms below `a` and replaces the rest by `a`, and both steps need the values "
                    "to be non-negative. No variance is required, no shape is assumed, and there "
                    "is only one random variable so independence does not arise."},
            {"q": "How is Chebyshev's inequality obtained from Markov's?",
             "a": ["By taking square roots on both sides",
                   "By applying Markov to `(X − μ)²` at the threshold `t²`",
                   "By assuming the distribution is approximately normal",
                   "By summing Markov over the values of `X`"],
             "c": 1,
             "why": "`(X − μ)²` is non-negative so Markov applies to it, its expectation is the "
                    "variance by definition, and `|X − μ| ≥ t` is the same event as "
                    "`(X − μ)² ≥ t²`. Substituting gives `Var(X)/t²` directly. No normality is "
                    "involved anywhere, which is exactly why the inequality is usable on a "
                    "distribution nobody has written down."},
            {"q": "The panel shows Markov's bound at `a = 24` as `30791/30240 ≈ 1.0182`. What should be concluded?",
             "a": ["The lab has a bug: a probability cannot exceed one",
                   "The inequality has failed on this distribution",
                   "The bound is true and vacuous, because `a` is close to the mean",
                   "The exact tail must therefore be close to one"],
             "c": 2,
             "why": "The inequality says the probability is at most `1.0182`, which is true of "
                    "every probability. It is not a claim about the lab and not a failure of the "
                    "theorem; it is Markov being uninformative when the threshold is barely above "
                    "the mean of `24.44`. The exact tail there is `332/675 ≈ 0.49`."},
            {"q": "You want `P(C ≥ 36)` and you have `Var(C)`. Which is a valid route?",
             "a": ["Chebyshev gives `P(|C − μ| ≥ 11) ≤ Var/121`, and `C ≥ 36` implies `|C − μ| ≥ 11`",
                   "Chebyshev gives `P(C ≥ 36)` directly, since it is a tail",
                   "Halve Chebyshev's bound, since the distribution is symmetric",
                   "Neither inequality applies, because 36 is inside the support"],
             "c": 0,
             "why": "Chebyshev bounds a two-sided event, so the one-sided question is answered by "
                    "containment: with `μ ≈ 24.44`, the event `C ≥ 36` is contained in "
                    "`|C − μ| ≥ 11` — and not in `|C − μ| ≥ 12`, since `36 − μ` is only `11.56`. "
                    "Halving is not "
                    "available — nothing here establishes symmetry, and the distribution on this "
                    "page is visibly not symmetric."},
        ],
        "mistakes": [
            ("Quoting a bound that is greater than one",
             "It happens on the default slider position of this very lab: Markov at 24 comparisons "
             "returns `1.0182`. The statement is true and carries no information, and a conclusion "
             "resting on it is resting on nothing. Compare every bound with one before using it, "
             "and if it fails that test either move the threshold or find a stronger inequality."),
            ("Applying Markov to a variable that can be negative",
             "The proof needs every discarded term to be non-negative. A deviation `C − μ` takes "
             "negative values, and `P(C − μ ≥ a) ≤ E[C − μ]/a = 0` would be the conclusion, which "
             "is false. Square it first, which is what Chebyshev does, or shift it so that it "
             "cannot go below zero."),
            ("Reading Chebyshev's two-sided bound as a one-sided one",
             "`Var/t²` bounds the probability of landing `t` away in <em>either</em> direction. "
             "Treating it as a bound on the upper tail alone is still valid, because the upper "
             "tail is part of that event, but treating it as an equality for the upper tail is "
             "not, and neither is halving it: this page's distribution has `P(C ≥ μ + 12)` and "
             "`P(C ≤ μ − 12)` nowhere near equal."),
        ],
        "standard": ("Finish when you can derive both inequalities from the definition of expectation and say what each costs.",
                     "You should be able to prove Markov's inequality in three steps, obtain "
                     "Chebyshev's by substituting `(X − μ)²`, state the `1/k²` form, recognise a "
                     "vacuous bound on sight, and say which of a page's numbers is exact, which is "
                     "measured and which is bounded."),
        "note": ("These are the only two concentration results this library proves, and every later "
                 "page that needs one uses them by name. &ldquo;The Count-Min Sketch&rdquo; states "
                 "its guarantee as Markov's rather than the sharper textbook version for exactly "
                 "that reason, and the two maximum-load figures on &ldquo;Balls in Bins and the "
                 "Birthday Bound&rdquo; are labelled stated and not proved because their proofs "
                 "need a bound that comes after these two and is not taught here."),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "balls-in-bins-and-the-birthday-bound",
        "title": "Balls in Bins and the Birthday Bound",
        "module": "Expectation, and what it does not assume",
        "one_line": "Derive two expectations by linearity over pairs and over slots, find the even-odds collision point exactly, and name the quantity this library does not prove.",
        "summary": (
            "Throw `n` keys into `m` slots uniformly at random. The expected number of "
            "colliding pairs is `n(n − 1)/2m` and the expected number of empty slots is "
            "`m(1 − 1/m)ⁿ`, both by linearity of expectation over events that are not "
            "independent. The point where a collision becomes more likely than not is found "
            "by multiplying the exact product out. The maximum load is a different question "
            "and this library answers it nowhere."
        ),
        "key": [
            "E[colliding pairs] = n(n − 1)/2m      linearity over the C(n,2) pairs",
            "E[empty slots]     = m(1 − 1/m)ⁿ      linearity over the m slots",
            "23 keys, 365 slots: 253/365 pairs expected, one counted",
            "P(all 23 apart) = 0.492703…, so 23 is where the odds turn",
            "collisions start near √m, not near m",
            "max load at n = m: STATED, NOT PROVED anywhere in this library",
        ],
        "key_label": "Two exact expectations, one exact product, and one quantity nobody here proves",
        "concepts_intro": (
            "The hard idea is that linearity needs no independence, and here the events are "
            "visibly dependent. The other two are the exact product behind the birthday bound "
            "and the honest status of the maximum."
        ),
        "concepts": [
            ("Linearity over pairs, with no independence anywhere",
             "For each of the `C(n, 2)` pairs of keys, let `Xᵢⱼ` be `1` if they land in the same "
             "slot. Two keys land together with probability `1/m`, so `E[Xᵢⱼ] = 1/m`, and "
             "`E[Σ Xᵢⱼ] = C(n, 2)/m = n(n − 1)/2m` by linearity. The indicators are <em>not</em> "
             "independent &mdash; if `1` and `2` collide and `2` and `3` collide then `1` and `3` "
             "certainly do &mdash; and linearity does not care. That is the step most readers "
             "believe they need independence for."),
            ("Linearity over slots gives the empty count",
             "For each slot, let `Yⱼ` be `1` if it is empty. A given key misses a given slot with "
             "probability `1 − 1/m`, and the `n` keys are thrown independently, so "
             "`E[Yⱼ] = (1 − 1/m)ⁿ` and `E[Σ Yⱼ] = m(1 − 1/m)ⁿ`. At 23 keys in 365 slots that is "
             "`342.68`, and the seeded throw left `343` empty. The same technique, a different "
             "index set, and again no independence between the `Yⱼ` is needed or available."),
            ("The maximum is not an expectation, and it is not proved here",
             "With as many keys as slots the expected load per slot is `1`, and the "
             "<em>maximum</em> load is about `log n / log log n`. That result is quoted on the "
             "panel and labelled STATED, NOT PROVED, in those words, because its proof needs "
             "Chernoff bounds and this course excludes them. Beside it the panel puts the maximum "
             "it counted &mdash; `4` at 365 keys in 365 slots on this seed, against a stated "
             "figure of `3.32`. One of those two numbers was computed here."),
        ],
        "read_title": "Two expectations, one product, and a maximum nobody here derives",
        "read_intro": "The collision arithmetic behind every hash table on this path, with each quantity's standing stated next to it.",
        "body": [
            ("def", ("The model",
                     "`n` keys are thrown into `m` slots, each key landing in a uniformly random "
                     "slot, independently of the others. This is the idealisation a hash function "
                     "is assumed to realise; Universal Hashing is where the assumption is replaced "
                     "by something provable. A <strong>collision</strong> is a pair of keys in the "
                     "same slot, and the <strong>load</strong> of a slot is how many keys it "
                     "holds.")),
            ("thm", ("The expected number of colliding pairs",
                     "The expected number of unordered pairs of keys that land in the same slot is "
                     "`n(n − 1)/2m`, exactly, for every `n` and `m`.")),
            ("proof", ("Index the `C(n, 2) = n(n − 1)/2` unordered pairs. For a pair `{i, j}` let "
                       "`Xᵢⱼ = 1` if keys `i` and `j` land in the same slot and `0` otherwise. The "
                       "number of colliding pairs is `X = Σ Xᵢⱼ`.",
                       "Condition on where key `i` lands. Key `j` lands there with probability "
                       "`1/m` whatever that slot was, so `P(Xᵢⱼ = 1) = 1/m` and "
                       "`E[Xᵢⱼ] = 1/m`.",
                       "Linearity of expectation gives `E[X] = Σ E[Xᵢⱼ] = C(n, 2)·(1/m)`, which is "
                       "`n(n − 1)/2m`. The indicators are dependent &mdash; collision is transitive "
                       "&mdash; and linearity holds for dependent summands, so nothing here needs "
                       "repair.")),
            ("p", "At 23 keys in 365 slots that is `253/365 ≈ 0.693`, a number below one. The "
                  "seeded throw on the panel produced exactly one colliding pair. Change the seed "
                  "and the count moves between `0` and `3`; the expectation does not move at all, "
                  "and it is printed as the fraction `253/365` rather than as a decimal for the "
                  "same reason every other exact quantity on this course is."),
            ("thm", ("The expected number of empty slots",
                     "The expected number of slots holding no key is `m(1 − 1/m)ⁿ`, exactly.")),
            ("proof", ("For slot `j` let `Yⱼ = 1` if slot `j` is empty. A single key misses slot "
                       "`j` with probability `1 − 1/m`, and the `n` keys are independent of each "
                       "other, so all `n` miss it with probability `(1 − 1/m)ⁿ`.",
                       "So `E[Yⱼ] = (1 − 1/m)ⁿ`, and the expected number of empty slots is "
                       "`Σⱼ E[Yⱼ] = m(1 − 1/m)ⁿ` by linearity. The `Yⱼ` are dependent &mdash; if "
                       "`m − 1` slots are empty the last one is not &mdash; and again that costs "
                       "nothing.")),
            ("p", "Note which independence was used and which was not. Inside a single `Yⱼ` the "
                  "`n` keys are independent, and that is a genuine hypothesis of the model. "
                  "Between the `Yⱼ` nothing is assumed, and nothing is true. Keeping those two "
                  "apart is the whole skill: the first is about the throws, the second would be "
                  "about the slots, and only the first is available."),
            ("h3", "The birthday bound, multiplied out rather than estimated"),
            ("p", "The probability that all `n` keys land in distinct slots is the product "
                  "`(m/m)·((m − 1)/m)·…·((m − n + 1)/m)`, and the lab evaluates it as an exact "
                  "fraction over BigInt. At `m = 365` it first drops below a half at `n = 23`, "
                  "where it is `0.492703…`; so 23 keys make a collision more likely than not, and "
                  "22 do not. The familiar `√(2m ln 2) ≈ 22.5` is a rule of thumb, and the panel "
                  "does not use it &mdash; it searches upward through the exact product and "
                  "reports the first `n` that crosses."),
            ("example", ("Where collisions start, at three table sizes",
                         "`m = 64` slots: even odds at `n = 10`. `m = 128`: at `n = 14`. "
                         "`m = 365`: at `n = 23`. `m = 1000`: at `n = 38`. Each of those is close "
                         "to `√m` and nowhere near `m`. A table with a thousand slots is not "
                         "comfortable until far fewer than a thousand keys have arrived &mdash; it "
                         "sees its first collision at around forty, which is four per cent full.")),
            ("p", "This is why hash tables are engineered around load factors and chains rather "
                  "than around avoiding collisions. Collisions are not an anomaly to be designed "
                  "out; they are the expected state of a table that is a few per cent full, and "
                  "Hashing with Chaining spends its whole page on what to do about them."),
            ("h3", "The maximum load, and what this library will not claim"),
            ("p", "Throw `n` keys into `n` slots. The mean load is exactly `1`. The maximum load "
                  "is `Θ(log n / log log n)` with high probability, and if each key picks two "
                  "slots and takes the emptier the maximum drops to about `ln ln n`. Both of those "
                  "are quoted on the panel and both are labelled STATED, NOT PROVED. Their proofs "
                  "need Chernoff bounds, which no Subject in this library teaches, and stating a "
                  "result is not proving it."),
            ("p", "So the panel does the one honest thing available: it prints the stated figure "
                  "and the counted maximum in adjacent rows. At `m = 365` with 365 keys the stated "
                  "one-choice figure reads `3.32` and the seeded throw's tallest slot held `4`. "
                  "Those do not contradict each other &mdash; an asymptotic growth rate with "
                  "suppressed constants is not a prediction of a small instance &mdash; and the "
                  "gap is a reminder of what a growth rate is and is not."),
            ("p", "Partitioning and Load Balancing, on the System Design path, is where the "
                  "maximum load matters rather than the mean, because a shard's capacity is set by "
                  "its busiest moment. That course measures the same two quantities on real "
                  "placements and quotes the same two asymptotics under the same caveat. Between "
                  "the two pages the expectations are derived once, here, and the maximum is "
                  "measured twice and derived nowhere."),
        ],
        "lab": ("hash", {
            "mode": "balls",
            "preset": "birthday",
            "panel_title": "Throw the keys, then read each row's standing",
            "panel_intro": (
                "The two expectations and the all-apart probability are exact fractions; the "
                "colliding pairs, empty slots and tallest slot are counted on the seeded throw "
                "beside them. The two maximum-load rows are neither: they are asymptotic results "
                "quoted from outside this library, and the panel labels them so."
            ),
        }),
        "steps_title": "Counting with indicators",
        "steps_intro": "Choose the index set first. Everything else is one probability and a sum.",
        "steps": [
            ("Pick what you are summing over",
             "Pairs of keys for collisions, slots for emptiness, keys for something else. The "
             "choice fixes the size of the sum and is where almost all the difficulty is; the two "
             "results on this page differ only in that choice."),
            ("Compute one indicator's expectation",
             "`E[Xᵢⱼ] = P(the pair collides) = 1/m`. `E[Yⱼ] = P(slot j is empty) = (1 − 1/m)ⁿ`. "
             "This is one probability about one object, and it is where the model's independence "
             "assumption is used if it is used at all."),
            ("Add them up, and do not check for independence",
             "Linearity holds for dependent summands. If you find yourself arguing that the "
             "indicators are approximately independent, you have added a false premise to a proof "
             "that did not need one, and it will be false in the next example."),
            ("Say which quantity you have actually bounded",
             "An expectation over pairs is not a probability of a collision, and neither is a "
             "statement about the maximum. On this page all three are printed, they differ, and "
             "only the first two are computed here."),
        ],
        "worked": {
            "title": "Twenty-three keys into three hundred and sixty-five slots",
            "intro": [
                "The classic instance, with every quantity the panel prints and the standing of "
                "each. `n = 23`, `m = 365`, throw seed 4.",
            ],
            "lines": [
                "quantity                         value            standing",
                "  expected colliding pairs       253/365 = 0.6932  exact, linearity over pairs",
                "  colliding pairs this throw     1                 counted",
                "  expected empty slots           342.6800          exact, linearity over slots",
                "  empty slots this throw         343 of 365        counted",
                "  P(all 23 land apart)           0.492703…         exact product",
                "  so P(some pair collides)       0.507297…         exact, one minus the above",
                "  tallest slot this throw        2                 counted",
                "",
                "AT n = m = 365, a different question",
                "  log n / log log n              3.32              STATED, NOT PROVED",
                "  ln ln n, with two choices       1.78              STATED, NOT PROVED",
                "  tallest slot, counted           4                 counted, on this seed",
            ],
            "after": [
                "The expected number of colliding pairs is below one and yet a collision is more "
                "likely than not: `0.693` against `0.507`. There is no contradiction &mdash; the "
                "first is an expected count and the second is a probability of a count being at "
                "least one &mdash; but the pair of numbers is a good test of whether the "
                "distinction has landed. Markov's inequality, from the previous lesson, even "
                "relates them: `P(X ≥ 1) ≤ E[X]/1 = 0.693`, and the truth is `0.507`.",
                "The empty-slot figure is the one that surprises people in the other direction. "
                "343 of 365 slots empty after 23 throws is obvious once said and rarely predicted, "
                "and it is the same arithmetic that makes a hash table's memory cost real: most of "
                "the table is doing nothing at low load.",
                "For a faded rehearsal, set the slots to 128 and predict the even-odds point "
                "before moving the keys slider. The supplied first move is this: it is near `√m`, "
                "and `√128 ≈ 11.3`. Say whether the true answer is above or below that, then find "
                "it &mdash; and then say why `n(n − 1)/2m = 1` gives yet another nearby number, "
                "and which of the three questions each one answers.",
            ],
        },
        "quiz_title": "Indicators, independence, and standing",
        "quiz": [
            {"q": "The derivation of `n(n − 1)/2m` sums indicators that are not independent. What repairs the argument?",
             "a": ["Nothing needs repairing: linearity of expectation holds for dependent summands",
                   "The indicators are approximately independent for large `m`",
                   "Inclusion–exclusion over the dependencies",
                   "The pairs must be chosen in advance to make them independent"],
             "c": 0,
             "why": "`E[X + Y] = E[X] + E[Y]` is true for any two random variables with finite "
                    "expectations, dependent or not. Collision is transitive, so the indicators "
                    "here are strongly dependent, and the sum is still exactly `C(n,2)/m`. "
                    "Reaching for approximate independence adds a false premise to a proof that "
                    "was already complete."},
            {"q": "`E[colliding pairs] = 0.693` at 23 keys in 365 slots, and `P(some collision) = 0.507`. How do these fit together?",
             "a": ["They contradict each other, so one is a measurement",
                   "An expected count and a probability of at least one are different quantities; Markov even gives `P(X ≥ 1) ≤ 0.693`",
                   "The first is the second rounded",
                   "The first counts ordered pairs and the second unordered ones"],
             "c": 1,
             "why": "`X` is a count and `P(X ≥ 1)` is the probability that it is nonzero. They "
                    "agree only when `X` is always 0 or 1. Markov's inequality with `a = 1` gives "
                    "`P(X ≥ 1) ≤ E[X]`, which is `0.507 ≤ 0.693` here — true, and loose, as usual."},
            {"q": "What is the standing of `log n / log log n` on this page?",
             "a": ["Proved in this lesson from the indicator argument",
                   "Proved in Partitioning and Load Balancing and quoted here",
                   "Stated and proved nowhere in this library, because its proof needs Chernoff bounds",
                   "A measurement averaged over the seeds the panel ran"],
             "c": 2,
             "why": "The panel labels the row STATED, NOT PROVED. This course excludes Chernoff "
                    "bounds, which the proof requires, and the System Design page that also quotes "
                    "the result carries the same caveat. What both pages do instead is count the "
                    "tallest bin on a placement and print it in the next row."},
            {"q": "A table has 1 000 slots. About how many keys before a collision is more likely than not?",
             "a": ["About 500", "About 38", "About 1 000", "About 100"],
             "c": 1,
             "why": "The even-odds point sits near `√m`, and the exact product crosses a half at "
                    "`n = 38` for `m = 1000`. That is under four per cent of the table. Collisions "
                    "are the normal condition of a lightly loaded table, which is why chaining and "
                    "probing exist rather than schemes that try to avoid them."},
        ],
        "mistakes": [
            ("Claiming independence to justify linearity",
             "Linearity of expectation never needs it, and the indicators here are visibly "
             "dependent: three keys that pairwise collide cannot have independent collision "
             "indicators. Asserting independence makes the proof wrong even though the answer is "
             "right, and the next problem is one where the answer is wrong too."),
            ("Confusing the expected number of collisions with the chance of a collision",
             "At 23 keys in 365 slots those are `0.693` and `0.507`. They move together and they "
             "are not the same, and the gap widens as soon as more than one collision becomes "
             "likely. Say which one a design decision needs before quoting either."),
            ("Treating the maximum load as though it followed from the mean",
             "The mean load at `n = m` is exactly `1` and the maximum is around `log n / log log n`, "
             "which is `3.32` at 365 and was counted as `4`. An expectation says nothing about a "
             "maximum, this library proves nothing about this one, and a capacity plan that sizes "
             "for the mean is sizing for the wrong number."),
        ],
        "standard": ("Finish when you can compute an expected count by choosing an index set and summing one probability.",
                     "You should be able to derive both results on this page from indicators, say "
                     "exactly where independence was and was not used, distinguish an expected "
                     "count from the probability of at least one, and state the standing of every "
                     "row the panel prints."),
        "note": ("The model here gives each key a uniformly random slot, which no real hash "
                 "function does. &ldquo;Universal Hashing&rdquo; replaces the assumption with a "
                 "provable one: a family of functions such that any fixed pair of keys collides "
                 "with probability at most `1/m` when the function is drawn at random &mdash; "
                 "which is enough for every expectation on this page and is a guarantee about "
                 "keys chosen by an adversary."),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "universal-hashing",
        "title": "Universal Hashing",
        "module": "Expectation, and what it does not assume",
        "one_line": "Move the randomness from the keys to the choice of hash function, and get a collision bound that holds for keys an adversary picked.",
        "summary": (
            "Every expectation about a hash table assumes something about the keys, and an "
            "adversary who can see your hash function can break the assumption. A universal "
            "family removes it: choose the function at random, and any fixed pair of distinct "
            "keys collides with probability at most `1/m`, whichever pair it is. The lab "
            "counts every function in the family for a pair you choose, and the fraction is "
            "an exact count rather than a sample."
        ),
        "key": [
            "a family H is universal if P(h(x) = h(y)) ≤ 1/m for every x ≠ y, h drawn from H",
            "hₐ,ᵦ(k) = ((ak + b) mod p) mod m,  p prime,  a in 1..p−1,  b in 0..p−1",
            "p = 11, m = 4: 110 functions, the pair 3 and 7 collides in 20 of them",
            "20/110 = 2/11 = 0.1818… against the bound 1/4",
            "fix one function h(k) = k mod 4 and the pair 1 and 5 collides with probability 1",
            "the randomness is in the CHOICE OF FUNCTION, not in the keys",
        ],
        "key_label": "One definition, one family, and the adversary it defeats",
        "concepts_intro": (
            "The hard idea is where the randomness lives. The other two are the definition it "
            "makes possible and the guarantee that definition is worth."
        ),
        "concepts": [
            ("The randomness moves from the data to the algorithm",
             "&ldquo;Balls in Bins and the Birthday Bound&rdquo; assumed the keys were thrown "
             "uniformly at random. That is an assumption about the input, and an input can refuse "
             "to satisfy it &mdash; keys that are all multiples of `m` under `h(k) = k mod m`, for "
             "instance. A universal family makes no assumption about the keys at all: the keys are "
             "whatever they are, possibly chosen by someone who has read your code, and the "
             "<strong>function</strong> is what is drawn at random."),
            ("The definition, and what it does not say",
             "A family `H` of functions from keys to `0..m−1` is <strong>universal</strong> if for "
             "every pair of distinct keys `x` and `y`, a uniformly random `h` from `H` has "
             "`P(h(x) = h(y)) ≤ 1/m`. It says nothing about three keys, nothing about the shape of "
             "the whole table, and nothing about any particular `h` &mdash; some member of the "
             "family maps everything to one slot, and that is allowed. It is a statement about "
             "pairs, averaged over the family."),
            ("A pairwise bound is enough for a chain length",
             "That is why pairs are the right thing to bound. The expected length of the chain "
             "holding key `x` is `1 + Σ` over the other `n − 1` keys of `P(h(y) = h(x))`, which is "
             "at most `1 + (n − 1)/m` by universality and linearity. No independence between pairs "
             "is needed, which is fortunate, because a universal family need not provide any."),
        ],
        "read_title": "A guarantee that survives an adversary",
        "read_intro": "The definition, one family that meets it, the exact count over every member, and what a fixed function loses.",
        "body": [
            ("p", "Start with what goes wrong. Take `h(k) = k mod 8`, a perfectly reasonable hash "
                  "function, and hand it to someone who wants the table to perform badly. They "
                  "insert `8, 16, 24, 32, …`. Every key lands in slot `0`, every lookup walks the "
                  "whole chain, and the table's average-case analysis was about a distribution of "
                  "keys that this input is not from. Hashing with Chaining shows that instance "
                  "running; this lesson is what to do about it."),
            ("def", ("A universal family",
                     "Let `U` be the set of possible keys and `m` the number of slots. A finite "
                     "family `H` of functions `U → {0, …, m − 1}` is <strong>universal</strong> if "
                     "for every pair of distinct keys `x ≠ y` in `U`, "
                     "`P(h(x) = h(y)) ≤ 1/m` when `h` is drawn uniformly at random from `H`. The "
                     "probability is over the choice of `h` only; `x` and `y` are fixed first, and "
                     "may be chosen by an adversary who knows `H`.")),
            ("p", "The order of quantifiers is the content of the definition. For every pair, the "
                  "average over functions is small. Not: for every function, most pairs are fine "
                  "&mdash; that would be a much weaker statement and it is what a fixed hash "
                  "function offers. The adversary is allowed to pick the pair after seeing the "
                  "family, and is not allowed to see the coin that picks `h`."),
            ("def", ("The multiply-shift family",
                     "Fix a prime `p` larger than every key. For `a` in `1..p − 1` and `b` in "
                     "`0..p − 1`, let `hₐ,ᵦ(k) = ((a·k + b) mod p) mod m`. The family is all "
                     "`p(p − 1)` of these functions, and drawing `h` uniformly means drawing `a` "
                     "and `b` uniformly.")),
            ("thm", ("The multiply-shift family is universal",
                     "For distinct keys `x` and `y` below `p`, a uniformly chosen `hₐ,ᵦ` has "
                     "`P(hₐ,ᵦ(x) = hₐ,ᵦ(y)) ≤ 1/m`.")),
            ("proof", ("Work modulo `p`, which is a field because `p` is prime. Write "
                       "`r = (ax + b) mod p` and `s = (ay + b) mod p`. As `(a, b)` ranges over the "
                       "`p(p − 1)` allowed pairs, `(r, s)` ranges over all `p(p − 1)` pairs with "
                       "`r ≠ s`, each exactly once: given `r ≠ s`, solving "
                       "`r − s = a(x − y)` for `a` is possible and unique because `x − y` is "
                       "invertible modulo `p`, and `b` is then determined.",
                       "So the question becomes: for how many pairs `r ≠ s` is "
                       "`r mod m = s mod m`? For each of the `p` choices of `r`, the values `s` "
                       "congruent to it modulo `m` and different from it number at most "
                       "`⌈p/m⌉ − 1 ≤ (p − 1)/m`.",
                       "That gives at most `p(p − 1)/m` colliding pairs out of `p(p − 1)`, so the "
                       "probability is at most `1/m`.")),
            ("p", "The lab does not take that proof on trust: it enumerates. At `p = 11` and "
                  "`m = 4` the family has `10 × 11 = 110` functions, and for the pair `3` and `7` "
                  "exactly `20` of them collide. That is `2/11 ≈ 0.1818`, comfortably under the "
                  "bound `1/4`. Change the pair and the count changes; over every pair of distinct "
                  "keys below `11`, the worst is still `2/11`, so this family does better than "
                  "universality requires on this instance."),
            ("example", ("Three instances, counted in full",
                         "`p = 11, m = 4`, pair `3` and `7`: 20 collisions in 110 functions, "
                         "`2/11 = 0.1818`, bound `1/4`. `p = 7, m = 3`, pair `1` and `4`: 10 in "
                         "42, `5/21 = 0.2381`, bound `1/3`. `p = 13, m = 5`, pair `2` and `9`: 22 "
                         "in 156, `11/78 = 0.1410`, bound `1/5`. Every one of those is a complete "
                         "enumeration of the family, not a sample of it.")),
            ("h3", "What is bought, stated carefully"),
            ("p", "The guarantee is about a pair fixed before the coin is flipped, and it holds "
                  "for every such pair. So a table built on a universal family has an expected "
                  "chain length of at most `1 + (n − 1)/m` <em>for every input</em>, including "
                  "inputs constructed to be bad. The expectation is over the choice of `h`, and it "
                  "is the same guarantee that &ldquo;Randomised Quicksort&rdquo; gets from a "
                  "random pivot: the input is arbitrary, the coins are the algorithm's, and the "
                  "average is over the coins."),
            ("p", "What is not bought is any promise about the particular `h` you drew. Some member "
                  "of the family is terrible for your keys, and you may have drawn it. The "
                  "guarantee says that is unlikely, in the precise sense that the average over the "
                  "family is small; if the table turns out slow you re-draw `h` and rebuild, and "
                  "that is a real operation with a real cost. A guarantee in expectation is not a "
                  "guarantee per instance, which is the same distinction &ldquo;The Cost Is a "
                  "Distribution&rdquo; drew for a comparison count."),
            ("h3", "The fixed function, and the adversary"),
            ("p", "Set the comparison the other way. Fix `h(k) = k mod 4` and let the adversary "
                  "choose. They pick `1` and `5`, which are congruent modulo `4`, and those two "
                  "keys collide with probability `1` &mdash; certainty, not `1/4`. The panel prints "
                  "that row beside the counted rate, and the contrast is the entire argument for "
                  "the family: `2/11` against `1`, on keys the adversary chose in both cases."),
            ("p", "There is a cost, and it is worth naming. Every lookup now computes a "
                  "multiplication, an addition and two remainders instead of one remainder, and "
                  "the table must store `a`, `b` and `p`. Whether that is worth paying depends on "
                  "whether anyone can choose your keys, which is a question about the system "
                  "rather than about the algorithm &mdash; and it is the reason a compiler's "
                  "symbol table and a public web service make different choices here."),
        ],
        "lab": ("hash", {
            "mode": "universal",
            "preset": "p11-m4",
            "panel_title": "Pick a pair of keys and count every function in the family",
            "panel_intro": (
                "The collision rate is a count over every member of the family, not a sample of "
                "it, so it is an exact fraction. Choose the pair as adversarially as you like: the "
                "bound is a statement about every pair, and the grid shows all of them at once."
            ),
        }),
        "steps_title": "Reading a guarantee that quantifies over inputs",
        "steps_intro": "Check what is fixed, what is random, and in what order.",
        "steps": [
            ("Say what the probability is over",
             "Here it is over the choice of `h`, with `x` and `y` fixed first. Every sentence about "
             "universal hashing is wrong if that is reversed, and the reversal is the natural "
             "reading of the phrase &ldquo;the probability that two keys collide&rdquo;."),
            ("Try to break it by choosing the pair last",
             "Move the two key sliders to whatever looks worst. The counted rate stays under `1/m` "
             "because the definition quantifies over pairs. Then fix a single function and try the "
             "same thing: the panel shows the pair that collides with certainty."),
            ("Use the bound only on pairs",
             "Universality bounds pair collisions and nothing else. An expected chain length "
             "follows by linearity over pairs; a claim about the maximum chain, or about three "
             "keys landing together, does not follow and needs a stronger property."),
            ("Price the cost before adopting it",
             "Two modular reductions per lookup and three stored constants, in exchange for a "
             "guarantee that survives chosen keys. Decide whether anything in the system can "
             "choose the keys; if nothing can, the guarantee is buying insurance against an event "
             "that cannot occur."),
        ],
        "worked": {
            "title": "Every function in the family, for one pair",
            "intro": [
                "`p = 11`, `m = 4`, keys `x = 3` and `y = 7`. The family has `10` choices of `a` "
                "and `11` of `b`, so 110 functions, and the question is how many of them put `3` "
                "and `7` in the same slot.",
            ],
            "lines": [
                "  a   b   (3a+b) mod 11   h(3)   (7a+b) mod 11   h(7)",
                "  1   0        3            3         7            3    collides",
                "  1   1        4            0         8            0    collides",
                "  1   2        5            1         9            1    collides",
                "  1   3        6            2        10            2    collides",
                "  1   4        7            3         0            0    separate",
                "  1   5        8            0         1            1    separate",
                "  1   6        9            1         2            2    separate",
                "  1   7       10            2         3            3    separate",
                "  1   8        0            0         4            0    collides",
                "  1   9        1            1         5            1    collides",
                "  1  10        2            2         6            2    collides",
                " …   …        …            …         …            …",
                "",
                "  the a = 1 block alone                7 of 11 collide",
                "  a = 3, 4, 5, 6, 7 and 8              0 of 11 collide, each",
                "  a = 2 and a = 9                      3 of 11 each",
                "  a = 10                               7 of 11",
                "  collisions over all 110 functions   20",
                "  rate   20/110 = 2/11 = 0.1818…      bound 1/m = 1/4 = 0.25",
                "",
                "  by contrast, the fixed function h(k) = k mod 4",
                "  adversary picks 1 and 5:  both land in slot 1, probability 1",
            ],
            "after": [
                "Look at the `a = 1` block alone: seven collisions out of eleven, a rate far above "
                "`1/4`. Universality is not a promise about any one value of `a`; it is a promise "
                "about the average, and six of the ten values of `a` collide on this pair not once "
                "in eleven, which is what brings the total to 20. Reading a guarantee about an "
                "average as a guarantee about every member is the mistake this table is laid out "
                "to make visible.",
                "Notice also that the rate came out `2/11` rather than `1/4`. The bound is an "
                "inequality and this family clears it with room to spare on this instance; "
                "`⌈p/m⌉ − 1` in the proof is `2` here while `(p − 1)/m` is `2.5`, so the counting "
                "step gave away a little. A bound that is met with slack is the normal case, and "
                "the lab prints both numbers so the slack is visible rather than assumed away.",
                "For a faded rehearsal, switch to `p = 7`, `m = 3` and predict the collision count "
                "before reading it. The supplied first move is this: the family has `6 × 7 = 42` "
                "members and the bound is `1/3`, so at most 14 of them may collide. Say how many "
                "actually do, then check &mdash; and then say why the answer does not depend on "
                "which pair of distinct keys you picked, on this particular `p` and `m`.",
            ],
        },
        "quiz_title": "Where the randomness lives",
        "quiz": [
            {"q": "In the definition of a universal family, what is the probability over?",
             "a": ["The choice of keys, with the function fixed",
                   "The choice of function, with the pair of keys fixed first",
                   "Both, chosen independently",
                   "The order in which the keys are inserted"],
             "c": 1,
             "why": "The keys are fixed first — an adversary may choose them knowing the family — "
                    "and then `h` is drawn uniformly. Reversing the order gives the much weaker "
                    "statement a fixed hash function already satisfies, and it is the statement an "
                    "adversary breaks by choosing keys congruent modulo `m`."},
            {"q": "The panel counts 20 collisions among the 110 functions of the `p = 11`, `m = 4` family, for the pair 3 and 7. What does the 20 establish?",
             "a": ["That `2/11 ≤ 1/4` holds for this pair, exactly, by complete enumeration",
                   "That the family is universal, since one pair was checked",
                   "An estimate of the true rate, with sampling error",
                   "That every function in the family is good for this pair"],
             "c": 0,
             "why": "The count is over the whole family, so the rate is exact for this pair, not "
                    "an estimate. Universality is a claim about every pair and is established by "
                    "the proof; the lab lets you try other pairs and watch the bound hold, which "
                    "is evidence for the proof rather than a substitute. And it is certainly not a "
                    "claim about each function: at `a = 1` the rate is above a half."},
            {"q": "Why is a bound on pairs enough to bound an expected chain length?",
             "a": ["Because collisions between different pairs are independent",
                   "Because the chain length is a sum of pair indicators, and linearity needs no independence",
                   "Because the maximum chain equals the expected chain",
                   "It is not enough; a further assumption is needed"],
             "c": 1,
             "why": "The chain holding `x` has length `1 + Σ` over other keys `y` of the indicator "
                    "that `h(y) = h(x)`, each with expectation at most `1/m`. Linearity adds them "
                    "to at most `1 + (n − 1)/m` whether or not they are independent — which is the "
                    "same move &ldquo;Balls in Bins and the Birthday Bound&rdquo; makes over pairs."},
            {"q": "What does universal hashing NOT promise?",
             "a": ["A bound on the expected chain length for every input",
                   "That the bound survives keys chosen by an adversary",
                   "That the particular function you drew is good for your keys",
                   "That any fixed pair collides with probability at most `1/m`"],
             "c": 2,
             "why": "The guarantee is an average over the family. Some member is bad for your "
                    "keys and you may have drawn it; the remedy is to re-draw and rebuild, which "
                    "costs something real. This is the same gap between an expectation and a "
                    "particular execution that runs through the whole course."},
        ],
        "mistakes": [
            ("Reading universality as a property of one hash function",
             "No single function is universal; the word describes a family. The `p = 11`, `m = 4` "
             "family contains members that collide on the chosen pair for seven of eleven values of "
             "`b`, and the family is still universal because the average over all 110 members is "
             "`2/11`. A sentence beginning &ldquo;this hash function is universal&rdquo; has "
             "already lost the definition."),
            ("Assuming the keys are random when the point is that they are not",
             "Every expectation on the preceding page assumed uniformly thrown keys. Universal "
             "hashing exists precisely because that assumption is about the input and inputs can "
             "be hostile. Quoting a chain-length bound while silently keeping the random-keys "
             "assumption is quoting the weaker result under the stronger name."),
            ("Expecting the counted rate to equal 1/m",
             "It is `2/11` here against a bound of `1/4`, and `11/78` against `1/5` at `p = 13`. "
             "Universality is an inequality and the families that satisfy it usually do better "
             "than required on any given pair. A rate below the bound is the bound working, not "
             "the enumeration disagreeing with the theorem."),
        ],
        "standard": ("Finish when you can state the definition with the quantifiers in the right order and say what it buys.",
                     "You should be able to define a universal family, verify the multiply-shift "
                     "family meets it, derive the expected chain length from pairwise collisions "
                     "and linearity, and say precisely what the guarantee does not cover about the "
                     "function you happened to draw."),
        "note": ("The same structural move &mdash; randomise the algorithm rather than assume "
                 "something about the input &mdash; is what a random pivot does for quicksort and "
                 "what a random priority does for a search tree. &ldquo;Treaps&rdquo; is that "
                 "third case: the keys arrive in whatever order they arrive, and the shape of the "
                 "tree is decided by coins the structure flipped itself."),
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "the-probabilistic-method",
        "title": "The Probabilistic Method",
        "module": "Expectation, and what it does not assume",
        "one_line": "Prove that a good object exists by showing the average is good, then check the claim against every assignment the formula has.",
        "summary": (
            "A uniformly random assignment satisfies `7m/8` of the clauses of a 3-CNF "
            "formula, in expectation, because each clause on three distinct variables is "
            "satisfied by 7 of its 8 local assignments and expectations add. Since some "
            "value is at least the average, an assignment satisfying at least `7m/8` clauses "
            "must exist &mdash; a proof of existence that constructs nothing. The lab "
            "enumerates every assignment and shows which ones do worse."
        ),
        "key": [
            "each clause on three DISTINCT variables is satisfied by 7 of its 8 assignments",
            "E[satisfied] = Σ P(clause j satisfied) = 7m/8      linearity, not independence",
            "some value is at least the average, so such an assignment EXISTS",
            "four clauses: mean 7/2, and 7m/8 = 7/2 exactly",
            "4 of the 8 assignments are BELOW the mean",
            "the ratio is mean/OPTIMUM = 7/8, not mean/m",
        ],
        "key_label": "One expectation, one existence proof, and the assignments that miss",
        "concepts_intro": (
            "The hard idea is that an average proves an existence. The other two are why the "
            "expectation needs no independence and why the ratio is against the optimum."
        ),
        "concepts": [
            ("A clause is satisfied by seven of its eight local assignments",
             "Take a clause on three <em>distinct</em> variables, say `x₁ ∨ x₂ ∨ ¬x₃`. Fixing the "
             "three variables gives 8 possibilities and exactly one falsifies the clause: the one "
             "that makes every literal false. So `P(clause satisfied) = 7/8` when the assignment "
             "is uniformly random, whatever the signs are. The lab computes this per clause, from "
             "the clause's own variables, and prints it as a share."),
            ("Linearity adds the clauses, sharing variables and all",
             "Let `Zⱼ` be `1` if clause `j` is satisfied. The number satisfied is `Σ Zⱼ`, so "
             "`E[Σ Zⱼ] = Σ E[Zⱼ] = 7m/8`. The clauses overlap heavily &mdash; the lab's opening "
             "formula has four clauses on three variables, so every pair shares two of them "
             "&mdash; and the `Zⱼ` are strongly dependent. Linearity is indifferent, which is why "
             "this argument is two lines rather than an inclusion&ndash;exclusion."),
            ("An average proves an existence, and constructs nothing",
             "A random variable cannot always be strictly below its own expectation, so some "
             "assignment satisfies at least `7m/8` clauses. That is a complete existence proof and "
             "it names no assignment: the lab has to enumerate all `2ⁿ` of them to say which one. "
             "The gap between &ldquo;one exists&rdquo; and &ldquo;here it is&rdquo; is the whole "
             "difference between this argument and an algorithm."),
        ],
        "read_title": "An existence proof made of an average",
        "read_intro": "The 7m/8 bound, the linearity that gets it, the existence it proves, and the distribution it says nothing about.",
        "body": [
            ("def", ("MAX-3-SAT",
                     "A <strong>3-CNF formula</strong> is a conjunction of `m` clauses, each a "
                     "disjunction of three literals, where a literal is a variable or its "
                     "negation. <strong>MAX-3-SAT</strong> asks for the assignment satisfying as "
                     "many clauses as possible. The lab writes a clause as three signed integers, "
                     "so `1 2 -3` is `x₁ ∨ x₂ ∨ ¬x₃`, and separates clauses with a semicolon.")),
            ("thm", ("The expectation of a uniformly random assignment",
                     "Let `F` have `m` clauses, each on three distinct variables. Setting every "
                     "variable to true or false independently with probability `1/2` satisfies "
                     "`7m/8` clauses in expectation, exactly, whatever the clauses are and however "
                     "much they overlap.")),
            ("proof", ("Fix a clause `j`. Its three literals involve three distinct variables, so "
                       "the eight assignments to those three variables are equally likely under "
                       "the random assignment. Exactly one of the eight makes all three literals "
                       "false, namely the one setting each variable against its literal's sign. So "
                       "`P(Zⱼ = 1) = 7/8` and `E[Zⱼ] = 7/8`.",
                       "The number of satisfied clauses is `Z = Σⱼ Zⱼ`. By linearity of "
                       "expectation, `E[Z] = Σⱼ E[Zⱼ] = m·(7/8) = 7m/8`, with no assumption about "
                       "how the clauses share variables.")),
            ("thm", ("The existence claim",
                     "Every 3-CNF formula with `m` clauses, each on three distinct variables, has "
                     "an assignment satisfying at least `⌈7m/8⌉` clauses.")),
            ("proof", ("`Z` takes finitely many values with total probability `1`. If every value "
                       "were strictly less than `E[Z]`, then `E[Z]` would be a weighted average of "
                       "numbers all strictly below it, which is impossible. So some assignment has "
                       "`Z ≥ E[Z] = 7m/8`, and since `Z` is an integer it satisfies at least "
                       "`⌈7m/8⌉` clauses.")),
            ("p", "That is the <strong>probabilistic method</strong> in its simplest form: to show "
                  "an object with a property exists, put a distribution on the objects and show "
                  "the property holds on average. Nothing in it is constructive. The proof holds "
                  "for a formula with a thousand variables, and finding the assignment it promises "
                  "is a different problem, which Intractability and Approximation takes up."),
            ("example", ("Four clauses on three variables",
                         "`x₁ ∨ x₂ ∨ ¬x₃`, `¬x₁ ∨ x₂ ∨ x₃`, `x₁ ∨ ¬x₂ ∨ x₃`, "
                         "`¬x₁ ∨ ¬x₂ ∨ ¬x₃`. Each clause has three distinct variables, so each "
                         "contributes `7/8` and the mean is `4 × 7/8 = 7/2`, which is what "
                         "`7m/8` predicts. Enumerating all 8 assignments confirms it: four of "
                         "them satisfy 3 clauses and four satisfy 4, and the mean of that is "
                         "`7/2` exactly.")),
            ("p", "The clause table on the panel is the proof performed rather than quoted: each "
                  "row computes that clause's own satisfying fraction over its own variables, and "
                  "the last row adds the four shares and checks the total against the mean over "
                  "all assignments. Two independent computations of the same number &mdash; one by "
                  "linearity clause by clause, one by enumerating every assignment &mdash; and "
                  "they agree."),
            ("h3", "What the expectation does not say"),
            ("p", "It does not say a random assignment satisfies `7/2` clauses; no assignment "
                  "satisfies half a clause. It does not say most assignments are at or above the "
                  "mean: here exactly four of the eight are below it, a probability of `1/2`. And "
                  "it does not say the best assignment is anywhere near the mean. Those are three "
                  "separate facts and the lab prints all three because the expectation on its own "
                  "invites all three mistakes."),
            ("p", "The measured column makes the first point concrete. Over 120 seeded coin flips "
                  "the mean came out `139/40 = 3.475` against an expectation of `3.5`, with every "
                  "individual run landing on 3 or 4. The sample mean is close and it is not the "
                  "expectation, and it is the average of integers each of which is not `3.5`."),
            ("h3", "The ratio is against the optimum, not against m"),
            ("p", "A randomised algorithm that outputs a uniformly random assignment is a "
                  "`7/8`-approximation for MAX-3-SAT, and the word `7/8` is a ratio to the "
                  "<strong>optimum</strong>, not to `m`. On this formula the optimum is 4 and the "
                  "mean is `7/2`, so the ratio is `7/8` and the two coincide, because the formula "
                  "is satisfiable. Change the formula and they part."),
            ("p", "Take all eight clauses on three variables. The formula is unsatisfiable: every "
                  "assignment falsifies exactly one clause, so every assignment satisfies exactly "
                  "7 and the optimum is 7, not 8. The mean is `7m/8 = 7` as well, so the ratio "
                  "against the optimum is `1` while the ratio against `m` would be `7/8`. The "
                  "panel prints the optimum it found by enumeration beside the ratio, because a "
                  "ratio printed without the thing it is a ratio to is not a ratio."),
            ("p", "And take eight clauses on five variables: the mean is `7`, the optimum is `8`, "
                  "and 9 of the 32 assignments do worse than the mean. That instance is the one to "
                  "keep in mind, because it is the shape the guarantee is really about &mdash; a "
                  "satisfiable formula where the average is genuinely below the best, and the gap "
                  "is what an algorithm has to close."),
        ],
        "lab": ("random", {"mode": "max3sat", "preset": "four"}),
        "steps_title": "Using an average as a proof",
        "steps_intro": "Establish the average, then take one step, then stop — the step after that is a different problem.",
        "steps": [
            ("Compute the expectation clause by clause",
             "One clause, its own variables, its own satisfying fraction. Do not try to reason "
             "about the formula as a whole; the point of linearity is that you never have to."),
            ("Add the shares, and resist checking independence",
             "The clauses share variables and their indicators are dependent. Linearity applies "
             "anyway. If a step in your argument needs the clauses to be independent, it is not "
             "this argument."),
            ("Take exactly one step to existence",
             "Some value is at least the average. That gives an object and does not give a way to "
             "find it, and the sentence after it should not pretend otherwise."),
            ("Name the optimum before quoting a ratio",
             "`7/8` is the mean over the best possible, and on an unsatisfiable formula the best "
             "possible is below `m`. The lab enumerates to find it. A ratio computed against `m` "
             "flatters the algorithm on exactly the instances where it matters."),
        ],
        "worked": {
            "title": "Every assignment of the four-clause formula",
            "intro": [
                "`x₁ ∨ x₂ ∨ ¬x₃`, `¬x₁ ∨ x₂ ∨ x₃`, `x₁ ∨ ¬x₂ ∨ x₃`, `¬x₁ ∨ ¬x₂ ∨ ¬x₃`. Eight "
                "assignments, and the mean of the last column is the thing the theorem predicts.",
            ],
            "lines": [
                "x1 x2 x3   c1  c2  c3  c4    satisfied",
                " F  F  F    1   1   1   1        4",
                " F  F  T    0   1   1   1        3",
                " F  T  F    1   1   0   1        3",
                " F  T  T    1   1   1   1        4",
                " T  F  F    1   0   1   1        3",
                " T  F  T    1   1   1   1        4",
                " T  T  F    1   1   1   1        4",
                " T  T  T    1   1   1   0        3",
                "                              ----",
                "  total                          28  over 8 assignments",
                "  mean   = 28/8 = 7/2",
                "  7m/8   = 7*4/8 = 7/2            agrees",
                "  by clause: 7/8 + 7/8 + 7/8 + 7/8 = 7/2   agrees again",
                "  optimum = 4,  below the mean: 4 of 8,  ratio 7/2 over 4 = 7/8",
                "  measured over 120 seeds: 139/40 = 3.475, range 3 to 4",
            ],
            "after": [
                "Four assignments reach 4 and four reach 3. The existence claim asks for one "
                "reaching `⌈7/2⌉ = 4` and there are four of them, which is much more than the "
                "proof promised &mdash; the proof only ever promises one, and on a formula where "
                "the distribution is lopsided it may be promising exactly one.",
                "The three routes to `7/2` are worth separating. The column of eight integers "
                "averaged is an enumeration over assignments. The sum of four `7/8` shares is "
                "linearity over clauses. `7m/8` is the closed form. They agree because the clauses "
                "all have three distinct variables, and the next lesson is what happens when one "
                "of them does not.",
                "For a faded rehearsal, add the clause `x₁ ∨ x₂ ∨ x₃` to the formula and predict "
                "the new mean before the panel redraws. The supplied first move is this: the new "
                "clause has three distinct variables, so it contributes `7/8` like the others, and "
                "`m` is now 5. Say what the mean becomes, then say whether the optimum is still 4 "
                "&mdash; and check both.",
            ],
        },
        "quiz_title": "Averages, existence, and ratios",
        "quiz": [
            {"q": "Why does `E[Z] = 7m/8` hold even though the clauses share variables?",
             "a": ["Because the clauses are independent when the variables are uniform",
                   "Because linearity of expectation does not require independence",
                   "Because sharing variables makes the indicators positively correlated, which does not change the mean",
                   "It does not hold in general; the lab's formula is a special case"],
             "c": 1,
             "why": "`E[ΣZⱼ] = ΣE[Zⱼ]` for any random variables with finite expectations. Each "
                    "`E[Zⱼ]` is `7/8` because one of the eight local assignments falsifies the "
                    "clause. The overlap between clauses affects the variance and the shape of the "
                    "distribution and leaves the mean alone."},
            {"q": "The existence proof shows an assignment satisfying at least `⌈7m/8⌉` clauses exists. What does it give you?",
             "a": ["An algorithm that finds it in polynomial time",
                   "The assignment itself, once the expectation is computed",
                   "Only that one exists; finding it is a separate problem",
                   "A proof that the formula is satisfiable"],
             "c": 2,
             "why": "The argument is that a value cannot always be below its own average. It names "
                    "no assignment and constructs nothing, and the lab has to enumerate all `2ⁿ` "
                    "to report which assignments achieve it. Nor does it show satisfiability: the "
                    "eight-clause instance has every assignment satisfying exactly 7 of 8."},
            {"q": "On the all-eight-clauses formula the mean is 7, the optimum is 7, and `m` is 8. What is the approximation ratio a random assignment earns?",
             "a": ["`7/8`, the mean over `m`",
                   "`1`, the mean over the optimum",
                   "`0`, since the formula is unsatisfiable",
                   "Undefined, because the optimum is not `m`"],
             "c": 1,
             "why": "A ratio is measured against the best achievable, which enumeration finds to "
                    "be 7. The mean is 7 as well, so the random assignment is optimal in "
                    "expectation on this instance. Dividing by `m` instead would report `7/8` and "
                    "understate the algorithm — which is the same error in the other direction as "
                    "the one that flatters it on other instances."},
            {"q": "Four of the eight assignments satisfy 3 clauses, below the mean of `7/2`. What does that show?",
             "a": ["That the expectation is wrong",
                   "That the formula has a clause with a repeated variable",
                   "That an expectation says nothing about any particular draw, and half the draws here are below it",
                   "That a random assignment is a poor algorithm on this formula"],
             "c": 2,
             "why": "An expectation is a weighted average, and on this formula exactly half the "
                    "assignments fall below it. The existence proof needs only that not all of "
                    "them do. Whether a random assignment is a good algorithm is a separate "
                    "question, answered by the ratio `7/8` against the optimum."},
        ],
        "mistakes": [
            ("Treating the existence proof as an algorithm",
             "&ldquo;Some assignment reaches `7m/8`&rdquo; and &ldquo;here is an assignment "
             "reaching `7m/8`&rdquo; are different statements and the proof supplies only the "
             "first. The lab supplies the second by enumerating `2ⁿ` assignments, which is exactly "
             "the work the existence argument avoided and exactly the work an algorithm would have "
             "to avoid too."),
            ("Reaching for independence in the expectation",
             "The clauses of the lab's opening formula share every variable with every other "
             "clause, so their satisfaction indicators are anything but independent. Linearity "
             "does not need them to be. An argument that first checks for independence will fail "
             "on every interesting formula and will have been unnecessary on the others."),
            ("Dividing the mean by the number of clauses to get a ratio",
             "On an unsatisfiable formula the optimum is below `m` and the two divisions give "
             "different answers: `1` against the optimum and `7/8` against `m`, on the "
             "eight-clause instance. An approximation ratio is defined against the optimum, the "
             "lab enumerates to find it, and a ratio quoted without it is a number with no "
             "denominator."),
        ],
        "standard": ("Finish when you can prove an object exists by averaging, and say what the proof has not given you.",
                     "You should be able to compute a clause's satisfying fraction from its own "
                     "variables, add the shares by linearity without invoking independence, take "
                     "the one step to existence, and compute an approximation ratio against an "
                     "optimum you have actually found."),
        "note": ("The `7m/8` equality has a hypothesis, and it is the kind of hypothesis that is "
                 "easy to lose: every clause on three <em>distinct</em> variables. "
                 "&ldquo;Where the 7m/8 Argument Stops&rdquo; edits one clause so that it repeats "
                 "a variable, and watches the mean, the closed form and the ratio come apart while "
                 "the linearity argument itself stays perfectly correct."),
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "where-the-7m-8-argument-stops",
        "title": "Where the 7m/8 Argument Stops",
        "module": "Expectation, and what it does not assume",
        "one_line": "Repeat a variable inside one clause and watch a correct formula become a wrong one, with the per-clause table naming the culprit.",
        "summary": (
            "`7m/8` is a closed form, and a closed form has hypotheses. Write a clause with "
            "only two distinct variables and it is satisfied by 3 of its 4 local assignments "
            "rather than 7 of 8, so the mean drops to `27/8` while `7m/8` still reads `7/2`. "
            "Linearity of expectation has not failed; the arithmetic that collapsed `m` "
            "shares into one formula has. The lab computes each clause's share separately so "
            "the failure has an address."
        ),
        "key": [
            "x₁ ∨ x₁ ∨ x₂ has two distinct variables: 3 of 4, not 7 of 8",
            "mean = 7/8 + 7/8 + 3/4 + 7/8 = 27/8 = 3.375",
            "7m/8 = 7/2 = 3.5                        DOES NOT agree",
            "linearity still holds: the shares still add to the mean, exactly",
            "the closed form assumed something the formula on screen does not do",
            "optimum 4, ratio 27/32, and 4 of the 8 assignments below the mean",
        ],
        "key_label": "A hypothesis lost, and the row that finds it",
        "concepts_intro": (
            "The hard idea is which part of the argument broke. The other two are how the lab "
            "localises it and what a closed form owes its reader."
        ),
        "concepts": [
            ("The per-clause share is the real quantity",
             "The expectation is always `Σⱼ P(clause j satisfied)`, and that sum is correct for "
             "every formula. `7m/8` is what the sum collapses to <em>when every term is 7/8</em>. "
             "A clause on two distinct variables has 4 local assignments, one of which falsifies "
             "it, so its term is `3/4`. The lab prints one row per clause with its own variable "
             "count and its own share, and the sum of the shares is checked against the mean over "
             "every assignment."),
            ("Linearity did not fail, and nothing about the proof needs repair",
             "On the edited formula the four shares are `7/8`, `7/8`, `3/4` and `7/8`, adding to "
             "`27/8`, and the enumeration over all eight assignments gives `27/8` as well. "
             "Linearity is exactly as true as it was. What failed is a substitution: replacing "
             "each term by `7/8` was justified by a hypothesis, and the hypothesis stopped holding "
             "while the formula kept being applied."),
            ("A closed form carries its hypothesis, and the lab checks it",
             "`7m/8` is printed on the panel with the word agrees or the words DOES NOT agree "
             "beside it, and the clause table marks any clause whose distinct-variable count is "
             "not three. So the page cannot show a wrong closed form without saying so, and the "
             "reader is told which clause did it rather than that something did."),
        ],
        "read_title": "When a formula and its hypothesis part company",
        "read_intro": "One edited clause, three quantities that disagree, and the one of them that is still right.",
        "body": [
            ("p", "Start from the formula of &ldquo;The Probabilistic Method&rdquo; and change one "
                  "clause. `x₁ ∨ ¬x₂ ∨ x₃` becomes `x₁ ∨ x₁ ∨ x₂`. It is still a disjunction of "
                  "three literals, it is still a legal clause, and it still looks like every other "
                  "clause on the page. What it is not is a clause on three distinct variables, and "
                  "that was a hypothesis of the theorem."),
            ("def", ("The width of a clause and the number of variables in it",
                     "A clause has a <strong>width</strong> &mdash; how many literals it contains "
                     "&mdash; and a count of <strong>distinct variables</strong> &mdash; how many "
                     "different variables those literals mention. For most clauses the two are "
                     "equal. `x₁ ∨ x₁ ∨ x₂` has width 3 and two distinct variables, and it is the "
                     "second number that decides the clause's satisfying fraction.")),
            ("thm", ("A clause's share, in general",
                     "Let a clause mention `d` distinct variables and contain no pair of "
                     "complementary literals on the same variable. Under a uniformly random "
                     "assignment it is satisfied with probability `(2ᵈ − 1)/2ᵈ`. For `d = 3` that "
                     "is `7/8` and for `d = 2` it is `3/4`.")),
            ("proof", ("The clause is falsified exactly when every literal in it is false. A "
                       "literal on variable `v` is false for exactly one of the two values of `v`, "
                       "and since no variable appears with both signs, the requirement is "
                       "consistent: it pins each of the `d` variables to one value.",
                       "So exactly one of the `2ᵈ` assignments to those `d` variables falsifies the "
                       "clause, and the variables outside the clause are irrelevant. The satisfying "
                       "probability is `(2ᵈ − 1)/2ᵈ`.")),
            ("p", "If a clause does contain a variable and its negation &mdash; `x₁ ∨ ¬x₁ ∨ x₂` "
                  "&mdash; it is satisfied by every assignment and its share is `1`. The lab "
                  "handles that correctly too, by computing each clause's models over its own "
                  "variables rather than applying a formula, which is what makes the clause table "
                  "an enumeration rather than a second closed form waiting to be wrong."),
            ("example", ("The edited formula, clause by clause",
                         "`x₁ ∨ x₂ ∨ ¬x₃` has three distinct variables and a share of `7/8`. "
                         "`¬x₁ ∨ x₂ ∨ x₃`: three, `7/8`. `x₁ ∨ x₁ ∨ x₂`: <strong>two</strong>, and "
                         "3 of its 4 local assignments satisfy it, so `3/4`. "
                         "`¬x₂ ∨ ¬x₃ ∨ ¬x₁`: three, `7/8`. The shares add to "
                         "`7/8 + 7/8 + 3/4 + 7/8 = 27/8`, and enumerating all eight assignments "
                         "gives a mean of `27/8` as well. `7m/8` reads `7/2`, and `27/8 ≠ 7/2`.")),
            ("p", "`27/8` is `3.375` and `7/2` is `3.5`, a difference of `1/8` &mdash; exactly the "
                  "amount the third clause's share fell short, which is what an additive argument "
                  "predicts. Nothing subtle happened. One term in a sum of four was smaller than "
                  "assumed, and the sum was smaller by precisely that much."),
            ("h3", "What still holds, and it is most of it"),
            ("p", "The existence argument survives in its general form: `Z` cannot always be below "
                  "`E[Z]`, so some assignment satisfies at least `⌈27/8⌉ = 4` clauses. The panel "
                  "confirms it &mdash; the optimum is 4, which is all four clauses, so this formula "
                  "is satisfiable. What does not survive is the number `7m/8`, and any sentence "
                  "that used it as the guarantee rather than as the value of the sum in a special "
                  "case."),
            ("p", "The distribution has changed shape as well. On the original formula every "
                  "assignment satisfied 3 or 4 clauses; here one assignment satisfies only 2, "
                  "three satisfy 3, and four satisfy 4. The measured mean over 120 seeded coin "
                  "flips came out `33/10 = 3.3` with a range of 2 to 4, against an exact mean of "
                  "`27/8 = 3.375`. Same three kinds of number as everywhere else on this course, "
                  "and the middle one has moved because the formula moved."),
            ("h3", "The ratio moves too, and not by the same amount"),
            ("p", "The optimum is still 4, so the ratio the random assignment earns is "
                  "`(27/8)/4 = 27/32 ≈ 0.844`, down from `7/8 = 0.875`. The algorithm has not "
                  "changed and the instance has, which is the ordinary situation for an "
                  "approximation ratio: the `7/8` guarantee is a claim about a class of instances, "
                  "and this instance is outside the class. Either restate the guarantee for "
                  "general clause widths or preprocess the formula so the hypothesis holds."),
            ("p", "Preprocessing is the honest fix and it is cheap: `x₁ ∨ x₁ ∨ x₂` is logically "
                  "`x₁ ∨ x₂`, and a formula of clauses with fewer than three distinct variables "
                  "has a general bound of `Σ (2^dⱼ − 1)/2^dⱼ`, which the lab already computes as "
                  "the sum of the shares. The bound is weaker per clause with a smaller `d` "
                  "&mdash; `3/4` against `7/8` &mdash; and it is correct, which `7m/8` is not."),
            ("h3", "The general lesson, which is not about satisfiability"),
            ("p", "This is the path's hazard in its sharpest form. A count on one input is not a "
                  "bound; here, a closed form derived under a hypothesis is not a bound on "
                  "instances that fail it, and the failure is silent. Every quantity on the panel "
                  "was computed correctly and the page would have printed `7m/8` as the answer if "
                  "nobody had asked the clause table what its terms were."),
            ("p", "So the habit worth taking away is smaller than the theorem: keep the sum before "
                  "you collapse it. `Σⱼ P(clause j satisfied)` is right for every formula, costs "
                  "one row per clause to evaluate, and degrades into `7m/8` by itself when the "
                  "hypothesis happens to hold. The collapsed version is shorter and it is the one "
                  "that can be quietly wrong."),
        ],
        "lab": ("random", {"mode": "max3sat", "preset": "repeat"}),
        "steps_title": "Checking a hypothesis you did not write down",
        "steps_intro": "Find the term that changed before deciding what the theorem says.",
        "steps": [
            ("Count distinct variables, not literals",
             "Width three and three variables are different claims, and only the second decides "
             "the share. The lab prints both columns side by side and colours the second when they "
             "disagree, because this is the whole of the defect."),
            ("Recompute the term rather than patching the formula",
             "A clause with `d` distinct variables contributes `(2ᵈ − 1)/2ᵈ`. Put the real value in "
             "the sum and the answer is right again. Adjusting `7m/8` by a fudge factor is the "
             "move to avoid, since the fudge depends on the instance."),
            ("Check the sum against the enumeration",
             "The panel adds the per-clause shares and compares them with the mean over every "
             "assignment. Two routes, one number; if they ever disagreed, the clause table would "
             "be the thing to distrust, not linearity."),
            ("Restate the guarantee before reusing it",
             "`7/8` of the optimum is a claim about formulas whose clauses have three distinct "
             "variables. On this formula the ratio is `27/32`. Either say which class your "
             "instance is in, or quote the general sum, which is always available and always "
             "correct."),
        ],
        "worked": {
            "title": "Every assignment, after one clause is edited",
            "intro": [
                "`x₁ ∨ x₂ ∨ ¬x₃`, `¬x₁ ∨ x₂ ∨ x₃`, `x₁ ∨ x₁ ∨ x₂`, `¬x₂ ∨ ¬x₃ ∨ ¬x₁`. Only the "
                "third clause differs from the formula of the previous lesson, and only one "
                "variable in it.",
            ],
            "lines": [
                "clause               distinct   local models   share",
                "  x1 v x2 v !x3          3          7 of 8       7/8",
                "  !x1 v x2 v x3          3          7 of 8       7/8",
                "  x1 v x1 v x2           2          3 of 4       3/4   <- a variable repeats",
                "  !x2 v !x3 v !x1        3          7 of 8       7/8",
                "                                               -----",
                "  sum of the shares                              27/8",
                "",
                "x1 x2 x3   c1  c2  c3  c4    satisfied",
                " F  F  F    1   1   0   1        3",
                " F  F  T    0   1   0   1        2",
                " F  T  F    1   1   1   1        4",
                " F  T  T    1   1   1   1        4",
                " T  F  F    1   0   1   1        3",
                " T  F  T    1   1   1   1        4",
                " T  T  F    1   1   1   1        4",
                " T  T  T    1   1   1   0        3",
                "  mean = 27/8 = 3.375       the shares agree with the enumeration",
                "  7m/8 = 7/2 = 3.5          DOES NOT agree",
                "  optimum 4,  ratio 27/32,  4 of 8 below the mean",
                "  measured over 120 seeds: 33/10 = 3.3, range 2 to 4",
            ],
            "after": [
                "Two numbers agree and one does not, and the two that agree were computed by "
                "completely different routes: adding four per-clause fractions, and averaging "
                "eight integers. When a closed form disagrees with two independent computations, "
                "the closed form is the thing to doubt, and here the reason is visible in the "
                "third row of the first table.",
                "The second row of the assignment table is new. `F F T` satisfies only 2 clauses, "
                "which the original formula had no assignment doing. Editing a clause changed the "
                "shape of the distribution as well as its mean, and neither change is visible from "
                "`7m/8`, which did not move at all.",
                "For a faded rehearsal, edit the third clause again, to `x₁ ∨ ¬x₁ ∨ x₂`, and "
                "predict the new mean first. The supplied first move is this: that clause contains "
                "a variable and its negation, so no assignment falsifies it and its share is `1`. "
                "Work out the new sum of shares, say whether `7m/8` is now too high or too low, "
                "and then check both against the enumeration.",
            ],
        },
        "quiz_title": "Which part of the argument broke",
        "quiz": [
            {"q": "On the edited formula the mean is `27/8` and `7m/8` is `7/2`. What has gone wrong?",
             "a": ["Linearity of expectation fails when clauses share variables",
                   "The enumeration is wrong, since the theorem is proved",
                   "Nothing is wrong with linearity; `7m/8` assumed every clause has three distinct variables and one does not",
                   "The measured mean over 120 seeds is the correct value"],
             "c": 2,
             "why": "The expectation is `Σⱼ P(clause j satisfied)` always, and here that sum is "
                    "`7/8 + 7/8 + 3/4 + 7/8 = 27/8`, which matches the enumeration exactly. "
                    "`7m/8` is what the sum equals when every term is `7/8`, and the third clause's "
                    "term is `3/4`. Linearity is untouched."},
            {"q": "A clause mentions `d` distinct variables and no variable twice with opposite signs. What is its satisfying probability?",
             "a": ["`7/8` regardless of `d`", "`(2ᵈ − 1)/2ᵈ`", "`d/8`", "`1 − d/8`"],
             "c": 1,
             "why": "Exactly one assignment to those `d` variables makes every literal false, and "
                    "the other `2ᵈ − 1` satisfy the clause. At `d = 3` that is `7/8` and at `d = 2` "
                    "it is `3/4`, which is what the lab's clause table prints for the repeated "
                    "clause."},
            {"q": "Which claim still holds on the edited formula?",
             "a": ["Some assignment satisfies at least `⌈7m/8⌉ = 4` clauses, by the `7m/8` bound",
                   "Some assignment satisfies at least `⌈27/8⌉ = 4` clauses, because a value cannot always be below its mean",
                   "Every assignment satisfies at least 3 clauses",
                   "The ratio against the optimum is still `7/8`"],
             "c": 1,
             "why": "The existence argument uses the true mean, whatever it is, so it gives "
                    "`⌈27/8⌉ = 4`. Quoting `7m/8` here is quoting a number the formula does not "
                    "have. And one assignment satisfies only 2 clauses, so the third option is "
                    "false; the ratio is `27/32`."},
            {"q": "What is the safest habit this page suggests?",
             "a": ["Avoid clauses with repeated variables",
                   "Keep the per-clause sum and let it collapse to a closed form only when it does",
                   "Always use the measured mean instead of the exact one",
                   "Use `7m/8` and subtract a correction term per repeated variable"],
             "c": 1,
             "why": "`Σⱼ P(clause j satisfied)` is correct for every formula and costs one row per "
                    "clause. The closed form is a special case of it, and the failure mode of the "
                    "closed form is silent. A correction term would itself depend on the instance, "
                    "which is the problem the sum already solves."},
        ],
        "mistakes": [
            ("Blaming linearity when a closed form disagrees with an enumeration",
             "Linearity of expectation is unconditional and it was not the step that failed. The "
             "step that failed was substituting `7/8` for a term that was `3/4`. Reaching for the "
             "general theorem when the specialisation is at fault sends you looking in the one "
             "place where nothing is wrong."),
            ("Counting literals instead of distinct variables",
             "`x₁ ∨ x₁ ∨ x₂` has three literals and two variables, and only the second number "
             "matters. The lab prints them in adjacent columns for that reason, and every clause "
             "where they differ is coloured. A parser that validates width and not variable count "
             "will accept exactly the formulas that break the bound."),
            ("Quoting an approximation ratio without checking the instance is in its class",
             "`7/8` is a guarantee for formulas whose clauses have three distinct variables. Here "
             "the ratio is `27/32`. The algorithm did not change; the class did, and a ratio "
             "carried across a class boundary is the kind of claim that survives every test except "
             "the one nobody ran."),
        ],
        "standard": ("Finish when a disagreement between a closed form and an enumeration sends you to the hypothesis rather than to the theorem.",
                     "You should be able to compute a clause's share from its distinct variables, "
                     "keep the per-clause sum rather than the collapsed form, say which of the "
                     "argument's steps survives an edited clause, and recompute an approximation "
                     "ratio against an optimum that has actually been found."),
        "note": ("Both kinds of guarantee met so far have been about averages. The next module is "
                 "about the other kind: an algorithm that gives the right answer with a "
                 "probability you can state, gets it wrong the rest of the time, and is made "
                 "useful by being run again. &ldquo;Karger's Contraction&rdquo; starts with a "
                 "success probability of `19/35` and an argument for why that is enough."),
    },
]
