"""Games and the Social Contract, lessons 7-11: the social contract and the many-player games.

Hume's farmers are the repeated dilemma of the previous lesson told as a story
about convention; Hobbes's state of nature is the dilemma (and its stag-hunt
cousin) with a sovereign who changes the payoffs; the commons, the public good
and the replicator step are the same dilemma with many players and then with a
population. Every figure the prose states is one the lab prints; the presets pin
the tiles that say why each preset exists.
"""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "humes-farmers-and-convention",
        "title": "Hume's Farmers and Convention",
        "module": "Repeated games",
        "one_line": "Two farmers who would each gain from the other's help refuse in one season and help over many, with no promise between them.",
        "summary": (
            "Hume's two neighbours have corn that ripens on different days, and each would harvest faster with the other's "
            "help. Played once, the exchange is the prisoner's dilemma and nobody helps; played season after season by "
            "farmers who answer help with help, it pays both of them. The farmers are no less selfish in the second case: "
            "what has changed is that there is a next season."
        ),
        "key": [
            "one harvest: refusing dominates, no help",
            "a season: help answered by help pays both",
            "a convention is kept as the others keep it",
            "no promise, no kindness, a next season",
        ],
        "key_label": "From one harvest to a season",
        "concepts_intro": (
            "Hume's story is short, and the three ideas below are all that the lab needs from it."
        ),
        "concepts": [
            ("The exchange is the dilemma",
             "Each farmer does best by being helped and not helping, next best by helping and being helped, "
             "worse by neither, and worst by helping alone. That is the ordering of the prisoner's dilemma, and the "
             "four payoffs here are the course's standard ones: `3`, `0`, `5` and `1`."),
            ("One harvest has no tomorrow",
             "Played once, refusing pays more than helping whatever the neighbour does. Both refuse, "
             "each collects `1`, and the harvests are lost for want of the help that would have paid both."),
            ("A convention is a habit the others keep",
             "Hume's farmers need no promise and no kindness. A farmer helps because the neighbour will stop helping "
             "otherwise, and the neighbour helps for the same reason. The habit is stable when each, keeping it, does best given that the other keeps it."),
        ],
        "read_title": "Why the second farmer helps",
        "read_intro": "Hume's story, the table behind it, and the one change that turns refusal into help.",
        "body": [
            ("p", "Hume imagines two neighbours whose corn is ripe on different days. Your corn is ripe today and mine will "
                  "be ripe tomorrow, and it would profit us both that I labour with you today and you aid me tomorrow. "
                  "But I have no kindness for you and know you have as little for me, so I will not take pains on your "
                  "account; and if I did, I should expect to be disappointed. You reason the same way. In his words, "
                  "&ldquo;both of us lose our harvests for want of mutual confidence and security.&rdquo;"),
            ("p", "Write each season as a game in which both farmers choose, help or refuse, and the payoffs follow the order "
                  "just described. Hume's farmers in fact move in turns, and the lab has them choose together; the "
                  "dilemma is the same, and the turns are left out. The four numbers below are the course's standard "
                  "ones and nothing in the lab knows about corn, so only their order should be read as Hume's."),
            ("math", [
                "                 neighbour helps    neighbour refuses",
                "     I help           3, 3                0, 5",
                "     I refuse         5, 0                1, 1",
            ]),
            ("p", "Played once, this is the dilemma of “The Prisoner's Dilemma”. Refusing pays `5` against a farmer who "
                  "helps and `1` against one who does not, so it beats helping either way. Both refuse and each collects "
                  "`1`. That dominance was computed in “The Prisoner's Dilemma”'s lab, which checks every cell; the lab "
                  "here plays matches, and its first preset only plays the single harvest between two farmers who refuse "
                  "and prints the `1` each. Hume's conclusion is right for one harvest, "
                  "and it has nothing to do with the farmers being unkind: change them into saints with the same "
                  "payoffs and the table is the same."),
            ("h3", "The second farmer"),
            ("p", "The tempted farmer is whichever one has just been helped. Refusing to return the help pays `5` this "
                  "season in place of `3`, a gain of `2`. Hume's point is that the same farmer will want help again, and "
                  "that the neighbour knows it. If the neighbour follows tit for tat, which helps first and afterwards "
                  "does whatever the other did last, then a refusal is answered by a refusal, and the gain of `2` is "
                  "followed by seasons at `1` where there would have been `3`."),
            ("p", "That trade is worth refusing exactly when the future counts for little. From “The Shadow of the "
                  "Future”, with these payoffs tit for tat is stable against itself when the chance of another season is at "
                  "least `2/3`. The lab's second preset sets that chance at `9/10`, and the tile says it sustains cooperation."),
            ("def", ("Convention",
                     "A <strong>convention</strong> is a regularity of behaviour that each member keeps because the others keep it, "
                     "so that no one gains by departing from it alone. Hume's example is two men rowing a boat, who pull together "
                     "without ever having promised to.")),
            ("p", "Twelve seasons of tit for tat against tit for tat are all help, and each farmer collects `12` times "
                  "`3`, which is `36`. Nobody gave a word, and nobody is kind. Each is doing the best available given "
                  "what the other will do, which is the definition of an equilibrium met in “Nash Equilibrium in Pure "
                  "and Mixed Strategies”. A convention in Hume's sense is that equilibrium, reached by habit."),
            ("p", "The word is wider here than in “Coordination, Conventions and the Stag Hunt”, where a convention picked "
                  "one of several matches in a coordination game and another match would have served as well. Hume's "
                  "rowers are a case of that kind. His farmers are not: helping is not an equilibrium of the one-harvest "
                  "game at all, and becomes one only because the seasons repeat and a refusal can be answered. What the "
                  "two uses share is the part that does the work in both lessons: a regularity that each keeps because "
                  "the others keep it, with no promise behind it."),
            ("h3", "A refusal that begins the season"),
            ("p", "The third preset has one farmer suspicious: he refuses in the first season and afterwards copies his "
                  "neighbour, who helps first. In the first season the suspicious farmer collects `5` and the neighbour `0`. "
                  "In the next each copies the other, and the roles reverse. The pair then alternate, helped and "
                  "refused in turn, and over twelve seasons each collects `30`, six short of what the two "
                  "trusting farmers made. Neither can leave the pattern by following his own rule."),
            ("p", "Three limits belong here. The twelve seasons are a stand-in for a game with no known end: farmers who "
                  "knew which harvest was the last would, by the argument in the previous lesson, stop helping before it and "
                  "unravel the whole run. Second, tit for tat is not the only way the pair could play, and two farmers who "
                  "always refuse are an equilibrium too. Third, the payoffs are chosen, and a farmer who also enjoys "
                  "the company is playing a different game."),
        ],
        "lab": ("choicekit", {
            "mode": "iterated",
            "a": "TFT",
            "b": "TFT",
            "rounds": 12,
            "presets": [
                {"id": "farmers-once", "label": "One harvest, neither farmer helps",
                 "R": 3, "S": 0, "T": 5, "P": 1, "a": "ALLD", "b": "ALLD", "rounds": 1, "delta": "9/10", "expect": {"itScoreA": "1", "itScoreB": "1"}},
                {"id": "farmers-season", "label": "Twelve seasons, help answered by help",
                 "R": 3, "S": 0, "T": 5, "P": 1, "a": "TFT", "b": "TFT", "rounds": 12, "delta": "9/10", "expect": {"itScoreA": "36", "itScoreB": "36", "itThresh": "GRIM 1/2, TFT 2/3: δ = 9/10 sustains"}},
                {"id": "farmers-suspicious", "label": "Twelve seasons, one farmer refuses first",
                 "R": 3, "S": 0, "T": 5, "P": 1, "a": "STFT", "b": "TFT", "rounds": 12, "delta": "9/10", "expect": {"itScoreA": "30", "itScoreB": "30"}},
            ],
            "panel_title": "Play one harvest, then a season",
            "panel_intro": "Player A is the first farmer and player B the second. Change the strategies or the number of "
                           "rounds and read the two totals; the last tile gives the continuation chance the lab needs for help to be stable.",
        }),
        "steps_title": "From a refusal to a convention",
        "steps_intro": "The same five moves for any pair of farmers.",
        "steps": [
            ("Write the exchange as a table",
             "Put the four outcomes in order of what each farmer would rather have, and give them the course's numbers. "
             "If help-and-be-helped is not below being helped for nothing, the game is not a dilemma."),
            ("Play it once",
             "Compare refusing with helping against each choice of the neighbour. Refusing wins both comparisons, so one harvest "
             "ends with nobody helping."),
            ("Choose the rule each farmer follows",
             "Tit for tat helps first and then copies. State what it plays in the opening season and what it plays after a refusal."),
            ("Play the season and add the payoffs",
             "Sum the seasons for each farmer. Two rules that never refuse each other earn the reward every season."),
            ("Check the temptation against the future",
             "The farmer who refuses gains `2` once and loses `2` in each later season the neighbour answers. "
             "Whether that is a loss depends on the continuation chance, not on the farmer's character."),
        ],
        "worked": {
            "title": "One harvest and twelve",
            "intro": ["Payoffs 3, 0, 5, 1 for help-and-help, help alone, refusal alone, neither."],
            "lines": [
                "One harvest: refusing pays 5 or 1, helping pays 3 or 0",
                "Both refuse:  1 each",
                "Twelve seasons, tit for tat against itself:",
                "every season both help: 3 each, twelve times",
                "Each farmer:  12 x 3 = 36",
                "One farmer refuses first: seasons alternate 5 and 0",
                "Each farmer:  6 x 5 + 6 x 0 = 30",
            ],
            "after": [
                "The gap between `1` and `36` is the cost of playing once, and it is paid by two farmers who are exactly "
                "as self-interested in both cases. The gap between `36` and `30` is the cost of a single refusal to go first.",
            ],
        },
        "quiz_title": "One season and twelve",
        "quiz": [
            {"q": "Hume's farmers play a single harvest with payoffs 3, 0, 5, 1. What happens?",
             "a": ["Both help, since each wants the other's labour and each would collect 3",
                   "Both refuse, and each collects 1",
                   "One helps and one refuses, so the payoffs are 0 and 5",
                   "Both help if they trust each other and refuse if they do not"],
             "c": 1,
             "why": "Refusing pays 5 against a helper and 1 against a refuser, so it beats helping in both cases and each farmer "
                    "refuses. Trust changes what a farmer expects, not what refusing pays. A split needs one farmer to help "
                    "while the table pays him more for refusing."},
            {"q": "Two farmers each follow tit for tat for twelve seasons with the standard payoffs. What does each collect?",
             "a": ["12", "30", "36", "60"],
             "c": 2,
             "why": "Neither refuses first, so both help every season and each earns 3 twelve times. Thirty is what the pair "
                    "collect when one refuses in the opening season. Sixty would be 5 in every season, which the table pays only "
                    "to a farmer who refuses a helper each time, and tit for tat stops helping a farmer who refuses."},
            {"q": "In the twelve-season preset, why does the farmer who has just been helped help back?",
             "a": ["Gratitude, which Hume says is not to be relied on",
                   "A promise made before the harvest",
                   "Fear of what the neighbour will think of him",
                   "Refusing would win 2 once and then cost him help in later seasons, which is worth more"],
             "c": 3,
             "why": "The lab needs no feeling and no word: a refusal gains 5 in place of 3, and tit for tat answers it with "
                    "refusals, and with a continuation chance of 9/10, above the 2/3 the tile gives, that loses more than it gained."},
            {"q": "In the suspicious preset one farmer refuses first. What does the record show?",
             "a": ["The farmers take turns being helped and refused, and each collects 30",
                   "The neighbour gives up helping after one season and both collect 12",
                   "The pair settle into mutual help from the second season",
                   "The suspicious farmer collects more than the neighbour, since he went first"],
             "c": 0,
             "why": "Each copies the other's last move, so the refusal passes back and forth and the pair take turns at 5 and 0. "
                    "Each ends with six of each, which is 30, and neither ends ahead. Mutual help from the second season "
                    "would need one of them to help while being refused, which tit for tat does not do."},
        ],
        "mistakes": [
            ("Thinking Hume's farmers fail because they are selfish",
             "The farmers of the twelve-season preset are exactly as selfish as those of the one-harvest preset: the payoffs "
             "are identical and so is each farmer's wish to be helped for nothing. One harvest ends in `1` each and twelve seasons "
             "of tit for tat in `36`, so what separates failure from success is whether there is a next season, and "
             "not the character of the people in the story."),
            ("Thinking a convention needs a promise",
             "Hume's rowers pull together though they have never promised, and the farmers help each other for the same reason. "
             "A promise can start such a habit, but what keeps it going is that each does best by keeping it while the "
             "other does. The lab has no promises in it and the farmers still reach `36`."),
            ("Reading twelve seasons as proof that the farmers must cooperate",
             "Two farmers who always refuse are also in equilibrium, and the lab's totals say what happens if both follow "
             "tit for tat, not that they will. The result also needs a season that might come: farmers who know which "
             "harvest is the last will refuse in it, and so on backwards, as in the previous lesson."),
        ],
        "standard": ("Finish when you can say what turns the farmers' refusal into help.",
                     "Given the standard payoffs, play one harvest and a twelve-season run between named rules, read both totals, and "
                     "state the continuation chance above which repaying a favour is better than refusing it."),
        "note": "Hume's own farmers are not playing together; the second harvests after being helped. That version is a game "
                "in turns, which this course does not build, and flattening it loses the sequence while keeping the incentive. "
                "Try a season in which one farmer follows ALLD against the other's TFT, and read what the helper loses.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "hobbes-and-the-state-of-nature",
        "title": "Hobbes and the State of Nature",
        "module": "Many players",
        "one_line": "Without a sovereign, two rational and uncertain people attack each other, and a penalty on attacking changes the equilibrium.",
        "summary": (
            "Hobbes's state of nature can be written as a game between two people who each choose peace or attack. "
            "Where attacking pays whatever the other does, war is the only equilibrium; where attacking is only protection "
            "against an attacker, war and peace are both equilibria. A sovereign who punishes attack changes the payoffs, "
            "and with a large enough penalty peace is the only equilibrium."
        ),
        "key": [
            "anarchy: attack pays against either move",
            "so both attack, and each does worse",
            "fear alone gives two equilibria",
            "a sovereign changes payoffs, not people",
        ],
        "key_label": "A game whose payoffs a sovereign changes",
        "concepts_intro": (
            "Hobbes's argument is a claim about incentives, and the three ideas below put it into a table."
        ),
        "concepts": [
            ("The state of nature is a game without enforcement",
             "Two people each choose peace or attack, with no one to punish an attack. Whatever the numbers are, "
             "they are the payoffs of an interaction in which only the players' own interests apply."),
            ("Attack can pay from greed or from fear",
             "If attacking a peaceful neighbour pays most, attack dominates and the game is the prisoner's dilemma. If it pays "
             "no more than defending against an attacker, the game is the stag hunt and the trouble is only that each fears the other."),
            ("A sovereign changes the payoffs",
             "A penalty on attacking is subtracted from every payoff in which someone attacks. It is a change to the table, and a "
             "large enough change moves the equilibrium without changing what anyone wants."),
        ],
        "read_title": "War of all against all, and what ends it",
        "read_intro": "Three tables: Hobbes's competition, the same people under a sovereign, and Hobbes's diffidence.",
        "body": [
            ("p", "Hobbes finds three causes of quarrel in human nature: competition, diffidence and glory. Competition "
                  "makes men invade for gain, diffidence for safety, and glory for reputation. Without a common power "
                  "to keep them all in awe, he writes, they are in a condition of war &mdash; &ldquo;of every man against every man&rdquo; "
                  "&mdash; and life is &ldquo;solitary, poor, nasty, brutish, and short.&rdquo; Competition and diffidence can be "
                  "tabulated; glory cannot, and the lab leaves it out."),
            ("p", "Take competition first. Two people each choose peace or attack. If both keep the peace each gets `3`. "
                  "An attacker who finds the other at peace takes `5`, and the victim gets `0`. If both attack, each gets `1`."),
            ("math", [
                "                 other: peace    other: attack",
                "     peace           3, 3             0, 5",
                "     attack          5, 0             1, 1",
            ]),
            ("p", "This is the table of “The Prisoner's Dilemma” with new labels. Attack pays `5` against peace and `1` "
                  "against attack, and peace pays `3` and `0`, so attack dominates. Both attack, each collects `1`, "
                  "and both would have collected `3` at peace. The model needs no wicked people to get there: only "
                  "that each prefers more to less and cannot count on the other."),
            ("h3", "The sovereign"),
            ("p", "Now let a sovereign fine whoever attacks, by `4`, whatever the target does. Subtract `4` from every "
                  "payoff in which the person attacks. An attacker who finds the other at peace now gets `1`, and two attackers "
                  "each get `−3`. The victim's payoffs do not change."),
            ("math", [
                "                 other: peace    other: attack",
                "     peace           3, 3             0, 1",
                "     attack          1, 0            −3, −3",
            ]),
            ("p", "Against peace, peace pays `3` and attack pays `1`. Against attack, peace pays `0` and attack pays `−3`. "
                  "Peace now dominates, the only equilibrium is peace with peace, and each collects `3`. Nobody is fined "
                  "there, so the penalty is never collected: a threat that works costs nothing to carry out. "
                  "Hobbes's remark that covenants without the sword are but words is, in the table, the observation that a "
                  "promise changes no payoff: only the sword does, and it has to change them by enough. A penalty of `2` "
                  "or less does not make peace dominate, since at `1` attacking a peaceful neighbour still pays `4` "
                  "against `3`, and at `2` the two tie. The lab's dominance tile reports strict dominance only, so it "
                  "turns at a penalty of `3`."),
            ("h3", "Fear without greed"),
            ("p", "The third table has no gain from attacking at all. Peace with peace pays `4` each. Attacking pays `3` "
                  "whatever the other does, because the attacker gets only the safety of not being caught unprepared, and a "
                  "peaceful victim gets `0`. This is the stag hunt of “Coordination, Conventions and the Stag Hunt”, "
                  "and it has two equilibria: peace with peace and attack with attack."),
            ("p", "Hobbes's point about diffidence is that the second equilibrium can be reached by people who want nothing "
                  "the other has. Peace is worth keeping only if the neighbour keeps it with probability at least `3/4`; "
                  "short of that, attacking first is the better bet. What the sovereign supplies in this version is "
                  "assurance. The remedy is a common power that makes each person's expectation of the other safe."),
            ("p", "The lab does not say who watches the sovereign, who pays him, or why he would fine anyone: the penalty is "
                  "an assumption of the model, and Hobbes's own argument for an authority that can be trusted to apply it "
                  "is the part the table leaves out."),
        ],
        "lab": ("choicekit", {
            "mode": "game",
            "view": "dominance",
            "presets": [
                {"id": "anarchy", "label": "Competition: attacking a peaceful neighbour pays 5",
                 "rows": ["Peace", "Attack"], "cols": ["Peace", "Attack"],
                 "payoffs": [[[3, 3], [0, 5]], [[5, 0], [1, 1]]], "expect": {"gaPure": "(Attack, Attack)", "gaDom": "Attack dominates for both"}},
                {"id": "sovereign", "label": "A penalty of 4 on every attack",
                 "rows": ["Peace", "Attack"], "cols": ["Peace", "Attack"],
                 "payoffs": [[[3, 3], [0, 1]], [[1, 0], [-3, -3]]], "expect": {"gaPure": "(Peace, Peace)", "gaDom": "Peace dominates for both"}},
                {"id": "assurance", "label": "Diffidence: attacking pays 3 whatever the other does",
                 "rows": ["Peace", "Attack"], "cols": ["Peace", "Attack"],
                 "payoffs": [[[4, 4], [0, 3]], [[3, 0], [3, 3]]], "expect": {"gaPure": "(Peace, Peace); (Attack, Attack)", "gaDom": "none", "gaMixed": "row Peace: 3/4, col Peace: 3/4"}},
            ],
            "panel_title": "Subtract a penalty from the attack cells",
            "panel_intro": "Start from the anarchy table, then lower every payoff of an attacker by the same amount and watch the "
                           "dominance tile move. Try a penalty of 1, then 2, then 3.",
        }),
        "steps_title": "Writing the state of nature as a game",
        "steps_intro": "The same steps for each of Hobbes's causes.",
        "steps": [
            ("List what each person can do",
             "Peace or attack. Hobbes's conclusions follow from this much, so a third option has to be argued for."),
            ("Order the four outcomes by what each would rather have",
             "Ask what an attacker gains from a peaceful victim. If the gain is more than peace, the cause is competition; "
             "if it is only safety, the cause is diffidence."),
            ("Find the equilibria",
             "Check dominance first, then the cells where both are best-responding. Anarchy by competition has one, "
             "and anarchy by diffidence has two."),
            ("Subtract the sovereign's penalty",
             "Take it from every payoff in which the person attacks, and leave the victim's payoff alone."),
            ("Find the equilibria again",
             "If peace now dominates, the sovereign's penalty is large enough. If attack still pays against peace, "
             "it is not."),
        ],
        "worked": {
            "title": "Competition, then a penalty of four",
            "intro": ["Payoffs for peace with peace 3, 3; an attacker on a peaceful victim 5, 0; two attackers 1, 1."],
            "lines": [
                "Anarchy.  Other keeps peace: attack 5, peace 3 -> attack",
                "          Other attacks:     attack 1, peace 0 -> attack",
                "Only equilibrium:  (attack, attack), 1 each",
                "Penalty 4 off every attack payoff:",
                "          Other keeps peace: attack 1, peace 3 -> peace",
                "          Other attacks: attack -3, peace 0 -> peace",
                "Only equilibrium:  (peace, peace), 3 each, no fine paid",
            ],
            "after": [
                "Nothing in either table says the people have changed. The sovereign has changed what an attack costs, and "
                "with it what each does in reply to the other.",
            ],
        },
        "quiz_title": "Anarchy and the penalty",
        "quiz": [
            {"q": "In the anarchy table a person is sure the neighbour will keep the peace. What is the best response?",
             "a": ["Peace, because a certain peace is worth keeping",
                   "Either, since the neighbour's peace fixes the result",
                   "Attack, which pays 5 where peace pays 3",
                   "Peace, because both would then collect 3"],
             "c": 2,
             "why": "Certainty about the neighbour's peace raises the pay for attacking: 5 against 3. The pair collecting 3 each is "
                    "a cell neither can reach by moving alone, and a choice is judged by what it pays against the neighbour's move."},
            {"q": "Why does a penalty of 4 on every attack make peace the only equilibrium?",
             "a": ["It makes attackers want peace more than before",
                   "It makes attack unavailable to either person",
                   "It makes each victim's payoff larger",
                   "Attacking now pays 1 against peace where peace pays 3, and −3 against attack where peace pays 0"],
             "c": 3,
             "why": "The penalty is subtracted from the attacker's payoffs and changes no wish. Attack is not removed, only made "
                    "worse than peace in both columns, and the victim's payoff stays as it was."},
            {"q": "In the diffidence table attacking pays 3 whether or not the neighbour attacks. What does the table show?",
             "a": ["Fear alone can sustain war: both diagonal cells are equilibria",
                   "Peace cannot be an equilibrium unless someone is fined",
                   "Both people want to exploit the other",
                   "A sovereign would have nothing to add"],
             "c": 0,
             "why": "Nobody gains from attacking a peaceful neighbour here, so greed plays no part, yet the lab marks both "
                    "diagonal cells as equilibria. Peace is stable too, which is why the answer is not that peace is impossible, "
                    "and the sovereign can still move people from the worse equilibrium by assuring them of the other's peace."},
            {"q": "Subtract a penalty of 1 rather than 4 from every attack payoff in the anarchy table. Against a peaceful neighbour, what does attack pay?",
             "a": ["Less than peace does, at 1 against 3",
                   "4, still more than peace's 3",
                   "−3, as with a penalty of 4",
                   "The same as peace, at 3"],
             "c": 1,
             "why": "Attack paid 5 against peace, and 5 less 1 is 4, which still beats 3. A penalty must exceed 2 before attack "
                    "stops beating peace against a peaceful neighbour. At exactly 2 the two tie at 3."},
        ],
        "mistakes": [
            ("Thinking Hobbes took people to be wicked",
             "The diffidence table has no gain from attacking a peaceful neighbour: attack pays `3` whether the other attacks or not, "
             "and peace with peace pays `4`. Yet attack with attack is still an equilibrium, because anyone who doubts "
             "the neighbour's peace does better to strike first. The model needs only that people are rational and unsure of each other."),
            ("Expecting the sovereign to be the cause of peace",
             "The sovereign changes payoffs, and peace follows from the new table. In the penalty table the fine is never paid. "
             "If it is too small, as `1` is, attacking still pays and the war continues under a ruler."),
            ("Reading the model as a history of how states began",
             "The tables say what follows from a given set of payoffs and say nothing about whether any people were ever in "
             "that condition. Hobbes himself treats the state of nature as what would follow without a common power, and the model makes that claim checkable."),
        ],
        "standard": ("Finish when you can show how a penalty moves an equilibrium.",
                     "Write the state of nature as a two-by-two table, find its equilibria, subtract a stated penalty from the "
                     "attack payoffs, and say whether peace now dominates and, if it does not, how large the penalty must be."),
        "note": "Hobbes's glory, which makes men fight for reputation, has no payoff to attach to it here, and the lab "
                "leaves it out rather than invent one. The two people stand for any pair; the next lessons ask what changes when "
                "ten take part.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "the-tragedy-of-the-commons",
        "title": "The Tragedy of the Commons",
        "module": "Many players",
        "one_line": "Each herder gains from one more animal while the cost falls on all, so every herder adds and all are left worse off.",
        "summary": (
            "Ten herders share a pasture, and each can keep a single animal or add a second. An added animal pays "
            "its owner in full and costs every herder a share of the grass, so adding is best whatever the others do. "
            "The lab finds the one equilibrium, the best total for the group, and the gap between them. No herder "
            "needs to be greedy for this to happen."
        ),
        "key": [
            "my animal's gain is mine, its cost is shared",
            "adding dominates, so every herder adds",
            "the equilibrium falls short of the best",
            "make the adder pay and the gap closes",
        ],
        "key_label": "A gain kept and a cost shared",
        "concepts_intro": (
            "Writing a herder's payoff as a function of the others is the new skill; the three ideas below set it up."
        ),
        "concepts": [
            ("A payoff as a function of the others",
             "Fix a herder and count how many of the other herders restrain. Call the count `k`. Then the herder's payoff "
             "from restraining is `C(k)` and from adding is `D(k)`, and the whole game is those two lists."),
            ("The equilibrium and the optimum are different questions",
             "The equilibrium asks where no herder gains by changing alone. The optimum asks where the herders' payoffs "
             "sum to most. In a dilemma these are different answers, and the gap is the tragedy."),
            ("A cost on others is not a wish for more",
             "Greed would mean wanting more animals than the pasture can carry. The tragedy needs only that the herder who "
             "adds does not pay the whole cost of adding, which is a fact about who bears the grass, not about the herder."),
        ],
        "read_title": "Ten herders and one pasture",
        "read_intro": "A payoff for each choice, the equilibrium it leads to, and the optimum it misses.",
        "body": [
            ("p", "Ten herders graze one pasture. Each keeps one animal and may add a second. Every animal on the pasture "
                  "yields `22` less the number of animals grazing there, so each animal added makes every animal, "
                  "the herder's own included, worth one less. A herder owns either one animal or two."),
            ("p", "Count the others who restrain, `k`, from `0` to `9`. If I restrain, the pasture carries ten animals "
                  "plus the second animals of the nine other herders who add, which is `2·n − 1 − k` in all, with `n = 10` herders, and my one animal is worth "
                  "`22 − (2·n − 1 − k)`. If I add, the pasture carries `2·n − k` animals, and my two are each worth `22 − (2·n − k)`."),
            ("math", [
                "C(k) = 22 − (2·n − 1 − k)",
                "D(k) = 2·(22 − (2·n − k))",
            ]),
            ("p", "With ten herders these are `C(k) = 3 + k` and `D(k) = 4 + 2·k`. The difference is `D(k) − C(k) = 1 + k`, "
                  "which is positive for every `k`. Adding pays more than restraining "
                  "whatever the others do, so adding dominates. The lab's dominance tile says so, and it reports one equilibrium, "
                  "with no herder restraining. A lone restrainer among nine adders would get `3` where adding gets `4`, "
                  "so no herder can improve alone."),
            ("p", "Compare the equilibrium with the best the group could do. Each herder gets `4` there, `40` in all. If all ten restrain, "
                  "each gets `12` and the total is `120`. The lab searches every number of restrainers for the largest total, "
                  "and finds it at nine restraining and one adding, `121`, because the first extra animal does little harm to "
                  "a pasture that is otherwise lightly stocked. The point survives: the equilibrium is far below the optimum."),
            ("h3", "What one herder gains and what everyone loses"),
            ("p", "A herder who adds while the other nine restrain gets `D(9) = 22` against `C(9) = 12`, a gain of `10`. "
                  "If every herder does the same thing, each gets `4` where all restraining would have given `12`, a loss of "
                  "`8` each. The lab prints both in the tile for what defecting gains. The gain is private and the loss is shared, "
                  "and that asymmetry is the whole of the tragedy."),
            ("h3", "Make the adder pay"),
            ("p", "Put a fee of `11` on every animal added. The most a herder ever gains by adding is `10`, when the other "
                  "nine restrain, so `11` is more than anyone gains in any case. Restraining now pays more at every `k`, "
                  "and the only equilibrium is all ten restraining. A fee of exactly `10` is the border, and the lab's fourth "
                  "preset sits on it: a herder facing nine restrainers is then indifferent, so the equilibria tile lists "
                  "nine restrainers as well as ten, while the dominance tile already says restraining dominates, because "
                  "this lab counts dominance the way “The Decision Matrix and Dominance” did, at least as good everywhere "
                  "and better somewhere, where the two-player lab of “The Prisoner's Dilemma” counted only strict dominance. "
                  "The herders' wishes are the same as before: the cost of the extra animal has been "
                  "moved onto the herder who adds it. Giving each herder his own pasture would do the same."),
            ("p", "Three herders on the same pasture do not reach a tragedy. Adding is still best for each, but three herders do not "
                  "crowd the grass enough for the equilibrium to fall below the optimum. The lab finds the equilibrium total, `96`, "
                  "to be the best total as well, and it shows that each herder would even get `13` more if all three added "
                  "than if all three restrained. The payoffs are written with the number of herders in them, so the slider shows "
                  "where the gap opens: at five herders the equilibrium is still the best total, and at six it is not. It is a fact "
                  "about how large the cost to others is compared with the gain, and a lightly used commons can be left alone."),
            ("p", "Two limits. The herders here cannot talk, and real commons are often managed by their users with rules "
                  "that change the payoffs; Elinor Ostrom's work on such arrangements is the reason this lesson claims no more "
                  "than a conditional. And the payoffs are chosen: a pasture that regrows differently is a different table."),
        ],
        "lab": ("choicekit", {
            "mode": "commons",
            "gens": 0,
            "presets": [
                {"id": "herders", "label": "Ten herders, each animal worth 22 less the animals grazing",
                 "n": 10, "payC": "22 - (2*n - 1 - k)", "payD": "2*(22 - (2*n - k))", "x0": "1/2", "gens": 0, "expect": {"cmDom": "Defect dominates", "cmEq": "k* = 0", "cmOpt": "9 cooperate: total 121", "cmUniv": "alone +10, everyone −8"}},
                {"id": "small-commons", "label": "Three herders on the same pasture",
                 "n": 3, "payC": "22 - (2*n - 1 - k)", "payD": "2*(22 - (2*n - k))", "x0": "1/2", "gens": 0, "expect": {"cmDom": "Defect dominates", "cmEq": "k* = 0", "cmOpt": "none cooperate: total 96", "cmUniv": "alone +17, everyone +13"}},
                {"id": "regulated", "label": "Ten herders and a fee of 11 on each animal added",
                 "n": 10, "payC": "22 - (2*n - 1 - k)", "payD": "2*(22 - (2*n - k)) - 11", "x0": "1/2", "gens": 0, "expect": {"cmDom": "Cooperate dominates", "cmEq": "k* = 10", "cmOpt": "all 10 cooperate: total 120"}},
                {"id": "fee-ten", "label": "Ten herders and a fee of 10, the border",
                 "n": 10, "payC": "22 - (2*n - 1 - k)", "payD": "2*(22 - (2*n - k)) - 10", "x0": "1/2", "gens": 0, "expect": {"cmDom": "Cooperate dominates", "cmEq": "k* = 9, 10"}},
            ],
            "panel_title": "Change the herd, the fee or the number of herders",
            "panel_intro": "Payoffs are expressions in k, the number of other herders who restrain, and n, the number of herders. "
                           "Subtract a fee from the adder's payoff and find the smallest whole fee at which the dominance tile "
                           "turns, and the smallest at which the equilibria tile lists ten restrainers alone.",
        }),
        "steps_title": "Writing a commons as a game",
        "steps_intro": "Four steps, and the last is the comparison the lesson exists for.",
        "steps": [
            ("Fix one herder and count the others who restrain",
             "Call the count `k`. Everything the herder needs to know about the others is that number."),
            ("Write what restraining and adding pay at each k",
             "Count the animals on the pasture in each case and value each at the pasture's yield per animal. "
             "These are `C(k)` and `D(k)`."),
            ("Compare the two lists",
             "If adding pays at least as much at every `k` and more at some, adding dominates, and the only equilibrium is that nobody restrains."),
            ("Add up the herders' payoffs for each number of restrainers",
             "The largest sum is the optimum. If it exceeds the sum at the equilibrium, there is a gap, and that gap is what a fee or an owner is for."),
        ],
        "worked": {
            "title": "Ten herders at 22 less the animals",
            "intro": ["The pasture yields 22 less the number of animals grazing, with ten herders."],
            "lines": [
                "k others restrain: restrain pays 3 + k, add pays 4 + 2k",
                "Add minus restrain = 1 + k, positive for every k",
                "So every herder adds: 10 x 4 = 40 in all",
                "A lone adder among nine who restrain: 22 against 12",
                "All ten restrain: 10 x 12 = 120",
                "Best total, nine restrain and one adds: 121",
            ],
            "after": [
                "No herder, looking at the nine others adding, would restrain: restraining pays `3` and adding pays `4`. "
                "The total of `40` is a third of what restraint would give, and each step that led there was individually sensible.",
            ],
        },
        "quiz_title": "Gain, cost and gap",
        "quiz": [
            {"q": "Nine of the ten herders restrain. What does the tenth get by adding, and by restraining?",
             "a": ["22 by adding and 12 by restraining",
                   "12 by adding and 22 by restraining",
                   "4 by adding and 3 by restraining",
                   "16 by adding and 16 by restraining"],
             "c": 0,
             "why": "With k = 9, adding pays 4 + 2·9 = 22 and restraining pays 3 + 9 = 12. Four and three are the payoffs "
                    "when no other herder restrains, and the other pairs reverse the two choices or treat them as equal."},
            {"q": "The lab reports the equilibrium with no one restraining, and a larger total elsewhere. Why is no herder willing to restrain alone?",
             "a": ["Each herder is greedy and wants the whole pasture",
                   "A lone restrainer gets 3 where adding would get 4, and the benefit of restraint goes to others",
                   "The herders are forbidden to talk",
                   "Restraining is not allowed in the table"],
             "c": 1,
             "why": "The payoffs say a lone restrainer is worse off by 1 and the other nine are better off by a share of the grass. Greed would be "
                    "a wish for more than the pasture can carry, and none of the numbers contains one. Talk would not change the payoffs."},
            {"q": "A fee of 11 on each animal added makes restraint the equilibrium. Why 11 and not 5?",
             "a": ["Eleven is the smallest fee that stops adding paying when no other herder restrains",
                   "A fee of 5 cannot be collected",
                   "Eleven exceeds the most any herder gains by adding, 10, so adding never pays",
                   "A fee of 5 makes restraining the worse choice for everyone"],
             "c": 2,
             "why": "Adding gains 1 + k over restraining, up to 10 when the nine others restrain. The fee has to beat that gain at "
                    "every k, and the hard case is k = 9, not k = 0: when no other herder restrains the gain is only 1, and a fee of 2 "
                    "already covers it. A fee of 5 stops adding paying when few restrain but not when most do, so some herders still "
                    "add. The fee is subtracted from the adder only and does not touch restraining."},
            {"q": "Which change would end the tragedy while leaving each herder's wish for more animals as it is?",
             "a": ["Ask the herders to want fewer animals",
                   "Make the herder who adds an animal pay for what it costs the others",
                   "Add more herders, so that each is a smaller part of the whole",
                   "Tell each herder what the others are doing"],
             "c": 1,
             "why": "The tragedy comes from the payoffs, and the fee changes them while leaving wishes alone. Asking for fewer wishes "
                    "attacks the wrong cause; more herders raise each herder's share of the cost to others, and information changes nothing "
                    "when adding already dominates."},
        ],
        "mistakes": [
            ("Thinking the tragedy requires greed",
             "No herder in the table wants more than one extra animal, and the herders of the regulated preset want exactly the same. "
             "The equilibrium is bad because the cost of the extra animal falls on the nine others: add the fee that moves the "
             "cost to the adder and all ten restrain. Greed would be a change in wishes; the tragedy needs only a change in who pays."),
            ("Mistaking the equilibrium for the best the herders can do",
             "No herder gains by changing alone at four each, and the total of `40` is still below the `120` of all restraining and the "
             "`121` of the best split. Stability is not merit, as in “The Prisoner's Dilemma”."),
            ("Thinking every shared resource is a tragedy",
             "Three herders on the same pasture have no gap between the equilibrium and the optimum, since three animals "
             "added do not crowd it. The lab's verdict depends on the size of the cost to others in comparison with the gain, and "
             "different payoffs can remove it."),
        ],
        "standard": ("Finish when you can find the gap and say what closes it.",
                     "Write each herder's payoff as a function of how many others restrain, find the dominance verdict and the "
                     "equilibrium, find the best total, state the difference, and choose a fee that makes restraint dominate."),
        "note": "The yield rule here, a fixed number less the animals grazing, is the simplest that makes each animal "
                "worse for all the others. Drag the number of herders from three up to ten and read where the equilibrium total "
                "stops matching the best total. The last tile, the share of cooperators after some generations, is the "
                "replicator step of “The Evolution of Cooperation”; with the generations at zero it repeats the starting share.",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "public-goods-and-free-riding",
        "title": "Public Goods and Free-Riding",
        "module": "Many players",
        "one_line": "A contribution that benefits everyone returns little to the contributor, so each does better by letting the others pay.",
        "summary": (
            "In a public-goods game each of ten people may put a sum into a pool that is multiplied and shared equally. "
            "If the multiplier is smaller than the group, each contribution returns less to its giver than it cost, "
            "and not contributing dominates. The lab prints what one free-rider gains, what universal free-riding loses, "
            "and where the dilemma stops."
        ),
        "key": [
            "a good for all returns a share to me",
            "multiplier below the group: free-riding wins",
            "one free-rider gains, all free-riding loses",
            "multiplier above the group: giving wins",
        ],
        "key_label": "A share of a pool I fill",
        "concepts_intro": (
            "The structure is the commons turned around: there a cost fell on others, here a benefit does."
        ),
        "concepts": [
            ("The pool and the share",
             "Each person contributes a fixed sum or nothing. The pool is multiplied and divided equally among all, "
             "contributors or not, so a contributor gets back only the multiplier over the group size of what was given."),
            ("A free-rider takes the share and keeps the sum",
             "The person who does not contribute still receives an equal share of the pool. Compared with contributing, "
             "that is the same share less the contribution, and the difference is the free-rider's gain."),
            ("The ratio decides",
             "What matters is the multiplier against the number of people. Below the group size contributing loses on "
             "every contribution, at it contributing breaks even, and above it contributing pays whatever others do."),
        ],
        "read_title": "Who pays for the lighthouse",
        "read_intro": "One pool, ten people, and the arithmetic of a share.",
        "body": [
            ("p", "Ten people are each given `10`. Each may put it into a common pool or keep it. The pool is tripled and divided "
                  "equally among all ten, whether they contributed or not. A contribution of `10` therefore grows to `30` in the pool, "
                  "and the contributor gets back one tenth of that, `3`, as does every one of the nine others."),
            ("p", "As in the commons, count the others, and let `k` be how many of the other nine contribute. "
                  "If I contribute, the pool holds `k + 1` contributions and I keep none of my `10`; if I do not, it holds "
                  "`k` and I keep mine. In both cases I receive a tenth of three times the pool."),
            ("math", [
                "C(k) = 3·(k + 1) − 10 = 3·k − 7",
                "D(k) = 3·k",
            ]),
            ("p", "The difference is `D(k) − C(k) = 7` for every `k`. Not contributing pays `7` more than contributing "
                  "whatever the others do, so not contributing dominates, and the lab's tile for dominance says so. "
                  "Each contribution is worth `30` to the group and `3` to the giver, who has paid `10` for it."),
            ("def", ("Free-rider",
                     "A <strong>free-rider</strong> receives the benefit of a good without bearing a share of its cost. In the "
                     "game, a free-rider is a person who does not contribute and takes a share of the pool.")),
            ("h3", "What one free-rider gains, and what all of them lose"),
            ("p", "If nine people contribute and I do not, I get `D(9) = 27`. If I had contributed too I should have had "
                  "`C(9) = 20`. A lone free-rider gains `7`. Now let everyone do as I did. Nobody contributes, the pool is "
                  "empty, and each gets `0` where universal contribution would have given `20`. Each person loses `20`. "
                  "The lab prints both: the gain alone and the loss when everyone does it."),
            ("p", "The best total is when all ten contribute: each receives `20`, and the sum is `200`. Against that, the "
                  "only equilibrium has no one contributing, and the sum is `0`. The good would benefit everyone, and "
                  "that is not enough to get anyone to pay for it."),
            ("h3", "Where the dilemma stops"),
            ("p", "It stops when the share is large enough. Two people with the same tripling have a share of one half, so a "
                  "contribution of `10` returns `15` to its giver. Now contributing pays `5` more than not contributing, "
                  "whatever the other does, and contributing dominates. With ten people and a multiplier of exactly ten, a "
                  "contribution of `10` becomes `100` in the pool and a tenth of that, `10`, returns to its giver: it returns "
                  "exactly what it cost, and the lab finds neither choice dominant and every number of contributors an equilibrium."),
            ("p", "So the rule is the comparison of the multiplier with the group. Below the group size the dilemma holds, and the "
                  "larger the group, the smaller each person's share of a given multiplier. Public goods are hard to supply "
                  "for large groups, easy for small ones, and the lab computes where the line falls. What it does not do is say "
                  "that real people behave like the table, and experiments in which they give something are not refuted by it, "
                  "for a person who values giving has a different table."),
        ],
        "lab": ("choicekit", {
            "mode": "commons",
            "gens": 0,
            "presets": [
                {"id": "public-goods", "label": "Ten people, a contribution of 10, tripled",
                 "n": 10, "payC": "3*10*(k + 1)/n - 10", "payD": "3*10*k/n", "x0": "1/2", "gens": 0, "expect": {"cmDom": "Defect dominates", "cmOpt": "all 10 cooperate: total 200", "cmUniv": "alone +7, everyone −20"}},
                {"id": "small-group", "label": "Two people, tripled",
                 "n": 2, "payC": "3*10*(k + 1)/n - 10", "payD": "3*10*k/n", "x0": "1/2", "gens": 0, "expect": {"cmDom": "Cooperate dominates", "cmOpt": "all 2 cooperate: total 40", "cmUniv": "alone −5, everyone −20"}},
                {"id": "threshold", "label": "Ten people, multiplied by ten",
                 "n": 10, "payC": "10*10*(k + 1)/n - 10", "payD": "10*10*k/n", "x0": "1/2", "gens": 0, "expect": {"cmDom": "neither", "cmEq": "k* = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10", "cmUniv": "alone 0, everyone −90"}},
            ],
            "panel_title": "Change the multiplier or the size of the group",
            "panel_intro": "A payoff is the multiplier times the contribution times the contributors, over the number of people, less "
                           "what a contributor gave. Change the multiplier and find where dominance flips.",
        }),
        "steps_title": "Setting up a public-goods game",
        "steps_intro": "Five moves from the rules to the verdict.",
        "steps": [
            ("State the rules in three numbers",
             "How many people, how much each may give, and by what factor the pool is multiplied before it is shared equally."),
            ("Write what a contributor gets with k of the others contributing",
             "The multiplier times the contribution times `k + 1`, over the group size, less the contribution."),
            ("Write what a non-contributor gets",
             "The same share of a pool with `k` contributions in it, and no cost."),
            ("Subtract",
             "If the difference is positive at every `k`, not contributing dominates. If it is negative at every `k`, contributing does."),
            ("Compute the universalisation numbers",
             "What a lone free-rider gains, what everyone loses if all free-ride, and the total when all contribute."),
        ],
        "worked": {
            "title": "Ten people, tripled, a contribution of ten",
            "intro": ["Each contribution of 10 becomes 30 in the pool, and the pool is shared among ten."],
            "lines": [
                "C(k) = 3(k + 1) - 10 = 3k - 7",
                "D(k) = 3k",
                "D(k) - C(k) = 7 for every k: not giving dominates",
                "All contribute: C(9) = 20 each, 200 in all",
                "No one contributes: 0 each",
                "One free-rider among nine givers: D(9) = 27, gain 7",
            ],
            "after": [
                "A free-rider gains `7` and the group, if all do likewise, loses `20` a head. Every step of the "
                "reasoning is the reasoning of a person who is correct about their own payoff.",
            ],
        },
        "quiz_title": "Shares and free-riders",
        "quiz": [
            {"q": "Ten people, a contribution of 10, a multiplier of 3. What does a contributor net from their own contribution?",
             "a": ["+20, the benefit to the group",
                   "−7, which is 3 back on 10 given",
                   "0, since the pool is shared equally",
                   "+3, the share"],
             "c": 1,
             "why": "The contribution of 10 returns a tenth of 30, which is 3, so the giver is 7 down. The 20 is not what the giver "
                    "receives, and +3 ignores the 10 that was paid."},
            {"q": "Nine others contribute. What does the tenth person get by contributing and by not contributing?",
             "a": ["20 by contributing and 27 by not contributing",
                   "27 by contributing and 20 by not contributing",
                   "20 by contributing and 0 by not contributing",
                   "30 by contributing and 27 by not contributing"],
             "c": 0,
             "why": "With k = 9 the contributor gets 3·10 − 7 = 20 and the non-contributor gets 3·9 = 27. The other pairs reverse the "
                    "payoffs, or forget that the non-contributor also receives a share of the pool."},
            {"q": "Two people, a contribution of 10, a multiplier of 3. What does the lab report for dominance?",
             "a": ["Defect dominates, as with ten people",
                   "Neither dominates, since the group is small",
                   "Every number of contributors is an equilibrium",
                   "Cooperate dominates"],
             "c": 3,
             "why": "Each contribution returns half of 30, which is 15, against a cost of 10, so contributing pays 5 more whatever "
                    "the other does. The multiplier is above the group size. Smallness of the group does not make it neutral, "
                    "and the tie of every equilibrium comes only when the multiplier equals the group size."},
            {"q": "Ten people and a multiplier of 10. What happens to a person who gives 10?",
             "a": ["They lose, since they gave more than they got",
                   "They get back exactly 10, so neither choice dominates",
                   "They gain, since the pool is multiplied",
                   "They get back nothing, since no one else gives"],
             "c": 1,
             "why": "The pool grows tenfold and is divided among ten, so a contribution returns exactly what it cost to its giver. "
                    "The giver is neither better nor worse off, and the lab shows neither choice dominating. Gain would need "
                    "a multiplier above the group size, and loss one below."},
        ],
        "mistakes": [
            ("Thinking that if everyone benefits from the good, everyone will pay for it",
             "A contribution of `10` is worth `30` to the group and returns `3` to the giver, so the benefit to everyone does not "
             "reach the person who decides. Not contributing dominates by `7`. The good is worth having, `20` a head against `0`, "
             "and the table still has nobody paying."),
            ("Confusing the free-rider's gain with the group's loss",
             "One free-rider among nine givers gains `7`; everyone free-riding costs each person `20`. A person may reason correctly "
             "from the first number and the group ends up with the second."),
            ("Thinking any shared good is a dilemma",
             "The dilemma depends on the multiplier being below the group size. With two people and a multiplier of 3 contributing "
             "dominates, and with ten people and a multiplier of ten the two choices tie. The lab finds the line by changing the multiplier."),
        ],
        "standard": ("Finish when you can say whether a public-goods game is a dilemma and by how much.",
                     "Given the number of people, the contribution and the multiplier, write both payoff lines, state the "
                     "dominance verdict, compute what a lone free-rider gains and what universal free-riding costs each person, and find the break-even multiplier."),
        "note": "The commons and the public good are one dilemma with the sign turned around: a cost that falls on others "
                "there, a benefit that falls on others here. Real public goods are often provided by compulsion, which is a change "
                "to the payoffs of the kind the previous lessons studied. As in the commons, the last tile belongs to "
                "“The Evolution of Cooperation” and only repeats the starting share while the generations stay at zero.",
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "the-evolution-of-cooperation",
        "title": "The Evolution of Cooperation",
        "module": "Many players",
        "one_line": "In a population, a type spreads when it out-earns the other type, and what spreads need not be good for the group.",
        "summary": (
            "Instead of choosing, the players are born cooperators or defectors, and each generation a type grows in "
            "proportion to its average payoff. In the prisoner's dilemma the defectors out-earn the cooperators at "
            "every share and take over; in the stag hunt, cooperators win from above a threshold and lose from below it; "
            "and when cooperators meet their own kind more often than chance, the dilemma payoffs can favour them."
        ),
        "key": [
            "new share = share · payoff / mean payoff",
            "dilemma: defectors out-earn at every share",
            "stag hunt: the winner depends on the start",
            "selection compares types, not populations",
        ],
        "key_label": "One exact generation at a time",
        "concepts_intro": (
            "The replicator step replaces choice with inheritance. The three ideas below are what the lab computes."
        ),
        "concepts": [
            ("Fitness is the average payoff",
             "A cooperator meets another individual at random and receives the payoff for that pairing. Its average, "
             "over the chance of meeting a cooperator, is the cooperators' fitness, and the defectors have their own."),
            ("A share grows by its relative fitness",
             "The next generation's share of cooperators is the old share times the cooperators' fitness, divided by "
             "the population's mean fitness. If cooperators earn more than the mean their share rises, and if less, it falls."),
            ("Rest points and which ones hold",
             "A share that does not move is a rest point. A rest point is stable if shares nearby move toward it, and in the "
             "stag hunt the interior one is not: it divides the starts that end in cooperation from the starts that end in defection."),
        ],
        "read_title": "Shares, generation by generation",
        "read_intro": "The step, applied to the dilemma, the stag hunt and a population that sorts itself.",
        "body": [
            ("p", "Everything so far has had players who choose. Here each individual is born a cooperator or a defector "
                  "and plays that type against one other individual drawn at random. A share `x` of the population "
                  "cooperates, so a cooperator meets a cooperator with chance `x` and a defector with chance `1 − x`. "
                  "The payoffs are fitness: the number of offspring, who inherit the type."),
            ("def", ("Replicator step",
                     "With cooperators' average payoff <em>fC</em> and defectors' <em>fD</em>, the next generation's cooperating share is "
                     "<em>x′ = x·fC / (x·fC + (1 − x)·fD)</em>: the old share times its payoff, over the population's mean payoff.")),
            ("p", "Take the dilemma of “The Prisoner's Dilemma”, with `R = 3`, `S = 0`, `T = 5` and `P = 1`. A cooperator "
                  "earns `3` against a cooperator and `0` against a defector, so on average `3·x`. A defector earns `5` and `1`, so "
                  "on average `1 + 4·x`. Start with half of the population cooperating, `x = 1/2`."),
            ("math", [
                "fC = 3·(1/2) = 3/2",
                "fD = 1 + 4·(1/2) = 3",
                "x′ = (1/2)·(3/2) / ((1/2)·(3/2) + (1/2)·3) = 1/3",
            ]),
            ("p", "After one generation a third of the population cooperates. The defectors out-earn the cooperators by "
                  "`1 + x` at every share, so the cooperating share falls each generation, and the lab's longer run, "
                  "five generations from the same start, ends close to zero."),
            ("p", "Compare what the two populations earn. A population of cooperators averages `3` each and a population of "
                  "defectors averages `1`, and selection still moves toward the defectors. Selection compares types "
                  "inside a population, one against the other, and the mean of the whole is nothing it looks at."),
            ("h3", "The stag hunt"),
            ("p", "In the stag hunt of “Coordination, Conventions and the Stag Hunt”, stag pays `4` against stag and `0` against "
                  "hare, and hare pays `3` whatever the other does. A stag hunter earns `4·x` and a hare hunter earns `3`. They "
                  "tie at `x = 3/4`, the very number that was the belief threshold for hunting stag. Above it stag hunters out-earn "
                  "hare hunters and grow; below it they shrink."),
            ("p", "From `x = 4/5` the stag hunters' share rises, to `64/79` in one generation. From `x = 1/2` it falls, to `2/5`. "
                  "Both populations are in equilibrium at their ends, all stag and all hare, and which end is reached depends on the "
                  "start. History, in the sense of where the population began, settles a stag hunt in a way it cannot settle the dilemma."),
            ("h3", "Meeting your own kind"),
            ("p", "Suppose the dilemma's payoffs are unchanged but half of every individual's meetings are with its own kind and half "
                  "are at random. A cooperator's average is then `3/2 + (3/2)·x` and a defector's is `1 + 2·x`. At `x = 1/2` that "
                  "is `9/4` against `2`, and the cooperating share rises, to `9/17` in one generation."),
            ("p", "Nothing in the payoffs has become kinder. The change is in who meets whom, and with enough of it the "
                  "dilemma's cooperators do better than its defectors. This is why the repeated games of earlier lessons and "
                  "the structured populations of biology can sustain cooperation that a well-mixed population cannot. "
                  "What the replicator step does not show is how any of this is inherited, or what happens when a rare new type appears."),
        ],
        "lab": ("choicekit", {
            "mode": "commons",
            "gens": 5,
            "presets": [
                {"id": "pd-evolve", "label": "The dilemma, half cooperators, five generations",
                 "n": 2, "payC": "3*k", "payD": "1 + 4*k", "x0": "1/2", "gens": 5, "expect": {"cmShare": "14348907/50660543233"}},
                {"id": "pd-first-step", "label": "The dilemma, half cooperators, one generation",
                 "n": 2, "payC": "3*k", "payD": "1 + 4*k", "x0": "1/2", "gens": 1, "expect": {"cmShare": "1/3"}},
                {"id": "stag-evolve", "label": "The stag hunt, four fifths stag hunters",
                 "n": 2, "payC": "4*k", "payD": "3", "x0": "4/5", "gens": 5, "expect": {"cmShare": "85070591730234615865843651857942052864/98444752461727794529217939193237846379"}},
                {"id": "stag-doubt", "label": "The stag hunt, half stag hunters",
                 "n": 2, "payC": "4*k", "payD": "3", "x0": "1/2", "gens": 5, "expect": {"cmShare": "70368744177664/159919526031198379"}},
                {"id": "assortment", "label": "The dilemma with half of the meetings among one's own kind, one generation",
                 "n": 2, "payC": "3/2 + 3*k/2", "payD": "1 + 2*k", "x0": "1/2", "gens": 1, "expect": {"cmShare": "9/17"}},
            ],
            "panel_title": "Set a starting share and a number of generations",
            "panel_intro": "With two players k is the cooperating share itself. Run the dilemma for one generation and for "
                           "five, then try starting shares on either side of 3/4 in the stag hunt.",
        }),
        "steps_title": "Running the replicator step",
        "steps_intro": "One generation by hand, and then as many as the lab will run.",
        "steps": [
            ("Write each type's average payoff as a function of the share",
             "A cooperator's is its payoff against a cooperator times `x` plus its payoff against a defector times `1 − x`. "
             "A defector's is the same with its own payoffs."),
            ("Evaluate both at the starting share",
             "Use exact fractions. The two numbers are `fC` and `fD`."),
            ("Form the mean payoff",
             "It is `x·fC + (1 − x)·fD`, the average over the whole population. It must be positive."),
            ("Divide to get the new share",
             "The cooperators' part of the mean over the whole mean is `x′`. If it is above `x` the cooperators have grown."),
            ("Repeat, and look for where the share stops",
             "A share that returns to itself is a rest point. Check which way the neighbouring shares move."),
        ],
        "worked": {
            "title": "One generation of the dilemma",
            "intro": ["Payoffs 3, 0, 5, 1 and a starting share of one half."],
            "lines": [
                "Cooperator: 3 x 1/2 + 0 x 1/2 = 3/2",
                "Defector:   5 x 1/2 + 1 x 1/2 = 3",
                "Mean:       1/2 x 3/2 + 1/2 x 3 = 9/4",
                "New share:  (1/2 x 3/2) / (9/4) = 1/3",
                "Stag hunt from 4/5: stag 16/5, hare 3: share rises",
                "Stag hunt from 1/2: stag 2, hare 3: share falls to 2/5",
            ],
            "after": [
                "The mean payoff of the dilemma's starting population is `9/4`, which is well below the `3` of a population of cooperators. "
                "The step ignores that: it compares `3/2` with `3` and the defectors grow.",
            ],
        },
        "quiz_title": "Where a population goes",
        "quiz": [
            {"q": "The dilemma with payoffs 3, 0, 5, 1 and half the population cooperating. What is the cooperating share a generation later?",
             "a": ["1/2, since the dilemma is symmetric", "2/3", "3/4", "1/3"],
             "c": 3,
             "why": "Cooperators earn 3/2 and defectors earn 3, so the cooperators' part of the mean is (1/2)(3/2) over 9/4, which is 1/3. "
                    "Symmetry of the table does not make the types earn equally, and 2/3 is the defectors' share, not the cooperators'."},
            {"q": "A population of cooperators averages 3 and a population of defectors averages 1. Why does the dilemma population still move toward defection?",
             "a": ["Selection compares the types inside one population, and defectors out-earn cooperators at every share",
                   "The replicator step is wrong when the mean payoff is low",
                   "Cooperators are punished by the defectors",
                   "The cooperators lose their numbers at random"],
             "c": 0,
             "why": "In any mix the defectors earn 1 + x more than the cooperators, so they grow whatever the mean. The step is "
                    "deterministic, no one punishes anyone, and the all-cooperator average never enters the calculation."},
            {"q": "In the stag hunt, from which starting share do the stag hunters grow?",
             "a": ["Only from exactly 3/4", "From any share, because stag pays 4", "From any share above 3/4", "From any share below 3/4"],
             "c": 2,
             "why": "Stag hunters earn 4·x and hare hunters earn 3, so stag hunters out-earn them exactly when x is above 3/4. "
                    "Four is the best payoff but is earned only against stag. At exactly 3/4 the two tie and the share stays where it is."},
            {"q": "Which change, with the four dilemma payoffs untouched, lets cooperation spread from a half share?",
             "a": ["Defectors are fewer to begin with",
                   "The population is larger",
                   "Cooperators meet cooperators more often than chance would give",
                   "The mean payoff of the population is raised"],
             "c": 2,
             "why": "Assortment raises a cooperator's average and lowers a defector's without altering any payoff in the table, and the lab "
                    "shows the share rising from 1/2 to 9/17. In the dilemma defectors out-earn cooperators at every share, so a smaller "
                    "start does not help; and population size and the mean do not appear in the step."},
        ],
        "mistakes": [
            ("Thinking natural selection favours what is good for the group",
             "A population of cooperators averages `3` and one of defectors averages `1`, and the dilemma population moves "
             "to the defectors anyway: from half cooperating to a third in one generation. The step compares the two types' earnings within "
             "the population, so a type that is bad for the group but better for the individual spreads."),
            ("Reading a rising share as a verdict that the type is good",
             "In the stag hunt the stag hunters grow from `4/5` and shrink from `1/2`, under the same payoffs. A share rises because "
             "it out-earns the other type at the share it has, not because it is better in itself."),
            ("Treating the step as a model of choice",
             "No one in the population decides anything. Types are inherited, and the step is a rule for how shares change. "
             "That is why the lab's results are about which types persist and not about what a rational player does."),
        ],
        "standard": ("Finish when you can say where a population goes from a stated start.",
                     "Given a two-player game and a starting share, compute each type's average payoff, apply the replicator step for one "
                     "generation by hand, and say whether the cooperating share rises or falls and where it ends."),
        "note": "The step is a rule given here and not derived, and it assumes an infinite population, no mutation, and payoffs that "
                "are never negative. A different rule for how shares change gives different paths, though for these games the same ends.",
    },
]
