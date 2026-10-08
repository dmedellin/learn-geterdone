"""Course 6, lessons 07-12 -- deontology, virtue and method. Written by the second author.

The deontology lessons each turn one idea into something with a checkable
structure: a maxim as the defecting choice in a many-player game, a means as a
but-for cause in a causal model, an omission as a variable set to zero, a
dilemma as a set of sentences with no model. The last two lessons test a
function argument for validity and a slippery slope as a chain of conditionals.
"""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "kant-and-the-universalisability-test",
        "title": "Kant and the Universalisability Test",
        "module": "Deontology",
        "one_line": "Treating a maxim as the defecting choice in a many-player game, and asking "
                    "whether its point survives everyone adopting it.",
        "summary": (
            "Kant’s first test asks whether the rule behind an act could be adopted by everyone. "
            "The lab models the rule as the defecting choice among ten players and computes what "
            "the defector gains when alone, and what the choice is worth once all have made it. "
            "When the gain disappears at universal adoption, the practice the act depends on has "
            "collapsed."
        ),
        "key": [
            "a maxim: the rule behind the act",
            "alone, the defector gains over the honest",
            "if all adopt it, does the gain survive?",
            "no: its own point collapses",
        ],
        "key_label": "A maxim tested at universal adoption",
        "concepts_intro": (
            "Games and the Social Contract supplied the many-player game. The test below reads "
            "two numbers off it, and the three ideas say what each number is for."
        ),
        "concepts": [
            ("A maxim is the rule behind an act",
             "The test is applied to the rule an agent acts on, stated with the act, the "
             "circumstance and the aim, and not to a single deed. In the lab the rule is the "
             "defecting choice and the practice it exploits is the cooperating one."),
            ("The defector’s gain is borrowed",
             "A liar is paid only because other people believe promises. That is why the payoff "
             "of lying rises with the number of others who keep their word, and why it can fall to "
             "nothing when none does."),
            ("A collapse is not the same as a worse outcome",
             "A maxim fails the first test when it defeats its own aim at universal adoption. "
             "Whether the world would be worse for everyone is a different question, and the "
             "lab’s other tiles answer it separately."),
        ],
        "read_title": "A maxim among ten players",
        "read_intro": "One maxim, its payoff table, and the two numbers the test reads from it.",
        "body": [
            ("p", "The consequentialist lessons ended with a forbidden list typed by hand: “The "
                  "Trolley Problem as a Decision Matrix” struck an act from the table and did not "
                  "say why it belonged there. The deontological theories are attempts to say "
                  "why. This lesson and the two after it each give one such account a checkable "
                  "structure: a maxim tested at universal adoption, a harm tested for whether the "
                  "good depends on it, and an omission tested as a cause."),
            ("p", "Kant’s first formulation of the categorical imperative says to act only on a "
                  "maxim you can at the same time will to be a universal law. The usual gloss, "
                  "“what if everyone did that?”, is where the trouble starts, because it sounds "
                  "like a forecast of consequences. The lab lets the two readings be told apart, "
                  "and this lesson takes the first of Kant’s two failures: the contradiction in "
                  "conception."),
            ("def", ("Maxim",
                     "A <strong>maxim</strong> is the rule an agent acts on, stated with the act, "
                     "the circumstance and the aim. Here it is: when I need money, I will promise "
                     "to repay it, knowing I will not, in order to be given it.")),
            ("p", "Model the practice of promising as a game with ten players. Each player "
                  "either keeps promises (cooperates) or makes false ones (defects). Let `k` be "
                  "the number of the other nine who keep their word. An honest promiser gets 2 "
                  "whatever the others do. A liar gets `5k/(n − 1)` with `n = 10`: nothing when "
                  "no one else is honest, because no promise is believed, and 5 when everyone else "
                  "is, because every promise is."),
            ("math", [
                "k     honest C(k)     liar D(k)",
                "0     2               0",
                "3     2               5/3",
                "6     2               10/3",
                "9     2               5",
            ]),
            ("p", "The test reads two numbers from this table. The first is the liar’s gain when "
                  "alone: every one of the other nine is honest, so the liar gets 5 where an honest "
                  "promiser gets 2, a gain of 3. The second is what the same choice is worth when "
                  "everyone makes it: with no one honest the liar gets 0, against the 2 that "
                  "honesty yields among honest people, a difference of −2. The lab prints the pair "
                  "as one line. Its equilibrium and replicator tiles are the ones Games and the "
                  "Social Contract read, and the test leaves them alone."),
            ("def", ("Contradiction in conception",
                     "A maxim has a <strong>contradiction in conception</strong> when, adopted "
                     "by everyone, the practice its act depends on could not exist and so the act "
                     "could not achieve its aim. A promise is believed only where promises are "
                     "usually kept; where everyone lies, there is nothing to exploit.")),
            ("p", "That is what the figure of 0 records, and it is why the test is not the "
                  "forecast it sounds like. A forecast would ask whether the world of universal "
                  "lying is worse. The test asks whether the liar can still do what the lie was "
                  "for. The lab’s social-optimum tile makes the difference visible: total welfare "
                  "among the ten is highest not when everyone is honest but with seven honest "
                  "and three liars, because in this table an honest promiser loses nothing to a "
                  "liar, and a liar among the honest collects 5 where honesty pays 2. That "
                  "stipulation is generous to the liar. A table in which the deceived lose would "
                  "move the optimum; it would not move the two figures the test reads, which are "
                  "taken where all nine others are honest and where none is. A sum-of-welfare "
                  "view therefore does not condemn the maxim as stated, and Kant’s test does."),
            ("example", ("Queue-jumping",
                         "Cutting in line pays only where others wait. Let a waiting person get "
                         "`2 + 2k/9` and a jumper `1 + 5k/9`, where `k` counts the others who wait. "
                         "Alone, the jumper gains 2. When all jump, the jumper gets 1 where the "
                         "orderly queue gave 4: the advantage was being ahead of people who waited, "
                         "and nobody is left to be ahead of.")),
            ("p", "The tax preset shows where the test is less clean. Evading a tax that funds "
                  "something everyone uses pays whatever the others do, and when all evade nothing "
                  "is funded. Nothing in that is a contradiction in conception, because a world "
                  "without the tax is perfectly conceivable. Kant’s second failure, the "
                  "contradiction in the will, fits better: the evader cannot coherently will a "
                  "world without the public good, since the evader wants it. The lab prints the "
                  "same two numbers for both failures, and which one a number means is "
                  "your reading, not its output."),
            ("p", "The limit belongs here. Kant did not compute anything, and the lab does so only "
                  "by treating the maxim’s point as a payoff you supply. It also cannot choose how "
                  "general the maxim should be: “I will lie to this person on this day” passes any "
                  "such test, and most of the test’s critics begin there."),
        ],
        "lab": ("choicekit", {
            "mode": "commons",
            "preset": "false-promise",
            "presets": [
                {"id": "false-promise", "label": "The false promise among ten",
                 "n": 10, "payC": "2", "payD": "5k/(n - 1)", "x0": "1/2",
                 "expect": {"cmDom": "neither", "cmOpt": "7 cooperate: total 77/3", "cmUniv": "alone +3, everyone −2"}},
                {"id": "tax", "label": "Evading a tax that funds a shared good",
                 "n": 10, "payC": "(k + 1)/2 - 2", "payD": "k/2", "x0": "1/2",
                 "expect": {"cmDom": "Defect dominates", "cmOpt": "all 10 cooperate: total 30", "cmUniv": "alone +3/2, everyone −3"}},
                {"id": "queue-jumping", "label": "Cutting in line",
                 "n": 10, "payC": "2 + 2k/9", "payD": "1 + 5k/9", "x0": "1/2",
                 "expect": {"cmDom": "neither", "cmOpt": "9 or 10 cooperate: total 40", "cmUniv": "alone +2, everyone −3"}},
            ],
        }),
        "steps_title": "Testing a maxim at universal adoption",
        "steps_intro": "Five steps. The third is where a story becomes a table, and every later "
                       "step reads from that table.",
        "steps": [
            ("State the maxim in full",
             "Write the act, the circumstance and the aim: “when I need money I will make a "
             "promise I do not mean, in order to be given it”. A maxim without its aim cannot be "
             "tested for whether the aim survives."),
            ("Name the practice it exploits",
             "Find what must be going on for the act to work. A false promise works because "
             "promises are usually kept. The cooperating choice is that practice."),
            ("Write the two payoffs",
             "Give the honest player’s payoff and the defector’s as functions of how many of the "
             "others keep the practice. Be explicit that these are numbers you chose."),
            ("Read the two figures",
             "The first is the defector’s gain when alone. The second is the defector’s payoff "
             "when no one keeps the practice, set against the honest payoff."),
            ("Say what the second figure means",
             "If the defector’s point vanishes, the maxim defeats itself in conception. If the "
             "world is merely worse, or the agent wants the practice, say which of the other "
             "failures it is."),
        ],
        "worked": {
            "title": "The liar among nine honest people",
            "intro": ["Ten players, `k` of the other nine keeping their word. Read the two "
                      "figures off the table."],
            "lines": [
                "honest player gets 2 whatever the others do",
                "liar gets 5k/9 when k of the other nine are honest",
                "alone among honest players:  liar 5, honest 2, gain 3",
                "when no one is honest:  liar 0, honest 2, gain minus 2",
                "no promise is believed, so the lie buys nothing",
            ],
            "after": [
                "The first figure is why a rule like this is tempting, and the second is why it "
                "cannot be a universal law. The lie gains only against a background of "
                "honesty that the lie, adopted generally, removes."
            ],
        },
        "quiz_title": "What the two figures show",
        "quiz": [
            {"q": "In the false-promise preset the lab prints that defecting gains 3 when alone. "
                  "What does that 3 measure?",
             "a": ["The liar’s whole payoff",
                   "The liar’s payoff minus an honest player’s, when the other nine are all honest",
                   "The harm done to the nine honest players together",
                   "The number of people who are deceived"],
             "c": 1,
             "why": "The liar gets 5 and an honest player 2, so the gain is 3. The liar’s whole "
                    "payoff is 5. The lab computes nothing about harm to others here, and nine "
                    "people being deceived is a count, not a payoff difference."},
            {"q": "The second figure is the liar’s payoff of 0 when no one is honest, against 2 for "
                  "honesty. Why does that count against the maxim on Kant’s test?",
             "a": ["Because 0 is less than the gain of 3 that the liar had alone",
                   "Because total welfare is lower when everyone lies than when everyone is honest",
                   "Because the lab marks a negative number as forbidden",
                   "Because once everyone lies the lie can no longer achieve what it was for"],
             "c": 3,
             "why": "The test asks whether the maxim can still do its work when universal. Comparing "
                    "0 with the earlier gain is not the point, a lower total is the consequence "
                    "reading the lesson sets aside, and the lab forbids nothing."},
            {"q": "Change the liar’s payoff to `3 + 5k/9` and leave the honest payoff at 2. "
                  "What does the lab print for the gain when everyone defects?",
             "a": ["−2, unchanged",
                   "+6",
                   "+1",
                   "+3"],
             "c": 2,
             "why": "With no one honest the liar gets 3 + 0 = 3 against the honest player’s 2, so "
                    "the difference is +1. The figure −2 belongs to the original payoff, and +6 is "
                    "the gain when alone among honest players. The new maxim survives universal "
                    "adoption, so it passes this test."},
            {"q": "What separates Kant’s contradiction in conception from a consequence test?",
             "a": ["It asks whether the maxim defeats its own aim when universal, not whether the "
                   "resulting world is worse",
                   "It uses no assumptions about what the agent wants",
                   "It is satisfied whenever the defector’s gain is positive",
                   "It compares totals over all ten players"],
             "c": 0,
             "why": "The first is the test. The agent’s aim is built in, so it does rest on an "
                    "assumption about what the agent wants. A positive gain is what makes the "
                    "maxim tempting, not what makes it pass, and comparing totals is the "
                    "consequence reading."},
        ],
        "mistakes": [
            ("Reading the test as a forecast of consequences",
             "If the test were “is the world of universal lying worse?”, the answer would come "
             "from the total, and the lab’s social-optimum tile shows the total is highest with a "
             "few liars in it. A sum of welfare does not condemn the maxim. The test condemns it "
             "for a different reason: when all adopt the rule, the lie buys nothing, so the rule "
             "cannot be what any agent is acting on."),
            ("Treating the two figures as a verdict",
             "The lab prints a gain when alone and a difference at universal adoption. Which "
             "failure that is, a contradiction in conception or in the will, depends on why the "
             "second figure matters, and the tax preset prints the same kind of number for a "
             "case that is not a contradiction in conception."),
            ("Forgetting that the maxim fixes the verdict",
             "State the maxim more narrowly and it passes, because a rule that mentions this "
             "person on this day is not one anyone could adopt widely enough to spoil. The lab "
             "tests the payoffs you give it; it cannot say how general to make the maxim."),
        ],
        "standard": ("Finish when you can compute the defector’s two figures and say which one "
                     "the test reads.",
                     "Given a maxim, you should be able to write it as a defecting choice with "
                     "payoffs, compute the gain when alone and the payoff when everyone adopts "
                     "it, and state whether the practice the act depends on survives."),
        "note": "The numbers here are stipulations, as every payoff in this course is. Kant would "
                "reject the idea that the test is a calculation at all. The lab shows the "
                "structure he describes, a rule that undermines the practice it feeds on, and "
                "leaves the question of whether that structure is what makes an act wrong to the "
                "reader.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "double-effect-means-and-side-effects",
        "title": "Double Effect, Means and Side Effects",
        "module": "Deontology",
        "one_line": "Reading “the harm is the means” as a dependence, and testing it by flipping "
                    "the harm in a causal model.",
        "summary": (
            "The doctrine of double effect allows a harm that is a side effect of a good act and "
            "forbids the same harm used as the means. The lab reads that distinction as "
            "dependence: write the case as structural equations, flip the harm, and see whether "
            "the good outcome changes. If it does the harm was the means, and if not it was a "
            "side effect."
        ),
        "key": [
            "flip the harm, recompute the good",
            "the good flips: the harm was the means",
            "the good stands: a side effect",
            "intentions are not in the equations",
        ],
        "key_label": "Means or side effect, as a dependence",
        "concepts_intro": (
            "Science, Induction and Causation gave the but-for test. The three ideas below move "
            "it from a cause of a fire to a harm that a good act brings with it."
        ),
        "concepts": [
            ("Means or side effect is a question about dependence",
             "Either the good outcome needs the harm, or it comes about without it. The test is "
             "to intervene on the harm and re-evaluate the good, which is the but-for test applied "
             "to a harm."),
            ("The equations carry the contested work",
             "Two cases get different verdicts only because they were written with different "
             "equations. The lab confirms that the models behave as written; whether they were "
             "written fairly is the part it cannot check."),
            ("Intention is not read",
             "Double effect is stated in terms of what the agent intends, but a causal model "
             "contains no mental states. What the lab tests is the dependence that the "
             "intention is supposed to track."),
        ],
        "read_title": "A harm, a good, and the equations between them",
        "read_intro": "The switch and the loop as small models, and a pair of bombers.",
        "body": [
            ("p", "The doctrine of double effect, usually traced to Aquinas, says an act with "
                  "both a good and a bad effect can be permissible when the act itself is "
                  "permissible, the bad effect is not intended as a means to the good, and the "
                  "good is proportionate to the harm. This lesson takes one clause: the bad "
                  "effect is not the means."),
            ("p", "Take the switch case from “The Trolley Problem as a Decision Matrix”. Let `L` "
                  "be “the lever is pulled”, `M` be “a man is on the side track”, `E` be “the "
                  "trolley goes onto the side track”, `H` be “the man is hit” and `F` be “the "
                  "five survive”. The model has three equations."),
            ("math", [
                "E = L",
                "H = E and M",
                "F = E",
            ]),
            ("p", "Everything is true in the actual case. To test whether the harm is the means, "
                  "ask what happens to the five if the harm is set to false while the rest of "
                  "the model is left alone. `F = E`, and `E` has not changed, so the five still "
                  "survive. The lab reports that the man’s being hit is not a but-for cause of "
                  "the five surviving, and not a cause at all. The five live because the trolley "
                  "left their track; the man’s death is something that happens on the way."),
            ("p", "Now the loop. The side track curves back to the main one, so the trolley "
                  "would reach the five anyway unless something stops it, and the man’s body "
                  "does. The first two equations are the same, but the third changes."),
            ("math", [
                "E = L",
                "H = E and M",
                "F = E and H",
            ]),
            ("def", ("Means, in the lab’s sense",
                     "A harm is a <strong>means</strong> to a good when the good depends on it: "
                     "set the harm to false, hold everything else as it was, and the good "
                     "fails. It is a <strong>side effect</strong> when the good comes about "
                     "whether or not the harm occurs.")),
            ("p", "Flip `H` in the loop and `F` becomes false: the five die. The harm is a "
                  "but-for cause of the good, so it is a means. The two cases have the same lever, "
                  "the same body count and the same outcome for the five. They differ in one "
                  "equation. In “The Trolley Problem as a Decision Matrix” the loop was put on the "
                  "forbidden list by hand. The structure says why someone who accepts the "
                  "doctrine would put it there."),
            ("example", ("Two bombers",
                         "A strategic bomber destroys a munitions factory, and civilians next to "
                         "it die; the war is shortened because the factory is gone. A terror "
                         "bomber kills the same number of civilians in order to break morale; the "
                         "war is shortened because morale breaks. In the first model the war’s "
                         "shortening does not depend on the civilian deaths, in the second it "
                         "does. The two presets print different verdicts for the same deaths and "
                         "the same benefit.")),
            ("p", "Three limits apply. The lab tests one clause. It does not test "
                  "whether the act is itself permissible or the good proportionate to the harm. "
                  "It also cannot say that a means is worse than a side effect, which is the "
                  "doctrine’s central claim and the one most often disputed; many people judge "
                  "the loop permissible, and the doctrine has to say they are wrong. And the "
                  "equations are a description of the case. Redescribe the switch so that the "
                  "five survive only if the man’s weight slows the trolley, and the verdict "
                  "changes with no change in anyone’s conduct."),
        ],
        "lab": ("argkit", {
            "mode": "structural",
            "preset": "switch",
            "presets": [
                {"id": "switch", "label": "The switch: the man is a side effect",
                 "equations": {"E": "L", "H": "E & M", "F": "E"},
                 "exogenous": {"L": 1, "M": 1}, "cause": "H", "effect": "F",
                 "expect": {"stButFor": "No", "stHP": "No", "stKind": "not a cause"}},
                {"id": "loop", "label": "The loop: the man stops the trolley",
                 "equations": {"E": "L", "H": "E & M", "F": "E & H"},
                 "exogenous": {"L": 1, "M": 1}, "cause": "H", "effect": "F",
                 "expect": {"stButFor": "Yes", "stHP": "Yes, holding nothing", "stKind": "but-for cause"}},
                {"id": "strategic-bomber", "label": "The strategic bomber: civilians die beside the target",
                 "equations": {"Z": "B", "C": "B & N", "W": "Z"},
                 "exogenous": {"B": 1, "N": 1}, "cause": "C", "effect": "W",
                 "expect": {"stButFor": "No", "stHP": "No", "stKind": "not a cause"}},
                {"id": "bomber", "label": "The terror bomber: civilians die to break morale",
                 "equations": {"C": "B", "M": "C", "W": "M"},
                 "exogenous": {"B": 1}, "cause": "C", "effect": "W",
                 "expect": {"stButFor": "Yes", "stHP": "Yes, holding nothing", "stKind": "but-for cause"}},
            ],
            "panel_title": "Flip the harm and recompute the good",
            "panel_intro": "Each preset is a small model with the harm as the candidate cause and "
                           "the good as the effect. Change an equation, such as the five’s survival, "
                           "to see the verdict move.",
        }),
        "steps_title": "Testing a harm for dependence",
        "steps_intro": "Four steps. The model is written before the test is run, and the verdict "
                       "belongs to the model.",
        "steps": [
            ("Name the harm and the good",
             "Pick one variable for the harm and one for the good it accompanies. They must be "
             "events in the model, not descriptions of the agent."),
            ("Write the equations from the case",
             "Say what each variable depends on, as the case is described. Whether the good needs "
             "the harm is decided here, by what you write."),
            ("Flip the harm and re-evaluate",
             "Set the harm to its opposite, leave the rest, and read whether the good changes. "
             "That is the but-for test."),
            ("Name the clause tested and the ones not",
             "A harm that is a means fails the clause that the harm not be the means. Whether "
             "the act is permissible and the good proportionate are separate questions."),
        ],
        "worked": {
            "title": "The same five lives, two equations",
            "intro": ["Both models have the harm true and the five surviving. Flip the harm."],
            "lines": [
                "switch:  F = E       flip H, F stays 1   side effect",
                "loop:    F = E and H  flip H, F goes to 0  means",
                "same lever, same man, same five",
                "the difference is one equation",
            ],
            "after": [
                "In the switch the five are saved by the turning of the trolley, and the man is "
                "hit afterwards. In the loop they are saved by the man’s being hit. The lab "
                "reports the first as not a cause and the second as a but-for cause, which is "
                "the distinction the doctrine draws and nothing more."
            ],
        },
        "quiz_title": "What the flip shows",
        "quiz": [
            {"q": "In the switch preset the lab reports that the man’s being hit is not a but-for "
                  "cause of the five surviving. What follows?",
             "a": ["The act of pulling the lever is permissible",
                   "The man does not die",
                   "The five survive whether or not he is hit, so he is a side effect by this test",
                   "The lever is not a cause of the five surviving"],
             "c": 2,
             "why": "Setting the harm to false leaves the good as it was, which is the side-effect "
                    "verdict. The test says nothing about permissibility, he is hit in the model "
                    "as actually run, and the lever is a cause of the trolley’s turning."},
            {"q": "Which equation makes the harm a means in the loop preset?",
             "a": ["`E = L`, the trolley goes onto the side track when the lever is pulled",
                   "`H = E and M`, the man is hit when the trolley reaches him",
                   "`L` and `M` both being true",
                   "`F = E and H`, the five survive only if the trolley is diverted and the man "
                   "is hit"],
             "c": 3,
             "why": "Only the last makes the five’s survival depend on the man’s being hit. The "
                    "first two are identical in the switch preset, where the harm is not a means, "
                    "and the inputs are the same in both."},
            {"q": "The strategic and terror bombers kill the same civilians and shorten the war by "
                  "the same amount. How does the lab tell them apart?",
             "a": ["By what each pilot privately wants",
                   "By whether the war’s shortening depends on the civilians’ deaths",
                   "By how many civilians die",
                   "By whether the war is shortened at all"],
             "c": 1,
             "why": "The models contain no wants. The deaths and the shortening are the same in "
                    "both presets. What differs is the path: the factory’s destruction shortens the "
                    "war in the first, and the broken morale does in the second."},
            {"q": "Someone rewrites the switch so that `F = E and H`, keeping everything else. "
                  "What does the lab now report?",
             "a": ["The man’s being hit is a but-for cause of the five surviving, as in the loop",
                   "Nothing changes, because the case is still called the switch",
                   "The lever is no longer a cause",
                   "The model is refused"],
             "c": 0,
             "why": "The verdict follows the equations, and the label is not an input. With that "
                    "equation the model is the loop. The lever is still a cause of the trolley "
                    "turning, and the model is well formed."},
        ],
        "mistakes": [
            ("Thinking double effect is about intentions the lab can read",
             "The equations contain no mental state. Two agents with opposite intentions in the "
             "same loop get identical tiles, because the tiles read what depends on what. "
             "Dependence is the observable thing an intention to use the harm is supposed to "
             "go with, since a person who sees that the good needs the harm cannot pursue the "
             "good without relying on the harm. Whether that is all the doctrine means is part "
             "of what is disputed."),
            ("Treating a side effect as a harm that does not matter",
             "In the switch the man is hit and dies, and the lab’s “not a cause of the good” says "
             "nothing about how much his death weighs. The proportionality clause, which the lab "
             "does not test, is where that is argued."),
            ("Reading the verdict off the case instead of the model",
             "The case does not come with equations. Rewrite `F = E` as `F = E and H` and the "
             "verdict moves from side effect to means with no change in the world. The "
             "classification is only as good as the description it was computed from."),
        ],
        "standard": ("Finish when you can write a case as equations and say which clause the "
                     "flip tests.",
                     "Given a case with a good and a harm, you should be able to write the "
                     "structural equations, intervene on the harm, report whether the good "
                     "depends on it, and name the clauses of the doctrine the test leaves "
                     "unchecked."),
        "note": "The Boolean models here have no probabilities, so a harm that makes a good merely "
                "more likely is not covered. Extending the test to risk is a real open problem "
                "for the doctrine, and no lab in this course settles it.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "doing-allowing-and-omissions-as-causes",
        "title": "Doing, Allowing and Omissions as Causes",
        "module": "Deontology",
        "one_line": "Modelling a rescue not performed as a variable, and testing whether the "
                    "omission makes a difference to the death.",
        "summary": (
            "An omission is a rescue that was not performed, and in a causal model it is a variable "
            "like any other. Flip it, and the death flips: the omission is a but-for cause. Two "
            "would-be rescuers change the structure and not the answer, and whatever separates "
            "doing from allowing, it is not that one is a cause and the other is not."
        ),
        "key": [
            "an omission: a rescue variable set to 0",
            "flip it: if the death flips, it is but-for",
            "out of reach: flipping willingness is idle",
            "doing and allowing both depend on you",
        ],
        "key_label": "An omission as a cause",
        "concepts_intro": (
            "The previous lesson tested a harm for dependence. The same test now applies to "
            "something that did not happen."
        ),
        "concepts": [
            ("An omission is a value, not a gap",
             "The rescue that was available and not performed is a variable whose actual value "
             "is 0. A model can flip it to 1 and recompute, so there is nothing about an omission "
             "that the but-for test cannot handle."),
            ("Availability lives in the equations",
             "Not everything left undone is a cause. The lifeguard’s unwillingness matters only "
             "because the lifeguard was in reach, and the equations say so by making the rescue "
             "depend on both."),
            ("A causal verdict is not a moral one",
             "That an omission is a cause shows that the distinction between doing and allowing "
             "cannot rest on cause. It does not show the two are equally bad."),
        ],
        "read_title": "A lifeguard who did not go in",
        "read_intro": "One drowning, three ways the rescue can fail to happen, and what the test says "
                      "about each.",
        "body": [
            ("p", "Many people hold that killing is worse than letting die, and the commonest "
                  "support is a claim about cause: the person who pushes causes the drowning, "
                  "the person who watches only fails to prevent it. The claim is easy to test, "
                  "because the but-for test does not care whether the cause is an event or an "
                  "absence."),
            ("p", "Let `L` be “the lifeguard is in reach”, `W` be “the lifeguard is willing”, `R` "
                  "be “the swimmer is rescued” and `D` be “the swimmer drowns”. The rescue "
                  "happens only if the lifeguard is both in reach and willing, and the swimmer "
                  "drowns when there is no rescue."),
            ("math", [
                "R = L and W",
                "D = not R",
            ]),
            ("p", "In the case as it happened the lifeguard is in reach and unwilling: `L = 1, W = 0`. So `R = 0` "
                  "and `D = 1`. Take the rescue not performed, `R`, as the candidate cause and "
                  "the drowning as the effect. Setting `R` to 1 makes `D` 0, and the lab reports "
                  "a but-for cause. The omission is a cause in exactly the sense that a struck "
                  "match is a cause of a fire in “Counterfactual Causation and the But-For "
                  "Test”."),
            ("def", ("Omission",
                     "An <strong>omission</strong> is the absence of an act that was available. "
                     "In a structural model it is a variable whose actual value is 0, and it is "
                     "tested for causation like any other variable: flip it and recompute.")),
            ("p", "The obvious objection is that this proves too much. Everyone has failed to "
                  "rescue every swimmer in the world. The model answers it, because availability "
                  "is an equation and not a footnote. If the lifeguard is out of reach, `L = 0`, "
                  "the rescue does not happen whether or not the lifeguard is willing, and "
                  "flipping `W` changes nothing. Of everything that was not done, the lab "
                  "selects what was available."),
            ("p", "Now two lifeguards. If either would suffice, `R = W1 or W2`, and both are "
                  "unwilling, flipping either one alone produces a rescue. Each omission is a "
                  "but-for cause, so the thought that neither is responsible because the other "
                  "could have gone is not one the structure supports. If instead both are "
                  "needed, `R = W1 and W2`, as when two people must carry a boat, flipping one "
                  "alone changes nothing and the lab reports a joint cause: neither is a "
                  "but-for cause and each is a cause together with the other."),
            ("example", ("The shallow pond",
                         "A child is drowning in a pond shallow enough to wade into, at the cost "
                         "of ruined shoes. Let `W` be “you wade in”, `A` be “the child is within "
                         "reach”, `R = W and A`, `D = not R` and `M = R`, where `M` is the "
                         "ruined shoes. Flipping `W` flips both the drowning and the shoes. The "
                         "lab shows the dependence of the death on your choice; whether the "
                         "shoes outweigh it is not a quantity it computes.")),
            ("p", "A pusher’s act is a but-for cause of the drowning too. So if pushing is worse "
                  "than watching, the reason is not that the first is a cause and the second "
                  "is not. Candidates are that the pusher initiates the harm and the watcher "
                  "does not, that duties not to harm are stronger than duties to aid, or that "
                  "the cost to the rescuer differs. Each is a premise about what matters, and "
                  "none of them is computed here."),
        ],
        "lab": ("argkit", {
            "mode": "structural",
            "preset": "lifeguard",
            "presets": [
                {"id": "lifeguard", "label": "The lifeguard who was there and unwilling",
                 "equations": {"R": "L & W", "D": "~R"},
                 "exogenous": {"L": 1, "W": 0}, "cause": "R", "effect": "D",
                 "expect": {"stButFor": "Yes", "stHP": "Yes, holding nothing", "stKind": "but-for cause"}},
                {"id": "out-of-reach", "label": "A willing lifeguard out of reach",
                 "equations": {"R": "L & W", "D": "~R"},
                 "exogenous": {"L": 0, "W": 1}, "cause": "W", "effect": "D",
                 "expect": {"stButFor": "No", "stHP": "No", "stKind": "not a cause"}},
                {"id": "two-rescuers", "label": "Two lifeguards, either would do, both unwilling",
                 "equations": {"R": "W1 | W2", "D": "~R"},
                 "exogenous": {"W1": 0, "W2": 0}, "cause": "W1", "effect": "D",
                 "expect": {"stButFor": "Yes", "stHP": "Yes, holding nothing", "stKind": "but-for cause"}},
                {"id": "two-needed", "label": "Two people needed to launch the boat, both unwilling",
                 "equations": {"R": "W1 & W2", "D": "~R"},
                 "exogenous": {"W1": 0, "W2": 0}, "cause": "W1", "effect": "D",
                 "expect": {"stButFor": "No", "stHP": "No", "stKind": "joint cause with W2"}},
                {"id": "shallow-pond", "label": "The shallow pond, and the cost of the shoes",
                 "equations": {"R": "W & A", "D": "~R", "M": "R"},
                 "exogenous": {"W": 0, "A": 1}, "cause": "W", "effect": "D",
                 "expect": {"stButFor": "Yes", "stHP": "Yes, holding nothing", "stKind": "but-for cause"}},
            ],
            "panel_title": "Flip the omission and recompute the death",
            "panel_intro": "Each preset is a rescue that did not happen. The candidate cause is the "
                           "omission and the effect is the drowning. Change a willingness to 1 to "
                           "see the rescue and the death move.",
        }),
        "steps_title": "Testing an omission",
        "steps_intro": "Four steps. The second decides everything, because it is where availability "
                       "is written down.",
        "steps": [
            ("Name the rescue as a variable",
             "Give the act that was not performed its own letter, with actual value 0, and give "
             "the harm that followed its own letter."),
            ("Write what the rescue depends on",
             "Say what had to be true for the rescue to happen: being in reach, being willing, "
             "having help. These are the conditions that separate an available act from a mere "
             "possibility."),
            ("Flip the omission",
             "Set the rescue, or the willingness behind it, to its opposite and recompute. A "
             "change in the harm makes the omission a but-for cause."),
            ("Check the other agents",
             "If someone else could have rescued, write that in. Either one would do, and each is "
             "a but-for cause, or both are needed, and the cause is joint."),
        ],
        "worked": {
            "title": "The lifeguard, then a second lifeguard",
            "intro": ["The drowning depends on the rescue, and the rescue on who is willing."],
            "lines": [
                "R = L and W,  D = not R,  L = 1, W = 0",
                "actual:  R = 0, D = 1",
                "flip R to 1:  D = 0   so R is a but-for cause",
                "two lifeguards, either would do:  each is a but-for cause",
                "both needed:  neither alone, a joint cause",
            ],
            "after": [
                "None of this says the lifeguard did wrong. It says the drowning depended on "
                "the lifeguard’s unwillingness in the same sense that a fire depends on a match, "
                "so any account of why failing to rescue is different from drowning someone has "
                "to look elsewhere than cause."
            ],
        },
        "quiz_title": "What the flip shows about an omission",
        "quiz": [
            {"q": "In the lifeguard preset the lab reports the rescue not performed is a but-for "
                  "cause of the drowning. What does that show?",
             "a": ["That the lifeguard acted wrongly",
                   "That the drowning would not have occurred had the rescue been performed",
                   "That the lifeguard pushed the swimmer",
                   "That the lifeguard was the only person who could help"],
             "c": 1,
             "why": "A but-for cause is a condition without which the effect would not have "
                    "occurred. It makes no claim about right and wrong, nothing in the model "
                    "involves a push, and being the only person who could help is a different "
                    "feature of the case."},
            {"q": "In the out-of-reach preset the lifeguard is willing but out of reach. Flipping "
                  "willingness changes nothing. Why does the objection that omissions “prove "
                  "too much” fail?",
             "a": ["Because the lab refuses to test omissions",
                   "Because willingness is always irrelevant",
                   "Because the equations make the rescue depend on being in reach, so only "
                   "an available act is selected",
                   "Because the swimmer does not drown"],
             "c": 2,
             "why": "The rescue needs both conditions, so an act out of reach is not a cause "
                    "however willing the agent. The lab tests omissions without difficulty, "
                    "willingness matters when the lifeguard is in reach, and the swimmer does "
                    "drown, since the rescue still fails."},
            {"q": "Two lifeguards are each unwilling and either alone would have sufficed. What "
                  "does the lab report for one of them?",
             "a": ["A joint cause with the other",
                   "Not a cause, since the other could have gone",
                   "A but-for cause",
                   "The model is refused"],
             "c": 2,
             "why": "Flipping either willingness alone produces a rescue, so each omission is a "
                    "but-for cause. Joint causation is the verdict when both are needed, and "
                    "the possibility that the other could have gone is already in the equation."},
            {"q": "Both omissions are causes of the drowning, and so is a push. What follows "
                  "about killing and letting die?",
             "a": ["Any difference in their wrongness cannot be explained by one being a cause "
                   "and the other not",
                   "They are equally wrong",
                   "Neither is ever wrong",
                   "The difference is that only the push is a but-for cause"],
             "c": 0,
             "why": "The lab removes one explanation, the causal one, and leaves others. It "
                    "does not show equal wrongness or the absence of wrongness, and it reports a "
                    "but-for cause for both."},
        ],
        "mistakes": [
            ("Thinking an omission cannot be a cause",
             "A rescue not performed is a variable with value 0, and flipping it to 1 turns the "
             "drowning off. The lifeguard preset reports a but-for cause, by the same test "
             "that reports a struck match as the cause of a fire. What an omission lacks is a "
             "process, some transfer of energy from cause to effect, and the test does not ask "
             "for one. A philosopher who insists that it should is holding that dependence is "
             "not enough for causation, which is a position with a price: it must then say what "
             "the match has that the lifeguard lacks, since the drowning depends on each in "
             "the same way."),
            ("Spreading the responsibility until it vanishes",
             "With two lifeguards, either of whom would have sufficed, the lab reports each "
             "omission as a but-for cause. The presence of another person who could have helped "
             "does not remove anyone’s dependence on their own choice."),
            ("Treating the causal verdict as the moral one",
             "The lab shows that the drowning depended on the omission. It does not show the "
             "omission was wrong, or as wrong as a push. The cost of the shoes in the pond preset "
             "is on the page and the lab cannot weigh it."),
        ],
        "standard": ("Finish when you can model an omission and say what the flip shows.",
                     "Given a rescue that was not performed, you should be able to write it as a "
                     "variable, state what it depends on, flip it, report whether it is a "
                     "but-for or joint cause, and say what the verdict leaves open."),
        "note": "The Boolean model treats willingness as a switch. Real omissions come in degrees "
                "of effort and cost, and a rescue that was possible only at great risk to the "
                "rescuer is a different case that the model would need a new variable to hold.",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "moral-dilemmas-and-deontic-consistency",
        "title": "Moral Dilemmas and Deontic Consistency",
        "module": "Deontology",
        "one_line": "Writing a dilemma as a set of sentences that cannot all hold, and naming "
                    "the principle each way out gives up.",
        "summary": (
            "A moral dilemma is a situation in which you ought to do each of two things and cannot "
            "do both. Written as a set of sentences, two oughts, a principle that oughts combine, "
            "a principle that ought implies can, and a fact of inability, it has no model, and "
            "all five sentences are needed for the clash. Each way out rejects exactly one."
        ),
        "key": [
            "two oughts, and you cannot do both",
            "agglomeration: oughts combine",
            "ought implies can",
            "five sentences, no model: drop one",
        ],
        "key_label": "A dilemma as an inconsistent set",
        "concepts_intro": (
            "Arguments and Validity gave the consistency check and the smallest subset that "
            "cannot be true together. The dilemma is a case for both."
        ),
        "concepts": [
            ("Not knowing what to do is a different thing",
             "A dilemma in this sense is not uncertainty. Every sentence in the set can be "
             "settled, and the set is still unsatisfiable. The conflict is among the principles, "
             "not in the agent’s knowledge."),
            ("A set can fail in one place or in many",
             "A smallest inconsistent subset is a set that cannot hold but each of whose parts "
             "can. If it is the whole set, every sentence is doing work, and any one sentence "
             "given up restores a model."),
            ("Every exit has a price",
             "The set is consistent once a sentence is rejected, but each rejection has a "
             "cost, and the genuine dilemma is the case where none is free."),
        ],
        "read_title": "Two promises at six o’clock",
        "read_intro": "A dilemma written out, its smallest inconsistent subset, and four ways out.",
        "body": [
            ("p", "You have promised Ana to be at her door at six, and promised Bo to be at his, "
                  "on the other side of town, at the same hour. Each promise gives you an "
                  "obligation, and you cannot keep both. Philosophers who call this a moral "
                  "dilemma mean something stronger than that it is hard: that you ought to do "
                  "each, you cannot do both, and neither obligation overrides the other."),
            ("def", ("Moral dilemma",
                     "A <strong>moral dilemma</strong> is a situation in which an agent ought to "
                     "do each of two actions, cannot do both, and has no further reason that "
                     "makes one of the oughts lapse.")),
            ("p", "The standard argument that dilemmas are impossible uses two principles. "
                  "Write `a` for “you ought to keep your promise to Ana”, `b` for “you ought to "
                  "keep your promise to Bo”, `c` for “you ought to keep both” and `d` for “you can "
                  "keep both”. The five sentences are below."),
            ("math", [
                "1   a                 you ought to keep the promise to Ana",
                "2   b                 you ought to keep the promise to Bo",
                "3   (a and b) → c      agglomeration: oughts combine",
                "4   c → d              ought implies can",
                "5   not d              you cannot keep both",
            ]),
            ("p", "The lab finds no assignment of truth values that makes all five true. Sentences "
                  "1, 2 and 3 give `c`; with 4 that gives `d`; and 5 says `not d`. The smallest "
                  "inconsistent subset is all five, so none of them is idle: take any one away and "
                  "a model exists. This is the sense in which a dilemma is a set that cannot be "
                  "true together, and it is a fact about the principles and the situation, not "
                  "about the agent’s ignorance."),
            ("p", "The set is also why people disagree about dilemmas, because each of the "
                  "four ways of restoring consistency is held by someone. Williams keeps both "
                  "oughts: the remorse you owe whichever promise you break shows, he argues, that "
                  "the obligation you set aside did not lapse, and what he gives up is "
                  "agglomeration, since from “you ought to keep each” it does not follow that "
                  "“you ought to keep both”, and the combined obligation is never formed. A "
                  "second camp keeps agglomeration and gives up ought-implies-can: you ought to "
                  "keep both though you cannot, and an obligation can outrun what the situation "
                  "allows. A third denies one of the first two sentences, holding that when two "
                  "obligations conflict one of them lapses, so there was never a dilemma; that is "
                  "the orthodox view, and standard deontic logic is built to deliver it. The "
                  "fourth says you can keep both after all, by a plan not yet considered, and so "
                  "denies the situation that made it a dilemma."),
            ("p", "Marcus adds a point the lab makes visible. Delete sentence 5 and the "
                  "remaining four have a model, so the principles were never inconsistent with "
                  "one another; the clash needed the world to supply `not d`. On her view that "
                  "is what a dilemma is, a consistent code meeting an unlucky situation, and it "
                  "is why she holds there is a further obligation to arrange one’s life so that "
                  "such situations are rare."),
            ("example", ("The cost of each exit",
                         "Reject agglomeration, and you have two separate obligations and no "
                         "obligation to meet them jointly, so it is unclear what a person is doing "
                         "who fails one. Reject ought-implies-can, and an obligation no longer "
                         "guides action, since it can demand the impossible. Drop one of the "
                         "oughts, and the guilt you feel at breaking the promise you set aside "
                         "has nothing to be about. The lab shows the set is consistent in each "
                         "case; it does not say which price is the lowest.")),
            ("p", "The lab sees four letters. That `c` stands for "
                  "the conjunction of what `a` and `b` say is not something it can tell, which is "
                  "why agglomeration appears as a sentence in the set. Standard deontic logic "
                  "builds in agglomeration and ought-implies-can, and so makes dilemmas "
                  "inconsistent by design. That is itself a position, and the set above lets it be "
                  "stated rather than assumed."),
        ],
        "lab": ("argkit", {
            "mode": "consistency",
            "preset": "dilemma",
            "presets": [
                {"id": "dilemma", "label": "Both oughts, agglomeration, ought implies can, and inability",
                 "sentences": ["a", "b", "(a & b) -> c", "c -> d", "~d"],
                 "expect": {"coVerdict": "Inconsistent", "coMis": "{1, 2, 3, 4, 5}", "coWitness": "none"}},
                {"id": "drop-agglomeration", "label": "Williams: oughts do not combine",
                 "sentences": ["a", "b", "c -> d", "~d"],
                 "expect": {"coVerdict": "Consistent", "coMis": "none", "coWitness": "a=T b=T c=F d=F"}},
                {"id": "drop-can", "label": "Ought does not imply can",
                 "sentences": ["a", "b", "(a & b) -> c", "~d"],
                 "expect": {"coVerdict": "Consistent", "coMis": "none", "coWitness": "a=T b=T c=T d=F"}},
                {"id": "drop-an-ought", "label": "One obligation lapses",
                 "sentences": ["a", "(a & b) -> c", "c -> d", "~d"],
                 "expect": {"coVerdict": "Consistent", "coMis": "none", "coWitness": "a=T b=F c=F d=F"}},
            ],
            "panel_title": "Delete a sentence and look for a model",
            "panel_intro": "The set in the text is the first preset. Use the drop menu to delete one "
                           "sentence at a time and read whether a model appears.",
        }),
        "steps_title": "Writing a dilemma as a set",
        "steps_intro": "Five steps. The fourth is a table and the fifth is a choice, and the lab "
                       "only does the fourth.",
        "steps": [
            ("State the two oughts",
             "Give each action its own sentence saying you ought to do it, with a letter each."),
            ("Add the principles the argument uses",
             "Write the agglomeration principle and ought-implies-can as conditionals over the "
             "letters. If the argument uses a third principle, add it too."),
            ("Add the fact of inability",
             "Write that you cannot do both. This is a claim about the situation, not a principle."),
            ("Check the set for a model",
             "The lab reports that no assignment makes all the sentences true, and which "
             "sentences are the smallest subset that cannot. If that is all of them, each "
             "is needed."),
            ("Choose the sentence to give up, and name its price",
             "Delete one sentence at a time and see which deletion restores a model. Then say "
             "what the deletion costs, because the dilemma is genuine only if each exit does."),
        ],
        "worked": {
            "title": "Ana and Bo, five sentences",
            "intro": ["Write the situation, find the smallest set that cannot hold, then try each "
                      "exit."],
            "lines": [
                "1 a   2 b   3 (a and b) imply c   4 c implies d   5 not d",
                "all five together:  no model",
                "smallest inconsistent set:  1, 2, 3, 4, 5",
                "drop 3:  a model exists   drop 4:  a model exists",
                "drop 1 or 2:  a model exists   drop 5:  a model exists",
            ],
            "after": [
                "Each deletion works, which is exactly the problem. A dilemma is real only if "
                "every sentence is held for good reason, so that giving any one up has a cost "
                "someone will not pay."
            ],
        },
        "quiz_title": "What the set shows",
        "quiz": [
            {"q": "The lab reports the smallest inconsistent subset of the dilemma set is all "
                  "five sentences. What does that mean?",
             "a": ["Four of the five can be true together, so the set is consistent",
                   "The first two sentences are false",
                   "Removing any one sentence leaves a set that has a model",
                   "The agent cannot know what to do"],
             "c": 2,
             "why": "If a smaller part were inconsistent it would be the smallest subset. All five "
                    "being needed means every part is consistent and every deletion restores a "
                    "model. The set as a whole is inconsistent, no sentence is shown false, and "
                    "the lab says nothing about the agent’s knowledge."},
            {"q": "Williams says oughts do not combine. Which sentence of the original set does "
                  "the lab’s Williams preset delete, and what does it report?",
             "a": ["Sentence 3, agglomeration, and the set is consistent",
                   "Sentence 4, ought implies can, and the set is consistent",
                   "Sentence 3, agglomeration, and the set is still inconsistent",
                   "None, since agglomeration is not in the set"],
             "c": 0,
             "why": "The sentence at issue is the third, and removing it leaves a consistent "
                    "set with one model. Sentence 4 is the ought-implies-can exit, and deleting 3 "
                    "does not leave an inconsistency, since `c` is no longer derived. "
                    "Agglomeration is in the set as the third sentence."},
            {"q": "Someone keeps both oughts and agglomeration, insists the dilemma is real, and "
                  "refuses to say you can keep both. Which sentence must they reject?",
             "a": ["`not d`, you cannot keep both",
                   "`a`, you ought to keep the first promise",
                   "`(a and b) → c`, agglomeration",
                   "`c → d`, ought implies can"],
             "c": 3,
             "why": "With sentences 1, 2 and 3 kept, `c` follows, and with 5 kept, `d` is false; "
                    "the only sentence left to deny is the fourth. That is the exit on which an "
                    "obligation can demand what the situation does not allow. Agglomeration is "
                    "Williams’s target, and denying the inability is the friend’s move in the "
                    "next question."},
            {"q": "A friend says the dilemma is only apparent, because you could phone Ana and "
                  "reach her by seven. Which sentence is the friend denying?",
             "a": ["`a`",
                   "`not d`",
                   "`c → d`",
                   "`b`"],
             "c": 1,
             "why": "The proposal is that doing both is possible by another plan, which is the "
                    "denial of the inability. The friend may be right about the case, and then "
                    "there is no dilemma to analyse, which is what a consistent set says."},
        ],
        "mistakes": [
            ("Thinking a dilemma is not knowing what to do",
             "Every sentence in the set is settled: you know what each promise requires and you "
             "know you cannot keep both. The set still has no model, and that is the dilemma. "
             "Uncertainty would be a case in which one of the sentences has not yet been "
             "settled, and the lab does not need to know which sentences are true to report "
             "that these five cannot be true together."),
            ("Thinking an inconsistent set shows the situation is impossible",
             "The set is about principles and a situation. Someone who holds all five holds "
             "something inconsistent, and the repair is to give up a sentence, not to deny that "
             "you made two promises. Whether a real dilemma remains depends on which "
             "sentence you give up."),
            ("Expecting the lab to pick the exit",
             "Each of the four exits is consistent, and consistency is all the lab checks. The "
             "price of each is a judgment about what the ought is for, and that judgment is the "
             "argument."),
        ],
        "standard": ("Finish when you can write a dilemma as a set and name the sentence each "
                     "exit rejects.",
                     "Given two conflicting obligations, you should be able to write the five "
                     "sentences, report that they have no model, name the smallest inconsistent "
                     "subset, and say for each deletion which principle was rejected and what "
                     "that costs."),
        "note": "A fuller treatment would use a logic of obligation with its own axioms. Here "
                "the principles are written as sentences, so each can be deleted separately, which "
                "is the point of the exercise and also its limit.",
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "virtue-ethics-and-the-function-argument",
        "title": "Virtue Ethics and the Function Argument",
        "module": "Virtue and method",
        "one_line": "Formalising Aristotle’s argument from function, finding the premise it needs, "
                    "and saying where the lab’s reach ends.",
        "summary": (
            "Aristotle argues that the human good is a certain kind of activity because it is what "
            "performing the human function well comes to. Written as three sentence letters, the "
            "argument as stated has a counterexample row, and the lab finds the premise that "
            "closes it. The rest of virtue ethics, including the mean, has no structure the lab "
            "can test, and the lesson says so."
        ),
        "key": [
            "good = performing the function well",
            "the human function is reasoning",
            "as stated: a counterexample row",
            "the added premise carries the weight",
        ],
        "key_label": "A function argument and its missing premise",
        "concepts_intro": (
            "Virtue ethics is a family of views about character. The argument below is one "
            "piece of it that is also an argument in the sense this course tests."
        ),
        "concepts": [
            ("The argument is an enthymeme",
             "An enthymeme is an argument with a premise left unstated. The function argument "
             "is usually told in three steps, and one of the steps between them is never "
             "written down."),
            ("Validity finds the missing premise",
             "The counterexample row names the case that the stated premises allow and the "
             "conclusion forbids. The premise that rules it out is the one to examine."),
            ("The argument is a bridge from is to ought",
             "A claim about what a kind of thing does leads to a claim about what is good for "
             "it. The gap in “Is and Ought” is the one that the first premise has to close."),
        ],
        "read_title": "From function to good",
        "read_intro": "One argument, its counterexample row, and two ways it can be completed.",
        "body": [
            ("p", "Virtue ethics asks what kind of person to be before it asks what act to do. Its "
                  "oldest argument for a view about the good life is Aristotle’s function "
                  "argument. A flute player’s good, it says, lies in playing the flute well, "
                  "and an eye’s in seeing well. A thing’s good is performing its function well. "
                  "What is distinctive of human beings, shared with neither plants nor animals, "
                  "is reasoning. So the human good is reasoning well."),
            ("p", "Write three sentence letters. `f` is “reasoning is the human function”, `g` is "
                  "“the human good is reasoning well” and `r` is “reasoning is what sets human "
                  "beings apart from other living things”. The argument as told gives two "
                  "premises: `f → g`, that if reasoning is the human function then the human good "
                  "is reasoning well, and `r`. The conclusion is `g`."),
            ("p", "The lab builds the eight rows and finds one on which both premises are true "
                  "and the conclusion false: `f = F, g = F, r = T`. On that row reasoning "
                  "distinguishes humans, and it is not the human function, so the first premise "
                  "is true because its antecedent is false, and the human good is not reasoning "
                  "well. Nothing in the stated premises connects what is distinctive of humans "
                  "to what is their function."),
            ("math", [
                "f  g  r  |  f → g   r  |  g",
                "F  F  T  |  T       T  |  F   (the counterexample row)",
                "any other row with both premises true has g true",
            ]),
            ("def", ("Enthymeme",
                     "An <strong>enthymeme</strong> is an argument that relies on a premise it "
                     "does not state. Making the premise explicit does not make the argument "
                     "sound. It makes visible the thing a critic should question.")),
            ("p", "The missing premise is `r → f`: whatever sets a kind apart is its function. "
                  "With it the argument is valid, and the lab finds no counterexample row. "
                  "Aristotle supplies something like it, saying that a function is what a thing "
                  "does that nothing else does. That is the premise a critic should look at. "
                  "Laughing also sets humans apart, and few would say that laughing well is "
                  "the human good, so distinctiveness alone looks too weak to fix a function."),
            ("p", "The argument has a second gap, on the other side. Strip it to `r` and "
                  "`r → f`, so that it ends with the claim that reasoning is the function, "
                  "and ask whether it reaches `g`. The lab finds it does not: the row `r = T, "
                  "f = T, g = F` is a counterexample. Here `f → g` is the premise that is "
                  "missing, and it is the bridge from a claim about what a thing does to a claim "
                  "about what is good for it, the step that “Is and Ought” asks everyone to "
                  "price. A defender says that for a thing with a function, being good just is "
                  "performing the function well. A critic asks why we should care about the "
                  "function of a kind we belong to, which is the open question again."),
            ("example", ("A tool and a person",
                         "The premise sounds compelling for a knife, whose function was given by "
                         "someone who made it, and a good knife is one that cuts well. It sounds "
                         "less compelling for a person, whose function, if there is one, was not "
                         "assigned. The argument needs `f → g` to hold for kinds whose function "
                         "comes from nature or nothing, and the lab can say the argument is valid "
                         "with it and cannot say whether it holds.")),
            ("p", "The lab does not reach further. The doctrine "
                  "of the mean, that each virtue sits between a deficiency and an excess, the role "
                  "of practical wisdom in finding it, and the way character is formed by habit "
                  "have no premises and conclusion to test. Any widget offered for them would be "
                  "decorative, so the lesson leaves them alone, along with the history of "
                  "who held which view."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "show": "all",
            "preset": "function",
            "presets": [
                {"id": "function", "label": "The function argument as told",
                 "premises": ["f -> g", "r"], "conclusion": "g",
                 "expect": {"vaVerdict": "Invalid", "vaCounter": "1"}},
                {"id": "function-bridged", "label": "With distinctive-means-function added",
                 "premises": ["f -> g", "r", "r -> f"], "conclusion": "g",
                 "expect": {"vaVerdict": "Valid", "vaCounter": "0"}},
                {"id": "enthymeme", "label": "With the function-to-good step left out",
                 "premises": ["r", "r -> f"], "conclusion": "g",
                 "expect": {"vaVerdict": "Invalid", "vaCounter": "1"}},
            ],
        }),
        "steps_title": "Completing an enthymeme",
        "steps_intro": "Five steps. The counterexample row is the guide, and the premise that "
                       "excludes it is the answer.",
        "steps": [
            ("Give each claim a letter",
             "Write the argument in standard form with one letter per simple sentence. Keep a "
             "claim about a kind’s function separate from a claim about its good."),
            ("Run the table",
             "Let the lab list every row where the premises hold and the conclusion fails. If "
             "there are none, the argument is valid as it stands."),
            ("Read the row as a story",
             "Say in words what the counterexample describes. It tells you what the argument "
             "assumed without saying."),
            ("Write the premise that excludes the row",
             "State the conditional that makes the row impossible, add it, and check that the "
             "argument is now valid."),
            ("Price the premise",
             "Ask who would accept it and whether it holds for every case it covers. The "
             "argument is as strong as that premise."),
        ],
        "worked": {
            "title": "Function, reason and the human good",
            "intro": ["Three letters, two premises as stated, and the row that breaks them."],
            "lines": [
                "f  reasoning is the human function",
                "g  the human good is reasoning well",
                "r  reasoning sets humans apart from other living things",
                "f implies g, r  therefore g:  invalid, row f=F g=F r=T",
                "add r implies f:  valid, no such row",
                "r, r implies f  therefore g:  invalid, row r=T f=T g=F",
            ],
            "after": [
                "Two different premises are missing from the two shorter forms. The argument "
                "in the books needs both, and each can be doubted separately."
            ],
        },
        "quiz_title": "What the rows show",
        "quiz": [
            {"q": "In the first preset the lab finds one counterexample row. Which is it?",
             "a": ["`f = T, g = F, r = T`, reasoning is the function and the good is something else",
                   "`f = F, g = F, r = T`, reasoning sets humans apart and is not their function",
                   "`f = F, g = T, r = T`, the conclusion holds but the function does not",
                   "`f = T, g = T, r = F`, the function holds but nothing sets humans apart"],
             "c": 1,
             "why": "The row must make `f → g` and `r` true and `g` false. With `g` false, "
                    "`f → g` is true only if `f` is false. The first option makes the first premise "
                    "false, the third makes the conclusion true, and the fourth makes the second "
                    "premise false."},
            {"q": "Adding `r → f` makes the argument valid. What are you committed to by "
                  "accepting it?",
             "a": ["That reasoning is good for humans",
                   "That the argument is sound",
                   "That nothing else sets humans apart",
                   "That whatever sets a kind apart is its function"],
             "c": 3,
             "why": "That is what the conditional says. It does not assert that reasoning is good "
                    "for humans, which is `g`, validity is not soundness, and it is silent on "
                    "whether other things also set humans apart, which is why laughing is an "
                    "objection."},
            {"q": "The enthymeme preset keeps `r` and `r → f` and drops `f → g`. What is the "
                  "missing step?",
             "a": ["From the function to the good of the kind",
                   "From the premises to `r`",
                   "From the conclusion back to the premises",
                   "There is none, since the preset is valid"],
             "c": 0,
             "why": "The row `r = T, f = T, g = F` is a counterexample, so the preset is invalid, "
                    "and what is missing is the conditional from function to good. `r` is itself a "
                    "premise, and nothing is needed from the conclusion back."},
            {"q": "Why does the lesson provide no lab for the doctrine of the mean?",
             "a": ["Because the doctrine is false",
                   "Because Aristotle never stated it",
                   "Because it has no premises and conclusion the lab could check, so a widget "
                   "would be decorative",
                   "Because the lab cannot handle two premises"],
             "c": 2,
             "why": "The mean is a claim about judging what is fitting in the circumstances, which "
                    "has no checkable structure. The lab takes no view on whether the doctrine "
                    "is true, Aristotle states it at length, and the lab handles three premises "
                    "in the bridged preset."},
        ],
        "mistakes": [
            ("Assuming an argument from a great philosopher is valid as written",
             "The first preset is the argument as it is usually told, and the lab finds the row "
             "`f = F, g = F, r = T` on which its premises hold and its conclusion fails. Care "
             "and prestige do not make a premise appear. A great argument is usually one whose "
             "missing premise is worth the dispute."),
            ("Treating the added premise as a repair that costs nothing",
             "With `r → f` the argument is valid, and its strength is now exactly the strength "
             "of `r → f`. Laughing sets humans apart and is not obviously the human function, "
             "which is the objection a critic would press."),
            ("Taking a failure of the lab to cover the mean as a failure of the doctrine",
             "The lab checks arguments. The mean is not stated as one, and the lesson says so "
             "instead of inventing a test. That is a limit of the method, not a verdict."),
        ],
        "standard": ("Finish when you can state the premise an argument from function leaves "
                     "out.",
                     "Given a function argument, you should be able to formalise it with one "
                     "letter per simple claim, produce the counterexample row, write the premise "
                     "that closes it, and say what accepting that premise commits you to."),
        "note": "The three letters hide a good deal. A fuller formalisation would quantify over "
                "kinds and functions, and the first-order machinery to do so arrives later in the "
                "Subject, but the gaps found here do not depend on it.",
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "slippery-slopes-and-small-differences",
        "title": "Slippery Slopes and Small Differences",
        "module": "Virtue and method",
        "one_line": "Writing a slippery slope as a chain of conditionals, and watching four "
                    "treatments of vagueness give four verdicts on it.",
        "summary": (
            "A slippery slope says that no single step makes a difference, so no number of steps "
            "does. Written as forty conditionals chained from a starting case, it is valid, "
            "and the lab shows what each of four treatments of vagueness does to the chain: "
            "classical logic keeps every conditional and the absurd conclusion, a cutoff "
            "falsifies one, a borderline range makes the universal claim super-false, and degrees "
            "spread the loss over all forty."
        ),
        "key": [
            "F(start), and each step makes no difference",
            "so F(end): the slope’s conclusion",
            "classical: all true, conclusion true",
            "cutoff: one false. degrees: each loses a bit",
        ],
        "key_label": "A slope as a chain of conditionals",
        "concepts_intro": (
            "The previous lessons tested arguments for validity and sets for consistency. The "
            "slope uses both, and adds a choice about how to treat a vague word."
        ),
        "concepts": [
            ("A slope is a chain of small conditionals",
             "Each step says that if the property holds at one point it holds one step further "
             "down. The start is granted, the steps are granted one by one, and the conclusion "
             "follows by modus ponens repeated as many times as there are steps."),
            ("Validity does not make it a fallacy",
             "The chain is valid in form. An argument is faulty when a premise is false, and the "
             "slope’s question is which premise. Four treatments of the vague word answer that "
             "differently."),
            ("Small is not zero",
             "A step that makes no noticeable difference may still make a small one, and small "
             "differences add up. The degrees treatment is the one that keeps track of the sum."),
        ],
        "read_title": "Forty weeks of notice",
        "read_intro": "One slope, its premises, and what each treatment does to them.",
        "body": [
            ("p", "A slippery slope argument has a familiar shape: this step makes no moral "
                  "difference, and so does the next, and so on, so no step does and we may go "
                  "all the way. It is used both ways, to warn against a first step and to excuse "
                  "a last one, and it is often dismissed as a fallacy without saying which kind. "
                  "The lab writes it out and lets the dismissal be tested."),
            ("p", "Let `F(k)` be “`k` weeks’ notice is adequate notice”. Forty weeks is plainly "
                  "adequate, so `F(40)` is a premise. One week less never makes a moral "
                  "difference, so for each `k` from 40 down to 1 there is a premise `F(k) → "
                  "F(k − 1)`. The conclusion is `F(0)`: no notice at all is adequate."),
            ("math", [
                "F(40)",
                "F(40) → F(39)",
                "F(39) → F(38)",
                "...",
                "F(1) → F(0)",
                "therefore F(0)",
            ]),
            ("p", "Under the classical treatment, every conditional is true, the start is true and "
                  "the conclusion is true. The lab reports forty steps, all forty conditionals "
                  "true, and the conclusion true. The argument is valid, so someone who finds "
                  "the conclusion absurd must give up a premise, and the question is which one. "
                  "That is the whole content of the dispute, and it is why “fallacy” is not the "
                  "right word for it."),
            ("def", ("Tolerance conditional",
                     "A <strong>tolerance conditional</strong> says that one small step does not "
                     "change whether a vague property holds: `F(k) → F(k − 1)`. A slope is a "
                     "start plus a chain of them.")),
            ("p", "Three other treatments give a different answer to the question. A sharp "
                  "cutoff says there is some `k` where adequacy stops, here 24: `F(24)` is true and "
                  "`F(23)` is false, so exactly one conditional is false and the conclusion is "
                  "false. A borderline range says the boundary is vague: there is no fact about "
                  "where adequacy stops, only a set of admissible places to put the line. With "
                  "the range 16 to 32 the lab lets the cutoff fall anywhere from 17 to 32, so the "
                  "sixteen conditionals from `F(17) → F(16)` up to `F(32) → F(31)` are each true "
                  "on some sharpenings and false on others, and so neither true nor false "
                  "outright. No single conditional is false, but the claim that every step is "
                  "tolerated is false on every sharpening, which the lab calls super-false, and "
                  "so is the conclusion. Degrees give each conditional a value just under 1, and "
                  "chaining forty of them guarantees nothing."),
            ("example", ("Where the slope is sound",
                         "Let `F(k)` be “`k` is smaller than a million”, started at 10,000. "
                         "Each step down keeps it smaller, so every tolerance premise is true "
                         "and the conclusion that 0 is smaller than a million is true. The "
                         "chain is the same chain. What separates this from the notice case is "
                         "that here the premises are all true, and the form was never the "
                         "difference.")),
            ("p", "The lab models the conceptual slope, in which a property is said to survive "
                  "each step. It does not model the causal slope, in which allowing one step "
                  "makes the next more likely to be taken. That is a claim about how people and "
                  "institutions behave, to be supported with evidence of the kind "
                  "Science, Induction and Causation discusses. A policy can be on a causal slope "
                  "without any conceptual one, and the argument against it is then an empirical "
                  "claim."),
        ],
        "lab": ("argkit", {
            "mode": "sorites",
            "treatment": "classical",
            "preset": "weeks",
            "presets": [
                {"id": "weeks", "label": "Forty weeks of notice, a week at a time",
                 "start": 40, "end": 0, "cutoff": 24, "range": [16, 32],
                 "predicate": "is adequate notice",
                 "expect": {"soSteps": "40", "soCond": "all 40 true", "soConc": "True"}},
                {"id": "cents", "label": "An exploitative price, a cent nearer the fair one each step",
                 "start": 100, "end": 0, "cutoff": 25, "range": [10, 40],
                 "predicate": "is an exploitative price",
                 "expect": {"soSteps": "100", "soCond": "all 100 true", "soConc": "True"}},
                {"id": "grains", "label": "A heap, a grain at a time",
                 "start": 10000, "end": 0, "cutoff": 100, "range": [20, 400],
                 "predicate": "is a heap",
                 "expect": {"soSteps": "10000", "soCond": "all 10000 true", "soConc": "True"}},
            ],
            "panel_title": "Run the chain and change the treatment",
            "panel_intro": "The shipped treatment is classical. Move the treatment menu to the cutoff, "
                           "to a borderline range or to degrees, and watch the conditionals and the "
                           "conclusion change.",
        }),
        "steps_title": "Testing a slope",
        "steps_intro": "Five steps. The third and fourth are two runs of the same chain under "
                       "different rules.",
        "steps": [
            ("State the property and the two ends",
             "Name the property, the case where it plainly holds and the case where it plainly "
             "fails, and count the steps between them."),
            ("Write the tolerance conditionals",
             "Say what one step changes, and write one conditional per step, in the direction "
             "that carries the property from the start to the end."),
            ("Run it classically",
             "With every conditional true, the conclusion follows. Confirm that it is the "
             "absurd one you started with."),
            ("Run it under the other treatments",
             "Move the treatment menu to the cutoff, the borderline range and degrees. Read the "
             "conditional tile and the conclusion tile each time."),
            ("Choose the premise to give up",
             "A sharp cutoff gives up one conditional. A range gives up the universal claim. "
             "Degrees give up the idea that tolerance is perfect. Say what each costs."),
        ],
        "worked": {
            "title": "Forty weeks, four ways",
            "intro": ["The chain has forty steps, from 40 weeks of notice down to none."],
            "lines": [
                "classical:  all 40 conditionals true, conclusion true",
                "cutoff 24:  one false, at 24, conclusion false",
                "range 16 to 32:  16 indeterminate (17 to 32), super-false",
                "degrees:  each conditional 39/40, conclusion 0",
            ],
            "after": [
                "Each treatment keeps the chain valid and answers the question of which premise "
                "fails. The classical one answers none, which is why it has to accept the "
                "absurd conclusion."
            ],
        },
        "quiz_title": "Which premise fails",
        "quiz": [
            {"q": "Under the classical treatment the weeks preset has forty true conditionals and a "
                  "true start. Someone still rejects the conclusion. What follows?",
             "a": ["The lab has made an error",
                   "The conditionals are all false",
                   "The argument is invalid",
                   "At least one premise must be given up, since the argument is valid"],
             "c": 3,
             "why": "The chain is valid, so a false conclusion requires a false premise. The "
                    "classical treatment says none is false, which is why it is stuck with the "
                    "conclusion. The argument is not invalid, and the lab computes no error."},
            {"q": "With the cutoff at 24, where is the false conditional?",
             "a": ["`F(24) → F(23)`",
                   "`F(40) → F(39)`",
                   "`F(1) → F(0)`",
                   "None of them"],
             "c": 0,
             "why": "The cutoff treatment makes `F(24)` true and `F(23)` false, so the conditional "
                    "between them is the false one. The ends of the chain are true, and the "
                    "conclusion is false because exactly one conditional fails."},
            {"q": "Under degrees, each of the forty conditionals has value 39/40, and the "
                  "conclusion’s guaranteed value is 0. Why?",
             "a": ["Because 39/40 is a false value",
                   "Because the conditionals are not chained",
                   "Because the start is not true",
                   "Because forty small losses add up to the whole"],
             "c": 3,
             "why": "Each step loses 1/40, and forty steps lose 40/40. The chain still holds, and the "
                    "start has full value. Nothing is false, which is what makes this treatment "
                    "different from the cutoff."},
            {"q": "Which slippery slope is not modelled by the lab?",
             "a": ["A conceptual slope about notice",
                   "A causal slope, in which allowing one step makes the next more likely",
                   "A slope about a heap",
                   "A slope about a price"],
             "c": 1,
             "why": "The three presets are conceptual: each asks whether a property survives small "
                    "steps. A causal slope is a claim about what people would do next, which needs "
                    "evidence and not a chain of conditionals."},
        ],
        "mistakes": [
            ("Thinking a slippery slope is always a fallacy",
             "The chain is valid. In the classical run every conditional is true and the "
             "conclusion is true, so the form is not what is wrong, and when the premises are all "
             "true, as in the example with a million, the conclusion is true as well. A slope "
             "fails when a premise does, and the question is which one."),
            ("Counting each step’s difference as zero when it is only small",
             "Under degrees each step costs 1/40 of the property, which is too little to notice and "
             "enough, forty times, to lose it all. The tolerance premise was true of each step "
             "taken singly and false of the steps taken together."),
            ("Expecting the lab to say which treatment is right",
             "The four treatments are rival accounts of a vague word, and each gives a verdict "
             "on the same chain. The lab reports the verdicts. Choosing among them is a view "
             "about vagueness, not something a table decides."),
        ],
        "standard": ("Finish when you can write a slope as a chain and state what each "
                     "treatment does to it.",
                     "Given a slippery slope, you should be able to write its start, its "
                     "tolerance conditionals and its conclusion, run the chain under the "
                     "classical, cutoff, range and degree treatments, and report for each which "
                     "premise gives way."),
        "note": "The lab treats the property as a function of a count, one number that changes "
                "step by step. Many slopes, such as those about a person’s character, are "
                "multidimensional, and nothing here says how to line them up on one scale.",
    },
]
