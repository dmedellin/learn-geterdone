---
format: long
lesson: paradoxes-and-their-exits/zenos-dichotomy
title: Zeno's dichotomy: can you ever cross the room?
thumb: Halves add up to one
---

@chapter The paradox
@title text="Zeno's Dichotomy" sub="Paradoxes and Their Exits" art=thumb
To cross a room, you first have to get halfway. Then half of what's left, a quarter. Then an eighth. The halving never stops, so the crossing has infinitely many parts. Zeno concludes that you never arrive.

@list heading="Zeno's argument" items="You must complete every step@complete every one|Each step takes a positive time@positive time|Infinitely many positive times add to infinity@infinitely many positive|So you never arrive@never arrive"
Set it out. To cross, you must complete every one of the steps. At constant speed, each step takes a positive time. A sum of infinitely many positive times is infinite. So the crossing takes infinite time, and you never arrive.

@art halving-room
The argument is valid, and the first two premises are as plausible as a description of walking can be. The third has a hidden claim. It says that adding enough positive amounts always passes any size. That's true of equal steps. Whether it's true of steps that shrink is a matter of arithmetic.

@chapter The series
@math heading="The halves" items="1/2 + 1/4 + 1/8 + …@a half;;S(n) = 1 − 1/2ⁿ@one minus;;S(1) = 1/2,  S(2) = 3/4,  S(3) = 7/8@After one step"
The steps form a geometric series: a half, plus a quarter, plus an eighth, and so on. The sum of the first n halves is one minus one over two to the n. After one step it's a half. After two, three quarters. After three, seven eighths.

@math heading="Ten halves" items="S(10) = 1023/1024@ten halves;;remainder:  1/1024@still to go;;limit:  1@The limit"
With ten halves, the sum is one thousand and twenty three over one thousand and twenty four. The remainder, the distance still to go, is one over one thousand and twenty four. The limit is one.

@chapter What the limit means
@art shrinking-remainder
What does it mean to say the infinite sum equals one, when nobody adds infinitely many numbers? It means this. Whatever small fraction you name, the remainder falls below it from some step on, and stays below.

@words text="Name one thousandth" sub="9 steps: 1/512, too large · 10 steps: 1/1024, smaller"
Name one thousandth. After nine steps the remainder is one over five hundred and twelve, still too large. After ten it's one over one thousand and twenty four, smaller, and it stays smaller. Name one millionth, and the twentieth step does it. No number but one is approached that way. That's all the limit is one says.

@chapter A different cut
@art two-thirds-steps
The halves aren't special.

@math heading="Cover two thirds of what's left" items="a = 2/3,  r = 1/3@two thirds;;after 5 steps:  242/243@five steps;;remainder:  1/243,  limit:  1@remainder"
A walker who covers two thirds of what's left at each step has a first term of two thirds and a ratio of one third. After five steps, the sum is two hundred and forty two over two hundred and forty three. The remainder is one over two hundred and forty three, and the limit is again one. A smaller ratio shrinks the remainder faster.

@chapter The exit
@art finite-total
So the third premise is false for these steps. A sum of infinitely many positive times isn't always infinite. When the times shrink in a fixed proportion, the total is finite, and here it's exactly the crossing time. The steps take as long as the crossing, because the steps are the crossing.

@words text="Exit one: deny the third premise" sub="the price: a habit about adding up"
That's exit one. Deny the premise that infinitely many positive times must add to infinity. The series is the refutation. And the price is a habit about adding up, and nothing about walking.

@art space-points
The answer has limits. The arithmetic settles the sum, and the sum was the faulty premise. It doesn't settle whether space is made of points, or can be divided forever, or whether a body can do something at each of an unending list of places. Those are questions about the world, not the series.

@chapter Where people slip
@list heading="Common slips" items="Thinking infinitely many steps take infinitely long@The first|Treating a partial sum as the limit@The second|Reading the series as a proof about space@And the third"
The first slip is thinking infinitely many steps take infinitely long. Only if the steps don't shrink. The second is treating a partial sum as the limit. No finite number of halves reaches one, and the limit doesn't have to. And the third is reading the series as a proof about space. Say which question you mean before claiming Zeno is answered.

@chapter Try it
@art doubling-steps
Slide the number of terms in the lab, and watch the remainder halve each time. Then type two for the ratio, so each step is twice the last. Read the limit tile, and say why it shows none.

@end text="Halves add up to one"
You can slide the steps and watch the remainder shrink, on Learn. That's learn dot get er done dot I O.
