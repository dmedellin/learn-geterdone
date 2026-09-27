"""Greedy Algorithms and Matroids, lessons 06-10 - matroids, and three guarantees.

As in the first part file, every figure here was read off the shipped lab by
extracting the `*_JS` blocks and executing them under node, not reasoned about.
Three of the presets used in these five lessons carry a recorded `note` or
`label` that the run contradicts, and each of the three is named in the prose
that quotes it: those strings reach the reader in the status line and nothing
in the build has ever checked them.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "independence-systems-and-matroids",
        "title": "Independence Systems and Matroids",
        "module": "Matroids",
        "one_line": "Define a family of feasible sets by a membership test, list it by running that test on every subset, and decide whether it satisfies the exchange property.",
        "summary": (
            "Three of the algorithms on this course are greedy and optimal, each proved its own "
            "way. There is a single condition on the family of feasible sets that explains all "
            "three, and it is not &ldquo;the problem looks like scheduling&rdquo;. The lab gives "
            "four families as membership tests, lists each by asking the test about every "
            "subset, and then tests the exchange property on every ordered pair of independent "
            "sets. Three of the four pass. One does not, and it is the one with three elements."
        ),
        "key": [
            "independence system: nonempty, and closed downward — a subset of a feasible set is feasible",
            "exchange: |A| < |B|  ⟹  some x in B \\ A has A + x still independent",
            "matroid = independence system + exchange",
            "forests of 1-2, 2-3, 3-1, 3-4, 1-4:  24 of 32 subsets, rank 3, 8 bases, 193 pairs",
            "uniform (any two of five): 16 sets, rank 2, 10 bases, 65 pairs",
            "matchings of the path 1-2, 2-3, 3-4: 5 sets, 7 pairs, ONE failure — not a matroid",
        ],
        "key_label": "Two conditions, four families, and the pair that breaks one of them",
        "concepts_intro": (
            "Three ideas: why a family is given by a test rather than by a list, what downward "
            "closure buys before the exchange property is even asked about, and what the "
            "exchange property actually says."
        ),
        "concepts": [
            ("A family is defined by a membership test, because that is the definition",
             "An independence oracle answers one question: is this set independent? The four "
             "families here are exactly that &mdash; a rank test, a cycle test, a "
             "one-per-group test, a shared-vertex test &mdash; and the panel produces the "
             "family by asking the oracle about all `2ⁿ` subsets. Nothing is labelled a "
             "matroid anywhere in the kit; the family is enumerated from the test, and the "
             "properties are then checked on what came out."),
            ("Downward closure is a separate and earlier requirement",
             "Greedy needs to be able to stop. If dropping an element from a feasible set could "
             "make it infeasible, then a rule that adds elements one at a time has no invariant "
             "to maintain. <strong>Downward closed</strong> says every subset of an independent "
             "set is independent, and it is what makes the family an <em>independence "
             "system</em>. All four families here satisfy it, including the one that is not a "
             "matroid, so it is genuinely the weaker condition."),
            ("The exchange property is about sizes, not about elements",
             "If `A` and `B` are independent and `A` is strictly smaller than `B`, then some "
             "element of `B` not already in `A` can be added to `A` keeping it independent. "
             "Note what it does not say: not that any particular element works, not that `A` "
             "can be grown to `B`'s size in one step, and not that `A` is contained in "
             "anything. The panel tests every ordered pair with `|A| &lt; |B|`, which is 193 "
             "pairs on the opening family and 7 on the smallest one."),
        ],
        "read_title": "Two axioms, four families, and one counterexample",
        "read_intro": "The definitions, the four families given as oracles, what the exchange test finds, and why the graphic case is a course you have already taken.",
        "body": [
            ("def", ("Independence system",
                     "A pair `(E, I)` where `E` is a finite ground set and `I` is a collection "
                     "of subsets of `E`, called <strong>independent</strong>, such that `I` is "
                     "nonempty and <strong>downward closed</strong>: if `B` is in `I` and "
                     "`A ⊆ B` then `A` is in `I`. A maximal independent set is called a "
                     "<strong>basis</strong>; the size of a largest one is the "
                     "<strong>rank</strong>.")),
            ("def", ("Matroid",
                     "An independence system `(E, I)` satisfying the <strong>exchange "
                     "property</strong>: whenever `A` and `B` are independent with "
                     "`|A| &lt; |B|`, there is an element `x` in `B` but not in `A` such that "
                     "`A ∪ {x}` is independent.")),
            ("p", "One consequence is worth stating immediately, because it is what the "
                  "counterexample later violates: in a matroid every basis has the same size. "
                  "If two maximal independent sets had different sizes, the exchange property "
                  "applied to the smaller and the larger would produce an element extending the "
                  "smaller one, contradicting its maximality."),
            ("p", "The lab opens on the forests of a four-vertex graph with edges `1-2`, `2-3`, "
                  "`3-1`, `3-4`, `1-4`, labelled `A` to `E` in that order. A set of edges is "
                  "independent when it contains no cycle. The oracle is asked about all 32 "
                  "subsets and accepts 24 of them; the rank is 3, there are 8 bases, and the "
                  "family is downward closed &mdash; dropping an edge from a forest leaves a "
                  "forest."),
            ("example", ("The exchange property on 193 pairs",
                         "The panel forms every ordered pair `(A, B)` of independent sets with "
                         "`|A| &lt; |B|` &mdash; 193 of them on this family &mdash; and for "
                         "each asks whether some element of `B` can join `A`. Every one of the "
                         "193 succeeds, so the forests of this graph form a matroid. The 8 "
                         "bases are its spanning trees, and every one of them has 3 edges, "
                         "which is `|V| − 1` for a connected graph on four vertices.")),
            ("h3", "Greedy on this family is an algorithm you already know"),
            ("p", "Sort the elements by weight and add each one if it keeps the set "
                  "independent. On the forests of a graph that is Kruskal's algorithm. The one "
                  "difference from the version proved in the graph course is the direction: "
                  "matroid greedy maximises, so it sorts heaviest first and builds a maximum "
                  "spanning tree. With weights `8 6 5 4 2` it takes `A`, takes `B`, rejects `C` "
                  "because `1-2`, `2-3` and `3-1` would close a cycle, takes `D`, rejects `E`, "
                  "and finishes with `{A, B, D}` worth 18 &mdash; the best any independent set "
                  "can do."),
            ("p", "That is the point of the whole construction. The cut property gave a proof "
                  "of Kruskal that is about graphs: lightest edge crossing a cut, cycles, "
                  "connectivity. The matroid theorem gives a proof that is about the family of "
                  "feasible sets and mentions no graph at all, and the same proof then covers "
                  "families that have nothing to do with graphs."),
            ("h3", "Two more matroids, and one family that is not"),
            ("p", "The <strong>uniform</strong> family takes every subset of at most `k` "
                  "elements from a ground set of five. With `k = 2` that is 16 sets, rank 2, "
                  "and all 10 pairs are bases; 65 ordered pairs are tested and none fails. The "
                  "<strong>partition</strong> family allows at most one element from each "
                  "group; with groups `1 1 2 2 3` that is 18 sets, rank 3, 4 bases, 109 pairs, "
                  "and no failure. Greedy with weights `7 6 5 4 3` takes the heaviest element "
                  "of each group, `{A, C, E}`, worth 15."),
            ("example", ("The matchings of a path are not a matroid",
                         "Ground set: the three edges `1-2`, `2-3`, `3-4` of a path, labelled "
                         "`A`, `B`, `C`. A set is independent when no two of its edges share a "
                         "vertex. The oracle accepts 5 of the 8 subsets: the empty set, each "
                         "single edge, and `{A, C}`. The family is downward closed. Of the 7 "
                         "ordered pairs tested, exactly one fails: `A = {B}` and `B = {A, C}`. "
                         "Neither end can join the middle edge, because each shares a vertex "
                         "with it.")),
            ("p", "So this family has two maximal independent sets of different sizes: `{B}`, "
                  "which cannot be grown, and `{A, C}`, which is the only basis. That is the "
                  "same statement as the exchange failure, and it is the first place on this "
                  "course where the shape of the feasible family, rather than the rule, is "
                  "what goes wrong."),
            ("p", "It is also the smallest possible instance. Two elements cannot produce a "
                  "failure &mdash; with `|A| &lt; |B| ≤ 2` and downward closure, the singleton "
                  "inside `B` is available &mdash; so three elements is where a "
                  "non-matroid independence system can first appear, and a path with three "
                  "edges is the one everybody meets first."),
            ("p", "Measured on this page: 24 independent sets of 32 for the forests, rank 3, "
                  "8 bases, 193 exchange pairs and 0 failures; 5 independent sets of 8 for the "
                  "matchings, 7 pairs and 1 failure. Proved on this page: in any matroid all "
                  "bases have the same size, which the matchings family visibly violates. What "
                  "is not on this page is the reason any of this predicts whether greedy works "
                  "&mdash; that is a theorem in both directions, and it is next."),
        ],
        "lab": ("greedy", {
            "mode": "matroid",
            "preset": "graphic",
            "panel_title": "Choose the family, and see it listed from its own oracle",
            "panel_intro": "The family is defined by a membership test and produced by running "
                           "that test on every subset, so nothing here is labelled a matroid in "
                           "advance. The exchange property is then tested on every ordered pair "
                           "of independent sets and the failures, if any, are listed.",
        }),
        "steps_title": "Deciding whether a family is a matroid",
        "steps_intro": "Four steps, in this order. The second catches more candidate families than the third does.",
        "steps": [
            ("Write the membership test, not the list",
             "A family is only as clear as the predicate that defines it. &ldquo;Edge sets with "
             "no cycle&rdquo;, &ldquo;at most one from each group&rdquo;, &ldquo;no two sharing "
             "a vertex&rdquo;: each is a test you can apply to a set handed to you, and the "
             "list follows from it rather than the other way round."),
            ("Check downward closure first",
             "It is cheaper than the exchange test and it fails more often in practice. If "
             "removing an element can break feasibility, the family is not an independence "
             "system and no greedy rule has an invariant to maintain. All four families in the "
             "lab pass this and one of them still fails the next step, which is why they are "
             "separate conditions."),
            ("Look for two maximal sets of different sizes",
             "This is the fast way to refute the exchange property by hand. Any independence "
             "system with two maximal independent sets of different sizes fails it, and the "
             "smaller one is half of the counterexample. On the matchings family, `{B}` is "
             "maximal with one element and `{A, C}` is maximal with two."),
            ("Only then test every ordered pair",
             "The full test is quadratic in a family that is itself exponential, which is why "
             "the panel caps the ground set at six elements and says so. When it runs, it "
             "reports the number of pairs tested and lists the failures, so a passing family "
             "comes with the size of the evidence attached."),
        ],
        "worked": {
            "title": "The matchings of a three-edge path, by hand",
            "intro": [
                "Ground set `A = 1-2`, `B = 2-3`, `C = 3-4`. A set of edges is independent when "
                "no two of them share a vertex. There are eight subsets; test each.",
            ],
            "lines": [
                "   subset      shares a vertex?                 independent",
                "   {}          nothing to share                 yes",
                "   {A}         -                                yes",
                "   {B}         -                                yes",
                "   {C}         -                                yes",
                "   {A,B}       both use vertex 2                no",
                "   {B,C}       both use vertex 3                no",
                "   {A,C}       1,2 and 3,4 are disjoint         yes",
                "   {A,B,C}     contains {A,B}                   no",
                "",
                "family        5 of the 8 subsets",
                "downward closed?   yes - every subset of an independent set is listed",
                "rank          2, attained only by {A,C}, so there is 1 basis",
                "maximal sets  {A,C} of size 2, and {B} of size 1",
                "",
                "exchange test   7 ordered pairs with |A| < |B|; one fails:",
                "   A = {B},  B = {A,C}     A shares vertex 2 with B, C shares vertex 3",
                "   nothing in {A,C} can join {B}, so the property fails",
            ],
            "after": [
                "Two maximal independent sets of different sizes is the whole failure, said "
                "twice. The set `{B}` cannot be extended and is not a basis, so &ldquo;maximal "
                "independent set&rdquo; and &ldquo;maximum independent set&rdquo; are different "
                "things here &mdash; and in a matroid they are the same thing, which is why the "
                "distinction never came up on the previous page.",
                "The uniform, graphic and partition families all pass the same test: 65, 193 and "
                "109 ordered pairs respectively, with no failures. Three passes and one failure "
                "on four families is not a survey; what makes the failure interesting is that "
                "the theorem coming next makes it predictive rather than merely true.",
                "For a faded rehearsal, work out the independent sets of the matchings of a "
                "four-edge path, `1-2, 2-3, 3-4, 4-5`, before running it. The supplied first "
                "move is that `{A, C}`, `{A, D}` and `{B, D}` are all independent and none of "
                "the three can be extended, so on that path every maximal independent set does "
                "have the same size. Say how many independent sets there are in all, how many "
                "ordered pairs the exchange test forms, and whether the property still fails "
                "&mdash; and then say which single edge you could delete to turn the family "
                "into a matroid.",
            ],
        },
        "quiz_title": "Systems, matroids, and what the pair test finds",
        "quiz": [
            {"q": "The matchings family is downward closed and fails the exchange property. What does that make it?",
             "a": ["Neither an independence system nor a matroid",
                   "An independence system that is not a matroid",
                   "A matroid whose rank function is wrong",
                   "A matroid, since downward closure is the definition"],
             "c": 1,
             "why": "Downward closure plus nonemptiness is exactly an independence system, and "
                    "the panel confirms it. Matroid needs the exchange property on top, and the "
                    "pair `{B}` against `{A, C}` refutes it. The two conditions are separate, "
                    "which is why the panel reports them separately."},
            {"q": "In a matroid, why must every basis have the same size?",
             "a": ["Because the rank function is defined as the size of a basis",
                   "Because the exchange property applied to a smaller maximal set and a larger one would extend the smaller, contradicting maximality",
                   "Because the ground set is finite",
                   "Because downward closure forces it"],
             "c": 1,
             "why": "It is a consequence of the exchange property, not a definition and not a "
                    "consequence of closure. The matchings family is downward closed, finite, "
                    "and has maximal sets of sizes 1 and 2, which is the same failure viewed "
                    "differently."},
            {"q": "Greedy over the forests of the opening graph with weights `8 6 5 4 2` returns `{A, B, D}` worth 18. Which algorithm is that?",
             "a": ["Prim's algorithm started at vertex 1",
                   "Kruskal's algorithm, sorted heaviest first, so it builds a maximum spanning tree",
                   "A depth-first walk that skips back edges",
                   "Kruskal's algorithm, which always minimises"],
             "c": 1,
             "why": "Sort by weight and add an element when the set stays independent is exactly "
                    "Kruskal. Matroid greedy maximises, so the sort is descending and the "
                    "result is a maximum spanning tree; the same algorithm with an ascending "
                    "sort gives the minimum one. Prim grows from a vertex and is a different "
                    "schedule."},
            {"q": "Why does the panel enumerate the family from the oracle rather than shipping the list of independent sets?",
             "a": ["Because the list would be too large to store",
                   "Because a membership test is the definition, and a shipped list could disagree with the test that is supposed to define it",
                   "Because the oracle is faster",
                   "Because the exchange test needs the sets in a particular order"],
             "c": 1,
             "why": "A family given as a list is a family nobody can check. Asking the oracle "
                    "about every subset means the listed family is by construction exactly the "
                    "sets the test accepts, and the panel additionally re-checks each listed "
                    "set against the oracle. At six elements the list is 64 subsets, so size is "
                    "not the issue."},
        ],
        "mistakes": [
            ("Treating downward closure as the whole definition",
             "It is the easier half and it is not the one that makes greedy work. The matchings "
             "family passes it and greedy still loses on it. A candidate family that is "
             "downward closed has earned the right to be tested, not the label."),
            ("Confusing maximal with maximum",
             "A maximal independent set cannot be extended; a maximum one is as large as any. "
             "In a matroid they coincide, which is convenient and is exactly the property being "
             "tested. Outside a matroid they do not: `{B}` in the matchings family is maximal "
             "and has one element, while the maximum has two."),
            ("Reading three passing families as a general rule",
             "Uniform, graphic and partition are all matroids, tested on 65, 193 and 109 pairs, "
             "and none of that predicts the next family. Independence systems are far more "
             "common than matroids; the lab ships three of the latter because they are the "
             "three that recur, not because the ratio means anything."),
        ],
        "standard": ("Finish when you can take a family described in words, write its membership test, and decide by hand whether it is a matroid.",
                     "You should be able to state both axioms, list a small family from its "
                     "oracle, produce the two maximal sets of different sizes when a family "
                     "fails, explain why matroid greedy on the forests of a graph is Kruskal "
                     "with the sort reversed, and say what downward closure buys before the "
                     "exchange property is asked about."),
        "note": ("Defining a condition is not the same as showing it matters. What makes the "
                 "exchange property the right condition is a theorem in both directions: "
                 "greedy is optimal for <em>every</em> weighting exactly when the family is a "
                 "matroid. &ldquo;Greedy for Every Weighting&rdquo; states it, and the lab "
                 "searches for the weighting that beats greedy rather than asserting that one "
                 "exists."),
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "greedy-for-every-weighting",
        "title": "Greedy for Every Weighting",
        "module": "Matroids",
        "one_line": "State the theorem in both directions, then watch the lab sweep every weighting and either find the one that beats greedy or report that none exists.",
        "summary": (
            "Rado and Edmonds: greedy is optimal for every weight function exactly when the "
            "family of feasible sets is a matroid. Both directions matter and the second is the "
            "one with teeth &mdash; a family that is not a matroid always has a weighting on "
            "which greedy loses. The lab does not quote that; it searches `{1, 2, 3}ⁿ` and "
            "returns the first weighting that works, which on the three-element non-matroid is "
            "the thirteenth of twenty-seven."
        ),
        "key": [
            "Rado–Edmonds: greedy optimal for EVERY weighting  ⟺  the family is a matroid",
            "matchings of a path: not a matroid, and the 13th of the 27 weightings beats greedy",
            "weights 1 2 2 → greedy takes the middle edge for 2; {ends} is worth 3",
            "uniform, graphic, partition: all 243 weightings tried, greedy optimal on every one",
            "the shipped weights 2 3 2 already beat greedy: 3 against 4",
            "one weighting where greedy wins is not the theorem; every weighting is",
        ],
        "key_label": "One theorem, two directions, and a search instead of an assertion",
        "concepts_intro": (
            "Three ideas: what quantifying over weightings changes, why the converse is the "
            "useful half, and why a search that stops at the first counterexample is the right "
            "thing for a panel and the wrong thing for a check."
        ),
        "concepts": [
            ("The quantifier is over weightings, and it is the whole statement",
             "Greedy can be optimal on a non-matroid for a particular weighting, and often is. "
             "On the matchings of a path with weights `3 1 3` the ends are heaviest, greedy "
             "takes both, and it is optimal. The theorem is not about a weighting; it says the "
             "family is a matroid exactly when <em>no</em> weighting defeats greedy. A single "
             "successful run tells you about that run."),
            ("The converse is what makes the condition useful",
             "&ldquo;Matroid implies greedy works&rdquo; licenses an algorithm. &ldquo;Greedy "
             "works for all weightings implies matroid&rdquo; is what lets you rule a problem "
             "out: show that the feasible sets have two maximal sets of different sizes and you "
             "have proved that some weighting defeats every greedy rule of this shape, without "
             "having to find it. The lab then finds it anyway, because a counterexample you can "
             "read is worth more than one you know exists."),
            ("A first counterexample and a full sweep answer different questions",
             "`beatingWeights` walks `{1, 2, 3}ⁿ` in a fixed order and stops at the first "
             "weighting where greedy loses, reporting how many it tried. That is right for a "
             "reader: it makes the counterexample reproducible. It is wrong as a check, because "
             "stopping early cannot establish that a matroid has none &mdash; for that the "
             "whole space has to be walked, and on five elements that is 243 weightings."),
        ],
        "read_title": "The theorem, and the weighting the lab goes and finds",
        "read_intro": "Both directions with proofs, the counterexample search, and the reason the number thirteen on this page is a fact about a walk order rather than about matroids.",
        "body": [
            ("def", ("Greedy on an independence system",
                     "Given an independence system `(E, I)` and non-negative weights `w`, sort "
                     "`E` in decreasing weight and walk it once, adding each element when the "
                     "set so far plus that element is still independent. The result is a "
                     "maximal independent set; the question is whether it is a maximum-weight "
                     "one.")),
            ("thm", ("Rado and Edmonds",
                     "Let `(E, I)` be an independence system. Greedy returns a maximum-weight "
                     "independent set for every non-negative weight function `w` if and only if "
                     "`(E, I)` is a matroid.")),
            ("proof", ("Suppose first that `(E, I)` is a matroid and let `G` be greedy's answer "
                       "and `O` a maximum-weight independent set. Both are bases, so they have "
                       "the same size `r`. List each in decreasing weight, `g₁ ≥ g₂ ≥ … ≥ g_r` "
                       "and `o₁ ≥ o₂ ≥ … ≥ o_r`. The claim is that `w(gᵢ) ≥ w(oᵢ)` for every "
                       "`i`, which gives `w(G) ≥ w(O)` at once.",
                       "Suppose not, and take the least `i` with `w(gᵢ) &lt; w(oᵢ)`. Let "
                       "`A = {g₁, …, g_(i−1)}` and `B = {o₁, …, oᵢ}`, both independent by "
                       "downward closure, with `|A| &lt; |B|`. By the exchange property some "
                       "`x` in `B \\ A` has `A ∪ {x}` independent, and `w(x) ≥ w(oᵢ) &gt; "
                       "w(gᵢ)`. But greedy, having chosen `A`, would have reached `x` before "
                       "`gᵢ` and taken it. Contradiction.",
                       "For the converse, suppose the exchange property fails for some "
                       "independent `A` and `B` with `|A| &lt; |B|`, chosen with `|A|` as large "
                       "as possible among failures, and write `a = |A|`. Give every element of "
                       "`A` weight `a + 2`, every element of `B \\ A` weight `a + 1`, and "
                       "everything else weight 0. Greedy takes all of `A` first, then can add "
                       "nothing from `B \\ A` by assumption, so it collects at most "
                       "`a(a + 2)` from the weighted elements; `B` alone is worth at least "
                       "`(a + 1)²`, which is larger. So greedy is not optimal for that "
                       "weighting.")),
            ("p", "The converse is constructive, which is worth noticing: it does not merely "
                  "assert that a bad weighting exists, it builds one out of the failing pair. "
                  "On the matchings of a path with `A = {B}` and `B = {A, C}`, that recipe gives "
                  "the middle edge weight 3 and the two ends weight 2 each, and greedy takes the "
                  "middle for 3 against 4."),
            ("p", "Which is exactly the weighting the lab ships as that family's default: "
                  "`2 3 2`. Greedy takes the middle edge, worth 3, and the best independent set "
                  "is the pair of ends, worth 4. So the reader meets a counterexample before "
                  "reading the proof that guarantees one, and the panel reports the gap as a "
                  "measurement rather than as an illustration."),
            ("h3", "The search, and the number thirteen"),
            ("p", "The panel then does something the proof does not: it walks every weighting in "
                  "`{1, 2, 3}ⁿ` in a fixed order and stops at the first one on which greedy is "
                  "beaten. On the three-element family that space has 27 weightings, and the "
                  "search stops after 13 of them, at `1 2 2`. Greedy takes the middle edge for "
                  "2; the two ends are worth 3 together."),
            ("p", "Thirteen is a fact about the enumeration order and nothing else. It is not a "
                  "measure of how badly the family fails, not a property of matroids, and not "
                  "stable under relabelling the elements. What is a fact about the family is "
                  "that the search terminates at all, which the converse guarantees for every "
                  "non-matroid, and that its answer is a concrete triple a reader can type back "
                  "into the weights box."),
            ("h3", "The other direction, swept rather than sampled"),
            ("p", "On each of the three families that are matroids the panel walks the whole "
                  "space: all `3⁵ = 243` weightings in `{1, 2, 3}⁵`, with greedy compared "
                  "against the best member of the family on each. None of the 243 beats greedy "
                  "on the uniform family, none on the graphic family, none on the partition "
                  "family. The panel reports that it tried all of them, because &ldquo;no "
                  "counterexample found&rdquo; and &ldquo;the whole space was searched&rdquo; "
                  "are different sentences and only the second is worth printing."),
            ("p", "It is still a sample. `{1, 2, 3}ⁿ` is 243 of the infinitely many weight "
                  "functions on five elements, and a family could in principle survive all of "
                  "them and fail on `{1, 2, 4}`. The theorem is what rules that out, and the "
                  "sweep is what would catch an implementation that had drifted away from the "
                  "theorem. Neither replaces the other."),
            ("p", "One detail of the sweep is worth a sentence because it decides a tie. With "
                  "weights `1 2 2` the two heaviest elements are tied, and greedy takes the "
                  "middle edge rather than an end. Change the order in which ties are broken "
                  "and greedy would take an end, then the other end, and reach 3 &mdash; the "
                  "optimum. A counterexample to a greedy rule can depend on the tie-break, and "
                  "the panel's is fixed, stated by the trace it prints, and part of the "
                  "algorithm rather than an accident of it."),
            ("p", "Measured on this page: 27 weightings in the space for the matchings family, "
                  "13 tried before one beat greedy, `1 2 2`, giving 2 against 3; 243 weightings "
                  "each for the three matroids, all tried, none beating greedy. Proved on this "
                  "page: greedy is optimal for every non-negative weight function exactly when "
                  "the family is a matroid. The sweep is 243 points and the theorem is every "
                  "point, and this is the page on the course where that gap is smallest and "
                  "still absolute."),
        ],
        "lab": ("greedy", {
            "mode": "matroid",
            "preset": "matchings",
            "panel_title": "The family that is not a matroid, and the weighting that proves it",
            "panel_intro": "The panel searches for a weighting on which greedy loses and prints "
                           "the one it finds, how many of the space it tried, and what the two "
                           "answers are worth. Switch to any of the other three families and it "
                           "reports instead that the whole space was tried and greedy won "
                           "everywhere.",
        }),
        "steps_title": "Using the theorem in both directions",
        "steps_intro": "Four steps. The first two decide the question; the last two are what make the answer usable by someone else.",
        "steps": [
            ("Identify the family of feasible sets, separately from the objective",
             "The theorem is about `(E, I)`. Weights are a separate input and the whole content "
             "of the statement is that they do not matter when the family is a matroid. A "
             "problem description that mixes the two &mdash; &ldquo;pick the heaviest "
             "non-conflicting set&rdquo; &mdash; hides the object being tested."),
            ("Test the exchange property, and stop if it passes",
             "A matroid needs no further argument: greedy is optimal for every weighting, "
             "including ones nobody will ever supply. This is the direction that licenses an "
             "algorithm, and it is the reason the previous page's pair test is worth running."),
            ("If it fails, build the counterexample from the failing pair",
             "The converse's recipe is explicit: weight `A` at `|A| + 2`, weight `B \\ A` at "
             "`|A| + 1`, weight everything else 0. On the matchings of a path that gives "
             "`2 3 2`, which is the family's shipped weighting and beats greedy by 3 to 4."),
            ("Report the weighting, not the existence of one",
             "&ldquo;Some weighting defeats greedy&rdquo; is a citation. &ldquo;Weights 1, 2, 2 "
             "give greedy 2 where the optimum is 3&rdquo; is a counterexample a reader can "
             "check in ten seconds. The panel prints the second and prints how much of the "
             "space it had to look at to get there."),
        ],
        "worked": {
            "title": "Both sides of the theorem on the three-edge path",
            "intro": [
                "The family: subsets of `A = 1-2`, `B = 2-3`, `C = 3-4` with no two edges "
                "sharing a vertex. Independent sets: `{}`, `{A}`, `{B}`, `{C}`, `{A,C}`. The "
                "exchange property fails on `{B}` against `{A,C}`.",
            ],
            "lines": [
                "THE RECIPE FROM THE PROOF       A = {B}, so |A| = 1",
                "   weight of B        |A| + 2  =  3",
                "   weight of A and C  |A| + 1  =  2",
                "   giving weights      2 3 2   - the family's shipped default",
                "   greedy   takes B (3), then A rejected, C rejected      total 3",
                "   best     {A,C}                                         total 4",
                "",
                "THE SEARCH OVER {1,2,3}^3       27 weightings in a fixed order",
                "   stops after 13 of them, at weights  1 2 2",
                "   greedy   takes B (2), then C rejected, A rejected      total 2",
                "   best     {A,C}  =  1 + 2                               total 3",
                "",
                "THE SAME SEARCH ON THE THREE MATROIDS      3^5  =  243 each",
                "   uniform     all 243 tried, greedy optimal on every one",
                "   graphic     all 243 tried, greedy optimal on every one",
                "   partition   all 243 tried, greedy optimal on every one",
                "",
                "a weighting where greedy WINS on the matchings   3 1 3",
                "   greedy takes A (3), then C (3), B rejected             total 6 = best",
            ],
            "after": [
                "The last line is the one to keep. Greedy is optimal on the non-matroid for the "
                "weighting `3 1 3`, and for many others: of the 27 weightings in the search "
                "space, the walk had to pass twelve before finding a failure. A reader who "
                "typed one weighting and saw greedy win would have evidence for the wrong "
                "conclusion, and that is the entire reason the theorem quantifies.",
                "Notice also that the two counterexamples differ. The proof's recipe produces "
                "`2 3 2` and a gap of 3 against 4; the search produces `1 2 2` and a gap of 2 "
                "against 3. Both are valid and neither is canonical: what the theorem "
                "guarantees is that the set of bad weightings is nonempty, not that it has a "
                "distinguished member.",
                "For a faded rehearsal, apply the recipe to the matchings of a four-edge path, "
                "`1-2, 2-3, 3-4, 4-5`. The supplied first move is to find a failing pair: "
                "`{B, D}` is maximal with two elements, and `{A, C}` extends &mdash; look for a "
                "pair where the smaller side cannot be grown. Write down the weighting the "
                "recipe gives, predict greedy's answer and the optimum, then check both in the "
                "panel by typing the edge list and the weights.",
            ],
        },
        "quiz_title": "Quantifiers, converses, and what a search reports",
        "quiz": [
            {"q": "Greedy on the matchings of a path with weights `3 1 3` returns the optimum. What does that show?",
             "a": ["That the family is a matroid after all",
                   "That the exchange test was wrong",
                   "That greedy can be optimal on a particular weighting over a family that is not a matroid, which is why the theorem quantifies over all weightings",
                   "That the weights must be distinct for the theorem to apply"],
             "c": 2,
             "why": "The theorem says greedy is optimal for <em>every</em> weighting exactly "
                    "when the family is a matroid. One successful weighting is consistent with "
                    "the family failing, and here twelve of the twenty-seven weightings in the "
                    "search space pass before one fails."},
            {"q": "The panel reports that it found a beating weighting after trying 13 of the 27. What is 13 a fact about?",
             "a": ["How badly the family fails the exchange property",
                   "The enumeration order of the search, and nothing else",
                   "The rank of the family",
                   "The number of independent sets"],
             "c": 1,
             "why": "`beatingWeights` walks the space in a fixed order and stops at the first "
                    "failure. Relabel the elements and the count changes. What is a fact about "
                    "the family is that the walk terminates, which the converse of the theorem "
                    "guarantees for every non-matroid."},
            {"q": "Why does the panel walk all 243 weightings on a matroid rather than stopping when none of the first few fails?",
             "a": ["Because 243 is small enough that stopping saves nothing",
                   "Because `no counterexample found so far` and `the whole space was searched` are different claims and only the second is worth reporting",
                   "Because the exchange test needs the same walk",
                   "Because greedy's answer changes with the weighting"],
             "c": 1,
             "why": "An early stop on a matroid would report an absence of evidence. Walking the "
                    "whole space lets the panel say it tried every weighting in the space, "
                    "which is a stronger and checkable sentence &mdash; and still a sentence "
                    "about 243 of infinitely many weight functions."},
            {"q": "Which direction of the theorem lets you rule out every greedy rule of this shape for a problem, before writing any code?",
             "a": ["Matroid implies greedy optimal",
                   "Greedy optimal for every weighting implies matroid, used in contrapositive: a family that is not a matroid has a weighting that defeats greedy",
                   "Both directions equally",
                   "Neither; ruling out requires an explicit counterexample"],
             "c": 1,
             "why": "Exhibiting two maximal independent sets of different sizes refutes the "
                    "exchange property, and the converse then guarantees a bad weighting "
                    "exists. The proof even builds one, so an explicit counterexample is "
                    "available &mdash; but the ruling-out does not wait for it."},
        ],
        "mistakes": [
            ("Testing greedy on the weighting you happen to have",
             "This is the course's hazard in its purest form. The theorem is a statement about "
             "all weightings, and on the shipped non-matroid twelve weightings in a row let "
             "greedy win. Any conclusion drawn from one weighting is a conclusion about one "
             "weighting, and the panel's search exists to make that vivid rather than to be "
             "clever."),
            ("Reading the thirteen as meaningful",
             "It is the position of the first failure in a fixed walk order and nothing more. "
             "Neither the number of bad weightings, nor the size of the gap, nor any property "
             "of the family can be read off it, and relabelling the ground set moves it."),
            ("Forgetting that the 243-weighting sweep is itself a sample",
             "It is the whole of `{1, 2, 3}⁵` and it is not the whole of the weight functions "
             "on five elements. The reason a matroid can be trusted on a weighting nobody tried "
             "is the proof, not the sweep &mdash; and the sweep's job is to catch an "
             "implementation that has stopped agreeing with the proof."),
        ],
        "standard": ("Finish when you can decide, for a problem stated in words, whether some greedy rule is guaranteed to solve it, and produce the counterexample when the answer is no.",
                     "You should be able to state the theorem with its quantifier in the right "
                     "place, reproduce the exchange argument that proves the forward direction, "
                     "build a bad weighting from a failing pair using the converse's recipe, "
                     "and explain why a weighting on which greedy wins over a non-matroid is "
                     "not evidence of anything."),
        "note": ("The three remaining pages step outside matroids entirely. Each is an "
                 "algorithm whose guarantee is real, is proved, and is not the guarantee a "
                 "reader expects: a matching that is stable and systematically favours one "
                 "side, a policy that is optimal and cannot be implemented, and a rule with no "
                 "guarantee at all until a second arm is bolted onto it."),
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "stable-matching-and-who-it-favours",
        "title": "Stable Matching, and Who It Favours",
        "module": "What the guarantee says",
        "one_line": "Run the proposal algorithm, print an empty list of blocking pairs, and then find out which of several stable matchings it chose and whose interests that served.",
        "summary": (
            "The deferred-acceptance algorithm always terminates with a stable matching, and "
            "the lab checks that by listing the blocking pairs and printing an empty list. The "
            "harder fact is what it chose: on the opening instance there are six stable "
            "matchings, and the algorithm lands on the one every proposer likes best and every "
            "receiver likes worst. Stability is a guarantee. Fairness is not one, and the "
            "difference is visible in a single column."
        ),
        "key": [
            "blocking pair: two people who each prefer the other to their partner",
            "stable = no blocking pair, checked over all n(n−1) ordered pairs",
            "four on each side: 4 proposals, 0 blocking pairs, 24 matchings, 6 stable",
            "proposers' mean rank 1, receivers' mean rank 4 — best possible and worst possible",
            "swap the sides and the matching flips to 4 3 2 1, mean ranks 7/2 and 1",
            "proposer-optimality read off the list of stable matchings, not off the algorithm",
        ],
        "key_label": "One algorithm, six stable answers, and the one it picks",
        "concepts_intro": (
            "Three ideas: what stability actually forbids, why an empty list is the interesting "
            "output, and why the choice among several stable matchings is the real content of "
            "the theorem."
        ),
        "concepts": [
            ("Stability forbids a mutually preferred pair, and nothing else",
             "A <strong>blocking pair</strong> is two people, one from each side, who both "
             "prefer each other to their current partners. A matching is "
             "<strong>stable</strong> when no such pair exists. That is a local condition: it "
             "says nobody can improve by defecting <em>in pairs</em>. It says nothing about "
             "totals, nothing about fairness, and nothing about whether a three-way rotation "
             "would please everybody."),
            ("An empty list is a stronger output than a yes",
             "The panel does not report a boolean. It forms every one of the `n(n − 1)` ordered "
             "pairs &mdash; 12 on the opening instance &mdash; tests each against the "
             "definition, and prints the resulting list, which is empty. A reader can see what "
             "was checked. The same test is then applied to all `n!` matchings, so the count of "
             "stable ones comes from the definition rather than from the algorithm."),
            ("Choosing among stable matchings is where the asymmetry lives",
             "Six of the 24 matchings on the opening instance are stable. The algorithm returns "
             "one of them, and which one is not an accident: every proposer receives the best "
             "partner they have in <em>any</em> stable matching, and every receiver the worst. "
             "The panel establishes that by reading the list of all stable matchings, not by "
             "trusting the algorithm that produced one of them."),
        ],
        "read_title": "Proposals, stability, and the choice nobody notices",
        "read_intro": "The algorithm, the proof that it terminates with a stable matching, the enumeration beside it, and the asymmetry that the same instance makes unmissable.",
        "body": [
            ("def", ("The stable matching problem",
                     "`n` proposers and `n` receivers, each with a complete ranking of the "
                     "other side. A <strong>matching</strong> pairs each proposer with exactly "
                     "one receiver. A <strong>blocking pair</strong> is a proposer `p` and a "
                     "receiver `r`, not matched to each other, such that `p` prefers `r` to "
                     "their partner and `r` prefers `p` to theirs. A matching with no blocking "
                     "pair is <strong>stable</strong>.")),
            ("def", ("Deferred acceptance",
                     "While some proposer is unengaged and has not yet proposed to everyone, "
                     "they propose to the highest-ranked receiver they have not yet tried. A "
                     "receiver who is unengaged accepts; a receiver who is engaged accepts if "
                     "they prefer the new proposer, releasing the old one, and otherwise "
                     "rejects. The algorithm stops when everyone is engaged.")),
            ("p", "The greedy character is in the word <em>deferred</em>. Each proposer works "
                  "down their own list and never goes back up, which is the commitment; each "
                  "receiver holds the best offer so far and may release it, which is the part "
                  "that is not committed. A version in which receivers accepted irrevocably "
                  "would be fully greedy and would not produce a stable matching."),
            ("thm", ("The algorithm terminates, and its output is stable",
                     "Deferred acceptance makes at most `n²` proposals and ends with every "
                     "proposer matched, and the matching it produces has no blocking pair.")),
            ("proof", ("Each proposer proposes to each receiver at most once, so there are at "
                       "most `n²` proposals and the process terminates. A receiver, once "
                       "engaged, stays engaged and only ever trades up, so at the end a "
                       "proposer who had been rejected by everyone would imply a receiver "
                       "engaged to nobody while having received a proposal, which is "
                       "impossible. Hence everyone is matched.",
                       "Suppose `p` and `r` form a blocking pair: `p` prefers `r` to their "
                       "partner. Then `p` proposed to `r` at some point, before proposing to "
                       "their eventual partner. Either `r` rejected `p` outright, which means "
                       "`r` was already holding someone better, or `r` accepted and later "
                       "released `p` for someone better. Either way `r`'s partner only improved "
                       "afterwards, so `r` ends with someone they prefer to `p`, and `r` does "
                       "not prefer `p` to their partner. So no blocking pair exists.")),
            ("p", "On the opening instance the algorithm makes 4 proposals, which is well under "
                  "the bound of 16, and every one of them is accepted immediately. The "
                  "resulting matching pairs proposer `i` with receiver `i` for all four, and "
                  "the blocking-pair list, built from all 12 ordered pairs, is empty."),
            ("example", ("Six stable matchings, and the one that was chosen",
                         "All 24 matchings are tested against the blocking-pair definition and "
                         "6 of them are stable: `1234`, `1243`, `2134`, `2143`, `2341` and "
                         "`4321`, writing each as the partner of proposer 1, 2, 3, 4 in order. "
                         "Their mean ranks for the proposers are `1`, `3/2`, `3/2`, `2`, `5/2` "
                         "and `7/2`. The algorithm returned `1234`, the best of the six for "
                         "every proposer &mdash; and `4321`, the worst for them, is what the "
                         "receivers get when they propose instead.")),
            ("h3", "Proposer-optimality, and where the panel gets it from"),
            ("p", "The theorem is that every proposer receives the best partner they have in "
                  "any stable matching, simultaneously. That is stronger than it sounds: it is "
                  "not that the outcome is good on average for proposers, but that no proposer "
                  "can point to another stable matching in which they personally do better. The "
                  "panel verifies it by computing, for each proposer, their best achievable "
                  "partner over the enumerated stable matchings, and comparing."),
            ("p", "That is the right way round. Reading proposer-optimality off the algorithm "
                  "would mean trusting the algorithm to describe its own output; reading it off "
                  "the list of all stable matchings means the claim is checked against objects "
                  "the algorithm never saw. On the opening instance the proposers' mean rank is "
                  "`1` and the receivers' is `4`, the extreme values in both directions."),
            ("h3", "Three more instances, and a caption that is wrong"),
            ("p", "When everyone on both sides agrees on the same ranking there is exactly one "
                  "stable matching, both sides reach it, and proposing buys nothing: the panel "
                  "reports 6 proposals, 1 stable matching, and mean rank `2` for both sides. "
                  "When the two sides want opposite things there are 3 stable matchings and the "
                  "algorithm reaches the one its proposers prefer, mean ranks `1` and `3`."),
            ("p", "The fourth instance is labelled as having a long chain of rejections, and its "
                  "caption says one proposal displaces a partner who displaces another. The "
                  "trace on the page is: 1 proposes to 2, accepted; 2 proposes to 2, rejected; 3 "
                  "proposes to 1, accepted; 4 proposes to 4, accepted; 2 proposes to 3, "
                  "accepted. Five proposals, one rejection, and nobody displaced at all "
                  "&mdash; proposer 2 was turned away by a receiver who was already engaged to "
                  "someone they preferred. The count of 5 exceeds the 4 people for that reason "
                  "and not for the one the caption gives."),
            ("p", "Measured on this page: 4 proposals, 0 blocking pairs from 12 ordered pairs, "
                  "6 stable matchings of 24, proposers' mean rank `1` and receivers' `4`, and "
                  "the sides swapped giving `7/2` and `1`. Proved on this page: the algorithm "
                  "always terminates within `n²` proposals with a stable matching, and that "
                  "matching is best for every proposer among all stable ones. What no page here "
                  "proves, because it is false, is that the outcome is fair."),
        ],
        "lab": ("greedy", {
            "mode": "stable",
            "preset": "classic",
            "panel_title": "Choose the preference lists, and watch who benefits",
            "panel_intro": "The blocking-pair list is built by testing every ordered pair "
                           "against the definition and it is printed even when it is empty. "
                           "Beside it, every one of the n! matchings is tested the same way, so "
                           "the count of stable ones is independent of the algorithm.",
        }),
        "steps_title": "Reading a matching, and reading the algorithm that made it",
        "steps_intro": "Five steps. The last two are where the interesting facts are and where most readers stop too early.",
        "steps": [
            ("Follow the proposals in order, not the final pairing",
             "The trace is the algorithm. Each line names who proposed to whom and what "
             "happened, and the number of lines is the proposal count &mdash; 4 on the opening "
             "instance, 6 on the one where everybody agrees, and 5 on the one with a rejection "
             "in it."),
            ("Check stability against the definition, pair by pair",
             "For every proposer and every receiver not matched to each other, ask whether both "
             "would rather swap. That is `n(n − 1)` questions and the answer should be no every "
             "time. An empty list is the output worth printing, because it shows what was "
             "asked."),
            ("Count the stable matchings before concluding anything about this one",
             "If there is only one, the algorithm had no choice and the asymmetry question does "
             "not arise. If there are six, the choice is the whole story. The panel enumerates "
             "all `n!` matchings and filters them with the same blocking-pair test."),
            ("Compare the mean ranks of the two sides",
             "On the opening instance the proposers average rank 1 and the receivers rank 4, "
             "which on four people is the best and the worst possible. Two numbers, and they "
             "say more about the algorithm's character than the stability verdict does."),
            ("Swap the sides and run it again",
             "The same instance with the receivers proposing gives a different stable matching "
             "and the mean ranks exchange places. If the two runs agree, as they do when "
             "everyone shares a ranking, the stable matching is unique and the algorithm never "
             "had a decision to make."),
        ],
        "worked": {
            "title": "Four on each side, and the six stable matchings",
            "intro": [
                "Proposers' rankings, one row each: `1 2 3 4`, `2 1 3 4`, `3 4 1 2`, `4 3 1 2`. "
                "Receivers' rankings: `4 3 2 1`, `3 4 1 2`, `2 1 4 3`, `1 2 3 4`. Each proposer "
                "has a different first choice, which is why the run is short.",
            ],
            "lines": [
                "   proposal   from   to   outcome",
                "      1         1      1   accepted     receiver 1 was free",
                "      2         2      2   accepted     receiver 2 was free",
                "      3         3      3   accepted     receiver 3 was free",
                "      4         4      4   accepted     receiver 4 was free",
                "",
                "matching        1 2 3 4        proposals 4, against a bound of 16",
                "blocking pairs  none, out of all 12 ordered pairs tested",
                "",
                "   all 24 matchings tested; 6 are stable",
                "   matching   partners of 1,2,3,4   mean rank A   mean rank B",
                "     1234           1 2 3 4              1            4",
                "     1243           1 2 4 3             3/2          7/2",
                "     2134           2 1 3 4             3/2          7/2",
                "     2143           2 1 4 3              2            3",
                "     2341           2 3 4 1             5/2           2",
                "     4321           4 3 2 1             7/2           1",
                "",
                "the algorithm returned   1234, the top row",
                "the receivers proposing  4 3 2 1, the bottom row",
            ],
            "after": [
                "Every proposer got their first choice and every receiver got their last. Both "
                "are visible in the table as the extremes of the mean-rank columns, and the "
                "algorithm did not have to do anything clever to get there: all four proposals "
                "were accepted at once, because the four proposers wanted four different "
                "people.",
                "The six stable matchings form a chain in the mean-rank columns: as the "
                "proposers' average rank worsens from 1 to 7/2 the receivers' improves from 4 "
                "to 1. That is not a coincidence of this instance either &mdash; the stable "
                "matchings of any instance form a lattice, with the proposer-optimal one at "
                "one end and the receiver-optimal one at the other &mdash; but the lattice is "
                "not proved anywhere in this library and the table is one instance of it.",
                "For a faded rehearsal, predict the trace on the instance where every row on "
                "both sides is `1 2 3`. The supplied first move is that proposer 1 takes "
                "receiver 1 immediately and proposer 2 is rejected there. Say how many "
                "proposals the run takes in total, how many stable matchings exist, and what "
                "both mean ranks are &mdash; then say why swapping the sides changes nothing.",
            ],
        },
        "quiz_title": "Stability, choice, and the asymmetry",
        "quiz": [
            {"q": "The panel reports 0 blocking pairs and 6 stable matchings. What does the first number establish about the second?",
             "a": ["That the algorithm found the best of the six",
                   "That the matching returned is one of the six; which one, and whether it is good for anybody, are separate questions",
                   "That the other five are worse",
                   "Nothing, since blocking pairs and stability are different properties"],
             "c": 1,
             "why": "An empty blocking-pair list is exactly the definition of stable, so the "
                    "returned matching is one of the six. Stability is a property all six "
                    "share, which is precisely why it cannot distinguish them &mdash; the "
                    "mean-rank columns do."},
            {"q": "Why does the panel compute proposer-optimality from the enumerated list of stable matchings rather than from the algorithm?",
             "a": ["Because the algorithm does not track ranks",
                   "Because the claim is about all stable matchings, so checking it against the algorithm that produced one of them would be checking the algorithm against itself",
                   "Because enumeration is faster for small n",
                   "Because the algorithm may return an unstable matching"],
             "c": 1,
             "why": "&ldquo;Every proposer gets their best achievable partner&rdquo; quantifies "
                    "over the stable matchings. The panel computes each proposer's best "
                    "achievable partner from the enumerated list and compares, so the claim is "
                    "checked against objects the algorithm never constructed."},
            {"q": "On the opening instance the proposers' mean rank is 1 and the receivers' is 4. What is the right conclusion?",
             "a": ["The algorithm is unfair in general and should not be used",
                   "On this instance the algorithm reached the extreme in both directions; proposer-optimality and receiver-pessimality are the proved statements, and neither is a fairness claim",
                   "The receivers' preferences were entered incorrectly",
                   "Stability and fairness coincide when the mean ranks are extreme"],
             "c": 1,
             "why": "The two numbers are this instance's measurement. The theorems are that "
                    "every proposer does as well as they can in any stable matching and every "
                    "receiver as badly, and those are guarantees about the structure rather "
                    "than judgements about it. On the instance where everyone shares a ranking "
                    "both means are 2."},
            {"q": "The caption on one instance says a proposal displaces a partner who displaces another. The trace shows five proposals with one rejection and nobody released. What should be written down?",
             "a": ["The caption, since it explains why the count exceeds four",
                   "The trace: one proposer was turned away by an already-engaged receiver, and that single extra proposal is why the count is five",
                   "Neither, since proposal counts vary between runs",
                   "The caption, since displacement is what makes the count exceed n"],
             "c": 1,
             "why": "A displacement would release an engaged proposer, who would then propose "
                    "again; the trace shows no release at all. The count exceeds four because "
                    "proposer 2's first proposal was refused. Deferred acceptance is "
                    "deterministic, so the trace is the same on every run."},
        ],
        "mistakes": [
            ("Reading stability as fairness",
             "Stability forbids exactly one thing: a pair who would both rather have each other. "
             "It permits an outcome in which one entire side receives its worst acceptable "
             "partner, and on the opening instance that is what happens. The word does a great "
             "deal of quiet work in how this algorithm is described elsewhere."),
            ("Stopping at the stability verdict",
             "The verdict is the easy half and the algorithm guarantees it. The interesting "
             "question is which of the stable matchings was returned, and that needs the "
             "enumeration beside it: 6 on the opening instance, 3 on one, 1 on the other two. "
             "Where the count is 1 there is nothing to discuss, and a reader who only ever saw "
             "those instances would never learn that there is."),
            ("Expecting the proposal count to track the number of rejections in the way a caption says",
             "One caption on this panel claims a chain of displacements and the trace shows a "
             "single refusal. The count of proposals exceeds `n` by exactly the number of "
             "rejections, and a rejection of an unengaged proposer by an engaged receiver "
             "displaces nobody. Read the trace."),
        ],
        "standard": ("Finish when you can run the proposals by hand, verify stability from the definition, and say what the algorithm chose among the stable matchings and at whose expense.",
                     "You should be able to state what a blocking pair is without hedging, "
                     "reproduce the argument that the output has none, explain why the "
                     "enumeration of all `n!` matchings is what makes proposer-optimality "
                     "checkable, and say what changes when the two sides swap roles."),
        "note": ("This algorithm's guarantee is real and is not fairness. The next one's "
                 "guarantee is real and is not implementability: &ldquo;Caching and the Offline "
                 "Bound&rdquo; builds a replacement policy that is provably optimal and cannot "
                 "be run, because it needs to know the future, and then uses it as the bound "
                 "the policies you can run are measured against."),
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "caching-and-the-offline-bound",
        "title": "Caching and the Offline Bound",
        "module": "What the guarantee says",
        "one_line": "Build a replacement policy that is optimal and cannot be implemented, check it against a search over every eviction, and watch a bigger cache do worse.",
        "summary": (
            "Evicting the page whose next use is furthest away is optimal for any known "
            "sequence of references, and it is unimplementable, because it needs the sequence "
            "in advance. That is what makes it a bound rather than a policy. The lab checks the "
            "bound against a search over every eviction decision a cache of that size could "
            "make, and then sweeps FIFO from one slot to six on a trace where more cache means "
            "fewer hits."
        ),
        "key": [
            "demand paging: every miss loads the page, so the only choice is what to evict",
            "farthest-in-future: evict the page whose next use is latest — needs the whole trace",
            "twelve references, three slots: FIFO 3, LRU 2, farthest-in-future 5",
            "the best any offline policy can do is 5, over 43 distinct (position, cache) states",
            "FIFO as the cache grows 1 to 6: 0, 0, 3, 2, 7, 7 — four slots lose a hit",
            "LRU on the same trace: 0, 0, 2, 4, 7, 7 — never falls",
        ],
        "key_label": "A bound you cannot run, and an anomaly you can watch",
        "concepts_intro": (
            "Three ideas: what demand paging leaves to decide, why an unimplementable policy is "
            "still the right yardstick, and why more cache is not automatically more hits."
        ),
        "concepts": [
            ("The only decision is which page to throw out",
             "Under <strong>demand paging</strong> a referenced page that is absent is loaded, "
             "always, and nothing is loaded speculatively. So a policy is entirely determined "
             "by its eviction rule, and comparing policies is comparing eviction rules on the "
             "same trace with the same cache size. Every figure on this page is a hit count "
             "under that model."),
            ("A bound need not be a policy",
             "Farthest-in-future evicts the page whose next reference is latest, which requires "
             "knowing the references that have not happened. No real cache can do it. It is "
             "still exactly the right thing to measure against, because it is optimal among all "
             "policies including the ones nobody can run: if LRU reaches 2 hits where the bound "
             "is 5, no cleverness in an online policy can recover more than 3, and the shortfall "
             "is attributable to not knowing the future rather than to LRU."),
            ("A hit count is not monotone in the cache size",
             "The intuition that a bigger cache cannot hurt is false for FIFO, and the panel "
             "sweeps it rather than saying so. On the opening trace FIFO gets 3 hits with three "
             "slots and 2 with four. The extra slot changes which pages are resident when each "
             "reference arrives, and FIFO's eviction order does not respect what is about to be "
             "used, so the change can go the wrong way."),
        ],
        "read_title": "Three policies, a bound, and an anomaly",
        "read_intro": "The model, the three eviction rules, the proof that farthest-in-future is optimal, the independent search that confirms it, and the sweep where a bigger cache loses.",
        "body": [
            ("def", ("The paging problem",
                     "A cache holds `k` pages. A <strong>trace</strong> is a sequence of page "
                     "references. A reference to a resident page is a <strong>hit</strong>; a "
                     "reference to an absent page is a <strong>miss</strong>, and the page is "
                     "loaded, evicting one resident page if the cache is full. A policy is the "
                     "rule for choosing which.")),
            ("p", "The lab opens on the trace `1 2 3 4 1 2 5 1 2 3 4 5` with three slots: twelve "
                  "references over five distinct pages. FIFO evicts the page that has been "
                  "resident longest and gets 3 hits, a rate of `1/4`. LRU evicts the page "
                  "unused for longest and gets 2, a rate of `1/6`. Farthest-in-future gets 5, a "
                  "rate of `5/12`."),
            ("p", "LRU doing worse than FIFO here is worth a moment. LRU is the better policy on "
                  "most workloads and it is not a theorem; on this trace, which was built to "
                  "embarrass FIFO's cache-size behaviour, LRU happens to lose by one hit. Two "
                  "measurements on one trace, and neither is a ranking."),
            ("def", ("Farthest-in-future",
                     "On a miss with a full cache, evict the resident page whose next reference "
                     "is latest in the remaining trace; a page never referenced again is "
                     "evicted first. This requires the whole trace in advance, so it is an "
                     "<strong>offline</strong> policy.")),
            ("thm", ("Farthest-in-future is optimal",
                     "For every trace and every cache size, no policy &mdash; online or offline "
                     "&mdash; achieves more hits than farthest-in-future under demand paging.")),
            ("p", "The proof is an exchange argument of exactly the shape performed earlier on "
                  "this course. Take any optimal schedule of evictions and the first point at "
                  "which it differs from farthest-in-future; show that its choice can be "
                  "replaced by farthest-in-future's without losing a hit, by tracking the two "
                  "caches, which differ in at most one page, until they coincide again. "
                  "Repeating drives the first difference forward, and the schedule becomes "
                  "farthest-in-future's."),
            ("p", "The lab does not run that argument. It does something stronger for the "
                  "instance on screen: it searches every eviction decision a cache of this size "
                  "could make, memoised on the pair of position and cache contents, and reports "
                  "the maximum hits reachable. On the opening trace that search visits 43 "
                  "distinct states and returns 5, which is what farthest-in-future got. So the "
                  "optimality claim is checked here rather than cited, by a search that knows "
                  "nothing about looking ahead."),
            ("example", ("Where the online policies cannot reach",
                         "On the thirteen-reference trace `1 2 3 1 4 1 2 5 1 2 3 4 5` with "
                         "three slots, FIFO and LRU both get 4 hits and farthest-in-future gets "
                         "6, confirmed by a search over 44 states. On the loop `1 2 3 4` "
                         "repeated three times with three slots, FIFO and LRU both get 0 "
                         "&mdash; each evicts precisely the page about to be used &mdash; while "
                         "the offline optimum is 6 of 12, because on every miss it discards the "
                         "page whose turn comes last rather than the one whose turn comes "
                         "next.")),
            ("h3", "Belady's anomaly, swept rather than described"),
            ("p", "The panel sweeps FIFO from one slot to six on whatever trace is loaded and "
                  "prints the hit count at each size. On the opening trace that row reads 0, 0, "
                  "3, 2, 7, 7: going from three slots to four costs a hit. On the "
                  "thirteen-reference trace it reads 0, 1, 4, 3, 8, 8, and the same step loses a "
                  "hit again. This is Belady's anomaly, and the reader sees the row rather than "
                  "the citation."),
            ("p", "The same sweep under LRU on those two traces reads 0, 0, 2, 4, 7, 7 and 0, 1, "
                  "4, 5, 8, 8: never falling. That is not luck. LRU is a <em>stack</em> policy "
                  "&mdash; the pages resident with `k` slots are always a subset of those "
                  "resident with `k + 1` at the same point &mdash; and a stack policy cannot "
                  "suffer the anomaly. FIFO is not a stack policy, and the two rows above are "
                  "what that difference costs."),
            ("p", "The sweep the panel draws is always FIFO's, whichever policy is selected for "
                  "the chart, and the column that reads whether a bigger cache ever does worse "
                  "is about FIFO alone. On two of the four shipped traces it reads no, and a "
                  "reader who took that as a statement about caching in general would have "
                  "generalised from a policy to a field."),
            ("h3", "A caption to distrust"),
            ("p", "The trace `1 2 1 3 1 4 1 5 1 6 1 7` with two slots is captioned as one where "
                  "every policy keeps the hot page and the differences between them disappear. "
                  "The table above it reads FIFO 3, LRU 5, farthest-in-future 5. FIFO does not "
                  "keep the hot page: it evicts by arrival order, and page 1 is reloaded and "
                  "then evicted again on every cycle. The difference between the policies on "
                  "that trace is two hits out of twelve, which is the largest relative gap "
                  "between FIFO and LRU on any of the four."),
            ("p", "Measured on this page: 12 references, 3 slots, FIFO 3, LRU 2, "
                  "farthest-in-future 5, offline optimum 5 over 43 states, and a FIFO sweep of "
                  "0, 0, 3, 2, 7, 7. Proved on this page: farthest-in-future is optimal on every "
                  "trace and every cache size. Not proved anywhere in this library: any bound "
                  "on how far an online policy can fall behind it, which is the competitive "
                  "analysis this course names and does not develop."),
        ],
        "lab": ("greedy", {
            "mode": "caching",
            "preset": "belady",
            "panel_title": "Choose the trace and the cache size, then read the sweep",
            "panel_intro": "The last row sweeps FIFO from one slot to six and marks any size at "
                           "which the hit count falls. The offline optimum beside it is a search "
                           "over every eviction decision, so the claim that farthest-in-future "
                           "attains it is checked rather than assumed.",
        }),
        "steps_title": "Measuring a policy against a bound",
        "steps_intro": "Four steps, and the fourth is the one that separates a policy comparison from a ranking.",
        "steps": [
            ("Fix the trace and the cache size before comparing anything",
             "A hit count means nothing without both. The same policy on the same trace gets 0 "
             "hits with three slots and 8 with four on the loop instance, and two policies "
             "compared at different sizes are not being compared at all."),
            ("Run the online policies first, then the bound",
             "FIFO and LRU are what a real cache can do. Farthest-in-future is what the trace "
             "permits. Recording them in that order keeps the bound in its place: it is the "
             "denominator of the comparison, not a candidate."),
            ("Confirm the bound against the exhaustive search",
             "The panel searches every eviction decision, memoised on position and cache "
             "contents, and prints the number of states it visited. When that search agrees "
             "with farthest-in-future, optimality has been checked on this trace. When the "
             "trace is too long the panel refuses and says so."),
            ("Sweep the cache size before saying anything about cache size",
             "One size is one data point, and the direction of the effect is not guaranteed. "
             "Read the whole row: three slots to four costs FIFO a hit on two of the four "
             "shipped traces, and nothing in the first three columns of either row would have "
             "warned you."),
        ],
        "worked": {
            "title": "Twelve references, three slots, three policies",
            "intro": [
                "The trace is `1 2 3 4 1 2 5 1 2 3 4 5`. Three slots. Each column below shows "
                "the cache after the reference, with a star marking a hit.",
            ],
            "lines": [
                "   ref    FIFO cache      LRU cache       farthest-in-future cache",
                "    1     1               1               1",
                "    2     1 2             1 2             1 2",
                "    3     1 2 3           1 2 3           1 2 3",
                "    4     2 3 4           2 3 4           1 2 4   evict 3, next used latest",
                "    1     3 4 1           3 4 1           1 2 4  *",
                "    2     4 1 2           4 1 2           1 2 4  *",
                "    5     1 2 5           1 2 5           1 2 5   evict 4, never used again",
                "    1     1 2 5  *        2 5 1  *        1 2 5  *",
                "    2     1 2 5  *        5 1 2  *        1 2 5  *",
                "    3     2 5 3           1 2 3           2 5 3   evict 1, never used again",
                "    4     5 3 4           2 3 4           5 3 4   evict 2, never used again",
                "    5     5 3 4  *        3 4 5           5 3 4  *",
                "",
                "hits        FIFO 3            LRU 2            farthest-in-future 5",
                "rate        1/4               1/6              5/12",
                "",
                "search over every eviction    43 distinct (position, cache) states",
                "best any offline policy can do   5    - so the bound is attained",
                "",
                "FIFO swept from 1 to 6 slots     0  0  3  2  7  7",
                "                                       ^ four slots, fewer hits than three",
                "LRU swept the same way           0  0  2  4  7  7",
            ],
            "after": [
                "Farthest-in-future's first interesting move is at reference 4. Pages 1, 2 and 3 "
                "are resident and page 4 arrives; page 3's next use is at position 10 and pages "
                "1 and 2 are needed at 5 and 6, so 3 goes. Every later eviction is the same "
                "calculation, and the two pages evicted at the end are ones the trace never "
                "mentions again.",
                "The sweep is the row to stare at. FIFO's hit count goes 0, 0, 3, 2, 7, 7: three "
                "slots beat four. The reason is that FIFO's eviction order depends on when pages "
                "arrived, and adding a slot changes the arrival order of everything downstream, "
                "so the resident set at each reference is not a superset of the smaller cache's. "
                "LRU's resident set always is, which is why its row never falls.",
                "For a faded rehearsal, work out the loop trace `1 2 3 4 1 2 3 4 1 2 3 4` with "
                "three slots before running it. The supplied first move is that after the first "
                "four references the cache holds 2, 3, 4 under both FIFO and LRU, and the next "
                "reference is 1. Say what FIFO and LRU each score, what the offline optimum is, "
                "and what happens to all three when the cache is given a fourth slot.",
            ],
        },
        "quiz_title": "Bounds, policies, and the row that falls",
        "quiz": [
            {"q": "Why is farthest-in-future used as the yardstick even though no cache can run it?",
             "a": ["Because it is easy to compute offline",
                   "Because it is optimal among all policies, so the gap to it isolates the cost of not knowing the future",
                   "Because LRU approximates it closely on real workloads",
                   "Because it never suffers Belady's anomaly"],
             "c": 1,
             "why": "The point of a bound is that nothing can beat it. When LRU reaches 2 and the "
                    "bound is 5, the missing 3 hits are attributable to the information LRU "
                    "lacks rather than to a defect in LRU. Ease of computation and LRU's "
                    "behaviour on real workloads are not why it is the right comparison."},
            {"q": "The panel reports that a search over 43 states also reaches 5 hits. What does that add to the claim that farthest-in-future is optimal?",
             "a": ["Nothing, since the theorem already says so",
                   "It checks the theorem's conclusion on this trace by a search that knows nothing about looking ahead, so the two could have disagreed",
                   "It proves the theorem for all traces of this length",
                   "It replaces the theorem with a computation"],
             "c": 1,
             "why": "The search enumerates eviction decisions and shares no reasoning with the "
                    "lookahead rule. Agreement is a real check &mdash; disagreement would be "
                    "conclusive &mdash; and it is about this trace. The theorem covers the "
                    "traces nobody typed."},
            {"q": "FIFO's sweep on the opening trace reads 0, 0, 3, 2, 7, 7 and LRU's reads 0, 0, 2, 4, 7, 7. Which conclusion is safe?",
             "a": ["LRU is better than FIFO",
                   "A bigger cache can reduce FIFO's hits; LRU's row never falls here, and for LRU that is guaranteed because it is a stack policy",
                   "Both policies converge at five slots, so cache size stops mattering",
                   "FIFO's anomaly disappears at larger cache sizes"],
             "c": 1,
             "why": "FIFO loses a hit from three slots to four, which is Belady's anomaly. LRU's "
                    "row not falling is not luck: its resident set with `k` slots is always "
                    "contained in its resident set with `k + 1`. FIFO at two slots beats LRU at "
                    "two on another trace, so no ranking follows, and the rows merely happen to "
                    "coincide at five."},
            {"q": "One trace is captioned as one where every policy keeps the hot page and the differences disappear. The table reads FIFO 3, LRU 5, farthest-in-future 5. What is true?",
             "a": ["The caption is right; a two-hit difference over twelve references is negligible",
                   "FIFO does not keep the hot page, because it evicts by arrival order rather than by use, so the difference is the largest relative gap on any shipped trace",
                   "The caption refers to a different cache size",
                   "LRU and farthest-in-future agreeing means the differences have disappeared"],
             "c": 1,
             "why": "FIFO reloads page 1 and then evicts it again on every cycle, because "
                    "arrival order says nothing about reuse. Three hits against five is the "
                    "measurement; the caption is prose that nothing in the build has ever "
                    "checked against a run."},
        ],
        "mistakes": [
            ("Treating farthest-in-future as a policy to implement",
             "It needs the references that have not happened yet. Every description of it as "
             "&ldquo;the optimal replacement algorithm&rdquo; is correct and every attempt to "
             "deploy it is confused. Its role here is the same as the depth's on the "
             "interval-partitioning page: a quantity nothing can beat, computed separately, "
             "against which a real algorithm is measured."),
            ("Assuming more cache cannot hurt",
             "For FIFO it can, and the sweep shows it on two of the four shipped traces. The "
             "guarantee people are reaching for belongs to stack policies such as LRU, where "
             "the resident set grows with the cache, and FIFO is not one. Adding memory to a "
             "FIFO cache is an experiment, not an improvement."),
            ("Reading the anomaly column as a statement about caching",
             "The sweep the panel draws is FIFO's, whatever policy is selected above it, so the "
             "column reporting whether a bigger cache ever does worse is about FIFO on this "
             "trace. It reads no on two of the four traces, and neither answer is a statement "
             "about any other policy."),
        ],
        "standard": ("Finish when you can measure a policy against a bound you cannot run, and say what a change in cache size did rather than what it should have done.",
                     "You should be able to replay FIFO, LRU and farthest-in-future by hand on a "
                     "short trace, explain why an offline optimum is the right denominator, "
                     "describe the exchange argument that proves the lookahead rule optimal, "
                     "and say why LRU is immune to the anomaly and FIFO is not."),
        "note": ("This algorithm's guarantee was real and unattainable. The last of these three "
                 "is a rule with no guarantee whatever: on the knapsack, sorting by value per "
                 "unit weight is provably optimal when items may be cut and provably nothing at "
                 "all when they may not. &ldquo;Fractional and 0/1 Knapsack&rdquo; measures the "
                 "gap, adds the one line that turns the rule into a guarantee, and hands the "
                 "next course its subject."),
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "fractional-and-0-1-knapsack",
        "title": "Fractional and 0/1 Knapsack",
        "module": "What the guarantee says",
        "one_line": "Watch one rule solve a problem exactly and then fail completely on its twin, and see what a proved half-guarantee is and is not worth.",
        "summary": (
            "Sorting by value per unit weight and filling greedily is optimal for the knapsack "
            "when items may be cut, and the answer is an exact fraction. Refuse to cut, and the "
            "same rule has no guarantee at all: on the opening instance it returns 160 against "
            "an optimum of 220, and on another it returns two per cent of the optimum. Taking "
            "the better of it and the single most valuable item that fits is guaranteed to "
            "reach at least half the optimum &mdash; a real bound, and one that no shipped "
            "instance comes close to."
        ),
        "key": [
            "fractional: cut items freely; sort by value per unit weight, fill, cut the last",
            "0/1: take an item whole or not at all",
            "three items 10/60, 20/100, 30/120, capacity 50: fractional 240, 0/1 optimum 220",
            "density greedy 160 — a ratio of 8/11 — while value-first greedy gets 220",
            "max(density greedy, best single item that fits) ≥ OPT / 2, proved",
            "on this instance that arm returns 160 against a promise of 110",
        ],
        "key_label": "One rule, two problems, and the bound that survives",
        "concepts_intro": (
            "Three ideas: why cutting changes the problem completely, why a ratio on one "
            "instance is not a guarantee, and what a proved ratio actually promises."
        ),
        "concepts": [
            ("Cutting an item makes the greedy choice safe",
             "In the fractional problem the densest item can always be taken as far as capacity "
             "allows, because any solution not doing so can be improved by swapping weight into "
             "it. That is an exchange argument and it is airtight. It relies entirely on weight "
             "being divisible: the moment items must be taken whole, &ldquo;swap weight into "
             "the denser item&rdquo; stops being a legal move and the argument has nothing left."),
            ("A ratio measured on an instance is a measurement",
             "Density greedy returns 160 where the optimum is 220, a ratio of `8/11`. On another "
             "of the lab's instances it returns 2 where the optimum is 100, a ratio of `1/50`. "
             "Neither number is a guarantee, and there is no number that is: for any bound you "
             "propose, an instance exists on which plain density greedy does worse. The rule "
             "has no approximation ratio at all."),
            ("A proved ratio is a statement about the instances nobody typed",
             "Take the better of density greedy and the single most valuable item that fits. "
             "That is at least half the optimum, on every instance. On the opening instance it "
             "returns 160 against a promised 110, which is far above the promise &mdash; and on "
             "all four shipped instances the ratio is `8/11`, `3/5`, `1` and `47/51`, never "
             "near a half. A guarantee is a floor, and observing that the floor is loose on "
             "four instances says nothing about the fifth."),
        ],
        "read_title": "Two problems that differ in one word",
        "read_intro": "The fractional problem and its exact answer, the 0/1 problem and the three rules that fail on it, and the second arm that turns a rule with no guarantee into one with a proof.",
        "body": [
            ("def", ("The two knapsack problems",
                     "Given items with positive integer weights `wᵢ` and values `vᵢ` and a "
                     "capacity `W`, choose amounts `xᵢ` maximising `Σ vᵢ xᵢ` subject to "
                     "`Σ wᵢ xᵢ ≤ W`. In the <strong>fractional</strong> problem `0 ≤ xᵢ ≤ 1`; "
                     "in the <strong>0/1</strong> problem `xᵢ ∈ {0, 1}`. The "
                     "<strong>density</strong> of an item is `vᵢ / wᵢ`.")),
            ("p", "The lab opens on three items &mdash; `A 10/60`, `B 20/100`, `C 30/120` "
                  "&mdash; with capacity 50, writing each as weight over value. The densities "
                  "are 6, 5 and 4, compared as exact fractions rather than as decimals, so two "
                  "items whose densities differ in the fifteenth place are ordered by their "
                  "values and not by rounding."),
            ("thm", ("Density greedy solves the fractional problem exactly",
                     "Sorting by decreasing density, taking each item whole while it fits and "
                     "the last one in whatever fraction remains, yields an optimal solution to "
                     "the fractional knapsack.")),
            ("proof", ("Let `x` be an optimal solution and suppose some item `i` is taken only "
                       "partly while a less dense item `j` is taken in positive amount. Move a "
                       "small weight `ε` of capacity from `j` to `i`: the value changes by "
                       "`ε(vᵢ/wᵢ − vⱼ/wⱼ) ≥ 0`, so the solution does not get worse, and the "
                       "amounts stay within their bounds for small enough `ε`.",
                       "Repeating drives every such inversion out, so some optimal solution "
                       "takes the items in decreasing density order, whole while they fit, with "
                       "at most one cut. That is exactly greedy's answer, and the capacity is "
                       "used in full unless every item is taken.")),
            ("example", ("240 with cutting, 220 without",
                         "Densities 6, 5 and 4. Greedy takes `A` whole (10 of the 50), `B` whole "
                         "(30 used), then two thirds of `C`, giving `60 + 100 + 80 = 240` "
                         "exactly. The 0/1 optimum, over all 8 subsets, is `B` and `C` together "
                         "for 220 at exactly 50 units of weight. The caption on that instance "
                         "names the cut item as the cause, which is right; the arithmetic is "
                         "that the difference is 20 while the two thirds of `C` is worth 80.")),
            ("p", "Now run the same density rule on the 0/1 problem. It takes `A` (10 used, "
                  "value 60), takes `B` (30 used, value 160), then cannot fit `C`, which needs "
                  "30 and has 20 left. It stops at 160, with 20 units of capacity unused, "
                  "against an optimum of 220. The exchange argument that made the rule exact a "
                  "moment ago is gone: the move it relies on, shifting a little weight between "
                  "items, is not available."),
            ("h3", "Three rules, and the one that looks worst doing best"),
            ("p", "The panel offers two other orders. By value, highest first, greedy takes `C` "
                  "then `B` and reaches 220 &mdash; the optimum. By weight, lightest first, it "
                  "takes `A` and `B` and reaches 160. So on this instance the rule with a "
                  "theorem behind it loses to the rule that sounds naive, and the reader who "
                  "concludes that value-first is the better rule will be right about this "
                  "instance."),
            ("p", "And about three of the four. On `1/2, 10/10, 10/10` with capacity 20 the "
                  "value rule reaches the optimum of 20 while density reaches 12; on `1/2, "
                  "50/100` with capacity 50 the value rule reaches 100 while density reaches 2; "
                  "on the six-item instance both reach 47 against an optimum of 51. Value-first "
                  "matches the optimum on three of the four shipped instances and density on "
                  "none of them, and neither fact is a guarantee about either rule."),
            ("h3", "The second arm, and what it buys"),
            ("thm", ("The half guarantee",
                     "Let `g` be the value density greedy returns and `s` the value of the most "
                     "valuable single item that fits. Then `max(g, s) ≥ OPT / 2`, where `OPT` "
                     "is the 0/1 optimum, on every instance.")),
            ("proof", ("Run density greedy and let `i` be the first item it rejects, the one "
                       "that did not fit. The fractional optimum is at most `g + vᵢ`: greedy "
                       "took the densest items whole up to `i`, and the fractional solution can "
                       "add at most the whole of `i` beyond that before the capacity is used.",
                       "The 0/1 optimum is at most the fractional optimum, so "
                       "`OPT ≤ g + vᵢ ≤ g + s`, since `i` fits by itself and so `vᵢ ≤ s`. Hence "
                       "`2 max(g, s) ≥ g + s ≥ OPT`, which is the claim. If greedy rejects "
                       "nothing it took everything and is optimal.")),
            ("p", "On the opening instance the two arms are 160 and 120, so the guaranteed "
                  "answer is 160, and half the optimum is 110. The guarantee is met with a great "
                  "deal to spare. On `1/2, 50/100` the arms are 2 and 100, the guaranteed answer "
                  "is 100, and it is the optimum: density greedy takes the crumb and stops, and "
                  "the single most valuable item alone does fifty times better."),
            ("p", "That instance is labelled in the panel as greedy at almost exactly half, and "
                  "it is not: density greedy reaches `1/50` of the optimum and the guaranteed "
                  "arm reaches all of it. The instance's own caption gets it right &mdash; it is "
                  "the one where the second arm rescues the first &mdash; and the label "
                  "contradicts it. Neither string is checked by anything in the build, and the "
                  "figures above them are."),
            ("p", "None of the four shipped instances comes near the bound: the guaranteed arm "
                  "reaches `8/11`, `3/5`, `1` and `47/51` of the optimum. A reader who inferred "
                  "from that row that the true ratio is about three quarters would be reading a "
                  "floor as an estimate. The bound is a floor, it is proved, and instances that "
                  "approach it exist even though none of these does."),
            ("p", "Measured on this page: fractional 240 exactly, 0/1 optimum 220 over 8 "
                  "subsets, density greedy 160 at a ratio of `8/11`, value-first 220, "
                  "lightest-first 160, and the guaranteed arm 160 against a promise of 110. "
                  "Proved on this page: density greedy is exact on the fractional problem, and "
                  "`max(g, s) ≥ OPT / 2` on every instance of the 0/1 problem. Not provable at "
                  "all: any ratio whatever for plain density greedy on the 0/1 problem."),
        ],
        "lab": ("greedy", {
            "mode": "knapsack",
            "preset": "classic",
            "panel_title": "Choose the items, the capacity, and the order the rule uses",
            "panel_intro": "The fractional optimum is an exact fraction and is printed as one. "
                           "The 0/1 optimum is the best of every subset and knows nothing about "
                           "any rule. The last two figures are the guaranteed arm and whether it "
                           "met its promise, both computed rather than asserted.",
        }),
        "steps_title": "Reading a rule, a ratio and a guarantee apart",
        "steps_intro": "Five steps. The first three produce numbers; the last two decide what the numbers license.",
        "steps": [
            ("Solve the fractional problem first, and keep it as a fraction",
             "It is the easy one, it is exact, and it is an upper bound on the 0/1 optimum, "
             "which the half-guarantee's proof uses. On the opening instance it is 240, made of "
             "`A` whole, `B` whole and two thirds of `C`."),
            ("Run the 0/1 rule and re-weigh what it took",
             "The panel adds up the picks independently and reports the weight used &mdash; 30 "
             "of 50 for density greedy on the opening instance. A rule that reported a value it "
             "could not carry would otherwise look like the winner."),
            ("Put it beside the 0/1 optimum, not beside the fractional one",
             "Comparing a whole-item answer with a cut-item answer measures the effect of "
             "cutting, not the quality of the rule. Density greedy's shortfall against 220 is "
             "the rule's; the further gap from 220 to 240 is the problem's."),
            ("Try every rule the panel offers before ranking them",
             "On the opening instance the naive value-first rule reaches the optimum and the "
             "principled density rule does not. On the six-item instance both fall short and "
             "lightest-first falls furthest. Three rules and four instances is twelve numbers, "
             "and no ordering of the rules survives all of them."),
            ("Separate the measured ratio from the proved one",
             "Write both down. The guaranteed arm reached `8/11` of the optimum here and the "
             "guarantee is `1/2`. The first is what happened; the second is what will happen on "
             "an instance you have not seen, and only the second is a reason to ship the "
             "algorithm."),
        ],
        "worked": {
            "title": "Three items and a capacity of fifty, four ways",
            "intro": [
                "Items `A 10/60`, `B 20/100`, `C 30/120`, written weight over value, with "
                "capacity 50. Densities `60/10 = 6`, `100/20 = 5`, `120/30 = 4`.",
            ],
            "lines": [
                "FRACTIONAL, densest first",
                "   A  take all 10     value  60     capacity left 40",
                "   B  take all 20     value 100     capacity left 20",
                "   C  take 20 of 30 = two thirds    value 80",
                "   total  60 + 100 + 80  =  240      exact, and an upper bound on the 0/1 answer",
                "",
                "0/1 OPTIMUM, the best of all 8 subsets",
                "   {B, C}   weight 50   value 220",
                "",
                "0/1 GREEDY, three orders",
                "   by density  A then B, C does not fit      value 160   weight 30 of 50",
                "   by value    C then B, A does not fit      value 220   weight 50 of 50",
                "   lightest    A then B, C does not fit      value 160   weight 30 of 50",
                "",
                "RATIOS against the 0/1 optimum of 220",
                "   density   160/220  =  8/11  =  0.727",
                "   value     220/220  =  1",
                "   lightest  160/220  =  8/11",
                "",
                "THE GUARANTEED ARM",
                "   density greedy                     160",
                "   most valuable single item that fits 120   (item C)",
                "   the better of the two               160",
                "   the promise, OPT / 2                110      met, with 50 to spare",
            ],
            "after": [
                "The twenty units of capacity density greedy leaves unused are the whole story. "
                "It spent its first ten on the densest item and then could not fit the third, "
                "while the optimum ignores density entirely and packs the capacity exactly. "
                "Nothing in the rule notices, because the rule never reconsiders `A`.",
                "The by-value rule reaching 220 here is worth resisting. It reaches the optimum "
                "on three of the four shipped instances, which is a better record than density's "
                "zero, and it has no guarantee either: an instance with one enormous heavy item "
                "and many smaller ones defeats it just as easily. Three rules, four instances, "
                "and not one proved statement among them without the second arm.",
                "For a faded rehearsal, work out all four figures for `12/24, 7/13, 11/23, 8/15, "
                "9/16, 5/9` with capacity 26 before running it. The supplied first move is the "
                "densities: `C` is densest at `23/11`, then `A` at 2, then `D` at `15/8`. Say "
                "what the fractional optimum is as a fraction, what the 0/1 optimum is over the "
                "64 subsets, what each of the three rules gets, and whether the guaranteed arm "
                "clears half.",
            ],
        },
        "quiz_title": "Exactness, ratios, and what a guarantee promises",
        "quiz": [
            {"q": "Which step of the fractional proof stops working in the 0/1 problem?",
             "a": ["Sorting by density, which is ill-defined when items are whole",
                   "Moving a small amount of capacity from a less dense item to a denser one, which is not a legal move when items cannot be cut",
                   "The claim that the capacity is used in full",
                   "The comparison of densities as exact fractions"],
             "c": 1,
             "why": "The whole argument is an exchange: shift `ε` of weight from the less dense "
                    "item to the denser one and the value does not fall. With whole items there "
                    "is no `ε` to shift. Sorting is still well-defined and exact-fraction "
                    "comparison is an implementation choice that holds in both problems."},
            {"q": "Density greedy returns 160 against an optimum of 220, a ratio of 8/11. What guarantee does that establish for the rule?",
             "a": ["That it always returns at least 8/11 of the optimum",
                   "That it returns at least 8/11 on instances of three items",
                   "None; on another shipped instance the same rule returns 2 where the optimum is 100, and no ratio holds for it in general",
                   "That it returns at least half, since 8/11 exceeds a half"],
             "c": 2,
             "why": "`8/11` is one measurement. On `1/2, 50/100` with capacity 50 the same rule "
                    "returns `1/50` of the optimum, and by scaling that instance the ratio can "
                    "be made as bad as you like. Plain density greedy has no approximation "
                    "ratio, which is exactly why the guarantee needs a second arm."},
            {"q": "The guaranteed arm returns 160 on the opening instance and half the optimum is 110. What does the gap between them mean?",
             "a": ["That the guarantee should be strengthened to 8/11",
                   "That the bound is loose on this instance; it is a floor and being far above the floor on four instances says nothing about the fifth",
                   "That the proof is not tight and probably wrong",
                   "That the second arm was unnecessary here"],
             "c": 1,
             "why": "A guarantee is a worst-case floor. The four shipped instances give `8/11`, "
                    "`3/5`, `1` and `47/51`, all comfortably above `1/2`, and instances "
                    "approaching the bound exist. Reading a floor as an estimate is the same "
                    "error as reading a measurement as a bound, from the other direction."},
            {"q": "Why does the half-guarantee's proof use the fractional optimum?",
             "a": ["Because the fractional optimum is easier to compute",
                   "Because it is an upper bound on the 0/1 optimum, so bounding it bounds what greedy is being compared against",
                   "Because density greedy and fractional greedy take the same items",
                   "Because the cut item is the one the second arm supplies"],
             "c": 1,
             "why": "The argument bounds the fractional optimum by `g + vᵢ`, and the 0/1 optimum "
                    "cannot exceed the fractional one, so the chain reaches `OPT`. That is the "
                    "same shape as the depth argument earlier on this course: bound every "
                    "solution from above by something computable, then compare."},
        ],
        "mistakes": [
            ("Comparing the 0/1 rule against the fractional optimum",
             "Density greedy's 160 against 240 mixes two different shortfalls: what the rule "
             "lost, and what cutting was worth. Against the 0/1 optimum of 220 the rule's own "
             "shortfall is 60, and the remaining 20 is the price of whole items, which no 0/1 "
             "algorithm can recover."),
            ("Concluding that value-first is the better rule",
             "It reaches the optimum on three of the four shipped instances and density greedy "
             "on none, which is twelve numbers and no theorem. Both rules are unbounded, and "
             "the reason density is the one with a name is that it is exact on the fractional "
             "problem &mdash; a fact about a different problem."),
            ("Reading the measured ratio as the guarantee, or the guarantee as an estimate",
             "Both directions are errors and both appear on this page. The measured ratios on "
             "the shipped instances run from `3/5` to `1` and none of them is what the algorithm "
             "promises; the promise is `1/2` and none of them is close to it. A guarantee tells "
             "you what will not happen, and a measurement tells you what did."),
        ],
        "standard": ("Finish when you can say, for a rule and a problem, whether you have a measurement, an unbounded heuristic, or a proved ratio, and produce the instance that decides it.",
                     "You should be able to solve the fractional problem by hand as an exact "
                     "fraction, run all three 0/1 rules, explain which step of the exchange "
                     "argument the integrality kills, prove the half-guarantee from the "
                     "fractional bound, and say why the loose ratios on the shipped instances "
                     "neither strengthen nor weaken it."),
        "note": ("The 0/1 knapsack is where greed runs out, and it is not where the problem "
                 "does. Its optimum is found here by trying all `2ⁿ` subsets, which is the only "
                 "honest thing a page can do with a greedy toolkit. The next course replaces "
                 "that enumeration with a table indexed by capacity, and it takes the same "
                 "instance as its opening example precisely because the rule that solved the "
                 "fractional version has just failed on it."),
    },
]
