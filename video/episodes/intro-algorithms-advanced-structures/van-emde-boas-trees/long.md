---
format: long
lesson: intro-algorithms-advanced-structures/van-emde-boas-trees
title: van Emde Boas trees: beating log n with integer keys
thumb: One recursive call per level
---

@chapter The limit
@title text="van Emde Boas Trees" sub="Introduction to Algorithms, Chapter 20" art=thumb
Binary heaps, red black trees and Fibonacci heaps all spend theta of log n on some operation, and they have to. If a structure that only compares keys could insert and extract the minimum faster, it could sort with fewer comparisons than the sorting lower bound allows.

@art bit-vector
Chapter twenty escapes the limit the way counting sort did, by using keys as indices. Assume the keys are distinct integers from zero to u minus one. Then every dynamic set operation can take O of log log u time in the worst case.

@chapter Split the key
@art clusters-and-summary
Divide the universe into the square root of u clusters, each holding the square root of u consecutive values. A summary records which clusters are nonempty, and it's itself a set over a universe of size root u.

@math heading="High, low and index" items="high(x) = ⌊x / √u⌋@high of x;;low(x) = x mod √u@low of x;;index(x, y) = x·√u + y@index"
High of x is the floor of x over root u, its cluster number: the upper half of its bits. Low of x is x mod root u, its position inside the cluster: the lower half. And index puts them back together.

@chapter The target
@math heading="The square-root recurrence" items="T(u) = T(√u) + O(1)@T of u equals;;m = lg u: S(m) = S(m/2) + O(1)@m equal to;;O(lg m) = O(lg lg u)@which is"
If an operation does constant work at a level and recurses once into a universe of root u, then T of u equals T of root u plus a constant. Set m equal to log u, and S of m equals S of m over two plus a constant, so O of log m, which is O of log log u.

@art halving-bits
Another way to see it: the number of bits in the universe size halves at each level. Sixteen bits, eight, four, two, one. Halving log u reaches one after log log u steps.

@chapter A near miss
@art two-calls
The proto van Emde Boas structure follows the plan literally: a summary and root u clusters, each a smaller copy. Membership drills straight down, and meets the target. But finding the minimum asks the summary for the first nonempty cluster, then asks that cluster too. Two calls a level.

@math heading="Two calls a level" items="T(u) = 2T(√u) + O(1) = Θ(lg u)@two calls;;insert: 2·lg u − 1 calls@an insertion;;u = 16: 7 · u = 256: 15 · u = 65,536: 31@seven at"
With two calls, the recurrence solves to theta of log u. An insertion always recurses into a cluster and into the summary, so it makes two log u minus one calls: seven at u equals sixteen, fifteen at two fifty six, thirty one at sixty five thousand five hundred thirty six.

@quote text="Clearly, we need to modify the proto-vEB structure to get each operation down to making at most one recursive call." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 20.2"
The authors end section twenty point two plainly. Clearly, we need to modify the proto v E B structure to get each operation down to making at most one recursive call.

@chapter The fix: min and max
@art min-kept-out
The van Emde Boas tree adds two fields at every level, min and max, with one twist: the minimum isn't stored in any cluster. Minimum and maximum now just read a field. Successor compares low of x with the max of x's cluster, so it knows which way to go, never both.

@words text="Insert: one call that recurses" sub="empty cluster: recurse into summary, fill cluster in O(1)"
Insert swaps x with min when x is smaller. Then, if x's cluster is empty, it recurses into the summary and fills the cluster in constant time. Otherwise the summary already knows, and it recurses into the cluster only. Delete can make two calls, but only when one of them is cheap.

@chapter The counts
@math heading="Same eleven operations" items="u = 16: 82 vs 31 calls@sixteen;;u = 256: 142 vs 37@two fifty six;;u = 65,536: 258 vs 38@sixty five thousand"
The lab runs the same eleven operations on both structures. At u equals sixteen, eighty two proto calls against thirty one. At two fifty six, a hundred forty two against thirty seven. At sixty five thousand five hundred thirty six, two fifty eight against thirty eight. The van Emde Boas totals barely move.

@art one-path-down
On that largest universe, every proto insertion makes thirty one calls, while the van Emde Boas insertions make at most four. One path down, instead of a branching tree of calls.

@chapter Where people slip
@list heading="Common slips" items="Reading it as lg lg n@in the number of elements|Thinking the split alone is enough@split alone|Treating min like the other elements@treating min"
Don't read the bound as log log n in the number of elements. It's in u, and the space is O of u too. Don't think the square root split alone gives the speed. And watch out for treating min like the other elements. It lives only in its field.

@chapter Try it
@words text="u = 16" sub="insert 3 · insert 14 · insert 8 · successor 3 · delete 3"
Your turn. With u equals sixteen, run insert three, insert fourteen, insert eight, successor three, delete three, by hand. Write high and low at every level, and count the calls.

@end text="Race the two structures"
You can run both structures side by side over universes up to sixty five thousand five hundred thirty six, on Learn. That's learn dot get er done dot I O.
