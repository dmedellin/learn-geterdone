---
format: long
lesson: discrete-probability/probability-axioms
title: The three probability axioms, and everything they give you
thumb: Three rules, every theorem
---

@chapter The idea
@title text="The Probability Axioms" sub="Discrete Probability" art=thumb
Equally likely outcomes are one way to assign probabilities. But a loaded die isn't equally likely, and it still has probabilities. So what do all probability assignments have in common? Just three rules.

@math heading="A finite probability space" items="A1   P(E) ≥ 0@never negative;;A2   P(S) = 1@total is one;;A3   P(A ∪ B) = P(A) + P(B)  when A ∩ B = ∅@disjoint events"
Take a sample space S and a function P on its subsets. First, P of any event is never negative. Second, the probability of the whole sample space, its total is one. Third, for disjoint events, the probability of their union is the sum of their probabilities.

@art disjoint-blobs
That third rule is the only way probabilities combine, and it only applies when the events share no outcomes.

@art mass-bar
That's all. Notice the axioms don't say what probability means. They only constrain how probabilities combine. The equally likely model is one assignment that satisfies them, and it's not the only one.

@chapter What follows
@words text="Everything else is a theorem"
Every other rule you know is proved from those three. The complement rule, monotonicity, inclusion and exclusion, and the union bound. Let's prove them, one at a time.

@math heading="The empty event" items="S ∪ ∅ = S, disjoint ⟹ P(S) = P(S) + P(∅)@S and the empty set;;⟹ P(∅) = 0@is zero"
S and the empty set are disjoint, and their union is S. So by axiom three, P of S equals P of S plus P of the empty set. That means P of the empty set is zero.

@math heading="The complement" items="E ∪ Ē = S, disjoint ⟹ P(E) + P(Ē) = 1@E and not E;;⟹ P(Ē) = 1 − P(E)@one minus;;⟹ P(E) ≤ 1@at most one"
Next, E and not E are disjoint, with union S, so by axioms two and three their probabilities add to one. So P of not E is one minus P of E. And since P of not E is at least zero, P of E is at most one.

@art nested-circles
Monotonicity. If A sits inside B, then B is A together with B minus A, and those two pieces are disjoint. So P of B is P of A plus P of B minus A, and by axiom one that's at least P of A.

@art three-pieces
Inclusion and exclusion. The union of A and B splits into three disjoint pieces: A but not B, A and B, and B but not A. Adding P of A and P of B counts the middle piece twice.

@math heading="Inclusion–exclusion and the union bound" items="P(A ∪ B) = P(A) + P(B) − P(A ∩ B)@subtract it once;;P(A ∪ B) ≤ P(A) + P(B)@the union bound"
So subtract it once, and you get the probability of the union. Then, since the overlap's probability is never negative, you get the union bound: the probability of A or B is at most P of A plus P of B.

@chapter The union bound
@art union-bound
The union bound looks weak, but it's used constantly. It bounds the chance that anything at all goes wrong by the sum of the individual failure probabilities. And it needs no independence assumption whatsoever.

@chapter A loaded die
@art loaded-bars
For a finite sample space, any assignment of non-negative numbers to the outcomes that adds up to one defines a probability space. So suppose a die has P of six equal to one third, and the other five faces share the rest equally.

@math heading="Loaded die" items="P(6) = 1/3,  others 2/15 each@two fifteenths;;1/3 + 5 · 2/15 = 1/3 + 2/3 = 1@Check;;P(even) = 2/15 + 2/15 + 1/3 = 3/5@three fifths"
Each of the other faces gets two fifteenths. Check: one third plus five times two fifteenths is one third plus two thirds, which is one. Then P of an even number is two fifteenths plus two fifteenths plus one third, which is three fifths. The equally likely model would have said one half.

@words text="The axioms did all the work"
The axioms did all the work there, and the equally likely assumption did none. Everything from conditional probability onward is proved from the axioms, so it holds for loaded dice too.

@chapter Where people slip
@list heading="Common slips" items="Adding probabilities of overlapping events@overlapping events|Confusing disjoint with independent@disjoint with independent|Using the count ratio for a loaded die@loaded die"
First, adding probabilities of overlapping events. Axiom three needs disjointness, and without it the sum overshoots by the overlap, and may even exceed one. Second, confusing disjoint with independent. Disjoint events with positive probability are maximally dependent. Third, using size of E over size of S for a loaded die. It's simply the wrong formula.

@chapter Try it
@words text="Loaded die: P(odd)?" sub="P(6) = 1/3, others 2/15"
Your turn. With the same loaded die, find the probability of an odd number. Then check that it and P of even add to one, exactly as the complement rule says they must.

@end text="Three rules, every theorem"
The full lesson, with practice and recall questions, is on Learn. That's learn dot get er done dot I O.
