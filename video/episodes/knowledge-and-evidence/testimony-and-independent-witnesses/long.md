---
format: long
lesson: knowledge-and-evidence/testimony-and-independent-witnesses
title: What a reliable witness is worth, and Hume on miracles
thumb: Nine in ten isn't nine in ten
---

@chapter One witness
@title text="Testimony and Independent Witnesses" sub="Knowledge and Evidence" art=thumb
A witness is right nine times in ten, and she tells you something's true. Does that make it nine in ten likely? Not unless you ignore what you thought before she spoke.

@art witness-reliability
Here's the setup. A claim has prior credence one in a hundred. The witness is reliable in a precise sense. She says yes with probability nine tenths when the claim is true, and says no with probability nine tenths when it's false. So a yes has likelihood nine tenths if true, and a tenth if false. And she says yes.

@math heading="One yes" items="true:  1/100 · 9/10 = 9/1000@If true;;false:  99/100 · 1/10 = 99/1000@if false;;posterior:  9/108 = 1/12, about 8%@one twelfth"
Multiply each prior by its likelihood. If true, one hundredth times nine tenths, nine thousandths. If false, ninety nine hundredths times a tenth, ninety nine thousandths. So the posterior is one twelfth, about eight percent. She raised the claim from one percent to eight, and nowhere near ninety.

@words text="P(yes | true) ≠ P(true | yes)"
It's the base rate mistake again, in a new setting. Her reliability is the probability of a yes, given that the claim is true. What you want is the probability that the claim is true, given a yes. A claim that was improbable to start with stays improbable, unless the witness is very good.

@chapter Odds and the factor
@math heading="In odds" items="factor:  (9/10) / (1/10) = 9@nine tenths over a tenth;;odds:  1 to 99  →  9 to 99 = 1 to 11@one to ninety nine"
In odds it's quicker. Her Bayes factor is nine tenths over a tenth, which is nine. The prior odds are one to ninety nine. Multiply, and the posterior odds are nine to ninety nine, which is one to eleven. That's a credence of one twelfth.

@chapter Independent witnesses
@art two-witnesses
Two witnesses are independent when, given whether the claim is true, what one says doesn't depend on what the other says. Then the likelihood of both answers is the product of the two likelihoods. And so is the Bayes factor.

@math heading="Witnesses at 9 in 10" items="none:  factor 1,  posterior 1/100@With no witness;;one:  factor 9,  posterior 1/12@one witness;;two:  factor 81,  posterior 9/20@two witnesses"
A second witness of the same reliability also says yes. Now the factor is nine times nine, eighty one. With no witness, the claim is at one hundredth. With one witness, one twelfth. With two witnesses, nine twentieths, a little under a half.

@art odds-climb
The second witness is worth as much as the first, in the sense that matters: a factor of nine. And it's worth more in credence, because the same factor, applied at higher odds, moves the credence further.

@art shared-source
But independence is an assumption. Two newspapers that both reprint the same agency report are one witness heard twice. Multiplying their factors would count that witness's possible error as if it had been confirmed. If the second only repeats the first, the posterior stays at one twelfth.

@chapter Hume and the miracle
@art miracle-scale
Hume's argument about miracles can be put as a comparison of two likelihoods. Suppose an extraordinary event has prior one in a million, and a witness reports it who's wrong only once in a thousand. Either the event happened and she's right, or it didn't and she's wrong.

@math heading="Two ways the report arises" items="happened, she's right:  (1/1000000) · (999/1000)@happened and she's right;;didn't, she's wrong:  (999999/1000000) · (1/1000)@didn't and she's wrong;;second is 1,001 times the first:  posterior 1/1002@a thousand and one times"
The weight for happened and she's right is one in a million times nine hundred and ninety nine thousandths. For didn't and she's wrong, it's nine hundred and ninety nine thousand, nine hundred and ninety nine millionths, times a thousandth. The second is a thousand and one times the first. The posterior is one over a thousand and two.

@art stacking-factors
But that's a comparison, not a ban. A report is worth believing when its Bayes factor outweighs the odds against the event. Three independent witnesses like her have a factor near a thousand million, and put the claim at about ninety nine point nine percent. What's worth disputing is whether they really are independent, and as reliable as stated.

@chapter Where people slip
@list heading="Common slips" items="Treating reliability as the posterior@The first|Multiplying witnesses who share a source@The second|Reading Hume as saying no testimony could do it@the third"
The first slip is thinking a ninety percent reliable witness makes the claim ninety percent likely. That's only true from even odds. The second is multiplying the factors of witnesses who share a source. And the third is reading Hume as saying no testimony could ever support a miracle. The argument sets a bar.

@chapter Try it
@words text="prior 1/2 · two witnesses at 9 in 10" sub="posterior?"
Here's one to try. Start the claim at one in two instead, and have two independent witnesses at nine in ten both say yes. Multiply the odds, and convert back to a credence. You should find eighty one over eighty two.

@end text="Add witnesses, watch the odds"
You can change the prior, the reliability and the number of witnesses, on Learn. That's learn dot get er done dot I O.
