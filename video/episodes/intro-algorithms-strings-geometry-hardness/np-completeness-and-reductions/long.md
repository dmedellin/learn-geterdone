---
format: long
lesson: intro-algorithms-strings-geometry-hardness/np-completeness-and-reductions
title: NP-completeness: proving a problem is hard by construction
thumb: Turn a formula into numbers
---

@chapter A statement about hardness
@title text="NP-Completeness and Reducibility" sub="Introduction to Algorithms, Sections 34.3–34.5" art=thumb
Most of the book proves algorithms are fast. These sections prove problems are probably not.

@quote text="When we demonstrate that a problem is NP-complete, we are making a statement about how hard it is (or at least how hard we think it is), rather than about how easy it is." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 34"
When we demonstrate that a problem is NP complete, we are making a statement about how hard it is, or at least how hard we think it is, rather than about how easy it is.

@chapter Reductions
@art reduction-map
A reduction from L one to L two is a function f, computable in polynomial time, such that x is in L one exactly when f of x is in L two. Put f in front of a fast decider for L two, and you've decided L one. So L one is no harder than L two.

@math heading="Two definitions" items="NP-hard: every NP language reduces to it@NP hard;;NP-complete: NP-hard and in NP@NP complete;;one NPC problem in P ⇒ P = NP@Theorem thirty four point four"
A language is NP hard when every language in NP reduces to it, and NP complete when it's also in NP. Theorem thirty four point four draws the consequence. A fast algorithm for any one NP complete problem would give one for every problem in NP.

@chapter The first one
@art circuit
Something has to be first. The book takes circuit satisfiability: is there an input that makes a boolean circuit output one? The whole computation of any polynomial time verifier can be wired as one circuit, whose only free inputs are the certificate's bits. That's the only proof that reduces every NP problem directly.

@list heading="The five-step method" items="prove it's in NP@in NP|choose a known NPC language@choose|describe the map@describe|prove both directions@both directions|prove it's polynomial@polynomial time"
After that, there's a five step method. Prove the language is in NP. Choose a known NP complete language. Describe a map from its instances. Prove the map preserves the answer in both directions. And prove it runs in polynomial time.

@art reduction-chain
Section thirty four point five extends the chain. From three CNF satisfiability to clique, clique to vertex cover, vertex cover to hamiltonian cycle, hamiltonian cycle to the travelling salesman, and three CNF satisfiability to subset sum.

@chapter Formulas into numbers
@art digit-columns
The subset sum construction is worth reading slowly. For n variables and k clauses, every number has n plus k decimal digits, a column per variable, and a column per clause. Each variable gets two numbers, one for true and one for false. Each has a one in its own column, and in every clause its literal satisfies.

@words text="target: 1 per variable column, 4 per clause column" sub="slack numbers 1 and 2 per clause · no column above 6"
Each clause also gets two slack numbers, with one and two in its column. The target has one in every variable column, and four in every clause column. A clause column reaches four only if at least one literal is true. No column can exceed six, so nothing carries.

@math heading="(x1 ∨ ¬x2 ∨ x3) ∧ (¬x1 ∨ x2 ∨ ¬x3)" items="x1 true: 10010 · x2 true: 01001@x one true;;target 11144@target;;6 subsets ↔ 6 satisfying assignments@six subsets"
On the lesson's formula, x one true is one, zero, zero, one, zero, and x two true is zero, one, zero, zero, one. The target is one one one four four. The lab finds six subsets that hit it, and six satisfying assignments, matched one for one.

@art failing-clause
The two assignments that fail each make one clause entirely false. That clause column would need four from slack that can supply only three.

@art both-directions
The lab checks both directions. Every subset that hits the target carries back to an assignment that satisfies both clauses, and every satisfying assignment gives a subset. For an unsatisfiable formula, there are no subsets at all.

@chapter Where people slip
@list heading="Common slips" items="Reducing in the wrong direction@The first|Checking only one direction@The second|Taking pseudo-polynomial for polynomial@the third"
The first slip is reducing in the wrong direction. To show a problem is hard, reduce a known hard problem to it. The second is checking only one direction of the answer. And the third is taking pseudo polynomial for polynomial. Subset sum's dynamic programme is proportional to the target, and every digit multiplies that by ten.

@chapter Try it
@code block=1 lines=1-1 focus="1@two clauses"
Your turn. Build the subset sum instance for these two clauses by hand, as five digit strings with the target. Then take x one true, x two false, x three true, choose its numbers and the slack each clause needs, and add them.

@end text="Build the numbers"
You can build the digit table for any formula and check the match, on Learn. That's learn dot get er done dot I O.
