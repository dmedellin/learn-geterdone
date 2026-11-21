---
format: long
lesson: intro-algorithms-design-techniques/activity-selection-and-the-greedy-strategy
title: Activity selection and when greedy is provably right
thumb: Take whatever finishes first
---

@chapter Looks best now
@title text="Activity Selection and the Greedy Strategy" sub="Introduction to Algorithms, Sections 16.1 and 16.2" art=thumb
Chapter sixteen opens with one line.

@quote text="A greedy algorithm always makes the choice that looks best at the moment." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 16"
A greedy algorithm always makes the choice that looks best at the moment. The hope is that choices that look best locally add up to the best overall. Often they don't. The chapter studies problems where they do.

@chapter The problem
@art timeline-activities
Several activities want one lecture hall, each for a time interval from its start up to its finish. Pick as many as possible that don't overlap. One finishing at six and another starting at six are fine together.

@words text="Dynamic programming would work" sub="cut and paste gives optimal substructure"
The authors take the long way round first. The problem has optimal substructure, by cut and paste, and a table trying every activity in each subproblem would work. It would also be overlooking something.

@chapter The greedy choice
@art earliest-finish
Pick the activity that finishes first. That leaves as much of the day as possible for everything else. Then solve only what's left, the activities starting at or after it finishes.

@art exchange-swap
Theorem sixteen point one proves this is safe, by an exchange. Take any best schedule, and its earliest finishing activity. If that isn't the greedy choice, swap the greedy choice in. It finishes no later, so the schedule stays compatible, and it's just as big.

@words text="Sort by finish, then one scan: Θ(n)" sub="take the next activity that starts after the last finish"
So the table turns into a single scan. Sort by finish time, then take each activity that starts no earlier than the last chosen one finished. Each activity is examined once.

@math heading="Ten activities, by finish" items="take 1-3@take one to three;;skip 2-5, take 4-6@skip two to five;;skip 5-8, 0-9, take 7-10@seven to ten;;skip 9-11, 6-13, take 11-14@eleven to fourteen;;skip 12-15: four activities@four activities"
Here are ten activities, sorted by finish. Take one to three, skip two to five because it starts too early, and take four to six. Skip five to eight and zero to nine, and take seven to ten. Then skip nine to eleven and six to thirteen, take eleven to fourteen, and skip twelve to fifteen: four activities.

@art start-trap
Other sensible rules fail. Earliest start takes zero to nine first, which blocks everything before nine, and gets only three. The lab has instances where shortest first, and fewest conflicts, lose too.

@chapter The general recipe
@list heading="Three steps" items="Cast it as a choice leaving one subproblem@a choice|Prove some optimum makes the greedy choice@some optimal solution|Greedy choice plus optimal rest is optimal@the rest"
Section sixteen point two gives the recipe. Cast the problem as a choice that leaves one subproblem. Prove that some optimal solution makes the greedy choice. And show the greedy choice plus an optimal solution to the rest is optimal. Beneath almost every greedy algorithm, the authors add, lies a more cumbersome dynamic program.

@words text="Choose first, then solve" sub="dynamic programming: solve first, then choose"
Both methods need optimal substructure. The difference is the order. Dynamic programming solves the subproblems first and then chooses, with their answers in hand, usually bottom up. A greedy algorithm chooses first, then solves the single subproblem its choice leaves, usually top down.

@chapter The knapsack warning
@art knapsack-whole
Both knapsack problems have optimal substructure, but only one yields to greedy. Capacity seven, items of weight one, three and four, worth three, seven and nine. Best value per pound first takes the first two, for ten, and the third won't fit. But the second and third together weigh seven, and are worth sixteen.

@art knapsack-fraction
If you may take fractions, greedy wins. Take the first two, and three quarters of the third: three plus seven plus six point seven five is sixteen point seven five, which is optimal. With whole items, each one must be weighed against leaving it out, and that needs dynamic programming.

@chapter Common slips
@list heading="Common slips" items="Trusting a rule because it sounds sensible@The first|Reading one agreement as the proof@The second|Expecting the knapsack to yield to greedy@the third"
The first slip is trusting a greedy rule because it sounds sensible. The second is reading one agreement with the optimum as a proof. And the third is expecting the whole item knapsack to yield to greedy too.

@chapter Try it
@words text="Start last, work backwards" sub="Exercise 16.1-2"
Your turn. On the same ten activities, pick the one that starts last, and work backwards, taking each activity that finishes by the time the last chosen one starts. Compare its selection and size with the earliest finish rule.

@end text="Break the greedy rules"
You can run four greedy rules against every subset, and watch three of them fail, on Learn. That's learn dot get er done dot I O.
