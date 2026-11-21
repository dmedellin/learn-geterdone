---
format: long
lesson: enterprise-patterns-layers-and-performance/performance-terms
title: Which system is faster? It depends on the load
thumb: Faster at what load?
---

@chapter The caution
@title text="Thinking About Performance" sub="Patterns of Enterprise Application Architecture, Introduction" art=thumb
Which of two systems is faster? It sounds like a question with one answer. Martin Fowler's section on performance shows it isn't.

@quote text="any advice about performance should not be treated as fact until it's measured on your configuration." cite="Fowler, Patterns of Enterprise Application Architecture, Introduction"
He starts with a caution. Any advice about performance should not be treated as fact until it's measured on your configuration. That includes his own advice, and the rest of the book holds itself to it.

@words text="Measure before · measure after" sub="and again when the setup changes"
For most problems he'd rather get the system running, instrument it, and optimise by measurement. Measure before and after every change. And measure again when the configuration changes, because a new virtual machine, database or piece of hardware can turn an old optimisation into a cost.

@chapter Response time and responsiveness
@art stopwatch
Then come his terms. Response time is how long the system takes to process a request from outside, like a button press or an API call.

@art progress-bar
Responsiveness is how quickly the request is acknowledged. Show a progress bar while a file copies, and you improve responsiveness while leaving response time exactly as it was. If the system says nothing until it's done, the two are the same.

@chapter Latency and throughput
@art remote-call
Latency is the least time any response takes at all. Fowler's picture is a program asked to do nothing and report when it's finished. On his laptop, it's instant. On a remote machine, it may take seconds. That wait is why remote calls should be few.

@art conveyor
Throughput is how much gets done in a given time. For enterprise applications, that's usually transactions a second. And by performance, Fowler means whichever of throughput and response time matters more to you. He'd rather you name the one you mean.

@chapter Load
@art crowd-load
Load is how much stress the system is under, like how many users are connected. It's the context for another figure: a response time is always at some load. And load sensitivity is how response time changes as load changes.

@code block=1 lines=1-6 label=Java focus="1@its comment|3@reads the clock|4@handles one request|5@divides by a million"
Here's the measurement all of this rests on, written for the lesson. It reads the clock, handles one request, and divides by a million to turn nanoseconds into milliseconds. And its comment makes Fowler's point. The figure is a response time at whatever load the system was under, and it means nothing without that load beside it.

@chapter Two systems
@math heading="The book's illustration" items="A: 500 ms at 10 users, 500 ms at 20@System A;;B: 200 ms at 10 users, 2,000 ms at 20@System B"
Fowler's illustration is two systems. System A answers in half a second, from ten users through twenty. System B answers in a fifth of a second at ten users, and two seconds at twenty. These are the book's figures, not a real measurement.

@math heading="Per user, and the ratio" items="A: 0 ms a user · 1×@A rises zero;;B: 1,800 ms ÷ 10 users = 180 ms a user@B rises;;B: 2,000 ÷ 200 = 10×@ten times"
Work out the change a user. A rises zero milliseconds a user. B rises eighteen hundred milliseconds over ten users, so a hundred and eighty a user. And B's last time over its first is ten times. B is the more load sensitive. It degrades more.

@math heading="On a straight line between them" items="at 10 users: A 500 ms, B 200 ms@At ten users;;at 15 users: A 500 ms, B 1,100 ms@at fifteen;;200 + 180 × (u − 10) = 500 → u a little below 12@a little below twelve"
At ten users, B is faster by three hundred milliseconds. Read each on a straight line, and at fifteen, A is faster by six hundred. They meet a little below twelve users. That straight line is the lab's assumption, not the book's.

@art two-curves
So neither system is faster. Each is faster at some load, and the figure that decides is the load you expect. That's why Fowler keeps response time and load sensitivity apart.

@chapter Where people slip
@list heading="Common slips" items="Faster at one load means faster at all@The first|Responsiveness is response time@The second|A performance tip is a fact@And the third"
The first slip is thinking the faster system at one load is faster at every load. The second is treating responsiveness and response time as one thing. And the third is taking a performance tip as a fact, before you've measured it on your own setup.

@chapter Try it
@words text="North: 400 ms @ 5, 1,400 ms @ 25" sub="South: 900 ms @ 5, 1,000 ms @ 25"
Your turn. System north answers in four hundred milliseconds at five users, and fourteen hundred at twenty five. System south answers in nine hundred at five, and a thousand at twenty five. Find each one's change a user and its ratio. Read both at twenty users, and say which is faster there, and which at five.

@end text="Measure two systems yourself"
You can type in measurements and read any load between them, on Learn. That's learn dot get er done dot I O.
