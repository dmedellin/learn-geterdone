---
format: long
lesson: ddd-putting-the-model-to-work/ubiquitous-language
title: The Ubiquitous Language: one vocabulary, from speech to code
thumb: Stop translating
---

@chapter The divide
@title text="The Ubiquitous Language" sub="Domain-Driven Design, Chapter 2" art=thumb
On most projects, nobody quite speaks the same language. Evans thinks that's one of the most expensive things a team can tolerate.

@art fractured-language
Experts speak their own field's jargon, often in several flavours. Developers describe the system in functional terms, or invent abstractions the experts never hear. So everyone translates: developers for experts, experts for other experts, developers for each other.

@art bilingual-bottleneck
A few people become bilingual, and they turn into bottlenecks, with translations that are inexact. Worse is what translation hides: two people using one word for different things without noticing. That shows up later as software whose parts don't fit.

@quote text="Translation blunts communication and makes knowledge crunching anemic." cite="Evans, Domain-Driven Design, Chapter 2"
Evans puts it in one line. Translation blunts communication and makes knowledge crunching anemic.

@chapter The pattern
@art one-language
The answer is to build the team's language on the model, and use it without exception: in conversation, in writing, in diagrams and in the code. The names of classes and their main operations are its vocabulary. The model's relationships are its grammar.

@quote text="Recognize that a change in the UBIQUITOUS LANGUAGE is a change to the model." cite="Evans, Domain-Driven Design, Chapter 2"
And there's a point the lab will lean on. Recognize that a change in the ubiquitous language is a change to the model.

@words text="Sounds circular?" sub="speaking the model exposes its gaps"
Evans admits that sounds circular. At first the model isn't good enough to be a language. But the jargons carry ambiguities and contradictions, and insisting on speaking the model drags its weaknesses into the open. Gaps get new words, new words change the model, and the model changes the code.

@art two-dialogues
His example is two dialogues about rerouting a cargo. In the first, the developer talks in rows, flags and procedures. In the second, both talk about a route specification and the itinerary that must satisfy it. The second is shorter, and says more. The difference is in the nouns.

@chapter Out loud, one team
@art say-it-aloud
Modeling out loud adds a habit. An awkward model is often easier to hear than to see. So describe scenarios aloud in the model's terms, look for shorter ways to say them, and carry the better phrasing back to the diagrams and the code.

@words text="If capable experts can't follow it, the model is wrong."
And one team, one language adds a limit. Developers often keep the model from the experts as too abstract. Evans answers that if capable experts can't follow the model, the model is wrong. The line between languages must never fall between the experts and the developers.

@chapter The box office
@code block=1 lines=1-6 label=Records focus="1@production|2@performance|4@booking"
Here's a theatre's box office. Each record is a concept, then the experts' word, the developers' word, and the code's name. Look at production, performance and booking.

@math heading="two-languages" items="6 concepts · 0 named alike@six concepts;;5 × 3 + 2 = 17 translations@seventeen;;show = production and performance@show"
The lab finds six concepts, none named alike by all three. Every concept costs three translations except production, which costs two. That's seventeen. And the ambiguous name is the experts' show: the production that runs all season, and the one performance on Tuesday evening.

@art ambiguous-word
That's the translation no one notices in the room. The experts hear no difference. A developer told a show is sold out has to guess which one.

@math heading="one-language" items="5 of 6 named alike@five of the six;;2 translations, both on booking@both on booking;;class order → booking@renamed"
After the team takes the model's words for its own, experts included, five of the six concepts are named alike. Two translations remain, both on booking, because the code still has a class called order. By the pattern, that class is to be renamed.

@chapter Where people slip
@list heading="Common slips" items="Keep a bilingual translator@The first|Treat a rename as cosmetic@The second|Shield the experts from the model@And the third"
The first slip is keeping two vocabularies, with a bilingual teammate to translate. The second is treating a rename as cosmetic. The word changed, so the model changed. And the third is shielding the experts from the model as too abstract for them.

@chapter Try it
@code block=2 lines=1-4 label=Records focus="1@subscription|2@exchange|3@standby"
Your turn. Four more concepts: subscription, exchange, standby and seat, with the experts', the developers' and the code's names. Count the translations by hand, and say which audience the code agrees with on each one.

@end text="Count the translations"
Then type them into the lab, on Learn. That's learn dot get er done dot I O.
