---
format: long
lesson: induction-and-recursion/recursive-definitions
title: Recursive definitions: defining things in terms of themselves
thumb: Base, rule, and nothing else
---

@chapter Smaller copies of itself
@title text="Recursive Definitions" sub="Induction and Recursion" art=thumb
How do you define something in terms of itself without going round in circles? You give a base clause, which states some values outright. Then a recursive clause, which builds bigger objects from smaller ones.

@math heading="Sequences" items="0! = 1,   n! = n · (n−1)!@factorial;;F₀ = 0,  F₁ = 1,   Fₙ = Fₙ₋₁ + Fₙ₋₂@Fibonacci"
Here are two. For factorial, zero factorial is one, and n factorial is n times n minus one factorial. For Fibonacci, F nought is zero, F one is one, and each term is the sum of the two before.

@math heading="Sequences" items="a⁰ = 1,   aⁿ = a · aⁿ⁻¹@powers;;H₁ = 1,   Hₙ = 2Hₙ₋₁ + 1@Hanoi"
Two more. For powers, a to the zero is one, and a to the n is a times a to the n minus one. And for Hanoi, H one is one, and H n is two H n minus one, plus one.

@chapter How many base values
@art two-roots
Notice Fibonacci needs two base values. Its recursive clause reaches back two, so it needs two starting points. That number isn't a choice. With one fewer, some values would be undefined. With one more, the definition might contradict itself.

@words text="well formed" sub="every object reached in finitely many steps, one value each"
A recursive definition is well formed when every object is produced from a base in finitely many steps, and the clauses never give one object two different values.

@art runaway-chain
Here's one that fails. f of zero is one, and f of n is f of n plus one, minus one. To compute f of one you need f of two, which needs f of three, and it never reaches the base. It defines nothing. The recursive clause must move toward the base.

@chapter Recursive sets
@art even-hops
Sets work the same way. Name some elements, then give rules for building more. The even naturals: zero is in E. If n is in E, so is n plus two. And nothing else is in E.

@words text="Nothing else is in E."
That last sentence isn't optional. Without it, the definition allows any bigger set too. The whole of the naturals would satisfy the first two clauses. Only the closing sentence says what's left out.

@art nested-arcs
Strings of balanced parentheses: the empty string is well formed. If s is, so is s wrapped in a pair of parentheses. And if s and t are, so is s followed by t. That generates every balanced string, and nothing else.

@chapter Recursive structures
@art binary-tree
Binary trees are the same again. The empty tree is a binary tree. And if L and R are binary trees and v is a value, the tree with root v, left subtree L and right subtree R is one too. There's no obvious size to induct on, but there's a structure, and the next lesson proves things about it directly.

@words text="base + rule  ⟹  exactly one function"
Why is any of this legitimate? Informally: given a base value and a rule making f of n from f of n minus one, there's exactly one function that satisfies both. Existence and uniqueness both follow from induction.

@chapter The Tower of Hanoi
@art hanoi-pegs
Here's a definition that falls straight out of a puzzle. Move a stack of n discs from one peg to another, using three pegs, and never put a larger disc on a smaller one.

@math items="move n−1 discs out of the way:  Hₙ₋₁@out of the way;;move the largest disc:  1@largest disc;;move the n−1 discs back on top:  Hₙ₋₁@back on top;;Hₙ = 2Hₙ₋₁ + 1,  H₁ = 1@two H"
To move n discs, first move the top n minus one out of the way. Then move the largest disc. Then move the n minus one back on top. That's two H n minus one, plus one. And one disc takes one move.

@math heading="Unroll it" items="1, 3, 7, 15, 31, 63, …@one, three;;= 2ⁿ − 1@two to the n;;n = 64:  2⁶⁴ − 1 seconds ≈ 585 billion years@sixty four"
Unroll a few values: one, three, seven, fifteen, thirty one, sixty three. That's two to the n, minus one. With sixty four discs, at one move a second, that's about five hundred and eighty five billion years.

@chapter Where people slip
@list heading="Common slips" items="Too few base cases@too few|A recursion that doesn't decrease@doesn't decrease|Leaving out the closure sentence@closure"
Three slips. Too few base cases, which leaves later terms undefined. A recursion that doesn't decrease, which produces no values at all. And leaving out the closure sentence for a set, which leaves the set undetermined. Unroll the first few values every time. It catches an off by one right away.

@end text="Unroll a definition"
You can unroll the Hanoi definition and compare it with the closed form on Learn. That's learn dot get er done dot I O.
