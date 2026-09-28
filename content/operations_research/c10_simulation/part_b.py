"""Simulation and Variance Reduction, the last four lessons - four ways to make
the interval narrower without buying draws.

Every one of them moves a covariance, and every one of them leaves the estimate
where it was: an unbiased estimator with a smaller variance is the only kind of
improvement this course recognises. Each is measured against the honest
comparison rather than against the flattering one, and two of the four are shown
failing as well as working. Every figure below is read off the `simulate` kit.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "common-random-numbers",
        "title": "Common Random Numbers",
        "module": "Moving the covariance",
        "one_line": "Feed two systems the same stream, and the variance of their difference falls by twice the covariance.",
        "summary": (
            "When two systems are being compared, the quantity estimated is the "
            "difference, and `Var(A − B) = Var A + Var B − 2 Cov(A, B)`. Driving both "
            "systems from the same draws makes their outputs move together, which makes "
            "that covariance positive and takes twice it off the variance of the "
            "difference. Each system's own estimate is untouched; only the comparison "
            "improves, which is the whole of the technique and the whole of the "
            "misreading to avoid."
        ),
        "key": [
            "Var(A − B) = Var A + Var B − 2 Cov(A, B)       the only identity in play",
            "shared stream ⟹ Cov > 0 ⟹ the variance of the difference falls",
            "q = 1/2 against q = 3/5, same arrivals:  exact means 12/5 and 6/5, difference 6/5",
            "24 replications of 200 slots:  Var(A − B) = 0.80789 shared, 2.10367 separate",
            "Cov = 0.46132 shared,  −0.17812 separate;  1.53075 + 0.19979 − 2(0.46132) = 0.80790",
            "the marginal estimate of A is unchanged;  independent runs are noisier, not fairer",
        ],
        "key_label": "One identity, and what sharing a stream does to it",
        "concepts_intro": (
            "Three ideas. The first says what is being estimated, the second says what "
            "moves, and the third is the credit this technique must not be given."
        ),
        "concepts": [
            ("The thing being estimated is the difference",
             "&ldquo;Is the faster server worth it?&rdquo; is a question about `A − B`, "
             "not about `A` and `B` separately, and the variance of a difference has a "
             "covariance term in it. That term is the only place a comparison can be "
             "improved without buying draws, and it is free: it costs a decision about "
             "seeds and nothing else."),
            ("Sharing the stream induces the covariance",
             "Run both configurations from the same seed and the same draws drive both: "
             "a run that happens to get a heavy burst of arrivals gets it in both "
             "systems, so both outputs are high together and the difference is stable. "
             "The covariance goes positive, `2 Cov` comes off `Var(A − B)`, and the "
             "interval on the comparison narrows."),
            ("Only the difference improves, and only the difference may be credited",
             "The marginal distribution of each system's estimate is exactly what it was "
             "&mdash; sharing a stream changes which draws `B` sees, not the law of "
             "`B`'s output. Reporting a smaller error bar on `A` alone because the runs "
             "were paired is the standard misreading, and it claims a precision that was "
             "never bought."),
        ],
        "read_title": "Two systems, one stream, and the term that comes off",
        "read_intro": "Why a comparison has a covariance in it, how a shared stream makes that covariance positive, and what the technique does not buy.",
        "body": [
            ("def", ("Common random numbers",
                     "A comparison of two configurations in which both are driven by the "
                     "<strong>same</strong> stream of draws, so that replication `j` of "
                     "system `A` and replication `j` of system `B` see the same "
                     "randomness. The alternative &mdash; a fresh stream for each "
                     "&mdash; is the <strong>independent</strong> scheme.")),
            ("thm", ("The variance of a difference",
                     "`Var(A − B) = Var A + Var B − 2 Cov(A, B)`. Hence any scheme that "
                     "makes `Cov(A, B)` positive reduces the variance of the estimated "
                     "difference, and one that makes it negative increases it.")),
            ("proof", ["Expand: `Var(A − B) = E[((A − B) − E[A − B])²]`, and write "
                       "`(A − B) − E[A − B]` as `(A − E[A]) − (B − E[B])`.",
                       "Squaring gives `(A − E[A])² − 2(A − E[A])(B − E[B]) + "
                       "(B − E[B])²`, and taking expectations term by term gives "
                       "`Var A − 2 Cov(A, B) + Var B`. Nothing about the two "
                       "distributions was used, so the identity holds however `A` and "
                       "`B` were generated."]),
            ("p", "That is the entire mechanism. Nothing about queues is involved and "
                  "nothing is approximated: pairing does not make the estimator better in "
                  "some vague sense, it moves one named term of an identity. If the "
                  "covariance does not go positive, the technique has not worked, and the "
                  "panel prints the covariance so that the question is answerable."),
            ("h3", "Why sharing a stream makes the covariance positive"),
            ("p", "The two configurations on this page differ only in the service rate. "
                  "The arrival test in slot `t` reads draw `t`, and the same draw against "
                  "the same arrival probability gives the same answer, so both systems "
                  "see <em>exactly</em> the same arrivals &mdash; verified, not assumed: "
                  "the two runs produce identical arrival lists. A busy stretch is busy "
                  "for both, a quiet one is quiet for both, and the difference between "
                  "their occupancies is then driven by the service draws alone."),
            ("p", "That is also why the kit takes the arrival draw for slot `t` from a "
                  "fixed index and the service draw for the `i`-th customer from another "
                  "fixed index, rather than consuming one stream in event order. "
                  "Consuming in order would make the second system's arrival draws depend "
                  "on how many service draws the first had taken, the two runs would "
                  "silently decorrelate, and the mode built to measure the correlation "
                  "would report a smaller one than the method actually achieves."),
            ("h3", "The measurement"),
            ("math", ["  A:  p = 2/5, q = 1/2   exact mean 12/5",
                      "  B:  p = 2/5, q = 3/5   exact mean  6/5      true difference 6/5",
                      "  24 replications of 200 slots, seed 1",
                      "",
                      "                        shared stream      separate streams",
                      "    Var A                  1.53075             1.53075",
                      "    Var B                  0.19979             0.21668",
                      "    Cov(A, B)              0.46132            −0.17812",
                      "    Var(A − B)             0.80789             2.10367",
                      "",
                      "    check  1.53075 + 0.19979 − 2(0.46132) = 0.80790",
                      "",
                      "    estimate of the difference   1.1329        1.0913",
                      "    ratio of the two variances   2.604"]),
            ("p", "Read the two difference columns and not the two estimates. The "
                  "estimates are `1.1329` and `1.0913`, both aiming at `6/5 = 1.2`, and "
                  "neither is better than the other in any sense the method claims. The "
                  "variance of the difference is `0.80789` against `2.10367`, a factor of "
                  "`2.604`, and that factor is the only thing common random numbers "
                  "bought."),
            ("p", "The separate-stream covariance is `−0.17812` rather than zero, which is "
                  "worth a moment. Independent runs have covariance zero <em>in "
                  "expectation</em>; a sample covariance over twenty-four replications is "
                  "an estimate of zero and lands somewhere near it, on either side. Here "
                  "it landed slightly negative, which pushed the independent variance up "
                  "by `0.356` rather than leaving it at `Var A + Var B`."),
            ("h3", "The reduction is itself an estimate"),
            ("p", "Change the seed and the factor moves: `2.604` at seed 1, `5.770` at "
                  "seed 0, `1.823` at seed 7, on the same twenty-four replications of two "
                  "hundred slots. The covariance is reliably positive; its size is a "
                  "measurement with a spread of its own. This is the course's own hazard "
                  "arriving in the middle of a variance-reduction lesson: the number that "
                  "says how much better the estimator got is an estimate, and quoting it "
                  "to three figures from one seed is exactly the habit the first three "
                  "pages were about."),
            ("example", ("A pair that does not consume the stream in step",
                         "The panel's second pair changes the arrival probability as well "
                         "&mdash; `2/5` against `1/2` &mdash; so the two systems no "
                         "longer see the same arrivals and their service draws line up "
                         "against different customers. The coupling is still strong, and "
                         "on this instance it is stronger: the arrival test is "
                         "`x &lt; 0.4m` in one system and `x &lt; 0.5m` in the other, so "
                         "every arrival in the first is an arrival in the second, and the "
                         "two arrival streams are nested rather than merely similar. The "
                         "measured factor is `5.001` against the first pair's `2.604`.")),
            ("p", "The lesson of that second pair is not that more differences are better. "
                  "It is that the size of the reduction is a property of how the two runs "
                  "happen to couple, that coupling is a fact about the implementation as "
                  "much as about the model, and that the only way to know what a pairing "
                  "bought is to compute both variances and divide. Every claim on this "
                  "page is of that form."),
        ],
        "lab": ("simulate", {
            "mode": "crn",
            "preset": "service",
            "panel_title": "The same draws, or a fresh set, and the variance of the difference",
            "panel_intro": "Both schemes are computed on every redraw, because the claim "
                           "is a comparison and one number cannot make it. The first "
                           "system is the same run in both schemes; only the second "
                           "changes, between reading the first system's draws and reading "
                           "its own. Read down the two difference columns rather than "
                           "across the estimates, then reseed three times and watch the "
                           "reduction factor move while its sign does not.",
        }),
        "steps_title": "Comparing two configurations honestly",
        "steps_intro": "Four steps, and the second is the one that makes the pairing real rather than nominal.",
        "steps": [
            ("Estimate the difference, not the two systems",
             "Form `Dⱼ = Aⱼ − Bⱼ` per replication and take the sample mean and sample "
             "variance of the `D`s. An interval built from `Var A` and `Var B` separately "
             "throws the covariance away and is wider than the data supports."),
            ("Synchronise the draws by purpose, not by order",
             "Arrival draws at one set of indices, service draws at another. If both "
             "systems consume a single stream in event order, a difference anywhere makes "
             "every later draw land in a different place and the pairing evaporates "
             "without any warning."),
            ("Compute both schemes at least once",
             "Run the comparison paired and unpaired on the same replications. The ratio "
             "of the two variances is the only evidence that the pairing did anything, "
             "and it costs one extra set of runs on a question that is usually asked once."),
            ("Report the estimate, both variances, and the covariance",
             "Covariance positive and variance ratio above one is a working pairing. "
             "Covariance near zero means the synchronisation is nominal. Covariance "
             "negative means the pairing is actively hurting, which happens and is worth "
             "finding out before the result is published rather than after."),
        ],
        "worked": {
            "title": "Is the faster server worth it? Twenty-four paired replications",
            "intro": [
                "The two configurations are the slotted queue at `q = 1/2` and at "
                "`q = 3/5`, arrivals at `p = 2/5` in both. The exact long-run means are "
                "`12/5` and `6/5`, so the true difference is `6/5` and every estimate "
                "below can be measured against it.",
            ],
            "lines": [
                "rep   first system   second, shared   difference   second, own   difference",
                "  1      207/200        71/100           13/40         69/50       −69/200",
                "  2       62/25          28/25           34/25        441/200        11/40",
                "  3      221/100        261/200         181/200       221/200       221/200",
                "  4      319/200        109/100         101/200        11/8          11/50",
                "  5      437/200         23/20          207/200         7/8         131/100",
                "      … nineteen more …",
                "",
                "                        shared        separate",
                "  mean difference       1.1329        1.0913        true value 6/5 = 1.2",
                "  Var(A − B)            0.80789       2.10367",
                "  Cov(A, B)             0.46132      −0.17812",
                "  ratio of variances    2.604",
                "",
                "the arrival lists of the two systems are identical, slot for slot",
                "so only the service draws differ, which is what makes Cov large",
            ],
            "after": [
                "The first replication is the one that shows what pairing does. Under the "
                "shared stream the two systems gave `207/200` and `71/100`, a difference "
                "of `13/40 = 0.325`; under separate streams the second system happened to "
                "draw a busy run, gave `69/50 = 1.38`, and the difference came out "
                "`−69/200 = −0.345` &mdash; the wrong sign, on a comparison whose true "
                "answer is `6/5`. Nothing is wrong with that replication; it is one draw "
                "of a quantity with a standard deviation of about `1.45`.",
                "Twenty-four such replications average to almost the same place under "
                "both schemes, which is the point: both estimators are unbiased for "
                "`6/5`. What differs is that one of them has a variance of `0.81` and the "
                "other of `2.10`, so an interval on the first is about `1.6` times "
                "narrower for the same compute.",
                "For a faded rehearsal, drag the slots per replication from `200` to "
                "`800`. The supplied first move is that both variances fall, because each "
                "replication is now a longer-run average of the same system. Say what you "
                "expect to happen to the <em>ratio</em> between them, and then check: it "
                "goes to `1.639`, which is smaller, and the reason is that the two "
                "systems' long-run averages depend less on the particular burst of "
                "arrivals they shared.",
            ],
        },
        "quiz_title": "Covariance, pairing and what it buys",
        "quiz": [
            {"q": "Under common random numbers, what happens to the variance of the estimate of system `A` alone?",
             "a": ["It falls, by the same covariance term", "It rises slightly, as the price of the pairing",
                   "It is unchanged: `A`'s marginal distribution does not depend on what `B` does",
                   "It is undefined, because `A` and `B` are no longer independent"],
             "c": 2,
             "why": "Sharing a stream changes which draws `B` sees. `A` is run exactly as "
                    "it would have been, so its output has exactly the law it had. Only "
                    "the joint distribution changed, and only quantities that depend on "
                    "the joint distribution &mdash; the difference &mdash; can improve."},
            {"q": "A paired comparison reports `Cov(A, B) = −0.4`. What has happened?",
             "a": ["The pairing has worked especially well, since the magnitude is large",
                   "The pairing has made the comparison worse: `−2 Cov` is now `+0.8` on the variance",
                   "Nothing: the sign of a covariance is arbitrary",
                   "The two systems are independent, since a negative covariance averages out"],
             "c": 1,
             "why": "`Var(A − B) = Var A + Var B − 2 Cov(A, B)`, so a negative covariance "
                    "<em>adds</em> to the variance of the difference. Synchronisation that "
                    "makes one system busy exactly when the other is idle is a real "
                    "possibility, and computing the covariance is how you find out."},
            {"q": "Why does this kit read the arrival draw for slot `t` from a fixed index rather than consuming one stream in event order?",
             "a": ["Because fixed indices are faster to compute",
                   "Because otherwise two systems differing in the service rate would stop seeing the same arrivals",
                   "Because a stream consumed in order eventually repeats",
                   "Because the service draws need more bits than the arrival draws"],
             "c": 1,
             "why": "Consumed in order, the first difference in the number of service "
                    "draws shifts every later arrival draw, and the two runs decorrelate "
                    "from that point on. The pairing would look like it was in place, the "
                    "covariance would be small, and the technique would be blamed for an "
                    "implementation detail."},
            {"q": "Paired runs give a variance ratio of `2.604` at one seed and `5.770` at another. What should be reported?",
             "a": ["`5.770`, since it is the best the method achieved",
                   "`2.604`, since it is the conservative figure",
                   "That the pairing reliably reduces the variance, with the factor given as a measurement over several seeds",
                   "Nothing, since the two figures contradict each other"],
             "c": 2,
             "why": "The two figures do not contradict each other: the reduction factor is "
                    "a ratio of two sample variances and is itself an estimate with a "
                    "spread. What is stable is the sign of the covariance. Quoting either "
                    "single figure to three decimals asserts a precision that one seed "
                    "cannot support."},
        ],
        "mistakes": [
            ("Crediting the pairing with a narrower interval on one system",
             "The marginal distribution of `A`'s estimate is untouched, so any error bar "
             "on `A` alone must be computed from `Var A`, which is `1.53075` in both "
             "schemes. The reduction is `2.604` on the difference and exactly `1` on "
             "either system taken by itself."),
            ("Thinking independent runs are the fairer comparison",
             "Fairness is a property of the estimator, not of the seeds, and both schemes "
             "are unbiased for the same `6/5`. Independent runs are simply noisier about "
             "the one quantity the comparison was for &mdash; two and a half times noisier "
             "here &mdash; and choosing them out of a feeling about independence is paying "
             "for nothing."),
            ("Declaring the pairing successful without computing both variances",
             "&ldquo;We used the same seed&rdquo; is a description of the procedure, not "
             "evidence about its effect. The two systems may consume the stream "
             "differently enough that the covariance is near zero, and the only way to "
             "know is to run the unpaired scheme as well and divide."),
        ],
        "standard": ("Finish when a comparison reported without its covariance reads as incomplete.",
                     "You should be able to expand `Var(A − B)` and say which term the "
                     "pairing moves, explain why synchronising by purpose rather than by "
                     "order is what makes the pairing real, compute both variances and "
                     "their ratio from the same replications, say what the technique does "
                     "to a single system's own error bar, and treat the reduction factor "
                     "as the estimate it is."),
        "note": 'Common random numbers moves the covariance between two <em>systems</em>. The next technique moves the covariance between two <em>draws</em> inside one run, and it does it by pairing every draw with its opposite &mdash; which works perfectly when the quantity is monotone in the draw and is exactly twice the work for nothing when it is not. &ldquo;Antithetic Variates&rdquo; has both cases on the same page.',
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "antithetic-variates",
        "title": "Antithetic Variates",
        "module": "Moving the covariance",
        "one_line": "Pair every draw U with 1 − U, average the pair, and read the sign of the covariance you have induced.",
        "summary": (
            "Take a draw `U`, take its opposite `1 − U`, and average the two results. If "
            "the quantity is monotone in `U` the two move in opposite directions, the "
            "covariance is negative, and the variance of the pair mean falls &mdash; to "
            "exactly zero in the best case. If the quantity is symmetric about `1/2` the "
            "two are identical, the covariance is maximally positive, and the pair costs "
            "two draws to produce an observation no better than one."
        ),
        "key": [
            "pair U with 1 − U;  the pair mean is (g(U) + g(1 − U))/2",
            "Var(pair mean) = (Var A + Var B + 2 Cov(A, B))/4       the sign of Cov decides",
            "g monotone in U  ⟹  Cov < 0;  here exactly −1 correlation and Var = 0",
            "g symmetric about 1/2  ⟹  g(1 − U) = g(U);  correlation +1, and twice the work",
            "the honest comparison is against an INDEPENDENT PAIR, not against one draw",
            "inverse-transform sampling is monotone in U by construction",
        ],
        "key_label": "One pairing, and the two things it can do",
        "concepts_intro": (
            "Three ideas. The first is the mechanism, the second is the condition, and the "
            "third is the accounting error that lets this technique take credit it has not "
            "earned."
        ),
        "concepts": [
            ("A pair is one observation, not two draws",
             "The estimator is the average of the pair means, and each pair mean is one "
             "observation of it. That is the whole of the accounting, and it is the only "
             "way to compare fairly: a pair consumes two draws, so it must be judged "
             "against an independent pair, which also consumes two."),
            ("Monotonicity is the condition, and it is a real one",
             "If `g` is non-decreasing in `U` then `g(U)` and `g(1 − U)` move in opposite "
             "directions and their covariance is negative &mdash; that is the whole "
             "argument. Inverse-transform sampling is monotone in `U` by construction, "
             "which is why the technique is available at all on this path. Where "
             "monotonicity fails the covariance can be positive, and then the pairing "
             "costs rather than pays."),
            ("The variance of the pair mean has the covariance in the numerator",
             "`Var((A + B)/2) = (Var A + Var B + 2 Cov(A, B))/4`. With `A` and `B` "
             "identically distributed this is `(Var A + Cov)/2`, against `Var A/2` for an "
             "independent pair. The entire effect is the covariance term, and it can take "
             "the variance anywhere from zero to twice the independent value."),
        ],
        "read_title": "A draw and its opposite, in the best case and in the worst",
        "read_intro": "How pairing induces a covariance, what monotonicity has to do with its sign, and what the pair has to be compared against.",
        "body": [
            ("def", ("Antithetic pair",
                     "Given one uniform draw `U`, the <strong>antithetic pair</strong> is "
                     "`U` and `1 − U`. If `U` is uniform on `[0, 1)` then so is `1 − U`, "
                     "so each half of the pair is a legitimate draw and the estimator "
                     "built on the pair mean is unbiased for the same quantity as the "
                     "ordinary one.")),
            ("thm", ("The variance of a pair mean",
                     "For `A = g(U)` and `B = g(1 − U)` with the same distribution, "
                     "`Var((A + B)/2) = (Var A + Cov(A, B))/2`. An independent pair has "
                     "`Cov = 0` and therefore variance `Var A/2`, so the antithetic pair "
                     "is better exactly when `Cov(A, B) &lt; 0` and worse exactly when it "
                     "is positive.")),
            ("proof", ["`Var((A + B)/2) = (Var A + Var B + 2 Cov(A, B))/4`, which is the "
                       "expansion of the variance of a sum divided by four.",
                       "`A` and `B` have the same distribution, because `U` and `1 − U` "
                       "do, so `Var B = Var A` and the expression is "
                       "`(2 Var A + 2 Cov)/4 = (Var A + Cov)/2`. Setting `Cov = 0` gives "
                       "the independent-pair value `Var A/2`, and the comparison is the "
                       "sign of `Cov`."]),
            ("p", "So the technique has no magic in it and no tuning: it is a choice about "
                  "which second draw to take, and the choice is good or bad according to "
                  "the sign of one number. The panel prints that number."),
            ("h3", "The best case, and it is exact"),
            ("example", ("A monotone quantity: g(U) = 1 when U is at least 1/2",
                         "Sixty-four pairs from the standard stream. Whenever `U ≥ 1/2` "
                         "the partner `1 − U` is below `1/2`, and conversely, so one of "
                         "the two is always `1` and the other always `0`: every pair mean "
                         "is exactly `1/2`. The sample variance of the pair means is "
                         "exactly `0`, the correlation within a pair is exactly `−1`, and "
                         "an independent pair would have had variance `247/2016`.")),
            ("p", "Look at what that does to the estimate. The sixty-four single draws "
                  "came out `1` thirty-eight times, so an ordinary estimator on the same "
                  "draws would report `19/32 = 0.59375` against a true value of `1/2`. "
                  "The antithetic estimator reports `1/2`, exactly, because every pair "
                  "mean is `1/2`, exactly. The variance is not small here; it is zero, and "
                  "the arithmetic says so rather than the picture."),
            ("h3", "The worst case, and it is exactly twice as bad"),
            ("example", ("A symmetric quantity: g(U) = the distance from U to 1/2",
                         "`|(1 − U) − 1/2| = |1/2 − U|`, so `g(1 − U)` is `g(U)` "
                         "identically: the two halves of the pair are the same number. "
                         "The correlation is exactly `+1`, the pair mean has exactly the "
                         "variance of a single draw &mdash; both `0.022439`, exact "
                         "fractions shown to six places &mdash; and an independent pair "
                         "would have had `0.011219`. The ratio is exactly `2`.")),
            ("p", "Two draws were consumed to produce one observation that is no better "
                  "than one draw. That is not a mild disappointment; it is exactly double "
                  "the work for exactly the same width, and it is what happens when the "
                  "condition fails. A reader who has only ever seen the technique work "
                  "cannot tell the condition from the conclusion, which is why both cases "
                  "are on the page rather than one of them being mentioned in a footnote."),
            ("math", ["  64 pairs, the same stream, the same seed",
                      "",
                      "                       monotone g        symmetric g",
                      "    exact mean            1/2                1/4",
                      "    Var of one draw      247/1008          0.022439",
                      "    Var, independent pair 247/2016          0.011219",
                      "    Var, antithetic pair    0              0.022439",
                      "    Cov within a pair    −247/1008         0.022439",
                      "    squared correlation      1                 1",
                      "",
                      "    antithetic / independent    0                2",
                      "",
                      "  same squared correlation, opposite sign, opposite result"]),
            ("p", "The squared correlation is `1` in both columns, and that is the sharpest "
                  "way to see why `ρ²` is not the whole story here. `ρ² = 1` says the two "
                  "halves of the pair determine each other; the <em>sign</em> of the "
                  "covariance says whether that is worth nothing or worth everything. "
                  "Later on this course `ρ²` is exactly the right summary, because there "
                  "the sign has been optimised away; here it is not."),
            ("h3", "Why this is available at all on this path"),
            ("p", "Inverse-transform sampling returns the first value whose cumulative "
                  "probability reaches `U`, so a larger `U` never gives a smaller value: "
                  "the sampler is monotone in `U` by construction. Any quantity that is a "
                  "non-decreasing function of the sampled values is therefore monotone in "
                  "`U`, and the pairing is guaranteed to have a negative covariance. That "
                  "is a property of the method built in the opening lesson of this course, "
                  "not a lucky feature of the examples."),
            ("p", "It stops being guaranteed the moment a run uses more than one draw in a "
                  "way that is not monotone in each of them, which is most interesting "
                  "simulations. The queue runs earlier on this course are not monotone in "
                  "the service draws in any useful sense, which is why the pairing is "
                  "demonstrated here on functions of a single draw, where the claim can be "
                  "exact, rather than asserted on a system where it would have to be "
                  "hoped for."),
        ],
        "lab": ("simulate", {
            "mode": "antithetic",
            "preset": "monotone",
            "panel_title": "The pair table, and the variance column beside it",
            "panel_intro": "Read the last column of the pair table first. In the monotone "
                           "case every entry is `1/2` &mdash; the same number, sixty-four "
                           "times &mdash; and the variance of the pair mean is exactly "
                           "zero. Then switch to the symmetric case and read it again: "
                           "every entry is the draw itself, the pairing has bought "
                           "nothing, and the bar chart shows the antithetic pair at "
                           "exactly twice the variance of an independent one.",
        }),
        "steps_title": "Pairing draws, and accounting for them",
        "steps_intro": "Four steps, and the last is the one that decides whether the technique is being measured or flattered.",
        "steps": [
            ("Check that the quantity is monotone in the draw",
             "Not &ldquo;roughly increasing&rdquo; &mdash; monotone. If a larger `U` can "
             "give a smaller output anywhere, the covariance is not guaranteed negative, "
             "and the technique becomes something to measure rather than something to "
             "rely on."),
            ("Use U for one half of the pair and 1 − U for the other",
             "Both halves are uniform, so both are legitimate draws, and each half on its "
             "own is an unbiased sample. Nothing about the model changes; only the second "
             "draw's provenance does."),
            ("Average within the pair first, and treat the pair mean as the observation",
             "The sequence of pair means is what the estimator is built from. Its length "
             "is half the number of draws, and that is the correct denominator for every "
             "variance computed afterwards."),
            ("Compare against an independent pair, never against a single draw",
             "A pair costs two draws either way. Comparing an antithetic pair mean against "
             "one draw makes the technique look like a factor-of-two improvement even when "
             "the covariance is zero, which is how it is routinely credited with a "
             "reduction it did not make."),
        ],
        "worked": {
            "title": "Sixty-four pairs, the best case and the worst, on the same draws",
            "intro": [
                "The two quantities are functions of a single uniform draw, which is what "
                "makes both claims exact rather than measured. `g(U) = 1` when `U ≥ 1/2` "
                "is monotone and has mean `1/2`; `g(U) = |U − 1/2|` is symmetric about "
                "`1/2` and has mean `1/4`.",
            ],
            "lines": [
                "monotone case:  g(U) = 1 if U ≥ 1/2, else 0",
                "",
                "  pair     U          1 − U      g(U)   g(1−U)   pair mean",
                "         (both exact fractions, shown to five places)",
                "    1    0.93425    0.06575       1       0        1/2",
                "    2    0.87963    0.12037       1       0        1/2",
                "    3    0.00891    0.99109       0       1        1/2",
                "    4    0.73728    0.26272       1       0        1/2",
                "    5    0.49863    0.50137       0       1        1/2",
                "         … sixty-four rows, every pair mean 1/2 …",
                "",
                "  Var of the pair means                0        exactly",
                "  Cov within a pair              −247/1008",
                "  Var of one draw                 247/1008",
                "  Var of an independent pair      247/2016",
                "  the single draws alone average    19/32 = 0.59375",
                "  the pair means average             1/2   exactly",
                "",
                "symmetric case:  g(U) = |U − 1/2|",
                "",
                "  every pair mean equals the draw itself",
                "  Var of the pair mean            0.022439",
                "  Var of one draw                 0.022439      the same number",
                "  Var of an independent pair      0.011219",
                "  antithetic / independent               2      exactly",
            ],
            "after": [
                "The `19/32` is the figure to keep. Thirty-eight of the sixty-four single "
                "draws landed above `1/2`, which is a perfectly ordinary sixty-four-draw "
                "sample and would have produced an estimate of `0.59375` with a standard "
                "error of about `0.061`. The same draws, paired with their opposites, "
                "produce `1/2` with no error at all &mdash; not a small error, none.",
                "That happens because this `g` takes two values and the pairing balances "
                "them perfectly. On a monotone `g` with more values the covariance is "
                "still negative and the reduction is still real, but it is partial, and "
                "the number to report is the ratio of the two variances rather than the "
                "word &ldquo;antithetic&rdquo;.",
                "For a faded rehearsal, halve the number of pairs from `64` to `32` in "
                "each case. The supplied first move is that in the monotone case nothing "
                "whatever happens to the variance of the pair mean: it is zero at every "
                "count, because every individual pair mean is `1/2`. Say what happens to "
                "the symmetric case's ratio, and why that one is also insensitive to the "
                "count.",
            ],
        },
        "quiz_title": "Pairs, signs and fair comparisons",
        "quiz": [
            {"q": "An antithetic scheme is compared against a single draw and reported as halving the variance. What is wrong with that comparison?",
             "a": ["Nothing: the pair mean does have half the variance of a draw",
                   "A pair costs two draws, so the comparison must be against an independent pair, which also has half",
                   "The pair mean is biased, so its variance is not comparable",
                   "The variance of a pair mean is never less than that of a single draw"],
             "c": 1,
             "why": "An independent pair already has variance `Var A/2` for free. Any "
                    "scheme that consumes two draws must be judged against that, and the "
                    "antithetic scheme's claim is whatever it achieves <em>beyond</em> it "
                    "&mdash; which is the covariance term and nothing else."},
            {"q": "For `g(U) = |U − 1/2|`, what is the correlation between `g(U)` and `g(1 − U)`?",
             "a": ["`−1`, because `1 − U` is the opposite draw",
                   "`0`, because the function is symmetric",
                   "`+1`, because `g(1 − U)` is `g(U)` identically",
                   "It depends on the sample"],
             "c": 2,
             "why": "`|(1 − U) − 1/2| = |1/2 − U| = |U − 1/2|`, so the two halves of the "
                    "pair are literally the same number. Perfect positive correlation, "
                    "and the pair mean therefore has exactly the variance of one draw "
                    "&mdash; twice what an independent pair would have had."},
            {"q": "Why is the antithetic pairing guaranteed to help when the output is a non-decreasing function of the sampled values?",
             "a": ["Because inverse-transform sampling is monotone in `U`, so the two halves move in opposite directions and the covariance is negative",
                   "Because `U` and `1 − U` are independent",
                   "Because the sample mean of `U` and `1 − U` is always `1/2`",
                   "Because a non-decreasing function has bounded variance"],
             "c": 0,
             "why": "Monotonicity of the sampler composes with monotonicity of the output, "
                    "so a larger `U` gives a larger `A` and a smaller `B`. `U` and "
                    "`1 − U` are as dependent as two variables can be, which is the whole "
                    "mechanism; and the mean of the two uniforms being `1/2` says nothing "
                    "about the mean of `g` of them."},
            {"q": "In both the monotone and the symmetric case the squared correlation is `1`. What does that tell you about `ρ²` as a summary here?",
             "a": ["That both cases are equally good, since `ρ²` is the reduction factor",
                   "That `ρ²` alone cannot distinguish them, because it discards the sign that decides the outcome",
                   "That one of the two `ρ²` values must be a computational error",
                   "That `ρ²` is only meaningful for continuous quantities"],
             "c": 1,
             "why": "`ρ² = 1` says each half of the pair determines the other, which is "
                    "true in both cases. Whether that is worth everything or worth less "
                    "than nothing is the sign of the covariance. `ρ²` becomes the right "
                    "summary in the control-variate setting, where the coefficient is "
                    "chosen so that the sign cannot hurt."},
        ],
        "mistakes": [
            ("Counting a pair as two independent observations",
             "It is one observation of the pair mean, and using `2n` as the denominator "
             "of the variance of the estimator understates it by a factor that depends on "
             "the covariance. In the symmetric case it understates it by two, which turns "
             "a technique that doubled the cost into one that appears to have halved the "
             "width."),
            ("Assuming the pairing helps because it is called a variance reduction",
             "On `g(U) = |U − 1/2|` it doubles the variance per unit of work, with the "
             "same estimator, the same unbiasedness and the same code. The name describes "
             "the intent; the covariance describes the result, and only one of them is "
             "printed by the panel."),
            ("Applying it to a run whose output is not monotone in the draws",
             "A queueing run uses hundreds of draws and is not a monotone function of most "
             "of them. Pairing the whole stream with its complement is then a scheme whose "
             "covariance has no guaranteed sign, and it has to be measured on the model in "
             "hand rather than assumed from the name."),
        ],
        "standard": ("Finish when the first question about an antithetic scheme is the sign of its covariance.",
                     "You should be able to derive `Var((A + B)/2) = (Var A + Cov)/2` for "
                     "identically distributed halves, say why monotonicity in `U` makes "
                     "the covariance negative, state the correct comparison and why it is "
                     "an independent pair, produce the exact zero in the best case and the "
                     "exact factor of two in the worst, and explain why `ρ²` is not "
                     "sufficient to tell those two cases apart."),
        "note": 'Both techniques so far move a covariance that is already there for free. The next one pays for it: it brings in a second quantity whose mean is known, and chooses how much of it to subtract. &ldquo;Control Variates&rdquo; turns the variance into a quadratic in that choice, finds the vertex exactly, and shows what the wrong choice costs on either side of it.',
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "control-variates",
        "title": "Control Variates",
        "module": "Moving the covariance",
        "one_line": "Subtract a multiple of a companion quantity whose mean you know, and choose the multiple at the vertex of a parabola.",
        "summary": (
            "Take a second quantity `C` measured on the same run whose expectation is "
            "<em>known</em>, and report `X − b(C − E[C])`. The correction has expectation "
            "zero, so the estimator is unbiased at every `b`, and its variance is a "
            "quadratic in `b` whose vertex sits at `b* = Cov(X, C)/Var C`. There the "
            "variance has been multiplied by `1 − ρ²`. The condition is the known mean, "
            "not the correlation &mdash; and a control with a known mean and no "
            "correlation buys almost nothing."
        ),
        "key": [
            "X − b(C − E[C])        unbiased for E[X] at EVERY b, because E[C − E[C]] = 0",
            "Var = Var X − 2b Cov(X, C) + b² Var C          a quadratic in b, opening upward",
            "b* = Cov(X, C) / Var C                          its vertex, by completing the square",
            "at b*:  Var X × (1 − ρ²)      with ρ² = Cov² / (Var X · Var C), an exact rational",
            "arrivals as the control:  ρ² = 0.457615,  1.530750 becomes 0.830256",
            "b = 0 and b = 2b* give exactly the same variance;  b = −b* is worse than no control",
        ],
        "key_label": "One correction, one quadratic, and its vertex",
        "concepts_intro": (
            "Three ideas. The first is why the estimator stays honest at every `b`, the "
            "second is how the best `b` is found, and the third is the condition people "
            "substitute something easier for."
        ),
        "concepts": [
            ("The correction has expectation zero, so nothing is risked",
             "`E[C − E[C]] = 0` by definition, so `E[X − b(C − E[C])] = E[X]` for every "
             "`b`, good or bad. A control variate cannot bias the estimate; the only "
             "thing at stake is the variance, and the worst outcome is a variance larger "
             "than you started with."),
            ("The variance is a quadratic, so the best b is a vertex and not a search",
             "`Var X − 2b Cov(X, C) + b² Var C` opens upward, so completing the square "
             "puts its minimum at `b* = Cov/Var C`, and the minimum value is "
             "`Var X (1 − ρ²)`. Both `b*` and `ρ²` are ratios of exact sample quantities, "
             "so the optimum is computed rather than tuned."),
            ("The condition is a KNOWN mean, not a strong correlation",
             "A control whose mean you estimated from the same run puts back exactly the "
             "error it was brought in to remove. Correlation decides how much the control "
             "is worth; a known mean decides whether it is a control at all. The two get "
             "confused because the second is usually easy and the first is usually the "
             "reason a candidate fails."),
        ],
        "read_title": "A companion with a known mean, and the coefficient that uses it",
        "read_intro": "Why the correction is free, where the best coefficient is, what it buys, and what happens when the coefficient is wrong.",
        "body": [
            ("def", ("Control variate",
                     "A <strong>control variate</strong> for an estimator `X` is a second "
                     "quantity `C`, measured on the same run, whose expectation `E[C]` is "
                     "known exactly. The <strong>controlled estimator</strong> is "
                     "`X − b(C − E[C])` for a coefficient `b` chosen by the "
                     "experimenter.")),
            ("p", "The word <em>known</em> is the whole definition. `E[C]` has to be a "
                  "number you can write down before the run: the number of slots times "
                  "the arrival probability, the expected number of coin flips that come "
                  "up heads, the mean of a distribution you are sampling from. A quantity "
                  "whose mean you would have to estimate is not a control variate, "
                  "whatever its correlation with `X`."),
            ("thm", ("The optimal coefficient and what it achieves",
                     "`Var(X − b(C − E[C])) = Var X − 2b Cov(X, C) + b² Var C`, a "
                     "quadratic in `b` with positive leading coefficient. Its minimum is "
                     "at `b* = Cov(X, C)/Var C`, and the value there is "
                     "`Var X · (1 − ρ²)` where `ρ² = Cov(X, C)²/(Var X · Var C)`.")),
            ("proof", ["The variance of `X − bD` with `D = C − E[C]` is "
                       "`Var X − 2b Cov(X, D) + b² Var D`, and `Var D = Var C`, "
                       "`Cov(X, D) = Cov(X, C)`, because subtracting a constant changes "
                       "neither.",
                       "Complete the square: "
                       "`Var C (b − Cov/Var C)² + Var X − Cov²/Var C`. The first term is "
                       "non-negative and vanishes at `b = Cov/Var C`, so that is the "
                       "minimiser.",
                       "The value there is `Var X − Cov²/Var C`, which is "
                       "`Var X (1 − Cov²/(Var X · Var C)) = Var X (1 − ρ²)`."]),
            ("h3", "Rho is irrational and rho squared is not"),
            ("p", "`ρ = Cov(X, C)/(σ_X σ_C)` is a covariance divided by a product of two "
                  "square roots, and it is irrational at almost any data. `ρ²` is "
                  "`Cov²/(Var X · Var C)`, a ratio of three exact rationals, so the "
                  "reduction factor `1 − ρ²` is exact even where `ρ` is not. That is why "
                  "this page prints `ρ²` everywhere and `ρ` once, with the rounding named "
                  "&mdash; and `ρ` is the third and last of the three quantities on this "
                  "course that are genuinely irrational."),
            ("p", "What `ρ` adds over `ρ²` is its sign, and here the sign has already been "
                  "used: it is inside `b*`. A negatively correlated control works exactly "
                  "as well as a positively correlated one, because `b*` comes out "
                  "negative and the correction changes direction with it. That is the "
                  "difference from the previous technique, where the sign could not be "
                  "chosen and therefore decided everything."),
            ("h3", "The measurement"),
            ("example", ("The arrivals as a control for the queue's occupancy",
                         "`X` is the time-average number in system over a run of two "
                         "hundred slots; `C` is the number of arrivals in that run. `C` "
                         "is a sum of two hundred indicators of probability `2/5`, so "
                         "`E[C] = 80` exactly &mdash; known, not estimated &mdash; and "
                         "the arrivals plainly drive the queue. Over twenty-four "
                         "replications: `Cov(X, C) = 172147/27600 ≈ 6.23721`, "
                         "`Var C = 3832/69 ≈ 55.5362`, so "
                         "`b* = 172147/1532800 ≈ 0.1123`.")),
            ("math", ["  X = time average in system,  C = arrivals,  E[C] = 200 × 2/5 = 80",
                      "  24 replications of 200 slots, seed 1",
                      "",
                      "     Var X                1.530750",
                      "     Cov(X, C)            6.23721",
                      "     Var C               55.5362",
                      "     b* = Cov/Var C       0.1123",
                      "     ρ²                   0.457615        exact, shown to 6 places",
                      "     1 − ρ²               0.542385        exact, shown to 6 places",
                      "     variance at b*       0.830256",
                      "",
                      "     ρ ≈ 0.6765                           (rounded)",
                      "",
                      "  1.530750 × 0.542385 = 0.830255…      the factor does the work"]),
            ("p", "Just over forty-five per cent of the variance removed, from a quantity "
                  "that was already being recorded and cost nothing to collect. That is a "
                  "typical result for a good control, and it compares well with buying it: "
                  "the same reduction from more runs would take about `1/0.542`, nearly "
                  "twice the replications."),
            ("h3", "Both ways the coefficient can be wrong"),
            ("p", "The parabola rises on both sides of `b*`, and it rises symmetrically. "
                  "At `b = 0` the variance is `1.530750`, which is the uncontrolled value "
                  "&mdash; correctly, since `b = 0` is no control. At `b = 2b*` it is "
                  "`1.530750` again, exactly: overshooting the optimum by a factor of two "
                  "throws away the entire benefit and leaves you no worse off than not "
                  "having bothered. At `b = −b*`, the right magnitude with the wrong sign, "
                  "it is `3.632232` &mdash; more than twice the uncontrolled variance, and "
                  "the one outcome that is actively bad."),
            ("example", ("A control with a known mean and no correlation",
                         "The panel's second companion counts, out of two hundred draws "
                         "from a stream the queue never reads, how many fall below `1/2`. "
                         "Its mean is exactly `100`, every bit as firmly known as the "
                         "arrivals' `80`, and it has almost nothing to do with the queue: "
                         "`ρ² = 0.074965`, so `1 − ρ² = 0.925035` and the variance falls "
                         "only from `1.530750` to `1.415997`. A known mean is necessary "
                         "and it is not sufficient.")),
            ("p", "The reverse case &mdash; a strongly correlated quantity whose mean is "
                  "not known &mdash; is not a weaker control; it is not a control. "
                  "Substituting an estimate of `E[C]` from the same replications makes the "
                  "correction correlated with the very error it was supposed to cancel, "
                  "and the estimator stops being unbiased. That failure does not show up "
                  "in any variance figure on the page, which is what makes it worth "
                  "stating as a condition rather than as advice."),
            ("p", "The control does not have to be the target in disguise, either. Any "
                  "quantity that moves with `X` and has a known mean will do, and the "
                  "arrivals are a good example precisely because they are an input rather "
                  "than an output: their mean is known from the model specification and "
                  "needs no analysis of the queue at all."),
        ],
        "lab": ("simulate", {
            "mode": "control",
            "preset": "arrivals",
            "chain": "base",
            "panel_title": "Choose the companion, then drag b off its optimum",
            "panel_intro": "The curve is the variance as a function of `b`, sampled from "
                           "the same quadratic the figures come out of, so the picture and "
                           "the numbers cannot disagree. The purple mark is the vertex "
                           "`b* = Cov(X, C)/Var C` and the hollow one is the `b` you "
                           "chose. Drag `b` to `0%`, to `200%` and to `−100%` of `b*` and "
                           "read the three variances; then switch the companion to the "
                           "count from an unrelated stream and watch `1 − ρ²` go to "
                           "`0.925035`.",
        }),
        "steps_title": "Choosing and using a control variate",
        "steps_intro": "Five steps, and the first one disqualifies most of the candidates people reach for.",
        "steps": [
            ("Write down E[C] before the run, or reject the candidate",
             "If you cannot state the control's expectation from the model specification "
             "&mdash; `200 × 2/5 = 80`, and nothing measured &mdash; then it is not a "
             "control variate. Estimating `E[C]` from the same replications reintroduces "
             "exactly the error the control was for, and no figure on the page will show "
             "it."),
            ("Collect C on every replication alongside X",
             "It is usually free: the arrival count was already being computed. A control "
             "that costs a second simulation run has to be worth more than the runs it "
             "displaces, which is a much harder test to pass."),
            ("Compute Cov(X, C), Var C, and b* as exact fractions",
             "`b* = Cov/Var C`. No search and no tuning: the variance is a quadratic and "
             "its vertex is an arithmetic expression in quantities you already have."),
            ("Report 1 − ρ² as the reduction, and report it as exact",
             "`ρ²` is a ratio of three exact rationals even though `ρ` is not, so the "
             "factor `1 − ρ²` can be printed in full. It is the honest headline: "
             "`0.542385` says what the control did, and `0.6765` for `ρ` is a rounded "
             "decimal that says less."),
            ("Sanity-check the sign, not just the size",
             "A `b` of the right magnitude and the wrong sign more than doubles the "
             "variance here. Since `b*` carries the sign of the covariance automatically, "
             "the way to get this wrong is to impose a sign by hand, and the check is to "
             "confirm that the variance at your `b` is below the variance at `b = 0`."),
        ],
        "worked": {
            "title": "The arrivals as a control, and the parabola either side of b*",
            "intro": [
                "Twenty-four replications of two hundred slots at `p = 2/5`, `q = 1/2`, "
                "seed 1. `X` is the run's time-average number in system and `C` is its "
                "arrival count, whose expectation is `200 × 2/5 = 80` exactly.",
            ],
            "lines": [
                "rep     X          C      C − 80     X − b*(C − 80)",
                "  1   207/200      78       −2           1.2596",
                "  2    62/25       90      +10           1.3569",
                "  3   221/100      86       +6           1.5361",
                "  4   319/200      79       −1           1.7073",
                "  5   437/200      76       −4           2.6342",
                "  6   303/200      70      −10           2.6381",
                "     … eighteen more …",
                "",
                "  Cov(X, C)   172147/27600   ≈  6.23721",
                "  Var C         3832/69      ≈ 55.5362",
                "  Var X    33798959/22080000 ≈  1.530750",
                "",
                "  b* = Cov / Var C = 172147/1532800 ≈ 0.1123",
                "  ρ²      = 0.457615        1 − ρ² = 0.542385      both exact",
                "  variance at b*                    0.830256",
                "",
                "the parabola, read at four values of b",
                "     b = −b*      3.632232      worse than no control",
                "     b = 0        1.530750      no control",
                "     b = b*       0.830256      the minimum",
                "     b = 2b*      1.530750      exactly no control again",
            ],
            "after": [
                "The `C − 80` column is the whole idea in one place. Replication 6 drew "
                "only seventy arrivals, ten below the known mean, and its raw `X` of "
                "`303/200 = 1.515` is low partly for that reason; the correction adds "
                "`b* × 10`, about `1.1231`, back and lands at `2.6381`. The estimator is not being nudged toward the "
                "answer &mdash; the correction has expectation zero &mdash; it is having a "
                "known source of run-to-run variation removed.",
                "The symmetry of the last block is worth keeping. `b = 0` and `b = 2b*` "
                "give the same variance to the last digit, because a parabola is symmetric "
                "about its vertex, so the penalty for overshooting by a factor of two is "
                "exactly the benefit foregone. The penalty for the wrong sign is not "
                "symmetric with anything: `3.632232` against `1.530750` is a control that "
                "has made the estimate more than twice as noisy.",
                "For a faded rehearsal, switch the configuration to the busier queue, "
                "`p = 1/2` and `q = 3/5`. The supplied first move is that `E[C]` becomes "
                "`200 × 1/2 = 100` exactly, so the whole `C − E[C]` column shifts. Predict "
                "whether `ρ²` will rise or fall &mdash; the arrivals now drive a queue "
                "that is closer to saturation &mdash; and say what you would need to see "
                "before believing your prediction rather than the one seed in front of "
                "you.",
            ],
        },
        "quiz_title": "Coefficients, conditions and what the factor means",
        "quiz": [
            {"q": "A colleague proposes using the run's own mean waiting time as a control variate for its mean queue length. What is the problem?",
             "a": ["The two are too strongly correlated to be useful",
                   "Its expectation is not known in advance; it is exactly the sort of thing the simulation is being run to find out",
                   "It has the wrong units",
                   "Nothing: strong correlation is the condition for a control variate"],
             "c": 1,
             "why": "The condition is a known mean. A quantity the simulation exists to "
                    "estimate has no known mean by construction, and substituting an "
                    "estimate of it from the same replications reintroduces the error the "
                    "control was for. Strong correlation is what makes a valid control "
                    "valuable, not what makes it valid."},
            {"q": "The controlled estimator is used with `b = 2b*` by mistake. What happens?",
             "a": ["The variance is doubled relative to `b*`",
                   "The estimator becomes biased",
                   "The variance returns to exactly its uncontrolled value",
                   "The variance is halved, since `b` is a scale factor"],
             "c": 2,
             "why": "The variance is a parabola symmetric about `b*`, and `b = 0` and "
                    "`b = 2b*` are equidistant from it, so they give the same value "
                    "&mdash; `1.530750` in both cases on the measured run. Unbiasedness "
                    "holds at every `b`, so nothing about the estimate's aim has changed."},
            {"q": "Why does this course print `ρ²` rather than `ρ` almost everywhere?",
             "a": ["Because `ρ` can be negative and `ρ²` cannot",
                   "Because `ρ²` is a ratio of exact rationals while `ρ` is a covariance over a product of two square roots",
                   "Because `ρ²` is easier to interpret as a percentage",
                   "Because `ρ` is undefined when the covariance is negative"],
             "c": 1,
             "why": "`ρ² = Cov²/(Var X · Var C)` has no root in it, so the reduction factor "
                    "`1 − ρ²` is exact. `ρ` is one of the three genuinely irrational "
                    "quantities on this course and is printed once, rounded and labelled. "
                    "Its sign is real information, and here it has already been used "
                    "&mdash; it is inside `b*`."},
            {"q": "A control with `ρ² = 0.075` and a perfectly known mean is applied. What should be expected?",
             "a": ["A variance reduction of about `92.5%`",
                   "A variance multiplied by about `0.925`, which is a reduction of about `7.5%`",
                   "No change, since `ρ²` is close to zero",
                   "An increase in variance, since the correlation is weak"],
             "c": 1,
             "why": "The factor is `1 − ρ² = 0.925035`, so the variance falls from "
                    "`1.530750` to `1.415997`. That is a real but small improvement, "
                    "bought for nothing, and it is exactly the case the panel's second "
                    "companion exists to show: a known mean with no correlation is a valid "
                    "control that is barely worth having."},
        ],
        "mistakes": [
            ("Using a control whose mean was estimated from the same run",
             "The correction is then correlated with the error it is meant to cancel, and "
             "the estimator is no longer unbiased. Nothing on the page reveals it: the "
             "variance figures all look fine, and the variance of a biased estimator is a "
             "perfectly well-defined number that says nothing about how far the estimate "
             "is from the truth."),
            ("Choosing b by hand, or imposing a sign on it",
             "`b* = Cov/Var C` is an arithmetic expression in quantities already computed, "
             "and it carries the correct sign automatically. Setting `b = 1` because the "
             "control &ldquo;should track&rdquo; `X`, or flipping the sign because the "
             "correction &ldquo;should be a subtraction&rdquo;, is how a control ends up "
             "at `3.632232` against an uncontrolled `1.530750`."),
            ("Treating correlation as the condition and the known mean as a detail",
             "It is the other way round. The measured page has one control with `ρ²` of "
             "`0.458` and one with `0.075`, and both are valid because both means are "
             "known exactly. A candidate with `ρ²` of `0.9` and an estimated mean is not "
             "a better control; it is not one."),
        ],
        "standard": ("Finish when the first question about a proposed control is whether its mean is known.",
                     "You should be able to state why the controlled estimator is unbiased "
                     "at every `b`, complete the square to find `b*` and the value "
                     "`Var X (1 − ρ²)` there, compute `Cov`, `Var C`, `b*` and `ρ²` as "
                     "exact quantities from a set of replications, say what `b = 0`, "
                     "`b = 2b*` and `b = −b*` each cost, and distinguish a control that is "
                     "weak from one that is invalid."),
        "note": 'All three techniques so far leave the sampling distribution alone and rearrange what is computed from it. The last one changes the distribution being sampled from, which is the only way to reach an event that almost never happens &mdash; and it is the one technique on this course that can make things enormously worse. &ldquo;Importance Sampling for Rare Events&rdquo; measures both directions on the same event.',
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "importance-sampling-for-rare-events",
        "title": "Importance Sampling for Rare Events",
        "module": "Sampling somewhere else",
        "one_line": "Sample from a distribution where the event is common, weight each draw by p/q, and read the variance rather than the estimate.",
        "summary": (
            "Direct simulation of an event with probability `1/1024` spends almost every "
            "draw learning nothing. Importance sampling draws from a different "
            "distribution `q` under which the event is common and weights each draw by "
            "the likelihood ratio `p/q`, which keeps the estimator unbiased. The whole "
            "question is what the reweighting does to the variance: a good `q` divides it "
            "by about `123`, a bad one multiplies it by about `9546`, and a `q` with a "
            "hole where the event lives gives no estimator at all."
        ),
        "key": [
            "E_p[h(X)] = E_q[h(X)·p(X)/q(X)]        provided q > 0 wherever p·h is",
            "the weight p/q is the likelihood ratio, and it is where the variance lives",
            "ten fair coins, all heads:  probability exactly 1/1024,  Var = p(1 − p) = 1023/1048576",
            "q with P(head) = 4/5:   variance DIVIDED by 32505856/264153 ≈ 123.0569",
            "q with P(head) = 1/5:   variance MULTIPLIED by 295928/31 ≈ 9546.0645",
            "q with the event removed:  refused — there is no estimator, and that is the answer",
        ],
        "key_label": "One identity, one weight, and three things it can do",
        "concepts_intro": (
            "Three ideas. The first is the identity, the second is the condition that "
            "decides whether there is an estimator at all, and the third is where all the "
            "risk in the method is concentrated."
        ),
        "concepts": [
            ("Reweighting is an identity, not an approximation",
             "`E_p[h] = Σ h(x)p(x) = Σ h(x)(p(x)/q(x))q(x) = E_q[h·p/q]`, which is "
             "multiplying and dividing by the same thing. So the reweighted estimator is "
             "unbiased for the same number as the direct one, exactly, for every valid "
             "`q`. The estimate is not where the difference between a good `q` and a bad "
             "one lives."),
            ("The support condition is the only condition, and it is absolute",
             "`q` must put positive mass everywhere `p·h` does. If it does not, the "
             "likelihood ratio is undefined exactly where the event lives, and an "
             "implementation that quietly skips that outcome returns a number that is "
             "biased low with nothing on the page to reveal it. There is no partial "
             "credit: either the identity holds or there is no estimator."),
            ("All the risk is in the weight",
             "A draw that misses the event contributes nothing whatever its weight; a "
             "draw that hits contributes its whole weight. So the variance is decided by "
             "how large the weight is on the outcomes that matter, and a `q` that makes "
             "the event rarer makes that weight enormous. The method can therefore be "
             "catastrophically worse than doing nothing, with no symptom except the "
             "variance figure."),
        ],
        "read_title": "Sample where the event is, then weight it back",
        "read_intro": "The identity that makes the reweighting legitimate, the condition it needs, and the three orders of magnitude between a good choice and a bad one.",
        "body": [
            ("p", "Direct simulation of a rare event is an arithmetic problem before it is "
                  "anything else. To see an event of probability `1/1024` even ten times "
                  "takes about ten thousand draws, and to estimate it to within ten per "
                  "cent takes on the order of a hundred thousand. Nine hundred and "
                  "ninety-nine draws in a thousand return a zero and teach nothing, and "
                  "the arithmetic gets worse in exact proportion as the event gets more "
                  "interesting."),
            ("def", ("Importance sampling",
                     "To estimate `E_p[h(X)]`, draw `X₁, …, Xₙ` from a different "
                     "distribution `q` and report the average of `h(Xᵢ)·p(Xᵢ)/q(Xᵢ)`. "
                     "The factor `p/q` is the <strong>likelihood ratio</strong> or "
                     "<strong>importance weight</strong>. `q` is the "
                     "<strong>proposal</strong>.")),
            ("thm", ("The reweighted estimator is unbiased",
                     "If `q(x) &gt; 0` whenever `p(x)h(x) ≠ 0`, then "
                     "`E_q[h(X)p(X)/q(X)] = E_p[h(X)]`. The estimator is therefore "
                     "unbiased for the same quantity as direct simulation, for every "
                     "proposal satisfying that condition and for no other.")),
            ("proof", ["`E_q[h·p/q] = Σ_x q(x)·h(x)p(x)/q(x)`, summed over the `x` with "
                       "`q(x) &gt; 0`.",
                       "The `q(x)` cancels, leaving `Σ h(x)p(x)` over those same `x`. By "
                       "the support condition every `x` with `h(x)p(x) ≠ 0` is among "
                       "them, so the sum is `Σ_x h(x)p(x) = E_p[h]`.",
                       "The cancellation is also the proof that the condition cannot be "
                       "relaxed: an `x` with `p(x)h(x) ≠ 0` and `q(x) = 0` is a term "
                       "present in the target sum and absent from the reweighted one, so "
                       "the estimator is short by exactly that term."]),
            ("h3", "The event, and the three proposals"),
            ("p", "The event on this page is ten fair coins all landing heads. Its "
                  "probability under `p` is exactly `1/1024`, which is what makes the "
                  "comparison a measurement rather than a demonstration: both estimators "
                  "are aiming at a number already known, so any difference between them "
                  "must be variance. Direct sampling has per-draw variance "
                  "`p(1 − p) = 1023/1048576`."),
            ("example", ("A coin weighted toward heads",
                         "Take `q` to be ten coins with `P(head) = 4/5`. Under `q` the "
                         "event has probability `1048576/9765625`, about `0.1074` &mdash; "
                         "roughly one draw in nine rather than one in a thousand &mdash; "
                         "and the weight on it is `9765625/1073741824`, about `0.0091`. "
                         "The per-draw variance becomes `8717049/1099511627776`, about "
                         "`0.0000079`, which is the original variance divided by "
                         "`32505856/264153 ≈ 123.0569`.")),
            ("example", ("The same coin, weighted the wrong way",
                         "Take `P(head) = 1/5` instead. The event now has probability "
                         "`1/9765625` under `q` &mdash; about a hundred times rarer than "
                         "it already was &mdash; and the weight on it is `9765625/1024`, "
                         "about `9537`. One draw in ten million contributes nine thousand "
                         "five hundred, and the per-draw variance is `1220703/131072`, "
                         "about `9.31`: the original variance multiplied by "
                         "`295928/31 ≈ 9546.0645`.")),
            ("math", ["  event: ten heads.   p = 1/1024 exactly.",
                      "",
                      "  proposal            q(event)          weight p/q       per-draw variance",
                      "  direct, P(H) = 1/2   1/1024            1                1023/1048576",
                      "  good,   P(H) = 4/5   ≈ 0.1073742       ≈ 0.0090949      ≈ 0.0000079281",
                      "  bad,    P(H) = 1/5   ≈ 0.0000001024    ≈ 9536.743       ≈ 9.313",
                      "",
                      "  good:  variance DIVIDED   by 32505856/264153 ≈ 123.0569",
                      "  bad:   variance MULTIPLIED by   295928/31    ≈ 9546.0645",
                      "",
                      "  same estimator, same unbiasedness, four orders of magnitude apart"]),
            ("h3", "What the runs look like, which is not what the variances look like"),
            ("p", "Two thousand draws under the good proposal hit the event two hundred and "
                  "fifteen times and estimate `0.00097771` against the exact `0.00097656`. "
                  "Two thousand draws under the fair coin hit it once and estimate "
                  "`1/2000 = 0.0005`. Two thousand draws under the bad proposal hit it "
                  "<em>not at all</em> and estimate exactly `0` &mdash; not near the "
                  "answer, at zero, with a perfectly ordinary-looking trace and nothing on "
                  "the page to suggest anything went wrong except the variance figure."),
            ("p", "That is the failure this lesson leads with. A bad proposal looks fine on "
                  "a short run because all of the damage is in the spread and none of it "
                  "is in the picture: the estimate is stable at zero, the running average "
                  "is a flat line, and the estimator is still unbiased. What is wrong is "
                  "that one draw in ten million would have carried the entire estimate, "
                  "and this run did not get it."),
            ("h3", "The proposal that is refused"),
            ("example", ("A perfectly good distribution that cannot be used",
                         "Take the good proposal and remove its mass on ten heads, "
                         "redistributing it over the other outcomes. The result is a "
                         "genuine probability distribution &mdash; its entries are "
                         "positive where they are present and they sum to `1` &mdash; and "
                         "the panel refuses it. `p` puts `1/1024` on the event and `q` "
                         "puts nothing there, so the likelihood ratio is undefined exactly "
                         "where the estimator needs it.")),
            ("p", "The refusal is the interesting behaviour. An implementation that skipped "
                  "the undefined outcome would return a number, and the number would be "
                  "biased low by precisely the term it dropped &mdash; which here is the "
                  "whole of the answer, so it would return zero, every time, with a "
                  "variance of zero to go with it. A confident, reproducible, perfectly "
                  "stable wrong answer is the worst thing a simulation can produce, and "
                  "the only defence is a support check that refuses rather than degrades."),
            ("p", "Note what the condition is not about. It is not about `q` being close to "
                  "`p`, and it is not about making the event common; those decide the "
                  "variance, which is a question of how good the estimator is. The support "
                  "condition decides whether there is an estimator, which is a prior "
                  "question with a yes-or-no answer."),
        ],
        "lab": ("simulate", {
            "mode": "importance",
            "preset": "good",
            "panel_title": "Choose the proposal, and read the variance column rather than the estimate",
            "panel_intro": "The event is ten fair coins all landing heads, a probability of "
                           "exactly `1/1024`, so both estimators are aiming at a number "
                           "already known and any difference between them is variance. "
                           "Read the `p/q` column of the first table and then the bar "
                           "chart. Switch to `P(head) = 1/5` and watch two thousand draws "
                           "return exactly zero with a flat, confident trace; then switch "
                           "to the proposal with the event removed and read the refusal.",
        }),
        "steps_title": "Estimating a rare event",
        "steps_intro": "Five steps, and the third is the one that separates a hard problem from an impossible report.",
        "steps": [
            ("Check whether direct simulation is affordable at all",
             "To see an event of probability `θ` about `m` times takes roughly `m/θ` "
             "draws. At `θ = 1/1024` and `m = 10` that is ten thousand; at `θ = 10⁻⁶` it "
             "is ten million, and the arithmetic decides the question before any "
             "cleverness is needed."),
            ("Choose a proposal that makes the event common, and write it down",
             "Tilting a parameter &mdash; a coin's bias, an arrival rate, a service time "
             "&mdash; is the usual move. The proposal has to be something you can both "
             "sample from and evaluate, because the weight needs `q(x)` for every drawn "
             "`x`."),
            ("Verify the support condition before anything else",
             "`q(x) > 0` wherever `p(x)h(x) ≠ 0`. This is a yes-or-no question about the "
             "two distributions and it is answered before a single draw is taken. A "
             "proposal that fails it is not a worse estimator; it is not an estimator."),
            ("Weight every draw by p/q, including the ones that miss",
             "A draw that misses the event contributes `0 × weight = 0`, and it still "
             "counts in the denominator. Averaging only the hits estimates a conditional "
             "expectation, which is a different and much larger number."),
            ("Compare the variances, not the estimates",
             "Both estimators are unbiased, so the estimates will be near each other when "
             "both are working and the comparison tells you nothing. The per-draw variance "
             "under `p` against the per-draw variance under `q` is the entire result, and "
             "a proposal whose ratio is below one has made the problem worse."),
        ],
        "worked": {
            "title": "Ten heads, three proposals, and one refusal",
            "intro": [
                "The event is ten fair coins all landing heads. Its probability is exactly "
                "`1/1024`, so nothing below is an approximation of an unknown: every "
                "figure is a fraction, and the two estimators are being compared on a "
                "quantity they both already agree about.",
            ],
            "lines": [
                "p, the fair coin      P(10 heads) = 1/1024",
                "                      per-draw variance p(1 − p) = 1023/1048576",
                "",
                "q, P(head) = 4/5      q(10 heads) = 1048576/9765625   ≈ 0.1073742",
                "                      weight p/q  = 9765625/1073741824 ≈ 0.0090949",
                "                      variance    = 8717049/1099511627776",
                "                                  ≈ 0.0000079281",
                "                      ratio p-variance / q-variance",
                "                                  = 32505856/264153 ≈ 123.0569",
                "",
                "q, P(head) = 1/5      q(10 heads) = 1/9765625        ≈ 0.0000001024",
                "                      weight p/q  = 9765625/1024     ≈ 9536.743",
                "                      variance    = 1220703/131072   ≈ 9.313",
                "                      MULTIPLIED by 295928/31        ≈ 9546.0645",
                "",
                "q, P(head) = 1/2      weight exactly 1, ratio exactly 1",
                "                      direct simulation written as importance sampling",
                "",
                "q = the good coin with its mass on ten heads removed      REFUSED",
                "",
                "two thousand draws each, same seed",
                "   good      215 hits    estimate 0.00097771    exact 0.00097656",
                "   fair        1 hit     estimate 0.0005",
                "   bad         0 hits    estimate 0",
            ],
            "after": [
                "The fair-coin row is worth keeping because it shows the method contains "
                "direct simulation as a special case: set `q = p`, every weight is exactly "
                "`1`, and the ratio of variances is exactly `1`. Importance sampling is "
                "not a different estimator, it is the same estimator with a parameter, and "
                "the parameter is the proposal.",
                "The bad row is the one to be frightened of. Its estimate is `0` and its "
                "trace is a flat line at zero, which is the most stable-looking output on "
                "the page, and the estimator is still unbiased: in expectation, over "
                "enough runs, those one-in-ten-million draws carrying a weight of nine "
                "thousand five hundred would bring the average back to `1/1024`. The "
                "expectation is right and no run will ever show it.",
                "For a faded rehearsal, drag the draw count from `2000` to `4000` under "
                "the bad proposal. The supplied first move is that the per-draw variance "
                "does not change at all &mdash; it is a property of `p`, `q` and the "
                "event, not of the run &mdash; so the variance of the average falls by "
                "exactly half. Say how many draws it would take for that average to have "
                "a standard error smaller than `1/1024` itself, and then say what that "
                "number means about the proposal.",
            ],
        },
        "quiz_title": "Weights, support and which column to read",
        "quiz": [
            {"q": "A proposal `q` makes the rare event ten times <em>rarer</em> than it was under `p`. What happens to the estimator?",
             "a": ["It becomes biased, since the event is under-represented",
                   "It stays unbiased, and its variance rises sharply",
                   "It stays unbiased, and its variance is unchanged",
                   "It fails the support condition and must be refused"],
             "c": 1,
             "why": "Unbiasedness needs only the support condition, which a rarer-but-"
                    "positive event satisfies. What changes is that the whole estimate now "
                    "rests on a huge weight attached to an outcome almost nothing draws, "
                    "which is exactly the measured case: the variance goes up by a factor "
                    "of about `9546`."},
            {"q": "A run of two thousand draws under a bad proposal returns exactly `0` with a perfectly flat trace. What does that indicate?",
             "a": ["A bug, since an unbiased estimator cannot return zero",
                   "That the event is impossible under `q`",
                   "That not one draw hit the event, which is what a huge variance looks like from inside a single run",
                   "That the run has converged to the answer"],
             "c": 2,
             "why": "Zero hits gives an estimate of exactly zero, and it is the "
                    "characteristic appearance of a high-variance importance sampler: all "
                    "of the damage is in the spread and none of it is in the picture. The "
                    "event is not impossible under this `q`, merely a hundred times rarer "
                    "than it already was."},
            {"q": "Why does the panel refuse a proposal that removes all mass from the event, even though it is a valid probability distribution?",
             "a": ["Because the weights would be too large to compute",
                   "Because `p/q` is undefined exactly where the event lives, so there is no unbiased estimator to run",
                   "Because the probabilities no longer sum to one",
                   "Because the event would then never be drawn, which would slow the run down"],
             "c": 1,
             "why": "The support condition fails at the one outcome that contributes. An "
                    "implementation that skipped it would return a number biased low by "
                    "exactly the term it dropped &mdash; here, by the whole answer &mdash; "
                    "with a variance of zero to make it look reliable. Refusing is the only "
                    "honest behaviour."},
            {"q": "Someone reports that oversampling the interesting region gave a much higher estimate of the event's probability. What has gone wrong?",
             "a": ["Nothing: sampling where the event is naturally finds it more often",
                   "The weights were not applied, so what was reported is the probability under `q` rather than under `p`",
                   "The proposal violated the support condition",
                   "The sample size was too small for the estimate to be reliable"],
             "c": 1,
             "why": "Without the factor `p/q` the average of the indicator estimates "
                    "`q(event)`, not `p(event)` &mdash; here about `0.107` instead of "
                    "`0.00098`, a hundred times too large. The reweighting is not an "
                    "optional refinement; it is the whole of what makes the draws relevant "
                    "to the original question."},
        ],
        "mistakes": [
            ("Oversampling the interesting region and forgetting to weight",
             "The result is an estimate of the probability under the proposal, reported as "
             "one under the target. On this page that is `0.107` in place of `0.00098`, "
             "and the run looks healthier than the correct one because the event keeps "
             "occurring. It is not an inaccurate estimate of the right thing; it is an "
             "accurate estimate of the wrong thing."),
            ("Judging a proposal by the estimate it produced",
             "Every valid proposal is unbiased for the same number, so the estimate cannot "
             "distinguish them. The good and the bad proposals here differ by four orders "
             "of magnitude in variance and both are aiming at `1/1024`. The variance "
             "column is the result and the estimate column is a formality."),
            ("Assuming importance sampling can only help",
             "It multiplied the variance by about `9546` on the measured bad proposal, "
             "from the same estimator with the same guarantees. Choosing `q` is a real "
             "decision with a real downside, and the only protection is to compute the two "
             "variances and divide rather than to trust that moving the sampling "
             "distribution toward the event was the right instinct."),
        ],
        "standard": ("Finish when the first thing you compute for a proposal is its variance, and the first thing you check is its support.",
                     "You should be able to derive the reweighting identity and see in the "
                     "derivation why the support condition cannot be relaxed, choose a "
                     "tilted proposal for a rare event and compute its likelihood ratios, "
                     "state the per-draw variance under both the target and the proposal "
                     "as exact fractions and divide them, recognise a zero-hit run as a "
                     "variance symptom rather than as convergence, and refuse a proposal "
                     "with a hole in its support rather than patching it."),
        "note": 'That is the whole of the method, and the last of these courses. Every other course here proves its answer: a tableau is optimal, a corner is whole, a schedule is best by an exchange argument, a steady state is the solution of a linear system. This one runs the model instead, and hands back an estimate with an interval around it &mdash; which is the honest report when nothing else is available, and never as good as a proof. Both hazards are still in force and they compound: the optimum of the wrong model is exactly, confidently, provably wrong, and here the output carries sampling noise on top of that, so a simulation of the wrong model is wrong in a way that more runs make look more convincing. The last thing to take from this path is the habit of asking what the model left out, and the second-to-last is the habit of printing the width beside the number.',
    },
]
