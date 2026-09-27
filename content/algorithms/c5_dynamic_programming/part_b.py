"""Dynamic Programming and Optimal Substructure, lessons 07-12 - alignment, sequences, counting, and the tables that are not grids."""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "edit-distance-and-performing-the-script",
        "title": "Edit Distance, and Performing the Script",
        "module": "Two axes, and reading the answer back",
        "one_line": "Fill the edit-distance table for two words, read the edit script back out of it, and carry that script out on the first word character by character.",
        "summary": (
            "Two prefixes index this table, one per string, and each cell reads exactly three "
            "neighbours. The number it produces is checked against a recursion with no table; "
            "the script it produces is checked by being <em>performed</em>, one operation at a "
            "time, on the word it claims to transform &mdash; refusing if an operation names a "
            "character that is not there. A script of the right length and the wrong content "
            "cannot survive that."
        ),
        "key": [
            "D(i, j) = min of   D(i−1, j) + 1        delete the i-th character",
            "                   D(i, j−1) + 1        insert the j-th character",
            "                   D(i−1, j−1) + cost   keep if equal, else substitute",
            "",
            "kitten to sitting:  distance 3,  56 cells,  29 737 calls without a table",
            "  substitute k for s, keep itt, substitute e for i, keep n, insert g",
            "  seven operations, three of which cost anything",
        ],
        "key_label": "Three neighbours per cell, and the script the pointers spell out",
        "concepts_intro": (
            "The hard idea is the last one: a reconstruction can be checked by executing it, "
            "which is a stronger check than comparing two numbers."
        ),
        "concepts": [
            ("Two prefixes are the state, and three neighbours are the recurrence",
             "`D(i, j)` is the cheapest way to turn the first `i` characters of the first word "
             "into the first `j` of the second. The last operation is a delete, an insert, or "
             "a keep-or-substitute, and those three are exactly the cell above, the cell to "
             "the left, and the cell diagonally back. The base row and column are `j` and `i` "
             "&mdash; turning nothing into a prefix costs one insert per character."),
            ("The script is a path, and its length is not the distance",
             "Walking the recorded pointers from the bottom-right corner to the origin gives a "
             "sequence of operations. On kitten and sitting there are seven of them and the "
             "distance is three, because four are keeps and a keep costs nothing. Confusing "
             "the two counts is the commonest reading error on this page, and the panel prints "
             "both figures in separate rows for that reason."),
            ("Performing the script is a stronger check than costing it",
             "Every operation names the character it acts on: delete the `t` at position 3, "
             "keep the `n`, substitute `e` for `i`. Carrying the script out means walking the "
             "first word and refusing as soon as an operation names a character that is not "
             "where it says. A wrong reconstruction of the right length passes a cost check "
             "and fails this one, because the characters are what it gets wrong."),
        ],
        "read_title": "Three neighbours, one script, and the script carried out",
        "read_intro": "The recurrence and its proof, the walk back, why performing beats costing, and the two counts that diverge.",
        "body": [
            ("def", ("Edit distance",
                     "The <strong>edit distance</strong> between strings `a` and `b` is the "
                     "fewest single-character operations &mdash; insert, delete, substitute "
                     "&mdash; that turn `a` into `b`. Each costs one; keeping a character "
                     "costs nothing and is not an operation in the count, though it is a step "
                     "in the script.")),
            ("thm", ("The edit recurrence",
                     "With `D(i, 0) = i` and `D(0, j) = j`, for `i, j ≥ 1`: "
                     "`D(i, j) = min( D(i−1, j) + 1, D(i, j−1) + 1, D(i−1, j−1) + c )`, where "
                     "`c` is 0 if the `i`-th character of `a` equals the `j`-th of `b` and 1 "
                     "otherwise.")),
            ("proof", ("Consider a cheapest sequence of operations turning `a[1..i]` into "
                       "`b[1..j]` and look at what happens to the last character of each. "
                       "Either `a[i]` is deleted, in which case the rest is a cheapest way of "
                       "turning `a[1..i−1]` into `b[1..j]`, costing `D(i−1, j) + 1`; or "
                       "`b[j]` is inserted, giving `D(i, j−1) + 1`; or `a[i]` is aligned with "
                       "`b[j]`, kept if they are equal and substituted otherwise, giving "
                       "`D(i−1, j−1) + c`.",
                       "In each case the remaining sub-sequence must itself be cheapest, or "
                       "substituting a cheaper one would beat the original &mdash; optimal "
                       "substructure again, discharged by the same substitution argument as "
                       "every other page on this course. No other last step is possible, so "
                       "the minimum over three cases is the distance.")),
            ("p", "Filling this table in row-major order is correct, and it is worth pausing "
                  "on why, given &ldquo;The Fill Order Is Part of the Algorithm&rdquo;. The "
                  "three cells a cell reads are "
                  "`(i−1, j)`, `(i, j−1)` and `(i−1, j−1)`: one row up, one column left, and "
                  "both. Row-major writes every cell of row `i−1` before any of row `i`, and "
                  "within row `i` it writes column `j−1` before column `j`. All three reads "
                  "are therefore already written, and the count of reads landing on unwritten "
                  "cells is zero. The fill order is not always wrong; it is always something "
                  "to check."),
            ("example", ("Kitten to sitting, three ways",
                         "The table is 7 by 8, fills 56 cells and makes 126 reads, and its "
                         "corner is 3. A recursion with no table at all reaches 3 after 29 737 "
                         "calls. The script the pointers spell out is: substitute `k` for `s`, "
                         "keep `i`, keep `t`, keep `t`, substitute `e` for `i`, keep `n`, "
                         "insert `g`. Performing that on `kitten`, character by character, "
                         "produces `sitting`, and the panel compares that string with the "
                         "second word rather than trusting the walk.")),
            ("h3", "Why the script is carried out rather than added up"),
            ("p", "Suppose the walk back followed one wrong pointer and returned a script that "
                  "still had three paid operations. Costing it would give 3, matching the "
                  "table, and the check would pass. Performing it would not: a delete that "
                  "names the wrong character, or a keep whose character is not where the "
                  "script says, stops the execution and the panel reports that the script "
                  "could not be performed. The stronger check is available because the object "
                  "here is a program, and a program can be run."),
            ("p", "This generalises past strings. Whenever a reconstruction is a sequence of "
                  "steps rather than a set, executing it against the input is strictly more "
                  "informative than re-costing it, and usually no harder to write. The "
                  "knapsack's set could only be re-weighed; this script can be run."),
            ("h3", "Two counts, and the bound that is loose"),
            ("p", "The measured figures are 56 cells against 29 737 calls on two words of six "
                  "and seven letters. The proved bounds are `Θ(mn)` for the table and, for the "
                  "memo-free recursion, at most `3^(m+n)` calls because each call makes three "
                  "and the arguments shrink by at least one in total. For `kitten` and "
                  "`sitting` that upper bound is `3^13`, which is 1 594 323 &mdash; true, and "
                  "roughly fifty times the measured 29 737."),
            ("p", "That gap is worth naming rather than smoothing over. The bound is an "
                  "over-count because many branches hit a base case early and because the "
                  "three recursive calls do not all reduce the same amount. A measurement "
                  "cannot repair a loose bound; it can only tell you that on this input the "
                  "truth is well below it. Change the pair to `sunday` and `saturday` and the "
                  "measured count is 60 121 against a bound of `3^14`, so the ratio moved "
                  "without either number being wrong."),
            ("p", "One more count that does not mean what it looks like: the panel reports "
                  "seven operations in the script and a distance of three. Four of the seven "
                  "are keeps. A reader who quotes the script's length as the distance has "
                  "reported the length of a path instead of the cost of one, and on "
                  "`dog` to `dogma` the two numbers are five and two."),
        ],
        "lab": ("dpkit", {
            "mode": "edit",
            "preset": "kitten",
            "panel_title": "Choose two words, then explain one cell of the alignment",
            "panel_intro": "Letters only, so every column of the table is visible. The two "
                           "range controls pick a cell and the panel paints the three cells it "
                           "read; the script under the table is performed on the first word "
                           "and the result compared with the second.",
        }),
        "steps_title": "Building an alignment table and checking what it returns",
        "steps_intro": "Four steps, and the last one is the one that distinguishes this page from the two before it.",
        "steps": [
            ("Index by prefixes, and say what the empty prefixes cost",
             "`D(i, 0) = i` and `D(0, j) = j`, because turning a prefix into nothing is one "
             "delete per character. Getting the base row wrong is the commonest way to build "
             "a table that is off by a constant everywhere and looks fine in the middle."),
            ("Enumerate the possible last operations, not the possible first ones",
             "Three of them here, and they map onto three neighbours. If you find yourself "
             "with four cases or with a case that does not reduce both indices or one, the "
             "state is not two prefixes and the table will not close."),
            ("Check the fill order even when it is obviously fine",
             "Row-major is correct here and the count of reads landing on unwritten cells is "
             "zero. Checking costs one glance at the painting and it is the difference between "
             "knowing and assuming, which the matrix chain has already shown is not a small "
             "difference."),
            ("Recover the script as operations that name their characters",
             "A step that says only `substitute` is not checkable. A step that says "
             "`substitute e for i at position 5` can be performed, and performing it is what "
             "turns the reconstruction from a claim into a demonstration."),
            ("Perform the script and compare the result with the target",
             "Run it on the first word, refusing on the first operation whose character is not "
             "where it says, and compare the output with the second word. Report the "
             "distance and the script length separately; they are different numbers."),
        ],
        "worked": {
            "title": "Kitten to sitting: the table, the path, and the script performed",
            "intro": [
                "Rows are prefixes of kitten, columns are prefixes of sitting. The top row and "
                "left column are the costs of turning a prefix into nothing and nothing into a "
                "prefix.",
            ],
            "lines": [
                "               s   i   t   t   i   n   g",
                "          0    1   2   3   4   5   6   7",
                "    k     1    1   2   3   4   5   6   7",
                "    i     2    2   1   2   3   4   5   6",
                "    t     3    3   2   1   2   3   4   5",
                "    t     4    4   3   2   1   2   3   4",
                "    e     5    5   4   3   2   2   3   4",
                "    n     6    6   5   4   3   3   2   3",
                "",
                "the corner is 3, and the walk back gives the script",
                "",
                "    substitute k for s      paid",
                "    keep i",
                "    keep t",
                "    keep t",
                "    substitute e for i      paid",
                "    keep n",
                "    insert g                paid",
                "",
                "seven operations, three of them paid    ->    distance 3",
                "",
                "performing it on kitten, one step at a time:",
                "    k i t t e n   ->   s i t t e n   ->   s i t t i n   ->   s i t t i n g",
                "the result is sitting, which is the second word",
            ],
            "after": [
                "Each paid operation moves the walk diagonally or sideways and each keep moves "
                "it diagonally for free. The four keeps are why the script is longer than the "
                "distance, and they are also why the alignment is readable: `itt` and `n` "
                "survive intact from one word to the other, and the script says so rather "
                "than reporting three anonymous edits.",
                "The execution is the check. It walks `kitten` from the left with a cursor, "
                "and every operation but `insert` has to find its named character under that "
                "cursor. Swap two operations in the script and the execution stops; drop one "
                "and the cursor finishes short of the end of the word, which the panel also "
                "refuses. Only a script that is right about every character survives.",
                "For a faded rehearsal, change the words to `abc` and `xyz` before running "
                "it. The supplied first move: no character of one appears in the other, so no "
                "keep is possible and no insert or delete can help, which fixes the distance "
                "at 3 &mdash; the largest it can be when the lengths match. Predict the "
                "script's length as well as its cost, and check both.",
            ],
        },
        "quiz_title": "Cells, scripts, and the difference between costing and performing",
        "quiz": [
            {"q": "The panel reports seven operations in the script and an edit distance of three. Which is right?",
             "a": ["Three: the script has been mis-costed",
                   "Seven: the distance is the number of steps the walk took",
                   "Both, of different things: four of the seven are keeps, which are steps and not edits",
                   "Neither: the distance should be the number of paid operations plus the number of keeps"],
             "c": 2,
             "why": "A keep is a step in the alignment and costs nothing, so the script's "
                    "length and its cost are different numbers and the panel prints both. On "
                    "`dog` to `dogma` they are five and two. Reporting the length as the "
                    "distance is the commonest reading error on this page."},
            {"q": "Why is the script performed on the first word rather than simply costed?",
             "a": ["Because costing it would require the table, and the check must be independent",
                   "Because a wrong script of the right cost passes a cost check, and performing it catches the characters it names",
                   "Because the distance is not known until the script is performed",
                   "Because performing it is cheaper than adding up three numbers"],
             "c": 1,
             "why": "The failure mode is a script of the right length with the wrong contents, "
                    "and cost alone cannot see it. Performing refuses as soon as an operation "
                    "names a character that is not under the cursor. Costing does not need "
                    "the table either, and the distance is known from the corner cell before "
                    "any script exists."},
            {"q": "The memo-free recursion makes 29 737 calls on kitten and sitting, against an upper bound of `3^13`, which is 1 594 323. What does the gap show?",
             "a": ["The bound is wrong and should be corrected downward",
                   "The measurement is unreliable, since a recursion's call count is not deterministic",
                   "The bound is true and loose on this input, and a measurement cannot tighten it",
                   "The recursion must be memoising something implicitly"],
             "c": 2,
             "why": "`3^(m+n)` over-counts because many branches reach a base case early and "
                    "the three calls do not all reduce the same amount. The bound is a correct "
                    "upper bound; the measurement says where this input sits under it. The "
                    "count is deterministic and there is no memo &mdash; the memoised version "
                    "would make far fewer than 56 calls."},
            {"q": "Row-major fill is correct for the edit table but wrong for the matrix chain. What decides it?",
             "a": ["Whether the table is square",
                   "Whether every cell's reads are written before that cell is visited, which is checkable by counting",
                   "Whether the recurrence takes a minimum or a maximum",
                   "Whether the base cases lie on the first row and column"],
             "c": 1,
             "why": "The edit table reads one row up and one column left, both of which "
                    "row-major has already written; the chain table reads cells below the "
                    "diagonal, which it has not. The count of reads landing on unwritten cells "
                    "is zero here and 35 there, and that count is the test. Shape, direction "
                    "of the optimum and base-case placement decide nothing on their own."},
        ],
        "mistakes": [
            ("Reporting the script's length as the distance",
             "Seven against three on the lab's default pair. Keeps are steps in the alignment "
             "and cost nothing, and a script with many keeps is a sign the two strings are "
             "similar rather than a sign it is expensive. Print the two numbers separately "
             "and the confusion cannot survive."),
            ("Checking a reconstruction only by its cost",
             "The cost check compares two numbers and passes whenever the wrong object "
             "happens to cost the right amount, which for a path of fixed length is not rare. "
             "When the object is a sequence of steps, run it. That is available here and was "
             "not available for the knapsack's set of items."),
            ("Assuming row-major is safe because it worked here",
             "It is safe here for a reason that can be stated and counted: the three "
             "neighbours are all written before the cell is reached. The same order on the "
             "chain table reads 35 cells early and reports a number two-fifths low. The "
             "order is a property of the recurrence, never of habit."),
        ],
        "standard": ("Finish when you can recover a script from a table and check it by running it.",
                     "You should be able to write the three-case recurrence with its base row "
                     "and column, confirm that row-major respects the reads by counting, walk "
                     "the pointers back into operations that name their characters, and "
                     "separate the script's length from its cost."),
        "note": ("Every table so far has answered with a number and been asked, separately, "
                 "for an object. The next lesson has two algorithms that agree on the number "
                 "and disagree about the object, and one of them is not carrying an answer at "
                 "all."),
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "the-tails-array-is-not-the-subsequence",
        "title": "The Tails Array Is Not the Subsequence",
        "module": "Sequences, and counting rather than optimising",
        "one_line": "Run both longest-increasing-subsequence algorithms on one sequence, check what each returns against two properties, and find where the faster one stops being an answer.",
        "summary": (
            "Two algorithms find the same length. The quadratic table stores, for each "
            "position, the longest increasing run ending there, and a predecessor, so the run "
            "itself can be read back. The binary-search method keeps the smallest possible "
            "last value for each length and finds the same number far faster &mdash; and what "
            "it holds at the end is not a subsequence of the input, though on the sequence in "
            "front of you it happens to be one."
        ),
        "key": [
            "table:  best(i) = 1 + max of best(j) over j < i with a(j) < a(i)",
            "tails:  tails(L) = the smallest value that can end an increasing run of length L",
            "",
            "10 9 2 5 3 7 101 18 4 8",
            "  the table    length 4    2 5 7 101    45 comparisons",
            "  the tails    length 4    2 3 4 8      14 comparisons",
            "  every subsequence        length 4     1024 examined",
        ],
        "key_label": "Two routes to one length, and two different arrays at the end of them",
        "concepts_intro": (
            "The hard idea is the invariant the tails array maintains, which is about lengths "
            "and not about any particular run, and which is why its contents need not be a run "
            "at all."
        ),
        "concepts": [
            ("The table stores an answer per position, and a predecessor",
             "`best(i)` is the length of the longest increasing subsequence ending exactly at "
             "position `i`. It is one more than the largest `best(j)` over earlier positions "
             "holding smaller values, and recording which `j` attained that maximum makes the "
             "subsequence recoverable. The whole array takes `Θ(n²)` comparisons &mdash; 45 on "
             "ten values &mdash; and the answer is the largest entry."),
            ("The tails array stores a bound per length, not a run",
             "`tails(L)` is the smallest value that can end an increasing subsequence of "
             "length `L` among the elements seen so far. Each new value replaces the first "
             "entry that is at least as large, or extends the array. The invariant is about "
             "what is achievable at each length; nothing says the entries occur in the input "
             "in that order, and usually they do not."),
            ("Two properties, checked separately, and one of them is the trap",
             "An answer must be increasing and must be a subsequence of the input. The tails "
             "array is always increasing &mdash; that is forced by the invariant &mdash; so "
             "checking only that property will never catch it. On the lab's default sequence "
             "it also happens to be a subsequence, which is worse: the check passes and the "
             "array still is not the answer the table found. Switch to the sequence with "
             "repeats and the subsequence check fails outright."),
        ],
        "read_title": "Two algorithms, one length, and the array that is not an answer",
        "read_intro": "The quadratic table, the binary-search invariant, the two checks, and the instance where agreement is a coincidence.",
        "body": [
            ("def", ("Longest increasing subsequence",
                     "A <strong>subsequence</strong> of a sequence is what is left after "
                     "deleting zero or more entries, keeping the rest in order. It is "
                     "<strong>strictly increasing</strong> if each entry is larger than the "
                     "one before. The problem is to find a longest strictly increasing "
                     "subsequence; there may be many, and the lesson is careful never to call "
                     "one of them <em>the</em> answer.")),
            ("thm", ("The per-position recurrence",
                     "Let `best(i)` be the length of the longest strictly increasing "
                     "subsequence ending at position `i`. Then `best(i) = 1` if no earlier "
                     "position holds a smaller value, and otherwise `best(i) = 1 + max` of "
                     "`best(j)` over positions `j &lt; i` with `a(j) &lt; a(i)`. The answer is "
                     "the maximum over all `i`.")),
            ("proof", ("A longest increasing subsequence ending at `i` has some "
                       "second-to-last entry, at a position `j &lt; i` with `a(j) &lt; a(i)`, "
                       "unless it consists of `a(i)` alone. Removing `a(i)` leaves an "
                       "increasing subsequence ending at `j`, and it must be a longest one, or "
                       "substituting a longer one and re-appending `a(i)` would beat the "
                       "original.",
                       "So the length is `1 + best(j)` for that `j`, and taking the maximum "
                       "over all admissible `j` gives `best(i)`. Every increasing subsequence "
                       "ends somewhere, so the overall answer is the largest `best(i)`, and "
                       "the predecessor recorded at each step reconstructs one witness for "
                       "it.")),
            ("h3", "What the other algorithm maintains"),
            ("p", "The binary-search method processes the values in order and keeps an array "
                  "`tails` in which position `L` holds the smallest value that ends an "
                  "increasing subsequence of length `L + 1` among the values processed so far. "
                  "A new value either extends the array, when it is larger than everything in "
                  "it, or replaces the first entry that is at least as large. Both cases are "
                  "found by binary search, so the whole run is `Θ(n log n)` comparisons "
                  "&mdash; 14 on ten values, against the table's 45."),
            ("p", "Nothing in that description promises the array is a subsequence of the "
                  "input. It is a record of what is achievable at each length, and its entries "
                  "may come from positions in any order, including positions that cannot "
                  "coexist in one run. The length is right, because the array's length is "
                  "exactly the longest achievable, and the contents are a different question."),
            ("example", ("Ten values, and the array that changed its mind",
                         "On `10 9 2 5 3 7 101 18 4 8` the tails array after the seventh value "
                         "is `2 3 7 101`, which is a genuine longest increasing subsequence. "
                         "Then 18 replaces 101, then 4 replaces 7, then 8 replaces 18, and the "
                         "array ends as `2 3 4 8`. The table's reconstruction is `2 5 7 101`. "
                         "Both have length 4 and both are valid answers here; the array "
                         "passed through one valid answer on its way to a different one, and "
                         "nothing about the mechanism guarantees the destination is valid.")),
            ("p", "That last sentence is the whole lesson, and the lab has the instance that "
                  "proves it. Switch the sequence to `3 1 4 1 5 9 2 6 5 3`. The tails array "
                  "ends `1 2 3 6`, which is increasing; the panel's second check asks whether "
                  "it is a subsequence of the input, and the answer is no &mdash; 1, 2 and 3 "
                  "occur in that order, and the only 6 sits before the last 3. The table's "
                  "reconstruction is `3 4 5 9`, which passes both checks."),
            ("h3", "Why two checks, and why the weaker one never fires"),
            ("p", "The panel reports `is increasing` and `is a subsequence of the input` as "
                  "separate verdicts. The first is satisfied by the tails array on every "
                  "input, because the invariant forces it, and by a sorted copy of the input "
                  "too &mdash; which is why it cannot be the only check. The second is the one "
                  "with teeth. A reconstruction that returns the right values in the wrong "
                  "positions fails it, and so does an array that was never a run in the first "
                  "place."),
            ("p", "The third route is the enumeration: every one of the `2ⁿ` subsequences, "
                  "tested for increase, with the longest kept. On ten values that is 1 024 "
                  "subsets, which is instant, and the lab refuses above sixteen values. It "
                  "agrees with both algorithms on the length, which is what makes the "
                  "comparison of the two arrays a comparison rather than a guess."),
            ("p", "The measured comparison counts are 45 and 14 on ten values. The proved "
                  "bounds are `Θ(n²)` and `Θ(n log n)`, and the enumeration is `Θ(2ⁿ n)`. "
                  "Here the three measured numbers and the three bounds agree in order, which "
                  "is worth saying out loud on a course where three pages show them "
                  "disagreeing. What does not follow from the measurement is the shape of "
                  "either curve: 45 and 14 are two numbers, and two numbers fit any pair of "
                  "curves you like."),
        ],
        "lab": ("dpkit", {
            "mode": "lis",
            "preset": "classic",
            "panel_title": "Choose a sequence, and step the tails array forward",
            "panel_intro": "The step control replays the tails array one position at a time, "
                           "so the replacements can be watched rather than described. The "
                           "panel checks the reconstruction for both properties an answer must "
                           "have, and reports separately whether the tails array happens to "
                           "coincide with it.",
        }),
        "steps_title": "Comparing two algorithms that report the same number",
        "steps_intro": "Agreement on a number is the weakest kind of agreement, and it is the one that is easiest to mistake for correctness.",
        "steps": [
            ("Ask what each algorithm's array is for",
             "The table's array holds an answer per position; the tails array holds a bound "
             "per length. Those are different objects with the same shape, and the shape is "
             "what invites the confusion. Write the sentence defining each entry before "
             "comparing them."),
            ("Recover the answer from predecessors, never from the bound array",
             "The subsequence comes out of the table's recorded predecessors. If you need the "
             "run itself and you are using the binary-search method, you must record "
             "predecessors there too &mdash; the tails array alone cannot produce it."),
            ("Check both properties, not the easy one",
             "Increasing, and a subsequence of the input. The first is satisfied by things "
             "that are not answers at all, including a sorted copy of the input, so a check "
             "that stops there has not tested anything the failure mode can fail."),
            ("Try a sequence with repeats before believing a coincidence",
             "On the lab's default the tails array is a valid answer, and on the sequence with "
             "repeats it is not even a subsequence. If an invariant does not promise a "
             "property, a single input exhibiting the property is a coincidence to be checked "
             "against a second input, not evidence."),
            ("Read the comparison counts as two numbers, not as two curves",
             "Forty-five and fourteen at one length. The bounds `Θ(n²)` and `Θ(n log n)` come "
             "from the structure of the loops, and no pair of measurements establishes them."),
        ],
        "worked": {
            "title": "The tails array, one value at a time",
            "intro": [
                "Each line is one value being processed. Position is where the binary search "
                "placed it: past the end extends the array, anywhere else replaces an entry. "
                "The input is 10 9 2 5 3 7 101 18 4 8.",
            ],
            "lines": [
                "value   position   tails afterwards",
                "",
                "   10      0        10",
                "    9      0        9",
                "    2      0        2",
                "    5      1        2 5",
                "    3      1        2 3",
                "    7      2        2 3 7",
                "  101      3        2 3 7 101        <- a valid answer, in passing",
                "   18      3        2 3 7 18",
                "    4      2        2 3 4 18",
                "    8      3        2 3 4 8          <- what it ends as",
                "",
                "the table, meanwhile",
                "",
                "  input      10   9   2   5   3   7 101  18   4   8",
                "  best(i)     1   1   1   2   2   3   4   4   3   4",
                "  prev(i)     -   -   -   2   2   3   5   5   4   5",
                "",
                "  largest best is 4, first attained at 101; walking prev back",
                "  from there gives    2  5  7  101",
                "",
                "every one of the 1024 subsequences agrees: the longest has length 4",
            ],
            "after": [
                "Only the length is shared. The table's run is `2 5 7 101`, occupying "
                "positions 3, 4, 6 and 7 of the input; the tails array is `2 3 4 8`, whose "
                "values occur at positions 3, 5, 9 and 10 and which is also a valid run here. "
                "Two valid answers and one number, and the panel says whether the two "
                "coincided rather than assuming they must.",
                "Watch the seventh line. At that moment the tails array is `2 3 7 101`, a "
                "perfectly good answer, and the algorithm then overwrites it three times "
                "because smaller endings become available. Each of those replacements is "
                "correct for the invariant it maintains &mdash; the smallest possible last "
                "value for each length &mdash; and each of them destroys a run that was there "
                "a moment ago. The array is doing its job; its job is not to hold a run.",
                "For a faded rehearsal, switch the sequence to `3 1 4 1 5 9 2 6 5 3` before "
                "running it. The supplied first move: the value 1 appears twice and equal "
                "values cannot both sit in a strictly increasing run, so the second 1 replaces "
                "rather than extends. Predict the final tails array, then check the panel's "
                "second verdict &mdash; this is the instance where the array is not a "
                "subsequence at all.",
            ],
        },
        "quiz_title": "Lengths, arrays, and the property that does the work",
        "quiz": [
            {"q": "The tails array is always increasing. What does checking that property establish about it?",
             "a": ["That it is a valid longest increasing subsequence",
                   "Nothing the invariant did not already force: a sorted copy of the input is increasing too",
                   "That it is a subsequence of the input, since increasing runs must occur in order",
                   "That its length is correct"],
             "c": 1,
             "why": "Increase is forced by the invariant, so the check can never fail and "
                    "therefore never tests anything. A sorted copy of the input passes it and "
                    "is not an answer. Being increasing says nothing about occurring in the "
                    "input in that order, and the length is correct for a separate reason "
                    "&mdash; the array's length is what the invariant tracks."},
            {"q": "On `10 9 2 5 3 7 101 18 4 8` the tails array ends `2 3 4 8`, which is a valid answer. What does that show?",
             "a": ["That the tails array is the subsequence after all",
                   "That the two algorithms agree on this input, which is why the misconception survives",
                   "That the table's reconstruction `2 5 7 101` is one of several and the array happens to be another",
                   "Both of the previous two, and neither generalises"],
             "c": 3,
             "why": "Both statements are true of this input and neither is true in general: on "
                    "`3 1 4 1 5 9 2 6 5 3` the array ends `1 2 3 6`, which is not a "
                    "subsequence of the input at all. An input on which a wrong idea gives the "
                    "right answer is exactly how a wrong idea survives, which is why the lab "
                    "ships that second sequence."},
            {"q": "You need the subsequence itself and you are using the binary-search method. What do you have to add?",
             "a": ["Nothing: the tails array is the subsequence once the input is sorted",
                   "A predecessor recorded for each position, exactly as the quadratic table does",
                   "A second pass over the tails array to reorder it",
                   "A check that the array is increasing"],
             "c": 1,
             "why": "The run comes from predecessors, and the tails array holds no information "
                    "about which positions its entries came from in combination. Reordering "
                    "cannot help, since the entries need not be able to coexist in one run. "
                    "Checking increase tests nothing, and sorting the input destroys the "
                    "problem."},
        ],
        "mistakes": [
            ("Printing the tails array as the answer",
             "It has the right length, it is increasing, and on many inputs it is even a valid "
             "run &mdash; which is exactly why this shipped as a bug in real code more than "
             "once. The array is a record of the smallest achievable ending per length. The "
             "run comes from predecessors or not at all."),
            ("Checking only that the output is increasing",
             "The property the failure mode has is increase; the property it lacks is being a "
             "subsequence of the input. A check that tests the first and not the second has "
             "been written to pass. The panel reports both, separately, for that reason."),
            ("Concluding from one sequence that the two methods return the same object",
             "They return the same number on every input and the same object on some. The lab "
             "ships four sequences and they differ: on the sorted one the two coincide "
             "exactly, on the default one they are two different valid answers, and on the one "
             "with repeats the array is not an answer at all."),
        ],
        "standard": ("Finish when you can say what each of two arrays holds and which property separates them.",
                     "You should be able to state the per-position recurrence and the tails "
                     "invariant in one sentence each, recover a run from predecessors, check a "
                     "candidate for both required properties, and produce the input on which "
                     "the faster method's array is not an answer."),
        "note": ("Every table so far has optimised something. The next one counts, which "
                 "changes the recurrence from a minimum to a sum, and makes the order of the "
                 "two loops decide not how fast the answer arrives but which question was "
                 "asked."),
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "combinations-or-ordered-sequences",
        "title": "Combinations, or Ordered Sequences",
        "module": "Sequences, and counting rather than optimising",
        "one_line": "Swap the two loops of the coin-counting table and watch the answer change from 541 to a twenty-three-digit number, at identical cost.",
        "summary": (
            "Counting recurrences replace the minimum with a sum, and the change is larger "
            "than it looks: with the coin types on the outside each multiset is built in one "
            "fixed order and counted once, and with the amounts on the outside every ordering "
            "is counted separately. Both loops read the table exactly 295 times on the lab's "
            "instance. One answers 541 and the other 91 197 869 007 632 925 819 218."
        ),
        "key": [
            "coins outside:   for each coin c:  for v = c to k:  ways(v) += ways(v − c)",
            "amounts outside: for v = 1 to k:   for each coin c ≤ v:  ways(v) += ways(v − c)",
            "",
            "coins 1, 2, 5 and an amount of 100",
            "  combinations                541",
            "  ordered sequences           91197869007632925819218",
            "",
            "both loops: 295 reads. The cost is identical; the question is not.",
        ],
        "key_label": "Two nestings of the same two loops, and the questions they answer",
        "concepts_intro": (
            "The hard idea is that the loop nesting is the specification here, not an "
            "implementation choice: it is what fixes whether an ordering counts as a second "
            "way of paying."
        ),
        "concepts": [
            ("Counting replaces the minimum with a sum, and the base case with a one",
             "The optimising recurrences on this course take the best of several options. A "
             "counting recurrence adds them: the number of ways to make `v` is the sum, over "
             "the options, of the number of ways to make what is left. The empty amount has "
             "exactly one way of being made &mdash; take nothing &mdash; so the base case is "
             "1 rather than 0, and getting that wrong makes every count zero."),
            ("Coin types outside counts each multiset once",
             "Running the coin loop outermost means every combination is assembled in one "
             "fixed order: all the ones, then all the twos, then all the fives. A multiset has "
             "exactly one such assembly, so it is counted exactly once, and the answer for 100 "
             "from 1, 2 and 5 is 541."),
            ("Amounts outside counts every ordering separately",
             "Running the amount loop outermost lets any coin be the last one added at any "
             "step, so `1 then 2` and `2 then 1` are two different histories and both are "
             "counted. That is a count of ordered sequences, and for 100 from the same three "
             "coins it is a twenty-three-digit number. Readers write this loop while meaning "
             "the other one, which is why both are on the panel."),
        ],
        "read_title": "Two nestings, two questions, and the arithmetic that has to be exact",
        "read_intro": "The counting recurrences, why the loop order decides the question, what the objects look like at small amounts, and why the numbers are BigInt.",
        "body": [
            ("def", ("Combinations and ordered sequences",
                     "A <strong>combination</strong> is a multiset of coins adding to the "
                     "amount: how many of each denomination, with no notion of order. An "
                     "<strong>ordered sequence</strong> is a list of coins adding to the "
                     "amount, where two lists differing only in order are different. Every "
                     "combination corresponds to one or more ordered sequences, and the two "
                     "counts are never equal once more than one denomination is used.")),
            ("thm", ("The two counting recurrences",
                     "Let `C(i, v)` be the number of combinations of the first `i` coin types "
                     "adding to `v`, with `C(i, 0) = 1` and `C(0, v) = 0` for `v &gt; 0`. Then "
                     "`C(i, v) = C(i−1, v) + C(i, v − c(i))`, the second term omitted when "
                     "`c(i) &gt; v`. Let `S(v)` be the number of ordered sequences adding to "
                     "`v`, with `S(0) = 1`. Then `S(v)` is the sum of `S(v − c)` over all "
                     "coins `c ≤ v`.")),
            ("proof", ("For combinations, split on how many copies of coin type `i` are used. "
                       "If none, the combination uses the first `i−1` types and there are "
                       "`C(i−1, v)` of those. If at least one, remove exactly one copy and "
                       "what remains is a combination of the first `i` types adding to "
                       "`v − c(i)`, and this correspondence is a bijection. The two cases are "
                       "disjoint and exhaustive, so the counts add.",
                       "For sequences, split on the last coin. Each sequence adding to `v` has "
                       "a final coin `c`, and deleting it leaves a sequence adding to "
                       "`v − c`; conversely appending `c` to such a sequence gives one adding "
                       "to `v`. That is a bijection for each `c`, the cases are disjoint "
                       "because the final coin differs, and summing over `c` gives `S(v)`. "
                       "The single-row loop with the amounts outermost is exactly this "
                       "recurrence, and the one with the coins outermost is exactly the "
                       "other.")),
            ("example", ("Five from 1, 2 and 5, with the objects listed",
                         "Four combinations: `5`, `2 + 2 + 1`, `2 + 1 + 1 + 1`, "
                         "`1 + 1 + 1 + 1 + 1`. Nine ordered sequences: the five ones; `1 1 1 2` "
                         "and its three other arrangements; `1 2 2`, `2 1 2` and `2 2 1`; and "
                         "`5`. Four and nine, and the lab lists both at this size so the "
                         "difference is an object rather than a number.")),
            ("p", "Notice which objects multiplied. The combination `2 + 2 + 1` has three "
                  "arrangements and the combination `2 + 1 + 1 + 1` has four, while `5` and "
                  "the five ones have one each: `1 + 4 + 3 + 1 = 9`. The ratio between the two "
                  "counts is not a constant and is not a factorial &mdash; it depends on how "
                  "many copies of each denomination each combination uses."),
            ("h3", "The cost is the same; the question is not"),
            ("p", "On the lab's main instance &mdash; 1, 2 and 5 at an amount of 100 &mdash; "
                  "both nestings read the table 295 times. Identical work, identical table, "
                  "identical arithmetic per step. The only difference is which loop is "
                  "outside, and the two answers differ by twenty orders of magnitude. There is "
                  "no performance argument for either one and there is no way to tell them "
                  "apart by watching them run."),
            ("p", "This is the most direct version of a claim this course keeps making. A "
                  "measurement of what an algorithm costs tells you nothing about what it "
                  "computes, and here the two are completely decoupled: same reads, same "
                  "cells, different question. The only defence is a second route, and the "
                  "panel provides one &mdash; a memo-free recursion for each count, which at "
                  "small amounts confirms both, and the objects themselves listed where they "
                  "fit."),
            ("h3", "Why these numbers are not held as doubles"),
            ("p", "`91 197 869 007 632 925 819 218` has twenty-three digits, and the largest "
                  "integer a double holds exactly is 9 007 199 254 740 992, which has sixteen. "
                  "A page computing this count in floating point would print a number that is "
                  "merely close &mdash; the leading digits right, the tail invented &mdash; "
                  "and would look exactly like a page that had computed it. Every count of "
                  "ways in this kit is an arbitrary-precision integer for that reason, and "
                  "none is ever converted."),
            ("p", "One consequence for the cost model, and it is the divergence this page "
                  "closes on. The table makes 295 reads, and each read is followed by an "
                  "addition; but those additions are on numbers of up to twenty-three digits, "
                  "not on machine words. The bound `Θ(nk)` counts arithmetic operations and "
                  "treats each as constant, which is exactly what stops being true here. "
                  "Measured: 295 reads. Proved: `Θ(nk)` operations. What neither of them says "
                  "is how long an addition takes when the numbers are as long as the answer, "
                  "and on this instance it is the addition that dominates."),
        ],
        "lab": ("dpkit", {
            "mode": "coins",
            "preset": "big",
            "panel_title": "Set the coins and the amount, and read both counts",
            "panel_intro": "Both nestings are computed on every redraw and both are checked "
                           "against a recursion with no table, at the amounts where that is "
                           "affordable. Drop the amount to five and the objects themselves are "
                           "listed, which is the only way the difference stops being two "
                           "numbers.",
        }),
        "steps_title": "Writing a counting recurrence and knowing what it counts",
        "steps_intro": "Three of these four steps are about deciding what the question is before deciding how to answer it.",
        "steps": [
            ("Say whether order matters, in the problem rather than in the code",
             "A shopkeeper handing over change wants combinations; a process that emits coins "
             "one at a time and cares about the history wants sequences. The two loops are "
             "both correct and they answer those two different questions, so the question has "
             "to be settled first."),
            ("Set the empty case to one, not zero",
             "There is exactly one way to make nothing. A counting table initialised entirely "
             "to zero stays entirely zero, which at least fails loudly; a table whose base is "
             "zero only at the empty amount fails quietly and undercounts."),
            ("Put the coin loop outside when you want each multiset once",
             "That nesting fixes an assembly order, and one fixed assembly order per multiset "
             "is what makes the count a count of multisets. The inner loop then runs upward, "
             "so that a coin may be reused &mdash; which is the same forward sweep that made "
             "the one-row knapsack unbounded, doing the same job for the same reason."),
            ("Hold the counts as exact integers and say so",
             "These numbers pass what a double holds long before they stop being interesting. "
             "An exact integer type costs nothing at this size and is the difference between "
             "a printed answer and a printed approximation that looks like an answer."),
        ],
        "worked": {
            "title": "The table for an amount of five, both ways",
            "intro": [
                "Three coin types, amounts zero to five. The first block adds one coin type per "
                "row, which counts combinations; the second is a single row swept once per "
                "amount, which counts ordered sequences.",
            ],
            "lines": [
                "amount              0   1   2   3   4   5",
                "",
                "coin types outside",
                "  start             1   0   0   0   0   0",
                "  after coin 1      1   1   1   1   1   1",
                "  after coin 2      1   1   2   2   3   3",
                "  after coin 5      1   1   2   2   3   4      <- 4 combinations",
                "",
                "amounts outside",
                "  one row           1   1   2   3   5   9      <- 9 ordered sequences",
                "",
                "the four combinations                the nine sequences",
                "  5                                    5",
                "  2 + 2 + 1                            2 2 1   2 1 2   1 2 2",
                "  2 + 1 + 1 + 1                        2 1 1 1   1 2 1 1",
                "                                       1 1 2 1   1 1 1 2",
                "  1 + 1 + 1 + 1 + 1                    1 1 1 1 1",
                "",
                "at an amount of 100 the same two loops give",
                "  combinations                 541",
                "  ordered sequences            91197869007632925819218",
                "and both make 295 reads",
            ],
            "after": [
                "The row for ordered sequences begins 1, 1, 2, 3, 5 and a reader who has met "
                "the Fibonacci numbers will recognise it: with coins 1 and 2 alone that is "
                "exactly what counting ordered sequences gives, and the 5 coin first shows up "
                "at amount 5, where it turns the expected 8 into 9. That recognition is worth "
                "having, because it makes the sequence count feel like the natural one, and it "
                "is usually not the one wanted.",
                "The combination block is the one to read slowly. After the first row every "
                "amount has exactly one combination, made of ones. Adding the 2 coin gives the "
                "row 1 1 2 2 3 3: the entry at 4 is 3 because a four is four ones, two and two "
                "ones, or two twos, and the entry was reached by adding the count from two "
                "columns left in the same row, which is the forward sweep allowing reuse.",
                "For a faded rehearsal, change the coins to 3 and 7 and keep the amount at 20 "
                "before running it. The supplied first move: 20 is not a multiple of 3, and "
                "subtracting one 7 leaves 13, which is not either, so at least two sevens are "
                "needed. Work out how many combinations there are, predict how many ordered "
                "sequences, and check both &mdash; the panel lists the combinations, and the "
                "sequence count is the one you have to reason about.",
            ],
        },
        "quiz_title": "Loop order, base cases, and exactness",
        "quiz": [
            {"q": "Both nestings read the table 295 times on the lab's instance. What does the equal cost tell you?",
             "a": ["That the two are the same algorithm written differently",
                   "That either may be used, since they agree on the answer",
                   "Nothing about what either computes: one counts 541 combinations and the other counts ordered sequences",
                   "That the difference between them is a constant factor"],
             "c": 2,
             "why": "Cost and meaning are decoupled here as completely as they can be: same "
                    "reads, same cells, same arithmetic per step, and answers twenty orders "
                    "of magnitude apart. That is the sharpest form of the course's standing "
                    "warning that watching an algorithm run tells you what it costs and not "
                    "what it computes."},
            {"q": "A counting table is initialised to zero everywhere, including the empty amount. What happens?",
             "a": ["Every entry stays zero, because every entry is a sum of earlier zeros",
                   "The counts come out one too small",
                   "Only the combination count is affected; the sequence count is unaffected",
                   "The table counts non-empty combinations, which is usually what was wanted"],
             "c": 0,
             "why": "There is exactly one way to make nothing, and that 1 is the only thing in "
                    "the table that is not derived from something else. Without it every sum "
                    "has zero as its only term. Both nestings depend on it equally, and this "
                    "failure is at least loud, which is more than can be said for most "
                    "mistakes on this course."},
            {"q": "Why is the ordered-sequence count held as an arbitrary-precision integer rather than a double?",
             "a": ["Because the additions would otherwise be too slow",
                   "Because it has twenty-three digits and a double holds sixteen exactly, so the printed tail would be invented",
                   "Because doubles cannot represent integers at all",
                   "Because the combination count is also too large for a double"],
             "c": 1,
             "why": "The largest integer a double holds exactly is 9 007 199 254 740 992. "
                    "Past that, a printed value has correct leading digits and an invented "
                    "tail, and looks exactly like a computed answer. Doubles represent small "
                    "integers perfectly well, and 541 is nowhere near the limit. Exact "
                    "arithmetic is slower here, not faster."},
            {"q": "Which loop nesting counts each multiset of coins exactly once?",
             "a": ["Amounts outermost, because each amount is visited once",
                   "Coin types outermost, because that fixes one assembly order per multiset",
                   "Either, provided the inner loop runs upward",
                   "Neither: multisets have to be enumerated rather than counted"],
             "c": 1,
             "why": "With the coin loop outside, every multiset is assembled in denomination "
                    "order and so is reached along exactly one path. With the amounts outside, "
                    "any coin may be last at any step and the orderings are counted "
                    "separately. The inner loop's direction controls reuse, which is a "
                    "different question, and multisets are certainly countable without being "
                    "listed &mdash; 541 of them here."},
        ],
        "mistakes": [
            ("Writing the sequence loop while meaning combinations",
             "It is the nesting that comes more naturally, because it visits the amounts in "
             "order and feels like filling a table left to right. It answers a different "
             "question and gives a wildly larger number, and nothing about running it reveals "
             "which one you wrote. Say which you want before you nest the loops."),
            ("Initialising the empty amount to zero",
             "One way to make nothing, not none. The mistake propagates to every entry and "
             "produces a table of zeros, which is at least visible &mdash; unlike most of the "
             "failures on this course."),
            ("Printing a count that a double cannot hold",
             "Twenty-three digits against sixteen. The output looks like an answer, is wrong "
             "in its last seven digits, and no check that compares it with another double "
             "will notice. The counts here are exact integers throughout and are never "
             "converted."),
        ],
        "standard": ("Finish when you can pick the loop nesting from the question rather than from habit.",
                     "You should be able to write both counting recurrences and prove each by "
                     "a bijection, explain why one counts multisets and the other counts "
                     "orderings, set the empty case correctly, and say at what size a "
                     "floating-point count stops being a count."),
        "note": ("The tables so far have been rectangles indexed by numbers. The next three "
                 "are not: the first is indexed by the vertices of a tree, the second by the "
                 "positions of a game, and the last by subsets of a set."),
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "dynamic-programming-on-a-tree",
        "title": "Dynamic Programming on a Tree",
        "module": "Tables that are not grids",
        "one_line": "Compute two numbers per vertex in one postorder pass, and check the chosen set against every subset and against the edge list.",
        "summary": (
            "There is no grid here. The table has one entry per vertex, and the entry is a "
            "pair: the best total in that vertex's subtree with the vertex taken, and the best "
            "without it. One postorder pass fills both, because a vertex's children are "
            "finished before it is. The set that comes back is then checked to be independent "
            "&mdash; against the edge list, not against the structure the pass walked &mdash; "
            "and re-weighed."
        ),
        "key": [
            "with(v)    = weight(v) + sum over children u of without(u)",
            "without(v) = sum over children u of max( with(u), without(u) )",
            "answer     = max( with(root), without(root) )",
            "",
            "a spine 1-2-3-4 with legs at 2, 3 and 4, weights 1 6 6 6 1 1 1",
            "  one pass      13     7 vertices visited, 12 reads",
            "  every subset  13     128 subsets examined",
        ],
        "key_label": "Two numbers per vertex, and one pass that fills both",
        "concepts_intro": (
            "The hard idea is that the fill order is the tree's own postorder, so it is forced "
            "by the structure rather than chosen &mdash; and the structure is what the "
            "argument depends on."
        ),
        "concepts": [
            ("The state is a vertex and a yes-or-no, so the table is a pair per vertex",
             "For each vertex, the best total obtainable within its subtree if that vertex is "
             "in the chosen set, and the best if it is not. Taking a vertex forbids all its "
             "children, so `with(v)` sums the children's `without`. Declining it frees each "
             "child to do whichever is better for itself, so `without(v)` sums the children's "
             "maxima. Two numbers, one recurrence each."),
            ("Postorder is the fill order, and the tree supplies it",
             "Every read is from a child, and postorder finishes every child before its "
             "parent, so no read lands on an unfilled entry. There is no ordering decision to "
             "get wrong here &mdash; which is worth noticing precisely because the matrix "
             "chain had one and got it wrong. The tree's shape is the order."),
            ("It is a fact about trees, and the parser enforces that",
             "The argument uses that a child's subtree interacts with the rest of the graph "
             "only through its parent. In a graph with a cycle that is false, the subtrees "
             "overlap, and the same pass would still produce a number. So the lab refuses an "
             "edge list that is not a tree &mdash; a cycle, a self-loop, a forest &mdash; "
             "rather than answering about a graph its recurrence does not describe."),
        ],
        "read_title": "Two numbers per vertex, one pass, and every subset beside it",
        "read_intro": "The problem, the pair recurrence and its proof, why the order is free here, and the two checks on what comes back.",
        "body": [
            ("def", ("Independent set, and its weighted version",
                     "A set of vertices is <strong>independent</strong> if no edge joins two "
                     "of them. Given a weight on each vertex, the <strong>maximum weight "
                     "independent set</strong> problem asks for an independent set of largest "
                     "total weight. On a general graph this is NP-hard; on a tree it is one "
                     "pass, and this lesson is about why the difference is the tree and not "
                     "the cleverness.")),
            ("thm", ("The pair recurrence on a tree",
                     "Root the tree anywhere. For a vertex `v` with children `u`, let "
                     "`with(v)` be the largest total over independent sets in `v`'s subtree "
                     "containing `v`, and `without(v)` the largest over those not containing "
                     "it. Then `with(v) = weight(v) + sum of without(u)` and "
                     "`without(v) = sum of max(with(u), without(u))`, and the answer is "
                     "`max(with(root), without(root))`.")),
            ("proof", ("Take an independent set `S` in `v`'s subtree that is largest among "
                       "those containing `v`. No child of `v` is in `S`, since each is "
                       "adjacent to `v`. For each child `u`, the part of `S` inside `u`'s "
                       "subtree is independent and avoids `u`, and it must be largest among "
                       "such sets &mdash; otherwise substituting a heavier one gives a heavier "
                       "`S`, and the substitution is legal because the subtrees are disjoint "
                       "and share no edge. Summing gives the first equation.",
                       "If `S` is largest among sets avoiding `v`, each child is free, and the "
                       "part of `S` in `u`'s subtree must be a heaviest independent set there "
                       "with no constraint, which is `max(with(u), without(u))`. Again the "
                       "substitution is legal because distinct subtrees share no vertex and no "
                       "edge. That disjointness is exactly what a tree provides and a cycle "
                       "destroys, and it is where the proof would fail on a general graph.")),
            ("p", "The proof is worth reading twice for that last sentence. Optimal "
                  "substructure here is not a property of the objective; it is a property of "
                  "the input's shape. The same objective on a graph with one extra edge has no "
                  "such decomposition, and no amount of care with the recurrence recovers it."),
            ("example", ("A spine with legs, and the two heavy vertices that cannot both go",
                         "The lab loads a tree on seven vertices: a path `1-2-3-4` with extra "
                         "leaves hanging off 2, 3 and 4, and weights `1 6 6 6 1 1 1`. Vertices "
                         "2, 3 and 4 are the heavy ones and they form a path, so at most two "
                         "of them can be chosen. The pass returns 13, choosing vertices 2, 4 "
                         "and 6 &mdash; two of the three heavy ones and one leaf &mdash; and "
                         "every one of the 128 subsets confirms 13.")),
            ("h3", "The two checks, and why both"),
            ("p", "The chosen set is tested for independence against the edge list as it was "
                  "typed, not against the adjacency structure the pass walked. That matters: a "
                  "bug in building the adjacency map would make the pass and a structure-based "
                  "check wrong in the same way, and the two would agree. Reading the raw edges "
                  "is a route that shares nothing with the pass."),
            ("p", "Then the set is re-weighed, and its total compared with the number the pass "
                  "reported. Independence alone is not enough &mdash; the empty set is "
                  "independent &mdash; and a matching total alone is not enough either, since "
                  "a heavier but illegal set would also fail to be an answer. Both checks, "
                  "separately, and the panel prints both verdicts."),
            ("h3", "Where the greedy instinct goes, and what the counts say"),
            ("p", "The instinct readers arrive with is to alternate: take every second level. "
                  "On a path that is right, and the lab ships a path where it gives 15, the "
                  "correct answer. On this tree, alternating from the root takes vertices 1, "
                  "3, 5 and 7 for a total of 9, against the optimum's 13 &mdash; and "
                  "alternating the other way happens to give 13. A rule whose answer depends "
                  "on which parity you start from is not a rule until that choice is made, and "
                  "making it correctly is the problem again."),
            ("p", "The measured counts are 7 vertex visits and 12 reads for the pass, against "
                  "128 subsets for the check, on a tree of seven vertices. The proved bounds "
                  "are `Θ(n)` and `Θ(2ⁿ n)`. Here the measurement and the bound agree in order "
                  "already at `n = 7`, which is worth stating plainly because on three other "
                  "pages of this course they do not &mdash; the coin table loses to a plain "
                  "recursion at an amount of six, the chain table loses to enumeration at four "
                  "matrices, and the last lesson of the course loses by a factor of forty."),
        ],
        "lab": ("dpkit", {
            "mode": "tree",
            "preset": "caterpillar",
            "panel_title": "Type a tree as an edge list, and a weight per vertex",
            "panel_intro": "Edges are written `1-2`, separated by commas, and anything that is "
                           "not a tree is refused rather than answered about. The panel shows "
                           "both numbers for every vertex, checks the chosen set against the "
                           "edges you typed, and re-weighs it.",
        }),
        "steps_title": "Running a dynamic program over a structure rather than a grid",
        "steps_intro": "The table is still a table; what changes is that the index set and the fill order come from the input.",
        "steps": [
            ("Choose the state so that a vertex's subtree is summarised by a few numbers",
             "Two here, because the only thing the parent needs to know about a child's "
             "subtree is what it is worth with the child taken and without. If the parent "
             "would need to know more, the state is bigger and the pass is more expensive; if "
             "it would need to know the whole subtree, there is no dynamic program."),
            ("Root the tree anywhere, and say that it does not matter",
             "The answer is a property of the tree, not of the root, so any vertex will do. "
             "That is worth checking on a small example by re-rooting and re-running, because "
             "if it does matter, the state is wrong."),
            ("Take the fill order from the traversal, not from a loop",
             "Postorder guarantees every child is finished before its parent, which is exactly "
             "the condition the reads need. This is the one lesson on the course where the "
             "order cannot be got wrong, and the reason is that the structure supplies it."),
            ("Check independence against the raw input",
             "Read the edge list as typed rather than the structure the algorithm built. A "
             "check that shares a data structure with the thing it checks will agree with it "
             "about the bugs they have in common."),
            ("Re-weigh the set as well as validating it",
             "The empty set is independent and worth nothing. A set that is independent and "
             "adds to the reported total is a checked answer; either check alone is not."),
        ],
        "worked": {
            "title": "Seven vertices, two numbers each, one pass",
            "intro": [
                "The tree is the path 1-2-3-4 with a leaf 5 on vertex 2, a leaf 6 on vertex 3 "
                "and a leaf 7 on vertex 4. Weights are 1, 6, 6, 6, 1, 1, 1. Rooted at vertex "
                "1, the postorder is 7, 4, 6, 3, 5, 2, 1.",
            ],
            "lines": [
                "vertex   weight   children        with     without",
                "",
                "   7        1      -                 1           0",
                "   4        6      7                 6           1",
                "   6        1      -                 1           0",
                "   3        6      4, 6              7           7",
                "   5        1      -                 1           0",
                "   2        6      3, 5             13           8",
                "   1        1      2                 9          13",
                "",
                "answer = max( with(1), without(1) ) = max(9, 13) = 13",
                "",
                "the set the pass chooses:   2, 4, 6",
                "  independent against the typed edges?   yes",
                "  re-weighed:   6 + 6 + 1 = 13,  which matches",
                "",
                "every one of the 128 subsets agrees: 13",
                "alternating levels from the root gives 1 + 6 + 1 + 1 = 9",
            ],
            "after": [
                "Vertex 3 is the interesting line: `with` and `without` are both 7. Taking it "
                "costs its two children's freedom and gains its own 6; declining it lets "
                "vertex 4 take its 6 and vertex 6 take its 1. The tie means the pass could "
                "have gone either way at that vertex, and the answer above it is unaffected, "
                "which is a reminder that an optimum can be non-unique in shape while being "
                "unique in value.",
                "Vertex 1's line shows where the answer comes from: it has weight 1 and one "
                "child, so taking it is worth `1 + 8 = 9` and declining it is worth 13. The "
                "root is declined, and a reader who expected the root to matter is reading the "
                "weight rather than the structure. Switch the lab to the star and the same "
                "thing happens for the opposite reason: the centre is worth 3 and the four "
                "leaves together are worth 12.",
                "For a faded rehearsal, keep the tree and set every weight to 1 before running "
                "it. The supplied first move: with equal weights the problem becomes the "
                "largest independent set by count, and the three leaves 5, 6 and 7 are "
                "pairwise non-adjacent, so the answer is at least 3. Work out whether it is "
                "more, then check &mdash; and note that the pass returns a set, not just a "
                "count, so you can see which one it picked.",
            ],
        },
        "quiz_title": "Pairs, passes, and what the tree is doing in the proof",
        "quiz": [
            {"q": "Why does the recurrence need the input to be a tree rather than any graph?",
             "a": ["Because a graph with a cycle has no independent sets",
                   "Because the proof substitutes an improved solution into one subtree, which is only legal when the subtrees are disjoint and share no edge",
                   "Because postorder is undefined on a graph with a cycle",
                   "Because the weights would no longer be well defined"],
             "c": 1,
             "why": "The substitution argument is where the tree is used: distinct subtrees "
                    "share no vertex and no edge, so improving one cannot violate "
                    "independence elsewhere. Cycles do have independent sets, a traversal "
                    "order can be defined on any graph, and the weights are unaffected. The "
                    "same pass on a cyclic graph would return a number, which is why the "
                    "parser refuses one."},
            {"q": "The chosen set is checked for independence against the edge list as typed rather than against the adjacency structure the pass walked. Why?",
             "a": ["Because the adjacency structure is discarded after the pass",
                   "Because the edge list is smaller and the check is therefore faster",
                   "Because a check sharing a data structure with the algorithm agrees with it about the bugs they have in common",
                   "Because the edge list is the only place the weights are stored"],
             "c": 2,
             "why": "Independence is a property of the input the reader typed. A check reading "
                    "the same derived structure the pass walked would pass whenever that "
                    "structure was built wrong. Speed is not the issue at these sizes, the "
                    "structure survives the pass, and the weights are a separate input."},
            {"q": "On the lab's tree, alternating levels from the root gives 9 and the optimum is 13. What does that show about the alternating rule?",
             "a": ["That it is never correct on a tree",
                   "That it is not a rule until the parity is chosen, and choosing correctly is the original problem",
                   "That it is correct only on trees of even depth",
                   "That the optimum must always avoid the root"],
             "c": 1,
             "why": "Alternating the other way happens to give 13 on this tree, and on the "
                    "lab's path both parities are available and one of them is optimal. A "
                    "procedure whose answer depends on an unspecified choice is not yet a "
                    "procedure. It is not never correct, depth parity is not the issue, and "
                    "the star's optimum avoids the centre while the root is taken in plenty of "
                    "other trees."},
        ],
        "mistakes": [
            ("Keeping one number per vertex instead of two",
             "The parent needs to know what the child's subtree is worth under two different "
             "constraints, and a single best-for-this-subtree number cannot answer both. A "
             "one-number version runs, returns something plausible, and is wrong on any tree "
             "where the constraint bites."),
            ("Carrying the result to a graph that is not a tree",
             "The pass would run. It would produce a number. The number would not be the "
             "maximum weight independent set, because the substitution the proof performs is "
             "illegal once two subtrees share an edge. Maximum weight independent set on a "
             "general graph is NP-hard, and Intractability and Approximation is where that "
             "line is drawn."),
            ("Checking the answer's weight without checking its legality",
             "A set whose weight matches the reported number may still contain two adjacent "
             "vertices if the reconstruction went wrong, and a set that is independent may be "
             "worth less than reported. The two verdicts are printed separately because they "
             "fail separately."),
        ],
        "standard": ("Finish when you can design a pass over a structure and say where the structure is used in the proof.",
                     "You should be able to choose a state that summarises a subtree in a few "
                     "numbers, write the pair recurrence, point to the line of the proof that "
                     "needs disjointness, and check a returned set against the raw input rather "
                     "than against the algorithm's own scaffolding."),
        "note": ("The next table is indexed by the positions of a game rather than by anything "
                 "in a data structure, and its entries are not numbers at all. It is also the "
                 "one place on this course where the pattern a reader is asked to find is a "
                 "claim the table cannot establish."),
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "won-and-lost-positions",
        "title": "Won and Lost Positions",
        "module": "Tables that are not grids",
        "one_line": "Label every position of a subtraction game from the definition alone, find the period in the labels, and say what the table can and cannot prove about it.",
        "summary": (
            "A position loses exactly when every move from it leads to a winning position. "
            "That definition is a recurrence whose entries are two symbols rather than "
            "numbers, and evaluating it upward from zero labels the whole game. With moves 1, "
            "3 and 4 the losing positions are 0, 2, 7, 9, 14, 16 &mdash; a period of seven "
            "that is not the multiples of anything, and that the table exhibits over nineteen "
            "positions without proving."
        ),
        "key": [
            "position p is LOSING   when every move from p reaches a winning position",
            "position p is WINNING  when some move from p reaches a losing position",
            "a position with no moves is losing",
            "",
            "take 1, 3 or 4, positions 0 to 18",
            "  L W L W W W W L W L W W W W L W L W W",
            "  losing: 0, 2, 7, 9, 14, 16        the pattern repeats every 7",
        ],
        "key_label": "One definition, evaluated upward, and the period it exhibits",
        "concepts_intro": (
            "The hard idea is the last one: the period is measured over the positions on "
            "screen, and the proof that the labels are eventually periodic is a separate and "
            "quite different argument."
        ),
        "concepts": [
            ("The table's entries are labels, and the recurrence is a quantifier",
             "There is no arithmetic here. A position is losing when <em>every</em> move from "
             "it reaches a winning position, and winning when <em>some</em> move reaches a "
             "losing one. Those are the two quantifiers, and they are duals, so one definition "
             "suffices. The base case falls out of it: a position with no legal move has "
             "vacuously every move reaching a win, so it loses."),
            ("Evaluating upward from zero is the fill order, and it is forced",
             "Every move strictly decreases the position, so the label of `p` depends only on "
             "labels below `p`, and counting upward from zero is the order that has them all. "
             "The lab checks this against a memo-free recursion that labels each position from "
             "scratch, so the table is compared with a second computation rather than "
             "displayed and believed."),
            ("A period seen over nineteen positions is measured, not proved",
             "The panel reports the smallest `k` for which the labels agree at every pair of "
             "positions `k` apart, <em>within the range shown</em>. That is a statement about "
             "nineteen positions. The general fact &mdash; that such a game's labels are "
             "eventually periodic &mdash; comes from a pigeonhole argument over windows of "
             "labels, and it bounds the period rather than giving its value."),
        ],
        "read_title": "Two labels, one quantifier, and a period that has to be argued for",
        "read_intro": "The definition, the labelling, the second computation that checks it, and the exact status of the pattern.",
        "body": [
            ("def", ("A subtraction game, and its two kinds of position",
                     "Two players alternate. From a position `p` a player may move to `p − m` "
                     "for any `m` in a fixed subtraction set with `m ≤ p`. A player with no "
                     "legal move loses. A position is <strong>losing</strong> if the player "
                     "about to move from it loses under perfect play, and "
                     "<strong>winning</strong> otherwise.")),
            ("thm", ("The labelling recurrence",
                     "A position `p` is losing if and only if every move from `p` leads to a "
                     "winning position; equivalently, `p` is winning if and only if some move "
                     "from `p` leads to a losing position. A position with no legal moves is "
                     "losing.")),
            ("proof", ("By strong induction on `p`. Suppose every position below `p` is "
                       "correctly labelled. If some move from `p` reaches a losing position, "
                       "the player to move takes it and hands the opponent a position from "
                       "which, by hypothesis, the opponent loses; so `p` is winning.",
                       "If every move from `p` reaches a winning position, then whatever the "
                       "player does, the opponent is handed a position from which the "
                       "opponent, by hypothesis, wins; so `p` is losing. The two cases are "
                       "exhaustive, and the vacuous case &mdash; no moves at all &mdash; falls "
                       "under the second, which is why a terminal position loses.")),
            ("p", "Notice that this table has no objective to optimise. Every other page on "
                  "this course computes a best value; this one computes a truth value, and "
                  "the recurrence is a pair of quantifiers rather than a minimum or a sum. "
                  "That is worth seeing once, because it separates the technique &mdash; a "
                  "table, an order, a recurrence &mdash; from the arithmetic that usually "
                  "accompanies it."),
            ("example", ("Take one, three or four, from zero to eighteen",
                         "The labels come out `L W L W W W W L W L W W W W L W L W W`. The "
                         "losing positions are 0, 2, 7, 9, 14 and 16. Position 2 loses because "
                         "its only legal move is to 1, which wins; position 7 loses because "
                         "its moves reach 6, 4 and 3, all winning. The panel reports the "
                         "smallest period over the positions shown as 7, and a memo-free "
                         "minimax recursion agrees with the table at every position.")),
            ("p", "That period is not the multiples of anything. Losing positions are those "
                  "congruent to 0 or 2 modulo 7, which is two residues rather than one. Change "
                  "the subtraction set to 1, 2 and 3 and the losing positions are exactly the "
                  "multiples of 4, and that pattern has an argument a reader can give in one "
                  "line. Change it to 1 and 2 and the answer is the multiples of 3. Change it "
                  "to 2 and 5 and positions 0 and 1 both lose, so the pattern does not even "
                  "begin with a single loss."),
            ("h3", "What is measured, and what can be proved"),
            ("p", "The panel's period is computed by testing, for each `k` in turn, whether "
                  "the labels agree at every pair of positions `k` apart among the positions "
                  "labelled. With nineteen positions on screen and a reported period of 7, "
                  "that is two full repetitions and a bit. It is a measurement, and if the "
                  "pattern broke at position 40 the panel would say nothing about it."),
            ("thm", ("Subtraction games are eventually periodic",
                     "Let `M` be the largest element of the subtraction set. The label of a "
                     "position is determined by the labels of the `M` positions below it. "
                     "There are at most `2^M` distinct windows of `M` consecutive labels, so "
                     "some window repeats, and from that point the sequence of labels repeats "
                     "with a period at most `2^M`.")),
            ("proof", ("Consider the sequence of windows `w(p)` consisting of the labels of "
                       "positions `p−M` through `p−1`. The recurrence determines the label of "
                       "`p` from `w(p)` alone, and therefore determines `w(p+1)` from `w(p)`. "
                       "So the sequence of windows is generated by a function from a finite "
                       "set to itself.",
                       "A sequence of elements of a set of size at most `2^M` generated by "
                       "iterating a function must repeat a value within the first `2^M + 1` "
                       "steps, and once a window repeats, everything after it repeats too. "
                       "Hence the labels are eventually periodic with period at most `2^M`. "
                       "For the subtraction set 1, 3, 4 that bound is 16, and the measured "
                       "period is 7 &mdash; the bound is true, loose, and says nothing about "
                       "which value below it occurs.")),
            ("p", "Those two results are exactly the pairing this Subject insists on. The "
                  "table measures a period of 7 over nineteen positions. The pigeonhole "
                  "argument proves eventual periodicity with period at most 16, for every "
                  "subtraction set. Neither implies the other: the measurement does not "
                  "establish that 7 continues, and the proof does not say the period is 7 or "
                  "that it starts at position zero rather than later. Raising the range on the "
                  "lab extends the measurement and never turns it into the theorem."),
            ("p", "The cost is the least interesting thing on the page and is worth one "
                  "sentence: nineteen positions are labelled with nineteen calls, each looking "
                  "at up to three predecessors, so labelling `n` positions is `Θ(n)` for a "
                  "fixed subtraction set. The memo-free recursion that checks it is "
                  "exponential and is capped at position 24 for that reason."),
        ],
        "lab": ("dpkit", {
            "mode": "game",
            "preset": "subtract134",
            "panel_title": "Choose what may be taken, and how far to label",
            "panel_intro": "The subtraction set is typed as numbers; the labels are computed "
                           "from the definition alone and checked against a memo-free minimax "
                           "recursion. The reported period is the smallest one consistent with "
                           "the positions on screen, which is a measurement and is not the "
                           "same claim as periodicity.",
        }),
        "steps_title": "Labelling a game, and reporting a pattern honestly",
        "steps_intro": "The first three steps are mechanical; the fourth is the one this page exists for.",
        "steps": [
            ("Write the definition as a quantifier over moves",
             "Losing when every move wins, winning when some move loses. Resist turning it "
             "into a formula about the position's value: the two quantifiers are the "
             "recurrence, and games where the pattern is not arithmetic are exactly where a "
             "formula would be invented."),
            ("Label upward, because every move goes down",
             "The fill order is forced by the fact that a move strictly decreases the "
             "position. There is nothing to choose and nothing to get wrong, which makes this "
             "the cheapest table on the course to be confident about."),
            ("Check the labels against a second computation",
             "A memo-free minimax recursion at each position shares no state with the table. "
             "Run it at every position while the positions are small, and compare. The lab "
             "does this on every redraw up to its cap."),
            ("Report a measured period as a measurement",
             "Say over how many positions it was observed. If you want the claim that it "
             "continues, the argument is the pigeonhole one over windows of labels, and it "
             "gives eventual periodicity with a bound rather than the value you measured."),
            ("Check the first few positions by hand before believing the pattern",
             "With moves 2 and 5, positions 0 and 1 both lose, so the pattern opens with two "
             "losses in a row and a reader who has assumed a single loss at zero will misread "
             "the whole table. The beginning is where measured patterns most often mislead."),
        ],
        "worked": {
            "title": "Take one, three or four: nineteen positions labelled",
            "intro": [
                "Each position is labelled from the definition using only the labels below it. "
                "A position is losing when every move from it reaches a winning position.",
            ],
            "lines": [
                "position   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18",
                "label      L  W  L  W  W  W  W  L  W  L  W  W  W  W  L  W  L  W  W",
                "",
                "why each of the first few is what it is",
                "",
                "  0    no legal move at all                          losing",
                "  1    move to 0, which loses                        winning",
                "  2    only move is to 1, which wins                 losing",
                "  3    move to 2, which loses                        winning",
                "  4    move to 0, which loses                        winning",
                "  5    move to 2, which loses                        winning",
                "  6    move to 2, which loses                        winning",
                "  7    moves reach 6, 4 and 3, all winning           losing",
                "",
                "losing positions:   0, 2, 7, 9, 14, 16",
                "differences:        2, 5, 2, 5, 2          -    period 7",
                "residues mod 7:     0, 2, 0, 2, 0, 2",
                "",
                "measured over 19 positions.  The pigeonhole argument proves",
                "eventual periodicity with period at most 2 to the 4, which is 16.",
            ],
            "after": [
                "The residues are the honest way to state what was seen: the losing positions "
                "are those congruent to 0 or 2 modulo 7, over the range labelled. Two residues, "
                "not one, which is why no multiple-of-something description fits and why the "
                "table had to be computed rather than guessed.",
                "Compare with the subtraction set 1, 2, 3, where the losing positions are "
                "0, 4, 8, 12, 16 and the argument is one line: from a multiple of four, "
                "whatever you take, your opponent takes the complement to four and hands back "
                "another multiple of four. That argument is a proof for every position, and "
                "nothing like it is available for 1, 3, 4 &mdash; the lab measures 7 and the "
                "general theorem bounds the period by 16.",
                "For a faded rehearsal, switch the subtraction set to 2 and 5 before running "
                "it. The supplied first move: from position 1 there is no legal move at all, "
                "so 1 loses, and so does 0. Predict the first six labels, then check &mdash; "
                "and note how much harder the pattern is to see when it does not begin the way "
                "you expect.",
            ],
        },
        "quiz_title": "Labels, orders, and the status of a pattern",
        "quiz": [
            {"q": "Why is a position with no legal move labelled losing rather than needing a separate base case?",
             "a": ["Because the table is initialised to losing everywhere",
                   "Because every move from it reaches a winning position, vacuously",
                   "Because the player who cannot move has taken the last item, and taking last wins",
                   "Because zero is even"],
             "c": 1,
             "why": "The definition says losing when every move reaches a win, and a position "
                    "with no moves satisfies that with nothing to check. The base case is "
                    "therefore not an extra rule. Under this convention the player who cannot "
                    "move loses, so taking last wins &mdash; which is a consequence, not the "
                    "reason &mdash; and parity has nothing to do with it."},
            {"q": "The panel reports a period of 7 over nineteen positions. What has been established?",
             "a": ["That the labels are periodic with period 7 for every position",
                   "That the labels agree at every pair of positions seven apart among those shown",
                   "That the period divides 7, since 7 is prime",
                   "That the losing positions are the multiples of 7"],
             "c": 1,
             "why": "It is a measurement over the range on screen, and extending the range "
                    "extends the measurement without changing its kind. The theorem available "
                    "is eventual periodicity with period at most `2^M`, which for this set is "
                    "16. The losing positions here are 0 and 2 modulo 7, two residues, so they "
                    "are certainly not the multiples of 7."},
            {"q": "With the subtraction set 2 and 5, positions 0 and 1 are both losing. Why does that matter for reading the table?",
             "a": ["It does not: the pattern is still periodic",
                   "Because a reader expecting the pattern to open with a single loss at zero will misalign every later repetition",
                   "Because two consecutive losses make the game unfair",
                   "Because it means the game has no winning strategy"],
             "c": 1,
             "why": "Position 1 has no legal move, since the smallest move is 2, so it loses "
                    "along with 0. The pattern opens with two losses and a reader who assumes "
                    "one will line the repetitions up wrong. The game is perfectly ordinary "
                    "otherwise, and one of the two players has a winning strategy from every "
                    "position, as the labelling shows."},
            {"q": "What does the pigeonhole argument over windows of labels prove?",
             "a": ["That the labels are eventually periodic, with period at most `2^M` where `M` is the largest move",
                   "That the period is exactly the largest move plus one",
                   "That the losing positions form an arithmetic progression",
                   "That the period observed on any finite range continues for ever"],
             "c": 0,
             "why": "The label of a position is determined by the window of the `M` labels "
                    "below it, there are at most `2^M` windows, and iterating a function on a "
                    "finite set must repeat. That gives eventual periodicity and a bound, "
                    "nothing sharper. The measured period here is 7 against a bound of 16, and "
                    "the losing positions are two residues rather than one progression."},
        ],
        "mistakes": [
            ("Turning the observed pattern into a formula",
             "The multiples of 4 for the set 1, 2, 3 have a one-line proof; the residues 0 and "
             "2 modulo 7 for the set 1, 3, 4 have only a table over nineteen positions and a "
             "theorem that bounds the period at 16. Writing the second as though it had the "
             "status of the first is the defect this page exists to prevent."),
            ("Reading the base case as a special rule",
             "It is the general rule applied to a position with nothing to quantify over. "
             "Treating it as an exception invites getting it backwards in a game where the "
             "player who cannot move wins instead, and there the same recurrence with the "
             "labels swapped is the correct one."),
            ("Extending the range and calling the pattern proved",
             "Nineteen positions, then forty, then a hundred. Each is a longer measurement and "
             "none is the theorem. The theorem comes from the finiteness of the window, and it "
             "is available without labelling a single position."),
        ],
        "standard": ("Finish when you can label a game from the definition and state the period's status precisely.",
                     "You should be able to write the two quantifiers, explain why a terminal "
                     "position falls out of them, check the labels against a second "
                     "computation, and separate a period measured over a range from the "
                     "eventual periodicity a pigeonhole argument proves."),
        "note": ("One table remains, and it is indexed by subsets. It is also the page where "
                 "the asymptotically better method loses by the widest margin on this course "
                 "&mdash; not by a little, and not on a contrived instance, but on the smallest "
                 "one the lab will accept."),
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "subsets-as-a-table-and-where-it-loses",
        "title": "Subsets as a Table, and Where the Table Loses",
        "module": "Tables that are not grids",
        "one_line": "Solve the travelling salesman exactly by indexing a table with subsets, then compare its work with trying every tour and find the size at which the table finally wins.",
        "summary": (
            "Held and Karp index a table by a subset of the cities and the city currently ended "
            "at, which turns a factorial search into an exponential one. On four cities that "
            "is 256 units of work against 6, so the table loses by a factor of more than forty "
            "on the instance in front of you. It does not overtake trying every tour until "
            "ten cities, and both numbers are printed as exact integers because the whole "
            "point is how they pull apart."
        ),
        "key": [
            "table entry: (subset S containing city 1, end city j)  ->  shortest path",
            "  covering exactly S and finishing at j",
            "",
            "work:  Held-Karp  n²2ⁿ        every ordering  (n−1)!",
            "  n = 4        256   against          6        the table loses",
            "  n = 6       2304   against        120        the table loses",
            "  n = 10   102 400   against    362 880        the table finally wins",
        ],
        "key_label": "Two exact counts, and the size at which they cross",
        "concepts_intro": (
            "The hard idea is the state: a subset is an index, and accepting that is what "
            "turns an ordering problem into a table problem."
        ),
        "concepts": [
            ("A subset is a perfectly good index",
             "The table has one entry per pair: a set of cities already visited, and which of "
             "them the route currently ends at. The entry is the length of the shortest route "
             "from the start that visits exactly that set and finishes there. Nothing about a "
             "table requires its index to be a number, and once the index may be a set the "
             "problem has `n2ⁿ` states rather than `(n−1)!` orderings."),
            ("The saving is that the order inside a set stops mattering",
             "Two routes visiting the same cities and ending at the same city are "
             "interchangeable for everything that follows, so only the shorter needs keeping. "
             "That is optimal substructure stated for this problem, and it is what collapses "
             "the factorial: the `(k−1)!` orders of a `k`-subset ending at a given city "
             "become one entry."),
            ("Exponential and factorial cross late, and before the crossing the table loses",
             "`n²2ⁿ` against `(n−1)!` is 256 against 6 at four cities, 2 304 against 120 at "
             "six, and 41 472 against 40 320 at nine, where the table is still behind. It "
             "first wins at ten, 102 400 against 362 880. The better asymptotic method is the "
             "worse method on every instance this lab will run."),
        ],
        "read_title": "Subsets as a table, and the crossing that comes late",
        "read_intro": "The problem, the recurrence over subsets, what the tour that comes back actually is, and the two exact counts that pull apart.",
        "body": [
            ("def", ("The travelling salesman problem, as this page states it",
                     "Given `n` cities and a distance from each to each, find a cyclic route "
                     "that starts at city 1, visits every city exactly once, and returns to "
                     "city 1, of least total length. The distances need not be symmetric and "
                     "nothing here assumes the triangle inequality &mdash; the lab ships a "
                     "matrix violating both.")),
            ("thm", ("The Held-Karp recurrence",
                     "For a subset `S` of the cities containing city 1 and a city `j` in `S` "
                     "other than 1, let `D(S, j)` be the length of the shortest path that "
                     "starts at city 1, visits exactly the cities of `S`, and ends at `j`. "
                     "Then `D({1, j}, j) = d(1, j)`, and for larger `S`, `D(S, j)` is the "
                     "minimum over cities `i` in `S` other than `1` and `j` of "
                     "`D(S − {j}, i) + d(i, j)`. The tour's length is the minimum over `j` of "
                     "`D(all, j) + d(j, 1)`.")),
            ("proof", ("A shortest path from city 1 covering `S` and ending at `j` arrives at "
                       "`j` from some city `i` in `S`. Deleting the final leg leaves a path "
                       "from 1 covering `S − {j}` and ending at `i`, and that path must be a "
                       "shortest such path: a shorter one could be extended by the same final "
                       "leg to beat the original. So the length is "
                       "`D(S − {j}, i) + d(i, j)` for that `i`, and minimising over `i` gives "
                       "the recurrence.",
                       "The substitution is legal because the final leg's cost depends only on "
                       "`i` and `j` and not on how `S − {j}` was traversed, which is exactly "
                       "the property that makes the order inside a subset irrelevant. Closing "
                       "the cycle at the end adds the return leg, and taking the minimum over "
                       "the last city gives the tour.")),
            ("p", "The fill order follows from the recurrence as usual: `D(S, j)` reads "
                  "entries for `S − {j}`, which is a strictly smaller set, so filling by "
                  "increasing subset size &mdash; or, equivalently here, by increasing numeric "
                  "value of the subset's bit pattern &mdash; has every read written. On the "
                  "lab's four-city instance the fill makes 12 reads."),
            ("h3", "What comes back, and the convention it follows"),
            ("p", "The tour is returned as an <em>open</em> list of `n` cities beginning at "
                  "city 1. The leg home is counted in the reported length and is not in the "
                  "list. On the lab's default matrix the tour is `1, 3, 4, 2` and the length "
                  "is 21; adding up the three legs written down gives 20, and the missing 1 is "
                  "the return from city 2 to city 1. Re-measuring the list as written is the "
                  "way to convince yourself there is an off-by-one in the table, and there is "
                  "not."),
            ("p", "So the check closes the cycle. The panel confirms that the list is a "
                  "permutation of the cities starting at city 1 and re-adds the `n` legs "
                  "&mdash; the `n − 1` written plus the return &mdash; from the distance "
                  "matrix. Both of those are separate from the table, and both are printed."),
            ("example", ("Four cities, and all six tours",
                         "The matrix is asymmetric: the distance from city 1 to city 2 is 2 "
                         "and from 2 to 1 is 1. The six tours are `1-2-3-4-1` at 22, "
                         "`1-2-4-3-1` at 33, `1-3-2-4-1` at 26, `1-3-4-2-1` at 21, "
                         "`1-4-2-3-1` at 34 and `1-4-3-2-1` at 30. Held-Karp returns 21 and "
                         "the tour `1, 3, 4, 2`, and the enumeration agrees on both.")),
            ("h3", "Where the table loses, and by how much"),
            ("p", "Held-Karp fills one entry per (subset, end city) pair, which is `n2ⁿ` "
                  "entries, and each entry minimises over up to `n` predecessors, so the work "
                  "is `n²2ⁿ`. Trying every ordering is `(n−1)!` tours. At four cities those "
                  "are 256 and 6. At five, 800 and 24. At six, 2 304 and 120. At nine, 41 472 "
                  "and 40 320 &mdash; still behind. At ten, 102 400 and 362 880, and from "
                  "there the gap widens for ever."),
            ("p", "This is the Subject's warning in its sharpest available form, and it is "
                  "worth being precise about what each number is. The two figures on the panel "
                  "are exact integers evaluated from `n`, not measurements of a running time "
                  "and not estimates: `n²2ⁿ` and `(n−1)!` are the two bounds, printed at the "
                  "`n` on screen. They are the proved statements, and they are what says the "
                  "table wins eventually. What the lab measures is separate: 12 reads for the "
                  "fill and 6 tours for the enumeration on this instance, and by that "
                  "measurement too the table is the slower method here."),
            ("p", "So a reader who chose Held-Karp for a four-city problem chose the "
                  "asymptotically better algorithm and did more work, and would keep doing "
                  "more work up to nine cities. Nothing is wrong with the analysis. What is "
                  "wrong is treating an asymptotic comparison as advice about an instance, and "
                  "this page is on the course because that mistake is invisible when both "
                  "methods finish instantly."),
            ("p", "Intractability and Approximation takes this further: `O(n²2ⁿ)` is still "
                  "exponential and this problem is NP-hard, so the table is a better "
                  "exponential rather than a way out of one. The six honest responses to a "
                  "problem with no fast algorithm are that course's subject, and an exact "
                  "algorithm that is merely less bad is the first of them."),
        ],
        "lab": ("dpkit", {
            "mode": "tsp",
            "preset": "four",
            "panel_title": "Type a distance matrix, and step through the subsets",
            "panel_intro": "Rows are separated by semicolons and the matrix need not be "
                           "symmetric. The two work figures are exact integers computed from "
                           "the number of cities; the tour that comes back is re-measured from "
                           "the matrix with the cycle closed, because the list itself omits "
                           "the leg home.",
        }),
        "steps_title": "Indexing a table by subsets, and deciding whether to",
        "steps_intro": "The technique is mechanical. The decision about whether it helps at your size is not.",
        "steps": [
            ("Ask what a partial solution needs to remember",
             "For a tour: which cities are used and where you are. Not the order they were "
             "used in, because nothing in the future depends on it. That observation is the "
             "whole algorithm, and it is the same optimal-substructure argument as every other "
             "page here."),
            ("Index by the set, and fill by increasing set size",
             "A subset is a legitimate index. Entries for a set read entries for strictly "
             "smaller sets, so increasing size is a valid order and can be checked the same "
             "way every other order on this course is checked."),
            ("Close the cycle before you measure a tour",
             "The list that comes back is open: `n` cities, starting at the start, with the "
             "leg home counted in the length and absent from the list. Re-measuring the list "
             "as written gives a tour one leg short, which looks exactly like an off-by-one in "
             "the table."),
            ("Compute both work figures at your own `n` before choosing",
             "`n²2ⁿ` and `(n−1)!` are two integers you can evaluate in a second. Below ten "
             "cities the factorial one is smaller, and the simpler algorithm is also the "
             "faster one. Above it, the table pulls away without bound."),
            ("Check the exact answer against the enumeration while both run",
             "Six tours at four cities, 120 at six, 5 040 at eight. Use the enumeration to "
             "establish the table, note the size at which you had to stop, and do not extend "
             "the claim past it without an argument."),
        ],
        "worked": {
            "title": "Four cities, every tour, and the two work figures",
            "intro": [
                "The distance matrix is asymmetric: row i column j is the distance from city i "
                "to city j, and it need not equal row j column i. The diagonal is zero.",
            ],
            "lines": [
                "          to 1   to 2   to 3   to 4",
                "  from 1      0      2      9     10",
                "  from 2      1      0      6      4",
                "  from 3     15      7      0      8",
                "  from 4      6      3     12      0",
                "",
                "all six tours, each written with the return leg",
                "",
                "  1-2-3-4-1     2 +  6 +  8 +  6   =   22",
                "  1-2-4-3-1     2 +  4 + 12 + 15   =   33",
                "  1-3-2-4-1     9 +  7 +  4 +  6   =   26",
                "  1-3-4-2-1     9 +  8 +  3 +  1   =   21     <- shortest",
                "  1-4-2-3-1    10 +  3 +  6 + 15   =   34",
                "  1-4-3-2-1    10 + 12 +  7 +  1   =   30",
                "",
                "Held-Karp returns length 21 and the list   1, 3, 4, 2",
                "  adding the three legs written down       9 + 8 + 3   =   20",
                "  adding the return leg, city 2 to city 1            +   1",
                "                                                     =   21",
                "",
                "work at four cities",
                "  Held-Karp       n squared times 2 to the n   =   256",
                "  every ordering  n minus 1 factorial          =     6",
            ],
            "after": [
                "The asymmetry is doing real work in this instance. The tour `1-3-4-2-1` uses "
                "the leg from city 2 back to city 1, which costs 1, where the leg from 1 to 2 "
                "costs 2. Its reverse, `1-2-4-3-1`, costs 33. On a symmetric matrix a tour and "
                "its reverse cost the same and half the enumeration is redundant; here it is "
                "not, and nothing in the recurrence assumed it was.",
                "The list `1, 3, 4, 2` has four entries for four cities and the length is "
                "twenty-one. Those two facts are consistent only once you know the convention: "
                "the leg home is counted and not listed. A reader who adds up the list as "
                "written gets 20, concludes the table is off by one, and goes looking for a "
                "bug in the recurrence. There is no bug; there is a convention, and the "
                "check on the panel closes the cycle for exactly this reason.",
                "For a faded rehearsal, switch to the matrix that violates the triangle "
                "inequality before running it. The supplied first move: going straight from "
                "city 1 to city 4 costs fifty, and going round by 2 and 3 costs three, so no "
                "shortcut argument applies and the exact answer is the only answer available. "
                "Predict the optimal tour's length, then check &mdash; and note that the work "
                "figures are unchanged, because they depend on the number of cities and not on "
                "what is in the matrix.",
            ],
        },
        "quiz_title": "Subsets, conventions, and the crossing",
        "quiz": [
            {"q": "What makes indexing by a subset an improvement over trying every ordering?",
             "a": ["Subsets are cheaper to compare than sequences",
                   "Two routes covering the same cities and ending at the same city are interchangeable for the future, so only the shorter is kept",
                   "The number of subsets is smaller than the number of cities factorial for every `n`",
                   "The subset index allows the distances to be asymmetric"],
             "c": 1,
             "why": "That interchangeability is the optimal-substructure argument for this "
                    "problem, and it is what collapses the orderings inside a subset to one "
                    "entry. The comparison cost is not the issue; `n2ⁿ` is larger than "
                    "`(n−1)!` for small `n`, which is the whole point of the page; and "
                    "asymmetry is allowed by both methods."},
            {"q": "Held-Karp returns the list `1, 3, 4, 2` and a length of 21, but adding the legs in the list gives 20. What is going on?",
             "a": ["The table is off by one and the last leg was dropped",
                   "The list is open: the leg home is counted in the length and is not in the list",
                   "The length includes a fixed cost for leaving the start city",
                   "The list is in the wrong order and should be read backwards"],
             "c": 1,
             "why": "Both the table and the enumeration return an open list of `n` cities "
                    "starting at city 1, and the return leg is counted in the length. Adding "
                    "the missing leg from city 2 to city 1, which costs 1, gives 21. The "
                    "convention is documented in the kit and asserted directly by the "
                    "arithmetic checks, so it cannot change quietly."},
            {"q": "At nine cities `n²2ⁿ` is 41 472 and `(n−1)!` is 40 320. What follows?",
             "a": ["Held-Karp is still behind at nine cities and first wins at ten",
                   "The two methods are equivalent at nine cities and either may be used",
                   "The crossing has already happened, since the numbers are close",
                   "The comparison is meaningless because the two count different things"],
             "c": 0,
             "why": "41 472 is larger than 40 320, so the table is behind, narrowly. At ten "
                    "the figures are 102 400 and 362 880 and the table wins for the first "
                    "time, and thereafter for ever. Closeness is not equality, and both "
                    "figures count units of work in the same sense, which is why they are "
                    "printed side by side."},
            {"q": "You have a six-city instance and both algorithms are available. Which does the page recommend, and on what evidence?",
             "a": ["Held-Karp, because `O(n²2ⁿ)` beats `O(n!)`",
                   "Trying every ordering, because at six cities it is 120 against 2 304 and the crossing has not happened",
                   "Held-Karp, because the enumeration cannot handle an asymmetric matrix",
                   "Either: at six cities the difference is a constant factor"],
             "c": 1,
             "why": "The asymptotic comparison is true and is not advice about an instance. At "
                    "six cities the exact figures are 120 and 2 304, and the enumeration is "
                    "nineteen times less work. Both methods handle asymmetry, and a ratio of "
                    "nineteen at one size is not a constant factor &mdash; it is 42 at four "
                    "cities and below 1 at ten."},
        ],
        "mistakes": [
            ("Choosing the better asymptotic algorithm for an instance",
             "The bound says which method wins eventually. On four cities Held-Karp does 256 "
             "units of work against the enumeration's 6, and it is behind all the way to nine. "
             "Evaluating both expressions at your own `n` takes a second and is the only thing "
             "that answers the question you actually have."),
            ("Re-measuring the returned tour without closing the cycle",
             "The list is `n` cities and the tour is `n` legs. Adding the written legs gives a "
             "number one leg short, which looks exactly like an off-by-one in the "
             "reconstruction and sends a reader into the recurrence looking for a bug that is "
             "not there."),
            ("Reading a better exponential as a solution",
             "`n²2ⁿ` is exponential. Held-Karp makes twenty cities possible where twelve was "
             "not, and it does not make the problem tractable. Intractability and "
             "Approximation is where that distinction is made precise and where the honest "
             "alternatives are laid out."),
        ],
        "standard": ("Finish when you can index a table by subsets and say, at your own size, which method to use.",
                     "You should be able to state what a partial tour has to remember, write "
                     "the recurrence over subsets, close the cycle before measuring a returned "
                     "tour, and evaluate both work expressions at a given number of cities "
                     "rather than quoting their order of growth."),
        "note": ("That is the course. Every page has put a measured count beside a proved "
                 "bound, and on four of them the two point in opposite directions at the size "
                 "on screen: the coin table loses to a plain recursion at an amount of six, the "
                 "chain table to enumeration at four matrices, the knapsack grid to every "
                 "subset at four items, and this one by a factor of more than forty. Strings "
                 "and Pattern Matching is next, and its tables are indexed by positions in a "
                 "pattern."),
    },
]
