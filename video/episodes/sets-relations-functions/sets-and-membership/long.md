---
format: long
lesson: sets-relations-functions/sets-and-membership
title: What is a set? Membership, notation and the empty set
thumb: A set is its members
---

@chapter The question
@title text="Sets and Membership" sub="Sets, Relations and Functions" art=thumb
Almost every idea in discrete maths is built out of sets. So it's worth being precise about what a set actually is, because the answer is shorter, and stranger, than you might expect.

@art member-box
A set is a collection of distinct objects, called its elements, or members. For any object x, there's one question you can ask: is x in the set, or not? The answer is always yes or no.

@math heading="Membership" items="x ∈ A@x is in A;;x ∉ A@x is not in A"
We write it with a small curly symbol. x is in A, or x is not in A. Membership is the basic relation everything else is built from.

@chapter Two ways to describe a set
@math heading="One set, two descriptions" items="A = {2, 3, 5, 7}@roster notation;;A = {x ∈ ℤ : x is prime and x < 10}@set builder"
There are two ways to write a set down. Roster notation simply lists the members: two, three, five and seven. Set builder notation states the property that picks them out: the integers x such that x is prime and x is less than ten. The colon is read such that, and you'll often see a vertical bar used instead.

@art sieve
Think of set builder notation as a filter. The part before the colon says which objects are candidates. The part after it says which of them get through.

@chapter A set is its members
@words text="A = B ⟺ same members" sub="extensionality"
Here's the one rule that defines everything. Two sets are equal exactly when they have the same members. Every member of A is in B, and every member of B is in A. This is called extensionality. A set carries no information beyond what belongs to it.

@art two-orders
Two consequences follow straight away, and both surprise people once. Order means nothing. And repetition means nothing either.

@math items="{1, 2} = {2, 1}@one, two;;{1, 1, 2} = {1, 2}@one, one, two"
The set one, two is the same set as two, one. And one, one, two is just one, two. If you need order, you need a tuple, which comes later in this course.

@chapter The empty set
@art empty-boxes
The empty set is the set with no members at all. There's exactly one, because any two sets with no members have the same members, so they're equal. Now compare it with the set containing the empty set. That one has one member. A box with an empty box inside isn't an empty box.

@math items="|∅| = 0@has size zero;;|{∅}| = 1@has size one"
So the empty set has size zero, and the set containing it has size one. For a finite set, those bars mean the number of members.

@art empty-filter
And set builder notation can hide emptiness. The real numbers whose square is less than zero: nothing gets through that filter, so that's the empty set, written in a way that doesn't look empty. A description says which objects belong. It doesn't promise that any do.

@chapter The standard sets
@art nested-regions
A few sets have names of their own. The natural numbers, the integers, the rationals, the reals and the complex numbers, each one sitting inside the next.

@math items="ℕ = {0, 1, 2, 3, …}@natural numbers;;ℤ = {…, −2, −1, 0, 1, 2, …}@the integers"
The natural numbers here are zero, one, two, three, and so on. Whether zero counts is a convention, not a fact, and sources differ. This course includes it. The integers run in both directions.

@chapter Deciding membership
@math heading="A = {x ∈ ℤ : x = 3k + 1 for some k ∈ ℤ}" items="7 = 3(2) + 1  →  7 ∈ A@seven is three times two;;9 = 3(3) + 0  →  9 ∉ A@nine is three times three"
Let A be the integers of the form three k plus one, for some integer k. Is seven in A? Yes: seven is three times two, plus one. Is nine? No: nine is three times three, plus zero, and there's no integer k that works.

@math heading="A = {x ∈ ℤ : x = 3k + 1 for some k ∈ ℤ}" items="−2 = 3(−1) + 1  →  −2 ∈ A@minus two;;A = {…, −5, −2, 1, 4, 7, 10, …}@So A is"
What about minus two? Yes, with k equal to minus one. So A is the list running minus five, minus two, one, four, seven, ten, and on in both directions.

@words text="k may be negative"
Notice that minus two needed a negative k. Forgetting that k can be negative is exactly how half a set goes missing.

@chapter Where people slip
@list heading="Common slips" items="Confusing ∈ with ⊆@The first|Reading {∅} as empty@The second|Forgetting the domain@The third"
The first slip is confusing is a member of with is a subset of. One is in the set one, two, but one isn't a set, so it can't be a subset. The second is reading the set containing the empty set as empty. The third is forgetting the domain: x squared equals two has no solutions in the rationals, and two in the reals.

@chapter Try it
@words text="{x ∈ ℤ : x² < 10}" sub="write the roster"
Your turn. Take the set two, four, six, eight, ten, and write a set builder description for it. Then go the other way: list the integers whose square is less than ten. If you get seven elements, you've remembered the negatives.

@end text="Twelve elements, three sets"
You can move elements in and out of sets and watch equality flip, on Learn. That's learn dot get er done dot I O.
