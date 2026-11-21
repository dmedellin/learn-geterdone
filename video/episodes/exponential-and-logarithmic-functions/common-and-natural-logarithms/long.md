---
format: long
lesson: exponential-and-logarithmic-functions/common-and-natural-logarithms
title: log and ln: the two logarithms on your calculator
thumb: Find the hidden base
---

@chapter Two bases with nicknames
@title text="Common and Natural Logarithms" sub="Exponential and Logarithmic Functions" art=thumb
Two bases are used so often that they drop the subscript. Log x, with no base written, means base ten. Ln x means base e. Neither is a new function. They're ordinary logarithms with the base hidden.

@math heading="Two names" items="log x  =  log₁₀(x)@common logarithm;;ln x  =  logₑ(x),     e = 2.71828…@natural logarithm"
The common logarithm, log x, is the exponent you put on ten to get x. The natural logarithm, ln x, is the exponent you put on e, the number from compounding. The name natural is historical. e is the base continuous growth is written in, and that's why it's here.

@art two-keys
A standard scientific calculator offers exactly these two keys. That turns out to be enough, because every other base can be computed from either one. And every law you know about logarithms applies to both, unchanged.

@chapter The inverse pairs
@math heading="The same facts, two bases" items="log 10 = 1          ln e = 1@Log ten;;log 1 = 0          ln 1 = 0@Log one;;log(10ᵏ) = k          ln(eᵏ) = k@for every real k;;10^(log x) = x          e^(ln x) = x@for every positive x"
Log ten is one, and ln e is one. Log one is zero, and ln one is zero. Log of ten to the k is k, and ln of e to the k is k, for every real k. And ten to the log x is x, and e to the ln x is x, for every positive x.

@words text="10ᵏ > 0 for every k        log x needs x > 0 first"
Why the different conditions? Ten to the k is positive whatever k is, so its log always exists. But ten to the log x needs x positive first, or there's no log x to raise ten to.

@chapter Match the base before cancelling
@art matched-pair
When the power and the logarithm share a base, they undo each other exactly. Log of ten to the k is k. Ln of e to the k is k.

@math heading="Crossed bases keep a factor" items="log(e²) = 2·log e@Log of e squared;;ln(10³) = 3·ln 10@Ln of ten cubed"
Cross the bases and there's no cancellation. Log of e squared is two log e, not two. Ln of ten cubed is three ln ten, not three. Those answers are exact. They just keep a constant factor.

@art crossed-pair
Write the hidden base once, and the false cancellation becomes visible. Log asks for a power of ten, not a power of e.

@math heading="eˣ = 12" items="x = ln 12@taking ln;;x·log e = log 12    →    x = log 12 / log e@a common logarithm"
So from e to the x equals twelve, taking ln gives x equals ln twelve in one step. Taking a common logarithm is also legal: x log e equals log twelve. Both answers are exact, and equal. Ln is just the shorter route, because its base matches.

@chapter Estimate first
@art bracket-powers
The base gives you a free bracket. Ten cubed is less than forty five hundred, which is less than ten to the fourth. So log of forty five hundred is between three and four. A decimal outside that interval used the wrong base, lost a sign, or was typed wrong.

@math heading="Bracket ln 10" items="e² ≈ 7.389  <  10  <  20.086 ≈ e³@E squared;;2 < ln 10 < 3@between two and three;;ln 10 ≈ 2.302585@about two point three"
The same works for ln. E squared is about seven point three nine, e cubed is about twenty point oh nine, and ten sits between them. So ln ten is between two and three. It's about two point three zero two six.

@chapter One constant apart
@art scaled-curves
The two logarithms are proportional. For every positive x, ln x is ln ten times log x. So the natural log of a number is always about two point three times its common log.

@words text="log 500 ≈ 2.6990        ln 500 ≈ 6.2146"
Log of five hundred is about two point six nine nine. Ln of five hundred is about six point two one four six. A later lesson shows that every pair of bases is related by a constant like this.

@chapter Where people slip
@list heading="Common slips" items="Assuming a bare log is base 10 everywhere@The first|Giving ln rules of its own@The second|Cancelling across different bases@The third"
The first is assuming a bare log means base ten everywhere. It does here and on a calculator, but in analysis it usually means base e, and in computer science, base two. The second is thinking ln has rules of its own. It's log base e, and the same laws apply. The third is cancelling across bases.

@art hidden-base
One habit guards against these. Before you do anything with a bare log or an ln, write its hidden base in. Then the right cancellation, or the right factor, is plain to see.

@chapter Try it
@words text="log(10⁻⁶)        ln(e^(5/2))        log(e³)" sub="first:   write each as log₁₀ or logₑ"
Your turn. Take log of ten to the minus six, ln of e to the five halves, and log of e cubed. First write each with its hidden base. Evaluate the matching pairs exactly, leave the crossed one in exact form, and bracket it using nearby powers of ten.

@end text="Two hidden bases, one argument"
You can enter any positive number and compare the exponents that base ten and base e need, on Learn. That's learn dot get er done dot I O.
