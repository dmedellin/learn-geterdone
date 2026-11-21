---
format: long
lesson: mind-language-and-meaning/functionalism-and-multiple-realisability
title: Functionalism: two circuits, one truth table
thumb: Same function, different wiring
---

@chapter The idea
@title text="Functionalism and Multiple Realisability" sub="Mind, Language and Meaning" art=thumb
Could an octopus be in pain? It has no C fibres. Could a machine? It has no neurons at all. Functionalism says yes, they could, if something in them plays the right role.

@art many-materials
Functionalism says a mental state is defined by the role it plays. What brings it about, what it brings about, and how it combines with other states. Anything with states playing those roles is in the state, whatever it's made of.

@art octopus-machine
If that's right, the identity theory was aiming at the wrong level. Pain isn't the firing of C fibres, because an octopus, or a machine, might be in pain by having something in the right role. One state, many realisations. That's multiple realisability.

@chapter Two circuits
@art two-circuits
A truth table shows the idea at its smallest scale. Here are two circuits with three inputs, p, q and r. They're wired differently, and one has more gates than the other.

@math heading="Three gates against two" items="A = (p ∧ q) ∨ (p ∧ r)@The first;;B = p ∧ (q ∨ r)@The second;;true rows of both:  TTT, TTF, TFT@the same three;;differing rows:  none@false in the same five"
The first is p and q, or p and r. Three gates, two ands and an or. The second is p and, q or r. Two gates. Put them in the lab, and they agree in all eight rows. True in the same three, and false in the same five.

@art same-table
So as functions, they're one. Anything that treats an input according to this table is doing what both do. And nothing about the output reveals which circuit produced it. A functionalist says the same of minds. The state is the function, and the circuit is its realisation.

@chapter More pairs
@art gate-shapes
And there are many other pairs.

@math heading="Other routes to one function" items="¬(¬p ∨ ¬q)  computes  p ∧ q@a negation at each input;;(p → q) ∧ (q → p)  computes  p ↔ q@if p then q"
Put a negation at each input, a disjunction, and a negation at the output, and you compute exactly p and q. That's De Morgan's law as wiring. And if p then q, and if q then p, computes p if and only if q, again by a different route.

@chapter What a test can miss
@math heading="One row apart" items="p ∧ q@p and q;;p ∧ (q ∨ r)@p and, q or r;;differ only at  p = T,  q = F,  r = T@differ in one row"
The same lab shows what a behavioural test can miss. The functions p and q, and p and, q or r, differ in one row only, where p and r are true and q is false. Feed them every other input and they behave alike. Seven rows match, and only the eighth gives them away.

@art untested-row
A tester who never tries that input concludes they're the same, and is wrong. That's the Turing judge's position too. Ten answers heard are ten rows of a table whose other rows were never tried.

@chapter What it leaves out
@words text="A table has no memory" sub="a mind has states that depend on history"
What the example leaves out matters. A truth table is a function of the present inputs, and a mind has states that depend on history. Real functionalism describes machines with internal states, not tables. And it doesn't show that the role is all there is to pain. The next lessons press that from two sides.

@chapter Where people slip
@list heading="Common slips" items="Thinking same behaviour means same mechanism@The first|Taking agreement on inputs tried for agreement@The second|Reading functionalism as saying material never matters@And the third"
The first slip is thinking the same behaviour means the same mechanism. A function can be reached by more than one route. The second is taking agreement on the inputs you tried for agreement. A test that skips the one telling row rates two different functions equal. And the third is reading functionalism as saying the material never matters. It can still decide whether anything plays the role at all.

@chapter Try it
@words text="A = p ∧ q,  B = p ∧ (q ∨ r)" sub="find the row where they differ"
Try it in the lab. Set A to p and q, and find the one row where it differs from p and, q or r. Fill both tables over every input, not a selection, because a shortcut here is the very mistake the lesson is about. Then set B to p and q as well, set A to the formula with a negation at each input, and confirm you find none.

@end text="Two circuits, one table"
You can compare your own circuits row by row, on Learn. That's learn dot get er done dot I O.
