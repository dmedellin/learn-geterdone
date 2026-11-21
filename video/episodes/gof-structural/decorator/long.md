---
format: long
lesson: gof-structural/decorator
title: Decorator: stack features at run time instead of subclassing
thumb: Wrap it, don't subclass it
---

@chapter One object, not the class
@title text="Decorator" sub="Design Patterns, chapter 4" art=thumb
You want one object to have an extra feature, not every object of its class. Decorator is how the Gang of Four do that, and by the end you'll see why the order you stack them in can change the answer.

@quote text="Decorators provide a flexible alternative to subclassing for extending functionality." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 4"
That's the second sentence of the intent. Decorators provide a flexible alternative to subclassing for extending functionality. The first says it attaches responsibilities to an object at run time. Like Adapter, it's also called Wrapper.

@art border-scroll
The book's question is how to give one user interface component a border, or scrolling. Inheriting a border decides for every instance, and the client has no say. So instead you enclose the component in another object, the decorator, that adds the border.

@chapter Transparent enclosure
@art nested-wrappers
Because the decorator has the component's interface, its clients don't see it. And because they don't see it, decorators can nest. The book wraps a text view in a scrolling decorator, and that in a border.

@code block=1 lines=1-19 label=Java focus="1-3@price interface|4-8@the seat|9-12@abstract decorator|13-18@member discount|19@built up"
Here's the lesson's version, a theatre seat's price. There's a price interface, and the seat itself, which just returns its base. The abstract decorator holds an inner price. A member discount asks the inner price for its amount and multiplies by nought point nine. And the last line shows a stack built up, insurance on the outside.

@chapter Benefits and liabilities
@list heading="Two benefits" items="More flexible than inheritance@more flexible|Pay only for what you attach@pay for"
The authors count two benefits. It's more flexible than static inheritance: responsibilities attach and detach at run time, mix and match, and the same one can be added twice. And it avoids feature laden classes high in the hierarchy. You pay for the features you attach.

@art little-objects
And two liabilities. A decorator and its component aren't the same object, so code that relies on identity will be surprised. And the design becomes lots of little objects that look alike and differ only in how they're connected. Easy to customise if you understand it, hard to learn and debug.

@chapter Trace the stack
@art in-and-out
In the lab, a stalls seat costs thirty two. Innermost first, there's a booking fee that adds two fifty, a member discount, times nought point nine, and insurance that adds one seventy five. The request goes in through insurance, the discount and the fee, reaches the seat, and the answers come back out the other way.

@math heading="From the inside out" items="seat: 32@the seat;;fee: 32 + 2.50 = 34.50@the fee;;member: 34.50 × 0.9 = 31.05@the discount;;insurance: 31.05 + 1.75 = 32.80@insurance"
So, the seat, thirty two. Then the fee: thirty two plus two fifty, thirty four fifty. Then the discount: thirty four fifty times nought point nine, thirty one oh five. Then insurance: plus one seventy five, thirty two eighty.

@art order-swap
Now reverse the stack. Thirty two plus one seventy five, times nought point nine, plus two fifty, gives thirty two point eight seven five. The order changed the result, because a discount applied after the fee discounts the fee too.

@chapter Count the classes
@math heading="Three on or off options" items="subclasses: 2³ = 8@two cubed;;decorators: 3 + 3 = 6@three plus three;;a fourth option: +8 vs +1@a fourth option"
Three options as subclasses need a class for every combination: two cubed, eight. With Decorator it's three plus three, six: the interface, the seat, the abstract decorator, and three decorators. And a fourth option doubles the first count, adding eight, but adds just one to the second.

@art subclass-grid
But with only the fee and insurance, it's four classes against five, so with two options the subclasses are actually fewer. It's the combinations, not the options, that make the explosion. And three decorators on one seat are four objects where a subclass would be one.

@chapter Where people slip
@list heading="Common slips" items="Assuming order doesn't matter@The first|Counting classes, not objects@The second|Decorating a heavyweight component@And the third"
The first slip is assuming order doesn't matter. The second is counting only the classes and not the objects. And the third is decorating a heavyweight component. Every decorator carries its whole interface, so the authors suggest changing the guts instead: a strategy object the component delegates to.

@chapter Try it
@words text="A circle seat at 24" sub="fee + 2.50 · member × 0.9"
Your turn. A circle seat at twenty four, with a fee and a member discount. By hand, give the result in the order given and in reverse, and the classes as subclasses and with Decorator.

@end text="Stack the decorators"
Then type the records into the lab and check, on Learn. That's learn dot get er done dot I O.
