"""Data Structures, lessons 6-8 -- Chapters 13 and 14.

Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 3rd ed.
(MIT Press, 2009): Chapter 13, Red-Black Trees (pp. 308-338); Chapter 14,
Augmenting Data Structures (pp. 339-355). Every quotation is copied from the
operator's copy with its printed page in the comment beside the lesson. The
trees and key sequences are written for these lessons: none of the book's
figures, examples or exercises is reproduced, and its procedures are
described in prose and named.
"""

# Lesson 6's trees, in the rbtree check view's record form: key, color,
# parent ("-" for the root). Written for the lesson.
RB_VALID = ("26, black, -; 14, red, 26; 41, black, 26; 9, black, 14; 19, black, 14; "
            "5, red, 9; 33, red, 41; 52, red, 41")
RB_RED_CHILD = RB_VALID + "; 30, red, 33"
RB_UNEQUAL = RB_VALID.replace("52, red", "52, black")
RB_RED_ROOT = ("26, red, -; 14, black, 26; 41, black, 26; 9, red, 14; 19, red, 14; "
               "33, red, 41; 52, red, 41")
RB_DISORDER = ("26, black, -; 14, red, 26; 41, black, 26; 9, black, 14; 30, black, 14; "
               "33, red, 41; 52, red, 41")

