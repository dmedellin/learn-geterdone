---
format: long
lesson: ddd-life-cycle/aggregates
title: Aggregates: where does an object begin and end?
thumb: One root, one boundary
---

@chapter A web with no edges
@title text="Aggregates" sub="Domain-Driven Design, Chapter 6" art=thumb
Chapter 6 is about the life of long-lived domain objects: stored, changed under rules, and tied to many others. Evans names two dangers. Losing integrity over that life, and burying the model under the machinery of managing it.

@art shared-address
His small case is a delete. Remove a person from the database, and the name and birth date plainly go too. But the address might be shared with others in the same house. Delete it, and their references dangle. Keep it, and stale addresses pile up.

@quote text="Put another way, how do we know where an object made up of other objects begins and ends?" cite="Evans, Domain-Driven Design, Chapter 6"
A garbage collector might tidy that up, but it's a gap in the model. Nobody has said what the person owns. Put another way, how do we know where an object made up of other objects begins and ends?

@art lock-too-much
Concurrency makes the gap expensive. Some rules apply to a group of objects, not one. Lock too little and two changes together break the rule. Lock too much and users block each other for nothing. Evans's claim is that the scope of a change is a modelling question.

@chapter Root and boundary
@art car-and-tires
An aggregate is a cluster with a root and a boundary. The root is a single entity, the only member outsiders may hold a reference to. His example is a repair shop's car, identified worldwide by its vehicle number. Its tires are tracked for wear, but never looked up on their own. The car is the root, and the tires sit inside.

@list heading="The rules" items="Root has global identity and checks the invariants@global identity|Outsiders hold only the root@outside|Only roots are fetched from the database@fetched|Insiders may refer to other roots@other aggregates|Delete the root, delete the cluster@deleting the root|Every rule true after each commit@committed"
Then the rules. The root has global identity, and checks the invariants. Nothing outside keeps a reference to an inner object. Only roots are fetched from the database. Objects inside may refer to the roots of other aggregates. Deleting the root takes everything inside. And after any committed change, all of the aggregate's rules are true.

@art strict-and-lagging
Rules inside an aggregate are enforced as each transaction completes. A rule that spans aggregates may be out of date for a while, and is brought back into line by events or a batch run. Choosing the boundary is choosing which rules get the strict treatment.

@chapter In code
@code block=1 lines=1-21 label=Java focus="4@allergies|7-12@recordAllergy|8-10@already recorded|18-20@read-only"
Here's a clinic's patient, the root of its aggregate. It owns its allergies. A new one goes through recordAllergy, which checks the patient's own rule: a substance is recorded once, or it's already recorded. And the list goes out read-only, for the caller to read and let go.

@chapter Count the references
@math heading="clinic" items="3 aggregates · 6 objects@three aggregates;;4 references cross a boundary@cross a boundary;;0 reach a non-root@none"
The lab takes the clinic's model: a patient with allergies and an emergency contact, an appointment with its consultation note, and a doctor. Three aggregates, six objects. Four references cross a boundary, and none of them reach a non-root. A note that names its doctor is fine: inside may hold another aggregate's root.

@art reach-past-root
Now add two shortcuts a busy programmer might take. The pharmacy system keeps a list of the allergies it's checked. And the note points straight at the allergy it discusses.

@math heading="shortcuts" items="6 references cross a boundary@six references;;2 violations, both past the patient root@two as violations"
Now six references cross a boundary, and the lab lists two as violations, both reaching past the patient. Each is a place where the allergy could change, or vanish, without the patient knowing.

@chapter Deletes follow the boundary
@math heading="delete-patient" items="removes 3: patient, allergy, contact@three objects;;1 dangling: appointment → patient@dangling"
Delete the patient, and the lab removes three objects: the patient, the allergy, and the contact. One reference is left dangling: the appointment's reference to the patient.

@art dangling-reference
That's not a failure of the pattern. It's the rule that spans aggregates, and the model must handle it, by refusing the delete while appointments exist, or closing them first. And deleting just an allergy? The lab refuses. It's not a root.

@chapter Where people slip
@list heading="Common slips" items="Objects stored together@The first|Nothing inside may refer out@The second|Every rule holds at once@And the third"
The first slip is taking an aggregate for objects stored together. It's defined by change, not storage. The second is thinking nothing inside may refer outward. It may, to other roots. And the third is expecting the boundary to make every rule hold at once.

@chapter Try it
@words text="Member · Loan · Copy" sub="plus the desk and the overdues report"
Your turn. A library with three aggregates, member, loan and copy, and two outside holders, the issue desk and the overdues report. Count the references that cross a boundary and those that reach a non-root. Then say what deleting the member removes, and what it leaves dangling.

@end text="Draw the boundary"
Type the model into the lab to check, on Learn. That's learn dot get er done dot I O.
