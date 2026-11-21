---
format: long
lesson: identity-modality-and-freedom/necessity-possibility-and-possible-worlds
title: Possible worlds: what necessarily really means
thumb: Necessary, and false?
---

@chapter The question
@title text="Necessity, Possibility and Possible Worlds" sub="Identity, Modality and Freedom" art=thumb
What does it mean to say something is necessarily true? It's tempting to say, it's true, and certain. But that reading fails. A claim of necessity is a claim about other worlds, and which worlds count is part of the model.

@art worlds-and-arcs
A possible worlds model has three parts. A set of worlds. An accessibility relation, arrows saying which worlds each world can see. And a valuation, saying which sentence letters are true at which world. A formula is evaluated at a world, so it can be true at one and false at another.

@chapter Box and diamond
@math heading="The two operators" items="□p true at w  ⟺  p true at every world w sees@box p;;◇p true at w  ⟺  p true at some world w sees@diamond p"
The ordinary connectives work world by world, as before. Two new operators look beyond. Box p is true at a world when p is true at every world it sees. Diamond p is true at a world when p is true at some world it sees. They look only at the worlds it sees.

@chapter Necessity without truth
@art one-way-arc
Take two worlds. World one sees world two, and nothing else. The letter p is true at world two only.

@math heading="At w1" items="w1 sees: w2@the one world it sees;;p at w2: true,  so □p at w1: true@true there;;p at w1 itself: false@world one itself"
At world one, the box asks about the one world it sees, world two. p is true there, so box p is true at world one. But p isn't true at world one itself. So in this model, p is necessary as seen from world one, and false at world one.

@words text="Not: true and certain" sub="no believers in the model · w1 does not see itself"
The reading true and certain fails for both halves. Certainty is a fact about someone's evidence, and the model has no believers in it. And truth at the world itself isn't guaranteed either, because world one doesn't see itself.

@chapter One more arc
@art self-loop
Give world one an arrow to itself, and the guarantee returns. The box now includes the world being evaluated. p is false there, so box p is false. Whether necessity implies truth depends on whether worlds see themselves.

@art arc-toggle
Notice that the valuation didn't change. One arc did. So necessity is never a property of p alone. It's a property of p and a model.

@chapter A world that sees nothing
@art lonely-world
Now suppose world one sees no world at all. The box is a universal claim over the worlds seen. A universal claim over no worlds has nothing to fail it, so it's true. So box p is true at world one for every p, even one false everywhere.

@math heading="At a world that sees nothing" items="□p: true for every p@box p is true;;◇p: false for every p@diamond p is false;;◇p ≡ ¬□¬p@linked"
So box p is true for every p. And diamond p is false for every p, since there's no seen world to find it at. The two operators are linked. Diamond p is the same as not box not p. At a world that sees nothing, the pair is necessarily true, and possibly false, together.

@chapter What the lab settles
@art three-readings
Whether the arcs for logical necessity, for what's known, or for what's permitted should look one way or another is a question about those subjects. The lab leaves it open. Change its reading from metaphysical to epistemic or deontic, and only the words change, never the computation. Given these arcs, this is the verdict.

@chapter Where people slip
@list heading="Common slips" items="Reading necessarily p as true and certain@The first|Thinking a world that sees nothing makes the box false@The second|Treating necessity as a property of the sentence alone@And the third"
The first slip is reading necessarily p as p is true and certain. The second is thinking a world that sees nothing makes the box false. A universal claim over nothing is true. And the third is treating necessity as a property of the sentence alone. A debate about necessity is partly a debate about which arcs to draw.

@chapter Try it
@words text="w1 → w2,  p at w2" sub="then add w1 → w1"
Rework the worked example. Two worlds, an arc from one to two, and p at two only. Collect the worlds that world one sees, and read box p. Then add the arc from world one to itself, and read it again. Say which arc made the difference.

@end text="Move one arc, read the box"
You can move the arcs and watch the box change, on Learn. That's learn dot get er done dot I O.