LESSONS = [
    # ---------------------------------------------------------------- 06
    # CLRS Chapter 13 opening and sections 13.1-13.2, pp. 308-315.
    # Quote: p. 308, 19 words, quotes.py OK. Lesson total: 19 words.
    # O(h) and balance (p. 308); color bit, NIL leaves, the five properties
    # (p. 308); the sentinel T.nil, black-height (p. 309); Lemma 13.1 and its
    # proof (pp. 309-310); rotations, LEFT-ROTATE, O(1), the BST property
    # preserved (pp. 312-314).
    {
        "slug": "red-black-trees",
        "title": "Red-Black Trees and Rotations",
        "module": "Chapter 13 · Red-Black Trees",
        "one_line": "A red-black tree is a search tree that spends one bit per node on a colour and obeys five rules about the colours; the rules force every root-to-leaf path to within a factor of two of every other, so the height is at most 2 lg(n + 1).",
        "summary": (
            "Sections 13.1 and 13.2 add a colour to each node of a search tree, state the five "
            "red-black properties, define black-height, and prove that a tree obeying them has "
            "height at most 2 lg(n + 1). They then give the rotation, the local restructuring "
            "that later sections use to restore the properties without breaking search-tree "
            "order. Check a tree's properties by hand, then let the lab check five trees and "
            "point to the first node where each property fails."
        ),
        "key": [
            "every node red or black; the root black",
            "every NIL leaf counts as black",
            "a red node has two black children",
            "equal black counts down every path",
            "bh(x): black nodes below x to a leaf",
            "height at most 2 lg(n + 1)",
            "a rotation keeps the inorder sequence",
        ],
        "key_label": "Sections 13.1 and 13.2 in seven lines",
        "concepts_intro": (
            "Three ideas carry the first two sections. The next lesson's insertion and deletion "
            "are written in terms of all three."
        ),
        "concepts": [
            ("The red-black properties",
             "Five rules on a search tree whose nodes are coloured: every node is red or black; "
             "the root is black; every leaf, the NIL below a node with a missing child, is "
             "black; a red node's children are both black; and from each node, every path down "
             "to a leaf passes the same number of black nodes."),
            ("Black-height",
             "For a node x, the number of black nodes on any path from x down to a leaf, not "
             "counting x and counting the NIL leaf. Property 5 is exactly the statement that "
             "this number is the same on every path, so `bh(x)` is well defined. The tree's "
             "black-height is its root's."),
            ("Rotation",
             "A local change at a node x and one child y that makes y the parent and x its child, "
             "handing y's inner subtree across to x. A left rotation lifts x's right child, a "
             "right rotation its left. It changes a constant number of pointers and keeps the "
             "inorder sequence, so the search-tree property survives."),
        ],
        "read_title": "The chapter's argument first, then the check",
        "read_intro": (
            "Read the chapter opening and sections 13.1 and 13.2 in your own copy first. The "
            "lesson sets out the properties, the lemma and the rotation in its own words, checks "
            "one tree by hand, and then lets the lab check five."
        ),
        "body": [
            ("p", "A red-black tree, the authors write in Section 13.1, constrains colours so "
                  "that &ldquo;no such path is more than twice as long as any other, so that the "
                  "tree is approximately balanced.&rdquo; The paths are the ones from the root "
                  "down to a leaf, and the claim is the chapter's whole purpose: Chapter 12 made "
                  "every operation cost the height, and this chapter keeps the height "
                  "logarithmic whatever order the keys arrive in. This lesson reads the opening "
                  "and sections 13.1 and 13.2."),
            ("p", "Section 13.1 starts with a convention. Wherever a node lacks a child, the "
                  "missing child is treated as a leaf, an external node, and the key-bearing "
                  "nodes are internal. Every internal node then has exactly two children, and "
                  "the properties can speak of leaves without exceptions. The book uses one "
                  "sentinel, `T.nil`, a black node standing for every leaf and for the root's "
                  "parent, which is the economy Section 10.2 recommended: one extra object per "
                  "tree rather than one per missing child. Drawings usually leave the leaves "
                  "out."),
            ("def", ("The five red-black properties, in the book's order",
                     "1. Each node carries one of two colours, red or black. 2. The root must be "
                     "black. 3. Each leaf, `T.nil`, is black. 4. A red node has two black "
                     "children. 5. From any node, every downward path to a leaf meets equally "
                     "many black nodes.")),
            ("p", "Properties 4 and 5 together do the work. By property 5 every path from the "
                  "root to a leaf has the same number of black nodes, the black-height; by "
                  "property 4 no two reds are adjacent, so reds can at most alternate with "
                  "blacks. The shortest possible path is all black and the longest alternates, "
                  "which is the factor of two in the quotation. The other three properties "
                  "make the count well defined: every node has a colour, the leaves are black, "
                  "and the root is black, which a fix-up can always restore by recolouring it."),
            ("thm", ("Lemma 13.1",
                     "If a red-black tree has n internal nodes, its height is at most "
                     "`2·lg(n + 1)`.")),
            ("p", "The proof has two steps. First, by induction on height, the subtree rooted at "
                  "any node x holds at least `2^bh(x) − 1` internal nodes: a leaf holds 0, and "
                  "each child of an internal node has black-height at least `bh(x) − 1`, so x's "
                  "subtree holds at least `2·(2^(bh(x) − 1) − 1) + 1` nodes, which is the claim. "
                  "Second, property 4 means black nodes make up at least half of every "
                  "root-to-leaf path, the root left out, so a tree of height h has "
                  "black-height at least h/2. Then `n ≥ 2^(h/2) − 1`, and taking logarithms gives "
                  "the bound. Search, minimum, maximum, successor and predecessor therefore run "
                  "in `O(lg n)` with no change to Chapter 12's code."),
            ("p", "Insertion and deletion are a different matter, since Chapter 12's versions can "
                  "break the properties. Section 13.2 supplies the tool for repairing them. "
                  "LEFT-ROTATE at a node x whose right child y is not `T.nil` makes y the root of "
                  "the subtree, makes x y's left child, and gives y's former left subtree to x as "
                  "its right subtree. RIGHT-ROTATE is the mirror image. Each runs in `O(1)` and "
                  "changes only pointers; the inorder sequence, and with it the search-tree "
                  "property, is untouched. The Algorithms Subject's lesson Rotations and the AVL "
                  "Invariant lets you rotate any node of a tree and watch what stays fixed."),
            ("math", [
                "a left rotation at x, with y = x's right child",
                "",
                "before:   x has left subtree α and right child y;",
                "          y has left subtree β and right subtree γ",
                "after:    y has left child x and right subtree γ;",
                "          x has left subtree α and right subtree β",
                "inorder, before and after:   α  x  β  y  γ",
            ]),
            ("p", "Now the lab, which checks a tree against all five properties and against "
                  "search-tree order. You write the tree as records, one per node: its key, its "
                  "colour, and its parent's key, or a dash for the root; a child smaller than "
                  "its parent is its left child. The tiles say whether the tree is red-black, "
                  "then each property in turn, holding or failing at the first node found, then "
                  "search-tree order, the number of nodes, the root's black-height, the height, "
                  "and the bound of Lemma 13.1. The lab's height counts the edges down to the "
                  "deepest leaf, NIL included, as the lemma's proof does, so it is one more than "
                  "Chapter 12's height of the same tree."),
            ("p", "The worked example <code>valid-eight</code> is the tree of the worked example "
                  "below: every property holds, 8 nodes, black-height 2, height 4, against the "
                  "bound `2 lg 9 ≈ 6.34`. <code>red-child</code> adds a red 30 below the red "
                  "33, and property 4 fails at 33 while property 5 still holds, since a red node "
                  "adds no black. <code>unequal-black</code> blackens 52, and property 5 fails "
                  "at 41: one black node down its left side, two down its right. "
                  "<code>red-root</code> is a tree whose only fault is its red root, the fault "
                  "RB-INSERT-FIXUP's last line repairs by recolouring. And "
                  "<code>out-of-order</code> is coloured correctly and is not a search tree: 30 "
                  "sits in 26's left subtree, which the colours cannot detect."),
            ("p", "Each verdict is about the tree on screen, and the lemma is about every tree. "
                  "No tree of 8 nodes has height below 4 in the lab's count, and the lemma says "
                  "no valid red-black tree of 8 nodes can reach 7; only its proof shows that."),
            ("h3", "Exercise"),
            ("p", "Check by hand the tree with root 20 black; 10 black and 30 red below it; 5 red "
                  "below 10; 25 and 40 black below 30; 35 and 45 red below 40. Give every node's "
                  "black-height. Then colour 40 red and 35 and 45 black, and say which property "
                  "fails, at which node, and whether the black-height changes. Type both trees "
                  "into the lab to check."),
            ("p", "Rotations restore balance, but something has to decide when to rotate and "
                  "what to recolour. The next lesson, Red-Black Insertion and Deletion, reads the "
                  "two fix-up procedures that do, and counts their work."),
        ],
        "lab": ("itakit", {
            "mode": "rbtree",
            "view": "check",
            "preset": "valid-eight",
            "panel_title": "Check a tree against the five properties",
            "panel_intro": (
                "Write one record per node: key, colour, parent (a dash for the root). The lab "
                "checks each red-black property and search-tree order, names the first node "
                "where one fails, and sets the height beside Lemma 13.1's bound. A verdict is "
                "about this tree; the lemma holds for every red-black tree."
            ),
            "presets": [
                {"id": "valid-eight", "label": "An eight-node tree, the lesson's worked example",
                 "nodes": RB_VALID,
                 "expect": {"rbiVerdict": "yes", "rbiBh": "2", "rbiHeight": "4", "rbiBound": "2 lg 9 ≈ 6.34"}},
                {"id": "red-child", "label": "The same tree with a red 30 below the red 33",
                 "nodes": RB_RED_CHILD,
                 "expect": {"rbiP4": "fails at 33: red, with red child 30", "rbiP5": "holds", "rbiNodes": "9"}},
                {"id": "unequal-black", "label": "The same tree with 52 coloured black",
                 "nodes": RB_UNEQUAL,
                 "expect": {"rbiP5": "fails at 41: 1 black node down its left side, 2 down its right", "rbiP4": "holds"}},
                {"id": "red-root", "label": "A seven-node tree with a red root",
                 "nodes": RB_RED_ROOT,
                 "expect": {"rbiVerdict": "no: property 2 fails", "rbiP2": "fails: the root 26 is red", "rbiP4": "holds"}},
                {"id": "out-of-order", "label": "A seven-node tree with 30 below 14",
                 "nodes": RB_DISORDER,
                 "expect": {"rbiBst": "fails: 30 comes before 26 in the inorder walk", "rbiP5": "holds"}},
            ],
        }),
        "steps_title": "Checking a red-black tree by hand",
        "steps_intro": "Four steps on a drawn tree, then one in the lab.",
        "steps": [
            ("Draw the leaves",
             "Hang a black NIL leaf wherever a node lacks a child. Every internal node now has "
             "two children, and properties 3 and 5 can be read off the drawing."),
            ("Check the colours locally",
             "The root must be black, and no red node may have a red child. These are "
             "properties 2 and 4, and each needs only a node and its children."),
            ("Compute black-heights from the bottom",
             "A NIL has black-height 0. For each node, add 1 to a child's black-height if the "
             "child is black; the two children must give the same number, or property 5 fails "
             "at that node."),
            ("Apply the lemma",
             "With n internal nodes, check `2^bh − 1 ≤ n` at the root and the height against "
             "`2·lg(n + 1)`."),
            ("Check a tree of your own",
             "Draw a red-black tree of nine to twelve nodes, type it into the lab, and confirm "
             "your black-height. Then recolour one node so that exactly one property fails, and "
             "predict which node the lab will name."),
        ],
        "worked": {
            "title": "Eight nodes, black-height 2",
            "intro": [
                "Root 26 black; 14 red and 41 black below it; 9 and 19 black below 14; 5 red "
                "below 9; 33 and 52 red below 41. Black-heights are computed from the leaves up.",
            ],
            "lines": [
                "5, 19, 33, 52: children NIL, bh 1",
                "9: children 5 (red, bh 1) and NIL: bh 1",
                "41: children 33 and 52, both red: bh 1",
                "14: children 9, 19, both black: bh 2",
                "26: 14 red gives 2, 41 black gives 2",
                "bh(26) = 2: at least 2² − 1 = 3 nodes",
                "longest path 26, 14, 9, 5, NIL: 4 edges",
                "bound 2·lg 9 ≈ 6.34",
            ],
            "after": [
                "Property 5 holds at every node because each node's two children give the same "
                "count; at 26 the red 14 adds nothing and the black 41 adds one, and both sides "
                "come to 2. Property 4 holds because the reds, 14, 5, 33 and 52, all have black "
                "children or NIL leaves. The longest path alternates red and black for part of "
                "its length, which is as long as the rules allow a path to be.",
            ],
        },
        "quiz_title": "Properties, black-height and the bound",
        "quiz": [
            {"q": "Take the exercise's tree and colour 40 red and its children 35 and 45 black. "
                  "Which property fails, and where?",
             "a": ["Property 4, at 30: a red node with the red child 40",
                   "Property 5, at 30: the paths through 40 now pass one more black node",
                   "Property 4, at 40: a red node with black children",
                   "No property fails; recolouring a node and its children together is always "
                   "safe"],
             "c": 0,
             "why": "30 is red and its child 40 is now red too. Property 5 still holds: below "
                    "30, the path through 25 passes 25 and a leaf, and the path through 40 "
                    "passes 35 or 45 and a leaf, two black nodes either way, so the black-height "
                    "stays 2. A red node with black children is what property 4 requires. Swapping "
                    "a node's colour with its children's preserves property 5, which is why case 1 "
                    "of the insertion fix-up does it, but it can create a red-red pair above."},
            {"q": "A red-black tree has black-height 3. What is the fewest internal nodes it can "
                  "have?",
             "a": ["7", "3", "8", "15"],
             "c": 0,
             "why": "The proof of Lemma 13.1 shows a subtree rooted at x has at least "
                    "`2^bh(x) − 1` internal nodes, here `2³ − 1 = 7`, and an all-black complete "
                    "tree of three levels attains it. Three is the black-height itself. Eight "
                    "forgets the minus one. Fifteen is a complete tree of four levels, more nodes "
                    "than a black-height of 3 requires."},
            {"q": "What does Lemma 13.1 allow as the height of a red-black tree with 15 "
                  "internal nodes?",
             "a": ["At most 8", "At most 4", "At most 15", "At most 3"],
             "c": 0,
             "why": "`2·lg(15 + 1) = 2·4 = 8`. The tree need not be that tall: a perfectly "
                    "balanced one has height 4 counted to the leaves. Four is that best case, not "
                    "the bound. Fifteen is a chain, which property 5 forbids. Three is "
                    "`⌊lg 15⌋`, the height of a complete tree counted without the leaves."},
            {"q": "A left rotation at x lifts its right child y. Which statement is true of it?",
             "a": ["It changes a constant number of pointers and leaves the inorder sequence of "
                   "keys unchanged",
                   "It restores all five red-black properties at x",
                   "It costs O(lg n), because the subtree below y must be rebalanced",
                   "It swaps the keys of x and y so that the larger key is on top"],
             "c": 0,
             "why": "LEFT-ROTATE relinks x, y and y's left subtree and their parents, a fixed "
                    "number of pointers, and the inorder sequence α x β y γ is the same before and "
                    "after. It changes no colours, so by itself it restores nothing; the fix-ups "
                    "pair it with recolourings. The subtrees below are moved whole, not rebalanced. "
                    "Keys stay in their nodes; the nodes move."},
        ],
        "mistakes": [
            ("Reading the red-black rules as making the tree perfectly balanced",
             "The rules bound the longest root-to-leaf path at twice the shortest, not at one "
             "more. The worked example's tree has paths of 3 and 4 edges to its leaves, and "
             "Lemma 13.1 allows a valid tree of 8 nodes a height of up to 6. What the rules buy "
             "is a guarantee of `O(lg n)` height for every insertion order, with a constant of "
             "2, at the price of one bit per node."),
            ("Counting black-height wrongly",
             "The book's `bh(x)` leaves x out and counts the NIL leaf. Counting x, or leaving "
             "out the leaf, gives a number one off, and Lemma 13.1's `2^bh(x) − 1` then stops "
             "matching small cases. In the worked example the root 26 has black-height 2: the "
             "path 26, 14, 9 and its leaf passes 9 and the leaf, and not 26."),
            ("Thinking the colours can stand in for the search-tree property",
             "The colours constrain shape and say nothing about key order. The lab's "
             "<code>out-of-order</code> tree satisfies all five properties and is not a search "
             "tree, because 30 sits in 26's left subtree. A red-black tree is first a binary "
             "search tree, and the five properties are added to it."),
        ],
        "standard": (
            "Finish when you can check a red-black tree and bound its height.",
            "Given a coloured tree of eight to fifteen nodes, check each property, give every "
            "node's black-height, name the first node where a property fails, and compare the "
            "height with `2·lg(n + 1)`."
        ),
        "note": (
            "The lab checks a tree you write; it does not rotate. Rotation is worked by hand "
            "here, and the Algorithms lesson named above rotates any node. Its height counts the "
            "edges to the deepest NIL leaf, one more than Chapter 12's height. Each verdict is "
            "about one tree; Lemma 13.1 is proved for all of them."
        ),
    },
    # ---------------------------------------------------------------- 07
    # CLRS sections 13.3-13.4, pp. 315-338.
    # Quote: p. 322, 19 words, quotes.py OK. Lesson total: 19 words.
    # RB-INSERT, z coloured red, the possible violations (pp. 315-316); the
    # three-part loop invariant (pp. 318-319); cases 1-3 and their mirrors
    # (pp. 319-321); O(lg n) and at most two rotations (p. 322); RB-TRANSPLANT,
    # RB-DELETE, y, y-original-color and x (pp. 323-325); why a red y is
    # harmless, the extra black (pp. 325-326); the four fix-up cases and
    # at most three rotations (pp. 326-328).
    {
        "slug": "red-black-insertion-and-deletion",
        "title": "Red-Black Insertion and Deletion",
        "module": "Chapter 13 · Red-Black Trees",
        "one_line": "An insertion adds a red leaf and repairs the one property it can break by recolouring up the tree and at most two rotations; a deletion that removes a black node pushes an extra black up the tree and settles it with at most three rotations.",
        "summary": (
            "Sections 13.3 and 13.4 make insertion and deletion keep the red-black properties. "
            "RB-INSERT colours the new node red and RB-INSERT-FIXUP removes the one possible "
            "violation by three cases; RB-DELETE tracks the node that leaves or moves and, when "
            "it was black, RB-DELETE-FIXUP moves an extra black up the tree by four cases. Both "
            "take O(lg n). Insert five keys by hand, then let the lab insert whole sequences and "
            "count every case, recolouring and rotation."
        ),
        "key": [
            "insert as in a search tree, coloured red",
            "only property 2 or 4 can then fail",
            "red uncle: recolour, move up two levels",
            "black uncle: one or two rotations, done",
            "insertion: O(lg n), at most 2 rotations",
            "deleting a red node breaks nothing",
            "a black one leaves an extra black to move",
            "deletion: O(lg n), at most 3 rotations",
        ],
        "key_label": "Sections 13.3 and 13.4 in eight lines",
        "concepts_intro": (
            "Three ideas. The uncle decides the insertion's case, the invariant proves the "
            "fix-up correct, and the extra black is how the deletion's proof keeps its accounts."
        ),
        "concepts": [
            ("Uncle",
             "The sibling of the new node's parent. When the parent is red the grandparent is "
             "black, and the uncle's colour chooses the case: red means the trouble can be "
             "recoloured away and passed upward, black means a rotation can end it here."),
            ("The fix-up's loop invariant",
             "At the start of each pass of RB-INSERT-FIXUP: the current node z is red; if z's "
             "parent is the root, it is black; and at most one property is violated, either 2 "
             "because z is the red root, or 4 because z and its parent are both red."),
            ("Extra black",
             "When RB-DELETE removes or moves a black node, the node x that takes its place is "
             "credited with one more black than its colour shows, so property 5 still counts "
             "correctly. x is then doubly black or red-and-black, and the fix-up's job is to "
             "move that extra black up until it can be discharged."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read sections 13.3 and 13.4 in your own copy first. The lesson sets out both "
            "fix-ups and their analyses in its own words, inserts five keys by hand, and then "
            "counts the cases, recolourings and rotations of longer sequences in the lab."
        ),
        "body": [
            ("p", "RB-INSERT, the authors conclude in Section 13.3, &ldquo;never performs more "
                  "than two rotations, since the while loop terminates if case 2 or case 3 is "
                  "executed.&rdquo; The recolouring may climb the whole height of the tree, but "
                  "the structural change is bounded by a constant. This lesson reads sections "
                  "13.3 and 13.4: how insertion and deletion keep the five properties, and what "
                  "each costs."),
            ("p", "RB-INSERT begins as TREE-INSERT does, with `T.nil` in place of NIL, hangs the "
                  "new node z as a leaf with two `T.nil` children, and colours it red. Red is the "
                  "safe colour. A black z would add a black node to every path through it and "
                  "break property 5 at every ancestor; a red z leaves the black counts alone, "
                  "and properties 1, 3 and 5 still hold. Only two things can go wrong: z is the "
                  "root, which breaks property 2, or z's parent is red, which breaks property 4. "
                  "RB-INSERT-FIXUP removes whichever it is."),
            ("p", "The fix-up loops while z's parent is red, and the book proves it with a loop "
                  "invariant in the three parts of Chapter 2. At the start of each pass z is "
                  "red, z's parent is black if it is the root, and the only violation is one of "
                  "the two above. Initially z is the new node, so this holds. At termination z's "
                  "parent is black, so property 4 holds, and the last line colours the root "
                  "black, which repairs property 2. Maintenance is the case analysis. Since z's "
                  "parent is red it is not the root, so the grandparent exists, and it is "
                  "black."),
            ("def", ("The three cases, with z's parent a left child",
                     "Case 1, the uncle is red: colour the parent and the uncle black and the "
                     "grandparent red, and make the grandparent the new z, two levels up. Case 2, "
                     "the uncle is black and z is a right child: left-rotate at the parent, which "
                     "turns the situation into case 3 with the roles of z and its parent swapped. "
                     "Case 3, the uncle is black and z is a left child: colour the parent black "
                     "and the grandparent red, and right-rotate at the grandparent. The loop then "
                     "ends. When the parent is a right child, the three mirror cases exchange "
                     "left and right.")),
            ("p", "Case 1 keeps property 5 because it moves one black from the grandparent down "
                  "onto both its children, so every path through the grandparent still passes "
                  "the same number of blacks; the only new risk is the red grandparent's own "
                  "parent, which the next pass handles. Cases 2 and 3 keep property 5 because "
                  "rotations change no colours and case 3's recolouring is matched by its "
                  "rotation. After case 3 the subtree's top is black, so the loop stops."),
            ("p", "The analysis follows. The descent costs `O(lg n)` because the tree's height is "
                  "`O(lg n)` by Lemma 13.1. Only case 1 repeats the loop, and each time it moves z "
                  "up two levels, so the loop runs `O(lg n)` times. Cases 2 and 3 end it, which "
                  "is the sentence quoted above: at most two rotations per insertion, whatever "
                  "the tree. In recolourings, case 1 changes three colours and case 3 two, and "
                  "the final colouring of the root changes one more when the root has turned "
                  "red."),
            ("p", "Section 13.4 is longer, because deletion can break more. RB-TRANSPLANT is "
                  "Chapter 12's TRANSPLANT with the sentinel, and RB-DELETE follows TREE-DELETE "
                  "while tracking three things: the node y that is removed or moved (z itself "
                  "when z has fewer than two children, z's successor otherwise), y's colour "
                  "before anything changed, and the node x that takes over y's old position, "
                  "possibly `T.nil`. If y was red, nothing breaks: no black count changes, no "
                  "two reds become adjacent, and y was not the root. If y was black, three "
                  "properties are at risk: 2 if a red child of y becomes the root, 4 if x and "
                  "its new parent are both red, and 5 on every path that used to pass through "
                  "y."),
            ("p", "The book repairs property 5 at once by bookkeeping: x carries an extra black, "
                  "so the counts are right, and the loop in RB-DELETE-FIXUP moves that extra "
                  "black up the tree. If x is red-and-black it is simply coloured black; if x "
                  "reaches the root the extra black is dropped. Otherwise x is a doubly black "
                  "non-root, and the cases look at x's sibling w. Case 1, w is red: recolour w "
                  "and the parent and rotate at the parent, which gives x a black sibling and "
                  "leads to one of the other cases. Case 2, w is black with two black children: "
                  "colour w red and move the extra black up to the parent. Case 3, w is black "
                  "with a red child on the near side and a black one on the far side: swap "
                  "colours and rotate at w, giving case 4. Case 4, w is black with a red child "
                  "on the far side: recolour and rotate at the parent, and the extra black is "
                  "gone."),
            ("p", "Only case 2 repeats, and it moves x up one level without rotating, so the loop "
                  "runs `O(lg n)` times. Case 1 leads into case 2, 3 or 4; a case 2 reached "
                  "from case 1 leaves x red-and-black, because the parent was red, so the loop "
                  "stops; and cases 3 and 4 end it at once. Past the climbing case 2 there are "
                  "a constant number of recolourings, and the worst path, 1 then 3 then 4, "
                  "rotates three times. RB-DELETE therefore takes `O(lg n)` with at most three "
                  "rotations. Here is one deletion by hand, from the tree the worked example "
                  "below ends with."),
            ("math", [
                "delete 10 from 20B(10B 40B(30R 50R))",
                "",
                "10 has no children: y = 10, black; x = T.nil",
                "x is doubly black; sibling w = 40, black",
                "w's far child 50 is red: case 4",
                "50 black, rotate left at 20; x = root",
                "result: 40B(20B(- 30R) 50B), bh 2",
            ]),
            ("p", "Now the lab, which runs RB-INSERT and RB-INSERT-FIXUP on the keys you type, "
                  "one at a time; it does not delete. The tiles are the tally of fix-up cases, a "
                  "prime marking a mirror case; the recolourings, counting each assignment that "
                  "changes a colour; the rotations; the most rotations in any one insertion; the "
                  "final tree, written as key and colour with the subtrees in parentheses and a "
                  "dash for a missing child; the black-height; the height to the leaves; and "
                  "Lemma 13.1's bound. The table under them gives each insertion's cases, "
                  "recolourings and rotations."),
            ("p", "The worked example <code>ascending</code> inserts 10 to 80 in increasing order: "
                  "case 1′ ×3, case 3′ ×4, 19 recolourings, 4 rotations, never more than 1 in an "
                  "insertion, and a final height of 4 against `2 lg 9 ≈ 6.34`. Chapter 12's tree "
                  "on the same order is a chain of height 7. <code>descending</code> is the "
                  "mirror image: case 1 ×3, case 3 ×4, the same 19 and 4. <code>zigzag</code>, "
                  "10 30 20 50 40 70 60, makes every other insertion from the third on bend inward: case 1′ ×2, "
                  "case 2′ ×3, case 3′ ×3, 14 recolourings and 6 rotations, 2 in each bent "
                  "insertion, the most the analysis allows. <code>spread-order</code>, ten keys "
                  "in an order that keeps the tree bushy, needs only case 1 ×2: 8 recolourings "
                  "and no rotations at all."),
            ("p", "None of those counts reached three rotations in one insertion, and the "
                  "argument above says none can. That is a claim about every tree and every key, "
                  "which no number of runs establishes; the runs show what the claim looks like "
                  "on four sequences."),
            ("h3", "Exercise"),
            ("p", "Insert `15 5 10 25 20` into an empty red-black tree by hand. For each key "
                  "name the fix-up cases, and count the recolourings and rotations. Write the "
                  "final tree in the lab's notation, then type the keys into the lab to check "
                  "your counts insertion by insertion."),
            ("p", "A red-black tree can carry more than a colour in each node. The next lesson, "
                  "Augmenting Data Structures, adds a subtree size, uses it to find the i-th "
                  "smallest key in `O(lg n)`, and asks which extra fields these fix-ups can keep "
                  "correct."),
        ],
        "lab": ("itakit", {
            "mode": "rbtree",
            "view": "insert",
            "preset": "ascending",
            "panel_title": "Insert keys and count the fix-up's work",
            "panel_intro": (
                "Type distinct keys; each is inserted by RB-INSERT and repaired by "
                "RB-INSERT-FIXUP. The cases, recolourings and rotations are counted for every "
                "insertion and in all, and the final tree is written out with its height beside "
                "Lemma 13.1's bound. The counts are about these keys; the two-rotation limit is "
                "proved for every insertion."
            ),
            "presets": [
                {"id": "ascending", "label": "Eight keys in increasing order",
                 "keys": "10 20 30 40 50 60 70 80",
                 "expect": {"rbiCases": "case 1′ ×3, case 3′ ×4", "rbiRecolor": "19", "rbiRotate": "4",
                            "rbiMostRot": "1", "rbiHeight": "4"}},
                {"id": "descending", "label": "The same keys in decreasing order",
                 "keys": "80 70 60 50 40 30 20 10",
                 "expect": {"rbiCases": "case 1 ×3, case 3 ×4", "rbiRecolor": "19", "rbiRotate": "4"}},
                {"id": "zigzag", "label": "Seven keys that bend inward in turn",
                 "keys": "10 30 20 50 40 70 60",
                 "expect": {"rbiCases": "case 1′ ×2, case 2′ ×3, case 3′ ×3", "rbiRecolor": "14",
                            "rbiRotate": "6", "rbiMostRot": "2"}},
                {"id": "spread-order", "label": "Ten keys in a bushy order",
                 "keys": "33 15 47 8 22 40 59 3 11 27",
                 "expect": {"rbiCases": "case 1 ×2", "rbiRecolor": "8", "rbiRotate": "0"}},
            ],
        }),
        "steps_title": "Running the insertion fix-up by hand",
        "steps_intro": "Four steps for each key, then one in the lab.",
        "steps": [
            ("Insert red, as in a search tree",
             "Walk down from the root, hang the key as a leaf, and colour it red. If its parent "
             "is black, or it is the root, skip to the last step."),
            ("Find the uncle",
             "Note whether the parent is a left or right child of the grandparent; the uncle is "
             "the grandparent's other child, a black NIL if missing."),
            ("Apply the case",
             "Red uncle: recolour parent, uncle and grandparent and continue from the "
             "grandparent. Black uncle, z on the inner side: rotate at the parent, then treat "
             "the old parent as z. Black uncle, z on the outer side: recolour parent and "
             "grandparent and rotate at the grandparent; stop."),
            ("Blacken the root and count",
             "Colour the root black. Record the cases, the colours that changed and the "
             "rotations; no insertion may rotate more than twice."),
            ("Run a sequence of your own",
             "Choose eight to twelve keys, predict which insertions will rotate, type them into "
             "the lab and compare its table with your predictions row by row."),
        ],
        "worked": {
            "title": "Five insertions, every case met",
            "intro": [
                "Insert `10 30 20 50 40` into an empty tree. R and B mark colours, and a prime "
                "marks a mirror case, the parent being a right child.",
            ],
            "lines": [
                "10: the root, red → black; 1 recolouring",
                "30: below black 10; nothing to do",
                "20: inner, uncle NIL black: case 2′, 3′",
                "  2 recolourings, 2 rotations: 20B(10R 30R)",
                "50: uncle 10 red: case 1′, root blackened",
                "  4 recolourings: 20B(10B 30B(- 50R))",
                "40: inner below 50: case 2′, 3′",
                "  2 and 2: 20B(10B 40B(30R 50R))",
            ],
            "after": [
                "In all, 9 recolourings and 4 rotations, and no insertion rotated more than "
                "twice. The case 1′ at 50 recoloured 30 and 10 black and 20 red, then stopped "
                "because 20 is the root, and the last line of the fix-up made it black again: "
                "four colours changed. The lab's first five rows of <code>zigzag</code> are "
                "these five insertions.",
            ],
        },
        "quiz_title": "Fix-up cases, rotations and deletion",
        "quiz": [
            {"q": "Insert `15 5 10 25 20` into an empty red-black tree. What is the final tree, "
                  "and how many recolourings and rotations were made?",
             "a": ["10B(5B 20B(15R 25R)); 9 recolourings, 4 rotations",
                   "10B(5B 20B(15R 25R)); 9 recolourings, 2 rotations",
                   "15B(5B(- 10R) 25B(20R -)); 5 recolourings, 0 rotations",
                   "10B(5R 20B(15R 25R)); 8 recolourings, 4 rotations"],
             "c": 0,
             "why": "15 becomes the black root (1). 10 is an inner child of 5: case 2 then case 3, "
                    "2 recolourings and 2 rotations, leaving 10B(5R 15R). 25 has the red uncle 5: "
                    "case 1′ and the root blackened again, 4. 20 is an inner child of 25: case 2′ "
                    "then case 3′, 2 and 2. Totals 9 and 4. Two rotations is one bent insertion, "
                    "not two. The tree with no rotations is the plain search tree of these keys, "
                    "which can be coloured legally, but RB-INSERT meets 10 below a red 5 with a "
                    "black uncle and must rotate. Leaving 5 red forgets case 1′'s recolouring."},
            {"q": "Which case of RB-INSERT-FIXUP can repeat, and what does it do to z?",
             "a": ["Case 1: it recolours and moves z up two levels, without rotating",
                   "Case 2: after its rotation the loop tests again from the old parent",
                   "Case 3: it rotates at the grandparent and moves z to the root",
                   "None: each case ends the loop after one pass"],
             "c": 0,
             "why": "Case 1 makes the grandparent red and sets z to it, and the grandparent's "
                    "parent may be red, so the loop goes on; this is why the recolouring is "
                    "`O(lg n)` while the rotations are at most two. Case 2 falls straight "
                    "through into case 3 in the same pass. Case 3 ends the loop with z's parent "
                    "black. So not every case ends the loop: case 1 does not."},
            {"q": "RB-DELETE removes a node y that was red. What must RB-DELETE-FIXUP do?",
             "a": ["Nothing; it is not called, because no black count changes, no two reds "
                   "become adjacent and the root stays black",
                   "Recolour y's replacement x black, to make up the missing red",
                   "Rotate once at y's old parent, to rebalance the shorter side",
                   "Run case 2 up the tree, to restore every black-height"],
             "c": 0,
             "why": "The book gives three reasons a red y is harmless: removing or moving it "
                    "changes no black-height, it cannot leave two reds adjacent, and a red node "
                    "was never the root. The fix-up is called only when y was black. There is no "
                    "missing red to make up, nothing to rebalance, and every black-height is "
                    "already right."},
            {"q": "Why is the new node coloured red rather than black in RB-INSERT?",
             "a": ["A red node adds no black to any path, so property 5 still holds and only "
                   "property 2 or 4 can fail",
                   "Red nodes are never rotated, so the new node stays where it was inserted",
                   "A black node could never be recoloured later",
                   "Red marks the node for deletion if the insertion fails"],
             "c": 0,
             "why": "Hanging a black node would add one black to every path through it and break "
                    "property 5 at every ancestor, a violation spread over the whole path. A red "
                    "node can only break property 2, as the root, or property 4, under a red "
                    "parent, and both are local. Red nodes are rotated freely, black ones are "
                    "recoloured freely, and colour has nothing to do with failure."},
        ],
        "mistakes": [
            ("Expecting the number of rotations to grow with the tree",
             "The recolouring of case 1 can climb `O(lg n)` levels, but cases 2 and 3 end the "
             "loop, so an insertion rotates at most twice; a deletion's fix-up rotates at most "
             "three times. In the lab no insertion of the four sequences rotates more than "
             "twice, and <code>zigzag</code> reaches two exactly. The bound comes from the case "
             "analysis, and the counts only illustrate it."),
            ("Colouring the new node black",
             "A black leaf adds a black node to every path through it, breaking property 5 at "
             "every ancestor at once. The book colours z red so that the only possible faults "
             "are property 2 at the root or property 4 below a red parent, each next to z, which "
             "is what lets three local cases repair them."),
            ("Calling the deletion fix-up whenever a node is removed",
             "RB-DELETE calls RB-DELETE-FIXUP only when the node y that left or moved was black. "
             "A red y changes no black-height, cannot make two reds adjacent and cannot have "
             "been the root. Tracking y's original colour is how the procedure knows which "
             "situation it is in."),
        ],
        "standard": (
            "Finish when you can run both fix-ups by hand and bound their work.",
            "Given a red-black tree and a key, insert it naming each case with its recolourings "
            "and rotations; given a node to delete, say whether a fix-up is needed and carry out "
            "its cases."
        ),
        "note": (
            "The lab inserts and does not delete; Section 13.4's cases are worked in prose and "
            "by hand here. Its recolourings count only assignments that change a colour, and "
            "its height counts the edges to the leaves. The counts are four sequences' and "
            "yours; the limits of two and three rotations are proved for every insertion and "
            "deletion."
        ),
    },
    # ---------------------------------------------------------------- 08
    # CLRS Chapter 14, sections 14.1-14.3, pp. 339-355 (14.3 named).
    # Quote: p. 345, 17 words, quotes.py OK. Lesson total: 17 words.
    # Augmenting textbook structures (p. 339); order-statistic trees, size,
    # OS-SELECT, OS-RANK and its invariant, maintaining sizes in insertion,
    # rotation and deletion (pp. 339-345); the four steps (p. 345);
    # Theorem 14.1 (pp. 346-347); interval trees, max, INTERVAL-SEARCH,
    # Theorem 14.2 (pp. 348-354).
    {
        "slug": "augmenting-data-structures",
        "title": "Augmenting Data Structures",
        "module": "Chapter 14 · Augmenting Data Structures",
        "one_line": "Most new structures are old ones with an extra field; a red-black tree that stores each subtree's size finds the i-th smallest key and the rank of a key in O(lg n), and any field computable from a node and its children can be kept up to date at no asymptotic cost.",
        "summary": (
            "Chapter 14 adds information to a red-black tree instead of inventing a new "
            "structure. Section 14.1 stores subtree sizes and answers select and rank queries in "
            "O(lg n); Section 14.2 states the four steps of augmenting and a theorem saying "
            "which fields come free; Section 14.3, named here, builds the interval tree. Run "
            "OS-SELECT and OS-RANK by hand, then let the lab walk a size-annotated tree and "
            "count the nodes each query visits."
        ),
        "key": [
            "store each node's subtree size",
            "x.size = left size + right size + 1",
            "select: compare i with left size + 1",
            "rank: add left size + 1 at right turns",
            "a rotation fixes two sizes in O(1)",
            "a field its children determine is free",
            "interval trees keep the max endpoint",
        ],
        "key_label": "Chapter 14 in seven lines",
        "concepts_intro": (
            "Three ideas. The first is the chapter's example, the second its method, the third "
            "the test a proposed field must pass."
        ),
        "concepts": [
            ("Order-statistic tree",
             "A red-black tree in which every node x also stores `x.size`, the number of "
             "internal nodes in its subtree, with `T.nil.size = 0`. The sizes obey "
             "`x.size = x.left.size + x.right.size + 1`, and from them the rank of any key, its "
             "position in sorted order, can be read off one path."),
            ("The four steps of augmenting",
             "Choose an underlying structure; decide what extra information to keep; check that "
             "the structure's modifying operations can keep it correct; and write the new "
             "operations that use it. The authors present the steps as a focus and a way to "
             "document the result, not as a strict sequence."),
            ("Theorem 14.1's condition",
             "A field f of a red-black tree can be maintained by insertion and deletion without "
             "raising their `O(lg n)` cost if each node's f can be computed from the node itself "
             "and its two children, their f included. Subtree size passes; a node's rank in the "
             "whole tree does not."),
        ],
        "read_title": "The chapter's argument first, then the walk",
        "read_intro": (
            "Read Chapter 14 in your own copy first. The lesson sets out the order-statistic "
            "tree, the method and the theorem in its own words, runs two queries by hand, and "
            "then counts the nodes the lab's queries visit."
        ),
        "body": [
            ("p", "&ldquo;As with any prescriptive design method, you should not blindly follow "
                  "the steps in the order given.&rdquo; The authors say it in Section 14.2 of "
                  "their own four-step method, and the chapter is in that spirit: design by "
                  "adapting a structure you already trust, with the maintenance of the new "
                  "information as the part to get right. This lesson reads Chapter 14, with "
                  "Section 14.3 named."),
            ("p", "Section 14.1 revisits Chapter 9's order statistics. Selecting the i-th "
                  "smallest of n keys took `O(n)` on an unordered set; on a dynamic set, with "
                  "insertions and deletions in between, the authors want `O(lg n)`. The device "
                  "is to store in each node the size of its subtree. A node's rank within its "
                  "own subtree is then its left child's size plus one, and the rank of a key in "
                  "the whole tree is that plus whatever lies to its left above it, ties between "
                  "equal keys being broken by inorder position."),
            ("p", "OS-SELECT finds the node of rank i in the subtree rooted at x. It computes "
                  "`r = x.left.size + 1`; if i equals r it returns x; if i is smaller it goes "
                  "left with the same i; if larger it goes right looking for rank `i − r` there, "
                  "since r keys have been passed. Each step descends a level, so the cost is "
                  "`O(lg n)`. OS-RANK goes the other way: it starts at the node, sets r to its "
                  "left size plus one, and climbs to the root, adding the left sibling's size "
                  "plus one each time it climbs from a right child. Its invariant is that r is "
                  "the node's rank within the subtree rooted where the climb has reached, so at "
                  "the root it is the rank. It also costs `O(lg n)`."),
            ("p", "Keeping the sizes right is the part the chapter calls step 3. An insertion's "
                  "first phase walks down to the new leaf, and adding one to each node passed "
                  "keeps every size correct, in `O(lg n)`. Its second phase is the fix-up, which "
                  "only recolours and rotates; recolouring leaves sizes alone, and a rotation "
                  "invalidates exactly two, the two nodes it moves. After a left rotation that "
                  "lifts y over x, y's size becomes x's old size and x's is recomputed from its "
                  "new children, in `O(1)`. At most two rotations means `O(1)` extra. Deletion "
                  "subtracts one along the path from the removed node's position to the root and "
                  "patches its at most three rotations the same way."),
            ("def", ("Augmenting, in four steps",
                     "1. Pick the structure to build on. 2. Decide what extra information it "
                     "will carry. 3. Make sure its modifying operations can keep that "
                     "information correct. 4. Write the new operations that use it. For "
                     "order-statistic trees: red-black trees; subtree sizes; insertion, deletion "
                     "and rotation patched as above; OS-SELECT and OS-RANK.")),
            ("p", "The quotation's warning is about order. Steps 2 and 4 are worth nothing if "
                  "step 3 fails, and in practice all four move forward together, with trial and "
                  "error. The authors also note the steps are a good outline for documenting an "
                  "augmented structure. Section 14.2 then generalises step 3 for red-black "
                  "trees."),
            ("thm", ("Theorem 14.1",
                     "Suppose every node of an n-node red-black tree carries a field f, and a "
                     "node's f is computable from the node itself and its two children, their f "
                     "included. Then insertion and deletion can maintain f in every node "
                     "and still run in `O(lg n)`.")),
            ("p", "The proof is that a change to one node's f can affect only the f of its "
                  "ancestors, which are `O(lg n)` in number, and each is recomputed in `O(1)` "
                  "from its children. An insertion changes the new node and its ancestors, and "
                  "each rotation two nodes and their ancestors; a deletion likewise. The test "
                  "rules some fields out at once. A node's rank in the whole tree depends on "
                  "keys far from it: insert a new smallest key and every rank changes, which is "
                  "`Θ(n)` updates. A node's depth fails too, since one rotation changes the "
                  "depth of every node in a moved subtree."),
            ("p", "Section 14.3 is named here, the theorem's second example. An interval tree "
                  "stores closed intervals in a red-black tree keyed on their low endpoints, and "
                  "each node also keeps `x.max`, the largest high endpoint in its subtree, which "
                  "is the largest of x's own high endpoint and its children's max fields, so "
                  "Theorem 14.1 applies. INTERVAL-SEARCH finds an interval overlapping a query by "
                  "walking one path: it goes left whenever the left subtree's max reaches the "
                  "query's low endpoint, and Theorem 14.2 proves that this never misses an "
                  "overlap. Each operation is `O(lg n)`."),
            ("p", "Now the lab, the one from the Algorithms Subject's lesson Augmenting a Tree, "
                  "where the queries are practised further. It builds a search tree from your "
                  "keys in the order typed, not a red-black tree, and draws each node with its "
                  "subtree size. Choose a query: select the i-th smallest, the rank of a chosen "
                  "key, or the number of keys in an interval. The tiles give the answer, whether "
                  "it agrees with a scan of the sorted keys, the nodes visited out of n, the "
                  "height, whether every stored size is correct, and whether every size is still "
                  "correct after one rotation at the root, recomputed as above. The lab's rank "
                  "walks down from the root and adds at each right turn, the same additions "
                  "OS-RANK makes climbing up."),
            ("p", "The worked example <code>select</code> builds a tree on nine keys of height 3 "
                  "and asks for the 3rd smallest: 18, agreeing with a scan, after visiting 4 of 9 "
                  "nodes. <code>rank</code> asks the rank of the 5th smallest key, 37: 5, after 3 "
                  "of 9. <code>range</code> counts the keys from 20 to 70 as the keys at most 70 "
                  "minus the keys below 20, two downward walks: 4, after 7 of 9 visits. Range "
                  "counting is not in the chapter's text, but it is one more operation the sizes "
                  "support in time proportional to the height. In all three the sizes stay "
                  "correct after the rotation, as Theorem 14.1's condition promises."),
            ("p", "Type the worked example's keys, `44 21 70 9 33 58 86 27 39 64`, choose select "
                  "and set i to 4: the answer is 33 after 3 of 10 visits. On ten keys a scan "
                  "would read up to ten; the walk reads one path. On a red-black tree the path "
                  "has length `O(lg n)` for every set of keys, and that, not one run, is the "
                  "chapter's claim."),
            ("h3", "Exercise"),
            ("p", "In the tree built from `44 21 70 9 33 58 86 27 39 64`, write every node's size. "
                  "Then run OS-RANK on the node holding 39 by climbing, writing r after each "
                  "step, and give its rank. Check it in the lab: choose the rank query and move "
                  "the slider until it reads rank of 39. The lab picks the key by its sorted "
                  "position, so the answer is no surprise; what to compare is its downward "
                  "walk, which visits 4 nodes and makes the same additions your climb made."),
            ("p", "This ends Part III. The next course, Advanced Design and Analysis Techniques, "
                  "reads Part IV: dynamic programming, greedy algorithms and amortized analysis, "
                  "beginning with rod cutting."),
        ],
        "lab": ("tree", {
            "mode": "augment",
            "preset": "select",
            "panel_title": "Answer rank queries from subtree sizes",
            "panel_intro": (
                "Type keys to build a search tree, each node annotated with its subtree size, and "
                "choose a query. The walk that answers it is drawn, its visits counted and its "
                "answer checked against a scan. The second drawing is the tree after one rotation, "
                "with every size recomputed and checked."
            ),
        }),
        "steps_title": "Order statistics by hand",
        "steps_intro": "Four steps on a drawn tree, then one in the lab.",
        "steps": [
            ("Annotate the sizes from the bottom",
             "Every leaf has size 1; every other node has its children's sizes plus one. The "
             "root's size is n."),
            ("Select by comparing with the left size",
             "At each node let r be the left child's size plus one. Stop if i equals r, go left "
             "if i is smaller, and go right with `i − r` if it is larger."),
            ("Rank by climbing",
             "Start with r equal to the node's left size plus one. Climb to the root, and each "
             "time you arrive from a right child add the parent's left size plus one."),
            ("Patch a rotation",
             "After rotating y above x, give y the old size of x and recompute x from its new "
             "children. Check that both agree with a count of their subtrees."),
            ("Query a tree of your own",
             "Type ten keys of your own into the lab, choose select, predict the walk for two "
             "values of i, and compare with the drawn path and the visit count."),
        ],
        "worked": {
            "title": "The 7th smallest of ten keys",
            "intro": [
                "Insert `44 21 70 9 33 58 86 27 39 64` into a search tree. Sizes: 44 has 10; 21 "
                "has 5, with 9 at 1 and 33 at 3 (27 and 39 at 1); 70 has 4, with 58 at 2 (64 at "
                "1) and 86 at 1. Find the key of rank 7.",
            ],
            "lines": [
                "at 44: r = 5 + 1 = 6;  7 > 6, go right",
                "  look for rank 7 − 6 = 1",
                "at 70: r = 2 + 1 = 3;  1 < 3, go left",
                "at 58: r = 0 + 1 = 1;  1 = 1, found",
                "answer 58, after 3 nodes",
                "inorder: 9 21 27 33 39 44 58 64 70 86",
            ],
            "after": [
                "The walk passed six keys at the root, the five in 44's left subtree and 44 "
                "itself, without visiting any of them, which is what the size field buys. The "
                "inorder list confirms that 58 is seventh. Choose select in the lab with these "
                "keys and i = 7: it prints 58 and 3 of 10.",
            ],
        },
        "quiz_title": "Sizes, ranks and which fields come free",
        "quiz": [
            {"q": "In the tree built from `44 21 70 9 33 58 86 27 39 64`, OS-RANK starts at 39 "
                  "and climbs to the root. What values does r take, from the start to the end?",
             "a": ["1, 3, 5, 5", "1, 2, 3, 4", "1, 3, 5, 11", "5, 5, 5, 5"],
             "c": 0,
             "why": "At 39, r is its left size plus one, 1. 39 is the right child of 33, whose "
                    "left size is 1, so r becomes 1 + 2 = 3. 33 is the right child of 21, whose "
                    "left size is 1, so r becomes 5. 21 is the left child of 44, so nothing is "
                    "added and r stays 5 at the root: 39 has rank 5. Adding one per level "
                    "ignores the left subtrees. Adding 44's left size plus one at the last step "
                    "treats a climb from a left child as if from a right one. Five throughout is "
                    "the answer without the walk."},
            {"q": "Which field can a red-black tree maintain under Theorem 14.1 without raising "
                  "the cost of insertion and deletion above `O(lg n)`?",
             "a": ["The largest key in x's subtree",
                   "x's depth below the root",
                   "x's rank among all the keys in the tree",
                   "The median key of x's subtree"],
             "c": 0,
             "why": "The largest key below x is the largest of x's key and its children's fields, "
                    "computable from x and its children, so the theorem applies. Depth changes for "
                    "every node of a subtree a rotation moves. Global rank changes for every larger "
                    "key when a new smallest key arrives. A subtree's median cannot be computed "
                    "from the two children's medians and sizes alone."},
            {"q": "A left rotation lifts y above x. Before it, x's size is 10, x's left subtree "
                  "has 5 nodes, and y's left and right subtrees have 2 and 1. What are y's and "
                  "x's sizes afterwards?",
             "a": ["y 10, x 8", "y 10, x 9", "y 4, x 8", "y 8, x 10"],
             "c": 0,
             "why": "y takes x's place at the top of the same set of nodes, so its size is x's "
                    "old size, 10. x keeps its left subtree of 5 and gains y's old left subtree "
                    "of 2, so `x.size = 5 + 2 + 1 = 8`. Nine counts y as still below x. Four is "
                    "y's old size, before the rotation. Swapping the two forgets which node is "
                    "now on top."},
            {"q": "In the same ten-key tree, what does OS-SELECT return for i = 4, and how many "
                  "nodes does it visit?",
             "a": ["33, visiting 3 nodes", "27, visiting 4 nodes", "39, visiting 4 nodes",
                   "21, visiting 2 nodes"],
             "c": 0,
             "why": "At 44, r = 6 and 4 < 6, so go left. At 21, r = 2 and 4 > 2, so go right "
                    "looking for rank 2. At 33, r = 1 + 1 = 2: found, after 44, 21 and 33. "
                    "Twenty-seven is third in sorted order, and 39 fifth. Twenty-one is second, "
                    "where the walk turns right, not where it stops."},
        ],
        "mistakes": [
            ("Storing each node's rank in the whole tree instead of its subtree size",
             "A global rank would answer rank queries in `O(1)`, but inserting a new smallest key "
             "changes the rank of every other node, which is `Θ(n)` updates. A subtree size "
             "depends only on the node's children, so an insertion changes it only along one "
             "path. That difference is Theorem 14.1's condition, and it is why the chapter "
             "stores sizes and computes ranks from them."),
            ("Forgetting that rotations change sizes",
             "The fix-ups rotate, and a rotation changes the subtrees of exactly the two nodes "
             "it moves. Their sizes must be recomputed, the lower one first, since the upper "
             "one's new size depends on it. The lab checks every size after a rotation at the "
             "root; a structure that patched only the insertion path would show a stale size "
             "there."),
            ("Following the four steps strictly in order",
             "The authors warn against it in the sentence quoted at the top. Choosing a field "
             "and writing operations for it, steps 2 and 4, is wasted if step 3 shows the field "
             "cannot be maintained, so the steps are worked together and revised. They remain a "
             "good way to organise the design and its documentation."),
        ],
        "standard": (
            "Finish when you can augment a tree and use the augmentation.",
            "Given a search tree, annotate subtree sizes, run OS-SELECT and OS-RANK by hand, "
            "patch the sizes after a rotation, and say whether a proposed field meets Theorem "
            "14.1's condition."
        ),
        "note": (
            "The lab builds a plain search tree in insertion order, not a red-black tree, so its "
            "height depends on the order you type; the queries and the size checks are the same. "
            "It has no interval tree. Its visit counts are for one tree; the `O(lg n)` bounds need "
            "the red-black height of Chapter 13."
        ),
    },
]
