"""Parallel, Matrix, Linear and Number Algorithms, lessons 1-5 -- Chapters 27-30.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed. (MIT
Press, 2009): Chapter 27, Multithreaded Algorithms (pp. 772-812); Chapter 28,
Matrix Operations (pp. 813-842); Chapter 29, Linear Programming (pp. 843-897);
Chapter 30, Polynomials and the FFT (pp. 898-925). Every quotation is copied
from the operator's copy with its printed page in the comment beside the
lesson. The instances are written for these lessons; none of the book's
figures, tables, pseudocode, worked examples or exercises is reproduced. Every
figure the prose attributes to a lab was read off the running kit, and every
hand computation was done by hand and checked against the lab.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # CLRS 27.1-27.3, pp. 772-812. Quote: printed p. 772, 27 words,
    # quotes.py OK. Lesson total: 27 words. Lab: itakit/workspan view
    # recurrence; P-FIB(4), the book's own figure, is not a preset.
    # Spawn, sync, parallel and serialization (pp. 774-777); the computation
    # DAG and its edges (pp. 777-779); work law, span law, speedup,
    # parallelism, slackness (pp. 779-781); greedy scheduling, Theorem 27.1,
    # Corollaries 27.2-27.3, slackness of 10 (pp. 781-783); series and
    # parallel composition and P-FIB's span (pp. 784-785); parallel loops and
    # determinacy races (pp. 785-790); matrix multiplication (27.2,
    # pp. 792-797); MERGE-SORT', P-MERGE's 3n/4 and lg^2 n, P-MERGE-SORT
    # (27.3, pp. 797-805).
    {
        "slug": "multithreaded-algorithms",
        "title": "Multithreaded Algorithms",
        "module": "Chapter 27 · Multithreaded Algorithms",
        "one_line": "A multithreaded program is a directed acyclic graph of strands; its work is the total cost, its span the costliest path, and a greedy scheduler on P processors finishes within work/P plus span.",
        "summary": (
            "Chapter 27 extends the book's serial model with three keywords, spawn, sync and "
            "parallel, and measures a program by two numbers: its work, the time on one "
            "processor, and its span, the time on unboundedly many. Section 27.1 proves that a "
            "greedy scheduler runs in at most work/P + span on P processors; sections 27.2 and "
            "27.3 apply the measures to matrix multiplication and merge sort. Compute work and "
            "span for P-FIB and a multithreaded merge sort in the lab and see which one more "
            "processors can help."
        ),
        "key": [
            "work T₁: the total cost of all strands",
            "span T∞: the costliest path in the DAG",
            "work law: T_P ≥ T₁/P",
            "span law: T_P ≥ T∞",
            "parallelism T₁/T∞ caps the speedup",
            "greedy: T_P ≤ T₁/P + T∞",
            "series adds spans, parallel takes the max",
        ],
        "key_label": "Chapter 27 in seven lines",
        "concepts_intro": (
            "Three ideas: the two measures of a multithreaded computation, the ratio between "
            "them, and the kind of scheduler that comes close to both."
        ),
        "concepts": [
            ("Work and span",
             "Draw the computation as a graph whose vertices are strands, runs of instructions "
             "with no spawn, sync or return inside, and whose edges say which must finish "
             "first. The work T₁ is the sum of all strand costs, the running time on one "
             "processor. The span T∞ is the cost of the costliest path, the running time with "
             "as many processors as could ever be used."),
            ("Parallelism and slackness",
             "The parallelism T₁/T∞ is the most speedup the computation can have on any number "
             "of processors: the average amount of work available at each step of the critical "
             "path. The slackness on P processors is the parallelism divided by P; below 1, "
             "perfect linear speedup is impossible."),
            ("Greedy scheduler",
             "A scheduler that never leaves a processor idle when a strand is ready. At each "
             "step it runs P ready strands if there are that many, and all of them otherwise. "
             "It needs no knowledge of the future, and Theorem 27.1 shows it never takes more "
             "than twice as long as the best possible schedule."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 27.1 to 27.3 in your own copy first; 27.1 is the one to read "
            "closely. The lesson sets out the model and its two laws in its own words, works "
            "a small computation by hand, and then counts P-FIB and a multithreaded merge sort "
            "in the lab."
        ),
        "body": [
            ("p", "&ldquo;The vast majority of algorithms in this book are serial algorithms "
                  "suitable for running on a uniprocessor computer in which only one instruction "
                  "executes at a time.&rdquo; Chapter 27 begins by stepping outside that model. "
                  "Multicore laptops are shared-memory parallel machines, and the authors choose "
                  "dynamic multithreading as the model to program them in: the programmer says "
                  "which parts may run at the same time, and a scheduler decides where and when "
                  "they do. This lesson reads all three sections, the basics, matrix "
                  "multiplication and merge sort."),
            ("p", "The model adds three keywords to the book's pseudocode. Spawn in front of a "
                  "call lets the caller go on while the child runs; sync makes the caller wait "
                  "for every child it has spawned; parallel in front of a for loop says the "
                  "iterations may run at once. Delete the three words and you get the "
                  "serialization, an ordinary serial program that computes the same thing. The "
                  "chapter's first example is P-FIB, the exponential Fibonacci recursion with "
                  "its first recursive call spawned, chosen because it is slow and easy to "
                  "analyse, not because anyone should compute Fibonacci numbers that way."),
            ("p", "A run of such a program is a directed acyclic graph. Each vertex is a "
                  "strand, a sequence of instructions containing no parallel control; each edge "
                  "is a continuation within one procedure, a spawn, a call, or a return to the "
                  "caller. The analysis assumes an ideal parallel computer: P equally fast "
                  "processors, a sequentially consistent shared memory, and no cost for "
                  "scheduling. Two numbers then describe the graph: the work T₁, the total cost of "
                  "the strands, and the span T∞, the cost of the costliest path."),
            ("thm", ("The work law and the span law",
                     "Let `T_P` be the running time on P processors. In one step P processors "
                     "do at most P units of work, so `T_P ≥ T₁/P`. A machine with P processors "
                     "can do no better than one with unboundedly many, so `T_P ≥ T∞`. The "
                     "speedup `T₁/T_P` is therefore at most P, and at most the parallelism "
                     "`T₁/T∞`.")),
            ("p", "The two laws are lower bounds on every schedule. The upper bound needs a "
                  "scheduler, and the authors analyse the simplest good one, the greedy "
                  "scheduler. Call a step complete if at least P strands are ready, so all P "
                  "processors are busy, and incomplete otherwise. Complete steps each do P units "
                  "of work, so there are at most `T₁/P` of them. An incomplete step runs every "
                  "ready strand, and every strand that starts a longest remaining path is ready, "
                  "so each incomplete step shortens the remaining span by one: at most T∞ of "
                  "them. Adding the two counts gives the theorem."),
            ("thm", ("Theorem 27.1, with its corollaries, in short",
                     "A greedy scheduler on P processors runs a computation of work T₁ and span "
                     "T∞ in time `T_P ≤ T₁/P + T∞`. Since the optimum is at least the larger of "
                     "the two terms, greedy never takes more than twice the optimum (Corollary 27.2), "
                     "and when P is much less than the parallelism, `T_P` is close to `T₁/P`, a "
                     "speedup of nearly P (Corollary 27.3).")),
            ("p", "How much is much less? The authors' rule of thumb is a slackness of at least "
                  "10, ten times as much parallelism as processors, which keeps the span term "
                  "under a tenth of the work term. Two composition rules make the measures easy "
                  "to compute. Subcomputations in series add both work and span; subcomputations "
                  "in parallel add their work but take the larger span. For P-FIB the work is "
                  "that of the serial recursion, `Θ(φⁿ)`, while the two recursive calls run in "
                  "parallel, so `T∞(n) = max(T∞(n − 1), T∞(n − 2)) + Θ(1) = Θ(n)`. The "
                  "parallelism, `Θ(φⁿ/n)`, grows so fast that a modest n keeps any machine "
                  "busy."),
            ("example", ("Seven strands by hand",
                         "A program starts with `init` (cost 2), then spawns `load` (6) and "
                         "continues with `parse` (3), which spawns `index` (4) and continues "
                         "with `check` (2). A sync joins `index` and `check` into `merge` (1), "
                         "and a final sync joins `merge` and `load` into `done` (1). The work is "
                         "`2 + 6 + 3 + 4 + 2 + 1 + 1 = 19`. The paths are init, load, done at "
                         "`2 + 6 + 1 = 9` and init, parse, index, merge, done at "
                         "`2 + 3 + 4 + 1 + 1 = 11`, so the span is 11 and the parallelism "
                         "`19/11 ≈ 1.73`. On two processors the greedy bound is "
                         "`19/2 + 11 = 20.5` and no schedule beats `max(9.5, 11) = 11`.")),
            ("p", "Loops are parallelized the same way. A parallel for loop of n iterations is "
                  "compiled into a divide-and-conquer tree of spawns, which adds `Θ(lg n)` to the "
                  "span on top of the costliest iteration; the book's matrix-vector product has "
                  "span `Θ(n)` because each iteration is a serial inner loop of n steps. The "
                  "model's hazard is the determinacy race: two logically parallel instructions "
                  "touch one memory location and one of them, at least, writes to it. The result "
                  "then depends on the schedule, and a race can hide through many correct runs. "
                  "The chapter's remedy is discipline: strands that run in parallel should be "
                  "independent."),
            ("p", "Section 27.2 parallelizes matrix multiplication. The triple loop with its two "
                  "outer loops made parallel has work `Θ(n³)` and span `Θ(n)`. The recursive "
                  "version spawns its eight half-size products and adds the results with a "
                  "parallel loop; its span obeys `M∞(n) = M∞(n/2) + Θ(lg n) = Θ(lg² n)`, so its "
                  "parallelism is `Θ(n³/lg² n)`. Strassen's method parallelizes the same way, with "
                  "the same span and work `Θ(n^(lg 7))`. Section 27.3 turns to merge sort, and "
                  "there the merge decides everything."),
            ("math", [
                "MERGE-SORT′: spawn the two halves, then merge serially",
                "work:  T₁(n) = 2·T₁(n/2) + Θ(n) = Θ(n lg n)",
                "span:  T∞(n) = T∞(n/2) + Θ(n) = Θ(n)",
                "parallelism: Θ(lg n)",
                "",
                "P-MERGE-SORT: the same, with the merge P-MERGE",
                "P-MERGE span: PM∞(n) = PM∞(3n/4) + Θ(lg n) = Θ(lg² n)",
                "sort span:  T∞(n) = T∞(n/2) + Θ(lg² n) = Θ(lg³ n)",
                "parallelism: Θ(n/lg² n)",
            ]),
            ("p", "A serial merge of n keys sits on the critical path at the top level, so "
                  "spawning the halves buys only a logarithmic parallelism. P-MERGE splits the "
                  "merge itself: it takes the median x of the larger input, finds by binary "
                  "search where x falls in the smaller one, places x in the output, and merges "
                  "the two pairs of pieces on either side of it in parallel. The larger input "
                  "contributes at most half of its keys to either side, so neither recursive "
                  "merge gets more than `3n/4` keys, and the span recurrence above solves to "
                  "`Θ(lg² n)` while the work stays linear."),
            ("p", "Now the lab. It evaluates work and span exactly for P-FIB and for "
                  "MERGE-SORT′, the serial-merge version, with the counting stated in its rules: a "
                  "P-FIB call on n ≥ 2 is three unit strands and a call on 0 or 1 is one; a "
                  "MERGE-SORT′ call on one key costs 1 and a merge of m keys costs m. Its tiles are "
                  "the work, the span, the parallelism, the greedy bound `T₁/P + T∞`, the lower "
                  "bound `max(T₁/P, T∞)` from the two laws, and the critical path. Preset "
                  "pfib-10: work 353, span 20, parallelism `353/20 = 17.65`, and on four "
                  "processors a greedy bound of `433/4 = 108.25` against a lower bound of "
                  "`353/4 = 88.25`."),
            ("p", "Preset pfib-10-on-64 gives the same computation 64 processors: the lower "
                  "bound falls only to 20, the span, because the parallelism is 17.65 and the "
                  "span law rules. Preset pfib-25-on-64 has work 485,569, span 50 and "
                  "parallelism `9,711.38`, a slackness of about 150, and the greedy bound "
                  "`≈ 7,637.02` is within one percent of the lower bound. MERGE-SORT′ on 1,024 keys "
                  "has work 11,264 and span 2,047, parallelism `≈ 5.50`: preset msort-1024-on-8 "
                  "bounds the time by 3,455, and msort-1024-on-64 by 2,223 against a floor of "
                  "2,047. Eight times the processors buys about a third off, because the serial "
                  "merge at the top costs 1,024 on its own."),
            ("h3", "Exercise"),
            ("p", "With the lab's counting, compute the work and span of P-FIB(6) by hand from "
                  "those of P-FIB(4) and P-FIB(5), and the work and span of MERGE-SORT′ on 16 keys. "
                  "Then set the lab to each and compare. Finally, find the smallest n at which "
                  "P-FIB(n) has a slackness of at least 10 on 64 processors."),
            ("p", "Matrix multiplication was one of this chapter's examples; the next lesson, "
                  "Solving Systems of Linear Equations, reads Chapter 28's other matrix problem, "
                  "solving `Ax = b` by an LUP decomposition."),
        ],
        "lab": ("itakit", {
            "mode": "workspan",
            "view": "recurrence",
            "preset": "pfib-10",
            "presets": [
                {"id": "pfib-10", "label": "P-FIB(10) on 4 processors",
                 "program": "p-fib", "n": "10", "p": "4",
                 "expect": {"wsiWork": "353", "wsiSpan": "20",
                            "wsiParallelism": "353/20 = 17.65",
                            "wsiBound": "433/4 = 108.25", "wsiLower": "353/4 = 88.25"}},
                {"id": "pfib-10-on-64", "label": "P-FIB(10) on 64 processors",
                 "program": "p-fib", "n": "10", "p": "64",
                 "expect": {"wsiParallelism": "353/20 = 17.65", "wsiLower": "20"}},
                {"id": "pfib-25-on-64", "label": "P-FIB(25) on 64 processors",
                 "program": "p-fib", "n": "25", "p": "64",
                 "expect": {"wsiWork": "485,569", "wsiSpan": "50",
                            "wsiParallelism": "485,569/50 = 9,711.38",
                            "wsiBound": "488,769/64 ≈ 7,637.02",
                            "wsiLower": "485,569/64 ≈ 7,587.02"}},
                {"id": "msort-1024-on-8", "label": "MERGE-SORT′ on 1,024 keys, 8 processors",
                 "program": "merge-sort", "n": "1024", "p": "8",
                 "expect": {"wsiWork": "11,264", "wsiSpan": "2,047",
                            "wsiParallelism": "11,264/2,047 ≈ 5.50",
                            "wsiBound": "3,455", "wsiLower": "2,047"}},
                {"id": "msort-1024-on-64", "label": "MERGE-SORT′ on 1,024 keys, 64 processors",
                 "program": "merge-sort", "n": "1024", "p": "64",
                 "expect": {"wsiBound": "2,223", "wsiLower": "2,047"}},
            ],
            "panel_title": "Work, span and the greedy bound",
            "panel_intro": (
                "Choose P-FIB or MERGE-SORT′, a size and a number of processors. The lab counts "
                "the work and the span exactly from the recurrences, sets the greedy bound "
                "beside the floor the work and span laws give, and prints the critical path. "
                "The table gives the figures at every size down that path."
            ),
        }),
        "steps_title": "Work and span by hand",
        "steps_intro": "Draw the graph first, even roughly; the measures are read off it.",
        "steps": [
            ("Mark the strands",
             "Split the procedure at every spawn, sync and return, and give each piece its "
             "cost."),
            ("Add everything for the work",
             "The work is the total cost of every strand, which is the running time of the "
             "serialization. Write it as a recurrence for a recursive procedure."),
            ("Take the costliest path for the span",
             "Add costs along each path. Where two subcomputations run in parallel, keep the "
             "larger span; where they run in series, add them."),
            ("Bound the time on P processors",
             "The floor is `max(T₁/P, T∞)` and a greedy scheduler stays under `T₁/P + T∞`. "
             "Divide the parallelism by P to get the slackness."),
            ("Do it at a size of your own",
             "Choose n = 12 for P-FIB and 16 processors, extend the worked table to get the "
             "work, span and greedy bound by hand, then set the lab to the same and check all "
             "three tiles."),
        ],
        "worked": {
            "title": "P-FIB(5), counted",
            "intro": [
                "Use the lab's counting: a call on n ≥ 2 is three unit strands, the one before the "
                "spawn, the one that makes the second call, and the one after the sync; a call "
                "on 0 or 1 is one strand.",
            ],
            "lines": [
                "work: W(n) = W(n − 1) + W(n − 2) + 3",
                "W: 1, 1, 5, 9, 17, 29 for n = 0 to 5",
                "span: S(n) = 2 + max(S(n − 1), 1 + S(n − 2))",
                "S: 1, 1, 4, 6, 8, 10 for n = 0 to 5",
                "P-FIB(5): work 29, span 10, parallelism 2.9",
            ],
            "after": [
                "The work grows like the Fibonacci numbers themselves, and the span by 2 a "
                "level. That gap is `Θ(φⁿ/n)` in the book's notation, here only 2.9 because n is "
                "5; at n = 10 the lab gives 17.65 and at n = 25 over 9,700.",
            ],
        },
        "quiz_title": "Work, span and schedules",
        "quiz": [
            {"q": "A computation has strands a (cost 2), b (5), c (3) and d (1), with edges a→b, "
                  "a→c, b→d and c→d. What is its span?",
             "a": ["8", "11", "6", "5.5"],
             "c": 0,
             "why": "The two paths are a, b, d at `2 + 5 + 1 = 8` and a, c, d at `2 + 3 + 1 = 6`; "
                    "the span is the costlier, 8. Eleven is the work, the sum of all four "
                    "strands. Six is the cheaper path, which bounds nothing. 5.5 is the work "
                    "split over two processors, the work-law floor for P = 2, not the span."},
            {"q": "A computation has work 1,200 and span 40. What does Theorem 27.1 guarantee "
                  "for a greedy scheduler on 10 processors?",
             "a": ["`T₁₀ ≤ 160`", "`T₁₀ ≤ 120`", "`T₁₀ ≤ 40`", "`T₁₀ = 30`"],
             "c": 0,
             "why": "The bound is `T₁/P + T∞ = 120 + 40 = 160`. 120 is the work-law floor "
                    "`T₁/P`, a lower bound that no schedule beats, not a guarantee. 40 is the span, "
                    "also a floor. 30 is the parallelism, 1,200/40, which limits the speedup, not "
                    "the time."},
            {"q": "Why is the parallelism of MERGE-SORT′, which spawns its two recursive calls "
                  "and then merges serially, only `Θ(lg n)`?",
             "a": ["The serial merge puts `Θ(n)` on the critical path, so the span is `Θ(n)`",
                   "Spawning the recursive calls doubles the work",
                   "The span is `Θ(n lg n)`, the same as the work",
                   "A greedy scheduler cannot use more than lg n processors"],
             "c": 0,
             "why": "The span obeys `T∞(n) = T∞(n/2) + Θ(n) = Θ(n)`, because the merge at each "
                    "level is serial and the top merge alone costs n. Work `Θ(n lg n)` over span "
                    "`Θ(n)` is `Θ(lg n)`. Spawning adds no work; the work is the serialization's. "
                    "The span is not `n lg n`: the halves run in parallel and only one of them "
                    "counts. The scheduler is not the limit; the computation is."},
            {"q": "In the lab, P-FIB(10) has parallelism 17.65. On 64 processors, what is the "
                  "most speedup any scheduler can achieve?",
             "a": ["17.65", "64", "32", "`353/64 ≈ 5.5`"],
             "c": 0,
             "why": "The span law gives `T₆₄ ≥ T∞`, so the speedup `T₁/T₆₄` is at most `T₁/T∞ = "
                    "17.65`. 64 would need a slackness of at least 1, and here it is about 0.28. "
                    "32 has no basis. 5.5 is the work per processor, a running time in units of "
                    "strand cost, not a speedup."},
        ],
        "mistakes": [
            ("Expecting every extra processor to help",
             "The span law caps the speedup at the parallelism, whatever P is. In the lab, "
             "MERGE-SORT′ on 1,024 keys has parallelism about 5.5: going from 8 to 64 processors "
             "lowers the greedy bound only from 3,455 to 2,223, and nothing can go below the "
             "span, 2,047. Past the parallelism, processors sit idle."),
            ("Thinking parallel code does less work",
             "The work is the running time of the serialization, so spawning reduces "
             "nothing; parallel versions often do a constant factor more. What changes is the "
             "span. P-MERGE has the same linear work as a serial merge and buys its "
             "`Θ(lg² n)` span with binary searches."),
            ("Letting parallel strands share a variable",
             "Two logically parallel strands that update the same location form a determinacy "
             "race, and the answer depends on the schedule. A race can pass every test run and "
             "fail on the next, so the chapter asks for strands that run in parallel to be "
             "independent, with results combined after the sync."),
        ],
        "standard": (
            "Finish when you can compute work, span and the greedy bound.",
            "Give work, span and parallelism for a small spawn-and-sync program and for P-FIB "
            "at a given n, state the work law, the span law and Theorem 27.1, and say why a "
            "serial merge limits merge sort's parallelism to `Θ(lg n)`."
        ),
        "note": (
            "The lab evaluates the recurrences exactly under its stated unit costs, and its "
            "greedy bound is Theorem 27.1's arithmetic, not a simulated schedule. It does not "
            "run P-MERGE or the matrix-multiplication algorithms, which the lesson carries by "
            "recurrence. A count at one n is a fact about that n; the Θ bounds are the book's "
            "proofs."
        ),
    },
    # ---------------------------------------------------------------- 02
    # CLRS 28.1-28.3, pp. 813-842. Quote: printed p. 813, 21 words,
    # quotes.py OK. Lesson total: 21 words. Lab: itakit/lup; the book's
    # 3 x 3 LUP-SOLVE example and its Figure 28.1-28.2 matrices are not used.
    # Numerical stability named (p. 813); inverse vs LUP (p. 815); PA = LU
    # and the two triangular solves (pp. 815-817); LU-DECOMPOSITION and the
    # Schur complement (pp. 819-821); pivoting on the largest absolute value,
    # pi, singular when a column is zero (pp. 822-826); 28.2 Theorems 28.1-28.2
    # (pp. 827-831); 28.3 SPD needs no pivoting (Corollary 28.6) and least
    # squares (pp. 832-839).
    {
        "slug": "solving-linear-systems",
        "title": "Solving Systems of Linear Equations",
        "module": "Chapter 28 · Matrix Operations",
        "one_line": "Factor the matrix once as PA = LU, by Gaussian elimination that swaps up the largest entry of each column, and every right-hand side is then two triangular solves away.",
        "summary": (
            "Section 28.1 solves `Ax = b` by an LUP decomposition: a permutation P, a unit "
            "lower-triangular L and an upper-triangular U with `PA = LU`, computed in `Θ(n³)` "
            "by elimination with pivoting, after which forward and back substitution solve "
            "for x in `Θ(n²)`. Sections 28.2 and 28.3 relate inversion to multiplication and "
            "treat symmetric positive-definite matrices and least squares. Decompose three "
            "matrices exactly in the lab, one of which cannot be done without a row exchange."
        ),
        "key": [
            "factor once: PA = LU",
            "L unit lower, U upper, P a permutation",
            "solve Ly = Pb forward, then Ux = y back",
            "each triangular solve costs Θ(n²)",
            "the factoring costs Θ(n³)",
            "pivot on the largest entry in the column",
            "no nonzero pivot left: singular",
        ],
        "key_label": "Section 28.1 in seven lines",
        "concepts_intro": (
            "Three ideas: the factorization, the entry it divides by, and the two cheap "
            "solves it makes possible."
        ),
        "concepts": [
            ("LUP decomposition",
             "Three n × n matrices with `PA = LU`: L is unit lower-triangular, with ones on the "
             "diagonal and zeros above; U is upper-triangular; P is a permutation matrix, "
             "stored as an array π in which `π[i]` names the row of A that becomes row i of PA. "
             "Every nonsingular matrix has one."),
            ("Pivot",
             "The entry elimination divides by at each step, the top-left entry of what is "
             "left of the matrix. A zero pivot is a division by zero and a tiny one magnifies "
             "rounding error, so LUP-DECOMPOSITION first swaps up the entry of largest absolute "
             "value in the current column."),
            ("Forward and back substitution",
             "A triangular system is solved one unknown at a time. With L lower-triangular, y₁ "
             "comes from the first equation, then y₂ from the second, and so on down; with U "
             "upper-triangular, xₙ comes first and the rest follow upward. Each costs `Θ(n²)`."),
        ],
        "read_title": "The chapter's argument first, then the arithmetic",
        "read_intro": (
            "Read section 28.1 closely and sections 28.2 and 28.3 for their results. The "
            "lesson sets out the decomposition and both substitutions in its own words, works "
            "one solve by hand, and decomposes matrices exactly in the lab."
        ),
        "body": [
            ("p", "&ldquo;Because operations on matrices lie at the heart of scientific "
                  "computing, efficient algorithms for working with matrices have many practical "
                  "applications.&rdquo; Chapter 28 takes up the most common of them, solving n "
                  "linear equations in n unknowns, and two relatives: inverting a matrix, and "
                  "fitting a curve by least squares. The authors flag numerical stability, the "
                  "way rounding errors can grow in floating point, as a real concern they "
                  "mostly leave to specialist texts. The lab here sidesteps it by computing in "
                  "exact fractions."),
            ("p", "Write the system as `Ax = b` with A nonsingular, so that x exists and is "
                  "unique. One could compute `A⁻¹` and multiply, but the authors point out that "
                  "this is numerically unstable in practice, and LUP decomposition is both "
                  "stable and faster. The plan is to find P, L and U with `PA = LU`. Multiplying "
                  "`Ax = b` by P permutes the equations, so `LUx = Pb`. Name `y = Ux`; solve "
                  "`Ly = Pb` for y by forward substitution, then `Ux = y` for x by back "
                  "substitution. LUP-SOLVE is those two loops, `Θ(n²)` in all."),
            ("thm", ("Forward and back substitution",
                     "With L unit lower-triangular, `yᵢ = b[π[i]] − (lᵢ₁·y₁ + … + lᵢ,ᵢ₋₁·yᵢ₋₁)` "
                     "for i from 1 up to n. With U upper-triangular, "
                     "`xᵢ = (yᵢ − (uᵢ,ᵢ₊₁·xᵢ₊₁ + … + uᵢₙ·xₙ))/uᵢᵢ` for i from n down to 1. Each "
                     "unknown costs one pass over a row, so each solve is `Θ(n²)`.")),
            ("p", "The factoring is Gaussian elimination, written recursively. Split A into "
                  "its top-left entry a₁₁, the rest of the first column v, the rest of the first "
                  "row wᵀ, and the remaining `(n − 1) × (n − 1)` block A′. Then the first column "
                  "of L is v divided by a₁₁, the first row of U is a₁₁ followed by wᵀ, and what "
                  "remains to factor is the Schur complement `A′ − v·wᵀ/a₁₁`: A′ with a multiple "
                  "of the first row subtracted from each later row to clear the first column. "
                  "LU-DECOMPOSITION repeats this on the Schur complement, `Θ(n³)` in all, and "
                  "can store L and U in place of A."),
            ("p", "The recursion divides by a₁₁. If it is zero the method fails even when A is "
                  "nonsingular, and if it is small the division magnifies rounding error. "
                  "LUP-DECOMPOSITION therefore exchanges rows before each step, bringing up the "
                  "entry of greatest absolute value in the current column, and records the "
                  "exchange in π. If every candidate in the column is zero, the matrix is "
                  "singular and the procedure says so. The authors show that the Schur "
                  "complement of a nonsingular matrix is nonsingular, so the recursion never "
                  "runs out of pivots on a nonsingular input. The cost is still `Θ(n³)`."),
            ("example", ("A zero in the corner",
                         "Take `A = [[0, 2], [3, 1]]` and `b = (4, 5)`. Elimination without a row "
                         "exchange would divide by 0. With the exchange, `π = 2, 1`, PA is "
                         "`[[3, 1], [0, 2]]`, which is already upper-triangular, so `L = I` and "
                         "`U = [[3, 1], [0, 2]]`. Then `Pb = (5, 4)`, forward substitution gives "
                         "`y = (5, 4)`, and back substitution gives `x₂ = 4/2 = 2` and "
                         "`x₁ = (5 − 1·2)/3 = 1`.")),
            ("p", "Section 28.2 asks how inversion compares with multiplication. Inverting A "
                  "with an LUP decomposition means solving `Ax = eᵢ` for each column eᵢ of the "
                  "identity: one `Θ(n³)` factoring and n solves of `Θ(n²)`, `Θ(n³)` in all. "
                  "Theorems 28.1 and 28.2 then show that, under mild regularity conditions, "
                  "multiplying and inverting n × n matrices have the same asymptotic cost, so a "
                  "faster multiplication such as Strassen's gives a faster inversion."),
            ("p", "Section 28.3 treats symmetric positive-definite matrices, those with "
                  "`xᵀAx > 0` for every nonzero x. Their Schur complements are again symmetric "
                  "positive-definite, so LU decomposition never divides by zero and needs no "
                  "pivoting (Corollary 28.6). The section ends with least squares: given more "
                  "data points than unknowns, choose the coefficients c that minimize the "
                  "squared error, which leads to the normal equations `AᵀA·c = Aᵀy`. When A has "
                  "full column rank, `AᵀA` is symmetric positive-definite, and the earlier "
                  "machinery solves them."),
            ("p", "Now the lab. It runs LUP-DECOMPOSITION in exact rational arithmetic, "
                  "choosing the largest absolute value in each column and the first on a tie, "
                  "and, given b, runs LUP-SOLVE and checks `Ax = b` exactly. Matrices are typed "
                  "row by row, one row a line; the entries are whole numbers or decimals, and "
                  "every result is a fraction. Its tiles are π, the pivots in order, L and U "
                  "row by row with rows separated by semicolons, the determinant, the solution "
                  "and the check."),
            ("p", "The lesson's matrix, preset three, is `[[1, 3, 2], [2, 2, 5], [4, 1, 3]]` "
                  "with `b = (1, 7, 10)`. The lab reports `π = 3, 1, 2`, pivots `4, 11/4, 31/11`, "
                  "L with rows `1, 0, 0; 1/4, 1, 0; 1/2, 6/11, 1`, U with rows "
                  "`4, 1, 3; 0, 11/4, 5/4; 0, 0, 31/11`, determinant 31 and `x = 2, −1, 1`, "
                  "checked exactly. Preset zero is the example above: `π = 2, 1` and "
                  "`x = 1, 2`. Preset four is a 4 × 4 system whose solution is all ones; "
                  "its third pivot is `−2/3`, negative, because the rule compares absolute "
                  "values."),
            ("p", "The determinant tile uses a fact the decomposition gives for free: "
                  "`det A` is the product of the pivots, with its sign changed once for each "
                  "row exchange. For preset three, `4 · 11/4 · 31/11 = 31`, and π is a cycle "
                  "of three rows, made by two exchanges, so the sign stays. Type a singular "
                  "matrix such as `[[1, 2], [2, 4]]` and the lab refuses it, naming the column "
                  "that has no nonzero pivot."),
            ("h3", "Exercise"),
            ("p", "By hand, find the LUP decomposition of `[[1, 2, 2], [4, 4, 2], [2, 6, 4]]` "
                  "with partial pivoting, then solve for `b = (3, 4, 4)` by forward and back "
                  "substitution. Type the matrix and b into the lab, one row a line, and check "
                  "π, L, U and x."),
            ("p", "The next lesson, Linear Programming and the Simplex Algorithm, solves "
                  "systems of inequalities rather than equations, and its pivot step turns out "
                  "to be a cousin of the elimination step here."),
        ],
        "lab": ("itakit", {
            "mode": "lup",
            "view": "decompose",
            "preset": "three",
            "presets": [
                {"id": "three", "label": "Three equations that need two row exchanges",
                 "matrix": "1 3 2\n2 2 5\n4 1 3", "b": "1 7 10",
                 "expect": {"luiPerm": "π = 3, 1, 2", "luiPivots": "4, 11/4, 31/11",
                            "luiL": "1, 0, 0; 1/4, 1, 0; 1/2, 6/11, 1",
                            "luiU": "4, 1, 3; 0, 11/4, 5/4; 0, 0, 31/11",
                            "luiDet": "31", "luiX": "x = 2, −1, 1",
                            "luiCheck": "yes: A·x = b exactly"}},
                {"id": "zero", "label": "A zero in the corner",
                 "matrix": "0 2\n3 1", "b": "4 5",
                 "expect": {"luiPerm": "π = 2, 1", "luiL": "1, 0; 0, 1",
                            "luiU": "3, 1; 0, 2", "luiX": "x = 1, 2"}},
                {"id": "four", "label": "Four equations whose solution is all ones",
                 "matrix": "2 1 0 3\n4 2 1 7\n-2 3 5 1\n6 3 2 8", "b": "6 14 7 19",
                 "expect": {"luiPerm": "π = 4, 3, 1, 2", "luiPivots": "6, 4, −2/3, 3/2",
                            "luiDet": "24", "luiX": "x = 1, 1, 1, 1"}},
            ],
            "panel_title": "Factor PA = LU, then solve",
            "panel_intro": (
                "Type a square matrix row by row, one row a line, and optionally a right-hand "
                "side b. The lab pivots on the largest absolute value in each column, prints "
                "π, L and U as exact fractions, and solves by forward and back substitution, "
                "checking the answer against A."
            ),
        }),
        "steps_title": "An LUP solve by hand",
        "steps_intro": "Keep π beside the matrix; every row exchange is recorded there.",
        "steps": [
            ("Choose the pivot",
             "In the current column, on and below the diagonal, find the entry of largest "
             "absolute value and swap its whole row up, recording the swap in π. If all are "
             "zero, stop: the matrix is singular."),
            ("Eliminate below it",
             "For each row below, the multiplier is its entry divided by the pivot. Store the "
             "multiplier as the entry of L, and subtract the multiplier times the pivot row "
             "from the rest of that row."),
            ("Repeat on the smaller block",
             "Move one row down and one column right and do the same until the last pivot. "
             "What is left on and above the diagonal is U."),
            ("Solve the two triangles",
             "Permute b by π, solve `Ly = Pb` from the top down, then `Ux = y` from the bottom "
             "up, and substitute x back into the original equations."),
            ("Do it on a system of your own",
             "Write a 3 × 3 matrix of your own with a 0 in the top-left corner, choose an "
             "integer x, compute b = Ax, and check that the lab recovers your x and swaps the "
             "row you expected."),
        ],
        "worked": {
            "title": "The lesson's system, solved from its factors",
            "intro": [
                "Use the factors the lab prints for preset three and solve for "
                "`b = (1, 7, 10)`.",
            ],
            "lines": [
                "Pb = (b₃, b₁, b₂) = (10, 1, 7)",
                "y₁ = 10",
                "y₂ = 1 − (1/4)·10 = −3/2",
                "y₃ = 7 − (1/2)·10 − (6/11)·(−3/2) = 31/11",
                "x₃ = (31/11)/(31/11) = 1",
                "x₂ = (−3/2 − (5/4)·1)/(11/4) = −1",
                "x₁ = (10 − 1·(−1) − 3·1)/4 = 2",
            ],
            "after": [
                "Six short steps once the factors are known, against a fresh elimination for "
                "each new b. That is why the factoring, `Θ(n³)`, is done once and reused: each "
                "further right-hand side costs only `Θ(n²)`.",
            ],
        },
        "quiz_title": "Pivots, factors and substitutions",
        "quiz": [
            {"q": "LUP-DECOMPOSITION factors `A = [[1, 3], [2, 8]]`. What is the bottom-right "
                  "entry of U?",
             "a": ["−1", "2", "1", "−1/2"],
             "c": 0,
             "why": "The larger entry of the first column is 2, so the rows swap: PA is "
                    "`[[2, 8], [1, 3]]`, the multiplier is 1/2, and `u₂₂ = 3 − (1/2)·8 = −1`. "
                    "2 is what elimination without the swap gives, `8 − 2·3`; it is a valid LU "
                    "factor of A itself but not what the pivoting procedure produces. −1/2 "
                    "confuses the multiplier with the pivot; 1 has no derivation."},
            {"q": "You must solve `Ax = b` for the same n × n matrix A and k different "
                  "right-hand sides, with k much smaller than n. With an LUP decomposition, "
                  "what does it cost?",
             "a": ["`Θ(n³ + k·n²)`", "`Θ(k·n³)`", "`Θ(n³·k²)`", "`Θ(k·n²)` with no other term"],
             "c": 0,
             "why": "The decomposition is done once in `Θ(n³)`, and each right-hand side then "
                    "costs two triangular solves of `Θ(n²)`. Refactoring for each b would be "
                    "`Θ(k·n³)`, which is the waste the method avoids. `Θ(k·n²)` alone forgets the "
                    "factoring, which dominates when k is smaller than n."},
            {"q": "During LUP-DECOMPOSITION the current column holds −7, 3 and 5 on and below "
                  "the diagonal. Which entry becomes the pivot?",
             "a": ["−7", "5", "3", "Whichever is on the diagonal, as long as it is nonzero"],
             "c": 0,
             "why": "The rule compares absolute values, and |−7| = 7 is the largest, so −7's row "
                    "is swapped up even though 5 is the largest number. Taking the first nonzero "
                    "entry avoids division by zero but not division by a small number, which is "
                    "the instability the rule exists to prevent. 3 is neither largest nor "
                    "first."},
            {"q": "In solving `LUx = Pb`, what does forward substitution compute?",
             "a": ["`y = Ux`, from `Ly = Pb`, first unknown first",
                   "x, from `Ux = y`, last unknown first",
                   "x, from `Ly = b` with b unpermuted",
                   "`A⁻¹`, one column at a time"],
             "c": 0,
             "why": "L is lower-triangular, so its system is solved from the top: y₁ from the "
                    "first equation, then y₂, and so on. The last-unknown-first solve is back "
                    "substitution on U, the second step. Using b without applying π solves a "
                    "different system whenever rows were exchanged. Inversion needs n such "
                    "solves and is not what one forward pass does."},
        ],
        "mistakes": [
            ("Expecting elimination to work without row exchanges",
             "LU decomposition without pivoting divides by the top-left entry, and a "
             "nonsingular matrix can have 0 there. Preset zero, `[[0, 2], [3, 1]]`, is "
             "invertible with determinant −6 and cannot be factored as LU at all; one row "
             "exchange fixes it. Only some classes, such as symmetric positive-definite "
             "matrices, are safe without pivoting."),
            ("Solving by computing the inverse",
             "`x = A⁻¹b` is correct algebra and poor computing. The authors note it is "
             "numerically unstable in practice, and it is no faster: the inverse itself costs "
             "an LUP decomposition plus n solves. Keep the factors and solve two triangular "
             "systems for each b."),
            ("Forgetting to permute b",
             "The factors describe PA, not A, so the right-hand side must be permuted the same "
             "way before forward substitution. Solving `Ly = b` with the original order gives "
             "the solution of a different system, and nothing in the arithmetic signals the "
             "mistake until x is substituted back into `Ax = b`."),
        ],
        "standard": (
            "Finish when you can factor and solve a small system by hand.",
            "Compute an LUP decomposition of a 3 × 3 matrix with partial pivoting, solve "
            "`Ax = b` from the factors, say what each step costs, and explain why the "
            "pivot is the entry of largest absolute value."
        ),
        "note": (
            "The lab computes in exact fractions, so it cannot show the rounding error that "
            "makes pivoting matter in floating point; the lesson states that reason from the "
            "chapter. It does not compute inverses or least-squares fits, which sections 28.2 "
            "and 28.3 cover. The `Θ(n³)` and `Θ(n²)` costs are the book's analysis, not "
            "something the lab measures."
        ),
    },
    # ---------------------------------------------------------------- 03
    # CLRS 29.1-29.3, pp. 843-879. Quote: printed p. 843, 17 words,
    # quotes.py OK. Lesson total: 17 words. Lab: simplex/walk, kit preset
    # `plants` (the simplex kit takes no programme from a lesson; reported as
    # a kit gap). The book's campaign data and its worked simplex example are
    # not used. LP defined, no strict inequalities (pp. 845-846); convex
    # region, optimum at a vertex, the walk along edges (pp. 846-849);
    # ellipsoid and interior-point methods named (p. 850); standard form and
    # the four conversions (pp. 850-855); slack form (pp. 855-857); 29.2
    # formulations named (pp. 859-864); basic solution, pivot, PIVOT
    # (pp. 864-870); SIMPLEX's choices, unboundedness, degeneracy and
    # cycling, Lemmas 29.4-29.7, Bland's rule (pp. 871-878).
    {
        "slug": "linear-programming-and-the-simplex-algorithm",
        "title": "Linear Programming and the Simplex Algorithm",
        "module": "Chapter 29 · Linear Programming",
        "one_line": "A linear program is written in slack form, where basic variables are expressed in terms of nonbasic ones; the simplex algorithm pivots one variable in and one out at a time, walking from corner to neighbouring corner until no objective coefficient is positive.",
        "summary": (
            "Sections 29.1 to 29.3: what a linear program is, how any one is rewritten in "
            "standard form and then slack form, and how the simplex algorithm moves between "
            "basic solutions by pivoting until the objective can rise no further. The section "
            "ends by showing that the algorithm can only fail to stop by cycling, and that "
            "breaking ties by smallest index prevents it. Walk a two-product programme from the "
            "origin to its optimum in the lab and try a jump that is not an edge."
        ),
        "key": [
            "maximize a linear objective, linear limits",
            "standard form: max cᵀx, Ax ≤ b, x ≥ 0",
            "slack form: basics in terms of nonbasics",
            "basic solution: nonbasic variables at 0",
            "pivot: tightest row decides who leaves",
            "stop when no coefficient in z is positive",
            "at most C(n + m, m) slack forms",
        ],
        "key_label": "Sections 29.1 to 29.3 in seven lines",
        "concepts_intro": (
            "Three ideas: the two forms a program is written in, the point each form stands "
            "for, and the step that moves between forms."
        ),
        "concepts": [
            ("Standard and slack forms",
             "Standard form maximizes `cᵀx` subject to `Ax ≤ b` and `x ≥ 0`. Slack form gives "
             "each inequality a slack variable, the room left in it, and writes the program as "
             "equations: each basic variable on the left, expressed in terms of the nonbasic "
             "variables on the right, with the objective written the same way."),
            ("Basic solution",
             "The point a slack form names when every nonbasic variable is set to 0: each basic "
             "variable then equals the constant in its equation. It is a corner of the "
             "feasible region when all those constants are nonnegative, and the objective's "
             "constant is its value."),
            ("Pivot",
             "Exchange one nonbasic variable, the entering one, for one basic variable, the "
             "leaving one. The entering variable has a positive objective coefficient; the "
             "leaving one is the basic variable whose equation limits the increase most "
             "tightly. Solving that equation for the entering variable and substituting gives "
             "an equivalent slack form."),
        ],
        "read_title": "The chapter's argument first, then the walk",
        "read_intro": (
            "Read the chapter's introduction and sections 29.1 to 29.3 in your own copy; skim "
            "29.2's formulations. The lesson sets out the forms and the pivot in its own words, "
            "walks a small programme by hand in slack form, and then watches the same walk in "
            "the lab."
        ),
        "body": [
            ("p", "&ldquo;Many problems take the form of maximizing or minimizing an objective, "
                  "given limited resources and competing constraints.&rdquo; Chapter 29 opens "
                  "with a campaign deciding how to spend on advertising, and turns it into the "
                  "general problem: optimize a linear function of some variables subject to "
                  "linear equalities and inequalities, with strict inequalities not allowed. "
                  "This lesson reads sections 29.1 to 29.3, the two standard ways of writing such "
                  "a program and the simplex algorithm that solves it; the next lesson reads "
                  "duality and how the algorithm gets started."),
            ("p", "In two variables a program can be drawn. Each constraint is a half-plane, "
                  "their intersection is a convex region, and the lines on which the objective is "
                  "constant are parallel; sliding the line as far as it goes while still "
                  "touching the region ends at a corner, or along an edge whose two ends are "
                  "both corners. The same holds in n dimensions, and the simplex algorithm "
                  "exploits it: start at a corner, move along an edge to a neighbouring corner "
                  "no worse than the current one, and stop at a corner none of whose neighbours "
                  "is better, which convexity makes a global optimum. The method is not "
                  "polynomial in the worst case, the authors note, but is fast in practice; the "
                  "ellipsoid and interior-point methods are polynomial and are only named."),
            ("p", "Section 29.1 fixes a standard form: maximize `cᵀx` subject to `Ax ≤ b` and "
                  "`x ≥ 0`. A program can miss it in four ways, and each has a repair. A "
                  "minimization becomes a maximization by negating the objective. A variable "
                  "with no sign constraint is replaced by the difference of two nonnegative ones. "
                  "An equality becomes two opposite inequalities. A greater-than constraint is "
                  "multiplied by −1. Each repair gives an equivalent program, one with the same "
                  "optimal value and solutions that translate back."),
            ("example", ("Four repairs on one program",
                         "Minimize `2x₁ − x₂` subject to `x₁ + x₂ = 5`, `x₁ − 3x₂ ≥ −4`, "
                         "`x₁ ≥ 0`, with x₂ free. Negate the objective: maximize `−2x₁ + x₂`. "
                         "Replace x₂ by `x₂′ − x₂″` with both nonnegative. Split the equality into "
                         "`x₁ + x₂′ − x₂″ ≤ 5` and `−x₁ − x₂′ + x₂″ ≤ −5`. Multiply the other "
                         "constraint by −1: `−x₁ + 3x₂′ − 3x₂″ ≤ 4`. The result is in standard "
                         "form, with three variables and three constraints.")),
            ("p", "Slack form comes next. For each constraint `aᵢ·x ≤ bᵢ` define a slack "
                  "variable `sᵢ = bᵢ − aᵢ·x`, required to be nonnegative, so that the inequality "
                  "becomes an equation. The program is then a set of equations with the basic "
                  "variables, at first the slacks, on the left, each expressed in terms of the "
                  "nonbasic variables on the right, and an objective `z = v + Σ cⱼxⱼ` written "
                  "in the nonbasic variables too. Section 29.2 then formulates shortest paths, "
                  "maximum flow, minimum-cost flow and multicommodity flow as linear programs, "
                  "which is worth reading for how constraints express a graph problem."),
            ("p", "Section 29.3's simplex algorithm works on slack forms. Set the nonbasic "
                  "variables to 0 and read off the basic solution. If some nonbasic variable "
                  "has a positive coefficient in z, raising it raises z; raise it until the "
                  "first basic variable reaches 0. That basic variable leaves, the nonbasic one "
                  "enters, and PIVOT rewrites every equation with the new choice: solve the "
                  "leaving variable's equation for the entering one and substitute everywhere. "
                  "If no equation limits the entering variable, the program is unbounded. If no "
                  "objective coefficient is positive, the basic solution is optimal, a claim the "
                  "next lesson proves by duality."),
            ("math", [
                "the lesson's program: maximize z = 3x₁ + 5x₂",
                "subject to  x₁ ≤ 4,  2x₂ ≤ 12,  3x₁ + 2x₂ ≤ 18,  x ≥ 0",
                "",
                "slack form:",
                "z  = 0 + 3x₁ + 5x₂",
                "s₁ = 4 − x₁",
                "s₂ = 12 − 2x₂",
                "s₃ = 18 − 3x₁ − 2x₂",
                "basic solution: x₁ = x₂ = 0, z = 0",
            ]),
            ("p", "Choose x₂ to enter; its coefficient, 5, is positive. The equation for s₁ does "
                  "not contain x₂, so it sets no limit; s₂ reaches 0 at `x₂ = 6`; s₃ at `x₂ = 9`. "
                  "The tightest is s₂, which leaves. Solving its equation gives "
                  "`x₂ = 6 − s₂/2`, and substituting gives `z = 30 + 3x₁ − (5/2)·s₂` and "
                  "`s₃ = 6 − 3x₁ + s₂`. The new basic solution is `(x₁, x₂) = (0, 6)` with "
                  "`z = 30`. One coefficient in z, that of x₁, is still positive, so the walk "
                  "goes on; the worked example below finishes it."),
            ("p", "Can the walk go on forever? A pivot can leave z unchanged when the leaving "
                  "variable's constant is already 0, a situation called degeneracy, and a run of "
                  "such pivots can return to a slack form it has seen, which is cycling. The "
                  "authors show that the set of basic variables determines the slack form "
                  "uniquely (Lemma 29.4), so there are at most `C(n + m, m)` slack forms, and "
                  "SIMPLEX either stops within that many iterations or cycles (Lemma 29.5). "
                  "Breaking ties by the smallest index, Bland's rule, prevents cycling; the book "
                  "states this as Lemma 29.6 and omits the proof."),
            ("p", "Now the lab, the one the Operations Research Subject's lesson Adjacent "
                  "Corners and the Simplex Idea uses, where the tableau lessons that follow it "
                  "carry the arithmetic further. It cannot take a programme typed in; its "
                  "worked examples are built in, and the lesson's program is its first, two "
                  "products across three plants. It draws the region, lists every corner with "
                  "the basis that stands there, and prints the walk the method takes from the "
                  "slack basis. Its tiles are the basis at the chosen corner, the objective "
                  "there, the columns exchanged by a move to another corner, and the verdict on "
                  "the move."),
            ("p", "On the lesson's program the region has 5 corners and the walk visits 3 of "
                  "them in 2 pivots: x₂ in and s₂ out to `(0, 6)` at 30, then x₁ in and s₃ out to "
                  "`(2, 6)` at 36. Ask to move from `(0, 0)` to `(4, 3)` and the lab refuses: the "
                  "two bases, `{s₁, s₂, s₃}` and `{x₁, s₂, x₂}`, differ in two columns, and a "
                  "pivot exchanges one. Its entering rule takes the largest positive "
                  "coefficient, one of the choices SIMPLEX allows. Set the objective "
                  "coefficients to 5 and 1 and the walk changes to `(0, 0)`, `(4, 0)`, `(4, 3)`, "
                  "ending at 23."),
            ("p", "The lab prints its bases in tableau language, a grid of coefficients in "
                  "which the objective row holds the negated coefficients, so an improving "
                  "column shows a negative entry there. That is the same information as the "
                  "book's slack form with the opposite sign convention: a positive coefficient "
                  "in the book's z is a negative entry in the tableau's last row."),
            ("h3", "Exercise"),
            ("p", "Change the objective to `2x₁ + 3x₂` on the same constraints. By hand, in slack "
                  "form, choose the variable with the larger coefficient to enter, run the "
                  "pivots to the end, and write each basic solution and the final value of z. "
                  "Then set the lab's objective coefficients to 2 and 3 and compare its walk "
                  "with yours."),
            ("p", "The walk stopped because no coefficient in z was positive. The next lesson, "
                  "Duality and the Initial Basic Feasible Solution, proves that this really is "
                  "optimal, and shows how to start when the origin is not feasible."),
        ],
        "lab": ("simplex", {
            "mode": "walk",
            "preset": "plants",
            "panel_title": "Walk from corner to adjacent corner",
            "panel_intro": (
                "The first worked example is the lesson's program. Choose two corners and ask "
                "for the move: two corners are adjacent exactly when their bases differ in one "
                "column, and the table below prints the walk the method takes from the origin. "
                "Change the two objective coefficients and watch the walk change."
            ),
        }),
        "steps_title": "A simplex walk by hand",
        "steps_intro": "Write the slack form out in full before the first pivot.",
        "steps": [
            ("Put the program in standard form",
             "Negate a minimization, split free variables and equalities, and flip "
             "greater-than rows, until it reads maximize `cᵀx`, `Ax ≤ b`, `x ≥ 0`."),
            ("Write the slack form",
             "One slack per row, `sᵢ = bᵢ − aᵢ·x`, and `z` in terms of the original variables. "
             "Read the basic solution by setting every right-hand variable to 0."),
            ("Choose who enters and who leaves",
             "Take a variable with a positive coefficient in z. For each equation, find how far "
             "it can rise before that basic variable hits 0; the smallest limit names the "
             "leaving variable. No limit at all means unbounded."),
            ("Pivot and repeat",
             "Solve the leaving equation for the entering variable, substitute into every "
             "other equation and into z, and read the new basic solution. Stop when no "
             "coefficient in z is positive."),
            ("Do it on an objective of your own",
             "Pick objective coefficients of your own between 1 and 9 for the lab's program, "
             "predict by hand which corner is optimal and how many pivots the walk takes, "
             "then set them in the lab and check."),
        ],
        "worked": {
            "title": "The walk finished",
            "intro": [
                "Continue from the slack form after the first pivot, with x₁ entering.",
            ],
            "lines": [
                "z  = 30 + 3x₁ − (5/2)·s₂",
                "s₁ = 4 − x₁;  x₂ = 6 − s₂/2;  s₃ = 6 − 3x₁ + s₂",
                "limits on x₁: s₁ at 4, s₃ at 2, x₂ none: s₃ leaves",
                "x₁ = 2 + s₂/3 − s₃/3",
                "z  = 36 − (3/2)·s₂ − s₃",
                "s₁ = 2 − s₂/3 + s₃/3",
                "basic solution: (x₁, x₂) = (2, 6), s₁ = 2, z = 36",
            ],
            "after": [
                "Both coefficients left in z are negative, so the walk stops at 36, the corner "
                "the lab reaches. The slack s₁ = 2 says the first plant has two hours to spare. "
                "Keep the final objective line: its coefficients, 3/2 on s₂ and 1 on s₃, "
                "return in the next lesson as the optimal dual solution.",
            ],
        },
        "quiz_title": "Forms, pivots and stopping",
        "quiz": [
            {"q": "A program asks you to minimize `2x₁ − x₂`. What objective does its standard "
                  "form maximize?",
             "a": ["`−2x₁ + x₂`", "`2x₁ − x₂`", "`2x₂ − x₁`", "`1/(2x₁ − x₂)`"],
             "c": 0,
             "why": "Minimizing f is maximizing −f, and the negation of `2x₁ − x₂` is "
                    "`−2x₁ + x₂`. Maximizing `2x₁ − x₂` itself solves the opposite problem. "
                    "`2x₂ − x₁` negates but also swaps the two coefficients, which changes the "
                    "problem. A reciprocal is not linear."},
            {"q": "In the slack form `z = 30 + 3x₁ − (5/2)·s₂`, `s₁ = 4 − x₁`, `x₂ = 6 − s₂/2`, "
                  "`s₃ = 6 − 3x₁ + s₂`, x₁ enters. Which variable leaves?",
             "a": ["s₃", "s₁", "x₂", "s₂"],
             "c": 0,
             "why": "With the other nonbasic variable, s₂, held at 0, s₁ reaches 0 at `x₁ = 4` "
                    "and s₃ at `x₁ = 2`; x₂'s equation has no x₁ and sets no limit. The tightest "
                    "is s₃. Letting s₁ leave would push x₁ to 4 and make `s₃ = −6`, outside the "
                    "region. s₂ is nonbasic, so it cannot leave."},
            {"q": "When does SIMPLEX conclude that its basic solution is optimal?",
             "a": ["When no nonbasic variable has a positive coefficient in the objective",
                   "When a pivot leaves the objective value unchanged",
                   "When every basic variable is strictly positive",
                   "After m pivots, one per constraint"],
             "c": 0,
             "why": "If every coefficient in z is zero or negative, raising any nonbasic "
                    "variable cannot raise z, and Theorem 29.10 proves the point optimal. A "
                    "pivot that leaves z unchanged is degeneracy, which can happen well before "
                    "the optimum. Positive basic variables say only that the point is not "
                    "degenerate. The number of pivots is not fixed at m; the lesson's walk takes "
                    "2 on 3 constraints."},
            {"q": "For a program with n = 2 variables and m = 3 constraints, how many slack "
                  "forms can SIMPLEX possibly visit, by Lemma 29.5's count?",
             "a": ["At most 10", "Exactly 5, one per corner", "At most 6", "At most 32"],
             "c": 0,
             "why": "A slack form is determined by its m basic variables chosen from n + m = 5, "
                    "and `C(5, 3) = 10`. The lesson's region has 5 corners, but the count is "
                    "over choices of basis, some of which are infeasible, so 5 is what one "
                    "program happens to have, not the lemma's bound. 6 is 3!, and 32 is 2⁵, "
                    "every subset of the five variables."},
        ],
        "mistakes": [
            ("Thinking the simplex method tries every corner",
             "It walks: each pivot moves to an adjacent corner no worse than the last, and it "
             "stops at the first corner with no improving edge. On the lesson's program, it "
             "visits 3 of the 5 corners. The `C(n + m, m)` count is the worst case the analysis "
             "allows, not what a run does, and no jump between corners that are not adjacent "
             "is ever made."),
            ("Stopping because the objective did not rise",
             "A degenerate pivot changes the basis without changing the point, so z can stay "
             "put for one or several pivots and then rise again. The stopping test is the signs "
             "of the coefficients in z, not the change in its value."),
            ("Choosing the leaving variable by the largest coefficient",
             "The leaving variable is fixed by the tightest limit, the smallest ratio of "
             "constant to coefficient among equations that limit the entering variable. Any "
             "other choice drives some basic variable below 0: in the worked example, letting "
             "s₁ leave instead of s₃ would give `s₃ = −6`."),
        ],
        "standard": (
            "Finish when you can carry a small program through the simplex algorithm.",
            "Convert a program to standard form, write its slack form, choose entering and "
            "leaving variables correctly, pivot to the optimum, and say when the algorithm "
            "stops, when it reports unboundedness and why cycling is the only way it can "
            "fail to stop."
        ),
        "note": (
            "The lab's simplex kit runs only its built-in programs, so the lesson's program is "
            "its first worked example rather than one written for the lesson, and it chooses "
            "the entering variable by the largest coefficient. The walk on one program shows "
            "how pivots move; the `C(n + m, m)` bound and the correctness of stopping are the "
            "book's proofs."
        ),
    },
    # ---------------------------------------------------------------- 04
    # CLRS 29.4-29.5, pp. 879-897. Quote: printed p. 879, 11 words,
    # quotes.py OK. Lesson total: 11 words. Lab: duality/certificate, kit
    # preset workshop, which is the same program as the simplex kit's
    # `plants` and lesson 3's. The book's dual example and its L_aux example
    # are not used. Duality via max-flow min-cut (p. 879); forming the dual
    # (p. 880); Lemma 29.8 and Corollary 29.9 (pp. 880-881); Theorem 29.10
    # and y from the final slack form, equation (29.91) (pp. 881-884);
    # INITIALIZE-SIMPLEX, L_aux, Lemma 29.11 (pp. 886-887); the first pivot,
    # the degenerate pivot, Lemma 29.12 (pp. 887-891); Theorem 29.13
    # (p. 892).
    {
        "slug": "duality-and-the-initial-solution",
        "title": "Duality and the Initial Basic Feasible Solution",
        "module": "Chapter 29 · Linear Programming",
        "one_line": "Every linear program has a dual whose feasible solutions bound it, the simplex algorithm's last slack form hands over a dual solution that meets the bound, and an auxiliary program with one extra variable finds a feasible start or proves there is none.",
        "summary": (
            "Section 29.4 builds the dual of a maximization program, proves that any feasible "
            "dual solution bounds every feasible primal one from above, and reads an optimal "
            "dual solution off SIMPLEX's final slack form, which proves the algorithm's answer "
            "optimal. Section 29.5 handles programs whose origin is infeasible with an "
            "auxiliary program L_aux and proves the fundamental theorem: every program is "
            "infeasible, unbounded, or has a finite optimum. Bracket the last lesson's optimum "
            "with plans and prices in the lab until the bracket closes."
        ),
        "key": [
            "dual: min bᵀy, Aᵀy ≥ c, y ≥ 0",
            "weak duality: cᵀx ≤ bᵀy, always",
            "equal values certify both optimal",
            "the final slack form gives an optimal y",
            "L_aux: maximize −x₀, add −x₀ to each row",
            "L feasible exactly when L_aux reaches 0",
            "infeasible, unbounded, or optimal",
        ],
        "key_label": "Sections 29.4 and 29.5 in seven lines",
        "concepts_intro": (
            "Three ideas: the second program every program carries, the inequality between "
            "them, and the program that finds a place to start."
        ),
        "concepts": [
            ("Dual linear program",
             "For the primal program, maximize `cᵀx` subject to `Ax ≤ b` and `x ≥ 0`, the dual "
             "minimizes `bᵀy` subject to `Aᵀy ≥ c` and `y ≥ 0`: one variable per primal "
             "constraint, one constraint per primal variable, the objective and right-hand "
             "side exchanged. The dual of the dual is the primal."),
            ("Weak duality",
             "Lemma 29.8: for any feasible x of the primal and any feasible y of the dual, "
             "`cᵀx ≤ bᵀy`. A feasible y is therefore a certificate that no plan earns more "
             "than `bᵀy`, and a pair with equal values proves both optimal (Corollary 29.9)."),
            ("Auxiliary program",
             "L_aux adds one variable x₀ ≥ 0, subtracts it from the left side of every "
             "constraint, and maximizes −x₀. With x₀ large enough every constraint holds, so "
             "L_aux always has a feasible start, and its optimum is 0 exactly when the original "
             "program L is feasible (Lemma 29.11)."),
        ],
        "read_title": "The chapter's argument first, then the certificate",
        "read_intro": (
            "Read sections 29.4 and 29.5 in your own copy first. The lesson sets out the dual "
            "and both proofs in its own words, brackets the last lesson's optimum in the lab, "
            "and runs the auxiliary program by hand on a program written for the lesson."
        ),
        "body": [
            ("p", "&ldquo;Duality enables us to prove that a solution is indeed optimal.&rdquo; "
                  "The last lesson's walk stopped when no coefficient in z was positive, and "
                  "Section 29.4 is where the authors prove that stopping there is right. They "
                  "point back to Chapter 26 for the pattern: a flow is shown to be maximum by a "
                  "cut of the same value, a minimization problem paired with the maximization. "
                  "Section 29.5 then removes the last assumption of Section 29.3, that the "
                  "program starts at a feasible corner."),
            ("p", "The dual of a program in standard form is built mechanically. Give each "
                  "primal constraint a nonnegative variable yᵢ; minimize `bᵀy`; and for each "
                  "primal variable xⱼ write one constraint saying that the yᵢ weighted by column "
                  "j of A add up to at least cⱼ. In words, the dual looks for nonnegative "
                  "multipliers of the constraints whose combination dominates the objective "
                  "term by term."),
            ("example", ("The dual of the last lesson's program",
                         "The primal maximizes `3x₁ + 5x₂` subject to `x₁ ≤ 4`, `2x₂ ≤ 12`, "
                         "`3x₁ + 2x₂ ≤ 18`. Its dual minimizes `4y₁ + 12y₂ + 18y₃` subject to "
                         "`y₁ + 3y₃ ≥ 3` (the column of x₁) and `2y₂ + 2y₃ ≥ 5` (the column of "
                         "x₂), with y ≥ 0. The point `y = (0, 3/2, 1)` meets both with equality "
                         "and gives `0 + 18 + 18 = 36`.")),
            ("thm", ("Lemma 29.8, weak duality, in short",
                     "If x is feasible for the primal and y for the dual, then "
                     "`cᵀx ≤ (Aᵀy)ᵀx = yᵀ(Ax) ≤ bᵀy`. The first step uses `c ≤ Aᵀy` with `x ≥ 0`; "
                     "the second uses `Ax ≤ b` with `y ≥ 0`. If the two ends are equal, no "
                     "feasible x can beat this one and no feasible y can undercut this one "
                     "(Corollary 29.9).")),
            ("p", "Weak duality is two lines of algebra, and what makes it useful is the "
                  "converse direction the authors prove next. Theorem 29.10: when SIMPLEX stops, "
                  "set `yᵢ` to minus the final objective coefficient of the slack sᵢ if sᵢ is "
                  "nonbasic, and to 0 if it is basic. This y is feasible for the dual and its "
                  "value equals z, so by Corollary 29.9 both the returned x and this y are "
                  "optimal. The last lesson's walk ended with `z = 36 − (3/2)·s₂ − s₃` and s₁ "
                  "basic, which gives `y = (0, 3/2, 1)`, the point in the example above."),
            ("p", "Now the lab, the one the Operations Research Subject's lesson Weak Duality "
                  "and Certificates uses. Its first worked example, the workshop, is the same "
                  "program as the last lesson's. Type a plan x and a set of prices y and it "
                  "computes the three links of the weak-duality chain: what the plan earns, "
                  "`cᵀx`; the middle quantity `yᵀAx`; and what the prices allow, `bᵀy`; with "
                  "the gap between the ends. A table checks every primal row against the plan "
                  "and every dual constraint against the prices."),
            ("p", "The preset plan `x = (1, 1)` and prices `y = (0, 2, 1)` give the chain "
                  "`8 ≤ 9 ≤ 42`, a gap of 34: the optimum lies between 8 and 42, and neither "
                  "number needed a solver. Type `2 6` and `0 1.5 1` and all three links read 36 "
                  "and the gap 0. Type the plan `3 6` and the lab reports that it breaks the "
                  "assembly row, so its apparent 39 says nothing; type prices `1 1 0` and it "
                  "reports that they do not cover the x₁ and x₂ columns, so their 16 bounds "
                  "nothing."),
            ("p", "Section 29.5 asks where SIMPLEX starts. If every bᵢ is nonnegative, the "
                  "origin is feasible and the initial slack form will do. If some bᵢ is "
                  "negative, the basic solution of that slack form is outside the region, yet "
                  "the program may still be feasible. INITIALIZE-SIMPLEX settles the question "
                  "with L_aux: maximize −x₀ subject to `Σⱼ aᵢⱼxⱼ − x₀ ≤ bᵢ` for every i, with all "
                  "variables nonnegative. A feasible x of L with `x₀ = 0` is feasible for L_aux "
                  "with value 0, the best possible; conversely an optimum of 0 has `x₀ = 0` and "
                  "an x that satisfies L."),
            ("p", "L_aux's own initial slack form is also infeasible, but one pivot fixes that: "
                  "let x₀ enter and the slack of the row with the most negative bᵢ leave. Then "
                  "SIMPLEX runs on L_aux. If its optimum is 0, the procedure makes x₀ nonbasic "
                  "with one degenerate pivot if it is still basic, deletes x₀, and restores L's "
                  "objective, rewriting it in the current nonbasic variables. That slack form's "
                  "basic solution is feasible for L, and SIMPLEX starts from it. If the optimum is "
                  "negative, L is infeasible (Lemma 29.12)."),
            ("thm", ("Theorem 29.13, the fundamental theorem of linear programming",
                     "Every linear program in standard form is infeasible, or is unbounded, or "
                     "attains an optimum of finite value; and SIMPLEX, "
                     "with INITIALIZE-SIMPLEX, returns the right one of the three answers.")),
            ("p", "The Operations Research Subject starts the method differently, with one "
                  "artificial variable per row whose sum it minimizes in a first phase. The two "
                  "routes decide the same question in the same way: an auxiliary program that "
                  "is always feasible, whose optimum is the ideal value exactly when the "
                  "original program is feasible."),
            ("h3", "Exercise"),
            ("p", "Find a set of prices with `y₁ = 1` that is feasible for the dual of the "
                  "lesson's program, compute the bound it certifies, and check it in the lab. "
                  "Then write L_aux for the program maximize `x₁ + x₂` subject to "
                  "`x₁ + x₂ ≥ 8`, `x₁ ≤ 4`, `x₂ ≤ 3`, and show without running SIMPLEX that its "
                  "optimum is −1/3, so the program is infeasible. Remember that x₀ is subtracted "
                  "from every row, not only the first."),
            ("p", "That ends the linear programming chapter. The next lesson, Polynomials and "
                  "the FFT, multiplies polynomials in `Θ(n lg n)` by changing how they are "
                  "represented."),
        ],
        "lab": ("duality", {
            "mode": "certificate",
            "preset": "workshop",
            "panel_title": "Bracket the optimum with a plan and a set of prices",
            "panel_intro": (
                "The workshop is the last lesson's program. Type a plan, one number per "
                "variable, and a set of prices, one per row; the lab checks each and prints "
                "the weak-duality chain. Equal ends prove both optimal; a plan or price that "
                "breaks a constraint is named and certifies nothing."
            ),
        }),
        "steps_title": "Certifying an optimum",
        "steps_intro": "Write the dual first; the certificate is a point of it.",
        "steps": [
            ("Write the dual",
             "One price per primal row, `minimize bᵀy`, one constraint per primal variable "
             "from its column, and every price nonnegative."),
            ("Check the plan and the prices",
             "Substitute x into every primal row and y into every dual constraint. A point "
             "that breaks one is not feasible and bounds nothing."),
            ("Compare the values",
             "Compute `cᵀx` and `bᵀy`. The optimum lies between them; if they are equal, both "
             "points are optimal."),
            ("Read y from the final slack form",
             "After SIMPLEX stops, the price of row i is minus the objective coefficient of "
             "its slack if the slack is nonbasic, and 0 if it is basic."),
            ("Do it with prices of your own",
             "Pick a set of prices of your own for the workshop that covers both columns, "
             "predict `bᵀy` and the gap the preset plan leaves, then type both into the lab and "
             "check."),
        ],
        "worked": {
            "title": "A program whose origin is not feasible",
            "intro": [
                "Maximize `x₁ + 2x₂` subject to `x₁ + x₂ ≥ 2`, `x₁ ≤ 4`, `x₂ ≤ 3`. In standard "
                "form the first row is `−x₁ − x₂ ≤ −2`, so the origin breaks it. L_aux "
                "maximizes −x₀ with x₀ subtracted from each row's left side.",
            ],
            "lines": [
                "s₁ = −2 + x₁ + x₂ + x₀;  s₂ = 4 − x₁ + x₀;  s₃ = 3 − x₂ + x₀",
                "pivot x₀ in, s₁ out (b₁ = −2 is the most negative):",
                "x₀ = 2 − x₁ − x₂ + s₁;  s₂ = 6 − 2x₁ − x₂ + s₁;  s₃ = 5 − x₁ − 2x₂ + s₁",
                "z = −x₀ = −2 + x₁ + x₂ − s₁: basic solution feasible",
                "x₁ enters; limits: x₀ at 2, s₂ at 3, s₃ at 5: x₀ leaves",
                "z = −x₀: optimum 0, so the program is feasible",
                "drop x₀: x₁ = 2 − x₂ + s₁, objective x₁ + 2x₂ = 2 + x₂ + s₁",
            ],
            "after": [
                "The start SIMPLEX receives is `(x₁, x₂) = (2, 0)` with value 2, a corner of the "
                "original region, and SIMPLEX goes on from there to the optimum `(4, 3)` at 10. "
                "Had the first row read `x₁ + x₂ ≥ 8` instead, x₀ could not drop below 1/3, "
                "since x₀ loosens every row at once, the optimum of L_aux would be −1/3, and "
                "INITIALIZE-SIMPLEX would report the program infeasible.",
            ],
        },
        "quiz_title": "Duals, certificates and starts",
        "quiz": [
            {"q": "What is the dual of: maximize `2x₁ + x₂` subject to `x₁ + x₂ ≤ 4`, "
                  "`x₁ − x₂ ≤ 2`, `x ≥ 0`?",
             "a": ["Minimize `4y₁ + 2y₂` subject to `y₁ + y₂ ≥ 2`, `y₁ − y₂ ≥ 1`, `y ≥ 0`",
                   "Minimize `2y₁ + y₂` subject to `y₁ + y₂ ≥ 4`, `y₁ − y₂ ≥ 2`, `y ≥ 0`",
                   "Minimize `4y₁ + 2y₂` subject to `y₁ + y₂ ≤ 2`, `y₁ − y₂ ≤ 1`, `y ≥ 0`",
                   "Maximize `4y₁ + 2y₂` subject to `y₁ + y₂ ≥ 2`, `y₁ − y₂ ≥ 1`, `y ≥ 0`"],
             "c": 0,
             "why": "The dual's objective takes the primal right-hand sides, 4 and 2; its "
                    "constraints come from the columns of A, `(1, 1)` for x₁ and `(1, −1)` for "
                    "x₂, with the primal objective coefficients 2 and 1 on the right and ≥ as "
                    "the sense. The second option swaps b and c without transposing the roles. "
                    "The third keeps ≤, which would make y = 0 feasible and bound nothing. The "
                    "fourth maximizes, which is unbounded."},
            {"q": "For the workshop program, the plan `(2, 6)` earns 36 and the prices "
                  "`(0, 3/2, 1)`, which cover both columns, give `bᵀy = 36`. What follows?",
             "a": ["Both are optimal, by Corollary 29.9",
                   "The plan is optimal, but other prices might give a lower bound still",
                   "Nothing until SIMPLEX has been run to confirm it",
                   "The plan is optimal only if every constraint is tight"],
             "c": 0,
             "why": "Weak duality says no feasible plan exceeds 36 and no feasible prices fall "
                    "below 36, so a pair meeting at 36 settles both problems. Lower prices would "
                    "contradict weak duality with the plan's 36. No solver is needed, which is "
                    "the point of a certificate. The cutting row is slack at this plan, `2 < 4`, "
                    "and the plan is still optimal; its price is 0."},
            {"q": "INITIALIZE-SIMPLEX solves L_aux for a program L and finds the optimal value "
                  "−1. What does that mean?",
             "a": ["L is infeasible",
                   "L is unbounded",
                   "L's optimal value is −1",
                   "L is feasible, starting from x₀ = 1"],
             "c": 0,
             "why": "By Lemma 29.11, L is feasible exactly when L_aux's optimum is 0. An "
                    "optimum of −1 means every feasible point of L_aux has `x₀ ≥ 1`, so no x "
                    "satisfies L's constraints as written. L_aux says nothing about L's "
                    "objective, which it does not contain, so neither unboundedness nor the "
                    "value −1 follows. A point with `x₀ = 1` satisfies only the loosened "
                    "constraints."},
            {"q": "A program has right-hand sides `b = (5, −3, −7)`. In INITIALIZE-SIMPLEX's "
                  "first pivot on L_aux, which variable leaves?",
             "a": ["The slack of row 3", "The slack of row 2", "The slack of row 1", "x₀"],
             "c": 0,
             "why": "x₀ enters, and the slack of the row with the most negative bᵢ, −7, leaves. "
                    "Then x₀ = 7 plus nonbasic terms, and every slack becomes nonnegative: row 2 "
                    "gets `−3 + 7 = 4` and row 1 `5 + 7 = 12`. Choosing row 2 would leave row 3 "
                    "at `−7 + 3 = −4`, still infeasible. Row 1 is already satisfied. x₀ is the "
                    "entering variable, not the leaving one."},
        ],
        "mistakes": [
            ("Believing optimality can only be shown by searching for something better",
             "A feasible dual solution bounds every feasible plan at once, and a plan whose "
             "value meets that bound is optimal with no further search. In the lab, the plan "
             "`(2, 6)` and prices `(0, 3/2, 1)` close the chain at 36, and the table shows why "
             "term by term. Theorem 29.10 is exactly this certificate, read off SIMPLEX's last "
             "slack form."),
            ("Using prices that do not cover every column",
             "Weak duality needs `Aᵀy ≥ c` as well as `y ≥ 0`. Prices that fall short on some "
             "column bound nothing: in the lab, `y = (1, 1, 0)` gives `bᵀy = 16`, below the "
             "optimum 36, and the table marks both columns uncovered."),
            ("Assuming the initial slack form always has a feasible basic solution",
             "Setting every original variable to 0 is feasible only when every bᵢ is "
             "nonnegative. With a negative bᵢ the basic solution lies outside the region even "
             "when the program is feasible, and INITIALIZE-SIMPLEX must find a start through "
             "L_aux, or prove there is none."),
        ],
        "standard": (
            "Finish when you can certify an optimum and find a start.",
            "Write the dual of a program, use a feasible dual point to bound the primal, read "
            "the optimal dual solution off a final slack form, and set up and solve L_aux to "
            "decide whether a program with negative right-hand sides is feasible."
        ),
        "note": (
            "The lab runs only its built-in programs; the workshop matches the last lesson's "
            "program, and the lesson's L_aux example is worked by hand because the Phase I "
            "mode of the simplex kit uses one artificial per row rather than the book's single "
            "x₀. A closed chain certifies one pair of points; weak duality and Theorem 29.10 "
            "are proved for every program."
        ),
    },
    # ---------------------------------------------------------------- 05
    # CLRS 30.1-30.3, pp. 898-925. Quote: printed p. 898, 15 words,
    # quotes.py OK. Lesson total: 15 words. Lab: itakit/fft; the book's
    # exercise vectors are not used. Degree-bound, addition and
    # multiplication costs (pp. 898-900); coefficient and point-value forms,
    # Horner, Theorem 30.1, Lagrange in Theta(n^2), 2n points for a product,
    # Theorem 30.2 (pp. 900-905); roots of unity and Lemmas 30.3-30.6
    # (pp. 906-908); DFT, RECURSIVE-FFT, T(n) = 2T(n/2) + Theta(n)
    # (pp. 908-911); Theorem 30.7, the inverse DFT, Theorem 30.8 (pp. 912-913);
    # butterfly, bit-reverse, ITERATIVE-FFT, (n/2) per stage, the parallel
    # circuit (pp. 915-920); Problem 30-6 named.
    {
        "slug": "polynomials-and-the-fft",
        "title": "Polynomials and the FFT",
        "module": "Chapter 30 · Polynomials and the FFT",
        "one_line": "Two polynomials multiply in linear time once each is known by its values at enough points, and the fast Fourier transform moves between coefficients and values at the complex roots of unity in Θ(n lg n).",
        "summary": (
            "Chapter 30 multiplies two polynomials of degree-bound n in `Θ(n lg n)` instead of "
            "the schoolbook `Θ(n²)`. Section 30.1 sets the coefficient form beside the "
            "point-value form, in which multiplication is pointwise; Section 30.2 evaluates "
            "at the complex roots of unity by the divide-and-conquer FFT and interpolates by "
            "the same method run backwards; Section 30.3 lays the FFT out as stages of "
            "butterflies. Multiply polynomials in the lab both ways and count multiplications "
            "against butterflies, including a size at which the FFT does more work."
        ),
        "key": [
            "coefficient form: multiply in Θ(n²)",
            "point-value form: multiply in Θ(n)",
            "a product of degree-bound n needs 2n points",
            "evaluate at the complex roots of unity",
            "A(x) = A_e(x²) + x·A_o(x²)",
            "T(n) = 2T(n/2) + Θ(n) = Θ(n lg n)",
            "inverse DFT: the same FFT with ω⁻¹, over n",
        ],
        "key_label": "Chapter 30 in seven lines",
        "concepts_intro": (
            "Three ideas: a second way to write a polynomial, the points that make the switch "
            "cheap, and the operation the fast switch is built from."
        ),
        "concepts": [
            ("Point-value representation",
             "A polynomial of degree-bound n is fixed by its values at n distinct points "
             "(Theorem 30.1), so it can be stored as n pairs (x, A(x)) instead of n "
             "coefficients. Two polynomials stored at the same points add and multiply point "
             "by point, in linear time."),
            ("Complex roots of unity",
             "The n numbers ω with `ωⁿ = 1`, the powers of `ωₙ = e^(2πi/n)`. Squaring them "
             "gives the n/2 roots of unity of order n/2, each twice (the halving lemma), which "
             "is what lets an evaluation at n of them split into two evaluations at n/2."),
            ("Butterfly",
             "The FFT's unit of work: given two values u and v and a power ω of the root, "
             "multiply once to get `t = ω·v` and output `u + t` and `u − t`. A transform of "
             "size n is lg n stages of n/2 butterflies."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 30.1 and 30.2 closely and 30.3 for the iterative layout. The "
            "lesson sets out the two representations and the recursion in its own words, "
            "computes one small transform by hand, and multiplies polynomials both ways in the "
            "lab."
        ),
        "body": [
            ("p", "&ldquo;The most common use for Fourier transforms, and hence the FFT, is in "
                  "signal processing.&rdquo; Chapter 30 mentions signals, audio and video "
                  "compression, and then sets them aside for a cleaner problem with the same "
                  "mathematics: multiplying two polynomials. Adding two polynomials of "
                  "degree-bound n takes `Θ(n)` time; multiplying them the schoolbook way, every "
                  "coefficient of one against every coefficient of the other, takes `Θ(n²)`. "
                  "This lesson reads all three sections, which bring the product down to "
                  "`Θ(n lg n)`."),
            ("p", "Section 30.1 compares two representations. In coefficient form a "
                  "polynomial is its list a₀ to aₙ₋₁. Evaluating at one point costs `Θ(n)` by "
                  "Horner's rule, adding costs `Θ(n)`, and the product's coefficients are the "
                  "convolution of the two lists, `Θ(n²)` done directly. In point-value form a "
                  "polynomial is its values at n distinct points. Theorem 30.1 says these "
                  "determine it uniquely, because the Vandermonde matrix of distinct points is "
                  "invertible, and Lagrange's formula interpolates in `Θ(n²)`."),
            ("p", "In point-value form, multiplication is easy: if A and B are known at the "
                  "same points, `C(x) = A(x)·B(x)` at each of them, in `Θ(n)`. There is one "
                  "catch. Multiplying two polynomials of degree-bound n gives one of degree-bound "
                  "`2n − 1`, so n values of it do not determine it; each factor must first be "
                  "evaluated at 2n points. The plan is then evaluate, multiply pointwise, "
                  "interpolate, and the whole question is whether evaluation and interpolation "
                  "at 2n points can be done in less than quadratic time. Theorem 30.2 answers "
                  "yes, `Θ(n lg n)`, provided the points are chosen well."),
            ("p", "Section 30.2 chooses the complex nth roots of unity, the n powers of the "
                  "principal root `ωₙ = e^(2πi/n)`. Three lemmas do the work: the cancellation "
                  "lemma, `ω_(dn)^(dk) = ωₙᵏ`, which gives `ωₙ^(n/2) = −1`; the halving lemma, "
                  "that the squares of the n roots are the n/2 roots of order n/2, each "
                  "appearing twice; and the summation lemma, that the powers `ωₙ^(jk)` sum to 0 "
                  "over j for any k not divisible by n. The vector of values of A at the n roots "
                  "is the discrete Fourier transform of its coefficient vector, `DFTₙ(a)`."),
            ("thm", ("The FFT's recursion",
                     "Split A into its even-indexed and odd-indexed coefficients, "
                     "`A_e(x) = a₀ + a₂x + a₄x² + …` and `A_o(x) = a₁ + a₃x + a₅x² + …`, so that "
                     "`A(x) = A_e(x²) + x·A_o(x²)`. By the halving lemma, evaluating A at the n "
                     "roots needs A_e and A_o only at the n/2 roots of order n/2: two transforms "
                     "of half the size. Then `y_k = e_k + ωₙᵏ·o_k` and "
                     "`y_(k + n/2) = e_k − ωₙᵏ·o_k` for k below n/2, where e and o are the two "
                     "half-size transforms, so "
                     "`T(n) = 2T(n/2) + Θ(n) = Θ(n lg n)`.")),
            ("example", ("A transform of size 4 by hand",
                         "Take `a = (2, 0, −1, 3)`, so `A(x) = 2 − x² + 3x³`, and `ω₄ = i`. The "
                         "even part `(2, −1)` has size-2 transform `(2 + (−1), 2 − (−1)) = (1, 3)`; "
                         "the odd part `(0, 3)` has `(3, −3)`. Combining, `y₀ = 1 + 3 = 4`, "
                         "`y₂ = 1 − 3 = −2`, `y₁ = 3 + i·(−3) = 3 − 3i` and `y₃ = 3 + 3i`. Direct "
                         "evaluation agrees: `A(1) = 4`, `A(i) = 2 + 1 − 3i`, `A(−1) = −2`, "
                         "`A(−i) = 3 + 3i`.")),
            ("p", "Interpolation turns out to be the same computation. The DFT is "
                  "multiplication by the Vandermonde matrix of the roots, and Theorem 30.7 shows "
                  "that the inverse matrix has entries `ωₙ^(−kj)/n`. So the inverse DFT is the "
                  "FFT run with `ωₙ⁻¹` in place of ωₙ, followed by division by n, again "
                  "`Θ(n lg n)`. The convolution theorem, Theorem 30.8, puts the pieces together: "
                  "pad both coefficient vectors with zeros to length 2n, transform both, "
                  "multiply the transforms entry by entry, and transform back."),
            ("p", "Section 30.3 makes the FFT fast in practice. The two updates in the "
                  "recursion share the product `ωₙᵏ·o_k`; computing it once and forming the sum "
                  "and difference is a butterfly operation. Unrolling the recursion, the leaves "
                  "are the coefficients in bit-reversed order, and ITERATIVE-FFT first permutes "
                  "the input that way and then runs lg n stages, each of n/2 butterflies, "
                  "bottom up. The same layout gives a parallel FFT circuit of depth `Θ(lg n)`, "
                  "which the section draws."),
            ("p", "Now the lab. It multiplies two integer polynomials, coefficients listed "
                  "constant term first, by the schoolbook method and by the FFT route, and "
                  "compares. The FFT runs in floating point with complex roots, so each output "
                  "coefficient is rounded to the nearest integer, and the lab checks the rounded "
                  "product against the exact schoolbook one. Its tiles are n, the padded power "
                  "of 2; the schoolbook product and its count of coefficient multiplications; "
                  "the FFT product; the butterflies, three transforms of `(n/2)·lg n` each, plus "
                  "n pointwise products; whether the two agree; and how far the unrounded values "
                  "were from integers."),
            ("p", "Preset cubic multiplies the example's `2 − x² + 3x³` by `1 + 4x + 2x³`: "
                  "the product, degree 6, needs 7 coefficients, so n is 8; the schoolbook "
                  "method makes 16 multiplications and the FFT route 36 butterflies and 8 "
                  "pointwise products, and both give `2, 8, −1, 3, 12, −2, 6`. Preset sixteen "
                  "multiplies two polynomials of 16 coefficients: n is 32, schoolbook 256 "
                  "multiplications, the FFT 240 butterflies and 32 products, the first size in "
                  "these presets where the butterflies alone are fewer."),
            ("p", "Preset five squares `1 + x + x² + x³ + x⁴`. The product has 9 coefficients, "
                  "one more than 8, so n jumps to 16 and the FFT spends 96 butterflies against 25 "
                  "schoolbook multiplications. Preset large uses coefficients near a million; "
                  "the products near 10¹² are still recovered exactly, though the unrounded "
                  "values now miss integers by about `1.8 × 10⁻⁴` rather than by less than 10⁻⁹. "
                  "Rounding is safe while that distance stays well under one half, and it grows "
                  "with the size of the numbers; Problem 30-6 develops an FFT in modular "
                  "arithmetic that avoids floating point altogether."),
            ("h3", "Exercise"),
            ("p", "Multiply `1 + x` by itself through the DFT by hand. Evaluate `1 + x` at the "
                  "four 4th roots of unity 1, i, −1 and −i, square the four values, and "
                  "interpolate with the inverse transform, using `ω⁻¹ = −i` and dividing by 4. "
                  "Then type `1 1` and `1 1` into the lab and compare your coefficients and the "
                  "number of butterflies."),
            ("p", "The last chapter of this course turns from polynomials to integers. The "
                  "next lesson, GCD and Modular Arithmetic, reads Euclid's algorithm and the "
                  "arithmetic modulo n that the RSA cryptosystem is built on."),
        ],
        "lab": ("itakit", {
            "mode": "fft",
            "view": "multiply",
            "preset": "cubic",
            "presets": [
                {"id": "cubic", "label": "Two cubics, padded to 8",
                 "a": "2 0 -1 3", "b": "1 4 0 2",
                 "expect": {"ftiN": "8 (product degree 6)",
                            "ftiSchool": "2, 8, −1, 3, 12, −2, 6",
                            "ftiSchoolMults": "16 (4 × 4)",
                            "ftiFft": "2, 8, −1, 3, 12, −2, 6",
                            "ftiButterflies": "36 (3 transforms × (n/2) lg n = 3 × 12), and 8 pointwise products",
                            "ftiAgree": "yes"}},
                {"id": "sixteen", "label": "Sixteen coefficients each, padded to 32",
                 "a": "3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3",
                 "b": "2 7 1 8 2 8 1 8 2 8 4 5 9 0 4 5",
                 "expect": {"ftiN": "32 (product degree 30)",
                            "ftiSchoolMults": "256 (16 × 16)",
                            "ftiButterflies": "240 (3 transforms × (n/2) lg n = 3 × 80), and 32 pointwise products",
                            "ftiAgree": "yes"}},
                {"id": "five", "label": "Five ones squared, padded to 16",
                 "a": "1 1 1 1 1", "b": "1 1 1 1 1",
                 "expect": {"ftiN": "16 (product degree 8)",
                            "ftiSchool": "1, 2, 3, 4, 5, 4, 3, 2, 1",
                            "ftiSchoolMults": "25 (5 × 5)",
                            "ftiButterflies": "96 (3 transforms × (n/2) lg n = 3 × 32), and 16 pointwise products",
                            "ftiAgree": "yes"}},
                {"id": "large", "label": "Coefficients near a million",
                 "a": "1000000 -999999 1000000", "b": "999999 1000000 -1000000",
                 "expect": {"ftiN": "8 (product degree 4)", "ftiAgree": "yes"}},
            ],
            "panel_title": "Multiply two polynomials both ways",
            "panel_intro": (
                "Type two lists of integer coefficients, constant term first. The lab "
                "multiplies them by the schoolbook method and by the FFT route, pads to a power "
                "of 2, counts multiplications against butterflies, rounds the floating-point "
                "result and checks it against the exact product."
            ),
        }),
        "steps_title": "Multiplying through the DFT",
        "steps_intro": "Fix n before anything else; every later step depends on it.",
        "steps": [
            ("Choose n",
             "Count the product's coefficients, one more than the sum of the two degrees, and "
             "take the least power of 2 at least that large. Pad both coefficient lists with "
             "zeros to length n."),
            ("Transform both",
             "Split each list into even and odd positions, transform the halves, and combine "
             "with `e_k ± ωₙᵏ·o_k`, e and o the two half transforms, down to lists of length 1."),
            ("Multiply pointwise",
             "Multiply the two transforms entry by entry: n products."),
            ("Transform back",
             "Run the same recursion with `ωₙ⁻¹`, divide every entry by n, and round to the "
             "nearest integer when the inputs were integers."),
            ("Do it on polynomials of your own",
             "Type two polynomials of your own whose product has exactly 17 coefficients, "
             "predict n and the butterfly count before the lab prints them, and then remove "
             "one coefficient and predict again."),
        ],
        "worked": {
            "title": "Counting the two methods at n = 32",
            "intro": [
                "For preset sixteen, two polynomials of 16 coefficients each, count both "
                "methods by hand.",
            ],
            "lines": [
                "product: 16 + 16 − 1 = 31 coefficients, so n = 32",
                "schoolbook: 16 · 16 = 256 multiplications",
                "one transform: (32/2) · lg 32 = 16 · 5 = 80 butterflies",
                "three transforms: 240 butterflies, one multiplication each",
                "pointwise: 32 products; total 272 against 256",
            ],
            "after": [
                "Counted in multiplications the FFT still loses narrowly at this size, and each "
                "of its multiplications is complex. The order of growth decides only for larger "
                "n: at 1,024 coefficients each, n is 2,048, and the FFT needs "
                "`3 · 1,024 · 11 + 2,048 = 35,840` against 1,048,576.",
            ],
        },
        "quiz_title": "Roots, transforms and counts",
        "quiz": [
            {"q": "What is `ω₈⁴`, where `ω₈ = e^(2πi/8)`?",
             "a": ["−1", "1", "i", "−i"],
             "c": 0,
             "why": "By the cancellation lemma, `ω₈⁴ = ω₂¹ = e^(πi) = −1`, the case "
                    "`ωₙ^(n/2) = −1` of Corollary 30.4. 1 is `ω₈⁸`; i is `ω₈²`, a quarter turn; "
                    "−i is `ω₈⁶`."},
            {"q": "How many butterflies does one FFT of size n = 32 perform?",
             "a": ["80", "160", "32", "1,024"],
             "c": 0,
             "why": "lg 32 = 5 stages of n/2 = 16 butterflies is 80. 160 counts n per stage "
                    "instead of n/2. 32 would be one butterfly per entry with no stages. 1,024 "
                    "is n², the schoolbook count for two polynomials of 32 coefficients, not a "
                    "count for one transform."},
            {"q": "The lab pads the product of two polynomials of 5 coefficients each to "
                  "n = 16. Why not n = 8?",
             "a": ["The product has 9 coefficients, and n must be a power of 2 at least 9",
                   "Each factor has 5 coefficients, and 5 rounds up to 8 twice",
                   "The FFT always uses twice the next power of 2 above the input length",
                   "Rounding error would be too large at 8"],
             "c": 0,
             "why": "The product has degree 8, so 9 coefficients, and 8 values cannot "
                    "determine it; the least power of 2 that is at least 9 is 16. Two cubics, "
                    "with a 7-coefficient product, fit in 8, so there is no fixed doubling rule "
                    "on the input length. 8 + 8 adds sizes, which has no meaning here. Rounding "
                    "plays no part in choosing n."},
            {"q": "What are the squares of the eight complex 8th roots of unity?",
             "a": ["The four complex 4th roots of unity, each appearing twice",
                   "The eight complex 8th roots of unity again, in another order",
                   "The sixteen complex 16th roots of unity",
                   "The numbers 1 and −1, four times each"],
             "c": 0,
             "why": "This is the halving lemma: `(ω₈ᵏ)² = ω₄ᵏ`, and k and k + 4 give the same "
                    "square because `ω₈⁴ = −1`. That halving is why each recursive call is half "
                    "the size. Squaring cannot produce more distinct values than it starts with, "
                    "so 16 is impossible, and the squares include i and −i, so they are not only "
                    "±1."},
        ],
        "mistakes": [
            ("Thinking the FFT is always faster than the schoolbook product",
             "The bound `Θ(n lg n)` against `Θ(n²)` is about growth, and the constants and "
             "the padding matter at small sizes. In the lab, squaring a polynomial of 5 "
             "coefficients pads to 16 and costs 96 butterflies and 16 products against 25 "
             "multiplications; even at 16 coefficients each, the counts are 272 against 256."),
            ("Evaluating each factor at only n points",
             "Multiplying two polynomials of degree-bound n gives up to `2n − 1` coefficients, "
             "and fewer values than that do not determine it: the pointwise product would "
             "describe a different, wrapped-around polynomial. Each factor must be padded and "
             "evaluated at 2n points before multiplying."),
            ("Trusting floating-point output as exact",
             "The FFT computes with complex numbers in floating point, so its outputs carry "
             "rounding error, and integer coefficients are recovered only by rounding. In the "
             "lab the error is below 10⁻⁹ for small coefficients but about `1.8 × 10⁻⁴` for "
             "coefficients near a million; large enough inputs would round wrongly, which is "
             "why exact variants such as Problem 30-6's use modular arithmetic."),
        ],
        "standard": (
            "Finish when you can multiply polynomials through the DFT.",
            "Compute a size-4 transform by hand with the even-odd split, state why a product "
            "needs 2n points, invert a transform with `ω⁻¹` and 1/n, and count butterflies "
            "against schoolbook multiplications for a given size."
        ),
        "note": (
            "The lab's FFT works in floating point and checks its rounded product against the "
            "exact schoolbook one; its butterfly count is the iterative FFT's, three "
            "transforms of `(n/2)·lg n`. Counts at one size show where the methods stand "
            "there; the `Θ(n lg n)` bound is the book's analysis of the recursion."
        ),
    },
]
