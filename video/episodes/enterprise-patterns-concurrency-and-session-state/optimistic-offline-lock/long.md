---
format: long
lesson: enterprise-patterns-concurrency-and-session-state/optimistic-offline-lock
title: Optimistic Offline Lock: a version number in every row
thumb: Zero rows means someone was first
---

@chapter The save that loses work
@title text="Optimistic Offline Lock" sub="Patterns of Enterprise Application Architecture, Chapter 16" art=thumb
You've probably written this save. It writes whatever the form sent back, an update that sets the new total on the row with the invoice's id.

@art two-clerks
Two clerks open the invoice, and both change it. The second save wins, and nobody learns the first one happened. That's the lost update, spread across requests. Once a business transaction runs across several system transactions, the database alone can't keep the data consistent.

@chapter How it works
@art version-row
David Rice's pattern, in Fowler's book, checks before committing that a session's changes don't clash with another's. The usual way is a version number in each record. The session keeps the version it loaded, and at commit compares it with the version in the database.

@art where-match
If they match, the changes and an increment of the version commit together. Now any session still holding the old number can't get the lock. With a relational database, the comparison goes into every update and delete, so one statement both takes the lock and changes the row.

@code block=1 lines=1-11 label=Java focus="5-6@sets the new total|7-9@three set calls|10@turns that count"
Here's a save with the check built in. The update sets the new total and moves the version on, but only for the row whose id and version both match. Three set calls fill the three question marks. And the last line turns that count into the answer: true for one row, false for none.

@art row-count
One row means success. Zero means someone changed or deleted the record first. So the session rolls back its system transaction, and gives up, or resolves the conflict and tries again. And don't use modification times instead of a version count. Clocks on different machines can't be trusted to agree.

@chapter Replay two clerks
@math heading="two-clerks" items="0: Kim reads, version 0@minute zero;;1–3: Lee reads, edits, commits → version 1@Lee reads;;20: Kim saves, matches no row@Kim saves"
In the lab, Kim reads the invoice at minute zero, at version zero. Lee reads it at one, edits at two, and commits at three, moving it to version one. Kim edits at four, and at minute twenty Kim saves. Her update matches no row.

@math heading="result" items="committed: lee@Lee commits;;conflict: kim@Kim conflicts;;minutes redone: 20@twenty minutes"
So Lee commits, Kim conflicts, and she redoes twenty minutes, from her read at minute zero to the failed save.

@chapter The read nobody checks
@art read-dependency
Most implementations stop there, Rice says, and that misses the inconsistent read. Kim reads a discount, and edits a quote computed from it. Lee edits the discount at minute one, and commits at two. Kim commits at six.

@math heading="check the reads?" items="no: lee, kim commit · 0 conflicts@set to no;;yes: lee commits · kim conflicts · 6 minutes@set to yes"
The lab's last control checks records that were only read. Set to no, both saves succeed, and Kim's quote is built on a discount that no longer exists. Set to yes, Lee commits, Kim conflicts, and six minutes are redone.

@words text="Check what you read, too" sub="reread at repeatable read or stronger · else increment"
So the remedy is to check the version of what you read, too. Rereading a version works only at repeatable read or stronger. Below that, the version must be incremented.

@chapter When to use it
@quote text="Optimistic concurrency management is appropriate when the chance of conflict between any two business transactions is low." cite="David Rice, in Fowler, Patterns of Enterprise Application Architecture, Chapter 16, When to Use It"
Here's Rice's condition. Optimistic concurrency management is appropriate when the chance of conflict between any two business transactions is low.

@art late-failure
The check finds a conflict at the last possible moment. It's cheap to build, and costs nothing while conflicts are rare. But each conflict is paid for in someone's lost work. When conflicts are likely, use Pessimistic Offline Lock. Rice still makes the optimistic lock the default. And a good merge makes it far stronger, as source code control shows.

@chapter Where people slip
@list heading="Common slips" items="A version check catches every conflict@The first|Optimistic locking costs nothing@The second|Zero rows is a database error@And the third"
The first slip is thinking a version check catches every conflict. It misses what you only read. The second is thinking it costs nothing. It costs the failed session's whole work. And the third is treating a zero row count as an error to log and move past. It's the lock refusing.

@chapter Try it
@code block=2 lines=1-9 label=Timeline focus="1-4@Ana reads|5-6@Ben edits|7-9@Cy reads"
Your turn. Ana reads the budget, then Ben. Ana edits and commits at five. Ben edits at six and commits at thirty. Then Cy reads, edits, and commits at forty. For each user, write the version seen and the version at commit. Who fails, and how many minutes are lost?

@end text="Replay the clerks yourself"
You can replay the clerks and the discount in the lab, on Learn. That's learn dot get er done dot I O.
