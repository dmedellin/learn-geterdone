"""Strings and Pattern Matching, lessons 01-06 - naive matching, the failure function, and the machine."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "naive-matching-and-the-two-numbers",
        "title": "Naive Matching, Measured and Bounded",
        "module": "Matching one pattern",
        "one_line": "Slide the pattern over every offset, count the characters actually compared, and put that count beside the worst case it cannot exceed.",
        "summary": (
            "The simplest matcher tries every offset and compares until something fails. On "
            "the lab's opening text that costs 50 character comparisons against a proved "
            "bound of 123, and the gap between those two numbers is not a rounding error "
            "&mdash; it is the difference between a measurement of one input and a statement "
            "about all of them. This lesson establishes both numbers and what each is worth."
        ),
        "key": [
            "for each of the n − m + 1 offsets: compare until a mismatch or a match",
            "measured, on the opening text:  50 comparisons over 41 alignments",
            "proved, for every text:         m(n − m + 1) = 3 × 41 = 123",
            "per alignment: 50/41 measured, 13/12 expected, 3 possible",
            "sigma/(sigma − 1) is the expected cost per alignment, and m is not in it",
        ],
        "key_label": "What it cost, what it was expected to cost, what it could have cost",
        "concepts_intro": (
            "One hard idea: a count and a bound answer different questions. The other two say "
            "what one alignment costs and why ordinary text never spends it."
        ),
        "concepts": [
            ("An alignment is an offset, and it costs at most m",
             "At offset `i` the matcher compares `t[i]` with `p[0]`, then `t[i+1]` with `p[1]`, "
             "and stops at the first disagreement. There are `n − m + 1` offsets at which the "
             "pattern still fits, and the work at one of them is at least 1 comparison and at "
             "most `m`. Everything else on this page is those two facts multiplied out or "
             "measured."),
            ("A measured count and a proved bound are different claims",
             "The lab prints 50 for the text on screen. It prints 123 for every text of 43 "
             "characters searched for a pattern of 3. The first is evidence about one input "
             "and changes the moment a character is typed; the second is a theorem and does "
             "not. This Subject's whole hazard is reading the first as though it were the "
             "second, and every page here prints them side by side so that the substitution "
             "has to be made deliberately rather than by accident."),
            ("The expected cost per alignment does not contain m at all",
             "Over an alphabet of `sigma` equally likely letters, the chance that an alignment "
             "survives `k` comparisons is `(1/sigma)` to the power `k`, so the expected number "
             "of comparisons at one alignment sums to exactly `sigma/(sigma − 1)`. At the "
             "thirteen distinct characters of the opening input that is `13/12`, which is "
             "under 1.09 whatever `m` is. The bound multiplies by `m`; the expectation does "
             "not, and that single discrepancy is why the simplest matcher is the one most "
             "programs actually run."),
        ],
        "read_title": "One offset at a time, and two numbers for what that costs",
        "read_intro": "The algorithm, the bound with its proof, the measurement, and the expectation that explains why the two are so far apart.",
        "body": [
            ("def", ("Naive string matching",
                     "Given a text `t` of length `n` and a pattern `p` of length `m` with "
                     "`m &le; n`, the <strong>naive matcher</strong> considers each offset `i` "
                     "from 0 to `n − m` in turn. At offset `i` it compares `t[i+k]` with `p[k]` "
                     "for `k = 0, 1, 2, ...`, stopping at the first `k` where they differ, or "
                     "reporting a match at `i` when all `m` agree. The offsets it considers are "
                     "called its <strong>alignments</strong>, and there are `n − m + 1` of "
                     "them.")),
            ("p", "Nothing is remembered between alignments. That is the whole of the "
                  "algorithm and also the whole of the criticism of it: after an alignment has "
                  "matched five characters and failed on the sixth, the matcher throws those "
                  "five away and starts the next offset from nothing. The rest of this module "
                  "is three different things to do with the information that was thrown away."),
            ("thm", ("The comparison count is at most m(n − m + 1)",
                     "On any text of length `n` and any pattern of length `m`, the naive "
                     "matcher makes at most `m(n − m + 1)` character comparisons, and at least "
                     "`n − m + 1`.")),
            ("proof", ("There are exactly `n − m + 1` alignments, because `i` runs over the "
                       "integers from 0 to `n − m` inclusive and the loop body is entered once "
                       "for each.",
                       "At one alignment the inner loop increments `k` from 0 and stops the "
                       "first time `t[i+k]` differs from `p[k]`, or when `k` reaches `m`. Each "
                       "iteration performs one comparison and `k` never exceeds `m`, so one "
                       "alignment costs at most `m` comparisons; and the loop body runs at "
                       "least once, so it costs at least 1. Multiplying both ends by the "
                       "number of alignments gives the two bounds.",
                       "Both are attained. The lower one is reached whenever no character of "
                       "the text equals `p[0]`; the upper one needs every alignment to match "
                       "`m − 1` characters and then fail, which is the input the sibling "
                       "lesson &ldquo;The Text Built to Reach the Bound&rdquo; constructs.")),
            ("example", ("Forty-one alignments, broken down exactly",
                         "The lab opens on the text `the rain in spain stays mainly in the "
                         "plain` and the pattern `ain`, so `n = 43`, `m = 3` and there are 41 "
                         "alignments. Five of those offsets carry an `a`: 5, 14, 20, 25 and 40. "
                         "The other 36 disagree on the very first comparison and cost 1 each. "
                         "Offset 20 matches the `a` of `stays` and then fails on `y`, costing "
                         "2. The remaining four are matches and cost 3 each. So the total is "
                         "36 + 2 + 12 = 50, and the panel reports 50.")),
            ("p", "The bound over the same input is `3 × 41 = 123`. The measurement is 50, "
                  "which is `123/50 = 2.46` times smaller, and both numbers are right. Change "
                  "one character of the text and 50 moves; 123 does not move until the lengths "
                  "do."),
            ("thm", ("Expected comparisons per alignment over a uniform alphabet",
                     "If each character of the text is drawn independently and uniformly from "
                     "an alphabet of `sigma &ge; 2` letters, the expected number of comparisons "
                     "the naive matcher makes at one alignment is at most "
                     "`sigma/(sigma − 1)`.")),
            ("proof", ("The alignment performs a comparison for `k = 0`, and performs the "
                       "comparison at `k` only if the first `k` agreed, which for independent "
                       "uniform characters has probability `(1/sigma)` to the power `k`.",
                       "So the expected count is the sum over `k &ge; 0` of `(1/sigma)^k`, a "
                       "geometric series with ratio `1/sigma &lt; 1`, which is exactly "
                       "`1/(1 − 1/sigma) = sigma/(sigma − 1)`. Truncating the series at `m` "
                       "terms, as the real algorithm does, can only reduce it.",
                       "The quantity `m` does not appear. A longer pattern gives more ways to "
                       "fail early, not more work per alignment, and that is the whole reason "
                       "the naive matcher is linear in practice.")),
            ("p", "At `sigma = 13`, the thirteen distinct characters of the opening input, the "
                  "expectation is `13/12`, just over 1.08. The measured figure is `50/41`, just "
                  "over 1.22. The two disagree because the text is English rather than uniform "
                  "&mdash; the letter `a` is commoner than a thirteenth of the text &mdash; and "
                  "the panel prints both rather than picking one."),
            ("h3", "Repeating the text does not produce a quadratic, and the lab says so"),
            ("p", "The first table under the chart repeats your text 1 to 6 times with the "
                  "pattern unchanged. On the opening input the counts come out 50, 102, 154, "
                  "206, 258 and 310 as `n` runs 43, 86, 129, 172, 215, 258. The differences are "
                  "52 every time: that is a straight line, not a parabola."),
            ("p", "It has to be. Holding `m` fixed makes the bound `m(n − m + 1)` linear in `n` "
                  "as well, so nothing in that table can be quadratic in anything. The column "
                  "worth reading is comparisons per character, which moves only from 1.16 to "
                  "1.20 across the six rows. The quadratic needs `m` to grow with `n`, which "
                  "the second table does and this one deliberately does not."),
            ("h3", "The other two matchers on the same text"),
            ("p", "The panel also runs Knuth&ndash;Morris&ndash;Pratt and Horspool over "
                  "whatever you typed, so that the comparison is on one input rather than "
                  "between two anecdotes. On the opening text they take 44 and 25 against "
                  "naive's 50. Horspool is ahead because it skips; KMP is behind by 6 because "
                  "it reads every character of the text once and naive mostly reads one "
                  "character per alignment and leaves."),
            ("p", "All three report the same 4 matches, at offsets 5, 14, 25 and 40, and the "
                  "panel checks all three against a scan that compares the whole substring at "
                  "every offset. That check is not ceremony: a matcher that shifts too far "
                  "returns a shorter list of positions, and a shorter list of correct positions "
                  "is the one kind of wrong answer that looks exactly like a right one."),
        ],
        "lab": ("strings", {
            "mode": "naive",
            "preset": "prose",
            "panel_title": "Type a text and a pattern, and watch the count separate from the bound",
            "panel_intro": "Every bar is one alignment and its height is the characters compared "
                           "there; the dashed line across the chart is `m`, the most one "
                           "alignment can cost. The match positions are checked against a scan "
                           "over every offset on each keystroke, and the two tables below "
                           "separate growing the text from growing the pattern.",
        }),
        "steps_title": "Reading a count without promoting it to a bound",
        "steps_intro": "Write the measurement and the bound in two columns from the start, and never let a sentence use one where it means the other.",
        "steps": [
            ("Count the alignments before counting anything else",
             "`n − m + 1` is fixed by the two lengths and nothing about the characters can "
             "change it. It is the denominator of every per-alignment figure on the page, and "
             "getting it wrong by one is the commonest arithmetic slip in this module."),
            ("Classify the alignments by where they died",
             "On ordinary text almost all of them fail on the first comparison. Counting how "
             "many start with `p[0]` gives the total almost immediately: everything else costs "
             "1, and only those few cost more."),
            ("Put the bound in the next column, not the same one",
             "`m(n − m + 1)` is a separate calculation from the same two lengths, and it must "
             "be written down even when it is five times too big. A page that prints only the "
             "measurement has said nothing about any text but the one on screen."),
            ("Change the text before generalising, and change the pattern too",
             "Retyping the text moves the count and leaves the bound alone if the lengths hold. "
             "Lengthening the pattern moves both. Any sentence that survives only one of those "
             "two edits is a sentence about that input."),
        ],
        "worked": {
            "title": "Fifty comparisons, accounted for one alignment at a time",
            "intro": [
                "The text is `the rain in spain stays mainly in the plain` and the pattern is "
                "`ain`. Offsets are counted from 0, so `n = 43`, `m = 3`, and the alignments "
                "run from 0 to 40.",
            ],
            "lines": [
                "offsets whose character is not 'a'          36 alignments  x 1 = 36",
                "offset 20   a y ...   'a' matches, 'y' fails  1 alignment  x 2 =  2",
                "offset  5   a i n     match                   1 alignment  x 3 =  3",
                "offset 14   a i n     match                   1 alignment  x 3 =  3",
                "offset 25   a i n     match                   1 alignment  x 3 =  3",
                "offset 40   a i n     match                   1 alignment  x 3 =  3",
                "",
                "alignments  36 + 1 + 4                                     = 41",
                "comparisons 36 + 2 + 12                                    = 50",
                "the bound   m(n - m + 1) = 3 x 41                          = 123",
                "measured / possible                                        = 50/123",
            ],
            "after": [
                "The single most useful line in that table is the first. Thirty-six of the "
                "forty-one alignments never reach a second comparison, and that is the whole "
                "reason the measured figure sits at 1.22 per alignment rather than at 3.",
                "Now predict before you check. Replace the pattern with `in` and the answer "
                "changes in two places at once: there are 42 alignments rather than 41, and "
                "`i` is a commoner first character than `a`, so more alignments survive to a "
                "second comparison. The supplied first move is the bound &mdash; it becomes "
                "`2 × 42 = 84`, which is smaller than 123 even though the pattern got easier "
                "to find. Say why a shorter pattern lowers the bound and then say whether it "
                "must lower the count.",
                "For a second rehearsal, keep `ain` and delete the final word of the text. Two "
                "matches survive, the alignment count falls by 6, and the count falls by more "
                "than 6. Say by exactly how much before running it, using nothing but the "
                "breakdown above.",
            ],
        },
        "quiz_title": "Which number answers which question",
        "quiz": [
            {"q": "The lab reports 50 comparisons against a bound of 123 on the opening text. What has been established about naive matching?",
             "a": ["That it makes about 40 per cent of the comparisons the bound allows",
                   "That on this text it made 50 comparisons, and that on any text with these two lengths it cannot exceed 123",
                   "That the bound is loose and should be replaced by a smaller one",
                   "That its running time is linear in the length of the text"],
             "c": 1,
             "why": "The two numbers answer different questions and neither answers the other's. "
                    "50 is a measurement of one input; 123 is a theorem about every input of "
                    "those two lengths. The first choice turns the measurement into a general "
                    "proportion, which the next preset refutes immediately by reaching the "
                    "bound exactly."},
            {"q": "A pattern is lengthened from 3 characters to 7 on the same text. What happens to the expected comparisons per alignment over a uniform alphabet?",
             "a": ["It rises, because there are more characters that could match",
                   "It is unchanged: the expectation is sigma/(sigma − 1), in which m does not appear",
                   "It falls, because a longer pattern is rarer",
                   "It cannot be determined without knowing the text"],
             "c": 1,
             "why": "The series `1 + 1/sigma + 1/sigma^2 + ...` sums to `sigma/(sigma − 1)` "
                    "with no reference to `m` at all; truncating it at `m` terms only lowers "
                    "it. A longer pattern gives more chances to fail early rather than more "
                    "work per alignment. The bound `m(n − m + 1)` does contain `m`, which is "
                    "exactly why the two figures diverge as the pattern grows."},
            {"q": "The first table repeats the text 1 to 6 times and the naive count rises 50, 102, 154, 206, 258, 310. What does that table show?",
             "a": ["That naive matching is quadratic, since the numbers grow quickly",
                   "That naive matching is linear in n when m is held fixed, which is all a table with a fixed pattern can show",
                   "That naive matching is linear on all inputs",
                   "Nothing, because repeating a text is not a fair experiment"],
             "c": 1,
             "why": "The differences are a constant 52, so the growth is linear &mdash; and it "
                    "has to be, because holding `m` fixed makes the bound `m(n − m + 1)` linear "
                    "in `n` too. The table cannot show a quadratic and cannot rule one out "
                    "either; the second table, where `m` grows with `n`, is the one that "
                    "addresses that claim."},
            {"q": "On the opening text, naive matching takes 50 comparisons and Knuth–Morris–Pratt takes 44. Which statement is safe?",
             "a": ["KMP is 12 per cent faster than naive matching",
                   "KMP took 6 fewer comparisons on this text, and both counts are linear in n while m is fixed",
                   "KMP is the better algorithm and this settles it",
                   "The 6 comparisons are the saving KMP's failure function buys"],
             "c": 1,
             "why": "Both figures are measurements of one input. The gap here is a constant, "
                    "not an order: with `m` fixed both algorithms are linear in `n`, and the "
                    "sibling lesson &ldquo;Where the Simple Algorithm Wins&rdquo; loads a "
                    "pattern on which the same two numbers come out the other way round."},
        ],
        "mistakes": [
            ("Quoting the bound as though it were the cost",
             "&ldquo;Naive matching is `O(nm)`&rdquo; is true and is almost never what the "
             "algorithm did. On the opening text it made 50 comparisons where `nm` is 129 and "
             "the tight bound is 123. The phrase describes the worst input, and the worst input "
             "has to be constructed &mdash; it does not arrive by typing English."),
            ("Quoting the measurement as though it were the cost",
             "The opposite error and the one this Subject is about. 50 comparisons on 43 "
             "characters does not establish that naive matching is linear; it establishes that "
             "it was linear here. The preset one click away reaches the bound exactly, on a "
             "text of 24 characters."),
            ("Forgetting that a match costs m comparisons too",
             "An alignment that succeeds is the most expensive kind, not a free one: it compares "
             "all `m` characters and finds all `m` equal. Four matches contribute 12 of the 50 "
             "comparisons on the opening text, almost a quarter of the total from under a tenth "
             "of the alignments."),
        ],
        "standard": ("Finish when you can state both numbers for a text you have not seen, and say which questions each one closes.",
                     "You should be able to count the alignments from the two lengths, break the "
                     "comparison total down by where each alignment died, compute "
                     "`m(n − m + 1)` beside it, explain why `m` appears in the bound and not in "
                     "the expectation, and say what a table that repeats one text can and "
                     "cannot demonstrate."),
        "note": ("The next two pages take the same algorithm to its two extremes without "
                 "changing a line of it. &ldquo;Where the Simple Algorithm Wins&rdquo; loads a "
                 "pattern that is not in the text at all, and naive matching comes out ahead of "
                 "Knuth&ndash;Morris&ndash;Pratt; &ldquo;The Text Built to Reach the Bound&rdquo; "
                 "loads the input on which the measurement and the bound are the same number. "
                 "Both use this same lab, so the comparison is between presets rather than "
                 "between pages."),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "where-the-simple-algorithm-wins",
        "title": "Where the Simple Algorithm Wins",
        "module": "Matching one pattern",
        "one_line": "On a pattern that is not in the text, naive matching makes 39 comparisons and Knuth–Morris–Pratt makes 43, and the reason is structural rather than accidental.",
        "summary": (
            "Change the pattern to one the text does not contain and the asymptotically "
            "better algorithm loses. Naive matching makes exactly one comparison per "
            "alignment, `n − m + 1` in total; KMP reads every character of the text once, "
            "`n` in total. The difference is `m − 1` in naive's favour on every such text, "
            "which makes this the clearest instance on the path of a count that says nothing "
            "about a bound."
        ),
        "key": [
            "pattern zebra, text without a z:  no alignment survives one comparison",
            "naive        n − m + 1 = 39 comparisons      1 per alignment, exactly",
            "KMP          n = 43 comparisons              1 per text character",
            "the gap is m − 1 = 4, in naive's favour, on every text with no z",
            "KMP's bound 2n = 86 is still correct and still not the cost",
            "Horspool 14, because it looks at one character in five",
        ],
        "key_label": "Three matchers, one text, and the asymptotically best one last",
        "concepts_intro": (
            "The hard idea is that the loss is structural, not noise. The other two are the "
            "exact counts each algorithm makes and what a guarantee is actually for."
        ),
        "concepts": [
            ("Naive matching pays per alignment; KMP pays per character",
             "When no character of the text equals `p[0]`, every naive alignment ends after one "
             "comparison, so the total is the number of alignments, `n − m + 1`. KMP holds a "
             "matched-length `k` that stays at 0 throughout and makes exactly one comparison "
             "for each character of the text, so its total is `n`. Since `n` exceeds "
             "`n − m + 1` by `m − 1`, naive wins by `m − 1` on every such text &mdash; 4 here, "
             "and more for a longer pattern."),
            ("The loss is not a defect in KMP and does not touch its bound",
             "KMP's promise is that the text pointer never moves backwards and the total stays "
             "under `2n`. On this input it makes 43 comparisons against a bound of 86, so the "
             "promise is kept with room to spare. What it is not is a promise to beat the naive "
             "matcher on any particular text, and nothing in the proof of `2n` ever claimed "
             "that. A guarantee bounds the bad case; it does not improve the good one."),
            ("A single input can refute a general claim but cannot establish one",
             "This text settles &ldquo;KMP always makes fewer comparisons than naive "
             "matching&rdquo;, and settles it negatively, because one counterexample is enough "
             "to kill a universal statement. The same text establishes nothing at all about "
             "&ldquo;naive matching is faster than KMP&rdquo;, because no number of examples "
             "adds up to a quantifier. The asymmetry is the whole method of this Subject: "
             "measurements refute, and only proofs confirm."),
        ],
        "read_title": "The same two algorithms, and the text that reverses them",
        "read_intro": "Why each count is what it is, why the reversal is guaranteed rather than lucky, and what KMP is being paid for if not this.",
        "body": [
            ("p", "Keep the text from the previous page and change the pattern from `ain` to "
                  "`zebra`. There is no `z` anywhere in `the rain in spain stays mainly in the "
                  "plain`, so no alignment gets past its first comparison. The lab reports 39 "
                  "comparisons over 39 alignments, at exactly 1 per alignment, against a bound "
                  "of `5 × 39 = 195`."),
            ("thm", ("Naive matching on a text avoiding the pattern's first character",
                     "If no character of `t` equals `p[0]`, the naive matcher makes exactly "
                     "`n − m + 1` comparisons and reports no match.")),
            ("proof", ("Each alignment begins by comparing `t[i]` with `p[0]`. By hypothesis "
                       "these differ, so the inner loop stops with `k = 0` after one "
                       "comparison, and the alignment reports nothing.",
                       "There are `n − m + 1` alignments and each contributes exactly 1, so the "
                       "total is `n − m + 1`. No alignment reaches `k = m`, so no match is "
                       "reported, which is correct because a match would require `t[i]` to "
                       "equal `p[0]`.")),
            ("thm", ("Knuth–Morris–Pratt on the same text",
                     "If no character of `t` equals `p[0]`, KMP makes exactly `n` comparisons.")),
            ("proof", ("KMP maintains `k`, the number of pattern characters currently matched, "
                       "starting at 0. Its fallback loop runs only while `k &gt; 0`.",
                       "Suppose `k = 0` on entering the step for text position `i`. The "
                       "fallback loop is skipped, one comparison of `t[i]` against `p[0]` is "
                       "made, and by hypothesis it fails, so `k` stays 0. By induction `k` is 0 "
                       "at every position, so exactly one comparison happens at each of the "
                       "`n` positions and the total is `n`.")),
            ("p", "Subtract: `n − (n − m + 1) = m − 1`. On this input that is 4, and the panel "
                  "reports 39 against 43. The margin does not depend on the text at all, only "
                  "on the length of the pattern, so lengthening `zebra` to `zebraic` widens it "
                  "to 6 without touching either algorithm."),
            ("example", ("The same reversal at six text lengths",
                         "The growth table repeats the text and the two columns stay apart in "
                         "the same direction. Naive reads 39, 82, 125, 168, 211, 254 as `n` "
                         "runs 43, 86, 129, 172, 215, 258, and KMP reads 43, 86, 129, 172, 215, "
                         "258 &mdash; which is `n` itself, in every row. The difference is 4 in "
                         "every row, because it is `m − 1` and `m` never moved.")),
            ("h3", "What the guarantee is actually for"),
            ("p", "Switch the preset to the one built to reach the bound and read the same two "
                  "columns: naive 100, KMP 44, on a text of 24 characters. KMP is not better on "
                  "average here or worse on average there; it is the algorithm whose count "
                  "cannot exceed `2n` whatever is typed, and naive matching is the algorithm "
                  "whose count cannot exceed `m(n − m + 1)`. At `n = 24` and `m = 5` those two "
                  "ceilings are 48 and 100, and the measured numbers sit under each."),
            ("p", "So the honest summary of the pair of experiments is: the measured counts "
                  "reverse between two texts, and the bounds do not. Whichever direction you "
                  "want to argue, the evidence for it is a proof and the numbers are "
                  "illustrations."),
            ("h3", "Horspool, which wins here by a wider margin and promises nothing"),
            ("p", "The third column reports 14. Horspool compares the window from the right and "
                  "then shifts by the last occurrence of the text character sitting under the "
                  "window's final position, which for a letter absent from the pattern is the "
                  "full `m`. So it reads roughly one character in five and finishes in 14 "
                  "comparisons where naive needs 39."),
            ("p", "That is the largest saving on the page and the one with the least behind it. "
                  "Horspool's worst case is `m(n − m + 1)` comparisons, the same as naive's, and "
                  "the sibling lesson &ldquo;The Text Where Nothing Is Skipped&rdquo; is a "
                  "30-character text on which it makes 130 comparisons and naive makes 26."),
            ("p", "Put the three side by side and the ordering changes twice in this course "
                  "with no algorithm changing at all. That is the point: the ranking is a "
                  "property of the input, and the only statements that survive every input are "
                  "the bounds, which do not rank them at all."),
        ],
        "lab": ("strings", {
            "mode": "naive",
            "preset": "absent",
            "panel_title": "A pattern the text does not contain, and three matchers on it",
            "panel_intro": "The bar chart is flat at 1 because every alignment dies on its first "
                           "comparison. Read the last three counters together: the measured "
                           "count, `KMP on the same text`, and `Horspool on the same text` are "
                           "three numbers for one input, and the order they come in changes "
                           "when you change the preset rather than the algorithm.",
        }),
        "steps_title": "Using a counterexample for exactly what it is worth",
        "steps_intro": "One input can kill a universal claim outright and can never establish one. Keep those two uses apart.",
        "steps": [
            ("State the claim with its quantifier before testing it",
             "&ldquo;KMP makes fewer comparisons&rdquo; has to be finished: fewer on every "
             "text, or fewer on this one. The first is refuted by the input on screen. The "
             "second is a measurement and generalises to nothing."),
            ("Check whether the reversal is structural or incidental",
             "Here it is structural: the two counts are `n − m + 1` and `n` exactly, both "
             "proved, so the margin `m − 1` holds on every text with no `z` in it. An "
             "incidental reversal would move when the text moved, and this one does not."),
            ("Read the bound column even when the measured column is the interesting one",
             "39 against a bound of 195, and 43 against a bound of 86. The algorithm that lost "
             "the measurement has by far the tighter guarantee, and a page showing only the "
             "measurements would have hidden that."),
            ("Switch the preset before writing a conclusion down",
             "The same lab, one click away, has naive at 100 and KMP at 44. If a sentence you "
             "were about to write survives only one of the two presets, it is a sentence about "
             "a text."),
        ],
        "worked": {
            "title": "Thirty-nine against forty-three, derived rather than observed",
            "intro": [
                "The text is `the rain in spain stays mainly in the plain`, 43 characters, and "
                "the pattern is `zebra`, 5 characters. No `z` occurs in the text.",
            ],
            "lines": [
                "alignments                 n - m + 1 = 43 - 5 + 1        = 39",
                "naive, per alignment       first comparison fails        =  1",
                "naive, total               39 x 1                        = 39",
                "",
                "KMP, k stays 0             one comparison per position   =  1",
                "KMP, total                 43 x 1                        = 43",
                "",
                "margin                     n - (n - m + 1) = m - 1       =  4",
                "naive bound                m(n - m + 1) = 5 x 39         = 195",
                "KMP bound                  2n = 2 x 43                   = 86",
                "Horspool, measured                                       = 14",
            ],
            "after": [
                "Nothing in that table was read off the screen except the last line. The two "
                "totals and the margin follow from the two theorems above and the two lengths, "
                "which is what makes this a reversal you can predict rather than one you "
                "notice.",
                "For a faded rehearsal, keep the text and change the pattern to `quartz`. The "
                "supplied first move: there is no `q` in the text either, so the same two "
                "theorems apply with `m = 6`. Say what the three counts become &mdash; naive, "
                "KMP, and the margin &mdash; before running it, and then say which of the three "
                "you could have got wrong by assuming the margin was a property of the text.",
                "Then try `plain`, which does occur. Now `p` appears twice in the text, so the "
                "first theorem no longer applies and the naive count is no longer the alignment "
                "count. Predict whether naive still beats KMP, and say what you would have to "
                "know about the text to answer that without running it.",
            ],
        },
        "quiz_title": "What one text settles and what it cannot",
        "quiz": [
            {"q": "Naive matching makes 39 comparisons and KMP makes 43 on this text. Which claim has been settled?",
             "a": ["Naive matching is faster than KMP",
                   "The claim that KMP makes fewer comparisons than naive matching on every text is false",
                   "KMP's 2n bound is wrong",
                   "Naive matching is faster whenever the pattern is absent"],
             "c": 1,
             "why": "A single input refutes a universal claim and establishes none. The fourth "
                    "choice is a universal claim of its own and would need a proof; the lesson "
                    "gives one for the narrower statement about texts avoiding `p[0]`, which is "
                    "not the same condition as the pattern being absent."},
            {"q": "Why is the margin exactly 4 here rather than some incidental number?",
             "a": ["Because the text happens to contain no z",
                   "Because naive makes n − m + 1 comparisons and KMP makes n, so the gap is m − 1 and m is 5",
                   "Because the pattern is one character longer than the alphabet allows",
                   "Because 43 and 39 happen to differ by 4"],
             "c": 1,
             "why": "Both totals are proved exactly for a text containing no character equal to "
                    "`p[0]`, so their difference is `m − 1` independently of which text it is. "
                    "The first choice states the hypothesis of that theorem rather than its "
                    "conclusion, and does not by itself say what the gap is."},
            {"q": "On the adversarial preset the same lab reports naive 100 and KMP 44. Taken with this page, what follows?",
             "a": ["The two algorithms are equally good on average",
                   "Which one makes fewer comparisons is a property of the input, and only the bounds hold across all inputs",
                   "KMP is better, because 44 is smaller than 100",
                   "The measurements on one of the two presets must be wrong"],
             "c": 1,
             "why": "Both pairs of measurements are correct and they point in opposite "
                    "directions, which is exactly what it means for the ranking to depend on "
                    "the input. The statements that hold everywhere are `m(n − m + 1)` and "
                    "`2n`, and neither of those ranks the two algorithms."},
        ],
        "mistakes": [
            ("Treating the reversal as a measurement artefact",
             "It is not noise and it does not go away with a longer text: the growth table shows "
             "the same 4-comparison margin at all six sizes, because both counts are exact "
             "formulas in `n` and `m`. Calling it an artefact is the same error as calling the "
             "adversarial preset unrepresentative &mdash; both are inputs, and the claim under "
             "test was about all of them."),
            ("Concluding that the failure function was wasted here",
             "KMP built `fail[]` for a pattern with no borders at all, so the table is five "
             "zeros and no fallback ever fires. The work was not wasted, it was insured: the "
             "same construction is what holds the count under `2n` on the text where naive "
             "makes 100. You cannot buy the guarantee only on the inputs that need it."),
            ("Reading KMP's 43 as evidence that its bound is loose",
             "43 against 86 is a factor of two, and the bound is nevertheless tight: a text "
             "exists on which KMP genuinely approaches `2n`, which is why the constant is 2 and "
             "not 1. A measurement below a bound is the normal case and says nothing about "
             "whether the bound can be lowered."),
        ],
        "standard": ("Finish when you can predict both counts from the two lengths alone, and say precisely which claim the reversal kills.",
                     "You should be able to prove that naive makes `n − m + 1` comparisons and "
                     "KMP makes `n` when the text avoids `p[0]`, derive the margin `m − 1` "
                     "without running anything, state why this refutes a universal claim but "
                     "supports no general one, and name what KMP's guarantee is bounding if not "
                     "this text."),
        "note": ("&ldquo;Borders, and the Failure Function Built&rdquo; is where `fail[]` stops "
                 "being a table that appeared and becomes something constructed character by "
                 "character and checked against the definition of a border. Until then it is "
                 "enough to know that KMP never moves the text pointer backwards, which is the "
                 "property that pins its count to `n` here."),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "the-text-built-to-reach-the-bound",
        "title": "The Text Built to Reach the Bound",
        "module": "Matching one pattern",
        "one_line": "Construct the input on which the measured count equals m(n − m + 1) exactly, and then show what it takes to make naive matching actually quadratic.",
        "summary": (
            "A run of twenty-four a's searched for `aaaab` costs 100 comparisons against a "
            "bound of 100. That is the worst case attained, not approached. But repeating "
            "that same text 1 to 6 times still gives a straight line, because holding `m` "
            "fixed makes the bound linear too &mdash; the quadratic needs a family in which "
            "`m` grows with `n`, and the lab builds one where the count is `m(m − 1)` and "
            "equals the bound in every row."
        ),
        "key": [
            "text a^24, pattern aaaab:  every alignment matches m − 1 then fails",
            "measured 100 = m(n − m + 1) = 5 × 20 = 100,  the bound attained",
            "repeating that text: 100, 220, 340, 460, 580, 700  -  a straight line",
            "the family: text a^(2(m − 1)), pattern a^(m − 1) b",
            "there the count is m(m − 1), equals the bound, and per character is m/2",
            "KMP on the same family is 3(m − 1), so 1.5 per character, flat",
        ],
        "key_label": "The bound attained on one text, and the family where it grows without limit",
        "concepts_intro": (
            "The hard idea is the one the lab's author retracted after printing the numbers: a "
            "fixed pattern cannot exhibit a quadratic. The other two are the construction and "
            "what makes it worst."
        ),
        "concepts": [
            ("The worst case is constructed, not encountered",
             "For every alignment to cost the full `m`, each one must agree on `m − 1` "
             "characters and disagree on the last. A run of one letter with a pattern that is "
             "that letter `m − 1` times followed by a different one does exactly that at every "
             "offset. The lab opens on `aaaaaaaaaaaaaaaaaaaaaaaa` and `aaaab`: 20 alignments, 5 "
             "comparisons each, 100 in total, and the bound `5 × 20` is 100 as well. The "
             "measured column and the proved column agree for the first and only time on this "
             "course."),
            ("Repeating a text with the pattern fixed cannot show a quadratic",
             "Concatenate the adversarial text with itself and the counts read 100, 220, 340, "
             "460, 580, 700 &mdash; differences of 120, a line. That is forced: with `m` held "
             "at 5 the bound `m(n − m + 1)` is itself linear in `n`, so nothing in that table "
             "can be quadratic in anything. A page that showed those six numbers and said "
             "&ldquo;quadratic&rdquo; would be reading steep growth as a different order of "
             "growth, and steepness is a constant."),
            ("The quadratic is a statement about a family in which m grows with n",
             "Take the text to be `2(m − 1)` copies of `a` and the pattern to be `m − 1` copies "
             "followed by `b`. Then the alignment count is `m − 1`, each alignment costs `m`, "
             "and the total is `m(m − 1)`, which is the bound. As `m` runs 3 to 11 the lab "
             "prints 6, 12, 20, 30, 42, 56, 72, 90, 110, and the comparisons per character are "
             "exactly `m/2` &mdash; rising without limit. Knuth&ndash;Morris&ndash;Pratt on the "
             "same family makes `3(m − 1)` comparisons, which is 1.5 per character in every "
             "row."),
        ],
        "read_title": "Attaining the bound, and then earning the word quadratic",
        "read_intro": "The construction and its proof, the table that cannot show what it looks like it shows, and the family that can.",
        "body": [
            ("def", ("The adversarial pair",
                     "For a letter `a` and a different letter `b`, write `a^k` for the string "
                     "of `k` copies of `a`. The <strong>adversarial pair</strong> at pattern "
                     "length `m` is the text `a^N` for some `N &ge; m` together with the "
                     "pattern `a^(m − 1) b`. Every character of the text is `a`; the pattern "
                     "agrees with the text on its first `m − 1` characters at every offset and "
                     "disagrees on its last.")),
            ("thm", ("The adversarial pair attains the bound",
                     "On the text `a^N` with the pattern `a^(m − 1) b`, the naive matcher makes "
                     "exactly `m(N − m + 1)` comparisons and reports no match &mdash; which is "
                     "the maximum possible for those two lengths.")),
            ("proof", ("Fix an alignment at offset `i`, which exists for `0 &le; i &le; N − m`. "
                       "For `k &lt; m − 1` the comparison of `t[i+k]` with `p[k]` is `a` "
                       "against `a` and succeeds, so the inner loop reaches `k = m − 1`.",
                       "At `k = m − 1` the comparison is `t[i+m−1] = a` against `p[m−1] = b`, "
                       "which fails. So the alignment makes exactly `m` comparisons and reports "
                       "nothing.",
                       "There are `N − m + 1` alignments, each costing `m`, so the total is "
                       "`m(N − m + 1)`. That is the upper bound proved on the opening page of "
                       "this module, so it is attained and cannot be improved.")),
            ("p", "At `N = 24` and `m = 5` this is `5 × 20 = 100`, and the panel's status line "
                  "says so in the strongest terms it has: the measured count IS the bound. No "
                  "other preset in this kit produces that sentence."),
            ("h3", "The table that looks like a quadratic and is not one"),
            ("p", "The first table repeats whatever is in the box 1 to 6 times with the pattern "
                  "unchanged. On the adversarial text it reads 100, 220, 340, 460, 580, 700 at "
                  "`n = 24, 48, 72, 96, 120, 144`. Those differences are 120 each and the "
                  "comparisons per character creep from 4.17 to 4.86. It is a line with a steep "
                  "slope."),
            ("thm", ("A fixed pattern makes the bound linear",
                     "With `m` held constant, `m(n − m + 1)` is a linear function of `n`, and "
                     "the naive matcher's count is at most that. So no family of inputs with a "
                     "fixed pattern can make the comparison count grow faster than linearly in "
                     "`n`.")),
            ("p", "This is the claim the kit's author withdrew after printing the numbers, and "
                  "the docstring records the withdrawal. It is worth being precise about what "
                  "was wrong: nothing in the six counts was mismeasured, and the growth really "
                  "is much steeper than on English text. What was wrong was the word. Four and "
                  "a half comparisons per character is a constant, and a constant times `n` is "
                  "not quadratic however large the constant is."),
            ("h3", "The family where m grows with n"),
            ("p", "The second table is fixed rather than read from the boxes, because a text "
                  "that reaches the bound has to be built and cannot be typed by accident. At "
                  "each `m` from 3 to 11 it takes the text `a^(2(m − 1))` and the pattern "
                  "`a^(m − 1) b`, so `n = 2(m − 1)` and the pattern is half the text."),
            ("math", [
                "  m      n      naive      m(n - m + 1)    per character   KMP",
                "  3      4          6            6              3/2          6",
                "  5      8         20           20              5/2         12",
                "  7     12         42           42              7/2         18",
                "  9     16         72           72              9/2         24",
                " 11     20        110          110             11/2         30",
            ]),
            ("p", "Read the arithmetic rather than the shape. The alignment count is "
                  "`n − m + 1 = 2(m − 1) − m + 1 = m − 1`, each alignment costs `m`, so the "
                  "total is `m(m − 1)` and equals the bound in every row. Per character that is "
                  "`m(m − 1)/(2(m − 1)) = m/2`, which grows without limit as the family is "
                  "extended. KMP's column is `3(m − 1)`, which is `1.5n`: flat per character, "
                  "in every row, for ever."),
            ("p", "That is the honest form of the quadratic claim. It is not &ldquo;naive "
                  "matching is quadratic&rdquo;, which is about an algorithm and is false on "
                  "almost every input anyone types. It is &ldquo;there is a family of inputs on "
                  "which naive matching's count is a constant times the product of the two "
                  "lengths, and that family is exhibited here&rdquo;. The lower table is the "
                  "exhibit and the upper table is not."),
            ("h3", "Horspool, for contrast, is at its best here"),
            ("p", "The third matcher takes 20 comparisons on the opening text, five times fewer "
                  "than naive's 100, and `m − 1` in every row of the family table. Its shift "
                  "table sends it forward by 1 each time, but it compares the window from the "
                  "right, so it meets the `b` first and fails immediately. The sibling lesson "
                  "&ldquo;The Text Where Nothing Is Skipped&rdquo; reverses the pattern's "
                  "letters and gets 130 comparisons on 30 characters, which is the same "
                  "algorithm at its worst on almost the same text."),
        ],
        "lab": ("strings", {
            "mode": "naive",
            "preset": "adversarial",
            "panel_title": "The input where the measurement and the bound are the same number",
            "panel_intro": "The bar chart is a solid block sitting on the dashed line, because "
                           "every alignment costs the full `m`. Read the two tables as answering "
                           "different questions: the upper one grows the text with the pattern "
                           "fixed and is linear by construction, and the lower one grows the "
                           "pattern with it and is the only place on this page where the "
                           "quadratic appears.",
        }),
        "steps_title": "Building a worst case, and naming its growth honestly",
        "steps_intro": "Construct the input from the bound rather than searching for it, then check which quantity you actually varied.",
        "steps": [
            ("Read the bound backwards to get the input",
             "`m(n − m + 1)` is attained when every alignment costs `m`, which means every "
             "alignment matches `m − 1` characters and fails on the last. Writing a text and "
             "pattern with that property is then mechanical rather than inventive."),
            ("Check that the failure really is at the last position",
             "A run of a's with the pattern `baaaa` also has 26 alignments, but each fails on "
             "the first comparison and the total is 26, not 130. Where the odd character sits "
             "in the pattern decides everything, and for the left-to-right matcher it has to "
             "sit at the end."),
            ("Name which quantity you varied before using the word quadratic",
             "If the pattern is fixed, the bound is linear and so is anything under it. A "
             "quadratic claim is a claim about a family in which both lengths move together, "
             "and it needs a row for each member of the family."),
            ("Read the per-character column, not the total",
             "Totals rise in both tables and that is uninformative. Comparisons per character "
             "is 4.17 rising to 4.86 in the upper table, which is a constant settling down, and "
             "`m/2` in the lower one, which is not."),
            ("Put a second algorithm in the same table",
             "KMP's column is what makes the lower table an argument rather than an "
             "observation: `m(m − 1)` beside `3(m − 1)` on the same inputs is the difference "
             "between an unbounded ratio and a fixed one."),
        ],
        "worked": {
            "title": "One hundred comparisons, and then the family that leaves it behind",
            "intro": [
                "The text is twenty-four a's and the pattern is `aaaab`, so `n = 24`, `m = 5`, "
                "and the alignments run from 0 to 19.",
            ],
            "lines": [
                "alignments              n - m + 1 = 24 - 5 + 1          = 20",
                "cost of one alignment   4 matches on 'a', 1 fail on 'b' =  5",
                "measured total          20 x 5                          = 100",
                "the bound               m(n - m + 1) = 5 x 20           = 100",
                "measured / bound                                        = 1",
                "",
                "repeat the text 1..6 times, pattern fixed:",
                "  n     24    48    72    96   120   144",
                "  cmp  100   220   340   460   580   700      differences 120: a line",
                "",
                "the family, m growing with n:      n = 2(m - 1)",
                "  m      3     5     7     9    11",
                "  cmp    6    20    42    72   110      = m(m - 1), = the bound",
                "  /char 3/2   5/2   7/2   9/2  11/2     = m/2, unbounded",
                "  KMP    6    12    18    24    30      = 3(m - 1), = 1.5n, flat",
            ],
            "after": [
                "The two blocks at the bottom are the same algorithm on inputs of the same kind, "
                "and only the second earns the word quadratic. If you cover the `m` row of the "
                "third block, the counts 6, 20, 42, 72, 110 look like nothing in particular; it "
                "is the fact that `n` is tied to `m` that makes them `n^2/4` in disguise.",
                "For a faded rehearsal, work out what the family looks like at `m = 13`. The "
                "supplied first move is `n = 2(m − 1) = 24`, which is the same length as the "
                "opening text. Give the naive count, the bound, the per-character figure and "
                "KMP's count, then check them against the lab by extending the family in your "
                "head rather than on screen &mdash; the table stops at 11.",
                "Then do the harder one. Keep `m = 5` and ask what text of length 24 makes naive "
                "matching cost as little as possible. The answer is not unique and the minimum "
                "is 20, one comparison per alignment; say which texts achieve it, and notice "
                "that the bound is 100 for every one of them.",
            ],
        },
        "quiz_title": "Attaining a bound, and what growth means",
        "quiz": [
            {"q": "Repeating the adversarial text 1 to 6 times gives counts 100, 220, 340, 460, 580, 700. What does that establish?",
             "a": ["That naive matching is quadratic in n",
                   "That with m fixed the count grows linearly in n, here at about 4.8 comparisons per character",
                   "That the adversarial text stops being adversarial as it gets longer",
                   "That the bound m(n − m + 1) has been exceeded"],
             "c": 1,
             "why": "The differences are a constant 120, which is a line. It could not be "
                    "anything else: with `m` fixed the bound itself is linear in `n`, and the "
                    "count is under the bound. The text stays adversarial throughout &mdash; "
                    "the count equals the bound in every one of those six rows."},
            {"q": "In the family where the text is a^(2(m − 1)) and the pattern is a^(m − 1) b, what is the comparison count?",
             "a": ["m(m + 1), because there are m + 1 alignments",
                   "m(m − 1), because there are m − 1 alignments each costing m",
                   "2m(m − 1), because the text has length 2(m − 1)",
                   "m^2, because the pattern is half the text"],
             "c": 1,
             "why": "The alignment count is `n − m + 1` with `n = 2(m − 1)`, which is "
                    "`2m − 2 − m + 1 = m − 1`. Each of those costs the full `m`, so the total is "
                    "`m(m − 1)`, and that equals `m(n − m + 1)`, the bound. At `m = 11` it is "
                    "110 on a text of 20 characters, which is the lab's last row."},
            {"q": "The pattern is changed from `aaaab` to `baaaa` on the same run of a's. What happens to the naive count?",
             "a": ["It stays at 100: the pattern has the same characters",
                   "It falls to 26, because every alignment now fails on its first comparison",
                   "It rises, because b now has to be matched first",
                   "It becomes 130, which is what Horspool makes on that input"],
             "c": 1,
             "why": "Naive matching compares left to right, so a pattern beginning with the "
                    "absent character fails immediately at every alignment: on a 30-character "
                    "run that is 26 comparisons. 130 is Horspool's count on the same input, "
                    "because it compares from the right and meets the four matching a's first "
                    "&mdash; the mirror image, and the subject of a later page."},
            {"q": "Why does the lab build the second table from a fixed family rather than from the text in the box?",
             "a": ["Because typing is slow",
                   "Because an input that attains the bound has to be constructed, and no edit of an arbitrary text grows m with n",
                   "Because the reader's text might be too long",
                   "Because the quadratic only appears for the letter a"],
             "c": 1,
             "why": "The claim the table supports is about a family indexed by `m`, so both "
                    "lengths have to move together under the table's control. Repeating "
                    "whatever is in the box grows `n` alone, which is the upper table, and no "
                    "amount of it produces a family."},
        ],
        "mistakes": [
            ("Calling a steep line a quadratic",
             "Four and a half comparisons per character is a large constant and constants do not "
             "change the order of growth. The test is whether the per-character figure keeps "
             "rising: in the upper table it settles near 4.86, in the lower one it is `m/2` and "
             "has no ceiling."),
            ("Believing the worst case is rare because it looks contrived",
             "It is contrived, and it is also exactly what a periodic input looks like &mdash; "
             "runs of one symbol, or a short cycle repeated, which is what DNA, binary sensor "
             "traces and padded records are made of. &ldquo;Unlikely for English prose&rdquo; is "
             "a claim about a distribution of inputs, and it is not a claim the bound makes or "
             "needs."),
            ("Reading `m(n − m + 1)` as `nm`",
             "They differ by `m(m − 1)`, which is 20 on the opening text and 110 at the bottom "
             "of the family table, where `nm` is 220 and the true bound is 110 &mdash; a factor "
             "of two. The looser form is usually harmless as an order of growth and is wrong as "
             "a number, and this page is about the number."),
        ],
        "standard": ("Finish when you can construct a worst-case input for any m and say exactly which table earns the word quadratic.",
                     "You should be able to build the adversarial pair from the bound rather "
                     "than recall it, prove that it attains `m(n − m + 1)`, explain why a fixed "
                     "pattern forces linear growth, derive `m(m − 1)` and `m/2` for the family, "
                     "and say what KMP's flat 1.5 per character means beside it."),
        "note": ("This closes the naive matcher. Everything in the rest of the course is an "
                 "answer to the same question: what to do with the `m − 1` characters this "
                 "algorithm matched and threw away. &ldquo;Borders, and the Failure Function "
                 "Built&rdquo; keeps them by remembering how much of the pattern is still "
                 "aligned; &ldquo;Shifting by More Than One&rdquo; jumps past positions no "
                 "match can start at; and &ldquo;A Rolling Hash, and a Collision You Can "
                 "Read&rdquo; stops comparing characters altogether."),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "borders-and-the-failure-function",
        "title": "Borders, and the Failure Function Built",
        "module": "Preprocessing the pattern",
        "one_line": "Define the longest proper border of every prefix, compute it twice — once by trying every length and once in linear time — and check the two columns against each other.",
        "summary": (
            "A border of a string is a proper prefix that is also a suffix. `fail[k]` is the "
            "length of the longest border of the first `k` characters, and it is the entire "
            "content of Knuth&ndash;Morris&ndash;Pratt: after a mismatch the pattern slides so "
            "that `fail[k]` characters still line up and the text pointer never moves back. "
            "The lab builds the array in linear time and, in the same table, finds every "
            "border by trying every length."
        ),
        "key": [
            "border of s: a proper prefix of s that is also a suffix of s",
            "fail[k] = length of the longest border of the first k characters",
            "ababaca:  fail = 0, 0, 1, 2, 3, 0, 1     on prefixes of length 1 to 7",
            "the fallback chain from the whole pattern:  7 -> 1 -> 0",
            "on a mismatch after k matched, retry at fail[k]; i never decreases",
            "measured: KMP 34 comparisons, naive 61, on the same 29-character text",
        ],
        "key_label": "One array, computed two ways, and what it is for",
        "concepts_intro": (
            "The hard idea is the border itself. The other two are the slide it licenses and "
            "the reason the fast construction has to be checked against the slow one."
        ),
        "concepts": [
            ("A border is a prefix that is also a suffix, and shorter than the whole",
             "For `ababa` the borders are `aba` and `a`, the longest being `aba`. For `abc` "
             "there are none but the empty string. The word <em>proper</em> matters: the whole "
             "string is trivially a prefix and a suffix of itself and is excluded, otherwise "
             "every string would have a border of its own length and the definition would carry "
             "no information. Borders are what makes a partial match reusable: if the first "
             "`k` characters of the pattern matched and `fail[k] = 3`, then three characters of "
             "the pattern are already aligned at the new position without a single comparison."),
            ("The failure function is that length for every prefix at once",
             "`fail[k]` is the longest border of `p[0..k−1]`, one number for each `k` from 0 to "
             "`m`. On `ababaca` the seven values are 0, 0, 1, 2, 3, 0, 1: the prefix `abab` has "
             "border `ab` of length 2, `ababa` has `aba` of length 3, and `ababac` has none at "
             "all because it ends in `c`. Following the array from `m` gives the fallback "
             "chain `7 → 1 → 0`, which is every length at which the pattern can still be "
             "aligned after a mismatch at its end."),
            ("A linear construction has to be checked against the definition",
             "Computing `fail[]` in `O(m)` is a three-line loop whose correctness is not "
             "obvious. Computing it by trying every one of the `k − 1` candidate lengths and "
             "comparing two substrings is obvious and cubic. The lab's table prints both "
             "columns for every prefix and reports how many rows disagree; on the presets that "
             "number is 0, and a construction that is fast and right is only interesting once "
             "the second half has been demonstrated rather than assumed."),
        ],
        "read_title": "Borders, the array, and the slide it licenses",
        "read_intro": "The definition, the two constructions, the theorem that makes the slide safe, and the counts on the text beside it.",
        "body": [
            ("def", ("Border",
                     "A string `b` is a <strong>border</strong> of a string `s` if `b` is both "
                     "a prefix and a suffix of `s` and `b` is shorter than `s`. The empty "
                     "string is a border of every non-empty string, so the set of borders is "
                     "never empty and &ldquo;the longest border&rdquo; is always defined.")),
            ("def", ("The failure function",
                     "For a pattern `p` of length `m`, the <strong>failure function</strong> is "
                     "the array `fail[0..m]` in which `fail[k]` is the length of the longest "
                     "border of the prefix `p[0..k−1]`. By convention `fail[0]` is treated as "
                     "before the start and `fail[1] = 0`, since a single character has only the "
                     "empty border.")),
            ("example", ("Seven prefixes of ababaca",
                         "The prefixes are `a`, `ab`, `aba`, `abab`, `ababa`, `ababac` and "
                         "`ababaca`, and their longest borders are the empty string, the empty "
                         "string, `a`, `ab`, `aba`, the empty string and `a`. So `fail[1..7]` is "
                         "0, 0, 1, 2, 3, 0, 1. The rise from 0 to 3 across the middle is the "
                         "pattern's periodicity; the collapse to 0 at `ababac` is the `c`, which "
                         "occurs nowhere else, so no prefix ending in `c` can be matched by a "
                         "prefix starting with `a`.")),
            ("p", "The lab's table puts that column beside a second one computed from the "
                  "definition: for each `k`, try `k − 1`, then `k − 2`, down to 1, and stop at "
                  "the first length where `p[0..j−1]` equals `p[k−j..k−1]` as strings. It is "
                  "`O(m^3)` and it is obviously right. The panel reports that the two agree on "
                  "all 7 prefixes."),
            ("thm", ("The slide is safe",
                     "Suppose the pattern is aligned at text offset `i` and its first `k` "
                     "characters have matched, so `t[i..i+k−1] = p[0..k−1]`, and the comparison "
                     "at `k` fails. Then no offset strictly between `i` and `i + k − fail[k]` "
                     "can begin a match, and at offset `i + k − fail[k]` the first `fail[k]` "
                     "characters already agree.")),
            ("proof", ("Let `j` be an offset with `i &lt; j &lt; i + k`, and suppose a match "
                       "begins at `j`. The match's first `i + k − j` characters lie inside the "
                       "region already known to equal `p[0..k−1]`, so `p[0..i+k−j−1]` equals "
                       "`t[j..i+k−1]`, which equals `p[j−i..k−1]`.",
                       "That says `p[0..i+k−j−1]` is both a prefix of the pattern and a suffix "
                       "of `p[0..k−1]`, so it is a border of `p[0..k−1]` of length `i + k − j`. "
                       "Since `fail[k]` is the longest such border, `i + k − j &le; fail[k]`, "
                       "which rearranges to `j &ge; i + k − fail[k]`.",
                       "So no offset before `i + k − fail[k]` can start a match, and at that "
                       "offset the border itself is the `fail[k]` characters already in place. "
                       "The matcher therefore sets `k` to `fail[k]` and leaves the text pointer "
                       "where it is.")),
            ("p", "That last clause is the property the previous module leaned on. The text "
                  "pointer only ever advances, so the number of comparisons that succeed or "
                  "advance it is at most `n`; the rest are fallbacks, and the bound `2n` "
                  "follows. The lab prints both, and on the opening text it reports 34 "
                  "comparisons against a bound of 58."),
            ("h3", "The fallback chain, and why it is every alignment worth trying"),
            ("p", "Applying `fail` repeatedly from `m` gives `7 → 1 → 0` on this pattern. Each "
                  "step is the longest border of the one before, and by the theorem above every "
                  "length in that chain is an alignment at which the pattern could still match "
                  "while no length outside it can. The chain is short here because `ababaca` has "
                  "one short border; on `aaaaa` it is `5 → 4 → 3 → 2 → 1 → 0`, every length "
                  "there is."),
            ("h3", "The counts on the text below"),
            ("p", "The panel searches `abababacaba ababacaab ababaca`, 29 characters, and finds "
                  "3 occurrences at offsets 2, 12 and 22. KMP makes 34 character comparisons and "
                  "the naive matcher makes 61 on the same input, so KMP is ahead by 27 here. "
                  "The bound `2n` is 58, and the measured 34 sits well under it."),
            ("p", "Read those four numbers as four different kinds of statement. 34 is a "
                  "measurement. 61 is another measurement, of a different algorithm on the same "
                  "input. 58 is a theorem about KMP on every text of 29 characters. And 27 is "
                  "the difference between two measurements, which is the one number of the four "
                  "that does not generalise at all &mdash; the sibling lesson &ldquo;Where the "
                  "Simple Algorithm Wins&rdquo; has it at negative 4."),
            ("h3", "What the second column is protecting against"),
            ("p", "The linear construction is short enough to look self-evident and subtle "
                  "enough to be wrong in a way that survives testing: an off-by-one in the "
                  "fallback gives an array that is correct on most patterns and too small on "
                  "periodic ones, and a matcher using a too-small `fail[]` still finds every "
                  "match, just slowly. The failure mode is invisible in the output and visible "
                  "only in the count."),
            ("p", "So the table compares against the definition on every keystroke, over "
                  "whatever pattern you type, and prints the number of rows where the two "
                  "disagree. Type a pattern of your own and watch the count stay at 0; that is "
                  "the check being exercised rather than merely present."),
        ],
        "lab": ("strings", {
            "mode": "kmp",
            "preset": "ababaca",
            "panel_title": "Type a pattern, and watch its borders appear one prefix at a time",
            "panel_intro": "The bar chart is one bar per prefix and its height is that prefix's "
                           "longest border, found by trying every length. The table puts the "
                           "linear-time `fail[k]` beside it, row by row, so the fast "
                           "construction is checked against the definition rather than trusted "
                           "&mdash; and the slider walks the construction forward one character "
                           "at a time.",
        }),
        "steps_title": "Finding a border, and then finding all of them",
        "steps_intro": "Do one prefix by hand before running anything. The array is the same operation repeated, and the operation is short.",
        "steps": [
            ("Write the prefix out and fold it",
             "For `ababa`, try length 4: `abab` against `baba` &mdash; no. Length 3: `aba` "
             "against `aba` &mdash; yes. Stop at the first success, because you are counting "
             "down from the longest."),
            ("Build the array left to right, not prefix by prefix",
             "The linear construction extends the previous answer: if `p[k]` continues the "
             "current border it lengthens by 1, and otherwise the border falls back along the "
             "chain. Doing each prefix independently is the checking column, not the algorithm."),
            ("Read the chain before reading the array",
             "`7 → 1 → 0` says more about how the pattern behaves under mismatch than the seven "
             "numbers do. It is the complete list of alignments that survive a failure at the "
             "end of the pattern."),
            ("Check the two columns on your own pattern, not just on the preset",
             "The agreement on `ababaca` is a fact about `ababaca`. Type something periodic, "
             "something with a repeated block, and something with no repeats at all, and watch "
             "the disagreement count stay at 0 on each."),
        ],
        "worked": {
            "title": "Every border of every prefix of ababaca, by hand",
            "intro": [
                "The pattern is `ababaca`, seven characters, indexed from 1 for the prefix "
                "lengths. For each prefix the longest proper border is found by trying lengths "
                "downwards and comparing the two substrings as strings.",
            ],
            "lines": [
                "k  prefix    candidate lengths tried          longest border  fail[k]",
                "1  a         (none)                           empty                 0",
                "2  ab        1: a vs b  no                    empty                 0",
                "3  aba       2: ab vs ba no; 1: a vs a yes    a                     1",
                "4  abab      3: aba vs bab no; 2: ab vs ab    ab                    2",
                "5  ababa     4: abab vs baba no; 3: aba=aba   aba                   3",
                "6  ababac    5,4,3,2,1 all fail on the c      empty                 0",
                "7  ababaca   6..2 fail; 1: a vs a yes         a                     1",
                "",
                "fail[1..7]                                    0 0 1 2 3 0 1",
                "linear construction                           0 0 1 2 3 0 1",
                "rows where they disagree                      0",
                "fallback chain from 7                         7 -> 1 -> 0",
            ],
            "after": [
                "Row 6 is the one to look at twice. Five candidate lengths are tried and all "
                "five fail, for the same reason each time: the prefix ends in `c` and every "
                "candidate suffix must therefore end in `c`, while every candidate prefix "
                "begins with `a`. A single character occurring once in the pattern collapses "
                "the border to nothing.",
                "For a faded rehearsal, do `aabaaab` the same way. The supplied first move: "
                "`aa` has border `a`, so `fail[2] = 1`, and then the `b` at position 3 takes it "
                "straight back to 0. Complete the seven rows, give the fallback chain, and then "
                "check them against the lab by switching the preset.",
                "Then try `abcabcabd`, where the border climbs to 5 before the final `d` "
                "destroys it in one step. Predict `fail[8]` and `fail[9]` before running it, and "
                "say which single character of the pattern is responsible for the collapse.",
            ],
        },
        "quiz_title": "Borders, the array, and the slide",
        "quiz": [
            {"q": "What is the longest border of `abab`?",
             "a": ["`abab`, since a string is a prefix and a suffix of itself",
                   "`ab`, of length 2",
                   "`a`, of length 1",
                   "`aba`, of length 3"],
             "c": 1,
             "why": "A border must be a PROPER prefix, so the whole string is excluded by "
                    "definition. `aba` is a prefix but not a suffix of `abab`; `ab` is both, and "
                    "it is longer than `a`, so it is the longest. This is `fail[4] = 2` in the "
                    "table."},
            {"q": "The pattern is aligned at offset i, k characters have matched, and the next comparison fails. What does KMP do?",
             "a": ["It moves the text pointer back to i + 1 and starts again",
                   "It sets the matched length to fail[k] and leaves the text pointer where it is",
                   "It shifts the pattern by k and clears the matched length to 0",
                   "It shifts by 1 and rechecks the k characters it already matched"],
             "c": 1,
             "why": "Setting `k` to `fail[k]` is exactly the slide the theorem licenses: every "
                    "offset in between has been ruled out, and at the new offset `fail[k]` "
                    "characters already agree. The text pointer never decreases, which is what "
                    "holds the total under `2n`. Clearing to 0 would be correct but would throw "
                    "away the border and cost more."},
            {"q": "The lab's table prints fail[k] beside the longest border found by trying every length, and reports 0 disagreements on your pattern. What has been shown?",
             "a": ["That the linear construction is correct",
                   "That on this pattern the two agree, which is evidence for the construction and not a proof of it",
                   "That the cubic construction is unnecessary",
                   "That the pattern has no borders"],
             "c": 1,
             "why": "The comparison is run on the pattern in the box, so it is a measurement on "
                    "one input &mdash; the same distinction this course draws between a count "
                    "and a bound. What it does do is catch the realistic failure, an off-by-one "
                    "that makes `fail[]` too small on periodic patterns, and it catches it on "
                    "whatever pattern the reader types."},
            {"q": "Why does a matcher using a fail[] array that is too small still report the right matches?",
             "a": ["It does not; the matches would be wrong",
                   "Because a smaller fallback is a shorter slide, which only re-examines offsets that were already ruled out",
                   "Because the matches are checked against a scan over every offset",
                   "Because fail[] does not affect which offsets are tried"],
             "c": 1,
             "why": "Sliding less far than the theorem permits is conservative: it tries offsets "
                    "that cannot match, wastes comparisons, and still finds everything. That is "
                    "why the defect is invisible in the output and visible only in the count "
                    "&mdash; and why the page prints the count."},
        ],
        "mistakes": [
            ("Including the whole string among the borders",
             "Every string is a prefix and a suffix of itself, so allowing that would make "
             "`fail[k] = k` for every `k` and the matcher would never advance. The word "
             "<em>proper</em> is doing real work in the definition, and dropping it turns the "
             "algorithm into an infinite loop rather than into a slower one."),
            ("Reading fail[k] as an index rather than a length",
             "`fail[5] = 3` on `ababaca` means the longest border of the first five characters "
             "has length 3, so after a mismatch three characters are already matched and the "
             "next comparison is at pattern position 3. Treating it as &ldquo;go to index "
             "3&rdquo; happens to give the same answer only because lengths and zero-based "
             "next-indices coincide here; on a one-based reading it is off by one everywhere."),
            ("Assuming the failure function says something about the text",
             "It is computed from the pattern alone, before the text is looked at. Two texts "
             "searched for the same pattern share the identical array, which is why the "
             "construction cost `O(m)` is paid once and why the lab's upper table does not move "
             "when you retype the text."),
        ],
        "standard": ("Finish when you can build the array by hand for a pattern you have not seen and justify the slide it licenses.",
                     "You should be able to state what a border is and why proper matters, "
                     "compute `fail[]` by trying every length, read the fallback chain off it, "
                     "prove that no offset between `i` and `i + k − fail[k]` can start a match, "
                     "and say why a too-small array is a performance defect rather than a "
                     "correctness one."),
        "note": ("The construction itself has a claim attached that this page has not tested: "
                 "that building `fail[]` costs `O(m)` rather than `O(m^2)`, even though the "
                 "fallback loop inside it can run several times for one character. "
                 "&ldquo;The Amortised Bound, as a Count&rdquo; measures those inner iterations "
                 "directly and puts them beside `2m`."),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "the-amortised-bound-as-a-count",
        "title": "The Amortised Bound, as a Count",
        "module": "Preprocessing the pattern",
        "one_line": "The inner loop of the failure-function construction can run many times for one character; count the total and put it beside 2m.",
        "summary": (
            "&ldquo;Amortised&rdquo; is the claim that a loop which sometimes runs many times "
            "runs few times in total, and the only honest evidence for it is the total. The "
            "lab counts every inner-loop iteration while building `fail[]`. On `aabaaab` it "
            "reports 2 against a bound of `2m = 14`; across all five patterns the kit ships, "
            "the largest total is also 2. The bound is correct and the measurements are "
            "nowhere near it, and both of those facts need saying."
        ),
        "key": [
            "the inner loop lowers k; the outer loop raises it by at most 1 per character",
            "so total falls ≤ total rises ≤ m − 1, and inner iterations ≤ 2m overall",
            "aabaaab:  fail = 0, 1, 0, 1, 2, 2, 3   inner iterations = 2   bound 14",
            "the chain from the whole pattern:  7 -> 3 -> 0",
            "on the text: KMP 19 comparisons, naive 42, bound 2n = 36",
            "across the five shipped patterns the largest inner total is 2, never 14",
        ],
        "key_label": "A loop inside a loop, and the argument that it is still linear",
        "concepts_intro": (
            "The hard idea is the potential argument: nothing bounds one step, and the sum is "
            "bounded anyway. The other two are what the count is and why it sits so far below."
        ),
        "concepts": [
            ("No bound on one step, and a bound on the sum",
             "While building `fail[]` at character `i`, the inner loop follows the fallback "
             "chain as far as it has to: on `aaaaab` that is several steps at one character, and "
             "there is no useful ceiling on a single character's work other than `m`. The claim "
             "is about the sum over the whole construction, and the argument never looks at an "
             "individual step. `k` rises by at most 1 per character of the pattern, so across "
             "the whole loop it rises by at most `m − 1`; every inner iteration strictly lowers "
             "`k`, and `k` never goes below 0; so the number of inner iterations is at most the "
             "total rise, `m − 1`. Adding the one comparison per character gives the `2m` the "
             "panel prints."),
            ("The measured total is the only honest evidence for an amortised claim",
             "A page can say &ldquo;amortised `O(m)`&rdquo; and show a pattern where the inner "
             "loop runs twice at one character, which demonstrates nothing in either direction. "
             "What settles it is the sum: on `aabaaab` the construction performs 2 inner "
             "iterations in total, on `ababaca` 2, on `abcabcabd` 2, and on `aaaaa` and "
             "`abcdefg` none at all. Every one of those is far under `2m`, and it is the total "
             "rather than the worst character that the bound is about."),
            ("Far under the bound is the normal case, and does not make the bound loose",
             "2 against 14 is a factor of seven, and the bound cannot be improved to a constant: "
             "patterns exist for which the inner loop runs a number of times proportional to "
             "`m`. What the gap shows is that the amortised argument is doing its work in the "
             "worst case and is invisible in the ordinary one &mdash; which is precisely why "
             "the argument has to be a proof and not a survey of examples."),
        ],
        "read_title": "Counting the loop nobody can bound one step at a time",
        "read_intro": "The construction, the potential argument, the measured totals across every pattern the kit ships, and where the two meet.",
        "body": [
            ("p", "The construction walks `i` from 1 to `m − 1` holding `k`, the length of the "
                  "current border. If `p[i]` equals `p[k]` the border extends and `k` rises by "
                  "1. If not, `k` falls to `fail[k]` and the test is repeated &mdash; that "
                  "repetition is the inner loop, and it is the only part of the algorithm whose "
                  "cost is not one per character."),
            ("thm", ("The inner loop runs at most m − 1 times in total",
                     "Over the whole construction of `fail[]` for a pattern of length `m`, the "
                     "number of inner-loop iterations is at most `m − 1`, so the total work is "
                     "at most `2m − 1` operations and the construction is `O(m)`.")),
            ("proof", ("Take `k` as a potential. It starts at 0 and is never negative, because "
                       "the inner loop stops at 0 and `fail[j] &ge; 0` for every `j`.",
                       "The outer loop runs `m − 1` times and each iteration increases `k` by at "
                       "most 1, so the total increase over the whole construction is at most "
                       "`m − 1`.",
                       "Every inner-loop iteration sets `k` to `fail[k]`, which is strictly less "
                       "than `k` because a border of `p[0..k−1]` is shorter than it. So each "
                       "inner iteration decreases the potential by at least 1. Since the total "
                       "decrease cannot exceed the total increase plus the starting value, the "
                       "number of inner iterations is at most `m − 1`.")),
            ("p", "The panel prints that total under the name inner-loop iterations and the "
                  "bound beside it as `2m`. The bound it prints is the looser `2m` rather than "
                  "`m − 1` because it is counting the outer comparison as well, and because "
                  "`2m` is the form the claim is usually quoted in."),
            ("example", ("Seven prefixes of aabaaab, and where the chain is followed",
                         "The pattern is `aabaaab` and `fail[1..7]` comes out 0, 1, 0, 1, 2, 2, "
                         "3. The inner loop fires at exactly two places: at the `b` in position "
                         "3, where the border of length 1 cannot be extended and falls to 0, and "
                         "at position 6, where the border of length 2 cannot be extended by an "
                         "`a` and falls to 1 &mdash; from which the `a` does extend it back to "
                         "2. One iteration each, two in total, against a bound of 14.")),
            ("h3", "The same count on the other patterns the kit ships"),
            ("math", [
                "pattern      m    fail[1..m]              inner   bound 2m",
                "ababaca      7    0 0 1 2 3 0 1               2         14",
                "aaaaa        5    0 1 2 3 4                   0         10",
                "abcabcabd    9    0 0 0 1 2 3 4 5 0           2         18",
                "aabaaab      7    0 1 0 1 2 2 3               2         14",
                "abcdefg      7    0 0 0 0 0 0 0               0         14",
            ]),
            ("p", "Two of the five never enter the inner loop at all. `aaaaa` never needs to, "
                  "because every character extends the border; `abcdefg` never needs to, because "
                  "`k` is 0 at every step and the loop's guard is `k &gt; 0`. The three that do "
                  "enter it enter it twice, and on `ababaca` and `abcabcabd` those two "
                  "iterations both happen at a single character, while on `aabaaab` they are one "
                  "at each of two characters."),
            ("p", "That distinction is worth holding on to, because it is where an amortised "
                  "argument earns its keep. A pattern whose chain is followed twice at one "
                  "character has a step the per-character reasoning cannot bound; a pattern "
                  "whose chain is followed once at each of two characters does not. Both have "
                  "the same total, and the total is what the theorem is about."),
            ("h3", "The construction is not the matching, and both are counted"),
            ("p", "The failure function costs `O(m)` and the search over the text costs `O(n)`, "
                  "and the panel keeps them in separate counters because they are separate "
                  "claims with separate proofs. On the text `aabaaabaaabaabaaab`, 18 characters, "
                  "the search makes 19 comparisons against a bound of `2n = 36` and finds 3 "
                  "occurrences at offsets 0, 4 and 11. The naive matcher makes 42 on the same "
                  "input."),
            ("p", "So the full accounting for KMP on this input is 2 inner iterations plus the 6 "
                  "outer comparisons to build the array, and then 19 comparisons to search: "
                  "under 30 operations where naive matching spends 42 comparisons alone. The "
                  "preprocessing is cheap here, and on a long text it is negligible &mdash; "
                  "which is the practical reason the failure function is built at all rather "
                  "than the theoretical one."),
            ("h3", "Why the search bound is 2n and not n"),
            ("p", "The search loop has the same shape as the construction: one comparison per "
                  "text character, plus a fallback loop that lowers `k`. The same potential "
                  "argument applies with `k` rising at most once per text character, so the "
                  "fallbacks total at most `n` and the whole search is at most `2n`. The factor "
                  "of two is the fallbacks, and it is the price of never moving the text "
                  "pointer backwards."),
            ("p", "On this text the measured 19 is just over `n`, so almost all of those "
                  "comparisons advanced the text pointer and hardly any were fallbacks. On the "
                  "adversarial input from the previous module KMP made 44 comparisons on 24 "
                  "characters, which is close to `2n` and is the shape the bound was written "
                  "for."),
        ],
        "lab": ("strings", {
            "mode": "kmp",
            "preset": "aabaaab",
            "panel_title": "Build the array one character at a time and count the fallbacks",
            "panel_intro": "The counter marked inner-loop iterations is the total over the whole "
                           "construction, not the worst single character, and the counter beside "
                           "it is the proved `2m`. Move the slider to walk the construction "
                           "forward and watch which characters make the border fall rather than "
                           "rise.",
        }),
        "steps_title": "Reading an amortised claim without believing an example",
        "steps_intro": "Find the potential, check it only ever rises slowly, and then add up the falls.",
        "steps": [
            ("Name the quantity that rises and falls",
             "Here it is `k`, the current border length. Every amortised argument on this path "
             "has one: a potential that the cheap steps raise a little and the expensive steps "
             "consume. Naming it is most of the proof."),
            ("Bound the total rise, not the individual steps",
             "`k` rises by at most 1 per character of the pattern, so across the construction it "
             "rises by at most `m − 1`. That single sentence is what makes the falls bounded, "
             "and it is a statement about the loop's shape rather than about any pattern."),
            ("Count the falls in the lab, on more than one pattern",
             "The counter is a total. Type a pattern with a long repeated block, one with none, "
             "and one that is a single letter repeated, and watch the total stay far under `2m` "
             "on all three while the shape of the array changes completely."),
            ("Keep construction and search in separate columns",
             "`O(m)` to build and `O(n)` to search are two claims with two proofs, and the lab "
             "prints four counters for them rather than one. Adding them into a single figure "
             "hides which half a change affected."),
        ],
        "worked": {
            "title": "Two inner iterations, located exactly",
            "intro": [
                "The pattern is `aabaaab`. The construction runs `i` from 1 to 6 holding `k`, "
                "the current border length, and writes `fail[i + 1] = k` after each step.",
            ],
            "lines": [
                "i  p[i]  k before   inner iterations   k after   fail[i+1]",
                "1   a        0            0               1          1",
                "2   b        1            1  (1 -> 0)     0          0",
                "3   a        0            0               1          1",
                "4   a        1            0               2          2",
                "5   a        2            1  (2 -> 1)     2          2",
                "6   b        2            0               3          3",
                "",
                "fail[1..7]                                0 1 0 1 2 2 3",
                "inner iterations, total                   2",
                "the bound 2m                              14",
                "the fallback chain from 7                 7 -> 3 -> 0",
            ],
            "after": [
                "Look at row 5. The border is 2, meaning `aa` is both a prefix and a suffix of "
                "`aabaa`; the next character of the text-side is `a` and the next character of "
                "the border-side is `b`, so the border cannot extend and falls to `fail[2] = 1`. "
                "From length 1 the `a` does extend, so `k` ends at 2 &mdash; the same value it "
                "started with, after one iteration of the inner loop. Work was done and the "
                "potential did not change, which is exactly the case per-step reasoning cannot "
                "handle.",
                "For a faded rehearsal, run the same six rows for `ababaca`. The supplied first "
                "move: the first three characters give `k` values 0, 1, 2 with no inner "
                "iterations at all. Find the single character where the chain is followed twice, "
                "give the total, and check it against the lab by switching the preset.",
                "Then predict, before looking, what the total is for `aaaaa` and why. Say which "
                "clause of the inner loop's guard is responsible, and then say what that implies "
                "about patterns over a one-letter alphabet in general.",
            ],
        },
        "quiz_title": "Totals, potentials, and what a bound is bounding",
        "quiz": [
            {"q": "The lab reports 2 inner-loop iterations against a bound of 14. What does the 2 establish?",
             "a": ["That the construction is O(m)",
                   "That on this pattern the fallbacks totalled 2, which is consistent with the bound and does not prove it",
                   "That the bound 2m is far too generous and should be lowered",
                   "That the inner loop never runs more than twice"],
             "c": 1,
             "why": "It is a measurement of one pattern. The `O(m)` claim is established by the "
                    "potential argument, which holds for every pattern including ones where the "
                    "total is proportional to `m`. A count far below a bound is the normal case "
                    "and says nothing about whether the bound can be tightened."},
            {"q": "Which fact makes the total number of inner-loop iterations bounded?",
             "a": ["Each inner iteration is cheap",
                   "k rises by at most 1 per character and every inner iteration strictly lowers it, so the falls cannot exceed the rises",
                   "fail[k] is always much smaller than k",
                   "The inner loop is guarded by k > 0"],
             "c": 1,
             "why": "It is the accounting between rises and falls, not the size of either. "
                    "`fail[k]` need only be strictly less than `k`, not much less; and the guard "
                    "`k > 0` stops the loop but does not by itself bound how often it runs. The "
                    "cost of one iteration is irrelevant to how many there are."},
            {"q": "On `ababaca` and on `aabaaab` the inner-loop total is 2 in both cases. What differs between them?",
             "a": ["Nothing measurable; the two constructions do the same work",
                   "On ababaca both iterations happen at one character; on aabaaab they are one at each of two characters",
                   "One of the two arrays disagrees with the definition",
                   "ababaca has a longer fallback chain"],
             "c": 1,
             "why": "The totals coincide and the distribution does not, which is exactly the "
                    "distinction an amortised bound is built to ignore. `ababaca`'s chain is "
                    "followed twice at its sixth character; `aabaaab`'s is followed once at each "
                    "of two characters. Both arrays agree with the definition on every prefix."},
            {"q": "KMP's search bound is 2n rather than n. Where does the second n come from?",
             "a": ["From building the failure function",
                   "From the fallback loop, which lowers the matched length and is paid for by the same potential argument",
                   "From comparing each character twice, once forwards and once backwards",
                   "From the matches, each of which costs m"],
             "c": 1,
             "why": "One comparison per text character advances the pointer; the fallbacks are "
                    "the extra, and they total at most `n` by the same rise-and-fall accounting. "
                    "Building the array is counted separately and costs `O(m)`, and the text "
                    "pointer is never read backwards at all."},
        ],
        "mistakes": [
            ("Arguing the bound from the worst single character",
             "&ldquo;The inner loop can run `m` times, so the construction is `O(m^2)`&rdquo; is "
             "the error the potential argument exists to answer. One character really can cost "
             "`m`, and the sum over all characters still cannot exceed `m − 1`, because the "
             "expensive character has consumed rises that earlier cheap characters paid for."),
            ("Reading a small measured total as a tighter bound",
             "2 against 14 on five different patterns is five measurements, and the bound is "
             "about all patterns. Patterns exist whose construction really does perform a "
             "number of fallbacks proportional to `m`; none of them is among the presets, which "
             "is a fact about the presets."),
            ("Merging the construction cost into the search cost",
             "They are `O(m)` and `O(n)` and they are proved separately; the panel keeps four "
               "counters rather than one for that reason. A change to the fallback rule moves "
               "the first pair and leaves the second alone, and a single combined number would "
               "hide which."),
        ],
        "standard": ("Finish when you can state the potential, prove the total bound from it, and read the measured total as evidence rather than as the theorem.",
                     "You should be able to identify `k` as the quantity that rises slowly and "
                     "falls in the inner loop, bound the total rise at `m − 1`, conclude the "
                     "same for the falls, locate each inner iteration in a hand construction, "
                     "and say why a measured total of 2 neither establishes nor threatens the "
                     "bound of `2m`."),
        "note": ("Both of the preprocessing costs on this page are `O(m)` and both buy something "
                 "at search time. &ldquo;The Matcher as a Machine&rdquo; asks what happens if "
                 "you are willing to spend more than `O(m)` up front: writing out every "
                 "transition for every character of the alphabet removes the fallback loop "
                 "entirely and makes the search exactly one step per character, at a table cost "
                 "of `(m + 1)` times the alphabet size."),
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "the-matcher-as-a-machine",
        "title": "The Matcher as a Machine",
        "module": "Preprocessing the pattern",
        "one_line": "Write out every transition in advance and the search becomes exactly one table lookup per character, with no comparison and no back-up at all.",
        "summary": (
            "KMP still compares characters and still falls back. Precompute, for every state "
            "and every letter of the alphabet, how much of the pattern would then be matched, "
            "and both disappear: the run is `n` lookups whatever the text is. The cost is a "
            "table of `(m + 1)` times sigma cells. On the lab's opening pattern that is 18 "
            "cells against a run of 19 steps, and widening the alphabet grows the table while "
            "the run does not move."
        ),
        "key": [
            "one state per number of pattern characters matched: 0 to m",
            "delta(state, c) = the longest prefix of p that is a suffix of p[0..state−1] + c",
            "table size (m + 1) × sigma;  ababc over a, b, c is 6 × 3 = 18 cells",
            "the run is exactly n steps, 19 here, with no comparison anywhere",
            "state 4 on an a goes to 3, not to 0: the border is compiled into the table",
            "KMP made 21 comparisons on the same text; the automaton made 0",
        ],
        "key_label": "A table built once, and a run whose cost does not depend on the text",
        "concepts_intro": (
            "The hard idea is that the table is the failure function unrolled. The other two "
            "are what the run costs and what the table costs, and they move in opposite "
            "directions."
        ),
        "concepts": [
            ("A state is a matched length, and the transition is a longest-suffix question",
             "The machine has `m + 1` states, state `j` meaning that the last `j` characters "
             "read are exactly `p[0..j−1]` and no longer prefix of the pattern ends here. The "
             "transition from state `j` on character `c` is the length of the longest prefix of "
             "the pattern that is a suffix of `p[0..j−1]` followed by `c`. On `ababc` that makes "
             "`delta(4, a) = 3`, because `ababa` ends in `aba` which is a prefix of the pattern; "
             "the border is not consulted at run time because it has already been compiled into "
             "the cell."),
            ("The run is n steps, independent of the text",
             "Reading a character means one array lookup and one assignment. There is no "
               "comparison to succeed or fail and no fallback loop, so the work is the same on "
               "every text of the same length: the panel reports 19 steps for 19 characters, and "
               "it reports `n` steps for `n` characters on anything you type. This is the only "
               "matcher on the course whose count does not depend on the characters at all, "
               "which is worth noticing precisely because every other page here is about how "
               "much it does depend on them."),
            ("The table is the price, and it is charged per letter of the alphabet",
             "`(m + 1)` times sigma cells have to be written before a single character of the "
             "text is read. On `ababc` over three letters that is 18; on `the` over the thirteen "
             "distinct characters of its text it is 52, for a pattern less than half as long. "
             "KMP stores `m` numbers instead and pays a fallback loop at run time. That is the "
             "whole trade, and which side of it wins depends on the alphabet and on how long the "
             "text is &mdash; the panel prints table cells per text character so the comparison "
             "is a number rather than an intuition."),
        ],
        "read_title": "Compiling the pattern into a table, and reading the text once",
        "read_intro": "The construction, the proof that one step per character suffices, and the two costs that move in opposite directions.",
        "body": [
            ("def", ("The string-matching automaton",
                     "For a pattern `p` of length `m` over an alphabet `A`, the "
                     "<strong>matching automaton</strong> has states `0, 1, ..., m` and a "
                     "transition function `delta` defined by: `delta(j, c)` is the length of the "
                     "longest prefix of `p` that is a suffix of the string `p[0..j−1]` followed "
                     "by `c`. State `m` is accepting. The machine starts in state 0 and reads "
                     "the text one character at a time.")),
            ("p", "The definition is a statement about strings and mentions no algorithm, which "
                  "is why the table can be built by the obvious method &mdash; for each state "
                  "and each character, form the string and try every prefix length downwards "
                  "&mdash; and why the lab does exactly that, writing `(m + 1)` times sigma "
                  "cells and counting each write."),
            ("thm", ("The state after reading a prefix of the text is the longest match ending there",
                     "If the machine is started in state 0 and fed `t[0..i]`, it ends in the "
                     "state equal to the length of the longest prefix of `p` that is a suffix of "
                     "`t[0..i]`. Consequently it is in state `m` exactly when an occurrence of "
                     "`p` ends at position `i`.")),
            ("proof", ("By induction on `i`. Before anything is read the longest prefix of `p` "
                       "that is a suffix of the empty string is the empty prefix, of length 0, "
                       "and the machine is in state 0.",
                       "Suppose after `t[0..i−1]` the machine is in state `j`, the length of the "
                       "longest prefix of `p` that is a suffix of `t[0..i−1]`. Any prefix of `p` "
                       "that is a suffix of `t[0..i]` and has length at least 1 has its last "
                       "character equal to `t[i]` and its first part a suffix of `t[0..i−1]` "
                       "that is also a prefix of `p`, hence of length at most `j`.",
                       "So the candidates are exactly the prefixes of `p` that are suffixes of "
                       "`p[0..j−1]` followed by `t[i]`, and the longest of those is "
                       "`delta(j, t[i])` by definition. The machine moves there, which "
                       "completes the induction. State `m` then means the whole pattern is a "
                       "suffix of what has been read, which is an occurrence ending at `i`.")),
            ("example", ("Eighteen cells, and the transition that carries the border",
                         "The lab opens on the pattern `ababc` over the alphabet `{a, b, c}`, so "
                         "there are 6 states and 18 cells. The row for state 4 &mdash; `abab` "
                         "matched &mdash; reads `a → 3`, `b → 0`, `c → 5`. The first of those is "
                         "the interesting one: reading an `a` after `abab` gives `ababa`, whose "
                         "longest suffix that is a prefix of the pattern is `aba`, so the "
                         "machine drops to 3 rather than restarting at 0 or advancing to 5. "
                         "Everything the failure function would have computed at run time is "
                         "sitting in that cell.")),
            ("p", "The run over `abababcababcabababc` takes exactly 19 steps for 19 characters "
                  "and finds 3 occurrences, at offsets 2, 7 and 14. The counter for character "
                  "comparisons does not exist on this page, because the algorithm makes none."),
            ("h3", "The trade, in two numbers that move in opposite directions"),
            ("p", "KMP makes 21 comparisons on that same text and stores 5 numbers. The "
                  "automaton makes 0 comparisons, takes 19 steps, and stores 18. Neither is "
                  "dominant: the automaton is ahead on the run and behind on the setup, and "
                  "which matters depends on how many texts one table will be used for."),
            ("math", [
                "preset      pattern   m   sigma   states   cells   n    run   KMP   cells/char",
                "ababc       ababc     5     3        6       18   19     19    21     18/19",
                "aaab        aaab      4     2        5       10   15     15    18       2/3",
                "binary      10110     5     2        6       12   36     36    43       1/3",
                "distinct    abcd      4     4        5       20   14     14    16      10/7",
                "wide        the       3    13        4       52   38     38    40      26/19",
            ]),
            ("p", "Read the last two columns together. The run column is the text length in "
                  "every row, with no exceptions and no dependence on the characters. The cells "
                  "column moves by a factor of five across the same rows, and it moves with "
                  "sigma rather than with `m`: `the` is the shortest pattern in the table and "
                  "has the largest table, because its text uses thirteen distinct characters."),
            ("p", "The last column is cells per text character, and it is the number that "
                  "decides. Below 1 the table is cheaper than the text it will read; above 1 it "
                  "is not, and a single search would have been better served by KMP. The binary "
                  "preset sits at `1/3` and the wide one at `26/19`, on the same algorithm."),
            ("h3", "Why KMP is what actually gets used"),
            ("p", "The automaton's table is `(m + 1)` times sigma. For byte data that is 256 "
                  "cells per state, and for Unicode text it is not a table one writes out at "
                  "all. KMP stores `m` integers regardless of the alphabet and pays for it with "
                  "a fallback loop whose total cost is bounded by the same potential argument "
                  "that bounds the construction."),
            ("p", "So the automaton is the clearer explanation and the worse implementation, "
                  "and it is worth building once for exactly that reason: `delta(j, c)` is what "
                  "`fail[]` is compressing, and a reader who has seen the table knows what the "
                  "fallback chain is walking through."),
        ],
        "lab": ("strings", {
            "mode": "automaton",
            "preset": "ababc",
            "panel_title": "Read the whole transition table, then watch the machine walk the text",
            "panel_intro": "Every cell is the number of pattern characters that would be matched "
                           "after reading that character in that state, and the row highlighted "
                           "is where the machine stands at the position the slider picks. Widen "
                           "the alphabet by typing into the text box and watch the table grow "
                           "while the step count stays exactly `n`.",
        }),
        "steps_title": "Building a table, and pricing it against the text",
        "steps_intro": "Fill one row by hand before reading the panel's, then compare the two costs in the same unit.",
        "steps": [
            ("Fill one row from the definition",
             "For state `j` and character `c`, write down `p[0..j−1]` followed by `c` and then "
               "ask for the longest prefix of the pattern that is a suffix of it. Trying lengths "
               "downwards from `min(m, j + 1)` gets there in a few steps and needs no algorithm."),
            ("Check the accepting row and the zero row first",
             "State `m`'s row is the same as the row for the pattern's longest border, because "
               "after a full match the machine is exactly as far along as that border leaves it. "
               "State 0's row is 1 for `p[0]` and 0 everywhere else, always."),
            ("Count the cells before counting the steps",
             "`(m + 1)` times sigma is fixed by the pattern and the alphabet and is paid whether "
               "or not the text is ever read. A table of 52 cells for a text of 38 characters is "
               "a loss before the search begins."),
            ("Widen the alphabet, not the pattern, to see the cost move",
             "Adding one distinct character to the text adds `m + 1` cells and adds nothing to "
               "the run. That asymmetry is the whole argument for KMP, and it is visible in one "
               "keystroke."),
        ],
        "worked": {
            "title": "The eighteen cells of ababc, and one walk across the text",
            "intro": [
                "The pattern is `ababc` and the alphabet of the text and pattern together is "
                "`{a, b, c}`, so the machine has 6 states and the table has 18 cells. Each entry "
                "is the length of the longest prefix of `ababc` that is a suffix of the state's "
                "string followed by the column's character.",
            ],
            "lines": [
                "state  matched   a   b   c     why the a column is what it is",
                "  0     -        1   0   0     'a' is a prefix of length 1",
                "  1     a        1   2   0     'aa' ends in 'a'",
                "  2     ab       3   0   0     'aba' is a prefix of length 3",
                "  3     aba      1   4   0     'abaa' ends in 'a'",
                "  4     abab     3   0   5     'ababa' ends in 'aba'",
                "  5     ababc    1   0   0     'ababca' ends in 'a'",
                "",
                "cells         (m + 1) x sigma = 6 x 3            = 18",
                "writes to build it                               = 18",
                "text          abababcababcabababc, n             = 19",
                "steps to run it                                  = 19",
                "comparisons made                                 =  0",
                "KMP on the same text                             = 21",
                "matches at offsets                               = 2, 7, 14",
            ],
            "after": [
                "The cell to argue with is state 4 on an `a`. The naive intuition says a "
                "mismatch throws everything away and the machine restarts at state 1, having "
                "just read an `a`. The right answer is 3, because `ababa` ends in `aba` and "
                "`aba` is a prefix of the pattern &mdash; two characters of progress that the "
                "restart would have discarded. The same two characters are what "
                "`fail[4] = 2` encodes in the failure function.",
                "For a faded rehearsal, build the table for `aaab` over `{a, b}`. The supplied "
                "first move is the `a` column: from states 0, 1 and 2 it climbs 1, 2, 3, and "
                "from state 3 it stays at 3 rather than reaching 4, because `aaaa` is not a "
                "prefix of `aaab` but `aaa` is. Fill the `b` column, give the cell count, and "
                "check against the lab.",
                "Then do the pricing exercise. Keep the pattern `the` and add a single new "
                "distinct character to the text &mdash; a digit will do. Say by how many cells "
                "the table grows, by how many steps the run grows, and what happens to cells per "
                "text character. Then say which of those three you could have predicted without "
                "the lab.",
            ],
        },
        "quiz_title": "States, cells, and steps",
        "quiz": [
            {"q": "On the pattern `ababc`, what is delta(4, a) and why?",
             "a": ["0, because `a` does not continue `abab` towards the pattern",
                   "3, because `ababa` ends in `aba`, which is a prefix of the pattern",
                   "1, because the machine restarts and has just read an `a`",
                   "5, because state 4 plus one more character is a match"],
             "c": 1,
             "why": "The transition is a longest-suffix question, not a continue-or-restart one. "
                    "`abab` followed by `a` is `ababa`, whose longest suffix that is also a "
                    "prefix of `ababc` is `aba`. Restarting at 1 would be correct but would "
                    "discard two characters of progress, and that discarded progress is exactly "
                    "what the failure function stores."},
            {"q": "The same pattern is run against a text of 19 characters and then against a different text of 19 characters. What changes?",
             "a": ["The number of steps, because the second text may match more often",
                   "Nothing about the step count: it is 19 for any text of 19 characters",
                   "The table, because it depends on the text's alphabet",
                   "The number of comparisons, which depends on the characters"],
             "c": 1,
             "why": "One lookup per character, with no comparison and no fallback, so the run is "
                    "the text length exactly. The table can change if the second text introduces "
                    "new distinct characters &mdash; the lab builds it over the alphabet of the "
                    "text and pattern together &mdash; but the step count cannot."},
            {"q": "Pattern `the` over a 13-character alphabet gives 52 cells and a 38-character run; pattern `10110` over 2 characters gives 12 cells and a 36-character run. What is the lesson?",
             "a": ["Shorter patterns need bigger tables",
                   "The table grows with the alphabet rather than with the pattern, and the run grows with neither",
                   "Binary data is always faster to search",
                   "The automaton is better on small alphabets and worse on long patterns"],
             "c": 1,
             "why": "`(m + 1)` times sigma has both factors in it, and between those two rows "
                    "sigma moved by a factor of 6.5 while `m` moved by less than 2 in the other "
                    "direction. The run is the text length in both rows, which is what makes the "
                    "cells-per-character column the one that decides."},
            {"q": "Why is KMP preferred in practice despite making comparisons the automaton avoids?",
             "a": ["Because it finds matches the automaton misses",
                   "Because it stores m numbers rather than (m + 1) times sigma cells, and its extra work is bounded by 2n anyway",
                   "Because the automaton is only correct for small alphabets",
                   "Because building the table is quadratic"],
             "c": 1,
             "why": "Space is the deciding factor: for byte data the table is 256 cells per "
                    "state, and the fallback loop KMP pays instead is bounded by the same "
                    "potential argument that bounds its construction. Both algorithms find "
                    "exactly the same matches, and the lab checks both against a scan over every "
                    "offset."},
        ],
        "mistakes": [
            ("Thinking a mismatch sends the machine to state 0",
             "It sends it to whatever the cell says, which is often neither 0 nor the state "
             "before. `delta(4, a) = 3` on `ababc` is the example on screen: the machine loses "
             "one character of progress, not four. Every cell of the table is a separate "
             "longest-suffix computation and none of them is a restart rule."),
            ("Counting the table as part of the search cost",
             "The table is built once from the pattern and is independent of the text, so a "
             "program searching a thousand documents for one pattern pays 18 cells once and 19 "
             "steps a thousand times. The cells-per-character figure on the panel is for a "
             "single search, and it is the pessimistic reading."),
            ("Treating sigma as a property of the pattern",
             "The lab builds the table over the characters of the text and pattern together, "
             "because a transition is needed for every character the machine might read. "
             "Pasting a text with an accented letter in it widens every row, and the pattern "
             "has not changed at all."),
        ],
        "standard": ("Finish when you can fill a transition row from the definition and price the table against the text in one unit.",
                     "You should be able to state what state `j` means, compute `delta(j, c)` as "
                     "a longest-suffix question, prove that the machine's state is the longest "
                     "match ending at the current position, give the cell count as "
                     "`(m + 1)` times sigma, and say why the run is `n` steps on every text."),
        "note": ("That closes the pattern-preprocessing module: three matchers that all read "
                 "every character of the text, differing only in what they remember. The next "
                 "module gives that up. &ldquo;Shifting by More Than One&rdquo; skips over "
                 "characters without reading them at all, which buys a large saving on ordinary "
                 "text and buys no guarantee whatsoever &mdash; its worst case is the same "
                 "`m(n − m + 1)` the naive matcher has."),
    },
]
