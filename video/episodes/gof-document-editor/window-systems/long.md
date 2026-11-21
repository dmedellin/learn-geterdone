---
format: long
lesson: gof-document-editor/window-systems
title: Bridge in Lexi: running on window systems you don't control
thumb: Two hierarchies, one reference
---

@chapter Four window systems
@title text="Supporting Multiple Window Systems" sub="Design Patterns, Section 2.6" art=thumb
A window system manages overlapping windows on the screen, and routes keyboard and mouse input to them. In nineteen ninety five there were several, Macintosh, Presentation Manager, Windows and X, with largely incompatible interfaces. Lexi has to run on all of them.

@art no-common-base
Why not a factory per window system, like the last lesson? Because Abstract Factory worked for widgets only because the authors wrote the widget classes themselves, from a common abstract base. Hierarchies from different vendors share no such base, and Lexi can't write its own window system to supply one.

@words text="They all do broadly the same things"
What Lexi can do is notice that window systems all do broadly the same things, and slide each one under a common interface.

@chapter How much interface?
@art intersection-union
That interface is the Window class. How much should it offer? Only what every window system has, and Lexi is as weak as the weakest. Everything any of them has, and the interface is huge, incoherent, and changes with every vendor's release. The authors settle in between.

@words text="Popular window operations + drawing" sub="subclasses: application window · icon · dialog"
So Window offers the popular windowing operations, plus the graphics operations glyphs need to draw themselves. Its subclasses are kinds of window: an application window, an icon, a dialog.

@chapter Where the platform code goes
@art platform-explosion
Two ways are dismissed. A separate version of every window class for each platform, chosen at build time. Or a platform subclass of every kind of window, which the authors call another subclass explosion. Neither lets the window system change after compiling.

@art window-windowimp
Their third way is the chapter's refrain: encapsulate the concept that varies. Each window system's functionality goes in an object, a WindowImp, and Window is implemented in terms of it. A request to draw a rectangle becomes a call on the implementation, and each subclass carries it out its own way.

@chapter Bridge
@quote text="The intent behind Bridge is to allow separate class hierarchies to work together even as they evolve independently." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Section 2.6"
Which implementation does a window get? An abstract factory, one per window system, supplies it. And the relationship between the two hierarchies is Bridge. The intent behind Bridge is to allow separate class hierarchies to work together even as they evolve independently.

@list heading="What it gives, and costs" items="Choose the implementation at run time@at run time|Extend each side on its own@on its own|A second hierarchy to maintain@a second hierarchy|A call through for every request@a call through"
The catalog lists the gains. The implementation can be chosen at run time, each hierarchy can be extended on its own, and clients don't see implementation details. It names no liability, but the section shows some: a second hierarchy to maintain, a call through the implementation for every drawing request, and an interface that must fit systems that differ.

@chapter Library notices
@art library-notices
The lab's design is a library that sends notices, overdue, hold ready and renewal, through channels it doesn't control: email, text and app push, each with its own provider's interface.

@code block=1 lines=2-19 focus="3@holds its implementation|5-7@delivering just|10-15@overdue|17-19@delivery services"
A notice holds its implementation, a channel. Delivering just asks the channel to send. An overdue notice is one kind of notice. And the channel interface caters to the delivery services, not to the library.

@math heading="3 notices × 3 channels" items="subclasses: 3 × 3 = 9 → 9 + 1 = 10@nine plus one;;bridge: (3 + 1) + (3 + 1) = 8@eight;;fourth channel: 10 → 13 vs 8 → 9@a fourth channel"
Three kinds on three channels is nine combinations, so a platform subclass of every kind needs nine plus one, ten classes. Two hierarchies need eight. A fourth channel adds three subclasses, against one class, and no notice is touched.

@math heading="Add a letter, then a notice" items="3 × 4 = 12 → 13 classes vs 9@thirteen classes;;new notice: 13 → 17 vs 9 → 10@the new notice"
Add a letter channel, and there are twelve combinations: thirteen classes against nine. Then the new notice costs four subclasses, against one.

@art reference-swap
The ratio isn't large here, five quarters on the first preset. What the authors argue from is that one count multiplies and the other adds, and that only the reference lets a notice be given a different channel while the program runs.

@chapter Where people slip
@list heading="Common slips" items="Abstract Factory because it looks the same@The first|A platform subclass of every class@The second|Mirroring the abstraction@And the third"
The first slip is applying Abstract Factory because the problem looks the same. The second is adding a platform subclass to every class in a hierarchy. And the third is making the implementation interface mirror the abstraction. The two serve different readers.

@chapter Try it
@words text="2 documents · 4 printers" sub="receipt, label · thermal, laser, inkjet, pdf"
Your turn. A shop prints receipts and labels on four kinds of printer, each with its own driver. Count the classes under each design, and what a fifth printer adds to each.

@end text="Build the bridge"
Then type it into the lab and check, on Learn. That's learn dot get er done dot I O.
