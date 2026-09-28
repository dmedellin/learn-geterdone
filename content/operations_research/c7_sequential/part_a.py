"""Dynamic Programming and Sequential Decisions -- the first half.

The recursion on a network where every path can still be walked, the same
recursion on a problem with no network in it until you build one, and then lot
sizing twice: exactly, and with the two rules of thumb that are used instead.
The half closes with chance in the transition.

Every figure below is read off scripts/mathpath/labs/dpseq.py by executing its
shipped JavaScript blocks under node, not transcribed from a design note.
Where the note and the kit disagreed, the kit won and the prose says so.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "filling-the-table-from-the-end",
        "title": "Filling the Table from the End",
        "module": "The recursion, backwards",
        "one_line": "Solve a staged network backwards, keep every tie, and check the recursion against an enumeration of every path it stands for.",
        "summary": (
            "The value of being somewhere is the cost of the next step plus the value of where "
            "that step leads. Write that down at every node, fill it in from the last stage back, "
            "and a routing problem falls out in one pass. The formula is the easy half. The half "
            "this lesson is built on is what the table does <em>not</em> contain: it holds one "
            "number per node and no route at all, so the routes have to be reconstructed "
            "afterwards &mdash; and when two continuations are worth the same, there is more "
            "than one of them."
        ),
        "key": [
            "f(v) = min over arcs v>w of [ c(v,w) + f(w) ],        f(w) = 0 in the last stage",
            "filled from the LAST stage back, so every f(w) is settled before f(v) is written",
            "the value at the start is the answer; the ROUTE comes back from the argmins",
            "a node with two argmins is a TIE, and a tie on the route means two best answers",
            "arcs  A>B 0  A>C 4  B>D 7  B>E 4  C>D 3  C>E 2  D>F 1  E>F 4     value 8",
            "change A>B from 0 to 2 and the three optimal routes collapse to one",
        ],
        "key_label": "One recursion, and the reason every tie is kept",
        "concepts_intro": (
            "Three ideas, and the formula is only the first of them. The other two are about what "
            "the table is and what it costs."
        ),
        "concepts": [
            ("A node's value is a number, and it is not a route",
             "What the recursion writes at each node is one quantity: the best total from there "
             "to the finish. It does not contain a path and cannot be asked for one. The routes "
             "are recovered at the end by walking the argmins forward from the start, and a node "
             "may have several argmins, so what comes back is a set of routes rather than a "
             "route. Reading the value as though it were a plan is what makes ties invisible."),
            ("Backwards is forced, not stylistic",
             "`f(v)` is defined in terms of `f(w)` for the nodes `v` can reach, so it can only be "
             "written once those are settled. That is the whole reason the last stage comes "
             "first: its value is zero by definition, and every other value is built on values "
             "already final. A forward pass would need the answer before it could compute it, "
             "which is why the forward object in this lesson is an enumeration and not a second "
             "method."),
            ("The saving is that each node is priced once",
             "Walking every path prices each path separately, and paths multiply as stages are "
             "added. The recursion prices each node once, and nodes add. On the network in the "
             "lab the two counts are 4 paths against 6 node values, which is no saving at all "
             "&mdash; and that is deliberate, because at this size you can check the recursion "
             "against the thing it replaces by eye. The saving is a shape, not a number."),
        ],
        "read_title": "One sentence, written down at every node",
        "read_intro": "The definition, the order it forces, and then the instance whose answer is three routes rather than one.",
        "body": [
            ("def", ("A staged network and its value function",
                     "A <strong>staged network</strong> is a list of stages, each holding some "
                     "nodes, together with <strong>arcs</strong> that only ever run forward: an "
                     "arc may join a node in one stage to a node in any later stage, never to one "
                     "in the same stage or an earlier one. Each arc carries a <strong>cost</strong>.",
                     "The <strong>value function</strong> `f` gives each node the cheapest total "
                     "from that node to the finish: `f(w) = 0` for every node in the last stage, "
                     "and `f(v) = min` over arcs out of `v` of `c(v,w) + f(w)` otherwise. An "
                     "<strong>argmin</strong> at `v` is an arc attaining that minimum; there may "
                     "be more than one.")),
            ("p", "The lab takes the stages as names separated by semicolons and the arcs one "
                  "clause each, tail then `>` then head then cost. An arc that runs backwards or "
                  "sideways is refused with the two stage numbers named, because that is a "
                  "modelling error rather than a typing one: a network with a cycle in it has no "
                  "last stage to start from and the recursion has nowhere to bottom out."),
            ("math", [
                "stages   A ; B C ; D E ; F",
                "arcs     A>B 0   A>C 4   B>D 7   B>E 4   C>D 3   C>E 2   D>F 1   E>F 4",
                "",
                "filled from the END:",
                "",
                "   f(F) = 0                                          last stage",
                "   f(D) = 1 + f(F) = 1",
                "   f(E) = 4 + f(F) = 4",
                "   f(B) = min( 7 + 1 ,  4 + 4 ) = min( 8 , 8 ) = 8   TIE: D and E both",
                "   f(C) = min( 3 + 1 ,  2 + 4 ) = min( 4 , 6 ) = 4   D",
                "   f(A) = min( 0 + 8 ,  4 + 4 ) = min( 8 , 8 ) = 8   TIE: B and C both",
                "",
                "six values written, and the answer is f(A) = 8",
            ]),
            ("p", "Read the last two lines again. `f(A)` is 8 and there are two ways to attain "
                  "it, and `f(B)` is 8 with two ways to attain that. Following the argmins "
                  "forward from `A` therefore produces three routes and not one: `A B D F`, "
                  "`A B E F` and `A C D F`. The lab prices each of them again from the arcs "
                  "before printing it, and all three come to 8."),
            ("h3", "The enumeration beside it, and what it is for"),
            ("p", "This network has four paths in total. Walked forwards and priced "
                  "independently they come to 8, 8, 8 and 10, so the best is 8 and exactly three "
                  "paths attain it. That agrees with the recursion, which is the point: the lab "
                  "runs both and prints both, and shows nothing as an answer when they disagree. "
                  "The enumeration is an oracle, not an alternative algorithm &mdash; it is "
                  "exponential on purpose, and offering it as a way to solve these problems would "
                  "undo the lesson."),
            ("example", ("One arc cost, and the number of best answers",
                         "Change `A>B` from 0 to 2 and nothing else. Every value in the table is "
                         "the same except `f(A)`, which becomes `min(2 + 8, 4 + 4) = 8` &mdash; "
                         "still 8, but now attained only through `C`. The tie at `B` is still "
                         "there, `f(B)` is still 8 with `D` and `E` both attaining it, and the "
                         "four paths now cost 10, 10, 8 and 10.",
                         "So the answer is the same number and one route instead of three, and "
                         "the tie that remains is on no optimal route at all. A recursion that "
                         "dropped ties would give identical output on both networks. That is "
                         "worth sitting with: the two cases are one arc cost apart, and nothing "
                         "in the value 8 distinguishes them.")),
            ("h3", "An arc that skips a stage"),
            ("p", "Add `A>E 3` to the original network. The recursion needs no adjustment at all: "
                  "`f(E)` is already settled when `f(A)` is written, because `E` lives in a later "
                  "stage, and the new candidate is `3 + 4 = 7`. That beats 8, so `f(A)` becomes 7 "
                  "and the single optimal route is `A E F`. Walking all five paths forwards "
                  "agrees. What makes this work is not a special case in the code but the "
                  "ordering: a value is written only once everything it depends on is final, and "
                  "a forward jump does not disturb that."),
            ("example", ("Where the stages actually come from",
                         "In a routing problem the stages are given: they are the columns of the "
                          "map. In most of the problems on this course they are not. A stage is "
                         "whatever index makes the arcs run one way &mdash; an activity, a time "
                         "period, a candidate, a number of periods left &mdash; and choosing it "
                         "is choosing the model.",
                         "That is why this lesson comes first and why it is the easiest one here. "
                         "Everything about the recursion is visible because the hard half has "
                         "been done for you. The rest of the course does the hard half.")),
            ("p", "One last property, easy to miss because it looks like an implementation "
                  "detail: a value is written once and never revised. If you find yourself "
                  "wanting to go back and improve `f` at a node already filled in, either the "
                  "ordering is wrong or the state is &mdash; and the second of those is the "
                  "subject of everything that follows."),
        ],
        "lab": ("dpseq", {
            "mode": "stages",
            "preset": "several",
            "panel_title": "Type a staged network and watch it fill from the last stage back",
            "panel_intro": "The table is filled backwards and every argmin is kept; the routes it "
                           "reconstructs are then priced again from the arcs, and every path is "
                           "walked forwards and priced independently. Nothing is shown as an "
                           "answer unless all three agree. This example has three optimal routes "
                           "and a tie at two different nodes. The example above it in the list is "
                           "the same network with one arc cost changed, and it has one optimal "
                           "route and a tie that lies off it; the one below adds an arc that "
                           "skips a stage.",
        }),
        "steps_title": "Filling a table backwards by hand",
        "steps_intro": "Five steps, and the last two are the ones people skip. Doing them in this order means you never revise a value.",
        "steps": [
            ("Check that every arc runs forward",
             "Stage numbers on the tail and the head, and the head's must be larger. If any arc "
             "fails this there is no last stage to start from and the recursion has no base "
             "case. The lab refuses such an arc by name rather than drawing it."),
            ("Set the last stage to zero and work leftwards",
             "One column at a time, right to left. Within a column the order does not matter, "
             "because nothing in a stage depends on anything else in it."),
            ("At each node, price every arc out of it and record every argmin",
             "`c(v,w) + f(w)` for each arc, then the minimum &mdash; and then a second pass for "
             "any other arc attaining it. Writing down only the first is where the ties go."),
            ("Reconstruct the routes by walking the argmins forward",
             "From the start, branching wherever a node has more than one argmin. This is the "
             "step that turns a table of numbers into something you can act on, and it is the "
             "step at which a reader discovers the answer is a set."),
            ("Price each reconstructed route again, from the arcs",
             "Add the arc costs along it and check the total against the value at the start. The "
             "recursion and the reconstruction are two pieces of arithmetic, and only the second "
             "one produces the thing you were actually asked for."),
        ],
        "worked": {
            "title": "The same network twice, one arc cost apart",
            "intro": [
                "Both tables below are filled from `F` back. Only the cost of `A>B` differs, and "
                "only the last line of each table does."
            ],
            "lines": [
                "stages   A ; B C ; D E ; F",
                "         A>C 4   B>D 7   B>E 4   C>D 3   C>E 2   D>F 1   E>F 4",
                "",
                "                             A>B 0                 A>B 2",
                "",
                "   f(F)                        0                     0",
                "   f(D) = 1 + f(F)             1                     1",
                "   f(E) = 4 + f(F)             4                     4",
                "   f(B) = min(7+1, 4+4)        8  tie D,E             8  tie D,E",
                "   f(C) = min(3+1, 2+4)        4                     4",
                "   f(A)                  min(0+8, 4+4) = 8     min(2+8, 4+4) = 8",
                "                               tie B,C              C only",
                "",
                "   optimal routes              A B D F               A C D F",
                "                               A B E F",
                "                               A C D F",
                "",
                "   all four paths walked forwards, priced from the arcs:",
                "",
                "      A B D F                    8                    10",
                "      A B E F                    8                    10",
                "      A C D F                    8                     8",
                "      A C E F                   10                    10",
                "",
                "   value at the start            8                     8",
                "   optimal routes           3 of 4                1 of 4",
                "   nodes with a tie          B, A                     B",
            ],
            "after": [
                "The two columns agree on the answer and disagree on how many answers there are. "
                "Nothing in the number 8 carries that difference, and neither does the drawing "
                "unless the ties are drawn &mdash; which is why the lab colours a tied arc "
                "differently from a chosen one and reports the tied nodes as a field of their own.",
                "For a rehearsal, put `A>B` back to 0 and change `D>F` from 1 to 2 instead. Work "
                "out by hand what happens to `f(D)`, `f(B)`, `f(C)` and `f(A)`, and how many "
                "optimal routes survive, before you let the lab tell you. The answer is still 8 "
                "and there is now exactly one route; the third rehearsal below is the one that "
                "goes the other way.",
                "The harder rehearsal: add an arc from `A` straight to `F` and give it a cost of "
                "9, then 8, then 7. At 9 nothing changes; at 8 the set of optimal routes grows by "
                "one; at 7 every other route stops being optimal and the answer becomes a single "
                "arc. Three regimes, one number, and the recursion never needed to be told that "
                "the arc skipped two stages.",
            ],
        },
        "quiz_title": "Values, routes, and what a tie is",
        "quiz": [
            {"q": "The recursion has filled in `f` at every node and `f` at the start is 8. What does the table tell you about the route?",
             "a": ["The route, since each value records the step that produced it",
                   "Nothing directly: the table holds one number per node, and the routes are reconstructed afterwards from the argmins",
                   "The first arc of the route, and nothing beyond it",
                   "The route, provided no two arcs have the same cost"],
             "c": 1,
             "why": "A value is a total from that node onward, not a plan. Reconstruction walks "
                    "the argmins forward from the start, and because a node can have several "
                    "argmins the result can be several routes &mdash; on the network in the lab "
                    "it is three."},
            {"q": "A node has two arcs out of it attaining the same minimum. What follows?",
             "a": ["The network has been entered wrongly, since an optimum is unique",
                   "One of the two can be discarded, because they are worth the same",
                   "It may or may not matter: the tie means two best answers only if that node lies on an optimal route",
                   "The value at that node has to be recomputed with a tie-break rule"],
             "c": 2,
             "why": "Both networks in the worked example have a tie at the same node. In one of "
                    "them that node is on an optimal route and there are three best answers; in "
                    "the other it is not and there is one. Discarding the tie gives the same "
                    "printed output for both, which is exactly the defect."},
            {"q": "Why must the table be filled from the last stage backwards rather than from the start forwards?",
             "a": ["Because arcs may skip stages, and a forward pass cannot handle that",
                   "Because `f(v)` is defined from the values of the nodes `v` reaches, so those must already be settled",
                   "Because the costs could be negative",
                   "Because a forward pass would visit some nodes twice"],
             "c": 1,
             "why": "The definition is the constraint. `f(v) = min` of `c(v,w) + f(w)`, so every "
                    "`f(w)` has to be final before `f(v)` is written, and only the last stage has "
                    "a value that needs nothing. An arc that skips a stage is handled by the same "
                    "rule with no special case, because its head is still in a later stage."},
            {"q": "The lab walks every path forwards as well as running the recursion. What is that second computation for?",
             "a": ["It is a faster method for small networks",
                   "It is an independent oracle: it never forms a value for a node, so it cannot repeat the recursion's mistake",
                   "It finds routes the recursion cannot reach",
                   "It is what produces the drawing"],
             "c": 1,
             "why": "It prices whole paths and never writes `f` anywhere, so it shares no "
                    "arithmetic with the thing it is checking. It is exponential on purpose and "
                    "the page refuses to show an answer when the two disagree. Treating it as a "
                    "second algorithm would undo the lesson, which is that pricing each node once "
                    "beats pricing each path once."},
        ],
        "mistakes": [
            ("Recording the first argmin and calling it the argmin",
             "This is the defect that survives every check. The value is right, the route printed "
             "is a genuinely optimal route, and the page looks finished &mdash; it has simply "
             "stopped saying that there are others. On the network in the lab it turns three "
             "correct answers into one, and a reader who later needs a second-best route, or has "
             "a tie-break criterion the model did not include, has been quietly deprived of the "
             "thing they needed."),
            ("Trying to fill the table forwards",
             "A forward pass computes, for each node, the cheapest way to <em>reach</em> it. That "
             "is a perfectly good quantity and it is not this one, and the two coincide only "
             "because a shortest path is reversible. The moment the arcs mean something "
             "asymmetric &mdash; an action taken, an amount spent &mdash; the forward quantity "
             "answers a different question. Fill backwards and the definition keeps you honest."),
            ("Believing the saving is about this network",
             "Six values against four paths is not a saving and the lab says so. The reason to "
             "care is the shape: add a stage with `k` nodes and the paths multiply by something "
             "like `k` while the values grow by `k`. At the sizes on this page you can check the "
             "recursion by hand against the enumeration, which is the only reason the enumeration "
             "is there."),
        ],
        "standard": ("Finish when you can fill a small staged network backwards, list every optimal route, and say which nodes have ties and whether those ties matter.",
                     "You should be able to write `f` at each node from the last stage back, "
                     "record every argmin rather than one, reconstruct the routes by walking "
                     "forward, price each of them again from the arcs, and explain why changing "
                     "a single arc cost can change the number of optimal routes without changing "
                     "the answer."),
        "note": 'Everything here was solved on a network somebody else had already drawn: the stages were given, so the hardest modelling decision on this course had already been made. The next lesson, &ldquo;The State Is What Is Left&rdquo;, takes that away. There is no network in it until you build one, the nodes have to be invented, and the whole difficulty moves from the arithmetic to the question of what a node should mean.',
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-state-is-what-is-left",
        "title": "The State Is What Is Left",
        "module": "The recursion, backwards",
        "one_line": "Split indivisible units across activities by building the network from a return table, and watch a rule that looks only at the next unit lose by six.",
        "summary": (
            "Nobody hands you the stages. Here the data are a table &mdash; what each activity "
            "returns for nothing, one unit, two units and so on &mdash; and before anything can "
            "be solved a network has to be invented from it. The invention is the lesson: a node "
            "is how much is still unspent when an activity has to decide, which is a statement "
            "about what the future needs to know. Once that is settled the arithmetic is the "
            "previous page again."
        ),
        "key": [
            "a state is what the FUTURE needs to know, not a record of what has happened",
            "here that is: how many units are still unspent when this activity decides",
            "stage = the activity deciding;  node = units left;  arc = units this one takes",
            "P 0 2 4 15 16 ; Q 0 6 8 9 10 ; R 0 3 7 8 9,  four units:   best return 21",
            "20 state values against 35 splits, and the two agree exactly",
            "taking the best NEXT unit each time gives 15, and it is not an arithmetic error",
        ],
        "key_label": "The table, the network built from it, and the two numbers that must agree",
        "concepts_intro": (
            "Three ideas. The first is a definition, the second is a construction, and the third "
            "is the failure the construction exists to avoid."
        ),
        "concepts": [
            ("A state is a claim that two situations can be finished identically",
             "Saying &ldquo;the state is the number of units left&rdquo; asserts that any two "
             "histories leaving the same number unspent have exactly the same future open to "
             "them. Here that is true, because the activities that remain do not care which of "
             "the earlier ones took what. If the return of a later activity depended on an "
             "earlier choice, the claim would be false and the table would be answering a "
             "different question &mdash; correctly, and about the wrong problem."),
            ("The network is built, not typed",
             "There is no picture in the data. One stage per activity plus a finish; one node in "
             "each stage for each amount that could still be unspent; and one arc for each amount "
             "this activity could take, carrying that amount's return. With three activities and "
             "four units that is 20 nodes, and the lab draws them as a grid so that the state "
             "space is a thing you can see rather than a phrase."),
            ("A rule that looks one unit ahead is solving a smaller problem",
             "The tempting shortcut is to hand out units one at a time, each to whichever "
             "activity gains most from the next one. It is fast, it is what a marginal argument "
             "suggests, and on the instance in the lab it returns 15 against the recursion's 21. "
             "Nothing about its arithmetic is wrong. It is choosing among the wrong set of "
             "plans, because it cannot pay for two poor units in order to reach a third good "
             "one."),
        ],
        "read_title": "Inventing the nodes, and then solving the thing you invented",
        "read_intro": "The data, the state, the network it forces, and the rule that gets this wrong for a reason worth understanding.",
        "body": [
            ("def", ("An allocation problem, and its state",
                     "Given activities `1` to `n`, a whole number `u` of indivisible units to "
                     "hand out, and a <strong>return table</strong> giving `rᵢ(x)` for each "
                     "activity `i` and each whole `x` from 0 up, choose `x₁, ..., xₙ` with "
                     "`Σ xᵢ ≤ u` maximising `Σ rᵢ(xᵢ)`.",
                     "The <strong>state</strong> before activity `i` decides is the number of "
                     "units still unspent. The value function is `g(i, s) = max` over `x` from 0 "
                     "to `s` of `rᵢ(x) + g(i+1, s−x)`, with `g(n+1, s) = 0` for every `s`: once "
                     "there are no activities left, what remains is worth nothing.")),
            ("p", "Two things about that definition are worth saying out loud. The first is that "
                  "`rᵢ(0)` must be 0 &mdash; a table whose first column is not zero is measuring "
                  "something other than a return, and the lab refuses it by name. The second is "
                  "that nothing anywhere records which activity took what; the state is a single "
                  "number. That is not an economy, it is the modelling claim, and it is the thing "
                  "to check before trusting any answer the table produces."),
            ("math", [
                "the table                      units:  0   1   2    3    4",
                "",
                "   P                                   0   2   4   15   16",
                "   Q                                   0   6   8    9   10",
                "   R                                   0   3   7    8    9",
                "",
                "the network it forces, with four units to hand out:",
                "",
                "   stage P        stage Q        stage R         done",
                "   4 left  --2u->  2 left  --1u->  1 left  --1u->  0 left",
                "   3 left          1 left         0 left",
                "   2 left          0 left",
                "   1 left",
                "   0 left",
                "",
                "   an arc from  s left  to  s-x left  carries the return of x units",
                "   5 nodes per stage, 4 stages:  20 state values in all",
            ]),
            ("p", "Filled from the finish back, the last column is zero everywhere, `R`'s column "
                  "is just its own returns, `Q`'s column combines its returns with `R`'s, and "
                  "`P`'s column combines all three. The value at the node marked <em>4 left</em> "
                  "in `P`&rsquo;s column is 21, attained by `P` taking 3, `Q` taking 1 and `R` "
                  "taking none. The lab prices all 35 ways of splitting four units across three "
                  "activities and finds 21 as well, attained by exactly that split and no other."),
            ("h3", "The rule that looks at the next unit"),
            ("p", "Hand out the units one at a time. The first unit goes to `Q`, which gains 6 "
                  "against `P`'s 2 and `R`'s 3. The second goes to `R` at 3, since `Q`'s next "
                  "unit gains only 2 and `P`'s still gains 2. The third goes to `R` again at 4. "
                  "The fourth is a tie among gains of 2, and whichever way it falls the total is "
                  "15. Every one of those comparisons is correct and the answer is six short."),
            ("example", ("Why it loses, in one line",
                         "`P`'s returns are 0, 2, 4, 15, 16, so its first two units gain 2 each "
                         "and its third gains 11. A rule that asks only what the next unit is "
                         "worth never sees the 11, because it never gets past the two units of 2 "
                         "that stand in front of it.",
                         "The recursion sees it because it never asks about a unit at all: it "
                         "asks what `P` should take given how much is left, and 3 is one of the "
                         "options it prices. That is the difference between choosing a decision "
                         "and choosing an increment, and the table's jump is there to make it "
                         "visible rather than arguable.")),
            ("h3", "Diminishing returns, and the tie that appears"),
            ("p", "Switch to the example whose three activities all have non-increasing "
                  "marginal returns and the shortcut stops losing: the greedy split and the "
                  "recursion both reach 19. But look at what the enumeration says about that 19. "
                  "There are two splits attaining it &mdash; one unit to `P`, two to `Q`, one to "
                  "`R`, and two to `P`, one to `Q`, one to `R` &mdash; so even in the friendly "
                  "case the answer is a set, and a page printing one of them would be printing a "
                  "choice the model never made."),
            ("p", "That is the same point as the ties on the previous page, arriving from a "
                  "different direction, and it is why the lab prints both the route the recursion "
                  "reconstructed and every split the enumeration found. Where the two examples "
                  "differ is in what the tie costs you. A tie among optimal routes is a free "
                  "choice; the shortcut's failure is not a tie at all, it is a worse answer that "
                  "looks like a method."),
            ("h3", "What the state left out"),
            ("p", "The model here says that four units handed to `P`, `Q` and `R` in any order "
                  "are worth the sum of three table lookups. That rules out a great deal: no "
                  "activity can make another cheaper, no unit can be split, no combination can be "
                  "forbidden, and nothing costs anything to set up. Each of those, if true of the "
                  "situation, is a state the model does not carry &mdash; and the recursion would "
                  "still return an exact optimum, of the problem it was given."),
            ("p", "Two activities rather than three is worth a minute, because the whole table "
                  "fits on one line: with `P` at 0, 7, 11, 14, 15 and `Q` at 0, 5, 10, 13, 16, "
                  "four units split two and two return 21, out of 15 possible splits. Small "
                  "enough to check every one of them by hand, which is the only way to be sure "
                  "the recursion is not being believed rather than checked."),
        ],
        "lab": ("dpseq", {
            "mode": "allocation",
            "preset": "lumpy",
            "panel_title": "Build the network from the table, and check the split against every other split",
            "panel_intro": "There is nothing to draw here until the state is chosen. A node is "
                           "how many units are still unspent when an activity has to decide, an "
                           "arc is how many that activity takes, and the drawing is what those "
                           "two sentences produce. The recursion fills it backwards; every "
                           "possible split is then priced directly from the table, with no "
                           "network involved, and both numbers are shown. This example is the "
                           "one where an activity is nearly worthless until its third unit.",
        }),
        "steps_title": "Turning a table into a network you can solve",
        "steps_intro": "The first two steps are the whole of the difficulty, and neither of them is arithmetic.",
        "steps": [
            ("Say what the future needs to know, in a sentence",
             "Not what has happened &mdash; what still matters. Here: how much is left. Then test "
             "the sentence by finding two different histories it calls the same state, and asking "
             "whether they really do have the same options from here on."),
            ("Make the stages the decisions, in any fixed order",
             "One stage per activity. The order is yours to choose and the answer does not depend "
             "on it, which is itself worth checking on a small instance: reorder the activities "
             "in the lab and the optimum does not move, though the table does."),
            ("Draw one node per reachable state and one arc per decision",
             "From <em>s left</em> in stage `i` there is an arc to <em>s−x left</em> in stage "
             "`i+1` for every `x` from 0 to `s`, carrying `rᵢ(x)`. Every arc runs forward by "
             "construction, so the recursion applies unchanged."),
            ("Fill from the last stage back, maximising rather than minimising",
             "The finish is worth zero in every state. Nothing else about the method changes: "
             "the direction of the comparison is a parameter, not a different algorithm."),
            ("Check the value against the enumeration before reading the split",
             "There are `C(u+n, n)` splits &mdash; the units need not all be spent &mdash; which is "
             "35 here, and the lab prices all of them. "
             "If the two numbers agree, read the split off the argmins; if they do not, the "
             "network you built is not the problem you meant."),
        ],
        "worked": {
            "title": "The recursion, and the rule that looks one unit ahead",
            "intro": [
                "Four units, three activities, the table with the jump in it. The left column is "
                "the recursion filled from `R` back; the right is the marginal rule, step by step."
            ],
            "lines": [
                "table            0   1   2    3    4          marginal gains",
                "   P             0   2   4   15   16            2   2  11   1",
                "   Q             0   6   8    9   10            6   2   1   1",
                "   R             0   3   7    8    9            3   4   1   1",
                "",
                "THE RECURSION, filled from the end",
                "",
                "   stage R      0 left 0   1 left 3   2 left 7   3 left 8   4 left 9",
                "   stage Q      0 left 0   1 left 6   2 left 9   3 left 13  4 left 15",
                "                            take 1     take 1     take 1     take 2",
                "   stage P      4 left  max( 0+15 , 2+13 , 4+9 , 15+6 , 16+0 ) = 21",
                "                                                   ^^^^^^ P takes 3",
                "",
                "   best return 21     split  P=3  Q=1  R=0",
                "   35 splits priced directly from the table:  best 21, the same split, only one",
                "",
                "THE MARGINAL RULE, one unit at a time",
                "",
                "   unit 1   gains  P 2   Q 6   R 3      -> Q      running total  6",
                "   unit 2   gains  P 2   Q 2   R 3      -> R      running total  9",
                "   unit 3   gains  P 2   Q 2   R 4      -> R      running total 13",
                "   unit 4   gains  P 2   Q 2   R 1      -> P      running total 15",
                "",
                "   its answer 15        the optimum 21        every comparison correct",
            ],
            "after": [
                "The fourth line of the marginal rule is the one to stare at. `P`'s next unit is "
                "worth 2 and the rule duly treats `P` as the weakest of the three, at the exact "
                "moment when `P` holding three units would be worth 15. The rule is not "
                "approximating the optimum; it is optimising over a smaller set of plans, the "
                "ones reachable by never regretting a unit.",
                "For a rehearsal, change `P`'s table to 0, 2, 4, 6, 16 &mdash; a jump at the "
                "fourth unit instead of the third &mdash; and predict both answers before "
                "running anything. The recursion has to be willing to give `P` everything, and "
                "the marginal rule never will.",
                "The harder rehearsal: build a table on which the marginal rule and the recursion "
                "agree at four units and disagree at five. It exists, it is not hard to find once "
                "you look for the jump, and constructing one is a better test of whether the "
                "failure is understood than any number of instances where the rule happens to "
                "win.",
            ],
        },
        "quiz_title": "States, networks and marginal rules",
        "quiz": [
            {"q": "Why is &ldquo;how many units are still unspent&rdquo; a state, while &ldquo;which activities have already been given something&rdquo; is not?",
             "a": ["Because it is a smaller piece of information to carry",
                   "Because the activities still to decide have the same options from any history leaving the same amount unspent",
                   "Because the returns are non-negative",
                   "Because the activities are considered in a fixed order"],
             "c": 1,
             "why": "A state is a claim that two histories can be finished identically. Here the "
                    "later activities' returns depend only on what they take and what is "
                    "available, so the claim holds. If a later return depended on an earlier "
                    "choice, the claim would be false, the table would still fill in, and the "
                    "answer would be exactly wrong."},
            {"q": "A rule hands out units one at a time, each to the activity whose next unit gains most. On the table in the lab it returns 15 against the optimum of 21. What went wrong?",
             "a": ["An arithmetic slip in one of the comparisons",
                   "The rule broke a tie the wrong way",
                   "Nothing in its arithmetic: it optimises over a smaller set of plans and cannot pay for two poor units to reach a good one",
                   "It should have been run backwards"],
             "c": 2,
             "why": "Every comparison it makes is correct. The activity in question gains 2, then "
                    "2, then 11, and the rule never reaches the 11 because it will not accept two "
                    "gains of 2 first. Choosing an increment and choosing a decision are "
                    "different problems, and only one of them is the one asked."},
            {"q": "The lab reports 20 state values and 35 splits on this instance. What is that comparison there to show?",
             "a": ["That the recursion is about a third faster here",
                   "That the enumeration is unnecessary",
                   "That the two counts grow differently &mdash; states with the units, splits with the units raised to a power &mdash; while being small enough here to check one against the other",
                   "That the state space has been chosen badly, since it should be smaller than the number of splits by more"],
             "c": 2,
             "why": "At this size the saving is nearly nothing and that is deliberate: 35 splits "
                    "can be priced and read. The point is the shape of the growth, and the reason "
                    "the enumeration is on the page at all is that it can still be checked "
                    "against the recursion by eye."},
            {"q": "On the example with three non-increasing return tables, the recursion reports 19 and the enumeration finds two different splits attaining it. What should the page print?",
             "a": ["Whichever split the recursion found first, since they are worth the same",
                   "Both, because the answer is a set and printing one of them presents a choice the model did not make",
                   "Neither, since the answer is ambiguous",
                   "The average of the two splits"],
             "c": 1,
             "why": "Two splits at 19 is the same situation as two optimal routes on a network: "
                    "the value is unique, the plan is not, and any tie-break is a criterion from "
                    "outside the model. The lab prints every optimal split it finds, up to the "
                    "handful it has room for."},
        ],
        "mistakes": [
            ("Making the state a record of the past",
             "&ldquo;Activity `P` has been given two units&rdquo; is history, not state. It is "
             "sometimes necessary &mdash; if a later return depends on it, it belongs in the "
             "state &mdash; but reaching for it by default makes the state space explode for no "
             "reason, and it hides the question you should be asking, which is whether the "
             "future really depends on it. Write the sentence about the future first."),
            ("Reading a marginal rule as an approximation",
             "It is not solving this problem slightly worse; it is solving a different problem "
             "exactly. The set of plans reachable by handing out units one at a time, never "
             "revisiting, is a strict subset of all splits, and it excludes exactly the ones that "
             "pay upfront. Calling the gap an approximation error suggests it shrinks with care, "
             "and it does not."),
            ("Trusting the reconstruction without the enumeration",
             "The recursion's value and the split it reconstructs are two different pieces of "
             "arithmetic, and the second one involves walking argmins through a network that was "
             "itself generated. The lab prices every split directly from the table for exactly "
             "this reason, and shows nothing as an answer until the two agree. At 35 splits that "
             "check is free; the habit is what has to survive to larger instances."),
        ],
        "standard": ("Finish when you can take a return table, state what a node means in one sentence, build the network, and say why a rule that looks at the next unit is not an approximation.",
                     "You should be able to justify the state as a claim about the future, "
                     "construct the stages and arcs from the table alone, fill the values "
                     "backwards while maximising, reconstruct every optimal split, and reproduce "
                     "the instance on which a marginal rule returns 15 where the optimum is 21."),
        "note": 'The state here was a single number and the choice of it was almost forced. That will not last. The next lesson, &ldquo;Wagner-Whitin and the Order Intervals&rdquo;, has a state that is genuinely surprising the first time &mdash; not the stock on hand, which is what everybody reaches for, but the period the last order was placed in &mdash; and the reason that works is a small theorem about what an optimal plan never does.',
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "wagner-whitin-and-the-order-intervals",
        "title": "Wagner-Whitin and the Order Intervals",
        "module": "Ordering over time",
        "one_line": "A small theorem about what an optimal plan never does turns a schedule of quantities into a partition into intervals, and the recursion solves the partition.",
        "summary": (
            "Demand is known period by period, an order costs a fixed charge whatever its size, "
            "and stock costs something to hold. The decision looks like a quantity per period, "
            "which is a continuum, until one observation collapses it: an optimal plan never "
            "orders while stock remains. That makes a plan a partition of the periods into "
            "consecutive intervals, each covered by one order, and the recursion runs over the "
            "period the last order was placed in rather than over the stock on hand."
        ),
        "key": [
            "an optimal plan never orders while stock remains, so it never holds and orders at once",
            "therefore a plan IS a partition of 1..T into consecutive order intervals",
            "F(t) = min over j from 1 to t of [ F(j-1) + K + h x (holding from j to t) ]",
            "demand 10 62 12 130 154 129,  K = 54,  h = 2",
            "F: 0, 54, 108, 132, 186, 240, 294      and the cheapest plan costs 294",
            "2^(T-1) = 32 order patterns, all of them priced, and none beats 294",
        ],
        "key_label": "One observation, and the recursion it makes possible",
        "concepts_intro": (
            "The theorem first, because without it there is no recursion; then the state it "
            "licenses, then the check that keeps the reconstruction honest."
        ),
        "concepts": [
            ("An optimal plan never orders while stock remains",
             "Suppose it did: some period `t` has stock left over from an earlier order and "
             "places a new order as well. Move the quantity that period `t` orders for its own "
             "demand back into the earlier order, or move the leftover stock forward by "
             "cancelling part of the earlier order &mdash; one of the two saves holding cost "
             "without adding a setup, and neither can cost more. So an order always covers a "
             "whole run of consecutive periods, ending exactly where the next order begins."),
            ("So the state is when the last order was, not what is in stock",
             "Stock on hand is the obvious state and it is a poor one: it takes many values and "
             "most of them are unreachable. The theorem says the only thing the future needs to "
             "know is where the current interval started, so `F(t)`, the cheapest way to cover "
             "periods 1 through `t` exactly, is enough &mdash; one number per period, and the "
             "decision in each row is which period the last order went in."),
            ("Reconstructing the plan is a second computation",
             "`F(T)` is the cost. The plan is recovered by following the argmins back: the last "
             "order went in period `j`, so the one before it covers 1 through `j−1`, and so on. "
             "That chain is separate arithmetic from the table, so the lab re-prices what it "
             "produces &mdash; setup by setup and unit-period by unit-period &mdash; and puts "
             "the total beside `F(T)`."),
        ],
        "read_title": "From a quantity per period to a partition into intervals",
        "read_intro": "The theorem, the table it makes possible, and the plan read back out of the argmins.",
        "body": [
            ("def", ("The lot-sizing problem",
                     "Demands `d₁, ..., d_T` are known. An order placed in period `t` arrives in "
                     "time for period `t` and costs a fixed <strong>setup charge</strong> `K` "
                     "whatever its size. Stock carried from one period into the next costs `h` "
                     "per unit per period. Shortages are not allowed and there is no stock at "
                     "the start or required at the end.",
                     "A <strong>plan</strong> says how much to order in each period. Its cost is "
                     "`K` times the number of orders, plus `h` times the total unit-periods of "
                     "holding.")),
            ("thm", ("An optimal plan orders only when stock has run out",
                     "There is an optimal plan in which every order arrives in a period that "
                     "begins with nothing in stock. Consequently every order covers a "
                     "consecutive run of periods, the runs partition `1` through `T`, and the "
                     "quantity ordered at the start of a run is exactly the demand over that run.",
                     "So the search is over the `2^(T−1)` ways of choosing where the runs break "
                     "&mdash; one binary choice at each of the `T−1` boundaries &mdash; rather "
                     "than over quantities.")),
            ("proof", [
                "Take an optimal plan and suppose period `t` both begins with stock `s > 0` and "
                "places an order of size `q > 0`. Let `ε` be the smaller of `s` and `q`.",
                "Reduce the earlier order by `ε` and increase period `t`'s order by `ε`: the "
                "number of orders is unchanged or falls by one, and `ε` units are held for fewer "
                "periods, so holding cost strictly falls. The plan is no more expensive.",
                "Repeat while any period both holds and orders. Each step removes at least one "
                "such period and never creates one, so the process ends, and it ends at a plan "
                "that is optimal and orders only into an empty stock.",
            ]),
            ("p", "That is the whole of the modelling work. What is left is the recursion, and "
                  "it is the one from &ldquo;Filling the Table from the End&rdquo; with the stages "
                  "relabelled: let `F(t)` be "
                  "the cheapest way to cover periods 1 through `t` exactly, with `F(0) = 0`. The "
                  "last order in such a plan went in some period `j`, covering `j` through `t`, "
                  "so `F(t)` is the smallest over `j` of `F(j−1)` plus `K` plus the holding on "
                  "the run `j` to `t`. Holding on that run is `h` times `Σ (i − j) dᵢ`, because "
                  "period `i`'s demand sits in stock for `i − j` periods."),
            ("math", [
                "demand    d1..d6 = 10  62  12  130  154  129        K = 54     h = 2",
                "",
                "F(0) = 0",
                "F(1) = 54                                                 order at 1",
                "F(2) = min( 178 , 108 )                       = 108       order at 2",
                "F(3) = min( 226 , 132 , 162 )                 = 132       order at 2",
                "F(4) = min( 1006 , 652 , 422 , 186 )          = 186       order at 4",
                "F(5) = min( 2238 , 1576 , 1038 , 494 , 240 )  = 240       order at 5",
                "F(6) = min( 3528, 2608, 1812, 1010, 498, 294 ) = 294      order at 6",
                "",
                "reading the argmins backwards from t = 6:",
                "",
                "   last order at 6, covering 6        so F(5) is next",
                "   last order at 5, covering 5        so F(4) is next",
                "   last order at 4, covering 4        so F(3) is next",
                "   last order at 2, covering 2 to 3   so F(1) is next",
                "   last order at 1, covering 1",
                "",
                "   five orders:  10 in p1,  74 in p2,  130 in p4,  154 in p5,  129 in p6",
            ]),
            ("p", "Five orders at 54 each is 270, and the plan's holding is 24 &mdash; the whole "
                  "of it is period 3's demand of 12 carried one period at 2 per unit &mdash; so "
                  "294. The lab prices the plan again that way, from the demand and the two "
                  "charges rather than from `F`, and prints the result beside the recursion's. "
                  "It also enumerates all 32 order patterns and prices each of them; the best is "
                  "294 and it breaks at the same places."),
            ("h3", "Why the argmin column is worth more than the value column"),
            ("p", "Look at the row for `F(4)`. The candidates are 1006, 652, 422 and 186, and "
                  "the last of them wins by a wide margin: covering period 4's demand of 130 "
                  "from any earlier order means carrying 130 units for at least one period at 2 "
                  "each, which is 260 on its own against a setup charge of 54. The value column "
                  "tells you the answer; the argmin column tells you why, and it is where the "
                  "structure of the instance is visible."),
            ("example", ("Flat demand, and the block structure",
                         "Set every demand to 40, the setup to 90 and the holding rate to 1. The "
                         "table comes out 0, 90, 130, 210, 260, 340, 390, the plan is three "
                         "orders of 80 covering periods 1 to 2, 3 to 4 and 5 to 6, and the cost "
                         "is 390.",
                         "Even blocks, because nothing distinguishes one period from another. "
                         "Now move the setup charge up and down with the slider and watch where "
                         "the breaks go: raise it and the intervals lengthen, raise the holding "
                         "rate instead and they shorten. The plan is the balance of the two and "
                         "neither alone decides it.")),
            ("example", ("One period that dwarfs the rest",
                         "Demands 8, 6, 200, 7, 9, 5 with a setup of 60 and a holding rate of 3. "
                         "The cheapest plan costs 234 with three orders, and the middle one is "
                         "placed in period 3 itself.",
                         "Carrying 200 units even one period would cost 600, which is ten setup "
                         "charges, so no optimal plan holds that demand at all. The instance is "
                         "worth meeting because it shows the theorem doing real work: the search "
                         "is over partitions, and this one is forced to break just before "
                         "period 3.")),
            ("h3", "What the model left out"),
            ("p", "Demand is known exactly, and known in advance for the whole horizon. Orders "
                  "arrive instantly. Shortages are impossible rather than expensive. There is no "
                  "capacity on an order and no minimum size, no discount for ordering more, and "
                  "the setup charge is the same in every period. Each of those is a real feature "
                  "of real ordering and each of them is absent here; several of them would break "
                  "the theorem rather than merely complicate the arithmetic, which is the sort of "
                  "omission worth knowing about before quoting a plan."),
        ],
        "lab": ("dpseq", {
            "mode": "lotsize",
            "preset": "classic",
            "panel_title": "Move the two charges and watch the intervals move",
            "panel_intro": "The recursion is over the period the last order was placed in, not "
                           "over the stock on hand. Every row shows each candidate priced, so "
                           "the argmin is visible rather than asserted; the plan it returns is "
                           "then priced again from the demand and the two charges; and all "
                           "`2ᵀ⁻¹` order patterns are enumerated and priced as a third witness. "
                           "Nothing is shown as an answer unless the three agree.",
        }),
        "steps_title": "Filling the F table",
        "steps_intro": "Four steps. The third is the one worth writing out in full the first few times, because it is where the holding arithmetic hides.",
        "steps": [
            ("Set F(0) = 0 and take the periods in order",
             "`F(0) = 0` says that covering nothing costs nothing. Every later row depends only "
             "on earlier rows, so one pass left to right finishes it."),
            ("For each t, try every period j the last order could have gone in",
             "That is `j` from 1 to `t`. Each choice splits the problem into &ldquo;cover 1 to "
             "`j−1` optimally&rdquo;, which is `F(j−1)` and already known, and &ldquo;one order "
             "covering `j` to `t`&rdquo;."),
            ("Price the interval as K plus h times the unit-periods",
             "Demand in period `i` covered by an order in period `j` waits `i − j` periods, so "
             "the holding is `h` times `Σ (i − j) dᵢ` over the interval. The demand in period `j` "
             "itself contributes nothing, which is the term people drop."),
            ("Record the minimum and the period that attained it",
             "Both columns. The values give the cost; the argmins give the plan, read backwards "
             "from `t = T`."),
            ("Re-price the reconstructed plan from the demand",
             "Setup charges plus holding, computed from scratch. If it does not equal `F(T)` the "
             "reconstruction is wrong even though the table is right, and that failure has a "
             "completely different cause from an arithmetic slip in the table."),
        ],
        "worked": {
            "title": "One table, one plan, and thirty-two patterns",
            "intro": [
                "The candidates in each row of `F`, then the plan read back out of the argmins, "
                "then the same answer reached by pricing every way of breaking the six periods "
                "into intervals."
            ],
            "lines": [
                "demand  10  62  12  130  154  129        K = 54      h = 2",
                "",
                "t   each candidate F(j-1) + K + holding(j..t)              F(t)   order at",
                "",
                "1   j=1  0 + 54 + 0                            =   54       54      1",
                "2   j=1  0 + 54 + 2(62)          = 178",
                "    j=2  54 + 54 + 0             = 108                     108      2",
                "3   j=1  0 + 54 + 2(62 + 24)     = 226",
                "    j=2  54 + 54 + 2(12)         = 132                     132      2",
                "    j=3  108 + 54 + 0            = 162",
                "4   j=3  108 + 54 + 2(130)       = 422",
                "    j=4  132 + 54 + 0            = 186                     186      4",
                "5   j=5  186 + 54 + 0            = 240                     240      5",
                "6   j=6  240 + 54 + 0            = 294                     294      6",
                "",
                "the plan, read backwards from t = 6:",
                "",
                "   ordered in   quantity   covering       setup   holding   total",
                "   period 1         10     period 1          54         0      54",
                "   period 2         74     periods 2 to 3    54        24      78",
                "   period 4        130     period 4          54         0      54",
                "   period 5        154     period 5          54         0      54",
                "   period 6        129     period 6          54         0      54",
                "   in all                                   270        24     294",
                "",
                "   all 32 order patterns priced:  best 294, breaking at 1, 2, 4, 5, 6",
            ],
            "after": [
                "The only holding in the whole plan is 12 units carried one period, and it buys "
                "the saving of one setup charge: 24 against 54. Every other pair of adjacent "
                "periods has too much demand in the later one for that trade to pay, which is "
                "why the plan is four singletons and one pair rather than something tidier.",
                "For a rehearsal, drop the setup charge to 20 and predict the plan before "
                "running it. With setups cheap relative to holding, the intervals should shrink "
                "to singletons everywhere; check whether they actually do, and find the first "
                "charge at which periods 2 and 3 separate.",
                "The harder rehearsal: the enumeration is `2ᵀ⁻¹`, which at six periods is 32 and "
                "at thirteen is 4096. The recursion prices `T(T+1)/2` candidates, which is 21 at "
                "six periods and 91 at thirteen. Work out roughly where on that curve an "
                "enumeration stops being something a page can do, and notice that the recursion "
                "has not changed at all in the meantime.",
            ],
        },
        "quiz_title": "Intervals, states and what the theorem buys",
        "quiz": [
            {"q": "Why can the recursion be over &ldquo;the period the last order was placed in&rdquo; rather than over the stock on hand?",
             "a": ["Because stock is a continuous quantity and periods are discrete",
                   "Because an optimal plan never orders while stock remains, so every order covers a whole run of periods and the run's start is all the future needs",
                   "Because the demands are whole numbers",
                   "Because the setup charge does not depend on the quantity"],
             "c": 1,
             "why": "The exchange argument removes every plan that both holds and orders in the "
                    "same period. What is left is exactly the partitions into consecutive "
                    "intervals, so the only thing carried forward is where the current interval "
                    "began. Without that theorem the state would have to be the stock, and most "
                    "stock levels are unreachable anyway."},
            {"q": "An order placed in period `j` covers periods `j` through `t`. What is the holding cost of that order?",
             "a": ["`h` times the total demand from `j` to `t`",
                   "`h` times `Σ (i − j) dᵢ` for `i` from `j` to `t` &mdash; period `j`'s own demand contributes nothing",
                   "`h` times `Σ (i − j + 1) dᵢ`, since the stock is held during period `j` as well",
                   "`h` times `(t − j)` times the average demand"],
             "c": 1,
             "why": "Demand in period `i` waits `i − j` periods, and the demand the order arrives "
                    "for waits none. Adding one to every coefficient is the commonest slip and "
                    "it inflates every candidate by the same setup-like amount, which is why it "
                    "is easy to miss: the plan often comes out right and the cost never does."},
            {"q": "On the six-period instance, the lab reports 294 from the recursion, 294 from re-pricing the plan, and 294 from enumerating every pattern. Why is the middle one not redundant?",
             "a": ["It is redundant; two witnesses would do",
                   "Because the table's value and the plan reconstructed from the argmins are separate computations, and a right table can be read back wrongly",
                   "Because the enumeration might time out",
                   "Because the holding cost is easy to get wrong"],
             "c": 1,
             "why": "`F(T)` is a number; the plan is produced by a second walk through the "
                    "argmin column. A page could print a correct cost beside a plan that does "
                    "not achieve it, and every markup check would pass. Pricing the plan from "
                    "the demand catches exactly that."},
            {"q": "Demands are 8, 6, 200, 7, 9, 5 with `K = 60` and `h = 3`. Why does no optimal plan carry period 3's demand?",
             "a": ["Because 200 exceeds the order capacity",
                   "Because carrying 200 units one period costs 600, which is ten setup charges, so breaking the interval is always cheaper",
                   "Because an order must be placed in every period whose demand exceeds 100",
                   "Because the holding rate is higher than the setup charge"],
             "c": 1,
             "why": "It is an arithmetic comparison and nothing more: `3 × 200 = 600` against a "
                    "setup of 60. The theorem restricts the search to partitions; within that "
                    "search, this instance forces a break immediately before period 3, and the "
                    "argmin column shows it."},
        ],
        "mistakes": [
            ("Taking the stock on hand as the state",
             "It is the first thing everyone reaches for and it is a much worse state: it takes "
             "many values, most of them are never reached by any optimal plan, and it makes the "
             "table larger without making it more correct. The theorem is what licenses the "
             "smaller state, so if you cannot state the theorem you should not be using the "
             "small state &mdash; and the moment shortages or capacities enter, the theorem goes "
             "and the small state goes with it."),
            ("Charging holding on the demand the order arrives for",
             "An order placed in period `j` covers period `j` immediately, so period `j`'s own "
             "demand is never held. Writing `(i − j + 1)` instead of `(i − j)` adds `h` times "
             "the interval's whole demand to every candidate. Because it inflates all candidates "
             "in a row, the argmins often survive and the plan looks right while every number in "
             "the table is wrong."),
            ("Quoting the plan without saying demand was assumed known",
             "The entire construction depends on knowing `d₁` through `d_T` in advance. A rolling "
             "horizon, where the table is refilled each period as forecasts arrive, is a "
             "different thing and its plans are not optimal for any single problem. The "
             "arithmetic here cannot tell you which situation you are in, and it will produce a "
             "confident answer either way."),
        ],
        "standard": ("Finish when you can state the exchange argument, fill the F table with its argmin column, read the plan back out and price it independently.",
                     "You should be able to say why an optimal plan never holds and orders in "
                     "the same period, explain why that makes a plan a partition, write "
                     "`F(t)` as a minimum over the period of the last order, compute the holding "
                     "on an interval without the off-by-one, and reconstruct and re-price the "
                     "plan from the argmins."),
        "note": 'The answer above is exact, and it is exact about a schedule that nobody in practice fills in this way: the table needs the whole horizon in advance, and it is more work than the situation usually justifies. So two rules of thumb are used instead, and the honest question is what they cost. The next lesson, &ldquo;Silver-Meal and Least Unit Cost&rdquo;, traces both of them against this same recursion &mdash; on an instance where one of them happens to find the optimum, and on another where both miss, by different amounts, with different numbers of orders.',
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "silver-meal-and-least-unit-cost",
        "title": "Silver-Meal and Least Unit Cost",
        "module": "Ordering over time",
        "one_line": "Two rules of thumb that extend an order interval while an average is falling, traced against the exact answer on an instance where both of them lose.",
        "summary": (
            "Both rules build the plan left to right: start an interval, keep extending it while "
            "an average falls, stop when the average turns up, start again. They differ only in "
            "which average they watch &mdash; cost per period, or cost per unit &mdash; and that "
            "is enough to make them disagree with each other as well as with the exact answer. "
            "Neither dominates the other, and the instance that shows it has one of them paying "
            "24 too much with three orders and the other 30 too much with two."
        ),
        "key": [
            "Silver-Meal      extend while the average cost per PERIOD is falling",
            "least unit cost  extend while the average cost per UNIT is falling",
            "both stop at the first turn upwards, and neither can see past it",
            "demand 17 25 73 113 89,  K = 116,  h = 1:   exact 462",
            "   Silver-Meal 486, three orders, 24 too much",
            "   least unit cost 492, two orders, 30 too much",
            "demand 10 62 12 130 154 129,  K = 54,  h = 2:  exact 294, SM 294, LUC 600",
        ],
        "key_label": "Two averages, two stopping points, and what each one costs",
        "concepts_intro": (
            "Three ideas: what the rules do, why they can be wrong, and how to price the wrongness "
            "without trusting either rule's own bookkeeping."
        ),
        "concepts": [
            ("Both rules are myopic in the same way, and greedy in different ways",
             "Each starts an interval at the first uncovered period and extends it one period at "
             "a time, watching a running average. While the average falls, extending looks "
             "worthwhile; at the first increase the rule closes the interval and starts a new "
             "one at the next period. Neither ever revisits a decision, so a plan is built in one "
             "left-to-right sweep, and the whole question is which average is being watched."),
            ("Per period and per unit are different questions",
             "Silver-Meal divides the interval's total cost by the number of periods it covers; "
             "least unit cost divides it by the quantity ordered. When demand is rising sharply, "
             "adding a period adds a lot of quantity, so the per-unit average keeps falling long "
             "after the per-period average has turned up &mdash; which is exactly why least unit "
             "cost places fewer, longer orders on the instances here, and why the two rules "
             "disagree rather than one being a rough version of the other."),
            ("A heuristic's own cost figure is not evidence",
             "Each rule reports a total as it goes. That total is produced by the same code that "
             "chose the plan, so it cannot testify to it. The lab prices each plan again from "
             "the demand, the setup charge and the holding rate &mdash; the same function that "
             "prices the exact plan &mdash; so the comparison is between three plans measured "
             "with one instrument, which is the only kind of comparison worth making."),
        ],
        "read_title": "Two rules, traced, and then priced against the exact answer",
        "read_intro": "What each rule does step by step, the instance where one of them is lucky, and the instance where both of them are not.",
        "body": [
            ("def", ("Silver-Meal and least unit cost",
                     "Both rules build a plan by intervals. Starting at the first uncovered "
                     "period `t`, consider covering `t` through `t+k` for `k = 0, 1, 2, ...`. "
                     "The interval's cost is `K + h ×` its holding, and the rule compares a "
                     "running average as `k` grows.",
                     "<strong>Silver-Meal</strong> uses the average per period, "
                     "`(K + h × holding) / (k+1)`. <strong>Least unit cost</strong> uses the "
                     "average per unit, `(K + h × holding) / (quantity covered)`. Each extends "
                     "while its average strictly falls and closes the interval at the first "
                     "value that does not, then starts again at the next uncovered period.")),
            ("p", "Two things follow immediately. Both rules always terminate, because every "
                  "interval covers at least one period. And both are exact on the first interval "
                  "only in the sense that they stop where their own average stops &mdash; "
                  "neither has any notion of what happens after the interval it is currently "
                  "building, so neither can trade a worse interval now for a much better one "
                  "later. That is the failure mode, and it is structural rather than a matter "
                  "of tuning."),
            ("h3", "The instance where both of them miss"),
            ("math", [
                "demand  17  25  73  113  89        K = 116     h = 1",
                "",
                "EXACT (the recursion of the previous page)",
                "   orders at 1, 3, 4      covering 1-2, 3, 4-5",
                "   cost  141 + 116 + 205  =  462",
                "",
                "SILVER-MEAL, average per PERIOD",
                "   from 1:  116/1 = 116   141/2 = 70.5   287/3 = 95.66..   turned up, span 2",
                "   from 3:  116/1 = 116   229/2 = 114.5  407/3 = 135.66..  turned up, span 2",
                "   from 5:  116/1 = 116                                    last period, span 1",
                "   plan  1-2, 3-4, 5      cost  141 + 229 + 116  =  486     three orders",
                "",
                "LEAST UNIT COST, average per UNIT",
                "   from 1:  116/17 = 6.82   141/42 = 3.357   287/115 = 2.496   626/228 = 2.745",
                "                                                     turned up, span 3",
                "   from 4:  116/113 = 1.026   205/202 = 1.014        ran out, span 2",
                "   plan  1-3, 4-5         cost  287 + 205  =  492            two orders",
                "",
                "   exact 462      Silver-Meal 486 (+24)      least unit cost 492 (+30)",
            ]),
            ("p", "Neither rule dominates. Silver-Meal is 24 over with three orders; least unit "
                  "cost is 30 over with two. They do not merely differ in how much they lose, "
                  "they differ in what kind of plan they produce, and no amount of preferring "
                  "one of them in advance is justified by this instance &mdash; or, as the next "
                  "paragraph shows, by the other one."),
            ("h3", "The instance where one of them is exactly right"),
            ("p", "Take the six-period demand of &ldquo;Wagner-Whitin and the Order Intervals&rdquo;: "
                  "10, 62, 12, 130, 154, 129 "
                  "with a setup of 54 and a holding rate of 2. Silver-Meal produces precisely "
                  "the exact plan &mdash; five orders, with periods 2 and 3 covered together "
                  "&mdash; and costs 294, which is the optimum. Least unit cost produces four "
                  "orders and costs 600, more than twice the optimum."),
            ("example", ("Why least unit cost goes so badly wrong there",
                         "Starting at period 1 it compares 116/17-style ratios: `54/10 = 5.4`, "
                         "then `178/72 ≈ 2.47`, then `226/84 ≈ 2.69`. So it covers periods 1 and "
                         "2 together and stops. Starting again at period 3 it sees `54/12 = 4.5` "
                         "and then `314/142 ≈ 2.21`, so it covers periods 3 and 4 together "
                         "&mdash; which means carrying 130 units for a period at 2 each.",
                         "That single decision costs 260 in holding to save one setup charge of "
                         "54. The per-unit average is falling the whole time, because the 130 "
                         "units in the denominator swamp the 260 in the numerator; the average "
                         "is a ratio and the rule is watching the ratio rather than the money.")),
            ("p", "So on one instance Silver-Meal is exact and least unit cost is more than "
                  "double; on another Silver-Meal is 24 over and least unit cost 30 over. Two "
                  "instances is not a study, and this page does not claim one. What it claims is "
                  "narrower and is measured: neither rule dominates the other, and the honest "
                  "way to use either is to price its output against the recursion whenever you "
                  "can afford to."),
            ("h3", "The instance where everything agrees"),
            ("p", "Flat demand of 30 for six periods, a setup of 80 and a holding rate of 1: "
                  "both rules and the recursion produce the same three-order plan costing 330. "
                  "That is the case a textbook reaches for when it wants to show a heuristic in "
                  "a good light, and it is exactly the case that cannot distinguish the rules "
                  "from each other or from the exact answer. A flat instance is where a "
                  "heuristic looks best, which is why it is not the test."),
            ("p", "The lab plots the cost of each plan against the number of orders it places, "
                  "which makes one thing visible that a table does not: the exact plan is not "
                  "always the one with the most orders or the fewest. On the five-period "
                  "instance the optimum has three orders, one heuristic has three and is still "
                  "wrong, and the other has two. The order count is not the thing being "
                  "optimised and reading the plot as though it were is a mistake worth making "
                  "once, on the page, with the numbers in front of you."),
            ("p", "What none of this settles is whether the exact plan is worth having. The "
                  "recursion needs the whole horizon in advance and the heuristics need only the "
                  "next few periods, so on a rolling forecast the comparison is not between 462 "
                  "and 486 at all &mdash; it is between two different problems. That is a "
                  "judgement about the situation rather than about the arithmetic, and it is the "
                  "reason both rules are still in use."),
        ],
        "lab": ("dpseq", {
            "mode": "heuristics",
            "preset": "both",
            "panel_title": "Trace both rules, and price what each of them produces",
            "panel_intro": "Each rule is traced interval by interval with the running average it "
                           "was watching, so the period it stops at is visible rather than "
                           "asserted. Every plan &mdash; both heuristics and the exact one "
                           "&mdash; is then priced again from the demand and the two charges by "
                           "the same function, so the three totals are comparable. This example "
                           "is the one where both rules miss and neither dominates; the "
                           "first in the list is the one where Silver-Meal happens to be exact.",
        }),
        "steps_title": "Tracing a rule honestly",
        "steps_intro": "Four steps. The fourth is the one that turns a demonstration into a measurement.",
        "steps": [
            ("Write the running total for each candidate interval, not just the average",
             "`K` plus `h` times the holding, for covering one period, two periods, three. The "
             "average is that total divided by something, and keeping the total in view stops "
             "you from losing track of what the ratio is a ratio of."),
            ("Divide by the right denominator, and be able to say which",
             "Periods for Silver-Meal, units for least unit cost. Writing both columns side by "
             "side once is worth more than remembering which is which, because the point of the "
             "lesson is that the choice of denominator changes the plan."),
            ("Stop at the first value that is not smaller, and start again",
             "Not the smallest over the whole horizon &mdash; the first turn upwards. That is "
             "what makes these rules cheap and what makes them wrong; a rule that searched for "
             "the global minimum of the average would be doing more work than the recursion."),
            ("Price the finished plan from the demand, not from the rule's own running total",
             "Setup charges plus `h` times unit-periods, computed independently. Then subtract "
             "the exact cost to get the gap. A heuristic that reports its own cost is not a "
             "witness to it, and the whole comparison depends on one instrument measuring all "
             "three plans."),
        ],
        "worked": {
            "title": "Two rules on two instances, priced with one instrument",
            "intro": [
                "The five-period instance where both rules miss, and the six-period one where "
                "Silver-Meal is exactly right. Every cost below is the plan priced from the "
                "demand rather than the number the rule reported."
            ],
            "lines": [
                "INSTANCE A     demand 17 25 73 113 89        K = 116     h = 1",
                "",
                "   exact            orders at 1, 3, 4       141 + 116 + 205  =  462",
                "   Silver-Meal      orders at 1, 3, 5       141 + 229 + 116  =  486     +24",
                "   least unit cost  orders at 1, 4          287 + 205        =  492     +30",
                "",
                "   three orders is not the problem: the exact plan also places three.",
                "   Silver-Meal covers 3-4 where the optimum covers 3 alone and 4-5 together.",
                "",
                "INSTANCE B     demand 10 62 12 130 154 129   K = 54      h = 2",
                "",
                "   exact            orders at 1, 2, 4, 5, 6                   =  294",
                "   Silver-Meal      orders at 1, 2, 4, 5, 6                   =  294     +0",
                "   least unit cost  orders at 1, 3, 5, 6                      =  600   +306",
                "",
                "   least unit cost covers 3-4 together, carrying 130 units one period:",
                "      holding 2 x 130 = 260,   to save one setup charge of 54.",
                "",
                "INSTANCE C     demand 30 30 30 30 30 30      K = 80      h = 1",
                "",
                "   exact 330      Silver-Meal 330      least unit cost 330",
                "   all three place three orders covering 1-2, 3-4, 5-6.",
            ],
            "after": [
                "Instance C is the one to be suspicious of. Every rule agrees, every plan is "
                "tidy, and nothing has been tested: with demand flat there is no way for the two "
                "averages to disagree, so the instance cannot distinguish the rules even in "
                "principle. A demonstration built on it would be a demonstration of nothing.",
                "For a rehearsal, take instance A and raise the setup charge with the slider "
                "until least unit cost becomes exact. Then keep going and watch whether it stays "
                "exact. The interesting part is that the gap is not monotone in the charge: a "
                "heuristic can be right, then wrong, then right again as a parameter moves, "
                "which is another way of saying its error is not an approximation.",
                "The harder rehearsal: find a demand sequence on which least unit cost beats "
                "Silver-Meal. It exists &mdash; the per-unit average is the better guide when "
                "demand rises steeply and holding is cheap &mdash; and constructing one is the "
                "only way to be sure you believe &ldquo;neither dominates&rdquo; rather than "
                "having read it.",
            ],
        },
        "quiz_title": "Averages, stopping points and what a gap means",
        "quiz": [
            {"q": "Silver-Meal and least unit cost differ in exactly one respect. Which?",
             "a": ["One works forwards and the other backwards",
                   "One allows shortages and the other does not",
                   "The denominator of the running average: periods covered, against units ordered",
                   "One stops at the first turn upwards and the other at the global minimum"],
             "c": 2,
             "why": "Both build intervals left to right and both stop at the first turn upwards. "
                    "Dividing the same total by the number of periods or by the quantity is the "
                    "whole difference, and it is enough to make them produce plans with "
                    "different numbers of orders on the same data."},
            {"q": "On the five-period instance the exact cost is 462, Silver-Meal costs 486 and least unit cost 492. What does that show?",
             "a": ["That Silver-Meal is the better rule",
                   "That neither rule dominates: on this instance Silver-Meal is closer, and on the six-period instance least unit cost costs more than twice the optimum while Silver-Meal is exact",
                   "That both rules are approximations converging to the optimum",
                   "That the optimum has fewer orders than either rule places"],
             "c": 1,
             "why": "Two instances is not a ranking. What is measured is that they miss "
                    "differently &mdash; 24 with three orders against 30 with two &mdash; and "
                    "that on other data the ordering reverses sharply. The exact plan on the "
                    "five-period instance also places three orders, so the order count is not "
                    "the thing that went wrong."},
            {"q": "Why does the lab price every plan again from the demand rather than using the total each rule reported?",
             "a": ["Because the rules do not report a total",
                   "Because the rounding would otherwise differ",
                   "Because a rule's own bookkeeping is produced by the code that chose the plan, so it cannot testify to it &mdash; all three plans need one instrument",
                   "Because the exact plan is priced differently from a heuristic plan"],
             "c": 2,
             "why": "The comparison is the whole content of the lesson, so the measurement has "
                    "to be independent of the thing measured. One pricing function is applied to "
                    "all three plans, and it also checks that each plan covers every period "
                    "exactly once, which is a way a reconstructed plan can be wrong without "
                    "costing anything."},
            {"q": "With demand flat at 30 for six periods, all three methods agree at 330. What has that instance tested?",
             "a": ["That the heuristics are correct",
                   "That the heuristics are correct when demand is known",
                   "Almost nothing: with demand flat the two averages cannot disagree, so the instance cannot distinguish the rules even in principle",
                   "That the exact recursion is unnecessary for flat demand"],
             "c": 2,
             "why": "It is the friendly case, and a friendly case is not a test. The reason it is "
                    "in the lab at all is to be recognised as one: a heuristic looks best exactly "
                    "where nothing can separate it from the alternative, and a demonstration "
                    "built on such an instance demonstrates nothing."},
        ],
        "mistakes": [
            ("Reading the gap as an approximation error that shrinks with care",
             "It does not shrink and there is nothing to tune. Both rules stop at the first turn "
             "upwards by construction, so the plans they can produce form a restricted set, and "
             "the exact plan is often not in it. Raising or lowering a charge moves a heuristic "
             "from exact to badly wrong and back again, which is the signature of a different "
             "search rather than a noisy one."),
            ("Choosing between the rules once, in advance",
             "The measured fact on this page is that neither dominates. Silver-Meal is exact on "
             "one of the instances here and 24 over on another; least unit cost is 30 over on "
             "one and more than double on the other. Any general preference has to come from "
             "knowing something about the demand pattern, and if you know that much you can "
             "usually afford the recursion."),
            ("Comparing the number of orders instead of the cost",
             "On the five-period instance the exact plan and the Silver-Meal plan both place "
             "three orders and differ by 24, while the least-unit-cost plan places two and "
             "differs by 30. The order count is not the objective; it is a feature of the plan, "
             "and a plot of cost against order count is there to make that separation visible "
             "rather than to suggest a target."),
        ],
        "standard": ("Finish when you can trace both rules by hand on a five-period instance, price each plan independently, and say why neither rule dominates.",
                     "You should be able to write the running average for each candidate "
                     "interval under both denominators, identify where each rule stops and why, "
                     "price each finished plan from the demand rather than from the rule's own "
                     "total, and reproduce the instance where both rules miss by different "
                     "amounts with different numbers of orders."),
        "note": 'Everything so far has been deterministic: the arcs, the returns and the demands were known before anything was decided. The next lesson, &ldquo;The Stochastic Recursion&rdquo;, puts chance inside the transition, so a value becomes an expectation and the maximum sits outside it. The recursion itself barely changes. What changes is that the best action in a state can now depend on how many periods are left, which means a policy has a time index and the stationary case becomes the special one.',
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "the-stochastic-recursion",
        "title": "The Stochastic Recursion",
        "module": "When the next step is uncertain",
        "one_line": "An expectation inside a maximum, filled backwards on exact fractions, and checked against every deterministic policy evaluated by pushing a distribution forward.",
        "summary": (
            "An action no longer decides where you end up; it decides a distribution over where "
            "you end up. The recursion absorbs that with one change &mdash; the value of an "
            "action is its immediate reward plus the expected value of where it sends you "
            "&mdash; and everything else about filling the table backwards is unchanged. What is "
            "new is that the best action in a state can depend on how many periods remain, so a "
            "policy in a finite horizon carries a time index and a policy that does not is a "
            "special case rather than the norm."
        ),
        "key": [
            "Vₜ(i) = max over a of [ r(a,i) + Σⱼ P(a,i,j) Vₜ₊₁(j) ],   V_T(i) = 0",
            "the expectation is INSIDE the maximum: choose, then average over what follows",
            "states small large,  acts grow harvest,  four periods",
            "V: (0,0) then (3,9) then (15/2, 27/2) then (12,18) then (33/2, 45/2)",
            "with one period left the small state harvests; with two or more it grows",
            "256 deterministic policies, each evaluated forwards, and none beats the table",
        ],
        "key_label": "One recursion with an expectation in it, and the policy it implies",
        "concepts_intro": (
            "Three ideas. The first is where the expectation goes, the second is what a policy "
            "now is, and the third is how the table is checked without using a value function."
        ),
        "concepts": [
            ("The expectation is inside the maximum, and the order is the model",
             "`max over a of E[...]` says you choose the action and then chance resolves. "
             "`E[max over a of ...]` would say chance resolves first and you choose knowing the "
             "outcome, which is a completely different problem and a strictly better one &mdash; "
             "it is the perfect-information value that &ldquo;Folding a Decision Tree Back&rdquo; "
             "uses as an upper bound. "
             "Writing the two down side by side once is the cheapest way to stop confusing them."),
            ("A policy in a finite horizon is a function of time as well as state",
             "The table has one column per period, and the argmax in a cell can differ from the "
             "argmax in the cell above it. In the instance here the small state harvests when "
             "one period is left and grows whenever two or more are, because growing pays almost "
             "nothing now and improves where you will be &mdash; and with nothing left to come, "
             "improving where you will be is worth nothing. A stationary policy is what you get "
             "when that never happens, which is a fact about an instance."),
            ("Every policy can be evaluated without a value function at all",
             "Fix a policy, put all the probability on a starting state, and push the "
             "distribution forward period by period, collecting the reward that policy earns in "
             "each state weighted by the probability of being there. No maximum is ever taken "
             "and no value is ever written, so this computation cannot repeat a mistake the "
             "recursion made. With two states, two actions and four periods there are 256 "
             "deterministic policies and the lab evaluates all of them."),
        ],
        "read_title": "One change to the recursion, and one change to what an answer is",
        "read_intro": "The recursion, the instance where the best action depends on the horizon, and the forward evaluation that checks the whole thing.",
        "body": [
            ("def", ("A finite-horizon Markov decision process",
                     "A set of <strong>states</strong>, a set of <strong>actions</strong>, a "
                     "<strong>transition</strong> `P(a, i, j)` giving the probability of moving "
                     "to state `j` when action `a` is taken in state `i`, a "
                     "<strong>reward</strong> `r(a, i)` earned immediately, and a horizon of `T` "
                     "periods. Every row of every transition table sums to 1 exactly.",
                     "A <strong>policy</strong> assigns an action to each state in each period. "
                     "The <strong>value</strong> `Vₜ(i)` is the largest expected total reward "
                     "obtainable from state `i` with `T − t` periods left, and satisfies "
                     "`Vₜ(i) = max over a of [ r(a,i) + Σⱼ P(a,i,j) · Vₜ₊₁(j) ]` with "
                     "`V_T(i) = 0`.")),
            ("p", "The lab refuses a transition row that does not sum to exactly 1, rather than "
                  "normalising it. A distribution that does not add up is a modelling error and "
                  "not a typing one: silently rescaling it would answer a question the reader "
                  "did not ask, and every number on the page would be exactly right about it."),
            ("math", [
                "states  small large       actions  grow harvest       T = 4",
                "",
                "   grow      from small -> small 1/4, large 3/4        pays  small 0   large 1",
                "             from large -> large 1",
                "   harvest   from small -> small 1                     pays  small 3   large 9",
                "             from large -> small 3/4, large 1/4",
                "",
                "filled from the end, V with 0 periods left is 0 in both states:",
                "",
                "1 left    small   grow 0 + 0 = 0        harvest 3 + 0 = 3        -> harvest  3",
                "          large   grow 1 + 0 = 1        harvest 9 + 0 = 9        -> harvest  9",
                "",
                "2 left    small   grow 0 + (1/4)(3) + (3/4)(9) = 15/2",
                "                  harvest 3 + (1)(3)           = 6               -> grow  15/2",
                "          large   grow 1 + (1)(9)              = 10",
                "                  harvest 9 + (3/4)(3) + (1/4)(9) = 27/2         -> harvest 27/2",
                "",
                "3 left    small   grow 0 + (1/4)(15/2) + (3/4)(27/2) = 12        -> grow    12",
                "                  harvest 3 + 15/2 = 21/2",
                "          large   grow 1 + 27/2 = 29/2",
                "                  harvest 9 + (3/4)(15/2) + (1/4)(27/2) = 18     -> harvest 18",
                "",
                "4 left    small   grow 0 + (1/4)(12) + (3/4)(18) = 33/2          -> grow    33/2",
                "                  harvest 3 + 12 = 15",
                "          large   grow 1 + 18 = 19",
                "                  harvest 9 + (3/4)(12) + (1/4)(18) = 45/2       -> harvest 45/2",
            ]),
            ("p", "Read the small state down the table: harvest, grow, grow, grow. With one "
                  "period left there is nothing to grow into, so the 3 that harvesting pays "
                  "immediately wins; with two or more, growing pays 0 now and puts three "
                  "quarters of the probability into the large state, which is worth 9 and then "
                  "27/2 and then 18. The large state harvests throughout, because harvesting "
                  "there pays 9 and only knocks you back three times in four."),
            ("h3", "What the table does not say on its own"),
            ("p", "`V₀(small) = 33/2` is a claim about a number. &ldquo;The policy this table "
                  "describes is worth 33/2 starting from the small state&rdquo; is a different "
                  "claim, and it is the one a reader can act on. The lab makes it separately: it "
                  "takes the argmax in each cell, treats that as a fixed policy, and evaluates "
                  "it by pushing a probability distribution forward from each starting state "
                  "through four periods. Both come to 33/2 and 45/2."),
            ("p", "Then it does the harder thing. There are two actions, two states and four "
                  "periods, so a deterministic policy is eight independent choices and there are "
                  "256 of them. Every one is evaluated the same forward way, and the best "
                  "starting from each state is recorded. The best from the small state is 33/2 "
                  "and from the large state 45/2, which is what the table said. Three routes to "
                  "the same pair of numbers, and only two of them involve a value function."),
            ("example", ("An action that ends the game",
                         "Switch to the example with an owned machine: keeping pays 3 a period "
                         "and leaves it owned four times in five, selling pays 7 once and the "
                         "sold state pays nothing ever again. With one period left the table "
                         "sells, because 7 beats 3 and there is no future to protect. With two "
                         "left it keeps, because keeping is worth 43/5; with three left it keeps "
                         "again, at 247/25.",
                         "Same shape as the growing instance and a different story: here the "
                         "action that pays best now is the one that destroys every future "
                         "period, so it becomes correct only at the very end. An absorbing state "
                         "is worth meeting because it is the cleanest case where a stationary "
                         "policy is simply wrong.")),
            ("h3", "What the state left out"),
            ("p", "The transition depends on the current state and the chosen action, and on "
                  "nothing else. That is the Markov assumption, and it is doing a great deal of "
                  "work: it says that how you arrived in the small state cannot matter, that the "
                  "probabilities do not drift over the four periods, and that nothing outside "
                  "the two named states influences anything. Each of those can be false, and "
                  "each of them, if false, leaves every number in the table exactly right about "
                  "a process that is not the one in front of you."),
            ("p", "There is a second assumption hiding in the objective. Maximising expected "
                  "total reward treats a certain 10 and a fifty-fifty gamble between 0 and 20 as "
                  "the same thing. That is a choice about what the decision-maker cares about, "
                  "it is not implied by anything in the model, and no amount of exact arithmetic "
                  "on the expectation will reveal it. Say it out loud before quoting a policy."),
        ],
        "lab": ("dpseq", {
            "mode": "stochastic",
            "preset": "flip",
            "panel_title": "Fill the table backwards, then check it forwards, twice",
            "panel_intro": "Every cell shows both actions priced, so the argmax is visible rather "
                           "than asserted, and the values stay exact fractions because an "
                           "expectation of an expectation of an expectation is still rational. "
                           "Beside it, two independent checks that never form a value: the "
                           "policy the table describes, evaluated by pushing a distribution "
                           "forward, and every deterministic policy there is, evaluated the same "
                           "way. In this example the best action in one of the two states "
                           "changes with how many periods are left.",
        }),
        "steps_title": "Filling a stochastic table",
        "steps_intro": "Five steps. The first is a check on the data and the last is a check on the answer, and skipping either produces confident nonsense.",
        "steps": [
            ("Check that every transition row sums to exactly one",
             "One row per state per action. A row that does not sum to 1 is not a distribution "
             "and nothing downstream is meaningful; the lab refuses rather than normalising, "
             "because rescaling silently answers a different question."),
            ("Set the value in the final period to zero and work backwards",
             "`V_T(i) = 0` for every state, unless the problem gives a terminal payoff. Every "
             "later column depends only on the column to its right, so one right-to-left pass "
             "fills the table."),
            ("In each cell, price every action and keep the maximum",
             "`r(a,i)` plus the sum over `j` of `P(a,i,j)` times the value of `j` in the next "
             "column. Keep the arithmetic in fractions: the products and sums of rationals are "
             "rational, and a decimal here hides whether two actions are genuinely tied."),
            ("Read the policy down each row, and notice where it changes",
             "A state whose argmax is the same in every column has a stationary policy on this "
             "instance; a state where it changes does not, and the period where it changes is "
             "usually the interesting fact about the problem."),
            ("Evaluate the policy forwards, independently",
             "Put all the probability on a starting state, and for each period collect the "
             "reward the policy earns in each state weighted by the chance of being there, then "
             "push the distribution through that period's transitions. No maximum, no value "
             "function. The number that comes out should equal the table's first column."),
        ],
        "worked": {
            "title": "One table, three routes to the same two numbers",
            "intro": [
                "The recursion, then the policy it describes evaluated by pushing a distribution "
                "forward, then the best of all 256 deterministic policies evaluated the same way."
            ],
            "lines": [
                "states small large      grow: small -> (1/4, 3/4), large -> (0, 1)",
                "                        harvest: small -> (1, 0), large -> (3/4, 1/4)",
                "rewards  grow    small 0   large 1",
                "         harvest small 3   large 9",
                "",
                "THE TABLE",
                "",
                "   periods left        0        1        2        3        4",
                "   small               0        3      15/2       12      33/2",
                "   large               0        9      27/2       18      45/2",
                "",
                "   small takes      -     harvest    grow     grow     grow",
                "   large takes      -     harvest  harvest  harvest  harvest",
                "",
                "FORWARD, the policy above, starting in small with four periods to go",
                "",
                "   period 1   in small with probability 1, grows, pays 0",
                "              distribution becomes  small 1/4   large 3/4",
                "   period 2   small grows (pays 0), large harvests (pays 9)",
                "              collected  (3/4)(9) = 27/4",
                "              distribution becomes  small 1/16 + 9/16 = 5/8   large 3/8",
                "   period 3   small grows, large harvests",
                "              collected  (3/8)(9) = 27/8",
                "   period 4   both harvest:  small pays 3, large pays 9",
                "",
                "   total collected over the four periods  =  33/2         agrees",
                "",
                "EVERY POLICY",
                "",
                "   2 actions, 2 states, 4 periods   ->   2^8 = 256 deterministic policies",
                "   best from small  33/2        best from large  45/2      both agree",
            ],
            "after": [
                "The forward evaluation is worth doing once by hand because it makes the "
                "distribution concrete: after one period there is a three-quarters chance of "
                "being in the large state, and every reward from then on is weighted by where "
                "the process actually is rather than by where it was aimed. Nothing in that "
                "computation resembles the recursion, which is exactly why it is a check.",
                "For a rehearsal, set the horizon to one period with the slider and read the "
                "policy: both states harvest, and the values are 3 and 9. Then raise it one "
                "period at a time and watch the small state flip to growing and stay there. The "
                "flip happens between one period and two, and the reason is visible in the "
                "arithmetic: growing is worth 15/2 against harvesting's 6.",
                "The harder rehearsal: change the reward for harvesting in the small state from "
                "3 to 8 and find the horizon at which the flip disappears altogether. Then ask "
                "what you would have concluded from a table filled at a single horizon, and what "
                "it would have taken to notice.",
            ],
        },
        "quiz_title": "Expectations, policies and horizons",
        "quiz": [
            {"q": "Why is the expectation written inside the maximum rather than outside it?",
             "a": ["Because expectation is linear",
                   "Because it is easier to compute that way",
                   "Because the action is chosen before chance resolves; the other order describes a decision-maker who already knows the outcome",
                   "Because the transition rows sum to one"],
             "c": 2,
             "why": "`max E` and `E max` are different problems. The second is the "
                    "perfect-information value, it is never smaller, and the gap between the two "
                    "is exactly what the next lesson prices. Getting the order wrong produces a "
                    "number that is too good and no symptom on the page."},
            {"q": "In the instance in the lab, the small state harvests with one period left and grows with two or more. What does that show?",
             "a": ["That the table has been filled in the wrong direction",
                   "That a policy in a finite horizon is a function of time as well as of state, and a stationary policy is a special case",
                   "That the transition probabilities change over time",
                   "That growing is always the better action"],
             "c": 1,
             "why": "Growing pays 0 immediately and moves three quarters of the probability into "
                    "the state worth 9. With nothing left to come, that improvement is worth "
                    "nothing and the immediate 3 wins. The argmax therefore differs between "
                    "columns, which is what a time index in the policy is for."},
            {"q": "The lab evaluates all 256 deterministic policies by pushing a distribution forward. What does that check catch that re-reading the table cannot?",
             "a": ["An arithmetic slip in a single cell",
                   "A transition row that does not sum to one",
                   "An error in the recursion itself, because the forward evaluation never forms a value function and so cannot repeat it",
                   "A policy that is not stationary"],
             "c": 2,
             "why": "Checking a computation with itself proves nothing. The forward evaluation "
                    "takes no maximum and writes no `V`; it collects reward against a "
                    "distribution. If the recursion were wrong in a way that is internally "
                    "consistent, only an independent computation would show it."},
            {"q": "A transition row typed into the lab adds to `9/10`. What does the lab do, and why?",
             "a": ["Rescales it to sum to one, since that is what was clearly meant",
                   "Refuses it and says so, because a distribution that does not add up is a modelling error and rescaling would answer a different question",
                   "Treats the missing tenth as a probability of stopping",
                   "Warns but continues with the row as typed"],
             "c": 1,
             "why": "Both of the other readings &mdash; a typo, or a tenth of a chance of "
                    "leaving the system &mdash; are plausible, and they give different answers. "
                    "Choosing one silently would produce a page of exactly correct arithmetic "
                    "about a process the reader never described."},
        ],
        "mistakes": [
            ("Averaging the maximum instead of maximising the average",
             "`E[max]` assumes the outcome is known before the choice, which is the "
             "perfect-information problem. It is never smaller than the right answer and it can "
             "be much larger, and the two look identical on a page until you ask what is known "
             "when. Write the two expressions out once and keep the version with `max` on the "
             "outside where you can see it."),
            ("Assuming the optimal policy is stationary because it usually looks like one",
             "It is stationary on some instances and not on others, and the finite horizon is "
             "exactly where it fails. In the instance here one of the two states flips between "
             "one period left and two; in the absorbing example, selling is right only in the "
             "final period. A policy quoted without saying how many periods it was computed for "
             "is incomplete."),
            ("Reading exact fractions as a stylistic choice",
             "The values here are `15/2`, `27/2`, `33/2`, `45/2`, `43/5`, `247/25`. In decimal "
             "some of these are exact and some are not, and once rounded there is no way to tell "
             "whether two actions are genuinely tied or merely close &mdash; which matters, "
             "because a tie means two optimal policies and a near-miss means one. The arithmetic "
             "stays rational so that the distinction survives."),
        ],
        "standard": ("Finish when you can fill a two-state, two-action table backwards in fractions, read the policy down each row, and evaluate that policy forwards without using the table.",
                     "You should be able to write the recursion with the expectation inside the "
                     "maximum and say why the other order is a different problem, check the "
                     "transition rows before computing anything, identify the period at which an "
                     "argmax changes and explain it from the arithmetic, and push a distribution "
                     "forward through a fixed policy to reproduce the value independently."),
        "note": 'Chance has been in the transition: you knew the state and not where the action would send you. The next lesson, &ldquo;Folding a Decision Tree Back&rdquo;, moves the uncertainty to the other side, where you do not know the state and can pay to learn something about it. The recursion is the same fold &mdash; a chance node is an average and a decision node is a maximum &mdash; and the new quantity is what a signal is worth, which turns out to have a ceiling that no signal can exceed and can be exactly zero for a signal that looks perfectly informative.',
    },
]
