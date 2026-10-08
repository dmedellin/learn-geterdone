"""Games and the Social Contract, lessons 1-6: one-shot games and repeated games.

Every figure the prose states is one the lab prints; the presets pin the tiles
that say why each preset exists (scripts/mathpath/AGENTS.md, "a preset's two
claims").
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "strategic-form-and-best-responses",
        "title": "Strategic Form and Best Responses",
        "module": "One-shot games",
        "one_line": "A game is a table of payoffs, and a best response is the reply that pays most against one particular move.",
        "summary": (
            "Two players each choose once, without seeing the other's choice, and the table says what each receives. "
            "Mark every player's best reply to every move of the other, and the cells where both marks fall are the "
            "cells no one wants to leave. The wrong model is to pick the row with the biggest number in it."
        ),
        "key": [
            "a game: players, strategies, payoffs",
            "best response: the reply that pays most",
            "fix the other's move, then compare",
            "a cell with both marks is stable",
        ],
        "key_label": "A table, two marks, one reading",
        "concepts_intro": (
            "Nothing in this course is harder than reading one small table correctly. "
            "The three ideas below are the whole of the reading."
        ),
        "concepts": [
            ("A game is a table",
             "Each player has a short list of strategies, and every pair of choices, one from each list, is a cell. "
             "The cell holds two numbers: what the row player gets, then what the column player gets. "
             "The players choose without seeing each other's choice, so the table is all there is."),
            ("A best response answers one particular move",
             "Hold the other player's strategy fixed and compare your own payoffs along that line of the table. "
             "The largest is your best response to that strategy. "
             "Change what the other does and the best response may change with it."),
            ("Marks that meet pick out cells",
             "Mark each player's best replies. A cell carrying both players' marks is one where each is already "
             "doing the best available against what the other is doing. The next lessons call such a cell an equilibrium."),
        ],
        "read_title": "Reading a bimatrix",
        "read_intro": "A table with two numbers in every cell, and a procedure for marking it.",
        "body": [
            ("def", ("Strategic form",
                     "A game in <strong>strategic form</strong> lists the players, the strategies open to each, and a payoff "
                     "for each player at every combination of strategies. With two players it is a "
                     "<strong>bimatrix</strong>: the row player's strategies run down the side, the column player's run "
                     "across the top, and each cell shows <em>row payoff, column payoff</em> in that order.")),
            ("p", "A payoff is a number that stands for how much the outcome is worth to the player who gets it. "
                  "Where the number comes from is a question the lab cannot answer; it uses whatever you type, and "
                  "every verdict in this course is a verdict about the payoffs as stated. "
                  "Decision and Rationality is where the numbers earn their meaning as utilities."),
            ("p", "Here is the smallest interesting case. Two people must each choose the left path or the right path "
                  "to a meeting point, and they cannot talk. If both take the left path they meet at a place both "
                  "like very much. If both take the right they meet at a place they like less. If they choose "
                  "differently they do not meet."),
            ("math", [
                "                 column L    column R",
                "     row L        2, 2         0, 0",
                "     row R        0, 0         1, 1",
            ]),
            ("def", ("Best response",
                     "A strategy is a <strong>best response</strong> to a given strategy of the other player when no "
                     "other strategy of one's own pays more against it. Ties are allowed: a best response need only be "
                     "among the largest.")),
            ("p", "To find the row player's best responses, go column by column. If the column player takes L, the row "
                  "player compares `2` for L with `0` for R, and L is the best response. "
                  "If the column player takes R, the comparison is `0` for L against `1` for R, and R is the best "
                  "response. The column player's marks are found the same way, going row by row."),
            ("p", "The two cells where both players' marks fall are the L, L cell and the R, R cell. "
                  "The other two cells carry no pair of marks: in the L, R cell the row player gets `0` and "
                  "would prefer to be playing R."),
            ("h3", "The model to drop"),
            ("p", "A tempting shortcut is to look for the row with the largest number anywhere in it and play that. "
                  "In the table above the largest number is `2`, in row L. But the row player's task is not to find "
                  "a good row in the abstract; it is to answer what the other player does. "
                  "Against column R, row L pays `0` and row R pays `1`, so the row with the biggest number "
                  "is the worse reply."),
            ("example", ("Two other tables",
                         "The lab also holds a game whose only marked cell is D, D (each player's best reply is D "
                         "whatever the other does) and a game, matching pennies, in which no cell carries both marks. "
                         "In matching pennies one player wins if the two coins match and the other wins if they do not, "
                         "so in every cell exactly one player would rather have chosen otherwise.")),
            ("p", "Marking a table is mechanical, and it is meant to be. What is not mechanical is deciding "
                  "which table describes the situation. The same two people with different feelings about the "
                  "right-hand meeting place are playing a different game."),
        ],
        "lab": ("choicekit", {
            "mode": "game",
            "view": "best",
            "presets": [
                {"id": "coordination", "label": "Two paths to a meeting, L and R",
                 "rows": ["L", "R"], "cols": ["L", "R"],
                 "payoffs": [[[2, 2], [0, 0]], [[0, 0], [1, 1]]], "expect": {"gaPure": "(L, L); (R, R)"}},
                {"id": "unique", "label": "Cooperate or defect, 3 / 0 / 5 / 1",
                 "rows": ["C", "D"], "cols": ["C", "D"],
                 "payoffs": [[[3, 3], [0, 5]], [[5, 0], [1, 1]]], "expect": {"gaPure": "(D, D)"}},
                {"id": "none-pure", "label": "Matching pennies",
                 "rows": ["H", "T"], "cols": ["H", "T"],
                 "payoffs": [[[1, -1], [-1, 1]], [[-1, 1], [1, -1]]], "expect": {"gaPure": "none"}},
            ],
            "panel_title": "Mark the best responses",
            "panel_intro": "Each payoff cell carries an asterisk against the player for whom it is a best response. "
                           "Change a payoff and watch which asterisks move; the tile lists the cells where both fall.",
        }),
        "steps_title": "Marking a bimatrix",
        "steps_intro": "Five moves, and the third is the one people skip.",
        "steps": [
            ("Write the strategies down the side and across the top",
             "Row player's down the side, column player's across the top. Each cell holds two numbers, row first."),
            ("Fix one of the column player's strategies",
             "Take one column. The row player cannot change what the other has chosen, only answer it."),
            ("Compare the row player's two numbers inside that column only",
             "Not the whole table, and not the other player's numbers. The larger one gets the mark; a tie marks both."),
            ("Repeat for every column, then do the column player's marks row by row",
             "The column player compares along a row, the mirror image of the row player's comparison."),
            ("Read off the cells with two marks",
             "Those are the cells where each player is already best-responding. A table can have one, several, or none."),
        ],
        "worked": {
            "title": "Marking the meeting game",
            "intro": ["Payoffs are row, column. Row L, column L gives each of them 2."],
            "lines": [
                "Column plays L:  row L pays 2, row R pays 0  -> L",
                "Column plays R:  row L pays 0, row R pays 1  -> R",
                "Row plays L:     column L pays 2, R pays 0   -> L",
                "Row plays R:     column L pays 0, R pays 1   -> R",
                "Both marks fall on: (L, L) and (R, R)",
            ],
            "after": [
                "The two diagonal cells are each a best response to the other. The off-diagonal cells are not: "
                "in each of them one player gets `0` and would switch. Which diagonal cell the pair ends up in "
                "is not settled by the table, which is the question “Coordination, Conventions and the Stag Hunt” takes up.",
            ],
        },
        "quiz_title": "Reading the marks",
        "quiz": [
            {"q": "In the meeting game, the column player is sure to take R. What is the row player's best response?",
             "a": ["L, because row L contains the largest payoff in the table",
                   "R, because it pays 1 against R and L pays 0",
                   "Either, because both rows contain a payoff of at least 0",
                   "L, because the pair would then each get 2"],
             "c": 1,
             "why": "A best response is found by comparing the row player's payoffs within the column the other has "
                    "chosen: 0 for L and 1 for R. The largest number in the table is in the wrong column, and the "
                    "pair getting 2 each is a cell neither can reach alone once the column has chosen R."},
            {"q": "Which statement says what it takes for a cell to carry both players' marks?",
             "a": ["Both players receive the largest payoff in the whole table",
                   "The sum of the two payoffs is largest in that cell",
                   "Each player's strategy there is a best response to the other's strategy there",
                   "The row player's payoff is the largest in its column"],
             "c": 2,
             "why": "Marks are best responses, one set for each player. The first two describe a cell that is good "
                    "for the pair; the cooperate-or-defect table has the largest numbers in a cell that is not "
                    "marked for both. The last gives only the row player's mark."},
            {"q": "In matching pennies the lab reports no cell with both marks. What is true of every cell?",
             "a": ["Both players get the same payoff",
                   "Neither player has a best response",
                   "The game is symmetric, so there is nothing to choose",
                   "One of the two players would do better by changing their own choice"],
             "c": 3,
             "why": "Whichever cell you pick, one player has just lost the match and the other has won it, "
                    "and the loser gains by switching. Best responses exist in every cell; they just never agree."},
        ],
        "mistakes": [
            ("Playing the row with the biggest number in it",
             "A row is judged against a column, never alone. In the meeting game row L holds the table's largest "
             "payoff, 2, and still pays only 0 against column R, where row R pays 1. The question to ask is "
             "&ldquo;what is best given what the other does?&rdquo; and the answer can differ from column to column."),
            ("Comparing numbers in the wrong direction",
             "The row player compares down a column, the column player compares along a row, and each looks "
             "only at their own number in the cell. Comparing the two players' numbers with each other "
             "answers a different question, who is better off, which is no part of a best response."),
            ("Expecting every game to have a cell with both marks",
             "Matching pennies has none. A game can have one cell with both marks, several, or none, "
             "and the next two lessons show what to say in the cases where the answer is not one."),
        ],
        "standard": ("Finish when you can mark a table and say why the marks fall where they do.",
                     "Given any two-by-two bimatrix, mark each player's best replies to each move of the other, "
                     "list the cells with both marks, and say for one unmarked cell which player would switch and to what."),
        "note": "The lab accepts games up to four strategies a side, and changing a payoff in the text box redraws "
                "the marks at once. Try raising a single payoff in the meeting game until row L is the best response "
                "to both columns: then the table has a cell where the row player no longer needs to guess. "
                "The lab also prints a mixed equilibrium and a Pareto verdict; those tiles belong to “The Prisoner's "
                "Dilemma” and “Nash Equilibrium in Pure and Mixed Strategies”, and nothing here depends on them.",
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "the-prisoners-dilemma",
        "title": "The Prisoner's Dilemma",
        "module": "One-shot games",
        "one_line": "Defecting is the better move whatever the other does, and two players who follow it both do worse.",
        "summary": (
            "In the prisoner's dilemma one strategy is strictly better than the other against every move of the "
            "opponent, so both players take it, and the cell they reach pays each less than the cell they passed over. "
            "The dilemma does not come from distrust; it is in the payoffs, and it goes away only when the payoffs change."
        ),
        "key": [
            "defect beats cooperate against either move",
            "so both defect, and (D, D) is the cell",
            "(C, C) pays both more than (D, D) does",
            "the dilemma is in the payoffs, not the mood",
        ],
        "key_label": "Dominance, then the gap",
        "concepts_intro": (
            "One definition, one argument that uses it, and one comparison that makes the argument uncomfortable."
        ),
        "concepts": [
            ("Strict dominance",
             "A strategy strictly dominates another when it pays more against every strategy of the opponent. "
             "A player with a dominating strategy has no need to guess what the other will do."),
            ("The equilibrium of a dominance argument",
             "If both players have a strictly dominating strategy, the pair of them is the only cell where "
             "both are best-responding. Nothing else in the table survives."),
            ("Pareto domination",
             "A cell Pareto-dominates another when it pays someone more and nobody less. In the dilemma the "
             "cell nobody chooses pays both players more than the cell everybody chooses."),
        ],
        "read_title": "Why the best move for each is the worst for both",
        "read_intro": "The argument is four comparisons, and then a fifth that goes the other way.",
        "body": [
            ("p", "Two people are held separately and each is asked to stay silent or to inform on the other. "
                  "The standard payoffs are written C for cooperating with the other prisoner (staying silent) "
                  "and D for defecting (informing). The four payoffs are named: `R` for the reward "
                  "when both cooperate, `T` for the temptation to defect against a cooperator, `P` for the "
                  "punishment when both defect, and `S` for the sucker's payoff of cooperating against a defector."),
            ("math", [
                "                 column C    column D",
                "     row C        3, 3         0, 5",
                "     row D        5, 0         1, 1",
            ]),
            ("p", "Here `R = 3`, `S = 0`, `T = 5` and `P = 1`, and the game is a prisoner's dilemma exactly when "
                  "`T > R > P > S`. The ordering is the whole definition: temptation beats reward, reward beats "
                  "punishment, punishment beats being the sucker."),
            ("def", ("Strict dominance",
                     "Strategy A <strong>strictly dominates</strong> strategy B for a player when A pays more than B "
                     "against every strategy the other player might choose.")),
            ("p", "Take the row player. If the column player cooperates, D pays `5` and C pays `3`. "
                  "If the column player defects, D pays `1` and C pays `0`. D is better in both cases, by `2` "
                  "in the first and by `1` in the second, so D strictly dominates C. The table is symmetric, "
                  "so the same holds for the column player."),
            ("p", "That settles the play without asking what either player believes. A player who is certain the "
                  "other will cooperate should defect, since `5` beats `3`. A player who is certain the other will "
                  "defect should defect, since `1` beats `0`. Each, then, defects, and the cell reached is D, D."),
            ("def", ("Pareto domination",
                     "Cell X <strong>Pareto-dominates</strong> cell Y when every player gets at least as much in X as in Y, "
                     "and at least one gets more.")),
            ("p", "Compare the cell reached with the one passed over. Mutual cooperation gives each player `3` and "
                  "mutual defection gives each `1`. So the only equilibrium of the game is Pareto-dominated, "
                  "and the lab says so in the efficiency tile. That is the dilemma: each has a reason that does not "
                  "depend on the other, and the reasons together defeat both."),
            ("h3", "What changes the game"),
            ("p", "The dilemma needs the ordering and nothing else. Lower the temptation from `5` to `4` and "
                  "the ordering still holds, so D still dominates and the diagnosis stays the same. "
                  "Set the reward at `4` and the temptation at `3`, and against a cooperator cooperating now pays "
                  "`4` where defecting pays `3`. The ordering is broken, D no longer dominates, and mutual "
                  "cooperation becomes an equilibrium alongside mutual defection."),
            ("p", "The lab does not say which of these payoffs describes a real pair of prisoners, or whether "
                  "real prisoners would not also care about each other. That would be a different table, "
                  "and the computation would be on it."),
        ],
        "lab": ("choicekit", {
            "mode": "game",
            "view": "dominance",
            "presets": [
                {"id": "pd", "label": "Reward 3, temptation 5, punishment 1, sucker 0",
                 "rows": ["C", "D"], "cols": ["C", "D"],
                 "payoffs": [[[3, 3], [0, 5]], [[5, 0], [1, 1]]], "expect": {"gaDom": "D dominates for both", "gaPure": "(D, D)", "gaPareto": "(D, D) is dominated by (C, C)"}},
                {"id": "pd-mild", "label": "Temptation 4 instead of 5",
                 "rows": ["C", "D"], "cols": ["C", "D"],
                 "payoffs": [[[3, 3], [0, 4]], [[4, 0], [1, 1]]], "expect": {"gaDom": "D dominates for both", "gaPareto": "(D, D) is dominated by (C, C)"}},
                {"id": "not-pd", "label": "Reward 4 against a cooperator",
                 "rows": ["C", "D"], "cols": ["C", "D"],
                 "payoffs": [[[4, 4], [0, 3]], [[3, 0], [1, 1]]], "expect": {"gaDom": "none", "gaPure": "(C, C); (D, D)"}},
            ],
            "panel_title": "Test the ordering",
            "panel_intro": "Change any payoff and read the three tiles: whether a strategy dominates, which cells are equilibria, "
                           "and whether any equilibrium is Pareto-dominated.",
        }),
        "steps_title": "Showing a game is a dilemma",
        "steps_intro": "Four checks, in this order. A failure at any one means the game is something else.",
        "steps": [
            ("Compare the row player's two payoffs in each column",
             "If the same strategy is larger in every column, it strictly dominates. If it is larger in one and tied or "
             "smaller in the other, it does not."),
            ("Do the same for the column player",
             "Compare along each row. A dilemma needs the dominating strategy for both players."),
            ("Name the cell the two dominating strategies reach",
             "That cell is the only one in which both players are best-responding; no belief about the other changes it."),
            ("Compare it with the other cells",
             "If some cell pays both players more, the equilibrium is Pareto-dominated. That cell, not the equilibrium, "
             "is what the players would choose together."),
        ],
        "worked": {
            "title": "The standard dilemma, line by line",
            "intro": ["Payoffs R = 3, S = 0, T = 5, P = 1."],
            "lines": [
                "Row vs column C:  D pays 5, C pays 3   -> D better",
                "Row vs column D:  D pays 1, C pays 0   -> D better",
                "Column, by symmetry:                   -> D better",
                "Only equilibrium:  (D, D), payoffs 1, 1",
                "Passed over:  (C, C), payoffs 3, 3",
            ],
            "after": [
                "Cooperating together gives each player `3` against `1`. "
                "The shortfall is `2` for each, and no one is able to close it alone: a player who moves to C while the "
                "other holds D drops to `0`.",
            ],
        },
        "quiz_title": "Dominance and the gap",
        "quiz": [
            {"q": "A player is certain the other will cooperate. In the standard dilemma, what does that player do?",
             "a": ["Cooperate, since the other can be trusted",
                   "Defect, since 5 beats 3",
                   "Either, since the other's cooperation fixes the outcome",
                   "Defect, but only if the other might also defect"],
             "c": 1,
             "why": "Trust changes the belief, not the payoffs. Against a certain cooperator defecting pays 5 and "
                    "cooperating pays 3, so the more the player trusts, the more the temptation bites."},
            {"q": "What makes the standard dilemma a dilemma, and not just a game with one equilibrium?",
             "a": ["The players cannot talk to each other before choosing",
                   "Defect dominates for one player but not for the other",
                   "Another cell pays both players more than the equilibrium does",
                   "The equilibrium gives the players different payoffs"],
             "c": 2,
             "why": "The mark of the dilemma is that the equilibrium is Pareto-dominated. Talking changes nothing "
                    "while defect still pays more whatever is promised, and in the standard table the equilibrium "
                    "pays both players the same."},
            {"q": "Temptation falls from 5 to 4, the other payoffs unchanged. What does the lab report for dominance?",
             "a": ["Defect still dominates for both, since 4 beats 3 and 1 beats 0",
                   "Defect no longer dominates, because the temptation is smaller",
                   "Cooperate now dominates for both",
                   "Neither strategy dominates, so the game is no longer symmetric"],
             "c": 0,
             "why": "Against a cooperator D pays 4 against 3, and against a defector 1 against 0. The ordering "
                    "T above R above P above S still holds, so the dilemma survives a milder temptation."},
            {"q": "Which change turns the dilemma into a game where cooperating can be an equilibrium?",
             "a": ["Lower the punishment for mutual defection from 1 to 0",
                   "Let the players talk before they choose",
                   "Tell the players the payoffs are fair",
                   "Make cooperating against a cooperator pay more than defecting against one: reward 4, temptation 3"],
             "c": 3,
             "why": "Cooperating becomes a best response to cooperating only if it pays more than defecting does there, "
                    "which is a change in the table. Lowering the punishment leaves D at least as good everywhere, and talk or "
                    "a reassurance changes no payoff in this table, so D still pays more whatever is promised."},
        ],
        "mistakes": [
            ("Thinking the dilemma comes from distrust, and would vanish between people who trust each other",
             "Defect dominates, and a dominating strategy is best whatever the player believes about the other. "
             "Against a certain cooperator defecting pays `5` and cooperating `3`, so trust makes defecting "
             "more tempting, not less. What can dissolve the dilemma is a different table, such as the one "
             "with reward `4` and temptation `3`: there cooperating against a cooperator pays more than defecting, "
             "which is to say the players value the outcomes differently."),
            ("Reading the equilibrium as the best the pair can do",
             "It is the cell where each is best-responding, which is a different thing. The cell passed over "
             "gives both players `3` against the `1` they reach, and the dilemma is that gap."),
            ("Treating &ldquo;defect&rdquo; as a verdict on the players",
             "Both strategies are names for columns in a table. The argument takes no view on who is wicked; "
             "it takes the payoffs as given and shows what follows."),
        ],
        "standard": ("Finish when you can prove a game is a dilemma, or show it is not.",
                     "Given a two-by-two table, check dominance for each player, name the cell the dominating strategies "
                     "reach, and say whether another cell Pareto-dominates it. Then change one payoff so the verdict flips and say which."),
        "note": "The cooperate-or-defect labels are conventional and the payoffs here are the usual teaching numbers; "
                "only the ordering of the four matters for the diagnosis. The prisoner's dilemma returns three times in "
                "this course: repeated, among many players, and as the shape of Hobbes's state of nature.",
    },
    # ---------------------------------------------------------------- 03
    {
        "slug": "nash-equilibrium-in-pure-and-mixed-strategies",
        "title": "Nash Equilibrium in Pure and Mixed Strategies",
        "module": "One-shot games",
        "one_line": "An equilibrium is a pair of strategies, each a best response to the other, and where no cell qualifies the pair may randomise.",
        "summary": (
            "A Nash equilibrium is a combination of strategies in which no player gains by changing alone. "
            "Some games have several such cells and some have none, and for the games with none a player may mix "
            "strategies with chosen probabilities. The mixed equilibrium of a two-by-two game is found exactly, "
            "by making each player's mix leave the other indifferent."
        ),
        "key": [
            "Nash: no player gains by moving alone",
            "pure: a cell where both best-respond",
            "mixed: weights that leave the other even",
            "an equilibrium need not be the best outcome",
        ],
        "key_label": "Mutual best response",
        "concepts_intro": (
            "The definition is one sentence. Everything else in the lesson is what it does and does not promise."
        ),
        "concepts": [
            ("Equilibrium is mutual best response",
             "A combination of strategies is a Nash equilibrium when each player's strategy is a best response to the "
             "others'. Check it cell by cell: ask of each player whether switching alone would pay."),
            ("A mixed strategy is a set of probabilities",
             "A player who mixes picks each pure strategy with a stated probability, and a mix is a best response "
             "only if every strategy used in it is itself a best response. That is why a mixing player must be indifferent "
             "between the strategies mixed."),
            ("Equilibrium describes stability, not merit",
             "The definition says nothing about whether the outcome is good for the pair. A game may have an equilibrium "
             "that both would swap for another cell, and the previous lesson already showed one."),
        ],
        "read_title": "Pure cells, and the mix when there are none",
        "read_intro": "Three games, the third of which has no pure equilibrium.",
        "body": [
            ("def", ("Nash equilibrium",
                     "A combination of strategies, one for each player, is a <strong>Nash equilibrium</strong> when no "
                     "player can get a larger payoff by changing their own strategy while the others keep theirs. "
                     "An equilibrium in <strong>pure strategies</strong> is a cell of the table; an equilibrium in "
                     "<strong>mixed strategies</strong> gives each player a probability for each pure strategy.")),
            ("p", "Pure equilibria are the doubly marked cells of the previous lesson, and a game can have none, one, "
                  "or several. Chicken has two. Two drivers head for each other on a narrow road and each can swerve "
                  "or go straight. If both swerve nothing is lost. If one swerves and the other does not, the one who "
                  "swerves gets `-1` and the other gets `1`. If neither swerves they crash and each gets `-10`."),
            ("math", [
                "                    column Swerve    column Straight",
                "     row Swerve         0, 0             -1, 1",
                "     row Straight       1, -1           -10, -10",
            ]),
            ("p", "The cells Swerve, Straight and Straight, Swerve are equilibria. In the first, the driver going straight "
                  "gets `1` and would get `0` by swerving, and the driver who swerved gets `-1` and would get `-10` "
                  "by going straight. Swerve, Swerve is not an equilibrium, because either driver gains by going straight. "
                  "It is the one cell in which nobody is hurt, and equilibrium does not choose it."),
            ("p", "Matching pennies is the opposite case. No cell is an equilibrium, because in every cell the player who "
                  "loses the match would rather have chosen the other side. Nash's theorem says that every game with "
                  "finitely many strategies has an equilibrium if mixed strategies are allowed. The theorem is stated "
                  "here and not proved. What the lab does is compute the mix for a two-by-two game."),
            ("h3", "Solving for the mix"),
            ("p", "Let the column player swerve with probability `q`. The row player's expected payoff from swerving "
                  "is `0·q − 1·(1 − q)`, which is `q − 1`. From going straight it is `1·q − 10·(1 − q)`, "
                  "which is `11q − 10`. A row player who mixes must be indifferent between the two, so the column "
                  "player's probability is the one that makes them equal:"),
            ("math", [
                "q − 1  =  11q − 10",
                "9  =  10q",
                "q  =  9/10",
            ]),
            ("p", "The column player swerves nine times in ten. The table is symmetric, so the row player does too. "
                  "At that pair of mixes each driver expects `-1/10`, which is below the `0` each would get if "
                  "both simply swerved, and the two crash with probability `1/10 · 1/10`, one time in a hundred. "
                  "The mixed equilibrium is an equilibrium in the full sense, since at it neither driver gains by changing "
                  "alone, and it is worse for both than the cell it does not use."),
            ("p", "The surprise is whose numbers fix whose mix. Each player's probability is chosen so that the "
                  "<em>other</em> is indifferent. A player does not randomise to be unpredictable at the cost of "
                  "expected payoff; they randomise because, at that mix, the opponent has no better strategy to move to."),
        ],
        "lab": ("choicekit", {
            "mode": "game",
            "view": "best",
            "presets": [
                {"id": "pennies", "label": "Matching pennies, heads and tails",
                 "rows": ["H", "T"], "cols": ["H", "T"],
                 "payoffs": [[[1, -1], [-1, 1]], [[-1, 1], [1, -1]]], "expect": {"gaPure": "none", "gaMixed": "row H: 1/2, col H: 1/2"}},
                {"id": "chicken", "label": "Chicken, crash costs 10",
                 "rows": ["Swerve", "Straight"], "cols": ["Swerve", "Straight"],
                 "payoffs": [[[0, 0], [-1, 1]], [[1, -1], [-10, -10]]], "expect": {"gaPure": "(Swerve, Straight); (Straight, Swerve)", "gaMixed": "row Swerve: 9/10, col Swerve: 9/10"}},
                {"id": "stag", "label": "A stag worth 4, a hare worth 3",
                 "rows": ["Stag", "Hare"], "cols": ["Stag", "Hare"],
                 "payoffs": [[[4, 4], [0, 3]], [[3, 0], [3, 3]]], "expect": {"gaPure": "(Stag, Stag); (Hare, Hare)", "gaMixed": "row Stag: 3/4, col Stag: 3/4"}},
            ],
            "panel_title": "Find the pure cells and the mix",
            "panel_intro": "The mixed tile gives each player's probability of the first strategy. "
                           "Change a payoff and the mix moves; when it would leave the interval from 0 to 1, the tile says none.",
        }),
        "steps_title": "Solving a two-by-two game",
        "steps_intro": "Pure cells first, then the mix.",
        "steps": [
            ("Mark the best responses and list the doubly marked cells",
             "These are the pure equilibria. There may be none, one or several."),
            ("Let the column player play the first strategy with probability q",
             "Write the row player's expected payoff from each row as a line in `q`."),
            ("Set the two expected payoffs equal and solve for q",
             "That is the mix that leaves the row player indifferent. If the answer is not strictly between 0 and 1, "
             "no completely mixed equilibrium exists."),
            ("Swap the roles to find the row player's probability",
             "Let the row player play the first strategy with probability `p` and make the column player indifferent."),
            ("Report all of them",
             "Pure and mixed together are the equilibria. Chicken has three, matching pennies has one."),
        ],
        "worked": {
            "title": "The mix in chicken",
            "intro": ["Let q be the chance the column driver swerves."],
            "lines": [
                "Row swerves:      0·q − 1·(1 − q)   =   q − 1",
                "Row goes straight: 1·q − 10·(1 − q) = 11q − 10",
                "Indifference:    q - 1 = 11q - 10",
                "Solve:           10q = 9,   q = 9/10",
                "Each driver expects 0·(9/10) − 1·(1/10) = −1/10",
            ],
            "after": [
                "The same calculation for the row driver gives `9/10` again, since the table is symmetric. "
                "The lab prints this as the mixed equilibrium, with the two pure cells beside it, "
                "and it is the only completely mixed equilibrium the game has.",
            ],
        },
        "quiz_title": "Pure, mixed, and good",
        "quiz": [
            {"q": "In matching pennies each player plays heads and tails half the time. Why can neither gain by switching to all heads?",
             "a": ["Because the two players' payoffs are equal in every cell",
                   "Because against a player mixing half and half, heads and tails have the same expected payoff",
                   "Because heads is not a best response to anything",
                   "Because the game has a pure equilibrium the mix approximates"],
             "c": 1,
             "why": "Against a half-and-half opponent each side wins half the time, so any strategy, pure or mixed, "
                    "earns the same expectation. The players' payoffs are opposite rather than equal, heads is "
                    "the best response to heads, and the game has no pure equilibrium."},
            {"q": "In chicken, the column driver swerves with probability above 9/10. What is the row driver's best response?",
             "a": ["Swerve, because a crash is more likely",
                   "Either, since the mixed equilibrium is the only stable point",
                   "Go straight, since 11q − 10 then exceeds q − 1",
                   "Go straight only with probability 9/10"],
             "c": 2,
             "why": "The two expected payoffs are equal at 9/10, and straight rises faster in q. Above 9/10 going straight "
                    "pays more, so a pure best response exists and the row driver stops mixing."},
            {"q": "Compared with both drivers simply swerving, what does chicken's mixed equilibrium give each driver?",
             "a": ["Exactly the same, since both are equilibria",
                   "More, because the drivers sometimes get the temptation payoff of 1",
                   "More, because equilibrium is the best the pair can do",
                   "Less: an expectation of −1/10 against 0"],
             "c": 3,
             "why": "Both swerving pays 0 each and is not an equilibrium. The mixed equilibrium expects −1/10 and "
                    "carries a one-in-a-hundred chance of the −10 crash. Being an equilibrium does not make a cell good for the pair."},
            {"q": "The lab reports no pure equilibrium for matching pennies. Does that contradict the claim that finite games have equilibria?",
             "a": ["Yes, the lab has found a finite game with none",
                   "Yes, unless the players are allowed to talk",
                   "No, the claim covers mixed equilibria and this game has one",
                   "No, because the game is not really finite"],
             "c": 2,
             "why": "The theorem allows probabilities over strategies, and the lab finds one half and one half for each player. "
                    "The game has two strategies a side, so it is finite, and talk does not enter."},
        ],
        "mistakes": [
            ("Taking an equilibrium to be the best outcome for the group",
             "Equilibrium is a property of each player's reply, and it says nothing about the pair. In chicken "
             "the cell where both swerve pays each `0` and is not an equilibrium, while the mixed equilibrium "
             "expects `-1/10` each and crashes one time in a hundred. The previous lesson's dilemma is the same fact in starker form."),
            ("Reading a player's mix as a way of keeping the opponent guessing",
             "The weights are fixed by the opponent's payoffs, not one's own. Drivers in chicken swerve nine times in ten "
             "because that is the weight at which the other driver is exactly as well off going straight as swerving."),
            ("Expecting one equilibrium per game",
             "Chicken has two pure equilibria and a mixed one. When a table has several, the table by itself does not say "
             "which will be played, and “Coordination, Conventions and the Stag Hunt” is about how people choose between them."),
        ],
        "standard": ("Finish when you can compute the mix of a two-by-two game and check it.",
                     "Given a two-by-two table, list the pure equilibria, write one player's expected payoffs as lines in "
                     "the other's probability, solve for the point where they cross, and say whether that mix is an "
                     "equilibrium by checking that neither player gains from a pure deviation."),
        "note": "Chicken here is the textbook version with a crash costing ten, and its mix depends on that ten: "
                "a crash costing a hundred makes the drivers swerve more often. Try it in the payoffs box.",
    },
    # ---------------------------------------------------------------- 04
    {
        "slug": "coordination-conventions-and-the-stag-hunt",
        "title": "Coordination, Conventions and the Stag Hunt",
        "module": "One-shot games",
        "one_line": "When several equilibria pay, what makes people land on one is a shared expectation, and the belief it takes can be computed.",
        "summary": (
            "In a coordination game both players want to match, and there is more than one way to match. "
            "A convention is an equilibrium that is kept going by each player's expectation that the others keep it, "
            "with no promise needed. In the stag hunt the best match is also the riskier one, and the lab gives the belief "
            "at which the risk is worth taking."
        ),
        "key": [
            "coordination: match, and several matches pay",
            "convention: stable because others conform",
            "two equilibria: one pays most, one is safest",
            "stag is best only above a belief threshold",
        ],
        "key_label": "Which equilibrium, and why",
        "concepts_intro": (
            "A game with two equilibria raises a question the table cannot answer: which one? "
            "Three ideas give the question some structure."
        ),
        "concepts": [
            ("Coordination games",
             "Each player does best by matching the other, and there is more than one match to choose. "
             "The payoffs reward getting on the same page and do not, in the plainest cases, say which page."),
            ("Convention",
             "A convention is a regularity that is an equilibrium of a coordination game that recurs, "
             "and that is followed because the others follow it. Another regularity would have done as well."),
            ("Payoff dominance against risk dominance",
             "One equilibrium may pay both players more while another costs them less if the other player "
             "turns out to be elsewhere. The two properties can pick different equilibria."),
        ],
        "read_title": "Three coordination games",
        "read_intro": "Driving, the stag hunt, and a game where the players disagree about which match is best.",
        "body": [
            ("p", "The driving game is the plainest coordination problem. Two drivers meet on a road and each chooses "
                  "to keep to the left or to the right. If they choose the same side they pass safely and each gets `1`. "
                  "If they choose differently each gets `0`. The lab marks two equilibria, left with left and right with right, "
                  "and gives them identical payoffs."),
            ("def", ("Convention",
                     "A <strong>convention</strong> is a way of behaving, in a coordination game that keeps coming up, "
                     "such that everyone follows it, everyone expects the others to follow it, and everyone prefers to "
                     "follow it provided the others do. Some other way of behaving would have served as well.")),
            ("p", "Driving on the right is a convention in this sense in every country that does it, and so is driving on "
                  "the left. Nothing in the table prefers either. What keeps a country on one side is each driver's "
                  "expectation of the others, and that expectation is in turn kept going by the fact that each "
                  "does best conforming. It does not need anyone to have promised anything, which is why the term "
                  "&ldquo;agreement&rdquo; is the wrong model: an agreement could start a convention, and "
                  "a custom with no origin in any agreement can be one."),
            ("p", "The stag hunt has the same two matched cells with payoffs that differ. Two hunters can each go for a stag "
                  "or for a hare. A stag takes both of them to bring down and is worth `4` to each; a hare can be taken "
                  "alone and is worth `3`. A hunter who goes for a stag alone gets nothing."),
            ("math", [
                "                 column Stag    column Hare",
                "     row Stag       4, 4           0, 3",
                "     row Hare       3, 0           3, 3",
            ]),
            ("p", "Stag with stag and Hare with Hare are both equilibria. The first pays both players more, so it is "
                  "<strong>payoff-dominant</strong>; the second is Pareto-dominated by the first. "
                  "But Hare guarantees `3` whatever the other does, and Stag risks `0`. "
                  "One standard measure of that risk compares what each player would lose by deviating: from "
                  "Stag, Stag a deviator loses `1`, and from Hare, Hare a deviator loses `3`. The equilibrium whose "
                  "product of losses is larger, here `3·3 = 9` against `1·1 = 1`, is <strong>risk-dominant</strong>. "
                  "That is Hare, Hare."),
            ("h3", "The belief at which stag is worth it"),
            ("p", "Let `q` be the probability the hunter gives to the other hunting stag. Going for the stag "
                  "pays `4q`, since it succeeds only when the other joins. Going for the hare pays `3` whatever happens. "
                  "So stag is the better choice exactly when `4q ≥ 3`, that is when `q ≥ 3/4`."),
            ("p", "Three-quarters is the number the lab prints as the mixed equilibrium, now read as a threshold "
                  "on belief. A hunter who is only fifty-fifty about the partner should go for the hare, and a pair "
                  "who both give stag a probability of nine in ten can sustain it. The table does not say which belief "
                  "the pair will have. That depends on what each has seen the other do, which is the part of the "
                  "problem a convention answers and a table cannot."),
            ("p", "A third game, the battle of the sexes, adds disagreement about which match is better. One player "
                  "prefers the opera and the other the football; both prefer going together to going apart. "
                  "With the opera worth `3` to one and `2` to the other, and the football the reverse, the lab marks "
                  "both matches as equilibria and prints a mix in which the row player chooses the opera with "
                  "probability `3/5` and the column player with probability `2/5`. At that mix each expects only `6/5`, "
                  "less than the `2` either gets at the match they like less. The move from a coordination problem "
                  "to a bargaining problem is already visible: even a convention now favours someone."),
        ],
        "lab": ("choicekit", {
            "mode": "game",
            "view": "pareto",
            "presets": [
                {"id": "stag", "label": "Stag worth 4, hare worth 3, a failed stag 0",
                 "rows": ["Stag", "Hare"], "cols": ["Stag", "Hare"],
                 "payoffs": [[[4, 4], [0, 3]], [[3, 0], [3, 3]]], "expect": {"gaPure": "(Stag, Stag); (Hare, Hare)", "gaMixed": "row Stag: 3/4, col Stag: 3/4", "gaPareto": "(Hare, Hare) is dominated by (Stag, Stag)"}},
                {"id": "driving", "label": "Left or right, a match pays 1",
                 "rows": ["Left", "Right"], "cols": ["Left", "Right"],
                 "payoffs": [[[1, 1], [0, 0]], [[0, 0], [1, 1]]], "expect": {"gaPure": "(Left, Left); (Right, Right)", "gaMixed": "row Left: 1/2, col Left: 1/2", "gaPareto": "every equilibrium is efficient"}},
                {"id": "sexes", "label": "Opera or football, each prefers a different match",
                 "rows": ["Opera", "Football"], "cols": ["Opera", "Football"],
                 "payoffs": [[[3, 2], [0, 0]], [[0, 0], [2, 3]]], "expect": {"gaPure": "(Opera, Opera); (Football, Football)", "gaMixed": "row Opera: 3/5, col Opera: 2/5", "gaPareto": "every equilibrium is efficient"}},
            ],
            "panel_title": "Compare the equilibria",
            "panel_intro": "Efficient cells are shown in green and an equilibrium that is not efficient in amber. "
                           "The mixed tile is the probability, for each player, of the first strategy.",
        }),
        "steps_title": "Reading a coordination game",
        "steps_intro": "Five questions about a table with two matching cells.",
        "steps": [
            ("List the pure equilibria",
             "Mark the best responses. A coordination game has at least two doubly marked cells."),
            ("Compare their payoffs",
             "If one pays everyone more, it is payoff-dominant. If the payoffs are the same, the table is silent."),
            ("Find what each player risks",
             "Ask what a player gets in each equilibrium if the other player plays the other strategy."),
            ("Compute the belief threshold",
             "With belief `q` that the other plays the good strategy, write both payoffs and solve for the `q` that makes them equal."),
            ("Say what would settle the choice",
             "Precedent, a signal, or a history of play. These are things outside the table, and a convention is what they leave behind."),
        ],
        "worked": {
            "title": "When is the stag worth hunting",
            "intro": ["Payoffs: stag with stag 4, a lone stag hunter 0, hare 3 whatever happens."],
            "lines": [
                "q = chance the other hunts stag",
                "Hunt stag:  4·q + 0·(1 - q)  =  4q",
                "Hunt hare:  3·q + 3·(1 - q)  =  3",
                "Stag is at least as good when  4q >= 3",
                "so  q >= 3/4",
            ],
            "after": [
                "The lab's mixed equilibrium, `3/4` for each player, is the same number: it is the belief that leaves "
                "the other player indifferent between stag and hare. Read as a threshold on belief it says how much "
                "trust the better equilibrium needs.",
            ],
        },
        "quiz_title": "Matching, risk and belief",
        "quiz": [
            {"q": "In the stag hunt, what probability of the partner hunting stag makes stag at least as good as hare?",
             "a": ["1/4", "1/2", "3/4", "3"],
             "c": 2,
             "why": "Stag pays 4q and hare pays 3, so stag is at least as good when q is at least 3/4. One half is the "
                    "threshold of a symmetric coin flip, which the payoffs do not give."},
            {"q": "Why might sensible hunters settle on hare when both would prefer to have stag?",
             "a": ["Hare is the only equilibrium of the game",
                   "Hare pays 3 whatever the other does, while stag pays 0 if the other goes for hare",
                   "Hare Pareto-dominates stag",
                   "Rational players must pick the risk-dominant strategy"],
             "c": 1,
             "why": "Both are equilibria, and stag with stag Pareto-dominates hare with hare, so the first and third are false. "
                    "Nothing makes risk dominance compulsory: a pair with a history of hunting stag together can keep to it. "
                    "What hare offers is a floor."},
            {"q": "In the driving game the lab marks two cells with identical payoffs. What keeps a country on one side?",
             "a": ["A promise made by every driver",
                   "The larger payoff on that side",
                   "A penalty paid by those who drive on the other side",
                   "Each driver doing best by conforming given that the others do"],
             "c": 3,
             "why": "Conforming is a best response to conformity, and that is sufficient. The payoffs on the two sides are equal, "
                    "a penalty would change the table, and a promise may have started the custom but is not what keeps it going."},
            {"q": "Suppose the hare paid 2 instead of 3 in every cell where it is chosen, and the stag payoffs stayed. What belief makes stag at least as good?",
             "a": ["1/2", "1/4", "2/3", "3/4"],
             "c": 0,
             "why": "Stag pays 4q and hare pays 2, so 4q is at least 2 when q is at least 1/2. A cheaper hare "
                    "makes the stag easier to believe in."},
        ],
        "mistakes": [
            ("Thinking a convention is an agreement",
             "In the driving game the two sides pay the same, and no one signs anything for either. What makes each "
             "side an equilibrium is that conforming is a best response to the others conforming. An agreement "
             "can start such a regularity, but a convention that began in custom is as much a convention as one that began in a treaty."),
            ("Taking the payoff-dominant equilibrium to be the one rational players choose",
             "Stag with stag pays `4` each, against `3` for hare with hare, and rational hunters still end up at hare "
             "when each doubts the other. Rationality alone does not pick between equilibria; expectation does."),
            ("Hunting stag on an even chance",
             "A fifty-fifty belief gives stag an expectation of `2` against the hare's certain `3`. "
             "The better equilibrium needs a belief of three in four, which is the reason trust is hard to start and easy to lose."),
        ],
        "standard": ("Finish when you can compute the belief at which the risky equilibrium is worth it.",
                     "Given a two-by-two coordination game, name its pure equilibria, say which is payoff-dominant and "
                     "which is risk-dominant, and compute the probability of the partner's cooperation above which the "
                     "better equilibrium is the better bet."),
        "note": "Risk dominance has several definitions. The one here, the larger product of deviation losses, is the "
                "standard one for two-by-two games and agrees with the belief threshold: the risk-dominant equilibrium "
                "is the one that is best for the wider range of beliefs.",
    },
    # ---------------------------------------------------------------- 05
    {
        "slug": "repeated-games-and-reciprocity",
        "title": "Repeated Games and Reciprocity",
        "module": "Repeated games",
        "one_line": "Played again and again, the dilemma rewards strategies that answer in kind, and a tournament shows which ones score.",
        "summary": (
            "When the prisoner's dilemma is played for many rounds, a strategy is a rule that turns the history so far "
            "into the next move. The lab plays two named rules against each other round by round and then runs a round robin "
            "of seven. The winner is not the strategy that beats its partners but the one that does well with all of them."
        ),
        "key": [
            "a strategy is a rule: history in, move out",
            "TFT: cooperate first, then copy the last move",
            "a match goes on points, a tournament on sums",
            "never beating a partner can still win",
        ],
        "key_label": "Rules, matches, totals",
        "concepts_intro": (
            "Three words need fixing before the lab means anything: strategy, match, and total."
        ),
        "concepts": [
            ("A strategy is a rule over histories",
             "In a repeated game a strategy does not name a move; it says what to play given everything that has happened. "
             "The lab's seven are all simple: always cooperate, always defect, copy the other's last move, and four more."),
            ("A match is a fixed number of rounds",
             "Two strategies meet for a stated number of rounds, and each earns the sum of its round payoffs. "
             "The record of moves is the evidence for any claim about what a strategy did."),
            ("A tournament sums over partners",
             "In the round robin every strategy meets every strategy, itself included, and its total is the sum "
             "of its scores. One strategy outscoring another in a match is not what the total counts."),
        ],
        "read_title": "Playing the dilemma again",
        "read_intro": "Seven rules, one match read round by round, and a tournament.",
        "body": [
            ("p", "The previous two lessons gave the dilemma one round. Here the same four payoffs, `R = 3`, `S = 0`, "
                  "`T = 5` and `P = 1`, are played over a stated number of rounds by two strategies, and each player's "
                  "score is the sum of what the rounds paid."),
            ("def", ("Strategy in a repeated game",
                     "A <strong>strategy</strong> is a rule that gives a move, C or D, for every possible history of "
                     "play. It may depend on what the other player has done, on what the player has done, and on how many rounds have passed.")),
            ("ul", [
                "<strong>ALLC</strong> always cooperates and <strong>ALLD</strong> always defects.",
                "<strong>TFT</strong> (tit for tat) cooperates in the first round and afterwards copies the other player's previous move.",
                "<strong>GRIM</strong> cooperates until the other player defects once, and defects ever after.",
                "<strong>PAVLOV</strong> cooperates first, then repeats its move if the last round paid `R` or `T`, and switches otherwise; equivalently it cooperates exactly when both players made the same move last round.",
                "<strong>TF2T</strong> (tit for two tats) defects only after two defections in a row.",
                "<strong>STFT</strong> (suspicious tit for tat) is TFT with a defection in the first round.",
            ]),
            ("p", "Take TFT against ALLD for ten rounds. In the first round TFT cooperates and ALLD defects, "
                  "so TFT gets `0` and ALLD gets `5`. From then on TFT copies the defection and both defect for nine "
                  "rounds, one point each round. The lab prints `9` for TFT and `14` for ALLD."),
            ("p", "TFT lost that match, and it can never do better than tie any match: it defects only after being "
                  "defected against, so it cannot score more than its partner. ALLD is the reverse. It scores at least "
                  "as much as its partner in every match, since it can always choose the strictly better move in a round. "
                  "A natural inference is that ALLD is the strategy to beat."),
            ("p", "The round robin refutes it. ALLD takes `50` from ALLC and `30` from PAVLOV, but only `14` from TFT and from GRIM, "
                  "`18` from TF2T, and `10` from itself and from STFT. Meanwhile TFT, GRIM, PAVLOV, ALLC and TF2T "
                  "cooperate in all ten rounds with one another and take `30` each time. Over the whole field TF2T "
                  "scores `185`, TFT `184` and ALLD `146`."),
            ("h3", "Two matches that never defect"),
            ("p", "TFT against TFT cooperates throughout and each scores `30`; so do GRIM and PAVLOV against each "
                  "other, because neither is ever defected against and so neither ever has cause to respond. "
                  "Reciprocity is a rule that is silent when met by cooperation, which is why it does not cost "
                  "anything against a cooperator."),
            ("p", "Two limits belong here. The field is seven rules chosen for the lab, and a different field would "
                  "rank them differently. And the winner at ten rounds is only one point ahead of the next, so "
                  "the order is not stable: change the number of rounds in the lab and watch it move."),
        ],
        "lab": ("choicekit", {
            "mode": "iterated",
            "a": "TFT",
            "b": "ALLD",
            "rounds": 10,
            "presets": [
                {"id": "tft-alld", "label": "Tit for tat against always defect",
                 "R": 3, "S": 0, "T": 5, "P": 1, "a": "TFT", "b": "ALLD", "rounds": 10, "delta": "9/10", "expect": {"itScoreA": "9", "itScoreB": "14", "itWinner": "TF2T: 185"}},
                {"id": "tft-tft", "label": "Tit for tat against itself",
                 "R": 3, "S": 0, "T": 5, "P": 1, "a": "TFT", "b": "TFT", "rounds": 10, "delta": "9/10", "expect": {"itScoreA": "30", "itScoreB": "30"}},
                {"id": "grim-pavlov", "label": "Grim trigger against Pavlov",
                 "R": 3, "S": 0, "T": 5, "P": 1, "a": "GRIM", "b": "PAVLOV", "rounds": 10, "delta": "9/10", "expect": {"itScoreA": "30", "itScoreB": "30"}},
            ],
            "panel_title": "Pick two strategies and a number of rounds",
            "panel_intro": "The table shows the first twelve moves of the match and every strategy's round-robin total "
                           "at the same number of rounds. Change the rounds and watch the order of the totals.",
        }),
        "steps_title": "Reading a match and a tournament",
        "steps_intro": "Match first, then the field.",
        "steps": [
            ("Write each strategy as a rule",
             "State what it plays in round one and what it plays given the history. If you cannot, you do not yet know what the lab ran."),
            ("Play the first few rounds by hand",
             "Round one needs no history. Round two uses round one's moves, and so on."),
            ("Add each side's payoffs",
             "Use `R`, `S`, `T` and `P` for the four move pairs. The score of a match is a sum."),
            ("Compare the totals within the match",
             "This says who won that match. It says nothing yet about the tournament."),
            ("Read the round robin as sums over partners",
             "A strategy's total adds its scores against all seven, including itself. Find which partners it gained from and which it lost to."),
        ],
        "worked": {
            "title": "Tit for tat against always defect",
            "intro": ["Ten rounds, with R = 3, S = 0, T = 5, P = 1."],
            "lines": [
                "Round 1:     TFT plays C, ALLD plays D -> 0 and 5",
                "Rounds 2 to 10: both play D, nine rounds -> 9 and 9",
                "TFT total:   0 + 9 = 9",
                "ALLD total:  5 + 9 = 14",
                "Round robin: TF2T 185, TFT 184, ALLD 146",
            ],
            "after": [
                "TFT loses the match by five and finishes one point behind the winner of the round robin. "
                "ALLD beats or ties every partner it meets and finishes sixth of seven. The two facts are consistent "
                "because the tournament adds points and does not count victories.",
            ],
        },
        "quiz_title": "Matches and totals",
        "quiz": [
            {"q": "Tit for tat meets always defect for ten rounds with the standard payoffs. What are the totals?",
             "a": ["TFT 9 and ALLD 14", "TFT 14 and ALLD 9", "TFT 10 and ALLD 10", "TFT 0 and ALLD 50"],
             "c": 0,
             "why": "TFT is cheated in round one only: 0 against 5. After that both defect and each earns 1 for nine rounds. "
                    "TFT's total is 0 + 9 and ALLD's is 5 + 9."},
            {"q": "ALLD never scores less than its partner in any match, yet finishes near the bottom of the round robin. Why?",
             "a": ["The tournament is rigged against defectors",
                   "ALLD gains only from the strategies it exploits, and earns just 1 a round against the rest",
                   "ALLD loses to TFT in each match",
                   "The round robin counts matches won, and ALLD wins few"],
             "c": 1,
             "why": "Totals are sums of points. Against ALLC ALLD earns 50, but against most partners it settles into mutual "
                    "defection and earns about 10 to 14, while the cooperative strategies earn 30 from one another. "
                    "ALLD does not lose to TFT, and the round robin counts points, not wins."},
            {"q": "TFT meets TFT for ten rounds with the standard payoffs. What does each score?",
             "a": ["10", "50", "30", "9"],
             "c": 2,
             "why": "Neither defects first, so both cooperate in every round and each earns R = 3 ten times."},
            {"q": "Over ten rounds against ALLD, in how many rounds does TFT cooperate?",
             "a": ["None", "Every round", "Five", "Only the first"],
             "c": 3,
             "why": "TFT opens with C and then copies ALLD's previous move, which is always D. The record is C, D, D, D and so on."},
        ],
        "mistakes": [
            ("Thinking the strategy that beats every opponent wins the tournament",
             "ALLD scores at least as much as its partner in every match and still finishes sixth of seven at ten rounds, "
             "on `146` points against `185` for the winner. TFT never beats a partner and finishes one point behind. "
             "A tournament adds points across partners, and strategies that cooperate with one another earn `30` a match where mutual defection earns `10`."),
            ("Reading the winner as the best strategy",
             "The winner is the best of these seven against these seven at this number of rounds. At one round ALLD "
             "and STFT win; at five, TF2T; at eight, TFT and TF2T tie. No claim about the best strategy in general follows."),
            ("Treating reciprocity as a feeling",
             "TFT is a rule with no attitude in it: copy the last move. That it earns well is a fact about the "
             "payoffs and the partners, which is what the next lesson turns into a threshold."),
        ],
        "standard": ("Finish when you can read a match round by round and say why the totals came out as they did.",
                     "Given two of the seven strategies and a number of rounds, write out the moves of the first few rounds, "
                     "sum the payoffs, and say which of the two scored more and by how much."),
        "note": "The seven strategies and the round-robin rules are fixed by the lab; the payoffs and the number of rounds are yours. "
                "Raising the number of rounds to fifty puts TF2T further ahead, and the winner at a single round is "
                "a defector. The last tile, the continuation probability that cooperation needs, belongs to “The Shadow "
                "of the Future”; nothing in this lesson depends on it.",
    },
    # ---------------------------------------------------------------- 06
    {
        "slug": "the-shadow-of-the-future",
        "title": "The Shadow of the Future",
        "module": "Repeated games",
        "one_line": "Cooperation is stable when the future counts for enough, and the amount can be computed from the four payoffs.",
        "summary": (
            "Suppose each round is followed by another with probability delta. Against a partner who punishes defection, "
            "cooperating forever beats defecting once exactly when delta is above a threshold fixed by the four payoffs. "
            "The threshold needs an uncertain end rather than a long game: a last round that is known unravels the whole thing."
        ),
        "key": [
            "δ: the chance there is a next round",
            "GRIM holds if δ ≥ (T − R) / (T − P)",
            "TFT holds if δ ≥ (T − R) / (R − S) as well",
            "a known last round unravels, backwards",
        ],
        "key_label": "How much the future must count",
        "concepts_intro": (
            "The previous lesson ran matches of fixed length. The question here is when a player with a reason to defect has a "
            "reason, larger still, to hold back."
        ),
        "concepts": [
            ("The continuation probability",
             "After every round the game goes on with probability `δ`, so a payoff `n` rounds away is worth `δ` to the "
             "power `n` times as much now. A larger `δ` means the future weighs more."),
            ("A punishment makes defection costly later",
             "A player who defects gains the temptation now, and loses whatever the partner's reply costs in the "
             "rounds that follow. Cooperation is stable when the loss outweighs the gain."),
            ("A known last round has no future",
             "In the final round there is nothing to protect, so defecting dominates; with that round settled, "
             "the one before has no future either. The argument runs backwards to the first round."),
        ],
        "read_title": "When the future outweighs the temptation",
        "read_intro": "Two comparisons, one threshold from each, and the argument for why the end must not be known.",
        "body": [
            ("p", "Take the standard payoffs, `R = 3`, `S = 0`, `T = 5` and `P = 1`, and let the game continue after each "
                  "round with probability `δ`. A payoff `n` rounds away is then worth `δ^n` times as much now, so getting "
                  "`x` every round is worth `x·(1 + δ + δ^2 + …)`. The sum in the brackets is `1 / (1 − δ)` whenever "
                  "`δ` is below `1`: multiply it by `δ` and subtract, and every term but the first cancels. So the value "
                  "of `x` every round is `x / (1 − δ)`, and the expected number of rounds, which is the same sum with "
                  "`x = 1`, is `1 / (1 − δ)`. “The St Petersburg Game” summed one tail of this series; this is the whole of it."),
            ("h3", "Against a player who never forgives"),
            ("p", "GRIM cooperates until it is defected against once and defects forever after. A player who meets "
                  "GRIM can cooperate throughout, or defect and be punished. Cooperating throughout earns "
                  "`R / (1 − δ)`. Defecting at once earns `T` this round and then, with GRIM defecting for good, `P` in every "
                  "later round, worth `δ·P / (1 − δ)` altogether. Cooperation is at least as good when"),
            ("math", [
                "R / (1 − δ)  ≥  T + δ·P / (1 − δ)",
                "R  ≥  T·(1 − δ) + δ·P",
                "δ·(T − P)  ≥  T − R",
                "δ  ≥  (T − R) / (T − P)",
            ]),
            ("p", "With the standard payoffs that is `2 / 4`, or `1/2`."),
            ("h3", "Against a player who forgives"),
            ("p", "TFT punishes only for as long as the other defects. The best deviation against it is one of two. "
                  "Defect forever, which is as bad as it is against GRIM and needs the same `δ`. Or defect once and go "
                  "back to cooperating, which earns `T` now, `S` next round while TFT retaliates and `R` afterwards. "
                  "Comparing the two streams round by round, the first two rounds of cooperating pay `R + δ·R` and the "
                  "two rounds of the deviation pay `T + δ·S`, with everything later equal. Cooperation is at least as good when"),
            ("math", [
                "R + δ·R  ≥  T + δ·S",
                "δ·(R − S)  ≥  T − R",
                "δ  ≥  (T − R) / (R − S)",
            ]),
            ("p", "With the standard payoffs this is `2 / 3`. The lab reports the larger of the two thresholds for TFT, "
                  "since both deviations must be unprofitable, and the first alone for GRIM. With these payoffs the milder "
                  "punishment needs the more patient player, because a deviator who returns to cooperation loses only one round to the retaliation."),
            ("h3", "The end that must not be known"),
            ("p", "Suppose the game lasts exactly one hundred rounds and both players know it. In round one hundred there is "
                  "no later round to punish in, so defecting dominates, as in the one-shot dilemma. Both defect then "
                  "whatever happened before. So in round ninety-nine nothing the players do changes round one hundred, "
                  "the same argument applies, and so on back to the first round. A hundred rounds is not a long game in this "
                  "sense; it is a game with a last round. A game that ends after each round with probability one half "
                  "lasts two rounds on average, and with these payoffs it just sustains cooperation against GRIM."),
        ],
        "lab": ("choicekit", {
            "mode": "iterated",
            "presets": [
                {"id": "standard", "label": "Payoffs 3, 0, 5, 1 and a continuation chance of 9/10",
                 "R": 3, "S": 0, "T": 5, "P": 1, "a": "TFT", "b": "GRIM", "rounds": 10, "delta": "9/10", "expect": {"itThresh": "GRIM 1/2, TFT 2/3: δ = 9/10 sustains"}},
                {"id": "low-delta", "label": "The same payoffs and a continuation chance of 1/4",
                 "R": 3, "S": 0, "T": 5, "P": 1, "a": "TFT", "b": "GRIM", "rounds": 10, "delta": "1/4", "expect": {"itThresh": "GRIM 1/2, TFT 2/3: δ = 1/4 does not"}},
                {"id": "high-temptation", "label": "Payoffs 6, 0, 11, 2 and a chance of 3/4",
                 "R": 6, "S": 0, "T": 11, "P": 2, "a": "TFT", "b": "GRIM", "rounds": 10, "delta": "3/4", "expect": {"itThresh": "GRIM 5/9, TFT 5/6: δ = 3/4 sustains GRIM only"}},
            ],
            "panel_title": "Change the payoffs or the continuation probability",
            "panel_intro": "The last tile gives the two thresholds and says whether the stated delta clears them. "
                           "Raise the temptation and watch both thresholds rise; they depend on the four payoffs and nothing else.",
        }),
        "steps_title": "Finding the discount factor",
        "steps_intro": "The same five lines for any partner who punishes.",
        "steps": [
            ("Write the value of cooperating forever",
             "It is the reward every round: `R / (1 − δ)`."),
            ("Write the value of the best deviation",
             "The temptation now, then whatever the partner's reply yields in the rounds after."),
            ("Set cooperation at least as large and cancel",
             "Multiply through by `1 − δ` to clear the denominator and collect the terms in `δ`."),
            ("Solve for the smallest delta",
             "The result is a ratio of two gaps between payoffs: the gain from defecting over the gain of cooperation, "
             "against how much the reply takes away."),
            ("Compare with the delta you have",
             "If it is above the threshold the deviation does not pay. If it is below, it does."),
        ],
        "worked": {
            "title": "The thresholds with the standard payoffs",
            "intro": ["R = 3, S = 0, T = 5, P = 1, and delta = 9/10."],
            "lines": [
                "GRIM:  (T - R)/(T - P) = 2/4  = 1/2",
                "TFT:   (T - R)/(R - S) = 2/3, and 2/3 > 1/2",
                "Cooperate for good against GRIM:  3/(1/10) = 30",
                "Defect at once:  5 + (9/10)·1/(1/10) = 5 + 9 = 14",
                "9/10 clears 1/2 and 2/3: cooperation is stable",
            ],
            "after": [
                "Thirty against fourteen is not close. At `δ = 1/4` the comparison reverses: cooperating for good is worth `4` "
                "and defecting at once is worth about `5.33`, and the lab says the future does not count enough.",
            ],
        },
        "quiz_title": "Thresholds and the last round",
        "quiz": [
            {"q": "With R = 3, S = 0, T = 5 and P = 1, what is the smallest delta that sustains cooperation against GRIM?",
             "a": ["1/4", "2/3", "9/10", "1/2"],
             "c": 3,
             "why": "The threshold is (T − R) / (T − P), which is 2 over 4. Two thirds is the figure for TFT, which "
                    "forgives, and 9/10 is the delta the preset happens to use."},
            {"q": "With the same payoffs, delta is 3/5. What does the lab say?",
             "a": ["Cooperation is stable against TFT and GRIM",
                   "Cooperation is stable against neither",
                   "Cooperation is stable against GRIM only",
                   "Cooperation is stable against TFT only"],
             "c": 2,
             "why": "3/5 is above 1/2 and below 2/3, so it clears the GRIM threshold and misses the TFT threshold. "
                    "The TFT threshold is the larger of the two, so it cannot be cleared when GRIM's is missed."},
            {"q": "Two players know they will play exactly one hundred rounds of the dilemma. Why does cooperation fail even against GRIM?",
             "a": ["A hundred rounds is too short for any punishment to work",
                   "Defecting in the last round dominates, so the round before has no future either, and so on back",
                   "With a known end delta is always below the threshold",
                   "GRIM cannot be played for a fixed number of rounds"],
             "c": 1,
             "why": "The last round has no later round to protect, so both defect there whatever came earlier. That removes the "
                    "reason to cooperate in the round before, and the argument repeats. Length has nothing to do with it, and GRIM can be played for any number of rounds."},
            {"q": "Raise the temptation T and leave R, S and P alone. What happens to the thresholds?",
             "a": ["Both fall, because defecting is more attractive",
                   "Both rise: a larger gain from defecting needs a larger weight on the future",
                   "Neither changes, since they depend only on R",
                   "GRIM's rises and TFT's falls"],
             "c": 1,
             "why": "For TFT the denominator R − S does not involve T, so the ratio rises with T. For GRIM both gaps grow by the same amount, "
                    "and a smaller gap over a larger one rises when both grow equally. A bigger temptation asks for a heavier shadow."},
        ],
        "mistakes": [
            ("Thinking cooperation needs a long game when it needs an uncertain end",
             "A game of exactly one hundred rounds unravels from the last round back, while a game that continues "
             "with probability one half, two rounds on average, sustains cooperation against GRIM with the standard payoffs. "
             "What counts is whether a next round is possible at every point, not how many there will be."),
            ("Assuming a mild punishment sustains cooperation as easily as a harsh one",
             "GRIM needs a continuation probability of `1/2` and TFT needs `2/3`. A deviator against TFT who goes back to "
             "cooperating loses only one round to the reply, so the shadow of the future has to be heavier."),
            ("Reading the threshold as a prediction that players will cooperate",
             "It says cooperation is stable, that nobody gains by deviating. Both players always defecting is also stable in the repeated game, "
             "so the threshold says what is possible, not what will happen."),
        ],
        "standard": ("Finish when you can derive a threshold and use it.",
                     "Given the four payoffs, compute the continuation probability above which cooperation is stable against "
                     "GRIM and against TFT, say whether a stated delta clears each, and explain why a known final round removes the threshold."),
        "note": "The lab refuses payoffs that are not a dilemma, and refuses 2R below T + S as well, since then taking turns to "
                "exploit beats cooperating and the derivation above is not the right comparison. That is why the high-temptation "
                "preset is the standard game scaled by two, with the temptation raised to eleven.",
    },
]
