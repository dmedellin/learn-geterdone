---
format: long
lesson: enterprise-patterns-concurrency-and-session-state/the-value-of-statelessness
title: The value of statelessness: a hundred users, ten objects
thumb: Idle users are the saving
---

@chapter The field
@title text="The Value of Statelessness" sub="Patterns of Enterprise Application Architecture, Chapter 6" art=thumb
You may have written a handler that keeps something in a field between calls. The last few pages a user viewed. A half filled form. A cart. It works, until there are two servers, or a thousand users.

@quote text="The shift from stateless to stateful is much more than three or four letters at the end of the word." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 6"
Chapter six, Session State, opens with this line. The shift from stateless to stateful is much more than three or four letters at the end of the word.

@chapter What stateless means
@art field-between-calls
A stateless server isn't an object with no fields. Those are rare, and arguably bad design. It's an object that keeps no state between requests. It may fill its fields while building one page, and then the values are useless. Make it remember every product a client has viewed, and it's stateful.

@chapter The thought experiment
@art stateful-pinned
Fowler makes the case with a thought experiment he calls completely unrealistic, but helpful. A hundred people want to know about books. A request takes one second. Each person sends one request every ten seconds, perfectly balanced. With a stateful object per user, you need a hundred objects.

@math heading="hundred-users" items="stateful objects: 100@a hundred;;stateless busy: 100 × 1,000 / 10,000 = 10@ten;;idle share: 1 − 1,000 / 10,000 = 9/10 = 90%@ninety percent;;users per stateless object: 10,000 / 1,000 = 10@each stateless object serves"
In the lab's milliseconds: stateful objects, a hundred. Stateless objects busy on average, a hundred times a thousand over ten thousand, which is ten. A stateful object sits idle ninety percent of the time. And each stateless object serves ten users.

@art idle-grid
That's what many people mean when they call stateful servers a disaster. The main issue, Fowler says, is resources. Each stateful object waits, holding one user's data, while that user thinks. With stateless objects, ten can do all the work, busy all the time.

@art pooled-objects
Without state between calls, it doesn't matter which object serves a request, so they can be pooled. The more idle users, the more statelessness is worth. And it fits the web, whose protocol is stateless.

@chapter When users wait less
@math heading="busier: every 2,000 ms" items="stateful objects: 100@stays at a hundred;;stateless busy: 50@fifty;;idle share: 1/2 = 50%@half;;users per stateless object: 2@two users"
Now make the same users ask every two thousand milliseconds. The stateful count stays at a hundred. But now fifty stateless objects are busy, a stateful one is idle half the time, and each stateless object serves two users.

@art peak-bunching
The saving is the idle time, so when users wait less, it shrinks. And the experiment assumes perfectly balanced requests. Real ones bunch. The stateless figure is an average, so a pool sized to it is too small at a peak.

@chapter Stateful by nature
@words text="Browse: stateless · Buy: stateful"
So should everything be stateless? Where it can be. But many interactions are stateful by nature. A cart has to be remembered for the whole session. A visitor who only browses has a stateless session. One who buys has a stateful one. The only way to avoid it, Fowler remarks, is to stay poor.

@code block=1 lines=1-16 label=Java focus="4@store|11@loads the cart|13@saves the cart"
The good news is that a stateless server can carry a stateful session. This handler has one field, store, set when it's built. Each call loads the cart its id names, adds the item, saves the cart, and returns a summary. Between calls it holds no cart, so any handler in a pool can take the next request.

@art cart-in-store
The session's state hasn't gone. The cart is the same size whether the handler is stateful or not. Statelessness moves the state out of the server object, to the client or the database, and that move has its own cost, which the next lesson counts.

@chapter Where people slip
@list heading="Common slips" items="Stateless means no state@The first|Stateful is always worse@The second|Stateless means no fields@And the third"
The first slip is thinking stateless means the application keeps no state. The cart still lives somewhere. The second is thinking stateful is always worse. The saving depends on idle time. And the third is thinking a stateless object has no fields. It just can't rely on them for the next request.

@chapter Try it
@words text="250 users · 400 ms · every 20,000 ms"
Your turn. Two hundred and fifty users. A request takes four hundred milliseconds. Each user sends one every twenty seconds, that's twenty thousand milliseconds. Work out the stateful objects, the stateless objects busy on average, the idle share, and the users each stateless object serves.

@end text="Change the idle time yourself"
You can change the users and their idle time and watch the saving move, on Learn. That's learn dot get er done dot I O.
