---
format: long
lesson: measuring-systems/burn-rate-alerts
title: Burn-rate alerts: page on the budget, not the error rate
thumb: 43.2 minutes, spent how fast?
---

@chapter An objective is a budget
@title text="Burn-rate Alerts" sub="Measuring Systems" art=thumb
An alert that fires above one percent errors pages you for a two minute blip, and stays quiet while a slow leak spends your whole month. There's a better quantity to alert on: how fast you're spending your error budget.

@art budget-bar
An objective over a period implies a budget, the quantity of failure it permits. That's one minus the objective, times the period.

@math heading="99.9% over 30 days" items="budget = (1 − 999/1000) × 43 200 min@gives a budget of;;= 216/5 = 43.2 minutes  exactly@forty three point two"
Ninety nine point nine percent over thirty days, forty three thousand two hundred minutes, gives a budget of two hundred and sixteen fifths, forty three point two minutes, exactly.

@art two-months
Say which period you mean, every time. Over a twelfth of a year, the same objective gives forty three point eight minutes, also exact. Same objective, different month. Count it in failed requests and you get a third framing. A budget is a quantity, a period and a unit together.

@chapter Burn rate
@words text="b = 1 spends the budget exactly over the period"
A burn rate is a multiple. A burn of one is the failure rate that spends the whole budget exactly at the end of the period. At three nines, that's point one percent of requests failing. A burn of fourteen point four is one point four four percent.

@math heading="Window w at burn b" items="spends b · w / P of the budget@b times w over P;;exhausts it after P / b@P over b"
A window of length w at burn b spends b times w over P of the budget, whatever the objective is. And the budget runs out after P over b.

@art burning-bar
So a burn of fourteen point four, sustained, spends the thirty day budget in fifty hours. After one hour, it's spent fourteen point four times sixty over forty three thousand two hundred, one fiftieth, two percent. That's point eight six four minutes.

@chapter The standard pairs
@math heading="Burn,  window,  budget spent,  exhausts in" items="14.4×,  1 hour:  2% = 0.864 min,  50 hours@fourteen point four;;6×,  6 hours:  5% = 2.16 min,  5 days@six times;;3×,  1 day:  10% = 4.32 min,  10 days@three times;;1×,  3 days:  10% = 4.32 min,  30 days@one times"
The standard set has four pairs. Fourteen point four times over an hour fires having spent two percent. Six times over six hours, five percent. Three times over a day, ten percent. And one times over three days, also ten percent.

@art fast-and-slow
The fast pair fires with almost all the budget left, so it can afford to wake someone. The slow pair catches a burn the fast one never notices. A burn of one isn't an emergency, but it's exactly the rate that leaves you with nothing at the end.

@art burn-slopes
One pair can't do both jobs. Only the fast pair, and a service failing point one five percent for a fortnight blows the budget without tripping it. Only the slow pair, and a total outage pages you after it's spent a third of the allowance.

@words text="02:00 deploy, burn 14.4" sub="pages at 03:00 with 0.864 of 43.2 min spent"
A deploy at two in the morning takes errors to one point four four percent. A raw one percent alert pages at five past, and would also page for a six minute blip that costs almost nothing. The burn rate rule pages at three, having spent point eight six four minutes, and ignores the blip.

@chapter An SLO is not an SLA
@art slo-vs-sla
The arithmetic is the same for both. The consequences aren't. Missing an objective spends a budget you own. Missing an agreement spends money. So set the agreement looser, say ninety nine point five promised against ninety nine point nine targeted, so the internal alarm fires long before the external one.

@chapter Where people slip
@list heading="Common slips" items="Alerting on the raw error rate@The first|Quoting a budget without its period@The second|Running one burn-rate pair@the third"
The first slip is alerting on the raw error rate instead of on the budget. The second is quoting a budget without the period it's for. And the third is running one burn rate pair. You need at least one fast and one slow.

@chapter Try it
@words text="99.95% over 30 days" sub="first move: budget = 21.6 min"
Your turn. Take ninety nine point nine five percent over thirty days. The budget halves, to twenty one point six minutes. Work out what fourteen point four times over an hour spends, as a fraction and in minutes, and say whether the fraction changed, and why.

@end text="Alert on the budget"
You can move the objective and the burn and watch the budget drain, on Learn. That's learn dot get er done dot I O.
