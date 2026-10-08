"""Course 8, lessons 7 to 12: the rest of identity over time, freedom, and evil.

Two lessons on identity (psychological continuity as the ancestral of a direct
tie, and fission as an inconsistent set), three on freedom (the triad, the
consequence argument as the K axiom, Frankfurt cases in a structural model) and
the problem of evil as the same inconsistent-set method applied once more.

The consistency lab writes negation with a tilde and the conditional with an
arrow of two characters; the prose writes the symbols. The kripke lab's box
here is read as "no one has power over", and the lessons say what the arcs
mean before using it.
"""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "personal-identity-and-psychological-continuity",
        "title": "Personal Identity and Psychological Continuity",
        "module": "Identity over time",
        "one_line": "A direct tie between stages of a life, such as a memory, is not transitive, and the chain of such ties is what identity can follow.",
        "summary": (
            "Reid's brave officer remembers the boy he was and is remembered by the general he became, "
            "while the general no longer remembers the boy. Memory between stages is therefore not "
            "transitive, and identity is. The relation lab shows the gap on five stages, and its "
            "closure control shows the chain that fills it."
        ),
        "key": [
            "connected: a direct tie, such as a memory",
            "continuous: a chain of overlapping ties",
            "a direct tie need not be transitive",
            "continuity is the closure of the tie",
            "identity follows the chain, not the tie",
        ],
        "key_label": "A tie between stages, and the chain of ties",
        "concepts_intro": (
            "The previous lesson asked what makes a ship the same ship through change of parts. A person "
            "changes too, and the most natural answer is that a person is held together by the mind, "
            "not the planks. This lesson tests that answer on its first objection."
        ),
        "concepts": [
            ("Connectedness is a direct tie",
             "Two stages of a life are <strong>connected</strong> when one directly carries something of the "
             "other: a memory, an intention carried out, a belief or a trait. It is a relation between two "
             "stages, it comes in degrees, and the lab draws it as a single pair in a grid."),
            ("Continuity is a chain of ties",
             "Two stages are <strong>continuous</strong> when some chain of connected stages leads from one to "
             "the other. In the vocabulary of the relation lab it is the transitive closure of connectedness: "
             "every pair joined by a path of one or more steps."),
            ("A connection can fail where a continuity holds",
             "Because the tie is direct, it need not pass through. A stage can be connected to its neighbour "
             "on each side and to nothing further away, and the stages at the ends are still continuous. "
             "That gap is the whole lesson."),
        ],
        "read_title": "From a tie to a chain",
        "read_intro": "Locke's proposal, Reid's objection to it, and the relation that repairs it.",
        "body": [
            ("p", "Locke proposed that a person is the same person as far back as the person's consciousness "
                  "extends, and the plainest evidence of that reach is memory. If I remember doing something, "
                  "I am the one who did it. The proposal is a criterion for when two stages of a life, a "
                  "person at one time and a person at another, belong to one person."),
            ("p", "Thomas Reid answered with a case. A brave officer, in his first campaign, took a standard "
                  "from the enemy. As a boy he had been flogged for robbing an orchard. When he took the "
                  "standard he remembered the flogging. Late in life, as a general, he remembers taking the "
                  "standard and has quite lost the flogging. So the officer is the boy, since he remembers "
                  "being flogged. The general is the officer, since he remembers the standard. And by the "
                  "same criterion the general is not the boy, since he remembers nothing of the orchard. "
                  "Identity is transitive, so a criterion that says all three things has contradicted itself."),
            ("math", [
                "officer remembers boy:      yes",
                "general remembers officer:  yes",
                "general remembers boy:      no",
            ]),
            ("def", ("Connectedness and continuity",
                     "Two stages are <strong>psychologically connected</strong> when there is a direct tie "
                     "of the kind memory gives. They are <strong>psychologically continuous</strong> when "
                     "there is a sequence of stages from the one to the other in which each is connected "
                     "to the next. Continuity is the <strong>transitive closure</strong> of connectedness.")),
            ("p", "The repair is the one the definition makes. Let the tie be as weak as Reid likes. The "
                  "general and the boy are not connected, but they are continuous, since the officer stands "
                  "between them and each neighbouring pair is tied. The criterion for identity is then "
                  "continuity, not connectedness, and Reid's contradiction is gone: the three stages are "
                  "one person, and the general does not need to remember the boy for that to be so."),
            ("p", "The relation lab draws this on five stages. Read the pair `(a, b)` as &ldquo;stage `b` "
                  "directly remembers stage `a`&rdquo;, and take the pattern in which each stage remembers "
                  "only the one just before it. The grid holds four pairs, the first with `a = 1` and "
                  "`b = 2`, and the property table finds the failing triple at once: the pairs "
                  "`(1, 2)` and `(2, 3)` are in the relation and `(1, 3)` is not. The relation is not "
                  "transitive, and that is Reid's finding on five stages instead of three."),
            ("p", "Set the closure control to transitive. The lab marks six more cells, the pairs "
                  "`(1, 3)`, `(1, 4)`, `(1, 5)`, `(2, 4)`, `(2, 5)` and `(3, 5)`, and with the original "
                  "four they fill the cells above the diagonal. The relation the closure draws is &ldquo;stage "
                  "`a` comes earlier than stage `b` in one chain&rdquo;, and every stage is continuous with "
                  "every other. The closure leaves the original four pairs where they were. It does not "
                  "invent a memory; it adds the pairs that a chain of memories supplies."),
            ("h3", "What the repair leaves open"),
            ("p", "Two limits should be stated. The first is that the chain needs enough strength at each "
                  "link. A link so faint that nothing remains of the earlier stage is no tie at all, and "
                  "the lab has only two answers, a pair or no pair, where a real tie comes in degrees. "
                  "Where to put the threshold is an input, as the cutoff was in the previous lesson."),
            ("p", "The second is that continuity as defined does not say that the chain is unique. If a "
                  "single stage can be continuous with two later stages that are not continuous with each "
                  "other, a person has been divided, and identity, which is one-one, cannot follow the chain "
                  "in both directions. The next lesson takes that case as its subject. Here the chain "
                  "runs in a line, and a line is what the closure of the next-stage relation is."),
            ("example", ("The closure is not the tie",
                         "Five stages, each remembering the one before. The relation has 4 pairs and fails "
                         "transitivity at `(1, 2)` and `(2, 3)`. Its transitive closure has 10 pairs, every "
                         "pair `(a, b)` with `a` less than `b`. Stage 5 is continuous with stage 1 and "
                         "directly connected to stage 4 only.")),
        ],
        "lab": ("relation", {
            "size": 5, "preset": "succ",
            "panel_title": "Five stages, each remembering the one before",
            "panel_intro": "Row `a`, column `b`: a 1 means stage `b` directly remembers stage `a`. As shipped, every stage remembers only its predecessor, so the grid has four pairs and the transitive row of the property table is <strong>no</strong>, naming the pair of pairs that fails. Set the closure selector to transitive and the amber cells are the chain's contribution. Then click a cell to add a pair of your own, or to remove one such as row 3, column 4, and watch the chain break where the tie does.",
        }),
        "steps_title": "Testing a criterion of identity over time",
        "steps_intro": "Five moves for any criterion that names a tie between stages.",
        "steps": [
            ("Name the tie",
             "Say what must hold directly between two stages for them to count as linked: remembering, "
             "carrying out an intention, keeping a trait. Write it as a set of pairs."),
            ("Check the tie for transitivity",
             "For each pair of pairs `(a, b)` and `(b, c)`, look for `(a, c)`. Any missing pair is a "
             "stage that the criterion cannot link to a stage it ought to."),
            ("Read the criterion as a claim about identity",
             "Identity is transitive. If the criterion says the stages are one person whenever the tie "
             "holds, a missing `(a, c)` is a contradiction, not a free choice."),
            ("Replace the tie by its closure",
             "Take every pair joined by a chain of ties. This is a criterion of continuity, and it can "
             "be transitive because it was built to be."),
            ("Ask what the closure now permits",
             "Check whether one stage can be continuous with two stages that are not continuous with "
             "each other. If it can, identity has been asked to follow a fork."),
        ],
        "worked": {
            "title": "Reid's officer, in three stages",
            "intro": ["Three stages: the boy, the officer and the general. A pair is a memory of the earlier by the later."],
            "lines": [
                "pairs:   (boy, officer), (officer, general)",
                "is (boy, general) a pair?  no",
                "so the tie is not transitive",
                "chain: boy to officer to general",
                "closure adds (boy, general)",
                "boy and general: continuous, not connected",
            ],
            "after": [
                "The tie is the weak relation and the closure is the one identity can use. Had the "
                "criterion been the tie itself, it would have said the general is not the boy and the "
                "officer is both; with the chain it says the three are one."
            ],
        },
        "quiz_title": "Ties and chains",
        "quiz": [
            {"q": "In the lab's default grid each stage remembers only the stage just before it. How many pairs does the grid hold, and is `(1, 3)`, stage 3 directly remembering stage 1, among them?",
             "a": ["Ten pairs, and yes",
                   "Four pairs, and no",
                   "Four pairs, and yes",
                   "Ten pairs, and no"],
             "c": 1,
             "why": "Each of stages 2, 3, 4 and 5 remembers one predecessor, so there are four pairs, and `(1, 3)` is not among them: stage 3 remembers stage 2 and nothing earlier. Ten is the size of the transitive closure, which the lab marks in amber without adding to the grid."},
            {"q": "In Reid's case, what is the right diagnosis of the contradiction?",
             "a": ["Memory is not a tie between stages at all",
                   "Identity is not transitive when a person forgets",
                   "The general is in fact a different person from the officer",
                   "The criterion used a relation that is not transitive where identity is"],
             "c": 3,
             "why": "The criterion was memory, and memory fails to pass through the officer. Identity is transitive by what it is, so a criterion built on a non-transitive tie cannot be identity itself. Memory remains a tie, which is why the repair keeps it, and the general's remembering the officer is part of the case, not in dispute."},
            {"q": "Which statement about the transitive closure of the lab's default grid is correct?",
             "a": ["It adds the six pairs a chain of memories supplies and removes none of the four",
                   "It replaces the four pairs by ten new ones",
                   "It adds the pair `(3, 1)` since the stages are close",
                   "It adds nothing, because the grid is already transitive"],
             "c": 0,
             "why": "The closure keeps every original pair and adds exactly those joined by a longer path, the six above the diagonal that are not next-stage pairs. Pairs run only from earlier to later, so `(3, 1)` is not added by this closure. The property table showed that the grid is not transitive, so the last choice is false."},
            {"q": "A critic says: the general and the boy share no memory, so by the chain criterion they are still not the same person. What is wrong with that?",
             "a": ["Continuity needs no direct tie between the two end stages, only a chain of ties between neighbours",
                   "The general does remember the boy after all",
                   "The chain criterion ignores memory",
                   "Two stages are always the same person if one is later than the other"],
             "c": 0,
             "why": "The criterion is continuity, the closure, and the end stages need not be tied directly. The second choice contradicts the case, and the third misdescribes the criterion, which is built from memory ties. The last would make every two stages of a life the same person, whether or not any tie joined them."},
        ],
        "mistakes": [
            ("Believing memory connects every stage of a life to every other",
             "Each stage in the lab's grid remembers one predecessor, and the grid has four pairs, not "
             "ten. The pairs `(1, 3)`, `(1, 4)` and the rest are not in it, and the property table "
             "names `(1, 2)` and `(2, 3)` as the pair of pairs whose shortcut is missing. A life is "
             "joined by overlapping memories, and the overlap is the point."),
            ("Thinking the chain criterion makes identity a matter of how many links there are",
             "Continuity does not count links. The closure marks stage 5 as continuous with stage 1 "
             "exactly as it marks stage 2, and a longer chain is no weaker as a chain. What can weaken "
             "is a link, and the lab can show it: remove row 3, column 4 and stages 1 to 3 are one "
             "chain and stages 4 and 5 are another."),
            ("Assuming the closure settles personal identity",
             "It settles Reid's contradiction, which is a contradiction about the form of the criterion. "
             "It does not decide whether a body, a brain or a story is also required, and it does not "
             "decide what to say when the chain forks. The next lesson takes the fork, and the body "
             "and the story are left to prose."),
        ],
        "standard": (
            "Finish when you can give a tie that is not transitive, build its closure, and say which stages are continuous but not connected.",
            "Given a set of pairs of stages, you should be able to name the pair of pairs whose shortcut is "
            "missing, list the pairs the transitive closure adds, and state which stages are continuous "
            "without being connected. A claim that a criterion of identity fails, made without the missing "
            "pair, has not been checked."),
        "note": "The lab shows one closure at a time, and the closure it draws for this relation is the transitive one. A relation that was also reflexive and symmetric would partition the stages into classes, one person to a class, and the lab's status line reports those classes when it finds them.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "fission-and-what-matters",
        "title": "Fission and What Matters",
        "module": "Identity over time",
        "one_line": "If one person divides into two who are each continuous with the original, four plausible claims cannot all be true, and each way of giving one up is a position.",
        "summary": (
            "Suppose each half of a brain is placed in a new body, and both survivors are continuous "
            "with the original. Continuity seems enough for survival, and identity is one-one, and the "
            "two claims cannot both hold. The consistency lab finds no model for the five sentences, "
            "shows that dropping any one restores a model, and so lists the exits."
        ),
        "key": [
            "A and B are each continuous with me",
            "continuity suffices for identity",
            "identity is one-one: not both A and B",
            "five sentences, no model; drop one, a model",
            "Parfit drops the question, not the facts",
        ],
        "key_label": "Four claims, and the case that splits them",
        "concepts_intro": (
            "The last lesson ended with a chain that runs in a line. Here the chain forks, and the method "
            "is the one “Consistency and Belief Sets” taught and “The Regress of Justification” in "
            "Knowledge and Evidence applied: write the claims as a set and ask for a model. Two later "
            "lessons in this course use it again."
        ),
        "concepts": [
            ("Fission is a case, and the claims are the problem",
             "The case is stipulated: after the division two people, A and B, are each psychologically "
             "continuous with the original person. What is in dispute is how to describe it, and the "
             "description is a set of sentences the lab can test."),
            ("The set has no model",
             "Write `ca` for &ldquo;A is continuous with me&rdquo; and `ia` for &ldquo;A is me&rdquo;, and likewise `cb` and "
             "`ib`. The claims are `ca`, `cb`, `ca → ia`, `cb → ib` and `¬(ia ∧ ib)`. No row of the "
             "truth table makes all five true."),
            ("Every exit is a deletion",
             "Drop one sentence and a model appears. Each deletion is a position that has been "
             "defended, and a reader can choose among them by what each costs."),
        ],
        "read_title": "A split in the chain",
        "read_intro": "The case, the five sentences, the models that appear when one is dropped, and the exit that changes the question.",
        "body": [
            ("p", "The case is a thought experiment, and it is stated so that nothing in it is "
                  "impossible by the laws of logic. Each half of a person's brain can sustain a mind, "
                  "and the two halves are removed and placed in two new bodies. Each of the two people "
                  "who wake is psychologically continuous with the original in every way the previous "
                  "lesson asked for: memories, intentions, character. Call them A and B."),
            ("p", "Three things are then hard to deny together. A is continuous with the original, "
                  "and B is, because that is how the case was built. Continuity is enough for "
                  "survival: if someone were connected to me by the chain I would want, that someone "
                  "is me. And identity is one-one: if A is me and B is me, then A is B, but A and B "
                  "now lead two lives and have two different bodies. Written out, with the sufficiency "
                  "claim split over the two survivors, these are five sentences."),
            ("math", [
                "1.  ca            A is continuous with me",
                "2.  cb            B is continuous with me",
                "3.  ca → ia       continuity suffices for A to be me",
                "4.  cb → ib       continuity suffices for B to be me",
                "5.  ¬(ia ∧ ib)    A and B are not both me",
            ]),
            ("p", "The lab's consistency mode, with the rows of the truth table behind it, finds no row "
                  "that makes all five true. By sentences 1 and 3, `ia` is true; by 2 and 4, `ib` is "
                  "true; sentence 5 denies their conjunction. The smallest inconsistent subset it reports is all "
                  "five, so every sentence is needed for the contradiction, and the drop menu shows "
                  "what each is worth: remove any one and a model is found."),
            ("def", ("Minimal inconsistent subset",
                     "A set of sentences with no model is <strong>minimally inconsistent</strong> when "
                     "removing any one sentence leaves a set that has a model. Every sentence of such a "
                     "set is doing work, and each is a place where the set can be repaired.")),
            ("h3", "The exits"),
            ("p", "Dropping sentence 1 or 2 denies the stipulation, and says only one survivor is truly "
                  "continuous. That changes the case instead of answering it. Dropping sentence 3 or "
                  "4 is the more interesting move. A closest-continuer theory says continuity gives "
                  "identity only when no rival is as close, so that in the case of a tie neither survivor "
                  "is me. The lab's second preset writes this as continuity suffices only when "
                  "unbranched, and the set then has a model. The theory adds that in a tie neither "
                  "survivor is me, and its price is that my survival depends on whether someone else "
                  "also exists: if only one half had taken, I would have survived, and with both I "
                  "do not."),
            ("p", "Dropping sentence 5 says both A and B are me. One version holds that there were always "
                  "two people before the division, overlapping in one body, so that the one-one claim "
                  "is true of people and false of the stages we counted as one. The cost is a count of "
                  "persons that no one made before the case arose."),
            ("p", "The exit that changes the question is Parfit's. Identity, he says, is the wrong thing "
                  "to want. What matters in survival is the relation of continuity and connectedness, "
                  "and both A and B have it in full. The third preset replaces sentences 3 and 4 by "
                  "claims that continuity gives what matters, written `ca → ma` and `cb → mb`, and "
                  "keeps the one-one claim, and the set has a model. Whether A is me is left without an "
                  "answer that matters, and it is the loss of that answer, not of a person, that "
                  "Parfit asks you to accept. Whether he is right to say that nothing is lost is the "
                  "philosophical question, and the lab, which can only test the set, leaves it open."),
        ],
        "lab": ("argkit", {
            "mode": "consistency",
            "preset": "fission",
            "presets": [
                {"id": "fission", "label": "continuity suffices, and identity is one-one",
                 "sentences": ["ca", "cb", "ca -> ia", "cb -> ib", "~(ia & ib)"],
                 "expect": {"coVerdict": "Inconsistent", "coMis": "{1, 2, 3, 4, 5}", "coWitness": "none"}},
                {"id": "no-branching", "label": "continuity suffices only when unbranched",
                 "sentences": ["ca", "cb", "(ca & ~cb) -> ia", "(cb & ~ca) -> ib", "~(ia & ib)"],
                 "expect": {"coVerdict": "Consistent", "coMis": "none", "coWitness": "ca=T cb=T ia=T ib=F"}},
                {"id": "parfit", "label": "continuity gives what matters, not identity",
                 "sentences": ["ca", "cb", "ca -> ma", "cb -> mb", "~(ia & ib)"],
                 "expect": {"coVerdict": "Consistent", "coMis": "none", "coWitness": "ca=T cb=T ia=T ib=F ma=T mb=T"}},
            ],
            "panel_title": "Drop one sentence and look for a model",
            "panel_intro": "The first set is the five sentences of the text, with a tilde for not and an arrow made of a hyphen and a greater-than sign for the conditional. Use the drop menu to remove them one at a time and read whether a model appears, and which letters it makes true. Then try the other two presets.",
        }),
        "steps_title": "Writing a puzzle of identity as a set",
        "steps_intro": "Five moves, in this order. The third is the one that is usually done by instinct.",
        "steps": [
            ("State the case as sentences",
             "Write what the thought experiment stipulates, and nothing that is merely natural to say. "
             "Here those are the two continuity claims."),
            ("Write each principle as a sentence",
             "Give the sufficiency of continuity and the one-one nature of identity their own lines. "
             "A principle left implicit is a premise nobody can reject."),
            ("Run the check for a model",
             "If the lab finds none, the set is inconsistent. Read the smallest inconsistent subset: "
             "it names the sentences that must be present for the trouble."),
            ("Delete one sentence at a time",
             "Read the model that appears each time, and say which view of identity it is."),
            ("State what each view costs",
             "A deletion is a position only when you can say what it gives up. For each exit, name "
             "a case in which the cost shows."),
        ],
        "worked": {
            "title": "The five sentences and the models that remain",
            "intro": ["Letters: `ca` and `cb` for continuity with A and B, `ia` and `ib` for being me."],
            "lines": [
                "all five: no model",
                "drop 5: ia and ib both true is allowed",
                "drop 3: ib is forced true, so ia must be false",
                "drop 4: ia is forced true, so ib must be false",
                "drop 1 or 2: one survivor is not continuous",
                "each drop leaves a model; none was avoidable",
            ],
            "after": [
                "Nothing in the table says which sentence to keep. Dropping sentence 3 leaves a model in "
                "which only B is me, and dropping sentence 4 one in which only A is, and the case was "
                "built so that nothing prefers either. A view that keeps both conditionals and "
                "yet wants a single survivor has to add a tie-break the five sentences do not contain."
            ],
        },
        "quiz_title": "Fission as an inconsistent set",
        "quiz": [
            {"q": "The lab reports the five sentences inconsistent, with {1, 2, 3, 4, 5} as the smallest inconsistent subset. What follows?",
             "a": ["Every one of the five is needed for the contradiction, so dropping any one gives a set with a model",
                   "Sentences 3 and 4 alone are the cause of the trouble",
                   "Fission cannot happen",
                   "Sentence 5 is the only one that can be rejected"],
             "c": 0,
             "why": "A minimal inconsistent subset is one from which no sentence can be removed without restoring consistency, and here that is the whole set. The second is false for that reason: 1, 2 and 5 are needed too. The set says nothing about whether the case can occur, and every sentence is a place to push, so the last is false."},
            {"q": "In the no-branching set, both survivors are continuous with me. What does the set say about whether A is me?",
             "a": ["A must be me, since A is continuous",
                   "Nothing forces A to be me and nothing forbids it; only that A and B are not both me",
                   "A cannot be me, since B is continuous too",
                   "A is me exactly when B is me, since the case is symmetric"],
             "c": 1,
             "why": "The conditionals now apply only when exactly one survivor is continuous, so with both continuous they say nothing, and the one-one sentence rules out only the case where both are me. The first and third each claim more than the sentences give. The last would make `ia` and `ib` agree, and the set forbids their both being true while permitting one without the other, as the model the lab prints, with `ia` true and `ib` false, shows; the symmetry is in the case, not in the sentences."},
            {"q": "Parfit's exit, as the third preset writes it, is best described as which move?",
             "a": ["Denying that A and B are continuous with me",
                   "Allowing that both A and B are me",
                   "Replacing the claim that continuity suffices for identity with the claim that it gives what matters",
                   "Choosing which survivor is me by a tie-break"],
             "c": 2,
             "why": "The preset keeps both continuity claims and the one-one claim, and swaps the sufficiency sentences for ones about what matters, so the set has a model. Allowing both to be me would drop the one-one sentence, which the preset keeps, and a tie-break is a different exit that the set cannot state."},
            {"q": "A reader says: the set has no model, so a person cannot divide. What is the best reply?",
             "a": ["The set is about identity, and says nothing about whether the division could happen; it shows only that the four claims cannot all be kept",
                   "A person can divide, because the lab found a model",
                   "The set is consistent if one letter is renamed",
                   "Inconsistent sets always describe possible cases"],
             "c": 0,
             "why": "An inconsistent set shows that a set of claims cannot all be true together, whatever happens in the world. Whether the division can occur is another question. The lab found no model for the full set, renaming a letter changes nothing, and an inconsistent set describes no case that could be as it says."},
        ],
        "mistakes": [
            ("Believing that one of the two survivors must be me",
             "The five sentences do not say so. In the no-branching set the lab finds a model in which "
             "neither survivor is me, and one in which exactly one is, and no sentence prefers A to B, "
             "since the case was built to be symmetric. The belief that one must be me is sentence 3 "
             "or 4 on its own, and it is the claim the case puts under strain."),
            ("Hearing Parfit as saying the survivors do not matter, or that fission is as bad as death",
             "The exit keeps both continuity claims and the claim that continuity gives what matters. "
             "On his view each survivor has what I should care about in survival, so the case is "
             "close to ordinary survival, not death. What goes is the assumption that the question "
             "whether A is me has a further answer."),
            ("Taking an inconsistent set to prove that the case is impossible",
             "The lab shows that five claims cannot all be true. A reader who holds all five has a "
             "contradiction to repair; the case, in which a person divides, is untouched by the check. "
             "Whether it can happen is a matter for biology, and the repair is a matter for you."),
        ],
        "standard": (
            "Finish when you can write the fission case as a set, name its smallest inconsistent subset, and state what each deletion yields.",
            "You should be able to write the five sentences, run the check and report that no model exists, "
            "delete each sentence in turn and say which position the model that appears represents, and "
            "state what Parfit's exit gives up. A deletion named without the model it yields has not been "
            "checked."),
        "note": "The lab searches the sentences you give it and nothing else. It cannot tell whether continuity really does suffice for survival, whether the division could happen, or whether the description of the survivors is fair; those are the premises.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "free-will-determinism-and-compatibility",
        "title": "Free Will, Determinism and Compatibility",
        "module": "Freedom",
        "one_line": "Determinism, free will and the claim that they exclude each other cannot all be true, and each of the three standard positions deletes a different one.",
        "summary": (
            "Hard determinism, libertarianism and compatibilism are usually presented as rival answers. "
            "Written as a set of three sentences they are the three ways to delete one, and the "
            "consistency lab shows the set has no model. It also shows that a compatibilist set is "
            "consistent while keeping determinism, because it defines free will differently."
        ),
        "key": [
            "d: determinism   f: free will",
            "incompatibilism: d → ¬f",
            "{d, f, d → ¬f}: no model",
            "drop f, d, or the conditional: a model",
            "compatibilism keeps d, and changes what f is",
        ],
        "key_label": "Three claims, three deletions",
        "concepts_intro": (
            "The last lesson was a consistency check on a puzzle about identity. The same "
            "check applies to the oldest of the freedom debates, and its first result is a map of the "
            "positions."),
        "concepts": [
            ("The triad is a set of three sentences",
             "Let `d` say that determinism is true, `f` that people act freely, and `d → ¬f` that "
             "determinism rules out free action. Together they have no model, since `d` and `d → ¬f` "
             "give `¬f`, which contradicts `f`."),
            ("The three positions are the three deletions",
             "Hard determinism keeps `d` and the conditional and drops `f`. Libertarianism keeps `f` "
             "and the conditional and drops `d`. Compatibilism keeps `d` and `f` and drops the "
             "conditional, which is what the word &ldquo;compatible&rdquo; says."),
            ("What f means decides which sets are consistent",
             "A compatibilist does not only reject the conditional. The compatibilist gives `f` a "
             "different meaning, for instance acting on one's own desires, and under that meaning "
             "the conditional no longer connects the two claims."),
        ],
        "read_title": "The triad and its exits",
        "read_intro": "The claims, the set that has no model, the models that appear on each deletion, and the definition on which compatibilism turns.",
        "body": [
            ("def", ("Determinism",
                     "<strong>Determinism</strong> is the thesis that the state of the world at one time, "
                     "together with the laws of nature, entails the state at every later time. It is a thesis "
                     "about entailment, and it says nothing of compulsion or of what anyone feels.")),
            ("p", "Take free will in its ordinary sense: when I raise my hand it is up to me, and I could "
                  "have kept it down. The old worry is that these two do not fit. If the past and the laws "
                  "entail everything that happens, then my raising my hand was already entailed, and it "
                  "does not look as if it was up to me. Write the worry as a conditional, and put it beside "
                  "the two claims it threatens."),
            ("math", [
                "1.  d            determinism is true",
                "2.  f            some people act freely",
                "3.  d → ¬f       if determinism is true, no one acts freely",
            ]),
            ("p", "Sentence 3 is <strong>incompatibilism</strong>, and it is the one in dispute. The "
                  "lab finds no model for the three: from 1 and 3 comes `¬f`, and sentence 2 is `f`. "
                  "It reports the smallest inconsistent subset as the whole set, so every sentence "
                  "has to be present for the clash, and each is a place to give way."),
            ("p", "Three places, three positions. The <strong>hard determinist</strong> drops sentence 2 "
                  "and accepts that no one acts freely. The <strong>libertarian</strong> drops sentence 1 and "
                  "holds that some choices are not entailed by the past and the laws. The "
                  "<strong>compatibilist</strong> drops sentence 3. Each position can be stated at its "
                  "strongest, and each pays: the first gives up the practice of praise and blame, or has to "
                  "reinterpret it; the second needs causes that are not entailed, which the physics may or "
                  "may not supply; and the third has to say what freedom is, given that it is not "
                  "the ability to do otherwise whatever the past."),
            ("h3", "What drops the conditional"),
            ("p", "The compatibilist cannot simply deny sentence 3. The conditional is plausible on a "
                  "reading of `f`, and that reading is what the compatibilist rejects. Suppose free "
                  "will is acting on one's own desires, without constraint. Write `a` for &ldquo;the "
                  "person acts on her own desires&rdquo; and `o` for &ldquo;she could have done otherwise "
                  "whatever the past&rdquo;. The compatibilist set is `d`, `f`, `f ↔ a` and "
                  "`d → ¬o`, which says that determinism rules out the strong ability and keeps "
                  "free will as acting on desires."),
            ("p", "The lab finds a model for it, and the model makes `d` true and `f` true. The "
                  "misreading of the position is the thought that compatibilism needs determinism to be "
                  "false somewhere. It needs no such thing: the compatibilist holds both claims at once, "
                  "which is why the position is called what it is."),
            ("p", "The cost is on the other side of the biconditional. If the incompatibilist insists that "
                  "free will does require the ability to do otherwise whatever the past, the sentence "
                  "`f ↔ o` replaces `f ↔ a`, and with `d → ¬o` the set is inconsistent again. The lab "
                  "shows the clash is back, and it shows that the dispute has moved from the logic to "
                  "the meaning of `f`. A consistent set does not tell you that the compatibilist's "
                  "`a` is the freedom anyone wanted. It tells you that the position is coherent."),
            ("p", "The lab has one limit that matters here. It treats `d`, `f`, `a` and `o` as unanalysed "
                  "claims, and it cannot tell you whether determinism is true or what freedom is. "
                  "It checks the sentences you chose."),
        ],
        "lab": ("argkit", {
            "mode": "consistency",
            "preset": "triad",
            "presets": [
                {"id": "triad", "label": "determinism, free will, and their incompatibility",
                 "sentences": ["d", "f", "d -> ~f"], "expect": {"coVerdict": "Inconsistent", "coMis": "{1, 2, 3}", "coWitness": "none"}},
                {"id": "compatibilist", "label": "free will is acting on one's desires",
                 "sentences": ["d", "f", "f <-> a", "d -> ~o"], "expect": {"coVerdict": "Consistent", "coMis": "none", "coWitness": "a=T d=T f=T o=F"}},
                {"id": "incompatibilist-meaning", "label": "free will requires doing otherwise",
                 "sentences": ["d", "f", "f <-> o", "d -> ~o"], "expect": {"coVerdict": "Inconsistent", "coMis": "{1, 2, 3, 4}", "coWitness": "none"}},
                {"id": "libertarian", "label": "free will requires doing otherwise, and determinism is false",
                 "sentences": ["~d", "f", "f <-> o", "d -> ~o"], "expect": {"coVerdict": "Consistent", "coMis": "none", "coWitness": "d=F f=T o=T"}},
            ],
            "panel_title": "Delete one claim, or change what f means",
            "panel_intro": "The first set is the triad. Use the drop menu to delete each claim in turn and read the model: hard determinism, libertarianism and compatibilism are the three that appear. Then select the second set, where free will is defined as acting on one's own desires, and read the model that keeps determinism. The third set gives free will the other definition and brings the clash back.",
        }),
        "steps_title": "Mapping a debate by its inconsistent set",
        "steps_intro": "Five moves for any question that offers a few claims and says they conflict.",
        "steps": [
            ("Write the claims, including the one that says they conflict",
             "The conflict is itself a sentence. Write the bridge as a conditional, as with `d → ¬f`, "
             "and not as a remark."),
            ("Ask for a model",
             "If the lab finds one, the claims do not conflict as written. If it finds none, "
             "read the smallest inconsistent subset."),
            ("Delete each sentence once",
             "The model that appears each time is a position. Name it, and name who holds it."),
            ("Look at the letters, not only the sentences",
             "Ask what each letter means. If a position works by giving a letter a different meaning, "
             "add the defining sentence to the set, as with `f ↔ a`, and test again."),
            ("Say what each position pays",
             "A position is not defended by being consistent. State the cost it accepts, and decide "
             "whether you are willing to pay it."),
        ],
        "worked": {
            "title": "One table, three positions",
            "intro": ["The triad `d`, `f`, `d → ¬f`, with each sentence dropped in turn."],
            "lines": [
                "all three: no model",
                "drop 2, f: d true, f false",
                "drop 1, d: d false, f true",
                "drop 3, the conditional: d true, f true",
                "drop 2 is hard determinism",
                "drop 1 is libertarianism; drop 3, compatibilism",
            ],
            "after": [
                "Each model is the position's picture of the world, and none is argued for by the table. "
                "The second preset keeps the conditional for the strong ability `o` and changes what "
                "free will is, so the set has a model and `d` remains true in it."
            ],
        },
        "quiz_title": "Positions as deletions",
        "quiz": [
            {"q": "In the triad `d`, `f`, `d → ¬f`, which sentence does the compatibilist drop?",
             "a": ["`d`, because determinism is false",
                   "`f`, because no one is free",
                   "`d → ¬f`, because determinism does not rule out free action",
                   "None, because the set is consistent"],
             "c": 2,
             "why": "Keeping `d` and `f` leaves only the conditional to give up. Dropping `d` is the libertarian's move and dropping `f` the hard determinist's. The set has no model, so the last choice is false."},
            {"q": "In the compatibilist preset, the lab finds a model. What does the model make true?",
             "a": ["`d` false and `f` true",
                   "`d` true and `f` true",
                   "`d` true and `f` false",
                   "`d` false and `f` false"],
             "c": 1,
             "why": "The set contains `d`, so every model makes determinism true, and `f` is true because the set contains it. So the position does not deny determinism. The first and fourth contradict the sentence `d`, and the third contradicts `f`."},
            {"q": "Which change brings the clash back when the compatibilist's `f ↔ a` is replaced by `f ↔ o`?",
             "a": ["Free will now requires the ability to do otherwise, and `d → ¬o` says determinism excludes it",
                   "The letter `a` is no longer in the set",
                   "The set now has more sentences",
                   "Determinism has become false"],
             "c": 0,
             "why": "From `d` and `d → ¬o` comes `¬o`, and with `f ↔ o` and `f` that gives `o`. The set is inconsistent for that reason. The number of sentences and the letter `a` are irrelevant to the clash, and `d` is still in the set, so determinism is still asserted."},
            {"q": "What does the lab's finding of a model for the compatibilist set establish?",
             "a": ["That the set is coherent, and says nothing yet about whether acting on desires is the freedom worth wanting",
                   "That determinism is true",
                   "That people act freely",
                   "That the incompatibilist is mistaken"],
             "c": 0,
             "why": "A model shows the sentences can all be true together. It does not make any of them true, so it neither establishes determinism nor free will, and it does not settle the dispute with the incompatibilist, who denies that `a` is what `f` means."},
        ],
        "mistakes": [
            ("Thinking compatibilism denies determinism",
             "The sentence `d` is in the compatibilist set, and the lab's model makes it true: "
             "determinism and free will are both true in it. What the compatibilist denies is the "
             "conditional between them, once free will is understood as acting on one's own desires. "
             "The position is called compatibilism because it claims the two are compatible, and "
             "determinism is the thing that is kept."),
            ("Treating a determined act as a compelled act",
             "Determinism is a thesis that the past and the laws entail what happens. Compulsion is a "
             "fact about a particular act, such as one made under threat or against one's own desires. "
             "The compatibilist's `a` is exactly what compulsion removes, so an act can be determined "
             "and uncompelled, and a person acting on a compulsion is not free under any of the "
             "definitions in the lab."),
            ("Believing consistency is a win for the compatibilist",
             "A set with a model shows only that the position is coherent. The incompatibilist's "
             "reply is that `f ↔ a` has changed the subject, and the third preset shows what the "
             "reply is: give `f` the other meaning and the clash returns. The argument is about "
             "which meaning of `f` is the one that matters for praise, blame and choice."),
        ],
        "standard": (
            "Finish when you can write the triad, name the three positions as deletions, and show how a definition of free will changes the verdict.",
            "You should be able to state the three sentences, report the verdict and the smallest "
            "inconsistent subset, give the model that appears on each deletion, and show with a defining "
            "sentence how a compatibilist definition of free will makes the set consistent. A position "
            "named without the sentence it drops has not been placed."),
        "note": "The next lesson turns to the argument that gives the conditional its best support, and it is the strongest case an incompatibilist can offer.",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "the-consequence-argument",
        "title": "The Consequence Argument",
        "module": "Freedom",
        "one_line": "The consequence argument for incompatibilism is valid because its transfer step is the K axiom, so the dispute is over its two premises and over the reading of its box.",
        "summary": (
            "If determinism is true, our acts are the consequences of the laws and the remote past, and "
            "no one has power over those. Reading &ldquo;no one has power over&rdquo; as a box, the step that carries "
            "unavoidability across a consequence is the K axiom, valid on every frame the reader can "
            "draw. The kripke lab checks it and then lets you falsify each premise in a model."
        ),
        "key": [
            "N p: p, and no one has power over p",
            "box reading: p at every world left open",
            "□p ∧ □(p → q) → □q   valid on every frame",
            "premise one: the past and laws are fixed",
            "premise two: determinism makes the act follow",
        ],
        "key_label": "Powerlessness passes across a consequence",
        "concepts_intro": (
            "The previous lesson left the incompatibilist's conditional unsupported. This one gives it "
            "its best support, an argument whose logic can be checked, and shows where the checking stops."
        ),
        "concepts": [
            ("No one has power over p is a box",
             "Read a world that `w` sees as a way things could still go, given what anyone can do at "
             "`w`. Then `□p` says that `p` holds in every such way: no one can make it false. "
             "The kripke lab computes this box exactly as before."),
            ("The transfer step is K",
             "If no one has power over `p`, and none over the fact that `p` leads to `q`, then none "
             "over `q`. That is `□p ∧ □(p → q) → □q`, the axiom called K, and the lab finds it valid on "
             "every frame."),
            ("What is left is the premises and the reading",
             "A valid argument leaves you its premises to examine. Here there are two, and a third "
             "thing to examine: whether &ldquo;has no power over&rdquo; is the sort of operator the box "
             "computes."),
        ],
        "read_title": "A valid transfer, and where to push",
        "read_intro": "The argument as its defender states it, the check that its logic is K, and the three places a reader can push.",
        "body": [
            ("p", "Let `h` be the state of the world long before anyone was born, `l` the laws of "
                  "nature, and `a` some act of mine tomorrow. Suppose determinism is true: "
                  "the remote past and the laws entail the act. The argument then runs in three lines. "
                  "Nobody has any power over the remote past and the laws, since they were fixed "
                  "before anyone could act. Nobody has any power over the fact that the past and "
                  "the laws entail the act, since that is a matter of what the laws are. So nobody has "
                  "any power over the act. If I have no power over my acts, I do not act freely."),
            ("p", "Write `N` for &ldquo;and no one has, or ever had, any power over whether&rdquo;. The "
                  "premises are `N(h ∧ l)` and `N((h ∧ l) → a)`, and the "
                  "conclusion is `N a`. The step from the premises to the conclusion is an instance of "
                  "one rule: from `N p` and `N(p → q)`, conclude `N q`. Peter van Inwagen called it "
                  "the transfer of powerlessness. Since `N p` says `p` among other things, a frame that "
                  "models `N` has each world seeing itself, and the presets that evaluate a premise give "
                  "w1 that arc; the transfer step, as the next paragraph shows, needs no arc at all."),
            ("p", "The lab's box is `N` when the arcs are read as described: world `w` sees a "
                  "world when that world is still open, given what anyone can do. The transfer rule is "
                  "then the formula in the key, and the lab can test it. Take any frame at all; the "
                  "reason it holds is short. If `p` holds at every world seen from `w`, and `p → q` "
                  "does too, then at each seen world `p` is true and `p → q` is true, so `q` is "
                  "true, and `q` holds at every seen world. Nothing was assumed about the arcs."),
            ("thm", ("The transfer rule is valid on every frame",
                     "For every frame, every valuation and every world, `□p ∧ □(p → q) → □q` is true. "
                     "The lab's first preset evaluates it at every world of a three-world frame and "
                     "finds it true at all of them, and changing the arcs or the valuation does not "
                     "change that.")),
            ("p", "So the argument is valid, given the reading of its box. A reader who wants to resist "
                  "the conclusion has three choices, and the lab can model each. The first is to deny "
                  "that the past and laws are beyond everyone's power. On David Lewis's compatibilism, "
                  "had I done otherwise, a small miracle would have broken the laws shortly before. "
                  "I cannot cause that miracle, but I can act in a way such that, were I to act "
                  "so, it would have occurred, and that is a power over the laws of the "
                  "relevant kind. In the second preset, w1 sees a world where the laws fail, and "
                  "`□(h ∧ l)` is false at w1. This is the compatibilist's move."),
            ("p", "The second choice is to deny that the past and the laws entail the act: to deny "
                  "determinism. In the third preset the seen worlds all keep the past and the laws, "
                  "and in one of them the act does not occur. Then `□((h ∧ l) → a)` is false at w1. "
                  "This is the libertarian's move. The fourth preset shows both premises true and "
                  "the conclusion true with them, as the validity of the step promises."),
            ("h3", "The third place to push"),
            ("p", "The last choice is not about either premise. It is to say that &ldquo;no one has power "
                  "over&rdquo; does not behave as the box does. Every box satisfies agglomeration: from "
                  "`□p` and `□q` comes `□(p ∧ q)`, since a world where each holds at every seen world is "
                  "one where the conjunction does. The operator `N` has been argued not to. A coin I "
                  "could toss lies untossed. I have no power over whether it fails to land heads, since "
                  "even tossing it cannot make it land heads; I have none over whether it fails to land "
                  "tails, for the same reason; but I have power over whether it fails to do both, since "
                  "tossing it would make one of them happen. If that is right, `N` fails agglomeration, "
                  "no box does, and the transfer step is not an instance of K, because the operator is "
                  "not a box; the lab's verdict does not apply. The argument's defender has replied by "
                  "redefining `N` so that it is a box after all, as truth throughout every region of "
                  "possibility anyone can reach, and then the two premises have to be argued for under "
                  "that definition."),
            ("p", "This answers the objection that the logic can be denied. K cannot be denied for a box. "
                  "What can be denied is that the operator in the argument is a box, and that is a "
                  "claim about the premises' meaning, not about the logic of necessity. The lab shows "
                  "the logic is secure and is silent on whether the argument has the logic's shape."),
        ],
        "lab": ("argkit", {
            "mode": "kripke",
            "at": 1,
            "reading": "alethic",
            "preset": "transfer",
            "presets": [
                {"id": "transfer", "label": "the transfer step, on a frame with a fork",
                 "n": 3, "access": [[1, 2], [1, 3], [2, 3], [3, 3]], "valuation": {"p": [2, 3], "q": [2, 3]},
                 "formula": "([]p & [](p -> q)) -> []q", "expect": {"krValue": "True at w1", "krWorlds": "all"}},
                {"id": "premise-one", "label": "a seen world where the laws fail",
                 "n": 3, "access": [[1, 1], [1, 2], [1, 3]],
                 "valuation": {"h": [1, 2, 3], "l": [1, 2], "a": [1, 2]},
                 "formula": "[](h & l)", "expect": {"krValue": "False at w1", "krWorlds": "w2, w3"}},
                {"id": "premise-two", "label": "a seen world where the act does not follow",
                 "n": 3, "access": [[1, 1], [1, 2], [1, 3]],
                 "valuation": {"h": [1, 2, 3], "l": [1, 2, 3], "a": [1, 2]},
                 "formula": "[]((h & l) -> a)", "expect": {"krValue": "False at w1", "krWorlds": "w2, w3"}},
                {"id": "both-hold", "label": "both premises true, and the conclusion with them",
                 "n": 2, "access": [[1, 1], [1, 2]],
                 "valuation": {"h": [1, 2], "l": [1, 2], "a": [1, 2]},
                 "formula": "([](h & l) & []((h & l) -> a)) -> []a", "expect": {"krValue": "True at w1", "krWorlds": "all"}},
            ],
            "panel_title": "Test the transfer step, then break a premise",
            "panel_intro": "In every model, the worlds a world sees are the ways things are still open to anyone, and in the three premise models w1 is the actual world, sees itself, and has the act occur. The first formula is the transfer step; edit the arcs and the valuation however you like and watch it stay true at every world. The second and third presets evaluate one premise each at w1. The fourth evaluates the whole argument, and the worlds tile says where it holds.",
        }),
        "steps_title": "Testing an argument that transfers a modal property",
        "steps_intro": "Five moves for any argument of the form: this is beyond control, that follows from it, so that is too.",
        "steps": [
            ("Name the operator and what the arcs mean",
             "Say what the box stands for here and what it is for one world to see another. The "
             "reading is part of the argument, and the lab cannot supply it."),
            ("Put the argument in the form of the transfer rule",
             "Write the first premise as `□p`, the second as `□(p → q)` and the conclusion as `□q`. "
             "If the argument does not have that shape, K does not apply."),
            ("Test the rule on a frame of your own",
             "Build a frame, type the formula and read the worlds tile. It is valid on every frame, "
             "so any frame will do; a failure would show a mistake in the typing."),
            ("Falsify each premise in a model",
             "Draw the smallest model in which the first premise is false and the smallest in which "
             "the second is. Each model is a view of the world, and each has a holder."),
            ("Ask whether the operator is a box",
             "If the reader's `has no power over` fails to combine as a box does, the argument "
             "has lost its logic. Say which instance of the rule fails, with a case."),
        ],
        "worked": {
            "title": "Both premises and the conclusion, at w1",
            "intro": ["Two worlds. World w1 sees itself and w2. The past and laws hold in both, and the act occurs in both."],
            "lines": [
                "h and l at w1 and at w2: true",
                "so box of (h and l) at w1: true",
                "(h and l) implies a at w1 and at w2: true",
                "so box of ((h and l) implies a) at w1: true",
                "a at w1 and at w2: true, so box of a at w1: true",
                "the act is beyond power, as the argument said",
                "now add a seen world w3 without the act",
                "box of ((h and l) implies a) at w1 fails",
            ],
            "after": [
                "The conclusion followed from the premises, as the rule says it must. The last two "
                "lines show a model in which a premise fails, and in it the conclusion fails too. "
                "That is a libertarian's picture, and the lab does not say it is the right one."
            ],
        },
        "quiz_title": "Powerlessness across a consequence",
        "quiz": [
            {"q": "What does the lab report for the transfer step, `□p ∧ □(p → q) → □q`, at every world of any frame you build?",
             "a": ["True only on reflexive frames",
                   "True only when p is true at w1",
                   "True on every frame, at every world, for every valuation",
                   "False on frames in which a world sees nothing"],
             "c": 2,
             "why": "The formula is the K axiom, valid on every frame. It does not need the world to see itself, and it does not need p to hold anywhere. At a world that sees nothing the consequent `□q` is vacuously true, so the formula holds there too."},
            {"q": "A philosopher says that if I were to raise my hand, a small violation of the laws would have occurred earlier. Which part of the argument does this deny?",
             "a": ["The second premise, that the past and laws entail the act",
                   "The first premise, that the past and the laws are beyond anyone's power",
                   "The transfer rule",
                   "The conclusion, but not any premise"],
             "c": 1,
             "why": "If I can act so that the laws would have differed, then I have power over the laws, and `□(h ∧ l)` fails. The entailment in the second premise is untouched, since the same laws are being used to say what would have happened. The rule is valid on every frame, and denying a conclusion with no premise to point to is not a response."},
            {"q": "How does the libertarian answer the argument?",
             "a": ["By denying that the transfer rule is valid",
                   "By denying that the past and the laws entail the act, so the second premise fails",
                   "By accepting both premises and denying the conclusion",
                   "By denying that anyone has power over the remote past"],
             "c": 1,
             "why": "The libertarian denies determinism for some choices, so the entailment from the past and laws to the act, the second premise, is false there. Denying the rule or accepting both premises with a denied conclusion would be invalid on any frame, and the last choice grants the first premise, which the libertarian can keep."},
            {"q": "What is the one way left to resist the argument without denying either premise?",
             "a": ["To say that the lab found K invalid",
                   "To say that K is valid on every frame, so the argument is sound",
                   "To say that no one has power over p is not a box, so the transfer step is not an instance of K",
                   "To say that the argument is circular"],
             "c": 2,
             "why": "If the operator does not behave as a box, the step is not an instance of the axiom, and the lab's verdict does not touch it. The first choice is false of the lab, the second does not follow, since validity does not give soundness, and the fourth is not shown by anything the lab computes."},
        ],
        "mistakes": [
            ("Believing the consequence argument can be escaped by denying its logic",
             "The transfer rule is K, and the lab finds it true at every world of every frame, "
             "however the arcs and atoms are changed. A reader who wants to resist has to deny a "
             "premise or deny that the operator is a box, and these are claims about the world "
             "and about the argument's reading, not about the logic of the box."),
            ("Taking the validity of the transfer step to show that the premises are true",
             "The lab's fourth preset has both premises true because they were typed in as true. "
             "The second and third make one false. In each model the step is valid, and the models "
             "differ in what the world is like. Whether the past and laws are beyond everyone's "
             "power, and whether the laws entail the act, are what the dispute is about."),
            ("Drawing the arcs of N to every world there is",
             "If w1 sees every logically possible world, it sees worlds with another past and other "
             "laws, `□(h ∧ l)` is false at w1, and the argument is lost at its first premise before "
             "anyone has argued against it. The arcs of `N` are narrower: w1 sees a world when "
             "someone at w1 could still bring it about. Under that reading the first premise says "
             "that no one can bring about a different past or different laws, which is the claim "
             "Lewis's compatibilist contests, and the lab draws whichever arcs you give it."),
        ],
        "standard": (
            "Finish when you can show that the transfer step is valid on every frame, and name the premise or the reading each response rejects.",
            "You should be able to write the argument as a box over two premises and a conclusion, test "
            "the transfer rule on a frame you built, draw a model in which each premise fails, and "
            "state which position the model represents. A response that says only that the argument is "
            "&ldquo;question-begging&rdquo; has not located the premise."),
        "note": "Worlds w2 and w3 see nothing in the models of the second and third presets, so a box is vacuously true there, and the verdict to read is the one at w1. The lab computes with whichever arcs you give it. It cannot say that the past is fixed, that the laws fix the act, or that the arcs you drew are the ways things are still open to anyone; the argument turns on those.",
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "frankfurt-cases-and-the-ability-to-do-otherwise",
        "title": "Frankfurt Cases and the Ability to Do Otherwise",
        "module": "Freedom",
        "one_line": "A counterfactual intervener removes the agent's ability to do otherwise and leaves the agent's decision as the cause of the act, which tells against the claim that responsibility needs that ability.",
        "summary": (
            "Black will make Jones act if Jones does not decide to, and Jones decides on his own. Jones "
            "could not have done otherwise, and yet his decision produced the act. The structural lab "
            "shows the decision is not a but-for cause of the act, and is a cause once Black's "
            "inaction is held fixed, and that is the case against the principle of alternate possibilities."
        ),
        "key": [
            "PAP: responsible only if could do otherwise",
            "B = ¬D: Black acts if Jones does not decide",
            "A = D ∨ B: the act follows either",
            "flip D alone: A stays 1, not but-for",
            "hold B at 0, flip D: A is 0, a cause",
        ],
        "key_label": "Could not have done otherwise, and still the cause",
        "concepts_intro": (
            "The previous lesson granted the incompatibilist a valid argument whose conclusion is that "
            "no one can do otherwise. This one asks whether responsibility needed that ability at all."),
        "concepts": [
            ("The principle of alternate possibilities",
             "Call it PAP: a person is morally responsible for an act only if the person could have done "
             "otherwise. It is the premise that connects an inability to the loss of responsibility, and "
             "it seems obvious until a case is built to separate the two."),
            ("A counterfactual intervener",
             "Black is ready to make Jones perform the act if Jones does not decide to. He never has to. "
             "Jones decides on his own, and the act follows. Black's readiness removes the alternative "
             "and takes no part in what actually happens."),
            ("Two tests of cause give two answers",
             "The but-for test asks whether flipping the decision alone changes the act, and the answer "
             "is no. The holding-fixed test holds Black's inaction at its actual value and then flips "
             "the decision, and the answer is yes. The lab runs both."),
        ],
        "read_title": "A model of the case",
        "read_intro": "Three equations, the two tests, what they show, and the objection that Black has been described too kindly.",
        "body": [
            ("p", "The principle of alternate possibilities has a long history of seeming obvious. If "
                  "I could not have done otherwise, then what I did was not up to me, and it is hard "
                  "to blame someone for what was not up to them. Harry Frankfurt built a case in which "
                  "the first condition is false and the verdict about blame does not seem to follow."),
            ("p", "Jones is deciding whether to shoot someone. Black wants him to, and has arranged "
                  "things so that if Jones shows any sign of deciding not to, Black will bring about "
                  "the decision and the act in Jones by a device. Jones does not show such a sign. He "
                  "decides for his own reasons, and shoots. Black does nothing. Had Jones wavered, "
                  "Black would have acted, so Jones could not have done otherwise."),
            ("p", "Build the model with three variables. `D` says Jones decides to shoot, and is a "
                  "given, true. `B` says Black acts, and Black acts exactly when Jones does not "
                  "decide. `A` says the shooting occurs, and it occurs if either Jones decides or "
                  "Black acts."),
            ("math", [
                "D = 1                 Jones decides",
                "B = ¬D                Black acts only if Jones does not decide",
                "A = D ∨ B             the shooting occurs either way",
            ]),
            ("p", "At the actual values, `D` is 1, `B` is 0 and `A` is 1. Now run the but-for test of "
                  "“Counterfactual Causation and the But-For Test” in Science, Induction and Causation. Flip `D` "
                  "to 0. Then `B` becomes 1, because Black acts, and `A` is still 1. Flipping Jones's "
                  "decision alone leaves the act in place, so the decision is not a but-for cause of the "
                  "act. That is the formal content of &ldquo;Jones could not have done otherwise&rdquo;."),
            ("def", ("Holding a variable fixed",
                     "To test whether `D` is a cause once Black's inaction is held fixed, set `B` at its "
                     "actual value, 0, and flip `D` with `B` kept there. If the act then changes, `D` "
                     "is a cause <strong>holding `B` fixed</strong>, and `B` is the witness.")),
            ("p", "Hold `B` at 0 and flip `D` to 0. Now `A = D ∨ B` is 0 ∨ 0, which is 0. The act does "
                  "not occur. With Black's inaction fixed, the act depends on Jones's decision, and the "
                  "lab reports `D` as a cause holding `B` fixed. This is the structure of preemption: "
                  "Black is a backup that was never used, and a backup never used does not take the "
                  "credit from the decision that did the work."),
            ("p", "Frankfurt's conclusion is that Jones is responsible for the shooting, though he could "
                  "not have done otherwise, because the act issued from his own decision in the actual "
                  "sequence of events, and Black played no part in it. If so, PAP is false. The "
                  "ability to do otherwise was never what grounded responsibility; the actual "
                  "source of the act was."),
            ("h3", "Has Black been described too kindly?"),
            ("p", "The case has been pressed hard. One reply says that Black must read some sign "
                  "to know whether to act, and that the agent could have shown the sign or not, a "
                  "small alternative that is enough for responsibility. Another says that if the "
                  "sign reliably predicts a decision that Jones has not yet made, then determinism "
                  "has been assumed about Jones's choice, and the case begs the question against "
                  "the libertarian who denies it. The model leaves both open. Its equation `B = ¬D` "
                  "gives Black a perfect reader, which is exactly what the objections dispute."),
            ("p", "Two further points. The case does not make anyone free in the sense of the previous "
                  "lesson, since it grants that Jones cannot do otherwise. A philosopher can hold "
                  "that determinism removes the ability to do otherwise, as the consequence argument "
                  "says, and still hold that this does not remove responsibility. The position is "
                  "called semi-compatibilism. Second, the lab computes a verdict about causes in the "
                  "model, and whether the model fairly describes Jones is the question the case turns on."),
        ],
        "lab": ("argkit", {
            "mode": "structural",
            "preset": "frankfurt",
            "presets": [
                {"id": "frankfurt", "label": "Black acts only if Jones does not decide",
                 "equations": {"B": "~D", "A": "D | B"}, "exogenous": {"D": 1},
                 "cause": "D", "effect": "A", "expect": {"stActual": "A = 1", "stButFor": "No", "stHP": "Yes, holding {B}", "stKind": "cause (holding fixed)"}},
                {"id": "no-intervener", "label": "no Black: the act follows the decision",
                 "equations": {"A": "D"}, "exogenous": {"D": 1},
                 "cause": "D", "effect": "A", "expect": {"stActual": "A = 1", "stButFor": "Yes", "stKind": "but-for cause"}},
                {"id": "intervener-acts", "label": "Jones does not decide, and Black acts",
                 "equations": {"B": "~D", "A": "D | B"}, "exogenous": {"D": 0},
                 "cause": "B", "effect": "A", "expect": {"stActual": "A = 1", "stButFor": "Yes", "stKind": "but-for cause"}},
            ],
            "panel_title": "Flip the decision, then hold Black's inaction",
            "panel_intro": "The table has three columns: the actual values, the values after the cause is flipped, and the values after it is flipped with the witness held at its actual value. In the first model, change the cause menu from D to B to see what Black is. In the third, Jones does not decide and Black acts, and the cause to test is Black.",
        }),
        "steps_title": "Testing responsibility without alternatives",
        "steps_intro": "Five moves for any case built to remove the ability to do otherwise.",
        "steps": [
            ("Name the decision, the backup and the act",
             "In a Frankfurt case there are three: what the agent decides, what the intervener would "
             "do, and what happens. Give each a variable."),
            ("Write the backup as a conditional on the decision",
             "The intervener acts only if the agent does not. That is `B = ¬D`, and it is the sentence "
             "that takes away the alternative."),
            ("Run the but-for test",
             "Flip the decision alone and recompute. If the act survives, the agent could not have "
             "done otherwise, in the model's sense."),
            ("Hold the backup at its actual value and flip again",
             "If the act now changes, the decision is a cause holding the backup fixed, and the "
             "intervener, who did nothing, has not displaced it."),
            ("Ask whether the model is fair",
             "Check what the intervener reads, and whether the reading assumes the agent's choice is "
             "settled in advance. If it does, the case may beg the question."),
        ],
        "worked": {
            "title": "Jones, Black and the shooting",
            "intro": ["Jones decides. Black acts only if Jones does not. The act occurs if either does."],
            "lines": [
                "actual: D = 1, B = 0, A = 1",
                "flip D to 0: B becomes 1, A = 0 or 1 = 1",
                "flipping D alone leaves A at 1: not but-for",
                "hold B at 0, flip D to 0: A = 0 or 0 = 0",
                "holding B fixed, D flips A: D is a cause",
                "Jones could not do otherwise; he is still the cause",
            ],
            "after": [
                "The two tests disagree, and that is the point of the case. The but-for test records the "
                "absence of an alternative. The holding-fixed test records where the act came from. The "
                "dispute is about which of the two grounds responsibility."
            ],
        },
        "quiz_title": "Alternatives and causes",
        "quiz": [
            {"q": "In the Frankfurt model, what happens to the act `A` when `D` alone is flipped to 0?",
             "a": ["`A` becomes 0, because Jones no longer decides",
                   "`A` is undefined, because Black has not acted",
                   "`A` becomes 0, because Black does nothing",
                   "`A` stays 1, because Black's device then acts"],
             "c": 3,
             "why": "Flipping `D` makes `B = ¬D` equal 1, and `A = D ∨ B` is then 1. So the act survives. The first and third treat Black as inert, which is what holding `B` fixed does, and not what the but-for flip does. Every variable has a value in the model."},
            {"q": "Holding `B` at 0 and flipping `D` to 0 changes `A` to 0. What does this show?",
             "a": ["That Black could have acted",
                   "That Jones could have done otherwise",
                   "That Jones's decision is a cause of the act once Black's inaction is held fixed",
                   "That the but-for test was wrong"],
             "c": 2,
             "why": "With Black's actual inaction held, the act depends on the decision, so the decision is a cause. It does not show that Jones could have done otherwise, since the unheld flip left `A` at 1. Black's ability is already given. The but-for test answered a different question correctly."},
            {"q": "If the Frankfurt case is a fair description, what follows about PAP?",
             "a": ["That Jones was free to do otherwise",
                   "That responsibility does not require the ability to do otherwise",
                   "That determinism is false",
                   "That Black is responsible for the act"],
             "c": 1,
             "why": "The case is built to give a responsible agent without alternatives, so if it is fair, the principle that responsibility requires alternatives is false. It grants that Jones could not do otherwise. The case does not mention determinism, and Black did not act."},
            {"q": "In the no-intervener preset, what does the lab report for the cause `D` of the act?",
             "a": ["A cause holding something fixed, with Black as the witness",
                   "A but-for cause",
                   "Not a cause",
                   "A joint cause with Black"],
             "c": 1,
             "why": "With no Black the act is `A = D`. Flipping `D` flips `A`, so the decision is a but-for cause, which is the ordinary case where the agent could have done otherwise. There is no Black to be a witness or a partner, and there is nothing to hold fixed."},
        ],
        "mistakes": [
            ("Thinking responsibility requires that the agent could have done otherwise",
             "In the model Jones cannot: flipping his decision leaves the act at 1, because Black's "
             "device takes over. Yet with Black's actual inaction held fixed, flipping the decision "
             "flips the act, so the decision is the cause of the shooting. The belief that "
             "responsibility needs an alternative has a counterexample if the case is fair."),
            ("Thinking Black's presence makes Jones's decision irrelevant to the act",
             "Black is a backup that was not used. The act came about through `D`, and the lab "
             "reports `D` as a cause holding `B` fixed. A spare tyre in the boot does not take over from "
             "the tyre that carried the car, and the structure is the preemption of the earlier course."),
            ("Treating the case as a proof that people are free or responsible",
             "The case argues against one premise, PAP. It assumes that Jones is responsible and "
             "that Black has been described fairly, and a reader who denies either is not refuted "
             "by the lab. Whether a deterministic world removes responsibility for another reason, "
             "such as that the source of the act lies outside the agent, is left open."),
        ],
        "standard": (
            "Finish when you can build a Frankfurt case as a structural model and report both tests of cause.",
            "You should be able to write the equations for decision, backup and act, state whether the "
            "decision is a but-for cause, find the variable that must be held fixed for it to become a "
            "cause, and say which dispute about the case the model leaves open. A claim that the agent "
            "&ldquo;is still the cause&rdquo; without the witness has not been computed."),
        "note": "The structural lab is Boolean and the equations are given by you. It cannot tell you that a real intervener could read a decision before it was made, and the objections to the case turn on exactly that.",
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "the-problem-of-evil-as-an-inconsistent-set",
        "title": "The Problem of Evil as an Inconsistent Set",
        "module": "God and evil",
        "one_line": "The logical problem of evil is a set of five sentences with no model, and each response to it is a deletion or a weakening of one.",
        "summary": (
            "That God is all-powerful, all-knowing and wholly good, that evil exists, and that a being "
            "like that eliminates evil cannot all be true. The consistency lab confirms there is no "
            "model, shows that every sentence is needed for the clash, and then shows what the "
            "free-will defence changes, and what the evidential version asserts instead."
        ),
        "key": [
            "o, k, g: omnipotent, omniscient, good",
            "e: evil exists",
            "bridge: (o ∧ k ∧ g) → ¬e",
            "five sentences, no model: drop or weaken one",
            "weaker bridge: (o ∧ k ∧ g) → ¬u",
        ],
        "key_label": "Five sentences, and the one that is weakened",
        "concepts_intro": (
            "This lesson uses the same method as the free-will triad and the fission case. What is new "
            "is the sentence that does the connecting, and the observation that arguing for consistency "
            "is a matter of finding a model."),
        "concepts": [
            ("The set has five sentences",
             "Write `o`, `k` and `g` for the three attributes, `e` for &ldquo;evil exists&rdquo;, and a bridge "
             "premise `(o ∧ k ∧ g) → ¬e` for &ldquo;a being with all three attributes eliminates evil&rdquo;. "
             "The lab finds no model, and all five are needed."),
            ("A defence needs only a model",
             "To show the five sentences do not contradict, it is enough to describe a possible way "
             "for them all to be true. A defence changes the bridge so that it no longer says "
             "that evil cannot exist, and the lab finds a model."),
            ("The evidential problem asserts a different sentence",
             "The weakened bridge says such a being eliminates <em>unnecessary</em> evil, written `u`. "
             "The evidential argument asserts that some evil is unnecessary, `u`, and then the set "
             "has no model again. Its support is probabilistic and the set is not."),
        ],
        "read_title": "Five sentences and what each response does",
        "read_intro": "The set, the exits, the defence as a model, and the premise that the evidential argument adds.",
        "body": [
            ("p", "The problem is old and has been stated many times. J. L. Mackie's version has three "
                  "claims, that God is omnipotent, that God is wholly good, and that evil exists, joined "
                  "by two principles he called quasi-logical: a good being eliminates evil as far as it "
                  "can, and there are no limits to what an omnipotent being can do. The set below is the "
                  "one later statements settle on. It adds omniscience, since a being that could not "
                  "know of an evil could not be faulted for leaving it, and it folds the two principles "
                  "into one bridge. Each of the first three sentences is part of the traditional idea of "
                  "God, the fourth is a fact, and the fifth connects them."),
            ("math", [
                "1.  o                     God is omnipotent",
                "2.  k                     God is omniscient",
                "3.  g                     God is wholly good",
                "4.  e                     evil exists",
                "5.  (o ∧ k ∧ g) → ¬e      such a being eliminates evil",
            ]),
            ("p", "From 1, 2 and 3 the antecedent of 5 is true, so `¬e` follows, which contradicts 4. "
                  "The lab confirms there is no row of the table that satisfies all five, and the smallest "
                  "inconsistent subset it reports is the whole set. Dropping any one gives a model, "
                  "and the drop menu shows each."),
            ("p", "Each deletion is a position that has been held. Dropping sentence 1 or 2 gives a "
                  "God who is limited in power or knowledge. Dropping 3 gives a God who is not "
                  "good, and dropping 4 says that evil is an illusion, which "
                  "most readers think denies a fact. Dropping 5 is the interesting move, because it "
                  "keeps all of the traditional attributes and the fact, and says that a being "
                  "with those attributes might still permit evil."),
            ("h3", "The defence as a model"),
            ("p", "The bridge is not a logical truth. It says a good being eliminates evil as far as "
                  "it can, and it is plausible only if there is no reason a good being would have "
                  "for permitting some. The free-will defence supplies one. Perhaps a world with free "
                  "creatures is better than one without, and perhaps any free creature might misuse "
                  "its freedom, and then some evil is necessary for the greater good. Write `u` for "
                  "&ldquo;there is evil that is not necessary for any greater good&rdquo;. The weakened "
                  "bridge is `(o ∧ k ∧ g) → ¬u`: such a being eliminates the unnecessary evil."),
            ("p", "With that bridge the lab finds a model. It makes `o`, `k`, `g` and `e` true and "
                  "`u` false. The model shows the five sentences can all be true together, and "
                  "that is all a defence claims. Alvin Plantinga's version does not assert that the "
                  "story about freedom is true or likely, only that it is possible, and a possible way "
                  "for all the sentences to hold is what a model is."),
            ("p", "That is also its limit. A defence settles the <em>logical</em> problem and does not "
                  "show that God exists or that the story is probable. It establishes that the "
                  "contradiction is not forced. The lab can check the model, and whether `u` is false "
                  "is not something it can check."),
            ("p", "This is where the evidential problem enters. Instead of the bridge, it asserts "
                  "`u`: that there are evils, such as the suffering of an animal in a forest fire "
                  "that no one sees, that look as if no greater good required them. Add `u` to the "
                  "weakened bridge and the three attributes, and the lab finds no model again. The "
                  "logic of the clash is the same as before. What differs is where the support for "
                  "the offending sentence comes from: for `u` it is an estimate of how likely it is, "
                  "given what we can see, and the estimate is exactly what the lab does not compute. "
                  "The reply that we are poorly placed to see what a being with unlimited knowledge "
                  "would see is a reply to that estimate, not to the logic."),
        ],
        "lab": ("argkit", {
            "mode": "consistency",
            "preset": "mackie",
            "presets": [
                {"id": "mackie", "label": "the traditional attributes, evil and the bridge",
                 "sentences": ["o", "k", "g", "e", "(o & k & g) -> ~e"], "expect": {"coVerdict": "Inconsistent", "coMis": "{1, 2, 3, 4, 5}", "coWitness": "none"}},
                {"id": "free-will-defence", "label": "the bridge weakened to unnecessary evil",
                 "sentences": ["o", "k", "g", "e", "(o & k & g) -> ~u"], "expect": {"coVerdict": "Consistent", "coMis": "none", "coWitness": "e=T g=T k=T o=T u=F"}},
                {"id": "evidential", "label": "the weakened bridge and the claim that evil is unnecessary",
                 "sentences": ["o", "k", "g", "u", "(o & k & g) -> ~u"], "expect": {"coVerdict": "Inconsistent", "coMis": "{1, 2, 3, 4, 5}", "coWitness": "none"}},
            ],
            "panel_title": "Weaken the bridge, then assert the unnecessary evil",
            "panel_intro": "The first set is the five sentences of the text, with a tilde for not. Drop each one in turn and read the model. The second preset replaces the last sentence by the weaker bridge, using the letter `u`. The third adds the claim that there is unnecessary evil, and the clash returns.",
        }),
        "steps_title": "Treating a problem of evil as a set",
        "steps_intro": "Five moves, in this order, for the logical problem and for its variants.",
        "steps": [
            ("Write each commitment as a sentence",
             "Include the bridge. The attributes and the fact are uncontroversial as sentences. The "
             "bridge is where the argument is carried."),
            ("Ask for a model, and for the smallest inconsistent subset",
             "If there is no model, the subset names the sentences among which one must be given up. "
             "When the subset is the whole set, no sentence is idle."),
            ("Delete each sentence once",
             "Name the position each model represents and what it gives up, such as a limited God, "
             "or the denial that evil exists."),
            ("Weaken the bridge and test again",
             "Replace the bridge by a weaker conditional, such as one about unnecessary evil, and ask "
             "again for a model. A model shows consistency, which is all a defence claims."),
            ("Find what the argument now asserts",
             "If the weakened set is consistent, the argument that remains must assert a sentence "
             "that restores the clash. Name it, and say what supports it."),
        ],
        "worked": {
            "title": "From the logical to the evidential problem",
            "intro": ["The three attributes `o`, `k`, `g`, evil `e`, and unnecessary evil `u`."],
            "lines": [
                "o, k, g, e and (o and k and g) implies not e: no model",
                "every one of the five is in the smallest subset",
                "weaken to (o and k and g) implies not u",
                "o, k, g, e with u false: a model",
                "the defence has shown the set is consistent",
                "now assert u: the clash returns, no model",
            ],
            "after": [
                "The first change is a deletion and the second an assertion, and each is read off a table. "
                "The first shows that a defence can be given. The second shows what the evidential "
                "argument needs, a sentence whose support is not in the table."
            ],
        },
        "quiz_title": "Deletions, weakenings and assertions",
        "quiz": [
            {"q": "What does the lab report for the five sentences of the first preset?",
             "a": ["Consistent, with `e` true and the bridge false",
                   "Inconsistent, with a smallest inconsistent subset that is the whole set",
                   "Inconsistent, with a smallest subset of 1, 2, 3 and 4 only",
                   "Consistent, with `o`, `k` and `g` false"],
             "c": 1,
             "why": "No row satisfies all five. The bridge is needed to link the attributes to the absence of evil, so a subset without sentence 5 has a model, and a subset without any one of the other four is consistent. The other choices describe models the lab does not find."},
            {"q": "What does the free-will defence change in the set?",
             "a": ["It denies that evil exists",
                   "It denies that God is omniscient",
                   "It weakens the bridge, so that a good being eliminates only unnecessary evil",
                   "It adds the claim that evil is unnecessary"],
             "c": 2,
             "why": "The defence leaves the attributes and the fact and replaces the bridge, so the set has a model. Denying evil or omniscience is a deletion of a different sentence, and adding the claim that evil is unnecessary restores the clash, which is what the evidential argument does."},
            {"q": "In the third preset the lab reports no model. What has changed from the second?",
             "a": ["The bridge has been strengthened",
                   "`e` has been removed",
                   "The claim `u`, that there is unnecessary evil, has been asserted",
                   "God has been given another attribute"],
             "c": 2,
             "why": "The weakened bridge together with `o`, `k` and `g` gives `¬u`, and the preset asserts `u`. The bridge is the same as in the second preset, `e` plays no role in the clash, and no attribute has been added."},
            {"q": "A reader says that the problem of evil is a probabilistic argument only. What does the first preset show against this?",
             "a": ["That the argument is sound",
                   "That probability is irrelevant to the problem of evil",
                   "That a probabilistic argument is invalid",
                   "That a version of the problem is a question of consistency and needs no probabilities"],
             "c": 3,
             "why": "The logical version is settled by whether the five sentences have a model, and the lab finds none without counting any likelihoods. It does not show soundness, since the bridge may be rejected, and it does not show the evidential version is irrelevant, since that asserts `u` on probabilistic grounds."},
        ],
        "mistakes": [
            ("Believing the problem of evil is a probabilistic argument only",
             "The logical problem has no probabilities in it. The five sentences have no model, and the "
             "lab reports it by checking every row. The probabilistic version is a second argument, "
             "which asserts that unnecessary evil is likely; it appears in the third preset as the "
             "sentence `u`, and what the lab can say about it is only that, if it is true, the set "
             "has no model."),
            ("Thinking a defence shows that God exists, or that evil is justified",
             "The lab finds a model for the weakened set, and that shows the sentences can all be "
             "true together. It shows nothing about whether they are, and a model in which `u` is "
             "false is a possibility and not a finding. A defence answers an argument that the "
             "attributes are impossible, and no more."),
            ("Treating the bridge as a logical truth",
             "The sentence `(o ∧ k ∧ g) → ¬e` is false in the lab's model for the second set, where "
             "all three attributes and `e` are true. It is an assumption about what a good being "
             "does, and the free-will defence is a reason to reject it. The argument for the "
             "problem has to defend the bridge, and the lab cannot do that for it."),
        ],
        "standard": (
            "Finish when you can write the problem of evil as a set, find its smallest inconsistent subset, and state what each response changes.",
            "You should be able to write the five sentences, report the verdict, delete each sentence in "
            "turn and name the position it yields, weaken the bridge and say what a model for it "
            "shows, and name the sentence the evidential argument asserts. A response named without "
            "the sentence it alters has not been placed."),
        "note": "A consistency check is silent on whether any of the five sentences is true, whether the weakened bridge is plausible, and whether a given evil is necessary for a greater good. The first is metaphysics, the second is a question about goodness, and the third is where the evidential debate lives.",
    },
]
