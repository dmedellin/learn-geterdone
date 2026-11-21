---
format: long
lesson: algorithms-and-complexity/correctness-and-termination
title: Proving an algorithm works: invariants and termination
thumb: Right answer, and it stops
---

@chapter Two obligations
@title text="Correctness and Termination" sub="Algorithms and Complexity" art=thumb
How do you know an algorithm works? Testing a few inputs isn't enough. You need a proof, and it turns out there are two separate things to prove.

@art two-locks
The first is partial correctness: if the algorithm stops, its output is right. The second is termination: it does stop. Put the two together and you have total correctness, a right answer on every valid input.

@words text="Neither implies the other"
They really are independent. An algorithm can be partially correct and never stop. Or it can stop promptly with the wrong answer. Proving one tells you nothing about the other. So you prove both, and you say clearly which one you've proved.

@chapter Linear search
@math heading="LINEAR-SEARCH(a, x)" items="for i = 1 to n:  if aᵢ = x: return i@for i from one;;return 0@return zero;;Invariant: before iteration i,  x ∉ {a₁, …, a_{i−1}}@The invariant"
Here's linear search. For i from one to n, if a i equals x, return i. If the loop finishes, return zero. The invariant is the key: before iteration i, x is not among a one up to a i minus one.

@list heading="Checking the invariant" items="Initialisation: the set is empty@Before the first|Maintenance: reaching i + 1 means x ≠ aᵢ@Each iteration|Termination: x is in none of a₁ … aₙ@And if the loop"
Before the first iteration, that set is empty, so the claim is true for free. Each iteration returns if a i equals x, so reaching the next one means x isn't a i, and the invariant extends. And if the loop finishes, x is in none of the n entries, so returning zero is correct.

@art search-scan
That shows partial correctness. For termination, look at n minus i. It's a whole number, it never goes below zero, and it strictly decreases every time round. Something like that can't decrease forever, so the loop stops.

@chapter Insertion sort
@art sorted-prefix
Insertion sort's outer loop has a two part invariant. The first j minus one positions hold the original first j minus one elements, in sorted order. You need both halves.

@art zeroed-array
Why both? Sorted on its own would be satisfied by an algorithm that replaced the whole array with zeros. The specification says the output must be a permutation of the input, the same elements rearranged, so the invariant has to say so too.

@chapter Euclid's algorithm
@math heading="Euclid" items="gcd(a, b) = gcd(b, a mod b)@a mod b;;Invariant: gcd(a, b) = gcd(a₀, b₀)@the starting pair;;at exit b = 0,  gcd(a, 0) = a@At the exit"
Euclid's algorithm repeatedly replaces a and b with b and a mod b, and that step doesn't change the greatest common divisor. So the invariant is that the gcd of a and b equals the gcd of the starting pair. At the exit b is zero, and the gcd of a and zero is a.

@art shrinking-stack
Termination is just as short. b strictly decreases, and it's a non negative whole number. That one line invariant is the whole proof, and that's typical. A good invariant names what the loop preserves, and correctness falls out of the exit condition.

@chapter When stopping is the hard part
@art collatz-path
Here's a case where termination is everything. Start from n. If it's even, halve it. Otherwise replace it with three n plus one. Stop at one. Partial correctness is trivial, since it only ever stops at one.

@words text="Tested beyond 10²⁰" sub="no proof that it always stops"
It has stopped for every starting value ever tested, beyond ten to the twenty. And nobody has proved that it always does. Termination is an open problem. And there's no general procedure that decides termination for every program, which is why each one needs its own argument.

@chapter Where people slip
@list heading="Common slips" items="Proving one obligation and stopping@The first|Choosing an invariant that's too weak@The second|Assuming loops obviously terminate@The third"
The first slip is proving one obligation and stopping. The second is choosing an invariant that's too weak, like sorted without the rest. And the third is assuming loops obviously terminate. Name the decreasing quantity and its lower bound. It's one sentence, and it's exactly where an off by one error shows up.

@chapter Try it
@words text="Invariant + decreasing measure" sub="for each loop you write"
Here's something to practise. Take Euclid's algorithm, or the linear search, and write out both halves yourself. First the invariant, checked at the start, through each iteration, and at the exit. Then the quantity that decreases, and the bound that stops it decreasing forever.

@end text="Two proofs, every time"
The full lesson, with insertion sort and the Collatz procedure, is on Learn. That's learn dot get er done dot I O.
