---
format: long
lesson: intro-algorithms-foundations/insertion-sort-and-loop-invariants
title: Insertion sort, and how to prove a loop is correct
thumb: Prove the loop, not the tests
---

@chapter The promise
@title text="Insertion Sort and Loop Invariants" sub="Introduction to Algorithms, Section 2.1" art=thumb
Chapter two of Introduction to Algorithms makes a promise for the whole book. Specify an algorithm, argue that it's correct, and analyse its running time. Insertion sort is the first algorithm to get that treatment.

@chapter A hand of cards
@art card-hand
The authors' picture is a hand of playing cards. You pick up one card at a time from the pile, and slide it into place among the cards already in your left hand, comparing from right to left. The cards in your hand are always sorted, and they're always the cards that were on top of the pile.

@art sliding-key
Insertion sort does exactly that with an array. The index j marks the card being inserted, called the key. Everything to its left is the hand. Each larger element in the hand moves one place right, and the key drops into the gap. Only the key is ever held outside the array, so it sorts in place.

@chapter Loop invariants
@quote text="We use loop invariants to help us understand why an algorithm is correct." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 2.1"
A page after the algorithm, the authors write: we use loop invariants to help us understand why an algorithm is correct.

@art invariant-three-parts
A loop invariant is a property that holds at the start of each iteration of a loop. To use one, you show three things. Initialisation: it holds before the first iteration. Maintenance: if it holds before one iteration, it holds before the next. And termination: when the loop ends, it gives you what you wanted.

@list heading="Three parts" items="Initialisation: the base case@the base case|Maintenance: the inductive step@the inductive step|Termination: uses the stopping condition@the analogy stops"
The first two are like induction. Initialisation is the base case, and maintenance is the inductive step. Termination is where the analogy stops. An induction runs forever, but a loop stops, and termination uses the reason it stopped. The authors call it perhaps the most important of the three.

@chapter The invariant for insertion sort
@art sorted-prefix
Here's the invariant. At the start of the pass for j, the subarray from one to j minus one holds the elements that started in those positions, now sorted.

@math heading="Checking the three parts" items="j = 2: A[1] alone, trivially sorted@At j equals two;;pass j: A[1..j] holds the first j, in order@each pass;;j = n + 1: A[1..n] sorted@j equals n plus one"
At j equals two, the subarray is the single element A one, which is trivially sorted. Then each pass shifts the larger elements right and drops the key in place, so the first j elements are now in order. The loop stops at j equals n plus one, and the invariant says the whole array is sorted.

@words text="…the elements that started there" sub="Without this, zeros would pass"
Don't drop the clause about the original elements. An invariant that only says the prefix is sorted is also kept by a procedure that writes zeros. That clause is what makes the result a sorted rearrangement of the input.

@chapter Three arrays, three costs
@math heading="Comparisons and shifts" items="[8, 3, 5, 1, 9, 2, 7]: 15 comparisons, 11 shifts@shuffled;;8 keys sorted: 7 comparisons, 0 shifts@already sorted;;8 keys reversed: 28 comparisons, 28 shifts@reversed"
Run it on the shuffled array eight, three, five, one, nine, two, seven, and the invariant holds at all seven checks, with fifteen comparisons and eleven shifts. Eight keys already sorted take seven comparisons and no shifts. Reversed, they take twenty eight of each.

@art reversed-worst
In the reversed array, every key travels all the way to the front. Same n, three very different amounts of work, and the same invariant held through each.

@chapter Equal keys
@art stable-equal
One more property. The test is strict: is A of i greater than the key? So a key stops as soon as it meets an equal one, and never passes it. Equal keys leave in the order they arrived. That's stability, and the radix sort of chapter eight depends on it.

@chapter Common slips
@list heading="Common slips" items="Expecting it to hold mid-pass@The first|Dropping the original-elements clause@The second|Taking checks on examples for a proof@the third"
The first slip is expecting the invariant to hold at every moment. Halfway through a pass, it's false, and it's true again once the key is dropped in. The second is dropping the clause about the original elements. And the third is taking checks on examples for a proof. Only the maintenance argument covers every array.

@chapter Try it
@words text="[6, 2, 9, 4, 1, 7]" sub="write j, key and the array at each pass"
Your turn. Sort six, two, nine, four, one, seven by hand. At the start of each pass, write j, the key and the array, and check the invariant. Count the comparisons and the shifts, then compare with the lab.

@end text="Watch the invariant hold"
You can watch the invariant checked pass by pass on arrays of your own, on Learn. That's learn dot get er done dot I O.
