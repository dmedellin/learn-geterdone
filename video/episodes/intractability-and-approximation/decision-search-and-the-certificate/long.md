---
format: long
lesson: intractability-and-approximation/decision-search-and-the-certificate
title: Yes or no is enough: getting an answer out of a decision oracle
thumb: Four questions, one answer
---

@chapter Yes-or-no problems
@title text="Decision, Search and the Certificate" sub="Intractability and Approximation" art=thumb
The theory of hard problems is stated for yes or no questions. That sounds like a big restriction. It isn't. Here's a yes or no oracle handing over a full answer it was never asked for.

@art yes-no-box
A decision problem is a set of inputs, with a yes or no question about each one. SAT asks of a formula: is there an assignment of true and false that satisfies every clause? An algorithm for it only has to answer. It doesn't have to hand anything back.

@chapter Checking versus finding
@art certificate-check
Hand someone an assignment, and they can check every clause in one pass. Ask them to find one, and nobody knows a method that isn't, in the worst case, a search. That gap is what a certificate captures.

@list heading="Two classes" items="NP: every yes instance has a certificate a polynomial-time verifier accepts@NP is|P: solvable in polynomial time@P is|P ⊆ NP@inside N P"
NP is the class of decision problems where every yes instance has a short certificate that a polynomial time verifier accepts, and no certificate fools it on a no instance. P is the class solvable in polynomial time. P sits inside N P, because a solver is a verifier that ignores its certificate. Whether that's strict, nobody knows.

@chapter Search from decision
@list heading="Three forms of one question" items="Decision: does a solution exist?@The decision form|Search: hand me one@the search form|Optimisation: hand me the best@the optimisation form"
Every problem on this course can be asked three ways. The decision form asks whether a solution exists. The search form asks for one. The optimisation form asks for the best one. The theory is stated for the first, and the reason that costs nothing is this lesson.

@art fix-variable
Here's why the restriction costs almost nothing. Ask the oracle about the whole formula. If it says no, you're done. If yes, fix x one to true, simplify, and ask again.

@list heading="One question per variable" items="Still yes: some model has x₁ true, keep it@If it says yes|No: every model has x₁ false, commit to false@If it says no|Repeat for x₂ … xₙ@Repeat"
If it says yes, some satisfying assignment has x one true, so keeping it loses nothing. If it says no, every satisfying assignment has x one false, so committing to false loses nothing. Repeat for every variable. One question settles one variable, so n plus one calls write out the whole assignment.

@chapter Four calls
@math heading="Three variables, four clauses" items="(x₁ ∨ x₂ ∨ ¬x₃) ∧ (¬x₁ ∨ x₂ ∨ x₃) ∧ (x₁ ∨ ¬x₂ ∨ x₃) ∧ (¬x₁ ∨ ¬x₂ ∨ ¬x₃)@the formula;;4 oracle calls  vs  8 assignments@four oracle calls;;answer: x₁ = T, x₂ = T, x₃ = F@x one true"
Here's the formula in the lab, three variables and four clauses. The panel reports four oracle calls, against eight assignments a search would try. And the answer comes out x one true, x two true, x three false.

@art refusal-step
At x one and x two, both branches are allowed, so it takes true. After that, what's left is just not x three. The oracle refuses x three true, so it's false. That one refusal is the difference between an assignment and a guess, and it cost one question.

@words text="checked, not assumed"
Two checks run beside the trace. Every restricted formula is re decided by brute force, and the final assignment is evaluated clause by clause. A reduction that produced a confident wrong answer would look identical on the page without them.

@chapter Read the numbers carefully
@art call-tree
Now read the two numbers side by side, and resist the obvious conclusion.

@words text="4 vs 8 · 5 vs 16" sub="calls grow by one; assignments double"
With four variables, it's five calls against sixteen. Calls grow by one per variable, and assignments double.

@art doubling-bars
So the gap widens without limit. But that's a claim about the two expressions, not something the numbers on screen can prove. And the oracle itself is brute force, trying all eight.

@words text="polynomial in calls" sub="not in running time"
That's deliberate. The claim is about the number of calls, not their cost. Anyone who concludes from this page that satisfiability has been solved efficiently has read a statement about one quantity as a statement about another.

@chapter Where people slip
@list heading="Common slips" items="Reading NP as a claim about finding@The first|Taking the call count for a running time@The second|Thinking decision results are weaker@And the third"
The first slip is reading the certificate definition as a claim about finding. It's only about checking. The second is taking the call count for a running time. Here, one call is itself a search. And the third is thinking decision results are weaker. Search and optimisation are no harder, by an argument just like this one.

@end text="n + 1 questions"
Watch the oracle answer each question on Learn. That's learn dot get er done dot I O.
