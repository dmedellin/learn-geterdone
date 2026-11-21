---
format: long
lesson: mind-language-and-meaning/scope-ambiguity-and-negation
title: Scope ambiguity: one sentence, two readings, two values
thumb: Where does the not go?
---

@chapter The question
@title text="Scope Ambiguity and Negation" sub="Mind, Language and Meaning" art=thumb
The King of France is not bald. Is that true, or false? There's no king. The answer depends on where you put the not. And that's not a matter of style. Each placement is a different formula, with its own value.

@art quantifier-swap
The scope of a negation or a quantifier is the part of the formula it applies to. A sentence is scope ambiguous when its words fit two formulas that differ only in scope.

@chapter Two places for the not
@art not-outside-inside
Take, the King is not bald, in the model where nobody is a king. There are two places for the negation. Outside the description, it denies the whole claim: it's not the case that there's one king and he's bald. Inside, it's part of what's said of the king: there's one king, and he's not bald.

@math heading="No king in the model" items="wide:  ¬ (the King is bald)  →  True@the wide one;;narrow:  (the King) is not bald  →  False@the narrow one"
Evaluate the wide one. The king is bald is false, because nobody is a king. The negation of false is true. Evaluate the narrow one. It still opens by asserting a king, which there isn't, so it's false. In the same model, the two readings have opposite values.

@art excluded-middle
So someone who means the wide reading is saying something true. Someone who means the narrow reading is saying something false, since it adds there's a king. Russell used the distinction to defend the law of excluded middle. Either the king is bald or he isn't. With no king, neither holds, unless the second is read with the negation outside. So the ambiguity isn't a quibble. A law of logic seemed to hang on it.

@chapter Two orders for quantifiers
@art love-ring
The same thing happens with two quantifiers. Take, everyone loves someone. Put three people in a ring. a loves b, b loves c, and c loves a.

@math heading="Everyone loves someone" items="∀x ∃y Loves(x, y):  True@each person loves;;∃y ∀x Loves(x, y):  False@one person everyone loves"
One reading is, for every x there's a y that x loves: each person loves a person, who may differ. In the ring, that's true. The other is, there's one person everyone loves. In the ring, nobody is loved by all three. False. Same English sentence, two formulas that aren't equivalent, and in one model they get two different values.

@chapter How they relate
@art all-love-c
They are related, though. If there's one person everyone loves, then each person loves someone, namely that one. So the second implies the first. The ring shows it doesn't run back. And in a model where a, b and c all love c, both readings are true, with c as the witness.

@words text="When the description denotes, the readings agree" sub="the negation only separates them where it fails"
Readings can also agree. If the King is a real person and he's not bald, the wide and narrow readings both come out true. The negation only separates them where the description fails. That's why the ambiguity went unnoticed for so long. In ordinary cases, it makes no difference.

@art two-ears
The lab evaluates both formulas, and doesn't choose. Which one a speaker meant is a question about the speaker. The lesson's claim is only that a careful hearer should ask.

@chapter Where people slip
@list heading="Common slips" items="Believing a sentence has one logical form@The first|Hearing everyone loves someone as one beloved@The second|Moving a negation across a quantifier freely@And the third"
The first slip is believing a sentence has one logical form. The second is hearing, everyone loves someone, as saying there's one beloved. Someone who answers, but who, has supplied the second order. And the third is moving a negation across a quantifier as if it were free. Not for all differs from for all not. Moving it needs a rule, and the rule swaps the quantifiers.

@chapter Try it
@words text="∀x ∃y  vs  ∃y ∀x" sub="edit Loves until they agree"
Start with the ring of three, and evaluate both orders. Then edit who loves whom until the two orders agree, and name the witness. Then go back to the king, and find a model where the wide and narrow readings agree.

@end text="Read it with each scope"
You can move the negation and the quantifiers yourself, on Learn. That's learn dot get er done dot I O.
