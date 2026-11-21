---
format: long
lesson: ddd-implicit-concepts/digging-out-concepts
title: Five ways to find the concept your model is missing
thumb: Listen for the missing word
---

@chapter Where deep models start
@title text="Digging Out Concepts" sub="Domain-Driven Design, Chapter 9" art=thumb
How does a team actually reach a deep model? Evans's answer in Chapter 9 is that it starts with something small: a concept hinted at in conversation, or buried in the design, made explicit.

@art hidden-concept
Most of the changes he cares about happen when developers notice something the conversation keeps suggesting, or the design quietly depends on, and give it an object or a relationship. Now and then that's a breakthrough. More often, the breakthrough comes later, once several such concepts are in place.

@chapter Listen to language
@quote text="When the users or domain experts use vocabulary that is nowhere in the design, that is a warning sign." cite="Evans, Domain-Driven Design, Chapter 9"
The first tool is listening. When the users or domain experts use vocabulary that is nowhere in the design, that is a warning sign.

@art listen-words
Notice the terms experts use to say something complicated in a word, the times they gently correct you, and the phrase that makes their puzzled looks go away. This isn't the old rule that every noun becomes a class. A word is a lead. And if developers and experts both use a term the design doesn't contain, the warning is twice as strong.

@chapter Four more places to dig
@art awkward-code
Scrutinize awkwardness is for when nobody's saying the word. Dig in the most awkward part of the design, where each new requirement adds complexity, and bring the experts in. In the book's example, an interest calculation was growing out of control, until a conversation turned up a term the model lacked.

@art contradiction
Contemplate contradictions takes seriously what two experts say when it can't all be true. Much is loose wording. But what's left can point to a deeper model. Not every contradiction should be resolved, but asking how both could be true is revealing.

@list heading="And two more" items="Read the book@Read the book|Try, try again@Try, try again"
Read the book means the field's own literature. A developer with an unhelpful expert can start there, and then ask better questions. And try, try again is the honest end of the list. Evans may follow half a dozen leads before one is worth trying, and replace that one later.

@chapter A library's glossary
@art three-columns
Now a library. The lab takes a glossary with one name per concept for each audience: the librarians, the developers, and the code. A dash means no name. It counts translations, one for each pair of audiences whose names differ, and the names each audience is missing.

@math heading="library-before" items="8 concepts · 1 named alike: loan@eight concepts;;12 translations@twelve;;code missing 2: recall, pickup window@no name"
Before: eight concepts, and only one, the loan, is named alike by everyone. A conversation touching each concept once needs twelve translations. And the code has no name for two of them: the recall, when a librarian asks for a book back early, and the pickup window, the days a held book waits.

@art doubly-strong
Look at recall. The librarians say it, and so do the developers, and the code has nothing. That's Evans's doubly strong warning, and it's worth more than the count.

@words text="reservation = hold + study-room booking"
The lab also finds one name doing two jobs. The developers say reservation both for a hold on a book and for a study room booking, which the code keeps apart.

@math heading="library-after" items="every concept named@every concept;;1 concept left · 2 translations@only one still;;code: user · everyone else: patron@user"
After the team has listened, recall and pickup window are classes, and everyone says hold and booking. Every concept is named, and only one still needs translating, at two pairs. The code says user, where everyone else says patron, because the class is shared with the login system. Whether to rename it, the lab can't say.

@chapter Where people slip
@list heading="Common slips" items="Wait to be handed the concept@The first|Make every term a class@The second|Expect the first idea to last@And the third"
The first slip is waiting for the missing concept to be handed to you. The second is turning every term the experts use into a class. A word is a lead, not an order. And the third is expecting the first good idea to last.

@chapter Try it
@words text="appointment · did-not-attend · triage · care-episode · referral · clinician"
Your turn. A clinic's glossary, six concepts, in the order experts, developers, code. Find the concepts the code can't name, and the one Evans would call a doubly strong warning. Then count the translations for the concepts every audience names.

@end text="Find the missing names"
Type the glossary into the lab to check, on Learn. That's learn dot get er done dot I O.
