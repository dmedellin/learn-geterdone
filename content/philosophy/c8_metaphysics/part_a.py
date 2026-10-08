"""Course 8, lessons 1 to 6: modality, and the ship of Theseus.

Five modal lessons (necessity at a world, frames and axioms, the scope fallacy of
the sea battle, the ontological argument in S5, Leibniz's law and the masked man)
and then the first lesson on identity over time.

The `kripke` lab ships `at = 1` and its box is read alethically unless a lesson
says otherwise. A world that sees no world makes every box vacuously true, and
the lessons that use such worlds say so where it matters.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "necessity-possibility-and-possible-worlds",
        "title": "Necessity, Possibility and Possible Worlds",
        "module": "Modality",
        "one_line": "A claim of necessity is a claim about every world a given world can see, and what it can see is part of the model.",
        "summary": (
            "&ldquo;Necessarily p&rdquo; is not &ldquo;p and certainly p&rdquo;. In a possible-worlds model it is true at a "
            "world when p holds at every world that world can see, and &ldquo;possibly p&rdquo; when p holds at some such "
            "world. Compute both from a list of worlds, arcs and atoms, and watch one added arc change the verdict."
        ),
        "key": [
            "□p at w: p at every world w sees",
            "◇p at w: p at some world w sees",
            "w sees nothing: □p true, ◇p false",
            "same worlds, other arcs: other verdict",
        ],
        "key_label": "Necessity is relative to what a world sees",
        "concepts_intro": (
            "Modal logic adds two words to the logic of Arguments and Validity, necessarily and possibly, and "
            "gives them a meaning by quantifying over worlds. Everything in this course that mentions "
            "necessity uses this one rule."
        ),
        "concepts": [
            ("A model is worlds, arcs and atoms",
             "A world is a complete way things could be, and the model says which simple sentences are true "
             "at each. An arc from one world to another says the second is possible as seen from the first. "
             "Nothing else is in the model."),
            ("The box and the diamond quantify over what a world sees",
             "At a world, `□p` is true when `p` is true at every world it sees, and `◇p` when `p` is true "
             "at some world it sees. The first is a universal claim and the second an existential one, over "
             "the seen worlds only."),
            ("Necessity depends on the arcs",
             "Hold the atoms fixed and change who sees whom, and `□p` can change from true to false. So "
             "necessity is never a property of `p` alone; it is a property of `p` and a model."),
        ],
        "read_title": "Evaluating a box and a diamond",
        "read_intro": "The rule, a model in which it gives a surprising answer, and the case where a world sees nothing.",
        "body": [
            ("def", ("Possible-worlds model",
                     "A <strong>model</strong> is a set of worlds, an <strong>accessibility relation</strong> "
                     "saying which worlds each world can see, and a <strong>valuation</strong> saying which "
                     "sentence letters are true at which world. A formula is evaluated <em>at a world</em>; the "
                     "same formula can be true at one world and false at another.")),
            ("p", "The connectives of “Truth Values and the Connectives” work world by world, exactly as "
                  "before. The two new operators are the only part that looks beyond the world being "
                  "evaluated, and they look only at the worlds it sees."),
            ("math", [
                "□p is true at w   iff   p is true at every world w sees",
                "◇p is true at w   iff   p is true at some world w sees",
            ]),
            ("p", "Take a model with two worlds. World w1 sees w2 and nothing else, and the letter `p` is "
                  "true at w2 only. At w1 the box asks about the one world w1 sees, w2, and `p` is true "
                  "there, so `□p` is true at w1. But `p` is not true at w1 itself. That is the surprise the "
                  "lesson is built around: <strong>necessity without truth</strong>. In this model `p` is "
                  "necessary as seen from w1 and false at w1."),
            ("p", "The reading &ldquo;necessarily p means p is true and certain&rdquo; fails here for both of "
                  "its halves. Certainty is a fact about someone&rsquo;s evidence and the model has no "
                  "believers in it. Truth at the world itself is not guaranteed either, because w1 does not "
                  "see itself. Give w1 an arc to w1 and the guarantee returns: the box now includes the "
                  "world being evaluated, `p` is false there, and `□p` is false. This is the first appearance "
                  "of a fact the next lesson turns into a table: whether necessity implies truth depends on "
                  "whether worlds see themselves."),
            ("h3", "A world that sees nothing"),
            ("p", "The rule for the box is a universal claim over the worlds seen. A universal claim over "
                  "no worlds has nothing to fail it, so it is true. If w1 sees no world at all, then "
                  "`□p` is true at w1 for every `p`, including a `p` that is false everywhere, and `◇p` is "
                  "false for every `p`, since there is no seen world at which to find it. The two operators "
                  "are linked by `◇p ≡ ¬□¬p`, and at a world that sees nothing the pair behaves as the lab "
                  "shows: necessarily true and possibly false together."),
            ("example", ("Same atoms, different arcs",
                         "Two worlds, `p` true at w2 only. If w1 sees only w2, then `□p` is true at w1. If "
                         "w1 also sees itself, then `□p` is false at w1. The valuation did not change. One "
                         "arc did.")),
            ("p", "The lab quantifies over the worlds you give it, and the arcs are your choice. Whether the "
                  "arcs for logical necessity, for what is known, or for what is permitted should look one "
                  "way or another is a question about those subjects, and the lab leaves it open. What it "
                  "settles is the consequence: given these arcs, this is the verdict."),
        ],
        "lab": ("argkit", {
            "mode": "kripke",
            "at": 1,
            "reading": "alethic",
            "preset": "two-worlds",
            "presets": [
                {"id": "two-worlds", "label": "w1 sees only w2, where p holds",
                 "n": 2, "access": [[1, 2]], "valuation": {"p": [2]}, "formula": "[]p",
                 "expect": {"krValue": "True at w1", "krWorlds": "all"}},
                {"id": "blind", "label": "w1 sees no world",
                 "n": 2, "access": [], "valuation": {"p": [2]}, "formula": "[]p & ~<>p",
                 "expect": {"krValue": "True at w1", "krWorlds": "all"}},
                {"id": "self", "label": "w1 sees itself and w2",
                 "n": 2, "access": [[1, 1], [1, 2], [2, 2]], "valuation": {"p": [2]}, "formula": "[]p",
                 "expect": {"krValue": "False at w1", "krWorlds": "w2"}},
            ],
            "panel_title": "Move one arc and read the box",
            "panel_intro": "The first model has the arc from w1 to w2 and `p` at w2. The formula box is written with two square brackets for the box and a less-than and greater-than for the diamond. Add the arc `1-1` to the arcs and watch the value at w1 change while the atoms stay where they are.",
        }),
        "steps_title": "Evaluating a modal formula at a world",
        "steps_intro": "Five moves, in this order. The third is where most mistakes happen.",
        "steps": [
            ("List the worlds and what is true at each",
             "Write every world with the sentence letters it makes true. A letter not listed at a world "
             "is false there."),
            ("List the arcs",
             "For each world write the worlds it sees. Check whether a world sees itself, and whether "
             "any world sees nothing."),
            ("Collect the worlds the evaluated world sees",
             "Only these are consulted. A world the evaluated world cannot see is irrelevant to its "
             "box, however true or false `p` is there."),
            ("Apply the quantifier",
             "For a box, `p` must hold at every collected world, and at a world that sees nothing it "
             "holds vacuously. For a diamond, `p` must hold at one collected world, and at a world "
             "that sees nothing it fails."),
            ("Compare with the world itself",
             "Read `p` at the evaluated world. If the box is true and `p` is false, necessity has "
             "come apart from truth, and the cause is an arc that is missing."),
        ],
        "worked": {
            "title": "Necessity without truth",
            "intro": ["Two worlds. The arc runs from w1 to w2, and p is true at w2 only."],
            "lines": [
                "w1 sees: w2",
                "p at w2: true",
                "so the box of p at w1: true",
                "p at w1 itself: false",
                "the box is true and p is false",
                "now add the arc from w1 to w1",
                "w1 sees: w1, w2",
                "p at w1: false, so the box of p at w1: false",
            ],
            "after": [
                "The first verdict is the one a reader finds odd, and the lab prints it. The second shows "
                "what repaired it. When a world sees itself, the box includes the world being evaluated, "
                "and the odd case disappears."
            ],
        },
        "quiz_title": "Boxes and diamonds at a world",
        "quiz": [
            {"q": "World w1 sees only w2. The letter `p` is true at w2 and false at w1. What is the value of `□p` at w1?",
             "a": ["False, because p is false at w1",
                   "True, because p is true at every world w1 sees",
                   "Undefined, because w1 does not see itself",
                   "False, because w1 sees only one world"],
             "c": 1,
             "why": "The box consults the worlds w1 sees, and that is w2 alone, where `p` holds. What `p` does at w1 is irrelevant unless w1 sees itself. The value is defined whatever the arcs are, and seeing one world is no obstacle to a universal claim being true."},
            {"q": "World w sees no world at all. Which pair of verdicts holds for every sentence letter `p`?",
             "a": ["`□p` false and `◇p` false",
                   "`□p` true and `◇p` true",
                   "`□p` undefined and `◇p` false",
                   "`□p` true and `◇p` false"],
             "c": 3,
             "why": "A box over no worlds has no failing world, so it is true; a diamond over no worlds has no witnessing world, so it is false. A false box would need a seen world where `p` fails, and a true diamond would need one where `p` holds. The rule yields a value in every case."},
            {"q": "Which statement is exactly what makes `□p` true at a world in the lab?",
             "a": ["`p` is true at every world that world sees",
                   "`p` is true at that world and at some world it sees",
                   "`p` is true at every world in the model",
                   "Someone is certain that `p`"],
             "c": 0,
             "why": "The rule quantifies over the worlds seen. The second choice mixes the box with the diamond; the third is the special case in which the world sees every world, and the fourth is an epistemic reading, which needs someone whose evidence is in the model."},
            {"q": "In the first model, p is true at w2 only and w1 sees w2. The arc from w1 to w1 is added. What happens to `□p` at w1?",
             "a": ["It stays true, because arcs to w1 do not affect w1",
                   "It becomes true, because a world that sees itself satisfies the box",
                   "It becomes false, because w1 now sees a world where p fails",
                   "It becomes undefined"],
             "c": 2,
             "why": "After the arc, w1 sees w1 as well as w2, and `p` is false at w1, so the universal claim fails. The first choice forgets that an arc to w1 puts w1 among the worlds it sees, and no arc makes a world satisfy a box it would otherwise fail."},
        ],
        "mistakes": [
            ("Reading “necessarily p” as “p is true and certain”",
             "In the two-worlds model `□p` is true at w1 and `p` is false at w1, so necessity does not even "
             "bring truth with it until the world sees itself. And no one in the model is certain of "
             "anything, since the model contains worlds, arcs and atoms and no believers. Certainty "
             "belongs to the epistemic reading, where the arcs are drawn from what someone knows."),
            ("Thinking a world that sees nothing makes the box false",
             "The box is a universal claim and a universal claim over nothing is true. The lab prints it: at w1 "
             "in the second preset, which sees nothing, `□p` is true although `p` holds only at a world "
             "w1 cannot see, and `◇p` is false. The surprising value is the one the rule gives."),
            ("Treating necessity as a property of the sentence alone",
             "The valuation of `p` is the same in the first and third presets, and the value of `□p` at w1 "
             "differs between them. The difference is one arc. A claim that something is necessary is a "
             "claim about it relative to a model, and a debate about necessity is partly a debate about "
             "which arcs to draw."),
        ],
        "standard": (
            "Finish when you can compute a box and a diamond from a diagram, and say which arc changed the verdict.",
            "Given worlds, arcs and a valuation, you should be able to state the value of `□p` and `◇p` at a "
            "named world, including a world that sees nothing, and to say which single added or removed arc "
            "turns a true box into a false one. A verdict stated without the list of worlds it consulted has "
            "not yet been computed."),
        "note": "The lab&rsquo;s status line says what the box is read as. Change the reading menu to epistemic or deontic and only the words change; the computation does not. That is the point of the lesson: one rule for the quantifier, and the subject matter enters through the arcs.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "frames-axioms-and-what-necessity-obeys",
        "title": "Frames, Axioms and What Necessity Obeys",
        "module": "Modality",
        "one_line": "Each of the modal axioms T, D, B, 4 and 5 is the fingerprint of one property of the arcs.",
        "summary": (
            "Drop the valuation and keep only the worlds and arcs: that is a frame. An axiom is valid on a "
            "frame when it is true at every world under every valuation. The lab computes which of five "
            "axioms a frame validates and which of five properties it has, so the match between them is "
            "something you read off a tile and not something you are told."
        ),
        "key": [
            "T  □p → p     every world sees itself",
            "D  □p → ◇p    every world sees a world",
            "B  p → □◇p    seeing goes both ways",
            "4  □p → □□p   seeing passes through",
            "5  ◇p → □◇p   worlds seen share a view",
        ],
        "key_label": "Five axioms, five properties of the arcs",
        "concepts_intro": (
            "The previous lesson fixed the meaning of the box for one model. This one asks what the box "
            "obeys across all the models that share a set of arcs."
        ),
        "concepts": [
            ("A frame is worlds and arcs",
             "A frame has no valuation. An axiom is <strong>valid on a frame</strong> when it is true at every "
             "world of the frame for every way of assigning `p` to the worlds. The lab tests every assignment."),
            ("Each axiom asks for one property of the arcs",
             "T asks that every world see itself. D asks that every world see some world. B asks that "
             "seeing be symmetric, 4 that it be transitive, and 5 that it be euclidean. The lab lists "
             "the properties a frame has beside the axioms it validates."),
            ("The axioms are chosen by choosing the frame",
             "No axiom is a discovery about necessity in general. To say that necessity obeys T is to say "
             "that the arcs of the kind of necessity you mean are reflexive, which is a claim about "
             "that kind of necessity."),
        ],
        "read_title": "From arcs to axioms",
        "read_intro": "The five axioms, the property each corresponds to, and the one that is valid on every frame.",
        "body": [
            ("def", ("Frame and validity on a frame",
                     "A <strong>frame</strong> is a set of worlds and an accessibility relation. A formula is "
                     "<strong>valid on the frame</strong> if it is true at every world under every valuation. "
                     "The formula `□(p → q) → (□p → □q)`, called <strong>K</strong>, is valid on every frame "
                     "and is not listed in the lab.")),
            ("math", [
                "axiom   formula       what the arcs must do",
                "D       □p → ◇p       serial: every world sees some world",
                "T       □p → p        reflexive: every world sees itself",
                "B       p → □◇p       symmetric: if w sees v, then v sees w",
                "4       □p → □□p      transitive: if w sees v and v sees u, then w sees u",
                "5       ◇p → □◇p      euclidean: if w sees v and u, then v sees u",
            ]),
            ("p", "The table is not a list of facts to memorise, because each row can be reasoned out. "
                  "Suppose a world w does not see itself. Make `p` true at every world w sees and false at "
                  "w. Then `□p` is true at w and `p` is false at w, so T fails at w. The other direction "
                  "is as direct: if every world sees itself, then `□p` includes `p` at the world itself, so "
                  "T holds. Transitivity is the same argument one step longer. If w sees v, v sees u and "
                  "w does not see u, make `p` true at everything w sees and false at u. Then `□p` is "
                  "true at w, and `□□p` is false at w, because v sees u."),
            ("p", "B is easy to misread. It does not say that what is true is necessarily true, which would "
                  "be `p → □p`. It says that what is true is necessarily possible: at a world w where `p` holds, "
                  "every world v that w sees must itself see a world with `p`, and symmetry supplies one, "
                  "since v sees w."),
            ("h3", "Which logic is which"),
            ("p", "The frames people reach for have names. A frame that is reflexive and transitive validates "
                  "the system called S4. A frame that is an equivalence relation, reflexive, symmetric and "
                  "transitive, validates S5, and in S5 every world in a group sees every other. Each step "
                  "up the list adds a property, so each adds axioms. What the lab does is compute the "
                  "list for the frame you build, so you can add one arc and see the first axiom that "
                  "appears."),
            ("p", "That is also its limit. A frame that validates all five axioms is a frame, and whether "
                  "it is the right model of logical necessity, of metaphysical necessity or of what a "
                  "person can know is not computed. The next lessons use S5 for one argument and "
                  "ask whether it was a fair choice."),
        ],
        "lab": ("argkit", {
            "mode": "kripke",
            "at": 1,
            "reading": "alethic",
            "preset": "reflexive",
            "presets": [
                {"id": "reflexive", "label": "each world sees itself; w1 sees w2, w2 sees w3",
                 "n": 3, "access": [[1, 1], [2, 2], [3, 3], [1, 2], [2, 3]], "valuation": {"p": [1, 2]},
                 "formula": "[]p -> p", "expect": {"krFrame": "reflexive, serial", "krAxioms": "D, T"}},
                {"id": "s4", "label": "reflexive, and w1 also sees w3",
                 "n": 3, "access": [[1, 1], [2, 2], [3, 3], [1, 2], [2, 3], [1, 3]], "valuation": {"p": [1, 2]},
                 "formula": "[]p -> p", "expect": {"krFrame": "reflexive, serial, transitive", "krAxioms": "D, T, 4"}},
                {"id": "s5", "label": "every world sees every world",
                 "n": 3, "access": [[1, 1], [2, 2], [3, 3], [1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2]],
                 "valuation": {"p": [1, 2]}, "formula": "[]p -> p", "expect": {"krFrame": "reflexive, serial, symmetric, transitive, euclidean", "krAxioms": "D, T, B, 4, 5"}},
                {"id": "serial-only", "label": "w1 sees w2, w2 sees w3, w3 sees w1",
                 "n": 3, "access": [[1, 2], [2, 3], [3, 1]], "valuation": {"p": [2]},
                 "formula": "[]p -> p", "expect": {"krFrame": "serial", "krAxioms": "D", "krValue": "False at w1"}},
            ],
            "panel_title": "Add an arc and read the axiom list",
            "panel_intro": "Each preset is a frame, and the two tiles on the right of the model read off that frame alone: the properties it has, and the axioms it validates. The formula box tests one valuation at one world. Start with the last model and add `1-1 2-2 3-3` to its arcs to watch T appear.",
        }),
        "steps_title": "Reading the axioms off a frame",
        "steps_intro": "Five moves. The first four need only the arcs.",
        "steps": [
            ("Write the arcs and nothing else",
             "Forget the valuation. A frame is judged by who sees whom."),
            ("Check each property by its definition",
             "Reflexive: every world has an arc to itself. Serial: every world has an arc out. Symmetric: "
             "every arc has its reverse. Transitive: every two-step path has a shortcut. Euclidean: every "
             "two arcs leaving the same world are joined by an arc from the first target to the second."),
            ("Pair each property with its axiom",
             "Serial with D, reflexive with T, symmetric with B, transitive with 4, euclidean with 5. A frame "
             "validates an axiom exactly when it has the matching property."),
            ("Name the logic if there is one",
             "Reflexive and transitive is S4. Reflexive, symmetric and transitive is S5."),
            ("Test one valuation if you want a case",
             "To see an axiom fail, type it as the formula, choose the valuation that breaks it, and read "
             "the value at the world the proof used."),
        ],
        "worked": {
            "title": "Growing a frame one arc at a time",
            "intro": ["Four frames on three worlds. The second drops the arc from 3 to 1 and adds the loops; the third and fourth only add arcs."],
            "lines": [
                "cycle, w1 sees w2 sees w3 sees w1:    D",
                "loops, w1 sees w2, w2 sees w3:        D, T",
                "add: w1 sees w3, the shortcut:        D, T, 4",
                "add: every reverse arc:               D, T, B, 4, 5",
            ],
            "after": [
                "Each line was read off the tile, and each new axiom appeared when its property did. Nothing "
                "about necessity was consulted: the axioms followed from the arcs."
            ],
        },
        "quiz_title": "From arcs to axioms",
        "quiz": [
            {"q": "A frame has three worlds in a cycle: w1 sees w2, w2 sees w3, w3 sees w1, and there are no other arcs. Which axiom does it validate?",
             "a": ["T, because necessity implies truth in a cycle",
                   "4, because the cycle is transitive",
                   "D, because every world sees some world",
                   "B, because the cycle returns to where it started"],
             "c": 2,
             "why": "Every world has an arc out, which is seriality, which is D. T needs each world to see itself. The cycle is not transitive: w1 sees w2 and w2 sees w3, but w1 does not see w3. And B needs each arc reversed, while w1 sees w2 and w2 does not see w1."},
            {"q": "The axiom T says that `□p` implies `p`. What must the arcs of a frame do for T to be valid on it?",
             "a": ["Every world must see itself",
                   "Every world must see some world",
                   "Every arc must have its reverse",
                   "Every two-step path must have a shortcut"],
             "c": 0,
             "why": "If every world sees itself, the box includes `p` at the world evaluated. The second is D, the third is B and the fourth is 4. Each is a different condition, and the lab lists them in separate columns."},
            {"q": "On the serial-only frame the formula `□p → p` is false at w1 when `p` is true at w2 only. What does that show?",
             "a": ["That necessity never implies truth",
                   "That the formula is false on every frame",
                   "That the lab has mislabelled the valuation",
                   "That w1 has no arc to itself, so this frame does not validate T"],
             "c": 3,
             "why": "The failure is at one world of one frame, because w1 does not see itself. It says nothing about frames that are reflexive, where the lab finds T valid, and it does not make the formula false everywhere. Nothing is mislabelled; the valuation was chosen to expose the missing arc."},
            {"q": "The s4 preset adds the arc from w1 to w3 to the reflexive one. Which axiom newly appears in the tile, and why?",
             "a": ["T, because there are more arcs",
                   "4, because w1 sees w2 and w2 sees w3, so w1 must see w3",
                   "5, because w1 now sees two worlds",
                   "B, because w1 sees w3 and w3 is in the model"],
             "c": 1,
             "why": "T was already valid, since the loops are there. The arc closes the two-step path from w1 through w2 to w3, and that is what 4 asks for. Seeing two worlds is not enough for 5, which needs the worlds seen to see each other, and B needs reverse arcs, which this frame still lacks."},
        ],
        "mistakes": [
            ("Treating the axioms as truths about necessity that every frame obeys",
             "On the serial-only frame the lab lists D and nothing else: T fails at w1, 4 fails because w1 "
             "does not see w3, and so on. Which of the axioms hold is a fact about the arcs, and the "
             "arcs are what you chose. To claim that necessity obeys T is to claim that the right frame "
             "for it is reflexive, which can be argued for or against."),
            ("Reading B as “what is true is necessarily true”",
             "B is `p → □◇p`, which says what is true is necessarily possible. On the frame where every "
             "world sees every world, B is valid, yet `p → □p` is false at a world where `p` is true "
             "and another seen world lacks it. Symmetry brings the world back into view; it does not "
             "fix its truth values."),
            ("Assuming the frame that validates more axioms is the better model of necessity",
             "The s5 frame validates all five and the serial-only frame only one. That is a "
             "difference in the arcs and not a difference in correctness. Whether the necessity at "
             "issue, in a particular argument, has arcs that are symmetric and transitive is the "
             "question the next lessons ask."),
        ],
        "standard": (
            "Finish when you can read the axiom list off a set of arcs, and add one arc to make a chosen axiom appear.",
            "Given three or four worlds and their arcs, you should be able to state which of reflexive, "
            "serial, symmetric, transitive and euclidean the frame has, name the axioms it therefore "
            "validates, and say which single arc must be added for a named axiom to be valid. A match "
            "stated without the pair of arcs that produces it has not been checked."),
        "note": "The axiom tile checks every assignment of `p` to the worlds, which is why a frame of six worlds is the limit of the lab. The formula tile shows one assignment, so a formula that is true at w1 is not thereby valid on the frame, and the tiles can differ.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "modal-fallacies-and-the-sea-battle",
        "title": "Modal Fallacies and the Sea Battle",
        "module": "Modality",
        "one_line": "From a necessary disjunction it does not follow that one disjunct is necessary, and the fatalist's argument needs that step.",
        "summary": (
            "&ldquo;Necessarily, either there will be a sea battle tomorrow or there will not&rdquo; is true at every world "
            "of every model. &ldquo;Either it is necessary that there will be one, or it is necessary that there will "
            "not&rdquo; is false at a world that sees both kinds of future. The lab evaluates both, and the "
            "difference is where the box sits."
        ),
        "key": [
            "□(p ∨ ¬p)   true at every world",
            "□p ∨ □¬p    false if both p, ¬p seen",
            "the box does not split over ∨",
            "open future: the seen worlds disagree",
        ],
        "key_label": "One box over a disjunction, or one on each side",
        "concepts_intro": (
            "The argument that the future is fixed is an old one, and one version of it has a precise "
            "flaw that a small model shows."
        ),
        "concepts": [
            ("Where the box sits is part of what is said",
             "`□(p ∨ ¬p)` puts one box around the whole disjunction. `□p ∨ □¬p` puts a box on each side. "
             "They are different sentences, and the second is a much stronger claim."),
            ("A logical truth is true at every seen world",
             "`p ∨ ¬p` is true at every world of every model, so it is true at every world a world sees, "
             "and `□(p ∨ ¬p)` is true wherever you evaluate it."),
            ("An open future is a disagreement among the seen worlds",
             "`□p ∨ □¬p` requires the seen worlds to agree on `p`, either all true or all false. If one "
             "has `p` and another has `¬p`, neither box holds."),
        ],
        "read_title": "The fatalist's step",
        "read_intro": "The argument at its strongest, the model that refutes the step, and what is left of fatalism.",
        "body": [
            ("p", "Put the argument as its defender would. Tomorrow either there is a sea battle or there is "
                  "not, and that is not up to anyone: it is a matter of logic, and logic is necessary. So "
                  "either it is necessary that there will be a sea battle, or it is necessary that there "
                  "will not. If the first, nothing anyone does can prevent it; if the second, nothing can "
                  "produce it. In either case deliberating about it is idle."),
            ("p", "Write `p` for &ldquo;there will be a sea battle tomorrow&rdquo;. The first premise is `□(p ∨ ¬p)`. The "
                  "conclusion the fatalist wants is `□p ∨ □¬p`. Whether the argument is valid is the "
                  "question “Validity by Truth Table” teaches, with one change: the counterexample "
                  "is a world in a model, not a row."),
            ("math", [
                "premise:      □(p ∨ ¬p)",
                "conclusion:   □p ∨ □¬p",
            ]),
            ("p", "Build the model. World w1 is today. It sees w2, a world where the battle happens, and w3, "
                  "a world where it does not. The letter `p` is true at w2 and false at w3. At w1 the "
                  "premise asks whether `p ∨ ¬p` holds at w2 and at w3. It does at both, so the premise is "
                  "true. The first disjunct of the conclusion asks whether `p` holds at both seen worlds, "
                  "and it fails at w3. The second asks whether `¬p` holds at both, and it fails at w2. "
                  "Both disjuncts are false, so the conclusion is false. The premise holds and the "
                  "conclusion fails, so the form is invalid."),
            ("def", ("Modal scope fallacy",
                     "The <strong>scope fallacy</strong> here is the move from a box over a disjunction to a "
                     "disjunction of boxes. It treats the box as if it distributed over &ldquo;or&rdquo;. It "
                     "distributes over &ldquo;and&rdquo;, and not over &ldquo;or&rdquo;.")),
            ("p", "A look at the third preset shows when the disjunction of boxes is true. If w1 sees only "
                  "worlds where the battle happens, then `□p` is true, so `□p ∨ □¬p` is true. That is a "
                  "model of a settled future, and the conclusion is true in it for a reason that has "
                  "nothing to do with the premise: the seen worlds agree."),
            ("p", "Two features of the lab need a word. Worlds w2 and w3 see nothing, so any box is "
                  "vacuously true there, and that is why the worlds tile for the conclusion lists them. "
                  "The value to read is the one at w1. And the model says nothing about whether the "
                  "future has a truth value today; it is a point about a scope, not a theory of time."),
            ("h3", "What the fatalist can say instead"),
            ("p", "Take the repair at its strongest. The fatalist can drop the disjunction and "
                  "assert that what is true is already necessary: `p → □p`. If `p` is true today and "
                  "that makes it necessary, then there is no open future. This is a different "
                  "argument. Its premise is false at a world that has `p` and sees a world without "
                  "it, so the lab agrees with the fatalist only where the seen worlds already agree. "
                  "Accepting the premise is accepting that the future is settled, and then the "
                  "conclusion is not argued for but assumed."),
        ],
        "lab": ("argkit", {
            "mode": "kripke",
            "at": 1,
            "reading": "alethic",
            "preset": "wide",
            "presets": [
                {"id": "wide", "label": "the box around the whole disjunction",
                 "n": 3, "access": [[1, 2], [1, 3]], "valuation": {"p": [2]}, "formula": "[](p | ~p)",
                 "expect": {"krValue": "True at w1", "krWorlds": "all"}},
                {"id": "narrow", "label": "a box on each disjunct",
                 "n": 3, "access": [[1, 2], [1, 3]], "valuation": {"p": [2]}, "formula": "[]p | []~p",
                 "expect": {"krValue": "False at w1", "krWorlds": "w2, w3"}},
                {"id": "determined", "label": "w1 sees only worlds where p holds",
                 "n": 3, "access": [[1, 2], [1, 3]], "valuation": {"p": [2, 3]}, "formula": "[]p | []~p",
                 "expect": {"krValue": "True at w1", "krWorlds": "all"}},
            ],
            "panel_title": "Choose where the box goes",
            "panel_intro": "World w1 sees w2, where the battle happens, and w3, where it does not. The first preset is the premise, the second the conclusion, and the third a model where the conclusion is true. Edit the valuation to `p: 2 3` in the first two to see what a settled future does to each.",
        }),
        "steps_title": "Finding a scope shift",
        "steps_intro": "Four moves for any argument that moves a box.",
        "steps": [
            ("Mark where each box sits",
             "Write the premise and the conclusion with brackets. A box before an opening bracket "
             "governs everything inside it. A box before a letter governs the letter only."),
            ("Build a world that sees one world of each kind",
             "Give the premise's subject matter two seen worlds that disagree. One with `p` and one with "
             "`¬p` is the smallest."),
            ("Evaluate the premise and then the conclusion at that world",
             "The premise is a logical truth and will hold. Ask the conclusion about each seen world "
             "separately."),
            ("Name the shift",
             "If the premise holds and the conclusion fails, the box was moved across the connective. "
             "Say which connective, and say that the inference is invalid."),
        ],
        "worked": {
            "title": "The sea battle at w1",
            "intro": ["World w1 sees w2, where p is true, and w3, where p is false."],
            "lines": [
                "p or not p at w2: true, at w3: true",
                "box of (p or not p) at w1: true",
                "p at w3: false, so box of p at w1: false",
                "not p at w2: false, so box of not p at w1: false",
                "box of p or box of not p at w1: false",
                "the premise holds and the conclusion fails",
            ],
            "after": [
                "The disjunction of boxes is false because neither box holds, and neither holds because "
                "the seen worlds disagree. The inference from the first line to the last needs the seen "
                "worlds to agree, and the premise says nothing of the kind."
            ],
        },
        "quiz_title": "Where the box sits",
        "quiz": [
            {"q": "In the model where w1 sees w2 (p true) and w3 (p false), what is the value of `□(p ∨ ¬p)` at w1?",
             "a": ["False, because p is false at w3",
                   "False, because p is true at w2",
                   "True, because each seen world makes `p ∨ ¬p` true",
                   "Undefined, because the future has no truth value yet"],
             "c": 2,
             "why": "The box asks whether `p ∨ ¬p` holds at w2 and at w3, and it holds at both. The first two choices evaluate `p` or `¬p` alone, which is the other formula. The model gives every sentence a value at every world, so the last choice describes a different kind of theory."},
            {"q": "Why is `□p ∨ □¬p` false at w1 in that model?",
             "a": ["The seen worlds disagree about p, so neither box holds",
                   "Because `p ∨ ¬p` is false at w1",
                   "Because w1 sees only two worlds",
                   "Because `□` does not apply to disjunctions"],
             "c": 0,
             "why": "`□p` needs `p` at both w2 and w3, and `□¬p` needs `¬p` at both. Each fails at one. The disjunction `p ∨ ¬p` is true at every world, and the number of worlds seen does not matter, since a box over any number is evaluated the same way. Boxes apply to any formula."},
            {"q": "In which model is `□p ∨ □¬p` true at w1? In each, `p` is false at w1.",
             "a": ["w1 sees w2 and w3; p is true at w2 only",
                   "w1 sees w1, w2 and w3; p is true at w2 and w3",
                   "w1 sees w2 and w3; p is true at w2 and w3",
                   "w1 sees w2, w3 and w4; p is true at w2 and w3 and false at w4"],
             "c": 2,
             "why": "The disjunction of boxes is true exactly when the seen worlds agree about `p`. In the third model they all have `p`, so `□p` holds. In the first they disagree. In the second w1 sees itself, where `p` is false, so they disagree again, and in the fourth w4 lacks `p` while the others have it."},
            {"q": "What does the lab show about the fatalist's first premise, `□(p ∨ ¬p)`?",
             "a": ["It is false, because the future is open",
                   "It is true at every world of every model",
                   "It is true only when the seen worlds agree",
                   "It cannot be evaluated until the battle happens"],
             "c": 1,
             "why": "`p ∨ ¬p` holds at every world, so a box over it holds at any world. The premise is therefore not where the argument can be attacked, and the open-future theorist does not have to deny it. The second and third choices confuse it with the stronger conclusion."},
        ],
        "mistakes": [
            ("Believing that “necessarily, either there will be a battle or not” entails that one of them is necessary",
             "The first is `□(p ∨ ¬p)` and the second is `□p ∨ □¬p`. In the lab's model the first is true "
             "at w1 and the second is false, because w2 has `p` and w3 lacks it. A premise true and a "
             "conclusion false at one world is a counterexample, and the form is invalid however "
             "natural the English sounds."),
            ("Thinking an open future requires denying that the battle either will or will not happen",
             "The model keeps `□(p ∨ ¬p)` true. It is the claim that the outcome is settled that the model "
             "withholds. The two claims are different, and the open-future view needs only the second to "
             "be false."),
            ("Concluding that fatalism is refuted",
             "One argument for it has been shown invalid. A fatalist who asserts `p → □p` has a different "
             "argument, and the lab agrees with it exactly where the seen worlds already agree. Whether "
             "truth today makes the future necessary is the premise to judge, and no model decides it."),
        ],
        "standard": (
            "Finish when you can show, with a model, that a box does not distribute over a disjunction.",
            "Given an argument that passes from a necessary disjunction to a necessary disjunct, you should be "
            "able to draw a world that sees two worlds that disagree, evaluate the premise and the "
            "conclusion there, and name the connective the box was moved across. An answer that says "
            "only &ldquo;it confuses scope&rdquo; has not shown the world."),
        "note": "Worlds w2 and w3 see nothing, so a box is vacuously true there, and the verdict to read is the one at w1.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "the-ontological-argument-in-s5",
        "title": "The Ontological Argument in S5",
        "module": "Modality",
        "one_line": "The modal ontological argument is valid when the frame is euclidean, so the dispute is over its first premise and over the choice of frame.",
        "summary": (
            "If it is possible that a maximally great being necessarily exists, then, in S5, it necessarily "
            "exists. The lab evaluates the conditional on a frame where it holds and on one where it fails, "
            "and shows that the missing ingredient is a property of the arcs. What remains for the reader "
            "is whether to grant the possibility premise and whether S5 is the right logic for God."
        ),
        "key": [
            "G: a maximally great being exists",
            "◇□G → □G  valid on euclidean frames",
            "S4 + B = S5: the conditional appears",
            "valid in S5; the premise ◇□G is disputed",
        ],
        "key_label": "A valid argument whose premise carries the weight",
        "concepts_intro": (
            "The previous lessons gave the tools: a box and a diamond read off the arcs, and the "
            "axioms the arcs force. This lesson applies them to one old argument."
        ),
        "concepts": [
            ("The argument has one modal premise",
             "The premise is `◇□G`: it is possible that G is necessary, where G says that a "
             "maximally great being exists. The conclusion is `□G`, and by T, if the frame is "
             "reflexive, `G` itself."),
            ("The step from premise to conclusion is a property of the frame",
             "The conditional `◇□G → □G` is valid on a frame exactly when the frame is "
             "euclidean: whenever a world sees two worlds, the first sees the second."),
            ("Validity is not the same as acceptance",
             "A valid argument with a doubtful premise gives you a choice. You can accept the "
             "conclusion, or deny the premise, and the second has an equally good argument "
             "available."),
        ],
        "read_title": "Where S5 does the work",
        "read_intro": "The argument, the frame property it needs, the frame that lacks it, and the shape of the exit.",
        "body": [
            ("p", "The argument runs in three lines. A being is maximally great if it is as excellent as "
                  "a being can be in every possible world. A being like that, if there is one, "
                  "exists necessarily, since otherwise there would be a world in which it was missing, "
                  "and it would not be maximally great there. So the claim that there could be such a "
                  "being is the claim that it is possible that something exists necessarily. Write `G` "
                  "for &ldquo;a maximally great being exists&rdquo;. The first premise is `◇□G`. The second is a "
                  "fact about the logic of necessity, and the conclusion is `□G`."),
            ("math", [
                "premise 1:   ◇□G",
                "logic:       ◇□G → □G",
                "conclusion:  □G",
            ]),
            ("p", "The second line is valid on a frame exactly when the frame is euclidean, meaning "
                  "that if a world sees two worlds, the first of them sees the second. The "
                  "reasoning is short. Suppose w sees v, where `□G` holds, and w sees u. Euclidean says "
                  "v sees u, and `□G` at v gives `G` at u. So every world w sees has `G`, and `□G` "
                  "holds at w. In a frame that is reflexive and euclidean, which is the same as an equivalence "
                  "relation, every world can see every other in its group, and that is S5. The lab "
                  "shows the equivalence frame validating the conditional."),
            ("h3", "A frame where it fails"),
            ("p", "Weaken S5 by one property. Let w1 see itself and w2, and let w2 see only itself. "
                  "This frame is reflexive and transitive, the system S4, but not symmetric. Put `G` at "
                  "w2 only. At w2 the box holds, since the only world w2 sees has `G`. At w1, `◇□G` is "
                  "true because w1 sees w2. But `□G` is false at w1, because w1 sees itself and `G` is "
                  "false there. The premise is true and the conclusion false, so the conditional "
                  "fails on this frame."),
            ("p", "The missing arc is the one from w2 back to w1. Add it, and w2 now sees a world where "
                  "`G` is false, so `□G` fails at w2 and the antecedent fails at w1 as well. The "
                  "conditional is true, and the frame is the equivalence relation of S5, the S4 frame plus "
                  "the symmetry that B demands. The argument therefore needs the frame to be euclidean, which on a "
                  "reflexive frame means symmetric as well as transitive, and it gets no help from S4."),
            ("thm", ("What the lab establishes",
                     "On a euclidean frame the conditional `◇□G → □G` holds at every world for "
                     "every valuation of `G`. On the frame without the arc from w2 to w1 there is a "
                     "valuation and a world where it fails. The argument is valid in S5.")),
            ("h3", "What the argument costs"),
            ("p", "Two exits are open, and each is an argument. The first is to deny `◇□G`. The same "
                  "logic proves `◇□¬G → □¬G`, so whoever grants that it is possible that God necessarily "
                  "exists must also refuse the parallel premise, that it is possible that God "
                  "necessarily does not exist, and in S5 both premises cannot be true at one world. "
                  "Granting the first is therefore not a modest concession. It carries the conclusion "
                  "with it, and the modest-sounding word &ldquo;possible&rdquo; hides that. The second exit "
                  "is to reject S5 as the logic of the necessity in question, for example because "
                  "metaphysical necessity may not be symmetric. Then the argument has no valid form to "
                  "stand on."),
            ("p", "The lab can say none of this for you. It computes that the argument is valid on "
                  "one frame and invalid on another. Which frame suits God, or necessity, or the "
                  "word &ldquo;possible&rdquo; in the first premise, is the philosophical question, and it "
                  "comes after the logic, not instead of it."),
        ],
        "lab": ("argkit", {
            "mode": "kripke",
            "at": 1,
            "reading": "alethic",
            "preset": "s5",
            "presets": [
                {"id": "s5", "label": "w1 and w2 see each other, w3 sees itself",
                 "n": 3, "access": [[1, 1], [1, 2], [2, 1], [2, 2], [3, 3]], "valuation": {"G": [1, 2]},
                 "formula": "<>[]G -> []G", "expect": {"krValue": "True at w1", "krAxioms": "D, T, B, 4, 5"}},
                {"id": "no-symmetry", "label": "w1 sees w1 and w2, w2 sees only w2",
                 "n": 2, "access": [[1, 1], [1, 2], [2, 2]], "valuation": {"G": [2]},
                 "formula": "<>[]G -> []G", "expect": {"krValue": "False at w1", "krAxioms": "D, T, 4"}},
                {"id": "b-axiom", "label": "w1 and w2 see each other and themselves",
                 "n": 2, "access": [[1, 1], [1, 2], [2, 1], [2, 2]], "valuation": {"G": [2]},
                 "formula": "<>[]G -> []G", "expect": {"krValue": "True at w1", "krAxioms": "D, T, B, 4, 5"}},
            ],
            "panel_title": "Test the conditional on a frame",
            "panel_intro": "The formula is the logical step of the argument. The first model is an equivalence relation with `G` at every world of one group, the second lacks the arc from w2 to w1, and the third restores it. The axioms tile tells you which frame you are on.",
        }),
        "steps_title": "Testing a modal argument on a frame",
        "steps_intro": "Five moves. The fourth is the one a reader tends to skip.",
        "steps": [
            ("State the argument as premises, a logic and a conclusion",
             "Mark which line is a claim about the world and which is a principle about necessity. Here the "
             "first is `◇□G` and the second is the conditional."),
            ("Test the logical line on a frame the logic is meant to describe",
             "Build the frame, type the conditional, and read the value at a world. On an equivalence "
             "relation it holds."),
            ("Weaken the frame by one property",
             "Remove the arc that symmetry requires, and read the value again. The change in the tile is the "
             "property the argument needs."),
            ("Check the parallel premise",
             "Replace `G` with `¬G` in the premise and the conclusion. If the logic proves both, the "
             "two premises cannot both be granted, and the choice is no longer neutral."),
            ("Decide where to push",
             "Either the premise, or the claim that the frame is the right one. Say which you pick and "
             "what it costs."),
        ],
        "worked": {
            "title": "The conditional on a frame without symmetry",
            "intro": ["Two worlds. World w1 sees w1 and w2, w2 sees only w2, and G is true at w2 only."],
            "lines": [
                "box of G at w2: w2 sees w2, G there: true",
                "diamond of box of G at w1: w1 sees w2: true",
                "box of G at w1: w1 sees w1, G false there: false",
                "the conditional at w1: true then false, so false",
                "add the arc from w2 to w1",
                "box of G at w2: now w2 sees w1, G false there: false",
                "diamond of box of G at w1: false, so the conditional: true",
            ],
            "after": [
                "On the frame without symmetry the antecedent is true and the consequent false. Restoring "
                "the arc does not make the consequent true. It makes the antecedent false, which "
                "is how the conditional becomes true on that frame, and it is the sense in which "
                "S5 does the work."
            ],
        },
        "quiz_title": "The argument on a frame",
        "quiz": [
            {"q": "On the frame where w1 sees w1 and w2 and w2 sees only w2, with G true at w2 only, what is the value of `◇□G → □G` at w1?",
             "a": ["True, because ◇□G is false",
                   "True, because G is true at w2",
                   "Undefined, because G is false at w1",
                   "False, because ◇□G is true and □G is false"],
             "c": 3,
             "why": "At w1, `◇□G` holds through w2, and `□G` fails because w1 sees itself and `G` is false there. A true antecedent with a false consequent makes the conditional false. The first choice has the antecedent wrong, and the second looks at `G` at w2 only."},
            {"q": "Which frame property is exactly what `◇□G → □G` needs to be valid on a frame?",
             "a": ["Reflexive: every world sees itself",
                   "Serial: every world sees some world",
                   "Euclidean: if a world sees two worlds, the first sees the second",
                   "No property: it holds on every frame"],
             "c": 2,
             "why": "The proof uses exactly this: w sees v with `□G`, w sees u, so v sees u. The no-symmetry frame is reflexive and serial and the conditional still fails, so neither is enough, and the failure shows that it does not hold on every frame."},
            {"q": "A critic grants S5 and denies the first premise `◇□G`. Which description fits her?",
             "a": ["She accepts that the argument is valid and denies a premise",
                   "She denies that the argument is valid",
                   "She rejects the logic S5",
                   "She accepts the conclusion"],
             "c": 0,
             "why": "She grants the logic, so the conditional holds, and withholds the premise, so the argument does not establish the conclusion. The second and third choices are about the logic, which she accepted. And rejecting the premise does not commit her to the conclusion."},
            {"q": "In S5 the same reasoning gives `◇□¬G → □¬G`. What follows for the first premise?",
             "a": ["`◇□G` is false in every model",
                   "At a world of S5, `◇□G` and `◇□¬G` cannot both be true, so granting the first is not neutral",
                   "`G` is true at every world",
                   "The argument for the conclusion `□G` is refuted"],
             "c": 1,
             "why": "If both held, `□G` and `□¬G` would both hold at a reflexive world, and `G` would be true and false there. So at most one premise can be granted. That does not make `◇□G` false in all models, make `G` true, or refute the argument, which is still valid."},
        ],
        "mistakes": [
            ("Believing that the modal ontological argument is invalid",
             "On the equivalence frame the lab finds the conditional true, and the proof for euclidean "
             "frames shows why it holds at every world for every valuation. The argument is valid in S5. "
             "What the reader may doubt is the first premise, or the claim that the necessity in "
             "question has the arcs of S5, and each of these is a reason to reject the conclusion "
             "without calling the reasoning a mistake."),
            ("Treating the conditional as a claim about God",
             "`◇□G → □G` mentions `G` only as an example of a letter. The same conditional is valid for "
             "`¬G`, for `p` and for any sentence at all, so it carries no theological content. All "
             "the content is in `◇□G`, which is why a reader who grants it has granted nearly "
             "everything."),
            ("Taking a valid argument to be a proof of its conclusion",
             "A valid argument can be run backwards. If `□G` is false at a world, the conditional "
             "gives that `◇□G` is false there as well. A reader who finds the conclusion more "
             "doubtful than the premise is entitled to deny the premise, and nothing in the lab "
             "ranks the two doubts."),
        ],
        "standard": (
            "Finish when you can say which property of the frame the argument needs and which premise is left to dispute.",
            "You should be able to evaluate the conditional on an equivalence relation and on a "
            "reflexive transitive frame without symmetry, state the frame property that separates "
            "them, and name two replies open to someone who finds the conclusion hard to accept. A reply "
            "that says only &ldquo;the argument is a trick&rdquo; has not located the premise."),
        "note": "The frame tile and the axioms tile describe the frame, not the formula. A formula that is true at w1 on one valuation does not show validity, and the proof for euclidean frames is what shows it for every valuation.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "leibnizs-law-and-the-masked-man",
        "title": "Leibniz's Law and the Masked Man",
        "module": "Modality",
        "one_line": "Two sentences that are true together can still not be swapped inside a box, which is why the masked man does not refute Leibniz's law.",
        "summary": (
            "I know that my father is here and I do not know that the masked man is here, yet the masked man "
            "is my father. In a model whose box is read as &ldquo;it is known that&rdquo;, the lab shows both sentences "
            "true at the actual world and the two boxes with different values. The substitution fails "
            "inside the box, and outside it the law holds."
        ),
        "key": [
            "if a is b, a and b share every property",
            "f ↔ m  true, but  □f ↔ □m  false",
            "swap freely outside a box, not inside",
            "one world: nothing to disagree about",
        ],
        "key_label": "Where substitution holds and where it fails",
        "concepts_intro": (
            "The lab reads the box epistemically here, as &ldquo;it is known that&rdquo;. The computation is the "
            "same as in “Necessity, Possibility and Possible Worlds”. The subject matter has entered through the arcs."
        ),
        "concepts": [
            ("Leibniz's law",
             "If a and b are the same thing, then whatever is true of a is true of b. It is a principle "
             "about identity and about properties of the thing."),
            ("A box looks at other worlds",
             "`□f` is true at w1 only if `f` is true at every world compatible with what is known there. "
             "Two sentences that agree at w1 can disagree at another such world, and then the boxes "
             "differ."),
            ("Being known is not a property of the man",
             "&ldquo;Is known by me to be here&rdquo; depends on how the man is picked out, as the father or as the "
             "masked man. It is a property of the man under a description, and the law concerns the "
             "properties of the man himself."),
        ],
        "read_title": "A true equivalence that does not survive a box",
        "read_intro": "The masked man as a model, the substitution that fails, and the one that cannot.",
        "body": [
            ("p", "The old argument runs as follows. I know who my father is, so I know that my father is "
                  "here. I do not know who the masked man is, so I do not know that the masked man is "
                  "here. But the masked man is my father. So by Leibniz&rsquo;s law my father has a property "
                  "that the masked man lacks, being known by me to be here, and they are not the same "
                  "man. Since they are the same man, something has gone wrong."),
            ("p", "The lab makes the failure exact. Let `f` say that my father is here and `m` that the "
                  "masked man is here. At the actual world, w1, both are true: the man in the mask is "
                  "my father. Read the box as &ldquo;it is known that&rdquo; and draw the arcs from w1 to the "
                  "worlds compatible with what I know. There are two: w1 itself and w2. At w2 my father is "
                  "here but the man in the mask is not, since for all I know the masked man is a "
                  "stranger."),
            ("math", [
                "world   f   m",
                "w1      T   T",
                "w2      T   F",
            ]),
            ("p", "Now evaluate. `□f` is true at w1, because `f` holds at both worlds w1 sees. `□m` is false "
                  "at w1, because `m` fails at w2. And `f ↔ m` is true at w1, since both are true there. "
                  "So at one world two sentences are equivalent and their boxed versions differ in value. "
                  "That is the whole of the masked man: substitution of equivalents inside a box fails, "
                  "because a box consults worlds at which the equivalence need not hold."),
            ("p", "Outside the box nothing fails. From `f ↔ m` at w1 you may swap `f` and `m` in any "
                  "context that looks only at w1: in a conjunction, a negation, a conditional. The "
                  "extensional preset shows the opposite end. With a single world the box has only "
                  "that one world to look at, `f` and `m` agree there, and `□f ↔ □m` is true. "
                  "Substitution inside the box is harmless when the box has nothing to disagree about."),
            ("def", ("Opaque context",
                     "A context is <strong>opaque</strong> when swapping two sentences, or two names for "
                     "one thing, that agree in value at the actual world can change the value of the whole. "
                     "A box is opaque whenever the worlds it looks at can disagree.")),
            ("p", "The same shape appears with necessity. The number of planets is eight, and eight is "
                  "necessarily even, but it does not follow that the number of planets is necessarily "
                  "even, since there are worlds where the planets are seven. The model is the "
                  "same, with the arcs read alethically."),
            ("p", "What survives for Leibniz is a point about what the law covers. It speaks of "
                  "properties of the man, and being known to be here is not one of them, because it "
                  "changes with the description. The reply is not free: it commits the reader to a "
                  "distinction between properties of things and properties of things under "
                  "descriptions, and some philosophers resist that. The lab computes the failure of "
                  "substitution; it does not decide how to describe it. It also contains no individuals "
                  "and no identity sign, so it models the sentences and not the man."),
        ],
        "lab": ("argkit", {
            "mode": "kripke",
            "at": 1,
            "reading": "epistemic",
            "preset": "known-father",
            "presets": [
                {"id": "known-father", "label": "I know my father is here",
                 "n": 2, "access": [[1, 1], [1, 2]], "valuation": {"f": [1, 2], "m": [1]},
                 "formula": "[]f", "expect": {"krValue": "True at w1"}},
                {"id": "known-masked", "label": "I know the masked man is here",
                 "n": 2, "access": [[1, 1], [1, 2]], "valuation": {"f": [1, 2], "m": [1]},
                 "formula": "[]m", "expect": {"krValue": "False at w1"}},
                {"id": "same-man", "label": "the father is the masked man",
                 "n": 2, "access": [[1, 1], [1, 2]], "valuation": {"f": [1, 2], "m": [1]},
                 "formula": "f <-> m", "expect": {"krValue": "True at w1", "krWorlds": "w1"}},
                {"id": "extensional", "label": "one world, nothing else to consider",
                 "n": 1, "access": [[1, 1]], "valuation": {"f": [1], "m": [1]},
                 "formula": "[]f <-> []m", "expect": {"krValue": "True at w1"}},
            ],
            "panel_title": "Substitute inside the box and outside it",
            "panel_intro": "The box is read as it is known that. World w1 sees itself and w2. At w1 both sentences are true, at w2 only `f`. The first three presets are the three sentences of the argument. Type `[]f <-> []m` yourself on the first model to see the boxed versions disagree.",
        }),
        "steps_title": "Telling a failed substitution from a counterexample to the law",
        "steps_intro": "Four moves for any puzzle that seems to refute Leibniz's law.",
        "steps": [
            ("Find the sentences that are true together",
             "Evaluate both at the actual world. The masked man gives `f` and `m` both true."),
            ("Find the box in the context that goes wrong",
             "Look for knowing, believing, necessity, or any operator that looks at other worlds. "
             "The property that seems to differ is built from it."),
            ("Evaluate the boxed sentences separately",
             "Type each into the lab. If the boxed versions differ while the unboxed ones agree, "
             "the substitution failed inside an opaque context."),
            ("Ask whether the changing property belongs to the thing",
             "If it depends on how the thing is described, it is not a property of the thing, and "
             "the law was never applied to it."),
        ],
        "worked": {
            "title": "The masked man at w1",
            "intro": ["World w1 sees w1 and w2. At w1, f and m are both true. At w2, f is true and m is false."],
            "lines": [
                "box of f at w1: f at w1 true, at w2 true: true",
                "box of m at w1: m at w1 true, at w2 false: false",
                "f iff m at w1: true iff true: true",
                "box of f iff box of m at w1: true iff false: false",
                "swap f for m outside any box: still true",
                "swap f for m inside the box: the value changes",
            ],
            "after": [
                "The two sentences agree where they are evaluated and differ in the worlds the box "
                "consults. That is all the failure is, and it needs no property of the man."
            ],
        },
        "quiz_title": "Substituting inside a box",
        "quiz": [
            {"q": "At w1, `f ↔ m` is true and `□f` is true. What is `□m` in the lab&rsquo;s model?",
             "a": ["True, because f and m agree at w1",
                   "False, because m is false at w2, which w1 sees",
                   "True, because □f is true",
                   "Undefined, because the masked man is unknown"],
             "c": 1,
             "why": "The box consults both w1 and w2, and `m` fails at w2. Agreement at w1 is not enough, which is the lesson. The model gives the sentence a value like any other."},
            {"q": "Which substitution does the lab show failing?",
             "a": ["Replacing `f` by `¬¬f` inside a box",
                   "Replacing `f` by `m` outside any box, given `f ↔ m` at w1",
                   "Replacing `f` by `m` inside a box, given `f ↔ m` at w1",
                   "Replacing a sentence by itself inside a box"],
             "c": 2,
             "why": "`f` and `m` agree at w1 but not at w2, so a box that looks at w2 can tell them apart. The first is harmless, because `¬¬f` agrees with `f` at every world. The second is also harmless, since outside a box only w1 is consulted. The fourth cannot fail."},
            {"q": "What does the extensional preset, with a single world, show?",
             "a": ["That `f` and `m` are the same sentence",
                   "That Leibniz's law is false",
                   "That with no other world to look at, a box cannot tell `f` from `m`",
                   "That the masked man is not the father"],
             "c": 2,
             "why": "There the box looks only at the one world, where `f` and `m` agree, so `□f ↔ □m` is true. The sentences are not the same sentence, and a single model does not test the law or settle who the masked man is."},
            {"q": "Which reply to the masked man keeps the law and keeps the facts of the case?",
             "a": ["Deny that the masked man is the father",
                   "Hold that being known to be here is not a property of the man himself, since it depends on the description",
                   "Deny that I know my father is here",
                   "Hold that the father is different from himself"],
             "c": 1,
             "why": "The first and third change the facts the case was built from, and the fourth gives up identity. The second leaves the case alone and limits what the law covers. It costs a distinction that some philosophers reject."},
        ],
        "mistakes": [
            ("Thinking the masked man refutes Leibniz's law",
             "The lab shows `f ↔ m` true at w1, `□f` true and `□m` false. The pair that differ are "
             "the boxed sentences, which are about the worlds compatible with what I know, and not "
             "about the man. The law was never applied to anything it covers, so nothing has refuted "
             "it."),
            ("Thinking substitution fails in every context",
             "Outside a box it holds. From `f ↔ m` at w1 you may replace one by the other inside a "
             "negation, a conjunction or a conditional and keep the value at w1. The failure belongs to "
             "contexts that look at other worlds."),
            ("Treating the failure as a quirk of talk about knowledge",
             "The same arcs read as necessity give the same failure: eight is necessarily even, the "
             "number of planets is eight, and the number of planets is not necessarily even. Any "
             "operator that quantifies over worlds is opaque in this way. Reading the box as knowledge "
             "changed the words in the status line and left the computation alone."),
        ],
        "standard": (
            "Finish when you can show with a model that two true sentences differ under a box, and say why that leaves the law untouched.",
            "You should be able to give a model in which two sentences agree at the actual world and "
            "their boxed versions do not, say which worlds make the difference, and state what "
            "Leibniz&rsquo;s law covers that the boxed sentences are not. A claim that substitution &ldquo;fails&rdquo; "
            "without the world at which the sentences come apart has not been shown."),
        "note": "World w2 sees nothing, so any box is vacuously true there. The tiles that matter in this lesson are the values at w1.",
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "the-ship-of-theseus",
        "title": "The Ship of Theseus",
        "module": "Identity over time",
        "one_line": "Replacing one plank at a time is a chain of tolerance conditionals, and each way of treating the chain says something different about the all-new ship.",
        "summary": (
            "A thousand planks are replaced one by one. Replacing one plank seems to preserve identity, "
            "and a thousand times over that gives an all-new ship that is the original. The lab runs the "
            "chain under the classical, cutoff and degree treatments, and the question becomes which "
            "premise or which logic to give up."
        ),
        "key": [
            "F(k): k original planks, still the ship",
            "tolerance: F(k) → F(k − 1) at each step",
            "1000 steps from F(1000) reach F(0)",
            "classical true; cutoff false; degrees 0",
        ],
        "key_label": "A thousand small steps to an all-new ship",
        "concepts_intro": (
            "The five modal lessons asked what is true at the worlds a world can see. The next three ask "
            "what stays the same through time, and the oldest case is a ship. The ship of Theseus is a "
            "sorites in disguise. Treating it as one lets the lab count the steps and show what each way "
            "out of the chain commits you to."
        ),
        "concepts": [
            ("Each replacement is a tolerance conditional",
             "Let `F(k)` say that the ship with `k` original planks, repaired plank by plank, is the "
             "original ship. &ldquo;Replacing one plank preserves identity&rdquo; is `F(k) → F(k − 1)`, and there "
             "is one such conditional for each plank."),
            ("The chain is valid",
             "From `F(1000)` and every conditional, modus ponens a thousand times gives `F(0)`: "
             "the ship with no original planks is the original. If the conclusion is unacceptable, "
             "a premise or the logic must go."),
            ("Each treatment gives up something different",
             "The classical treatment keeps every conditional and accepts the conclusion. The cutoff "
             "treatment makes one conditional false. The degree treatment makes each slightly less than "
             "true, and the conclusion has value 0."),
        ],
        "read_title": "One chain, three treatments",
        "read_intro": "The conditionals, the lab&rsquo;s counts, and what is left to say about the reassembled ship.",
        "body": [
            ("p", "Begin with the puzzle in its standard form. A wooden ship has a thousand planks. "
                  "Each year one is replaced. After a thousand years none of the original planks "
                  "remains, and it seems to have been the same ship throughout, since at no year did "
                  "anyone say that a different ship had appeared. But a ship with no original plank "
                  "is not the original ship, at least not on the face of it."),
            ("p", "Write the first claim as a chain. The starting ship has all its planks, `F(1000)`. "
                  "The tolerance claim, one plank does not matter, is the family `F(1000) → F(999)`, "
                  "`F(999) → F(998)` and so on down to `F(1) → F(0)`. The conclusion is `F(0)`. This "
                  "is the structure of a sorites, the same chain as in “Slippery Slopes and Small "
                  "Differences” in Ethics and the Arithmetic of Welfare, and the lab counts it: "
                  "1000 steps, 1000 conditionals."),
            ("p", "Under the classical treatment every conditional is true, and the lab prints "
                  "&ldquo;all 1000 true&rdquo; and the conclusion True. The ship with no original plank is the "
                  "original ship. Accepting that is the first exit, and it is not as silly as it sounds: "
                  "it says that what makes a ship the same is continuity of repair, not material."),
            ("p", "Under the cutoff treatment one conditional is false. With the cutoff at 500 it is "
                  "`F(500) → F(499)`: the ship with 500 original planks is the original, and the one with 499 "
                  "is not. The lab prints that one conditional is false, at 500, and the conclusion "
                  "False. Nothing in the arithmetic chose 500. Any number from 1 to 1000 gives a "
                  "consistent verdict, and a reader who picks one has made an input and not found "
                  "a fact."),
            ("p", "Under the degree treatment each conditional is almost true. Each loses one "
                  "thousandth, so each has value 999/1000, and a thousand of them chained lose "
                  "everything: the lab prints 0 as the value the chain guarantees for the conclusion. "
                  "Identity comes in degrees, and the all-new ship is guaranteed none of it."),
            ("h3", "The reassembled ship"),
            ("p", "The standard puzzle adds a second ship. The old planks, as they were removed, were "
                  "stored and later reassembled in their old order. The reassembled ship has "
                  "every original plank, and was never repaired. Now there are two candidates for being "
                  "Theseus&rsquo; ship, and they are two ships, so at most one is the original."),
            ("p", "The lab says nothing about the reassembled ship directly, because its claim is "
                  "not a step in the chain. What it computes is how much the repaired ship keeps. "
                  "Classically it keeps the whole title, so the reassembled ship does not have it. "
                  "With a cutoff at 500 the repaired ship loses the title at one replacement, and "
                  "a reader who thinks material makes a ship the same will give it to the "
                  "reassembled one. With degrees the repaired ship ends at 0, and the "
                  "reassembled one has the only remaining claim. Which criterion should carry the "
                  "weight, continuity of repair or the parts, is the philosophical question, and the "
                  "lab counts only the first."),
            ("p", "So the arithmetic does not find the original ship. It shows what a treatment "
                  "delivers when you feed it a chain. The choice of treatment is the question."),
        ],
        "lab": ("argkit", {
            "mode": "sorites",
            "treatment": "classical",
            "preset": "planks",
            "presets": [
                {"id": "planks", "label": "a thousand planks, replaced one at a time",
                 "start": 1000, "end": 0, "cutoff": 500, "predicate": "is the original ship",
                 "expect": {"soSteps": "1000", "soCond": "all 1000 true", "soConc": "True"}},
                {"id": "half-replaced", "label": "from all planks to half replaced",
                 "start": 1000, "end": 500, "cutoff": 750, "predicate": "is the original ship",
                 "expect": {"soSteps": "500", "soCond": "all 500 true", "soConc": "True"}},
                {"id": "twenty-planks", "label": "a boat of twenty planks",
                 "start": 20, "end": 0, "cutoff": 10, "predicate": "is the original boat",
                 "expect": {"soSteps": "20", "soCond": "all 20 true", "soConc": "True"}},
            ],
            "panel_title": "Run the chain and change the treatment",
            "panel_intro": "The shipped treatment is classical. Move the treatment menu to the cutoff to see one conditional fail at the cutoff you typed, and to degrees to see each conditional lose a little and the conclusion guaranteed nothing. The menu also has a borderline-range entry, which is not used in this lesson.",
        }),
        "steps_title": "Running a puzzle of identity as a chain",
        "steps_intro": "Five moves. The first two set up the chain and the rest read the treatments.",
        "steps": [
            ("Name the predicate and the clear case",
             "&ldquo;Is the original ship&rdquo; applied to the ship with all its planks is the starting case. "
             "Write it as `F` at the starting count."),
            ("Write the tolerance conditional",
             "One step changes the count by one, and the claim is that this does not change the "
             "answer. Write `F(k) → F(k − 1)`."),
            ("Count the steps",
             "The start minus the end. The lab prints it, and it is also the number of conditionals."),
            ("Read each treatment",
             "Classical keeps every conditional and accepts the end. Cutoff falsifies one. Degrees "
             "lower each, and the conclusion has value 0."),
            ("Decide what the second claimant shows",
             "A reassembled or rival ship is not a step of the chain. Ask which criterion would give "
             "it the title and whether you accept that criterion."),
        ],
        "worked": {
            "title": "A thousand planks",
            "intro": ["The starting count is 1000, the end count 0, and the cutoff is 500."],
            "lines": [
                "F(1000): all planks original, the original ship",
                "F(k) to F(k - 1): replace one plank",
                "steps: 1000 - 0 = 1000",
                "classical: all 1000 true, F(0) true",
                "cutoff 500: F(500) to F(499) false, F(0) false",
                "degrees: each 999/1000, F(0) no more than 0",
            ],
            "after": [
                "Three treatments of one chain, and three different answers about the same ship. "
                "The arithmetic reported each one exactly; it did not say which treatment to use."
            ],
        },
        "quiz_title": "Planks and treatments",
        "quiz": [
            {"q": "Under the classical treatment of a chain from 1000 planks to 0, what does the lab report?",
             "a": ["All 1000 conditionals true and the conclusion False",
                   "One conditional false and the conclusion False",
                   "All 1000 conditionals true and the conclusion True",
                   "Each conditional 999/1000 and the conclusion 0"],
             "c": 2,
             "why": "Classically every tolerance conditional is true and modus ponens carries the title to the end. The second is the cutoff treatment, and the fourth is the degree treatment. The first could not be, since a valid chain of true conditionals has a true conclusion."},
            {"q": "With a cutoff at 500, what does the lab say about the conditionals?",
             "a": ["Every conditional is false from 500 down",
                   "Exactly one is false, the step from 500 planks to 499",
                   "Exactly one is false, chosen by the arithmetic as the right one",
                   "All are true and the conclusion is False"],
             "c": 1,
             "why": "A cutoff makes the single conditional `F(500) → F(499)` false and the rest true. The arithmetic did not select 500; it was an input, so the third is wrong. If all were true the conclusion would be true, which rules out the fourth. The first falsifies many conditionals that a cutoff leaves true."},
            {"q": "Under degrees each conditional has value 999/1000, yet the conclusion is guaranteed only 0. Why?",
             "a": ["Because the premise F(1000) is only partly true",
                   "Because 999/1000 is below the threshold of truth",
                   "Because the chain is invalid",
                   "Because a thousand steps each lose one thousandth, and the losses add up to everything"],
             "c": 3,
             "why": "Chained modus ponens loses the shortfall of every step, and a thousand shortfalls of one thousandth come to one whole. The premise `F(1000)` is fully true. Validity is not at issue, and the lab does not use a threshold."},
            {"q": "A reader says that if the lab is run with every cutoff from 1 to 1000 it will find the plank at which the ship stopped being the original. What is wrong with this?",
             "a": ["A cutoff is an input, and every choice gives a consistent verdict that the arithmetic cannot rank",
                   "The cutoff must always be 500",
                   "The lab refuses cutoffs above 100",
                   "The classical treatment already finds it"],
             "c": 0,
             "why": "Each cutoff falsifies one conditional and makes all else true, and nothing in the counts prefers one cutoff to another. 500 is only an example, the lab accepts any cutoff above the end count, and the classical treatment finds no false conditional."},
        ],
        "mistakes": [
            ("Believing there is a fact about which ship is the original that the arithmetic can find",
             "The lab prints what each treatment delivers for a chain you supply: all true, one false at "
             "the cutoff you typed, or each 999/1000. It has no input for the thing that would "
             "decide between them. A cutoff at 500 and a cutoff at 501 are equally consistent, and "
             "the arithmetic cannot say which describes the ship."),
            ("Treating the conclusion as absurd and therefore the argument as broken",
             "The chain is valid, which the classical row shows: true conditionals carry the title all the "
             "way. If `F(0)` is unacceptable, a premise or the logic must go, and the treatments are "
             "the choices. The classical treatment gives up nothing and accepts `F(0)`. The cutoff "
             "gives up one conditional, at a line you drew. Degrees give up the full truth of every "
             "conditional, and with it the classical logic of the chain."),
            ("Thinking the reassembled ship settles the matter",
             "It is a second claimant with a different criterion, parts instead of continuity. Giving it "
             "the title is the position that parts make the ship, and that position has its own cost: "
             "every ship that has ever had a plank replaced would be a new ship. The lab counts the "
             "first criterion only."),
        ],
        "standard": (
            "Finish when you can write a puzzle of identity as a chain and say what each treatment commits you to.",
            "You should be able to state the tolerance conditional for the ship, give the number of "
            "steps, read the lab&rsquo;s report under the classical, cutoff and degree treatments, and "
            "say which premise or which logic each one gives up. A verdict stated without the "
            "treatment it came from has not been computed."),
        "note": "The treatment menu is not a preset, so the presets here fix the chain and the cutoff and the three treatments are read by moving the menu. Only the classical reading is pinned in the presets; the cutoff and degree figures in the lesson are read from the lab with the menu moved.",
    },
]
