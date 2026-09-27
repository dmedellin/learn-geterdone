"""Graph Algorithms, lessons 08-13 - shortest paths, and flow and matching."""

LESSONS = [
    # ---------------------------------------------------------------- 08
    {
        "slug": "relaxation-and-dijkstras-schedule",
        "title": "Relaxation and Dijkstra's Schedule",
        "module": "Shortest paths",
        "one_line": "Apply one line of arithmetic in three different orders, reach the same distances, and count what each order costs.",
        "summary": (
            "Every shortest-path algorithm on this course is the same step applied on a "
            "different schedule: if going to `u` and then along an edge beats the best known "
            "route to `v`, write the better number down. The step never makes a label too small, "
            "so a schedule can only be judged on whether it finishes and on what it costs. Three "
            "schedules are run side by side on the graph you type, and all three agree with an "
            "independent answer."
        ),
        "key": [
            "relax(u, v):   if d[u] + w < d[v] then d[v] = d[u] + w, parent[v] = u",
            "invariant      d[v] is never below the true distance, at any moment",
            "nearest first  the heap schedule: settle the closest unfinished vertex",
            "linear scan    the same choice, found by reading every label",
            "arc order      relax every edge over and over until nothing changes",
            "same answer, different work, on a graph with no negative weight",
        ],
        "key_label": "One step, three schedules, and the invariant that holds throughout",
        "concepts_intro": (
            "The hard idea is that the schedule is a separate question from the step. The "
            "invariant is what makes that separation legitimate."
        ),
        "concepts": [
            ("The step is an upper bound being improved",
             "Every label `d[v]` starts at infinity and only ever falls, and it always records "
             "the length of some actual route from the source &mdash; which is why it can never "
             "drop below the true distance. The lab checks that invariant after every single "
             "step, against distances computed by a different algorithm entirely, and reports "
             "both that it held and that every label ended exact."),
            ("A schedule decides the work, not the answer",
             "On the lab's opening graph the three schedules all reach the distances `0, 7, 9, "
             "20, 20, 11` from vertex 1. What differs is the cost: taking the nearest unfinished "
             "vertex from a heap does 18 relaxations with 8 pushes and 8 pops; finding the same "
             "vertex by scanning every label does 18 relaxations and 42 label reads; relaxing "
             "the edges in the order they were typed, round after round, does 36. Same six "
             "numbers, twice the work at one end."),
            ("Settling early is what nearest-first buys, and what it risks",
             "The heap schedule declares a vertex finished the moment it is the closest "
             "unfinished one, and never looks at it again. That is sound only because no edge "
             "can reduce a distance &mdash; with every weight at least 0, nothing reached later "
             "can offer a cheaper route back. Where that fails, the schedule fails, and on this "
             "undirected graph it fails for a reason worth being precise about: an edge of "
             "negative weight that can be walked in both directions IS a negative cycle."),
        ],
        "read_title": "One step, and the three orders it can be applied in",
        "read_intro": "The relaxation step, the invariant it maintains, the three schedules with their counts, and what the reference column is not.",
        "body": [
            ("def", ("Relaxation",
                     "Given labels `d` and an edge from `u` to `v` of weight `w`, to "
                     "<strong>relax</strong> that edge is to test whether `d[u] + w` is less than "
                     "`d[v]`, and if so to set `d[v] = d[u] + w` and record `u` as `v`'s "
                     "predecessor. The label `d[v]` is initialised to infinity for every vertex "
                     "but the source, whose label is 0.")),
            ("thm", ("The upper-bound invariant",
                     "At every moment during any sequence of relaxations, `d[v]` is either "
                     "infinite or the length of some path from the source to `v`. In particular "
                     "`d[v]` is never less than the true shortest distance to `v`.")),
            ("proof", ("By induction on the number of relaxations performed. Before any, only "
                       "the source has a finite label and 0 is the length of the empty path.",
                       "Suppose the claim holds and the edge from `u` to `v` is relaxed, setting "
                       "`d[v] = d[u] + w`. By hypothesis `d[u]` is the length of some path from "
                       "the source to `u`; appending the edge gives a path to `v` of length "
                       "exactly `d[u] + w`. So the new label is again the length of a path, and "
                       "no path is shorter than the shortest one.")),
            ("p", "That theorem is why a schedule cannot be wrong in the direction of "
                  "underestimating, and it is what makes the three schedules comparable. Each is "
                  "a rule for which edge to relax next; none of them can produce a number below "
                  "the truth; the only questions left are whether the labels ever reach the "
                  "truth, and how much work that takes."),
            ("h3", "Three schedules"),
            ("ul", ["<strong>Nearest unfinished first.</strong> Keep the unfinished vertices in "
                    "a heap keyed by their current labels. Pop the smallest, declare it "
                    "finished, and relax every edge out of it. This is Dijkstra's schedule.",
                    "<strong>Linear scan.</strong> The same choice made by reading every "
                    "vertex's label and taking the smallest unfinished one. No heap, `V` reads "
                    "per step.",
                    "<strong>Arc order.</strong> Ignore distance entirely: sweep the whole edge "
                    "list relaxing everything, and repeat until a full sweep changes nothing."]),
            ("example", ("Six vertices, one source, three schedules",
                         "The lab opens on `1-2 7, 1-3 9, 1-6 14, 2-3 10, 2-4 15, 3-4 11, "
                         "3-6 2, 4-5 6, 5-6 9` from vertex 1. All three schedules reach `0, 7, "
                         "9, 20, 20, 11`, and so does an independently written Dijkstra from "
                         "another Subject that knows nothing about this representation. The route "
                         "to vertex 5 is 1, 3, 6, 5, at `9 + 2 + 9 = 20`. The counts: heap 18 "
                         "relaxations, 8 pushes, 8 pops, 15 key comparisons; scan 18 relaxations "
                         "and 42 label reads; arc order 36 relaxations.")),
            ("p", "Two numbers in there are worth dwelling on. The heap and the scan perform the "
                  "same 18 relaxations, because they make the same choices &mdash; they differ "
                  "only in how the choice is found, which is 15 heap comparisons against 42 "
                  "label reads. And the arc-order schedule does exactly twice as many "
                  "relaxations, because it needs a second sweep to confirm that the first one "
                  "settled everything."),
            ("p", "The lab's other presets move those numbers in opposite directions. On a chain "
                  "of six edges the scan does 56 label reads where the heap does 7 pushes, 7 "
                  "pops and no key comparisons at all; on ten edges over five vertices the scan "
                  "does 30 reads against the heap's 14 comparisons, 7 pushes and 7 pops. The "
                  "heap's advantage is largest where the frontier is small, which is the sparse "
                  "case, and that is the shape of the usual advice."),
            ("h3", "The reference column, and what it is for"),
            ("p", "The panel prints `E` times the integer part of `log₂ V`, labelled for "
                  "reference: 18 on the opening graph, since it has nine edges and six vertices. "
                  "The measured relaxation count is also 18 and that is a coincidence of this "
                  "graph; on the chain the reference is 12 and the heap does 12 relaxations with "
                  "quite different heap traffic. No verdict is read off the column, and none "
                  "should be: it is a scale to watch the counts against as the graph changes."),
            ("h3", "The one weight this mode will not take"),
            ("p", "The edges here are undirected, and that is deliberate, because it is what "
                  "lets the answers be checked live against an undirected implementation written "
                  "for another Subject. It has a consequence the panel states outright: on an "
                  "undirected graph a negative weight is a negative cycle. Walk such an edge and "
                  "walk back, and the total has fallen by twice the weight; do it again and it "
                  "falls further. No shortest path exists to anything on that side of the graph."),
            ("p", "The lab will let you type one so that you can see what happens, and what "
                  "happens is not an error message. On `1-2 -3, 2-3 4` the heap schedule returns "
                  "labels of `-6`, `-3` and `1` &mdash; including a label of `-6` for the source "
                  "itself, whose distance to itself is 0. The rounds method on the same graph "
                  "returns the cycle 1, 2, 1 as a certificate. Negative weights belong to "
                  "directed arcs, and they are the subject of &ldquo;Negative Weights and "
                  "Bellman&ndash;Ford&rdquo;."),
            ("p", "Measured beside proved, one last time. The three schedules agreeing on six "
                  "numbers, on four presets, is evidence that the step is indifferent to order. "
                  "The theorem is that on any graph with no negative weight, the nearest-first "
                  "schedule settles every vertex exactly once with its true distance, and the "
                  "proof is a separate argument about the smallest unfinished label &mdash; not "
                  "something the agreement could establish, because agreement on four graphs is "
                  "agreement on four graphs."),
        ],
        "lab": ("graphkit", {
            "mode": "relax",
            "preset": "classic",
            "panel_title": "Type the graph, then change only the schedule",
            "panel_intro": "The relaxation step is one line of arithmetic. Each schedule applies "
                           "it in a different order, and after every step the labels are checked "
                           "against distances computed by a different algorithm entirely, so the "
                           "invariant is verified rather than asserted. The edges are "
                           "undirected, which is what makes that live check possible.",
        }),
        "steps_title": "Choosing a schedule, and checking it",
        "steps_intro": "The step is fixed. Everything you decide is about order.",
        "steps": [
            ("Write the step once and never vary it",
             "Every algorithm in this module performs exactly `d[v] = min(d[v], d[u] + w)` and "
             "records a predecessor. Bugs at this level are rare; bugs in the schedule are "
             "common, and keeping the step separate in your head is what makes the difference "
             "visible."),
            ("Check the invariant, not the answer",
             "After any prefix of the relaxations, every finite label should be the length of a "
             "real path. That is checkable at every step, whereas the final answer is checkable "
             "only at the end. The lab reports both, and it is the per-step check that localises "
             "a mistake."),
            ("Pick the schedule from the shape of the graph",
             "A small frontier favours the heap; a dense graph where almost every vertex is a "
             "candidate at once narrows the gap, because the scan's `V` reads are then cheap "
             "relative to the heap traffic. The lab prints both counters on whatever you type, "
             "which is a better guide than a rule of thumb."),
            ("Before quoting a bound, ask whether a weight can be negative",
             "Nearest-first is correct because no later edge can reduce a settled label, and "
             "that argument uses non-negativity and nothing else. On these undirected edges a "
             "negative weight is not merely awkward, it is a negative cycle, and the question "
             "stops having an answer rather than becoming harder."),
        ],
        "worked": {
            "title": "The same six distances, reached three ways",
            "intro": [
                "The graph is `1-2 7, 1-3 9, 1-6 14, 2-3 10, 2-4 15, 3-4 11, 3-6 2, 4-5 6, "
                "5-6 9`, undirected, and the source is vertex 1.",
            ],
            "lines": [
                "nearest unfinished first",
                "  settle 1  at 0     relax 1-2, 1-3, 1-6      d = 0  7  9  -  - 14",
                "  settle 2  at 7     relax 2-3, 2-4           d = 0  7  9 22  - 14",
                "  settle 3  at 9     relax 3-4, 3-6           d = 0  7  9 20  - 11",
                "  settle 6  at 11    relax 5-6                d = 0  7  9 20 20 11",
                "  settle 5  at 20    relax 4-5                nothing improves",
                "  settle 4  at 20                             done",
                "",
                "final     d[1]=0  d[2]=7  d[3]=9  d[4]=20  d[5]=20  d[6]=11",
                "route to 5      1 - 3 - 6 - 5        9 + 2 + 9 = 20",
                "",
                "cost of each schedule, same six numbers",
                "  heap        18 relaxations   8 pushes  8 pops  15 key comparisons",
                "  scan        18 relaxations   42 label reads",
                "  arc order   36 relaxations",
                "  E times the integer part of log2 V, for reference        18",
                "",
                "an independently written Dijkstra, same graph:  0 7 9 20 20 11",
            ],
            "after": [
                "Watch vertex 4. Its label was 22 after vertex 2 was settled and fell to 20 when "
                "vertex 3 was settled &mdash; an improvement to an unsettled vertex, which is "
                "ordinary. What never happens on this graph is an improvement to a SETTLED "
                "vertex, and that is the property nearest-first depends on. It is guaranteed by "
                "the weights being non-negative and by nothing else.",
                "Notice that the heap and the scan performed the same 18 relaxations. They make "
                "identical choices; the 15 comparisons and the 42 reads are two ways of finding "
                "the same minimum. The arc-order schedule, which never asks which vertex is "
                "closest, pays 36 relaxations for a saving of all the bookkeeping &mdash; and on "
                "a graph where the arcs happen to be in a good order it would pay far less, "
                "which is what &ldquo;Negative Weights and Bellman&ndash;Ford&rdquo; is about.",
                "For a faded rehearsal, delete the edge `3-6` and predict all six distances "
                "before running it. The supplied first move is this: the route to 6 through 3 "
                "cost `9 + 2 = 11`, and without it the only remaining routes to 6 are the direct "
                "edge at 14 and the way round through 5. Say what `d[6]` becomes, then say what "
                "happens to `d[5]`, and check both.",
            ],
        },
        "quiz_title": "Steps, schedules and invariants",
        "quiz": [
            {"q": "Three schedules reach the same distances on the graph on screen. What does that establish?",
             "a": ["That the relaxation step is order-independent in general",
                   "That all three are correct on graphs with non-negative weights",
                   "That they agree on this graph; the general claim is a separate theorem",
                   "That the heap schedule is unnecessary"],
             "c": 2,
             "why": "Agreement on one graph is agreement on one graph, which is exactly the "
                    "hazard this path is about. The general statement &mdash; nearest-first "
                    "settles every vertex with its true distance whenever no weight is negative "
                    "&mdash; is proved separately, and the agreement is evidence about the run "
                    "rather than about all runs."},
            {"q": "Partway through any run, a vertex has label 12 while its true shortest distance is 9. Which is possible?",
             "a": ["Yes: the label is an upper bound and may still fall",
                   "No: the invariant says the label equals the distance",
                   "No: the label would have to be below 9",
                   "Only under the arc-order schedule"],
             "c": 0,
             "why": "The invariant is that the label is the length of SOME path, hence never "
                    "below the true distance &mdash; above it is exactly the state a run is in "
                    "before that vertex's best route has been relaxed. A label below the true "
                    "distance is what would be impossible, and that is what the lab checks after "
                    "every step."},
            {"q": "On these undirected edges, what does a single negative weight mean?",
             "a": ["Shortest paths still exist but need a different algorithm",
                   "The graph contains a negative cycle, so shortest paths do not exist",
                   "Only the heap schedule fails; the other two still work",
                   "The weight is treated as zero"],
             "c": 1,
             "why": "An edge traversable in both directions can be walked out and back, and with "
                    "a negative weight that round trip lowers the total by twice the weight and "
                    "can be repeated. There is no shortest path to improve on. The lab prints "
                    "labels anyway, including a negative label for the source, so that the "
                    "failure is visible rather than hidden."},
            {"q": "The scan schedule does 42 label reads where the heap does 15 key comparisons, on the same graph. What follows?",
             "a": ["The heap is always the better choice",
                   "The two do different amounts of bookkeeping for the same 18 relaxations, on this graph",
                   "The scan performs more relaxations",
                   "The heap's answer is more accurate"],
             "c": 1,
             "why": "Both perform 18 relaxations because they make the same choices; the "
                    "difference is only in how the minimum is located. On other presets the gap "
                    "moves either way &mdash; 56 reads against no comparisons at all on a chain, "
                    "30 reads against 14 comparisons on a denser graph &mdash; so which is "
                    "cheaper is a property of the graph."},
        ],
        "mistakes": [
            ("Confusing the step with the schedule",
             "&ldquo;Dijkstra's algorithm&rdquo; names a schedule, and the arithmetic in it is "
             "the same arithmetic the other two schedules perform. A reader who treats them as "
             "three algorithms has three things to remember and no way to see that the next two "
             "lessons change only the order. The lab makes the schedule a control precisely so "
             "it can be varied while nothing else is."),
            ("Taking a settled vertex as settled without the non-negativity",
             "The one thing nearest-first does that the other schedules do not is refuse to "
             "reconsider. That refusal is licensed by there being no way for a later route to be "
             "cheaper, which is a consequence of every weight being at least 0. Drop that and "
             "the schedule quietly returns wrong numbers, which is the subject of "
             "&ldquo;Negative Weights and Bellman&ndash;Ford&rdquo; and of &ldquo;Shortest and "
             "Longest Paths in a DAG&rdquo;."),
            ("Reading the reference column as a budget",
             "`E` times an integer logarithm is printed so the measured counts can be watched "
             "against a scale across several graphs. On the opening graph it equals the "
             "relaxation count exactly, which is a coincidence of nine edges and six vertices, "
             "and reading that coincidence as confirmation of anything is the error the column's "
             "label is trying to prevent."),
        ],
        "standard": ("Finish when you can run all three schedules on a graph you have not seen and explain why they must agree.",
                     "You should be able to state the relaxation step and the invariant, run "
                     "nearest-first by hand recording the settle order, say what the other two "
                     "schedules do differently, read the three counter sets as costs rather than "
                     "as answers, and say precisely why a negative weight on an undirected edge "
                     "ends the question."),
        "note": ("&ldquo;Negative Weights and Bellman&ndash;Ford&rdquo; gives the arcs a direction "
                 "and lets the weights go negative, which makes the arc-order schedule above "
                 "into an algorithm rather than a curiosity. &ldquo;Shortest and Longest Paths "
                 "in a DAG&rdquo; then takes the other extreme &mdash; a graph "
                 "with no cycles at all, where a single pass in the right order is enough and "
                 "the longest path becomes computable too."),
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "negative-weights-and-bellman-ford",
        "title": "Negative Weights and Bellman–Ford",
        "module": "Shortest paths",
        "one_line": "Sweep every arc once per round, watch each label become final, and get a negative cycle back as the cycle itself.",
        "summary": (
            "Relax every arc, `V - 1` times over. After round `i` every label that has a "
            "shortest path of at most `i` arcs is correct, so `V - 1` rounds suffice &mdash; a "
            "shortest path cannot repeat a vertex. If a round `V` still improves something then "
            "no shortest path exists, and the predecessor pointers hold the negative cycle that "
            "is the reason. Nothing here settles a vertex, which is exactly why it survives a "
            "negative arc."
        ),
        "key": [
            "one round = relax every arc once, in whatever order they are stored",
            "after round i: every label with a shortest path of at most i arcs is correct",
            "V - 1 rounds suffice, because a shortest path has at most V - 1 arcs",
            "still improving in round V  ->  a negative cycle, returned as the cycle",
            "the arc ORDER changes the number of rounds, never the answer",
        ],
        "key_label": "One sweep per round, and what a round guarantees",
        "concepts_intro": (
            "The hard idea is the round invariant, because it is about the number of arcs on a "
            "path rather than about distance. The stopping rule and the certificate follow."
        ),
        "concepts": [
            ("A round buys one more arc of path length",
             "After one full sweep, every vertex whose shortest path uses one arc is correct; "
             "after two, every vertex whose shortest path uses at most two; and so on. A "
             "shortest path never repeats a vertex, because removing a repeated stretch cannot "
             "make it longer unless that stretch was negative &mdash; and if it was, no shortest "
             "path exists at all. So `V - 1` arcs is the most any shortest path has, and `V - 1` "
             "rounds is enough."),
            ("Nothing is settled, which is why negative arcs are survivable",
             "Dijkstra&rsquo;s schedule declares a vertex finished and stops relaxing its "
             "outgoing arcs. Here every arc is relaxed in every round, so a label that improves "
             "late still propagates. On the lab's opening graph the label at vertex 5 improves "
             "in the second round, from 2 to `-2`, and the nearest-first schedule on the same "
             "graph returns 2 &mdash; the right shape of answer and the wrong number."),
            ("The certificate is the cycle, not a flag",
             "If a full round after the `V - 1` still changes a label, some path uses `V` arcs "
             "and is therefore shorter than one that repeats no vertex, which means a cycle of "
             "negative total weight. Walking the predecessor pointers back `V` times from a "
             "vertex that moved lands inside that cycle, and following them round closes it. On "
             "`1>2 1, 2>3 -3, 3>4 1, 4>2 1` the lab returns the cycle 2, 3, 4, 2, which weighs "
             "`-3 + 1 + 1 = -1`."),
        ],
        "read_title": "Rounds, the invariant, and the certificate",
        "read_intro": "Why a round is the right unit, why V minus 1 of them suffice, what the arc order changes, and the negative cycle as evidence.",
        "body": [
            ("h3", "The algorithm"),
            ("ol", ["Set the source's label to 0 and every other to infinity.",
                    "Repeat `V - 1` times: relax every arc, once, in whatever order they happen "
                    "to be stored.",
                    "Stop early if a full round changes nothing, because nothing later will "
                    "change either.",
                    "Perform one more round. If anything improves, report a negative cycle and "
                    "recover it from the predecessor pointers."]),
            ("thm", ("The round invariant",
                     "After `i` complete rounds, for every vertex `v` whose shortest path from "
                     "the source uses at most `i` arcs, `d[v]` equals that shortest distance.")),
            ("proof", ("By induction on `i`. For `i = 0` the only such vertex is the source, "
                       "whose label is 0.",
                       "Assume it after `i` rounds and let `v` have a shortest path `s, ..., u, "
                       "v` with `i + 1` arcs. The prefix to `u` is itself a shortest path with "
                       "`i` arcs, so `d[u]` is correct after round `i`, by hypothesis. Round "
                       "`i + 1` relaxes the arc from `u` to `v` at some point, and by then "
                       "`d[u]` is at most its correct value, so afterwards `d[v]` is at most "
                       "`d[u] + w`, the true shortest distance. The upper-bound invariant of the "
                       "relaxation step says it is not less, so it is equal.")),
            ("p", "Note what the proof does not need: the arcs may be relaxed in any order "
                  "within a round, and `d[u]` may have been improved earlier in the same round, "
                  "which only helps. That is why the algorithm is indifferent to how the arcs are "
                  "stored, and also why the number of rounds it actually needs is not."),
            ("example", ("Five vertices, four negative arcs, and no negative cycle",
                         "The lab opens on `1>2 6, 1>3 7, 2>3 8, 2>4 5, 2>5 -4, 3>4 -3, 3>5 9, "
                         "4>2 -2, 5>1 2, 5>4 7` from vertex 1. The distances come out `0, 2, 7, "
                         "4, -2`. The first round reaches `0, 2, 7, 4, 2` and the second improves "
                         "only vertex 5, to `-2`; the third changes nothing and the run stops "
                         "after 3 rounds and 30 relaxations. Floyd's all-pairs matrix, computed "
                         "separately, gives the same row from vertex 1. The nearest-first "
                         "schedule gives `0, 2, 7, 4, 2`.")),
            ("p", "The route to vertex 2 is `1, 3, 4, 2`, three arcs, at `7 - 3 - 2 = 2`. Its "
                  "label was already final after the first round even though its path has three "
                  "arcs, because the arcs happened to be swept in an order that carried the "
                  "improvement all the way along in one pass. The invariant promises correctness "
                  "by round three; it does not forbid getting there sooner."),
            ("h3", "The arc order is worth a measurement of its own"),
            ("p", "Take a chain of five arcs each of weight 1, and type it backwards: "
                  "`5>6 1, 4>5 1, 3>4 1, 2>3 1, 1>2 1`. Each round pushes the frontier forward "
                  "by exactly one arc, so the run takes 6 rounds and 20 relaxations, and the "
                  "round each label became final is `0, 1, 2, 3, 4, 5`. Type the same five arcs "
                  "forwards and one sweep carries the improvement the whole way: 2 rounds, 10 "
                  "relaxations, and every label final in round 1. Both give the distances "
                  "`0, 1, 2, 3, 4, 5`."),
            ("p", "That is the cleanest example on this course of a count moving while an answer "
                  "does not. Same vertices, same arcs, same weights, same distances; two thirds "
                  "less work. And it is also why the bound is `V - 1` rounds rather than "
                  "something smaller: the backwards chain needs every one of them, so no smaller "
                  "number is correct for all inputs."),
            ("h3", "The certificate"),
            ("thm", ("Negative cycle detection",
                     "If a round after the `V - 1` improves any label, then some cycle reachable "
                     "from the source has negative total weight, and no shortest path exists to "
                     "the vertices beyond it. If no such round improves anything, every label is "
                     "a true shortest distance.")),
            ("p", "The forward direction is the round invariant read backwards: if no negative "
                  "cycle is reachable then every shortest path has at most `V - 1` arcs, so "
                  "round `V - 1` finished the job and round `V` finds nothing. If something does "
                  "improve, the improving path uses `V` arcs, hence repeats a vertex, hence "
                  "contains a cycle; and it could only be an improvement if that cycle is "
                  "negative."),
            ("example", ("A negative cycle, returned as the cycle",
                         "On `1>2 1, 2>3 -3, 3>4 1, 4>2 1` the lab runs all four rounds, "
                         "something changes in the last, and 16 relaxations are performed. The "
                         "labels it prints, `0, -3, -5, -4`, are not distances and the panel does "
                         "not present them as any: they are one lap further round the loop than "
                         "the previous values. What it returns instead is the cycle "
                         "2, 3, 4, 2, whose weight is `-1`, so every lap subtracts one more.")),
            ("p", "A flag saying &ldquo;negative cycle&rdquo; would leave the reader with "
                  "nowhere to go. The cycle itself is actionable: in a scheduling or currency "
                  "model it names the loop that must be broken, and in a debugging session it "
                  "names the arc whose weight was typed with the wrong sign."),
            ("p", "Measured against proved. On the opening graph: 3 rounds, 30 relaxations, "
                  "five distances. On the backwards chain: 6 rounds, 20 relaxations. The bound "
                  "is `O(V E)`, from `V - 1` rounds of `E` relaxations each, and it is attained "
                  "&mdash; the backwards chain needs every round. What the measurements cannot "
                  "tell you is that no ordering forces more than `V - 1`, and that is what the "
                  "invariant is for."),
        ],
        "lab": ("graphkit", {
            "mode": "bellmanford",
            "preset": "negative",
            "panel_title": "Type the arcs; negative weights are the subject",
            "panel_intro": "The table is one row per round. The round each label became final is "
                           "compared with the number of arcs on its own shortest path, the "
                           "distances are compared with an all-pairs matrix that never mentions "
                           "a round, and a negative cycle comes back as the cycle itself rather "
                           "than as a flag.",
        }),
        "steps_title": "Running the rounds",
        "steps_intro": "One sweep is one unit of progress. Count the sweeps, not the improvements.",
        "steps": [
            ("Sweep every arc every round, including the ones that did nothing",
             "Skipping arcs whose tails did not change is a real optimisation and it changes what "
             "the round invariant says. Get the plain version right first: the correctness "
             "argument is about complete sweeps, and a partial sweep needs its own argument."),
            ("Stop early on a round that changes nothing",
             "If a full sweep improves no label, no later sweep can either, since nothing has "
             "changed for it to build on. On the forwards chain this cuts six rounds to two. It "
             "is the one shortcut that costs nothing to justify."),
            ("Run the extra round deliberately",
             "The `V`-th round is not part of computing the distances; it is the test for "
             "whether they mean anything. Code that stops at `V - 1` returns numbers on a graph "
             "with a negative cycle and gives no sign that they are not distances."),
            ("Recover the cycle rather than reporting a boolean",
             "From a vertex that improved in the last round, follow the predecessor pointers "
             "back `V` times to land inside the cycle, then follow them until you return to "
             "where you started. That is the evidence, and it is what makes the result "
             "actionable rather than merely negative."),
        ],
        "worked": {
            "title": "Three rounds on ten arcs, and the label that moves late",
            "intro": [
                "The arcs are `1>2 6, 1>3 7, 2>3 8, 2>4 5, 2>5 -4, 3>4 -3, 3>5 9, 4>2 -2, "
                "5>1 2, 5>4 7`, swept in that order, from vertex 1.",
            ],
            "lines": [
                "start        d = 0   -   -   -   -",
                "",
                "round 1, sweeping the ten arcs in order",
                "  1>2 6      d[2] = 6",
                "  1>3 7      d[3] = 7",
                "  2>4 5      d[4] = 11",
                "  2>5 -4     d[5] = 2",
                "  3>4 -3     d[4] = 4          (7 - 3 beats 11)",
                "  4>2 -2     d[2] = 2          (4 - 2 beats 6)",
                "  after round 1     d = 0   2   7   4   2",
                "",
                "round 2      2>5 -4 gives d[5] = 2 - 4 = -2",
                "  after round 2     d = 0   2   7   4  -2",
                "",
                "round 3      nothing improves; stop            3 rounds, 30 relaxations",
                "",
                "round each label became final     0   1   1   1   2",
                "arcs on its own shortest path     0   3   1   2   4",
                "",
                "route to 2   1 - 3 - 4 - 2       7 - 3 - 2 = 2",
                "route to 5   1 - 3 - 4 - 2 - 5   7 - 3 - 2 - 4 = -2",
                "",
                "the all-pairs matrix, row from 1        0   2   7   4  -2      agrees",
                "nearest unfinished first on the same arcs  0   2   7   4   2   WRONG at 5",
            ],
            "after": [
                "The round-final column is at most the arc-count column at every vertex, and "
                "strictly below it at three of them. That is the invariant doing exactly what it "
                "promises and no more: round `i` guarantees correctness for paths of at most `i` "
                "arcs, and a lucky sweep order can deliver a four-arc path in round two.",
                "Vertex 5 is where the nearest-first schedule breaks. That schedule settles 5 at "
                "2 when 2 is the smallest unfinished label, and never revisits it; the arc "
                "`2>5` of weight `-4` then improves `d[2]`'s own route too late to help. Here "
                "every arc is relaxed in every round, so nothing is too late.",
                "For a faded rehearsal, change `5>1 2` to `5>1 -2` and predict what the lab "
                "reports before running it. The supplied first move is this: the route to 5 "
                "costs `-2`, so going on to 1 now costs `-4`, and 1 already had a label of 0. "
                "Say whether that makes the loop through 1, 3, 4, 2, 5 negative, what the extra "
                "round will find, and what the panel should print instead of distances.",
            ],
        },
        "quiz_title": "Rounds, orders and certificates",
        "quiz": [
            {"q": "A label becomes final in round 1 although its shortest path uses three arcs. Is the invariant violated?",
             "a": ["Yes: round 1 may only finalise one-arc paths",
                   "No: the invariant is a guarantee by round i, not a prohibition before it",
                   "No, but only because the graph has negative weights",
                   "Yes, and it means the arc order was illegal"],
             "c": 1,
             "why": "The invariant says every at-most-`i`-arc path is correct AFTER round `i`; it "
                    "says nothing about what else may already be correct. A sweep that happens "
                    "to relax the arcs of a path in order carries the improvement the whole way "
                    "in one round, which is exactly what the lab's opening graph does for vertex "
                    "2."},
            {"q": "The same five arcs typed in two different orders give 6 rounds and 2 rounds. What does that show?",
             "a": ["One of the two runs is wrong",
                   "The number of rounds needed depends on the arc order while the distances do not",
                   "The bound of `V - 1` rounds is not tight",
                   "The forwards order should always be used"],
             "c": 1,
             "why": "Both runs return `0, 1, 2, 3, 4, 5`. The backwards order advances the "
                    "frontier one arc per round and needs all of them, which is precisely what "
                    "makes `V - 1` tight; the forwards order finishes in one sweep plus the "
                    "confirming one. Arcs are not generally arriving in a helpful order, which "
                    "is why the bound is the one quoted."},
            {"q": "After `V - 1` rounds, one more round improves a label. What has been established?",
             "a": ["That the algorithm needs more rounds",
                   "That some reachable cycle has negative total weight, so shortest paths do not exist beyond it",
                   "That the graph is disconnected",
                   "That the labels are correct but the predecessors are not"],
             "c": 1,
             "why": "An improving path after `V - 1` rounds uses `V` arcs, so it repeats a "
                    "vertex, so it contains a cycle &mdash; and it improved, so that cycle is "
                    "negative. Running more rounds only subtracts more. The lab returns the "
                    "cycle itself rather than a flag, because the cycle is what a caller can act "
                    "on."},
            {"q": "Why can the nearest-unfinished-first schedule not be used on the lab's opening graph?",
             "a": ["Because the graph is directed",
                   "Because it settles a vertex and never reconsiders it, and here a later arc does reduce a settled label",
                   "Because there is a negative cycle",
                   "Because the heap cannot hold negative keys"],
             "c": 1,
             "why": "There is no negative cycle on that graph &mdash; the distances exist and "
                    "Bellman-Ford finds them. What fails is the settling rule: vertex 5 is "
                    "settled at 2 and an improvement to vertex 2 afterwards would have reduced "
                    "it to `-2`, and nothing goes back. The lab prints both answers side by "
                    "side."},
        ],
        "mistakes": [
            ("Stopping at `V - 1` rounds and reporting the labels",
             "On a graph with a reachable negative cycle those labels are one lap's worth of "
             "arithmetic, not distances, and nothing about them looks wrong. The extra round is "
             "the only thing standing between a correct answer and a confidently presented "
             "meaningless one, and it costs a single sweep."),
            ("Reading the rounds needed as a property of the graph",
             "It is a property of the graph and the arc order together. The lab's two chain "
             "presets are the same graph with the arcs typed in two orders, and they take 6 "
             "rounds and 2. Anyone benchmarking this algorithm on one arc ordering and quoting "
             "the round count has measured their input format."),
            ("Treating the absence of settling as an inefficiency to be fixed",
             "Relaxing every arc in every round is what makes a late improvement propagate, and "
             "that is the whole reason this algorithm survives negative arcs where nearest-first "
             "does not. The optimisation of skipping arcs whose tails have not changed is real, "
             "but it is a change to the algorithm and it needs its own correctness argument."),
        ],
        "standard": ("Finish when you can run the rounds by hand, read the round-final column against the arc count, and recover a cycle.",
                     "You should be able to sweep the arcs in order recording the label table per "
                     "round, state what round `i` guarantees, explain why `V - 1` is both "
                     "sufficient and tight, run the extra round as a test rather than as part of "
                     "the computation, and walk the predecessor pointers back to a negative "
                     "cycle."),
        "note": ("&ldquo;Shortest and Longest Paths in a DAG&rdquo; removes the cycles entirely. "
                 "On a graph with no cycle at all "
                 "there is an order in which one sweep suffices &mdash; the topological order "
                 "&mdash; and because no cycle can be repeated for profit, the same pass with "
                 "the sign flipped computes the LONGEST path, which is a problem nothing else on "
                 "this course can solve."),
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "shortest-and-longest-paths-in-a-dag",
        "title": "Shortest and Longest Paths in a DAG",
        "module": "Shortest paths",
        "one_line": "Relax each arc exactly once in topological order, then flip the sign and read the critical path off the same pass.",
        "summary": (
            "On an acyclic digraph the arcs can be put in an order where every tail is settled "
            "before its head is ever relaxed, so one relaxation per arc is enough &mdash; no "
            "rounds, no heap, and negative weights make no difference. Reverse the comparison "
            "and the same pass returns the longest path instead, which on a general graph is a "
            "problem no algorithm on this course solves. The difference is that a DAG has no "
            "cycle to go round for profit."
        ),
        "key": [
            "topological order first; then relax each arc once, tails before heads",
            "exactly E relaxations, whatever the weights are",
            "flip the comparison and the same pass gives the LONGEST path",
            "latest start, computed backwards from the far end; slack = latest - earliest",
            "no order  ->  refuse: a graph with a cycle has no topological order",
        ],
        "key_label": "One pass, either extreme, and the slack that falls out",
        "concepts_intro": (
            "The hard idea is why one pass suffices. Longest paths and slack are both that same "
            "pass with a sign or a direction changed."
        ),
        "concepts": [
            ("One pass, because the order guarantees the tail is done",
             "Process the vertices in topological order. When `v` is reached, every arc into `v` "
             "came from a vertex earlier in the order, and every earlier vertex has already had "
             "all its outgoing arcs relaxed. So `d[v]` is final the moment `v` is reached, and "
             "each arc is relaxed exactly once. On the lab's opening project the pass performs 7 "
             "relaxations on 7 arcs, and the rounds method on the same graph agrees with the "
             "answer."),
            ("Longest paths, because there is no cycle to exploit",
             "Reverse the comparison in the relaxation step and the pass maximises instead. That "
             "would be nonsense on a general graph &mdash; a positive cycle could be walked "
             "forever &mdash; but a DAG has no cycle at all, so the longest path is finite and "
             "the same argument goes through unchanged. On the opening project the shortest "
             "route to the end is 6 and the longest is 10."),
            ("Slack is the second pass, and it must be seeded at the far end",
             "The latest a vertex may be scheduled without delaying the end is computed "
             "backwards: seed only the far end at its own earliest time, and take the minimum "
             "over successors of their latest minus the arc weight. Slack is latest minus "
             "earliest. Seeding every vertex at its own earliest time instead gives zero slack "
             "everywhere, which looks plausible and is wrong; the lab computes it the right way "
             "and reports the vector."),
        ],
        "read_title": "One pass in the right order, and the four things it gives",
        "read_intro": "Why a single pass suffices, the sign flip, the backward pass and slack, and what happens when there is no order.",
        "body": [
            ("h3", "The algorithm"),
            ("ol", ["Compute a topological order. If none exists, stop: the graph has a cycle "
                    "and this method does not apply.",
                    "Set the source's label to 0 and every other to infinity.",
                    "Visit the vertices in topological order; at each one, relax every arc out "
                    "of it.",
                    "For the longest path, reverse the comparison in the relaxation step and "
                    "change nothing else."]),
            ("thm", ("One pass suffices",
                     "On an acyclic digraph processed in topological order, `d[v]` equals the "
                     "shortest distance from the source at the moment `v` is visited, and each "
                     "arc is relaxed exactly once.")),
            ("proof", ("By induction along the order. The source's label is 0 and correct. Let "
                       "`v` be the next vertex, and let `s, ..., u, v` be a shortest path to it.",
                       "Every arc of that path goes forwards in the topological order, so `u` "
                       "precedes `v` and was visited earlier. By hypothesis `d[u]` was correct "
                       "when `u` was visited, and the arc from `u` to `v` was relaxed then, "
                       "giving `d[v] &le; d[u] + w`, which is the true distance. The upper-bound "
                       "invariant says it is no smaller.",
                       "Each arc is relaxed when its tail is visited, and each vertex is visited "
                       "once, so the arc count is exact.")),
            ("p", "Nothing in that argument mentions the sign of a weight. A negative arc "
                  "changes which number is smaller and changes nothing about the order in which "
                  "vertices are visited, which is why this is the one shortest-path method on "
                  "the course that handles negative weights at no extra cost at all."),
            ("example", ("Seven arcs, one pass, two answers",
                         "The lab opens on `1>2 3, 1>3 2, 2>4 4, 3>4 1, 4>5 2, 3>5 7, 5>6 1`. A "
                         "topological order is 1, 3, 2, 4, 5, 6. The shortest pass gives `0, 3, "
                         "2, 3, 5, 6` in 7 relaxations, one per arc, by the route 1, 3, 4, 5, 6. "
                         "The longest pass, on the same 7 relaxations, gives `0, 3, 2, 7, 9, 10` "
                         "by the route 1, 3, 5, 6. Both are confirmed by the rounds method on the "
                         "shortest reading.")),
            ("h3", "Slack, and the backward pass that produces it"),
            ("p", "Read the longest reading as a project: each arc is a task with a duration and "
                  "each vertex is a milestone. The longest distance to a vertex is the earliest "
                  "it can happen. The latest it may happen without delaying the end is computed "
                  "the other way, and the difference is the slack &mdash; how much the "
                  "corresponding task may slip for free."),
            ("p", "Three details in that backward pass all produce something that looks like "
                  "slack when they are wrong. It must be seeded ONLY at the far end, and at the "
                  "far end's own extreme distance. Its extremum is the opposite of the forward "
                  "pass's: under the longest reading the backward pass takes a minimum over "
                  "successors. And the subtraction goes the arc's own way, latest of the head "
                  "minus the weight. Get any of the three wrong and the answer is a vector of "
                  "plausible non-negative numbers."),
            ("p", "On the opening project every vertex has slack 0 under the longest reading, "
                  "because every vertex lies on a critical path: the latest vector equals the "
                  "earliest vector exactly. On the lab's wide preset `1>2 5, 2>3 5, 3>6 5, "
                  "1>4 7, 4>5 4, 5>6 3, 1>6 2` the longest distances are `0, 5, 10, 7, 11, 15` "
                  "and the slack is `0, 0, 0, 1, 1, 0`: the route through 4 and 5 finishes at 14 "
                  "where the critical route finishes at 15, so those two milestones may each "
                  "slip by one."),
            ("p", "The shortest reading has a slack of its own and it means something different: "
                  "on the opening project it is `0, 4, 0, 0, 0, 0`, so vertex 2 is four longer "
                  "than the cheapest route needs. Slack is never negative under either reading, "
                  "which is a cheap check that the backward pass was done correctly."),
            ("h3", "Where the settling schedule goes wrong and this one does not"),
            ("example", ("Four vertices, one negative arc",
                         "On `1>2 2, 1>3 3, 3>2 -2, 2>4 1` the topological order is 1, 3, 2, 4 "
                         "and the one pass gives `0, 1, 3, 2` in 4 relaxations. The rounds method "
                         "agrees. The nearest-unfinished-first schedule gives `0, 1, 3, 3`: it "
                         "settled vertex 2 at label 2, relaxed the arc out of it from that label, "
                         "and by the time vertex 2 improved to 1 it had already been declared "
                         "finished. The lab prints all three.")),
            ("p", "The gap is one at vertex 4, which is small enough to be missed and large "
                  "enough to be wrong. It is the clearest demonstration on this course that "
                  "settling is an assumption rather than an optimisation: the topological "
                  "schedule settles too, in the sense that `d[v]` is final when `v` is visited, "
                  "but it settles in an order the arcs themselves justify."),
            ("h3", "The graph this does not work on, and how it says so"),
            ("p", "On `1>2 3, 2>3 2, 3>1 1, 3>4 5` there is no topological order, and the lab "
                  "returns no distances rather than numbers. That refusal is the right behaviour "
                  "and it is worth seeing why the longest reading in particular cannot be "
                  "rescued: negate every weight and the cycle 1, 2, 3 becomes a cycle of weight "
                  "`-6`, so the rounds method reports it as a negative cycle. A longest walk on a "
                  "graph with a cycle does not exist, and the trick that computes it on a DAG "
                  "does not extend."),
            ("p", "Measured against proved. On the opening project: 7 relaxations for the "
                  "shortest reading and 7 for the longest, on 7 arcs, plus one topological sort. "
                  "That is `Θ(V + E)` for that graph. The bound is `Θ(V + E)` on every acyclic "
                  "graph, and the proof is that each arc is relaxed when its tail is visited and "
                  "each vertex is visited once &mdash; so unlike the rounds method, the "
                  "measurement here cannot vary with the arc order at all."),
        ],
        "lab": ("graphkit", {
            "mode": "dagsp",
            "preset": "project",
            "panel_title": "Type the arcs and choose shortest or longest",
            "panel_intro": "One relaxation per arc, in topological order. The values are checked "
                           "against the rounds method, and against the nearest-unfinished-first "
                           "schedule as well &mdash; which on a graph with a negative arc returns "
                           "something different, printed beside them. Slack comes from a "
                           "backward pass seeded only at the far end.",
        }),
        "steps_title": "Running the single pass",
        "steps_intro": "Order first, then one sweep. Everything else is the same sweep read differently.",
        "steps": [
            ("Get the order before you relax anything",
             "The whole saving depends on every tail being visited before its head, and that is "
             "what the topological order guarantees and nothing else does. If the order does not "
             "exist, stop and say so: there is no repair, and the rounds method is the tool for "
             "that graph."),
            ("Relax out of each vertex as you visit it",
             "Sweeping the arcs by tail, in order, is what makes the arc count exactly `E`. "
             "Relaxing into each vertex from its predecessors is equally valid and needs the "
             "reversed arc list; mixing the two is how an arc gets relaxed twice or not at all."),
            ("Flip the comparison, and nothing else, for the longest path",
             "Not the weights, not the order, not the initialisation. Negating the weights also "
             "works and is a useful way to see why it is legitimate, but it is two changes where "
             "one will do, and on a graph with a cycle it is the version that exposes why the "
             "trick fails."),
            ("Compute slack backwards, from the far end only",
             "Seed the far end at its own extreme distance and nothing else, take the opposite "
             "extremum over successors, and subtract each arc's weight from the head's value. "
             "Then check that no slack came out negative &mdash; that check costs nothing and "
             "catches all three of the ways this pass is usually written wrong."),
        ],
        "worked": {
            "title": "One project, read two ways",
            "intro": [
                "The arcs are `1>2 3, 1>3 2, 2>4 4, 3>4 1, 4>5 2, 3>5 7, 5>6 1`, and the "
                "topological order the lab produces is 1, 3, 2, 4, 5, 6.",
            ],
            "lines": [
                "visit   arcs relaxed        shortest labels            longest labels",
                "  1     1>2, 1>3            0  3  2  -  -  -           0  3  2  -  -  -",
                "  3     3>4, 3>5            0  3  2  3  9  -           0  3  2  3  9  -",
                "  2     2>4                 0  3  2  3  9  -           0  3  2  7  9  -",
                "  4     4>5                 0  3  2  3  5  -           0  3  2  7  9  -",
                "  5     5>6                 0  3  2  3  5  6           0  3  2  7  9 10",
                "  6     none",
                "",
                "shortest   0  3  2  3  5  6      route 1 - 3 - 4 - 5 - 6      7 relaxations",
                "longest    0  3  2  7  9 10      route 1 - 3 - 5 - 6          7 relaxations",
                "",
                "slack, shortest reading    0  4  0  0  0  0",
                "slack, longest reading     0  0  0  0  0  0      every vertex is critical",
                "",
                "the rounds method on the shortest reading   0  3  2  3  5  6     agrees",
            ],
            "after": [
                "Under the longest reading, vertex 4 goes to 7 when vertex 2 is visited and stays "
                "there when vertex 4 itself is visited, because the route through 2 is longer "
                "than the route through 3. Under the shortest reading the opposite happens. The "
                "two columns differ at exactly the vertices where the two routes differ, and "
                "nothing else about the pass changed.",
                "Notice that the longest reading leaves no slack anywhere on this project. That "
                "is not the usual case; it means every milestone lies on some critical path, so "
                "any delay anywhere delays the end. The lab's wide preset is the contrasting "
                "shape, where two routes race and the slower one has a spare unit at each of its "
                "two interior vertices.",
                "For a faded rehearsal, change `3>5 7` to `3>5 3` and predict both readings "
                "before running it. The supplied first move is this: the longest route to 5 was "
                "1, 3, 5 at `2 + 7 = 9`, and the competing route 1, 2, 4, 5 is `3 + 4 + 2 = 9` "
                "as well. Say which route becomes critical, what the longest distance to 6 "
                "becomes, and where slack now appears.",
            ],
        },
        "quiz_title": "Order, sign and slack",
        "quiz": [
            {"q": "Why does one pass suffice on a DAG when the rounds method needs up to `V - 1` sweeps?",
             "a": ["Because a DAG has fewer arcs",
                   "Because the topological order guarantees every tail is final before its head is relaxed",
                   "Because a DAG has no negative weights",
                   "Because the heap finds the right order automatically"],
             "c": 1,
             "why": "Every arc goes forwards in the order, so by the time a vertex is visited all "
                    "of its predecessors are done. A DAG may have as many arcs as any graph and "
                    "may certainly have negative weights &mdash; the lab's own trap preset does "
                    "&mdash; and the heap schedule is exactly what gets the wrong answer on that "
                    "preset."},
            {"q": "Longest paths are computed here by flipping one comparison. Why can the same trick not be used on a general digraph?",
             "a": ["Because the topological order does not exist, and a positive cycle could be walked forever",
                   "Because the relaxation step is not defined for maximisation",
                   "Because the weights would have to be negated first",
                   "Because the heap cannot be reversed"],
             "c": 0,
             "why": "Two reasons and they are the same reason: with a cycle there is no order to "
                    "sweep in, and a cycle of positive total weight makes the longest walk "
                    "unbounded. The lab shows the second explicitly by negating a cyclic graph, "
                    "at which point the rounds method reports a negative cycle."},
            {"q": "On a DAG with a negative arc, the one pass gives `0, 1, 3, 2` and the nearest-unfinished-first schedule gives `0, 1, 3, 3`. Which is right and why?",
             "a": ["The heap schedule, since it settles vertices in distance order",
                   "The one pass: the heap settled a vertex at 2, relaxed its outgoing arc from that label, and never went back when it improved to 1",
                   "Neither: with a negative arc no shortest path exists",
                   "Both: they are answers to different questions"],
             "c": 1,
             "why": "There is no cycle, so the distances exist, and the rounds method confirms "
                    "the one pass. The heap schedule's settling rule is licensed only by "
                    "non-negative weights; with one negative arc a settled label can still "
                    "improve, and its outgoing arcs were relaxed from the stale value."},
            {"q": "A backward pass reports zero slack at every vertex of a project with two routes of clearly different lengths. What is the most likely cause?",
             "a": ["The project really has no slack",
                   "The backward pass was seeded at every vertex rather than only at the far end",
                   "The forward pass used the shortest reading by mistake",
                   "The slack was computed as earliest minus latest"],
             "c": 1,
             "why": "Seeding every vertex at its own earliest time leaves the pass unable to move "
                    "anything later, so nothing off the critical path ever reports slack. It is "
                    "the first of the three ways this pass is written wrong, and all three "
                    "produce non-negative numbers that look like slack."},
        ],
        "mistakes": [
            ("Trying the one pass on a graph with a cycle",
             "There is no topological order to sweep, so there is nothing to run, and the "
             "honest response is to refuse. The lab does, returning no distances rather than "
             "numbers. Any implementation that falls back on an arbitrary vertex order here will "
             "return something, and what it returns is not a distance."),
            ("Believing a DAG cannot have negative weights",
             "The two properties are unrelated: a DAG forbids cycles, not negative numbers. The "
             "lab's trap preset is an acyclic graph with one negative arc, and it is the graph on "
             "which the nearest-first schedule gives the wrong answer while this pass gives the "
             "right one. Acyclicity is what makes negative weights harmless, not what excludes "
             "them."),
            ("Computing slack forwards",
             "The latest a vertex may be scheduled is determined by what comes after it, so the "
             "pass runs backwards, is seeded only at the far end, and takes the opposite extremum "
             "of the forward pass. Each of the three is easy to get wrong and none of them makes "
             "the output look wrong: the only free check is that no slack is negative."),
        ],
        "standard": ("Finish when you can run the pass both ways on a graph you have not seen, and produce the slack vector.",
                     "You should be able to compute a topological order, relax each arc exactly "
                     "once in that order, flip the comparison for the longest path, run the "
                     "backward pass seeded at the far end to get slack, and say precisely why "
                     "the settling schedule is wrong on a DAG with a negative arc while this one "
                     "is not."),
        "note": ("That is the last of the shortest-path methods. The final module changes the "
                 "question from what a route costs to how much can be sent along all routes at "
                 "once, and it is the one place on this course where the algorithm produces its "
                 "own proof of optimality instead of the lesson supplying one."),
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "augmenting-paths",
        "title": "Augmenting Paths",
        "module": "Flow and matching",
        "one_line": "Push flow along a path, discover that a first choice has to be undone, and watch a backward arc undo it.",
        "summary": (
            "A flow is an assignment of a number to every arc that respects capacities and "
            "conserves at every interior vertex. Raise its value by finding a path from source to "
            "sink with spare capacity and pushing the bottleneck along it. The whole subject "
            "turns on one detail: the path may also run backwards along an arc that already "
            "carries flow, and without that the method stops below the maximum."
        ),
        "key": [
            "capacity constraint  0 <= f(a) <= c(a)        on every arc",
            "conservation         in = out                 at every vertex but s and t",
            "residual network     forward spare c - f, and backward f",
            "augment              push the bottleneck along a path from s to t",
            "maximal is not maximum: no path left under a restricted rule is not the same thing",
        ],
        "key_label": "What a flow is, and the one arc that is easy to leave out",
        "concepts_intro": (
            "The hard idea is the backward arc. The definition and the residual network exist to "
            "make it expressible."
        ),
        "concepts": [
            ("A flow is two constraints, and both are checkable",
             "Every arc carries a number between 0 and its capacity, and at every vertex other "
             "than the source and the sink the total in equals the total out. The value of the "
             "flow is what leaves the source. The lab checks both constraints on whatever it "
             "produces and reports a verdict per vertex, so &ldquo;this is a flow&rdquo; is a "
             "measured statement rather than an assumption."),
            ("The residual network is where the search happens",
             "For each arc carrying `f` out of a capacity `c`, the residual network holds a "
             "forward arc of capacity `c - f`, meaning how much more can be pushed, and a "
             "backward arc of capacity `f`, meaning how much of the existing flow can be taken "
             "back. A path from source to sink in that network is an augmenting path, and the "
             "bottleneck is the smallest residual capacity on it."),
            ("Undoing an earlier choice is not an optimisation",
             "On the lab's opening network the first-found rule takes a path through the middle "
             "arc, pushes 1, and then cannot find a second path at all &mdash; the value stops at "
             "1. With backward arcs available the same rule finds a second path that runs "
             "backwards along the middle arc, and reaches 2. The stuck flow is a perfectly legal "
             "flow; it is maximal, in that nothing can be added to it under that restriction, "
             "and it is not maximum."),
        ],
        "read_title": "What a flow is, and the one arc the search must have",
        "read_intro": "The two constraints, the residual network, the augmenting step, the failure without backward arcs, and what the path rule costs.",
        "body": [
            ("def", ("Flow, and its value",
                     "Given a digraph with a non-negative capacity `c(a)` on every arc, a source "
                     "`s` and a sink `t`, a <strong>flow</strong> assigns to each arc a number "
                     "`f(a)` with `0 &le; f(a) &le; c(a)`, such that at every vertex other than "
                     "`s` and `t` the total on incoming arcs equals the total on outgoing ones. "
                     "Its <strong>value</strong> is the net amount leaving `s`.")),
            ("def", ("The residual network",
                     "For a flow `f`, the <strong>residual network</strong> has, for each arc `a` "
                     "from `u` to `v`, a forward arc from `u` to `v` of capacity `c(a) - f(a)` "
                     "and a backward arc from `v` to `u` of capacity `f(a)`. Arcs of residual "
                     "capacity 0 are omitted. An <strong>augmenting path</strong> is any path "
                     "from `s` to `t` in it, and its <strong>bottleneck</strong> is the least "
                     "residual capacity along it.")),
            ("p", "Pushing the bottleneck along an augmenting path &mdash; adding it on each "
                  "forward arc and subtracting it on each backward one &mdash; produces a flow "
                  "again, whose value is higher by the bottleneck. Capacities hold because the "
                  "bottleneck was the minimum, and conservation holds because each interior "
                  "vertex of the path gains the same amount on one side as the other."),
            ("h3", "The method"),
            ("ol", ["Start with zero on every arc.",
                    "Build the residual network and look for a path from `s` to `t` in it.",
                    "If there is one, push its bottleneck along it and repeat.",
                    "If there is not, stop."]),
            ("example", ("Four vertices, and a first push that has to be undone",
                         "The lab opens on `1>2 1, 1>3 1, 2>3 1, 2>4 1, 3>4 1` with source 1 and "
                         "sink 4, and with backward arcs switched OFF. The first-found rule takes "
                         "the three-arc path `1>2, 2>3, 3>4`, pushes its bottleneck of 1, and "
                         "then finds nothing: the search reaches only vertices 1 and 3, although "
                         "the arc `1>3` still has spare capacity. The value stops at 1. Switch "
                         "the backward arcs on and the same rule finds `1>3`, then backwards "
                         "along `2>3`, then `2>4`, pushes 1 more, and reaches 2.")),
            ("p", "Look at what the second path does. It sends a new unit from 1 to 3, cancels "
                  "the unit that was going 2 to 3, and sends that one on to 4 instead. The net "
                  "effect is two units arriving at the sink by two disjoint routes, and it was "
                  "reachable only by rewriting a decision the first path had made. That is why "
                  "the backward arc is part of the algorithm and not a refinement of it."),
            ("p", "The stuck flow is worth naming precisely. It satisfies both constraints "
                  "&mdash; the lab confirms conservation at every interior vertex &mdash; and no "
                  "more can be pushed without taking something back. It is MAXIMAL. The maximum "
                  "is 2. Two words that differ by three letters and by the whole content of this "
                  "module."),
            ("h3", "The rule that chooses the path is a second question"),
            ("p", "The failure above was exhibited with a RULE rather than with a hand-picked "
                  "path, and that matters: it is a claim about what an implementation does, not "
                  "about what an adversary could do. On the same network the shortest-path rule "
                  "happens never to take the middle arc, so it reaches 2 even with backward arcs "
                  "off. That does not rescue the forward-only method, it just means this network "
                  "does not defeat that particular rule."),
            ("example", ("One thin arc between two fat ones",
                         "On `1>2 100, 1>3 100, 2>3 1, 2>4 100, 3>4 100` both rules reach the "
                         "maximum of 200, and they take different numbers of steps to do it. The "
                         "shortest-path rule augments twice, by 100 each time. The first-found "
                         "rule augments four times, by 1, then 99, then 1, then 99: it walks into "
                         "the thin arc, pays for it with a backward arc later, and does it "
                         "twice.")),
            ("p", "That is the case the choice of rule is usually justified by, and the lab lets "
                  "you watch it rather than describing it. The shortest-path rule &mdash; always "
                  "take an augmenting path with the fewest arcs &mdash; is the one the kit's own "
                  "maximum-flow routine uses, and its augmentation count on this network is the "
                  "one the panel reports."),
            ("p", "On the six-vertex network with capacities from 4 to 20, the shortest-path "
                  "rule reaches 23 in three augmentations, pushing 12, then 4, then 7. Three "
                  "numbers that add to the answer, and the third path is four arcs long where "
                  "the first two were three &mdash; the rule takes the shortest available, and "
                  "what is available changes as the residual network does."),
            ("p", "Measured against proved, and this lesson is where the two are furthest apart. "
                  "Three augmentations reaching 23 is a measurement. That 23 cannot be beaten is "
                  "not something any number of augmentations can establish, because stopping "
                  "means only that this search found no path. &ldquo;Max Flow and Min Cut&rdquo; "
                  "supplies the missing half, and it is the one place on this course where the "
                  "algorithm hands back its own proof."),
        ],
        "lab": ("flowkit", {
            "mode": "augment",
            "preset": "forwardonly",
            "panel_title": "Type the network, then switch the backward arcs off",
            "panel_intro": "Each augmentation is one row: the path through the residual network, "
                           "the bottleneck pushed along it, and the value afterwards. The result "
                           "is checked against the maximum the shortest-path rule reaches with "
                           "backward arcs in place, so a run that stops early is shown stopping "
                           "early rather than reported as finished.",
        }),
        "steps_title": "Augmenting by hand",
        "steps_intro": "Build the residual network first; the search is then an ordinary reachability question.",
        "steps": [
            ("Draw the residual network, both directions",
             "For every arc write its spare capacity forwards and its current flow backwards, "
             "and omit anything at 0. Doing the search on the original network with the flow in "
             "your head is where the backward arcs get lost, and losing them does not look like "
             "an error &mdash; it looks like being finished."),
            ("Take the bottleneck, and take it everywhere on the path",
             "The amount pushed is the smallest residual capacity on the path, added on forward "
             "arcs and subtracted on backward ones. Pushing different amounts on different arcs "
             "breaks conservation, and pushing more than the minimum breaks a capacity."),
            ("Check that what you have is still a flow",
             "Both constraints, every arc and every interior vertex. It is `Θ(V + E)` and it "
             "catches a sign error on a backward arc immediately, which is the mistake that "
             "otherwise survives until the final value is compared with something."),
            ("When no path is left, do not conclude anything yet",
             "&ldquo;My search found no path&rdquo; and &ldquo;no augmenting path exists&rdquo; "
             "are the same statement only if the search was on the full residual network. The "
             "lab's opening preset is the case where they differ, and the honest report at this "
             "point is a value plus the rule that produced it."),
        ],
        "worked": {
            "title": "The same four-vertex network, with and without the backward arc",
            "intro": [
                "The network is `1>2 1, 1>3 1, 2>3 1, 2>4 1, 3>4 1`, every capacity 1, source 1 "
                "and sink 4. The rule is first-found, which takes arcs in the order they were "
                "typed.",
            ],
            "lines": [
                "backward arcs OFF",
                "  path      1>2   2>3   3>4       bottleneck 1     value 1",
                "  residual  1>2 full, 2>3 full, 3>4 full, 1>3 spare 1, 2>4 spare 1",
                "  search    from 1 reaches 3 through 1>3, and 3>4 is full: stop",
                "  reachable {1, 3}                                  value stays 1",
                "  is it a flow?  yes: conserved at 2 and at 3, inside every capacity",
                "",
                "backward arcs ON, same rule, same network",
                "  path 1    1>2   2>3   3>4       bottleneck 1     value 1",
                "  path 2    1>3   3>2 backwards   2>4   bottleneck 1     value 2",
                "  reachable afterwards  {1}                          no path exists",
                "",
                "what the second path did",
                "  new unit  1 -> 3 ,  cancel the unit 2 -> 3 ,  send that one 2 -> 4",
                "  net       1 -> 2 -> 4  and  1 -> 3 -> 4        two disjoint routes, value 2",
                "",
                "the shortest-path rule, backward arcs OFF",
                "  path 1    1>2   2>4                            value 1",
                "  path 2    1>3   3>4                            value 2",
            ],
            "after": [
                "The forward-only run ends with the source's own arcs not both full: `1>3` still "
                "has its whole unit of spare capacity. That is the signature of being stuck "
                "rather than finished, and it is visible without knowing the answer &mdash; a "
                "maximum flow in this network would have to saturate one side of every cut, and "
                "the source's two arcs are a cut.",
                "The last three lines are the reason the failure was demonstrated with a rule. "
                "The shortest-path rule never enters the middle arc here, so it does not need to "
                "undo anything on this particular network. A reader who saw only that rule would "
                "conclude the backward arcs are optional, and on a slightly larger network they "
                "would be wrong.",
                "For a faded rehearsal, raise the capacity of `2>3` from 1 to 5 and predict what "
                "the first-found rule does with backward arcs off. The supplied first move is "
                "this: the first path is still `1>2, 2>3, 3>4` and its bottleneck is still 1, "
                "because `1>2` and `3>4` are unchanged. Say whether the run still stops at 1, "
                "and then say what happens if you raise `1>2` to 5 as well.",
            ],
        },
        "quiz_title": "Flows, residuals, and stopping",
        "quiz": [
            {"q": "A run stops with no augmenting path and a value of 1, on a network whose maximum is 2. What was wrong?",
             "a": ["The flow violated conservation",
                   "The search was run without backward arcs, so it could not undo an earlier push",
                   "The bottleneck was computed as the maximum rather than the minimum",
                   "The sink was unreachable from the source in the original network"],
             "c": 1,
             "why": "The flow is legal &mdash; conserved and within every capacity &mdash; and "
                    "the sink is certainly reachable. What is missing is the residual arc that "
                    "lets a later path cancel part of an earlier one. That is the lab's opening "
                    "preset, and the flow it reaches is maximal rather than maximum."},
            {"q": "An augmenting path uses a backward arc. What does pushing along it do to that arc's flow?",
             "a": ["Increases it by the bottleneck",
                   "Decreases it by the bottleneck",
                   "Sets it to zero",
                   "Leaves it alone; backward arcs are only for the search"],
             "c": 1,
             "why": "A backward residual arc represents flow that can be taken back, so pushing "
                    "along it subtracts the bottleneck from the original arc. Conservation still "
                    "holds at both of its ends because the path enters and leaves each interior "
                    "vertex once. Leaving the arc alone would break conservation immediately."},
            {"q": "On one network the first-found rule augments four times and the shortest-path rule twice, both reaching 200. What does that measure?",
             "a": ["That the first-found rule is incorrect",
                   "That the two rules reach the same value at different costs, on this network",
                   "That the maximum flow depends on the rule",
                   "That the shortest-path rule is `O(VE)` and the other is not"],
             "c": 1,
             "why": "Both are correct and both reach 200; the difference is four augmentations "
                    "against two, with bottlenecks of 1, 99, 1, 99 against 100, 100. That is a "
                    "measurement on one network. A general bound on the number of augmentations "
                    "is a separate argument that this page does not make."},
            {"q": "What distinguishes a maximal flow from a maximum one?",
             "a": ["Nothing: the words are synonyms",
                   "A maximal flow saturates every arc; a maximum one need not",
                   "A maximal flow admits no further augmentation under the rule in use; a maximum one has the greatest possible value",
                   "A maximum flow is unique and a maximal one is not"],
             "c": 2,
             "why": "Maximal is a local property &mdash; nothing more can be added the way you "
                    "are adding &mdash; and maximum is a global one. The lab's opening preset "
                    "exhibits a maximal flow of value 1 where the maximum is 2, and neither flow "
                    "saturates every arc."},
        ],
        "mistakes": [
            ("Searching the original network instead of the residual one",
             "The arcs with spare capacity are only half of what is available, and the half that "
             "is missing is the one that makes the method correct. The symptom is a run that "
             "terminates cleanly with a legal flow below the maximum, which is the hardest kind "
             "of wrong answer to notice: nothing crashes and every constraint holds."),
            ("Reading a failed search as a proof that no path exists",
             "They are the same statement only when the search covered the full residual network "
             "and the graph is the one you think it is. The lab's opening preset separates them "
             "deliberately, and the separation is the reason the certificate in &ldquo;Max Flow "
             "and Min Cut&rdquo; matters: it is what turns a failed search into a proof."),
            ("Concluding the backward arcs are unnecessary because one rule managed without them",
             "The shortest-path rule reaches the maximum on the opening preset with backward arcs "
             "off, which is a fact about that network and that rule. Change the network and it "
             "stops being true. A demonstration that a restriction sometimes does no harm is not "
             "an argument that the restriction is safe."),
        ],
        "standard": ("Finish when you can augment by hand, including backwards, and say what stopping does and does not prove.",
                     "You should be able to build a residual network from a flow, find a path in "
                     "it, push the bottleneck with the right sign on each arc, verify both "
                     "constraints afterwards, and say precisely why a run that finds no further "
                     "path has not yet established that its value is the maximum."),
        "note": ("&ldquo;Max Flow and Min Cut&rdquo; closes that gap, and it closes it completely. "
                 "When the search "
                 "fails, the set of vertices it reached is itself a cut, and the total capacity "
                 "of the arcs leaving that set equals the value of the flow &mdash; which means "
                 "the algorithm hands back a proof of its own optimality rather than needing "
                 "one."),
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "max-flow-and-min-cut",
        "title": "Max Flow and Min Cut",
        "module": "Flow and matching",
        "one_line": "Read the certificate off the failed search, and check it against every cut the network has.",
        "summary": (
            "When no augmenting path remains, the set of vertices still reachable from the source "
            "in the residual network is a cut, every arc leaving it is full, and no arc comes "
            "back into it carrying anything. So the capacity of that cut equals the value of the "
            "flow &mdash; and since no flow can exceed any cut, both are optimal. The algorithm "
            "produces its own proof, and the lab checks it against an enumeration of every cut "
            "there is."
        ),
        "key": [
            "a cut is a set S containing the source and not the sink",
            "its capacity counts only arcs LEAVING S; arcs coming back count nothing",
            "every flow value <= every cut capacity          the weak direction, one line",
            "when the search fails, S = the reachable set, and the two are EQUAL",
            "saturated is not the same as being in a cut",
        ],
        "key_label": "One set, one capacity, and the equality that ends the search",
        "concepts_intro": (
            "The hard idea is that the certificate is free: it is the failed search's own "
            "reachable set. The asymmetry of a cut's capacity is what makes it work."
        ),
        "concepts": [
            ("A cut's capacity counts one direction only",
             "For a set `S` containing the source but not the sink, the capacity is the total "
             "capacity of the arcs from `S` to the outside. Arcs coming back into `S` contribute "
             "nothing at all. On the lab's backwards preset the set `{1, 2}` has capacity 6 with "
             "9 units of capacity pointing back into it, and that 9 is simply not part of the "
             "number. Readers who add it get a cut capacity that no flow ever approaches."),
            ("Every flow is below every cut, in one line",
             "Everything reaching the sink must cross from `S` to the outside at some point, and "
             "it can cross no faster than the capacity allows. So the value of ANY flow is at "
             "most the capacity of ANY cut. That one inequality is what makes an equality "
             "decisive: a flow and a cut of the same size prove each other optimal, with no "
             "further argument."),
            ("The failed search hands you the cut",
             "Let `S` be the vertices reachable from the source in the final residual network. "
             "The sink is not in it, or the search would have succeeded. Every arc from `S` to "
             "the outside is full, or its forward residual arc would have extended the search. "
             "Every arc from outside into `S` carries nothing, or its backward residual arc "
             "would have. So the net flow across the cut is exactly the cut's capacity, and it is "
             "also the value of the flow."),
        ],
        "read_title": "The certificate, and the enumeration that checks it",
        "read_intro": "What a cut is, the easy inequality, the theorem, what the lab enumerates, and the arc that is full and in no cut.",
        "body": [
            ("def", ("Cut, and its capacity",
                     "An <strong>s-t cut</strong> is a partition of the vertices into a set `S` "
                     "containing the source and its complement containing the sink. Its "
                     "<strong>capacity</strong> is the sum of `c(a)` over arcs `a` whose tail is "
                     "in `S` and whose head is not. Arcs in the other direction are not counted.")),
            ("thm", ("Weak duality",
                     "For any flow `f` and any s-t cut `S`, the value of `f` is at most the "
                     "capacity of `S`.")),
            ("proof", ("The value of `f` equals the net flow across the cut: summing "
                       "conservation over every vertex of `S` cancels every arc with both ends "
                       "inside, and leaves the total on arcs out of `S` minus the total on arcs "
                       "into it.",
                       "The first sum is at most the capacity of `S`, because each arc's flow is "
                       "at most its capacity. The second is at least 0, because flows are "
                       "non-negative. So the value is at most the capacity.")),
            ("thm", ("Max-flow min-cut",
                     "The maximum value of a flow equals the minimum capacity of an s-t cut. "
                     "Moreover, when the augmenting-path method stops, the set of vertices "
                     "reachable from the source in the residual network is a cut of exactly that "
                     "capacity.")),
            ("proof", ("Let `f` be the flow when no augmenting path remains, and let `S` be the "
                       "set reachable from the source in the residual network. The sink is not "
                       "in `S`, so `S` is a cut.",
                       "Take an arc from `u` in `S` to `v` outside. If it were not full, its "
                       "forward residual arc would have taken the search from `u` to `v`, so `v` "
                       "would be in `S`. Hence every such arc is full. Take an arc from `v` "
                       "outside to `u` in `S`. If it carried anything, its backward residual arc "
                       "would run from `u` to `v` and again put `v` in `S`. Hence every such arc "
                       "carries nothing.",
                       "So the net flow across the cut is the total capacity out of `S` minus "
                       "zero, which is the capacity of `S`; and the net flow across any cut is "
                       "the value of `f`. By weak duality no flow exceeds this cut and no cut is "
                       "below this flow, so both are optimal.")),
            ("example", ("Six vertices, three augmentations, one certificate",
                         "The lab opens on `1>2 16, 1>3 13, 2>3 10, 3>2 4, 2>4 12, 3>5 14, "
                         "4>3 9, 5>4 7, 4>6 20, 5>6 4` with source 1 and sink 6. The "
                         "shortest-path rule reaches 23 in three augmentations. The reachable "
                         "set afterwards is `{1, 2, 3, 5}`, and the arcs leaving it are `2>4` at "
                         "12, `5>4` at 7 and `5>6` at 4 &mdash; capacity 23, and all three are "
                         "full. Separately, all 16 sets containing 1 and not 6 are enumerated; "
                         "the smallest capacity among them is 23, attained by exactly one set, "
                         "and it is the one the algorithm returned.")),
            ("p", "Three numbers reached by three different routes: the flow's value, the "
                  "capacity of the cut read off the failed search, and the smallest capacity "
                  "among every cut there is, found without any flow at all. The theorem says they "
                  "are one number, and the panel computes them separately and compares."),
            ("h3", "Saturated is not the same as being in a cut"),
            ("p", "A full arc is not automatically part of a minimum cut, and this is the "
                  "misconception the lab's second preset exists for. On `1>2 1, 2>3 1, 3>4 5, "
                  "1>4 1` the maximum flow is 2, and three arcs end up full: `1>2`, `2>3` and "
                  "`1>4`. The cut is only `{1>2, 1>4}`, the two arcs out of the reachable set "
                  "`{1}`. Deleting `2>3` leaves the sink perfectly reachable; deleting the two "
                  "cut arcs does not."),
            ("p", "The reason is that `2>3` is full because of what happens downstream of it, "
                  "not because it is a bottleneck between the two sides. Being full is a local "
                  "fact about one arc; being in a cut is a statement about a partition. The lab "
                  "prints both the saturated set and the cut set so the difference is visible "
                  "rather than argued."),
            ("h3", "The minimum cut is not unique either"),
            ("p", "On a chain of three unit arcs, `1>2 1, 2>3 1, 3>4 1`, there are 4 sets "
                  "containing the source and not the sink, and 3 of them have capacity 1. The "
                  "algorithm returns one of them &mdash; the reachable set, which is `{1}` "
                  "&mdash; and the enumeration confirms that it is among the smallest. &ldquo;The "
                  "minimum cut&rdquo; names a value and picks out a set only when the value is "
                  "attained once, which on the opening network it is."),
            ("p", "And the asymmetry of the definition is worth one concrete number. On "
                  "`1>2 5, 2>3 5, 3>2 9, 3>4 5, 2>4 1` the maximum flow is 5. The set "
                  "`{1, 2, 3}` leaves 5 and 1, so its capacity is 6, with nothing coming back. "
                  "The set `{1, 2}` also has capacity 6 &mdash; and 9 units of capacity pointing "
                  "back into it, from `3>2`, which count for nothing. A definition that counted "
                  "them would make that cut 15 and would break the theorem."),
            ("p", "Measured against proved. The enumeration is exhaustive and it is also small: "
                  "16 cuts on six vertices, because only the four vertices that are neither "
                  "source nor sink can be placed freely, and it is refused above the size it "
                  "states. So the equality is read off a complete list on a network you can type "
                  "and proved by the reachable-set argument everywhere else. This is the one "
                  "lesson on the course where the measurement and the proof answer exactly the "
                  "same question, which is what makes it the strongest result here."),
        ],
        "lab": ("flowkit", {
            "mode": "mincut",
            "preset": "classic",
            "panel_title": "Type the network and read the certificate",
            "panel_intro": "The flow's value and the cut's capacity are computed separately and "
                           "compared. Every set holding the source and not the sink is then "
                           "enumerated, so the claim that no cut is smaller is a fact about a "
                           "list; and a set of full arcs that is not a cut is shown beside it.",
        }),
        "steps_title": "Reading the certificate",
        "steps_intro": "The cut is the failed search's own output. Take it, check it, and report both numbers.",
        "steps": [
            ("Take S from the final residual network, not from the original one",
             "Reachability in the original network would reach the sink. The set you want is "
             "what the last, failed search touched: forward along arcs with spare capacity and "
             "backward along arcs carrying flow. Recording it costs nothing because the search "
             "computed it already."),
            ("Add up the arcs leaving S, and only those",
             "Arcs from `S` to the outside, at full capacity, summed. Arcs pointing back in are "
             "excluded, and excluded is not the same as subtracted. The lab's backwards preset "
             "has 9 units pointing back into a cut of capacity 6, and both treatments of that 9 "
             "give the wrong number."),
            ("Compare the two figures and report both",
             "The value and the capacity should be equal. If they are not, one of them is wrong "
             "&mdash; usually the cut, from a mis-signed backward arc during augmentation. This "
             "is a free correctness check on the whole run and it is the reason to compute the "
             "cut even when only the value is wanted."),
            ("Do not read a set of full arcs as a cut",
             "Check it: delete exactly those arcs and see whether the sink is still reachable. "
             "On the lab's saturated preset three arcs are full and only two of them separate "
             "the two sides, and the third can be deleted without disconnecting anything."),
        ],
        "worked": {
            "title": "Three augmentations, then the set the search reached",
            "intro": [
                "The network is `1>2 16, 1>3 13, 2>3 10, 3>2 4, 2>4 12, 3>5 14, 4>3 9, 5>4 7, "
                "4>6 20, 5>6 4`, source 1, sink 6, under the shortest-path rule.",
            ],
            "lines": [
                "augmentation   path                          bottleneck   value after",
                "  1            1>2  2>4  4>6                     12            12",
                "  2            1>3  3>5  5>6                      4            16",
                "  3            1>3  3>5  5>4  4>6                 7            23",
                "  4            no path in the residual network                 23",
                "",
                "the set the failed search reached      S = {1, 2, 3, 5}",
                "arcs leaving S      2>4 at 12     5>4 at 7     5>6 at 4",
                "capacity                                  12 + 7 + 4 = 23",
                "all three full?                           yes",
                "arcs coming back into S carrying flow?    none",
                "",
                "value of the flow                         23",
                "capacity of the cut the search gave       23",
                "smallest of all 16 cuts, found separately 23        attained by 1 set",
                "conservation checked at vertices 2, 3, 4, 5         all hold",
            ],
            "after": [
                "Three augmentations and three bottlenecks that add to the answer: 12, 4 and 7. "
                "That is arithmetic about the run. The three 23s are the result, and they were "
                "produced by three methods that share nothing &mdash; pushing along paths, "
                "reading a reachable set, and enumerating every subset of four vertices.",
                "The third path is the interesting one. It is four arcs long where the first two "
                "were three, and it uses `5>4` to get to the sink through `4>6` after `5>6` has "
                "filled. The shortest-path rule takes the shortest path that exists at the time, "
                "and what exists changes as arcs fill.",
                "For a faded rehearsal, raise the capacity of `5>6` from 4 to 40 and predict the "
                "new value and the new cut before running it. The supplied first move is this: "
                "`5>6` is one of the three cut arcs, so relaxing it can only raise the minimum "
                "cut &mdash; but the arcs into 5 are limited by `3>5` at 14, and `1>3` at 13 "
                "limits that in turn. Say what the new maximum is, and which set attains it.",
            ],
        },
        "quiz_title": "Cuts, capacities and certificates",
        "quiz": [
            {"q": "A cut `S` has arcs out of it totalling 6 and arcs into it totalling 9. What is its capacity?",
             "a": ["15", "6", "3", "9"],
             "c": 1,
             "why": "Only arcs leaving `S` count. The 9 coming back is excluded entirely, not "
                    "netted off &mdash; counting it would give 15 and netting it off would give "
                    "&minus;3, and both break the theorem. The lab's backwards preset is exactly this network, "
                    "with a maximum flow of 5."},
            {"q": "The augmenting-path method stops with value 23, and the reachable set has capacity 23. What has been proved?",
             "a": ["That 23 is the maximum flow and that set is a minimum cut",
                   "That 23 is the maximum flow, but the cut may not be minimum",
                   "Only that the flow is maximal under the rule used",
                   "Nothing until every cut is enumerated"],
             "c": 0,
             "why": "Weak duality says no flow exceeds any cut, so a flow and a cut of equal size "
                    "pin each other from both sides: no flow can beat 23 because this cut caps "
                    "it, and no cut can be below 23 because this flow requires it. The "
                    "enumeration in the lab confirms it; the proof does not need it."},
            {"q": "Three arcs are full at the end of a run and the cut has two arcs. What is the third arc?",
             "a": ["A second minimum cut of size one",
                   "An arc that is full for downstream reasons and lies in no cut; deleting it leaves the sink reachable",
                   "Evidence that the flow is not maximum",
                   "An arc that was pushed twice"],
             "c": 1,
             "why": "Being saturated is a local fact about one arc. On the lab's saturated preset "
                    "the full arc `2>3` can be deleted and the sink is still reachable, whereas "
                    "deleting the two cut arcs separates the two sides. Saturation and membership "
                    "of a cut are different properties that coincide on the cut arcs only."},
            {"q": "On a chain of three unit arcs, the enumeration finds three minimum cuts. What does the algorithm return?",
             "a": ["All three", "The reachable set, which is one of the three",
                   "An error, since the minimum cut is not unique",
                   "The largest of the three"],
             "c": 1,
             "why": "The certificate is the reachable set of the final failed search, which on "
                    "that chain is the source alone. The enumeration then confirms it is among "
                    "the smallest. &ldquo;The minimum cut&rdquo; names a value; it identifies a "
                    "set only when that value is attained once."},
        ],
        "mistakes": [
            ("Counting arcs that point back into the cut",
             "The definition is one-directional and the theorem depends on it. On the lab's "
             "backwards preset a cut of capacity 6 has 9 units pointing back into it; counting "
             "them gives 15 and netting them off gives &minus;3, and the maximum flow is 5. The "
             "one arithmetic that is right is to ignore them."),
            ("Reading the saturated arcs as the cut",
             "It is the most natural wrong answer, because every cut arc is indeed full. The "
             "converse fails, and the check is cheap: delete the arcs you think form a cut and "
             "ask whether the sink is still reachable. The lab does that check and prints the "
             "verdict."),
            ("Treating the enumeration as what establishes the theorem",
             "Sixteen cuts on six vertices is a fact about six vertices, and the enumeration is "
             "refused above the size it states. The reachable-set argument is what covers every "
             "network, and the enumeration's job is to catch the equality being asserted about a "
             "cut that was computed wrongly &mdash; which is what it is good at."),
        ],
        "standard": ("Finish when you can produce the certificate from a failed search and check it three ways.",
                     "You should be able to compute a cut's capacity counting only the arcs that "
                     "leave it, state and prove weak duality in one line, take the reachable set "
                     "as the cut when the search fails, explain why every arc leaving it is full "
                     "and every arc entering it is empty, and separate saturation from membership "
                     "of a cut."),
        "note": ("&ldquo;Bipartite Matching&rdquo; applies the theorem rather than proving anything "
                 "new: a bipartite matching problem becomes a flow network with every capacity 1, "
                 "the maximum flow is the size of the largest matching, and the minimum cut read "
                 "back is a set of vertices covering every pair &mdash; which is a classical "
                 "theorem obtained here as a corollary."),
    },
    # ---------------------------------------------------------------- 13
    {
        "slug": "bipartite-matching",
        "title": "Bipartite Matching",
        "module": "Flow and matching",
        "one_line": "Turn a pairing problem into a unit-capacity network, and read the matching, the cover and the obstruction off one run.",
        "summary": (
            "Pairing up two sides so that nobody is used twice is a maximum-flow problem in "
            "disguise: give every arc capacity 1, add a source feeding the left and a sink fed "
            "by the right, and the value of the maximum flow is the size of the largest "
            "matching. The minimum cut, read back through the construction, is a set of vertices "
            "touching every pair, and where the matching falls short it exhibits the reason."
        ),
        "key": [
            "source to every left vertex, capacity 1; every right vertex to the sink, capacity 1",
            "one arc of capacity 1 per allowed pair, left to right",
            "max flow = size of the largest matching, and every flow value is a whole number",
            "min cut read back = a smallest set of vertices touching every pair",
            "maximal is not maximum: the greedy answer depends on the order",
        ],
        "key_label": "One construction, and the three things one run returns",
        "concepts_intro": (
            "The hard idea is the correspondence, in both directions. The cover and the "
            "obstruction are then the max-flow certificate translated back."
        ),
        "concepts": [
            ("The construction, and why it is exact both ways",
             "Every matching of size `k` gives a flow of value `k`: push one unit along the "
             "source arc, the pair arc and the sink arc of each matched pair, and no capacity is "
             "exceeded because no vertex is matched twice. Every integer flow of value `k` gives "
             "a matching of size `k`: the pair arcs carrying flow share no endpoint, because each "
             "left vertex admits one unit in and each right vertex emits one unit out. So the two "
             "maxima are the same number, and neither direction has slack in it."),
            ("Whole numbers, because every capacity is one",
             "The augmenting-path method pushes the bottleneck of each path, and on this network "
             "every residual capacity is 0 or 1, so every push is by 1 and every arc ends "
             "carrying 0 or 1. The lab checks this rather than assuming it &mdash; the flow is "
             "reported as whole on every case &mdash; because a fractional flow would carry no "
             "matching at all."),
            ("The cut translates into a cover, and the shortfall into an obstruction",
             "The minimum cut of this network, read back, is a set containing some left vertices "
             "and some right ones such that every allowed pair has an end in it &mdash; a vertex "
             "cover &mdash; and its size equals the matching's. On the lab's opening case with "
             "three on the left and two on the right, the matching has size 2 and the cover is "
             "the left vertex 3 together with the right vertex 1, also size 2. Two left vertices "
             "between them reach only one right vertex, and that deficiency is what makes a "
             "perfect matching impossible."),
        ],
        "read_title": "One network, and the three readings of its answer",
        "read_intro": "The construction, the correspondence in both directions, the cover, the deficient set, and why greedy is not enough.",
        "body": [
            ("def", ("Matching, maximal, maximum",
                     "A <strong>matching</strong> in a bipartite graph is a set of allowed pairs "
                     "no two of which share a vertex. It is <strong>maximal</strong> if no "
                     "further pair can be added to it, and <strong>maximum</strong> if no "
                     "matching is larger. A matching is <strong>perfect</strong> on the left if "
                     "every left vertex is in it.")),
            ("h3", "The construction"),
            ("ol", ["Add a source with an arc of capacity 1 to every left vertex.",
                    "Add a sink with an arc of capacity 1 from every right vertex.",
                    "For each allowed pair, add an arc of capacity 1 from the left vertex to the "
                    "right one.",
                    "Find a maximum flow. The pair arcs carrying flow are a maximum matching."]),
            ("thm", ("The two maxima coincide",
                     "In the network above, the maximum flow value equals the size of a maximum "
                     "matching, and a maximum matching can be read off any integer maximum flow "
                     "as the set of pair arcs carrying one unit.")),
            ("proof", ("A matching gives a flow of the same value, by routing one unit through "
                       "each matched pair. The capacity 1 on the source arcs and the sink arcs is "
                       "respected because a matching uses each vertex at most once, and "
                       "conservation holds at every left and right vertex by construction.",
                       "An integer flow of value `k` gives a matching of size `k`. Each pair arc "
                       "carries 0 or 1. If two pair arcs carrying flow shared a left vertex, that "
                       "vertex would emit 2 while receiving at most 1, breaking conservation; the "
                       "same argument on the right settles the other side. So the arcs carrying "
                       "flow form a matching, and there are `k` of them because `k` units leave "
                       "the source along distinct arcs.",
                       "Each maximum therefore bounds the other, so they are equal. The "
                       "augmenting-path method returns an integer flow on this network because "
                       "every capacity is 1 and every bottleneck is therefore 1.")),
            ("example", ("Three on the left competing for two",
                         "The lab opens on three left vertices and two right ones with the "
                         "allowed pairs L1&ndash;R1, L2&ndash;R1, L3&ndash;R1 and "
                         "L3&ndash;R2. The network has 7 vertices and 9 arcs, and the maximum "
                         "flow is 2, reached in two augmentations. The matching is L1 with R1 and "
                         "L3 with R2. The cut, read back, is the cover {L3, R1}, of size 2. A "
                         "search over every subset of the four pairs, which knows nothing about "
                         "flow, also returns 2.")),
            ("p", "Check the cover against the pairs: L1&ndash;R1 is covered by R1, "
                  "L2&ndash;R1 by R1, L3&ndash;R1 by both, and L3&ndash;R2 by L3. Four pairs, two "
                  "vertices, everything touched. And no single vertex could do it, because "
                  "L1&ndash;R1 and L3&ndash;R2 share nothing &mdash; which is the matching "
                  "bounding the cover from below."),
            ("h3", "Why the matching stopped at two"),
            ("p", "The left vertices 1 and 2 have only one right vertex between them: both are "
                  "joined to R1 and nothing else. Two of them cannot both be matched into one, so "
                  "no matching covers all three left vertices. The lab exhibits that set rather "
                  "than describing it, reporting `S = {L1, L2}` with a neighbourhood of size 1 "
                  "against a set of size 2."),
            ("p", "That is the general shape of the obstruction: a set of left vertices whose "
                  "combined neighbourhood is smaller than itself. Whenever the matching misses a "
                  "left vertex, the cut hands one back. It is a proof that no better matching "
                  "exists, in a form a reader can check by looking at four pairs rather than by "
                  "trusting a flow."),
            ("p", "The lab's star case is the same phenomenon at a larger scale: four on each "
                  "side with the pairs L1&ndash;R1, L2&ndash;R1, L3&ndash;R1, L4&ndash;R1 and "
                  "L4&ndash;R4. The maximum matching is 2, the cover is {L4, R1} of size 2, and "
                  "the deficient set is {L1, L2, L3} with a neighbourhood of exactly one vertex. "
                  "One popular right vertex is the whole story, and the cover names it."),
            ("h3", "Greedy is maximal, and the order decides how maximal"),
            ("example", ("Three pairs, two orders, two answers",
                         "Take two vertices on each side with the pairs L2&ndash;R2, "
                         "L1&ndash;R2 and L2&ndash;R1. Taking them greedily in that order gives "
                         "one pair: L2&ndash;R2 is taken and it blocks both of the others. Taking "
                         "the same three pairs in the order L1&ndash;R2, L2&ndash;R1, "
                         "L2&ndash;R2 gives two. The maximum is 2, confirmed by the exhaustive "
                         "search and by the flow, and the cover has size 2 as well.")),
            ("p", "So a matching nothing can be added to may be half the size of the largest one, "
                  "and which happens depends only on the order the pairs were considered in. That "
                  "is the same distinction &ldquo;Augmenting Paths&rdquo; drew between maximal and "
                  "maximum flow, appearing here in its most concrete form &mdash; and the augmenting path "
                  "is exactly what repairs it, because an augmenting path in this network "
                  "alternates between unmatched and matched pairs and swaps them."),
            ("p", "Where the matching is perfect there is nothing to exhibit. On three left and "
                  "three right with six pairs the lab returns a matching of size 3, a cover of "
                  "size 3, and a greedy pass that also finds 3; the network has 8 vertices and 12 "
                  "arcs. The construction is unchanged, and the absence of a deficient set is the "
                  "report."),
            ("p", "Measured against proved, for the last time on this course. The exhaustive "
                  "search over subsets of the pairs is refused above the size it states &mdash; "
                  "seventeen pairs is declined rather than run slowly &mdash; so below that cap "
                  "&ldquo;this matching is maximum&rdquo; is a fact about a complete list, and "
                  "above it the claim rests on the flow and its cut. The equality of the matching "
                  "and the cover is proved by the max-flow min-cut theorem and confirmed on "
                  "every case the panel runs, which is the right division of labour: the "
                  "enumeration catches a construction that is wrong, and the theorem covers the "
                  "sizes the enumeration cannot reach."),
        ],
        "lab": ("flowkit", {
            "mode": "matching",
            "preset": "hall",
            "panel_title": "Type the pairs; the network is built from them",
            "panel_intro": "The matching is the middle layer of a maximum flow, and the cover is "
                           "read off the same cut. Both are compared with a search over every "
                           "subset of the pairs, which knows nothing about flow, and with a "
                           "greedy pass that stops too early &mdash; and where the matching is "
                           "imperfect the deficient set is exhibited rather than described.",
        }),
        "steps_title": "Solving a pairing problem",
        "steps_intro": "Build the network, run one maximum flow, then read three things off it.",
        "steps": [
            ("Build the network before you look for a pairing",
             "Source to left at capacity 1, right to sink at capacity 1, one arc per allowed "
             "pair. Every constraint of the problem is now a capacity, and nothing about matching "
             "has to be re-implemented &mdash; which is the point of the reduction and the reason "
             "it is worth the extra vertices."),
            ("Check that the flow came back whole",
             "Every capacity is 1, so every bottleneck is 1 and every arc ends at 0 or 1. If any "
             "arc carries a fraction, the flow does not correspond to a matching at all, and the "
             "check costs one pass over the arcs."),
            ("Read the matching off the middle layer",
             "The pair arcs carrying one unit are the matching. Not the source arcs, which only "
             "say which left vertices were used, and not the saturated arcs generally &mdash; the "
             "distinction drawn in &ldquo;Max Flow and Min Cut&rdquo; applies here too."),
            ("When the matching is short, produce the obstruction",
             "The cut gives a vertex cover of the same size, and where a left vertex is unmatched "
             "it also gives a set of left vertices with too few neighbours. Report that set: it "
             "is what makes the shortfall explicable, and it is the difference between "
             "&ldquo;no&rdquo; and &ldquo;no, because these two both need that one&rdquo;."),
        ],
        "worked": {
            "title": "Three on the left, two on the right, and why two is the answer",
            "intro": [
                "The allowed pairs are L1 with R1, L2 with R1, L3 with R1, and L3 with R2. Three "
                "left vertices, two right ones, four pairs.",
            ],
            "lines": [
                "the network        7 vertices, 9 arcs, every capacity 1",
                "  s > L1, s > L2, s > L3",
                "  L1 > R1,  L2 > R1,  L3 > R1,  L3 > R2",
                "  R1 > t, R2 > t",
                "",
                "augmentation   path                     bottleneck   value",
                "  1            s > L1 > R1 > t              1           1",
                "  2            s > L3 > R2 > t              1           2",
                "  3            no path remains                          2",
                "",
                "matching       L1 - R1 ,  L3 - R2                       size 2",
                "cover          L3  and  R1                              size 2",
                "  L1-R1 covered by R1      L2-R1 covered by R1",
                "  L3-R1 covered by both    L3-R2 covered by L3",
                "",
                "every subset of the four pairs, searched exhaustively:   2",
                "greedy, in the order typed:                              2",
                "",
                "the obstruction     S = {L1, L2}      their neighbours = {R1}",
                "                    2 left vertices reaching 1 right vertex",
            ],
            "after": [
                "The cover and the matching have the same size, and that is not a coincidence of "
                "this instance: it is the max-flow min-cut theorem, since the cover is the "
                "minimum cut read back through the construction and the matching is the maximum "
                "flow. Every pair must be touched by the cover, and no two matched pairs can be "
                "touched by one vertex, so the cover is at least the matching and the theorem "
                "makes it equal.",
                "The deficient set is the part a human can check without any of the machinery. "
                "L1 and L2 both need R1 and nothing else; one of them will go unmatched whatever "
                "is done. That sentence is a complete proof that 3 is impossible, and it came out "
                "of the cut.",
                "For a faded rehearsal, add the pair L2 with R2 and predict the matching, the "
                "cover and the obstruction before running it. The supplied first move is this: "
                "L2 now has two choices, so the set {L1, L2} reaches both right vertices and is "
                "no longer deficient. Say what the maximum matching becomes, whether any left "
                "vertex is still unmatched, and what the cover should then be.",
            ],
        },
        "quiz_title": "Matchings, covers and obstructions",
        "quiz": [
            {"q": "Why is the maximum flow in this network guaranteed to be a whole number?",
             "a": ["Because flows are always integers",
                   "Because every capacity is 1, so every bottleneck is 1",
                   "Because the network is bipartite",
                   "Because the source has only one arc"],
             "c": 1,
             "why": "Each augmentation pushes the least residual capacity on its path, and on "
                    "this network every residual capacity is 0 or 1. Flows in general may be "
                    "fractional; bipartiteness alone does not force integrality; and the source "
                    "has one arc per left vertex. The lab checks the wholeness rather than "
                    "assuming it, because a fractional answer would carry no matching."},
            {"q": "A greedy pass takes the pairs in the order given and returns a matching of size 1, while the maximum is 2. What does that show?",
             "a": ["The greedy pass has a bug",
                   "That a matching nothing can be added to may be smaller than the largest one, and the order decides which you get",
                   "That the maximum matching is not unique",
                   "That the flow network was built incorrectly"],
             "c": 1,
             "why": "The same three pairs in another order give 2, so the greedy pass is correct "
                    "about being maximal and wrong about being maximum. This is the matching form "
                    "of the distinction &ldquo;Augmenting Paths&rdquo; drew, and the augmenting path is "
                    "exactly the repair: it alternates matched and unmatched pairs and swaps "
                    "them."},
            {"q": "The matching has size 2 and the cover read off the cut has size 2. Which statement is justified?",
             "a": ["Every pair has an end in the cover, and no smaller set does",
                   "Every vertex is either matched or in the cover",
                   "The matching is perfect",
                   "The cover is the set of matched vertices"],
             "c": 0,
             "why": "A cover must touch every pair, and no cover can be smaller than a matching, "
                    "since no vertex covers two matched pairs. Equality therefore certifies both. "
                    "It is not the matched-vertex set &mdash; on the lab's opening case the "
                    "matching uses L1, R1, L3 and R2 while the cover is L3 and R1."},
            {"q": "Three left vertices, two right ones, and the maximum matching is 2. What does the lab exhibit as the reason?",
             "a": ["That there are more left vertices than right ones",
                   "A set of left vertices whose combined neighbourhood is smaller than the set",
                   "The unmatched left vertex",
                   "The list of every matching it tried"],
             "c": 1,
             "why": "Having more left vertices than right ones is not itself the reason &mdash; "
                    "it makes a left-perfect matching impossible here, but the general "
                    "obstruction is deficiency, and the lab reports `S = {L1, L2}` with a "
                    "neighbourhood of one vertex. That set is checkable by hand and is a complete "
                    "proof that 3 is unreachable."},
        ],
        "mistakes": [
            ("Giving the source or sink arcs a capacity above one",
             "The capacity 1 on those arcs is what encodes &ldquo;each vertex may be used "
             "once&rdquo;. Raise it and the maximum flow rises too, and what comes back is no "
             "longer a matching &mdash; it is a set of pairs in which some vertex appears twice. "
             "Nothing about the flow looks wrong; the constraint has simply stopped being "
             "expressed."),
            ("Taking the saturated arcs as the matching",
             "The source and sink arcs are saturated too, and they are not pairs. The matching is "
             "the middle layer: the arcs from a left vertex to a right vertex that carry one "
             "unit. This is the same confusion &ldquo;Max Flow and Min Cut&rdquo; drew out between "
             "saturation "
             "and membership of a cut, in a setting where the wrong answer has the right size."),
            ("Reporting a shortfall without the obstruction",
             "&ldquo;The largest matching has size 2&rdquo; is an answer nobody can act on. "
             "&ldquo;L1 and L2 both need R1, so one of them cannot be placed&rdquo; names what "
             "would have to change. The cut supplies it at no extra cost, and the lab prints "
             "both the cover and the deficient set for exactly that reason."),
        ],
        "standard": ("Finish when you can build the network from a pairing problem and read all three answers off one run.",
                     "You should be able to write down the source and sink arcs with the right "
                     "capacities, argue the correspondence in both directions, extract the "
                     "matching from the middle layer, translate the cut into a vertex cover, and "
                     "produce the deficient set that explains a shortfall rather than reporting "
                     "only its size."),
        "note": ("This is the last lesson of the course. What carries forward is the pattern "
                 "rather than the algorithm: a problem that mentions no flow at all was solved by "
                 "building a network, and the certificate came back translated into the original "
                 "vocabulary. The next course generalises a different result from this one "
                 "&mdash; the cut property and the sorted method are the instance that the "
                 "matroid theorem is the abstraction of, which is why they were built here "
                 "first."),
    },
]
