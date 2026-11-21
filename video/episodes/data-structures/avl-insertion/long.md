---
format: long
lesson: data-structures/avl-insertion
title: AVL insertion: the four cases and the one fix that suffices
thumb: Two turns decide the case
---

@chapter The question
@title text="AVL Insertion" sub="Data Structures" art=thumb
Insert one through ten in order into a plain search tree, and you get a path of height nine. Insert them into an AVL tree, and the height is three. Here's how it stays balanced, one insertion at a time.

@chapter Insert, then walk back
@art walk-back
Insert exactly as in a plain search tree. Walk to where the search fails, and attach a leaf. Then walk back up the path, updating heights. Only the new key's ancestors changed height, so only they can be out of balance.

@words text="Fix the lowest unbalanced ancestor" sub="balance factor +2 or −2"
If some node's balance factor reaches plus two or minus two, rebalance there, and stop. The lowest such node is the one to fix, and you'll only need one fix.

@chapter The outside cases
@art single-rotation
Say node z has balance plus two, and the new key went into the left subtree of z's left child. That's the L L case. One right rotation at z fixes it. The left child rises, z drops to its right, and the sides come out equal. R R is the mirror, fixed by one left rotation.

@math heading="LL: keys 30 20 10" items="30 has balance +2@thirty has;;rotate right at 30@rotate right;;root 20, children 10 and 30@twenty"
Insert thirty, twenty, ten. Thirty has balance plus two, with the new key on the outside. Rotate right at thirty, and twenty becomes the root, with ten and thirty as its children.

@chapter The inside cases
@art single-fails
Now say z is plus two, but the new key went into the right subtree of z's left child. That's L R. One right rotation at z lifts the child, but the offending subtree lands back on z's left, and now the tree leans minus two the other way.

@math heading="LR: keys 30 10 20" items="rotate 10 left:  30 → 20 → 10@rotate ten left;;rotate 30 right:  root 20, children 10 and 30@then rotate thirty"
So rotate twice. Insert thirty, ten, twenty. First rotate ten left, which turns L R into L L. Then rotate thirty right. Twenty ends up as the root. A double rotation always lifts the inner grandchild two levels.

@art double-rotation
R L is the mirror. Rotate the child right, then z left. And notice, on these three key examples, L L, L R and R L all end at the same tree: twenty, with ten and thirty. Same shape, three different routes.

@list heading="Two turns decide the case" items="LL: rotate right@L L|RR: rotate left@R R|LR: left, then right@L R|RL: right, then left@R L"
The rule is about two turns. From the unbalanced node to its taller child, and from that child toward the new key. Same direction twice, L L or R R, needs one rotation. Different directions, L R or R L, need two.

@art four-cases
So there are four shapes. Two straight lines, which need one rotation, and two zigzags, which need two. Spot the shape, and you know the fix.

@chapter Why one fix is enough
@words text="height h → h + 1 → back to h"
Before the insert, the subtree at the unbalanced node had height h. The insert made it h plus one, which unbalanced it. Both kinds of rotation bring it back to h. So nothing above it changed height, and every ancestor is exactly as balanced as before.

@chapter Measured
@math heading="keys 1 … 10, in order" items="AVL:  height 3,  6 rebalances,  25 comparisons@the AVL tree;;plain BST:  height 9@the plain tree;;N(3) = 7 ≤ 10 < N(4) = 12  ⟹  h ≤ 3@N of three"
Now insert one to ten in order. The AVL tree ends at height three, with six rebalances and twenty five comparisons. The plain tree reaches nine. And the table bound is three, since N of three is seven and N of four is twelve. The tree reaches it.

@art path-vs-avl
Every one of the six fixes is R R, because every key arrives bigger than everything present. So that's six single rotations, and they buy height three against nine, on the input that's worst for a plain tree.

@words text="Mixed order: 4 rebalances, height 3 vs 4" sub="LL at 5 · LR at 30 · RR at 80 · RL at 62"
A mixed order of thirteen keys shows all four cases: L L at five, L R at thirty, R R at eighty, R L at sixty two. Height three against four. The gap depends on the order you test. The reason to balance is the guarantee on every input.

@chapter Where people slip
@list heading="Common slips" items="Fixing an inside case with one rotation@The first|Fixing the highest unbalanced node@The second|Reading the measured gap as the value@And the third"
The first slip is trying an inside case with a single rotation. Check that the inner grandchild ends up as the subtree root. The second is fixing the highest unbalanced node instead of the lowest. And the third is reading a measured height gap as the value of balancing.

@chapter Try it
@words text="Insert 50 25 75 10 5 30 27 60 90 80 70 98 62"
Your turn. Insert these thirteen keys, name the case at each rebalance, and compare the final height with the plain tree's.

@end text="Watch the cases fire"
You can insert your own keys and see each case named and animated, on Learn. That's learn dot get er done dot I O.
