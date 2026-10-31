"""Data Structures, lessons 1-5 -- Chapters 10, 11 and 12.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed.
(MIT Press, 2009): Chapter 10, Elementary Data Structures (pp. 232-252);
Chapter 11, Hash Tables (pp. 253-285); Chapter 12, Binary Search Trees
(pp. 286-307). Every quotation is copied from the operator's copy with its
printed page in the comment beside the lesson. The keys, tables and trees are
written for these lessons: none of the book's figures, examples or exercises
is reproduced, and its procedures are described in prose and named.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # CLRS Part III introduction (pp. 229-231) and Chapter 10, sections
    # 10.1-10.4, pp. 232-252.
    # Quote: p. 238, 13 words, quotes.py OK. Lesson total: 13 words.
    # Stacks, S.top, underflow and overflow (pp. 232-233); queues, head, tail,
    # wrap-around, n - 1 capacity (pp. 234-235); linked lists, LIST-SEARCH,
    # LIST-INSERT, LIST-DELETE (pp. 236-238); sentinels and their cost
    # (pp. 238-240); multiple-array and single-array objects, the free list
    # (pp. 241-245); rooted trees, left-child right-sibling (pp. 246-249).
    {
        "slug": "stacks-queues-and-linked-lists",
        "title": "Stacks, Queues and Linked Lists",
        "module": "Chapter 10 · Elementary Data Structures",
        "one_line": "A stack, a queue and a linked list are three ways to hold a changing set, and each makes some operations constant-time by giving up others; the cost of an operation belongs to a representation, not to the set.",
        "summary": (
            "Chapter 10 builds the simplest dynamic sets: a stack and a queue in an array, the "
            "doubly linked list with and without a sentinel, objects and pointers made out of "
            "plain arrays, and rooted trees with any number of children. Run a queue round its "
            "array by hand, then let the lab price one operation sequence on an array and on a "
            "linked list and show which operation decides between them."
        ),
        "key": [
            "a stack removes the newest element",
            "a queue removes the oldest element",
            "a queue in Q[1..n] holds n − 1 at most",
            "list search Θ(n); splice in or out O(1)",
            "a sentinel removes the boundary tests",
            "a free list hands out unused objects",
            "any tree fits two pointers per node",
        ],
        "key_label": "Chapter 10 in seven lines",
        "concepts_intro": (
            "Three ideas from the opening of Part III and Chapter 10. Every later structure in "
            "the course is described in their terms."
        ),
        "concepts": [
            ("Dynamic set",
             "A set that algorithms grow, shrink and query while they run. Each element has a "
             "key, which identifies it, and may carry satellite data, which travels with it. The "
             "operations split into queries, such as SEARCH, MINIMUM and SUCCESSOR, and "
             "modifying operations, INSERT and DELETE. A set that needs only insert, delete and "
             "search is a dictionary."),
            ("Stack and queue",
             "Two dynamic sets whose DELETE takes no argument because the element removed is "
             "fixed in advance: the most recently inserted for a stack (last in, first out), the "
             "longest present for a queue (first in, first out). Insert and delete are called "
             "PUSH and POP on a stack, ENQUEUE and DEQUEUE on a queue."),
            ("Sentinel",
             "A dummy object that stands where the list would otherwise point to nothing. A "
             "doubly linked list with one sentinel becomes a ring: the sentinel's next is the "
             "head, its previous is the tail, and no operation has to test whether it is at an "
             "end."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the introduction to Part III and Chapter 10 in your own copy first. The lesson "
            "sets out the four representations in its own words, runs a queue by hand, and then "
            "prices one operation sequence two ways in the lab."
        ),
        "body": [
            ("p", "&ldquo;A sentinel is a dummy object that allows us to simplify boundary "
                  "conditions.&rdquo; The authors say it in Section 10.2, and the sentence is a "
                  "fair summary of the chapter's method: each structure here is a small device "
                  "that makes some operation cheap or some code short, and each has a price "
                  "somewhere else. This lesson reads the introduction to Part III and the four "
                  "sections of Chapter 10."),
            ("p", "Part III opens with vocabulary rather than algorithms. A dynamic set changes "
                  "while an algorithm runs; its elements are objects with a key and perhaps "
                  "satellite data; and the operations on it fall into queries, which only look, "
                  "and modifying operations, which change it. The authors list seven of them, "
                  "SEARCH, INSERT, DELETE, MINIMUM, MAXIMUM, SUCCESSOR and PREDECESSOR, and say "
                  "that the time an operation takes is usually measured against the size of the "
                  "set. Every structure in this course is judged by which of those seven it does "
                  "quickly."),
            ("p", "Section 10.1 puts a stack in an array `S[1..n]` with one index, `S.top`. PUSH "
                  "increments it and stores; POP decrements it and returns the element above. "
                  "Each costs `O(1)`. Popping an empty stack is <em>underflow</em>, pushing past "
                  "n is <em>overflow</em>, and the book's code checks only the first. A queue "
                  "needs two indices: `Q.head`, the element to leave next, and `Q.tail`, the slot "
                  "the next arrival takes. Both move rightward and wrap from n back to 1, so the "
                  "array is used as a ring. Empty and full must look different, which is why one "
                  "slot is always left unused: the queue is empty when head equals tail and full "
                  "when the tail is one step behind the head, so `Q[1..n]` holds at most "
                  "n − 1 elements."),
            ("p", "Section 10.2 replaces index order with pointer order. In a doubly linked list "
                  "every element points to its successor and its predecessor, and `L.head` "
                  "points to the first. A list can also be singly linked, sorted, or circular. "
                  "LIST-SEARCH walks from the head and costs `Θ(n)` in the worst case. "
                  "LIST-INSERT splices a new element in at the front and costs `O(1)`. "
                  "LIST-DELETE splices an element out in `O(1)`, but only when it is handed a "
                  "pointer to the element; deleting by key means searching first, and then the "
                  "cost is `Θ(n)`. The distinction between an operation given a key and the same "
                  "operation given a pointer runs through the rest of the course."),
            ("def", ("Sentinel, as Section 10.2 uses it",
                     "An object `L.nil` with the same fields as a list element and no real key. "
                     "Every pointer that would be NIL points to it instead, so the list becomes "
                     "circular with `L.nil` between tail and head, and the empty list is the "
                     "sentinel pointing to itself. Insert and delete then lose their tests for "
                     "the first and last element.")),
            ("p", "The authors are careful about what the sentinel buys. It rarely changes an "
                  "asymptotic bound; in the list procedures it saves a constant number of tests, "
                  "and the gain is mostly clearer code. In a tight loop it can lower the "
                  "coefficient of the running time, which is the use Chapter 2's merge made of "
                  "it. It also costs one extra object per list, which matters when a program "
                  "keeps many short lists, so the book uses sentinels only where they make the "
                  "code simpler. Chapter 13's red-black trees are one such place."),
            ("p", "Section 10.3 asks what to do in a language without pointers, and answers with "
                  "arrays. In the multiple-array form, three arrays <em>next</em>, <em>key</em> "
                  "and <em>prev</em> hold one field each, and an object is an index into all "
                  "three. In the single-array form an object is a run of consecutive cells and a "
                  "pointer is the index of its first cell, with each field at a fixed offset. "
                  "Unused objects are kept on a singly linked <em>free list</em>, which is "
                  "worked as a stack: ALLOCATE-OBJECT pops an object off it and FREE-OBJECT "
                  "pushes one back, both in `O(1)`."),
            ("p", "Section 10.4 represents rooted trees. A binary tree node carries pointers to "
                  "its parent and its left and right children. A tree whose nodes may have any "
                  "number of children cannot reserve a field per child, so each node keeps just "
                  "two: its leftmost child and its next sibling to the right. That "
                  "<em>left-child, right-sibling</em> form stores any n-node rooted tree in "
                  "`O(n)` space. Chapters 12 to 14 build on the binary form."),
            ("p", "Now the lab, the one from the Algorithms Subject's lesson Arrays, Linked "
                  "Lists, and the Cost Model, where the comparison is practised further. It runs "
                  "one operation sequence on a dynamic array and on a doubly linked list with a "
                  "tail pointer and adds up a cost per operation in a stated model: reaching "
                  "index i of the array costs 1, reaching the i-th list node costs i + 1 hops, "
                  "inserting at the front of the array shifts every element, and deleting at a "
                  "position shifts the elements after it in the array but walks to it in the "
                  "list. That last rule prices LIST-DELETE as the book does when it is given a "
                  "position rather than a pointer: the splice is cheap, the walk is not."),
            ("p", "The tiles are the number of operations run, each representation's total, which "
                  "one was cheaper, the ratio of the two totals, and the kind of operation whose "
                  "two columns differ most, labelled decided by. The worked example "
                  "<code>four-operations</code> repeats index, insert at the front, insert at "
                  "the end and delete from the middle four times from 16 elements: 122 on the "
                  "array, 92 on the list, decided by the front insertions. "
                  "<code>front-insertions</code> is three front insertions and one index from 24 "
                  "elements: 370 against 78, the ratio 185/39. <code>random-access</code>, three "
                  "indexes and one insertion at the end, reverses it: 16 against 250, decided by "
                  "index. <code>scan-bound</code>, search and delete mixed in, gives 212 against "
                  "216, the ratio 53/54: when both must walk, the representation hardly "
                  "matters."),
            ("p", "Move the position slider in <code>random-access</code> to the front and the "
                  "list's total drops from 250 to 16, a tie: the same operations, reaching the "
                  "front instead of four fifths of the way along. A count is a fact about one "
                  "sequence at one position. The bounds in the chapter, `O(1)` for a splice and "
                  "`Θ(n)` for a search, hold for every list of n elements; the totals say what "
                  "one sequence cost."),
            ("h3", "Exercise"),
            ("p", "In the lab choose <code>front-insertions</code>, set the starting size to 8, "
                  "one round, and the position to halfway. Before reading the tiles, price each "
                  "of the four operations on both representations by hand, carrying the size "
                  "down as it grows, and add the columns. Then move the position to the back and "
                  "say which total changes, by how much, and why the other does not."),
            ("p", "A list finds a key by walking the whole of it. The next lesson, Direct "
                  "Addressing and Hashing with Chaining, uses the key to compute where to look, "
                  "and keeps short lists only for the keys that land in the same place."),
        ],
        "lab": ("seqkit", {
            "mode": "arraylist",
            "preset": "four-operations",
            "panel_title": "Price one sequence on an array and on a linked list",
            "panel_intro": (
                "Choose an operation sequence, a starting size, how many times it repeats and how "
                "far along the indexed operations reach. Each operation is costed on both "
                "representations in the lab's model, an array index at 1 and the i-th list node "
                "at i + 1, and the totals are counts of that one sequence, not bounds."
            ),
        }),
        "steps_title": "A queue round its array by hand",
        "steps_intro": "Four steps on a small array, then one on the lab.",
        "steps": [
            ("Draw the array and both indices",
             "Write the slots 1 to n in a row, mark the head and the tail, and start both at "
             "slot 1. The queue is empty while they are equal."),
            ("Enqueue at the tail",
             "Store the arrival in the tail's slot and move the tail one to the right, from n "
             "back to 1. Refuse the arrival if the tail would land on the head: the queue is "
             "full."),
            ("Dequeue at the head",
             "Take the element in the head's slot and move the head one to the right, wrapping "
             "the same way. Refuse if head equals tail: the queue is empty."),
            ("Read the queue off the ring",
             "The queue is the slots from the head up to the one before the tail, read with "
             "wrap-around. Check that their number never exceeds n − 1."),
            ("Price a sequence in the lab",
             "Choose <code>front-insertions</code> at 8 elements, one round, halfway: work the "
             "four costs by hand on both representations, then compare your two totals with the "
             "tiles."),
        ],
        "worked": {
            "title": "Nine operations on a queue of six slots",
            "intro": [
                "A queue in `Q[1..6]`, so it can hold five elements. Head and tail start at "
                "slot 1. Each line gives the operation and the indices after it.",
            ],
            "lines": [
                "enqueue 4, 8, 15, 16, 23:  head 1, tail 6",
                "tail + 1 = 7 wraps to 1 = head: full",
                "dequeue → 4:  head 2",
                "dequeue → 8:  head 3",
                "enqueue 42 in slot 6:  tail wraps to 1",
                "enqueue 7 in slot 1:  tail 2",
                "head 3, tail 2: full again",
                "queue, head first: 15 16 23 42 7",
            ],
            "after": [
                "The queue was full twice, both times holding five elements in six slots, and "
                "never with the tail on the head: had a sixth arrival been allowed, head and "
                "tail would have coincided and the full queue would have looked empty. That is "
                "why one slot is given up. Every operation moved one index by one slot, so each "
                "cost `O(1)` whatever the queue held.",
            ],
        },
        "quiz_title": "Stacks, queues, lists and their costs",
        "quiz": [
            {"q": "In the lab, <code>front-insertions</code> at a starting size of 8, one round, "
                  "the position halfway: three insertions at the front, then one index. What do "
                  "the array and the list cost in all?",
             "a": ["Array 31, list 9", "Array 27, list 9", "Array 31, list 14",
                   "Array 4, list 31"],
             "c": 0,
             "why": "The array shifts every element on a front insertion: 9, 10 and 11 at sizes "
                    "8, 9 and 10, then the index costs 1, for 31. The list splices each insertion "
                    "for 1, and at size 11 halfway is position 5, which costs 6 hops: 9 in all. "
                    "Twenty-seven forgets that the size grows between insertions. Fourteen is the "
                    "list's total with the position at the back, where the index costs 11. Four "
                    "is what the array would cost if a front insertion shifted nothing."},
            {"q": "A queue is kept in `Q[1..8]` by the head-and-tail method of Section 10.1. "
                  "What is the most elements it can hold?",
             "a": ["7", "8", "9", "4"],
             "c": 0,
             "why": "Empty is head equal to tail. If all eight slots could be filled, the tail "
                    "would come round onto the head and a full queue would look empty, so one "
                    "slot stays unused and the capacity is n − 1 = 7. Eight is the array's size, "
                    "not the queue's. Nine is impossible in eight slots, and four confuses the "
                    "ring with two stacks of half the size."},
            {"q": "You hold a pointer to an element x in a doubly linked list of n elements. "
                  "What does LIST-DELETE cost, and what would deleting by x's key cost?",
             "a": ["`O(1)` with the pointer; `Θ(n)` in the worst case by key, because the "
                   "element must be found first",
                   "`Θ(n)` either way, because the list must be walked to find x's predecessor",
                   "`O(1)` either way, because deletion only changes two pointers",
                   "`O(lg n)` by key, because the list can be searched by halving"],
             "c": 0,
             "why": "A doubly linked element knows its predecessor, so the splice changes two "
                    "pointers and costs `O(1)`. Given only a key, LIST-SEARCH must find the "
                    "element first, which is `Θ(n)` in the worst case. Walking for the "
                    "predecessor is the singly linked case. Changing two pointers is the splice "
                    "alone, not the search, and a list cannot be halved because reaching its "
                    "middle is itself a walk."},
            {"q": "What does a sentinel `L.nil` change about a doubly linked list's operations?",
             "a": ["It removes the special cases at the ends; the bounds stay `O(1)` for "
                   "insert and delete and `Θ(n)` for search",
                   "It makes search `O(1)`, because the sentinel points straight at the tail",
                   "It makes the list sorted, because the sentinel holds the smallest key",
                   "It saves memory, because the head pointer is no longer stored"],
             "c": 0,
             "why": "Every NIL becomes a pointer to `L.nil`, so the code no longer tests for the "
                    "first or last element; the authors note that this rarely changes an "
                    "asymptotic bound. Search still walks the list. The sentinel holds no real "
                    "key, so order is unchanged. And although `L.head` disappears, the sentinel "
                    "is a whole extra object per list, which is the memory cost the book warns "
                    "about for many small lists."},
        ],
        "mistakes": [
            ("Saying a linked list inserts in constant time, without saying where",
             "LIST-INSERT splices at the head in `O(1)`, and LIST-DELETE splices out in `O(1)` "
             "given a pointer. Neither covers inserting or deleting at a position or by key, "
             "which first needs a walk that costs `Θ(n)` in the worst case. In the lab, "
             "<code>scan-bound</code> mixes searches and deletes at a position, and the list's "
             "total, 216, is no better than the array's, 212. The cheap part of a list "
             "operation is the splice; reaching the place is the part that costs."),
            ("Filling every slot of a circular queue",
             "With head and tail alone, an empty queue and a full queue would both have the "
             "tail on the head. Section 10.1's queue therefore holds at most n − 1 elements in "
             "`Q[1..n]`. Keeping a separate count of elements is another way out, but it is a "
             "different structure from the book's, with one more field to keep right on every "
             "operation."),
            ("Expecting a sentinel to improve the bound",
             "The sentinel removes boundary tests. The authors say it rarely changes an "
             "asymptotic bound and mostly makes code clearer, and that it costs one extra "
             "object per list, which adds up when a program keeps many small lists. LIST-SEARCH "
             "with a sentinel still walks up to n elements."),
        ],
        "standard": (
            "Finish when you can run and price the chapter's structures by hand.",
            "Given a short sequence of operations, run it on a stack, an array queue or a doubly "
            "linked list, say the cost of each operation, and say which costs depend on being "
            "handed a pointer rather than a key."
        ),
        "note": (
            "The lab compares a dynamic array with a doubly linked list in one fixed cost model "
            "on four sequences it supplies; you choose the size, the repetitions and the "
            "position, not the operations. It does not run the array stack or queue, the "
            "objects built from arrays, or the tree representations; those are worked by hand "
            "here. Its totals describe one sequence, and the chapter's bounds hold for all."
        ),
    },
    # ---------------------------------------------------------------- 02
    # CLRS Chapter 11 opening and sections 11.1-11.2, pp. 253-262.
    # Quote: p. 253, 13 words, quotes.py OK. Lesson total: 13 words.
    # Dictionaries and the O(1) average (p. 253); direct-address tables and
    # their storage (pp. 254-256); hash functions, collisions, chaining and its
    # three operations (pp. 256-258); load factor, worst case, simple uniform
    # hashing, Theorems 11.1 and 11.2 and the 1 + alpha/2 - alpha/2n sum
    # (pp. 258-260); n = O(m) gives O(1) on average (p. 260).
    {
        "slug": "hash-tables",
        "title": "Direct Addressing and Hashing with Chaining",
        "module": "Chapter 11 · Hash Tables",
        "one_line": "A hash table computes where a key belongs instead of searching for it, keeps the keys that collide in short lists, and searches in Θ(1 + α) expected time when keys hash uniformly.",
        "summary": (
            "Sections 11.1 and 11.2 start from a table with one slot per possible key, where "
            "every operation is a single array access, and shrink it to a table sized for the "
            "keys actually stored, with a hash function choosing the slot and a linked list in "
            "each slot for the keys that collide. Hash ten keys by hand, then set the lab's "
            "measured chain lengths beside the load factor and the book's expectations."
        ),
        "key": [
            "direct addressing: one slot per key",
            "a hash table: one slot per m, not per key",
            "collisions go into a list per slot",
            "load factor α = n/m",
            "worst case: one chain of n, Θ(n)",
            "expected: Θ(1 + α), if keys hash uniformly",
        ],
        "key_label": "Sections 11.1 and 11.2 in six lines",
        "concepts_intro": (
            "Three ideas carry the first half of the chapter. The rest of it, and the next two "
            "lessons, refine the second and the third."
        ),
        "concepts": [
            ("Direct-address table",
             "An array `T[0..m − 1]` with one slot for every key in a universe `U` of size m. "
             "Slot k holds the element with key k or NIL, so search, insert and delete are each "
             "one array access. It works only when the universe is small enough to allocate."),
            ("Hash function and collision",
             "A function h from the universe to the slots 0 to m − 1, with m much smaller than "
             "the universe. A key k <em>hashes to</em> slot `h(k)`. Two keys that hash to the "
             "same slot collide, and since there are more keys than slots, some keys must."),
            ("Simple uniform hashing",
             "The assumption that each key lands in each of the m slots with probability 1/m, "
             "whichever slots the other keys took. It is an assumption about the keys "
             "and the function together, and the chapter's averages hold only under it."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the chapter opening and sections 11.1 and 11.2 in your own copy first. The "
            "lesson sets out chaining and its analysis in its own words, hashes ten keys by hand, "
            "and then sets the lab's measured chains beside the expectations."
        ),
        "body": [
            ("p", "&ldquo;The bottom line is that hashing is an extremely effective and practical "
                  "technique.&rdquo; The authors say it at the opening of Chapter 11, and qualify "
                  "it at once: the constant time is an average, and in the worst case a search "
                  "takes as long as in a linked list. This lesson reads the opening and sections "
                  "11.1 and 11.2: the table that needs no hashing, the table that does, and the "
                  "argument that puts the average at `Θ(1 + α)`."),
            ("p", "Section 11.1 begins where hashing is unnecessary. If keys come from a universe "
                  "`U = {0, 1, …, m − 1}` and m is modest, an array with one slot per key does "
                  "everything: DIRECT-ADDRESS-SEARCH, INSERT and DELETE each touch one slot in "
                  "`O(1)`. The trouble is size. The table needs a slot for every key that "
                  "<em>could</em> occur, and when the universe is large and the set of keys "
                  "actually stored is small, almost all of it is empty. A hash table keeps the "
                  "storage at `Θ(|K|)` for the stored keys K, and gives up the worst-case "
                  "`O(1)` for an average one."),
            ("p", "Section 11.2 makes the trade. A hash function maps the universe onto slots 0 "
                  "to m − 1, and the element with key k goes to slot `h(k)`. Because the "
                  "universe is larger than m, two keys can share a slot, and the chapter's first "
                  "remedy is <em>chaining</em>: each slot holds a linked list of the elements "
                  "that hash there. CHAINED-HASH-INSERT puts a new element at the head of its "
                  "list in `O(1)`, assuming it is not already present. CHAINED-HASH-SEARCH walks "
                  "one list, so its cost is that list's length. CHAINED-HASH-DELETE splices the "
                  "element out in `O(1)` when the lists are doubly linked and it is handed the "
                  "element, the distinction the last lesson drew."),
            ("def", ("Load factor",
                     "For a table of m slots holding n elements, `α = n/m`, the average number "
                     "of elements per chain. It can be below, equal to or above 1 under "
                     "chaining. Every average in the section is a function of α.")),
            ("p", "The worst case is plain: if all n keys hash to one slot, the table is one list "
                  "of length n and a search costs `Θ(n)`, plus the hashing. "
                  "Hashing is useful only because of the average, and the average depends on how "
                  "evenly the function spreads the keys. The authors take the simple uniform "
                  "hashing assumption, under which each chain's expected length is exactly α, "
                  "and assume the hash itself costs `O(1)`."),
            ("thm", ("Theorems 11.1 and 11.2",
                     "Under chaining and simple uniform hashing, an unsuccessful search and a "
                     "successful search each take `Θ(1 + α)` time on average. An unsuccessful "
                     "search examines every element of one chain, α on average. A successful "
                     "search for an element chosen uniformly from the n stored examines "
                     "`1 + (n − 1)/(2m)` elements on average, which is `1 + α/2 − α/(2n)`.")),
            ("p", "The successful case is the interesting proof. New elements go to the head of "
                  "their list, so the elements a search passes before reaching x are exactly "
                  "those inserted into x's slot after x. For the i-th and j-th keys inserted, an "
                  "indicator variable records whether they share a slot, with expectation 1/m. "
                  "Averaging one plus the later collisions over all n elements gives "
                  "`1 + (1/(n·m)) · Σ (n − i)`, and the sum of n − i for i from 1 to n is "
                  "`n·(n − 1)/2` (Appendix A). The 1 is the element itself; the rest is half "
                  "of the other keys' share of its slot. The consequence the section draws: if "
                  "the table grows with the keys, so that n is `O(m)`, then α is `O(1)` and "
                  "every dictionary operation runs in constant time on average."),
            ("p", "Now the lab, which hashes keys into chains and runs every search. It is the "
                  "lab of the Algorithms Subject's lesson Hashing with Chaining, where the same "
                  "table is practised further. You set m, the hash rule, and the keys: drawn "
                  "from a seeded stream, multiples of m, a run of consecutive numbers, or your "
                  "own. The tiles are the load factor; the expected elements examined in an "
                  "unsuccessful search, which is α; an expected successful cost; the measured "
                  "mean, found by searching for every stored key and counting the elements "
                  "examined; the longest chain; and the empty slots. The lab adds each key at "
                  "the end of its chain rather than the front, which leaves the total over a "
                  "chain, and so the mean, unchanged."),
            ("p", "One tile needs care. The lab's expected successful cost uses `α/(2m)` where "
                  "Theorem 11.2's sum gives `α/(2n)`, so it differs slightly from the book's "
                  "figure; compute the book's `1 + (n − 1)/(2m)` beside it yourself. On the "
                  "worked example <code>eight-slots</code>, twenty keys from the stream in "
                  "eight slots, α is 5/2, the book's successful expectation is 35/16, about "
                  "2.19, and the measured mean is 23/10 = 2.300, with a longest chain of 5 and "
                  "1 of 8 slots empty. On <code>half-full</code>, eight keys in sixteen slots, "
                  "α is 1/2, the book's figure 39/32, about 1.22, and the mean 9/8 = 1.125: "
                  "below the expectation this time, as a single small table can be."),
            ("p", "Then choose <code>degenerate</code>: twenty keys, every one a multiple of 8, "
                  "under `h(k) = k mod 8`. The load factor is still 5/2 and the expectations "
                  "have not moved, but every key is in slot 0, the longest chain is 20, 7 of 8 "
                  "slots are empty, and the mean is 21/2 = 10.500, which is `(1 + 2 + … + 20)/20`. "
                  "Nothing in the theorem is wrong. These keys break its assumption, and the "
                  "next lesson is about choosing a function that such keys cannot break. Switch "
                  "the rule to the multiplicative one and the same keys spread: a mean of 39/20, "
                  "with no slot empty."),
            ("h3", "Exercise"),
            ("p", "Hash the keys `3, 14, 25, 9, 20, 31, 6, 17` into m = 11 slots with "
                  "`h(k) = k mod 11`. Draw the chains, then compute the mean number of elements "
                  "examined over a successful search for each key, and set it beside "
                  "Theorem 11.2's `1 + (n − 1)/(2m)`. Type the keys into the lab as your own to "
                  "check, then change m to 8 and explain why the mean falls although α rises."),
            ("p", "Whether chaining is fast depends on the hash function. The next lesson, Hash "
                  "Functions and Universal Hashing, looks at the two standard ways to compute "
                  "one, and at choosing the function at random so that no set of keys is bad "
                  "for it."),
        ],
        "lab": ("hash", {
            "mode": "chaining",
            "preset": "eight-slots",
            "panel_title": "Hash keys into chains and search for every one",
            "panel_intro": (
                "Choose the number of slots, the hash rule and the keys, or type your own. Every "
                "chain is drawn and every stored key searched for with a counter. The load factor "
                "is an exact fraction; the mean and the longest chain are counts on these keys, "
                "and the book's expectation holds on average under simple uniform hashing."
            ),
        }),
        "steps_title": "Hashing with chaining by hand",
        "steps_intro": "Four steps on paper, then one in the lab.",
        "steps": [
            ("Compute every home slot",
             "Apply the hash function to each key and write the slot beside it. For "
             "`h(k) = k mod m` that is the remainder on division by m."),
            ("Build the chains in arrival order",
             "Put each key into its slot's list. The book adds at the head; adding at the tail "
             "gives the same total cost over a chain, so either will do for the mean."),
            ("Count the successful searches",
             "A key in position j of its chain costs j elements examined. A chain of length L "
             "costs `L·(L + 1)/2` over all its keys; add over the chains and divide by n."),
            ("Set the count beside the expectations",
             "Compute `α = n/m` for an unsuccessful search and `1 + (n − 1)/(2m)` for a "
             "successful one. The count is about these keys; the expectations are averages over "
             "keys that hash uniformly."),
            ("Do it on keys of your own",
             "Choose ten keys and a table size between 5 and 12, work the chains and the mean by "
             "hand, then set the lab's key set to the keys you type and check both."),
        ],
        "worked": {
            "title": "Ten keys in seven slots",
            "intro": [
                "Keys `10, 23, 5, 31, 18, 44, 2, 27, 39, 16`, in that order, with "
                "`h(k) = k mod 7`. Here n = 10 and m = 7.",
            ],
            "lines": [
                "slot 2: 23, 44, 2, 16     length 4",
                "slot 3: 10, 31            length 2",
                "slot 4: 18, 39            length 2",
                "slot 5: 5;  slot 6: 27    length 1 each",
                "slots 0 and 1 empty",
                "successful: (10 + 3 + 3 + 1 + 1)/10 = 9/5",
                "Theorem 11.2: 1 + 9/14 = 23/14 ≈ 1.64",
                "unsuccessful, expected: α = 10/7 ≈ 1.43",
            ],
            "after": [
                "The four keys in slot 2 cost 1, 2, 3 and 4 to find, ten in all; the two pairs "
                "cost three each; the singletons one each. The mean, 1.8, sits above the "
                "expectation 1.64 because slot 2 drew four keys where the average is under one "
                "and a half. Type the keys into the lab with m = 7 and the division rule: it "
                "prints 9/5, a longest chain of 4 and 2 of 7 slots empty.",
            ],
        },
        "quiz_title": "Load factors, chains and averages",
        "quiz": [
            {"q": "Hash `3, 14, 25, 9, 20, 31, 6, 17` into 11 slots with `h(k) = k mod 11`. "
                  "What is the mean number of elements examined over a successful search for "
                  "each key?",
             "a": ["15/8", "29/22", "8/11", "3/2"],
             "c": 0,
             "why": "The keys land in three chains: 3, 14, 25 in slot 3; 9, 20, 31 in slot 9; "
                    "6, 17 in slot 6. Finding them costs 1 + 2 + 3 twice and 1 + 2 once, 15 in "
                    "all, over 8 keys. 29/22 is Theorem 11.2's expectation `1 + 7/22` for keys "
                    "that hash uniformly, which these do not: they differ by multiples of 11. "
                    "8/11 is α, the unsuccessful expectation. 3/2 is the mean with m = 8, where "
                    "the same keys spread over five slots."},
            {"q": "A chained table has m = 20 slots and n = 50 keys, and simple uniform hashing "
                  "holds. On average, how many elements does an unsuccessful search examine?",
             "a": ["5/2", "1/2", "7/2", "50"],
             "c": 0,
             "why": "An unsuccessful search examines the whole of one chain, and each chain's "
                    "expected length is `α = n/m = 50/20 = 5/2`. The running time is "
                    "`Θ(1 + α)` once the hash is counted, but the elements examined are α. One "
                    "half inverts the ratio. Seven halves adds the one twice over. Fifty is the "
                    "worst case, every key in one chain, which the assumption makes unlikely but "
                    "does not forbid."},
            {"q": "Under chaining, what does CHAINED-HASH-DELETE cost if each chain is a singly "
                  "linked list and you hold a pointer to the element?",
             "a": ["As much as walking its chain to find the predecessor, so proportional to "
                   "the chain's length",
                   "`O(1)`, because only the element's own next pointer changes",
                   "`O(1)`, because the hash function locates the slot directly",
                   "`Θ(n)`, because every chain must be searched"],
             "c": 0,
             "why": "Splicing out x means changing its predecessor's next pointer, and a singly "
                    "linked x does not know its predecessor; finding it walks the chain. With "
                    "doubly linked chains the predecessor is at hand and the delete is `O(1)`, "
                    "which is why the book uses them. Changing x's own pointer does not remove "
                    "x. Hashing finds the slot, not the predecessor. Only x's own chain needs "
                    "walking, not all of them."},
            {"q": "On the lab's <code>degenerate</code> example the load factor is 5/2, the same "
                  "as on <code>eight-slots</code>, but the measured mean is 21/2. Which statement "
                  "is right?",
             "a": ["The keys are all multiples of 8, so `k mod 8` sends them all to one slot; "
                   "they violate simple uniform hashing, and the theorem says nothing about them",
                   "Theorem 11.2 is wrong for twenty keys, because it holds only as n grows",
                   "The load factor was computed wrongly; with one chain of 20 it should be 20",
                   "The mean is high because the lab adds keys at the tail instead of the head"],
             "c": 0,
             "why": "Every key is a multiple of 8, so every remainder is 0 and the table is one "
                    "chain of twenty; the mean is `(1 + 2 + … + 20)/20 = 21/2`. The theorem's "
                    "average is exact at every n, but only for keys that hash uniformly. α is n/m "
                    "by definition, 20/8, whatever the chains look like. Head or tail insertion "
                    "changes which key is found first, not the total over a chain."},
        ],
        "mistakes": [
            ("Reading Θ(1 + α) as a guarantee for every set of keys",
             "Theorems 11.1 and 11.2 average over keys that hash uniformly. For a fixed hash "
             "function there are always keys that all land in one slot, and then a search costs "
             "`Θ(n)`. In the lab, <code>degenerate</code> has the same load factor as "
             "<code>eight-slots</code> and a mean of 21/2 instead of 23/10. The average is a "
             "statement about the assumption, and the next lesson's universal hashing is the way "
             "to make it a statement about the algorithm instead."),
            ("Treating the load factor as every chain's length",
             "α is the mean chain length, exact by arithmetic. The chains themselves vary: in the "
             "worked example α is 10/7, one chain has four keys and two slots have none. The "
             "longest chain is what an unlucky search pays, and it is a separate figure from α."),
            ("Dropping the 1 from Θ(1 + α)",
             "Even when α is tiny, a search computes the hash and looks at a slot, so its cost is "
             "never below a constant. The 1 is that constant, and a successful search also "
             "examines the element it finds, which is the 1 in `1 + (n − 1)/(2m)`. A table with "
             "far more slots than keys is not free to search; it is constant-time."),
        ],
        "standard": (
            "Finish when you can build a chained table by hand and price its searches.",
            "Given a hash function, a table size and eight to twelve keys, build the chains, "
            "compute the measured mean for successful searches, and set it beside α and "
            "`1 + (n − 1)/(2m)`."
        ),
        "note": (
            "The lab's tile for the expected successful cost uses α/(2m) where Theorem 11.2 has "
            "α/(2n); the lesson gives the book's figure beside it. The measured mean and the "
            "longest chain describe the keys on screen. Whether a set of keys hashes uniformly "
            "cannot be read off one table; the expectations are averages over the assumption."
        ),
    },
    # ---------------------------------------------------------------- 03
    # CLRS section 11.3, pp. 262-269.
    # Quote: p. 265, 11 words, quotes.py OK. Lesson total: 11 words.
    # What makes a good hash function, keys as natural numbers (pp. 262-263);
    # the division method and the choice of m (p. 263); the multiplication
    # method, the w-bit implementation, Knuth's A (pp. 263-264); universal
    # hashing, the definition, Theorem 11.3, Corollary 11.4 (pp. 265-267);
    # the family H_pm and Theorem 11.5 (pp. 267-268).
    {
        "slug": "hash-functions",
        "title": "Hash Functions and Universal Hashing",
        "module": "Chapter 11 · Hash Tables",
        "one_line": "The division and multiplication methods are fast heuristics that some keys defeat; drawing the function at random from a universal family makes any two keys collide with probability at most 1/m, whatever the keys are.",
        "summary": (
            "Section 11.3 asks what makes a hash function good, gives two heuristics, the "
            "remainder on division by m and the fractional part of a product, and then removes "
            "the reliance on friendly keys by choosing the function at random from a family in "
            "which no pair of keys collides too often. Hash a few keys both ways by hand, then "
            "count in the lab, over every function in the family, how often one pair collides."
        ),
        "key": [
            "division: k mod m, with m a prime",
            "avoid m = 2ᵖ: only the low bits count",
            "multiplication: ⌊m·(kA mod 1)⌋",
            "fixed functions have bad key sets",
            "universal: collide with chance ≤ 1/m",
            "h(k) = ((ak + b) mod p) mod m",
        ],
        "key_label": "Section 11.3 in six lines",
        "concepts_intro": (
            "Three ideas. The first two are the heuristics most tables use; the third is the "
            "guarantee the section proves."
        ),
        "concepts": [
            ("Division method",
             "`h(k) = k mod m`. One division, so it is fast. Its quality depends on m: a power "
             "of 2 makes the hash the key's lowest bits and ignores the rest, and the authors "
             "suggest a prime not close to a power of 2."),
            ("Multiplication method",
             "`h(k) = ⌊m·(kA mod 1)⌋` for a constant A between 0 and 1: multiply, keep the "
             "fractional part, scale by m and round down. The value of m is not critical, so it "
             "is usually a power of 2, which lets a machine compute the hash with one "
             "multiplication and a shift."),
            ("Universal family",
             "A finite set H of hash functions such that for every pair of distinct keys, at "
             "most `|H|/m` of the functions send them to the same slot. A function drawn from "
             "H at random makes the pair collide with probability at most 1/m, the chance "
             "two independent random slots would agree."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read Section 11.3 in your own copy first. The lesson sets out the two methods and "
            "the universal family in its own words, hashes a few keys both ways by hand, and "
            "then counts a pair's collisions over a whole family in the lab."
        ),
        "body": [
            ("p", "&ldquo;Any fixed hash function is vulnerable to such terrible worst-case "
                  "behavior.&rdquo; The authors write it in Section 11.3.3, of an adversary who "
                  "knows the function and picks n keys for one slot, and it is the turn the "
                  "section takes: two heuristics that work well on ordinary keys, and then a "
                  "method whose guarantee does not depend on the keys at all. This lesson reads "
                  "Section 11.3."),
            ("p", "A good hash function would satisfy simple uniform hashing, but the section "
                  "begins by admitting that this can rarely be checked: the distribution of the "
                  "keys is usually unknown, and the keys may not be independent. What can be "
                  "done is to make the hash depend on the key in a way unlikely to line up with "
                  "patterns in the data, such as programs that use identifiers differing in one "
                  "letter. The functions all take natural numbers, so a string is first read as "
                  "a number, its characters as the digits of a large radix."),
            ("p", "Section 11.3.1's division method takes the remainder `k mod m`. Its weakness "
                  "is the modulus. If m is `2ᵖ`, the remainder is the lowest p bits of k and the "
                  "higher bits are ignored, so keys that agree in their low bits all collide; "
                  "the authors warn against `2ᵖ − 1` for strings too, since permuting the "
                  "characters leaves the hash unchanged (Exercise 11.3-3). Their advice is a "
                  "prime not near a power of 2, chosen from the number of slots the expected "
                  "load calls for."),
            ("p", "Section 11.3.2's multiplication method multiplies k by a constant A between 0 "
                  "and 1, keeps the fractional part, multiplies by m and takes the floor. On a "
                  "machine with w-bit words, A is taken as `s/2ʷ` for a w-bit integer s; the "
                  "product `k·s` is two words, and the hash is the top p bits of the lower word "
                  "when m is `2ᵖ`. Any A works, some better than others, and the authors report "
                  "Knuth's suggestion of `(√5 − 1)/2 ≈ 0.618`, the fractional part of the golden "
                  "ratio."),
            ("p", "Both methods are fixed functions, and Section 11.3.3, starred in the book, "
                  "starts from the adversary in the quotation. Its answer is the one quicksort "
                  "used in Chapter 7: randomize. At the start of execution, pick the function "
                  "by chance from a family designed for the purpose, independently of the keys "
                  "that will be stored. Then no particular set of keys is bad every time; a bad "
                  "outcome needs an unlucky draw of the function, and its probability is the same "
                  "for every set of keys of the same size."),
            ("thm", ("Theorem 11.3 and Corollary 11.4",
                     "If h is drawn from a universal family and n keys are chained in m slots, a "
                     "key not in the table hashes to a list of expected length at most α, and a "
                     "key in the table lies in a list of expected length at most 1 + α. So any "
                     "sequence of n insertions, searches and deletions containing `O(m)` "
                     "insertions takes `Θ(n)` expected time. The expectation is over the choice "
                     "of h; nothing is assumed about the keys.")),
            ("p", "The proof is the indicator method of Chapter 5. For a stored key k, add an "
                  "indicator for each other key l that lands in k's slot; each has expectation "
                  "at most 1/m by the definition, and linearity of expectation turns the sum "
                  "into at most `(n − 1)/m` other keys, or n/m for a key not stored. The "
                  "corollary adds this up over the operations, with α kept `O(1)` by the limit "
                  "on insertions."),
            ("def", ("The family of Section 11.3.3",
                     "Choose a prime p larger than every key. For a in 1 to p − 1 and b in 0 to "
                     "p − 1, let `h_ab(k) = ((ak + b) mod p) mod m`. The family has "
                     "`p·(p − 1)` functions, and Theorem 11.5 proves it universal.")),
            ("p", "The proof of Theorem 11.5 is a counting argument worth having by heart. Fix "
                  "keys k ≠ l and write r and s for `(ak + b) mod p` and `(al + b) mod p`. "
                  "Because p is prime and a is not 0, r ≠ s, and each pair (a, b) gives a "
                  "different pair (r, s): the map is one-to-one from the `p·(p − 1)` choices "
                  "of (a, b) onto the `p·(p − 1)` ordered pairs of distinct residues. So k and "
                  "l collide for exactly as many functions as there are pairs r ≠ s with "
                  "`r ≡ s (mod m)`, and for each r at most `(p − 1)/m` values of s qualify. The "
                  "count depends on p and m and not on k and l."),
            ("p", "Now the lab, the one from the Algorithms Subject's lesson Universal Hashing, "
                  "where the family is practised further. Choose p, m and two keys x and y; the "
                  "lab enumerates every (a, b), draws one cell per function, red where the pair "
                  "collides, and prints the number of functions, the colliding ones, the exact "
                  "rate, the bound 1/m and whether the rate is within it. A last tile picks two "
                  "keys that `k mod m` sends to the same slot, the adversary's move against one "
                  "fixed function, which collide with probability 1. The worked example "
                  "<code>p11-m4</code>, the pair 3 and 7, gives 20 of 110 functions, the rate "
                  "2/11 against 1/4; <code>p7-m3</code>, the pair 1 and 4, gives 10 of 42, or "
                  "5/21 against 1/3; <code>p13-m5</code>, the pair 2 and 9, gives 22 of 156, or "
                  "11/78 against 1/5."),
            ("p", "Then move the keys and leave p and m alone. At p = 11 and m = 4 every pair "
                  "you choose collides under 20 functions, which is the proof's count made "
                  "visible: the residues 0 to 10 fall into classes of sizes 3, 3, 3 and 2 modulo "
                  "4, and the ordered pairs within a class number `3·2 + 3·2 + 3·2 + 2·1 = 20`. "
                  "The count is exact for this family. The bound 1/m is what the theorem promises "
                  "for every universal family, and the expected chain lengths follow from it."),
            ("h3", "Exercise"),
            ("p", "Take p = 7 and m = 3, and the keys 2 and 5. Without listing the 42 functions, "
                  "count by the residue-pair argument how many send the two keys to the same "
                  "slot, and give the rate as a fraction beside 1/m. Then set the lab to p = 7, "
                  "m = 3, x = 2 and y = 5 to check, and say why the count matches a preset whose "
                  "keys are different."),
            ("p", "Chaining stores the colliding keys outside the table. The next lesson, Open "
                  "Addressing, keeps every key inside it and probes from slot to slot, and the "
                  "load factor then decides the cost in a different way."),
        ],
        "lab": ("hash", {
            "mode": "universal",
            "preset": "p11-m4",
            "panel_title": "Count one pair's collisions over the whole family",
            "panel_intro": (
                "The family is `h(k) = ((ak + b) mod p) mod m` with a from 1 to p − 1 and b from "
                "0 to p − 1. Choose the prime, the number of slots and two keys; every function "
                "is enumerated and the colliding ones counted, so the rate is exact, and it is "
                "set beside the 1/m that universality promises."
            ),
        }),
        "steps_title": "Hashing three ways by hand",
        "steps_intro": "Four steps on a few keys, then one in the lab.",
        "steps": [
            ("Divide",
             "Compute `k mod m` for each key. Then try m a power of 2 and see whether keys that "
             "share their low bits collide."),
            ("Multiply in a small word",
             "Pick w and `s ≈ 0.618·2ʷ`. Multiply k by s, split the product into a high and a "
             "low w-bit word, and take the top p bits of the low word as the slot in `2ᵖ` "
             "slots."),
            ("Draw one function from the family",
             "Pick a prime p above every key, then a from 1 to p − 1 and b from 0 to p − 1. "
             "Compute `((ak + b) mod p) mod m` for each key."),
            ("Count a pair's collisions exactly",
             "Sort the residues 0 to p − 1 into classes modulo m and count the ordered pairs of "
             "distinct residues within a class. That is how many of the `p·(p − 1)` functions "
             "make any two keys collide."),
            ("Check a pair of your own",
             "Choose p, m and two keys in the lab, predict the count of colliding functions by "
             "the class sizes, and read it off the tiles. Then change only the keys."),
        ],
        "worked": {
            "title": "Four keys, two methods, one small family",
            "intro": [
                "Division with `m = 16` and with `m = 11` on the keys 37, 53, 69 and 85; then "
                "multiplication with an 8-bit word; then the family at p = 5, m = 3.",
            ],
            "lines": [
                "mod 16:  37, 53, 69, 85 → 5, 5, 5, 5",
                "mod 11:  37, 53, 69, 85 → 4, 9, 3, 8",
                "w = 8, s = 158, p = 3 (m = 8):",
                "77·158 = 12166 = 47·256 + 134 → slot 4",
                "78·158 = 12324 = 48·256 + 36  → slot 1",
                "p = 5, m = 3: classes {0, 3} {1, 4} {2}",
                "ordered pairs: 2 + 2 + 0 = 4 of 20",
                "rate 1/5, against the bound 1/3",
            ],
            "after": [
                "The four keys differ by 16, so they share their low four bits and `k mod 16` "
                "puts them in one slot; modulo 11 they spread. In the multiplication, 134 is "
                "10000110 in binary and its top three bits are 100, slot 4; 36 is 00100100, "
                "slot 1, so neighbouring keys land far apart. In the family, the pair 1 and 4 "
                "collides under the functions with (a, b) equal to (1, 0), (1, 4), (4, 0) and "
                "(4, 4), four of twenty, and so would any other pair.",
            ],
        },
        "quiz_title": "Division, multiplication and the universal family",
        "quiz": [
            {"q": "In the family `((ak + b) mod 7) mod 3`, with a from 1 to 6 and b from 0 to 6, "
                  "how many of the 42 functions send the keys 2 and 5 to the same slot?",
             "a": ["10", "14", "6", "12"],
             "c": 0,
             "why": "Modulo 3 the residues 0 to 6 form the classes {0, 3, 6}, {1, 4} and {2, 5}. "
                    "Ordered pairs of distinct residues within a class number `3·2 + 2 + 2 = 10`, "
                    "and each corresponds to exactly one function, so 10 of 42, a rate of 5/21, "
                    "below 1/3. Fourteen is 42/3, the bound itself, which the family beats here. "
                    "Six counts only the largest class. Twelve counts each class as if it had "
                    "three residues. The count is the same as the preset pair 1 and 4 because it "
                    "depends only on p and m."},
            {"q": "Why do the authors advise against `m = 2ᵖ` for the division method?",
             "a": ["`k mod 2ᵖ` is the lowest p bits of k, so the hash ignores every higher bit "
                   "and keys that share their low bits all collide",
                   "A power of 2 makes the division slower than division by a prime",
                   "With `m = 2ᵖ` some slots can never be reached by `k mod m`",
                   "A power of 2 makes the table too large for the expected load"],
             "c": 0,
             "why": "Dividing by `2ᵖ` keeps the last p bits, so unless every low-bit pattern is "
                    "equally likely the hash depends on too little of the key; in the worked "
                    "example 37, 53, 69 and 85 all give 5 modulo 16. Speed is not the objection, "
                    "and division by a power of 2 is in fact a shift. Every remainder from 0 to "
                    "m − 1 is reachable. The table's size is chosen from the load either way."},
            {"q": "What exactly does universal hashing guarantee?",
             "a": ["For any fixed pair of distinct keys, the probability over the random choice "
                   "of function that they collide is at most 1/m",
                   "For a randomly chosen pair of keys, a fixed function makes them collide with "
                   "probability at most 1/m",
                   "No two keys ever collide, because the function is chosen after the keys",
                   "Every function in the family spreads every set of keys evenly"],
             "c": 0,
             "why": "The randomness is in the function, drawn once at the start and "
                    "independently of the keys, and the bound holds for every pair, including "
                    "pairs an adversary picks. Randomness over the keys with a fixed function is "
                    "the simple-uniform-hashing assumption, which universality removes. "
                    "Collisions still happen: in the worked example 4 of 20 functions collide on "
                    "the pair. Individual functions can be bad for particular keys; only the "
                    "average over the family is bounded."},
            {"q": "With `w = 8`, `s = 158` and `m = 8 = 2³`, where does the multiplication method "
                  "put the key 79?",
             "a": ["Slot 6", "Slot 4", "Slot 2", "Slot 7"],
             "c": 0,
             "why": "`79·158 = 12482 = 48·256 + 194`, so the low word is 194, which is 11000010 "
                    "in binary, and its top three bits 110 give slot 6. Slot 4 is the hash of 77. "
                    "Slot 2 takes the bottom three bits of 194 instead of the top three. Slot 7 "
                    "comes from rounding `8·(194/256) ≈ 6.06` up instead of down."},
        ],
        "mistakes": [
            ("Thinking universal hashing randomizes the keys",
             "The keys are whatever the user or an adversary supplies. What is random is the "
             "function, chosen once when the table is created and independently of the keys. "
             "Theorem 11.3's expectations are over that choice, and the lab makes this concrete: "
             "the pair is fixed and the count runs over every function. The authors compare it "
             "to randomized quicksort, whose pivot rather than its input is random."),
            ("Using a power of 2 as the modulus of the division method",
             "`k mod 2ᵖ` keeps the lowest p bits and discards the rest, so keys with a common "
             "low part collide, as 37, 53, 69 and 85 do modulo 16. The multiplication method is "
             "the one that suits a power of 2, because it mixes all the bits of k into the bits "
             "it keeps."),
            ("Expecting a function from a universal family to be good for every set of keys",
             "Universality bounds a probability over the draw. In the worked example the pair "
             "1 and 4 collides under 4 of the 20 functions, so one draw in five is unlucky for "
             "that pair. The guarantee is that bad draws are rare for every set of keys, not "
             "that any particular function is safe."),
        ],
        "standard": (
            "Finish when you can compute a hash three ways and count a family's collisions.",
            "Given keys, m and the constants, compute division and multiplication hashes by hand, "
            "and count how many functions of `h_ab` at a small prime make two keys collide."
        ),
        "note": (
            "The lab enumerates the family at primes up to 13 and keys below the prime, so its "
            "counts are exact rather than sampled. It does not run the division or "
            "multiplication methods on a table; the chaining lab of the previous lesson offers "
            "both rules, and the worked example does them by hand. A count over a family is "
            "still one family at one size; Theorem 11.5 is the claim for every prime."
        ),
    },
    # ---------------------------------------------------------------- 04
    # CLRS sections 11.4-11.5, pp. 269-285 (11.5 starred, named).
    # Quote: p. 272, 15 words, quotes.py OK. Lesson total: 15 words.
    # Open addressing, probe sequences, HASH-INSERT and HASH-SEARCH, deletion
    # with DELETED (pp. 269-271); uniform hashing; linear, quadratic and
    # double hashing (pp. 271-274); Theorem 11.6, Corollary 11.7, Theorem 11.8
    # (pp. 274-277); perfect hashing, Theorem 11.9, Corollary 11.11
    # (pp. 277-282).
    {
        "slug": "open-addressing",
        "title": "Open Addressing",
        "module": "Chapter 11 · Hash Tables",
        "one_line": "Open addressing keeps every key inside the table and probes slot after slot until it finds the key or an empty slot; under uniform hashing an unsuccessful search makes at most 1/(1 − α) probes, which grows without bound as the table fills.",
        "summary": (
            "Section 11.4 drops the chains: every key lives in the table, and each key has its "
            "own order in which to try the slots. Linear probing, quadratic probing and double "
            "hashing are three such orders, and the analysis under uniform hashing bounds the "
            "expected probes by 1/(1 − α). Section 11.5 is named: perfect hashing for a set of "
            "keys that never changes. Insert five keys by two probe rules by hand, then set the "
            "lab's counted probes beside the bound."
        ),
        "key": [
            "every key in the table, so α ≤ 1",
            "probe until the key or an empty slot",
            "delete by marking, never by emptying",
            "linear probing builds long clusters",
            "double hashing: Θ(m²) probe orders",
            "unsuccessful: at most 1/(1 − α) probes",
        ],
        "key_label": "Sections 11.4 and 11.5 in six lines",
        "concepts_intro": (
            "Three ideas. The first is the method, the second the assumption the analysis "
            "rests on, the third the reason the practical rules fall short of it."
        ),
        "concepts": [
            ("Probe sequence",
             "For each key k, the order `h(k, 0), h(k, 1), …, h(k, m − 1)` in which slots are "
             "tried, required to be a permutation of all m slots. Insertion takes the first "
             "empty slot in it; search follows the same order and stops at the key or at an "
             "empty slot."),
            ("Uniform hashing",
             "The assumption that every one of the `m!` orders of the slots is as likely as any "
             "other to be a key's probe sequence. It extends simple uniform hashing from one slot to a "
             "whole sequence, and the chapter's bounds hold under it."),
            ("Clustering",
             "Linear probing tries `h′(k), h′(k) + 1, …` and so lets runs of occupied slots "
             "grow: a key landing anywhere in a run extends it. That is primary clustering. "
             "Quadratic probing avoids it but keys with one home slot still share one "
             "sequence, a milder secondary clustering."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 11.4 and 11.5 in your own copy first. The lesson sets out the probe "
            "rules and the bound in its own words, fills a small table two ways by hand, and "
            "then sets the lab's counted probes beside the bound."
        ),
        "body": [
            ("p", "&ldquo;Long runs of occupied slots tend to get longer, and the average search "
                  "time increases.&rdquo; The authors say it in Section 11.4 of linear probing, "
                  "the simplest way to keep every key inside the table and the one most "
                  "affected by how full the table is. This lesson reads Section 11.4 and names "
                  "the starred Section 11.5."),
            ("p", "In open addressing there are no lists. Each slot holds a key or NIL, so the "
                  "table can fill and α can never exceed 1. What it saves is the pointers, and "
                  "the memory they took can buy more slots. Instead of following a chain, a key "
                  "carries a probe sequence: the hash function takes a second argument, the "
                  "probe number, and must produce every slot once as it runs from 0 to "
                  "m − 1. HASH-INSERT walks the sequence to the first empty slot; HASH-SEARCH "
                  "walks the same sequence and may stop at an empty slot, because the key would "
                  "have been placed there."),
            ("p", "That stopping rule is why deletion is hard. Emptying a deleted key's slot "
                  "would cut every probe sequence that passed through it, and keys inserted "
                  "later along those sequences would no longer be found. The book marks the "
                  "slot DELETED instead: insertion may reuse it, search walks past it. The price "
                  "is that search times stop depending on α alone, since marked slots lengthen "
                  "searches without holding keys, and for that reason the authors say chaining "
                  "is the usual choice when keys must be deleted."),
            ("p", "Three probe rules are compared, each built on an ordinary auxiliary hash. "
                  "<em>Linear probing</em> tries the home slot and then each next slot in turn, "
                  "wrapping round; the first probe fixes the whole sequence, so there are only m "
                  "sequences, and an empty slot after a run of i full ones is filled next with "
                  "probability `(i + 1)/m`, which is how runs grow. <em>Quadratic probing</em> "
                  "offsets by `c₁·i + c₂·i²`, which breaks up the runs, but needs its constants "
                  "chosen with care to reach every slot (Problem 11-3), and still has only m "
                  "sequences. <em>Double hashing</em> steps by a second hash, "
                  "`h(k, i) = (h₁(k) + i·h₂(k)) mod m`, so keys with one home slot usually step "
                  "differently."),
            ("p", "For double hashing to reach every slot, `h₂(k)` must share no factor with m. "
                  "The book's two ways are m a power of 2 with `h₂` always odd, and m prime with "
                  "`h₂` between 1 and m − 1. Then each pair of values `(h₁(k), h₂(k))` gives its "
                  "own sequence, `Θ(m²)` in all against linear probing's m, and in practice "
                  "double hashing behaves close to the uniform hashing the analysis assumes. "
                  "None of the three reaches the `m!` sequences that assumption requires."),
            ("thm", ("Theorem 11.6, Corollary 11.7, Theorem 11.8",
                     "Under uniform hashing with load factor `α < 1`, an unsuccessful search "
                     "makes at most `1/(1 − α)` probes on average, and so does an insertion. A "
                     "successful search makes at most `(1/α)·ln(1/(1 − α))` probes on "
                     "average.")),
            ("p", "The proof of the first bound is short and worth following. The first probe "
                  "finds an occupied slot with probability n/m. Given that the first j − 1 "
                  "probes all hit occupied slots, the next does with probability "
                  "`(n − j + 1)/(m − j + 1)`, which is at most n/m, so the chance of needing "
                  "an i-th probe is at most `α^(i − 1)`. Adding those chances over i gives the "
                  "geometric series `1 + α + α² + …`, which is `1/(1 − α)`. Read it as one probe "
                  "always, a second with probability about α, a third about α², and so on. An "
                  "insertion is an unsuccessful search followed by a store, hence the corollary. "
                  "A successful search for the (i + 1)-th key inserted repeats the unsuccessful "
                  "search made when it went in, and averaging that over the keys gives the "
                  "logarithm."),
            ("p", "Section 11.5, starred, is named here. When the set of keys never changes, as "
                  "with the reserved words of a language, two levels of universal hashing give "
                  "search in `O(1)` in the worst case. The first level hashes the n keys into n "
                  "slots; slot j's keys get a secondary table of size `n_j²` with its own "
                  "function, chosen so that it has no collisions. Theorem 11.9 shows a random "
                  "choice from a universal family is collision-free with probability over one "
                  "half at that size, and Corollary 11.11 that the secondary tables total under "
                  "2n slots in expectation."),
            ("p", "Now the lab, the one from the Algorithms Subject's lesson Open Addressing and "
                  "Linear Probing, where probing is practised further. It fills a table of "
                  "power-of-two size from a seeded stream of keys up to the load you choose, "
                  "searches for twelve keys that are absent and for every key present, and "
                  "counts probes. Its double hashing uses an odd second hash, the book's first "
                  "way. The tiles are the load factor, the mean probes counted for the absent "
                  "and the present keys, two values of Knuth's approximation for linear "
                  "probing, the longest run of occupied slots, and how many keys a delete would "
                  "lose if it emptied its slot instead of marking it."),
            ("p", "The worked example <code>linear-seventy</code> puts 22 keys in 32 slots, "
                  "α = 11/16. The bound for an absent key is `1/(1 − 11/16) = 16/5 = 3.2` "
                  "probes; linear probing counts 5 = 5.000, its longest cluster is 12 slots, and "
                  "emptying a slot would lose 3 keys. Choose <code>double</code> at the same "
                  "load: 3 = 3.000 for absent keys and 18/11 for present ones, against the "
                  "successful bound `(16/11)·ln(16/5) ≈ 1.69`, and the longest cluster is 8. "
                  "Then <code>clustered</code>: 28 keys, α = 7/8, the bound is 8, and linear "
                  "probing counts 101/12, about 8.42, with a cluster of 16 slots. The Knuth tiles "
                  "are the clustering curve for linear probing whatever rule is selected, and "
                  "the lab marks them approximate."),
            ("p", "Linear probing above the bound and double hashing below it is what the theory "
                  "leads you to expect: the bound is for uniform hashing, which double hashing "
                  "approximates and linear probing does not. It is also twelve absent keys in "
                  "one table. Move the seed and the counts move; the bound does not, because it "
                  "is an average over the assumption, and only the proof establishes it."),
            ("h3", "Exercise"),
            ("p", "Fill an 11-slot table by linear probing with `h′(k) = k mod 11`, inserting "
                  "27, 49, 16, 38 and 60. Now delete 49 by emptying its slot, and search for each "
                  "remaining key. How many can no longer be found? Then mark the slot DELETED "
                  "instead and count the probes a search for 60 makes."),
            ("p", "Chapter 11 has made search fast on average and slow in the worst case. The "
                  "next lesson, Binary Search Trees, starts Chapter 12, where the cost of every "
                  "operation is the height of a tree, and the order of the keys is kept as well."),
        ],
        "lab": ("hash", {
            "mode": "probing",
            "preset": "linear-seventy",
            "panel_title": "Fill an open table and count the probes",
            "panel_intro": (
                "Choose the probe rule, the table size and the load. The slots are drawn with "
                "their clusters, and probes are counted for twelve absent keys and for every key "
                "present. Set the absent count beside `1/(1 − α)`, the bound under uniform "
                "hashing; the dashed curve is Knuth's approximation for linear probing and is "
                "labelled so."
            ),
        }),
        "steps_title": "Open addressing by hand",
        "steps_intro": "Four steps on a small table, then one in the lab.",
        "steps": [
            ("Write each key's probe sequence",
             "For linear probing, the home slot and then each next slot, wrapping round. For "
             "double hashing, the home slot `h₁(k)` and then steps of `h₂(k)`, all modulo m."),
            ("Insert at the first empty slot",
             "Walk the sequence, count the probes, and store the key at the first empty or "
             "DELETED slot."),
            ("Search until the key or an empty slot",
             "Walk the same sequence. Pass occupied and DELETED slots; stop and report the key "
             "absent at an empty one."),
            ("Set the counts beside the bounds",
             "Compute `1/(1 − α)` for an absent key and `(1/α)·ln(1/(1 − α))` for a present "
             "one, and compare your counts, remembering that the bounds assume uniform hashing."),
            ("Try a load of your own",
             "In the lab, choose double hashing and a load between 0.5 and 0.9, compute "
             "`1/(1 − α)` from the printed load factor, and compare it with the counted probes; "
             "then switch to linear probing at the same load."),
        ],
        "worked": {
            "title": "Five keys, one home slot, two rules",
            "intro": [
                "An 11-slot table, `h₁(k) = k mod 11`, and for double hashing "
                "`h₂(k) = 1 + (k mod 10)`. The keys 27, 49, 16, 38 and 60 all have home slot 5.",
            ],
            "lines": [
                "linear: 27→5, 49→6, 16→7, 38→8, 60→9",
                "  probes 1 + 2 + 3 + 4 + 5 = 15",
                "double: 27→5",
                "  49: step 10, 5 → 4;  16: step 7, 5 → 1",
                "  38: step 9, 5 → 3;   60: step 1, 5 → 6",
                "  probes 1 + 2 + 2 + 2 + 2 = 9",
                "search 71 (home 5): linear 5,…,10: 6 probes",
                "double, step 2: 5, then 7 empty: 2 probes",
            ],
            "after": [
                "Every key collided at slot 5, and linear probing turned the collisions into one "
                "run of five slots, which every later key with a home anywhere from 5 to 9 must "
                "walk. Double hashing sent each key off by its own step. Here α = 5/11 and the "
                "bound for an absent key is 11/6, about 1.83; the two counts for 71, 6 and 2, "
                "are one key each, on either side of it.",
            ],
        },
        "quiz_title": "Probes, clusters and deletion",
        "quiz": [
            {"q": "Linear probing, `h′(k) = k mod 11`, inserts 27, 49, 16, 38, 60. Slot 6, which "
                  "holds 49, is then emptied rather than marked. How many of the remaining four "
                  "keys can a search no longer find?",
             "a": ["3", "1", "0", "4"],
             "c": 0,
             "why": "All five keys have home slot 5, so 16, 38 and 60 were placed by probing "
                    "past slot 6. With slot 6 empty, a search for any of them probes 5, finds 27, "
                    "probes 6, finds it empty and stops. Only 27, in its home slot, is still "
                    "found. One counts only the key in the next slot. None would be right if the "
                    "slot were marked DELETED, and four counts 27, which is never past the gap."},
            {"q": "Under uniform hashing, a table has 40 of its 64 slots occupied. What does "
                  "Theorem 11.6 bound the expected probes of an unsuccessful search by?",
             "a": ["8/3", "5/8", "8/5", "13/8"],
             "c": 0,
             "why": "α = 40/64 = 5/8, so `1/(1 − α) = 1/(3/8) = 8/3`, about 2.67. Five eighths is "
                    "α itself, the unsuccessful cost under chaining. Eight fifths is 1/α. "
                    "Thirteen eighths is `1 + α`, the shape of the chaining bound, which grows "
                    "far more slowly than open addressing's as the table fills."},
            {"q": "Why can double hashing with m a power of 2 use only odd values of `h₂(k)`?",
             "a": ["The step must share no factor with m, or the probe sequence cycles through "
                   "only some of the slots",
                   "Even steps would make double hashing the same as linear probing",
                   "Odd steps make the probe sequence a uniform random permutation",
                   "Odd steps keep every probe sequence inside the key's own cluster"],
             "c": 0,
             "why": "Stepping by d modulo m visits `m/gcd(d, m)` slots, all of them only when the "
                    "greatest common divisor is 1, and with m a power of 2 that means d odd. An "
                    "even step is not linear probing, whose step is 1. Odd steps give `Θ(m²)` "
                    "sequences, far fewer than the `m!` of uniform hashing. And the point of a "
                    "second hash is to step out of clusters, not to stay in them."},
            {"q": "On the lab's <code>linear-seventy</code>, α = 11/16, the counted probes for "
                  "absent keys are 5 while Theorem 11.6 gives 3.2. Which reading is right?",
             "a": ["The theorem assumes uniform hashing; linear probing has only m probe "
                   "sequences and clusters, so it is not covered, and twelve searches are one "
                   "sample in any case",
                   "The theorem is refuted, because a counted mean exceeded its bound",
                   "The count is wrong, because no search can exceed 1/(1 − α) probes",
                   "The bound applies only to successful searches, so 5 is not comparable"],
             "c": 0,
             "why": "Theorem 11.6 bounds an expectation under uniform hashing. Linear probing "
                    "falls short of that assumption, and its clusters make long searches likely, "
                    "which is why double hashing at the same load counts 3. A bound on an average "
                    "does not cap any single search, and one table's twelve searches cannot refute "
                    "a theorem about a different model. The bound in question is the unsuccessful "
                    "one; the successful bound is the logarithmic one."},
        ],
        "mistakes": [
            ("Expecting open addressing to slow down gently as the table fills",
             "Under chaining the cost grows like `1 + α` and the table can hold more keys than "
             "slots. Open addressing's bound is `1/(1 − α)`, which is modest while the table is "
             "partly empty and grows without limit as α approaches 1. In the lab the bound is "
             "3.2 at α = 11/16 and 8 at α = 7/8, and linear probing counts 5 and about 8.4. The "
             "fix is to keep α away from 1, usually by rebuilding into a larger table."),
            ("Deleting by emptying the slot",
             "A search stops at an empty slot, so emptying one cuts every probe sequence that "
             "ran through it. In the exercise one emptied slot hides three of four keys, and "
             "the lab's last tile counts the same loss on its table. Mark the slot DELETED; "
             "insertion may reuse it and search walks past it. The authors add that marked slots "
             "make search times depend on more than α, which is why chaining is preferred when "
             "deletions are common."),
            ("Taking linear probing for uniform hashing",
             "Linear probing gives only m different probe sequences, one per home slot, and its "
             "runs grow because a key that lands anywhere in one extends it. Uniform hashing "
             "needs every one of the `m!` orders to be equally likely. The bounds of Theorems "
             "11.6 and 11.8 are about that model; double hashing comes close to it and linear "
             "probing does not."),
        ],
        "standard": (
            "Finish when you can run an open-address table by hand and bound its probes.",
            "Given a probe rule, a table size and five to eight keys, insert them counting "
            "probes, search with DELETED slots handled correctly, and compute the bounds "
            "`1/(1 − α)` and `(1/α)·ln(1/(1 − α))`."
        ),
        "note": (
            "The lab fills its table from a seeded stream at power-of-two sizes and does not take "
            "your keys; the worked example and the exercise use an 11-slot table by hand. Its "
            "quadratic rule is not the one Problem 11-3 recommends, so the lesson does not use "
            "it. Its counts are a dozen searches on one table; the bounds are expectations under "
            "uniform hashing."
        ),
    },
    # ---------------------------------------------------------------- 05
    # CLRS Chapter 12, sections 12.1-12.4, pp. 286-307 (12.4 starred, its
    # proof named).
    # Quote: p. 286, 16 words, quotes.py OK. Lesson total: 16 words.
    # Dictionary and priority queue, O(h) (p. 286); the BST property and the
    # inorder walk, Theorem 12.1 (pp. 286-288); TREE-SEARCH, MINIMUM,
    # MAXIMUM, SUCCESSOR, Theorem 12.2 (pp. 289-293); TREE-INSERT
    # (pp. 294-295); deletion's three cases, TRANSPLANT, Theorem 12.3
    # (pp. 295-298); randomly built trees, Theorem 12.4 (pp. 299-303).
    {
        "slug": "binary-search-trees",
        "title": "Binary Search Trees",
        "module": "Chapter 12 · Binary Search Trees",
        "one_line": "A binary search tree keeps every key in a node's left subtree no larger and every key in its right subtree no smaller, so search, minimum, successor, insertion and deletion each follow one path and cost O(h) for a tree of height h.",
        "summary": (
            "Chapter 12 defines the binary-search-tree property, walks the tree in sorted order, "
            "and gives search, minimum, maximum, successor and predecessor, insertion, and the "
            "three-case deletion that moves subtrees with TRANSPLANT. Every operation costs time "
            "proportional to the height, and Section 12.4 shows that random insertion orders "
            "give height O(lg n) on average. Build and prune a ten-key tree by hand, then run the "
            "same operations in the lab with every comparison counted."
        ),
        "key": [
            "left subtree ≤ node ≤ right subtree",
            "an inorder walk prints the keys sorted",
            "search and insert follow one path, O(h)",
            "successor: leftmost key of the right",
            "two children: the successor replaces it",
            "sorted insertion order gives h = n − 1",
            "random orders give O(lg n) on average",
        ],
        "key_label": "Chapter 12 in seven lines",
        "concepts_intro": (
            "Three ideas carry the chapter. Chapters 13 and 14 keep all three and add balance "
            "and extra fields."
        ),
        "concepts": [
            ("Binary-search-tree property",
             "For every node x, every key in x's left subtree is at most `x.key` and every key "
             "in its right subtree is at least `x.key`. The property is about whole subtrees, "
             "not only about a node's two children."),
            ("Successor",
             "The node with the smallest key larger than x's. If x has a right subtree, it is "
             "that subtree's leftmost node. Otherwise climb from x until the climb arrives at a node "
             "from its left child; that node is the successor."),
            ("Transplant",
             "Replacing the subtree rooted at one node by the subtree rooted at another, by "
             "relinking the first node's parent to the second. TREE-DELETE is written in terms "
             "of it, so that whole subtrees move without being copied."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read Chapter 12 in your own copy first. The lesson sets out the property and the "
            "operations in its own words, builds and prunes one tree by hand, and then runs the "
            "operations in the lab with the comparisons counted."
        ),
        "body": [
            ("p", "&ldquo;Basic operations on a binary search tree take time proportional to the "
                  "height of the tree.&rdquo; The authors put it in the chapter's second "
                  "paragraph, and the rest of Part III follows from it: if height is the cost, "
                  "then a tree that is a chain is a linked list, and keeping the height down is "
                  "worth a chapter of its own. This lesson reads Chapter 12."),
            ("p", "Section 12.1 defines the tree. Each node has a key, satellite data and "
                  "pointers to its left child, right child and parent, and the keys obey the "
                  "binary-search-tree property. Different trees can hold the same keys; what "
                  "they share is that an <em>inorder</em> walk, left subtree, then the node, "
                  "then the right subtree, prints the keys in sorted order. Theorem 12.1 shows "
                  "the walk takes `Θ(n)` time on n nodes. Preorder and postorder walks, node "
                  "first or node last, are named beside it."),
            ("p", "Section 12.2's queries each follow a single path down. TREE-SEARCH compares "
                  "the key sought with the node's and goes left if smaller, right if larger, "
                  "stopping at a match or NIL; the book gives a recursive version and a loop "
                  "that does the same. TREE-MINIMUM follows left pointers to the end and "
                  "TREE-MAXIMUM right pointers. TREE-SUCCESSOR has two cases: the leftmost node "
                  "of x's right subtree if there is one, and otherwise the first ancestor reached "
                  "by climbing out of a left subtree. It never compares a key, because the shape "
                  "of the tree already encodes the order. Theorem 12.2 puts each of these at "
                  "`O(h)`."),
            ("p", "Section 12.3 changes the tree. TREE-INSERT walks down as a search would, "
                  "keeping a trailing pointer to the last node passed, and hangs the new node "
                  "from it as a leaf, in `O(h)`. Deletion of a node z has three cases. With no "
                  "left child, z is replaced by its right subtree; with no right child, by its "
                  "left; either covers a leaf. With two children, z's successor y takes z's "
                  "place. The successor sits in z's right subtree and lacks a left child, which "
                  "is what makes it easy to lift out."),
            ("def", ("The two-child case of TREE-DELETE",
                     "Let y be the minimum of z's right subtree. If y is z's right child, "
                     "transplant y into z's place and give it z's left subtree. Otherwise, "
                     "first transplant y's right subtree into y's place, make z's right subtree "
                     "y's right subtree, and then transplant y into z's place with z's left "
                     "subtree. Each step relinks a constant number of pointers.")),
            ("p", "Theorem 12.3 completes the chapter's claim: insertion and deletion run in "
                  "`O(h)` on a tree of height h, deletion's cost being the search for the "
                  "successor. The height itself depends on the order of insertion. Keys inserted "
                  "in increasing order make a chain of height n − 1, and the best any n-node tree "
                  "can do is `⌊lg n⌋`. Section 12.4, starred, defines a randomly built tree as "
                  "one made by inserting n distinct keys in an order chosen uniformly from all "
                  "n! orders."),
            ("thm", ("Theorem 12.4",
                     "Insert n distinct keys into an empty tree in an order drawn uniformly at "
                     "random, and the tree's expected height is `O(lg n)`.")),
            ("p", "The proof works with the exponential height `2^h`, conditions on which key is "
                  "the root, and bounds the expectation of the larger subtree's term by the sum "
                  "of both, a recurrence whose solution is a polynomial in n; Jensen's "
                  "inequality then brings it back to the height. It is left to the book. Two "
                  "warnings come with it. Deletions are excluded, since little is known about "
                  "trees built by both, and the randomness is in the order of the keys, which "
                  "the program usually does not choose; Chapter 13's red-black trees remove that "
                  "dependence."),
            ("p", "Now the lab, from the Algorithms Subject's lesson Binary Search Trees, where "
                  "the operations are practised further; its lesson The Shape Problem and Random "
                  "BSTs runs Section 12.4's insertion orders. Type operations: a number inserts "
                  "it, a minus sign before it deletes it, a question mark searches for it. The "
                  "slider chooses which step's tree is drawn. The tiles are the height, counted "
                  "in edges as the book does, the keys held, the comparisons counted over the "
                  "whole sequence, whether the tree is still a search tree, and what the shown "
                  "step did. A smaller drawing beside it is a tree in which every node lies "
                  "between its two children and which is still not a search tree."),
            ("p", "The worked example <code>two-child-delete</code> inserts seven keys and "
                  "deletes 30, which has two children: successor 40 moved up, 6 keys at height 2, "
                  "13 comparisons. <code>delete-the-root</code> deletes 50 instead and the "
                  "successor 60 comes up from the right side. <code>degenerate</code> inserts six "
                  "keys in increasing order: height 5, the chain. <code>search</code> builds the "
                  "seven-key tree and looks up 40 and 55: found via 50, 30 and 40, and 16 "
                  "comparisons in all. Move the slider to the last step to see each sequence's "
                  "final tree."),
            ("p", "Then type the worked example's keys, `41 20 65 11 29 50 91 32 72 99`, and end "
                  "with `-65`: successor 72 moved up, 9 keys, height 3, 23 comparisons. Here the "
                  "successor is not 65's right child, which is the case that needs the extra "
                  "transplant. Type the same ten keys in increasing order and the height is 9 "
                  "with 45 comparisons, against 19 for the order above: one set of keys, two "
                  "costs, decided by the order alone."),
            ("h3", "Exercise"),
            ("p", "Build the tree from `41 20 65 11 29 50 91 32 72 99` by hand. Delete 20, saying "
                  "which of TREE-DELETE's cases applies, and draw the result. What is its height "
                  "and what is its inorder sequence? Then find the successor of 32 in the "
                  "original tree by the climbing rule, without comparing keys."),
            ("p", "The height decides everything, and the insertion order decides the height. "
                  "The next lesson, Red-Black Trees and Rotations, begins Chapter 13: one colour "
                  "bit per node and five rules that hold the height to `2·lg(n + 1)` whatever "
                  "the order."),
        ],
        "lab": ("tree", {
            "mode": "bst",
            "preset": "two-child-delete",
            "panel_title": "Insert, search and delete, and count the comparisons",
            "panel_intro": (
                "Write a number to insert it, a minus sign before it to delete it, a question mark "
                "before it to search. Every comparison is counted, the inorder sequence is read "
                "off the tree after each step, and the property is checked over whole subtrees. "
                "The slider shows the tree after any step."
            ),
        }),
        "steps_title": "Operating a search tree by hand",
        "steps_intro": "Four steps on paper, then one in the lab.",
        "steps": [
            ("Insert by searching",
             "For each key, start at the root, go left if the key is smaller and right if it is "
             "larger, and hang it as a leaf where the path ends. Count the comparisons."),
            ("Find a successor without comparing",
             "If the node has a right subtree, go right once and then left to the end. If not, "
             "climb until you leave a left subtree; the parent you reach is the successor."),
            ("Delete by the three cases",
             "No left child: replace the node by its right subtree. No right child: by its left. "
             "Two children: lift its successor, first giving the successor's right subtree to "
             "the successor's parent if the successor is deeper than the right child."),
            ("Check the inorder sequence",
             "Read the tree left subtree, node, right subtree. If the keys are not sorted, a "
             "step went wrong."),
            ("Try an order of your own",
             "Choose ten keys, insert them in two different orders in the lab, and compare the "
             "heights and the comparisons; then delete a node with two children in each."),
        ],
        "worked": {
            "title": "Ten keys, one successor, one deletion",
            "intro": [
                "Insert `41 20 65 11 29 50 91 32 72 99` in that order, then find the successor "
                "of 29 and delete 65.",
            ],
            "lines": [
                "41 root; 20, 65 below; 11, 29, 50, 91",
                "32 right of 29; 72 left of 91; 99 right",
                "comparisons 0+1+1+2+2+2+2+3+3+3 = 19",
                "height 3: 41, 20, 29, 32",
                "successor of 29: right to 32, no left: 32",
                "delete 65: successor 72, not its child",
                "lift 72 out: 91 now has no left child",
                "72 replaces 65, with 50 left and 91 right",
            ],
            "after": [
                "Deleting 65 is the two-child case where the successor is deeper than the right "
                "child. 72 has no right subtree, so lifting it out leaves 91 with no left child; "
                "72 then takes 91 as its right subtree and 50 as its left, and replaces 65 under "
                "41. The inorder sequence, 11 20 29 32 41 50 72 91 99, is still sorted. The lab "
                "prints 23 comparisons: 19 for the insertions, 2 to find 65, 2 to reach 72.",
            ],
        },
        "quiz_title": "Search-tree operations and their heights",
        "quiz": [
            {"q": "Build the tree from `41 20 65 11 29 50 91 32 72 99` and delete 20. What is the "
                  "tree's height afterwards, and which key took 20's place?",
             "a": ["Height 3; 29 took its place, keeping 32 as its right child",
                   "Height 2; 29 took its place",
                   "Height 3; 11 took its place",
                   "Height 3; 32 took its place"],
             "c": 0,
             "why": "20 has two children, and its successor 29 is its own right child, so 29 is "
                    "transplanted into 20's place and given 11 as its left subtree, keeping 32 on "
                    "its right. The left side shrinks to depth 2, but 41, 65, 91, 72 is still a "
                    "path of three edges, so the height stays 3. Eleven is the predecessor, the "
                    "other legitimate choice of Exercise 12.3-6, which TREE-DELETE does not make. "
                    "Thirty-two is the leftmost key of 29's right subtree, not of 20's."},
            {"q": "In the same original tree, what is the successor of 32?",
             "a": ["41", "29", "50", "65"],
             "c": 0,
             "why": "32 has no right subtree, so climb: 32 is 29's right child and 29 is 20's "
                    "right child, so keep climbing; 20 is 41's left child, so the climb leaves a "
                    "left subtree there and 41 is the successor. Twenty-nine is the parent, and "
                    "its key is smaller. Fifty is the next key after 41. Sixty-five is 41's right "
                    "child, which is where a successor search starts only when the node has a "
                    "right subtree."},
            {"q": "Ten distinct keys are inserted in increasing order into an empty tree. What is "
                  "the height, and how many comparisons do the insertions make?",
             "a": ["Height 9, 45 comparisons", "Height 3, 19 comparisons",
                   "Height 10, 55 comparisons", "Height 9, 55 comparisons"],
             "c": 0,
             "why": "Each key becomes the right child of the one before, so the tree is a chain "
                    "of nine edges, and the i-th key is compared with the i − 1 keys above it: "
                    "`0 + 1 + … + 9 = 45`. Height 3 and 19 comparisons belong to the worked "
                    "order of the same ten keys. Ten and 55 count nodes and comparisons one too "
                    "many each, height being edges."},
            {"q": "A check confirms that every node's left child is smaller than it and its right "
                  "child larger. Does that make the tree a binary search tree?",
             "a": ["No: the property is about whole subtrees, and a key deep in a left subtree "
                   "can still exceed an ancestor",
                   "Yes: the property for every node and its children implies it for subtrees by "
                   "induction",
                   "Yes, provided the tree's height is at most lg n",
                   "No, because a binary search tree's keys must also be stored in sorted order "
                   "level by level"],
             "c": 0,
             "why": "A right child of a left child can be larger than the grandparent and still "
                    "beat its own parent; a search for it then turns the wrong way at the "
                    "grandparent. The lab's small tree is such a case. The induction fails "
                    "because the children's comparisons say nothing about the grandparent. "
                    "Height is irrelevant to correctness. Level-by-level order is not part of "
                    "the property, and most search trees do not have it."},
        ],
        "mistakes": [
            ("Checking the search-tree property only between parents and children",
             "The property says every key in a left subtree is at most the node's key, and the "
             "local check misses a key that is larger than an ancestor two levels up. The lab "
             "draws such a tree beside every run: it passes the local check and fails the real "
             "one, and a search for its misplaced key turns the wrong way and never finds it. "
             "Checking the inorder sequence for sortedness tests the real property."),
            ("Assuming the successor is always the deleted node's right child",
             "The successor is the leftmost node of the right subtree, which may be several "
             "levels down. When it is, TREE-DELETE first hands the successor's right subtree to "
             "the successor's parent and only then lifts the successor into place. In the "
             "worked example deleting 65 lifts 72 from below 91; in the exercise deleting 20 "
             "lifts 29, which is its right child."),
            ("Treating O(lg n) as the cost of every search-tree operation",
             "Every operation is `O(h)`, and h ranges from `⌊lg n⌋` to n − 1 depending on the "
             "insertion order. The same ten keys give height 3 and 19 comparisons in one order "
             "and height 9 and 45 in increasing order. Theorem 12.4's `O(lg n)` is an expectation "
             "over random orders, not a bound on any tree a program builds."),
        ],
        "standard": (
            "Finish when you can carry out every search-tree operation by hand.",
            "Given eight to twelve keys, build the tree, find a successor by the two cases, "
            "delete nodes of each kind including a two-child node whose successor is not its "
            "child, and give the height and inorder sequence after each step."
        ),
        "note": (
            "The lab deletes with the successor and searches by key; it has no predecessor or "
            "successor query of its own, so those are worked by hand. Its height is in edges, as "
            "in Chapter 12. Its comparison counts are for the sequence typed; Theorem 12.4's "
            "expectation is over random insertion orders and is not something one run can show."
        ),
    },
]
