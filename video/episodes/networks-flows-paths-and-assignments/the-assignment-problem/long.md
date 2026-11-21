---
format: long
lesson: networks-flows-paths-and-assignments/the-assignment-problem
title: The Hungarian method, with a certificate you can check
thumb: The bound climbs to the cost
---

@chapter The problem
@title text="The Assignment Problem" sub="Networks, Flows, Paths and Assignments" art=thumb
Four fitters, four jobs, and a cost for every pairing. One job each, one fitter each. Which assignment costs least, and how would you prove it?

@words text="4! = 24 · 5! = 120" sub="corners of the relaxation = the permutations"
There are twenty four ways to assign four, and a hundred and twenty for five. But you don't need to try them all. It's a transportation problem with every supply and demand equal to one, so its corners are exactly the permutations.

@chapter Reductions don't move the answer
@art cost-grid
Here's the key fact. Take a constant off every entry of a row. Every complete assignment uses exactly one cell of that row, so every assignment gets cheaper by exactly that constant. The best one stays the best. The same goes for columns.

@math heading="The four fitters" items="row minima 8, 7, 9, 8: total 32@row minima;;column minima 2, 7, 0, 5: total 14@column minima;;taken off so far: 32 + 14 = 46@forty six"
On the fitters, the row minima are eight, seven, nine and eight, thirty two in all. Then the column minima of what's left are two, seven, zero and five, another fourteen. So far, forty six has been taken off.

@chapter Counting the cover
@art zero-cover
The reduced matrix has seven zeros. Do they carry a complete assignment, four zeros with no two sharing a row or column? Count the fewest lines that cover every zero. If that's four, yes. Here it's three.

@art matching-zeros
But don't count lines by eye. Find the largest matching on the zero cells instead. By Koenig's theorem, the smallest cover equals the largest matching, so the number is well defined. Here the largest matching has three pairs.

@art tie-break
Here's why it matters. After one adjustment, the usual eye test, cover the line with the most uncovered zeros, draws four lines if you break ties towards rows, and three towards columns. Same matrix, same rule, different answers. A matching gives one answer.

@chapter Adjust
@words text="θ = smallest uncovered entry" sub="− θ uncovered · + θ covered twice"
When the cover is short, let theta be the smallest uncovered entry. Subtract it from every uncovered entry, and add it to every entry covered twice. Nothing goes negative, no zero is lost, and a new zero appears.

@chapter The bound climbs
@math heading="Constants taken off" items="32 → 46 → 47 → 49@thirty two;;A→J4, B→J1, C→J2, D→J3@the assignment;;15 + 10 + 16 + 8 = 49@fifteen plus"
On the fitters, the total taken off goes thirty two, forty six, forty seven, forty nine, with adjustments of one and then two. The final zeros carry the assignment A to job four, B to job one, C to job two, and D to job three. That costs fifteen plus ten plus sixteen plus eight, forty nine.

@art climbing-bound
The constants are a dual solution, and their total is a lower bound on every assignment. It never falls. The method stops when the bound meets the cost of an assignment it has actually found. That's strong duality, and it's a certificate, not just a claim that the method stopped.

@chapter Greed, priced
@art greedy-pick
Compare greed. Take the cheapest cell, strike its row and column, repeat. On the fitters it ends at fifty, one too many. On the five drivers it lands on thirty eight, exactly right. But it gave no reason to believe it. The Hungarian run gives thirty eight beside a bound of thirty eight.

@chapter Where people slip
@list heading="Common slips" items="Drawing lines until it looks done@The first|Reporting the reduced matrix's answer@The second|Handing over the assignment without the bound@And the third"
The first slip is drawing lines until you can't obviously do better. The second is reporting the reduced matrix's answer. On the drivers that's one, and the answer is thirty eight: add back everything you took off. And the third is handing over the assignment without the bound that proves it.

@chapter Try it
@math heading="Check the certificate" items="u = (10, 10, 9, 11)@u equals;;v = (0, 7, −3, 5)@v equals;;Σu + Σv = 49@add them"
Your turn. The method hands you u equals ten, ten, nine, eleven, and v equals zero, seven, minus three, five. Add them, and confirm you get forty nine. Then take the fitters' cost table and check, cell by cell, that u i plus v j never exceeds the cost. If all sixteen pass, nothing can cost less than forty nine.

@end text="Watch the bound meet the cost"
You can step through the Hungarian method and watch the bound climb to the cost, on Learn. That's learn dot get er done dot I O.
