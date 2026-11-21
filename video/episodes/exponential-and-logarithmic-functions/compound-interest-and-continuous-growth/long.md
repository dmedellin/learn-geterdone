---
format: long
lesson: exponential-and-logarithmic-functions/compound-interest-and-continuous-growth
title: Compound interest and continuous growth, built from scratch
thumb: Compounding has a ceiling
---

@chapter Built, not memorised
@title text="Compound Interest and Continuous Growth" sub="Exponential and Logarithmic Functions" art=thumb
Two formulas look like conventions until you build them. P times one plus r over n, to the n t, is one multiplication repeated n t times. And P e to the r t is where that expression settles as n grows. No new fact about money is involved.

@words text="P,   r,   n,   t" sub="principal  ·  nominal annual rate  ·  times a year  ·  years"
A principal P is invested at a nominal annual rate r, compounded n times a year, for t years. Every one of those has a unit, and most errors with these formulas are unit errors, not algebra errors.

@art year-periods
The nominal rate is quoted per year and split evenly among the periods, so one period carries r over n. A nominal five percent compounded monthly means five twelfths of a percent a month.

@chapter Each period multiplies
@math heading="Repeated multiplication" items="after 1 period:    P(1 + r/n)@After one period;;after 2 periods:    P(1 + r/n)²@after two;;after k periods:    P(1 + r/n)ᵏ@after k;;t years = nt periods:    A = P(1 + r/n)^(nt)@t years"
Each period multiplies the balance by one plus r over n. After one period, P times that factor. Then after two, the factor squared, and after k, the factor to the k. And t years is n t periods, so A equals P times one plus r over n, to the n t.

@art period-multiply
That's the whole derivation. The balances form a geometric sequence, multiplied by the same factor each time, never added to.

@math heading="$1000 at 6% for 5 years, quarterly" items="r/n = 0.06/4 = 0.015@one quarter;;nt = 4·5 = 20@twenty quarters;;A = 1000(1.015)²⁰ ≈ 1346.86@about thirteen"
A thousand dollars at six percent for five years, compounded quarterly. The rate for one quarter is point oh six over four, point oh one five. There are twenty quarters. So A is a thousand times one point oh one five to the twentieth, about thirteen hundred and forty six dollars, eighty six.

@chapter Comparing accounts
@words text="effective rate = (1 + r/n)ⁿ − 1" sub="5% monthly:   ≈ 5.1162%"
The effective annual rate is one plus r over n, to the n, minus one. It's the single yearly rate that gives the same balance after a year. For five percent compounded monthly, it's about five point one one six two percent.

@words text="6% monthly  ≈  6.1678% effective" sub="so it beats 6.1% compounded yearly"
Accounts quoted at different frequencies can only be compared this way. Six percent compounded monthly is about six point one six eight percent effective, so it beats six point one percent compounded yearly.

@chapter More often, up to a ceiling
@math heading="$1000 at 5% for 10 years" items="yearly:    1628.89@Yearly;;quarterly:    1643.62@quarterly;;monthly:    1647.01@monthly;;daily:    1648.66@daily;;continuous:    1648.72@continuously"
Now raise n, with a thousand dollars at five percent for ten years. Yearly gives sixteen twenty eight, eighty nine. Then quarterly, sixteen forty three, sixty two. Then monthly, sixteen forty seven, oh one. Then daily, sixteen forty eight, sixty six. And continuously, sixteen forty eight, seventy two.

@art frequency-ceiling
The column climbs and then stops climbing. Daily and continuous differ by about six cents over ten years. Compounded continuously isn't a claim about speed. It's the ceiling of the process.

@words text="P(1 + r/n)^(nt)  →  P·e^(rt)" sub="m = n/r:    P·[(1 + 1/m)ᵐ]^(rt)"
Why e? Substitute m equals n over r, and the expression becomes P times one plus one over m, to the m, all to the r t. As n grows so does m, and the inner bracket tends to e. So the whole thing tends to P e to the r t.

@art simple-vs-compound
For scale, simple interest on the same thousand dollars gives only fifteen hundred.

@chapter Solving for time
@math heading="Doubling, continuously" items="2P = P·e^(rt)@two P;;2 = e^(rt)@the P cancels;;t = ln 2 / r@t equals ln two over r;;5%:    ≈ 13.86 years@At five percent"
To double a balance under continuous growth, set two P equal to P e to the r t. Then the P cancels, so r t is ln two, and t equals ln two over r. At five percent, that's about thirteen point eight six years.

@art doubling-time
The principal cancelling is the mark of exponential growth: the time to double doesn't depend on where you start. Compounded yearly instead, it's about fourteen point two one years.

@chapter Where people slip
@art runaway-bar
The costliest slip is entering the rate as a percent. Five instead of point oh five, compounded monthly, turns a thousand dollars into about one point four times ten to the twenty one dollars in ten years. Nothing in the formula objects.

@list heading="Two more slips" items="Using t where nt belongs@using t|Comparing nominal rates directly@comparing"
The others are using t where n t belongs, and comparing nominal rates directly. Quarterly for five years is twenty compoundings, not five.

@chapter Try it
@words text="$1500 at 4.8%, monthly, for 2 years" sub="period rate 0.048/12,    24 periods"
Your turn. Fifteen hundred dollars at a nominal four point eight percent, compounded monthly, for two years. The period rate and the twenty four periods are given. Build the formula, compute once at the end, and compare it with the continuous value, fifteen hundred times e to the point oh four eight times two.

@end text="Six frequencies and the ceiling"
You can set a principal, a rate and a term, and watch every frequency climb toward the continuous ceiling, on Learn. That's learn dot get er done dot I O.
