---
format: long
lesson: intro-algorithms-advanced-structures/disjoint-sets
title: Disjoint sets: union by rank and path compression
thumb: Two tiny rules, nearly linear
---

@chapter Three operations
@title text="Disjoint Sets" sub="Introduction to Algorithms, Chapter 21" art=thumb
Chapter twenty one is about a structure whose code is almost nothing, and whose analysis takes a whole starred section.

@list heading="The interface" items="MAKE-SET(x)@make set|UNION(x, y)@union|FIND-SET(x)@find set"
There are three operations. Make set creates a set whose only member is x, so x is its representative. Union replaces the sets holding x and y with their union. And find set returns the representative of x's set.

@art components
The section's application is connected components. Make a set for each vertex, and unite the two ends of every edge. Two vertices are in the same component exactly when their finds agree. That pays off when the edges arrive one at a time.

@chapter Linked lists first
@art linked-lists
Section twenty one point two keeps each set as a linked list, with the head as representative. A union appends one list to the other, and every appended object must update its pointer back to the set. Append carelessly onto a singleton every time, and the cost is theta of n squared.

@math heading="Weighted union" items="append the shorter list@always append the shorter;;each change at least doubles the set@at least doubles;;O(m + n lg n)@m plus n log n"
The fix is weighted union: always append the shorter list. Then each time an object's pointer changes, its set at least doubles, so no pointer changes more than log n times. Theorem twenty one point one: m operations take O of m plus n log n.

@chapter Forests
@art forest
Section twenty one point three keeps each set as a tree. Every node points to its parent, and the root, its own parent, is the representative. Find follows the pointers up. Union makes one root point at the other. Done naively, unions can build a single path of n nodes.

@art union-by-rank
The first heuristic is union by rank. Each root carries a rank, an upper bound on its height. Link the root of smaller rank under the larger. If the ranks are equal, pick one as parent and add one to its rank.

@quote text="The second heuristic, path compression, is also quite simple and highly effective." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 21.3"
The second heuristic, path compression, is also quite simple and highly effective.

@art path-compression
Find climbs to the root, and on the way back down it points every node on the path straight at the root. Ranks aren't changed, so afterwards a rank may overstate a height.

@chapter The bound
@math heading="m operations" items="union by rank alone: O(m lg n)@rank alone;;both together: O(m α(n))@together"
Union by rank alone gives O of m log n, and that's tight. Together, the two heuristics give O of m times alpha of n.

@math heading="Section 21.4: the inverse α" items="A_k(1), k = 0…3: 2, 3, 7, 2047@two, three, seven;;A₄(1) > 2²⁰⁴⁸ ≫ 10⁸⁰@beyond;;α(n) ≤ 4 for n ≤ A₄(1)@alpha of n is at most four"
Alpha comes from a family of functions, each level repeating the one below. At j equal to one they give two, three, seven, two thousand forty seven, then a number beyond two to the two thousand forty eight, more than the atoms in the observable universe. So alpha of n is at most four for any n you'll meet.

@chapter The lab's chain
@art tall-chain
The lab's chain unites each element with the next, zero with one, one with two, and so on, then finds every element. With both rules off, that builds a single path.

@math heading="Chain of 12: 11 unions, then 12 finds" items="neither rule: 66 hops, worst find 11@neither;;union by rank: 20 hops, worst 1@rank alone;;compression: 21 hops, worst 11@compression alone;;both: 20 hops, worst 1@both"
With neither rule, the twelve elements walk sixty six pointer hops, with a worst find of eleven. Union by rank alone cuts that to twenty hops, worst find one. Compression alone gives twenty one, but its first find still walks all eleven. Both give twenty.

@words text="star: 11 hops in every combination" sub="depth 1 · nothing to save"
On the star pattern, where everything is united straight into element zero, every combination walks eleven hops. The trees have depth one, and the rules save nothing, because there was nothing to save.

@chapter Where people slip
@list heading="Common slips" items="Reading O(m α(n)) as a constant-time find@The first|Taking rank for height@The second|Linking without looking@the third"
The first slip is reading the bound as a constant time find. It's amortized over the whole sequence. The second is taking rank for the height. Compression flattens trees and never lowers a rank. And the third is linking without looking at the trees, which can build a single path.

@chapter Try it
@words text="UNION(1,2) (3,4) (1,3) (5,6) (7,8) (5,7) (2,8) · FIND-SET(1)" sub="union by rank · path compression"
Your turn. Take elements one to eight, with both heuristics. Run the seven unions shown, then find set of one. Draw the forest with ranks after each union, and say where one and two point afterwards.

@end text="Switch the heuristics on and off"
You can turn each rule on and off and count every pointer hop, on Learn. That's learn dot get er done dot I O.
