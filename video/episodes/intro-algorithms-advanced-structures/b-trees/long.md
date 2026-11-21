---
format: long
lesson: intro-algorithms-advanced-structures/b-trees
title: B-trees: why a search tree on disk grows at the top
thumb: Wide nodes, short trees
---

@chapter The disk problem
@title text="B-Trees" sub="Introduction to Algorithms, Chapter 18" art=thumb
Chapter eighteen designs a search tree for data that lives on disk, where reading a page costs far more than looking at what's on it.

@art disk-vs-memory
The authors put numbers on the gap. One rotation of a seventy two hundred RPM disk takes eight point three three milliseconds. A memory access takes roughly fifty nanoseconds. So a disk reads and writes whole pages at once, and the chapter counts those page reads and writes apart from the computing time.

@words text="1 node = 1 disk page" sub="DISK-READ before use · DISK-WRITE after change"
A node is as large as a page. It has to be brought in with a disk read before you touch it, and saved with a disk write after it changes. The root stays in memory, so it's never read, though it's written whenever it changes.

@chapter What a B-tree is
@art wide-node
A B-tree has a minimum degree, t, of at least two. Each node keeps its keys in order, and an internal node with k keys has k plus one children, with the keys separating the ranges below them.

@list heading="The rules" items="Every leaf at the same depth@same depth|Non-root node: t − 1 to 2t − 1 keys@every node other than the root|Root: at least one key@the root"
Every leaf sits at the same depth, the height h. Every node other than the root holds between t minus one and two t minus one keys. And a nonempty tree's root has at least one. With t equal to two, you get a two three four tree.

@chapter The height theorem
@math heading="Fewest keys at height h" items="depth 1: ≥ 2 nodes@depth one;;depth h: ≥ 2·tʰ⁻¹ nodes, each ≥ t − 1 keys@depth h;;n ≥ 2·tʰ − 1@add these up;;h ≤ log_t((n + 1)/2)@so h is at most"
Count the fewest keys at height h. Depth one has at least two nodes. Depth h has at least two t to the h minus one, each with at least t minus one keys. Add these up: n is at least two t to the h, minus one. So h is at most log base t of n plus one, over two, theorem eighteen point one.

@words text="16 keys" sub="t = 2: height ≤ 3 · t = 3: height ≤ 1"
Read it the other way. At t equal to two, height four needs thirty one keys, so sixteen keys give height at most three. At t equal to three, height two needs seventeen, so sixteen keys allow height at most one. The base of the logarithm is t, and t can be in the thousands.

@chapter Insert in one pass
@art split-median
A new key always goes into an existing leaf, and a full leaf can't take it. A full node of two t minus one keys is split around its median. Each half keeps t minus one keys, and the median moves up into the parent.

@art split-on-the-way-down
But what if the parent is full too? Rather than climb back up, the insert procedure splits every full node it meets on the way down. Every node it steps into has room, so the whole insertion is one pass from root to leaf.

@art grows-at-the-top
When the root is full, a new empty root goes above it and the old one splits. That's the only way the height grows.

@quote text="Unlike a binary search tree, a B-tree increases in height at the top instead of at the bottom." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 18.2"
As the authors put it, unlike a binary search tree, a B-tree increases in height at the top instead of at the bottom.

@chapter Counting disk work
@words text="1 read per step · 1 write per key · 3 writes per split"
Stepping into a child costs one read, writing the key costs one write, and each split costs three writes.

@math heading="16 keys, one shuffled order" items="t = 2: 6 splits · 20 reads · 34 writes · height 2@t equal to two;;34 = 16 leaf writes + 3 × 6@sixteen leaf writes;;t = 3: 3 splits · 11 reads · 25 writes · height 1@t equal to three;;t = 5: 1 split · 3 nodes · height 1@at t equal to five"
With sixteen keys at t equal to two, you get six splits, twenty reads, and thirty four writes, which is sixteen leaf writes plus three for each split, at height two. At t equal to three, three splits, eleven reads, twenty five writes, height one. And at t equal to five, one split leaves three nodes at height one.

@art bigger-t-shorter
A larger t means fewer, fuller pages and a lower tree. That's the whole reason for the structure.

@chapter Deleting, briefly
@words text="Deletion mirrors insertion" sub="make each child hold ≥ t keys before descending"
Section eighteen point three sketches deletion. Before it steps into a child, it makes sure that child has at least t keys, one more than the minimum, by borrowing from a sibling or merging. When the root runs out of keys, it's removed, and the tree loses a level at the top.

@chapter Where people slip
@list heading="Common slips" items="Expecting height about lg n@The first|Picturing growth at the leaves@The second|Pricing by comparisons@the third"
The first slip is expecting the height to be about log base two of n. The base is t, and t is large. The second is picturing the tree growing downward at its leaves. It only grows a new root. And the third is pricing operations by comparisons, when the cost that counts is pages read and written.

@chapter Try it
@words text="12, 3, 7, 18, 25, 1, 9, 15, 21, 30" sub="t = 2 · split full nodes on the way down"
Your turn. Insert twelve, three, seven, eighteen, twenty five, one, nine, fifteen, twenty one, thirty, in that order, into an empty B-tree with t equal to two. Draw the tree after each split, and count the splits, reads, and writes.

@end text="Grow a B-tree and count its pages"
You can grow bigger trees and count every split, read, and write against the height theorem, on Learn. That's learn dot get er done dot I O.
