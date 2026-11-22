---
format: long
lesson: algorithmic-and-automated-trading/broker-apis-and-order-lifecycle
title: Broker APIs: why submitting an order isn't getting a fill
thumb: Submitted is not filled
---

@chapter The problem
@title text="Broker APIs and Order Lifecycle" sub="Algorithmic and Automated Trading" art=thumb
Your code sends a buy order to the broker, and gets back a success response. So you mark the position as bought. That's one of the most common mistakes in automated trading, and the lesson names it directly.

@words text="Submitting is not filling"
Submitting an order is not the same as receiving a fill. When buyers move price up quickly, a buy limit may sit unfilled, while a market order can execute at a worse price than the last value on the chart. Marking an order filled after an HTTP success response is a named mistake.

@chapter Three ideas
@list heading="What to understand" items="Client order ID@client order ID|Order lifecycle@order lifecycle|Unknown state@unknown state"
Three ideas. A client order ID: a stable identifier you generate before submission, and reuse for reconciliation. The order lifecycle: created, submitted, accepted, partially filled, filled, cancelled, expired, or rejected. And unknown state: a timeout means the result is unknown until you query the broker or an update arrives.

@art lifecycle-states
Picture the lifecycle as a path of states, with branches. An order moves from created to submitted to accepted. From there it can fill, fill in part, be cancelled, expire, or be rejected. Your system has to follow whichever path the broker reports, not the one it hoped for.

@chapter Timeouts
@art timeout-unknown
What does a request timeout prove? Only that the broker didn't respond in time. Not that the order failed, and not that it filled. The broker may have accepted the request before the response was lost. So a timeout is unknown state, and you treat it that way.

@art client-order-id
That's where the client order ID earns its keep. It correlates retries with broker state. If you resend, you resend with the same ID, so the broker can tell it's the same order. Generating a new ID for every retry is a named mistake, because it turns one intended order into two real ones.

@chapter Asynchronous by default
@list heading="Treat broker communication as asynchronous" items="Identify: create the ID, persist the intent@Identify|Submit: send once, record broker ID and response@Submit|Reconcile: consume updates, query on disagreement@Reconcile"
State changes can arrive later, partially, or more than once. So the lesson's method has three steps. Identify: create a client order ID and persist the intent. Submit: send once, then record the broker ID and the response. Reconcile: consume updates, and query the broker whenever local and external state disagree.

@art async-updates
The order matters. Persist the intent before the network call, so that if anything fails mid flight, you know what you meant to do and which ID to look for.

@chapter Partial fills
@math heading="100-share buy limit at $108.53 · 55 shares filled" items="position: 55 shares@position;;still open: 100 − 55 = 45 shares@still open;;cash: 55 × the fill price, spent now@cash"
Here's the lesson's example. A hundred share buy limit at one hundred and eight fifty three is working, and the stream reports fifty five shares filled. Three things change at once. The position is now fifty five shares. A hundred minus fifty five leaves forty five still open. And cash for those fifty five shares is spent now.

@art partial-fill
Not nothing until the order completes. The fifty five shares are owned the moment the fill arrives, and the rest may never fill if price doesn't come back. And not the whole hundred, because forty five are still working at the broker. The risk engine sizing the next order reads all three numbers.

@chapter Where people slip
@list heading="Common mistakes" items="Marking filled after an HTTP success@The first|A new ID for every retry@The second|Ignoring partial fills and cancel races@And the third"
The first mistake is marking an order filled after an HTTP success response. The second is generating a new ID for every retry. And the third is ignoring partial fills and cancel races, where a cancel and a fill cross in flight and both seem to have happened.

@art stream-and-query
The practical rule is to use both channels. Consume the streaming updates as they arrive, and periodically reconcile by query. The stream tells you quickly. The query tells you for certain.

@chapter Try it
@words text="Submit · acknowledge · fill · timeout · reconcile"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, submit an order, step through the acknowledgements and fills, inject a timeout, and reconcile the final broker state.

@end text="Step an order through its life"
You can step an order through its lifecycle and inject timeouts, on Learn. That's learn dot get er done dot I O.
