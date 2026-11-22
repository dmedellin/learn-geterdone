---
format: long
lesson: volume-and-order-flow/order-book-and-market-depth
title: Order book and market depth: intentions, not control
thumb: Displayed isn't done
---

@chapter The question
@title text="Order Book and Market Depth" sub="Volume and Order Flow" art=thumb
The order book shows you orders waiting to trade, at prices above and below the market. A big wall of size looks like it should stop price. Sometimes it does. Often it isn't even there when price arrives.

@words text="The book shows intentions" sub="not completed control"
The lesson's idea is this. The order book shows available intentions, not completed control. A large displayed bid can support price only if it remains, and absorbs selling. A large ask can cap price only if it remains, and absorbs buying.

@chapter Depth, queue, events
@art ladder
Three words. Depth is the displayed resting quantity at multiple bid and ask prices. It's the size you can see waiting near the market.

@art queue
Queue is how orders at the same price wait, according to the venue's priority rules. So orders at one price form a line, in an order the venue sets. Ignoring your queue position is one of the lesson's common mistakes, so keep it in mind.

@art book-events
And events are what change the book. Adds, executions, modifications, and cancellations. Orders can be added, moved, or cancelled at any time.

@chapter Reading the near touch
@math heading="Bids 420 @ 99.99 · 690 @ 99.98 · Asks 380 @ 100.01 · 610 @ 100.02" items="depth = 420 + 690 + 380 + 610 = 2,100@twenty one hundred;;spread = 100.01 − 99.99 = 0.02@point zero two"
Here's the lesson's book. Bids of four hundred and twenty at ninety nine ninety nine, and six ninety at ninety nine ninety eight. Asks of three eighty at one hundred point zero one, and six ten at one hundred point zero two. Near touch depth, two levels each side, is twenty one hundred. The spread is point zero two.

@math heading="Not these" items="✗  1,110: the bid side alone@eleven hundred and ten;;✗  spread 0.01@point zero one"
Eleven hundred and ten would be the bid side alone. The lab's near touch depth adds both sides. And the spread is best ask minus best bid, one hundred point zero one minus ninety nine ninety nine, so point zero two, not point zero one.

@chapter A wall that holds
@art bid-absorbs
Now watch a wall get tested. A large bid is repeatedly hit, but price doesn't fall. What may be happening? Buy side absorption. Resting buyers are absorbing aggressive selling, and preventing lower progress.

@words text="Not seller control · not no trading"
It's not seller control. Sellers are hitting the bid, and price isn't falling. That's sellers failing to progress. And it's not a lack of trading. The bid is being hit, so trades are executing. What's absent is price movement.

@chapter A wall that vanishes
@art vanishing-ask
Now the other case. A large ask disappears before price reaches it. What happened? It was cancelled or moved. It didn't provide executed resistance. Displayed intent is not the same as a completed transaction.

@words text="Never tested · never volume"
So it didn't guarantee a reversal. A cancelled order was never tested, and nothing about it says where price goes. And it didn't become volume. Volume is executed trade, and an order that vanished without executing added nothing to it.

@chapter Depth is not the whole picture
@words text="Depth omits" sub="spread · replenishment · execution cost · market response"
Why is depth alone an incomplete liquidity measure? Because it omits spread, replenishment, execution costs, and market response. Liquidity also depends on resilience, impact, and how orders behave when tested.

@art hidden
Displayed depth isn't a firm commitment to trade. Every displayed order can be pulled before anything reaches it. And depth beyond the best prices is what a large market order walks through. That's why execution evidence is required.

@chapter Where people slip
@list heading="Common mistakes" items="Trading every large displayed order@The first|Assuming all liquidity is visible@The second|Ignoring book speed and queue position@the third"
Three mistakes. The first is trading every large displayed order. The second is assuming all liquidity is visible. And the third is ignoring order book speed and queue position.

@chapter Try it
@list heading="Reading steps" items="Read spread and depth@read spread and depth|Track changes@track changes|Require execution evidence@require execution evidence"
The lab's steps are these. First, read spread and depth. How much quantity is displayed near the market? Then track changes. Does liquidity remain, replenish, get consumed, or disappear? Then require execution evidence. Displayed size matters only through its behaviour when tested.

@words text="Synthetic educational data" sub="no live market connection"
The lab runs on synthetic educational data, with no live market connection. Watch a large displayed order as price approaches it, and before you read the explanation, say which of those four things it did.

@end text="Watch what the wall does"
You can watch a practice book add, trade and cancel in the lab, on Learn. That's learn dot get er done dot I O.
