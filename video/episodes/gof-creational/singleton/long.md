---
format: long
lesson: gof-creational/singleton
title: Singleton: one instance, one point of access, and its costs
thumb: Exactly one, made on first use
---

@chapter Only one
@title text="Singleton" sub="Design Patterns, Chapter 3" art=thumb
Some things a system should have only one of. One printer spooler, however many printers. One file system. One window manager. Singleton is the last creational pattern, and the most argued over since.

@quote text="Ensure a class only has one instance, and provide a global point of access to it." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 3"
Here's its intent. Ensure a class only has one instance, and provide a global point of access to it.

@art global-vs-singleton
A global variable makes an object easy to reach, but does nothing to stop a second one being made. So the authors make the class itself responsible. It keeps track of its sole instance, intercepts requests to create new ones, and offers a way to get the one it has.

@chapter The class
@code block=1 lines=2-14 focus="3@no instance until|5-7@no client can call new|9-14@on first use"
There's one participant, the singleton class, with a static instance operation. Here's the lesson's locker registry. It holds no instance until one is asked for. Its constructor is private, so no client can call new. And the instance operation creates it on first use, and hands back the same one every time after. It's synchronized, so threads can share it safely.

@list heading="Five benefits" items="Controlled access@controlled|A reduced name space@name space|Refinement by subclassing@subclassing|A variable number of instances@variable number|More flexible than class operations@class operations"
The authors list five benefits. Access to the sole instance is controlled. The name space is reduced, compared with globals. Operations can be refined by subclassing. A variable number of instances is easy, since only the access operation changes. And it's more flexible than class operations, which in C plus plus can't be overridden.

@chapter The costs
@list heading="Why not a static object?" items="Nothing stops a second one@a second one|Values may not be known yet@may not be known|No defined order across files@no order|Made whether used or not@whether it's used"
The costs are in the implementation section. Why not just a C plus plus global or static object? Nothing stops a second one being declared. The values it needs may not be known yet. C plus plus fixes no order of initialisation across files. And every singleton is made whether it's used or not.

@art registry-of-singletons
Subclassing is harder still. Choosing the subclass with conditionals in the access operation hard wires the list. A registry, where each singleton registers itself by name, frees the access operation from knowing the subclasses, but only if every candidate is created so it can register.

@art hidden-dependency
And there's a later view the book doesn't cover. A singleton reached through a static operation is global state under another name. Every class that calls it depends on it without saying so, and a test can't easily swap in a different instance. So many designs now create the one instance at start up, and pass it to whoever needs it.

@words text="Read both · weigh them against your design"
The authors' text meets part of this, with the registry and the variable number of instances. It doesn't discuss testing. Read both, and weigh them against the design in front of you.

@chapter A locker network
@art locker-requests
Now the lab, on a parcel locker network. Its registry of locker banks costs fifty to load, and its audit log costs twenty to open. Five requests reach the registry in turn: a kiosk, the app, a courier, the kiosk again and a night job. None reaches the log.

@math heading="Three schemes" items="fresh: 5 instances · 5 × 50 = 250@five times fifty;;lazy: 1 instance · 50 · first request pays 50@made on first use;;eager: 2 instances · 50 + 20 = 70 at start@before any request"
If every request constructs its own registry, that's five instances, five times fifty, two hundred and fifty. With one made on first use, the other four reuse it: one instance, a cost of fifty, and the first request pays it. Eager makes both objects before any request: two instances, seventy paid at the start.

@art many-fresh
The difference between fresh and lazy is the whole pattern: five objects, each paying the load, or one object that five clients share.

@art lazy-vs-eager
And the difference between lazy and eager is when the one object is made.

@words text="eager 70 · lazy 50 · fresh 250" sub="eager makes a log nobody asks for"
Side by side: eager seventy, lazy fifty, fresh two hundred and fifty. Eager and lazy both keep one registry. They differ on the log, made under eager though nobody asks for it, and on who pays: the program at start up, or the first request.

@chapter Where people slip
@list heading="Common slips" items="A global variable as a singleton@The first|Every singleton at start-up@The second|Conditionals in the access operation@And the third"
The first slip is treating a global variable as a singleton. The second is creating every singleton at start up, made whether used or not. And the third is choosing the subclass with conditionals in the access operation, which must then be edited for every new subclass.

@chapter Try it
@words text="A thermostat app" sub="settings: 12 · sensor-bus: 40 · six requests"
Your turn. A thermostat app has two shared objects: settings, which costs twelve to load, and a sensor bus, which costs forty to open. Six requests come in. Count the instances and the total cost when every request makes a new object, and when each is a singleton made on first use.

@end text="Count instances and cost"
Then check both schemes in the lab, on Learn. That's learn dot get er done dot I O.
