---
format: long
lesson: algorithmic-and-automated-trading/observability-logging-and-auditability
title: Observability for trading systems: was it the market or the machine?
thumb: Price loss or system failure?
---

@chapter The problem
@title text="Observability, Logging, and Auditability" sub="Algorithmic and Automated Trading" art=thumb
Your system lost money today. Was the strategy wrong about the market, or did something inside the system break? Those are different problems, with different fixes, and from the profit and loss alone you can't tell them apart.

@art loss-or-failure
A price loss and a system failure need different evidence. Sellers may keep accepting lower prices exactly as the strategy expected, while delayed data or a missing risk response creates an operational loss. The first is the strategy doing its job in a bad market. The second is the system failing to do its job at all.

@chapter Three kinds of evidence
@list heading="What to understand" items="Metrics@Metrics|Logs and audit@Logs and audit|Trace@trace"
Three kinds of evidence. Metrics: numeric measurements like feed age, signal count, order latency, rejection rate and exposure. Logs and audit: structured event records with identities, versions, reasons, and the before and after state. And a trace: the causal path from a market event through strategy, risk, order and broker response.

@art feed-age-metric
Which metric directly protects strategy freshness? Market data age. A stale feed can make an otherwise valid rule act on old information. Monitoring process uptime while ignoring feed freshness and broker state is one of the lesson's named mistakes. The process can be up, and blind.

@chapter Audit events
@art audit-record
An audit event has to include the rule version, the inputs, the decision, the reason and the identity. Without timestamps, the trail can't be ordered or matched against the market. And the final profit and loss alone says what happened to the money, not why.

@words text="Structured, with stable IDs"
That's why unstructured text without stable IDs is a named mistake, and so is logging only exceptions. You need a record of the normal decisions too, or there's nothing to compare the strange one against.

@chapter Following a trace
@art trace-spans
A trace connects one decision across services. It shows where time and errors happened along the end to end path. It doesn't replace the audit log, though. The trace shows timing, and the audit log holds the inputs, decision and reason. Each answers a question the other can't.

@math heading="Feed 20 · normalize 17 · strategy 240 · risk 18 · broker 24 ms" items="20 + 17 + 240 + 18 + 24 = 319 ms@three hundred and nineteen;;baseline sum 99 ms → excess 220 ms@ninety nine;;all 220 ms of it in the strategy span@strategy span"
Here's the lesson's trace. Twenty, seventeen, two hundred and forty, eighteen and twenty four milliseconds across feed, normalize, strategy, risk and broker. That adds up to three hundred and nineteen milliseconds. The baseline sum is ninety nine, so there's two hundred and twenty extra, and all of it sits in the strategy span.

@art open-the-span
So you open the strategy span. Not the broker, just because brokers are often slow. Its twenty four is its normal value. And not nothing, because ninety nine was the baseline, not this trace. The trace tells you where to look before anyone guesses.

@chapter Instrument the whole path
@list heading="Instrument the complete decision path" items="Measure with clear units and thresholds@Measure|Correlate IDs across components@Correlate|Alert on actionable symptoms, with evidence@Alert"
Telemetry should explain both system health and trading behaviour. Measure: emit service and domain metrics, with clear units and thresholds. Correlate: carry event, signal, order and trace identifiers across every component. Alert: notify on actionable symptoms, and link straight to the supporting evidence.

@art correlation-ids
Correlation IDs are what make that work. One identifier follows a decision from the market event to the broker's response, so every log line and every span along the way can be pulled up together.

@chapter Where people slip
@list heading="Common mistakes" items="Logging only exceptions@The first|Unstructured text without stable IDs@The second|Watching uptime, ignoring freshness and broker state@And the third"
The first mistake is logging only exceptions. The second is using unstructured text without stable IDs. And the third is monitoring process uptime while ignoring feed freshness and broker state. Alert on stale data, unknown orders, risk breaches and state divergence.

@chapter Try it
@words text="Inject an incident · toggle the evidence"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, inject a latency or data incident, then toggle metrics, logs, traces and correlation IDs. Measure how quickly the incident is detected, and how well it can be diagnosed.

@end text="Find the slow span"
You can inject an incident and trace it to the slow span, on Learn. That's learn dot get er done dot I O.
