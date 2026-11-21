---
format: long
lesson: ddd-putting-the-model-to-work/crunching-knowledge
title: Crunching Knowledge: how a team digs out a domain model
thumb: Developers and experts, together
---

@chapter The story
@title text="Crunching Knowledge" sub="Domain-Driven Design, Chapter 1" art=thumb
Eric Evans opens his book with a confession. He was asked to build a tool for engineers who design printed circuit boards, and he knew nothing about electronics.

@art one-way-handoff
So he asked the engineers what the software should do. What came back were designs for reading, sorting and annotating text files. Useful, maybe, but nowhere near the leap the engineers actually wanted.

@art sketch-together
What helped was something else. He talked through what they needed while sketching informal diagrams. They corrected him, and he corrected their terms in turn. Over some days, the two sides built a model together.

@words text="A prototype with no UI and no storage" sub="only the behaviour"
Then he wrote a small prototype with no user interface and no storage, only the behaviour. Now the engineers could see what the model meant, and argue with it.

@chapter Five ingredients
@list heading="Effective modelling" items="Bind the model to the code early@Bind the model|Cultivate a language based on the model@cultivate a language|Make it rich in knowledge@rich in knowledge|Distil it@distil it|Brainstorm and experiment@brainstorm"
From that story Evans draws five ingredients. Bind the model to the implementation early, and keep the link. Cultivate a language based on the model. Make it rich in knowledge: behaviour and rules, not a data schema. Distil it, adding concepts that prove useful and dropping those that don't. And brainstorm and experiment, because an awkward model is often heard before it's seen.

@chapter Crunching
@art many-to-few
He compares a modeller to a financial analyst sifting figures for the few that matter. Many ways of organising the domain are tried and dropped, until a small set of abstract concepts makes sense of the detail.

@quote text="Knowledge crunching is not a solitary activity. A team of developers and domain experts collaborate, typically led by developers." cite="Evans, Domain-Driven Design, Chapter 1"
And here's the claim the whole lesson rests on. Knowledge crunching is not a solitary activity. A team of developers and domain experts collaborate, typically led by developers.

@chapter Three ways to fail
@art one-way-handoff zoom=in
He sets it against three ways of working that don't crunch. In waterfall, experts talk to analysts, and analysts hand an abstraction to programmers. Nothing comes back, so the knowledge flows one way and never builds up.

@list heading="Also not crunching" items="Iterate without abstracting@iterative project|Abstract without the experts@good programmers"
In an iterative project that doesn't abstract, the team learns what the application does, but never the principles behind it. And where good programmers abstract on their own, without the experts, the concepts come out naive.

@chapter Continuous learning
@art leaking-knowledge
At the start a team never knows enough, and what it knows leaks. People move on, teams get reorganised, work gets outsourced, so the code arrives and the knowledge doesn't. Evans even admits the feature his story turned on was later dropped. The early work still mattered, because it started the crunching everything after it used.

@chapter Count the translations
@code block=1 lines=1-8 label=Records focus="1@accession|5@variety|7@packet"
The lesson's own domain is a seed library. Each record is one concept, then the curators', the growers' and the developers' word for it. The lab counts a translation for each pair of audiences whose names differ. Look at accession, then variety, then packet.

@math heading="First meetings" items="8 concepts · 1 named alike@eight concepts;;6 × 3 + 1 × 2 = 20 translations@six concepts;;batch = accession and packet@ambiguous"
There are eight concepts, and only variety is named alike by everyone. On six concepts all three words differ, which is three translations each. Packet adds two more, because only the developers differ. That's twenty. And there's an ambiguous name: the developers' batch means both an accession and a packet.

@art three-vocabularies
Twenty isn't a cost the lab can price. It's the number of places a conversation has to stop and explain a word.

@math heading="After crunching" items="7 concepts · 6 named alike@seven concepts;;2 translations, both on regeneration@two translations"
Some weeks later, the model has consolidated the synonyms and dropped the isolation distance, which the software doesn't need. Now there are seven concepts, six named alike, and just two translations, both on regeneration, which the growers still call a grow out.

@chapter Where people slip
@list heading="Common slips" items="Crunching is the analysts' job@The first|Short iterations are enough@The second|The model holds everything@And the third"
The first slip is thinking crunching is the analysts' job, finished before coding starts. The second is thinking short iterations and demos are enough. They aren't, if nobody abstracts. And the third is expecting the model to hold everything the experts know. A model is selective by design.

@art consolidated-terms
Whether grow out belongs in the model, or stays the growers' dialect, is a judgement the count doesn't make. That's for the team to decide.

@chapter Try it
@code block=2 lines=1-4 label=Records focus="1@withdrawal|2@return"
Your turn. Four concepts from the lending desk, with the curators', the volunteers' and the code's names. Count the translations by hand, starting with withdrawal and return, and find the name one audience uses for two concepts.

@end text="Count your team's translations"
Then type the records into the lab and check your count, on Learn. That's learn dot get er done dot I O.
