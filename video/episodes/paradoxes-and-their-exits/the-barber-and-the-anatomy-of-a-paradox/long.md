---
format: long
lesson: paradoxes-and-their-exits/the-barber-and-the-anatomy-of-a-paradox
title: The barber paradox, and what a paradox really is
thumb: Three exits
---

@chapter What a paradox is
@title text="The Barber and the Anatomy of a Paradox" sub="Paradoxes and Their Exits" art=thumb
The word paradox gets used for anything surprising. Here it means something narrower, and the narrowness makes it useful. A paradox is an argument with three features, all at once.

@list heading="A paradox" items="It looks valid@looks valid|Each premise looks plausible@Each premise|The conclusion can't be accepted@the conclusion"
It looks valid: no case makes every premise true and the conclusion false. Each premise looks plausible, taken by itself. And the conclusion is one that can't be accepted. Remove any one feature, and what's left is an ordinary refutation, or an ordinary surprise.

@art three-doors
Because the argument looks valid and the conclusion has to go, there are three exits. Deny a premise, and say why it deceived. Fault a step, because it trades on an ambiguity, or a rule that fails here. Or accept the conclusion, because it was only unfamiliar. Every lesson in this course ends by asking which exit the best answer takes, and what it costs.

@chapter The barber
@art village-barber
The oldest tidy example is a village with a barber, and a rule about him. The barber shaves all and only those who don't shave themselves.

@math heading="The village rule" items="∀x (Shaves(b, x) ↔ ¬Shaves(x, x))@for every"
Write b for the barber. The rule says, for every individual x, the barber shaves x exactly when x doesn't shave x.

@chapter Apply it to the barber
@math heading="Put x = b" items="Shaves(b, b) ↔ ¬Shaves(b, b)@b shaves b;;s ↔ ¬s@s if and only if;;s true:  T ↔ F,  false@If s is true;;s false:  F ↔ T,  false@If s is false"
Now apply the rule to the barber himself, which is allowed, because it's about everyone. b shaves b exactly when b doesn't shave b. Write s for, b shaves b. Then it's s if and only if not s. If s is true, the left is true and the right is false. If s is false, the reverse. Either way, it fails.

@words text="Valid · the logic of every · a contradiction" sub="so the first premise goes"
Lay out the whole argument. Premise one: there's a barber the rule is true of. Premise two: what a rule says of every individual, it says of b. The conclusion is a contradiction. The steps are valid, and the second premise is just the logic of every. So the first premise goes.

@art empty-chair
That's exit one, and it's the cheapest exit this course will offer. Nothing about shaving or logic is overturned. The rule can be written down and understood, and there's simply no barber who meets it. It's like, the largest whole number: a description no one satisfies, however clearly it reads.

@chapter The lab's village
@art shaving-arrows
The lab builds a village of a, b and c, with b as the barber. In the first one, a shaves himself, b shaves c, and c shaves no one. That satisfies the rule for a and c, and leaves b as the failure. Try to repair it. Adding b shaves b never helps, because the instance at b is s if and only if not s either way.

@art loop-paradox
Be clear about the lab's limit. It evaluates the sentence in the models you build, and says false in each. It doesn't search all models. That the sentence is false in every model of any size comes from the argument. The lab shows the instance. The argument generalises it.

@art outside-village
A change of wording changes the verdict. If the rule only ranges over villagers, and the barber isn't one, nothing demands anything of b. The lab reports true. The barber can exist, if he lives outside the rule. The next paradoxes are harder, because the premise that has to go won't be so easily spared.

@chapter Where people slip
@list heading="Common slips" items="Treating a paradox as a contradiction@The first|Hunting for a flaw in the logic@The second|Reading the lab's false as a proof for all models@And the third"
The first slip is treating a paradox as a contradiction. The sentence isn't the paradox. The argument is. The second is hunting for a flaw in the logic of the barber, or a trick in the word shaves. The steps are valid. And the third is reading the lab's false as a proof for all models. Say whether you're relying on the lab, or the argument.

@chapter Try it
@words text="add bb · remove bc · add ba" sub="the sentence stays False"
Try to repair the first village. Add b shaves b, remove b shaves c, add b shaves a. The sentence stays false. Then switch to the rule that only ranges over villagers, and see the only change that helps.

@end text="Find the exit"
You can build your own village and test the rule, on Learn. That's learn dot get er done dot I O.
