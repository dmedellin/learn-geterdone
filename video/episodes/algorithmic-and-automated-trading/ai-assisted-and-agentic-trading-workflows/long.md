---
format: long
lesson: algorithmic-and-automated-trading/ai-assisted-and-agentic-trading-workflows
title: AI in a trading workflow: let it propose, never let it decide alone
thumb: The model proposes, rules decide
---

@chapter The question
@title text="AI-Assisted and Agentic Trading Workflows" sub="Algorithmic and Automated Trading" art=thumb
An AI model reads the news, studies the chart, and tells you, with ninety five percent confidence, that buyers are in control. Should it be allowed to place the order? The lesson's answer is a firm no, and the reasons are worth understanding.

@words text="AI interprets · data and controls decide"
AI can propose an interpretation, but observable market data and fixed controls decide whether an action is allowed. A model may describe buyer control, but the system must verify actual higher prices, volume, freshness, risk and invalidation before it creates an order.

@chapter Three ideas
@list heading="What to understand" items="Advisory task@advisory task|Structured proposal@structured proposal|Deterministic guardrail@deterministic guardrail"
Three ideas. An advisory task: summarise news, extract events, classify regimes, or explain a setup, without any direct execution authority. A structured proposal: return evidence, timestamps, uncertainty, rule references, invalidation and a requested action, in a fixed schema. And a deterministic guardrail: validate source freshness, allowed symbols, strategy rules, position size, risk and approval before execution.

@art advisory-only
Advisory work is where AI fits first. Reading many documents, pulling out events, putting a regime into words. That's useful, and none of it needs the ability to trade. The lesson's practical rule is to use AI for advisory work before giving it any execution authority.

@chapter The authority boundary
@art authority-boundary
The key picture is a boundary. The model sits on one side. It may propose. On the other side are controlled services that decide and execute. The model's output never crosses that line on its own.

@list heading="Keep AI outside the final authority boundary" items="Gather timestamped evidence@Gather|Propose a structured thesis with citations@Propose|Validate with deterministic checks@Validate"
The workflow has three steps. Gather: retrieve timestamped market, company and event evidence. Propose: return a structured thesis, with uncertainty and citations. Validate: apply deterministic strategy, risk, permission and approval checks.

@art structured-proposal
Which output is safer from an AI component? A structured proposal with evidence and uncertainty. Not an unrestricted broker command, which reaches execution with nothing in between. And not a hidden free text instruction, which no rule can validate and no one can audit.

@chapter Confidence isn't permission
@art stale-source
High model confidence should never bypass deterministic risk controls. Confidence is the model's report on itself. It's not a freshness check, and it's not a reason to double the size. Treating confidence as the probability of profit is one of the lesson's named mistakes. Freshness belongs to the evidence, not to the model.

@math heading="Confidence 95% · newest source 12 min old · limit 5 min · guardrail on · mode automatic" items="95% ≥ 65% → proposal created@proposal is created;;12 min > 5 min → stale@twelve minutes;;final action: blocked@blocked"
Here's the lesson's example. Confidence is ninety five percent, so the proposal is created, since that clears the sixty five percent threshold. But the newest source is twelve minutes old, against a five minute limit. Twelve is more than five, so the proposal fails freshness, and the final action is blocked.

@art guardrail-block
Not submitted, even though the mode is automatic, because one failed check blocks it before the mode is ever consulted. And not awaiting approval, because there's nothing to approve. The ninety five percent is never read again. That's what a deterministic guardrail means. A confident proposal built on a stale source is just confidently stale.

@chapter The execution contract
@art validated-command
So what should the execution service accept? Only validated commands from authorised components. Not unversioned model output, because then nobody knows which model or prompt produced it. And not any natural language message, because language is ambiguous and can't be checked field by field.

@chapter Where people slip
@list heading="Common mistakes" items="Free-form model output calling the broker@The first|Confidence treated as probability of profit@The second|Stale news or context used unvalidated@And the third"
The first mistake is allowing free form model output to call the broker directly. The second is treating confidence as the probability of profit. And the third is using stale news or market context without validation. Require structured outputs with evidence and timestamps, and validate every proposal with deterministic rules and risk controls.

@chapter Try it
@words text="Freshness · confidence · evidence · hallucination risk · mode"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, change the source freshness, model confidence, evidence quality, hallucination risk, approval mode and guardrails. Watch how often a confident proposal is still, correctly, blocked.

@end text="Let the guardrail decide"
You can send AI proposals through deterministic guardrails yourself, on Learn. That's learn dot get er done dot I O.
