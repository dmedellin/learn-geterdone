---
format: long
lesson: integer-programming/incumbents-bounds-and-the-optimality-gap
title: The optimality gap: what a solver has actually proved
thumb: A gap is not a probability
---

@chapter The question
@title text="Incumbents, Bounds and the Gap" sub="Integer Programming" art=thumb
A solver has been running for an hour and hasn't finished. Your manager asks: can we stop? To answer honestly, you need two numbers, and you need to know exactly what they prove.

@chapter Two bounds
@art many-sources
The incumbent is the best feasible plan found so far. For a maximisation it's a lower bound on the optimum, because it's achievable. And it doesn't matter where it came from: greed, a tree, or someone who knows the business. A plan is a plan.

@art two-bounds
The global bound comes from the relaxations: the best bound over every node still open. It's an upper bound, because it optimises over a bigger set. The optimum sits somewhere between the two.

@math heading="The gap" items="gap = bound − incumbent@the difference;;relative gap = gap ÷ incumbent@divided by"
The gap is the difference between the global bound and the incumbent. The relative gap is that difference divided by the incumbent. A gap of zero means the incumbent is optimal, and that's a proof.

@chapter Watching it close
@math heading="max 4x₁ + 3x₂" items="3x₁ + 2x₂ ≤ 17  welding@seventeen;;2x₁ + 5x₂ ≤ 23  painting@twenty three;;root relaxation 261/11 ≈ 23.73@root"
Here's the lesson's example. Maximise four x one plus three x two, with three x one plus two x two at most seventeen hours of welding, and two x one plus five x two at most twenty three of painting. The root relaxation is worth two hundred and sixty one elevenths, about twenty three point seven three.

@math heading="Newest open node first" items="node 3:  no incumbent,  bound 47/2@node three;;node 5:  21 and 47/2,  gap 5/2,  11.9%@node five;;node 7:  21 and 70/3,  gap 7/3,  11.1%@node seven;;node 9:  23 and 23,  gap 0@node nine"
After node three, there's a bound of forty seven halves and no incumbent. After node five, the incumbent is twenty one, and the gap is five halves, eleven point nine percent. After node seven, the bound is seventy thirds, a gap of seven thirds, eleven point one percent. After node nine, both are twenty three. Gap zero.

@art closing-gap
Read the node five row as a sentence. Nothing beats twenty one by more than five halves. That's all of it. As it happens, twenty one isn't best. The answer is twenty three, two more, well within the five halves allowed.

@art no-incumbent
The node three row matters too. With no incumbent, nothing at all has been proved. A bound alone rules nothing out, because it doesn't exhibit a plan. You need both numbers.

@chapter Not a probability
@words text="2% gap: nothing beats the plan by more than 2%"
A two percent gap proves that nothing beats the incumbent by more than two percent. There's no probability in that sentence. The incumbent may be optimal, or two percent short, and the gap can't tell those apart.

@words text="Stop with a gap: a result" sub="stop without one: a plan and a hope"
So can you stop? Stopping with a stated gap is a result: the plan is in hand and its worst case is quantified. Stopping without one leaves a plan and a hope, and they look identical on a slide.

@chapter Search order
@art two-orders-search
Search order changes the work, not the answer. Newest node first closes this tree in nine nodes. Most promising node first closes it in seven, and its first incumbent is already twenty three, so the gap is zero the moment it appears.

@art bound-falls
And notice where the work went. The bound went forty seven halves, seventy thirds, twenty three, while the plan sat at twenty one for four nodes and then jumped. A falling bound means the claim is getting stronger, not that the answer is improving.

@chapter Where people slip
@list heading="Common slips" items="Reading a small gap as a probability@The first|Reporting the incumbent on its own@The second|Treating a falling bound as a better answer@And the third"
The first slip is reading a small gap as a probability. The second is reporting the incumbent on its own. One number can't be checked. And the third is treating a falling bound as progress on the answer.

@chapter Try it
@words text="21 and 70/3" sub="relative gap = ?"
Your turn. After node seven the incumbent is twenty one and the bound is seventy thirds. Compute the gap, then divide by the incumbent, and check you get one ninth. Then say in one sentence what that proves, and what it doesn't.

@end text="Watch the gap close"
You can step through the tree and watch the incumbent, the bound and the gap after every node, on Learn. That's learn dot get er done dot I O.
