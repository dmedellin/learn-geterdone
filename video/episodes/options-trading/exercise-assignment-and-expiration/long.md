---
format: long
lesson: options-trading/exercise-assignment-and-expiration
title: Exercise, assignment and expiration: what you hold on Monday
thumb: What do you hold on Monday?
---

@chapter The question
@title text="Exercise, Assignment, and Expiration" sub="Options Trading" art=thumb
Your option expires on Friday. On Monday, you might hold nothing. Or you might hold shares, or owe shares, or have cash missing from your account. Which one depends on things that are easy to ignore until the last minute.

@words text="Exercise · assignment · expiration handling"
Three words do the work here. Exercise is the holder's act. Assignment is what that act does to a writer. And expiration handling is the broker's. Keep the three apart and the outcomes become predictable.

@chapter Exercise
@art holder-exercise
Exercise is the holder using the contractual right, to buy or to sell the underlying according to the contract terms. A call holder who exercises buys shares at the strike. A put holder who exercises sells shares at the strike.

@chapter Assignment
@art writer-assigned
Assignment is the other side of the same event. When a holder exercises, a writer is selected to fulfill the obligation. A short call writer who's assigned has to deliver shares at the strike. A short put writer who's assigned has to buy them at the strike.

@words text="Early assignment" sub="short American options"
And on American style options, assignment doesn't have to wait for expiration. It can happen before, especially when the option's remaining extrinsic value is low. Ignoring that is one of the lesson's common mistakes.

@chapter Expiration handling
@art auto-exercise
At expiration, in the money standardized options may be exercised by exception. In other words, automatically, unless someone says otherwise. But contrary instructions and brokerage policies can change the result. The actual handling depends on the contract and on your brokerage firm.

@art otm-instruction
And out of the money isn't a guarantee either. A holder can sometimes give exercise instructions even when exercise looks economically unusual. Assuming an out of the money option can never be exercised is another of the lesson's mistakes.

@chapter What changes hands
@list heading="The simulator asks" items="Side: holder or writer@holder or writer|Type: call or put@call or put|Style: American or European@American or European|Price at expiration and shares held@shares you already hold"
The lesson's simulator makes this concrete. You pick holder or writer, call or put, and American or European style. Then set the price at expiration and the shares you already hold. It shows what changes hands: shares, cash, or nothing. It's a model of the role and the likely consequence, not a promise about your broker.

@art split-legs
The hardest case is a spread where the stock finishes between the two strikes, so one leg is in the money and one is out. One leg may be exercised or assigned, and the other simply expires. After hours movement and separate exercise decisions can leave you with a stock position you never planned to hold.

@chapter Manage it deliberately
@art deadline-clock
Notice what all of this has in common. Every one of these surprises shows up at the very end, when there's the least time to react. Brokers have their own instructions and cutoff times, so work from the actual ones, never from assumptions.

@list heading="Before expiration" items="Identify settlement and style@settlement|Review moneyness and extrinsic value@moneyness|Check buying power and shares@buying power|Submit or close before firm deadlines@deadlines"
Operational risk can remain even when the maximum theoretical loss is defined. So first, identify settlement and style: physical or cash, American or European. Review moneyness and extrinsic value early, not in the final minutes. Check your buying power and shares for every possible outcome. And submit instructions, or close, before your firm's deadlines, using its actual cutoff times.

@chapter Where people slip
@list heading="Common mistakes" items="OTM can never be exercised@The first|Ignoring early assignment@The second|One leg ITM, one OTM, no review@The third"
The three mistakes, together. The first is assuming an out of the money option can never be exercised. The second is ignoring early assignment on short American options. And the third is letting one spread leg expire in the money and the other out of the money, without reviewing what you'll be left holding.

@chapter Try it
@words text="Exercised or assigned? What moves? Which broker step first?"
Your turn. For any expiring position, say whether it's exercised or assigned, what shares or cash move, and which broker step you'd verify first. Then take the drill's spread, with legs on different sides of the stock, and say what you hold on Monday.

@end text="Run the expiration simulator"
You can choose side, type and style, and see what changes hands, on Learn. That's learn dot get er done dot I O.
