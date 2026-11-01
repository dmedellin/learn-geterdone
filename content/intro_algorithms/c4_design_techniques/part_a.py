"""Advanced Design and Analysis Techniques, lessons 1-5 -- Chapter 15.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed.
(MIT Press, 2009): Chapter 15, Dynamic Programming (pp. 359-413), one lesson
per section. Every quotation is copied from the operator's copy with its
printed page in the comment beside the lesson. The prices, dimensions,
coins, strings and probabilities are written for these lessons: none of the
book's figures, examples or exercises is reproduced, and its procedures are
described in prose and named.
"""

# The rod lesson's price list, lengths 1 to 8 (and 9 and 10 in later presets).
ROD_EIGHT = "1 4 8 9 14 15 19 21"

LESSONS = [
    # ---------------------------------------------------------------- 01
    # CLRS Chapter 15 opening and section 15.1, pp. 359-370.
    # Quote: p. 359, 30 words, quotes.py OK. Lesson total: 30 words.
    # DP against divide-and-conquer, optimization problems, the four steps
    # (p. 359); the rod-cutting problem, 2^(n-1) decompositions, equations
    # 15.1 and 15.2, optimal substructure (pp. 360-363); CUT-ROD and
    # T(n) = 2^n (pp. 363-364); memoized and bottom-up versions, Theta(n^2)
    # by an arithmetic series (pp. 364-367); subproblem graphs (pp. 367-368);
    # EXTENDED-BOTTOM-UP-CUT-ROD and PRINT-CUT-ROD-SOLUTION (pp. 368-369).
    {
        "slug": "rod-cutting",
        "title": "Rod Cutting and Dynamic Programming",
        "module": "Chapter 15 · Dynamic Programming",
        "one_line": "A rod of length n can be cut in 2ⁿ⁻¹ ways and a plain recursion visits every one, but there are only n + 1 distinct subproblems, and solving each once turns exponential work into a table of n·(n + 1)/2 steps.",
        "summary": (
            "The opening of Chapter 15 sets dynamic programming beside divide-and-conquer: both "
            "combine solutions to subproblems, but dynamic programming applies when those "
            "subproblems overlap, and it solves each one once. Section 15.1 shows the method on "
            "rod cutting: the recurrence for the best revenue, a plain recursion that makes 2ⁿ "
            "calls, a memoized version and a bottom-up version that each take Θ(n²), the "
            "subproblem graph, and the extra array that recovers the cuts. Fill the table for an "
            "eight-inch rod by hand, then let the lab count the three routes."
        ),
        "key": [
            "a rod of length n has 2ⁿ⁻¹ cuttings",
            "r(n): best first piece plus best rest",
            "plain recursion: 2ⁿ calls",
            "each subproblem solved once: Θ(n²)",
            "memoized and bottom-up: same answer",
            "s(j) records the first piece to cut",
        ],
        "key_label": "Section 15.1 in six lines",
        "concepts_intro": (
            "Three ideas carry the section, and the rest of the chapter reuses all three."
        ),
        "concepts": [
            ("Overlapping subproblems",
             "A recursion has overlapping subproblems when it asks the same smaller question many "
             "times over. Rod cutting asks for the best revenue from a rod of length j for every "
             "j below n, again and again in different branches. Divide-and-conquer, by contrast, "
             "usually splits into pieces that never recur."),
            ("Memoized and bottom-up",
             "Two ways to solve each subproblem once. Top-down with memoization keeps the "
             "recursion and stores each answer the first time it is computed. Bottom-up orders "
             "the subproblems by size and solves the smallest first, so that every answer a step "
             "needs is already in the table. The two have the same asymptotic running time."),
            ("The subproblem graph",
             "One vertex per distinct subproblem and an arc from each subproblem to every "
             "subproblem it consults directly. It is the recursion tree with repeated nodes "
             "merged. Its size estimates the running time, and bottom-up order is a reverse "
             "topological order of it."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the opening of Chapter 15 and Section 15.1 in your own copy first. The lesson "
            "sets out the argument in its own words, fills one revenue table by hand, and then "
            "sets the three routes' call counts side by side."
        ),
        "body": [
            ("p", "&ldquo;A dynamic-programming algorithm solves each subsubproblem just once and "
                  "then saves its answer in a table, thereby avoiding the work of recomputing the "
                  "answer every time it solves each subsubproblem.&rdquo; That sentence, from the "
                  "first paragraph of Chapter 15, is the whole method; the authors add at once "
                  "that the word programming here means a tabular method, not writing code. This "
                  "lesson reads the chapter's opening and Section 15.1, the first of its five "
                  "examples."),
            ("p", "The opening sets the method beside divide-and-conquer. Both solve a problem by "
                  "combining solutions to subproblems. Divide-and-conquer splits into disjoint "
                  "pieces; dynamic programming applies when the subproblems overlap, so that "
                  "subproblems share subsubproblems, and it saves each answer in a table so that "
                  "no subsubproblem is solved twice. The usual targets are optimization problems, "
                  "where many solutions exist and one with the best value is wanted, and the "
                  "authors note the article: <em>an</em> optimal solution, since several may tie. "
                  "They give four steps: characterize the structure of an optimal solution, "
                  "define its value recursively, compute that value, usually bottom-up, and "
                  "construct a solution from what was computed. The fourth is optional when only "
                  "the value is wanted."),
            ("def", ("The rod-cutting problem",
                     "Given a rod of n inches and a price `pᵢ` for a piece of length i, for i "
                     "from 1 to n, find the largest revenue `rₙ` obtainable by cutting the rod "
                     "into pieces of whole-inch lengths and selling them. Cuts cost nothing, and "
                     "selling the rod whole is allowed.")),
            ("p", "There are `2ⁿ⁻¹` ways to cut the rod, because at each of the `n − 1` inch "
                  "marks you independently cut or do not. The authors first write the best "
                  "revenue as the larger of selling whole and every split into two pieces, each "
                  "then cut optimally; that the best solution is built from best solutions to "
                  "the two pieces is what they call <strong>optimal substructure</strong>. They "
                  "then simplify: view every cutting as a first piece of length i taken from "
                  "the left, which is sold as it is, and a remainder of length `n − i`, which "
                  "may be cut further. Then `rₙ` is the largest of `pᵢ + rₙ₋ᵢ` over i from 1 "
                  "to n, with `r₀ = 0`, and only one subproblem, the remainder, is consulted per "
                  "choice."),
            ("thm", ("The plain recursion makes 2ⁿ calls",
                     "CUT-ROD computes the recurrence directly: for each first piece i it calls "
                     "itself on `n − i`. If `T(n)` counts the calls made on a rod of length n, "
                     "including the first, then `T(0) = 1` and `T(n) = 1 + T(0) + T(1) + ⋯ + "
                     "T(n − 1)`, which solves to `T(n) = 2ⁿ` (Exercise 15.1-1). The recursion "
                     "tree has one leaf for each of the `2ⁿ⁻¹` cuttings.")),
            ("p", "The authors describe what that means in practice: at n = 40 the program runs "
                  "for minutes, likely more than an hour, and each extra inch roughly doubles the "
                  "time. The waste is plain in the recursion tree: a call on length j calls every "
                  "shorter length, so the length-1 subproblem alone is solved `2ⁿ⁻²` times. Yet "
                  "there are only `n + 1` distinct subproblems, the lengths 0 to n. Dynamic "
                  "programming trades memory for time: solve each length once, store it, and "
                  "look it up afterwards."),
            ("p", "Section 15.1 gives both ways of doing that. MEMOIZED-CUT-ROD keeps CUT-ROD's "
                  "shape but first checks an array of answers, initialised to a value meaning "
                  "unknown, and records each answer before returning it. BOTTOM-UP-CUT-ROD drops "
                  "the recursion: it fills `r[0..n]` in increasing order of length, so that "
                  "`r[j − i]` is always ready when `r[j]` needs it. Solving length j tries j "
                  "first pieces, so both versions do `1 + 2 + ⋯ + n = n·(n + 1)/2` iterations "
                  "of the inner step, an arithmetic series, and both run in `Θ(n²)`. The "
                  "bottom-up version usually has the better constant, with no calls to pay for; "
                  "the memoized one wins only when some subproblems need never be solved."),
            ("p", "The <strong>subproblem graph</strong> makes the count general. For rod cutting "
                  "it has a vertex for each length 0 to n and an arc from j to every shorter "
                  "length, `n·(n + 1)/2` arcs in all. The bottom-up method visits the vertices "
                  "in reverse topological order, so that every vertex comes after all the "
                  "vertices it points to, and the memoized method is a depth-first search of the "
                  "graph (Chapter 22's terms). When the work at a subproblem is proportional to "
                  "its out-degree, as here, the running time is linear in the graph's vertices "
                  "and arcs."),
            ("p", "The last step recovers the cutting itself. EXTENDED-BOTTOM-UP-CUT-ROD stores, "
                  "beside each `r[j]`, the size `s[j]` of the first piece that achieved it, "
                  "keeping the first i that wins because its comparison is strict. "
                  "PRINT-CUT-ROD-SOLUTION then prints `s[n]`, moves to `n − s[n]`, and repeats "
                  "until nothing is left. Here is the whole table for this lesson's price list, "
                  "eight lengths with prices `1 4 8 9 14 15 19 21`."),
            ("math", [
                "j        1   2   3   4   5   6   7   8",
                "p(j)     1   4   8   9  14  15  19  21",
                "r(j)     1   4   8   9  14  16  19  22",
                "s(j)     1   2   3   1   5   3   7   3",
                "",
                "cut 8:  s(8) = 3, then s(5) = 5      revenue 8 + 14 = 22",
            ]),
            ("p", "Two rows reward a second look. At j = 6 two 3-inch pieces earn 16 against 15 "
                  "for the whole rod, so `s(6) = 3`. At j = 7 the whole rod at 19 beats every "
                  "split, so `s(7) = 7`. And the best cutting of the 8-inch rod contains the best "
                  "cutting of its 5-inch remainder, which is optimal substructure in one line of "
                  "the table."),
            ("p", "Now the lab. It runs EXTENDED-BOTTOM-UP-CUT-ROD on the prices you type and "
                  "prints the best revenue, the pieces PRINT-CUT-ROD-SOLUTION would print, the "
                  "calls CUT-ROD would make (computed from `T(n) = 2ⁿ`, never run), the number of "
                  "cuttings, the calls MEMOIZED-CUT-ROD-AUX makes, counted as it runs with the "
                  "first call included, and the inner-loop runs of the bottom-up version. Ties "
                  "keep the smallest first piece, as the book's strict comparison does."),
            ("p", "The preset <code>eight-inch</code> is the table above: revenue 22, pieces "
                  "3 + 5, 256 calls for the plain recursion against 37 for the memoized one, "
                  "128 cuttings and 36 inner-loop runs. The memoized count is the 36 recursive "
                  "calls of the inner loop plus the first. <code>ten-inch</code> adds prices 24 "
                  "and 27: revenue 28 from 5 + 5, and 1,024 calls against 56. "
                  "<code>whole-is-best</code> prices six lengths at `1 3 6 10 15 21`, where every "
                  "cut loses money, and the lab prints 6 (no cut). <code>twenty-inch</code> "
                  "prices twenty lengths at the odd numbers 1 to 39, so each cut costs a dollar: "
                  "1,048,576 calls for the plain recursion, 211 memoized, 210 bottom-up."),
            ("p", "Those last figures are the whole chapter in two numbers, and the honest "
                  "reading of them is narrow. The 211 is a count on one price list. The `Θ(n²)` "
                  "bound holds for every price list, because the arithmetic series does not "
                  "depend on the prices at all; the proof says so, and the count only agrees."),
            ("h3", "Exercise"),
            ("p", "Append a price of 24 for a 9-inch piece to the lesson's list. Compute `r(9)` "
                  "by hand from the table above, list every first piece that achieves it, and "
                  "say which cutting the lab will print and why. Then type the nine prices into "
                  "the lab and check."),
            ("p", "Rod cutting chooses a first piece and leaves one subproblem. The next lesson, "
                  "Matrix-Chain Multiplication, chooses a split and leaves two, and its table has "
                  "a fill order that matters."),
        ],
        "lab": ("itakit", {
            "mode": "rod",
            "view": "cut",
            "preset": "eight-inch",
            "presets": [
                {"id": "eight-inch",
                 "label": "The lesson's price list, eight lengths",
                 "prices": ROD_EIGHT,
                 "expect": {"rdiRevenue": "22", "rdiCuts": "3 + 5", "rdiNaive": "256",
                            "rdiWays": "128", "rdiMemo": "37", "rdiInner": "36"}},
                {"id": "ten-inch",
                 "label": "The same list with prices for 9 and 10 inches",
                 "prices": ROD_EIGHT + " 24 27",
                 "expect": {"rdiRevenue": "28", "rdiCuts": "5 + 5", "rdiNaive": "1,024",
                            "rdiMemo": "56"}},
                {"id": "whole-is-best",
                 "label": "Six lengths priced 1 3 6 10 15 21",
                 "prices": "1 3 6 10 15 21",
                 "expect": {"rdiRevenue": "21", "rdiCuts": "6 (no cut)"}},
                {"id": "twenty-inch",
                 "label": "Twenty lengths priced at the odd numbers 1 to 39",
                 "prices": " ".join(str(2 * i - 1) for i in range(1, 21)),
                 "expect": {"rdiRevenue": "39", "rdiCuts": "20 (no cut)", "rdiNaive": "1,048,576",
                            "rdiMemo": "211", "rdiInner": "210"}},
            ],
            "panel_title": "One recurrence, three ways to evaluate it",
            "panel_intro": (
                "Type a price for each length from 1 inch up. The lab fills the revenue table "
                "bottom-up, recovers the pieces, and sets the calls of the plain recursion "
                "beside the memoized and bottom-up counts. The answer is the same three ways; "
                "the work is not."
            ),
        }),
        "steps_title": "Filling a revenue table by hand",
        "steps_intro": "Four steps fill the table; the fifth uses prices of your own.",
        "steps": [
            ("Write the prices in a row",
             "Lengths 1 to n across the top, `pⱼ` beneath, and an empty row each for `r(j)` "
             "and `s(j)`. Set `r(0) = 0` to the left."),
            ("Fill r(j) from left to right",
             "For each j, add `pᵢ + r(j − i)` for every first piece i from 1 to j, and write the "
             "largest. Every `r(j − i)` you need is already to the left: that is the bottom-up "
             "order."),
            ("Record the first piece that won",
             "Write the smallest i that achieves the maximum as `s(j)`. Ties go to the smaller "
             "piece, as the book's strict comparison does."),
            ("Read off the cutting",
             "From n, write `s(n)`, move to `n − s(n)`, and repeat until you reach 0. Add the "
             "prices of the pieces and check that they make `r(n)`."),
            ("Do it on a price list of your own",
             "Write prices for lengths 1 to 7, fill the table by hand, then type them into the "
             "lab: its revenue and pieces must match yours, its memoized count must be 29 and "
             "its bottom-up count 28."),
        ],
        "worked": {
            "title": "The first six lengths of the lesson's list",
            "intro": [
                "Prices `1 4 8 9 14 15` for lengths 1 to 6. Each line tries every first piece "
                "and keeps the largest total, the smallest piece on a tie.",
            ],
            "lines": [
                "r(1) = 1 + r(0) = 1;  s = 1",
                "r(2) = max(1 + 1, 4 + 0) = 4;  s = 2",
                "r(3) = max(1 + 4, 4 + 1, 8) = 8;  s = 3",
                "r(4) = max(1 + 8, 4 + 4, 8 + 1, 9) = 9;  s = 1",
                "r(5) = max(10, 12, 12, 10, 14) = 14;  s = 5",
                "r(6) = max(15, 13, 16, 13, 15, 15) = 16;  s = 3",
                "21 trials of a first piece in all",
            ],
            "after": [
                "At j = 4 the total 9 is reached three ways, 1 + 3, 3 + 1 and the whole rod; the "
                "smallest first piece is kept, so `s(4) = 1`. Twenty-one trials is `6·7/2`, the "
                "arithmetic series the bound counts.",
            ],
        },
        "quiz_title": "Rod cutting and its three routes",
        "quiz": [
            {"q": "On the lesson's eight prices, how many calls does CUT-ROD make, and how many "
                  "does MEMOIZED-CUT-ROD-AUX make, counting the first call of each?",
             "a": ["128 and 36",
                   "256 and 37",
                   "256 and 9",
                   "40,320 and 37"],
             "c": 1,
             "why": "CUT-ROD makes `T(8) = 2⁸ = 256` calls. The memoized version makes the first "
                    "call and then, once per length j from 1 to 8, j recursive calls: "
                    "`1 + 36 = 37`. 128 is the number of cuttings, `2⁷`, and 36 the bottom-up "
                    "inner-loop count. Nine is the number of distinct subproblems, lengths 0 to "
                    "8, not the number of calls. 40,320 is 8!, which counts nothing here."},
            {"q": "In the lesson's table, why is `s(6) = 3` when a 6-inch piece sells for 15?",
             "a": ["The first piece is always the most valuable piece per inch",
                   "A first piece of 3 and a remainder of 3 is the only cutting that ties with 15",
                   "Two 3-inch pieces earn `8 + 8 = 16`, more than the whole rod's 15",
                   "`s(j)` is half of j whenever j is even"],
             "c": 2,
             "why": "The trial with first piece 3 gives `p₃ + r(3) = 8 + 8 = 16`, the largest of "
                    "the six. Value per inch does not decide it: the 5-inch piece is worth 2.8 "
                    "an inch and the 3-inch piece about 2.67, yet 3 wins. Nothing ties with 16. "
                    "And `s(4) = 1` already shows an even length whose first piece is not half."},
            {"q": "Why do BOTTOM-UP-CUT-ROD and MEMOIZED-CUT-ROD both run in `Θ(n²)`?",
             "a": ["Each solves every length 0 to n once, and solving length j tries j first pieces, so the work is the arithmetic series `n·(n + 1)/2`",
                   "Each solves every length once, so the work is linear, and the square comes from sorting the prices",
                   "The recursion tree has n levels and n nodes per level",
                   "Memoization halves the `2ⁿ` calls n times"],
             "c": 0,
             "why": "Both store each length's answer, so each length is solved once, and the "
                    "inner loop for length j runs j times; the sum is `n·(n + 1)/2`. Solving "
                    "each subproblem once is linear in the number of subproblems only when each "
                    "costs a constant, which these do not, and nothing is sorted. The plain "
                    "recursion tree has `2ⁿ` nodes, not n per level, and halving `2ⁿ` n times "
                    "gives 1, not a count of work."},
            {"q": "How many vertices and arcs does the subproblem graph of rod cutting have for "
                  "a rod of length n?",
             "a": ["`2ⁿ` vertices and `2ⁿ − 1` arcs",
                   "n vertices and `n − 1` arcs",
                   "`n + 1` vertices and n arcs",
                   "`n + 1` vertices and `n·(n + 1)/2` arcs"],
             "c": 3,
             "why": "One vertex per length 0 to n, and an arc from each length j to each of the "
                    "j shorter lengths it consults, so `1 + 2 + ⋯ + n` arcs. `2ⁿ` nodes "
                    "describes the recursion tree before repeated subproblems are merged. A path "
                    "of n arcs would mean each length consults only the next shorter one, which "
                    "is not the recurrence."},
        ],
        "mistakes": [
            ("Thinking the table changes the recurrence",
             "Memoization and bottom-up order change how often each subproblem is solved, never "
             "what is computed: all three routes evaluate the same recurrence and return the "
             "same revenue. On the lesson's twenty-inch preset the plain recursion would make "
             "1,048,576 calls and the memoized one 211, and the lab's revenue is the same 39 by "
             "every route. The exponential cost was repetition, not a harder computation."),
            ("Counting calls when you mean subproblems",
             "`2ⁿ` is the number of calls the plain recursion makes; the number of distinct "
             "subproblems is `n + 1`. The running time of a dynamic program is set by the second "
             "number and the work per subproblem, here `Θ(n²)` in all. Mixing the two hides "
             "exactly the overlap the method exploits."),
            ("Reading s(n) as the whole answer",
             "`s(n)` is only the first piece of an optimal cutting. The rest comes from the "
             "remainder's entry, `s(n − s(n))`, and so on to zero. In the lesson's table "
             "`s(8) = 3`, and the cutting is 3 + 5 only because `s(5) = 5`."),
        ],
        "standard": (
            "Finish when you can fill and read a revenue table by hand.",
            "Given prices for six to eight lengths, fill `r(j)` and `s(j)`, recover an optimal "
            "cutting, and state how many calls the plain, memoized and bottom-up methods make."
        ),
        "note": (
            "The lab counts the memoized and bottom-up routes as they run but computes the plain "
            "recursion's calls from `T(n) = 2ⁿ` rather than running it, which at twenty inches "
            "would mean a million calls. It reports one optimal cutting, the one the book's "
            "strict comparison keeps; when several tie, the others are found by hand."
        ),
    },
    # ---------------------------------------------------------------- 02
    # CLRS section 15.2, pp. 370-378.
    # Quote: p. 372, 13 words, quotes.py OK. Lesson total: 13 words.
    # Fully parenthesized products, the pqr cost, the 10-to-1 example named
    # (pp. 370-371); counting parenthesizations, recurrence 15.6, Catalan
    # numbers, Omega(2^n) (p. 372); steps 1-4: optimal substructure by
    # cut-and-paste, recurrence 15.7 and s[i, j], MATRIX-CHAIN-ORDER by chain
    # length, O(n^3) time and Theta(n^2) space, PRINT-OPTIMAL-PARENS
    # (pp. 373-377).
    {
        "slug": "matrix-chain-multiplication",
        "title": "Matrix-Chain Multiplication",
        "module": "Chapter 15 · Dynamic Programming",
        "one_line": "The order in which a chain of matrices is multiplied can change the work many times over, the number of orders grows like the Catalan numbers, and a table filled by chain length finds the cheapest order in O(n³) time.",
        "summary": (
            "Section 15.2 asks how to parenthesize a product of n matrices so that the fewest "
            "scalar multiplications are performed. Trying every parenthesization is exponential, "
            "since their number is a Catalan number. The four steps give the recurrence for "
            "m[i, j], the cheapest cost of the subchain from i to j, a bottom-up fill by "
            "increasing chain length, and a table s[i, j] of best splits that prints the "
            "parenthesization. Fill a four-matrix table by hand, then let the lab fill a five-"
            "matrix one in two orders and check it against every bracketing."
        ),
        "key": [
            "a product p×q by q×r costs p·q·r",
            "bracketings of n matrices: Catalan(n − 1)",
            "m[i, j]: cheapest cost of Aᵢ to Aⱼ",
            "try every split k from i to j − 1",
            "fill by chain length, shortest first",
            "s[i, j] records the best split",
        ],
        "key_label": "Section 15.2 in six lines",
        "concepts_intro": (
            "Three ideas: what is being minimized, how many candidates there are, and how the "
            "table avoids trying them all."
        ),
        "concepts": [
            ("The cost of a product",
             "Multiplying a `p × q` matrix by a `q × r` matrix with the standard method takes "
             "`p·q·r` scalar multiplications, and the result is `p × r`. Matrix multiplication "
             "is associative, so every full parenthesization gives the same product, at "
             "different costs."),
            ("Counting parenthesizations",
             "A full parenthesization of n matrices makes a last multiplication between the "
             "first k and the remaining `n − k`, for some k. So the count obeys "
             "`P(n) = Σ P(k)·P(n − k)` with `P(1) = 1`, whose solutions are the Catalan numbers, "
             "growing as `Ω(4ⁿ/n^(3/2))`: 1, 1, 2, 5, 14, 42, 132 for one to seven matrices."),
            ("The m and s tables",
             "`m[i, j]` is the fewest scalar multiplications that compute the product of "
             "matrices i to j, and `s[i, j]` a split k that achieves it. The m table answers "
             "how much; the s table answers how, and it is what lets the parenthesization be "
             "printed in time proportional to its length."),
        ],
        "read_title": "The section's four steps, then one chain by hand and by lab",
        "read_intro": (
            "Read Section 15.2 in your own copy first. The lesson follows its four steps in its "
            "own words, fills a four-matrix table by hand, and then runs a five-matrix chain in "
            "the lab."
        ),
        "body": [
            ("p", "&ldquo;Note that in the matrix-chain multiplication problem, we are not "
                  "actually multiplying matrices.&rdquo; The authors make the point early in "
                  "Section 15.2: the output is an order of operations, and the time spent finding "
                  "it is meant to be repaid when the multiplications are finally done. This lesson "
                  "reads the section, which is the first full pass through the chapter's four "
                  "steps."),
            ("p", "The section opens with the cost. The standard method multiplies a `p × q` "
                  "matrix by a `q × r` matrix in `p·q·r` scalar multiplications, and the authors "
                  "show with three matrices that one parenthesization can be ten times cheaper "
                  "than the other. The problem is then stated: given the dimensions "
                  "`p₀, p₁, …, pₙ`, where matrix `Aᵢ` is `pᵢ₋₁ × pᵢ`, fully parenthesize "
                  "`A₁A₂⋯Aₙ` to minimize the scalar multiplications."),
            ("p", "Before any table, the authors rule out trying everything. The last "
                  "multiplication splits the chain after some matrix k, and each side is "
                  "parenthesized independently, which gives the recurrence for `P(n)` in the "
                  "concepts above. Its solutions are the Catalan numbers, and a simpler exercise "
                  "(Exercise 15.2-3) shows `P(n)` is `Ω(2ⁿ)`: exhaustive search is exponential."),
            ("p", "Step 1 is the structure. If an optimal parenthesization of `Aᵢ⋯Aⱼ` splits "
                  "after `Aₖ`, then the way it parenthesizes the prefix `Aᵢ⋯Aₖ` must itself be "
                  "optimal for that prefix: if a cheaper one existed, substituting it would "
                  "lower the total, contradicting optimality. The same holds for the suffix. "
                  "This substitution is the cut-and-paste argument the next lesson names, and it "
                  "means an optimal solution can be assembled from optimal solutions to two "
                  "subchains, provided every split is tried."),
            ("thm", ("The recurrence for m[i, j]",
                     "`m[i, i] = 0`, and for `i < j`, `m[i, j]` is the minimum over k from i to "
                     "`j − 1` of `m[i, k] + m[k + 1, j] + pᵢ₋₁·pₖ·pⱼ`. The last term is the cost "
                     "of multiplying the two subproducts, a `pᵢ₋₁ × pₖ` matrix by a `pₖ × pⱼ` "
                     "one. `s[i, j]` is a k that attains the minimum.")),
            ("p", "Step 3 computes the costs bottom-up, and the order is forced by the "
                  "recurrence. `m[i, j]` reads only entries for shorter subchains, `m[i, k]` and "
                  "`m[k + 1, j]`, so MATRIX-CHAIN-ORDER fills the table by chain length: all "
                  "chains of length 2, then length 3, up to the whole chain. There are only "
                  "`Θ(n²)` subproblems, one per pair `i ≤ j`, and a plain recursion would meet "
                  "each many times; that repetition is the second hallmark of dynamic "
                  "programming, after optimal substructure. The three nested loops give `O(n³)` "
                  "time (Exercise 15.2-5 shows `Ω(n³)` too) and the two tables `Θ(n²)` space. "
                  "Step 4 is PRINT-OPTIMAL-PARENS, which reads `s[1, n]` for the last "
                  "multiplication and recurses on the two sides."),
            ("p", "Here is a chain of four matrices with dimensions `3 5 2 6 4`: `A₁` is 3 × 5, "
                  "`A₂` is 5 × 2, `A₃` is 2 × 6 and `A₄` is 6 × 4. The table is filled by "
                  "length, each cell trying every split."),
            ("math", [
                "length 2:  m[1,2] = 3·5·2 = 30     m[2,3] = 5·2·6 = 60     m[3,4] = 2·6·4 = 48",
                "length 3:  m[1,3] = min(0 + 60 + 3·5·6, 30 + 0 + 3·2·6) = min(150, 66) = 66,  s = 2",
                "           m[2,4] = min(0 + 48 + 5·2·4, 60 + 0 + 5·6·4) = min(88, 180) = 88,  s = 2",
                "length 4:  m[1,4] = min(0 + 88 + 60, 30 + 48 + 24, 66 + 0 + 72)",
                "                  = min(148, 102, 138) = 102,  s = 2",
                "",
                "best:  ((A1 A2)(A3 A4)),  102 scalar multiplications",
            ]),
            ("p", "Five parenthesizations exist for four matrices, and the worst of them, "
                  "`(A₁((A₂A₃)A₄))`, costs 240, more than twice the best. Notice that `s[1, 4] = 2` "
                  "puts the last multiplication between the pair on the left and the pair on the "
                  "right, a shape no left-to-right or right-to-left evaluation would find."),
            ("p", "Now the lab. It is the chain lab of the Algorithms Subject's lesson The Fill "
                  "Order Is Part of the Algorithm, where the same table is practised further. It "
                  "fills the m table in the order you choose, by chain length or row by row, "
                  "reconstructs the parenthesization, re-costs it from the dimensions alone, and "
                  "enumerates every bracketing as a check that has no table in it. Its presets "
                  "are the lab's own; <code>square</code>, four matrices all 10 × 10, shows that "
                  "when every dimension is equal each of the 5 bracketings costs the same "
                  "3,000."),
            ("p", "Type the lesson's five-matrix chain, `6 2 10 4 8 3`. Filled by chain length, "
                  "the table's answer is 228, and the lab finds the same minimum among all 14 "
                  "bracketings; the parenthesization is `(A₁(((A₂A₃)A₄)A₅))`, and re-costing it "
                  "from the dimensions gives 228 again. The worst bracketing costs 1,064. Now "
                  "switch the fill to row by row: some cells are read before they are written, "
                  "the lab paints them red, and the table finishes with 36, a number below the "
                  "true minimum that no bracketing achieves. Nothing crashes, which is why the order has to be argued from the "
                  "recurrence and not trusted to look right."),
            ("p", "Fourteen bracketings is a count the enumeration can still afford. At seven "
                  "matrices it is 132, at ten 4,862, and the table's `Θ(n³)` work is what keeps "
                  "growing slowly. The enumeration agreeing at five matrices is evidence that "
                  "this table is right; the cut-and-paste argument is what makes every such "
                  "table right."),
            ("h3", "Exercise"),
            ("p", "Fill the m and s tables by hand for the lesson's five-matrix chain "
                  "`6 2 10 4 8 3`, by chain length. Check `m[1, 5] = 228`, print the "
                  "parenthesization from your s table, and list the cells a row-by-row fill would "
                  "read before writing them."),
            ("p", "Two examples in, the method has a pattern. The next lesson, Elements of "
                  "Dynamic Programming, names its two ingredients and shows a problem that "
                  "looks just like these and lacks one of them."),
        ],
        "lab": ("dpkit", {
            "mode": "chain",
            "preset": "square",
            "panel_title": "Fill the chain table in two orders, and check it against every bracketing",
            "panel_intro": (
                "Type n + 1 dimensions for n matrices. The lab fills the m table in the order "
                "you choose, prints the parenthesization the s choices give and re-costs it, and "
                "sets beside it the cheapest of every bracketing, found with no table at all. "
                "Type the lesson's chain 6 2 10 4 8 3, then switch the fill order."
            ),
        }),
        "steps_title": "Filling a chain table by hand",
        "steps_intro": "Four steps fill the tables; the fifth is a chain of your own.",
        "steps": [
            ("List the dimensions and the diagonal",
             "Write `p₀` to `pₙ` and set `m[i, i] = 0` for every i: a single matrix costs "
             "nothing."),
            ("Fill chains of length 2",
             "`m[i, i + 1] = pᵢ₋₁·pᵢ·pᵢ₊₁`, with only one split to try."),
            ("Fill longer chains, shortest first",
             "For each cell try every split k from i to `j − 1`, add the two shorter cells and "
             "`pᵢ₋₁·pₖ·pⱼ`, keep the smallest total in m and its k in s. Every cell you read is "
             "already filled because it covers a shorter chain."),
            ("Print the parenthesization",
             "Start at `s[1, n]`: the last multiplication splits after that matrix. Recurse on "
             "both sides with their own s entries until each side is one matrix."),
            ("Do it on a chain of your own",
             "Write dimensions for four or five matrices, fill both tables by hand, then type "
             "them into the lab and compare your `m[1, n]` and parenthesization with its "
             "answer and with the cheapest bracketing it enumerates."),
        ],
        "worked": {
            "title": "One cell of the five-matrix chain",
            "intro": [
                "For the chain `6 2 10 4 8 3`, the cell `m[2, 4]` covers `A₂A₃A₄`, matrices "
                "2 × 10, 10 × 4 and 4 × 8. Its two shorter neighbours are already filled: "
                "`m[2, 3] = 80` and `m[3, 4] = 320`.",
            ],
            "lines": [
                "k = 2:  m[2,2] + m[3,4] + p1·p2·p4",
                "      = 0 + 320 + 2·10·8 = 480",
                "k = 3:  m[2,3] + m[4,4] + p1·p3·p4",
                "      = 80 + 0 + 2·4·8 = 144",
                "m[2,4] = 144,  s[2,4] = 3",
            ],
            "after": [
                "Splitting after `A₃` multiplies the small 2 × 4 result by `A₄`, which is why it "
                "wins by more than three to one. The cell reads `m[3, 4]`, a chain of length 2, "
                "and a row-by-row fill reaches row 2 before row 3 is written, so it would read "
                "that cell empty.",
            ],
        },
        "quiz_title": "Chains, splits and the fill order",
        "quiz": [
            {"q": "What does MATRIX-CHAIN-ORDER give for the lesson's four-matrix chain "
                  "`3 5 2 6 4`?",
             "a": ["`m[1, 4] = 138`, with the last multiplication after `A₃`",
                   "`m[1, 4] = 148`, with the last multiplication after `A₁`",
                   "`m[1, 4] = 102`, with the last multiplication after `A₂`",
                   "`m[1, 4] = 240`, the cost of `(A₁((A₂A₃)A₄))`"],
             "c": 2,
             "why": "The three splits cost 148 (after `A₁`), 102 (after `A₂`) and 138 (after "
                    "`A₃`), and the minimum is 102 with `s[1, 4] = 2`, the bracketing "
                    "`((A₁A₂)(A₃A₄))`. 138 and 148 are the other two splits' totals, and 240 is "
                    "the worst of the five bracketings, not the best."},
            {"q": "How many full parenthesizations does a chain of six matrices have?",
             "a": ["42",
                   "14",
                   "720",
                   "32"],
             "c": 0,
             "why": "`P(6)` is the Catalan number for five splits: `P(6) = P(1)P(5) + P(2)P(4) + "
                    "P(3)P(3) + P(4)P(2) + P(5)P(1) = 14 + 5 + 4 + 5 + 14 = 42`. Fourteen is "
                    "`P(5)`. 720 is 6!, which counts orderings of six things, not bracketings of "
                    "a fixed sequence. 32 is `2⁵`, which grows too slowly: the count is `Ω(2ⁿ)` "
                    "but not equal to it."},
            {"q": "Why does MATRIX-CHAIN-ORDER fill the table by chain length rather than row "
                  "by row from `m[1, 1]`?",
             "a": ["Filling by length uses fewer scalar multiplications than filling by row",
                   "Filling by length makes the table symmetric",
                   "Row by row would give the same answer more slowly",
                   "`m[i, j]` reads `m[k + 1, j]` for every split, a cell in a later row, so a row-by-row fill would read cells not yet computed"],
             "c": 3,
             "why": "A cell needs every shorter subchain inside it, and `m[k + 1, j]` lies below "
                    "row i. Filling by length guarantees those are done; a row-by-row fill reads "
                    "them empty and, as the lab shows, finishes with a wrong number, not a slower "
                    "right one. The table itself performs no matrix multiplications, and it is "
                    "upper triangular, not symmetric."},
            {"q": "Matrix `A₁` is 6 × 2 and `A₂A₃` has been computed as a 2 × 4 matrix. What "
                  "does the final multiplication `A₁(A₂A₃)` cost?",
             "a": ["`6·2 + 2·4 = 20`",
                   "`6·2·4 = 48`",
                   "`6·4 = 24`",
                   "`6·2·10·4 = 480`"],
             "c": 1,
             "why": "A `p × q` times `q × r` product costs `p·q·r`, here `6·2·4 = 48`. 24 is the "
                    "number of entries in the result, each of which needs two multiplications. "
                    "The sum of the two sizes counts nothing, and the 10 inside `A₂A₃` was paid "
                    "for when `A₂A₃` was computed, so it does not appear again."},
        ],
        "mistakes": [
            ("Thinking the multiplication order does not matter much",
             "Associativity guarantees the same product, not the same cost. On the lesson's "
             "five-matrix chain the best bracketing costs 228 scalar multiplications and the "
             "worst 1,064; on four matrices, 102 against 240. The section's three-matrix example "
             "differs by a factor of ten."),
            ("Filling the table in the order it is drawn",
             "Row by row from the top left looks natural and is wrong: a cell reads cells in "
             "later rows. The table still finishes, with a plausible number, which is why the lab "
             "paints the cells read too early red. The order comes from the recurrence: every "
             "cell reads shorter chains, so shorter chains go first."),
            ("Expecting the cheapest first product to lead to the cheapest total",
             "Choosing the split that makes the final multiplication cheapest, before solving "
             "the subchains, is a greedy rule, and Exercise 15.3-4 asks for an instance where it "
             "fails. The recurrence instead tries every split with its subchains already "
             "solved, which is what makes the answer optimal."),
        ],
        "standard": (
            "Finish when you can fill a chain table by hand and print its answer.",
            "Given dimensions for four or five matrices, fill m and s by chain length, give "
            "`m[1, n]` and the parenthesization, and count the bracketings an exhaustive search "
            "would try."
        ),
        "note": (
            "The lab's presets are its own and its enumeration is capped at a few hundred "
            "bracketings, so it checks small chains only; the cubic bound for every chain is the "
            "book's loop-counting argument. The lab cannot be set to the lesson's chain from the "
            "menu; type it."
        ),
    },
    # ---------------------------------------------------------------- 03
    # CLRS section 15.3, pp. 378-390.
    # Quote: p. 379, 16 words, quotes.py OK. Lesson total: 16 words.
    # Optimal substructure and its four-part pattern, keeping the subproblem
    # space simple, subproblems times choices (pp. 379-381); greedy contrast
    # (p. 381); unweighted shortest against longest simple path, independence
    # of subproblems (pp. 381-384); overlapping subproblems,
    # RECURSIVE-MATRIX-CHAIN and T(n) >= 2^(n-1) (pp. 384-386); storing
    # choices (p. 387); MEMOIZED-MATRIX-CHAIN and LOOKUP-CHAIN in O(n^3),
    # bottom-up against memoized in practice (pp. 387-389).
    {
        "slug": "elements-of-dynamic-programming",
        "title": "Elements of Dynamic Programming",
        "module": "Chapter 15 · Dynamic Programming",
        "one_line": "Dynamic programming needs two things, optimal substructure and overlapping subproblems, and a problem that looks like a shortest path can lack the first, as the longest simple path does.",
        "summary": (
            "Section 15.3 steps back from the examples and asks when dynamic programming "
            "applies. Optimal substructure is found by a recurring pattern ending in a cut-and-"
            "paste argument, and its running time is roughly subproblems times choices. The "
            "longest simple path shows a problem whose subproblems are not independent, so the "
            "pattern fails. Overlapping subproblems are why a plain recursion is exponential and "
            "a memoized one is not. Check both ingredients on a small graph by hand, then count "
            "a plain and a memoized recursion in the lab."
        ),
        "key": [
            "first ingredient: optimal substructure",
            "second: few subproblems, met often",
            "prove substructure by cut and paste",
            "time ≈ subproblems × choices each",
            "longest simple path lacks substructure",
            "memoize: top-down, still each once",
        ],
        "key_label": "Section 15.3 in six lines",
        "concepts_intro": (
            "Three ideas, each a test you can apply to a new problem before writing a table."
        ),
        "concepts": [
            ("Optimal substructure",
             "A problem has optimal substructure when an optimal solution contains optimal "
             "solutions to subproblems. It is shown, not assumed: suppose a subproblem's part "
             "of an optimal solution were not optimal, cut it out, paste in a better one, and "
             "derive a better whole, a contradiction."),
            ("Independent subproblems",
             "Two subproblems of one problem are independent when solving one does not use up "
             "anything the other needs. The two halves of a matrix chain share no matrix. The "
             "two halves of a longest simple path can compete for the same vertices, and that "
             "is where optimal substructure breaks."),
            ("Overlapping subproblems",
             "The space of subproblems is small, typically polynomial in the input, and a "
             "natural recursion keeps meeting the same ones. The term is not the opposite of "
             "independent: overlap is one subproblem recurring across different problems, "
             "independence is two subproblems of one problem not sharing resources."),
        ],
        "read_title": "Two ingredients, one subtlety, and the memo",
        "read_intro": (
            "Read Section 15.3 in your own copy first. The lesson sets out each ingredient in "
            "its own words, builds a small graph where the first one fails, and then counts a "
            "plain recursion against a memoized one in the lab."
        ),
        "body": [
            ("p", "&ldquo;Whenever a problem exhibits optimal substructure, we have a good clue "
                  "that dynamic programming might apply.&rdquo; The authors choose the words "
                  "carefully: a clue, and <em>might</em>. Section 15.3 is about the two "
                  "ingredients an optimization problem needs before dynamic programming is worth "
                  "trying, and about how to check each one instead of hoping."),
            ("p", "The first ingredient is optimal substructure, and the authors describe the "
                  "pattern you will find yourself following to discover it. Show that a solution "
                  "consists of a choice, a first piece or a split point, that leaves subproblems. "
                  "Suppose you are handed the choice an optimal solution makes, without worrying "
                  "yet how to find it. Work out which subproblems follow and how to describe "
                  "their space. Then prove, by the cut-and-paste argument, that the parts of an "
                  "optimal solution that solve those subproblems must be optimal for them."),
            ("p", "Keep the subproblem space as simple as possible and widen it only when "
                  "forced. For rod cutting, one length per subproblem was enough. For the matrix "
                  "chain, subproblems of the form `A₁⋯Aⱼ` are not: a split leaves a suffix "
                  "`Aₖ₊₁⋯Aⱼ` that does not start at 1, so both ends must vary. Problems also "
                  "differ in how many subproblems an optimal solution uses and how many choices "
                  "are tried for each, and informally the running time is the product of the "
                  "number of subproblems and the choices per subproblem: `Θ(n)` subproblems with "
                  "n choices for rod cutting, `Θ(n²)` with `n − 1` for the chain. The subproblem "
                  "graph tells the same story with vertices and arcs."),
            ("p", "The authors set greedy algorithms against this in a paragraph. Both rely on "
                  "optimal substructure, but dynamic programming solves the subproblems first "
                  "and then chooses with their answers in hand, while a greedy algorithm makes "
                  "the choice that looks best now and solves only the one subproblem left. That "
                  "it sometimes works is Chapter 16's subject."),
            ("p", "Then the subtlety. Unweighted shortest paths have optimal substructure: if a "
                  "shortest path from u to v passes through w, its two parts are shortest paths "
                  "from u to w and from w to v, or one could be replaced by a shorter one. The "
                  "longest simple path, the path with the most arcs and no repeated vertex, looks "
                  "just as decomposable, and is not. Here is a small directed graph of this "
                  "lesson's own, four vertices and six arcs, none of them two-way."),
            ("math", [
                "arcs:  u→v   u→w   v→w   w→x   x→u   x→v",
                "",
                "longest simple path u to v:   u → w → x → v    (3 arcs, the only one)",
                "its prefix u → w has 1 arc;   longest u to w:  u → v → w      (2 arcs)",
                "its suffix w → x → v, 2 arcs;  longest w to v:  w → x → u → v  (3 arcs)",
                "",
                "splice the two longest pieces:  u → v → w → x → u → v   repeats u and v",
            ]),
            ("p", "Neither part of the longest path is longest for its own endpoints, and "
                  "gluing the longest parts together does not even give a simple path. The "
                  "reason is that the subproblems are not independent: the longest path from u "
                  "to w spends the vertex v, which the path from w to v must end at, and the "
                  "longest path from w to v spends u. For shortest paths the authors prove the "
                  "two parts can never share a vertex other than w, since a shared vertex would "
                  "allow a shorter path. No efficient dynamic program for the longest simple "
                  "path is known, and the problem is NP-complete, which Chapter 34 explains."),
            ("p", "The second ingredient is <strong>overlapping subproblems</strong>. The authors "
                  "return to the matrix chain and write RECURSIVE-MATRIX-CHAIN, which evaluates "
                  "recurrence 15.7 with no table. Its running time obeys `T(n) ≥ 2·Σ T(i) + n` "
                  "over i from 1 to `n − 1`, and the substitution method gives `T(n) ≥ 2ⁿ⁻¹`: at "
                  "least exponential, although there are only `Θ(n²)` distinct subproblems. The "
                  "bottom-up table solves each once. Divide-and-conquer problems, by contrast, "
                  "usually generate new subproblems at every level, and a memo would never hit."),
            ("p", "Two practical points follow. Store the choice as well as the value: without "
                  "`s[i, j]`, rebuilding a parenthesization means re-trying `j − i` splits at "
                  "every step instead of reading one entry. And memoize when you prefer the "
                  "recursion's shape. MEMOIZED-MATRIX-CHAIN fills its table through LOOKUP-CHAIN, "
                  "which computes an entry on its first request and returns it on every later "
                  "one, in `O(n³)` like the bottom-up version. The authors' summary: if every "
                  "subproblem must be solved, bottom-up usually wins by a constant factor; if "
                  "some need never be solved, memoization solves only those that are needed."),
            ("p", "Now the lab, the memo lab of the Algorithms Subject's lesson Overlapping "
                  "Subproblems and the Memo. Its problem is making change with the fewest coins, "
                  "which has rod cutting's shape: choose the first coin, solve the rest. It runs "
                  "the recursion three ways, with no memo, with a memo and as a table, counts "
                  "each, and checks that all three return the same answer. Its presets are the "
                  "lab's own; <code>canonical</code>, coins 1, 2 and 5 for an amount of 18, makes "
                  "22,089 plain calls against 50 memoized."),
            ("p", "Type this lesson's instance: coins `1 4 6` and an amount of 20. The fewest "
                  "coins is 4, from 6 + 6 + 4 + 4; taking the largest coin first would give "
                  "6 + 6 + 6 + 1 + 1, five coins, a first hint of why Chapter 16 needs proofs. "
                  "The plain recursion makes 3,053 calls and the memoized one 53, while the memo "
                  "holds only 20 distinct subproblems, the amounts 1 to 20 (amount 0 is the base "
                  "case and is never stored). The lab prints the saving as `3053/53`, about 57.6 "
                  "times fewer calls, and the table fills 84 cells. The ratio grows with the "
                  "amount and the 53 barely does: raise the amount to 24 and the plain count "
                  "jumps to 14,085 while the memoized one adds twelve calls, to 65."),
            ("h3", "Exercise"),
            ("p", "In the lesson's graph, add the arc w→u. Find the longest simple path from u "
                  "to v now, check whether its two parts at w are longest for their own "
                  "endpoints, and say whether adding the arc repaired optimal substructure or "
                  "only changed the instance."),
            ("p", "With both ingredients named, the chapter returns to examples. The next "
                  "lesson, Longest Common Subsequence, has a recurrence whose cases depend on "
                  "the input, and a table whose arrows spell out the answer."),
        ],
        "lab": ("dpkit", {
            "mode": "memo",
            "preset": "canonical",
            "panel_title": "One recursion with and without a memo, and the table",
            "panel_intro": (
                "Type the coin denominations and an amount. The lab finds the fewest coins three "
                "ways, counts the calls of the plain and the memoized recursion and the cells of "
                "the table, and checks that the three answers agree. Type the lesson's coins "
                "1 4 6 and the amount 20."
            ),
        }),
        "steps_title": "Checking the two ingredients",
        "steps_intro": "Four checks to make on a new problem; the fifth is a problem of your own.",
        "steps": [
            ("Name the choice and the subproblems it leaves",
             "Say what an optimal solution decides first, a piece, a split, a coin, and write "
             "the subproblems that remain once it is made."),
            ("Argue optimal substructure by cut and paste",
             "Suppose the part of an optimal solution that solves a subproblem were not optimal "
             "for it. Replace it with a better one and check that the result is still a valid "
             "solution; if it is, the whole improves and you have a contradiction."),
            ("Check that the subproblems are independent",
             "Ask whether solving one subproblem can use up something another needs, a vertex, "
             "an item, a time slot. If it can, the paste step may produce an invalid solution and "
             "the argument fails."),
            ("Count distinct subproblems against calls",
             "Count how many different subproblems the recursion can ever ask about, then count "
             "how many calls it makes on a small case. A large gap means overlap, and a memo or "
             "a table will pay."),
            ("Do it on a problem of your own",
             "Take the coin problem with coins of your choice, run the four checks, then type the "
             "coins and an amount into the lab and record the plain and memoized call counts and "
             "the number of distinct subproblems the lab says its memo holds."),
        ],
        "worked": {
            "title": "The calls a plain recursion makes, counted by hand",
            "intro": [
                "For coins 1, 4 and 6, let `C(a)` be the calls the plain recursion makes on "
                "amount a, the first one included. A call on a calls once for each coin no "
                "larger than a, so `C(a) = 1 + Σ C(a − c)` over those coins.",
            ],
            "lines": [
                "C(0) = 1,  C(1) = 2,  C(2) = 3,  C(3) = 4",
                "C(4) = 1 + C(3) + C(0) = 6",
                "C(5) = 1 + C(4) + C(1) = 9",
                "C(6) = 1 + C(5) + C(2) + C(0) = 14",
                "C(7) = 1 + C(6) + C(3) + C(1) = 21",
                "C(8) = 1 + C(7) + C(4) + C(2) = 31",
                "amounts the memo stores at 8: 1 to 8;  memoized calls: 17",
            ],
            "after": [
                "The memoized count is the first call plus one call per coin that fits at each "
                "of the eight positive amounts: `1 + 1 + 1 + 1 + 2 + 2 + 3 + 3 + 3 = 17`. The "
                "same recurrence carried to 20 gives the lab's 3,053. The plain count grows by "
                "roughly half again with each unit of amount; the memoized count grows by at most "
                "three.",
            ],
        },
        "quiz_title": "Substructure, independence and overlap",
        "quiz": [
            {"q": "In the lesson's graph, the longest simple path from u to v is u → w → x → v. "
                  "What is the longest simple path from u to w?",
             "a": ["u → w, one arc",
                   "u → w → x → v → w, four arcs",
                   "u → x → v → w, three arcs",
                   "u → v → w, two arcs"],
             "c": 3,
             "why": "From u the arcs go to v and to w; from v the only arc goes to w. So the "
                    "simple paths from u to w are u → w and u → v → w, and the longer has two "
                    "arcs. The prefix of the longest u-to-v path is the shorter of them, which "
                    "is the point. The four-arc walk repeats w, and there is no arc from u to x."},
            {"q": "What does it mean that the two subproblems of the longest simple path are "
                  "not independent?",
             "a": ["The two subproblems recur in many branches of the recursion",
                   "A vertex used by the best solution of one subproblem may be needed by the other, so the two best solutions cannot always be combined",
                   "The two subproblems have different numbers of arcs",
                   "One subproblem must be solved before the other"],
             "c": 1,
             "why": "Independence is about shared resources: here, the vertices of a simple path. "
                    "Recurring in many branches is overlap, a different property that dynamic "
                    "programming needs. Different lengths and an order of solving say nothing "
                    "about whether the solutions can be combined."},
            {"q": "Informally, what running time does the subproblems-times-choices estimate "
                  "give for the matrix-chain problem on n matrices?",
             "a": ["`O(n³)`: `Θ(n²)` subproblems with at most `n − 1` choices each",
                   "`O(n²)`: one choice per subproblem",
                   "`O(2ⁿ)`: the number of parenthesizations",
                   "`O(n)`: each matrix is a choice once"],
             "c": 0,
             "why": "There is one subproblem per pair `i ≤ j`, `Θ(n²)` in all, and each tries up "
                    "to `n − 1` splits, so `O(n³)`; Exercise 15.2-5 makes it `Θ(n³)`. Each "
                    "subproblem has many choices, not one. The exponential count is what an "
                    "exhaustive search pays, not the dynamic program."},
            {"q": "With coins 1, 4 and 6, how many calls does the memoized recursion make on "
                  "the amount 8, counting the first?",
             "a": ["31",
                   "9",
                   "17",
                   "24"],
             "c": 2,
             "why": "The first call, then at each amount a from 1 to 8 one call per coin no "
                    "larger than a: 1 + 1 + 1 + 1 + 2 + 2 + 3 + 3 + 3 = 17. 31 is the plain "
                    "recursion's count, `C(8)`. Nine counts the distinct amounts 0 to 8, which are "
                    "subproblems, not calls. 24 charges every amount all three coins, `8·3`, which forgets that "
                    "coins larger than the amount are never tried."},
        ],
        "mistakes": [
            ("Assuming optimal substructure because the problem looks decomposable",
             "A longest simple path from u to v through w looks like a longest path to w "
             "followed by a longest path from w, and it is not: in the lesson's four-vertex "
             "graph both pieces are longer on their own, and spliced together they repeat "
             "vertices. Optimal substructure has to survive the cut-and-paste argument, and here "
             "the paste produces a path that is not simple."),
            ("Confusing independent with non-overlapping",
             "The two words sound like opposites and describe different things. Independent "
             "subproblems of one problem share no resources; overlapping subproblems are the "
             "same subproblem arising inside different problems. Dynamic programming needs both: "
             "the matrix chain's two halves share no matrix, and its subchains recur all over "
             "the recursion tree."),
            ("Believing memoization makes a recursion slower than a table",
             "A memoized recursion solves each subproblem once, as the table does, and has the "
             "same asymptotic running time; the difference is the constant for calls and table "
             "checks. When some subproblems are never needed, memoization does less work. On the "
             "lesson's coins at 20 the memo makes 53 calls and stores 20 amounts, and the "
             "table fills 84 cells."),
        ],
        "standard": (
            "Finish when you can test a problem for both ingredients.",
            "Given a small optimization problem, state its choice and subproblems, argue or "
            "refute optimal substructure with an instance, and compare the calls of a plain and "
            "a memoized recursion on a small case."
        ),
        "note": (
            "The lab's problem is making change, not the matrix chain the section analyses; the "
            "two share the structure that matters, and the chain lab of the previous lesson "
            "covers the other. The lab counts calls on one instance. Whether a problem has "
            "optimal substructure is a proof, and no count can show it."
        ),
    },
    # ---------------------------------------------------------------- 04
    # CLRS section 15.4, pp. 390-397.
    # Quote: p. 391, 18 words, quotes.py OK. Lesson total: 18 words.
    # DNA similarity as motivation, subsequence, common subsequence, LCS
    # (pp. 390-391); brute force over 2^m subsequences, prefixes, Theorem 15.1
    # and its proof (p. 392); recurrence 15.9 and subproblems ruled out by a
    # condition (p. 393); LCS-LENGTH, row-major order, the b table, Theta(mn)
    # (p. 394); PRINT-LCS in O(m + n) (p. 395); dropping the b table, two
    # rows for the length alone (p. 396).
    {
        "slug": "longest-common-subsequence",
        "title": "Longest Common Subsequence",
        "module": "Chapter 15 · Dynamic Programming",
        "one_line": "The longest common subsequence of two strings is found by a table over pairs of prefixes, filled in Θ(mn) time, whose arrows trace one longest subsequence back from the corner.",
        "summary": (
            "Section 15.4 measures the similarity of two sequences by the longest sequence that "
            "appears in both in order, not necessarily contiguously. A theorem about the last "
            "characters gives optimal substructure over prefixes, the recurrence has three cases, "
            "one of which depends on whether two characters match, and LCS-LENGTH fills an "
            "(m + 1) × (n + 1) table row by row with an arrow in each cell. PRINT-LCS follows the "
            "arrows back from the corner. Fill a five-by-five table by hand, then let the lab "
            "fill larger ones and count the arrows."
        ),
        "key": [
            "a subsequence keeps order, not adjacency",
            "subproblems: pairs of prefixes Xᵢ, Yⱼ",
            "last characters equal: extend the diagonal",
            "unequal: the larger of up and left",
            "the table has (m + 1)·(n + 1) cells",
            "follow the arrows back from c[m, n]",
        ],
        "key_label": "Section 15.4 in six lines",
        "concepts_intro": (
            "Three ideas: what a common subsequence is, which subproblems the theorem allows, "
            "and how the arrows carry the answer."
        ),
        "concepts": [
            ("Subsequence",
             "A subsequence of a sequence is the sequence with zero or more elements removed, the "
             "rest kept in their order. BLE is a subsequence of TABLE; LBE is not. A common "
             "subsequence of X and Y is a subsequence of both, and a longest one is an LCS. There "
             "may be several."),
            ("Prefixes as subproblems",
             "The i-th prefix `Xᵢ` is the first i elements of X, with `X₀` empty. "
             "`c[i, j]` is how long a longest common subsequence of `Xᵢ` and `Yⱼ` is. There are `(m + 1)·(n + 1)` "
             "such pairs, and every subproblem the recurrence ever asks about is one of them."),
            ("The b table of arrows",
             "Beside each `c[i, j]` LCS-LENGTH records which neighbour gave its value: the "
             "diagonal when `xᵢ = yⱼ`, the cell above or the cell to the left otherwise. "
             "Following the arrows from `c[m, n]` and printing a character at each diagonal "
             "step spells an LCS backwards."),
        ],
        "read_title": "The theorem, the recurrence, and one table by hand",
        "read_intro": (
            "Read Section 15.4 in your own copy first. The lesson sets out the theorem and the "
            "recurrence in its own words, fills one small table by hand, and then lets the lab "
            "fill larger ones."
        ),
        "body": [
            ("p", "&ldquo;A subsequence of a given sequence is just the given sequence with zero "
                  "or more elements left out.&rdquo; The authors define it in Section 15.4 after "
                  "a biological motivation: one way to say two strands of DNA are similar is that "
                  "a long strand appears in both, in the same order but not necessarily "
                  "contiguously. This lesson reads the section, the chapter's third full example."),
            ("p", "The authors set aside the brute-force approach first. Enumerating every "
                  "subsequence of X and testing each against Y examines `2ᵐ` candidates, one per "
                  "subset of X's positions, which is hopeless for long sequences. The way out is "
                  "to work with prefixes: `Xᵢ` is the first i elements of X, and the subproblems "
                  "are pairs of prefixes, one of X and one of Y."),
            ("thm", ("Theorem 15.1, optimal substructure of an LCS",
                     "Let Z, of length k, be any LCS of X, of length m, and Y, of length n. (1) "
                     "If `xₘ = yₙ`, then `zₖ = xₘ = yₙ` and `Zₖ₋₁` is an LCS of `Xₘ₋₁` and "
                     "`Yₙ₋₁`. (2) If `xₘ ≠ yₙ` and `zₖ ≠ xₘ`, then Z is an LCS of `Xₘ₋₁` and Y. "
                     "(3) If `xₘ ≠ yₙ` and `zₖ ≠ yₙ`, then Z is an LCS of X and `Yₙ₋₁`.")),
            ("p", "Each part is a short contradiction. In part 1, if Z did not end with the "
                  "shared last character, appending it would give a longer common subsequence; "
                  "and if `Zₖ₋₁` were not longest for the shorter prefixes, a longer one plus the "
                  "shared character would beat Z. Parts 2 and 3 say that a last character Z does "
                  "not use can be dropped without losing anything. So an LCS of two sequences "
                  "contains an LCS of two prefixes, which is optimal substructure."),
            ("thm", ("The recurrence",
                     "`c[i, j] = 0` if i = 0 or j = 0; `c[i, j] = c[i − 1, j − 1] + 1` if "
                     "`i, j > 0` and `xᵢ = yⱼ`; and `c[i, j]` is the larger of `c[i, j − 1]` and "
                     "`c[i − 1, j]` if `i, j > 0` and `xᵢ ≠ yⱼ`.")),
            ("p", "The authors point out a feature the earlier examples lacked: a condition in "
                  "the problem decides which subproblems are considered. When the characters "
                  "match, only the diagonal subproblem is used; when they differ, only the two "
                  "others. Rod cutting and the matrix chain tried every choice. The subproblems "
                  "also overlap at once: both `Xₘ₋₁, Y` and `X, Yₙ₋₁` contain `Xₘ₋₁, Yₙ₋₁`. "
                  "There are only `Θ(mn)` of them, and LCS-LENGTH fills `c[0..m, 0..n]` in "
                  "row-major order, each cell in constant time, so the whole table costs "
                  "`Θ(mn)`. Each cell reads its upper, left and upper-left neighbours, all "
                  "earlier in that order."),
            ("p", "LCS-LENGTH also fills `b[1..m, 1..n]` with an arrow: up-left for a match, up "
                  "when the cell above is at least as large as the cell to the left, left "
                  "otherwise. The tie goes up because the test that chooses up comes first. "
                  "PRINT-LCS starts at `b[m, n]`, follows the arrows, and prints the character at "
                  "each up-left arrow on the way back out of the recursion, so the LCS comes out "
                  "in forward order in `O(m + n)` time. Here is the table for `TABLE` against "
                  "`BLEAT`, with the cells PRINT-LCS passes through in brackets."),
            ("math", [
                "           B     L     E     A     T",
                "      0    0     0     0     0     0",
                "T     0    0↑    0↑    0↑    0↑    1↖",
                "A     0    0↑    0↑    0↑    1↖    1↑",
                "B     0   [1↖]   1←    1←    1↑    1↑",
                "L     0    1↑   [2↖]   2←    2←    2←",
                "E     0    1↑    2↑   [3↖]  [3←]  [3←]",
                "",
                "c[5, 5] = 3;  the path from the corner prints  B L E",
            ]),
            ("p", "Start at the corner, row E and column T, and go left twice to the match at E, "
                  "then diagonally to L and to B, then out of the table. The arrows in the first "
                  "two rows are never visited: they record that T and A could be matched, but "
                  "only in a common subsequence of length 1. The section ends with improvements. "
                  "The b table can be dropped, since from `c[i, j]` and its three neighbours you "
                  "can tell in constant time which one it came from, and the c table alone still "
                  "reconstructs an LCS in `O(m + n)`. If only the length is wanted, two rows of c "
                  "suffice; but then the path back is lost."),
            ("p", "Now the lab. It runs LCS-LENGTH on two strings you type, case sensitive and "
                  "up to 30 characters each, and prints the length, the LCS PRINT-LCS prints, the "
                  "cells filled as m × n, and how many of each arrow the b table holds; when both "
                  "strings have at most 15 characters it draws the table with PRINT-LCS's cells "
                  "in brackets. The preset <code>table-bleat</code> is the table above: length "
                  "3, BLE, `5 × 5 = 25` cells, with 5 up-left, 13 up and 7 left arrows."),
            ("p", "<code>anagrams</code> compares `ALGORITHM` with `LOGARITHM`, the same nine "
                  "letters rearranged. The LCS has length 7, and the lab prints LGRITHM; LORITHM "
                  "is just as long, and the tie going up is what picks the first. "
                  "<code>stone-notes</code> pairs `STONE` with `NOTES`, another anagram pair, "
                  "whose LCS has length only 2. <code>nothing-shared</code> compares `ACE` with "
                  "`BDF`: length 0, the empty sequence, and every arrow up. <code>thirty</code> "
                  "compares two 30-character strings over A, C, G and T: 900 cells, an LCS of "
                  "length 18, and no table drawn."),
            ("p", "The 900 cells are the bound and the count at once, because LCS-LENGTH fills "
                  "every cell whatever the strings are; the arrows are what change. What the lab "
                  "cannot show is that 18 is the longest, except by the theorem: no table of "
                  "counts checks optimality, and the recurrence is right because Theorem 15.1 "
                  "says the cases cover every LCS."),
            ("h3", "Exercise"),
            ("p", "Fill the c and b tables by hand for `STONE` and `NOTES`, with ties going up. "
                  "Give the length, list every longest common subsequence you can find, and say "
                  "which one PRINT-LCS prints. Then type the pair into the lab and compare the "
                  "arrow counts with yours."),
            ("p", "An LCS table is filled once and read once. The next lesson, Optimal Binary "
                  "Search Trees, fills a table over ranges of keys whose entries are expected "
                  "costs, and reads a whole tree out of it."),
        ],
        "lab": ("itakit", {
            "mode": "lcs",
            "view": "table",
            "preset": "table-bleat",
            "presets": [
                {"id": "table-bleat",
                 "label": "TABLE against BLEAT",
                 "x": "TABLE", "y": "BLEAT",
                 "expect": {"lciLength": "3", "lciLcs": "BLE", "lciCells": "5 × 5 = 25",
                            "lciArrows": "↖ 5, ↑ 13, ← 7"}},
                {"id": "anagrams",
                 "label": "ALGORITHM against LOGARITHM",
                 "x": "ALGORITHM", "y": "LOGARITHM",
                 "expect": {"lciLength": "7", "lciLcs": "LGRITHM", "lciCells": "9 × 9 = 81"}},
                {"id": "stone-notes",
                 "label": "STONE against NOTES",
                 "x": "STONE", "y": "NOTES",
                 "expect": {"lciLength": "2", "lciLcs": "TE"}},
                {"id": "nothing-shared",
                 "label": "ACE against BDF",
                 "x": "ACE", "y": "BDF",
                 "expect": {"lciLength": "0", "lciLcs": "(empty)", "lciArrows": "↖ 0, ↑ 9, ← 0"}},
                {"id": "thirty",
                 "label": "Two strings of 30 bases",
                 "x": "ATGCGTACGTTAGCCTAGGATCCGATTACG",
                 "y": "TACGGATCCTAGGCTAACGTACGCATGCAT",
                 "expect": {"lciLength": "18", "lciCells": "30 × 30 = 900"}},
            ],
            "panel_title": "Fill the table, count the arrows, follow them back",
            "panel_intro": (
                "Type two strings of letters or digits. The lab fills the c and b tables in "
                "row-major order as LCS-LENGTH does, sends ties up, and follows the arrows back "
                "from the corner. The cell count is the bound; the arrows are what your strings "
                "decide."
            ),
        }),
        "steps_title": "Filling an LCS table by hand",
        "steps_intro": "Four steps fill and read the table; the fifth uses two words of your own.",
        "steps": [
            ("Lay out the grid",
             "Write Y across the top and X down the side, with an extra row and column of zeros "
             "for the empty prefixes."),
            ("Fill row by row",
             "For each cell, if the row's and column's characters match, write one more than the "
             "upper-left cell with an up-left arrow. Otherwise copy the larger of the cell above "
             "and the cell to the left, choosing up on a tie, and draw that arrow."),
            ("Read the length",
             "The bottom-right cell is the longest common subsequence length for the whole strings."),
            ("Follow the arrows back",
             "From the corner, follow each arrow; at every up-left arrow note the character. "
             "Read the noted characters in reverse to get the LCS PRINT-LCS prints."),
            ("Do it on two words of your own",
             "Choose two words of five to seven letters, fill the table by hand, then type them "
             "into the lab and compare the length, the LCS and the three arrow counts."),
        ],
        "worked": {
            "title": "The bottom row of TABLE against BLEAT",
            "intro": [
                "The row for E, the fifth letter of `TABLE`, filled from the row for L above it, "
                "which reads `0 1 2 2 2 2`.",
            ],
            "lines": [
                "E vs B: differ; up 1 ≥ left 0, so 1, up",
                "E vs L: differ; up 2 ≥ left 1, so 2, up",
                "E vs E: match; upper-left 2 + 1 = 3",
                "E vs A: differ; up 2 < left 3, so 3, left",
                "E vs T: differ; up 2 < left 3, so 3, left",
                "row E:  0 1 2 3 3 3",
            ],
            "after": [
                "The match at E adds one to the best common subsequence of `TABL` and `BL`, which "
                "is BL, length 2. The two cells to its right inherit 3 from the left because no "
                "later letter of `BLEAT` extends it.",
            ],
        },
        "quiz_title": "Subsequences, cases and arrows",
        "quiz": [
            {"q": "Which of these is a common subsequence of `TABLE` and `BLEAT`?",
             "a": ["TB",
                   "BE",
                   "ABL",
                   "LEA"],
             "c": 1,
             "why": "B comes before E in both words, so BE is common. TB is a subsequence of "
                    "TABLE but in BLEAT the T comes last. ABL needs A before B, true in TABLE but "
                    "not in BLEAT, where A follows L and E. LEA is a subsequence of BLEAT, but "
                    "TABLE has no A after its L."},
            {"q": "In LCS-LENGTH, `xᵢ ≠ yⱼ`, the cell above holds 4 and the cell to the left "
                  "holds 4. What is stored?",
             "a": ["4 with a left arrow",
                   "5 with an up-left arrow",
                   "4 with an up-left arrow",
                   "4 with an up arrow"],
             "c": 3,
             "why": "With unequal characters the value is the larger neighbour, here 4, and the "
                    "test that chooses up, `c[i − 1, j] ≥ c[i, j − 1]`, is tried first, so a tie "
                    "goes up. A left arrow would need the left cell strictly larger. Adding 1 and "
                    "the up-left arrow belong to a match only."},
            {"q": "`ALGORITHM` and `LOGARITHM` have two longest common subsequences, LGRITHM "
                  "and LORITHM. Which does PRINT-LCS print, with ties going up?",
             "a": ["LORITHM",
                   "Both, one after the other",
                   "LGRITHM",
                   "Neither, since the tie makes c[9, 9] ambiguous"],
             "c": 2,
             "why": "The lab, which follows the book's tie rule, prints LGRITHM: at the cell for "
                    "the O of ALGORITHM against the A of LOGARITHM the values above and to the "
                    "left tie at 2, and the path goes up, toward the G match. LORITHM would need "
                    "the left branch there. PRINT-LCS prints one LCS "
                    "only, and the length 7 in the corner is not ambiguous at all."},
            {"q": "How many cells does LCS-LENGTH fill for two strings of 30 characters, and how "
                  "long does PRINT-LCS take?",
             "a": ["900 cells, and at most 60 steps",
                   "900 cells, and up to 900 steps",
                   "60 cells, and at most 60 steps",
                   "`2³⁰` cells, and up to 900 steps"],
             "c": 0,
             "why": "Every cell `c[i, j]` with i and j from 1 to 30 is filled, `30·30 = 900`, "
                    "besides the zero row and column. PRINT-LCS decreases i, j or both at each "
                    "step, so it takes at most `m + n = 60` steps and never visits most of the "
                    "table. Sixty cells would be one row and one column. `2³⁰` counts the "
                    "subsequences a brute force would try."},
        ],
        "mistakes": [
            ("Confusing a subsequence with a substring",
             "A substring is contiguous; a subsequence need only keep order. `ALGORITHM` and "
             "`LOGARITHM` share the substring `RITHM` of length 5 and the subsequence LGRITHM of "
             "length 7. Chapter 32 treats substrings; this section, subsequences."),
            ("Assuming anagrams have a long common subsequence",
             "Two words with the same letters can still order them very differently. `STONE` "
             "and `NOTES` are anagrams, and their longest common subsequence has length 2. The "
             "table counts order, not letters."),
            ("Expecting the arrows to give every LCS",
             "PRINT-LCS follows one arrow per cell, so it prints one LCS, chosen by the tie rule. "
             "On the lab's anagram preset it prints LGRITHM; LORITHM is equally long and is "
             "found by following the other branch at the tie. The length in the corner is the "
             "same either way."),
        ],
        "standard": (
            "Finish when you can fill and read an LCS table by hand.",
            "Given two strings of five to seven characters, fill c and b with ties going up, "
            "give the length and the LCS PRINT-LCS prints, and say how many cells were filled."
        ),
        "note": (
            "The lab prints the single LCS that the book's tie rule selects and counts arrows; "
            "listing every LCS is done by hand. Its tables are drawn only up to 15 characters a "
            "side. That every printed length is the longest is Theorem 15.1's claim, not "
            "something the count checks."
        ),
    },
    # ---------------------------------------------------------------- 05
    # CLRS section 15.5, pp. 397-404.
    # Quote: p. 399, 19 words, quotes.py OK. Lesson total: 19 words.
    # Translation lookup as motivation, keys and dummy keys, probabilities
    # summing to 1, expected search cost 15.11 (pp. 397-399); not the
    # smallest height, not the most probable root, exponentially many trees
    # (p. 399); subtrees on contiguous ranges, cut-and-paste, empty subtrees
    # (pp. 399-400); e[i, j], w(i, j), recurrences 15.13-15.14, root[i, j]
    # (pp. 400-401); OPTIMAL-BST with its e, w and root tables, Theta(n^3)
    # (pp. 401-403).
    {
        "slug": "optimal-binary-search-trees",
        "title": "Optimal Binary Search Trees",
        "module": "Chapter 15 · Dynamic Programming",
        "one_line": "When the probability of each search is known, the binary search tree with the least expected search cost is found by a table over ranges of keys, and it need be neither the shortest tree nor the one with the likeliest key at the root.",
        "summary": (
            "Section 15.5 builds a binary search tree for keys whose search probabilities are "
            "known, including the probabilities of unsuccessful searches that end at dummy "
            "leaves. Every subtree holds a contiguous range of keys, an optimal tree has optimal "
            "subtrees, and the expected cost of a range obeys a recurrence over its possible "
            "roots, with the range's total probability added at each level. OPTIMAL-BST fills "
            "the e, w and root tables by range length in Θ(n³). Fill a four-key table by hand, "
            "then let the lab check its answer against every tree."
        ),
        "key": [
            "a search costs the depth found, plus 1",
            "dummy leaves catch unsuccessful searches",
            "every subtree holds a range kᵢ to kⱼ",
            "try every root r from i to j",
            "a subtree pushed down costs w(i, j) more",
            "likeliest key need not be the root",
        ],
        "key_label": "Section 15.5 in six lines",
        "concepts_intro": (
            "Three ideas: the cost being minimized, the shape of a subproblem, and the term that "
            "accounts for depth."
        ),
        "concepts": [
            ("Expected search cost",
             "Keys `k₁ < ⋯ < kₙ` are searched with probabilities `p₁, …, pₙ`, and dummy keys "
             "`d₀, …, dₙ`, standing for the gaps between and beyond the keys, with probabilities "
             "`q₀, …, qₙ`; all of them sum to 1. A search costs the depth of the node it ends at "
             "plus one, and the expected cost of a tree is the probability-weighted sum."),
            ("Ranges as subproblems",
             "Any subtree of a binary search tree holds a contiguous range of keys `kᵢ, …, kⱼ` "
             "and has exactly the dummies `dᵢ₋₁, …, dⱼ` as its leaves. `e[i, j]` is the least "
             "expected cost of a tree on that range; the empty range `j = i − 1` holds the "
             "single dummy `dᵢ₋₁`."),
            ("The weight w(i, j)",
             "The total probability of a range, `pᵢ + ⋯ + pⱼ` plus `qᵢ₋₁ + ⋯ + qⱼ`. When a "
             "subtree becomes a child of a new root every node in it moves one level deeper, so "
             "its expected cost rises by exactly its weight."),
        ],
        "read_title": "The cost, the four steps, and one table by hand",
        "read_intro": (
            "Read Section 15.5 in your own copy first. The lesson sets out the cost and the "
            "recurrence in its own words, fills a four-key table by hand, and then runs the lab, "
            "which checks the table against every tree."
        ),
        "body": [
            ("p", "&ldquo;This example shows that an optimal binary search tree is not "
                  "necessarily a tree whose overall height is smallest.&rdquo; The authors say it "
                  "early in Section 15.5, and add that putting the most probable key at the root "
                  "does not work either. Both shortcuts fail, and the section replaces them with "
                  "the chapter's method. This lesson reads it, the last of Chapter 15's examples."),
            ("p", "The motivating example is a translation program that looks up every word of "
                  "a text in a search tree: a balanced tree guarantees `O(lg n)` per lookup, but "
                  "frequent words should sit near the root, and some words of the text are not in "
                  "the tree at all. So the model has keys with probabilities `pᵢ` and dummy keys "
                  "with probabilities `qᵢ` for the unsuccessful searches. Each key is an internal "
                  "node and each dummy a leaf, every search ends at one of them, and the "
                  "probabilities sum to 1."),
            ("def", ("Expected search cost",
                     "With a search costing the depth of the node found plus one, the expected "
                     "cost of a tree T is the sum of `(depth(kᵢ) + 1)·pᵢ` over the keys plus the "
                     "sum of `(depth(dᵢ) + 1)·qᵢ` over the dummies, which equals 1 plus the "
                     "probability-weighted depths. An optimal binary search tree minimizes it.")),
            ("p", "Exhaustive search is out: there are as many trees as binary trees with n "
                  "nodes, which Problem 12-4 shows is `Ω(4ⁿ/n^(3/2))`. Step 1 is the observation "
                  "that a subtree holds a contiguous range of keys and the dummies between and "
                  "around them, and the cut-and-paste argument: if an optimal tree had a subtree "
                  "on `kᵢ, …, kⱼ` that was not optimal for that range, pasting in a better one "
                  "would lower the whole tree's cost. An optimal tree on the range has some root "
                  "`kᵣ`, an optimal left subtree on `kᵢ, …, kᵣ₋₁` and an optimal right subtree on "
                  "`kᵣ₊₁, …, kⱼ`, and trying every r finds it. A root at an end of the range has "
                  "an empty subtree on that side, which by convention holds one dummy."),
            ("thm", ("The recurrence for e[i, j]",
                     "`e[i, i − 1] = qᵢ₋₁`, and for `i ≤ j`, `e[i, j]` is the minimum over r "
                     "from i to j of `e[i, r − 1] + e[r + 1, j] + w(i, j)`. The root's own "
                     "`pᵣ` and the one level each subtree descends add up to exactly the range's "
                     "weight. `root[i, j]` records an r that attains the minimum.")),
            ("p", "Step 3 is OPTIMAL-BST, which has the matrix chain's shape: ranges instead of "
                  "subchains, filled by length. Its tables are indexed so that the empty ranges "
                  "fit, `e[1..n + 1, 0..n]`, and a third table `w` saves recomputing weights, "
                  "since `w[i, j] = w[i, j − 1] + pⱼ + qⱼ` in constant time. The loops nest three "
                  "deep and the procedure takes `Θ(n³)`. Building the tree from `root` is left as "
                  "Exercise 15.5-1, and Exercise 15.5-4 points to a faster method due to Knuth."),
            ("p", "Here is a four-key instance of this lesson's own, with every probability a "
                  "whole number of fortieths: `p = 7, 6, 5, 10` and `q = 3, 2, 2, 2, 3`. Key `k₄` "
                  "is the most likely search. The table below gives `w` and `e` in fortieths, "
                  "filled by range length."),
            ("math", [
                "range      w     e     root   (all in 40ths)",
                "1..1      12    17     k1",
                "2..2      10    14     k2",
                "3..3       9    13     k3",
                "4..4      15    20     k4",
                "1..2      20    37     k1",
                "2..3      17    32     k2",
                "3..4      22    38     k4",
                "1..3      27    57     k2",
                "2..4      30    64     k3",
                "1..4      40    95     k2      e[1, 4] = 95/40 = 19/8",
            ]),
            ("p", "So the least expected cost is `19/8 = 2.375`, with `k₂` at the root, `k₁` to "
                  "its left, and `k₄` to its right with `k₃` below it. The likeliest key, `k₄`, "
                  "is one level down; the best tree with `k₄` at the root costs `100/40 = 2.5`. "
                  "The reason is the dummies and the smaller keys: three keys and four dummies lie "
                  "to the left of `k₄`, and a root at the right end pushes all of them down."),
            ("p", "Now the lab. It runs OPTIMAL-BST on the probabilities you type, each given as "
                  "a whole-number weight divided by a common scale (the lab refuses fractions "
                  "such as `7/40`, so the four-key instance is typed as weights over the scale "
                  "40), and prints the expected cost `e[1, n]`, the optimal tree in nested text, "
                  "the root table row by row, and a brute-force check over every tree up to seven "
                  "keys. A tie keeps the smallest root."),
            ("p", "The preset <code>four-keys</code> is the table above: `19/8`, the tree "
                  "`k2(k1(d0 d1) k4(k3(d2 d3) d4))`, root rows `1: 1 1 2 2; 2: 2 2 3; 3: 3 4; 4: 4`, "
                  "and 14 trees tried by brute force, with one cheapest. "
                  "<code>three-keys</code> types decimals, `p = 0.2 0.1 0.25` and "
                  "`q = 0.1 0.15 0.1 0.1`, and the optimal root is `k₂`, the <em>least</em> likely "
                  "key, at expected cost `47/20 = 2.35`: its dummies carry the weight. "
                  "<code>seven-equal</code> gives seven keys equal probability and no misses, "
                  "and the answer is the perfectly balanced tree at `17/7`, the only cheapest of "
                  "429. <code>eight-keys</code> runs at n = 8, where the table answers `29/10` "
                  "and the brute force declines to enumerate 1,430 trees."),
            ("p", "That last preset marks the boundary of what a check can do. Up to seven keys "
                  "the lab can compare the table with every tree and they agree; at eight it can "
                  "only fill the table. The table is right at every n because of the cut-and-"
                  "paste argument, which the agreement at small n illustrates and does not prove."),
            ("h3", "Exercise"),
            ("p", "For the four-key instance, compute by hand the expected cost of the tree with "
                  "`k₃` at the root, `k₁` and `k₂` on its left with `k₁` above `k₂`, and `k₄` on "
                  "its right. Check your total against row 1..4 of the table: which root does the "
                  "table say beats it, and by how many fortieths?"),
            ("p", "Chapter 15 ends here. The next lesson, Activity Selection and the Greedy "
                  "Strategy, opens Chapter 16 with a problem where one choice can be made before "
                  "any subproblem is solved."),
        ],
        "lab": ("itakit", {
            "mode": "obst",
            "view": "table",
            "preset": "four-keys",
            "presets": [
                {"id": "four-keys",
                 "label": "Four keys in fortieths, the likeliest at the right end",
                 "p": "7 6 5 10", "q": "3 2 2 2 3", "scale": "40",
                 "expect": {"obiCost": "19/8 ≈ 2.38", "obiTree": "k2(k1(d0 d1) k4(k3(d2 d3) d4))",
                            "obiRoots": "1: 1 1 2 2; 2: 2 2 3; 3: 3 4; 4: 4",
                            "obiBrute": "14 trees; least 19/8 ≈ 2.38 (1 tree); agrees"}},
                {"id": "three-keys",
                 "label": "Three keys typed as decimals",
                 "p": "0.2 0.1 0.25", "q": "0.1 0.15 0.1 0.1",
                 "expect": {"obiCost": "47/20 = 2.35", "obiTree": "k2(k1(d0 d1) k3(d2 d3))"}},
                {"id": "seven-equal",
                 "label": "Seven equally likely keys and no misses",
                 "p": "1 1 1 1 1 1 1", "q": "0 0 0 0 0 0 0 0", "scale": "7",
                 "expect": {"obiCost": "17/7 ≈ 2.43",
                            "obiBrute": "429 trees; least 17/7 ≈ 2.43 (1 tree); agrees"}},
                {"id": "eight-keys",
                 "label": "Eight keys in eightieths",
                 "p": "5 9 4 12 3 8 6 10", "q": "2 3 2 4 3 2 3 2 2", "scale": "80",
                 "expect": {"obiCost": "29/10 = 2.90",
                            "obiBrute": "not run at n = 8 (the lab enumerates trees up to n = 7)"}},
            ],
            "panel_title": "Fill the e, w and root tables, then check every tree",
            "panel_intro": (
                "Type the key and dummy probabilities, as decimals or as whole weights over a "
                "scale. The lab fills the tables by range length as OPTIMAL-BST does, prints the "
                "tree its root table describes, and up to seven keys sets the answer beside the "
                "cheapest of every binary search tree."
            ),
        }),
        "steps_title": "Filling an optimal-tree table by hand",
        "steps_intro": "Four steps fill and read the tables; the fifth is an instance of your own.",
        "steps": [
            ("Scale to whole numbers",
             "Multiply every p and q by a common denominator so the arithmetic is in whole "
             "numbers. Write `e[i, i − 1] = w[i, i − 1] = qᵢ₋₁` for the empty ranges."),
            ("Fill the weights",
             "For each range, `w[i, j] = w[i, j − 1] + pⱼ + qⱼ`. The whole range must come to "
             "the scale, which checks your arithmetic."),
            ("Fill e by range length",
             "For each range try every root r: add `e[i, r − 1]`, `e[r + 1, j]` and `w[i, j]`, "
             "keep the smallest in e and its r in root, the smaller r on a tie."),
            ("Build the tree from root",
             "The whole range's root is `root[1, n]`; its left subtree is the range to its left, "
             "whose root is read from the table, and so on down to the dummies."),
            ("Do it on an instance of your own",
             "Choose three keys and four dummies with weights summing to 20, fill the tables by "
             "hand, then type the weights and the scale 20 into the lab and compare the cost, the "
             "tree and the brute-force check."),
        ],
        "worked": {
            "title": "The cell e[2, 4] of the four-key instance",
            "intro": [
                "In fortieths, the range `k₂, k₃, k₄` has weight `w[2, 4] = 30`. The cells it "
                "reads are already filled: `e[2, 1] = 2`, `e[3, 4] = 38`, `e[2, 2] = 14`, "
                "`e[4, 4] = 20`, `e[2, 3] = 32` and `e[5, 4] = 3`.",
            ],
            "lines": [
                "r = 2:  e[2,1] + e[3,4] + 30 = 2 + 38 + 30 = 70",
                "r = 3:  e[2,2] + e[4,4] + 30 = 14 + 20 + 30 = 64",
                "r = 4:  e[2,3] + e[5,4] + 30 = 32 + 3 + 30 = 65",
                "e[2,4] = 64,  root[2,4] = 3",
            ],
            "after": [
                "The middle key wins by one fortieth over `k₄`. The same weight 30 is added for "
                "every candidate root, so it never decides the choice; it is the price of the "
                "whole range moving one level down when it becomes a subtree.",
            ],
        },
        "quiz_title": "Costs, ranges and roots",
        "quiz": [
            {"q": "In the four-key instance, why is `k₄` not the root of the optimal tree, though "
                  "it is the likeliest key?",
             "a": ["The root must be a key with an even index",
                   "OPTIMAL-BST breaks ties toward smaller keys, and `k₂` and `k₄` tie",
                   "With `k₄` at the root, the other three keys and four of the five dummies sit one level lower, which costs more than `k₄`'s one level saves",
                   "The optimal tree always has the smallest height, and `k₄` at the root would make it taller"],
             "c": 2,
             "why": "The best tree with `k₄` at the root costs `100/40` against `95/40` for "
                    "`k₂`, so there is no tie for the tie rule to break. Index parity means "
                    "nothing. Height does not decide it either, as the section's opening "
                    "quotation says; the weights below a root decide it."},
            {"q": "A range has weight `w[i, j] = 30` in fortieths and becomes the left subtree of "
                  "a new root. By how much does its contribution to the expected cost rise?",
             "a": ["By `30/40`",
                   "By `60/40`",
                   "Not at all",
                   "By the new root's own probability"],
             "c": 0,
             "why": "Every node in the range moves one level deeper, and each level costs its "
                    "probability once more, so the rise is the range's total probability, "
                    "`w = 30/40`. Doubling it would count two levels. The root's own probability "
                    "is added separately, as `pᵣ`, inside the parent's weight."},
            {"q": "How many entries does OPTIMAL-BST compute for `e[i, j]` with `i ≤ j`, and how "
                  "many candidate roots does it try for a range of length l?",
             "a": ["`n²` entries, n roots each",
                   "`n·(n + 1)/2` entries, l roots each",
                   "n entries, `l − 1` roots each",
                   "`n·(n + 1)/2` entries, `l − 1` roots each"],
             "c": 1,
             "why": "One entry per range `1 ≤ i ≤ j ≤ n`, `n·(n + 1)/2` of them, and every key "
                    "of the range can be its root, l candidates. `l − 1` is the matrix chain's "
                    "number of splits, one fewer because a split falls between matrices while a "
                    "root is a key. The n entries would be the single-key ranges only."},
            {"q": "Seven keys with equal probability and no misses: what is the expected cost of "
                  "the optimal tree?",
             "a": ["`3`",
                   "`10/7`",
                   "`4`",
                   "`17/7`"],
             "c": 3,
             "why": "The optimal tree is the balanced one, with one key at depth 0, two at depth "
                    "1 and four at depth 2, costing `(1·1 + 2·2 + 4·3)/7 = 17/7`. Three is the "
                    "cost of a deepest key only. `10/7` is the weighted depth without the one "
                    "probe every search makes at the root. Four is a dummy's depth plus one, and "
                    "with no misses the dummies cost nothing."},
        ],
        "mistakes": [
            ("Putting the likeliest key at the root",
             "It sounds right and can be wrong, because a root at one end of the order pushes "
             "every other key and most dummies down a level. In the four-key instance the "
             "likeliest key `k₄` at the root gives `100/40` at best, against `95/40` for "
             "`k₂`; in the lab's three-key preset the optimal root is the least likely key."),
            ("Leaving out the unsuccessful searches",
             "The dummies `dᵢ` are leaves, and the searches that end at them have cost too. "
             "Without them the weight of a range is too small and the tree favours the keys "
             "wrongly. In the three-key preset the q's are 45 hundredths of all searches, and "
             "they are what put `k₂` at the root."),
            ("Forgetting the weight term in the recurrence",
             "`e[r + 1, j]` is the cost of the right subtree as a tree of its own; under a new "
             "root it is one level deeper, which costs `w(r + 1, j)` more, and the same holds on "
             "the left. Together with the root's `pᵣ` these add to `w(i, j)`. Leaving the term "
             "out computes the cost of a forest, not a tree."),
        ],
        "standard": (
            "Finish when you can fill an optimal-tree table and read the tree.",
            "Given three or four keys with dummy probabilities, fill w, e and root by range "
            "length, give `e[1, n]` and the tree, and explain why its root is not simply the "
            "likeliest key."
        ),
        "note": (
            "The lab takes probabilities as decimals or as whole weights over a scale and "
            "refuses fractions, so every instance here is in whole numbers over a common "
            "denominator. Its brute-force check stops at seven keys; the table is correct beyond "
            "that by the section's argument, not by any check the lab can run."
        ),
    },
]
