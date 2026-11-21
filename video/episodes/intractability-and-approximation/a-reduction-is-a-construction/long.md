---
format: long
lesson: intractability-and-approximation/a-reduction-is-a-construction
title: SAT to independent set: a reduction you can actually build
thumb: Triangles and contradiction edges
---

@chapter An arrow isn't a reduction
@title text="A Reduction Is a Construction" sub="Intractability and Approximation" art=thumb
Satisfiability reduces to independent set. You can repeat that sentence without being able to use it. A reduction is a construction, and once you build one, you can ask what it does to the solutions.

@math heading="A ≤ₚ B" items="f computable in polynomial time@polynomial time;;x ∈ A  ⟺  f(x) ∈ B@exactly when"
A reduces to B when there's a polynomial time map f from instances of A to instances of B, where x is a yes instance exactly when f of x is. An algorithm for B then gives one for A.

@art arrow-direction
So hardness travels from A to B, and tractability travels the other way.

@art independent-set
An independent set in a graph is a set of vertices with no edge between any two of them. The decision problem gives a graph and a number k, and asks if there's one of size k.

@chapter The construction
@list heading="Building the graph" items="One vertex per literal occurrence@One vertex|A triangle on each clause@a triangle|An edge between every x and every ¬x@x to every|Target k = number of clauses@the target"
Here's the construction. One vertex for each literal occurrence, not each literal. Join the vertices of each clause in a triangle. Join every occurrence of x to every occurrence of not x. And set the target k to the number of clauses.

@art clause-triangles
The triangle means you can pick at most one literal per clause. The contradiction edges mean you can never pick a literal and its negation. So an independent set of size m picks exactly one literal from each of the m clauses, consistently. That's an assignment.

@chapter Both directions
@art both-directions
Why does that work?

@words text="satisfiable  ⟺  independent set of size m"
Both directions matter. If the formula's satisfiable, pick one true literal per clause, and those vertices are independent. If there's an independent set of size m, set each chosen literal true. That's consistent, and satisfies every clause.

@words text="only one direction allows every no to become a yes"
The second half is the one people skip. With only the first, a construction could turn every no instance into a yes, and be useless. The lab checks both directions on every solution.

@chapter Two clauses, built
@math heading="(x₁ ∨ x₂ ∨ ¬x₃) ∧ (¬x₁ ∨ x₂ ∨ x₃)" items="6 vertices, 8 edges, k = 2@six vertices;;15 pairs − 8 edges = 7 independent pairs@fifteen pairs;;7 independent sets  vs  6 satisfying assignments@seven independent sets"
Two clauses, three variables. The construction gives six vertices and eight edges: two triangles, plus x one to not x one, and not x three to x three. Fifteen pairs of vertices, eight joined, so seven independent sets of size two, against six satisfying assignments.

@chapter What the map does
@list heading="Three questions about the map back" items="Sound: every set maps to a model@Sound|Not injective: three sets land on one model@not injective|Not onto: x₁ = x₂ = x₃ = T is hit by nothing@not onto"
The counts don't have to match. What the reduction promises is that one list is empty exactly when the other is. Map each set back to an assignment. It's sound: every set gives a model. It's not injective: three sets land on one assignment. And it's not onto.

@art many-to-one
That's three separate questions, and one word couldn't carry the answers. A reduction preserves the answer, yes or no. It doesn't promise the solution sets correspond one for one. That's a stronger property some reductions have, and this one doesn't.

@chapter The assignment nothing reaches
@art unreachable
All three true is a model. But a set here has two members, so at most two variables are named, and the map leaves the rest false. All true can't be the image of anything.

@art independent-set
And yet building forward from all true works: it picks x one, then x two, and that set reads back as true, true, false. The round trip isn't the identity.

@words text="proved: the answers agree" sub="measured: 3-to-1 somewhere, one model missed"
That's the first place on this course where a measured fact and a proved claim point different ways. The proof says the two yes or no answers agree, for every formula. The panel says that on this formula, the map is three to one somewhere and misses one assignment. Neither is evidence about the other.

@chapter Where people slip
@list heading="Common slips" items="Writing bijection over an arrow@The first|Proving only the map back@The second|Counting literals instead of occurrences@And the third"
The first slip is writing bijection over an arrow. Some reductions have one, and this one doesn't. The second is proving only that a solution maps back. And the third is merging repeated literals into one vertex, which breaks the triangle and the target.

@end text="Build it, then check the map"
Build the graph and carry every set back to the formula, on Learn. That's learn dot get er done dot I O.
