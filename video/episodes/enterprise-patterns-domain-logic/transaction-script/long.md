---
format: long
lesson: enterprise-patterns-domain-logic/transaction-script
title: Transaction Script: one procedure per user action
thumb: Simple, until it copies
---

@chapter Three ways
@title text="Transaction Script" sub="Patterns of Enterprise Application Architecture, Chapters 2 and 9" art=thumb
Fowler's second chapter sets out three ways to organise domain logic, the middle layer. He starts with the simplest, and he's warmer about it than you might expect.

@chapter The idea
@art script-pipeline
A Transaction Script is essentially a procedure. It takes input from the presentation, validates it, calculates, stores data, calls any other systems it needs, and replies.

@art one-per-action
Its organising principle is one procedure for each action a user might want to do. So a shop has one script for checking out, and another for showing what's in the basket. Pieces can be split into subroutines and shared, but the shape is still one procedure per action.

@chapter Why it's good
@quote text="The glory of Transaction Script is its simplicity. Organizing logic this way is natural for applications with only a small amount of logic, and it involves very little overhead either in performance or in understanding." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 9"
Here's how the pattern's When to Use It opens. The glory of Transaction Script is its simplicity. It's natural for applications with only a small amount of logic, with very little overhead, in performance or in understanding.

@list heading="Three advantages" items="Most developers know the style@procedural style|Sits on a simple data source@simple data source|The transaction boundary is obvious@transaction boundary"
Fowler gives it three advantages. Most developers already know the procedural style. It sits easily on a simple data source layer, like a Row Data Gateway or a Table Data Gateway. And the transaction boundary is obvious: open it at the start of the script, and close it at the end.

@art gateway-wall
Notice that even the simplest scripts in the lesson hold no SQL. They call a gateway, which is how Fowler keeps the database apart. He also keeps scripts out of the presentation, so they're easy to change and to test, usually with several related scripts to a class.

@chapter The catch
@art copied-block
The disadvantages appear as the logic grows. Several transactions do much the same work, and since each script handles just one transaction, code that two of them need tends to get written twice.

@code block=1 lines=1-17 label=Java focus="3-5@lines three to five|12-14@twelve to fourteen"
Here are two scripts from the lesson. One places an order, one quotes its price, and each works out the member discount for itself. The lab finds one repeated block: lines three to five, and twelve to fourteen. That's the subtotal, the test for a member, and the discount. Three lines, in two copies, six in all.

@words text="One rule, two homes"
If the member discount changes, both copies must change. That is exactly the duplication Fowler warns about. And nothing in either script says the other exists.

@chapter The first remedy
@code block=2 lines=1-16 label=Java focus="2-8@memberPrice|10-12@placeOrder|14-16@quotePrice"
Fowler's first remedy is a shared subroutine. The discount is written once, as memberPrice, and both scripts call it. Now placeOrder is one line, quotePrice is one line, and the lab finds zero repeated blocks. The rule has one home.

@art shared-subroutine
But the chapter is careful. Much of the duplication, Fowler says, is hard to remove, and harder still to notice. The lab matches text, so if the second copy had called its variable price instead of total, it would report nothing, though the rule would still be written twice.

@art tangle
Left alone, the application can end up a tangle of routines with no clear structure. More complex domains need a Domain Model. But Fowler cautions against his own enthusiasm: the world is full of simple problems, and a simple solution gets you running faster.

@chapter Where people slip
@list heading="Common slips" items="It's a beginner's pattern@The first|A script holds its own SQL@The second|Subroutines end the duplication@And the third"
The first slip is treating it as a beginner's pattern that serious systems grow out of. Fowler's own When to Use It tells you not to rule it out. The second is thinking a script must hold its own SQL, when a gateway can sit between them. And the third is expecting subroutines to end the duplication.

@chapter Try it
@code block=3 lines=1-19 label=Java focus="2@check out|12@show basket"
Your turn. Here are two scripts, one to check out a cart, and one to show basket contents. Mark the lines they repeat, give their numbers, and write the subroutine both would call, with its signature and its body.

@end text="Count the copies yourself"
You can paste two scripts into the lab and see what they repeat, on Learn. That's learn dot get er done dot I O.
