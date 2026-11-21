---
format: long
lesson: scheduling/shortest-processing-time-and-the-adjacent-exchange
title: Why shortest-first is optimal: one swap, one subtraction
thumb: One swap, one subtraction
---

@chapter The question
@title text="Shortest Processing Time" sub="Scheduling" art=thumb
To make the total of all the finish times as small as possible, you run the shortest job first. Everyone's heard that rule. But why is it true? The whole proof is one swap and one subtraction.

@chapter The adjacent exchange
@art adjacent-swap
Take an order, and swap two neighbouring jobs. Leave everything else alone. That's an adjacent exchange. And adjacent is the word doing the work.

@art only-two-move
Every job before the pair finishes at the same time as before, because nothing about it changed. Every job after the pair also finishes at the same time, because the same two jobs were done in between. Only two finish times move.

@math heading="Pair a then b, starting at t" items="before:  (t + p_a) + (t + p_a + p_b)@before;;after:  (t + p_b) + (t + p_b + p_a)@after;;change = p_b − p_a@the change"
Say the pair starts at time t. Before the swap, they finish at t plus p a, and t plus p a plus p b. After, at t plus p b, and t plus p b plus p a. The second of each is the same number. So the change in the total is p b minus p a. The start time cancels.

@words text="Negative exactly when the shorter job was behind"
Read the sign. The change is negative exactly when b is shorter than a, so when the shorter job was behind. Any order with a longer job right in front of a shorter one can be strictly improved by one swap.

@chapter Shortest first
@art sorted-staircase
So which orders can't be improved by any adjacent swap? Only those with no such pair: sorted by processing time, shortest first. Ties don't matter, because swapping two equal jobs changes the total by zero.

@math heading="A 9, B 2, C 6, D 3, E 5" items="longest first  A C E D B:  92@ninety two;;arrival  A B C D E:  82@eighty two;;shortest first  B D E C A:  58@fifty eight"
On the lesson's five jobs, longest first gives a total of ninety two. The arrival order gives eighty two. Shortest first, B, D, E, C, A, gives fifty eight. And that's the best of all hundred and twenty orders.

@words text="Minimises Σ C, and nothing more"
The theorem says shortest first minimises the total of finish times, and nothing more. Nothing about weights or due dates. And it's the rule that makes the longest job wait the longest.

@chapter Ten swaps
@art reverse-staircase
The lab starts from the worst order, longest first, and takes the first improving adjacent swap, again and again. It's never told what shortest first is, or where to stop.

@math heading="The walk" items="swap A, C:  6 − 9 = −3  →  89@six minus nine;;swap A, E:  5 − 9 = −4  →  85@five minus nine;;…;;swap D, B:  2 − 3 = −1  →  58@two minus three"
Swap A and C: six minus nine, minus three, down to eighty nine. Swap A and E: five minus nine, minus four, down to eighty five. And so on, until the tenth swap, D and B: two minus three, minus one, and the total is fifty eight.

@art swap-walk
It takes ten swaps, moving minus thirty four in total, and stops on its own at the sorted order. Ten is the number of pairs among five jobs, because the start was the exact reverse of the finish.

@words text="The walk shows it. The identity proves it."
But the walk only shows that this order wasn't optimal. The proof is the identity, applied to any pair at any position in any order: an unsorted order always has an improving swap.

@chapter Where people slip
@art distant-swap
Why neighbours? Swap the first and last of five jobs, and the three in between move too. The difference becomes a sum over the jobs straddled. Every proof in this course swaps neighbours for exactly this reason.

@list heading="Common slips" items="Getting the sign backwards@The first|Using the identity for a distant swap@The second|Reporting the walk as the proof@And the third"
The first slip is getting the sign backwards, which proves longest first, ninety two where fifty eight is available. The second is using the identity for a distant swap. And the third is reporting the walk as the proof.

@chapter Try it
@words text="Swap C and A in B D E C A" sub="change = p_A − p_C"
Your turn. Start from the shortest first order and swap its last two jobs, C and A. Use the identity to predict the change without running the clock. Then run the clock and check you land on sixty one.

@end text="Walk the swaps yourself"
You can start from any order and watch each swap move the total by one subtraction, on Learn. That's learn dot get er done dot I O.
