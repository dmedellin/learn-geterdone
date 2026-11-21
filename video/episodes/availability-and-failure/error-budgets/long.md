---
format: long
lesson: availability-and-failure/error-budgets
title: Error budgets: why a half-broken hour costs half a dead one
thumb: Count failures, not minutes
---

@chapter The question
@title text="Error Budgets" sub="Availability and Failure" art=thumb
Your service never went down this month. Every uptime check was green. And you blew your entire error budget. Here's how that's possible, and how to count it.

@art budget-jar
A service level objective sets a target for an indicator over a period, here the fraction of requests that succeed. The error budget is the failure that objective permits. It's a count, fixed when the period begins, and incidents spend it until it's gone.

@chapter The budget is a count
@math heading="99.9% at 1000 rps, a month" items="N = 1000 × 2 628 000 = 2 628 000 000 requests@a thousand requests;;budget = (1 − SLO) × N = 2 628 000 failures@the budget;;as time: (1/1000) × 2 628 000 s = 43 min 48 s@as time"
At a thousand requests a second over a month, that's two point six two eight billion requests. Three nines permits a thousandth of them to fail, so the budget is two million six hundred and twenty eight thousand failures. As time, it's the familiar forty three minutes forty eight seconds of complete outage.

@words text="43 min 48 s is the special case" sub="every request failing"
Both describe the same permission, and the second is the one everybody quotes. But it's only right if every single request is failing. That's the least likely incident shape there is.

@chapter What an incident spends
@math heading="The burn" items="burn = rate × duration × failed fraction@spends its rate"
An incident spends its rate, times its duration, times the fraction of requests that failed. That third factor is the one uptime monitoring doesn't have.

@list heading="30 minutes at 1000 rps" items="10% failing:  180 000 · 6.85%@ten percent|25%:  450 000 · 17.12%@twenty five|50%:  900 000 · 34.25%@fifty|100%:  1 800 000 · 68.49%@a full outage"
Thirty minutes at ten percent failing burns a hundred and eighty thousand, six point eight five percent of the budget. Twenty five percent burns seventeen percent. Fifty burns thirty four. And a full outage burns one point eight million, sixty eight point four nine percent.

@art partial-burn
So a half broken hour costs half of what a dead hour costs. And quoting forty three point eight minutes as the budget understates, by a factor of ten, what a long degradation at ten percent is allowed to cost. At ten percent, the whole budget lasts four hundred and thirty eight minutes.

@chapter Two incidents
@math heading="2000 rps · budget 5 256 000" items="A:  8 min at 100%  →  960 000 = 18.26%@incident A;;B:  6 h at 15%  →  6 480 000 = 123.29%@incident B;;total 7 440 000 = 141.55%@total spent"
Now a month at two thousand requests a second, with a budget of five million two hundred and fifty six thousand. Incident A is eight minutes of total outage, eighteen percent of the budget. Incident B is six hours where one request in seven fails, a hundred and twenty three percent. Total spent, a hundred and forty one percent.

@art green-checks
Uptime monitoring saw eight minutes against forty three, and called it comfortable. But incident B never took the service down, so every check stayed green, and it spent more than the whole month on its own. The request measure sees it, because severity is one of its factors.

@chapter Where the arithmetic stops
@art policy-split
What happens when the budget is spent is a policy decision. Freeze releases, divert the team, revise the objective, accept it. The arithmetic informs that and doesn't make it. But now the argument happens over an agreed number.

@art overrun-gauge
And sometimes the arithmetic settles it. At four nines, one thirty minute outage burns six hundred and eighty four point nine three percent of the month. An objective an ordinary incident can't fit inside isn't a target.

@art heavy-customer
One caution. A request weighted objective forgives quiet hours and punishes peaks. If one customer sends a million requests and ten send a thousand, it's mostly about that one customer. That's a choice to make deliberately.

@chapter Where people slip
@list heading="Common slips" items="Measuring uptime for a success-ratio objective@The first|Quoting the budget only as minutes@The second|Confusing the arithmetic with the policy@The third"
The first slip is measuring uptime when the objective is a success ratio. The second is quoting the budget only as minutes. And the third is confusing the arithmetic with the policy. We spent sixty eight percent is a computation. Therefore we freeze releases is a decision.

@chapter Try it
@words text="99.9% · 2000 rps · 5% severity" sub="minutes = budget ÷ (rate × severity)"
Your turn. Same objective and rate. How long can a five percent degradation run before it exhausts the month? Severity is a multiplier, so divide the budget by rate times severity. Then say what that implies about how fast a partial degradation must be detected.

@end text="Set the severity, watch the budget burn"
You can run incidents of any length and severity against the month's budget, on Learn. That's learn dot get er done dot I O.
