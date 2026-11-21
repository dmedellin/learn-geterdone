---
format: long
lesson: dynamic-programming/subsets-as-a-table-and-where-it-loses
title: Held-Karp: a table indexed by subsets, and where it still loses
thumb: Better exponential, still loses
---

@chapter The question
@title text="Subsets as a Table, and Where the Table Loses" sub="Dynamic Programming and Optimal Substructure" art=thumb
The travelling salesman problem asks for the shortest round trip through every city. Trying every order costs a factorial. A clever table cuts that to an exponential. And on small instances, the clever table still loses.

@art tour-loop
Here's the problem as this page states it. You have n cities and a distance from each to each. Find a round trip that starts at city one, visits every city exactly once, and comes back, with the least total length. The distances don't have to be symmetric, or obey the triangle inequality.

@chapter A subset as an index
@art subset-index
Held and Karp index a table by a pair: a set of cities already visited, and the city the route currently ends at. Each entry holds the shortest route from city one that visits exactly that set, and finishes there. Nothing says a table's index has to be a number.

@math heading="Held–Karp" items="D({1, j}, j) = d(1, j)@D of the set one, j;;D(S, j) = min over i of D(S − {j}, i) + d(i, j)@D of S, j;;tour = min over j of D(all, j) + d(j, 1)@the tour"
D of the set one, j is just the distance from one to j. For a bigger set, D of S, j is the minimum over the city i you came from, of D of S without j, ending at i, plus the leg from i to j. The tour adds the leg home, and takes the best last city.

@art order-forgotten
Why does it work? Two routes through the same cities, ending at the same city, are interchangeable for everything that follows. So only the shorter one needs keeping. The order inside a set stops mattering, and that's what collapses the factorial.

@words text="fill by subset size" sub="every read is a smaller set"
And the fill order follows as usual. Each entry reads entries for a strictly smaller set, so fill by increasing subset size, and every read is already written. On four cities, that's twelve reads.

@chapter Four cities
@list heading="All six tours" items="1-2-3-4-1: 22@twenty two|1-2-4-3-1: 33@thirty three|1-3-2-4-1: 26@twenty six|1-3-4-2-1: 21@twenty one|1-4-2-3-1: 34@thirty four|1-4-3-2-1: 30@thirty"
The matrix is asymmetric. One to two is two, but two to one is one. There are six tours. One two three four costs twenty two. One two four three, thirty three. One three two four, twenty six. One three four two, twenty one. One four two three, thirty four. And one four three two, thirty.

@art all-orders
Trying every one of those six orders gives the same best tour as the table. So the two routes agree, on both the length and the route itself.

@words text="1, 3, 4, 2  →  21" sub="the written legs add to 20"
Held Karp returns twenty one, and the tour one, three, four, two. Add up the three legs written down, and you get twenty.

@art leg-home
That isn't a bug. The missing one is the leg home, from two back to one. The list has n cities, and the tour has n legs, so any check has to close the cycle.

@chapter Where the table loses
@math heading="Work" items="Held–Karp: n² · 2ⁿ@n squared;;every order: (n − 1)!@n minus one factorial"
Held Karp fills one entry per subset and end city, and each minimises over up to n predecessors. That's n squared times two to the n. Trying every order is n minus one factorial tours.

@math heading="n² 2ⁿ  vs  (n − 1)!" items="n = 4:  256  vs  6@At four;;n = 6:  2 304  vs  120@At six;;n = 9:  41 472  vs  40 320@At nine;;n = 10:  102 400  vs  362 880@At ten"
At four cities, that's two hundred and fifty six against six. At six, two thousand three hundred and four against a hundred and twenty. At nine, forty one thousand four hundred and seventy two against forty thousand three hundred and twenty, still behind. Only at ten does the table win, and then the gap widens forever.

@art crossing-late
So choosing Held Karp for four cities means choosing the asymptotically better algorithm, and doing over forty times more work. Nothing's wrong with the analysis. What's wrong is treating an asymptotic comparison as advice about one instance.

@words text="A better exponential is still exponential"
And even when it wins, it's still exponential. This problem is NP hard. Held Karp makes twenty cities possible where twelve weren't, but it doesn't make the problem tractable.

@chapter Where people slip
@list heading="Common slips" items="Picking the better asymptotic algorithm for an instance@The first|Re-measuring the tour without closing the cycle@The second|Reading a better exponential as a solution@The third"
The first slip is picking the better asymptotic algorithm without evaluating both at your n. It takes a second. The second is re measuring the tour without the leg home, and hunting for a bug that isn't there. The third is reading a better exponential as a way out.

@chapter Try it
@words text="n = 7 and n = 8" sub="n² 2ⁿ  vs  (n − 1)!"
Your turn. Work out n squared times two to the n, and n minus one factorial, at seven cities and at eight. Which method does less work at each? Then say what that tells you, and what it doesn't.

@end text="Watch the two costs pull apart"
You can solve small tours both ways and watch the two costs cross, on Learn. That's learn dot get er done dot I O.
