---
format: long
lesson: enterprise-patterns-concurrency-and-session-state/concurrency-problems
title: Lost updates and inconsistent reads: why fifteen was never right
thumb: Right reads, wrong total
---

@chapter The story
@title text="Concurrency Problems" sub="Patterns of Enterprise Application Architecture, Chapter 5" art=thumb
Two correct numbers can add up to a total that was never true. That's where Fowler and David Rice open the book's chapter on concurrency.

@words text="Hard to think about · hard to test"
They start by admitting it's difficult. Concurrency is hard to think about, because the ways into trouble are hard to list. And it's hard to test. Enterprise developers lean on it heavily and think about it rarely, and they get away with it because of transactions.

@words text="Offline concurrency" sub="data handled across several database transactions"
Do your work inside one database transaction, and little goes wrong. The trouble is work that won't fit in one. A user editing an order across several screens spans several transactions. Controlling that is offline concurrency, and it's the book's main concern.

@chapter Two problems
@art lost-update
The first problem is the lost update. Martin spends a few minutes changing one method of a file. David changes another method of the same file, and finishes first. When Martin saves, his copy, read before David's change, writes over it. David's work is gone, and nobody is told.

@art inconsistent-read
The second is the inconsistent read. Martin counts the classes in two packages, locking and multiphase. He sees seven in locking, then takes a phone call. While he talks, David adds two classes to locking, and three to multiphase.

@math heading="Martin's count" items="locking: 7 → 9 · read before@seven in locking;;multiphase: 5 → 8 · read after@eight in multiphase;;Martin's total: 7 + 8 = 15@fifteen;;before: 12 · after: 17@twelve before"
Martin read seven in locking, before the change. He comes back and sees eight in multiphase, after it. So he arrives at fifteen. But the answer was twelve before David's change, and seventeen after.

@quote text="Sadly, fifteen classes was never the right answer." cite="Fowler and Rice, Patterns of Enterprise Application Architecture, Chapter 5"
Each of those was a true count at some moment. Fifteen was true at none. Sadly, fifteen classes was never the right answer.

@chapter In code
@code block=1 lines=1-6 label=Java focus="3@counts locking|4@then multiphase|5@adds them"
Here it is in code. The routine counts locking, then multiphase, with two separate queries, and adds them. Nothing ties the two queries together, so another session can commit between them. And neither query is wrong.

@chapter Move the reads
@list heading="One commit, three readers" items="martin-and-david: 15, matches neither@mixed|both-after: 17, the state after@both after|both-before: 12, the state before@both before"
The lab replays one commit against one reader. A read before the commit of a changed item is stale. A read after it is fresh. With Martin's mixed reads, the total is fifteen, and matches neither state. Read both after, and it's seventeen. Read both before, and it's twelve.

@words text="The fault is in the sum"
Only the timing changed. Every number Martin read was true when he read it, so checking each read would pass. The fault is in the sum. And it took only one person writing. The remedy isn't to read more carefully. It's to make both reads see one state.

@chapter Correctness and liveness
@art correctness-liveness
Both problems are failures of correctness, and correctness alone would be easy: let one person at a time near the data. But that destroys liveness, how much concurrent activity can go on. The essential problem, the authors say, is that you must worry about both.

@art execution-contexts
A few words the chapter fixes. A request is one call from outside. A session is a run of requests the user sees as one sequence. And a transaction gathers work to be treated as one: a system transaction to the database, a business transaction from the user.

@chapter Avoiding it
@art isolation-zones
There are two ways to dodge the problems entirely. Isolation partitions the data, so only one agent can reach each piece, the way an operating system gives each process its own memory.

@art immutable-shared
And immutability. Only data that can change causes trouble. Find what's immutable, or nearly so, and share it freely.

@chapter Where people slip
@list heading="Common slips" items="Correct reads give a correct result@The first|Concurrency needs two writers@The second|Correctness is the only goal@And the third"
The first slip is thinking correct reads give a correct result. Correctness belongs to the set of reads. The second is thinking you need two writers. An inconsistent read needs only one. And the third is treating correctness as the only goal. It's always traded against liveness.

@chapter Try it
@code block=2 lines=1-2 label=Records focus="1@cash goes|2@savings"
Your turn. A transfer of one hundred between two accounts commits while a report reads them. Cash goes from four hundred to three hundred, read after the commit. Savings goes from six hundred to seven hundred, read before. What total did the report see? Does it match either state? And which read is stale?

@end text="Replay the commit yourself"
You can move the reads around a commit and watch the total, on Learn. That's learn dot get er done dot I O.
