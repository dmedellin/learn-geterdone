---
format: long
lesson: trading-risk-management/trading-risk-plan
title: Writing a trading risk plan you can actually test
thumb: Decide before the pressure
---

@chapter The question
@title text="Trading Risk Plan" sub="Trading Risk Management" art=thumb
You've now got every piece. Risk per trade, sizing, stops, budgets, limits, leverage, correlation, options. The last step is to put them in one place, written down, before the market starts asking you questions.

@words text="Define the response before pressure changes the decision"
A risk plan defines the response before market pressure changes the decision. It states how much can be lost, when trading stops, how exposure is calculated, and which conditions prohibit a trade.

@art versions
Think of it as a specification, not a mood. The same document should work in your journal, in a backtest, and in an alert, and give the same answer each time. If two people read it, they should reach the same decision.

@chapter Three kinds of content
@art dials
First, numeric limits. Risk per trade, portfolio heat, leverage, daily loss, and weekly loss. Every one of them must be measurable. Each is a number you could write on a card, and check a trade against, without needing to interpret anything.

@art decision-paths
Second, decision rules. Specify when to reduce size, when to reject a trade, and when to stop trading.

@art review-flag
And third, review triggers. Define when results require investigation, simulation, or strategy suspension.

@chapter When to write it
@words text="Before trading"
So when should a risk plan be written? Before trading. Predefined rules reduce changes made under market and emotional pressure. Written after a loss, the plan is written by the loss. Its limits then describe what happened, rather than bound what can.

@words text="Not only for leveraged accounts"
And it isn't only for leveraged accounts. Leverage changes the arithmetic of the plan, not whether it's needed. An unleveraged account can still lose more than it planned.

@chapter Testable rules
@art vague-vs-exact
What makes a risk rule testable? Exact, measurable conditions. A general intention to be careful can't be checked against a trade. No more than one percent of current equity can. And a rule that changes for each trade isn't a rule. A test needs the same condition applied every time.

@chapter When limits conflict
@words text="Resolve it before trading"
What should happen when plan limits conflict? Resolve the contradiction before trading. The plan must be internally consistent before it can control risk. Ignoring the smaller limit means choosing, in advance, to breach it. And buying power can't settle a conflict between limits.

@art unreachable-cap
Here's the lesson's example. Risk per trade is one percent. Maximum positions is four. Maximum open risk is five percent. What does the lab's validator say?

@math heading="1% per trade · 4 positions · 5% open-risk cap" items="4 × 1% = 4%@four positions at one percent;;5% cap > 4% → never reached@can never be reached;;fix: cap 4%, or more positions@lower it"
Four positions at one percent each commit at most four percent of open risk. So a five percent cap can never be reached. It isn't wrong, but it isn't doing anything. Either lower it to four percent, or raise the position count.

@words text="Not 'consistent'" sub="the three numbers can't all bind"
So the plan isn't consistent, because the three numbers can't all bind. The lab flags it as a note to resolve. And with the lab's default three percent daily limit, it also flags open risk above the daily limit, which is the harder contradiction.

@chapter Where people slip
@list heading="Common mistakes" items="Vague terms such as small risk@The first|Exceptions without predefined criteria@The second|Changing several limits after a short losing run@the third"
Three mistakes. The first is using vague terms, such as small risk. The second is allowing exceptions without predefined criteria. And the third is changing multiple limits after a short losing sample.

@art versions
So version the plan, and record every change. Use measurable limits and explicit actions. And validate portfolio, leverage, and options rules together, not one at a time.

@chapter Try it
@list heading="Lab steps" items="Write the limits@write the limits|Check contradictions@check contradictions|Export and enforce@export and enforce"
The lab's steps: write the limits, using exact percentages, dollars, and conditions. Check contradictions. Open risk limits must be compatible with per trade risk and maximum concurrent positions. Then export and enforce, using the same specification in journals, backtests, alerts, and future automation.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. For practice, write three numbers for your own plan: risk per trade, maximum positions, and an open risk cap. Then check that all three can bind.

@end text="Write it before you need it"
You can write and validate your own risk plan in the lab, on Learn. That's learn dot get er done dot I O.
