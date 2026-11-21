---
format: long
lesson: graph-algorithms/negative-weights-and-bellman-ford
title: Bellman-Ford: negative weights, and the cycle as evidence
thumb: Return the cycle, not a flag
---

@chapter The question
@title text="Negative Weights and Bellman–Ford" sub="Graph Algorithms" art=thumb
Give Dijkstra a negative arc and it quietly returns a wrong number. Bellman Ford gets it right, and when no right answer exists, it hands you the reason: the negative cycle itself.

@chapter The algorithm
@list heading="Bellman–Ford" items="Source 0, everything else ∞@Set the source|V − 1 rounds: relax every arc once@Repeat|Stop early if a round changes nothing@Stop early|One more round: any change means a negative cycle@one more round"
Set the source to zero and everything else to infinity. Then repeat V minus one times: relax every arc, once, in whatever order they're stored. Stop early if a round changes nothing. Then do one more round. If anything still improves, there's a negative cycle.

@art rounds
Nothing is ever settled. Every arc is relaxed in every round, so a label that improves late still spreads. That's exactly why negative arcs are survivable here.

@chapter Why V − 1 rounds
@words text="After round i: every shortest path of ≤ i arcs is correct"
Here's the invariant. After i rounds, every vertex whose shortest path uses at most i arcs has the right label.

@list heading="Induction" items="i = 0: just the source@For i equals zero|Prefix to u is right after round i@The prefix|Round i + 1 relaxes u → v@Round i plus one"
For i equals zero, that's just the source. Now take a shortest path to v with i plus one arcs. The prefix to u is a shortest path with i arcs, so d of u is right after round i. Round i plus one relaxes the arc from u to v, so d of v becomes right too.

@art no-repeat
And a shortest path never repeats a vertex. Cutting out a repeated stretch can't make it longer, unless that stretch was negative, and then no shortest path exists at all. So V minus one arcs is the most any shortest path has.

@chapter Five vertices
@math heading="Ten arcs, four negative, from 1" items="round 1:  0, 2, 7, 4, 2@first round;;round 2:  0, 2, 7, 4, −2@the second;;round 3:  no change, stop@third round"
Here's the lab's graph: five vertices, ten arcs, four of them negative. The first round reaches zero, two, seven, four, two. The second improves only vertex five, to minus two. The third round changes nothing, so it stops, after three rounds and thirty relaxations.

@art late-improvement
Vertex five is the late one. It moved from two to minus two in round two, and because every arc is relaxed again, that improvement can keep spreading.

@art settle-fails
Floyd's all pairs method agrees. But the nearest first schedule on the same graph returns two for vertex five. Right shape of answer, wrong number, because it settled five too early.

@words text="route to 2: 1, 3, 4, 2 = 7 − 3 − 2 = 2"
The route to vertex two is one, three, four, two, three arcs, at seven minus three minus two, which is two. Its label was final after the first round, because the arcs happened to be swept in an order that carried it all the way.

@chapter Order changes the rounds
@math heading="Chain of five arcs, weight 1 each" items="typed backwards:  6 rounds,  20 relaxations@Type it backwards;;typed forwards:  2 rounds,  10 relaxations@forwards"
Take a chain of five arcs, each of weight one. Type it backwards, and each round pushes the frontier just one arc. Six rounds, twenty relaxations. Type it forwards, and one sweep carries it the whole way. Two rounds, ten relaxations. Same distances, zero to five.

@art chain-orders
So the round count belongs to the graph and the arc order together. And the backwards chain needs every one of its rounds, which is why the bound is V minus one, and nothing smaller. The bound is order V times E, and it's attained.

@chapter The certificate
@art negative-cycle
Now one to two at one, two to three at minus three, three to four at one, and four to two at one. All four rounds run, and the last still changes something. The labels it shows, zero, minus three, minus five, minus four, aren't distances. They're one more lap round a loop.

@math heading="The cycle, returned" items="2 → 3 → 4 → 2@two, three, four;;−3 + 1 + 1 = −1@minus one"
So it returns the cycle instead: two, three, four, back to two. Its weight is minus three plus one plus one, minus one. Every lap subtracts one more. Walk the predecessor pointers back from a vertex that moved, and you land inside it.

@words text="A cycle is actionable. A flag isn't."
A flag saying negative cycle leaves you nowhere to go. The cycle names the loop to break, or the arc whose sign was typed wrong.

@chapter Where people slip
@list heading="Common slips" items="Stopping at V − 1 rounds and trusting the labels@The first|Treating rounds needed as a graph property@The second|Treating no settling as waste@And the third"
The first slip is stopping at V minus one rounds and reporting the labels. With a negative cycle, they look fine and mean nothing. The second is quoting the rounds needed as a property of the graph, when it depends on the arc order. And the third is treating the lack of settling as an inefficiency. It's the whole reason this works.

@chapter Try it
@words text="Type the chain in a mixed order" sub="count the rounds"
Your turn. Type the five arc chain in a mixed order, neither forwards nor backwards. Predict how many rounds it needs, then run it and see.

@end text="Find the negative cycle"
You can sweep the rounds one at a time and get a negative cycle back as the cycle, on Learn. That's learn dot get er done dot I O.
