---
format: long
lesson: gof-behavioral-objects/state
title: State: when an object seems to change its class
thumb: A class for every state
---

@chapter Same call, different behaviour
@title text="State" sub="Design Patterns, chapter 5" art=thumb
If you've ever written the same switch on a status field in method after method, this is the pattern for you. By the end, you'll trace a state machine by hand and count what each way of writing it needs.

@quote text="Allow an object to alter its behavior when its internal state changes. The object will appear to change its class." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 5"
That's the intent. Allow an object to alter its behavior when its internal state changes. The object will appear to change its class. It's also called Objects for States.

@art switch-tangle
The second sentence is the striking one. A client calls the same operation on the same object, and gets different behaviour, as if the object had been replaced. Reach for it when what an object does turns on a status it carries, tested by switch after switch through its methods.

@chapter Objects for states
@art connection-states
The book's example is a network connection, which answers open or close differently when it's established, listening or closed. An abstract state class declares the requests. One subclass per state implements them. The connection keeps the current one, forwards every request to it, and swaps it when the state changes.

@code block=1 lines=1-19 label=Java focus="1-5@return the state unchanged|6-8@the shelf|9-12@on loan|14-19@the copy"
Here's the lesson's library copy. The interface's default methods return the state unchanged, which is how an ignored event looks. On the shelf, lend leads to on loan. On loan, a return goes back to the shelf, and falling due leads to overdue. And the copy itself only rebinds one field.

@words text="Enums: one shared instance each"
Each state is a Java enum, so each is a single shared instance, like the book's singletons. And the method is called give back, because return is a Java keyword.

@chapter Three consequences
@list heading="Consequences" items="Localizes state behaviour@localizes|Explicit, atomic transitions@explicit|Shareable state objects@shared"
The consequences are three. State localizes what each state does, so a new state is a new subclass, not edits to several conditionals. The cost: more classes, less compact. Transitions become explicit, and atomic: one variable rebound. And state objects with no fields can be shared.

@art shared-states
That last one is neat. A state object with no fields of its own can be shared among many contexts. In the book's terms it's a flyweight, with behaviour and no intrinsic state.

@art rebind
Who chooses the next state? The pattern leaves it open. Fixed rules can live in the context. Letting the states name their successors is usually easier to extend, at the price that each state class knows at least one other.

@words text="State models behaviour · a table models transitions"
There's also a table driven alternative, from Cargill, mapping each state and input to the next state. It's regular and easy to edit as data, but awkward when a transition must do something.

@chapter Trace it
@art state-machine
In the lab, the copy has five states: shelf, on loan, held, overdue and lost. Seven events, nine transitions. It starts on the shelf, and ten events come in.

@math heading="Ten events from the shelf" items="return at shelf: ignored@a return;;lend → on loan · renew → on loan@lend;;due → overdue · renew at overdue: ignored@falls due;;return → shelf · hold → held@back to the shelf;;lend → on loan · due → overdue · write off → lost@written off"
A return while it's on the shelf is ignored. Then lend, so it's on loan, and a renewal keeps it there. It falls due, and a renewal while overdue is ignored. It comes back to the shelf, is put on hold, lent again, falls due again, and is finally written off. Lost.

@math heading="Two ways to write it" items="one conditional: 9 + 5 = 14 branches@fourteen branches;;State: 5 + 2 = 7 classes@seven classes"
Now count the code. One conditional needs a branch for each of the nine transitions, and a default for each of the five states: fourteen branches. State needs one class per state, plus the context and the abstract state: seven classes.

@art new-state
Add a repair state, with damage and fix events. The conditional grows to eighteen branches, each a case added to code that already worked. State grows to eight classes, one of them new. Whether eight small classes beat one eighteen branch method is the book's judgement about many states, not the count's.

@chapter Where people slip
@list heading="Common slips" items="Expecting smaller code@The first|Keeping state as flags@The second|Thinking the context decides every transition@And the third"
The first slip is expecting State to make the code smaller. The book says the opposite. The second is keeping state as flags and assignments, so the object is briefly half in one state and half in another. And the third is assuming the context must decide every transition.

@chapter Try it
@words text="An audio guide handset" sub="docked · ready · playing · paused"
Your turn. A museum audio guide's handset starts docked. Trace play, lift, play, pause, pause, play, dock, lift. Give the final state and the events ignored, then count the branches and the classes.

@end text="Trace the machine"
Then enter the machine into the lab and check, on Learn. That's learn dot get er done dot I O.
