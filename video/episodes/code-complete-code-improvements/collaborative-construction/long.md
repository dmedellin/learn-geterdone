---
format: long
lesson: code-complete-code-improvements/collaborative-construction
title: Code reviews vs testing: which finds bugs faster?
thumb: Another pair of eyes
---

@chapter The question
@title text="Collaborative Construction" sub="Code Complete, chapter 21" art=thumb
Why should anyone else read your code? Chapter twenty one's answer is that every collaborative technique rests on one idea.

@art blind-spots
You're blind to some of the trouble spots in your own work, and other people are blind to different ones. So it pays to have someone else look.

@quote text="Collaborative development practices tend to find different kinds of errors than testing does, implying that you need to use both reviews and testing to ensure the quality of your software." cite="McConnell, Code Complete, 2nd ed., Chapter 21, p. 497"
That's the chapter's argument in one sentence. Collaborative development practices tend to find different kinds of errors than testing does, implying that you need to use both reviews and testing.

@words text="Unit 30% · integration 35% vs design inspection 55% · code inspection 60%"
After Jones, the chapter sets testing's average rates against inspection's. About thirty percent for unit testing and thirty five for integration, against fifty five and sixty for design and code inspections. And reviews pass on a team's knowledge, from experienced programmers to new ones.

@chapter Pair programming
@art pair-desk
In pair programming, one programmer types, and the other watches for mistakes and asks whether the right code is being written. Support pairs with a coding standard, so they don't argue about style. Don't let the second one become a spectator. And rotate the pairs. Pairing, the book says, costs about the same as inspection, with similar quality.

@chapter Formal inspections
@art inspection-roles
The formal inspection was developed by Michael Fagan at IBM, and made public in his nineteen seventy six paper. Its roles are moderator, author, reviewers and scribe. Management stays away, and the results are never used to appraise anyone.

@list heading="What makes it formal" items="Checklists of past trouble@Checklists|Find defects, don't fix them@finding|Preparation, alone, first@Preparation|A moderator who isn't the author@moderator|Data kept to improve the next@data"
Checklists point reviewers at past trouble. The focus is finding defects, not fixing them. Preparation comes before the meeting, each reviewer alone. A moderator who isn't the author runs it. And data from each inspection improves the next.

@art book-pages
McConnell's own book is the story. The first edition was reread, reviewed by peers, edited, proofread, and corrected from readers' reports. For the second, small teams inspected it formally, and to his surprise they found errors that every one of those earlier reviews had missed.

@chapter The looser kinds
@art reading-alone
A walk through is loosely defined, usually led by the author, and in Jones's data finds fewer defects. Code reading puts the effort into each reviewer's own reading. And a dog and pony show is a demonstration to a customer, a management review, not a technical one.

@chapter What it costs
@math heading="Hours per defect" items="IBM: inspection 3.5 · testing 15 to 25@three point five;;Microsoft: inspection about 3 · testing 12@about three"
The book reports two companies from the nineteen nineties. At IBM, three point five staff hours to find each error by code inspection, against fifteen to twenty five by testing. At Microsoft's applications division, about three hours to find and fix one by inspection, against twelve by testing.

@art one-step
Why the gap? An inspection is a one step technique. It finds a defect and its cause together. A test finds a symptom and leaves the cause to be debugged. Still, these are two organisations' averages, on their projects, not yours.

@math heading="100 defects, testing only, 20 h each" items="unit 30%:  30 found@thirty;;system 40%:  28 found@twenty eight;;found 58 · hours 1,160@one thousand one hundred and sixty"
The lab puts numbers on it. A hundred defects go through unit testing and system testing, each at twenty hours per defect found. Unit testing finds thirty, system testing twenty eight. That's fifty eight found, for one thousand one hundred and sixty hours.

@math heading="Inspect first, at 3.5 h" items="inspection 60%:  60 found, 210 h@sixty defects;;unit:  12 found · system:  11.2 found@twelve;;found 83.20 · hours 674@six hundred and seventy four;;≈ 8.10 hours per defect@eight point one"
Put a code inspection at sixty percent and three point five hours in front. It finds sixty defects in two hundred and ten hours. Unit testing finds twelve, system testing eleven point two. That's eighty three point two found, in six hundred and seventy four hours, about eight point one per defect.

@chapter Where people slip
@list heading="Common slips" items="Thinking reviews cost time testing wouldn't@The first|Fixing code in the inspection meeting@The second|A walk-through as a light inspection@the third"
The first slip is thinking reviews cost time testing wouldn't. The book reports the opposite. The second is fixing the code in the meeting. Discussion ends once a defect's recognised, and fixes come afterwards. And the third is treating a walk through as an inspection with less paperwork. It finds significantly fewer defects.

@chapter Try it
@code block=1 lines=1-10 label=Java focus="1@what its comment promises|2-9@line by line"
Your turn. Read count passing as a reviewer preparing for an inspection would, alone and line by line, against what its comment promises. List every defect you'd raise, with its line number, and name the checklist question that would have pointed you at it.

@end text="Price an inspection"
You can compare pipelines, with and without an inspection, in the lab on Learn. That's learn dot get er done dot I O.
