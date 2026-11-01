"""Advanced Data Structures, lessons 1-5 -- Chapters 18-21.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed.
(MIT Press, 2009): Chapter 18, B-Trees (pp. 484-504); Chapter 19, Fibonacci
Heaps (pp. 505-530); Chapter 20, van Emde Boas Trees (pp. 531-560);
Chapter 21, Data Structures for Disjoint Sets (pp. 561-585). Every quotation
is copied from the operator's copy with its printed page in the comment
beside the lesson. The keys and operation sequences are written for these
lessons: none of the book's figures, examples or exercises is reproduced, and
its procedures are described in prose and named.
"""

# Sixteen keys in one shuffled order, used by three of lesson 1's presets.
BT_KEYS = "17 4 30 9 22 1 13 26 35 6 19 11 28 2 33 8"

# Seventeen insertions and one EXTRACT-MIN: a single tree of 16 nodes rooted at
# 20, the starting point of every preset in lesson 3.
FH_TREE = ("insert 10 insert 20 insert 30 insert 40 insert 50 insert 60 insert 70 insert 80 "
           "insert 90 insert 100 insert 110 insert 120 insert 130 insert 140 insert 150 "
           "insert 160 insert 170 extract")

# Eight insertions in one order, used by lesson 2's first three presets.
FH_EIGHT = "insert 12 insert 7 insert 25 insert 3 insert 18 insert 9 insert 30 insert 15"

# One sequence of operations, run in three universes in lesson 4.
VEB_OPS = ("insert 1 insert 9 insert 10 insert 13 member 10 member 11 successor 5 "
           "successor 10 successor 13 delete 1 delete 13")

