---
format: long
lesson: science-induction-and-causation/preemption-and-overdetermination
title: Suzy, Billy and the bottle: when the but-for test fails
thumb: It would have broken anyway
---

@chapter Two rocks
@title text="Preemption and Overdetermination" sub="Science, Induction and Causation" art=thumb
Suzy throws a rock and shatters a bottle. Billy throws a moment later, and his rock would have shattered it if hers had missed. Did Suzy break the bottle? Obviously. But the but for test says no.

@math heading="The model" items="ST = 1,  BT = 1@both throw;;SH = ST@Suzy's rock hits;;BH = BT ∧ ¬SH@Billy's rock hits only if;;SHAT = SH ∨ BH@the bottle shatters"
Here's the model. Suzy and Billy both throw. Suzy's rock hits if she threw. Billy's rock hits only if he threw and Suzy's rock hasn't already hit. And the bottle shatters if either rock hits.

@art suzy-first
Solve it. Suzy's rock hits. So Billy's hit is one and not one, which is zero. And the bottle shatters. Suzy's rock did the work.

@chapter The test fails
@math heading="Flip Suzy's throw" items="ST = 0:  SH = 0@Suzy's rock doesn't hit;;BH = 1 ∧ ¬0 = 1@Billy's rock hits;;SHAT = 1@shatters anyway"
Now apply the but for test. Flip Suzy's throw to zero. Then Suzy's rock doesn't hit. So Billy's rock hits instead. And the bottle shatters anyway. So Suzy's throw isn't a but for cause.

@art backup-ready
This is preemption. A cause brings about an effect, and in doing so prevents a backup that was ready to bring it about. The effect would have happened without the cause, so the cause isn't a but for cause. And a counterfactual account that stopped there would say Suzy didn't break the bottle.

@chapter Hold the backup fixed
@math heading="Hold BH at its actual value, 0" items="flip ST to 0:  SH = 0@flip Suzy's throw;;BH held at 0@stays at zero;;SHAT = 0 ∨ 0 = 0@the bottle survives"
The repair uses what actually happened to the backup. In the actual course of events, Billy's rock didn't hit. So hold Billy's hit at zero, and flip Suzy's throw. Suzy's rock doesn't hit, Billy's hit stays at zero, and the bottle survives. With the backup held, flipping Suzy's throw flips the shattering.

@art held-fixed
Holding the backup fixed cancels the route through which Billy's rock took over. Billy still threw. His rock just isn't allowed to do anything it didn't actually do.

@words text="A cause, holding W fixed" sub="flip C with some set W held at actual values: does E change?"
So here's the wider test. A variable C is a cause of E when, for some set of other variables held at their actual values, flipping C changes E. If that set can be empty, C is a but for cause.

@art billy-not-cause
The held values must be the actual ones, and that matters. It's what keeps Billy's hit from qualifying. In the actual course, Suzy's rock has already hit, so nothing done to Billy's hit changes the shattering. Billy's hit is not a cause.

@words text="Billy's throw: only a joint cause with Suzy's"
Billy's throw comes out only as a joint cause with Suzy's, since flipping both throws leaves the bottle whole. That's true. But it's not what we mean by Billy having broken it. The joint rule can't tell equal partners from a cause and a bystander.

@chapter Both at once
@art simultaneous-rocks
Now remove the ordering. Both throw, both rocks reach the bottle at the same moment, and each hit is enough on its own. This is overdetermination. Flip Suzy's throw, and Billy's rock still shatters the bottle. Holding his hit at its actual value, one, doesn't help, since it's already doing the work.

@math heading="Overdetermination" items="flip ST alone:  SHAT = 1@neither throw passes alone;;flip both throws:  SHAT = 0@flip both"
So neither throw passes alone. Flip both, and the bottle survives. The pair passes together, and each throw is a joint cause with the other.

@chapter Limits
@art major-sergeant
Schaffer's case of trumping has a major's order and a sergeant's order that agree, and the soldiers do what the major says. Written with the sergeant obeyed only if the major gave no order, the equations are just those of preemption. A model like this can't represent a difference between preemption by timing and by rank, unless the equations already contain it.

@words text="A simplified Halpern–Pearl test"
And whether holding a variable fixed is a faithful account of causation is disputed. This is a simplified version of the Halpern Pearl definition, and the full version adds conditions. But anyone who rejects the approach owes a different account of why Suzy broke the bottle.

@chapter Where people slip
@list heading="Common slips" items="Thinking nothing caused what would have happened anyway@The first|Holding the backup at a convenient value@The second|Expecting each simultaneous cause to pass alone@the third"
The first slip is thinking that if the effect would have happened anyway, nothing caused it. A missing but for dependence shows a backup was present, not that the actual cause was idle. The second is holding the backup at whatever value is convenient. Only actual values may be held. And the third is expecting each of two simultaneous causes to pass alone.

@end text="Flip the cause, hold the backup"
You can flip the throws and hold the backup fixed yourself, on Learn. That's learn dot get er done dot I O.
