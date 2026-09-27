"""Sorting and Selection, lessons 01-06 - the promises, quicksort, heapsort, counting sort."""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "what-a-sort-must-promise",
        "title": "What a Sort Must Promise",
        "module": "The four promises",
        "one_line": "Classify four sorts on four promises, then sort records on two keys by stable passes in the right order.",
        "summary": (
            "Order is the least of what a sort is asked for. Three further promises are "
            "separate from it and from each other: whether equal keys keep the order they "
            "arrived in, whether the extra memory is constant, and whether nearly sorted "
            "input is cheaper. None of the three follows from a complexity class, and the "
            "first of them is what lets a two-key sort be done as two one-key passes."
        ),
        "key": [
            "stable       equal keys leave in the order they arrived",
            "in place     Θ(1) extra memory, the input aside",
            "adaptive     cheaper on input that is already nearly sorted",
            "comparison   asks only whether a ≤ b; key-based reads the key itself",
            "two keys by stable passes:   the MINOR key first, then the major",
        ],
        "key_label": "Four promises, and the order two stable passes go in",
        "concepts_intro": (
            "One hard idea: stability. The other two promises are easy to state and are here "
            "because they are routinely confused with stability and with each other."
        ),
        "concepts": [
            ("Stability is a claim about equal keys only",
             "A sort is <strong>stable</strong> when two records with equal keys come out in "
             "the order they went in. Tag every record with the position it started in and "
             "the property becomes visible: after a stable sort the tags inside each run of "
             "equal keys still ascend. On the list `7 3 7 1 9 3 5 1` insertion sort and merge "
             "sort leave every such run alone; selection sort leaves two pairs reversed, "
             "because the long-range swap that puts the minimum in place jumps one equal key "
             "over its twin."),
            ("In place and adaptive are different promises again",
             "<strong>In place</strong> means the extra memory is `Θ(1)`, the input array "
             "aside &mdash; merge sort's standard form needs `Θ(n)` and is not. "
             "<strong>Adaptive</strong> means already-ordered input costs less: insertion "
             "sort is `Θ(n)` on sorted input and `Θ(n²)` on reversed, and heapsort is "
             "`Θ(n log n)` on both. Each promise is independent of the others and of the "
             "complexity class."),
            ("A stable sort composes, and that is what it is for",
             "To order records by a major key with ties broken by a minor key, sort on the "
             "minor key and then on the major, both passes stable. The second pass puts the "
             "major keys in order; inside each run of equal major keys it changes nothing, "
             "so the minor order the first pass established survives. Run the passes the "
             "other way and the second pass, which orders by minor key across the whole "
             "list, destroys the major order the first one built."),
        ],
        "read_title": "Four promises, and which of them a complexity class implies",
        "read_intro": "The definitions, the counterexample that settles a stability question, and why the least significant key is sorted first.",
        "body": [
            ("def", ("Stable sort",
                     "A sorting algorithm is <strong>stable</strong> if, whenever two input "
                     "records have equal keys, the one that appeared earlier in the input "
                     "also appears earlier in the output. The property is about the "
                     "algorithm, for every input, not about one run of it.")),
            ("p", "Equal keys are the only records the definition talks about. A sort that "
                  "gets the order of unequal keys wrong is not unstable; it is broken. So "
                  "stability can only be observed on a list with repeats, and it is observed "
                  "by carrying something the key does not determine &mdash; here the input "
                  "position, called a tag."),
            ("example", ("Selection sort caught on eight keys",
                         "Tag the list `7 3 7 1 9 3 5 1` by position, so the records are "
                         "`7#1 3#2 7#3 1#4 9#5 3#6 5#7 1#8`. Insertion sort returns "
                         "`1#4 1#8 3#2 3#6 5#7 7#1 7#3 9#5` and merge sort returns the same. "
                         "Selection sort returns "
                         "`1#4 1#8 3#6 3#2 5#7 7#3 7#1 9#5`: the threes and the sevens have "
                         "each come out reversed. Two pairs out of input order, and the "
                         "question is settled.")),
            ("p", "That asymmetry is worth being explicit about. One reordered pair refutes "
                  "stability, because stability is a claim about every input and a "
                  "counterexample is enough to kill one. Zero reordered pairs on one list "
                  "establishes nothing at all: there are `8! = 40 320` lists of that length "
                  "and this was one. Stability is proved from the algorithm &mdash; insertion "
                  "sort never moves an element past an equal one, and merge sort's merge "
                  "takes from the left run when the heads are equal &mdash; never from a "
                  "measurement."),
            ("def", ("In place, and adaptive",
                     "An algorithm sorts <strong>in place</strong> if it uses `Θ(1)` memory "
                     "beyond the array it is given. It is <strong>adaptive</strong> if its "
                     "cost falls as its input gets closer to sorted, measured in whatever "
                     "way the analysis names: number of inversions, or number of already "
                     "ordered runs.")),
            ("p", "These two cut across stability and across the complexity class. Merge sort "
                  "is stable, not in place, not adaptive in its standard form. Heapsort is in "
                  "place, not stable, not adaptive. Insertion sort is stable, in place and "
                  "adaptive, and quadratic. Nothing in `Θ(n log n)` implies any of the three, "
                  "which is why the promise a situation needs has to be named before an "
                  "algorithm is chosen."),
            ("h3", "The fourth promise is about what the algorithm is allowed to look at"),
            ("p", "A <strong>comparison sort</strong> may only ask, of two keys, whether one "
                  "is at most the other. Every sort above is one. Discrete Mathematics' "
                  "&ldquo;Searching and Sorting&rdquo; proves that no such algorithm can sort "
                  "every array of `n` keys in fewer than `⌈log₂ n!⌉` comparisons, and that "
                  "bound is cited throughout this course and reproved nowhere in it. A sort "
                  "that reads the key itself &mdash; its digits, its value as an array index "
                  "&mdash; is outside the bound rather than better than it, which is what "
                  "&ldquo;Counting Sort&rdquo; is about."),
            ("thm", ("Two stable passes sort on two keys",
                     "Let a list be sorted by a stable pass on the minor key and then by a "
                     "stable pass on the major key. The result is in increasing order of "
                     "major key, and within each run of equal major keys, in increasing "
                     "order of minor key.")),
            ("proof", ("The second pass orders the major keys, which gives the first claim.",
                       "Take two records with equal major keys. The second pass is stable, "
                       "so it leaves them in the order it found them, which is the order the "
                       "first pass left them in. The first pass ordered the whole list by "
                       "minor key, so of those two the smaller minor key came first. Both "
                       "claims hold, and the only property of the second pass that was used "
                       "is its stability.")),
            ("p", "Read that proof backwards and the misconception dissolves. If the major "
                  "pass runs first, the minor pass afterwards is the one ordering the whole "
                  "list, and what survives inside its ties is the major order &mdash; so the "
                  "output is sorted by minor key, with major keys as a tie-break. That is a "
                  "correct sort of a different thing. The lab runs both orders on the same "
                  "eight records and prints the two sequences."),
            ("p", "This composition is not a curiosity: it is the whole correctness argument "
                  "of radix sort, which is `d` stable passes, one per digit, least "
                  "significant first. &ldquo;Radix Sort&rdquo; makes each pass unstable on "
                  "demand and lets the composition fall apart in front of you."),
        ],
        "lab": ("sortkit", {
            "mode": "stability",
            "algo": "selection",
            "panel_title": "Choose the list and the algorithm",
            "panel_intro": "Every record carries the position it was typed in, so a reordering "
                           "of equal keys is seen rather than claimed. The lower panel sorts "
                           "eight two-key records by two stable passes, in both orders, and "
                           "prints both results.",
        }),
        "steps_title": "Choosing a sort, rather than recalling one",
        "steps_intro": "The promises come before the algorithm, and the memory limit is usually what decides.",
        "steps": [
            ("Name the promises the situation needs",
             "Are there equal keys whose input order carries information? Is there room for "
             "another `n` records? Is the input usually nearly sorted already? Each answer "
             "rules algorithms out, and none of them is the question of which sort is "
             "fastest."),
            ("Tag the records before you sort them",
             "Attach the input position to every record. Without a tag, a reordering of "
             "equal keys is invisible: the keys come out in the same sequence either way. "
             "With one, the output is its own evidence."),
            ("Read a violation as a refutation, and zero as nothing",
             "One pair of equal keys out of input order proves the algorithm is not stable. "
             "No such pair proves nothing about the algorithm: it is one list. If you want "
             "stability, take it from the algorithm's structure, which the lab's hint states "
             "for the two sorts that have it."),
            ("For two keys, sort on the least significant first",
             "Then each later pass has only to order its own key, because it leaves its own "
             "ties alone. Write down which pass you intend to be stable; if a pass is not, "
             "the composition has no argument behind it."),
        ],
        "worked": {
            "title": "Eight records, two keys, and the two pass orders",
            "intro": [
                "The records are written `major:minor`, and they are the eight the lab loads. "
                "The aim is increasing major key, with ties broken by increasing minor key.",
            ],
            "lines": [
                "as typed      3:70  1:40  3:20  2:90  1:10  3:50  2:30  1:60",
                "",
                "the order that works",
                "  pass 1, stable on the MINOR key",
                "              1:10  3:20  2:30  1:40  3:50  1:60  3:70  2:90",
                "  pass 2, stable on the major key",
                "              1:10  1:40  1:60  2:30  2:90  3:20  3:50  3:70      ✓",
                "",
                "the order that does not",
                "  pass 1, stable on the MAJOR key",
                "              1:40  1:10  1:60  2:90  2:30  3:70  3:20  3:50",
                "  pass 2, stable on the minor key",
                "              1:10  3:20  2:30  1:40  3:50  1:60  3:70  2:90      ✗",
                "",
                "the second sequence is sorted by minor key alone:",
                "              10 < 20 < 30 < 40 < 50 < 60 < 70 < 90,",
                "and the major keys 1 3 2 1 3 1 3 2 are in no order at all",
            ],
            "after": [
                "Look at what each pass is responsible for. In the working order, pass 2 is "
                "the last word on the major key and pass 1 survives only inside pass 2's "
                "ties &mdash; which it does exactly because pass 2 is stable. In the other "
                "order, pass 2 is the last word on the minor key, so that is what the output "
                "is sorted by.",
                "The lab's third table row reports whether the two orders happened to agree. "
                "On these records they do not. On a list where every major key is distinct "
                "they would, and that agreement would be a fact about the list rather than "
                "permission to choose the order freely.",
                "For a faded rehearsal, add the record `2:10` to the end of the list and "
                "predict both outputs before running them. The supplied first move is this: "
                "`2:10` has the smallest minor key on the list, so in the working order it "
                "starts the pass-1 sequence &mdash; say where it ends up after pass 2, and "
                "then where it ends up under the other order, and check both in the lab.",
            ],
        },
        "quiz_title": "Promises, and what settles them",
        "quiz": [
            {"q": "On the list `7 3 7 1 9 3 5 1` selection sort leaves two pairs of equal keys out of their input order. What does that establish?",
             "a": ["That selection sort is not stable",
                   "That selection sort is unstable on lists of eight keys, and nothing about other lengths",
                   "That selection sort is nearly stable, since only two pairs moved",
                   "Nothing: one list is not a proof of anything"],
             "c": 0,
             "why": "Stability is a claim about every input, so one counterexample refutes it "
                    "outright. The asymmetry is the point of the lesson: zero violations on "
                    "one list would establish nothing, because that is one list out of "
                    "`8!`, but a single violation is a decided question."},
            {"q": "Records are to end up ordered by major key with ties broken by minor key, using two stable passes. Which pass runs first?",
             "a": ["The major key, then the minor",
                   "The minor key, then the major",
                   "Either: stable passes commute",
                   "The major key twice, once ascending and once descending"],
             "c": 1,
             "why": "The last pass is the one that orders the whole list, so it must be the "
                    "major key; the minor order survives inside its ties precisely because "
                    "it is stable. Running major first gives a list sorted by minor key with "
                    "major as the tie-break, which the lab prints beside the right answer."},
            {"q": "Merge sort and heapsort are both `Θ(n log n)` in the worst case. What follows about stability?",
             "a": ["Both are stable", "Neither is stable",
                   "Nothing: the complexity class says nothing about stability",
                   "Both are stable once they are made to sort in place"],
             "c": 2,
             "why": "Merge sort is stable and heapsort is not, and they share the class, so "
                    "the class cannot decide it. Stability comes from what the algorithm "
                    "does to equal keys: merge sort's merge takes from the left run on a tie, "
                    "and heapsort's sift-down moves an element across most of the array."},
            {"q": "Which promise does insertion sort make that merge sort's standard form does not?",
             "a": ["Stability", "In place, with `Θ(1)` extra memory",
                   "Comparison-based, using only `a ≤ b`",
                   "A `Θ(n log n)` worst case"],
             "c": 1,
             "why": "Both are stable and both are comparison sorts, so neither of those "
                    "separates them; the `Θ(n log n)` worst case is a promise merge sort "
                    "makes and insertion sort does not. What insertion sort adds is constant "
                    "extra memory, where merge sort's merge needs a buffer of `Θ(n)`."},
        ],
        "mistakes": [
            ("Reading stability off the complexity class",
             "Two sorts in the same class need not agree about anything except the growth of "
             "their worst-case comparison count. Merge sort and heapsort are both "
             "`Θ(n log n)`; one is stable, one is in place, and neither is both. The class is "
             "a statement about a count, and stability is a statement about where equal keys "
             "end up."),
            ("Sorting by the primary key first",
             "It feels like the important key should be settled first, and it is exactly "
             "backwards: the last pass is the one whose order survives across the whole "
             "list, so the primary key must be sorted last. The lab runs both orders on the "
             "same records, and the wrong one comes out ordered by the key nobody asked to "
             "order by."),
            ("Taking zero violations as a proof of stability",
             "The lab says &ldquo;no reordering seen&rdquo; rather than &ldquo;stable&rdquo; "
             "for a reason. A list on which every sort happens to be stable teaches nothing, "
             "and the first list tried when this panel was built was one of those. Separate "
             "an equal pair with a smaller key and try again, and take the actual claim from "
             "the algorithm."),
        ],
        "standard": ("Finish when you can say which promise a situation needs before you name a sort.",
                     "You should be able to tag a record list, read a stability violation off "
                     "the output, say why one violation settles the question and zero does "
                     "not, and order a two-key sort's passes with a reason rather than a "
                     "preference."),
        "note": ("The next four lessons are about one algorithm and one that stands beside "
                 "it. &ldquo;Partitioning&rdquo; takes the single pass quicksort is built "
                 "from, and it is worth noticing on the way that the pass is where "
                 "quicksort's instability comes from: a swap moves an element across the "
                 "array, past whatever equal keys lie between."),
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "partitioning",
        "title": "Partitioning",
        "module": "Quicksort and heapsort",
        "one_line": "Partition an array around a pivot in one pass, stating the three-region invariant at every step.",
        "summary": (
            "Partition is the whole of quicksort that is not recursion. One pass over `n` "
            "elements, `n − 1` comparisons against the pivot, and three regions whose "
            "boundaries are the loop's two indices: at most the pivot, above the pivot, not "
            "yet examined. At the end one element is where it belongs for ever, and nothing "
            "else has been sorted."
        ),
        "key": [
            "Lomuto, pivot parked at the end, i starts one before lo",
            "  a[lo..i] ≤ pivot     a[i+1..j−1] > pivot     a[j..hi−1] unexamined",
            "for j = lo to hi − 1:   if a[j] ≤ pivot:  i = i + 1;  swap a[i], a[j]",
            "then swap a[i+1], a[hi]      the pivot lands at i + 1 and never moves again",
            "comparisons = n − 1         on every array of length n, whatever is in it",
        ],
        "key_label": "One pass, three regions, and a count that does not depend on the data",
        "concepts_intro": (
            "The hard idea is the invariant: a statement true before the loop, preserved by "
            "one step of it, and strong enough at the end to be the postcondition."
        ),
        "concepts": [
            ("Three regions, and two indices that name their edges",
             "Lomuto's loop keeps `a[lo..i]` at most the pivot, `a[i+1..j−1]` above it, and "
             "`a[j..hi−1]` unexamined. Before the first step `i = lo − 1` and `j = lo`, so "
             "the first two regions are empty and the invariant holds of any array at all. "
             "Each step examines `a[j]`: if it is above the pivot, `j` advances and the "
             "middle region grows; if not, `i` advances and `a[i]` is swapped with `a[j]`, "
             "moving one element out of the middle region and one into the first."),
            ("The comparison count is n − 1, on every input",
             "Every element except the pivot is compared with the pivot exactly once, so a "
             "Lomuto partition of twelve elements costs eleven comparisons whatever the "
             "twelve are. That is the only figure on the lab's panel that does not depend on "
             "the data, and it is what makes quicksort's cost the sum of its subarray sizes "
             "rather than something that has to be measured. Hoare's two-pointer scheme "
             "stops when the pointers cross, so its count does depend on the data: on the "
             "lab's default array it makes fourteen comparisons where Lomuto makes eleven."),
            ("One element is placed; nothing is sorted",
             "After the final swap the pivot sits at index `i + 1` with everything at most it "
             "to the left and everything above it to the right, so it is at its final sorted "
             "position and will never be touched again. Neither side is sorted. On the lab's "
             "default array the left side comes out `3 9 10 16 7` and the right side "
             "`43 55 38 27 91 82`, and reading either as sorted is the mistake this lesson "
             "exists to prevent."),
        ],
        "read_title": "One pass, and the invariant that makes it correct",
        "read_intro": "The loop, the three regions, the proof that the pivot is placed, and what Hoare does differently.",
        "body": [
            ("def", ("Partition",
                     "To <strong>partition</strong> `a[lo..hi]` around a "
                     "<strong>pivot</strong> value `p` drawn from it is to rearrange the "
                     "subarray so that `p` sits at some index `q` with `a[lo..q−1] ≤ p` and "
                     "`a[q+1..hi] > p`. The index `q` is returned; it is not chosen in "
                     "advance and is not generally the middle.")),
            ("p", "Lomuto's scheme is the one this course counts. Swap the chosen pivot to "
                  "the end of the subarray, walk `j` from `lo` to `hi − 1`, and keep a second "
                  "index `i` marking the end of the at-most-pivot region. That is the whole "
                  "algorithm, and the pseudocode of it is four lines in the block above."),
            ("def", ("Loop invariant",
                     "A <strong>loop invariant</strong> is a statement about the program's "
                     "state that is true before the loop begins, and true after each "
                     "iteration if it was true before that iteration. It is useful when its "
                     "truth at the loop's exit, together with the exit condition, gives the "
                     "postcondition you wanted.")),
            ("p", "The invariant here is the three regions. It holds before the loop because "
                  "two of the regions are empty. It is preserved by each step, in the two "
                  "cases the concept card gives. And at exit `j = hi`, so the unexamined "
                  "region is empty and the array is exactly `at most | above | pivot`, one "
                  "swap away from what was wanted."),
            ("thm", ("Partition places the pivot",
                     "When the loop exits, swapping `a[i+1]` with `a[hi]` leaves the pivot at "
                     "index `i + 1` with every element of `a[lo..i]` at most it and every "
                     "element of `a[i+2..hi]` above it. The pivot is therefore at its final "
                     "position in the sorted array.")),
            ("proof", ("At exit the invariant gives `a[lo..i] ≤ p` and `a[i+1..hi−1] > p`, "
                       "with the pivot itself still at `hi`.",
                       "The final swap exchanges the pivot with `a[i+1]`, which is above the "
                       "pivot, so it lands in the region of elements above the pivot, where "
                       "it belongs. The pivot lands at `i + 1`. Every element to its left is "
                       "at most it and every element to its right is above it, which is the "
                       "definition of that position being its place in sorted order &mdash; "
                       "and that is a property of the final array, not of this pass, so no "
                       "later recursion can disturb it.")),
            ("example", ("Twelve elements, pivot 24",
                         "The array is `38 27 43 3 9 82 10 55 16 7 91 24` and the pivot is "
                         "the last element, `24`. Eleven comparisons and six swaps later the "
                         "array is `3 9 10 16 7 24 43 55 38 27 91 82`, with the pivot at "
                         "position six. Five elements are at most `24` and six are above it, "
                         "and neither group is in order. The worked example below steps "
                         "through all eleven comparisons.")),
            ("h3", "Hoare's scheme, and what it buys"),
            ("p", "Hoare's partition walks one index up from the left and one down from the "
                  "right, swapping an out-of-place pair whenever both stop, and finishes when "
                  "the indices cross. It does about a third as many swaps as Lomuto on "
                  "typical data &mdash; four rather than six on the lab's array &mdash; and "
                  "it does not place the pivot at a known index; it returns a boundary. Its "
                  "comparison count is data-dependent, which is why the clean `n − 1` above "
                  "is stated for Lomuto and not for partition in general."),
            ("p", "Both schemes send keys equal to the pivot to one side. That sounds like a "
                  "detail and it is the subject of a counterexample two lessons from here: on "
                  "an array whose keys are all equal, Lomuto splits `n` into `0` and `n − 1` "
                  "under every pivot rule there is, including a randomised one."),
            ("p", "Two things are worth checking in the lab's step table. The `i` and `j` "
                  "columns count from zero, which is why `i` starts at `−1`: the at-most "
                  "region is empty, and an index one before the start is how that is said. "
                  "And the invariant column is evaluated on the array at that step rather "
                  "than assumed, so a broken invariant would appear as the word BROKEN and "
                  "not as a missing row."),
        ],
        "lab": ("sortkit", {
            "mode": "partition",
            "keys": "38, 27, 43, 3, 9, 82, 10, 55, 16, 7, 91, 24",
            "scheme": "lomuto",
            "pivot": 12,
            "step": 6,
            "panel_title": "Choose the array, the pivot and the step",
            "panel_intro": "The partition runs in the browser and records every step. The "
                           "invariant column is computed from the array at that step, so a "
                           "broken invariant would show as a broken invariant rather than as "
                           "a missing one.",
        }),
        "steps_title": "Partitioning by hand without losing the invariant",
        "steps_intro": "Write the two indices down at every step. The array alone does not tell you where the regions are.",
        "steps": [
            ("Park the pivot and set the indices",
             "Swap the chosen pivot to the last position of the subarray. Set `j` to the "
             "first position and `i` to one before it. Say out loud what the invariant "
             "asserts now: both named regions are empty, so it holds."),
            ("For each j, compare once and do one of two things",
             "If `a[j]` is above the pivot, do nothing but advance `j`; the middle region "
             "grew. If `a[j]` is at most the pivot, advance `i`, swap `a[i]` with `a[j]`, "
             "then advance `j`. Exactly one comparison happens per step, which is where "
             "`n − 1` comes from."),
            ("Check the invariant on the array, not in your head",
             "After each step, read the array back: everything up to `i` should be at most "
             "the pivot and everything from `i + 1` to `j − 1` above it. This is the step "
             "where an off-by-one in the swap shows up, while it is still one line of work "
             "to undo."),
            ("Place the pivot and state what you have",
             "Swap `a[i+1]` with the pivot at the end. Now say the postcondition: one element "
             "is final, the two sides are separated, and neither side is sorted. If you "
             "catch yourself expecting a sorted side, look at the lab's final row."),
            ("Count, and compare the count with the bound",
             "Lomuto makes `n − 1` comparisons on every array. The panel prints that beside "
               "`⌈log₂ n!⌉`, the number any comparison sort needs for the whole job, so the "
               "two figures on screen are one measurement and one proof about every "
               "algorithm. Sorting twelve elements needs at least twenty-nine comparisons; "
               "one partition of them spends eleven."),
        ],
        "worked": {
            "title": "All eleven comparisons, with the indices",
            "intro": [
                "The array is the lab's default and the pivot is its last element, `24`. The "
                "indices are written as the lab writes them, counting from zero, so `i = −1` "
                "means the at-most region is still empty. The array shown on each line is "
                "the array after that step.",
            ],
            "lines": [
                "pivot 24, i = −1, j = 0",
                "",
                " step   a[j]  ≤ 24?   i    array",
                "   1     38     no   −1    38 27 43  3  9 82 10 55 16  7 91 24",
                "   2     27     no   −1    38 27 43  3  9 82 10 55 16  7 91 24",
                "   3     43     no   −1    38 27 43  3  9 82 10 55 16  7 91 24",
                "   4      3    yes    0     3 27 43 38  9 82 10 55 16  7 91 24",
                "   5      9    yes    1     3  9 43 38 27 82 10 55 16  7 91 24",
                "   6     82     no    1     3  9 43 38 27 82 10 55 16  7 91 24",
                "   7     10    yes    2     3  9 10 38 27 82 43 55 16  7 91 24",
                "   8     55     no    2     3  9 10 38 27 82 43 55 16  7 91 24",
                "   9     16    yes    3     3  9 10 16 27 82 43 55 38  7 91 24",
                "  10      7    yes    4     3  9 10 16  7 82 43 55 38 27 91 24",
                "  11     91     no    4     3  9 10 16  7 82 43 55 38 27 91 24",
                "",
                "final swap a[i+1] with a[hi]:  82 ↔ 24",
                "              3  9 10 16  7 24 43 55 38 27 91 82",
                "",
                "comparisons 11 = n − 1        swaps 6        pivot at position 6",
            ],
            "after": [
                "Five steps moved something and six did not, and the six that did not are "
                "where the middle region grew. The pivot's final position, six, was not "
                "chosen: it is one more than the number of elements at most `24`, which the "
                "pass discovered.",
                "Now read the two sides. `3 9 10 16 7` is not sorted and neither is "
                "`43 55 38 27 91 82`. Everything the pass promised is true and nothing more "
                "is: one element final, two groups separated, `n − 1` comparisons spent.",
                "For a faded rehearsal, change the pivot position slider to `1`, so the pivot "
                "is `38`. The supplied first move is the count: it is still eleven "
                "comparisons, because Lomuto's count does not depend on which element is the "
                "pivot. Predict the pivot's final position before running it &mdash; count "
                "how many of the twelve keys are at most `38` &mdash; and then check the "
                "swap count, which does change.",
            ],
        },
        "quiz_title": "One pass, and what it leaves behind",
        "quiz": [
            {"q": "A Lomuto partition of twelve elements around one pivot makes how many comparisons?",
             "a": ["Eleven, on every array of twelve elements",
                   "Eleven on average, and more when the data is badly arranged",
                   "Between eleven and sixty-six, depending on the data",
                   "Twelve, one per element"],
             "c": 0,
             "why": "Every element except the pivot is compared with the pivot exactly once, "
                    "so the count is `n − 1` regardless of the contents. The data-dependent "
                    "count belongs to Hoare's scheme, which made fourteen comparisons on the "
                    "same twelve elements."},
            {"q": "Immediately after one partition of `a[lo..hi]`, what is true?",
             "a": ["Both sides are sorted",
                   "The pivot is at its final sorted position, and nothing else is sorted",
                   "The left side is sorted and the right side is not",
                   "The array has one inversion fewer than it had"],
             "c": 1,
             "why": "Everything left of the pivot is at most it and everything right of it is "
                    "above it, which is exactly what its final position means &mdash; and "
                    "that is all. On the lab's array the left side comes out `3 9 10 16 7`, "
                    "which is a counterexample to the other three answers at once."},
            {"q": "At the start of the pass Lomuto sets `i` to one before `lo`. What does the invariant assert at that moment?",
             "a": ["That the at-most-pivot region is empty, which is true of any array",
                   "That the invariant does not hold yet, and starts holding after the first step",
                   "That `a[lo]` is at most the pivot",
                   "That the pivot is already at index `lo`"],
             "c": 0,
             "why": "An empty region satisfies &ldquo;every element of it is at most the "
                    "pivot&rdquo; vacuously, which is why the invariant can be established "
                    "before anything has been examined. An invariant that only starts holding "
                    "later is not an invariant, and the proof of the postcondition would have "
                    "nothing to stand on."},
            {"q": "On the lab's array Hoare's scheme made fourteen comparisons where Lomuto made eleven. What does that show?",
             "a": ["That Hoare's scheme is the worse of the two",
                   "That Hoare's comparison count depends on the data, so it is not `n − 1`",
                   "That Hoare's scheme compares every element with the pivot twice",
                   "That the pivot was badly chosen for Hoare's scheme"],
             "c": 1,
             "why": "Hoare's pointers stop and swap and continue until they cross, so how many "
                    "comparisons that takes is a function of the arrangement. Fourteen on this "
                    "array is one measurement; Hoare's scheme also does fewer swaps here, four "
                    "against six, which is why it is the one usually implemented."},
        ],
        "mistakes": [
            ("Expecting partition to sort the two sides",
             "It places one element and separates the rest, and the separation is not an "
             "ordering. The lab's final row prints the whole array after the pass so that "
             "both sides can be read: on the default input the left side is `3 9 10 16 7`. "
             "Sorting the sides is what the recursion does, not this pass."),
            ("Losing the invariant in the swap",
             "The common slip is to swap `a[i]` with `a[j]` before advancing `i`, which "
             "overwrites the boundary element. Advance `i` first, then swap, then advance "
             "`j`. The lab's invariant column is computed from the array itself at each step, "
             "so the step where this happens is visible rather than deduced from a wrong "
             "answer at the end."),
            ("Assuming the pivot ends near the middle",
             "The pivot lands one past the number of elements at most it, which is a fact "
             "about the data. On the lab's default array with pivot `24` it lands at position "
               "six of twelve; with pivot `43` it lands at position nine. Nothing in the pass "
               "aims for the middle, and “Quicksort and Its Worst Case” is about what "
               "happens when it "
               "misses badly and repeatedly."),
        ],
        "standard": ("Finish when you can run a partition on paper and state the invariant at every step.",
                     "You should be able to partition twelve elements around a named pivot, "
                     "say why the comparison count is `n − 1` before running it, predict the "
                     "pivot's final position by counting, and state the postcondition without "
                     "claiming either side is sorted."),
        "note": ("Quicksort is this pass, twice, on the two sides, recursively. Everything "
                 "about its cost is therefore a question about the sizes of those sides, "
                 "which is what &ldquo;Quicksort and Its Worst Case&rdquo; takes up &mdash; "
                 "and the answer is that the sizes depend on a rule that the input can be "
                 "chosen against."),
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "quicksort-and-its-worst-case",
        "title": "Quicksort and Its Worst Case",
        "module": "Quicksort and heapsort",
        "one_line": "Count quicksort's comparisons on the input built to defeat the pivot rule you chose, and place the count in the recurrence.",
        "summary": (
            "Quicksort's cost is the sum of the subarray sizes it partitions, so the split "
            "decides everything and the pivot rule decides the split. Every deterministic "
            "rule is a function of the array, which means an array can be built against it: "
            "the lab builds one by answering the rule's own comparisons adversarially, then "
            "runs the ordinary quicksort on what comes out and counts."
        ),
        "key": [
            "T(n) = T(k) + T(n − k − 1) + (n − 1)      k = how many keys are below the pivot",
            "balanced   k ≈ n/2      depth about log₂ n      about n log₂ n comparisons",
            "one-sided  k = 0 every time      depth n      n(n − 1)/2 comparisons",
            "first-element pivot on sorted input, 32 keys:   496 = n(n − 1)/2",
            "median of three on the array built for it, 32 keys:   304, depth 16",
        ],
        "key_label": "One recurrence, and the two ends of what the split can do",
        "concepts_intro": (
            "The hard idea is that a pivot rule is a claim about inputs, and a claim about "
            "inputs can be attacked by choosing one."
        ),
        "concepts": [
            ("The cost is the sum of the subarray sizes",
             "Each call partitions its range at a cost of one less than its length, then "
               "recurses on the two pieces. So the total comparison count is the sum, over "
               "every call, of that call's length minus one &mdash; nothing else. A balanced "
               "split halves the length each level, giving about `log₂ n` levels of about `n` "
               "work; a split that peels off one element at a time gives `n` levels, and "
               "`(n−1) + (n−2) + … + 1 = n(n − 1)/2`."),
            ("A deterministic rule is a function, so it can be inverted",
             "Take the first element, the middle element, the median of three named "
               "positions: each is a rule that reads the array and returns a position. Run "
               "the rule and answer each of its comparisons so as to keep the worst case "
               "reachable, and what falls out is a permutation on which that rule is bad "
               "every time. The lab does this rather than quoting an array from a paper, and "
               "then hands the array to the ordinary quicksort, which measures it: 304 "
               "comparisons for median of three at 32 keys, where `n log₂ n` is 160."),
            ("The worst case moves; it does not leave",
             "Median of three is a real improvement on sorted input &mdash; 151 comparisons "
               "at 32 keys where a first-element pivot pays 496. It is not a bound, because "
               "its own killer exists and the lab ships it. And the killer is rule-specific: "
               "the array built against median of three costs a first-element pivot only 143, "
               "because a bad input for one rule is not a bad input for another."),
        ],
        "read_title": "The recurrence, the two extremes, and the array built against a rule",
        "read_intro": "Where quicksort's comparisons come from, what the split does to them, and how an input is constructed to make the split bad.",
        "body": [
            ("def", ("Quicksort",
                     "To <strong>quicksort</strong> `a[lo..hi]`: if the range holds fewer "
                     "than two elements, stop. Otherwise partition it around a pivot chosen "
                     "by a <strong>pivot rule</strong>, then quicksort the part left of the "
                     "pivot and the part right of it. The pivot itself is never looked at "
                     "again.")),
            ("p", "There is no merge step and no extra array. All the work is in the "
                  "partitions, and by “Partitioning” each partition of a range of length "
                  "`m` costs `m − 1` comparisons. So the comparison count of a whole run is "
                  "determined by the multiset of range lengths the recursion visits, and "
                  "that is determined by the splits."),
            ("math", [
                "T(n) = T(k) + T(n − k − 1) + (n − 1)      T(0) = T(1) = 0",
                "",
                "k = n/2 each time:   T(n) ≈ 2T(n/2) + n   ⟹   T(n) = Θ(n log n)",
                "k = 0    each time:  T(n) = T(n − 1) + (n − 1)  =  n(n − 1)/2",
            ]),
            ("p", "Those two lines are the same recurrence with two values of `k`, and the "
                  "gap between their solutions is the whole subject of the lesson. "
                  "Discrete Mathematics' &ldquo;Divide and Conquer&rdquo; solves the first by "
                  "the master theorem and &ldquo;Recursion Trees and Amortised Analysis&rdquo; "
                  "gives the tree argument the second one is a degenerate case of. Neither "
                  "tells you which `k` you get; the pivot rule and the input do."),
            ("example", ("A first-element pivot on sorted input",
                         "The pivot is the smallest key, so `k = 0`: the left side is empty "
                         "and the right side has `n − 1` elements. Then the same thing "
                         "happens again. At 32 keys the lab measures 496 comparisons and a "
                         "recursion depth of 31, against `n(n − 1)/2 = 496` &mdash; the "
                         "recurrence's worst case, met exactly. Already-sorted input is the "
                         "commonest input there is, which is what makes this rule not merely "
                         "theoretically bad.")),
            ("h3", "Building the array that defeats a rule"),
            ("p", "The lab's killer input is constructed, not recalled. It runs the chosen "
                  "rule on `n` items whose values are not yet decided, and whenever the rule "
                  "compares two undecided items it freezes one of them at the next smallest "
                  "value available &mdash; choosing which one so that the pivot keeps turning "
                  "out to be near the smallest thing left. Every answer it gives is "
                  "consistent with the values it finally hands back, so what comes out is a "
                  "real permutation of `1 … n` and not a trick."),
            ("p", "That is the same manoeuvre as the lower-bound arguments at the end of this "
                  "course: answer the algorithm's questions so as to keep the bad case alive. "
                  "Here it is aimed at one rule rather than at every algorithm, which is why "
                  "it produces an input rather than a bound."),
            ("example", ("Median of three, against its own killer",
                         "At 32 keys the array the lab builds is "
                         "`1 18 4 26 6 20 8 30 10 22 12 28 14 24 16 2 3 5 7 …` and the "
                         "adversary answered 316 of the rule's comparisons while building "
                         "it. The ordinary quicksort then spends 304 comparisons on it and "
                         "recurses 16 deep, where a balanced split would be about 6 deep and "
                         "`n log₂ n` is 160. Halve the length to 16 and the count is 88; "
                         "doubling `n` multiplied the work by 3.45.")),
            ("p", "A count that roughly quadruples when `n` doubles is behaving quadratically "
                  "and a count that roughly doubles is not, and the lab prints the ratio at "
                  "two sizes rather than reading a verdict off a curve. Two sizes are two "
                  "measurements. The `n log₂ n` and `n(n − 1)/2` lines on the plot are "
                  "drawings sampled at double precision; every verdict on the panel compares "
                  "integers."),
            ("p", "Two further readings from the same panel are worth having. First, "
                  "rule-specificity: the array built against median of three costs a "
                  "first-element pivot 143 comparisons, and the array built against a "
                  "first-element pivot costs a middle-element pivot 103. Each rule has its "
                  "own bad input, which is exactly what it means for the flaw to be in the "
                  "rule rather than in quicksort. Second, the array of 24 equal keys: every "
                  "rule pays 276 there, `n(n − 1)/2` again, because Lomuto sends every key "
                  "equal to the pivot to one side."),
            ("p", "So what is quicksort's cost? On the input in front of you, whatever the "
                  "lab measured. As a claim about all inputs under a deterministic rule, "
                  "`Θ(n²)`, because the killer exists. “Randomised Quicksort” changes the "
                  "question by changing where the randomness lives, and gets an answer that is exact "
                  "and holds on every input at once."),
        ],
        "lab": ("sortkit", {
            "mode": "quick",
            "n": 32,
            "rule": "median3",
            "order": "killer",
            "seed": 7,
            "panel_title": "Choose the rule, then meet the array built against it",
            "panel_intro": "The killer array is constructed by answering the rule's own "
                           "comparisons adversarially, then handed to the ordinary quicksort, "
                           "which counts what it does. Change the rule and the array changes "
                           "with it.",
        }),
        "steps_title": "Reading a pivot rule as a claim about inputs",
        "steps_intro": "Do not ask how fast the rule is. Ask which inputs it is betting against, and then look for one.",
        "steps": [
            ("Write the recurrence with the split you expect",
             "Put your guess for `k` into `T(n) = T(k) + T(n − k − 1) + (n − 1)` and solve it. "
             "This is where a claim becomes falsifiable: a rule that promises `k ≈ n/2` is "
             "promising something about every input, and one input is enough to test it."),
            ("Try the inputs that are common before the inputs that are clever",
             "Sorted, reverse sorted, up-then-down, all keys equal. A first-element pivot "
             "fails on the first two immediately, at 496 comparisons for 32 keys. A rule that "
             "survives these has only survived four families."),
            ("Then let the lab build the input against the rule",
             "Choose the killer order and watch the count and the depth. The array is a "
             "permutation of `1 … n`, the sort still returns the sorted array, and the cost "
             "is quadratic: the bad case is exhibited rather than asserted."),
            ("Measure at two sizes and read the ratio, not the curve",
             "Halve `n` and compare. About four times the work means quadratic behaviour on "
             "this family; about twice means `n log n` behaviour on this family. Neither is a "
             "proof, and the word to use out loud is &ldquo;on this family&rdquo;."),
            ("Compare the measured count with something that did not come from quicksort",
             "The table's footer prints merge sort's comparison count on the same array, from "
             "an implementation written for another course, and the panel prints "
             "`⌈log₂ n!⌉`. One is an independent measurement and the other is a bound on "
             "every comparison sort; a measured count above both is a cost, not a "
             "contradiction."),
        ],
        "worked": {
            "title": "Median of three on the array built for it, at thirty-two keys",
            "intro": [
                "Set the pivot rule to median of first, middle and last, the input order to "
                "the array built to kill this rule, and the length to 32. The array below is "
                "what the lab constructs, and the call table is the first eight partitions of "
                "the run it then measures.",
            ],
            "lines": [
                "the array the adversary built (a permutation of 1 … 32):",
                "  1 18 4 26 6 20 8 30 10 22 12 28 14 24 16 2 3 5 7 9 11 13 15 17 19 …",
                "",
                " call   range    pivot   lands at   sizes left | right   depth",
                "   1     1–32      2         2           0 | 30           1",
                "   2     3–32      4         4           0 | 28           2",
                "   3     5–32      6         6           0 | 26           3",
                "   4     7–32      8         8           0 | 24           4",
                "   5     9–32     10        10           0 | 22           5",
                "   6    11–32     12        12           0 | 20           6",
                "   7    13–32     14        14           0 | 18           7",
                "   8    15–32     16        16           0 | 16           8",
                "",
                "measured        304 comparisons, depth 16",
                "n log₂ n        160          (a drawing, sampled)",
                "n(n − 1)/2      496          (the recurrence's worst case)",
                "⌈log₂ 32!⌉      118          (what every comparison sort needs)",
                "merge sort      111          on the same array, counted by running it",
            ],
            "after": [
                "Every left side is empty. That is the signature: the rule's three candidates "
                "have been arranged so that their median is always the smallest key left, so "
                "`k = 0` at every call and the recurrence degenerates to "
                "`T(n) = T(n − 1) + (n − 1)`. The depth is 16 rather than 31 because the "
                "adversary only has to fool the rule on the first half of the array; after "
                "that the tail is already arranged.",
                "The measured 304 is below `n(n − 1)/2 = 496`, and the difference is the "
                "three comparisons per call the median-of-three rule spends on its own "
                "decision, plus the shape of the tail. So the measurement is not the "
                "recurrence's worst case exactly; it is quadratic behaviour on a real input, "
                "which is what was to be shown.",
                "For a faded rehearsal, keep the killer order and change the rule to a seeded "
                "random pivot. The supplied first move: the array is rebuilt, because the "
                "killer is a function of the rule, and for a randomised rule the lab builds "
                "the median-of-three killer instead. Predict what happens to the count before "
                "you look, then move the seed slider and watch the count move while nothing "
                "else does &mdash; that is “Randomised Quicksort” in one control.",
            ],
        },
        "quiz_title": "Splits, rules and what a count proves",
        "quiz": [
            {"q": "Median of three costs 88 comparisons on its killer at 16 keys and 304 at 32. Which reading is right?",
             "a": ["It is `Θ(n log n)`, because 304 is below twice `n log₂ n`",
                   "The count more than tripled when `n` doubled, the signature of a quadratic cost, on this family of inputs",
                   "Quicksort is `Θ(n²)`, and that is what these two numbers prove",
                   "The killer array is not a real permutation, so the counts do not mean anything"],
             "c": 1,
             "why": "Two measurements at two sizes are evidence about this family and nothing "
                    "more, which is why the answer names the family. The lab builds the array "
                    "as a permutation of `1 … n` and checks that quicksort still sorts it, so "
                    "the last answer is ruled out by construction."},
            {"q": "Why does taking the median of three elements fail to make quicksort `O(n log n)`?",
             "a": ["Because the rule is deterministic, so an array can be built on which its choice is bad at every call",
                   "Because the median of three is only defined when `n` is odd",
                   "Because the median of three of a sorted array is its first element",
                   "Because the recurrence has no solution when the split is uneven"],
             "c": 0,
             "why": "The rule is a function of the array, and the lab inverts it: it answers "
                    "the rule's own comparisons so that the median of the three candidates is "
                    "always the smallest key remaining. On sorted input the median of first, "
                    "middle and last is the middle key, which is why that particular input is "
                    "no longer bad for this rule &mdash; the worst case moved rather than left."},
            {"q": "On 24 keys that are all equal, quicksort with a seeded random pivot made 276 comparisons on every seed tried. Why?",
             "a": ["The seeded stream repeats itself at small sizes",
                   "Lomuto sends every key equal to the pivot to the same side, so the split is `0` and `n − 1` whatever the pivot is",
                   "Random pivots do not help below about 50 elements",
                   "276 is `n log₂ n` at 24 keys, so the count is the expected one"],
             "c": 1,
             "why": "`276 = 24 × 23/2`, the one-sided worst case, and it is reached under every "
                    "rule including the randomised one, because with all keys equal every "
                    "comparison answers the same way. `n log₂ n` at 24 is about 110. This is "
                    "the array on which randomising the pivot buys nothing at all."},
            {"q": "The run above recursed 16 deep on 32 keys. What depth would a balanced split give?",
             "a": ["About 6", "16", "31", "About 11"],
             "c": 0,
             "why": "Halving the range each time gives `⌊log₂ 32⌋ + 1 = 6` levels, which is the "
                    "figure the lab prints beside the measured depth. Depth 16 is half of 31 "
                    "because the constructed array only needs its first half arranged against "
                    "the rule."},
        ],
        "mistakes": [
            ("Turning a worst case into a verdict about which sort is faster",
             "&ldquo;Quicksort is `O(n²)` so it is slower than merge sort&rdquo; puts two "
             "different questions in one sentence. `O(n²)` describes one family of inputs "
             "under one pivot rule; on a seeded shuffle of 32 keys a random pivot averages "
             "139.96 comparisons over 200 seeds against merge sort's 120 on the same array. "
             "And comparisons are not time: this course counts comparisons, so &ldquo;faster&rdquo; "
             "is a question its labs cannot settle at all."),
            ("Believing a better pivot rule removes the worst case",
             "Every deterministic rule has a killer, because every deterministic rule is a "
             "function of the array. Median of three, median of five, the median of three "
             "medians of three: each improves the inputs that used to be bad and acquires new "
             "ones. What changes the answer is not a cleverer rule but moving the randomness "
             "out of the data, which is what “Randomised Quicksort” does."),
            ("Reading the verdict off the drawn curve",
             "The `n log₂ n` and `n(n − 1)/2` curves on the plot are sampled at double "
               "precision and drawn; the measured points are integers produced by running the "
               "sort. A measured point that looks close to a curve is not a classification, "
               "and the panel's own verdict is computed from counts at two sizes instead."),
        ],
        "standard": ("Finish when a pivot rule reads as a bet about inputs rather than as a speed.",
                     "You should be able to write the recurrence for a given split, say what "
                     "`k = 0` at every call costs, explain how the lab builds an input against "
                     "a rule, and state what a count at two sizes does and does not establish."),
        "note": ("The fix is not a better rule. It is to make the pivot choice random, so "
                 "that the algorithm's behaviour no longer depends on which array it was "
                 "handed &mdash; and then the cost has an expectation that can be computed "
                 "exactly. &ldquo;Randomised Quicksort&rdquo; derives it, and it is the "
                 "pattern every expectation later on this path follows."),
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "randomised-quicksort",
        "title": "Randomised Quicksort",
        "module": "Quicksort and heapsort",
        "one_line": "Derive the exact expected comparison count with indicator variables, and say why it holds for every input.",
        "summary": (
            "Choose the pivot at random and quicksort's cost stops being a function of the "
            "input. Two keys are compared exactly when one of them is the first pivot drawn "
            "from the stretch of sorted order between them, which happens with probability "
            "`2/(j − i + 1)`; linearity of expectation adds the indicators up to "
            "`2(n+1)Hₙ − 4n`. That number is exact, it is under `2n ln n`, and it is the same "
            "on a sorted array, a reversed one and the array built to destroy median of three."
        ),
        "key": [
            "Xᵢⱼ = 1 if the i-th and j-th smallest keys are ever compared, else 0",
            "P(Xᵢⱼ = 1) = 2/(j − i + 1)     one of the two must be the first pivot drawn",
            "E[X] = Σ E[Xᵢⱼ] = 2(n+1)Hₙ − 4n     linearity; independence is never needed",
            "                 < 2n ln n           and it holds on EVERY input",
            "n = 9:   E[X] = 2593/126 = 20.5794      Hₙ = 7129/2520, exactly",
        ],
        "key_label": "The indicator, its probability, and the sum they give",
        "concepts_intro": (
            "One hard idea, and it is a shift in what the randomness is about rather than a "
            "new technique. The technique is Discrete Mathematics' linearity of expectation."
        ),
        "concepts": [
            ("The randomness is the algorithm's, not the data's",
             "&ldquo;Expected `Θ(n log n)`&rdquo; here does not mean &ldquo;`Θ(n log n)` on a "
             "typical array&rdquo;. Nothing is assumed about the array. The expectation is "
             "over the pivot choices the algorithm makes, and it is the same number for every "
             "array of `n` distinct keys &mdash; including the one built to destroy median "
             "of three. The lab settles this by averaging over every "
             "pivot sequence there is, on five different arrays, and getting one fraction."),
            ("Two keys are compared at most once, and only by a pivot",
             "Write the keys in sorted order as `z₁ … zₙ`. Two of them are compared only when "
             "one is the pivot of a call containing the other, so at most once in the whole "
             "run. And they land in different calls as soon as some key strictly between them "
             "is chosen as a pivot first. So the event `Xᵢⱼ` is decided entirely by which "
             "element of `zᵢ … zⱼ` is drawn as a pivot first: `zᵢ` or `zⱼ` gives a comparison, "
             "any of the others separates them for ever."),
            ("Linearity sums dependent indicators without apology",
             "There are `n(n − 1)/2` indicators and they are not independent: if `z₁` and `z₉` "
             "were compared, that says something about which pivots were drawn, and so about "
             "the other indicators. Linearity of expectation does not care. "
             "`E[ΣXᵢⱼ] = ΣE[Xᵢⱼ]` holds for any random variables at all, which is why this "
             "derivation is three lines rather than a case analysis."),
        ],
        "read_title": "The indicator argument, and the fraction it produces",
        "read_intro": "Why two keys are compared with probability two over their distance, and how the double sum collapses to a harmonic number.",
        "body": [
            ("def", ("Randomised quicksort",
                     "<strong>Randomised quicksort</strong> is quicksort with one change: the "
                     "pivot of each call is chosen uniformly at random from that call's range. "
                     "The input is not shuffled and nothing is assumed about it. Every run on "
                     "the same array may cost a different number of comparisons.")),
            ("p", "Rename the keys by rank: `z₁` is the smallest, `zₙ` the largest. This is a "
                  "relabelling, not an assumption &mdash; the algorithm never sees the names. "
                  "Let `Xᵢⱼ` be `1` if `zᵢ` and `zⱼ` are compared at some point during the "
                  "run and `0` otherwise, and let `X` be the total number of comparisons, "
                  "which is the sum of the `Xᵢⱼ` over all `i < j`."),
            ("thm", ("The comparison criterion",
                     "For `i < j`, the keys `zᵢ` and `zⱼ` are compared during the run if and "
                     "only if the first pivot chosen from among `zᵢ, zᵢ₊₁, …, zⱼ` is `zᵢ` or "
                     "`zⱼ`. Consequently `P(Xᵢⱼ = 1) = 2/(j − i + 1)`.")),
            ("proof", ("All of `zᵢ … zⱼ` begin in the same call, since every call holds a "
                       "contiguous stretch of sorted order and this stretch has not been "
                       "split yet. Consider the first pivot drawn from that stretch.",
                       "If it is some `z_m` with `i &lt; m &lt; j`, then `zᵢ` goes to the left "
                       "side and `zⱼ` to the right, they are never in the same call again, and "
                       "they are never compared: a comparison only ever happens between a "
                       "pivot and another element of the same call. If it is `zᵢ` or `zⱼ`, that "
                       "one is the pivot of a call containing the other, so the two are "
                       "compared exactly then.",
                       "Every element of the stretch is equally likely to be the first of the "
                       "stretch drawn, because each call draws uniformly from its range. The "
                       "stretch has `j − i + 1` elements and two of them give a comparison, so "
                       "the probability is `2/(j − i + 1)`.")),
            ("math", [
                "E[X] = Σ       Σ      2/(j − i + 1)          the double sum over i < j",
                "     i=1..n−1  j=i+1..n",
                "",
                "     = Σ       Σ      2/(d + 1)              d = j − i",
                "     i=1..n−1  d=1..n−i",
                "",
                "     = 2(n+1)Hₙ − 4n                         Hₙ = 1 + 1/2 + … + 1/n",
                "     <  2n ln n",
            ]),
            ("p", "The inner sum is a tail of the harmonic series, and collecting the "
                  "identical terms across the outer sum gives the closed form. The bound "
                  "`Hₙ &lt; 1 + ln n` turns it into `2n ln n`, which is the form usually "
                  "quoted &mdash; but the closed form is exact and the lab prints it as a "
                  "fraction, because `Hₙ` is computed as a rational and not as a float."),
            ("example", ("Nine keys, three ways",
                         "At `n = 9` the closed form is `2593/126 = 20.5794` comparisons, with "
                         "`H₉ = 7129/2520`. The lab computes the same number twice more. Once "
                         "by solving `T(n) = (n−1) + (1/n)Σ(T(i) + T(n−1−i))` from the bottom, "
                         "which contains no harmonic number at all. And once by enumerating "
                         "every one of the 4 862 possible pivot sequences on the array on "
                         "screen and averaging exactly. Three definitions, one fraction.")),
            ("p", "That third row is the one that matters, because it is not a sample. It is a "
                  "claim about every run of the algorithm on that array, computed rather than "
                  "argued. Run it on a sorted array, a reversed array, an up-then-down array, "
                  "a seeded shuffle and the median-of-three killer, and all five give "
                  "`2593/126`. The expectation does not know which array it was handed, which "
                  "is exactly what the derivation said."),
            ("p", "Beside those exact rows the lab prints a mean over seeds, and that one is a "
                  "sample. 120 seeds on the killer array at nine keys average `20.6583`, which "
                  "is `0.0790` above the expectation. Move the first seed and the row moves; "
                  "nothing above it does. The gap is sampling, and the honest description of "
                  "it is &ldquo;120 of the 4 862 runs&rdquo;."),
            ("h3", "What the expectation assumes, and the array that breaks it"),
            ("p", "The derivation used distinct keys twice: once in the relabelling and once "
                  "in the claim that a comparison between a pivot and an element sends the "
                  "element to one side or the other. On an array of 24 equal keys, Lomuto "
                  "sends every key to the same side, the split is `0` and `n − 1` under every "
                  "seed, and the cost is 276 comparisons while `2(n+1)Hₙ − 4n` at 24 is "
                  "`92.7979`. The formula has not been beaten; it was never a claim about "
                  "that array. Sorting with many equal keys wants a three-way partition, "
                  "which this course does not cover."),
            ("p", "This is the pattern the rest of the path follows. An expectation over the "
                  "algorithm's own coins holds for every input; an expectation over a "
                  "distribution of inputs holds only while the distribution does. "
                  "&ldquo;Bucket Sort and Average-Case Claims&rdquo; is the second kind, put "
                  "beside this one on purpose."),
        ],
        "lab": ("sortkit", {
            "mode": "expected",
            "n": 9,
            "trials": 120,
            "input": "killer",
            "seed": 1,
            "panel_title": "Choose the size, the array and the seeds",
            "panel_intro": "`Hₙ` is evaluated exactly, so the expectation is a fraction rather "
                           "than a decimal that nearly agrees with one. The measured mean is a "
                           "fraction too, and the two can therefore be subtracted.",
        }),
        "steps_title": "Deriving an expectation you can check",
        "steps_intro": "The order below is the order the argument is usually got wrong in: naming the indicator last, and the event never.",
        "steps": [
            ("Name the indicator before the sum",
             "Decide exactly what `Xᵢⱼ` is `1` for. Here: the `i`-th and `j`-th smallest keys "
             "are compared at some point in the run. Not &ldquo;compared at this level&rdquo;, "
             "not &ldquo;in the same call&rdquo;. The event has to be something you can "
             "compute a probability for."),
            ("Find the event that decides it",
             "Ask what single random choice settles whether the indicator is `1`. Here it is "
             "which element of `zᵢ … zⱼ` is drawn as a pivot first, and once that is seen the "
             "probability is a count: two favourable out of `j − i + 1`."),
            ("Sum by linearity, and do not look for independence",
             "`E[ΣXᵢⱼ] = ΣE[Xᵢⱼ]` needs nothing from the indicators. Re-index the double sum "
             "by the distance `d = j − i` so that identical terms collect, and the harmonic "
             "number appears."),
            ("Evaluate exactly, then measure, then subtract",
             "Compute the closed form as a fraction, take a mean over seeds, and print the "
             "difference. If the difference shrinks as the seed count grows, that is sampling; "
             "if it does not, one of the two is wrong."),
            ("Change the array and check that only the sample moves",
             "This is the test of the whole claim. Switch the input from sorted to the "
             "median-of-three killer: the exact rows do not move and the measured mean does. "
             "If the exact rows moved, the derivation would have used a property of the "
             "input."),
        ],
        "worked": {
            "title": "Nine keys: the derivation, then the same number three ways",
            "intro": [
                "Set the length to 9, the array to the median-of-three killer, the seeds to "
                "120 and the first seed to 1. The array on screen is `1 9 4 8 2 3 5 7 6`, "
                "which is a permutation of `1 … 9` built to be bad for a deterministic rule "
                "and which is about to make no difference at all.",
            ],
            "lines": [
                "H₉  = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 + 1/8 + 1/9  =  7129/2520",
                "",
                "E[X] = 2(n+1)Hₙ − 4n",
                "     = 2 · 10 · 7129/2520 − 36",
                "     = 7129/126 − 4536/126",
                "     = 2593/126",
                "     = 20.5794…",
                "",
                "where the number comes from                exactly      as a decimal",
                "  2(n+1)Hₙ − 4n                            2593/126      20.5794",
                "  the recurrence, solved from the bottom    2593/126      20.5794",
                "  every pivot sequence on 1 9 4 8 2 3 5 7 6  2593/126      20.5794",
                "  the same, on 1 2 3 4 5 6 7 8 9            2593/126      20.5794",
                "  the same, on 9 8 7 6 5 4 3 2 1            2593/126      20.5794",
                "  mean over 120 seeds                            —        20.6583",
                "",
                "4 862 pivot sequences enumerated per array;  2n ln n = 39.55",
            ],
            "after": [
                "The first five rows are exact and the sixth is not, and the difference "
                "between those two situations is the lesson. Rows three to five are not "
                "samples either: each is an average over all 4 862 executions, weighted by "
                "probability, so each is a complete statement about every run of the algorithm "
                "on that array.",
                "The last row is `0.0790` above the expectation. That is what a sample of 120 "
                "out of 4 862 looks like. Drag the seed count to 300 and it lands at "
                "`20.5300`, now below &mdash; a running mean wandering toward a level line, "
                "which is what the plot draws.",
                "For a faded rehearsal, do the same derivation at `n = 8`. The supplied first "
                "move is `H₈ = 761/280`; work out `2 · 9 · 761/280 − 32` as a fraction, check "
                "it against the panel's first row at `n = 8`, and then say &mdash; before "
                "looking &mdash; what the enumeration row will show, and how many executions "
                "it will report.",
            ],
        },
        "quiz_title": "What an expectation is over",
        "quiz": [
            {"q": "What does &ldquo;randomised quicksort makes `2(n+1)Hₙ − 4n` comparisons in expectation&rdquo; mean?",
             "a": ["That the average over all arrays of `n` keys is `2(n+1)Hₙ − 4n`",
                   "That for every array of `n` distinct keys, the average over the algorithm's pivot choices is `2(n+1)Hₙ − 4n`",
                   "That most arrays cost about `2(n+1)Hₙ − 4n`",
                   "That the cost is `2(n+1)Hₙ − 4n` unless the input was chosen adversarially"],
             "c": 1,
             "why": "The probability space is the algorithm's pivot draws, and the array is "
                    "fixed and arbitrary. The lab makes this checkable: averaged over every "
                    "pivot sequence, a sorted array, a reversed array and the median-of-three "
                    "killer all cost `2593/126` at nine keys."},
            {"q": "Why is `P(zᵢ and zⱼ are compared) = 2/(j − i + 1)`?",
             "a": ["Because there are two orders in which the comparison could happen",
                   "Because of the `j − i + 1` keys from `zᵢ` to `zⱼ`, exactly two cause a comparison when drawn as pivot first, and each is equally likely to be first",
                   "Because each of the two keys is chosen as a pivot with probability `1/(j − i + 1)`, and the events are independent",
                   "Because they are compared in two of the `j − i + 1` partitions they both survive"],
             "c": 1,
             "why": "The first pivot drawn from that stretch settles the matter: `zᵢ` or `zⱼ` "
                    "gives the comparison, anything strictly between separates them for ever. "
                    "The third answer gets the right number from an independence claim that "
                    "is not needed and not true &mdash; the two events are mutually exclusive, "
                    "not independent."},
            {"q": "The mean over 120 seeds at nine keys was `20.6583` and the expectation is `20.5794`. What is the gap?",
             "a": ["Evidence that the closed form is wrong at small `n`",
                   "Sampling: 120 seeds are 120 of the 4 862 possible executions",
                   "Rounding, because `Hₙ` is a decimal",
                   "The cost of running on an adversarial array rather than a typical one"],
             "c": 1,
             "why": "`Hₙ` is computed as an exact rational, so nothing is rounded, and the "
                    "enumeration row shows the array makes no difference. Raise the seed count "
                    "to 300 and the mean crosses to `20.5300`, below the expectation &mdash; "
                    "which is what a sample does and what a bound would not."},
            {"q": "Averaged over every pivot sequence, a sorted array, a reversed array and the median-of-three killer at nine keys each cost `2593/126`. What does that establish?",
             "a": ["That those three arrays happen to be equally hard for quicksort",
                   "That the expected cost is a property of the algorithm and not of the array, exactly as the derivation says",
                   "That `2593/126` is the worst case at nine keys",
                   "That randomisation has removed quicksort's bad inputs"],
             "c": 1,
             "why": "It is not a coincidence about three arrays: the derivation never used any "
                    "property of the input, and the enumeration confirms it by computation. "
                    "The worst case is still `n(n − 1)/2`, which some pivot sequence achieves "
                    "on every array; what randomisation changed is that no <em>input</em> can "
                    "force it."},
        ],
        "mistakes": [
            ("Hearing “expected” as “on a typical input”",
             "It is the most common misreading of the result and it throws the result away. "
             "An average over inputs is a claim about a distribution of inputs and fails when "
             "the distribution does; this is an average over the algorithm's own coin flips "
             "and holds for each input separately. The lab's enumeration row is there to be "
             "pointed at: same fraction, five different arrays."),
            ("Looking for independence before applying linearity",
             "The indicators are dependent and it does not matter. `E[X + Y] = E[X] + E[Y]` "
             "requires nothing of `X` and `Y`; it is independence that would be needed for "
             "`E[XY] = E[X]E[Y]`, which this derivation never uses. Discrete Mathematics' "
             "&ldquo;Linearity of Expectation&rdquo; is the reference, and this is the "
             "application that makes the point."),
            ("Applying the formula to an array with ties",
             "`2(n+1)Hₙ − 4n` was derived for distinct keys. On 24 equal keys the lab "
             "measures 276 comparisons under every seed, against an expectation of `92.7979` "
             "&mdash; not a refutation but a reminder that the claim had a hypothesis. Move "
             "the seed slider on that array and watch the count refuse to move with it."),
        ],
        "standard": ("Finish when you can derive the expectation from the indicator and say what it is an expectation over.",
                     "You should be able to state the comparison criterion and prove it, get "
                     "`2/(j − i + 1)` by counting, collapse the double sum to "
                     "`2(n+1)Hₙ − 4n`, evaluate it as a fraction at a given `n`, and explain "
                     "why a mean over seeds differs from it."),
        "note": ("Quicksort's price for its speed is that it is neither stable nor "
                 "guaranteed. “Heapsort” takes the sort that gives up something different: "
                 "it is `Θ(n log n)` on every input and needs no extra "
                 "memory at all, and it pays for both with stability and with a constant "
                 "factor you can watch it spend."),
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "heapsort",
        "title": "Heapsort",
        "module": "Quicksort and heapsort",
        "one_line": "Run heapsort by hand on eight keys, counting sift-down comparisons, and name the two promises it breaks.",
        "summary": (
            "Build a max-heap in the array itself, then repeatedly swap the root to the end, "
            "shrink the heap by one and sift the new root down. The array is a heap and a "
            "sorted suffix at the same time, so no extra memory is needed at all, and the "
            "comparison count is `Θ(n log n)` on every input. What it gives up is stability "
            "and adaptivity, neither of which any complexity class was ever going to supply."
        ),
        "key": [
            "build a max-heap in place, bottom up                       Θ(n)",
            "n − 1 times:  swap a[1] with the last heap slot, shrink, sift down",
            "in place   Θ(1) extra memory        Θ(n log n) on every input",
            "not stable      not adaptive        and no complexity class implies either",
            "8 keys, one shuffle:  heapsort 26 comparisons, merge sort 17",
        ],
        "key_label": "The two halves of the algorithm, and the two promises it does not make",
        "concepts_intro": (
            "The heap itself was &ldquo;Priority Queues and Binary Heaps&rdquo;. What is new "
            "is the trick that makes the sort need no second array."
        ),
        "concepts": [
            ("The array holds the heap and the output at once",
             "Slots `1 … m` are the heap and slots `m+1 … n` are the finished suffix, in "
             "increasing order. Each round swaps the largest remaining key, which is at the "
               "root, into slot `m`, then decrements `m` and sifts the displaced key down "
               "through the smaller heap. Nothing is allocated, and the boundary between "
               "&ldquo;heap&rdquo; and &ldquo;sorted&rdquo; is a single index."),
            ("The bound holds on every input, which is also the bad news",
             "A sift-down through a heap of `m` elements costs at most `2⌊log₂ m⌋` "
             "comparisons, so the teardown is `Θ(n log n)` whatever the input was, and the "
             "build is `Θ(n)` by the argument of &ldquo;Building a Heap in Linear "
             "Time&rdquo;. No input is bad. Equally, no input is good: at 16 keys the lab "
             "measures 85 comparisons on already-increasing input, 80 on a shuffle and 72 on "
             "decreasing input. Already-sorted input was the dearest of the three."),
            ("Stability is not implied by the class, and heapsort has none",
             "The build alone moves keys across the whole array: slot `n` can end up at the "
             "root. So two equal keys can be swapped past each other before the sort proper "
             "begins, and the lab shows it on eight records with four distinct keys, where "
             "three pairs come out reversed. Merge sort shares heapsort's complexity class "
             "and is stable; the class was never the reason."),
        ],
        "read_title": "Build, then tear down, in the array itself",
        "read_intro": "The two phases and their counts, what the in-place trick costs, and the counterexample to stability.",
        "body": [
            ("def", ("Heapsort",
                     "<strong>Heapsort</strong> sorts `a[1..n]` in two phases. "
                     "<strong>Build</strong>: rearrange `a` into a max-heap in place, bottom "
                     "up. <strong>Teardown</strong>: for `m = n` down to `2`, swap `a[1]` "
                     "with `a[m]`, treat the heap as having `m − 1` elements, and sift the "
                     "new `a[1]` down until the heap property holds again.")),
            ("p", "The max-heap is the choice that makes the sort ascending. The root is the "
                  "largest remaining key, and the slot it is swapped into is the last slot "
                  "the heap still owns, so the largest key lands where the sorted array wants "
                  "it and is immediately outside the heap."),
            ("ol", [
                "Build the max-heap, bottom up, from the last internal node to the root.",
                "Swap `a[1]` with `a[m]`. The key now at `a[m]` is final.",
                "Shrink the heap to `m − 1` slots, so `a[m]` is no longer part of it.",
                "Sift `a[1]` down: compare it with its children, swap with the larger if the larger is bigger, and repeat.",
                "Repeat from step two until `m = 1`.",
            ]),
            ("example", ("Eight keys, counted",
                         "On `8 1 3 6 5 2 7 4` the build costs 8 comparisons and produces the "
                         "heap `8 6 7 4 5 2 3 1`. The seven rounds of teardown cost 18 more, "
                         "so heapsort spends 26 comparisons in all and performs 20 swaps. "
                         "Merge sort on the same eight keys spends 17, and `⌈log₂ 8!⌉ = 16` "
                         "comparisons are necessary for any comparison sort on any array of "
                         "eight. Every one of those three numbers was produced by running "
                         "something.")),
            ("p", "The build is the cheap half and it is the half readers expect to dominate. "
                  "At 16 keys the lab measures 22 comparisons for the build and 58 for the "
                  "teardown, out of 80. The asymmetry is structural: the build's cost is "
                  "dominated by the many nodes near the bottom, which sift down almost no "
                  "distance, while every round of the teardown drops a key from the root and "
                  "usually carries it most of the way back down."),
            ("h3", "The two promises heapsort does not make"),
            ("p", "It is not adaptive. The comparison counts at 16 keys are 85 for increasing "
                  "input, 80 for a shuffle, 72 for decreasing input: not only is sorted input "
                  "no cheaper, it is the most expensive of the three, because an ascending "
                  "array is the worst possible starting shape for a max-heap build and every "
                  "key has to travel. A reader who expects &ldquo;nearly sorted input is "
                  "cheaper&rdquo; is expecting a property insertion sort has and this "
                  "algorithm does not."),
            ("p", "It is not stable. The lab's tie test builds eight records with four "
                  "distinct keys, `1#1 2#2 3#3 4#4 1#5 2#6 3#7 4#8`, and heapsort returns "
                  "`1#5 1#1 2#6 2#2 3#3 3#7 4#8 4#4`. Three pairs of equal keys come out "
                  "reversed. One would have been enough."),
            ("p", "What it does promise is worth being clear about, because it is the reason "
                  "the algorithm is used. `Θ(1)` extra memory, and a `Θ(n log n)` worst case "
                  "with no bad input and no randomness &mdash; which is exactly what "
                  "quicksort cannot offer and merge sort can only offer at the cost of a "
                  "second array. When memory is the binding constraint and a guarantee is "
                  "wanted, this is the sort."),
            ("p", "The cost of those two promises is a constant factor, and the lab prints it "
                  "as a ratio. At 16 keys heapsort spends 80 comparisons against merge sort's "
                  "48 on the same array: both are `Θ(n log n)` and heapsort's constant is "
                  "larger, chiefly because a sift-down compares the key with both children at "
                  "every level. That same factor of about two reappears in "
                  "&ldquo;k-Way Merging and Sorting in Practice&rdquo;, where a heap merges "
                  "`k` runs and pays for it in exactly the same way."),
            ("p", "Two figures on this page are measurements of one array each &mdash; 26 at "
                  "eight keys, 80 at sixteen &mdash; and one is a proof: `⌈log₂ n!⌉`, which "
                  "no comparison sort can go under on any array. At 16 keys that is 45, and "
                  "merge sort's 48 and heapsort's 80 both sit above it. The gap between 45 "
                  "and 80 is not slack in the bound; it is the price of the two promises."),
        ],
        "lab": ("heap", {
            "mode": "heapsort",
            "preset": "shuffled",
            "panel_title": "Sort in place and count what it cost",
            "panel_intro": "Heapsort builds a max-heap, then repeatedly swaps the root to the "
                           "end and sifts down: no extra memory at all. Merge sort's "
                           "comparison total beside it comes from running merge sort on the "
                           "very same array, so the two columns are two counts of one input "
                           "rather than two claims about a complexity class.",
        }),
        "steps_title": "Running heapsort on paper",
        "steps_intro": "Draw the array once and keep two marks on it: where the heap ends, and where the sorted suffix begins.",
        "steps": [
            ("Build bottom up, and count as you go",
             "Start at the last internal node, `⌊n/2⌋`, and work back to the root, sifting "
             "each down. Count one comparison per pair of children examined plus one against "
             "the parent. On eight keys this is 8 comparisons; check yours against the lab's "
             "build column."),
            ("Swap the root out and shrink",
             "Exchange `a[1]` with the last slot the heap owns. Write the boundary down. That "
             "key is final and will not be looked at again &mdash; which is the whole reason "
             "no second array is needed."),
            ("Sift the new root down, comparing both children",
             "At each level compare the two children with each other, then the larger with "
             "the parent. Stop when the parent wins or the node has no children. The number "
             "of levels it travels is what varies between rounds; the maximum is "
             "`⌊log₂ m⌋`."),
            ("Read the ratio, not just the total",
             "Put heapsort's count beside merge sort's on the same array and beside "
             "`⌈log₂ n!⌉`. Both sorts are above the bound and heapsort is above merge sort; "
             "the question that has an answer here is how big the constant is, not which sort "
             "is faster."),
            ("Change the arrival order and watch the count refuse to improve",
             "Run increasing, decreasing and shuffled at the same length. If sorted input "
             "came out cheapest you would have found an adaptive algorithm; it comes out "
             "dearest, and that is the promise heapsort does not make."),
        ],
        "worked": {
            "title": "Eight keys by hand, with the comparison count",
            "intro": [
                "Move the keys slider to 8 and leave the arrival order on the fixed shuffle. "
                "The array is `8 1 3 6 5 2 7 4`. The build is written out as four sift-downs; "
                "the teardown is written as the array after each round, which is what the "
                "lab's upper stage draws.",
            ],
            "lines": [
                "input        8  1  3  6  5  2  7  4",
                "",
                "BUILD, bottom up from node 4",
                "  node 4 (6):  child 4 … 6 wins, no swap",
                "  node 3 (3):  children 2 and 7 … 7 wins, 7 > 3, swap",
                "               8  1  7  6  5  2  3  4",
                "  node 2 (1):  children 6 and 5 … 6 wins, 6 > 1, swap; then 1 sifts to 4",
                "               8  6  7  4  5  2  3  1",
                "  node 1 (8):  children 6 and 7 … 7 wins, 8 > 7, stop",
                "  max-heap     8  6  7  4  5  2  3  1        build cost 8 comparisons",
                "",
                "TEARDOWN, seven rounds, sorted suffix in the tail",
                "  place 8      7  6  3  4  5  2  1 | 8",
                "  place 7      6  5  3  4  1  2 | 7  8",
                "  place 6      5  4  3  2  1 | 6  7  8",
                "  place 5      4  2  3  1 | 5  6  7  8",
                "  place 4      3  2  1 | 4  5  6  7  8",
                "  place 3      2  1 | 3  4  5  6  7  8",
                "  place 2      1 | 2  3  4  5  6  7  8",
                "",
                "heapsort      26 comparisons, 20 swaps, 0 extra slots",
                "merge sort    17 comparisons on the same array, and Θ(n) extra slots",
                "⌈log₂ 8!⌉     16 comparisons, necessary for every comparison sort",
            ],
            "after": [
                "Two things in that trace are worth pausing on. The build made 8 comparisons "
                "and the teardown 18, so the phase that sounds expensive is the cheap one. "
                "And the sorted suffix grows from the right while the heap shrinks from the "
                "same boundary, which is why the extra memory is a single index.",
                "The comparison totals are not a verdict about speed. Merge sort made fewer "
                "comparisons on this array and needs `Θ(n)` more memory to do it; the bound "
                "of 16 says neither of them is doing anything impossible. What heapsort "
                "bought with its 26 is a guarantee that holds on every array of eight keys "
                "and a memory footprint of zero.",
                "For a faded rehearsal, set the arrival order to already increasing at the "
                "same length. The supplied first move is a prediction: the build has more "
                "work to do, not less, because an ascending array is the worst possible shape "
                "for a max-heap. Count the build's comparisons by hand before you read them "
                "off, then compare the total with the 26 above.",
            ],
        },
        "quiz_title": "In place, and what that cost",
        "quiz": [
            {"q": "Heapsort and merge sort are both `Θ(n log n)`. Is heapsort stable?",
             "a": ["Yes, because the complexity class is the same as merge sort's",
                   "No: the lab's tie test returns three pairs of equal keys reversed",
                   "Yes, if the heap is built top down instead of bottom up",
                   "Only when all the keys are distinct"],
             "c": 1,
             "why": "The class says nothing about equal keys, and heapsort moves keys across "
                    "the whole array from the first phase onward. The last answer is a "
                    "category error: with distinct keys there is nothing for stability to be "
                    "about."},
            {"q": "How much memory does heapsort need beyond the array it is given?",
             "a": ["`Θ(n)`, for the heap",
                   "`Θ(log n)`, for the recursion",
                   "`Θ(1)`: the heap is the array, and the boundary is one index",
                   "`Θ(n)` for the build and `Θ(1)` for the teardown"],
             "c": 2,
             "why": "The heap occupies the front of the same array and the sorted output the "
                    "back, so the only extra state is the index between them. A sift-down "
                    "written iteratively needs no stack, which is why the `Θ(log n)` answer is "
                    "wrong for heapsort even though it is right for quicksort."},
            {"q": "At 16 keys the lab measures 85 comparisons on already-increasing input and 72 on decreasing input. What does that say?",
             "a": ["That heapsort is adaptive, but in reverse",
                   "That heapsort is not adaptive: sorted input is not cheaper, and here it is the dearest of the three orders",
                   "That the build dominates the count",
                   "That the two counts ought to be equal and one of them is a measurement error"],
             "c": 1,
             "why": "Adaptive means nearly-sorted input costs less, and it does not: an "
                    "ascending array is the worst starting shape for a max-heap build. The "
                    "difference between 85 and 72 is real and measured, and it is 13 "
                    "comparisons out of about 80 &mdash; a constant-factor wobble, not a "
                    "change of class."},
            {"q": "Heapsort spent 80 comparisons where merge sort spent 48 on the same 16 keys. What is the honest reading?",
             "a": ["Merge sort is asymptotically faster than heapsort",
                   "Both are `Θ(n log n)`; heapsort pays a larger constant and buys `Θ(1)` memory with it",
                   "Heapsort's `Θ(n log n)` bound must be wrong",
                   "48 is below `⌈log₂ 16!⌉`, so the merge sort count is impossible"],
             "c": 1,
             "why": "A sift-down compares the key with both children at every level, which is "
                    "roughly the factor of two you can see. `⌈log₂ 16!⌉ = 45`, so 48 is above "
                    "the bound and perfectly possible. And a comparison count is not a time: "
                    "which sort is faster is a question these labs do not measure."},
        ],
        "mistakes": [
            ("Inferring stability, or adaptivity, from `Θ(n log n)`",
             "The class bounds the growth of a comparison count and says nothing else. "
             "Heapsort and merge sort share it and agree about nothing else that matters: one "
             "is stable, the other is in place, neither is adaptive. If a situation needs a "
             "promise, the promise has to come from the algorithm's structure."),
            ("Expecting the build to be the expensive phase",
             "It is the cheap one. At 16 keys the build costs 22 comparisons and the teardown "
             "58. Most nodes in a heap are near the bottom and sift down almost no distance, "
             "which is the linear-time build argument; every teardown round, by contrast, "
             "starts at the root and usually travels the full height."),
            ("Reading “in place” as “no memory” or as “no movement”",
             "In place means `Θ(1)` extra memory, not that nothing moves: heapsort performs 20 "
             "swaps on eight keys, which is more movement than merge sort's, and all that "
             "movement is what costs it stability. The promise is about space, and it is the "
             "only promise of the four that heapsort makes outright."),
        ],
        "standard": ("Finish when you can run heapsort on eight keys, count its comparisons, and name what it gave up.",
                     "You should be able to build a max-heap bottom up by hand, carry out the "
                     "teardown with the boundary marked, count build and teardown separately, "
                     "and say which two of the four promises heapsort breaks and why no "
                     "complexity class was going to decide either."),
        "note": ("Every sort so far has been a comparison sort, so every one of them is under "
                 "`⌈log₂ n!⌉`. The next three lessons leave that world. If the keys are "
                 "integers in a known range they can be used as addresses instead of being "
                 "compared, and &ldquo;Counting Sort&rdquo; is the first of those &mdash; not "
                 "a sort that beats the bound, but one the bound does not describe."),
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "counting-sort",
        "title": "Counting Sort",
        "module": "Not comparing at all",
        "one_line": "Sort integer keys with a tally and a prefix sum, and say when the range makes it worse than a comparison sort.",
        "summary": (
            "If the keys are integers in `0 … k−1`, they can be used as indices instead of "
            "being compared: tally them, turn the tally into a prefix sum, and place each "
            "record into the slot its prefix sum names. The cost is `Θ(n + k)`, which is not "
            "a contradiction of the comparison lower bound because no two keys are ever "
            "compared. The placement pass runs from the back, and that direction is the whole "
            "of the algorithm's stability."
        ),
        "key": [
            "tally[key] += 1                        one pass over the n keys",
            "prefix[i] = prefix[i−1] + tally[i]     one pass over the k counters",
            "for each record from the BACK:  out[--prefix[key]] = record",
            "work = n + k        12 keys with k = 5:            17",
            "                    12 keys with a 32-bit key:  4 294 967 308",
        ],
        "key_label": "Three passes, and the second term of the cost",
        "concepts_intro": (
            "The hard idea is what the comparison lower bound is a bound on, which is a "
            "question about a model rather than about an algorithm."
        ),
        "concepts": [
            ("Nothing is compared, so the bound does not apply",
             "`⌈log₂ n!⌉` is a lower bound for algorithms whose only access to the keys is a "
             "comparison, and it is proved by counting the leaves a decision tree needs. "
             "Counting sort never asks whether one key is at most another: it uses a key as "
             "an array index. So it is outside the theorem's hypothesis, not a "
             "counterexample to its conclusion. On 12 keys the bound is 29 comparisons and "
             "counting sort makes none, which settles nothing about the bound and everything "
             "about the model."),
            ("The prefix sum says where each run of equal keys ends",
             "After tallying, `prefix[i]` is the number of keys at most `i`, so it is exactly "
             "the last output slot that key `i` may occupy, counting from one. On the lab's "
             "keys the tally is `1 2 2 3 4` and the prefix sums are `1 3 5 8 12`: the four "
             "records with key `4` own slots nine to twelve, and `prefix[4] = 12` names the "
             "last of them. That is why the placement pass counts down."),
            ("The placement direction is the stability",
             "Walk the input from the back and write each record into `prefix[key]`, "
             "decrementing as you go. The last record with a given key takes the last slot, "
             "the one before it takes the one before, and input order survives. Walk forward "
             "with the same bookkeeping and every run comes out reversed: the lab measures 11 "
             "reordered pairs on the same 12 keys. The algorithm is otherwise identical, "
             "which is what makes the direction worth a sentence in every description of it."),
        ],
        "read_title": "A tally, a prefix sum, and a placement pass with a direction",
        "read_intro": "The three passes, where the stability lives, and the term that decides whether this algorithm is worth using.",
        "body": [
            ("def", ("Counting sort",
                     "<strong>Counting sort</strong> sorts `n` records whose keys are integers "
                     "in `0 … k−1`. Tally the keys into an array of `k` counters. Replace the "
                     "tally with its running totals, so that counter `i` holds the number of "
                     "keys at most `i`. Then pass over the input from back to front, writing "
                     "each record into the output slot its counter names and decrementing "
                     "that counter.")),
            ("ol", [
                "Tally: `k` counters zeroed, then one increment per record. Cost `Θ(n + k)`.",
                "Prefix: one pass over the counters, replacing each with the running total. Cost `Θ(k)`.",
                "Place: one pass over the records, back to front, one write each. Cost `Θ(n)`.",
            ]),
            ("example", ("Twelve keys in the range zero to four",
                         "The keys are `4 1 3 4 3 0 2 4 1 3 4 2`. The tally is "
                         "`1 2 2 3 4` &mdash; one zero, two ones, two twos, three threes, "
                         "four fours &mdash; and the prefix sums are `1 3 5 8 12`. Placing "
                         "from the back gives `0 1 1 2 2 3 3 3 4 4 4 4` with the tags inside "
                         "each run still ascending. The work is `n + k = 17`.")),
            ("p", "No branch in that procedure looked at two keys together. The comparison "
                  "bound is silent, and the cost is the sum of two terms that have nothing to "
                  "do with each other: `n`, the number of records, and `k`, the width of the "
                  "declared key range."),
            ("h3", "The second term is the whole question"),
            ("p", "`Θ(n + k)` is called linear and is linear in `n + k`, which is not the same "
                  "thing as linear in `n`. At 12 keys over a range of five, the work is 17 "
                  "against `n log₂ n ≈ 43`, and counting sort wins comfortably. Declare a "
                  "16-bit key and the work is `12 + 65 536`. Declare a 32-bit key and it is "
                  "`4 294 967 308`, and the counter array alone is four billion slots of "
                  "memory for twelve records."),
            ("p", "So the algorithm is chosen by a comparison of terms, not by a class. It is "
                  "the right sort when `k` is `O(n)` or thereabouts: ages, bytes, digits, "
                  "bucket indices, grades. It is the wrong sort when `k` is `n²`, or a machine "
                  "word, or unknown. The lab's range control only changes the second term, "
                  "which is the term that decides."),
            ("thm", ("Backward placement is stable",
                     "If the placement pass visits the records from last to first, writing "
                     "each into slot `prefix[key]` and then decrementing that counter, then "
                     "records with equal keys appear in the output in the same relative order "
                     "as in the input.")),
            ("proof", ("Fix a key value `v`, and let the records with that key be, in input "
                       "order, `r₁, r₂, …, r_t`. Before any of them is placed, `prefix[v]` is "
                       "the number of keys at most `v`, which is the last slot the run owns.",
                       "The pass visits them in the order `r_t, r_{t−1}, …, r₁`, and each visit "
                       "takes the current value of `prefix[v]` and then decreases it by one. So "
                       "`r_t` gets the last slot of the run, `r_{t−1}` the one before, and `r₁` "
                       "the first. The output order is `r₁, …, r_t`, which is the input order.",
                       "The same argument with the pass running forwards hands `r₁` the last "
                       "slot and `r_t` the first, reversing the run &mdash; which is not a bug "
                       "in the bookkeeping but the same bookkeeping read the other way.")),
            ("p", "The lab runs both directions on the same keys and flags the reordered "
                  "pairs: zero from the back, eleven from the front. The output is sorted "
                  "either way. Only the order inside each run of equal keys differs, and that "
                  "is precisely what radix sort needs, since it is `d` of these "
                  "passes stacked and its correctness argument is nothing but their "
                  "stability."),
            ("p", "One more property is worth naming: counting sort is not in place. It needs "
                  "`n` output slots and `k` counters, so it trades memory for the comparison "
                  "it does not make. Heapsort was the other trade in the same two "
                  "dimensions, and neither trade is implied by anything about `Θ`."),
        ],
        "lab": ("sortkit", {
            "mode": "counting",
            "keys": "4, 1, 3, 4, 3, 0, 2, 4, 1, 3, 4, 2",
            "range": "0",
            "direction": "backward",
            "panel_title": "Choose the keys, the declared range and the pass",
            "panel_intro": "The tally and the prefix sums are computed from the keys you type. "
                           "The declared range only changes the second term of `n + k`, which "
                           "is the term that decides whether this algorithm is worth using.",
        }),
        "steps_title": "Running counting sort, and sizing it first",
        "steps_intro": "The sizing question comes first, because it is the one that can rule the algorithm out.",
        "steps": [
            ("Write down k before anything else",
             "Not the largest key present: the width of the range the keys are drawn from, "
             "which is what the counter array has to cover. If `k` is much larger than "
             "`n log n`, stop here and use a comparison sort. This is the step the "
             "misconception skips."),
            ("Tally, and check the total",
             "One counter per value in the range, one increment per record. The counters must "
             "sum to `n`; if they do not, a key was outside the range you declared and the "
             "algorithm has no defined behaviour for it."),
            ("Turn the tally into a prefix sum, and read it as slots",
             "After the running totals, counter `i` is the number of keys at most `i`, which "
             "is the last output slot key `i` may occupy. Say that sentence out loud before "
             "placing anything; it is what makes the next step obvious rather than magic."),
            ("Place from the back, decrementing",
             "Visit the input from last record to first. Write each into slot `prefix[key]`, "
             "then decrement that counter. Going forwards with the same counters also sorts, "
             "and reverses every run of equal keys, so the direction is not a matter of "
             "taste."),
            ("State the cost as two terms and compare them",
             "`n + k`, with both terms named. Put it beside `n log₂ n` at your `n`, and beside "
               "the `⌈log₂ n!⌉` the panel prints &mdash; remembering that the last of those is "
               "a number of comparisons and counting sort makes none, so it is a bound this "
               "algorithm is outside rather than one it beats."),
        ],
        "worked": {
            "title": "Twelve keys placed from the back, one record at a time",
            "intro": [
                "The keys are the lab's, tagged by input position so that stability is "
                "visible: `4#1 1#2 3#3 4#4 3#5 0#6 2#7 4#8 1#9 3#10 4#11 2#12`. The range is "
                "just wide enough for the keys, so `k = 5` and the counters cover `0 … 4`.",
            ],
            "lines": [
                "keys          4  1  3  4  3  0  2  4  1  3  4  2",
                "tags         #1 #2 #3 #4 #5 #6 #7 #8 #9 #10 #11 #12",
                "",
                "tally         key 0 1 2 3 4",
                "              cnt 1 2 2 3 4        sums to 12 = n",
                "prefix        key 0 1 2 3 4",
                "              cum 1 3 5 8 12       prefix[i] = how many keys are ≤ i",
                "",
                "placement, from the LAST record to the first",
                "  #12 key 2 → slot 5    prefix[2] 5 → 4",
                "  #11 key 4 → slot 12   prefix[4] 12 → 11",
                "  #10 key 3 → slot 8    prefix[3] 8 → 7",
                "   #9 key 1 → slot 3    prefix[1] 3 → 2",
                "   #8 key 4 → slot 11   prefix[4] 11 → 10",
                "   #7 key 2 → slot 4    prefix[2] 4 → 3",
                "   #6 key 0 → slot 1    prefix[0] 1 → 0",
                "   #5 key 3 → slot 7    prefix[3] 7 → 6",
                "   #4 key 4 → slot 10   prefix[4] 10 → 9",
                "   #3 key 3 → slot 6    prefix[3] 6 → 5",
                "   #2 key 1 → slot 2    prefix[1] 2 → 1",
                "   #1 key 4 → slot 9    prefix[4] 9 → 8",
                "",
                "output       0#6 1#2 1#9 2#7 2#12 3#3 3#5 3#10 4#1 4#4 4#8 4#11",
                "work         n + k = 12 + 5 = 17,  and not one comparison between two keys",
            ],
            "after": [
                "Follow the four records with key `4`. They were placed in the order "
                "`#11, #8, #4, #1` into slots `12, 11, 10, 9`, and they come out reading "
                "`#1, #4, #8, #11`. The pass ran backwards and the run came out forwards, "
                "which is the whole of the stability argument written in one line of "
                "bookkeeping.",
                "Now switch the placement control to front to back and watch the same twelve "
                "records come out `0#6 1#9 1#2 2#12 2#7 3#10 3#5 3#3 4#11 4#8 4#4 4#1`: still "
                "sorted by key, with every run reversed and eleven pairs flagged. The lab "
                "counts those pairs rather than asserting the property.",
                "For a faded rehearsal, change the declared range to a byte, `k = 256`, "
                "without changing the keys. The supplied first move is the arithmetic: the "
                "work becomes `12 + 256 = 268`, against `n log₂ n ≈ 43`. Say which algorithm "
                "you would now choose for twelve records, and then find the smallest `n` at "
                "which counting sort over a byte range wins again.",
            ],
        },
        "quiz_title": "Linear in what",
        "quiz": [
            {"q": "Counting sort is `Θ(n + k)`. Is it linear?",
             "a": ["Yes, always",
                   "Linear in `n + k`, which is linear in `n` only when `k` is `O(n)`",
                   "No: `k` is always larger than `n`",
                   "Yes, because `k` is a constant once the key type is fixed"],
             "c": 1,
             "why": "Both terms are real. Twelve keys over a range of five cost 17 units; the "
                    "same twelve keys with a 32-bit key declared cost `4 294 967 308`, and the "
                    "counter array is four billion slots. Calling `k` a constant because the "
                    "key type is fixed is the same claim with the number hidden."},
            {"q": "Does counting sort contradict the `⌈log₂ n!⌉` comparison lower bound?",
             "a": ["Yes: it sorts 12 keys in 17 units where the bound says 29 comparisons are needed",
                   "No: the bound is about algorithms whose only access to the keys is a comparison, and this one never compares two keys",
                   "No, because `n + k` is never smaller than `⌈log₂ n!⌉`",
                   "Yes, but only when `k` is smaller than `n`"],
             "c": 1,
             "why": "The bound is proved about a model &mdash; a decision tree whose internal "
                    "nodes are comparisons &mdash; and counting sort is not in that model, so "
                    "the theorem's hypothesis fails and its conclusion says nothing here. The "
                    "third answer is also false as arithmetic: 17 is less than 29."},
            {"q": "What breaks if the placement pass runs front to back with the same prefix array?",
             "a": ["The output is not sorted",
                   "The output is sorted, but every run of equal keys comes out reversed",
                   "The prefix sums come out wrong",
                   "The work rises to `n log n`"],
             "c": 1,
             "why": "Each counter still names the run's last unused slot, so the keys land in "
                    "the right runs; what changes is which record gets the last slot. The lab "
                    "measures eleven reordered pairs on the same twelve keys, with identical "
                    "tallies, prefix sums and work."},
            {"q": "Twelve records with a declared key range of 65 536. What is the work?",
             "a": ["12", "17", "65 548", "786 432"],
             "c": 2,
             "why": "`n + k = 12 + 65 536`. The tally and prefix passes both walk the whole "
                    "declared range whether or not any key lands in it, which is also "
                    "`65 536` counters of memory for twelve records. `786 432` is `n × k`, "
                    "which no pass of this algorithm performs."},
        ],
        "mistakes": [
            ("Calling counting sort linear without naming `k`",
             "&ldquo;Linear&rdquo; on its own hides the term that decides. Write the cost as "
             "`n + k` with both numbers filled in, and the algorithm selects itself: 17 for "
             "twelve keys over a range of five, `4 294 967 308` for the same twelve keys over "
             "a 32-bit range. The second is not a slow sort; it is not a sort you can run."),
            ("Taking the largest key present as `k`",
             "The counter array has to cover the range the keys are <em>drawn from</em>, "
             "because a key outside it has nowhere to be tallied. If the keys are 32-bit "
             "integers that happen to be small today, `k` is still `2³²` unless something "
             "guarantees otherwise. The lab separates the two ideas by letting you declare a "
             "range wider than the keys you typed."),
            ("Expecting stability to come for free",
             "Nothing about tallying and prefix summing is stable or unstable; the placement "
             "direction decides, and the forward direction is exactly as short to write. Any "
             "description of counting sort that does not say which way the placement pass "
               "runs has left out the only line where stability lives &mdash; and radix "
               "sort is built entirely on that line."),
        ],
        "standard": ("Finish when you can size counting sort before running it, and say where its stability lives.",
                     "You should be able to tally and prefix-sum twelve keys by hand, place "
                     "them from the back with the counters decrementing, state the cost as two "
                     "named terms, and explain why making no comparisons puts this algorithm "
                     "outside the comparison bound rather than above it."),
        "note": ("Counting sort needs `k` counters, which rules it out for wide keys. Split a "
                 "wide key into digits and the range per pass becomes the base rather than "
                 "the key's whole domain &mdash; and then the passes have to be composed, "
                 "which is a question about stability. That is &ldquo;Radix Sort&rdquo;, and "
                 "the stability proved above is the only thing its correctness rests on."),
    },
]
