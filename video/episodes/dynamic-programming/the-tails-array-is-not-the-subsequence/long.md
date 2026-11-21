---
format: long
lesson: dynamic-programming/the-tails-array-is-not-the-subsequence
title: Longest increasing subsequence: the tails array is not the answer
thumb: Right length, wrong object
---

@chapter The question
@title text="The Tails Array Is Not the Subsequence" sub="Dynamic Programming and Optimal Substructure" art=thumb
There are two classic ways to find the longest increasing subsequence. A slow one and a fast one. They always agree on the length. But the fast one's array, the one people print as the answer, isn't always an answer at all.

@art subsequence-pick
A subsequence is what's left after deleting some entries and keeping the rest in order. It's strictly increasing if each entry is bigger than the one before. The problem is to find a longest one. There can be many, so be careful about calling any one of them the answer.

@chapter The table
@math heading="Per position" items="best(i) = 1  if nothing earlier is smaller@best of i;;else  best(i) = 1 + max best(j),  j < i,  a(j) < a(i)@otherwise;;answer = max over i of best(i)@The answer"
Let best of i be the length of the longest increasing run ending exactly at position i. It's one if nothing earlier is smaller. Otherwise it's one plus the largest best of j, over earlier positions holding smaller values. The answer is the largest best of i.

@art predecessor-links
Record which j won at each step, a predecessor, and you can read the run back. Why is it right? Remove the last entry from a longest run ending at i, and what's left must be a longest run ending at j, or you could swap in a longer one. This takes order n squared comparisons.

@chapter The tails array
@words text="tails[L] = smallest value ending a run of length L + 1"
The fast method keeps an array called tails. Position L holds the smallest value that ends an increasing run of length L plus one, among the values seen so far.

@art tails-replace
Each new value either extends the array, if it's bigger than everything there, or replaces the first entry that's at least as large. Binary search finds the spot, so the whole run is order n log n. On ten values, fourteen comparisons, against the table's forty five.

@words text="A record per length, not a run"
But notice what's missing. Nothing promises the array is a subsequence of the input. Its entries can come from positions that never sit together in one run. The length is right. The contents are a different question.

@chapter Ten values
@art growing-array
Let's watch the tails array run, one value at a time, and see what it holds at each step.

@math heading="10 9 2 5 3 7 101 18 4 8" items="after 7 values:  2 3 7 101@after the seventh;;18 replaces 101 · 4 replaces 7 · 8 replaces 18@eighteen replaces;;tails ends:  2 3 4 8@ends as"
On ten, nine, two, five, three, seven, a hundred and one, eighteen, four, eight, the tails array after the seventh value is two, three, seven, a hundred and one, a real longest run. Then eighteen replaces a hundred and one, four replaces seven, and eight replaces eighteen. It ends as two, three, four, eight.

@words text="table: 2 5 7 101" sub="tails: 2 3 4 8"
The table, following its predecessors, gives two, five, seven, a hundred and one.

@art two-answers
Both have length four, and both happen to be valid here. The array passed through one valid answer on its way to another. Nothing about the mechanism guarantees where it ends up is valid.

@chapter Where it breaks
@math heading="3 1 4 1 5 9 2 6 5 3" items="tails ends:  1 2 3 6  ·  increasing ✓  ·  subsequence ✗@tails array ends;;table:  3 4 5 9  ·  both ✓@The table"
Now switch to three, one, four, one, five, nine, two, six, five, three. The tails array ends one, two, three, six. It's increasing, but it isn't a subsequence. The only six comes before the last three. The table gives three, four, five, nine, which passes both checks.

@art two-checks
So the panel checks two things separately. Is it increasing? The tails array always is, so that check can never catch it. Is it a subsequence of the input? That's the check with teeth. A third route, trying all one thousand and twenty four subsequences of ten values, confirms the length.

@chapter Where people slip
@list heading="Common slips" items="Printing the tails array as the answer@The first|Checking only that the output increases@The second|Assuming both methods return the same object@The third"
The first slip is printing the tails array as the answer. It has the right length, and often looks fine, which is how this has shipped as a real bug more than once. The second is checking only that the output increases. The third is concluding from one sequence that both methods return the same object.

@chapter Try it
@words text="3 1 4 1 5 9 2 6 5 3"
Your turn. Run the tails array on this sequence by hand, writing it out after each value. Then fill best of i with predecessors, and read back a run you can actually find in the input.

@end text="Compare the two arrays yourself"
You can run both methods and check each answer against both properties, on Learn. That's learn dot get er done dot I O.
