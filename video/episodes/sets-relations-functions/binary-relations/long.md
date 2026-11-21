---
format: long
lesson: sets-relations-functions/binary-relations
title: Binary relations: a set of pairs, and nothing more
thumb: Just a set of pairs
---

@chapter The question
@title text="Binary Relations" sub="Sets, Relations and Functions" art=thumb
Less than. Divides. Is a friend of. Is the parent of. They all relate one thing to another. What do they have in common, mathematically? Something almost disappointingly simple.

@art pair-cloud
A relation from A to B is just a subset of A cross B. A set of ordered pairs. A relation on A is a subset of A cross A. And when a, b is in R, we write a R b, and say a is related to b.

@math heading="Binary relation" items="R ⊆ A × B@a subset of;;a R b  means  (a, b) ∈ R@we write"
So R is a subset of A cross B, and we write a R b when the pair a, b is in R. There's no condition at all. Any set of pairs is a relation, which is why properties matter more than names.

@chapter Everything counts
@words text="∅ and A × A" sub="nothing related · everything related"
The definition permits everything. The empty set is a relation, where nothing is related. A cross A is a relation, where everything is related to everything.

@math items="2^(n²) relations on n elements@two to the n squared;;n = 3:  2⁹ = 512@three element set;;n = 5:  over 33 million@five element"
And between those there are two to the n squared relations on an n element set. On a three element set there are nine pairs, so two to the nine, five hundred and twelve relations. On a five element set, over thirty three million.

@chapter Three presentations
@list heading="One relation, three pictures" items="Pairs: {(1,2), (2,3), (3,1)}@as pairs|Matrix: 1 in row a, column b@as a matrix|Directed graph: an arrow a → b@as a directed graph"
You can present a relation three ways. As pairs: one, two, then two, three, then three, one. That's complete, and unreadable beyond a handful. As a matrix: a grid with a one in row a, column b whenever a is related to b. Or as a directed graph, with a dot per element and an arrow from a to b.

@art bool-matrix
The matrix makes some properties a single glance. Reflexive means a full diagonal. Symmetric means the matrix equals its own transpose.

@art digraph
The directed graph makes paths visible, which is how you'll read transitivity later. All three carry identical information. Each one makes different things obvious.

@chapter Inverse and composition
@art reverse-arrows
The inverse of R reverses every pair. As a matrix, it's the transpose. Don't confuse it with the complement, which takes the pairs that are not in R. They're unrelated operations.

@art two-step
Composition chains two relations. S after R contains a, c whenever there's some b with a R b, and b S c. Read it right to left: apply R first, then S. That matches function composition, where g after f means g of f of x.

@math heading="R = {(1,2), (2,3)},  S = {(2,1), (3,3)}" items="S ∘ R = {(1,1), (2,3)}@S after R;;R ∘ S = {(2,2)}@R after S"
Take R as one, two and two, three, and S as two, one and three, three. S after R: from one, R reaches two, and S takes two to one. From two, R reaches three, and S keeps three. So S after R is one, one and two, three. But R after S is just two, two. Order matters.

@chapter Composing with itself
@math heading="R = {(1,2), (2,3), (3,4)} on {1,2,3,4}" items="R ∘ R = {(1,3), (2,4)}@two steps;;R³ = {(1,4)}@three steps;;R⁴ = ∅@four steps"
Now the successor relation on one to four. Two steps: one goes to two to three, and two goes to three to four. Three has nowhere to go after four. So R after R is one, three and two, four. Three steps gives one, four. And four steps gives nothing, because a four element chain has no path that long.

@art successor-chain
Put all the powers together and you get every pair a, b with a less than b. That's the transitive closure of the successor relation, computed by hand.

@chapter Where people slip
@list heading="Common slips" items="Composing in the wrong order@The first|Assuming a relation must be meaningful@The second|Confusing R⁻¹ with a complement@the third"
The first slip is composing in the wrong order. S after R applies R first, and getting it backwards is silent. The second is assuming a relation has to mean something. Any set of pairs qualifies. And the third is confusing the inverse with the complement.

@chapter Try it
@words text="R = {(1,1), (1,2), (2,3), (3,1)}" sub="on {1, 2, 3}"
Your turn. Take this relation on one, two, three. Write its matrix, sketch its directed graph, and compute R after R in whichever is easiest. Then check the answer in a second presentation.

@end text="A relation as a matrix"
You can click a relation into a matrix and watch its closure fill in, on Learn. That's learn dot get er done dot I O.
