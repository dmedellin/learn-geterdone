---
format: long
lesson: dynamic-programming/edit-distance-and-performing-the-script
title: Edit distance: fill the table, then run the script it gives you
thumb: Kitten to sitting, run it
---

@chapter The question
@title text="Edit Distance, and Performing the Script" sub="Dynamic Programming and Optimal Substructure" art=thumb
How different are two words? One good answer is the fewest single character edits that turn one into the other. And once a table finds that number, you can do something stronger than trust it. You can carry the edits out.

@words text="insert · delete · substitute" sub="each costs 1 · keep costs 0"
The edit distance from a to b counts three operations: insert a character, delete one, or substitute one for another. Each costs one. Keeping a character costs nothing. It isn't counted, but it's still a step in the script.

@chapter The recurrence
@math heading="Edit distance" items="D(i, 0) = i,  D(0, j) = j@D of i, zero;;D(i − 1, j) + 1@delete;;D(i, j − 1) + 1@insert;;D(i − 1, j − 1) + c,  c = 0 if equal, else 1@diagonal"
D of i, j turns the first i characters of a into the first j of b. D of i, zero is i, and D of zero, j is j. Otherwise take the smallest of three. Delete, the cell above plus one. Insert, the cell to the left plus one. Or the diagonal, plus one if the characters differ.

@art three-neighbours
Why only three? Look at the last character of each prefix. Either a's last character is deleted, or b's last character is inserted, or the two are lined up, kept or substituted. And whatever comes before must itself be cheapest. Optimal substructure again.

@chapter Is row by row safe?
@art row-major-safe
Recall the matrix chain, where filling row by row went wrong. Here it's fine, and you can say why. The three cells each cell reads are one row up, one column left, and both. Row by row writes all of those first. Zero reads land on unwritten cells. The order isn't always wrong. It's always something to check.

@chapter Kitten to sitting
@list heading="Kitten → sitting" items="Table: 7 × 8, 56 cells, 126 reads → 3@The table|No table: 29 737 calls → 3@with no table"
The table is seven by eight, fifty six cells and a hundred and twenty six reads, and its corner says three. A recursion with no table at all also says three, after twenty nine thousand, seven hundred and thirty seven calls.

@art pointer-path
To get the script, start at the bottom right corner and follow the recorded pointers back to the start. Each step up, left or diagonal is one operation.

@math heading="The script" items="substitute k → s@swap k for s;;keep i, keep t, keep t@keep i;;substitute e → i@swap e for i;;keep n@keep n;;insert g@insert g"
The script reads: swap k for s, keep i, keep t, keep t, swap e for i, keep n, and insert g. Seven steps, and only three of them cost anything.

@art perform-script
Now carry it out on kitten, character by character. Each step names the character it acts on, and execution stops if that character isn't there. The result is sitting, and the panel compares that with the second word, instead of trusting the walk.

@chapter Run it, don't just add it up
@art tile-rows
Why perform it? Suppose the walk took one wrong pointer, but still had three paid steps. Adding up its cost gives three, matching the table, and the check passes. Performing it fails, because the wrong script names characters that aren't where it says.

@art run-vs-cost
That idea goes beyond strings. When a reconstruction is a sequence of steps, running it against the input tells you strictly more than costing it. The knapsack's items could only be re weighed. This script can be run.

@chapter Counts and a loose bound
@math heading="Recursion with no table" items="bound: 3^(m + n) = 3¹³ = 1 594 323@three to the m plus n;;measured: 29 737@twenty nine thousand"
The table is Theta of m n. The recursion without one makes at most three to the m plus n calls. For kitten and sitting, that's three to the thirteen, one million, five hundred and ninety four thousand, three hundred and twenty three. True, and about fifty times the measured twenty nine thousand, seven hundred and thirty seven.

@chapter Where people slip
@list heading="Common slips" items="Reporting the script's length as the distance@The first|Checking a reconstruction only by its cost@The second|Assuming row by row is always safe@The third"
The first slip is reporting the script's length as the distance. Seven steps, distance three. On dog to dogma, it's five and two. The second is checking a reconstruction only by its cost. When it's a sequence of steps, run it. The third is assuming row by row is safe because it worked here.

@chapter Try it
@words text="dog → dogma"
Your turn. Fill the table for dog and dogma, walk back the script, and perform it. Check that it has five steps, and a distance of two.

@end text="Perform the script yourself"
You can fill the table for any two words and run the script it gives, on Learn. That's learn dot get er done dot I O.
