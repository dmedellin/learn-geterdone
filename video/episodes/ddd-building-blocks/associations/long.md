---
format: long
lesson: ddd-building-blocks/associations
title: Associations in Domain-Driven Design: fewer links, more meaning
thumb: Constrain every link
---

@chapter Links cost
@title text="Associations" sub="Domain-Driven Design, Chapter 5" art=thumb
A line between two boxes takes a second to draw. Evans's point is that every one of those lines is a mechanism somebody has to build and keep working.

@art link-is-pointer
For each association the model says can be traversed, the code needs something that behaves the same way. A link between a customer and a sales rep might be a pointer, or a method that looks the other up in a database. Both carry the same model.

@art many-to-many-web
The trouble is that the world is full of many to many links, many of them two way, and so are early models. They're hard to implement, hard to maintain, and they say little about the relationship.

@quote text="It is important to constrain relationships as much as possible. A bidirectional association means that both objects can be understood only together." cite="Evans, Domain-Driven Design, Chapter 5"
So, in Evans's words: it is important to constrain relationships as much as possible. A bidirectional association means that both objects can be understood only together.

@chapter Three moves
@list heading="Make it tractable" items="Impose a traversal direction@impose a traversal direction|Add a qualifier@add a qualifier|Eliminate what isn't essential@eliminate"
He gives three moves. Impose a traversal direction. Add a qualifier, to reduce the multiplicity. And eliminate associations that aren't essential.

@art one-way-arrow
His example is a country and its presidents. You could follow it either way, but almost nobody starts from a person and asks which country he led. Making it one way, from country to president, is a simpler design, and an insight about which direction matters.

@art qualified-link
Look harder at the same link. A country has one president at a time. So qualified by the date, the association is one to one, and that rule is now in the model. And the two way links you keep now mean something: both directions matter to the domain.

@chapter Both ways in code
@code block=1 lines=1-9 label=Java focus="3@a set of courses|5-8@assign|7@the other end"
Here's what a two way link costs. A teacher holds a set of courses. To assign one, you add it here, and then tell the course about the teacher at the other end. Every change has to be made twice and kept in step, or the model lies.

@chapter A timetable
@math heading="timetable, before" items="5 associations, all two-way@five associations;;10 navigable directions@ten;;2 many-to-many · 6 many ends@six many ends"
The lab takes a school timetable. Five associations, all two way: a school's teachers, teachers and courses, a room's courses, students and courses, and a student's locker. That's ten navigable directions, two many to many associations, and six many ends.

@art timetable-after
Now apply the moves. School to teachers, and teacher to courses, go one way, because the timetable's printed per teacher. The room's courses go one way, qualified by period. Students and courses stay two way, because the school needs class lists and each student's timetable. And the locker goes.

@code block=2 lines=1-15 label=Java focus="3@a map|5-7@courseAt|10-12@room taken"
The qualified link becomes a map from period to course. Ask for courseAt a period and you get one course, not a collection. And booking a second course into the same period fails: room taken.

@math heading="timetable, after" items="4 associations@four associations;;5 directions · 5 many ends@five navigable;;2 many-to-many@two many to many;;two-way links: 5 → 1@from five to one"
After the moves, the lab counts four associations, five navigable directions, two many to many associations, and five many ends. And the two way links fall from five to one.

@words text="directions only: 10 → 6" sub="many-to-many and many ends unchanged"
Apply only the first move, directions, and the directions drop from ten to six, while the many ends stay at six. The many to many count doesn't move at all, because the lab counts ends as declared. Each move shows in a different tile.

@chapter What counts can't say
@art reasons-not-counts
The counts measure the implementation's burden. But the reasons for each move, that timetables are printed per teacher, and a room holds one class at a time, are facts about the school that no count supplies.

@chapter Where people slip
@list heading="Common slips" items="Make every link two-way@The first|Pick a direction for code convenience@The second|Treat a qualifier as a trick@And the third"
The first slip is making every association two way, so any question can be answered. The second is choosing a direction because one table has the foreign key. And the third is treating a qualifier as an implementation trick. It states a rule of the domain.

@chapter Try it
@words text="City · Dock · Bike · Member · Ride" sub="five two-way links"
Your turn. A bike-share with five two way links between city, dock, bike, member and ride. Apply the moves in the lesson, and count the associations, directions, many to many links and many ends before and after. Then pick a one way link, and say what question would need the other direction.

@end text="Count the directions"
Check your counts in the lab, on Learn. That's learn dot get er done dot I O.
