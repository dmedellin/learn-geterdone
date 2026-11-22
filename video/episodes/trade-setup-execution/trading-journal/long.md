---
format: long
lesson: trade-setup-execution/trading-journal
title: A trading journal you can actually review
thumb: Write the plan before the outcome
---

@chapter The question
@title text="Trading Journal" sub="Trade Setup & Execution" art=thumb
Most trading journals are written after the trade, when you already know how it turned out. And that's the problem. Once you know the outcome, it quietly rewrites what you think you knew before entry.

@words text="Enough to reproduce the decision" sub="without rewriting history"
This lesson builds a journal that records the original thesis, the planned and the actual execution, the result in R, whether you followed the plan, your mistakes, and notes. The aim is enough information to reproduce the decision and diagnose the execution, without rewriting history.

@words text="Process and measurement" sub="no live data, no recommendations, no signals"
As with the rest of this course, it teaches process and measurement. It doesn't give live market data, personal recommendations, or trade signals.

@chapter Three ideas
@art plan-vs-actual
First, plan and outcome are separate. Record what you intended separately from what happened, and separately again whether the plan was followed.

@art r-normalize
Second, record the result in R. Normalizing every outcome by its initial risk means trades with different prices and sizes can be compared directly.

@art tag-chips
And third, consistent tags. Use stable setup categories and stable mistake categories, so that patterns can be added up later. Free text alone is hard to aggregate into patterns you can act on.

@chapter What goes in an entry
@list heading="An entry" items="Date, symbol, setup, direction, timeframe@Date|Entry, initial stop, initial target@entry, initial stop|Result in R@result in R|Execution score, 1 to 5@execution score|Followed the written plan?@followed the written plan|Thesis, mistake tags, notes@thesis"
An entry has a date, a symbol, a setup, a direction, and an execution timeframe. Then the entry, initial stop and initial target, the result in R, an execution score from one to five, and whether you followed the written plan. Then the thesis and context, the mistake tags, and post trade notes.

@list heading="Mistake tags" items="Early entry@Early entry|Late entry@late entry|Oversized@oversized|Moved stop@moved stop|Unplanned exit@unplanned exit|No valid setup@no valid setup"
The mistake tags are fixed: early entry, late entry, oversized, moved stop, unplanned exit, and no valid setup. Because they're always the same, you can count them across many trades, and see which mistake actually costs you the most.

@chapter The lesson's example
@art journal-card
The lesson's example is the simulated trade from Trade Management. The symbol can be anything, because it was synthetic. The setup is a pullback, long, on the one hour timeframe. The result in R is what the simulation reported, and followed the plan is what its discipline score said. Each deviation gets its tag.

@words text="Write the thesis as it stood before the trade"
And the thesis line is written as it stood before the trade, the plan from that page, not the way the outcome makes it look now. Nothing in the entry is invented, and every field can be checked against what the simulation actually showed.

@chapter The process
@list heading="Journal process" items="Record before entry@Record before entry|Capture actual execution@Capture actual execution|Score after exit@Score after exit|Export and review periodically@Export and review"
Record before entry: context, setup, trigger, entry, invalidation, target, and management plan. Capture actual execution: fills, changes, partial exits, and deviations, while they're still facts. Score after exit: the result in R, adherence, execution score, tags, and notes. And export and review periodically.

@art export-box
The lab exports the journal as a JSON file, which can be imported directly into the Performance Review lesson. Keep a consistent review interval, and keep backups outside browser storage.

@chapter Where people slip
@list heading="Common mistakes" items="Recording only winners and memorable trades@The first|Writing the thesis after the outcome@The second|Vague notes without categories@The third|Judging quality only from profit@And the fourth"
The first mistake is recording only winners and memorable trades. Selective records produce misleading statistics. The second is writing the thesis after the outcome. The third is vague notes without categories. And the fourth is judging quality only from profit. A well executed trade can lose, and a poorly executed one can win.

@art selective-record
The first one deserves a picture. If the losing trades and the dull ones never make it into the journal, every statistic you compute later is built on the trades you chose to remember. The gaps are invisible, and the numbers look better than your trading really is.

@chapter Try it
@words text="Record · export · re-import"
Here's the lesson's standard. Record, export, and re import one complete entry. The thesis written as it was before the outcome, the result in R, plan adherence, the execution score, and a mistake tag wherever one applies.

@end text="Start your journal"
You can record, export and re import a journal entry on Learn. That's learn dot get er done dot I O.
