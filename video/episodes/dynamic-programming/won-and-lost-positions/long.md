---
format: long
lesson: dynamic-programming/won-and-lost-positions
title: Won and lost positions: a table of truth values, and a period you can't prove by looking
thumb: Seen to repeat, not proved
---

@chapter The question
@title text="Won and Lost Positions" sub="Dynamic Programming and Optimal Substructure" art=thumb
Two players take turns removing stones from a pile. Each turn you take one, three or four. If you can't move, you lose. From which piles can the player to move force a win? A table answers that, and then shows a pattern it can't actually prove.

@art pile-moves
That's a subtraction game. From position p, a player may move to p minus m, for any m in a fixed subtraction set, as long as m isn't bigger than p. A position is losing if the player about to move loses under perfect play, and winning otherwise.

@chapter The labelling rule
@list heading="The labelling recurrence" items="p is losing: every move reaches a winning position@losing if every move|p is winning: some move reaches a losing position@winning if some move|no moves at all: losing@no legal move"
A position is losing if every move from it reaches a winning position. It's winning if some move reaches a losing one. And a position with no legal move is losing, because every move, of which there are none, reaches a win.

@art stones-game
Why is that right? If some move reaches a losing position, take it, and your opponent is stuck losing. If every move reaches a winning position, whatever you do, your opponent wins. Those cases cover everything, by induction on the position.

@art truth-cells
Notice there's nothing to optimise here. Every other table on this course computes a best value. This one computes a truth value, and its recurrence is a pair of quantifiers, every and some, rather than a minimum or a sum. The technique survives without the arithmetic.

@chapter Take one, three or four
@words text="L W L W W W W L W L W W W W L W L W W" sub="positions 0 to 18"
Label positions zero to eighteen, counting up from zero, since every move goes down. The labels come out: lose, win, lose, win, win, win, win, lose, and then it starts again.

@math heading="Why 2 and 7 lose" items="2 → 1  (W)  ⇒  2 is L@Position two;;7 → 6, 4, 3  (all W)  ⇒  7 is L@Position seven"
Position two loses, because its only move is to one, which wins. Position seven loses because its moves reach six, four and three, all winning.

@math heading="Losing positions" items="0, 2, 7, 9, 14, 16@zero, two, seven;;≡ 0 or 2  (mod 7)@modulo seven"
The losing positions are zero, two, seven, nine, fourteen and sixteen. That's every position that leaves zero or two, modulo seven. Two residues, not the multiples of anything. The panel reports a period of seven, and a minimax recursion agrees with the table everywhere.

@art other-sets
Other subtraction sets behave differently. With one, two and three, the losing positions are exactly the multiples of four, and there's a one line argument for that. With one and two, the multiples of three. With two and five, positions zero and one both lose.

@chapter Measured versus proved
@art repeating-window
The panel's period comes from checking which shift makes the labels agree, across the nineteen positions shown. That's two full repetitions and a bit. If the pattern broke at position forty, the panel would never know.

@math heading="Eventually periodic" items="M = largest move@largest move;;label(p) depends on the M labels below it@depends only;;≤ 2^M possible windows  ⇒  period ≤ 2^M@two to the M;;moves 1, 3, 4:  bound 16,  measured 7@bound is sixteen"
Here's what can be proved. Let M be the largest move. Each label depends only on the M labels below it. There are at most two to the M such windows, so one must repeat, and from then on everything repeats. For one, three and four, the bound is sixteen. The measured period is seven.

@art window-slide
Picture a window of the last M labels sliding up the row. Each window decides the next label, and so the next window. The windows march through a finite set, so sooner or later they must cycle.

@words text="Measured: 7 over 19 positions · Proved: ≤ 16, eventually"
Neither implies the other. The table doesn't show that seven continues. The proof doesn't say the period is seven, or that it starts at zero. Raising the range extends the measurement. It never turns it into the theorem.

@chapter Where people slip
@list heading="Common slips" items="Turning the observed pattern into a formula@The first|Reading the base case as a special rule@The second|Extending the range and calling it proved@The third"
The first slip is turning the observed pattern into a formula, as if residues zero and two mod seven had a proof. The second is treating the base case as a special rule. It's the general rule with nothing to check. The third is extending the range and calling the pattern proved.

@chapter Try it
@words text="moves 1, 2, 3"
Your turn. Label positions zero to twelve with moves one, two and three. Check the losing ones are the multiples of four. Then find the one line argument for why that pattern always continues.

@end text="Label a game yourself"
You can pick your own subtraction set and label every position, on Learn. That's learn dot get er done dot I O.
