"""Data Structures, the last seven lessons - search trees, balance, union-find.

Same discipline as part_a: every figure was read off the lab at the preset the
lesson opens on. Two numbers in these seven dicts are not counts and both say so
on the page: `2 ln n`, the asymptotic mean depth of a random search tree, and the
near-constant bound for union-find with both rules, which is stated and not
proved anywhere in this library.
"""

LESSONS = [
    # ---------------------------------------------------------------- 08
    {
        "slug": "binary-search-trees",
        "title": "Binary Search Trees",
        "module": "Search trees",
        "one_line": "Search, insert and delete including a two-child node, and tell the global invariant apart from the local check that passes on a tree that is not a search tree.",
        "summary": (
            "The search-tree invariant is not a rule about a node and its two children; "
            "it is a rule about whole subtrees, and a tree can satisfy the local version "
            "and violate the real one. The lab draws that tree. Deleting a node with two "
            "children is the one operation with a case to remember: replace it by its "
            "in-order successor, which has at most one child."
        ),
        "key": [
            "invariant     every key in the LEFT subtree  <  node  <  every key in the RIGHT subtree",
            "              at every node, about whole subtrees, not about the children",
            "",
            "search, insert     one root-to-leaf path        comparisons ≤ height + 1",
            "delete, 0 or 1 child     unlink",
            "delete, 2 children       replace by the in-order successor, then delete that",
            "",
            "in-order walk is sorted  ⟺  the tree is a search tree",
        ],
        "key_label": "The invariant, the three deletions, and the test that actually detects it",
        "concepts_intro": (
            "The definition, the one delicate operation, and the check people substitute "
            "for the definition without noticing that it is weaker."
        ),
        "concepts": [
            ("The invariant is about subtrees, and it is what makes search a path",
             "At every node, every key in the left subtree is smaller and every key in "
             "the right subtree is larger. That is what lets a search discard half the "
             "remaining tree at each step on the strength of one comparison: if the "
             "target is smaller than this node it cannot be anywhere to the right, "
             "because <em>nothing</em> to the right is smaller. A local rule about two "
             "children would not license that."),
            ("The local check is strictly weaker, and the lab has the counterexample",
             "Checking only that each node is larger than its left child and smaller than "
             "its right child passes on the tree with root `20`, left child `10`, and "
             "`25` hanging as the right child of `10`. Every parent-child pair is in "
             "order. But `25` is in `20`&rsquo;s left subtree and `25 > 20`, so a search "
             "for `25` turns left at the root and never finds it."),
            ("Deleting a two-child node is a substitution, not a rearrangement",
             "A node with no children or one child is unlinked. A node with two children "
             "cannot be: both subtrees have to stay attached to something in the right "
             "order. The key that can take its place is its in-order successor &mdash; "
             "the smallest key in its right subtree &mdash; and that node has no left "
             "child by construction, so removing it is the easy case."),
        ],
        "read_title": "The invariant, the walk that tests it, and the three deletions",
        "read_intro": "Why search is one path, what the local check misses, and the successor substitution done by hand.",
        "body": [
            ("def", ("Binary search tree",
                     "A binary tree in which, at every node `x`, every key in the left "
                     "subtree of `x` is less than the key at `x`, and every key in the "
                     "right subtree of `x` is greater than it. Duplicate keys are "
                     "excluded here.",
                     "The condition is quantified over subtrees, not over children. That "
                     "is the whole of the definition and the source of the only "
                     "misconception in this lesson.")),
            ("p", "Search follows one path. Compare the target with the root: equal and "
                  "you are done; smaller and the target can only be in the left subtree, "
                  "because every key to the right is larger; larger and only in the "
                  "right. Repeat. The number of comparisons is one per level visited, so "
                  "at most the height plus one. Insertion is the same walk, ending at the "
                  "empty position where the search failed."),
            ("thm", ("The in-order walk of a search tree is sorted",
                     "Traverse left subtree, then node, then right subtree, recursively. "
                     "The sequence of keys produced is in increasing order if and only if "
                     "the tree is a binary search tree.",
                     "One direction is the invariant unrolled: everything in the left "
                     "subtree is smaller than the node and is emitted before it, and "
                     "everything in the right subtree is larger and is emitted after. The "
                     "other direction is why this is useful as a test &mdash; a walk that "
                     "comes out sorted certifies the invariant everywhere, including the "
                     "subtree conditions the local check never looks at.")),
            ("example", ("The tree that passes the local check",
                         "Root `20`, left child `10`, right child `30`, and `25` as the "
                         "right child of `10`. Local check: `10 < 20`, `30 > 20`, "
                         "`25 > 10`. All pass. In-order walk: `10, 25, 20, 30` &mdash; "
                         "not sorted, and the walk names the offender. The lab builds "
                         "this tree and evaluates both checks on it in your browser, "
                         "reporting the local one as satisfied and the real one as "
                         "violated.")),
            ("h3", "Deleting a node, in three cases"),
            ("p", "No children: unlink it. One child: splice the child into its place, "
                  "which preserves the invariant because the whole subtree moves up "
                  "unchanged and its keys were already on the correct side of everything "
                  "above. Two children: neither child can simply take the node&rsquo;s "
                  "place, because the other subtree would have nowhere correct to go."),
            ("p", "So replace the key rather than the node. The in-order successor is the "
                  "smallest key in the right subtree &mdash; walk right once, then left "
                  "as far as possible. Every key in the left subtree is smaller than it "
                  "(they were smaller than the node, which is smaller than everything "
                  "right), and every remaining key in the right subtree is larger than it "
                  "(it was the smallest). So it can sit where the deleted node was. And "
                  "it has no left child, or it would not have been the smallest, so "
                  "removing it from where it was is one of the two easy cases."),
            ("math", [
                "insert 50 30 70 20 40 60 80,  then delete 30",
                "",
                "                50                       50",
                "           30        70              40      70",
                "        20    40   60  80         20      60    80",
                "",
                "  30 has two children, 20 and 40",
                "  successor of 30 = smallest key right of it = 40,  which has no children",
                "  40 takes 30's place;  20 stays where it was",
                "",
                "  in-order before   20 30 40 50 60 70 80",
                "  in-order after    20    40 50 60 70 80        one key gone, still sorted",
            ]),
            ("p", "The lab counts `13` comparisons for those eight operations and reports "
                  "the resulting height as `2`. Deleting the root instead of `30` is the "
                  "same rule with a longer reach: the successor of `50` is `60`, which "
                  "lives in the other subtree, and `60` becomes the root while `70` keeps "
                  "`80` as its right child. The tree is different and the in-order "
                  "sequence is still sorted, which is the only thing the invariant asks."),
            ("h3", "What the counts do and do not say"),
            ("p", "Search for `40` in the seven-key tree before that deletion and the "
                  "lab reports the path `50 → 30 → 40`: three comparisons, and the panel "
                  "prints the route so the path is a thing you can see rather than infer. "
                  "Search for `55` and it reports three comparisons and not found. Run the "
                  "same eight operations with the keys arriving as `20, 30, 40, 50, 60, 70, "
                  "80` and the seven insertions build a path of height `6`, the whole "
                  "sequence costs `23` comparisons rather than `13`, and the delete leaves "
                  "a tree of height `5`."),
            ("p", "That last pair is the warning. The invariant says nothing about the "
                  "shape, so it says nothing about the cost: `13` comparisons and `23` "
                  "comparisons come from the same keys and the same algorithm, and the "
                  "only difference is the order they arrived in. A search tree is `O(log "
                  "n)` per operation exactly when it is short, and nothing established so "
                  "far makes it short. The next lesson is about what does."),
        ],
        "lab": ("tree", {
            "mode": "bst",
            "preset": "two-child-delete",
            "panel_title": "Insert, delete, and check the invariant both ways",
            "panel_intro": "Type keys to insert, `-k` to delete and `?k` to search. The tree "
                           "is drawn after each operation, the successor substitution is shown "
                           "when a two-child node is deleted, comparisons are counted, and the "
                           "in-order walk is printed beneath. The panel also evaluates both "
                           "the global invariant and the weaker local check on a tree built "
                           "to separate them.",
        }),
        "steps_title": "Operating a search tree",
        "steps_intro": "Four steps, and the fourth is the one that catches a broken tree that looks fine.",
        "steps": [
            ("Search by comparing once per level",
             "Smaller, go left; larger, go right; equal, stop. Write the path down. The "
             "comparison count is the path length, and a path longer than about `log₂ n` "
             "is telling you something about the shape rather than about the search."),
            ("Insert where the search failed",
             "Run the search for the new key. It ends at an empty child pointer, and that "
             "is the only place the key can go without breaking the invariant. There is no "
             "choice to make, which is exactly why the insertion order determines the "
             "shape."),
            ("Delete by case, and name the case",
             "Zero or one child: unlink or splice. Two children: find the in-order "
             "successor &mdash; right once, then left until you cannot &mdash; move its "
             "key up, and delete it from where it was. Saying which case you are in "
             "before acting is what keeps the two-child case from being attempted as a "
             "splice."),
            ("Check with the in-order walk, not node by node",
             "Emit left, node, right. If the sequence is sorted the invariant holds "
             "everywhere; if it is not, the first out-of-order pair names the offending "
             "key. Checking each node against its two children can pass on a tree that is "
             "not a search tree, and the lab has that tree."),
        ],
        "worked": {
            "title": "Seven keys in, one two-child node out",
            "intro": [
                "The lab&rsquo;s opening sequence with the comparison counter shown. The "
                "last line is the deletion the lesson is about."
            ],
            "lines": [
                "op          path of comparisons            cmp   tree height after",
                "",
                "insert 50   —                                0     0",
                "insert 30   50                               1     1",
                "insert 70   50                               1     1",
                "insert 20   50, 30                           2     2",
                "insert 40   50, 30                           2     2",
                "insert 60   50, 70                           2     2",
                "insert 80   50, 70                           2     2",
                "",
                "                        50",
                "                  30          70",
                "               20    40    60    80",
                "",
                "delete 30   50, 30  →  two children                  2",
                "            successor = smallest right of 30 = 40",
                "            40 has no children, so move 40 up and unlink it",
                "",
                "                        50",
                "                  40          70",
                "               20        60      80",
                "",
                "total comparisons 13,   in-order 20 40 50 60 70 80,   height 2",
            ],
            "after": [
                "The successor of `30` was `40`, one step to the right and then no left "
                "child to follow. That is the common case and it makes the operation look "
                "trivial. Delete `50` from the original tree instead and the successor is "
                "`60`, reached by going right to `70` and then left once &mdash; and `60` "
                "becomes the root of the whole tree while `70` keeps `80`. Same rule, "
                "longer walk.",
                "Count the comparisons and then count them again for the same seven keys "
                "arriving as `20, 30, 40, 50, 60, 70, 80`. The seven insertions build a "
                "single path of height `6`, the eight operations cost `23` rather than "
                "`13`, and every search is a scan. Nothing in the invariant was violated. "
                "The cost changed because the shape changed, and the shape was decided "
                "by the arrival order.",
                "For a faded rehearsal, build `50 30 70 20 40 60 80` and then delete `70`. "
                "The supplied first move is that `70` has two children, so the successor "
                "is the smallest key in the subtree rooted at `80` &mdash; which is `80` "
                "itself, since it has no left child. Carry out the substitution, write the "
                "in-order walk, and confirm it is still sorted. Then run the local check "
                "on the lab&rsquo;s counterexample tree and say, in one sentence, what the "
                "walk detects that the local check cannot.",
            ],
        },
        "quiz_title": "Invariant and deletion",
        "quiz": [
            {"q": "A tree has root `20`, left child `10`, right child `30`, and `25` as the right child of `10`. Is it a binary search tree?",
             "a": ["Yes: every node is larger than its left child and smaller than its right child",
                   "No: `25` is in the left subtree of `20` and `25 > 20`",
                   "Yes, provided `25` is a leaf",
                   "No: a node may not have a right child without a left child"],
             "c": 1,
             "why": "The invariant is about whole subtrees. `25` sits in `20`&rsquo;s left "
                    "subtree, so it must be less than `20`, and it is not &mdash; a search "
                    "for `25` turns left at the root and fails. The local parent-child "
                    "check does pass on this tree, which is exactly why it is not the "
                    "definition. Whether `25` is a leaf is irrelevant, and a right child "
                    "without a left one is perfectly ordinary."},
            {"q": "You delete a node with two children. Why is its in-order successor always safe to promote?",
             "a": ["Because it is the largest key in the left subtree",
                   "Because it is larger than everything left of the node and smaller than everything else right of it, and it has no left child",
                   "Because the tree is rebalanced afterwards",
                   "Because it is always a leaf"],
             "c": 1,
             "why": "The successor is the smallest key in the right subtree, so it exceeds "
                    "every key in the left subtree and is below every other key in the "
                    "right one: it fits where the deleted node was. And being the smallest "
                    "there, it has no left child, so removing it from its old position is "
                    "the zero- or one-child case. The in-order predecessor &mdash; the "
                    "largest key on the left &mdash; works symmetrically, but it is not "
                    "the successor. No rebalancing happens in a plain search tree, and the "
                    "successor may well have a right child."},
            {"q": "The same seven keys are inserted in two different orders. One tree has height `2` and costs `13` comparisons; the other has height `5` and costs `23`. What does that tell you about the invariant?",
             "a": ["One of the two trees violates it",
                   "It constrains the key positions but not the shape, so it does not bound the cost",
                   "It only holds for balanced trees",
                   "Comparisons are not a fair measure of cost here"],
             "c": 1,
             "why": "Both trees satisfy the invariant perfectly; both in-order walks come "
                    "out sorted. The invariant says where a key may sit relative to "
                    "others, and says nothing about how tall the tree gets &mdash; which "
                    "is decided by the insertion order. That gap is what the next lesson "
                    "is about, and it is why a search tree needs something extra before "
                    "`O(log n)` can be claimed."},
        ],
        "mistakes": [
            ("Checking the invariant node against its children only",
             "It passes on the tree with `25` under `10` under `20`, which is not a search "
             "tree and in which `25` cannot be found. The condition quantifies over "
             "subtrees, and the cheap way to test it properly is the in-order walk: if the "
             "keys come out sorted the invariant holds everywhere, and if they do not the "
             "first inversion names the problem."),
            ("Splicing one child up when deleting a two-child node",
             "Promoting the left child leaves the right subtree with nowhere to attach "
             "that keeps the ordering, and the usual improvisation &mdash; hanging it off "
             "the promoted child somewhere &mdash; breaks the invariant or reshapes half "
             "the tree. The successor substitution exists because it is the move that "
             "changes one key and nothing else."),
            ("Expecting the invariant to imply a logarithmic cost",
             "Insert seven keys in sorted order and you get a path of height `6`, "
             "satisfying every condition in the definition, in which search is a linear "
             "scan. The invariant is about correctness. The cost is about shape, the shape "
             "is decided by the order the keys arrived in, and nothing so far controls it."),
        ],
        "standard": ("Finish when you reach for the in-order walk rather than a node-by-node check.",
                     "You should be able to search, insert and delete by hand including the "
                     "two-child case with the successor named, produce the in-order walk of "
                     "a drawn tree, explain why the local check is weaker using the "
                     "four-node counterexample, and state plainly that the invariant bounds "
                     "nothing about the height."),
        "note": (
            "The same keys can build a tree of height `2` or a path of height `14`, and "
            "nothing in the definition prefers either. &ldquo;The Shape Problem and Random "
            "BSTs&rdquo; is about what does decide it: the insertion order, and only the "
            "insertion order &mdash; with a measured mean depth beside the `2 ln n` "
            "asymptote that is often mistaken for it."
        ),
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "the-shape-problem-and-random-bsts",
        "title": "The Shape Problem and Random BSTs",
        "module": "Search trees",
        "one_line": "Predict a tree’s height from its insertion order, and produce one order that degenerates a key set and one that balances it.",
        "summary": (
            "The cost of a search tree is fixed by the order the keys arrived in, not by "
            "the keys. Fifteen keys inserted in sorted order give a path of height `14`; "
            "the same fifteen in a shuffled order give height `6`, and middle-first gives "
            "`3`. A uniformly random order gives expected height `O(log n)` &mdash; "
            "stated here, and the recurrence behind it is the one Sorting and "
            "Selection solves for randomised quicksort."
        ),
        "key": [
            "the keys do not decide the shape;  the ORDER decides the shape",
            "",
            "n = 15, keys 10 20 … 150         height    mean depth   comparisons",
            "  sorted                              14            7           105",
            "  a seeded shuffle                     6        44/15            44",
            "  middle first, then each half         3        34/15            34",
            "",
            "2 ln n  =  5.416 at n = 15       an ASYMPTOTE, and not the height above",
        ],
        "key_label": "One key set, three orders, and the reference curve that is none of them",
        "concepts_intro": (
            "One idea and two things it is constantly confused with. The idea is that the "
            "order is the whole story; the confusions are between height and mean depth, "
            "and between either of them and an asymptotic formula."
        ),
        "concepts": [
            ("The insertion order determines the tree completely",
             "Insertion has no choices: the new key goes where the search for it failed. "
             "So the order fixes the tree, and the same key set can produce anything from "
             "a path of height `n − 1` to a tree of height `⌊log₂ n⌋`. &ldquo;These keys "
             "are badly distributed&rdquo; is almost never the problem; the keys arriving "
             "sorted is, and sorted input is the single commonest way real data arrives."),
            ("Height and mean depth are different quantities",
             "The height is the longest path, and it is what a worst-case search costs. "
             "The mean depth is the average over all nodes, and it is what a search for a "
             "uniformly chosen key costs. At `n = 15` the shuffled tree has height `6` and "
             "mean depth `44/15 ≈ 2.93` &mdash; the two differ by a factor of two, and a "
             "page that printed one number would be ambiguous about which claim it was "
             "making."),
            ("O(log n) expected is a statement about the order, not about the tree",
             "Insert `n` distinct keys in a uniformly random order and the expected height "
             "is `O(log n)`. The randomness is in the arrival order; the keys themselves "
             "can be anything. This is why the fix for the shape problem in the two "
             "randomised trees later on is to inject randomness deliberately rather than "
             "to hope the input has some."),
        ],
        "read_title": "Three orders, one key set, and three numbers that are not the same number",
        "read_intro": "Why sorted input is the worst case, what a shuffle actually buys, and how to read the asymptote printed beside the measurements.",
        "body": [
            ("p", "Insertion into a search tree is deterministic given the order. Each "
                  "new key walks from the root to the empty position where a search for "
                  "it would have failed, and there is exactly one such position. So the "
                  "tree is a function of the sequence, and asking &ldquo;how tall is the "
                  "tree for these keys&rdquo; is not a well-posed question."),
            ("example", ("Sorted input is the worst case, and it is not a rare one",
                         "Insert `10, 20, 30, …, 150`. Every key is larger than everything "
                         "present, so every key becomes the right child of the previous "
                         "one: a path of height `14` on fifteen keys. Reversed input does "
                         "the same thing leftwards. Sorted arrival is what you get from a "
                         "database dump ordered by primary key, a log replayed by "
                         "timestamp, or an identifier that increments &mdash; so the worst "
                         "case for this structure is also one of the most common inputs "
                         "in practice.")),
            ("math", [
                "n = 15,  keys 10 20 30 … 150,  three insertion orders",
                "",
                "order                        height   mean depth   comparisons to build",
                "",
                "sorted        10 20 … 150         14       105/15 = 7          105",
                "reversed     150 140 … 10         14       105/15 = 7          105",
                "shuffled  130 80 100 110 …         6        44/15 ≈ 2.93         44",
                "bisect     80 40 20 10 30 …        3        34/15 ≈ 2.27         34",
                "",
                "2 ln 15 = 5.416     asymptotic mean depth of a RANDOM tree",
            ]),
            ("p", "Read the last line carefully, because it is the one number on this "
                  "page that was not counted. `2 ln n` is the asymptotic expected depth of "
                  "a node in a tree built from a uniformly random order. At `n = 15` it "
                  "evaluates to `5.416`, and the lab draws it as a dashed reference curve "
                  "and labels its readout asymptotic. It is not the height of any of the "
                  "trees above &mdash; the shuffled tree&rsquo;s height is `6` and the "
                  "balanced tree&rsquo;s is `3` &mdash; and it is not the measured mean "
                  "depth either, which is `2.93` on the shuffle."),
            ("p", "So there are three numbers on screen and they are three different "
                  "quantities: the <strong>measured height</strong>, the longest path in "
                  "the tree drawn; the <strong>measured mean depth</strong>, an exact "
                  "fraction over the nodes of that tree; and the <strong>asymptote</strong>, "
                  "a formula about the limit of an average over orders. At `n = 15` the "
                  "asymptote is about `85%` above the measured mean depth, which is what "
                  "an asymptotic formula does at small `n`. Push the size up and the gap "
                  "narrows; it does not close from above or below in any tidy way, because "
                  "one shuffle is one sample."),
            ("thm", ("Expected height of a randomly built search tree",
                     "Insert `n` distinct keys in an order chosen uniformly at random from "
                     "all `n!` orders. The expected height of the resulting tree is "
                     "`O(log n)`, and the expected depth of a node is `2 ln n + O(1)`.",
                     "This is <strong>stated here and proved elsewhere</strong>. The "
                     "recurrence it comes from is the one produced by choosing a uniformly "
                     "random root and recursing on the two pieces &mdash; which is exactly "
                     "the recurrence &ldquo;Randomised Quicksort&rdquo; solves on the "
                     "Sorting and Selection course, because a random pivot and a random "
                     "root are the same object looked at twice. &ldquo;Treaps&rdquo;, on "
                     "the Randomised Algorithms course, closes the loop by building a tree "
                     "whose shape is random no matter what order the keys arrive in.")),
            ("h3", "What a shuffle buys, and what it does not"),
            ("p", "The shuffled order above gives height `6` where sorted gives `14`: a "
                  "factor of more than two, and `44` comparisons to build rather than "
                  "`105`. That is a real and large improvement, and it is one sample. Run "
                  "a different seed and the height moves. The theorem is about the average "
                  "over all orders, and no single shuffle establishes it &mdash; which is "
                  "the same caution as everywhere else on this course, sharpened by the "
                  "fact that here the quantity in question is itself an average."),
            ("p", "And a shuffle is not always available. It requires having all the keys "
                  "before inserting any of them, which defeats the point of an online "
                  "structure. If keys arrive one at a time from a sorted stream there is "
                  "nothing to shuffle, and the tree degenerates as it grows. That is the "
                  "gap the rest of this course closes: instead of hoping the order is "
                  "random, enforce a shape condition on every insertion, which is what "
                  "&ldquo;Rotations and the AVL Invariant&rdquo; begins."),
            ("p", "One last measurement worth having. The bisect order &mdash; middle "
                  "key first, then the middle of each half, recursively &mdash; gives "
                  "height `3` at `n = 15`, which is `⌊log₂ 15⌋`: the shortest a tree on "
                  "fifteen nodes can be. It costs `34` comparisons to build. It is also "
                  "useless as a strategy, for the same reason a shuffle often is: you have "
                  "to know all the keys and their order in advance, which is to say you "
                  "have to have sorted them already."),
        ],
        "lab": ("tree", {
            "mode": "orders",
            "preset": "sorted",
            "panel_title": "One key set, four orders, and three numbers kept apart",
            "panel_intro": "Choose the size and the insertion order &mdash; sorted, reversed, "
                           "a seeded shuffle, middle-first, or your own. The tree is drawn, and "
                           "the panel prints the measured height, the measured mean depth as "
                           "an exact fraction, and `2 ln n` as a dashed reference. The last of "
                           "those is an asymptote and is labelled as one: at `n = 15` it reads "
                           "`5.416` while the balanced tree&rsquo;s height is `3`.",
        }),
        "steps_title": "Predicting and controlling a shape",
        "steps_intro": "Predict before running. A prediction that turns out wrong is the only cheap way to find out which of the three numbers you were thinking of.",
        "steps": [
            ("Read the order, not the keys",
             "Ask what happens to each arriving key relative to the ones already there. "
             "Monotone in either direction gives a path of height `n − 1`. Alternating "
             "between extremes gives a path too. The keys&rsquo; values matter only "
             "through their relative order."),
            ("Predict the height, then the mean depth, separately",
             "The height is the longest path; the mean depth is the average over nodes. "
             "Write both predictions down. Getting the height right and the mean depth "
             "wrong is the normal outcome the first few times, and it is the thing worth "
             "finding out."),
            ("Construct a degenerate order and a balanced one",
             "Sorted for the first. Middle-first, recursively, for the second &mdash; and "
             "notice while doing it that you needed the sorted key list to build it, which "
             "is why it is a diagnostic rather than a strategy."),
            ("Compare the measurements with the asymptote as three separate quantities",
             "Measured height, measured mean depth, `2 ln n`. Say aloud which is which "
             "before drawing any conclusion. The asymptote is about an average over "
             "orders in the limit, and at `n = 15` it sits well above the measured mean "
             "depth of a shuffled tree."),
        ],
        "worked": {
            "title": "Fifteen keys, three orders, by hand",
            "intro": [
                "The first few insertions of each order, far enough to see the shape being "
                "decided, with the finished measurements underneath."
            ],
            "lines": [
                "sorted:  10 20 30 40 …",
                "  10                  10                 10",
                "                        \\                  \\",
                "                         20                 20",
                "                                              \\",
                "                                               30      … a path",
                "  height 14,  mean depth 7,  105 comparisons to build",
                "",
                "bisect:  80 40 20 10 30 60 50 70 120 100 90 110 140 130 150",
                "  its top three levels:",
                "                     80",
                "               40         120",
                "            20    60   100   140",
                "  height 3,  mean depth 34/15,  34 comparisons to build",
                "",
                "seeded shuffle:  130 80 100 110 60 140 10 30 150 20 50 40 70 120 90",
                "  height 6,  mean depth 44/15,  44 comparisons to build",
                "",
                "2 ln 15 = 5.416      not the height (6), not the mean depth (2.93)",
            ],
            "after": [
                "Every insertion in the sorted case goes to the right of everything, "
                "because it is larger than everything, and there is no decision to make "
                "anywhere. That is the whole of the degeneracy: the structure is doing "
                "exactly what it is defined to do and the order is doing all the damage.",
                "The shuffle&rsquo;s height is `6` against the balanced `3` and the "
                "degenerate `14`. Its mean depth, `44/15`, is much closer to the balanced "
                "tree&rsquo;s `34/15` than to the path&rsquo;s `7` &mdash; which is the "
                "useful way to summarise what randomness buys: it makes the typical search "
                "nearly optimal while leaving the worst search a constant factor worse.",
                "For a faded rehearsal, run `n = 31` with each order. The supplied "
                "observation is that sorted must give height `30` and mean depth `15`, by "
                "the same argument as above. Predict the shuffle&rsquo;s height before "
                "looking &mdash; the lab reports `9`, with mean depth `139/31 ≈ 4.48` "
                "against `2 ln 31 = 6.868` &mdash; and then say which of the three numbers "
                "on your screen would change if you changed nothing but the seed.",
            ],
        },
        "quiz_title": "Order, shape and asymptote",
        "quiz": [
            {"q": "Fifteen distinct keys are inserted into a search tree in increasing order. What is the height?",
             "a": ["`3`", "`4`", "`14`", "It depends on the keys"],
             "c": 2,
             "why": "Each key is larger than everything already present, so it becomes the "
                    "right child of the previous one and the tree is a path of `15` nodes, "
                    "height `14`. `3` is `⌊log₂ 15⌋`, the best possible, which the "
                    "middle-first order achieves. The actual key values are irrelevant: "
                    "only their relative order matters, and it is increasing."},
            {"q": "The lab shows a shuffled tree at `n = 15` with height `6`, mean depth `44/15`, and `2 ln 15 = 5.416`. Which of the three is a measurement of that tree?",
             "a": ["only the height", "the height and the mean depth",
                   "only `2 ln 15`", "all three"],
             "c": 1,
             "why": "The height is the longest path in the tree drawn and the mean depth is "
                    "the average over its nodes as an exact fraction &mdash; both counted. "
                    "`2 ln n` is an asymptotic formula for the expected depth in a "
                    "randomly built tree; it is a model, it is about an average over all "
                    "orders in the limit, and at `n = 15` it is about `85%` above the "
                    "measured mean depth."},
            {"q": "Why is shuffling the keys before inserting them not a general fix for the shape problem?",
             "a": ["Because a shuffle can produce sorted order",
                   "Because it requires holding all the keys before inserting any, which an online structure cannot do",
                   "Because the expected height of a random tree is still `Θ(n)`",
                   "Because shuffling changes the in-order sequence"],
             "c": 1,
             "why": "A shuffle needs the whole key set in advance, and a search tree is "
                    "usually wanted precisely because keys arrive over time. A shuffle can "
                    "in principle return sorted order, but with probability `1/n!` &mdash; "
                    "that is not the objection. The expected height of a randomly built "
                    "tree is `O(log n)`, not `Θ(n)`. And a shuffle changes the insertion "
                    "order, never the in-order sequence, which is always sorted."},
        ],
        "mistakes": [
            ("Blaming the keys for the shape",
             "&ldquo;These keys are clustered&rdquo; almost never explains a degenerate "
             "tree. The same fifteen keys give height `14`, `6` or `3` depending only on "
             "the order they arrived in. The diagnostic question is not what the keys look "
             "like; it is whether they arrived sorted &mdash; which they very often did, "
             "because that is how dumps, logs and autoincrementing identifiers come."),
            ("Reading `2 ln n` as the height",
             "It is an asymptotic formula for the expected depth of a node in a randomly "
             "built tree, which is a third quantity distinct from both the height and the "
             "measured mean depth. At `n = 15` it reads `5.416` while the balanced "
             "tree&rsquo;s height is `3` and a shuffled tree&rsquo;s mean depth is `2.93`. "
             "The lab prints all three side by side and labels which one is asymptotic, "
             "and the reason it does is that reading them as one number is the standard "
             "failure of this lesson."),
            ("Taking one shuffle as evidence for the expected-height theorem",
             "A single seeded shuffle gives height `6` at `n = 15`. A different seed gives "
             "something else. The theorem is about the average over all `n!` orders, and "
             "the proof of it is not on this course &mdash; it is the recurrence "
             "&ldquo;Randomised Quicksort&rdquo; solves. Sampling an average is not "
             "computing it, and the lab is showing you one order at a time."),
        ],
        "standard": ("Finish when the question “how tall is the tree for these keys” sounds ill-posed.",
                     "You should be able to predict the height and the mean depth of a tree "
                     "from a stated insertion order, construct an order that degenerates a "
                     "key set and one that balances it, and say of each number on the "
                     "lab&rsquo;s panel whether it was counted from the tree drawn or "
                     "evaluated from an asymptotic formula."),
        "note": (
            "If the order cannot be trusted, the structure has to fix its own shape. "
            "&ldquo;Rotations and the AVL Invariant&rdquo; introduces the one local rewrite "
            "that changes heights without changing the in-order sequence, and the balance "
            "condition that turns it into a height bound &mdash; by way of a recurrence "
            "whose solution is the Fibonacci numbers."
        ),
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "rotations-and-the-avl-invariant",
        "title": "Rotations and the AVL Invariant",
        "module": "Search trees",
        "one_line": "Rotate at a chosen node and verify the in-order sequence is unchanged, then tabulate `N(h)` and bound the height at a given `n`.",
        "summary": (
            "A rotation is a local rewrite that moves pointers and leaves every key in "
            "its in-order position, so it preserves the search-tree invariant "
            "automatically. Requiring `|h_L − h_R| ≤ 1` at every node then forces a "
            "logarithmic height, because the smallest AVL tree of height `h` has "
            "`N(h) = N(h−1) + N(h−2) + 1` nodes &mdash; Fibonacci growth, tabulated "
            "exactly rather than quoted as `1.44 log₂ n`."
        ),
        "key": [
            "rotate right at x:   x's left child y rises;  y's right subtree becomes x's left",
            "in-order sequence unchanged  ⟹  the search-tree invariant survives, always",
            "",
            "AVL invariant    |h_L − h_R| ≤ 1   at every node",
            "N(h) = N(h−1) + N(h−2) + 1        the fewest nodes in a tree of height h",
            "N: 1  2  4  7  12  20  33  54  88  143  232        Fibonacci, minus one",
            "",
            "6 nodes ⟹ h ≤ 2,   1000 nodes ⟹ h ≤ 13       and 1.44 log₂ 1000 = 14.35",
        ],
        "key_label": "One rewrite, one condition, and the table that is the height bound",
        "concepts_intro": (
            "Two mechanical facts and one counting argument. The counting argument is the "
            "only place a new technique appears, and it is the same recurrence Fibonacci "
            "satisfies with a `+1` bolted on."
        ),
        "concepts": [
            ("A rotation moves pointers and no keys",
             "Rotating right at `x` lifts `x`&rsquo;s left child `y` into `x`&rsquo;s "
             "place, hangs `x` as `y`&rsquo;s right child, and re-parents `y`&rsquo;s old "
             "right subtree as `x`&rsquo;s new left subtree. Read the in-order sequence "
             "before and after: identical. No key changes its position in the sorted "
             "order, which is why the invariant cannot break and why every balanced tree "
             "in existence is allowed to use one."),
            ("The AVL condition is local and its consequence is global",
             "`|h_L − h_R| ≤ 1` is checked at a single node using two numbers stored "
             "there. Requiring it everywhere bounds the height of the whole tree, and the "
             "bound is proved by asking the opposite question: what is the <em>fewest</em> "
             "nodes a tree of height `h` can have while satisfying it? That count grows "
             "exponentially, so the height grows logarithmically."),
            ("N(h) is a recurrence, and its table is the bound",
             "A tree of height `h` satisfying the condition has one subtree of height "
             "`h−1` and the other of height at least `h−2`, plus the root: "
             "`N(h) = N(h−1) + N(h−2) + 1`. That gives `1, 2, 4, 7, 12, 20, 33, 54, 88`. "
             "To bound the height of a tree on `n` nodes, find the largest `h` with "
             "`N(h) ≤ n` &mdash; an exact integer comparison, which is what the lab does "
             "instead of evaluating `1.44 log₂ n`."),
        ],
        "read_title": "The rewrite, the condition, and the Fibonacci count that bounds the height",
        "read_intro": "What a rotation does and does not change, where the recurrence comes from, and the table evaluated exactly beside the closed form.",
        "body": [
            ("def", ("Rotation",
                     "A <strong>right rotation</strong> at a node `x` with left child `y`: "
                     "`y` takes `x`&rsquo;s place, `x` becomes the right child of `y`, and "
                     "`y`&rsquo;s former right subtree becomes `x`&rsquo;s left subtree. A "
                     "<strong>left rotation</strong> is the mirror image. Both are a fixed "
                     "number of pointer writes.",
                     "A rotation requires the child it lifts to exist: there is no right "
                     "rotation at a node with no left child, and the lab reports that as "
                     "&ldquo;not possible&rdquo; rather than silently returning the tree "
                     "unchanged &mdash; because a panel that could not tell those apart "
                     "would show &ldquo;in-order unchanged&rdquo; as a success.")),
            ("thm", ("A rotation preserves the in-order sequence",
                     "Let `x` have left child `y`, with subtrees `A` and `B` under `y` and "
                     "`C` under `x`. In-order before: `A, y, B, x, C`. After a right "
                     "rotation at `x`, `y` is the root with `A` on its left and `x` on its "
                     "right, and `x` has `B` on its left and `C` on its right. In-order "
                     "after: `A, y, B, x, C`.",
                     "The two sequences are the same symbol by symbol, so no key has "
                     "changed its position in the sorted order and the search-tree "
                     "invariant holds after if it held before. The heights do change, by "
                     "at most one at each of the two nodes, and that is the entire point "
                     "of performing one.")),
            ("math", [
                "rotate right at 50                         keys 50 30 70 20 40 10",
                "",
                "         50                                       30",
                "     30      70                              20        50",
                "  20    40                                 10       40    70",
                "10",
                "",
                "in-order   10 20 30 40 50 70              in-order   10 20 30 40 50 70",
                "height 3                                  height 2",
            ]),
            ("p", "The lab draws both trees with the balance factor written above each "
                  "node, and prints the two in-order sequences to be compared "
                  "character by character. It also reports whether the rotation was "
                  "possible at all. Try one at a node whose relevant child is missing and "
                  "the panel says so, which matters because &ldquo;nothing changed&rdquo; "
                  "and &ldquo;the sequence was preserved&rdquo; look identical from the "
                  "outside."),
            ("p", "Not every rotation shortens the tree. Rotating left at `30` in the "
                  "tree built from `50 30 70 20 40 35 45` leaves the height at `3`: the "
                  "in-order sequence is preserved, the pointers moved, and the tree is no "
                  "shorter. A rotation is a tool, not a repair; knowing which rotation to "
                  "perform where is the next lesson."),
            ("h3", "The balance condition, and how tall a tree it allows"),
            ("def", ("AVL tree",
                     "A binary search tree in which, at every node, the heights of the two "
                     "subtrees differ by at most `1`. The difference `h_L − h_R` is the "
                     "node&rsquo;s <strong>balance factor</strong>, and it must be `−1`, "
                     "`0` or `1` everywhere.",
                     "The height of an empty subtree is taken as `−1` and of a leaf as "
                     "`0`. Every node stores its height, which is one extra integer and is "
                     "what makes the condition checkable in constant time.")),
            ("thm", ("The AVL condition forces a logarithmic height",
                     "Let `N(h)` be the fewest nodes in an AVL tree of height `h`. Then "
                     "`N(0) = 1`, `N(1) = 2`, and `N(h) = N(h−1) + N(h−2) + 1`.",
                     "A tree of height `h` has a subtree of height exactly `h−1`. The "
                     "other subtree has height at least `h−2`, because the balance "
                     "condition forbids a difference of `2` or more. To make the total as "
                     "small as possible, take the smallest trees of those two heights, "
                     "plus the root: that is the recurrence. Since `N(h) + 1` is the "
                     "Fibonacci number `F(h+3)`, `N(h)` grows like `φʰ`, so a tree on `n` "
                     "nodes has `h ≤ log_φ n`, which is about `1.44 log₂ n`.")),
            ("math", [
                "h      N(h)   from the recurrence        fits inside n nodes?",
                "",
                "0         1    by definition",
                "1         2    by definition",
                "2         4    N(1) + N(0) + 1",
                "3         7    N(2) + N(1) + 1",
                "4        12    N(3) + N(2) + 1",
                "5        20    N(4) + N(3) + 1",
                "6        33    N(5) + N(4) + 1",
                "7        54    N(6) + N(5) + 1",
                "8        88    N(7) + N(6) + 1",
                "",
                "N(h) + 1  =  2  3  5  8  13  21  34  55  89     Fibonacci",
            ]),
            ("p", "To bound the height of an AVL tree on `n` nodes, read up the `N(h)` "
                  "column for the largest `h` whose entry is at most `n`. Six nodes: "
                  "`N(2) = 4 ≤ 6` and `N(3) = 7 > 6`, so the height is at most `2`. A "
                  "thousand nodes: `N(13) = 986` fits and `N(14) = 1596` does not, so the "
                  "height is at most `13`."),
            ("p", "Compare that with the closed form. `1.44 log₂ 1000` is `14.35`, so the "
                  "closed form permits `14` where the exact table permits `13`. Both are "
                  "correct bounds and the table is tighter, which is why the lab evaluates "
                  "the recurrence instead of the logarithm: the recurrence is integer "
                  "arithmetic with nothing to round, and the constant `1.44` is itself a "
                  "rounded `1/log₂ φ`. Quoting `1.44 log₂ n` is fine as a shape; using it "
                  "as a number when an exact table is available is throwing away accuracy "
                  "for no reason."),
        ],
        "lab": ("tree", {
            "mode": "rotate",
            "preset": "right-heavy",
            "panel_title": "Rotate, compare the in-order sequences, and read the height bound",
            "panel_intro": "Type the keys, choose a node by its in-order position and a "
                           "direction. Before and after are drawn side by side with balance "
                           "factors above each node, the two in-order sequences are printed to "
                           "be compared directly, and the panel reports whether the rotation "
                           "was possible at all. The `N(h)` table is evaluated from the "
                           "recurrence and the row that bounds this tree is highlighted.",
        }),
        "steps_title": "Rotating, and bounding a height",
        "steps_intro": "The rotation is mechanical and the bound is arithmetic. What needs care is checking each one rather than assuming it.",
        "steps": [
            ("Name the node and check the child exists",
             "A right rotation needs a left child to lift; a left rotation needs a right "
               "child. Without it there is no rotation, and a tool that returns the tree "
               "unchanged in that case is indistinguishable from one that worked."),
            ("Perform it as three pointer moves",
             "The child rises, the node becomes its child on the opposite side, and the "
             "child&rsquo;s inner subtree re-parents onto the node. Write the three moves "
             "down rather than redrawing the tree from intuition &mdash; that is where the "
             "inner subtree gets dropped."),
            ("Write both in-order sequences and compare them",
             "Symbol by symbol. They must be identical. This is the check that a rotation "
             "was performed rather than a tree rearranged, and it costs one line. Then "
             "look at the heights, which are the thing that was supposed to change."),
            ("Bound a height by reading the N(h) table upward",
             "Find the largest `h` with `N(h) ≤ n`. That is the bound for `n` nodes, and "
             "it is exact. Compare it with `1.44 log₂ n` if you like, and expect the "
             "closed form to be looser &mdash; at `n = 1000` it permits one level more "
             "than the table does."),
        ],
        "worked": {
            "title": "One rotation, and the height bound at six nodes",
            "intro": [
                "The lab&rsquo;s opening preset, with the three pointer moves written out and "
                "the table read for the tree that results."
            ],
            "lines": [
                "keys 50 30 70 20 40 10        in-order 10 20 30 40 50 70",
                "",
                "before                        balance factors",
                "         50                   50:  h_L 2, h_R 0  →  +2   VIOLATES AVL",
                "     30      70               30:  h_L 1, h_R 0  →  +1",
                "  20    40                    20:  h_L 0, h_R −1 →  +1",
                "10                            height 3",
                "",
                "rotate RIGHT at 50:",
                "  1.  y = 30 rises into 50's place",
                "  2.  50 becomes the right child of 30",
                "  3.  30's old right subtree (40) becomes 50's left subtree",
                "",
                "after                         balance factors",
                "         30                   30:  h_L 1, h_R 1  →   0",
                "     20      50               20:  h_L 0, h_R −1 →  +1",
                "  10       40   70            50:  h_L 0, h_R 0  →   0",
                "                              height 2",
                "",
                "in-order  10 20 30 40 50 70   identical, as the theorem requires",
                "",
                "height bound at n = 6:   N(2) = 4 ≤ 6,  N(3) = 7 > 6   ⟹   h ≤ 2",
                "the rotated tree has height 2 and is therefore as short as 6 nodes allow",
            ],
            "after": [
                "The three pointer moves are the whole operation and the third is the one "
                "that gets forgotten. `30`&rsquo;s right subtree cannot stay with `30` "
                "&mdash; `30` now has `50` there &mdash; and it cannot go anywhere except "
                "`50`&rsquo;s left, because its keys are between `30` and `50`. The "
                "in-order sequence forces it.",
                "The table gives `h ≤ 2` at six nodes and the rotated tree achieves it, "
                "which is a pleasant coincidence of this example rather than something a "
                "single rotation generally does. The pre-rotation tree had a balance "
                "factor of `+2` at the root and was not an AVL tree at all; one rotation "
                "fixed it here because the imbalance was on the outside.",
                "For a faded rehearsal, build `50 30 70 20 40 35 45` and rotate left at "
                "`30`. The supplied observation is that the in-order sequence must be "
                "`20 30 35 40 45 50 70` before and after. Carry out the three moves, "
                "confirm the sequence, and note that the height is `3` both times: the "
                "rotation was legal, was performed, and did not shorten the tree. Then say "
                "what that means for a rule that has to choose which rotation to perform.",
            ],
        },
        "quiz_title": "Rotations and the bound",
        "quiz": [
            {"q": "A right rotation is performed at the root of a valid search tree. What must be true of the in-order sequence afterwards?",
             "a": ["It is reversed", "It is unchanged",
                   "It is unchanged only if the tree was balanced before",
                   "It changes by one transposition"],
             "c": 1,
             "why": "A rotation re-parents subtrees without moving any key past another in "
                    "the sorted order: `A, y, B, x, C` before and after. That is why the "
                    "search-tree invariant survives every rotation automatically, balanced "
                    "or not. If the sequence ever changed, the operation performed was not "
                    "a rotation."},
            {"q": "What is the fewest nodes an AVL tree of height `4` can have?",
             "a": ["`7`", "`12`", "`15`", "`16`"],
             "c": 1,
             "why": "`N(4) = N(3) + N(2) + 1 = 7 + 4 + 1 = 12`. `7` is `N(3)`. `15` is the "
                    "<em>most</em> nodes a tree of height `3` can have &mdash; a perfect "
                    "tree &mdash; and `16` is `2⁴`. The recurrence asks for the smallest "
                    "tree that still satisfies the balance condition, which is one subtree "
                    "of height `3`, one of height `2`, and a root."},
            {"q": "An AVL tree holds `1000` nodes. The table gives `N(13) = 986` and `N(14) = 1596`, and `1.44 log₂ 1000 = 14.35`. Which height bound should the page print?",
             "a": ["`14`, from the closed form",
                   "`13`, from the table, because it is exact and tighter",
                   "`10`, which is `log₂ 1000`",
                   "Either: they are the same bound"],
             "c": 1,
             "why": "`N(14)` exceeds `1000`, so no AVL tree on `1000` nodes can have height "
                    "`14`; the exact bound is `13`. The closed form permits `14` because "
                    "`1.44` is a rounded `1/log₂ φ` and the derivation drops the `+1` in "
                    "the recurrence. Both are correct upper bounds and they are not the "
                    "same number. `log₂ 1000 ≈ 10` is the height of a perfect tree, which "
                    "is a lower bound rather than the AVL limit."},
        ],
        "mistakes": [
            ("Thinking a rotation rearranges keys",
             "No key changes its position in the sorted order &mdash; only pointers move, "
             "and the in-order sequence is identical before and after. The habit that "
             "prevents the confusion is to write both sequences out and compare them, "
             "which also catches the genuine error: dropping the inner subtree when "
             "re-parenting it."),
            ("Expecting every rotation to reduce the height",
             "Rotating left at `30` in the tree from `50 30 70 20 40 35 45` leaves the "
             "height at `3`. A rotation is a legal rewrite, not a repair, and choosing "
             "which one to perform at which node is a separate matter that the insertion "
             "rules settle. A rotation performed in the wrong direction can make a tree "
             "taller."),
            ("Quoting `1.44 log₂ n` when the exact table is available",
             "At `n = 1000` the closed form permits height `14` and the recurrence permits "
             "`13`. The constant is a rounded `1/log₂ φ` and the derivation discards the "
             "`+1` in `N(h) = N(h−1) + N(h−2) + 1`. Use the closed form to say the shape "
             "is logarithmic; use the table when you want the number."),
        ],
        "standard": ("Finish when you can perform a rotation as three pointer moves and prove it legal with one line of in-order.",
                     "You should be able to rotate at a named node in either direction, "
                     "state which child must exist for it to be possible, write both "
                     "in-order sequences and confirm they match, tabulate `N(h)` from the "
                     "recurrence, and read an exact height bound off the table for a stated "
                     "`n`."),
        "note": (
            "A rotation is the tool; the rule for using it is four cases. &ldquo;AVL "
            "Insertion&rdquo; fixes the lowest unbalanced ancestor after an insert, names "
            "the case &mdash; two of the four need a double rotation &mdash; and measures "
            "the resulting height against the plain search tree on the very same insertion "
            "order, which at ten keys in increasing order is `3` against `9`."
        ),
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "avl-insertion",
        "title": "AVL Insertion",
        "module": "Search trees",
        "one_line": "Insert a key sequence into an AVL tree naming the case at each rebalance, and compare the height with the plain tree on the same order.",
        "summary": (
            "After an insertion, at most one node is out of balance &mdash; the lowest "
            "unbalanced ancestor &mdash; and one of four cases applies. The outside cases "
            "need a single rotation, the inside cases need two, and one fix restores "
            "balance all the way to the root. Ten keys in increasing order give height "
            "`3` with six rebalances, against `9` for the plain tree on the same order."
        ),
        "key": [
            "after an insert, walk back up;  fix the LOWEST unbalanced ancestor",
            "",
            "balance +2, key in the left child's LEFT  subtree     LL    rotate right",
            "balance −2, key in the right child's RIGHT subtree    RR    rotate left",
            "balance +2, key in the left child's RIGHT subtree     LR    left, then right",
            "balance −2, key in the right child's LEFT  subtree    RL    right, then left",
            "",
            "1 … 10 in order:   AVL height 3, 6 rebalances    plain tree height 9",
        ],
        "key_label": "The four cases, and what one fix costs",
        "concepts_intro": (
            "One decision procedure, one counting fact, and one thing that is genuinely "
            "surprising the first time: fixing a single node fixes the whole tree."
        ),
        "concepts": [
            ("Only the ancestors of the new key can be unbalanced",
             "An insertion changes the height of nothing except the nodes on the path from "
             "the new leaf to the root, because every other subtree is untouched. So the "
             "repair walks back up that path, and the node to fix is the lowest one whose "
             "balance factor has reached `±2`."),
            ("The case is decided by two turns, not by the keys",
             "Look at the direction from the unbalanced node to its taller child, and then "
             "from that child toward the new key. Same direction twice &mdash; left-left "
             "or right-right &mdash; and one rotation suffices. Different directions "
             "&mdash; left-right or right-left &mdash; and one rotation moves the problem "
             "sideways rather than fixing it, so two are needed."),
            ("One fix restores the whole tree",
             "After the rebalance the subtree is exactly as tall as it was before the "
             "insertion, so every ancestor&rsquo;s balance factor returns to what it was, "
             "and none of them needs anything. That is why an AVL insertion costs at most "
             "one single or one double rotation regardless of `n`, and it is a property of "
             "insertion specifically &mdash; deletion can need a rotation at every level, "
             "which is one reason this course states AVL deletion and does not develop "
             "it."),
        ],
        "read_title": "The four cases, the double rotation, and the height against the plain tree",
        "read_intro": "Why the inside cases need two rotations, why one fix is enough, and what the measured heights are on the same insertion order.",
        "body": [
            ("p", "Insert the key exactly as in a plain search tree: walk to where the "
                  "search fails and attach a leaf. Then walk back up the path updating "
                  "heights. If some node&rsquo;s balance factor reaches `+2` or `−2`, "
                  "rebalance there and stop. The lowest such node is the one to fix, and "
                  "there is at most one of them."),
            ("h3", "The two outside cases"),
            ("p", "Suppose node `z` has balance `+2` &mdash; its left subtree is two "
                  "taller &mdash; and the new key went into the LEFT subtree of "
                  "`z`&rsquo;s left child. That is the LL case, and one right rotation at "
                  "`z` fixes it: the left child rises, `z` drops to its right, and the two "
                  "sides come out equal. RR is the mirror image, fixed by one left "
                  "rotation."),
            ("math", [
                "LL,  keys 30 20 10                       one right rotation at 30",
                "",
                "      30   (+2)                                  20   (0)",
                "   20                                        10      30",
                "10",
                "",
                "RR,  keys 10 20 30                       one left rotation at 10",
                "",
                "  10   (−2)                                      20   (0)",
                "      20                                     10      30",
                "         30",
            ]),
            ("h3", "The two inside cases, and why one rotation is not enough"),
            ("p", "Now suppose `z` has balance `+2` and the new key went into the RIGHT "
                  "subtree of `z`&rsquo;s left child &mdash; the LR case. A single right "
                  "rotation at `z` lifts the left child, but the offending subtree was on "
                  "that child&rsquo;s right, so it lands back on the left of `z` and the "
                  "tree is now `−2` the other way. The fix is to rotate the child left "
                  "first, converting LR into LL, and then rotate `z` right."),
            ("math", [
                "LR,  keys 30 10 20",
                "",
                "      30   (+2)          rotate 10 LEFT:      30          then 30 RIGHT:",
                "   10                                      20                    20",
                "      20                                10                   10      30",
                "",
                "  the grandchild 20 ends up as the root, which is what a double rotation",
                "  always does:  the INNER grandchild rises two levels",
                "",
                "RL,  keys 10 30 20       rotate 30 RIGHT, then 10 LEFT     same result",
            ]),
            ("p", "The lab names the case at every rebalance and animates it. On the "
                  "three-key sequences above it reports `LL`, `LR` and `RL` respectively, "
                  "each with one rebalance, each ending at the same tree "
                  "`20` with children `10` and `30` &mdash; the same final shape reached "
                  "three different ways, which is worth seeing because it makes the case "
                  "analysis feel less arbitrary."),
            ("thm", ("One rebalance per insertion suffices",
                     "After an AVL insertion, rebalancing the lowest unbalanced ancestor "
                     "restores the invariant everywhere.",
                     "Before the insertion the subtree rooted at that node had some height "
                     "`h`. The insertion made it `h + 1`, which is what unbalanced it. "
                     "Both the single and the double rotation return the subtree to height "
                     "`h`. So from that node upward nothing has changed height at all, and "
                     "every ancestor&rsquo;s balance factor is what it was before the "
                     "insertion &mdash; which was legal. Hence one fix, at most two "
                     "rotations, regardless of how tall the tree is.")),
            ("h3", "The measurement, on the input that breaks a plain tree"),
            ("p", "Insert `1` through `10` in increasing order &mdash; the order that "
                  "turns a plain search tree into a path. The lab runs both:"),
            ("math", [
                "keys 1 2 3 4 5 6 7 8 9 10,  in order",
                "",
                "                        AVL      plain BST",
                "height                    3              9",
                "rebalances                6              —",
                "comparisons              25",
                "",
                "the six fixes, in order:   RR at 3, RR at 5, RR at 6,",
                "                           RR at 7, RR at 9, RR at 10",
                "",
                "height bound from N(h) at n = 10:   N(3) = 7 ≤ 10,  N(4) = 12 > 10",
                "                                    so h ≤ 3,  and the tree achieves it",
            ]),
            ("p", "Every one of the six fixes is the RR case, because every key arrives "
                  "larger than everything present. Height `3` against `9`, on the input "
                  "that is worst for the plain tree and costs the AVL tree six rotations "
                  "&mdash; one per rebalance, since RR is a single rotation. The bound "
                  "from the `N(h)` table is `3`, and the tree reaches it."),
            ("p", "A mixed order shows all four cases and a smaller gap. On the "
                  "thirteen keys `50 25 75 10 5 30 27 60 90 80 70 98 62` the lab reports "
                  "four rebalances &mdash; `LL` at `5`, `LR` at `30`, `RR` at `80`, `RL` "
                  "at `62` &mdash; giving height `3` against the plain tree&rsquo;s `4`, "
                  "with `33` comparisons. The gap is one level, because that order was "
                  "already reasonably balanced. Which is the caution: the measured benefit "
                  "of balancing depends entirely on the order you measured it on, and the "
                  "guarantee &mdash; `h ≤ 1.44 log₂ n` for every order &mdash; is the "
                  "reason to pay for it."),
        ],
        "lab": ("tree", {
            "mode": "avl",
            "preset": "mixed",
            "panel_title": "Insert, and watch the case get named",
            "panel_intro": "Type a key sequence. Each insertion is animated, every rebalance "
                           "is labelled `LL`, `RR`, `LR` or `RL` with the node it happened at, "
                           "and the panel reports the resulting height beside the plain search "
                           "tree&rsquo;s height on the identical order. The opening sequence "
                           "produces all four cases; the ascending preset produces six of one "
                           "case and the largest gap.",
        }),
        "steps_title": "Inserting into an AVL tree",
        "steps_intro": "Insert, then walk up, then name the case before rotating. Naming it first is what stops a double rotation being attempted as a single one.",
        "steps": [
            ("Insert as an ordinary search tree, then walk back up",
             "The key goes where the search failed. Update the height at each node on the "
             "way back to the root and watch the balance factors. Stop at the first node "
             "&mdash; the lowest &mdash; whose factor reaches `±2`."),
            ("Name the case from two directions",
             "From the unbalanced node to its taller child: left or right. From that child "
             "toward the new key: left or right. Same twice is LL or RR; different is LR "
             "or RL. The keys&rsquo; values play no part beyond telling you which way the "
             "walk went."),
            ("Rotate once for an outside case, twice for an inside one",
             "LL: rotate right at the unbalanced node. RR: rotate left. LR: rotate the "
             "left child left, then the node right. RL: rotate the right child right, then "
             "the node left. In the double cases the inner grandchild ends up as the "
             "subtree root, which is the thing to check afterwards."),
            ("Stop, and verify you may",
             "One fix is enough: the subtree is back to its pre-insertion height, so no "
             "ancestor has changed. Confirm it by checking the balance factor at the "
             "parent of where you rotated &mdash; it should be what it was before the "
             "insertion, and if it is not, the rotation was wrong."),
        ],
        "worked": {
            "title": "Four keys that produce an inside case",
            "intro": [
                "The LR case in full, because it is the one people attempt as a single "
                "rotation. Keys arriving `30, 10, 20`."
            ],
            "lines": [
                "insert 30        30                        balance 0",
                "",
                "insert 10        30   (+1)                 still legal",
                "              10",
                "",
                "insert 20        30   (+2)                 lowest unbalanced node: 30",
                "              10                           from 30 to taller child: LEFT",
                "                 20                        from 10 toward 20:      RIGHT",
                "                                           →  LR, a double rotation",
                "",
                "  the single rotation that does NOT work:  rotate 30 right",
                "                 10                       balance at 10 is now −2",
                "                    30                    the problem moved, unfixed",
                "                 20",
                "",
                "  step 1:  rotate 10 LEFT      30          now it is an LL case",
                "                            20",
                "                         10",
                "",
                "  step 2:  rotate 30 RIGHT     20          balance 0 everywhere",
                "                            10    30",
                "",
                "in-order 10 20 30 throughout    height 2 → 1    one rebalance, named LR",
            ],
            "after": [
                "The failed single rotation is the useful half of this example. Rotating "
                "`30` right lifts `10`, but `20` was hanging on `10`&rsquo;s right, so it "
                "comes along and lands under `30` again &mdash; the tree is now left-light "
                "instead of left-heavy and is still illegal. The first rotation of the "
                "double exists to move `20` onto the outside, where a single rotation can "
                "reach it.",
                "The inner grandchild ends as the subtree root. That is true of every "
                "double rotation and is the quickest way to check one: in the LR case the "
                "right child of the left child rises two levels. If something else ended "
                "up on top, the two rotations were done in the wrong order.",
                "For a faded rehearsal, insert `10, 30, 20` &mdash; the RL case, the "
                "mirror of this one. The supplied observation is that it must end at the "
                "same tree, `20` with children `10` and `30`, because there is only one "
                "AVL tree on three keys. Name the two rotations and their nodes, then run "
                "the lab&rsquo;s ascending preset and say why all six of its rebalances "
                "are the same case.",
            ],
        },
        "quiz_title": "Cases and counts",
        "quiz": [
            {"q": "A node has balance factor `+2` and the newly inserted key went into the right subtree of that node&rsquo;s left child. Which case is it?",
             "a": ["LL, one right rotation", "LR, a left rotation then a right one",
                   "RL, a right rotation then a left one", "RR, one left rotation"],
             "c": 1,
             "why": "`+2` means left-heavy, so the first letter is L; the key went right "
                    "from there, so the second is R. LR is an inside case and needs two "
                    "rotations: the left child rotates left to move the offending subtree "
                    "outward, then the unbalanced node rotates right. A single right "
                    "rotation leaves the tree unbalanced the other way."},
            {"q": "Inserting `1` through `10` in increasing order gives an AVL tree of height `3` and a plain search tree of height `9`. How many rebalances did the AVL insertion perform?",
             "a": ["`1`", "`3`", "`6`", "`9`"],
             "c": 2,
             "why": "The lab counts six, all of them RR, because every arriving key is "
                    "larger than everything present. One rebalance per insertion is the "
                    "maximum, not the rule &mdash; four of the ten insertions needed "
                    "nothing. `3` is the resulting height and `9` is the plain "
                    "tree&rsquo;s."},
            {"q": "Why does rebalancing one node restore the invariant for the whole tree after an insertion?",
             "a": ["Because the rotations are applied bottom-up until the root is reached",
                   "Because the rotation returns that subtree to its height before the insertion, so no ancestor changed",
                   "Because an insertion can only unbalance the root",
                   "Because the balance factors are recomputed for every node afterwards"],
             "c": 1,
             "why": "The insertion raised that subtree from `h` to `h + 1`; both the single "
                    "and the double rotation bring it back to `h`. Every ancestor "
                    "therefore sees the height it saw before the insertion, and their "
                    "balance factors were legal then. No further walking is needed &mdash; "
                    "which is specific to insertion, since a deletion can require a "
                    "rotation at every level."},
        ],
        "mistakes": [
            ("Attempting an inside case with a single rotation",
             "Rotating `30` right in the tree `30, 10, 20` lifts `10` and brings `20` "
             "along with it, leaving the tree unbalanced in the opposite direction. The "
             "first rotation of a double exists to move the offending subtree to the "
             "outside. The check afterwards is that the inner grandchild is now the "
             "subtree root."),
            ("Rebalancing the highest unbalanced node instead of the lowest",
             "Walk up from the new leaf and fix the first node that reaches `±2`. Fixing a "
             "higher one first can leave the lower one illegal, and the argument that one "
             "fix suffices depends on the subtree returning to the height it had before "
             "the insertion &mdash; which is only true of the lowest such node."),
            ("Reading the measured height gap as the value of balancing",
             "On increasing keys the gap is `3` against `9`; on a reasonably mixed order "
             "it is `3` against `4`. Both are real measurements and neither is the reason "
             "to use an AVL tree. The reason is the guarantee &mdash; `h ≤ 1.44 log₂ n` on "
             "every input, including the one you did not test &mdash; and a measured gap "
             "on a chosen order is not that."),
        ],
        "standard": ("Finish when you can name the case from two turns before touching a pointer.",
                     "You should be able to insert a key sequence by hand, identify the "
                     "lowest unbalanced ancestor, name the case, perform the right number of "
                     "rotations with the inner grandchild ending on top in the double cases, "
                     "and say why one fix suffices for an insertion in terms of the "
                     "subtree&rsquo;s height."),
        "note": (
            "A balanced tree gives search, predecessor and an ordered walk in "
            "`O(log n)`, and one extra integer per node gives it two more operations. "
            "&ldquo;Augmenting a Tree&rdquo; stores the subtree size at every node, gets "
            "`rank` and `select` in `O(log n)` from it, and shows the rotation updating the "
            "field &mdash; which is the part that goes stale if it is forgotten."
        ),
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "augmenting-a-tree",
        "title": "Augmenting a Tree",
        "module": "Search trees",
        "one_line": "Compute rank and select by walking a size-annotated tree, and say which attributes can ride along and which cannot.",
        "summary": (
            "Store the size of each subtree at its root and a search tree answers two new "
            "questions in `O(log n)`: the rank of a key, and the i-th smallest key. The "
            "rule for what else can be added is sharp &mdash; any attribute computable "
            "from a node&rsquo;s own key and its two children&rsquo;s attributes in "
            "constant time. A median field is not one. And every rotation must update the "
            "field, or it goes quietly stale."
        ),
        "key": [
            "augment    size[x] = size[left] + size[right] + 1      one integer per node",
            "",
            "select(i)    left = size[left];  i = left+1 → here;  i ≤ left → left;  else i −= left+1, right",
            "rank(k)      walk to k, adding size[left]+1 at every RIGHT turn",
            "",
            "both visit one root-to-leaf path      O(height) = O(log n) in a balanced tree",
            "",
            "maintainable: size, sum, min, max     NOT maintainable: a median field",
        ],
        "key_label": "One integer a node, two new queries, and the rule for what else fits",
        "concepts_intro": (
            "One mechanism, one criterion, and one maintenance obligation. The criterion "
            "is what makes this a technique rather than a trick, and the obligation is "
            "where it breaks in practice."
        ),
        "concepts": [
            ("Subtree size turns a search into counting",
             "At a node, the size of the left subtree tells you how many keys are smaller "
             "than this one within this subtree. That single number converts the "
             "search-tree walk into an arithmetic walk: `select` subtracts as it goes "
             "right, `rank` accumulates as it goes right, and both finish in one "
             "root-to-leaf path."),
            ("An attribute can ride along if a node can compute it from its children",
             "The criterion is constant-time computability from the node&rsquo;s own key "
             "and the attribute values at its two children. Size qualifies: "
             "`1 + left + right`. So do sum, min, max, and the count of keys satisfying a "
             "fixed predicate. A median does not: knowing the medians of two subtrees and "
             "one key does not determine the median of the whole, so maintaining it would "
             "cost more than a constant per node and the technique gives nothing."),
            ("Every structural change must update the attribute",
             "An insertion increments the size at each node on its path. A rotation "
             "rearranges three subtrees and must recompute the sizes at the two nodes "
             "involved, bottom-up. Forget it and the field is wrong while the tree is "
             "correct, which means `select` returns the wrong key and nothing complains. "
             "The lab rotates a size-annotated tree and prints the sizes before and after "
             "for exactly that reason."),
        ],
        "read_title": "Two queries from one integer, and the rule for adding a third",
        "read_intro": "How select and rank walk, what a range count costs, which attributes are maintainable, and what a rotation has to do.",
        "body": [
            ("def", ("Size-augmented search tree",
                     "A search tree in which every node `x` stores "
                     "`size[x] = size[left(x)] + size[right(x)] + 1`, the number of nodes "
                     "in the subtree rooted at `x`. An empty subtree has size `0`.",
                     "The field costs one machine word per node and is maintained by "
                     "insertion, deletion and rotation. Nothing else about the tree "
                     "changes.")),
            ("p", "<strong>select(i)</strong>, the i-th smallest key, counting from `1`. "
                  "At a node, let `L` be the size of its left subtree. If `i = L + 1` the "
                  "answer is this node&rsquo;s key, because exactly `L` keys in this "
                  "subtree are smaller. If `i ≤ L` the answer is in the left subtree at "
                  "the same rank. Otherwise it is in the right subtree at rank "
                  "`i − (L + 1)`, because the left subtree and this node account for "
                  "`L + 1` of the keys below it."),
            ("p", "<strong>rank(k)</strong>, how many keys are at most `k`. Walk toward "
                  "`k` from the root, keeping a running count. Each time the walk goes "
                  "right, every key in the left subtree and the node itself are below `k`, "
                  "so add `L + 1`. Each time it goes left, add nothing. When `k` is found, "
                  "add `L + 1` one last time."),
            ("math", [
                "tree from 50 25 75 12 37 62 87 6 18        sizes in brackets",
                "",
                "                      50 [9]",
                "              25 [5]           75 [3]",
                "        12 [3]      37 [1]   62 [1]  87 [1]",
                "     6 [1]  18 [1]",
                "",
                "in-order   6  12  18  25  37  50  62  75  87",
                "rank        1   2   3   4   5   6   7   8   9",
            ]),
            ("math", [
                "select(3):   at 50, L = 5,  3 ≤ 5              go left",
                "             at 25, L = 3,  3 ≤ 3              go left",
                "             at 12, L = 1,  3 > 1+1  →  i = 1  go right",
                "             at 18, L = 0,  1 = 0+1            ANSWER 18",
                "                                              4 nodes visited",
                "",
                "rank(62):    at 50, 62 > 50  →  add 5+1 = 6,   go right",
                "             at 75, 62 < 75  →  add 0,         go left",
                "             at 62, found    →  add 0+1 = 1,   ANSWER 7",
                "                                              3 nodes visited",
            ]),
            ("p", "Four nodes for `select(3)` and three for `rank(62)`, on a tree of "
                  "height `3`. Both walks are one path and nothing else, which is the "
                  "whole claim: `O(height)`, and `O(log n)` once the tree is balanced. "
                  "Without the size field, `select(3)` would need an in-order traversal "
                  "counting as it went &mdash; `O(n)` &mdash; and `rank` would need the "
                  "same. The `3` and the `4` are counts on the tree drawn, whose "
                  "height is `3` because that insertion order was kind; the claim is "
                  "`O(height)`, and on the sorted order of the shape-problem lesson "
                  "the identical queries would walk `n`. The augmentation buys "
                  "`O(log n)` only on top of something that keeps the tree short, "
                  "which is why an order-statistic tree is an AVL tree with a size "
                  "field rather than a search tree with one."),
            ("h3", "Counting a range, as two walks"),
            ("p", "How many keys lie in `[20, 70]`? Count the keys at most `70` and "
                  "subtract the keys below `20`. Each count is a rank-style walk adding a "
                  "subtree size at every right turn, so the query is two paths rather than "
                  "a scan: the lab reports `4` &mdash; `25, 37, 50, 62` &mdash; from `7` "
                  "nodes visited across both walks. Listing the keys would of course cost "
                  "the number of keys listed; counting them does not."),
            ("h3", "What can be augmented, and what cannot"),
            ("thm", ("The augmentation criterion",
                     "An attribute `f` can be maintained on a search tree at constant "
                     "extra cost per structural change if `f(x)` is computable in constant "
                     "time from the key at `x` and the values `f(left(x))` and "
                     "`f(right(x))`.",
                     "Insertion and deletion change `f` only on one root-to-leaf path, and "
                     "a rotation changes it only at the two nodes it rearranges; in each "
                     "case recomputing bottom-up from the criterion costs a constant per "
                     "node touched. Size satisfies it with `1 + left + right`, sum with "
                     "`key + left + right`, min with `min(key, left)`. A median does not: "
                     "the median of a set is not a constant-time function of one key and "
                     "the medians of two subsets, so the field would have to be rebuilt "
                     "and the technique buys nothing.")),
            ("p", "That criterion is the reusable part of this lesson. It is why an "
                  "interval tree can store the maximum endpoint in a subtree, why an "
                  "order-statistic tree stores sizes, and why nobody stores a median. The "
                  "question to ask about any proposed field is not whether it is useful "
                  "but whether a node could recompute it from its two children without "
                  "looking further down."),
            ("h3", "The rotation that has to update the field"),
            ("p", "Rotate left at `25` in the tree above. The node `37` rises, `25` "
                  "becomes its left child, and the sizes must be recomputed at `25` first "
                  "and then at `37`:"),
            ("math", [
                "before                         after rotating LEFT at 25",
                "",
                "         50 [9]                        50 [9]",
                "   25 [5]      75 [3]            37 [5]      75 [3]",
                "12 [3]  37 [1]                 25 [4]",
                "                              12 [3]",
                "",
                "  25: 3 + 0 + 1 = 4     recomputed first, from its own children",
                "  37: 4 + 0 + 1 = 5     then the new subtree root",
                "  50: 5 + 3 + 1 = 9     unchanged, as it must be",
            ]),
            ("p", "The order matters: recompute the node that descended before the node "
                  "that rose, because the riser&rsquo;s value depends on it. The lab "
                  "checks every size in the tree against a fresh recount after the "
                  "rotation and reports whether they all agree &mdash; which is the kind "
                  "of check worth having, because a stale size field produces wrong "
                  "answers from a structurally perfect tree and no error anywhere."),
        ],
        "lab": ("tree", {
            "mode": "augment",
            "preset": "select",
            "panel_title": "Walk a size-annotated tree, and rotate one",
            "panel_intro": "Choose a query &mdash; select the i-th smallest, rank a key, or "
                           "count an interval &mdash; and the walk is drawn step by step with "
                           "the left-subtree size and the running arithmetic at each node, and "
                           "the nodes visited are counted. The panel also rotates the tree and "
                           "re-checks every size field against a fresh count, because a stale "
                           "field is a wrong answer from a correct tree.",
        }),
        "steps_title": "Querying and maintaining an augmented tree",
        "steps_intro": "The walk is arithmetic, so the discipline is to write the arithmetic down at each node rather than following the shape by eye.",
        "steps": [
            ("Write the left-subtree size at every node you visit",
             "`L` is the only thing either query needs from a node besides its key. "
             "Writing it down at each step is what makes the two rules mechanical instead "
             "of a guess about which way the target lies."),
            ("For select, compare i with L + 1 and adjust when you go right",
             "`i = L + 1` stops. `i ≤ L` goes left with `i` unchanged. Otherwise go right "
             "with `i` reduced by `L + 1`. Forgetting the reduction is the standard error "
             "and it gives an answer that is too small by the number of keys skipped."),
            ("For rank, accumulate L + 1 at every right turn and only there",
             "Going left passes over nothing that is below the target. Going right passes "
             "over the whole left subtree and the node, so add `L + 1`. At the target, add "
             "`L + 1` once more for the keys below it in its own left subtree, plus "
             "itself."),
            ("After any structural change, recompute the field bottom-up",
             "An insertion increments along its path. A rotation recomputes at the "
             "descending node first and the rising node second. Then check the invariant "
             "`size[x] = size[left] + size[right] + 1` somewhere, because nothing else in "
             "the structure will notice if it fails."),
        ],
        "worked": {
            "title": "select(5), rank(37), and the keys in [20, 70]",
            "intro": [
                "Three queries on the same nine-node tree, with the node count for each. "
                "The in-order sequence is `6 12 18 25 37 50 62 75 87`."
            ],
            "lines": [
                "                      50 [9]",
                "              25 [5]           75 [3]",
                "        12 [3]      37 [1]   62 [1]  87 [1]",
                "     6 [1]  18 [1]",
                "",
                "select(5)     node   L    test                  action",
                "                50   5    5 ≤ 5                  go left",
                "                25   3    5 > 3+1  →  i = 1      go right",
                "                37   0    1 = 0+1                ANSWER 37",
                "              3 nodes visited",
                "",
                "rank(37)      node        running                action",
                "                50   L=5   37 < 50, add 0        go left",
                "                25   L=3   37 > 25, add 3+1 = 4  go right",
                "                37   L=0   found,   add 0+1 = 5  ANSWER 5",
                "              3 nodes visited",
                "",
                "count [20, 70]   = (keys ≤ 70) − (keys < 20)",
                "                 =        7     −      3        = 4",
                "              7 nodes visited across the two walks",
                "              the four keys are 25 37 50 62",
            ],
            "after": [
                "`select(5)` and `rank(37)` are inverse queries and both cost three nodes "
                "on this tree, which is the point of the pair: one integer per node bought "
                "two operations that a plain search tree cannot perform at all without a "
                "full traversal.",
                "The range count is `4` from seven nodes visited, and the seven is worth "
                "noticing: it is two independent walks down a tree of height `3`, not a "
                "scan of the four keys. If the query had been to <em>list</em> the keys "
                "the cost would include them; counting them does not, and that asymmetry "
                "is exactly what the augmentation is for.",
                "For a faded rehearsal, compute `select(9)` and `rank(62)` on the same "
                "tree. The supplied first step for `select(9)` is that `L = 5` at the "
                "root and `9 > 6`, so the walk goes right with `i = 3`. Finish both, "
                "predict the node counts, and check them in the lab &mdash; three each. "
                "Then rotate left at `25` and write down the two sizes that change, in the "
                "order they must be recomputed.",
            ],
        },
        "quiz_title": "Walks and maintenance",
        "quiz": [
            {"q": "On a size-augmented tree, `select(i)` is at a node whose left subtree has size `L` and `i > L + 1`. What does it do?",
             "a": ["Go right with `i` unchanged",
                   "Go right with `i` reduced by `L + 1`",
                   "Go left with `i` reduced by `L`",
                   "Return this node&rsquo;s key"],
             "c": 1,
             "why": "The left subtree holds `L` keys smaller than this node, and the node "
                    "is one more, so `L + 1` keys have been passed over: the target is the "
                    "`(i − L − 1)`-th smallest in the right subtree. Going right without "
                    "adjusting `i` returns a key that is too large by `L + 1` positions "
                    "&mdash; the standard error here."},
            {"q": "Which of these attributes cannot be maintained by an augmented search tree at constant cost per structural change?",
             "a": ["the sum of the keys in each subtree",
                   "the minimum key in each subtree",
                   "the median key in each subtree",
                   "the number of even keys in each subtree"],
             "c": 2,
             "why": "The criterion is constant-time computability from the node&rsquo;s key "
                    "and its two children&rsquo;s values. Sum is `key + left + right`; min "
                    "is `min(key, left)`; a count of keys satisfying a fixed predicate is "
                    "`left + right + [predicate holds here]`. The median of a set is not "
                    "determined by one key and the medians of two subsets, so no "
                    "constant-time recomputation exists."},
            {"q": "A rotation is performed on a size-augmented tree and the size fields are not updated. What happens?",
             "a": ["The tree stops being a search tree",
                   "The next insertion fails",
                   "The tree is structurally correct and `select` returns wrong answers, with nothing reporting an error",
                   "The sizes correct themselves on the next traversal"],
             "c": 2,
             "why": "A rotation preserves the search-tree invariant regardless of the "
                    "augmentation, so the tree is fine and the in-order walk is still "
                    "sorted. What is wrong is the arithmetic `select` and `rank` rely on, "
                    "so they walk to the wrong node and return confidently. Nothing "
                    "recomputes the field on its own, which is why the lab re-checks every "
                    "size against a fresh count after rotating."},
        ],
        "mistakes": [
            ("Forgetting to reduce `i` when select goes right",
             "Going right means the left subtree and the current node have been passed "
             "over, so `i` must drop by `L + 1`. Without it the walk asks for the same "
             "rank in a smaller subtree and returns a key too far to the left. The symptom "
             "is an answer that is plausible and consistently too small, which is the "
             "hardest kind to notice."),
            ("Adding to the rank on a left turn",
             "Going left passes over nothing at all that is below the target &mdash; every "
             "key skipped is larger. Only a right turn passes keys, and it passes exactly "
             "`L + 1` of them. Adding on both turns gives the number of nodes visited "
             "rather than the rank, and the two coincide often enough on small trees to be "
             "mistaken for correct."),
            ("Treating the augmentation as free",
             "It costs a word per node, an increment along every insertion path, and a "
             "recomputation at every rotation &mdash; in the right order, the descending "
             "node before the rising one. Skip the rotation update and the field goes "
             "stale silently: the tree is correct, the queries are wrong, and no invariant "
             "in the structure is violated."),
        ],
        "standard": ("Finish when a proposed extra field prompts the question “could a node compute this from its two children?”",
                     "You should be able to run `select` and `rank` on a drawn "
                     "size-annotated tree writing the arithmetic at each node, count the "
                     "nodes a range query visits and say why it is not proportional to the "
                     "answer, state the augmentation criterion and apply it to size, sum, "
                     "min and a median, and recompute the sizes after a rotation in the "
                     "correct order."),
        "note": (
            "Every structure so far has been a container: it holds keys and answers "
            "questions about them. The last one is not. &ldquo;Union&ndash;Find&rdquo; "
            "maintains a partition of `n` elements and answers only &ldquo;are these two "
            "in the same set&rdquo; &mdash; and the two rules that make it fast are so "
            "cheap that leaving one out is the natural mistake, which the lab punishes "
            "with a tree of depth `11` on twelve elements."
        ),
    },
    # ---------------------------------------------------------------- 13
    {
        "slug": "union-find",
        "title": "Union–Find",
        "module": "Sets and choices",
        "one_line": "Run a union/find sequence under each combination of the two rules and give the rank–height proof that union by rank bounds the depth.",
        "summary": (
            "Sets as rooted trees, one root per set: `find` walks to the root and `union` "
            "links one root under another. Which way round it links is the whole "
            "difference between a depth of `1` and a depth of `11` on twelve elements. "
            "Union by rank keeps every height at most `log₂ n`, by an induction showing a "
            "tree of rank `r` has at least `2ʳ` elements; path compression flattens as it "
            "searches."
        ),
        "key": [
            "sets as rooted trees     find(x) = walk parent pointers to the root",
            "union(x, y)              link one ROOT under the other",
            "",
            "union by rank     link the shorter tree under the taller;  equal ⟹ rank + 1",
            "path compression  on the way back, point every node on the path at the root",
            "",
            "rank r ⟹ at least 2ʳ elements     ⟹  height ≤ log₂ n      proved here",
            "11 unions and 12 finds, n = 12:  66 hops with no rules,  20 with union by rank",
        ],
        "key_label": "Two rules, one proved bound, and what the sequence costs without them",
        "concepts_intro": (
            "A structure with two operations and two optional rules. The rules look like "
            "optimisations and one of them is the difference between a bound and no bound "
            "at all."
        ),
        "concepts": [
            ("A set is a rooted tree and its name is its root",
             "Each element points at a parent; a root points at itself. `find(x)` walks up "
             "and returns the root, which is the set&rsquo;s identity, so `find(x) = "
             "find(y)` is the &ldquo;same set&rdquo; test. Nothing is stored about the "
             "elements and nothing can be enumerated: this structure answers connectivity "
             "and refuses every other question, including &ldquo;what is in this set&rdquo;."),
            ("Union does not link the two roots either way",
             "Linking the taller tree under the shorter one adds a level to the whole "
             "thing; linking the shorter under the taller adds none. Do it wrong "
             "consistently and the trees become paths. The lab runs a sequence of eleven "
             "unions both ways on twelve elements: with the rule the tallest tree has "
             "depth `1`, without it, depth `11`."),
            ("The 2ʳ bound is an induction on the rule, so it fails without the rule",
             "Union by rank increases a root&rsquo;s rank only when two equal-rank trees "
             "merge, and then the merged tree has at least twice as many elements. So a "
             "rank-`r` tree has at least `2ʳ` elements, and with only `n` elements no rank "
             "exceeds `log₂ n`. Without the rule the claim is simply false, and the lab "
             "shows a depth-`11` tree holding `12` elements where `2¹¹` is `2048`."),
        ],
        "read_title": "Two operations, two rules, and the induction that bounds the height",
        "read_intro": "The structure, the rank–height proof, what path compression adds, and the one bound on this page that is stated rather than proved.",
        "body": [
            ("def", ("Disjoint-set forest",
                     "A partition of `{1, …, n}` represented as a forest: each element has "
                     "a parent pointer, each set is a tree, and the root of a tree is its "
                     "<strong>representative</strong>. `find(x)` follows parent pointers "
                     "from `x` to the root. `union(x, y)` finds both roots and, if they "
                     "differ, makes one the parent of the other.",
                     "The cost of `find` is the number of pointers walked, which is the "
                     "depth of `x`. Everything about the performance of this structure is "
                     "therefore a statement about how deep the trees get.")),
            ("p", "The naive version links the root of the first argument under the root "
                  "of the second. Run `union(0,1), union(1,2), …, union(10,11)` that way "
                  "and each union hangs the growing tree under a fresh singleton: the "
                  "result is a path of twelve nodes. The twelve finds afterwards walk "
                  "`11 + 10 + … + 0 = 66` pointers, and the deepest find walks `11`."),
            ("def", ("Union by rank",
                     "Each root carries a <strong>rank</strong>, initially `0`. On a "
                     "union, the root of smaller rank is made a child of the root of "
                     "larger rank. If the two ranks are equal, either becomes the child "
                     "and the new root&rsquo;s rank increases by `1`.",
                     "Rank is an upper bound on height and equals it when path compression "
                     "is not used. The rule is two comparisons and costs nothing, and the "
                     "next theorem is what it buys.")),
            ("thm", ("A tree of rank r has at least 2ʳ elements",
                     "Under union by rank, any root of rank `r` has at least `2ʳ` elements "
                     "in its tree. Consequently no rank exceeds `log₂ n`, and since rank "
                     "bounds height, every `find` walks at most `log₂ n` pointers.",
                     "Induction on `r`. A rank-`0` root is a singleton, and `2⁰ = 1`. A "
                     "root reaches rank `r` only by merging two roots of rank `r − 1`, "
                     "each of which has at least `2ʳ⁻¹` elements by the inductive "
                     "hypothesis; the merged tree has at least `2ʳ⁻¹ + 2ʳ⁻¹ = 2ʳ`. "
                     "Attaching a lower-rank tree does not change the root&rsquo;s rank, "
                     "so it cannot break the claim &mdash; it only adds elements. With "
                     "`n` elements in total, `2ʳ ≤ n` forces `r ≤ log₂ n`.")),
            ("p", "Every step of that induction is about the rule. It is the "
                  "&ldquo;only by merging two roots of equal rank&rdquo; clause that "
                  "supplies the doubling, and the naive union has no such clause. So the "
                  "bound is not a fact about disjoint-set forests; it is a fact about "
                  "disjoint-set forests built with union by rank, and the lab makes the "
                  "difference concrete."),
            ("math", [
                "n = 12,   union(i, i+1) for i = 0 … 10,   then find on all 12",
                "",
                "rules                        hops   worst find   tallest   2ʳ bound   holds?",
                "",
                "neither                        66           11        11       2048      no",
                "union by rank                  20            1         1          2     yes",
                "path compression only          21           11        11       2048      no",
                "both                           20            1         1          2     yes",
                "",
                "  the 2048 rows are the point:  a tree of depth 11 would need 2048",
                "  elements to satisfy the bound, and this set holds 12",
            ]),
            ("p", "Read the first row as a refutation rather than a slow result. A depth "
                  "of `11` on twelve elements is not a worse constant; it is the `2ʳ` "
                  "claim failing outright, because there is no rank rule in force to make "
                  "it true. The lab prints the bound and the set size side by side with "
                  "the verdict, and the verdict on that row is &ldquo;no&rdquo;."),
            ("h3", "Path compression"),
            ("def", ("Path compression",
                     "During `find(x)`, after the root is located, set the parent of every "
                     "node on the path from `x` directly to the root.",
                     "The walk has already visited those nodes, so the rewriting is free "
                     "up to a constant. Every subsequent `find` on any of them costs one "
                     "hop. It changes no set and no root; it only shortens the paths it "
                     "has just traversed.")),
            ("p", "On the chain sequence, compression alone brings the total from `66` "
                  "hops to `21`: the first find walks eleven pointers and flattens the "
                  "entire path, so the remaining eleven finds cost one each. The worst "
                  "single find is still `11`, because the tall tree was built before any "
                  "find happened &mdash; compression repairs, it does not prevent. And the "
                  "`2ʳ` bound still fails on that row, because it is a claim about union "
                  "by rank and compression is not that."),
            ("example", ("A sequence where the rules separate more finely",
                         "Pair up, then pair the pairs: `union(0,1), union(2,3), …` then "
                         "`union(0,2), union(4,6), …` and so on. On twelve elements the lab "
                         "reports `39` hops with neither rule and a tallest tree of depth "
                         "`4`, whose `2ʳ` bound of `16` exceeds the twelve elements "
                         "present &mdash; failing again, on a pattern that was not even "
                         "trying to be bad. With union by rank the tallest rank is `3`, "
                         "the bound is `8`, the set holds `12`, and it holds. Both rules "
                         "together bring the hops to `30`.")),
            ("h3", "What is proved here and what is only stated"),
            ("p", "With <em>both</em> rules, a sequence of `m` operations on `n` elements "
                  "costs `O(m α(n))`, where `α` is the inverse Ackermann function and is "
                  "at most `4` for every `n` that will ever be written down. That bound is "
                  "<strong>stated on this course and not proved</strong>: its proof needs "
                  "machinery no Subject in this library teaches, and the course&rsquo;s "
                  "list of what it does not cover says so too."),
            ("p", "What <em>is</em> proved here is the `log n` bound from union by rank "
                  "alone, by the induction above, and it is the bound every later course "
                  "quotes when it uses this structure &mdash; Kruskal&rsquo;s algorithm "
                  "sorts the edges and then does `union` and `find`, and the sort "
                  "dominates a logarithmic union anyway. The near-constant bound is "
                  "better and is not needed to make the structure worth using, which is "
                  "the honest reason a course can state it without developing it."),
        ],
        "lab": ("seqkit", {
            "mode": "unionfind",
            "preset": "chain",
            "panel_title": "The forest, the hops, and the bound with each rule on or off",
            "panel_intro": "Choose a union pattern and the size, then switch each rule on and "
                           "off. The forest is drawn, hops are counted for every find, and the "
                           "table reports the tallest tree, the `2ʳ` bound its rank implies, "
                           "the number of elements actually present, and whether the bound "
                           "holds. The opening preset has both rules off, so the bound fails "
                           "&mdash; which is the demonstration, not a defect.",
        }),
        "steps_title": "Running a union/find sequence",
        "steps_intro": "Run it without the rules first. The structure is only interesting once you have seen what it does when the rules are left out.",
        "steps": [
            ("Draw the forest and keep the parent pointers explicit",
             "One arrow per element, roots pointing at themselves. The set is the tree and "
             "the name of the set is the root, so &ldquo;same set&rdquo; is always two "
             "walks and a comparison."),
            ("Perform the unions without either rule, and measure the depth",
             "Link the first root under the second every time. On the chain pattern this "
             "gives a path, and the depth is one less than the number of elements. This is "
             "the baseline the rules are measured against and it is not a straw man: it is "
             "what the obvious implementation does."),
            ("Turn on union by rank and check the 2ʳ claim",
             "Link the smaller rank under the larger; on a tie, increase the new "
             "root&rsquo;s rank. Then for the tallest root, compare `2ʳ` with the number "
             "of elements in its set. The claim is that `2ʳ` is at most the set size, and "
             "with the rule off it will not be."),
            ("Add path compression and compare totals rather than worst cases",
             "Compression does not reduce the worst single find on a tree built before "
             "any find happened; it reduces the total over a sequence. Read the hop total "
             "for that, and read the worst-find column to see what it did not fix."),
        ],
        "worked": {
            "title": "Six elements, one sequence, two ways of linking",
            "intro": [
                "Small enough to draw both forests. The unions are `(0,1), (1,2), (2,3), "
                "(3,4), (4,5)` in that order, and then a find on every element."
            ],
            "lines": [
                "no rules:  link find(a)'s root under find(b)'s root",
                "",
                "  after (0,1)   0→1",
                "  after (1,2)   0→1→2",
                "  after (2,3)   0→1→2→3",
                "  after (3,4)   0→1→2→3→4",
                "  after (4,5)   0→1→2→3→4→5          a path, depth 5",
                "",
                "  finds   x:  0  1  2  3  4  5",
                "          hops 5  4  3  2  1  0        total 15,  worst 5",
                "  tallest depth 5,  2⁵ = 32 elements needed,  6 present   BOUND FAILS",
                "",
                "union by rank:",
                "",
                "  after (0,1)   0→1                   rank[1] = 1",
                "  after (1,2)   2→1  (rank 0 under rank 1)",
                "  after (2,3)   3→1",
                "  after (3,4)   4→1",
                "  after (4,5)   5→1                   depth 1 throughout",
                "",
                "  finds   hops 1 0 1 1 1 1            total 5,  worst 1",
                "  tallest rank 1,  2¹ = 2 elements needed,  6 present    BOUND HOLDS",
            ],
            "after": [
                "The only difference between the two columns is which root became the "
                "child, and the depth went from `5` to `1`. On twelve elements the lab "
                "reports the same contrast at scale: `66` hops against `20`, and a depth "
                "of `11` against `1`.",
                "Look at what the failing row actually says. A tree of depth `5` would "
                "need `32` elements for the `2ʳ` claim to hold and there are `6`. That is "
                "not a large constant or a slow case &mdash; it is the claim being false, "
                "because the claim is about union by rank and no rank rule was in force. "
                "A bound is a consequence of a rule, and removing the rule removes the "
                "bound rather than weakening it.",
                "For a faded rehearsal, run the pairing pattern on twelve elements with "
                "each of the four rule combinations. The supplied observation is that "
                "pairing is already fairly balanced, so the no-rules depth is `4` rather "
                "than `11`. Predict whether the `2ʳ` bound holds on that row before "
                "looking &mdash; the rank is `4`, the bound is `16`, and twelve elements "
                "are present &mdash; and then say which of the four rows is the one the "
                "theorem in this lesson is about.",
            ],
        },
        "quiz_title": "Rules and bounds",
        "quiz": [
            {"q": "Eleven unions chained over twelve elements, with neither rule, produce a tree of depth `11`. The `2ʳ` bound would require `2048` elements. What does that show?",
             "a": ["The bound is wrong",
                   "The bound is a consequence of union by rank, which is not in force here",
                   "Path compression is required for the bound to hold",
                   "Twelve elements is too few for the bound to apply"],
             "c": 1,
             "why": "The induction proving `2ʳ ≤ set size` uses the fact that a rank rises "
                    "only when two equal-rank trees merge &mdash; which is the rule. Take "
                    "the rule away and the doubling step has nothing to stand on, and the "
                    "conclusion fails. Path compression alone leaves the depth at `11` and "
                    "the bound still failing, and the bound is not a large-`n` statement: "
                    "it holds for every `n` when the rule is used."},
            {"q": "On the chained sequence, path compression alone brings the hop total from `66` to `21` but leaves the worst single find at `11`. Why?",
             "a": ["Because compression only works on finds, not unions",
                   "Because the tall tree was built before any find happened, so the first find still walks it",
                   "Because compression requires union by rank to be effective",
                   "Because `11` is the theoretical minimum for twelve elements"],
             "c": 1,
             "why": "Compression rewrites the path it has just walked, so the first find "
                    "pays the full depth and flattens everything behind it: the remaining "
                    "eleven finds cost one hop each. It repairs rather than prevents. "
                    "Compression is indeed only applied during a find, but that is not why "
                    "the <em>worst</em> find is `11` &mdash; the reason is the order of "
                    "events. And `11` is nothing like a minimum: union by rank gives a "
                    "worst find of `1`."},
            {"q": "Which bound for union–find does this course prove?",
             "a": ["`O(m α(n))` with both rules",
                   "`O(log n)` per operation from union by rank",
                   "`O(1)` amortised with path compression",
                   "`O(log* n)` with path compression alone"],
             "c": 1,
             "why": "The `2ʳ` induction gives rank at most `log₂ n` and therefore height at "
                    "most `log₂ n`, so every find walks `O(log n)` pointers &mdash; that is "
                    "the proof in this lesson. The near-constant `α(n)` bound with both "
                    "rules is stated and not proved here, and the course says so in its "
                    "list of what it does not cover. The other two are not results this "
                    "library states at all."},
        ],
        "mistakes": [
            ("Linking the two roots without comparing their ranks",
             "&ldquo;Make the first root a child of the second&rdquo; is the natural "
             "implementation and it builds paths: depth `11` on twelve elements in the "
             "lab. The rule is two comparisons, it costs nothing, and without it the `2ʳ` "
             "induction has no doubling step &mdash; so what is lost is the bound itself "
             "rather than a constant factor."),
            ("Expecting path compression to fix a tree that is already tall",
             "It flattens the path it has just walked, so the first find pays in full. On "
             "the chain the worst find is still `11` with compression alone, while the "
             "total drops from `66` to `21`. Compression improves a sequence and does "
             "nothing for the first operation, which is the one a latency requirement "
             "cares about."),
            ("Quoting the near-constant bound as something proved here",
             "`O(m α(n))` with both rules is stated on this course and not proved, and the "
             "course&rsquo;s own list of exclusions says so. The proved bound is `log n` "
             "from union by rank, and it is the one every later course quotes &mdash; in "
             "Kruskal&rsquo;s algorithm the edge sort dominates it anyway, so nothing "
             "downstream needs the stronger result."),
        ],
        "standard": ("Finish when “link one root under the other” sounds like an unfinished sentence.",
                     "You should be able to run a union/find sequence keeping the parent "
                     "pointers explicit, state and apply union by rank, give the `2ʳ` "
                     "induction in full, say what path compression does to a total and what "
                     "it does not do to a worst case, and separate the bound this course "
                     "proves from the one it states."),
        "note": (
            "Eight structures, each cheap at something and refusing something else. The "
            "course closes by putting them in one table: &ldquo;Choosing a "
            "Structure&rdquo; costs a stated operation mix on every structure at once and "
            "asks what the winner cannot do at all &mdash; because &ldquo;not "
            "supported&rdquo; is a column, not a slow number."
        ),
    },
    # ---------------------------------------------------------------- 14
    {
        "slug": "choosing-a-structure",
        "title": "Choosing a Structure",
        "module": "Sets and choices",
        "one_line": "Cost an operation mix on every structure at once, rank them, and name what the winner cannot answer at all.",
        "summary": (
            "The operation mix decides the structure: which operations, whether order "
            "matters, whether the set changes. The data does not decide. The instrument is "
            "a cost table with a &ldquo;not supported&rdquo; column, because the reason "
            "not to use a hash table is usually not that it is slow at predecessor "
            "&mdash; it is that it cannot answer predecessor at any speed."
        ),
        "key": [
            "                 search    insert   delete   min     predecessor   range    ordered walk",
            "sorted array     log n         n        n      1         log n     log n + k        n",
            "hash table       1 exp     1 exp    1 exp      n             —            —         —",
            "AVL tree         log n     log n    log n  log n         log n     log n + k        n",
            "binary heap          n     log n    log n      1             —            —         —",
            "union–find           —         —        —      —             —            —         —",
            "",
            "the dashes are the answer:  not supported, at any speed",
        ],
        "key_label": "Five structures, seven operations, and the column that decides most choices",
        "concepts_intro": (
            "One rule for choosing, one instrument for applying it, and one thing the "
            "instrument must record that a cost column cannot express."
        ),
        "concepts": [
            ("The mix decides, and the data does not",
             "&ldquo;What kind of data is it&rdquo; is almost always the wrong question. "
             "The questions that decide are: which operations happen and in what "
             "proportion; does anything need the keys in order; does the set change or is "
             "it built once. The same million integers want a sorted array for a read-only "
             "range workload and an AVL tree if they change, and the integers are "
             "identical."),
            ("A cost table is the instrument, and it has to include the refusals",
             "Write the operations as rows and the structures as columns and fill in the "
             "bounds this course proved. Then fill in a dash wherever the structure cannot "
             "answer the operation at all. The dashes decide more choices than the numbers "
             "do, and a table of numbers alone silently suggests that every structure can "
             "do everything at some price."),
            ("A measured total ranks structures on one mix, and only that mix",
             "The lab runs a stated mix on every representation it can execute and ranks "
             "them by counted cost. Change the proportions and the ranking changes "
             "&mdash; on a lookup-heavy mix at `n = 32` the sorted array costs `108` and "
             "the linked list `513`; change it to insert-at-one-end and remove-at-the-other "
             "and the sorted array cannot run at all while the list costs `168`."),
        ],
        "read_title": "The cost table, the refusals, and one mix ranked by execution",
        "read_intro": "The five structures this course built, the operations they refuse, and what changes when the proportions change.",
        "body": [
            ("p", "This course has built eight structures and proved a bound for each. "
                  "Putting the useful five in one table is the whole of the method, and "
                  "the table is not new information &mdash; every entry in it was proved "
                  "in one of the thirteen lessons before this one."),
            ("math", [
                "                search    insert   delete    min   predecessor   range     ordered walk",
                "",
                "sorted array     log n         n        n      1        log n    log n + k        n",
                "hash table       1 exp     1 exp    1 exp      n            —            —        —",
                "AVL tree         log n     log n    log n  log n        log n    log n + k        n",
                "binary heap          n     log n    log n      1            —            —        —",
                "union–find           —         —        —      —            —            —        —",
                "",
                "  hash table: expected, under simple uniform hashing;  Θ(n) worst case",
                "  binary heap: delete of a known position;  finding the key first costs n",
                "  union–find: same-set tests and merges only, at log n per operation",
            ]),
            ("p", "Three entries in that table deserve saying out loud. The hash "
                  "table&rsquo;s three `1`s are <em>expected</em> under an assumption "
                  "about the keys, with a `Θ(n)` worst case that no hash function removes. "
                  "The heap&rsquo;s `min` is `1` but its `search` is `n`, because it keeps "
                  "no order between siblings. And union&ndash;find&rsquo;s row is dashes "
                  "all the way across, because it is not a container at all: it answers "
                  "&ldquo;are these two together&rdquo; and holds no retrievable keys."),
            ("h3", "The refusals, which are where most choices are actually made"),
            ("p", "A hash table cannot answer <strong>predecessor</strong> "
                  "(&ldquo;the largest key below `k`&rdquo;), cannot answer a "
                  "<strong>range</strong> query, and cannot produce the keys in order "
                  "without sorting them from scratch. This is not slowness: hashing "
                  "deliberately destroys the order, which is how it gets its constant. "
                  "The dash is the right entry, and a column of numbers with a large "
                  "number in that cell would be a lie."),
            ("p", "That refusal is the in-memory form of a mistake System Design counts "
                  "in I/O. &ldquo;Hash vs Tree for Ranges&rdquo; prices a hash index and a "
                  "B-tree on a workload of nine hundred point lookups and a hundred small "
                  "ranges a second, and the hash index &mdash; which wins the point lookup "
                  "one I/O to three &mdash; loses the mix by a factor of nearly a hundred "
                  "and seventy, because its only way to answer a range is to read the "
                  "whole table. Same mistake, with a disk attached and a number on it."),
            ("h3", "One mix, executed"),
            ("p", "The lab costs a mix by running it. It ranks the five sequence "
                  "representations whose cost model it can execute &mdash; dynamic array, "
                  "sorted array, doubly-linked list, stack and queue &mdash; rather than "
                  "the five in the table above, because those are the five with a "
                  "per-operation cost model already proved on this course. The lesson it "
                  "teaches is the same one, and it is about the refusals:"),
            ("math", [
                "n = 32,  mostly lookups:  12 search, 2 index, 2 delete, 2 min",
                "",
                "  sorted array            108        cheapest; binary search",
                "  dynamic array           478        scans",
                "  doubly-linked list      513        scans, and pays to reach a position",
                "  stack                     —        cannot search, index, delete or take a min",
                "  queue                     —        the same four refusals",
                "",
                "n = 32,  insert at one end, remove at the other:  8 + 8",
                "",
                "  doubly-linked list      168        cheapest",
                "  dynamic array           440        shifts on every front insertion",
                "  sorted array              —        cannot be told where to insert",
                "  stack, queue              —        cannot delete at a position",
            ]),
            ("p", "Two mixes, and the winner changed and the refusals changed with it. "
                  "The sorted array is four to five times cheaper than anything else on "
                  "the lookup-heavy mix and cannot run the second one at all &mdash; not "
                  "slowly, at all &mdash; because an insertion at a caller-chosen position "
                  "is not an operation a sorted array has. That is the shape of a real "
                  "structure choice far more often than a factor of two on a shared "
                  "operation."),
            ("p", "And the ranking is a measurement of one mix at one size. `108` against "
                  "`513` is a fact about eighteen operations on thirty-two elements. Move "
                  "the proportions and the order changes; move `n` and the gaps change, "
                  "because `log n` and `n` diverge. The table of bounds is what "
                  "generalises, the measured ranking is what convinces, and the honest "
                  "report uses both &mdash; the bound to say what will happen and the "
                  "count to show it happening."),
        ],
        "lab": ("seqkit", {
            "mode": "workload",
            "preset": "lookup-heavy",
            "panel_title": "Set the mix, and every structure runs it",
            "panel_intro": "Set the proportions of each operation and the size. Every "
                           "representation runs the mix with a counter, the totals are ranked, "
                           "and a structure that cannot perform an operation in the mix is "
                           "reported as refusing it rather than given a large number. Change "
                           "the proportions and watch both the winner and the set of refusals "
                           "change.",
        }),
        "steps_title": "Choosing a structure from a workload",
        "steps_intro": "Four steps, and the third eliminates more candidates than the fourth ranks.",
        "steps": [
            ("Write the operation mix down as proportions",
             "&ldquo;Mostly reads&rdquo; is not a workload. Twelve searches, two indexes, "
             "two deletions and two minima at `n = 32` is. Include the operations that "
             "happen rarely: a single range query per hour still eliminates every hash "
             "table."),
            ("Ask the three questions that decide",
             "Does anything need the keys in order? Does the set change after it is "
             "built? Is any single operation on a latency deadline, as opposed to the "
             "sequence being fast on average? The first eliminates hashing, the second "
             "eliminates a sorted array, the third eliminates anything amortised."),
            ("Cross out every structure that cannot answer something in the mix",
             "This is the step that does the work. A dash is not a large number and it "
             "cannot be traded against a small one. Do this before totalling anything, "
             "because a structure that refuses one operation in the mix is not a candidate "
             "at any cost."),
            ("Total the survivors, then name what the winner cannot do",
             "Rank by counted cost on the mix. Then state, explicitly, the operations the "
             "winner refuses &mdash; because the next requirement to arrive will be one of "
             "them, and having named them is the difference between a choice and a "
             "guess."),
        ],
        "worked": {
            "title": "Three workloads, three answers",
            "intro": [
                "The same five structures against three mixes. The interesting column is "
                "the last one."
            ],
            "lines": [
                "A.  a read-only price list:  lookup by key, range scans, no changes",
                "",
                "    hash table       lookups are fastest        RANGE: not supported",
                "    sorted array     log n lookup, log n + k range,  no inserts needed",
                "    AVL tree         same as sorted array, and pays constants for",
                "                     an update ability the workload never uses",
                "    →  sorted array.  It cannot insert; the workload never asks.",
                "",
                "B.  a live index:  lookup, insert, delete, occasional range",
                "",
                "    hash table       three operations in one, RANGE: not supported",
                "    sorted array     insert and delete are n",
                "    AVL tree         log n on all four",
                "    →  AVL tree.  It cannot answer a lookup in one step; nothing else",
                "       here can do all four at all.",
                "",
                "C.  a scheduler:  insert a task, always take the most urgent",
                "",
                "    binary heap      insert log n, min 1, extract log n",
                "    AVL tree         the same bounds, larger constants, plus order",
                "                     it does not need",
                "    hash table       MIN: n.  It has no order at all.",
                "    →  binary heap.  It cannot find a task by name: SEARCH is n.",
                "",
                "measured, mix A at n = 32 in the lab's five representations:",
                "    sorted array 108,  dynamic array 478,  list 513,  stack and queue refuse",
            ],
            "after": [
                "Every one of the three answers was decided by a refusal rather than by a "
                "ratio. The hash table lost A and B because it cannot do ranges; the "
                "sorted array lost B because it cannot insert cheaply; the heap won C and "
                "the sentence naming what it cannot do &mdash; find a task by name "
                "&mdash; is the most useful line in the analysis, because that is the "
                "requirement that will arrive next.",
                "Notice what the AVL tree is in workload A: correct, general, and wrong. "
                "It answers everything the mix asks at the same asymptotic cost as the "
                "sorted array, with larger constants, in exchange for an update ability "
                "the workload never exercises. Choosing the more capable structure by "
                "default is a real cost paid for a real reason that does not apply.",
                "For a faded rehearsal, take workload D: a union-of-components problem "
                "&mdash; repeated &ldquo;are these two connected&rdquo; and &ldquo;merge "
                "these two groups&rdquo;, with no key ever retrieved. The supplied "
                "observation is that four of the five structures in the table have a dash "
                "in every column that matters, because none of them maintains a partition. "
                "Name the structure, quote its proved bound from this course, and then say "
                "what it cannot do &mdash; the list is long, and that is the point.",
            ],
        },
        "quiz_title": "Mixes and refusals",
        "quiz": [
            {"q": "A workload does a million lookups a second and one range query an hour. Which structure does the range query eliminate?",
             "a": ["the AVL tree", "the sorted array", "the hash table", "none of them: one query an hour is negligible"],
             "c": 2,
             "why": "A hash table cannot answer a range query at all &mdash; hashing "
                    "destroys the order, so its only option is to examine every key. The "
                    "frequency does not matter: an operation the structure cannot perform "
                    "is not a slow operation, and one query an hour that reads the whole "
                    "table is still a scan of the whole table. The sorted array and the "
                    "AVL tree both answer it in `log n + k`."},
            {"q": "The lab ranks a lookup-heavy mix at `n = 32` as sorted array `108`, dynamic array `478`, linked list `513`, with the stack and queue refusing four of the operations. What generalises from this?",
             "a": ["That a sorted array is about four times faster than a dynamic array",
                   "That the refusals are structural, while the ratios are facts about this mix at this size",
                   "That linked lists should not be used",
                   "That the ranking is the same at every `n`"],
             "c": 1,
             "why": "A stack cannot search at any size or any mix &mdash; that is a "
                    "property of the structure. `108` against `478` is eighteen operations "
                    "on thirty-two elements, and since the sorted array searches in "
                    "`log n` while the others scan in `n`, the ratio grows with `n` rather "
                    "than staying at four. The linked list won the other mix in this "
                    "lesson by a factor of nearly three."},
            {"q": "Why is &ldquo;not supported&rdquo; a column in the cost table rather than a large number?",
             "a": ["Because the cost would be hard to estimate",
                   "Because a refusal cannot be traded against a saving elsewhere, while a number can",
                   "Because unsupported operations are rare in practice",
                   "Because the asymptotic notation has no symbol for it"],
             "c": 1,
             "why": "A structure that costs `n` on one operation and `1` on another can be "
                    "chosen if the mix is right; a structure that cannot perform an "
                    "operation in the mix is out, whatever it saves elsewhere. Writing a "
                    "large number in that cell invites exactly the trade that is not "
                    "available. The cost is often easy to state &mdash; a hash table "
                    "answers a range by scanning, which is `n` &mdash; and that is "
                    "precisely the number that misleads."},
        ],
        "mistakes": [
            ("Believing a hash table is always the fastest map",
             "It cannot answer predecessor, cannot answer a range, and cannot produce the "
             "keys in order &mdash; not slowly, at all, because hashing destroys the order "
             "that those operations are about. Its constant-time lookup is also expected "
             "rather than worst-case. System Design&rsquo;s &ldquo;Hash vs Tree for "
             "Ranges&rdquo; is the same mistake with an I/O count attached: the hash index "
             "wins the point lookup and loses the mix by a factor of nearly a hundred and "
             "seventy."),
            ("Choosing from the data rather than from the mix",
             "&ldquo;They are integers, so use a hash table&rdquo; and &ldquo;there are a "
             "lot of them, so use a tree&rdquo; are both non-arguments. The same million "
             "integers want a sorted array if they never change and are scanned in "
             "ranges, an AVL tree if they change, a heap if only the smallest is ever "
             "wanted, and a disjoint-set forest if the question is connectivity. The data "
             "is identical in all four."),
            ("Reading a measured ranking as a general result",
             "The lab&rsquo;s `108` against `513` is one mix at one size. Change the "
             "proportions and the winner changes; change `n` and the ratios change, "
             "because the structures being compared have different growth rates. The cost "
             "table is what generalises and the measurement is what makes it concrete, and "
             "a report that offers only one of the two is either unconvincing or "
             "unjustified."),
        ],
        "standard": ("Finish when your first question about a workload is which operations it contains rather than what the data is.",
                     "You should be able to reproduce the cost table for the five structures "
                     "with the dashes in the right places, eliminate candidates on refusals "
                     "before totalling anything, rank the survivors on a stated mix, and "
                     "state in one sentence what your chosen structure cannot do at all."),
        "note": (
            "Every cost in that table was produced by running an operation sequence on the "
            "structure and counting, and every bound beside it was proved once. The next "
            "course spends them: Sorting and Selection uses the heap directly for "
            "heapsort and for merging many runs, and turns the expected-height argument "
            "left open in &ldquo;The Shape Problem and Random BSTs&rdquo; into the exact "
            "expectation `2(n+1)Hₙ − 4n` that randomised quicksort pays on every input."
        ),
    },
]
