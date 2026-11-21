---
format: long
lesson: induction-and-recursion/loop-invariants-and-correctness
title: Loop invariants: proving a loop does what it should
thumb: What the loop never changes
---

@chapter Induction on a loop
@title text="Loop Invariants and Program Correctness" sub="Induction and Recursion" art=thumb
How do you know a loop computes what it should? Testing a few inputs doesn't prove it. But induction does, applied to the iterations of the loop instead of to a number.

@art loop-cycle
The tool is a loop invariant: a statement that's true just before the loop begins, and stays true just before every later iteration.

@list heading="Three parts" items="Initialisation: true before the first iteration@Initialisation|Maintenance: if true before an iteration, true after@Maintenance|Termination: the loop stops, and the invariant gives the result@Termination"
A proof has three parts. Initialisation: the invariant holds before the first iteration. That's the base case. Maintenance: if it holds before an iteration, it holds after. That's the inductive step. Termination: the loop stops, and the invariant then gives you the result.

@chapter Summing an array
@math heading="SUM(A)" items="s = 0,  i = 0@start;;while i < n:  s = s + A[i],  i = i + 1@while i;;invariant:  s = A[0] + ⋯ + A[i−1]@invariant"
Here's a loop that sums an array. Start with s and i at zero. While i is less than n, add A of i to s, and add one to i. The invariant: s is the sum of the first i elements.

@art running-total
Initialisation: before the loop, i is zero and s is zero, and the sum of the first zero elements is zero. Maintenance: the body adds the next element to s and moves i on, so the invariant holds again for the new i.

@words text="exit:  i = n,  so  s = A[0] + ⋯ + A[n−1]"
Termination: i goes up by one each time and can't pass n, so the loop exits, with i equal to n. Then the invariant says s is the sum of all n elements. That's exactly what you wanted.

@chapter Insertion sort
@art sorted-prefix
Insertion sort keeps the front of the array sorted. Each pass takes the next element, the key, shifts every bigger element in the sorted part one place right, and drops the key into the gap.

@words text="A[0..j−1] holds the original first j elements, sorted"
The invariant for the outer loop: the first j positions hold the original first j elements, in sorted order. At j equals one, that's a single element, trivially sorted. Each pass keeps it true for one more. And at the end, j is n, so the whole array is sorted.

@art flattened-bars
The invariant says two things: sorted, and the same elements. Drop the second half, and the proof would also accept an algorithm that sorts by replacing the array with zeros. Invariants that are too weak are the usual failure, and they fail at termination.

@chapter Finding an invariant
@list heading="Finding one" items="Start from the postcondition@postcondition|Include everything the proof needs@everything|Check the zero-iteration case@zero times"
To find one, start from the postcondition, what should be true at the end, and put the loop variable in place of its final value. Include everything the proof needs. And check it holds when the loop has run zero times, which is where the vacuous cases live.

@words text="partial correctness + termination = total correctness"
Partial correctness means if the loop terminates, the postcondition holds. Total correctness adds that it does terminate. The invariant gives you the first, and a quantity that strictly decreases and is bounded gives you the second.

@chapter Euclid's algorithm
@math heading="GCD(a, b)" items="while b ≠ 0:  (a, b) = (b, a mod b)@while b;;return a@return a;;invariant:  gcd(a, b) = gcd(a₀, b₀)@invariant"
Here's a worked example. Euclid's algorithm: while b isn't zero, replace a and b with b and a mod b. Then return a. The invariant: the gcd of a and b always equals the gcd of the original inputs.

@art rectangle-squares
It's trivially true at the start. It's maintained because any common divisor of a and b also divides a minus a multiple of b, and the other way round. So the pair changes, but its gcd doesn't.

@math items="b strictly decreases, b ≥ 0  →  ends with b = 0@strictly decreases;;gcd(a, 0) = a = gcd(a₀, b₀)@gcd of a and zero"
And it terminates, because b strictly decreases and is a non-negative integer. It ends with b equal to zero, and the gcd of a and zero is a. By the invariant, that's the gcd of the inputs.

@art invariant-scale
The algorithm works because the quantity it's computing never changes while the numbers get smaller. Every good invariant is like that. It names what the loop preserves, which tells you more than what the loop does.

@chapter Where people slip
@list heading="Common slips" items="An invariant too weak for the postcondition@too weak|Skipping initialisation@Skipping|Stopping at partial correctness@partial correctness"
Three slips. An invariant too weak to give the postcondition. Test it at termination first. Skipping initialisation, which is where off by one errors live. And proving partial correctness and calling it done. A loop with a correct invariant that never exits is useless.

@end text="Watch the invariant hold"
On Learn, you can watch insertion sort find each gap while its invariant holds. That's learn dot get er done dot I O.
