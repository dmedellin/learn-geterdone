"""Advanced Design and Analysis Techniques, lessons 6-9 -- Chapters 16 and 17.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed.
(MIT Press, 2009): Chapter 16, Greedy Algorithms (pp. 414-450), and
Chapter 17, Amortized Analysis (pp. 451-480). Every quotation is copied from
the operator's copy with its printed page in the comment beside the lesson.
The intervals, weights, graphs, tasks and operation sequences are written for
these lessons; the book's figures, examples and exercises are named, not
reproduced.
"""

# The activity-selection lesson's ten activities, typed into the lab.
ACTIVITIES = "0-9, 1-3, 2-5, 4-6, 5-8, 7-10, 9-11, 6-13, 11-14, 12-15"

LESSONS = [
    # ---------------------------------------------------------------- 06
    # CLRS Chapter 16 opening and sections 16.1-16.2, pp. 414-428.
    # Quote: p. 414, 13 words, quotes.py OK. Lesson total: 13 words.
    # Greedy choice and later greedy algorithms (p. 414); the problem,
    # half-open intervals, sorted by finish (p. 415); optimal substructure
    # over S_ij and recurrence 16.2 (p. 416); the greedy choice and
    # Theorem 16.1 (pp. 417-418); RECURSIVE- and GREEDY-ACTIVITY-SELECTOR,
    # Theta(n) after sorting (pp. 418-421); the six steps and the three-step
    # design, greedy-choice property, optimal substructure, 0-1 against
    # fractional knapsack (pp. 423-427).
    {
        "slug": "activity-selection-and-the-greedy-strategy",
        "title": "Activity Selection and the Greedy Strategy",
        "module": "Chapter 16 · Greedy Algorithms",
        "one_line": "Choosing the activity that finishes first, again and again, schedules as many compatible activities as possible, and the proof is an exchange: some optimal schedule already makes that choice.",
        "summary": (
            "Chapter 16 opens with a problem that dynamic programming could solve and does not "
            "need to. Activity selection has optimal substructure, but one choice, the activity "
            "with the earliest finish, can be made before any subproblem is solved, and a short "
            "exchange argument shows it is always part of some optimal solution. Section 16.2 "
            "draws the general lesson: the greedy-choice property and optimal substructure, and "
            "the knapsack problems as a warning. Run the earliest-finish rule by hand on ten "
            "activities, then let the lab check it against every subset."
        ),
        "key": [
            "pick the activity that finishes first",
            "then solve only what starts after it",
            "exchange: an optimum can start that way",
            "Θ(n) after sorting by finish time",
            "greedy choice first, subproblem second",
            "whole-item knapsack needs a table",
        ],
        "key_label": "Sections 16.1 and 16.2 in six lines",
        "concepts_intro": (
            "Three ideas, the two ingredients of a greedy proof and the one that tells greedy "
            "from dynamic programming."
        ),
        "concepts": [
            ("Compatible activities",
             "Activity `aᵢ` occupies the half-open interval `[sᵢ, fᵢ)`. Two activities are "
             "compatible when their intervals do not overlap, so one finishing at 6 and another "
             "starting at 6 can both be scheduled. The problem asks for a largest set of "
             "mutually compatible activities."),
            ("The greedy-choice property",
             "A globally optimal solution can be reached by making the choice that looks best "
             "now, without consulting the answers to subproblems. It is proved, usually by taking "
             "an optimal solution and exchanging one of its choices for the greedy one without "
             "making it worse."),
            ("Greedy against dynamic programming",
             "Both need optimal substructure. Dynamic programming solves the subproblems first "
             "and chooses with their answers known, usually bottom-up. A greedy algorithm chooses "
             "first and then solves the single subproblem the choice leaves, usually top-down."),
        ],
        "read_title": "From a dynamic program to a single choice",
        "read_intro": (
            "Read the opening of Chapter 16 and sections 16.1 and 16.2 in your own copy first. "
            "The lesson follows the authors from the dynamic-programming formulation to the "
            "greedy one, runs the rule by hand, and then checks it against every subset in the "
            "lab."
        ),
        "body": [
            ("p", "&ldquo;A greedy algorithm always makes the choice that looks best at the "
                  "moment.&rdquo; The authors open Chapter 16 with that sentence and qualify it at "
                  "once: the hope is that locally optimal choices add up to a globally optimal "
                  "solution, and often they do not. The chapter studies problems where they do, "
                  "and later chapters supply more, among them minimum spanning trees, Dijkstra's "
                  "shortest paths and a greedy heuristic for set cover. This lesson reads the "
                  "opening and sections 16.1 and 16.2."),
            ("p", "Section 16.1's problem: n activities want one resource, a lecture hall, and "
                  "activity `aᵢ` would hold it during `[sᵢ, fᵢ)`. Select as many mutually "
                  "compatible activities as possible. The activities are assumed sorted by finish "
                  "time. The authors deliberately take the long way round, starting from dynamic "
                  "programming. Let `Sᵢⱼ` be the activities that start after `aᵢ` finishes and "
                  "finish before `aⱼ` starts. If an optimal set for `Sᵢⱼ` contains `aₖ`, it "
                  "contains optimal sets for `Sᵢₖ` and `Sₖⱼ`, by cut and paste, and the size "
                  "`c[i, j]` satisfies a recurrence that tries every `aₖ` in `Sᵢⱼ` "
                  "(recurrence 16.2). A table would work. It would also be overlooking something."),
            ("thm", ("Theorem 16.1, the greedy choice is safe",
                     "In any nonempty subproblem `Sₖ`, the activities that start after `aₖ` "
                     "finishes, let `aₘ` be one with the earliest finish time. Then `aₘ` belongs "
                     "to some maximum-size set of mutually compatible activities of `Sₖ`.")),
            ("p", "The proof is an exchange. Take any maximum set `Aₖ` and its earliest-finishing "
                  "activity `aⱼ`. If `aⱼ = aₘ`, done. Otherwise replace `aⱼ` by `aₘ`: since `aₘ` "
                  "finishes no later than `aⱼ`, it still ends before every other member starts, "
                  "the set stays compatible, and it is just as large. So choosing the first "
                  "activity to finish never costs anything, and once it is chosen only one "
                  "subproblem remains: the activities that start at or after its finish. None can "
                  "finish before it starts, because it finishes earliest of all."),
            ("p", "That turns the table into a single scan. RECURSIVE-ACTIVITY-SELECTOR adds a "
                  "fictitious activity `a₀` finishing at time 0, looks for the first activity that "
                  "starts no earlier than the last chosen one finishes, takes it, and recurses on "
                  "what follows. GREEDY-ACTIVITY-SELECTOR is the same loop without the recursion. "
                  "Each activity is examined once, so after sorting by finish time the work is "
                  "`Θ(n)`. Here is the rule on this lesson's ten activities, sorted by finish."),
            ("math", [
                "activity   1-3  2-5  4-6  5-8  0-9  7-10  9-11  6-13  11-14  12-15",
                "finish      3    5    6    8    9    10    11    13    14     15",
                "",
                "take 1-3     last finish 3",
                "skip 2-5     starts at 2 < 3",
                "take 4-6     last finish 6",
                "skip 5-8, 0-9",
                "take 7-10    last finish 10",
                "skip 9-11, 6-13",
                "take 11-14   last finish 14",
                "skip 12-15                       four activities",
            ]),
            ("p", "Section 16.2 extracts the method. The long route went through six steps, "
                  "from optimal substructure and a recurrence to an iterative greedy algorithm. "
                  "The short route has three: cast the problem as a choice that leaves one "
                  "subproblem; prove some optimal solution makes the greedy choice; and show that "
                  "the greedy choice plus an optimal solution to what remains is optimal. The two "
                  "ingredients are the <strong>greedy-choice property</strong> and optimal "
                  "substructure, and the authors add that beneath almost every greedy algorithm "
                  "lies a more cumbersome dynamic program."),
            ("p", "The warning is the knapsack. In the 0-1 knapsack each item is taken whole or "
                  "left; in the fractional knapsack any fraction may be taken. Both have optimal "
                  "substructure, yet only the fractional one yields to the greedy rule of taking "
                  "the best value per pound first. A small instance of this lesson's own: "
                  "capacity 7, items of weight 1, 3 and 4 worth 3, 7 and 9. By value per pound "
                  "the order is the first, the second, the third; the 0-1 greedy takes the first "
                  "two for 10 and cannot fit the third, while the second and third together weigh "
                  "7 and are worth 16. The fractional greedy takes the first two and three "
                  "quarters of the third, `3 + 7 + 6.75 = 16.75`, which is optimal. In the 0-1 "
                  "problem an item must be weighed against leaving it out, and that comparison "
                  "needs the subproblems solved: dynamic programming."),
            ("p", "Now the lab, the intervals lab of the Algorithms Subject's lesson Greedy Rules "
                  "and the Optimum. It runs four greedy rules on the intervals you type, earliest "
                  "finish, earliest start, shortest first and fewest conflicts, finds the true "
                  "optimum by trying every subset, checks the chosen set for overlaps, and "
                  "performs the exchange argument one swap at a time. An interval `4-6` holds "
                  "from 4 up to but not including 6."),
            ("p", "The lab's presets are its own, and three of them each break one of the other "
                  "rules. <code>startfails</code> opens with one interval covering the whole day "
                  "and four short ones inside it: earliest finish takes 4, the optimum is 4, and "
                  "earliest start, if you switch the rule, takes the long one and nothing else. "
                  "<code>shortestfails</code> puts a short interval across two longer ones that "
                  "fit together: optimum 2, shortest first 1. <code>conflictfails</code> does the "
                  "same to fewest conflicts with seven intervals."),
            ("p", "Then type this lesson's ten activities. The lab reads 10 intervals, earliest "
                  "finish selects 4, the most any of the 1,024 subsets fits is 4, the selection is "
                  "feasible, and the exchange argument survives every swap. Switch to earliest "
                  "start and the count falls to 3: the activity `0-9` starts first and blocks "
                  "everything before 9, and the lab's exchange table breaks at the first swap it "
                  "tries. Earliest finish matching 4 out of 1,024 subsets here is "
                  "one instance agreeing with Theorem 16.1; the theorem's exchange is what "
                  "covers the instances nobody has typed."),
            ("h3", "Exercise"),
            ("p", "On the lesson's ten activities, run the rule that picks the activity that "
                  "starts last, and works backwards from the end of the day, taking each "
                  "activity that finishes by the time the last chosen one starts. Compare its "
                  "selection and size with the earliest-finish rule's. The rule is the one in "
                  "Exercise 16.1-2, which asks for its proof; work that in the book."),
            ("p", "Activity selection's greedy choice was easy to see. The next lesson, Huffman "
                  "Codes, makes a greedy choice that is not obvious at all, and proves it by the "
                  "same kind of exchange."),
        ],
        "lab": ("greedy", {
            "mode": "intervals",
            "preset": "startfails",
            "panel_title": "Four greedy rules against every subset",
            "panel_intro": (
                "Type intervals as start-finish, separated by commas. The lab runs four greedy "
                "rules, finds the largest compatible set among every subset, and performs the "
                "exchange argument swap by swap. Type the lesson's ten activities, then try the "
                "other rules."
            ),
        }),
        "steps_title": "Running the earliest-finish rule by hand",
        "steps_intro": "Four steps run and check the rule; the fifth is a day of your own.",
        "steps": [
            ("Sort by finish time",
             "List the activities in order of finish time; break ties any way you like."),
            ("Take the first, and remember its finish",
             "The first activity in the list finishes earliest. Take it and write down its "
             "finish time."),
            ("Scan once",
             "Go down the list; take each activity that starts at or after the last finish you "
             "wrote, and write its finish instead. Skip the others."),
            ("Check the exchange on one optimum",
             "Find another maximum set by hand. Replace its earliest-finishing activity with the "
             "rule's first choice and check that the set is still compatible."),
            ("Do it on a day of your own",
             "Write eight to eleven activities from your own calendar as start-finish hours, run "
             "the rule by hand, then type them into the lab and compare your count with the "
             "optimum over every subset."),
        ],
        "worked": {
            "title": "The exchange on one optimum of the lesson's activities",
            "intro": [
                "One maximum set of the ten activities is `2-5, 5-8, 9-11, 11-14`, four "
                "activities. The greedy rule's first choice is `1-3`.",
            ],
            "lines": [
                "earliest finish in the set: 2-5",
                "1-3 finishes at 3, no later than 5",
                "swap: 1-3, 5-8, 9-11, 11-14",
                "1-3 ends at 3 ≤ 5, where 5-8 starts",
                "still compatible, still four",
            ],
            "after": [
                "The swap works because the greedy activity finishes no later than the one it "
                "replaces, so it cannot collide with anything that came after that one. Repeated "
                "on what follows, the same swap turns any optimum into the greedy selection.",
            ],
        },
        "quiz_title": "Greedy choices and their proofs",
        "quiz": [
            {"q": "Activities `[2, 6)` and `[6, 9)` are both requested. Are they compatible?",
             "a": ["No, because both contain the instant 6",
                   "Yes, because the first interval is half-open and ends just before 6",
                   "Only if they are sorted by start time",
                   "No, because compatible activities must leave a gap"],
             "c": 1,
             "why": "Intervals are half-open, `[sᵢ, fᵢ)`, so `[2, 6)` does not contain 6 and the "
                    "two do not overlap; the book's test is `sᵢ ≥ fⱼ` or `sⱼ ≥ fᵢ`, and "
                    "`6 ≥ 6`. Sorting changes nothing about overlap, and no gap is required."},
            {"q": "In Theorem 16.1's exchange, why is the set still compatible after `aⱼ` is "
                  "replaced by `aₘ`?",
             "a": ["Because `aₘ` starts before `aⱼ`",
                   "Because `aₘ` is shorter than `aⱼ`",
                   "Because `aₘ` finishes no later than `aⱼ`, which finished before every other "
                   "member started",
                   "Because the set was sorted by finish time"],
             "c": 2,
             "why": "`aⱼ` was the earliest to finish in the optimal set, so every other member "
                    "starts at or after `fⱼ`, and `fₘ ≤ fⱼ`. When `aₘ` starts and how long it "
                    "lasts do not matter: it could start earlier and be longer. Sorting is a "
                    "convenience for the algorithm, not part of the argument."},
            {"q": "Capacity 7, items of weight 1, 3 and 4 worth 3, 7 and 9. What do the 0-1 and "
                  "the fractional knapsack optima come to?",
             "a": ["16 and 16.75", "10 and 16.75", "16 and 16", "19 and 19"],
             "c": 0,
             "why": "In the 0-1 problem the second and third items fit exactly, `3 + 4 = 7`, for "
                    "16; taking the best ratio first gives only 10. The fractional optimum takes "
                    "the first two whole and three quarters of the third, `3 + 7 + 6.75 = 16.75`. "
                    "Nineteen is all three items, which weigh 8."},
            {"q": "What does the lab report for the lesson's ten activities under the "
                  "earliest-start rule?",
             "a": ["4, equal to the optimum",
                   "3, below the optimum of 4",
                   "1, because `0-9` blocks everything",
                   "5, above the optimum, which shows the optimum was wrong"],
             "c": 1,
             "why": "Earliest start takes `0-9`, then the first activity starting at 9 or later, "
                    "`9-11`, then `11-14`: three. The optimum over every subset is 4. `0-9` blocks "
                    "only what starts before 9, and no feasible selection can exceed the optimum, "
                    "which is why the lab also checks feasibility."},
        ],
        "mistakes": [
            ("Trusting a greedy rule because it sounds sensible",
             "Earliest start, shortest first and fewest conflicts all sound reasonable, and each "
             "loses on an instance the lab carries; on this lesson's activities earliest start "
             "takes 3 where 4 fit. A greedy rule is right only when its choice is proved safe, "
             "as Theorem 16.1 proves for earliest finish."),
            ("Reading one agreement as the proof",
             "The lab's exhaustive search shows earliest finish reaching the optimum on the "
             "instance in front of it, among 1,024 subsets here. That is evidence about ten "
             "activities. The exchange argument is about every instance, and it is the reason "
             "the rule is used."),
            ("Expecting the knapsack to yield to greedy too",
             "Both knapsacks have optimal substructure, and only the fractional one has the "
             "greedy-choice property. On the lesson's three items the best ratio first gives 10 "
             "in the 0-1 problem, where 16 is possible. Optimal substructure alone does not "
             "license a greedy algorithm."),
        ],
        "standard": (
            "Finish when you can run and justify the earliest-finish rule.",
            "Given eight to eleven activities, select a maximum set by the earliest-finish rule, "
            "carry out the exchange on another optimum, and give an instance where another "
            "greedy rule fails."
        ),
        "note": (
            "The lab's exhaustive search tries every subset, so it caps the instance at eleven "
            "intervals, and its presets are its own: the lesson's activities are typed in. It "
            "has no knapsack here; the Algorithms lesson Fractional and 0/1 Knapsack runs both."
        ),
    },
    # ---------------------------------------------------------------- 07
    # CLRS section 16.3, pp. 428-437.
    # Quote: p. 431, 15 words, quotes.py OK. Lesson total: 15 words.
    # Savings of 20% to 90%, fixed- and variable-length codes (pp. 428-429);
    # prefix codes, decoding, code trees, full binary trees, B(T) (pp. 429-
    # 431); HUFFMAN with a min-priority queue, n - 1 merges, O(n lg n)
    # (pp. 431-433); Lemma 16.2 by exchange, Lemma 16.3, Theorem 16.4
    # (pp. 433-435); chapter notes: Huffman, 1952 (p. 450).
    {
        "slug": "huffman-codes",
        "title": "Huffman Codes",
        "module": "Chapter 16 · Greedy Algorithms",
        "one_line": "Huffman's algorithm builds an optimal prefix code by repeatedly merging the two least frequent symbols, and two exchange lemmas show that this greedy merge is always safe.",
        "summary": (
            "Section 16.3 compresses a file by giving frequent characters short codewords. "
            "Prefix codes, in which no codeword begins another, decode without ambiguity and are "
            "drawn as binary trees whose cost is the sum of frequency times depth. Huffman's "
            "algorithm merges the two lightest trees n − 1 times with a min-priority queue, in "
            "O(n lg n). One lemma shows the two rarest symbols can be siblings at the bottom of "
            "an optimal tree, another that merging them leaves a smaller problem of the same "
            "kind. Build a code by hand, then let the lab check it against every tree."
        ),
        "key": [
            "no codeword is a prefix of another",
            "a prefix code is a binary tree",
            "cost B(T): frequency times depth, summed",
            "merge the two lightest, n − 1 times",
            "the two rarest can be deepest siblings",
            "B(T) is the sum of all merge totals",
        ],
        "key_label": "Section 16.3 in six lines",
        "concepts_intro": (
            "Three ideas: what makes a code decodable, what a code costs, and why the cheapest "
            "merge is safe."
        ),
        "concepts": [
            ("Prefix code",
             "A binary code in which no codeword is a prefix of another. Encoding concatenates "
             "codewords; decoding reads bits until they spell a codeword, emits it, and starts "
             "again, which is unambiguous because no longer codeword can begin the same way. "
             "The authors note that such codes lose nothing in compression against any other "
             "character code."),
            ("The code tree and its cost",
             "A prefix code is a binary tree with the characters at the leaves, 0 for a left "
             "edge and 1 for a right. An optimal code's tree is full, with `|C|` leaves and "
             "`|C| − 1` internal nodes. Its cost `B(T)` is the sum over characters of frequency "
             "times depth, the number of bits the file takes."),
            ("The greedy merge",
             "Huffman's choice: take the two least frequent items, make them children of a new "
             "node whose frequency is their sum, and repeat. Each merge adds the sum of the two "
             "frequencies to the cost, so the rule always makes the cheapest merge available."),
        ],
        "read_title": "Codes as trees, the merge, and two lemmas",
        "read_intro": (
            "Read Section 16.3 in your own copy first. The lesson sets out prefix codes and the "
            "cost in its own words, builds one code by hand, follows the two lemmas, and then "
            "lets the lab check the code against every tree."
        ),
        "body": [
            ("p", "&ldquo;Huffman invented a greedy algorithm that constructs an optimal prefix "
                  "code called a Huffman code.&rdquo; The authors state it plainly in Section "
                  "16.3 and spend the rest of the section earning the word optimal. A prefix "
                  "code, as a footnote concedes, would be better called prefix-free: no codeword "
                  "is a prefix of another. This lesson reads the section."),
            ("p", "The section begins with a file of characters and their frequencies. A "
                  "fixed-length code spends the same number of bits on every character, three for "
                  "an alphabet of six. A variable-length code gives frequent characters short "
                  "codewords and rare ones long codewords, and the authors report typical savings "
                  "of 20% to 90%, depending on the data. The catch is decoding: with variable "
                  "lengths, where does one codeword end? Prefix codes answer it, since the first "
                  "codeword of the encoded bits can always be recognised."),
            ("p", "A prefix code is a binary tree: each character a leaf, each codeword the path "
                  "from the root, 0 for left and 1 for right. These are not binary search trees; "
                  "the leaves need not be in any order. An optimal code has a <em>full</em> tree, "
                  "where every internal node has two children (Exercise 16.3-2): a node with one "
                  "child could be removed, shortening every codeword below it. The number of bits "
                  "for the file is `B(T)`, the sum of `c.freq · d(c)` over the characters c, "
                  "where `d(c)` is the depth of c's leaf and also the length of its codeword."),
            ("p", "David Huffman found the algorithm, which the chapter notes date to 1952. "
                  "HUFFMAN puts the characters in a min-priority queue keyed on frequency, then "
                  "`n − 1` times extracts the two least frequent items, makes them the children of "
                  "a new node whose frequency is their sum, and inserts that node. The last item "
                  "left is the root. With a binary min-heap each of the `O(n)` queue operations "
                  "costs `O(lg n)`, so the algorithm takes `O(n lg n)`; the authors note a van "
                  "Emde Boas tree would bring it to `O(n lg lg n)`. Here is the algorithm on this "
                  "lesson's six characters, with frequencies a:14, b:6, c:10, d:21, e:4, f:5, "
                  "which total 60."),
            ("math", [
                "queue:  e:4  f:5  b:6  c:10  a:14  d:21",
                "merge e:4 + f:5      =  9     queue: b:6  9  c:10  a:14  d:21",
                "merge b:6 + 9        = 15     queue: c:10  a:14  15  d:21",
                "merge c:10 + a:14    = 24     queue: 15  d:21  24",
                "merge 15 + d:21      = 36     queue: 24  36",
                "merge 24 + 36        = 60     the root",
                "",
                "codeword lengths:  a 2, c 2, d 2, b 3, e 4, f 4",
                "B(T) = 14·2 + 10·2 + 21·2 + 6·3 + 4·4 + 5·4 = 144 bits",
                "     = 9 + 15 + 24 + 36 + 60, the sum of the merges",
            ]),
            ("p", "So the code spends 144 bits on a file with these 60 characters, `12/5 = 2.4` "
                  "bits a character against 3 for a fixed-length code. The last line is Exercise "
                  "16.3-4's identity: each merge pushes every leaf below it one level down, so "
                  "the tree's cost is the sum of the merged frequencies, and Huffman's rule always "
                  "chooses the cheapest merge on offer."),
            ("thm", ("Lemma 16.2, the greedy choice",
                     "If x and y are two characters of lowest frequency, some optimal prefix code "
                     "gives x and y codewords of the same length that differ only in the last "
                     "bit: they are sibling leaves at the greatest depth.")),
            ("p", "The proof is an exchange like Theorem 16.1's. Take any optimal tree and two "
                  "sibling leaves a and b at its greatest depth. Swap x with a: x moves down, a "
                  "moves up, and since x is no more frequent than a and a was no shallower than x, "
                  "the cost does not rise. Swap y with b in the same way. The result is still "
                  "optimal and has x and y as deepest siblings. Lemma 16.3 supplies optimal "
                  "substructure: replace x and y by one new character z of frequency "
                  "`x.freq + y.freq`; for any tree T′ for the smaller alphabet, splitting z's leaf "
                  "into x and y gives a tree T with `B(T) = B(T′) + x.freq + y.freq`, so an "
                  "optimal T′ yields an optimal T. Theorem 16.4 follows: HUFFMAN produces an "
                  "optimal prefix code."),
            ("p", "Now the lab, the Huffman lab of the Algorithms Subject's lesson Huffman Codes. "
                  "It builds the tree for the symbols and weights you type, shows the merges one "
                  "at a time, lists the codewords, checks that no codeword is a prefix of another, "
                  "encodes a message and decodes it again, and enumerates every full binary tree "
                  "and every assignment of the weights to its leaves to confirm the cost is the "
                  "minimum. Its presets are its own; <code>skewed</code> gives one symbol 60 of "
                  "100 and the expected length is `17/10` bits against 3, and "
                  "<code>uniform</code> gives four equal weights, where Huffman saves nothing."),
            ("p", "Type this lesson's alphabet, `a:14, b:6, c:10, d:21, e:4, f:5`, and the "
                  "message `faced`. The lab reads 6 symbols, prints an expected length of "
                  "`12/5 = 2.400` bits a symbol against 3 for a fixed-length code, confirms the "
                  "code is prefix-free and the message comes back, and reports the cost at the "
                  "minimum over every tree. The message takes `4 + 2 + 2 + 4 + 2 = 14` bits "
                  "instead of 15. The codewords themselves may differ from yours where the lab "
                  "puts a different child on the left; the lengths cannot."),
            ("p", "The enumeration agreeing at six symbols is a check on one alphabet. Lemmas "
                  "16.2 and 16.3 are what make the merge right for alphabets of any size, where "
                  "no enumeration could finish."),
            ("h3", "Exercise"),
            ("p", "Build the Huffman tree by hand for `p:2, q:3, r:5, s:5, t:9, u:14`. At which "
                  "steps does the queue hold equal frequencies? Build the tree twice, breaking the "
                  "first such tie each way, and say whether the choice changes the codeword "
                  "lengths, the cost, or both. Compute `B(T)` from the depths and as the sum of "
                  "the merges, then type the alphabet into the lab."),
            ("p", "Huffman's rule and the earliest-finish rule were proved one problem at a "
                  "time. The next lesson, Matroids and Greedy Methods, describes a whole family "
                  "of problems on which the greedy rule is always right, and one scheduling "
                  "problem that belongs to it."),
        ],
        "lab": ("greedy", {
            "mode": "huffman",
            "preset": "skewed",
            "panel_title": "Merge the two lightest, then check the code",
            "panel_intro": (
                "Type symbols as name:weight, separated by commas, and a message. The lab shows "
                "each merge, the tree and the codewords, checks the code prefix-free, encodes and "
                "decodes the message, and compares the cost with every full binary tree. Type "
                "the lesson's alphabet a:14, b:6, c:10, d:21, e:4, f:5."
            ),
        }),
        "steps_title": "Building a Huffman code by hand",
        "steps_intro": "Four steps build and price the code; the fifth is an alphabet of your own.",
        "steps": [
            ("Queue the characters by frequency",
             "Write every character with its frequency in increasing order."),
            ("Merge the two smallest",
             "Remove the two smallest, write a new node with their sum, and put it back in "
             "order. Repeat until one node is left; there are `n − 1` merges."),
            ("Read off the codeword lengths",
             "Draw the tree from the merges: each merged pair are siblings under their sum. A "
             "character's codeword length is its depth."),
            ("Price the code two ways",
             "Compute `B(T)` as the sum of frequency times depth, and again as the sum of the "
             "merged totals. They must agree."),
            ("Do it on an alphabet of your own",
             "Count the letters of a short sentence of your own, build the code by hand, then "
             "type the counts and the sentence's letters as the message into the lab and compare "
             "your cost with its expected length times the total weight."),
        ],
        "worked": {
            "title": "Why a fixed-length code is not optimal here",
            "intro": [
                "A three-bit code for six characters uses six of the eight codewords. Its tree "
                "has an internal node with only one child.",
            ],
            "lines": [
                "fixed: 000 001 010 011 100 101",
                "no codeword starts 11, so the node",
                "  for prefix 1 has one child (10)",
                "drop that node: 100 → 10, 101 → 11",
                "two characters save a bit each",
                "the tree is still a prefix code",
            ],
            "after": [
                "Any tree with a one-child node can be shortened this way, which is why an "
                "optimal code's tree is full. On the lesson's alphabet the fixed code costs "
                "`60·3 = 180` bits, the shortened one less, and Huffman's 144.",
            ],
        },
        "quiz_title": "Prefix codes, merges and lemmas",
        "quiz": [
            {"q": "Which of these codes is a prefix code?",
             "a": ["0, 10, 110, 111", "0, 01, 11", "1, 10, 100", "00, 01, 0"],
             "c": 0,
             "why": "In 0, 10, 110, 111 no codeword begins another. In 0, 01, 11 the codeword 0 "
                    "begins 01. In 1, 10, 100, 1 begins both others. In 00, 01, 0, the codeword "
                    "0 begins 00 and 01."},
            {"q": "What is the second merge Huffman's algorithm makes on the lesson's alphabet "
                  "a:14, b:6, c:10, d:21, e:4, f:5?",
             "a": ["c:10 with a:14", "b:6 with c:10", "b:6 with the node 9 made from e and f",
                   "e:4 with f:5"],
             "c": 2,
             "why": "The first merge joins e:4 and f:5 into 9. The queue then holds 6, 9, 10, 14 "
                    "and 21, and the two smallest are b:6 and 9. Merging b with c skips the "
                    "smaller new node. c with a is the third merge, and e with f the first."},
            {"q": "For the lesson's code, why is `B(T) = 144` also the sum `9 + 15 + 24 + 36 + 60` "
                  "of the merged totals?",
             "a": ["Each merge pushes every character below it one level deeper, adding their "
                   "total frequency to the cost once",
                   "It is a coincidence of this alphabet",
                   "Each merge costs the same as the one before plus the frequencies merged",
                   "The total frequency 60 is counted once per character"],
             "c": 0,
             "why": "A character at depth d lies below exactly d internal nodes, each made by one "
                    "merge, so summing the merged totals counts its frequency d times, which is "
                    "its share of `B(T)`. It holds for every tree (Exercise 16.3-4), so it is no "
                    "coincidence. The root's 60 is counted once, not once per character."},
            {"q": "In Lemma 16.2's proof, x, a rarest character, is swapped with a, a leaf of "
                  "greatest depth. Why does the cost not rise?",
             "a": ["Because x and a have the same frequency",
                   "Because the change in cost is `(a.freq − x.freq)·(d(a) − d(x))` taken away, "
                   "and both factors are at least zero",
                   "Because swapping leaves never changes the cost",
                   "Because a is a sibling of y"],
             "c": 1,
             "why": "Moving x down to a's depth and a up to x's changes the cost by "
                    "`−(a.freq − x.freq)·(d(a) − d(x))`; x is rarest, so the first factor is at "
                    "least zero, and a is deepest, so the second is too. The frequencies need not "
                    "be equal, swaps in general do change the cost, and a's sibling is b, not y."},
        ],
        "mistakes": [
            ("Thinking a variable-length code needs separators",
             "If no codeword is a prefix of another, the bits decode themselves: read until you "
             "have a codeword, emit it, carry on. The lab's round trip on the message `faced` "
             "returns it from 14 bits with nothing between the codewords. A code that needs "
             "separators is not a prefix code."),
            ("Merging by the original frequencies only",
             "After a merge the new node competes in the queue like any character. On the "
             "lesson's alphabet the second merge is b:6 with the new node 9, not b:6 with c:10; "
             "skipping the merged node gives a different tree that costs more."),
            ("Expecting Huffman to compress every file",
             "The saving comes from unequal frequencies. With equal weights the lab's "
             "<code>uniform</code> preset gives every symbol two bits, the same as a fixed-length "
             "code, and Exercise 16.3-8 shows that nearly equal frequencies over 256 characters "
             "cannot beat eight bits. The algorithm is optimal; the optimum may save nothing."),
        ],
        "standard": (
            "Finish when you can build and price a Huffman code by hand.",
            "Given five to seven characters with frequencies, carry out the merges, give each "
            "codeword's length, compute `B(T)` two ways, and say how the greedy-choice lemma's "
            "exchange works."
        ),
        "note": (
            "The lab's codewords depend on which child it puts on the left, which the book calls "
            "arbitrary; lengths and cost do not. Its check against every tree is exhaustive only "
            "for small alphabets, and the lesson's alphabet is typed in. Optimality in general "
            "is Lemmas 16.2 and 16.3."
        ),
    },
    # ---------------------------------------------------------------- 08
    # CLRS sections 16.4-16.5, pp. 437-446.
    # Quote: p. 437, 11 words, quotes.py OK. Lesson total: 11 words.
    # Matroid definition, Whitney, matric and graphic matroids, Theorem 16.5
    # (pp. 437-438); extensions, maximal sets, Theorem 16.6, weighted
    # matroids, optimal subsets, MST through w0 - w(e) (pp. 438-440); GREEDY
    # and its O(n lg n + n f(n)) time (p. 440); Lemma 16.7, Lemma 16.8,
    # Corollary 16.9, Lemma 16.10, Theorem 16.11 (pp. 441-442); unit-time
    # tasks, early and late, canonical form, Lemma 16.12, Theorem 16.13,
    # O(n^2) (pp. 443-446); chapter notes: Whitney 1935, Edmonds 1971 (p. 450).
    {
        "slug": "matroids-and-greedy-methods",
        "title": "Matroids and Greedy Methods",
        "module": "Chapter 16 · Greedy Algorithms",
        "one_line": "A matroid is a family of independent sets closed under subsets and satisfying an exchange property, and on every weighted matroid the greedy algorithm finds a maximum-weight independent set; scheduling unit-time tasks with deadlines is one.",
        "summary": (
            "Sections 16.4 and 16.5 are starred, and they explain a large class of greedy "
            "successes at once. A matroid is a ground set with a hereditary family of "
            "independent subsets in which a smaller independent set can always be extended from "
            "a larger one. The forests of a graph form one. On any weighted matroid GREEDY, "
            "taking elements by decreasing weight whenever independence survives, returns an "
            "optimal subset, by a greedy-choice lemma and a contraction. Unit-time tasks with "
            "deadlines and late penalties give a matroid too. Test a graph in the lab and "
            "schedule six tasks by hand."
        ),
        "key": [
            "independent sets: closed under subsets",
            "exchange: a smaller set can grow",
            "forests of a graph form a matroid",
            "all maximal independent sets: same size",
            "greedy: heaviest first, if independent",
            "tasks scheduled on time form a matroid",
        ],
        "key_label": "Sections 16.4 and 16.5 in six lines",
        "concepts_intro": (
            "Three ideas: the two axioms, what greedy computes on them, and the scheduling "
            "problem that turns out to satisfy them."
        ),
        "concepts": [
            ("Matroid",
             "A pair `M = (S, ℐ)` of a finite set S and a nonempty family ℐ of its subsets, the "
             "independent sets, that is <strong>hereditary</strong>, every subset of an "
             "independent set is independent, and has the <strong>exchange property</strong>: if "
             "A and B are independent and `|A| < |B|`, some element of B not in A can be added "
             "to A keeping it independent."),
            ("Weighted matroid and optimal subset",
             "Give each element a positive weight and a set the sum of its elements' weights. An "
             "optimal subset is an independent set of greatest weight. With positive weights it "
             "is always maximal, and all maximal independent sets of a matroid have the same "
             "size (Theorem 16.6)."),
            ("Early and late tasks",
             "In a schedule of unit-time tasks, a task is early if it finishes by its deadline "
             "and late otherwise. A set of tasks is independent if some schedule makes all of "
             "them early; the problem of least total penalty becomes finding an independent set "
             "of greatest total penalty."),
        ],
        "read_title": "Two axioms, one algorithm, one schedule",
        "read_intro": (
            "Read sections 16.4 and 16.5 in your own copy first; both are starred, and both "
            "repay the effort. The lesson sets out the axioms and the proof in its own words, "
            "tests a graph in the lab, and schedules six tasks by hand."
        ),
        "body": [
            ("p", "&ldquo;In this section, we sketch a beautiful theory about greedy "
                  "algorithms.&rdquo; The authors open Section 16.4 with that sentence and are "
                  "careful about its reach: the theory covers many cases of practical interest but "
                  "not all, and in particular neither activity selection nor Huffman codes. This "
                  "lesson reads the two starred sections that finish Chapter 16."),
            ("p", "The word matroid is Hassler Whitney's, from a 1935 paper the chapter notes "
                  "cite; he was studying the rows of a matrix, where a set of rows is independent "
                  "if it is linearly independent. The greedy algorithm on matroids entered "
                  "combinatorial optimization with a 1971 article by Jack Edmonds. The example "
                  "the section proves in full is the <strong>graphic matroid</strong>: the ground "
                  "set is the edges of an undirected graph, and a set of edges is independent if "
                  "it contains no cycle, that is, if it forms a forest."),
            ("thm", ("Theorem 16.5, the forests of a graph form a matroid",
                     "Heredity is immediate: removing edges cannot create a cycle. For exchange, a "
                     "forest with vertex set V and edge set A has exactly `|V| − |A|` trees. If "
                     "`|B| > |A|`, the forest B has fewer trees than A, so some tree of B joins "
                     "vertices lying in two different trees of A, and one of its edges joins "
                     "them; adding that edge to A creates no cycle.")),
            ("p", "Section 16.4 then adds vocabulary. An element x is an extension of an "
                  "independent A if adding it keeps A independent, and A is maximal if it has no "
                  "extension. Theorem 16.6, all maximal independent sets have the same size, "
                  "follows straight from exchange; in a connected graph's matroid the maximal sets "
                  "are the spanning trees, each with `|V| − 1` edges. A weighted matroid gives "
                  "each element a positive weight, and the authors show that the minimum-spanning-"
                  "tree problem is one: weigh each edge `w₀ − w(e)`, with `w₀` larger than every "
                  "length, and a heaviest maximal forest is a lightest spanning tree."),
            ("p", "GREEDY sorts the elements by decreasing weight and takes each one whose "
                  "addition keeps the set independent. Its time is `O(n lg n + n·f(n))`, where "
                  "`f(n)` is the cost of one independence test. The proof of Theorem 16.11 has "
                  "three parts. Lemma 16.7 is the greedy choice: the first element x that is "
                  "independent on its own belongs to some optimal subset, shown by growing "
                  "`{x}` from an optimal B by exchange until the two differ in one element, which "
                  "cannot outweigh x. Corollary 16.9 says an element that cannot be added to the "
                  "empty set can never be added later, so passing it over loses nothing. Lemma "
                  "16.10 is optimal substructure: after x is taken, what remains is to solve the "
                  "contraction of the matroid by x, which is a matroid again."),
            ("p", "Section 16.5 applies the theory to a scheduling problem. There are n tasks, "
                  "each taking one unit of time on a single processor, each with an integer "
                  "deadline and a penalty paid if it finishes late. Any schedule can be put in "
                  "early-first form, with every early task before every late one, and then in "
                  "canonical form, with the early tasks in order of deadline; swapping never makes "
                  "an early task late. So the problem is to choose the set of early tasks."),
            ("thm", ("Lemma 16.12 and Theorem 16.13",
                     "For a set of tasks A, let `Nₜ(A)` be the number of tasks in A with deadline "
                     "t or earlier. A is independent, schedulable with none late, exactly when "
                     "`Nₜ(A) ≤ t` for every t, which holds exactly when running A in order of "
                     "deadline makes no task late. The independent sets of tasks form a matroid.")),
            ("p", "So GREEDY applies: take tasks by decreasing penalty, keeping each one whose "
                  "addition keeps every `Nₜ` within t. Each test costs `O(n)` and there are n of "
                  "them, `O(n²)` in all; Problem 16-4 gives a faster version. Here is an instance "
                  "of this lesson's own, six tasks."),
            ("math", [
                "task        a1   a2   a3   a4   a5   a6",
                "deadline     2    1    3    2    4    1",
                "penalty     60   45   40   35   25   15",
                "",
                "a1 (60)  take       N1 = 0, N2 = 1",
                "a2 (45)  take       N1 = 1, N2 = 2",
                "a3 (40)  take       N3 = 3",
                "a4 (35)  reject     N2 would be 3 > 2",
                "a5 (25)  take       N4 = 4",
                "a6 (15)  reject     N1 would be 2 > 1",
                "",
                "schedule: a2, a1, a3, a5, then a4, a6 late;   penalty 35 + 15 = 50",
            ]),
            ("p", "The lab is the matroid lab of the Algorithms Subject's lesson Independence "
                  "Systems and Matroids. It defines a family by a membership test, lists every "
                  "independent set by running the test on all `2ⁿ` subsets, tests the exchange "
                  "property on every ordered pair, runs GREEDY for the weights you type and "
                  "compares it with the heaviest independent set. Its families are uniform, "
                  "graphic, partition and the matchings of a graph; it has no task-scheduling "
                  "family, which is why the schedule above is worked by hand."),
            ("p", "The presets are the lab's own. <code>uniform</code>, any two of five "
                  "elements, has 16 independent sets and rank 2. <code>matchings</code> takes "
                  "the matchings of a three-edge path, which are hereditary but fail exchange: "
                  "the middle edge alone cannot grow, though the two end edges together exist, "
                  "and the lab finds weights on which greedy loses. Choose <code>graphic</code> "
                  "and type this lesson's graph, two triangles sharing vertex 3, as the edges "
                  "`1-2, 2-3, 1-3, 3-4, 4-5, 3-5` with weights `9 4 6 8 3 5`. The lab counts 6 "
                  "elements and 49 independent sets, rank 4, tests exchange on 867 ordered pairs "
                  "and confirms it is a matroid, and finds "
                  "greedy equal to the optimum: it takes the edges of weight 9, 8, 6 and 5, a "
                  "spanning tree of weight 28."),
            ("p", "Forty-nine is `7·7`: in each triangle every set of edges except all three is a "
                  "forest, and the triangles share no cycle. That count, and greedy's agreement, "
                  "are facts about one small graph. Theorem 16.11 is what makes GREEDY correct on "
                  "every weighted matroid, including those of graphs with millions of edges."),
            ("h3", "Exercise"),
            ("p", "Raise the penalty of a6 from 15 to 70, keeping everything else in the six-task "
                  "instance. Run GREEDY by hand with the `Nₜ` test, give the early set, the "
                  "canonical schedule and the total penalty, and check that every rejection is "
                  "forced by some `Nₜ > t`."),
            ("p", "Chapter 16 ends here. The next lesson, Amortized Analysis and Dynamic Tables, "
                  "opens Chapter 17, which bounds the cost of a whole sequence of operations "
                  "rather than one at a time."),
        ],
        "lab": ("greedy", {
            "mode": "matroid",
            "preset": "graphic",
            "panel_title": "Test the exchange property, then run greedy",
            "panel_intro": (
                "Choose a family, give its parameter and a weight per element. The lab lists "
                "every independent set, tests exchange on every pair, and sets greedy beside the "
                "heaviest independent set. With the graphic family, type the lesson's edges "
                "1-2, 2-3, 1-3, 3-4, 4-5, 3-5 and weights 9 4 6 8 3 5."
            ),
        }),
        "steps_title": "Checking a matroid and running greedy",
        "steps_intro": "Four steps on a family; the fifth is tasks of your own.",
        "steps": [
            ("Check heredity",
             "Take an independent set and remove any element: is what remains independent? For "
             "forests, schedulable task sets and sets of at most k elements it always is."),
            ("Check exchange on a pair",
             "Take independent sets A and B with `|A| < |B|` and find an element of B outside A "
             "that keeps A independent. One pair where none exists ends the matter: not a "
             "matroid."),
            ("Run greedy by decreasing weight",
             "Sort the elements, heaviest first, and take each one whose addition keeps the set "
             "independent. Write down every rejection and the reason."),
            ("Check the answer is maximal",
             "In a matroid with positive weights greedy's answer is maximal, and every maximal "
             "set has the same size. Count yours against the rank."),
            ("Do it on tasks of your own",
             "Write five to seven unit-time tasks, each with a deadline and a penalty, run greedy with "
             "the `Nₜ` test by hand, give the canonical schedule and its penalty, and check it by "
             "trying one other schedule."),
        ],
        "worked": {
            "title": "The exchange step of Theorem 16.5 on the lesson's graph",
            "intro": [
                "In the two-triangle graph take `A = {1-2, 4-5}` and `B = {1-3, 2-3, 3-4}`, both "
                "forests, with `|A| = 2 < |B| = 3`.",
            ],
            "lines": [
                "A on 5 vertices: 5 − 2 = 3 trees",
                "  {1, 2}, {4, 5}, {3}",
                "B: 5 − 3 = 2 trees, {1, 2, 3, 4}, {5}",
                "B's big tree spans A's trees",
                "edge 1-3 joins {1, 2} and {3}",
                "A + 1-3 = {1-2, 4-5, 1-3}: a forest",
            ],
            "after": [
                "The count of trees does the work: B has fewer, so one of its trees must straddle "
                "two of A's, and an edge of that tree crossing between them can join A. Edge 2-3 "
                "would do as well; edge 3-4 too.",
            ],
        },
        "quiz_title": "Matroids, greedy and deadlines",
        "quiz": [
            {"q": "Which family is a matroid on the ground set `{1, 2, 3, 4}`?",
             "a": ["All sets of at most two elements",
                   "All sets with an even number of elements",
                   "The sets `{}`, `{1}`, `{2}` and `{1, 2, 3}`",
                   "All sets containing the element 1"],
             "c": 0,
             "why": "Sets of at most k elements form the uniform matroid (Exercise 16.4-1): any "
                    "subset is small enough, and a smaller set can always take an element from a "
                    "larger one. The even sets are not hereditary, since `{1}` is inside "
                    "`{1, 2}`. The third family omits `{1, 3}`, a subset of `{1, 2, 3}`. Sets "
                    "containing 1 exclude the empty set, which every hereditary family holds."},
            {"q": "In the lesson's two-triangle graph with weights `9 4 6 8 3 5` on edges "
                  "`1-2, 2-3, 1-3, 3-4, 4-5, 3-5`, which edges does GREEDY reject?",
             "a": ["1-3 and 3-5", "Only 4-5", "None, since the graph has six edges and the rank "
                   "is six", "2-3 and 4-5"],
             "c": 3,
             "why": "Greedy takes 1-2 (9), 3-4 (8), 1-3 (6) and 3-5 (5); then 2-3 (4) would close "
                    "the triangle 1, 2, 3, and 4-5 (3) the triangle 3, 4, 5. Rejecting 1-3 and "
                    "3-5 would mean taking lighter edges first. The rank is 4, the size of a "
                    "spanning tree on five vertices, not six."},
            {"q": "Four unit-time tasks have deadlines 1, 2, 2 and 4. Can all four be early?",
             "a": ["Yes, there are four tasks and the latest deadline is 4",
                   "No, because `N₂ = 3 > 2`",
                   "Yes, if they run in order of deadline",
                   "No, because `N₁ = 1` is not less than 1"],
             "c": 1,
             "why": "Three tasks have deadline 2 or earlier and only two can finish by time 2, so "
                    "`N₂ = 3 > 2` and one of them must be late. The latest deadline says nothing "
                    "about the crowding at time 2, and running in deadline order is Lemma 16.12's "
                    "test, which fails there. The condition is `Nₜ ≤ t`, so `N₁ = 1` is allowed."},
            {"q": "Why does GREEDY never need to reconsider an element it passed over because it "
                  "was not an extension of the empty set?",
             "a": ["Such an element has the smallest weight",
                   "By Corollary 16.9 it cannot extend any independent set at all",
                   "GREEDY sorts it to the end of the list",
                   "The exchange property forces it into every maximal set"],
             "c": 1,
             "why": "If x could extend some independent A, then `A ∪ {x}` would be independent "
                    "and, by heredity, so would `{x}`; Corollary 16.9 is the contrapositive. "
                    "Weight has nothing to do with it, GREEDY sorts by weight only, and such an "
                    "element is in no independent set at all."},
        ],
        "mistakes": [
            ("Assuming every hereditary family is a matroid",
             "Heredity is the easy axiom. The matchings of a graph are hereditary, since a subset "
             "of a matching is a matching, and they fail exchange on a three-edge path; the lab's "
             "<code>matchings</code> preset finds weights on which greedy then loses. Without "
             "exchange, Theorem 16.11 does not apply."),
            ("Believing matroids explain every greedy algorithm",
             "The authors say plainly that the theory does not cover activity selection or "
             "Huffman codes, both proved greedy-optimal in this chapter by their own exchange "
             "arguments. A matroid is a sufficient reason for greedy to work, not the only one."),
            ("Scheduling the early tasks by penalty",
             "Greedy picks the early set by decreasing penalty; the schedule then runs that set "
             "in order of deadline, which Lemma 16.12 shows makes none late. In the lesson's "
             "instance the early set is chosen as a1, a2, a3, a5 but run as a2, a1, a3, a5, "
             "because a2's deadline is 1."),
        ],
        "standard": (
            "Finish when you can test a family and run greedy on it.",
            "Given a small family of sets, check heredity and exchange or find the pair that "
            "fails; run GREEDY on a weighted graphic matroid; and schedule five to seven "
            "unit-time tasks with deadlines by the `Nₜ` test."
        ),
        "note": (
            "The lab has no family for unit-time tasks, so Section 16.5 is worked by hand. Its "
            "graph families are capped at six edges, because every subset and every pair of "
            "independent sets is enumerated. The theorem holds for every matroid; the lab tests "
            "small ones."
        ),
    },
    # ---------------------------------------------------------------- 09
    # CLRS Chapter 17, sections 17.1-17.4, pp. 451-471 (to p. 480 with the
    # exercises, problems and notes).
    # Quote: p. 451, 14 words, quotes.py OK. Lesson total: 14 words.
    # Amortized against average-case, the three methods, charges not in the
    # code (pp. 451-452); aggregate analysis of MULTIPOP and INCREMENT,
    # floor(n/2^i) flips, < 2n (pp. 452-455); accounting, inequality 17.1,
    # credit never negative, 2 for PUSH and for setting a bit (pp. 456-458);
    # potential, equations 17.2-17.4, Phi = stack size and number of 1s,
    # counters not starting at zero (pp. 459-462); dynamic tables, load
    # factor, doubling, 3n by aggregate, $3 by accounting, Phi = 2 num -
    # size (pp. 463-467); contraction at 1/2 thrashes, at 1/4 with equation
    # 17.6, insert at most 3, delete bounded (pp. 467-471).
    {
        "slug": "amortized-analysis",
        "title": "Amortized Analysis and Dynamic Tables",
        "module": "Chapter 17 · Amortized Analysis",
        "one_line": "Amortized analysis bounds the total cost of any sequence of operations, so that an occasional expensive operation is paid for by many cheap ones, and three methods, aggregate, accounting and potential, reach the bound by different bookkeeping.",
        "summary": (
            "Chapter 17 bounds the worst-case cost of a whole sequence of operations and divides "
            "by its length. Aggregate analysis sums the sequence directly; the accounting method "
            "overcharges some operations and stores the surplus as credit on objects; the "
            "potential method stores it as a function of the whole structure. All three are "
            "applied to a stack with MULTIPOP and to a binary counter, and the potential method "
            "then designs a table that doubles when full and halves when a quarter full, with "
            "constant amortized cost per operation. Work the counter and the stack by hand, then "
            "let the lab price a table operation by operation."
        ),
        "key": [
            "amortized: worst case of a sequence",
            "no probability, unlike average case",
            "aggregate: total cost over n",
            "accounting: credit never below zero",
            "potential: actual cost plus change in Φ",
            "double when full, halve at a quarter",
        ],
        "key_label": "Chapter 17 in six lines",
        "concepts_intro": (
            "Three ideas: what an amortized bound promises, and the two ways of storing prepaid "
            "work."
        ),
        "concepts": [
            ("Amortized cost",
             "A bound on the total cost of any sequence of n operations, spread over the "
             "operations. It is a worst-case guarantee about sequences: no probability is "
             "involved, which is what separates it from average-case analysis. A single "
             "operation may cost far more than its amortized cost."),
            ("Credit",
             "In the accounting method each operation is charged an amortized cost; the excess "
             "over its actual cost is stored as credit on particular objects and spent later. The "
             "total credit must never be negative, so that the charges bound the actual costs for "
             "every prefix of every sequence."),
            ("Potential",
             "In the potential method the prepaid work belongs to the structure as a whole: a "
             "function Φ of the structure's state. An operation's amortized cost is its actual "
             "cost plus the change in Φ. If Φ starts at 0 and never goes negative, the amortized "
             "total bounds the actual total."),
        ],
        "read_title": "Three methods on two examples, then the table",
        "read_intro": (
            "Read Chapter 17, sections 17.1 to 17.4, in your own copy first. The lesson sets out "
            "each method in its own words on the counter and the stack, works both by hand, and "
            "then lets the lab price a dynamic table one operation at a time."
        ),
        "body": [
            ("p", "Chapter 17 opens by separating its subject from average-case analysis, since no "
                  "probability enters it: &ldquo;an amortized analysis guarantees the average "
                  "performance of each operation in the worst case.&rdquo; Its average is over a "
                  "sequence of operations, "
                  "not over random inputs, and the guarantee holds for every sequence. The authors add a "
                  "practical point. The charges and credits of an analysis are bookkeeping for the "
                  "proof and have no place in the code itself. This lesson reads the "
                  "whole chapter, sections 17.1 to 17.4."),
            ("p", "Section 17.1 is <strong>aggregate analysis</strong>: show that n operations "
                  "cost at most `T(n)` in total, and charge each `T(n)/n`. The first example is a "
                  "stack with PUSH and POP, cost 1 each, and MULTIPOP(S, k), which pops "
                  "`min(s, k)` objects from a stack of s and costs that much. A single MULTIPOP "
                  "can cost `O(n)`, so a careless bound on n operations is `O(n²)`. But an object "
                  "can be popped at most once for each time it was pushed, so all the pops "
                  "together, inside MULTIPOP or not, number at most the pushes, at most n: the "
                  "sequence costs `O(n)`, and each operation `O(1)` amortized."),
            ("p", "The second example is a k-bit binary counter with INCREMENT, whose cost is the "
                  "number of bits it flips. One increment can flip all k bits, so n increments "
                  "cost `O(nk)` by the careless bound. Counted bit by bit, bit 0 flips every time, "
                  "bit 1 every second time, and bit i `⌊n/2ⁱ⌋` times in n increments from zero, so "
                  "the total is less than `n·(1 + 1/2 + 1/4 + ⋯) = 2n`."),
            ("p", "Section 17.2 is the <strong>accounting method</strong>. Charge each "
                  "operation an amortized cost; when it exceeds the actual cost, leave the "
                  "difference as credit on objects in the structure, and let later operations "
                  "spend it. The one rule is that total credit never goes negative, for every "
                  "sequence. For the stack, charge 2 for a push, 1 to pay for it and 1 left on the "
                  "pushed object, and nothing for POP or MULTIPOP, which pay with the credit on "
                  "the objects they remove. For the counter, charge 2 to set a bit to 1 and leave "
                  "a dollar on that bit; resetting it is paid by the dollar. INCREMENT sets at "
                  "most one bit, so its amortized cost is at most 2."),
            ("thm", ("The potential method",
                     "Let `Dᵢ` be the structure after the i-th operation, `cᵢ` that operation's "
                     "actual cost and Φ a potential function. The amortized cost is "
                     "`ĉᵢ = cᵢ + Φ(Dᵢ) − Φ(Dᵢ₋₁)`, and the amortized costs of n operations sum to "
                     "the actual costs plus `Φ(Dₙ) − Φ(D₀)`, since the middle terms telescope. If "
                     "`Φ(Dᵢ) ≥ Φ(D₀)` for every i, the amortized total bounds the actual total.")),
            ("p", "Section 17.3 applies it twice. For the stack, let Φ be the number of objects: "
                  "a push raises it by 1, amortized cost 2; a MULTIPOP of `k′` objects lowers it "
                  "by `k′`, amortized cost 0. For the counter, let Φ be the number of 1 bits: an "
                  "increment that resets `tᵢ` bits costs at most `tᵢ + 1` and changes Φ by at most "
                  "`1 − tᵢ`, so it costs at most 2. The potential method also handles a counter "
                  "that does not start at zero: with `b₀` ones at the start and `bₙ` at the end, "
                  "the actual total is at most `2n − bₙ + b₀`, which is `O(n)` once `n` is `Ω(k)`."),
            ("p", "Here are both examples worked by hand. A 4-bit counter incremented 10 times "
                  "from zero, and a stack given a short sequence of this lesson's own."),
            ("math", [
                "counter, 10 increments from 0000:",
                "  bit 0 flips 10, bit 1 flips 5, bit 2 flips 2, bit 3 flips 1",
                "  actual 18 < 2·10 = 20;   Φ₀ = 0,  Φ₁₀ = ones in 1010 = 2",
                "  amortized total 18 + 2 − 0 = 20, exactly 2 per increment",
                "",
                "stack: push 3, multipop 2, push 2, pop, multipop 5",
                "  sizes 3, 1, 3, 2, 0;   costs 3, 2, 2, 1, 2;   actual 10",
                "  pushes 5, so aggregate bound 2·5 = 10, met because it ends empty",
                "  Φ = size: amortized 6, 0, 4, 0, 0, total 10",
            ]),
            ("p", "Section 17.4 turns to a table that grows and shrinks. With insertions only, "
                  "the common rule is to double the table when it is full, copying every item; "
                  "the load factor, items over slots, then stays at least ½. The i-th insertion "
                  "costs i when `i − 1` is a power of 2 and 1 otherwise, and n insertions cost "
                  "less than `n + 2n = 3n` by aggregate analysis. The accounting version charges "
                  "3: one to insert the item, one to move it at the next expansion, and one to "
                  "move an item that has already moved once. The potential version uses "
                  "`Φ = 2·num − size`, which is 0 just after an expansion and equals num just "
                  "before one, exactly enough to pay for the copying; every insertion then has "
                  "amortized cost 3."),
            ("p", "Deletions bring a trap. Halving the table whenever it falls below half full "
                  "keeps the load factor at least ½ but lets a sequence of insert, delete, delete, "
                  "insert, insert at the boundary expand and contract again and again, each time "
                  "copying `Θ(n)` items, `Θ(n)` amortized per operation. The authors' remedy is to "
                  "halve only when the table falls below a quarter full, and to use a potential "
                  "that is 0 at load factor ½ and grows toward both ends: `2·num − size` at load "
                  "factor ½ or more, `size/2 − num` below ½ (equation 17.6). It reaches num both "
                  "when the table is full and when it is a quarter full, so either resize is "
                  "prepaid. An insertion then costs at most 3 amortized and a deletion at most 2 "
                  "in the cases the section works, the remaining case being Exercise 17.4-2."),
            ("p", "Now the lab, which runs the table with doubling when full and halving when a "
                  "deletion leaves it under a quarter full, freeing it when empty, and prints the "
                  "actual total, the bound of 3 an insertion and 2 a deletion, Φ at the start and "
                  "end, the amortized total and the largest amortized cost of each kind, the "
                  "amortized total less the actual, the final count, size and load factor, and "
                  "the expansions, contractions and items moved. Its table lists each operation "
                  "with its actual cost, Φ after it and its amortized cost."),
            ("p", "The preset <code>boundary</code> is the trap above, played against the "
                  "quarter rule: eight insertions fill a table of 8, a ninth expands it, and then "
                  "two deletions and two insertions take turns, ending on one insertion. "
                  "Twenty operations cost 35 in all, against a bound of 54; Φ ends where it "
                  "started, at 0; there are 4 expansions and no contraction. Played by hand under "
                  "the half rule, the same sequence costs 72, because every round of delete, "
                  "delete, insert, insert after the first expansion costs `1 + 8 + 1 + 9 = 19` "
                  "instead of 4, and the closing delete, delete, insert costs 10 instead of 3. With "
                  "the nine opening insertions at 24 under either rule, that is "
                  "`24 + 19 + 19 + 10 = 72`. <code>grow</code> makes 33 insertions: actual 96, bound 99, "
                  "amortized 98 because Φ ends at 2, with 6 expansions moving 63 items. "
                  "<code>fill-and-empty</code> inserts 16 items and deletes them all: actual 51 "
                  "against a bound of 80, with two contractions on the way down and the table "
                  "freed at the end."),
            ("p", "Every one of these counts sits under its bound, and the lab prints the "
                  "largest amortized cost of any single insertion as 3 and of any deletion as 2. "
                  "Those maxima are about the sequences typed. That no sequence can do worse is "
                  "the case analysis of Section 17.4, which the lab runs one case at a time and "
                  "cannot run for all."),
            ("h3", "Exercise"),
            ("p", "A 3-bit counter starts at 6 (110) and is incremented 5 times, wrapping past 7 "
                  "to 0. Count the bits flipped by each increment, the total, `b₀` and `b₅`, and "
                  "check the total against `2n − bₙ + b₀`. Then explain why the bound needs the "
                  "term `b₀` at all."),
            ("p", "This lesson ends Part IV. The next course, Advanced Data Structures, puts the "
                  "potential method to work at once: Fibonacci heaps are designed around a "
                  "potential function, and disjoint sets are priced first by an aggregate count "
                  "and then, in a starred section, by a potential."),
        ],
        "lab": ("itakit", {
            "mode": "amortized",
            "view": "table",
            "preset": "boundary",
            "presets": [
                {"id": "boundary",
                 "label": "Fill a table of 8, then insert and delete at the boundary",
                 "ops": "insert 8, insert, delete 2, insert 2, delete 2, insert 2, delete 2, "
                        "insert",
                 "expect": {"amiActual": "35", "amiBound": "3 × 14 + 2 × 6 = 54",
                            "amiPhi": "Φ0 = 0, Φn = 0", "amiMax": "insert 3, delete 2",
                            "amiResize": "expansions 4, contractions 0, items moved 15"}},
                {"id": "grow",
                 "label": "Thirty-three insertions",
                 "ops": "insert 33",
                 "expect": {"amiActual": "96", "amiBound": "3 × 33 + 2 × 0 = 99", "amiPhi": "Φ0 = 0, Φn = 2",
                            "amiAmortized": "98",
                            "amiResize": "expansions 6, contractions 0, items moved 63"}},
                {"id": "fill-and-empty",
                 "label": "Sixteen insertions, then sixteen deletions",
                 "ops": "insert 16, delete 16",
                 "expect": {"amiActual": "51", "amiBound": "3 × 16 + 2 × 16 = 80",
                            "amiSize": "num 0, size 0",
                            "amiResize": "expansions 4, contractions 2, items moved 19"}},
            ],
            "panel_title": "Price a dynamic table one operation at a time",
            "panel_intro": (
                "Type insert and delete, each optionally followed by a count. The table doubles "
                "when full and halves when a deletion leaves it under a quarter full. The lab "
                "prints each operation's actual cost, the potential of equation 17.6 after it, "
                "and its amortized cost, with the totals and the bound beside them."
            ),
        }),
        "steps_title": "Running the three methods by hand",
        "steps_intro": "Four steps on one sequence; the fifth is a sequence of your own.",
        "steps": [
            ("Write the actual cost of each operation",
             "For each operation in the sequence, write what it actually costs: bits flipped, "
             "objects popped, items inserted and moved."),
            ("Bound the total by aggregate counting",
             "Find a reason the total is small: each object popped at most once per push, each "
             "bit flipping half as often as the one below, each item moved a bounded number of "
             "times. Divide by n."),
            ("Charge and keep the books",
             "Assign each kind of operation an amortized charge, place the surplus as credit on "
             "objects, and check after every operation that no credit is negative."),
            ("Choose Φ and check it",
             "Write a potential that is 0 at the start and never negative, compute "
             "`cᵢ + Φᵢ − Φᵢ₋₁` for each operation, and confirm the amortized total is the actual "
             "total plus `Φₙ − Φ₀`."),
            ("Do it on a sequence of your own",
             "Write a sequence of 15 to 30 table insertions and deletions, compute each "
             "operation's actual cost and Φ by hand, then type it into the lab and compare your "
             "totals with its actual and amortized totals."),
        ],
        "worked": {
            "title": "The first five insertions into an empty table",
            "intro": [
                "Doubling when full, starting from size 0. The first insertion allocates one "
                "slot. Φ is `2·num − size`, since the load factor stays at least ½.",
            ],
            "lines": [
                "1: size 1, cost 1, Φ 1, amortized 2",
                "2: full → size 2, cost 2, Φ 2, amortized 3",
                "3: full → size 4, cost 3, Φ 2, amortized 3",
                "4: room, cost 1, Φ 4, amortized 3",
                "5: full → size 8, cost 5, Φ 2, amortized 3",
                "actual 12, amortized 14 = 12 + Φ₅ − Φ₀",
            ],
            "after": [
                "Every insertion after the first costs exactly 3 amortized, whether it copies or "
                "not; the first costs 2 because there was nothing to copy. The potential rises by "
                "2 on each cheap insertion and is spent all at once on the expansion.",
            ],
        },
        "quiz_title": "Sequences, credits and potentials",
        "quiz": [
            {"q": "How does an amortized bound differ from an average-case bound?",
             "a": ["It averages over random inputs drawn from a distribution",
                   "It holds for every single operation separately",
                   "It bounds the total of every sequence of operations, with no probability "
                   "involved",
                   "It is the best case of a sequence divided by its length"],
             "c": 2,
             "why": "The amortized cost is a worst-case total over any sequence, divided out over "
                    "its operations, and the authors stress that probability plays no part. "
                    "Averaging over random inputs is average-case analysis. A single operation "
                    "can exceed its amortized cost, and best cases bound nothing."},
            {"q": "A 4-bit counter is incremented 10 times from zero. How many bit flips are "
                  "made in all?",
             "a": ["18", "20", "40", "10"],
             "c": 0,
             "why": "Bit 0 flips 10 times, bit 1 five, bit 2 twice and bit 3 once: 18. Twenty is "
                    "the bound `2n`, forty the careless bound `n·k`, and ten counts only bit 0."},
            {"q": "Under the potential `Φ = 2·num − size`, what is the amortized cost of an "
                  "insertion that triggers an expansion from 8 slots to 16?",
             "a": ["9", "3", "1", "−5"],
             "c": 1,
             "why": "The actual cost is 9, 8 items moved and 1 inserted. Before, `num = size = 8`, "
                    "so Φ = 8; after, `num = 9` and `size = 16`, so Φ = 2. The amortized cost is "
                    "`9 + 2 − 8 = 3`. Nine forgets the potential, 1 is an insertion with room, and "
                    "−5 is `1 + 2 − 8`, which keeps the drop in Φ but forgets the 8 items moved."},
            {"q": "Why does halving a table when it falls below half full make the amortized "
                  "cost large?",
             "a": ["Because a contraction costs more than an expansion",
                   "Because the load factor can then drop below ½",
                   "Because a short alternation of insertions and deletions at the boundary can "
                   "expand and contract again and again, each time copying Θ(n) items",
                   "Because Φ becomes negative after a contraction"],
             "c": 2,
             "why": "Just after an expansion the table is half full, and two deletions then "
                    "trigger a contraction, two insertions an expansion, and so on, with no cheap "
                    "operations between to pay for them. A contraction costs about what an "
                    "expansion does, the half rule keeps the load factor at least ½, and the "
                    "trouble is not Φ but the absence of any Φ that could prepay both."},
        ],
        "mistakes": [
            ("Reading amortized cost as average-case cost",
             "Nothing is random. An amortized bound says every sequence of n operations costs at "
             "most so much, so it is a worst-case statement about sequences. Average-case "
             "analysis assumes a distribution over inputs and bounds an expectation."),
            ("Thinking a cheap amortized cost means every operation is cheap",
             "An expansion of a full table of 32 items costs 33, and its amortized cost is 3. "
             "The bound is on the total: in the lab's <code>grow</code> preset 33 insertions cost "
             "96 though one of them alone cost 33. A program that cannot tolerate one slow "
             "operation needs a worst-case bound per operation."),
            ("Letting the credit or the potential go negative",
             "Charges that undercharge early and promise to repay later do not bound the actual "
             "cost of the prefix that stops before repayment. The accounting method requires "
             "non-negative credit at all times, and the potential method `Φ(Dᵢ) ≥ Φ(D₀)` for "
             "every i, not only at the end of the sequence."),
        ],
        "standard": (
            "Finish when you can bound a sequence three ways.",
            "Given a short sequence of counter, stack or table operations, compute the actual "
            "total, an aggregate bound, a valid set of accounting charges, and every operation's "
            "amortized cost under a stated potential."
        ),
        "note": (
            "The lab runs one table policy, doubling when full and halving below a quarter, so "
            "the half rule's thrashing is worked by hand; its counter and stack views exist but "
            "this lesson uses the table. Its maxima describe the sequence typed. The constant "
            "bounds hold for every sequence by the section's case analysis."
        ),
    },
]
