---
format: long
lesson: ddd-large-scale-structure/who-sets-the-strategy
title: Who Sets the Strategy? Evans's six essentials, and how the book ends
thumb: Developers as generalists
---

@chapter Not from on high
@title text="Who Sets the Strategy, and a Conclusion" sub="Domain-Driven Design, Chapter 17" art=thumb
Architecture is traditionally handed down. It's made before development starts, by a team with more organisational power than the application developers. It needn't be, Evans says, and it usually doesn't work well. He describes two arrangements he's seen work.

@art emergent-structure
The first is emergent structure from application development. A team with its own discipline and very good communication can follow Evolving Order to shared principles without central authority. Usually one person takes some oversight, ideally a developer who writes code, and who arbitrates and explains, rather than being the only source of ideas.

@art peer-architects
Across several teams, an informal committee of their representatives can work, if the teams are few, committed, and similar. The second arrangement is a customer focused architecture team, working as a peer of the application teams. It discovers patterns with them, and gets its hands dirty.

@chapter Six essentials
@list heading="Any way of deciding needs" items="Decisions reach the entire team@entire team|The process absorbs feedback@absorb feedback|The plan allows for evolution@evolution|Don't take all the best and brightest@best and brightest|Minimalism and humility@humility|Objects specialists, developers generalists@about people"
Then come six essentials. Decisions must reach the entire team. The process must absorb feedback, because only application developers know the project deeply enough. The plan must allow for evolution. Architecture teams mustn't take all the best and brightest. Minimalism and humility are essential. And the last one is about people.

@quote text="Make the objects into specialists; let the developers be generalists." cite="Evans, Domain-Driven Design, Chapter 17"
Make the objects into specialists; let the developers be generalists. The narrow responsibilities good objects need are no model for a team. Architects write application code, and developers play with frameworks.

@art master-plan
The same holds for technical frameworks. Evans singles out frameworks built on the assumption that application developers can't design. And the chapter closes with Christopher Alexander's architects, who found that master plans fail, too rigid to adapt, and turned instead to principles every act of piecemeal growth applies.

@chapter Epilogues
@art five-projects
The conclusion follows five of Evans's projects, years later. A circuit board tool outlived its company. A lending system kept growing and leads its field. And a utility with an abstract core was handed to a new team that kept its design alive, then rebuilt it around deeper insight.

@quote text="The success of a design is not necessarily marked by its stasis." cite="Evans, Domain-Driven Design, Conclusion"
Evans is unsentimental about that. The success of a design is not necessarily marked by its stasis. And an inventory company, cut to four developers after the dot com crash, survived because a supple design let those four scale the product.

@words text="Understanding the domain comes first"
What makes a project domain driven isn't using every technique. It's putting understanding of the domain first. Attention to language, dissatisfaction with the model as you learn, and design skill taken seriously.

@chapter A school's map
@art school-map
Now the kind of reading a team does together: a school's systems, seven contexts on one map, each relationship written with the book's name for its kind.

@list heading="Seven contexts" items="enrolment → timetable: customer and supplier@customer and supplier|rooms ↔ timetable: shared kernel@share a kernel|staff-records → timetable: anticorruption layer@anticorruption layer|timetable → parent-portal: open host@open host|parent-portal conforms to enrolment@conforms"
Enrolment supplies the timetable as customer and supplier. Rooms and timetable share a kernel. The timetable reads staff records through an anticorruption layer, and serves the parent portal as an open host. The parent portal conforms to enrolment. The exam board publishes a language, and the cafeteria goes its separate way.

@math heading="enrolment-changes" items="must change: timetable, parent-portal, rooms = 3@three models;;translators: 1 · untouched: 3@one translator"
When enrolment's model changes, the timetable and the parent portal must change, and the timetable's kernel carries it on to rooms. Three models. The open host service is one translator to update. And three contexts are untouched.

@art layer-absorbs
Now change the bought staff records system instead. The anticorruption layer absorbs it: one translator, no models changed, and the other five untouched. That difference is a decision someone took, and the six essentials are about who takes such decisions, and whether the whole team knows.

@chapter Where people slip
@list heading="Common slips" items="Evans rejects architecture teams@The first|Moving the strongest into strategy@The second|Reading reach as cost@And the third"
The first slip is concluding that Evans rejects architecture teams. He rejects the ivory tower. The second is moving the strongest designers into strategy. And the third is reading the lab's reach as the cost of a change.

@chapter Try it
@words text="A bike share's map: rentals changes" sub="payment provider · maintenance · city reporting"
Your turn. A bike share's map: a payment provider upstream of rentals, read through an anticorruption layer. Rentals and maintenance share a kernel, and city reporting conforms to rentals. The rentals model changes. Find the models that must change, the translators to update, and the contexts untouched.

@end text="Understanding the domain comes first"
Then draw your own project's map in the lab, on Learn. That's learn dot get er done dot I O.
