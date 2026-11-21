---
format: long
lesson: greedy-and-matroids/the-exchange-argument
title: The exchange argument: proving a greedy rule, one swap at a time
thumb: Swap the optimum into greedy
---

@chapter The question
@title text="The Exchange Argument" sub="Greedy Algorithms and Matroids" art=thumb
Testing a greedy rule on examples can only ever catch it out. To show it's right on every input, you need a proof. The standard one is the exchange argument, and here you'll watch it run, and watch it break.

@art chain-of-swaps
The idea is surprising. You don't build the optimum. You take any optimal solution, whatever it is, and edit it, one swap at a time, until it becomes greedy's answer. If optimality survives every edit, greedy's answer was optimal all along.

@chapter The procedure
@math heading="The exchange" items="g₁, g₂, …, g_k = greedy's choices, in order@g one;;O = any optimal solution@O be any;;swap i:  put gᵢ into O at position i@swap i;;check: still feasible?  still the same size?@two things"
Let g one, g two, up to g k be greedy's choices in the order it made them, and let O be any optimal solution. At swap i, put g i into O in the i th position, dropping whatever was there. After every swap, check two things. Is the set still feasible, and is it still the same size?

@art optimum-to-greedy
If both checks pass every time, then after k swaps the set holds all of greedy's choices and is still optimal. And it can't be bigger than greedy's answer, because greedy only stopped when nothing more would fit. That's where the rule's own stopping condition enters the proof.

@chapter Three intervals
@words text="A 0–5 · B 4–6 · C 5–10" sub="optimum: A C, size 2"
Take three intervals. A from zero to five, B from four to six, and C from five to ten. Of the eight subsets, the best is A and C, size two.

@list heading="Two rules" items="Earliest finish: greedy = A C → both swaps already in place@Under earliest finish|Shortest first: greedy = B → swap 1 gives B C@Under shortest first|B 4–6 and C 5–10 overlap@B runs from four"
Under earliest finish, greedy also picks A and C, so both swaps find their target already there, and the chain survives. Under shortest first, greedy picks B alone. The first swap puts B in for A, giving B and C. Same size, but B runs from four to six and C from five to ten. They overlap.

@art swap-overlap
That's the whole negative result, in one swap. The proof doesn't just fail to apply to shortest first. It produces a specific illegal set, at a named step, from a specific optimum.

@chapter Two ways to fail
@art swap-shrink
A swap has two obligations, and they fail independently. Under earliest start on its trap, the first swap gives a set of the right size that overlaps. Under fewest conflicts on its trap, the second swap gives a set that's perfectly feasible, but has three intervals where the optimum had four.

@words text="Feasible? · Same size?" sub="both checks fire, on different instances"
So the size check and the feasibility check both fire, on different instances. Watch only one kind of trap, and you'd wrongly think the argument always breaks the same way.

@chapter Why earliest finish survives
@art finish-earlier
Now the proof. Take the first position i where O and greedy differ, and let o be O's i th interval. Greedy looked at every interval compatible with its first choices, and took the one that finishes earliest. So g i finishes no later than o.

@math heading="The one inequality" items="f(gᵢ) ≤ f(o)@f of g i;;every later interval of O starts ≥ f(o) ≥ f(gᵢ)@every later interval;;one out, one in  →  same size@One interval out"
F of g i is less than or equal to f of o. Every later interval of O starts at or after f of o, so it also starts after g i finishes. Feasibility holds. One interval out and one in, so the size holds too. Repeat, and the first difference moves forward each time.

@words text="f(gᵢ) ≤ f(o)" sub="the step the other three rules can't make"
That single inequality is the whole content of the proof. Nothing about sorting by length, start time, or conflict count makes greedy finish no later than the optimum. The traps are exactly instances where it finishes later.

@chapter A chain that does nothing
@art already-there
One trap in reading the lab. On the eleven interval instance under earliest finish, all four swaps say already there. The optimum the panel found is greedy's own answer, so nothing was exchanged, and nothing was tested. Switch to shortest first, and the first swap is real: A out, B in, still feasible, still four.

@chapter Where people slip
@list heading="Common slips" items="Treating a surviving chain as the proof@The first|Checking only the failure you expect@The second|Swapping in the optimum's order@The third"
The first slip is treating a surviving chain as the proof. It edits one optimum on one instance. The second is checking only the failure you expect, overlap or lost size. The third is swapping in the optimum's order. The index runs over greedy's choices, so write them down first.

@chapter Try it
@words text="0–10 · 1–2 · 3–4 · 5–6 · 7–8" sub="earliest start: run the chain"
Try the earliest start trap: zero to ten, then one to two, three to four, five to six and seven to eight. Greedy takes only the long one. Do the first swap by hand. Which check fails, and why does a broken chain count against the rule?

@end text="Watch each swap survive or break"
You can run the exchange chain on every rule and watch the step where it breaks, on Learn. That's learn dot get er done dot I O.
