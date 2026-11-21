---
format: long
lesson: code-complete-high-quality-code/design-challenges-and-complexity
title: Why software design is hard, and the one job it has
thumb: Manage the complexity
---

@chapter The question
@title text="Design Challenges and Complexity" sub="Code Complete, chapter 5" art=thumb
Why is designing software so hard? Chapter five opens with an honest answer, and then with the idea that the whole of this course is built on.

@quote text="Software’s Primary Technical Imperative is managing complexity. This is greatly aided by a design focus on simplicity." cite="McConnell, Code Complete, 2nd ed., Chapter 5, p. 123"
Here it is. Software's primary technical imperative is managing complexity. This is greatly aided by a design focus on simplicity.

@chapter A wicked problem
@art tacoma-bridge
Design, McConnell says, is a wicked problem. One you can define clearly only by solving it, or part of it. His example is the first Tacoma Narrows bridge. Strong enough for its load, and shaken apart by the wind in nineteen forty, because nobody knew aerodynamics mattered that much until the bridge showed them.

@list heading="Design is" items="Sloppy@sloppy|About trade-offs and restrictions@trade offs|Nondeterministic@nondeterministic|Heuristic@heuristics|Emergent@emergent"
The rest follows. Design is sloppy, full of false steps, even when the result is tidy. It's about trade offs and restrictions. It's nondeterministic: three people can come back with three acceptable designs. Its techniques are heuristics. And it's emergent, evolving as you write and revise the code.

@chapter Essential and accidental
@art essential-accidental
Where does the difficulty come from? Fred Brooks split it into two kinds. Accidental difficulty came from the tools, like assembly language and batch computers, and was largely dealt with decades ago. Essential difficulty is the problem itself, an intricate set of concepts that must be exactly right.

@art skull-capacity
The root of both is complexity. Citing Dijkstra, the chapter says no one's skull is big enough to hold a modern program. So a design should let you focus safely on one part at a time.

@list heading="Two prongs" items="Minimise the essential complexity at any one time@keep the essential|Keep accidental complexity from spreading@keep accidental"
That gives two prongs. First, keep the essential complexity anyone must deal with at one time to a minimum. Second, keep accidental complexity from spreading.

@chapter Hoses between modules
@art hoses
Now picture six subsystems, each talking to every other. McConnell's image: think of every line between them as a hose with water in it, and imagine how wet you get pulling one out to use elsewhere. Allow communication on a need to know basis, and keep the diagram free of cycles.

@list heading="Three counts" items="Loose coupling@loose coupling|High fan-in@High fan in|Low to medium fan-out@fan out"
Three of the chapter's desirable characteristics are counts. Loose coupling. High fan in, meaning many classes use a given utility. And low to medium fan out, meaning a class uses only a few others.

@chapter Count a design
@art everything-talks
The lesson's lab counts these for five modules: user interface, orders, billing, stock and database. In the first design, every module uses every other.

@math heading="Everything talks" items="pairs = 5 × 4 ÷ 2 = 10@five times four;;uses = 20@twenty uses;;connected = 10 of 10 = 100%@all ten;;largest fan-in = 4 (all five tie)@all five tie"
With five modules, the possible pairs are five times four over two, which is ten. There are twenty uses, and all ten pairs are connected, a hundred percent. And the largest fan in is four, because all five tie at four. That's the hoses picture in miniature.

@art layered-modules
Now redraw it in layers. The user interface uses orders and billing. Each of those uses stock and the database. And stock uses the database.

@math heading="Layered" items="uses = 7@seven uses;;connected = 7 of 10 = 70%@seventy percent;;largest fan-in: db, 3@the database;;strict layers: 5 uses · 50% · db, 2@strict layers"
That's seven uses, touching seven of the ten pairs, seventy percent. The largest fan in is the database, three. And in strict layers, where each module talks to fewer below it, it's five uses, half the pairs, and the database's fan in falls to two.

@words text="A count is a reason to look"
A high fan in at the bottom is what the chapter hopes for: one utility many modules use. The counts don't prove a design is good. They show where a change could travel, and which module everything leans on.

@chapter Where people slip
@list heading="Common slips" items="Thinking design ends when coding begins@The first|Taking fewer connections for a better design@The second|Expecting design to remove all complexity@the third"
The first slip is thinking design is a phase that ends when coding begins. Much of it happens during construction. The second is taking fewer connections for a better design. The chapter asks for loose coupling, not the fewest lines. And the third is expecting design to remove complexity. Some of it belongs to the problem.

@chapter Try it
@words text="6 modules, two designs" sub="ui · api · orders · billing · stock · db"
Your turn. Take six modules. First, every module uses every other. Then a layered version with six dependencies. For each, find the possible pairs, the uses, the share connected and the largest fan in, and say in one sentence what the layering changed.

@end text="Count your own design"
You can paste a design's dependencies into the lab and count them, on Learn. That's learn dot get er done dot I O.
