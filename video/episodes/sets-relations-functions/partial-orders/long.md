---
format: long
lesson: sets-relations-functions/partial-orders
title: Partial orders and Hasse diagrams: ranking without a total ranking
thumb: Some pairs can't be compared
---

@chapter The question
@title text="Partial Orders" sub="Sets, Relations and Functions" art=thumb
Take an equivalence relation and swap one property: symmetry out, antisymmetry in. The structure changes completely. Instead of grouping elements into classes, the relation ranks them.

@words text="reflexive + antisymmetric + transitive"
A partial order is reflexive, antisymmetric and transitive. A set with a partial order is called a poset. Antisymmetry is what makes it an order: distinct elements never relate both ways, so nothing gets folded together.

@chapter Partial, not total
@art total-ladder
Two elements are comparable when one is below the other. If every pair is comparable, it's a total order, like the integers under less than or equal. Every element sits on one ladder.

@list heading="Four posets" items="(ℤ, ≤) : total@the integers|(P(S), ⊆) : partial@subsets|divisibility : partial@divisibility|alphabetical order : total@alphabetical"
But the integers are the exception. Subsets under subset are partial: one and two, as sets, are incomparable, since neither contains the other. Divisibility is partial too: neither two nor three divides the other. Alphabetical order on words is total. Incomparable pairs are the normal case, not a defect.

@chapter Hasse diagrams
@art implied-edge
Drawing every pair of a partial order is unreadable, and most pairs are forced anyway. A Hasse diagram draws only what's not forced. Put b above a when a comes first, and draw an edge only when b covers a, with nothing strictly between.

@list heading="Hasse rules" items="No loops@no loops|No arrowheads@no arrowheads|No implied edges@no implied edges"
So: no loops, because reflexivity is assumed. No arrowheads, because height shows direction. And no implied edges, because transitivity supplies them. To recover the full order, a is below b exactly when an upward path leads from a to b.

@chapter Divisors of twelve
@math heading="a ≼ b when a | b, on {1, 2, 3, 4, 6, 12}" items="1 ≺ 2   1 ≺ 3@one is covered;;2 ≺ 4   2 ≺ 6   3 ≺ 6@two is covered;;4 ≺ 12   6 ≺ 12@twelve covers"
Take divisibility on one, two, three, four, six and twelve. One is covered by two and by three. Two is covered by four and six, and three by six. And twelve covers four and six.

@art hasse-divisors
So the diagram has one at the bottom, then two and three, then four and six, and twelve at the top. There's no edge from one to four, even though one divides four, because it's implied by going through two.

@math items="least: 1@one divides everything;;greatest: 12@everything divides twelve;;incomparable: 4 and 6,  3 and 4,  2 and 3@incomparable"
One divides everything, so it's the least element. Everything divides twelve, so it's the greatest. And the incomparable pairs are four and six, three and four, and two and three.

@chapter Minimal versus least
@art two-minimal
Minimal means nothing is strictly below it. Least means it's below everything. In a partial order these come apart. In two, three, four, six under divides, both two and three are minimal, and there's no least element, because neither divides the other.

@words text="a ≼ b and b ≼ a ⟹ a = b"
A least element is unique when it exists. If a and b were both least, a would be below b and b below a, and antisymmetry makes them equal. That's where antisymmetry earns its place. It also means a least element is the only minimal one, so a poset with three minimal elements has no least element at all.

@chapter Topological sort
@art line-up
A topological sort lists the elements of a finite poset so that each appears after everything below it. It extends the partial order to a total one, and every finite poset has one. Build systems, course prerequisites and spreadsheet recalculation all do exactly this. A depth first search finds one, and it fails exactly when the dependencies contain a cycle.

@chapter Where people slip
@list heading="Common slips" items="Confusing minimal with least@The first|Drawing implied edges@The second|Assuming every poset is total@the third"
The first slip is confusing minimal with least. Minimal is about what's below it, least is about everything. The second is drawing implied edges in a Hasse diagram. With them, it's just the relation, unreduced. And the third is assuming every poset is a total order. Subsets, divisibility and task dependencies are all partial.

@chapter Try it
@art subset-cube
Your turn. Draw the Hasse diagram of the subsets of a three element set: eight vertices in four levels, with edges only between sets that differ by one element. Then find the least, the greatest, and an incomparable pair in the middle.

@end text="Divisibility is a partial order"
You can check that divisibility is a partial order, and see which pairs stay incomparable, on Learn. That's learn dot get er done dot I O.
