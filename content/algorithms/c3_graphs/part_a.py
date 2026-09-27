"""Graph Algorithms, lessons 01-07 - searching a graph, and minimum spanning trees."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "depth-first-search-and-the-timestamps",
        "title": "Depth-First Search and the Timestamps",
        "module": "Searching a graph",
        "one_line": "Run one walk, write two numbers on every vertex, and classify every arc from those numbers alone.",
        "summary": (
            "A depth-first walk writes two numbers on each vertex: the step it was discovered "
            "and the step it was finished. Everything else this course reads off a walk comes "
            "from those two numbers. Whether one vertex is a descendant of another, whether the "
            "graph has a cycle, and which of four classes an arc belongs to are all decided by "
            "arithmetic on two intervals, and none of them needs a second pass."
        ),
        "key": [
            "d[v] discovery, f[v] finish     one counter, incremented twice per vertex",
            "tree      the arc that discovered its head",
            "back      d[head] < d[tail] and f[tail] < f[head]: the head is still open",
            "forward   d[tail] < d[head] and f[head] < f[tail], and it is not the tree arc",
            "cross     the two intervals are disjoint",
            "parenthesis theorem:  two intervals nest or are disjoint, never overlap",
        ],
        "key_label": "Two times per vertex, and the four classes they decide",
        "concepts_intro": (
            "One hard idea: the interval. The classes and the cycle test are both consequences of "
            "it, and neither is a separate thing to remember."
        ),
        "concepts": [
            ("Two times, and the interval between them",
             "A depth-first walk keeps one counter. It ticks when a vertex is first reached, "
             "giving <strong>d[v]</strong>, and again when the walk has finished with every arc "
             "out of it, giving <strong>f[v]</strong>. The pair `[d[v], f[v]]` is an interval on "
             "the timeline, and `v` is open for exactly that stretch. On the lab's opening graph "
             "the walk starts at 1 and the six intervals come out `[1, 8]`, `[2, 7]`, `[9, 12]`, "
             "`[4, 5]`, `[3, 6]` and `[10, 11]` &mdash; twelve ticks for six vertices, because "
             "every vertex is opened once and closed once."),
            ("Four classes, each decided by arithmetic on two intervals",
             "An arc from `u` to `v` is a <strong>tree</strong> arc when it is the one that "
             "discovered `v`; a <strong>back</strong> arc when `v` is still open, which is "
             "`d[v] &lt; d[u]` with `f[u] &lt; f[v]`; a <strong>forward</strong> arc when `v` is "
             "an already finished descendant of `u`; and a <strong>cross</strong> arc when the "
             "two intervals do not meet at all. Nothing else is consulted &mdash; not the drawing, "
             "not the order the arcs were typed, only the four numbers at the arc's ends."),
            ("A back arc is a cycle, and it is the whole test",
             "If `u` has an arc to a vertex `v` that is still open, then `v` is an ancestor of "
             "`u`, so the tree path from `v` down to `u` exists; that path plus the arc is a "
             "cycle. Run it the other way and a cycle must produce a back arc, because the first "
             "vertex of the cycle the walk reaches stays open until every other vertex on it has "
             "been finished. So &ldquo;acyclic&rdquo; and &ldquo;no back arc in one walk&rdquo; "
             "are the same statement, and the second is checkable in one pass."),
        ],
        "read_title": "One walk, and everything it writes down",
        "read_intro": "The two times, the four classes, the theorem that the intervals obey, and the cycle test that falls out of it.",
        "body": [
            ("def", ("Discovery and finish times",
                     "A <strong>depth-first walk</strong> of a digraph keeps a counter starting "
                     "at 0. On reaching an undiscovered vertex `v` it increments the counter and "
                     "records <strong>d[v]</strong>; after every arc out of `v` has been "
                     "considered it increments the counter again and records "
                     "<strong>f[v]</strong>. When the walk from one root runs out of reachable "
                     "vertices it restarts at the lowest-numbered undiscovered vertex, so the "
                     "tree arcs form a FOREST and not necessarily a tree.")),
            ("p", "The counter is shared across the whole forest, which is what makes the times "
                  "comparable between vertices that were never on the same walk. On `n` vertices "
                  "it ends at `2n`, always, because each vertex contributes exactly one tick when "
                  "it opens and one when it closes."),
            ("def", ("The four classes of an arc",
                     "Relative to one completed walk, an arc `(u, v)` is a "
                     "<strong>tree</strong> arc if `v` was discovered by it; a "
                     "<strong>back</strong> arc if `v` is a proper ancestor of `u` in the forest; "
                     "a <strong>forward</strong> arc if `v` is a proper descendant of `u` and the "
                     "arc is not the tree arc; and a <strong>cross</strong> arc otherwise. The "
                     "four are exhaustive and exclusive, so every arc gets exactly one label.")),
            ("p", "The definition names ancestry, and ancestry is read off the times: `v` is a "
                  "descendant of `u` exactly when `d[u] &lt; d[v]` and `f[v] &lt; f[u]`. That is "
                  "the whole of the implementation. The lab prints, for every arc, the class and "
                  "the comparison that settled it."),
            ("example", ("Eight arcs, one walk, all four classes",
                         "The lab opens on the arcs `1>2, 1>4, 2>5, 4>2, 5>4, 3>5, 3>6, 6>3` with "
                         "the walk starting at 1. The walk goes 1, 2, 5, 4, closes all four, then "
                         "restarts at 3 and reaches 6, giving `d = 1, 2, 9, 4, 3, 10` and "
                         "`f = 8, 7, 12, 5, 6, 11`. Classified from those numbers: `1>2`, `2>5`, "
                         "`5>4` and `3>6` are tree arcs; `4>2` and `6>3` are back; `1>4` is "
                         "forward, because 4 is a finished descendant of 1; and `3>5` is cross, "
                         "because `[9, 12]` and `[3, 6]` do not meet. Four, two, one and one, on "
                         "eight arcs.")),
            ("p", "Two of those deserve a second look. `1>4` is forward rather than tree because "
                  "the walk reached 4 first through 2 and 5 &mdash; the arc `1>4` was examined "
                  "later, found 4 already finished, and discovered nothing. And `3>5` is cross "
                  "although 3 and 5 are both on the same picture: the walk had closed 5 at step 6 "
                  "before it opened 3 at step 9, so neither is an ancestor of the other."),
            ("thm", ("The parenthesis theorem",
                     "For any two vertices `u` and `v` of one walk, exactly one of three things "
                     "holds: the intervals `[d[u], f[u]]` and `[d[v], f[v]]` are disjoint and "
                     "neither vertex is an ancestor of the other; `[d[v], f[v]]` lies wholly "
                     "inside `[d[u], f[u]]` and `v` is a descendant of `u`; or the reverse. The "
                     "intervals never partly overlap.")),
            ("proof", ("Suppose `d[u] &lt; d[v]`. When `v` is discovered, `u` is either still "
                       "open or already closed.",
                       "If `u` is still open then the walk reached `v` from inside `u`, so `v` is "
                       "a descendant of `u`; and the walk cannot close `u` while `v` is open, "
                       "because closing `u` means every arc out of it, and every recursive call "
                       "below it, has returned. So `f[v] &lt; f[u]` and the intervals nest.",
                       "If `u` is already closed then `f[u] &lt; d[v]`, so the intervals are "
                       "disjoint, and neither can be an ancestor of the other: an ancestor is "
                       "open for the whole of its descendant's interval. A partial overlap would "
                       "need `d[u] &lt; d[v] &lt; f[u] &lt; f[v]`, which is the first case with "
                       "`v` closing after `u`, and that case has just been ruled out.")),
            ("p", "The lab does not quote that theorem, it checks it. On the opening graph there "
                  "are 15 pairs of vertices; the panel reports that 7 of them nest, 8 are "
                  "disjoint, and 0 overlap without nesting, and it separately confirms that "
                  "nesting and descent agree on every pair. Change the graph and it recounts."),
            ("h3", "The class of an arc is a fact about the walk, not about the graph"),
            ("p", "Start the same eight arcs at vertex 3 instead of vertex 1. The times become "
                  "`d = 11, 4, 1, 3, 2, 8` and `f = 12, 5, 10, 6, 7, 9`, and the counts change: "
                  "four tree arcs and two back arcs as before, but now 0 forward arcs and 2 cross "
                  "arcs. The arc `1>4` that was forward is now cross. Move the slider in the lab "
                  "and watch the table rewrite itself."),
            ("p", "What does NOT change is the back count. It is 2 from either root, and it has "
                  "to be: a back arc means a cycle, a cycle is a property of the arcs and not of "
                  "the walk, and this graph has cycles. The lab's status line therefore reads "
                  "acyclicity off the back count alone and says nothing about the other three."),
            ("h3", "Read the same arcs undirected and two classes disappear"),
            ("p", "Switch the lab's reading to undirected and the counts for forward and cross "
                  "both come out 0, on this graph and on every graph the panel has been given. "
                  "The reason is that an undirected edge is met from whichever end the walk "
                  "reached first: if the far end is already discovered it cannot have been "
                  "finished, because the walk would have crossed this very edge and finished this "
                  "end first. So the far end is an open ancestor, which is a back edge. Forward "
                  "and cross are phenomena of direction."),
            ("p", "Finally the cost. On the opening graph the panel reports 6 vertex visits and 8 "
                  "arc reads, and those two numbers are what `Θ(V + E)` names: each vertex is "
                  "opened once and each arc is examined once from its tail. The count is for this "
                  "graph. The bound is the claim that on every graph the two figures are exactly "
                  "`V` and `E`, and it is proved by the walk's own structure &mdash; a vertex is "
                  "discovered once because discovery sets `d`, and an arc is read once because "
                  "the loop over a vertex's arcs runs once."),
        ],
        "lab": ("graphkit", {
            "mode": "dfstimes",
            "preset": "allfour",
            "panel_title": "Type a graph, then move the walk's starting point",
            "panel_intro": "The walk runs in your browser and every class is decided from the two "
                           "times at the arc's ends, never from the drawing. The parenthesis "
                           "theorem is checked on every pair of vertices rather than stated, and "
                           "the reading can be switched to undirected to watch two of the four "
                           "counts fall to zero.",
        }),
        "steps_title": "Reading a walk, rather than re-running it",
        "steps_intro": "Write the times down first. Every question after that is arithmetic on two of them.",
        "steps": [
            ("Record both times, not just the order",
             "A list of the order vertices were visited in loses the finish times, and the finish "
             "times are what every classification uses. Write the interval beside each vertex as "
             "the walk closes it."),
            ("Classify an arc from its two intervals",
             "Nested with the head inside means forward or tree; nested with the tail inside "
             "means back; disjoint means cross. Then separate tree from forward by asking which "
             "arc actually discovered the head, which is the one thing the times alone cannot "
             "tell you."),
            ("Answer the cycle question with the back count and nothing else",
             "Do not look for a cycle in the drawing and do not count the other three classes. "
             "One back arc is a cycle and no back arc is acyclicity, and both directions of that "
             "are proved, so one number settles it."),
            ("Change the root before you generalise",
             "Any claim that survives one starting vertex and not another is a claim about the "
             "walk. The lab makes this cheap: move the slider, and if the number you were about "
             "to write down moves with it, it was not a property of the graph."),
        ],
        "worked": {
            "title": "The opening graph, walked by hand",
            "intro": [
                "The arcs are `1>2, 1>4, 2>5, 4>2, 5>4, 3>5, 3>6, 6>3` and the walk starts at 1. "
                "Arcs out of a vertex are taken in the order they were typed.",
            ],
            "lines": [
                "tick  event                                   d / f written",
                "  1   open 1                                  d[1] = 1",
                "  2   1>2 discovers 2, open 2                 d[2] = 2",
                "  3   2>5 discovers 5, open 5                 d[5] = 3",
                "  4   5>4 discovers 4, open 4                 d[4] = 4",
                "  5   4>2 finds 2 open  -> BACK; close 4      f[4] = 5",
                "  6   close 5                                 f[5] = 6",
                "  7   close 2                                 f[2] = 7",
                "  8   1>4 finds 4 finished -> FORWARD; close 1  f[1] = 8",
                "  9   restart at 3, open 3                    d[3] = 9",
                " 10   3>5: [9,12] and [3,6] disjoint -> CROSS",
                " 10   3>6 discovers 6, open 6                 d[6] = 10",
                " 11   6>3 finds 3 open -> BACK; close 6       f[6] = 11",
                " 12   close 3                                 f[3] = 12",
                "",
                "intervals   1:[1,8]  2:[2,7]  3:[9,12]  4:[4,5]  5:[3,6]  6:[10,11]",
                "classes     tree 4   back 2   forward 1   cross 1        on 8 arcs",
                "pairs       15 checked:  7 nest,  8 disjoint,  0 overlap",
            ],
            "after": [
                "The forest has two roots, 1 and 3, because nothing reaches 3 from 1. That is why "
                "the definition says forest: a single walk from a single root would have left "
                "three vertices with no times at all, and the restart rule is what makes `d` and "
                "`f` total functions.",
                "Notice that tick 10 does two things. The arc `3>5` is examined and classified "
                "without the counter moving, because examining an arc that discovers nothing is "
                "not an event the counter records. Only openings and closings tick, which is why "
                "the last finish time is `2n` exactly.",
                "For a faded rehearsal, delete the arc `3>5` and predict all twelve numbers "
                "before running it. The supplied first move is this: removing `3>5` removes the "
                "only cross arc and changes no time at all, because that arc discovered nothing "
                "and the counter never moved for it. Say what the four counts become, then check "
                "them &mdash; and then delete `1>4` instead and say why that one also leaves "
                "every time alone.",
            ],
        },
        "quiz_title": "Times, classes, and what each one settles",
        "quiz": [
            {"q": "In one walk, `d[u] = 3`, `f[u] = 10`, `d[v] = 4` and `f[v] = 9`. What follows?",
             "a": ["Nothing: the intervals overlap, so the walk was wrong",
                   "`v` is a descendant of `u`",
                   "`u` is a descendant of `v`",
                   "There is an arc from `u` to `v`"],
             "c": 1,
             "why": "`[4, 9]` lies wholly inside `[3, 10]`, which by the parenthesis theorem means "
                    "`v` is a descendant of `u`. It does NOT mean there is an arc between them: "
                    "the descendant may be several tree arcs below. The intervals do not overlap "
                    "partly, they nest, and that is the only two options the theorem leaves."},
            {"q": "The lab reports 4 tree, 2 back, 1 forward and 1 cross arc. Moving the starting vertex changes the last two to 0 forward and 2 cross. Which conclusion is safe?",
             "a": ["The graph changed, so the comparison is meaningless",
                   "The back count is unreliable too, it just happened not to move",
                   "Forward and cross are properties of the walk; the back count being unchanged reflects something about the graph",
                   "The walk starting at 1 was the correct one and the other is an artefact"],
             "c": 2,
             "why": "A back arc exists in some walk if and only if the graph has a cycle, and "
                    "having a cycle does not depend on where you start &mdash; so the back count "
                    "being nonzero is stable, even though which arcs are back can move. Forward "
                    "and cross carry no such guarantee, and the lab shows one turning into the "
                    "other when the root moves."},
            {"q": "A walk on an undirected graph reports 0 forward and 0 cross edges. What has been established?",
             "a": ["That this graph happens to be a tree",
                   "Nothing, since one graph is one graph",
                   "A fact about this graph only, though the general claim is proved separately in the lesson",
                   "That the graph is connected"],
             "c": 2,
             "why": "The measurement is about the graph on screen. The general statement &mdash; "
                    "an undirected walk has no forward and no cross edges, ever &mdash; is proved "
                    "in the lesson from the fact that an edge to a discovered vertex must reach "
                    "an ancestor, and the lab agreeing on every graph tried is evidence for that "
                    "proof rather than a substitute for it."},
            {"q": "Which single number decides whether a digraph is acyclic?",
             "a": ["The number of back arcs in one completed walk",
                   "The number of cross arcs", "The number of tree arcs",
                   "The largest finish time"],
             "c": 0,
             "why": "Zero back arcs in one walk means acyclic and one or more means there is a "
                    "cycle, both proved. The tree count is `V` minus the number of roots, which "
                    "says nothing about cycles; the largest finish time is always `2V`; and the "
                    "cross count moves when the root moves."},
        ],
        "mistakes": [
            ("Treating the classification as a property of the graph",
             "Only the tree and back counts are stable in the way readers expect, and even the "
             "tree arcs change which arcs they are. The lab's root slider is there to make this "
             "cheap to check: on the opening graph, starting at 1 gives one forward arc and one "
             "cross arc, and starting at 3 gives none and two. Any sentence beginning "
             "&ldquo;the forward arcs of this graph&rdquo; is already wrong."),
            ("Hunting for a cycle in the picture",
             "The drawing is a convenience and the walk is the algorithm. A reader who looks for "
             "a loop by eye on twelve vertices will miss one, and worse, will have no procedure "
             "when the graph has fifty. One completed walk answers it with a count, and the "
             "answer is proved in both directions rather than spotted."),
            ("Reading a cross arc as evidence of a second component",
             "A cross arc only says the two intervals are disjoint. On the opening graph the arc "
             "`3>5` is cross and 5 is perfectly reachable from 3 &mdash; the walk simply finished "
             "with 5 before it ever opened 3. Reachability and ancestry in one walk's forest are "
             "different questions, and the times answer the second."),
        ],
        "standard": ("Finish when you can classify every arc of a graph you have not seen before, from the times alone.",
                     "You should be able to run the walk by hand and record both times, name the "
                     "class of an arc by comparing two intervals, say why zero back arcs settles "
                     "acyclicity while zero cross arcs settles nothing, and predict which counts "
                     "will move when the root moves."),
        "note": ("Everything in the rest of this module is these two numbers used again. "
                 "&ldquo;Topological Order&rdquo; takes the finish times in decreasing order and "
                 "gets a schedule for tasks; &ldquo;Bridges and Cut Vertices&rdquo; adds one more number per vertex "
                 "to the same walk; and &ldquo;Strongly Connected Components&rdquo; runs the walk "
                 "twice, the second time on the reversed arcs, using the first walk's finishing "
                 "order as its schedule."),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "topological-order",
        "title": "Topological Order",
        "module": "Searching a graph",
        "one_line": "Produce an order in which every task follows its prerequisites, two different ways, and count how many such orders exist.",
        "summary": (
            "An acyclic digraph can be laid out in a line so that every arc points forwards. Two "
            "algorithms produce such a line: reverse finishing order from one depth-first walk, "
            "and repeatedly removing a vertex nothing points into. They generally disagree, and "
            "both are right, because the order is usually not unique. The lab answers "
            "uniqueness with a number by enumerating every valid order there is."
        ),
        "key": [
            "topological order: every arc u to v has u before v in the line",
            "exists  <=>  the digraph is acyclic",
            "reverse finishing order of one DFS      is one valid order",
            "Kahn: repeatedly take a vertex of in-degree 0   is another",
            "unique  <=>  exactly one valid order, which is a COUNT and not a feeling",
        ],
        "key_label": "One property, two algorithms, and uniqueness as a count",
        "concepts_intro": (
            "The hard idea is that two correct algorithms disagreeing is not a bug. The other two "
            "are the existence condition and the way uniqueness is settled."
        ),
        "concepts": [
            ("The order exists exactly when there is no cycle",
             "If the vertices can be lined up with every arc pointing forwards then a cycle would "
             "have to return to a vertex already passed, which would need an arc pointing "
             "backwards. Conversely, if there is no cycle then one depth-first walk has no back "
             "arc, and listing the vertices by decreasing finish time is a valid order. So "
             "existence is not a separate question from acyclicity: it is the same question."),
            ("Two algorithms, two answers, both correct",
             "Reverse finishing order comes out of the depth-first walk at no extra "
             "cost. Kahn's method instead keeps the in-degrees, emits any vertex whose in-degree "
             "has reached 0, and decrements its successors. On the lab's opening task graph the "
             "first returns `2 1 3 5 4 6` and the second returns `1 2 3 4 5 6`. The panel checks "
             "each one arc by arc, and both pass."),
            ("Uniqueness is a count, and the lab produces it",
             "&ldquo;Is the order unique?&rdquo; has a numerical answer: how many valid orders "
             "are there. The lab enumerates them all. The opening graph has 4; a chain of five "
             "vertices has 1, which is what uniqueness looks like; a diamond has 2; five vertices "
             "with no arcs at all have 120. A graph with a cycle has 0, and the enumeration "
             "reports that as the same fact the walk reports as a back arc."),
        ],
        "read_title": "Two orders, both valid, and a number for how many there are",
        "read_intro": "The definition, the existence theorem, the two algorithms with their counts, and what the enumeration is for.",
        "body": [
            ("def", ("Topological order",
                     "A <strong>topological order</strong> of a digraph is a listing of all its "
                     "vertices such that for every arc `(u, v)`, `u` appears before `v`. A "
                     "digraph with such a listing is often drawn left to right, which makes the "
                     "condition visible: no arc points leftwards.")),
            ("thm", ("Existence",
                     "A digraph has a topological order if and only if it is acyclic.")),
            ("proof", ("If a topological order exists and `v1, v2, ..., vk, v1` is a cycle, then "
                       "each arc of the cycle forces its tail earlier than its head in the "
                       "listing, so `v1` appears strictly before itself. That is impossible, so "
                       "there is no cycle.",
                       "If the digraph is acyclic, run one depth-first walk. It has no back arc, "
                       "so for every arc `(u, v)` the head `v` is either discovered inside `u` "
                       "and finished before it, or already finished when the arc is examined. "
                       "Either way `f[v] &lt; f[u]`. Listing the vertices by decreasing `f` "
                       "therefore puts every tail before its head.")),
            ("p", "The proof is also the algorithm, which is why the first method costs nothing "
                  "beyond the walk: sort by finish time, or equivalently push each vertex onto a "
                  "stack as it closes and read the stack off. The lab reports 6 vertex visits and "
                  "6 arc reads on the opening graph, the same `Θ(V + E)` the walk itself costs."),
            ("h3", "Kahn's method, which never mentions a finish time"),
            ("ol", ["Compute the in-degree of every vertex, and put every vertex of in-degree 0 "
                    "into a queue.",
                    "Remove a vertex from the queue, emit it, and decrement the in-degree of each "
                    "of its successors.",
                    "Any successor whose in-degree has just reached 0 joins the queue.",
                    "Stop when the queue is empty. If fewer than `V` vertices were emitted, the "
                    "remaining ones lie on or below a cycle and no order exists."]),
            ("p", "On the opening graph `1>3, 2>3, 3>4, 3>5, 4>6, 5>6` the starting in-degrees "
                  "are `0, 0, 2, 1, 1, 2`, two vertices are in the queue at once, and the method "
                  "emits `1 2 3 4 5 6` with 4 queue pushes, 6 pops and 6 arc reads. The walk's "
                  "answer on the same graph is `2 1 3 5 4 6`. Both are checked arc by arc in the "
                  "panel and both pass, and the disagreement is not a defect in either."),
            ("example", ("Four valid orders, enumerated",
                         "For that graph the lab enumerates every valid order and finds 4: "
                         "`1 2 3 4 5 6`, `1 2 3 5 4 6`, `2 1 3 4 5 6` and `2 1 3 5 4 6`. Kahn's "
                         "answer is the first and the walk's answer is the last. The freedom is "
                         "exactly the two independent starts and the two independent middles, and "
                         "2 times 2 is 4.")),
            ("p", "The enumeration is a real search over all orders, not a formula, so it is "
                  "refused rather than run slowly above the size it can finish: nine vertices is "
                  "declined with a message naming the cap, and the reason is that eight vertices "
                  "with no arcs already have `8! = 40 320` orders. Where it does run, the number "
                  "it prints is a fact about every order rather than about the one produced."),
            ("h3", "Uniqueness, and what it takes"),
            ("p", "A chain of five vertices has exactly 1 valid order; a diamond has 2; five "
                  "vertices with no arcs have `5! = 120`. The chain is the shape uniqueness "
                  "needs: there must be an arc between each consecutive pair in the order, "
                  "because two vertices with no path between them can always be swapped. So "
                  "uniqueness is equivalent to the order being a Hamiltonian path of the digraph, "
                  "which is a much stronger condition than acyclicity."),
            ("p", "A cycle shows up twice, by two different mechanisms, and the lab prints both. "
                  "On `1>2, 2>3, 3>1, 3>4` the depth-first walk finds a back arc and returns no "
                  "order; Kahn's queue starts empty, because every one of the first three "
                  "vertices has in-degree 1, and it emits nothing at all. The enumeration "
                  "independently returns a count of 0. Three witnesses, one cause."),
            ("p", "The measured counts are worth putting beside the bound. Kahn's method on the "
                  "opening graph did 4 pushes, 6 pops and 6 arc reads, which is `V` pops and `E` "
                  "reads. That is `Θ(V + E)` for this graph. The bound is the claim that it is "
                  "`Θ(V + E)` for every graph, and the argument is that each vertex enters the "
                  "queue at most once &mdash; it enters when its in-degree reaches 0, and the "
                  "in-degree only ever decreases &mdash; and each arc is read exactly once, when "
                  "its tail is emitted."),
        ],
        "lab": ("graphkit", {
            "mode": "topo",
            "preset": "twoways",
            "panel_title": "Type the dependencies and compare the two orders",
            "panel_intro": "Both orders are produced in your browser and both are checked arc by "
                           "arc, so a disagreement between them is visible as two valid answers "
                           "rather than as an error. The count of valid orders is an enumeration, "
                           "not an estimate, and it is refused rather than run slowly above the "
                           "size it states.",
        }),
        "steps_title": "Getting an order, and knowing what you have",
        "steps_intro": "Produce one, check it, and only then ask whether it was the only one.",
        "steps": [
            ("Decide which algorithm you are already paying for",
             "If a depth-first walk is being run anyway, the order is free: push each vertex as "
             "it closes. If the in-degrees are already maintained, Kahn's method is free instead. "
             "Neither is better; they cost the same and produce different answers."),
            ("Check the order arc by arc, not by eye",
             "For every arc, confirm the tail's position is lower than the head's. This is `E` "
             "comparisons and it catches an off-by-one in the emission order that a drawing will "
             "not. The lab does exactly this and reports a verdict per algorithm."),
            ("Read a missing order as a cycle, and find it",
             "Neither algorithm should be made to fail silently. A walk that stops with a back "
             "arc has the cycle in hand: it is the tree path from the head down to the tail plus "
             "that arc. Kahn's method instead leaves you the set of vertices never emitted, which "
             "is everything on or downstream of a cycle."),
            ("Ask for the count before you promise uniqueness",
             "Two correct algorithms agreeing is not uniqueness; on the diamond they can agree "
             "and there are still two orders. Enumerate where the graph is small enough, and "
             "where it is not, check the much simpler equivalent condition: is there an arc "
             "between every consecutive pair of the order you produced?"),
        ],
        "worked": {
            "title": "Both algorithms on the same six tasks",
            "intro": [
                "The dependencies are `1>3, 2>3, 3>4, 3>5, 4>6, 5>6`: two things must happen "
                "before 3, then 4 and 5 may happen in either order, then 6.",
            ],
            "lines": [
                "in-degrees   1:0   2:0   3:2   4:1   5:1   6:2",
                "",
                "Kahn's method",
                "  queue [1, 2]      emit 1    3 drops to 1",
                "  queue [2]         emit 2    3 drops to 0, enters",
                "  queue [3]         emit 3    4 and 5 drop to 0, both enter",
                "  queue [4, 5]      emit 4    6 drops to 1",
                "  queue [5]         emit 5    6 drops to 0, enters",
                "  queue [6]         emit 6",
                "  order             1 2 3 4 5 6            4 pushes, 6 pops, 6 arc reads",
                "",
                "one depth-first walk, restarting where it must",
                "  open 1, open 3, open 4, open 6, close 6, close 4",
                "  from 3 open 5, 5>6 finds 6 finished, close 5, close 3, close 1",
                "  restart at 2, 2>3 finds 3 finished, close 2",
                "  decreasing finish time                   2 1 3 5 4 6",
                "",
                "every valid order, enumerated:  4",
                "  1 2 3 4 5 6     1 2 3 5 4 6     2 1 3 4 5 6     2 1 3 5 4 6",
            ],
            "after": [
                "The two answers differ in both places the graph allows them to. Kahn's emitted 1 "
                "before 2 because 1 was pushed first; the walk finished 2 last because it "
                "restarted there. Neither choice is forced by an arc, which is precisely why the "
                "enumeration finds four orders and not one.",
                "Notice what the enumeration is being used for. It is not a third algorithm for "
                "producing an order &mdash; it is far too expensive for that. It is the only way "
                "on this page to turn &ldquo;the order is not unique&rdquo; from an impression "
                "into a number, and the number is what the lesson's third concept is about.",
                "For a faded rehearsal, add the arc `4>5` and predict the new count before "
                "running it. The supplied first move is this: the only freedom left between 4 and "
                "5 is removed, so the two middle choices collapse to one while the two starting "
                "choices survive. Say what the count becomes, then add `2>1` as well and say what "
                "it becomes then.",
            ],
        },
        "quiz_title": "Orders, cycles, and counting",
        "quiz": [
            {"q": "Depth-first reverse finishing order and Kahn's method return different listings of the same acyclic digraph. What follows?",
             "a": ["One of them has a bug",
                   "The graph has more than one topological order",
                   "The graph has a cycle that one of them missed",
                   "The graph is disconnected"],
             "c": 1,
             "why": "Both algorithms are proved correct, so two different outputs means two "
                    "different valid orders exist. The lab checks each answer arc by arc and "
                    "reports both as valid, and the enumeration then says how many there are in "
                    "total &mdash; four, on the opening graph."},
            {"q": "The enumeration reports that a digraph has exactly one topological order. What does that tell you about the digraph?",
             "a": ["It is a chain: there is an arc between each consecutive pair of the order",
                   "It has no arcs",
                   "It is connected",
                   "Both algorithms will produce it, so the check was unnecessary"],
             "c": 0,
             "why": "If two consecutive vertices of the order had no arc between them they could "
                    "be swapped and the result would still be valid, giving a second order. So "
                    "uniqueness forces an arc at every consecutive position, which is a "
                    "Hamiltonian path. Connectivity follows but is much weaker, and a graph with "
                    "no arcs has `V!` orders."},
            {"q": "On a digraph with a cycle, Kahn's method emits nothing at all. Why?",
             "a": ["Because the in-degree array was computed wrongly",
                   "Because every vertex of that digraph happened to lie on the cycle, so none had in-degree 0",
                   "Because the method always fails on cyclic input before emitting anything",
                   "Because the queue is a stack in disguise"],
             "c": 1,
             "why": "The method emits every vertex not on or downstream of a cycle first, and "
                    "only then runs out. On the lab's cyclic preset all of the first three "
                    "vertices lie on the cycle and the fourth is downstream of it, so nothing "
                    "ever reaches in-degree 0 and the count emitted is zero. On a graph with a "
                    "cycle in one corner it would emit everything else."},
            {"q": "Which cost does one depth-first walk pay to produce a topological order, beyond the walk itself?",
             "a": ["A sort by finish time, costing `Θ(V log V)`",
                   "Nothing: pushing each vertex as it closes gives the reversed order directly",
                   "A second walk on the reversed arcs",
                   "An in-degree table, costing `Θ(E)`"],
             "c": 1,
             "why": "The vertices close in increasing finish time by definition, so a stack "
                    "pushed at each close pops in decreasing finish time. No comparison sort is "
                    "needed. The in-degree table belongs to the other method, and the second walk "
                    "on reversed arcs belongs to strongly connected components."},
        ],
        "mistakes": [
            ("Calling the output the topological order, with the definite article",
             "It is one of them. On the lab's opening graph there are four, and two correct "
             "algorithms produce two different ones. Any downstream code that depends on which "
             "order came back is depending on an implementation detail; the lab's count is the "
             "cheapest way to find out whether you are relying on something real."),
            ("Sorting the vertices by finish time and calling it free",
             "The vertices close in increasing finish time already, so the order is obtained by "
             "pushing at each close and reading the stack. Actually sorting a `V`-element array "
             "adds a `log V` factor to a linear algorithm for nothing. The mistake is common "
             "because the proof is naturally phrased as &ldquo;list them by decreasing `f`&rdquo;."),
            ("Reading a missing order as an error rather than as a result",
             "It is the answer to a real question: this dependency graph cannot be scheduled "
             "because something must precede itself. Both algorithms hand back the evidence "
             "&mdash; a back arc that closes a cycle, or the set of vertices never emitted "
             "&mdash; and discarding that evidence in favour of a boolean throws away the "
             "diagnosis that makes the result actionable."),
        ],
        "standard": ("Finish when you can produce both orders on a graph you have not seen, and say how many orders it has.",
                     "You should be able to run Kahn's method with the in-degree table by hand, "
                     "read a topological order off one walk's closings, check a candidate order "
                     "arc by arc, and say what uniqueness would require of the graph rather than "
                     "inferring it from two algorithms agreeing."),
        "note": ("The two algorithms here are used again separately. "
                 "&ldquo;Strongly Connected Components&rdquo; needs the finishing order and not "
                 "the in-degrees, because the order it wants is a schedule for a second walk; "
                 "&ldquo;Shortest and Longest Paths in a DAG&rdquo; needs the order itself, and "
                 "is the one place on this course where a shortest-path problem is solved in a "
                 "single pass over the arcs."),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "bridges-and-cut-vertices",
        "title": "Bridges and Cut Vertices",
        "module": "Searching a graph",
        "one_line": "Add one number per vertex to the same walk and find every edge and vertex whose removal breaks the graph apart.",
        "summary": (
            "An edge whose removal disconnects the graph is a bridge; a vertex whose removal does "
            "the same is a cut vertex. Both can be found by deleting each candidate and recounting "
            "the components, which costs a walk per candidate. One extra number per vertex "
            "&mdash; the earliest discovery time reachable from its subtree &mdash; finds all of "
            "them in a single walk, and the lab runs the slow method beside it on the graph you "
            "typed."
        ),
        "key": [
            "low[v] = min over the subtree at v of d, using at most one non-tree edge",
            "tree edge (u, v) is a BRIDGE       when low[v] > d[u]",
            "non-root u is a CUT VERTEX         when some child v has low[v] >= d[u]",
            "the root is a cut vertex           when the walk gave it two or more children",
            "exclusion is by ARC, not by endpoint: a second edge to the parent is a back edge",
        ],
        "key_label": "One extra number per vertex, and the three rules it feeds",
        "concepts_intro": (
            "The hard idea is low, and specifically what it is allowed to use. The two rules that "
            "read it, and the root's exception, follow from the definition."
        ),
        "concepts": [
            ("low[v] is the highest the subtree at v can climb",
             "Write `low[v]` for the smallest discovery time reachable from `v` by going down any "
             "number of tree edges and then along at most one non-tree edge. It is computed as "
             "`v` closes, from `d[v]`, from the `low` of each child, and from the `d` of each "
             "vertex a non-tree edge from `v` reaches. On the lab's opening graph the discovery "
             "times are `1, 2, 3, 4, 5, 6` in order and the low values come out "
             "`1, 1, 1, 4, 4, 4` &mdash; two blocks of three, and the boundary between them is "
             "the answer."),
            ("A bridge is a subtree with no way back above its own parent",
             "For a tree edge `(u, v)`, the subtree at `v` is cut off by removing that edge "
             "exactly when nothing in the subtree reaches `u` or higher by another route "
             "&mdash; that is, `low[v] &gt; d[u]`. Every non-tree edge is a back edge in an "
             "undirected walk, so &ldquo;another route&rdquo; means exactly what `low` measures. "
             "On the opening graph that fires once, at the edge between 3 and 4."),
            ("The root needs its own rule, and it is about children",
             "For a non-root `u`, a child `v` with `low[v] >= d[u]` means the subtree cannot get "
             "past `u`, so deleting `u` strands it. The root has no parent to be stranded from, "
             "so that test is vacuous; instead the root is a cut vertex exactly when the walk "
             "gave it two or more children, because a second child means a part of the graph that "
             "only the root connected. The lab ships a preset for this: on four vertices with "
             "arcs `1-2, 1-3, 2-3, 1-4` the root 1 is the only cut vertex."),
        ],
        "read_title": "One more number, and the two rules that read it",
        "read_intro": "The definitions, what low means precisely, the two tests, the root exception, and the graph the matrix check cannot be given.",
        "body": [
            ("def", ("Bridge and cut vertex",
                     "An edge of a connected undirected graph is a <strong>bridge</strong> if "
                     "deleting it leaves a graph with more components. A vertex is a "
                     "<strong>cut vertex</strong> if deleting it, and every edge at it, does the "
                     "same. Neither definition mentions an algorithm, and the slow method is a "
                     "direct transcription of them: delete, recount, restore.")),
            ("p", "That slow method costs one walk per candidate, so `Θ(E(V + E))` for the "
                  "edges. It is also completely reliable, which is why the lab runs it as an "
                  "independent answer beside the fast one rather than as a fallback. On the "
                  "opening graph both report the single bridge between 3 and 4 and the two cut "
                  "vertices 3 and 4, and the panel prints the comparison rather than the "
                  "agreement it expects."),
            ("def", ("The low-link value",
                     "For a vertex `v` of a depth-first forest on an undirected graph, "
                     "<strong>low[v]</strong> is the minimum of `d[v]`, of `low[c]` over the "
                     "children `c` of `v`, and of `d[w]` over every vertex `w` joined to `v` by a "
                     "non-tree edge. Equivalently it is the smallest discovery time reachable "
                     "from `v` using tree edges downwards and then at most one non-tree edge.")),
            ("p", "The recursive form is what makes it computable in the walk: `low[v]` is "
                  "finished exactly when `v` closes, because by then every child has closed and "
                  "every edge at `v` has been examined. So the cost is the walk's cost and "
                  "nothing more. On the opening graph the panel counts 6 vertex visits and 18 "
                  "edge reads, against `Θ(V + E)` &mdash; 18 rather than 7 because each edge is "
                  "considered from both of its ends, the adjacency index holds it at each end "
                  "both as leaving and as entering, and the one arc the walk arrived on is "
                  "skipped at every vertex but the root."),
            ("thm", ("The bridge test",
                     "Let `(u, v)` be a tree edge with `v` the child. Then `(u, v)` is a bridge "
                     "if and only if `low[v] > d[u]`.")),
            ("proof", ("Suppose `low[v] &gt; d[u]`. Every vertex in the subtree at `v` has all "
                       "its edges going either inside that subtree or upwards to a vertex "
                       "discovered no earlier than `v` &mdash; if any went to something "
                       "discovered before `u` or to `u` itself, `low[v]` would be at most "
                       "`d[u]`. So the only edge leaving the subtree is `(u, v)`, and deleting it "
                       "separates the subtree from the rest.",
                       "Conversely, suppose `low[v] &le; d[u]`. Then some vertex `x` in the "
                       "subtree at `v` has a non-tree edge to a vertex discovered at or before "
                       "`u`, which in an undirected walk means an ancestor of `v` at or above "
                       "`u`. The tree path from `v` down to `x`, that edge, and the tree path "
                       "back down to `v` form a cycle through `(u, v)`, and no edge on a cycle is "
                       "a bridge.")),
            ("example", ("Two triangles joined by one edge",
                         "The lab opens on `1-2, 2-3, 3-1, 3-4, 4-5, 5-6, 6-4`. The walk "
                         "discovers the vertices in order, so `d` is `1, 2, 3, 4, 5, 6`, and the "
                         "low values are `1, 1, 1, 4, 4, 4`. The tree edge from 3 to 4 has "
                         "`low[4] = 4 > d[3] = 3`, so it is a bridge; every other tree edge fails "
                         "the test because its child sits on a triangle and can climb back. Cut "
                         "vertices: 3, because its child 4 has `low[4] >= d[3]`, and 4, because "
                         "its child 5 has `low[5] = 4 >= d[4] = 4`. Delete-and-recount returns "
                         "the same three answers.")),
            ("h3", "The two tests are nearly the same and differ by one comparison"),
            ("p", "The bridge test is `low[v] &gt; d[u]` and the cut-vertex test is "
                  "`low[v] >= d[u]`. Equality is the case where the subtree can climb back to `u` "
                  "itself but no higher: then the edge `(u, v)` lies on a cycle and is not a "
                  "bridge, while `u` is still the only way in and out, so `u` is a cut vertex. "
                  "The lab's opening graph has both endpoints of its bridge as cut vertices; its "
                  "path preset has four bridges and three cut vertices, because the two ends of a "
                  "path are on a bridge without being cut vertices."),
            ("p", "And in the other direction, a cut vertex need not be on a bridge at all. Two "
                  "triangles sharing a single vertex have that vertex as a cut vertex and no "
                  "bridge anywhere, because every edge is on a triangle. Neither concept implies "
                  "the other, and a reader who has only seen the opening graph will believe they "
                  "come in pairs."),
            ("h3", "Exclusion is by arc, and that is not a technicality"),
            ("p", "The walk must not follow the edge it arrived on, and the way to enforce that "
                  "is to remember the EDGE and not the parent vertex. With two edges between the "
                  "same pair, remembering the parent vertex would ignore both, and the graph "
                  "would be reported as having a bridge that it does not have. The lab ships this "
                  "as a preset: on `1-2, 1-2, 2-3` the only bridge is the one between 2 and 3, "
                  "whereas with a single edge between 1 and 2 the same three vertices give two "
                  "bridges."),
            ("p", "That preset is also where the independent check stops. The delete-and-recount "
                  "oracle works on an adjacency matrix, which holds one entry per pair of "
                  "vertices and therefore cannot represent two edges between the same pair at "
                  "all. The panel says so, in those words, rather than comparing against a "
                  "different graph and reporting agreement. A checker that quietly answers a "
                  "question you did not ask is worse than one that declines."),
            ("p", "Put the two figures side by side one last time. On the opening graph: 6 visits "
                  "and 18 reads for the one-pass method, against a delete-and-recount that runs a "
                  "fresh traversal for each of the 7 edges. Those are measurements on that graph. "
                  "The bound is that the one-pass method is `Θ(V + E)` on every graph, and the "
                  "reason is that `low` is completed at the moment a vertex closes, so no vertex "
                  "and no edge is revisited."),
        ],
        "lab": ("graphkit", {
            "mode": "lowlink",
            "preset": "twoblocks",
            "panel_title": "Type the graph, then try to break the rules",
            "panel_intro": "The low-links come from one depth-first pass. The bridges and cut "
                           "vertices are then found again the slow way &mdash; delete each edge, "
                           "recount the components &mdash; and the two answers are compared in "
                           "front of you. Type two edges between the same pair and the slow "
                           "method declines rather than answering about another graph.",
        }),
        "steps_title": "Finding the weak points of a graph",
        "steps_intro": "Compute d on the way down and low on the way back up; then read the two rules.",
        "steps": [
            ("Write d as you descend and low as you return",
             "`d[v]` is fixed the moment `v` is reached. `low[v]` is not fixed until `v` closes, "
             "because it takes the minimum over children that have not been explored yet. "
             "Recording low too early is the single commonest way to get this wrong by hand."),
            ("Fold in three things, and only three",
             "`d[v]` itself, `low[c]` for each child `c`, and `d[w]` for each non-tree edge to "
             "`w`. Note the asymmetry: a child contributes its `low`, but a back edge contributes "
             "the other end's `d`. Using `low[w]` for a back edge is wrong and produces values "
             "that are too small, which hides bridges."),
            ("Apply the two tests, and remember the root is different",
             "Strictly greater for a bridge, greater or equal for a cut vertex, and for the root "
             "of each tree in the forest, count its children instead. The lab's root preset "
             "exists because this exception is the one readers drop."),
            ("Check against deletion on something small",
             "Delete an edge, recount the components, restore it. It is the definition, it is "
             "cheap on a graph you can draw, and it is what the panel runs beside the fast "
             "method. Where the two disagree, the fast one is the one to distrust."),
        ],
        "worked": {
            "title": "Two triangles, one bridge, and the low values that find it",
            "intro": [
                "The graph is `1-2, 2-3, 3-1, 3-4, 4-5, 5-6, 6-4`. The walk starts at 1 and takes "
                "the edges at each vertex in the order they were typed.",
            ],
            "lines": [
                "vertex   d    low    why low is that",
                "  1      1     1     its own d; nothing climbs above it",
                "  2      2     1     back edge from the subtree reaches d = 1",
                "  3      3     1     child 2's low is 1                      (walk: 1 - 2 - 3)",
                "  4      4     4     its own d; the subtree at 4 never leaves 4, 5, 6",
                "  5      5     4     back edge 6 - 4 reaches d = 4",
                "  6      6     4     its own back edge to 4",
                "",
                "bridge test on each tree edge, child first",
                "  (1, 2)   low[2] = 1  >  d[1] = 1 ?   no",
                "  (2, 3)   low[3] = 1  >  d[2] = 2 ?   no",
                "  (3, 4)   low[4] = 4  >  d[3] = 3 ?   YES   -> bridge",
                "  (4, 5)   low[5] = 4  >  d[4] = 4 ?   no",
                "  (5, 6)   low[6] = 4  >  d[5] = 5 ?   no",
                "",
                "cut-vertex test, same numbers with >=",
                "  3 has child 4 with low[4] = 4 >= d[3] = 3   -> cut vertex",
                "  4 has child 5 with low[5] = 4 >= d[4] = 4   -> cut vertex",
                "  1 is the root and has one child             -> not a cut vertex",
                "",
                "delete and recount:  1 bridge, cut vertices 3 and 4        agrees",
            ],
            "after": [
                "Look at the pair `(4, 5)`. Its low value equals `d[4]` exactly, so it fails the "
                "bridge test by one and passes the cut-vertex test by nothing. That is the whole "
                "difference between the two rules, and it is why the same walk answers both "
                "questions without a second pass.",
                "Look also at vertex 1. The walk gave it one child, so the root rule does not "
                "fire; but if the walk had started at 3 instead, the root would have had two "
                "children and would have been reported as a cut vertex &mdash; which it is. The "
                "answer does not depend on the root, but which rule produces it does.",
                "For a faded rehearsal, add the edge `1-5` and predict the new bridges and cut "
                "vertices before running it. The supplied first move is this: the new edge gives "
                "the subtree at 4 a way back to `d = 1`, so `low[4]` falls from 4 to 1. Say what "
                "that does to the bridge test at `(3, 4)`, and then say which cut vertices "
                "survive.",
            ],
        },
        "quiz_title": "Low values, and the two rules",
        "quiz": [
            {"q": "A tree edge `(u, v)` with `v` the child has `low[v] = d[u]` exactly. What is true?",
             "a": ["It is a bridge and `u` is a cut vertex",
                   "It is not a bridge, but `u` is a cut vertex",
                   "It is a bridge, but `u` is not a cut vertex",
                   "Neither: equality means the subtree escapes above `u`"],
             "c": 1,
             "why": "The bridge test is strict and fails at equality, because the subtree reaches "
                    "`u` by another route, putting the edge on a cycle. The cut-vertex test is "
                    "not strict and fires, because reaching `u` is not the same as getting past "
                    "`u`: delete `u` and the subtree is stranded."},
            {"q": "Computing low, a reader folds in `low[w]` for a back edge to `w` instead of `d[w]`. What goes wrong?",
             "a": ["Nothing: for a back edge the two are equal",
                   "The values come out too large and phantom bridges appear",
                   "The values come out too small and real bridges are missed",
                   "The walk no longer terminates"],
             "c": 2,
             "why": "`low[w] &le; d[w]` always, so substituting it can only lower the value. A "
                    "lowered `low[v]` fails the strict test `low[v] &gt; d[u]` more often, so "
                    "edges that are bridges are reported as not being bridges. The claim that the "
                    "two are equal for a back edge is false: `w` is an ancestor, and its own low "
                    "may reach far above it."},
            {"q": "A graph is typed with two edges between the same pair of vertices. What does the lab's independent check do?",
             "a": ["Compares against the same graph with one of the two edges dropped",
                   "Reports that a matrix cannot represent the graph, and declines",
                   "Reports a disagreement between the two methods",
                   "Treats the pair as a bridge, since both edges join the same vertices"],
             "c": 1,
             "why": "The oracle is built on an adjacency matrix, which has one entry per pair and "
                    "cannot hold two edges between one pair. Comparing against the single-edge "
                    "version would answer a different question and report agreement or "
                    "disagreement about a graph the reader did not type, so the panel declines "
                    "and says why."},
            {"q": "Which of these is possible?",
             "a": ["A connected graph with a cut vertex and no bridge",
                   "A connected graph with a bridge and no cut vertex, on four or more vertices",
                   "A cut vertex that is not an endpoint of some bridge, never",
                   "A bridge whose two endpoints are both non-cut vertices, on four or more vertices"],
             "c": 0,
             "why": "Two triangles sharing one vertex have that shared vertex as a cut vertex "
                    "while every edge lies on a triangle, so there is no bridge. The other three "
                    "are false: on four or more vertices a bridge has at least one endpoint with "
                    "another edge, and that endpoint is a cut vertex."},
        ],
        "mistakes": [
            ("Excluding the parent by vertex rather than by edge",
             "With two edges between the same pair, skipping every edge to the parent vertex "
             "skips both, and the second one &mdash; which is a genuine back edge and puts the "
             "pair on a cycle &mdash; never contributes to `low`. The result is a reported bridge "
             "that is not one. The lab's parallel preset is exactly this case, and it is also the "
             "graph the matrix-based check has to decline."),
            ("Finalising low on the way down",
             "`low[v]` takes a minimum over the low values of `v`'s children, and those do not "
             "exist until the children have closed. Anyone computing it as the walk descends is "
             "computing something else &mdash; usually the minimum over back edges at `v` alone "
             "&mdash; and that value is too large, which manufactures bridges."),
            ("Assuming bridges and cut vertices come in pairs",
             "They are different properties with different tests and the strictness of one "
             "comparison between them. A path has every interior vertex as a cut vertex and every "
             "edge as a bridge; two triangles sharing a vertex have a cut vertex and no bridges; "
             "the two ends of any bridge on a long path are on a bridge without being cut "
             "vertices. Run the lab's path and cycle presets before believing either implication."),
        ],
        "standard": ("Finish when you can compute every low value by hand and read both answers off them.",
                     "You should be able to run the walk recording `d` on the way down and `low` "
                     "on the way back, apply the strict test for bridges and the non-strict one "
                     "for cut vertices, remember the root's own rule, and say why the parent must "
                     "be excluded by edge rather than by vertex."),
        "note": ("This is the second use of one walk and it will not be the last. "
                 "&ldquo;Strongly Connected Components&rdquo; asks the directed version of the "
                 "same question &mdash; which vertices can reach each other &mdash; and the "
                 "answer needs two walks rather than one extra number, because in a digraph "
                 "reaching and being reached are different relations."),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "strongly-connected-components",
        "title": "Strongly Connected Components",
        "module": "Searching a graph",
        "one_line": "Partition a digraph into the groups whose members can all reach each other, in two walks, and collapse it to something acyclic.",
        "summary": (
            "Two vertices of a digraph are in the same strongly connected component when each can "
            "reach the other. That is an equivalence relation, so it partitions the vertices, and "
            "the partition can be computed from two depth-first walks: one on the graph to get a "
            "finishing order, and one on the reversed arcs taking the vertices in that order. "
            "Collapsing each component to a point always gives an acyclic digraph, which is what "
            "the whole construction is for."
        ),
        "key": [
            "u ~ v   when u reaches v and v reaches u        an equivalence relation",
            "pass 1  depth-first walk on G, record finishing times",
            "pass 2  walk the REVERSED arcs, vertices in decreasing finish order",
            "each tree of pass 2 is one component",
            "the condensation, one point per component, is always acyclic",
        ],
        "key_label": "One relation, two passes, and an acyclic quotient",
        "concepts_intro": (
            "The hard idea is why the second pass runs on the reversed arcs. The relation and the "
            "condensation are the setup for it."
        ),
        "concepts": [
            ("Mutual reachability partitions the vertices",
             "Write `u ~ v` when there is a path from `u` to `v` and a path from `v` to `u`. It "
             "is reflexive by the empty path, symmetric by its own statement, and transitive by "
             "concatenating paths, so it is an equivalence relation and its classes partition the "
             "vertices. The lab computes those classes twice: once by the two-pass algorithm and "
             "once straight from the definition, by testing reachability from every vertex to "
             "every other, and compares the two partitions."),
            ("The condensation is acyclic, always",
             "Collapse each component to a single point and keep an arc between two points when "
             "some arc ran between their components. The result cannot have a cycle: a cycle "
             "among components would make every vertex on it mutually reachable with every other, "
             "so they would all have been one component. On the lab's opening graph the seven "
             "vertices collapse to three points joined in a line, and the panel reports the "
             "condensation acyclic rather than assuming it."),
            ("The finishing order names a source, which is why the second pass reverses",
             "The vertex that finishes last in the first walk lies in a component that nothing "
             "points into &mdash; a source of the condensation. Walking forwards from there would "
             "reach everything downstream and swallow several components at once. Walking the "
             "REVERSED arcs from there reaches exactly its own component, because the arcs into "
             "the component became arcs out of it and lead nowhere in the reversed graph. The lab "
             "checks the claim by reporting the in-degree of that component in the condensation, "
             "and it is 0."),
        ],
        "read_title": "Two passes, and why the second one runs backwards",
        "read_intro": "The relation, the algorithm, the reason the reversal is necessary rather than convenient, and the independent check.",
        "body": [
            ("def", ("Strongly connected component",
                     "A <strong>strongly connected component</strong> of a digraph is a maximal "
                     "set of vertices in which every vertex reaches every other. Maximal matters: "
                     "a single vertex is always mutually reachable with itself, so without "
                     "maximality every vertex would be its own component and the definition would "
                     "say nothing.")),
            ("p", "The classes of the relation are those maximal sets, so nothing further has to "
                  "be checked: partition and maximality come together. The brute-force method is "
                  "the definition made mechanical &mdash; compute reachability from every vertex, "
                  "then group `u` with `v` when each appears in the other's set &mdash; and that "
                  "is what the lab runs beside the fast method."),
            ("h3", "The algorithm, in two passes"),
            ("ol", ["Run a depth-first walk on the digraph, restarting as needed, and record the "
                    "finish time of every vertex.",
                    "Reverse every arc.",
                    "Walk the reversed digraph, starting each new tree at the undiscovered vertex "
                    "with the largest finish time from the first pass.",
                    "The vertex set of each tree in the second pass is one component."]),
            ("p", "Nothing about step 3 is arbitrary and everything about it is fragile. Taking "
                  "the vertices in increasing finish order, or walking the original arcs in the "
                  "second pass, both produce something &mdash; a partition of the vertices "
                  "&mdash; and neither produces the components. The lab's independent check is "
                  "the only thing on the page that can tell the difference."),
            ("thm", ("The last vertex to finish is in a source component",
                     "Let `v` have the largest finish time of a depth-first walk on a digraph. "
                     "Then the component containing `v` has in-degree 0 in the condensation: no "
                     "arc enters it from another component.")),
            ("proof", ("Suppose an arc ran from a component `B` into the component `A` of `v`, "
                       "and let `b` be its tail. Since the condensation is acyclic, no path "
                       "returns from `A` to `B`.",
                       "Consider which of `A` and `B` the walk enters first. If it enters `B` "
                       "first, then from inside `b` it can reach `A` along that arc, so every "
                       "vertex of `A` is discovered inside the call at `b` and finishes before "
                       "it, making `f[b] &gt; f[v]`. If it enters `A` first, then it cannot reach "
                       "`B` at all from `A`, so `B` is untouched while `A` finishes, and `b` is "
                       "discovered afterwards, again giving `f[b] &gt; f[v]`.",
                       "Either way something finishes later than `v`, contradicting the choice of "
                       "`v`. So no such arc exists.")),
            ("p", "That theorem is the whole design. Standing in a source component and following "
                  "the reversed arcs, everything reachable is inside the component: the reversed "
                  "arcs that would take you out of it are the forward arcs that came in, and "
                  "there are none. So the second pass's first tree is exactly one component. "
                  "Remove it and the remaining condensation still has the same property, so the "
                  "argument repeats."),
            ("example", ("Seven vertices, three components",
                         "The lab opens on `1>2, 2>3, 3>1, 3>4, 4>5, 5>6, 6>4, 5>7`. The first "
                         "walk finishes the vertices in the order that makes the decreasing list "
                         "`1 2 3 4 5 7 6`. The second pass, on the reversed arcs, produces the "
                         "components `{1, 2, 3}`, `{4, 5, 6}` and `{7}`. The condensation has "
                         "three points and two arcs, in a line, and is acyclic. Mutual "
                         "reachability computed from the definition returns the same three sets, "
                         "and the panel prints both partitions.")),
            ("p", "Two things in that example are easy to misread. The vertex 7 is its own "
                  "component not because it is isolated &mdash; 5 points at it &mdash; but "
                  "because nothing comes back from it. And the decreasing finish list puts 7 "
                  "before 6 even though 6 is lower-numbered, because the walk reached 6 first "
                  "from 5 and closed it before it ever opened 7."),
            ("h3", "The cases at the two ends"),
            ("p", "A single cycle through every vertex is one component: on `1>2, 2>3, 3>4, 4>1` "
                  "the lab reports one component of four vertices, and a condensation that is a "
                  "single point with no arcs. An acyclic digraph is the other extreme: on "
                  "`1>2, 2>3, 1>3, 3>4` every vertex is its own component, there are four of "
                  "them, and the condensation is the graph itself. Those are the two cases where "
                  "the second pass has the least to do, and running them is the fastest way to "
                  "convince yourself the algorithm is not doing something else."),
            ("p", "The counts, beside the bound. On the opening graph the second pass reports 7 "
                  "vertex visits and 8 arc reads; on the four-vertex cycle, 4 and 4; on the "
                  "acyclic preset, 4 and 4. Each is `V` and `E` for that graph. The bound is that "
                  "the whole algorithm is `Θ(V + E)`, and it is two walks plus a reversal: the "
                  "reversal itself is one pass over the arcs, and neither walk visits a vertex "
                  "twice. What the measurement cannot show is that no input makes it worse, and "
                  "that is what the argument is for."),
        ],
        "lab": ("graphkit", {
            "mode": "scc",
            "preset": "three",
            "panel_title": "Type the arcs; direction is the whole point",
            "panel_intro": "Both passes run in your browser, and the partition they produce is "
                           "compared with the one you get straight from the definition &mdash; "
                           "each vertex reaching each other. The condensation is built from the "
                           "components and checked for a cycle rather than assumed to have none.",
        }),
        "steps_title": "Running the two passes by hand",
        "steps_intro": "The first pass produces a schedule. The second pass consumes it, backwards.",
        "steps": [
            ("Do the first pass for the finish times only",
             "Nothing else from that walk is used &mdash; not its forest, not its edge classes. "
             "Record the closing order and then put the walk aside; the list of vertices in "
             "decreasing finish time is the only output the second pass reads."),
            ("Reverse the arcs before you start the second pass",
             "Reversing is `Θ(E)` and doing it lazily, by scanning for arcs that point at the "
             "current vertex, turns a linear algorithm into a quadratic one. Build the reversed "
             "arc list once."),
            ("Take the next start from the schedule, never from the numbering",
             "Each new tree of the second pass begins at the undiscovered vertex that finished "
             "LATEST in the first pass. Falling back on the lowest-numbered undiscovered vertex "
             "is the single change that quietly breaks this algorithm: it still terminates, still "
             "partitions the vertices, and no longer computes components."),
            ("Build the condensation and check it for a cycle",
             "It is `Θ(E)` and it is the thing most downstream work actually wants. If it has a "
             "cycle, the components are wrong &mdash; that check is free and it catches the "
             "previous step having gone astray."),
        ],
        "worked": {
            "title": "Seven vertices, both passes",
            "intro": [
                "The arcs are `1>2, 2>3, 3>1, 3>4, 4>5, 5>6, 6>4, 5>7`. Arcs out of a vertex are "
                "taken in the order they were typed.",
            ],
            "lines": [
                "pass 1, on the arcs as typed",
                "  open 1, 2, 3; 3>1 is a back arc",
                "  from 3 open 4, 5; then 5>6 opens 6, whose 6>4 is a back arc; close 6",
                "  then 5>7 opens 7; close 7, 5, 4, 3, 2, 1",
                "  finishing order, latest first      1  2  3  4  5  7  6",
                "",
                "reverse every arc",
                "  2>1, 3>2, 1>3, 4>3, 5>4, 6>5, 4>6, 7>5",
                "",
                "pass 2, taking starts from the list above",
                "  start 1   reaches 3 (via 1>3) and 2 (via 3>2)     component {1, 2, 3}",
                "  next undiscovered in the list is 4",
                "  start 4   reaches 6 (via 4>6) and 5 (via 6>5)     component {4, 5, 6}",
                "            4>3 leads to a vertex already taken, and stops there",
                "  next undiscovered in the list is 7",
                "  start 7   7>5 leads to a vertex already taken     component {7}",
                "",
                "condensation   {1,2,3} -> {4,5,6} -> {7}        3 points, 2 arcs, acyclic",
                "mutual reachability, computed from the definition: same three sets",
            ],
            "after": [
                "Watch what the reversal bought at the very first step. Walking forwards from 1 "
                "would have reached all seven vertices and returned one component. Walking "
                "backwards from 1 reached exactly three, because the arc `3>4`, which is the only "
                "way out of that component, became `4>3` and points inwards.",
                "Watch also the start at 4. In the reversed graph the arc `4>3` exists and leads "
                "straight into a finished component; the walk simply finds 3 already discovered "
                "and stops, which is why no special handling is needed for arcs between "
                "components. The schedule guarantees that any component reached this way is "
                "already complete.",
                "For a faded rehearsal, add the arc `7>5` to the original graph and predict the "
                "new components before running it. The supplied first move is this: 5 already "
                "reaches 7, so the new arc makes 5 and 7 mutually reachable, and 7 joins whatever "
                "5 is in. Say what the three components become, how many points the condensation "
                "then has, and whether it is still acyclic.",
            ],
        },
        "quiz_title": "Components, order, and reversal",
        "quiz": [
            {"q": "The second pass is run on the original arcs instead of the reversed ones, with the same schedule. What happens?",
             "a": ["Exactly the same components, since reachability is symmetric within a component",
                   "It crashes on the first arc leaving a component",
                   "It returns a partition, but the first tree swallows every component downstream of the source",
                   "It returns each vertex as its own component"],
             "c": 2,
             "why": "The schedule starts in a source component, and walking forwards from a "
                    "source reaches everything it points at. The result is still a partition of "
                    "the vertices, still produced without error, and not the components &mdash; "
                    "which is why the lab's independent check from the definition is the only "
                    "thing that catches it."},
            {"q": "The condensation of some digraph is computed and found to contain a cycle. What does that establish?",
             "a": ["That the digraph had a cycle",
                   "That two components should have been one, so the components are wrong",
                   "Nothing: condensations may have cycles",
                   "That the digraph is strongly connected"],
             "c": 1,
             "why": "A cycle among components would make every vertex on it mutually reachable "
                    "with every other, so maximality would have merged them. The condensation of "
                    "a correct partition is always acyclic, which makes checking it a free test "
                    "of the algorithm's output. That the digraph itself has cycles is expected "
                    "and says nothing."},
            {"q": "In a digraph, vertex 5 has an arc to vertex 7 and there is no path from 7 back to 5. Which is true?",
             "a": ["7 is isolated", "5 and 7 are in different components",
                   "7 is in a source component of the condensation",
                   "5 and 7 are in the same component, since one reaches the other"],
             "c": 1,
             "why": "Mutual reachability needs both directions, and only one holds, so they lie "
                    "in different components. 7 is not isolated &mdash; an arc reaches it "
                    "&mdash; and it is in a component with an arc coming in, so it is not a "
                    "source. This is exactly vertex 7 on the lab's opening graph."},
            {"q": "Why does the algorithm need the finishing times of the first pass rather than just any listing of the vertices?",
             "a": ["Because the reversal would otherwise be wrong",
                   "Because the largest finish time is guaranteed to lie in a component nothing points into",
                   "Because the finishing order is the topological order of the condensation, which is needed for its own sake",
                   "It does not: any listing works as long as the arcs are reversed"],
             "c": 1,
             "why": "The proof on this page is exactly that: the last vertex to finish lies in a "
                    "source component, which is what makes the first reversed tree be one "
                    "component. An arbitrary listing might start in the middle of the "
                    "condensation, where the reversed walk escapes upstream and merges "
                    "components."},
        ],
        "mistakes": [
            ("Starting the second pass at the lowest-numbered undiscovered vertex",
             "It is the default in every other traversal on this course, it terminates, it "
             "partitions the vertices, and it is wrong. Nothing about the output looks broken "
             "&mdash; the sets are disjoint and cover everything &mdash; which is why the lab "
             "computes the partition a second time from the definition rather than trusting the "
             "algorithm it is demonstrating."),
            ("Reading a one-way arc as membership",
             "An arc from `u` to `v` says `u` reaches `v` and nothing else. On the lab's opening "
             "graph, 5 points at 7 and 7 is still its own component. Strong connectivity is the "
             "conjunction of two reachability facts, and half of a conjunction is not weak "
             "evidence for it, it is no evidence at all."),
            ("Believing the condensation is acyclic because the lesson said so",
             "It is proved, and it is also checked on every graph the panel is given, because the "
             "proof is about correct components and a cycle in the condensation is the signature "
             "of incorrect ones. Treat the check as a test of the run rather than as a "
             "restatement of the theorem, and it earns its cost."),
        ],
        "standard": ("Finish when you can run both passes by hand on a graph you have not seen and say why the second one reverses.",
                     "You should be able to produce the finishing order from the first walk, "
                     "reverse the arcs, take the starts from the schedule rather than from the "
                     "numbering, build the condensation, and state the theorem about the "
                     "last-finishing vertex that makes the whole thing work."),
        "note": ("This is the last lesson built on one traversal. The next module keeps the "
                 "graph and adds weights, and the question changes from what is reachable to what "
                 "is cheapest: &ldquo;The Cut Property&rdquo; is the single lemma every minimum "
                 "spanning tree algorithm is an instance of, and it is proved there against an "
                 "enumeration of every spanning tree the graph has."),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "the-cut-property",
        "title": "The Cut Property",
        "module": "Minimum spanning trees",
        "one_line": "Prove the one lemma both minimum-tree algorithms rest on, against an enumeration of every spanning tree the graph has.",
        "summary": (
            "Split the vertices into two sides. Among the edges with one end on each side, the "
            "lightest is in some minimum spanning tree, and if it is strictly lightest it is in "
            "every one. That single lemma justifies every edge either algorithm in this module "
            "takes. The lab does not quote it: it enumerates every spanning tree of the graph you "
            "typed and reads the verdict off the list."
        ),
        "key": [
            "a cut is a split of the vertices into S and its complement",
            "crossing edges: one end in S, the other outside",
            "cut property   the lightest crossing edge is in SOME minimum spanning tree",
            "               and if it is strictly lightest, in EVERY one",
            "cycle property the strictly heaviest edge on a cycle is in NO minimum spanning tree",
        ],
        "key_label": "One split, two lemmas, and the difference between some and every",
        "concepts_intro": (
            "The hard idea is the exchange argument. The two lemmas are two readings of it, and "
            "the gap between some and every is where ties live."
        ),
        "concepts": [
            ("A cut is a question you ask of a graph",
             "Choose any set `S` of vertices, not empty and not everything. The edges with "
             "exactly one end in `S` are the crossing edges, and the cut property is a statement "
             "about the lightest of them. Nothing requires `S` to be connected, or to be half the "
             "graph, or to have anything to do with an algorithm &mdash; which is exactly why one "
             "lemma covers two algorithms that choose their cuts in completely different ways."),
            ("The proof is an exchange, and it is three lines",
             "Take a minimum spanning tree that does not contain the lightest crossing edge `e`. "
             "Adding `e` to it makes exactly one cycle, and that cycle must cross the cut a "
             "second time, at some other crossing edge `g`. Remove `g`. The result is a spanning "
             "tree again, and its weight changed by the weight of `e` minus the weight of `g`, "
             "which is at most 0. So it is also minimum, and it contains `e`."),
            ("Some and every differ exactly at a tie",
             "If `e` is strictly lighter than every other crossing edge then the exchange "
             "strictly reduces the weight, which is impossible for a minimum tree, so every "
             "minimum tree already contained `e`. With a tie the exchange is weight-neutral and "
             "only produces one tree containing `e`. The lab measures the difference: on the "
             "opening graph, whose weights are all distinct, the lightest crossing edge is in the "
             "one minimum tree there is. On a triangle with all three weights equal there are 3 "
             "spanning trees, all 3 minimum, and the lightest crossing edge is in 2 of them."),
        ],
        "read_title": "One lemma, its proof, and the enumeration that checks it",
        "read_intro": "Cuts and crossing edges, the exchange argument, the cycle property as the same picture read backwards, and what the lab enumerates.",
        "body": [
            ("def", ("Cut, crossing edge, spanning tree",
                     "A <strong>cut</strong> of a graph is a partition of its vertices into a "
                     "non-empty proper subset `S` and the rest. An edge <strong>crosses</strong> "
                     "the cut if exactly one of its ends lies in `S`. A <strong>spanning "
                     "tree</strong> is a subset of the edges that connects every vertex and "
                     "contains no cycle; on a connected graph with `V` vertices it has exactly "
                     "`V - 1` edges. A <strong>minimum</strong> spanning tree is one of least "
                     "total weight; there may be several.")),
            ("thm", ("The cut property",
                     "Let `S` be one side of a cut of a connected weighted graph, and let `e` be "
                     "a crossing edge of least weight. Then some minimum spanning tree contains "
                     "`e`. If `e` is the unique crossing edge of least weight, then every minimum "
                     "spanning tree contains it.")),
            ("proof", ("Let `T` be a minimum spanning tree with `e` not in it, and write `e` as "
                       "joining `x` in `S` to `y` outside it. `T` connects `x` to `y`, so adding "
                       "`e` creates exactly one cycle, consisting of `e` and the tree path from "
                       "`y` back to `x`.",
                       "That tree path starts outside `S` and ends inside it, so it contains at "
                       "least one crossing edge; call one of them `g`. Then `T` with `e` added "
                       "and `g` removed is connected &mdash; removing an edge of a cycle cannot "
                       "disconnect anything &mdash; and has `V - 1` edges, so it is a spanning "
                       "tree.",
                       "Its weight is `w(T) + w(e) - w(g)`, and `w(e) &le; w(g)` because `e` is a "
                       "lightest crossing edge. So the new tree weighs at most `w(T)`, and since "
                       "`T` was minimum it weighs exactly `w(T)` and is minimum too. That gives "
                       "the first claim. For the second, if `e` is strictly lightest then "
                       "`w(e) &lt; w(g)` and the new tree would weigh strictly less than `T`, "
                       "which is impossible &mdash; so no minimum tree can have omitted `e`.")),
            ("p", "The lab is built to make that proof checkable rather than believable. Give it "
                  "a graph of at most seven vertices and it enumerates every spanning tree, "
                  "totals each one, and reports how many are minimum and how many of them contain "
                  "the lightest crossing edge. The verdict comes off the list."),
            ("example", ("Six vertices, one cut, eight spanning trees",
                         "The lab opens on `1-2 4, 1-3 3, 2-3 2, 2-4 5, 3-4 7, 4-5 1, 5-6 6` with "
                         "`S = {1, 2, 3}`. Two edges cross: `2-4` at weight 5 and `3-4` at weight "
                         "7, so the lightest crossing edge is `2-4`. The enumeration finds 8 "
                         "spanning trees in total, exactly 1 of them minimum, at weight 17; that "
                         "tree is `1-3`, `2-3`, `2-4`, `4-5`, `5-6`, and it contains `2-4`. "
                         "Kruskal's method on the same graph also returns 17.")),
            ("p", "That graph has distinct weights, so the minimum tree is unique and the "
                  "distinction between some and every collapses. Sweeping every one of the 62 "
                  "proper cuts of those six vertices, the lightest crossing edge is in a minimum "
                  "tree every time, and where it is strictly lightest it is in all of them."),
            ("h3", "Where the two halves of the lemma come apart"),
            ("p", "Type a triangle with all three weights equal &mdash; `1-2 1, 2-3 1, 3-1 1` "
                  "&mdash; and take `S = {1}`. Two edges cross, tied at weight 1. There are 3 "
                  "spanning trees, all 3 minimum at weight 2, and each edge is in exactly 2 of "
                  "them. So the lightest crossing edge is in SOME minimum tree and not in every "
                  "one, and the panel reports the some-verdict as yes and the every-verdict as "
                  "no, with the tie count beside it. That is the whole content of the second "
                  "sentence of the theorem."),
            ("h3", "The same picture, read the other way"),
            ("thm", ("The cycle property",
                     "If an edge is the unique heaviest edge on some cycle of the graph, then no "
                     "minimum spanning tree contains it.")),
            ("p", "The argument is the exchange run backwards: a minimum tree containing that "
                  "edge, with the edge removed, splits into two pieces, and the rest of the cycle "
                  "must rejoin them with some strictly lighter edge, giving a lighter tree. The "
                  "lab prints the per-edge count that settles this. On `1-2 1, 2-3 2, 3-4 3, "
                  "4-1 9, 2-4 4` there are 8 spanning trees, 1 of them minimum at weight 6, and "
                  "two edges appear in none of the minimum trees: `4-1` at weight 9 and `2-4` at "
                  "weight 4. The second is the interesting one &mdash; it is not the heaviest "
                  "edge in the graph, it is the heaviest on the cycle 2, 3, 4."),
            ("h3", "Two things the lemma does not say"),
            ("p", "It does not say that taking the lightest edge at each vertex builds a tree. On "
                  "`1-2 1, 2-3 5, 3-4 1, 4-5 6, 5-6 1` that rule selects three edges on six "
                  "vertices and leaves three separate pieces &mdash; the lab reports all three "
                  "figures. Every one of those three edges is in the minimum tree, which is the "
                  "cut property doing its job; they are simply not enough of it, because the "
                  "lemma is about one cut at a time and says nothing about what a family of cuts "
                  "collectively covers."),
            ("p", "And it does not say the lightest edge overall is in every minimum tree, "
                  "although that happens to be true whenever it is uniquely lightest: take "
                  "`S` to be one of its endpoints alone and it is the unique lightest crossing "
                  "edge of that cut. What makes this worth stating is that the same trick does "
                  "not extend &mdash; the second-lightest edge has no such argument, because the "
                  "cut that isolates its endpoint may be crossed by the lightest edge as well."),
            ("p", "The measured figure and the proved claim, one more time. The panel's numbers "
                  "&mdash; 8 spanning trees, 1 minimum, weight 17, verdict yes &mdash; are about "
                  "the graph on screen and the cut you chose. The theorem is about every graph "
                  "and every cut, and the enumeration cannot reach it: seven vertices is where "
                  "the lab stops, and it declines above that rather than running slowly. The "
                  "exchange argument is what covers the rest."),
        ],
        "lab": ("graphkit", {
            "mode": "cutproperty",
            "preset": "distinct",
            "panel_title": "Type the weighted graph and choose a side",
            "panel_intro": "Every spanning tree is enumerated exactly, so the verdict on the "
                           "lightest crossing edge is read off the list rather than taken from "
                           "the lemma. The count of minimum trees is the answer to whether the "
                           "tree is unique, and the per-edge column says how many minimum trees "
                           "each edge appears in.",
        }),
        "steps_title": "Using the lemma to justify an edge",
        "steps_intro": "Name the cut first. Every safe edge on this course is safe because of some cut.",
        "steps": [
            ("Name the set S before you name the edge",
             "The lemma licenses an edge only relative to a cut. &ldquo;This edge is light, so it "
             "is safe&rdquo; is not an argument; &ldquo;this edge is the lightest crossing the "
             "cut between what I have built and what I have not&rdquo; is. Both algorithms in "
             "this module are a rule for choosing `S`, and nothing more."),
            ("Check whether the lightest crossing edge is unique",
             "If it is, you are entitled to say every minimum tree contains it, which is the "
             "stronger and more useful claim. If it is not, you may only say some minimum tree "
             "does &mdash; and two implementations may then legitimately return different trees "
             "of the same weight."),
            ("Use the cycle property to rule an edge out",
             "The two lemmas are complementary: one puts an edge in, one keeps an edge out. When "
             "a candidate edge closes a cycle with edges you already have and it is the heaviest "
             "on that cycle, it is in no minimum tree at all, which is exactly why one of the two "
             "algorithms can discard an edge for ever on first sight."),
            ("Enumerate where you can, and know where you stopped",
             "Below eight vertices the lab lists every spanning tree, so &ldquo;in every minimum "
             "tree&rdquo; is a fact about a list. Above that it declines. Any claim you carry "
             "past the cap is carried by the proof, and it is worth being able to say which of "
             "the two you are relying on."),
        ],
        "worked": {
            "title": "One cut, every spanning tree, and the verdict",
            "intro": [
                "The graph is `1-2 4, 1-3 3, 2-3 2, 2-4 5, 3-4 7, 4-5 1, 5-6 6` and the chosen "
                "side is `S = {1, 2, 3}`. Six vertices, so a spanning tree has five edges.",
            ],
            "lines": [
                "crossing edges of S = {1, 2, 3}      2-4 at 5      3-4 at 7",
                "lightest crossing edge               2-4",
                "",
                "every spanning tree, by total weight",
                "  1-3, 2-3, 2-4, 4-5, 5-6      3+2+5+1+6 = 17     minimum",
                "  1-2, 2-3, 2-4, 4-5, 5-6      4+2+5+1+6 = 18",
                "  1-2, 1-3, 2-4, 4-5, 5-6      4+3+5+1+6 = 19",
                "  1-3, 2-3, 3-4, 4-5, 5-6      3+2+7+1+6 = 19",
                "  1-2, 2-3, 3-4, 4-5, 5-6      4+2+7+1+6 = 20",
                "  1-2, 1-3, 3-4, 4-5, 5-6      4+3+7+1+6 = 21",
                "  1-2, 2-4, 3-4, 4-5, 5-6      4+5+7+1+6 = 23",
                "  1-3, 2-4, 3-4, 4-5, 5-6      3+5+7+1+6 = 22",
                "                               8 trees, 1 of them minimum",
                "",
                "verdict     the lightest crossing edge 2-4 is in 1 of the 1 minimum trees",
                "            strictly lightest, so: in EVERY minimum spanning tree",
                "Kruskal on the same graph                                    17",
            ],
            "after": [
                "The edge `3-4`, at weight 7, is in four of the eight spanning trees and in none "
                "of the minimum ones. That is the cycle property: it is the heaviest edge on the "
                "cycle 2, 3, 4 formed with `2-3` and `2-4`. The two lemmas are visible in the "
                "same list, one putting `2-4` in and the other keeping `3-4` out.",
                "Notice that the verdict does not depend on which cut was chosen. Sweeping all 62 "
                "proper subsets of these six vertices, the lightest crossing edge is in a minimum "
                "tree every time. The cut is the reader's choice; the conclusion is not.",
                "For a faded rehearsal, change the weight of `3-4` from 7 to 5 and predict what "
                "happens to the verdict before running it. The supplied first move is this: the "
                "two crossing edges now tie at 5, so the panel's tie count rises to 2 and the "
                "strict half of the theorem no longer applies. Say what the number of minimum "
                "trees becomes, and whether `2-4` is still in every one of them.",
            ],
        },
        "quiz_title": "Cuts, exchanges, and ties",
        "quiz": [
            {"q": "Across some cut, two edges tie for lightest. What may be concluded about one of them?",
             "a": ["It is in every minimum spanning tree",
                   "It is in some minimum spanning tree",
                   "It is in no minimum spanning tree, since the other one is taken instead",
                   "Nothing at all: the lemma needs distinct weights"],
             "c": 1,
             "why": "The exchange argument still works &mdash; it produces a tree of the same "
                    "weight containing the edge &mdash; so the some-claim holds. Only the strict "
                    "half fails, and the lab shows the failure concretely on an equal-weight "
                    "triangle, where each of the three edges is in two of the three minimum "
                    "trees."},
            {"q": "An edge is the unique heaviest edge on some cycle of a connected graph. What follows?",
             "a": ["It is in no minimum spanning tree",
                   "It is in some minimum spanning tree but not every one",
                   "It is the heaviest edge in the graph",
                   "Nothing, unless it is also a crossing edge of some cut"],
             "c": 0,
             "why": "That is the cycle property. Any tree containing it, with it removed, breaks "
                    "into two pieces the rest of the cycle can rejoin more cheaply. The lab's "
                    "cycle preset shows an edge of weight 4 in no minimum tree while an edge of "
                    "weight 6 is in the minimum tree, so being heaviest overall is neither "
                    "necessary nor the point."},
            {"q": "Selecting the lightest edge at every vertex of `1-2 1, 2-3 5, 3-4 1, 4-5 6, 5-6 1` gives three edges on six vertices. What does that show?",
             "a": ["That the cut property is false for those cuts",
                   "That those three edges are not all in a minimum spanning tree",
                   "That a family of correct local choices need not add up to a spanning tree",
                   "That the graph has no spanning tree"],
             "c": 2,
             "why": "All three selected edges ARE in the minimum tree &mdash; each is the "
                    "strictly lightest edge crossing the cut that isolates its own endpoint, so "
                    "the lemma applies and holds. They simply leave three separate pieces. The "
                    "lemma is about one cut at a time and promises nothing about coverage."},
            {"q": "The lab reports 8 spanning trees, 1 of them minimum. What does the 1 settle?",
             "a": ["That the weights are all distinct",
                   "That the minimum spanning tree of this graph is unique",
                   "That both algorithms in this module will produce the same edge order",
                   "That every crossing edge of every cut is uniquely lightest"],
             "c": 1,
             "why": "One minimum tree is exactly what uniqueness means, and it is read off a "
                    "complete enumeration. Distinct weights are sufficient for uniqueness but not "
                    "necessary, so the count does not establish them; and two algorithms "
                    "producing the same tree still take its edges in different orders."},
        ],
        "mistakes": [
            ("Reading the cut property as being about the lightest edge in the graph",
             "It is about the lightest edge across one particular cut, and the cut is part of the "
             "statement. The confusion is fed by the fact that the globally lightest edge IS "
             "covered, by taking `S` to be one of its endpoints &mdash; but that argument does "
             "not extend to the second-lightest, and readers who have only seen the global "
             "version tend to believe it does."),
            ("Upgrading some to every without checking the tie",
             "The two halves of the theorem are separated by exactly one strict inequality, and "
             "the lab prints the tie count so the distinction is visible. With a tie, two correct "
             "implementations may return different trees, both minimum, and code that compares "
             "them edge by edge will report a defect that is not there."),
            ("Treating the enumeration as the proof",
             "Eight spanning trees on six vertices is a fact about six vertices. The lab stops at "
             "seven and declines above that, and every claim the course makes past the cap rests "
             "on the exchange argument. The enumeration's job is to catch a lemma stated "
             "backwards, which is what it is good at, not to establish anything universal."),
        ],
        "standard": ("Finish when you can justify an edge by naming a cut, and say whether you have earned some or every.",
                     "You should be able to state both lemmas, reproduce the exchange argument, "
                     "identify the crossing edges of a cut you chose, read the verdict off the "
                     "enumeration, and explain why lightest-at-each-vertex is not a spanning tree "
                     "even though every edge it picks is safe."),
        "note": ("Both of the next two lessons are this lemma with a rule for choosing the cut "
                 "attached. &ldquo;Kruskal's Algorithm&rdquo; sorts the edges and lets the cut be "
                 "whatever the current forest makes it; &ldquo;Prim's Algorithm&rdquo; fixes the "
                 "cut as the boundary of one growing tree. They are not two ideas, they are two "
                 "schedules for the same one, which is why this lesson came first."),
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "kruskals-algorithm",
        "title": "Kruskal's Algorithm",
        "module": "Minimum spanning trees",
        "one_line": "Sort the edges, take each one unless its ends are already joined, and count the union-find work that decides.",
        "summary": (
            "Sort every edge by weight and walk the list once. Take an edge when its two ends lie "
            "in different pieces of the forest built so far; reject it when they lie in the same "
            "piece, because it would close a cycle. The whole algorithm is the sort plus a "
            "structure that answers same piece or not, and the cut property is what says each "
            "taken edge is safe."
        ),
        "key": [
            "sort the edges by weight, then walk the list once",
            "find(u) = find(v)  ->  reject: the edge would close a cycle",
            "otherwise          ->  take it, and union the two pieces",
            "safe by the cut property, with S the piece containing one end",
            "stop after V - 1 edges are taken; fewer means the graph is not connected",
        ],
        "key_label": "One sorted pass, and one question asked of every edge",
        "concepts_intro": (
            "The hard idea is which cut justifies each taken edge, because the algorithm never "
            "names one. The other two are the rejection rule and what the counts measure."
        ),
        "concepts": [
            ("Every taken edge is safe, and the cut is implied",
             "When the algorithm takes an edge joining two different pieces, let `S` be the piece "
             "containing one of its ends. Every crossing edge of that cut is still unexamined or "
             "already rejected, and every unexamined edge is at least as heavy, because the list "
             "is sorted. So the edge being taken is a lightest crossing edge of that cut, and the "
             "cut property applies. The algorithm never computes `S`; the argument does."),
            ("A rejection is the cycle property, not a heuristic",
             "An edge whose ends are already in the same piece closes a cycle with edges the "
             "algorithm has already taken, and every one of those is at most as heavy because "
             "they came earlier in the sorted list. So the rejected edge is a heaviest edge on "
             "that cycle. Discarding it for ever is therefore justified rather than merely "
             "convenient. On the lab's opening graph three of the nine edges are rejected, each "
             "for that reason, and the panel prints the reason per edge."),
            ("The cost is a sort plus the pieces",
             "The sort is `Θ(E log E)`, which is `Θ(E log V)` because `E &lt; V²`. What remains "
             "is two find operations per edge and one union per taken edge. On the opening graph "
             "the panel counts 18 finds, 6 unions and 10 pointer hops on nine edges and seven "
             "vertices &mdash; and the hop count is the part that depends on the structure rather "
             "than on the graph, which is what makes it worth measuring separately."),
        ],
        "read_title": "One sorted pass, and the structure underneath it",
        "read_intro": "The algorithm, why each taken edge is safe, why each rejected edge is dead, and what the three counters mean.",
        "body": [
            ("h3", "The algorithm"),
            ("ol", ["Sort the edges by weight, breaking ties any way at all.",
                    "Put every vertex in its own piece.",
                    "For each edge in order, ask whether its two ends are in the same piece. If "
                    "they are, reject it. If they are not, take it and merge the two pieces.",
                    "Stop when `V - 1` edges have been taken, or when the list runs out &mdash; "
                    "in which case the graph was not connected and what was built is a minimum "
                    "spanning forest."]),
            ("p", "The operations on pieces are exactly the two a disjoint-set structure "
                  "provides, and Data Structures' &ldquo;Union&ndash;Find&rdquo; costs them. This "
                  "lesson uses the operations and re-derives none of their analysis; what it does "
                  "measure is how many of each this algorithm performs, which is a property of "
                  "the algorithm rather than of the structure."),
            ("thm", ("Kruskal's algorithm returns a minimum spanning tree",
                     "On a connected weighted graph, the set of edges the algorithm takes is a "
                     "spanning tree of least total weight.")),
            ("proof", ("It is a forest at every step, because an edge is taken only when its ends "
                       "are in different pieces, which is exactly the condition for it not to "
                       "close a cycle. It ends spanning: if two pieces remained, connectivity "
                       "gives an edge between them, and that edge would have been taken when the "
                       "list reached it.",
                       "It is minimum by induction on the number of edges taken, with the "
                       "invariant that the current forest is contained in some minimum spanning "
                       "tree. Empty at the start, so the invariant holds. Suppose it holds before "
                       "an edge `e` is taken, with the forest inside a minimum tree `T`. Let `S` "
                       "be the piece containing one end of `e`. No edge of the forest crosses "
                       "that cut, and every crossing edge is either unexamined &mdash; hence at "
                       "least as heavy as `e` &mdash; or was rejected, which cannot happen to a "
                       "crossing edge while `S` is a piece. So `e` is a lightest crossing edge, "
                       "and by the exchange in the cut property there is a minimum tree "
                       "containing the forest and `e`. The invariant survives, and at the end the "
                       "forest is a spanning tree inside a minimum tree, so it is one.")),
            ("example", ("Nine edges, six taken, three rejected",
                         "The lab opens on `1-2 4, 1-3 3, 2-3 2, 2-4 5, 3-4 7, 4-5 1, 5-6 6, "
                         "5-7 8, 6-7 2`. Sorted, the list is `4-5` at 1, `2-3` at 2, `6-7` at 2, "
                         "`1-3` at 3, `1-2` at 4, `2-4` at 5, `5-6` at 6, `3-4` at 7, `5-7` at 8. "
                         "The algorithm takes the first four, rejects `1-2`, takes `2-4` and "
                         "`5-6`, then rejects `3-4` and `5-7`. Total weight 19, on six edges for "
                         "seven vertices. The counters read 18 finds, 6 unions and 10 pointer "
                         "hops. An independently written Kruskal, from another Subject and with "
                         "its own representation, is handed the same graph and returns 19.")),
            ("p", "Read the rejections. `1-2` at weight 4 is refused because 1 and 2 are already "
                  "joined through 3, by the edges `2-3` at 2 and `1-3` at 3, and 4 is heavier "
                  "than both &mdash; it is the heaviest edge on that triangle. `3-4` and `5-7` "
                  "are refused for the same reason on their own cycles. No rejected edge is ever "
                  "reconsidered, and the cycle property is why that is sound rather than greedy."),
            ("h3", "What the three counters are for"),
            ("p", "Finds are two per edge examined, so 18 on nine edges, whatever the graph looks "
                  "like. Unions are one per taken edge, so `V - 1` on a connected graph, so 6 "
                  "here. Neither of those is interesting on its own. The hops are: they count how "
                  "far each find had to walk up the parent pointers, and that depends on how the "
                  "unions happened to be arranged."),
            ("p", "The lab's chain preset makes this visible. On `1-2 1, 2-3 2, 3-4 3, 4-5 4, "
                  "5-6 5, 1-6 9` the unions build a line, and the counters read 12 finds, 5 "
                  "unions and 5 hops for weight 15. The complete graph on five vertices goes the "
                  "other way: ten edges, four taken and six rejected, 20 finds, 4 unions and 18 "
                  "hops for weight 7. The hop count is the only one of the three that moved for a "
                  "reason other than the number of edges."),
            ("p", "This implementation deliberately does neither union by rank nor path "
                  "compression, so the hop count is a real measurement of an unassisted "
                  "structure. With those two refinements the finds and unions would be identical "
                  "and the hops would collapse, which is precisely the point: the refinements "
                  "change the cost of the structure and not the behaviour of the algorithm."),
            ("h3", "When the graph is not connected"),
            ("p", "On `1-2 1, 2-3 2, 4-5 3, 5-6 4` the list runs out after four edges are taken, "
                  "one short of the five a spanning tree of six vertices needs. The panel reports "
                  "that it does not span, rather than presenting a forest of weight 10 as though "
                  "it were a tree. The result is still the minimum spanning forest, and it is "
                  "still the right answer to a slightly different question &mdash; but the "
                  "difference is exactly the kind a caller has to be told about."),
            ("p", "Measurement beside bound, last time. On the opening graph: 18 finds, 6 unions, "
                  "10 hops, and a sort of nine items. Those are counts for that graph. The bound "
                  "is `O(E log V)` on every graph and it is dominated by the sort: the finds are "
                  "`2E` exactly, the unions are at most `V - 1` exactly, and the hops are what "
                  "the disjoint-set analysis bounds. The measured hop count on the complete graph "
                  "&mdash; 18, on twenty finds &mdash; is evidence about an unassisted structure "
                  "on one input, and nothing more."),
        ],
        "lab": ("graphkit", {
            "mode": "kruskal",
            "preset": "classic",
            "panel_title": "Type the graph and step the sorted edges",
            "panel_intro": "Each row is one edge in sorted order, the two finds it made, and the "
                           "reason it was taken or rejected. The forest beside the graph is the "
                           "union-find state those finds walk, the pointer hops are counted, and "
                           "the total is compared with an independently written minimum-tree "
                           "algorithm from another Subject.",
        }),
        "steps_title": "Running the sorted pass",
        "steps_intro": "Sort once, then ask one question of each edge in turn.",
        "steps": [
            ("Sort first, and stop caring about order after that",
             "Ties may be broken any way; the lemma covers it, and two different tie-breaks give "
             "two different minimum trees of the same weight. What must not happen is re-sorting "
             "or revisiting: the proof depends on every unexamined edge being at least as heavy "
             "as the current one."),
            ("Ask same-piece, not same-vertex",
             "The test is whether the two ends have the same representative, which is a question "
             "about the forest built so far and not about the edge. A reader tracking connected "
             "pieces by eye will get this right on six vertices and wrong on twenty; the "
             "structure exists because the question is asked `2E` times."),
            ("Record why each rejection happened",
             "A rejected edge closes a cycle with edges already taken, all of them at most as "
             "heavy, so it is a heaviest edge on that cycle and is in no minimum tree. Writing "
             "the reason down turns a discarded edge into an application of the cycle property, "
             "and it is what the lab's third column prints."),
            ("Count the taken edges and check against V minus 1",
             "Anything less means the graph was not connected, and the honest report is a minimum "
             "spanning forest with the number of pieces named. Presenting a forest as a tree is "
             "the failure mode this algorithm has, because nothing in its inner loop notices."),
        ],
        "worked": {
            "title": "Seven vertices, nine edges, in sorted order",
            "intro": [
                "The graph is `1-2 4, 1-3 3, 2-3 2, 2-4 5, 3-4 7, 4-5 1, 5-6 6, 5-7 8, 6-7 2`. "
                "Seven vertices, so a spanning tree needs six edges.",
            ],
            "lines": [
                "edge    w   find(u)  find(v)   verdict          pieces afterwards",
                "4-5     1      4        5      take             {4,5}",
                "2-3     2      2        3      take             {2,3} {4,5}",
                "6-7     2      6        7      take             {2,3} {4,5} {6,7}",
                "1-3     3      1        3      take             {1,2,3} {4,5} {6,7}",
                "1-2     4      3        3      REJECT: a cycle  unchanged",
                "2-4     5      3        5      take             {1,2,3,4,5} {6,7}",
                "5-6     6      5        7      take             {1,2,3,4,5,6,7}",
                "3-4     7      7        7      REJECT: a cycle  unchanged",
                "5-7     8      7        7      REJECT: a cycle  unchanged",
                "",
                "tree    4-5, 2-3, 6-7, 1-3, 2-4, 5-6        6 edges, weight 19",
                "counts  18 finds, 6 unions, 10 pointer hops",
                "an independently written Kruskal on the same graph            19",
            ],
            "after": [
                "The find column is the whole algorithm. It is not the vertex numbers; it is the "
                "representative of each end's piece, which is why `1-2` shows 3 and 3 &mdash; by "
                "then 1, 2 and 3 have all been merged and 3 is the representative. The rejection "
                "is that equality and nothing else.",
                "The two edges of weight 2 were both taken, and they could have been examined in "
                "either order with the same result, because they touch no common vertex. Where a "
                "tie does matter, the two orders give two different trees of the same weight, and "
                "the enumeration in &ldquo;The Cut Property&rdquo; is what tells you how many "
                "such trees exist.",
                "For a faded rehearsal, change the weight of `1-2` from 4 to 1 and predict the "
                "new tree before running it. The supplied first move is this: `1-2` now ties with "
                "`4-5` at the top of the list and is examined before `2-3` and `1-3`, so it is "
                "taken. Say which edge is rejected in its place, and whether the total weight "
                "changes.",
            ],
        },
        "quiz_title": "Sorting, finding, and rejecting",
        "quiz": [
            {"q": "Which cut makes a taken edge safe, given that the algorithm never computes one?",
             "a": ["The cut between the taken edges and the rejected ones",
                   "The cut whose side S is the piece containing one end of the edge",
                   "The cut separating the lightest half of the edges from the heaviest half",
                   "None: Kruskal's correctness does not use the cut property"],
             "c": 1,
             "why": "Taking `S` to be one end's current piece, every crossing edge is unexamined "
                    "and therefore at least as heavy, so this edge is a lightest crossing edge "
                    "and the lemma applies. The cut exists in the proof rather than in the code, "
                    "which is what makes the same lemma cover the other algorithm in this module "
                    "as well."},
            {"q": "On nine edges the lab reports 18 finds. What does that number depend on?",
             "a": ["The number of edges examined, and nothing else",
                   "The weights",
                   "Whether union by rank is used",
                   "The number of vertices"],
             "c": 0,
             "why": "Two finds are performed per edge, whatever the answer turns out to be, so "
                    "the count is `2E` on any connected input with `E` edges examined. The "
                    "counter that does respond to the structure is the pointer-hop count, which "
                    "is why the lab prints it separately."},
            {"q": "The list of edges runs out with only `V - 2` edges taken. What should be reported?",
             "a": ["A minimum spanning tree, with one edge missing",
                   "An error: the algorithm failed",
                   "A minimum spanning forest, with the number of pieces named",
                   "The tree, plus the heaviest rejected edge to make up the count"],
             "c": 2,
             "why": "The input was not connected, and what the algorithm built is the correct "
                    "minimum spanning forest. Nothing in the inner loop notices, so the check "
                    "against `V - 1` has to be made deliberately &mdash; the lab's forest preset "
                    "is exactly this case and reports that it does not span."},
            {"q": "An edge is rejected. Under what circumstances might it belong to some minimum spanning tree after all?",
             "a": ["If a later edge is heavier",
                   "If the graph has ties, so the edge may be tied with the heaviest on its cycle",
                   "Never: a rejected edge is in no minimum spanning tree",
                   "If the tie-break order had been different"],
             "c": 1,
             "why": "The cycle property is about a UNIQUELY heaviest edge. A rejected edge tied "
                    "with another on its cycle may appear in a different minimum tree of the same "
                    "weight &mdash; which is exactly what different tie-breaks produce. The "
                    "algorithm is still correct: it returns one minimum tree, not the set of "
                    "them."},
        ],
        "mistakes": [
            ("Testing whether the edge's endpoints are adjacent rather than connected",
             "The question is whether a path already exists between them, not whether an edge "
             "does. On the lab's opening graph `1-2` is rejected although 1 and 2 have no other "
             "edge between them: they are joined through 3. This is the mistake that makes a "
             "hand-run of the algorithm produce a graph with a cycle in it."),
            ("Re-examining a rejected edge later",
             "Once rejected, an edge is dead, and the cycle property is why. The temptation "
             "arises when a later edge turns out heavy, and the instinct is that the earlier "
             "lighter one should be reconsidered &mdash; but the earlier one closed a cycle with "
             "edges that were lighter still, and nothing that happens afterwards changes that."),
            ("Quoting the union-find bound as the algorithm's cost",
             "The sort dominates. `O(E log V)` comes from ordering the edges, and the "
             "disjoint-set work is below it whatever refinements the structure uses &mdash; which "
             "means that speeding up the structure cannot speed up this algorithm, and that if "
             "the edges arrive already sorted the bound is a different one."),
        ],
        "standard": ("Finish when you can run the sorted pass by hand and justify every take and every reject.",
                     "You should be able to sort the edges, maintain the pieces, name the cut "
                     "that makes each taken edge safe, name the cycle that makes each rejected "
                     "edge dead, read the three counters and say which of them depends on the "
                     "structure rather than on the graph, and check the result against `V - 1`."),
        "note": ("The other algorithm in this module chooses its cut in advance rather than "
                 "letting the sorted list imply one. &ldquo;Prim's Algorithm&rdquo; fixes `S` as "
                 "the set of vertices already in one growing tree, which turns the question from "
                 "&ldquo;are these two joined&rdquo; into &ldquo;what is the lightest edge "
                 "leaving here&rdquo; &mdash; and that is a heap rather than a disjoint-set "
                 "structure."),
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "prims-algorithm",
        "title": "Prim's Algorithm",
        "module": "Minimum spanning trees",
        "one_line": "Grow one tree across its own boundary, step the heap, and watch a stale entry come out of it.",
        "summary": (
            "Fix the cut in advance: one side is the tree built so far, the other is everything "
            "else. The lightest edge across that boundary is safe by the cut property, so the "
            "algorithm is a loop that finds it and adds it. A heap keyed on edge weight finds it, "
            "and the interesting consequence is that entries in the heap go out of date and must "
            "be discarded when they surface."
        ),
        "key": [
            "S = the vertices already in the tree; the cut is its boundary",
            "repeat V - 1 times: take the lightest edge leaving S, add its far end to S",
            "heap holds candidate edges; a pop whose ends are BOTH in S is stale, skip it",
            "same tree as the sorted method, reached in a different order",
            "the answer does not depend on the starting vertex; the work does",
        ],
        "key_label": "One growing side, and the heap that finds its lightest exit",
        "concepts_intro": (
            "The hard idea is the stale entry. The cut and the correctness are the sorted "
            "method's, restated with the choice of cut made in advance."
        ),
        "concepts": [
            ("The cut is chosen first, and never changes shape",
             "`S` starts as the single starting vertex and grows by one vertex each step. At "
             "every step the algorithm takes a lightest edge crossing the cut between `S` and the "
             "rest, which is exactly the hypothesis of the cut property, so every edge it takes "
             "is safe. Where the sorted method leaves the cut implicit in its proof, this "
             "algorithm maintains it explicitly, which is the only real difference between them."),
            ("A heap entry can go out of date, and the fix is to check on the way out",
             "Candidate edges are pushed as their tail joins `S`. An edge pushed while its far "
             "end was outside may have that end brought into `S` by a different edge before it "
             "surfaces, and then it crosses nothing. Rather than find and delete it &mdash; which "
             "a binary heap cannot do cheaply &mdash; the algorithm pops it and discards it. On "
             "the lab's opening graph that happens exactly once, to the edge between 1 and 2 at "
             "weight 4, and the panel labels the row rather than hiding it."),
            ("The answer is fixed, the work is not",
             "Starting the same graph at different vertices gives the same tree of weight 19 "
             "every time, and different amounts of work: 12 key comparisons from vertex 1, 14 "
             "from vertex 2, 24 from vertex 4 and 15 from vertex 7. That is a measurement of the "
             "heap's behaviour on one graph from four starts, and it is the clearest small "
             "example on this course of a count that moves while the answer does not."),
        ],
        "read_title": "One boundary, one heap, and the entries that expire",
        "read_intro": "The algorithm, the correctness it inherits, what a stale entry is, and the reference column that is not a verdict.",
        "body": [
            ("h3", "The algorithm"),
            ("ol", ["Put the starting vertex in `S` and push every edge at it onto a heap keyed "
                    "by weight.",
                    "Pop the lightest entry. If both its ends are already in `S`, discard it and "
                    "pop again.",
                    "Otherwise take the edge, put its far end `u` into `S`, and push every edge "
                    "at `u` whose far end is not yet in `S`.",
                    "Stop when `V - 1` edges have been taken, or when the heap empties first "
                    "&mdash; in which case the graph was not connected."]),
            ("p", "Correctness is the cut property applied once per step, with `S` as the side. "
                  "The edge taken is by construction a lightest edge crossing that cut, so it lies "
                  "in some minimum spanning tree extending what has been built. That is the same "
                  "induction the sorted method uses; only the choice of cut differs."),
            ("example", ("Seven vertices, seven pops, one of them stale",
                         "The lab opens on `1-2 4, 1-3 3, 2-3 2, 2-4 5, 3-4 7, 4-5 1, 5-6 6, "
                         "5-7 8, 6-7 2`, starting at vertex 1. The pops come out `1-3` at 3 "
                         "adding vertex 3, `2-3` at 2 adding vertex 2, then `1-2` at 4 with both "
                         "ends already in `S` &mdash; discarded &mdash; then `2-4` at 5 adding 4, "
                         "`4-5` at 1 adding 5, `5-6` at 6 adding 6, and `6-7` at 2 adding 7. Six "
                         "edges, weight 19, the same tree the sorted method built. The counters "
                         "read 9 pushes, 7 pops and 12 key comparisons.")),
            ("p", "The pop order is worth a second look, because it is not sorted. `1-3` at "
                  "weight 3 comes out before `2-3` at weight 2, and `2-4` at 5 before `4-5` at 1. "
                  "The heap returns the lightest entry it HOLDS, and an edge is only held once "
                  "its tail has joined the tree &mdash; `4-5` was not a candidate until 4 was in. "
                  "That is the whole difference from the sorted method, which considers every "
                  "edge in one global order."),
            ("h3", "Stale entries, and why they are tolerated"),
            ("p", "Nine edges were pushed and seven popped. The two never popped are the two the "
                  "loop stopped before reaching, and one of the seven was stale. A heap has no "
                  "cheap way to find and remove an entry that is no longer wanted, so the "
                  "standard answer is to leave it and test on the way out. The cost is that the "
                  "heap may hold up to `E` entries rather than `V`, which is where the `E log V` "
                  "term in the usual bound comes from."),
            ("p", "The lab's lazy preset was built to fill the heap with such entries, and "
                  "measuring it is instructive: on `1-2 1, 1-3 1, 1-4 1, 2-3 9, 2-4 9, 3-4 9, "
                  "1-5 2, 2-5 3, 3-5 4` the run pushes 9 entries, pops 4, and discards none of "
                  "them. The heavy edges do become stale, but the four light edges at vertex 1 "
                  "are enough to finish the tree, and the loop stops before any stale entry "
                  "reaches the top. Staleness costs memory here and no pops at all &mdash; which "
                  "is a different thing from what the preset's name suggests, and the count is "
                  "what settles it."),
            ("h3", "The reference column, and what may not be read off it"),
            ("p", "The panel prints a column labelled as `E` times `log₂ V` for reference. It is "
                  "computed as the number of edges times the integer part of the base-two "
                  "logarithm of the number of vertices, so on the opening graph it is 9 times 2, "
                  "which is 18. The measured comparison count is 12. Those two numbers are not "
                  "the same kind of thing and the panel says so: the first is a count of "
                  "something that happened on one graph from one starting vertex, and the second "
                  "is a scale for what the heap operations would cost in the worst case."),
            ("p", "Specifically, 12 being below 18 is not evidence that the algorithm beats its "
                  "bound, and 24 from vertex 4 being above it is not evidence that it fails one. "
                  "The reference is a number to compare growth against across several graphs, and "
                  "the lab's other presets are there to be swept: a star on six vertices gives 12 "
                  "comparisons against a reference of 10, and the nine-edge graph on five "
                  "vertices gives 18 against 18. No verdict is printed beside the column, "
                  "deliberately."),
            ("h3", "Against the other algorithm"),
            ("p", "Both algorithms are run on whatever graph you type and the two weights are "
                  "printed together. On the opening graph both give 19. On the ties preset "
                  "`1-2 2, 1-3 2, 2-3 2, 3-4 1` both give 5, and here they take the same three "
                  "edges in different orders: one starts with the edge of weight 1 because it "
                  "sorted first, the other reaches it last because its tail only joined the tree "
                  "at the end. Equal weight, equal edge set, different schedule &mdash; and on a "
                  "graph with a genuine choice between tied edges, the edge sets can differ too."),
            ("p", "The measured counts, beside the bound. From vertex 1: 9 pushes, 7 pops, 12 "
                  "comparisons, weight 19. From vertex 4: 9 pushes, 7 pops, 24 comparisons, "
                  "weight 19. The bound is `O(E log V)` on every graph from every start, and it "
                  "comes from at most `E` pushes and at most `E` pops, each costing `O(log V)` "
                  "comparisons on a heap holding at most `E &lt; V²` entries. Four starting "
                  "vertices on one graph is not a bound, and the spread between 12 and 24 is "
                  "exactly the reason to say so."),
        ],
        "lab": ("graphkit", {
            "mode": "prim",
            "preset": "classic",
            "panel_title": "Type the graph and step the heap",
            "panel_intro": "Every pop is a row: what came out, whether it was used, and the "
                           "heap's keys afterwards. The same graph is run through the sorted "
                           "method as well, so the two answers sit side by side, and the starting "
                           "vertex can be moved to watch the counts change while the weight does "
                           "not.",
        }),
        "steps_title": "Growing one tree",
        "steps_intro": "Maintain the boundary, and test every pop before you use it.",
        "steps": [
            ("Keep S explicit, as a flag per vertex",
             "The whole algorithm is a question about the boundary of `S`, and the boundary is "
             "cheap to maintain only if membership is a constant-time test. Recomputing which "
             "vertices are in the tree from the edge list each step is the change that turns this "
             "into a quadratic algorithm without anything looking wrong."),
            ("Test both ends on the way out, not on the way in",
             "An entry is valid when pushed and may expire before it surfaces. Checking at push "
             "time is not enough and deleting from the middle of a heap is not cheap, so the "
             "check belongs at the pop. Count the discarded pops: they are real work and they "
             "belong in any measurement you report."),
            ("Read the pop order as the algorithm's order, not as sorted order",
             "The heap returns the lightest edge it currently holds, and it only holds edges "
             "whose tails have joined. A heavier edge coming out before a lighter one is normal "
             "and is not a defect in the heap; it means the lighter one was not yet a candidate."),
            ("Move the starting vertex before quoting a count",
             "The tree does not change and the work does. On the lab's opening graph the "
             "comparison count runs from 12 to 24 over four starts. A single measurement "
             "presented as the algorithm's cost is a measurement of one start on one graph."),
        ],
        "worked": {
            "title": "Seven pops from vertex 1, one of them wasted",
            "intro": [
                "The graph is `1-2 4, 1-3 3, 2-3 2, 2-4 5, 3-4 7, 4-5 1, 5-6 6, 5-7 8, 6-7 2` and "
                "the tree starts at vertex 1.",
            ],
            "lines": [
                "push at start   1-2 (4), 1-3 (3)                 S = {1}",
                "",
                "pop    w   both ends in S?   action              S afterwards",
                "1-3    3        no           take, add 3         {1, 3}",
                "                             push 2-3 (2), 3-4 (7)",
                "2-3    2        no           take, add 2         {1, 2, 3}",
                "                             push 2-4 (5)",
                "1-2    4       YES           STALE, discard      unchanged",
                "2-4    5        no           take, add 4         {1, 2, 3, 4}",
                "                             push 4-5 (1)",
                "4-5    1        no           take, add 5         {1, 2, 3, 4, 5}",
                "                             push 5-6 (6), 5-7 (8)",
                "5-6    6        no           take, add 6         {1, ..., 6}",
                "                             push 6-7 (2)",
                "6-7    2        no           take, add 7         all seven; stop",
                "",
                "tree    1-3, 2-3, 2-4, 4-5, 5-6, 6-7        weight 19",
                "counts  9 pushes, 7 pops, 12 key comparisons",
                "the sorted method on the same graph           weight 19",
                "E times the integer part of log2 V, for reference        18",
            ],
            "after": [
                "The stale pop is the third row, and it is worth being precise about why `1-2` "
                "expired. It was pushed at the start, when 2 was outside the tree. By the time it "
                "reached the top, 2 had been brought in by `2-3` at weight 2 &mdash; a lighter "
                "edge that did not exist as a candidate until 3 joined. Nothing went wrong; the "
                "entry simply stopped describing a crossing edge.",
                "Two entries were never popped at all: `3-4` at 7 and `5-7` at 8 were still in "
                "the heap when the sixth edge was taken and the loop stopped. Those are the "
                "same two edges the sorted method rejected, reached by a completely different "
                "route, and it is a good check on a hand-run that the two methods disagree about "
                "nothing but order.",
                "For a faded rehearsal, start the same graph at vertex 4 and predict the first "
                "three pops before running it. The supplied first move is this: the edges at 4 "
                "are `2-4` at 5, `3-4` at 7 and `4-5` at 1, so the first pop is `4-5`. Say what "
                "the next two are, whether any pop is stale from this start, and what the final "
                "weight is.",
            ],
        },
        "quiz_title": "Boundaries, heaps and stale entries",
        "quiz": [
            {"q": "A pop returns an edge whose two ends are both already in the tree. What should happen?",
             "a": ["Add it anyway; it is the lightest available",
                   "Discard it and pop again",
                   "Stop: the tree is complete",
                   "Push it back with its weight increased"],
             "c": 1,
             "why": "The entry has expired: its far end joined the tree by another edge, so it "
                    "crosses nothing and adding it would close a cycle. Discarding at the pop is "
                    "the standard handling, because removing an arbitrary entry from a binary "
                    "heap is not cheap. The heap being non-empty says nothing about the tree "
                    "being complete."},
            {"q": "Starting the same graph at four different vertices gives weight 19 every time and comparison counts of 12, 14, 24 and 15. What is established?",
             "a": ["That the heap implementation is inconsistent",
                   "That the minimum spanning tree is unique on this graph",
                   "That the work depends on the start while the answer does not, on this graph",
                   "That starting at vertex 1 is optimal in general"],
             "c": 2,
             "why": "Four measurements on one graph show the counts moving and the weight not. "
                    "That the weight cannot move is a theorem &mdash; the algorithm returns a "
                    "minimum tree from any start &mdash; but uniqueness of the tree is a "
                    "different claim needing the enumeration, and one graph says nothing about "
                    "which start is best in general."},
            {"q": "The reference column reads 18 and the measured comparison count reads 12. What may be concluded?",
             "a": ["The algorithm beat its bound on this run",
                   "Nothing about a bound: one is a count on one input, the other is a scale",
                   "The bound is wrong for this graph",
                   "The heap is smaller than it should be"],
             "c": 1,
             "why": "The column is `E` times the integer part of `log₂ V`, printed for "
                    "comparison as the graph changes, and no verdict is read off it. A count "
                    "below it is not a refutation of anything and a count above it &mdash; 24, "
                    "from another starting vertex on the same graph &mdash; is not a failure "
                    "either."},
            {"q": "Nine edges are pushed and seven popped on a seven-vertex graph. Why do two entries never come out?",
             "a": ["They were deleted from the heap when they expired",
                   "The loop stopped after `V - 1` edges were taken, leaving them behind",
                   "They were never pushed, since both ends were already in the tree",
                   "The heap discards its two largest entries automatically"],
             "c": 1,
             "why": "Six edges complete a spanning tree of seven vertices, and the loop halts "
                    "there with whatever the heap still holds. Expired entries are not deleted "
                    "&mdash; they are discarded on the way out, and one of the seven pops was "
                    "exactly that."},
        ],
        "mistakes": [
            ("Keying the heap on the wrong quantity",
             "The key is the edge's weight, full stop. The other algorithm on this path that "
             "looks like this one keys on the distance from a source, which is a running total "
             "rather than a single edge, and swapping the two gives a wrong answer that is hard "
             "to see: both produce a spanning tree, and only one of them is minimum."),
            ("Expecting the pops to come out in sorted order",
             "They come out in the order the heap holds them, and an edge is only held once its "
             "tail has joined the tree. On the lab's opening graph weight 3 comes out before "
             "weight 2 and weight 5 before weight 1. A reader who reads the pop column as a "
             "sorted list will conclude the heap is broken."),
            ("Reading the reference column as a bound the run must respect",
             "It is `E` times an integer logarithm, printed so that the measured counts can be "
             "watched against a scale as the graph grows. On one graph the same algorithm "
             "produced 12 comparisons from one start and 24 from another, either side of a "
             "reference of 18. No verdict is printed beside it, and none should be inferred."),
        ],
        "standard": ("Finish when you can step the heap by hand, spot the stale pop, and say what changes when the start moves.",
                     "You should be able to maintain `S` and the candidate heap, take the "
                     "lightest crossing edge each step, recognise and discard an expired entry, "
                     "name the cut that makes each taken edge safe, and separate the counts that "
                     "move with the starting vertex from the weight that does not."),
        "note": ("&ldquo;Relaxation and Dijkstra&rsquo;s Schedule&rdquo; is this algorithm with one "
                 "word changed. Replace the key "
                 "&ldquo;weight of this edge&rdquo; with &ldquo;distance from the source through "
                 "this edge&rdquo; and the same loop computes shortest paths instead of a minimum "
                 "tree &mdash; and the arithmetic in the key is what makes the second one break "
                 "on a negative weight while the first does not."),
    },
]
