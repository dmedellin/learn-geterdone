"""Markov Chains, Decisions and Queues -- the chains half.

The transition matrix as an object, its structure read off the arcs, the steady
state solved as a linear system rather than waited for, absorption, and a
decision attached to every state.

Every figure below is read off the kit -- scripts/mathpath/labs/markov.py --
by executing its shipped JavaScript under node, rather than asserted here, and
scripts/mathcheck.js executes that same block. Where a design note and the kit
disagreed, the kit won and the lesson says what the kit does.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "transition-matrices-and-the-support-digraph",
        "title": "Transition Matrices and the Support Digraph",
        "module": "The chain as an object",
        "one_line": "A row is a distribution, an arc is drawn wherever an entry is positive, and Pⁿ is n steps taken at once in exact fractions.",
        "summary": (
            "A transition matrix is not a square table of numbers. Every row is a probability "
            "distribution &mdash; where the chain goes next, given where it is now &mdash; and a "
            "matrix whose rows do not sum to one is not a chain, so every quantity computed from "
            "it would still produce a number and none of them would mean anything. The lab adds "
            "each row up before it draws a single arc. Two objects come out of the matrix: the "
            "digraph, which records only which entries are nonzero, and `Pⁿ`, which is n steps "
            "taken at once and whose entries here are fractions rather than decimals."
        ),
        "key": [
            "P[i][j] = P(next is j | now at i)      one row per state, each row a distribution",
            "every row sums to exactly 1, or it is not a chain and nothing below is meaningful",
            "(vP)ⱼ = Σᵢ vᵢ P[i][j]        a distribution moves on the LEFT of the matrix",
            "Pⁿ[i][j] = P(at j after n steps | started at i)          n steps in one object",
            "an arc is drawn wherever P[i][j] > 0 — the digraph is about which, not how much",
            "five states, denominator 20:  P¹² has numerators of 15 digits over 16",
        ],
        "key_label": "What a transition matrix is, and what a power of one means",
        "concepts_intro": (
            "Three ideas, and the first of them is the whole definition. The other two are the "
            "objects this course will keep taking out of the same matrix."
        ),
        "concepts": [
            ("A row is a distribution, and that is the entire definition",
             "From state `i` the chain has to go somewhere, so the numbers in row `i` are "
             "non-negative and add to exactly 1. That is all a transition matrix is. The lab "
             "refuses a matrix that fails it and names the offending row, because a row summing "
             "to `9/10` says the chain goes somewhere nine times out of ten and vanishes the "
             "tenth &mdash; and every steady state, expected time and value on this course would "
             "still compute happily on such a matrix."),
            ("The digraph records which entries are nonzero, not how big they are",
             "Draw an arc from `i` to `j` exactly when `P[i][j] > 0`. An arc of probability "
             "`1/1000` is as much an arc as one of probability `1/2`, and the structure that "
             "&ldquo;Communicating Classes, Recurrence and Period&rdquo; reads &mdash; who can "
             "reach whom, what the chain cannot leave, how long the cycles are &mdash; depends "
             "on nothing but that yes-or-no answer."),
            ("A power of P is n steps at once, and its entries outgrow a decimal",
             "`Pⁿ[i][j]` is the probability of being at `j` after exactly n steps having started "
             "at `i`, and it is obtained by multiplying the matrix by itself rather than by "
             "simulating anything. The arithmetic is exact: on the five-state example `P¹²` has "
             "numerators fifteen digits long over denominators of sixteen, which is past what a "
             "double can hold, so a decimal implementation would be storing the nearest number "
             "it had and calling it the answer."),
        ],
        "read_title": "Everything a chain is, before anything is asked of it",
        "read_intro": "The definition, the one test the data must pass, the two directions a matrix can be read in, and where the decimals would have gone.",
        "body": [
            ("def", ("A finite Markov chain",
                     "A finite set of <strong>states</strong> `1, …, n` together with a "
                     "<strong>transition matrix</strong> `P`, where `P[i][j]` is the probability "
                     "that the chain is at `j` at the next step given that it is at `i` now. "
                     "Every entry satisfies `0 ≤ P[i][j] ≤ 1` and every row satisfies "
                     "`Σⱼ P[i][j] = 1`.",
                     "A <strong>distribution</strong> on the states is a row vector `v` with "
                     "`vᵢ ≥ 0` and `Σᵢ vᵢ = 1`. The chain is <strong>memoryless</strong>: the "
                     "row used at each step depends on the current state and on nothing "
                     "earlier.")),
            ("p", "The lab takes the matrix as text, rows separated by a semicolon and entries "
                  "by spaces: `1/2 1/2; 1/4 3/4` is a two-state chain whose first row is an even "
                  "split. Entries may be fractions, and they stay fractions &mdash; `7/10` is "
                  "seven tenths exactly, not `0.7`. The state names are yours, and they are "
                  "labels: nothing below depends on them."),
            ("p", "Before it draws anything the page adds each row up and prints the sum beside "
                  "the row. This looks like fussiness for about as long as it takes to mistype "
                  "one entry. A matrix with a bad row still has powers, still has an invariant "
                  "vector, still yields expected times to absorption; all of those numbers are "
                  "answers about an object that is not a chain, and no later check on this "
                  "course would catch it."),
            ("math", [
                "the two-state example                    the row sums, checked",
                "",
                "         fine    wet                        fine   1/2 + 1/2 = 1   ok",
                "  fine   1/2     1/2                        wet    1/4 + 3/4 = 1   ok",
                "  wet    1/4     3/4",
                "",
                "  start (1, 0)  —  certainly fine today",
                "",
                "     step 0    (1, 0)",
                "     step 1    (1/2, 1/2)",
                "     step 2    (3/8, 5/8)",
                "     step 3    (11/32, 21/32)",
                "     step 4    (43/128, 85/128)",
                "     step 5    (171/512, 341/512)",
                "     step 6    (683/2048, 1365/2048)",
            ]),
            ("h3", "The distribution moves on the left, and that is not a convention"),
            ("p", "A distribution is a row vector and it is multiplied on the <em>left</em>: "
                  "`(vP)ⱼ = Σᵢ vᵢ P[i][j]`. Read the sum out loud and the reason is immediate "
                  "&mdash; the chance of being at `j` next is the chance of being at each `i` "
                  "now, times the chance of the step from `i` to `j`, added over every `i`. "
                  "That is why the stationary vector solves `πP = π` rather than `Pπ = π`, and "
                  "why it is a left eigenvector; a reader who has met eigenvectors as columns "
                  "meets the transpose here and should notice."),
            ("thm", ("Powers compose",
                     "`P^(m+n) = Pᵐ Pⁿ` for all `m, n ≥ 0`, with `P⁰` the identity. Hence "
                     "`Pⁿ[i][j]` is the probability of being at `j` after exactly n steps from "
                     "`i`, and `vPⁿ` is the distribution after n steps from `v`.")),
            ("proof", ["To get from `i` to `j` in `m + n` steps the chain is somewhere at step "
                       "`m` &mdash; at exactly one state `k`, and those events are disjoint and "
                       "exhaust the possibilities.",
                       "So the probability is `Σₖ P(i to k in m) · P(k to j in n)`, which by "
                       "memorylessness is `Σₖ Pᵐ[i][k] · Pⁿ[k][j]`, and that sum is the "
                       "`(i, j)` entry of the matrix product. Nothing about the numbers was "
                       "used, only that the intermediate state is exactly one of the n."]),
            ("p", "So there is no separate machinery for &ldquo;n steps&rdquo;. The lab computes "
                  "`Pⁿ` by repeated multiplication and prints it whole, and the distribution "
                  "bars beneath the digraph are that same walk shown one step at a time. Push "
                  "the step count up on the two-state example and the bars stop moving long "
                  "before the fractions stop growing, which is worth watching: those are two "
                  "different facts and only one of them is about probability."),
            ("h3", "Where the decimals would have gone"),
            ("p", "The five-state example has every entry over a denominator of 20, which looks "
                  "harmless. Multiplying the matrix by itself multiplies denominators, and by "
                  "the twelfth power the entries are fifteen-digit numerators over sixteen-digit "
                  "denominators; by the twenty-fourth they are thirty-one over thirty-two. The "
                  "lab prints the widest numerator and the largest denominator as figures, and "
                  "warns when the denominator passes what a double can hold."),
            ("math", [
                "five states, every entry over 20        widest numerator   largest denominator",
                "",
                "     P                                      1 digit             2 digits",
                "     P⁶                                     8 digits            8 digits",
                "     P¹²                                   15 digits           16 digits",
                "     P²⁴                                   31 digits           32 digits",
                "",
                "  one entry of P¹², exactly:",
                "     203244268876273 / 1024000000000000",
                "",
                "  a double carries about 15 to 17 significant figures in total,",
                "  so from P¹² onward a decimal is storing a nearby number, not this one",
            ]),
            ("p", "This is not a point about arithmetic hygiene for its own sake. The claim the "
                  "whole of this course rests on is that certain quantities are exactly equal "
                  "&mdash; `πP` is exactly `π`, two routes to a queue's distribution give "
                  "exactly the same fractions &mdash; and an equality between two decimals that "
                  "look alike is not evidence of anything."),
            ("example", ("A matrix that is refused, and why refusing is the right answer",
                         "Type `1/2 1/4; 1/4 3/4`. The first row sums to `3/4`, and the lab "
                         "stops with the row named and nothing drawn.",
                         "Every quantity on this page would have computed. The powers exist, "
                         "the digraph can be drawn, a distribution can be pushed through it. "
                         "What they would describe is a process that disappears with "
                         "probability `1/4` per step from state one, which is a fine object and "
                         "is not a Markov chain. The page refuses rather than painting, because "
                         "a number produced from bad data is worse than a blank panel.")),
            ("example", ("A starting distribution the lab will not rescale",
                         "Type `1 1` as the starting distribution on the two-state chain. It is "
                         "refused: the entries have to be non-negative and sum to exactly 1.",
                         "Rescaling it silently to `(1/2, 1/2)` would answer a question nobody "
                         "asked. A distribution that does not sum to one is a typo far more "
                         "often than it is an unnormalised weight, and the two cases want "
                         "opposite treatment.")),
        ],
        "lab": ("markov", {
            "mode": "chain",
            "preset": "weather",
            "panel_title": "Type a matrix, name the states, push a distribution forward",
            "panel_intro": "Every row is added up on this page before anything is computed from "
                           "it, and a matrix whose rows do not sum to one is refused rather than "
                           "used. The digraph draws an arc wherever the probability is positive. "
                           "Pⁿ is exact repeated multiplication, which is why its entries can be "
                           "wider than a decimal &mdash; try the five-state example at twelve "
                           "steps and read the two width figures.",
        }),
        "steps_title": "Reading a transition matrix somebody has handed you",
        "steps_intro": "The data first, then the structure, then the powers. Doing them in that order means a bad matrix never reaches the arithmetic.",
        "steps": [
            ("Add every row up",
             "One addition per state. If a row does not come to 1, stop: whatever you have is "
             "not a transition matrix and nothing computed from it describes a chain. This is "
             "the cheapest test on the course and the only one that can invalidate all the "
             "others at once."),
            ("Write down the digraph before the numbers",
             "An arc wherever the entry is positive, and nothing else. The next several ideas "
             "&mdash; classes, recurrence, period, which states the chain can never leave "
             "&mdash; are properties of that picture alone, and having it in front of you stops "
             "you from reasoning about magnitudes when the question is about reachability."),
            ("Say which side your distribution multiplies on",
             "Distributions are rows and go on the left; `vP` is one step forward. If you find "
             "yourself computing `Pv` you are asking a different question, and the answer will "
             "not be a distribution."),
            ("Take powers rather than steps when you want a step count",
             "`Pⁿ` answers &ldquo;where is it after n&rdquo; for every starting state at once, "
             "which is usually what you want; `vPⁿ` answers it for one. Both come from the same "
             "matrix product and neither needs a simulation."),
            ("Check the width of what came out",
             "If the denominators have outgrown sixteen digits, any decimal answer you have seen "
             "for the same quantity was rounded, and the rounding happened before you looked. "
             "The lab prints both widths so that this is a fact rather than a suspicion."),
        ],
        "worked": {
            "title": "One two-state chain, pushed forward, and one five-state chain that outgrows a decimal",
            "intro": [
                "Two states, `fine` and `wet`, with `P = [1/2 1/2; 1/4 3/4]`, started certainly "
                "fine. Every entry below is exact, and the arithmetic is one row vector times "
                "one matrix, repeated.",
            ],
            "lines": [
                "P =    1/2  1/2         start v = (1, 0)",
                "       1/4  3/4",
                "",
                "  vP   = (1·1/2 + 0·1/4,  1·1/2 + 0·3/4)  =  (1/2, 1/2)",
                "  vP²  = (1/2·1/2 + 1/2·1/4, 1/2·1/2 + 1/2·3/4)  =  (3/8, 5/8)",
                "  vP³  = (11/32, 21/32)          0.34375000",
                "  vP⁴  = (43/128, 85/128)        0.33593750",
                "  vP⁵  = (171/512, 341/512)      0.33398438",
                "  vP⁶  = (683/2048, 1365/2048)   0.33349609",
                "  vP⁸  = (10923/32768, 21845/32768)     0.33334351",
                "  vP¹⁰ = (174763/524288, 349525/524288) 0.33333397",
                "",
                "P⁶ itself, both rows:",
                "       683/2048    1365/2048",
                "      1365/4096    2731/4096",
                "",
                "five states, every entry over 20:",
                "",
                "     n        widest numerator    largest denominator",
                "     1             1                     2",
                "     6             8                     8",
                "    12            15                    16",
                "    24            31                    32",
            ],
            "after": [
                "The numerators and denominators of the two-state walk are doing something "
                "regular: `1/2, 3/8, 11/32, 43/128`, each denominator four times the last and "
                "each numerator four times the last minus one. That the decimals are creeping towards "
                "`0.3333` is the eye-catching part, and it is the part this course will be most "
                "careful about: it is a fact about a limit, and the number `1/3` is available "
                "from a linear system with no limit involved at all. That is the subject of "
                "&ldquo;The Steady State as a Linear System&rdquo;.",
                "The five-state table is the reason nothing here is a decimal. At `n = 12` the "
                "largest denominator has sixteen digits; a double carries about fifteen to "
                "seventeen significant figures altogether, so a floating-point implementation "
                "has already stopped holding these numbers and started holding the nearest ones "
                "it can. Nothing warns it, and the entries still sum to something that prints "
                "as 1.",
                "For a rehearsal, take the two-state chain and start it at `(0, 1)` instead. "
                "The supplied first move is that `vP = (1/4, 3/4)`. Work out where the walk is "
                "heading and then check it against the walk from `(1, 0)`: both approach the "
                "same pair of numbers from opposite sides, which is a hint about what that pair "
                "is and a warning about what &ldquo;approach&rdquo; will turn out to be worth.",
            ],
        },
        "quiz_title": "Rows, arcs and powers",
        "quiz": [
            {"q": "A matrix has non-negative entries and its COLUMNS each sum to 1, but two of its rows do not. Is it a transition matrix for a chain on those states?",
             "a": ["Yes: column sums of 1 are the same condition written the other way",
                   "Yes, provided the matrix is square",
                   "No: the condition is on rows, because from each state the chain must go somewhere",
                   "Only if it is also symmetric"],
             "c": 2,
             "why": "The row condition says that from state `i` the total probability of going "
                    "somewhere is 1, which is what makes each row a distribution. Column sums "
                    "are a different and much stronger condition &mdash; it holds for some "
                    "chains and fails for most &mdash; and a matrix satisfying it with bad rows "
                    "describes no chain at all. The lab names the failing row for this reason."},
            {"q": "On a chain with `P[1][2] = 1/1000` and `P[3][4] = 1/2`, what is the difference between those two arcs in the support digraph?",
             "a": ["None: both entries are positive, so both arcs are drawn",
                   "The first is drawn thinner, because the digraph is weighted",
                   "The first is omitted, because it is below any reasonable threshold",
                   "The first is drawn as a dashed arc to mark it as unlikely"],
             "c": 0,
             "why": "The digraph records only which entries are nonzero. That is exactly the "
                    "right amount of information for the structural questions that follow: a "
                    "single arc of probability `1/1000` out of a set of states makes that set "
                    "escapable, and the chain takes it eventually."},
            {"q": "You want the probability of being at state `j` after 7 steps, starting from a known distribution `v`. Which computation answers it?",
             "a": ["The `j`-th entry of `P⁷v`", "The `j`-th entry of `vP⁷`",
                   "The `j`-th diagonal entry of `P⁷`", "The average of the `j`-th column of `P⁷`"],
             "c": 1,
             "why": "Distributions are row vectors and multiply on the left, so `vP⁷` is the "
                    "distribution after seven steps and its `j`-th entry is the answer. `P⁷v` "
                    "is a column vector of something else entirely, and the diagonal entry "
                    "answers the different question of returning to where you started."},
            {"q": "At `P¹²` on the five-state example the denominators run to sixteen digits. What does that tell you about a decimal version of the same computation?",
             "a": ["Nothing: the decimals would still be accurate to sixteen places",
                   "It has been storing rounded values from some earlier power onwards, silently",
                   "It would refuse to compute, because the numbers overflow",
                   "It would be faster and therefore preferable"],
             "c": 1,
             "why": "A double holds roughly fifteen to seventeen significant figures in total, "
                    "so once the exact value needs more than that the stored number is a "
                    "different number. Nothing announces it, the rows still appear to sum to 1, "
                    "and every later claim of exact equality on this course would be a "
                    "comparison of two roundings."},
        ],
        "mistakes": [
            ("Checking that the whole matrix sums to n instead of checking each row",
             "A matrix with one row over by `1/4` and another under by `1/4` passes that test "
             "and is not a chain. The failures have to be found row by row, which is why the "
             "lab prints one sum per row and names the first that fails rather than giving a "
             "single verdict."),
            ("Reading the digraph as though the arc widths mattered",
             "Reachability, communicating classes, recurrence and the period are computed from "
             "the pattern of nonzero entries and from nothing else. An arc that is very "
             "unlikely still connects, and reasoning that a small probability &ldquo;may as "
             "well be zero&rdquo; changes the structural answer and not just its precision."),
            ("Multiplying the distribution on the wrong side",
             "`Pv` is a perfectly good matrix-vector product and it is not the next "
             "distribution. The habit comes from meeting eigenvectors as columns; here the "
             "stationary vector is a LEFT eigenvector, and a reader who has it on the wrong "
             "side will be solving the transposed system for the rest of the course."),
        ],
        "standard": ("Finish when you can look at a square array of fractions and say in one pass whether it is a chain, and what its digraph is.",
                     "You should be able to test a matrix row by row and name the failing row, "
                     "draw the support digraph from the pattern of nonzero entries, push a "
                     "distribution forward by hand as a row vector, say what the `(i, j)` entry "
                     "of `Pⁿ` means without hesitating over which index is which, and explain "
                     "why the entries of a power outgrow a decimal and what that costs."),
        "note": 'Everything above is the matrix as data. The next question is what its <em>shape</em> forces: which states the chain can leave and never return to, which sets it can never leave at all, and whether its returns are locked to a rhythm. All three are read off the digraph alone, and two of them are the hypotheses of the one theorem this course states without proving. &ldquo;Communicating Classes, Recurrence and Period&rdquo; computes them.',
    },

    # ---------------------------------------------------------------- 02
    {
        "slug": "communicating-classes-recurrence-and-period",
        "title": "Communicating Classes, Recurrence and Period",
        "module": "The chain as an object",
        "one_line": "Reachability splits the states into classes, a class is recurrent when no arc leaves it, and the period is a gcd of cycle lengths.",
        "summary": (
            "Three structural facts, all of them read off the arcs and none of them off the "
            "probabilities. Two states <em>communicate</em> when each can reach the other, which "
            "partitions the states into classes. A class is <strong>recurrent</strong> when "
            "nothing leaves it &mdash; a statement about which arcs exist, not about how large "
            "they are &mdash; and <strong>transient</strong> otherwise. The "
            "<strong>period</strong> of a class is the greatest common divisor of its cycle "
            "lengths, and the lab computes it without enumerating a single cycle. Irreducible "
            "and aperiodic are the two hypotheses of the convergence theorem, and this page is "
            "where they become checkable rather than assumed."
        ),
        "key": [
            "i → j when some Pⁿ[i][j] > 0;  i ↔ j when both — and ↔ is an equivalence relation",
            "the classes are its equivalence classes: a partition, computed from reachability",
            "recurrent ⟺ no arc leaves the class          transient ⟺ some arc does",
            "irreducible ⟺ exactly one class ⟺ everything reaches everything",
            "period d = gcd of the lengths of the cycles through a state;  aperiodic ⟺ d = 1",
            "level the class by breadth-first search:  d = gcd over arcs of level(u) + 1 − level(v)",
        ],
        "key_label": "Structure from the arcs alone, with nothing about magnitudes in it",
        "concepts_intro": (
            "Three properties of the same digraph. The first partitions the states, the second "
            "says which parts the chain settles into, and the third says whether it settles at "
            "all or merely returns on a schedule."
        ),
        "concepts": [
            ("Communication is an equivalence relation, so the classes are a partition",
             "Reachability is reflexive (`n = 0`) and transitive (compose the paths), so "
             "two-way reachability is an equivalence relation and its classes tile the state "
             "space with no overlaps and nothing left over. That is why the lab can print a "
             "reachability table and a class list side by side: the second is forced by the "
             "first, and `↔` in the table is exactly the entries that share a class."),
            ("Recurrent means no arc leaves, and an arc is an arc",
             "If some arc leads out of a class and never comes back, the chain takes it "
             "eventually &mdash; probability one, whatever the arc's size &mdash; and cannot "
             "return, so the class is visited finitely often. If no arc leaves, the class is "
             "closed and the chain that enters it stays. The test is a scan of the arcs out of "
             "the class, and a probability of `1/1000` decides it exactly as a probability of "
             "`1/2` does."),
            ("The period is a gcd, and it is computed without listing cycles",
             "Take the lengths of all the cycles through a state and take their greatest common "
             "divisor. Enumerating cycles is expensive and unnecessary: level the class by "
             "breadth-first search and take the gcd of `level(u) + 1 − level(v)` over every arc "
             "`u → v` in it. Every cycle's length is a sum of those quantities, so the two gcds "
             "agree, and the second costs one traversal."),
        ],
        "read_title": "What the arrows force, before any probability is looked at",
        "read_intro": "Reachability and its classes, the arc test for recurrence, the period as a gcd, and the two hypotheses the one unproved theorem on this path needs.",
        "body": [
            ("def", ("Reachability, communication and classes",
                     "State `j` is <strong>reachable</strong> from `i`, written `i → j`, when "
                     "`Pⁿ[i][j] > 0` for some `n ≥ 0`. States `i` and `j` "
                     "<strong>communicate</strong>, written `i ↔ j`, when `i → j` and `j → i`.",
                     "`↔` is an equivalence relation, and its classes are the "
                     "<strong>communicating classes</strong>. A class `C` is "
                     "<strong>closed</strong>, or <strong>recurrent</strong>, when no arc leads "
                     "from a state of `C` to a state outside it, and <strong>transient</strong> "
                     "otherwise. The chain is <strong>irreducible</strong> when there is exactly "
                     "one class.")),
            ("p", "Reachability is computed as the transitive closure of the arc relation, so "
                  "the table the lab prints is closed under composition rather than a list of "
                  "single steps. A cell shows `↔` when the two states reach each other, `→` "
                  "when only one direction works, and a dot when neither does; the `↔` cells "
                  "are precisely the pairs sharing a class."),
            ("h3", "Why “no arc leaves” is the right test"),
            ("p", "Suppose one arc leads out of `C` and does not lead back. Each visit to its "
                  "tail takes it with some fixed positive probability, so over infinitely many "
                  "visits the chance of never taking it is zero. The chain therefore leaves `C` "
                  "with probability one and, since it cannot come back, visits `C` finitely "
                  "often: that is what transient means. If instead no arc leaves, the chain that "
                  "enters `C` can never be anywhere else, and every state of `C` is visited "
                  "again and again."),
            ("p", "Nothing in that argument used a magnitude. It used only that the arc exists "
                  "and that the probability of never taking a fixed positive chance infinitely "
                  "often is zero. This is the single most common place to reason about the "
                  "wrong thing: a reader looking at `0.001` out of a class and `0.999` inside "
                  "it sees a class the chain is basically never going to leave, and the correct "
                  "answer is that it leaves, every time, eventually."),
            ("example", ("One state that can leave and never return",
                         "The three-state example `1/2 1/4 1/4; 0 3/4 1/4; 0 1/2 1/2` has "
                         "classes `{trial}` and `{kept, lapsed}`. The first column is zero "
                         "below the diagonal, so nothing returns to `trial`; the lab reports it "
                         "transient and colours it red, and reports `{kept, lapsed}` recurrent "
                         "because no arc leaves it.",
                         "The chain is therefore <em>reducible</em>, so the convergence theorem "
                         "does not apply to it. It still has a unique stationary distribution "
                         "&mdash; `(0, 2/3, 1/3)`, which mode <em>steady</em> computes &mdash; "
                         "and the zero is not a rounding: the chain spends finitely much of its "
                         "time at `trial`, so the long-run fraction is exactly nothing.")),
            ("h3", "The period, and the gcd that computes it"),
            ("def", ("Period",
                     "The <strong>period</strong> of state `i` is `d(i) = gcd{n ≥ 1 : "
                     "Pⁿ[i][i] > 0}`, the greatest common divisor of the lengths of the closed "
                     "walks from `i` back to itself. States in the same class have the same "
                     "period, so it is a property of the class. A class with `d = 1` is "
                     "<strong>aperiodic</strong>.")),
            ("p", "A self-loop forces `d = 1` immediately, since 1 divides everything. A "
                  "three-state ring with no other arcs has closed walks of lengths `3, 6, 9, …` "
                  "and therefore period 3: the chain returns to where it started only at "
                  "multiples of three, for ever, and no amount of waiting changes that."),
            ("p", "The lab does not enumerate closed walks. It levels the class by "
                  "breadth-first search from one of its states and takes the gcd of "
                  "`level(u) + 1 − level(v)` over every arc `u → v` inside the class. Each "
                  "closed walk's length is the sum of those quantities along it, so every walk "
                  "length is a multiple of that gcd; and each arc lies on some closed walk, so "
                  "the gcd of the walk lengths divides it. The two divide each other and are "
                  "therefore equal, and one traversal has replaced an enumeration."),
            ("math", [
                "the 3-cycle      0 1 0            classes        {1, 2, 3}, one class",
                "                 0 0 1            irreducible    yes",
                "                 1 0 0            period         3        aperiodic  no",
                "",
                "  levels from state 1 by breadth-first search:  1 → 0,  2 → 1,  3 → 2",
                "  arcs and level(u) + 1 − level(v):",
                "      1 → 2     0 + 1 − 1 = 0",
                "      2 → 3     1 + 1 − 2 = 0",
                "      3 → 1     2 + 1 − 0 = 3",
                "  gcd(0, 0, 3) = 3            and no cycle was ever written down",
                "",
                "the three-brand chain, every entry positive:",
                "      classes 1    irreducible yes    period 1    aperiodic yes",
            ]),
            ("h3", "The two hypotheses, and the theorem this path does not prove"),
            ("thm", ("Convergence of the powers, stated and not proved",
                     "If a finite chain is irreducible and aperiodic then `Pⁿ[i][j] → πⱼ` as "
                     "`n → ∞` for every `i` and `j`, where `π` is the unique solution of "
                     "`πP = π` with `Σπ = 1`.",
                     "This is one of the three results the footer of this subject names as "
                     "<strong>stated and not proved</strong>. What is proved here is nothing; "
                     "what is <em>computed</em> here is both hypotheses, on whatever matrix you "
                     "type, and the conclusion's `π` is obtained by solving a linear system in "
                     "the material that follows &mdash; not as a limit.")),
            ("p", "A stated theorem whose hypotheses you can check is a different object from a "
                  "stated theorem taken on trust. Both conditions are needed, and each fails on "
                  "its own preset here. The three-cycle is irreducible and periodic: the powers "
                  "return to the identity every third step and converge to nothing, while the "
                  "linear system still has exactly one answer. The two-closed-group example is "
                  "aperiodic and reducible: the powers do converge, and not to a single `π`, "
                  "because there is no single `π` for them to converge to."),
            ("example", ("Two closed groups, and a chain with no unique steady state",
                         "The four-state example `1/2 1/2 0 0; 1/2 1/2 0 0; 0 0 1/3 2/3; "
                         "0 0 1/4 3/4` has two classes, `{a, b}` and `{c, d}`, and "
                         "<em>both</em> are recurrent: no arc leaves either.",
                         "So the chain is reducible with two recurrent classes, and the balance "
                         "equations have a whole family of solutions rather than one. The lab "
                         "reports two recurrent classes here and says that mode "
                         "<em>steady</em> on the same matrix refuses to print one of them as "
                         "though it were the answer.")),
        ],
        "lab": ("markov", {
            "mode": "classify",
            "preset": "leaky",
            "panel_title": "Type a matrix and read its structure off the arcs",
            "panel_intro": "Classes come from reachability on the digraph, recurrence from "
                           "whether any arc leaves a class, and the period from a gcd taken over "
                           "a breadth-first levelling. These are the two hypotheses the "
                           "convergence theorem needs, and this page computes both of them on "
                           "whatever matrix you give it. Switch to the 3-cycle: irreducible, and "
                           "period 3.",
        }),
        "steps_title": "Classifying a chain by hand",
        "steps_intro": "Arcs, then closure, then classes, then the two properties. Every step is about the pattern and none of them is about the numbers.",
        "steps": [
            ("Write the arcs, ignoring the probabilities entirely",
             "One arrow per positive entry, self-loops included. Cover the fractions up if it "
             "helps. Everything in this material is a property of the arrows, and keeping the "
             "magnitudes in view is how a reader talks themselves into treating a small "
             "probability as absent."),
            ("Close the relation, then group",
             "Find what each state can reach, following arrows as far as they go. Two states "
             "with arrows both ways share a class. The result is a partition; if you end up "
             "with a state in two groups, you have made an error, because communication is an "
             "equivalence relation and cannot overlap."),
            ("Test each class for an escaping arc",
             "Scan the arcs out of the class. One that leaves and does not come back makes the "
             "class transient, however small it is. None at all makes it recurrent, and a "
             "chain with exactly one class is irreducible."),
            ("Find the period as a gcd, not as an observation",
             "Level the class from any state and take the gcd of `level(u) + 1 − level(v)` over "
             "its internal arcs. A self-loop anywhere gives 1 straight away. Do not conclude "
             "&ldquo;aperiodic&rdquo; from having failed to spot a rhythm: the gcd is a "
             "computation and the eye is not."),
            ("Say which hypotheses hold before quoting any convergence",
             "Irreducible and aperiodic together are what the convergence statement needs. "
             "Either one alone is not enough, and both of the presets that break it are on the "
             "dropdown of this page."),
        ],
        "worked": {
            "title": "Four matrices, classified: one leaky, one cyclic, one split, one where everything is fine",
            "intro": [
                "The same four questions asked of four matrices: how many classes, is it "
                "irreducible, which classes are recurrent, and what is the period. Every answer "
                "below is read off the arcs.",
            ],
            "lines": [
                "A   1/2 1/4 1/4 ;  0 3/4 1/4 ;  0 1/2 1/2        names  trial kept lapsed",
                "    arcs out of trial: to trial, kept, lapsed.  Into trial: none but itself.",
                "    classes {trial}  {kept, lapsed}       transient 1   recurrent 1",
                "    irreducible  no        period per class  1, 1",
                "",
                "B   0 1 0 ;  0 0 1 ;  1 0 0",
                "    classes {1, 2, 3}            irreducible  yes",
                "    period  gcd(0, 0, 3) = 3     aperiodic  no",
                "",
                "C   1/2 1/2 0 0 ; 1/2 1/2 0 0 ; 0 0 1/3 2/3 ; 0 0 1/4 3/4",
                "    classes {a, b}  {c, d}       no arc leaves EITHER",
                "    recurrent 2   transient 0    irreducible  no",
                "    two recurrent classes ⟹ the balance system is rank deficient",
                "",
                "D   7/10 2/10 1/10 ; 3/10 5/10 2/10 ; 1/10 3/10 6/10",
                "    every entry positive ⟹ one class, and every self-loop gives period 1",
                "    classes 1   irreducible yes   period 1   aperiodic yes",
                "",
                "  only D satisfies both hypotheses of the convergence statement",
            ],
            "after": [
                "Matrix A is the one to sit with, because it is the case where the intuition "
                "&ldquo;transient means rare&rdquo; is most tempting and most wrong. The chain "
                "starts at `trial` with probability one; it is there at step zero, and it may "
                "be there at step five. What makes `{trial}` transient is that the number of "
                "visits is finite with probability one, and the long-run fraction of time spent "
                "there is therefore exactly zero &mdash; a fact you will see printed as an "
                "exact `0` in the steady state, not as a small number.",
                "Matrices B and C are the two failures, and they fail differently. B is "
                "irreducible, so the linear system has one answer; it is periodic, so the "
                "powers have none. C is aperiodic, so the powers settle; it is reducible with "
                "two recurrent classes, so what they settle to depends on where the chain "
                "started, and no single distribution is the answer.",
                "For a rehearsal, take matrix B and add a self-loop: change the first row to "
                "`1/2 1/2 0` and renormalise nothing else, so the matrix reads "
                "`1/2 1/2 0; 0 0 1; 1 0 0`. The supplied first move is that it is still "
                "irreducible. Work out the period before you type it: the closed walks now have "
                "lengths 1 and 3, so the gcd is 1, and one added arc has turned a chain whose "
                "powers never settle into one whose powers do.",
            ],
        },
        "quiz_title": "Classes, closure and rhythm",
        "quiz": [
            {"q": "A class has one arc leaving it, of probability `1/10000`, and every other arc stays inside. Is the class recurrent?",
             "a": ["Yes, because the escape probability is negligible",
                   "Yes, provided the chain starts inside it",
                   "No: the chain takes that arc eventually with probability one and cannot return, so the class is transient",
                   "It depends on how many states the class has"],
             "c": 2,
             "why": "Over infinitely many visits, the probability of never taking a fixed "
                    "positive chance is zero. The class is left with probability one and never "
                    "re-entered, so it is visited finitely often: transient. The magnitude "
                    "affects how long you wait, not the classification."},
            {"q": "A chain is irreducible with period 3. What does that say about its stationary distribution and about `Pⁿ`?",
             "a": ["Both fail to exist",
                   "The stationary distribution is unique and `Pⁿ` does not converge",
                   "`Pⁿ` converges but the stationary distribution is not unique",
                   "Both exist and agree, but convergence is slow"],
             "c": 1,
             "why": "Irreducibility is what makes the balance system have exactly one solution, "
                    "and that solution is computed by elimination with no limit involved. "
                    "Aperiodicity is what the convergence statement additionally needs; at "
                    "period 3 the powers return to an earlier power exactly, for ever."},
            {"q": "Why does the lab compute the period from a breadth-first levelling instead of listing cycles?",
             "a": ["Because listing cycles would give a different number",
                   "Because a cycle's length is a sum of the per-arc quantities, so the two gcds divide each other and are equal — at the cost of one traversal instead of an enumeration",
                   "Because cycles are only defined for undirected graphs",
                   "Because the gcd of an empty list is undefined"],
             "c": 1,
             "why": "Every closed walk's length is the sum of `level(u) + 1 − level(v)` along "
                    "it, so it is a multiple of the per-arc gcd; and every internal arc lies on "
                    "some closed walk, so the walk gcd divides the arc gcd. Mutual divisibility "
                    "gives equality, and the traversal is linear where an enumeration is not."},
            {"q": "A four-state chain has two classes and BOTH are recurrent. What follows about `πP = π`?",
             "a": ["It has no solution at all",
                   "It has a unique solution putting zero on one of the classes",
                   "It has infinitely many solutions: each closed class has its own, and every mixture of them is stationary too",
                   "It has exactly two solutions, one per class"],
             "c": 2,
             "why": "Each closed class carries a stationary distribution of its own, and any "
                    "convex combination of two stationary distributions is stationary, so there "
                    "is a whole family. The balance matrix is rank deficient, and the honest "
                    "response is to say so rather than to print one member of the family."},
        ],
        "mistakes": [
            ("Treating a small escape probability as no escape",
             "The class with one thin arc out of it is transient, full stop. The size of the "
             "arc changes the expected time to escape, which is a different question and has "
             "its own material later; it does not change the classification, and a chain "
             "described as &ldquo;effectively closed&rdquo; will have an exactly zero "
             "stationary probability on every one of its states."),
            ("Concluding aperiodic because no rhythm was noticed",
             "The period is a gcd and has to be computed. A chain can have closed walks of "
             "lengths 4, 6 and 10 and period 2 with nothing obviously alternating about it. "
             "Aperiodicity has one easy sufficient sign &mdash; any self-loop &mdash; and "
             "beyond that the computation is the evidence."),
            ("Assuming irreducible and aperiodic mean the same thing",
             "They are independent. The three-cycle is irreducible and periodic; a chain with "
             "two closed groups each carrying self-loops is aperiodic and reducible. The "
             "convergence statement needs both, and each preset on this page that breaks one of "
             "them satisfies the other."),
        ],
        "standard": ("Finish when you can partition a chain's states from the arrows alone and say what each class is, without looking at a single probability.",
                     "You should be able to compute reachability and read the classes off it, "
                     "decide recurrence by scanning for an escaping arc and say why the arc's "
                     "size is irrelevant, obtain the period as a gcd rather than by "
                     "observation, and state the two hypotheses of the convergence result "
                     "together with a matrix that fails each one."),
        "note": 'Both hypotheses are now computable, and the statement they support is about a <em>limit</em>. The material that follows argues that the limit was never the point: `πP = π` is n linear equations in n unknowns, one of them redundant, and solving it gives an exact answer on chains where no limit exists at all. &ldquo;The Steady State as a Linear System&rdquo; puts the solve and the iteration on the same page and prints the gap between them.',
    },

    # ---------------------------------------------------------------- 03
    {
        "slug": "the-steady-state-as-a-linear-system",
        "title": "The Steady State as a Linear System",
        "module": "πP = π",
        "one_line": "Drop one dependent balance equation, put Σπ = 1 in its place, and solve exactly — on one preset the answer exists and no limit does.",
        "summary": (
            "`πP = π` is n equations in n unknowns and one of them is implied by the others, "
            "because every column of `P − I` sums to zero. Drop any one of them by name, put "
            "`Σπ = 1` in its place, and run exact Gauss-Jordan over the rationals: the steady "
            "state is a solution of a linear system and nothing iterates. Beside the solve the "
            "page runs the thing readers think a steady state is &mdash; repeated multiplication "
            "in floating point &mdash; and prints how far short it is. On one preset it is short "
            "by `2/3` at every step, for ever, because `P³` is exactly `P⁰` and no limit exists "
            "at all."
        ),
        "key": [
            "πP = π  and  Σπ = 1          the definition: a distribution that one step leaves alone",
            "every column of P − I sums to zero, so the n balance equations are dependent",
            "drop one by name, put Σπ = 1 in its place, and solve exactly — nothing iterates",
            "three brands:  π = (7/17, 11/34, 9/34) exactly,  and πP − π is exactly 0",
            "the 3-cycle:  π = (1/3, 1/3, 1/3) unique,  P³ = P⁰,  and the powers never settle",
            "two closed classes:  rank 3 against 4 unknowns, so the page prints no π at all",
        ],
        "key_label": "One linear system, one dropped equation, and a limit that is not the method",
        "concepts_intro": (
            "Three ideas. The first says what a steady state is, the second says why the obvious "
            "system is short of information, and the third is the claim this whole course exists "
            "to make."
        ),
        "concepts": [
            ("A steady state is defined by an equation, not by a process",
             "`π` is stationary when one step of the chain leaves it unchanged: `πP = π`. That "
             "is an algebraic condition on a vector, and it says nothing about starting "
             "anywhere, waiting, or anything converging. Read as a linear system it is n "
             "equations, one per state, saying that the probability flowing into each state "
             "equals the probability flowing out."),
            ("The n balance equations are dependent, so one must be replaced",
             "`πP = π` is `π(P − I) = 0`, and every column of `P − I` sums to zero because every "
             "row of `P` sums to one. So the n equations have a linear dependency and the "
             "system is rank n − 1 at best: it pins `π` only up to a scale. Dropping one "
             "equation loses nothing, and `Σπ = 1` supplies the one piece of information "
             "`πP = π` never had."),
            ("Solving and waiting are different, and on one matrix only one of them works",
             "Power iteration reaches about fifteen decimal places on a well-behaved chain and "
             "then stops improving, because it has run out of double rather than out of steps. "
             "On the three-cycle it never improves at all: `P³` is exactly the identity, the "
             "powers repeat for ever, and the error sits at `2/3`. The linear system on that "
             "same matrix has one solution, and the solve had it before the iteration took its "
             "first step."),
        ],
        "read_title": "Solving for the steady state, and watching an iteration fail to find it",
        "read_intro": "The equation, the dependency, the replacement, the exact solve, the on-page verification, and the matrix where the two ideas come apart completely.",
        "body": [
            ("def", ("Stationary distribution",
                     "A distribution `π` is <strong>stationary</strong> for `P` when `πP = π`, "
                     "that is `Σᵢ πᵢ P[i][j] = πⱼ` for every `j`, together with `πᵢ ≥ 0` and "
                     "`Σᵢ πᵢ = 1`.",
                     "Equivalently `π(P − I) = 0` with the normalisation attached. Nothing in "
                     "this definition mentions a starting distribution, a number of steps, or a "
                     "limit.")),
            ("thm", ("The balance equations are dependent",
                     "For any transition matrix `P`, the columns of `P − I` sum to zero: "
                     "`Σⱼ (P[i][j] − I[i][j]) = 1 − 1 = 0` for every row `i`. Hence the n "
                     "equations `π(P − I) = 0` have rank at most n − 1, and one of them is "
                     "implied by the rest.")),
            ("proof", ["Row `i` of `P − I` has entries `P[i][j]` for `j ≠ i` and "
                       "`P[i][i] − 1` at `j = i`. Its entries add to `Σⱼ P[i][j] − 1`, which is "
                       "`1 − 1 = 0` because every row of `P` is a distribution.",
                       "So the all-ones column vector is in the null space of `P − I` acting on "
                       "the right, which is exactly the statement that the columns &mdash; the "
                       "equations of the system `π(P − I) = 0` &mdash; sum to the zero "
                       "functional. Adding all n equations together therefore gives `0 = 0`, "
                       "and any one of them can be recovered from the other n − 1."]),
            ("p", "That dependency is the reason the system as written cannot be solved: it "
                  "determines `π` only up to a multiple, and `π = 0` satisfies all of it. The "
                  "repair is not a trick. One equation carries no information the others lack, "
                  "so it is removed by name; and `Σπ = 1`, which `πP = π` never contained, takes "
                  "its place. The lab prints the resulting system with the dropped equation "
                  "named in the caption and the augmented column ruled off, and lets you choose "
                  "which equation to drop. The answer does not move, and watching it not move "
                  "is the point of the control."),
            ("h3", "The solve, and the check the page performs on its own answer"),
            ("math", [
                "three brands,  P =   7/10  2/10  1/10",
                "                     3/10  5/10  2/10",
                "                     1/10  3/10  6/10",
                "",
                "  balance at state 1:   7/10 π₁ + 3/10 π₂ + 1/10 π₃ = π₁",
                "  balance at state 2:   2/10 π₁ + 5/10 π₂ + 3/10 π₃ = π₂",
                "  balance at state 3:   1/10 π₁ + 2/10 π₂ + 6/10 π₃ = π₃     ← dropped",
                "  in its place:              π₁ +     π₂ +     π₃ = 1",
                "",
                "  Gauss-Jordan over the rationals, 9 operations:",
                "",
                "      π = (7/17, 11/34, 9/34)        exactly, rank 3 of 3",
                "",
                "  the page then recomputes πP from that π:",
                "      πP = (7/17, 11/34, 9/34)       every entry EXACTLY equal",
                "      πP − π  =  0                   Σπ = 1",
            ]),
            ("p", "The verification is not decoration. `π` is claimed to satisfy two things, and "
                  "both are recomputed from the vector that came out of the elimination: `πP` is "
                  "formed again and compared entry by entry with exact equality of fractions "
                  "&mdash; not a tolerance &mdash; and the entries are added up. A page that "
                  "asserted this instead of computing it would be a page you have to trust, and "
                  "the whole reason the arithmetic here is rational is that claims of exact "
                  "equality can be made and checked."),
            ("h3", "The iteration, which is a different thing"),
            ("p", "Beside the solve the page runs repeated multiplication in floating point from "
                  "a corner of the simplex, for as many steps as you like, and prints the worst "
                  "entrywise disagreement with the exact answer. On the three-brand matrix the "
                  "disagreement is `2.882e-1` after one step, `2.255e-6` after twenty, and "
                  "`2.776e-16` after sixty. After four hundred steps it is `3.331e-16`, which is "
                  "not better. The iteration has run out of double, not out of steps, and the "
                  "exact column did not iterate at all."),
            ("math", [
                "three brands: how far the floating-point iteration is from the exact answer",
                "",
                "     steps        worst entry error        decimal places agreed",
                "        1            2.882e-1                       0",
                "        4            4.184e-2                       1",
                "       10            1.042e-3                       2",
                "       20            2.255e-6                       5",
                "       40            1.056e-11                     10",
                "       60            2.776e-16                     15",
                "      100            3.331e-16                     15",
                "      400            3.331e-16                     15",
                "",
                "  the exact solve reached (7/17, 11/34, 9/34) at step zero, and stayed there",
            ]),
            ("h3", "The matrix where there is no limit at all"),
            ("p", "Now switch to the three-cycle, `0 1 0; 0 0 1; 1 0 0`. It is irreducible, so "
                  "the balance system has exactly one solution and the page prints "
                  "`π = (1/3, 1/3, 1/3)` with `πP − π` exactly zero. It has period 3, so the "
                  "powers do something the word &ldquo;slowly&rdquo; does not describe: the lab "
                  "finds that `P³` is <em>exactly</em> `P⁰`, so the sequence of powers repeats "
                  "with period 3 for ever. The largest entry of `Pⁿ − π` is exactly `2/3` at "
                  "every single n, and the floating-point iteration sits at `6.667e-1` at one "
                  "step, at four hundred steps, and at every step in between."),
            ("example", ("A unique answer where no limit exists",
                         "On the three-cycle the linear system is rank 3 against 3 unknowns and "
                         "returns `(1/3, 1/3, 1/3)`; `powerCycles` reports `P³` exactly equal "
                         "to `P⁰`; and the exact distance from `Pⁿ` to `π` is `2/3` for "
                         "n = 1, 2, 3, 4, 5, 6 and onwards.",
                         "The sequence does not fail to converge slowly. It does not converge. "
                         "And the steady state is not the limit of anything &mdash; it is the "
                         "solution of three equations in three unknowns, which exists and is "
                         "unique whether or not any limit does. <strong>That is what "
                         "&ldquo;a steady state is a linear system, not a limit&rdquo; "
                         "means</strong>, and this one matrix is where the two come apart.")),
            ("h3", "And the matrix where there is no answer"),
            ("p", "The two-closed-group example is rank deficient: the reduced matrix has rank 3 "
                  "against 4 unknowns, and the page says so and prints nothing. That is the "
                  "right behaviour, because there is no shortage of solutions to print &mdash; "
                  "there are infinitely many, and choosing one would be choosing. "
                  "`(1/2, 1/2, 0, 0)` is stationary. `(0, 0, 3/11, 8/11)` is stationary. So is "
                  "every mixture of the two, and each of those three vectors satisfies "
                  "`πP − π = 0` exactly when it is checked."),
            ("math", [
                "two closed groups   1/2 1/2  0   0",
                "                    1/2 1/2  0   0",
                "                     0   0  1/3 2/3",
                "                     0   0  1/4 3/4",
                "",
                "  three stationary distributions, each verified by recomputing πP:",
                "",
                "      (1/2, 1/2, 0, 0)            πP − π = 0     Σπ = 1",
                "      (0, 0, 3/11, 8/11)          πP − π = 0     Σπ = 1",
                "      (1/4, 1/4, 3/22, 4/11)      πP − π = 0     Σπ = 1",
                "",
                "  and any weighting of the first two is another one",
                "  the page reports rank 3 against 4 unknowns, and prints no π",
            ]),
            ("p", "Note what the lab does and does not do there. It reports the rank and "
                  "refuses; it does not exhibit the family. Exhibiting three members, as above, "
                  "is a stronger demonstration of non-uniqueness than a rank is, because a rank "
                  "is a claim about an elimination and three checked vectors are three checked "
                  "vectors. Both are worth having, and they answer slightly different doubts."),
        ],
        "lab": ("markov", {
            "mode": "steady",
            "preset": "market",
            "panel_title": "Choose which equation to drop, and how long to iterate",
            "panel_intro": "The system is built and reduced here in exact fractions, with the "
                           "dropped equation named in the caption. Beside it a floating-point "
                           "power iteration runs for as many steps as you like and the page "
                           "prints how far short it is. Change which equation is dropped and the "
                           "answer does not move; switch to the 3-cycle and the iteration never "
                           "moves either.",
        }),
        "steps_title": "Solving πP = π by hand",
        "steps_intro": "Five steps, and the third is the one that turns an underdetermined system into a solvable one.",
        "steps": [
            ("Write one balance equation per state",
             "For each `j`, the inflow `Σᵢ πᵢ P[i][j]` equals `πⱼ`. Reading down a COLUMN of `P` "
             "is what gives the equation for that state, which is the opposite of how you read "
             "the matrix to take a step, and is worth saying out loud the first few times."),
            ("Notice that one equation is free",
             "Add them all together and you get `1 = 1`. The system is rank n − 1, so it fixes "
             "`π` only up to a scale and admits the zero vector. Discovering this after an hour "
             "of elimination is the usual route; discovering it from the column sums of "
             "`P − I` takes one line."),
            ("Drop one equation and put the normalisation in its place",
             "Any one. Say which one you dropped, so that the system you actually solved is on "
             "the page. Then add `Σπ = 1`, which is the piece of information `πP = π` never "
             "carried, and you have n independent equations in n unknowns."),
            ("Eliminate in fractions",
             "Gauss-Jordan over the rationals. The three-brand example takes nine operations and "
             "gives `(7/17, 11/34, 9/34)`, with the seventeenths there because seventeen is "
             "what the elimination produced, not because anything was rounded to it."),
            ("Verify by recomputing πP, and check the sum",
             "Multiply your answer back through the matrix and compare entry by entry. This "
             "costs one matrix-vector product and catches every arithmetic slip in the "
             "elimination. If the residual is exactly zero and the entries sum to exactly one, "
             "the answer is right &mdash; and &ldquo;exactly&rdquo; is available here because "
             "nothing was a decimal."),
        ],
        "worked": {
            "title": "One system solved four ways, and two matrices where the iteration has nothing to find",
            "intro": [
                "The three-brand matrix first, with each of the three balance equations dropped "
                "in turn and the normalisation put in its place. Then the two matrices that "
                "separate the solve from the limit.",
            ],
            "lines": [
                "P =   7/10  2/10  1/10          π unknown, three entries",
                "      3/10  5/10  2/10",
                "      1/10  3/10  6/10",
                "",
                "  drop equation 1     π = (7/17, 11/34, 9/34)",
                "  drop equation 2     π = (7/17, 11/34, 9/34)",
                "  drop equation 3     π = (7/17, 11/34, 9/34)",
                "  all three agree, because the dropped one was implied by the others",
                "",
                "  check:  πP = (7/17, 11/34, 9/34)     πP − π = 0     Σπ = 1",
                "  as decimals:  0.411765, 0.323529, 0.264706",
                "",
                "  power iteration in floating point, from (1, 0, 0):",
                "      after  20 steps   worst error 2.255e-6      5 places",
                "      after  60 steps   worst error 2.776e-16    15 places",
                "      after 400 steps   worst error 3.331e-16    15 places",
                "",
                "the 3-cycle   0 1 0 ; 0 0 1 ; 1 0 0",
                "      solve       π = (1/3, 1/3, 1/3)     rank 3 of 3    πP − π = 0",
                "      powers      P³ = P⁰ exactly, so they repeat with period 3",
                "      exact |Pⁿ − π|, worst entry:   n = 1  2/3     n = 2  2/3",
                "                                     n = 3  2/3     n = 6  2/3",
                "      iteration in floating point at 400 steps:  6.667e-1",
                "",
                "two closed groups   rank 3 against 4 unknowns, no unique π",
                "      (1/2, 1/2, 0, 0)   (0, 0, 3/11, 8/11)   (1/4, 1/4, 3/22, 4/11)",
                "      each satisfies πP − π = 0 exactly",
                "",
                "one leaky state    1/2 1/4 1/4 ; 0 3/4 1/4 ; 0 1/2 1/2",
                "      π = (0, 2/3, 1/3)      unique, and the 0 is exact",
            ],
            "after": [
                "Read the three-brand block first and notice what the three identical answers "
                "prove. If dropping a different equation gave a different `π`, the equations "
                "would be carrying different information and removing one would be a choice. "
                "They do not, so it is not.",
                "The three-cycle block is the argument the whole of this material is for. Both "
                "columns are computed on the same matrix at the same moment: a unique exact "
                "answer on the left, and on the right a sequence with no limit whatsoever. "
                "&ldquo;It has not converged yet&rdquo; is the natural thing to say about "
                "`6.667e-1` after four hundred steps, and it is false; there is nothing to "
                "converge to, and the exact distance `2/3` is the same at every n rather than "
                "shrinking at any rate at all.",
                "The leaky chain is the quiet one. Its `π` is unique because it has only one "
                "recurrent class, and it puts exactly `0` on the transient state. That zero is "
                "not a small number rounded down, and no floating-point iteration could have "
                "told you the difference: at sixty steps the iteration's worst error is "
                "`1.110e-16`, which is indistinguishable from a genuinely tiny positive answer.",
                "For a rehearsal, take the two-state chain `1/2 1/2; 1/4 3/4` and solve it by "
                "hand. The supplied first move is the balance equation at state one: "
                "`1/2 π₁ + 1/4 π₂ = π₁`, which gives `π₂ = 2π₁`. Finish with the normalisation "
                "and check your answer against the lab; then ask why the iteration on that "
                "matrix stalls at fifteen places rather than sixteen, and what it would take to "
                "get the sixteenth.",
            ],
        },
        "quiz_title": "Systems, dependencies and limits",
        "quiz": [
            {"q": "Why can `πP = π` not be solved as it stands?",
             "a": ["Because it is not linear",
                   "Because the n equations are dependent, so they fix π only up to a scale and admit π = 0",
                   "Because P is not invertible",
                   "Because π is a row vector and the system expects a column"],
             "c": 1,
             "why": "Every column of `P − I` sums to zero, so adding the n equations gives "
                    "`0 = 0` and the rank is at most n − 1. The system is homogeneous, so the "
                    "zero vector solves it; the missing information is the normalisation, which "
                    "`πP = π` never contained."},
            {"q": "On the three-cycle the power iteration is out by `2/3` after four hundred steps. What is the right description?",
             "a": ["It is converging, but very slowly",
                   "It has hit floating-point noise and cannot improve",
                   "There is no limit: `P³` equals `P⁰` exactly, so the powers repeat for ever and the distance is `2/3` at every step",
                   "The exact answer must be wrong, since the iteration disagrees with it"],
             "c": 2,
             "why": "The lab detects the repetition exactly rather than by tolerance: `P³` is "
                    "the identity, so the sequence of powers is periodic and has no limit. The "
                    "exact distance from `Pⁿ` to `π` is `2/3` for every n. Meanwhile the linear "
                    "system has exactly one solution, which is the whole point."},
            {"q": "On the three-brand matrix the iteration agrees to fifteen places at sixty steps and to fifteen places at four hundred. What has run out?",
             "a": ["The steps", "The double", "The memory", "The precision of the exact solve"],
             "c": 1,
             "why": "The error stops falling at about `3e-16`, which is the resolution of a "
                    "double near these values. More steps cannot help, and the exact column "
                    "never had the problem because it never used a decimal."},
            {"q": "A four-state chain has two recurrent classes. What should a page print for its steady state?",
             "a": ["The one belonging to the larger class",
                   "The average of the two classes' distributions",
                   "That the system is rank deficient and there is no unique answer",
                   "A warning, followed by whichever answer the elimination happened to produce"],
             "c": 2,
             "why": "There are infinitely many stationary distributions and no principle "
                    "selecting one, so printing any of them presents a choice as a result. The "
                    "lab reports rank 3 against 4 unknowns and prints nothing; naming three "
                    "members of the family, as the worked example does, is the constructive "
                    "half of the same answer."},
        ],
        "mistakes": [
            ("Solving the transposed system",
             "`π` multiplies `P` on the left, so the equation for state `j` reads down the "
             "`j`-th COLUMN of `P`. Setting up rows instead solves `Pπ = π`, which is a "
             "different system with a different answer, and on a matrix with all entries "
             "positive it will look plausible enough to survive."),
            ("Trying to solve the n balance equations without replacing one",
             "They are dependent, so elimination will produce a row of zeros and the answer will "
             "come out as a one-parameter family or as zero. The fix is not to persevere; it is "
             "to drop one equation deliberately, say which, and add `Σπ = 1`."),
            ("Reporting a steady state as the limit of a power iteration",
             "It is defined as the solution of a linear system, and on a periodic chain there "
             "is no limit for it to be. Even where a limit exists, the iteration stops "
             "improving at about fifteen places while the solve is exact, so quoting the "
             "iterate concedes precision for nothing. Compute `π`; use the iteration as the "
             "thing being compared against."),
        ],
        "standard": ("Finish when the sentence a steady state is a linear system, not a limit reads as a description of what you do rather than a slogan.",
                     "You should be able to write the n balance equations from the columns of "
                     "`P`, show that they are dependent from the row sums, drop one by name and "
                     "normalise, eliminate in fractions and verify the answer by recomputing "
                     "`πP`, and produce a matrix on which the system has a unique solution and "
                     "the powers have no limit at all."),
        "note": 'The chains here keep moving for ever. The next question is the opposite one: what happens on a chain that can stop, where some states are exits and the interesting quantities are how long until it stops and which exit it takes. Both come out of one matrix inverse &mdash; which is really a sum of powers, and &ldquo;Absorbing States and the Fundamental Matrix&rdquo; shows the sum climbing towards it.',
    },

    # ---------------------------------------------------------------- 04
    {
        "slug": "absorbing-states-and-the-fundamental-matrix",
        "title": "Absorbing States and the Fundamental Matrix",
        "module": "Chains that stop, chains you steer",
        "one_line": "N = (I − Q)⁻¹ is the sum of the powers of Q, so it counts visits; t = N·1 is how long, and B = N·R is where it ends.",
        "summary": (
            "An <strong>absorbing</strong> state is one the chain cannot leave, and that is a "
            "property of the matrix rather than a label put on it. Split the matrix into "
            "transient and absorbing blocks and two questions have one answer: how long until "
            "the chain stops, and which exit it takes. The answer runs through "
            "`N = (I − Q)⁻¹`, which is usually introduced as an inverse and then used as a "
            "count. It is the <strong>sum</strong> of the powers of `Q`, and the lab shows the "
            "partial sums climbing towards it entry by entry, because `Qᵏ[i][j]` is the chance "
            "of being at `j` after exactly k steps and adding those over k counts visits."
        ),
        "key": [
            "absorbing state ⟺ P[i][i] = 1;  the rest are transient",
            "canonical blocks:  Q = transient to transient,  R = transient to absorbing",
            "N = I + Q + Q² + ⋯ = (I − Q)⁻¹        expected visits to each transient state",
            "t = N·1      expected steps to absorption      B = N·R      where it ends up",
            "every row of B sums to 1, checked on the page: absorption happens with probability 1",
            "gambler with 4 units, even stakes:  t = (3, 4, 3),  B rows (3/4,1/4) (1/2,1/2) (1/4,3/4)",
        ],
        "key_label": "One inverse, two questions, and the sum it is really made of",
        "concepts_intro": (
            "Three ideas. The first is a property of the matrix, the second is the identity that "
            "makes the inverse mean something, and the third is what the two block products say."
        ),
        "concepts": [
            ("Absorbing is a property of the matrix, not a label",
             "State `i` is absorbing when `P[i][i] = 1`, which forces every other entry of that "
             "row to zero. The lab checks this against the matrix you typed and refuses a state "
             "you have merely declared absorbing: listing one whose diagonal entry is `3/4` is "
             "a modelling error, and calling it a boundary condition would produce numbers for "
             "a chain that does not stop there."),
            ("N counts visits, because it is a sum of powers",
             "`Qᵏ[i][j]` is the probability of being at transient state `j` after exactly k "
             "steps having started at `i`. Add over all k and you have counted the expected "
             "number of visits to `j`, which is what `N[i][j]` means. That the sum equals "
             "`(I − Q)⁻¹` is the geometric series argument with matrices, and the slider on this "
             "page is the reason rather than the illustration: move it and the partial sums "
             "close on `N` while the page prints what is still missing."),
            ("t and B are the same object read two ways",
             "`t = N·1` adds the expected visits across a row: the total number of steps before "
             "absorption. `B = N·R` multiplies the expected visits by the one-step chance of "
             "exiting to each absorbing state: the probability of finishing there. Every row of "
             "`B` sums to one and the page checks it, which is the statement that the chain is "
             "absorbed with probability one rather than an assumption that it is."),
        ],
        "read_title": "How long until it stops, and where it stops",
        "read_intro": "The canonical form, the series that N really is, the two products, and the case where I − Q has no inverse because the chain never stops.",
        "body": [
            ("def", ("Absorbing states and the canonical blocks",
                     "State `i` is <strong>absorbing</strong> when `P[i][i] = 1`. Order the "
                     "states with the transient ones first and the matrix splits into "
                     "`Q` (transient to transient), `R` (transient to absorbing), a zero block "
                     "and an identity block.",
                     "The <strong>fundamental matrix</strong> is `N = (I − Q)⁻¹`, when the "
                     "inverse exists. `t = N·1` is the vector of expected numbers of steps "
                     "before absorption, and `B = N·R` is the matrix of probabilities of "
                     "finishing in each absorbing state.")),
            ("p", "The lab extracts those blocks from the matrix you typed, given the positions "
                  "of the absorbing states, and computes `N` by exact Gauss-Jordan on "
                  "`[I − Q | I]` over the rationals. So the inverse of a matrix of halves and "
                  "thirds is a matrix of halves and thirds, and the expected times come out as "
                  "fractions you can check by hand."),
            ("thm", ("N is the sum of the powers of Q",
                     "If `(I − Q)` is invertible and `Qᵏ → 0` then "
                     "`I + Q + Q² + ⋯ = (I − Q)⁻¹`, and the `(i, j)` entry of that sum is the "
                     "expected number of visits to transient state `j` starting from transient "
                     "state `i`, counting the start.")),
            ("proof", ["Let `Sₖ = I + Q + ⋯ + Qᵏ`. Then "
                       "`(I − Q)Sₖ = I − Q^(k+1)`, because everything in between cancels &mdash; "
                       "the same telescoping as the scalar geometric series, and matrix "
                       "multiplication is all that was used.",
                       "As `k` grows, `Q^(k+1) → 0` whenever every transient state can reach an "
                       "absorbing one, so `(I − Q)Sₖ → I` and `Sₖ → (I − Q)⁻¹`. For the "
                       "interpretation, note that the expected number of visits to `j` is the "
                       "sum over `k` of the probability of being at `j` at step `k`, which is "
                       "`Σₖ Qᵏ[i][j]` &mdash; the same sum, entry by entry."]),
            ("p", "That is why the slider matters. What is left over from the partial sum after "
                  "k steps is exactly the probability mass still sitting in transient states "
                  "after k steps, and the page prints it beside every entry. On the "
                  "gambler's-ruin example the worst shortfall is `1` at k = 0, `1/2` at k = 2, "
                  "`1/8` at k = 6, `1/32` at k = 10 and `1/1024` at k = 20: halving every two "
                  "steps, which is the chain's own structure showing up in the remainder."),
            ("h3", "The gambler with four units"),
            ("math", [
                "P =  1   0   0   0   0        states 0 1 2 3 4, absorbing 0 and 4",
                "    1/2  0  1/2  0   0        transient  1, 2, 3",
                "     0  1/2  0  1/2  0",
                "     0   0  1/2  0  1/2",
                "     0   0   0   0   1",
                "",
                "  Q =   0  1/2  0            R =  1/2   0",
                "       1/2  0  1/2                0    0",
                "        0  1/2  0                 0   1/2",
                "",
                "  N = (I − Q)⁻¹  =   3/2   1   1/2",
                "                      1    2    1",
                "                     1/2   1   3/2",
                "",
                "  t = N·1  =  (3, 4, 3)        and i(n − i) gives 1·3, 2·2, 3·1",
                "",
                "  B = N·R  =   3/4  1/4        from 1: ruined 3 times in 4",
                "               1/2  1/2        from 2: even, as the symmetry says",
                "               1/4  3/4        from 3: ruined 1 time in 4",
                "",
                "  every row of B sums to 1, checked on the page",
            ]),
            ("p", "The diagonal of `N` is worth a second look. `N[2][2] = 2` says the walk "
                  "started at 2 is at 2 twice on average, counting the start; `N[1][1] = 3/2` "
                  "says the walk started at 1 is at 1 one and a half times. Those are counts of "
                  "visits, and they are what makes the row sums `3, 4, 3` mean &ldquo;total "
                  "steps&rdquo; rather than anything more mysterious."),
            ("example", ("The biased walk, where the symmetry goes",
                         "Change the step probabilities to two-thirds up and one-third down. "
                         "The expected times become `(17/5, 18/5, 11/5)` and the absorption "
                         "probabilities `(7/15, 8/15)`, `(1/5, 4/5)`, `(1/15, 14/15)`.",
                         "From the top transient state the walk now finishes at the far end "
                         "fourteen times in fifteen, and the expected wait from there has "
                         "dropped from 3 to `11/5`. Notice that the middle row is no longer "
                         "even and that the longest wait is still from the middle, but by a "
                         "narrower margin: the drift shortens every journey and skews every "
                         "destination, and both effects come out of the same `N`.")),
            ("h3", "When there is no inverse"),
            ("p", "`I − Q` is singular exactly when some transient state cannot reach an "
                  "absorbing one &mdash; there is a closed set of states you have not declared "
                  "absorbing, the chain can enter it and never leave, and there is no expected "
                  "number of steps to absorption because absorption does not happen. The lab "
                  "reports this rather than producing a number, and the diagnosis it gives is "
                  "the actionable one: every state you have not listed as absorbing has to be "
                  "able to reach one that you have."),
            ("example", ("A chain that never stops",
                         "Take `1 0 0; 0 1/2 1/2; 0 1/2 1/2` and declare the first state "
                         "absorbing. States two and three communicate with each other and with "
                         "nothing else.",
                         "`I − Q` is singular, and the lab says so. The right reading is not "
                         "&ldquo;the arithmetic failed&rdquo; but &ldquo;the model has a second "
                         "closed class in it&rdquo;, which the material on communicating "
                         "classes finds directly and which is very often an unintended "
                         "consequence of a transition that was left out.")),
        ],
        "lab": ("markov", {
            "mode": "absorb",
            "preset": "ruin",
            "panel_title": "Name the absorbing states and add up the powers of Q",
            "panel_intro": "The canonical blocks are extracted from the matrix you typed, and a "
                           "state listed as absorbing whose diagonal entry is not 1 is refused. "
                           "N comes from exact elimination on the augmented matrix, and the "
                           "partial sums I + Q + ⋯ + Qᵏ are shown climbing towards it with the "
                           "shortfall printed beside each entry.",
        }),
        "steps_title": "Working out how long and where",
        "steps_intro": "Four steps, and the first is a check on the matrix rather than on your arithmetic.",
        "steps": [
            ("Confirm each absorbing state from the matrix",
             "`P[i][i] = 1` and the rest of the row zero. A state you intend to be an exit but "
             "which still has an arc out of it is not one, and every figure below would be "
             "answering a question about a different chain."),
            ("Check that every transient state can reach an exit",
             "Otherwise `I − Q` is singular and there is no expected absorption time, because "
             "there is a set of states the chain can enter and never leave. This is a "
             "reachability question and it is answered from the arcs."),
            ("Form Q and R, and invert I − Q in fractions",
             "`Q` is the transient block, `R` the transient-to-absorbing block. Elimination on "
             "`[I − Q | I]` over the rationals gives `N` exactly. On small chains this is "
             "faster by hand than it looks, and the entries are checkable."),
            ("Read t and B off N, and check the rows of B",
             "`t = N·1` for the times, `B = N·R` for the destinations. Every row of `B` must sum "
             "to 1; if one does not, either the arithmetic slipped or the chain escapes "
             "absorption, and the two are worth telling apart before you report anything."),
        ],
        "worked": {
            "title": "Two walks on the same five states, and what the partial sums of Q look like",
            "intro": [
                "The even-money walk first, then the biased one, on the same state space with "
                "the same exits. Everything is exact and every row of `B` is added up.",
            ],
            "lines": [
                "even money, up 1/2 and down 1/2, exits at 0 and 4",
                "",
                "   N     3/2   1   1/2      t = N·1 = (3, 4, 3)",
                "          1    2    1       longest expected wait: 4, from state 2",
                "         1/2   1   3/2",
                "",
                "   B     3/4  1/4           row sums  1",
                "         1/2  1/2                     1",
                "         1/4  3/4                     1",
                "",
                "   partial sums I + Q + ⋯ + Qᵏ, worst entry still missing from N:",
                "      k = 0     1",
                "      k = 2     1/2",
                "      k = 3     1/2",
                "      k = 6     1/8          =  0.12500000",
                "      k = 10    1/32         =  0.03125000",
                "      k = 20    1/1024       =  0.00097656",
                "",
                "   at k = 6 the partial sum is    23/16   7/8   7/16",
                "                                   7/8   15/8   7/8",
                "                                  7/16   7/8   23/16",
                "   against N                      3/2     1    1/2",
                "                                   1      2     1",
                "                                  1/2     1    3/2",
                "",
                "biased, up 2/3 and down 1/3, same exits",
                "",
                "   N     7/5  6/5  4/5       t = (17/5, 18/5, 11/5)",
                "         3/5  9/5  6/5",
                "         1/5  3/5  7/5",
                "",
                "   B     7/15  8/15          row sums  1",
                "          1/5   4/5                    1",
                "         1/15  14/15                   1",
            ],
            "after": [
                "The even-money `t = (3, 4, 3)` matches the closed form `i(n − i)` for a "
                "symmetric walk absorbed at `0` and `n`: `1·3`, `2·2`, `3·1`. That is a useful "
                "coincidence to have met, because it means this instance has an independent "
                "answer and the fundamental matrix is being checked against something rather "
                "than being taken on trust.",
                "The partial-sum block is the argument. At `k = 6` the entry `23/16` is short of "
                "`3/2 = 24/16` by exactly `1/16`, and the shortfall is halving every couple of "
                "steps. That remainder is the probability mass still in transient states after "
                "six steps &mdash; not an error term, not a truncation artefact, but the thing "
                "the series has not yet counted.",
                "For a rehearsal, take the biased walk and predict `B[3][2]` before computing "
                "it. The supplied first move is that from state 3 the walk reaches 4 in one "
                "step with probability `2/3`, so the answer is at least `2/3`. Work out how "
                "much the remaining `1/3` contributes, and check against `14/15`.",
            ],
        },
        "quiz_title": "Visits, times and destinations",
        "quiz": [
            {"q": "What does the entry `N[i][j]` of the fundamental matrix mean?",
             "a": ["The probability of ever reaching `j` from `i`",
                   "The expected number of visits to transient state `j`, starting at `i` and counting the start",
                   "The expected number of steps from `i` to `j`",
                   "The probability of being absorbed at `j`"],
             "c": 1,
             "why": "`N` is `Σₖ Qᵏ`, and `Qᵏ[i][j]` is the probability of being at `j` after "
                    "exactly k steps. Summing probabilities of being somewhere over all times "
                    "counts expected visits. That is why the row sums of `N` are the expected "
                    "times to absorption: total visits to transient states is total steps."},
            {"q": "You declare a state absorbing, but its diagonal entry is `3/4`. What should happen?",
             "a": ["The computation proceeds with the state treated as absorbing",
                   "The remaining `1/4` is redistributed to the other states in the row",
                   "The page refuses, because absorbing is a property of the matrix rather than a label",
                   "The state is silently reclassified as transient"],
             "c": 2,
             "why": "A state with `P[i][i] = 3/4` can be left. Treating it as an exit answers a "
                    "question about a different chain, and the numbers that come out will look "
                    "entirely reasonable. The lab names the state and the offending entry and "
                    "computes nothing."},
            {"q": "`I − Q` turns out to be singular. What is the modelling diagnosis?",
             "a": ["The matrix is too large for exact arithmetic",
                   "Some transient state cannot reach any absorbing state, so the chain need never stop",
                   "Two absorbing states have been listed and only one is allowed",
                   "The rows of `Q` do not sum to 1, which they never do"],
             "c": 1,
             "why": "`Qᵏ` fails to go to zero exactly when there is a closed set among the "
                    "states you did not declare absorbing. There is then no expected time to "
                    "absorption, because absorption is not certain. The fix is in the model, "
                    "usually a transition that was left out."},
            {"q": "On the even-money walk with exits at 0 and 4, the partial sum at `k = 6` is short of `N` by at most `1/8`. What is that remainder?",
             "a": ["Rounding error in the elimination",
                   "The probability mass still in transient states after six steps",
                   "The difference between the exact and the floating-point answer",
                   "The probability of never being absorbed"],
             "c": 1,
             "why": "`N − Sₖ = Q^(k+1) + Q^(k+2) + ⋯`, and `Q^(k+1)[i][j]` is the chance of "
                    "being at transient `j` after `k+1` steps. Nothing here is rounded: `1/8` "
                    "is an exact fraction, and it halves as the walk gets more chances to "
                    "finish."},
        ],
        "mistakes": [
            ("Using N as a formula and never asking what it counts",
             "&ldquo;The expected time to absorption is the row sums of `(I − Q)⁻¹`&rdquo; is "
             "true and teaches nothing. The inverse is a sum of powers, the powers are "
             "probabilities of being somewhere at a given step, and the row sum is therefore a "
             "total number of visits. A reader who has only the formula cannot tell whether a "
             "variant problem is still covered by it."),
            ("Forgetting that N counts the starting visit",
             "`N[i][i] ≥ 1` always, because the chain is at `i` at step zero. The expected times "
             "`t = N·1` therefore count steps taken from the start, and comparing them against "
             "a formula that counts transitions differently is a reliable source of "
             "off-by-one disagreements."),
            ("Reporting an absorption probability without checking the row sums of B",
             "If a row of `B` does not sum to 1 then either the arithmetic is wrong or the chain "
             "escapes absorption with positive probability, and those need completely different "
             "responses. The check is n additions and the page does it in public."),
        ],
        "standard": ("Finish when you can derive N as a series rather than recall it as an inverse, and say what each of its entries counts.",
                     "You should be able to identify absorbing states from the matrix, split it "
                     "into `Q` and `R`, argue that `I + Q + Q² + ⋯` telescopes to `(I − Q)⁻¹`, "
                     "read expected times off the row sums and destinations off `N·R`, check "
                     "the rows of `B`, and recognise a singular `I − Q` as a second closed class "
                     "rather than as a numerical problem."),
        "note": 'So far the chain is something that happens to you. The last of this material puts a choice in every state: two matrices, two reward vectors, and a policy to pick. The evaluation step turns out to be exactly the linear solve already built &mdash; `v = r + γPv` is n equations in n unknowns &mdash; and &ldquo;Markov Decision Processes and Policy Iteration&rdquo; sets it beside value iteration converging to the number the solve already has.',
    },

    # ---------------------------------------------------------------- 05
    {
        "slug": "markov-decision-processes-and-policy-iteration",
        "title": "Markov Decision Processes and Policy Iteration",
        "module": "Chains that stop, chains you steer",
        "one_line": "Evaluate a policy by solving v = r + γPᵈv exactly, improve it greedily, and stop for a reason better than nothing moved.",
        "summary": (
            "Put an action in every state and a reward on every state-action pair, and the chain "
            "becomes a decision problem. A <strong>policy</strong> picks one action per state, "
            "and it induces an ordinary Markov chain whose discounted value solves "
            "`v = r + γPᵈv` &mdash; n linear equations in n unknowns, solved exactly. "
            "<strong>Policy iteration</strong> alternates that solve with a greedy improvement "
            "and stops because there are finitely many policies and the value never decreases: "
            "a termination proof rather than a tolerance. Beside it the page runs value "
            "iteration, which approaches the same numbers from below and is still `7.06` short "
            "after twelve steps."
        ),
        "key": [
            "a policy d picks one action per state, and induces an ordinary chain Pᵈ with reward rᵈ",
            "v = rᵈ + γPᵈv       n equations, n unknowns, solved exactly — the evaluation step",
            "improve greedily:  q(s, a) = r(s, a) + γΣ P(s′|s, a) v(s′),  take the best a",
            "finitely many policies and a value that never decreases ⟹ the loop must stop",
            "two states, two actions: 4 policies, 2 rounds, v = (265/11, 285/11) at γ = 9/10",
            "value iteration after 12 steps: still 7.06068 and 7.06080 BELOW that value",
        ],
        "key_label": "One linear solve per round, and a stopping argument that is not a tolerance",
        "concepts_intro": (
            "Three ideas. The first turns a decision problem into a chain, the second is the "
            "solve that was already built, and the third is why the loop is guaranteed to end."
        ),
        "concepts": [
            ("A policy turns a decision problem back into a chain",
             "Fix one action per state and the transition matrix is determined: row `s` is the "
             "row that action gives. So a policy is an ordinary Markov chain with a reward "
             "attached, and everything already built applies to it. The decision problem is the "
             "question of which of the finitely many chains to be."),
            ("Evaluating a policy is the linear solve, again",
             "`v(s) = r(s) + γ Σ P(s′|s) v(s′)` is n equations in n unknowns, and it is solved "
             "by the same exact elimination that produced the steady state. So the value of a "
             "policy is `265/11` and `285/11` rather than a decimal near them, and a comparison "
             "between two policies is a comparison of fractions. Iterating that equation would "
             "also work and would never finish."),
            ("The loop stops for a reason, not because the numbers stopped moving",
             "Greedy improvement never decreases the value of any state, and there are finitely "
             "many policies &mdash; `2ⁿ` with two actions &mdash; so a policy cannot recur "
             "without the value having stayed put, which is the stopping condition. That is a "
             "proof of termination. Value iteration below it stops when you stop looking, and "
             "the page prints how far short it is when you do."),
        ],
        "read_title": "Choosing an action in every state, and knowing when to stop choosing",
        "read_intro": "The model, the evaluation solve, the greedy improvement, the finiteness argument, and value iteration approaching a number the solve already has.",
        "body": [
            ("def", ("A discounted Markov decision process",
                     "States `1, …, n`, a finite set of <strong>actions</strong>, a transition "
                     "matrix `P(· | s, a)` for each action, a reward `r(s, a)`, and a "
                     "<strong>discount</strong> `γ` with `0 ≤ γ < 1`.",
                     "A <strong>policy</strong> `d` assigns one action to each state. Its "
                     "<strong>value</strong> `v_d` is the unique solution of "
                     "`v = r_d + γ P_d v`, where `P_d` and `r_d` are the matrix and the reward "
                     "vector the policy selects. The unique solution exists because "
                     "`I − γP_d` is invertible for `γ < 1`.")),
            ("p", "The lab takes two transition matrices and two reward vectors, one pair per "
                  "action, and validates each matrix as a chain before anything else. The "
                  "discount is set in twentieths so that it stays a fraction: at `γ = 18/20` "
                  "every value on the page is a rational with a small denominator, which is "
                  "what makes the comparison between two policies decidable rather than "
                  "approximate. The page heads its two action columns simply "
                  "&ldquo;action 1&rdquo; and &ldquo;action 2&rdquo;; which real-world choice "
                  "each stands for is in the matrices and the rewards you typed."),
            ("h3", "Evaluation, improvement, and the round structure"),
            ("p", "A round does two things. It <em>evaluates</em> the current policy by solving "
                  "`v = r_d + γP_d v` exactly &mdash; the lab reports how many elimination "
                  "operations that took &mdash; and then it <em>improves</em>: for each state "
                  "it computes `q(s, a) = r(s, a) + γ Σ P(s′|s, a) v(s′)` for every action, "
                  "using the `v` it just solved for, and switches to the best. If no state "
                  "switched, the policy is optimal and the loop stops."),
            ("math", [
                "two states, two actions, γ = 9/10",
                "",
                "   action 1    P =  1/2  1/2      r = (1, 3)",
                "                    1/4  3/4",
                "   action 2    P =  3/4  1/4      r = (2, 1)",
                "                    1/2  1/2",
                "",
                "  round 1   policy  action 1 / action 1",
                "            solve v = r + γPv     v = (670/31, 750/31)",
                "            q at state 1:  670/31  against  683/31   → switch",
                "            q at state 2:  750/31  against  670/31   → keep",
                "            1 state improved",
                "",
                "  round 2   policy  action 2 / action 1",
                "            solve                 v = (265/11, 285/11)",
                "            q at state 1:  47/2   against  265/11    → keep",
                "            q at state 2:  285/11 against  47/2      → keep",
                "            nothing changed — stop",
                "",
                "  4 policies in total, 2 rounds, and 47/2 = 23.5 against 265/11 = 24.09…",
            ]),
            ("p", "Look at the last comparison. `265/11` and `47/2` differ by `13/22`, which is "
                  "about `0.591`. Both routes to it are exact, so the decision is decided; a "
                  "floating-point evaluation would also have got it right here, and on a "
                  "problem with a near-tie it would be choosing between two roundings and "
                  "reporting a policy. That is the case exactness is insurance against, and it "
                  "is not a rare one at discounts close to 1, where the values of neighbouring "
                  "policies crowd together."),
            ("thm", ("Policy iteration terminates",
                     "Greedy improvement produces a policy whose value is at least as large as "
                     "the current one in every state. Since there are finitely many policies "
                     "and the loop only stops when no state changes, the loop cannot run for "
                     "ever, and the policy it stops at satisfies the optimality condition for "
                     "every state.")),
            ("proof", ["Let `d` be the current policy with value `v`, and `d′` the greedy "
                       "policy. By construction `r_{d′} + γP_{d′}v ≥ v` entrywise, since the "
                       "greedy choice is at least as good as the current action, whose value is "
                       "exactly `v`.",
                       "Applying `r_{d′} + γP_{d′}(·)` repeatedly preserves that inequality, "
                       "because `P_{d′}` has non-negative entries and `γ > 0`; the iterates "
                       "converge to `v_{d′}`, so `v_{d′} ≥ v`. If the values are equal in every "
                       "state, no state changed and the loop has stopped. Otherwise the value "
                       "has strictly increased somewhere, so the policy is new. With finitely "
                       "many policies the loop can only strictly increase finitely often."]),
            ("p", "That is worth contrasting with the other way of solving the same problem. "
                  "Value iteration starts at zero and applies the improvement operator over and "
                  "over; it converges, and there is no step at which anything tells you it has "
                  "arrived. What people do instead is stop when the change between steps falls "
                  "below a number they chose, which is a statement about the increments and not "
                  "about the distance to the answer."),
            ("h3", "Value iteration, measured against the answer the solve already has"),
            ("p", "Because the exact value is on the same page, the lab can print what value "
                  "iteration is actually short by rather than how much it moved last step. On "
                  "the two-state example at `γ = 9/10` the iterates start at `(0, 0)` and climb "
                  "&mdash; `2.00000`, `4.02500`, `5.94875`, `7.72569` &mdash; reaching "
                  "`17.03023` at step twelve against an exact `265/11 = 24.09…`. It is short by "
                  "`7.06068` and `7.06080`, and it approaches from underneath and never "
                  "arrives."),
            ("math", [
                "value iteration on the best policy, state 1, γ = 9/10, exact value 265/11",
                "",
                "     step      v₁          denominator of v₁",
                "        0     0.00000            1 digit",
                "        1     2.00000            1",
                "        4     7.72569            5",
                "        8    13.33076           10",
                "       12    17.03023           15",
                "       20    21.05149",
                "       40    23.72139",
                "",
                "     the exact solve    265/11 = 24.090909…       2 digits, at round 2",
                "",
                "     still short by:   at 12 steps  7.06068      at 40 steps  0.36952",
            ]),
            ("p", "Two things in that table are worth naming. The shortfall shrinks by a factor "
                  "of about `γ` per step, which is why raising the discount towards 1 slows it "
                  "down sharply while policy iteration takes the same two or three rounds. And "
                  "the denominators grow by one power of the discount's denominator every step, "
                  "from one digit to fifteen by step twelve, while the exact answer has a "
                  "two-digit denominator &mdash; the iteration is accumulating complexity as it "
                  "approaches a number that was simple all along."),
            ("example", ("Raising the discount",
                         "At `γ = 9/20` the two-state problem still stops in 2 rounds, with "
                         "value `(1330/341, 1770/341)`, and value iteration is within `0.0003` "
                         "after twelve steps. At `γ = 19/20` it still stops in 2 rounds, with "
                         "value `(1030/21, 1070/21)`, and value iteration is `27.02` short "
                         "after twelve.",
                         "The number of rounds is a property of how many policies there are and "
                         "how quickly the greedy step finds the best one; the iteration's "
                         "progress is a property of `γ`. Those are different mechanisms, and "
                         "the slider makes the difference visible in a few seconds.")),
            ("example", ("Three states and a penalty for being empty",
                         "The stock-control example has three states and rewards "
                         "`(4, 1, −3)` under one action and `(1, 0, −1)` under the other. At "
                         "`γ = 9/10` policy iteration takes 3 rounds over 8 policies and "
                         "settles on `(1640/59, 1440/59, 1345/59)`.",
                         "The middle round is the instructive one: the greedy step swings the "
                         "policy from all-hold to all-restock, values it at `(10, 360/41, "
                         "310/41)`, and then swings the first state back. A method that stopped "
                         "at the first improvement would have taken that middle policy and been "
                         "wrong by between fifteen and eighteen in every state.")),
        ],
        "lab": ("markov", {
            "mode": "mdp",
            "preset": "machine",
            "panel_title": "Two actions, two matrices, two reward vectors",
            "panel_intro": "Every policy is evaluated by solving v = r + γPv exactly rather than "
                           "by iterating it, which is what lets the page show value iteration "
                           "converging TO something instead of stopping when it gets bored. "
                           "Raise the discount towards 1 and watch the iteration slow down "
                           "while the number of rounds does not move.",
        }),
        "steps_title": "Running policy iteration by hand",
        "steps_intro": "Four steps and a loop. The first is the one people skip, and it is what makes the comparison in the third meaningful.",
        "steps": [
            ("Check each action's matrix separately",
             "Each action needs its own transition matrix and each of those has to be a chain in "
             "its own right: every row summing to 1. A single bad row anywhere means one of the "
             "policies being compared is not a chain, and the comparison will still produce a "
             "winner."),
            ("Pick any starting policy and evaluate it exactly",
             "Solve `v = r_d + γP_d v`. Any starting policy will do &mdash; the loop is not "
             "sensitive to it &mdash; so take the obvious one. Solve rather than iterate: this "
             "is n equations in n unknowns and the elimination is short."),
            ("Improve greedily, one state at a time, using the value you just solved for",
             "For each state compute `q(s, a)` for every action and take the best. Use the same "
             "`v` throughout the sweep; recomputing it mid-sweep is a different algorithm with "
             "different guarantees."),
            ("Stop when no state changed, and say that that is a proof",
             "No change means the policy is greedy with respect to its own value, which is the "
             "optimality condition. Combined with finiteness and monotonicity, the loop "
             "terminates. This is a reason to stop; &ldquo;the numbers stopped moving&rdquo; is "
             "not, and on value iteration it is never even true."),
        ],
        "worked": {
            "title": "A two-state machine, two rounds, and a value iteration that never catches up",
            "intro": [
                "Two states and two actions. Under one action the state decays faster and pays "
                "more when worn; under the other it holds better and pays more when good. "
                "Discount `γ = 9/10`, so there are four policies in total.",
            ],
            "lines": [
                "action 1   P = 1/2 1/2 ; 1/4 3/4        r = (1, 3)",
                "action 2   P = 3/4 1/4 ; 1/2 1/2        r = (2, 1)",
                "",
                "round 1    policy (1, 1)",
                "           v solves  v = r + (9/10)Pv     4 elimination operations",
                "           v = (670/31, 750/31) = (21.613, 24.194)",
                "",
                "           q(state 1, action 1) = 670/31 = 21.613",
                "           q(state 1, action 2) = 683/31 = 22.032      ← better",
                "           q(state 2, action 1) = 750/31 = 24.194      ← better",
                "           q(state 2, action 2) = 670/31 = 21.613",
                "           1 state improved",
                "",
                "round 2    policy (2, 1)",
                "           v = (265/11, 285/11) = (24.0909, 25.9091)",
                "",
                "           q(state 1, action 1) = 47/2   = 23.5000",
                "           q(state 1, action 2) = 265/11 = 24.0909     ← keep",
                "           q(state 2, action 1) = 285/11 = 25.9091     ← keep",
                "           q(state 2, action 2) = 47/2   = 23.5000",
                "           nothing changed — stop, after 2 rounds over 4 policies",
                "",
                "value iteration on the same policy, from (0, 0):",
                "     step  1     2.00000        short by 22.09091",
                "     step  4     7.72569        short by 16.36522",
                "     step  8    13.33076        short by 10.76015",
                "     step 12    17.03023        short by  7.06068",
                "     step 20    21.05149        short by  3.03942",
                "     step 40    23.72139        short by  0.36952",
                "     exact      265/11          short by 0, at round 2",
            ],
            "after": [
                "Round 1 is where the method earns its name. The policy being evaluated is not "
                "optimal, and the `q` values computed from its own value function still point "
                "at the better action: `683/31` beats `670/31` at the first state. That is the "
                "improvement theorem in one comparison &mdash; you do not need the optimal value "
                "function to find a better policy, only the current one's.",
                "Round 2 stops, and it stops for a reason you can state: both states are already "
                "choosing the action their own value function prefers, so the policy is greedy "
                "with respect to itself. No tolerance was involved and no number had to be "
                "compared against a threshold.",
                "The value-iteration block underneath is the comparison the whole page exists "
                "for. It is converging to `265/11`, it is monotone from below, and after forty "
                "steps it is still `0.36952` short of a number the solve produced in four "
                "elimination operations. Its denominators have gone from one digit to fifteen "
                "on the way to a number whose denominator is `11`.",
                "For a rehearsal, set the discount to its lowest setting and predict what "
                "happens to both methods before looking. The supplied first move is that at a "
                "small `γ` the future barely counts, so the greedy one-step reward nearly "
                "decides the policy. Say what you expect of the round count and of the "
                "iteration's shortfall, then check: the rounds stay at 2 and the shortfall at "
                "twelve steps collapses to about `0.0003`.",
            ],
        },
        "quiz_title": "Policies, values and stopping",
        "quiz": [
            {"q": "What makes the evaluation step of policy iteration a linear system rather than a fixed-point iteration?",
             "a": ["Nothing: it must be iterated, because `v` appears on both sides",
                   "`v = r + γPv` rearranges to `(I − γP)v = r`, which is n equations in n unknowns and is solved by elimination",
                   "The rewards are linear in the state",
                   "It is linear only when the discount is zero"],
             "c": 1,
             "why": "`(I − γP)` is invertible for `γ < 1`, so the equation is an ordinary linear "
                    "system and the exact value of a policy comes out of one elimination. "
                    "Iterating it also converges and never finishes, which is exactly the "
                    "comparison the page draws."},
            {"q": "Policy iteration stops when no state's action changed. Why is that a better stopping rule than value iteration's?",
             "a": ["It is not: both are tolerances",
                   "Because it certifies that the policy is greedy with respect to its own exact value, and with finitely many policies and a non-decreasing value the loop must reach that point",
                   "Because policy iteration always takes exactly two rounds",
                   "Because value iteration cannot be run on the same problem"],
             "c": 1,
             "why": "No change means the optimality condition holds at every state, and the "
                    "argument that the loop gets there is finiteness plus monotonicity. Value "
                    "iteration's usual rule compares consecutive iterates, which bounds the "
                    "step and not the distance to the answer."},
            {"q": "After twelve steps value iteration on the two-state example sits `7.06` below the exact value. What does that number depend on most?",
             "a": ["The number of states", "The number of policies",
                   "The discount, since the shortfall shrinks by roughly a factor of γ per step",
                   "The size of the rewards alone"],
             "c": 2,
             "why": "The iteration contracts by `γ` per step, so the shortfall after a fixed "
                    "number of steps is governed by the discount. At a lower discount the same "
                    "twelve steps land within `0.0003`; at a higher one they are `27` short, "
                    "while policy iteration takes the same two rounds throughout."},
            {"q": "The exact value of the best policy is `265/11`, and value iteration's twelfth iterate has a fifteen-digit denominator. What does that say?",
             "a": ["The iterate is more precise than the exact answer",
                   "The iteration is accumulating complicated fractions on the way to a simple number it never reaches",
                   "The exact answer must have been rounded to `265/11`",
                   "The two are computing different quantities"],
             "c": 1,
             "why": "Each step multiplies by the discount, so the denominator gains a factor of "
                    "20 every time. The limit is `265/11`. Complexity of representation and "
                    "closeness to the answer are unrelated, and here they move in opposite "
                    "directions."},
        ],
        "mistakes": [
            ("Improving a state using a value that has already been updated in the same sweep",
             "Policy iteration evaluates the policy once and then improves every state against "
             "that single value vector. Updating as you go is a different algorithm with "
             "different behaviour, and the finiteness argument above does not apply to it as "
             "written."),
            ("Stopping value iteration on the change between steps and reporting it as the answer",
             "The gap between consecutive iterates is not the gap to the limit; with a discount "
             "close to 1 it understates it badly. This page can print the true shortfall only "
             "because the exact value is sitting beside it, which is the situation you will not "
             "be in when it matters."),
            ("Comparing two policies on floating-point values",
             "Two policies can differ by `13/22` in value, as the two actions at the first state "
             "do here, and at a discount near 1 they can differ by far less. A comparison of "
             "two roundings returns a policy either way and says nothing about which is better. "
             "Evaluate exactly and the comparison is decided."),
        ],
        "standard": ("Finish when you can run a round of policy iteration on paper and state why the loop must end.",
                     "You should be able to build `P_d` and `r_d` from a policy, solve "
                     "`v = r_d + γP_d v` as a linear system, compute `q(s, a)` for each action "
                     "from that `v` and improve greedily, give the finiteness-and-monotonicity "
                     "argument for termination, and say what value iteration's shortfall depends "
                     "on and why its stopping rule measures the wrong thing."),
        "note": 'Everything so far has been one matrix with n named states. The material that follows keeps the chain and throws the matrix away: on a queue the states are 0, 1, 2, … and the only transitions are up one and down one, so the whole distribution comes out of one equation applied between each pair of neighbours. &ldquo;The Cut Equation, and Every Queue From It&rdquo; derives it and then checks it against the full balance system solved by elimination.',
    },
]
