---
format: long
lesson: enterprise-patterns-objects-and-tables/identity-map
title: Identity Map: one row, one object
thumb: Never load a row twice
---

@chapter Two watches
@title text="Identity Map" sub="Patterns of Enterprise Application Architecture, Chapters 3 and 11" art=thumb
What goes wrong if you load the same database row twice in one session? Quite a lot, it turns out. And the fix is one of the simplest patterns in the book.

@quote text="An old proverb says that a man with two watches never knows what time it is." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 11"
The pattern opens with a proverb. An old proverb says that a man with two watches never knows what time it is.

@art two-watches
That proverb is the pattern's first reason in miniature. Two copies of the same thing, and no way to tell which one is right.

@art two-copies
Load the same row into two objects, and change them both, and everything gets very confusing. Two in memory objects claim to be one record. And whichever is written last decides what the database holds.

@chapter The guard
@art map-lookup
The cure is to keep a record of every row read, and check it before each read. If the row's already loaded, return a second reference to the object you already have. As a benefit, the record doubles as a cache. But Fowler is explicit: the map is there first so each row has one object. Speed is a side benefit.

@code block=1 lines=1-19 label=Java focus="3-4@The map|7@looks in it first|8-10@only when the key is missing|12@same object"
Here's an explicit map written for the lesson. The map is a field. Find looks in it first, and only when the key is missing does it load the row and record the new object. A second find for the same key returns the same object, without the query.

@chapter Keys and scope
@words text="Key on a surrogate key" sub="one column, never changes"
The map is keyed on the table's primary key, which works well if the key is one column and never changes. So a surrogate key, a number with no meaning outside the database, suits it. Fowler prefers explicit maps, with a method for each kind of object, for compile time checking.

@art session-boxes
Where the maps live matters most. Each session needs its own, isolated from every other session's, and the Unit of Work is by far the best place to keep them. A map shared between sessions would need transactional protection of its own. The exception is objects that are never, or very rarely, changed.

@chapter The count
@words text="customer 7 · order 31 · customer 7 · order 32" sub="customer 7 · product 5 · product 5"
The lab reads a session's finds in order. In one session, it finds customer seven, order thirty one, customer seven, order thirty two, customer seven, product five and product five.

@math heading="one-session" items="7 finds@seven finds;;4 distinct objects@four distinct;;3 duplicates@three duplicates;;customer 7 ×3, product 5 ×2@customer seven"
That's seven finds, four distinct objects, and three duplicates. Customer seven is found three times, and product five twice.

@art shared-reference
Read that with both of Fowler's reasons. Without a map, the session holds three objects for customer seven and two for product five, and a change made through one is invisible to the others. With it, four objects, and three of the seven finds need no query.

@words text="no-repeats: 3 finds, 0 duplicates" sub="the map still does its job"
Now find three different rows once each. Three finds, three distinct, no duplicates. The map does nothing for speed here. But it still guarantees that a later find would return the same object.

@chapter What it doesn't do
@art query-many
The map answers a find by key. A query for many rows, like everyone whose surname matches a pattern, still has to go to the database, because nothing guarantees all the matches are loaded. And it prevents conflicting updates within one session only.

@chapter Where people slip
@list heading="Common slips" items="It's a performance cache@The first|One map on the whole server@The second|It answers every query@And the third"
The first slip is thinking an Identity Map is a performance cache. Its first reason is correctness. The second is putting one map on the whole server. It belongs to a session. And the third is expecting the map to answer every query.

@chapter Try it
@words text="room 12 · guest 3 · room 14 · guest 3" sub="room 12 · guest 9 · guest 3"
Your turn. A hotel session finds room twelve, guest three, room fourteen, guest three, room twelve, guest nine, and guest three. Count the finds, the distinct rows and the duplicates, and say which objects are shared, and how often.

@end text="Count the duplicates yourself"
You can type a session's finds and see what the map shares, on Learn. That's learn dot get er done dot I O.
