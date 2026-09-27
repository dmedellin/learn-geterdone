"""Networks: Flows, Paths and Assignments -- the first half.

The network as an object, the one programme every network problem turns out to
be, the transportation tableau and the method that solves it, and the theorem
that says why the answers came out whole.

Every figure below is read off the kits -- scripts/mathpath/labs/network.py and
scripts/mathpath/labs/transport.py -- by executing their shipped JavaScript,
rather than asserted here, and scripts/mathcheck.js executes those same blocks.
Where a design note and a kit disagreed, the kit won.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "arcs-capacities-and-conservation",
        "title": "Arcs, Capacities and Conservation",
        "module": "The network as a programme",
        "one_line": "Write a directed network down as data and test a proposed flow twice: at every node, and on every arc.",
        "summary": (
            "A network on this course is not a picture. It is a list of ordered arcs, each with "
            "a capacity and a cost, and a supply at every node; and a flow on it is a number per "
            "arc that has to survive two separate tests. Conservation is local, so a flow can "
            "balance in total and still fail. Capacity is a different test entirely, so a flow "
            "can conserve everywhere and still ask an arc to carry more than it can."
        ),
        "key": [
            "an arc is ORDERED:  a to b and b to a are two objects, two capacities, two costs",
            "conservation at node i:   (out of i) − (into i) = bᵢ      one equation per node",
            "capacity on arc j:        0 ≤ xⱼ ≤ uⱼ            one row per BOUNDED arc only",
            "Σᵢ bᵢ = 0, or nothing is feasible: add the node equations and every flow cancels",
            "s>a 5:2   capacity 5, cost 2 per unit          s>a *:2   no upper bound at all",
        ],
        "key_label": "The two tests a flow must pass, and the one the data must pass first",
        "concepts_intro": (
            "Drawing the arrows is the easy part. The three ideas here are the ones that decide "
            "whether what you have written down can be solved at all."
        ),
        "concepts": [
            ("An arc is ordered, and an adjacency matrix cannot hold one",
             "A matrix indexed by a pair of nodes has one cell for that pair. A directed network "
             "needs two: `a` to `b` may hold 4 units at a price of 2 while `b` to `a` holds 3 at "
             "a price of 5, and those are different variables in the programme that follows. "
             "The lab stores an array of arcs for exactly this reason, and it will hold two "
             "copies of the same arc if you type it twice."),
            ("Conservation is local, and its failures cancel",
             "Each node carries one equation: what leaves minus what arrives equals what that "
             "node supplies. Add all those equations together and every arc appears once "
             "positively and once negatively, so the total is always zero &mdash; which means a "
             "single overall verdict can never detect a violation. The imbalances have to be "
             "reported node by node or they are invisible."),
            ("Capacity is a second test, and an unbounded arc is not a large number",
             "A flow that conserves at every node has said nothing about whether the arcs can "
             "carry it. Those are two independent checks and the lab runs both. An arc written "
             "with no upper bound contributes no capacity row at all &mdash; which is what "
             "&ldquo;unbounded&rdquo; means, and is different from an arc bounded by some very "
             "large constant, because the constant can bind and infinity cannot."),
        ],
        "read_title": "Everything a network is, before anything is optimised",
        "read_intro": "The data, then the two tests, then the three ways the data itself can already be wrong.",
        "body": [
            ("def", ("A directed network with capacities and costs",
                     "A <strong>directed network</strong> is a set of nodes together with a list "
                     "of <strong>arcs</strong>. Each arc has a tail, a head, a "
                     "<strong>capacity</strong> `u` (possibly no upper bound) and a "
                     "<strong>cost</strong> `c` per unit. Each node `i` carries a "
                     "<strong>supply</strong> `bᵢ`, positive where goods enter the network and "
                     "negative where they leave.",
                     "A <strong>flow</strong> is one number `xⱼ ≥ 0` for each arc. It is "
                     "<strong>feasible</strong> when it conserves at every node and respects "
                     "every capacity.")),
            ("p", "The lab takes a network as text, one clause per arc: `s>a 5:2` is an arc from "
                  "`s` to `a` with capacity 5 and cost 2. A `*` in the capacity field means no "
                  "upper bound; `7/2` is seven halves, exactly, because the field separator is a "
                  "colon and a slash is therefore free to mean division. A clause running from a "
                  "node back to itself is refused rather than drawn, and so is a negative "
                  "capacity."),
            ("math", [
                "the network                       the supplies         a proposed flow",
                "",
                "   s>a  5:2                         s :  4                s>a  4",
                "   a>b  4:2                         t : -4                a>b  2",
                "   b>a  3:5                                               b>a  0",
                "   a>t  3:1                                               a>t  2",
                "   b>t  4:3                                               b>t  2",
                "",
                "conservation, node by node:   out − in    supplied",
                "",
                "   s      4 − 0                =   4         4     ✓",
                "   a      2 + 2 − 4            =   0         0     ✓",
                "   b      0 + 2 − 2            =   0         0     ✓",
                "   t      0 − 4                =  −4        −4     ✓",
                "",
                "capacity:  4 ≤ 5,  2 ≤ 4,  0 ≤ 3,  2 ≤ 3,  2 ≤ 4      ✓",
                "cost:      4(2) + 2(2) + 0(5) + 2(1) + 2(3)  =  20",
            ]),
            ("p", "Two arcs in that list join the same pair of nodes. `a>b` carries up to 4 at a "
                  "price of 2; `b>a` carries up to 3 at a price of 5. They are two variables. "
                  "Sending one unit forward and two back costs 12; sending two forward and one "
                  "back costs 9 &mdash; same total movement, different bill, because the "
                  "directions are priced separately. The lab draws the pair in its own colour so "
                  "that the two arrows cannot be read as one edge."),
            ("h3", "Conservation fails locally, and the total will not tell you"),
            ("example", ("A flow that balances overall and is not a flow",
                         "Change one number in the flow above &mdash; `a>b` from 2 to 1 &mdash; "
                         "and the net outflows become `4, −1, 1, −4` against supplies "
                         "`4, 0, 0, −4`. Node `a` now takes in one more unit than it sends on, "
                         "and node `b` sends on one more than it takes in.",
                         "Those two errors are equal and opposite, so the imbalances still sum "
                         "to zero, and any check that adds them up passes. The lab names `a` and "
                         "`b` instead, and shades the two of them, because a verdict of "
                         "&ldquo;this flow is invalid&rdquo; is not something a reader can act "
                         "on.")),
            ("example", ("A flow that conserves everywhere and is still impossible",
                         "Set the supplies to `s: 5`, `t: −5` and the flow to "
                         "`s>a 5, a>b 5, b>a 0, a>t 0, b>t 5`. Every node balances exactly.",
                         "Two arcs are over capacity: `a>b` is asked for 5 where it holds 4, and "
                         "`b>t` for 5 where it holds 4. Conservation cannot see this, because "
                         "the node equations contain no capacities at all. The two tests are "
                         "separate and the lab runs them separately.")),
            ("h3", "Two things the data can get wrong before any flow does"),
            ("p", "Add the node equations together. Every arc leaves exactly one node and enters "
                  "exactly one, so its variable appears once with a plus and once with a minus "
                  "and cancels. What is left is `Σᵢ bᵢ = 0`. So if the supplies do not sum to "
                  "zero, the equations contradict each other and no flow of any kind exists "
                  "&mdash; a test that costs one addition and needs no algorithm."),
            ("example", ("Six in, four out",
                         "Leave the network alone and set the supplies to `s: 6`, `t: −4`. The "
                         "lab reports a total of 2 and stops: adding the four node equations "
                         "gives `2 = 0`.",
                         "This is worth meeting before the programme is written rather than "
                         "after a solver reports infeasibility, because the diagnosis is "
                         "completely different. Nothing is wrong with the network; the demand "
                         "does not match the supply, and the fix is to say what happens to the "
                         "surplus.")),
            ("p", "The second is quieter. A flow may only name arcs that exist: write "
                  "`s>c 1` on a network with no such arc and the lab refuses it rather than "
                  "creating one. This sounds pedantic until you have spent twenty minutes on a "
                  "transportation problem in which a route you assumed was available was never "
                  "in the data."),
            ("p", "Everything from here on is this object with an objective attached. The arcs "
                  "become the columns of a matrix, the nodes become its rows, the supplies "
                  "become the right-hand side, and the whole of the rest of the course is what "
                  "that matrix turns out to be like."),
        ],
        "lab": ("network", {
            "mode": "digraph",
            "preset": "twoway",
            "panel_title": "Type a network, its supplies and a flow, and watch both tests run",
            "panel_intro": "Each arc is labelled with what it carries out of what it can hold, "
                           "and priced. The strip beneath the drawing is one bar per node: net "
                           "outflow against what that node is supposed to supply, so a local "
                           "failure is visible even when the total is zero. Four worked examples "
                           "break it four different ways.",
        }),
        "steps_title": "Checking a flow somebody has handed you",
        "steps_intro": "The data first, then conservation, then capacity, and the cost last. Doing them in that order means an infeasible instance never reaches the arithmetic.",
        "steps": [
            ("Add the supplies up",
             "If `Σ bᵢ` is not zero, stop. There is no feasible flow and no flow you write down "
             "will be one. This is one addition and it is the cheapest test on the course."),
            ("Check that every arc in the flow is an arc in the network",
             "And that every arc in the network has been given a value, even if that value is "
             "zero. A missing arc is usually a typing error; an invented arc is usually a wish."),
            ("Compute net outflow at each node separately",
             "Out minus in, one node at a time, against `bᵢ`. Do not add the results up: the sum "
             "is always zero and it will tell you nothing. Write the imbalance beside each node "
             "and look for the non-zero ones."),
            ("Check every capacity, including the ones you think are slack",
             "`0 ≤ xⱼ ≤ uⱼ` on each arc. Conservation has said nothing about this. An arc with "
             "no upper bound needs only `xⱼ ≥ 0`."),
            ("Only then price it",
             "`Σⱼ cⱼ xⱼ`. Pricing an infeasible flow produces a number, and the number is "
             "meaningless; the lab still prints it, because a reader who watches a cost appear "
             "beside a red banner learns something a hidden field cannot teach."),
        ],
        "worked": {
            "title": "One network, four flows, and what each one fails",
            "intro": [
                "The same five arcs throughout. Only the supplies and the flow change, and each "
                "line of arithmetic below is a test rather than a step towards an answer."
            ],
            "lines": [
                "arcs        s>a 5:2    a>b 4:2    b>a 3:5    a>t 3:1    b>t 4:3",
                "",
                "A   supplies  s:4  t:-4          flow  4, 2, 0, 2, 2",
                "    total supply  4 + (-4) = 0                             data ok",
                "    net out       s: 4   a: 0   b: 0   t: -4               conserves",
                "    capacity      4/5   2/4   0/3   2/3   2/4              fits",
                "    cost          8 + 4 + 0 + 2 + 6 = 20                   FEASIBLE",
                "",
                "B   supplies  s:4  t:-4          flow  4, 1, 0, 2, 2",
                "    net out       s: 4   a: -1   b: 1   t: -4",
                "                        ^^^^^        ^^^   two nodes fail",
                "    sum of imbalances  4 - 1 + 1 - 4 = 0   always, so useless",
                "    cost          8 + 2 + 0 + 2 + 6 = 18   a cheaper NON-flow",
                "",
                "C   supplies  s:5  t:-5          flow  5, 5, 0, 0, 5",
                "    net out       s: 5   a: 0   b: 0   t: -5               conserves",
                "    capacity      5/5   5/4   0/3   0/3   5/4",
                "                        ^^^                ^^^   two arcs over",
                "",
                "D   supplies  s:6  t:-4          flow  4, 2, 0, 2, 2",
                "    total supply  6 + (-4) = 2  ≠  0",
                "    adding the four node equations gives  2 = 0",
                "    INFEASIBLE, and no flow needed to be written at all",
                "",
                "two arcs, one pair of nodes:   a>b 4:2   and   b>a 3:5",
                "    1 forward and 2 back   1(2) + 2(5)  = 12",
                "    2 forward and 1 back   2(2) + 1(5)  =  9",
            ],
            "after": [
                "Case B is the one to sit with. It is cheaper than case A, it passes every "
                "capacity, and the imbalances add to zero. Nothing about it is wrong except "
                "that it is not a flow, and the only way to find that out is to look at the "
                "nodes one at a time.",
                "For a rehearsal, take case A and try to move one unit off `a>t` without "
                "breaking anything. You will find that the unit has to go somewhere, that the "
                "only other way out of `a` is `a>b`, and that `b` then has to pass it on &mdash; "
                "so the repair is forced, and the repaired flow costs 22 rather than 20. That "
                "forced chain is a cycle in disguise, and it comes back as the stepping-stone "
                "cycle in the transportation lessons.",
                "The harder rehearsal: type an arc with `*` in the capacity field and satisfy "
                "yourself that the lab stops printing a capacity ratio for it. An unbounded arc "
                "contributes no row to the programme that follows, which is not the same thing "
                "as contributing a row with a very large number in it.",
            ],
        },
        "quiz_title": "Arcs, nodes, and what each test can see",
        "quiz": [
            {"q": "A flow conserves at every node of a network. What follows about its capacities?",
             "a": ["Every arc is within capacity, since conservation implies feasibility",
                   "Nothing at all: conservation and capacity are separate tests",
                   "At most one arc can be over capacity",
                   "The arcs are within capacity provided the supplies sum to zero"],
             "c": 1,
             "why": "The node equations contain no capacities, so they cannot possibly report on "
                    "them. The lab ships the instance that makes this concrete: supplies of 5 "
                    "and −5, a flow conserving at all four nodes, and two arcs each asked to "
                    "carry 5 where they hold 4."},
            {"q": "You compute the net outflow at every node, and the imbalances add up to zero. What have you learned?",
             "a": ["That the flow conserves everywhere",
                   "That the flow conserves everywhere provided no arc is over capacity",
                   "Nothing, because that sum is zero for every flow whatever",
                   "That the supplies sum to zero"],
             "c": 2,
             "why": "Each arc contributes its value once positively at its tail and once "
                    "negatively at its head, so the imbalances always cancel. That is exactly "
                    "why a per-node report is the only useful one: the instance in the lab has "
                    "an imbalance of −1 at one node and +1 at another, and the total is zero."},
            {"q": "A network has an arc from `a` to `b` of capacity 4 at cost 2, and an arc from `b` to `a` of capacity 3 at cost 5. How many flow variables do those two arcs contribute?",
             "a": ["One, since there is only one pair of nodes involved",
                   "One, with a sign to say which way the flow runs",
                   "Two, one per arc, each with its own capacity and its own cost",
                   "Two, but they are forced to be equal and opposite"],
             "c": 2,
             "why": "They are two objects. One unit forward and two back costs 12; two forward "
                    "and one back costs 9. A single signed variable could not price those "
                    "differently, and could not hold two different capacities either &mdash; "
                    "which is why the lab stores arcs as a list and never as a matrix indexed "
                    "by the pair."},
            {"q": "The supplies on a network are `s: 6` and `t: −4`, all other nodes zero. What can you say before writing any flow?",
             "a": ["The problem is infeasible, because adding the node equations gives 2 = 0",
                   "The problem is feasible but its optimum will be expensive",
                   "The extra 2 will sit at `s`, which is what a supply means",
                   "It depends on the capacities of the arcs leaving `s`"],
             "c": 0,
             "why": "Every arc variable cancels when the node equations are added, leaving "
                    "`Σ bᵢ = 0` as a requirement on the data alone. Here the sum is 2, so the "
                    "equations contradict each other and capacities are irrelevant. Making the "
                    "surplus disposable is a modelling decision &mdash; it is what the dummy "
                    "column in the transportation lessons is for &mdash; and it has to be "
                    "written into the network rather than assumed."},
        ],
        "mistakes": [
            ("Treating the two arcs between a pair of nodes as one edge",
             "This is the undirected habit surviving into a directed setting, and it is the "
             "error this lesson exists for. The two arcs have separate capacities, separate "
             "costs and separate variables, and nothing in the model makes their flows related. "
             "A reader who collapses them will later write a transportation tableau with the "
             "wrong number of columns and never find out why the answer is cheap."),
            ("Adding the imbalances up and reading the total as a verdict",
             "The total is zero for every flow ever written, feasible or not. It is not a weak "
             "check, it is a check with no information in it. Report the imbalance at each node "
             "separately, and if you are writing code that reports a single boolean, make it "
             "return the list of failing nodes instead."),
            ("Modelling an unbounded arc with a large constant",
             "A capacity of one million is a capacity: it appears as a row in the programme, it "
             "can be tight at the optimum, and it can produce a shadow price on a constraint "
             "you invented. An arc with no upper bound contributes no row at all. If the "
             "quantity really is unbounded, say so; if it is not, use the real bound."),
        ],
        "standard": ("Finish when you can take a drawing and a proposed flow and say exactly which test fails and where.",
                     "You should be able to write a directed network as arcs with capacities and "
                     "costs, check the supplies sum to zero before anything else, compute net "
                     "outflow node by node without adding the results up, check capacities "
                     "separately, and explain why an arc and its reverse are two variables."),
        "note": 'Everything checked here was checked against the network as written down, and nothing yet has been optimised. That is the right order: a flow that fails conservation is not a bad solution, it is not a solution. The next lesson, “The Minimum-Cost Flow Programme”, turns these same two tests into the rows of a matrix and hands the result to the simplex method &mdash; at which point four problems you may have met separately turn out to be the same one.',
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-minimum-cost-flow-programme",
        "title": "The Minimum-Cost Flow Programme",
        "module": "The network as a programme",
        "one_line": "One matrix, one objective, one constraint set — and transportation, assignment, shortest path and maximum flow obtained by changing the data alone.",
        "summary": (
            "The node equations and the capacity bounds are a linear programme, and its matrix "
            "has one column per arc with a single plus one and a single minus one in it. That "
            "programme is the whole of this course: four problems usually taught as four "
            "separate algorithms are the same programme with a different right-hand side, and "
            "the lab solves all of them with the same exact simplex."
        ),
        "key": [
            "min Σⱼ cⱼ xⱼ    subject to    N x = b,    0 ≤ xⱼ ≤ uⱼ",
            "N is nodes × arcs: column j is +1 at arc j's tail, −1 at its head, 0 elsewhere",
            "transportation   b = supplies and −demands,   no upper bound on any arc",
            "assignment       the same, with every supply and every demand equal to 1",
            "shortest path    b = +1 at s, −1 at t,   every capacity 1,  c = the lengths",
            "maximum flow     c = 0, a return arc t>s priced at −1,  b = 0 at every node",
        ],
        "key_label": "One programme, and the four data sets that make it something else",
        "concepts_intro": (
            "The programme itself takes two lines to write. What takes a lesson is seeing that "
            "the four famous problems are not analogies for it."
        ),
        "concepts": [
            ("The incidence matrix is the model",
             "Number the nodes down the side and the arcs across the top. Column `j` of `N` "
             "holds `+1` in the row of arc `j`'s tail, `−1` in the row of its head, and zero in "
             "every other row. The row for node `i` then reads exactly &ldquo;what leaves `i` "
             "minus what arrives at `i`&rdquo;, so `Nx = b` is conservation at every node at "
             "once. Nothing about the drawing survives into the programme except this matrix."),
            ("The rows are dependent, and that is a fact about networks",
             "Every column of `N` holds one `+1` and one `−1`, so the rows sum to the zero "
             "vector and `N` never has full row rank. That is the same statement as "
             "`Σ bᵢ = 0`, seen from the other side: one node equation is implied by the others, "
             "which is why a transportation tableau with `m` rows and `n` columns has a basis of "
             "`m + n − 1` cells rather than `m + n`."),
            ("An unbounded arc contributes no row",
             "The capacity bounds are rows of the programme too, one per bounded arc. Write a "
             "network in which nothing is capacitated and the programme has node rows only: on "
             "the transportation data the lab solves a five-row programme in six variables, "
             "where the same six arcs with capacities would have given eleven rows. Which rows "
             "exist is a modelling decision, and it is visible in the size of the tableau."),
        ],
        "read_title": "The programme, and the four data sets that are the rest of the subject",
        "read_intro": "The matrix first, then the objective, then four instances solved by the same code with nothing changed but the numbers.",
        "body": [
            ("def", ("The minimum-cost flow problem",
                     "Given a directed network with costs `c`, capacities `u` and supplies `b`, "
                     "the <strong>minimum-cost flow problem</strong> is "
                     "`min cᵀx` subject to `Nx = b` and `0 ≤ x ≤ u`, where `N` is the "
                     "<strong>node-arc incidence matrix</strong>: one row per node, one column "
                     "per arc, `+1` at the tail, `−1` at the head.",
                     "It is a linear programme with equality rows, so it is solved by the "
                     "two-phase simplex method exactly as written. No new algorithm is "
                     "introduced here and none is needed.")),
            ("math", [
                "the network                     N   (rows s a b t, columns in arc order)",
                "",
                "   s>a  3:2                          s>a  s>b  a>b  a>t  b>t",
                "   s>b  3:3                    s      1    1    0    0    0",
                "   a>b  2:1                    a     -1    0    1    1    0",
                "   a>t  3:5                    b      0   -1   -1    0    1",
                "   b>t  3:2                    t      0    0    0   -1   -1",
                "",
                "   supplies  s: 4,  t: -4      the four rows sum to the zero row",
                "",
                "the programme     min 2x1 + 3x2 + x3 + 5x4 + 2x5",
                "                  N x = b,   0 ≤ x ≤ (3, 3, 2, 3, 3)",
                "                  4 node rows + 5 capacity rows = 9 rows, 5 columns",
                "",
                "the optimum       x = (3, 1, 2, 1, 3)        cost 22",
            ]),
            ("p", "Every one of those five numbers is a whole number. Nothing in the programme "
                  "asked for that: there is no integrality constraint anywhere, the simplex "
                  "method was free to stop at a corner with halves in it, and on a general "
                  "linear programme it very often does. It came out whole because of what `N` "
                  "is, and that is proved later on this course rather than left as a happy "
                  "observation."),
            ("h3", "The same programme, four more times"),
            ("p", "What follows is not a family of related problems. It is one programme, one "
                  "matrix and one objective, and the only thing that changes between the four is "
                  "what was typed into the boxes. The lab's mode for this lesson has a single "
                  "control for the data set and prints the same tableau each time."),
            ("example", ("Transportation",
                         "Two sources and three sinks, arcs from every source to every sink, no "
                         "capacity on any of them, supplies `20, 30` and demands `10, 25, 15`. "
                         "The programme has five rows &mdash; one per node and nothing else, "
                         "because no arc is bounded &mdash; and six columns.",
                         "The optimum ships `10` and `10` from the first source and `25` and `5` "
                         "from the second, for a total of 245. The tableau method usually taught "
                         "for this is in the next two lessons; the point here is that it does "
                         "not need one.")),
            ("example", ("Assignment",
                         "Three workers, three jobs, an arc from every worker to every job at "
                         "capacity 1, every supply `+1` and every demand `−1`. Fifteen rows and "
                         "nine columns.",
                         "The optimum is 9, at the assignment that gives the second job to the "
                         "first worker, the first to the second and the third to the third. "
                         "Every variable came out `0` or `1`: the programme is a transportation "
                         "problem whose margins happen to be ones, and no binary variable was "
                         "declared anywhere.")),
            ("example", ("Shortest path",
                         "One unit at the source, one unit demanded at the sink, every capacity "
                         "1, and the arc costs read as lengths. Moving a single unit as cheaply "
                         "as possible is moving it along the cheapest route.",
                         "On the lab's data the optimum is 6, carried on `s>b`, `b>a` and `a>t`. "
                         "Bellman-Ford's labels on the same network are `0, 3, 2, 6`, and the "
                         "label at the sink is the same 6 &mdash; the relaxation and the simplex "
                         "method reaching one number by different routes.")),
            ("example", ("Maximum flow",
                         "Price every arc at zero, add one arc from the sink back to the source "
                         "with no upper bound and a cost of `−1`, and supply nothing anywhere. "
                         "The only way to earn anything is to run flow round the loop, so "
                         "minimising the cost maximises the flow.",
                         "The optimum is `−5`, and 5 is the maximum flow &mdash; and also the "
                         "capacity of the smallest cut in the same network, which is the theorem "
                         "two lessons from the end of this course. The return arc is deliberately "
                         "unbounded: bounding it would cap the answer at whatever bound you "
                         "chose.")),
            ("h3", "What this buys, and what it costs"),
            ("p", "What it buys is that everything already proved about linear programmes now "
                  "applies to all four. A dual exists and its variables have units; "
                  "complementary slackness holds; a shadow price on a node row is worth something "
                  "per unit of supply. The rest of this course is mostly reading those duals, "
                  "and each one turns out to be an object with a name of its own."),
            ("p", "What it costs is speed, and honesty about that matters. A specialised method "
                  "that knows the basis is a spanning tree will beat a general tableau on a "
                  "large network, which is why such methods exist. On the size of instance this "
                  "course works with, the general programme is both fast enough and the right "
                  "reference: when a hand method and the programme disagree, the programme is "
                  "not the one that is wrong."),
        ],
        "lab": ("network", {
            "mode": "mincost",
            "preset": "mincost",
            "panel_title": "Change the data, and watch the model stay where it is",
            "panel_intro": "The drawing, the matrix `N`, the vector `b`, the bounds and the "
                           "solved programme are all on the page at once, and the data-set "
                           "control swaps between minimum-cost flow, transportation, assignment, "
                           "a shortest path and a maximum flow. Nothing about the programme "
                           "changes when you do: watch the matrix rather than the answer.",
        }),
        "steps_title": "Turning a network into a programme you can hand to the simplex method",
        "steps_intro": "Columns before rows, and the redundancy noticed on purpose rather than discovered by a solver.",
        "steps": [
            ("Index the arcs, and let that be the variable order",
             "The `j`-th arc is the `j`-th column and the `j`-th component of `x`. Fix this "
             "order once and write it down; almost every confusion later comes from a flow "
             "vector whose order stopped matching the arc list."),
            ("Build `N` one column at a time, not one row at a time",
             "For each arc write `+1` in its tail's row and `−1` in its head's row. Every "
             "column has exactly two non-zero entries, whatever the network looks like, and if "
             "one of yours does not then you have written a loop or missed an endpoint."),
            ("Write `b`, and check it sums to zero",
             "Positive where goods enter, negative where they leave, zero at every node that "
             "merely passes things on. The rows of `N` sum to zero, so the programme is "
             "infeasible unless `b` does too."),
            ("Add a bound row only for arcs that have one",
             "`xⱼ ≤ uⱼ` for each capacitated arc; nothing at all for the rest. Non-negativity is "
             "already part of the standard form and does not need a row."),
            ("Solve it, then read the answer back onto the drawing",
             "A vector of numbers is not a shipping plan until each component is written on its "
             "arc. Do this even when the answer looks obvious &mdash; it is how you notice that "
             "the optimum sends nothing at all down two of the routes."),
        ],
        "worked": {
            "title": "Four problems, one tableau, and the data that made each one",
            "intro": [
                "Each block below is what changed. The matrix is built the same way every time, "
                "the objective is `cᵀx` every time, and the solver is the same exact simplex "
                "every time."
            ],
            "lines": [
                "MINIMUM-COST FLOW     s>a 3:2  s>b 3:3  a>b 2:1  a>t 3:5  b>t 3:2",
                "   b   s:4  t:-4            u   (3, 3, 2, 3, 3)",
                "   9 rows (4 node + 5 capacity), 5 columns",
                "   x = (3, 1, 2, 1, 3)      cost 22        all whole",
                "",
                "TRANSPORTATION        S1,S2 to D1,D2,D3, every capacity *",
                "   c   4  6  9 / 5  3  8",
                "   b   S1:20  S2:30  D1:-10  D2:-25  D3:-15",
                "   5 rows (node rows only), 6 columns",
                "   x = (10, 0, 10, 0, 25, 5)      cost 245",
                "",
                "ASSIGNMENT            W1..W3 to J1..J3, every capacity 1",
                "   c   9  2  7 / 6  4  3 / 5  8  1",
                "   b   every W: +1     every J: -1",
                "   15 rows, 9 columns",
                "   x = (0,1,0, 1,0,0, 0,0,1)      cost 9      every entry 0 or 1",
                "",
                "SHORTEST PATH         every capacity 1, costs are lengths",
                "   b   s:1  t:-1",
                "   x = (0, 1, 1, 1, 0)      cost 6      the route s, b, a, t",
                "   Bellman-Ford labels on the same data:  0, 3, 2, 6",
                "",
                "MAXIMUM FLOW          every cost 0, plus  t>s *:-1,  b = 0 everywhere",
                "   x = (3, 2, 1, 2, 3, 5)      cost -5",
                "   the 5 on the return arc IS the flow value",
                "   smallest cut of the same network:  5",
            ],
            "after": [
                "The sizes are the part to notice. The transportation instance has five rows "
                "because not one of its arcs is capacitated; the assignment instance has fifteen "
                "because all nine are. Same programme, same builder, and the shape of the "
                "tableau is a consequence of the data rather than of the problem's name.",
                "For a rehearsal, take the shortest-path data and raise the capacity on every "
                "arc from 1 to 2 while leaving `b` at one unit. The answer does not move. Then "
                "ask yourself why the capacities were there at all &mdash; and notice that with "
                "`b` at one unit they never bind, so the honest model has no capacity rows in it.",
                "The harder rehearsal: change the maximum-flow instance's return arc from `*:-1` "
                "to `10:-1` and re-solve, then to `3:-1`. The first changes nothing; the second "
                "caps the answer at 3. A bound you invented has become the answer, which is the "
                "cost of modelling &ldquo;no limit&rdquo; with a number.",
            ],
        },
        "quiz_title": "One matrix, and what the data does to it",
        "quiz": [
            {"q": "What does column `j` of the node-arc incidence matrix `N` contain?",
             "a": ["A `1` in the row of every node arc `j` touches",
                   "`+1` in the row of arc `j`'s tail, `−1` in the row of its head, zero elsewhere",
                   "The capacity of arc `j` in its tail's row and the cost in its head's row",
                   "`+1` in the row of arc `j`'s head, and nothing else"],
             "c": 1,
             "why": "Two non-zero entries, always, with opposite signs. That is what makes row "
                    "`i` read as net outflow at node `i`, and it is also why the rows sum to "
                    "zero &mdash; every column contributes `+1` and `−1` to that sum. The first "
                    "choice describes the undirected incidence matrix, which is a different "
                    "matrix and behaves differently, as this course later shows."},
            {"q": "A transportation instance has six arcs, none of them capacitated, over five nodes. How many rows does its minimum-cost flow programme have?",
             "a": ["Five", "Six", "Eleven", "Thirty"],
             "c": 0,
             "why": "One row per node and nothing else: a bound row exists only for an arc that "
                    "has a bound. The assignment instance in the same lab has six nodes and nine "
                    "arcs all of capacity 1, and therefore fifteen rows. The number of rows is a "
                    "consequence of the data, not of the problem's name."},
            {"q": "In the maximum-flow instance, why is the return arc from the sink to the source given no upper bound?",
             "a": ["Because an arc with no upper bound is cheaper to solve",
                   "Because a bound on it would cap the flow at whatever bound was chosen",
                   "Because the return arc has to carry the same flow as the source arcs",
                   "Because a negative cost is only allowed on an unbounded arc"],
             "c": 1,
             "why": "The flow round the loop is the quantity being maximised, so any bound on "
                    "the return arc becomes a bound on the answer. Setting it to `3:-1` in the "
                    "lab caps the optimum at 3 on a network whose maximum flow is 5 &mdash; and "
                    "nothing in the output announces that the binding constraint is one you "
                    "invented."},
            {"q": "The minimum-cost flow instance solves to `x = (3, 1, 2, 1, 3)`, every component whole. Why?",
             "a": ["Because the simplex method returns whole numbers on whole data",
                   "Because the capacities were whole, which forces the flows to be",
                   "Because of a property of `N` that has to be proved, and is",
                   "Because the solver rounded, as every floating-point solver does"],
             "c": 2,
             "why": "None of the first three routes is available: the simplex method routinely "
                    "stops at fractional corners on whole data, whole capacities do not force "
                    "whole flows, and the arithmetic here is exact rather than rounded. The "
                    "reason is total unimodularity, and it is a determinant argument about `N` "
                    "given later on this course rather than an observation about this instance."},
        ],
        "mistakes": [
            ("Writing `N` row by row",
             "Going along node `i` and asking which arcs touch it invites you to put a `1` in "
             "for each, losing the sign that carries the direction. Build it column by column: "
             "each arc writes `+1` once and `−1` once, and a column with any other pattern is a "
             "data error you have just caught for free."),
            ("Adding a capacity row for every arc out of tidiness",
             "An uncapacitated arc with a row `xⱼ ≤ 1000` in the programme is a different model. "
             "The row can bind, it has a dual variable, and a shadow price will eventually be "
             "reported on a constraint that does not exist in the situation. If there is no "
             "bound, write no row."),
            ("Believing the four problems are analogies",
             "They are one programme. A reader who files transportation, assignment, shortest "
             "path and maximum flow as four topics with four methods will learn four sets of "
             "special cases and miss the single duality argument that covers all of them. "
             "The lab exists to make this hard to misremember: the matrix is on the screen "
             "while the data set changes under it."),
        ],
        "standard": ("Finish when you can take any of the four problems and write it as `min cᵀx` subject to `Nx = b`, `0 ≤ x ≤ u`, from scratch.",
                     "You should be able to build `N` column by column, say why its rows are "
                     "dependent, decide which arcs earn a capacity row, recognise the four "
                     "special cases by what their `b`, `u` and `c` look like, and read a solved "
                     "flow vector back onto the drawing."),
        "note": 'Every optimum in this lesson came out in whole units, on every one of the four data sets, and nothing in the programme required it. That is the single most useful fact about networks and it is not yet proved. The transportation lessons that follow will produce whole answers again, by a method that never mentions integrality either &mdash; and then “Total Unimodularity and Integer Corners” explains all of it with one argument about determinants.',
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "the-transportation-problem",
        "title": "The Transportation Problem",
        "module": "The transportation tableau",
        "one_line": "Balance the supplies against the demands, add a dummy row or column if they differ, and start from a basis of exactly m + n − 1 occupied cells.",
        "summary": (
            "The transportation problem is the minimum-cost flow programme laid out as a table: "
            "sources down the side, destinations across the top, a cost in every cell. Before "
            "anything can be solved the two margins have to agree, and a dummy row or column "
            "priced at zero is how that is arranged. Then a starting solution has to occupy "
            "exactly the right number of cells &mdash; and one of the two standard rules "
            "sometimes cannot."
        ),
        "key": [
            "m sources, n destinations, cost cᵢⱼ in every cell, ship xᵢⱼ ≥ 0",
            "row i sums to supply sᵢ,  column j sums to demand dⱼ,   min Σ cᵢⱼ xᵢⱼ",
            "Σ sᵢ ≠ Σ dⱼ  ⟹  add a dummy column (surplus) or dummy row (shortfall) at cost 0",
            "a basis is m + n − 1 occupied cells forming a spanning tree of rows and columns",
            "north-west corner    ignores every cost;   least cost    reads them and is greedy",
            "fewer than m + n − 1 occupied  ⟹  place a ZERO, do not carry on",
        ],
        "key_label": "The tableau, the balance condition, and the count that has to come out right",
        "concepts_intro": (
            "Two of the three ideas here are about arithmetic that happens before any "
            "optimisation, and they are where the instances go wrong."
        ),
        "concepts": [
            ("Balancing adds, and it never reprices",
             "If supply exceeds demand, add one destination that absorbs the difference at a "
             "cost of zero per unit; if demand exceeds supply, add one source. Every real cost "
             "in the table is left exactly as it was &mdash; the lab checks this on all three of "
             "its worked examples and reports that not one real unit cost moved. A dummy is a "
             "bookkeeping device for making the two margins agree, and it must not be allowed to "
             "express an opinion."),
            ("The basis count is m + n − 1, and it comes from the rank",
             "There are `m + n` constraints and only `m + n − 1` independent ones, because the "
             "rows of the incidence matrix sum to zero. So a basic solution occupies "
             "`m + n − 1` cells, and those cells must form a spanning tree of the bipartite "
             "graph of rows and columns: connected, so every potential is determined, and "
             "acyclic, so none is over-determined."),
            ("A start can be degenerate, and two different things are meant by that",
             "The count can be met with some occupied cells carrying zero &mdash; those zeros "
             "are real basic cells and the lab names them rather than dropping them. Or the "
             "count can be missed altogether, which is worse: the occupied cells then fall into "
             "two disconnected pieces and the potentials cannot be solved for at all. The repair "
             "is to place a zero in a cell that joins two pieces without closing a cycle."),
        ],
        "read_title": "Getting a transportation problem to the point where it can be solved",
        "read_intro": "The table and what it is, then balancing, then the two starting rules and the count each one has to satisfy.",
        "body": [
            ("def", ("The transportation problem",
                     "Given `m` sources with supplies `sᵢ`, `n` destinations with demands `dⱼ`, "
                     "and a unit cost `cᵢⱼ` for each pair, the <strong>transportation "
                     "problem</strong> is to choose `xᵢⱼ ≥ 0` minimising `Σ cᵢⱼ xᵢⱼ` subject to "
                     "each row summing to its supply and each column to its demand.",
                     "It is <strong>balanced</strong> when `Σ sᵢ = Σ dⱼ`. Only a balanced "
                     "problem has a feasible solution, because the row equations and the column "
                     "equations both add up to the total shipped.")),
            ("p", "This is the minimum-cost flow programme with the drawing removed. The sources "
                  "and destinations are the nodes, the cells are the arcs, no arc has a capacity "
                  "&mdash; and the node equations, written as a table, become &ldquo;each row "
                  "sums to its supply, each column to its demand&rdquo;. A tableau is worth "
                  "having anyway, because the structure it exposes is what the method in the "
                  "&ldquo;Potentials and the Stepping-Stone Cycle&rdquo; exploits."),
            ("math", [
                "                D1    D2    D3    D4     supply",
                "   Plant A      10     2    20    11        15",
                "   Plant B      12     7     9    20        25",
                "   Plant C       4    14    16    18        10",
                "   demand        5    15    15    15",
                "",
                "   total supply 15 + 25 + 10 = 50",
                "   total demand  5 + 15 + 15 + 15 = 50        balanced, no dummy",
                "",
                "   m + n - 1  =  3 + 4 - 1  =  6 occupied cells in a basis",
            ]),
            ("h3", "When the margins do not agree"),
            ("p", "Two cases, one fix each. More supply than demand: add a dummy destination "
                  "whose demand is the difference, with a cost of zero in every cell of its "
                  "column. More demand than supply: add a dummy source with that supply and a "
                  "zero row. Either way the problem becomes balanced, every real cost is "
                  "untouched, and units sent to the dummy are units that never move."),
            ("example", ("A surplus of ten",
                         "Three mills supplying `20, 30, 25` and three yards demanding "
                         "`20, 25, 20`: 75 available and 65 wanted. The lab adds a dummy "
                         "destination carrying 10, both totals become 75, and the three costs in "
                         "the new column are `0, 0, 0`.",
                         "The optimum for this instance costs 605, and whichever plan is chosen, "
                         "exactly 10 units go to the dummy &mdash; they have nowhere else to go. "
                         "That is what makes a uniform dummy price harmless and a non-uniform "
                         "one dangerous.")),
            ("example", ("A shortfall of five",
                         "Two sources supplying `4` and `6` against demands of `5, 5, 5`: 10 "
                         "available and 15 wanted. A dummy source of 5 is added, with the row "
                         "`0, 0, 0`, and both sides become 15.",
                         "The dummy row now says which destinations go short, and by how much. "
                         "That is genuinely useful output and it is the reason the dummy is part "
                         "of the model rather than an apology for it.")),
            ("h3", "Two ways to start, and the count both have to meet"),
            ("p", "The <strong>north-west corner rule</strong> fills the top-left cell with as "
                  "much as its row and column allow, crosses off whichever is exhausted, and "
                  "repeats. It never looks at a single cost. The <strong>least-cost rule</strong> "
                  "picks the cheapest remaining cell instead, so it reads the costs and is "
                  "greedy. Both produce a basic feasible solution; neither produces an optimum, "
                  "and neither claims to."),
            ("example", ("Two starts on the same table",
                         "On the three-plant table above, the north-west rule occupies six cells "
                         "and ships at a cost of 520. The least-cost rule occupies six cells too "
                         "and ships at 475, one of which carries zero &mdash; the cell joining "
                         "the second plant to the second depot.",
                         "The optimum is 435, so neither start is close and the cheaper start is "
                         "not automatically the better one to start from. What matters is that "
                         "both are bases: six cells, spanning, acyclic.")),
            ("example", ("A start that cannot be priced",
                         "On the lab's third table &mdash; three depots and three shops where "
                         "the north-west rule ties &mdash; the least-cost rule occupies only "
                         "four cells where five are needed, and those four fall into two "
                         "disconnected pieces. The potentials of the lesson that follows then cannot be "
                         "solved for: three of the six never get a value.",
                         "The lab repairs it by placing a zero allocation in the cell joining "
                         "the first depot to the first shop, which is the cheapest cell that "
                         "joins two pieces of the forest without closing a cycle. The count is "
                         "restored to five, the basis becomes a spanning tree, and the method "
                         "can start. The north-west rule on the same data occupies five cells, "
                         "two of them carrying zero.")),
            ("p", "Those zeros are not decoration and they are not absences. A basic cell "
                  "carrying zero is in the basis, it has a potential equation, and it can be the "
                  "cell that leaves at the next pivot. A reader who quietly drops them will find "
                  "the count wrong two steps later and will not know when it went wrong."),
        ],
        "lab": ("transport", {
            "mode": "setup",
            "preset": "balanced",
            "panel_title": "Balance the table, then build a start one cell at a time",
            "panel_intro": "The occupied-cell count is displayed against `m + n − 1` at every "
                           "step of both rules, so a start that falls short announces itself "
                           "while it is being built. Editing the supplies or the demands adds or "
                           "removes the dummy live, and the real cells are never repriced.",
        }),
        "steps_title": "Setting a transportation problem up so that it can be solved",
        "steps_intro": "Balance, then start, then count. The count is not a formality: everything in &ldquo;Potentials and the Stepping-Stone Cycle&rdquo; assumes it.",
        "steps": [
            ("Add both margins and compare them",
             "`Σ sᵢ` against `Σ dⱼ`. Equal, and you have a balanced problem. Otherwise note the "
             "difference and which side is short, because that decides whether you are adding a "
             "column or a row."),
            ("Add the dummy, priced at zero, and change nothing else",
             "A dummy destination absorbs surplus supply; a dummy source covers unmet demand. "
             "Every cell in it costs zero. Resist the urge to charge for the dummy, and if you "
             "think the situation really does have a penalty for unmet demand, put that penalty "
             "in the model deliberately and say so."),
            ("Build a start by one rule, and write the amount in each cell as you go",
             "North-west if you want the count to be the only thing you are thinking about, "
             "least-cost if you want to open nearer the optimum. Cross off a row or a column "
             "each time, never both, unless the problem is over."),
            ("Count the occupied cells against `m + n − 1`",
             "Too many is impossible if you crossed off one line at a time. Exactly right, "
             "including any zeros, and you have a basis. Too few means the start is degenerate "
             "in the serious sense and needs repair before anything else happens."),
            ("Repair a short count by placing a zero that joins two pieces",
             "Find a cell whose row belongs to one component of the occupied cells and whose "
             "column belongs to another, put a zero in it, and treat it as basic. Placing the "
             "zero inside a component instead closes a cycle and leaves you no better off."),
        ],
        "worked": {
            "title": "Three tables: one balanced, one with a surplus, one that ties",
            "intro": [
                "The counts are the thing to follow. Every figure below is what the lab reports "
                "as the start is built, and two of the three starts are degenerate in one of the "
                "two senses."
            ],
            "lines": [
                "TABLE 1   3 x 4, supply 15 25 10, demand 5 15 15 15      50 = 50, no dummy",
                "   m + n - 1 = 6",
                "   north-west   (1,1)=5  (1,2)=10  (2,2)=5  (2,3)=15  (2,4)=5  (3,4)=10",
                "                6 of 6 occupied, none zero        cost 520",
                "   least cost   (1,2)=15 (3,1)=5   (2,2)=0   (2,3)=15 (3,4)=5  (2,4)=10",
                "                6 of 6 occupied, (2,2) is ZERO   cost 475",
                "   the optimum, for later                        cost 435",
                "",
                "TABLE 2   3 x 3, supply 20 30 25, demand 20 25 20        75 vs 65",
                "   dummy DESTINATION carrying 10, column of costs 0 0 0",
                "   now 3 x 4 and 75 = 75,  m + n - 1 = 6",
                "   north-west   6 of 6, with (2,1) carrying ZERO  cost 765",
                "   least cost   6 of 6, none zero                 cost 665",
                "   the optimum, for later                         cost 605",
                "",
                "TABLE 3   3 x 3, supply 10 20 10, demand 10 20 10        40 = 40",
                "   m + n - 1 = 5",
                "   north-west   5 of 5, with (2,1) and (3,2) ZERO  cost 240",
                "   least cost   4 of 5  -- SHORT",
                "                the four cells fall into 2 components",
                "                potentials: 3 of the 6 never get a value",
                "                repair: place a zero at (1,1), which costs 5 and joins",
                "                        two pieces without closing a cycle",
                "                5 of 5, spanning, and the method can start",
                "   the optimum, for later                          cost 150",
            ],
            "after": [
                "Table 3's least-cost start is the instructive one, and notice what it is not: "
                "it is not wrong, and it is not infeasible. It ships 40 units at a cost of 150, "
                "which happens to be the optimum. It simply is not a <em>basis</em>, so the "
                "machinery that proves optimality has nothing to stand on &mdash; and a reader "
                "who does not count will conclude the method is broken.",
                "For a rehearsal, take table 2 and change the demands to `20, 25, 30`. Supply "
                "and demand now both come to 75, the dummy disappears, and the tableau goes back "
                "to three by three with a basis of five. Watch the count control as you type: it "
                "is the fastest way to internalise where `m + n − 1` comes from.",
                "The harder rehearsal: on table 1, build the north-west start and then "
                "deliberately drop the smallest allocation, leaving five cells. Ask the lab for "
                "the potentials. You will get a disconnected forest and a refusal, which is "
                "exactly what happens to a reader who treats a zero allocation as an empty cell.",
            ],
        },
        "quiz_title": "Balancing, the dummy, and the count",
        "quiz": [
            {"q": "A transportation problem has total supply 75 and total demand 65. What is added, and at what cost?",
             "a": ["A dummy source of 10, priced at zero",
                   "A dummy destination of 10, priced at zero",
                   "A dummy destination of 10, priced at the highest real cost in the table",
                   "Nothing: the ten surplus units are simply not shipped"],
             "c": 1,
             "why": "Surplus supply needs somewhere to go, so the dummy is a destination, and "
                    "its column costs zero because units sent there do not move. Pricing it at "
                    "the dearest real route is the usual instinct and it is discussed in the "
                    "following lesson, where the lab measures what it does and does not change. "
                    "Leaving the problem unbalanced is not an option: the row and column "
                    "equations then contradict each other."},
            {"q": "A three-by-four transportation tableau has a starting solution occupying five cells. What does that mean?",
             "a": ["It is optimal, since fewer cells means a cheaper plan",
                   "It is infeasible and must be rebuilt",
                   "It is feasible but not a basis: six cells are needed, and a zero must be placed",
                   "It has one cell too many and one allocation must be removed"],
             "c": 2,
             "why": "`m + n − 1` is `3 + 4 − 1 = 6`. Five occupied cells can ship every unit "
                    "perfectly well &mdash; the plan may even be optimal, as one of the lab's "
                    "tables shows &mdash; but the occupied cells then fall into more than one "
                    "component and the potentials cannot all be determined. The repair is a zero "
                    "in a cell joining two components."},
            {"q": "Why is the basis size `m + n − 1` rather than `m + n`?",
             "a": ["Because one destination is always supplied by a dummy",
                   "Because the row and column equations are dependent: they add to the same total",
                   "Because the north-west corner rule stops one cell early",
                   "Because the last cell is determined by non-negativity"],
             "c": 1,
             "why": "Both margins sum to the total shipped, so any one equation follows from the "
                    "others: the constraint matrix has rank `m + n − 1`. This is the "
                    "transportation tableau's version of the fact that the rows of a node-arc "
                    "incidence matrix sum to zero, and it is the same fact."},
            {"q": "A basic cell in a transportation tableau carries an allocation of zero. What should you do with it?",
             "a": ["Remove it, since nothing is shipped there",
                   "Keep it as a basic cell: it is in the basis and can be the cell that leaves",
                   "Replace it with a tiny positive number so the count still works",
                   "Move the allocation from the cheapest occupied cell into it"],
             "c": 1,
             "why": "A basic cell carrying zero is a basic cell. It has a potential equation, it "
                    "can be part of a stepping-stone cycle, and it can leave the basis at the "
                    "next pivot &mdash; which is exactly what happens on the lab's default run, "
                    "where one pivot moves a quantity of zero and changes the basis without "
                    "changing the cost. Removing it breaks the count; substituting an epsilon is "
                    "an old device that exact arithmetic makes unnecessary."},
        ],
        "mistakes": [
            ("Pricing the dummy at something other than zero",
             "Charging the dummy column the dearest real rate is a widespread instinct, and the "
             "reasoning behind it &mdash; that not shipping should be discouraged &mdash; "
             "describes a different problem. In this one every feasible plan sends the same "
             "amount to the dummy, so a uniform price adds the same constant to every plan. It "
             "cannot change the answer, and the following lesson measures what it does change."),
            ("Treating a zero allocation as an empty cell",
             "The count then reads one short, the forest breaks into pieces, and the potentials "
             "come back undetermined &mdash; usually two or three steps after the zero was "
             "dropped, by which time the cause is invisible. Write the zeros in, and if the "
             "tableau looks untidy, that is what it is supposed to look like."),
            ("Crossing off a row and a column at the same step",
             "When an allocation exhausts a row and a column together, only one of them may be "
             "crossed off; the other stays with a remaining quantity of zero and the next cell "
             "placed in it carries a zero allocation. Crossing off both is precisely how a start "
             "ends up one cell short, and it is the commonest way to produce the degenerate "
             "start that cannot be priced."),
        ],
        "standard": ("Finish when you can take an unbalanced cost table and hand back a balanced tableau with a correctly counted basis.",
                     "You should be able to decide whether a dummy row or a dummy column is "
                     "needed and price it at zero, build a start by either rule, count the "
                     "occupied cells against `m + n − 1` including zeros, and repair a short "
                     "count by placing a zero in a cell that joins two components of the "
                     "occupied forest."),
        "note": 'Nothing has been optimised yet, and two of the three tables already have a start that would break a careless method. That is the honest proportion for this subject. The next lesson, “Potentials and the Stepping-Stone Cycle”, prices every empty cell against the basis, finds the cycle that a candidate cell creates, and moves flow round it &mdash; and it needs the count to be exactly right before it can do any of that.',
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "potentials-and-the-stepping-stone-cycle",
        "title": "Potentials and the Stepping-Stone Cycle",
        "module": "The transportation tableau",
        "one_line": "Price every empty cell from the basis, find the unique cycle an entering cell creates, and move as much round it as the minus cells allow.",
        "summary": (
            "Solve `uᵢ + vⱼ = cᵢⱼ` on the occupied cells and every empty cell gets a reduced "
            "cost. A negative one means an improvement, and taking it means finding the unique "
            "cycle that cell closes in the basis and alternating plus and minus round it. The "
            "potentials are the dual solution, the reduced costs are the dual constraints, and "
            "the method is the simplex method with the tableau drawn differently."
        ),
        "key": [
            "uᵢ + vⱼ = cᵢⱼ  on every BASIC cell         m + n − 1 equations, m + n unknowns",
            "fix one potential — any one — and the rest follow; the reduced costs do not move",
            "reduced cost of an empty cell    c̄ᵢⱼ = cᵢⱼ − uᵢ − vⱼ",
            "all c̄ᵢⱼ ≥ 0  ⟺  optimal                  a negative one is an improving direction",
            "the entering cell closes ONE cycle in the basis; alternate + and − round it",
            "θ = the smallest allocation on a minus cell, and that cell leaves the basis",
        ],
        "key_label": "The dual on the left, the pivot on the right",
        "concepts_intro": (
            "Two of these are the simplex method in disguise. The third is the one readers get "
            "wrong on paper, because the shape they expect is not always the shape they get."
        ),
        "concepts": [
            ("The potentials are the dual, and one of them is free",
             "There are `m + n` potentials and only `m + n − 1` equations, so the system is "
             "under-determined by exactly one degree of freedom. Fixing `u₁ = 0` is a "
             "normalisation, not a fact: fix any other potential instead and every `u` and every "
             "`v` moves, while not one reduced cost changes. The lab recomputes the entire "
             "reduced-cost table under any normalisation you choose, so this is watched rather "
             "than asserted."),
            ("A reduced cost is what a route would save, per unit",
             "`c̄ᵢⱼ = cᵢⱼ − uᵢ − vⱼ` is the difference between shipping through cell `(i, j)` and "
             "shipping the same unit round the basis. Negative means the route is cheaper than "
             "the current plan by that much per unit; zero on every empty cell means no route is "
             "cheaper, which is optimality. This is the dual-feasibility test from the duality "
             "course, written for a tableau."),
            ("The cycle is a cycle, and it is not always a rectangle",
             "Adding one cell to a spanning tree creates exactly one cycle, and that cycle is "
             "what the flow moves round. Readers reach for a rectangle &mdash; along the row, "
             "down the column, back &mdash; and on the lab's default start the very first pivot "
             "has a six-cornered staircase instead, with the rectangle's fourth corner falling "
             "on an empty cell. A cycle may cross an empty cell; it may only turn at an occupied "
             "one."),
        ],
        "read_title": "Pricing the empty cells, and moving flow round the cycle that follows",
        "read_intro": "The potentials and what they are, then the reduced costs, then the pivot in full on a table where the obvious shape fails.",
        "body": [
            ("def", ("Potentials and reduced costs",
                     "Given a basis of `m + n − 1` occupied cells, the "
                     "<strong>potentials</strong> `uᵢ` and `vⱼ` are the solution of "
                     "`uᵢ + vⱼ = cᵢⱼ` over those cells, with one potential fixed arbitrarily. "
                     "The <strong>reduced cost</strong> of any cell is "
                     "`c̄ᵢⱼ = cᵢⱼ − uᵢ − vⱼ`.",
                     "Basic cells have reduced cost zero by construction. If every empty cell "
                     "has `c̄ᵢⱼ ≥ 0` the current plan is optimal; otherwise a cell with "
                     "`c̄ᵢⱼ &lt; 0` enters.")),
            ("p", "The system is solvable exactly when the occupied cells form a spanning tree, "
                  "which is why the count mattered so much in &ldquo;The Transportation Problem&rdquo;. Connected "
                  "gives every potential a value; acyclic stops two equations from disagreeing "
                  "about one of them. Solve it by starting anywhere and walking the tree: each "
                  "basic cell hands a known `u` to an unknown `v` or the other way round."),
            ("math", [
                "the north-west start on the three-plant table, basis in bold",
                "",
                "              D1     D2     D3     D4      u",
                "   A         [5]   [10]      .      .      0",
                "   B           .    [5]   [15]    [5]      5",
                "   C           .      .      .   [10]      3",
                "   v          10      2      4     15",
                "",
                "   check   u_A + v_D1 = 0 + 10 = 10 = c        ok",
                "           u_B + v_D3 = 5 +  4 =  9 = c        ok",
                "",
                "reduced costs   c - u - v   on every cell",
                "",
                "              D1     D2     D3     D4",
                "   A           0      0     16     -4",
                "   B          -3      0      0      0",
                "   C          -9      9      9      0",
                "",
                "   most negative:  (C, D1) at -9        Dantzig's rule",
                "   first negative: (A, D4) at -4        Bland's rule",
            ]),
            ("p", "Fix `u_A = 0` and the potentials are `u = (0, 5, 3)`, `v = (10, 2, 4, 15)`. "
                  "Fix `v_D1 = 0` instead and they become `u = (10, 15, 13)`, "
                  "`v = (0, −8, −6, 5)` &mdash; every one of the seven has moved, by 10. Not one "
                  "of the twelve reduced costs changes, because each is `cᵢⱼ − uᵢ − vⱼ` and the "
                  "shift cancels. The lab has a control for each of the seven and reports the "
                  "shift each produces: `0, 5, 3, −10, −2, −4, −15`."),
            ("h3", "Taking the cell, and the cycle it closes"),
            ("p", "The basis is a spanning tree of the rows and columns. Adding one more cell to "
                  "a spanning tree creates exactly one cycle, and that cycle alternates between "
                  "moving along a row and moving down a column. Put a plus on the entering cell, "
                  "then alternate signs round the cycle. Every plus cell gains `θ`, every minus "
                  "cell loses it, and the row and column sums are unchanged for every `θ`."),
            ("example", ("The staircase, on the first pivot",
                         "`(C, D1)` enters with a reduced cost of `−9`. The cycle the lab "
                         "computes has six corners: `(C,D1)+ (C,D4)− (B,D4)+ (B,D2)− (A,D2)+ "
                         "(A,D1)−`. The rectangle a reader guesses &mdash; along row C, up "
                         "column D1 &mdash; would need to turn at `(B, D1)`, and `(B, D1)` is "
                         "empty, so the guess is refused and the walk goes further.",
                         "`θ` is the smallest allocation on a minus cell: the minus cells carry "
                         "`10`, `5` and `5`, so `θ = 5` and `(B, D2)` leaves. The cost falls "
                         "from 520 to 475, which is `9 × 5` less.")),
            ("p", "The lab draws the guess alongside the computed cycle and names the corner "
                  "that breaks it. On the second pivot of the same run the guess closes and the "
                  "two agree; on the third, the entering cell's column holds no other occupied "
                  "cell at all, so there is no rectangle to draw. The guess is not always wrong, "
                  "which is exactly why it has to be checked."),
            ("h3", "Degeneracy, and what it does to the cost"),
            ("example", ("A pivot that changes the basis and not the bill",
                         "The second pivot of the default run brings `(A, D4)` in, and the "
                         "smallest allocation on a minus cell is `0` &mdash; the zero at "
                         "`(A, D1)`. So `θ = 0`: the cell enters, `(A, D1)` leaves, the basis is "
                         "different, and the cost stands still at 475.",
                         "The run's costs are `520 → 475 → 475 → 435`, and an implementation "
                         "asserting that every iteration is strictly cheaper would fail on the "
                         "shipped example. Non-increasing is the claim. This is the degeneracy "
                         "of the simplex course, arriving in a tableau that looks nothing like a "
                         "simplex tableau.")),
            ("p", "Three pivots from the north-west start, one from the least-cost start, and "
                  "both land on 435 at the same plan. The entering rule moves the path and not "
                  "the destination: on the surplus table, Dantzig's rule takes three pivots from "
                  "either start while Bland's takes four from one and six from the other, all "
                  "four finishing at 605."),
            ("p", "And the dummy question from &ldquo;The Transportation Problem&rdquo; can now be settled with a "
                  "number. Price the dummy column at ten times the dearest real route &mdash; "
                  "160 rather than 0 &mdash; and re-solve the surplus table. The real shipping "
                  "bill is 605 either way. Every feasible plan sends the same 10 units to the "
                  "dummy, so the penalty adds a constant of 1600 to every plan and the cheapest "
                  "one cannot move. What does move is the least-cost <em>start</em>, from 665 to "
                  "635, because that rule reads the cost table; the north-west start does not "
                  "move at all, because it never reads one."),
        ],
        "lab": ("transport", {
            "mode": "modi",
            "preset": "balanced",
            "panel_title": "One pivot at a time, with the cycle drawn on the tableau",
            "panel_intro": "The potentials, the reduced costs, the entering cell under either "
                           "rule, the cycle with a plus or a minus on every corner, `θ` "
                           "tabulated over the minus cells and a ring on the cell that leaves. "
                           "The rectangle a reader guesses first is drawn too, and when it fails "
                           "the corner that breaks it is highlighted rather than described.",
        }),
        "steps_title": "One iteration, start to finish",
        "steps_intro": "Potentials, prices, entering cell, cycle, theta, leaving cell. Then do it again; there is nothing else in the method.",
        "steps": [
            ("Solve the potentials on the occupied cells",
             "Fix one &mdash; any one &mdash; and walk the tree, each basic cell determining one "
             "new potential from one already known. If you get stuck with potentials still "
             "unknown, the basis is disconnected and the repair from &ldquo;The Transportation Problem&rdquo; is needed."),
            ("Price every empty cell, and check the basic ones came out zero",
             "`c̄ᵢⱼ = cᵢⱼ − uᵢ − vⱼ`. The basic cells must all price at zero; if one does not, "
             "the potentials are wrong and there is no point going on. All non-negative on the "
             "empty cells means you have finished."),
            ("Choose the entering cell by a stated rule",
             "Most negative, or first negative in row order. Say which you are using: they pick "
             "different cells on the very first tableau of the worked example, and they take "
             "different numbers of pivots to the same answer."),
            ("Trace the cycle, turning only where something is allocated",
             "From the entering cell, alternate row moves and column moves back to where you "
             "started. Every corner after the first must be an occupied cell. You may cross an "
             "empty cell in passing; you may not turn at one, and the cycle is unique so there "
             "is nothing to choose."),
            ("Move `θ` round it and update",
             "`θ` is the smallest allocation on a minus corner. Add it to the plus corners, take "
             "it off the minus corners, and remove exactly one cell that hit zero &mdash; if two "
             "did, keep one as a basic zero, or the count breaks."),
        ],
        "worked": {
            "title": "The default table, from the north-west start to the optimum",
            "intro": [
                "Three pivots. Everything below is what the lab reports at each step, including "
                "the degenerate one and the two occasions on which the rectangle guess fails."
            ],
            "lines": [
                "START   north-west, cost 520",
                "   basis  (1,1)=5 (1,2)=10 (2,2)=5 (2,3)=15 (2,4)=5 (3,4)=10",
                "",
                "PIVOT 1   u = (0, 5, 3)    v = (10, 2, 4, 15)",
                "   reduced     0   0  16  -4  /  -3   0   0   0  /  -9   9   9   0",
                "   enters      (3,1) at -9                 Dantzig",
                "   guess       rectangle turns at (2,1), which is EMPTY   REFUSED",
                "   cycle       (3,1)+ (3,4)- (2,4)+ (2,2)- (1,2)+ (1,1)-   six corners",
                "   theta       min(10, 5, 5) = 5,  and (2,2) leaves",
                "   cost        520 - 9(5) = 475",
                "",
                "PIVOT 2   u = (0, -4, -6)  v = (10, 2, 13, 24)",
                "   enters      (1,4) at -13",
                "   guess       (1,4) (1,1) (3,1) (3,4) closes on four occupied corners",
                "   cycle       the same four",
                "   theta       0,  and (1,1) leaves            DEGENERATE",
                "   cost        475 - 13(0) = 475               unchanged",
                "",
                "PIVOT 3   u = (0, 9, 7)    v = (-3, 2, 0, 11)",
                "   enters      (2,2) at -4",
                "   guess       no rectangle: column 3 holds no other occupied cell",
                "   cycle       (2,2)+ (2,4)- (1,4)+ (1,2)-",
                "   theta       10,  and (2,4) leaves",
                "   cost        475 - 4(10) = 435",
                "",
                "STOP      u = (0, 5, 7)    v = (-3, 2, 4, 11)",
                "   reduced    13  0  16  0  / 10  0  0  4  /  0  5  5  0",
                "   none negative, so 435 is optimal",
                "   plan       0  5  0 10  /  0 10 15  0  /  5  0  0  5",
                "",
                "from the LEAST-COST start the same table needs ONE pivot, to the same 435",
            ],
            "after": [
                "Pivot 2 is the one to sit with. A cell enters, a cell leaves, the plan does not "
                "move an ounce of anything, and the cost is identical. That is not a bug and it "
                "is not a waste: the basis has changed, and the next tableau prices the cells "
                "differently because of it, which is how pivot 3 becomes available.",
                "For a rehearsal, run the same table from the least-cost start. It opens at 475 "
                "and one pivot takes it to 435. Then ask which start you would rather have: the "
                "cheaper opening took fewer pivots here, and on the surplus table it takes more "
                "under one of the two entering rules. There is no theorem in this neighbourhood, "
                "which is worth knowing.",
                "The harder rehearsal: switch the entering rule to Bland's and run the default "
                "table again. The first cell to enter is now `(1,4)` at `−4` rather than `(3,1)` "
                "at `−9`, and the path is different all the way down. Both finish at 435. A "
                "pivot rule is a policy about the route, not about the destination.",
            ],
        },
        "quiz_title": "Potentials, prices and the cycle",
        "quiz": [
            {"q": "You solve the potentials with `u₁ = 0` and then again with `v₁ = 0`. What changes?",
             "a": ["Every potential moves, and every reduced cost moves with it",
                   "Every potential moves, and not one reduced cost changes",
                   "Nothing moves: the potentials are determined by the costs",
                   "Only the potentials in the first row and first column move"],
             "c": 1,
             "why": "There are `m + n` unknowns and `m + n − 1` independent equations, so one "
                    "potential is free. On the lab's first tableau, fixing `v₁ = 0` instead of "
                    "`u₁ = 0` shifts all seven by 10 &mdash; and each reduced cost is "
                    "`cᵢⱼ − uᵢ − vⱼ`, in which the shift appears once positively and once "
                    "negatively and cancels. That is what makes the choice a normalisation."},
            {"q": "An entering cell's stepping-stone cycle passes through a cell that is empty. Is that allowed?",
             "a": ["No: every corner of the cycle must be occupied",
                   "Yes if the cycle crosses it in a straight line, but it may not turn there",
                   "Yes, and it may turn there provided the allocation would stay non-negative",
                   "Only if the empty cell is in the entering cell's own row"],
             "c": 1,
             "why": "A corner is where the path changes between a row move and a column move, "
                    "and every corner after the entering cell must carry an allocation, because "
                    "only allocated cells can give up `θ`. Crossing an unoccupied cell in "
                    "passing changes nothing. The lab's own check refuses a drawn cycle that "
                    "turns at an empty cell and names the cell."},
            {"q": "A pivot is taken and `θ` comes out zero. What has happened?",
             "a": ["The tableau is optimal and the method should stop",
                   "The entering cell was chosen wrongly",
                   "The basis changes, the plan does not, and the cost stands still",
                   "The problem is unbounded"],
             "c": 2,
             "why": "A minus corner already carrying zero caps `θ` at zero. The entering cell "
                    "joins the basis, the zero cell leaves, and nothing is shipped differently "
                    "&mdash; but the potentials and hence every reduced cost are recomputed from "
                    "the new basis, which is what makes progress possible afterwards. The "
                    "default run costs 520, 475, 475 and 435 for exactly this reason."},
            {"q": "On a transportation problem with a dummy column, you price the dummy at ten times the dearest real route instead of at zero. What happens to the optimal plan?",
             "a": ["It gets cheaper, because the penalty discourages waste",
                   "It does not change, because every feasible plan sends the same amount to the dummy",
                   "It changes, because the reduced costs in the dummy column all move",
                   "It becomes infeasible"],
             "c": 1,
             "why": "The dummy's column demand is fixed, so every feasible plan sends exactly "
                    "that quantity there and a uniform price adds the same constant to all of "
                    "them. On the lab's surplus table the constant is 1600 and the real bill "
                    "stays at 605. What does move is the least-cost starting rule, from 665 to "
                    "635, because that rule reads the cost table &mdash; the north-west rule, "
                    "which does not, gives the same start either way."},
        ],
        "mistakes": [
            ("Believing `u₁ = 0` is part of the method",
             "It is one arbitrary choice out of `m + n`, made so that a solvable system has a "
             "unique answer. Readers who think the potentials are determined go looking for an "
             "error when someone else's `u` and `v` differ from theirs by a constant, and "
             "sometimes recompute a whole tableau over it. Check the reduced costs instead: "
             "those really are determined, and they are what the method uses."),
            ("Looking for a rectangle instead of tracing the cycle",
             "On the lab's very first pivot the cycle has six corners, and the rectangle a "
             "reader draws needs to turn on an empty cell. The habit survives because rectangles "
             "are common &mdash; the second pivot of the same run is one &mdash; which makes it "
             "worse, not better. Trace the path: alternate row and column moves, turn only "
             "where something is allocated, and stop when you are back at the start."),
            ("Removing two cells when two of them hit zero together",
             "If `θ` is attained on more than one minus corner, exactly one of them leaves and "
             "the others stay in the basis carrying zero. Removing both drops the count below "
             "`m + n − 1`, the basis stops being a spanning tree, and the next set of potentials "
             "cannot be solved for &mdash; with the cause now several steps behind you."),
        ],
        "standard": ("Finish when you can run a full iteration by hand and produce the cycle without guessing its shape.",
                     "You should be able to solve the potentials from any normalisation, price "
                     "every empty cell, state the entering rule you are using and apply it, "
                     "trace the unique cycle turning only at occupied cells, compute `θ` over the "
                     "minus corners, and say which cell leaves &mdash; including when `θ` is "
                     "zero."),
        "note": 'Both the transportation optima on this lesson came out in whole units, and so did every intermediate plan, and nothing in the method ever mentioned integrality: `θ` was the smallest of a set of whole allocations, so it was whole, so every updated allocation was whole. That argument only works because the cycle has coefficients of plus and minus one, which is a property of the matrix. The next lesson, “Total Unimodularity and Integer Corners”, is where that property gets a name and a proof &mdash; and where a matrix that does not have it produces a corner made of halves.',
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "total-unimodularity-and-integer-corners",
        "title": "Total Unimodularity and Integer Corners",
        "module": "Integer corners",
        "one_line": "Every square submatrix of a node-arc incidence matrix has determinant 0, +1 or −1 — and Cramer's rule turns that into whole-numbered corners.",
        "summary": (
            "Every optimum so far has come out in whole units without anyone asking. The reason "
            "is a property of the matrix: every square submatrix of a node-arc incidence matrix "
            "has determinant zero, one or minus one, so Cramer's rule divides by one and a basic "
            "solution of whole data is whole. Drop the directions and the property fails &mdash; "
            "on an odd cycle the determinant is two and the optimal corner is genuinely halves."
        ),
        "key": [
            "totally unimodular: EVERY square submatrix has determinant 0, +1 or −1",
            "a node-arc incidence matrix is totally unimodular; its own determinant is 0",
            "basic solution   x_B = B⁻¹ b = adj(B) b / det(B),   and det(B) = ±1",
            "so integer b and TU A  ⟹  every basic feasible solution is an integer point",
            "undirected incidence of an ODD cycle: determinant 2, and the corner is halves",
            "an even cycle is bipartite; its determinant is 0 and its corners stay whole",
        ],
        "key_label": "The definition, the consequence, and the smallest matrix that fails it",
        "concepts_intro": (
            "This is the lesson the path's ordering exists for. Three ideas, and the third is "
            "the one that stops it becoming a slogan."
        ),
        "concepts": [
            ("Total unimodularity is a condition on every submatrix, not on the matrix",
             "It is not enough that the determinant of the whole matrix be `±1`, and it is not "
             "about the entries being `0` and `±1` either. Every square submatrix of every size "
             "must have determinant in `{0, +1, −1}`. On a four-by-five incidence matrix that is "
             "120 submatrices up to size three, and the lab sweeps all of them and reports zero "
             "failures."),
            ("Cramer's rule is the whole argument",
             "A basic solution solves `B x_B = b` for a square non-singular submatrix `B` of the "
             "constraint matrix. Cramer's rule gives each component as a ratio of determinants "
             "with `det B` underneath. If the data are whole, the numerator is whole; if "
             "`det B = ±1`, the division is exact. The corners are then lattice points, and a "
             "linear programme attains its optimum at a corner."),
            ("Direction is what makes it work",
             "The `+1` and `−1` in each column are not decoration. Replace them with two `+1`s "
             "&mdash; the undirected incidence matrix &mdash; and the property fails on any "
             "cycle of odd length: the triangle's determinant is 2. The lab then solves a "
             "packing programme on that matrix and returns `x = (1/2, 1/2, 1/2)` worth `3/2`, "
             "which no integer point reaches. Integrality is earned, and this is what earns it."),
        ],
        "read_title": "Why a network programme returns whole numbers, and when it stops",
        "read_intro": "The definition, then the theorem and its two-line proof, then the matrix that fails it and the halves it produces.",
        "body": [
            ("def", ("Totally unimodular",
                     "A matrix `A` is <strong>totally unimodular</strong> when every square "
                     "submatrix of `A` &mdash; of every size, formed by choosing any rows and "
                     "any equally many columns &mdash; has determinant `0`, `+1` or `−1`.",
                     "Every entry of such a matrix is itself a one-by-one submatrix, so every "
                     "entry is `0`, `+1` or `−1`. The converse fails, and the failure is the "
                     "interesting part of this lesson.")),
            ("thm", ("Integrality of network corners",
                     "Let `A` be totally unimodular and `b` an integer vector. Then every basic "
                     "feasible solution of `Ax = b`, `x ≥ 0` is an integer vector.",
                     "The node-arc incidence matrix `N` of any directed network is totally "
                     "unimodular. Hence every corner of the minimum-cost flow programme is "
                     "whole, on whole supplies and whole capacities, with no integrality "
                     "constraint written anywhere.")),
            ("proof", [
                "A basic solution takes a square non-singular submatrix `B` of the columns and "
                "sets `x_B = B⁻¹b`, with every other variable zero. By Cramer's rule the `k`-th "
                "component of `x_B` is `det(Bₖ) / det(B)`, where `Bₖ` is `B` with its `k`-th "
                "column replaced by `b`.",
                "`B` is a square submatrix of a totally unimodular matrix and is non-singular, "
                "so `det(B)` is `+1` or `−1`. `Bₖ` has integer entries throughout &mdash; the "
                "columns of `B` are integer and `b` is integer &mdash; so `det(Bₖ)` is an "
                "integer. An integer divided by `±1` is an integer, and every component of "
                "`x_B` is therefore whole. The non-basic components are zero.",
                "Nothing in this depends on the objective, so it holds at the optimum in "
                "particular; and since a bounded linear programme attains its optimum at a "
                "corner, the optimum is an integer point.",
            ]),
            ("p", "That the incidence matrix satisfies the condition is checkable rather than "
                  "memorable, and the lab checks it. On the five-arc network from the "
                  "minimum-cost flow lesson, `N` is four by five and the sweep runs every "
                  "submatrix of size one, two and three &mdash; 20, then 60, then 40, which is "
                  "120 in all &mdash; and reports every determinant in `{0, ±1}`."),
            ("math", [
                "N for  s>a  s>b  a>b  a>t  b>t",
                "",
                "   s      1    1    0    0    0",
                "   a     -1    0    1    1    0",
                "   b      0   -1   -1    0    1",
                "   t      0    0    0   -1   -1",
                "",
                "   rows 1,2,3 and columns 1,3,4      det  1",
                "   rows 1,2   and columns 1,2        det  1",
                "   rows 1,2,3 and columns 1,2,3      det  0",
                "",
                "   the whole matrix is singular: every column holds one +1 and one -1,",
                "   so the four rows sum to the zero row",
                "",
                "   sweep to size 3:   20 + 60 + 40 = 120 submatrices,  0 failures",
            ]),
            ("h3", "The same drawing, undirected, and the corner that is halves"),
            ("p", "Now take the triangle on three vertices and build the "
                  "<strong>undirected</strong> incidence matrix instead: `+1` at both ends of "
                  "each edge rather than `+1` and `−1`. Nothing about the picture has changed. "
                  "The matrix is three by three, and its determinant is 2."),
            ("math", [
                "undirected incidence of the triangle      directed, same drawing",
                "",
                "      1 0 1                                   1  0 -1",
                "      1 1 0                                  -1  1  0",
                "      0 1 1                                   0 -1  1",
                "",
                "   det = 2                                 sweep: unimodular",
                "   exactly one submatrix out of 19 fails, and it is the whole matrix",
                "",
                "   max x1 + x2 + x3   subject to that matrix times x ≤ 1,  x ≥ 0",
                "",
                "      corner   x = (1/2, 1/2, 1/2)      value 3/2",
                "      no integer point reaches 3/2; the best whole answer is 1",
            ]),
            ("example", ("The halves are real, and exact",
                         "The lab runs the same exact simplex on the same kind of programme and "
                         "returns `1/2` three times, printed as a fraction. There is no rounding "
                         "anywhere and nothing has gone wrong: `(1/2, 1/2, 1/2)` is a genuine "
                         "corner of that polyhedron, and it is strictly better than any lattice "
                         "point inside it.",
                         "This is the gap that the whole of Integer Programming is about, "
                         "arriving here as a two-line consequence of one determinant. It is also "
                         "the reason this course can be solved by the simplex method and that "
                         "one cannot.")),
            ("example", ("An even cycle keeps its whole corners",
                         "Do the same on the four-cycle. The undirected incidence matrix has "
                         "determinant `0`, the sweep finds nothing outside `{0, ±1}`, and the "
                         "packing programme's corner is `(1, 0, 1, 0)` worth 2 &mdash; whole.",
                         "So it is not undirectedness as such that breaks integrality; it is the "
                         "odd cycle. An even cycle is bipartite, and bipartite graphs are where "
                         "the undirected incidence matrix stays totally unimodular. That "
                         "observation is what makes the assignment problem behave, and it comes "
                         "back on the matching lesson.")),
            ("p", "Two warnings about the direction of the theorem. It says total unimodularity "
                  "is <em>sufficient</em> for integer corners, not necessary: plenty of "
                  "programmes have integral polyhedra for other reasons. And it says nothing "
                  "whatever about a programme whose matrix is not totally unimodular &mdash; "
                  "such a programme may still happen to have a whole optimum on some instance, "
                  "and that is luck rather than structure."),
        ],
        "lab": ("network", {
            "mode": "tu",
            "preset": "network",
            "panel_title": "Pick rows and columns, or sweep every submatrix at once",
            "panel_intro": "Type a network, choose whether to build the directed matrix or the "
                           "undirected one, and take the determinant of any submatrix you like "
                           "&mdash; or let the sweep do every submatrix up to size three and "
                           "report the failures by name. The odd cycle's failure comes with the "
                           "half-integral corner it produces, solved exactly.",
        }),
        "steps_title": "Deciding whether a programme's corners have to be whole",
        "steps_intro": "Build the matrix, check the condition, and then say which of the two conclusions you are entitled to.",
        "steps": [
            ("Write the constraint matrix out, not the drawing",
             "Total unimodularity is a property of a matrix. Two different matrices can describe "
             "the same picture &mdash; the directed and undirected incidence matrices of the "
             "triangle are the standard example &mdash; and one of them is totally unimodular "
             "and the other is not."),
            ("Check the entries first, because it is free",
             "Every entry must already be `0`, `+1` or `−1`, since each is a one-by-one "
             "submatrix. An entry of 2 anywhere settles the question immediately and you have "
             "spent no effort."),
            ("Sweep the small submatrices, and name any failure",
             "Every two-by-two, then every three-by-three. A failure is not a verdict of "
             "&ldquo;probably not&rdquo;: it is a specific submatrix with a specific "
             "determinant, and quoting it is the difference between a check and an impression."),
            ("If it passes, state the conclusion with its hypothesis attached",
             "Integer right-hand side gives integer corners. On fractional supplies you get "
             "fractional corners from a totally unimodular matrix too, and the theorem never "
             "claimed otherwise."),
            ("If it fails, look for the fractional corner rather than assuming one",
             "Failure removes the guarantee; it does not prove a fractional optimum exists. The "
             "odd cycle really does produce one, and finding it is what turns the failed check "
             "into something you have learned."),
        ],
        "worked": {
            "title": "One drawing, two matrices, two answers",
            "intro": [
                "The triangle throughout. The only thing that changes is whether each column "
                "gets a plus and a minus or two pluses, and every number below is read off the "
                "sweep and the exact simplex."
            ],
            "lines": [
                "DIRECTED    1>2, 2>3, 3>1",
                "",
                "        e1  e2  e3",
                "   1     1   0  -1",
                "   2    -1   1   0",
                "   3     0  -1   1",
                "",
                "   sweep to size 3:  9 + 9 + 1 = 19 submatrices",
                "   failures: none                         TOTALLY UNIMODULAR",
                "   det of the whole matrix: 0             (the rows sum to zero)",
                "",
                "UNDIRECTED  the same three edges, +1 at both ends",
                "",
                "        e1  e2  e3",
                "   1     1   0   1",
                "   2     1   1   0",
                "   3     0   1   1",
                "",
                "   sweep to size 3:  19 submatrices",
                "   failures: 1, and it is rows 1,2,3 by columns 1,2,3",
                "   det = 2                                NOT totally unimodular",
                "",
                "   max x1 + x2 + x3   s.t.  A x ≤ 1,  x ≥ 0",
                "      x = (1/2, 1/2, 1/2)     value 3/2",
                "      best integer point       value 1",
                "",
                "FOUR-CYCLE  undirected, 1-2-3-4-1",
                "   det = 0,  sweep clean,  corner x = (1, 0, 1, 0)  value 2   whole",
            ],
            "after": [
                "The pair of three-by-three matrices differs in three minus signs and in nothing "
                "else, and that is the whole of the difference between a problem the simplex "
                "method settles and a problem that needs a search. Worth staring at for a "
                "minute.",
                "For a rehearsal, take the four-arc network from the minimum-cost flow lesson "
                "and use the lab's row and column pickers to find a three-by-three submatrix "
                "with determinant `−1`, then one with determinant `0`. Both exist; predicting "
                "which is which before you press the button is the exercise.",
                "The harder rehearsal: build the undirected incidence matrix of the five-cycle "
                "and sweep it. It fails, for the same reason the triangle does, and the "
                "half-integral corner is worth `5/2` against a best whole answer of 2. Then do "
                "the six-cycle and watch the failure disappear.",
            ],
        },
        "quiz_title": "The condition, the argument, and its limits",
        "quiz": [
            {"q": "A matrix has every entry in `{0, +1, −1}`. Is it totally unimodular?",
             "a": ["Yes, that is the definition",
                   "Yes, provided it has more columns than rows",
                   "Not necessarily: the undirected incidence matrix of a triangle is a counterexample",
                   "Only if its own determinant is `±1`"],
             "c": 2,
             "why": "Entries in `{0, ±1}` is necessary and not sufficient. The triangle's "
                    "undirected incidence matrix has only zeros and ones in it and a determinant "
                    "of 2, and that single failing submatrix is enough: the sweep over its "
                    "nineteen submatrices reports exactly one, and it is the whole matrix."},
            {"q": "Which step in the proof actually uses total unimodularity?",
             "a": ["That `B` is non-singular",
                   "That the numerator `det(Bₖ)` is an integer",
                   "That the denominator `det(B)` is `±1`, so the division is exact",
                   "That the optimum is attained at a corner"],
             "c": 2,
             "why": "The numerator is an integer as soon as `B` and `b` are integer, and "
                    "non-singularity is what makes `B` a basis at all. The hypothesis earns its "
                    "keep in one place: `det(B) = ±1`, so `det(Bₖ)/det(B)` is a whole number "
                    "rather than a fraction. Take that away and everything else in the proof "
                    "still holds while the conclusion fails."},
            {"q": "A programme's constraint matrix is not totally unimodular. What follows about its optimum?",
             "a": ["It is fractional",
                   "It is fractional unless the right-hand side is even",
                   "Nothing: the guarantee is gone, but a whole optimum may still occur",
                   "It cannot be solved by the simplex method"],
             "c": 2,
             "why": "The theorem is one-directional. Losing the hypothesis loses the guarantee "
                    "and nothing more &mdash; many programmes with other matrices have integral "
                    "optima on particular data. The odd cycle is worth knowing precisely because "
                    "it does produce a fractional corner, `(1/2, 1/2, 1/2)`, rather than merely "
                    "failing to rule one out."},
            {"q": "Why does the undirected incidence matrix of a four-cycle keep its whole corners while the triangle's does not?",
             "a": ["Because four is larger than three",
                   "Because the four-cycle is bipartite and the triangle is not",
                   "Because the four-cycle's matrix is singular and singular matrices are always fine",
                   "Because the triangle has an arc pointing the wrong way"],
             "c": 1,
             "why": "Odd cycles are exactly the obstruction: a graph's undirected incidence "
                    "matrix is totally unimodular precisely when the graph is bipartite, and a "
                    "graph is bipartite precisely when it has no odd cycle. The four-cycle "
                    "sweeps clean and its corner is `(1, 0, 1, 0)` worth 2. Singularity is not "
                    "the reason &mdash; the triangle's directed matrix is singular too, and it "
                    "is totally unimodular."},
        ],
        "mistakes": [
            ("Checking only the whole matrix's determinant",
             "&ldquo;Totally&rdquo; is doing the work in the name. The directed incidence matrix "
             "of any network has determinant zero, because its rows sum to zero, and it is still "
             "totally unimodular; the undirected triangle's determinant is 2 and one failing "
             "submatrix is enough to lose everything. The condition is over all square "
             "submatrices of all sizes."),
            ("Concluding that integrality is a property of the problem",
             "It is a property of the matrix you wrote. The same triangle gives a totally "
             "unimodular matrix read one way and a matrix with a fractional corner read the "
             "other. Change the formulation &mdash; add a side constraint, share a capacity "
             "between two commodities &mdash; and the structure can be gone while the picture "
             "still looks like a network."),
            ("Reading fractional corners as a numerical problem",
             "`(1/2, 1/2, 1/2)` is not a rounding artefact and it will not go away with better "
             "arithmetic; it is where the optimum of that programme is. The labs carry exact "
             "fractions throughout for this reason, and a half printed as a half is the lesson "
             "rather than a display detail."),
        ],
        "standard": ("Finish when you can state the theorem with its hypothesis, run the argument from Cramer's rule, and produce the counterexample.",
                     "You should be able to define total unimodularity over all square "
                     "submatrices, build both incidence matrices of a small graph, explain where "
                     "`det(B) = ±1` enters the proof, say why an integer right-hand side is part "
                     "of the hypothesis, and exhibit the odd cycle's half-integral corner."),
        "note": 'This is the result the ordering of the whole path was arranged around, and it is why networks and general whole-number problems belong to different courses: a network is a linear programme whose corners are already lattice points, and Integer Programming exists for the linear programmes whose corners are not. &ldquo;The Assignment Problem&rdquo; takes the sharpest special case of the network side &mdash; every supply and every demand equal to one &mdash; and solves it by a method that never writes a tableau at all.',
    },
]
