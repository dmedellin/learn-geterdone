---
format: long
lesson: graph-algorithms/augmenting-paths
title: Augmenting paths: why max flow has to undo its choices
thumb: Maximal is not maximum
---

@chapter The question
@title text="Augmenting Paths" sub="Graph Algorithms" art=thumb
To push as much as possible through a network, keep finding a path with spare room and push along it. Simple. Except that, done naively, it gets stuck below the maximum. The fix is to let a path run backwards.

@chapter What a flow is
@art capacity-pipes
Every arc has a capacity. A flow puts a number on every arc, between zero and its capacity. And at every vertex except the source and the sink, what comes in equals what goes out. The value is what leaves the source.

@math heading="A flow" items="0 ≤ f(a) ≤ c(a)  on every arc@between zero;;in = out  at every vertex but s and t@what comes in"
Two constraints, both checkable. Each arc's flow is between zero and its capacity. And what comes in equals what goes out, everywhere but the source and the sink.

@chapter The residual network
@art residual
For an arc carrying f out of capacity c, the residual network has a forward arc with c minus f, how much more you can push. And a backward arc with f, how much of the existing flow you can take back. An augmenting path is any path from source to sink in that network.

@art bottleneck
Its bottleneck is the smallest residual capacity on it. Push that amount: add it on forward arcs, subtract it on backward ones. The result is a flow again, with a higher value.

@chapter Getting stuck
@math heading="1>2 1 · 1>3 1 · 2>3 1 · 2>4 1 · 3>4 1" items="backward arcs off:  path 1>2>3>4, push 1@backward arcs off;;then no path:  value 1@finds nothing;;backward arcs on:  1>3, back along 2>3, 2>4@Switch backward arcs on;;value 2@reaches two"
Here's the lab's four vertex network, source one, sink four, every capacity one. With backward arcs off, the first found rule takes one, two, three, four, and pushes one. Then it finds nothing. The value is stuck at one. Switch backward arcs on, and the same rule finds one to three, back along two to three, then two to four. It reaches two.

@art stuck-flow
Notice where it's stuck. The arc from one to three still has room, but the search only reaches one and three. Every forward route to four is already used.

@art undo
Look at what that second path did. It sent a new unit from one to three, cancelled the unit that was going two to three, and sent that one on to four instead. Two units arrive by two separate routes, and it only worked by rewriting an earlier decision.

@words text="maximal ≠ maximum"
The stuck flow is a perfectly legal flow. Every constraint holds. Nothing more can be pushed without taking something back. It's maximal. The maximum is two. Those two words differ by three letters, and by the whole content of this topic.

@chapter Choosing the path
@art thin-arc
Which path to take is a second question. On one to two and one to three at a hundred, a middle arc of one, and two to four and three to four at a hundred, both rules reach two hundred. The shortest path rule augments twice, a hundred each time.

@math heading="First-found rule" items="1 + 99 + 1 + 99 = 200@one, then ninety nine;;four augmentations@four times"
The first found rule augments four times: by one, then ninety nine, then one, then ninety nine. It walks into the thin arc, pays for it with a backward arc later, and does it twice.

@math heading="Six vertices, capacities 4 to 20" items="12 + 4 + 7 = 23@twelve, then four, then seven"
On a six vertex network, the shortest path rule reaches twenty three in three augmentations, pushing twelve, then four, then seven. The third path is four arcs long where the first two were three, because what's available changes as the residual network does.

@words text="23 measured · 'can't beat 23' not shown"
But here measurement and proof are furthest apart. Three augmentations reaching twenty three is a measurement. That twenty three can't be beaten isn't something more augmentations could show. Stopping only means this search found nothing. The next lesson supplies the proof.

@chapter Where people slip
@list heading="Common slips" items="Searching the original network, not the residual@The first|Taking a failed search as proof@The second|Dropping backward arcs because one rule coped@And the third"
The first slip is searching the original network instead of the residual one. It ends cleanly with a legal flow below the maximum, and nothing crashes. The second is reading a failed search as proof that no path exists. And the third is concluding backward arcs are unnecessary because one rule managed without them, on one network.

@chapter Try it
@words text="Push flow on the four-vertex network" sub="with backward arcs off, then on"
Your turn. On the four vertex network, push flow by hand with backward arcs off, and see where you get stuck. Then draw the residual network and find the path that runs backwards.

@end text="Undo a push"
You can switch backward arcs on and off and watch a stuck flow come unstuck, on Learn. That's learn dot get er done dot I O.
