---
format: long
lesson: sets-relations-functions/equivalence-relations-and-partitions
title: Equivalence relations: how sameness cuts a set into classes
thumb: Equal or disjoint, never between
---

@chapter The question
@title text="Equivalence Relations and Partitions" sub="Sets, Relations and Functions" art=thumb
Same remainder. Same shape. Same parity. We say two things are the same in some respect all the time. An equivalence relation is the precise version of that idea, and it comes with a gift: it cuts the whole set into neat, separate pieces.

@words text="reflexive + symmetric + transitive"
A relation is an equivalence relation when it's reflexive, symmetric and transitive. Those are exactly the structural properties of equality. It keeps those, and drops the demand that the two objects be identical. It's often written with a small wavy line.

@chapter Classes and partitions
@math heading="Equivalence class" items="[a] = {x ∈ A : x ∼ a}@the class of a"
The class of a is everything related to a. Any member of a class is called a representative of it.

@art partition-tiles
A partition of A is a collection of nonempty pieces, called blocks, that don't overlap, and together cover A. Every element lands in exactly one block.

@art dot-groups
To find the partition, take one element and collect everything related to it. That's a block. Then move to an element not placed yet. Its class is a new block, disjoint from the first. Repeat until every element has a home.

@chapter Equal or disjoint
@art overlapping-blobs
Here's the theorem. For an equivalence relation, two classes are either identical or share nothing at all. There's no partial overlap. And a is related to b exactly when their classes are equal.

@art merging-loops
Why? Suppose a is related to b, and x is in the class of a. By transitivity, x is related to b, so x is in the class of b. Symmetry runs the same argument backwards. So the classes are equal. And if some x is in both classes, symmetry and transitivity make a related to b, so again the classes are equal.

@list heading="Each property's job" items="Reflexive: a is in its own class@reflexivity|Symmetric: the argument runs both ways@symmetry|Transitive: links members of one class@transitivity"
All three properties did a distinct job. Reflexivity puts a into its own class. Symmetry lets the argument run in both directions. And transitivity is what links two members of the same class to each other.

@words text="equivalence relations ⟷ partitions"
And it goes both ways. Every equivalence relation gives a partition into its classes. Every partition gives the relation lies in the same block. Each construction undoes the other.

@chapter Congruence mod 3
@art three-colour-wheel
On the integers, say a is related to b when three divides a minus b. It's reflexive, because three divides zero. It's symmetric, and it's transitive. The three classes are the integers with remainder zero, one and two.

@words text="|a − b| ≤ 1" sub="reflexive, symmetric, not transitive"
Now one that just misses: a and b are at most one apart. Reflexive and symmetric, yes. But one is related to two, and two to three, while one isn't related to three. The would be classes of one and two overlap without being equal, exactly what the theorem forbids.

@chapter The classes mod 4
@math heading="a ∼ b when 4 | (a − b)" items="[0] = {…, −8, −4, 0, 4, 8, …}@remainder zero;;[1] = {…, −7, −3, 1, 5, 9, …}@remainder one;;[2] = {…, −6, −2, 2, 6, 10, …}@remainder two;;[3] = {…, −5, −1, 3, 7, 11, …}@remainder three"
Now mod four. Four divides a minus b. Remainder zero: minus eight, minus four, zero, four, eight. Remainder one: minus seven, minus three, one, five, nine. Remainder two, and remainder three. Four classes, pairwise disjoint, and together they make up all the integers.

@art many-names
And the class of four is the class of zero. The class of minus one is the class of three. A class has many names and one identity. So any definition made through a representative has to be checked: it must give the same answer whichever name you use.

@chapter Where people slip
@list heading="Common slips" items="Checking only two properties@The first|Treating a class as its representative@The second|Allowing an empty block@the third"
The first slip is calling a relation an equivalence after checking only two properties. Transitivity is what makes the classes fit together. The second is treating a class as its representative. And the third is forgetting that blocks must be nonempty.

@chapter Try it
@words text="{{1, 4}, {2}, {3, 5}}" sub="a partition of {1, …, 5}"
Your turn. Take this partition of one to five. Write the relation it induces as a set of pairs, and check all three properties. Then read the classes back off the relation.

@end text="Build an equivalence relation"
You can build an equivalence relation, break it with one click, and watch its classes vanish, on Learn. That's learn dot get er done dot I O.
