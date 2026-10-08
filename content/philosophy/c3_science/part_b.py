"""Course 3, lessons 6 to 10: the Duhem-Quine problem, Mill's methods, and causation."""


def _case(name, values, verdict):
    return {"name": name, "values": values, "verdict": verdict}


LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "the-duhem-quine-problem",
        "title": "The Duhem–Quine Problem",
        "module": "Confirmation",
        "one_line": "A failed prediction refutes the theory together with its auxiliaries, and logic cannot say which to give up.",
        "summary": (
            "A theory yields a prediction only when it is joined to auxiliary hypotheses and a bridge to the "
            "instruments. When the prediction fails, the theory, the auxiliaries, the bridge and the "
            "observation cannot all be true, and the smallest inconsistent subset is the whole set. The "
            "observation refutes the conjunction and nothing smaller."
        ),
        "key": [
            "theory + auxiliaries + bridge → prediction",
            "prediction fails: the whole set is false",
            "drop any one member: consistent again",
            "logic alone cannot pick which to drop",
        ],
        "key_label": "What a failed test refutes",
        "concepts_intro": (
            "The previous lessons let a theory forbid an outcome and treated one forbidden observation as "
            "the end of it. This lesson asks what exactly was forbidden."
        ),
        "concepts": [
            ("A prediction needs more than the theory",
             "Newton's laws say nothing about where Uranus will stand on a given night. The calculation "
             "also uses the list of planets that pull on it, their masses, and a rule that links the "
             "computed position to what a telescope reports. Each of these is an assumption added to the "
             "theory."),
            ("A failed prediction makes a set inconsistent",
             "Write the theory, the added assumptions, the link to the instruments and the claim that the "
             "predicted outcome did not occur. These cannot all be true together, and that is all the "
             "observation establishes."),
            ("Every member is a candidate for blame",
             "Dropping any single member of the set restores consistency. The logic is silent on which "
             "one to drop, and the choice rests on grounds the set does not contain."),
        ],
        "read_title": "From a failed prediction to a set of claims",
        "read_intro": (
            "The prediction first, written as a derivation. Then the set it makes inconsistent, and the "
            "repairs that restore consistency."
        ),
        "body": [
            ("p", "A theory by itself forbids nothing observable. “Falsification and What a Theory Forbids” "
                  "gave a hypothesis a likelihood of zero for some outcome, and that is the right way to "
                  "model a theory together with the conditions of one particular test. The conditions "
                  "are the subject here."),
            ("def", ("Auxiliary hypothesis",
                     "An <strong>auxiliary hypothesis</strong> is an assumption, other than the theory under "
                     "test, that is used to derive a prediction from it. A <strong>bridge</strong> is the "
                     "assumption that links a computed quantity to what an instrument will report.")),
            ("p", "Write `h` for the theory, `a` for the auxiliary that nothing unseen disturbs the system, "
                  "`b` for the bridge, and `e` for the predicted observation. The prediction is a "
                  "conditional: if the theory, the auxiliary and the bridge are all true, then `e`. "
                  "The observation is that `e` did not occur."),
            ("math", [
                "1   h",
                "2   a",
                "3   b",
                "4   (h ∧ a ∧ b) → e",
                "5   ¬e",
            ]),
            ("p", "Sentences 1 to 4 entail `e`, and sentence 5 denies it. So the five cannot all be true, "
                  "and this is the whole logical content of a failed test. The lab runs the test of "
                  "“Consistency and Belief Sets”: it finds no assignment of truth values to the four "
                  "letters that makes all five true, and names the smallest subset that cannot be true as "
                  "`{1, 2, 3, 4, 5}`: the whole set."),
            ("thm", ("The refuted unit is the set",
                     "If every member of an inconsistent set is needed for the inconsistency, the set has "
                     "no smaller inconsistent subset, and dropping any one member makes the rest "
                     "consistent. A failed prediction therefore refutes the conjunction of everything used "
                     "to derive it, and no single member by itself.")),
            ("p", "Duhem made this point for physics: an experiment can condemn only a whole theoretical "
                  "group, never an isolated hypothesis, because the physicist reads the instrument through "
                  "the theory being tested. Quine extended it to everything we believe, so that any "
                  "statement can be held true come what may if enough is adjusted elsewhere, and the "
                  "unit of empirical significance becomes the whole of science. The set above is Duhem's "
                  "group written out in five lines. Where the two differ is whether its boundary can be "
                  "drawn anywhere short of everything, and the lab, which takes the sentences it is given, "
                  "cannot say."),
            ("p", "The lab's drop control shows this. Drop sentence 1 and the other four have models; drop "
                  "sentence 2 and they have models; the same holds for 3, 4 and 5. Five different repairs "
                  "are equally consistent. Dropping sentence 5 means disbelieving the observation, and "
                  "that is a repair too, though a costly one when the measurement was careful."),
            ("example", ("Uranus and the eighth planet",
                         "By the 1840s the orbit of Uranus disagreed with the position computed from "
                         "Newton's laws and the seven known planets. Astronomers who dropped the auxiliary "
                         "that no further planet exists, and kept Newton, computed where an eighth would "
                         "have to be, and Neptune was found close to that place in 1846. The same repair was "
                         "tried for Mercury's orbit: a planet inside Mercury's orbit was proposed, none "
                         "was found, and the repair that worked dropped the theory, in 1915.")),
            ("p", "The second and third presets are two consistent sets made from this one failure. In the "
                  "second, the theory is kept and the auxiliary is replaced by its denial, so an eighth "
                  "planet exists. In the third, the auxiliary is kept and the theory is denied. Each "
                  "has exactly one model, and the count is the same. Nothing in the arithmetic prefers "
                  "either."),
            ("p", "What does choose is outside the set. A repair that predicts something new and checkable, "
                  "such as a planet at a stated place, can be tested on its own, and one that only "
                  "restores the old prediction cannot. That is a reason to try the first kind of repair "
                  "first, and it is a reason of method and not of logic."),
            ("p", "The positions can be put at full strength. The falsificationist can say that science "
                  "proceeds by a decision to hold the auxiliaries fixed for the purpose of a test, so "
                  "that the theory is exposed. The holist can answer that no such decision is forced by "
                  "the logic, and that a decision to hold something fixed can be revised by the next test. "
                  "The lab agrees with both: the set is refuted, and the choice of what to blame is made "
                  "outside it."),
            ("p", "The lab's limit is that it tests only whether sentences can all be true together. It "
                  "does not weigh them, so it cannot say that the bridge is better supported than the "
                  "theory. The earlier lessons supply the means for that: the posterior of each member "
                  "given the observation."),
        ],
        "lab": ("argkit", {
            "mode": "consistency",
            "preset": "duhem",
            "presets": [
                {"id": "duhem",
                 "label": "Theory, auxiliary, bridge and a failed prediction",
                 "sentences": ["h", "a", "b", "(h & a & b) -> e", "~e"],
                 "expect": {"coModels": "0 of 16", "coVerdict": "Inconsistent", "coMis": "{1, 2, 3, 4, 5}"}},
                {"id": "neptune",
                 "label": "Theory kept, auxiliary denied: an eighth planet",
                 "sentences": ["h", "~a", "b", "(h & a & b) -> e", "~e"],
                 "expect": {"coModels": "1 of 16", "coVerdict": "Consistent", "coWitness": "a=F b=T e=F h=T"}},
                {"id": "rival",
                 "label": "Auxiliary kept, theory denied",
                 "sentences": ["~h", "a", "b", "(h & a & b) -> e", "~e"],
                 "expect": {"coModels": "1 of 16", "coVerdict": "Consistent", "coWitness": "a=T b=T e=F h=F"}},
            ],
            "panel_title": "Choose what to drop",
            "panel_intro": (
                "The first set is the failed prediction in full. Use the drop menu to remove one "
                "sentence at a time and read the verdict, then choose the other two sets, which "
                "repair the same failure in two different ways."
            ),
        }),
        "steps_title": "Reading a failed prediction",
        "steps_intro": "Five steps, in this order, for any test that did not come out as predicted.",
        "steps": [
            ("List what the derivation used",
             "Write the theory, every auxiliary, and the bridge to the instrument as separate "
             "sentences. If you cannot say what the auxiliaries were, you have not yet said what was "
             "tested."),
            ("Write the prediction as a conditional",
             "Join the theory, auxiliaries and bridge as the antecedent and the predicted outcome as "
             "the consequent. Then add the observation that the outcome failed."),
            ("Find the smallest inconsistent subset",
             "Run the set through the consistency test. If each sentence is needed, the smallest "
             "inconsistent subset is the whole set."),
            ("Drop each member in turn",
             "For every sentence, ask whether the rest is consistent. Each yes is a repair that the "
             "logic permits."),
            ("Ask what each repair costs",
             "For each repair, say what else it commits you to and whether that can be tested "
             "separately. Prefer the repair that makes a prediction of its own."),
        ],
        "worked": {
            "title": "Uranus against Newton",
            "intro": [
                "Take `h` as Newton's laws, `a` as &ldquo;no eighth planet&rdquo;, `b` as the bridge "
                "from computed to observed position, and `e` as the predicted orbit."
            ],
            "lines": [
                "1  h   2  a   3  b   4  (h ∧ a ∧ b) → e   5  ¬e",
                "assignments of h, a, b, e making all five true: 0 of 16",
                "smallest inconsistent subset: {1, 2, 3, 4, 5}",
                "replace a by ¬a: 1 model, h = T, a = F, b = T, e = F",
                "replace h by ¬h: 1 model, h = F, a = T, b = T, e = F",
            ],
            "after": [
                "Both repairs are consistent, with the same number of models, and the arithmetic cannot "
                "say which was right. History chose the first for Uranus. For Mercury it tried the "
                "same repair first, a planet Vulcan, and the second repair, a new theory, was the one "
                "that worked."
            ],
        },
        "quiz_title": "What the failed test refutes",
        "quiz": [
            {"q": "In the first set the sentences are `h`, `a`, `b`, `(h ∧ a ∧ b) → e` and `¬e`. Which is "
                  "its smallest inconsistent subset?",
             "a": ["`h` and `¬e`",
                   "`h`, `(h ∧ a ∧ b) → e` and `¬e`",
                   "All five sentences",
                   "`a`, `b` and `¬e`"],
             "c": 2,
             "why": "Every proper subset has a model. For the second option, take `h` true, `a` false and "
                    "`e` false: all three sentences hold. The first and fourth subsets are consistent "
                    "for the same reason. Each of the five is needed."},
            {"q": "In the second set the theory is kept and the auxiliary is replaced by its denial. The "
                  "lab reports it consistent. What does that show?",
             "a": ["That the theory is now confirmed",
                   "That the observation is compatible with the theory if an eighth planet is allowed",
                   "That an eighth planet exists",
                   "That the original auxiliary was true"],
             "c": 1,
             "why": "Consistency shows only that the sentences can all be true together. It does not say "
                    "that they are, so the planet's existence and the confirmation of the theory are not "
                    "shown, and the original auxiliary is the one the repair discards."},
            {"q": "The second and third sets each have exactly one model. What follows?",
             "a": ["The two repairs are equally probable",
                   "The theory is false",
                   "The observation was in error",
                   "The logic gives no ground for preferring either repair"],
             "c": 3,
             "why": "Counting assignments is not weighing credences, so equal counts do not make the "
                    "repairs equally probable. Neither repair denies the observation, and the theory is "
                    "denied only in the third set. What the equal counts show is that consistency is not "
                    "what chooses between them."},
            {"q": "Which would be an independent test of the auxiliary &ldquo;no eighth planet&rdquo;?",
             "a": ["Searching the sky near the place an eighth planet would have to occupy",
                   "Deriving the prediction for Uranus a second time",
                   "Measuring Uranus's position again with the same bridge",
                   "Checking that the five sentences are inconsistent"],
             "c": 0,
             "why": "A test is independent when it can come out against the auxiliary without using the "
                    "prediction that failed. A search for the planet can. Re-deriving or re-measuring "
                    "tests the same set again, and the consistency check is a fact about the sentences, "
                    "not about the sky."},
        ],
        "mistakes": [
            ("Thinking a failed test refutes the theory",
             "The lab finds no assignment that makes `h`, `a`, `b`, the conditional and `¬e` all true, but "
             "it also finds that replacing `a` by `¬a` leaves a consistent set that keeps `h`. The "
             "observation refutes the conjunction of everything used to derive the prediction, so the "
             "theory is refuted only if the auxiliaries and the bridge are held fixed."),
            ("Concluding that any theory can be saved, so tests prove nothing",
             "Each repair is consistent, but a repair is a new claim, and the claim can be tested. A "
             "rescue that predicts nothing further costs the theory its risk, which is the cost that the "
             "lesson on falsification counted in forbidden outcomes."),
            ("Reading an inconsistent set as saying that every member is false",
             "Inconsistency says that at least one member is false. In the first set there are five "
             "repairs, and in each of them four of the sentences are kept."),
        ],
        "standard": (
            "Finish when you can write a prediction as a set and locate what the failed observation refutes.",
            "Given a theory, its auxiliaries, a bridge and a failed prediction, you should be able to "
            "write them as a set of sentences, find the smallest inconsistent subset, list the repairs "
            "that restore consistency, and say what separates a repair that can be tested from one that "
            "cannot."
        ),
        "note": (
            "The letters `h`, `a`, `b` and `e` stand for whole claims, and a real derivation has many "
            "more auxiliaries than one. The lab accepts up to eight sentences and six letters, and the "
            "result does not depend on how many: the more were used, the larger the set that is refuted."
        ),
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "mills-methods-and-the-common-factor",
        "title": "Mill's Methods and the Common Factor",
        "module": "Causation",
        "one_line": "The factor present in every positive case and absent from every negative one is a candidate for the cause, and no more.",
        "summary": (
            "Mill's method of agreement looks for the factor shared by every case with the effect, and his "
            "method of difference for the one factor that separates a case with the effect from a case "
            "without it. A case table makes the search mechanical: the positive cases keep what they "
            "share, the negative cases eliminate what they contain, and the lab lists every one- or "
            "two-factor formula that fits. A fit is a candidate for the cause; the table cannot rule out "
            "the others that fit, or a factor it does not list."
        ),
        "key": [
            "agreement: shared by every positive case",
            "difference: a well case with it eliminates it",
            "a fit is a candidate, not yet a cause",
            "two causes: no single factor fits",
        ],
        "key_label": "Searching a table for a cause",
        "concepts_intro": (
            "The earlier lessons asked what evidence does to a hypothesis. This one asks how to find a "
            "hypothesis about a cause in a table of cases."
        ),
        "concepts": [
            ("The method of agreement",
             "Take the cases in which the effect occurred and ask which factor appeared in all of them. "
             "A factor missing from even one such case is eliminated."),
            ("The method of difference",
             "Mill's method of difference sets a case with the effect beside one as like it as possible "
             "without the effect, and blames the one factor in which they differ. A table rarely holds "
             "such a pair, and what it offers instead is elimination: a factor present in a case without "
             "the effect cannot be what was sufficient for it."),
            ("A fit is a candidate",
             "A factor that survives both is the only one the table leaves, among the factors the table "
             "lists. Whether it is the cause depends on what the table did not list and on whether one "
             "cause is all there is."),
        ],
        "read_title": "Five diners and five dishes",
        "read_intro": (
            "A table first, then the two methods applied to it by hand, then what the lab's search adds."
        ),
        "body": [
            ("p", "Five people ate at the same dinner and two of them fell ill. The table records which "
                  "of five dishes each of them ate, as 1 for eaten and 0 for not, and the verdict, 1 for "
                  "ill. The dishes are oysters `O`, soup `S`, bread `B`, wine `W` and cake `C`."),
            ("math", [
                "diner   O  S  B  W  C  |  ill",
                "---------------------------------",
                "Ann     1  1  1  0  1  |   1",
                "Ben     1  0  1  1  0  |   1",
                "Cy      0  1  1  1  1  |   0",
                "Di      0  1  0  0  1  |   0",
                "Eve     0  0  1  0  0  |   0",
            ]),
            ("p", "Begin with the method of agreement, which looks only at the ill diners. Ann ate oysters, "
                  "soup, bread and cake; Ben ate oysters, bread and wine. The dishes both ate are oysters "
                  "and bread, so soup, wine and cake are eliminated."),
            ("p", "Then turn to the well diners. Mill's method of difference would look here for a pair of "
                  "cases alike in everything but one dish, and the table has none: Ann and Cy, the closest "
                  "pair, differ in the oysters and in the wine. What the well diners offer instead is "
                  "elimination. Cy ate bread and did not fall ill, so, if one dish is responsible, bread "
                  "is not it. No well diner ate oysters. Oysters survive both steps, and nothing else does."),
            ("def", ("The joint method",
                     "Mill's <strong>joint method of agreement and difference</strong> applies agreement "
                     "twice: the cases with the effect agree in having the factor, and the cases without "
                     "it agree in lacking it. In the lab's terms, it is a definition that agrees with the "
                     "verdict on every row.")),
            ("p", "The lab does this search for any table. With the definition `O` it agrees on all five "
                  "rows. With the search switched to pairs it also lists every formula built from one "
                  "factor or two, shows the first one it found, and says how many there are. Two fit: "
                  "`O`, and `O ∧ B`, oysters together with bread."),
            ("thm", ("A fit is a candidate",
                     "If a formula agrees with the verdict on every row, then the table does not "
                     "eliminate it. If the table lists every relevant factor, and the effect has a single "
                     "cause, a formula of one factor that fits is that cause.")),
            ("p", "Each of those conditions can fail, and the lab shows the first. The formula `O ∧ B` "
                  "fits because both ill diners ate bread, even though a well diner did too: Cy ate "
                  "bread without oysters, so bread alone fails, and bread with oysters has not been "
                  "excluded. The table has only two ill diners, so it cannot separate oysters from "
                  "oysters with bread. Its other limits are not visible in it at all: the knife, the "
                  "water or the oysters' source are not columns, and a table cannot eliminate a factor "
                  "it does not contain."),
            ("p", "The second preset removes the other assumption, that there is one cause. Here prawns "
                  "`P` or eggs `E` made a diner ill, and no diner ate both. The lab starts with the suspect "
                  "`P`, which misses Ben. No single factor fits, "
                  "because prawns miss Ben and eggs miss Ann and Eve, and the agreement method returns "
                  "nothing common to the ill. The search over pairs finds the disjunction `P ∨ E`. Mill "
                  "called this a plurality of causes, and his methods were not designed for it."),
            ("p", "The lab's limit is that it checks a formula against the cases it is given. It cannot "
                  "say whether the table is complete, or whether the cases were chosen fairly, or "
                  "whether a factor that is always found with the effect is a cause of it or a sign of "
                  "something else. The last of these is the subject of the next lesson."),
        ],
        "lab": ("argkit", {
            "mode": "analysis",
            "search": "pairs",
            "preset": "diners",
            "presets": [
                {"id": "diners", "label": "Five diners, five dishes",
                 "conditions": ["O", "S", "B", "W", "C"], "target": "ill", "definition": "O",
                 "cases": [
                     _case("Ann", [1, 1, 1, 0, 1], 1),
                     _case("Ben", [1, 0, 1, 1, 0], 1),
                     _case("Cy", [0, 1, 1, 1, 1], 0),
                     _case("Di", [0, 1, 0, 0, 1], 0),
                     _case("Eve", [0, 0, 1, 0, 0], 0),
                 ],
                 "expect": {"anAgree": "5 / 5", "anVerdict": "Adequate", "anCands": "2: first O"}},
                {"id": "two-causes", "label": "Prawns or eggs, never both",
                 "conditions": ["P", "E", "M", "T"], "target": "ill", "definition": "P",
                 "cases": [
                     _case("Ann", [1, 0, 1, 1], 1),
                     _case("Ben", [0, 1, 1, 0], 1),
                     _case("Cy", [0, 0, 1, 1], 0),
                     _case("Di", [0, 0, 0, 0], 0),
                     _case("Eve", [1, 0, 0, 0], 1),
                 ],
                 "expect": {"anAgree": "4 / 5", "anFail": "Ben: too narrow", "anVerdict": "Too narrow", "anCands": "1: first P | E"}},
            ],
            "panel_title": "Test a suspect against the table",
            "panel_intro": (
                "The definition is the factor you suspect. Click any value in the table to change a "
                "case and watch the verdict and the list of formulas that fit follow."
            ),
        }),
        "steps_title": "Searching a case table",
        "steps_intro": "Four steps, in this order, for any table of cases and an effect.",
        "steps": [
            ("Apply agreement to the positive cases",
             "Keep only the rows with the effect and list the factors present in every one of them. "
             "Everything else is eliminated."),
            ("Eliminate by the negative cases",
             "Of the factors that remain, remove any that appears in a row without the effect. This is "
             "what the method of difference becomes when no two rows are alike in all but one factor, "
             "and what is left fits every row."),
            ("List every formula that fits",
             "Run the search over single factors and pairs, and read the count. More than one fit means "
             "the table is too small to say which is operating."),
            ("Say what the table cannot rule out",
             "Name a factor the table does not list, and a case that would separate the formulas that "
             "fit. Those are the next two things to collect."),
        ],
        "worked": {
            "title": "Oysters at the dinner",
            "intro": ["Five diners, five dishes; Ann and Ben ill, Cy, Di and Eve well."],
            "lines": [
                "Ann ate O, S, B, C; Ben ate O, B, W",
                "agreement: dishes in both = O, B",
                "well diners: Cy ate B and stayed well, so B is out",
                "no well diner ate O, so O stays",
                "formulas that fit every row: O, and O ∧ B",
            ],
            "after": [
                "The oysters are the candidate. The table does not distinguish oysters from oysters "
                "together with bread, since both ill diners ate bread, and it says nothing about a factor "
                "it does not list. To tell the two apart you need a case with oysters and no bread."
            ],
        },
        "quiz_title": "From a table to a candidate",
        "quiz": [
            {"q": "In the five-diner table, why do the well diners eliminate bread?",
             "a": ["Ben ate bread and was ill",
                   "Ann did not eat wine",
                   "Bread was eaten by more than two diners",
                   "Cy ate bread and was not ill"],
             "c": 3,
             "why": "The negative cases eliminate a factor that appears in a case without the effect, and "
                    "Cy is such a case. Both ill diners did eat bread, which is why agreement keeps it. "
                    "The number of diners who ate it is not the test."},
            {"q": "The lab finds two formulas that fit the five-diner table, `O` and `O ∧ B`. What does "
                  "that show about the table?",
             "a": ["Oysters are not the cause",
                   "Bread is the cause, and oysters a sign of it",
                   "The table cannot separate oysters alone from oysters with bread",
                   "The table is wrong"],
             "c": 2,
             "why": "Both formulas agree with every row, so no row distinguishes them. That shows nothing "
                    "about which is operating. A case with oysters and no bread would decide it, and the "
                    "table has none."},
            {"q": "In the prawns-or-eggs table no single factor fits, and `P ∨ E` does. Which assumption of "
                  "the simple method does this table break?",
             "a": ["That the effect has a single cause",
                   "That the table lists some cases with the effect",
                   "That the factors are eaten rather than drunk",
                   "That the verdicts are known"],
             "c": 0,
             "why": "Agreement looks for one factor in every ill diner, and here the ill diners had "
                    "different factors. The table has ill diners and known verdicts, so the second and "
                    "fourth options do not describe what failed."},
            {"q": "A formula of one factor fits every row of a table. Which is the strongest statement "
                  "that follows?",
             "a": ["It is the cause",
                   "It is a candidate, not eliminated by this table",
                   "It is the cause whenever no other formula fits",
                   "It is proved by the cases"],
             "c": 1,
             "why": "Fitting is all that the table can establish. A unique fit is still only a "
                    "candidate, since the table could omit the factor that matters, so the third option "
                    "adds a condition that does not close the gap. Cases do not prove a general claim."},
        ],
        "mistakes": [
            ("Thinking the factor common to the cases is the cause",
             "In the five-diner table bread is common to both ill diners and still not what the table "
             "points to, since Cy ate it and stayed well. Oysters survive both methods and are "
             "still only a candidate: `O ∧ B` fits the same rows, and neither the knife nor the water "
             "is a column."),
            ("Expecting every effect to have one factor that explains it",
             "The prawns-or-eggs table has no single factor that fits, and the lab's pair search finds "
             "`P ∨ E`. An effect with two independent routes breaks the agreement method without "
             "breaking the table."),
            ("Treating a candidate that survives the well cases as proved",
             "Absence from three well diners eliminates every dish they ate. It does not show that "
             "the dish that remains has any effect: one more well diner who ate the oysters would remove "
             "it, and the table cannot say that none exists."),
        ],
        "standard": (
            "Finish when you can apply both methods to a table and state what the result leaves open.",
            "Given a table of cases with a verdict, you should be able to apply agreement and "
            "difference, list the formulas that fit, and name one factor not in the table and one case "
            "that would separate the formulas that fit."
        ),
        "note": (
            "The lab searches formulas of at most two factors, from the six conditions it allows. A "
            "table that fits only a longer formula will report no candidates, and that is a limit of the "
            "search and not a statement that no cause exists."
        ),
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "correlation-confounding-and-simpsons-paradox",
        "title": "Correlation, Confounding and Simpson's Paradox",
        "module": "Causation",
        "one_line": "A treatment can do better in every group and worse overall, and the group variable explains why.",
        "summary": (
            "Compare two treatments by the rate of success within each group of patients and then by the "
            "pooled rate. In the kidney-stone figures one treatment wins in both groups and loses overall, "
            "because it was given to the harder cases. The reversal is arithmetic; which comparison to "
            "trust depends on what the groups are."
        ),
        "key": [
            "rate = successes / trials, kept exact",
            "A wins in every group, B wins pooled",
            "the confounder sets who gets which arm",
            "which table to trust is a causal question",
        ],
        "key_label": "When the pooled rate reverses",
        "concepts_intro": (
            "A correlation is a comparison of rates. The comparison can change sign when a third variable "
            "is held fixed, and the lab computes both."
        ),
        "concepts": [
            ("A rate is a fraction of trials",
             "The success rate of a treatment is its successes over its trials. Two groups of different "
             "sizes can have rates that differ in order from the order of their pooled counts."),
            ("A confounder is a variable that changes both",
             "If severity affects who is given a treatment and also affects whether it succeeds, severity "
             "confounds the comparison of the treatments."),
            ("Simpson's reversal is a fact about counts",
             "The pooled comparison reverses when the weights of the groups differ between the two arms. "
             "The reversal is a property of the numbers, and nothing is wrong with the arithmetic."),
        ],
        "read_title": "Two treatments, two kinds of stone",
        "read_intro": (
            "The counts first, then the comparison within each group, then the pooled comparison and the "
            "variable that explains the gap."
        ),
        "body": [
            ("p", "“Reference Classes and Statistical Evidence” showed these counts as two reference "
                  "classes and left the reason for the reversal to this lesson. A study compared two "
                  "treatments for kidney stones, open surgery, `A`, and a keyhole procedure, `B`. Patients "
                  "had small stones or large ones, and the study counted successes over patients treated. "
                  "These are the counts the lab starts with."),
            ("math", [
                "stones   A: successes / treated   B: successes / treated",
                "--------------------------------------------------------",
                "small          81 / 87                 234 / 270",
                "large         192 / 263                 55 / 80",
                "all           273 / 350                289 / 350",
            ]),
            ("p", "Within small stones `A` succeeded `81/87`, which is `27/29`, against `13/15` for `B`; "
                  "within large stones `A` succeeded `192/263` against `11/16`. In each group `A` has "
                  "the higher rate. Pooled, `A` has `273/350`, which is `39/50`, and `B` has `289/350`, and "
                  "`B` is higher. The lab's verdict tile reads Reversal."),
            ("p", "There is no mistake in either comparison. The reason is in the denominators. `A` "
                  "was given to 263 patients with large stones and 87 with small, and `B` to 80 with large "
                  "and 270 with small. Large stones are the harder cases, with success rates below "
                  "those of small stones under both treatments, so `A`'s pooled figure is pulled down "
                  "by a mix that is mostly hard cases."),
            ("def", ("Confounder",
                     "A <strong>confounder</strong> is a variable that influences both which treatment a "
                     "patient receives and whether the treatment succeeds, so that comparing the "
                     "treatments without it compares different kinds of patient.")),
            ("p", "The way to remove the effect of the mix is to give both treatments the same mix. The "
                  "lab's weight control, switched from pooled to standardised, weights each group by "
                  "its share of all patients, which is the same weighting for both arms. Under that "
                  "weighting the lab prints `634983/762700` for `A` against `6231/8000` for `B`, about `0.83` "
                  "against `0.78`, so the adjusted comparison agrees with both groups."),
            ("thm", ("When the pooled comparison reverses",
                     "The pooled comparison disagrees with the comparison in both groups only if the two "
                     "treatments were given to different proportions of the groups, and the groups "
                     "themselves differ in their rates. With balanced groups the pooled comparison "
                     "agrees with the groups.")),
            ("p", "The second preset shows the balanced case. Both arms have the same number in each "
                  "group, `A` wins in each group, and `A` wins pooled; the lab's verdict is No reversal. "
                  "The third preset shows the pattern of the first in real counts: two of the largest "
                  "departments in the 1973 admissions to the University of California at Berkeley. "
                  "Women were admitted at a higher rate in each department and at a lower rate over the "
                  "two together, since they applied more to the department that admitted fewer."),
            ("p", "Which table to believe is not a question the lab can settle. If severity is the "
                  "reason the doctors chose a treatment, then comparing within groups is right. If the "
                  "grouping variable is itself an effect of the treatment, such as a complication that "
                  "the treatment causes, then conditioning on it removes part of the effect being "
                  "measured and the pooled comparison is the right one. The same counts can support "
                  "either answer, and the difference is a claim about what causes what."),
            ("p", "That is where this lesson meets the next ones. A correlation between a treatment and "
                  "an outcome is a comparison of rates; whether it reflects a cause is decided by a "
                  "model of how the variables influence each other, and “Counterfactual Causation and "
                  "the But-For Test” is where such models are written down."),
        ],
        "lab": ("choicekit", {
            "mode": "simpson",
            "preset": "kidney",
            "weight": "pooled",
            "presets": [
                {"id": "kidney", "label": "Kidney stones, small and large",
                 "names": ["A", "B"],
                 "groups": [{"name": "small", "a": [81, 87], "b": [234, 270]},
                            {"name": "large", "a": [192, 263], "b": [55, 80]}],
                 "expect": {"siVerdict": "Reversal", "siPooled": "A 273/350 vs B 289/350: B higher", "siAdjusted": "A 273/350 vs B 289/350: B higher"}},
                {"id": "no-reversal", "label": "Balanced groups, no reversal",
                 "names": ["A", "B"],
                 "groups": [{"name": "small", "a": [18, 20], "b": [16, 20]},
                            {"name": "large", "a": [10, 20], "b": [8, 20]}],
                 "expect": {"siVerdict": "No reversal", "siPooled": "A 28/40 vs B 24/40: A higher"}},
                {"id": "berkeley", "label": "Berkeley admissions, departments A and F",
                 "names": ["women", "men"],
                 "groups": [{"name": "Department A", "a": [89, 108], "b": [512, 825]},
                            {"name": "Department F", "a": [24, 341], "b": [22, 373]}],
                 "expect": {"siVerdict": "Reversal", "siGroup1": "women higher", "siPooled": "women 113/449 vs men 534/1198: men higher"}},
            ],
        }),
        "steps_title": "Checking a comparison for a reversal",
        "steps_intro": "Four steps, in this order, for any comparison of two rates across groups.",
        "steps": [
            ("Compute the rate in each group",
             "For each group and each arm, divide successes by trials and keep the fraction. Say which "
             "arm is higher in each group."),
            ("Compute the pooled rates",
             "Add the successes and the trials over the groups, for each arm separately, and divide. "
             "Say which arm is higher."),
            ("Compare the two verdicts",
             "If the pooled order differs from the order in both groups, there is a reversal. Look at "
             "the group sizes in each arm for the reason."),
            ("Decide what the groups are",
             "If the grouping variable influences who gets which arm and does not result from the arm, "
             "trust the within-group comparison. If it results from the arm, trust the pooled one."),
        ],
        "worked": {
            "title": "Kidney stones, group by group",
            "intro": ["Treatment `A` and treatment `B`, with small and large stones."],
            "lines": [
                "small: A = 81/87 = 27/29, B = 234/270 = 13/15; A higher",
                "large: A = 192/263, B = 55/80 = 11/16; A higher",
                "pooled: A = 273/350, B = 289/350; B higher",
                "A treated 263 large and 87 small; B treated 80 and 270",
                "standardised: A = 634983/762700, B = 6231/8000; A higher",
            ],
            "after": [
                "`A` wins in both groups and loses in the pooled figures, because most of its patients "
                "had large stones, which are the harder cases. Weighting both arms the same way removes "
                "the effect of the mix and restores `A`'s lead, `634983/762700` against `6231/8000`."
            ],
        },
        "quiz_title": "Rates, groups and the pooled figure",
        "quiz": [
            {"q": "In the kidney-stone counts `A` has the higher rate in both groups, and `B` has the higher "
                  "pooled rate. What explains this?",
             "a": ["An arithmetic error in the pooled counts",
                   "The two arms were given different mixes of small and large stones",
                   "Treatment `B` is better for every patient",
                   "Rates cannot be added across groups"],
             "c": 1,
             "why": "The pooled rate weights each group by the number treated, and `A` was given mostly "
                    "large stones, which have lower success under both treatments. The counts add "
                    "correctly, and the third option contradicts the group figures."},
            {"q": "Which of these makes a reversal impossible?",
             "a": ["Each arm treated the same number of patients in each group",
                   "Both groups having the same size",
                   "One group having a higher success rate than the other",
                   "The success rates being fractions rather than percentages"],
             "c": 0,
             "why": "If both arms have the same number in each group, they are weighted the same way, so "
                    "the pooled comparison cannot disagree with both group comparisons. Equal group "
                    "sizes alone leave the arms free to split each group unevenly, and a fraction "
                    "is the same rate as a percentage."},
            {"q": "The grouping variable is a complication that the treatment itself causes. Which "
                  "comparison is more reliable for the effect of the treatment?",
             "a": ["The within-group comparison, because it is more detailed",
                   "Neither, because the numbers conflict",
                   "The average of the two",
                   "The pooled comparison, since conditioning on an effect of the treatment hides part "
                   "of what the treatment does"],
             "c": 3,
             "why": "A variable lying between the treatment and the outcome carries part of the effect, "
                    "so holding it fixed removes that part. Detail is no virtue here. The numbers "
                    "do not decide, so the causal facts must, and these point to the pooled comparison."},
        ],
        "mistakes": [
            ("Thinking a higher overall rate means a better treatment",
             "In the kidney counts `B` has the higher overall rate, `289/350` against `273/350`, and `A` "
             "has the higher rate for small stones and for large ones. The overall rate also reflects "
             "who was treated, and `A` treated mostly the hard cases."),
            ("Always trusting the within-group comparison",
             "Comparing within groups is right only when the groups are not themselves caused by the "
             "treatment. When they are, the pooled comparison measures what the treatment does, and "
             "conditioning on the groups removes some of it."),
            ("Treating the reversal as a trick of the numbers",
             "Each rate is correct, and each comparison answers a different question: how the arms do "
             "for a patient of each kind, and how they do for the patients actually treated. The "
             "reversal is the sign that the two questions have different answers."),
        ],
        "standard": (
            "Finish when you can compute both comparisons, test for a reversal and name the confounder.",
            "Given two tables of counts, you should be able to compute the rate within each group "
            "and pooled, say whether the pooled comparison reverses, and name the variable that "
            "accounts for it and the facts that decide which comparison to trust."
        ),
        "note": (
            "Nothing here is estimated: the lab compares counts as given and does not say whether a "
            "difference could be chance. Statistical inference is left out of the course, and every "
            "figure above is a ratio of whole numbers."
        ),
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "counterfactual-causation-and-the-but-for-test",
        "title": "Counterfactual Causation and the But-For Test",
        "module": "Causation",
        "one_line": "Write a situation as equations, flip a variable, recompute, and see whether the effect flips with it.",
        "summary": (
            "A structural model gives each variable an equation in terms of the variables it depends on. "
            "To test a cause, set it to the other value and recompute everything downstream. If the effect "
            "changes, the variable is a but-for cause. Striking the match and the presence of oxygen both "
            "pass, and the test does not distinguish them."
        ),
        "key": [
            "each variable has an equation",
            "actual values: solve the equations",
            "flip C, recompute: E flips, C is but-for",
            "but-for says nothing of which cause matters",
        ],
        "key_label": "The but-for test",
        "concepts_intro": (
            "Rates compare what happened. A cause is a claim about what would have happened otherwise, "
            "and a model is how the claim is computed."
        ),
        "concepts": [
            ("A structural equation",
             "Each variable that is not an input is defined by an equation in the variables it depends "
             "on, such as `F = S ∧ O` for a fire that needs a struck match and oxygen. The inputs are "
             "given their actual values."),
            ("Flipping a variable",
             "To ask what would have happened, set a variable to its other value, leave the inputs "
             "alone, and recompute every variable that depends on it. The flipped variable ignores "
             "its own equation."),
            ("The but-for test",
             "A variable is a but-for cause of an effect if the effect has a different value after the "
             "flip. This is the counterfactual &ldquo;had the cause not occurred, the effect would not "
             "have&rdquo;, computed."),
        ],
        "read_title": "A fire, two causes, and a chain",
        "read_intro": (
            "The equations first, the actual values second, and then the flip and what it does and does "
            "not tell you."
        ),
        "body": [
            ("p", "A fire starts when a match is struck in a room with oxygen. Write `S` for &ldquo;the match "
                  "is struck&rdquo; and `O` for &ldquo;oxygen is present&rdquo;, each 1 if true and 0 if "
                  "false. These are inputs: nothing in the model determines them. Write `F` for the fire."),
            ("math", [
                "S = 1",
                "O = 1",
                "F = S ∧ O",
            ]),
            ("def", ("Structural model",
                     "A <strong>structural model</strong> lists the input variables with their actual values "
                     "and gives every other variable an equation in terms of variables it depends on. The "
                     "equations must not loop. The <strong>actual values</strong> are what solving them "
                     "gives.")),
            ("p", "Solving the equations gives `F = 1 ∧ 1 = 1`. Now ask the counterfactual question. Set "
                  "`S` to 0 and recompute: `F = 0 ∧ 1 = 0`. The fire does not occur, so the strike is a "
                  "but-for cause. The lab's table shows three columns, the actual values, the values "
                  "with the cause flipped, and a third column that the next lesson puts to use."),
            ("thm", ("The but-for test",
                     "A variable `C` is a but-for cause of the effect `E` in a model when flipping `C`, "
                     "leaving every input at its actual value and recomputing each variable that "
                     "depends on `C`, changes the value of `E`.")),
            ("p", "Do the same for oxygen. Set `O` to 0 and `F = 1 ∧ 0 = 0`, so oxygen is a but-for cause "
                  "too. Ordinary speech would call the strike the cause and the oxygen a condition. "
                  "The equations contain no such difference: `F = S ∧ O` is symmetric in the two. "
                  "Whatever separates a cause from a background condition is a matter of what is "
                  "unusual, controllable or of interest, and the test does not decide it."),
            ("p", "The third preset is a chain. `A` makes `B` happen, and `B` makes `C` happen: `B = A`, "
                  "`C = B`, with `A = 1`. Flipping `A` sets `B` to 0 and then `C` to 0, so `A` is a "
                  "but-for cause of `C` even though it acts only through `B`. The test follows the "
                  "dependency downstream, which is why recomputing is required and a glance at the "
                  "last equation is not enough."),
            ("p", "What the lab computes is only as good as the equations. A model that leaves out a "
                  "second source of fire, or treats two variables as independent that are not, gives a "
                  "different verdict, and no step of the computation can notice. The model is a premise."),
            ("p", "Hume added, almost in passing, a second definition of a cause: had the first object not "
                  "been, the second would never have existed. The test above is that counterfactual with "
                  "the words &ldquo;had not been&rdquo; replaced by a flip and a recomputation. It is "
                  "exact for the model and it has a famous failure, in which an event is plainly a cause "
                  "and the flip leaves the effect unchanged. The next lesson is about that failure."),
        ],
        "lab": ("argkit", {
            "mode": "structural",
            "preset": "match",
            "presets": [
                {"id": "match", "label": "A fire needs a struck match and oxygen: the strike",
                 "equations": {"F": "S & O"}, "exogenous": {"S": 1, "O": 1},
                 "cause": "S", "effect": "F",
                 "expect": {"stActual": "F = 1", "stButFor": "Yes", "stKind": "but-for cause"}},
                {"id": "oxygen", "label": "The same fire: the oxygen",
                 "equations": {"F": "S & O"}, "exogenous": {"S": 1, "O": 1},
                 "cause": "O", "effect": "F",
                 "expect": {"stActual": "F = 1", "stButFor": "Yes", "stKind": "but-for cause"}},
                {"id": "chain", "label": "A makes B, B makes C",
                 "equations": {"B": "A", "C": "B"}, "exogenous": {"A": 1},
                 "cause": "A", "effect": "C",
                 "expect": {"stActual": "C = 1", "stButFor": "Yes", "stKind": "but-for cause"}},
            ],
            "panel_title": "Flip the cause and recompute",
            "panel_intro": (
                "Each preset is a small model. The table shows every variable's actual value and its "
                "value after the cause is flipped; change the equations or the inputs to build your own."
            ),
        }),
        "steps_title": "Testing a cause in a model",
        "steps_intro": "Four steps, in this order, for any situation you can describe in a few variables.",
        "steps": [
            ("List the variables and the inputs",
             "Name each thing that can be true or false, and mark those that nothing else in the model "
             "determines. Give each input its actual value."),
            ("Write one equation for each other variable",
             "Say what each depends on, using and, or and not. If two equations depend on each other, "
             "the model has a loop and must be redrawn."),
            ("Solve for the actual values",
             "Work from the inputs to the effect and check that the effect has the value it did in the "
             "case. If it does not, the model describes another case."),
            ("Flip the candidate and recompute",
             "Set it to the other value, recompute everything that depends on it, and compare the "
             "effect. A change makes it a but-for cause."),
        ],
        "worked": {
            "title": "The fire, the strike and the oxygen",
            "intro": ["Inputs `S = 1`, `O = 1`; the equation `F = S ∧ O`."],
            "lines": [
                "actual: S = 1, O = 1, so F = 1 and 1 = 1",
                "flip S to 0: F = 0 and 1 = 0, the fire goes out",
                "flip O to 0: F = 1 and 0 = 0, the fire goes out",
                "both are but-for causes of the fire",
                "chain: A = 1, B = A = 1, C = B = 1; flip A: C = 0",
            ],
            "after": [
                "The test reports the strike and the oxygen in the same words. Choosing to call one of "
                "them the cause is a decision about what is unusual or of interest, and it is made "
                "outside the model."
            ],
        },
        "quiz_title": "Flipping and recomputing",
        "quiz": [
            {"q": "In the model `F = S ∧ O` with `S = 1` and `O = 1`, what happens to `F` when `O` is "
                  "flipped?",
             "a": ["`F` becomes 0, so `O` is a but-for cause",
                   "`F` stays 1, because `S` is still 1",
                   "`F` becomes 0 only if `S` is flipped as well",
                   "`F` cannot be computed without an equation for `O`"],
             "c": 0,
             "why": "With `O = 0` the conjunction `1 ∧ 0` is 0. The second option treats the fire as if "
                    "one condition were enough, which is not what the equation says. `O` is an input and "
                    "needs no equation."},
            {"q": "The lab reports both the strike and the oxygen as but-for causes of the fire. What "
                  "does that show about the but-for test?",
             "a": ["It is wrong, since only the strike is a cause",
                   "It does not distinguish a cause from a background condition",
                   "Oxygen is more important than the strike",
                   "It reports whichever variable is entered first"],
             "c": 1,
             "why": "The equation treats the two variables alike, so the test must. Which one deserves "
                    "the name is a further judgement. Neither is more important by the model, and the "
                    "order of entry does not matter."},
            {"q": "In the chain `B = A`, `C = B` with `A = 1`, why is `A` a but-for cause of `C`?",
             "a": ["Because `A` appears in an equation next to `C`",
                   "Because `C` has the value 1",
                   "Because flipping `A` flips `B`, and so flips `C`",
                   "Because `A` is the first variable in the model"],
             "c": 2,
             "why": "The flip is passed down the equations: `A = 0` gives `B = 0` and then `C = 0`. "
                    "Neither the order of the variables nor the value of `C` shows that a flip would "
                    "matter, and `A` does not appear in `C`'s equation."},
            {"q": "A model leaves out a second source of ignition, a pilot light that is on. What is "
                  "true of the verdict that the strike is a but-for cause?",
             "a": ["It still holds, because the lab checks the real world",
                   "It holds only if the pilot light is also flipped",
                   "It is wrong in the model and right in the world",
                   "It follows from the equations given and may fail in a model that includes the pilot light"],
             "c": 3,
             "why": "The verdict is computed from the equations and nothing else. Add the pilot light as "
                    "an alternative route to the fire and flipping the strike no longer changes it. The "
                    "lab does not look at the world."},
        ],
        "mistakes": [
            ("Thinking a cause is what made the difference in the circumstances, as against a background condition",
             "The but-for test cannot make that distinction. In `F = S ∧ O` the lab reports the strike "
             "and the oxygen identically, and the equation is symmetric in them. A reader who wants to "
             "say that only the strike is the cause is relying on something outside the model, "
             "which is allowed but should be said."),
            ("Taking the test to apply only to the nearest variable",
             "The chain shows that the flip is carried along every equation that depends on the "
             "variable. `A` is a but-for cause of `C` though `C`'s equation mentions only `B`."),
            ("Treating a verdict as a fact about the world rather than the model",
             "The lab recomputes the equations it was given. If the equations leave out a second route "
             "to the effect, the verdict is correct for the model and may be wrong for the situation."),
        ],
        "standard": (
            "Finish when you can write a situation as equations and test a variable by flipping it.",
            "Given a short description of a situation, you should be able to write its variables and "
            "equations, compute the actual values, flip a candidate cause, recompute, and say whether "
            "it is a but-for cause and what the model leaves out."
        ),
        "note": (
            "The variables here are Boolean and the models are given, not learned from data. Choosing "
            "the variables and the equations is the substantive step, and the course does not try to "
            "automate it."
        ),
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "preemption-and-overdetermination",
        "title": "Preemption, Overdetermination and Redundant Causes",
        "module": "Causation",
        "one_line": "When a backup would have produced the effect anyway, the but-for test fails, and holding the backup fixed repairs it.",
        "summary": (
            "Suzy throws a rock and shatters the bottle; Billy, a moment behind her, would have shattered "
            "it had hers missed. Suzy's throw is not a but-for cause, yet it plainly caused the "
            "shattering. Holding Billy's rock at what it actually did, flipping Suzy's throw does flip "
            "the shattering. When two rocks arrive together, each fails alone and the pair passes."
        ),
        "key": [
            "backup present: flipping the cause is idle",
            "hold the backup at its actual value, flip",
            "two at once: neither alone, both together",
            "no but-for does not mean no cause",
        ],
        "key_label": "When the effect was coming anyway",
        "concepts_intro": (
            "The previous lesson ended on a failure of the but-for test. The failures have two shapes, "
            "and each has a repair that is computed rather than described."
        ),
        "concepts": [
            ("Preemption",
             "A cause brings about the effect and in doing so stops a backup from doing so. Flip the "
             "cause and the backup takes over, so the effect is unchanged."),
            ("Overdetermination",
             "Two causes act at once, each sufficient. Flip either and the other still produces the "
             "effect, so neither is a but-for cause."),
            ("Holding something fixed",
             "A variable is a cause, in the lab's sense, if for some set of other variables held at "
             "their actual values, flipping it flips the effect. The held set cancels the backup."),
        ],
        "read_title": "Two rocks and a bottle",
        "read_intro": (
            "The preemption model first, the failure of the test, the repair, and then the case of two "
            "rocks that arrive together."
        ),
        "body": [
            ("p", "Suzy and Billy each throw a rock at a bottle. Suzy throws first and her rock hits. "
                  "Billy's rock is a moment behind, and would have hit if hers had not. Write `ST` and "
                  "`BT` for the throws, `SH` and `BH` for the hits, and `SHAT` for the shattering."),
            ("math", [
                "ST = 1",
                "BT = 1",
                "SH = ST",
                "BH = BT ∧ ¬SH",
                "SHAT = SH ∨ BH",
            ]),
            ("p", "The equation for `BH` says that Billy's rock hits only if he threw and Suzy's rock has "
                  "not already hit. Solving: `SH = 1`, so `BH = 1 ∧ 0 = 0`, and `SHAT = 1`. Suzy's rock "
                  "did the work."),
            ("p", "Now apply the test of the previous lesson. Flip `ST` to 0. Then `SH = 0`, and `BH = "
                  "1 ∧ 1 = 1`, and `SHAT = 1`. The bottle shatters anyway, so Suzy's throw is not a "
                  "but-for cause. The lab reports No for the but-for test, and a counterfactual account "
                  "of causation that stopped there would say Suzy did not break the bottle."),
            ("def", ("Preemption",
                     "<strong>Preemption</strong> is the case in which a cause brings about an effect and "
                     "thereby prevents a backup that was ready to bring it about. The effect would "
                     "have occurred without the cause, so the cause is not a but-for cause.")),
            ("p", "The repair uses what actually happened to the backup. In the actual course of events "
                  "Billy's rock did not hit: `BH = 0`. Hold `BH` at 0 and flip `ST`. Then `SH = 0`, `BH` "
                  "stays at 0, and `SHAT = 0 ∨ 0 = 0`. With the backup held at its actual value, flipping "
                  "Suzy's throw flips the shattering."),
            ("thm", ("A cause with a held set",
                     "A variable `C` is a cause of `E` when, for some set `W` of other variables held at "
                     "their actual values, flipping `C` changes `E`. If `W` can be empty, `C` is a "
                     "but-for cause. The lab reports the smallest `W` that works.")),
            ("p", "The held values must be the actual ones, and that restriction matters. It is what "
                  "keeps Billy's hit from qualifying: select `BH` as the cause and the lab reports not a "
                  "cause, because in the actual course Suzy's rock has already hit and nothing done to "
                  "`BH` changes the shattering. Billy's throw `BT` is reported only as a joint cause "
                  "with Suzy's, since flipping both throws leaves the bottle whole. That is true, and it "
                  "is not what we mean by Billy having broken it. The joint rule asks only whether a "
                  "pair changes the effect, and it cannot tell equal partners from a cause and a "
                  "bystander."),
            ("p", "The second preset removes the ordering. Both throw, both rocks reach the bottle at "
                  "once, and `BH = BT`. Each hit is enough on its own. Flip `ST` and `BH` still shatters "
                  "the bottle, and holding `BH` at its actual value 1 does not help, since it is "
                  "already doing the work. Neither throw passes alone. Flip both, and the bottle "
                  "survives, so the pair passes together; the lab calls Suzy's throw a joint cause "
                  "with Billy's."),
            ("p", "The third preset is Schaffer's case of trumping, in which a major's order and a "
                  "sergeant's order agree and the soldiers do what the major says. Here it is written "
                  "with the sergeant's order obeyed only if the major gave none, and the equations are "
                  "those of preemption. That is a limit of the model: a Boolean model cannot represent "
                  "a difference between preemption by timing and by rank, unless the equations already "
                  "contain it."),
            ("p", "Whether holding a variable fixed is a faithful account of causation is disputed. The "
                  "lab implements a simplified version of the Halpern–Pearl definition, and the full "
                  "definition adds conditions that exclude some cases the simple version accepts. The "
                  "reader who rejects the whole approach owes a different account of why Suzy broke "
                  "the bottle."),
        ],
        "lab": ("argkit", {
            "mode": "structural",
            "preset": "preemption",
            "presets": [
                {"id": "preemption", "label": "Suzy's rock preempts Billy's",
                 "equations": {"SH": "ST", "BH": "BT & ~SH", "SHAT": "SH | BH"},
                 "exogenous": {"ST": 1, "BT": 1},
                 "cause": "ST", "effect": "SHAT",
                 "expect": {"stButFor": "No", "stHP": "Yes, holding {BH}", "stKind": "cause (holding fixed)"}},
                {"id": "overdetermination", "label": "Both rocks arrive together",
                 "equations": {"SH": "ST", "BH": "BT", "SHAT": "SH | BH"},
                 "exogenous": {"ST": 1, "BT": 1},
                 "cause": "ST", "effect": "SHAT",
                 "expect": {"stButFor": "No", "stHP": "No", "stKind": "joint cause with BT"}},
                {"id": "trumping", "label": "The major's order outranks the sergeant's",
                 "equations": {"SGTO": "SGT & ~MAJ", "ADV": "MAJ | SGTO"},
                 "exogenous": {"MAJ": 1, "SGT": 1},
                 "cause": "MAJ", "effect": "ADV",
                 "expect": {"stButFor": "No", "stHP": "Yes, holding {SGTO}", "stKind": "cause (holding fixed)"}},
            ],
            "panel_title": "Flip the cause, then hold the backup",
            "panel_intro": (
                "The table has a third column in which the witness set is held at its actual values. "
                "Change the cause to BH, Billy's hit, to see a variable that is not a cause."
            ),
        }),
        "steps_title": "Testing a cause when a backup is present",
        "steps_intro": "Five steps, in this order, when the but-for test says No for something that looks like a cause.",
        "steps": [
            ("Run the but-for test",
             "Flip the candidate and recompute. If the effect changes you are done: it is a but-for "
             "cause."),
            ("Look for a backup",
             "If the effect did not change, find the variable that took over, and note its actual value "
             "in the case. That variable is the candidate to hold fixed."),
            ("Hold it at its actual value and flip again",
             "Fix the backup at what it actually did, flip the candidate, and recompute. If the effect "
             "now changes, the candidate is a cause once the backup is held."),
            ("Try the pair if nothing works alone",
             "If no held set works, flip the candidate together with another variable. If the effect "
             "changes, the two are a joint cause of an overdetermined effect."),
            ("Check that the held value was the actual one",
             "A set held at a value that did not occur proves too much, since almost anything is a "
             "cause then. Say what each held variable actually did."),
        ],
        "worked": {
            "title": "Suzy's throw and Billy's backup",
            "intro": ["Inputs `ST = 1`, `BT = 1`; the equations as in the lab."],
            "lines": [
                "actual: SH = 1, BH = 1 ∧ ¬1 = 0, SHAT = 1 ∨ 0 = 1",
                "flip ST to 0: SH = 0, BH = 1 ∧ ¬0 = 1, SHAT = 1",
                "but-for: no, the bottle shatters either way",
                "hold BH at actual 0, flip ST: SH = 0, SHAT = 0 ∨ 0 = 0",
                "cause, holding BH fixed",
            ],
            "after": [
                "Suzy's throw is a cause once Billy's rock is held at what it actually did, which was "
                "nothing. Billy's hit, by the same recipe, is not a cause: whatever is held, Suzy's rock "
                "hits and the bottle breaks."
            ],
        },
        "quiz_title": "Backups and pairs",
        "quiz": [
            {"q": "In the preemption model, why does flipping `ST` leave `SHAT` unchanged?",
             "a": ["Because Suzy's rock never hit",
                   "Because Billy's rock then hits, since `BH = BT ∧ ¬SH` becomes 1",
                   "Because `SHAT` has no equation",
                   "Because the throws are inputs, and inputs cannot be flipped"],
             "c": 1,
             "why": "With `ST = 0` Suzy's rock does not hit, so the clause `¬SH` is satisfied and Billy's "
                    "rock hits instead. Suzy's rock did hit in the actual case, and inputs can be "
                    "flipped; that is how the test works."},
            {"q": "What does holding `BH` at 0 do in the repair?",
             "a": ["It makes Billy's rock hit",
                   "It proves Billy did not throw",
                   "It sets the bottle to unbroken",
                   "It cancels the backup, so the flip of `ST` shows its effect"],
             "c": 3,
             "why": "`BH` is 0 in the actual case, and fixing it there removes the route through which "
                    "Billy's rock took over. Billy still threw, as `BT` stays 1, and the bottle's state is "
                    "computed after the flip, not set by hand."},
            {"q": "Both rocks arrive at once. The lab finds that neither throw is a but-for cause. "
                  "What does it say about `ST`?",
             "a": ["It is a joint cause with `BT`",
                   "It is not a cause of any kind",
                   "It is a cause of the shattering, on its own",
                   "It is a but-for cause once `BH` is held at 1"],
             "c": 0,
             "why": "Flipping both throws leaves the bottle whole, so the pair passes. Holding `BH` at 1 "
                    "keeps Billy's rock hitting, and the bottle shatters whatever Suzy does. The "
                    "single throw fails, and it is not cleared on its own."},
            {"q": "The effect would have happened anyway. Which conclusion does the lesson draw?",
             "a": ["Nothing caused it",
                   "The effect had no cause because a backup existed",
                   "The but-for test cannot decide, and a held-fixed test may",
                   "The model must be mistaken"],
             "c": 2,
             "why": "That the effect was coming anyway shows the but-for test fails, not that there is no "
                    "cause. In the preemption model the held-fixed test finds one. The model is "
                    "doing what it was built to do."},
        ],
        "mistakes": [
            ("Thinking that if the effect would have happened anyway, nothing caused it",
             "The bottle would have shattered without Suzy's throw, and the lab still finds the throw "
             "a cause once Billy's rock is held at what it actually did. A missing but-for dependence "
             "shows that a backup was present and not that the actual cause was idle."),
            ("Holding the backup at whatever value is convenient",
             "Only actual values may be held. If any value were allowed, Billy could be made a cause by "
             "setting Suzy's rock to a miss, and the test would name causes that did nothing."),
            ("Expecting each of two simultaneous causes to pass alone",
             "In the overdetermination model neither throw is a but-for cause and neither passes with "
             "the other's hit held at its actual value. The two pass together, and the lab names the "
             "partner."),
        ],
        "standard": (
            "Finish when you can build a preemption model, show the but-for test fail and recover the cause.",
            "Given a case with a backup, you should be able to write its equations, show that the "
            "candidate is not a but-for cause, find the variable to hold at its actual value, show "
            "the cause pass, and show two simultaneous causes pass only jointly."
        ),
        "note": (
            "The held-fixed test is a simplified version of the Halpern–Pearl definition and is "
            "contested, as the lesson says. The trumping preset is a Boolean rendering with the same "
            "equations as preemption, and it is offered as a limit of the model, not as an analysis of "
            "trumping."
        ),
    },
]
