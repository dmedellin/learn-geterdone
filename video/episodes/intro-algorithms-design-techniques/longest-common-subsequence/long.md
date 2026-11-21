---
format: long
lesson: intro-algorithms-design-techniques/longest-common-subsequence
title: Longest common subsequence, with the table and its arrows
thumb: Follow the arrows home
---

@chapter Measuring similarity
@title text="Longest Common Subsequence" sub="Introduction to Algorithms, Section 15.4" art=thumb
How similar are two strands of DNA? One answer is that a long strand appears in both, in the same order, though not necessarily side by side.

@art dna-strands
That's a common subsequence. The authors define the word simply.

@quote text="A subsequence of a given sequence is just the given sequence with zero or more elements left out." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 15.4"
A subsequence of a given sequence is just the given sequence with zero or more elements left out.

@art subsequence-pick
So B L E is a subsequence of TABLE, but L B E is not, because order matters. Trying every subsequence of X is hopeless: there are two to the m of them. So work with prefixes instead, the first i characters of X and the first j of Y.

@art prefix-grid
So the table has a row for each prefix of X, including the empty one, and a column for each prefix of Y. That's m plus one by n plus one cells, and every subproblem the recurrence ever asks about is one of them.

@chapter The last characters
@list heading="Theorem 15.1" items="Last characters equal: they end the LCS@If the last characters|Unequal: drop X's last@drop the last character of X|Or drop Y's last@or of Y"
Theorem fifteen point one looks at the last characters. If the last characters match, that character ends the longest common subsequence, and the rest is a longest one for the two shorter prefixes. If they differ, you can drop the last character of X, or of Y, without losing anything.

@math heading="The recurrence" items="c[i, j] = 0  if i = 0 or j = 0@zero;;c[i − 1, j − 1] + 1  if xᵢ = yⱼ@match;;max(c[i, j − 1], c[i − 1, j])  otherwise@differ"
So c of i j is zero if either prefix is empty. If x i and y j match, it's the diagonal cell plus one. If they differ, it's the larger of the cell to the left and the cell above.

@art three-neighbours
Here's something new. Rod cutting and the matrix chain tried every choice. Here, the input decides which subproblems are used: a match uses only the diagonal, a mismatch only the other two. Each cell reads three earlier neighbours, so filling row by row works, at constant time per cell. That's theta of m times n.

@chapter Arrows
@art arrow-path
Beside each cell, record an arrow: up left for a match, up when the cell above is at least as large, left otherwise. Ties go up. Then start from the bottom right corner and follow the arrows, printing a character at each diagonal step.

@math heading="TABLE vs BLEAT" items="c[5, 5] = 3@three;;from the corner: left, left, then ↖ at E@left twice;;↖ at L, ↖ at B@then diagonally;;prints  B L E@prints B L E"
For TABLE against BLEAT, the corner holds three. From the corner, go left twice to the match at E, then diagonally to L, then to B, and out. So it prints B L E. The arrows in the first two rows are never visited.

@words text="25 cells: 5 ↖, 13 ↑, 7 ←" sub="LCS: BLE"
The lab fills twenty five cells for that pair, holding five diagonal arrows, thirteen up and seven left.

@chapter Ties and anagrams
@words text="ALGORITHM vs LOGARITHM" sub="LCS length 7: LGRITHM (or LORITHM)"
Compare ALGORITHM with LOGARITHM, the same nine letters rearranged. The longest common subsequence has length seven. The lab prints L G R I T H M. But L O R I T H M is just as long. The tie going up picks the first.

@art substring-vs-subsequence
Don't confuse a subsequence with a substring. Those two words share the substring R I T H M, length five, but the subsequence L G R I T H M, length seven. And anagrams needn't share much: STONE and NOTES have a longest common subsequence of only two.

@words text="Drop the b table · keep two rows for length only" sub="the path back needs the full c table"
The section ends with savings. You can drop the arrow table, since each cell and its neighbours tell you where it came from. If you only want the length, two rows suffice. But then the path back is lost.

@chapter Common slips
@list heading="Common slips" items="Confusing a subsequence with a substring@The first|Assuming anagrams share a long LCS@The second|Expecting the arrows to give every LCS@the third"
The first slip is confusing a subsequence with a substring. The second is assuming anagrams have a long common subsequence. And the third is expecting the arrows to give every one. They give one, chosen by the tie rule.

@chapter Try it
@words text="STONE vs NOTES" sub="fill c and b, ties going up"
Your turn. Fill the c and b tables by hand for STONE and NOTES, with ties going up. Give the length, list every longest common subsequence you can find, and say which one the arrows print.

@end text="Fill the table yourself"
You can fill LCS tables for strings of your own and count the arrows, on Learn. That's learn dot get er done dot I O.
