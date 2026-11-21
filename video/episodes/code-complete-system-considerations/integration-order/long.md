---
format: long
lesson: code-complete-system-considerations/integration-order
title: Integration order: big bang, top-down, bottom-up, or risk first?
thumb: One piece at a time
---

@chapter The question
@title text="Integration Order" sub="Code Complete, chapter 29" art=thumb
In what order should the pieces of a system be put together? Integration means combining separately written components into one system. And it can't be separated from the order they're built in, because nothing can be integrated before it exists.

@art stadium
McConnell's illustration is from his own region. A stadium extension at the University of Washington collapsed partway through construction. It would probably have stood when finished. It was built in an order in which it couldn't stand at each step. Software built in the wrong order is harder to code, test and debug in the same way.

@chapter Phased or incremental
@art big-bang
Phased integration develops and tests every class alone, combines them all at once, then tests the whole. Every problem appears together, and any class is a suspect. That's why the book also calls it big bang integration.

@art skeleton-grow
Incremental integration starts with a small working skeleton, then adds one tested class at a time, testing each combination before the next. When something breaks, the new class or its connection is where to look. The system works early, and progress shows as features.

@quote text="Incremental integration comes in several varieties, and, unless the project is trivial, any one of them is better than phased integration." cite="McConnell, Code Complete, 2nd ed., Chapter 29, p. 708"
That's the chapter's key point. Incremental integration comes in several varieties, and, unless the project is trivial, any one of them is better than phased integration.

@chapter The orders
@art top-down
Top down starts with the class that holds main, and replaces stubs with real classes going down. It exercises the control logic early, but it leaves the tricky low level interfaces until last, and needs, in McConnell's phrase, a dump truck full of stubs. Integrating in vertical slices is the workable form.

@words text="Stub: called before it's integrated" sub="Driver: test code that calls it before its callers arrive"
Bottom up reverses it. Low level classes first, exercised by test drivers until their callers arrive. A stub stands in for something not yet integrated. A driver calls something whose real callers aren't integrated yet.

@list heading="Blends" items="Sandwich: top and bottom first@Sandwich|Risk-oriented: hardest parts first@risk oriented|Feature-oriented: one feature at a time@feature oriented|T-shaped: one deep slice, then breadth@T shaped"
Then four blends. Sandwich does the top and bottom first and the middle last. Risk oriented does the hardest parts first, wherever they sit. Feature oriented adds one feature's classes at a time. And T shaped does one deep slice end to end, then the breadth.

@chapter Count the scaffolding
@art call-graph
The lab's call graph has six components. Main calls ui and orders. Ui calls widgets. Orders calls pricing and db. And pricing calls db too.

@math heading="Stubs and drivers" items="top-down:  5 stubs · 0 drivers@top down;;bottom-up:  0 stubs · 5 drivers@bottom up;;risk-first:  3 stubs · 2 drivers@risk first"
Integrate top down, and everything below the top is called before it arrives. Five stubs, no drivers. Bottom up, db first and main last, needs no stubs and five drivers. And risk first, starting with pricing as the hard part, needs three stubs and two drivers.

@words text="Risk-first stubs: db, ui, widgets" sub="drivers: pricing, orders"
The stubs are db, ui and widgets, and the drivers are pricing and orders. Doing the hardest part first costs scaffolding of both kinds, which is the trade the chapter accepts. The lab can't tell how big each stub is, or how risky each part. That's for you to judge.

@chapter The daily build
@art daily-build
Whatever the order, add the daily build and smoke test. Every file is compiled, linked and combined into a program every day, and run through a simple test of the whole system to see whether it smokes. A broken build is fixed first. If it worked yesterday and is broken today, something since yesterday broke it.

@chapter Where people slip
@list heading="Common slips" items="Integration as a phase at the end@The first|Pure top-down as the safe order@The second|Least scaffolding as the best order@the third"
The first slip is treating integration as a phase at the end. That's big bang. The second is thinking pure top down is the safe, textbook order. The book calls it nearly impossible. And the third is thinking the best order has the least scaffolding. A count is a reason to look, not a ranking.

@chapter Try it
@code block=1 lines=1-20 label=Java focus="3-4@app|9@ui|14@core"
Your turn. Read the calls off these four classes, each a caller and callee pair. Integrate them in the order app, ui, core, store. Then list the components that need a stub, and those that need a driver.

@end text="Walk an integration order"
You can type the pairs and the order into the integration lab to check, on Learn. That's learn dot get er done dot I O.
