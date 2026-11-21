---
format: long
lesson: networks-flows-paths-and-assignments/project-networks-and-the-critical-path
title: The critical path, and the moment shortening it stops paying
thumb: When the speed-up stops
---

@chapter The question
@title text="Project Networks and the Critical Path" sub="Networks, Flows, Paths and Assignments" art=thumb
A project has nine activities, and some have to wait for others. How soon can it finish? Which activities actually hold the finish date? And if you speed one up, how long does that keep paying?

@art activity-chain
Each activity has a duration and a list of predecessors that must finish before it starts. The arcs are precedence. Nothing flows along them. And the number you want is a longest path, not a shortest one.

@chapter Four times per activity
@list heading="For each activity" items="ES: earliest start@earliest start|EF = ES + d@earliest finish|LF: latest finish@latest finish|LS = LF − d@latest start"
Each activity gets four times. The earliest start, and the earliest finish, which adds the duration. Then the latest finish that doesn't delay the project, and the latest start, which takes the duration back off. Slack is the latest start minus the earliest start.

@chapter The forward pass
@art forward-pass
The forward pass goes through the activities in order. An activity starts when its last predecessor finishes. So the rule at every node is a maximum. In the lesson's project, F waits for both D and E.

@math heading="Forward pass at F" items="EF(D) = 7,  EF(E) = 10@finish at seven;;ES(F) = max(7, 10) = 10@the maximum;;project length = 12@takes twelve"
D and E finish at seven and ten, so F starts at ten, not at seven. The maximum is the whole rule. Carry it to the end and the project takes twelve, even though the durations add up to twenty one. Independent chains run at the same time.

@chapter The backward pass and slack
@words text="G: EF 8, LF 9 → slack 1"
The backward pass is the mirror image, taking a minimum over successors. G is followed only by H, which must start by nine. So G must finish by nine. It can finish at eight, so it has one unit of slack.

@art gantt-bars
Activities with zero slack are critical. Here that's A, C, E, F and I, one critical path. Delay any of them, and the whole project slips. B and D each have three units of slack, G and H have one.

@chapter When shortening stops paying
@math heading="Shorten C" items="C − 1:  12 → 11@by one;;C − 2, 3, 4:  still 11@two, three or four;;now held by A, G, H, I@held by"
C is critical, so shorten it by one, and the project goes from twelve to eleven. Shorten it by two, three or four, and it stays at eleven. With one day off C, the project has two critical paths, and past that, the length is held by A, G, H, I, a chain C isn't on.

@art flat-curve
That's the most useful thing the method tells you. Knowing which activity to shorten is easy. Knowing when to stop, and which chain has become binding instead, is what keeps a schedule from absorbing money for nothing.

@art two-paths-level
Sometimes the first day already buys nothing. Take six activities: A for three, then two chains of two, joining at F. Both chains take the same time, the project is eight, and there are two critical paths. Shorten B, and it's still eight. Shorten one on each path, or a shared one like A or F.

@chapter When there's nothing to compute
@art precedence-loop
The forward pass needs an order where every predecessor comes first. Write A after C, B after A, and C after B, and no such order exists. Each is waiting on another. The right response is to name the loop, not to report a length. And an activity waiting on something that is not in the project gets refused by name, too.

@chapter Where people slip
@list heading="Common slips" items="Adding the durations up@The first|Treating slack as private@The second|Shortening a critical activity forever@And the third"
The first slip is adding the durations up, twenty one instead of twelve. The second is treating slack as private. Two activities on the same chain share it, so spending it on one leaves none for the other. And the third is assuming a critical activity is worth shortening indefinitely.

@chapter Try it
@words text="Shorten G by one" sub="does the project move?"
Your turn. In the nine activity project, G has one unit of slack. Suppose you shorten G by one day instead of C. Redo the forward pass and decide whether the finish date moves at all, and say why.

@end text="Run both passes yourself"
You can run both passes, shorten any activity, and watch where the curve goes flat, on Learn. That's learn dot get er done dot I O.
