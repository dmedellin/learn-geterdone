---
format: long
lesson: networks-flows-paths-and-assignments/maximum-flow-and-minimum-cut
title: Max flow, min cut: the cut that proves the flow is biggest
thumb: The cut is the proof
---

@chapter The question
@title text="Maximum Flow and Minimum Cut" sub="Networks, Flows, Paths and Assignments" art=thumb
How much can you push from a source to a sink, through arcs that each have a capacity? And once you've found a flow, how do you prove nobody can do better?

@art pipes-network
The lesson's network has four nodes and five arcs: s to a with capacity three, s to b with two, a to b with two, a to t with two, and b to t with three. Flow value is the net amount leaving the source.

@chapter Cuts
@art cut-line
A cut is a set of nodes holding the source but not the sink. Its capacity is the total capacity of the arcs leaving that set. Arcs running back in don't count. Every unit of flow has to cross every cut, so any cut bounds any flow.

@math heading="Every cut of this network" items="S = {s}:  3 + 2 = 5@just s;;S = {s, a, b}:  2 + 3 = 5@s, a and b;;S = {s, a}:  6@s and a;;S = {s, b}:  6@s and b"
Here are all four. Just s gives three plus two, five. S, a and b gives two plus three, also five. S and a gives six, and s and b gives six. So no flow can ever exceed five, and that's an addition, not an algorithm.

@chapter Augmenting paths
@art augmenting-path
Now find flow. Look for a path in the residual network: forward arcs where there's spare capacity, backward arcs where flow can be undone. Push the bottleneck along it, and repeat until no path remains.

@math heading="From nothing" items="s→a→b→t:  +2,  value 2@two;;s→a→t:  +1,  value 3@three;;s→b, back b→a, a→t:  +1,  value 4@backward;;s→b→t:  +1,  value 5@five"
First s, a, b, t, with a bottleneck of two. Then s, a, t, adding one, for three. Then s to b, backward from b to a, then a to t, for four. And finally s, b, t, for five. Then no residual path is left.

@art backward-arc
Look at that third path. There's no arc from b to a. What it does is un-send a unit that had gone from a to b, and reroute it to the sink. Without backward arcs, the algorithm would stop at four and confidently report it.

@chapter The cut comes free
@art reachable-set
When no path remains, take the nodes still reachable from the source in the residual network. Here that's just s. Every arc out of it is full, and every arc into it is empty. So the flow across it equals its capacity: three plus two, which is five.

@words text="max flow = min cut = 5"
A flow of five and a cut of five. Since no flow can beat any cut, both are optimal. That's max flow min cut. And the certificate costs nothing. It's the set the search already found when it failed.

@chapter Why a cut bounds a flow
@words text="A cut is a 0-1 dual point" sub="one variable per interior node, one per arc"
There's a deeper reason. The max flow programme has one row per interior node and one per arc, so its dual has a variable for each. Set the node variables to one inside the cut, and the arc variables to one on arcs leaving it. That point is dual feasible, and its objective is the cut's capacity.

@art two-min-cuts
So a cut bounding a flow is weak duality with different nouns. And minimum cuts needn't be unique. This network has two out of four. A six node instance has sixteen cuts, four of them minimum at seven. The theorem is about the number, not which set reaches it.

@chapter Where people slip
@list heading="Common slips" items="Counting arcs that run back into the cut@The first|Leaving out the backward arcs@The second|Reporting the flow and dropping the cut@And the third"
The first slip is counting arcs that run back into the cut. The second is leaving out the backward arcs, which makes the algorithm wrong, not just slow. And the third is reporting the flow and throwing away the cut, when the cut is the proof.

@chapter Try it
@words text="S = {s, b}" sub="which arcs leave it?"
Your turn. Take the cut s and b. List the arcs whose tail is inside and whose head is outside, add their capacities, and check you get six. Then say which arc, running back in, you were right to leave out.

@end text="Choose your own augmenting paths"
You can pick each augmenting path yourself and watch the cut appear, on Learn. That's learn dot get er done dot I O.
