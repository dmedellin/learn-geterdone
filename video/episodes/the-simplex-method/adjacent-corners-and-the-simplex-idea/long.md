---
format: long
lesson: the-simplex-method/adjacent-corners-and-the-simplex-idea
title: The simplex idea: walk the edges, uphill, and stop
thumb: One column in, one out
---

@chapter The question
@title text="Adjacent Corners and the Simplex Idea" sub="The Simplex Method" art=thumb
A linear programme can have a huge number of corners. Trying them all is hopeless. So how does the simplex method find the best one without visiting most of them?

@art corner-path
It walks. It starts at a corner, moves along an edge to a better neighbour, and repeats. It never enters the interior, and it never takes a census of every corner.

@chapter A basis names a corner
@words text="basis = m columns" sub="every other variable at zero"
In standard form, with m equations, a basis is a choice of m columns whose matrix is invertible. Set every other variable to zero, solve for the basic ones, and you get one point. If all the basic variables come out at least zero, that point is a corner.

@math heading="The example" items="maximise 3x₁ + 5x₂@maximise;;x₁ ≤ 4@plant A;;2x₂ ≤ 12@plant B;;3x₁ + 2x₂ ≤ 18@plant C"
Here's the example. Maximise three x one plus five x two. Plant A hours give x one at most four. Plant B gives two x two at most twelve. Plant C gives three x one plus two x two at most eighteen. One slack per row.

@math heading="Five corners, five bases" items="(0, 0):  {s₁, s₂, s₃},  z = 0@zero, zero;;(0, 6):  {s₁, x₂, s₃},  z = 30@zero, six;;(2, 6):  {s₁, x₂, x₁},  z = 36@two, six;;(4, 0):  {x₁, s₂, s₃},  z = 12@four, zero;;(4, 3):  {x₁, s₂, x₂},  z = 27@four, three"
The region has five corners, each with its basis. Zero, zero stands on the three slacks, with z zero. Zero, six on s one, x two, s three, worth thirty. Two, six on s one, x two, x one, worth thirty six. Four, zero, worth twelve. And four, three, worth twenty seven.

@art five-bases
Notice that nothing in the definition of a basis mentions the objective. A basis is a choice of columns, and the point follows from the choice. The objective only decides which of these points you want.

@words text="Start: all slacks"
Notice the origin's basis is just the three slacks. That's what makes the origin a free starting corner when every row is at most.

@chapter Adjacent bases
@art one-swap
Two bases are adjacent when they differ in exactly one column. Then the corners they name are the two ends of one edge. And one pivot moves between them: one column enters the basis, one leaves.

@math heading="From the origin" items="{s₁, s₂, s₃} → {s₁, x₂, s₃}:  one change ✓@x two in;;{s₁, s₂, s₃} → {x₁, s₂, s₃}:  one change ✓@x one in;;{s₁, s₂, s₃} → {x₁, s₂, x₂}:  two changes ✗@two changes"
From the origin, swap s two for x two, x two in, and you're one step away. Swap s three for x one, x one in, also one step. But four, three needs x one and x two in, and s one and s three out. That's two changes, so no single pivot goes there.

@art diagonal-square
And adjacency is arithmetic on sets, not a look at the picture. On a square, the opposite corners differ in two columns, however short the diagonal looks.

@chapter The walk
@math heading="The path" items="(0, 0),  z = 0@from the origin;;(0, 6),  z = 30@thirty;;(2, 6),  z = 36@thirty six;;every edge out lowers z: stop@stops"
From the origin, the method takes the edge to zero, six, raising z to thirty. Then the edge to two, six, raising it to thirty six. At two, six every edge out lowers z, so it stops. Two pivots, three corners visited, two never examined.

@chapter The licence to stop
@art plane-on-region
Why is it allowed to stop? A linear objective on a convex region has no local maximum that isn't global. So checking the edges at one corner tells you something about every point of the region.

@art hill-vs-plane
That's what separates this from hill climbing. On an arbitrary surface, walking uphill only finds a local summit. Here the surface is a plane and the region has no dents. A corner that beats its neighbours beats everything.

@words text="5 choose 3 = 10 choices, 5 corners, 3 visited"
And it explains why corners aren't the work. Five columns give ten ways to choose three, and five of those are corners here. The method visited three.

@chapter Where people slip
@list heading="Common slips" items="Searching over all the corners@The first|Calling corners adjacent because they look close@The second|Reading the basis as the non-zero variables@The third"
The first slip is thinking the method searches all the corners. It follows one path. The second is calling corners adjacent because they look close. The third is reading the basis as whichever variables aren't zero. Where three boundaries meet, a basic variable is zero too, and two bases name one point. That's degeneracy, coming later.

@end text="Walk the path, one swap at a time"
You can pick bases, try exchanges, and walk the simplex path yourself, on Learn. That's learn dot get er done dot I O.
