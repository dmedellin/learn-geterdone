---
format: long
lesson: ddd-supple-design/intention-revealing-interfaces
title: Intention-Revealing Interfaces: name the purpose, not the means
thumb: Name what it's for
---

@chapter Serving the developer
@title text="Intention-Revealing Interfaces" sub="Domain-Driven Design, Chapter 10" art=thumb
Chapter ten asks a question the book has mostly left aside. What kind of design does a developer want to work with? Software exists for its users, but before it can serve them, it has to serve the people who build it and keep changing it.

@art copy-not-reuse
When a design with complicated behaviour is hard to read, developers stop trusting their predictions of what a change will do. They copy code instead of reusing it. They avoid touching what works. And the system hits a ceiling on how rich its behaviour can become.

@words text="Supple design" sub="simple is not the same as easy"
Evans calls the alternative a supple design, one that invites change. He's careful about what that doesn't mean. A lot of over engineering has been excused as flexibility, and layers of abstraction usually get in the way. The designs that really help tend to be simple, which isn't the same as easy.

@chapter Encapsulation, lost
@art reading-internals
The first pattern starts from encapsulation. An object's value is that a client can use it without knowing the fine print of its calculation. If the interface doesn't tell the client what it needs, the client reads the internals anyway, and that value is gone.

@art crossed-purposes
Worse, a second developer who works out an operation's purpose from its code may land on one it serves only by accident. The code goes on working, and the two developers are now working against each other.

@chapter The pattern
@quote text="Name classes and operations to describe their effect and purpose, without reference to the means by which they do what they promise." cite="Evans, Domain-Driven Design, Chapter 10"
Here's the pattern's first sentence. Name classes and operations to describe their effect and purpose, without reference to the means by which they do what they promise.

@list heading="Names are the interface" items="Type names@Type names|Method names@method names|Argument names@argument names|In the Ubiquitous Language@Ubiquitous Language"
Type names, method names and argument names together make up the interface. Each one is a chance to say what the design intends, in the words of the Ubiquitous Language. Say what rule holds and what event happens, and leave how to the code.

@chapter A box office
@art seat-row
Here's a routine written for the lesson, from a theatre box office. It answers one question: can a party sit side by side in a row?

@code block=1 lines=1-15 focus="2@called scan|3@a run|5@zero"
It's called scan, and it takes row and k. Inside, it counts a run of entries equal to zero. What does that tell a client? Not much. It names what the code does to an array, not what the box office asks.

@code block=2 lines=1-15 focus="2@seat together|3@free in a row|5@that are free"
Now the same calculation as a method of SeatRow, named for the question a clerk would ask. Can seat together, given a party size. Inside, free in a row counts the seats that are free. Only the names have changed.

@chapter What the lab counts
@math heading="Minimum length: 5" items="scan:  row, k, run → mean 7/3 ≈ 2.33, all short@all three short;;SeatRow:  partySize, freeInARow → mean 19/2 = 9.50, none short@none short;;long-means:  mean 40/3 ≈ 13.33, none short@the longest"
The lab lists the declared names and marks those shorter than five characters. For scan it counts row, k and run, a mean length of seven thirds, about two point three three, all three short. For SeatRow, party size and free in a row, a mean of nine and a half, none short. A third version, long means, averages about thirteen point three three, the longest.

@art long-mechanism-names
But read that third one. Scan array for zero run, seat flags, current zero run. All long, and all about the mechanism: an array, zeros, a run. A client still has to know that a zero means a free seat. Length is what the lab can count. Whether a name states purpose is a reading against the domain.

@chapter Write the test first
@art test-first
Evans adds a working habit. Write a test of the behaviour before you write the behaviour, so you're forced to think as its client.

@code block=3 lines=1-4 focus="2@parse|3@party of three|4@party of four"
This one was written before the method. Parse a row: free, free, sold, free, free, free. It can seat a party of three together, and not a party of four. It reads the way the box office speaks.

@chapter Where people slip
@list heading="Common slips" items="Taking a long name for a revealing one@The first|Adding layers to make it supple@The second|Expecting a name to say everything@And the third"
The first slip is taking a long, descriptive name for an intention revealing one. The second is trying to make a design supple by adding layers of abstraction. And the third is expecting a good name to say everything. Evans says his own renamed method doesn't. What it changes, and what it guarantees, are the next two patterns.

@chapter Try it
@code block=4 lines=1-12 focus="2@called amt|3@base price|4-11@returns something"
Your turn. Here's a booking method called amt, taking d. It works out a base price and returns something. First, list the declared names the lab counts, and the ones it marks as short. Then cover the body, say in one sentence what the method promises, and give it a method name and an argument name that say so.

@end text="Name the purpose, not the means"
Paste your listing into the lab to check the first part, on Learn. That's learn dot get er done dot I O.
