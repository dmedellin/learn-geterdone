---
format: long
lesson: induction-and-recursion/structural-induction
title: Structural induction: proving things about trees, strings and formulas
thumb: One case per rule
---

@chapter Induction without a number
@title text="Structural Induction" sub="Induction and Recursion" art=thumb
Ordinary induction runs on a number, n. But how do you prove something about every binary tree, or every logical formula? There's no obvious n to count with.

@art build-steps
What these objects do have is a recipe. They're defined recursively: some base objects, plus rules for building bigger ones from parts. Structural induction follows that recipe instead of a number.

@list heading="Structural induction" items="Prove P for every base object@base object|Show each rule preserves P@each recursive"
To prove P for every member of the set, prove it for each base object. Then show that each recursive rule preserves it: if P holds for the parts, it holds for the object built from them.

@words text="every object is built in finitely many steps"
Why is that valid? Every member is built in finitely many steps. So you can secretly induct on the number of steps. At zero steps it's a base object, and every later step applies a rule to objects built in fewer steps.

@chapter Balanced parentheses
@math heading="Well-formed strings" items="the empty string@empty string;;if s is, so is (s)@wrapped;;if s and t are, so is st@followed by"
Recall the definition of well-formed parenthesis strings. The empty string is well formed. If s is, so is s wrapped in parentheses. And if s and t are, so is s followed by t.

@math heading="Equally many ( and )" items="empty:  0 of each@zero of each;;(s):  m + 1 of each@m plus one;;st:  m + p of each@m plus p"
Claim: every well-formed string has equally many left and right parentheses. The empty string has zero of each. If s has m of each, wrapping it gives m plus one of each. And if s has m and t has p, then s followed by t has m plus p of each.

@art balance-scale
Three parts, matching the three clauses. Forget one, say concatenation, and a whole family of strings goes unproved. That omission is invisible unless you keep the definition beside the proof.

@chapter Trees: height and size
@math heading="Binary trees" items="h(empty) = −1,   h(node) = 1 + max(h(L), h(R))@height;;n(empty) = 0,   n(node) = 1 + n(L) + n(R)@count"
For binary trees, define height: the empty tree has height minus one, and a node's height is one more than the taller of its subtrees. And count nodes: the empty tree has zero, and a node has one plus the nodes in each subtree.

@art height-levels
Claim: a tree of height h has at most two to the h plus one, minus one nodes. Base: the empty tree has height minus one and no nodes, and two to the zero minus one is zero.

@math items="h(L), h(R) ≤ h − 1@at most h minus one;;n(T) = 1 + n(L) + n(R)@one plus;;≤ 1 + (2ʰ − 1) + (2ʰ − 1)@bound for each;;= 2ʰ⁺¹ − 1@two to the h plus one"
For the step, take a tree with height h, and subtrees L and R. Both have height at most h minus one. The tree has one plus the nodes of L plus the nodes of R. Use the bound for each, and you get two times two to the h, minus one, which is two to the h plus one, minus one.

@art tree-two-parts
Both subtrees needed the hypothesis. That's structural induction with two recursive parts, the same reason a two term recurrence called for strong induction.

@chapter Formulas
@art formula-tree
Logical formulas are recursive too. A variable is a formula. If A is a formula, so is not A. And if A and B are, so is A and B in brackets, and the same for the other connectives. Base: a variable has no brackets. Negation adds none. Each binary rule adds one of each. So every formula's brackets match.

@chapter Where people slip
@list heading="Common slips" items="Leaving out a clause@leaving out|Using the hypothesis for only one part@only one|Assuming there are no other members@no other members"
Three slips. Leaving out a clause, usually concatenation for strings or the second subtree for trees. Using the hypothesis for only one part, when a binary rule gives you two. And assuming the set has no other members. That's the definition's closure sentence, and if the definition leaves it out, the proof can't supply it.

@chapter Try it
@art full-tree
To practise: a binary tree is full when every node has zero or two children. A single node is full, and a new root over two full trees is full. Prove every full binary tree has an odd number of nodes.

@math items="base:  1 node, odd@single node;;step:  1 + n(L) + n(R)@one plus;;odd + odd = even,  1 + even = odd@odd plus odd"
The base, a single node, has one node, which is odd. For the step, assume L and R both have an odd number of nodes. The new tree has one plus both. Odd plus odd is even, and one plus even is odd.

@end text="Two parts, two base cases"
On Learn, you can see Fibonacci as the numeric shadow of a two part structure. That's learn dot get er done dot I O.
