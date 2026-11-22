---
format: long
lesson: algorithmic-and-automated-trading/reliability-idempotency-retries-and-recovery
title: Idempotency and retries: how one order becomes four
thumb: Retry the request, not the trade
---

@chapter The problem
@title text="Reliability, Idempotency, Retries, and Recovery" sub="Algorithmic and Automated Trading" art=thumb
Your system sends an order, and the network times out. The obvious move is to try again. And again. The trouble is, the first one may already have reached the broker.

@art lost-response
The lesson's principle is that retries must repeat the request safely, without repeating the economic action. The market keeps moving while a service times out. Recovery has to find out the actual order state before deciding whether another action is allowed.

@words text="Repeat the request, not the economic action"
So the question is never just, did my call fail? It's, what does the broker hold right now, and what did I mean to happen? Only the second pair of answers tells you whether to send anything again.

@chapter Three ideas
@list heading="What to understand" items="Idempotency@Idempotency|Bounded retry@Bounded retry|Reconciliation@Reconciliation"
Three ideas. Idempotency: processing the same command more than once produces one intended economic result. Bounded retry: retry only eligible failures, with backoff, limits, and the same command identity. Reconciliation: compare internal state with broker state, and repair differences through controlled rules.

@art idempotency-key
Idempotency is the key one. A retry should reuse the same idempotency key. Not a different symbol, which is a different trade. Not a new strategy version, which is a different command. The stable identity is what lets duplicate attempts resolve to a single action.

@chapter One intent, four orders
@math heading="Timeout after send · 3 retries · each with a new client order ID" items="1 original that arrived@one original;;+ 3 retries with fresh IDs@three retries;;= up to 4 orders@up to four"
Here's the lesson's worked question. The submit times out after the send. The client retries three times, each time with a new client order ID. How many orders can the broker hold for that one intent? One original, plus three retries with fresh identities, gives up to four orders.

@art four-orders
Not one. A timeout after the send means the response was lost, not the request. The first attempt very likely reached the broker. And not three, because the original counts too. Four orders, three of them duplicates the broker can't tell apart. With the same key on every attempt, the broker recognises one intent and holds one.

@chapter Bounded retries
@art bounded-retry
Unlimited retries are their own problem. They create repeated load and uncontrolled actions. Retries don't make a dependency available. They queue demand against it, and without a key, they multiply its effects. So retries must be bounded, spaced out with backoff, and aware of side effects.

@words text="An HTTP error isn't a broker rejection"
And be careful what a failure means. Treating HTTP errors as a definitive broker rejection is a named mistake. Don't infer execution state from a failed network call alone.

@chapter Recover from durable facts
@list heading="Recover from durable facts" items="Persist identity and intent first@Persist|Attempt with bounded retry and the same key@Attempt|Reconcile against the broker@Reconcile"
The lesson's method has three steps. Persist: store the command identity and intent before any external side effect. Attempt: use bounded retry with the same idempotency key. Reconcile: query the authoritative external state after any uncertainty or restart.

@art crash-recovery
After a crash, recovery begins from durable internal records and broker reconciliation. Not the last screen displayed, which was a rendering of memory that's now gone. And never a new order, which is exactly how a duplicate gets made. Recovery first establishes what already exists.

@art reconcile-broker
Persistent facts reveal which transitions may be incomplete. Restarting without checking the open orders at the broker is the third of the lesson's named mistakes.

@chapter Where people slip
@list heading="Common mistakes" items="A new order ID on every retry@The first|HTTP errors as definitive rejections@The second|Restarting without checking open orders@And the third"
The first mistake is creating a new order ID on every retry. The second is treating HTTP errors as definitive broker rejections. And the third is restarting without checking open external orders. Use stable command and client order IDs, persist before calling anything external, and reconcile after a timeout, a restart or a status conflict.

@chapter Try it
@words text="Timeouts · duplicates · crashes · delayed updates"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, inject timeouts, duplicate events, crashes and delayed broker updates. Then toggle idempotency and reconciliation, and count how many orders end up at the broker.

@end text="Crash it, then recover"
You can inject timeouts and crashes and watch the orders multiply, on Learn. That's learn dot get er done dot I O.
