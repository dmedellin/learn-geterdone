---
format: long
lesson: ddd-building-blocks/entities
title: Entities: what makes an object the same thing over time
thumb: Same thing, every change
---

@chapter Mistaken identity
@title text="Entities" sub="Domain-Driven Design, Chapter 5" art=thumb
Evans opens this pattern with a story from his own life. He was sued for damage to a flat he'd never seen, mistaken for a former tenant with the same name.

@art two-listings
What saved him was an old phone book, showing two listings side by side: his, and his namesake's. People can resolve a mistaken identity with some resourcefulness. A system that confuses two people corrupts its data.

@chapter Identity, not attributes
@art thread-of-identity
Many things are defined by identity, not by any attribute. A person's name, address and finances can all change, and the person persists. The question for a model is whether its users care that it's the same person.

@art look-alike-pair
And it cuts both ways. Two records may need matching even though their attributes differ. And two others need telling apart even though their attributes agree.

@quote text="The model must define what it means to be the same thing." cite="Evans, Domain-Driven Design, Chapter 5"
So Evans ends the pattern like this. The model must define what it means to be the same thing.

@words text="== is not identity" sub="lost when stored, read back, or sent"
And the language's own identity won't do. Java's double equals only says two references point at one object in memory. That's lost whenever an object is stored and read back, or sent across a network.

@chapter Imposed, because useful
@art stadium-seats
Identity isn't part of the things themselves. It's imposed because it's useful. Two equal deposits on one day are still two transactions. And a stadium's seats are entities when tickets are for numbered seats, but not at general admission, where only the count matters.

@chapter Designing it
@list heading="Spare and identifiable" items="Attributes that identify or match it@identify|Behaviour essential to the concept@essential|Everything else moves out@moved"
Keep the entity class spare: the attributes that identify the object or are commonly used to find it, the behaviour essential to the concept, and the rest moved to associated objects.

@art tracking-number
For the identifier itself, some attributes can serve as a key, though such keys have exceptions. Otherwise the system attaches an identifier that's unique and, once assigned, never changes. It may be hidden, or given to users, like a parcel's tracking number.

@words text="National numbers, phone numbers" sub="can be missing, shared or reassigned"
Identifiers issued outside the system, like a national number or a phone number, can be missing, shared or reassigned. That's why matching records often ends with a person deciding.

@chapter A clinic's patients
@code block=1 lines=1-16 label=Java focus="2@issued once|8-10@equals|13-15@hashCode"
Here's a patient at a clinic. Its id is issued once and never changed. And equals compares only that id, as does hashCode. The name, birth date and town can change freely.

@math heading="patients" items="4 records · 6 pairs@four records;;same by identity: 1@same by identity;;same by attributes: 1@same by attributes"
The lab compares a front desk's and a lab's records: four records, six pairs. One pair is the same by identity, patient P one oh four seven, in both places. One pair is the same by attributes: two different patients called Ana Ruiz, same birth year, same town.

@art look-alike-pair zoom=in
They disagree on both. The first is a changed pair, because she's moved and only the lab knows. The second is a look-alike pair. Matching on fields would split one patient into two, and merge two patients into one.

@math heading="patients-keyed-by-name" items="same by identity: 3@three pairs;;2 changed pairs · 0 look-alikes@two changed"
Now build the identifier from what people search by: the name with the birth year. Three pairs are the same by identity, every pairing of the three Ana Ruiz records. Two changed pairs, no look-alikes. The lab reports, faithfully, that two different patients are one.

@art merged-patients
That's Evans's warning about attribute keys. The count follows the identity you state, and only the model can say whether that identity is right.

@chapter Where people slip
@list heading="Common slips" items="Compare every attribute@The first|Give everything an identity@The second|Load the entity with everything@And the third"
The first slip is deciding sameness by comparing every attribute. The second is giving every object an identity, to be safe. Identity costs analysis and design. And the third is loading the entity with every attribute and behaviour.

@chapter Try it
@words text="m1–m4 · L-301 · L-455" sub="six pairs to compare"
Your turn. Four library member records, all named Kim Lee, with two identifiers between them. Compare all six pairs, count the same by identity and by attributes, and list the changed pairs and look-alikes. Then say what a librarian would ask.

@end text="Compare by identity"
Check your answer in the lab, on Learn. That's learn dot get er done dot I O.