LESSONS = [
    # ---------------------------------------------------------------- 01
    # CLRS Chapter 18 opening and sections 18.1-18.3, pp. 484-504.
    # Quote: p. 495, 18 words, quotes.py OK. Lesson total: 18 words.
    # Disks, pages, DISK-READ and DISK-WRITE, the root kept in memory
    # (pp. 484-488); the definition, minimum degree t, 2-3-4 trees (pp. 488-489);
    # Theorem 18.1 and its counting proof (pp. 489-490); B-TREE-SEARCH's O(h)
    # pages and O(t h) CPU (p. 492); B-TREE-SPLIT-CHILD, B-TREE-INSERT and
    # B-TREE-INSERT-NONFULL, splitting on the way down (pp. 493-497); the
    # deletion cases 1, 2a-2c, 3a-3b (pp. 499-502).
    {
        "slug": "b-trees",
        "title": "B-Trees",
        "module": "Chapter 18 · B-Trees",
        "one_line": "A B-tree is a balanced search tree whose nodes each fill a disk page, so its height, and with it the number of disk accesses an operation makes, grows as the logarithm to the base t of the number of keys.",
        "summary": (
            "Chapter 18 designs a search tree for data that lives on disk, where reading a page "
            "costs far more than examining what is on it. Section 18.1 defines the B-tree by its "
            "minimum degree t and proves its height is at most log_t((n + 1)/2); Section 18.2 "
            "searches it and inserts into it in one pass down, splitting full nodes on the way; "
            "Section 18.3 sketches deletion. Insert eight keys by hand, then grow larger trees "
            "in the lab and count every split, read and write against the height theorem."
        ),
        "key": [
            "a node fills one disk page",
            "each non-root node: t − 1 to 2t − 1 keys",
            "every leaf sits at the same depth",
            "height h ≤ log_t((n + 1)/2)",
            "split each full node on the way down",
            "a B-tree grows only at its root",
        ],
        "key_label": "Chapter 18 in six lines",
        "concepts_intro": (
            "Three ideas carry the chapter. Everything after the definition is a way of keeping "
            "the first two true while keys arrive."
        ),
        "concepts": [
            ("Minimum degree",
             "The fixed integer `t ≥ 2` that bounds every node's occupancy. A node other than "
             "the root holds between `t − 1` and `2t − 1` keys, so an internal node has between "
             "t and 2t children; a node holding exactly `2t − 1` keys is called full. With "
             "`t = 2` every internal node has 2, 3 or 4 children: a 2-3-4 tree."),
            ("Disk accesses as the cost",
             "The chapter counts two things separately: the CPU time spent inside nodes, and the "
             "pages read from and written to disk. A page read is so much slower than the work "
             "done on it that the second count usually decides the running time, and it is "
             "set by the height of the tree."),
            ("Splitting a full node",
             "A full node of `2t − 1` keys is cut around its median key into two nodes of "
             "`t − 1` keys each, and the median moves up into the parent to separate them. It "
             "is the only way a B-tree gains a node at a level, and splitting the root is the "
             "only way it gains a level."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the chapter opening and sections 18.1 to 18.3 in your own copy first. The "
            "lesson sets out the argument in its own words, grows one small tree by hand, and "
            "then counts splits and disk accesses on larger trees in the lab."
        ),
        "body": [
            ("p", "&ldquo;Unlike a binary search tree, a B-tree increases in height at the top "
                  "instead of at the bottom.&rdquo; The authors say it in Section 18.2, after "
                  "the procedure that splits a full root, and it is the shortest summary of why a "
                  "B-tree stays balanced without any rotations. This lesson reads Chapter 18: "
                  "why data on disk calls for a different measure of cost, what a B-tree is, why "
                  "its height is logarithmic to a large base, and how keys are inserted in a "
                  "single pass from the root down."),
            ("p", "The chapter opens with the machine. Main memory is silicon; secondary storage "
                  "is a magnetic disk whose platters rotate under heads on moving arms, and the "
                  "authors put the gap in the figures of their day: one rotation of a 7200 RPM "
                  "disk takes 8.33 milliseconds, against roughly 50 nanoseconds for a memory "
                  "access. To spread that wait, a disk reads and writes whole pages at once. So "
                  "the chapter models a node as an object that must be brought in by DISK-READ "
                  "before its fields are touched and saved by DISK-WRITE after they change, and "
                  "it counts those calls apart from the computing time. Two conventions follow: "
                  "the root stays in main memory, so it is never read, though it is written "
                  "whenever it changes; and a node is as large as a page, which is what makes "
                  "branching factors in the hundreds or thousands possible."),
            ("def", ("B-tree of minimum degree t",
                     "A rooted tree in which each node x stores its number of keys, the keys in "
                     "nondecreasing order, and whether it is a leaf; an internal node with k keys "
                     "has k + 1 children, and the keys separate the ranges of the subtrees "
                     "between them. All leaves have the same depth, the height h. Every node "
                     "other than the root has at least `t − 1` keys, every node has at most "
                     "`2t − 1`, and a nonempty tree's root has at least one.")),
            ("p", "Section 18.1 bounds the height by counting the fewest keys a tree of height "
                  "h can hold. The root has at least one key and so at least two children; every "
                  "other internal node has at least t children; so depth 1 holds at least 2 nodes, "
                  "depth 2 at least `2t`, and depth h at least `2·tʰ⁻¹`, each "
                  "holding at least `t − 1` keys. Adding these up gives the theorem."),
            ("thm", ("Theorem 18.1",
                     "If `n ≥ 1`, a B-tree with n keys, height h and minimum degree `t ≥ 2` has "
                     "`n ≥ 2·tʰ − 1`, and so `h ≤ log_t((n + 1)/2)`. A red-black tree's height "
                     "is also `O(lg n)`, but here the base of the logarithm is t, and t can be "
                     "in the thousands; the saving in nodes visited is a factor of about "
                     "`lg t`.")),
            ("math", [
                "the fewest keys a B-tree of height h can hold, 2·tʰ − 1",
                "",
                "h        t = 2      t = 3      t = 5",
                "0          1          1          1",
                "1          3          5          9",
                "2          7         17         49",
                "3         15         53        249",
                "4         31        161      1,249",
            ]),
            ("p", "Read the table from the other side and it is the bound: 16 keys cannot fill a "
                  "tree of height 4 at `t = 2`, which needs 31, so the height is at most 3; at "
                  "`t = 3` the same 16 keys allow height at most 1, since height 2 needs 17. "
                  "Section 18.2 then searches the tree as a binary search tree is searched, but "
                  "with a many-way decision at each node: a linear scan finds the first key not "
                  "smaller than the target, and the search either stops there or reads the child "
                  "to its left and goes on. That reads `O(h)` pages and spends `O(t)` time in each "
                  "node, `O(t·h)` in all."),
            ("p", "Insertion is the heart of the section. A new key always goes into an existing "
                  "leaf, and a full leaf cannot take it, so a full node must be split first, and "
                  "the median that moves up needs room in the parent. Rather than discover a full "
                  "parent and climb back up, B-TREE-INSERT splits every full node it meets on the "
                  "way down: when the root is full it puts a new empty root above it and splits "
                  "the old one, which is the only way the height grows; then B-TREE-INSERT-NONFULL "
                  "descends, and before stepping into a child it splits that child with "
                  "B-TREE-SPLIT-CHILD if the child is full. Because every node it steps into has "
                  "room, a split never has to reach above the node it starts at, and the whole "
                  "insertion is one pass from root to leaf."),
            ("p", "The pass also fixes the disk count of one insertion, and the lab counts by "
                  "exactly this rule. Stepping into a child costs one DISK-READ (the root never "
                  "does, and neither does the fresh right half of a split, which is already in "
                  "memory); writing the key into its leaf costs one DISK-WRITE; and each split "
                  "costs three DISK-WRITEs, for the two halves and the parent that gains the "
                  "median. The count is of calls, as the procedures make them: just after a root "
                  "split, B-TREE-INSERT-NONFULL calls DISK-READ on a half that is still in memory, "
                  "and the lab counts that call too. So an insertion into a tree of height h makes h reads and one write "
                  "when nothing splits, and at most `3·(h + 1) + 1` writes when everything on the "
                  "path is full."),
            ("p", "Section 18.3 sketches deletion without pseudocode. A key can be removed from "
                  "any node, not only a leaf, so the procedure must keep nodes from becoming too "
                  "small, and it does the mirror of what insertion does: before it descends into "
                  "a child it makes sure the child has at least t keys, one more than the "
                  "minimum. A key in a leaf is simply removed (case 1); a key in an internal node "
                  "is replaced by its predecessor or successor when a neighbouring child can "
                  "spare one, or pushed down into a merged child when neither can (cases 2a to "
                  "2c); and a thin child on the way down borrows a key through the parent from a "
                  "sibling, or merges with one (cases 3a and 3b). When the root is left with no "
                  "keys it is removed, and the tree loses a level at the top, just as it gained "
                  "them. The lab does not delete."),
            ("p", "Now the lab. Give it t and a list of distinct keys and it inserts them in "
                  "order with B-TREE-INSERT. The tiles are the height (edges from the root to a "
                  "leaf), the number of nodes, the splits, the DISK-READs and DISK-WRITEs counted "
                  "by the rule above, Theorem 18.1's bound `log_t((n + 1)/2)` printed to two "
                  "places, and the finished tree level by level with each node's keys in "
                  "brackets. The table below gives each insertion its own splits, reads, writes "
                  "and the height after it."),
            ("p", "The worked example <code>sixteen-keys-t2</code> inserts sixteen keys in one "
                  "shuffled order with `t = 2`. It makes 6 splits, 20 reads and 34 writes, the 34 "
                  "being 16 leaf writes and 3 for each split, and finishes with 9 nodes at height "
                  "2, under a bound of about 3.09. Choose <code>sixteen-keys-t3</code>: the same "
                  "keys at `t = 3` make 3 splits, 11 reads and 25 writes and leave 5 nodes at "
                  "height 1, under 1.95. At <code>sixteen-keys-t5</code> one split turns the "
                  "single full leaf into a root over two leaves: 3 nodes, height 1, 7 reads. A "
                  "larger t means fewer, fuller pages and a lower tree, which is the whole reason "
                  "for the structure."),
            ("p", "<code>thirty-two-keys-t2</code> inserts 32 keys at `t = 2`: height 3 under a "
                  "bound of about 4.04, 16 nodes, 12 splits, 62 reads and 68 writes. The bound is "
                  "a ceiling for every tree on 32 keys, and this order stays a level below it. "
                  "<code>ascending-t3</code> sends 1 to 30 in increasing order at `t = 3` and "
                  "makes 11 splits and 14 nodes for 30 keys, height 2 under 2.49: each split "
                  "leaves a left half at the minimum `t − 1` keys that no later key will visit, "
                  "so sorted input leaves most nodes at the minimum. Both counts describe their orders; "
                  "the theorem holds for all of them."),
            ("h3", "Exercise"),
            ("p", "Insert `12, 3, 7, 18, 25, 1, 9, 15, 21, 30` in that order into an empty B-tree "
                  "with `t = 2`, splitting full nodes on the way down. Draw the tree after each "
                  "split, and count the splits, DISK-READs and DISK-WRITEs by the rule above. "
                  "Then type the keys into the lab and compare."),
            ("p", "A B-tree keeps its keys in order for searching. The next lesson, Fibonacci "
                  "Heaps, gives up that order almost entirely, keeping only enough to find a "
                  "minimum, and puts off nearly all its work until a minimum is taken out."),
        ],
        "lab": ("itakit", {
            "mode": "btree",
            "view": "insert",
            "preset": "sixteen-keys-t2",
            "presets": [
                {"id": "sixteen-keys-t2",
                 "label": "Sixteen keys in one shuffled order, t = 2",
                 "t": "2", "keys": BT_KEYS,
                 "expect": {"btiHeight": "2", "btiNodes": "9", "btiSplits": "6",
                            "btiReads": "20", "btiWrites": "34",
                            "btiBound": "log_2 8.5 ≈ 3.09"}},
                {"id": "sixteen-keys-t3",
                 "label": "The same sixteen keys, t = 3",
                 "t": "3", "keys": BT_KEYS,
                 "expect": {"btiHeight": "1", "btiNodes": "5", "btiSplits": "3",
                            "btiReads": "11", "btiWrites": "25",
                            "btiBound": "log_3 8.5 ≈ 1.95"}},
                {"id": "sixteen-keys-t5",
                 "label": "The same sixteen keys, t = 5",
                 "t": "5", "keys": BT_KEYS,
                 "expect": {"btiHeight": "1", "btiNodes": "3", "btiSplits": "1",
                            "btiReads": "7",
                            "btiLevels": "[17] / [1 2 4 6 8 9 11 13] [19 22 26 28 30 33 35]"}},
                {"id": "thirty-two-keys-t2",
                 "label": "Thirty-two keys in one shuffled order, t = 2",
                 "t": "2",
                 "keys": ("41 7 63 22 88 15 54 3 70 29 96 11 47 35 82 58 1 76 19 66 92 26 "
                          "44 9 51 85 31 13 60 99 5 38"),
                 "expect": {"btiHeight": "3", "btiNodes": "16", "btiSplits": "12",
                            "btiReads": "62", "btiWrites": "68",
                            "btiBound": "log_2 16.5 ≈ 4.04"}},
                {"id": "ascending-t3",
                 "label": "The keys 1 to 30 in increasing order, t = 3",
                 "t": "3",
                 "keys": ("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 "
                          "26 27 28 29 30"),
                 "expect": {"btiHeight": "2", "btiNodes": "14", "btiSplits": "11",
                            "btiBound": "log_3 15.5 ≈ 2.49"}},
            ],
            "panel_title": "Grow a B-tree and count its disk accesses",
            "panel_intro": (
                "Choose the minimum degree t and type keys separated by spaces. The lab inserts "
                "them in order with B-TREE-INSERT, splitting every full node on the way down, "
                "and counts splits, DISK-READs and DISK-WRITEs by the book's conventions, beside "
                "Theorem 18.1's bound on the height. The counts are this order's; the bound "
                "holds for every B-tree on the same number of keys."
            ),
        }),
        "steps_title": "Inserting into a B-tree by hand",
        "steps_intro": "Four steps on paper, then one on keys of your own.",
        "steps": [
            ("Fix the capacity",
             "From t, write down the most keys a node may hold, `2t − 1`, and the fewest a "
             "non-root node may hold, `t − 1`. A node at the most is full."),
            ("Split a full root first",
             "If the root is full, make a new empty root above it, move the old root's median "
             "up into it, and give it the two halves as children. Count three writes."),
            ("Walk down, splitting before you step",
             "At each internal node pick the child whose range holds the key and count a read. "
             "If that child is full, split it, move its median into the current node, count three "
             "writes, and step into whichever half now holds the key, without a second read."),
            ("Insert at the leaf",
             "Place the key in order in the leaf you reach, which cannot be full, and count one "
             "write. Check that every leaf is still at the same depth."),
            ("Do it on keys of your own",
             "Write twelve distinct numbers, insert them by hand with `t = 2`, then type them "
             "into the lab and compare your splits, reads, writes and final tree with the tiles."),
        ],
        "worked": {
            "title": "Eight keys at t = 2",
            "intro": [
                "Insert `50, 20, 80, 10, 30, 60, 90, 40` into an empty B-tree with `t = 2`, so a "
                "node holds at most 3 keys. The root starts as an empty leaf in memory.",
            ],
            "lines": [
                "50, 20, 80: one leaf fills; 3 writes",
                "10: root full; split it",
                "   [50] over [20] and [80]; 3 writes",
                "   read [20]; write [10 20]",
                "30, 60, 90: 1 read and 1 write each",
                "40: read [10 20 30]; it is full",
                "   split: 20 rises to [20 50]; 3 writes",
                "   step into [30] unread; write [30 40]",
                "2 splits, 5 reads, 14 writes",
                "[20 50] / [10] [30 40] [60 80 90]",
            ],
            "after": [
                "The height is 1 and the bound is `log_2 4.5 ≈ 2.17`, so a height of 2 was also "
                "possible for 8 keys. The read of [20] when 10 arrives is the call made just after "
                "the root split, on a node still in memory. The fourteen writes are the eight leaf "
                "writes plus three for each of the two splits. Notice that the node [10] was left at the minimum of "
                "`t − 1 = 1` key by the second split and that the full leaf [60 80 90] stays full "
                "until a key passes through it.",
            ],
        },
        "quiz_title": "Occupancy, height and disk accesses",
        "quiz": [
            {"q": "Insert the exercise's keys `12, 3, 7, 18, 25, 1, 9, 15, 21, 30` into an empty "
                  "B-tree with `t = 2`. What is the final tree, and how many splits, DISK-READs "
                  "and DISK-WRITEs are made?",
             "a": ["`[7 18] / [1 3] [9 12 15] [21 25 30]`; 2 splits, 7 reads, 16 writes",
                   "`[7 18] / [1 3] [9 12 15] [21 25 30]`; 2 splits, 17 reads, 16 writes",
                   "`[7 18] / [1 3] [9 12 15] [21 25 30]`; 2 splits, 7 reads, 10 writes",
                   "`[7 15] / [1 3] [9 12] [18 21 25 30]`; 2 splits, 7 reads, 16 writes"],
             "c": 0,
             "why": "The root splits when 18 arrives, giving [7] over [3] and [12]; the leaf "
                    "[12 18 25] splits when 9 arrives, sending 18 up. Every insertion from 18 on "
                    "reads one child, 7 reads, and the root is never read, so 17 counts the root "
                    "ten times over. The writes are 10 leaf writes plus 3 for each split, "
                    "16; 10 forgets the splits. A node of four keys is impossible at `t = 2`, where "
                    "the most is 3."},
            {"q": "A B-tree with minimum degree `t = 3` holds 1,000 keys. What is the greatest "
                  "height it can have?",
             "a": ["9", "6", "5", "4"],
             "c": 2,
             "why": "Theorem 18.1 gives `h ≤ log_3(1001/2) = log_3 500.5 ≈ 5.66`, and h is a whole "
                    "number, so h ≤ 5. Check it against the count: height 5 needs at least "
                    "`2·3⁵ − 1 = 485` keys, which 1,000 exceeds, and height 6 needs 1,457, which it "
                    "does not. Six rounds the logarithm up instead of down; nine is about lg 1000, "
                    "a binary tree's height; four is possible but not the greatest."},
            {"q": "Why does B-TREE-INSERT split every full node it meets on the way down, rather "
                  "than only the nodes that actually overflow?",
             "a": ["It guarantees the parent of any node being split has room for the median, so "
                   "the insertion never has to go back up the tree",
                   "It never makes more splits than splitting only on overflow would",
                   "It keeps every node exactly half full",
                   "It keeps the tree's height lower than splitting on overflow would"],
             "c": 0,
             "why": "Splitting before stepping in means every node the procedure enters has room, "
                    "so the median of a split always fits in its parent and one downward pass "
                    "suffices. It can split a full node the new key would not have overflowed, so "
                    "it may make more splits, not fewer. Nodes range from `t − 1` to `2t − 1` keys, "
                    "not exactly half. Height grows only when the root splits in either scheme."},
            {"q": "An insertion into a B-tree of height 3 splits no node. With the root held in "
                  "memory, how many DISK-READs and DISK-WRITEs does it make?",
             "a": ["4 reads and 1 write", "3 reads and 1 write", "3 reads and 3 writes",
                   "3 reads and no writes"],
             "c": 1,
             "why": "It steps from the root down three levels, reading each child once, 3 reads; "
                    "the root itself is never read, so 4 is one too many. It writes only the leaf "
                    "that receives the key, 1 write. Three writes is the cost of a split, which did "
                    "not happen, and a leaf that gains a key must be written back."},
        ],
        "mistakes": [
            ("Expecting a B-tree's height to be about lg n",
             "A B-tree is balanced like a red-black tree, so `O(lg n)` is true, but the "
             "Theorem 18.1 bound is a logarithm to the base t, and t is chosen large. The same "
             "sixteen keys stand at height 2 with `t = 2` and at height 1 with `t = 3` or "
             "`t = 5`; in the authors' illustration, with 1,001 children a node, a tree of "
             "height 2 holds over a billion keys and two page reads find any of them."),
            ("Picturing a B-tree growing downward at its leaves",
             "A binary search tree hangs a new leaf below an old one; a B-tree never does. Keys "
             "go into existing leaves, full nodes split sideways, and the only new level is a "
             "new root above a split one, which is why every leaf stays at the same depth. "
             "Watch the height column in the lab's table: it rises only on an insertion that "
             "split the root."),
            ("Pricing B-tree operations by comparisons",
             "Inside a node a search makes up to `2t − 1` comparisons, so its CPU time is "
             "`O(t·log_t n)`, more than a binary tree's when t is large. The chapter's point is "
             "that this is cheap beside the disk: the cost that counts is pages read and "
             "written, `O(h)`, which is why the lab counts DISK-READs and DISK-WRITEs and not "
             "comparisons."),
        ],
        "standard": (
            "Finish when you can grow a B-tree by hand and price it in disk accesses.",
            "Given t and ten to twelve keys, produce the tree B-TREE-INSERT builds, count its "
            "splits, reads and writes, and check its height against Theorem 18.1's bound."
        ),
        "note": (
            "The lab inserts only; deletion, Section 18.3, is set out in prose. Its disk counts "
            "follow the chapter's conventions, the root in memory and B-TREE-CREATE's first "
            "write left out, and they describe the order of keys on screen. The height bound is "
            "Theorem 18.1's, for every B-tree on the same number of keys."
        ),
    },
    # ---------------------------------------------------------------- 02
    # CLRS Chapter 19 opening and sections 19.1-19.2, pp. 505-518.
    # Quotes: p. 510, 12 words, and p. 507, 4 words, quotes.py OK.
    # Lesson total: 16 words.
    # Mergeable heaps and the two extra operations (p. 505); Figure 19.1's
    # comparison and theory against practice (pp. 506-507); the structure,
    # degree, mark, H.min, H.n (pp. 507-509); the potential (19.1) and D(n)
    # (p. 509); MAKE-FIB-HEAP, insert, minimum, union and their potential
    # changes (pp. 510-512); EXTRACT-MIN, CONSOLIDATE, FIB-HEAP-LINK, the
    # while-loop invariant and the O(D(n)) amortized bound (pp. 512-518).
    {
        "slug": "fibonacci-heaps",
        "title": "Fibonacci Heaps",
        "module": "Chapter 19 · Fibonacci Heaps",
        "one_line": "A Fibonacci heap inserts and unites in constant time by only adding roots to a list, and pays for the delay when the minimum is extracted, with a potential that charges one unit for every root waiting to be tidied.",
        "summary": (
            "Sections 19.1 and 19.2 build a mergeable heap out of min-heap-ordered trees whose "
            "roots sit in one circular list. Insertion and union add roots and do nothing else; "
            "EXTRACT-MIN removes the minimum, promotes its children and consolidates the root "
            "list until no two roots share a degree. The potential t(H) + 2m(H) turns that "
            "bargain into amortized bounds: constant for insertion and union, O(D(n)) for "
            "extraction. Run one extraction by hand, then watch the lab charge every operation "
            "its actual cost and its change in potential."
        ),
        "key": [
            "a list of min-heap-ordered trees",
            "Φ(H) = t(H) + 2m(H)",
            "insert and union only add roots",
            "EXTRACT-MIN consolidates the roots",
            "after it, no two roots share a degree",
            "extraction is O(D(n)) amortized",
        ],
        "key_label": "Sections 19.1 and 19.2 in six lines",
        "concepts_intro": (
            "Three ideas: the interface the chapter implements, the shape that implements it, "
            "and the bookkeeping that prices it."
        ),
        "concepts": [
            ("Mergeable heap",
             "A structure supporting MAKE-HEAP, INSERT, MINIMUM, EXTRACT-MIN and UNION, the last "
             "combining two heaps into one. Fibonacci heaps add DECREASE-KEY and DELETE, which are "
             "the next lesson's. A binary heap does everything but UNION in `O(lg n)`; its union "
             "costs `Θ(n)`, which is the gap this chapter closes."),
            ("Root list",
             "The roots of all the heap's trees, linked in a circular, doubly linked list so that "
             "a node can be added or removed anywhere, and two lists spliced together, in constant "
             "time. The pointer H.min marks the root with the least key; every other root is "
             "unordered, waiting for the next extraction to tidy it."),
            ("Potential",
             "The function `Φ(H) = t(H) + 2m(H)`: how many trees the root list holds, plus twice "
             "the number of marked nodes. It starts at 0 and never goes negative, so by "
             "Chapter 17's potential method the amortized costs, each the actual cost plus the "
             "change in Φ, add up to at least the actual total."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the chapter opening and sections 19.1 and 19.2 in your own copy first. The "
            "lesson sets out the argument in its own words, runs one extraction by hand, and "
            "then lets the lab price every operation of a longer sequence."
        ),
        "body": [
            ("p", "&ldquo;The mergeable-heap operations on Fibonacci heaps delay work as long as "
                  "possible.&rdquo; That sentence opens Section 19.2, and the whole chapter is an "
                  "account of what the delay buys and who pays for it. This lesson reads the "
                  "chapter opening and sections 19.1 and 19.2: the operations a mergeable heap "
                  "supports, the trees and lists a Fibonacci heap is made of, the potential "
                  "function, and the three operations that leave all the work to the fourth."),
            ("p", "The chapter opens with a comparison. A binary heap, the structure of "
                  "Chapter 6, inserts, extracts and decreases keys in `Θ(lg n)` worst-case time, "
                  "but uniting two of them means concatenating the arrays and rebuilding, `Θ(n)`. "
                  "A Fibonacci heap inserts, unites and decreases a key in `Θ(1)` amortized time, "
                  "and extracts or deletes in `O(lg n)` amortized. The authors name two cautions "
                  "of their own. These are amortized bounds, not per-operation ones; and the "
                  "constant factors and the programming effort make the structure, in their "
                  "words, &ldquo;predominantly of theoretical interest.&rdquo; Its appeal is "
                  "greatest where extractions are few beside the other operations, as in graph "
                  "algorithms that may decrease a key once per edge (Chapters 23 and 24)."),
            ("def", ("Fibonacci heap",
                     "A collection of rooted trees, each obeying the min-heap property, whose "
                     "roots form a circular, doubly linked root list. Each node keeps a parent "
                     "pointer, a pointer to one child, its siblings in a circular child list, its "
                     "degree (the number of children) and a boolean mark. The heap keeps H.min, "
                     "the root with the least key, and H.n, the number of nodes. Siblings and roots "
                     "may appear in any order.")),
            ("p", "Section 19.1 sets up the analysis. With `t(H)` trees in the root list and "
                  "`m(H)` marked nodes, the potential is `t(H) + 2m(H)`; the marks play no part "
                  "until the next lesson, and here every mark is false. The analysis also needs "
                  "a bound `D(n)` on the largest degree a node can have in a heap of n nodes. When only the "
                  "mergeable-heap operations are used, `D(n) ≤ ⌊lg n⌋` (Problem 19-2 asks for the "
                  "proof); the next lesson shows `D(n) = O(lg n)` in general."),
            ("p", "Section 19.2's first three operations are short. FIB-HEAP-INSERT makes the new "
                  "node a one-node tree, adds it to the root list beside H.min, and updates H.min "
                  "if the new key is smaller; t rises by one, so the amortized cost is the constant "
                  "actual cost plus 1. Finding the minimum reads H.min and changes nothing. "
                  "FIB-HEAP-UNION splices two root lists and keeps the smaller minimum; the trees "
                  "and marks of the result are those of the two heaps together, so the potential "
                  "does not change at all. None of the three ever looks at a tree's shape."),
            ("p", "FIB-HEAP-EXTRACT-MIN is where the delayed work is done. It moves every child of "
                  "the minimum node z into the root list, removes z, and calls CONSOLIDATE, which "
                  "takes the roots one at a time and keeps an array A indexed by degree. When a root "
                  "x arrives and `A[d]` already holds a root y of the same degree d, the two are "
                  "linked: FIB-HEAP-LINK makes the one with the larger key a child of the other, "
                  "clears its mark, and raises the survivor's degree to `d + 1`, and the step "
                  "repeats at the new degree. The authors prove the inner loop with an invariant, "
                  "that at the start of each iteration d is x's degree. At the end at most one root "
                  "of each degree is left, and the root list is rebuilt from A."),
            ("thm", ("Extraction is O(D(n)) amortized",
                     "The actual cost is `O(D(n) + t(H))`: at most D(n) children are moved, and "
                     "CONSOLIDATE handles at most `D(n) + t(H) − 1` roots, each link removing one. "
                     "Afterwards at most `D(n) + 1` roots remain and no node has been marked, so "
                     "the potential falls from `t(H) + 2m(H)` to at most `D(n) + 1 + 2m(H)`. Scaling "
                     "the unit of potential to cover the constant in `O(t(H))`, the amortized cost "
                     "is `O(D(n))`.")),
            ("p", "The lab does not scale the unit: it charges one step for the minimum, one for "
                  "each child moved, and one for each root CONSOLIDATE takes, and one unit of "
                  "potential for each root. On those terms the sum can be done exactly. With c "
                  "children and t roots before and t′ after, the actual cost is `1 + c + (t − 1 + c)` "
                  "and the potential changes by `t′ − t` when no node is marked, so the amortized "
                  "cost is `2c + t′`: the children counted twice and the surviving roots once, "
                  "both bounded by the degree bound, and the t roots that were waiting cost nothing "
                  "net."),
            ("math", [
                "the degree bounds the lab prints, beside ⌊lg n⌋",
                "",
                "n        ⌊lg n⌋     ⌊log_φ n⌋",
                "4          2           2",
                "7          2           4",
                "8          3           4",
                "16         4           5",
                "100        6           9",
            ]),
            ("p", "Now the lab. Type operations as words and keys, `insert 12`, `min`, `extract`, "
                  "and it runs them on an empty heap, placing each new root just left of H.min and "
                  "consolidating from the old minimum's right neighbour, as the chapter's figures "
                  "do. The tiles are the actual and the amortized cost of the whole sequence; the "
                  "potential now, written out as `t(H) + 2m(H)`; the largest amortized cost of any "
                  "one operation of each kind; the root list read from H.min; the largest degree "
                  "beside `⌊log_φ n⌋`, the bound the next lesson proves; and n. The table prices "
                  "every operation separately."),
            ("p", "The worked example <code>eight-inserts</code> inserts eight keys and stops. "
                  "Nothing has been tidied: the root list is all eight keys, the potential is 8, "
                  "the actual cost is 8 and the amortized cost 16, two per insertion, one spent and "
                  "one stored. Choose <code>then-extract</code>, which adds one EXTRACT-MIN. The "
                  "extraction scans seven roots, actual cost 8, and links them into three trees of "
                  "degrees 0, 1 and 2, so the potential falls from 8 to 3 and the amortized cost "
                  "is 3; the totals are 16 actual and 19 amortized, and 19 is 16 plus the "
                  "potential left over, as it must be when the heap started empty."),
            ("p", "<code>extract-twice</code> extracts again. Now the minimum has two children, "
                  "so the extraction moves 2, scans 4 roots and costs 7, and leaves two roots, so "
                  "its amortized cost is `2·2 + 2 = 6`. <code>seventeen-inserts</code> inserts 17 "
                  "keys and extracts the least: the single extraction costs 17 actual steps and "
                  "links all 16 survivors into one "
                  "tree of degree 4, so the potential falls from 17 to 1 and the amortized cost "
                  "is 1. The 16 units the insertions stored paid for the 16 roots scanned. "
                  "<code>mixed</code> interleaves extractions, a <code>min</code> and new "
                  "insertions, and ends with 7 nodes in three trees, 31 actual steps and 34 "
                  "amortized; its dearest extraction is charged 9."),
            ("h3", "Exercise"),
            ("p", "On an empty heap, run `insert 6, insert 2, insert 9, insert 4, insert 7, "
                  "insert 1, insert 8, extract` by hand, placing each new root just left of H.min "
                  "and consolidating from the old minimum's right neighbour. Write the root list "
                  "after the extraction and the extraction's actual cost, change in potential and "
                  "amortized cost. Then type the operations into the lab."),
            ("p", "Extraction pays for itself because roots carry potential. The next lesson, "
                  "Decreasing a Key and Bounding the Degree, gives the marks their work, cuts nodes "
                  "out of their trees in constant amortized time, and proves the degree bound the "
                  "whole analysis has been assuming."),
        ],
        "lab": ("itakit", {
            "mode": "fibheap",
            "view": "ops",
            "preset": "eight-inserts",
            "presets": [
                {"id": "eight-inserts",
                 "label": "Eight insertions and nothing else",
                 "ops": FH_EIGHT,
                 "expect": {"fhiActual": "8", "fhiAmortized": "16",
                            "fhiPhi": "t(H) + 2m(H) = 8 + 2 × 0 = 8",
                            "fhiRoots": "3 (min), 7, 12, 25, 18, 9, 30, 15",
                            "fhiDegree": "max degree 0; ⌊log_φ 8⌋ = 4"}},
                {"id": "then-extract",
                 "label": "The same eight insertions, then one extraction",
                 "ops": FH_EIGHT + " extract",
                 "expect": {"fhiActual": "16", "fhiAmortized": "19",
                            "fhiPhi": "t(H) + 2m(H) = 3 + 2 × 0 = 3",
                            "fhiMostAm": "insert 2, extract-min 3",
                            "fhiRoots": "7 (min), 15, 9",
                            "fhiDegree": "max degree 2; ⌊log_φ 7⌋ = 4"}},
                {"id": "extract-twice",
                 "label": "The same eight insertions, then two extractions",
                 "ops": FH_EIGHT + " extract extract",
                 "expect": {"fhiActual": "23", "fhiAmortized": "25",
                            "fhiMostAm": "insert 2, extract-min 6",
                            "fhiRoots": "9 (min), 18"}},
                {"id": "seventeen-inserts",
                 "label": "Seventeen insertions, then one extraction",
                 "ops": ("insert 1 insert 2 insert 3 insert 4 insert 5 insert 6 insert 7 insert 8 "
                         "insert 9 insert 10 insert 11 insert 12 insert 13 insert 14 insert 15 "
                         "insert 16 insert 17 extract"),
                 "expect": {"fhiActual": "34", "fhiAmortized": "35",
                            "fhiMostAm": "insert 2, extract-min 1",
                            "fhiRoots": "2 (min)",
                            "fhiDegree": "max degree 4; ⌊log_φ 16⌋ = 5"}},
                {"id": "mixed",
                 "label": "Eight insertions, an extraction, a min, two insertions, two extractions",
                 "ops": FH_EIGHT + " extract min insert 1 insert 40 extract extract",
                 "expect": {"fhiActual": "31", "fhiAmortized": "34",
                            "fhiMostAm": "insert 2, extract-min 9, min 1",
                            "fhiRoots": "9 (min), 12, 18", "fhiN": "7"}},
            ],
            "panel_title": "Run a Fibonacci heap and price every operation",
            "panel_intro": (
                "Type operations separated by spaces or commas: insert k, min, extract. The lab "
                "runs them on an empty heap and charges each its actual cost in steps and its "
                "change in the potential t(H) + 2m(H); their sum is the amortized cost. The totals "
                "describe this sequence; the chapter's bounds hold for every sequence."
            ),
        }),
        "steps_title": "Running a Fibonacci heap by hand",
        "steps_intro": "Four steps on paper, then one on a sequence of your own.",
        "steps": [
            ("Keep the root list as a circle",
             "Write the roots in a row, read round from H.min. Put each inserted key just left "
             "of H.min and move H.min if the new key is smaller. Add 1 to t for each."),
            ("Extract: promote, then remove",
             "Move the minimum's children into the root list where it stood, remove it, and count "
             "1 plus the number of children."),
            ("Consolidate by degree",
             "Starting at the old minimum's right neighbour and going round, take each root once. "
             "If an earlier root has the same degree, link the larger key under the smaller and "
             "check again at the new degree. Count one step for each root taken."),
            ("Price it",
             "Add the steps for the actual cost, subtract t before from t after for the change in "
             "potential, and add the two. With no marks, the result is twice the children plus the "
             "roots left."),
            ("Do it on a sequence of your own",
             "Write ten insertions and two extractions, run them by hand, then type them into the "
             "lab and compare your root lists and costs with its table."),
        ],
        "worked": {
            "title": "Five insertions and one extraction",
            "intro": [
                "Run `insert 40, insert 10, insert 30, insert 20, insert 50, extract` on an empty "
                "heap. Each insertion goes just left of H.min, which is 10 from the second on, so "
                "the circle read from 10 is 10, 40, 30, 20, 50.",
            ],
            "lines": [
                "5 insertions: 5 roots, Φ = 5, cost 5",
                "extract 10: no children; 4 roots left",
                "scan from 40, the right neighbour:",
                "   40, 30: link 40 under 30 (degree 1)",
                "   20, 50: link 50 under 20 (degree 1)",
                "   degree 1 twice: 30 goes under 20",
                "one root, 20, of degree 2; Φ = 1",
                "actual 1 + 0 + 4 = 5; ΔΦ = −4",
                "amortized 5 − 4 = 1",
            ],
            "after": [
                "Over the whole sequence the actual cost is 10 and the amortized cost 11, which is "
                "10 plus the final potential of 1. The tree rooted at 20 has 4 nodes and degree 2, "
                "and `⌊log_φ 4⌋ = 2`, so it sits exactly at the degree bound. Type the six "
                "operations into the lab to see the same root list and costs.",
            ],
        },
        "quiz_title": "Roots, links and potential",
        "quiz": [
            {"q": "Run the exercise, `insert 6, insert 2, insert 9, insert 4, insert 7, insert 1, "
                  "insert 8, extract`, on an empty heap. What is the root list afterwards, and "
                  "what are the extraction's actual cost, change in potential and amortized cost?",
             "a": ["Roots 2 (min) and 7; actual 7, ΔΦ = −5, amortized 2",
                   "Roots 2 (min) and 7; actual 7, ΔΦ = −5, amortized 12",
                   "One root, 2; actual 7, ΔΦ = −6, amortized 1",
                   "Roots 2 (min) and 7; actual 6, ΔΦ = −5, amortized 1"],
             "c": 0,
             "why": "Before the extraction the circle from 1 is 1, 2, 6, 9, 4, 7, 8. Removing 1 "
                    "leaves six roots, scanned from 2: 6 goes under 2, 9 under 4, then 4 under 2 "
                    "(both degree 1), and 8 under 7. Roots 2, of degree 2, and 7, of degree 1, "
                    "remain; they differ in degree, so they are not linked, which rules out one "
                    "root. The actual cost is 1 for the minimum plus 6 roots scanned, 7; t falls "
                    "from 7 to 2. The amortized cost is `7 − 5 = 2`, not 7 + 5."},
            {"q": "Nine keys are inserted into an empty Fibonacci heap and nothing else is done. "
                  "What are the potential and the total amortized cost?",
             "a": ["Φ = 9, amortized total 18", "Φ = 9, amortized total 9",
                   "Φ = 1, amortized total 10", "Φ = 0, amortized total 9"],
             "c": 0,
             "why": "Insertion never links, so nine one-node trees sit in the root list: t = 9, "
                    "no marks, Φ = 9. Each insertion costs 1 and raises Φ by 1, an amortized 2, "
                    "18 in all, which is the actual 9 plus the stored 9. One root would need a "
                    "consolidation, which only EXTRACT-MIN performs."},
            {"q": "Why does EXTRACT-MIN's amortized cost not grow with t(H), the number of roots "
                  "waiting when it is called?",
             "a": ["Each root scanned either survives, and there are at most D(n) + 1 survivors, "
                   "or is linked, and each link lowers the potential by one, paying for its scan",
                   "Because t(H) is never more than D(n) + 1",
                   "Because CONSOLIDATE skips the roots of degree 0",
                   "Because EXTRACT-MIN is called less often than INSERT"],
             "c": 0,
             "why": "The scan's cost is proportional to the roots it handles, and every root that "
                    "does not survive was linked under another, taking one unit of potential "
                    "with it. The root list can be long before an extraction (eight insertions "
                    "leave eight roots, beyond `D(8) + 1`); only afterwards is it short. "
                    "CONSOLIDATE takes every root, of any degree. How often operations are called "
                    "has no place in the bound on each operation's amortized cost."},
            {"q": "The lab prints the degree bound `⌊log_φ n⌋`. What is it at n = 16, and how "
                  "does it compare with ⌊lg 16⌋?",
             "a": ["5, one more than ⌊lg 16⌋ = 4", "4, the same as ⌊lg 16⌋",
                   "3, one less than ⌊lg 16⌋", "16, since a root can have every node as a child"],
             "c": 0,
             "why": "φ is about 1.618, so `φ⁵ ≈ 11.09 ≤ 16 < φ⁶ ≈ 17.94` and `⌊log_φ 16⌋ = 5`. "
                    "The base φ is smaller than 2, so the bound is larger than `⌊lg 16⌋ = 4`; "
                    "4 is the tighter bound Problem 19-2 proves when only mergeable-heap "
                    "operations are used. A root with fifteen children is impossible because "
                    "roots are only linked at equal degree."},
        ],
        "mistakes": [
            ("Reading a constant amortized bound as a cheap operation every time",
             "Insertion's amortized cost is 2 in the lab's units, but the amortized bound "
             "promises only that the total stays within the sum of the amortized costs. Single "
             "operations can be expensive: on <code>seventeen-inserts</code> one extraction "
             "costs 17 actual steps. It is cheap amortized, 1, because the insertions before it "
             "stored the potential that pays for it."),
            ("Expecting the root list to stay short",
             "Nothing tidies the root list except EXTRACT-MIN. Insertions and unions only add "
             "roots, so after eight insertions there are eight roots, and a long run of them can "
             "leave thousands. Every one carries a unit of potential, and the next extraction "
             "spends it; the shortness of the list is a fact about the moment after an "
             "extraction, not a rule."),
            ("Linking any two roots to shorten the list",
             "CONSOLIDATE links only roots of equal degree, and that restriction is what keeps "
             "degrees small: two trees of degree d make one of degree d + 1, much as a binomial "
             "tree doubles. On the exercise, roots of degrees 2 and 1 are left side by side. "
             "Linking unequal roots would shorten the list and lose the bound on degree that the "
             "amortized cost of extraction depends on."),
        ],
        "standard": (
            "Finish when you can run a Fibonacci heap by hand and price each operation.",
            "Given six to ten insertions and one or two extractions, produce the root list after "
            "each extraction and compute every operation's actual cost, change in t(H) + 2m(H) "
            "and amortized cost."
        ),
        "note": (
            "The lab has no UNION operation, since its change in potential is 0 and its work is "
            "one splice; the lesson sets it out in prose. Its actual costs are counts of steps "
            "under its stated rules, with one unit of potential a root, and the root-list order "
            "is the chapter's convention. Both describe the sequence on screen; the bounds are "
            "the chapter's."
        ),
    },
    # ---------------------------------------------------------------- 03
    # CLRS sections 19.3-19.4, pp. 518-526.
    # Quote: p. 522, 33 words, quotes.py OK. Lesson total: 33 words.
    # FIB-HEAP-DECREASE-KEY, CUT and CASCADING-CUT (pp. 519-520); what a mark
    # records (p. 520); the amortized analysis with c calls and the change in
    # potential at most 4 - c (pp. 520-522); FIB-HEAP-DELETE (p. 522);
    # Lemma 19.1 on the children's degrees, Lemmas 19.2-19.3 on Fibonacci
    # numbers, Lemma 19.4 and Corollary 19.5 (pp. 523-526).
    {
        "slug": "decrease-key-and-the-degree-bound",
        "title": "Decreasing a Key and Bounding the Degree",
        "module": "Chapter 19 · Fibonacci Heaps",
        "one_line": "A key that falls below its parent's is cut out to the root list, a node that loses a second child is cut after it, and the marks that enforce this rule are what force every node of degree k to have at least F(k + 2) nodes beneath it.",
        "summary": (
            "Section 19.3 decreases a key by cutting the node from its parent and, when the "
            "parent has already lost a child, cutting the parent too, in a chain of cascading "
            "cuts that stops at a root or an unmarked node. The marked nodes in the potential "
            "pay for the chain, so DECREASE-KEY costs O(1) amortized, and DELETE is a decrease "
            "followed by an extraction. Section 19.4 then proves the degree bound: a node of "
            "degree k heads a subtree of at least F(k + 2) ≥ φ^k nodes. Cut by hand, then let the "
            "lab count cuts, marks and the lemma at every node."
        ),
        "key": [
            "a key below its parent's: cut it out",
            "a marked node losing a child is cut too",
            "cascading cuts stop at a root or unmarked",
            "DECREASE-KEY is O(1) amortized",
            "size(x) ≥ F(k + 2) ≥ φᵏ at degree k",
            "so D(n) ≤ ⌊log_φ n⌋",
        ],
        "key_label": "Sections 19.3 and 19.4 in six lines",
        "concepts_intro": (
            "Three ideas: the operation that breaks trees apart, the one bit of history that "
            "limits it, and the quantity that history protects."
        ),
        "concepts": [
            ("Cut",
             "Removing a node, with its whole subtree, from its parent's child list and adding it "
             "to the root list as a new tree, unmarked. DECREASE-KEY cuts a node only when its new "
             "key is smaller than its parent's, the one case where heap order is broken."),
            ("Mark",
             "A boolean on each node recording that it has lost one child since it was last made "
             "a child of another node. A new node is unmarked, linking clears the mark, and a "
             "marked node that loses a second child is itself cut by CASCADING-CUT."),
            ("Size of a node",
             "How many nodes the subtree rooted at x contains, x included, written `size(x)`. "
             "Section 19.4 shows it is exponential in x's degree, which is what bounds the degree "
             "of every node by a logarithm of n."),
        ],
        "read_title": "The section's argument first, then the count",
        "read_intro": (
            "Read sections 19.3 and 19.4 in your own copy first. The lesson sets out the argument "
            "in its own words, cuts one tree by hand, and then lets the lab count cuts, marks and "
            "the size lemma on longer sequences."
        ),
        "body": [
            ("p", "&ldquo;One unit of potential pays for the cut and the clearing of the mark bit, "
                  "and the other unit compensates for the unit increase in potential due to node y "
                  "becoming a root.&rdquo; That is the authors' answer, at the end of their analysis "
                  "of DECREASE-KEY, to the question the last lesson left open: why the potential "
                  "counts each marked node twice. This lesson reads sections 19.3 and 19.4: how a "
                  "key is decreased and a node deleted, what the marks are for, and why a node of "
                  "degree k must have a Fibonacci number of nodes below it."),
            ("p", "FIB-HEAP-DECREASE-KEY lowers x's key to a value no larger than the old one. If "
                  "x is a root, or its new key is still at least its parent y's, nothing is "
                  "violated and nothing moves. Otherwise CUT removes x from y's child list, makes it "
                  "an unmarked root, and CASCADING-CUT is called on y. That procedure does nothing at "
                  "a root; marks y if y was unmarked, since y has just lost its first child; and if y "
                  "was already marked, cuts y as well and calls itself on y's parent. The chain climbs "
                  "until it reaches a root or an unmarked node. Finally H.min is updated, since the "
                  "only key that changed is x's."),
            ("p", "The mark is a small piece of history. Suppose a node was a root, was then linked "
                  "under another node, and then lost two children to cuts. The authors' rule is "
                  "that the second loss cuts the node from its parent at once. The mark records the "
                  "state between the first loss and the second, which is why CUT clears it (the node "
                  "becomes a root again) and why FIB-HEAP-LINK clears it (the node has just been "
                  "made a child)."),
            ("thm", ("DECREASE-KEY is O(1) amortized",
                     "Suppose one call makes c calls of CASCADING-CUT. Its actual cost is `O(c)`. "
                     "Afterwards there are `t(H) + c` trees: the original ones, x's, and the `c − 1` cut by cascading. At "
                     "most `m(H) − c + 2` nodes are marked: `c − 1` lost their mark when cut, and "
                     "the last call may have marked one. So the potential rises by at most "
                     "`c + 2·(2 − c) = 4 − c`, and with the unit of potential scaled to cover the "
                     "constant in `O(c)`, the amortized cost is `O(1)`.")),
            ("p", "The lab's units make the constant visible. It charges one step for the decrease "
                  "and one for each cut, so a call with c calls of CASCADING-CUT, which makes c cuts "
                  "when its last call cuts nothing, costs `1 + c`; with one unit of potential a root "
                  "the change is at most `4 − c`; so no DECREASE-KEY can cost more than "
                  "`1 + c + 4 − c = 5` amortized, however long its cascade. A decrease that breaks "
                  "no heap order costs 1. FIB-HEAP-DELETE gives x the smallest possible key, which "
                  "the lab writes as minus infinity, by DECREASE-KEY and then calls EXTRACT-MIN, so "
                  "its amortized cost is `O(1) + O(D(n))`."),
            ("p", "Section 19.4 earns the degree bound. Take a node x of degree k and list its "
                  "children in the order they were linked to it. Lemma 19.1 says the first has "
                  "degree at least 0 and the i-th, for `i ≥ 2`, degree at least `i − 2`: when the "
                  "i-th was linked, x already had the `i − 1` earlier ones, and CONSOLIDATE links "
                  "only equal degrees, so the child had degree at least `i − 1` then; since then it "
                  "can have lost at most one child, or it would have been cut away from x."),
            ("thm", ("Lemma 19.4 and Corollary 19.5",
                     "For any node x of degree k, `size(x) ≥ F(k + 2) ≥ φᵏ`, where `F(0) = 0`, "
                     "`F(1) = 1` and each later Fibonacci number adds the two before it, and "
                     "`φ = (1 + √5)/2 ≈ 1.618`. The proof bounds the least possible size `s(k)` by "
                     "`2 + s(0) + s(1) + … + s(k − 2)` using Lemma 19.1, and Lemmas 19.2 and 19.3 "
                     "turn that sum into `F(k + 2)` and then into `φᵏ`. Since `n ≥ size(x) ≥ φᵏ`, "
                     "every degree is at most `⌊log_φ n⌋`, so `D(n) = O(lg n)`.")),
            ("math", [
                "the least size of a node of degree k",
                "",
                "k          0     1     2     3     4     5",
                "F(k + 2)   1     2     3     5     8    13",
                "φᵏ         1   1.62  2.62  4.24  6.85  11.09",
                "2ᵏ         1     2     4     8    16    32",
            ]),
            ("p", "The last row is the size of a binomial tree, the shape consolidation alone "
                  "produces: a tree linked from two trees of degree `k − 1`. Cuts let a node of degree "
                  "k fall well below `2ᵏ`, and the marks stop the fall at `F(k + 2)`. The structure "
                  "is named for that Fibonacci row, and the base φ of the logarithm the last "
                  "lesson's lab printed comes from it too."),
            ("p", "Now the lab, the same heap with a second set of tiles. Its operations add "
                  "`decrease k v` and `delete k`. The tiles count the cuts made by decreases and "
                  "deletions, the cascading cuts among them, and the calls of CASCADING-CUT; list "
                  "the marked nodes now; give the largest amortized cost of any one DECREASE-KEY; "
                  "check Lemma 19.4 at every node and name the node closest to the bound, the one "
                  "with the least ratio of size to `F(k + 2)`; and repeat the degree bound and the "
                  "root list. Every preset starts from the same tree: seventeen insertions of 10, "
                  "20, …, 170 and one extraction leave 16 nodes in a single tree rooted at 20, whose "
                  "children are 30; 40 over 50; 60 over 70 and over 80, which is over 90; and 100, "
                  "whose own children 110; 120 over 130; and 140 over 150 and 160, which is over "
                  "170, repeat the first three in shape."),
            ("p", "The worked example <code>fresh-tree</code> stops there: no cuts, nothing "
                  "marked, one root, degree 4 against the bound 5, and the lemma holds at all 16 "
                  "nodes, closest at 40, of degree 1 and size 2, which is exactly `F(3) = 2` (the leaves, each of size `1 = F(2)`, are just as close; the lab breaks the tie toward the larger degree). Choose "
                  "<code>one-cascade</code>, the worked example below: three decreases make 4 cuts, "
                  "1 of them cascading, in 4 calls of CASCADING-CUT, and leave no node marked; the "
                  "largest amortized DECREASE-KEY is 5, the ceiling, and the root list read from "
                  "H.min is 3, 60, 4, 5, 20."),
            ("p", "<code>two-cascades</code> marks 160, 140 and 100 by cutting one child from each, "
                  "then decreases 160 itself: 160 is cut, its parent 140 is marked and is cut, and "
                  "140's parent 100 is marked and is cut, stopping at the root 20. That makes 6 cuts "
                  "in all, 2 cascading, and the largest amortized decrease is still 5; the long "
                  "cascade itself was cheap, because the three marks it cleared had been paid for "
                  "when they were set. <code>cascade-then-extract</code> adds an extraction, which "
                  "leaves 15 nodes in three trees, the lemma holding at every node. "
                  "<code>two-deletes</code> deletes 140 and then 60: 2 cuts, no cascade, and 100 is "
                  "left marked, having lost 140."),
            ("h3", "Exercise"),
            ("p", "Start from the lab's 16-node tree and, by hand, run `decrease 130 9`, "
                  "`decrease 150 8`, `decrease 160 7`. For each, say what is cut and what is marked. "
                  "Count the cuts, the cascading cuts and the calls of CASCADING-CUT, list the "
                  "marked nodes at the end, and find a node whose size equals `F(k + 2)` exactly. "
                  "Then add the three operations to the end of a preset's list in the lab."),
            ("p", "A Fibonacci heap's operations all compare keys, and Chapter 20 opens by noting "
                  "that any comparison-based heap must spend `Ω(lg n)` somewhere. The next lesson, "
                  "van Emde Boas Trees, steps outside that bound by assuming the keys are small "
                  "integers."),
        ],
        "lab": ("itakit", {
            "mode": "fibheap",
            "view": "cascade",
            "preset": "fresh-tree",
            "presets": [
                {"id": "fresh-tree",
                 "label": "Seventeen insertions and one extraction: one tree of 16 nodes",
                 "ops": FH_TREE,
                 "expect": {"fhiCuts": "0", "fhiMarked": "0: none",
                            "fhiLemma": "holds at all 16; closest 40: degree 1, size 2, F(3) = 2",
                            "fhiDegree": "max degree 4; ⌊log_φ 16⌋ = 5",
                            "fhiRoots": "20 (min)"}},
                {"id": "one-cascade",
                 "label": "The same tree, then three decreases under 60",
                 "ops": FH_TREE + " decrease 70 5 decrease 90 4 decrease 80 3",
                 "expect": {"fhiCuts": "4", "fhiCascades": "1", "fhiCalls": "4",
                            "fhiMarked": "0: none", "fhiMostDec": "5",
                            "fhiRoots": "3 (min), 60, 4, 5, 20"}},
                {"id": "two-cascades",
                 "label": "The same tree, then four decreases under 100",
                 "ops": FH_TREE + " decrease 170 1 decrease 150 2 decrease 110 3 decrease 160 4",
                 "expect": {"fhiCuts": "6", "fhiCascades": "2", "fhiCalls": "6",
                            "fhiMarked": "0: none", "fhiMostDec": "5",
                            "fhiRoots": "1 (min), 20, 2, 3, 4, 140, 100"}},
                {"id": "cascade-then-extract",
                 "label": "The four decreases under 100, then an extraction",
                 "ops": (FH_TREE + " decrease 170 1 decrease 150 2 decrease 110 3 decrease 160 4"
                         " extract"),
                 "expect": {"fhiCuts": "6", "fhiCascades": "2",
                            "fhiLemma": "holds at all 15; closest 4: degree 1, size 2, F(3) = 2",
                            "fhiRoots": "2 (min), 20, 100"}},
                {"id": "two-deletes",
                 "label": "The same tree, then delete 140 and delete 60",
                 "ops": FH_TREE + " delete 140 delete 60",
                 "expect": {"fhiCuts": "2", "fhiCascades": "0", "fhiCalls": "2",
                            "fhiMarked": "1: 100", "fhiRoots": "20 (min), 80, 70"}},
            ],
            "panel_title": "Cut, cascade and check the size lemma",
            "panel_intro": (
                "Type operations separated by spaces or commas: insert k, min, extract, decrease k "
                "v, delete k. The lab runs them on an empty heap, counts every cut, cascading cut "
                "and call of CASCADING-CUT, keeps the marks, and checks Lemma 19.4's bound on "
                "subtree size at every node. The counts are this sequence's; the lemma and the "
                "amortized bound are the chapter's, for every sequence."
            ),
        }),
        "steps_title": "Decreasing keys by hand",
        "steps_intro": "Four steps on paper, then one on a sequence of your own.",
        "steps": [
            ("Draw the tree with its marks",
             "Write each node with its children below it and a star on each marked node. Roots "
             "are never cut, so a star on a root does no work."),
            ("Decrease and test the parent",
             "Lower the key. If it is still at least its parent's, or the node is a root, stop: "
             "actual cost 1, no change in potential."),
            ("Cut and climb",
             "Otherwise move the node to the root list unmarked. Go to its old parent: at a root "
             "stop; if unmarked, star it and stop; if starred, cut it too, unstar it, and go to its "
             "parent. Count each visit as one call of CASCADING-CUT and each removal as one cut."),
            ("Price it",
             "Actual cost is 1 plus the cuts. The change in potential is the new roots plus twice "
             "the change in stars. Check the sum is at most 5."),
            ("Do it on a sequence of your own",
             "Starting from the lab's 16-node tree, choose four decreases that produce a cascade of "
             "length two, predict the cuts and marks, then add them to a preset in the lab and "
             "compare."),
        ],
        "worked": {
            "title": "Three decreases under 60",
            "intro": [
                "Start from the 16-node tree rooted at 20, with Φ = 1. Node 60 has children 70 and "
                "80, and 80 has the child 90. Run `decrease 70 5`, `decrease 90 4`, "
                "`decrease 80 3`.",
            ],
            "lines": [
                "70 → 5: below 60, so cut; 60 marked",
                "   actual 2, ΔΦ = 1 + 2 = 3, amortized 5",
                "90 → 4: below 80, so cut; 80 marked",
                "   actual 2, ΔΦ = 3, amortized 5",
                "80 → 3: cut 80, clearing its mark",
                "   60 is marked: cut 60 too",
                "   60's parent 20 is a root: stop",
                "   actual 3, ΔΦ = 2 − 2·2 = −2",
                "   amortized 1",
                "4 cuts, 1 cascading, 4 calls",
            ],
            "after": [
                "The roots are now 3, 60, 4, 5 and 20, read from H.min, nothing is marked, and Φ = 5. The third "
                "decrease did the most work and cost the least amortized, because it cleared two "
                "marks the first two had paid for. Choose <code>one-cascade</code> in the lab to "
                "see each step in its table.",
            ],
        },
        "quiz_title": "Cuts, marks and the size lemma",
        "quiz": [
            {"q": "From the 16-node tree, run the exercise's `decrease 130 9`, `decrease 150 8`, "
                  "`decrease 160 7`. How many cuts are made, how many of them cascading, and which "
                  "nodes are marked at the end?",
             "a": ["4 cuts, 1 cascading; 100 and 120 marked",
                   "3 cuts, none cascading; 120 and 140 marked",
                   "5 cuts, 2 cascading; nothing marked",
                   "4 cuts, 1 cascading; 100, 120 and 140 marked"],
             "c": 0,
             "why": "Cutting 130 marks 120; cutting 150 marks 140; cutting 160 finds 140 already "
                    "marked, so 140 is cut too and 100, unmarked, is marked. That is 4 cuts, one "
                    "cascading. Three cuts ignores the cascade; five treats 100 as marked, which it "
                    "was not. A cut clears the mark of the node it moves, so 140 ends unmarked. "
                    "Node 100 is left with children 110 and 120 and size 3, exactly `F(4) = 3`."},
            {"q": "A DECREASE-KEY on an unmarked node makes c = 3 calls of CASCADING-CUT: two "
                  "cascading cuts, then a call that marks a node. In the lab's units, what are its "
                  "actual cost, change in potential and amortized cost?",
             "a": ["actual 4, ΔΦ = 1, amortized 5", "actual 4, ΔΦ = −1, amortized 3",
                   "actual 4, ΔΦ = 7, amortized 11", "actual 2, ΔΦ = 1, amortized 3"],
             "c": 0,
             "why": "Three cuts (x and two cascading) plus the decrease cost 4. Three new roots add "
                    "3; the two cascading cuts clear two marks, −4; the last call sets one, +2; so "
                    "ΔΦ = 1 and the amortized cost is 5. Leaving out the new mark gives −1 and 3; "
                    "counting the two cleared marks as added, +4, and dropping the new one gives 7; "
                    "and counting only x's cut misses two steps."},
            {"q": "What is the least size Lemma 19.4 allows a node of degree 5 in a Fibonacci "
                  "heap?",
             "a": ["32", "13", "11", "6"],
             "c": 1,
             "why": "The bound is `F(k + 2) = F(7) = 13`. Thirty-two is `2⁵`, the size of a binomial "
                    "tree of degree 5, which cuts can reduce. Eleven is `⌊φ⁵⌋`, a weaker bound the "
                    "lemma also proves, but the lemma's sharper bound, 13, already rules it out. Six "
                    "would be a node with five leaf children, which Lemma 19.1 forbids: its later "
                    "children must have children of their own."},
            {"q": "Why does the potential count each marked node twice?",
             "a": ["When a cascading cut moves a marked node, clearing its mark releases two "
                   "units: one pays for the cut, one for the new root it adds",
                   "Because a marked node is twice as likely as an unmarked one to be cut",
                   "Because every marked node will later be linked twice",
                   "Because the marks double the bound on the degree"],
             "c": 0,
             "why": "Each cascading cut costs a step and adds a root, raising t by one; it also "
                    "clears a mark, lowering 2m by two, so the cut is paid for and t's rise is "
                    "covered, with nothing left over. Weighted once, the marks would leave the "
                    "cascade unpaid. The other options are not claims the analysis makes or needs."},
        ],
        "mistakes": [
            ("Cutting every node whose key is decreased",
             "DECREASE-KEY cuts only when the new key is below the parent's, the one case where "
             "min-heap order breaks; a decrease that keeps order changes one field and costs 1. On "
             "the lab's tree, decreasing 70 to 65 moves nothing, since 65 is still above 60; "
             "decreasing it to 5 cuts it. A root is never cut, whatever its new key."),
            ("Fearing that cascading cuts make DECREASE-KEY expensive",
             "One call can climb a long chain, and on <code>two-cascades</code> the last decrease "
             "cuts three nodes. But every node a cascade cuts was marked, and its mark had stored "
             "two units of potential; the amortized cost of every decrease in the lab is at most "
             "5, the constant the analysis predicts for its units. The actual cost of one call is "
             "not bounded by a constant; the amortized cost is."),
            ("Assuming every tree in the heap is a binomial tree",
             "Consolidation alone builds binomial shapes, with `2ᵏ` nodes at degree k, and the "
             "last lesson's bound `⌊lg n⌋` holds for them. Cuts break the shape, and the bound "
             "Section 19.4 proves is `size(x) ≥ F(k + 2)`, so the degree bound becomes "
             "`⌊log_φ n⌋`, larger than `⌊lg n⌋`. The lab's lemma tile checks the Fibonacci bound, "
             "not the binomial one."),
        ],
        "standard": (
            "Finish when you can decrease keys by hand and keep the marks.",
            "Given a Fibonacci heap's trees with their marks and three or four decreases, produce "
            "every cut and cascading cut, the marks afterwards, each decrease's amortized cost, "
            "and the size bound at a node of your choice."
        ),
        "note": (
            "The lab's costs are steps under its stated rules, with one unit of potential a root "
            "and two a mark, so its ceiling of 5 for DECREASE-KEY is the chapter's O(1) in those "
            "units. Its lemma check covers the nodes of the heap on screen; the lemma itself is "
            "proved for every node of every Fibonacci heap."
        ),
    },
    # ---------------------------------------------------------------- 04
    # CLRS Chapter 20 opening and sections 20.1-20.3, pp. 531-556.
    # Quote: p. 544, 20 words, quotes.py OK. Lesson total: 20 words.
    # The comparison lower bound for priority queues and the integer escape
    # (p. 531); n against u, MEMBER (p. 532); bit vector, binary tree of bits,
    # tree of degree sqrt(u) (pp. 532-535); recurrence (20.2), high, low, index
    # (pp. 536-538); proto-vEB structures and their operations, recurrences
    # (20.3) and the successor's Theta(lg u lg lg u), deletion left to the
    # exercises (pp. 538-544); vEB trees, upper and lower square roots, min and
    # max, recurrence (20.4), O(u) space and creation (pp. 545-549); MEMBER,
    # SUCCESSOR, INSERT and DELETE and why each makes one call that recurses
    # (pp. 549-556).
    {
        "slug": "van-emde-boas-trees",
        "title": "van Emde Boas Trees",
        "module": "Chapter 20 · van Emde Boas Trees",
        "one_line": "When keys are integers below u, a structure that splits each key into a cluster number and a position, and recurses into a universe of size √u at most once per level, answers every dynamic-set query in O(lg lg u) time.",
        "summary": (
            "Chapter 20 escapes the comparison lower bound by assuming the keys are distinct "
            "integers from 0 to u − 1. Section 20.1 tries a bit vector and trees laid over it; "
            "Section 20.2 makes the idea recursive, a summary and √u clusters each of universe "
            "√u, and finds that two recursive calls per level cost Θ(lg u); Section 20.3 adds a "
            "minimum and a maximum to each structure and brings every operation down to one "
            "call that recurses, O(lg lg u). Count one structure's calls by hand, then set the "
            "two structures side by side in the lab over universes up to 65,536."
        ),
        "key": [
            "keys are distinct integers 0 to u − 1",
            "high(x) = ⌊x/√u⌋, low(x) = x mod √u",
            "T(u) = T(√u) + O(1) = O(lg lg u)",
            "proto-vEB recurses twice: Θ(lg u)",
            "vEB keeps min out, max at hand",
            "one call that recurses, per level",
        ],
        "key_label": "Chapter 20 in six lines",
        "concepts_intro": (
            "Three ideas: the way a key is split, the recurrence the split is designed to obey, "
            "and the two fields that let the structure obey it."
        ),
        "concepts": [
            ("Universe, clusters and summary",
             "The universe is the set of possible keys, 0 to `u − 1`. It is divided into `√u` "
             "clusters of `√u` consecutive values; key x lies in cluster `high(x) = ⌊x/√u⌋` at "
             "position `low(x) = x mod √u`. A summary records which clusters are nonempty, and is "
             "itself a set over a universe of `√u` values."),
            ("The square-root recurrence",
             "`T(u) = T(√u) + O(1)`. Substituting `m = lg u` turns it into "
             "`S(m) = S(m/2) + O(1)`, which the master method solves as `O(lg m)`, so "
             "`T(u) = O(lg lg u)`. An operation obeys it when it does constant work at a level "
             "and recurses at most once."),
            ("min and max",
             "Fields that a van Emde Boas tree keeps at every level. The minimum is stored only "
             "there, not in any cluster; the maximum is stored there and in its cluster. They "
             "answer MINIMUM and MAXIMUM without recursion, tell whether a successor lies in x's "
             "own cluster, and make inserting into an empty tree constant work."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the chapter opening and sections 20.1 to 20.3 in your own copy first. The "
            "lesson sets out the argument in its own words, counts the calls of four operations "
            "by hand, and then sets the two recursive structures side by side in the lab."
        ),
        "body": [
            ("p", "&ldquo;Clearly, we need to modify the proto-vEB structure to get each operation "
                  "down to making at most one recursive call.&rdquo; The authors write it at the end "
                  "of Section 20.2, having built a recursive structure that has exactly the right "
                  "shape and still runs too slowly, and Section 20.3 is the modification. This "
                  "lesson reads Chapter 20: why integer keys allow a faster priority queue, the "
                  "recurrence that sets the target, the structure that misses it, and the tree "
                  "that meets it."),
            ("p", "The chapter opens with a limit. Binary heaps, red-black trees and Fibonacci "
                  "heaps all spend `Θ(lg n)` on some operation, and they must: a structure that only "
                  "compares keys and could both insert and extract the minimum in `o(lg n)` time "
                  "could sort n keys with `o(n lg n)` comparisons, which Section 8.1 forbids. Counting "
                  "sort escaped that bound by using the keys as array indices, and van Emde Boas "
                  "trees escape it the same way: if the keys are distinct integers from 0 to "
                  "`u − 1`, with u a power of 2, each dynamic-set operation takes "
                  "`O(lg lg u)` time in the worst case. From here on n counts the elements and u the "
                  "universe, and MEMBER replaces SEARCH, since only keys are stored."),
            ("p", "Section 20.1 tries three warm-ups. A bit vector of u bits inserts, deletes and "
                  "tests membership in constant time, but its minimum and successor may scan "
                  "`Θ(u)` bits. A binary tree of bits laid over the vector, each internal bit the "
                  "logical or of its children, brings every operation to `O(lg u)`, one walk up and "
                  "one down. A tree of degree `√u` laid over it instead has height 2: a summary of "
                  "`√u` bits, one per cluster, over the clusters themselves, and its queries take "
                  "`O(√u)`. That looks like a step backwards, and the authors say so; but it is the "
                  "split the rest of the chapter makes recursive."),
            ("def", ("high, low and index",
                     "For a universe of size u, `high(x) = ⌊x/√u⌋` is x's cluster number, the "
                     "upper half of its `lg u` bits; `low(x) = x mod √u` is its position inside "
                     "the cluster, the lower half; and `index(x, y) = x·√u + y` puts them back "
                     "together, so `x = index(high(x), low(x))`. Inside a cluster or a summary the "
                     "same functions are taken with that structure's own, smaller u.")),
            ("p", "Section 20.2 sets the target before building anything. A structure that spends "
                  "constant time at a level and then recurses once into a universe of `√u` obeys "
                  "`T(u) = T(√u) + O(1)`, and the change of variables `m = lg u` gives "
                  "`S(m) = S(m/2) + O(1)`, so `O(lg m)`, which is `O(lg lg u)`. The other way to "
                  "see it: the number of bits in the universe size halves at each level, from "
                  "`lg u` down to 1, and halving `lg u` reaches 1 after `lg lg u` steps."),
            ("math", [
                "the levels below a universe of u = 2^(2^k)",
                "",
                "u            √u        lg u    lg lg u",
                "4             2          2        1",
                "16            4          4        2",
                "256          16          8        3",
                "65,536      256         16        4",
                "2^32      65,536        32        5",
            ]),
            ("p", "The proto van Emde Boas structure, proto-vEB(u), follows the plan literally for "
                  "`u = 2^(2^k)`. At `u = 2` it is an array of two bits; above that it holds a "
                  "summary and `√u` clusters, each a proto-vEB(`√u`). PROTO-vEB-MEMBER drills "
                  "straight down through `cluster[high(x)]` and meets the target, `O(lg lg u)`. "
                  "PROTO-vEB-MINIMUM must ask the summary for the first nonempty cluster and then ask "
                  "that cluster for its minimum: two calls a level, `T(u) = 2T(√u) + O(1)`, which "
                  "solves to `Θ(lg u)`. PROTO-vEB-SUCCESSOR can search x's cluster, then the summary, "
                  "then call MINIMUM, and costs `Θ(lg u·lg lg u)`; PROTO-vEB-INSERT inserts into the "
                  "cluster and into the summary, `Θ(lg u)`. Deletion is harder still, since a "
                  "summary bit can be cleared only when its cluster is empty, and the book leaves it "
                  "to Exercises 20.2-2 and 20.2-3."),
            ("thm", ("Two calls a level",
                     "An insertion into proto-vEB(u) always recurses into both a cluster and the "
                     "summary, so at `u = 2^(2^k)` it makes `1 + 2 + 4 + … + 2ᵏ = 2^(k+1) − 1` calls, "
                     "which is `2·lg u − 1`: 7 at u = 16, 15 at u = 256, 31 at u = 65,536. Doubling "
                     "the calls at each of `lg lg u` levels multiplies them by `2^(lg lg u) = lg u`.")),
            ("p", "Section 20.3's van Emde Boas tree, vEB(u), keeps the shape and adds two fields "
                  "at every level, min and max, with one twist: the minimum is not stored in any "
                  "cluster. (It also allows any power of 2 as u, splitting the bits into an upper "
                  "and a lower square root when `lg u` is odd; the lab keeps to `u = 2^(2^k)`.) Now "
                  "MINIMUM and MAXIMUM read a field. SUCCESSOR compares low(x) with the maximum of "
                  "x's cluster and so knows, without a call, whether to recurse into the cluster or "
                  "into the summary, never both. INSERT into an empty tree sets min and max; "
                  "otherwise it first swaps x with min when x is smaller, so that the old minimum is "
                  "the element carried down, and then, if x's cluster is empty, it recurses into the summary and fills the "
                  "cluster in constant time, and if the cluster is not empty the summary already "
                  "knows it, and it recurses into the cluster only. The price is space: a vEB tree "
                  "takes `O(u)` space and `O(u)` time to create (Problem 20-1)."),
            ("p", "DELETE is the one operation that can make two recursive calls, one into x's "
                  "cluster and one into the summary, and the authors show it still obeys the "
                  "recurrence. The summary call happens only when the cluster has just become "
                  "empty, which means x was its only element, and deleting the only element of a vEB "
                  "tree is constant work, setting min and max to nothing. So at any level one of the "
                  "two calls is cheap. Deleting the minimum itself needs one more step: the next "
                  "smallest element is fetched from the first nonempty cluster, becomes the new min, "
                  "and is deleted from its cluster in its place."),
            ("p", "Now the lab. Give it k, which sets `u = 2^(2^k)`, and a list of operations, "
                  "`insert x`, `member x`, `successor x`, `delete x`; it runs every operation on a "
                  "proto-vEB structure and a vEB tree side by side and counts each structure's "
                  "procedure calls, the top call included. It does not count VEB-TREE-MINIMUM, "
                  "VEB-TREE-MAXIMUM or VEB-EMPTY-TREE-INSERT, which only read or set fields, and its "
                  "proto-vEB deletion is its own answer to Exercise 20.2-2, stated in its rules. The "
                  "tiles are the universe, the two totals, the most calls either made in one "
                  "operation, the answers to the queries, the members at the end, and the vEB tree's "
                  "top level: its min and max, the clusters its summary lists, and each cluster's "
                  "low parts with the elements they stand for."),
            ("p", "The worked example <code>worked-u16</code> is the sequence below: 32 proto-vEB "
                  "calls against 9 vEB calls, and the successor of 6 is 11. Choose "
                  "<code>mixed-u16</code>, eleven operations at `u = 16`: 82 calls against 31, at "
                  "most 11 in one proto-vEB operation and 5 in one vEB operation. Its top level shows "
                  "min 9, max 10 and cluster 2 holding the low part 2, the element 10: 9 is the "
                  "minimum, so it sits in no cluster at all."),
            ("p", "<code>mixed-u256</code> and <code>mixed-u65536</code> run the same eleven "
                  "operations with `lg lg u` at 3 and 4. The proto-vEB totals climb to 142 and 258, "
                  "each insertion alone costing 15 and then 31 calls, while the vEB totals barely "
                  "move, 37 and 38, at most 6 and 5 in one operation. "
                  "<code>spread-u65536</code> uses keys scattered across the whole universe: 360 "
                  "proto-vEB calls against 30, and one proto-vEB successor makes 57 calls where the "
                  "vEB tree makes at most 5. These are counts on these sequences; the bounds are the "
                  "recurrences'."),
            ("h3", "Exercise"),
            ("p", "With `u = 16`, run `insert 3`, `insert 14`, `insert 8`, `successor 3`, "
                  "`delete 3` on an empty vEB tree by hand. For each operation write high and low at "
                  "every level you visit and count the calls, the top call included, not counting "
                  "MINIMUM, MAXIMUM or EMPTY-TREE-INSERT. Then type the operations into the lab."),
            ("p", "A van Emde Boas tree keeps one set and answers questions about order. The next "
                  "lesson, Disjoint Sets, keeps many sets at once and answers only which set an "
                  "element is in, with a structure so simple its analysis needed a new function to "
                  "state."),
        ],
        "lab": ("itakit", {
            "mode": "veb",
            "view": "ops",
            "preset": "worked-u16",
            "presets": [
                {"id": "worked-u16",
                 "label": "Three insertions and a successor, u = 16",
                 "k": "2", "ops": "insert 6 insert 11 insert 4 successor 6",
                 "expect": {"vbiProto": "32", "vbiVeb": "9",
                            "vbiAnswers": "successor 6: 11",
                            "vbiTop": ("min 4, max 11; summary: 1, 2; cluster 1: 2 (6); "
                                       "cluster 2: 3 (11)")}},
                {"id": "mixed-u16",
                 "label": "Eleven mixed operations, u = 16",
                 "k": "2", "ops": VEB_OPS,
                 "expect": {"vbiU": "u = 16, √u = 4, lg lg u = 2", "vbiProto": "82",
                            "vbiVeb": "31", "vbiMost": "proto-vEB 11, vEB 5",
                            "vbiAnswers": ("member 10: yes; member 11: no; successor 5: 9; "
                                           "successor 10: 13; successor 13: none"),
                            "vbiTop": "min 9, max 10; summary: 2; cluster 2: 2 (10)"}},
                {"id": "mixed-u256",
                 "label": "The same eleven operations, u = 256",
                 "k": "3", "ops": VEB_OPS,
                 "expect": {"vbiU": "u = 256, √u = 16, lg lg u = 3", "vbiProto": "142",
                            "vbiVeb": "37", "vbiMost": "proto-vEB 19, vEB 6"}},
                {"id": "mixed-u65536",
                 "label": "The same eleven operations, u = 65,536",
                 "k": "4", "ops": VEB_OPS,
                 "expect": {"vbiU": "u = 65,536, √u = 256, lg lg u = 4", "vbiProto": "258",
                            "vbiVeb": "38", "vbiMost": "proto-vEB 35, vEB 5"}},
                {"id": "spread-u65536",
                 "label": "Keys spread across the universe, u = 65,536",
                 "k": "4",
                 "ops": ("insert 300 insert 40000 insert 40001 insert 65535 member 40001 "
                         "successor 300 successor 40001 successor 65535 delete 300 delete 40000"),
                 "expect": {"vbiProto": "360", "vbiVeb": "30", "vbiMost": "proto-vEB 57, vEB 5",
                            "vbiMembers": "2: 40001, 65535"}},
            ],
            "panel_title": "Count the calls of two recursive structures",
            "panel_intro": (
                "Choose k, which sets u = 2^(2^k), and type operations separated by spaces or "
                "commas: insert x, member x, successor x, delete x. The lab runs them on a "
                "proto-vEB structure and on a van Emde Boas tree over the same universe and counts "
                "each structure's recursive calls. The counts are this sequence's; the bounds are "
                "the chapter's recurrences, for every sequence."
            ),
        }),
        "steps_title": "Counting a vEB tree's calls by hand",
        "steps_intro": "Four steps on paper, then one on a sequence of your own.",
        "steps": [
            ("Draw the levels",
             "From u write the universe at each level, `u, √u, …, 2`, and for each element you "
             "use, high and low at every level."),
            ("Keep min out of the clusters",
             "At each level hold min and max apart. When a smaller element arrives, swap it into "
             "min and carry the old minimum down instead."),
            ("Recurse once",
             "For an insertion into a nonempty tree: if x's cluster is empty, recurse into the "
             "summary with high(x) and set the cluster's min and max to low(x); otherwise recurse "
             "into the cluster. For a successor: compare low(x) with the cluster's max and recurse "
             "into the cluster or the summary, not both. Count one call per level entered."),
            ("Compare with proto-vEB",
             "For the same operation count the proto-vEB calls: insertion always enters both the "
             "cluster and the summary, `2·lg u − 1` calls in all."),
            ("Do it on a sequence of your own",
             "Write five operations at `u = 16`, count both structures' calls by hand, then type "
             "them into the lab and compare with its table."),
        ],
        "worked": {
            "title": "Three insertions and a successor at u = 16",
            "intro": [
                "Run `insert 6`, `insert 11`, `insert 4`, `successor 6` on an empty vEB(16). At the "
                "top `√u = 4`, so 6 is cluster 1, low 2; 11 is cluster 2, low 3; 4 is cluster 1, "
                "low 0.",
            ],
            "lines": [
                "insert 6: empty; min = max = 6; 1 call",
                "insert 11: cluster 2 empty",
                "   summary gets 2; cluster 2 gets 3",
                "   2 calls",
                "insert 4: below min; 4 is min, 6 goes down",
                "   cluster 1 empty: summary gets 1",
                "   summary had min 2: 1 goes below it",
                "   3 calls",
                "successor 6: low 2 = cluster 1's max",
                "   so ask the summary for after 1: 2",
                "   answer 2·4 + 3 = 11; 3 calls",
                "vEB 1 + 2 + 3 + 3 = 9",
                "proto-vEB 7 + 7 + 7 + 11 = 32",
            ],
            "after": [
                "Inserting 1 into the summary, a vEB(4) holding only 2, swaps 1 into its min and "
                "carries 2 down, which costs one more call into the summary's own summary: that is "
                "the third call of `insert 4`. The successor's answer is cluster 2's min, 3, read "
                "from a field. Choose <code>worked-u16</code> in the lab to see the same counts in "
                "its table.",
            ],
        },
        "quiz_title": "Clusters, calls and recurrences",
        "quiz": [
            {"q": "With `u = 16`, run the exercise, `insert 3, insert 14, insert 8, successor 3, "
                  "delete 3`, on an empty vEB tree. How many calls does each operation make, the "
                  "top call included, and what is the successor of 3?",
             "a": ["1, 2, 3, 2, 5 calls, 13 in all; the successor of 3 is 8",
                   "1, 2, 2, 2, 5 calls, 12 in all; the successor of 3 is 8",
                   "1, 1, 1, 2, 3 calls, 8 in all; the successor of 3 is 8",
                   "1, 2, 3, 2, 5 calls, 13 in all; the successor of 3 is 14"],
             "c": 0,
             "why": "Insert 14 enters the summary once; insert 8 enters the summary, which then "
                    "swaps 2 below its min 3 and enters its own summary, 3 calls. The successor "
                    "of 3 finds cluster 0 empty, asks the summary, whose min 2 answers at once, and "
                    "returns `2·4 + 0 = 8`, 2 calls; 14 skips 8. Deleting the minimum 3 pulls 8 up "
                    "and deletes it from cluster 2 (1 call), which empties it, so 2 is deleted from "
                    "the summary (3 calls), 5 in all. Missing the summary's own summary gives 12; "
                    "one call per insertion ignores the summary."},
            {"q": "With `u = 2^32`, how many times can the universe be square-rooted before it "
                  "reaches the base size 2?",
             "a": ["32", "16", "5", "65,536"],
             "c": 2,
             "why": "The universe sizes are `2^32, 2^16, 2^8, 2^4, 2^2, 2`, five steps, and "
                    "`lg lg 2^32 = lg 32 = 5`. Thirty-two is `lg u`, the height of a binary tree of "
                    "bits; 16 is the exponent of `√u`; 65,536 is `√u` itself, the number of "
                    "clusters at the top."},
            {"q": "Why does PROTO-vEB-MINIMUM take `Θ(lg u)` time rather than `O(lg lg u)`?",
             "a": ["Each call asks the summary for the first nonempty cluster and then asks that "
                   "cluster for its minimum, so `T(u) = 2T(√u) + O(1)`",
                   "It scans the `√u` clusters one by one, so `T(u) = T(√u) + Θ(√u)`",
                   "Each call shrinks the universe only to `u/2`, so there are `lg u` levels",
                   "It must call PROTO-vEB-SUCCESSOR at each level"],
             "c": 0,
             "why": "Two recursive calls on universes of `√u` give `S(m) = 2S(m/2) + O(1)` with "
                    "`m = lg u`, which is `Θ(m) = Θ(lg u)` by the master method's first case. The "
                    "summary removes any scan of clusters; each level shrinks the universe to its "
                    "square root, not its half; and MINIMUM calls only itself (it is SUCCESSOR "
                    "that calls MINIMUM)."},
            {"q": "Why does keeping a vEB tree's minimum out of its clusters let VEB-TREE-INSERT "
                  "make only one recursive call?",
             "a": ["If x's cluster is empty, x can become that cluster's min and max in constant "
                   "time, so only the summary needs a recursive call; if it is not empty, the "
                   "summary already records it, so only the cluster does",
                   "Because with max also stored, insertion never touches the summary",
                   "Because the minimum is the only element that is ever inserted into a summary",
                   "Because the clusters are allocated only when they are first used"],
             "c": 0,
             "why": "An empty vEB tree takes an element by setting two fields, which is why the "
                    "empty-cluster case costs nothing below the summary, and a nonempty cluster's "
                    "number is already in the summary. Insertion does touch the summary, whenever a "
                    "cluster receives its first element; any cluster number can be inserted into a "
                    "summary; and allocation has nothing to do with the number of calls."},
        ],
        "mistakes": [
            ("Expecting O(lg lg n) in the number of elements",
             "The bound is in u, the size of the universe, not n, the number of keys stored, and "
             "it holds only because the keys are integers below u. The space is `O(u)` too, "
             "however few keys there are: the lab's <code>spread-u65536</code> stores four keys "
             "in a universe of 65,536, and creating the tree costs `O(u)` time, which, the "
             "authors note, can exceed what a few operations save."),
            ("Thinking the square-root split alone gives lg lg u",
             "proto-vEB has exactly the split and the levels, and still costs `Θ(lg u)` to insert "
             "or find a minimum, because it recurses twice at a level. The recurrence "
             "`T(u) = T(√u) + O(1)` needs at most one recursive call. On the lab's universe of "
             "65,536 every proto-vEB insertion makes 31 calls, `2·lg u − 1`, while the vEB "
             "insertions there make at most 4."),
            ("Treating min like the other elements",
             "A vEB tree's minimum lives only in its min field, not in a cluster, which is what "
             "makes insertion into an empty tree constant work. Forgetting it gives wrong "
             "successors and wrong deletions: deleting the minimum must fetch the next smallest "
             "from the first nonempty cluster, make it the new min, and delete it from its "
             "cluster. The lab's top-level tile lists min apart from the clusters for this "
             "reason."),
        ],
        "standard": (
            "Finish when you can count a vEB tree's calls by hand.",
            "Given a universe of 16 and four or five operations, produce high and low at each "
            "level, each operation's calls in a vEB tree and in a proto-vEB structure, and the "
            "answers to the queries."
        ),
        "note": (
            "The lab keeps to universes of the form 2^(2^k), as Section 20.2 does, so the upper "
            "and lower square roots of Section 20.3 never differ; it counts procedure calls, not "
            "time, and its proto-vEB deletion is its own. The counts describe the sequence on "
            "screen; the bounds are the chapter's recurrences."
        ),
    },
    # ---------------------------------------------------------------- 05
    # CLRS Chapter 21, sections 21.1-21.4, pp. 561-585 (21.4 starred: its
    # definitions read, its proof named).
    # Quote: p. 569, 12 words, quotes.py OK. Lesson total: 12 words.
    # MAKE-SET, UNION, FIND-SET, n and m, connected components (pp. 561-564);
    # linked lists, the simple union's Theta(n^2) sequence, the weighted-union
    # heuristic and Theorem 21.1 (pp. 564-567); forests, union by rank, path
    # compression, LINK and the two-pass FIND-SET, the bounds for each
    # heuristic alone and together (pp. 568-572); A_k(j), alpha(n), Lemma 21.4
    # and the potential-method proof named (pp. 573-575).
    {
        "slug": "disjoint-sets",
        "title": "Disjoint Sets",
        "module": "Chapter 21 · Data Structures for Disjoint Sets",
        "one_line": "A collection of disjoint sets can be kept as a forest of rooted trees in which every union hangs the lower-ranked root under the higher and every find points its whole path at the root, and then m operations cost O(m α(n)), linear in m for every n that could ever occur.",
        "summary": (
            "Chapter 21 maintains a collection of disjoint sets under three operations: make a "
            "set, unite two sets, and find which set an element is in. Section 21.2 keeps each "
            "set as a linked list and, by always appending the shorter list, bounds m operations "
            "by O(m + n lg n); Section 21.3 keeps each set as a tree, where ranked unions and "
            "path compression together bring m operations to O(m α(n)), where α grows so "
            "slowly that Section 21.4's starred analysis is needed to say how slowly. Run a "
            "small sequence by hand, then switch each heuristic on and off in the lab."
        ),
        "key": [
            "MAKE-SET, UNION and FIND-SET",
            "lists: append the shorter one",
            "a set is a tree; its root names it",
            "union by rank: lower rank goes under",
            "path compression: the path points home",
            "both: O(m α(n)), and α(n) ≤ 4 in use",
        ],
        "key_label": "Chapter 21 in six lines",
        "concepts_intro": (
            "Three ideas: the name a set answers to, and the two rules that keep the trees "
            "holding those names flat."
        ),
        "concepts": [
            ("Representative",
             "The member that names a set. FIND-SET returns it, and two elements are in the same "
             "set exactly when their finds return the same representative, provided no union "
             "intervenes. In a list it is the head; in a forest it is the root."),
            ("Union by rank",
             "Each node carries a rank, an upper bound on its height. A union links the root of "
             "smaller rank under the root of larger rank and leaves both ranks alone; when the "
             "ranks are equal it chooses one to be the parent and raises that one's rank by 1."),
            ("Path compression",
             "During FIND-SET, after the root is found, every node on the path walked is made to "
             "point directly at the root. Ranks are not changed, so afterwards a rank may "
             "overstate a node's height."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 21.1 to 21.3 in your own copy, and the definitions at the start of "
            "the starred Section 21.4. The lesson sets out the argument in its own words, runs a "
            "short sequence by hand, and then counts the pointers every find walks in the lab."
        ),
        "body": [
            ("p", "&ldquo;The second heuristic, path compression, is also quite simple and highly "
                  "effective.&rdquo; Simplicity is the theme of Chapter 21, and the authors keep "
                  "pointing out the contrast between how little the code does and how much work it "
                  "takes to prove what it achieves. This lesson reads the chapter: the three "
                  "operations, two representations, the two heuristics, and the function α(n) that "
                  "the final bound is stated in."),
            ("p", "Section 21.1 fixes the interface. MAKE-SET(x) creates a set whose only member, "
                  "and so its representative, is x; UNION(x, y) replaces the sets holding x and y "
                  "by their union; FIND-SET(x) returns the representative of x's set. The analysis "
                  "uses two numbers, n, the MAKE-SET operations, and m, all operations together, so "
                  "`m ≥ n`, and since each union removes a set there are at most `n − 1` unions. "
                  "The section's application is connected components: make a set for each vertex, "
                  "unite the ends of every edge, and two vertices are in the same component exactly "
                  "when their finds agree, which pays off when edges arrive one at a time."),
            ("p", "Section 21.2 keeps each set as a linked list whose objects point back to a set "
                  "object holding the head and the tail; the head is the representative. MAKE-SET "
                  "and FIND-SET take constant time. UNION appends one list to the other, and every "
                  "object of the appended list must have its back-pointer changed, so a union costs "
                  "time proportional to the list appended. Unite n singletons by always appending "
                  "the growing list onto a new singleton and the i-th union updates i objects: "
                  "`Θ(n²)` over `2n − 1` operations, `Θ(n)` each on average. The weighted-union "
                  "heuristic keeps each list's length and always appends the shorter."),
            ("thm", ("Theorem 21.1",
                     "With linked lists and weighted union, any m "
                     "operations, n of them MAKE-SET, take `O(m + n lg n)` time. An object's "
                     "back-pointer changes only when its list is the shorter, so each change at "
                     "least doubles the size of the set it belongs to; after `⌈lg k⌉` changes the "
                     "set has at least k members, and no set exceeds n, so no object's pointer "
                     "changes more than `⌈lg n⌉` times.")),
            ("p", "Section 21.3 keeps each set as a rooted tree in which every node points only to "
                  "its parent and the root, its own parent, is the representative. MAKE-SET makes a "
                  "one-node tree, FIND-SET follows parent pointers up the find path, and UNION makes "
                  "one root point to the other. Done naively this is no better than the lists: "
                  "`n − 1` unions can build a single path of n nodes, and finds at its foot walk "
                  "nearly n pointers. Two heuristics repair it."),
            ("def", ("The two heuristics in the procedures",
                     "UNION(x, y) calls LINK on the roots FIND-SET(x) and FIND-SET(y). LINK makes "
                     "the root of smaller rank a child of the other; with equal ranks it makes the "
                     "first a child of the second and adds 1 to the second's rank. FIND-SET is "
                     "two passes: it climbs to the root, and on the way back down it sets each "
                     "node's parent to the root it found.")),
            ("p", "Section 21.3 then states the bounds without proving them all. Union by rank "
                  "alone gives `O(m lg n)`, and that is tight (Exercises 21.4-4 and 21.3-3). Path "
                  "compression alone, with f finds, gives `Θ(n + f·(1 + log_(2 + f/n) n))`, stated "
                  "without proof. Together they give `O(m α(n))`, which is superlinear, strictly "
                  "speaking, but linear for every n any application could meet. Exercise 21.4-2 "
                  "asks you to show that no rank exceeds `⌊lg n⌋`. Behind it is the fact that a root "
                  "of rank r has at least `2ʳ` nodes in its tree, and on every run the lab sets the "
                  "tallest root's `2ʳ` beside the size of the largest set, where that fact says it "
                  "must fit."),
            ("p", "Section 21.4, starred, makes α precise. It defines a family of functions "
                  "`A_k(j)`: `A_0(j) = j + 1`, and each higher level applies the one below it "
                  "`j + 1` times, starting from j. Then `A_1(j) = 2j + 1` and "
                  "`A_2(j) = 2^(j+1)·(j + 1) − 1`, and at `j = 1` the levels give 2, 3, 7, 2047, and "
                  "for `A_4(1)` a number beyond `2^2048`, far more than `10^80`, the authors' estimate "
                  "of the atoms in the observable universe. The inverse `α(n)` is the least level k "
                  "with `A_k(1) ≥ n`: it is 3 from `n = 8` to `n = 2047` and 4 from 2048 all the way up to "
                  "`A_4(1)`. The section then proves `O(m α(n))` with a potential function built "
                  "on ranks; that proof is left to the book."),
            ("math", [
                "chain of 12 elements: 11 unions, then 12 finds",
                "",
                "union by rank   compression   pointer hops   worst find",
                "off             off               66             11",
                "on              off               20              1",
                "off             on                21             11",
                "on              on                20              1",
            ]),
            ("p", "Now the lab, the forest lab of the Algorithms Subject's lesson Union–Find, where "
                  "the rank argument is practised further. Its elements are 0 to `n − 1`, with n set "
                  "by a slider from 4 to 16. Three union patterns are built in, each followed by one "
                  "find of every element, and two switches turn union by rank and path compression "
                  "on and off; UNION links the first root under the second exactly as LINK does. The "
                  "tiles count the operations (the unions and finds; the n MAKE-SETs that the book's m "
                  "includes are not counted), the pointer hops walked by every find (including the "
                  "two inside each union), the worst single find, the tallest root's rank (with the "
                  "rank rule off, the depth the unions built, which compression may since have "
                  "flattened: on <code>chain</code> with compression alone it still reads 11), `2ʳ` against the elements present, and the hops the "
                  "two rules together save against neither. The table runs all four combinations."),
            ("p", "The worked example <code>chain</code> unites each element with the next, 0 with "
                  "1, 1 with 2, and so on, with both rules off. At 12 elements that builds a single "
                  "path: 23 operations, 66 hops, a worst find of 11, a depth of 11 whose `2¹¹ = 2048` "
                  "is far more than the 12 elements present, since without the rank rule nothing "
                  "makes the bound true; the two rules save 46 of the 66 hops. The table above is "
                  "this preset's: either rule alone already cuts the hops to about 20, compression "
                  "alone only after its first find has walked all 11."),
            ("p", "<code>pairs</code> unites neighbours, then pairs of pairs, then larger blocks, "
                  "with union by rank on: 35 hops, a worst find of 3, a tallest rank of 3, and "
                  "`2³ = 8 ≤ 12`, as the rank argument requires. Across the four combinations the "
                  "hops are 39, 35, 32 and 30; on this pattern neither rule helps much, because the "
                  "trees are never tall. Slide n to 16 and the tallest rank is 4 with "
                  "`2⁴ = 16 ≤ 16`, the bound met exactly. <code>star</code> unites everything "
                  "directly into element 0, with compression on: every tree has depth 1, every "
                  "combination walks 11 hops, and the rules save nothing, because there was nothing "
                  "to save."),
            ("h3", "Exercise"),
            ("p", "Take eight elements 1 to 8 and use union by rank and path compression, LINK "
                  "making the second root the parent when ranks are equal. Run UNION(1, 2), "
                  "UNION(3, 4), UNION(1, 3), UNION(5, 6), UNION(7, 8), UNION(5, 7), UNION(2, 8), "
                  "then FIND-SET(1). Draw the forest after each union with every rank, and say which "
                  "root holds the final set, its rank, how many pointers FIND-SET(1) follows, and "
                  "where 1 and 2 point afterwards."),
            ("p", "That closes Part V. The next course, Graph Algorithms, opens Part VI with Graph "
                  "Representations and Breadth-First Search; its minimum-spanning-tree lesson uses "
                  "this chapter's forest to tell whether an edge joins two trees, and its "
                  "shortest-path lessons come back to the heaps of Chapter 19."),
        ],
        "lab": ("seqkit", {
            "mode": "unionfind",
            "preset": "chain",
            "panel_title": "Switch the two heuristics on and off, and count every hop",
            "panel_intro": (
                "Choose a union pattern and the number of elements, then turn union by rank and "
                "path compression on or off. The forest is drawn, the pointer hops of every find "
                "are counted and plotted, and the table runs all four combinations on the same "
                "sequence, with the rank bound checked for each. The counts are this sequence's; "
                "the chapter's bounds hold for every sequence."
            ),
        }),
        "steps_title": "Running unions and finds by hand",
        "steps_intro": "Four steps on paper, then one on a sequence of your own.",
        "steps": [
            ("Start with singletons",
             "Draw every element as its own root, pointing at itself, with rank 0."),
            ("Find both roots, then link",
             "For UNION(x, y) walk from x and from y to their roots, counting the pointers. Hang "
             "the root of smaller rank under the other; with equal ranks hang the first under the "
             "second and add 1 to the second's rank."),
            ("Compress on the way back",
             "After any find, redraw every node on the path you walked as a child of the root. "
             "Leave every rank as it was."),
            ("Check the rank bound",
             "For each root of rank r count the nodes in its tree; there must be at least `2ʳ`. "
             "With compression on, check that a rank may now exceed the height it bounds."),
            ("Do it on a sequence of your own",
             "Set the lab to the chain pattern at 8 elements, predict by hand the hops for each of "
             "the four combinations of rules, then read the table and compare."),
        ],
        "worked": {
            "title": "A chain of six elements, with and without rank",
            "intro": [
                "Elements 0 to 5, unions (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), then a find of "
                "each element, as in the lab's <code>chain</code> pattern at `n = 6`.",
            ],
            "lines": [
                "no rules: each union hangs a root",
                "   under the next; unions walk 0",
                "   a path 0 → 1 → … → 5, depth 5",
                "   finds walk 5 + 4 + 3 + 2 + 1 + 0 = 15",
                "union by rank: 0 under 1, rank 1",
                "   2, 3, 4, 5 each go under 1",
                "   unions 3 to 5 walk 1 each: 3",
                "   finds walk 1 each, 5 in all",
                "   total 3 + 5 = 8; depth 1",
            ],
            "after": [
                "With union by rank, the second union finds root 1 of rank 1 and root 2 of rank 0, "
                "so 2 goes under 1 rather than 1 under 2, and from then on every element joins the "
                "same root directly. Set the lab to <code>chain</code> at 6 elements: its table "
                "reads 15 hops with neither rule and 8 with union by rank.",
            ],
        },
        "quiz_title": "Lists, ranks and α",
        "quiz": [
            {"q": "Run the exercise: UNION(1, 2), UNION(3, 4), UNION(1, 3), UNION(5, 6), UNION(7, 8), "
                  "UNION(5, 7), UNION(2, 8), then FIND-SET(1), with union by rank and path "
                  "compression and equal ranks making the second root the parent. Which statement "
                  "is right?",
             "a": ["The root is 8, of rank 3; FIND-SET(1) follows 3 pointers, and afterwards 1 and "
                   "2 point to 8",
                   "The root is 4, of rank 2; FIND-SET(1) follows 2 pointers, and afterwards 1 "
                   "points to 4",
                   "The root is 8, of rank 3; FIND-SET(1) follows 3 pointers, and afterwards only "
                   "1 points to 8",
                   "The root is 8, of rank 4; FIND-SET(1) follows 4 pointers, and afterwards 1, 2 "
                   "and 4 point to 8"],
             "c": 0,
             "why": "The first two unions give roots 2 and 4 of rank 1, and UNION(1, 3) links 2 "
                    "under 4, rank 2. Likewise 6 under 8 makes 8 rank 2. UNION(2, 8) links two "
                    "rank-2 roots, 4 under 8, and 8 becomes rank 3. FIND-SET(1) walks 1 → 2 → 4 "
                    "→ 8, three pointers, and compression points both 1 and 2 at 8 (4 already "
                    "does). Root 4 forgets the last union; only 1 moving forgets that compression "
                    "redirects every node on the path; rank 4 would need 16 elements."},
            {"q": "With linked lists and the weighted-union heuristic on 1,024 objects, at most how "
                  "many times can one object's back-pointer be changed?",
             "a": ["1,023", "512", "10", "32"],
             "c": 2,
             "why": "Each change at least doubles the size of the object's set, so after j changes "
                    "the set holds at least `2ʲ` objects, and no set exceeds `1024 = 2¹⁰`: at most "
                    "`lg 1024 = 10` changes, and ten are reached when sets of equal size are united "
                    "again and again. One thousand and twenty-three is the number of unions, all of "
                    "which could move some object, but not the same one each time; 512 halves n "
                    "instead of taking its logarithm; 32 is the square root of 1,024."},
            {"q": "Using `A_3(1) = 2047` and `A_4(1) > 10^80`, what is `α(n)` for `n = 10⁶`?",
             "a": ["3", "4", "6", "20"],
             "c": 1,
             "why": "`α(n)` is the least k with `A_k(1) ≥ n`. `A_3(1) = 2047` is below a million, "
                    "so k = 3 is not enough, and `A_4(1)` is far above it, so `α(10⁶) = 4`. Three "
                    "holds only up to 2,047. Twenty is about `lg 10⁶`, the find cost of union by "
                    "rank alone in the worst case; six has no source here."},
            {"q": "Which statement about ranks is true when path compression is used together "
                  "with union by rank?",
             "a": ["A node's rank is an upper bound on its height, and compression never changes "
                   "a rank",
                   "A node's rank always equals its height",
                   "Compression lowers the rank of every node it moves",
                   "A node's rank is the number of nodes in its subtree"],
             "c": 0,
             "why": "LINK sets ranks and FIND-SET leaves them alone, so when compression shortens "
                    "a tree, ranks overstate heights; that is why the chapter defines rank as an "
                    "upper bound rather than the height. Without compression rank and height "
                    "coincide under union by rank, but not with it. A root of rank r has at least "
                    "`2ʳ` nodes, so a rank is about the logarithm of a tree's size, never the size "
                    "itself."},
        ],
        "mistakes": [
            ("Reading O(m α(n)) as a constant-time find",
             "The bound is on the whole sequence of m operations, so it is an amortized "
             "statement. A single find can still be slow: with union by rank alone it can walk "
             "`⌊lg n⌋` pointers, and on <code>pairs</code> at 12 elements with union by rank "
             "on, as the preset starts, the worst find walks 3. What the bound says is that such finds are rare enough, "
             "and compression repairs enough of what they walk, that the total stays within "
             "`O(m α(n))`."),
            ("Taking rank for the height of the tree",
             "Under union by rank alone they coincide; with path compression they part, because "
             "compression flattens paths and never lowers a rank. The chapter calls rank an upper "
             "bound on height for exactly this reason, and the rank argument, `2ʳ` nodes under a "
             "root of rank r, is a statement about ranks, which LINK alone sets."),
            ("Linking without looking at the trees",
             "A union that always hangs the first root under the second can build a single path: "
             "the lab's <code>chain</code> at 12 elements walks 66 pointers with neither rule and "
             "20 with union by rank, whose depth is 1. The rank rule refuses to hang a taller tree "
             "under a shorter one, and that refusal alone is what gives every root of rank r at "
             "least `2ʳ` nodes."),
        ],
        "standard": (
            "Finish when you can run unions and finds under both heuristics by hand.",
            "Given six to eight elements and a sequence of unions and finds, produce the forest "
            "with every rank after each operation, count the pointers each find follows, and "
            "check the rank bound at every root."
        ),
        "note": (
            "The lab offers three fixed union patterns, each followed by one find of every "
            "element, at 4 to 16 elements, so the exercise's own sequence is done by hand; it "
            "has no linked-list representation, so Section 21.2 is set out in prose. It counts "
            "pointer hops, which is what a find's cost is made of. The bound O(m α(n)) is "
            "Section 21.4's, for every sequence."
        ),
    },
]
