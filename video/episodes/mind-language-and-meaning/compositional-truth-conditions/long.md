---
format: long
lesson: mind-language-and-meaning/compositional-truth-conditions
title: Truth conditions: evaluating a sentence in a model
thumb: True in which model?
---

@chapter The idea
@title text="Compositional Truth Conditions" sub="Mind, Language and Meaning" art=thumb
To give the meaning of a sentence is, at least, to say when it would be true. Knowing that isn't knowing whether it is true. And a sentence is true or false only in a model.

@art domain-box
The truth conditions of a sentence are the conditions under which it would be true. To know them is to know, for any situation described in enough detail, whether the sentence is true there. It isn't to know whether the sentence is true.

@chapter A small model
@art three-dots
A situation, here, is a finite model. A domain of individuals, an extension for each predicate, and a referent for each name. Take three individuals, a, b and c. Planet holds of a and b. Orbits holds of the pair a, b, and of the pair b, c. It's a table, not astronomy.

@list heading="The rules" items="Atomic: is it in the extension?@An atomic|Connectives: the truth tables@The connectives|∀x: every individual · ∃x: at least one@A universal"
The rules are short, and they're the whole method. An atomic sentence is true when its individuals are in the extension. The connectives take their values from their parts, by the truth tables. A universal is true when its part is true for every individual, and an existential when it's true for at least one.

@chapter Every planet orbits something
@math heading="∀x (Planet(x) → ∃y Orbits(x, y))" items="x = a:  Planet(a) T,  y = b works:  T@Put a;;x = b:  Planet(b) T,  y = c works:  T@Put b;;x = c:  Planet(c) F:  conditional T@Put c;;every x passes:  True@Every individual"
Take the sentence, every planet orbits something. Put a for x. a is a planet, and putting b for y gives a pair in the extension, so the conditional is true. Put b for x. b is a planet, and c is what it orbits. True. Put c for x. c isn't a planet, so the conditional is true whatever c orbits. Every individual passes, and the sentence is true.

@chapter Remove one pair
@art removed-pair
Now remove the pair b, c from Orbits, and change nothing else. The sentence is the same, with the same words in the same order. At a, it still passes. But at b, the planet orbits nothing. There's no witness, so the conditional is false, and the sentence is false. One pair in one extension decided the value.

@words text="Is this sentence true?" sub="no answer until a model is named"
That's the point about truth conditions. Someone who understands the sentence knows what it takes for it to be true, in any model. They don't thereby know which model is the actual one. So, is this sentence true, has no answer until a model is named.

@chapter Existentials and nesting
@art self-loop-missing
Now try a different kind of sentence, one that asks for a witness.

@math heading="A planet that orbits itself" items="∃x (Planet(x) ∧ Orbits(x, x))@a planet that orbits itself;;no witness:  False@no witness"
An existential is the same idea, turned over. Is there a planet that orbits itself? Check each individual in turn. No individual in the model is one, so there's no witness, and the value is false. A universal is refuted by one individual, and an existential is confirmed by one.

@art love-ring
Two quantifiers nest the same way. For everyone, there's someone they love. In a ring where a loves b, b loves c, and c loves a, every individual passes. Three of three. For the planets it was three of three as well, and two of three once the pair b, c was gone.

@chapter Where people slip
@list heading="Common slips" items="Thinking a sentence is true or false on its own@The first|Reading a universal as a statement about most@The second|Reading a false antecedent as a failure@And the third"
The first slip is thinking a sentence is true or false on its own. Its value belongs to it together with a model. The second is reading a universal as a statement about most. Ninety nine passing individuals and one failing one leave it false. And the third is reading a false antecedent as a failure. c isn't a planet, so the sentence isn't about it.

@chapter Try it
@art extension-edit
Try the lab's challenge. Start from the model without the pair b, c, where the sentence is false at b. Find the smallest change to an extension that makes it true again. Then do the same for the planet that orbits itself. Say which entry decided each.

@end text="One sentence, many models"
You can edit the model and evaluate sentences yourself, on Learn. That's learn dot get er done dot I O.
