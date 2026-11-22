---
format: long
lesson: backtesting-and-trading-systems/trading-system-specification-and-backtest-report
title: Writing a trading system spec someone else could reproduce
thumb: Same inputs, same decisions
---

@chapter The problem
@title text="Trading System Specification and Backtest Report" sub="Backtesting and Trading Systems" art=thumb
You've built a rule, tested it, checked it out of sample and stressed it. Now someone else wants to implement it. Could they, from what you've written down, reproduce every historical decision your test made?

@words text="Another implementation reproduces the same decisions"
That's the lesson's definition of done. A trading system is complete when another implementation can reproduce the same historical decisions. Not similar decisions. The same ones.

@art spec-document
And the document says what buyer, seller, trend, range and volatility behaviour qualifies, before the system is evaluated or automated. If a critical piece of execution logic lives outside the specification, the specification is incomplete.

@chapter Three documents in one
@list heading="What to understand" items="System specification@system specification|Backtest report@backtest report|Acceptance criteria@acceptance criteria"
There are three parts. A system specification: versioned rules, data contracts, event timing, accounting and constraints. A backtest report: dates, assumptions, metrics, regimes, failures and comparison results. And acceptance criteria: thresholds set in advance that decide whether the system advances, changes, or is rejected.

@art versioned-inputs
What makes a specification reproducible is explicit, versioned inputs and deterministic rules. A high historical return doesn't. That's an output. And a private verbal explanation doesn't either. If it lives in one person's head, it can't be versioned or compared, so it can't be reproduced.

@chapter Criteria before results
@art criteria-gate
Acceptance criteria have to be defined before the final result is reviewed. Criteria set after you've seen the result are set to be met. They describe the result instead of testing it. And setting them only after live losses is far too late, because they're what decides whether a system goes live at all.

@list heading="Report metrics with their context" items="Dates and assumptions@dates|Costs and benchmark@costs|Regimes and failures@regimes"
The report has to give metrics their context: the dates and assumptions, the costs and the benchmark, the regimes and the failures. A return without dates, costs and a benchmark can't be interpreted. It could be one good year or one lucky trade. And reporting only the winners is survivorship bias, applied to a trade log.

@art report-context
Think of the headline metric as sitting in the middle of the page, surrounded by everything needed to read it. The dates it covers. The costs it paid. The benchmark it's compared with. The regimes where it struggled. Take any of those away and the number stops meaning anything.

@chapter Catching contradictions
@words text="Risk per trade 3.5% · maximum open risk 3%"
The lesson's builder checks the specification for contradictions. Here's one. A specification sets risk per trade at three point five percent, and maximum open risk at three percent. What should the builder do?

@math heading="First position alone" items="open risk = 3.5%@three point five;;3.5% > 3% cap@more than the;;the cap can never bind → block@block it"
Block it. The first position alone would carry three point five percent of open risk, which is more than the three percent cap. So the cap is broken by the very first trade, and can never constrain anything. The lab marks this a hard failure and refuses to export it.

@art contradiction-block
It's not a warning that the cap will be reached sooner. And it doesn't pass just because three point five is inside the slider's range. The contradiction is between two fields the system itself set.

@chapter Freeze the contract
@list heading="Freeze the test contract" items="Specify data, rules, execution, accounting, limits@Specify|Validate causality, completeness, assumptions, criteria@Validate|Version and report immutable inputs with results@Version and report"
The workflow has three steps. Specify: define the data, rules, execution, portfolio accounting and limits. Validate: check causality, completeness, assumptions and acceptance criteria. Version and report: export immutable inputs beside complete results and diagnostics.

@art spec-to-automation
And this specification is the handoff. It becomes the input to the next course, Algorithmic and Automated Trading. The lesson's builder exports it as machine readable JSON, ready for that step.

@chapter Where people slip
@list heading="Common mistakes" items="Execution logic outside the specification@The first|Return without dates or costs@The second|Automating a rule that hasn't passed validation@And the third"
The first mistake is keeping critical execution logic outside the specification. The second is reporting a return without dates or costs. And the third is automating a rule that hasn't passed validation and robustness testing. Reject incomplete or contradictory systems before automation.

@chapter Try it
@words text="Define · validate · export"
In the lesson's builder, which uses deterministic synthetic educational data, define a complete system, let it check for contradictions, preview the test pipeline, and export the specification.

@end text="Build a spec that exports"
You can build, validate and export a full system specification, on Learn. That's learn dot get er done dot I O.
