---
format: long
lesson: ethics-and-welfare/the-trolley-problem-as-a-decision-matrix
title: The trolley problem as a decision table
thumb: Same numbers, different answers
---

@chapter Two cases
@title text="The Trolley Problem as a Decision Matrix" sub="Ethics and Welfare" art=thumb
Here are two famous cases with exactly the same numbers. Most people answer them differently. So if the numbers are the same, what's doing the work?

@art switch-track
In the switch case, a runaway trolley will kill five people unless you pull a lever that sends it onto a side track, where it will kill one.

@art footbridge
In the footbridge case, it will kill five unless you push a large man off a bridge into its path, killing him. Most people say pulling the lever is permissible, and pushing the man is not.

@chapter The same table
@math heading="Payoff = − deaths, outcome certain" items="switch:  divert −1,  do nothing −5@In the switch;;footbridge:  push −1,  do nothing −5@In the footbridge"
Write each case as acts against outcomes. Let the payoff be minus the number of deaths, and let the outcome be certain. In the switch case, divert scores minus one, and doing nothing scores minus five. In the footbridge case, push scores minus one, and doing nothing scores minus five.

@art twin-tables
They're the same table, with the first act renamed. Total welfare picks the largest payoff, so it says divert in the first case and push in the second. No rule that reads only the table can say otherwise. Not total welfare, and not any other rule that looks only at payoffs. They all see one table.

@words text="Something outside the table" sub="is carrying the difference"
So if you judge the cases differently, something that isn't a cell in the table is carrying the difference.

@chapter Side constraints
@art struck-row
A side constraint is a restriction on acts that holds whatever the outcomes. The constrained rule deletes every forbidden act from the table first, and then picks the best payoff among what's left.

@math heading="Forbidden: push a man to his death as a means" items="footbridge:  push struck@loses its first row;;only act left:  do nothing, −5@the only act;;switch:  nothing struck,  divert@The switch table"
Put do not push a man to his death as a means on the forbidden list. The footbridge table loses its first row, and the only act left is doing nothing, at minus five. The switch table has nothing forbidden, so its answer doesn't change. The numbers were never the difference. The list was.

@chapter Not a penalty
@art penalty-weight
A constraint isn't just a big penalty. Subtract a large number from pushing, and the act sinks in the table. But a large enough gain elsewhere brings it back, because a number can be outweighed. A constraint is applied before any weighing, so no gain can reach it.

@chapter The loop
@art loop-track
Now suppose the side track loops back to the main one, and the trolley will kill the five unless the one man's body stops it. The numbers are the same again.

@words text="Is the man being used?" sub="the loop preset lists diverting as forbidden"
Whether diverting onto the loop belongs on the forbidden list depends on whether the man is being used to stop the trolley, and people disagree. The lab's loop preset lists it as forbidden. A later lesson, on double effect, takes that up with a causal model.

@words text="The lab applies the list you give it" sub="which acts belong on it is the ethical question"
So be clear about what the lab does. It applies the list you give it, whatever that list says. Whether an act belongs on the list is the ethical question. It can't say why a constraint should exist, or how it fares when the stakes grow large.

@chapter Where people slip
@list heading="Common slips" items="Thinking the cases differ in their numbers@The first|Treating a constraint as a large penalty@The second|Expecting the lab to know what's forbidden@And the third"
The first slip is thinking the two cases differ in their numbers. They don't. One dies against five in both. The second is treating a constraint as a very large penalty. A penalty can be outweighed, and a constraint can't. And the third is expecting the lab to know what's forbidden. That pushing belongs on the list, and diverting doesn't, is the very thing in dispute.

@chapter Try it
@list heading="Three cases, one table" items="switch: divert@switch|footbridge, push forbidden: do nothing@footbridge|loop, divert forbidden: do nothing@loop"
Work through the three cases from the lesson. List the acts, fill in the payoffs, apply total welfare, then write the forbidden list and run the constrained rule. You should get divert for the switch, do nothing for the footbridge, and do nothing for the loop.

@end text="Strike, then maximise"
You can edit the forbidden list and watch the answer change, on Learn. That's learn dot get er done dot I O.
