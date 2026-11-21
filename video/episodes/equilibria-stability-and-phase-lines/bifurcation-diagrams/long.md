---
format: long
lesson: equilibria-stability-and-phase-lines/bifurcation-diagrams
title: Bifurcation diagrams: forks, crossings and vanishing pairs
thumb: A stack of phase lines
---

@chapter The question
@title text="Bifurcation Diagrams" sub="Equilibria, Stability and Phase Lines" art=thumb
When a parameter changes, how do the equilibria change with it? One picture shows the whole story. Put the parameter across, the equilibria up, and read off forks and crossings at a glance.

@chapter A stack of phase lines
@art stacked-lines
A bifurcation diagram puts the parameter a along the horizontal axis and the equilibria up the vertical one. Cut it with a vertical line at one value of a, and the crossings are that equation's equilibria. So each vertical slice is a phase line.

@words text="solid = stable    dashed = unstable"
Stable branches are drawn solid, and unstable ones dashed. That's the sign of f prime, the slope that classified each equilibrium. A branch changes style where its slope passes through zero, which is where it meets another branch.

@chapter The pitchfork
@math heading="y′ = a·y − y³ = y·(a − y²)" items="equilibria:  0,  and ±√a for a > 0@zero for every a;;f′(y) = a − 3y²@slope in y;;f′(0) = a,   f′(±√a) = −2a@at zero it's a"
Take y prime equals a y minus y cubed, which is y times a minus y squared. The equilibria are zero for every a, and plus or minus root a when a is positive. The slope in y is a minus three y squared. At zero it's a, and at the other two it's a minus three a, minus two a.

@math heading="Three slices" items="a = −1:   0 stable@minus one;;a = 0:   slope 0, use the signs@At zero;;a = 4:   −2 stable,  0 unstable,  2 stable@At four"
For negative a, like minus one, zero is the only equilibrium, and it's stable. At zero the slope is zero, so you use the signs. For positive a, zero turns unstable, and the pair plus or minus root a appears, both stable. At four, that's minus two and two, with slope minus eight, and zero with slope four.

@art pitchfork
So the diagram is a solid line for negative a, then a dashed line for positive a, with two solid arms leaving it. A fork opening to the right.

@art pitchfork-slice
Slice it at a equals four. The line crosses at minus two, zero and two, the outer two solid, the middle dashed. The arrows go up, down, up, down. So a start above zero goes to two, and one below goes to minus two. At minus one, the slice crosses once, and everything goes to zero.

@chapter The crossing
@math heading="y′ = a·y − y² = y·(a − y)" items="equilibria:  0  and  a@zero and a;;f′(0) = a,   f′(a) = −a@slope is;;a = 2:   0 unstable,  2 stable@At a equals two;;a = −2:   0 stable,  −2 unstable@At minus two"
Now a y minus y squared, which is y times a minus y. The equilibria are zero and a, for every a. The slope is a minus two y, so it's a at zero and minus a at a. At a equals two, zero is unstable and two is stable. At minus two, it's the other way round.

@art transcritical
The two branches pass through each other at a equals zero, and trade stability there. The count goes two, one, two. No equilibrium vanishes. One passes through the other. That's a transcritical shape, not a saddle node.

@chapter Three shapes
@art saddle-node
And a plus y squared is the third. Its two branches, of opposite type, meet at a equals zero and vanish. That's a saddle node.

@art three-shapes
So three shapes carry the story here. In a saddle node, a pair meets and vanishes. In a transcritical shape, two branches cross and swap stability. In a pitchfork, one branch changes type and two new ones spring from it.

@list heading="As a rises through 0" items="a + y²:   two → none@a plus y squared|a·y − y³:   one → three@a y minus y cubed|a·y − y²:   two → two@a y minus y squared"
So as a rises through zero, a plus y squared goes from two equilibria to none. a y minus y cubed goes from one to three. And a y minus y squared has two on both sides. Nothing about a parameter makes the count grow or shrink. The shape of f does.

@chapter Where people slip
@list heading="Common slips" items="Thinking the count only goes up@The first|Reading a branch as a solution in time@The second|Treating a dashed branch as not a solution@The third"
The first slip is thinking the count can only go up as a increases. The second is reading a branch as a solution plotted against time. The horizontal axis is a, fixed for each solution. The third is treating a dashed branch as not a solution. At a equals four, y equals zero solves the equation exactly. Dashed means unstable.

@chapter Try it
@words text="y′ = a·y − y²" sub="slice at a = 2 and a = −2"
Your turn. For a y minus y squared, draw the slices at a equals two and a equals minus two. Mark each equilibrium solid or dashed from its slope, then say where a start at one goes in each.

@end text="Read the diagram slice by slice"
You can sweep a across all three families and watch each diagram form, on Learn. That's learn dot get er done dot I O.
