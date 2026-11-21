---
format: long
lesson: identity-modality-and-freedom/frames-axioms-and-what-necessity-obeys
title: Modal axioms T, D, B, 4 and 5, read off the arrows
thumb: Each axiom is a shape of arrows
---

@chapter The question
@title text="Frames, Axioms and What Necessity Obeys" sub="Identity, Modality and Freedom" art=thumb
Does necessity imply truth? Does necessarily p imply necessarily necessarily p? These sound like deep questions about necessity itself. In fact, each one is the fingerprint of one simple property of the arrows between worlds.

@art bare-frame
Drop the valuation, and keep only the worlds and arcs. That's a frame. A formula is valid on a frame if it's true at every world, under every valuation. One formula, called K, is valid on every frame. The interesting ones aren't.

@chapter Five axioms
@math heading="Axiom: what the arcs must do" items="D:  □p → ◇p   serial@D says;;T:  □p → p   reflexive@T says;;B:  p → □◇p   symmetric@B says;;4:  □p → □□p   transitive@Four says;;5:  ◇p → □◇p   euclidean@Five says"
D says if box p, then diamond p. It needs a serial frame, where every world sees some world. T says if box p, then p. It needs every world to see itself. B says if p, then box diamond p. It needs symmetry. Four says if box p, then box box p. It needs transitivity. Five says if diamond p, then box diamond p. It needs a euclidean frame.

@chapter Reasoning out T
@art no-self-loop
You don't have to memorise the table. Each row can be reasoned out. Suppose a world w doesn't see itself. Make p true at every world w sees, and false at w. Then box p is true at w, and p is false. So T fails.

@art all-loops
The other direction is as direct. If every world sees itself, then box p includes p at the world itself. So T holds. A frame validates T exactly when it's reflexive.

@chapter Reasoning out 4
@art missing-shortcut
Transitivity is the same argument, one step longer. Suppose w sees v, v sees u, and w doesn't see u. Make p true at everything w sees, and false at u. Then box p is true at w. But box box p is false at w, because v sees u.

@chapter Reading B
@words text="B: p → □◇p" sub="not p → □p"
B is easy to misread. It doesn't say what's true is necessarily true. That would be if p then box p. It says what's true is necessarily possible. Wherever p holds at w, every world w sees must itself see a world with p. Symmetry supplies one, since that world sees w.

@chapter Named logics
@list heading="Named systems" items="S4: reflexive and transitive@S four|S5: reflexive, symmetric and transitive@S five"
Some frames have names. A reflexive and transitive frame validates S four. An equivalence relation, reflexive, symmetric and transitive, validates S five. In S five, every world in a group sees every other.

@art growing-frame
Each step up adds a property, so each adds axioms.

@math heading="Growing a frame" items="cycle  w1 → w2 → w3 → w1:  D@a cycle;;loops,  w1 → w2,  w2 → w3:  D, T@loops;;add the shortcut w1 → w3:  D, T, 4@shortcut;;add every reverse arc:  D, T, B, 4, 5@every reverse"
Watch the axioms appear. A cycle of three worlds validates only D. Drop the arc back to world one and add loops, and you get D and T. Add the shortcut from world one to world three, and four appears. Add every reverse arc, and you have all five. Nothing about necessity was consulted. Every axiom followed from the arcs, and each new one appeared exactly when its property did.

@art complete-frame
That's also the limit. A frame that validates all five is a frame. Whether it's the right model of logical necessity, metaphysical necessity, or what a person can know isn't computed. The next lessons use S five for one argument, and ask whether that was fair.

@chapter Where people slip
@list heading="Common slips" items="Treating the axioms as truths every frame obeys@The first|Reading B as what is true is necessarily true@The second|Assuming more axioms means a better model@And the third"
The first slip is treating the axioms as truths about necessity that every frame obeys. Which ones hold is a fact about the arcs you chose. The second is reading B as what's true is necessarily true. And the third is assuming the frame with more axioms is the better model. That's a difference in arcs, not in correctness.

@chapter Try it
@words text="add 1-1  2-2  3-3" sub="watch T appear"
Try it on the lab's last model. Add a loop at every world, and read the axiom list. T should appear. Then remove one loop, choose the valuation that breaks T, and find the world where it fails.

@end text="Add an arc, read the axioms"
You can grow your own frames and watch the axioms appear, on Learn. That's learn dot get er done dot I O.
