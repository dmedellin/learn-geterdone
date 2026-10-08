"""Course 1, lessons 07-12 -- consistency, categorical logic, quantifiers, fallacies."""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "consistency-and-belief-sets",
        "title": "Consistency and Belief Sets",
        "module": "Propositional logic",
        "one_line": "Decide whether a set of beliefs can all be true, and find the smallest part that cannot.",
        "summary": (
            "A set of sentences is consistent when some row makes every one of them "
            "true. When no row does, the set is inconsistent, and the smallest "
            "subset that already fails is the place to look. That subset says "
            "that something must go. It does not say what."
        ),
        "key": [
            "consistent: some row makes all of them true",
            "a model is a row where every sentence holds",
            "inconsistent: no such row exists",
            "the smallest subset that cannot all be true",
            "it says one must go, never which one",
        ],
        "key_label": "Beliefs that cannot all be true",
        "concepts_intro": (
            "An argument has a conclusion to test. A set of beliefs has none, and "
            "the question changes from whether something follows to whether the "
            "sentences can live together."
        ),
        "concepts": [
            ("A model is a row where everything holds",
             "Take the table over the simple sentences in the set. A row that makes "
             "every member true is a model. A set with at least one model is "
             "consistent; a set with none is inconsistent. Counting the models says "
             "how much the set leaves open."),
            ("An inconsistent set is a valid argument in disguise",
             "Put a conclusion's denial beside the premises. If the result has no "
             "model, no row makes the premises true and the conclusion false, which "
             "is validity. Testing an argument and testing a belief set are the "
             "same table read two ways."),
            ("The smallest failing subset is the diagnosis",
             "Remove sentences until the rest can all be true. A subset that cannot "
             "all be true, and becomes possible when any member is removed, is "
             "a minimal inconsistent subset. It marks where the trouble is, and "
             "nothing in it marks which member is the false one."),
        ],
        "read_title": "Can they all be true together?",
        "read_intro": (
            "The test is the table of “Validity by Truth Table”, run on a set "
            "instead of an argument."
        ),
        "body": [
            ("def", ("Consistency",
                     "A set of sentences is <strong>consistent</strong> when at least "
                     "one row of its table makes every member true. Such a row is a "
                     "<strong>model</strong> of the set. A set with no model is "
                     "<strong>inconsistent</strong>.")),
            ("p", "Start with the smallest interesting case. The set contains "
                  "`p → q`, `p` and `¬q`. Read the three together: if the first two "
                  "hold, `q` must hold, and the third denies it. This is modus "
                  "ponens with its conclusion turned into a premise, and the table "
                  "shows that no row survives."),
            ("math", [
                "p   q  |  p → q   p   ¬q",
                "---------------------------",
                "T   T  |    T     T    F",
                "T   F  |    F     T    T",
                "F   T  |    T     F    F",
                "F   F  |    T     F    T",
            ]),
            ("p", "Every row has a false cell, so there is no model and the set is "
                  "inconsistent. The lab reports this as zero rows of four. Note what "
                  "kind of fact this is. No pair of these sentences contradicts "
                  "another: `p → q` with `p` is fine, `p` with `¬q` is fine, and "
                  "`p → q` with `¬q` is fine. The trouble appears only when all three "
                  "are held at once."),
            ("def", ("Minimal inconsistent subset",
                     "A subset that cannot all be true, and that becomes possible "
                     "when any one member is removed, is a <strong>minimal "
                     "inconsistent subset</strong>. A set may have several. The lab "
                     "reports the smallest, and among those of equal size the one "
                     "that comes first by sentence number.")),
            ("p", "Sentences outside the minimal subset are innocent of this "
                  "particular failure. Add `q → r` to the set above and the smallest "
                  "failing subset is still the first three. Added sentences cannot "
                  "repair an inconsistency, because every row that fails already "
                  "fails."),
            ("p", "Now the part that matters for philosophy. An inconsistent set tells "
                  "you that at least one member is false. It does not tell you which. "
                  "In the four-sentence set `p → q`, `q → r`, `p`, `¬r` the lab lets "
                  "you give up each sentence in turn, and each time exactly one model "
                  "appears:"),
            ("math", [
                "give up         model that appears",
                "-----------------------------------",
                "1  p → q        p=T q=F r=F",
                "2  q → r        p=T q=T r=F",
                "3  p            p=F q=F r=F",
                "4  ¬r           p=T q=T r=T",
            ]),
            ("p", "All four repairs work, and they describe four different worlds. "
                  "Which to choose is a question about the sentences themselves: how "
                  "much you trust each, what each costs to lose, what else depends on "
                  "it. The table is neutral. That neutrality is why a skeptic's valid "
                  "argument forces a choice and cannot make it."),
            ("p", "Consistency is also weaker than truth. The set `p ∨ q`, `¬p`, "
                  "`q → r` is consistent, with one model, `p` false and `q` and `r` "
                  "true. That means the three sentences could all be true. Whether "
                  "they are is again a question about the world, which no lab here "
                  "answers."),
        ],
        "lab": ("argkit", {
            "mode": "consistency",
            "preset": "triad",
            "presets": [
                {"id": "triad", "label": "p → q, p, ¬q",
                 "sentences": ["p -> q", "p", "~q"], "expect": {"coVerdict": "Inconsistent", "coMis": "{1, 2, 3}", "coModels": "0 of 4"}},
                {"id": "four", "label": "p → q, q → r, p, ¬r",
                 "sentences": ["p -> q", "q -> r", "p", "~r"], "expect": {"coVerdict": "Inconsistent", "coMis": "{1, 2, 3, 4}", "coModels": "0 of 8"}},
                {"id": "fine", "label": "p ∨ q, ¬p, q → r",
                 "sentences": ["p | q", "~p", "q -> r"], "expect": {"coVerdict": "Consistent", "coMis": "none", "coModels": "1 of 8"}},
            ],
            "panel_title": "Which sentences cannot live together",
            "panel_intro": (
                "The lab counts the rows that make every kept sentence true and, "
                "when there are none, lists the smallest subset that fails. Start "
                "with the four-sentence set and use the give-up menu on each "
                "sentence in turn. Then choose the third set, which is consistent, "
                "and read its single model."
            ),
        }),
        "steps_title": "Testing a set of beliefs",
        "steps_intro": "Four steps. The last is a judgement, and the lab stops before it.",
        "steps": [
            ("Write each belief as a sentence over simple letters",
             "Use one letter per simple claim and the same letter every time the "
             "claim recurs. A letter used for two different claims manufactures an "
             "inconsistency that was never there."),
            ("Look for a model",
             "Find a row that makes every sentence true. If you find one, the set is "
             "consistent and you can stop: that one row is the whole proof."),
            ("If none exists, find the smallest failing subset",
             "Give up each sentence in turn, or try subsets by size. The smallest "
             "subset that fails is where the incompatibility lives."),
            ("Choose what to give up on other grounds",
             "Any member of a minimal subset can be dropped to restore consistency. "
             "Pick by which you have most reason to doubt, and say what the choice "
             "costs."),
        ],
        "worked": {
            "title": "The alarm that did not wake her",
            "intro": [
                "Let `p` be &ldquo;the alarm was set&rdquo;, `q` &ldquo;the alarm "
                "rang&rdquo; and `r` &ldquo;she woke&rdquo;. Four beliefs: if it was "
                "set it rang; if it rang she woke; it was set; she did not wake.",
            ],
            "lines": [
                "1.  p → q     if it was set, it rang",
                "2.  q → r     if it rang, she woke",
                "3.  p         it was set",
                "4.  ¬r        she did not wake",
                "models: 0 of 8        smallest subset: {1, 2, 3, 4}",
            ],
            "after": [
                "Chain the first three: set, so rang, so woke. The fourth denies "
                "the last link. No smaller subset fails, because giving up any one "
                "of the four leaves a possible world, and the table above lists "
                "all four. If the alarm was not set the story is one thing; if it "
                "rang without waking her, another; if she did wake, a third. The "
                "lab has shown that the beliefs cannot stand together and has not "
                "said which is false.",
            ],
        },
        "quiz_title": "Models and minimal subsets",
        "quiz": [
            {"q": "The set `p → q`, `p`, `¬q` is inconsistent. Which sentence is the "
                  "false one?",
             "a": ["`p → q`, because conditionals are the weakest claims",
                   "`p`, because it is the premise with no support",
                   "`¬q`, because it is the one that contradicts the conclusion",
                   "The table does not say; at least one is false, and removing "
                   "any one leaves a set with a model"],
             "c": 3,
             "why": "The three are symmetric in the table. Dropping the first leaves "
                    "`p` true and `q` false; dropping the second leaves `q` false; "
                    "dropping the third leaves `q` true. Each repair works, so "
                    "nothing in the logic singles one out."},
            {"q": "In the third preset, `p ∨ q`, `¬p`, `q → r`, what does the lab "
                  "report?",
             "a": ["Inconsistent, with the smallest subset `{1, 2}`",
                   "Consistent, with one model of eight, `p` false and `q` and "
                   "`r` true",
                   "Consistent, with four models of eight",
                   "Inconsistent, with no model in eight"],
             "c": 1,
             "why": "`¬p` forces `p` false, then `p ∨ q` forces `q` true, then "
                    "`q → r` forces `r` true. Exactly one of the eight rows survives, "
                    "so the set is consistent with a single model."},
            {"q": "The argument `p → q`, `q → r`, `p` ∴ `r` is valid. Which set of "
                  "sentences is therefore inconsistent?",
             "a": ["`p → q`, `q → r`, `p`, `¬r`",
                   "`p → q`, `q → r`, `p`, `r`",
                   "`p → q`, `q → r`, `¬p`, `r`",
                   "`p → q`, `q → r`, `¬p`, `¬r`"],
             "c": 0,
             "why": "A valid argument has no row with true premises and a false "
                    "conclusion, which is to say that the premises with the "
                    "conclusion denied have no model. The other three sets each "
                    "have a model: all true with `r` true, `p` false and `r` true, "
                    "and every letter false."},
            {"q": "A set of beliefs is consistent. What follows?",
             "a": ["Every member is true",
                   "None of its members is false",
                   "Some row makes all of them true, so they could be true "
                   "together, though they may all be false",
                   "Every subset is a minimal inconsistent subset"],
             "c": 2,
             "why": "Consistency says a model exists. Whether the world is that row "
                    "is a separate matter, and a consistent set can be false "
                    "throughout. A consistent set has no inconsistent subset at all, "
                    "so the last choice is the reverse of the truth."},
        ],
        "mistakes": [
            ("Looking for the false sentence in an inconsistent set",
             "The set `p → q`, `p`, `¬q` has no model, but its table shows no sentence "
             "marked as the culprit: giving up any one of the three leaves a model. "
             "&ldquo;At least one is false&rdquo; is all the inconsistency proves. "
             "Which to give up is decided by the weight of the reasons for each, and "
             "that is the work philosophy does."),
            ("Expecting an inconsistent set to contain a pair that contradict",
             "Every pair drawn from `p → q`, `p`, `¬q` is consistent. The conflict "
             "needs all three, and a larger set can need more. This is why a belief "
             "system can be inconsistent while every belief in it looks fine beside "
             "its neighbours."),
            ("Reading &ldquo;consistent&rdquo; as &ldquo;true&rdquo;",
             "A consistent set has a model, a row, and a row is a description of a "
             "possible case. The set may be false of the actual world in every "
             "member. The lab checks that the beliefs could all be true; it cannot "
             "check that they are."),
        ],
        "standard": (
            "Finish when you can produce the model, or the failing subset.",
            "Given a set of up to four sentences over three letters, either write a "
            "row that makes all of them true or name the smallest subset that cannot "
            "all be true, and say what that subset does and does not tell you about "
            "which belief to give up."
        ),
        "note": (
            "The lab lists every model and every minimal subset by trying them all, "
            "so it takes at most eight sentences over six letters. The same test "
            "returns in Knowledge and Evidence, where the regress of justification "
            "is set out as an inconsistent set with four ways out."
        ),
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "categorical-statements-and-immediate-inference",
        "title": "Categorical Statements and Immediate Inference",
        "module": "Categorical logic",
        "one_line": "Read All, No and Some as claims about regions, and test one-step inferences on them.",
        "summary": (
            "All, No, Some and Some-not are claims about which regions of a two-circle "
            "diagram are empty and which are occupied. Reading them that way turns "
            "conversion, obversion and contraposition into checks: a conclusion "
            "follows when the premise forces its regions."
        ),
        "key": [
            "All S are P:   S outside P is empty",
            "No S are P:    S inside P is empty",
            "Some S are P:  S inside P is occupied",
            "Some S are not P: S outside P occupied",
            "valid when the premise forces the regions",
        ],
        "key_label": "Four statements, four region claims",
        "concepts_intro": (
            "The propositional connectives cannot see inside a sentence. Categorical "
            "statements are about the things a sentence is about, and regions are "
            "the cases."
        ),
        "concepts": [
            ("A statement is about two circles",
             "Draw one circle for the S things and one for the P things. They make "
             "four regions: S only, both, P only, neither. Every categorical "
             "statement says something about whether a region is empty or occupied."),
            ("Universal statements remove, particular ones require",
             "All and No say that a region is empty. Some and Some-not say that a "
             "region is occupied. An unmarked region is left open, which is not the "
             "same as occupied."),
            ("A one-step inference is a test of forcing",
             "Conversion, obversion and contraposition each take one statement and "
             "write another. The new statement follows when every pattern of empty "
             "and occupied regions that the first allows also makes the second true."),
        ],
        "read_title": "Statements as regions",
        "read_intro": (
            "Four forms, each a claim about one region, and then the three "
            "rewritings that logicians have always tried on them."
        ),
        "body": [
            ("def", ("Categorical statement",
                     "A <strong>categorical statement</strong> relates two terms, a "
                     "subject `S` and a predicate `P`, in one of four forms: "
                     "<strong>A</strong>, All `S` are `P`; <strong>E</strong>, No `S` "
                     "are `P`; <strong>I</strong>, Some `S` are `P`; and "
                     "<strong>O</strong>, Some `S` are not `P`.")),
            ("math", [
                "form   statement           what it claims about regions",
                "---------------------------------------------------------",
                "A      All S are P         S outside P is empty",
                "E      No S are P          S inside P is empty",
                "I      Some S are P        S inside P is occupied",
                "O      Some S are not P    S outside P is occupied",
            ]),
            ("p", "This reading is the Boolean one: a universal statement says that a "
                  "region has nothing in it, and does not say that any other region "
                  "has anything in it. “All S are P” is true if there are no S at all. "
                  "The next lesson sets this beside the older reading and says what "
                  "each costs; for now the lab shows the Boolean one."),
            ("example", ("All squares are rectangles",
                         "Let `S` be the squares and `P` the rectangles. The claim "
                         "empties one region only: the squares that are not "
                         "rectangles. It says nothing about the region of rectangles "
                         "that are not squares, which is where the two-by-one "
                         "rectangle lives, and it says nothing about whether "
                         "the region of squares that are rectangles has anything in "
                         "it.")),
            ("p", "An <strong>immediate inference</strong> has one premise. The test "
                  "is the same as for a larger argument: list the patterns of empty "
                  "and occupied regions the premise allows, and check the conclusion "
                  "in each. With two terms there are four regions and sixteen "
                  "patterns; a premise that fixes one region, empty or occupied, "
                  "leaves the other three open, so eight patterns survive it, and "
                  "that is the count the lab reports. If the conclusion fails in some "
                  "allowed pattern, that pattern is the counterexample; if it fails "
                  "in none, the inference is valid."),
            ("p", "<strong>Conversion</strong> swaps subject and predicate. No `S` are "
                  "`P` converts to No `P` are `S`, because both empty the single "
                  "region where the circles overlap. The same holds for Some, which "
                  "occupies that region. But All `S` are `P` empties `S` outside `P`, "
                  "and All `P` are `S` empties `P` outside `S`, a different region. "
                  "Some `S` are not `P` occupies `S` outside `P`, and its converse "
                  "needs `P` outside `S`: the same failure, with occupied in place of "
                  "empty."),
            ("p", "<strong>Contraposition</strong> swaps the terms and takes the "
                  "complement of each, written `non-P`. All `S` are `P` becomes All "
                  "non-`P` are non-`S`, and both empty the same region, `S` outside "
                  "`P`. <strong>Obversion</strong> changes the quality and takes the "
                  "complement of the predicate: All `S` are `P` becomes No `S` are "
                  "non-`P`. Again one region is emptied."),
            ("thm", ("Which one-step inferences are valid",
                     "Conversion is valid for E and I, invalid for A and O. "
                     "Contraposition is valid for A and O, invalid for E and I. "
                     "Obversion is valid for all four. Each verdict is read off "
                     "which region the premise and conclusion constrain, and "
                     "nothing is memorised.")),
            ("p", "The lab draws two circles, shades what the premise forces empty, "
                  "and puts a cross in any region it forces occupied. When the "
                  "inference is invalid it draws the counterexample, the smallest "
                  "pattern that satisfies the premise and fails the conclusion."),
        ],
        "lab": ("argkit", {
            "mode": "syllogism",
            "preset": "convert-e",
            "import": "boolean",
            "presets": [
                {"id": "convert-e", "label": "No S are P, so No P are S",
                 "premises": ["No S are P"], "conclusion": "No P are S", "expect": {"syVerdict": "Valid", "syCounter": "none", "syModels": "8"}},
                {"id": "convert-a", "label": "All S are P, so All P are S",
                 "premises": ["All S are P"], "conclusion": "All P are S", "expect": {"syVerdict": "Invalid", "syCounter": "P", "syModels": "8"}},
                {"id": "contrapose-a", "label": "All S are P, so All non-P are non-S",
                 "premises": ["All S are P"], "conclusion": "All non-P are non-S", "expect": {"syVerdict": "Valid", "syCounter": "none", "syModels": "8"}},
                {"id": "convert-o", "label": "Some S are not P, so Some P are not S",
                 "premises": ["Some S are not P"], "conclusion": "Some P are not S", "expect": {"syVerdict": "Invalid", "syCounter": "S", "syModels": "8"}},
                {"id": "obvert-a", "label": "All S are P, so No S are non-P",
                 "premises": ["All S are P"], "conclusion": "No S are non-P", "expect": {"syVerdict": "Valid", "syCounter": "none", "syModels": "8"}},
            ],
            "panel_title": "Which regions does the premise force?",
            "panel_intro": (
                "Shaded regions are empty and crosses are occupied. Run the five "
                "inferences in turn. For each invalid one, read the counterexample "
                "and say in a sentence which things it describes."
            ),
        }),
        "steps_title": "Testing a one-premise inference",
        "steps_intro": "Five steps; the second is where most errors enter.",
        "steps": [
            ("Name the terms, and their complements",
             "Pick the two terms and write `non-S` and `non-P` where they occur. A "
             "complement is a term in its own right: it is everything outside the "
             "circle."),
            ("Turn each statement into a region claim",
             "A and E empty a region. I and O occupy one. Write which region, "
             "using the four names S only, both, P only and neither."),
            ("List what the premise forces",
             "Mark the regions the premise empties or occupies. Leave every other "
             "region open, because an unmarked region may be empty or occupied."),
            ("Ask whether the conclusion's region is forced",
             "If the conclusion empties a region, the premise must empty it. If it "
             "occupies one, the premise must occupy it."),
            ("If it is not forced, describe the counterexample",
             "Say which region the premise leaves open that the conclusion needs. "
             "That region, emptied or occupied the wrong way, is the case the "
             "conclusion does not survive."),
        ],
        "worked": {
            "title": "Squares and rectangles, converted",
            "intro": [
                "Let `S` be the squares and `P` the rectangles. The premise is All "
                "squares are rectangles, and the conversion offered is All "
                "rectangles are squares.",
            ],
            "lines": [
                "premise      squares outside rectangles: empty",
                "conclusion   rectangles outside squares: must be empty",
                "premise leaves that region open",
                "counterexample: only rectangles outside squares",
            ],
            "after": [
                "The conclusion needs a region the premise never mentions. The "
                "pattern with only that region occupied satisfies the premise "
                "(no square is missing from the rectangles) and fails the "
                "conclusion (there is a rectangle that is not a square). In the "
                "lab this is the convert-a preset, and the counterexample it draws "
                "is the same pattern. A premise can force one region without "
                "forcing its mirror image.",
            ],
        },
        "quiz_title": "Regions and rewritings",
        "quiz": [
            {"q": "Which immediate inference is valid?",
             "a": ["All `S` are `P`, so all `P` are `S`",
                   "Some `S` are not `P`, so some `P` are not `S`",
                   "No `S` are `P`, so no `P` are `S`",
                   "All `S` are `P`, so all non-`S` are non-`P`"],
             "c": 2,
             "why": "No `S` are `P` empties the region where the circles overlap, "
                    "and so does no `P` are `S`. The first and second are "
                    "conversions of A and O, which fail. The last is the inverse of "
                    "an A statement, which empties a different region."},
            {"q": "Which of the following is the contrapositive of &ldquo;All "
                  "squares are rectangles&rdquo;?",
             "a": ["All non-rectangles are non-squares",
                   "All rectangles are squares",
                   "All non-squares are non-rectangles",
                   "No squares are non-rectangles"],
             "c": 0,
             "why": "Contraposition swaps the terms and complements each. The second "
                    "is the converse and the third the inverse, and both fail. The "
                    "last is the obverse, which is valid but is a different "
                    "rewriting."},
            {"q": "The only occupied region is P outside S. Which statement is true "
                  "in that case?",
             "a": ["All `P` are `S`", "Some `S` are `P`",
                   "Some `S` are not `P`", "All `S` are `P`"],
             "c": 3,
             "why": "All `S` are `P` needs only that `S` outside `P` is empty, and "
                    "it is, because nothing is in `S` at all. The other choices each "
                    "need a region occupied or empty that the case denies."},
            {"q": "Why is &ldquo;Some `S` are not `P`, so some `P` are not `S`&rdquo; "
                  "invalid?",
             "a": ["Some is too weak a word to support a conversion",
                   "Some `S` are not `P` can hold while every `P` is an `S`",
                   "Particular statements never support any inference",
                   "Conversion fails only for universal statements"],
             "c": 1,
             "why": "Occupying `S` outside `P` leaves `P` outside `S` open, and it can "
                    "be empty, which makes the conclusion false. Conversion is valid "
                    "for E and I, so the last choice is wrong in both directions."},
        ],
        "mistakes": [
            ("Converting &ldquo;All `S` are `P`&rdquo; to &ldquo;All `P` are `S`&rdquo;",
             "The first empties `S` outside `P`; the second empties `P` outside "
             "`S`. All squares are rectangles is true, and all rectangles are squares "
             "is false of the two-by-one rectangle. The lab draws exactly that "
             "pattern as the counterexample, a region occupied that the premise "
             "never touches."),
            ("Reading &ldquo;Some&rdquo; as &ldquo;some but not all&rdquo;",
             "Some `S` are `P` requires one occupied region and is silent about the "
             "rest. It is compatible with every `S` being a `P`, and Some `S` are "
             "`P` and Some `S` are not `P` can both be true at once. &ldquo;Some&rdquo; "
             "here means at least one."),
            ("Taking an unshaded region to be occupied",
             "A shaded region is empty, and a cross is occupied; a blank region is "
             "open. A premise that says nothing about a region allows it to be "
             "either, which is what the counterexample uses. Blank is permission, "
             "and the lab tests every way of using it."),
        ],
        "standard": (
            "Finish when you can name the region that decides each inference.",
            "Given one categorical premise and a conclusion, write each as a claim "
            "about empty or occupied regions, say whether the premise forces the "
            "conclusion's region, and describe the counterexample pattern when it "
            "does not."
        ),
        "note": (
            "Every statement here is read the Boolean way, with no assumption that "
            "a term has members. The next lesson makes that assumption a switch and "
            "shows which inferences depend on it."
        ),
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "the-square-of-opposition-and-existential-import",
        "title": "The Square of Opposition and Existential Import",
        "module": "Categorical logic",
        "one_line": "Find out which of the traditional inferences need the assumption that a term has members.",
        "summary": (
            "The square of opposition links the four categorical forms by contradiction, "
            "contrariety, subcontrariety and subalternation. On the Boolean reading "
            "only the contradictions survive. The rest return when every term is "
            "assumed to be non-empty, which is the existential import the old "
            "square relied on."
        ),
        "key": [
            "A and O, E and I: contradictories",
            "A to I, E to O: subalternation",
            "Boolean reading: terms may be empty",
            "import: every term has members",
            "only contradictories survive without import",
        ],
        "key_label": "The square, with and without import",
        "concepts_intro": (
            "The traditional square arranges the four forms so that each relation "
            "is a claim about truth values. Whether the claims hold depends on a "
            "background assumption that is easy to miss."
        ),
        "concepts": [
            ("Four relations among four forms",
             "A and O, and E and I, are contradictories: exactly one of each pair "
             "is true. A and E are contraries: not both true. I and O are "
             "subcontraries: not both false. A implies I and E implies O, which is "
             "subalternation."),
            ("One inference carries the rest",
             "A is true only if E is false, and E is false exactly when I is true. "
             "So the contrariety of A and E is the same claim as A implies I. In the "
             "same way the subcontrariety of I and O is E implies O. Only "
             "subalternation and the contradictions need testing."),
            ("Import is a switch",
             "Existential import is the assumption that every term has at least one "
             "member. Without it, All unicorns are white is true and Some unicorns "
             "are white is not, and the square loses its sides. With it, the "
             "square returns. The lab makes the assumption a menu."),
        ],
        "read_title": "What the square needs",
        "read_intro": (
            "The same four forms of the last lesson, now compared in pairs, and "
            "the one assumption that decides which comparisons hold."
        ),
        "body": [
            ("p", "The square arranges the four forms in a box. A at the top left, E "
                  "at the top right, I at the bottom left and O at the bottom right. "
                  "The relations are claims about what can be true or false together, "
                  "and each can be checked as an inference."),
            ("math", [
                "pair       relation          claim",
                "------------------------------------------------",
                "A and O    contradictories   exactly one is true",
                "E and I    contradictories   exactly one is true",
                "A and E    contraries        not both true",
                "I and O    subcontraries     not both false",
                "A to I     subalternation    A true, so I true",
                "E to O     subalternation    E true, so O true",
            ]),
            ("p", "On the Boolean reading of the last lesson the contradictions hold "
                  "in every case, because A empties the region that O occupies and E "
                  "empties the region that I occupies. The rest fail on one pattern. "
                  "Let nothing be an `S`. Then All `S` are `P` is true, and so is No "
                  "`S` are `P`: the contraries are both true. Some `S` are `P` and "
                  "Some `S` are not `P` are both false: the subcontraries are both "
                  "false. And A is true while I is false, so subalternation fails."),
            ("example", ("All unicorns are white",
                         "Read as a region claim, it empties the unicorns that are not "
                         "white, and that region is empty because no unicorn is "
                         "anywhere. So the statement is true. Some unicorns are "
                         "white needs a white unicorn, and there is none. The lab's "
                         "unicorns preset draws the pattern with every region "
                         "empty as the counterexample to the step from All to Some.")),
            ("p", "Existential import is the repair. The <strong>Aristotelian</strong> "
                  "reading assumes every term names something: each circle has at "
                  "least one occupied region. Under that assumption an A statement, "
                  "which empties the outside of `P`, leaves only the overlap to "
                  "hold the `S`, so the overlap is occupied and Some `S` are `P` "
                  "follows. Every relation on the square returns with it."),
            ("p", "So the reading is a choice with a price on each side. The Boolean "
                  "reading lets “All trespassers will be prosecuted” be true when "
                  "there are no trespassers, and a law is not shown false by a quiet "
                  "year; the price is that the old square collapses to its two "
                  "diagonals. The Aristotelian reading keeps the whole square; the "
                  "price is that it cannot say anything universal about what may not "
                  "exist without also saying that it does."),
            ("p", "The lab shows the reading as a switch, with the Boolean one "
                  "shipped. Its status line always reports the other verdict as "
                  "well. Take the step from All `S` are `P` to Some `P` are `S`, "
                  "traditionally called conversion per accidens. On the Boolean "
                  "reading it has a counterexample; on the Aristotelian reading it "
                  "has none, because `S` is non-empty and every `S` is a `P`."),
            ("thm", ("What the switch does not change",
                     "Contradictories hold on both readings: A with O, and E with I, "
                     "never agree. An inference that never needed a term to have "
                     "members, such as converting No `S` are `P`, keeps its verdict "
                     "when the reading changes. Only inferences that move from a "
                     "universal to a particular claim are affected.")),
            ("p", "The contradictory preset has All `S` are `P` as its premise and Some "
                  "`S` are not `P` as its conclusion. The inference is invalid on both "
                  "readings. That is what contradiction says: when A is true, O is "
                  "false, so the counterexample is exactly a case where A holds and "
                  "O fails. Switch the reading and only the counterexample moves."),
        ],
        "lab": ("argkit", {
            "mode": "syllogism",
            "preset": "subalt",
            "import": "boolean",
            "presets": [
                {"id": "subalt", "label": "All S are P, so Some S are P",
                 "premises": ["All S are P"], "conclusion": "Some S are P", "expect": {"syVerdict": "Invalid", "syCounter": "every region empty"}},
                {"id": "contradictory", "label": "All S are P, so Some S are not P",
                 "premises": ["All S are P"], "conclusion": "Some S are not P", "expect": {"syVerdict": "Invalid", "syCounter": "every region empty"}},
                {"id": "converse-accidens", "label": "All S are P, so Some P are S",
                 "premises": ["All S are P"], "conclusion": "Some P are S", "expect": {"syVerdict": "Invalid", "syCounter": "every region empty"}},
                {"id": "unicorns", "label": "All unicorns are white, so Some unicorns are white",
                 "premises": ["All unicorns are white"], "conclusion": "Some unicorns are white", "expect": {"syVerdict": "Invalid", "syCounter": "every region empty"}},
            ],
            "panel_title": "The same premise under two readings",
            "panel_intro": (
                "Each preset is shown on the Boolean reading. Change the reading "
                "menu to Aristotelian and watch which verdicts flip, and which "
                "do not. The status line names the verdict on the other reading "
                "before you change it."
            ),
        }),
        "steps_title": "Deciding whether an inference needs import",
        "steps_intro": "Four steps, one of them a comparison.",
        "steps": [
            ("Run it on the Boolean reading",
             "Find whether any pattern satisfies the premise and fails the "
             "conclusion, with no assumption that a term has members."),
            ("Run it with every term non-empty",
             "Require each circle to hold a cross somewhere, and test again. This is "
             "the only change the switch makes."),
            ("Compare the two verdicts",
             "If they agree, the inference does not depend on import. If it is "
             "invalid on the first and valid on the second, import is the extra "
             "premise doing the work."),
            ("State the assumption in the conclusion",
             "Say, “assuming there are `S`”, and mean it. An inference that needs "
             "import is sound only for terms that name something."),
        ],
        "worked": {
            "title": "Trespassers and unicorns",
            "intro": [
                "&ldquo;All unicorns are white. So some unicorns are white.&rdquo; "
                "Take the premise as a region claim and run the step on both "
                "readings.",
            ],
            "lines": [
                "premise       unicorns outside white: empty",
                "Boolean       every region empty satisfies it",
                "conclusion    unicorns inside white: occupied",
                "Boolean       fails there: invalid",
                "Aristotelian  unicorns exist: the overlap is occupied",
            ],
            "after": [
                "On the Boolean reading the pattern with nothing anywhere is allowed "
                "by the premise and fails the conclusion. Require the unicorns "
                "to exist and that pattern is gone: the only place left for them is "
                "inside the white region. The step from All to Some is a good "
                "inference about trespassers and a bad one about unicorns, and the "
                "logic cannot tell which a term is. That is the cost of having a "
                "switch, and the lab's status line shows it.",
            ],
        },
        "quiz_title": "Reading the square",
        "quiz": [
            {"q": "On the Boolean reading, which relation on the square still holds?",
             "a": ["A and O are contradictories",
                   "A implies I",
                   "A and E cannot both be true",
                   "I and O cannot both be false"],
             "c": 0,
             "why": "A empties the region that O needs occupied, so exactly one of "
                    "them is true in every pattern. The other three each fail on the "
                    "pattern with every region empty: A and E both true, I and O both "
                    "false, A true with I false."},
            {"q": "&ldquo;All trespassers will be prosecuted, so some trespasser "
                  "will be prosecuted.&rdquo; On which reading is this valid?",
             "a": ["Both readings", "Neither reading",
                   "The Aristotelian reading only", "The Boolean reading only"],
             "c": 2,
             "why": "On the Boolean reading there might be no trespassers, and the "
                    "premise is then true while the conclusion is false. Assume "
                    "there are trespassers and the step goes through. It cannot be "
                    "valid on the Boolean reading and not on the other."},
            {"q": "When can All `S` are `P` and No `S` are `P` both be true?",
             "a": ["Never, on either reading",
                   "When `S` has no members, on the Boolean reading",
                   "When `S` has members, on either reading",
                   "When `P` has no members, on the Aristotelian reading"],
             "c": 1,
             "why": "Both claims empty regions of `S`, and they are jointly satisfied "
                    "when `S` is empty. The Aristotelian reading forbids an empty "
                    "`S`, and so the contrariety returns there; having members only "
                    "makes them incompatible, not compatible."},
            {"q": "In the converse-accidens preset, All `S` are `P` against Some `P` are "
                  "`S`, what are the two verdicts?",
             "a": ["Valid on both readings",
                   "Invalid on both readings",
                   "Valid on the Boolean reading only",
                   "Invalid on the Boolean reading, valid on the Aristotelian"],
             "c": 3,
             "why": "The Boolean reading allows the pattern with nothing occupied, "
                    "which fails Some `P` are `S`. With `S` required to have members "
                    "and all of them inside `P`, the overlap is occupied and the "
                    "conclusion holds."},
        ],
        "mistakes": [
            ("Thinking &ldquo;All `S` are `P`&rdquo; implies &ldquo;Some `S` are `P`&rdquo;",
             "It does only if some `S` exists. On the Boolean reading the lab finds "
             "the pattern with every region empty: the premise is true, the "
             "conclusion false. The step feels safe because the examples we reach for "
             "(dogs, squares) name things that exist, and the logic has no way to "
             "know that."),
            ("Treating the Boolean reading as the claim that there are no such things",
             "The Boolean reading does not say that unicorns are absent. It declines "
             "to assume they are present. The empty pattern is one the premise "
             "allows among many, and an argument is valid only if the conclusion "
             "survives all of them."),
            ("Supposing the switch changes every verdict",
             "Contradictories hold on both readings. Converting No `S` are `P` is "
             "valid on both. Only the steps from a universal claim to a particular "
             "one move. Check the status line, which always reports the verdict on "
             "the reading you are not using."),
        ],
        "standard": (
            "Finish when you can say which side of the switch an inference sits on.",
            "Given an inference from a categorical premise, state its verdict on the "
            "Boolean and on the Aristotelian reading, say whether it needs "
            "existential import, and say which relations on the square hold on each "
            "reading."
        ),
        "note": (
            "Modern logic took the Boolean reading and rebuilt the particular "
            "statements as explicit existence claims, which is the move made in "
            "“Quantifiers and Their Order”. The older reading is not an error; it is "
            "a theory of what ordinary general statements presuppose."
        ),
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "syllogisms-tested-by-venn-regions",
        "title": "Syllogisms Tested by Venn Regions",
        "module": "Categorical logic",
        "one_line": "Test a three-term argument by listing the region patterns its premises allow.",
        "summary": (
            "A syllogism has two premises and three terms. The test is the one for a "
            "single premise: enumerate the patterns of empty and occupied regions the "
            "premises allow, and check the conclusion in each. Barbara, Celarent, "
            "Darii and Ferio pass; the undistributed middle and the illicit major do "
            "not."
        ),
        "key": [
            "three terms: S minor, P major, M middle",
            "valid: no allowed pattern breaks it",
            "Barbara, Celarent, Darii, Ferio: valid",
            "undistributed middle: P and S both inside M",
            "true parts do not make a valid argument",
        ],
        "key_label": "A syllogism, tested by regions",
        "concepts_intro": (
            "Three circles make eight regions and two premises constrain several of "
            "them. What remains open is the whole question."
        ),
        "concepts": [
            ("Three terms, three roles",
             "The conclusion joins the minor term S to the major term P. Each "
             "premise joins one of them to the middle term M, which does not appear "
             "in the conclusion. The premise with P is the major premise, and the one "
             "with S the minor."),
            ("Mood and figure name the shape",
             "The mood is the three letters of the premises and conclusion, such as "
             "AAA. The figure, one to four, says where M sits in the premises. "
             "Together they fix the form, and the valid forms carry traditional "
             "names; the four from the first figure are the ones learnt here, and "
             "the lab knows the rest."),
            ("Validity belongs to the regions",
             "A syllogism is valid when no allowed pattern makes the conclusion "
             "false. Whether the premises or the conclusion are true in the world "
             "plays no part, and the same holds for a one-premise inference."),
        ],
        "read_title": "Eight regions, two premises, one conclusion",
        "read_intro": (
            "The test of the last two lessons, applied to three terms, with the "
            "names that go with the forms that pass."
        ),
        "body": [
            ("def", ("Syllogism",
                     "A <strong>categorical syllogism</strong> has two premises and a "
                     "conclusion, each a categorical statement, over three terms. "
                     "The <strong>minor term</strong> `S` is the conclusion's "
                     "subject, the <strong>major term</strong> `P` its predicate, and "
                     "the <strong>middle term</strong> `M` occurs in both premises "
                     "and not in the conclusion.")),
            ("math", [
                "figure   major premise   minor premise",
                "----------------------------------------",
                "1        M   P            S   M",
                "2        P   M            S   M",
                "3        M   P            M   S",
                "4        P   M            M   S",
            ]),
            ("p", "Three circles divide the plane into eight regions, so a pattern "
                  "of empty and occupied regions is one of 256. The lab considers "
                  "them all, keeps those in which both premises hold, and tests the "
                  "conclusion in each. The count it reports is the number of "
                  "patterns the premises allow, and the argument is valid when the "
                  "conclusion is true in every one."),
            ("example", ("Barbara",
                         "All `M` are `P`, All `S` are `M`, so All `S` are `P`. The "
                         "first premise empties `M` outside `P`. The second empties "
                         "`S` outside `M`. A thing of `S` outside `P` would have to be "
                         "either inside `M`, which the first premise forbids, or "
                         "outside it, which the second forbids. The region is "
                         "empty in every allowed pattern, so the conclusion holds.")),
            ("thm", ("The four moods of the first figure",
                     "Barbara (AAA), Celarent (EAE), Darii (AII) and Ferio (EIO) are "
                     "valid. Celarent is No `M` are `P`, All `S` are `M`, so No `S` "
                     "are `P`. In Darii and Ferio the minor premise, Some `S` are "
                     "`M`, occupies a region inside `S` and `M`. All `M` are `P` "
                     "empties its part outside `P`, so the occupied region is inside "
                     "`P`; No `M` are `P` empties its part inside `P`, so it is "
                     "outside.")),
            ("p", "Two forms look like these and fail. In the second figure, All "
                  "`P` are `M` and All `S` are `M`, so All `S` are `P` (AAA-2) is "
                  "the <strong>undistributed middle</strong>. Both premises say "
                  "only that a circle sits inside `M`. Nothing relates the two "
                  "circles, and `S` may lie in `M` outside `P`. The lab draws that "
                  "pattern."),
            ("p", "The second failure is the <strong>illicit major</strong>: All `M` are "
                  "`P`, No `S` are `M`, so No `S` are `P`. The conclusion makes a "
                  "claim about every `P`, and the major premise gives no information "
                  "about `P` outside `M`. The pattern with `S` and `P` overlapping "
                  "outside `M` satisfies both premises and fails the conclusion."),
            ("p", "The traditional rules, such as that the middle term must be "
                  "distributed at least once, are summaries of these region facts. "
                  "They are quick when they apply and opaque when they do not, "
                  "while the patterns are always available. Where a rule and the "
                  "lab seem to disagree, the lab has the definition."),
            ("p", "Truth in the world does not decide any of this. All cats are "
                  "mammals, all dogs are mammals, so all dogs are cats has true "
                  "premises and a false conclusion, which is the signature of an "
                  "invalid form. But No cats are fish, No dogs are fish, so no "
                  "dogs are cats has true premises and a true conclusion and is "
                  "invalid too: its form allows cats and dogs to overlap outside "
                  "fish. A true conclusion is a coincidence of subject matter and "
                  "is no evidence of form."),
            ("p", "One limit, stated once. The lab takes at most three terms and "
                  "defaults to the Boolean reading, on which the weakened moods "
                  "that draw a particular conclusion from two universal premises "
                  "are invalid. Switching to the Aristotelian reading restores them."),
        ],
        "lab": ("argkit", {
            "mode": "syllogism",
            "preset": "barbara",
            "import": "boolean",
            "presets": [
                {"id": "barbara", "label": "Barbara: All M are P, All S are M, so All S are P",
                 "premises": ["All M are P", "All S are M"], "conclusion": "All S are P", "expect": {"syVerdict": "Valid", "syForm": "AAA-1 Barbara", "syModels": "16"}},
                {"id": "celarent", "label": "Celarent: No M are P, All S are M, so No S are P",
                 "premises": ["No M are P", "All S are M"], "conclusion": "No S are P", "expect": {"syVerdict": "Valid", "syForm": "EAE-1 Celarent", "syModels": "16"}},
                {"id": "darii", "label": "Darii: All M are P, Some S are M, so Some S are P",
                 "premises": ["All M are P", "Some S are M"], "conclusion": "Some S are P", "expect": {"syVerdict": "Valid", "syForm": "AII-1 Darii", "syModels": "32"}},
                {"id": "ferio", "label": "Ferio: No M are P, Some S are M, so Some S are not P",
                 "premises": ["No M are P", "Some S are M"], "conclusion": "Some S are not P", "expect": {"syVerdict": "Valid", "syForm": "EIO-1 Ferio", "syModels": "32"}},
                {"id": "undistributed", "label": "All P are M, All S are M, so All S are P",
                 "premises": ["All P are M", "All S are M"], "conclusion": "All S are P", "expect": {"syVerdict": "Invalid", "syForm": "AAA-2 (no name)", "syModels": "32", "syCounter": "S+M"}},
                {"id": "illicit-major", "label": "All M are P, No S are M, so No S are P",
                 "premises": ["All M are P", "No S are M"], "conclusion": "No S are P", "expect": {"syVerdict": "Invalid", "syForm": "AEE-1 (no name)", "syModels": "32", "syCounter": "S+P"}},
            ],
            "panel_title": "Patterns the premises allow",
            "panel_intro": (
                "Run the four named forms and note that each has no counterexample. "
                "Then run the last two, read the counterexample regions, and "
                "describe in a sentence the things they contain."
            ),
        }),
        "steps_title": "Testing a syllogism",
        "steps_intro": "Five steps. A diagram helps; the patterns decide.",
        "steps": [
            ("Find the three terms and their roles",
             "The conclusion's subject is `S` and its predicate `P`. The remaining "
             "term, in both premises, is `M`."),
            ("Put each premise as a region claim",
             "Each universal premise empties a region of the three-circle diagram; "
             "each particular premise requires one occupied."),
            ("List what the premises force",
             "Mark the regions emptied. Note where a particular premise has more "
             "than one region it could use."),
            ("Check the conclusion in every pattern",
             "Ask whether each pattern the premises allow makes the conclusion true. "
             "One failure is the counterexample."),
            ("Name the form",
             "Write mood and figure. If it is one of Barbara, Celarent, Darii or "
             "Ferio, or the undistributed middle, you have a name; the verdict "
             "comes from the patterns."),
        ],
        "worked": {
            "title": "Cats, dogs and mammals",
            "intro": [
                "&ldquo;All cats are mammals. All dogs are mammals. So all dogs are "
                "cats.&rdquo; Let `S` be the dogs, `P` the cats and `M` the mammals. "
                "The major premise is the one with the cats.",
            ],
            "lines": [
                "P1.  All cats are mammals      P inside M",
                "P2.  All dogs are mammals      S inside M",
                "C.   All dogs are cats         S inside P",
                "form: AAA, figure 2",
                "counterexample: dogs inside mammals, outside cats",
            ],
            "after": [
                "Both premises are satisfied by a pattern in which the only occupied "
                "region is the dogs that are mammals but not cats. In it the "
                "conclusion fails. Nothing about cats or dogs was used beyond the "
                "shape: the same pattern refutes the form whatever the three terms "
                "name, which is why the verdict can be read off before anyone asks "
                "whether the sentences are true.",
            ],
        },
        "quiz_title": "Syllogism checks",
        "quiz": [
            {"q": "A syllogism has true premises and a true conclusion. What follows "
                  "about its validity?",
             "a": ["It is valid, because the conclusion is true",
                   "Nothing: it may be valid or invalid, and only the patterns "
                   "decide",
                   "It is invalid, because the premises are separate from the "
                   "conclusion",
                   "It is valid if the conclusion is particular"],
             "c": 1,
             "why": "Truth of the parts is compatible with either verdict. No cats "
                    "are fish, no dogs are fish, no dogs are cats has all three "
                    "true and is invalid; Barbara with true parts is valid."},
            {"q": "Which pattern refutes &ldquo;All `P` are `M`, All `S` are `M`, so "
                  "All `S` are `P`&rdquo;?",
             "a": ["`S` inside `M` and outside `P`",
                   "`P` inside `M` and inside `S`",
                   "`S` outside `M`",
                   "`M` outside `P` and `S`"],
             "c": 0,
             "why": "That pattern satisfies both premises and puts something of `S` "
                    "outside `P`. The others each break a premise or leave the "
                    "conclusion true: the second makes `S` and `P` overlap, and "
                    "something in `S` outside `M` breaks the minor premise."},
            {"q": "Why is Darii valid? All `M` are `P`, Some `S` are `M`, so Some `S` "
                  "are `P`.",
             "a": ["Because a particular conclusion always follows from a universal "
                   "premise",
                   "Because both premises are true",
                   "Because the middle term is distributed in the minor premise",
                   "Because the occupied part of `S` inside `M` is forced into `P`, "
                   "as `M` outside `P` is empty"],
             "c": 3,
             "why": "The minor premise occupies a region inside both `S` and `M`; "
                    "the major premise empties the part of `M` outside `P`; so "
                    "the occupied region lies inside `P`. A particular conclusion "
                    "does not follow from just any universal premise, truth is no "
                    "part of validity, and the minor premise distributes nothing."},
            {"q": "On the Boolean reading, which conclusion follows from No `M` are "
                  "`P` and All `S` are `M`?",
             "a": ["No `S` are `P`", "All `S` are `P`",
                   "Some `S` are `P`", "Some `S` are not `P`"],
             "c": 0,
             "why": "That is Celarent: `S` lies inside `M`, `M` is disjoint from "
                    "`P`, so `S` is disjoint from `P`. The last choice would need an "
                    "`S` to exist, which the Boolean reading does not assume."},
        ],
        "mistakes": [
            ("Calling a syllogism valid because its premises and conclusion are all true",
             "Validity is about whether the premises force the conclusion, and a "
             "true conclusion can be a coincidence. No cats are fish, no dogs are "
             "fish, so no dogs are cats has three true statements, and the lab finds "
             "a pattern where cats and dogs overlap outside fish. The same "
             "arrangement with a false conclusion is easy to find, and the form is "
             "the same."),
            ("Drawing one picture and stopping",
             "A diagram in which the premises hold and the conclusion holds is "
             "easy to draw for almost any syllogism. It proves nothing unless the "
             "conclusion holds in every picture the premises allow. The lab looks at "
             "all of them, and the count of patterns shows how many there were."),
            ("Naming the form from the order the premises are typed",
             "The major premise is the one containing the conclusion's predicate, "
             "whichever line it is typed on. The lab names the mood and figure from "
             "the term positions, so swapping the premises does not change the "
             "name or the verdict."),
        ],
        "standard": (
            "Finish when you can show the pattern that decides it.",
            "Given a three-term syllogism, identify the major, minor and middle "
            "terms, state mood and figure, say whether the premises force the "
            "conclusion, and when they do not describe the counterexample pattern "
            "in plain words."
        ),
        "note": (
            "Nothing here depends on the syllogism being the only form of argument. "
            "Its use in this course is as a second example of a test that works by "
            "listing cases, after the truth table."
        ),
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "quantifiers-and-their-order",
        "title": "Quantifiers and Their Order",
        "module": "Quantifiers and fallacies",
        "one_line": "Read every and some over a finite universe, and see why their order cannot be swapped.",
        "summary": (
            "A universal claim over a finite universe is a check of every member, an "
            "existential claim a search for one. With two variables the order "
            "decides whether one partner is shared by all or each member has its "
            "own, and the shift from the second to the first is a fallacy that a "
            "grid exposes."
        ),
        "key": [
            "∀x: true for every member of the universe",
            "∃x: true for at least one member",
            "∀x ∃y: each x has its own y",
            "∃y ∀x: one y serves every x",
            "∃y ∀x implies ∀x ∃y, not the reverse",
        ],
        "key_label": "Two quantifiers, two orders",
        "concepts_intro": (
            "The categorical forms had one variable. Statements about relations "
            "need two, and the order in which they are quantified is a change of "
            "meaning."
        ),
        "concepts": [
            ("Over a finite universe, a quantifier is a check",
             "With a universe of four members, `∀x P(x)` says P holds at each of the "
             "four and `∃x P(x)` says it holds at one or more. Either can be settled "
             "by looking. The lab shows the universe, so no truth is hidden."),
            ("The order picks who chooses",
             "In `∀x ∃y P(x, y)` the y is chosen after the x is known, so it may "
             "differ from one x to the next. In `∃y ∀x P(x, y)` the y is chosen first "
             "and must serve every x. On a grid, the first is a true cell in "
             "every row; the second is a column that is true throughout."),
            ("The universe is part of the claim",
             "A statement is true or false of a universe, not in itself. The "
             "same formula can be true over all the numbers and false over the "
             "first four, because a member is missing at the edge."),
        ],
        "read_title": "Reading a grid",
        "read_intro": (
            "A relation over four things is a four-by-four grid of true and false. "
            "Every quantified statement about it is a question about the grid."
        ),
        "body": [
            ("def", ("Quantifiers over a finite universe",
                     "The <strong>universal quantifier</strong> `∀x` says that every "
                     "member of the universe satisfies what follows; the "
                     "<strong>existential quantifier</strong> `∃x` says that at least "
                     "one does. Over a finite universe the first is a conjunction of "
                     "the cases and the second a disjunction.")),
            ("p", "With one variable, this is the categorical logic of the last "
                  "lessons. All `S` are `P` is `∀x (S(x) → P(x))`, and Some `S` are "
                  "`P` is `∃x (S(x) ∧ P(x))`. With two variables the new thing is "
                  "that the order of quantifiers can change the meaning."),
            ("p", "Let `P(x, y)` mean that `y` is the successor of `x`, over the "
                  "numbers 1 to 4. The grid has rows for `x` and columns for `y`, "
                  "and a true cell where `y = x + 1`. Read `∀x ∃y P(x, y)` as: for "
                  "every `x` there is a `y`. Read `∃y ∀x P(x, y)` as: there is a "
                  "`y` such that, for every `x`, `P(x, y)` holds."),
            ("math", [
                "form       reads as                  on the grid",
                "-------------------------------------------------",
                "∀x ∃y P    each x has its own y      a true cell per row",
                "∃y ∀x P    one y serves every x      a column all true",
                "∃x ∀y P    one x pairs with every y  a row all true",
                "∀y ∃x P    each y has its own x      a true cell per column",
            ]),
            ("p", "These are different statements, and the lab shows all six "
                  "forms of two quantifiers at once. Over the infinite numbers, "
                  "everything has a successor and nothing is everything's "
                  "successor, so `∀x ∃y P(x, y)` is true and `∃y ∀x P(x, y)` is false. "
                  "The finite lab makes one thing visible that the infinite "
                  "case hides: the grid ends. In the successor preset the number 4 "
                  "has no partner, so the first form is false at the edge."),
            ("p", "To see the separation, close the loop. Click the cell with `x` equal "
                  "to 4 and `y` equal to 1, so that 4 + 1 wraps round to 1, as on a "
                  "clock. Now every row has a true cell, and no column has more "
                  "than one. `∀x ∃y P(x, y)` is true and `∃y ∀x P(x, y)` is false, and the "
                  "lab's status line says that this is the case that settles the "
                  "order question."),
            ("thm", ("Which direction holds",
                     "`∃y ∀x P(x, y)` implies `∀x ∃y P(x, y)`: if one `y` serves "
                     "every `x`, it serves each. The reverse fails. One grid with "
                     "the first true and the second false is a complete refutation "
                     "of the reverse, whatever the size of the universe.")),
            ("example", ("A quantifier shift",
                         "&ldquo;Everything has a cause, so something causes "
                         "everything.&rdquo; Read `P(x, y)` as `x` having `y` as a "
                         "cause. The premise is `∀x ∃y P(x, y)`, a true cell in every "
                         "row. The conclusion is `∃y ∀x P(x, y)`, a column all true. "
                         "The wrapped successor grid is a case with the first and not "
                         "the second, so the step is invalid. Whether the premise is "
                         "true of the world is a separate question, and so is whether "
                         "any serious version of the cosmological argument takes this "
                         "step: its defenders say it does not, and argue instead that "
                         "a chain of causes with no first member is itself impossible. "
                         "That reply grants the verdict on the form and disputes the "
                         "formalisation, which is the right kind of reply to make.")),
            ("p", "A finite grid is a legitimate countermodel. The lab does not search "
                  "every possible universe, and does not need to for this verdict, "
                  "because one universe with true premise and false conclusion is "
                  "all invalidity takes. It could not, by looking at a few grids, "
                  "prove the other direction; that follows from the meaning of the "
                  "words."),
        ],
        "lab": ("quantifier", {
            "size": 4,
            "preset": "succ",
            "panel_title": "Rows, columns and the six orders",
            "panel_intro": (
                "The grid is the relation: a cell is true when the pair holds. "
                "Start with the successor preset and read the verdict for each "
                "of the six forms. Then click the cell in the last row and "
                "first column, and watch which forms change."
            ),
        }),
        "steps_title": "Reading a nested quantifier on a grid",
        "steps_intro": "Four steps, and the order of the quantifiers is the first.",
        "steps": [
            ("Read the quantifiers left to right",
             "The first quantifier is chosen first. If it is `∀`, everything is "
             "considered; if it is `∃`, a single member is picked and held while the "
             "rest are tested."),
            ("Say what has to be shared",
             "In `∃y ∀x` the same y must work for every x. In `∀x ∃y` the y may "
             "change from one x to the next."),
            ("Look at the grid for the shape",
             "A full row, a full column, a true cell in every row, a true cell in "
             "every column or just a true cell somewhere. Each form asks for one "
             "of these."),
            ("Check the edges of the universe",
             "Ask whether the claim would still hold if the universe were larger, "
             "and whether it holds only because of its boundary."),
        ],
        "worked": {
            "title": "The successor grid, closed into a loop",
            "intro": [
                "Over 1 to 4, let `P(x, y)` be &ldquo;`y` follows `x`&rdquo;, with 4 "
                "followed by 1. The rows are `x` and the columns `y`.",
            ],
            "lines": [
                "x \\ y    1   2   3   4",
                "1        F   T   F   F",
                "2        F   F   T   F",
                "3        F   F   F   T",
                "4        T   F   F   F",
            ],
            "after": [
                "Every row has exactly one true cell, so for each `x` there is a "
                "`y`: `∀x ∃y P(x, y)` is true. No column is true throughout, since "
                "each has three false cells, so no one `y` serves every `x`: "
                "`∃y ∀x P(x, y)` is false. Without the wrap the fourth row is empty "
                "and the first form fails too, which is the finite universe saying "
                "that the claim about the numbers needs the numbers to go on.",
            ],
        },
        "quiz_title": "Order and shape",
        "quiz": [
            {"q": "On a grid, `∃y ∀x P(x, y)` is true when",
             "a": ["some row is true throughout",
                   "every row has at least one true cell",
                   "some column is true throughout",
                   "some cell is true"],
             "c": 2,
             "why": "One `y`, a column, must pair with every `x`. A row true throughout "
                    "is `∃x ∀y`, a true cell in every row is `∀x ∃y`, and some true "
                    "cell is `∃x ∃y`."},
            {"q": "Which statement is correct?",
             "a": ["`∃y ∀x P(x, y)` implies `∀x ∃y P(x, y)`, but not the reverse",
                   "`∀x ∃y P(x, y)` implies `∃y ∀x P(x, y)`, but not the reverse",
                   "The two always have the same value",
                   "Neither implies the other"],
             "c": 0,
             "why": "If one `y` works for all `x`, then each `x` has a `y`, namely "
                    "that one. The wrapped successor grid shows the reverse fails, "
                    "so the second and third choices are wrong, and the last ignores "
                    "the valid direction."},
            {"q": "&ldquo;Everyone loves someone, so there is someone whom everyone "
                  "loves.&rdquo; Which is the best verdict?",
             "a": ["Valid, since someone is loved by everyone who loves anyone",
                   "Invalid: people each love the next around a ring, so everyone "
                   "loves someone and no one is loved by all",
                   "Valid, since the universe is finite",
                   "Invalid only if the universe is infinite"],
             "c": 1,
             "why": "A ring of four people is a universe with a true premise and a "
                    "false conclusion, and one such universe is enough. The finite "
                    "size does not rescue the argument, which is why the last two "
                    "choices fail."},
            {"q": "A universe of four members, and `P(x, y)` true in exactly one "
                  "cell. Which of the six forms is true?",
             "a": ["None of them",
                   "`∃x ∃y P(x, y)` and `∀x ∃y P(x, y)`",
                   "`∃x ∃y P(x, y)` and `∃y ∀x P(x, y)`",
                   "Only `∃x ∃y P(x, y)`"],
             "c": 3,
             "why": "A single true cell satisfies the some-some form. `∀x ∃y` needs a "
                    "true cell in every row, and the other three rows are empty; "
                    "`∃y ∀x` needs four true cells in a column."},
        ],
        "mistakes": [
            ("Inferring ∃y ∀x P(x, y) from ∀x ∃y P(x, y)",
             "The first says one partner serves all; the second says each has a "
             "partner of its own. The wrapped successor grid has a true cell in "
             "every row and no column true throughout. Reading the two quantifiers "
             "as if the order did not matter is the quantifier shift, and it is the "
             "mistake the cosmological argument is accused of."),
            ("Reading &ldquo;everyone loves someone&rdquo; as a claim about one person",
             "The English sentence is ambiguous and the formulas are not. "
             "`∀x ∃y` allows a different object of love for each person; `∃y ∀x` "
             "demands a single beloved. The grid makes you choose, and the choice "
             "changes the verdict."),
            ("Forgetting that the universe belongs to the claim",
             "Over all the numbers every number has a successor. Over 1 to 4, the "
             "fourth has none, and the claim fails at the edge. Whenever a verdict "
             "depends on the size of the grid, say so, and say which size you "
             "meant."),
        ],
        "standard": (
            "Finish when you can read the order off the grid.",
            "Given a relation as a grid, state the values of all six two-quantifier "
            "forms and the cell, row or column that decides each, and say which "
            "direction between `∀x ∃y` and `∃y ∀x` holds and why."
        ),
        "note": (
            "A universe is a list you can see, so every verdict can be checked by "
            "looking. This course does not search all universes for a countermodel; "
            "it uses a single universe, which is enough to refute a form and not "
            "enough to prove one valid."
        ),
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "fallacies-and-the-counterexample-method",
        "title": "Fallacies and the Counterexample Method",
        "module": "Quantifiers and fallacies",
        "one_line": "Refute an invalid form by writing an argument of the same form with true premises and a false conclusion.",
        "summary": (
            "A form is refuted by an argument of that form whose premises are "
            "plainly true and whose conclusion is plainly false. The method sorts "
            "the valid forms, hypothetical syllogism, disjunctive syllogism and "
            "constructive dilemma, from the fallacies that resemble them, and it "
            "is the course's table put to use on sentences."
        ),
        "key": [
            "refute a form: same shape, true premises, F",
            "p → q, q → r ∴ p → r     valid",
            "p ∨ q, ¬p ∴ q            valid",
            "p ∨ q, p ∴ ¬q            affirming a disjunct",
            "a false conclusion does not mean invalid",
        ],
        "key_label": "Valid forms, and the fallacies beside them",
        "concepts_intro": (
            "Showing that a form is bad takes one argument of that form that "
            "obviously fails. The table says which row to imitate."
        ),
        "concepts": [
            ("A counterexample is a substitution",
             "Take a counterexample row from the table, and choose a real sentence "
             "for each letter so that it has the value the row gives it. The "
             "result is an argument of the same shape with true premises and a "
             "false conclusion."),
            ("Valid forms have no such row",
             "Hypothetical syllogism, disjunctive syllogism and constructive "
             "dilemma have none, so no substitution can work. That is a theorem "
             "about the form, not a failure of imagination."),
            ("Validity is independent of the truth of the parts",
             "A valid argument may have a false conclusion, and an invalid one a "
             "true conclusion. The verdict comes from the rows. What the world "
             "supplies is only the sentences with which to illustrate them."),
        ],
        "read_title": "Three forms that hold, two that do not",
        "read_intro": (
            "The lab names each shape from a catalogue; the table decides the "
            "verdict, and the method turns a row into a sentence."
        ),
        "body": [
            ("p", "Three forms are valid and are worth knowing by name. "
                  "<strong>Hypothetical syllogism</strong> chains two conditionals: "
                  "`p → q`, `q → r`, so `p → r`. <strong>Disjunctive syllogism</strong> "
                  "rules out one alternative: `p ∨ q`, `¬p`, so `q`. "
                  "<strong>Constructive dilemma</strong> combines two conditionals "
                  "with a disjunction: `p → q`, `r → s`, `p ∨ r`, so `q ∨ s`. Each "
                  "has no row in which the premises hold and the conclusion fails."),
            ("p", "Two look similar and are not. <strong>Affirming a disjunct</strong> "
                  "treats an inclusive or as exclusive: `p ∨ q`, `p`, so `¬q`. "
                  "<strong>Denying the antecedent</strong>, from “Validity by Truth "
                  "Table”, is `p → q`, `¬p`, so `¬q`. In the first the troublesome "
                  "row is `p` true and `q` true."),
            ("math", [
                "p   q  |  p ∨ q   p  |  ¬q",
                "---------------------------",
                "T   T  |    T     T  |  F    counterexample",
                "T   F  |    T     T  |  T",
                "F   T  |    T     F  |  F    a premise is F",
                "F   F  |    F     F  |  T    a premise is F",
            ]),
            ("def", ("Counterexample method",
                     "To refute a form, find a row of its table with every premise "
                     "true and the conclusion false, then replace each letter with "
                     "a sentence that has the value the row gives it. The result is "
                     "an argument of the same form whose premises are plainly "
                     "true and whose conclusion is plainly false.")),
            ("example", ("The same shape in the open",
                         "&ldquo;Either Paris is in France or Rome is in Italy. "
                         "Paris is in France. So Rome is not in Italy.&rdquo; The "
                         "row is `p` true and `q` true, and both sentences are true. "
                         "Both premises are true and the conclusion is false, so "
                         "the shape cannot be valid, and the argument needed no "
                         "detective story to show it.")),
            ("p", "The method is also how a weak argument is identified in a "
                  "conversation without a table. Say the form in letters, ask which "
                  "row would break it, and offer a case of that kind. For denying "
                  "the antecedent the row is `p` false and `q` true: “If 6 is "
                  "divisible by 4, then 6 is even; 6 is not divisible by 4; so 6 is "
                  "not even.” Both premises are true and the conclusion is false."),
            ("p", "What the method does not do is refute the conclusion of the "
                  "original argument. An invalid form shows that the premises do "
                  "not guarantee the conclusion. The conclusion may still be true, and "
                  "may be established by another route. “If 9 is divisible by 4, "
                  "then 9 is even; 9 is not divisible by 4; so 9 is not even” has the "
                  "same shape, true premises and a true conclusion, and is invalid "
                  "still."),
            ("p", "Valid forms behave differently when their conclusion is false. "
                  "Disjunctive syllogism with “the moon is cheese or Paris is in "
                  "Germany; the moon is not cheese; so Paris is in Germany” is valid "
                  "and the conclusion is false. A false conclusion forces a false "
                  "premise, and here it is the first."),
            ("thm", ("What a false conclusion tells you",
                     "If a valid argument has a false conclusion, at least one premise "
                     "is false. If an argument has true premises and a false "
                     "conclusion, it is invalid. A false conclusion alone settles "
                     "nothing about validity.")),
            ("p", "In the lab, choose each of the five presets in turn. The lab names "
                  "the form from the shape of the formulas, and the verdict "
                  "comes from the rows. Hypothetical syllogism has three letters "
                  "and eight rows, disjunctive syllogism two and four, and the "
                  "dilemma four letters and sixteen rows."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "preset": "hs",
            "show": "all",
            "presets": [
                {"id": "hs", "label": "hypothetical syllogism: p → q, q → r, so p → r",
                 "premises": ["p -> q", "q -> r"], "conclusion": "p -> r", "expect": {"vaVerdict": "Valid", "vaForm": "hypothetical syllogism", "vaRows": "8"}},
                {"id": "ds", "label": "disjunctive syllogism: p ∨ q, ¬p, so q",
                 "premises": ["p | q", "~p"], "conclusion": "q", "expect": {"vaVerdict": "Valid", "vaForm": "disjunctive syllogism", "vaRows": "4"}},
                {"id": "cd", "label": "constructive dilemma: p → q, r → s, p ∨ r, so q ∨ s",
                 "premises": ["p -> q", "r -> s", "p | r"], "conclusion": "q | s", "expect": {"vaVerdict": "Valid", "vaForm": "constructive dilemma", "vaRows": "16"}},
                {"id": "affirm-disjunct", "label": "affirming a disjunct: p ∨ q, p, so ¬q",
                 "premises": ["p | q", "p"], "conclusion": "~q", "expect": {"vaVerdict": "Invalid", "vaForm": "affirming a disjunct", "vaCounter": "1"}},
                {"id": "da", "label": "denying the antecedent: p → q, ¬p, so ¬q",
                 "premises": ["p -> q", "~p"], "conclusion": "~q", "expect": {"vaVerdict": "Invalid", "vaForm": "denying the antecedent", "vaCounter": "1"}},
            ],
            "panel_title": "Five forms, one row each",
            "panel_intro": (
                "For each invalid preset, read the counterexample row and write a "
                "real argument of that shape with true premises and a false "
                "conclusion. For each valid one, try to do the same and say why "
                "you cannot."
            ),
        }),
        "steps_title": "Refuting a form with a case",
        "steps_intro": "Five steps; the third is the craft.",
        "steps": [
            ("Write the form in letters",
             "Replace each simple sentence with a letter, one letter per sentence, "
             "and keep the connectives."),
            ("Find a counterexample row",
             "Use the table, or the lab. If there is none, the form is valid and "
             "the method has nothing to offer."),
            ("Choose sentences that fit the row",
             "For each letter pick a sentence whose actual truth value is the "
             "row's. Arithmetic and geography are good sources, because nobody "
             "disputes them."),
            ("Check the instance",
             "Every premise must be true, and the conclusion false. If a premise "
             "is false, the instance refutes nothing."),
            ("State what has been shown",
             "The form is invalid. Say nothing about the original conclusion, "
             "which may be true."),
        ],
        "worked": {
            "title": "The butler and the maid",
            "intro": [
                "&ldquo;Either the butler or the maid did it. The butler did it. "
                "So the maid did not.&rdquo; Let `p` be the butler and `q` the "
                "maid.",
            ],
            "lines": [
                "P1.  The butler did it or the maid did.     p ∨ q",
                "P2.  The butler did it.                     p",
                "C.   The maid did not do it.                ¬q",
                "counterexample row:   p = T,  q = T",
                "same form: raining or Tuesday; raining; so not Tuesday",
            ],
            "after": [
                "In the row `p` true and `q` true the premises hold and the "
                "conclusion fails: they did it together. The pattern is audible "
                "with the same form on a rainy Tuesday: it is raining or it is "
                "Tuesday, it is raining, so it is not Tuesday. The argument "
                "moves from one alternative to the denial of the other and "
                "treats or as exclusive. It does not show that the maid is "
                "guilty; it shows that this reason does not clear her.",
            ],
        },
        "quiz_title": "Forms and counterexamples",
        "quiz": [
            {"q": "Which argument is valid?",
             "a": ["`p ∨ q`, `p`, so `¬q`",
                   "`p → q`, `¬p`, so `¬q`",
                   "`p ∨ q`, `¬p`, so `q`",
                   "`p → q`, `q`, so `p`"],
             "c": 2,
             "why": "Disjunctive syllogism has no row with both premises true and "
                    "`q` false. The others are affirming a disjunct, denying the "
                    "antecedent and affirming the consequent, each of which has "
                    "one."},
            {"q": "A valid argument has a false conclusion. What must be true?",
             "a": ["Its form has a counterexample row",
                   "At least one premise is false",
                   "Every premise is true",
                   "Every premise is false"],
             "c": 1,
             "why": "A valid argument cannot have true premises and a false "
                    "conclusion, so a false conclusion means a premise is false. "
                    "A valid form has no counterexample row. That all the premises "
                    "are false is possible but is not forced, and all true is "
                    "ruled out."},
            {"q": "Which letters give a counterexample to affirming a disjunct, "
                  "`p ∨ q`, `p`, so `¬q`?",
             "a": ["`p`: Paris is in Germany; `q`: Rome is in Italy",
                   "`p`: Paris is in France; `q`: Rome is in Spain",
                   "`p`: Paris is in Germany; `q`: Rome is in Spain",
                   "`p`: Paris is in France; `q`: Rome is in Italy"],
             "c": 3,
             "why": "The row needs both `p` and `q` true. Only the last choice "
                    "has both true, so both premises hold and `¬q` is false. The "
                    "first makes `p` false, the second makes `q` false and the "
                    "third makes both false."},
            {"q": "How many counterexample rows does the constructive dilemma "
                  "preset have?",
             "a": ["None, in sixteen rows", "One, in sixteen rows",
                   "Four, in sixteen rows", "Sixteen, in sixteen rows"],
             "c": 0,
             "why": "Constructive dilemma is valid. Its four letters give sixteen "
                    "rows, and in none do `p → q`, `r → s` and `p ∨ r` hold with "
                    "`q ∨ s` false."},
        ],
        "mistakes": [
            ("Judging an argument invalid because its conclusion is false",
             "Validity concerns the link, not the conclusion. “The moon is cheese or "
             "Paris is in Germany; the moon is not cheese; so Paris is in Germany” "
             "is valid with a false conclusion, because a premise is false. "
             "And “If 9 is divisible by 4 then 9 is even; it is not; so 9 is not "
             "even” has true parts and is invalid. The table, not the conclusion, "
             "decides."),
            ("Treating the counterexample as a proof that the original conclusion "
             "is false",
             "The counterexample is to the form. It shows the premises do not "
             "force the conclusion. The maid may be innocent; the argument just "
             "did not show it. A better argument for the same conclusion is "
             "always possible."),
            ("Building a counterexample in which a premise is false",
             "An instance with a false premise and a false conclusion is "
             "compatible with a valid form. The substitution must make every "
             "premise true, as well as the conclusion false. Check the premises "
             "one at a time."),
        ],
        "standard": (
            "Finish when you can answer a bad form with a case.",
            "Given an argument in sentences, write its form in letters, say whether "
            "it is valid, and if not produce a counterexample row and an instance "
            "of the same form with true premises and a false conclusion."
        ),
        "note": (
            "Informal fallacies such as ad hominem have no table. They are failures "
            "of relevance, and the method here does not reach them. The rest of the "
            "Subject uses this course's test whenever it sets out a famous argument "
            "and asks which premise to doubt."
        ),
    },
]
