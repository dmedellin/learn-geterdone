---
format: long
lesson: knowledge-and-evidence/conditional-credence-and-base-rates
title: A 99% accurate test, and why most of its positives are false
thumb: Positive, and probably fine
---

@chapter Two directions
@title text="Conditional Credence and Base Rates" sub="Knowledge and Evidence" art=thumb
A test is right ninety nine times in a hundred for people who have a condition. You test positive. How worried should you be? Probably a lot less than you think.

@art grandmothers
Start with something simpler. Almost every grandmother is a woman. Very few women are grandmothers. Those two statements are about different groups, and nothing forces their proportions to match.

@math heading="Conditional credence" items="P(A | B) = P(A ∧ B) / P(B)@the credence in A given B;;P(B) > 0@above zero"
A conditional credence makes that difference exact. The credence in A given B is the credence in A and B together, divided by the credence in B, defined when the credence in B is above zero. It's the credence you'd hold in A if you learned B and nothing else. And the direction of the bar matters.

@chapter The test
@list heading="The test" items="1 in 1,000 have the condition@One person in a thousand|99 in 100 of them test positive@ninety nine in a hundred|5 in 100 of the others test positive@five in a hundred"
Now the test. One person in a thousand has the condition. The test is positive for ninety nine in a hundred of those who have it. And it's positive for five in a hundred of those who don't. Someone tests positive. How likely is it that they have it?

@art million-split
The easiest way to answer is to count a million people. Split them by the condition first. A thousand have it. Nine hundred and ninety nine thousand don't. And don't skip that second group. It's the larger one.

@math heading="A million people" items="have it: 1,000  →  990 positive@Of the thousand;;don't: 999,000  →  49,950 positive@Of the nine hundred;;all positives: 990 + 49,950 = 50,940@Everyone who tests positive"
Of the thousand who have it, ninety nine in a hundred test positive. That's nine hundred and ninety. Of the nine hundred and ninety nine thousand who don't, five in a hundred test positive. That's forty nine thousand, nine hundred and fifty. Everyone who tests positive: fifty thousand, nine hundred and forty people.

@math heading="Divide" items="P(D | +) = 990 / 50,940 = 11/566 ≈ 1.9%@nine hundred and ninety over;;P(+ | D) = 990 / 1,000 = 99/100@ninety nine hundredths"
So the chance of having the condition given a positive is nine hundred and ninety over fifty thousand, nine hundred and forty. That's eleven over five hundred and sixty six, about one point nine percent. The ninety nine in a hundred was the other direction, ninety nine hundredths. Same numerator, different denominators.

@art bar-direction
That's the whole difference between them. One divides by the thousand people who have the condition. The other divides by the fifty thousand, nine hundred and forty who tested positive. A statement about how often the test finds the condition isn't a statement about how often a positive is right.

@chapter Why it happens
@art false-alarms
The reason is the size of the healthy group. There are nine hundred and ninety nine healthy people for every sick one. So a false positive rate of five in a hundred produces about fifty false positives for every true one. Reading one direction as the other is called base rate neglect.

@chapter The base rate is an input
@math heading="Same test, different people" items="1 in 1,000 tested:  P(D | +) = 11/566@one in a thousand;;30 in 100 tested:  P(D | +) = 297/332 ≈ 89%@thirty in a hundred"
Hold the test fixed and change who's tested. At one in a thousand, a positive was worth eleven over five hundred and sixty six. If thirty in a hundred of those tested have the condition, the same test gives two hundred and ninety seven over three hundred and thirty two, about eighty nine percent. Nothing about the test changed. The people did.

@art two-populations
So a positive result is worth what the population makes it worth. With more true positives against about the same stream of false ones, the positives are mostly real.

@art negative-result
And a negative result is the other half of the table. Of the nine hundred and forty nine thousand and sixty who test negative, only ten have the condition. In this population, a negative is far more conclusive than a positive, which isn't what ninety nine percent accurate suggests.

@chapter Where people slip
@list heading="Common slips" items="Reading P(+ | D) as P(D | +)@The first|Treating the base rate as background@The second|Applying the number to anyone who tested positive@the third"
The first slip is reading one direction of the bar as the other. The second is treating the base rate as background. It's as much an input as the test. And the third is applying the number to any person who tested positive. Someone tested because of symptoms isn't drawn from the same population. The count is exact about its group, and silent about which group a person belongs to.

@chapter Try it
@words text="“The test is 99% accurate, so a positive means a 99% chance.”"
Here's one to try. A friend says, the test is ninety nine percent accurate, so a positive means a ninety nine percent chance of having the condition. What's missing? Count a million people again, and find it.

@end text="Count the positives yourself"
You can change the base rate and the error rates and watch the true positives shrink, on Learn. That's learn dot get er done dot I O.
