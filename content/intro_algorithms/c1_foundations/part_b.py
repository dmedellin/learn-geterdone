"""Foundations, lessons 6-8 -- Chapters 4 and 5.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed.
(MIT Press, 2009): Chapter 4, Divide-and-Conquer, sections 4.1-4.5
(pp. 65-97; 4.6 named); Chapter 5, Probabilistic Analysis and Randomized
Algorithms, sections 5.1-5.3 (pp. 114-130; 5.4 named). Every quotation is
copied from the operator's copy with its printed page in the comment beside
the lesson. The arrays, recurrences and orders are written for these
lessons: none of the book's figures, examples or exercises is reproduced,
and its procedures are described in prose and named.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    # CLRS Chapter 4 opening and sections 4.1-4.2, pp. 65-83.
    # Quote: p. 79, 14 words, quotes.py OK. Lesson total: 14 words.
    # Recursive and base cases, recurrences, technicalities (pp. 65-67);
    # the stock problem, brute force, the transformation to changes
    # (pp. 68-70); FIND-MAX-CROSSING-SUBARRAY, FIND-MAXIMUM-SUBARRAY and
    # the recurrence (pp. 70-74); SQUARE-MATRIX-MULTIPLY, the simple
    # recursive method, T(n) = 8T(n/2) + Theta(n^2) (pp. 75-79); Strassen's
    # four steps and seven products (pp. 79-82); chapter notes on practice
    # (pp. 111-112).
    {
        "slug": "the-maximum-subarray-problem-and-strassen",
        "title": "The Maximum-Subarray Problem and Strassen's Method",
        "module": "Chapter 4 · Divide-and-Conquer",
        "one_line": "A maximum subarray lies in the left half, the right half or across the middle, which gives a Θ(n lg n) algorithm, and Strassen multiplies matrices with seven half-size products instead of eight, which gives Θ(n^(lg 7)).",
        "summary": (
            "Sections 4.1 and 4.2 apply divide-and-conquer twice. The maximum-subarray problem "
            "asks for the contiguous run of an array with the largest sum; brute force tries "
            "every pair of ends, and dividing at the middle does better because the best run "
            "across the middle takes only linear time to find. Matrix multiplication divided into "
            "quarters needs eight products and gains nothing, until Strassen's method does the "
            "job with seven. Find a maximum subarray by hand, then compare three algorithms' step "
            "counts in the lab."
        ),
        "key": [
            "brute force: n(n + 1)/2 subarray sums",
            "left half, right half, or across the middle",
            "the crossing run takes one scan each way",
            "T(n) = 2T(n/2) + Θ(n) = Θ(n lg n)",
            "quarters: 8T(n/2) + Θ(n²) = Θ(n³)",
            "Strassen: 7T(n/2) + Θ(n²) = Θ(n^(lg 7))",
        ],
        "key_label": "Sections 4.1 and 4.2 in six lines",
        "concepts_intro": (
            "Three ideas. Two are problems, and the third is the lesson the second one teaches "
            "about recurrences."
        ),
        "concepts": [
            ("Maximum subarray",
             "Given an array of numbers, some negative, a nonempty contiguous subarray "
             "`A[i..j]` whose sum is as large as possible. With no negative entries the whole "
             "array is the answer, so the problem is interesting only when there are some."),
            ("The crossing subarray",
             "A subarray of `A[low..high]` that contains both `A[mid]` and `A[mid + 1]`. The "
             "best one is the best run ending at mid joined to the best run starting at mid + 1, "
             "and each is found by one scan outward from the middle."),
            ("The count of subproblems",
             "In a recurrence `a·T(n/b) + f(n)`, the number a of subproblems is not absorbed by "
             "asymptotic notation. Cutting it from 8 to 7, at the price of more additions, is "
             "what turns `Θ(n³)` into `Θ(n^(lg 7))`, about `n^2.81`."),
        ],
        "read_title": "The sections' arguments first, then the count",
        "read_intro": (
            "Read the opening of Chapter 4 and Sections 4.1 and 4.2 in your own copy first. The "
            "lesson sets out both algorithms in its own words, finds one maximum subarray by "
            "hand, and then runs three algorithms side by side in the lab."
        ),
        "body": [
            ("p", "&ldquo;The key to Strassen&rsquo;s method is to make the recursion tree "
                  "slightly less bushy.&rdquo; The authors say it halfway through Section 4.2, and "
                  "it sums up what Chapter 4 is about: the shape of a recursion decides its cost. "
                  "This lesson reads the opening of Chapter 4 and its first two sections, the "
                  "maximum-subarray problem and Strassen's algorithm for matrix multiplication."),
            ("p", "The chapter opening recalls divide-and-conquer and names its parts: the "
                  "<em>recursive case</em>, when subproblems are large enough to recurse on, and "
                  "the <em>base case</em>, where the recursion bottoms out. Some subproblems are "
                  "not smaller instances of the original problem, and solving them is counted as "
                  "part of combining. Running times come out as recurrences, and the chapter "
                  "promises three ways to solve them, the subject of the next lesson. It also "
                  "warns that floors, ceilings and boundary conditions are usually left out of "
                  "recurrences, because they usually do not change the order of growth."),
            ("p", "Section 4.1 begins with a story. You may buy one share of a volatile stock "
                  "once and sell it later, and you are allowed to know the future prices. The obvious "
                  "rule, buy at the bottom or sell at the top, does not always give the best "
                  "profit, because the lowest price may come after the highest. Brute force tries "
                  "every pair of buy and sell days, about `n²/2` of them, so it takes `Ω(n²)` "
                  "time. The authors then look at the daily changes in price instead of the "
                  "prices: the best trade is the stretch of consecutive days whose changes have "
                  "the greatest sum."),
            ("def", ("Maximum subarray",
                     "A contiguous run of `A`, of at least one element, with the greatest possible sum. "
                     "There may be several; the book speaks of <em>a</em> maximum subarray. On "
                     "the lesson's array of changes `[5, −8, 3, 4, −2, 6, −9, 7, −1, 2, −6, 1]` "
                     "it is `A[3..6]`, with sum 11: buy before the third day's change, sell after "
                     "the sixth.")),
            ("p", "Divide-and-conquer splits `A[low..high]` at its midpoint. Any subarray lies "
                  "entirely in the left half, entirely in the right half, or across the midpoint, "
                  "so a maximum subarray is the best of three: the two halves' answers, found "
                  "recursively, and the best crossing subarray. That last is not a smaller copy "
                  "of the problem, since it must cross the middle, and that restriction is what "
                  "makes it easy: FIND-MAX-CROSSING-SUBARRAY scans left from mid keeping the best "
                  "sum so far, scans right from mid + 1 the same way, and adds the two, in time "
                  "linear in the subarray's length."),
            ("p", "FIND-MAXIMUM-SUBARRAY returns a one-element subarray as its base case and "
                  "otherwise takes the best of the three candidates. Dividing is constant, "
                  "conquering is `2T(n/2)`, combining is the linear crossing scan, so the "
                  "recurrence is `T(n) = 2T(n/2) + Θ(n)`, merge sort's, and the solution is "
                  "`Θ(n lg n)`. The section's exercises go further: Exercise 4.1-5 sketches a "
                  "nonrecursive, linear-time method that extends the best subarray ending at each "
                  "position by one element at a time."),
            ("p", "Section 4.2 turns to multiplying n × n matrices. The definition costs n "
                  "scalar multiplications for each of the `n²` entries, so SQUARE-MATRIX-MULTIPLY "
                  "takes `Θ(n³)`. Dividing each matrix into four `n/2 × n/2` quarters writes each "
                  "quarter of the product as two products of quarters added together: eight "
                  "half-size products and four additions. Partitioning by index calculation "
                  "costs only constant time, so the recurrence is `T(n) = 8T(n/2) + Θ(n²)`, whose "
                  "solution is `Θ(n³)`. Divide-and-conquer alone bought nothing. The authors' "
                  "warning is that asymptotic notation absorbs constant factors but the 8 in "
                  "front of `T(n/2)` is not a constant factor of the answer: it decides how bushy "
                  "the tree is."),
            ("thm", ("Strassen's method",
                     "Form 10 sums and differences of the quarters, compute only seven products "
                     "of `n/2 × n/2` matrices from them, and assemble the four quarters of the "
                     "product from the seven with 8 more additions and subtractions. The "
                     "additions cost `Θ(n²)`, so `T(n) = 7T(n/2) + Θ(n²)`, which Section 4.5 "
                     "solves as `Θ(n^(lg 7))`, with `lg 7 ≈ 2.807`.")),
            ("p", "The authors call the method not at all obvious, and describe it in four "
                  "steps, leaving the algebra that checks each quarter to the section itself. "
                  "Their chapter notes add the practical view: the constant factor is larger than "
                  "the simple method's, sparse matrices have faster special methods, the method "
                  "is somewhat less numerically stable, and the submatrices cost memory. Fast "
                  "implementations use Strassen's method above a system-dependent crossover size "
                  "and the simple method below it, as Chapter 1's race predicts."),
            ("math", [
                "scalar multiplications, recursing all the way to 1 × 1",
                "",
                "n      8 products a level (n³)    7 products a level (7^(lg n))",
                "2              8                       7",
                "4             64                      49",
                "8            512                     343",
                "16         4,096                   2,401",
            ]),
            ("p", "Now the lab, which runs three algorithms on the array you type. Brute force "
                  "adds each subarray's sum to a running total, one step an addition, "
                  "`n(n + 1)/2` steps. Divide-and-conquer is FIND-MAXIMUM-SUBARRAY, counted as "
                  "its calls and the elements its crossing scans add. One pass is the linear "
                  "method of Exercise 4.1-5, one step an element. The tiles give each answer as "
                  "a subarray and its sum, each step count, and whether the three agree."),
            ("p", "The worked example <code>changes</code> is the array in the definition above. "
                  "All three find `A[3..6]` with sum 11. Brute force takes 78 sums; "
                  "divide-and-conquer makes 23 calls and its crossing scans add 44 elements; the "
                  "single pass reads 12 elements. Choose <code>sixteen</code>, a longer array of "
                  "changes: the answer is `A[3..12]` with sum 13, and brute force needs 136 sums "
                  "against 31 calls and 64 scanned elements, and 16 for one pass. At n = 16 the "
                  "crossing scans add `n·lg n` elements exactly, one full pass per level."),
            ("p", "The edge cases are worth a look. In <code>all-negative</code>, `[−4, −2, −7, "
                  "−3, −5]`, the answer is the single element `A[2..2]` with sum −2: the problem "
                  "asks for a nonempty subarray, so an empty one with sum 0 is not allowed. In "
                  "<code>all-positive</code> it is the whole array, `A[1..5]` with sum 14, as the "
                  "book observes it must be."),
            ("h3", "Exercise"),
            ("p", "Find a maximum subarray of `[−3, 4, −1, 2, −6, 5, −2, 3, −4]` by hand with "
                  "the divide-and-conquer method: split at mid = 5, find the best crossing "
                  "subarray by scanning out from the middle, and compare it with the best of each "
                  "half. Then enter the array in the lab."),
            ("p", "Both algorithms in this lesson were priced by recurrences that the lesson "
                  "solved by appeal to merge sort or left to Section 4.5. The next lesson, Solving "
                  "Recurrences, gives the three methods that solve them."),
        ],
        "lab": ("itakit", {
            "mode": "maxsub",
            "view": "compare",
            "preset": "changes",
            "presets": [
                {"id": "changes", "label": "Twelve daily changes in price",
                 "list": "5 -8 3 4 -2 6 -9 7 -1 2 -6 1",
                 "expect": {"msiBrute": "A[3..6], sum 11", "msiDc": "A[3..6], sum 11",
                            "msiLinear": "A[3..6], sum 11",
                            "msiBruteSteps": "78 sums (n(n + 1)/2)",
                            "msiDcSteps": "23 calls, 44 elements scanned across the middle",
                            "msiLinearSteps": "12 elements, one pass"}},
                {"id": "sixteen", "label": "Sixteen daily changes in price",
                 "list": "2 -5 6 -1 -4 8 3 -7 -2 9 -3 4 -8 1 5 -6",
                 "expect": {"msiDc": "A[3..12], sum 13",
                            "msiBruteSteps": "136 sums (n(n + 1)/2)",
                            "msiDcSteps": "31 calls, 64 elements scanned across the middle"}},
                {"id": "all-negative", "label": "Five changes, every one negative",
                 "list": "-4 -2 -7 -3 -5",
                 "expect": {"msiBrute": "A[2..2], sum −2",
                            "msiAgree": "yes: all three find sum −2, the same subarray"}},
                {"id": "all-positive", "label": "Five changes, every one positive",
                 "list": "3 1 4 1 5",
                 "expect": {"msiDc": "A[1..5], sum 14"}},
            ],
            "panel_title": "One maximum subarray, three algorithms",
            "panel_intro": (
                "Type an array of whole numbers, some negative. The lab finds a maximum subarray by "
                "brute force, by FIND-MAXIMUM-SUBARRAY and by a single pass, and counts each "
                "algorithm's steps on that array."
            ),
        }),
        "steps_title": "Finding a maximum subarray by divide-and-conquer",
        "steps_intro": "Four steps on one array, then one of your own.",
        "steps": [
            ("Split at the middle",
             "Compute `mid = ⌊(low + high)/2⌋`. The left half is `A[low..mid]`, the right half "
             "`A[mid + 1..high]`."),
            ("Scan out from the middle",
             "Add `A[mid]`, `A[mid − 1]`, and so on, keeping the largest running sum and where it "
             "began. Do the same rightward from `A[mid + 1]`. The best crossing subarray joins the "
             "two best runs."),
            ("Solve each half the same way",
             "Recurse until the pieces have one element, whose best subarray is itself. On paper, "
             "you may solve a short half by inspection."),
            ("Take the best of three",
             "Compare the left answer, the right answer and the crossing answer, and keep the "
             "largest sum."),
            ("Price trades of your own",
             "Write ten daily prices for an invented stock, convert them to nine changes, find "
             "the best trade by hand, and check it against the lab's three algorithms."),
        ],
        "worked": {
            "title": "The crossing subarray of the twelve changes",
            "intro": [
                "Find the best subarray crossing the middle of `[5, −8, 3, 4, −2, 6, −9, 7, −1, "
                "2, −6, 1]`, the lab's example <code>changes</code>. Here mid = 6.",
            ],
            "lines": [
                "left from A[6]: 6, 4, 8, 11, 3, 8",
                "best ending at 6: A[3..6], sum 11",
                "right from A[7]: −9, −2, −3, −1, −7, −6",
                "best starting at 7: A[7..10], sum −1",
                "crossing: A[3..10], sum 11 − 1 = 10",
                "left half's best: A[3..6], sum 11",
                "right half's best: A[8..10], sum 8",
                "best of three: A[3..6], sum 11",
            ],
            "after": [
                "The crossing run must take something from the right, and the best it can take "
                "costs 1, so it loses to the left half's answer by exactly that. The scans read "
                "all twelve elements once, which is the linear combine step.",
            ],
        },
        "quiz_title": "Maximum subarrays and matrix products",
        "quiz": [
            {"q": "What is a maximum subarray of the exercise array `[−3, 4, −1, 2, −6, 5, −2, "
                  "3, −4]`?",
             "a": ["A[2..4], sum 5", "A[6..8], sum 6", "A[2..8], sum 5", "A[6..6], sum 5"],
             "c": 1,
             "why": "The right half's best run, 5 − 2 + 3, has sum 6. The left half's best, "
                    "`A[2..4]`, has 4 − 1 + 2 = 5, and the best crossing subarray joins it to "
                    "`A[6..8]` through the −6, giving `A[2..8]` with sum 5. The single 5 also has "
                    "sum 5. Six beats all three, and the lab's three algorithms agree on "
                    "`A[6..8]`."},
            {"q": "Multiplying two 16 × 16 matrices with Strassen's method all the way down to "
                  "1 × 1, how many scalar multiplications are made?",
             "a": ["4,096", "2,401", "3,584", "256"],
             "c": 1,
             "why": "Each level of recursion makes seven products of half the size, and there "
                    "are `lg 16 = 4` levels, so `7⁴ = 2,401`. 4,096 is `16³ = 8⁴`, the simple "
                    "method or the eight-product recursion. 3,584 is seven-eighths of 4,096, as "
                    "if the saving applied at one level only. 256 is the number of entries in the "
                    "product."},
            {"q": "Why can FIND-MAX-CROSSING-SUBARRAY find its answer in linear time, when the "
                  "maximum-subarray problem itself is not solved that way by the recursion?",
             "a": ["Because the crossing subarray has at most two elements",
                   "Because a crossing subarray is a best run ending at mid joined to a best run "
                   "starting at mid + 1, and each is found by one scan from the middle",
                   "Because it reuses the answers of the two recursive calls",
                   "Because the crossing subarray is always the largest of the three candidates"],
             "c": 1,
             "why": "Fixing both ends at the middle leaves only one free end on each side, and "
                    "the best choice of each is found by one scan. The crossing subarray can be "
                    "as long as the whole range. It uses nothing from the recursive calls. And it "
                    "is often not the winner: in the worked example the left half's answer beats "
                    "it."},
            {"q": "In the example <code>all-negative</code>, `[−4, −2, −7, −3, −5]`, why is "
                  "the answer `A[2..2]` with sum −2, rather than an empty subarray with sum 0?",
             "a": ["Because the problem asks for a nonempty subarray",
                   "Because the divide-and-conquer recursion cannot return an empty subarray, "
                   "though brute force could",
                   "Because −2 is the median of the array",
                   "Because the sum of an empty subarray is undefined"],
             "c": 0,
             "why": "Section 4.1 defines the maximum subarray as a nonempty contiguous subarray, "
                    "and all three algorithms in the lab answer that problem, brute force "
                    "included. With nonempty required, the best is the largest single element. "
                    "The median of the array is −4. The empty sum is perfectly well defined as "
                    "0; the problem simply excludes it."},
        ],
        "mistakes": [
            ("Expecting the best trade to buy at the bottom or sell at the top",
             "The lowest price can come after the highest, and even when it does not, the best "
             "stretch may contain neither. Section 4.1 gives a small counterexample, and here is "
             "another: prices 20, 23, 15, 21, 12, 14 over six days. The highest, 23, comes before "
             "the lowest, 12; buying at 12 earns 2, and selling at 23 earns at most 3; the best "
             "trade buys at 15 and sells at 21 for 6, touching neither. As changes, "
             "`[3, −8, 6, −9, 2]`, its maximum subarray is the single element `A[3..3]`."),
            ("Expecting divide-and-conquer to beat brute force by itself",
             "Dividing a matrix product into quarters gives eight half-size products, "
             "`8T(n/2) + Θ(n²)`, which is still `Θ(n³)`. The gain comes from having fewer "
             "subproblems than the size reduction would suggest, or a cheap combine, and "
             "Strassen's seven products are what buy the improvement. Division is a way to "
             "organise an algorithm, not a speed-up in itself."),
            ("Taking Strassen's method to be faster at every size",
             "Its order of growth is lower, but its constant factor is larger and it needs extra "
             "matrices, so for small n the simple method wins. The book's chapter notes describe "
             "implementations that switch to the simple method below a crossover size that "
             "depends on the system, the same crossover argument as in Chapter 1."),
        ],
        "standard": (
            "Finish when you can solve the maximum-subarray problem by divide-and-conquer and "
            "write the recurrences of Section 4.2.",
            "Given an array of ten to sixteen numbers, find a maximum subarray by the crossing "
            "method, and write and solve by the tree the recurrences of the simple and of "
            "Strassen's matrix multiplication."
        ),
        "note": (
            "The lab counts additions, calls and elements read on the array you type; they "
            "are counts of steps on one input, not times. It does not multiply matrices: "
            "Strassen's seven products are set out in the book's Section 4.2, and the next "
            "lesson's lab solves its recurrence exactly."
        ),
    },
    # ---------------------------------------------------------------- 07
    # CLRS sections 4.3-4.5, pp. 83-97 (4.6 named).
    # Quote: p. 66, 30 words, quotes.py OK. Lesson total: 30 words.
    # Substitution method, guessing, subtleties, the O(n) pitfall,
    # changing variables (pp. 83-88); recursion trees as guesses
    # (pp. 88-93); the master theorem, intuition, the gaps, applying it
    # (pp. 93-97); its proof in 4.6 named.
    {
        "slug": "solving-recurrences",
        "title": "Solving Recurrences",
        "module": "Chapter 4 · Divide-and-Conquer",
        "one_line": "A recurrence is solved by guessing and proving with induction, by summing a recursion tree level by level, or for T(n) = a·T(n/b) + f(n) by comparing f(n) with n^(log_b a) under the master theorem, which leaves gaps.",
        "summary": (
            "Sections 4.3 to 4.5 give three methods for solving recurrences. Substitution guesses "
            "the form of the answer and proves it by induction, constants included. The "
            "recursion tree sums the cost level by level and supplies the guess. The master "
            "method settles most divide-and-conquer recurrences in one comparison and leaves "
            "gaps where it says nothing. Solve a recurrence exactly at small n by hand, then let "
            "the lab evaluate recurrences at large n beside the master method's verdict."
        ),
        "key": [
            "substitution: guess, then prove by induction",
            "prove the exact form, constant included",
            "a recursion tree sums each level's cost",
            "compare f(n) with n^(log_b a)",
            "smaller: Θ(n^(log_b a)); equal: times lg n",
            "larger, and regular: Θ(f(n))",
            "not polynomially apart: no answer",
        ],
        "key_label": "Sections 4.3 to 4.5 in seven lines",
        "concepts_intro": (
            "Three methods, used together: one to find an answer, one to prove it, and one that "
            "does both for a common family of recurrences."
        ),
        "concepts": [
            ("The substitution method",
             "Guess the form of the solution, then use induction to find constants that make it "
             "work, substituting the guess for T on the smaller arguments. It proves upper or "
             "lower bounds, and it needs a good guess."),
            ("The recursion tree",
             "Draw each call as a node labelled with its own cost, add the costs across each "
             "level, and add the levels. Done carefully it is a proof; done loosely it is the "
             "quickest way to a guess for substitution."),
            ("The master theorem",
             "For `T(n) = a·T(n/b) + f(n)` with `a ≥ 1` and `b > 1`, compare f(n) with "
             "`n^(log_b a)`. Polynomially smaller gives `Θ(n^(log_b a))`, the same order gives "
             "`Θ(n^(log_b a)·lg n)`, polynomially larger and regular gives `Θ(f(n))`. Anything "
             "else is outside the theorem."),
        ],
        "read_title": "The sections' methods first, then the exact values",
        "read_intro": (
            "Read Sections 4.3 to 4.5 in your own copy first. The lesson sets out the three "
            "methods in its own words, solves one recurrence exactly by hand, and then lets the "
            "lab evaluate recurrences at large n beside the master method's case."
        ),
        "body": [
            ("p", "&ldquo;To use the master method, you will need to memorize three cases, but "
                  "once you do that, you will easily be able to determine asymptotic bounds for "
                  "many simple recurrences.&rdquo; The authors make the promise in the opening of "
                  "Chapter 4 and keep it in Section 4.5. Before that come two methods that work "
                  "more widely and ask more of you. This lesson reads Sections 4.3, 4.4 and 4.5."),
            ("p", "Section 4.3 is the substitution method, in two steps: guess the form of the "
                  "solution, then prove the guess by induction, finding constants that make "
                  "it hold. The guess is substituted for T on the smaller arguments in the "
                  "inductive step, which gives the method its name. The base case needs care, "
                  "because a bound like `T(n) ≤ c·n lg n` can fail at n = 1, where `lg n` is 0; "
                  "asymptotic notation only asks for the bound from some `n₀` on, so the induction "
                  "may start at a larger n."),
            ("p", "The authors list the subtleties. A guess can be right in form and still fail "
                  "the induction by a lower-order term; the cure is to subtract a lower-order term "
                  "from the guess, which makes the induction stronger rather than weaker. A "
                  "careless proof can seem to show what is false: from `T(n) ≤ 2c·(n/2) + n` one "
                  "may write `c·n + n = O(n)` and conclude `T(n) = O(n)`, but the induction "
                  "promised `T(n) ≤ c·n` with the same c, and `c·n + n` is not at most `c·n`. And an "
                  "unfamiliar recurrence can sometimes be turned into a familiar one by changing "
                  "variables, for instance by writing n as `2ᵐ`."),
            ("p", "Section 4.4 is the recursion tree. Each node is one subproblem labelled with "
                  "the cost of its own dividing and combining; summing each level and then the "
                  "levels gives the total. The authors use the tree mainly to generate a guess, "
                  "tolerating some sloppiness (assuming n a power of b, dropping floors) because "
                  "substitution will verify the guess afterwards. Uneven splits, such as a third "
                  "and two thirds, give trees whose leaves sit at different depths; the section "
                  "reads a guess of `O(n lg n)` off such a tree and then verifies it by "
                  "substitution."),
            ("thm", ("The master theorem (Theorem 4.1)",
                     "Let `a ≥ 1` and `b > 1` be constants and `T(n) = a·T(n/b) + f(n)`. (1) If "
                     "`f(n) = O(n^(log_b a − ε))` for some `ε > 0`, then `T(n) = Θ(n^(log_b a))`. "
                     "(2) If `f(n) = Θ(n^(log_b a))`, then `T(n) = Θ(n^(log_b a)·lg n)`. (3) If "
                     "`f(n) = Ω(n^(log_b a + ε))` for some `ε > 0` and `a·f(n/b) ≤ c·f(n)` for some "
                     "`c < 1` and all large n, then `T(n) = Θ(f(n))`.")),
            ("p", "The intuition is a contest between the root and the leaves of the recursion "
                  "tree. The leaves number `a^(log_b n) = n^(log_b a)`, so `n^(log_b a)` measures "
                  "the bottom of the tree and f(n) the top. If the leaves win by a polynomial "
                  "factor, they set the answer; if the root wins by a polynomial factor and the "
                  "costs shrink geometrically down the tree, which is the regularity condition, "
                  "the root sets it; if they tie, every level costs about the same and there are "
                  "`log_b n` levels. The theorem's technicalities are the gaps: f(n) smaller than "
                  "`n^(log_b a)` but not by a factor of `n^ε`, or larger but not by such a factor. "
                  "In a gap the master method does not apply."),
            ("math", [
                "the lab's recurrences, f(n) = c·n^k·lg^p n",
                "",
                "T(n) = 2T(n/2) + n         n^(log_b a) = n       case 2  Θ(n lg n)",
                "T(n) = 7T(n/2) + n²        n^(lg 7) ≈ n^2.807    case 1  Θ(n^(lg 7))",
                "T(n) = 8T(n/2) + n²        n³                    case 1  Θ(n³)",
                "T(n) = 2T(n/2) + n²        n                     case 3  Θ(n²)",
                "T(n) = T(n/2) + 1          1                     case 2  Θ(lg n)",
                "T(n) = 4T(n/2) + n²·lg n   n²                    gap",
            ]),
            ("p", "Section 4.6 proves the theorem, first for n an exact power of b and then with "
                  "floors and ceilings, and the course leaves that proof to the book. Its first "
                  "half is a recursion tree with the three cases read off the sum of the levels, "
                  "which is what the lab evaluates."),
            ("p", "Now the lab. Enter a, b and f(n) as `c·n^k·lg^p n`, a value for `T(1)` and a "
                  "largest exponent j; the lab computes `T(n)` exactly at every `n = b^j` from the "
                  "recurrence itself. The tiles are `n^(log_b a)`, the master method's case "
                  "(decided by comparing the whole numbers `b^k` and a), the solution it gives, "
                  "`T(n)` at the largest n, and `T(n)` divided by the predicted growth there. If "
                  "the prediction is right, that ratio settles toward a constant as j grows; the "
                  "table shows it level by level."),
            ("p", "The worked example <code>merge-sort</code> is `T(n) = 2T(n/2) + n` with "
                  "`T(1) = 1`: case 2, `Θ(n lg n)`, and `T(1,024) = 11,264`, which is exactly "
                  "`n·lg n + n`; the ratio is 11/10, heading for 1. In <code>strassen</code>, "
                  "`7T(n/2) + n²`, case 1 gives `Θ(n^(lg 7))`, `T(1,024) = 657,710,813` and the "
                  "ratio is about 2.33, heading for 7/3. In <code>eight-products</code>, the "
                  "simple recursive matrix method, the critical function is `n³`, and the ratio "
                  "is about 2.00. Change j and watch the ratios settle."),
            ("p", "In <code>heavy-top</code>, `2T(n/2) + n²`, the root dominates: case 3, with "
                  "regularity `2·f(n/2) = (1/2)·f(n)`, and `Θ(n²)`. In <code>binary-search</code>, "
                  "`T(n/2) + 1`, case 2 with `n^(log_b a) = 1` gives `Θ(lg n)`, and `T(1,024) = "
                  "11`. Then <code>gap</code>: `4T(n/2) + n²·lg n` is larger than `n²` but only by "
                  "a logarithm, so no case applies. The lab still evaluates it, `T(1,024) = "
                  "58,720,256`, and sets it against `n²·lg² n`, the answer that Exercise 4.6-2's "
                  "extension of case 2 gives; the ratio is 14/25 there, heading for 1/2."),
            ("p", "One more, <code>strassen-big-base</code>, repeats Strassen's recurrence with "
                  "`T(1) = 50`. The exact value jumps to 14,498,998,014 and the ratio to about "
                  "51.33, but the case and the solution do not move. Boundary conditions change "
                  "the constant, which is why the chapter allows itself to leave them out."),
            ("h3", "Exercise"),
            ("p", "Take `T(n) = 3T(n/2) + n` with `T(1) = 1`. Compute `T(2)`, `T(4)`, `T(8)`, "
                  "`T(16)` and `T(32)` by hand from the recurrence, say which case of the master "
                  "theorem applies and what it predicts, and check both in the lab with a = 3, "
                  "b = 2, k = 1 and j = 5."),
            ("p", "Recurrences describe deterministic algorithms. The next lesson, The Hiring "
                  "Problem and Randomized Algorithms, opens Chapter 5, where the count depends on "
                  "the order of the input and the tool is an expectation."),
        ],
        "lab": ("itakit", {
            "mode": "recurrence",
            "view": "master",
            "preset": "merge-sort",
            "presets": [
                {"id": "merge-sort", "label": "T(n) = 2T(n/2) + n, T(1) = 1",
                 "a": "2", "b": "2", "k": "1", "j": "10",
                 "expect": {"rciCritical": "n", "rciCase": "case 2: f(n) = Θ(n^(log_b a))",
                            "rciSolution": "Θ(n lg n)", "rciLast": "T(1,024) = 11,264",
                            "rciRatio": "11/10 = 1.10"}},
                {"id": "strassen", "label": "T(n) = 7T(n/2) + n², T(1) = 1",
                 "a": "7", "b": "2", "k": "2", "j": "10",
                 "expect": {"rciCritical": "n^(log_2 7) ≈ n^2.807",
                            "rciCase": "case 1: f(n) = O(n^(log_b a − ε))",
                            "rciSolution": "Θ(n^(log_2 7))",
                            "rciLast": "T(1,024) = 657,710,813",
                            "rciRatio": "657,710,813/282,475,249 ≈ 2.33"}},
                {"id": "eight-products", "label": "T(n) = 8T(n/2) + n², T(1) = 1",
                 "a": "8", "b": "2", "k": "2", "j": "10",
                 "expect": {"rciCritical": "n^3", "rciSolution": "Θ(n^3)",
                            "rciRatio": "2,047/1,024 ≈ 2.00"}},
                {"id": "heavy-top", "label": "T(n) = 2T(n/2) + n², T(1) = 1",
                 "a": "2", "b": "2", "k": "2", "j": "10",
                 "expect": {"rciCase": "case 3: f(n) = Ω(n^(log_b a + ε)), and a·f(n/b) ≤ (1/2)·f(n)",
                            "rciSolution": "Θ(n^2)"}},
                {"id": "binary-search", "label": "T(n) = T(n/2) + 1, T(1) = 1",
                 "a": "1", "b": "2", "k": "0", "j": "10",
                 "expect": {"rciCritical": "1", "rciSolution": "Θ(lg n)",
                            "rciLast": "T(1,024) = 11"}},
                {"id": "gap", "label": "T(n) = 4T(n/2) + n²·lg n, T(1) = 1",
                 "a": "4", "b": "2", "k": "2", "p": "1", "j": "10",
                 "expect": {"rciCase": "falls in the gap between cases 2 and 3",
                            "rciLast": "T(1,024) = 58,720,256",
                            "rciRatio": "14/25 = 0.56"}},
                {"id": "strassen-big-base", "label": "T(n) = 7T(n/2) + n², T(1) = 50",
                 "a": "7", "b": "2", "k": "2", "t1": "50", "j": "10",
                 "expect": {"rciSolution": "Θ(n^(log_2 7))",
                            "rciLast": "T(1,024) = 14,498,998,014",
                            "rciRatio": "14,498,998,014/282,475,249 ≈ 51.33"}},
            ],
            "panel_title": "A recurrence, exactly, beside the master method",
            "panel_intro": (
                "Enter a, b and f(n) = c·n^k·lg^p n, a value for T(1) and how far to go. The lab "
                "evaluates T(n) exactly at n = b, b², and so on, names the master method's case, "
                "and divides T(n) by the growth it predicts."
            ),
        }),
        "steps_title": "Applying the master method by hand",
        "steps_intro": "Four steps for one recurrence, then one of your own.",
        "steps": [
            ("Read off a, b and f(n)",
             "Check `a ≥ 1`, `b > 1`, and that f(n) does not depend on T. For "
             "`T(n) = 3T(n/2) + n`, a = 3, b = 2, f(n) = n."),
            ("Compute n^(log_b a)",
             "Here `n^(lg 3) ≈ n^1.585`. If `b^k = a` for f(n) = `n^k`, the two are of the same "
             "order."),
            ("Compare, by a polynomial factor",
             "Ask whether f(n) is smaller than `n^(log_b a)` by some `n^ε`, the same order, or "
             "larger by some `n^ε`. A factor of `lg n` is not polynomial: that is a gap."),
            ("Check regularity in case 3, then write the answer",
             "In case 3, confirm `a·f(n/b) ≤ c·f(n)` for some `c < 1`. Then write "
             "`Θ(n^(log_b a))`, `Θ(n^(log_b a)·lg n)` or `Θ(f(n))`."),
            ("Classify recurrences of your own",
             "Write three recurrences that fall in cases 1, 2 and 3 and one in a gap, predict each "
             "case, and confirm them in the lab, watching the ratio settle as you raise j."),
        ],
        "worked": {
            "title": "Strassen's recurrence, exactly",
            "intro": [
                "Evaluate `T(n) = 7T(n/2) + n²` with `T(1) = 1`, the lab's example "
                "<code>strassen</code>, at small powers of 2, and set the values beside "
                "`n^(lg 7)`.",
            ],
            "lines": [
                "T(2) = 7·1 + 4 = 11",
                "T(4) = 7·11 + 16 = 93",
                "T(8) = 7·93 + 64 = 715",
                "T(16) = 7·715 + 256 = 5,261",
                "n^(lg 7) at 16: 7⁴ = 2,401",
                "ratio 5,261/2,401 ≈ 2.19",
            ],
            "after": [
                "Unrolling gives the closed form `T(2ʲ) = (7·7ʲ − 4·4ʲ)/3`, so the ratio tends "
                "to 7/3 ≈ 2.33, which the lab shows at n = 1,024. Case 1 applies because "
                "`n² = O(n^(lg 7 − ε))` with ε about 0.8: the leaves dominate.",
            ],
        },
        "quiz_title": "Substitution, trees and the master method",
        "quiz": [
            {"q": "For the exercise, `T(n) = 3T(n/2) + n` with `T(1) = 1`, what is `T(32)`, and "
                  "what does the master theorem give?",
             "a": ["211; case 1, Θ(n^(lg 3))", "665; case 1, Θ(n^(lg 3))",
                   "665; case 2, Θ(n lg n)", "665; case 3, Θ(n)"],
             "c": 1,
             "why": "The values are 5, 19, 65, 211 and 665 at n = 2, 4, 8, 16 and 32; 211 is "
                    "T(16). Since `2¹ = 2 < 3`, f(n) = n is polynomially smaller than "
                    "`n^(lg 3) ≈ n^1.585`: case 1, `Θ(n^(lg 3))`. Case 2 would need `b^k = a`, "
                    "and case 3 needs f larger. In closed form `T(2ʲ) = 3^(j+1) − 2^(j+1)`."},
            {"q": "What does the master method give for `T(n) = 2T(n/4) + √n`?",
             "a": ["Θ(√n)", "Θ(√n·lg n)", "Θ(n)", "Nothing: it falls in a gap"],
             "c": 1,
             "why": "Here `n^(log_4 2) = n^(1/2) = √n`, the same order as f(n), so case 2 gives "
                    "`Θ(√n·lg n)`. Θ(√n) drops the logarithm that the equal levels add up to. "
                    "Θ(n) would need four subproblems of size n/4. A gap needs f to differ from "
                    "`√n` by a non-polynomial factor, and here they are equal."},
            {"q": "Which statement about `T(n) = 4T(n/2) + n²/lg n` is correct?",
             "a": ["Case 1 applies, because f(n) = O(n²)",
                   "Case 2 applies, because f(n) is n² up to a logarithm",
                   "The master method does not apply, because f(n) is smaller than n² but not by "
                   "a factor of n^ε",
                   "Case 3 applies, because n²/lg n grows faster than n"],
             "c": 2,
             "why": "Case 1 needs `f(n) = O(n^(2 − ε))` for some positive ε, and `n²/lg n` is not "
                    "that small; being `O(n²)` is not enough. Case 2 needs f to be `Θ(n²)` exactly. "
                    "Case 3 compares f with `n^(log_b a) = n²`, not with n. The recurrence falls in "
                    "the gap between cases 1 and 2."},
            {"q": "A proof by substitution for `T(n) = 2T(n/2) + n` reads: assume `T(m) ≤ cm` for "
                  "m < n; then `T(n) ≤ 2c·(n/2) + n = c·n + n = O(n)`. What is wrong?",
             "a": ["Nothing: T(n) = O(n) is correct",
                   "The base case was not checked",
                   "The induction must show `T(n) ≤ c·n` with the same c, and `c·n + n` is larger than `c·n`",
                   "Substitution can prove only lower bounds"],
             "c": 2,
             "why": "The hypothesis was a bound with a fixed constant, so the step must re-derive "
                    "that exact bound; absorbing the extra n into O changes the constant at every "
                    "level, which is no proof. In fact `T(n) = Θ(n lg n)`, so the claim is false. "
                    "A missing base case is a flaw too, but not the one that makes this proof "
                    "wrong. Substitution proves upper and lower bounds."},
        ],
        "mistakes": [
            ("Using case 3 whenever f(n) is larger than n^(log_b a)",
             "Case 3 needs f to be larger by a polynomial factor `n^ε`, and regular. A "
             "logarithmic factor is not enough: `4T(n/2) + n²·lg n` falls in the gap between "
             "cases 2 and 3, and the book's own example of a recurrence that looks like case 3 "
             "is of the same kind. On the lesson's gap example the exact value tracks "
             "`n²·lg² n`, not `n²·lg n`, which is what case 3 would predict."),
            ("Absorbing the extra term into O inside an induction",
             "In the substitution method the inductive step must reproduce the hypothesis "
             "exactly, constant and all. Writing `c·n + n = O(n)` replaces the constant at every "
             "step, and the authors show it proving a false bound. When the exact form fails by "
             "a lower-order term, subtract one from the guess instead."),
            ("Expecting T(1) to change the order of growth",
             "For recurrences of this kind the boundary value scales part of the answer and "
             "leaves the order alone, which is why the book omits it. The lab's "
             "<code>strassen-big-base</code> raises `T(1)` from 1 to 50 and the exact value grows "
             "about 22-fold while the case and the solution stay the same."),
        ],
        "standard": (
            "Finish when you can solve a divide-and-conquer recurrence by two methods.",
            "Given T(n) = a·T(n/b) + f(n), evaluate it exactly at small powers of b, draw its "
            "recursion tree with level costs, apply the master method or say which gap it falls "
            "in, and prove a guessed bound by substitution."
        ),
        "note": (
            "The lab evaluates a recurrence exactly at powers of b and names the master case "
            "for f(n) of the form c·n^k·lg^p n only. A ratio that settles is evidence that the "
            "predicted growth is right; the master theorem, or a substitution proof, is what "
            "establishes it for every n."
        ),
    },
    # ---------------------------------------------------------------- 08
    # CLRS sections 5.1-5.3, pp. 114-130 (5.4 named).
    # Quote: p. 115, 16 words, quotes.py OK. Lesson total: 16 words.
    # The hiring problem, HIRE-ASSISTANT, cost model, worst case
    # (pp. 114-115); probabilistic analysis, ranks, uniform random
    # permutations (pp. 115-116); randomized algorithms and RANDOM
    # (pp. 116-117); indicator random variables, Lemma 5.1 (pp. 118-119);
    # Lemma 5.2 and H_n (pp. 119-122); RANDOMIZED-HIRE-ASSISTANT, Lemma 5.3
    # (pp. 122-124); PERMUTE-BY-SORTING, RANDOMIZE-IN-PLACE, Lemmas 5.4-5.5
    # (pp. 124-128); Section 5.4 named, with the on-line hiring problem.
    {
        "slug": "the-hiring-problem-and-randomized-algorithms",
        "title": "The Hiring Problem and Randomized Algorithms",
        "module": "Chapter 5 · Probabilistic Analysis and Randomized Algorithms",
        "one_line": "Hiring every candidate better than all before costs n hires in the worst case and H_n ≈ ln n on a random order, a fact proved with indicator random variables, and shuffling the list first makes that expectation hold for every input.",
        "summary": (
            "Chapter 5 analyses a procedure whose cost depends on the order of its input. Hiring "
            "each candidate better than the current one costs n hires in the worst case; if the "
            "order is uniformly random, the expected number of hires is the harmonic number H_n, "
            "found in a few lines with indicator random variables. Randomizing the order turns "
            "that average into a guarantee about expectation for every input. Count hires by "
            "hand, then let the lab average them over every order of eight or nine candidates."
        ),
        "key": [
            "hire whenever a candidate beats the best",
            "cost: c_i·n to interview, c_h·m to hire",
            "worst case: increasing order, n hires",
            "I{A} is 1 if A occurs; E[I{A}] = Pr{A}",
            "Pr{candidate i is hired} = 1/i",
            "expected hires = H_n = ln n + O(1)",
            "shuffle first: the bound holds for any input",
        ],
        "key_label": "Sections 5.1 to 5.3 in seven lines",
        "concepts_intro": (
            "Three ideas that the rest of the book uses for quicksort, hashing, selection and "
            "much else."
        ),
        "concepts": [
            ("Probabilistic analysis",
             "Analysing an algorithm under an assumption about the distribution of its inputs, "
             "and reporting the average cost over that distribution. For the hiring problem the "
             "assumption is that every order of the candidates' ranks is equally likely."),
            ("Indicator random variable",
             "`I{A}` is 1 if the event A occurs and 0 if not. Its expectation is `Pr{A}` "
             "(Lemma 5.1), so a count written as a sum of indicators has an expectation that is "
             "a sum of probabilities, by linearity of expectation."),
            ("Randomized algorithm",
             "An algorithm whose behaviour depends on random choices it makes itself, through a "
             "random-number generator. Its expected cost is over its own choices, for each "
             "input, so no particular input is bad for it."),
        ],
        "read_title": "The chapter's argument first, then the averages",
        "read_intro": (
            "Read Sections 5.1 to 5.3 in your own copy first, with Appendix C nearby if "
            "probability is rusty. The lesson sets out the analysis in its own words, counts one "
            "order by hand, and then averages the hires over every order in the lab."
        ),
        "body": [
            ("p", "&ldquo;The hiring problem models how often we update our notion of which "
                  "element is currently winning.&rdquo; The authors say it in Section 5.1 of a "
                  "story about an employment agency, and the remark explains why the story is in "
                  "an algorithms book: keeping a running maximum is everywhere. This lesson reads "
                  "Chapter 5's first three sections and names the fourth."),
            ("p", "The story: an agency sends you one candidate a day for an office assistant's "
                  "job. You interview each, and whenever a candidate is better than your current "
                  "assistant, you fire the assistant and hire the candidate. HIRE-ASSISTANT "
                  "starts with a dummy candidate worse than everyone. Interviewing costs a small "
                  "`c_i` and hiring a large `c_h`, so with m hires the cost is `O(c_i·n + c_h·m)`. "
                  "The interviews always cost `c_i·n`; the analysis is about m. In the worst case, "
                  "candidates arrive in increasing order of quality and every one is hired."),
            ("p", "Probabilistic analysis needs an assumption about the input. The authors give "
                  "each candidate a distinct rank from 1 to n, higher meaning better, so that an "
                  "arrival order is a permutation of the ranks, and they assume each of the n! "
                  "permutations is equally likely: a <em>uniform random permutation</em>. The "
                  "average cost over that distribution is the average-case cost. Where no "
                  "distribution can be justified, probabilistic analysis cannot be used, and that "
                  "is where randomized algorithms come in: if you choose the order yourself, at "
                  "random, the distribution is yours. A randomized algorithm calls a generator "
                  "RANDOM(a, b) and its cost is an <em>expected</em> cost over those choices."),
            ("def", ("Indicator random variable",
                     "For an event A, `I{A}` is 1 if A occurs and 0 otherwise. "
                     "<strong>Lemma 5.1</strong>: if `X_A = I{A}`, then `E[X_A] = Pr{A}`. The "
                     "authors' warm-up is counting the heads when a fair coin is tossed n times, the sum "
                     "of n indicators each with expectation 1/2, so n/2 heads expected, with no "
                     "need for the binomial distribution.")),
            ("thm", ("Lemma 5.2",
                     "Let `X_i = I{candidate i is hired}` and `X = X_1 + … + X_n`. Candidate i is "
                     "hired exactly when it is the best of the first i, and in a uniform random "
                     "order each of the first i is equally likely to be best, so `E[X_i] = 1/i`. By "
                     "linearity, `E[X] = 1 + 1/2 + … + 1/n = H_n = ln n + O(1)`, and the "
                     "average-case hiring cost is `O(c_h·ln n)`.")),
            ("p", "The proof never computes the distribution of X, the probability of exactly m "
                  "hires, which would be much harder. Linearity of expectation needs no "
                  "independence among the `X_i`; Appendix C states it for any random variables. "
                  "The result is striking for its size: on a random order of a thousand "
                  "candidates you expect to hire about 7.5 of them, not hundreds."),
            ("math", [
                "harmonic numbers, exactly",
                "",
                "H_1 = 1        H_2 = 3/2      H_4 = 25/12 ≈ 2.08",
                "H_8 = 761/280 ≈ 2.72          H_9 = 7,129/2,520 ≈ 2.83",
                "ln n < H_n ≤ ln n + 1",
            ]),
            ("p", "Section 5.3 moves the randomness into the algorithm. RANDOMIZED-HIRE-ASSISTANT "
                  "first permutes the list of candidates at random and then runs the old loop. "
                  "Lemma 5.3 gives the same `O(c_h·ln n)`, but as an expected cost for any input, "
                  "with no assumption about the agency. The authors spell out the difference: "
                  "Lemma 5.2 assumes something about the input and averages over inputs; Lemma "
                  "5.3 assumes nothing and averages over the algorithm's own coin flips. A rival "
                  "who knows the code cannot choose a bad order, because the algorithm does not "
                  "use the order it is given."),
            ("p", "That leaves how to permute an array uniformly at random. PERMUTE-BY-SORTING "
                  "gives each element a random priority from 1 to `n³`, which makes all the "
                  "priorities distinct with probability at least `1 − 1/n`, and sorts by them; "
                  "Lemma 5.4 shows every permutation is then equally likely. RANDOMIZE-IN-PLACE "
                  "is better, `O(n)` time and no extra array: at step i it swaps `A[i]` with an "
                  "element chosen uniformly from `A[i..n]`. Lemma 5.5's proof is a loop invariant "
                  "about the probability that the prefix holds each possible arrangement of "
                  "i − 1 elements. The authors warn that showing each element equally likely to "
                  "land in each position is not enough for uniformity."),
            ("p", "Section 5.4, starred, applies the same tools further: the birthday paradox, "
                  "balls and bins, the longest streak of heads, and the on-line hiring problem, "
                  "where you may hire only once: interview and reject the first `n/e` candidates, "
                  "then hire the first who beats them all, and you hire the best with probability "
                  "at least `1/e`. The course leaves those to the book."),
            ("p", "Now the lab. Type an interview order as a permutation of the ranks 1 to n, "
                  "and the costs `c_i` and `c_h`. The tiles are the hires on that order with the "
                  "positions hired, their cost `c_i·n + c_h·hires`, the exact average number of "
                  "hires over every one of the n! orders (up to n = 9), `H_n` as a fraction, "
                  "whether the two agree, and the expected cost `c_i·n + c_h·H_n`."),
            ("p", "The worked example <code>one-order</code>, `[3, 6, 2, 7, 1, 8, 5, 4]`, hires "
                  "4 times, at positions 1, 2, 4 and 6, at cost 48 with `c_i = 1` and `c_h = 10`. "
                  "The average over all 40,320 orders of eight candidates is 761/280, about 2.72, "
                  "exactly `H_8`, and the expected cost is 985/28, about 35.18. Choose "
                  "<code>increasing</code>: 8 hires and cost 88, the worst case. Choose "
                  "<code>best-first</code>, where the best candidate comes first: 1 hire and cost "
                  "18. The average does not move, because it is over all orders, not this one."),
            ("p", "In <code>nine</code>, with `c_i = 2` and `c_h = 30`, the order `[4, 9, 1, 6, "
                  "3, 8, 2, 7, 5]` hires twice, at cost 78, and the average over 362,880 orders is "
                  "7,129/2,520, `H_9`. In <code>twenty</code> the lab no longer averages, since "
                  "20! orders are too many, but still prints `H_20`, about 3.60; the order given "
                  "hires 5 times. From here on only the proof covers the average."),
            ("h3", "Exercise"),
            ("p", "For the order `[5, 2, 7, 4, 8, 1, 6, 3]`, list the hires by hand and compute "
                  "the cost with `c_i = 1` and `c_h = 10`. Then compute `E[X_3]` and `E[X_8]`, the "
                  "probabilities that the third and the eighth candidates are hired on a random "
                  "order, and check the hires and the average in the lab."),
            ("p", "That completes Part I. The next course, Sorting and Order Statistics, opens "
                  "with Heaps and Building a Heap, and its quicksort lessons use this chapter's "
                  "indicator variables and randomization again."),
        ],
        "lab": ("itakit", {
            "mode": "hiring",
            "view": "order",
            "preset": "one-order",
            "presets": [
                {"id": "one-order", "label": "Eight candidates in one interview order",
                 "order": "3 6 2 7 1 8 5 4",
                 "expect": {"hriHires": "4: candidates 1, 2, 4, 6", "hriCost": "48",
                            "hriAverage": "761/280 ≈ 2.72 over 40,320 orders",
                            "hriHarmonic": "761/280 ≈ 2.72",
                            "hriAgree": "yes: the average is H_8",
                            "hriExpectedCost": "985/28 ≈ 35.18"}},
                {"id": "increasing", "label": "Eight candidates, each better than the last",
                 "order": "1 2 3 4 5 6 7 8",
                 "expect": {"hriHires": "8: candidates 1, 2, 3, 4, 5, 6, 7, 8", "hriCost": "88"}},
                {"id": "best-first", "label": "Eight candidates, the best one first",
                 "order": "8 1 2 3 4 5 6 7",
                 "expect": {"hriHires": "1: candidate 1", "hriCost": "18",
                            "hriAverage": "761/280 ≈ 2.72 over 40,320 orders"}},
                {"id": "nine", "label": "Nine candidates, interview 2 and hire 30",
                 "order": "4 9 1 6 3 8 2 7 5", "ci": "2", "ch": "30",
                 "expect": {"hriHires": "2: candidates 1, 2", "hriCost": "78",
                            "hriAverage": "7,129/2,520 ≈ 2.83 over 362,880 orders",
                            "hriExpectedCost": "8,641/84 ≈ 102.87"}},
                {"id": "twenty", "label": "Twenty candidates in one interview order",
                 "order": "7 2 12 15 4 19 1 9 20 3 11 6 14 5 17 10 18 8 16 13",
                 "expect": {"hriHires": "5: candidates 1, 3, 4, 6, 9",
                            "hriAverage": "not run: n > 9 (20! orders)",
                            "hriHarmonic": "55,835,135/15,519,504 ≈ 3.60"}},
            ],
            "panel_title": "Hires on one order, and on every order",
            "panel_intro": (
                "Type the candidates' ranks in interview order, higher meaning better, and the two "
                "costs. The lab runs HIRE-ASSISTANT on that order, then on every order of the same "
                "candidates, and sets the exact average beside the harmonic number H_n."
            ),
        }),
        "steps_title": "Computing an expectation with indicators",
        "steps_intro": "Four steps for the hiring count, then one count of your own.",
        "steps": [
            ("Write the count as a sum of indicators",
             "Hires `X = X_1 + … + X_n`, with `X_i = 1` if candidate i is hired. Every count that "
             "is a number of events can be written this way."),
            ("Find each indicator's probability",
             "Candidate i is hired when it is the best of the first i. In a uniform random order "
             "each of those i is equally likely to be the best, so the probability is 1/i."),
            ("Add the probabilities",
             "By Lemma 5.1 and linearity, `E[X] = Σ 1/i = H_n`. No independence is needed."),
            ("Check it by brute force at small n",
             "List all 6 orders of three candidates, count the hires on each, and average: you "
             "should get `H_3 = 11/6`."),
            ("Count something of your own",
             "Write the expected number of positions i for which `A[i] > A[i + 1]` in a random "
             "permutation of n distinct keys as a sum of indicators, compute it, and check it by "
             "hand for n = 3."),
        ],
        "worked": {
            "title": "One order of eight, and the average",
            "intro": [
                "Interview the order `[3, 6, 2, 7, 1, 8, 5, 4]`, the lab's example "
                "<code>one-order</code>, with `c_i = 1` and `c_h = 10`.",
            ],
            "lines": [
                "rank 3: beats the dummy, hire (1)",
                "rank 6: beats 3, hire (2)",
                "rank 2: no",
                "rank 7: beats 6, hire (3)",
                "rank 1: no",
                "rank 8: beats 7, hire (4)",
                "ranks 5, 4: no",
                "cost 8·1 + 4·10 = 48",
                "expected: 8 + 10·761/280 ≈ 35.18",
            ],
            "after": [
                "This order hired more than the average of about 2.72. Positions 1, 2, 4 and 6 "
                "were hired, with probabilities 1, 1/2, 1/4 and 1/6 on a random order; the sum "
                "of all eight probabilities, `H_8`, is the expectation the lab confirms by "
                "averaging all 40,320 orders.",
            ],
        },
        "quiz_title": "Hires, indicators and randomization",
        "quiz": [
            {"q": "For the exercise order `[5, 2, 7, 4, 8, 1, 6, 3]` with `c_i = 1` and "
                  "`c_h = 10`, how many hires are made and at what cost?",
             "a": ["3 hires, cost 30", "3 hires, cost 38", "4 hires, cost 48",
                   "about 2.72 hires, cost about 35.18"],
             "c": 1,
             "why": "Ranks 5, 7 and 8 are hired, at positions 1, 3 and 5, so the cost is "
                    "`8·1 + 3·10 = 38`. Thirty leaves out the eight interviews, which are always "
                    "paid. Four hires and 48 belong to the lesson's worked order. About 2.72 is "
                    "`H_8`, the average over all orders, not the count on this one. (For the "
                    "second part, `E[X_3] = 1/3` and `E[X_8] = 1/8`.)"},
            {"q": "In a uniform random order of 8 candidates, what is the probability that the "
                  "fifth candidate interviewed is hired?",
             "a": ["1/8", "1/5", "5/8", "1/2"],
             "c": 1,
             "why": "The fifth is hired exactly when it is the best of the first five, and each "
                    "of the five is equally likely to be best, so 1/5. One in eight is the chance "
                    "it is the best of all. Five-eighths is the chance its rank "
                    "is among the top five of eight, which is not what hiring needs. One half confuses beating the previous "
                    "candidate with beating all previous ones."},
            {"q": "What is the expected number of hires for 4 candidates in a uniform random "
                  "order?",
             "a": ["2", "25/12", "5/2", "ln 4 ≈ 1.39"],
             "c": 1,
             "why": "`H_4 = 1 + 1/2 + 1/3 + 1/4 = 25/12`, about 2.08, and averaging the hires over "
                    "all 24 orders gives exactly that. Two is n/2. Five-halves is the average "
                    "rank. `ln 4` is below `H_4`, which lies between `ln n` and `ln n + 1`."},
            {"q": "RANDOMIZED-HIRE-ASSISTANT permutes the list uniformly at random before "
                  "interviewing. Which statement is true?",
             "a": ["It never hires more than ln n + 1 candidates",
                   "Its expected hiring cost is O(c_h·ln n) for every input order, increasing "
                   "order included",
                   "Its analysis assumes the agency sends candidates in random order",
                   "Its expected cost is lower than HIRE-ASSISTANT's average-case cost"],
             "c": 1,
             "why": "Lemma 5.3 is an expectation over the algorithm's own random permutation, so "
                    "it holds whatever order arrives. It can still hire all n, if its shuffle "
                    "happens to come out increasing, with probability 1/n!. It assumes nothing "
                    "about the agency; that was Lemma 5.2. And the two bounds are the same "
                    "`O(c_h·ln n)`; what changes is what the expectation is over."},
        ],
        "mistakes": [
            ("Treating an average over inputs as a guarantee for your input",
             "Lemma 5.2's `H_n` is the average over all orders, under the assumption that every "
             "order is equally likely. A particular agency may send candidates in increasing "
             "order every time, and then HIRE-ASSISTANT hires n of them. On the lesson's "
             "illustration the average is 2.72 hires while the increasing order hires 8. "
             "Randomizing the order first, as Section 5.3 does, is what makes the expectation "
             "hold for every input."),
            ("Expecting to need the distribution of the count",
             "Computing the probability of exactly m hires for every m is hard; the expectation "
             "is easy, because X is a sum of indicators and each indicator's expectation is a "
             "probability you can read off. The coin-flip warm-up gets n/2 heads the same way, "
             "without the binomial distribution."),
            ("Believing linearity of expectation needs independence",
             "`E[X + Y] = E[X] + E[Y]` holds for any random variables, dependent or not, as "
             "Appendix C states. The argument for `H_n` uses only that, and the probability 1/i "
             "for each candidate; it never asks whether the events are independent. Products of "
             "random variables are where independence matters."),
        ],
        "standard": (
            "Finish when you can compute an expected count with indicator random variables.",
            "Given a procedure and a uniform random input, write a count as a sum of indicators, "
            "find each probability, sum them, and check the result by averaging over every input "
            "at a small n."
        ),
        "note": (
            "The lab's average is computed exactly by running the loop on every order, which is "
            "possible only up to nine candidates. It confirms the expectation at those sizes; "
            "Lemma 5.2 proves it for every n. The lab does not simulate random shuffles, so the "
            "randomized algorithm's guarantee is the lemma's, not the lab's."
        ),
    },
]
