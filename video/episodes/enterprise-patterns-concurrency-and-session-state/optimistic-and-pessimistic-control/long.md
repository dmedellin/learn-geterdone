---
format: long
lesson: enterprise-patterns-concurrency-and-session-state/optimistic-and-pessimistic-control
title: Optimistic vs pessimistic locking: detect or prevent?
thumb: Detect it, or prevent it
---

@chapter Two answers
@title text="Optimistic and Pessimistic Control" sub="Patterns of Enterprise Application Architecture, Chapter 5" art=thumb
What do you do with data that can change, and can't be isolated? Fowler and Rice give two answers, and the choice between them is the subject of this video.

@quote text="A good way of thinking about this is that an optimistic lock is about conflict detection while a pessimistic lock is about conflict prevention." cite="Fowler and Rice, Patterns of Enterprise Application Architecture, Chapter 5"
Here's the line to keep. A good way of thinking about this is that an optimistic lock is about conflict detection, while a pessimistic lock is about conflict prevention.

@chapter The two locks
@art optimistic-copies
Martin and David both want to edit one file. Optimistically, each takes a copy and edits freely. David checks in first, no trouble. When Martin commits, the system detects the conflict, rejects his commit, and leaves him to sort it out.

@art pessimistic-lock
Pessimistically, whoever checks the file out first stops anyone else editing it. So David can't work on the file until Martin has committed. The authors even grant that optimistic locking is arguably not locking at all.

@chapter What each costs
@words text="Pessimistic: everyone waits" sub="Optimistic: everyone after the first merges"
A pessimistic lock reduces concurrency. While Martin holds the file, everyone else waits. An optimistic lock is held only during the commit, so people make better progress. But after a conflict, everyone after the first commit has to merge.

@words text="How often? How much does it hurt?"
Source code merges easily. Business data usually doesn't, and often the only course is to throw the work away. So the choice turns on how often conflicts happen and how bad they are. Rare or cheap, pick optimistic. Painful for users, go pessimistic.

@code block=1 lines=1-19 label=Java focus="5-7@canCommit|11-18@tryLoadForEdit"
Here are both in one class. canCommit is optimistic: the commit goes ahead only if the stored version is still the one the session read. tryLoadForEdit is pessimistic: the session asks for the file before loading it, and is turned away if another session holds it.

@chapter Replay it
@art session-timeline
The lab replays one timeline. Martin reads the design at minute zero, and David at one. David edits at five, Martin at six. David commits at eight, and Martin at ten.

@math heading="no-control" items="committed: david, martin@both commits;;lost updates: 1@one lost update;;minutes redone: 0@zero minutes"
With no control, both commits succeed. Martin's, made from the version he read at minute zero, writes over David's change. That's one lost update, and zero minutes redone. Nobody is told. The loss is in the count and nowhere else.

@math heading="optimistic" items="committed: david@David commits;;conflict: martin@Martin's commit;;minutes redone: 10@ten minutes"
Optimistically, David commits, and moves the version to one. Martin's commit at minute ten finds it changed, and conflicts. Everything since minute zero has to be done again: ten minutes redone.

@math heading="pessimistic" items="committed: martin@Martin commits;;refused: david@David is refused;;minutes redone: 0 · most locks: 1@zero minutes"
Pessimistically, Martin takes the lock at minute zero, when he loads the design, not when he starts editing. David is refused at minute one, before doing any work. Martin commits, zero minutes redone, at most one lock held. What no tile shows is David's wait.

@words text="10 minutes of Martin's work · or David kept out for 9"
So which is safer? On this timeline, the sessions really do collide, and the schemes only choose who pays. Now delete Martin's commit, as if he walked away. Pessimistically, David is still refused. Optimistically, he commits, and nobody loses anything.

@chapter Reads and deadlocks
@art read-write-locks
Inconsistent reads need more. Pessimistic schemes use read locks, which are shared, and write locks, which are exclusive: many readers, or one writer.

@art version-steps
Optimistic schemes keep a version marker on the data, a timestamp or a counter. An update is allowed only if the marker is unchanged, and then it moves on. To catch an inconsistent read, check the markers of what you read too, but only for data you used, not data you merely glanced at.

@art deadlock
And the pessimistic side has deadlocks. Martin holds one file and wants David's. David holds that one and wants Martin's. You can pick a victim, time out locks, or take locks in a fixed order. The authors prefer very simple, conservative schemes.

@chapter Where people slip
@list heading="Common slips" items="Pessimistic is safer, so better@The first|Optimistic loses no work@The second|Checking only what you write@And the third"
The first slip is thinking pessimistic is safer, so better. It also keeps out sessions that would never collide. The second is thinking optimistic loses no work. It throws away the second session's work. And the third is checking only what you write, which misses the inconsistent read.

@chapter Try it
@code block=2 lines=1-6 label=Timeline focus="1-2@Ann reads|5@Bo commits|6@Ann commits"
Your turn. Ann reads the plan at minute zero, Bo at two. Ann edits at three, Bo at four. Bo commits at nine, and Ann commits at twelve. Replay it optimistically, then pessimistically. Who commits, who fails, at which minute, and how much work is lost?

@end text="Replay the timeline yourself"
You can replay a timeline under each lock and count the cost, on Learn. That's learn dot get er done dot I O.
