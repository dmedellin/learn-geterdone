---
format: long
lesson: algorithms-and-complexity/decidability-and-the-halting-problem
title: The halting problem: a proof that some questions have no algorithm
thumb: No program can decide this
---

@chapter Beyond hard
@title text="Decidability and the Halting Problem" sub="Algorithms and Complexity" art=thumb
Some problems are slow to solve. Some are worse than that. For some problems there is no algorithm at all, and that's not a guess. It's a theorem, and its proof fits on a page.

@words text="Decidable" sub="some algorithm always stops with the right yes or no"
A decision problem is decidable if some algorithm terminates on every input with the correct yes or no answer. If not, it's undecidable.

@words text="Undecidable ≠ very hard" sub="no algorithm exists, and none ever will"
Be careful what that means. Not hard, not exponential, not nobody has managed it yet. Undecidable means no algorithm exists, and none ever will.

@chapter The halting problem
@art oracle-box
Here's the famous one. Turing showed in nineteen thirty six that there is no algorithm H that takes a program P and an input x, always terminates, and correctly reports whether P halts on x.

@chapter The proof
@list heading="Build D(P)" items="Run H(P, P)@runs H|If H says P halts: loop forever@loops forever|If H says P doesn't halt: halt@halts immediately"
Suppose H did exist. Build a program D that takes one input, the source code of a program P. D runs H on P and P. If H says P halts on its own code, D loops forever. If H says P doesn't halt, D halts immediately.

@words text="D is an ordinary program"
There's nothing strange about D. It calls H, which by assumption always finishes, and then it branches. Now ask the killer question. What does D do when you feed it its own code?

@art mirror-loop
If D halts on D, then H said halts, so by construction D loops forever. Contradiction. If D doesn't halt on D, then H said doesn't halt, so D halts immediately. Contradiction again.

@art two-dead-ends
Both cases are impossible. So the assumption was wrong, and H cannot exist.

@chapter A diagonal argument
@art diagonal-grid
That's exactly Cantor's diagonal argument. Assume a complete listing, or here a complete decider. Construct the thing that differs from every entry. Derive a contradiction. Cantor used it against lists of the real numbers, and Turing used it against deciders.

@words text="Programs take programs as input"
And the self reference isn't a trick. Programs can take programs as input, and D is applied to itself. That's exactly what makes computation universal.

@chapter Rice's theorem
@list heading="All undecidable" items="Does this program ever output 0?@ever output zero|Do two programs compute the same function?@the same function|Is this code reachable?@reachable|Does this loop terminate?@terminate"
Rice's theorem goes further. Every nontrivial property of the function a program computes is undecidable, where nontrivial means some programs have it and some don't. Does this program ever output zero? Do these two programs compute the same function? Is this code reachable? Does this loop terminate? All undecidable.

@art approx-net
That's why static analysis is always conservative. Unreachable code warnings, type systems, linters and verifiers all approximate. They may report a problem that isn't there, or miss one that is, and Rice's theorem says no tool can do better for every program.

@chapter More, and the map
@list heading="Also undecidable" items="Post correspondence problem@Post correspondence|Hilbert's tenth problem (Matiyasevich, 1970)@Hilbert's tenth|Program equivalence@program equivalence"
There are others. The Post correspondence problem, a purely combinatorial question about lists of strings. Hilbert's tenth problem, whether a polynomial equation has integer solutions, shown undecidable by Matiyasevich in nineteen seventy. And program equivalence, by Rice.

@art hierarchy-rings
So here's the whole map. P, solvable efficiently. NP, verifiable efficiently. NP complete, the hardest in NP. EXPTIME, solvable but exponentially. Decidable, solvable eventually. And beyond that, undecidable, no algorithm at all.

@chapter Where people slip
@list heading="Common slips" items="Reading undecidable as very hard@The first|Thinking one program's halting can't be decided@The second|Believing better tools will win@The third"
The first slip is reading undecidable as very hard. The second is thinking a particular program's halting can't be determined. Many are easy. The theorem is about one procedure that covers them all. And the third is believing better tools will eventually decide these questions. Practical verification works by restricting the question, not by beating the theorem.

@chapter Try it
@words text="Does Rice's theorem apply?" sub="is it about what the program computes?"
Try sorting a few questions yourself. Does this program ever output zero? Does its source code have more than a hundred lines? For each one, ask whether it's about the function the program computes, and whether some programs have the property and some don't. If both are true, Rice says it's undecidable.

@end text="Some questions have no algorithm"
And that's where this course ends: some problems are intractable, and some are beyond any algorithm whatever. The full lesson is on Learn. That's learn dot get er done dot I O.
