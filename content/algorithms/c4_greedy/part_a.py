"""Greedy Algorithms and Matroids, lessons 01-05 - scheduling, and Huffman codes.

Every figure in these five dicts was read off the shipped lab by extracting the
`*_JS` blocks with the regex scripts/mathcheck.js uses and executing them under
node. Where a preset's recorded `note` disagrees with what the lab computes, the
lab wins and the prose says which caption is wrong: those strings are serialised
into the status line of every page and no check has ever held them to a run.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "greedy-rules-and-the-optimum",
        "title": "Greedy Rules and the Optimum",
        "module": "Rules and their proofs",
        "one_line": "Run four plausible selection rules on one instance and judge each against the best of every subset rather than against your intuition.",
        "summary": (
            "A greedy algorithm commits to a choice and never revisits it. Four rules for "
            "choosing non-overlapping activities all sound reasonable and three of them are "
            "wrong. Nothing on the page separates them except an optimum computed by trying "
            "every subset &mdash; and on the opening instance three of the four reach it. "
            "Each of the three that can fail has its own instance in the lab on which it does, "
            "and the only difference between the two runs is the input."
        ),
        "key": [
            "greedy: take the next feasible item by some rule, and never undo a choice",
            "feasible: no two chosen intervals overlap — checked pairwise, never inferred",
            "optimum: the largest feasible subset, over all 2ⁿ subsets of the input",
            "eleven intervals  →  2048 subsets  →  optimum 4",
            "earliest finish 4    earliest start 3    shortest 4    fewest conflicts 1",
            "three of the four match the optimum here, and two of those three are wrong rules",
        ],
        "key_label": "One instance, four rules, and the number that judges them",
        "concepts_intro": (
            "Three ideas: what makes a rule greedy, why a selection's size means nothing "
            "until its legality has been checked, and why an optimum that is computed rather "
            "than asserted changes what a lab can prove."
        ),
        "concepts": [
            ("A greedy rule is an order, plus a refusal to reconsider",
             "Fix an order on the input. Walk it once. Take the current item if taking it "
             "keeps the answer legal, and otherwise skip it forever. That is the whole "
             "pattern, and every difference between the four rules on this page is the order "
             "&mdash; earliest finish time, earliest start time, shortest first, fewest "
             "conflicts first. Nothing is ever put back, which is what makes these algorithms "
             "fast and what makes them capable of being wrong: a single bad early choice is "
             "never repaired."),
            ("A bigger selection may not be a legal one",
             "Two intervals are compatible when they do not overlap, and this course reads "
             "`3-8` as the half-open span from 3 up to but not including 8, so `3-8` and "
             "`8-11` both fit. A rule that returned six overlapping intervals would print a "
             "larger number than a rule that returned four legal ones, and the number alone "
             "cannot tell you which happened. So the panel runs `intervalsDisjoint` on every "
             "selection before it prints its size. On all four of the lab's instances every "
             "rule's selection passes that check &mdash; the column reads `yes` throughout "
             "&mdash; which is a measurement, not a reason to remove the check."),
            ("An enumerated optimum turns a claim into a computation",
             "Because a greedy rule commits and never revisits, its answer on a small "
             "instance can be put beside the best of every subset. The panel does exactly "
             "that: eleven intervals, `2¹¹ = 2048` subsets, each tested for feasibility, and "
             "the largest feasible one reported with its members. So the sentence on the "
             "screen is never &ldquo;greedy got four&rdquo;. It is &ldquo;greedy got four and "
             "the best of the 2048 is four, and here are its members&rdquo; &mdash; or, on "
             "another instance, &ldquo;greedy got one and the best of the eight is two, and "
             "here is the pair&rdquo;."),
        ],
        "read_title": "Four rules, one instance, and a number that settles it",
        "read_intro": "The problem, the four orders, what each one selects, and why three correct answers on one input establish nothing about three of the rules.",
        "body": [
            ("def", ("Interval scheduling",
                     "Given `n` intervals, each a half-open span `[s, f)` with `f &gt; s`, "
                     "select as many as possible so that no two of them overlap. A selection "
                     "is <strong>feasible</strong> when its intervals are pairwise disjoint, "
                     "and the <strong>optimum</strong> is the largest feasible selection. "
                     "Intervals that merely touch &mdash; one finishing exactly where the "
                     "next starts &mdash; do not overlap.")),
            ("p", "The lab opens on eleven intervals, labelled in the order they are typed: "
                  "`A 1-4`, `B 3-5`, `C 0-6`, `D 5-7`, `E 3-9`, `F 5-9`, `G 6-10`, `H 8-11`, "
                  "`I 8-12`, `J 2-14`, `K 12-16`. The labels are what every table names, so "
                  "one interval can be followed through four different orderings of the same "
                  "instance."),
            ("def", ("The four rules",
                     "<strong>Earliest finish</strong> sorts by `f` and sweeps. "
                     "<strong>Earliest start</strong> sorts by `s`. <strong>Shortest "
                     "first</strong> sorts by `f - s`. <strong>Fewest conflicts first</strong> "
                     "counts, for each interval, how many others it overlaps in the full "
                     "instance, sorts by that count, and sweeps. Each rule then walks its own "
                     "order once, taking an interval when it starts no earlier than the last "
                     "one taken finished.")),
            ("p", "That last clause is the implementation, and it is worth reading twice. The "
                  "sweep keeps one number &mdash; the finish time of the most recently taken "
                  "interval &mdash; and compares each candidate against it. For the "
                  "earliest-finish order that is the same thing as compatibility with "
                  "everything already chosen, because the chosen finish times only increase. "
                  "For the other three orders it is not, and the difference shows up below."),
            ("example", ("Eleven intervals, four answers",
                         "Earliest finish selects `A D H K`, four intervals. Earliest start "
                         "selects `C G K`, three. Shortest first selects `B D H K`, four. "
                         "Fewest conflicts selects `K` alone, one. All four selections are "
                         "feasible, checked pairwise. The best of the 2048 subsets is four, "
                         "attained by `A D H K`. So two rules match the optimum, one is one "
                         "short, and one is three short &mdash; on this instance.")),
            ("p", "The interesting entry there is shortest-first. It gets four, which is "
                  "optimal, and it is not a correct rule. The lab ships the three intervals "
                  "that prove it: `0-5, 4-6, 5-10`. Shortest-first takes the two-unit interval "
                  "in the middle, which blocks both of the others, and finishes with one where "
                  "the best of the eight subsets is two. One instance where a rule is wrong is "
                  "all it takes, and one instance where it is right is worth nothing at all."),
            ("h3", "Each losing rule has an instance built for it"),
            ("p", "Earliest start fails on `0-10, 1-2, 3-4, 5-6, 7-8`: the interval that starts "
                  "first occupies the whole day, the rule takes it and stops at one, and the "
                  "optimum is four. Fewest conflicts fails on `0-2, 2-4, 4-6, 6-8, 1-3, 3-5, "
                  "5-7`: it takes `A` and `D`, the two intervals with one conflict each, and "
                  "returns two against an optimum of four. Earliest finish has no such preset, "
                  "and the reason is not that nobody built one."),
            ("p", "The fewest-conflicts instance repays a careful look, because the panel's own "
                  "grey caption gets it wrong. That caption says taking the two ends "
                  "&ldquo;leaves the middle unusable&rdquo;. The table directly above it names "
                  "the optimum: `A B C D`, which is the two ends <em>and</em> the two middle "
                  "intervals. The middle is perfectly usable. What loses the two intervals is "
                  "the sweep: after `A` and then `D` the single finish-time pointer stands at "
                  "8, and `B` starting at 2 and `C` starting at 4 are both behind it. Where a "
                  "caption and the table disagree, the table is the measurement."),
            ("h3", "The rule the panel runs, and the rule the textbooks state"),
            ("p", "Fewest-conflicts is usually stated as a rule that recomputes the conflict "
                  "counts after each removal. The shipped implementation sorts once, by each "
                  "interval's conflict count in the full instance, and then sweeps &mdash; the "
                  "static-order variant. Both are wrong on some instance, the panel names the "
                  "one it ran, and the figures on this page are the static one's. A lesson "
                  "that quoted the dynamic rule's behaviour from a textbook while the page "
                  "computed the static one's would be teaching a third thing that is neither."),
            ("thm", ("The earliest-finish rule is optimal on every instance",
                     "For interval scheduling, the selection produced by sorting on finish "
                     "time and sweeping is a largest feasible selection, for every input. Not "
                     "&ldquo;usually&rdquo;, and not &ldquo;on the instances tried&rdquo;.")),
            ("p", "That is a claim about all inputs and the lab cannot establish it. What the "
                  "lab can do is the half that is checkable: for any instance you type, it "
                  "computes the optimum by enumeration and reports whether the rule matched. "
                  "The two proofs that close the other half &mdash; stays-ahead and the "
                  "exchange argument &mdash; are the subject of the material that follows this "
                  "page, and the second of them is performed rather than described."),
            ("p", "Stays-ahead is already visible here. Write `gᵢ` for the finish time of "
                  "greedy's `i`-th chosen interval and `oᵢ` for the optimum's, both in "
                  "increasing order. On the opening instance greedy's finish times are 4, 7, "
                  "11 and 16, and the panel reports that it never falls behind at any step. "
                  "The claim the proof makes is that `gᵢ ≤ oᵢ` for every `i` on every input, "
                  "which is induction, not four numbers."),
            ("p", "So the honest summary of this page is two sentences that do not say the "
                  "same thing. Measured: on the instance shown, earliest finish and shortest "
                  "first both reach the optimum of 4, earliest start reaches 3, fewest "
                  "conflicts reaches 1. Proved: earliest finish reaches the optimum on every "
                  "instance, and each of the other three has an instance on which it does not. "
                  "The first sentence is a count on one input. The second is the bound, and "
                  "nothing you can do to the controls will produce it."),
        ],
        "lab": ("greedy", {
            "mode": "intervals",
            "preset": "eleven",
            "panel_title": "Choose the instance, then choose the rule",
            "panel_intro": "The optimum is the best of every subset and knows nothing about any "
                           "of the four rules. Switch rules on one instance to see which of "
                           "them happen to be right here; switch instances with the rule fixed "
                           "to see the same rule stop being right.",
        }),
        "steps_title": "Judging a rule instead of admiring it",
        "steps_intro": "The order of these four matters: the last one is what turns an observation into a finding.",
        "steps": [
            ("Read the feasibility column before the size column",
             "A selection's size is meaningless until the selection is legal. The panel checks "
             "pairwise disjointness and prints the verdict; on every shipped instance it reads "
             "yes for all four rules, and that is a fact you confirm rather than assume."),
            ("Put the optimum beside the rule, every time",
             "Never write down what a rule selected without writing down what the best subset "
             "selected. The gap is the only thing that matters, and on this problem the gap is "
             "computed for you from an enumeration that has no idea the rules exist."),
            ("Change the instance with the rule held fixed",
             "This is the experiment that separates the rules, because switching rules on one "
             "instance cannot. Leave the rule on shortest-first and move through the four "
             "instances: 4, 1, 4 and 4 against optima of 4, 2, 4 and 4. The single 1 is the "
             "finding."),
            ("Name the step where a wrong rule went wrong",
             "Not &ldquo;it is a heuristic&rdquo;. On the shortest-first trap the rule takes "
             "the middle interval and blocks two; on the earliest-start trap it takes the "
             "interval spanning the whole day. Each failure is one identifiable commitment "
             "that could not be undone."),
        ],
        "worked": {
            "title": "The earliest-finish sweep on the opening instance, by hand",
            "intro": [
                "Sort the eleven intervals by finish time, then walk the sorted list once "
                "carrying a single number: the finish time of the last interval taken. Take "
                "the current interval when its start is at least that number.",
            ],
            "lines": [
                "sorted by finish   A 1-4  B 3-5  C 0-6  D 5-7  E 3-9  F 5-9",
                "                   G 6-10  H 8-11  I 8-12  J 2-14  K 12-16",
                "",
                "   interval   start   last finish   decision",
                "   A 1-4        1         -         TAKE      last = 4",
                "   B 3-5        3         4         skip",
                "   C 0-6        0         4         skip",
                "   D 5-7        5         4         TAKE      last = 7",
                "   E 3-9        3         7         skip",
                "   F 5-9        5         7         skip",
                "   G 6-10       6         7         skip",
                "   H 8-11       8         7         TAKE      last = 11",
                "   I 8-12       8        11         skip",
                "   J 2-14       2        11         skip",
                "   K 12-16     12        11         TAKE      last = 16",
                "",
                "selection   A D H K        finish times 4, 7, 11, 16",
                "feasible    yes, pairwise",
                "optimum     4, the best of 2048 subsets, attained by A D H K",
            ],
            "after": [
                "Four takes and seven skips, one pass, no interval reconsidered. The seven "
                "skips are where a greedy algorithm earns its speed and risks its "
                "correctness: `C 0-6` was rejected at step three and never looked at again, "
                "although at that moment nothing had been chosen that conflicted with it "
                "except `A`.",
                "Notice that the enumerated optimum came back as `A D H K` &mdash; greedy's own "
                "answer. That is a coincidence of this instance and it matters in the material "
                "that follows, where the exchange argument has nothing to do when the optimum "
                "the search returns is already the rule's answer. Switch the rule to shortest "
                "first, which selects `B D H K`, and the same enumeration still returns "
                "`A D H K`: now the two differ in one interval.",
                "For a faded rehearsal, predict the sweep for earliest start on the same "
                "eleven before running it. The supplied first move is this: sorted by start "
                "the list opens `C 0-6`, `A 1-4`, `J 2-14`, and the rule takes `C`, which "
                "finishes at 6 and rules out five of the remaining ten. Say what it ends with "
                "and how many that is, then check &mdash; and then say which single interval "
                "you would delete to make earliest start optimal here.",
            ],
        },
        "quiz_title": "Rules, optima, and what a match is worth",
        "quiz": [
            {"q": "On the opening instance shortest-first selects four intervals and the optimum is four. What has been established about shortest-first?",
             "a": ["That it is optimal for interval scheduling",
                   "That it is optimal whenever the intervals have distinct lengths",
                   "That it is optimal on this instance, and nothing beyond it",
                   "Nothing at all, because its selection was not checked feasible"],
             "c": 2,
             "why": "The selection was checked feasible &mdash; the panel prints that column "
                    "&mdash; so the four is real. What it is not is a bound. The lab ships "
                    "`0-5, 4-6, 5-10`, on which the same rule selects one where two fit, and "
                    "one such instance is enough to refute the general claim."},
            {"q": "A rule reports a selection of size 6 on an instance where the optimum is 4. What is the first thing to conclude?",
             "a": ["The enumeration is wrong, since a rule cannot beat the optimum",
                   "The selection is infeasible: the optimum is over all feasible subsets, so nothing legal can exceed it",
                   "The rule found a better optimum",
                   "The intervals must have been read as closed rather than half-open"],
             "c": 1,
             "why": "The optimum is the largest <em>feasible</em> subset, so no legal selection "
                    "can be larger. A bigger number means the selection overlaps, which is "
                    "exactly why the panel checks disjointness before printing a size. On the "
                    "shipped instances that check has never fired, and the check is still the "
                    "reason the sizes can be trusted."},
            {"q": "Why does switching rules on a single instance fail to separate the four rules?",
             "a": ["Because the optimum is recomputed for each rule",
                   "Because the rules happen to sort the same way on small inputs",
                   "Because three of the four reach the optimum on the opening instance, so the experiment cannot distinguish a correct rule from a lucky one",
                   "Because the feasibility check passes for all of them"],
             "c": 2,
             "why": "Earliest finish, shortest first and fewest conflicts are not all correct, "
                    "yet on the opening instance two of them reach 4. The experiment that "
                    "separates them holds the rule fixed and changes the instance, which is "
                    "why the lab ships one trap per losing rule."},
            {"q": "The panel's caption on the fewest-conflicts instance says that taking the two end intervals leaves the middle unusable, while the table above it names the optimum as those two ends plus the two middle intervals. What should you write down?",
             "a": ["The caption, since it explains the result",
                   "The table, and the reason the rule loses: its sweep keeps one finish-time pointer, which has already passed the middle",
                   "Neither, since a disagreement means the lab is broken",
                   "The caption, and treat the table as an artefact of enumeration"],
             "c": 1,
             "why": "`A B C D` is feasible and is the optimum, so the middle is usable. The "
                    "rule loses it because it considered `D`, which finishes at 8, before `B` "
                    "and `C`, which start at 2 and 4. The caption is prose that nothing checks; "
                    "the table is the run."},
        ],
        "mistakes": [
            ("Reading a match with the optimum as a proof",
             "The most common error on this page, and the whole reason the page exists. Three "
             "of the four rules reach 4 on the opening instance and only one of them is a "
             "correct algorithm. Any sentence of the form &ldquo;the rule works, I checked "
             "it&rdquo; is a statement about one input, and this course will keep asking which "
             "input."),
            ("Trusting a size without the feasibility column",
             "Greedy rules on this problem cannot produce overlapping selections, because the "
             "sweep compares against the last finish time &mdash; but that is a property of "
             "the implementation, not of the word &ldquo;greedy&rdquo;. Hand-built selections, "
             "and rules written differently, can and do overlap, and the only defence is a "
             "pairwise check on the selection you are about to believe."),
            ("Assuming the shipped fewest-conflicts rule is the one in your textbook",
             "The panel runs the static-order variant: conflict counts are taken once, in the "
             "full instance, and never recomputed. The dynamic version recounts after every "
             "removal and is a different algorithm with different output. The page says which "
             "it ran; reading the label and supplying the other algorithm's behaviour from "
             "memory produces figures that match neither."),
        ],
        "standard": ("Finish when you can take a selection rule you have not seen before and produce, from the lab, either a proof obligation or a counterexample.",
                     "You should be able to state the half-open convention and say why `3-8` "
                     "and `8-11` are compatible, run any of the four sweeps by hand, explain "
                     "why the enumerated optimum is a different kind of object from a rule's "
                     "output, and &mdash; given a rule that matched the optimum on the instance "
                     "in front of you &mdash; say precisely what remains unproved."),
        "note": ("The two ways of closing that gap are the material that follows. Stays-ahead "
                 "is the one already on this page: greedy's `i`-th finish time never exceeds "
                 "the optimum's, checked here step by step and proved by induction. &ldquo;The "
                 "Exchange Argument&rdquo; is the other, and it is not described there but "
                 "performed &mdash; an optimum turned into greedy's own answer one swap at a "
                 "time, with the set rechecked after every swap."),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-exchange-argument",
        "title": "The Exchange Argument",
        "module": "Rules and their proofs",
        "one_line": "Turn an optimal solution into greedy's own answer one swap at a time, and watch the same procedure break at a named step on a rule that is wrong.",
        "summary": (
            "The standard proof that a greedy rule is optimal starts from some optimal "
            "solution and rewrites it, choice by choice, into the rule's answer, checking after "
            "every swap that what remains is still legal and still as large. The lab performs "
            "that rewriting rather than describing it. On the earliest-finish rule every swap "
            "survives; on shortest-first it fails at the first swap, and the failure is in the "
            "feasibility half rather than the size half."
        ),
        "key": [
            "start from an optimum O, and let g₁, g₂, … be greedy's choices in order",
            "swap i: put gᵢ into O at position i, dropping whatever O had there",
            "after every swap, recheck TWO things: still feasible, and still the same size",
            "earliest finish on 0-5, 4-6, 5-10: two swaps, both survive",
            "shortest first on the same three: swap 1 gives B C, which OVERLAPS",
            "the swap that breaks is where the textbook proof stops working",
        ],
        "key_label": "One proof, run as a sequence of swaps",
        "concepts_intro": (
            "Three ideas: what the argument is for, what has to be rechecked after each swap, "
            "and why a rewriting that never breaks is a proof while a rewriting that happens "
            "to succeed on one instance is not."
        ),
        "concepts": [
            ("The argument transforms an optimum, it does not build one",
             "An exchange argument never asks what the optimum is. It says: take any optimal "
             "solution `O` whatever it is, and show that `O` can be edited into greedy's answer "
             "without ever losing optimality. If that editing always works then greedy's answer "
             "is itself optimal, because it is what `O` became. The edit is done in greedy's "
             "order: the first swap forces greedy's first choice in, the second forces its "
             "second choice in, and so on."),
            ("Each swap has two obligations, not one",
             "Putting `gᵢ` into the set is only safe if the result is still a legal selection "
             "&mdash; no two intervals overlap &mdash; <em>and</em> still has as many intervals "
             "as before. Those are different failures and the panel reports them in different "
             "columns. On the shortest-first trap the set after the first swap is still size 2 "
             "and is not feasible; on the fewest-conflicts trap the set after the second swap "
             "is still feasible and has lost an interval. A proof has to close both."),
            ("A run that survives is evidence; a proof is about every optimum",
             "The panel starts from one optimum &mdash; the one its enumeration happened to "
             "return &mdash; and edits that one. The theorem quantifies over all optimal "
             "solutions and all instances. So a green chain here does not prove the rule, and a "
             "red one does refute it: a single optimum that cannot be rewritten is a "
             "counterexample to the argument, and on these instances it comes with the losing "
             "rule's own trap attached."),
        ],
        "read_title": "The proof, performed",
        "read_intro": "What an exchange argument claims, the two checks each swap must pass, the swap that breaks on a wrong rule, and the case where the argument has nothing to do.",
        "body": [
            ("def", ("The exchange argument",
                     "Let `g₁, g₂, …, g_k` be greedy's choices in the order it made them, and "
                     "let `O` be any optimal solution. For `i = 1, 2, …, k` in turn, replace "
                     "the `i`-th element of `O` (in the same order greedy uses) by `gᵢ`, "
                     "leaving `gᵢ` alone if it is already there. The argument succeeds when "
                     "every intermediate set is feasible and has the same size as `O`.")),
            ("p", "If it succeeds then after `k` swaps the set contains all of greedy's choices "
                  "and is still optimal, and a feasible set containing greedy's answer cannot "
                  "be larger than greedy's answer, because greedy stopped only when nothing "
                  "more could be added. So greedy's answer is optimal. That last step is worth "
                  "saying out loud: it is where the rule's own stopping condition enters the "
                  "proof, and it is why the argument is about greedy rather than about swaps."),
            ("example", ("Three intervals, two rules, two outcomes",
                         "The lab opens on `0-5, 4-6, 5-10`, labelled `A`, `B`, `C`. The "
                         "optimum is `A C`, size 2, out of eight subsets. Under earliest "
                         "finish, greedy also selects `A C`, so both swaps find their target "
                         "already in place and the chain survives. Under shortest first, greedy "
                         "selects `B` alone; the first swap puts `B` in for `A`, giving the set "
                         "`B C`, which is still size 2 and is <strong>not feasible</strong>, "
                         "because `B` runs from 4 to 6 and `C` from 5 to 10. The chain stops "
                         "there.")),
            ("p", "That is the whole of the negative result and it took one swap. The proof "
                  "template for earliest finish does not merely fail to apply to shortest "
                  "first; it produces, at a named step, a specific infeasible set from a "
                  "specific optimum. The panel prints the set &mdash; `B C` &mdash; and runs a "
                  "feasibility check on it separately, so the verdict is not the chain's own "
                  "opinion of itself."),
            ("h3", "The two ways a swap can fail, and which trap shows which"),
            ("p", "On `0-10, 1-2, 3-4, 5-6, 7-8` under earliest start, greedy takes `A` alone. "
                  "The first swap puts `A` in for `B` and gives `A C D E`, which has the right "
                  "size and overlaps, since `A` spans the whole day. On `0-2, 2-4, 4-6, 6-8, "
                  "1-3, 3-5, 5-7` under fewest conflicts the opposite happens: the first swap "
                  "is a no-op, the second puts `D` in for `B`, and the resulting set `A D C` is "
                  "perfectly feasible and has three intervals where the optimum had four. On "
                  "the eleven-interval instance under earliest start the chain manages both "
                  "&mdash; three swaps, the first two same-size and overlapping, the third "
                  "feasible and down to three."),
            ("p", "So the size column and the feasibility column both fire somewhere, on "
                  "different instances, and a reader who only watched one of the traps would "
                  "conclude the argument always breaks the same way. It does not, and there is "
                  "no reason it should: the two obligations are independent."),
            ("thm", ("Exchange proves the earliest-finish rule",
                     "For interval scheduling with the earliest-finish rule, every swap in the "
                     "sequence above keeps the set feasible and keeps its size, for every "
                     "instance and every optimal solution. Hence the rule is optimal on every "
                     "instance.")),
            ("proof", ("Take the first index `i` at which `O` and greedy differ, so greedy's "
                       "first `i - 1` choices are already in `O`. Let `o` be the `i`-th "
                       "interval of `O` in increasing finish order and `gᵢ` greedy's `i`-th "
                       "choice.",
                       "Greedy considered every interval compatible with its first `i - 1` "
                       "choices and took the one finishing earliest, so `f(gᵢ) ≤ f(o)`. "
                       "Replacing `o` by `gᵢ` therefore leaves every later interval of `O` "
                       "still compatible, because each of them starts at or after `f(o)` and "
                       "so at or after `f(gᵢ)`. The earlier intervals of `O` are greedy's own "
                       "first `i - 1` choices, which `gᵢ` is compatible with by construction.",
                       "The size is unchanged because one interval was removed and one added, "
                       "and `gᵢ` was not already present by the choice of `i`. Repeating drives "
                       "the first difference forward one position at a time, so after at most "
                       "`k` swaps `O` contains all of greedy's choices while remaining feasible "
                       "and optimal.")),
            ("p", "The step that breaks for the other three rules is the inequality "
                  "`f(gᵢ) ≤ f(o)`. Nothing about sorting by length, or by start time, or by "
                  "conflict count makes greedy's `i`-th choice finish no later than the "
                  "optimum's, and the traps are instances where it finishes later. That single "
                  "inequality is the entire content of the proof, and it is the reason "
                  "earliest finish is the rule and the other three are folklore."),
            ("h3", "When the chain has nothing to do"),
            ("p", "On the eleven-interval instance under earliest finish, the panel reports "
                  "four swaps and every one of them reads &ldquo;already there&rdquo;. Nothing "
                  "was exchanged. That is not the argument working particularly well; it is the "
                  "enumeration having returned `A D H K`, which is greedy's own answer, so the "
                  "first difference never arrives. Switch the rule to shortest first on the same "
                  "eleven and the first swap becomes real: `A` out, `B` in, giving `B D H K`, "
                  "still feasible and still four."),
            ("p", "This is a small trap in reading the lab and a large one in reading a proof. "
                  "A chain of no-ops proves nothing about the rule, because the argument was "
                  "never exercised. When you want to see the machinery work, pick a rule whose "
                  "answer differs from the optimum the panel found, and watch a swap actually "
                  "replace something."),
            ("p", "Measured on this page: on the three-interval instance the earliest-finish "
                  "chain survives 2 swaps and the shortest-first chain breaks at swap 1 with "
                  "the set `B C`. Proved on this page: the earliest-finish chain survives every "
                  "swap on every instance, by the inequality above. The lab cannot reach the "
                  "second sentence, and the second sentence is the only one that licenses using "
                  "the rule on an input nobody has tried."),
        ],
        "lab": ("greedy", {
            "mode": "intervals",
            "preset": "shortestfails",
            "panel_title": "Watch the chain survive, then make it break",
            "panel_intro": "The lower table performs the exchange argument one swap at a time "
                           "and rechecks the set after each. Leave the instance alone and move "
                           "the rule between shortest first and earliest finish: the same three "
                           "intervals give a broken chain and a clean one.",
        }),
        "steps_title": "Running an exchange argument by hand",
        "steps_intro": "Four steps, and the third is the one that is usually skipped.",
        "steps": [
            ("Write greedy's choices down in order first",
             "The argument is indexed by greedy's own sequence, not by the optimum's. Get "
             "`g₁, g₂, …` on paper before touching `O`, because the swap at position `i` is "
             "defined by `gᵢ` and nothing else."),
            ("Do the swap at the first position where the two differ",
             "Earlier positions are already equal by construction and swapping there is a "
             "no-op. If every position is a no-op, as happens on the eleven-interval instance "
             "under earliest finish, the argument has not been exercised and you have learned "
             "nothing from it."),
            ("Recheck feasibility and size separately, after every swap",
             "These fail on different instances. The shortest-first trap produces a same-size "
             "infeasible set at the first swap; the fewest-conflicts trap produces a feasible "
             "smaller one at the second. Checking only the one you expect is how a broken "
             "argument gets written up as a working one."),
            ("Find the inequality the swap needed, and ask whether the rule supplies it",
             "For earliest finish it is `f(gᵢ) ≤ f(o)`, and the sort order supplies it "
             "directly. Write the corresponding inequality for the rule you are testing; if "
             "the rule's order does not give it to you, you have found where to look for the "
             "counterexample."),
        ],
        "worked": {
            "title": "Both chains on the three-interval instance",
            "intro": [
                "The instance is `A 0-5`, `B 4-6`, `C 5-10`. The optimum found by enumeration "
                "is `A C`, size 2, and `A` and `C` are compatible because `A` finishes exactly "
                "where `C` starts.",
            ],
            "lines": [
                "EARLIEST FINISH     greedy takes A, then C",
                "   swap 1   g1 = A, already in O           set A C   feasible   size 2",
                "   swap 2   g2 = C, already in O           set A C   feasible   size 2",
                "   verdict  survives every swap; the set ends as greedy's own answer",
                "",
                "SHORTEST FIRST      lengths A 5, B 2, C 5, so greedy takes B and stops",
                "   swap 1   g1 = B, replacing A            set B C   OVERLAPS   size 2",
                "   verdict  breaks at swap 1",
                "",
                "why B C overlaps      B = 4-6 and C = 5-10 share the span 5 to 6",
                "which half failed     feasibility; the size was still 2",
                "the rule's own result greedy 1, optimum 2, over all 8 subsets",
            ],
            "after": [
                "The two chains differ in one line and that line is the whole argument. Under "
                "earliest finish the first swap is forced by `f(g₁) ≤ f(o)`, which here reads "
                "`5 ≤ 5`. Under shortest first there is no such inequality available: `g₁` is "
                "`B`, which finishes at 6, and the optimum's first interval finishes at 5.",
                "It is worth being precise about what the broken chain refutes. It does not "
                "refute shortest-first on all instances by itself &mdash; the page beside it "
                "does that, by reporting greedy 1 against an optimum of 2. What it refutes is "
                "the <em>proof</em>: the template that works for earliest finish produces an "
                "infeasible set here, so it cannot be repaired by being more careful.",
                "For a faded rehearsal, run the chain for earliest start on `0-10, 1-2, 3-4, "
                "5-6, 7-8`. The supplied first move is this: greedy takes `A 0-10` alone, the "
                "optimum is `B C D E`, and the first swap puts `A` in for `B`. Say what the "
                "resulting set is, which of the two checks it fails, and what that tells you "
                "about the missing inequality &mdash; then do the same for fewest conflicts on "
                "the seven-interval instance, where the chain survives longer and fails the "
                "other check.",
            ],
        },
        "quiz_title": "Swaps, checks, and what a surviving chain means",
        "quiz": [
            {"q": "Under the earliest-finish rule on the eleven-interval instance, all four swaps report `already there`. What does that establish?",
             "a": ["That the exchange argument is valid for this rule",
                   "That the enumeration returned greedy's own answer, so the argument was never exercised on this instance",
                   "That greedy's answer is the unique optimum",
                   "That the rule is optimal on instances of this size"],
             "c": 1,
             "why": "The search returned `A D H K`, which is exactly what earliest finish "
                    "selects, so the first difference never occurs and no swap does anything. "
                    "The argument is valid for this rule, but that is proved in the lesson, not "
                    "by a chain of no-ops. Other optima of size four exist, so uniqueness does "
                    "not follow either."},
            {"q": "On the shortest-first trap the chain breaks with the set `B C`, size 2, infeasible. Which half of the argument failed?",
             "a": ["The size half: the set should have grown",
                   "The feasibility half: the set kept its size and stopped being legal",
                   "Both halves at once",
                   "Neither; the chain simply ran out of swaps"],
             "c": 1,
             "why": "The panel prints them separately and reports `false/true`: not feasible, "
                    "size kept. `B` runs from 4 to 6 and `C` from 5 to 10, so they overlap. On "
                    "other traps it is the size that goes &mdash; the fewest-conflicts chain "
                    "on the seven-interval instance falls from four to three while staying "
                    "feasible &mdash; which is why both columns exist."},
            {"q": "Which inequality does the earliest-finish exchange argument actually need?",
             "a": ["`s(gᵢ) ≤ s(o)`, greedy starts no later",
                   "`f(gᵢ) ≤ f(o)`, greedy's i-th choice finishes no later than the optimum's",
                   "`f(gᵢ) - s(gᵢ) ≤ f(o) - s(o)`, greedy's choice is no longer",
                   "That greedy's choice conflicts with no interval of the optimum"],
             "c": 1,
             "why": "Finishing no later is what keeps every later interval of the optimum "
                    "compatible after the swap, and sorting by finish time supplies it "
                    "directly. Greedy's choice may well start later, may well be longer, and "
                    "certainly may conflict with intervals of the optimum it is replacing."},
            {"q": "A colleague reports that their new rule's exchange chain survived on all four of the lab's instances. What follows?",
             "a": ["The rule is optimal for interval scheduling",
                   "The rule is optimal on inputs of at most eleven intervals",
                   "Four chains survived, which is evidence and not a proof; the theorem is about every instance and every optimum",
                   "Nothing, because the chains started from a single optimum each"],
             "c": 2,
             "why": "Four surviving chains are four data points, and the panel edits one optimum "
                    "per instance rather than all of them. They are worth having &mdash; a "
                    "single broken chain would refute the rule &mdash; but the claim that "
                    "licenses use on an unseen input is the inequality argument, not the count "
                    "of chains that happened to close."},
        ],
        "mistakes": [
            ("Treating a surviving chain as the proof",
             "The chain edits one optimum on one instance. The theorem quantifies over every "
             "optimum on every instance, and the difference is exactly the difference between a "
             "measurement and a bound. The asymmetry is real and useful, though: one broken "
             "chain is conclusive against the argument, while any number of intact ones is not "
             "conclusive for it."),
            ("Checking only the failure you expect",
             "Readers who meet the shortest-first trap first come away believing the exchange "
             "argument fails by producing overlaps. Readers who meet the fewest-conflicts trap "
             "come away believing it fails by losing an interval from a set that is still "
             "feasible. Both happen, in different places, and a check that only looks for one "
             "of them passes the other."),
            ("Swapping in the optimum's order rather than greedy's",
             "The index `i` runs over greedy's choices. Editing `O` toward greedy in the "
             "optimum's own order is a different procedure, and on an instance where the two "
             "sequences interleave it can break where the real argument does not. Write "
             "`g₁, g₂, …` down first, and let them drive."),
        ],
        "standard": ("Finish when you can run the chain by hand for any of the four rules and, on a failure, say which of the two checks failed and what inequality was missing.",
                     "You should be able to state the argument without looking, explain why it "
                     "ends by invoking greedy's stopping condition, produce the swap that "
                     "breaks on each of the three losing rules, and say why a chain made "
                     "entirely of no-ops has told you nothing."),
        "note": ("Both templates on this course so far argue that greedy meets the optimum. "
                 "The material that follows argues the other way round: it computes a quantity "
                 "that no schedule whatever can beat, and then shows greedy meeting it. A "
                 "lower bound and a stays-ahead argument answer the same question and leave "
                 "different things to check, and &ldquo;Interval Partitioning and the "
                 "Depth&rdquo; is where the difference is easiest to see."),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "interval-partitioning-and-the-depth",
        "title": "Interval Partitioning and the Depth",
        "module": "Rules and their proofs",
        "one_line": "Compute a number that no schedule can beat, then watch a greedy rule meet it exactly, with the certificate listed rather than asserted.",
        "summary": (
            "Every interval must now be scheduled, into as few rooms as possible. The greedy "
            "rule opens a new room only when no existing one is free. The proof is not a "
            "stays-ahead or an exchange argument: it is a lower bound &mdash; the largest "
            "number of intervals alive at any single instant &mdash; computed by a routine that "
            "shares nothing with the scheduler, together with the list of intervals that "
            "attains it."
        ),
        "key": [
            "depth: the most intervals alive at one instant — a bound on EVERY schedule",
            "greedy by start time: first free room, else open a new one",
            "ten lectures  →  3 rooms used, depth 3, certified at t = 2 by A B C",
            "the three intervals live at t = 2 pairwise overlap, so no two share a room",
            "rooms = depth on all four shipped instances, in both orders offered",
            "0-1, 1-4, 2-5, 4-9, 5-8: by start 2 rooms, by finish 3, depth 2",
        ],
        "key_label": "A bound computed separately, and a rule that meets it",
        "concepts_intro": (
            "Three ideas: why a lower bound is a different kind of argument, what makes the "
            "depth a bound on every schedule rather than on this one, and why the certificate "
            "is listed on the page instead of being taken on trust."
        ),
        "concepts": [
            ("A lower bound argues about every solution at once",
             "Stays-ahead and exchange both reason about greedy against an optimum. A lower "
             "bound does not mention greedy at all: it names a quantity `d` and proves that no "
             "solution can use fewer than `d` rooms, whatever produced it. Then it is enough to "
             "show greedy uses `d`. The two halves are completely independent, which is why "
             "the panel computes them with two routines that share no code and prints both."),
            ("The depth is a bound because overlapping intervals cannot share a room",
             "Fix any instant `t` and look at the intervals alive there. They all contain `t`, "
             "so every two of them overlap, so no two can go in the same room, so any schedule "
             "needs at least that many rooms. Take the instant where this count is largest and "
             "you have the <strong>depth</strong>. Nothing in that sentence mentions an "
             "algorithm, which is exactly what makes it apply to all of them."),
            ("A certificate is an object, not a number",
             "&ldquo;The depth is 3&rdquo; is a claim a reader has to trust. The panel instead "
             "prints the instant &mdash; `t = 2` on the opening instance &mdash; and the "
             "intervals alive there, `A`, `B` and `C`, and separately confirms that those three "
             "pairwise overlap. A reader can check that by eye in a few seconds and does not "
             "have to believe anything about how the depth was computed."),
        ],
        "read_title": "Rooms used, rooms needed, and the instant that proves it",
        "read_intro": "The problem, the rule, the bound, the certificate, and the one control on this panel that changes nothing on any shipped instance.",
        "body": [
            ("def", ("Interval partitioning",
                     "Given `n` intervals, assign every one of them to a room so that no room "
                     "holds two overlapping intervals, using as few rooms as possible. Unlike "
                     "interval scheduling, nothing may be discarded: the question is not which "
                     "intervals to keep but how many rooms they need.")),
            ("def", ("Depth",
                     "For an instant `t`, the intervals <strong>alive</strong> at `t` are those "
                     "with `s ≤ t &lt; f`. The <strong>depth</strong> of an instance is the "
                     "largest number of intervals alive at any single instant. The panel "
                     "reports the instant that attains it alongside the number.")),
            ("p", "The lab opens on ten lectures: `A 0-3`, `B 1-4`, `C 2-5`, `D 4-7`, `E 5-8`, "
                  "`F 6-9`, `G 8-11`, `H 9-12`, `I 10-13`, `J 12-15`. Greedy by start time "
                  "opens three rooms and fills them `A D G J`, `B E H` and `C F I`. Every room "
                  "is checked: no room holds two intervals that overlap, and all ten intervals "
                  "were placed exactly once."),
            ("example", ("The certificate at t = 2",
                         "The depth is 3, attained at `t = 2`, where `A 0-3`, `B 1-4` and "
                         "`C 2-5` are all alive. Those three pairwise overlap, so no schedule "
                         "of any kind can put two of them in one room, so no schedule uses "
                         "fewer than three rooms. Greedy used three. The two numbers were "
                         "computed by separate routines and they agree, which is optimality "
                         "demonstrated rather than asserted.")),
            ("thm", ("Greedy by start time uses exactly the depth",
                     "Sorting the intervals by start time and assigning each to the "
                     "lowest-numbered room whose last booking has already finished opens "
                     "exactly `d` rooms, where `d` is the depth. Hence it is optimal on every "
                     "instance.")),
            ("proof", ("Suppose the rule opens room number `d + 1` while placing some interval "
                       "`x`. It only opens a new room when every one of rooms `1` through `d` "
                       "is busy, which means each of those rooms holds an interval that has not "
                       "finished by `s(x)`.",
                       "Every such interval started at or before `s(x)`, because the rule "
                       "processes intervals in increasing start order and each of them was "
                       "placed earlier. So each of those `d` intervals satisfies `s ≤ s(x)` and "
                       "`f &gt; s(x)`, and is alive at the instant `s(x)`. Together with `x` "
                       "itself that is `d + 1` intervals alive at one instant.",
                       "So the depth is at least `d + 1`, contradicting the assumption that it "
                       "is `d`. The rule therefore never opens more than `d` rooms, and since "
                       "no schedule can use fewer, it uses exactly `d`.")),
            ("p", "That proof needs the start order and uses it twice. The panel offers a "
                  "second order &mdash; by finish time &mdash; and the theorem says nothing "
                  "about it. On all four shipped instances the finish order opens the same "
                  "number of rooms as the start order: three, two, five and one. A reader who "
                  "moved that control on the presets and concluded the order does not matter "
                  "would have measured four inputs and generalised to all of them."),
            ("p", "It does matter, and the instance is small. Type `0-1, 1-4, 2-5, 4-9, 5-8`. "
                  "The depth is 2, attained at `t = 2`. By start time greedy opens two rooms, "
                  "`A B D` and `C E`. By finish time it opens three: `A B E`, `C` and `D`. The "
                  "finish order places `E 5-8` into the first room because `B` finished at 4, "
                  "and then `D 4-9` fits nowhere. Same intervals, same rule shape, one more "
                  "room than the bound."),
            ("h3", "Why this proof looks different from the two before it"),
            ("p", "The earlier arguments on this course both compare greedy with an optimal "
                  "solution: stays ahead of it, or can be reached from it by swaps. This one "
                  "never mentions an optimal solution. It proves a fact about every schedule "
                  "&mdash; at least `d` rooms &mdash; and separately a fact about this one "
                  "&mdash; at most `d` rooms. Two inequalities from two arguments, meeting."),
            ("p", "That shape recurs for the rest of this path. An approximation ratio is the "
                  "same construction with the two sides not meeting: a bound on every solution "
                  "on one side, a measured quantity on the other, and the gap between them as "
                  "the guarantee. This is the page where the gap happens to be zero, and "
                  "noticing that it is a special case rather than the normal case is most of "
                  "what the page is for."),
            ("h3", "What the panel checks that a reader would otherwise assume"),
            ("p", "Three things, and each exists because the corresponding claim is otherwise "
                  "unverifiable. `roomsValid` confirms that every room's intervals are pairwise "
                  "disjoint and that every input interval appears in exactly one room &mdash; "
                  "an assignment that quietly dropped an interval would use fewer rooms and "
                  "look better. `liveAt` lists the intervals alive at the certifying instant "
                  "rather than reporting their number. `mutuallyOverlapping` then confirms that "
                  "those listed intervals really do pairwise overlap, which is the step that "
                  "makes the bound a bound."),
            ("p", "Measured on this page: on the ten lectures greedy by start opens 3 rooms, "
                  "the depth is 3, the certifying instant is `t = 2`, and the three intervals "
                  "there pairwise overlap; on the five-interval pile-up all five are alive at "
                  "`t = 4` and five rooms are used; on the disjoint instance the depth is 1. "
                  "Proved on this page: the start-order rule uses exactly the depth on every "
                  "instance. The finish order has no such theorem, and the five-interval "
                  "instance above is why."),
        ],
        "lab": ("greedy", {
            "mode": "partition",
            "preset": "lectures",
            "panel_title": "Choose the instance, and the order the rule considers it in",
            "panel_intro": "The rooms greedy opens and the depth are two separate calculations "
                           "and the panel prints both. It also prints the instant that attains "
                           "the depth and the intervals alive there, so the lower bound is an "
                           "object you can check rather than a number you are given.",
        }),
        "steps_title": "Proving a schedule optimal without finding the optimum",
        "steps_intro": "Four steps. The third is the one that turns a number into a proof.",
        "steps": [
            ("Run the rule and count the rooms",
             "Assign each interval, in increasing start order, to the lowest-numbered room "
             "whose last booking has finished; open a new room only when none has. Record how "
             "many rooms that took. This is the upper bound and it is about your schedule."),
            ("Compute the depth separately",
             "Do not read it off the rooms. Sweep the instants, count what is alive at each, "
             "take the largest. On the opening instance that is 3, at `t = 2`. This is the "
             "lower bound and it is about every schedule."),
            ("Write down the certificate, not the number",
             "Name the instant and list the intervals alive there, then check that they "
             "pairwise overlap. Three intervals that pairwise overlap need three rooms in any "
             "schedule whatsoever, and that sentence is the proof. &ldquo;The depth is 3&rdquo; "
             "on its own is something a reader has to take on faith."),
            ("Compare the two numbers, and say which argument each came from",
             "Equal means optimal on this instance, for a reason that is on the screen. If they "
             "ever differ under the start order, something is wrong with the run rather than "
             "with the theory &mdash; and if they differ under the finish order, nothing is "
             "wrong at all, because no theorem covers it."),
        ],
        "worked": {
            "title": "Ten lectures, three rooms, and the instant that forces them",
            "intro": [
                "Intervals in typed order: `A 0-3`, `B 1-4`, `C 2-5`, `D 4-7`, `E 5-8`, "
                "`F 6-9`, `G 8-11`, `H 9-12`, `I 10-13`, `J 12-15`. They are already in "
                "increasing start order, so the rule walks them as typed.",
            ],
            "lines": [
                "   interval   rooms free at its start        goes to",
                "   A 0-3      none open yet                  open room 1   r1 free at 3",
                "   B 1-4      r1 busy until 3                open room 2   r2 free at 4",
                "   C 2-5      r1 busy, r2 busy               open room 3   r3 free at 5",
                "   D 4-7      r1 free since 3                room 1        r1 free at 7",
                "   E 5-8      r1 busy, r2 free since 4       room 2        r2 free at 8",
                "   F 6-9      r1 busy, r2 busy, r3 free      room 3        r3 free at 9",
                "   G 8-11     r1 free since 7                room 1        r1 free at 11",
                "   H 9-12     r2 free since 8                room 2        r2 free at 12",
                "   I 10-13    r3 free since 9                room 3        r3 free at 13",
                "   J 12-15    r1 free since 11               room 1        r1 free at 15",
                "",
                "rooms used    3        A D G J  |  B E H  |  C F I",
                "every room    pairwise disjoint, and all 10 intervals placed once",
                "depth         3, attained at t = 2",
                "alive at 2    A 0-3, B 1-4, C 2-5   — and these three pairwise overlap",
                "conclusion    no schedule uses fewer than 3; this one uses 3",
            ],
            "after": [
                "The instant `t = 2` is doing all the work. `A`, `B` and `C` each contain it, so "
                "each pair of them overlaps, so a schedule that put any two in one room would be "
                "illegal. That argument mentions no algorithm and therefore constrains every "
                "algorithm, including ones nobody has written.",
                "A third room was opened at `C` and never again, although seven more intervals "
                "arrived. That is the proof's mechanism in miniature: a new room is opened only "
                "when every existing one is busy, and every existing one being busy at `s(x)` "
                "means that many intervals are alive at `s(x)`.",
                "For a faded rehearsal, work out the rooms and the depth for `0-1, 1-4, 2-5, "
                "4-9, 5-8` under both orders before running it. The supplied first move is "
                "this: by start time the walk is `A 0-1`, `B 1-4`, `C 2-5`, `D 4-9`, `E 5-8`, "
                "and `A` and `B` both land in room 1 because `A` finishes exactly when `B` "
                "starts. Say how many rooms each order opens, what the depth is, and which of "
                "the two orders the theorem actually covers.",
            ],
        },
        "quiz_title": "Bounds, certificates, and the order that has no theorem",
        "quiz": [
            {"q": "Why does the depth bound every schedule rather than just the greedy one?",
             "a": ["Because greedy is optimal, so its room count bounds the others",
                   "Because the intervals alive at one instant pairwise overlap, and no two overlapping intervals can share a room in any schedule",
                   "Because the depth is computed before the schedule is built",
                   "Because the intervals are processed in start order"],
             "c": 1,
             "why": "The argument never mentions an algorithm: it is about what a legal "
                    "assignment permits. Any `k` intervals containing a common instant "
                    "pairwise overlap and therefore occupy `k` distinct rooms, whoever built "
                    "the schedule. Computing the depth first is good practice but is not the "
                    "reason it is a bound."},
            {"q": "The panel reports 3 rooms used and depth 3 on all four shipped instances, under both orders offered. What is safe to conclude about the finish-time order?",
             "a": ["It is also optimal, since it matched the depth four times",
                   "It matched the depth on those four instances; no theorem covers it, and `0-1, 1-4, 2-5, 4-9, 5-8` opens three rooms against a depth of two",
                   "It is optimal on instances with at most ten intervals",
                   "It is never worse than the start order, which is why it matched"],
             "c": 1,
             "why": "Four matches are four data points. The proof in the lesson uses the start "
                    "order twice &mdash; once to know the blocking intervals all started "
                    "earlier &mdash; and does not transfer. The five-interval instance above "
                    "opens one room more than the bound, which settles it."},
            {"q": "What does `roomsValid` add that counting the rooms does not?",
             "a": ["It confirms the rooms are numbered consecutively",
                   "It confirms that no room holds two overlapping intervals and that every input interval was placed exactly once",
                   "It recomputes the depth from the room assignment",
                   "It checks that the number of rooms equals the depth"],
             "c": 1,
             "why": "A schedule that dropped an interval, or that doubled one up, would report a "
                    "smaller and better-looking room count. The check is on the assignment "
                    "itself, and it is separate from both the room count and the depth "
                    "comparison, which the panel reports in their own columns."},
            {"q": "On the pile-up instance `0-9, 1-9, 2-9, 3-9, 4-9` the panel reports five rooms and depth five. Which sentence is the bound?",
             "a": ["Greedy used five rooms",
                   "All five intervals are alive at t = 4 and pairwise overlap, so no schedule uses fewer than five",
                   "Five is the number of intervals, so five rooms are needed",
                   "The rooms were checked pairwise disjoint"],
             "c": 1,
             "why": "The measured quantity is the five rooms greedy opened; the bound is the "
                    "certificate at `t = 4`. The count of intervals is not a bound &mdash; the "
                    "disjoint instance also has five intervals and needs one room &mdash; and "
                    "the disjointness check validates the schedule rather than bounding "
                    "anything."},
        ],
        "mistakes": [
            ("Reading the depth off the schedule",
             "If the depth is computed by looking at how many rooms the algorithm opened, the "
             "two numbers agree by construction and prove nothing. They have to come from "
             "routines that share nothing, which is why the panel computes the rooms from the "
             "assignment and the depth from a sweep over the instants, and prints the "
             "certificate for the second."),
            ("Concluding from the presets that the processing order is irrelevant",
             "Both orders give the same room count on all four shipped instances, which is a "
             "measurement on four inputs. The proof uses the start order and the finish order "
             "has none; `0-1, 1-4, 2-5, 4-9, 5-8` opens three rooms against a depth of two. "
             "This is the course's own hazard turning up inside a control the reader is invited "
             "to move."),
            ("Treating this as the same kind of proof as the earlier two",
             "Stays-ahead and exchange both compare greedy against an optimal solution. This "
             "argument never mentions one: it bounds every schedule from below and this "
             "schedule from above, and the two bounds happen to meet. Filing all three under "
             "&ldquo;greedy proofs&rdquo; loses the distinction that makes approximation ratios "
             "readable later."),
        ],
        "standard": ("Finish when you can prove a schedule optimal by producing an instant and a list, without ever computing an optimal schedule.",
                     "You should be able to run the room assignment by hand, compute the depth "
                     "independently, state the certificate as an object rather than a number, "
                     "reproduce the proof that the start-order rule never opens more rooms than "
                     "the depth, and explain why the same proof says nothing about the finish "
                     "order."),
        "note": ("The lower-bound shape on this page is the one the end of this path is built "
                 "from: a quantity no solution can beat, a measured quantity, and a ratio "
                 "between them. Here the ratio is 1 and the page can say &ldquo;optimal&rdquo;. "
                 "&ldquo;Fractional and 0/1 Knapsack&rdquo; is where the same construction "
                 "produces a ratio that is not 1 and is still a guarantee."),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "huffman-codes",
        "title": "Huffman Codes",
        "module": "Huffman codes",
        "one_line": "Merge the two lightest weights repeatedly, read the codewords off the tree, and check that the message comes back.",
        "summary": (
            "Huffman's algorithm is greedy in an unusual direction: it builds the tree from the "
            "leaves upward, and the choice it commits to is which two symbols become siblings. "
            "The expected codeword length is a fraction and the lab prints it as one. The code "
            "is checked prefix-free pairwise rather than trusted to the construction, and a "
            "message is encoded and decoded again, because a code that is short and wrong looks "
            "exactly like a code that is short and right."
        ),
        "key": [
            "merge the two lightest weights; the merged node's weight is their sum",
            "n symbols  →  n − 1 merges  →  a full binary tree, every internal node with 2 children",
            "expected length = total bits / total weight, an exact fraction",
            "a:45 b:13 c:12 d:16 e:9 f:5  →  224 bits over weight 100  →  56/25",
            "against 3 bits for a fixed-length code over six symbols: a saving of 19/25",
            "prefix-free, checked pair by pair; and the message decodes back to itself",
        ],
        "key_label": "The merges, the tree, and the fraction they produce",
        "concepts_intro": (
            "Three ideas: what a prefix code buys, why the expected length is a fraction rather "
            "than a decimal, and why a round trip is worth more than a length."
        ),
        "concepts": [
            ("A prefix code can be decoded without separators",
             "A code is <strong>prefix-free</strong> when no codeword is a prefix of another. "
             "That is what lets a decoder read a bit stream left to right and commit to a "
             "symbol the moment it has seen one: no lookahead, no separators, no ambiguity. "
             "Every full binary tree with the symbols at its leaves gives a prefix code, "
             "because a leaf's path cannot be a prefix of another leaf's path. The panel still "
             "checks it pairwise, because a check that trusts the construction checks nothing."),
            ("The expected length is a ratio of two integers",
             "Multiply each symbol's weight by the length of its codeword, add, and divide by "
             "the total weight. On the opening alphabet that is 224 bits over a total weight of "
             "100, which is `56/25` exactly. The panel prints `56/25` first and `2.240` beside "
             "it as a rounding of the printing at three places. The fraction is the number; the "
             "decimal is a convenience, and on a path where two codes can differ in the third "
             "place that distinction earns its keep."),
            ("A round trip catches what a length cannot",
             "A shorter code is not a better code if it cannot be read back. The panel encodes "
             "a message you type, decodes the resulting bits, and prints whether what came out "
             "is what went in. On the opening alphabet `abcdef` encodes to 18 bits and decodes "
             "back exactly. The check is cheap and it is the only thing on the page that would "
             "notice a code that was short because it was wrong."),
        ],
        "read_title": "Merging upward, and the code that falls out",
        "read_intro": "The algorithm, the tree it builds, the exact expected length, and the three checks that stand between a short code and a correct one.",
        "body": [
            ("def", ("The coding problem",
                     "Given symbols with positive integer weights, assign each a binary "
                     "codeword so that no codeword is a prefix of another, minimising the total "
                     "`Σ wᵢ · |cᵢ|` &mdash; the number of bits needed to write a text in which "
                     "each symbol appears with its weight as a count. Dividing that total by "
                     "`Σ wᵢ` gives the <strong>expected codeword length</strong>.")),
            ("def", ("Huffman's algorithm",
                     "Put every symbol in a collection as a single-node tree with its weight. "
                     "Repeatedly remove the two lightest trees, join them under a new node "
                     "whose weight is their sum, and put that node back. After `n - 1` merges "
                     "one tree remains; label left edges 0 and right edges 1, and each leaf's "
                     "root-to-leaf path is its codeword.")),
            ("p", "The greedy commitment is the merge. Once two trees have been joined, the "
                  "symbols beneath them stay at the same depth relative to each other forever, "
                  "and nothing later reconsiders it. What makes this an unusual greedy "
                  "algorithm is the direction: the choice is made at the leaves, where the "
                  "rarest symbols are, and the consequence &mdash; the codewords &mdash; is "
                  "read off at the end."),
            ("example", ("Six symbols, five merges",
                         "The lab opens on `a:45, b:13, c:12, d:16, e:9, f:5`. The merges are "
                         "`f + e = 14`, then `c + b = 25`, then `14 + d = 30`, then "
                         "`25 + 30 = 55`, then `a + 55 = 100`. The codewords come out "
                         "`a = 0`, `c = 100`, `b = 101`, `f = 1100`, `e = 1101`, `d = 111`, "
                         "with lengths 1, 3, 3, 4, 4 and 3. Total bits `224`, total weight "
                         "`100`, expected length `56/25`.")),
            ("p", "The heaviest symbol got the shortest codeword and the two lightest got the "
                  "longest, which is the whole idea, and it is worth checking against the "
                  "alternative: a fixed-length code over six symbols needs 3 bits each, so it "
                  "spends 300 bits on the same text. The saving is `19/25` of a bit per symbol, "
                  "which the panel prints as a fraction as well."),
            ("h3", "The saving is a fact about the distribution, not about the algorithm"),
            ("p", "Run the same algorithm on four equal weights, `a:10, b:10, c:10, d:10`. Every "
                  "codeword comes out two bits, the expected length is exactly `2`, a "
                  "fixed-length code over four symbols is also 2, and the saving is `0`. "
                  "Huffman did nothing wrong; there was nothing to do. A reader who has only "
                  "ever seen the skewed example carries away &ldquo;Huffman compresses&rdquo; "
                  "as a property of the algorithm, and it is a property of the input."),
            ("p", "The other direction is on the panel too. On `a:60, b:20, c:10, d:5, e:5` the "
                  "common symbol gets one bit and the two rarest get four, and the expected "
                  "length falls to `17/10` against a fixed-length cost of 3. Same algorithm, "
                  "three different distributions, savings of `19/25`, `13/10` and `0`."),
            ("h3", "Where a preset's caption is wrong"),
            ("p", "The Fibonacci-weight instance, `a:1, b:1, c:2, d:3, e:5`, produces the "
                  "deepest tree five leaves can have: depths 4, 4, 3, 2, 1, so the tree is a "
                  "path and the rarest symbols need four bits. Both of those are true and the "
                  "panel prints them. The caption's reason is not: it says each merge is "
                  "exactly the next weight, and the merged weights are `2`, `4`, `7`, `12` "
                  "against symbol weights `1, 1, 2, 3, 5`. Only the first merge matches. After "
                  "`1 + 1 = 2` the collection holds two twos, and the next merge takes both of "
                  "them rather than the two and the three."),
            ("thm", ("Kraft's equality for a Huffman code",
                     "For a code produced by this algorithm on `n` symbols with codeword "
                     "lengths `ℓ₁, …, ℓₙ`, the sum `Σ 2^(−ℓᵢ)` equals exactly 1.")),
            ("p", "A prefix code can only ever satisfy `Σ 2^(−ℓᵢ) ≤ 1` &mdash; each codeword of "
                  "length `ℓ` rules out a `2^(−ℓ)` share of the space of infinite bit strings, "
                  "and the shares are disjoint. Equality means nothing is left over: every bit "
                  "string has a prefix that is a codeword. Huffman achieves equality because "
                  "the tree it builds is full, every internal node having two children, and a "
                  "full tree leaves no unused branch."),
            ("p", "That gives a quick sanity check by hand. On the opening code the lengths are "
                  "1, 3, 3, 4, 4, 3 and the sum is `1/2 + 1/8 + 1/8 + 1/16 + 1/16 + 1/8`, which "
                  "is 1. On the equal-weight code four lengths of 2 give `4 · 1/4 = 1`. A code "
                  "whose lengths sum to less than 1 has a branch going nowhere and can be "
                  "shortened; one that sums to more than 1 is not a prefix code at all."),
            ("h3", "The three checks, and what each one would catch"),
            ("p", "`codesPrefixFree` compares every pair of codewords, so a code that happened "
                  "to be built wrongly would be caught even though the tree construction "
                  "guarantees it. `encodeSyms` and `decodeBits` run the message out and back, "
                  "and the panel prints the decoded text. And the decoder refuses rather than "
                  "guesses: append a proper prefix of the longest codeword to a valid bit "
                  "stream and it returns nothing, because the leftover bits cannot be spent."),
            ("p", "Measured on this page: on the six-symbol alphabet, 224 bits over weight 100, "
                  "expected length `56/25`, saving `19/25`, prefix-free confirmed pairwise, and "
                  "`abcdef` encoded to 18 bits and decoded back unchanged. Proved on this page: "
                  "Kraft's sum is exactly 1 for any code this algorithm produces. What is not "
                  "on this page is the claim that no code is shorter, and that is the next "
                  "thing to establish rather than something the fraction above implies."),
        ],
        "lab": ("greedy", {
            "mode": "huffman",
            "preset": "clrs",
            "panel_title": "Choose the alphabet, and step through the merges",
            "panel_intro": "The merge slider replays the construction one join at a time and "
                           "highlights the two trees being joined. The expected length is "
                           "printed as a fraction first; the decimal beside it is a rounding of "
                           "the printing at three places, not a second number.",
        }),
        "steps_title": "Building and checking a code by hand",
        "steps_intro": "Five steps. The last two are the ones a reader in a hurry skips, and they are the ones that catch mistakes.",
        "steps": [
            ("Sort, then merge the two lightest, then re-insert",
             "Write the weights in a row. Take the two smallest, write their sum above them "
             "joined by a fork, and put the sum back into the row. Repeat until one weight "
             "remains. Ties may be broken any way; different tie-breaks give different trees "
             "and the same total cost."),
            ("Read the codewords off the paths, not off the order of merging",
             "Label every left edge 0 and every right edge 1 and walk from the root to each "
             "leaf. The length of a codeword is the depth of its leaf, which is the number of "
             "merges that symbol was carried through."),
            ("Compute the total as a sum of products, then divide",
             "`Σ wᵢ · ℓᵢ` first, as an integer; then divide by `Σ wᵢ`. Doing it the other way "
             "round, averaging decimals, loses the exactness that lets two codes be compared."),
            ("Check Kraft's sum is exactly 1",
             "Add `2^(−ℓᵢ)` over the symbols. Anything less than 1 means a wasted branch and a "
             "code you can shorten; anything more means the lengths do not describe a prefix "
             "code at all. This is a two-line check that catches an arithmetic slip in the "
             "depths."),
            ("Encode something and decode it back",
             "A length is a number and a round trip is a demonstration. Type a message into the "
             "panel and read the decoded line: it is the only check on the page that would "
             "notice a short code that cannot be read."),
        ],
        "worked": {
            "title": "The six-symbol alphabet, merged by hand",
            "intro": [
                "Weights `a:45, b:13, c:12, d:16, e:9, f:5`. At each step take the two smallest "
                "remaining weights, whether they are symbols or earlier merges.",
            ],
            "lines": [
                "   step   collection                     two lightest   merged",
                "    1     45 13 12 16  9  5              5 and 9        14      4 left",
                "    2     45 13 12 16 14                 12 and 13      25      3 left",
                "    3     45 16 25 14                    14 and 16      30      2 left",
                "    4     45 25 30                       25 and 30      55      1 left",
                "    5     45 55                          45 and 55     100      done",
                "",
                "   symbol   weight   codeword   bits   weight x bits",
                "     a        45        0        1          45",
                "     c        12       100       3          36",
                "     b        13       101       3          39",
                "     f         5      1100       4          20",
                "     e         9      1101       4          36",
                "     d        16       111       3          48",
                "   total     100                          224",
                "",
                "expected length   224 / 100  =  56/25  =  2.240 to three places",
                "fixed length      3 bits per symbol over six symbols  =  300 bits",
                "saving            3 - 56/25  =  19/25 bits per symbol",
                "Kraft             1/2 + 1/8 + 1/8 + 1/16 + 1/16 + 1/8  =  1",
            ],
            "after": [
                "Five merges for six symbols, and the count is not a coincidence: each merge "
                "reduces the collection by one and the process ends at one tree, so `n` symbols "
                "always take `n - 1` merges and produce a tree with `n - 1` internal nodes.",
                "Step 3 is the one worth watching. The lightest two are `14`, a merged node, and "
                "`16`, a symbol. Merged nodes compete with symbols on equal terms from the "
                "moment they are created, which is why the tree is not simply a sorted "
                "caterpillar and why the algorithm cannot be replaced by sorting the symbols "
                "once.",
                "For a faded rehearsal, do `a:1, b:1, c:2, d:3, e:5` by hand before running it. "
                "The supplied first move is `1 + 1 = 2`, leaving `2, 2, 3, 5`. Say what the "
                "remaining three merges are, what depth each symbol ends at, and what the "
                "expected length is as a fraction &mdash; and then say whether the merged "
                "weights reproduce the input sequence, which is what that instance's caption "
                "claims.",
            ],
        },
        "quiz_title": "Merges, fractions, and what the checks catch",
        "quiz": [
            {"q": "The panel reports an expected length of `56/25` and, beside it, `2.240`. Which is the number?",
             "a": ["`2.240`, since the fraction is only a display convenience",
                   "`56/25`; the decimal is a rounding of the printing at three stated places",
                   "Both, since they are equal",
                   "Neither, since the expected length depends on the message typed"],
             "c": 1,
             "why": "`56/25` is exactly `2.24`, so nothing is lost here &mdash; but the panel's "
                    "rule is that the fraction is the value and the decimal is a rounding at a "
                    "stated number of places, and on an alphabet whose expected length is "
                    "`25/12` the decimal `2.083` is not the number. The expected length depends "
                    "on the weights, not on the message."},
            {"q": "On four equal weights the expected length is exactly 2 and the saving over a fixed-length code is 0. What does that show?",
             "a": ["That Huffman failed on this input",
                   "That the algorithm needs at least one weight to dominate",
                   "That the saving is a property of the distribution, not of the algorithm",
                   "That equal weights are not a valid input"],
             "c": 2,
             "why": "Huffman produced an optimal code; there simply is no shorter one, because "
                    "with equal weights every arrangement of four leaves at depth 2 costs the "
                    "same. Compression comes from skew in the weights, and an algorithm cannot "
                    "manufacture skew that is not there."},
            {"q": "Why does the panel check the code prefix-free pairwise when the tree construction already guarantees it?",
             "a": ["Because ties in the merge order can break the guarantee",
                   "Because a check that assumes the construction is correct checks nothing about the construction",
                   "Because the codewords are assigned after the tree is built",
                   "Because Kraft's inequality can fail with equality"],
             "c": 1,
             "why": "The guarantee is a fact about the algorithm as designed; the check is about "
                    "the codewords actually on the page. If the two ever disagreed, only the "
                    "independent check would say so. Ties change which tree is built and never "
                    "make a leaf's path a prefix of another leaf's path."},
            {"q": "A bit stream that decodes correctly is given one extra bit, a proper prefix of the longest codeword. What does the decoder do?",
             "a": ["Ignores the leftover bits and returns the message",
                   "Returns the message with an extra symbol guessed from the partial codeword",
                   "Refuses and returns nothing, because the leftover bits are not a codeword",
                   "Pads the leftover bits with zeros until they match a codeword"],
             "c": 2,
             "why": "A proper prefix of a codeword is never itself a codeword in a prefix-free "
                    "code, so the decoder ends holding bits it cannot spend and refuses. "
                    "Guessing or ignoring would let a corrupted stream come back looking "
                    "correct, which is the failure the round trip exists to catch."},
        ],
        "mistakes": [
            ("Averaging the codeword lengths instead of weighting them",
             "The expected length is `Σ wᵢ ℓᵢ / Σ wᵢ`, not the mean of the lengths. On the "
             "opening alphabet the mean length is `18/6 = 3` and the expected length is "
             "`56/25`, which is 2.24 &mdash; a difference of three quarters of a bit per symbol, "
             "and the entire point of the algorithm."),
            ("Believing Huffman always compresses",
             "On four equal weights the saving is exactly zero and the panel says so. The "
             "algorithm is optimal on every input and useful only on skewed ones, and those are "
             "different statements. Quoting a compression figure without quoting the "
             "distribution it came from is quoting a measurement as though it were a bound."),
            ("Taking the Fibonacci caption's reason at face value",
             "That instance really does produce the deepest tree five leaves allow, and the "
             "rarest symbols really do need four bits. But the merged weights are `2, 4, 7, 12` "
             "and the caption says each merge is the next input weight, which stops being true "
             "at the second merge. Read the merge table: it is the run, and the caption is not."),
        ],
        "standard": ("Finish when you can build the tree, produce the exact expected length as a fraction, and check the result three ways without looking anything up.",
                     "You should be able to merge by hand and get the same tree shape the panel "
                     "draws, compute `Σ wᵢ ℓᵢ` and divide, verify Kraft's sum is 1, explain "
                     "what the round trip catches that a length does not, and say why a saving "
                     "of zero on equal weights is not a failure."),
        "note": ("Everything on this page is about the code the algorithm produced. None of it "
                 "says that no other code is shorter, and the fraction `56/25` is perfectly "
                 "consistent with some cleverer tree reaching `55/25`. Establishing that no "
                 "such tree exists is a separate argument with two lemmas behind it, and "
                 "&ldquo;Why Huffman Is Optimal&rdquo; both proves it and checks it against "
                 "every tree."),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "why-huffman-is-optimal",
        "title": "Why Huffman Is Optimal",
        "module": "Huffman codes",
        "one_line": "Prove that no prefix code is shorter, by two exchange lemmas, and check the proof against every full binary tree and every assignment of the weights to its leaves.",
        "summary": (
            "That Huffman's code is short is a measurement. That no code is shorter is a "
            "theorem, and it rests on two lemmas: an optimal tree can always be rearranged so "
            "that the two lightest symbols are deepest siblings, and merging those two reduces "
            "the problem to one symbol fewer. The lab checks the conclusion the only way a lab "
            "can &mdash; by building every full binary tree on `n` leaves and trying every way "
            "of putting the weights on them."
        ),
        "key": [
            "lemma 1: some optimal tree has the two lightest symbols as deepest siblings",
            "lemma 2: merging them leaves an optimal code for n − 1 symbols, and back again",
            "4 leaves: 5 shapes, 120 (shape, assignment) pairs, best 80 bits — Huffman's 80",
            "5 leaves: 14 shapes, 1680 pairs        6 leaves: 42 shapes, 30240 pairs",
            "shapes on n leaves = the Catalan numbers 1, 1, 2, 5, 14, 42",
            "seven leaves is refused: the page says so rather than printing a number",
        ],
        "key_label": "Two lemmas, and the enumeration that agrees with them",
        "concepts_intro": (
            "Three ideas: why optimality needs an exchange argument rather than a calculation, "
            "how an induction on the number of symbols closes it, and what an enumeration over "
            "every tree can and cannot add."
        ),
        "concepts": [
            ("Optimality is a claim about codes nobody built",
             "The expected length of Huffman's code is arithmetic. The claim that no prefix "
             "code on the same weights is shorter ranges over every full binary tree and every "
             "way of placing the symbols on its leaves &mdash; on six symbols that is 42 shapes "
             "and 30,240 placements. No amount of looking at the code Huffman produced settles "
             "it, which is why the argument has to be about an arbitrary optimal tree rather "
             "than about this one."),
            ("Rearranging an optimal tree is free when the swap is downhill",
             "If a heavier symbol sits deeper than a lighter one, swapping them cannot increase "
             "the cost: the change is `(w_heavy − w_light)(depth_shallow − depth_deep)`, a "
             "product of a non-negative and a non-positive number. That one inequality is the "
             "engine of the first lemma, and it is the same move as the exchange argument on "
             "intervals, applied to positions in a tree instead of to positions in a schedule."),
            ("An enumeration checks the conclusion, not the proof",
             "The panel builds every full binary tree on `n` leaves and tries every assignment "
             "of the weights, and reports the minimum. When that minimum equals Huffman's cost, "
             "the claim &ldquo;no code is shorter&rdquo; has been verified for this alphabet by "
             "a search that knows nothing about merging. It is still one alphabet. The lemmas "
             "are what cover the alphabets nobody typed."),
        ],
        "read_title": "Two lemmas, an induction, and a search that agrees",
        "read_intro": "The exchange lemma, the reduction lemma, the induction they close, and what the enumeration over every tree adds and does not add.",
        "body": [
            ("def", ("Cost of a tree",
                     "For a full binary tree `T` whose leaves carry the symbols, write "
                     "`B(T) = Σ wᵢ · dᵢ`, where `dᵢ` is the depth of symbol `i`. A prefix code "
                     "corresponds to such a tree and its total bit count is `B(T)`, so "
                     "minimising the code is minimising `B` over trees and over assignments of "
                     "the symbols to leaves.")),
            ("thm", ("Lemma 1: the two lightest can be made deepest siblings",
                     "Let `x` and `y` be two symbols of smallest weight. Some optimal tree has "
                     "`x` and `y` as sibling leaves at maximum depth.")),
            ("proof", ("Take any optimal tree `T` and let `a` and `b` be two sibling leaves at "
                       "maximum depth &mdash; they exist because the tree is full, so the "
                       "deepest leaf has a sibling, and that sibling is also a leaf at the same "
                       "depth.",
                       "Swap `a` with `x`. Writing `d` for depths, the cost changes by "
                       "`(w_a − w_x)(d_x − d_a)`. Since `x` is of smallest weight, "
                       "`w_a − w_x ≥ 0`; since `a` is at maximum depth, `d_x − d_a ≤ 0`. The "
                       "product is at most 0, so the cost did not increase, and `T` was optimal, "
                       "so it did not decrease either.",
                       "Swap `b` with `y` in the same way. The result is an optimal tree in "
                       "which `x` and `y` are sibling leaves at maximum depth.")),
            ("thm", ("Lemma 2: merging reduces the problem",
                     "Let `x` and `y` be two symbols of smallest weight and let `z` be a new "
                     "symbol of weight `w_x + w_y` replacing them. If `T'` is an optimal tree "
                     "for the reduced alphabet, then the tree `T` obtained by replacing the leaf "
                     "`z` with an internal node whose children are `x` and `y` is optimal for "
                     "the original alphabet.")),
            ("proof", ("First, the costs are related by a constant. In `T`, `x` and `y` sit one "
                       "level below where `z` sat, so "
                       "`B(T) = B(T') − w_z d_z + (w_x + w_y)(d_z + 1) = B(T') + w_x + w_y`, "
                       "using `w_z = w_x + w_y`. The same identity holds for any tree of the "
                       "reduced alphabet and its expansion.",
                       "Suppose some tree `U` for the original alphabet had `B(U) &lt; B(T)`. By "
                       "the first lemma we may assume `x` and `y` are sibling leaves in `U`. "
                       "Contract that pair into a single leaf `z` to get a tree `U'` for the "
                       "reduced alphabet, with `B(U') = B(U) − w_x − w_y`.",
                       "Then `B(U') = B(U) − w_x − w_y &lt; B(T) − w_x − w_y = B(T')`, "
                       "contradicting the optimality of `T'`. So no such `U` exists and `T` is "
                       "optimal.")),
            ("p", "The induction is now immediate. On two symbols the only full binary tree "
                  "gives both a one-bit codeword and is optimal. For `n` symbols, Huffman's "
                  "first merge takes the two lightest, the rest of its run is Huffman on the "
                  "reduced alphabet, which by induction is optimal there, and the second lemma "
                  "lifts that optimality back. So Huffman's code is optimal for every alphabet."),
            ("h3", "What the enumeration adds"),
            ("p", "The panel does something the proof does not: it builds every full binary tree "
                  "on `n` leaves and, for each, tries every assignment of the weights to its "
                  "leaves, then reports the smallest total. The number of shapes on `n` leaves "
                  "is the Catalan number `C(n−1)`, so four leaves give 5 shapes, five leaves 14, "
                  "and six leaves 42; with `n!` assignments each, that is 120, 1680 and 30,240 "
                  "(shape, assignment) pairs respectively."),
            ("p", "The lab opens on four equal weights, `a:10, b:10, c:10, d:10`. All 5 shapes "
                  "and all 120 pairs are tried, the best is 80 bits, and Huffman's code costs "
                  "80. On the six-symbol alphabet the best of the 30,240 pairs is 224 bits, "
                  "which is again what Huffman produced. On the skewed and Fibonacci alphabets, "
                  "170 and 25 bits respectively, matched both times."),
            ("p", "Trying every assignment as well as every shape is deliberate, and it is where "
                  "the check earns its place. A search that placed the heaviest weight on the "
                  "shallowest leaf of each shape would be assuming the rearrangement inequality "
                  "&mdash; the same inequality the first lemma is built on &mdash; and would "
                  "therefore be checking the proof against itself. Enumerating the assignments "
                  "assumes nothing, so the two can disagree, and on four alphabets they do not."),
            ("h3", "Where the search stops, and why the page says so"),
            ("p", "Seven leaves is 132 shapes and 5,040 assignments each, and the panel refuses "
                  "rather than running it. When it refuses it prints why, and the expected "
                  "length above stays exact: what is missing is the confirmation that nothing "
                  "beats it. A page that silently dropped the check would look identical to a "
                  "page that had run it, which is the failure mode this whole path is built "
                  "against."),
            ("p", "So the honest reading of this page has three layers rather than two. "
                  "Measured: on the four shipped alphabets, the minimum over every shape and "
                  "every assignment equals Huffman's cost &mdash; 80, 224, 170 and 25 bits. "
                  "Proved: Huffman is optimal for every alphabet, by the two lemmas and the "
                  "induction. Refused: on seven or more symbols the search does not run, and "
                  "the page says which of the two sentences it can still stand behind."),
        ],
        "lab": ("greedy", {
            "mode": "huffman",
            "preset": "uniform",
            "panel_title": "The alphabet where Huffman saves nothing, and is still optimal",
            "panel_intro": "The last figure is the minimum over every full binary tree on this "
                           "many leaves and every assignment of the weights to their leaves, "
                           "computed by a search that has never heard of merging. Change the "
                           "alphabet and watch the number of shapes it has to try grow.",
        }),
        "steps_title": "Proving a construction optimal",
        "steps_intro": "Four steps, and the first one is the one that decides whether the rest is a proof or a demonstration.",
        "steps": [
            ("Start from an arbitrary optimal object, never from yours",
             "The proof takes an optimal tree `T` that nobody built and shows it can be "
             "rearranged. Starting from Huffman's own tree and observing that it looks "
             "reasonable is the error this whole course is about, and it is easy to make when "
             "the tree is in front of you on the screen."),
            ("Make the rearrangement cost nothing, by signs",
             "The swap in the first lemma is justified by a product of two factors whose signs "
             "are known: a weight difference that is non-negative and a depth difference that "
             "is non-positive. No arithmetic on the actual numbers is needed, which is what "
             "makes the lemma hold for every alphabet."),
            ("Reduce the problem, do not solve it",
             "The second lemma turns `n` symbols into `n - 1` and relates the two costs by a "
             "constant, `w_x + w_y`. A reduction that changed the cost by something depending "
             "on the tree would not support an induction, and checking that the constant really "
             "is constant is the step worth writing out."),
            ("Check the conclusion against a search, and record what it could not reach",
             "Run the enumeration on the alphabets it will take, and write down that it "
             "matched. Then write down the size at which it refused. An optimality claim "
             "supported only by alphabets small enough to enumerate is a claim about those "
             "alphabets."),
        ],
        "worked": {
            "title": "Four equal weights: every tree, by hand",
            "intro": [
                "Weights `a:10, b:10, c:10, d:10`. With four leaves there are only five full "
                "binary tree shapes, and with equal weights the assignment of symbols to leaves "
                "cannot change a shape's cost, so the five shapes can be costed directly.",
            ],
            "lines": [
                "   shape (leaf depths)        cost = sum of 10 x depth",
                "   2 2 2 2   balanced         10(2+2+2+2)  =  80",
                "   1 2 3 3                    10(1+2+3+3)  =  90",
                "   1 3 3 2   mirror of above  10(1+3+3+2)  =  90",
                "   3 3 2 1                    10(3+3+2+1)  =  90",
                "   2 3 3 1                    10(2+3+3+1)  =  90",
                "",
                "best over all 5 shapes and all 120 (shape, assignment) pairs   80 bits",
                "Huffman's own run   merges 10+10 = 20, 10+10 = 20, 20+20 = 40",
                "Huffman's cost      four codewords of 2 bits, 10 x 2 x 4  =  80 bits",
                "expected length     80 / 40  =  2  exactly",
                "fixed-length code   2 bits per symbol over four symbols",
                "saving              0",
                "Kraft               4 x 1/4  =  1",
            ],
            "after": [
                "Only the balanced shape reaches 80, and Huffman finds it. The other four shapes "
                "each put one symbol at depth 1 and two at depth 3, which is exactly the trade "
                "that pays off when the weights are skewed and costs 10 bits when they are not.",
                "This is also the cleanest place to see what the optimality theorem does and "
                "does not promise. It promises that no tree beats 80, and that is true. It does "
                "not promise a saving: the fixed-length code also costs 80, and the panel "
                "reports a saving of 0 rather than hiding it.",
                "For a faded rehearsal, predict how many shapes the six-symbol alphabet has "
                "before opening it. The supplied first move is the recurrence: a full binary "
                "tree on `n` leaves splits into a left subtree on `k` leaves and a right one on "
                "`n − k`, so the counts satisfy the Catalan recurrence and run 1, 1, 2, 5, 14. "
                "Say what the sixth term is, multiply by `6!` for the assignments, and check "
                "both against the panel.",
            ],
        },
        "quiz_title": "Lemmas, inductions, and what a search settles",
        "quiz": [
            {"q": "Why does the first lemma start from an arbitrary optimal tree rather than from Huffman's tree?",
             "a": ["Because Huffman's tree may not be full",
                   "Because the claim is that no tree beats Huffman's, which cannot be established by examining Huffman's",
                   "Because Huffman's tree depends on how ties are broken",
                   "Because the cost of Huffman's tree is not known until the end"],
             "c": 1,
             "why": "The theorem quantifies over every tree. Starting from Huffman's own tree "
                    "and observing that it looks sensible is the exact error this course is "
                    "built around. Ties do change which tree is produced, and all such trees "
                    "cost the same, but that is a separate point."},
            {"q": "In the first lemma's swap, why is the cost change `(w_a − w_x)(d_x − d_a)` guaranteed not to be positive?",
             "a": ["Because both factors are non-negative",
                   "Because `x` has smallest weight so the first factor is at least 0, and `a` is at maximum depth so the second is at most 0",
                   "Because the tree is full",
                   "Because the swap preserves the number of leaves"],
             "c": 1,
             "why": "The signs come from the two choices: `x` is a lightest symbol and `a` sits "
                    "at maximum depth. A non-negative times a non-positive is non-positive, so "
                    "the cost cannot rise, and optimality of the original tree stops it falling. "
                    "Fullness is used to know that a deepest leaf has a leaf sibling."},
            {"q": "The panel tries every assignment of the weights to each shape's leaves rather than placing the heaviest on the shallowest leaf. Why does that matter?",
             "a": ["Because the heaviest-on-shallowest placement is sometimes infeasible",
                   "Because that placement is an instance of the rearrangement inequality the proof itself uses, so assuming it would check the proof against itself",
                   "Because it makes the search faster",
                   "Because ties between equal weights would otherwise be broken arbitrarily"],
             "c": 1,
             "why": "Placing heavy symbols shallow is exactly the move the first lemma "
                    "justifies. A check that assumed it would share a premise with the thing "
                    "being checked. Enumerating all `n!` assignments shares nothing, which is "
                    "why the panel reports both the shape count and the assignment count."},
            {"q": "On seven symbols the panel refuses to run the enumeration and says so. What is still true on the page?",
             "a": ["Nothing; without the search the expected length is unverified",
                   "The expected length is still exact; what is missing is the confirmation that no tree beats it",
                   "The code is no longer guaranteed prefix-free",
                   "The Kraft sum may no longer be 1"],
             "c": 1,
             "why": "The merges, the codewords, the totals and the round trip are all computed "
                    "as usual. Only the optimality check is absent, and the panel says which. A "
                    "page that dropped the check silently would be indistinguishable from one "
                    "that had run it, which is the failure this refusal exists to prevent."},
        ],
        "mistakes": [
            ("Confusing the shortest code found with the claim that no shorter one exists",
             "The first is arithmetic on the tree in front of you and the second ranges over "
             "every tree and every assignment of the weights. On six symbols that is 42 shapes "
             "and 30,240 placements, and on seven the panel will not even try. The gap between "
             "those two sentences is what the two lemmas close."),
            ("Reading the enumeration as the proof",
             "The search agrees with Huffman on all four shipped alphabets, which is four "
             "alphabets. It is a real check &mdash; a disagreement would be conclusive &mdash; "
             "but the statement that licenses using Huffman on an alphabet nobody typed is the "
             "induction, and the induction is not a bigger version of the search."),
            ("Expecting the enumeration to grow gently",
             "Shapes follow the Catalan numbers and assignments follow `n!`, so the product goes "
             "120, 1680, 30,240 for four, five and six symbols. A reader who saw the four-symbol "
             "case run instantly and assumed nine symbols would merely take a while has "
             "mis-estimated by several orders of magnitude, and the panel's refusal at seven is "
             "where that assumption meets the arithmetic."),
        ],
        "standard": ("Finish when you can state both lemmas, run the induction, and say exactly what the tree enumeration adds to them.",
                     "You should be able to justify the exchange swap by the signs of its two "
                     "factors, derive the constant `w_x + w_y` relating a tree to its "
                     "contraction, explain why the induction needs both lemmas rather than "
                     "either alone, and say what remains unestablished when the panel refuses "
                     "to enumerate."),
        "note": ("Huffman, the earliest-finish rule and the room-assignment rule are three "
                 "greedy algorithms that are optimal, each proved by its own argument. That "
                 "raises a question none of the three answers: is there a property of a problem "
                 "that decides whether some greedy rule works on it? There is, it is exactly a "
                 "condition on the family of feasible sets, and &ldquo;Independence Systems and "
                 "Matroids&rdquo; is where it is defined and tested."),
    },
]
