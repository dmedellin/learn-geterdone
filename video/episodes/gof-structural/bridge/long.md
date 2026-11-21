---
format: long
lesson: gof-structural/bridge
title: Bridge: stop one class hierarchy from multiplying
thumb: Sum, not product
---

@chapter Two ways to vary
@title text="Bridge" sub="Design Patterns, chapter 4" art=thumb
Some classes vary in two ways at once, and if you handle that with inheritance, the class count multiplies. Bridge is the Gang of Four's answer, and by the end you'll be able to count exactly what it saves.

@quote text="Decouple an abstraction from its implementation so that the two can vary independently." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 4"
That's the intent, as the book states it. Decouple an abstraction from its implementation so that the two can vary independently. It's also known as Handle, Body.

@words text="Inheritance fixes the pairing" sub="for good"
The usual way to give an abstraction several implementations is inheritance: an abstract class, and a concrete subclass for each way of carrying it out. The authors' objection is that inheritance fixes the pairing for good. Abstraction and implementation can't be changed, extended or reused apart.

@chapter The window problem
@art window-subclasses
The book's example is a portable window class for two window systems. Add a special kind of window, and you need a subclass of it for each system. Add a third system, and every kind of window needs one more. Worse, a client that creates a window must name a system specific class, so it's tied to the platform too.

@art two-hierarchies
The answer is two hierarchies. One for the kinds of window, one for the platform implementations, and every window operation is written in terms of the implementation's interface. The reference from one to the other is the bridge.

@chapter The code
@code block=1 lines=1-15 label=Java focus="3@the bridge|7-14@highlights guide"
The lesson's version is a museum audio guide. The abstract guide holds a player, and that field is the bridge. A highlights guide only refines what a guide does. When it arrives at a stop that's a highlight, it asks the player to show the title, and play a short clip.

@code block=1 lines=16-20 label=Java focus="17-20@a few primitives"
And the player is the implementor: a few primitives every device supplies. It doesn't mirror the guide. The guide builds its higher level behaviour from these.

@art primitives
That's worth stressing. The implementor's interface is expected to be smaller than the abstraction's. Copy the abstraction's operations into it, and you push the abstraction's logic into every implementation.

@chapter What it buys
@list heading="Three consequences" items="Interface and implementation decoupled@decoupled|Each side extends on its own@extended on its own|Details hidden from clients@hidden"
The book lists three consequences. Interface and implementation are decoupled, so an implementation can be chosen or even swapped while the program runs, and changing one needn't force clients to be recompiled. Each hierarchy can be extended on its own. And details, like shared implementor objects, can be hidden from clients.

@art player-swap
Someone still has to create the right implementor. The abstraction can choose from its constructor's arguments, start with a default and switch later, or ask another object, such as an Abstract Factory, so it never names an implementor class at all.

@chapter Count it
@math heading="Three guides, three players" items="3 × 3 = 9 pairings@three times three;;subclass per pairing: 9 + 1 = 10@nine plus one;;bridge: (3 + 1) + (3 + 1) = 8@three plus one;;new player: 10 → 13 vs 8 → 9@a fourth player"
Three kinds of guide run on three players. That's three times three, nine pairings. One subclass per pairing, under one abstract guide, is nine plus one, ten classes. The bridge is three plus one, twice, eight. Now add a fourth player. Subclassing goes from ten to thirteen. The bridge goes from eight to nine.

@art product-grid
The subclass count is the product of the variant counts, and the bridge's is their sum. So the gap widens as either side grows. With five players, it's sixteen classes against ten.

@chapter When not to
@art degenerate
But none of that says to build one. With one implementation and none in sight, the authors call it a degenerate bridge, and it only buys insulation from recompiling. It's growth on both sides that the pattern pays for.

@list heading="Common slips" items="Reading Bridge as Adapter@The first|Mirroring the abstraction@The second|Bridging what varies one way@The third"
Three slips. The first is reading Bridge as Adapter under another name. Bridge is designed in up front, Adapter is fitted later. The second is making the implementor mirror the abstraction. The third is bridging a hierarchy that only varies one way.

@chapter Try it
@words text="4 notices · 3 channels" sub="ready, reminder, returned, overdue · sms, email, app"
Your turn. A parcel locker sends four kinds of notice through three channels. By hand, count the classes with one subclass per pairing, and with a bridge. Then say what a fourth channel adds to each.

@end text="Product or sum?"
Then check your counts in the lab, on Learn. That's learn dot get er done dot I O.
