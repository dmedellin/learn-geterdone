---
format: long
lesson: enterprise-patterns-objects-and-tables/embedded-value-and-serialized-lob
title: Embedded Value and Serialized LOB: objects without a table
thumb: One column, one query
---

@chapter Not worth a table
@title text="Embedded Value and Serialized LOB" sub="Patterns of Enterprise Application Architecture, Chapters 3 and 12" art=thumb
Does every object deserve a table of its own? Fowler says no, and gives two answers: one for small values, and one for whole trees of objects.

@chapter Embedded Value
@art owner-row
Start with small values. A date range or an amount of money is a Value Object. It has no identity, only a value, so nobody needs to find it by key, and a table of nothing but amounts would be absurd. So its fields go into the owner's row, and the owner loads and saves them.

@code block=1 lines=1-7 label=Java focus="3-5@two columns|6@hands it to the lease"
Here's one written for the lesson. A lease's term is a DateRange, built from two columns of the lease's own row, term start and term end. The range has no key and no table. The last line hands it to the lease, with the lease's own key.

@art embedded-columns
Because a value has no identity, it needs no Identity Map either. You can make a new one on every read. And the great advantage over a LOB, Fowler says, is that SQL can still query the embedded values.

@words text="A reference object? Usually one-to-one"
What about a reference object, like a shipping record on an order? Fowler asks whether it means anything outside the order, whether it's always loaded with it, and whether anyone queries it separately. He uses the pattern there mostly where the link is one to one.

@chapter Serialized LOB
@art reply-tree
Serialized LOB is the same move on a larger scale. Take a cluster of objects and save it as a single column. Chapter three names the use: hierarchic structures, like an organisation chart or a bill of materials, which a relational schema reads with many small calls, and a LOB reads in one.

@code block=2 lines=1-19 label=Java focus="4-7@stack of posts|11@one line per post|13-16@pushed last first"
Here's a text serialization for a discussion thread. It walks the thread with a stack of posts and a matching stack of depths, and writes one line per post, its depth and its id. Replies are pushed last first, so they come off in order.

@chapter The count
@math heading="thread · 8 posts, depth 4" items="node by node: 1 + 8 = 9 queries@post by post;;level by level: 4 + 1 = 5 queries@level by level;;as a LOB: 1 query@from the column"
Take a thread with eight posts, four levels deep. Read it post by post, one query for the root and then one for each post's children, and that's nine queries. Level by level, five. From the column, one.

@art level-by-level
Both multi query counts include the queries that come back empty. Each leaf asks for children it doesn't have, and the level below the deepest is how a program learns it's finished. A flat thread, one post with three replies, takes five, three, and one.

@chapter The cost
@quote text="If you use it too much, it ends up turning your database into little more than a transactional file system." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 3"
So the column always wins on queries. But Chapter three warns: if you use it too much, it ends up turning your database into little more than a transactional file system.

@art one-column
SQL can't query inside it, so every query you might have run, like all of one person's replies, is gone. It invites duplication, and it works poorly when objects outside it refer to objects inside it. Today many databases can index and query a JSON or XML column, which takes away part of that reason, but not the rest.

@chapter Where people slip
@list heading="Common slips" items="A LOB because it's fast@The first|An Embedded Value with its own key@The second|Shared data copied into many LOBs@And the third"
The first slip is preferring a LOB just because it's fast. The second is giving an Embedded Value a key of its own. It's part of its owner's row. And the third is copying shared data, like a customer's details, into many LOBs, so every update must find every copy.

@chapter Try it
@words text="root · a → root · b → a · c → b · d → c · e → root"
Your turn. Root has two children, a and e. Then b under a, c under b, and d under c. Give the nodes and the depth, and the queries to read it node by node, level by level, and as a Serialized LOB.

@end text="Count the queries yourself"
You can type in a tree and compare the three ways of reading it, on Learn. That's learn dot get er done dot I O.
