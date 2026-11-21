---
format: long
lesson: enterprise-patterns-objects-and-tables/lazy-load
title: Lazy Load: when being lazy wins, and when it doesn't
thumb: Lazy saves only the unused
---

@chapter The slow list
@title text="Lazy Load" sub="Patterns of Enterprise Application Architecture, Chapters 3 and 11" art=thumb
You've probably seen a list page that's fast with ten rows and slow with fifty. In the log, there's one query for the list, and then one more for each row. This lesson is about why, and when to be lazy.

@art huge-graph
Chapter eleven starts from the opposite habit. It's handy to load an object's related objects with it, so the developer doesn't have to load them by hand. Taken to its conclusion, though, loading one object pulls a huge graph out of the database, when only a few of its objects are needed.

@quote text="As many people know, if you're lazy about doing things you'll win when it turns out you don't need to do them at all." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 11"
A Lazy Load interrupts that. In the pattern's own words: as many people know, if you're lazy about doing things, you'll win when it turns out you don't need to do them at all.

@chapter Four ways
@art marker
It leaves a marker, so data is loaded only when it's used. Fowler adds that in practice two degrees of laziness are enough: a complete load, and enough to identify each item in a list.

@art four-ways
There are four ways to build one. Lazy initialization checks a field on every access. A virtual proxy looks like the real object, and loads it when called. A value holder wraps the object. And a ghost is the real object holding only its key, which loads the rest on first touch.

@code block=1 lines=1-19 label=Java focus="5@in a list|6@a flag|13-16@first call|17@every later call"
Here's lazy initialization. The order keeps its lines in a list, and a flag saying whether they've been loaded. The first call finds the flag false, asks the mapper for the lines, and sets the flag. Every later call skips straight to the return. The list starts empty, so there's no null to test.

@chapter Ripple loading
@art ripple
Then the warning. Fill a collection with lazy objects, and look at them one by one. Each makes its own trip to the database, where one trip could have fetched them all. Fowler calls it ripple loading, and that's your slow list page.

@art lazy-collection
His cure is to make the collection itself the lazy thing, and load all of it when first touched. Another is to give different use cases different loaders. Fowler's own preference is not to add a Lazy Load until he thinks he needs one.

@chapter The count
@words text="5 orders: 3, 0, 5, 2, 4 lines" sub="orders 1, 3 and 5 used · batches of 2"
The lab compares four strategies. Five orders have three, zero, five, two and four lines. Only the first, third and fifth are used, and batches hold two.

@math heading="orders-and-lines" items="lazy: 4 statements, 17 rows@Lazy loading;;lazy in batches: 3 statements, 17 rows@in batches;;two queries: 2 statements, 19 rows@Two queries;;one join: 1 statement, 15 rows@the join"
Lazy loading issues four statements and reads seventeen rows. In batches, three statements, seventeen rows. Two queries, one for orders and one for every line, take two statements and nineteen rows. And the join takes one statement and fifteen rows.

@math heading="every-order-used" items="lazy: 6 statements, 19 rows@lazy is now;;in batches: 4 statements, 19 rows@batches four;;two queries: 2, 19 · join: 1, 15@unchanged"
Now use every order. Lazy is now six statements and nineteen rows, and batches four statements and nineteen rows. Two queries and the join are unchanged. When everything is used, laziness reads no fewer rows, and sends three times the statements.

@art join-rows
Two things the tiles don't show. The join's rows each repeat the order's columns beside the line's, and the lab counts rows, not their width. And a statement's cost depends on your network and database. Fowler's advice is to profile it.

@chapter Where people slip
@list heading="Common slips" items="Lazy always loads less@The first|Make each item lazy@The second|The join's rows are its whole cost@And the third"
The first slip is believing lazy loading always loads less. It saves only what isn't used. The second is making each item of a collection lazy, which is exactly the shape that ripple loads. And the third is reading the join's row count as its whole cost.

@chapter Try it
@words text="a 10 ✓ · b 0 · c 2 · d 6 ✓ · e 1 · f 3 ✓" sub="batches of 3"
Your turn. Six parents: a has ten children, b none, c two, d six, e one, and f three. Only a, d and f are used, and batches hold three. Give the statements and rows of all four strategies.

@end text="Compare the strategies yourself"
You can change what's used and watch each strategy's cost, on Learn. That's learn dot get er done dot I O.
