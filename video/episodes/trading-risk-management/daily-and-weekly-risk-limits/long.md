---
format: long
lesson: trading-risk-management/daily-and-weekly-risk-limits
title: Daily and weekly risk limits: stopping before a bad day grows
thumb: When the limit hits, stop
---

@chapter The question
@title text="Daily and Weekly Risk Limits" sub="Trading Risk Management" art=thumb
You've had three losses today. The next setup looks great. Surely one more trade can't hurt? That moment is exactly what a daily limit is for.

@words text="Repeated losses are information"
After repeated losses, the market may be unsuitable for the setup, or your execution may be deteriorating. A hard loss limit prevents a bad sequence from becoming a large account event. And the limit is applied even when the next setup looks attractive.

@chapter Two limits and a reason
@art daily-gate
A daily stop is the maximum realised plus open loss allowed during one session. Once you reach it, the session is over for new risk.

@art session-stack
Trades before the line count. After the line, there are no more, however good the next chart looks.

@art weekly-wall
A weekly stop is a larger limit that prevents repeated daily damage from compounding. One bad day can't become five bad days in a row.

@words text="Behavioural control" sub="revenge trading · size escalation · rule changes under pressure"
And there's a behavioural reason for both. Limits reduce revenge trading, size escalation, and rule changes under pressure. They make the decision before the pressure arrives.

@chapter When the limit is reached
@words text="Stop adding risk"
The daily loss limit is reached. What should happen? Stop adding risk. A hard limit only works when new exposure stops immediately.

@list heading="Not these" items="Add one final trade@one final trade|Double the next target@doubling the next target"
Adding one final trade is the one trade the limit was written to refuse. It's a decision made while losing, which is exactly when it can't be trusted. And doubling the next target doesn't change what the next trade can cost. The limit is about cost.

@art winner-reset
Should one winner reset a limit you've already reached? No. Resetting after a winner means the limit stops binding whenever the day gets lucky, which makes it not a limit. And volume has nothing to do with it. The limit is a rule about the account, not the market.

@chapter What counts
@art counting
What should count toward the limit? Realised loss, plus current open risk, plus costs. The account remains exposed to active stops, so open risk must be included. Counting only closed losses lets open positions carry the day past the limit before anything is realised. And commissions are part of the cost, not the whole of it.

@chapter Worked example
@math heading="Daily limit 3R · 1R per trade" items="realised = −1.5R@one and a half R;;open risk = 1R@one R of open risk;;3R − 1.5R − 1R = 0.5R left@half an R"
Here's the lesson's example. The daily limit is three R, with one R risked per trade. Realised loss so far is one and a half R, and there's one R of open risk to current stops. Three R minus one and a half, minus one, leaves half an R.

@words text="A new 1R trade doesn't fit" sub="a 0.5R trade could, or nothing until a stop moves to entry"
So a new one R trade can't be opened. Either a half R trade fits, or nothing does until an open stop is moved to entry.

@list heading="Not these" items="1.5R is under 3R@only the realised part|Fits if the open trade is at breakeven@breakeven"
One and a half R is only the realised part. The open stop is another R, so two and a half R is committed. And an open trade at breakeven still has its stop below it. Until the stop moves to entry, it carries its full one R of open risk.

@chapter Where people slip
@list heading="Common mistakes" items="A recovery trade after the limit@The first|Increasing size after consecutive losses@The second|Changing the limit during the session@the third"
Three mistakes. The first is taking a recovery trade after the limit. The second is increasing size after consecutive losses. And the third is changing the limit during the session.

@list heading="Practical rules" items="Hard limits, no discretionary override@hard limits|Count open risk and costs@include open risk|Record why the limit was reached@record why"
So use hard limits with no discretionary override. Include open risk and costs in limit consumption. And record why the limit was reached before the next session.

@chapter Try it
@list heading="Lab steps" items="Define the stop before trading@define the stop|Count all losses@count all losses|Require a review@require a review"
The lab's steps: define the stop before trading. The limit must be fixed before the first outcome. Count all losses, including realised loss, open risk, fees, and execution mistakes. Then require a review. Resume only after the defined reset period and a process review.

@art review
That review is where the limit pays off twice. It stops the damage today, and it makes you write down why it happened before you trade again.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. For practice, keep the three R limit, but suppose realised loss is two R and open risk is half an R. Work out what's left.

@end text="Decide the limit before the day starts"
You can run a session against a hard limit in the lab, on Learn. That's learn dot get er done dot I O.
