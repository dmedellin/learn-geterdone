---
format: long
lesson: algorithmic-and-automated-trading/scanners-alerts-and-human-approval
title: Trading alerts that a person can actually act on
thumb: What changed, and until when
---

@chapter The problem
@title text="Scanners, Alerts, and Human Approval" sub="Algorithmic and Automated Trading" art=thumb
A scanner finds a setup and sends you a message that just says buy. You look at it twenty minutes later. Buy what, at what price, with what stop? And is the setup even still there?

@words text="What changed · why it matters · when it expires"
The lesson's rule is that an alert should state what changed, why it matters, and when the decision expires. A scanner may detect buyers continuing to accept higher prices, but approval delay can make the original entry, stop and reward to risk invalid.

@chapter Three ideas
@list heading="What to understand" items="Scanner@scanner|Alert contract@alert contract|Approval gate@approval gate"
Three ideas. A scanner: it evaluates a defined universe on a schedule or an event stream, and produces ranked candidates. An alert contract: every alert includes the symbol, direction, setup, evidence, entry condition, invalidation, timestamp and expiration. And an approval gate: a person accepts, rejects or modifies a proposed order, within fixed permissions.

@art scanner-funnel
A scanner works like a funnel. Many symbols go in at the top, evaluated with the same versioned rules. Filters for quality, liquidity, risk and portfolio fit narrow them down. A short ranked list comes out of the bottom.

@chapter The alert contract
@art alert-card
A useful alert carries the thesis, the trigger, the invalidation, the timestamp and the expiry. Not just the word buy, which leaves the reviewer to rebuild everything from nothing. And not just a confidence percentage, which can't be checked and invites approval by feeling.

@art scan-schedule
The lesson puts the standard simply. The recipient shouldn't need to infer the trade rules from a generic message. Everything needed to decide, and to check the decision later, is in the alert. If the scanner runs on a schedule, the alert also says when it was produced, so the reader knows how old the evidence is.

@chapter Expiry
@art alert-expiry
Why should an alert expire? Because market conditions and prices change. The alert's entry, stop and expiry are numbers, and after a while those numbers stop describing the market. Setups expire, so alerts do too.

@words text="Re-run risk checks after the delay"
And when approval does come after a delay, re run the risk checks. Submitting the original quantity after a long approval delay is a named mistake. The price, the stop distance, and so the right size, may all have moved.

@chapter Condition or transition?
@math heading="Setup true for 20 min · scan every 5 min · 3 candidates" items="scans at 0, 5, 10, 15 min = 4 scans@four scans;;on the condition: 4 × 3 = 12 alerts@twelve alerts;;on the transition: 1 × 3 = 3 alerts@you send three"
Here's the lesson's worked question. A setup stays true for twenty minutes. The scanner runs every five minutes and finds three candidates. It sees the condition at zero, five, ten and fifteen minutes. That's four scans. Alert on the condition, and you send four times three, twelve alerts. Alert on the transition, one per candidate, and you send three.

@art duplicate-alerts
Nine of those twelve say nothing new. Sending repeated alerts while a condition stays true is a named mistake, and it trains the person reading them to ignore alerts. Deduplicate by setup and state transition.

@chapter Where approval sits
@list heading="Keep alerts actionable" items="Scan eligible symbols with versioned rules@Scan|Rank with quality, liquidity, risk filters@Rank|Communicate one alert with expiry and action@Communicate"
The pipeline has three steps. Scan: evaluate eligible symbols with the same versioned rules. Rank: apply quality, liquidity, risk and portfolio filters. Communicate: send one deduplicated alert, with an explicit expiration and an approval action.

@art approval-gate
And approval happens before the broker order is submitted. Not before the scan, when there's nothing to approve, and not after the audit log, which records the approval as it's made. The gate controls whether the proposed trade reaches execution at all.

@chapter Where people slip
@list heading="Common mistakes" items="Repeated alerts while a condition stays true@The first|Confidence with no evidence or invalidation@The second|Original quantity after a long delay@And the third"
The first mistake is sending repeated alerts while a condition remains true. The second is using confidence without evidence or invalidation. And the third is submitting the original quantity after a long approval delay.

@chapter Try it
@words text="Scan interval · threshold · expiry · approval delay"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, change the scan interval, the score threshold, the alert expiration and the approval delay. Watch duplicate and stale decisions appear, and then disappear.

@end text="Send fewer, better alerts"
You can tune the scanner and the approval delay yourself, on Learn. That's learn dot get er done dot I O.
