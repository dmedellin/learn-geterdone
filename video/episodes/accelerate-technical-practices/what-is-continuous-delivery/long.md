---
format: long
lesson: accelerate-technical-practices/what-is-continuous-delivery
title: What is continuous delivery? Five principles and a batch
thumb: Make the release cheap first
---

@chapter The definition
@title text="What Is Continuous Delivery?" sub="Accelerate, Chapter 4" art=thumb
Chapter four turns from culture to technical practice. And it asks a plain question: do the technical practices behind continuous delivery measurably change how a team performs?

@quote text="Continuous delivery is a set of capabilities that enable us to get changes of all kinds—features, configuration changes, bug fixes, experiments—into production or into the hands of users safely, quickly, and sustainably." cite="Forsgren, Humble and Kim, Accelerate, Chapter 4"
Here's the definition. Continuous delivery is a set of capabilities that enable us to get changes of all kinds, features, configuration changes, bug fixes, experiments, into production or into the hands of users safely, quickly, and sustainably.

@words text="A set of capabilities, not a tool"
Why ask? Many Agile adoptions treated technical practice as secondary to management practice. Though Extreme Programming had put test driven development and continuous integration at its centre.

@chapter Five principles
@list heading="Five principles" items="Build quality in@build quality in|Work in small batches@small batches|Computers repeat, people solve problems@Computers|Relentless improvement@Relentless|Everyone is responsible@Everyone"
Five principles sit at its heart. Build quality in. Work in small batches. Computers perform repetitive tasks, people solve problems. Relentless improvement. And everyone is responsible.

@art quality-in
Building quality in comes from Deming: stop relying on inspection at scale, and design quality in from the start. Find problems quickly, while they're cheap to fix.

@art small-batches
Small batches means planning in chunks that deliver a measurable outcome, getting feedback, and correcting course. The authors admit that adds overhead. The goal is to change the economics, so pushing out a single change costs very little.

@art shared-outcomes
Automate the slow, repetitive work, like regression testing and deployment, so people are free for work that needs judgement. High performers are never satisfied. And in a bureaucratic organization, development watches throughput, testing quality and operations stability, though all three are outcomes of the whole system.

@chapter Three foundations
@list heading="Three foundations" items="Comprehensive configuration management@configuration management|Continuous integration@Continuous integration|Continuous testing@Continuous testing"
Three foundations make the principles practical. Comprehensive configuration management: everything built, tested and deployed automatically from version control. Continuous integration: short lived branches, merged into trunk often, each change built and unit tested. And continuous testing: tests against every commit, and nobody calls work done until its automated tests pass.

@art ci-trunk
Continuous integration deserves a closer look. Branches live for less than a day's work, they merge into trunk often, every change triggers a build and unit tests, and any failure is fixed at once. Manual approvals may remain in the pipeline, but once given, everything after them is automatic.

@art feedback-loops
Put together, you get several feedback loops, and a release that's a routine activity, available on demand.

@chapter What a batch costs
@words text="24 changes · 1 h each · 2 h per release" sub="invented for this lesson"
Now the count. Picture a team with twenty four changes ready, each taking an hour to prepare and check, and a release that costs two hours however many changes it carries. Send all twenty four as one batch, and it's out at hour twenty six.

@math heading="Two batches of twelve" items="one batch: 12 × 1 h + 2 h = 14 h@twelve hours of work;;first release: hour 14 · second: hour 28@hour fourteen;;average wait: (14 + 28) / 2 = 21 h@twenty one;;overhead: 2 × 2 h = 4 h@overhead is four"
Split them into two batches of twelve. One batch is twelve hours of work plus two of release: fourteen hours. The first is out at hour fourteen, the second at hour twenty eight. The average wait is twenty one hours, and the overhead is four.

@math heading="Four batches of six" items="first release: hour 8@hour eight;;last release: hour 32@thirty two;;average wait 20 h · overhead 8 h@eight hours of overhead"
Go to batches of six. The first is out at hour eight, under a third of the time. But the last leaves at hour thirty two, six hours later than one big batch. The average wait is twenty hours, with eight hours of overhead.

@chapter Change the economics
@math heading="Batches of six, 15-minute release" items="first release: hour 6.25@six point two five;;last release: hour 25@hour twenty five;;average wait ≈ 15.63 h · overhead 1 h@fifteen point six three"
That's the overhead the authors warned about. Now automate, and cut the release to a quarter of an hour. The first feedback arrives at hour six point two five, the last change at hour twenty five, and the average wait falls to about fifteen point six three hours. Overhead: one hour.

@art cheap-release
Nothing in the changes got smaller. The cost of releasing one did. That's changing the economics, in a number.

@chapter Where people slip
@list heading="Common slips" items="Continuous delivery is a pipeline you buy@The first|Small batches are always faster@The second|Testing at the end@And the third"
The first slip is taking continuous delivery to be a pipeline you buy. The second is reading small batches as always faster. They aren't, until the release gets cheaper. And the third is leaving testing and quality to the end of the work.

@chapter Try it
@words text="30 changes · 1 h each · 3 h release" sub="batches of 15 vs 5"
Your turn. Thirty changes, an hour each, and a three hour release. Compare batches of fifteen and of five. For each, find the first release, the last release and the average wait. Which gives the earliest feedback, and which finishes first?

@end text="Make the release cheap first"
You can try different batch sizes and release costs in the lab, on Learn. That's learn dot get er done dot I O.
