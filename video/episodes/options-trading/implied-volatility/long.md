---
format: long
lesson: options-trading/implied-volatility
title: Implied volatility: how you can be right on direction and still lose
thumb: Right direction, still lost
---

@chapter The question
@title text="Implied Volatility" sub="Options Trading" art=thumb
You buy a call. The stock goes up, just as you expected. And the call is worth less than you paid. That isn't a glitch. It's implied volatility, and it moves on its own.

@words text="IV prices the size of a move" sub="not its direction"
Here's the core idea. Implied volatility prices the size of movement, not its direction. And it can change while the stock stands still, or move against you while the stock does exactly what you wanted.

@chapter What IV is
@art model-dial
Implied volatility is the volatility input that's consistent with an option's price under a model. Plug it into the model and you get back the market price. It's a reading of how much movement the price assumes. It does not predict direction.

@art wide-narrow
Think of two possible futures for the same stock. In one, the price might swing widely. In the other, it might barely move. The wide one has higher implied volatility, and the option costs more, whether the stock ends up rising or falling.

@chapter Vega exposure
@art iv-up-down
Long options generally gain theoretical value when implied volatility rises, and lose value when it falls, all else equal. That sensitivity is called vega, and it's the subject of a later lesson. For now, the direction is what matters. A long option wants implied volatility to rise.

@chapter Events
@art event-spike
Scheduled events change implied volatility. Before an anticipated event, like earnings or a decision, implied volatility can rise, because a big move is possible. Once the event has happened and the uncertainty is resolved, the option can reprice rapidly.

@words text="IV crush"
That rapid fall is often called IV crush. And it's the answer to the opening puzzle. A favorable move in the stock can be offset, or more than offset, by a large reduction in implied volatility.

@chapter Separate the two causes
@math heading="Attribute the premium change" items="Change = stock-move part + IV-change part@two parts;;Stock up → long call gains@stock move;;IV down → long call loses@volatility change;;Loss if the IV part is larger@larger"
So split any premium change into two parts: the part the stock move explains, and the part the volatility change explains. For a long call, the stock moving up adds value. Implied volatility falling takes value away. If the volatility part is larger, the trade loses, even though the direction was right.

@art two-arrows
That's exactly what the lesson's lab lets you do. Set a stock move and an implied volatility change separately, then read which one explained the premium change. The model behind it is simplified, European Black Scholes with a fixed rate and no dividends, but the split works the same way.

@chapter Evaluate IV exposure
@art before-entry
So before you enter, run through four questions. They keep the direction you expect and the volatility you're paying for in separate boxes.

@list heading="Before you enter" items="Read current IV@Read|Identify known events@identify|Model expansion and contraction@model|Plan the exit timing@plan"
Separate your directional thesis from the volatility price you're paying. Read current implied volatility by comparing contracts and expirations, rather than treating it as a standalone buy or sell signal. Identify known events. Model expansion and contraction, and test whether the position is still acceptable under several outcomes. And plan the exit timing: before, during, or after the event.

@chapter Where people slip
@list heading="Common mistakes" items="High IV as a direction forecast@The first|Ignoring IV crush@The second|Comparing raw IV across unrelated underlyings@And the third"
The first mistake is treating high implied volatility as a directional forecast. It describes expected variability, not whether price will rise or fall. The second is ignoring IV crush. And the third is comparing raw implied volatility across unrelated underlyings. Volatility behaves differently by product, maturity, and event context.

@words text="Compare contracts and expirations" sub="not unrelated underlyings"
So when you read implied volatility, compare like with like. Look across the contracts and expirations of the same underlying, and ask what event the market might be pricing. A single number on its own, compared with some other stock, tells you very little.

@chapter Try it
@words text="Stock part + volatility part = the change"
Your turn. In the lab's event preset, take the premium change apart. Find the part the stock move explains and the part the volatility change explains, and reproduce the loss from those two contributions. Then say, in one sentence, why a correct direction can still lose.

@end text="Move the stock and IV separately"
You can set a stock move and a volatility change separately, on Learn. That's learn dot get er done dot I O.
