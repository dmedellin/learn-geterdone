---
format: long
lesson: sets-relations-functions/subsets-and-power-sets
title: Subsets and power sets: why every set has 2ⁿ subsets
thumb: In or out, n times
---

@chapter The question
@title text="Subsets and Power Sets" sub="Sets, Relations and Functions" art=thumb
Is the empty set a subset of every set? Yes, and the reason isn't a special rule. It falls straight out of what subset means, once you read the definition honestly.

@art subset-loops
A is a subset of B when every member of A is also a member of B. Written out, that's a quantified conditional: for every x, if x is in A, then x is in B. If A is a subset of B but not equal to it, it's a proper subset.

@math heading="Subset" items="A ⊆ B  ⟺  ∀x (x ∈ A → x ∈ B)@for every x;;A ⊂ B  means  A ⊆ B and A ≠ B@proper subset"
For every x, x in A implies x in B. And a proper subset is a subset that isn't the whole thing.

@chapter Member or subset?
@art member-vs-subset
The standard error is mixing up is a member of with is a subset of. They relate different kinds of thing. Membership relates an object to a set. Subset relates a set to a set.

@math items="1 ∈ {1, 2}   ✓@one is a member;;{1} ⊆ {1, 2}   ✓@the set containing one;;1 ⊆ {1, 2}   ✗@one is not a set;;{1} ∈ {1, 2}   ✗@the members are"
One is a member of one, two. True. And the set containing one is a subset of one, two. Also true. But one is a subset of one, two is false, because one is not a set. And the set containing one is a member of one, two is false too, because the members are just one and two.

@chapter The empty set is inside everything
@art empty-inside
Now the claim from the start. The empty set is a subset of A means: for every x, if x is in the empty set, then x is in A. But nothing is in the empty set. The hypothesis is false every time, so every one of those conditionals is vacuously true. There's nothing to check, and that's exactly why it holds.

@words text="A ⊆ A" sub="every set is a subset of itself"
And every set is a subset of itself, which is easy to forget. That makes subset reflexive, while proper subset is not.

@chapter Double inclusion
@art double-arrows
To prove two sets are equal, you prove two subsets. A is a subset of B, and B is a subset of A. Take an arbitrary element of one, show it belongs to the other, then do the same in reverse. This is the workhorse of the whole course.

@math heading="A: x = 3k + 1  ·  B: x = 3m − 2" items="x ∈ A:  x = 3k + 1 = 3(k + 1) − 2  ⟹  x ∈ B@take x in A"
Here's one. A is the integers of the form three k plus one, and B is the integers of the form three m minus two. Take x in A. Then three k plus one equals three times k plus one, minus two. That's the form B needs, so x is in B.

@math heading="A: x = 3k + 1  ·  B: x = 3m − 2" items="x ∈ B:  x = 3m − 2 = 3(m − 1) + 1  ⟹  x ∈ A@take x in B;;A ⊆ B and B ⊆ A, so A = B@both inclusions"
Now take x in B. Three m minus two equals three times m minus one, plus one, so x is in A. With both inclusions, A equals B.

@math heading="One way only" items="{x : 6 | x} ⊆ {x : 3 | x}@multiples of six;;3 is a multiple of 3, not of 6@not of six"
But one direction is not enough. The multiples of six are a subset of the multiples of three, because six k is three times two k. The reverse is false. Three is a multiple of three and not of six, and one element is all a refutation needs.

@chapter The power set
@math heading="P(A) = {S : S ⊆ A}" items="P(∅) = {∅}@of the empty set;;P({a}) = {∅, {a}}@of a;;P({a, b}) = {∅, {a}, {b}, {a, b}}@of a, b"
The power set of A is the set of all its subsets. Its members are sets. The power set of the empty set is the set containing the empty set: one member. The power set of a has two: the empty set and a itself. The power set of a, b has four.

@art in-out-switches
Why does it keep doubling? A subset is decided by one independent yes or no for each element. Is it in, or out? Two choices, made n times, give two to the n subsets.

@art doubling-tree
That grows fast. A ten element set has one thousand and twenty four subsets. A thirty element set has over a billion. So power sets aren't something to list casually.

@chapter Where people slip
@list heading="Common slips" items="Writing ∈ where ⊆ is meant@The first|Proving one inclusion and claiming equality@The second|Forgetting A ⊆ A@the third"
The first slip is writing is a member of where you mean subset. The second is proving one inclusion and claiming equality. The other half needs its own argument, and it's often the half that fails. And the third is forgetting that every set is a subset of itself.

@chapter Try it
@words text="{2k + 1 : k ∈ ℤ} = {2m − 1 : m ∈ ℤ}" sub="prove it by double inclusion"
Your turn. Prove that the integers of the form two k plus one are the same as the integers of the form two m minus one. Do it by double inclusion. Each direction is three lines, in the same shape as the example.

@end text="Count the subsets, size by size"
You can list the subsets of a set size by size and watch them add up to a power of two, on Learn. That's learn dot get er done dot I O.
