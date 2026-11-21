---
format: long
lesson: paradoxes-and-their-exits/the-two-envelopes
title: The two envelopes paradox: should you always switch?
thumb: Switch forever?
---

@chapter The argument
@title text="The Two Envelopes" sub="Paradoxes and Their Exits" art=thumb
Two sealed envelopes hold money. One holds some amount, and the other holds exactly double. You're given one at random, and may keep it or swap. You open yours, and find eight.

@art two-envelopes
The other, you reason, holds four if yours is the larger, and sixteen if yours is the smaller. And the two cases are equally likely, because you were handed yours by chance.

@math heading="After finding 8" items="other = 4,  chance 1/2@four;;other = 16,  chance 1/2@sixteen;;switch = (1/2)·4 + (1/2)·16 = 10@worth"
So the other is four, with chance one half, or sixteen, with chance one half. Switching is worth a half times four plus a half times sixteen, which is ten. Ten is more than eight, so switch.

@chapter Why it's a paradox
@math heading="Whatever you find" items="switch = (1/2)·(x/2) + (1/2)·2x = 5x/4@five x over four"
Nothing here depends on eight. Find x, and the other is worth a half of x over two, plus a half of two x, which is five x over four. More than x. So you'd switch whatever you found.

@art endless-swap
So you may as well switch without opening. And having switched, the same argument says to switch back. A rule that recommends swapping forever, between envelopes that were symmetric to begin with, is what makes this a paradox.

@chapter The closed version
@words text="(1/2)·2y + (1/2)·y, either way" sub="the x in x/2 and in 2x is not one number"
Run without opening, the argument equivocates. The letter x is your amount in both cases. But if the pair is y and two y, yours is the smaller in one case and the larger in the other. So the two x's aren't the same number. Written with y, switching and keeping are worth the same. That's exit two, a step that only looked valid.

@chapter The open version
@art opened-envelope
Run after opening, with the eight in hand, the step is sound. Four and sixteen are definite amounts. So look at the premises. The envelopes hold an amount and its double. That's the setup. Pick the act of greater expected value. That was defended earlier. And the chance the other is double is one half. That one isn't part of the setup.

@art posterior-scale
Why was it thought to be? Before you open anything, the chance yours is the smaller is one half. The argument carries that across the opening. But the amount you see is evidence. A small amount suggests the smaller envelope, a large one the larger. After opening, the chance is a posterior, and it depends on a prior over the pairs.

@chapter A bounded prior
@art top-of-list
Suppose the prior is bounded, so the pairs come from a finite list. Then there's a largest amount, and when you see it, you know yours is the larger. Switching gets you half. At the smallest amount, it's the mirror image. So the chance of double is zero at one end, and one at the other.

@math heading="Same 8, different priors" items="prior 1/2 each:  switch 10,  keep 8@one half each;;8 is the top:  switch 4,  keep 8@largest amount;;8 is the bottom:  switch 16@third"
The lab shows it. With a prior of one half each, switching is worth ten against eight. If eight is the largest amount, the prior on sixteen is zero, and switching is worth only four. In the third case, switching is worth sixteen. The same arithmetic, with a different prior, reverses the advice. No single act is best at every amount.

@art prior-dial
The reply has a price. It gives up a very natural thought, that when you know nothing about the amounts, the two cases are equally likely. A bounded prior doesn't say that's always wrong. It says it can't be right at every amount, and leaves you free to hold it in the middle of the list.

@chapter Where people slip
@list heading="Common slips" items="Thinking symmetry shows switching is always better@The first|Carrying the pre-opening chance across the opening@The second|Reading the lab's best act as real advice@And the third"
The first slip is thinking symmetry shows switching is always better. The second is carrying the chance from before the opening across it. Treat the amount as evidence, and recompute. And the third is reading the lab's best act as advice about real envelopes. The prior is a number you typed.

@chapter Try it
@words text="prior 3/4 and 1/4" sub="then find where keeping and switching tie"
Move the prior in the first case to three quarters on the larger, and a quarter on the smaller, and work out switching. Then find the prior at which keeping and switching tie.

@end text="Switching, given a prior"
You can set the prior and compare keeping and switching, on Learn. That's learn dot get er done dot I O.
