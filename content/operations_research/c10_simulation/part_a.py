"""Simulation and Variance Reduction, the first five lessons - the stream, the
estimate, the error bar, and one system run.

The generator first, because every figure later on is a function of it; then the
estimate and the only interval this path can justify; then a queue run as a
calendar rather than as a formula, and the bias that a run started empty puts in
its own average. Every figure below is read off the `simulate` kit, which draws
from a seeded stream and reports exact fractions.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "random-numbers-and-inverse-transform-sampling",
        "title": "Random Numbers and Inverse-Transform Sampling",
        "module": "Where the numbers come from",
        "one_line": "Turn a recurrence into fractions, and let the cumulative table decide which value each one is.",
        "summary": (
            "A simulation has no randomness in it. It has a recurrence, a seed, and a "
            "table: `xₙ₊₁ = (a·xₙ + c) mod m` produces integers, `U = x/m` turns one into "
            "a fraction in `[0, 1)`, and the sampled value is the first outcome whose "
            "cumulative probability reaches `U`. Both halves are exact, so a run is "
            "reproducible from its seed and every count in it is a ratio of whole numbers "
            "&mdash; and the period of the recurrence decides whether the table is being "
            "sampled at all."
        ),
        "key": [
            "xₙ₊₁ = (a·xₙ + c) mod m        a = 25173, c = 13849, m = 65536, seed 1",
            "39022, 61087, 20196, 45005     the first four integers, exactly",
            "U = x/m = 19511/32768          a fraction, never a decimal",
            "F = 1/16, 5/16, 11/16, 15/16, 1        the cumulative table IS the sampler",
            "U in [5/16, 11/16)  ⟹  the sampled value is 2",
            "full period ⟺ gcd(c, m) = 1, every prime of m divides a − 1, and 4 | m ⟹ 4 | a − 1",
        ],
        "key_label": "One recurrence, one table, and the certificate underneath",
        "concepts_intro": (
            "Three ideas, and the third is the one that decides whether anything later on "
            "this course means anything: the sampler is the table, and a shortcut that "
            "does not read the probability column samples a different distribution."
        ),
        "concepts": [
            ("A pseudorandom stream is a recurrence, and the seed is all of it",
             "`xₙ₊₁ = (a·xₙ + c) mod m` is a function, not a source of chance. Fix `a`, "
             "`c`, `m` and the seed and every draw in the run is determined &mdash; which "
             "is a feature, because it is what makes a simulation reproducible, "
             "debuggable, and comparable with a second simulation. Nothing on this course "
             "would work if the numbers were genuinely unrepeatable."),
            ("U = x/m is a fraction, and keeping it one keeps everything after it exact",
             "`39022/65536` is `19511/32768` and it is not `0.5954`. Every statistic taken "
             "of a run &mdash; a count, a frequency, a sample mean, a sample variance "
             "&mdash; is then a ratio of whole numbers, and the page can print it in full "
             "rather than in a form the reader has to take on trust."),
            ("The cumulative table is the sampler",
             "Build `F(k) = p₀ + ⋯ + p_k` and return the first `k` with `U &lt; F(k)`. "
             "The band `[F(k−1), F(k))` has width exactly `p_k`, so the outcome comes out "
             "with exactly its own probability. The tempting shortcut &mdash; "
             "`⌊k·U⌋ + 1` &mdash; never looks at the probability column at all, and "
             "therefore samples the uniform distribution on `k` values whatever table is "
             "on the page."),
        ],
        "read_title": "A recurrence, a fraction, and the band it falls in",
        "read_intro": "Where the numbers come from, what turns them into outcomes, and the condition that decides whether the stream is long enough to be one.",
        "body": [
            ("def", ("Linear congruential generator",
                     "A <strong>linear congruential generator</strong> is the recurrence "
                     "`xₙ₊₁ = (a·xₙ + c) mod m` started from a seed `x₀`. The multiplier "
                     "`a`, the increment `c` and the modulus `m` fix the whole sequence. "
                     "Its <strong>period</strong> is the number of values before it "
                     "returns to a state it has already been in, and it is at most `m`.")),
            ("p", "Discrete Mathematics built this object in &ldquo;Hashing and "
                  "Pseudorandom Numbers&rdquo;, and the lab on this page lets you set all "
                  "three parameters and watch what they do. What is new here is the use it "
                  "is put to: this is the only supply of numbers a simulation has, and "
                  "every figure on the eight pages after this one is a function of it."),
            ("def", ("Inverse-transform sampling",
                     "Given a distribution on values `v₀ &lt; v₁ &lt; ⋯` with "
                     "probabilities `p₀, p₁, …`, build the cumulative table "
                     "`F(k) = p₀ + ⋯ + p_k`. To sample: draw `U = x/m` and return the "
                     "first `v_k` with `U &lt; F(k)`. The method is called "
                     "<em>inverse-transform</em> because it is applying the inverse of the "
                     "cumulative function to a uniform draw.")),
            ("p", "The correctness argument is one line and is worth having in front of "
                  "you, because it is what the shortcut breaks. `U` is uniform on "
                  "`[0, 1)`, so the probability that it lands in the band "
                  "`[F(k−1), F(k))` is the width of that band, which is `p_k` by "
                  "construction. Every outcome therefore comes out with its own "
                  "probability, and the bands are read off the table rather than assumed."),
            ("p", "Two properties of the method matter later and are easy to miss now. It "
                  "consumes exactly one draw per sampled value, so two runs that sample "
                  "the same number of things read the same number of draws &mdash; which "
                  "is what makes &ldquo;Common Random Numbers&rdquo; possible. And it is "
                  "<strong>monotone in U</strong>: a larger `U` never returns a smaller "
                  "value. That is the condition &ldquo;Antithetic Variates&rdquo; stands "
                  "on, and it is a property of this sampler rather than a lucky fact."),
            ("h3", "The comparison is made in whole numbers"),
            ("p", "`U &lt; F(k)` is `x/m &lt; n/d`, which is `x·d &lt; n·m`, and both "
                  "sides are integers. Nothing in the sampler ever becomes a decimal, so "
                  "there is no tie a rounding could decide wrongly. The modulus the rest "
                  "of this course uses is odd, so `U` is never exactly `1/2` either, and "
                  "no comparison on any of these pages has a boundary case at all."),
            ("thm", ("Hull-Dobell conditions, as Discrete Mathematics states them",
                     "A linear congruential generator has full period `m` from every seed "
                     "if and only if `gcd(c, m) = 1`, every prime dividing `m` also "
                     "divides `a − 1`, and `a − 1` is divisible by 4 whenever `m` is. This "
                     "course quotes the condition and checks it; the statement belongs to "
                     "&ldquo;Hashing and Pseudorandom Numbers&rdquo;, which states it "
                     "without proof, and so does this page.")),
            ("p", "The condition needs `c ≠ 0`, and the reason is worth a sentence because "
                  "the generator the rest of this course uses has `c = 0`. Zero is a fixed "
                  "point of `x ↦ a·x mod m`, so a purely multiplicative generator can "
                  "never visit it and its best possible period is `m − 1`. Set the lab's "
                  "generator to `a = 16807`, `c = 0`, `m = 2147483647` and the first "
                  "condition reads as a failure: `gcd(0, m) = m`. That is the theorem "
                  "declining to apply, not the generator being bad."),
            ("example", ("A generator with a period of one",
                         "Set `a = 2`, `c = 4`, `m = 16`. From seed 1 the stream is `6, 0, "
                         "4, 12, 12, 12, …`: four values and then a constant forever. All "
                         "three conditions fail &mdash; `gcd(4, 16) = 4`, and `a − 1 = 1` "
                         "is divisible neither by 2 nor by 4. A sampler fed that stream "
                         "returns `2, 0, 1, 3, 3, 3, …`, which is not a sample of any "
                         "table; it is one cycle, repeated, with a frequency column that "
                         "looks like data.")),
            ("h3", "What the run actually produced"),
            ("math", ["  a = 25173,  c = 13849,  m = 65536,  seed 1,  200 draws",
                      "",
                      "  band edges over m:   4096    20480    45056    61440    65536",
                      "                      1/16     5/16     11/16    15/16      1",
                      "",
                      "  x = 39022      20480 ≤ 39022 < 45056       value 2",
                      "  x = 61087      45056 ≤ 61087 < 61440       value 3",
                      "  x = 20196       4096 ≤ 20196 < 20480       value 1",
                      "  x = 45005      20480 ≤ 45005 < 45056       value 2",
                      "",
                      "  counts    10,  42,  86,  49,  13",
                      "  mean      413/200 = 2.065          true mean 2",
                      "  largest gap between an empirical frequency and its probability",
                      "            11/200, at the value 2"]),
            ("p", "The fourth draw is the one to look at. `45005` is `51` short of `45056`, "
                  "so it lands in the third band rather than the fourth by a margin of "
                  "fifty-one parts in sixty-five thousand. In whole numbers that is a "
                  "settled question; in floating point it is a question about the last "
                  "bit of a double, and the answer decides which outcome the reader is "
                  "shown."),
            ("p", "The gap of `11/200` between the empirical frequency of the value `2` "
                  "and its probability `6/16` is not an error and not something to "
                  "apologise for. It is what two hundred draws of this table look like. "
                  "How large such a gap can honestly be is the subject of the two pages "
                  "after this one, and the answer is the first thing on this path that "
                  "arrives as an interval rather than as a number."),
        ],
        "lab": ("simulate", {
            "mode": "sample",
            "preset": "binomial16",
            "generator": "turbo",
            "panel_title": "Set the three parameters, then watch each draw land in its band",
            "panel_intro": "The panel opens on the worked example: `a = 25173`, "
                           "`c = 13849`, `m = 65536`, seed 1, two hundred draws from the "
                           "table `1, 4, 6, 4, 1` over `16`. Every line above can be "
                           "checked against it. Then set the generator to `a = 2`, "
                           "`c = 4`, `m = 16` and read the frequency column of a stream "
                           "with a period of one.",
        }),
        "steps_title": "Sampling a table, by hand",
        "steps_intro": "Four steps, and the first is the one that is usually skipped.",
        "steps": [
            ("Check the generator before you use it",
             "Run the Hull-Dobell conditions on `a`, `c` and `m`, or, for a multiplicative "
             "generator, check that the modulus is prime and the multiplier is a primitive "
             "root. A short period is not a small inaccuracy: the run stops being a sample "
             "and becomes a cycle, and nothing downstream complains."),
            ("Build the cumulative table once, and keep it",
             "`F(k) = p₀ + ⋯ + p_k`, ending at exactly `1`. If the last entry is not `1` "
             "the probabilities do not sum to one and the bug is in the model, not in the "
             "sampler."),
            ("Turn each integer into a fraction, not a decimal",
             "`U = x/m` as a ratio of whole numbers. Every comparison after this is "
             "`x·d &lt; n·m` in the integers, which has no rounding in it and no boundary "
             "case to guess at."),
            ("Return the first band U reaches, and record which one",
             "The first `k` with `U &lt; F(k)`. Keeping the band alongside the value is "
             "what makes a disputed draw checkable afterwards, and it costs nothing."),
            ("Count the outcomes and compare with the probabilities",
             "Empirical frequency against probability, as fractions, with the difference "
             "shown. That difference is the thing the next two pages put a bound on; "
             "looking at it now is what makes the bound mean something later."),
        ],
        "worked": {
            "title": "Two hundred draws from 1, 4, 6, 4, 1 over 16",
            "intro": [
                "The table has mean exactly `2` and variance exactly `1`, which is why it "
                "is the one five of this course's nine panels open on: every theoretical "
                "standard error built on it is a fraction rather than a surd, and the "
                "halving of that standard error is a fact rather than a measurement.",
            ],
            "lines": [
                "table       value    0      1      2      3      4",
                "            p       1/16   4/16   6/16   4/16   1/16",
                "            F       1/16   5/16  11/16  15/16      1",
                "",
                "over m = 65536 the band edges are whole numbers",
                "            edges   4096  20480  45056  61440  65536",
                "",
                "stream      39022, 61087, 20196, 45005, 3882, 21259, …",
                "",
                "draw 1      x = 39022   20480 ≤ x < 45056     value 2",
                "draw 2      x = 61087   45056 ≤ x < 61440     value 3",
                "draw 3      x = 20196    4096 ≤ x < 20480     value 1",
                "draw 4      x = 45005   20480 ≤ x < 45056     value 2",
                "                        and 45005 is 51 short of the next edge",
                "",
                "after 200 draws",
                "  value      0       1       2       3       4",
                "  count     10      42      86      49      13",
                "  count/n   1/20  21/100  43/100  49/200  13/200",
                "  p         1/16    1/4     3/8     1/4    1/16",
                "  diff    −1/80   −1/25  +11/200 −1/200  +1/400",
                "",
                "  sample mean 413/200 = 2.065          true mean 2",
            ],
            "after": [
                "Every entry in that table is exact. The counts are integers, the "
                "frequencies are those integers over two hundred, and the differences are "
                "fractions with denominators no larger than four hundred. Nothing here is "
                "a measurement of the generator; it is the generator's output, written "
                "down.",
                "The sample mean is `413/200`, which is `2.065`, against a true mean of "
                "`2`. That is a discrepancy of `13/200` on two hundred draws. Is it large? "
                "The honest answer at this point in the course is that nothing on this "
                "page can say, and the next page is about the smallest thing that can.",
                "For a faded rehearsal, set the generator to `a = 5`, `c = 3`, `m = 16` "
                "&mdash; small enough to walk by hand. The supplied first move is that "
                "all three conditions hold, so the period is the full `16` and the stream "
                "from seed 1 is `8, 11, 10, 5, 12, 15, 14, 9, 0, 3, 2, 13, …`. Work out "
                "the first four sampled values by comparing `x` against the band edges "
                "over `m = 16` &mdash; they are `1, 5, 11, 15, 16` &mdash; and say why a "
                "modulus of sixteen cannot sample this table faithfully however long you "
                "run it, before the panel's frequency column tells you.",
            ],
        },
        "quiz_title": "Streams, bands and periods",
        "quiz": [
            {"q": "A run samples a five-outcome table by computing `⌊5·U⌋` and using it as an index. What distribution is being sampled?",
             "a": ["The stated table, provided the probabilities sum to one",
                   "The uniform distribution on the five outcomes, whatever the table says",
                   "The stated table, but with the first and last outcomes swapped",
                   "Nothing well defined, because `⌊5·U⌋` can be `5`"],
             "c": 1,
             "why": "`⌊5·U⌋` splits `[0, 1)` into five equal bands and never reads the "
                    "probability column, so every outcome comes out with probability "
                    "`1/5`. It is a correct sampler of the wrong distribution, which is "
                    "why nothing about the run looks broken. (`U &lt; 1` throughout, so "
                    "`⌊5·U⌋` is at most `4`; the fourth choice is a different worry and it "
                    "is unfounded.)"},
            {"q": "The lab's generator is set to `a = 2`, `c = 4`, `m = 16` and the frequency column still shows four different outcomes with different counts. What has been demonstrated?",
             "a": ["That the generator is adequate, since the outcomes are not all equal",
                   "That the table is being sampled correctly but slowly",
                   "Nothing about sampling: the counts are a fixed cycle repeated, and reseeding is what exposes it",
                   "That the modulus is too small but the multiplier is fine"],
             "c": 2,
             "why": "The stream is `6, 0, 4, 12, 12, 12, …`. The frequency column counts "
                    "one short prefix and then two hundred copies of the same value, and "
                    "it looks exactly like data. Uneven counts are not evidence of "
                    "sampling; a period is what has to be checked, and the certificate is "
                    "what checks it."},
            {"q": "Why does this course draw from `a = 16807`, `c = 0`, `m = 2147483647` on every page except this one?",
             "a": ["Because the Hull-Dobell conditions hold for it, giving the full period `m`",
                   "Because the modulus is prime, so reducing a draw modulo a small number samples rather than cycles",
                   "Because a multiplicative generator is faster than a mixed one",
                   "Because it is the only generator whose draws are exact fractions"],
             "c": 1,
             "why": "The Hull-Dobell conditions <em>fail</em> for it, and cannot do "
                    "otherwise with `c = 0`; its period is `m − 1`, attained because the "
                    "multiplier is a primitive root. The reason it is used is the low "
                    "bits: this course reduces draws modulo small numbers, and the low "
                    "bits of a power-of-two modulus are a cycle rather than a sample."},
            {"q": "A draw gives `x = 45005` with `m = 65536`, and the third band ends at `45056`. Which value is sampled, and how is the question settled?",
             "a": ["The third band's value, settled by `45005 &lt; 45056` in whole numbers",
                   "The fourth band's value, since `45005/65536` rounds to `0.6875`",
                   "Either, since the two are within a rounding error of each other",
                   "The third band's value, settled by comparing decimals to four places"],
             "c": 0,
             "why": "`U &lt; F(k)` is `x·d &lt; n·m` in the integers, and `45005 &lt; "
                    "45056` is not a close call in whole numbers even though it is fifty-"
                    "one parts in sixty-five thousand. The two wrong answers that invoke "
                    "rounding are describing an implementation that has already lost the "
                    "property this course is built on."},
        ],
        "mistakes": [
            ("Reaching for the index shortcut",
             "`⌊k·U⌋ + 1` is the first thing most people write and it ignores the "
             "probability column entirely. On the table `1, 4, 6, 4, 1` over `16` it "
             "returns each of the five outcomes a fifth of the time, so the middle outcome "
             "is under-sampled by `3/8 − 1/5 = 7/40` per draw and every expectation "
             "computed from the run is wrong by a fixed amount that no number of draws "
             "removes."),
            ("Treating a short period as a small inaccuracy",
             "A generator whose period is `1` does not produce a slightly worse sample; it "
             "produces no sample. The lab's `a = 2, c = 4, m = 16` returns the same "
             "outcome one hundred and ninety-seven times out of two hundred and prints a "
             "frequency column reading `1`, `1`, `1`, `197`, `0`, which a reader can "
             "mistake for a violently skewed distribution rather than for a dead stream."),
            ("Storing U as a decimal because the fraction is unreadable",
             "`19511/32768` is harder to read than `0.5954` and it is the only form in "
             "which the comparison against `11/16` has a definite answer. The library's "
             "convention is to keep the fraction and print a decimal beside it where a "
             "reader needs one &mdash; and to say, every time, whether the decimal is the "
             "exact value shown short or a genuine rounding."),
        ],
        "standard": ("Finish when a run's frequency column reads as a fact about the generator as much as about the table.",
                     "You should be able to run a linear congruential generator by hand "
                     "for four steps, check the Hull-Dobell conditions on its parameters "
                     "and say which fail, build a cumulative table and sample from it by "
                     "comparing whole numbers, explain in one line why the band `[F(k−1), "
                     "F(k))` gives outcome `k` its own probability, and say what the "
                     "index shortcut samples instead."),
        "note": 'Everything from here on treats the stream as settled and asks what to do with what it produces. &ldquo;Monte Carlo and the Standard Error&rdquo; takes the same two hundred draws, computes the sample mean, and then does the thing this page could not: puts a number on how far that mean can be from the truth.',
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "monte-carlo-and-the-standard-error",
        "title": "Monte Carlo and the Standard Error",
        "module": "The estimate and its error bar",
        "one_line": "Average the draws, then compute the standard error of the average and watch it fall like one over root n.",
        "summary": (
            "A simulation's output is a random variable. Averaging `n` draws estimates the "
            "expectation, and the estimator's own variance is `σ²/n`, so its standard "
            "deviation &mdash; the <strong>standard error</strong> &mdash; falls like "
            "`1/√n`. Four times the runs buy half the width and no more, and the "
            "estimate without that number beside it is a number with no claim attached."
        ),
        "key": [
            "X̄ₙ = (X₁ + ⋯ + Xₙ)/n        an estimator, and itself a random variable",
            "Var(X̄ₙ) = σ²/n              exact, and proved in Discrete Probability",
            "SE = σ/√n                    the standard error: one root, and it is the only one",
            "σ² = 1 on this table  ⟹  SE = 1/10, 1/20, 1/40 at n = 100, 400, 1600",
            "SE(n) / SE(4n) = 2           exact, because squaring removes both roots",
            "half the width costs 4n draws                 and there is no cheaper route",
        ],
        "key_label": "One estimator, and the rate at which it improves",
        "concepts_intro": (
            "Three ideas, and the middle one is the arithmetic. The first and the third "
            "are about what the arithmetic does and does not promise, which is where this "
            "course differs from every other one on the path."
        ),
        "concepts": [
            ("The output of a simulation is a random variable, not an answer",
             "Run it again with a different seed and it changes. So the thing to report is "
             "not the number but the number together with a statement about the spread of "
             "the process that produced it &mdash; and that statement is computable from "
             "the same run, which is the whole of Monte Carlo output analysis."),
            ("The estimator's variance is the population variance over n",
             "`Var(X̄ₙ) = σ²/n` exactly, for independent draws. Discrete Probability "
             "proves it in &ldquo;Variance and Standard Deviation&rdquo;: the variance of "
             "a sum of independent variables adds, and dividing by `n` scales a variance "
             "by `1/n²`. The standard error is the square root of that, and it is the one "
             "quantity on this page that is not a fraction."),
            ("One over root n is a rate, and it is a slow one",
             "Halving the width of an interval takes four times the runs; getting one more "
             "decimal digit takes a hundred times. That is not a defect of the method to "
             "be engineered around &mdash; it is the rate, it is proved, and the only way "
             "to beat it is to change the estimator rather than to buy draws, which is "
             "what the second half of this course does."),
        ],
        "read_title": "An estimate, and the width that goes with it",
        "read_intro": "What the sample mean estimates, how far it can be from the thing it estimates, and how fast that distance shrinks.",
        "body": [
            ("def", ("Monte Carlo estimator",
                     "Draw `X₁, …, Xₙ` independently from the distribution of interest and "
                     "report `X̄ₙ = (X₁ + ⋯ + Xₙ)/n`. It is <strong>unbiased</strong>: "
                     "`E[X̄ₙ] = μ` for every `n`, so it is aimed at the right number from "
                     "the first draw.")),
            ("def", ("Standard error",
                     "The <strong>standard error</strong> of an estimator is the standard "
                     "deviation of the estimator itself, not of the data. For the sample "
                     "mean it is `√(σ²/n) = σ/√n`. Where `σ²` is unknown it is estimated "
                     "by the sample variance `s² = Σ(Xᵢ − X̄)²/(n − 1)`, and the estimate "
                     "of the standard error is `√(s²/n)`.")),
            ("p", "The `n − 1` is not a fudge. The sample mean has already been fitted to "
                  "the same data, so one degree of freedom has been spent, and dividing by "
                  "`n` would make `s²` systematically too small. On four hundred draws the "
                  "difference is a fraction of a percent; on four draws it is a quarter, "
                  "which is why the convention is worth keeping even where it looks like "
                  "pedantry."),
            ("thm", ("The variance of the sample mean",
                     "For independent draws with variance `σ²`, `Var(X̄ₙ) = σ²/n`. Hence "
                     "the standard error is `σ/√n`, and multiplying `n` by four divides it "
                     "by exactly two.")),
            ("p", "That is proved in Discrete Probability and it is not reproved here; "
                  "what this page adds is the measurement. Squaring removes both roots, so "
                  "the ratio of the standard error at `n` to the standard error at `4n` is "
                  "`√((σ²/n)·(4n/σ²)) = 2` whatever `σ²` is. The panel prints that ratio "
                  "as an exact `2` at every step, which is the difference between checking "
                  "a claim and asserting it."),
            ("h3", "Exactly one number on this page is rounded, and it says so"),
            ("p", "The sample mean is a fraction. The sample variance is a fraction. The "
                  "standard error is the square root of a fraction, and a square root of a "
                  "rational is either rational or irrational with nothing in between. So "
                  "it is carried as an exact surd and printed twice: the surd, then a "
                  "decimal with the word <em>rounded</em> attached. Everything else that "
                  "prints as a decimal on these pages says &ldquo;exact, shown to `N` "
                  "places&rdquo; instead, and the distinction is load-bearing &mdash; a "
                  "reader who has seen &ldquo;rounded&rdquo; used loosely cannot tell "
                  "which figures really are."),
            ("example", ("The same stream, read at three lengths",
                         "On the table `1, 4, 6, 4, 1` over `16`, from the standard stream "
                         "at seed 1: at `n = 100` the sample mean is `21/10` and the "
                         "sample variance is `113/99`, giving a standard error of "
                         "`(1/330)√1243 ≈ 0.10684`; at `n = 400`, `413/200` and "
                         "`43031/39900`, giving `(1/79800)√17169369 ≈ 0.05192`; at "
                         "`n = 1600`, `3231/1600` and `2528639/2558400`, giving "
                         "`(1/2558400)√4043293761 ≈ 0.02485`. The three decimals are "
                         "rounded and the six fractions are not.")),
            ("p", "Beside those sit the theoretical standard errors, which on this table "
                  "are `1/10`, `1/20` and `1/40` exactly, because `σ² = 1` and `100`, "
                  "`400` and `1600` are squares. The estimates track them without matching "
                  "them, which is the correct behaviour: `s²` is itself an estimate, and "
                  "an estimate of a standard error has a standard error."),
            ("math", ["  n        sample mean    s²                SE                 σ/√n",
                      "  100      21/10          113/99            ≈ 0.10684          1/10",
                      "  400      413/200        43031/39900       ≈ 0.05192          1/20",
                      "  1600     3231/1600      2528639/2558400   ≈ 0.02485          1/40",
                      "",
                      "  ratio of one theoretical SE to the next:  2,  then 2",
                      "  exactly 2, because (σ²/n) / (σ²/4n) = 4 and the root of 4 is 2"]),
            ("h3", "What the shrinking does not mean"),
            ("p", "More draws do not converge <em>to</em> the answer. They shrink the "
                  "spread of a random quantity, which is a different promise: a single "
                  "long run can and does land further from the truth than a short one, and "
                  "at `n = 400` this stream is `13/200` out while the same length at seed 4 is "
                  "`3/400` out and at seed 0 is `3/40` out. The estimator is unbiased at "
                  "every `n`; it is the width that improves."),
            ("p", "And a running mean that has stopped moving has not converged. A settled-"
                  "looking trace is exactly what a small sample of a slow process "
                  "produces, and the flat stretch is evidence of nothing at all. The "
                  "interval is the evidence; the picture is a picture."),
            ("p", "The same `1/√n` turns up wherever a quantity is measured rather than "
                  "computed. A thousand requests cannot separate a success rate of `99.9%` "
                  "from one of `99.8%`, for precisely the reason four times the runs buy "
                  "twice the precision here &mdash; and the arithmetic that settles the "
                  "simulation question settles the measurement one unchanged."),
        ],
        "lab": ("simulate", {
            "mode": "montecarlo",
            "preset": "binomial16",
            "panel_title": "Run the same stream three lengths, and read the ratio column",
            "panel_intro": "The trace is the running mean against the exact expectation, "
                           "inside a ribbon of one standard error that narrows like "
                           "`1/√n`. The table reads the same stream at `100`, `400` and "
                           "`1600` draws; the last column is the ratio of one theoretical "
                           "standard error to the next, and it is an exact `2` because "
                           "squaring removes both roots. Drag the seed and watch every "
                           "figure except that ratio move.",
        }),
        "steps_title": "Reporting a simulated estimate",
        "steps_intro": "Four steps. The last one is the one that turns a number into a result.",
        "steps": [
            ("Average the draws, and keep the average as a fraction",
             "`X̄ₙ = (ΣXᵢ)/n`. On a seeded stream this is a ratio of whole numbers and "
             "there is no reason to lose that; `413/200` is checkable and `2.065` is a "
             "claim about a checkable thing."),
            ("Compute the sample variance with n − 1 in the denominator",
             "`s² = Σ(Xᵢ − X̄)²/(n − 1)`. Also exact. This is the estimate of the spread "
             "of a single draw, and it is not yet anything about the estimate."),
            ("Divide by n, then take the root, and label the root",
             "`SE = √(s²/n)`. This is the only irrational quantity produced so far, and "
             "the only honest way to print it is the exact form followed by a decimal with "
             "the rounding named."),
            ("Decide the budget from the width, not the other way round",
             "The width you need fixes `n` through `n = σ²/SE²`. Halving the target width "
             "multiplies the budget by four; an extra decimal digit multiplies it by a "
             "hundred. Discovering that after the runs have been bought is the expensive "
             "order to do it in."),
            ("Report the estimate and the width together, always",
             "`2.065` on its own is not a result. `2.065` with a standard error of about "
             "`0.052` from four hundred draws of a stated stream is one, because a reader "
             "can tell whether it answers their question."),
        ],
        "worked": {
            "title": "Four hundred draws, and the cost of halving the width",
            "intro": [
                "The table has `μ = 2` and `σ² = 1` exactly, so the theoretical standard "
                "errors are fractions and the halving can be checked rather than "
                "believed. Everything below is the panel's opening state at seed 1.",
            ],
            "lines": [
                "n = 400 draws from 1, 4, 6, 4, 1 over 16,  seed 1",
                "",
                "  sample mean       413/200   = 2.065",
                "  exact mean        2",
                "  this run is out by  13/200  = 0.065",
                "",
                "  sample variance   43031/39900",
                "  standard error    sqrt( (43031/39900) / 400 )",
                "                  = (1/79800) sqrt(17169369)",
                "                  ≈ 0.05192            (rounded — the only rounding here)",
                "  exact sigma/root n  1/20 = 0.05        (not rounded: 400 is a square)",
                "",
                "the same stream, read at three lengths",
                "  n       sample mean     s²                 SE",
                "  100     21/10           113/99             ≈ 0.10684",
                "  400     413/200         43031/39900        ≈ 0.05192",
                "  1600    3231/1600       2528639/2558400    ≈ 0.02485",
                "",
                "  theoretical:  1/10,  1/20,  1/40     ratios exactly 2 and 2",
                "",
                "  to halve 0.05192 you need 1600 draws, not 800",
            ],
            "after": [
                "The ratio column is the point of running the same stream at three "
                "lengths. Neither `1/10` nor `1/20` needs a root on this table, but the "
                "ratio is exactly `2` for <em>any</em> table, because `(σ²/n)` divided by "
                "`(σ²/4n)` is `4` and the roots cancel. A claim that survives not knowing "
                "`σ²` is worth more than one measured on a convenient example.",
                "The three sample standard errors are `0.10684`, `0.05192` and `0.02485`. "
                "Their ratios are about `2.058` and `2.089`, not `2`. That is not a "
                "failure of the theorem: `s²` is an estimate and it moves, so the ratio of "
                "two estimated standard errors is itself an estimate. The exact `2` lives "
                "in the theoretical column, and the difference between the two columns is "
                "the difference between a fact and a measurement of it.",
                "For a faded rehearsal, switch the panel's table to the skewed one &mdash; "
                "`1/2` on the first outcome and the rest falling away. The supplied first "
                "move is that its exact variance is `367/256`, which is not a square over "
                "`400`, so the theoretical standard error becomes `(1/320)√367 ≈ 0.05987` "
                "and is itself rounded for printing. Say what happens to the ratio column, "
                "and why, before the panel shows you.",
            ],
        },
        "quiz_title": "Rates, roots and what an estimate claims",
        "quiz": [
            {"q": "A run of `1000` draws gives a standard error of `0.04`. About how many draws are needed for a standard error of `0.01`?",
             "a": ["`4000`", "`8000`", "`16000`", "`40000`"],
             "c": 2,
             "why": "The standard error falls like `1/√n`, so dividing it by four "
                    "multiplies `n` by sixteen. `4000` divides the width by two, not by "
                    "four; `40000` would divide it by about six and a third and buys more "
                    "than was asked for."},
            {"q": "Two runs of the same model give `2.065` and `2.031`. Which is the better estimate?",
             "a": ["The one closer to `2`, since `2` is the exact answer",
                   "The one from more draws, and without knowing the counts the question cannot be answered",
                   "Their average, which halves the standard error",
                   "Neither: both are unbiased, so they are equally good estimates"],
             "c": 1,
             "why": "&ldquo;Closer to the truth&rdquo; is not available in a real "
                    "application, where the truth is what is being estimated. What is "
                    "available is the width, and the width comes from the count. Averaging "
                    "two runs of equal length divides the standard error by `√2`, not by "
                    "`2`; and unbiasedness is a statement about the expectation of the "
                    "estimator, not about the two numbers in hand."},
            {"q": "The panel's sample variance at `n = 400` reads `43031/39900` and is labelled &ldquo;exact, shown to 6 places&rdquo; when it is long. Why is the standard error labelled &ldquo;rounded&rdquo; instead?",
             "a": ["Because it is smaller, so the last digit matters more",
                   "Because `43031/39900` is a ratio of whole numbers and `√(43031/15960000)` is not",
                   "Because the sample variance is a population quantity and the standard error is a sample one",
                   "Because the standard error is divided by `n` and division introduces rounding"],
             "c": 1,
             "why": "A ratio of integers has a decimal expansion that can be cut short "
                    "without ceasing to be exact; an irrational number has no exact "
                    "decimal form at all. The two labels name genuinely different "
                    "situations, and using one word for both is what makes a reader stop "
                    "believing either."},
            {"q": "A running-mean trace has been flat for the last two thousand draws. What follows?",
             "a": ["The estimate has converged and further draws are wasted",
                   "Nothing: a flat trace is what a small sample of a slow process looks like, and the interval is the evidence",
                   "The variance is zero, so the standard error is zero",
                   "The generator's period has been exhausted"],
             "c": 1,
             "why": "A running mean over `n` draws moves by at most `(X − X̄)/n`, so it "
                    "goes flat whether or not the estimate is good &mdash; that is "
                    "arithmetic, not convergence. The standard error is computed from the "
                    "spread of the draws and is the only thing on the page entitled to "
                    "settle the question."},
        ],
        "mistakes": [
            ("Reporting the estimate without the width",
             "A simulated number with no standard error beside it makes no claim that can "
             "be checked or refused. This is the one habit the rest of the course depends "
             "on: every variance-reduction technique later on is a technique for making "
             "that width smaller, and a reader who does not print the width cannot tell "
             "whether any of them worked."),
            ("Quoting the spread of the data as the spread of the estimate",
             "`s` and `s/√n` differ by a factor of twenty at four hundred draws. The "
             "sample standard deviation describes a single draw; the standard error "
             "describes the average. Writing the first where the second belongs overstates "
             "the uncertainty enormously, and writing the second where the first belongs "
             "understates the variability of the thing being modelled."),
            ("Believing a run that has settled",
             "A trace that has stopped moving has demonstrated only that `1/n` is small. "
             "The queue lessons later on this course show a run sitting quietly at the "
             "wrong value for hundreds of slots because it started empty, with nothing in "
             "the picture to say so. The interval is the evidence and the picture is "
             "decoration."),
        ],
        "standard": ("Finish when an estimate without a width beside it reads as an unfinished result.",
                     "You should be able to compute a sample mean and a sample variance as "
                     "exact fractions, say why the denominator is `n − 1`, form the "
                     "standard error and print it in exact form with its rounding named, "
                     "convert a target width into a number of draws, and state in one "
                     "sentence what more draws do and do not promise."),
        "note": 'The standard error says how much the estimate moves. It does not by itself say how much of the time the truth is inside any particular band &mdash; that takes an inequality, and the only one this path can justify is Chebyshev&rsquo;s. &ldquo;How Sure? Chebyshev&rsquo;s Bound&rdquo; puts a guarantee on `±k SE` and then prints what the guarantee costs in width.',
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "how-sure-chebyshevs-bound",
        "title": "How Sure? Chebyshev's Bound",
        "module": "The estimate and its error bar",
        "one_line": "Put a guarantee on ±k standard errors that assumes nothing, and then read what the guarantee costs.",
        "summary": (
            "An interval is only worth what it guarantees. Chebyshev's inequality gives "
            "`±k` standard errors a coverage of at least `1 − 1/k²` for every distribution "
            "with a finite variance, with no shape assumed and nothing to be wrong about. "
            "At `k = 5` that is `24/25 = 96%`; the folklore `±2 SE` guarantees `3/4` and "
            "not the `95%` it is usually quoted with, because the `95%` comes from an "
            "approximation this path has not built."
        ),
        "key": [
            "P(|X̄ − μ| ≥ k·SE) ≤ 1/k²        Chebyshev, for every finite-variance law",
            "coverage ≥ 1 − 1/k²             k = 5 ⟹ 24/25 = 96%,  k = 2 ⟹ 3/4,  k = 1 ⟹ 0",
            "on this table σ² = 1 and n = 100, so SE = 1/10 exactly",
            "half-width at k = 5:  1/2        against the folklore ±2 SE:  1/5",
            "width ratio 5/2 = 2.5           and the folklore width is NOT five times narrower",
            "matching that width with runs instead costs (5/2)² = 25/4 = 6.25 times the draws",
        ],
        "key_label": "One inequality, one guarantee, and the price of the guarantee",
        "concepts_intro": (
            "Three ideas, and the first is a distinction that most reported intervals blur: "
            "what an interval guarantees is not what it usually achieves, and it is the "
            "guarantee that can be relied on."
        ),
        "concepts": [
            ("A bound is a worst case over all distributions, not a prediction",
             "Chebyshev says at most `1/k²` of the mass sits `k` standard deviations out, "
             "whatever the distribution is. Almost every distribution does far better than "
             "that, so the coverage you observe will usually beat the guarantee by a long "
             "way. Reading the bound as an estimate of the error is the standard mistake, "
             "and it runs in the safe direction exactly once: never."),
            ("The 95% attached to ±2 SE is an assumption, not a theorem",
             "It comes from the normal approximation, which this path has not built and "
             "does not assume. Under Chebyshev alone `k = 2` guarantees `1 − 1/4 = 3/4`. "
             "That is not a quibble about rigour: the approximation is a statement about "
             "sums of many comparable independent terms, and the estimators later on this "
             "course are sums of a few highly dependent ones."),
            ("Generality is bought with width, and the exchange rate is a square",
             "Five standard errors against two is a width ratio of exactly `5/2`, not of "
             "five. Buying that width back by running more instead &mdash; keeping `k = 5` "
             "and narrowing `SE` &mdash; costs `(5/2)² = 25/4` times the draws, because "
             "the width falls like `1/√n` and a ratio of widths therefore squares."),
        ],
        "read_title": "What an interval guarantees, and what it costs",
        "read_intro": "The one inequality this path can justify, the coverage it promises, and the two prices — in width and in runs — of promising it.",
        "body": [
            ("thm", ("Chebyshev's inequality, as Discrete Probability states it",
                     "For a random variable `X` with mean `μ` and finite standard "
                     "deviation `σ`, and any `k &gt; 0`, `P(|X − μ| ≥ kσ) ≤ 1/k²`. "
                     "Applied to the sample mean, whose standard deviation is the standard "
                     "error, this reads: the interval `X̄ ± k·SE` covers `μ` with "
                     "probability at least `1 − 1/k²`.")),
            ("p", "The statement is Discrete Probability's, in &ldquo;Variance and "
                  "Standard Deviation&rdquo;, which states it and stops. The two-line "
                  "derivation from Markov's inequality &mdash; apply Markov to "
                  "`(X − μ)²` &mdash; belongs to the Algorithms path, in "
                  "&ldquo;Randomised Algorithms&rdquo;, in the lesson that turns an "
                  "expectation into a probability. This page uses the statement and points "
                  "at the proof rather than repeating either."),
            ("p", "What it buys is unusual and worth naming. The inequality holds for every "
                  "distribution with a finite variance: skewed, bounded, discrete, "
                  "bimodal, anything. There is no assumption in it that can turn out to be "
                  "false about the model you actually simulated, which is precisely what "
                  "makes it the right tool for a simulation whose output distribution "
                  "nobody has written down."),
            ("h3", "The coverage counted, without taking a root"),
            ("p", "`|X̄ − μ| ≥ k·SE` is the same statement as `(X̄ − μ)² ≥ k²·σ²/n`, and "
                  "the second one has no root in it. So the panel counts coverage by "
                  "comparing two exact fractions, replication by replication, and the "
                  "count is a whole number over a whole number rather than a verdict about "
                  "two decimals."),
            ("example", ("Forty replications of a hundred draws",
                         "On the table `1, 4, 6, 4, 1` over `16`, whose variance is exactly "
                         "`1`, each replication of `100` draws has a mean with variance "
                         "`1/100`. At `k = 5` the guarantee is `1 − 1/25 = 24/25 = 96%`, "
                         "and the band actually covered `40` of `40` &mdash; `100%`. The "
                         "gap between `96%` and `100%` is not luck; it is the size of the "
                         "slack in a bound that had to hold for every distribution at "
                         "once.")),
            ("p", "Drag `k` down to `1` and the guarantee becomes `1 − 1/1 = 0`: "
                  "Chebyshev promises nothing whatever about `±1 SE`. The observed "
                  "coverage at that width on the same forty replications is `25` of `40`, "
                  "or `62.5%`. Both numbers are correct and they are answers to different "
                  "questions, and confusing them is the entire subject of this page."),
            ("h3", "The width, in the units the reader actually cares about"),
            ("math", ["  on this table σ² = 1, and with n = 100 per replication",
                      "",
                      "      SE = 1/10                        exactly — 100 is a square",
                      "",
                      "  k = 5    half-width  5 × 1/10 = 1/2      guarantee 24/25 = 96%",
                      "  k = 2    half-width  2 × 1/10 = 1/5      guarantee  3/4  = 75%",
                      "  k = 1    half-width  1 × 1/10 = 1/10     guarantee   0",
                      "",
                      "  width ratio      (1/2) / (1/5) = 5/2 = 2.5",
                      "  matching it with runs instead:  (5/2)² = 25/4 = 6.25 times the draws"]),
            ("p", "The phrase to avoid is &ldquo;five times wider&rdquo;. Five standard "
                  "errors against two is a ratio of `5/2`, and the number `5` in `k = 5` "
                  "is not a width ratio at all. The two-and-a-half is the honest price of "
                  "the guarantee, and it is small enough that a reader who wanted `96%` "
                  "rather than an assumption of `95%` might well pay it."),
            ("p", "The other way to pay is with runs. Keep `k = 5` and narrow the standard "
                  "error until the band is as tight as `±2 SE` was: since the width falls "
                  "like `1/√n`, that takes `(5/2)² = 25/4` times the draws. Six and a "
                  "quarter times the compute for the same width, with a guarantee instead "
                  "of an assumption, is a trade a reader can actually evaluate &mdash; "
                  "which is more than can be said for an unlabelled `95%`."),
            ("h3", "Where the arithmetic stops being exact, and where it does not"),
            ("p", "On this table the half-width comes out at `1/2` and the folklore "
                  "half-width at `1/5`: both rational, because `σ² = 1` and `100` is a "
                  "square. Switch the panel to the skewed table, whose variance is "
                  "`367/256`, and the half-width becomes `(1/32)√367 ≈ 0.59866`, printed "
                  "as a surd and then as a rounded decimal. The guarantee `24/25`, the "
                  "width ratio `5/2` and the run cost `25/4` do not move, because none of "
                  "them contains a root."),
            ("p", "That is the shape of every honest report on this course: the quantities "
                  "that carry the argument stay rational, and the one quantity that has to "
                  "be a root is printed in exact form with its rounding named. A coverage "
                  "count of `40` out of `40` is a count; `96%` is `24/25`; and `0.59866` "
                  "is `(1/32)√367` shown to five places and no more."),
        ],
        "lab": ("simulate", {
            "mode": "bound",
            "preset": "binomial16",
            "panel_title": "Drag k, and watch the guarantee and the coverage move apart",
            "panel_intro": "Forty replications of a hundred draws each, every one with its "
                           "own mean, against a band of `k` standard errors around the "
                           "exact mean of the table. The guarantee `1 − 1/k²` and the "
                           "coverage actually counted are printed side by side, and so are "
                           "the two prices of the guarantee: the width ratio `k/2` against "
                           "the folklore band, and the `(k/2)²` times the draws it would "
                           "take to buy that width back. Drag `k` to `1` and read a "
                           "guarantee of zero.",
        }),
        "steps_title": "Putting a defensible interval on a simulated number",
        "steps_intro": "Five steps, and the fourth is the one that keeps the report honest.",
        "steps": [
            ("Decide the coverage you need before looking at the data",
             "`1 − 1/k²` inverts to `k = 1/√(1 − coverage)`. Ninety-six per cent needs "
             "`k = 5`; ninety per cent needs about `3.163`; seventy-five per cent needs "
             "`k = 2`. Choosing `k` after seeing where the replications fell is choosing "
             "the interval that flatters the run."),
            ("Compute the standard error, and keep the root exact",
             "`SE = √(s²/n)`, carried as a surd. The half-width is `k·SE`, which is a "
             "second quantity with the same root in it; both are printed in exact form "
             "with the decimal labelled."),
            ("State the guarantee as a fraction, not as a percentage alone",
             "`24/25` and `96%` are the same number, and the fraction is the one that "
             "shows where it came from. A reader who sees `1 − 1/5²` can check it; a "
             "reader who sees `96%` has to trust it."),
            ("Say which inequality you used, and what it did not assume",
             "&ldquo;Chebyshev, so this holds for any finite-variance distribution&rdquo; "
             "is a claim a reader can evaluate. &ldquo;A 95% confidence interval&rdquo; on "
             "a simulation whose output law nobody has characterised is a claim about a "
             "normal approximation that has not been justified."),
            ("Report the coverage you observed as well, and keep them apart",
             "The observed coverage is a measurement of this run; the guarantee is a "
             "property of the method. Printing both, labelled, is what stops the first "
             "from being quietly promoted into the second."),
        ],
        "worked": {
            "title": "k = 5 on forty replications, and what k = 2 would have promised",
            "intro": [
                "Forty replications of a hundred draws each, from the table with `μ = 2` "
                "and `σ² = 1`. The variance of a replication mean is therefore exactly "
                "`1/100`, and the whole comparison below is in fractions.",
            ],
            "lines": [
                "table 1, 4, 6, 4, 1 over 16      μ = 2     σ² = 1",
                "40 replications of n = 100       Var(mean) = σ²/n = 1/100",
                "",
                "coverage is counted by comparing squares, so no root is taken",
                "    outside  ⟺  (mean − μ)²  ≥  k² · 1/100",
                "",
                "k = 5     threshold 25/100 = 1/4      half-width 1/2",
                "          guarantee 1 − 1/25 = 24/25 = 96%",
                "          observed  40 of 40         = 100.0%",
                "",
                "k = 2     threshold  4/100 = 1/25     half-width 1/5",
                "          guarantee 1 − 1/4  = 3/4   = 75%     ← not 95%",
                "          observed  40 of 40         = 100.0%",
                "",
                "k = 1     guarantee 1 − 1/1  = 0     = 0%",
                "          observed  25 of 40         = 62.5%",
                "",
                "the two prices of k = 5 over k = 2",
                "    width      (1/2)/(1/5)  = 5/2  = 2.5 times as wide",
                "    runs       (5/2)²       = 25/4 = 6.25 times the draws",
            ],
            "after": [
                "The `k = 1` row is the one to sit with. The guarantee is exactly zero "
                "&mdash; Chebyshev promises nothing at one standard error &mdash; and the "
                "band still covered sixty-two and a half per cent of the replications. "
                "Both numbers are right. One is a property of the inequality and one is a "
                "fact about forty runs of one table, and an interval reported without "
                "saying which is which is an interval that cannot be checked.",
                "The `k = 2` row is the one that gets misreported in practice. Its "
                "guarantee is `3/4`. The `95%` usually attached to `±2 SE` is a normal-"
                "approximation figure, and on a simulation output it is an assumption "
                "about a distribution nobody has examined. Where the approximation is "
                "justified it is a good deal; the error is not using it, it is using it "
                "silently.",
                "For a faded rehearsal, drag the draws per replication from `100` to `225` "
                "with `k` at `5`. The supplied first move is that the standard error "
                "becomes `1/15` &mdash; `225` is a square, so no root appears &mdash; and "
                "the half-width becomes `1/3`. Say what happens to the guarantee, what "
                "happens to the observed coverage, and which of the two you could have "
                "predicted before pressing anything.",
            ],
        },
        "quiz_title": "Guarantees, widths and what k means",
        "quiz": [
            {"q": "Under Chebyshev alone, what coverage does the interval `X̄ ± 2 SE` guarantee?",
             "a": ["`95%`", "`3/4`", "`24/25`", "`1 − 2/e²`"],
             "c": 1,
             "why": "`1 − 1/k²` at `k = 2` is `3/4`. The `95%` is the normal-approximation "
                    "figure and it is an assumption about the shape of the distribution, "
                    "not a consequence of the variance; `24/25` is the guarantee at "
                    "`k = 5`."},
            {"q": "A band at `k = 5` is how much wider than the folklore band at `k = 2`?",
             "a": ["Five times", "Two and a half times", "Six and a quarter times", "Twenty-five times"],
             "c": 1,
             "why": "The half-width is `k·SE`, so the ratio is `5/2 = 2.5`. &ldquo;Five "
                    "times&rdquo; mistakes `k` for the ratio; `6.25` is `(5/2)²`, which is "
                    "the factor on the number of <em>runs</em> needed to buy the width "
                    "back, not on the width itself."},
            {"q": "Over forty replications the guarantee is `96%` and the observed coverage is `100%`. What does that gap show?",
             "a": ["That the replications are not independent",
                   "That the bound is loose, as a worst case over all distributions must be",
                   "That `k` was chosen too large and should be reduced",
                   "That the sample size per replication was too small for the bound to apply"],
             "c": 1,
             "why": "Chebyshev has to hold for every finite-variance distribution at once, "
                    "including the worst of them, so on any particular one it will "
                    "normally be slack. The bound applies at every sample size &mdash; it "
                    "assumes nothing about `n` &mdash; and a large gap is the expected "
                    "behaviour rather than a symptom."},
            {"q": "You need coverage of at least `90%` from a Chebyshev interval. What `k` does that take?",
             "a": ["`k = 2`, since `2 SE` is the usual `95%` band",
                   "`k = 10`, since `1/10` is `10%`",
                   "About `k = 3.163`, since `1 − 1/k² ≥ 0.9` needs `k ≥ √10`",
                   "No finite `k`, since Chebyshev cannot reach `90%`"],
             "c": 2,
             "why": "`1 − 1/k² ≥ 9/10` rearranges to `k² ≥ 10`. The first choice is the "
                    "normal approximation again; the second confuses `1/k` with `1/k²`; "
                    "and Chebyshev reaches any coverage below `1` at a finite `k`, which "
                    "is why the interesting question is what the width costs."},
        ],
        "mistakes": [
            ("Calling ±2 SE a 95% interval on a simulation output",
             "The `95%` is a normal-approximation figure. What `±2 SE` guarantees with no "
             "assumption is `3/4`, and the difference is not academic: the estimators in "
             "the second half of this course are averages of a few strongly dependent "
             "replications, which is exactly the setting where the approximation is least "
             "justified and most convenient."),
            ("Reading the bound as an estimate of the error",
             "`96%` coverage at `k = 5` says that the truth is inside the band at least "
             "ninety-six times in a hundred. It does not say the error is about half the "
             "band, and it does not say anything at all about where inside the band the "
             "truth sits. On the panel's opening run the observed coverage is `100%`, "
             "which is what a worst-case bound normally looks like from the inside."),
            ("Choosing k after looking at where the replications fell",
             "The inequality is a statement about the procedure, and the procedure "
             "includes choosing `k`. Picking the smallest `k` that happens to cover "
             "everything on this run turns a guarantee into a description, and the "
             "description will not survive the next seed."),
        ],
        "standard": ("Finish when an interval with no named inequality behind it reads as a decoration.",
                     "You should be able to state Chebyshev's inequality and say where its "
                     "statement and its proof live, convert a required coverage into a `k` "
                     "and a `k` into a coverage, compute a half-width in exact form with "
                     "its rounding named, give both prices of a wider guarantee &mdash; "
                     "the `k/2` in width and the `(k/2)²` in runs &mdash; and keep an "
                     "observed coverage and a guaranteed one apart in the same sentence."),
        "note": 'Everything so far has sampled a table. A simulation earns its keep on systems no table describes, where the quantity of interest is an average over time rather than over draws &mdash; and there the estimate is still an estimate, with everything on these two pages still attached to it. &ldquo;Discrete-Event Simulation of a Queue&rdquo; runs one, by moving the clock to the next event rather than through the empty slots between them.',
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "discrete-event-simulation-of-a-queue",
        "title": "Discrete-Event Simulation of a Queue",
        "module": "Running a system",
        "one_line": "Keep a calendar of scheduled events, jump the clock to the earliest, change the state, and schedule what follows.",
        "summary": (
            "A discrete-event simulation holds a calendar of scheduled events and advances "
            "the clock to the earliest of them, skipping every instant at which nothing "
            "happens. The state changes, new events are scheduled from the new state, and "
            "the calendar is the model. The output is a time average, and it is an "
            "estimate of the steady-state value with everything the previous two pages "
            "attached to it."
        ),
        "key": [
            "state + calendar + clock      the whole of a discrete-event simulation",
            "next event = the earliest scheduled;  the clock JUMPS there",
            "arrivals p = 2/5 a slot, service completes with probability q = 1/2",
            "exact long-run mean in system  L = 12/5     server busy fraction ρ = p/q = 4/5",
            "one run of 2000 slots:  776 customers, area 4733, time average 4733/2000",
            "L = λW is an identity about one run's own averages, not a model of anything",
        ],
        "key_label": "The three objects, the model, and one run of it",
        "concepts_intro": (
            "Three ideas. The first is the mechanism, the second is what the mechanism "
            "produces, and the third is the one that keeps this course honest about it."
        ),
        "concepts": [
            ("The calendar is the simulation",
             "A discrete-event simulation is three things: a state, a list of scheduled "
             "future events, and a clock. The loop is: take the earliest event, move the "
             "clock to it, apply its effect to the state, schedule whatever that state "
             "now implies. There is no time step, and the instants between events are "
             "never visited because nothing happens at them."),
            ("A time average is an area divided by a length",
             "The number in system is a step function of the clock. Its time average over "
             "a window is the area under it divided by the window's length &mdash; and "
             "that area is also the sum of the customers' times in the system, one "
             "rectangle per customer. The two readings of the same area are Little's Law, "
             "and as a statement about one run's own averages it is an identity rather "
             "than a model."),
            ("A run is one observation of a random quantity",
             "The number this page produces is not the long-run mean; it is an estimate of "
             "it. Reseed and it lands somewhere else, and the spread of where it lands is "
             "what the standard error measures. The exact value is available here only "
             "because this particular queue was solved exactly in &ldquo;Markov Chains, "
             "Decisions and Queues&rdquo;, which is what makes this page a measurement "
             "rather than an assertion."),
        ],
        "read_title": "A clock that jumps, and the average it leaves behind",
        "read_intro": "How the event loop works, what it produces, and how far one run of it is from the answer.",
        "body": [
            ("def", ("Discrete-event simulation",
                     "A simulation in which the state changes only at a countable set of "
                     "<strong>event times</strong>. The simulator holds the current state, "
                     "a <strong>calendar</strong> of events scheduled for future times, "
                     "and a clock. Each step removes the earliest calendar entry, advances "
                     "the clock to its time, applies its effect, and schedules any events "
                     "the new state implies.")),
            ("p", "The model on this page is the single-server queue the earlier course "
                  "solved exactly: in each slot an arrival occurs with probability `p`, "
                  "and a customer in service completes with probability `q`, so a service "
                  "duration is a geometric variate on `{1, 2, 3, …}`. Both are sampled by "
                  "inverse transform from the seeded stream, so the run is reproducible "
                  "and every figure it produces is a fraction."),
            ("def", ("Time average",
                     "For a quantity `N(t)` that is constant between events, the "
                     "<strong>time average</strong> over `[0, T)` is `(1/T)∫N(t) dt`, "
                     "which for a step function is the sum of `N` times the length of each "
                     "interval, divided by `T`. It is not the average of the values `N` "
                     "took; it is the average weighted by how long it took them.")),
            ("p", "That distinction costs people real errors. A queue that holds one "
                  "customer for nine hundred slots and nine customers for one hundred has "
                  "a time average of `1.8` and an unweighted average over its two distinct "
                  "states of `5`. Only the first is the number anyone wants, and only the "
                  "first is what the area under the curve gives you."),
            ("h3", "One run, event by event"),
            ("example", ("The first ten events at p = 2/5, q = 1/2, seed 1",
                         "Customer 1 arrives at slot `3` and leaves at `4`. Customer 2 "
                         "arrives at `5` with a service of three slots; customers 3 and 4 "
                         "arrive at `6` and `7` and queue behind it. At clock `8` two "
                         "events share the instant: customer 2 departs and customer 5 "
                         "arrives. The departure is taken first, so immediately after it "
                         "the system holds two, and the arrival then takes it to three. "
                         "Nothing whatever happens at slots `0`, `1`, `2`, and the clock "
                         "never visits them.")),
            ("p", "The tie at clock `8` is not a detail. A simulator that answered "
                  "&ldquo;who is in the system at time `t`?&rdquo; by testing "
                  "`arrival ≤ t &lt; departure` would count the arriving customer as "
                  "present at the instant the departure is being processed, and its "
                  "headcount would disagree with its own list of names. The rule &mdash; "
                  "departures before arrivals at the same instant &mdash; has to be stated "
                  "once and then obeyed by every part of the program that asks the "
                  "question."),
            ("h3", "The long run, and the exact value it is aiming at"),
            ("math", ["  p = 2/5,  q = 1/2,  single server, first in first out",
                      "",
                      "  exact, from the chain:   L = 12/5 = 2.4       ρ = p/q = 4/5",
                      "",
                      "  one run of 2000 slots, seed 1",
                      "     customers            776",
                      "     area under N(t)      4733 slot-customers",
                      "     time average         4733/2000 = 2.3665",
                      "     server busy          1593 of 2000 slots = 79.7%",
                      "",
                      "  gap to the exact value:  0.0335 below"]),
            ("p", "The gap of `0.0335` is not a defect of the simulation and not a rounding "
                  "error; there is no rounding anywhere in it. It is one draw of a random "
                  "quantity whose expectation is near `12/5`, and reseeding moves it: the "
                  "same model at seed `0` gives `1.9660`, at seed `2` gives `2.7300`, at "
                  "seed `3` gives `2.5300`. A page that printed only the first of those "
                  "would be reporting a coincidence."),
            ("h3", "Little's Law, and which horizon you divide by"),
            ("p", "The area under the occupancy curve is both the integral of the number in "
                  "system and the sum of the customers' times in it. Divide it by the "
                  "horizon and you get the time average; divide the sum of times by the "
                  "number of customers and you get the mean time in system; divide the "
                  "number of customers by the horizon and you get the arrival rate. The "
                  "three are then related by `L = λW` as a matter of arithmetic, with no "
                  "assumption about the model at all."),
            ("p", "It is worth being precise about the horizon, because the panel uses two "
                  "of them and they differ. Over the trace's own horizon &mdash; from slot "
                  "`0` to the last departure, at slot `2005` &mdash; the arrival rate is "
                  "`776/2005` and the mean time in system is `4733/776`, and their product "
                  "is `4733/2005 ≈ 2.3606`. The panel's time average divides the same area "
                  "by the `2000` slots the run was asked for, giving `4733/2000 ≈ 2.3665`. "
                  "Same area, two denominators, and the identity holds for whichever one "
                  "you choose consistently."),
            ("p", "One thing that is often called a mistake here and is not: this is a "
                  "slotted model, so stepping one slot at a time <em>is</em> the model, "
                  "and next-event simulation is the efficient form of the same "
                  "computation. The two agree slot for slot and differ only in how much "
                  "work they do. They part company for systems in continuous time, which "
                  "this path does not sample."),
        ],
        "lab": ("simulate", {
            "mode": "des",
            "preset": "base",
            "panel_title": "Step the calendar by hand, then run long and check the average",
            "panel_intro": "The event slider walks the calendar one event at a time: the "
                           "clock, what happened, how many are in the system after it, who "
                           "holds the server and who is queued. Stop at event `6` and read "
                           "the pending list &mdash; there is an arrival scheduled for the "
                           "same instant, and departures are taken first. Then read the "
                           "long run's time average against the exact `12/5` beside it, "
                           "and reseed three times before believing either.",
        }),
        "steps_title": "Running an event calendar by hand",
        "steps_intro": "Five steps, and the third is the one that is skipped in every implementation that later disagrees with itself.",
        "steps": [
            ("Write down the state, and nothing else in it",
             "For this queue: how many are in the system, and who. Anything derivable "
             "&mdash; the queue length, whether the server is busy &mdash; is derived, not "
             "stored, because two copies of one fact are two copies that can disagree."),
            ("Seed the calendar with the events the initial state implies",
             "The first arrival, and nothing more. A calendar that starts with a hundred "
             "pre-generated arrivals is a different program: it cannot let the state "
             "decide what happens next, which is the one thing the method is for."),
            ("Fix the tie-breaking rule once, in writing",
             "Two events can share an instant. Departures before arrivals is the "
             "convention here; the opposite convention is equally defensible and gives "
             "different numbers. What is not defensible is one rule in the event loop and "
             "another in the code that reports the state."),
            ("Advance the clock to the earliest event and apply it",
             "Not to the next tick. The instants in between are not simulated at all, and "
             "the whole economy of the method is that a thousand empty slots cost nothing."),
            ("Accumulate the area as you go, and divide at the end",
             "Add `N × (new clock − old clock)` at every event. That running total is the "
             "integral of the occupancy, it is the sum of the customers' times, and it is "
             "the numerator of every average the run will report."),
        ],
        "worked": {
            "title": "Twelve customers, twenty-four events, and one tie",
            "intro": [
                "The panel's opening run, at `p = 2/5`, `q = 1/2`, seed 1. Twelve "
                "customers make twenty-four events, which is a calendar that fits on a "
                "screen and is twice as long as anyone wants to keep by hand.",
            ],
            "lines": [
                "arrivals    3, 5, 6, 7, 8, 11, 13, 16, 26, 31, 32, 33",
                "services    1, 3, 1, 2, 1,  2,  1,  1,  2,  2,  2,  1",
                "departures  4, 8, 9, 11, 12, 14, 15, 17, 28, 33, 35, 36",
                "",
                "ev  clock  what           in system  in service  waiting",
                " 1    3    arrival  c1        1          c1        —",
                " 2    4    departure c1       0        idle        —",
                " 3    5    arrival  c2        1          c2        —",
                " 4    6    arrival  c3        2          c2        c3",
                " 5    7    arrival  c4        3          c2        c3, c4",
                " 6    8    departure c2       2          c3        c4",
                " 7    8    arrival  c5        3          c3        c4, c5",
                " 8    9    departure c3       2          c4        c5",
                " 9   11    departure c4       1          c5        —",
                "10   11    arrival  c6        2          c5        c6",
                "",
                "events 6 and 7 share clock 8; the departure is taken first,",
                "and events 9 and 10 share clock 11 for the same reason.",
                "",
                "slots 0, 1 and 2 are never visited: nothing is scheduled there.",
            ],
            "after": [
                "Read the pair at clock `8` twice. After event 6 the system holds two "
                "customers and the waiting list holds one name; after event 7 it holds "
                "three and the list holds two. A headcount recomputed from the clock alone "
                "would report three at both instants, and the list of names would report "
                "two at the first &mdash; a program that disagrees with itself about a "
                "number it prints in two places.",
                "The gaps are where the method earns its keep. Between the departure at "
                "slot `17` and the arrival at slot `26` nothing whatever happens, and a "
                "next-event simulator does no work at all for those nine slots. Over two "
                "thousand slots this run has fifteen hundred and fifty-two events, and a "
                "fixed-tick loop would take two thousand steps to reach the same numbers.",
                "For a faded rehearsal, switch the panel to the faster server, `q = 3/5`, "
                "and predict the two headline figures before reading them. The supplied "
                "first move is that the exact long-run mean drops from `12/5` to `6/5` and "
                "the busy fraction from `4/5` to `2/3`. Say whether the arrival times "
                "change, and why, and then check the first four rows of the log against "
                "your answer.",
            ],
        },
        "quiz_title": "Calendars, clocks and time averages",
        "quiz": [
            {"q": "In a next-event simulation, what decides the next value of the clock?",
             "a": ["The clock advances by one time unit each step",
                   "The earliest time on the calendar of scheduled events",
                   "The arrival process, since arrivals are what drive the system",
                   "The shortest remaining service time among customers present"],
             "c": 1,
             "why": "The clock jumps to the earliest scheduled event, whatever kind it is. "
                    "A fixed increment is a different method; and privileging arrivals or "
                    "services would make the simulator wrong whenever the other kind came "
                    "first."},
            {"q": "A queue holds one customer for nine hundred slots and nine customers for one hundred slots. What is the time-average number in system?",
             "a": ["`5`, the average of the two values it took",
                   "`1.8`, the area divided by the length of the window",
                   "`10`, the largest number it reached",
                   "`4.5`, half the maximum"],
             "c": 1,
             "why": "`(1·900 + 9·100)/1000 = 1800/1000 = 1.8`. Averaging the two distinct "
                    "values gives `5` and ignores that one of them lasted nine times as "
                    "long, which is exactly the error the phrase <em>time average</em> "
                    "exists to prevent."},
            {"q": "One run of 2000 slots gives a time average of `4733/2000 ≈ 2.3665` against an exact long-run mean of `12/5`. What is the right reading?",
             "a": ["The simulation has a bug, since an exact computation is available",
                   "The run is an unbiased-in-the-limit estimate with sampling error, and reseeding will move it",
                   "The gap of `0.0335` is the rounding error of the arithmetic",
                   "The run has not converged, and running it four times as long will make the gap four times smaller"],
             "c": 1,
             "why": "There is no rounding anywhere in the run; every figure is a fraction. "
                    "Reseeding gives `1.9660`, `2.7300` and `2.5300` at seeds `0`, `2` and "
                    "`3`, which is what sampling error looks like. Four times the run "
                    "length divides the standard error by two, not the gap by four, and it "
                    "does nothing at all about the separate bias the next page is about."},
            {"q": "Why is `L = λW` described here as an identity rather than as a model?",
             "a": ["Because it has been proved for this particular queue",
                   "Because the same area is being read two ways, so it holds for any run of anything",
                   "Because it only holds in the long run",
                   "Because `λ` and `W` are estimated from the same data"],
             "c": 1,
             "why": "The area under the occupancy curve is the sum of the customers' times "
                    "in the system, so dividing it by the horizon in one order or the "
                    "other gives the two sides. Nothing about arrivals, service or "
                    "independence is used, which is why it holds for one finite run of any "
                    "system whose customers arrive and leave."},
        ],
        "mistakes": [
            ("Recomputing the state from the clock instead of walking the events",
             "Asking &ldquo;who satisfies `arrival ≤ t &lt; departure`?&rdquo; gives a "
             "different answer from the event loop at every instant that carries two "
             "events. On this run, clock `8` carries a departure and an arrival, and the "
             "two methods disagree about whether the system holds two or three. Walking "
             "the one event list makes the count and the contents the same object by "
             "construction."),
            ("Reporting a single run as the answer",
             "One run of two thousand slots gave `2.3665`; three other seeds gave "
             "`1.9660`, `2.7300` and `2.5300`. Any of the four could have been the one "
             "that reached a report. The estimate is the average over replications with a "
             "standard error attached, and a single run is one observation of it."),
            ("Confusing the time average with the average over customers",
             "The time average of the number in system and the average time in system per "
             "customer are different quantities with different units, and Little's Law is "
             "the statement that relates them. Quoting one where the other belongs is a "
             "factor of the arrival rate out, which on this run is about two and a half."),
        ],
        "standard": ("Finish when a single run's average reads as one observation rather than as the answer.",
                     "You should be able to run an event calendar by hand for ten events, "
                     "state and obey a tie-breaking rule for simultaneous events, "
                     "accumulate the area under the occupancy curve and turn it into a "
                     "time average, read the same area as `λ` times `W`, and say what "
                     "reseeding does to every figure the run produced."),
        "note": 'This run started with nothing in the system, which is a choice and not a neutral one: it means the early slots are sampling a system that has not yet reached the behaviour the average is supposed to describe. &ldquo;Warm-Up and the Initial Transient&rdquo; computes exactly how much that costs, as theory rather than as a story about noise, and shows what removing it does and does not fix.',
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "warm-up-and-the-initial-transient",
        "title": "Warm-Up and the Initial Transient",
        "module": "Running a system",
        "one_line": "Average from an empty start and the answer is biased; compute the bias exactly, then throw the beginning away.",
        "summary": (
            "A run that begins with an empty system spends its first slots somewhere the "
            "steady state is not, and every average taken from slot zero carries that as a "
            "<strong>bias</strong> &mdash; a wrongness in the expectation, which no number "
            "of replications removes. Carrying the whole distribution forward one slot at "
            "a time makes the bias exact rather than anecdotal, and a longer run only "
            "dilutes it while discarding a warm-up removes it."
        ),
        "key": [
            "E[N₀], E[N₁], …  =  0,  2/5,  3/5,  37/50,  17/20, …    climbing toward 12/5",
            "expected average over slots 0 to 399      2.2443   (exact, to 4 places)",
            "expected average over slots 100 to 399    2.3717   (exact, to 4 places)",
            "stationary mean                           12/5 = 2.4",
            "bias is in the EXPECTATION: replications shrink the variance and not this",
            "a longer run dilutes the transient;  discarding it deletes the transient",
        ],
        "key_label": "The transient as theory, and the two averages it separates",
        "concepts_intro": (
            "Three ideas. The first is the distinction the whole page turns on, the second "
            "makes it computable, and the third is the fix that is usually reached for and "
            "is the wrong one."
        ),
        "concepts": [
            ("Bias and variance are different problems with different cures",
             "Variance is how much the estimate moves when you reseed, and replications "
             "shrink it. Bias is where the estimate is aimed, and replications do nothing "
             "to it whatever: a thousand runs all started empty give a thousand estimates "
             "of the same wrong number, with a beautifully small standard error around it."),
            ("The transient is computable, not just visible",
             "Starting from an empty system, the distribution of the number in system at "
             "slot `t` can be carried forward exactly, one slot at a time. For this queue "
             "the expected occupancy runs `0`, `2/5`, `3/5`, `37/50`, `17/20`, … toward "
             "the stationary `12/5`, and those are fractions rather than measurements. The "
             "bias is then a statement about numbers you can print."),
            ("Diluting a fixed error is much slower than deleting it",
             "The transient is a fixed quantity of wrongness at the front of the run, so "
             "its share of the average falls like `1/T`. Quadrupling the run length from "
             "`100` slots to `400` divides the remaining bias by about `3.5`; throwing "
             "away the first quarter of the four-hundred-slot run divides it by about "
             "`5.5`. Deleting wins, and it wins on a quarter of the compute."),
        ],
        "read_title": "Where a run starts, and what that costs its average",
        "read_intro": "Why the beginning of a run is not a sample of the thing being estimated, how much that is worth in numbers, and what actually removes it.",
        "body": [
            ("def", ("Initial transient",
                     "The <strong>initial transient</strong> is the part of a run during "
                     "which the state distribution is still visibly moving away from the "
                     "initial condition and toward the steady-state distribution. It is "
                     "not a period of &ldquo;noise&rdquo;: the process is behaving "
                     "correctly throughout, and it is simply not yet behaving like the "
                     "system the long-run average describes.")),
            ("def", ("Bias of an estimator",
                     "An estimator `T` of a quantity `θ` has <strong>bias</strong> "
                     "`E[T] − θ`. Bias is a property of the estimator, not of a run: it "
                     "does not shrink with replications, it does not show up in a standard "
                     "error, and an interval built on that standard error is centred in "
                     "the wrong place.")),
            ("p", "That is the whole reason this page exists. Every technique after it "
                  "attacks variance, and all of them are worthless on an estimator aimed "
                  "at the wrong number. A narrow interval around a biased estimate is "
                  "worse than a wide one, because it is more convincing."),
            ("h3", "The transient, as arithmetic"),
            ("p", "The number in system at the end of a slot is a Markov chain: from state "
                  "`n` a departure happens first with probability `q`, then an arrival "
                  "with probability `p`, so the chain steps to `n − 1`, `n` or `n + 1`, "
                  "and from `0` only to `0` or `1`. Starting from the point mass at zero "
                  "and pushing the whole distribution forward one slot at a time gives "
                  "`E[Nₜ]` exactly, for every `t`."),
            ("math", ["  p = 2/5,  q = 1/2,  started empty",
                      "",
                      "  E[N₀] = 0",
                      "  E[N₁] = 2/5",
                      "  E[N₂] = 3/5",
                      "  E[N₃] = 37/50",
                      "  E[N₄] = 17/20",
                      "     …",
                      "  E[N₅₀]  ≈ 2.0332        E[N₁₀₀] ≈ 2.2633",
                      "  E[N₃₉₉] ≈ 2.3982        stationary  12/5 = 2.4",
                      "",
                      "  expected time average over slots   0 to 399:   2.2443",
                      "  expected time average over slots 100 to 399:   2.3717"]),
            ("p", "Both of those averages are exact fractions shown to four places, not "
                  "rounded numbers &mdash; they are averages of finitely many rationals. "
                  "The bias of the naive estimator is `2.2443 − 2.4`, about `−0.1557`; the "
                  "bias after discarding a hundred slots is about `−0.0283`. The discard "
                  "removes roughly four fifths of what was there, and it does so in "
                  "theory, before any run has been made."),
            ("thm", ("A longer run dilutes; a discard deletes",
                     "Let `B` be the total excess or shortfall contributed by the "
                     "transient. Averaging over `T` slots contributes `B/T` to the "
                     "estimate, which falls like `1/T`. Averaging over slots `w` to `T` "
                     "instead removes the part of `B` that lay before `w` outright. "
                     "Lengthening the run is therefore a `1/T` effect and discarding is "
                     "not.")),
            ("p", "The numbers say the same thing. At `100` slots the expected average is "
                  "`1.8624`, a shortfall of `0.5376`; at `400` slots it is `2.2443`, a "
                  "shortfall of `0.1557`. Four times the run divided the remaining bias by "
                  "about `3.5`. Discarding the first hundred of those four hundred slots "
                  "takes the shortfall to `0.0283` &mdash; a further factor of about "
                  "`5.5`, bought with a quarter of the data rather than with four times "
                  "the compute."),
            ("h3", "One run, and what it actually did"),
            ("example", ("Four hundred slots at seed 0",
                         "The average over every slot is `169/80 = 2.1125`; the average "
                         "over the three hundred slots after a warm-up of one hundred is "
                         "`361/150 ≈ 2.4067`. The discard moved the estimate up by about "
                         "`0.2942`, which is the direction the theory says and rather more "
                         "than the theory's `0.1274` &mdash; because one run is an "
                         "observation of the expectation and not the expectation.")),
            ("p", "Reseed and the sign can change. The same settings at seed 1 give "
                  "`1.3075` from slot zero and `1.2367` after the discard: the discard "
                  "moved the estimate <em>down</em>, on a run that spent its whole length "
                  "below the steady state. That is not a counterexample to the bias; it is "
                  "what a single observation of a quantity with a standard error looks "
                  "like, and it is exactly why the exact transient is printed beside the "
                  "run rather than the run being left to make the argument."),
            ("h3", "Batch means: replications out of one run"),
            ("def", ("Batch means",
                     "Discard the warm-up, split what remains into `b` equal "
                     "<strong>batches</strong>, and take the mean of each. A batch mean is "
                     "far closer to independent of its neighbour than one slot is of the "
                     "next, so the `b` batch means can be treated as replications: their "
                     "average is the estimate and their sample variance is what an "
                     "interval is built from.")),
            ("p", "On the run at seed 0 the four batches of seventy-five slots give means "
                  "`34/25`, `116/75`, `19/25` and `149/25` &mdash; that is `1.36`, `1.55`, "
                  "`0.76` and `5.96`. Their average is `361/150`, within `0.007` of the "
                  "exact `12/5`, and their sample variance is `10733/1875 ≈ 5.72`. The "
                  "point estimate could hardly be better and the four numbers behind it "
                  "say the run has established almost nothing. Printing the second fact "
                  "beside the first is the whole job."),
            ("p", "That spread is also a warning about the batches themselves. A batch mean "
                  "is only nearly independent of its neighbour if the batch is long "
                  "compared with how fast the system forgets its state, and seventy-five "
                  "slots of a queue running at `4/5` utilisation is not obviously long "
                  "enough. The remedy is fewer, longer batches, and the diagnostic is to "
                  "watch the batch variance as the batch count falls."),
        ],
        "lab": ("simulate", {
            "mode": "warmup",
            "preset": "base",
            "panel_title": "Drag the warm-up, and watch the bias leave the average",
            "panel_intro": "The green curve is not a fit to the trace: it is the exact "
                           "expected occupancy at each slot, carried forward from an empty "
                           "system one slot at a time. Two averages are printed &mdash; "
                           "over every slot, and over the slots after the discard &mdash; "
                           "and beside each of them the exact expected value it is an "
                           "estimate of, so the bias is visible as theory rather than as a "
                           "story about noise. Reseed and watch the run's two numbers "
                           "swap order while the two exact ones do not move.",
        }),
        "steps_title": "Getting the beginning out of the answer",
        "steps_intro": "Five steps, and the fourth one is the check that most warm-up procedures skip.",
        "steps": [
            ("Decide what the initial condition is, and admit that it is one",
             "An empty system is a choice, not a neutral default, and it is the choice "
             "that biases a queueing average downward. Starting in a typical state, if you "
             "have one, is a legitimate alternative and it moves the bias rather than "
             "removing it."),
            ("Plot the quantity against time and look for the shape",
             "Not for the noise &mdash; for the drift. A trace that climbs for two hundred "
             "slots and then wanders is showing you a transient and then a steady state, "
             "and the elbow is roughly where the warm-up should end."),
            ("Discard, and say how much you discarded",
             "&ldquo;The first hundred of four hundred slots&rdquo; is a reportable "
             "procedure. A discard chosen after seeing which choice gave the nicest answer "
             "is a procedure that will not survive a second seed, and it is not honest to "
             "report only its output."),
            ("Check that the estimate has stopped moving as the warm-up grows",
             "Increase the discard and watch the kept average. If it is still drifting, "
             "the warm-up is too short. If it has settled but the variance is climbing, "
             "you are throwing away data you needed, and the fix is a longer run rather "
             "than a longer discard."),
            ("Build the interval from batch means, not from slots",
             "Consecutive slots of a queue are strongly dependent, so the sample variance "
             "over slots understates the spread badly. Batch means are the standard repair "
             "and they come with their own condition: the batches must be long enough for "
             "their means to be nearly independent."),
        ],
        "worked": {
            "title": "Four hundred slots, a hundred discarded, four batches",
            "intro": [
                "The panel's opening state: `p = 2/5`, `q = 1/2`, four hundred slots, a "
                "warm-up of one hundred, four batches, seed 0. The exact column is "
                "computed from the chain and does not depend on the seed at all.",
            ],
            "lines": [
                "exact, from the chain started empty",
                "   E[N₀..N₄]     0,  2/5,  3/5,  37/50,  17/20",
                "   stationary    12/5 = 2.4",
                "   E[average over slots   0..399]   2.2443     shortfall 0.1557",
                "   E[average over slots 100..399]   2.3717     shortfall 0.0283",
                "",
                "this run, seed 0",
                "   average from slot 0        169/80  = 2.1125",
                "   average after the warm-up  361/150 ≈ 2.4067",
                "   the discard moved it up by          0.2942",
                "",
                "batch means, four batches of 75 slots each",
                "   slots 100..174     34/25  = 1.36",
                "   slots 175..249    116/75  ≈ 1.5467",
                "   slots 250..324     19/25  = 0.76",
                "   slots 325..399    149/25  = 5.96",
                "   mean of the four  361/150 ≈ 2.4067",
                "   their variance  10733/1875 ≈ 5.72",
                "",
                "the estimate is 0.007 from the exact 12/5",
                "and the four numbers behind it range from 0.76 to 5.96",
            ],
            "after": [
                "The two exact averages are the spine of the page. `2.2443` and `2.3717` "
                "are what the estimator is <em>aimed</em> at with and without the discard, "
                "and both are exact fractions shown to four places. Against the stationary "
                "`2.4` they say the naive estimator is short by about `0.16` in "
                "expectation and the discarded one by about `0.03`, before a single seed "
                "has been chosen.",
                "The run then does its own thing, as runs do. It moved by `0.2942` where "
                "the theory says `0.1274`, and at seed 1 it moves the other way entirely. "
                "Neither observation argues against the theory and neither confirms it; "
                "what confirms it is that the exact column does not move when the seed "
                "does.",
                "For a faded rehearsal, drag the warm-up from `100` to `0` and then to "
                "`200`. The supplied first move is that at a warm-up of zero the two "
                "averages are the same number by definition and the exact expected average "
                "reads `2.2443`. Say what you expect the exact figure to be at a warm-up "
                "of `200`, whether it can ever exceed `12/5`, and what happens to the "
                "batch variance when only two hundred slots are left to split four ways.",
            ],
        },
        "quiz_title": "Bias, dilution and batches",
        "quiz": [
            {"q": "A thousand independent replications, each started from an empty system, are averaged. What happens to the start-up bias?",
             "a": ["It falls like `1/1000`", "It falls like `1/√1000`",
                   "It is unchanged", "It is removed, because the replications are independent"],
             "c": 2,
             "why": "Bias is a property of the estimator's expectation, and averaging "
                    "unbiased-in-nothing copies of the same biased estimator leaves the "
                    "expectation exactly where it was. What the thousand replications do "
                    "is shrink the standard error, which produces a narrow interval "
                    "centred in the wrong place."},
            {"q": "Which does more for the bias: quadrupling the run length, or discarding the first quarter of the run?",
             "a": ["Quadrupling, because it collects four times the data",
                   "Discarding, because the transient is deleted rather than diluted",
                   "They are equivalent, since both change the averaging window by a factor of four",
                   "Neither, because the bias is a property of the model"],
             "c": 1,
             "why": "Diluting a fixed error over a longer window is a `1/T` effect; "
                    "deleting the slots it lives in removes it. On the measured chain, "
                    "quadrupling `100` slots to `400` divides the remaining shortfall by "
                    "about `3.5`, and discarding a quarter of the four-hundred-slot run "
                    "divides it by about `5.5` &mdash; at a quarter of the cost."},
            {"q": "One run gives `1.3075` from slot zero and `1.2367` after a warm-up discard, so the discard moved the estimate down. What does that show?",
             "a": ["That the warm-up was too long",
                   "That the bias for this model is upward, not downward",
                   "Nothing about the bias: one run is an observation of an expectation, and the exact column is what states the bias",
                   "That the run has a bug, since the discard must raise the average"],
             "c": 2,
             "why": "The bias is a statement about `E[estimator]`, and it is stated on the "
                    "page by two exact figures that do not depend on the seed. A single "
                    "run can move either way and often does; the panel prints the exact "
                    "expected averages precisely so that one run is not asked to carry the "
                    "argument."},
            {"q": "Four batch means come out as `1.36`, `1.55`, `0.76` and `5.96`, averaging `2.4067` against an exact `2.4`. What should be reported?",
             "a": ["`2.4067`, since it is within `0.007` of the truth",
                   "`2.4067` together with the batch variance, which says the run has established very little",
                   "The median batch mean, which is more robust to the outlier",
                   "Nothing, since one batch is clearly an outlier and should be dropped"],
             "c": 1,
             "why": "&ldquo;Within `0.007` of the truth&rdquo; is only knowable here "
                    "because the exact answer happens to be available, which is the "
                    "situation a real simulation is never in. The batch variance of about "
                    "`5.72` is the information the run actually produced, and dropping the "
                    "large batch would be discarding the evidence that the system has long "
                    "busy periods."},
        ],
        "mistakes": [
            ("Averaging from slot zero because that is where the run starts",
             "It is the default in every implementation and it is wrong for every "
             "queueing average. On the measured chain the naive estimator is aimed at "
             "`2.2443` where the answer is `2.4`, and no care about the generator, the "
             "sampler or the number of replications touches that gap by a single digit."),
            ("Fixing the bias by running longer",
             "It works, in the sense that `1/T` tends to zero, and it is the expensive way "
             "round. Four times the run length bought a factor of about `3.5` on the "
             "remaining bias here; a quarter of that run thrown away bought a factor of "
             "about `5.5`. Doing both is better than either, and doing only the first is "
             "the common choice because it needs no decision."),
            ("Building an interval from the slots of one run",
             "Consecutive slots of a busy queue are strongly dependent, so the sample "
             "variance over four hundred slots is far smaller than the variance of the "
             "average it is supposed to describe, and the resulting interval is confidently "
             "narrow and wrong. Batch means are the repair, and they are only a repair if "
             "the batches are long enough to have nearly forgotten each other."),
        ],
        "standard": ("Finish when an average taken from slot zero reads as a biased estimator rather than as the obvious one.",
                     "You should be able to say what distinguishes bias from variance and "
                     "which techniques touch which, read the exact expected occupancy of a "
                     "chain started empty and turn it into the expected average over a "
                     "window, compare a longer run against a discard on the numbers rather "
                     "than by intuition, form batch means from one run and state the "
                     "condition under which they may be treated as replications, and say "
                     "why a single run moving the wrong way is not evidence against any of "
                     "it."),
        "note": 'Bias is dealt with. Everything after this page attacks the other half of the problem &mdash; the width &mdash; and all four techniques do it the same way, by moving a covariance rather than by buying draws. &ldquo;Common Random Numbers&rdquo; takes the first and simplest of them: feed two systems the same stream, and read what happens to the variance of their difference.',
    },
]
