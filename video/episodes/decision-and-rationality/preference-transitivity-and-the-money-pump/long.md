---
format: long
lesson: decision-and-rationality/preference-transitivity-and-the-money-pump
title: The money pump: what it costs to have circular preferences
thumb: Three cents a lap, forever
---

@chapter Preference as a relation
@title text="Preference, Transitivity and the Money Pump" sub="Decision and Rationality" art=thumb
Can your preferences be irrational? Not what you like, but how your likes fit together. There's an argument that says yes, and it puts a price on it.

@math heading="Two symbols" items="A ≻ B:  A is strictly preferred to B@strictly preferred;;A ≽ B:  A is at least as good as B@at least as good"
Choice theory starts with pairs. Write A over B, with a curved bracket, when A is strictly preferred to B. And add a line underneath when A is at least as good: preferred, or tied. Everything later in the course assumes this relation can be turned into a ranking.

@list heading="Two conditions for a ranking" items="Complete: of any two, one is at least as good@Complete|Transitive: A ≽ B and B ≽ C give A ≽ C@Transitive"
That needs two conditions. Complete: for any two options, at least one is at least as good as the other, so you're never left without a view on a pair. Transitive: if A is at least as good as B, and B as C, then A is at least as good as C. Going through a third option doesn't change the answer.

@art ranking-ladder
Together they let you line the options up like rungs on a ladder, with ties sharing a rung. And the conditions don't care what the options are. Cakes, careers or lotteries, the relation is the same kind of thing.

@chapter A cycle
@math heading="A cycle" items="A ≻ B@A over B;;B ≻ C@B over C;;C ≻ A@C over A"
Now a cycle. A over B. B over C. C over A. Nothing in those three lines is false as a report of taste. But every option is beaten by another, so choosing the best has no answer.

@art grid-loop
On a grid of preferences, a cycle shows up as a loop. Follow the chain far enough, and each option ends up preferred to itself, which nobody means by preference.

@chapter The money pump
@art trader-swap
Here's what a cyclic chooser will do. Suppose you hold A, and you prefer C to A, B to C, and A to B. A trader offers C for A plus a small fee. You accept, because you prefer C. Then B for C plus the fee. You accept. Then A for B plus the fee. You accept again.

@math heading="One lap, at 1 cent a swap" items="A → C:  −1 cent@A for C;;C → B:  −2 cents@C for B;;B → A:  −3 cents@B for A;;100 laps:  −300 cents, still holding A@a hundred laps"
Walk it at a cent a swap. A for C: minus one. C for B: minus two. B for A: minus three. You're holding A again, and you're three cents poorer. After a hundred laps, you're down three hundred cents, still holding A.

@art lap-loss
Each trade was one you wanted at the moment you made it. It's the sequence that has no defence. And the fee can be as small as you please. The loss is three times the fee a lap, whatever the options are.

@chapter An objection
@art three-flats
The strongest objection deserves a hearing. You might rank three flats by different standards: price against size, size against light, light against price. Each pairwise verdict can be reasonable. The reply is that this is a cycle in the pairwise verdicts, not in a ranking of the flats as wholes. One standard has to give way, or a weighting has to be chosen, before you can act without being walked in circles.

@words text="The pump prices cycles."
And the argument has a limit. It assumes you'll pay for every swap, with no memory of the lap. If you see the trader coming and refuse the third offer, you've changed your preferences, which is exactly the repair transitivity asks for. The pump doesn't prove cycles unthinkable. It prices them.

@chapter Where people slip
@list heading="Common slips" items="Treating transitivity as a matter of taste@The first|Reading a cycle as indifference@The second|Expecting one choice to show the defect@the third"
The first slip is treating transitivity as a matter of taste. Taste decides whether you prefer tea to coffee. Transitivity constrains how preferences fit together. The second is reading a cycle as indifference. And the third is expecting a single choice to show the defect. The cost only appears in a sequence.

@art tie-rung
On that second slip: if A, B and C are tied, nothing's wrong. Ties are transitive, and nobody pays to swap between things they value equally. A cycle is the opposite case, a strict preference all the way round, and that's why each swap gets paid for.

@chapter Try it
@words text="X ≻ Y,  Y ≻ Z,  Z ≻ X" sub="2 cents a swap · how much per lap?"
Here's one to try. An agent prefers X to Y, Y to Z, and Z to X, and pays two cents to swap to anything it prefers. It holds X. Walk it round the cycle once. How much has the trader collected when the agent is back to X?

@end text="Add a loop, read the broken pair"
You can add a loop to a preference grid and see where transitivity breaks, on Learn. That's learn dot get er done dot I O.
