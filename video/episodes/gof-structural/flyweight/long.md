---
format: long
lesson: gof-structural/flyweight
title: Flyweight: 950 objects for the price of four
thumb: Share what never changes
---

@chapter Too many objects
@title text="Flyweight" sub="Design Patterns, chapter 4" art=thumb
Sometimes the cleanest design has an object for every little thing, and there are far too many things. Flyweight is how the Gang of Four make that affordable, and they're unusually strict about when it applies.

@quote text="Use sharing to support large numbers of fine-grained objects efficiently." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 4"
That's the whole of the intent. Use sharing to support large numbers of fine grained objects efficiently.

@art letter-objects
The book's example is a document editor that would like an object for every character. It can't afford hundreds of thousands of them. So there's one shared object per character code, and every occurrence of that letter refers to it.

@chapter Two kinds of state
@art intrinsic-extrinsic
The character code is intrinsic: it's stored in the shared object, because it's the same everywhere. The position and style are extrinsic. The layout works them out as it goes, and hands them to the shared object when it draws. Logically, there's an object at every occurrence. Physically, there's one per letter.

@code block=1 lines=1-8 label=Java focus="3@about two kilobytes|5@passed in"
Here's the lesson's garden planner. A plant kind is the flyweight. It holds a sprite, about two kilobytes, shared by every tomato on the plan. And draw takes the position as an argument. The extrinsic state is passed in.

@code block=1 lines=9-18 label=Java focus="11@a pool|14-16@made on first request"
And the factory keeps a pool, one plant kind per species, made on first request. Clients never create flyweights themselves. That's what guarantees they're shared.

@words text="180,000 characters · 480 objects" sub="the InterViews editor Doc, as the book gives it"
And it works in practice. The book reports that in the InterViews document editor, Doc, a document of a hundred and eighty thousand characters needed only four hundred and eighty character objects.

@chapter Five conditions
@list heading="Apply it only when all hold" items="A great many objects@a great many|Costly because of their number@simply because|Most state can be extrinsic@made extrinsic|A few shared objects remain@a few shared|No reliance on identity@identity"
The authors say to apply it only when all five of these hold. There are a great many objects. Storing them is costly simply because there are so many. Most of their state can be made extrinsic. Then a few shared objects can stand in for large groups. And the application doesn't depend on identity.

@words text="Shared means the same object"
That last condition is easy to forget. Two tomatoes that share a flyweight are one object, so an identity test can't tell them apart.

@chapter Count it
@art garden-plot
In the lab, the plot has a hundred and twenty tomatoes, three hundred basil, four hundred and fifty lettuces, and eighty marigolds. A species' sprite takes two thousand and forty eight bytes, a position eight, and a reference four.

@math heading="Bytes for the garden plan" items="plants: 120 + 300 + 450 + 80 = 950@nine hundred and fifty;;without sharing: 950 × (2048 + 8) = 1,953,200@without sharing;;with sharing: 4 × 2048 + 950 × 8 + 950 × 4 = 19,592@with sharing;;saved: 1,933,608, about 99%@ninety nine"
That's nine hundred and fifty plants. Without sharing, each carries both kinds of state: one million, nine hundred and fifty three thousand, two hundred bytes. With sharing, four sprites, plus a stored position and a reference per plant: nineteen thousand, five hundred and ninety two. About ninety nine percent saved.

@art shared-pool
Now compute each position from its row and the spacing, instead of storing it. That drops to eleven thousand, nine hundred and ninety two bytes, about ninety nine point four percent saved. The most is saved when the extrinsic state can be computed.

@chapter When it costs more
@art no-sharing
But the lab also breaks the conditions. Three name tags, each with its own text. Three flyweights for three objects. Unshared, they take two hundred and sixteen bytes. Shared, two hundred and twenty eight. The saving is minus twelve. With as many intrinsic states as objects, the references are all cost.

@list heading="Common slips" items="Using it wherever there are many objects@The first|Leaving context in the flyweight@The second|Comparing by identity@And the third"
So, three slips. The first is applying it wherever there are many objects. The second is leaving context in the flyweight, so every context sees the last one's value. And the third is comparing flyweights by identity.

@art factory
And remember what the byte count leaves out. Finding, passing or computing extrinsic state costs time. The space saving has to pay for it.

@chapter Try it
@words text="200 dock icons" sub="40 full · 25 empty · 135 some · 1,024 B shared · 16 B position · 4 B reference"
Your turn. A bike share map draws two hundred dock icons in three states. Each state's icon is one thousand and twenty four bytes, a stored position sixteen, and a reference four. Give the bytes without sharing, with flyweights, and the saving.

@end text="Count the bytes"
Then type the figures into the lab and check, on Learn. That's learn dot get er done dot I O.
