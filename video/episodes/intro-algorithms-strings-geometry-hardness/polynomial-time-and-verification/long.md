---
format: long
lesson: intro-algorithms-strings-geometry-hardness/polynomial-time-and-verification
title: P and NP: deciding versus checking a certificate
thumb: Easy to check, hard to find?
---

@chapter Problems that look alike
@title text="Polynomial Time and Verification" sub="Introduction to Algorithms, Sections 34.1–34.2" art=thumb
Chapter thirty four opens with pairs of problems that look alike, and aren't.

@list heading="Twins, one easy and one not" items="shortest vs longest simple path@shortest|Euler tour vs hamiltonian cycle@Euler|2-CNF vs 3-CNF satisfiability@two CNF"
Shortest and longest simple paths. Euler tours and hamiltonian cycles. Two CNF and three CNF satisfiability. In each pair, the first has a polynomial time algorithm, and the second is NP complete. No one has found a polynomial time algorithm for an NP complete problem, and no one has proved there isn't one.

@chapter Polynomial time, made exact
@words text="Shortest path → path of at most k edges?" sub="optimization becomes a decision"
The chapter works with decision problems, whose answer is yes or no. An optimization problem becomes one by adding a bound. Not the shortest path, but whether there's a path of at most k edges.

@art encoding
An algorithm sees an instance only as a binary string, and the encoding matters. An algorithm that runs in time proportional to an integer k is linear if k is written in unary, and exponential if k is written in binary, since binary k takes only about log k bits. So unary is ruled out.

@words text="P" sub="languages decided in polynomial time"
With encodings fixed, a decision problem is a language: the set of strings whose answer is yes. P is the class of languages decided in polynomial time. Polynomials compose, add and multiply, and agree across the usual models of computation. That's the case for drawing the line there.

@chapter Certificates
@quote text="If we were somehow given a “certificate” of a solution, then we could verify that the certificate is correct in time polynomial in the size of the input to the problem." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 34"
Here's how the chapter first describes NP. If we were somehow given a certificate of a solution, then we could verify that the certificate is correct in time polynomial in the size of the input to the problem.

@art hamiltonian-check
Take the hamiltonian cycle problem. Trying every ordering of the vertices takes exponential time. But if someone hands you an ordering, checking it is quick: is it a permutation of the vertices, and is every consecutive pair, last and first included, an edge?

@art certificate-slip
The certificate carries the hard part. The verifier only has to read it, and check, in time polynomial in the input.

@math heading="NP" items="verifier A(x, y): y is the certificate@verification algorithm;;certificate length polynomial in |x|@polynomial length;;P ⊆ NP@Every language in P"
That check is a verification algorithm, and the ordering is its certificate. NP is the class of languages with a polynomial time verifier and certificates of polynomial length. Every language in P is in NP, because a decider can just ignore the certificate.

@art class-diagram
Whether the inclusion is strict is the open question. The section adds two more: whether NP equals co NP, and whether P equals the overlap of NP and co NP. The authors say which picture most researchers expect, without claiming it's been shown.

@chapter Verifier and searcher
@math heading="(¬x1 ∨ x2 ∨ x3) ∧ (x1 ∨ ¬x2) ∧ (¬x2 ∨ ¬x3) ∧ (¬x1 ∨ ¬x3)" items="x1=T x2=T x3=F@x one true;;4 questions · 3 models of 8@four questions"
Here's the lesson's formula. The lab plays the searcher with a yes or no oracle. Ask whether the formula is satisfiable. Then fix x one true and ask again, keeping true if yes. It builds x one true, x two true, x three false, and checks it clause by clause. Four questions, three models among eight assignments.

@art search-tree
Brute force would walk this whole tree of choices, one leaf for every assignment. The self reduction walks a single path down it, fixing one variable per question.

@art oracle-questions
That's at most n plus one questions where trying assignments could take two to the n. But each question is a call to an oracle that decides satisfiability, and no fast algorithm for that is known. Finding a certificate is no harder than deciding one exists. Neither is shown easy.

@chapter Where people slip
@list heading="Common slips" items="Reading NP as not polynomial@The first|Measuring time against the value@The second|Taking the self-reduction as fast@the third"
The first slip is reading NP as not polynomial. It's nondeterministic polynomial, defined by verification, and P is inside it. The second is measuring time against an input's value instead of its length. And the third is taking the self reduction for a fast algorithm.

@chapter Try it
@code block=1 lines=1-1 focus="1@four clauses"
Your turn. Take these four clauses. Run the self reduction by hand, saying which formula each question asks about, and its answer. Then check the assignment as a verifier would, clause by clause, and count the formula's models.

@end text="Check a certificate"
You can build and check satisfying assignments yourself, on Learn. That's learn dot get er done dot I O.
