---
format: long
lesson: paradoxes-and-their-exits/moores-paradox-and-what-cannot-be-believed
title: Moore's paradox: true, but impossible to know
thumb: It's raining, but I don't know it
---

@chapter The odd sentence
@title text="Moore's Paradox and What Cannot Be Believed" sub="Paradoxes and Their Exits" art=thumb
It's raining, but I don't know that it is. G. E. Moore noticed that some sentences are odd to assert, though nothing about their content is odd. This one could be true, as when it's raining in a room where no one has looked. Yet no one can sincerely say it. Why?

@list heading="Three premises" items="Moore's sentence can be true@can be true|What can be true can be known by its subject@can be known|No one can sincerely assert it@sincerely assert"
Set out as a paradox, it's three premises that can't all hold. Moore's sentence can be true. Whatever can be true can be known, and so sincerely asserted, by the one it's about. And no one can sincerely assert Moore's sentence.

@chapter Writing it down
@math heading="p: it is raining,  □: the speaker knows that" items="p ∧ ¬□p@p and not box p;;□(p ∧ ¬□p)@with the box"
Write p for, it's raining, and read the box as, the speaker knows that. Moore's sentence is p and not box p. For the assertion to be sincere, the speaker would have to know it. That's the sentence with the box in front.

@chapter It can be true
@art rain-unseen
Model it with two worlds. At world one, it rains. The speaker at world one sees world one and world two, and at world two it doesn't rain. So the speaker doesn't know it's raining. The lab evaluates the sentence at world one, and reports true. So it's satisfiable. Moore's paradox isn't a contradiction.

@chapter It can't be known
@math heading="Suppose □(p ∧ ¬□p) at a world" items="□p  and  □¬□p@knows p;;reflexive:  □¬□p  gives  ¬□p@every world sees itself;;□p  and  ¬□p:  no such world@cannot both"
Now suppose a world where the boxed sentence is true. The box distributes over and, so the speaker knows p, and knows they don't know p. Now use the frame. If every world sees itself, whatever's known is true there. So it's true that the speaker doesn't know p. But the speaker knows p. Those cannot both hold, so there's no such world.

@art reflexive-frame
The lab checks this on a reflexive frame, and the list of worlds where the boxed sentence holds is empty. The argument shows the same holds in any reflexive frame, of any size. The lab shows it for one frame. The argument generalises it.

@chapter The exit
@art shuttered-window
So Moore's sentence is a truth that no one in a reflexive frame can know. That's exit one, denying the second premise, that whatever can be true can be known. The price is that some truths are unknowable by their own subject. Not through ignorance of the world, but through the form of the sentence.

@chapter What the frame did
@art no-self-loops
Drop reflexivity, and see what the argument needed. Take three worlds, where world one sees world two, and world two sees world three, and no world sees itself. At world one, the speaker knows that p, and that they don't know it. Without reflexivity, what's known needn't be true. It's a model of mistaken belief.

@art dead-end
There's a subtlety here. A world that sees no world satisfies every boxed sentence vacuously, because there's nothing for the box to range over. A reflexive frame has no dead ends, which is part of why it has no world for the boxed sentence.

@art introspective-frame
And a believer who can look into their own beliefs recovers the result, even without reflexivity. In a frame where each world sees only worlds that see the same worlds, the lab again finds nothing. What it shows is a property of the frame, not a finding about people.

@chapter Where people slip
@list heading="Common slips" items="Treating Moore's sentence as a contradiction@The first|Reading the boxed failure as the sentence failing@The second|Thinking it depends on how many worlds are drawn@And the third"
The first slip is treating Moore's sentence as a contradiction. It's true at world one. The second is reading the failure of the boxed form as a failure of the sentence. The odd thing is the claim to know, not the content. And the third is thinking the result depends on how many worlds are drawn.

@chapter Try it
@words text="p ∧ ¬□p,  then □(p ∧ ¬□p)" sub="on each frame"
Evaluate both sentences on each frame in the lab. Reflexive, no self loops, and the introspective one. Say which property of the arrows made the boxed sentence impossible, and which exit that leaves you.

@end text="True, and unknowable"
You can test Moore's sentence on your own frames, on Learn. That's learn dot get er done dot I O.
