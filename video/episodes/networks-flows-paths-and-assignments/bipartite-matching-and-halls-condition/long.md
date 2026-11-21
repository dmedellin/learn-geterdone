---
format: long
lesson: networks-flows-paths-and-assignments/bipartite-matching-and-halls-condition
title: Hall's condition: the minimum cut names who can't be placed
thumb: Too few jobs between them
---

@chapter The question
@title text="Bipartite Matching and Hall's Condition" sub="Networks, Flows, Paths and Assignments" art=thumb
You have applicants and jobs, and each applicant will take only certain jobs. Can everyone be placed? And if not, can you prove it to someone in one sentence?

@art bipartite-graph
A matching is a set of edges where no two share a vertex. You want one that places every applicant. For any group of applicants, look at the set of jobs at least one of them will take. That's their neighbourhood.

@math heading="Hall's condition" items="|N(S)| ≥ |S|@at least as many;;for every S ⊆ X@every group"
Hall's condition says every group has at least as many jobs between them as it has members. And this has to hold for every group of applicants. Hall's theorem says a full matching exists exactly when it does.

@chapter A matching is a flow
@art flow-reduction
Here's the trick. Add a source with an arc of capacity one to each applicant. Keep every edge, at capacity one. Add an arc of capacity one from each job to a sink. A flow of value k is now a matching of size k. With three applicants and two jobs, that network has seven nodes and eleven arcs.

@words text="Half an applicant is impossible" sub="the same unimodular matrix as before"
And the flow comes out whole, for the reason this course already proved. The constraint matrix is a network matrix, so it's totally unimodular. Half an applicant is ruled out by the matrix, not by the algorithm.

@chapter When it falls short
@math heading="Three applicants, two jobs" items="maximum matching 2 of 3@two of three;;S = {1, 2, 3},  N(S) = {a, b}@all three;;|N(S)| − |S| = −1@minus one"
Three applicants, each willing to take either of two jobs. The maximum matching is two of three, and the minimum cut has capacity two. The applicants on the source side of that cut are all three, and their jobs are a and b. Two minus three is minus one. Hall fails.

@words text="Both jobs filled, one applicant left out"
Both jobs are filled, and someone is still left out. That's not a contradiction. Placing three applicants would need three different jobs, and there are only two. Filling every job and placing every applicant are different conditions, so say which side you mean.

@chapter The deficient set
@art deficient-set
The failing group need not be everyone. Take applicants one, two and three, who all want only job a, and applicant four, who has jobs b, c and d. The maximum matching has two edges out of four.

@math heading="The cut names it" items="S = {1, 2, 3}@one, two and three;;N(S) = {a}@just job a;;shortfall 2@short by two"
The minimum cut names the group: one, two and three, with just job a between them. They're short by two. Applicant four isn't part of it at all. Anyone can check that claim by counting. No algorithm, no trust.

@art ring-graph
And when nothing is deficient, there's nothing to produce. Four applicants in a ring with four jobs: the matching places all four, and the minimum cut is the source alone. Remove one edge, and a certificate appears.

@chapter Three readings of one fact
@art min-cut-names
Koenig's theorem says the smallest vertex cover in a bipartite graph has as many vertices as the largest matching. That's the cover the Hungarian method counted with its lines. In the second example the cover is applicant four with job a. Max flow, Hall, and Koenig are one fact read three ways.

@art odd-cycle
One limit, stated plainly. All of this is about bipartite graphs. In a general graph, matching needs a different theory. The obstruction is the odd cycle, the same one that broke total unimodularity.

@chapter Where people slip
@list heading="Common slips" items="Expecting the deficient set to be everyone@The first|Filling every job is not placing everyone@The second|Carrying it over to general graphs@And the third"
The first slip is expecting the deficient set to be all the applicants. The second is reading a matching that fills every job as one that places everyone. And the third is carrying the theorem over to general graphs.

@chapter Try it
@words text="1-a, 2-a, 3-a, 4-b, 4-c, 4-d" sub="add one edge: 2-b"
Your turn. Take the second example and add one edge, from applicant two to job b. Find the largest matching now, then find a group whose jobs between them are still too few, and check it by counting.

@end text="Find the deficient set"
You can build a bipartite graph and let the minimum cut name the deficient set, on Learn. That's learn dot get er done dot I O.
