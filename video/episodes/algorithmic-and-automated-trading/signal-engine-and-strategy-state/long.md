---
format: long
lesson: algorithmic-and-automated-trading/signal-engine-and-strategy-state
title: Why your trading bot buys twelve times: signals as state transitions
thumb: Enter once, not every bar
---

@chapter The problem
@title text="Signal Engine and Strategy State" sub="Algorithmic and Automated Trading" art=thumb
Price breaks out, and buyers keep accepting higher prices. Your entry condition is true on this event, and the next, and the next. If the engine fires an entry every time the condition is true, it keeps buying the same position over and over.

@art condition-stays-true
The lesson's point is that a market condition can stay true for many events, but the strategy shouldn't keep opening the same position. The engine has to tell the difference between entering a bullish state and simply remaining in one.

@words text="Entering bullish ≠ remaining bullish"
That distinction is the whole job of the signal engine. It turns a stream of normalized events into a small number of decisions, each one a change of state, each one deterministic, and each one recorded with the event that caused it.

@chapter Three ideas
@list heading="What to understand" items="State machine@state machine|Transition signal@transition signal|Determinism@determinism"
Three ideas. A state machine: represent flat, candidate, active, exit pending and cooldown as explicit states. A transition signal: emit a decision when the state changes, not on every event where a condition is still true. And determinism: the same ordered inputs and the same prior state must always produce the same next state.

@art state-machine
Picture the states as circles joined by arrows. The strategy is always in exactly one of them. An event can move it along an arrow, or leave it where it is. A signal is the crossing of an arrow, not the act of standing still.

@chapter Twelve true events
@math heading="Entry condition true on 12 consecutive events" items="stateless, confirmation 1: 12 entries@twelve entries;;11 of them duplicates@eleven of them;;stateful: 1 transition into LONG@one transition"
Here's the lesson's example. The entry condition is true on twelve consecutive events. A stateless engine, with confirmation of one, has nothing to consult. Each event satisfies the condition, so it emits twelve entries, eleven of them duplicates. A stateful engine makes one transition into long, and then nothing.

@art twelve-vs-one
Because a condition that stays true isn't a new event. After the first transition, the other eleven are observations of a state the strategy is already in. That's why a true condition can produce no new signal at all.

@chapter Cooldown
@art cooldown
What about after an exit? A cooldown state stops rapid re entry. It enforces a defined period before the same setup can trigger again. It can't prevent a price gap, and it doesn't touch normalization. It only governs the engine's own transitions.

@chapter One event at a time
@list heading="Process one event at a time" items="Evaluate conditions from data and state@Evaluate|Transition once, with a reason code@Transition|Persist state before publishing@Persist"
The lesson's method processes one event at a time, and every transition references the triggering event and the previous state. Evaluate: calculate conditions from normalized data and the current state. Transition: apply one valid state transition, with a reason code. Persist: store the new state before publishing the resulting signal.

@art persist-then-publish
Why persist first? Because recovery must know whether the transition already happened. If the engine publishes, then crashes before saving, it restarts thinking it's still flat, and it can repeat the decision. Keeping state only in process memory is a named mistake for exactly this reason.

@words text="Stale or out-of-order: a fixed policy"
And late events need a rule too. Reject stale or out of order events according to a fixed policy. Otherwise a late event can silently reverse the current state, and nothing records why.

@chapter Where people slip
@list heading="Common mistakes" items="An entry on every qualifying bar@The first|State kept only in process memory@The second|Late events silently reversing state@And the third"
The first mistake is emitting an entry on every qualifying bar. The second is keeping state only in process memory. And the third is allowing late events to reverse the current state silently. Model the states explicitly, and attach event identifiers and reason codes to every transition.

@art reason-codes
Those reason codes pay off later. When you replay the same ordered events from the same starting state, you should get the same transitions, for the same reasons. That's what determinism means in practice.

@chapter Try it
@words text="Stateful · confirmation · cooldown · stale events"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, toggle stateful processing, confirmation, cooldown and stale event handling. Count the duplicate and contradictory signals each time.

@end text="Turn state on, watch duplicates vanish"
You can toggle state and cooldown and count the duplicates, on Learn. That's learn dot get er done dot I O.
