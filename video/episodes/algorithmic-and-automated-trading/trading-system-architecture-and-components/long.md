---
format: long
lesson: algorithmic-and-automated-trading/trading-system-architecture-and-components
title: Trading system architecture: containing the failure you didn't expect
thumb: One owner, contained failure
---

@chapter The problem
@title text="Trading System Architecture and Components" sub="Algorithmic and Automated Trading" art=thumb
Here's an uncomfortable fact from the lesson. The market can move correctly while the system fails internally. Your strategy can be right about the price, and the account can still end up holding something nobody intended.

@art spreading-failure
That's why architecture matters. It should contain failures, so a delayed data feed, a broken strategy, or a broker outage doesn't silently create an unintended position.

@chapter Three ideas
@list heading="What to understand" items="Component boundary@component boundary|State ownership@state ownership|Failure containment@failure containment"
The lesson names three ideas. A component boundary: market data, strategy, risk, orders and monitoring should each expose clear inputs and outputs. State ownership: each position, order and strategy state should have one authoritative owner. And failure containment: a component failure should stop or degrade the affected path without corrupting the whole system.

@art components-boxes
Picture the pieces as boxes with clear wires between them. Data in, signal out. Signal in, risk decision out. Each box can be tested on its own, and each wire carries a defined message.

@chapter One owner per state
@art single-owner
Why one owner for order state? To prevent conflicting updates. If two components can both write an order's status, you can end up with contradictory quantities, statuses, or cancellation decisions. One owner means every answer lands in one place.

@words text="Persist decisions before relying on messages"
And that owner keeps a durable record. Using in memory state as the only order record is a named mistake: restart the process and the record is gone. Persist decisions before depending on transient messages.

@chapter Design from events and state
@list heading="Design from events and state" items="Map events, signals, decisions, orders, fills, positions@Map|Assign each transition one owner and one record@Assign|Contain each dependency failure@Contain"
The lesson says to begin with the decisions and records you need, not with deployment technology. Map: list the market events, signals, risk decisions, orders, fills and positions. Assign: give each state transition one owner and one durable record. Contain: define timeouts, circuit breakers and safe behaviour for each dependency failure.

@art modular-vs-monolith
Is more services always better? No. A modular architecture is useful when it creates clear boundaries and contains failures. Service count is a cost, not a benefit. Splitting services without defining ownership just creates more places for state to disagree. And boundaries don't remove the need for testing.

@chapter When the broker goes quiet
@art safe-state
So what should a broker outage do? Enter a defined safe state. Not unlimited retries, which is how you get duplicate orders once the broker answers. And not estimated fills without confirmation, which create a position the system believes in but the broker may not hold.

@words text="A timeout is not proof the order failed"
The lesson adds a subtle point here. Treating a network timeout as proof that an order failed is a mistake. A timeout means you don't know. Unknown execution state needs controlled reconciliation, not an optimistic assumption either way.

@chapter Adding up latency
@math heading="Internal hops 112 ms · broker 160 ms slower" items="112 + 160 = 272 ms end to end@two hundred and seventy two;;only the order service is degraded@only the order service"
Here's the lesson's latency question. A modular system has one hundred and twelve milliseconds of internal hops, and during a timeout the broker takes one hundred and sixty milliseconds longer to answer. End to end, that's two hundred and seventy two milliseconds. And only the order service is degraded.

@art contained-failure
That's what modularity buys you. It doesn't make the broker answer faster. The order path still waits the full delay. What it decides is who else is stuck while it waits. The feed, strategy and risk stages keep their own state and keep working.

@chapter Where people slip
@list heading="Common mistakes" items="Splitting services without ownership@The first|In-memory state as the only order record@The second|A timeout treated as a failed order@And the third"
The first mistake is splitting services without defining ownership. The second is using in memory state as the only order record. And the third is treating a network timeout as proof that an order failed. Design a safe degraded state for every external dependency.

@chapter Try it
@words text="Monolith vs modules · inject one failure"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, compare a monolith with modular services, inject one component failure, and inspect the latency and how far the failure spreads.

@end text="Break one component, see what survives"
You can inject a failure and watch it spread or stay contained, on Learn. That's learn dot get er done dot I O.
