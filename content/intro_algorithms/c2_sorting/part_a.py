"""Sorting and Order Statistics, lessons 1-5 -- Chapters 6, 7 and 8.1-8.2.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed.
(MIT Press, 2009): Chapter 6, Heapsort (pp. 151-169); Chapter 7, Quicksort
(pp. 170-190); Chapter 8, Sorting in Linear Time, sections 8.1-8.2
(pp. 191-197). Every quotation is copied from the operator's copy with its
printed page in the comment beside the lesson. The arrays are written for
these lessons: none of the book's figures, examples or exercises is
reproduced, and its procedures are described in prose and named.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # CLRS Chapter 6 opening and sections 6.1-6.3, pp. 151-159.
    # Quote: p. 157, 9 words, quotes.py OK. Lesson total: 9 words.
    # Heapsort's two inherited virtues (p. 151); array view, PARENT/LEFT/
    # RIGHT, heap-size (pp. 151-152); max- and min-heap property, height
    # (pp. 152-153); MAX-HEAPIFY and T(n) <= T(2n/3) + Theta(1) (pp. 154-156);
    # BUILD-MAX-HEAP, its invariant, the loose and the tight bound
    # (pp. 156-159).
    {
        "slug": "heaps",
        "title": "Heaps and Building a Heap",
        "module": "Chapter 6 · Heapsort",
        "one_line": "A heap is a nearly complete binary tree stored in an array with every parent at least as large as its children, and the whole array can be made into one in linear time.",
        "summary": (
            "Sections 6.1 to 6.3 define the binary heap, give the procedure that restores the "
            "heap property below one node, and build a heap from an unordered array by calling "
            "it from the last internal node back to the root. The obvious bound on the build is "
            "n lg n; the book shows it is linear by counting nodes at each height. Build a heap "
            "by hand, then evaluate the sum over heights exactly in the lab and set the "
            "exchanges actually made beside it."
        ),
        "key": [
            "parent of i is ⌊i/2⌋; children 2i, 2i + 1",
            "max-heap: no node larger than its parent",
            "MAX-HEAPIFY costs O(h) at height h",
            "build from ⌊n/2⌋ down to the root",
            "most nodes are low, so the build is O(n)",
        ],
        "key_label": "Sections 6.1 to 6.3 in five lines",
        "concepts_intro": (
            "Three ideas carry the first half of the chapter. The rest of Part II, and the "
            "priority queues of later chapters, take them for granted."
        ),
        "concepts": [
            ("The array as a tree",
             "A heap is an array `A[1..n]` read as a nearly complete binary tree: every level "
             "full except perhaps the lowest, which fills from the left. Node `i` has its "
             "parent at `⌊i/2⌋` and its children at `2i` and `2i + 1`, so no pointers are "
             "stored at all."),
            ("The heap property",
             "In a max-heap every node other than the root holds a value no larger than its "
             "parent's, so the largest value sits at the root. A min-heap reverses the "
             "inequality. The property relates parents to children only; it says nothing about "
             "the order of two siblings."),
            ("The height of a node",
             "The number of edges on the longest path that leads from the node down to a leaf. "
             "Leaves have height 0 and the root has height `⌊lg n⌋`. The chapter's procedures "
             "cost time proportional to the height of the node they start at, which is why "
             "heights, and how many nodes have each, carry the analysis."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the chapter opening and sections 6.1 to 6.3 in your own copy first. The lesson "
            "sets out the argument in its own words, builds one heap by hand, and then evaluates "
            "the bound on the build beside the exchanges a real build makes."
        ),
        "body": [
            ("p", "&ldquo;This upper bound, though correct, is not asymptotically "
                  "tight.&rdquo; The authors say it in Section 6.3 of the obvious price of "
                  "building a heap, and the rest of that section is the counting argument that "
                  "replaces it. This lesson reads the opening of Chapter 6 and sections 6.1 to "
                  "6.3: what a heap is, how its defining property is restored below one node, "
                  "and why turning a whole array into a heap costs only linear time."),
            ("p", "The chapter opens by placing heapsort among the sorts of Part I. Like merge "
                  "sort it runs in `O(n lg n)` time; like insertion sort it sorts in place, "
                  "keeping only a constant number of elements outside the input array at any "
                  "moment. It also introduces a new design technique: let a data structure "
                  "manage the information an algorithm needs. The structure is the heap, and the "
                  "authors note that it reappears as a priority queue later in the book. They "
                  "also set aside the other meaning of the word, garbage-collected storage, "
                  "which has nothing to do with this one."),
            ("def", ("Binary heap",
                     "An array `A` with a length and a heap-size, where only `A[1..heap-size]` "
                     "belongs to the heap. The root is `A[1]`; node `i` has parent `⌊i/2⌋`, "
                     "left child `2i` and right child `2i + 1`, each computable with a shift. "
                     "A <strong>max-heap</strong> satisfies `A[⌊i/2⌋] ≥ A[i]` for every node "
                     "other than the root.")),
            ("p", "Section 6.1 adds two facts the analysis will need, both left to exercises. "
                  "An n-element heap has height `⌊lg n⌋` (Exercise 6.1-2), because the tree is "
                  "nearly complete. And in the array layout the leaves are exactly the nodes "
                  "`⌊n/2⌋ + 1` to `n` (Exercise 6.1-7): the second half of the array has no "
                  "children. Heapsort uses max-heaps; the min-heap, with the inequality "
                  "reversed, is the one priority queues usually use."),
            ("p", "Section 6.2 gives MAX-HEAPIFY, the procedure everything else is built on. "
                  "It is called on a node whose two subtrees are already max-heaps but whose own "
                  "value may be smaller than a child's. It finds the largest of the node and its "
                  "two children; if that is a child, it exchanges the two values and continues "
                  "from the child's position, because the smaller value may now break the "
                  "property one level down. The value sinks until it is at least as large as "
                  "both children or reaches a leaf. Each level costs a constant, and a child's "
                  "subtree holds at most `2n/3` of the nodes, which happens when the bottom "
                  "level is exactly half full; the recurrence `T(n) ≤ T(2n/3) + Θ(1)` gives "
                  "`O(lg n)` by the master theorem, or `O(h)` on a node of height h."),
            ("p", "Section 6.3 builds a heap from an arbitrary array. The leaves are one-element "
                  "heaps already, so BUILD-MAX-HEAP calls MAX-HEAPIFY on the internal nodes "
                  "only, from `⌊n/2⌋` down to 1. The order is the correctness argument, and the "
                  "authors give it as a loop invariant: before every iteration, every "
                  "node numbered above i is the root of a max-heap. It holds at the start "
                  "because those nodes are leaves; it is maintained because i's children are "
                  "numbered above i, so they are heap roots and MAX-HEAPIFY's precondition is "
                  "met; and when i reaches 0 it says node 1 is the root of a max-heap."),
            ("thm", ("The build is linear",
                     "An n-element heap has at most `⌈n/2ʰ⁺¹⌉` nodes of height h, and "
                     "MAX-HEAPIFY at height h costs `O(h)`. So BUILD-MAX-HEAP costs at most "
                     "the sum of `⌈n/2ʰ⁺¹⌉ · O(h)` over h from 0 to `⌊lg n⌋`, which is "
                     "`O(n · Σ h/2ʰ)`, and the infinite series `Σ h/2ʰ` converges to 2 "
                     "(Appendix A). The build is `O(n)`.")),
            ("p", "The loose bound charged every one of the roughly n/2 calls the height of "
                  "the whole tree. The tight one charges each call the height of its own node, "
                  "and the point of the theorem is how few nodes are high: half the nodes are "
                  "leaves and cost nothing, a quarter sit at height 1, an eighth at height 2, and "
                  "only the root is at height `⌊lg n⌋`. The node count halves at each level "
                  "while the cost per node grows by one, and a halving beats an increment."),
            ("math", [
                "the sum at n = 20, height ⌊lg 20⌋ = 4",
                "",
                "h    nodes, at most ⌈20/2ʰ⁺¹⌉    h · nodes",
                "0          10                    0",
                "1           5                    5",
                "2           3                    6",
                "3           2                    6",
                "4           1                    4",
                "                                ---",
                "                                 21      against n·⌊lg n⌋ = 80",
            ]),
            ("p", "Now the lab, which runs the build and counts. It is the heap lab of the "
                  "Algorithms Subject's lesson Building a Heap in Linear Time, where the same "
                  "build is practised further, and it builds a <em>min</em>-heap: the mirror "
                  "image of BUILD-MAX-HEAP, with every comparison reversed (Exercise 6.2-2 asks "
                  "for that procedure), so every count the book makes for one is the count for "
                  "the other. The keys are 1 to n in the arrival order you choose. The tiles are "
                  "the sum in the table, evaluated exactly; the swaps made sifting down from the "
                  "last internal node, which is BUILD-MAX-HEAP's method; the swaps made by "
                  "inserting the keys one at a time instead; the sum divided by n; the height; "
                  "and whether the two methods left the same array."),
            ("p", "The worked example <code>shuffled</code>, labelled one fixed shuffle of the "
                  "keys, has n = 31. The sum is 26, the bottom-up build makes 21 swaps, and "
                  "inserting one key at a time makes 30. Choose the worked example labelled "
                  "keys arriving in decreasing order, <code>worst-for-inserts</code>: every key "
                  "is as far from its place as a key can be, the bottom-up build makes 26 swaps, "
                  "exactly the sum, and insertion makes 98. The bound is met, so on this input "
                  "it cannot be improved. The third example, <code>already-a-heap</code>, sends "
                  "the keys in increasing order: no swaps at all for either method."),
            ("p", "Move the slider to 20 keys and you have the table above: the sum is 21, "
                  "which the lab prints as 21/20 per element. On the shuffle the build swaps 11 "
                  "times; in decreasing order, 17. Neither count is the bound. The bound is a "
                  "sum over the shape of the tree, the same for every array of 20 keys, and the "
                  "proof says no array can need more. The counts say what two arrays needed."),
            ("h3", "Exercise"),
            ("p", "Run BUILD-MAX-HEAP by hand on `[3, 8, 10, 1, 12, 6, 4, 7]`. Write the "
                  "array after each call of MAX-HEAPIFY, count the exchanges, and compare the "
                  "total with the sum over heights at n = 8. Then say which call made the most "
                  "exchanges and why it could not have made more."),
            ("p", "A heap's largest key is at its root. The next lesson, Heapsort and Priority "
                  "Queues, takes it from there, n − 1 times, and turns the heap into a sorted "
                  "array and into a queue that always serves its largest key first."),
        ],
        "lab": ("heap", {
            "mode": "build",
            "preset": "shuffled",
            "panel_title": "Build a heap and price it by the sum over heights",
            "panel_intro": (
                "The keys are 1 to n in the arrival order you choose. The bottom-up build, "
                "BUILD-MAX-HEAP's method mirrored for a min-heap, and n separate insertions run "
                "on the same keys with counters. The sum over heights is evaluated exactly beside "
                "them: it is the bound for every arrival order, and the swaps are what one order "
                "cost."
            ),
        }),
        "steps_title": "Building a heap by hand",
        "steps_intro": "Four steps on paper, then one on an array of your own.",
        "steps": [
            ("Draw the tree from the array",
             "Put `A[1]` at the root and fill each level left to right. Mark nodes `⌊n/2⌋ + 1` "
             "to `n`: they are the leaves and will not be touched."),
            ("Sift down from the last internal node",
             "For i from `⌊n/2⌋` down to 1, compare `A[i]` with its children, exchange it with "
             "the larger child if that child is larger, and repeat from where it landed until "
             "it is at least as large as its children or is a leaf."),
            ("Count the exchanges per call",
             "Write beside each node how many exchanges its call made. No call can make more "
             "than the height of its node."),
            ("Evaluate the sum over heights",
             "For h from 0 to `⌊lg n⌋`, multiply `⌈n/2ʰ⁺¹⌉` by h and add. Your total exchanges "
             "must not exceed it, whatever the array."),
            ("Do it on an array of your own",
             "Write ten distinct numbers in any order, build the max-heap by hand, then set the "
             "lab to 10 keys and compare your exchange count with the sum the lab prints, 10."),
        ],
        "worked": {
            "title": "Ten keys, five calls",
            "intro": [
                "Build a max-heap from `[6, 11, 3, 15, 9, 1, 14, 8, 12, 2]`. Here n = 10, so "
                "the calls run from i = 5 down to 1 and nodes 6 to 10 are leaves.",
            ],
            "lines": [
                "i = 5: 9 over 2, no exchange",
                "i = 4: 15 over 8 and 12, no exchange",
                "i = 3: 3 sinks below 14; 1 exchange",
                "i = 2: 11 sinks past 15, then 12; 2",
                "i = 1: 6 sinks past 15, 12, then 11; 3",
                "heap: 15 12 14 11 9 1 3 8 6 2",
                "6 exchanges; the sum at n = 10 is 10",
            ],
            "after": [
                "The sum at n = 10 is `3·1 + 2·2 + 1·3 = 10`, and six exchanges is within it. "
                "The root's call made 3, the most any call can make here, because the root has "
                "height 3. Check the final array against the property: each parent at `⌊i/2⌋` "
                "is at least as large as the node at i.",
            ],
        },
        "quiz_title": "Heaps, heights and the build",
        "quiz": [
            {"q": "Run BUILD-MAX-HEAP on the exercise array `[3, 8, 10, 1, 12, 6, 4, 7]`. "
                  "What is the resulting array, and how many exchanges are made?",
             "a": ["`[12, 8, 10, 7, 3, 6, 4, 1]`, 4 exchanges",
                   "`[12, 10, 8, 7, 6, 4, 3, 1]`, 4 exchanges",
                   "`[12, 8, 10, 7, 3, 6, 4, 1]`, 7 exchanges",
                   "`[12, 3, 10, 7, 8, 6, 4, 1]`, 3 exchanges"],
             "c": 0,
             "why": "The call at i = 4 exchanges 1 with 7; at i = 3, 10 is already larger than 6 "
                    "and 4; at i = 2, 8 is exchanged with 12; at i = 1, 3 sinks past 12 and then "
                    "8. That is 1 + 0 + 1 + 2 = 4 exchanges, leaving `[12, 8, 10, 7, 3, 6, 4, 1]`. "
                    "The sorted descending array is also a heap, but not the one this build "
                    "produces. Seven is the sum over heights at n = 8, the bound, not the count. "
                    "Stopping 3 at node 2 leaves it above 7 and 8, which breaks the property."},
            {"q": "What is the sum of `⌈n/2ʰ⁺¹⌉ · h` over h from 0 to `⌊lg n⌋` at n = 20?",
             "a": ["80", "21", "20", "26"],
             "c": 1,
             "why": "The terms are 10·0, 5·1, 3·2, 2·3 and 1·4, which add to 21. Eighty is "
                    "`n·⌊lg n⌋`, the loose bound that charges every node the root's height. "
                    "Twenty would be one unit per node. Twenty-six is the sum at n = 31."},
            {"q": "In a heap of 13 elements stored in `A[1..13]`, which indices are the leaves?",
             "a": ["7 to 13", "6 to 13", "8 to 13", "1 to 6"],
             "c": 0,
             "why": "The leaves are `⌊n/2⌋ + 1` to n, here 7 to 13: node 6 has a left child at "
                    "12, and node 7's first child would be at 14, beyond the heap. Indices 1 to 6 "
                    "are the internal nodes, the ones BUILD-MAX-HEAP calls MAX-HEAPIFY on."},
            {"q": "Why does BUILD-MAX-HEAP call MAX-HEAPIFY on nodes `⌊n/2⌋` down to 1, rather "
                  "than from 1 up to `⌊n/2⌋`?",
             "a": ["Going down from `⌊n/2⌋` makes fewer comparisons than going up, though "
                   "either order produces a max-heap",
                   "MAX-HEAPIFY on node i assumes both of i's subtrees are already max-heaps, "
                   "and the children are numbered above i",
                   "The leaves must be sorted before the internal nodes are visited",
                   "Going down from `⌊n/2⌋` makes the procedure stable"],
             "c": 1,
             "why": "MAX-HEAPIFY only repairs one node whose subtrees are already heaps. Working "
                    "from high indices to low, every child has been processed before its "
                    "parent, which is the maintenance step of the loop invariant. Run upward, "
                    "the root is fixed before its subtrees are heaps and the result need not be "
                    "a heap at all, so it is not a question of cost. The leaves are never "
                    "sorted, and heapsort is not stable in any order."},
        ],
        "mistakes": [
            ("Pricing the build at n lg n because each call costs O(lg n)",
             "There are about n/2 calls and each can cost up to the tree's height, so `O(n lg n)` "
             "is a correct bound, and the authors say so before showing it is not tight. A "
             "call costs the height of its own node, and half the nodes are leaves, a quarter "
             "have height 1, and only one has height `⌊lg n⌋`; the sum over heights is linear. "
             "On the lesson's 20 keys the sum is 21 against `n·⌊lg n⌋ = 80`, and the "
             "worst arrival order the lab offers at 31 keys meets its sum of 26 exactly."),
            ("Reading the heap property as sorted order",
             "The property relates each node to its parent and nothing else. Siblings can be "
             "in either order, and two nodes on different branches are not compared at all, "
             "which is why one set of keys has many heaps: the lab's two methods leave "
             "different arrays from the same shuffle. A sorted array is a heap, but a heap is "
             "rarely sorted; taking it apart into sorted order is the next lesson's work."),
            ("Calling MAX-HEAPIFY on a node whose subtrees are not heaps",
             "MAX-HEAPIFY sinks one value along one path and assumes everything below already "
             "obeys the property. Called on the root of an arbitrary array it fixes that path "
             "and leaves the rest as it was. That precondition is why the build goes from the "
             "last internal node upward to the root, and why the loop invariant is stated "
             "about the nodes numbered above i."),
        ],
        "standard": (
            "Finish when you can build a heap by hand and bound the work.",
            "Given eight to twelve keys, produce the max-heap BUILD-MAX-HEAP produces, count "
            "its exchanges, and evaluate the sum over heights that bounds them."
        ),
        "note": (
            "The lab builds a min-heap from the keys 1 to n in three arrival orders, so it "
            "cannot take your own array; the exercise and the worked example do that by hand. "
            "Its counts are swaps, which is what MAX-HEAPIFY's cost is made of, and they "
            "describe the order on screen. The linear bound is the theorem's, for every order."
        ),
    },
    # ---------------------------------------------------------------- 02
    # CLRS sections 6.4-6.5, pp. 159-169.
    # Quote: p. 162, 20 words, quotes.py OK. Lesson total: 20 words.
    # HEAPSORT and its O(n lg n) bound (pp. 159-160); priority queues, the
    # max- and min-priority operations, job scheduling and event-driven
    # simulation, handles (pp. 162-163); HEAP-MAXIMUM, HEAP-EXTRACT-MAX,
    # HEAP-INCREASE-KEY, MAX-HEAP-INSERT and their costs (pp. 163-165).
    {
        "slug": "heapsort-and-priority-queues",
        "title": "Heapsort and Priority Queues",
        "module": "Chapter 6 · Heapsort",
        "one_line": "Heapsort takes the root of a max-heap n − 1 times, and the same heap, with a key that can rise and a slot that can be added, is a priority queue whose every operation costs O(lg n).",
        "summary": (
            "Sections 6.4 and 6.5 use the heap twice. Heapsort builds a max-heap, then swaps the "
            "root to the end of the array and restores the heap n − 1 times, sorting in place in "
            "O(n lg n). A priority queue keeps a heap and offers the largest key, extracts it, "
            "raises a key and inserts a new one, each in O(lg n). Sort six keys by hand, then "
            "count heapsort's comparisons in the lab beside merge sort's on the same array."
        ),
        "key": [
            "build once, then n − 1 extractions",
            "each extraction: swap root, sift down",
            "heapsort is O(n lg n) and in place",
            "it is neither stable nor adaptive",
            "increase a key: walk it up, O(lg n)",
            "insert: add a slot, increase its key",
        ],
        "key_label": "Sections 6.4 and 6.5 in six lines",
        "concepts_intro": (
            "Three ideas: one sorting algorithm and two words for what the heap becomes when it "
            "serves an application rather than a sort."
        ),
        "concepts": [
            ("Heapsort",
             "Build a max-heap on `A[1..n]`; the largest key is at `A[1]`. Exchange it with "
             "`A[n]`, shrink the heap by one so that the key just placed is out of it, and call "
             "MAX-HEAPIFY on the root. Repeat until the heap has one element. The sorted part "
             "grows from the right as the heap shrinks from the left, in the same array."),
            ("Priority queue",
             "A set of elements, each with a key, that supports finding and removing the "
             "element with the largest key (a max-priority queue) or the smallest (a "
             "min-priority queue). The book's examples are a scheduler choosing the next job "
             "and an event-driven simulator choosing the next event by time."),
            ("Handle",
             "The link between an application's object and its position in the heap, kept in "
             "both directions, because the heap moves elements as it works. Raising the key of "
             "a particular job needs its handle to find where the job now is."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 6.4 and 6.5 in your own copy first. The lesson sets out the sort and "
            "the queue in its own words, sorts six keys by hand, and then counts heapsort's "
            "comparisons on larger arrays in the lab."
        ),
        "body": [
            ("p", "&ldquo;Heapsort is an excellent algorithm, but a good implementation of "
                  "quicksort, presented in Chapter 7, usually beats it in practice.&rdquo; The "
                  "authors write that at the start of Section 6.5, and then give the heap its "
                  "second career, as a priority queue. This lesson reads sections 6.4 and 6.5: "
                  "the sort the chapter is named for, and the queue that outlives it in the rest "
                  "of the book."),
            ("p", "Section 6.4's HEAPSORT is short because the last lesson did the work. "
                  "BUILD-MAX-HEAP puts the largest key at `A[1]`. That key belongs at `A[n]`, so "
                  "the two are exchanged and the heap-size drops by one, which takes the placed "
                  "key out of the heap without moving it again. The new root may now break the "
                  "property, but both of its subtrees are still heaps, which is exactly "
                  "MAX-HEAPIFY's precondition; one call restores the heap on the first n − 1 "
                  "elements. Repeating this down to a heap of size 2 leaves the array sorted."),
            ("thm", ("Heapsort's running time",
                     "BUILD-MAX-HEAP takes `O(n)`, and the n − 1 calls of MAX-HEAPIFY that follow "
                     "cost `O(lg n)` apiece, so HEAPSORT runs in `O(n lg n)` time, using only a "
                     "constant amount of storage outside the array.")),
            ("p", "That combination is the chapter's opening promise kept: merge sort's bound "
                  "and insertion sort's frugality. What heapsort does not promise matters as "
                  "much. Its long-range exchange, root to end, carries a key past others equal "
                  "to it, so equal keys can leave in a different order from the one they "
                  "arrived in: heapsort is not stable. And it does not get cheaper on input "
                  "that is already nearly sorted. Section 7.4 and Chapter 8 return to both "
                  "properties; here they are things to watch the lab for."),
            ("p", "Section 6.5 turns to priority queues. A max-priority queue supports four "
                  "operations on a set S: INSERT adds an element, MAXIMUM returns the element "
                  "with the largest key, EXTRACT-MAX removes and returns it, and INCREASE-KEY "
                  "raises one element's key to a new value at least as large. A min-priority "
                  "queue offers the mirror operations. The authors' two applications show why "
                  "both directions exist: a shared computer picks the highest-priority waiting "
                  "job, and a simulation always processes the event with the earliest time "
                  "next, inserting the new events each one causes."),
            ("p", "The heap implementations follow from the two procedures already met. "
                  "HEAP-MAXIMUM reads `A[1]` in `Θ(1)`. HEAP-EXTRACT-MAX saves the root, moves "
                  "the last element into its place, shrinks the heap and calls MAX-HEAPIFY: "
                  "`O(lg n)`. HEAP-INCREASE-KEY works the other way. A key that rises can only "
                  "break the property with its parent, so it is exchanged with its parent while "
                  "the parent is smaller, walking up a path of at most `⌊lg n⌋` edges. "
                  "MAX-HEAP-INSERT adds a slot at the end holding a key smaller than every key "
                  "and then increases it to the new key, so it costs what INCREASE-KEY costs."),
            ("def", ("The costs on an n-element heap",
                     "HEAP-MAXIMUM `Θ(1)`; HEAP-EXTRACT-MAX, HEAP-INCREASE-KEY and "
                     "MAX-HEAP-INSERT each `O(lg n)`. Every priority-queue operation on a set of "
                     "n elements runs in `O(lg n)` time.")),
            ("p", "Now the lab, the heap lab of the Algorithms Subject's lesson Heapsort, where "
                  "the sort is practised further. It sorts the keys 1 to n in the arrival order "
                  "you choose, counting comparisons the way MAX-HEAPIFY makes them, up to two "
                  "per level; runs merge sort on the same array for a second count; and sorts a "
                  "list of tagged repeated keys to show what happens to equal keys. The tiles are "
                  "heapsort's comparisons, how many of them the build spent, merge sort's "
                  "comparisons, the ratio of the two, the extra memory, and how many pairs of "
                  "equal keys came out in the wrong order."),
            ("p", "The worked example <code>shuffled</code>, labelled one fixed shuffle, sorts "
                  "16 keys in 80 comparisons, 22 of them building the heap and 58 in the 15 "
                  "extractions, against merge sort's 48: a ratio of 5/3. Extra memory is 0 "
                  "cells. With four distinct keys repeated four times each, 15 pairs of equal "
                  "keys come out reversed, which is the instability made visible. Now choose "
                  "<code>sorted-input</code>, labelled already in increasing order: 85 "
                  "comparisons, more than the shuffle cost, while merge sort's count falls to "
                  "32. The <code>reversed-input</code> example costs 72, with only two distinct "
                  "keys in the tie test and 40 pairs out of order."),
            ("p", "Set those beside the bounds. Every comparison sort needs at least "
                  "`⌈lg 16!⌉ = 45` comparisons in the worst case on 16 keys, a bound Chapter 8 "
                  "proves, and the 15 extractions can cost at most two comparisons per level of "
                  "a heap that is shrinking. The counts sit inside those limits on every array "
                  "the lab offers; that they stay inside them on every array is the theorem's "
                  "work, not the lab's."),
            ("h3", "Exercise"),
            ("p", "Start from the max-heap of the last lesson's worked example, `[15, 12, 14, "
                  "11, 9, 1, 3, 8, 6, 2]`. Perform HEAP-EXTRACT-MAX, then MAX-HEAP-INSERT with "
                  "key 13. Write the array after each operation and count the exchanges each "
                  "made."),
            ("p", "Heapsort's bound is a worst case it always meets within a constant. The next "
                  "lesson, Quicksort and Partitioning, reads the sort the authors say usually "
                  "beats it, whose worst case is far worse and whose typical case is not."),
        ],
        "lab": ("heap", {
            "mode": "heapsort",
            "preset": "shuffled",
            "panel_title": "Sort in place and count the comparisons",
            "panel_intro": (
                "Heapsort builds a max-heap on the keys 1 to n and then swaps the root to the end "
                "and sifts down, n − 1 times, in the same array. Merge sort runs on the same "
                "array for a second count. The tie test sorts tagged repeated keys and marks "
                "every pair of equal keys that came out in the wrong order."
            ),
        }),
        "steps_title": "Heapsort by hand",
        "steps_intro": "Keep two marks on the array: where the heap ends, and where the sorted part begins.",
        "steps": [
            ("Build the max-heap",
             "Run BUILD-MAX-HEAP as in the last lesson and count its comparisons: up to two at "
             "each node a value sinks through."),
            ("Exchange the root with the last heap slot",
             "Swap `A[1]` with the last element of the heap and move the boundary left by one. "
             "The key now right of the boundary is in its final place."),
            ("Sift the new root down",
             "Call MAX-HEAPIFY on node 1 of the smaller heap, comparing the two children, then "
             "the larger with the parent, until the parent wins or there are no children."),
            ("Repeat to a heap of one",
             "Do n − 1 extractions in all. Add up the comparisons of the build and of the "
             "extractions separately."),
            ("Do it on an array of your own",
             "Sort six keys of your own by hand, then set the lab to 6 keys and compare the "
             "split between building and extracting on its array with yours."),
        ],
        "worked": {
            "title": "Six keys, five extractions",
            "intro": [
                "Sort `[4, 9, 2, 7, 5, 1]`. BUILD-MAX-HEAP makes 7 comparisons and gives "
                "`[9, 7, 2, 4, 5, 1]`. The bar marks the boundary of the heap.",
            ],
            "lines": [
                "swap 9 out, sift 1:  7 5 2 4 1 | 9",
                "swap 7 out, sift 1:  5 4 2 1 | 7 9",
                "swap 5 out, sift 1:  4 1 2 | 5 7 9",
                "swap 4 out, sift 2:  2 1 | 4 5 7 9",
                "swap 2 out:          1 | 2 4 5 7 9",
                "comparisons: 4, 3, 2, 1, 0",
                "total: 7 building + 10 = 17",
            ],
            "after": [
                "Each extraction's comparisons depend on how far the new root sinks and how "
                "many children it meets. The first sinks two levels with two children at each, "
                "4 comparisons; the fourth meets a single child, 1. Heapsort's bound counts the "
                "levels, at most `⌊lg m⌋` in a heap of m elements, at two comparisons each.",
            ],
        },
        "quiz_title": "The sort and the queue",
        "quiz": [
            {"q": "Starting from the max-heap `[15, 12, 14, 11, 9, 1, 3, 8, 6, 2]`, perform "
                  "HEAP-EXTRACT-MAX and then MAX-HEAP-INSERT with key 13. What is the array?",
             "a": ["`[14, 13, 3, 11, 12, 1, 2, 8, 6, 9]`",
                   "`[14, 12, 3, 11, 9, 1, 2, 8, 6, 13]`",
                   "`[13, 12, 14, 11, 9, 1, 3, 8, 6, 2]`",
                   "`[14, 13, 12, 11, 9, 8, 6, 3, 2, 1]`"],
             "c": 0,
             "why": "Extraction moves the last key, 2, to the root and sifts it down past 14 and "
                    "then 3, giving `[14, 12, 3, 11, 9, 1, 2, 8, 6]` with 2 exchanges. Insertion "
                    "puts 13 at position 10, whose parent is position 5 holding 9: exchange; then "
                    "position 2 holding 12: exchange; then the root, 14, is larger, so it stops. "
                    "Leaving 13 at the end skips the walk up and breaks the property with its "
                    "parent 9. Replacing the root with 13 is not what extraction does. The "
                    "descending array is a heap but not the one these operations produce."},
            {"q": "After BUILD-MAX-HEAP on 16 keys, how many times does HEAPSORT exchange the "
                  "root with the last heap element and call MAX-HEAPIFY?",
             "a": ["16", "15", "8", "4"],
             "c": 1,
             "why": "Each extraction places one key, and when one key is left in the heap it is "
                    "already in place, so there are n − 1 = 15. Sixteen counts that last key too. "
                    "Eight is the number of internal nodes the build visits, and 4 is the height "
                    "of the heap."},
            {"q": "On the lab's shuffled 16 keys heapsort makes 80 comparisons and merge sort "
                  "48. What does that pair of counts establish?",
             "a": ["Heapsort's worst case grows faster than merge sort's",
                   "On this array heapsort made 5/3 as many comparisons as merge sort; both "
                   "sorts are `O(n lg n)` in the worst case",
                   "Heapsort makes 5/3 as many comparisons as merge sort on every array of 16 "
                   "keys",
                   "Heapsort is above the comparison lower bound and merge sort is below it"],
             "c": 1,
             "why": "Two counts on one array describe that array. Both sorts are `O(n lg n)` in "
                    "the worst case, so the worst-case growth is the same, and on the sorted "
                    "array the ratio is 85/32, not 5/3. Neither count can be below the bound "
                    "`⌈lg 16!⌉ = 45` on its worst input, and merge sort's 48 is above it."},
            {"q": "Why does HEAP-INCREASE-KEY run in `O(lg n)` time on an n-element heap?",
             "a": ["It calls BUILD-MAX-HEAP after changing the key, and the build is linear",
                   "It changes one key and returns, which is constant time",
                   "The raised key can only conflict with its ancestors, so it moves up one "
                   "path of at most `⌊lg n⌋` edges",
                   "It calls MAX-HEAPIFY on the node, which sinks the key toward the leaves"],
             "c": 2,
             "why": "A key that rises stays at least as large as its children, so only the "
                    "parent relation can break, and exchanging with the parent while the parent "
                    "is smaller climbs at most the height. Rebuilding would cost `O(n)`, more "
                    "than needed. Stopping after the change could leave the key above a smaller "
                    "parent. MAX-HEAPIFY sinks, which is what EXTRACT-MAX needs, not this."},
        ],
        "mistakes": [
            ("Expecting heapsort to keep equal keys in order, like merge sort",
             "Heapsort and merge sort share the `O(n lg n)` worst case, and it is tempting to "
             "assume they share their other properties. They do not: heapsort's exchange of "
             "the root with the last heap slot carries a key past others equal to it. In the "
             "lab's tie test, with four distinct keys four times each, 15 pairs of equal keys "
             "leave in the wrong order. A bound on time says nothing about stability."),
            ("Expecting sorted input to be cheap",
             "Insertion sort is fast on nearly sorted input, and some readers expect every sort "
             "to be. Heapsort first builds a max-heap, which rearranges an increasing array "
             "almost completely, and then takes it apart the same way whatever the input was. "
             "In the lab, 16 keys already in order cost 85 comparisons against 80 for the "
             "shuffle."),
            ("Thinking a priority queue keeps its elements sorted",
             "A sorted list would make MAXIMUM cheap and INSERT linear. The heap keeps only "
             "the heap property, which is enough to find the largest key at once and cheap "
             "enough to restore: every operation costs `O(lg n)`. The rest of the order is "
             "left undetermined until someone asks for it."),
        ],
        "standard": (
            "Finish when you can run heapsort and the queue operations by hand.",
            "Given six to ten keys, sort them by heapsort counting comparisons by phase, and "
            "carry a max-heap through an extraction and an insertion, naming the cost of each."
        ),
        "note": (
            "The lab sorts the keys 1 to n in three arrival orders and a tagged list of repeated "
            "keys; it does not run the priority-queue operations, which the exercise and quiz "
            "do by hand. Its comparison counts describe the arrays on screen. The `O(n lg n)` "
            "bound and the `O(lg n)` cost of each queue operation are the book's, for every "
            "input."
        ),
    },
    # ---------------------------------------------------------------- 03
    # CLRS sections 7.1-7.2, pp. 170-179.
    # Quote: p. 170, 17 words, quotes.py OK. Lesson total: 17 words.
    # Chapter opening: Theta(n^2) worst case, Theta(n lg n) expected, in
    # place (p. 170); divide, conquer, combine (pp. 170-171); PARTITION and
    # its four-region invariant (pp. 171-173); worst-case and best-case
    # partitioning, the 9-to-1 split, good and bad splits alternating
    # (pp. 174-178).
    {
        "slug": "quicksort",
        "title": "Quicksort and Partitioning",
        "module": "Chapter 7 · Quicksort",
        "one_line": "Quicksort puts one pivot in its final place and the smaller and larger keys on either side, then sorts the sides; how evenly the pivot splits decides whether that costs n lg n or n².",
        "summary": (
            "Sections 7.1 and 7.2 describe quicksort and its partition, prove the partition "
            "correct with a four-region loop invariant, and look at its running time by the "
            "shape of the splits: a split of n − 1 to 0 at every level gives Θ(n²), a split in "
            "half gives Θ(n lg n), and so does any split of constant proportion. Partition ten "
            "keys step by step in the lab with the invariant checked after every comparison."
        ),
        "key": [
            "partition: one pass, one pivot placed",
            "left of the pivot: at most the pivot",
            "n − 1 comparisons to partition n keys",
            "split n − 1 to 0 each time: Θ(n²)",
            "split in half each time: Θ(n lg n)",
            "a nine-to-one split is still Θ(n lg n)",
        ],
        "key_label": "Sections 7.1 and 7.2 in six lines",
        "concepts_intro": (
            "Three ideas: the pattern quicksort shares with merge sort, the step where the work "
            "is done, and the property that proves that step correct."
        ),
        "concepts": [
            ("Divide, conquer, combine",
             "Quicksort's version of Section 2.3's pattern. Divide: rearrange `A[p..r]` around "
             "a pivot so that everything left of position q is at most `A[q]` and everything "
             "right of it is at least `A[q]`. Conquer: sort the two sides recursively. Combine: "
             "nothing, because the sides are already in place."),
            ("The pivot",
             "The element the partition compares every other element with. PARTITION takes "
             "the last element of the subarray, and the quality of that choice, how close the "
             "pivot is to the middle of the keys, decides the running time."),
            ("The partition invariant",
             "Before every iteration of PARTITION's loop, the subarray is in four "
             "regions: keys known to be at most the pivot, keys known to be greater, keys not "
             "yet examined, and the pivot itself in the last position."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the chapter opening and sections 7.1 and 7.2 in your own copy first. The "
            "lesson sets out the partition and its invariant in its own words, steps through "
            "one partition in the lab, and then counts whole sorts by hand for the best and the "
            "worst split."
        ),
        "body": [
            ("p", "The chapter opens with a paradox. Quicksort's worst case is `Θ(n²)`, no "
                  "better than insertion sort's, and yet, in the authors' words, &ldquo;quicksort "
                  "is often the best practical choice for sorting because it is remarkably "
                  "efficient on the average&rdquo;. The expected time is `Θ(n lg n)` with small "
                  "constants, it sorts in place, and it behaves well with virtual memory. This "
                  "lesson reads sections 7.1 and 7.2, the algorithm and an intuitive look at its "
                  "performance; the next lesson reads the precise analysis."),
            ("p", "Section 7.1 sets quicksort beside merge sort as divide-and-conquer with the "
                  "work moved. Merge sort divides trivially and does its work combining; "
                  "quicksort does its work dividing and has nothing left to combine. QUICKSORT "
                  "calls PARTITION on `A[p..r]`, which returns the pivot's final index q, and "
                  "then sorts `A[p..q − 1]` and `A[q + 1..r]` by recursive calls. Sorting a whole "
                  "array is the call on `A[1..n]`."),
            ("p", "PARTITION takes `x = A[r]` as the pivot and keeps an index i, the end of the "
                  "region known to hold keys at most x. A second index j walks from p to "
                  "`r − 1`. Each key `A[j]` is compared with x once. If it is greater, the region "
                  "of greater keys grows by one just by j moving on. If it is at most x, i "
                  "advances and `A[i]` and `A[j]` are exchanged, which moves the small key to the "
                  "end of the small region and the first greater key to the end of the greater "
                  "region. When j reaches r, one last exchange puts the pivot between the two "
                  "regions, at `i + 1`, which is returned."),
            ("thm", ("The loop invariant of PARTITION",
                     "Before every iteration of the loop, for any index k: if "
                     "`p ≤ k ≤ i` then `A[k] ≤ x`; if `i + 1 ≤ k ≤ j − 1` then `A[k] > x`; and "
                     "if `k = r` then `A[k] = x`. The keys from j to `r − 1` are unrestricted.")),
            ("p", "The authors prove it in the usual three parts. Before the first iteration "
                  "`i = p − 1` and `j = p`, so the first two regions are empty and the third "
                  "condition holds by the assignment of x. Each iteration maintains it in one of "
                  "the two ways just described. At termination `j = r`, every key has been "
                  "placed in one of the three named sets, and the final exchange leaves the "
                  "pivot between them. The loop does a constant amount of work per key, so "
                  "PARTITION on n keys takes `Θ(n)` time and makes exactly n − 1 comparisons."),
            ("p", "Section 7.2 asks what the splits cost. In the worst case every partition "
                  "puts n − 1 keys on one side and none on the other, and the recurrence is "
                  "`T(n) = T(n − 1) + Θ(n)`, whose sum is `Θ(n²)`. The authors point out when "
                  "this happens: when the input is already completely sorted, the very case in "
                  "which insertion sort takes `O(n)`. In the best case each split is as even as "
                  "possible, `T(n) = 2T(n/2) + Θ(n)`, and case 2 of the master theorem gives "
                  "`Θ(n lg n)`."),
            ("p", "The surprise is in between. Suppose every split is 9 to 1, which looks "
                  "badly lopsided. The recursion tree has cost at most cn on each level, and its "
                  "deepest path, the one that keeps the 9/10 side, ends after "
                  "`log₁₀/₉ n = Θ(lg n)` levels. The total is `O(n lg n)`. Any split of constant "
                  "proportion gives the same: only the constant in front changes. The authors "
                  "add an intuition for random input, where good and bad splits mix: a bad split "
                  "followed by a good one costs `Θ(n)` and leaves pieces no worse than one good "
                  "split would, so the bad split is absorbed."),
            ("p", "Now the lab. It runs PARTITION on the keys in the box, records the array "
                  "after every comparison and evaluates the invariant on that array. The "
                  "Algorithms Subject's lessons Partitioning and Quicksort and Its Worst Case "
                  "use the same lab for more practice. The tiles are the comparisons, the "
                  "exchanges, the pivot's final position and whether the invariant held at "
                  "every step. The pivot slider chooses which element is the pivot; any choice "
                  "other than the last is first exchanged into the last position, as Section "
                  "7.3 will do at random, and that exchange is counted."),
            ("p", "The lesson's array is `21, 7, 30, 12, 4, 26, 15, 9, 33, 18` with the pivot at "
                  "position 10, the value 18: PARTITION as written. It makes 9 comparisons and "
                  "6 exchanges, the invariant holds at every step, and 18 ends at position 6, "
                  "with `7, 12, 4, 15, 9` before it and `21, 30, 33, 26` after it. The step "
                  "slider starts after the fourth comparison: 7 and 12 form the small region, 30 "
                  "and 21 the greater region, and five keys are unexamined. The table numbers "
                  "positions from 0, as the code inside the lab does, so its i and j are one "
                  "less than the book's."),
            ("p", "Now move the pivot slider to position 9, the value 33, the largest key. Nine "
                  "comparisons again, because the count does not depend on the data, but only 2 "
                  "exchanges, and the pivot ends at position 10 with all nine other keys on one "
                  "side. That is the worst-case split, made by one choice of pivot. Position 1, "
                  "the value 21, lands at position 7: a split of 6 to 3."),
            ("h3", "Exercise"),
            ("p", "Run PARTITION by hand on `[14, 3, 27, 8, 19, 5, 11]`, pivot 11. Write the "
                  "array after each comparison, mark the four regions, and say where the pivot "
                  "ends. Then type the keys into the lab, step through, and check each of your "
                  "arrays against its table."),
            ("p", "Section 7.2 showed that the input decides the splits when the pivot is the "
                  "last element. The next lesson, Randomized Quicksort and Its Analysis, takes "
                  "that power away from the input and computes the expected number of "
                  "comparisons exactly."),
        ],
        "lab": ("sortkit", {
            "mode": "partition",
            "keys": "21, 7, 30, 12, 4, 26, 15, 9, 33, 18",
            "scheme": "lomuto",
            "pivot": 10,
            "step": 3,
            "panel_title": "Partition ten keys and check the invariant",
            "panel_intro": (
                "PARTITION runs on the keys in the box and records the array after every "
                "comparison. The invariant column is evaluated on that array, never assumed. "
                "Keep the scheme on Lomuto, the book's PARTITION; Hoare's original scheme is the "
                "subject of Problem 7-1."
            ),
        }),
        "steps_title": "Partitioning by hand",
        "steps_intro": "Four steps for one partition, and one on keys of your own.",
        "steps": [
            ("Take the last key as the pivot",
             "Write x = `A[r]`. Set i one position before the start and j at the start."),
            ("Compare each key with the pivot",
             "For each j up to `r − 1`: if `A[j] ≤ x`, advance i and exchange `A[i]` with "
             "`A[j]`; otherwise leave it. Count one comparison per key."),
            ("Check the four regions",
             "After each comparison, mark the keys up to i (at most x), from `i + 1` to j "
             "(greater), the unexamined rest, and the pivot. A key in the wrong region means a "
             "mistake in the last step."),
            ("Place the pivot",
             "Exchange `A[i + 1]` with `A[r]`. The pivot is now in its final sorted position; "
             "the sides are separated, not sorted."),
            ("Do it on keys of your own",
             "Type eight keys of your own into the lab, choose as pivot first the largest key "
             "and then one near the middle, and note how the final position changes while the "
             "comparison count stays at seven."),
        ],
        "worked": {
            "title": "Seven keys, the worst split and the best",
            "intro": [
                "Count the comparisons of the whole of QUICKSORT, with PARTITION taking the last "
                "key, on two arrangements of 1 to 7.",
            ],
            "lines": [
                "sorted, [1, 2, 3, 4, 5, 6, 7]:",
                "  sizes 7, 6, 5, 4, 3, 2 each split to 0",
                "  6 + 5 + 4 + 3 + 2 + 1 = 21",
                "[1, 3, 2, 6, 5, 7, 4]:",
                "  pivot 4 splits 7 into 3 and 3",
                "  pivots 2 and 6 split each 3 into 1, 1",
                "  6 + 2 + 2 = 10",
            ],
            "after": [
                "Sorted input costs `n·(n − 1)/2 = 21`, the worst case, because each pivot is "
                "the largest key of its subarray. The second arrangement was chosen so that "
                "every pivot is a median, and costs less than half as much. The same seven keys "
                "cost 21 or 10 depending only on their order, which is what the next lesson's "
                "random pivot is designed to make irrelevant.",
            ],
        },
        "quiz_title": "Partition and the shape of the splits",
        "quiz": [
            {"q": "Run PARTITION on the exercise array `[14, 3, 27, 8, 19, 5, 11]`, pivot 11. "
                  "What is the array afterwards, and how many comparisons were made?",
             "a": ["`[3, 8, 5, 11, 19, 27, 14]`, 6 comparisons",
                   "`[3, 5, 8, 11, 14, 19, 27]`, 6 comparisons",
                   "`[3, 8, 5, 11, 19, 27, 14]`, 7 comparisons",
                   "`[3, 8, 5, 14, 19, 27, 11]`, 6 comparisons"],
             "c": 0,
             "why": "The keys at most 11 are 3, 8 and 5; each in turn is exchanged to the end of "
                    "the small region, giving `[3, 8, 5, 14, 19, 27, 11]` after the loop, and the "
                    "final exchange puts 11 at position 4: `[3, 8, 5, 11, 19, 27, 14]`. Each of "
                    "the six keys other than the pivot is compared once. The sorted array would "
                    "need the recursion as well. Seven counts the pivot against itself. Stopping "
                    "before the last exchange leaves the pivot at the end."},
            {"q": "QUICKSORT, with PARTITION taking the last key, sorts 10 keys that are already "
                  "in increasing order. How many comparisons does it make?",
             "a": ["45", "9", "19", "100"],
             "c": 0,
             "why": "Each pivot is the largest key of its subarray, so the sizes are 10, 9, …, 2 "
                    "and the comparisons 9 + 8 + … + 1 = 45. Nine is one partition. Nineteen is "
                    "what the whole sort costs on the lesson's lab array, whose splits are much "
                    "more even. A hundred is `n²`, the order of growth but not the count."},
            {"q": "Every partition in a run of quicksort splits its subarray 9 to 1. What is the "
                  "running time?",
             "a": ["`Θ(n²)`, because one side is nine times the other",
                   "`O(n lg n)`, because each level costs at most cn and there are "
                   "`Θ(lg n)` levels",
                   "`Θ(n)`, because the small side shrinks by a factor of ten",
                   "`O(n lg n)` only if n is a power of 10"],
             "c": 1,
             "why": "The recursion tree has at most cn work per level and its longest path "
                    "shrinks by 9/10 per level, so it has `log₁₀/₉ n = Θ(lg n)` levels and the "
                    "total is `O(n lg n)`. Quadratic time needs splits that leave a constant "
                    "number of keys on one side, not a constant fraction. The large side, not "
                    "the small one, sets the depth. The argument does not depend on n being a "
                    "power of anything."},
            {"q": "Partway through PARTITION, what does the invariant say about the keys in "
                  "positions `i + 1` to `j − 1`?",
             "a": ["They are greater than the pivot",
                   "They are at most the pivot",
                   "They have not yet been compared with the pivot",
                   "They are greater than the pivot and in sorted order"],
             "c": 0,
             "why": "Positions p to i hold keys at most the pivot, positions `i + 1` to `j − 1` "
                    "keys greater than it, positions j to `r − 1` keys not yet examined, and "
                    "position r the pivot. Nothing in the invariant orders the keys inside a "
                    "region."},
        ],
        "mistakes": [
            ("Thinking partition sorts the two sides",
             "Partition guarantees one thing: the pivot is in its final position, with nothing "
             "larger before it and nothing smaller after it. Inside each side the order is "
             "whatever the exchanges left. On the lesson's array the pivot 18 ends at position 6 "
             "with `7, 12, 4, 15, 9` before it, not sorted, and the lab's status line says so. "
             "Sorting the sides is the recursion's work."),
            ("Treating the worst case as a rare accident",
             "With the last key as pivot, the worst case is triggered by an input that is "
             "already sorted, or sorted in reverse, which in practice is common: data often "
             "arrives sorted or nearly so. The authors note the irony that this is where "
             "insertion sort is fastest. In the worked example, the sorted arrangement of seven "
             "keys costs 21 comparisons, the most any arrangement can."),
            ("Believing only an even split gives n lg n",
             "Section 7.2's 9-to-1 example shows the depth stays `Θ(lg n)` for any split of "
             "constant proportion, so the running time stays `O(n lg n)` with a larger "
             "constant. What ruins quicksort is a split that leaves only a constant number of "
             "keys on one side, level after level."),
        ],
        "standard": (
            "Finish when you can partition by hand and price a run by its splits.",
            "Given eight keys, carry PARTITION through with the four regions marked, and write "
            "and solve the recurrence for a run whose splits are all n − 1 to 0, all even, or "
            "all of one constant proportion."
        ),
        "note": (
            "The lab runs one partition, not a whole sort, so the counts for whole runs in the "
            "worked example and the quiz are done by hand. Its comparison count, n − 1, is the "
            "same for every array of a given length; its exchange count and the split depend on "
            "the keys. The running times of Section 7.2 are statements about the shapes of "
            "splits, for every input that produces them."
        ),
    },
    # ---------------------------------------------------------------- 04
    # CLRS sections 7.3-7.4, pp. 179-190.
    # Quote: p. 179, 13 words, quotes.py OK. Lesson total: 13 words.
    # Random sampling, RANDOMIZED-PARTITION and RANDOMIZED-QUICKSORT
    # (pp. 179-180); worst-case analysis by substitution, q^2 + (n-q-1)^2
    # (pp. 180-181); expected running time: Lemma 7.1, X_ij, each pair
    # compared at most once, Pr = 2/(j-i+1), the harmonic bound (pp. 181-184).
    # The closed form 2(n+1)H_n - 4n is the lab's exact evaluation of the
    # book's sum, and the prose says the book bounds the sum instead.
    {
        "slug": "analysis-of-randomized-quicksort",
        "title": "Randomized Quicksort and Its Analysis",
        "module": "Chapter 7 · Quicksort",
        "one_line": "Choose the pivot at random and no input is bad any more: two keys are compared with probability 2/(j − i + 1), and summing those probabilities gives O(n lg n) expected comparisons on every input.",
        "summary": (
            "Sections 7.3 and 7.4 make quicksort choose its pivot at random, prove that the "
            "worst case is still Θ(n²), and then compute the expected number of comparisons "
            "with one indicator variable per pair of keys. The pair of the ith and jth smallest "
            "keys is compared exactly when one of them is the first pivot chosen between them, "
            "with probability 2/(j − i + 1). Evaluate the sum by hand at n = 7, and see the lab "
            "reach the same fraction three ways, on every input it offers."
        ),
        "key": [
            "pick the pivot uniformly at random",
            "no input elicits the worst case",
            "each pair is compared at most once",
            "Pr{zᵢ meets zⱼ} = 2/(j − i + 1)",
            "sum over all pairs: O(n lg n)",
            "the expectation is over the pivots",
        ],
        "key_label": "Sections 7.3 and 7.4 in six lines",
        "concepts_intro": (
            "Three ideas carry the analysis. The second is the trick that makes it short: "
            "count comparisons pair by pair instead of call by call."
        ),
        "concepts": [
            ("Random sampling",
             "RANDOMIZED-PARTITION exchanges `A[r]` with an element chosen uniformly at random "
             "from `A[p..r]` before calling PARTITION, so every key of the subarray is equally "
             "likely to be the pivot. The input is not shuffled; the randomness is the "
             "algorithm's own."),
            ("The indicator for a pair",
             "Rename the keys `z₁, …, zₙ` in sorted order. `Xᵢⱼ` is 1 if `zᵢ` and `zⱼ` are "
             "compared at any time during the run and 0 if not. Their sum is the total number "
             "of comparisons X, and by linearity of expectation `E[X]` is the sum of the "
             "probabilities."),
            ("The set between two keys",
             "`Zᵢⱼ` is the set `zᵢ, zᵢ₊₁, …, zⱼ`, with `j − i + 1` elements. It stays together "
             "in one subarray until the first time a pivot is chosen from it, and that first "
             "choice decides whether `zᵢ` and `zⱼ` ever meet."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 7.3 and 7.4 in your own copy first. The lesson sets out the "
            "randomized algorithm and both analyses in its own words, evaluates the expectation "
            "by hand at n = 7, and then compares it with the lab's exact fractions and with a "
            "mean over seeded runs."
        ),
        "body": [
            ("p", "Section 7.2's intuition about average behaviour assumed that every ordering "
                  "of the input is as likely as any other. &ldquo;In an engineering situation, however, "
                  "we cannot always expect this assumption to hold.&rdquo; So Section 7.3 stops "
                  "assuming anything about the input and puts the randomness inside the "
                  "algorithm. This lesson reads sections 7.3 and 7.4: the randomized quicksort, "
                  "its worst case, and the expected number of comparisons, computed exactly."),
            ("p", "The change is two lines. Instead of always taking `A[r]`, RANDOMIZED-PARTITION "
                  "first exchanges `A[r]` with a key chosen at random from `A[p..r]`, then calls "
                  "PARTITION as before; RANDOMIZED-QUICKSORT calls it in place of PARTITION. "
                  "Section 5.3 randomized by permuting the whole input, and that would work here "
                  "too, but the authors prefer random sampling because its analysis is simpler. "
                  "Now no particular input is the bad one: a sorted array is exactly as likely to "
                  "be split well as any other."),
            ("p", "Section 7.4.1 settles the worst case first, for any choice of pivots. The "
                  "recurrence takes the worst split at every level, "
                  "`T(n) = max over q of (T(q) + T(n − q − 1)) + Θ(n)`. Guessing `T(n) ≤ cn²` "
                  "and substituting leaves the expression `q² + (n − q − 1)²` to maximize, and it "
                  "is largest at the ends, q = 0 or q = n − 1, which gives `O(n²)`; Section 7.2's "
                  "sorted input shows it is reached. Randomization does not remove the worst "
                  "case. It removes every input's power to force it."),
            ("p", "Section 7.4.2 counts comparisons, because the running time is "
                  "`O(n + X)` where X is the number of comparisons made in PARTITION's loop over "
                  "the whole run (Lemma 7.1): there are at most n calls of PARTITION, each "
                  "doing constant work plus its loop. Rather than count call by call, the "
                  "authors count pair by pair. Every comparison is between a pivot and another "
                  "key of the same call, and a pivot never appears in a later call, so each pair "
                  "of keys is compared at most once. The total X is therefore the sum of the "
                  "indicators `Xᵢⱼ` over all pairs `i < j`."),
            ("thm", ("When two keys meet",
                     "Assume the keys are distinct. `zᵢ` and `zⱼ` meet exactly when "
                     "the first pivot chosen from `Zᵢⱼ` is `zᵢ` or `zⱼ`. Each of the "
                     "`j − i + 1` keys of `Zᵢⱼ` is equally likely to be that first pivot, so "
                     "`Pr{zᵢ is compared to zⱼ} = 2/(j − i + 1)`.")),
            ("proof", ("Until a pivot is chosen from `Zᵢⱼ`, all of it lies in one subarray, "
                       "because any earlier pivot is either below `zᵢ` or above `zⱼ` and sends "
                       "the whole set to the same side.",
                       "If the first pivot from the set lies strictly between `zᵢ` and `zⱼ`, "
                       "the two go to different sides and are never in the same call again, so "
                       "they are never compared. If it is `zᵢ` or `zⱼ`, that key is compared with "
                       "every other key of its call, the other one included.",
                       "The pivot of the call is uniform over the call's keys, so, given that it "
                       "falls in `Zᵢⱼ`, it is uniform over `Zᵢⱼ`. Two of its `j − i + 1` members "
                       "give a comparison, and the two events are exclusive.")),
            ("p", "By linearity of expectation, which needs no independence, and the `Xᵢⱼ` are "
                  "far from independent, `E[X]` is the sum of `2/(j − i + 1)` over all pairs. "
                  "The authors substitute `k = j − i`, bound the inner sum by the harmonic series "
                  "`O(lg n)` and conclude `E[X] = O(n lg n)`; with Section 7.2's best case this "
                  "makes the expected time `Θ(n lg n)`. The sum can also be evaluated exactly. "
                  "Grouping the pairs by `d = j − i`, there are `n − d` pairs at distance d, and "
                  "the total comes to `2·(n + 1)·Hₙ − 4n`, where `Hₙ = 1 + 1/2 + … + 1/n`. The "
                  "book does not need that closed form, but the lab prints it."),
            ("math", [
                "E[X] at n = 7, pairs grouped by distance d = j − i",
                "",
                "d    pairs    each 2/(d + 1)    subtotal",
                "1      6          1              6",
                "2      5          2/3            10/3",
                "3      4          1/2            2",
                "4      3          2/5            6/5",
                "5      2          1/3            2/3",
                "6      1          2/7            2/7",
                "                                 ----",
                "                                 472/35 = 13.4857",
            ]),
            ("p", "Now the lab, which is the Algorithms Subject's lab for its lesson Randomised "
                  "Quicksort, where this analysis is practised further. It runs randomized "
                  "quicksort on an array of n keys under a series of seeds. Its tiles are "
                  "`2·(n + 1)·Hₙ − 4n` to four places, the mean comparison count over the seeds, "
                  "the difference between the two, and `Hₙ` as an exact fraction. Below them a "
                  "table gives the expectation three ways: from the closed form, from the "
                  "recurrence for the expected count solved step by step, and by averaging over "
                  "every possible sequence of pivot choices on the array on screen, each "
                  "weighted by its probability."),
            ("p", "The lesson's setting is 7 keys in a seeded shuffle, 200 seeds from seed 4. "
                  "The closed form is `472/35 = 13.4857`, the table above, with `H₇ = 363/140`. "
                  "The recurrence gives `472/35`. All 429 pivot sequences on the shuffled array "
                  "average `472/35`, and the same is true of the sorted array, the reversed one, "
                  "and an array built to defeat a median-of-three pivot: a different array, the "
                  "same fraction. The mean over 200 seeds is `13.7150`, 0.2293 above it, because "
                  "200 runs are a sample of the 429 possibilities, not all of them."),
            ("h3", "Exercise"),
            ("p", "At n = 5, compute `E[X]` by grouping the pairs by distance, as the table above "
                  "does at n = 7. Check your fraction against `2·(n + 1)·Hₙ − 4n`, then set the "
                  "lab to 5 keys and read the first row of its table."),
            ("p", "Quicksort's comparisons are bounded below as well as above, and not just for "
                  "quicksort. The next lesson, The Sorting Lower Bound and Counting Sort, proves "
                  "that every comparison sort needs `Ω(n lg n)` comparisons, and then sorts "
                  "without comparing at all."),
        ],
        "lab": ("sortkit", {
            "mode": "expected",
            "n": 7,
            "trials": 200,
            "input": "shuffle",
            "seed": 4,
            "panel_title": "The expected comparisons, exactly, and a mean over seeds",
            "panel_intro": (
                "The closed form uses an exact harmonic number, so the expectation is a fraction. "
                "The recurrence and the average over every pivot sequence compute it again by "
                "other routes. The mean over the seeds is a sample, and it is the only row that "
                "moves when you change the first seed."
            ),
        }),
        "steps_title": "Computing the expected comparisons",
        "steps_intro": "Four steps that turn the theorem into a number, and one on a size of your own.",
        "steps": [
            ("Name the keys by rank",
             "Call the smallest `z₁` and the largest `zₙ`. The input order no longer matters: "
             "the analysis is about ranks and random pivots."),
            ("Group the pairs by distance",
             "For each `d` from 1 to `n − 1`, there are `n − d` pairs with `j − i = d`, and each "
             "is compared with probability `2/(d + 1)`."),
            ("Add the subtotals as fractions",
             "Multiply each count by its probability and add exactly. Keep fractions; a "
             "decimal hides whether you have the right sum."),
            ("Check against the closed form",
             "Compute `Hₙ` as a fraction and evaluate `2·(n + 1)·Hₙ − 4n`. The two must agree "
             "exactly."),
            ("Do it at a size of your own",
             "Pick n = 6 or n = 8, compute the expectation by hand, then set the lab to that "
             "size and two different input orders and confirm that the exact rows do not "
             "change."),
        ],
        "worked": {
            "title": "Three keys, every pivot sequence",
            "intro": [
                "At n = 3 every run can be listed. The first pivot is `z₁`, `z₂` or `z₃`, each "
                "with probability 1/3.",
            ],
            "lines": [
                "pivot z₂ first: 2 comparisons, done",
                "pivot z₁ first: 2, then 2 keys left: 1",
                "pivot z₃ first: 2, then 2 keys left: 1",
                "E[X] = (2 + 3 + 3)/3 = 8/3",
                "by pairs: 1 + 1 + 2/3 = 8/3",
                "closed form: 2·4·(11/6) − 12 = 8/3",
            ],
            "after": [
                "Listing runs and summing pair probabilities give the same 8/3, and the pair "
                "view tells you why: `z₁` and `z₃` meet only if one of them is chosen before "
                "`z₂`, which happens with probability 2/3. The lab's third row does the listing "
                "at larger n, which is how it can be exact.",
            ],
        },
        "quiz_title": "Indicators, probabilities and samples",
        "quiz": [
            {"q": "What is the expected number of comparisons randomized quicksort makes on 5 "
                  "distinct keys?",
             "a": ["`37/5 = 7.4`", "10", "`29/6`", "`472/35`"],
             "c": 0,
             "why": "By distance: 4 pairs at d = 1 give 4, 3 at d = 2 give 3 · 2/3 = 2, 2 at d = 3 "
                    "give 2 · 1/2 = 1, and 1 at d = 4 gives 2/5; the total is 37/5. The closed "
                    "form agrees: `H₅ = 137/60` and `2 · 6 · 137/60 − 20 = 37/5`. Ten is "
                    "`n·(n − 1)/2`, every pair compared, the worst case. 29/6 is the value at n = 4 "
                    "and 472/35 the value at n = 7."},
            {"q": "In randomized quicksort on distinct keys, what is the probability that the "
                  "2nd smallest and the 6th smallest keys are ever compared?",
             "a": ["`1/5`", "`2/5`", "`1/3`", "`1/2`"],
             "c": 1,
             "why": "Here i = 2 and j = 6, so `Zᵢⱼ` has `6 − 2 + 1 = 5` keys, and the two are "
                    "compared exactly when one of those two is the first of the five chosen as a "
                    "pivot: 2/5. One fifth counts only one of the two keys. One third uses "
                    "`2/(j − i + 2)`. One half ignores the three keys between them."},
            {"q": "In the lab at n = 7, the mean over 200 seeds is 13.7150 while the closed form "
                  "is 13.4857. What explains the difference?",
             "a": ["The closed form is asymptotic and is only approximate at small n",
                   "A shuffled array is a harder input than average for randomized quicksort",
                   "The 200 seeded runs are a sample of the possible pivot sequences; the "
                   "average over all of them is exactly 472/35",
                   "The lab counts the comparisons that choose the pivot, which the formula "
                   "leaves out"],
             "c": 2,
             "why": "The table's third row averages over every pivot sequence on the shuffled "
                    "array and gets exactly 472/35, the closed form's value, so the formula is "
                    "exact at n = 7 and this array is not harder: the sorted and reversed arrays "
                    "give the same fraction. The random pivot is chosen without comparisons. "
                    "What remains is sampling, and changing the first seed moves only that row."},
            {"q": "Why is each pair of keys compared at most once in a run of quicksort?",
             "a": ["Every comparison involves the pivot of a call, and a pivot is never part of "
                   "any later call",
                   "PARTITION compares each key with its neighbour once",
                   "The keys are distinct",
                   "The pivot is chosen at random"],
             "c": 0,
             "why": "Comparisons happen only between the current pivot and the other keys of its "
                    "call, and once PARTITION places the pivot it is excluded from both recursive "
                    "calls, so it can never meet any key again. This holds for the deterministic "
                    "quicksort too, so randomness is not the reason, and distinctness is needed "
                    "for the probability, not for this fact. PARTITION compares keys with the "
                    "pivot, not with neighbours."},
        ],
        "mistakes": [
            ("Reading the expectation as an average over inputs",
             "Section 7.2's intuition averaged over random inputs, and it is natural to read "
             "Section 7.4's result the same way, so that some unlucky input could still be slow "
             "on average. It cannot: the expectation is over the algorithm's own pivot choices "
             "and holds for every input. In the lab at n = 7, the average over every pivot "
             "sequence is `472/35` on the shuffled, sorted, reversed and adversarial arrays "
             "alike."),
            ("Believing randomization removes the worst case",
             "Section 7.4.1 proves the worst case is still `Θ(n²)`: an unlucky run of pivot "
             "choices produces the same splits a sorted input does under the deterministic "
             "rule. What changes is that no input causes it; it happens only with small "
             "probability, on any input. At n = 7 the worst run still makes 21 comparisons."),
            ("Thinking linearity of expectation needs independent indicators",
             "The indicators are strongly dependent: whether `z₁` meets `z₃` depends on what "
             "happened to `z₂`. Linearity of expectation holds anyway, for any random variables, "
             "and that is what lets the authors add the pair probabilities without tracing "
             "how the calls unfold."),
        ],
        "standard": (
            "Finish when you can compute the expected comparisons at a small n.",
            "For n up to 8, compute `E[X]` exactly by grouping pairs by distance, check it "
            "against the closed form, and explain why it does not depend on the input order."
        ),
        "note": (
            "The lab's exact rows are exact only because n is small enough to enumerate every "
            "pivot sequence, which it does up to 10 keys. The mean over seeds is one sample. "
            "The `O(n lg n)` bound on the expectation, for every n and every input of distinct "
            "keys, is the book's proof; the lab shows it at the sizes it can count."
        ),
    },
    # ---------------------------------------------------------------- 05
    # CLRS Chapter 8 opening and sections 8.1-8.2, pp. 191-197.
    # Quote: p. 191, 14 words, quotes.py OK. Lesson total: 14 words.
    # Comparison sorts and the three linear sorts (p. 191); decision trees,
    # leaves and reachable permutations (pp. 191-193); Theorem 8.1 and
    # Corollary 8.2 (pp. 193-194); COUNTING-SORT, Theta(k + n), stability and
    # why it matters for radix sort (pp. 194-196).
    {
        "slug": "lower-bounds-and-counting-sort",
        "title": "The Sorting Lower Bound and Counting Sort",
        "module": "Chapter 8 · Sorting in Linear Time",
        "one_line": "Any sort that learns about its keys only by comparing them needs lg(n!) comparisons on some input, which is Ω(n lg n); counting sort escapes by using the keys as array indexes.",
        "summary": (
            "Section 8.1 models every comparison sort as a binary decision tree with a leaf for "
            "each of the n! orderings, so its worst case is at least lg(n!), which is Ω(n lg n): "
            "merge sort and heapsort are asymptotically optimal. Section 8.2's counting sort "
            "tallies small integer keys, turns the tallies into positions and places each key, "
            "in Θ(n + k) time and stably. Compute the bound for small n, then count ten keys in "
            "the lab and break their stability by placing them in the wrong direction."
        ),
        "key": [
            "a comparison sort is a decision tree",
            "n! orderings need n! reachable leaves",
            "height at least lg(n!), so Ω(n lg n)",
            "counting sort reads keys, not order",
            "tally, prefix-sum, place from the back",
            "Θ(n + k), and stable",
        ],
        "key_label": "Sections 8.1 and 8.2 in six lines",
        "concepts_intro": (
            "Three ideas: the class of algorithms the bound is about, the model that proves "
            "it, and the property of counting sort the next lesson depends on."
        ),
        "concepts": [
            ("Comparison sort",
             "A sort that gains information about the order of its keys only by comparing "
             "pairs of them. It may not inspect a key's value in any other way. Insertion sort, "
             "merge sort, heapsort and quicksort are all comparison sorts."),
            ("Decision tree",
             "A full binary tree describing every run of one comparison sort on n keys. Each "
             "internal node is a comparison of two positions, its two subtrees are the runs "
             "after each answer, and each leaf is the ordering the sort outputs. The worst-case "
             "number of comparisons is the tree's height."),
            ("Stable",
             "A sort is stable if keys with equal values leave in the same relative order as "
             "they arrived. It matters when keys carry other data with them, and Section 8.3's "
             "radix sort depends on it."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the opening of Chapter 8 and sections 8.1 and 8.2 in your own copy first. "
            "The lesson sets out the lower-bound argument and counting sort in its own words, "
            "computes the bound for small n, and then runs counting sort in the lab."
        ),
        "body": [
            ("p", "Every sort so far shares one property: &ldquo;the sorted order they determine "
                  "is based only on comparisons between the input elements.&rdquo; The authors "
                  "call such algorithms comparison sorts, and the opening of Chapter 8 announces "
                  "both halves of the chapter: a proof that no comparison sort can beat "
                  "`Ω(n lg n)` comparisons in the worst case, and three sorts that run in linear "
                  "time because they are not comparison sorts. This lesson reads Section 8.1, the "
                  "proof, and Section 8.2, the first of the three."),
            ("p", "Section 8.1 assumes the keys are distinct, so that a test for equality is "
                  "useless and every remaining test, less-than or at-most and their mirror "
                  "images, yields the same information. A comparison sort on n keys can then be "
                  "drawn as a decision tree. Its root is the first comparison the algorithm "
                  "makes; the answer sends the run left or right to the next comparison; and a "
                  "leaf records the permutation the algorithm has determined. One run of the "
                  "sort is one path from the root to a leaf."),
            ("p", "A correct sort must be able to produce every one of the n! permutations, "
                  "since each is the right answer for some input, so each must appear at a "
                  "reachable leaf. The length of the longest path is the number of comparisons "
                  "the sort makes in its worst case. A lower bound on the height of every such "
                  "tree is therefore a lower bound on the worst case of every comparison sort, "
                  "including ones nobody has written yet."),
            ("thm", ("Theorem 8.1, in short",
                     "Every comparison sort makes `Ω(n lg n)` comparisons on its worst input. "
                     "A binary tree of height h has at most `2ʰ` leaves, and the tree needs at "
                     "least `n!`, so `2ʰ ≥ n!` and `h ≥ lg(n!)`, which is `Ω(n lg n)` by "
                     "Stirling's approximation (equation 3.19).")),
            ("p", "Corollary 8.2 draws the consequence: heapsort and merge sort, whose upper "
                  "bounds are `O(n lg n)`, are asymptotically optimal comparison sorts. Nothing "
                  "that only compares can do better than a constant factor. Because h is a whole "
                  "number of comparisons, the exact form of the bound for a given n is "
                  "`⌈lg(n!)⌉`: 3 for three keys, 5 for four, 7 for five, 22 for ten."),
            ("p", "Section 8.2's counting sort assumes instead that each key is an integer from "
                  "0 to k. It uses an output array B and a working array `C[0..k]`. First it "
                  "counts how many keys equal each value. Then it adds the counts up from the "
                  "left, so that `C[i]` becomes the number of keys at most i, which is the last "
                  "output position a key of value i may take. Finally it walks the input from the "
                  "last key to the first, writes each key at the position its counter names and "
                  "decrements the counter, so the next equal key goes one place to the left."),
            ("def", ("Counting sort's cost",
                     "The tally and the placement each take `Θ(n)`, and clearing and summing C "
                     "take `Θ(k)`, so counting sort runs in `Θ(n + k)` time. When `k = O(n)` "
                     "that is `Θ(n)`, below the comparison bound, which does not apply: the "
                     "algorithm never compares two keys, and uses their values as indexes.")),
            ("p", "The walk from the back is what makes counting sort stable. Among keys of one "
                  "value the last to arrive is placed first, in the rightmost of their "
                  "positions, and each earlier one goes just to its left, so equal keys keep "
                  "their input order. The authors stress why this matters: when keys carry "
                  "satellite data, and above all when counting sort is the inner step of radix "
                  "sort in the next lesson."),
            ("p", "Now the lab, also the lab of the Algorithms Subject's lesson Counting Sort, "
                  "where more practice waits. It tallies the keys you type, forms the prefix sums "
                  "and places each key, keeping a tag that records where it started. Its tiles "
                  "are the work `n + k`, the comparison bound `⌈lg(n!)⌉` for the same n, the "
                  "writes into the output, and the number of pairs of equal keys left out of "
                  "input order. One difference of notation: where the book's keys run from 0 to k, "
                  "the lab's k is the number of possible values, the book's k + 1, and its "
                  "table numbers output slots from 0, so the book's position 5 is the lab's slot 4."),
            ("p", "The lesson's keys are `3, 0, 5, 2, 3, 5, 1, 0, 3, 4`: ten keys over the six "
                  "values 0 to 5. The work is 16, against a bound of 22 comparisons that any "
                  "comparison sort must reach on some input of ten keys. There are 10 writes and "
                  "no pairs reordered. Switch the placement pass to run from the front with the "
                  "same bookkeeping, and 5 pairs of equal keys come out reversed: three among the "
                  "three 3s, one among the 0s and one among the 5s. Then declare a 16-bit range: "
                  "the work becomes 65 546 for the same ten keys, because k, not n, now dominates "
                  "the sum."),
            ("h3", "Exercise"),
            ("p", "Sort `[2, 4, 1, 2, 0, 4, 2, 1]` by counting sort with k = 4. Write the tally "
                  "array, the prefix sums, and the output position each key takes as the input "
                  "is walked from the back. Then check by tags that the three 2s keep their "
                  "order."),
            ("p", "Counting sort is fast only when the range of keys is small. The next lesson, "
                  "Radix Sort and Bucket Sort, sorts large keys by running it once per digit, "
                  "and stability is what makes that work."),
        ],
        "lab": ("sortkit", {
            "mode": "counting",
            "keys": "3, 0, 5, 2, 3, 5, 1, 0, 3, 4",
            "range": "0",
            "direction": "backward",
            "panel_title": "Count, sum and place ten keys",
            "panel_intro": (
                "The tallies and prefix sums are computed from the keys you type, and each key "
                "is placed with a tag recording where it started. The declared range changes "
                "only the k in n + k, which is the term that decides whether counting sort is "
                "worth running."
            ),
        }),
        "steps_title": "Counting sort by hand",
        "steps_intro": "Three arrays on paper: the input, the counters and the output.",
        "steps": [
            ("Tally the keys",
             "Set `C[0..k]` to zero and add one to `C[v]` for each key v."),
            ("Turn tallies into positions",
             "Replace each `C[i]` by `C[0] + … + C[i]`, the number of keys at most i: the last "
             "output position free for value i."),
            ("Place from the back",
             "Walk the input from its last key to its first. Write each key v at position "
             "`C[v]` of the output and decrease `C[v]` by one."),
            ("Check stability and cost",
             "Equal keys must appear in the output in their input order. Count the work as n "
             "for each pass over the keys and k + 1 for each pass over the counters."),
            ("Do it on keys of your own",
             "Type twelve keys of your own from 0 to 7 into the lab, predict the prefix-sum "
             "column before you look, then switch the placement to the front and count the "
             "reordered pairs by hand before reading the tile."),
        ],
        "worked": {
            "title": "Ten keys, counted and placed",
            "intro": [
                "Sort the lab's keys `3, 0, 5, 2, 3, 5, 1, 0, 3, 4` with k = 5.",
            ],
            "lines": [
                "value    0  1  2  3  4  5",
                "tally    2  1  1  3  1  2",
                "prefix   2  3  4  7  8  10",
                "from the back: 4 to 8, 3 to 7, 0 to 2,",
                "  1 to 3, 5 to 10, 3 to 6, 2 to 4,",
                "  5 to 9, 0 to 1, 3 to 5",
                "output: 0 0 1 2 3 3 3 4 5 5",
            ],
            "after": [
                "The three 3s started at positions 1, 5 and 9 and land in positions 5, 6 and 7 "
                "in that order: stable. No two keys were compared. Against that, the decision-tree "
                "bound for ten keys is `⌈lg(10!)⌉ = ⌈lg 3 628 800⌉ = 22`, a bound on comparison "
                "sorts this algorithm is simply not one of.",
            ],
        },
        "quiz_title": "The bound and the sort outside it",
        "quiz": [
            {"q": "Counting sort on the exercise keys `[2, 4, 1, 2, 0, 4, 2, 1]` with k = 4: what "
                  "is the counter array `C[0..4]` after the prefix sums?",
             "a": ["`[1, 3, 6, 6, 8]`", "`[1, 2, 3, 0, 2]`", "`[0, 1, 3, 6, 6]`",
                   "`[1, 3, 6, 8, 8]`"],
             "c": 0,
             "why": "The tallies are one 0, two 1s, three 2s, no 3s and two 4s, which is "
                    "`[1, 2, 3, 0, 2]`, the second option, before summing. Adding from the left "
                    "gives `[1, 3, 6, 6, 8]`: value 3 has no keys, so its entry repeats value 2's. "
                    "`[0, 1, 3, 6, 6]` counts the keys strictly less than each value. "
                    "`[1, 3, 6, 8, 8]` drops the empty value 3 and shifts the 4s left."},
            {"q": "By the decision-tree argument, at least how many comparisons must any "
                  "comparison sort make on its worst input of 5 keys?",
             "a": ["5", "7", "10", "12"],
             "c": 1,
             "why": "There are `5! = 120` orderings, and a binary tree of height 6 has only 64 "
                    "leaves, so the height is at least `⌈lg 120⌉ = 7`. Five is the number of "
                    "keys. Ten is `n·(n − 1)/2`, the number of pairs. Twelve rounds up "
                    "`n·lg n ≈ 11.6`, the order of growth rather than the bound."},
            {"q": "Why does counting sort's `Θ(n + k)` not contradict Theorem 8.1?",
             "a": ["Theorem 8.1 is about the average case, and counting sort's bound is its "
                   "worst case",
                   "Counting sort never compares two keys; it uses their values as array "
                   "indexes, so it is not a comparison sort",
                   "Theorem 8.1 assumes distinct keys, and counting sort is only used on keys "
                   "with repeats",
                   "When k is small, `Θ(n + k)` is really `Θ(n lg n)`"],
             "c": 1,
             "why": "The theorem bounds algorithms that learn the order only by comparing, and "
                    "counting sort learns it by indexing with the keys. The theorem is a "
                    "worst-case bound, not an average one. Counting sort works on distinct keys "
                    "too. With small k the time is linear, not `n lg n`."},
            {"q": "Counting sort is run on n keys whose values range from 0 to `n²`. What is its "
                  "running time?",
             "a": ["`Θ(n)`", "`Θ(n lg n)`", "`Θ(n²)`", "`Θ(n + lg n)`"],
             "c": 2,
             "why": "With `k = n²`, `Θ(n + k) = Θ(n²)`: the passes over the counters dominate. "
                    "Linear time needs `k = O(n)`. Counting sort never takes `n lg n` time for "
                    "any reason of its own; that is the comparison sorts' figure. The range "
                    "enters the cost directly, not through its logarithm. Radix sort, in the "
                    "next lesson, is the way to handle such keys."},
        ],
        "mistakes": [
            ("Taking Ω(n lg n) as a bound on all sorting",
             "Theorem 8.1 is about comparison sorts: algorithms that learn the order only by "
             "comparing keys. The decision tree is a model of exactly that, and an algorithm "
             "that reads a key's value, as counting sort does, is not in the model. On the "
             "lesson's ten keys counting sort does 16 units of work and no comparisons, while "
             "every comparison sort needs 22 comparisons on its worst input of ten keys."),
            ("Reading the lower bound as a statement about every input",
             "The theorem bounds the worst case: the height of the tree, its longest path. "
             "Some leaves are shallow, so a comparison sort can be fast on particular inputs, "
             "as insertion sort is with n − 1 comparisons on sorted input. What no comparison "
             "sort can do is be fast on all inputs."),
            ("Calling counting sort linear without asking about k",
             "Its time is `Θ(n + k)`, linear in n only when k is `O(n)`. In the lab, declaring "
             "a 16-bit range turns 16 units of work into 65 546 for the same ten keys. The "
             "range of the keys is part of the input size, and here it is the larger part."),
        ],
        "standard": (
            "Finish when you can state the bound and run counting sort by hand.",
            "Compute `⌈lg(n!)⌉` for n up to 10 and say which algorithms it binds, and sort eight "
            "small integer keys by counting sort, showing the counters, the prefix sums and the "
            "placement, and checking stability."
        ),
        "note": (
            "The lab runs counting sort and prints the decision-tree bound beside it; it does "
            "not draw a decision tree or run a comparison sort. The bound `⌈lg(n!)⌉` is the "
            "book's theorem, true for every comparison sort on its worst input. The work and "
            "the reordered pairs are counts on the keys you typed."
        ),
    },
]
