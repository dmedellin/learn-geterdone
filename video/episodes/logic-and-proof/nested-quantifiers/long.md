---
format: long
lesson: logic-and-proof/nested-quantifiers
title: Nested quantifiers: why the order of for all and there exists matters
thumb: Everybody has somebody
---

@chapter The question
@title text="Nested Quantifiers" sub="Logic and Proof" art=thumb
Everybody has somebody. Somebody is everybody's. Same words, nearly. Completely different claims. When quantifiers stack up, their order decides the meaning, and mixing it up is the most common invalid proof in the whole course.

@chapter Each x gets its own y
@art own-keys
Take for all x, there exists y, P of x and y. You read it left to right. For each x, there's some y. And that y is chosen after x is known, so it may be a different y for each x. That dependence is the whole content.

@art master-key
Now flip it. There exists y, for all x, P of x and y. That asks for one single y that works with every x at once. It's a much stronger claim.

@chapter The one implication
@math heading="∃y ∀x P(x, y)  ⟹  ∀x ∃y P(x, y)" items="let b be the y that works for every x@let b;;then P(x, b) holds for every x@holds for every x;;so b witnesses ∃y P(x, y) for any x@witnesses"
One direction always works. Suppose some y works for every x, and let b be that y. Then P of x and b holds for every x. So given any x, the value b witnesses that some y works. Hence for all x, there exists y.

@art endless-ladder
The converse fails. Take the integers, and P of x and y as y is greater than x. Every integer has something larger, so for all x, there exists y, holds. But no single integer is larger than every integer, so there exists y, for all x, is false.

@chapter A worked pair
@math heading="Domain ℤ,  P(x, y): x + y = 0" items="∀x ∃y (x + y = 0)  TRUE:  take y = −x@take y equals minus x;;∃y ∀x (x + y = 0)  FALSE@a single y;;x = 0 forces y = 0,  then x = 1 gives 1 + 0 = 1 ≠ 0@x equals zero"
Now x plus y equals zero, over the integers. For all x, there exists y, is true: given x, take y equals minus x. The witness depends on x, which is allowed. But a single y for every x is false. X equals zero forces y equals zero, and then x equals one gives one plus zero, which is one, not zero.

@words text="witness y = −x mentions x" sub="that is a ∀∃ proof, never an ∃∀ proof"
Notice that the witness, minus x, mentions x. That's the signature of a for all, there exists proof. If your proof of a there exists, for all statement produces a witness that mentions the universal variable, the proof is wrong.

@chapter Six claims, and two mirror pairs
@list heading="Two variables, six claims" items="∀x ∀y: every pair@every pair|∀x ∃y and ∃y ∀x@the first mirror|∀y ∃x and ∃x ∀y@the other|∃x ∃y: some pair@some pair"
With one two place predicate there are eight orderings, but quantifiers of the same kind commute. For all x for all y is the same as for all y for all x. So six claims remain: every pair, the first mirror pair, the other mirror pair, and some pair.

@art full-column
On a grid, there exists y for all x is a full column, and there exists x for all y is a full row. A grid can have either without the other. So keep each one paired with the for all, there exists that shares its variables.

@chapter Reading longer strings
@art dependency-arrows
Three or more quantifiers behave the same way. Read them in the order written. Each variable may depend on those bound to its left, and on no others. In for all x, there exists y, for all z, the y may depend on x only.

@words text="continuous: ∀ε ∀x ∃δ  ·  uniformly continuous: ∀ε ∃δ ∀x"
The same swap shows up in analysis. Continuity at every point lets delta depend on both epsilon and x. Uniform continuity asks for one delta that works at every point. The entire difference is where the there exists delta sits.

@chapter Where people slip
@list heading="Common slips" items="Swapping ∀ and ∃ to simplify@The first|An x-dependent witness for ∃∀@The second|Trusting English word order@the third"
The first slip is swapping for all and there exists while simplifying. That's not a simplification, it's a different claim. The second is giving a witness that depends on x for a there exists, for all claim. And the third is trusting English word order. There is a key for every door is genuinely ambiguous.

@chapter Try it
@art diagonal-grid
Your turn. On a small grid, build a relation where for all x there exists y holds, but there exists y for all x fails. The diagonal does it: every x is paired with itself, but no single y equals everything. Then try the successor relation on one to four, and say which x is left without a y.

@end text="Build the separating case"
You can build the grid that separates the two orders yourself, on Learn. That's learn dot get er done dot I O.
