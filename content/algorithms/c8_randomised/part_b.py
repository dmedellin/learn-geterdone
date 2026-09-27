"""Randomised Algorithms, lessons 08-14 - the two kinds of guarantee, what
repetition buys, and four structures with the coin inside them."""

LESSONS = [
    # ---------------------------------------------------------------- 08
    {
        "slug": "kargers-contraction",
        "title": "Karger's Contraction",
        "module": "Two kinds of guarantee",
        "one_line": "Contract random edges until two vertices remain, compute the exact success probability by recursion over contraction states, and list the seeds that failed.",
        "summary": (
            "Pick a uniformly random edge, merge its endpoints, drop the loops, repeat until "
            "two supernodes remain, and report the edges between them. On the lab's opening "
            "graph that returns a minimum cut with probability `19/35`, which is exact and is "
            "not a sample; the proved bound is `2/(n(n − 1)) = 1/15`; and 53 of the first 120 "
            "seeds returned something bigger. All three numbers belong on the page and only "
            "one of them is a guarantee."
        ),
        "key": [
            "contract a uniformly random edge, drop loops, stop at two supernodes",
            "P(a given minimum cut survives) ≥ 2/(n(n − 1))       WITH HIGH PROBABILITY",
            "the lab's graph: minimum cut 2 edges, and three cuts of that size",
            "13/70 + 6/35 + 13/70 = 19/35        the probability of returning SOME one",
            "measured over 120 seeds: 67/120, and 53 seeds missed",
            "the bound is about ONE named cut; success is about ANY of them",
        ],
        "key_label": "One contraction, three cuts, and the difference between a bound and a rate",
        "concepts_intro": (
            "The hard idea is why a random edge is likely to miss a small cut. The other two "
            "are what the bound is about and what the algorithm is about, which are not the "
            "same event."
        ),
        "concepts": [
            ("Contraction cannot shrink the minimum cut, only lose sight of it",
             "Merging the endpoints of an edge produces a multigraph whose cuts are exactly the "
             "cuts of the original that keep those two vertices together. So every cut of the "
             "contracted graph is a cut of the original with the same size, and the minimum can "
             "only rise. A particular minimum cut survives as long as no edge crossing it is ever "
             "contracted &mdash; which is the only event the analysis has to track."),
            ("A small cut is unlikely to be hit, and multiplicity is why",
             "If the minimum cut has `k` edges then every vertex has degree at least `k`, so a "
             "graph on `n` vertices has at least `nk/2` edges. A uniformly random edge therefore "
             "crosses a given minimum cut with probability at most `k/(nk/2) = 2/n`. Parallel "
             "edges are counted separately and that is the whole point: a pair of supernodes joined "
             "by many edges is likely to be merged, and merging them is harmless."),
            ("The bound is about one cut; success is about any of them",
             "`kargerExact` answers &ldquo;what is the probability this named cut survives?&rdquo; "
             "The algorithm succeeds if it returns <em>any</em> minimum cut, and the lab's opening "
             "graph has three. Their probabilities are `13/70`, `6/35` and `13/70`, and the "
             "success probability is their sum, `19/35`. Reporting the first of those as the "
             "success probability would understate it by a factor of nearly three, silently."),
        ],
        "read_title": "A cut found by destroying the graph",
        "read_intro": "The algorithm, the bound, the exact probability the lab computes instead, and the seeds where it did not work.",
        "body": [
            ("def", ("Contraction, and the algorithm",
                     "To <strong>contract</strong> an edge `uv` of a multigraph, replace `u` and "
                     "`v` by a single supernode, redirect every other edge at `u` or `v` to it, and "
                     "delete the edges that have become loops. Parallel edges are kept. "
                     "<strong>Karger's algorithm</strong> repeatedly contracts a uniformly random "
                     "edge until two supernodes remain, and returns the set of edges between them, "
                     "which is a cut of the original graph.")),
            ("p", "The algorithm always returns a cut &mdash; the two supernodes are a bipartition "
                  "of the vertices, and the surviving edges are exactly the edges crossing it. What "
                  "it does not always return is a <em>minimum</em> cut, and that is the only thing "
                  "that can go wrong. This is a Monte Carlo algorithm: the running time is fixed "
                  "and the answer is sometimes wrong."),
            ("thm", ("The survival bound",
                     "Fix a minimum cut `C` of a connected graph on `n` vertices. Karger's "
                     "algorithm returns `C` with probability at least `2/(n(n − 1))`.")),
            ("proof", ("Let `k = |C|`. Every vertex has degree at least `k`, or else the edges at a "
                       "vertex of smaller degree would be a smaller cut, so the number of edges is "
                       "at least `nk/2`. A uniformly random edge is one of the `k` in `C` with "
                       "probability at most `k/(nk/2) = 2/n`, so the first contraction misses `C` "
                       "with probability at least `1 − 2/n`.",
                       "If `C` was missed, the contracted graph has `n − 1` vertices and `C` is "
                       "still a cut of it, still of size `k`, and still minimum &mdash; contraction "
                       "cannot create a smaller cut. So the same bound applies with `n − 1` in "
                       "place of `n`, and inductively the probability that all `n − 2` "
                       "contractions miss `C` is at least the product of `1 − 2/i` for `i` from "
                       "`n` down to `3`.",
                       "That product is `((n−2)/n)·((n−3)/(n−1))·…·(1/3)`, which telescopes to "
                       "`2/(n(n − 1))`. And if no edge of `C` was ever contracted, then every "
                       "supernode lies wholly on one side of `C`, so the two surviving supernodes "
                       "are exactly the two sides and the algorithm returns `C`.")),
            ("p", "At `n = 6` the bound reads `2/30 = 1/15`, about `0.067`. That is a guarantee for "
                  "every graph on six vertices and every minimum cut in it, and it is very far from "
                  "what happens on any particular graph &mdash; which is what the rest of this page "
                  "is about."),
            ("h3", "What the lab computes instead of the bound"),
            ("p", "The panel does not sample and it does not quote the bound as the answer. For a "
                  "named cut it computes the exact probability by recursion over "
                  "<strong>contraction states</strong>: a state is the current partition of the "
                  "vertices into supernodes, and the probability of success from a state is the sum "
                  "over pairs of supernodes that do not straddle the cut of `multiplicity/m` times "
                  "the probability of success from the merged state. Different contraction orders "
                  "reach the same state, so the recursion is memoised and the whole computation is "
                  "a few dozen states rather than `|E|!` edge orders."),
            ("p", "Then it enumerates every bipartition to find <em>all</em> the minimum cuts, and "
                  "adds their probabilities. That second step is not optional: the algorithm "
                  "succeeds if it returns any of them, and on graphs with symmetry there are "
                  "several."),
            ("example", ("Two triangles joined by two edges",
                         "The opening graph is `1-2, 1-3, 2-3, 4-5, 4-6, 5-6, 1-4, 2-5`: six "
                         "vertices, eight edges. Exhaustive search over all 31 bipartitions finds a "
                         "minimum cut of 2 edges, and three cuts achieve it &mdash; isolating "
                         "vertex 3, isolating vertex 6, and splitting the two triangles apart. "
                         "Their exact probabilities are `13/70`, `13/70` and `6/35`, and the "
                         "probability of returning one of the three is `19/35 ≈ 0.5429`. Every one "
                         "of them clears the bound `1/15`.")),
            ("p", "Notice that the cut the graph was built to illustrate &mdash; the pair of "
                  "joining edges &mdash; is the <em>least</em> likely of the three, at `6/35` "
                  "against `13/70`. The two cuts that isolate a single vertex are easier to find, "
                  "because each is protected by only two edges out of eight rather than by two "
                  "edges that the contraction of a triangle keeps threatening."),
            ("h3", "The measured rate, and the seeds that missed"),
            ("p", "Over seeds 1 to 120 the algorithm returned a minimum cut 67 times: a rate of "
                  "`67/120 ≈ 0.5583`, against an exact probability of `19/35 ≈ 0.5429`. The "
                  "measurement is above the truth here and will be below it at another slider "
                  "position, and it is a measurement either way. Move the seed count and watch it "
                  "wander around a number that does not move."),
            ("p", "Fifty-three of those 120 seeds failed, and the panel names them rather than "
                  "reporting a rate and stopping. Seed 5 is the first: it returned a cut of 3 edges "
                  "rather than 2. That is what <strong>with high probability</strong> means, and it "
                  "is the reason the phrase is on the page in those words. A guarantee whose "
                  "failures you have never seen is one you will eventually quote as though it were "
                  "an always claim."),
            ("p", "For contrast, switch the graph to a four-cycle. It has six minimum cuts, each of "
                  "exactly two edges, each with probability exactly `1/6` &mdash; which is exactly "
                  "the bound `2/(n(n − 1))` at `n = 4` &mdash; and they sum to `1`. The algorithm "
                  "never fails on that graph, and 120 of 120 seeds succeeded. A graph where the "
                  "bound is tight for every cut and the algorithm is nevertheless certain to "
                  "succeed is worth a minute's thought: the bound is per cut, and there are six of "
                  "them."),
        ],
        "lab": ("random", {"mode": "karger", "preset": "barbell"}),
        "steps_title": "Reading a Monte Carlo guarantee",
        "steps_intro": "Separate the event the bound covers from the event the algorithm is judged on.",
        "steps": [
            ("Find all the minimum cuts before asking about probability",
             "The panel enumerates every bipartition. If there are three minimum cuts then success "
             "is a union of three events and the success probability is their sum; quoting one "
             "cut's probability as the algorithm's is the commonest error here, and it always "
             "understates."),
            ("Read the bound as a floor for every graph, not a prediction for this one",
             "`1/15` at six vertices against an actual `19/35`: the bound is out by a factor of "
             "eight on this graph. It is not wrong. It is a statement about the worst graph on six "
             "vertices, and this one is not that graph."),
            ("Go and look at a failure",
             "The panel lists the seeds that returned a bigger cut and says what they returned "
             "instead. Do that before writing down the success rate; a probabilistic guarantee is "
             "not understood until its failure mode has been seen once."),
            ("Watch the measured rate move and the exact one stay",
             "Change the seed slider. The rate moves, the exact probability does not, and the "
             "distance between them at any slider position is a sample's noise rather than "
             "information about the algorithm."),
        ],
        "worked": {
            "title": "Every minimum cut of the opening graph, with its exact probability",
            "intro": [
                "`1-2, 1-3, 2-3, 4-5, 4-6, 5-6, 1-4, 2-5`. Two triangles, `{1, 2, 3}` and "
                "`{4, 5, 6}`, joined by `1-4` and `2-5`. Exhaustive search over the 31 "
                "bipartitions, then the exact probability of each minimum cut.",
            ],
            "lines": [
                "cut                       edges cut   exact P(returned)   against 1/15",
                " {3} | {1,2,4,5,6}            2           13/70 = 0.1857   at or above",
                " {1,2,3} | {4,5,6}            2            6/35 = 0.1714   at or above",
                " {6} | {1,2,3,4,5}            2           13/70 = 0.1857   at or above",
                "                                        -----",
                " any of the three                        19/35 = 0.5429",
                "",
                " the bound  2/(n(n-1)) = 2/30 = 1/15 = 0.0667",
                " exhaustive minimum cut, by brute force over bipartitions: 2 edges",
                "",
                "MEASURED over seeds 1..120",
                " returned a minimum cut   67 of 120 = 0.5583",
                " missed                   53 of 120",
                " first miss: seed 5 returned a cut of 3 edges",
                "",
                "REPETITION, exactly",
                " 1 run   0.542857      2 runs  0.791020",
                " 5 runs  0.980035      6 runs  0.990873   <- first to reach 99/100",
            ],
            "after": [
                "`13/70 + 6/35 + 13/70`: put the middle term over 70 as `12/70` and the sum is "
                "`38/70 = 19/35`. Doing that addition by hand once is worth more than reading the "
                "total, because it is the step that distinguishes the algorithm's success event "
                "from any one cut's survival.",
                "The bound of `1/15` is below every one of the three per-cut probabilities, which "
                "is what it means for the bound to hold. It is also about eight times below the "
                "algorithm's actual success probability, and the gap is not a defect in the proof "
                "&mdash; the proof has to cover the worst graph on six vertices, and no graph is "
                "the worst case for every `n` at once.",
                "For a faded rehearsal, switch to the graph with a parallel pair and predict the "
                "number of minimum cuts before reading it. The supplied first move is this: two "
                "edges written between the same pair of vertices make that pair twice as likely to "
                "be contracted, and contracting them is harmless, so parallel edges help. Say what "
                "the minimum cut size is, how many cuts achieve it, and whether the success "
                "probability should be above or below `19/35` &mdash; then check all three.",
            ],
        },
        "quiz_title": "Cuts, bounds, and rates",
        "quiz": [
            {"q": "The panel shows three minimum cuts with probabilities `13/70`, `6/35` and `13/70`, and a success probability of `19/35`. Why is the last one the sum?",
             "a": ["Because the three events are independent",
                   "Because the algorithm succeeds if it returns any of them, and the three outcomes are mutually exclusive",
                   "Because the bound is additive",
                   "It is a coincidence of this graph"],
             "c": 1,
             "why": "One run returns exactly one cut, so returning cut A and returning cut B are "
                    "disjoint events, and the probability of their union is the sum. Independence "
                    "is not involved and would be the wrong property to look for. Reporting only "
                    "`13/70` as the success probability would understate it by nearly three times."},
            {"q": "The bound is `1/15` and the exact success probability is `19/35`. What does that show?",
             "a": ["The bound is wrong for this graph",
                   "The exact computation must be wrong, since it exceeds the bound",
                   "The bound is a floor that must cover the worst graph on six vertices, and this graph is easier than that",
                   "The bound applies only to graphs with a unique minimum cut"],
             "c": 2,
             "why": "`2/(n(n−1))` is a lower bound on the survival probability of one named cut, "
                    "over all graphs on `n` vertices. Clearing it by a factor of eight is the bound "
                    "working. Exceeding a lower bound is not a contradiction, and the panel checks "
                    "that each per-cut probability is at or above it."},
            {"q": "Fifty-three of the first 120 seeds returned a cut of 3 edges rather than 2. What does that establish?",
             "a": ["A defect in the implementation",
                   "That the algorithm is Monte Carlo: the running time is fixed and the answer is sometimes wrong",
                   "That the exact probability `19/35` is too high",
                   "That 120 seeds is too small a sample"],
             "c": 1,
             "why": "Failing on about 46 per cent of runs is exactly what a success probability of "
                    "`19/35` predicts, and it is why the guarantee is labelled with high "
                    "probability rather than always. The panel lists the failing seeds "
                    "deliberately, because a probabilistic guarantee with no visible failure gets "
                    "read as a certainty."},
            {"q": "Why does the exact computation recurse over contraction states rather than over edge orders?",
             "a": ["Edge orders would give a different answer",
                   "Because the algorithm's future depends only on the current partition, so many orders share one state and the recursion can be memoised",
                   "Because edge orders cannot be enumerated for any graph",
                   "Because the state recursion is an approximation that is accurate enough"],
             "c": 1,
             "why": "Two different orders that reach the same partition of the vertices have the "
                    "same future, so the state is the right thing to index by, and memoising it "
                    "turns `|E|!` orders into a few dozen states. Both routes give the same exact "
                    "rational — the repository's arithmetic check enumerates edge orders to confirm "
                    "it — and neither is a sample."},
        ],
        "mistakes": [
            ("Quoting one cut's survival probability as the algorithm's success probability",
             "On the opening graph those are `6/35` and `19/35`. The first answers &ldquo;does this "
             "particular cut come back?&rdquo; and the second answers &ldquo;does a minimum cut "
             "come back?&rdquo; The panel prints every minimum cut in its own row and the union in "
             "bold precisely because the two questions are easy to conflate and the answers differ "
             "by a factor of three."),
            ("Folding parallel edges into one",
             "A representation that stored `1-2` once instead of twice would change the "
             "probability that pair is contracted, and that probability is the entire mechanism by "
             "which contraction favours small cuts. The lab's parser keeps repeated edges as "
             "repeated edges, and the multiplicity appears explicitly in the recursion's weights."),
            ("Reading a with-high-probability bound as an always bound",
             "It is an easy slip when the measured rate is `0.56` and the page is about a "
             "correctness guarantee. Fifty-three of 120 seeds returned the wrong answer. The fix is "
             "not a better bound; it is repetition, and the next lesson prices it."),
        ],
        "standard": ("Finish when you can prove the survival bound and say which event it is about.",
                     "You should be able to run one contraction by hand, state and prove "
                     "`2/(n(n − 1))` from the minimum-degree argument, explain why the success "
                     "probability is the sum over all minimum cuts, and produce a run where the "
                     "algorithm failed."),
        "note": ("A success probability of `19/35` is not usable on its own, and the algorithm was "
                 "never meant to be run once. &ldquo;Repetition, and the Probability It "
                 "Buys&rdquo; takes the worst graph the lab offers &mdash; a unique minimum cut "
                 "with probability `13/35` &mdash; and computes exactly how many independent runs "
                 "reach a stated target."),
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "repetition-and-the-probability-it-buys",
        "title": "Repetition, and the Probability It Buys",
        "module": "Two kinds of guarantee",
        "one_line": "Run a one-sided algorithm t times, keep the best answer, and compute the smallest t that reaches a stated target exactly.",
        "summary": (
            "An algorithm that is right with probability `p` and, when it is wrong, is "
            "detectably no better, becomes an algorithm that is right with probability "
            "`1 − (1 − p)ᵗ` after `t` independent runs. On the lab's bridge graph `p = 13/35`, "
            "so five runs reach `9/10` and ten reach `99/100`. The panel finds the smallest "
            "`t` by multiplying rather than by taking a logarithm, so the answer is an exact "
            "integer and the probability beside it is an exact fraction."
        ),
        "key": [
            "t independent runs all fail with probability (1 − p)ᵗ",
            "so P(at least one succeeds) = 1 − (1 − p)ᵗ",
            "p = 13/35 on the bridge graph: one run, and 79 of 120 seeds missed",
            "t = 5 reaches 0.901876, t = 10 reaches 0.990372",
            "smallest t for 99/100: ten runs — found by multiplying, not by a logarithm",
            "keeping the best of t answers needs the error to be ONE-SIDED",
        ],
        "key_label": "One inequality, the exact amplification, and the hypothesis it needs",
        "concepts_intro": (
            "The hard idea is the hypothesis: repetition only helps when you can tell a better "
            "answer from a worse one. The other two are the arithmetic and how the smallest "
            "`t` is found."
        ),
        "concepts": [
            ("Independent failures multiply",
             "Run the algorithm `t` times with independent randomness and keep the smallest cut any "
             "run returned. The kept answer is wrong only if <em>every</em> run was wrong, and the "
             "runs are independent, so that has probability `(1 − p)ᵗ`. On the bridge graph "
             "`p = 13/35`, so `1 − p = 22/35` and ten runs fail with probability "
             "`(22/35)¹⁰ ≈ 0.0096`. The panel computes that as an exact fraction rather than as a "
             "decimal."),
            ("The error must be one-sided for this to work at all",
             "Karger's algorithm never returns a cut smaller than the minimum, because everything "
             "it returns is a genuine cut. So a run that returns 2 edges is definitely at least as "
             "good as a run that returns 3, and taking the best of `t` answers cannot be fooled. If "
             "an algorithm could err in both directions, the best of `t` answers would be the most "
             "extreme error rather than the best answer, and amplification would make things "
             "worse."),
            ("The smallest t is found by multiplying, not by a logarithm",
             "`t ≥ ln(1/δ)/p` is the familiar estimate, and it is an estimate: it involves "
             "logarithms of quantities that are not exact and it rounds. The panel instead "
             "multiplies `1 − p` by itself until the product drops below `1 − target`, counting the "
             "steps. The answer is the exact least `t`, and the routine refuses rather than looping "
             "if `p` is zero."),
        ],
        "read_title": "Turning a coin-flip into a guarantee",
        "read_intro": "The amplification identity, the graph where one run is worst, and the exact cost of each target.",
        "body": [
            ("p", "The lab's hardest graph is two triangles joined by a single edge: "
                  "`1-2, 1-3, 2-3, 4-5, 4-6, 5-6, 3-4`. Seven edges, six vertices, and a unique "
                  "minimum cut of one edge &mdash; the bridge `3-4`. There is exactly one way to "
                  "succeed and the single edge has to survive all four contractions, which it does "
                  "with probability `13/35 ≈ 0.3714`. Over seeds 1 to 120 the algorithm succeeded "
                  "41 times and missed 79, the first miss being seed 1, which returned a cut of two "
                  "edges."),
            ("p", "One run at `0.37` is not an algorithm anybody would use. The question this page "
                  "answers is what it costs to turn it into one, and the answer is exact."),
            ("thm", ("Amplification",
                     "Let one run of a Monte Carlo algorithm return a correct answer with "
                     "probability at least `p`, and suppose a wrong answer is never better than a "
                     "correct one, so that keeping the best of several runs keeps a correct answer "
                     "if any run produced one. Then `t` independent runs return a correct answer "
                     "with probability at least `1 − (1 − p)ᵗ`.")),
            ("proof", ("Let `Aᵢ` be the event that run `i` returns a correct answer, so "
                       "`P(Aᵢ) ≥ p`. The kept answer is incorrect only if every run was incorrect, "
                       "which is the intersection of the complements.",
                       "The runs use independent randomness, so those complements are independent "
                       "and `P(no run correct) = Π P(not Aᵢ) ≤ (1 − p)ᵗ`. The kept answer is "
                       "therefore correct with probability at least `1 − (1 − p)ᵗ`.",
                       "The hypothesis about wrong answers is where the &ldquo;keep the best&rdquo; "
                       "step is discharged: without it, knowing that some run was correct does not "
                       "tell you that the answer you kept is.")),
            ("p", "On the bridge graph that gives `1 − (22/35)ᵗ`. The panel prints it at several "
                  "values of `t` as exact fractions with decimals beside them, and the growth is "
                  "the one to internalise: each extra run multiplies the failure probability by "
                  "`22/35`, so failure decays geometrically while the work grows linearly."),
            ("math", [
                "  t     P(at least one run succeeds)      P(all t fail)",
                "  1     13/35            = 0.371429       0.628571",
                "  2     741/1225         = 0.604898       0.395102",
                "  5     0.901876                          0.098124",
                " 10     0.990372                          0.009628",
                "",
                "  smallest t reaching  9/10   :  5",
                "  smallest t reaching 99/100  : 10",
                "  smallest t reaching 999/1000: 15",
            ]),
            ("h3", "The same arithmetic on an easier graph"),
            ("p", "Switch to the two triangles joined by two edges, where one run succeeds with "
                  "probability `19/35`. Now three runs reach `9/10`, six reach `99/100` and nine "
                  "reach `999/1000`. Compare with the bridge graph's 5, 10 and 15. The success "
                  "probability changed by less than a factor of two and the cost of a given target "
                  "changed by about the same factor, which is what a geometric decay predicts: "
                  "halving `p` roughly doubles the runs needed."),
            ("p", "And on the four-cycle one run succeeds with probability `1`, so the smallest `t` "
                  "for every target is `1`, and the panel prints `1` rather than a logarithm's "
                  "rounded suggestion. That is the case where the general formula would still work "
                  "and would be an odd thing to quote."),
            ("h3", "What repetition does not buy"),
            ("p", "It does not make the algorithm always correct. `1 − (22/35)¹⁵` is about "
                  "`0.9991`, which is not `1`, and no finite `t` reaches `1`. The panel's target "
                  "menu offers `9/10`, `99/100` and `999/1000` rather than certainty for that "
                  "reason. If you need certainty you need a different algorithm; what repetition "
                  "buys is a failure probability you choose, at a cost you can compute."),
            ("p", "It also does not help if the runs share randomness. Independence is a hypothesis "
                  "of the theorem, and it is the hypothesis that a real implementation is most "
                  "likely to break &mdash; by reusing a seed, by deriving all `t` seeds from one in "
                  "a way that correlates them, or by drawing from a generator whose low bits are a "
                  "short cycle. The generator behind every lab on this course is a prime-modulus "
                  "stream with a mixed seed for exactly that reason."),
            ("p", "And it does not turn a one-sided guarantee into a two-sided one. Everything "
                  "above rested on being able to prefer one answer to another. The next lesson's "
                  "algorithm has the same structure from a different direction: a primality test "
                  "whose positive findings are proofs and whose negative findings are silence, so "
                  "that repeating it accumulates evidence in one direction only."),
        ],
        "lab": ("random", {"mode": "karger", "preset": "bridge"}),
        "steps_title": "Pricing a target failure probability",
        "steps_intro": "Establish one run's probability first; everything after it is one multiplication per run.",
        "steps": [
            ("Check that the error is one-sided",
             "Can you tell a better answer from a worse one without knowing the truth? For a "
             "minimum cut, yes: fewer edges is better and nothing returned is ever below the "
             "minimum. If not, keeping the best of `t` runs is keeping the most extreme error."),
            ("Get one run's success probability, exactly if you can",
             "The panel computes it by recursion over contraction states. Where you cannot compute "
             "it, use the proved bound &mdash; and then the `t` you derive is a bound on the runs "
             "needed rather than the exact number."),
            ("Multiply, do not take a logarithm",
             "`(1 − p)` times itself, counting steps until it falls under `1 − target`. This gives "
             "the least `t` exactly. The logarithmic formula is a fine estimate and it rounds in an "
             "unstated direction, which matters when `t` is small."),
            ("State the failure probability you have bought",
             "Ten runs on the bridge graph leave a failure probability of about `0.0096`, not "
             "zero. Write that number down next to the answer; it is the part of the guarantee that "
             "is easiest to drop and the only part that is a risk."),
        ],
        "worked": {
            "title": "Ten runs on the bridge graph",
            "intro": [
                "`1-2, 1-3, 2-3, 4-5, 4-6, 5-6, 3-4`. A unique minimum cut of one edge, the bridge "
                "`3-4`, which must survive four contractions. One run succeeds with probability "
                "`13/35`.",
            ],
            "lines": [
                "one run              P(success) = 13/35 = 0.371429",
                "                     P(failure) = 22/35 = 0.628571",
                "",
                " t    (22/35)^t              1 - (22/35)^t",
                " 1    0.628571               0.371429",
                " 2    0.395102               0.604898      = 741/1225 exactly",
                " 3    0.248350               0.751650",
                " 4    0.156106               0.843894",
                " 5    0.098124               0.901876      first past 9/10",
                " 6    0.061678               0.938322",
                " 8    0.024369               0.975631",
                "10    0.009628               0.990372      first past 99/100",
                "14    0.001503               0.998497      one short of 999/1000",
                "15    0.000945               0.999055      first past 999/1000",
                "",
                "MEASURED, one run each, seeds 1..120",
                "  succeeded 41 of 120 = 41/120 = 0.341667",
                "  missed    79 of 120,  first miss seed 1, which returned 2 edges",
            ],
            "after": [
                "The measured rate `41/120 ≈ 0.342` sits below the exact `13/35 ≈ 0.371`. At the "
                "previous lesson's graph the measured rate sat above the exact one. Both are "
                "ordinary, and the pair of observations is the cheapest available demonstration "
                "that a measured rate is not an estimate of the truth in any sense you can act on "
                "at 120 samples.",
                "Ten runs of an algorithm that is wrong 63 per cent of the time give an answer that "
                "is wrong less than one per cent of the time. Nothing about the algorithm improved; "
                "the failure probability was multiplied by `22/35` ten times. That is the whole "
                "trade, and it is why a Monte Carlo algorithm with a constant success probability "
                "is a useful object even when the constant is small.",
                "For a faded rehearsal, set the target to `999/1000` and predict the smallest `t` "
                "on the two-triangles-joined-by-two-edges graph before switching to it. The "
                "supplied first move is this: there `p = 19/35`, so `1 − p = 16/35 ≈ 0.457`, and "
                "each run multiplies the failure probability by that. Estimate how many runs take "
                "`0.457ᵗ` below `0.001`, then check the exact answer &mdash; and then say why the "
                "bridge graph needs 15 for the same target.",
            ],
        },
        "quiz_title": "Amplification and its hypothesis",
        "quiz": [
            {"q": "One run succeeds with probability `13/35`. What is the probability that at least one of ten independent runs succeeds?",
             "a": ["`10 × 13/35`, which exceeds one and is therefore certain",
                   "`1 − (22/35)¹⁰ ≈ 0.9904`",
                   "`(13/35)¹⁰`",
                   "`13/35`, since the runs are identical"],
             "c": 1,
             "why": "All ten fail only if each fails, which has probability `(22/35)¹⁰` by "
                    "independence, so at least one succeeds with probability `1 − (22/35)¹⁰`. "
                    "Multiplying a probability by ten is not a probability, and `(13/35)¹⁰` is the "
                    "chance that all ten succeed."},
            {"q": "Which hypothesis makes “keep the best of `t` runs” work?",
             "a": ["The runs are identically distributed",
                   "The error is one-sided: a wrong answer is never better than a correct one, so the best answer kept is correct if any run was",
                   "`p` is at least a half",
                   "The algorithm is Las Vegas rather than Monte Carlo"],
             "c": 1,
             "why": "Karger's algorithm always returns a genuine cut, so it never returns fewer "
                    "edges than the minimum and fewer is always better. Without that, the best of "
                    "`t` answers would be the most extreme error. `p` may be arbitrarily small and "
                    "amplification still works — it just costs more runs."},
            {"q": "The panel reports the smallest `t` reaching `99/100` as 10 for the bridge graph and 6 for the two-triangles graph. Where do those come from?",
             "a": ["From `ln(1/δ)/p`, rounded up",
                   "From multiplying `1 − p` by itself and counting the steps until the product falls below `1 − target`",
                   "From the 120 measured seeds",
                   "From the bound `2/(n(n − 1))`"],
             "c": 1,
             "why": "The routine multiplies exactly and counts, so the answer is the exact least "
                    "`t` rather than a rounded estimate. The logarithmic formula is an "
                    "approximation and rounds in an unstated direction, which matters most when "
                    "`t` is small — which is exactly the regime these graphs are in."},
            {"q": "What does repetition NOT provide?",
             "a": ["A failure probability you choose",
                   "A cost you can compute in advance",
                   "Certainty: no finite `t` makes the failure probability zero",
                   "Protection against a run that returns a non-minimum cut"],
             "c": 2,
             "why": "`1 − (1 − p)ᵗ` is below one for every finite `t` and every `p < 1`. The "
                    "panel's targets are `9/10`, `99/100` and `999/1000` for that reason. What "
                    "repetition gives is a failure probability you pick and a number of runs that "
                    "achieves it, both exactly."},
        ],
        "mistakes": [
            ("Adding the success probabilities of the runs",
             "`10 × 13/35` is greater than three, which is not a probability. Failures multiply "
             "and successes do not add, and the identity to remember is the one about the "
             "complement: all `t` fail with probability `(1 − p)ᵗ`. The panel prints that column "
             "beside the success column so the two are never confused."),
            ("Amplifying an algorithm whose error is two-sided",
             "If a run can report a value that is too small as well as too large, the best of `t` "
             "runs is the largest error rather than the best answer, and repetition makes the "
             "output worse. Check that a wrong answer is detectably no better than a right one "
             "before running anything twice."),
            ("Deriving t from a logarithm and not checking it",
             "`ln(100)/p` at `p = 13/35` gives about `12.4`, suggesting 13 runs where 10 suffice. "
             "The estimate is in the right place and it is not the answer, and at these sizes the "
             "difference is 30 per cent of the work. The exact least `t` costs `t` multiplications "
             "to find."),
        ],
        "standard": ("Finish when you can price a target failure probability exactly, and say what the pricing assumes.",
                     "You should be able to derive `1 − (1 − p)ᵗ`, name the one-sided-error "
                     "hypothesis that licenses keeping the best run, find the smallest `t` for a "
                     "target by multiplying, and state the residual failure probability you have "
                     "bought rather than implying certainty."),
        "note": ("Independence between runs is the hypothesis a real implementation breaks, usually "
                 "by deriving every seed from one in a way that correlates them. Every lab on this "
                 "course draws from a prime-modulus stream with a mixed seed, because under the "
                 "power-of-two modulus used elsewhere in this library the low bits repeat on a "
                 "short cycle and a page whose whole claim is about independent runs would have "
                 "been demonstrating the opposite."),
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "witnesses-liars-and-one-sided-error",
        "title": "Witnesses, Liars, and One-Sided Error",
        "module": "Two kinds of guarantee",
        "one_line": "Test a number for primality with a base that can prove compositeness and can never prove primality, and look at the bases that prove nothing.",
        "summary": (
            "The strong test asks one question of one base and either proves the number "
            "composite or says nothing at all. For 561 &mdash; a Carmichael number &mdash; "
            "550 of the 558 usable bases prove compositeness and 8 do not; the Fermat test, on "
            "the same number, catches none of the 318 coprime bases. The error is one-sided, "
            "so `t` independent bases leave an error of `(liars/bases)ᵗ`, which is "
            "`1024/1690522737399` at `t = 5` against a bound of `1/1024`."
        ),
        "key": [
            "write n − 1 = d·2ˢ with d odd; the chain is aᵈ, then repeated squaring",
            "if the chain never reaches 1 or n − 1 then a is a WITNESS and n is composite",
            "a witness is a PROOF; no base ever proves primality",
            "561: 550 of 558 bases are witnesses = 275/279; 8 are not",
            "561 is Carmichael: 0 of its 318 coprime bases defeat Fermat's test",
            "exact error after 5 bases: 1024/1690522737399, against the bound 1/1024",
        ],
        "key_label": "One chain, one verdict, and the quarter of bases the bound allows for",
        "concepts_intro": (
            "The hard idea is the asymmetry: one verdict is a proof and the other is silence. "
            "The other two are the certificate that makes it a proof and the Carmichael numbers "
            "that show why the weaker test is not enough."
        ),
        "concepts": [
            ("One verdict is a proof, the other is silence",
             "If the squaring chain from `aᵈ` never reaches `1` or `n − 1`, then `n` is composite "
             "&mdash; not probably composite, composite, with a certificate. If it does reach one "
             "of them, nothing follows: `n` may be prime, or `a` may be one of the bases that "
             "happens to be fooled. So repeating the test accumulates evidence in exactly one "
             "direction, and a thousand silent bases never add up to a proof of primality."),
            ("The certificate is a nontrivial square root of one",
             "Modulo a prime, the only solutions of `x² = 1` are `1` and `−1`. So if the chain "
             "produces some `x` that is neither `1` nor `n − 1` and whose square is `1`, then `n` "
             "cannot be prime, and `gcd(x − 1, n)` is a proper factor. At `n = 341` with `a = 2` "
             "the chain is `32, 1`: `32² = 1024 = 3·341 + 1`, so `32` is a nontrivial square root "
             "of one and `gcd(31, 341) = 31` is a factor. The panel prints that row when it exists."),
            ("The bases that prove nothing are the whole content of the bound",
             "&ldquo;At least three quarters of the bases are witnesses&rdquo; has content only "
             "because the other quarter exists. For 561 the strong liars are `50, 101, 103, 256, "
             "305, 458, 460, 511` &mdash; eight of 558, so the test clears the bound with enormous "
             "room. A single run with base 50 reports nothing, and a reader who stopped there would "
             "call 561 prime."),
        ],
        "read_title": "A test that proves one thing and suggests the other",
        "read_intro": "The chain, the certificate, the exact witness fraction, the Carmichael numbers that break the weaker test, and the error after t bases.",
        "body": [
            ("def", ("The strong test on one base",
                     "Let `n` be odd and at least `5`, and write `n − 1 = d·2ˢ` with `d` odd. For a "
                     "base `a` in `2..n − 2`, compute `x₀ = aᵈ mod n` and then `xᵢ₊₁ = xᵢ² mod n` "
                     "for `i` up to `s − 1`. If `x₀ = 1` or some `xᵢ = n − 1`, the base is "
                     "<strong>inconclusive</strong>. Otherwise `a` is a <strong>witness</strong> and "
                     "`n` is composite.")),
            ("thm", ("A witness proves compositeness",
                     "If `n` is an odd prime, then for every base `a` in `2..n − 2` the chain "
                     "reaches `1` at `x₀` or reaches `n − 1` at some step. Equivalently, a witness "
                     "exists only for composite `n`.")),
            ("proof", ("Let `n` be prime. Fermat's little theorem gives "
                       "`aⁿ⁻¹ = a^(d·2ˢ) = 1`, so the last term of the chain is `1`. Consider the "
                       "first term of the chain that equals `1`.",
                       "If it is `x₀`, the base is inconclusive by the first condition. Otherwise "
                       "some `xᵢ₊₁ = 1` with `xᵢ ≠ 1`, so `xᵢ` is a square root of `1` modulo `n`. "
                       "Modulo a prime, `x² = 1` means `n` divides `(x − 1)(x + 1)`, so `n` divides "
                       "one of the factors and `x` is `1` or `n − 1`. Since `xᵢ ≠ 1`, it is "
                       "`n − 1`, and the base is inconclusive by the second condition.",
                       "So no base is a witness for a prime, and the contrapositive is the theorem: "
                       "a witness is a proof of compositeness.")),
            ("p", "The lab confirms the direction that cannot fail by trying every base. At "
                  "`n = 97`, all 94 usable bases are inconclusive and the witness count is `0`. "
                  "That is not evidence that 97 is prime &mdash; it is a consequence of 97 being "
                  "prime, and the panel says so, because the test has nothing to offer in that "
                  "direction."),
            ("p", "What the course does <em>not</em> prove is the other half: that at least three "
                  "quarters of the bases are witnesses for every odd composite. That result is "
                  "stated here, used in the error arithmetic, and established nowhere in this "
                  "library. The panel checks it on the `n` on screen and reports yes or the words "
                  "that would refute the theorem, which is a test rather than a proof."),
            ("h3", "The Fermat test, and why it is not enough"),
            ("def", ("The Fermat test",
                     "For a base `a`, compute `aⁿ⁻¹ mod n`. If the result is not `1`, then `n` is "
                     "composite. If it is `1`, the base is inconclusive. The strong test is this "
                     "test with the squaring chain inspected on the way, and every Fermat witness "
                     "is a strong witness.")),
            ("p", "There are composite numbers for which the Fermat test is not merely loose but "
                  "useless. A <strong>Carmichael number</strong> satisfies `aⁿ⁻¹ = 1` for every `a` "
                  "coprime to it, so no coprime base is ever a Fermat witness. The smallest is "
                  "`561 = 3 · 11 · 17`, and Discrete Mathematics names it when it introduces "
                  "Fermat's little theorem."),
            ("p", "The lab splits the Fermat count by coprimality, and the split is not a detail. "
                  "At `n = 561` there are 558 usable bases and 240 of them share a factor with 561; "
                  "those are caught, because `aⁿ⁻¹` cannot be `1` when `a` and `n` have a common "
                  "factor. So the Fermat test catches 240 of 558 bases, which is `40/93`, and a "
                  "panel printing only that fraction would show the Fermat test working about two "
                  "times in five and would have quietly refuted the Carmichael property. On the 318 "
                  "<em>coprime</em> bases it catches `0`, and that is the number the Carmichael "
                  "verdict is read off."),
            ("example", ("561, both tests, every base",
                         "558 bases from 2 to 559. The strong test: 550 witnesses, a fraction of "
                         "`275/279 ≈ 0.9857`, against a bound of `3/4`. The eight bases that are "
                         "not witnesses are `50, 101, 103, 256, 305, 458, 460, 511`. The Fermat "
                         "test: 240 witnesses of 558, and `0` of the 318 coprime bases. So the "
                         "strong test catches 561 with `275/279` of the bases and the Fermat test "
                         "catches it with none of the bases anyone would have chosen.")),
            ("p", "Trace base 50, which the panel opens on. `561 − 1 = 560 = 35 · 2⁴`, so `d = 35` "
                  "and `s = 4`. The chain starts at `50³⁵ mod 561 = 560`, which is `n − 1`, so the "
                  "base is inconclusive at the first step and the squaring never happens. One run "
                  "with that base reports nothing at all about 561."),
            ("p", "Contrast `n = 341 = 11 · 31` with `a = 2`. Here `d = 85`, `s = 2`, and "
                  "`2⁸⁵ mod 341 = 32`, which is neither `1` nor `340`; squaring gives `1`. The "
                  "chain reached `1` from something other than `±1`, so `32` is a nontrivial square "
                  "root of one and 341 is composite. And `2³⁴⁰ = 1 mod 341`, so the Fermat test on "
                  "the same base says nothing. Same number, same base, one test silent and the "
                  "other producing a factor."),
            ("h3", "The error after t independent bases"),
            ("p", "Because the error is one-sided, `t` independently chosen bases are wrong about a "
                  "composite `n` only if all `t` are inconclusive. If the fraction of inconclusive "
                  "bases is `q`, that has probability `qᵗ`. The proved bound gives `q ≤ 1/4` and so "
                  "an error of at most `4⁻ᵗ`, and the lab prints the exact `qᵗ` for the `n` on "
                  "screen beside `4⁻ᵗ`."),
            ("math", [
                "  n = 561:  q = 8/558 = 4/279",
                "",
                "  t      exact error q^t                         bound (1/4)^t",
                "  1      4/279                 = 0.0143369       0.25",
                "  3      64/21717639           = 0.0000029469    0.015625",
                "  5      1024/1690522737399    = 0.00000000061   0.0009765625",
                "",
                "  n = 2047: q = 240/2044 = 60/511",
                "  5      777600000/34842114263551 = 0.0000223178    0.0009765625",
            ]),
            ("p", "At `t = 5` on 561 the bound allows about one failure in a thousand and the truth "
                  "is about one in 1.65 billion. That gap is what &ldquo;at least three "
                  "quarters&rdquo; costs: it has to cover the worst composite, and 561 is nowhere "
                  "near it. The bound is the guarantee and the exact number is a fact about this "
                  "`n`, and only the first survives being applied to a number nobody has "
                  "enumerated."),
            ("p", "The worst of the lab's examples is `2047 = 23 · 89`, where 240 of the 2044 bases "
                  "are inconclusive, a fraction of `60/511 ≈ 0.117`. Still well inside `1/4`, and "
                  "the base that fails is `2` &mdash; the one everybody tries first. A "
                  "single-base test with a fixed base is not a randomised algorithm at all; it is a "
                  "deterministic test with a known counterexample, and someone can look the "
                  "counterexample up."),
        ],
        "lab": ("random", {"mode": "witness", "preset": "carmichael561"}),
        "steps_title": "Reading a one-sided test",
        "steps_intro": "Say what each verdict proves before counting anything.",
        "steps": [
            ("Write n − 1 = d·2ˢ first",
             "Everything else depends on it, and `d` must come out odd. At `n = 561`, `560 = 35·2⁴` "
             "so `d = 35` and `s = 4`; at `n = 341`, `340 = 85·2²`. The chain has `s + 1` entries "
             "and the panel labels each one."),
            ("Ask which verdict the chain produced",
             "Reached `1` at the start, or `n − 1` at some step: inconclusive, and nothing follows. "
             "Neither: `n` is composite, proved. Do not soften the second into &ldquo;probably "
             "composite&rdquo;, and do not harden the first into &ldquo;probably prime&rdquo; "
             "without the error arithmetic."),
            ("Look for the nontrivial square root",
             "If the chain reaches `1` from something other than `1` or `n − 1`, you have a factor: "
             "`gcd(x − 1, n)`. The panel prints that row when it appears, and it is the difference "
             "between a verdict and a certificate."),
            ("Choose the bases at random, and count how many",
             "A fixed base is a published counterexample waiting to be used &mdash; base 2 fails on "
             "2047. `t` random bases leave an error of at most `4⁻ᵗ`, and the panel shows the exact "
             "figure for this `n` alongside, usually many orders of magnitude smaller."),
        ],
        "worked": {
            "title": "Two numbers, one base each",
            "intro": [
                "561 with base 50, and 341 with base 2. The first produces no testimony and the "
                "second produces a factor, and the arithmetic in both is a squaring chain.",
            ],
            "lines": [
                "n = 561 = 3 * 11 * 17,  n - 1 = 560 = 35 * 2^4,  d = 35, s = 4",
                "  a = 50",
                "  a^d mod n = 50^35 mod 561 = 560 = n - 1   -> inconclusive, chain stops",
                "  verdict: no testimony.  561 is composite and this base does not say so.",
                "",
                "n = 341 = 11 * 31,  n - 1 = 340 = 85 * 2^2,  d = 85, s = 2",
                "  a = 2",
                "  a^d mod n = 2^85 mod 341 = 32        neither 1 nor 340",
                "  squared once             = 1         reached 1 from 32",
                "  32 is a nontrivial square root of 1, so 341 is COMPOSITE",
                "  gcd(32 - 1, 341) = gcd(31, 341) = 31,  and 341 / 31 = 11",
                "",
                "  the Fermat test on the same base: 2^340 mod 341 = 1  -> inconclusive",
                "",
                "EVERY BASE, both numbers",
                "  n = 561: strong 550 of 558 = 275/279 ; Fermat 0 of the 318 coprime bases",
                "  n = 341: strong 290 of 338 = 145/169 ; Fermat 200 of its 298 coprime bases",
                "  n =  97: strong 0 of 94 - it is prime, so there is no witness to find",
            ],
            "after": [
                "The 341 trace is the argument for the strong test in four lines. The Fermat test "
                "computes `2³⁴⁰` and looks only at the answer, which is `1`, and learns nothing. "
                "The strong test computes the same power by the same squaring chain and looks at "
                "the intermediate values, one of which is a nontrivial square root of one. Same "
                "work, more information, because it did not throw the chain away.",
                "Base 50 on 561 is the other half. It is one of only eight bases out of 558 that "
                "fail, and it is the base the panel opens on, deliberately: a lesson whose lab "
                "opens on a base that works would be showing the test succeeding and calling that "
                "an illustration of a probabilistic guarantee.",
                "For a faded rehearsal, set `n = 1105` and predict the two Fermat columns before "
                "reading them. The supplied first move is this: 1105 is `5 · 13 · 17` and it is a "
                "Carmichael number, so the coprime column is `0`. Work out how many of the 1102 "
                "bases are coprime to 1105, say what the other Fermat column must therefore be, "
                "and then check both &mdash; and then say how many strong liars you expect and "
                "compare.",
            ],
        },
        "quiz_title": "What each verdict proves",
        "quiz": [
            {"q": "The chain for base `a` never reaches `1` or `n − 1`. What has been established?",
             "a": ["`n` is probably composite",
                   "`n` is composite, proved",
                   "`n` is composite with probability at least 3/4",
                   "`a` shares a factor with `n`"],
             "c": 1,
             "why": "A witness is a proof: if `n` were prime, Fermat's theorem would force the "
                    "chain to end at `1`, and the only square roots of `1` modulo a prime are `1` "
                    "and `n − 1`, so the chain would have to pass through one of them. The "
                    "probability language belongs to the other verdict, where nothing is proved."},
            {"q": "The Fermat test catches 561 on 240 of its 558 bases. Why is 561 still called a Carmichael number?",
             "a": ["Because 240 is fewer than three quarters of 558",
                   "Because the Carmichael property is about bases coprime to `n`, and none of the 318 coprime bases is a Fermat witness",
                   "Because the strong test catches it",
                   "Because 240 of those bases are not usable"],
             "c": 1,
             "why": "A base sharing a factor with `n` cannot have `aⁿ⁻¹ = 1`, so it is caught for a "
                    "trivial reason; there are 240 such bases. The Carmichael property says every "
                    "coprime base is fooled, and the coprime column reads 0 of 318. Printing only "
                    "the 240 would show the Fermat test working two times in five and refute "
                    "nothing."},
            {"q": "The lab reports the exact error after five bases on 561 as `1024/1690522737399` and the bound as `1/1024`. What is the relationship?",
             "a": ["The bound is wrong by six orders of magnitude",
                   "The exact figure is a measurement and the bound is exact",
                   "Both are exact; the bound covers every odd composite and 561 is far easier than the worst one",
                   "The exact figure applies to the Fermat test and the bound to the strong test"],
             "c": 2,
             "why": "`q = 4/279` for 561, so `q⁵` is the exact error for this `n`, and `4⁻⁵` is "
                    "what the proved three-quarters bound allows for any odd composite. Both are "
                    "computed as exact fractions. The gap is the slack the bound leaves, and it is "
                    "the reason the bound is usable on numbers nobody has enumerated."},
            {"q": "Why is testing with a fixed base, say `a = 2`, not a randomised algorithm?",
             "a": ["Because 2 is even",
                   "Because there is no randomness, and the numbers it fails on — 2047 among them — can be looked up",
                   "Because the error bound needs at least four bases",
                   "Because the Fermat test uses base 2 as well"],
             "c": 1,
             "why": "With no random choice there is no probability to bound: the test either works "
                    "on your input or does not, and 2047 is a composite for which base 2 is "
                    "inconclusive. Choosing the bases at random is what makes `qᵗ` a probability "
                    "rather than a property of a published list."},
        ],
        "mistakes": [
            ("Reporting an inconclusive run as evidence of primality",
             "It is not evidence of anything on its own; it is the absence of a proof. Base 50 on "
             "561 runs the whole chain and produces no testimony, and 561 is composite. What "
             "licenses a probabilistic claim is the error arithmetic over several randomly chosen "
             "bases, and it has to be stated to be claimed."),
            ("Quoting the Fermat test's overall catch rate on a Carmichael number",
             "`40/93` of the bases at `n = 561`, which sounds like a test that half works. Every "
             "one of those catches is a base sharing a factor with 561, found for a reason that has "
             "nothing to do with Fermat's theorem. The number that matters is `0` of 318, and the "
             "lab prints both rows so the split cannot be missed."),
            ("Using one base, or the same base every time",
             "Base 2 is inconclusive for 2047, and 240 of that number's 2044 bases are. A "
             "single-base test has a fixed set of numbers it is wrong about, and an adversary "
             "choosing the input can pick one. Draw the bases at random and state how many you "
             "drew."),
        ],
        "standard": ("Finish when you can run the chain by hand and say exactly what each outcome licenses.",
                     "You should be able to factor `n − 1` as `d·2ˢ`, run the chain, recognise a "
                     "nontrivial square root of one and extract a factor from it, explain why no "
                     "base witnesses a prime, split a Fermat count by coprimality, and compute the "
                     "exact error after `t` random bases."),
        "note": ("This is the last of the three guarantees. An expectation says what happens on "
                 "average, a with-high-probability bound says what happens most of the time, and a "
                 "one-sided test says that one of its two answers is never wrong. The rest of the "
                 "course puts randomness inside a data structure, where the guarantee is again in "
                 "expectation &mdash; and where, as with a random pivot, the coins belong to the "
                 "structure rather than to the input."),
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "treaps",
        "title": "Treaps",
        "module": "Randomness inside the structure",
        "one_line": "Give each key a random priority, keep heap order on the priorities, and get the tree a random insertion order would have built whatever order you use.",
        "summary": (
            "A search tree's shape is decided by the insertion order, which the structure does "
            "not control. A treap gives every key a random priority and keeps heap order on "
            "the priorities as well as search order on the keys; the resulting tree is unique, "
            "so the insertion order cannot reach it. Twelve keys inserted in sorted order give "
            "a plain tree of height 11 and a treap of height 5, and inserting the same keys "
            "and priorities in a shuffled order gives the same treap, node for node."
        ),
        "key": [
            "a treap is a search tree on the keys AND a heap on the priorities",
            "for distinct keys and distinct priorities that tree is UNIQUE",
            "so the insertion order cannot change it — only the priorities can",
            "twelve keys sorted: plain tree height 11, treap height 5",
            "mean depth 5/2, counted; 2 ln n reads 4.970 and is an ASYMPTOTE",
            "rotations restore heap order only: there is no balance invariant anywhere",
        ],
        "key_label": "Two orders at once, and the uniqueness that follows",
        "concepts_intro": (
            "The hard idea is the uniqueness, because everything else follows from it. The "
            "other two are where the randomness comes from and what the structure does not have."
        ),
        "concepts": [
            ("Two invariants at once, and they determine the tree",
             "A <strong>treap</strong> holds a key and a priority at each node, is a binary search "
             "tree on the keys, and is a min-heap on the priorities. If all the keys and all the "
             "priorities are distinct, exactly one such tree exists: the minimum priority must be "
             "at the root, the keys below it split by the search property, and the same argument "
             "applies recursively. The lab's opening instance has the key with priority 1 at the "
             "root, and there is nothing to choose."),
            ("Uniqueness makes the insertion order irrelevant",
             "Two different insertion orders of the same key&ndash;priority pairs must end at the "
             "same tree, because there is only one tree they could end at. The panel builds it "
             "twice &mdash; sorted on the left, a shuffle on the right &mdash; and reports the same "
             "tree, node for node, while the rotation counts differ, 8 against 11. Different work, "
             "identical result."),
            ("The shape is the shape of a randomly built tree, and there is no balance rule",
             "A treap on keys with priorities in random order is exactly the tree a plain search "
             "tree would have if the keys had arrived in the order of those priorities. So its "
             "expected depth is the expected depth of a randomly built search tree, which The "
             "Shape Problem and Random BSTs measured: `2 ln n` asymptotically. Nothing checks a "
             "height, nothing checks a balance factor, and the rotations here restore heap order "
             "only."),
        ],
        "read_title": "A random order the structure supplies itself",
        "read_intro": "The two invariants, the uniqueness proof, what insertion costs, and the honest status of the depth figure.",
        "body": [
            ("p", "Binary Search Trees showed a tree's cost depending on something the structure "
                  "does not choose: twelve keys arriving in sorted order give a path of height 11, "
                  "and the same twelve arriving shuffled give a height of 4. Rotations and the AVL "
                  "Invariant fixed that by adding a rule the structure enforces on every "
                  "insertion. This lesson fixes it differently &mdash; by making the shape depend "
                  "on coins instead of on the arrival order."),
            ("def", ("A treap",
                     "A <strong>treap</strong> is a binary tree in which each node holds a "
                     "<strong>key</strong> and a <strong>priority</strong>. It satisfies the search "
                     "property on the keys &mdash; every key in a left subtree is smaller, every "
                     "key in a right subtree is larger &mdash; and the heap property on the "
                     "priorities: every node's priority is smaller than its children's.")),
            ("thm", ("Uniqueness",
                     "For any finite set of pairs with distinct keys and distinct priorities, "
                     "exactly one treap contains them.")),
            ("proof", ("Induct on the number of pairs. With none, the empty tree is the only one. "
                       "Otherwise the heap property forces the pair with the smallest priority to "
                       "be at the root: any other node with that pair would have an ancestor of "
                       "larger priority.",
                       "The search property then forces the partition of the remaining pairs: every "
                       "key smaller than the root's goes into the left subtree and every larger key "
                       "into the right. Neither subtree has a choice about which pairs it contains.",
                       "Each subtree is itself a treap on a strictly smaller set with distinct keys "
                       "and distinct priorities, so by induction each is unique. The whole tree is "
                       "therefore unique.")),
            ("p", "The lab does not argue this, it checks it. Both panels are built from the same "
                  "priority assignment and compared node for node, and the verdict reads the same "
                  "tree, node for node or words that would refute the claim. Priorities are ranked "
                  "rather than taken raw so that no two can collide; a tie would leave the shape "
                  "undetermined and the claim would fail for a reason with nothing to do with "
                  "treaps."),
            ("example", ("Twelve keys, one priority assignment, two insertion orders",
                         "The keys are `10, 20, …, 120` and the seed assigns priorities "
                         "`10:6  20:3  30:1  40:10  50:12  60:7  70:2  80:11  90:9  100:5  110:4  "
                         "120:8`. Priority 1 belongs to key 30, so 30 is the root. Inserting in "
                         "sorted order costs 8 rotations; inserting in a shuffled order costs 11. "
                         "Both produce a tree of height 5 with mean depth `5/2`, and the two trees "
                         "are identical. A plain search tree on the same sorted order has height "
                         "11 and mean depth `11/2`.")),
            ("p", "Height 5 against 11, and mean depth `5/2` against `11/2`: the treap is less than "
                  "half as deep on average, on the input that is worst for a plain tree. And it got "
                  "there without any rule about heights &mdash; the only thing being maintained is "
                  "heap order on twelve numbers the structure generated itself."),
            ("h3", "Insertion, and what a rotation is for here"),
            ("p", "To insert a key, give it a random priority, place it as a leaf by the ordinary "
                  "search-tree rule, and then rotate it upwards while its priority is smaller than "
                  "its parent's. A rotation preserves the search property &mdash; Rotations and the "
                  "AVL Invariant proves that, and the in-order sequence is what it preserves "
                  "&mdash; so the search property is never in danger, and the loop stops exactly "
                  "when heap order is restored."),
            ("p", "That is the whole implementation, and it is worth noticing what is absent. No "
                  "height is stored, no balance factor is computed, no case analysis over four "
                  "shapes. Deletion is the same idea in reverse: rotate the node down until it is a "
                  "leaf, then remove it. The panel's rotation counts, 8 and 11 for the two orders, "
                  "are the only work the structure did beyond the searches."),
            ("h3", "What the guarantee is, and what the printed 2 ln n is not"),
            ("p", "The depth of a treap is a random variable, and its expectation is the expected "
                  "depth of a search tree built from a uniformly random insertion order &mdash; "
                  "which is `2 ln n + O(1)` for the mean depth, and `O(log n)` for the height. Both "
                  "of those are <strong>stated</strong> on this path: The Shape Problem and Random "
                  "BSTs states them, Randomised Quicksort derives the recurrence they come from, "
                  "because a random root and a random pivot are the same object, and no lesson in "
                  "this library carries the full argument."),
            ("p", "So the panel prints `2 ln n` in its own row, labelled asymptotic, and it is "
                  "about 15 per cent wrong about the tree in front of you. At `n = 12` it reads "
                  "`4.970` while the counted mean depth is `2.500` and the counted height is `5`. "
                  "Three numbers, three meanings: one asymptote, one exact mean of integers, one "
                  "count. Reading them as estimates of each other is the failure mode of this "
                  "page, and it is why each is labelled where it is printed."),
            ("p", "The guarantee is also in expectation and not always. Over seeds 1 to 12 at "
                  "twelve keys the treap's height came out `5, 6, 4, 5, 5, 6, 6, 5, 5, 4, 6, 5` "
                  "&mdash; never 11, and never 3 either. Move the priority seed and watch it move. "
                  "An AVL tree's height at twelve keys is bounded by a rule the structure enforces; "
                  "a treap's is a random variable whose bad cases are unlikely rather than "
                  "impossible."),
            ("p", "That is the trade, and it is the same trade a random pivot makes. The input is "
                  "arbitrary, possibly chosen by someone who wants the structure to perform badly, "
                  "and the coins are the structure's own, so no input can be bad for it &mdash; "
                  "only an unlucky draw can, and the draw is not the adversary's to make. Universal "
                  "Hashing bought the same thing for a hash table with the same manoeuvre."),
        ],
        "lab": ("tree", {
            "mode": "treap",
            "preset": "sorted-against-shuffled",
            "panel_title": "Insert the same keys and priorities in two different orders",
            "panel_intro": (
                "Both trees are built from one priority assignment, so uniqueness says they must "
                "come out identical and the panel checks it node for node. The plain search tree on "
                "the same order is in the third row, and the `2 ln n` in the fourth is an asymptote "
                "rather than a prediction about either tree above it."
            ),
        }),
        "steps_title": "Working with a structure that randomises itself",
        "steps_intro": "Find the root before anything else; the rest of the tree is forced.",
        "steps": [
            ("Find the smallest priority: that is the root",
             "Then partition the remaining keys by comparison with it and recurse. This is the "
             "uniqueness proof used as an algorithm, and it builds the tree without reference to "
             "any insertion order at all."),
            ("Change the insertion order and expect nothing to happen",
             "Swap the two order menus. The rotation counts change and the trees do not. If they "
             "ever differed, the priorities would be the thing to check first &mdash; a tie breaks "
             "uniqueness and nothing else does."),
            ("Change the priority seed to see the real variability",
             "This is the knob that matters. Heights at twelve keys range over 4, 5 and 6 across "
             "the first dozen seeds. That spread is the guarantee's actual content: bad shapes are "
             "unlikely, not impossible."),
            ("Keep the three depth numbers apart",
             "The counted height, the exact mean depth as a fraction, and the `2 ln n` asymptote. "
             "At twelve keys they are `5`, `5/2` and `4.970`. Only the first two are about this "
             "tree, and the panel labels all three."),
        ],
        "worked": {
            "title": "One priority assignment, two insertion orders",
            "intro": [
                "Keys `10` to `120`, priorities from the seed, and the claim that the insertion "
                "order cannot be read off the result.",
            ],
            "lines": [
                "key       10  20  30  40  50  60  70  80  90 100 110 120",
                "priority   6   3   1  10  12   7   2  11   9   5   4   8",
                "",
                "smallest priority is 1, at key 30, so 30 is the root",
                "  left of 30:  keys 10, 20        smallest priority there is 3, at key 20",
                "  right of 30: keys 40..120       smallest priority there is 2, at key 70",
                "",
                "tree                                 height  mean depth  rotations",
                "  treap, inserted sorted                5       5/2 = 2.500      8",
                "  treap, inserted shuffled              5       5/2 = 2.500     11",
                "  the two trees                         identical, node for node",
                "  plain search tree, inserted sorted   11      11/2 = 5.500      0",
                "  2 ln n at n = 12                      -        4.970  asymptotic",
                "",
                "treap height at n = 12 over priority seeds 1..12",
                "  5  6  4  5  5  6  6  5  5  4  6  5      never 11, never 3",
            ],
            "after": [
                "Build the top two levels from the priority row by hand before looking at the "
                "drawing: root 30, then 20 on the left and 70 on the right. Nothing about the "
                "insertion order entered that reasoning, which is exactly the claim &mdash; the "
                "priorities determine the tree and the order determines only the rotations.",
                "The rotation counts are the one place the two runs differ, 8 against 11. That is "
                "real work and it is the price of the guarantee: a plain tree on the sorted order "
                "does no rotations at all and ends up with height 11. Paying eight rotations to "
                "halve the depth is the trade, and it is cheaper than the AVL case analysis it "
                "replaces.",
                "For a faded rehearsal, set the priority seed to 3 and predict the height before "
                "the panel redraws. The supplied first move is this: the seed changes the "
                "priorities and therefore the tree, and the first dozen seeds give heights between "
                "4 and 6. Say what the smallest and largest heights a twelve-key treap can possibly "
                "have are, and then say why neither extreme showed up in twelve seeds.",
            ],
        },
        "quiz_title": "Uniqueness and what follows from it",
        "quiz": [
            {"q": "Two insertion orders of the same keys and priorities give the same treap. Why?",
             "a": ["Because the insertion routine sorts the keys first",
                   "Because exactly one tree is both a search tree on the keys and a heap on the priorities",
                   "Because the rotation counts happened to match",
                   "Because the priorities were assigned in sorted order"],
             "c": 1,
             "why": "The smallest priority has to be at the root, the search property forces the "
                    "partition below it, and induction does the rest. With distinct keys and "
                    "distinct priorities there is nothing left to choose, so no insertion order can "
                    "reach a different tree. The rotation counts do differ: 8 against 11 on the "
                    "lab's instance."},
            {"q": "The panel prints a counted height of 5, an exact mean depth of `5/2` and `2 ln n = 4.970`. Which is a claim about this tree?",
             "a": ["All three",
                   "The first two; the third is an asymptote for the mean depth of a randomly built tree",
                   "Only the third, since it is the theoretical value",
                   "Only the first, since a mean is not a property of a tree"],
             "c": 1,
             "why": "The height is counted on the tree drawn beside it, and the mean depth is an "
                    "exact fraction computed from its node depths. `2 ln n` is an asymptote with "
                    "suppressed constants and is about 15 per cent off at this size — it reads "
                    "`4.970` where the mean depth is `2.500`. The panel labels the row asymptotic."},
            {"q": "What invariant does a treap's rotation restore?",
             "a": ["A balance factor of at most one",
                   "Heap order on the priorities; the search property was never in danger",
                   "The height bound `2 log₂ n`",
                   "Both heap order and a height bound"],
             "c": 1,
             "why": "A rotation preserves the in-order sequence, so the search property holds "
                    "automatically, and the insertion loop rotates upwards only while the new "
                    "node's priority is smaller than its parent's. There is no balance invariant "
                    "anywhere in a treap and nothing checks a height; the depth is a probabilistic "
                    "consequence of the priorities."},
            {"q": "Over the first twelve priority seeds the treap's height at twelve keys ranged over 4, 5 and 6. What does that tell you?",
             "a": ["The guarantee is in expectation, so bad shapes are unlikely rather than impossible",
                   "The structure is broken: a treap should have a fixed height",
                   "The height is bounded by 6 for twelve keys",
                   "The priorities were not random"],
             "c": 0,
             "why": "The shape is a random variable, and 4 to 6 is where its mass sits at twelve "
                    "keys. Height 11 is possible — it is the shape a plain sorted insertion gives — "
                    "and it requires the priorities to arrive in a particular one of `12!` orders. "
                    "An AVL tree's height is bounded by an enforced rule; a treap's is not bounded "
                    "at all."},
        ],
        "mistakes": [
            ("Expecting the insertion order to matter",
             "It changes the rotations and nothing else. A reader who has just come from Binary "
             "Search Trees, where the order decided everything, will look for its effect on the "
             "shape and find none &mdash; which is the result, not a failure of the experiment. "
             "The knob that changes the shape is the priority seed."),
            ("Reading 2 ln n as the tree's depth",
             "At twelve keys it reads `4.970` and the counted mean depth is `2.500`. It is an "
             "asymptote for the expected mean depth of a randomly built tree, with constants "
               "suppressed, and this library states it rather than proving it. Quoting it as a "
             "prediction about a small tree is quoting a growth rate as a value."),
            ("Expecting a height bound",
             "There is none. A treap can be a path, with probability `1/n!` for a given path "
             "shape, and nothing in the structure prevents it. If a bound that holds always is "
             "required, AVL Insertion is the structure that provides one and it pays for it with "
             "stored heights and a case analysis."),
        ],
        "standard": ("Finish when you can build the treap from a priority list without being told the insertion order.",
                     "You should be able to state both invariants, prove uniqueness by induction on "
                     "the smallest priority, describe insertion as a leaf placement plus upward "
                     "rotations, and say which of the panel's depth figures is counted, which is "
                     "exact and which is an asymptote."),
        "note": ("A treap keeps the coins in the priorities and the structure in the tree. "
                 "&ldquo;Skip Lists&rdquo; keeps the coins in the structure itself: each element "
                 "chooses how many express lanes it appears in by flipping until it stops, nothing "
                 "is ever rebalanced or rebuilt, and the search cost is counted by walking rather "
                 "than derived from a height."),
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "skip-lists",
        "title": "Skip Lists",
        "module": "Randomness inside the structure",
        "one_line": "Let each element choose its own number of express lanes by flipping a coin, then count the hops a search actually takes.",
        "summary": (
            "A skip list is a sorted linked list with express lanes above it. Each element "
            "picks its top lane when it is inserted, by flipping a coin until it comes up "
            "tails, and nothing is ever rebalanced. On the lab's opening tape, 10 of 16 keys "
            "reach at least the first express lane, the tallest reaches the fifth, and a "
            "search costs `77/16` hops on average with a worst case of 8 &mdash; against a "
            "reference curve of `2 log₂ n = 8.000`, which is not a count."
        ),
        "key": [
            "level 0 is the whole sorted list; level k+1 holds about half of level k",
            "each key's top level is the run of heads at its place on the tape",
            "search: go right while the next key is not past the target, else drop a level",
            "16 keys, one tape: 10 promoted, tallest L4, mean hops 77/16, worst 8",
            "2 log₂ n = 8.000 is a REFERENCE CURVE, not a count and not a bound",
            "nothing is rebuilt: every level decision is local and permanent",
        ],
        "key_label": "One coin per element, and the hops that follow",
        "concepts_intro": (
            "The hard idea is that the structure is never repaired. The other two are how a "
            "level is chosen and what the printed reference curve is for."
        ),
        "concepts": [
            ("Express lanes, each about half the one below",
             "Level 0 is the sorted list of every key. A key appears at level `k + 1` with "
             "probability a half, independently, so level `k` holds about `n/2ᵏ⁺¹` keys and the "
             "levels form a geometric cascade. A search starts at the top left, moves right while "
             "the next key does not overshoot the target, and drops a level when it does. Each drop "
             "roughly halves the interval that remains to be searched."),
            ("A level is chosen once, locally, and never revisited",
             "When a key is inserted it flips a coin until it comes up tails; the number of heads "
             "is its top level. That decision involves no other key, no global counter and no "
             "rebalancing, and it is never changed. The lab shows this directly: change `n` and the "
             "existing keys' levels do not move, because each one was decided from that key's own "
             "place on the tape."),
            ("The printed curve is a reference, not a count and not a bound",
             "The expected search cost is `O(log n)`, and the panel draws `2 log₂ n` as a dashed "
             "curve beside the hops it counted. That curve is sampled at double precision, no "
             "verdict is read off it, and at sixteen keys on this tape it reads `8.000` where the "
             "counted mean is `77/16 = 4.813`. The counted number is the one this page computed."),
        ],
        "read_title": "A structure with no invariant to maintain",
        "read_intro": "The levels, the search, the counted hops, and the reference curve that is labelled rather than quoted.",
        "body": [
            ("def", ("A skip list",
                     "A <strong>skip list</strong> on a sorted set of keys is a sequence of linked "
                     "lists `L₀ ⊇ L₁ ⊇ L₂ ⊇ …`. `L₀` contains every key. Each key in `Lₖ` appears "
                     "in `Lₖ₊₁` with probability `1/2`, independently of every other key. A key's "
                     "<strong>level</strong> is the highest list it appears in.")),
            ("p", "Equivalently, and this is how the lab builds it: each key reads the coin tape at "
                  "its own position and takes the length of the run of heads there as its level. "
                  "The tape is the reader's, chosen by a seed, so the structure is reproducible "
                  "without being fixed &mdash; and the coins come from the prime-modulus stream, "
                  "because the low bit of a power-of-two-modulus generator is not a coin and a "
                  "structure built from one would have levels that repeat on a short cycle."),
            ("def", ("The search",
                     "To find a target, start at the leftmost node of the highest level. Repeatedly: "
                     "if the next node at this level exists and its key is not greater than the "
                     "target, move to it; otherwise drop one level. Stop at level 0. Each move and "
                     "each drop is a <strong>hop</strong>, and the hops are what the lab counts.")),
            ("example", ("Sixteen keys from one tape",
                         "Keys `10` to `160`. The tape gives levels `1, 1, 2, 0, 0, 4, 0, 1, 0, 0, "
                         "1, 4, 1, 0, 1, 1`, so 10 of the 16 keys reach at least level 1 and two "
                         "reach level 4. Searching for key 120, which is at level 4, takes 2 hops; "
                         "searching for key 100, which is at level 0 and is the second of two "
                         "consecutive level-0 keys, takes 8. The mean over all sixteen searches is `77/16 = 4.813` and "
                         "the worst is 8.")),
            ("p", "Those two searches are the lesson in miniature. Key 120 is one of the two tallest "
                  "nodes, so the top-level walk reaches it in two hops. Key 100 has level 0 and must "
                  "be reached by descending all the way and walking, so it costs 8. Same structure, "
                  "same tape, a factor of four between two lookups &mdash; and the mean of the "
                  "sixteen is a fraction, because a mean of integers is."),
            ("h3", "The level table, and where the halving is visible"),
            ("math", [
                " level   keys whose top level is this   keys present at this level   n/2^(k+1)",
                "   L0                 6                            16                 8.00",
                "   L1                 7                            10                 4.00",
                "   L2                 1                             3                 2.00",
                "   L3                 0                             2                 1.00",
                "   L4                 2                             2                 0.50",
            ]),
            ("p", "The right-hand column is what the geometric cascade predicts and the middle "
                  "column is what this tape produced. They are in the same neighbourhood and they "
                  "are not equal: 10 keys present at level 1 against a predicted 8, and 2 at level "
                  "4 against a predicted `0.5`. Level 3 is the row worth staring at &mdash; no key "
                  "has 3 as its top level, and two keys are nevertheless present there, because a "
                  "key at level 4 appears at every level below it."),
            ("p", "That distinction between &ldquo;top level is `k`&rdquo; and &ldquo;present at "
                  "level `k`&rdquo; is the commonest confusion in reading a skip list, and it is "
                  "why the panel prints both columns. The first is a partition of the keys and adds "
                  "to `n`; the second is a nested family and decreases as `k` grows."),
            ("h3", "What is guaranteed, and what the dashed curve is doing"),
            ("p", "The expected number of levels is `O(log n)` and the expected search cost is "
                  "`O(log n)` as well: at each level the walk passes a constant number of nodes in "
                  "expectation before dropping, because the probability that the next node is "
                  "present one level up is a half. This course does not prove a concentration "
                  "result around that expectation &mdash; the tail bound needed is a Chernoff "
                  "bound and this course excludes it &mdash; so what is available is an expectation "
                  "and the counts on screen."),
            ("p", "So the panel draws `2 log₂ n` as a dashed reference and labels it. At sixteen "
                  "keys it reads `8.000` and the counted mean is `4.813`; at eight keys it reads "
                  "`6.000` and a different tape counted `3.250`. The curve is not a bound, not an "
                  "asymptote that has been proved here, and not a prediction; it is a familiar "
                  "shape to read the counted points against, and the panel says so in those terms."),
            ("p", "The search cost is also a random variable in the same way a treap's depth is, "
                  "and for the same reason: the coins belong to the structure. A worst case of 8 "
                  "hops on sixteen keys is this tape's worst case, and another tape gives another. "
                  "Nothing here bounds it, and the honest statement is the one the panel makes "
                  "&mdash; the mean is `77/16`, the worst observed is 8, and both are counts on the "
                  "structure drawn above them."),
            ("h3", "The trade against a balanced tree"),
            ("p", "An AVL tree guarantees a height, always, and pays with a stored height per node, "
                  "a case analysis over four rotation shapes, and a rebalancing pass on every "
                  "insertion and deletion. A skip list guarantees an expectation, and pays with "
                  "nothing at all: an insertion writes a few pointers at the levels the coin "
                  "chose, and no other node is touched. There is no global structure to maintain, "
                  "which is the whole point of the design."),
            ("p", "That absence is also what makes a skip list easy to get right and easy to make "
                  "concurrent, and it is what makes its worst case unbounded. Which of those "
                  "matters more is a question about the system rather than about the structure "
                  "&mdash; the same question Universal Hashing asked about whether anyone can "
                  "choose your keys."),
        ],
        "lab": ("tree", {
            "mode": "skiplist",
            "preset": "sixteen",
            "panel_title": "Fix the tape, then count the hops a search takes",
            "panel_intro": (
                "Every level is the run of heads at that key's place on the tape, chosen once and "
                "never revisited, and every hop is counted by walking the list. The dashed "
                "`2 log₂ n` beside the counted points is a reference curve: it is sampled at double "
                "precision and no verdict on this page is read off it."
            ),
        }),
        "steps_title": "Reading a randomised structure by walking it",
        "steps_intro": "Count the hops. Then ask what the count is a count of.",
        "steps": [
            ("Read the level of each key from the tape, not from the drawing",
             "A key's level is the run of heads at its position. That is the only input to the "
             "shape, and it means the structure can be rebuilt from the seed alone &mdash; which is "
             "what makes every number on the page reproducible."),
            ("Separate “top level is k” from “present at level k”",
             "The first partitions the keys and adds to `n`; the second is nested and decreases. "
             "The panel prints both, and the level-3 row of the opening tape has 0 in the first "
             "column and 2 in the second."),
            ("Search two keys that differ in level",
             "A tall key is found from the top in a couple of hops; a level-0 key behind a tall one "
             "costs the descent and the walk. On the opening tape those are 2 hops and 8, and the "
             "spread is what the mean is a mean of."),
            ("Read the dashed curve as a shape, not a value",
             "`2 log₂ n` reads `8.000` at sixteen keys where the counted mean is `4.813`. It is "
             "there to show the counted points growing like a logarithm. Nothing on the page is "
             "decided by it and the panel says so."),
        ],
        "worked": {
            "title": "Sixteen keys, one tape, sixteen searches",
            "intro": [
                "Keys `10` through `160`, levels from the tape, and the cost of finding each one. "
                "The mean of the last column is the panel's headline figure.",
            ],
            "lines": [
                "key     10  20  30  40  50  60  70  80  90 100 110 120 130 140 150 160",
                "level    1   1   2   0   0   4   0   1   0   0   1   4   1   0   1   1",
                "hops     4   5   3   6   7   1   6   5   7   8   6   2   3   5   4   5",
                "",
                "  promoted above level 0     10 of 16",
                "  tallest level              L4, reached by keys 60 and 120",
                "  mean hops   = 77/16 = 4.8125     worst = 8, for key 100",
                "  2 log2 16   = 8.000              a reference curve",
                "",
                "  cheapest search: key 60, at L4, one hop",
                "  dearest search:  key 100, at L0, eight hops",
            ],
            "after": [
                "Key 60 costs one hop and key 100 costs eight, and both are in the same structure. "
                "The mean `77/16` is an exact fraction because it is the average of sixteen "
                "integers, and it is not the cost of any search: no lookup costs `4.8125` hops. "
                "That is the same distinction as everywhere else on this course, arriving here as "
                "an average over queries rather than over seeds.",
                "The counted mean sits well below the dashed `8.000`. Do not read that as the "
                "structure beating its bound &mdash; `2 log₂ n` is not a bound, and at `n = 8` on "
                "another tape the counted mean was `3.250` against a reference of `6.000`. The "
                "curve is a shape, the points are counts, and the panel keeps them in different "
                "colours for that reason.",
                "For a faded rehearsal, move the tape seed and predict what happens to the level "
                "column before the page redraws. The supplied first move is this: each key's level "
                "is read from its own position on the tape, so a new tape gives new levels for "
                "every key at once. Say whether the number promoted above level 0 should stay near "
                "half of 16, then check several seeds &mdash; and then say why changing `n` instead "
                "leaves the existing keys' levels alone.",
            ],
        },
        "quiz_title": "Levels, hops, and reference curves",
        "quiz": [
            {"q": "The level table shows 0 keys whose top level is 3 and 2 keys present at level 3. How can both be true?",
             "a": ["One of the two columns is a measurement and the other a prediction",
                   "A key at level 4 appears at every level below it, so it is present at level 3 without level 3 being its top",
                   "The table has an off-by-one error",
                   "Level 3 is empty and the 2 is the prediction `n/2⁴`"],
             "c": 1,
             "why": "The lists are nested: `L₀ ⊇ L₁ ⊇ L₂ ⊇ …`, so the two keys at level 4 are "
                    "present at levels 3, 2, 1 and 0 as well. The first column partitions the keys "
                    "by their top level and adds to `n`; the second counts presence and decreases "
                    "with the level."},
            {"q": "What is the standing of `2 log₂ n` on this page?",
             "a": ["A proved upper bound on the hops",
                   "The expected number of hops, derived in this lesson",
                   "A reference curve, sampled at double precision, from which nothing is decided",
                   "A measurement averaged over the tapes the panel ran"],
             "c": 2,
             "why": "The panel labels it as a reference curve and draws it dashed. The expected "
                    "search cost is `O(log n)`; this page does not derive a constant and does not "
                    "prove a concentration result, because the tail bound that would need is a "
                    "Chernoff bound and this course excludes them. The counted mean at sixteen keys "
                    "is `77/16`, well below the curve's `8.000`."},
            {"q": "How is a key's level decided?",
             "a": ["By a global counter that keeps each level half the size of the one below",
                   "By flipping a coin at insertion until it comes up tails, with no reference to any other key",
                   "By rebalancing after every insertion",
                   "By its position in the sorted order"],
             "c": 1,
             "why": "The decision is local, made once, and never revisited — which is why nothing "
                    "is ever rebuilt. The lab reads the run of heads at that key's place on the "
                    "tape. Change `n` and the existing keys' levels do not move, which is the "
                    "observable consequence of the decision being local."},
            {"q": "Compared with an AVL tree, what does a skip list give up?",
             "a": ["The search property",
                   "A height guarantee that holds always: a skip list's cost is an expectation and nothing bounds its worst case",
                   "Ordered traversal",
                   "Logarithmic expected search cost"],
             "c": 1,
             "why": "An AVL tree enforces a rule on every insertion and gets a height bound that "
                    "holds for every input. A skip list enforces nothing and gets an expectation, "
                    "with the bad cases unlikely rather than impossible. In exchange an insertion "
                    "touches only a few pointers and no other node is disturbed."},
        ],
        "mistakes": [
            ("Reading the counted mean against the dashed curve as a pass or a fail",
             "`77/16 = 4.813` against `2 log₂ 16 = 8.000` is not the structure beating a bound, "
               "because the curve is not a bound. It is a familiar logarithmic shape drawn so that "
             "the counted points can be seen growing like one. The panel colours it differently and "
             "labels it for exactly this reason."),
            ("Confusing a key's top level with the levels it occupies",
             "A level-4 key is present at five levels. The partition column and the presence column "
             "answer different questions and only the first adds to `n`; on the opening tape they "
             "differ most visibly at level 3, where the first is 0 and the second is 2."),
            ("Expecting a bound on the worst search",
             "There is none. The worst search on the opening tape costs 8 hops on sixteen keys, "
             "another tape gives another number, and nothing in the structure prevents a tape that "
             "promotes nothing at all. If a worst case must be bounded, the structure to use is one "
             "that enforces an invariant."),
        ],
        "standard": ("Finish when you can build a skip list from a coin tape and count a search by walking it.",
                     "You should be able to read each key's level off the tape, describe the search "
                     "as move-right-or-drop, count its hops, distinguish top level from presence at "
                     "a level, and say what the dashed curve is and is not."),
        "note": ("The last two lessons of this course spend randomness on space rather than on "
                 "shape. A Bloom filter answers set membership in a few bits per key by accepting a "
                 "false positive rate it can compute exactly, and &ldquo;The Count-Min "
                 "Sketch&rdquo; estimates frequencies in a fixed grid of counters with a guarantee "
                 "that is Markov's inequality applied once per row."),
    },
    # ---------------------------------------------------------------- 13
    {
        "slug": "bloom-filters",
        "title": "Bloom Filters",
        "module": "Randomness inside the structure",
        "one_line": "Trade an exactly computable false-positive rate for a few bits per key, and watch the familiar formula turn out to be the approximation.",
        "summary": (
            "A Bloom filter stores a set in `m` bits by hashing each key to `k` of them and "
            "setting those bits. A clear bit is a certain no; a set bit may be somebody else's. "
            "The false-positive rate is `(1 − (1 − 1/m)^{kn})^k` exactly, and at sixteen keys "
            "in 160 bits with seven hashes that is `0.008319`. The textbook "
            "`(1 − e^{−kn/m})^k` gives `0.008194`, and the gap between the two is the "
            "independence assumption."
        ),
        "key": [
            "insert: set the k bits h₁(x) … hₖ(x).  query: are all k bits set?",
            "a clear bit is a CERTAIN no; there are no false negatives, ever",
            "P(false positive) = (1 − (1 − 1/m)^{kn})^k, exactly",
            "m = 160, n = 16, k = 7:  0.008319 — about 1 in 120",
            "the idealised (1 − e^{−kn/m})^k gives 0.008194, and it is an APPROXIMATION",
            "nothing can be deleted: clearing a bit would create false negatives",
        ],
        "key_label": "One-sided error in a few bits a key, and the exact rate",
        "concepts_intro": (
            "The hard idea is that one answer is certain and the other is not. The other two "
            "are the exact rate and the idealisation that is usually quoted in its place."
        ),
        "concepts": [
            ("A clear bit is a proof, a set bit is a hint",
             "Inserting `x` sets `k` specific bits. So if any of `x`'s `k` bits is clear, `x` was "
               "never inserted &mdash; a certain no, with no probability attached. If all `k` are "
             "set, either `x` is present or other keys happened to set all `k` between them. The "
             "error is <strong>one-sided</strong>, and it is the same shape as the primality test's: "
             "one answer is a proof and the other is silence."),
            ("The exact rate is a fraction, and the lab computes it as one",
             "A given bit is left clear by all `kn` settings with probability `(1 − 1/m)^{kn}`, so "
             "it is set with probability `1 − (1 − 1/m)^{kn}`, and a false positive needs `k` such "
             "bits: `(1 − (1 − 1/m)^{kn})^k`. That is a rational number, and at `m = 160`, `n = 16` "
             "and `k = 7` its denominator has over seventeen hundred digits. A double turns it into "
             "`NaN`; the lab holds it as BigInt over BigInt and prints the decimal by long "
             "division."),
            ("The familiar formula is the approximation, not the answer",
             "`(1 − e^{−kn/m})^k` is what textbooks quote, and it is the exact expression with two "
             "idealisations: `(1 − 1/m)^{kn} ≈ e^{−kn/m}`, and the `k` bit tests treated as "
             "independent when they are not. It reads `0.008194` where the truth is `0.008319`. The "
             "panel prints both and the difference, and the giveaway is that the idealised figure "
             "depends only on `k` and the bits per key &mdash; move the key slider and it does not "
             "change at all, while the exact rate does."),
        ],
        "read_title": "A set in a few bits, and the rate it costs",
        "read_intro": "The structure, the exact rate, the idealisation beside it, the best k found by scanning, and the operation the filter cannot support.",
        "body": [
            ("def", ("A Bloom filter",
                     "A <strong>Bloom filter</strong> for a set is an array of `m` bits, initially "
                     "all clear, together with `k` hash functions into `0..m − 1`. To "
                     "<strong>insert</strong> `x`, set the bits `h₁(x), …, hₖ(x)`. To "
                     "<strong>query</strong> `x`, report present if all `k` of those bits are set "
                     "and absent otherwise. The structure stores no keys.")),
            ("p", "That last sentence is the point of it. Sixteen keys at ten bits each is 160 bits "
                  "&mdash; twenty bytes &mdash; for a set that would take at least sixteen machine "
                  "words to store exactly. The saving is what the false-positive rate is paid for, "
                  "and the rate is what this lesson computes."),
            ("thm", ("The false-positive rate",
                     "Suppose `n` keys have been inserted into `m` bits with `k` hash functions, "
                     "each of the `kn` settings choosing a bit uniformly at random and "
                     "independently. Then a key that was never inserted is reported present with "
                     "probability `(1 − (1 − 1/m)^{kn})^k`.")),
            ("proof", ("Fix a bit. Each of the `kn` settings misses it with probability `1 − 1/m`, "
                       "and the settings are independent, so the bit is clear with probability "
                       "`(1 − 1/m)^{kn}` and set with probability `1 − (1 − 1/m)^{kn}`.",
                       "A query on an absent key reports present exactly when all `k` of its bits "
                       "are set. Treating those `k` events as independent gives the product, which "
                       "is the `k`-th power.")),
            ("p", "The second step is where the honesty is required. The `k` bits of a query are "
                  "<em>not</em> independent: knowing that one of them is set is mild evidence that "
                  "the filter is full, which makes the others more likely to be set too. So the "
                  "expression above is itself an idealisation of the truth for a real filter, and "
                  "this library's arithmetic computes it exactly as the expression it is, while "
                  "labelling the further `e^{−kn/m}` step as approximate. The lab's measured column "
                  "&mdash; the false positives an actual filter returned &mdash; is the only figure "
                  "on the page with no model in it."),
            ("example", ("Sixteen keys, ten bits each, seven hashes",
                         "`m = 160`, `n = 16`, `k = 7`. The exact rate is `0.008319`, which the "
                         "panel also prints as about 1 in 120. The idealised "
                         "`(1 − e^{−kn/m})^k` gives `0.008194`, a difference of `1.25 × 10⁻⁴`. The "
                         "filter the lab built set 74 of its 160 bits and returned 1 false positive "
                         "in 200 queries of keys it had never seen.")),
            ("p", "Three numbers again, in the shape this course has used throughout. `0.008319` is "
                  "exact under the stated model. `0.008194` is an approximation of it and is "
                  "labelled. `1 of 200` is a measurement on one filter with one seed, and 200 "
                  "queries cannot resolve a rate of one in 120 &mdash; the expected number of false "
                  "positives in 200 queries is about `1.66`, so `1` is unremarkable and so would "
                  "`0` or `4` be."),
            ("h3", "Choosing k, by scanning rather than by a rule of thumb"),
            ("p", "More hash functions set more bits, which raises the chance that any given bit is "
                  "set, and they also require more bits to be set for a false positive, which "
                  "lowers it. The two effects compete and there is an optimum. The usual rule is "
                  "`k* = (m/n)·ln 2`, which at ten bits per key suggests `6.93`. The panel does not "
                  "use it: it evaluates the exact rate at every `k` from 1 to 10 and reports the "
                  "smallest."),
            ("math", [
                "  m = 160, n = 16    exact rate by k",
                "   k = 1   0.095446      k = 6   0.008553",
                "   k = 2   0.033045      k = 7   0.008319   <- the best",
                "   k = 3   0.017551      k = 8   0.008595",
                "   k = 4   0.011934      k = 9   0.009287",
                "   k = 5   0.009545      k = 10  0.010373",
            ]),
            ("p", "The curve is flat near its minimum &mdash; `k = 6`, `7` and `8` are within four "
                  "per cent of each other &mdash; and it climbs sharply on the left. So "
                  "under-hashing is expensive and over-hashing is cheap, which is worth knowing "
                  "when the rule of thumb lands between two integers. At twelve keys and twelve "
                  "bits each the panel's scan puts the optimum at `k = 8` with a rate of "
                  "`0.003204`, and a filter running at `k = 10` there pays `0.003414` &mdash; six "
                  "per cent worse for 25 per cent more work."),
            ("h3", "The operation that does not exist"),
            ("p", "A Bloom filter cannot delete. Clearing the `k` bits of a removed key would clear "
                  "bits that other keys had set, and those keys would then be reported "
                  "<em>absent</em> &mdash; a false negative, which is the one answer the structure "
                  "exists never to give. The one-sided error is the whole guarantee, and deletion "
                  "would destroy it rather than degrade it."),
            ("p", "That is also why the structure is used where a certain no is what matters: a "
                  "cheap pre-filter in front of an expensive lookup. Storage Engines and Indexes, "
                  "on the System Design path, puts one in front of a disk read for exactly that "
                  "reason, and the consequence of a false positive there is a wasted read rather "
                  "than a wrong answer."),
            ("p", "The rate is a design parameter and it is computable in advance, which is the "
                  "unusual thing about this structure. Choose the bits per key and `k` and the "
                  "false-positive rate follows exactly; there is no measurement to run and no "
                  "instance-dependence to worry about. What must not happen is quoting the "
                  "idealised figure as the rate when the exact one is available, or quoting either "
                  "without saying which."),
        ],
        "lab": ("hash", {
            "mode": "bloom",
            "preset": "ten-bits",
            "panel_title": "Size the filter, then read the exact rate against the idealised one",
            "panel_intro": (
                "`(1 − (1 − 1/m)^{kn})^k` is computed as a fraction over BigInt, and the familiar "
                "`(1 − e^{−kn/m})^k` is printed beside it as the approximation it is. The gap "
                "between the columns is the independence assumption, and the best `k` is found by "
                "evaluating every one of them rather than from the `(m/n)·ln 2` rule."
            ),
        }),
        "steps_title": "Sizing a filter",
        "steps_intro": "Pick the bits per key first; it is the parameter the rate really depends on.",
        "steps": [
            ("Fix the bits per key, then choose k",
             "The idealised rate depends only on `k` and `m/n`, so the bits per key is the budget "
             "and `k` is the tuning. Ten bits a key with the best `k` gives about one false "
               "positive in 120; eight bits a key gives about one in 46."),
            ("Scan k rather than rounding a formula",
             "`(m/n)·ln 2` lands between integers and rounds in an unstated direction. The panel "
             "evaluates every `k` exactly, and the curve is flat near the optimum and steep to the "
             "left of it, so a guess that is too small costs much more than one that is too large."),
            ("Quote the exact rate, and say so when you quote the other one",
             "`0.008319` and `0.008194` are different numbers and only the first is the expression "
             "this model gives. If the idealisation is what you have, label it; the panel prints "
             "the difference in its own row so the size of the concession is visible."),
            ("Check that a false negative would be acceptable before considering deletion",
             "It would not be, which is why deletion does not exist. If your use needs removal, a "
             "Bloom filter is the wrong structure and a counting variant is a different structure "
             "with a different analysis."),
        ],
        "worked": {
            "title": "The same rate, two ways, at two sizes",
            "intro": [
                "The idealisation depends only on `k` and the bits per key; the exact rate depends "
                "on the actual filter. Here is what that difference looks like when the bits per "
                "key are held fixed and the filter grows.",
            ],
            "lines": [
                "  filter                     exact            idealised      difference",
                "  m = 160, n = 16, k = 7     0.008319         0.008194        1.25e-4",
                "  m = 1000, n = 100, k = 7   0.008214         0.008194        2.0e-5",
                "",
                "  ten bits a key and seven hashes in both cases, so kn/m = 7/10 in both",
                "  the idealised figure is IDENTICAL; the exact one is not",
                "",
                "  this filter, built and queried",
                "    bits set                 74 of 160",
                "    false positives          1 in 200 queries of keys never inserted",
                "    expected, at 0.008319    1.66 in 200",
                "",
                "  best k by exact scan at m = 160, n = 16:  k = 7, rate 0.008319",
                "  the rule of thumb (m/n) ln 2 = 6.93",
            ],
            "after": [
                "The idealised column is the same number twice, because `kn/m` is `0.7` in both "
                "rows. The exact column is not: the smaller filter is genuinely worse, at "
                "`0.008319` against `0.008214`, because `(1 − 1/m)^{kn}` and `e^{−kn/m}` diverge "
                "more when `m` is small. So the approximation hides a real difference between two "
                "filters, and it hides it in the direction of optimism.",
                "Both exact figures sit above the idealisation, which is the general pattern here "
                "and is worth knowing: the idealisation is optimistic. Quoting it as the rate "
                "understates the false-positive rate you will actually see, by a quarter of a per "
                "cent at a thousand bits and by one and a half per cent at 160.",
                "For a faded rehearsal, drop the bits per key to eight and predict what happens to "
                "the best `k` before the panel redraws. The supplied first move is this: the rule "
                "of thumb is `(m/n)·ln 2`, so at eight bits it suggests about `5.5`. Say which "
                "integer the exact scan will choose, then check &mdash; and then say why the rate "
                "at that `k` is nearly three times the ten-bit rate when the space only fell by a "
                "fifth.",
            ],
        },
        "quiz_title": "One-sided error, exactly and idealised",
        "quiz": [
            {"q": "A query finds one of its `k` bits clear. What follows?",
             "a": ["The key is probably absent",
                   "The key was definitely never inserted",
                   "The filter is too small",
                   "Nothing, since bits are shared"],
             "c": 1,
             "why": "Inserting a key sets all `k` of its bits and nothing ever clears a bit, so a "
                    "clear bit is a proof of absence. The error is entirely on the other side: all "
                    "`k` bits set may be the work of other keys. That one-sided structure is why "
                    "deletion is impossible — clearing a bit would manufacture false negatives."},
            {"q": "The panel prints `0.008319` and `0.008194` for the same filter. What is the second number?",
             "a": ["A measurement over the 200 queries the lab ran",
                   "The exact rate, with the first being a bound",
                   "The `(1 − e^{−kn/m})^k` idealisation, which is an approximation of the first",
                   "The rate at the optimal `k` rather than at the chosen one"],
             "c": 2,
             "why": "The exact expression is `(1 − (1 − 1/m)^{kn})^k`, a fraction whose denominator "
                    "has over seventeen hundred digits here. The idealisation replaces "
                    "`(1 − 1/m)^{kn}` by `e^{−kn/m}` and is optimistic. It also depends only on "
                    "`k` and the bits per key, so it is identical for `m = 160, n = 16` and "
                    "`m = 1000, n = 100` while the exact rate is not."},
            {"q": "How does the lab choose the best `k`?",
             "a": ["From `(m/n)·ln 2`, rounded",
                   "By evaluating the exact rate at every `k` from 1 to 10 and taking the smallest",
                   "By measuring false positives at each `k`",
                   "By the point where the idealised and exact rates agree"],
             "c": 1,
             "why": "It scans exactly. The rule of thumb gives `6.93` at ten bits a key and the "
                    "scan confirms `k = 7`, but at twelve bits and twelve keys the scan puts the "
                    "optimum at `8` and the filter in that preset runs at `10`. The curve is flat "
                    "near the minimum and steep on the left, which the table shows directly."},
            {"q": "Why can a Bloom filter not support deletion?",
             "a": ["Because the hash functions are not invertible",
                   "Because clearing a removed key's bits would clear bits other keys set, producing false negatives",
                   "Because the rate formula assumes a fixed `n`",
                   "Because the bit array is immutable"],
             "c": 1,
             "why": "Bits are shared. Clearing the `k` bits of one key can clear a bit that another "
                    "present key relies on, and that key would then be reported absent. A false "
                    "negative is the one answer the structure guarantees never to give, so "
                    "deletion would destroy the guarantee rather than weaken it."},
        ],
        "mistakes": [
            ("Quoting the exponential formula as the false-positive rate",
             "`(1 − e^{−kn/m})^k` is an approximation and it is optimistic: `0.008194` where the "
             "truth is `0.008319`. Worse, it depends only on `k` and the bits per key, so it "
             "reports the same rate for a 160-bit filter and a 1000-bit one when the two genuinely "
             "differ. If the exact expression is available, use it, and if it is not, say which one "
             "you used."),
            ("Reading a measured false-positive count as the rate",
             "One false positive in 200 queries is consistent with a rate of one in 120, where the "
             "expected count is `1.66`, and it is also consistent with a range of nearby rates. Two "
             "hundred queries cannot resolve a rate of that size, and the exact rate is available "
             "without any queries at all."),
            ("Deleting a key by clearing its bits",
             "It is the natural thing to try and it breaks the only guarantee the structure has. "
             "Other keys set some of those bits; after the clear, they are reported absent. A "
             "structure that supports removal is a different structure, with counters instead of "
             "bits and an analysis of its own."),
        ],
        "standard": ("Finish when you can size a filter and state its rate with the right label attached.",
                     "You should be able to derive `(1 − (1 − 1/m)^{kn})^k`, name the idealisation "
                     "that turns it into the textbook formula and say which direction the error "
                     "goes, choose `k` by scanning rather than rounding, and explain why deletion "
                     "is not available."),
        "note": ("A Bloom filter answers a yes-or-no question and its error is one-sided. The last "
                 "lesson of this course answers a how-many question with the same trick &mdash; a "
                 "fixed grid of counters, an estimate that is never below the truth, and a bound "
                 "that is Markov's inequality applied once per row and multiplied."),
    },
    # ---------------------------------------------------------------- 14
    {
        "slug": "the-count-min-sketch",
        "title": "The Count-Min Sketch",
        "module": "Randomness inside the structure",
        "one_line": "Estimate every frequency in a fixed grid of counters, never below the truth, with an error bound that is Markov applied once per row.",
        "summary": (
            "A Count-Min sketch is `d` rows of `w` counters. Each update increments one counter "
            "per row; each estimate is the minimum of a key's `d` counters. The estimate is "
            "never below the truth, because a counter can only be raised by other keys. The "
            "guarantee is Markov's inequality applied per row and multiplied: with `w = 8` and "
            "`d = 3` the error exceeds a quarter of the stream length with probability at most "
            "`1/8`, and on the lab's stream the worst overcount is 2 out of 64 updates."
        ),
        "key": [
            "d rows of w counters; update increments one counter per row",
            "estimate = the minimum of the key's d counters      never below the truth",
            "each row overcounts by F₁/w in expectation      linearity over the other keys",
            "Markov: P(row overcount ≥ 2F₁/w) ≤ 1/2, so d rows give ≤ 2⁻ᵈ",
            "w = 8, d = 3, F₁ = 64:  the bound allows 16, the worst overcount was 2",
            "space is fixed in advance and does not grow with the number of keys",
        ],
        "key_label": "A grid of counters, a one-sided error, and a bound made of Markov",
        "concepts_intro": (
            "The hard idea is that taking a minimum removes the error in one direction "
            "entirely. The other two are where the bound comes from and how loose it is."
        ),
        "concepts": [
            ("The error is one-sided by construction",
             "Key `x` increments one counter per row, so each of its `d` counters is at least its "
             "true count; the other keys that hash to the same cell can only add. Taking the "
             "<strong>minimum</strong> of the `d` counters therefore gives a value at or above the "
             "truth, always, on every stream and every hash choice. The panel checks it on every "
             "key and reports never below the truth rather than assuming it."),
            ("The expected overcount per row is F₁/w, by linearity",
             "Let `F₁` be the total number of updates. In one row, the overcount on key `x` is the "
             "number of updates by other keys landing in `x`'s cell. Each such update lands there "
             "with probability `1/w`, so by linearity the expected overcount is at most `F₁/w`. "
             "That is the same indicator-and-sum argument as &ldquo;Balls in Bins and the Birthday "
             "Bound&rdquo;, with updates in place of keys and counters in place of slots."),
            ("The bound is Markov's, per row, multiplied",
             "Markov's inequality on that overcount at `a = 2F₁/w` gives `P ≥ 2F₁/w) ≤ 1/2` for one "
             "row. The rows use independent hashes, so all `d` rows overcount by that much with "
             "probability at most `2⁻ᵈ`, and the minimum overcounts by that much only if all of "
             "them do. At `w = 8` and `d = 3`: error at most `16` with probability at least `7/8`. "
             "This library proves Markov and not Chernoff, so this is the guarantee it can state."),
        ],
        "read_title": "A fixed grid, a minimum, and a bound this library can prove",
        "read_intro": "The structure, the one-sided error, the Markov guarantee per row, and how far the bound sits from what happens.",
        "body": [
            ("def", ("The sketch",
                     "A <strong>Count-Min sketch</strong> is a `d × w` array of counters, all "
                     "initially zero, with one hash function per row mapping keys to `0..w − 1`. To "
                     "<strong>update</strong> key `x`, increment the counter at "
                     "`(i, hᵢ(x))` in every row `i`. To <strong>estimate</strong> the count of `x`, "
                     "report the minimum of those `d` counters. The space is `d·w` counters, fixed "
                     "in advance, independent of how many distinct keys arrive.")),
            ("p", "That last clause is why the structure exists. An exact frequency table grows with "
                  "the number of distinct keys and a stream can have more of them than you have "
                  "memory for. A sketch has the size you chose when you built it, and the price is "
                  "an error whose size you can bound."),
            ("thm", ("The estimate is never below the truth",
                     "For every key `x`, every stream and every choice of hash functions, the "
                     "reported estimate is at least the true count of `x`.")),
            ("proof", ("Fix a row `i`. Every update of `x` increments the counter at "
                       "`(i, hᵢ(x))`, so that counter is at least the true count of `x`. Every "
                       "other update increments some counter, possibly this one, and counters are "
                       "never decremented, so nothing can bring it below that.",
                       "The estimate is the minimum over `d` such counters, each at or above the "
                       "true count, so it is at or above the true count as well.")),
            ("thm", ("The error bound",
                     "Let `F₁` be the number of updates. For any key `x`, the estimate exceeds the "
                     "true count by at least `2F₁/w` with probability at most `2⁻ᵈ`, provided the "
                     "rows' hash functions are chosen independently and each spreads keys "
                     "uniformly.")),
            ("proof", ("Fix a row and a key `x`. For each update of a key other than `x`, let the "
                       "indicator be `1` if it lands in `x`'s cell in this row. Each has "
                       "expectation at most `1/w`, so by linearity the expected overcount in this "
                       "row is at most `F₁/w`.",
                       "The overcount is non-negative, so Markov's inequality applies: "
                       "`P(overcount ≥ 2F₁/w) ≤ (F₁/w)/(2F₁/w) = 1/2`.",
                       "The rows are independent, and the minimum overcounts by at least `2F₁/w` "
                       "only if every row does, which has probability at most `(1/2)ᵈ = 2⁻ᵈ`.")),
            ("p", "Markov's inequality is doing all the probabilistic work, and it is the "
                  "inequality &ldquo;From an Expectation to a Probability&rdquo; proves. The "
                  "textbook statement of this bound is sharper &mdash; `e/w` in place of `2/w`, and "
                  "`e⁻ᵈ` in place of `2⁻ᵈ` &mdash; and it needs a concentration result this library "
                  "does not teach. So the guarantee here is the one that can be proved with what "
                  "the reader has, and the panel prints `2/w` and `2⁻ᵈ` for that reason rather than "
                  "quoting a stronger claim it cannot support."),
            ("example", ("A heavy hitter in eight counters",
                         "The stream is 64 updates over 12 distinct keys: key 1 arrives forty "
                         "times, keys 2 and 3 arrive three times each, and keys 4 to 12 twice each. "
                         "With `w = 8` and `d = 3` the sketch takes 192 increments and 36 reads. "
                         "Every estimate is at or above the truth; five keys are overcounted, each "
                         "by exactly 2, and the rest are exact. Key 1's estimate is 42 against a "
                         "true 40.")),
            ("p", "The bound allows an error of `2F₁/w = 2·64/8 = 16` with probability up to "
                  "`1/8`, and the worst error observed is `2`. That is a factor of eight of slack "
                  "on this stream, and it is the ordinary situation: Markov is loose, "
                  "&ldquo;From an Expectation to a Probability&rdquo; measured it being loose by "
                  "factors from 2 to nearly 3849, and nothing about this application changes that."),
            ("p", "Notice which keys were overcounted. The heavy hitter was, by 2, and so were four "
                  "of the light keys &mdash; and those light keys were overcounted by the same "
                  "absolute amount, which is a much larger relative error: an estimate of 4 for a "
                  "true count of 2 is out by a factor of two, while 42 for 40 is out by five per "
                  "cent. The bound is additive in `F₁` and says nothing about relative error, which "
                  "is the sketch's real limitation and the reason it is used to find heavy hitters "
                  "rather than to count rare keys."),
            ("h3", "What the parameters buy"),
            ("p", "`w` controls the size of the error and `d` controls the probability of exceeding "
                  "it. Doubling `w` halves `2F₁/w`; adding a row halves `2⁻ᵈ`. They are separate "
                  "knobs and the space is their product, so a sketch with many narrow rows and one "
                  "with few wide rows can occupy the same memory and offer different guarantees."),
            ("p", "The lab's third preset makes the trade visible: `w = 12` and `d = 4` over a "
                  "seeded stream of 64 updates across 12 keys. The bound becomes "
                  "`2F₁/w = 32/3 ≈ 10.67` at a failure probability of `1/16`, and every estimate "
                  "came out exactly right &mdash; worst overcount `0`. A wider sketch on the same "
                  "amount of data collides less; the bound improved and the actual error improved "
                  "more."),
            ("p", "And when nothing collides the sketch is exact. The uniform preset &mdash; ten "
                  "keys, six updates each &mdash; has a worst overcount of `0` at `w = 8` and "
                  "`d = 3`, so every estimate equals its truth. That is not the sketch being right "
                  "about the stream in general; it is this stream's keys happening to miss each "
                  "other in at least one row each, and a different hash choice would give a "
                  "different table."),
            ("h3", "Three numbers, one last time"),
            ("p", "The exact quantities here are `2F₁/w` and `2⁻ᵈ`, which are fractions computed "
                  "from the parameters. The measurement is the worst overcount on the stream on "
                  "screen, which is `2` on the opening preset and `0` on the other two. The bound "
                  "is the pair of exact quantities read as a guarantee, and it covers streams "
                  "nobody has run. The course ends where it began: those are three kinds of number "
                  "and the page prints all three."),
        ],
        "lab": ("hash", {
            "mode": "countmin",
            "preset": "heavy-hitter",
            "panel_title": "Push a stream through the grid and compare every estimate with the truth",
            "panel_intro": (
                "Every estimate is the minimum of the key's `d` counters, so the panel can check "
                "that none of them falls below the truth. `2F₁/w` and `2⁻ᵈ` are exact fractions "
                "from the parameters and are the Markov guarantee this library can prove; the worst "
                "overcount beside them is a count on the stream shown."
            ),
        }),
        "steps_title": "Reading a sketch",
        "steps_intro": "Check the direction of the error first, then its size, then its probability.",
        "steps": [
            ("Confirm the estimates are never below the truth",
             "This holds always and by construction, and the panel verifies it key by key rather "
             "than asserting it. If it ever failed, the defect would be in the implementation "
             "rather than in the analysis."),
            ("Compute the additive error the parameters allow",
             "`2F₁/w`. At 64 updates and eight counters a row that is 16, which is a quarter of the "
             "whole stream &mdash; large. The bound is about a worst case over streams, and on the "
             "stream shown the worst error is 2."),
            ("Read the failure probability off d, separately",
             "`2⁻ᵈ`. Three rows give `1/8`. Adding a row halves it and costs `w` counters, and "
             "widening the rows shrinks the error instead. Decide which of the two you need before "
             "spending the space."),
            ("Ask whether you care about absolute or relative error",
             "The bound is additive in `F₁`, so a key with a true count of 2 can be reported as 4 "
             "and stay well inside it. Sketches find heavy hitters; they are not a way to count "
               "rare keys accurately, and the opening preset shows both cases in one table."),
        ],
        "worked": {
            "title": "Sixty-four updates through a three-by-eight grid",
            "intro": [
                "Key 1 forty times; keys 2 and 3 three times each; keys 4 to 12 twice each. Three "
                "rows of eight counters. Every estimate is the minimum of that key's three "
                "counters.",
            ],
            "lines": [
                "key   true   estimate   overcount",
                "  1     40      42          2",
                "  2      3       3          0",
                "  3      3       5          2",
                "  4      2       4          2",
                "  5      2       2          0",
                "  6      2       2          0",
                "  7      2       2          0",
                "  8      2       2          0",
                "  9      2       2          0",
                " 10      2       4          2",
                " 11      2       4          2",
                " 12      2       2          0",
                "",
                "  every estimate at or above the truth        yes, all 12",
                "  worst overcount                            2",
                "  updates F1 = 64,  writes 192,  reads 36",
                "",
                "  the guarantee, from the parameters alone",
                "    eps = 2/w = 1/4,  so the allowed error is 2F1/w = 16",
                "    delta = 2^-d = 1/8",
                "  so: error at most 16, with probability at least 7/8",
                "  observed: error at most 2",
            ],
            "after": [
                "The bound allows 16 and the worst error is 2. That is Markov being Markov, and it "
                "is the third time on this course that the same inequality has come in loose by "
                "roughly an order of magnitude. It is still the guarantee, because it holds for "
                "streams nobody has run, and the 2 holds only for this one.",
                "Compare key 1 and key 4. Both are overcounted by 2. For key 1 that is an estimate "
                "of 42 against 40, five per cent out; for key 4 it is 4 against 2, a factor of two. "
                "The bound is additive and does not distinguish them, which is precisely why the "
                "structure is used to find the keys with large counts and not to report the small "
                "ones.",
                "For a faded rehearsal, set the rows to 4 and predict what moves before the panel "
                "redraws. The supplied first move is this: `d` appears in `2⁻ᵈ` and not in "
                "`2F₁/w`, so one of the two guarantee figures changes and the other does not. Say "
                "which, say what the new value is, and then say what would have to change instead "
                "to shrink the allowed error from 16.",
            ],
        },
        "quiz_title": "Minimums, bounds, and which error is bounded",
        "quiz": [
            {"q": "Why is a Count-Min estimate never below the truth?",
             "a": ["Because the hash functions are universal",
                   "Because each of the key's counters is incremented by every one of its updates and counters are never decremented, so each is at least the true count",
                   "Because the minimum of `d` values is at least their average",
                   "Because `d` is odd"],
             "c": 1,
             "why": "Every update of `x` raises `x`'s counter in every row, and other keys can only "
                    "raise it further. So each of the `d` counters is at or above the truth and so "
                    "is their minimum. The property holds always — for every stream and every hash "
                    "choice — which is why the panel can check it rather than bound it."},
            {"q": "The guarantee on the panel is `2F₁/w` with probability `2⁻ᵈ`. Where does it come from?",
             "a": ["A Chernoff bound on the per-row overcount",
                   "Markov's inequality on each row's overcount at twice its mean, and independence across rows",
                   "The birthday bound",
                   "A measurement over the streams the lab ran"],
             "c": 1,
             "why": "The expected overcount per row is at most `F₁/w` by linearity over the other "
                    "updates; Markov at twice that mean gives a per-row failure probability of a "
                    "half; independent rows multiply to `2⁻ᵈ`. The sharper textbook version with "
                    "`e/w` and `e⁻ᵈ` needs a concentration bound this library does not teach."},
            {"q": "On the opening stream, keys 1 and 4 are both overcounted by 2. Why does that matter?",
             "a": ["It does not: the bound covers both",
                   "The bound is additive in `F₁`, so the same absolute error is five per cent for a count of 40 and a factor of two for a count of 2",
                   "Key 4's estimate violates the bound",
                   "It shows the hash functions are not independent"],
             "c": 1,
             "why": "Both are well inside the allowed 16, so the bound is satisfied. But an "
                    "additive guarantee says nothing about relative error, and a light key can be "
                    "doubled while a heavy one is barely disturbed. That is why sketches are used "
                    "to find heavy hitters rather than to count rare keys."},
            {"q": "You want to halve the allowed additive error. What do you change?",
             "a": ["Add a row, since `d` controls the error",
                   "Double `w`, since the error is `2F₁/w` and `d` only controls the failure probability",
                   "Halve the stream length",
                   "Either one: the two parameters are interchangeable"],
             "c": 1,
             "why": "`w` appears in `2F₁/w` and `d` appears in `2⁻ᵈ`. Doubling the row width halves "
                    "the error; adding a row halves the probability of exceeding it. They are "
                    "separate knobs that happen to multiply into the same space budget, which is "
                    "the design decision the panel's two sliders expose."},
        ],
        "mistakes": [
            ("Expecting the estimate to be close, rather than never low",
             "The guarantee is one-sided and additive: never below the truth, and above it by at "
             "most `2F₁/w` with high probability. On the opening stream that allowance is 16 out of "
             "64 updates. An estimate that is exactly right, as most of them are here, is this "
             "stream being kind rather than the structure promising accuracy."),
            ("Quoting the sharper textbook bound",
             "`e/w` and `e⁻ᵈ` are the numbers most references give, and their proof needs a "
             "concentration result no Subject in this library teaches. Using them here would be "
             "quoting a guarantee the reader cannot derive from anything they have been shown. The "
             "panel prints `2/w` and `2⁻ᵈ`, which follow from Markov's inequality in three lines."),
            ("Reading an exact table as evidence that the sketch is exact",
             "Two of the lab's three presets have a worst overcount of zero, and neither says "
             "anything about the next stream. Those are streams whose keys missed each other in at "
             "least one row apiece. Change the width, the depth or the stream and collisions "
             "return; the guarantee is the thing that does not change."),
        ],
        "standard": ("Finish when you can derive the guarantee from Markov's inequality and say which error it bounds.",
                     "You should be able to describe update and estimate, prove the estimate is "
                     "never below the truth, derive `2F₁/w` and `2⁻ᵈ` from linearity and Markov, "
                     "say which parameter moves which figure, and explain why an additive bound is "
                     "no use for a rare key."),
        "note": ("That is the course. Three kinds of number appeared on every page &mdash; the "
                 "exact quantity over every execution, the measurement over the seeds shown, and "
                 "the proved bound &mdash; and the three guarantees a randomised algorithm can "
                 "offer were always, with high probability, and in expectation. Intractability and "
                 "Approximation takes the probabilistic method from here to prove that "
                 "approximations exist, and reuses the same discipline about what a measured number "
                 "on one instance can establish."),
    },
]
