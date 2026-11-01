"""Large-Scale Structure and Strategy, lesson 6 -- Chapter 17 and the Conclusion.

Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004): Chapter 17, Who Sets the Strategy?, Six Essentials for
Strategic Design Decision Making and the sections after them; the Conclusion,
Epilogues and Looking Forward. Pages in the comments are PDF pages of the
operator's copy; the lesson cites by chapter and section. Every quotation is
copied from that copy and checked with quotes.py. The context maps in the lab
are written for this lesson (a school, a bike-share); the book's projects are
summarised in prose only. The design is docs/domain-driven-design/PLAN.md,
section C, Course 9.
"""


# A school's systems as one context map. Records: upstream, downstream, kind.
SCHOOL_CONTEXTS = "enrolment timetable rooms staff-records parent-portal exam-board cafeteria"
SCHOOL_RELS = (
    "enrolment, timetable, customer-supplier; "
    "rooms, timetable, shared-kernel; "
    "staff-records, timetable, acl; "
    "timetable, parent-portal, ohs; "
    "exam-board, enrolment, published-language; "
    "enrolment, parent-portal, conformist; "
    "timetable, cafeteria, separate-ways"
)


LESSONS = [
    # ---------------------------------------------------------------- 06
    # Chapter 17, Who Sets the Strategy? (PDF pp. 305-306 of the operator's
    # copy), Six Essentials for Strategic Design Decision Making (pp. 306-308),
    # The Same Goes for the Technical Frameworks, Don't Write Frameworks for
    # Dummies, Beware the Master Plan (pp. 308-309); Conclusion, Epilogues
    # (pp. 310-313), Looking Forward (pp. 313-314).
    # Quotes: PDF p. 308 of the operator's copy, 10 words, quotes.py OK;
    # PDF p. 312, 12 words, quotes.py OK. Lesson total: 22 words.
    {
        "slug": "who-sets-the-strategy",
        "title": "Who Sets the Strategy, and a Conclusion",
        "module": "Chapter 17 · Bringing the Strategy Together",
        "one_line": "Strategy that grows out of application development, the six essentials Evans asks of any way of deciding it, and the book's closing stories.",
        "summary": (
            "The rest of Chapter 17 asks who should make strategic design decisions, "
            "and the Conclusion follows five of Evans's projects years later. Read his "
            "two workable arrangements, his six essentials and his warning against the "
            "master plan; then read a school's context map the way a team would, by "
            "following one change across it."
        ),
        "key": [
            "strategy grows from application work",
            "decisions must reach the whole team",
            "the process must absorb feedback",
            "the plan must allow for evolution",
            "keep strong designers on every team",
            "minimalism, humility, generalists",
        ],
        "key_label": "Who sets the strategy, in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the third "
            "the lab's."
        ),
        "concepts": [
            ("Emergent structure",
             "Strategy arrived at by the application developers themselves, following "
             "Evolving Order, usually with one hands-on member or an informal committee "
             "of teams keeping it unified."),
            ("Customer-focused architecture team",
             "An architecture team that works as a peer of the application teams, "
             "discovering patterns with them and writing code, rather than handing "
             "down designs."),
            ("Reach of a change on the map",
             "In the lab, the contexts whose models must change when one context's model "
             "changes, following the relationships that pass a change on and stopping "
             "at the ones that translate it."),
        ],
        "read_title": "Who decides, the six essentials, the book's ending, then the map",
        "read_intro": (
            "Read Chapter 17 from Who Sets the Strategy? to its end, and the Conclusion, "
            "in your own copy first. The lesson reads the chapter as Evans's argument "
            "about people and the Conclusion as his stories, and then follows one change "
            "across a context map."
        ),
        "body": [
            ("p", "&ldquo;Make the objects into specialists; let the developers be "
                  "generalists.&rdquo; It is the last of the six essentials in Chapter 17's "
                  "Who Sets the Strategy?, and close to the last word of the book's argument. "
                  "This lesson reads that section, the sections after it, and the "
                  "Conclusion. Read them in your own copy first."),
            ("p", "Architecture, Evans observes, is traditionally handed down: made before "
                  "development starts, by a team with more organisational power than the "
                  "application developers. It need not be, and he says it usually does not "
                  "work well. Strategic design must apply across the project, and without "
                  "prescribing one organisation he describes two arrangements he has seen "
                  "work, setting aside the one he calls wisdom from on high."),
            ("p", "The first is emergent structure from application development. A "
                  "team that keeps its own discipline and communicates very well can follow Evolving "
                  "Order to shared principles without central authority, as Extreme "
                  "Programming teams do. Usually one person, or a few, takes some "
                  "oversight of the structure, and it works best when that person is a "
                  "developer who writes code and who arbitrates and explains, rather than the only "
                  "source of ideas. Across several teams an informal committee of their "
                  "representatives can adopt, modify or shelve a proposal, which works "
                  "when the teams are few, committed to coordinating, comparable in design "
                  "skill and similar in their structural needs."),
            ("p", "The second is a customer-focused architecture team: when several teams "
                  "share a strategy, some centralisation is attractive, and the ivory "
                  "tower is not the only form it can take. Such a team works as a peer of "
                  "the application teams, discovering patterns with them, experimenting "
                  "with them toward distillations, and getting its hands dirty. On an "
                  "organisation chart it may look like the traditional team; in every "
                  "activity it differs."),
            ("p", "Then come the six essentials, which Evans says any way of deciding "
                  "needs. Decisions must reach the entire team, and what matters is the "
                  "developers' actual relation to the strategy, not the authority "
                  "management grants it; architects without feedback from applying their "
                  "own rules are ignored or bypassed. The decision process must absorb "
                  "feedback, because only the application developers know the project "
                  "deeply enough; one architecture team he describes rotated its members "
                  "through the application teams to get it. The plan must allow for "
                  "evolution, since decisions set in stone leave a team few options when "
                  "things change."),
            ("p", "Architecture teams must not take all the best and brightest, which "
                  "leaves applications to the least experienced designers and cuts the "
                  "architects off from developers with deep domain knowledge; strong "
                  "designers belong on every application team. Minimalism and humility "
                  "are essential, because even a slight misfit gets in the "
                  "way, and Evans admits to having built an overbuilt architecture "
                  "himself. And objects are specialists while developers are "
                  "generalists: the narrow responsibilities good objects need are no model "
                  "for a team, on which architects write application code and developers "
                  "play with frameworks."),
            ("p", "The same holds, he says, for technical frameworks: evolution, minimalism "
                  "and involvement with application teams keep a framework helpful, and an "
                  "architecture that ignores them is stifling or bypassed. He singles out "
                  "frameworks built on the assumption that application developers cannot "
                  "design, which underrate how hard application work is; his test is to ask "
                  "the framework's designers what they expect of its users. The chapter "
                  "closes with Christopher Alexander's group of building architects, whose "
                  "account in The Oregon Experiment of why master plans fail, too rigid to "
                  "adapt and alienating the people who live with them, leads them to "
                  "principles that every act of piecemeal growth applies, so that an "
                  "organic order emerges."),
            ("p", "The Conclusion's Epilogues follow five of Evans's projects years later, "
                  "and they are summarised here only. The circuit-board tool of Chapter 1 "
                  "outlived its company in a few engineers' hands; the lending system of "
                  "Chapter 9 kept growing after a spin-off and leads its field. A utility "
                  "with an Abstract Core was handed to a new team that first kept its "
                  "design alive and later rebuilt it around deeper insight, and Evans is "
                  "unsentimental about it: &ldquo;The success of a design is not "
                  "necessarily marked by its stasis.&rdquo; The shipping project behind "
                  "the book's examples was hurt by a culture that resisted iteration and "
                  "fossilised into legacy, though its shared language still held the "
                  "system together. And Evant, an inventory-management software company cut "
                  "to four developers after the dot-com crash, survived because a supple "
                  "design let those four scale the product for one of the world's largest "
                  "retailers."),
            ("p", "What makes a project domain-driven, Evans ends, is not using every "
                  "technique but putting understanding of the domain first: attention to "
                  "language, dissatisfaction with the model as learning continues, "
                  "refinement treated as opportunity, design skill taken seriously. "
                  "Looking Forward compares the messiness of business domains to the "
                  "complex systems the sciences have learned to take seriously, asks for "
                  "tools that extend skilled developers rather than replace their "
                  "thinking, and insists that good software is a matter of learning and "
                  "thought."),
            ("p", "Now the lab, the kind of reading a team does together. A school's "
                  "systems are seven contexts on one map; each relationship is written "
                  "upstream first, with the book's name for its kind:"),
            ("ul", [
                "enrolment supplies timetable as customer and supplier",
                "rooms and timetable share a kernel",
                "timetable reads staff-records through an anticorruption layer",
                "timetable serves parent-portal as an open host service",
                "exam-board publishes a published language that enrolment reads",
                "parent-portal conforms to enrolment",
                "timetable and cafeteria go separate ways",
            ]),
            ("p", "On the preset <code>enrolment-changes</code> the enrolment model changes. "
                  "The lab follows the edges that pass a change on: timetable, as "
                  "enrolment's customer, and parent-portal, as its conformist, must change; "
                  "timetable's shared kernel carries the change on to rooms, 3 models in "
                  "all. Timetable's open host service to parent-portal is a translator "
                  "timetable updates, 1, and cafeteria, staff-records and exam-board, 3 "
                  "contexts, are untouched; the lab counts the 3 models as the contexts "
                  "reached. The table shows what the change does on each "
                  "of the seven relationships."),
            ("p", "The preset <code>staff-records-changes</code> changes the system the "
                  "school bought for staff records. The anticorruption layer absorbs it: 1 "
                  "translator to update, timetable's layer in front of staff-records, 0 "
                  "models that must change, timetable the 1 context reached, at its "
                  "layer and nowhere else, and the other 5 untouched. That difference is the result of a decision someone "
                  "took, to put a translator in front of a model the school does not "
                  "control, and the six essentials are about who takes such decisions "
                  "and whether the whole team knows they were taken."),
            ("h3", "Exercise"),
            ("ul", [
                "A bike-share's map: payment-provider is upstream of rentals, which reads "
                "it through an anticorruption layer; rentals and maintenance share a "
                "kernel; city-reporting conforms to rentals.",
                "The rentals model changes.",
            ]),
            ("p", "By hand, find the models that must change, the translators to update, "
                  "and the contexts untouched. Then draw the map of a project you work on "
                  "with the book's kinds, type it into the lab, change its most central "
                  "context, and compare the reach with what your team would have guessed."),
            ("p", "That is the end of the read-along. The book's Appendix on the use of "
                  "patterns and its Glossary are worth keeping beside you; for the "
                  "patterns this book shares with Fowler's, the Enterprise Application "
                  "Patterns read-along in this library reads them from the other side, "
                  "the side of the database and the layers."),
        ],
        "lab": ("dddkit", {
            "mode": "context",
            "view": "map",
            "preset": "enrolment-changes",
            "presets": [
                {"id": "enrolment-changes",
                 "label": "A school's map, with the enrolment model changing",
                 "contexts": SCHOOL_CONTEXTS,
                 "rels": SCHOOL_RELS,
                 "changed": "enrolment",
                 "expect": {"dcxRels": "7",
                            "dcxModels": "3: timetable, rooms, parent-portal",
                            "dcxTranslators": "1: timetable’s protocol",
                            "dcxReached": "3: timetable, rooms, parent-portal",
                            "dcxUntouched": "3: staff-records, exam-board, cafeteria"}},
                {"id": "staff-records-changes",
                 "label": "The same map, with the bought staff-records model changing",
                 "contexts": SCHOOL_CONTEXTS,
                 "rels": SCHOOL_RELS,
                 "changed": "staff-records",
                 "expect": {"dcxModels": "0: none",
                            "dcxTranslators": "1: timetable’s ACL from staff-records",
                            "dcxReached": "1: timetable",
                            "dcxUntouched": "5: enrolment, rooms, parent-portal, exam-board, cafeteria"}},
            ],
            "panel_title": "How far one change reaches on a context map",
            "panel_intro": (
                "A count over the small model the lesson states. Each relationship is "
                "written upstream first with one of the book's kinds; the lab follows the "
                "kinds that pass a change on and stops at those that translate it. The map "
                "is the lesson's, not the book's."
            ),
        }),
        "steps_title": "Reading a map as a team",
        "steps_intro": "Four steps, the last of them on your own project.",
        "steps": [
            ("Write every relationship with its kind",
             "Name the upstream and downstream context and one of the book's kinds. A "
             "relationship nobody can classify is a finding to discuss, not to guess."),
            ("Follow one change",
             "From the changed context, pass the change along customer-supplier and "
             "conformist edges downstream and along shared kernels both ways; stop at "
             "anticorruption layers, open host services and published languages, and "
             "count the translators there."),
            ("Name who decided each stop",
             "For each translator that stopped the change, say who chose to build it and "
             "whether the teams on both sides know it is there."),
            ("Do it on your own project",
             "Draw your project's map, change its most central context in the lab, and "
             "write down how many models the lab says must change against how many your "
             "team would have guessed."),
        ],
        "worked": {
            "title": "Enrolment changes",
            "intro": [
                "Follow <code>enrolment-changes</code> by hand.",
            ],
            "lines": [
                "to timetable, customer: must change",
                "to parent-portal, conformist: must change",
                "timetable's kernel: rooms must change",
                "timetable's open host: 1 translator",
                "exam-board is upstream: untouched",
                "staff-records, cafeteria: untouched",
            ],
            "after": [
                "Three models change and one translator is updated. Parent-portal is "
                "reached twice, once as a conformist and once through the open host "
                "service, and is counted once.",
            ],
        },
        "quiz_title": "Who decides, and how the book ends",
        "quiz": [
            {"q": "In the bike-share exercise, with the rentals model changing, by the lab's "
                  "rule (a translator is counted where a change arrives from upstream), how "
                  "many models must change, how many translators are updated, and how many "
                  "contexts are untouched?",
             "a": ["2 models, 0 translators, 1 untouched",
                   "3 models, 0 translators, 0 untouched",
                   "2 models, 1 translator, 1 untouched",
                   "1 model, 0 translators, 2 untouched"],
             "c": 0,
             "why": "Maintenance shares a kernel with rentals and city-reporting conforms to "
                    "it: 2 models must change. The anticorruption layer sits between "
                    "payment-provider and rentals with payment-provider upstream, so a "
                    "change in rentals does not cross it: no translator, and "
                    "payment-provider is the 1 context untouched. The lab does not count "
                    "rentals' own ACL, because the change did not come from "
                    "payment-provider. In a real system that layer translates into "
                    "rentals' model and may well need updating, which is one of the things "
                    "a team reading the map should ask."},
            {"q": "Which of these is one of Evans's six essentials for strategic design "
                  "decision making?",
             "a": ["Architecture must be finished before application development begins",
                   "The decision process must absorb feedback",
                   "Strategy must be set by the team with the most authority",
                   "Developers should specialise as narrowly as objects do"],
             "c": 1,
             "why": "The six are: decisions must reach the entire team; the process must "
                    "absorb feedback; the plan must allow for evolution; architecture teams "
                    "must not take all the best and brightest; strategic design requires "
                    "minimalism and humility; and objects as specialists with developers as "
                    "generalists. The other three options are what he argues against."},
            {"q": "When does Evans say an informal committee of team representatives can "
                  "work for a structure spanning several teams?",
             "a": ["When there is a separate architecture team to overrule it",
                   "Whenever the teams share one Bounded Context",
                   "When the teams are few, committed to coordinating, comparable in design skill and similar in needs",
                   "Only on Extreme Programming projects"],
             "c": 2,
             "why": "Those four conditions are his. The committee is a form of emergent "
                    "structure, so it needs no architecture team, and the teams may work "
                    "in different contexts; Extreme Programming is where he has seen "
                    "single-team emergent leadership, not a condition."},
            {"q": "What does Evans conclude from the utility whose design a later team "
                  "rebuilt around new insight?",
             "a": ["That the original design had failed",
                   "That a design's success is not necessarily shown by its staying unchanged",
                   "That an Abstract Core should never be handed to another team",
                   "That a distillation document prevents later redesign"],
             "c": 1,
             "why": "He says he is not sentimental about his designs, and that a deep model "
                    "and supple design are valuable because they allow new insight and "
                    "change; the new model was deeper and solved real problems. The "
                    "distillation document had helped the new team, not stopped it."},
        ],
        "mistakes": [
            ("Concluding that Evans rejects architecture teams",
             "He rejects the ivory tower, not the team. A customer-focused architecture "
             "team that works as a peer of the application teams, discovers patterns with "
             "them and writes code is one of the two arrangements he has seen work, and "
             "the six essentials apply to it as much as to an emergent structure."),
            ("Moving the strongest designers into strategy so that their decisions are good",
             "The fourth essential is the opposite: a strategy team that takes all the "
             "best designers leaves application teams unable to follow even a good "
             "strategy, and loses touch with developers who know the domain. Evans asks "
             "for strong designers on every application team and domain knowledge on any "
             "team doing strategic design."),
            ("Reading the lab's reach as the cost of a change",
             "The lab counts which models must change and which translators are updated "
             "on the map you give it, by the book's kinds. On the lesson's illustration "
             "it treats every edge of a kind alike; a real conformist may be barely "
             "affected, and a real translator may be a week's work. Who decides, and "
             "whether the team knows, are what the chapter is about."),
        ],
        "standard": (
            "Finish when you can follow a change across a context map.",
            "Given a map with the book's kinds and one changed context, name the models "
            "that must change, the translators to update and the contexts untouched, and "
            "say which decision placed each translator."
        ),
        "note": (
            "The lab follows one change across the map you give it, by the kind of each "
            "relationship. It cannot tell you who should decide your strategy, whether "
            "the team knows the decisions taken, or whether the map is true; Evans's six "
            "essentials are about people, and no map counts them."
        ),
    },
]
