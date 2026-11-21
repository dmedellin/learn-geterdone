---
format: long
lesson: scheduling/smiths-rule-and-weighted-completion-time
title: Smith's rule: sort by time over weight, not by either one
thumb: The ratio, not either number
---

@chapter The question
@title text="Smith's Rule" sub="Scheduling" art=thumb
Some jobs matter more than others. Should the most important job go first? Or the shortest? The answer is neither, and the same one swap from shortest first tells you exactly what to sort by instead.

@art weighted-bars
Give each job a positive weight, the cost of one unit of waiting for it. Twice the weight means an hour's delay hurts twice as much. The objective is the weighted total of finish times. Weights aren't ranks. They're multipliers, and their sizes matter.

@chapter The weighted swap
@math heading="Pair a then b" items="change in Σ wC = w_a p_b − w_b p_a@w a p b;;< 0  ⟺  p_a / w_a > p_b / w_b@divide"
Swap two adjacent jobs, a then b. Only their two finish times move, as before. Work it through, the start time cancels, and the change is w a p b minus w b p a. Divide by both weights, which are positive, and it's negative exactly when p a over w a is bigger than p b over w b.

@words text="Sort by p / w, ascending" sub="Smith's rule"
So the key is the ratio, time over weight. Sort ascending by it, and no swap can improve. That's Smith's rule. It's also why a weight of zero is refused: the ratio is a division.

@chapter Four jobs, three rules
@math heading="A 3:1,  B 8:4,  C 2:3,  D 6:2" items="ratios:  A 3,  B 2,  C 2/3,  D 3@ratios"
The lesson's four jobs, as time and weight: A is three and one, B is eight and four, C is two and three, D is six and two. Their ratios are three, two, two thirds, and three.

@art heaviest-first
B is both the longest and the heaviest job, so the one number rules disagree about it as loudly as they can. Heaviest first puts B at the very front, where its eight hours delay everyone. That costs a hundred and thirteen.

@art shortest-first-wrong
Shortest first puts B at the very back, where four units of weight wait the whole nineteen hours. That costs a hundred and nine.

@art ratio-order
The ratio puts B second: C, B, A, D. That costs ninety seven, the best of all twenty four orders. Neither one number rule is silly. Each is a correct rule for a question nobody asked.

@chapter The one swap between them
@art one-swap-gap
Heaviest first gives B, C, D, A. At the front, B's ratio is two and C's is two thirds, out of order. The identity predicts the swap.

@math heading="Swap B and C" items="w_B p_C − w_C p_B = 4 × 2 − 3 × 8@four times two;;= 8 − 24 = −16@minus sixteen;;113 − 16 = 97@ninety seven"
Four times two, minus three times eight. That's eight minus twenty four, minus sixteen. So the swap takes a hundred and thirteen down to ninety seven, which is optimal. The whole gap between the rival rule and the theorem is one adjacent pair, and two multiplications sized it in advance.

@chapter Smith includes shortest first
@words text="Equal weights → p / w orders like p"
Set every weight equal, and the ratio orders the jobs exactly as the time does. So Smith's rule becomes shortest first. The unweighted theorem isn't a separate result. It's the special case.

@art ratio-tiles
And a long heavy job can have the same ratio as a short light one. Then their order doesn't matter at all. The difference is exactly zero. That's why the optimum here is reached twice, by C, B, A, D and by C, B, D, A.

@chapter Where people slip
@list heading="Common slips" items="Sorting by weight, or by time, alone@The first|Rounding the ratios@The second|Treating p / w as a score@And the third"
The first slip is sorting by the weight, or by the time, and calling it a priority rule. Each ignores half the data. The second is rounding the ratios, which invents differences between ties. And the third is treating time over weight as a score. It's an ordering key, nothing else.

@chapter Try it
@words text="Walk from A B C D" sub="three improving swaps"
Your turn. Start from the order A, B, C, D, worth a hundred and twenty four. Find the first adjacent pair whose ratios are out of order, compute the swap's change with the identity, and keep going. You should stop at ninety seven after three swaps. Notice that the biggest gain, minus sixteen, comes last. Don't stop swapping just because the gains look small.

@end text="Weight the jobs, swap the pairs"
You can set the weights and watch each swap move the weighted total, on Learn. That's learn dot get er done dot I O.
