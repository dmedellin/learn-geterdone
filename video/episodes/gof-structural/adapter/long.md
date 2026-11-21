---
format: long
lesson: gof-structural/adapter
title: Adapter: make a class you can't change fit the interface you have
thumb: Fit it, don't edit it
---

@chapter The structural patterns
@title text="Adapter" sub="Design Patterns, chapter 4" art=thumb
Chapter four of Design Patterns is about structure, and it opens with the pattern you've probably already written without naming it. Let's see what the book says about it, and the one trade-off that decides which form to use.

@quote text="Structural patterns are concerned with how classes and objects are composed to form larger structures." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 4"
That's the chapter's first sentence. Structural patterns are concerned with how classes and objects are composed to form larger structures.

@list heading="Two kinds" items="Class patterns: inheritance@class patterns|Object patterns: composition@object patterns|Can change at run time@while the program runs"
The authors sort the seven patterns by mechanism. Structural class patterns put interfaces or implementations together by inheritance. Structural object patterns put objects together, and that buys something inheritance can't: the composition can change while the program runs.

@chapter The mismatch
@art plug-mismatch
Here's Adapter's problem. Your code is written against one interface. A class, often from a library you didn't write, does the work, but it answers to different names and arguments. Editing the library is rarely possible, and even with the source it's the wrong move. A general purpose class shouldn't take on one application's vocabulary.

@art adapter-between
So you put a small class in between. It turns a class's interface into the one its clients expect, so classes that couldn't work together now can. The book also calls it Wrapper.

@list heading="Four participants" items="Target@the target|Client@the client|Adaptee@the adaptee|Adapter@the adapter"
There are four participants. The target is the interface the client was written against. The adaptee is the existing class that doesn't match. And the adapter implements the target by calling the adaptee. The collaboration is one sentence: the client calls the adapter, and the adapter calls the adaptee.

@art drag-extra
And an adapter can do more than rename. In the book's drawing editor, an adapter makes a toolkit's text view behave like a shape, and also supplies an object for dragging it about, which the view never had.

@chapter Two forms
@code block=1 lines=1-16 label=Java focus="2-4@the target is|8-9@holds a label jet|11-15@feeds the stock"
Here's the lesson's box office. The target is the ticket printer interface the desk was written against. The vendor's class is called label jet. This object adapter holds a label jet, the vendor's class or any subclass of it, and its print method feeds the stock, writes the line, and cuts.

@code block=2 lines=1-11 label=Java focus="2@extends label jet|9-10@overrides beep"
The class form extends label jet and implements the target. It is a label jet, so it adapts that one class. And notice the last method. It overrides beep, and overriding the adaptee is one line.

@chapter The trade-off
@art class-adapter-each
A class adapter commits to one concrete adaptee class, so it can't cover that class and its subclasses together. In exchange, it can override the adaptee's behaviour, and it adds no second object to reach through.

@art object-adapter-family
An object adapter is the reverse. One adapter works with the adaptee and all its subclasses, and can add a feature to all of them at once. But overriding the adaptee now means writing a subclass of it, and pointing the adapter at that.

@chapter Count it
@math heading="Three printers, two designs" items="desk + target + vendor = 1 + 1 + 3 = 5@one plus one plus three;;class adapters: 5 + 3 = 8 classes@five plus three;;object adapter: 5 + 1 = 6 classes@five plus one;;uses: 1 + 3 × 2 + 2 = 9 vs 1 + 2 + 2 = 5@nine uses"
The vendor ships label jet and two subclasses. The desk, the target and the vendor classes make one plus one plus three, five. Class adapters need one per vendor class, so five plus three is eight classes. One object adapter makes five plus one, six. And the uses come to nine uses against five.

@words text="3 adapters vs 1" sub="but beep: one line vs a new subclass"
The difference is the adapters themselves, three against one, and it grows by one for every vendor subclass. What the count doesn't show is the other column: the class adapter overrode beep in one line, and the object adapter would need a fourth vendor subclass to do the same.

@chapter Variations
@art two-way
Two variations round it out. A pluggable adapter builds the adaptation into a reusable class, like a widget that draws any tree. And a two way adapter conforms to both interfaces, so two clients can each see one object as their own.

@chapter Where people slip
@list heading="Common slips" items="Treating the two forms as interchangeable@The first|Expecting only renaming@The second|Changing the library to fit@And the third"
The first slip is treating the two forms as interchangeable. They make opposite trade-offs. The second is expecting an adapter only to rename operations. And the third is changing the library class to fit your code, instead of keeping your vocabulary on your own side.

@chapter Try it
@words text="A fourth printer" sub="LabelJetColour extends LabelJet"
Your turn. The vendor ships a fourth printer, label jet colour, another subclass. By hand, give the classes and the distinct uses under each design once it's supported. Then ask yourself which one needed a new adapter.

@end text="Count both designs"
Then type the records into the lab and check, on Learn. That's learn dot get er done dot I O.
