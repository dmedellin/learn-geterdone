---
format: long
lesson: gof-structural/composite
title: Composite: ask a part and a whole the same question
thumb: One question, any size
---

@chapter Parts and wholes
@title text="Composite" sub="Design Patterns, chapter 4" art=thumb
A folder holds files and other folders. A menu holds items and other menus. Composite is how you build that kind of structure so your code never has to care which one it's holding.

@quote text="Composite lets clients treat individual objects and compositions of objects uniformly." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 4"
That's the second half of the intent. Composite lets clients treat individual objects and compositions of objects uniformly. The first half says what it builds: a tree of objects, standing for a part whole hierarchy.

@art grouped-shapes
The book's example is a drawing program. Users group simple shapes into larger ones, and group those again. With separate classes for shapes and containers, every piece of code must tell them apart, though the user hardly ever does.

@chapter One interface
@art tree-of-parts
So one abstract class stands for both. Simple shapes are leaves, and draw themselves. A picture is a composite: it draws by asking each child to draw. And a picture can hold pictures, so the tree nests as deep as you like.

@code block=1 lines=1-20 label=Java focus="2-4@one question|6-10@an emitter|12-19@a zone"
Here's the lesson's garden irrigation system. Every part answers one question: how many litres a minute. An emitter is a leaf, and returns its own flow. A zone is a composite. It holds parts, and adds up whatever each one answers.

@list heading="Four consequences" items="A composite fits where a part is expected@expects a simple object|Simpler clients@simpler|New kinds just work@new kinds|Too general@the liability"
Four consequences follow. Wherever the client expects a simple object, it can be given a composite. The client gets simpler, with no type tests. New kinds of leaf or composite work unchanged. And the liability: the design can get too general. The type system can't stop a composite holding the wrong kind of part, so that check moves to run time.

@chapter Safe or transparent
@art safe-vs-transparent
The authors dwell on one choice: where to declare add. Put it on the composite only, as the zone does, and that's safe. The compiler won't let you ask a leaf for a child. But leaves and composites no longer share one interface.

@code block=2 lines=1-7 label=Java focus="4-6@add on every"
Or declare add on every component. That's transparent: every node can be handled alike. The authors favour this, and suggest a default add should fail, by raising an exception, rather than quietly do nothing, because adding to a leaf probably means a bug.

@chapter Count it
@art request-down
Now the lab's garden. Ten nodes: six emitters and four zones, three levels deep. One request for the flow makes ten calls, one from the client and nine forwarded by the zones. One call per node.

@math heading="Adding up the garden" items="front: 2.5 + 4 = 6.5@front zone;;beds: 1.5 + 3.25 = 4.75@the beds;;back: 12.5 + 4.75 = 17.25@the back;;garden: 6.5 + 17.25 + 6 = 29.75@whole garden"
The front zone is two point five plus four, six point five. The beds are one point five plus three point two five, four point seven five. The back is twelve point five plus the beds, seventeen point two five. And the whole garden is six point five, plus seventeen point two five, plus six: twenty nine point seven five litres a minute.

@art add-up
Each zone's subtotal is computed once, by the zone, from its children's answers. And the client asked one question of one object.

@words text="Same calls · same total" sub="only when the mistake is caught differs"
Now ask an emitter to add a child. Under the safe declaration, the compiler refuses. Under the transparent one, it compiles, and the emitter must ignore it or fail at run time. The calls and the total are the same either way. The choice is about when a meaningless request is caught.

@chapter Where people slip
@list heading="Common slips" items="Thinking add changes the result@The first|Testing which kind of node@The second|Caching without invalidating@And the third"
The first slip is thinking the declaration of add changes what the tree computes. It doesn't. The second is letting the client test which kind of node it holds, the very code the pattern removes. And the third is caching a result in a composite without being told when something below it changes.

@art cache-invalidate
The authors allow that cache, a bounding box say, on one condition. A change below must invalidate the caches above, which is easiest when children know their parents.

@chapter Try it
@words text="A bakery's delivery" sub="crates hold bakes and other crates"
Your turn. A bakery's delivery is a crate holding a crate of breads, a crate of cakes, and some cookies. By hand, give the leaves, the composites, the depth, the calls one request makes, and the total weight.

@end text="Send one request down the tree"
Then type the records into the lab and check, on Learn. That's learn dot get er done dot I O.
