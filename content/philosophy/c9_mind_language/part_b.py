"""Course 9, lessons 06-10 -- language, where a sentence can be computed in a model."""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "compositional-truth-conditions",
        "title": "Compositional Truth Conditions",
        "module": "Language",
        "one_line": "Evaluate a sentence of predicate logic in a finite model from the values of its parts, and change one extension to change the value.",
        "summary": (
            "To give the meaning of a sentence is, at least, to say when it is true, "
            "and a sentence is true or false only in a model. Build a small model "
            "of individuals and extensions, evaluate a quantified sentence by "
            "evaluating its parts, and change one pair in one extension to turn "
            "the same sentence from true to false."
        ),
        "key": [
            "a sentence is true in a model, not alone",
            "model: individuals + extensions + names",
            "∀x: the part holds for every individual",
            "∃x: the part holds for some individual",
            "change one extension, the value can flip",
        ],
        "key_label": "Truth is relative to a model",
        "concepts_intro": (
            "The mind half of this course evaluated a claim in a model, whether of "
            "worlds, of rows or of likelihoods, and found the philosophy in the "
            "choice of model. The language half asks the same of a sentence. This "
            "first lesson fixes what it is to evaluate one, and the four lessons "
            "after it only change which sentences are evaluated."
        ),
        "concepts": [
            ("A model is a domain and what is true of it",
             "A finite model lists some individuals, says for each predicate which "
             "individuals (or which pairs) it holds of, and says which individual "
             "each name picks out. That list is everything the sentence is "
             "evaluated against, and nothing else is consulted."),
            ("The value of a sentence is built from the values of its parts",
             "An atomic sentence is true when its individuals are in the extension. "
             "The connectives work as in Arguments and Validity. A quantifier asks "
             "its part to be true of every individual, or of some. This is "
             "compositionality: the whole is computed from the parts and how they "
             "are put together."),
            ("The same sentence can have two values",
             "Because the value is computed from the model, one sentence read in "
             "two models can be true in one and false in the other. Truth "
             "conditions say when it would be true; they do not say that it is."),
        ],
        "read_title": "From a model to a value",
        "read_intro": (
            "A definition, one model, one evaluation worked by hand, and the same "
            "sentence in a model with one pair removed."
        ),
        "body": [
            ("def", ("Truth conditions",
                     "The <strong>truth conditions</strong> of a sentence are the "
                     "conditions under which it would be true. To know them is to "
                     "know, for any situation described in enough detail, whether "
                     "the sentence is true there. It is not to know whether the "
                     "sentence is true.")),
            ("p", "A situation, for this lesson, is a finite model. It has a "
                  "domain of individuals, an extension for each predicate, and a "
                  "referent for each name. Here is a small one, with three "
                  "individuals `a`, `b` and `c`. The predicate `Planet` holds of "
                  "`a` and `b`. The two-place predicate `Orbits` holds of the pair "
                  "`a` and `b` taken in that order, and of the pair `b` and `c`. "
                  "The model is a table and not astronomy; it is only meant to be "
                  "easy to hold in the head."),
            ("math", [
                "individual   Planet   orbits",
                "-------------------------------",
                "a            yes      b",
                "b            yes      c",
                "c            no       nothing",
            ]),
            ("p", "The rules for evaluating a sentence are short, and they are the "
                  "whole of the method."),
            ("ul", [
                "An atomic sentence such as `Planet(a)` is true when `a` is in the "
                "extension of `Planet`, and `Orbits(a, b)` when that pair is "
                "in the extension of `Orbits`.",
                "`¬A`, `A ∧ B`, `A ∨ B` and `A → B` take their values from the values "
                "of `A` and `B` by the tables of Arguments and Validity.",
                "`∀x A` is true when `A` is true with each individual of the domain "
                "put for `x`, and `∃x A` is true when it is true for at least one.",
            ]),
            ("p", "Take the sentence `∀x (Planet(x) → ∃y Orbits(x, y))`, which says "
                  "that every planet orbits something. Put `a` for `x`. "
                  "`Planet(a)` is true, and `∃y Orbits(a, y)` is true because "
                  "putting `b` for `y` gives a pair in the extension, so the "
                  "conditional is true. Put `b` for `x`: `Planet(b)` is true, "
                  "`c` is the something it orbits, and the conditional is true. "
                  "Put `c` for `x`: `Planet(c)` is false, so the conditional is "
                  "true whatever `c` orbits. Every individual passes, and the lab "
                  "prints True."),
            ("p", "Now remove the pair `b` and `c` from the extension of `Orbits`, "
                  "and change nothing else. The sentence is the same sentence, with "
                  "the same words in the same order. At `x = a` it still passes. At "
                  "`x = b` the planet `b` orbits nothing, `∃y Orbits(b, y)` has no "
                  "witness, the conditional is false, and the sentence is false. The "
                  "lab prints False and names `b` as the place it fails. One pair "
                  "in one extension decided the value."),
            ("p", "That is the point about truth conditions. Someone who understands "
                  "the sentence knows what it takes for it to be true, and that is "
                  "the rule above applied to any model. They do not thereby know "
                  "which model is the actual one. So &ldquo;is this sentence "
                  "true?&rdquo; has no answer until a model has been named, and what "
                  "we call a sentence's being true on its own is always a model "
                  "left unspoken."),
            ("p", "An existential sentence is the same idea with the quantifier "
                  "turned over. `∃x (Planet(x) ∧ Orbits(x, x))` asks for a planet "
                  "that orbits itself. No individual in the model is one, so there "
                  "is no witness to report, and the value is False. A universal "
                  "sentence is refuted by one individual and an existential one is "
                  "confirmed by one; each is false when the other kind of "
                  "individual is missing altogether."),
            ("p", "Two quantifiers nest the same way. `∀x ∃y Loves(x, y)` asks, for "
                  "each individual, whether some individual is loved by it, and in "
                  "a ring where `a` loves `b`, `b` loves `c` and `c` loves `a` "
                  "every individual passes, so the lab prints True. The tile for "
                  "the outermost quantifier counts the passes: 3 of 3 in the ring, "
                  "3 of 3 for the planets, and 2 of 3 once the pair `b`, `c` is "
                  "gone, which is the failing individual seen from the other side. "
                  "Whether the order of two quantifiers matters is its own "
                  "question, and “Scope Ambiguity and Negation” puts the same ring "
                  "to that use."),
            ("p", "The limit is the usual one. The lab evaluates in the model you "
                  "typed, and a model has the individuals and pairs you gave it. "
                  "Whether the pairs describe the solar system, or anything, is "
                  "not something it can check."),
        ],
        "lab": ("argkit", {
            "mode": "semantics",
            "preset": "orbits",
            "presets": [
                {"id": "orbits", "label": "every planet orbits something, in a chain of three",
                 "domain": ["a", "b", "c"], "names": {},
                 "predicates": {"Planet": ["a", "b"], "Orbits": [["a", "b"], ["b", "c"]]},
                 "sentence": "Ax (Planet(x) -> Ey Orbits(x, y))", "expect": {"seValue": "True", "seWitness": "—"}},
                {"id": "pair-removed", "label": "the same sentence, with the pair bc removed",
                 "domain": ["a", "b", "c"], "names": {},
                 "predicates": {"Planet": ["a", "b"], "Orbits": [["a", "b"]]},
                 "sentence": "Ax (Planet(x) -> Ey Orbits(x, y))", "expect": {"seValue": "False", "seWitness": "fails at x = b"}},
                {"id": "everyone-loves", "label": "everyone loves someone, in a ring of three",
                 "domain": ["a", "b", "c"], "names": {},
                 "predicates": {"Loves": [["a", "b"], ["b", "c"], ["c", "a"]]},
                 "sentence": "Ax Ey Loves(x, y)", "expect": {"seValue": "True", "seSat": "3 of 3 satisfy"}},
                {"id": "no-witness", "label": "a planet that orbits itself, and there is none",
                 "domain": ["a", "b", "c"], "names": {},
                 "predicates": {"Planet": ["a", "b"], "Orbits": [["a", "b"], ["b", "c"]]},
                 "sentence": "Ex (Planet(x) & Orbits(x, x))", "expect": {"seValue": "False", "seWitness": "—"}},
            ],
            "panel_title": "One sentence, evaluated in a model you can edit",
            "panel_intro": (
                "The domain lists the individuals, and each extension lists the "
                "individuals, or for two-place predicates the pairs, it holds of: "
                "ab means the pair a, b. Read the value and the witness in the "
                "first preset, then choose the second, which differs only by one "
                "pair. Then edit the extension yourself and find the smallest "
                "change that turns each False into True."
            ),
        }),
        "steps_title": "Evaluating a sentence in a model",
        "steps_intro": "Five steps, the same for any sentence and any model.",
        "steps": [
            ("Write down the model",
             "List the individuals, the extension of each predicate, and the "
             "referent of each name. If the sentence uses a predicate the model "
             "does not list, the model is incomplete."),
            ("Find the outermost connective or quantifier",
             "That is the last thing the sentence does, and it fixes what has to "
             "be checked first."),
            ("Check a universal at every individual, an existential at some",
             "Put each individual for the variable in turn. A universal is refuted "
             "by one failure; an existential is confirmed by one success."),
            ("Evaluate the parts first",
             "At each individual the part is a smaller sentence. Evaluate it the "
             "same way, down to atomic sentences, and read those off the "
             "extensions."),
            ("Say which entry decided it",
             "Name the witness or the failing individual, and the pair or "
             "membership in the extension that put it there."),
        ],
        "worked": {
            "title": "Every planet orbits something, with and without one pair",
            "intro": [
                "The sentence is `∀x (Planet(x) → ∃y Orbits(x, y))`, read at each "
                "individual in turn.",
            ],
            "lines": [
                "model: Planet a b;  Orbits ab bc",
                "x = a:  Planet(a) T,  y = b works,  so T",
                "x = b:  Planet(b) T,  y = c works,  so T",
                "x = c:  Planet(c) F,  so the conditional is T",
                "every x passes:  True",
                "remove bc:  x = b has Planet(b) T and no y,  so F",
                "one x fails:  False, at x = b",
            ],
            "after": [
                "The sentence did not change, and neither did the domain. The "
                "value moved because the extension of `Orbits` did, which is "
                "what it is for a sentence to be true in a model and not "
                "otherwise.",
            ],
        },
        "quiz_title": "Reading a model",
        "quiz": [
            {"q": "In the first model, why is `Planet(c) → ∃y Orbits(c, y)` true even "
                  "though `c` orbits nothing?",
             "a": ["Because `c` is a planet that orbits something outside the model",
                   "Because the conditional is only evaluated at individuals that "
                   "orbit something",
                   "Because the antecedent `Planet(c)` is false, which makes a "
                   "conditional true",
                   "Because a universal sentence is true when most individuals pass"],
             "c": 2,
             "why": "A conditional with a false antecedent is true by its table. "
                    "The first choice puts `c` in the extension of `Planet`, which "
                    "it is not, and goes outside a model that has no outside. The "
                    "second invents a restriction the rule does not have. The last "
                    "is false of every universal sentence: one failure refutes it."},
            {"q": "The pair `b` and `c` is removed from `Orbits`. Which statement "
                  "about the sentence `∀x (Planet(x) → ∃y Orbits(x, y))` is correct?",
             "a": ["It is false, because `x = b` has no `y` that `b` orbits",
                   "It is still true, because the sentence has not changed",
                   "It has no value until the domain is changed too",
                   "It is false, because `x = a` now fails"],
             "c": 0,
             "why": "The planet `b` is in the extension of `Planet` and now orbits "
                    "nothing, so the conditional fails there. The unchanged wording "
                    "does not keep the value, since the value depends on the "
                    "extension. The domain needs no change, and `a` still orbits "
                    "`b`, so it passes."},
            {"q": "The sentence `∃x (Planet(x) ∧ Orbits(x, x))` is False in the "
                  "first model. What does that show?",
             "a": ["Orbiting oneself is impossible",
                   "No individual of this model is a planet that orbits itself",
                   "The sentence is false in every model",
                   "The sentence is meaningless"],
             "c": 1,
             "why": "An existential is false in a model when no individual satisfies "
                    "its part, and that is all the lab found. It says nothing about "
                    "what is possible, or about other models, where a self-orbiting "
                    "planet could be listed; and a sentence with a perfectly "
                    "definite truth condition is not meaningless."},
            {"q": "Someone says: “I know what the sentence means, so I know "
                  "whether it is true.” Using this lesson, what is wrong?",
             "a": ["Knowing what it means gives its truth conditions, but whether "
                   "they are met depends on which model is actual",
                   "Nothing: knowing the meaning is knowing the truth value",
                   "A sentence has truth conditions only if it is true",
                   "The value cannot be known in a finite model"],
             "c": 0,
             "why": "Truth conditions are a rule from models to values. Applying "
                    "the rule needs a model. The second choice runs the two "
                    "together; the third reverses the order, since a false sentence "
                    "has truth conditions as well; and the last is wrong because a "
                    "finite model can be evaluated exactly, as the lab does."},
        ],
        "mistakes": [
            ("Thinking a sentence is true or false on its own",
             "The lab evaluates the same sentence in two models that differ by one "
             "pair, and prints True in one and False in the other. A sentence has "
             "truth conditions; a value belongs to the sentence together with a "
             "model. What it is natural to call the sentence's truth is its value "
             "in the model you had in mind."),
            ("Reading a universal as a statement about most",
             "`∀x A` fails when one individual fails. In a domain of a hundred, "
             "ninety-nine passing individuals and one failing one leave the "
             "sentence False. Use the failing individual the lab names to find "
             "the one that decides it."),
            ("Reading a false antecedent as a failure",
             "In `Planet(x) → ∃y Orbits(x, y)` the individual `c` is not a planet, "
             "so the conditional is true there and `c` is not what the sentence "
             "is about. The failing individual in the second model is a planet, "
             "which is why it fails."),
        ],
        "standard": (
            "Finish when you can evaluate a sentence in a model and say why.",
            "Given a finite model and a quantified sentence, you should be able "
            "to evaluate it from the values of its parts, name the witness or the "
            "failing individual, and say which single change to an extension "
            "would reverse the value. An answer that gives only True or False "
            "has not shown the evaluation."
        ),
        "note": (
            "Compositional semantics for a fragment of a language is the "
            "foundation of the field; this lesson does the fragment where "
            "evaluation is a finite check. English does not come with its "
            "model, and which one is in view is part of what speakers are "
            "doing."
        ),
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "names-reference-and-identity-statements",
        "title": "Names, Reference and Identity Statements",
        "module": "Language",
        "one_line": "Give two names one referent, evaluate their identity statement as true, and say why it can still be news.",
        "summary": (
            "In a model a name is a pointer to an individual, so two names for "
            "one individual make an identity statement true. Yet "
            "&ldquo;Hesperus is Phosphorus&rdquo; was a discovery. Evaluate it in "
            "a model, see what the model cannot show, and use Frege's distinction "
            "between sense and reference to say what is missing."
        ),
        "key": [
            "a name points at an individual in the model",
            "h = p is true when both name a",
            "the model shows reference, not sense",
            "a = a is trivial; a = b can be news",
            "same reference, different sense",
        ],
        "key_label": "Reference is not meaning",
        "concepts_intro": (
            "The last lesson let a sentence be evaluated in a model. This one "
            "asks what a name contributes to the value, and finds that it "
            "contributes less than its meaning."
        ),
        "concepts": [
            ("In a model, a name is its referent",
             "The model says which individual each name picks out, and a sentence "
             "containing the name is evaluated using that individual and nothing "
             "else. Two names that pick out the same individual make the same "
             "contribution to every value."),
            ("An identity statement can be informative",
             "&ldquo;Hesperus is Hesperus&rdquo; is known to anyone. "
             "&ldquo;Hesperus is Phosphorus&rdquo; had to be found out. In the "
             "model both are true, for the same reason, and the model cannot tell "
             "them apart."),
            ("Sense is the way the referent is given",
             "Frege's answer is that a name has a sense as well as a referent: "
             "the evening star and the morning star are two ways of being given "
             "one planet. The model records the planet, so it records the "
             "reference and leaves the sense out."),
        ],
        "read_title": "One planet, two names",
        "read_intro": (
            "The model that makes the identity true, the model that makes it "
            "false, and what neither of them records."
        ),
        "body": [
            ("def", ("Reference and sense",
                     "The <strong>reference</strong> of a name is the individual it "
                     "picks out. Its <strong>sense</strong>, on Frege's view, is the "
                     "way that individual is presented, the information that goes "
                     "with using the name. Two names can share a reference and "
                     "differ in sense.")),
            ("p", "The old example is a pair of names. People saw a bright light in "
                  "the evening sky and named it Hesperus. They saw a bright light "
                  "in the morning sky and named it Phosphorus. It was later "
                  "established that these were one planet, Venus. Let `h` be the "
                  "name Hesperus and `p` the name Phosphorus."),
            ("p", "A model for this has two individuals, `a` for the planet and "
                  "`b` for something else, say another planet. The predicate "
                  "`Shines` holds of `a` alone. The names are given referents: `h` "
                  "picks out `a`, and `p` picks out `a`. Evaluate `h = p`. The "
                  "sentence is true when its two terms pick out the same "
                  "individual; they both pick out `a`; the lab prints True."),
            ("p", "The model also makes `∀x (x = h → x = p)` true: whatever is "
                  "Hesperus is Phosphorus. And because the value of a sentence is "
                  "built from the referents of the names in it, you can put `p` "
                  "where `h` stood, anywhere, and the value cannot move. "
                  "`Shines(h)` and `Shines(p)` are true together or false "
                  "together."),
            ("p", "Now give `p` the referent `b`. The identity is False, and the "
                  "uniqueness sentence fails at `a`: the individual `a` is "
                  "Hesperus but is not Phosphorus. This model is just as easy to "
                  "write down as the first. It is a perfectly good description "
                  "of how things might have been, and for the early astronomers "
                  "it was a live candidate for how things were. Learning "
                  "that `h = p` was true was learning which of the two models "
                  "described the sky."),
            ("p", "So the model contains the discovery in one sense and misses it in "
                  "another. It contains it as the difference between the two "
                  "referent assignments. It misses why an astronomer could "
                  "sincerely say that Hesperus is visible in the evening and wonder "
                  "whether Phosphorus is, which no sentence the lab evaluates can "
                  "express once `h` and `p` share an individual. Frege's account "
                  "is that the two names come with different senses, and that "
                  "the astronomer's belief goes by sense. The lab has no senses "
                  "to hold and no beliefs to report, and the lesson does not "
                  "pretend it does."),
            ("p", "Putnam's Twin Earth shows the same gap from the other side. "
                  "Take the sentence &ldquo;water is H2O&rdquo;, written "
                  "`∀x (Water(x) ↔ H2O(x))`. In the first model the individual `a` "
                  "is water and H2O, and `b` is a different liquid, XYZ. The "
                  "sentence is True. In the second the word `Water` is applied to "
                  "the stuff around the speakers there, which is XYZ, "
                  "so its extension holds `b` and the sentence is False; the lab "
                  "names `a` as the first place it fails, since `a` is H2O and not "
                  "water there. "
                  "The sentence is the same string. What the speakers have in their "
                  "heads can be the same on both planets, and Putnam's claim is "
                  "that the meaning of the word is not in the head alone. The lab "
                  "shows only that extension is fixed by the model, not by the "
                  "sentence."),
            ("p", "The corrective to take away is narrow. Two names with the same "
                  "reference give the same value in every sentence the lab can "
                  "evaluate. That does not make them the same name, or give them the "
                  "same meaning in the sense of the word that explains why "
                  "&ldquo;Hesperus is Phosphorus&rdquo; was news."),
        ],
        "lab": ("argkit", {
            "mode": "semantics",
            "preset": "hesperus",
            "presets": [
                {"id": "hesperus", "label": "two names, one planet",
                 "domain": ["a", "b"], "names": {"h": "a", "p": "a"},
                 "predicates": {"Shines": ["a"]},
                 "sentence": "h = p", "expect": {"seValue": "True"}},
                {"id": "distinct", "label": "two names, two bodies",
                 "domain": ["a", "b"], "names": {"h": "a", "p": "b"},
                 "predicates": {"Shines": ["a"]},
                 "sentence": "h = p", "expect": {"seValue": "False"}},
                {"id": "whatever-h-is", "label": "whatever is h is p, with one planet",
                 "domain": ["a", "b"], "names": {"h": "a", "p": "a"},
                 "predicates": {"Shines": ["a"]},
                 "sentence": "Ax (x = h -> x = p)", "expect": {"seValue": "True", "seSat": "2 of 2 satisfy"}},
                {"id": "earth", "label": "water is H2O, on Earth",
                 "domain": ["a", "b"], "names": {},
                 "predicates": {"Water": ["a"], "H2O": ["a"], "XYZ": ["b"]},
                 "sentence": "Ax (Water(x) <-> H2O(x))", "expect": {"seValue": "True", "seSat": "2 of 2 satisfy"}},
                {"id": "twin-earth", "label": "water is H2O, on Twin Earth",
                 "domain": ["a", "b"], "names": {},
                 "predicates": {"Water": ["b"], "H2O": ["a"], "XYZ": ["b"]},
                 "sentence": "Ax (Water(x) <-> H2O(x))", "expect": {"seValue": "False", "seWitness": "fails at x = a"}},
            ],
            "panel_title": "Which individual does each name pick out?",
            "panel_intro": (
                "The names field assigns each name an individual. Read the value of "
                "the identity in the first preset, then in the second, which moves "
                "only the referent of one name. The last two presets keep one "
                "sentence and change the extensions; change a name or an extension "
                "yourself and see whether any sentence can tell h from p when they "
                "share a referent."
            ),
        }),
        "steps_title": "Telling reference from sense",
        "steps_intro": "Five steps for any identity statement that looks like news.",
        "steps": [
            ("Give each name a referent",
             "Say in the model which individual each name picks out. An identity "
             "statement is true exactly when its two terms pick out one."),
            ("Evaluate the identity",
             "Read the value. A True here means the names are co-referring; it "
             "does not say the names mean the same."),
            ("Substitute one name for the other",
             "Replace one by the other in a sentence the model can evaluate. If "
             "the names share a referent, the value cannot change."),
            ("Ask what a speaker could still doubt",
             "If a speaker could accept one sentence and doubt the other, the "
             "difference is not in the reference. It is in the way the referent "
             "is given."),
            ("Say what the model leaves out",
             "Name the sense, or the ignorance of which model is actual, that the "
             "table has no place for."),
        ],
        "worked": {
            "title": "Hesperus is Phosphorus",
            "intro": [
                "One sentence in two models, and a second sentence in each.",
            ],
            "lines": [
                "model 1:  h = a,  p = a",
                "  h = p:  a = a,  True",
                "  ∀x (x = h → x = p):  at x = a, T → T,  True",
                "model 2:  h = a,  p = b",
                "  h = p:  a = b,  False",
                "  ∀x (x = h → x = p):  at x = a, T → F,  False",
            ],
            "after": [
                "In the first model the names are interchangeable everywhere the "
                "lab can look, and still &ldquo;Hesperus is Phosphorus&rdquo; is "
                "not the trivial sentence that &ldquo;Hesperus is Hesperus&rdquo; "
                "is. That is Frege's point: the extra is the sense, and the model "
                "does not hold it.",
            ],
        },
        "quiz_title": "Names in a model",
        "quiz": [
            {"q": "In the model where `h` and `p` both pick out `a`, what does the "
                  "lab report for `h = p`, and why?",
             "a": ["False, because the names are different words",
                   "False, because an identity must be discovered to be true",
                   "True, because both names pick out the same individual",
                   "It cannot be evaluated until the names have senses"],
             "c": 2,
             "why": "An identity sentence is true when its terms pick out one "
                    "individual, and the words are different but the individual "
                    "is not. The first two choices make the value depend on the "
                    "spelling or on the history of finding out, neither of which "
                    "the model contains. Senses are not needed to evaluate "
                    "anything in a model."},
            {"q": "The names `h` and `p` pick out the same individual. Which "
                  "statement does the model force?",
             "a": ["`Shines(h)` and `Shines(p)` are true together or false together",
                   "Every speaker who accepts `Shines(h)` accepts `Shines(p)`",
                   "`h` and `p` have the same sense",
                   "`h = p` is a priori for every speaker"],
             "c": 0,
             "why": "Sentences differing only by the swap are evaluated from the "
                    "same individual, so they agree. The other three go beyond what "
                    "the model holds: what speakers accept, what senses names have "
                    "and what is a priori are exactly what a model of reference "
                    "leaves out."},
            {"q": "Frege's puzzle is that `h = h` and `h = p` have the same value in "
                  "the model. What is the puzzle?",
             "a": ["That the lab gets one of the values wrong",
                   "That the two sentences differ in what they tell a speaker, "
                   "although the model gives them one value for one reason",
                   "That a name must have a different referent in each sentence",
                   "That an identity can never be false"],
             "c": 1,
             "why": "The puzzle is the gap between sameness of value and sameness of "
                    "information: the first sentence is trivial and the second may "
                    "be a discovery. The lab computes the values correctly. "
                    "Referents may be reassigned between models but not within "
                    "one, and an identity is false in the second preset."},
            {"q": "On Earth `Water` holds of `a`, on Twin Earth of `b`, and the "
                  "sentence `∀x (Water(x) ↔ H2O(x))` is the same on both. What does "
                  "the difference in value show about the lab?",
             "a": ["That Twin Earth is impossible",
                   "That the sentence is true in every model",
                   "That the two planets must use different logic",
                   "That the value of a sentence depends on the extension the "
                   "model gives its words, which the sentence does not fix"],
             "c": 3,
             "why": "The value depends on the model, and the extensions differ. "
                    "Nothing about possibility is asked of the lab, and the sentence "
                    "is False in one of the two models, so it is not true in "
                    "every model. The logic of evaluation is the same in both; "
                    "only the extension of one predicate changed."},
        ],
        "mistakes": [
            ("Thinking that if a = b is true, the two names mean the same",
             "The model makes `h = p` true, because both names point at `a`. But "
             "the astronomer who first met both names was told something by "
             "&ldquo;Hesperus is Phosphorus&rdquo;, and was told nothing by "
             "&ldquo;Hesperus is Hesperus&rdquo;, though the model evaluates them "
             "alike. Sameness of reference is a fact about the pointer. Sameness of "
             "meaning, if the sentences carry different information, is a further "
             "matter."),
            ("Reading the lab as a theory of belief",
             "The lab swaps `p` for `h` in a sentence and the value does not move. "
             "It cannot say what anyone believes or doubts, because a belief report "
             "is not evaluated from the referents alone. That the lab agrees the "
             "two sentences have one value shows nothing about whether a person "
             "can hold one and doubt the other."),
            ("Treating the Twin Earth preset as a proof about meaning",
             "The two presets show that the same sentence takes two values when "
             "the extension of one word differs. They do not show where the "
             "meaning of the word lives, since the lab has no head to put it in. "
             "Putnam's claim that it is not only in the head is an argument "
             "about speakers, and the lab only illustrates the premise that "
             "extension varies."),
        ],
        "standard": (
            "Finish when you can separate what a name points at from what it adds.",
            "Given two names and a model, you should be able to say whether "
            "their identity is true, show that swapping them cannot change a "
            "value, and say in a sentence what an informative identity carries "
            "that the model does not."
        ),
        "note": (
            "Whether sense is the right repair for Frege's puzzle is disputed, "
            "and so is the further question how a name comes to be attached to "
            "its bearer. This lesson teaches the puzzle and the first answer, "
            "and the lab keeps them apart from the model."
        ),
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "definite-descriptions-and-the-king-of-france",
        "title": "Definite Descriptions and the Present King of France",
        "module": "Language",
        "one_line": "Expand “the F is G” in Russell's way, and read the three cases of one thing, nothing, and too many.",
        "summary": (
            "&ldquo;The present King of France is bald&rdquo; looks like a "
            "sentence about a king, and there is none. Russell reads it as a claim "
            "that there is exactly one king and that he is bald. Evaluate that "
            "expansion in a model for the three cases, and see where Strawson "
            "disagrees about what to call the result."
        ),
        "key": [
            "the F is G  =  one F, and it is G",
            "there is an F, at most one F, and G",
            "no F: Russell says false",
            "two Fs: false, even if both are G",
            "Strawson: a failed presupposition",
        ],
        "key_label": "A description is a claim, not a name",
        "concepts_intro": (
            "The previous lesson let a name point at an individual. A description "
            "such as &ldquo;the king&rdquo; looks like a name, and Russell's "
            "claim is that it is not one."
        ),
        "concepts": [
            ("A description asserts three things",
             "&ldquo;The F is G&rdquo; says that something is an F, that nothing "
             "else is an F, and that the one thing that is an F is G. All three are "
             "part of what is said, and each can fail."),
            ("Three cases",
             "The F can be there once, not at all, or more than once. Only the "
             "first can make the sentence true, and the other two make the "
             "expansion false by different clauses."),
            ("Russell and Strawson read the second case differently",
             "Russell calls the sentence false, because its existence clause is "
             "false. Strawson says the sentence presupposes a king, and if there "
             "is none the question of truth does not arise. They agree about the "
             "model, and differ on the name for the result."),
        ],
        "read_title": "Expanding a description",
        "read_intro": (
            "The expansion, the three models that fit it, and the dispute over "
            "the empty one."
        ),
        "body": [
            ("def", ("Definite description",
                     "A <strong>definite description</strong> is a phrase of the "
                     "form &ldquo;the F&rdquo;, such as &ldquo;the author of "
                     "Waverley&rdquo; or &ldquo;the present King of France&rdquo;. "
                     "It is used to speak of one thing by saying what that thing "
                     "is like.")),
            ("p", "On the surface a description behaves like a name: "
                  "&ldquo;the King of France is bald&rdquo; has a subject and a "
                  "predicate and seems to be about the king. The trouble is that "
                  "there is no king, and a sentence cannot be about a thing that is "
                  "not there. If it is meaningful, as it plainly is, then either "
                  "there is some such thing, or the surface form misleads."),
            ("p", "Russell's analysis holds that the surface misleads. &ldquo;The "
                  "F is G&rdquo; is a quantified sentence with three clauses."),
            ("math", [
                "∃x ( F(x)  ∧  ∀y ( F(y) → y = x )  ∧  G(x) )",
            ]),
            ("p", "Read it as: there is an `x` that is an `F`, any `y` that is an "
                  "`F` is that `x`, and that `x` is `G`. The first clause says there "
                  "is an F, the second that there is no more than one, and the "
                  "third says what the one is like. The lab takes a phrase of the "
                  "form &ldquo;the x such that F holds of x&rdquo;, followed by the "
                  "predicate G, and expands it this way."),
            ("p", "Three models cover the cases. In the first, the domain has "
                  "individuals `a`, `b` and `c`; `Author` holds of `b` alone, and "
                  "`Scot` holds of `b` and `c`. The description picks out `b`, the "
                  "one and only author. `b` is a Scot, and the sentence is True, "
                  "with the description denoting `b`."),
            ("p", "In the second, `King` holds of nobody, and `Bald` holds of `a`. "
                  "The first clause fails: no `x` is a king. Whatever the third "
                  "clause says, the conjunction cannot hold, and the lab prints "
                  "False. It also reports that the description denotes nothing, "
                  "which is the fact Strawson builds on."),
            ("p", "In the third, `King` holds of `a` and of `b`, and both are "
                  "bald. The first clause is met. The second is not, since `b` is "
                  "a king and is not `a`, and the lab prints False, reporting "
                  "that the description is not unique, and naming `a` and `b`. "
                  "That both kings are bald does not help, because the sentence "
                  "claims there is just one."),
            ("p", "Now the dispute. Strawson's observation is about what people say. "
                  "Asked whether the present King of France is bald, almost no one "
                  "answers &ldquo;no&rdquo;; they say there is no such king. The "
                  "sentence, he held, presupposes that there is a king, and when the "
                  "presupposition fails the sentence is neither true nor false. "
                  "Russell's reply is that the sentence does say that there is a "
                  "king, so it is false, as &ldquo;there is a king who is "
                  "bald&rdquo; is false. The lab computes only the expansion, so it "
                  "prints Russell's False in the value tile, and in the tile for the "
                  "description it prints the fact on which Strawson relies. Which "
                  "tile to treat as the sentence's status is the philosophical "
                  "choice, and it is not one the arithmetic makes for you."),
            ("p", "What the expansion buys is a way to say that the sentence is "
                  "meaningful although nothing is denoted: the description was "
                  "never a name, only a bundle of claims. Its price is a "
                  "complication for the grammar, since &ldquo;the King of "
                  "France&rdquo; no longer behaves as a single phrase. The next "
                  "lesson turns that complication into a second reading."),
        ],
        "lab": ("argkit", {
            "mode": "semantics",
            "preset": "king",
            "presets": [
                {"id": "king", "label": "no king of France, and one bald man",
                 "domain": ["a", "b", "c"], "names": {},
                 "predicates": {"King": [], "Bald": ["a"]},
                 "sentence": "[the x: King(x)] Bald(x)", "expect": {"seValue": "False", "seDesc": "denotes nothing"}},
                {"id": "author", "label": "one author, and he is a Scot",
                 "domain": ["a", "b", "c"], "names": {},
                 "predicates": {"Author": ["b"], "Scot": ["b", "c"]},
                 "sentence": "[the x: Author(x)] Scot(x)", "expect": {"seValue": "True", "seDesc": "denotes b"}},
                {"id": "two-kings", "label": "two kings, both bald",
                 "domain": ["a", "b", "c"], "names": {},
                 "predicates": {"King": ["a", "b"], "Bald": ["a", "b"]},
                 "sentence": "[the x: King(x)] Bald(x)", "expect": {"seValue": "False", "seDesc": "not unique: a, b"}},
            ],
            "panel_title": "One thing, nothing, or too many",
            "panel_intro": (
                "The description tile reports what the restrictor picks out in the "
                "model: one individual, nobody, or several. Read it with the "
                "value for each preset. Then edit the extension of King in the "
                "first preset: put a in it and watch the value change, then put "
                "b in it as well."
            ),
        }),
        "steps_title": "Evaluating a description",
        "steps_intro": "Five steps. The description tile is the one to read first.",
        "steps": [
            ("Pick out the restrictor",
             "In “the F is G” the F is the descriptive part. List the "
             "individuals of the model that satisfy it."),
            ("Count them",
             "None, one or several. This is the case, and it decides which clause "
             "of the expansion can fail."),
            ("Apply the three clauses",
             "There is an F; there is no more than one; it is G. All three are "
             "needed for True."),
            ("Read the value as Russell does",
             "A missing F and a doubled F both make the expansion False, by "
             "different clauses. Say which."),
            ("Say what Strawson would say",
             "For an empty description, the presupposition has failed. State the "
             "disagreement as one about what to call the result, not about the "
             "model."),
        ],
        "worked": {
            "title": "The present King of France is bald",
            "intro": [
                "Russell's expansion, applied to a model in which `King` holds "
                "of no one.",
            ],
            "lines": [
                "claim:  ∃x ( King(x) ∧ ∀y ( King(y) → y = x ) ∧ Bald(x) )",
                "model:  King holds of nobody,  Bald holds of a",
                "clause 1, something is a king:  no x,  False",
                "the conjunction cannot hold:  False",
                "description tile:  denotes nothing",
                "Russell:  False.  Strawson:  presupposition fails",
            ],
            "after": [
                "Both readings of the same fact are available at once. The "
                "expansion gives False because its first clause is false, and "
                "the description tile says the same thing in Strawson's words. "
                "The lab does not choose between them.",
            ],
        },
        "quiz_title": "The three cases",
        "quiz": [
            {"q": "In the model with no king, what does Russell's expansion of "
                  "“the King is bald” give?",
             "a": ["True, because nobody who is a king is not bald",
                   "No value, since the sentence is about nothing",
                   "True, because `Bald` holds of someone",
                   "False, because the clause that something is a king fails"],
             "c": 3,
             "why": "The first clause of the expansion asserts a king, and there "
                    "is none, so the conjunction is false. The first choice is "
                    "the vacuous truth of a universal, which is not what the "
                    "expansion says. The second is Strawson's reading, not "
                    "Russell's. The third confuses who is bald with who is king."},
            {"q": "Two individuals are kings and both are bald. What does the lab "
                  "print for “the King is bald”, and why?",
             "a": ["True, because every king is bald",
                   "False, because the uniqueness clause fails",
                   "False, because neither of them is bald",
                   "True, because at least one king is bald"],
             "c": 1,
             "why": "The expansion adds that there is no more than one king, and "
                    "here there are two, so it is False even though the third "
                    "clause is satisfied by each. Every king being bald is not "
                    "what the sentence says, and neither is one of them being "
                    "bald. The third choice gives a false reason, since both are "
                    "bald in this model."},
            {"q": "A reader says Russell's account gives the sentence about the "
                  "King of France no truth value. What is the best reply?",
             "a": ["Russell's expansion gives it the value False, and it is "
                   "Strawson who leaves it without one",
                   "Russell would agree, and add that such sentences are "
                   "meaningless",
                   "The lab shows it has no value because the description tile "
                   "says nothing is denoted",
                   "Both give the same status, only in different words"],
             "c": 0,
             "why": "On Russell's account the sentence is a false claim, which is "
                    "how the lab's value tile reads. Strawson's view is that the "
                    "question of truth does not arise. The second choice confuses "
                    "the two. The description tile reports the failed presupposition "
                    "and the value tile still says False. The last is wrong because "
                    "they differ on this very point."},
            {"q": "Why does the expansion let the sentence be meaningful although "
                  "there is no king?",
             "a": ["Because the model quietly includes a king",
                   "Because meaning is the same as reference",
                   "Because “the king” is not a name, but part of a quantified "
                   "claim that can be false",
                   "Because every sentence about nothing is false"],
             "c": 2,
             "why": "On the expansion nothing needs to be denoted for the "
                    "sentence to have truth conditions; it is a claim about what "
                    "there is. The first choice contradicts the model, the second "
                    "reverses the previous lesson, and the last is false: a "
                    "negated description may come out True, as the next lesson "
                    "shows."},
        ],
        "mistakes": [
            ("Saying the sentence has no truth value on Russell's account",
             "In the model with no king the lab prints False for Russell's "
             "expansion, because its first clause asserts a king. It is Strawson "
             "who withholds a value, and the description tile shows the fact he "
             "does so on. The mistake mixes up the two positions, and is common "
             "because the sentence still strikes most people as odd to call "
             "false."),
            ("Thinking that a doubled description is true if every F is G",
             "With two kings, both bald, the lab prints False and lists "
             "both. The expansion has a uniqueness clause, and &ldquo;the&rdquo; "
             "is what puts it there. Every king being bald is a different "
             "sentence."),
            ("Treating a description as a name that happens to fail",
             "A name points at an individual of the model, and a name with no "
             "individual is a model error. A description is evaluated by looking "
             "at the extension of its restrictor, which may be empty, and an "
             "empty one makes the sentence false rather than making it "
             "unparseable."),
        ],
        "standard": (
            "Finish when you can expand a description and name the clause that fails.",
            "Given a sentence of the form &ldquo;the F is G&rdquo; and a model, you "
            "should be able to write Russell's three clauses, evaluate them, say "
            "whether the description denotes one thing, nothing or several, and "
            "state what Strawson would call the empty case."
        ),
        "note": (
            "Whether ordinary speakers use descriptions as Russell says is a "
            "question about language use that this lesson does not settle; "
            "Strawson and later writers argued it does not fit. What the lesson "
            "teaches is the analysis as something with a checkable value."
        ),
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "scope-ambiguity-and-negation",
        "title": "Scope Ambiguity and Negation",
        "module": "Language",
        "one_line": "Evaluate one sentence in one model under two scopes of its negation or quantifiers, and get two values.",
        "summary": (
            "A negation can sit outside a description or inside it, and two "
            "quantifiers can come in either order. Each placement is a "
            "different formula with its own value. Evaluate &ldquo;the King is "
            "not bald&rdquo; and &ldquo;everyone loves someone&rdquo; under both "
            "scopes in a single model, and find the models in which the readings "
            "agree."
        ),
        "key": [
            "scope: what a ¬ or a quantifier covers",
            "¬ before the F, or after it: two readings",
            "∀x ∃y  against  ∃y ∀x: two readings",
            "one sentence, two values, one model",
            "∃y ∀x  implies  ∀x ∃y, not the reverse",
        ],
        "key_label": "One sentence can hold two formulas",
        "concepts_intro": (
            "The last lesson turned a description into a quantified claim. A "
            "quantified claim has a scope, and a sentence with two scope-taking "
            "parts can be placed in more than one order."
        ),
        "concepts": [
            ("Scope is the part a word governs",
             "A negation governs what follows inside its brackets, and a "
             "quantifier governs the formula it binds. Moving a negation across "
             "a quantifier, or a quantifier across another, changes which "
             "formula the sentence is."),
            ("English leaves scope to be recovered",
             "&ldquo;The King is not bald&rdquo; and &ldquo;everyone loves "
             "someone&rdquo; each fit more than one formula. The words do not "
             "say which, and a hearer chooses by context."),
            ("Two readings can have two values",
             "In one model the readings of one sentence can differ in value, "
             "which is a sharp test that they are not the same reading."),
        ],
        "read_title": "Two scopes, one model",
        "read_intro": (
            "Negation and a description first, then two quantifiers, then when "
            "the readings agree."
        ),
        "body": [
            ("def", ("Scope",
                     "The <strong>scope</strong> of a negation or a quantifier is "
                     "the part of the formula it applies to. A sentence is "
                     "<strong>scope ambiguous</strong> when its words fit two "
                     "formulas that differ only in scope.")),
            ("p", "Take &ldquo;the King is not bald&rdquo;, in the model of the "
                  "previous lesson in which nobody is a king. There are two "
                  "places to put the negation. Outside the description, it "
                  "denies the whole claim: it is not the case that there is one "
                  "king and he is bald. Inside, it is part of what is said of the "
                  "king: there is one king and he is not bald."),
            ("p", "Evaluate the wide one. The claim that the king is bald is "
                  "False, as in the previous lesson, because nobody is a king. "
                  "The negation of False is True, so with the negation outside "
                  "the sentence is True. Evaluate the narrow one. The expansion "
                  "now ends in `¬Bald(x)`, and still opens by asserting a king, "
                  "which there is not, so the sentence is False. The two "
                  "readings, in the same model, have opposite values."),
            ("math", [
                "reading    formula                          value",
                "-------------------------------------------------",
                "wide       ¬ (the king is bald)             True",
                "narrow     (the king) is not bald           False",
            ]),
            ("p", "That settles one thing about the ambiguity: it is not a "
                  "difference of style. Someone who says &ldquo;the King of France "
                  "is not bald&rdquo; and means the wide reading is saying what "
                  "is true, that the claim of baldness is false. Someone who "
                  "means the narrow reading is saying something false, since it "
                  "adds that there is a king. Russell used the distinction to "
                  "defend the law of excluded middle, which the sentence seemed "
                  "to threaten: either the king is bald or he is not, and "
                  "neither holds if there is no king, unless the second is "
                  "read with the negation outside."),
            ("p", "The same thing happens with two quantifiers, and the order "
                  "question of “Quantifiers and Their Order” in Arguments and "
                  "Validity returns in a model you can type. Take "
                  "&ldquo;everyone loves someone&rdquo;. One reading is "
                  "`∀x ∃y Loves(x, y)`: each person loves a person, who may differ. "
                  "The other is `∃y ∀x Loves(x, y)`: there is one person everyone "
                  "loves. Put three people in a ring, `a` loving `b`, `b` loving "
                  "`c` and `c` loving `a`. The first reading is True; each one "
                  "loves someone. The second is False; nobody is loved by all "
                  "three. The sentence in English is the same, and the two "
                  "formulas are not equivalent."),
            ("p", "They are related, though. If there is one person everyone "
                  "loves, then each person loves someone, namely that one. So "
                  "`∃y ∀x` implies `∀x ∃y`, and the ring shows that the "
                  "implication does not run back. In a model where `a`, `b` and "
                  "`c` all love `c`, both readings are True, with `c` as the "
                  "witness for the second."),
            ("p", "Readings can also agree. If the King is a real person and he is "
                  "not bald, both the wide negation and the narrow reading come out "
                  "True. A description that denotes something gives the two "
                  "placements one value, and the negation only separates "
                  "them where the description fails. That is why the ambiguity "
                  "went unnoticed for so long: in ordinary cases it makes no "
                  "difference."),
            ("p", "The lab evaluates the formulas, and it does not choose between "
                  "them. Which one a speaker meant is a question about the "
                  "speaker, and the lab has no access to it; the lesson's claim is "
                  "only that a careful hearer should ask."),
        ],
        "lab": ("argkit", {
            "mode": "semantics",
            "preset": "wide",
            "presets": [
                {"id": "wide", "label": "not: the King is bald, with no king",
                 "domain": ["a", "b", "c"], "names": {},
                 "predicates": {"King": [], "Bald": ["a"]},
                 "sentence": "~[the x: King(x)] Bald(x)", "expect": {"seValue": "True", "seDesc": "denotes nothing"}},
                {"id": "narrow", "label": "the King is not bald, with no king",
                 "domain": ["a", "b", "c"], "names": {},
                 "predicates": {"King": [], "Bald": ["a"]},
                 "sentence": "[the x: King(x)] ~Bald(x)", "expect": {"seValue": "False", "seDesc": "denotes nothing"}},
                {"id": "real-king", "label": "the King is not bald, with a king who is not",
                 "domain": ["a", "b", "c"], "names": {},
                 "predicates": {"King": ["a"], "Bald": ["b"]},
                 "sentence": "[the x: King(x)] ~Bald(x)", "expect": {"seValue": "True", "seDesc": "denotes a"}},
                {"id": "everyone-someone", "label": "everyone loves someone, in a ring",
                 "domain": ["a", "b", "c"], "names": {},
                 "predicates": {"Loves": [["a", "b"], ["b", "c"], ["c", "a"]]},
                 "sentence": "Ax Ey Loves(x, y)", "expect": {"seValue": "True", "seSat": "3 of 3 satisfy"}},
                {"id": "someone-everyone", "label": "someone is loved by everyone, in the same ring",
                 "domain": ["a", "b", "c"], "names": {},
                 "predicates": {"Loves": [["a", "b"], ["b", "c"], ["c", "a"]]},
                 "sentence": "Ey Ax Loves(x, y)", "expect": {"seValue": "False", "seSat": "0 of 3 satisfy"}},
            ],
            "panel_title": "The same model, read with each scope",
            "panel_intro": (
                "The first two presets share a model and differ only in where the "
                "negation sits. The last two share a ring of love and differ "
                "only in the order of the quantifiers. Read each pair against its "
                "partner, then edit the Loves extension until the two quantifier "
                "orders agree."
            ),
        }),
        "steps_title": "Resolving a scope ambiguity",
        "steps_intro": "Five steps, for a negation and for a pair of quantifiers alike.",
        "steps": [
            ("Find the scope-taking parts",
             "Look for a negation and for each quantifier or description. A "
             "sentence with only one of them cannot be ambiguous in this way."),
            ("Write each order as a formula",
             "Put the negation outside, then inside. Put one quantifier first, "
             "then the other. Each placement is its own formula."),
            ("Evaluate each in the model",
             "Use the same model for both. If they give the same value, this "
             "model does not tell the readings apart."),
            ("Find a model that separates them",
             "Change an extension until the two values differ. An empty "
             "description separates the negations, and a ring of love separates "
             "the quantifiers."),
            ("Say which reading was meant",
             "State why: the context, or what the speaker would have to be "
             "committed to. The lab cannot choose."),
        ],
        "worked": {
            "title": "The King is not bald, and the ring of love",
            "intro": [
                "Each sentence has two formulas. The model for the first has "
                "no king; the model for the second is a ring of three.",
            ],
            "lines": [
                "no king:  ¬ (the King is bald)",
                "   the King is bald is False,  so the negation is True",
                "no king:  the King is not bald",
                "   clause 1, something is a king:  no x,  False",
                "ring:  ∀x ∃y Loves(x, y)",
                "   a loves b,  b loves c,  c loves a:  True",
                "ring:  ∃y ∀x Loves(x, y)",
                "   no y is loved by a, b and c together:  False",
            ],
            "after": [
                "One sentence of English, in one model, takes both True and False "
                "depending on the formula. A reader who asked only whether the "
                "sentence is true would have had no way to answer.",
            ],
        },
        "quiz_title": "Placing the scope",
        "quiz": [
            {"q": "With no king in the model, what are the values of “not: the "
                  "King is bald” and “the King is not bald”?",
             "a": ["True and True",
                   "False and False",
                   "True and False, in that order",
                   "False and True, in that order"],
             "c": 2,
             "why": "The wide negation denies a False claim and is True. The narrow "
                    "reading still asserts a king, which is missing, and is False. "
                    "The readings are not equivalent here, so they cannot both be "
                    "True or both False, and the reverse order has the values "
                    "swapped."},
            {"q": "In the ring where `a` loves `b`, `b` loves `c` and `c` loves "
                  "`a`, which statement is correct?",
             "a": ["`∀x ∃y Loves(x, y)` is True and `∃y ∀x Loves(x, y)` is False",
                   "`∃y ∀x Loves(x, y)` is True and `∀x ∃y Loves(x, y)` is False",
                   "Both orders of the quantifiers are True",
                   "Both orders are False"],
             "c": 0,
             "why": "Each person loves someone, so the first is True. No one is "
                    "loved by all three, so the second is False. The second "
                    "choice has them reversed, and if the stronger reading were "
                    "true the weaker would be too. The ring gives the stronger "
                    "reading no witness, so not both are True, and the weaker "
                    "has one for each person, so not both are False."},
            {"q": "Why do the wide and narrow readings of “the King is not "
                  "bald” agree when a king exists and is not bald?",
             "a": ["Because a negation never matters",
                   "Because then the description denotes, so the claim of baldness "
                   "is False and the negation of it is True, and the narrow reading "
                   "is True as well",
                   "Because the lab cannot tell scopes apart",
                   "Because the king is bald in both"],
             "c": 1,
             "why": "When the description denotes a non-bald individual, the claim "
                    "that he is bald is False, so its wide negation is True, and "
                    "the narrow reading also says he is not bald, so it is True. "
                    "The first choice is false: the readings disagree in the "
                    "empty model. The lab evaluates each placement separately. "
                    "And in this model the king is not bald."},
            {"q": "Which implication between the quantifier orders is correct?",
             "a": ["`∀x ∃y` implies `∃y ∀x`",
                   "`∃y ∀x` implies `∀x ∃y`",
                   "Each implies the other",
                   "Neither implies the other"],
             "c": 1,
             "why": "If one person is loved by everyone, each person loves someone, "
                    "so the stronger reading implies the weaker. The ring is a "
                    "model of the weaker and not the stronger, which rules out "
                    "the reverse and so rules out equivalence. Since the first "
                    "direction does hold, 'neither' is also wrong."},
        ],
        "mistakes": [
            ("Believing a sentence has one logical form",
             "The same English sentence, “the King is not bald”, has "
             "a wide and a narrow reading. In the model with no king the lab "
             "gives True for the first and False for the second. Taking one "
             "form to be the form is a choice, and in ordinary cases, where the "
             "description denotes, it costs nothing because the two readings agree."),
            ("Reading “everyone loves someone” as saying there is one beloved",
             "That is the second order, and in a ring of three it is False while "
             "the first order is True. Someone who hears the first and answers "
             "&ldquo;but who?&rdquo; has supplied the second."),
            ("Moving a negation across a quantifier as if it were free",
             "`¬∀x A` and `∀x ¬A` "
             "differ, as `¬∃x A` and `∃x ¬A` do. In the model with no king, "
             "shifting the negation from outside the description to inside "
             "changed True to False. Moving it needs a rule, and the rule "
             "exchanges `∀` and `∃`."),
        ],
        "standard": (
            "Finish when you can give both readings and a model that separates them.",
            "Given an ambiguous sentence with a negation or two quantifiers, you "
            "should be able to write each formula, evaluate both in one model, "
            "and change the model until their values differ."
        ),
        "note": (
            "Scope is one of several sources of ambiguity, and linguists argue "
            "about which readings a sentence has. The lesson treats the "
            "readings as given and teaches how to tell them apart."
        ),
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "vagueness-and-the-sorites",
        "title": "Vagueness and the Sorites",
        "module": "Language",
        "one_line": "Run the heap argument under four treatments, say what each gives up, and say why the cutoff and the range inherit a second problem.",
        "summary": (
            "One grain is not a heap, and adding one grain never makes a heap, so "
            "ten thousand grains are not a heap. Run the chain of tolerance "
            "conditionals under classical logic, a sharp cutoff, a borderline "
            "range and degrees of truth, say what each treatment denies, and "
            "state higher-order vagueness as the problem the cutoff and range "
            "inherit."
        ),
        "key": [
            "each step true, the end false: sorites",
            "classical: all true, the end absurd",
            "cutoff: one false, nobody can say which",
            "range: borderline cases, edges also vague",
            "degrees: each 9999/10000, the end 0",
        ],
        "key_label": "Four treatments, four costs",
        "concepts_intro": (
            "The chain is one you have run before, as a slope in “Slippery Slopes "
            "and Small Differences” and as the ship in “The Ship of Theseus”. "
            "There the four treatments were four verdicts on an argument. Here "
            "the argument is the original heap, and the question is what each "
            "treatment says vagueness is, and what each must still say about its "
            "own line. The course on paradoxes takes the heap up again."
        ),
        "concepts": [
            ("A tolerance premise is plausible for each step",
             "If a number of grains is a heap, one grain fewer is still a heap. "
             "Each such conditional looks true taken alone, and a chain of them "
             "from ten thousand grains to none is valid by modus ponens."),
            ("Four treatments, each at a price",
             "Classical logic keeps every conditional and accepts the absurd end. "
             "A sharp cutoff makes one conditional false. A borderline range "
             "makes some neither true nor false. Degrees make each nearly true "
             "and the end wholly false."),
            ("Higher-order vagueness",
             "Wherever a treatment draws a line, the line is itself hard to place. "
             "The cutoff is sharp and unknowable, the edges of the range are "
             "vague, and the degrees are exact numbers that no one could have "
             "chosen."),
        ],
        "read_title": "The heap, run four ways",
        "read_intro": (
            "The argument, then each treatment on the same chain, then the "
            "problem that remains."
        ),
        "body": [
            ("def", ("Vagueness",
                     "A predicate is <strong>vague</strong> when it has clear cases, "
                     "clear non-cases, and cases in between where there seems to be "
                     "no fact of the matter, and no sharp line between them. "
                     "&ldquo;Heap&rdquo;, &ldquo;bald&rdquo; and &ldquo;tall&rdquo; "
                     "are examples.")),
            ("p", "The argument: ten thousand grains of sand are a heap. For any "
                  "number `k` of grains, if `k` grains are a heap, so are `k − 1`. "
                  "So, by ten thousand steps of modus ponens, no grains are a "
                  "heap. Write `F(k)` for &ldquo;`k` grains are a heap&rdquo;. The "
                  "premises are `F(10000)` and ten thousand conditionals of the form "
                  "`F(k) → F(k − 1)`, and the conclusion is `F(0)`."),
            ("p", "The conclusion is absurd and the form is valid, so one of the "
                  "premises has to go, or the logic. The conditionals are not "
                  "individually doubtful. Taking away one grain cannot make the "
                  "difference between a heap and a non-heap, or if it could, the "
                  "word would not be the one we use. The lab runs the chain "
                  "under four treatments, and the same ten thousand steps give "
                  "four different pictures."),
            ("p", "Classical. Every conditional is True, `F(10000)` is True, and "
                  "ten thousand applications of modus ponens deliver `F(0)`: "
                  "the lab prints True for a heap of no grains. The paradox is "
                  "left standing. This is not a solution but the statement of the "
                  "problem, and the other three treatments deny a premise."),
            ("p", "Cutoff. There is a number at which a heap stops being one, and "
                  "the conditional at that number is False. The other "
                  "conditionals are True and the conclusion is False. The cost is "
                  "that nobody can say where the number is. A defender of this "
                  "view holds that the boundary exists and that we are ignorant of "
                  "it for a good reason: our grasp of the word is not fine enough "
                  "to discriminate adjacent counts, and so any particular count "
                  "we named would be a guess. The lab accepts any cutoff you type: "
                  "the first preset puts it at 5000 and reports one false "
                  "conditional, at `k = 5000`; the second moves it to 1000, the "
                  "false conditional moves with it, and the conclusion is False "
                  "under both."),
            ("p", "Range. There is a borderline region, say between 50 and 200 "
                  "grains, where it is neither true nor false that a count is a "
                  "heap. The conditionals inside the region are indeterminate: "
                  "the lab reports 150 of them, and shows the tolerance claim "
                  "that all of them hold as super-false. That is the supervaluation "
                  "idea: on every way of drawing a sharp line inside the region, "
                  "some conditional is false, so the universal claim is false on "
                  "all of them, though no single conditional is false on "
                  "all. The cost is that a disjunction can be true while neither "
                  "disjunct is, and that bivalence fails for the borderline "
                  "cases."),
            ("p", "Degrees. Truth comes in amounts between 0 and 1. `F(k)` has the "
                  "value `k / 10000`, and each conditional `F(k) → F(k − 1)` "
                  "has the value `9999/10000`, since the antecedent is one "
                  "step truer than the consequent, which on the Łukasiewicz "
                  "rule costs `1/10000`. Each premise is almost perfectly true. "
                  "But each application of modus ponens can lose that "
                  "`1/10000`, and after ten thousand the guaranteed value of "
                  "`F(0)` is 0. The lab prints 0. The cost is that validity no "
                  "longer carries near-truth from premises to conclusion: "
                  "ten thousand almost-true premises, an argument of an "
                  "unquestioned form, and a wholly false end."),
            ("p", "Higher-order vagueness is what remains. The range treatment "
                  "puts sharp edges at 50 and 200. But is 50 definitely not "
                  "borderline, and 49 definitely not a heap? If the edges are "
                  "themselves vague, the treatment needs a borderline region "
                  "around each, and then around those, and has traded one "
                  "arbitrary line for several. The cutoff treatment has a "
                  "sharp line that it concedes cannot be found. Degrees need "
                  "an exact number for each count, and the choice of "
                  "`k / 10000` is a sharp choice of the same kind. Each "
                  "treatment says where vagueness is not and then finds that "
                  "the place where it stops is vague."),
            ("p", "So the lab does not show which treatment is right. It shows "
                  "the verdict each gives and what that verdict denies: "
                  "a conditional, bivalence, or the transmission of truth "
                  "by valid argument. The reader chooses by the one they would "
                  "least mind paying."),
        ],
        "lab": ("argkit", {
            "mode": "sorites",
            "treatment": "degrees",
            "preset": "heap",
            "presets": [
                {"id": "heap", "label": "ten thousand grains down to none",
                 "start": 10000, "end": 0, "cutoff": 5000, "range": [50, 200],
                 "predicate": "is a heap", "expect": {"soSteps": "10000", "soCond": "each 9999/10000", "soConc": "0"}},
                {"id": "heap-cutoff", "label": "the same chain, cutoff at 1000",
                 "start": 10000, "end": 0, "cutoff": 1000, "range": [50, 200],
                 "predicate": "is a heap", "expect": {"soSteps": "10000", "soCond": "each 9999/10000", "soConc": "0"}},
                {"id": "heap-range", "label": "a thousand grains, borderline from 50 to 200",
                 "start": 1000, "end": 0, "cutoff": 100, "range": [50, 200],
                 "predicate": "is a heap", "expect": {"soSteps": "1000", "soCond": "each 999/1000", "soConc": "0"}},
            ],
            "panel_title": "The same chain, four treatments",
            "panel_intro": (
                "The lab opens on degrees of truth. Read the conditionals and the "
                "conclusion, then use the treatment menu to move to each of the "
                "other three and read them again. The cutoff field matters only "
                "for the cutoff treatment, and the range field only for the range "
                "treatment; the second and third presets set those fields. Then "
                "shorten the chain and watch the degrees treatment's conclusion "
                "change."
            ),
        }),
        "steps_title": "Running the heap under each treatment",
        "steps_intro": "Five steps. The last is the one that is not computed.",
        "steps": [
            ("Write the chain",
             "State the clear case, `F(10000)`, the end, `F(0)`, and the "
             "tolerance conditional between neighbours. The lab prints the "
             "number of steps."),
            ("Run it classically",
             "Every conditional is True and the end is True. This is the "
             "paradox as it stands."),
            ("Choose a place to cut the chain",
             "A cutoff falsifies one conditional. A range makes a block of them "
             "indeterminate. Degrees make every one slightly less than true."),
            ("Read the conclusion",
             "False for the cutoff, super-false for the range, 0 for degrees. "
             "Each denies something, so write down what."),
            ("Ask where the line is",
             "Ask of the cutoff, the edges of the range and the degrees how "
             "anyone could have placed them. That is higher-order vagueness, "
             "and it is not a number the lab can print."),
        ],
        "worked": {
            "title": "Ten thousand almost-true conditionals",
            "intro": [
                "The chain from 10000 grains to none, under degrees of truth.",
            ],
            "lines": [
                "steps = 10000 − 0 = 10000",
                "v(F(k)) = k / 10000",
                "v(F(k) → F(k − 1)) = 1 − 1/10000 = 9999/10000",
                "each modus ponens may lose 1/10000",
                "after 10000 steps the guaranteed value of F(0):",
                "   1 − 10000 · (1/10000) = 0",
            ],
            "after": [
                "Every premise is almost wholly true and the conclusion is wholly "
                "false. That is the Łukasiewicz answer to the heap: the "
                "argument is valid and not dangerous at each step, and the "
                "steps add up.",
            ],
        },
        "quiz_title": "What each treatment gives up",
        "quiz": [
            {"q": "Under the classical treatment, what does the lab print for the "
                  "conclusion that no grains are a heap?",
             "a": ["False, because the conditionals fail",
                   "True, because every conditional and the start are True",
                   "Super-false",
                   "0"],
             "c": 1,
             "why": "Classically all the conditionals are True and so is the start, "
                    "and modus ponens carries truth along the chain, so the "
                    "absurd end is True. False belongs to the cutoff treatment, "
                    "super-false to the range, and 0 to degrees."},
            {"q": "Under degrees, the heap chain of 10000 steps has conditionals "
                  "of value 9999/10000. Why is the conclusion's value 0 and not "
                  "close to 1?",
             "a": ["Because modus ponens can lose 1/10000 at each of the ten thousand steps",
                   "Because 9999/10000 counts as false",
                   "Because the first premise is false",
                   "Because the lab takes the average of the premises"],
             "c": 0,
             "why": "The guaranteed value falls by 1/10000 per step, and 10000 steps "
                    "take it from 1 to 0. A value of 9999/10000 is almost true, "
                    "not false, so the second is wrong; `F(10000)` has value 1 so "
                    "the third is wrong; and the lab does not average, it chains "
                    "the loss."},
            {"q": "The cutoff treatment says some conditional is False. What is "
                  "its main cost?",
             "a": ["It keeps classical logic, which is a cost",
                   "It makes the tolerance claim true",
                   "It says there is a sharp boundary that no one can locate",
                   "It gives every conditional the value 0"],
             "c": 2,
             "why": "The sharp boundary no one can find is the price. Keeping "
                    "classical logic is its benefit. It makes one tolerance "
                    "conditional False, so the tolerance claim is not kept, and "
                    "only one conditional is False, not every one."},
            {"q": "Why is higher-order vagueness a problem for the range "
                  "treatment?",
             "a": ["The range makes every conditional True",
                   "The edges of the borderline region are sharp lines, "
                   "and the edges themselves look vague",
                   "The range is too wide for the lab",
                   "Because ranges cannot be written as numbers"],
             "c": 1,
             "why": "The treatment replaces one sharp line with two, and a "
                    "predicate that has no sharp line between heap and non-heap "
                    "seems to have none between borderline and not. The range "
                    "makes the conditionals inside it indeterminate, not True. The "
                    "lab accepts any range, and a range is written as two numbers "
                    "in the field."},
        ],
        "mistakes": [
            ("Taking vagueness to be ignorance of a sharp boundary",
             "That is one of the four treatments, the cutoff, and it is "
             "defensible: the lab marks a False conditional at the count you "
             "type, keeps classical logic, and gives the same verdict whichever "
             "count that is. What it cannot do is say which count is right, and "
             "a reader who takes the boundary to be the obvious default has "
             "not yet paid the cost. The other treatments are answers to the "
             "thought that no count is the boundary."),
            ("Concluding that vagueness is a defect that precision removes",
             "Replacing “heap” with “at least 1000 grains” settles the cases, "
             "and also changes the word. The sorites is about the word as used, "
             "and a stipulated cutoff is a decision about what to call a heap, "
             "not a discovery about heaps."),
            ("Thinking degrees make the paradox disappear",
             "Under degrees each premise is almost true and the conclusion is "
             "wholly false, from a valid argument. The paradox moves from a "
             "false premise to a loss at each step. And the exact number "
             "9999/10000 is itself a sharp choice."),
        ],
        "standard": (
            "Finish when you can run the chain four ways and state each price.",
            "Given the heap argument, you should be able to read the lab's "
            "verdict under each treatment, say what each denies, and state "
            "why the cutoff and the range both face the question where "
            "their lines fall."
        ),
        "note": (
            "Vagueness has more treatments than four, and the supervaluation "
            "and epistemic views have large literatures that this lesson does "
            "not enter. The aim is to see what each treatment does to the "
            "chain, and what it asks of you."
        ),
    },
]
