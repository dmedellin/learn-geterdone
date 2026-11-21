---
format: long
lesson: graphs-and-trees/trees
title: Trees: one definition, six equivalent descriptions
thumb: Connected, no cycles, n − 1 edges
---

@chapter The question
@title text="Trees" sub="Graphs and Trees" art=thumb
File systems, family trees, parse trees, search trees. They're all the same mathematical object. And one short definition turns out to force a whole list of other properties.

@chapter The definition
@art tree-forest
A tree is a connected graph with no cycles. A forest is a graph with no cycles, so each of its components is a tree. And a vertex of degree one is a leaf.

@list heading="Equivalent, on n vertices" items="a tree: connected and acyclic@a tree|connected with n − 1 edges@connected with|acyclic with n − 1 edges@acyclic with|exactly one path between every pair@exactly one path|connected, every edge a bridge@every edge is a bridge|acyclic, and any new edge makes one cycle@adding any edge"
Here's the theorem. For a graph on n vertices, these all say the same thing. It's a tree. It's connected with n minus one edges. It's acyclic with n minus one edges. Every pair is joined by exactly one path. It's connected and every edge is a bridge. And it's acyclic, but adding any edge creates exactly one cycle.

@chapter Why they agree
@art unique-path
Take a tree. It's connected, so there's at least one path between any two vertices. If there were two different ones, you could go out along one and come back along the other, and that's a cycle. So paths in a tree are unique.

@words text="Unique paths → every edge is a bridge"
And if the path is unique, then removing any edge u v leaves no way from u to v, because that edge was the only route. So every edge is a bridge. A tree has no redundancy at all.

@art longest-path-leaves
For the edge count, you need leaves. Every tree with at least two vertices has at least two. Take the longest path. Its end vertex can't have a neighbour off the path, or the path would be longer. And it can't have one further along it, or that would close a cycle. So it's a leaf, and so is the other end.

@math heading="Edges in a tree, by induction" items="n = 1:  0 edges@one vertex;;remove a leaf → n − 1 vertices, n − 2 edges@remove a leaf;;put it back → n − 1 edges@put the leaf back"
Now induct. A tree on one vertex has zero edges. For a bigger tree, remove a leaf. What's left is a tree on n minus one vertices, which by hypothesis has n minus two edges. Put the leaf back, and you have n minus one.

@art add-edge-cycle
So n minus one edges is exactly enough. Fewer, and the graph is disconnected. More, and there's a cycle. Add any edge to a tree, and you close exactly one cycle.

@chapter Is it a tree?
@math heading="Three graphs on 6 vertices, 5 edges each" items="A: 1–2, 2–3, 3–4, 4–5, 5–6 → connected → tree (a path)@Graph A;;B: 1–2, 1–3, 1–4, 1–5, 1–6 → connected → tree (a star)@Graph B;;C: 1–2, 2–3, 3–1, 4–5, 5–6 → two components, a cycle → not a tree@Graph C"
Three graphs, each with six vertices and five edges, which is n minus one. Graph A is a path, one to six. It's connected, so it's a tree. Graph B joins one to everything. Connected, so it's a tree, a star. Graph C is a triangle and a separate path. Two components, and a cycle.

@art path-star-cycle
The path has exactly two leaves, the minimum. The star has five. And graph C is the warning. It has the right edge count, and it's neither connected nor acyclic. So n minus one edges alone proves nothing.

@chapter Rooted and binary trees
@art rooted-tree
Pick one vertex as the root, and the tree gets structure. Every other vertex has a parent, toward the root, and children. A vertex's depth is its distance from the root, and the height is the largest depth.

@math heading="Binary trees" items="height h → at most 2ʰ⁺¹ − 1 vertices@height h;;n vertices → height ≥ log₂(n + 1) − 1@n vertices"
In a binary tree, each vertex has at most two children. One of height h has at most two to the h plus one, minus one vertices. So n vertices need height at least log base two of n plus one, minus one. That's why balanced search trees are fast.

@words text="Labelled trees on n vertices: nⁿ⁻²" sub="n = 4: 16 · n = 10: a hundred million"
And here's a surprise. Cayley's formula says there are n to the n minus two labelled trees on n vertices. That's sixteen for four vertices, and a hundred million for ten.

@chapter Where people slip
@list heading="Common slips" items="Using the edge count alone@The first|Thinking a rooted tree is a different graph@The second|Assuming a forest is a tree@And the third"
The first slip is using the edge count alone. The second is thinking a rooted tree is a different graph. Rooting just picks a vertex. And the third is forgetting that a forest needn't be a tree.

@chapter Try it
@words text="A tree on 12 vertices" sub="How many edges? What is its degree sum?"
Your turn. How many edges does a tree on twelve vertices have? And using the handshake theorem, what must its degrees add up to?

@end text="Check the characterisations yourself"
You can load all three graphs and check every condition yourself, on Learn. That's learn dot get er done dot I O.
