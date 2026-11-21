---
format: long
lesson: intro-algorithms-data-structures/red-black-insertion-and-deletion
title: Red-black insertion and deletion, case by case
thumb: At most two rotations
---

@chapter Keeping the rules
@title text="Red-Black Insertion and Deletion" sub="Introduction to Algorithms, Sections 13.3 and 13.4" art=thumb
A red black tree's height is at most two log of n plus one. But ordinary insertion and deletion can break the rules. Sections thirteen point three and four repair them, and the repair turns out to be remarkably cheap.

@chapter Insert red
@art new-red-leaf
Insertion starts like a normal search tree insert. Hang the new node z as a leaf, and colour it red. Red is the safe colour. A black leaf would add a black to every path through it, and break rule five at every ancestor at once.

@list heading="What can go wrong" items="z is the root: rule 2@the root|z's parent is red: rule 4@parent is red"
With a red z, only two things can go wrong. Either z is the root, which breaks rule two, or z's parent is red, which breaks rule four. Both are right next to z. The fix up loops while z's parent is red, and since that parent isn't the root, a black grandparent exists.

@chapter Three cases
@art red-uncle
The uncle, the parent's sibling, decides the case. Case one: the uncle is red. Colour the parent and uncle black, and the grandparent red, and move z up two levels. One black has moved down onto both children, so every black count is unchanged.

@art zigzag-bend
Case two: the uncle is black, and z bends inward, a right child of a left child. Left rotate at the parent. That turns it into case three, with z and its parent swapping roles.

@art black-uncle-rotate
Case three: the uncle is black, and z is on the outside. Colour the parent black and the grandparent red, and right rotate at the grandparent. Now the subtree's top is black, and the loop ends.

@quote text="never performs more than two rotations, since the while loop terminates if case 2 or case 3 is executed." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 13.3"
Only case one repeats, climbing two levels each time, so the loop runs O of log n times. And the book concludes that insertion never performs more than two rotations, since the while loop terminates if case two or case three is executed.

@chapter In the lab
@math heading="Insert 10 to 80 in order" items="case 1′ ×3, case 3′ ×4@case one prime;;19 recolourings, 4 rotations@nineteen;;height 4  vs  chain of 7@final height is four"
Insert ten to eighty in increasing order. That takes case one prime three times and case three prime four times, where prime means the mirror case. Nineteen recolourings and four rotations in all, never more than one per insertion. The final height is four, where a plain search tree would be a chain of seven.

@words text="Zigzag: 2 rotations per bent insertion" sub="spread order: no rotations at all"
A zigzag order bends every other insertion inward, and rotates twice in each, the most the analysis allows. And an order that keeps the tree bushy needs no rotations at all.

@chapter Deletion
@art extra-black
Deletion is longer. Track the node y that's removed or moved, and its original colour. If y was red, nothing breaks. If y was black, the node x that takes its place is given an extra black, so the black counts stay right. The fix up then moves that extra black up the tree.

@art sibling-cases
The cases look at x's sibling, w. If w is red, recolour and rotate to get a black sibling. If w is black with two black children, colour w red and move the extra black up. If w has a red child on the near side, rotate at w. And with a red child on the far side, recolour and rotate at the parent, and the extra black is gone.

@math heading="Delete 10 from 20B(10B 40B(30R 50R))" items="y = 10, black; x = nil, doubly black@doubly black;;sibling 40 black, far child 50 red: case 4@case four;;40B(20B(− 30R) 50B), bh 2@black height two"
Delete ten from this tree. Ten is black with no children, so x is the nil leaf, doubly black. Its sibling forty is black, with a red far child, fifty. That's case four. Colour fifty black, rotate left at twenty, and the tree is forty black, over twenty and fifty, with black height two.

@words text="Deletion: O(lg n), at most 3 rotations" sub="only case 2 repeats"
Only case two repeats, without rotating. So deletion is O of log n, with at most three rotations, case one, then three, then four.

@chapter Common slips
@list heading="Common slips" items="Expecting rotations to grow with the tree@The first|Colouring the new node black@The second|Fixing up after every deletion@the third"
The first slip is expecting rotations to grow with the tree. Recolouring climbs, but rotations are bounded. The second is colouring the new node black. And the third is calling the deletion fix up whenever a node is removed. It's needed only when y was black.

@chapter Try it
@words text="15 5 10 25 20" sub="cases, recolourings, rotations"
Your turn. Insert fifteen, five, ten, twenty five and twenty into an empty red black tree by hand. For each key, name the fix up cases, and count the recolourings and rotations.

@end text="Count every case"
You can insert whole sequences and count every case, recolouring and rotation, on Learn. That's learn dot get er done dot I O.
