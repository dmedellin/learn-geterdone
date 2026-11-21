---
format: long
lesson: graph-algorithms/shortest-and-longest-paths-in-a-dag
title: Shortest and longest paths in a DAG, in one pass
thumb: One pass, either way
---

@chapter The question
@title text="Shortest and Longest Paths in a DAG" sub="Graph Algorithms" art=thumb
Longest path is a problem no algorithm on this course can solve on a general graph. On a graph with no cycles, it takes one pass. And the same pass finds the shortest path, negative weights and all.

@chapter One pass
@list heading="The DAG method" items="Topological order first; none means stop@topological order|Source 0, everything else ∞@Set the source|Visit in order, relax every arc out@Visit the vertices|Longest: flip the comparison@longest path"
Compute a topological order. If none exists, stop, because the graph has a cycle. Set the source to zero and everything else to infinity. Visit the vertices in order, and at each one relax every arc out of it. For the longest path, flip the comparison, and change nothing else.

@art tails-first
Why is one pass enough? Every arc of a shortest path points forwards in the order. So when v is reached, the vertex before it on that path was visited earlier, its label was already right, and the arc into v was relaxed from it. So d of v is final the moment you get there.

@words text="exactly E relaxations, whatever the weights"
Each arc is relaxed once, when its tail is visited. And nothing in that argument mentions the sign of a weight. A negative arc changes which number is smaller, not the order of the visits.

@chapter Seven arcs, two answers
@math heading="1>2 3 · 1>3 2 · 2>4 4 · 3>4 1 · 4>5 2 · 3>5 7 · 5>6 1" items="order:  1, 3, 2, 4, 5, 6@topological order;;shortest:  0, 3, 2, 3, 5, 6  via 1, 3, 4, 5, 6@shortest pass;;longest:  0, 3, 2, 7, 9, 10  via 1, 3, 5, 6@longest pass"
Here are seven arcs. A topological order is one, three, two, four, five, six. The shortest pass gives zero, three, two, three, five, six, in seven relaxations, by the route one, three, four, five, six. The longest pass gives zero, three, two, seven, nine, ten, by one, three, five, six.

@art no-cycle
The longest reading only works because there's no cycle. On a general graph, a positive cycle could be walked forever for profit. A DAG has nothing to go round, so the longest path is finite and the same argument goes through.

@chapter Slack
@art critical-path
Read the longest reading as a project. Each arc is a task with a duration, each vertex a milestone. The longest distance to a vertex is the earliest it can happen. Work backwards from the end to find the latest it may happen. The difference is the slack.

@art backward-pass
The backward pass has three details, and getting any wrong still gives plausible numbers. Seed it only at the far end, at the far end's own time. Under the longest reading, take a minimum over successors. And subtract the arc's way round: the head's latest, minus the weight.

@math heading="Wide preset" items="longest:  0, 5, 10, 7, 11, 15@the longest distances;;slack:  0, 0, 0, 1, 1, 0@the slack"
On the lab's wide preset, the longest distances are zero, five, ten, seven, eleven, fifteen. The slack is zero, zero, zero, one, one, zero. The route through four and five finishes at fourteen, where the critical route takes fifteen, so those two milestones can each slip by one.

@art slack-bars
On the opening project, every vertex has slack zero under the longest reading, because every vertex is on a critical path. And slack is never negative, which is a free check that the backward pass was done right.

@chapter Where settling fails
@math heading="1>2 2 · 1>3 3 · 3>2 −2 · 2>4 1" items="one pass:  0, 1, 3, 2@the one pass;;rounds method:  0, 1, 3, 2@rounds method;;nearest-first:  0, 1, 3, 3@nearest first"
Four vertices, one negative arc. The order is one, three, two, four, and the one pass gives zero, one, three, two. The rounds method agrees. But nearest first gives zero, one, three, three. It settled vertex two at two, relaxed out of it, then two improved to one, too late.

@art cycle-refused
And on a graph with a cycle, there's no topological order, so the lab returns no distances at all. Negate the weights of a cycle and it becomes a negative cycle, which the rounds method reports. A longest walk round a cycle just doesn't exist.

@chapter Where people slip
@list heading="Common slips" items="Running the pass on a graph with a cycle@The first|Believing a DAG can't have negative weights@The second|Computing slack forwards@And the third"
The first slip is running the pass on a graph with a cycle, instead of refusing. The second is believing a DAG can't have negative weights. It forbids cycles, not negative numbers. And the third is computing slack forwards. It's about what comes after, so it runs backwards.

@chapter Try it
@words text="Compute slack on the wide preset" sub="backward pass, seeded at vertex 6"
Your turn. On the wide preset, run the backward pass by hand, seeded only at vertex six. Find the latest time for every milestone, and check the slack comes out zero, zero, zero, one, one, zero.

@end text="Find the critical path"
You can flip between shortest and longest and read the slack off one pass, on Learn. That's learn dot get er done dot I O.
