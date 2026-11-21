---
format: long
lesson: data-structures/stacks-queues-and-the-two-stack-queue
title: A queue from two stacks, and why it costs three per item
thumb: Paid for in advance
---

@chapter The question
@title text="Stacks, Queues, and the Two-Stack Queue" sub="Data Structures" art=thumb
Can you build a queue out of two stacks? You can. One dequeue will sometimes cost as much as the whole queue. And yet the total stays small. Here's how both are true.

@art stack-and-queue
A stack works at one end. Push and pop, and what comes out is the most recent thing in. A queue works at two ends. Enqueue at one, dequeue at the other, and what comes out is the oldest. Neither lets you ask what's at position seven, and refusing that question is what makes them cheap.

@chapter The trick
@art two-stacks
Keep two stacks, called in and out. To enqueue, push onto in. To dequeue, first check out. If it's empty, pop everything from in and push it onto out. Then pop out.

@art pour-across
Pouring across reverses the order. And since a stack already reverses, two reversals put things back. So whatever comes off out is the oldest element still in the queue.

@math heading="Cost, one per push, pop or move" items="enqueue:  1@an enqueue;;dequeue, OUT not empty:  1@isn't empty;;dequeue, OUT empty, k in IN:  k + 1@k plus one"
Charge one for every push, pop and move. An enqueue always costs one. A dequeue costs one if out isn't empty. If out is empty and in holds k elements, it costs k plus one: k moves, then the pop.

@chapter Three in, three out
@math heading="E E E D D D" items="costs:  1, 1, 1, 4, 1, 1@one, one, one;;total:  9@adds to nine;;3 arrivals × 3 = 9@three each"
Try three enqueues, then three dequeues. The costs are one, one, one, then four, then one and one. That adds to nine. The four is the first dequeue: three moves and a pop. Nine for three arrivals is exactly three each.

@words text="The expensive step is still there" sub="one operation cost 4× the others"
Notice what didn't happen. The expensive dequeue didn't go away. One operation out of six cost four times the others. The bound is about the total, not about any single step.

@art sequence-steps
Picture the six costs as bars. Five are short, and one, the first dequeue, stands four times taller. The bound says nothing about which bar paid. It only says the bars together come to nine.

@chapter Paying in advance
@list heading="A budget of 3 per enqueue" items="1 for the push, now@one for the push|1 for the move, later@one for the move|1 for the pop, at the end@one for the pop"
So here's the argument. Give every enqueue a budget of three. One for the push that happens now, one for the move this element makes later, and one for the pop that finally removes it.

@art one-way-trip
Nothing else ever touches an element. It enters once, moves from in to out at most once, and is popped once. It never goes back. So its three units cover everything that will ever happen to it, and m enqueues cost at most three m.

@math heading="The credit balance" items="credit = charged − real@charged total;;E E E D D D:  2, 4, 6, 2, 1, 0@two, four, six;;never negative ⟹ real ≤ 3m@never negative"
Formally, the credit is the charged total minus the real total. On our sequence it reads two, four, six, then two, one, zero. It's never negative, so the real cost never exceeded the charges, which is three m.

@art credit-bank
And the credit isn't stored anywhere. There's no counter in the code. The bank is a device in the proof, and the structure doesn't change at all.

@chapter What a run shows
@words text="E E E D D D: total 9 · bound 9" sub="E D E D E D E D: total 12 · bound 12"
On three in, three out, the total is nine and the bound is nine. On E D, four times over, both are twelve. They agree because every element that arrived was also served, so each one really paid all three charges.

@words text="Enqueue only: m against 3m"
A sequence that only enqueues costs m against a bound of three m, so there the bound is loose. And no run can establish the bound, because the bound is about every sequence, and a run is just one.

@chapter Where people slip
@list heading="Common slips" items="Reading amortised as every operation fast@The first|Taking a run under the line as the proof@The second|Looking for where the credit is stored@And the third"
The first slip is reading amortised as a promise about every operation. It's a promise about the total, so a real time deadline needs a worst case structure instead. The second is thinking the bound is proved because a run stayed under it. And the third is looking for where the credit lives.

@chapter Try it
@words text="E E D E E D E E D D D D" sub="total 18 · one dequeue costs 5 · bound 18"
Here's one to trace. Twelve operations: E E D, E E D, E E D, then D D D. The lab gets a total of eighteen, with one dequeue costing five, against a bound of eighteen. Track in, out and the credit at each step, and find the five.

@end text="Watch the credit stay non-negative"
You can type your own sequence and watch the credit balance after every step, on Learn. That's learn dot get er done dot I O.
