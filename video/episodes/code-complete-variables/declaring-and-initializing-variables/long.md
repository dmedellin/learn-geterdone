---
format: long
lesson: code-complete-variables/declaring-and-initializing-variables
title: The value you didn't expect: declaring and initializing variables
thumb: Initialize it where you declare it
---

@chapter The problem
@title text="Declaring and Initializing Variables" sub="Code Complete, chapter 10" art=thumb
Part three of Code Complete starts with the humblest thing in a program, the variable. How it's declared, and how it gets its first value. That second part turns out to be where a lot of bugs live.

@quote text="Data initialization is prone to errors, so use the initialization techniques described in this chapter to avoid the problems caused by unexpected initial values." cite="McConnell, Code Complete, 2nd ed., Chapter 10, p. 258"
Here's the chapter's first key point. Data initialization is prone to errors, so use the initialization techniques described in this chapter to avoid the problems caused by unexpected initial values.

@chapter Declarations
@art typo-twin
Some languages declare a variable for you the first time you use it. McConnell counts that among the most dangerous features a language can have. Type account no where you meant account num, and you've got a second variable, silently initialised, and a bug.

@words text="acctNo ≠ acctNum" sub="in Java, that slip takes two mistakes"
Account no is not account num. In a language that requires declarations, the same slip takes two mistakes: a wrong name, and a declaration to match it. Java is such a language, so this half of the advice is done for you.

@chapter Unexpected initial values
@list heading="Every initialisation error" items="Never assigned@never assigned|Out of date@out of date|Only partly assigned@part of it"
Improper initialisation, McConnell says, is among the richest sources of error in programming. And every case comes down to one thing: a variable holding an initial value you didn't expect. It was never assigned. Or its value is out of date. Or part of it was assigned and part wasn't.

@art proximity
So initialise each variable as it's declared. He calls that cheap insurance. Where you can't, initialise it close to where it's first used, not in a block at the top. That's the Principle of Proximity: keep related actions together.

@art loop-outside
Here's why the block at the top hurts. A loop is later built around the code, the initialisation is left outside it, and the second pass starts with the first pass's value.

@art counter-reset
Pay special attention to counters and accumulators, which are easy to forget to reset before their next use. Use final for anything that shouldn't change once it's set. Check input parameters before you use them. And read your compiler's warnings.

@chapter Three anomalies
@list heading="Data-flow anomalies" items="Used before set@used before set|Set twice@set twice|Set, never used@never used"
Chapter twenty two names patterns of what happens to a variable that deserve suspicion. The lab looks for three. Used before set, a read with nothing setting it first. Set twice, with no read between. And set, never used.

@art read-before-set
The lesson's first routine averages an array of prices. Line two declares count and gives it no value. Line six reads count to add one to it, and nothing above has set it. One anomaly, used before set. Java's compiler goes further, and refuses to compile it.

@code block=2 lines=1-9 label=Java focus="2-3@beside the total|6@adds one"
The fix is to initialise count to zero, right beside the total. Now each pass adds one to a value you chose, and the lab reports no anomaly at all.

@art set-twice
Now the case Java lets through. Someone replaces the loop with two assignments, and keeps the old initialisations.

@list heading="Set twice" items="total = 0.0, then total = prices[0]@total is set|count = 0, then count = prices.length@count is set|average set, never read@average"
So total is set to zero, then overwritten by the first price. Count is set to zero, then overwritten by the length. And a variable called average is set, and never read.

@words text="The first price ÷ the count" sub="compiles · runs · not an average"
It compiles, and it runs. And it returns the first price divided by the number of prices, which is not an average. Java's compiler doesn't question a value set and thrown away, or a variable never used.

@chapter Where people slip
@list heading="Common slips" items="If it compiles, every value is right@The first|Initialising everything at the top@The second|An unused variable is harmless@the third"
The first slip is thinking that if it compiles, every variable holds what you meant. A field declared without a value starts at zero, with no complaint. The second is initialising everything in a block at the top. And the third is treating an unused variable as harmless. The book cites a study linking unreferenced variables with higher fault rates.

@chapter Try it
@code block=4 lines=1-8 label=Java focus="3-5@if the first name|6@then line six"
Your turn. This routine builds a person's initials. If the first name isn't empty, it sets result. Then line six adds the last initial. Read it top to bottom and list the anomalies. Then say whether Java accepts it, and if not, on which path a line reads a variable nothing has set.

@end text="Read a routine for anomalies"
You can paste a routine into the lab and see every read before a set, on Learn. That's learn dot get er done dot I O.
