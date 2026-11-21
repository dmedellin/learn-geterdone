---
format: long
lesson: intractability-and-approximation/one-structure-three-problems
title: Independent set, vertex cover, clique: one problem, three names
thumb: Three names, one structure
---

@chapter Three problems
@title text="One Structure, Three Problems" sub="Intractability and Approximation" art=thumb
Independent set, vertex cover and clique look like three different problems. They're the same question written three ways, and the translation holds on every subset of the vertices, not just at the best one.

@list heading="Definitions" items="Independent set: no two joined@An independent set|Vertex cover: touches every edge@A vertex cover|Clique: every two joined@A clique"
An independent set is a set of vertices with no two joined. A vertex cover is a set of vertices touching every edge. A clique is a set where every two are joined. Call the largest independent set's size alpha, and the smallest cover's size tau.

@chapter Complement the set
@art set-complement
Take any set S, and look at everything else, V minus S. If S is independent, no edge has both ends in S, so every edge has an end outside it. So V minus S touches every edge. It's a cover. And the argument runs backwards just as easily.

@words text="S independent  ⟺  V − S is a vertex cover"
So S is independent exactly when V minus S is a vertex cover. That's the definition, read twice, and it's why the equivalence holds subset by subset rather than only at the extremes.

@chapter Complement the graph
@art graph-complement
Now complement the graph instead. Join exactly the pairs that weren't joined. If no pair in S was joined before, every pair in S is joined now. So S is independent in G exactly when it's a clique in the complement of G.

@words text="two different complements" sub="the set, and the graph"
Notice there are two different complements here. One complements the set, and gives a cover in the same graph. The other complements the graph, and gives a clique on the same vertices. Mixing them up produces statements that look like the theorem and are false.

@chapter Gallai's identity
@math heading="α + τ = n" items="largest independent S  ⟹  τ ≤ n − α@largest independent;;smallest cover C  ⟹  α ≥ n − τ@smallest cover;;so α + τ = n@alpha plus tau"
From the first equivalence comes Gallai's identity. The complement of a largest independent set is a cover, so tau is at most n minus alpha. The complement of a smallest cover is independent, so alpha is at least n minus tau. Together, alpha plus tau equals n.

@chapter The five-cycle
@art five-cycle
The lab loads the cycle on five vertices and checks every one of its thirty two subsets. Eleven are independent sets, eleven are vertex covers, and eleven are cliques in the complement. Alpha is two, tau is three, and they add to five.

@art subset-grid
The equal counts are a useful check, since a mismatch anywhere would separate them. Eleven isn't a round number, either. It's whatever the graph gives, and all three sides give it.

@words text="32 subsets checked, not just the optimum"
Gallai's identity compares two numbers on one pair of sets. That's the weakest test of the claim. The panel instead asks, for each subset, whether the three verdicts agree. Equal totals alone could hide disagreements that cancel.

@art self-complement
And here's a neat fact. Join the pairs the five cycle leaves out, one three, one four, two four, two five, three five. That's another five cycle. So this graph is its own complement, and its largest clique there has two vertices, matching alpha.

@chapter Exact, not approximate
@words text="hardness transfers · approximation doesn't"
So anything hard for one of the three is hard for all three, with no new gadget, and so is any polynomial algorithm. But approximation doesn't transfer. The identity is a subtraction, and subtraction doesn't preserve ratios. 

@art ratio-break
Vertex cover has a two approximation. Maximum independent set has no constant factor approximation at all, unless P equals N P. A cover within a factor of two of the smallest says nothing useful about the largest independent set. The identity transfers exact answers perfectly, and approximate answers not at all.

@chapter Where people slip
@list heading="Common slips" items="Confusing the two complements@The first|Pushing an approximation through@The second|Reading 11 = 11 = 11 as the theorem@And the third"
The first slip is confusing the two complements. The second is pushing an approximation through the identity. And the third is reading eleven, eleven, eleven as the theorem. It's a consequence. The theorem is that the verdicts agree, subset by subset.

@end text="Three names, one structure"
Click through all thirty two subsets of the five cycle on Learn. That's learn dot get er done dot I O.
