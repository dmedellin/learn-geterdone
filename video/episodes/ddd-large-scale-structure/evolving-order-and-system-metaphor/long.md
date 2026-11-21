---
format: long
lesson: ddd-large-scale-structure/evolving-order-and-system-metaphor
title: Evolving Order and System Metaphor: structure that grows with the system
thumb: Let the structure grow
---

@chapter Where does this class go?
@title text="Evolving Order and System Metaphor" sub="Domain-Driven Design, Chapter 16" art=thumb
Chapter sixteen opens on a team building a simulator of a satellite communications network. They'd broken a hard model into many sensible modules, and the modules multiplied until nobody could say where a new class belonged.

@art satellite-layers
Their way out wasn't another package. It was a story about the system as a whole: a stack of conceptual layers, from the physical links upward, refined while they refactored the code to fit it. What had been missing wasn't a class. It was a structure for the model as a whole.

@chapter Seeing the whole
@words text="A language for broad strokes"
Modules, Bounded Contexts and distillation all help, but none shows the whole. Without shared rules, people solve the same problem in different ways, and lose sight of how the parts fit. A large scale structure is a language for discussing the system in broad strokes, so anyone can say what a part is for without reading its details.

@art small-team-modules
It usually spans several contexts, and mostly isn't drawn in UML. It explains the model rather than appearing in it. And a small team with a modest model may need nothing more than well named modules, some distillation and informal coordination.

@chapter Evolving Order
@art free-for-all-straitjacket
Evans sets two failures against each other. A design free for all gives a system no one can understand as a whole. An architecture imposed up front freezes decisions made before the domain was understood. As requirements change, developers simplify the application to fit it, or route around it until there's no structure at all.

@quote text="The problem is not the existence of guiding rules, but rather the rigidity and source of those rules." cite="Evans, Domain-Driven Design, Chapter 16"
The problem is not the existence of guiding rules, but rather the rigidity and source of those rules. So keep guiding rules, but let them grow from the application and change with it, perhaps into a different kind of structure altogether.

@words text="A poor fit is worse than none" sub="Context Map: required · structure: optional"
A structure that fits rules out many options at once, and helps people reach consistent answers. But a Context Map is always needed, and a large scale structure isn't. Because a structure that fits badly is worse than none, aim a minimal set at the problems that have actually appeared.

@chapter System Metaphor
@art firewall
System Metaphor comes from Extreme Programming. Ward Cunningham's firewall made it click for Evans. The picture made a whole product category easy to grasp, yet it cut both ways. It suggested a barrier at the edge, so it said nothing about threats from inside.

@art metaphor-misleads
A metaphor is a loose structure, and models in several contexts can map to it approximately. The risk is that a persuasive analogy carries in features the problem doesn't have. Few projects find a really useful one. So take one up only when it's compelling, keep it under review, and drop it once it misleads.

@chapter A bike share, packaged twice
@list heading="Two packagings" items="By screen: rent · return · admin@one package for each screen|Grown: fleet · riding · pricing@grew"
Now the count. Eight elements of a bike share, packaged twice. The first was fixed before the domain was understood, one package for each screen of the app. The second grew as the team learned which things change together: fleet, riding and pricing.

@math heading="screens-against-grown" items="by screen:  2 + 2 + 2 + 2 = 8 touches · 0 confined@by screen;;grown:  1 + 1 + 1 + 2 = 5 touches · 3 confined@grown packaging"
Four changes arrive: a weekend tariff, a dock sensor, a family plan, and a ride time cap. By screen, every one reaches two modules, eight touches, none confined. Under the grown packaging, three stay in one module, and the ride time cap reaches two. Five touches.

@math heading="a-change-neither-fits" items="rebalancing-credit:  3 modules under both@rebalancing credit;;totals: 11 against 8@eleven against eight"
Then a fifth change: a rebalancing credit, paying riders who return a bike to an emptying station. It reaches three modules under both packagings, so the totals become eleven against eight. The grown structure was found from the first four changes, and doesn't help with a kind it never saw.

@art structure-rereads
That's the case Evolving Order is written for. The structure is a current best reading of the domain, and a new kind of requirement is a reason to look at it again.

@chapter Where people slip
@list heading="Common slips" items="No structure until late@The first|A metaphor because every project needs one@The second|Fewer touches as proof@And the third"
The first slip is thinking Evolving Order means no structure until late. Start early with something loose, and change it. The second is adopting a System Metaphor because every project should have one. And the third is reading a lower touch count as proof one packaging is better.

@chapter Try it
@words text="A seed bank: by department, then as learned" sub="retest-interval · member-quota · packet-size"
Your turn. A seed bank, packaged by department up front, and then as the team learned. Three changes. Find the modules each touches under each packaging, the total touches, and the changes confined to one module. Then say what the department packaging assumed about how the seed bank would change.

@end text="Let the structure grow"
Type the model into the lab to check, on Learn. That's learn dot get er done dot I O.
