"""Justice and Collective Choice, lessons 6-10: the rest of social choice and the jury theorem.

Every figure the prose states is one the lab prints or one the lesson computes by hand
from the profile it shows; the presets pin the tiles that say why each preset exists
(scripts/mathpath/AGENTS.md, "a preset's two claims"). A redraw-only control such as the
rule or the removed candidate keeps its shipped value when a preset is chosen, so the
pinned tiles describe the shipped rule and the prose says which rule to switch to.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    {
        "slug": "plurality-runoff-and-borda",
        "title": "Plurality, Runoff and Borda",
        "module": "Collective choice",
        "one_line": "One set of ballots, four counting rules, and more than one winner.",
        "summary": (
            "Plurality counts first places. The two-round runoff counts first places and then holds a head-to-head contest, "
            "instant runoff removes one candidate at a time, and the Borda count adds points for every position on every ballot. "
            "Run on one profile they can elect different candidates, and each answers a different question about the voters. "
            "The wrong model is that the candidate with the most first choices is the people's choice."
        ),
        "key": [
            "plurality counts first places",
            "runoff: the top two meet head to head",
            "Borda: 2, 1, 0 points down each ballot",
            "same ballots, different rule, new winner",
        ],
        "key_label": "One profile, four counts",
        "concepts_intro": (
            "Every rule in this lesson takes the same input, a profile of rankings, and returns a winner. "
            "What differs is what the rule reads off the ballots."
        ),
        "concepts": [
            ("Plurality reads only the top",
             "Each ballot counts once, for its first choice. The candidate with the most first places wins, with a majority or "
             "without one, and the rest of every ballot is ignored."),
            ("Runoff rules count first places more than once",
             "The two-round runoff keeps the two candidates with the most first places and lets the voters choose between them. "
             "Instant runoff removes the candidate with the fewest first places, passes those ballots to their next choice, and "
             "repeats until someone holds a majority."),
            ("Borda reads every position",
             "With three candidates a ballot gives `2` points to its first choice, `1` to its second and `0` to its last, and the "
             "points are added over all ballots. A candidate who is rarely ranked low can win without being ranked first often."),
        ],
        "read_title": "Four counts of one profile",
        "read_intro": "A nine-voter profile in which most rules agree, one in which they split three ways, and one in which plurality "
                      "elects the candidate most voters rank last.",
        "body": [
            ("p", "The previous lesson asked whether majorities can be assembled into a ranking and found that sometimes they cannot. "
                  "Real elections need a winner anyway, and the rules in use answer in different ways. The way to compare them is to "
                  "hold the ballots fixed and change only the rule."),
            ("p", "Take nine voters and three candidates. Four voters rank them `A B C`, three rank them `B C A`, and two rank them "
                  "`C B A`."),
            ("math", [
                "     voters   first   second   third",
                "     4        A       B        C",
                "     3        B       C        A",
                "     2        C       B        A",
            ]),
            ("p", "<strong>Plurality</strong> reads the first column. `A` has `4` first places, `B` has `3` and `C` has `2`, so `A` wins "
                  "with fewer than half the voters. The <strong>two-round runoff</strong> keeps `A` and `B`, the two with the most "
                  "first places, and asks the voters to choose between them using their whole ballots: `4` rank `A` above `B` and "
                  "`5` rank `B` above `A`, so `B` wins. <strong>Instant runoff</strong> reaches the same place by another road. "
                  "`C` has the fewest first places and is removed, its two ballots pass to their next choice, which is `B`, and `B` "
                  "holds `5` of the `9` ballots."),
            ("p", "The <strong>Borda count</strong> does not eliminate anyone. Each ballot gives `2`, `1` and `0` points down the "
                  "ranking, and the voters' points are summed. The sums below are the arithmetic the lab leaves to you; it prints the "
                  "winner."),
            ("math", [
                "              A     B     C",
                "     4 voters   8     4     0",
                "     3 voters   0     6     3",
                "     2 voters   0     2     4",
                "     total      8     12    7",
            ]),
            ("p", "`B` wins the Borda count with `12` points against `8` and `7`. `B` is also the Condorcet winner: it beats `A` "
                  "by `5` to `4` and `C` by `7` to `2`. So three of the four counts elect `B`, and plurality is the one that elects "
                  "`A`, a candidate who loses the head-to-head contest with `B`."),
            ("h3", "Three rules, three winners"),
            ("p", "Change one ballot group. Let four voters rank the candidates `A C B`, three `B C A` and two `C B A`. Plurality "
                  "still elects `A`, with `4` first places against `3` and `2`. The runoff and instant runoff elect `B`: `A` "
                  "meets `B` and loses `4` to `5`, and `C` is removed first. The Borda count elects `C`, with `11` points against "
                  "`8` and `8`. `C` is also the Condorcet winner, beating `A` by `5` to `4` and `B` by `6` to `3`."),
            ("p", "Three different counts, three different winners, from nine ballots. `C` is never ranked last by anyone, "
                  "and it is eliminated in the first round of both runoff rules because only two voters put it first. Nothing in "
                  "the ballots has changed between the rules; what changed is which part of the ballots each rule looks at."),
            ("h3", "What each rule is counting"),
            ("ul", [
                "Plurality counts <strong>enthusiasm</strong>: how many voters would be delighted. It cannot see how the others feel.",
                "The runoffs count <strong>strength against the strongest rival</strong>, but only after first places have chosen "
                "who the rivals are.",
                "Borda counts <strong>average standing</strong>: who is placed high by most voters, whether or not first.",
                "The Condorcet rule counts <strong>victories</strong>: who beats every other candidate by majority, when anyone does.",
            ]),
            ("p", "The lab runs these on the profile you type, with the winner under the chosen rule, the Condorcet result "
                  "and the table of pairwise counts. It reports a tie as a tie. It scores Borda as `2`, `1`, `0` for three "
                  "candidates and with the matching run of points for more, and it takes every ballot as the voter's real ranking; "
                  "whether voters would rank the same way under a different rule is the question of “Strategic Voting and Manipulation”."),
        ],
        "lab": ("choicekit", {
            "mode": "vote", "rule": "plurality",
            "preset": "most-firsts",
            "presets": [
                {"id": "most-firsts", "label": "Nine voters, A has the most first places",
                 "kind": "ranking",
                 "profile": [{"count": 4, "rank": "A B C"}, {"count": 3, "rank": "B C A"}, {"count": 2, "rank": "C B A"}],
                 "expect": {"voWinner": "A", "voCondorcet": "B"}},
                {"id": "three-winners", "label": "Nine voters, C ranked last by nobody",
                 "kind": "ranking",
                 "profile": [{"count": 4, "rank": "A C B"}, {"count": 3, "rank": "B C A"}, {"count": 2, "rank": "C B A"}],
                 "expect": {"voWinner": "A", "voCondorcet": "C"}},
                {"id": "spoiler", "label": "Nine voters, two similar candidates and one rival",
                 "kind": "ranking",
                 "profile": [{"count": 3, "rank": "A B C"}, {"count": 2, "rank": "B A C"}, {"count": 4, "rank": "C A B"}],
                 "expect": {"voWinner": "C", "voCondorcet": "A"}},
            ],
            "panel_title": "Run a rule on the profile",
            "panel_intro": "A profile reads count: best to worst, groups separated by semicolons. Choose the rule below the profile; "
                           "in the table each cell counts the voters who prefer the row candidate to the column candidate.",
        }),
        "steps_title": "Running four rules on one profile",
        "steps_intro": "Five moves, in this order, for any profile of three candidates. Keep the profile table in front of you throughout.",
        "steps": [
            ("Write the profile as a table of rankings with counts",
             "One row per ranking, best to worst, with the number of voters who hold it. Check that the counts add up to the electorate."),
            ("Plurality: count the first column",
             "Add the counts of the rows that begin with each candidate. The largest total wins, however small a share of the voters it is."),
            ("Runoff: take the top two, then count whole ballots",
             "The two candidates with the most first places meet. For each row, see which of the two it ranks higher, and add the counts. "
             "Instant runoff instead removes the candidate with the fewest first places and moves those rows to their next choice."),
            ("Borda: give each row `2`, `1`, `0` and sum",
             "Multiply a row's points by its count for each candidate, then add down the column. The largest total wins."),
            ("Compare with the Condorcet winner",
             "Count each pair of candidates. If one candidate beats both others it is the Condorcet winner, and each rule can now be "
             "described by whether it elected that candidate."),
        ],
        "worked": {
            "title": "Nine ballots, four counts",
            "intro": ["Four voters rank A B C, three rank B C A, two rank C B A."],
            "lines": [
                "plurality   A 4, B 3, C 2               -> A",
                "runoff      A against B: 4 to 5         -> B",
                "instant     drop C, its 2 go to B: 5-4  -> B",
                "Borda       A 8, B 12, C 7              -> B",
                "Condorcet   B beats A 5-4, C 7-2        -> B",
            ],
            "after": [
                "Plurality elects a candidate who loses a head-to-head contest with the Condorcet winner. The first column of a ballot is a "
                "small part of what the voter thinks, and a rule that reads only that part can disagree with every rule that reads more.",
            ],
        },
        "quiz_title": "Counting under four rules",
        "quiz": [
            {"q": "In the profile with four voters at A B C, three at B C A and two at C B A, what is B's Borda total, with 2, 1 and 0 points for first, second and third?",
             "a": ["9",
                   "8",
                   "12",
                   "7"],
             "c": 2,
             "why": "B earns 1 point from each of the 4 voters who rank it second, 2 points from each of the 3 who rank it first, "
                    "and 1 point from each of the 2 who rank it second: 4 + 6 + 2 = 12. The total 8 is A's and 7 is C's. "
                    "The figure 9 is the number of voters, which is not a score."},
            {"q": "In that same profile, instant runoff removes C first. Where do C's two ballots go?",
             "a": ["To B, the next choice on both",
                   "To A, because A has the most first places",
                   "They are discarded",
                   "One to A and one to B"],
             "c": 0,
             "why": "Both of those ballots read C B A, so the next live candidate on each is B, and B rises to 5 against A's 4. "
                    "The ballots follow the voters' own order, not the leader, and neither is split or thrown away."},
            {"q": "Four voters rank A C B, three B C A and two C B A. Which statement is true?",
             "a": ["Every rule elects A, who has the most first places",
                   "The runoff elects C, the Condorcet winner",
                   "Plurality and Borda agree, since both count first places",
                   "Plurality elects A, the runoff elects B and Borda elects C"],
             "c": 3,
             "why": "A has 4 first places, so plurality elects A. The runoff meets A and B, and B wins 5 to 4. Borda gives C 11 points against "
                    "8 and 8. The runoff does not elect C, because C has too few first places to reach it, and Borda counts "
                    "positions, not first places."},
            {"q": "Three voters rank A B C, two B A C and four C A B, and plurality elects C. What makes that a poor result?",
             "a": ["C is the Condorcet winner",
                   "Five of the nine voters rank C last, and A beats C by 5 to 4",
                   "A has more first places than C",
                   "C has more than half of the first places"],
             "c": 1,
             "why": "C has 4 first places, fewer than half, because the A and B voters split the other 5. Those five voters rank C last, "
                    "and each of them prefers A to C, which is why A beats C 5 to 4, so A, not C, is the Condorcet winner. "
                    "A has 3 first places, fewer than C's 4."},
        ],
        "mistakes": [
            ("Treating the most first choices as the people's choice",
             "With three voters at A B C, two at B A C and four at C A B, C has the most first places, 4 against 3 and "
             "2, and five of the nine voters rank C last. A beats C by 5 to 4 and B by 7 to 2. The first-place count measures how many "
             "voters are enthusiastic, and it says nothing about how the rest rank the winner, so a lead of 4 in 9 can be a "
             "majority's last choice."),
            ("Speaking of the winner without naming the rule",
             "With four voters at A C B, three at B C A and two at C B A, plurality elects A, the runoff elects B and Borda elects C. "
             "&ldquo;The winner&rdquo; is a statement about a profile and a rule together, and the same nine ballots give three "
             "answers to it."),
            ("Expecting a runoff to rescue the Condorcet winner",
             "In that same profile C is the Condorcet winner, beating A by 5 to 4 and B by 6 to 3, and both runoff rules eliminate it "
             "in the first round because only two voters put it first. A runoff lets first places decide who may reach the contest, "
             "so a candidate everyone finds acceptable but few adore never gets to it."),
        ],
        "standard": ("Finish when you can run plurality, runoff, instant runoff and Borda on a three-candidate profile and say what each counts.",
                     "Given a profile with counts, compute each rule's winner by hand, find the Condorcet winner, and name a profile on "
                     "which three of the rules elect three different candidates."),
        "note": "Change the rule below the profile and watch the winner move while the table of pairwise counts stays put: the counts "
                "belong to the ballots and the winner belongs to the rule. Then take the spoiler profile and move one voter from C A B "
                "to B A C, and the plurality count becomes a three-way tie.",
    },
    # ---------------------------------------------------------------- 07
    {
        "slug": "independence-and-arrows-theorem",
        "title": "Independence and Arrow's Theorem",
        "module": "Collective choice",
        "one_line": "Strike a losing candidate from every ballot and the winner can change, though no voter's view of the others did.",
        "summary": (
            "Arrow asked what a rule that turns voters' rankings into a group ranking should satisfy, and proposed three conditions: "
            "unanimity, independence of irrelevant alternatives and non-dictatorship. On a profile the independence condition can be "
            "tested by removing a losing candidate and recounting. The theorem says that with three or more candidates no such rule "
            "meets all three on every profile. The wrong model is that Arrow proved democracy impossible."
        ),
        "key": [
            "unanimity: all prefer A, so the group does",
            "IIA: A against B depends on A against B",
            "non-dictatorship: no voter always wins",
            "strike a loser and the winner can change",
            "3+ candidates: no ranking rule has all",
        ],
        "key_label": "Arrow's conditions",
        "concepts_intro": (
            "Arrow's theorem is about a kind of rule and three conditions on it. The conditions are easier to see on a profile than to "
            "state in the abstract, and one of them can be tested directly."
        ),
        "concepts": [
            ("Unanimity and non-dictatorship",
             "Unanimity says that if every voter ranks `A` above `B`, so does the group. Non-dictatorship says there is no voter "
             "whose ranking becomes the group's ranking whatever the others think. Both are modest conditions."),
            ("Independence of irrelevant alternatives",
             "The group's ranking of `A` against `B` should depend only on how each voter ranks `A` against `B`. A third candidate "
             "who is ranked above or below them by various voters is irrelevant to that comparison, and should not change it."),
            ("The test is a removal",
             "Strike a losing candidate from every ballot, keeping the order of the others, and recount under the same rule. "
             "No voter has changed their view of the candidates who remain, so if the winner changes, independence has failed on that profile."),
        ],
        "read_title": "Striking a loser",
        "read_intro": "Two profiles on which the winner changes when someone who lost is removed, and what the theorem says about rules that cannot avoid it.",
        "body": [
            ("p", "The Condorcet paradox is a failure of a particular rule, majority rule, to produce a ranking. Arrow's question was larger: "
                  "is there any rule that turns every profile of rankings into a group ranking and behaves sensibly? He made "
                  "&ldquo;sensibly&rdquo; precise with three conditions, and the second is the one that fails in practice."),
            ("ul", [
                "<strong>Unanimity.</strong> If every voter ranks `A` above `B`, the group ranks `A` above `B`.",
                "<strong>Independence of irrelevant alternatives</strong> (IIA). The group's ranking of `A` and `B` depends only on how "
                "each voter ranks `A` and `B`.",
                "<strong>Non-dictatorship.</strong> No one voter is such that the group ranking always equals theirs.",
            ]),
            ("p", "Return to the nine voters of the last lesson: four rank the candidates `A B C`, three rank them `B C A`, and two "
                  "rank them `C B A`. Under plurality `A` wins with `4` first places, against `3` for `B` and `2` for `C`. "
                  "Now strike `C` from every ballot. The four `A B C` voters become `A B`, the three `B C A` voters become `B A`, and the two "
                  "`C B A` voters become `B A`. Plurality now counts `4` for `A` and `5` for `B`, and `B` wins."),
            ("p", "No voter has changed a view about `A` and `B`. Before the removal, `4` voters ranked `A` above `B` and `5` ranked "
                  "`B` above `A`; after it, the same `4` and the same `5`. Yet the group's ranking of the pair has reversed, "
                  "because the voters who ranked `C` first have had their first places handed to `B`. The presence of `C` "
                  "decided the contest between `A` and `B`, and `C` was never going to win."),
            ("p", "The lab finds this when the removal menu is set to nobody: it tries each losing candidate in turn and names the first "
                  "whose removal changes the winner. Here that is `B`, since without `B` the contest is between `A` with `4` and `C` with `5`, and `C` "
                  "wins. Set the menu to `C` and the winner becomes `B`, as above."),
            ("def", ("Independence of irrelevant alternatives",
                     "A rule satisfies <strong>independence of irrelevant alternatives</strong> when the group's ranking of two "
                     "candidates depends only on the voters' rankings of those two. The lab's test is a close and visible cousin: "
                     "it asks whether the winner changes when a losing candidate is struck from every ballot.")),
            ("h3", "A rule that counts more fails too"),
            ("p", "It is tempting to blame plurality for reading only first places. Take nine voters: two rank them `A C B`, two `B A C`, "
                  "two `B C A` and three `C B A`. Plurality elects `B`, with `4` first places. Borda also elects `B`, with `11` "
                  "points against `10` for `C` and `6` for `A`. But `C` beats `B` by `5` to `4`, `C` beats `A` by `5` to `4`, and `C` "
                  "is the Condorcet winner."),
            ("p", "Strike `A`, who loses under every rule. With two candidates left, both plurality and Borda reduce to majority "
                  "rule between `B` and `C`, and `C` wins `5` to `4`. Both rules fail the removal test on this profile, and "
                  "the lab says so under either rule."),
            ("h3", "The theorem"),
            ("thm", ("Arrow's theorem",
                     "Suppose there are at least three candidates, and a rule turns every profile of complete, transitive rankings "
                     "into a complete, transitive group ranking. If the rule satisfies unanimity and independence of irrelevant "
                     "alternatives, it is a dictatorship: some one voter's ranking is the group ranking on every profile.")),
            ("p", "The proof is not reproduced here. The conditions, on the other hand, can all be read on a profile, and the "
                  "theorem says that no choice of rule stops the removal test from failing somewhere. It is a statement "
                  "about a specific kind of rule, and three things it does not say are worth stating."),
            ("ul", [
                "It does not say elections cannot be held. It says no single rule of this kind has all three properties on all "
                "profiles.",
                "It does not apply to two candidates. Majority rule between two satisfies all three conditions.",
                "It does not say every rule fails the same way. Borda gives up independence, majority rule gives up always "
                "producing a ranking, and restricting the profiles, for example to voters who place the candidates on one "
                "left-to-right line, lets majority rule work.",
            ]),
            ("p", "The lab's rules all respect unanimity, and the only dictatorship it can show is the degenerate one of a single voter. "
                  "Its removal test is about the winner, while Arrow's condition is about the ranking of a pair, so a pass on "
                  "one profile is a pass on that profile and nothing more."),
        ],
        "lab": ("choicekit", {
            "mode": "vote", "rule": "plurality", "remove": "nobody",
            "preset": "iia-plurality",
            "presets": [
                {"id": "iia-plurality", "label": "Nine voters, A leads on first places",
                 "kind": "ranking",
                 "profile": [{"count": 4, "rank": "A B C"}, {"count": 3, "rank": "B C A"}, {"count": 2, "rank": "C B A"}],
                 "expect": {"voWinner": "A", "voIIA": "violated (remove B)"}},
                {"id": "iia-borda", "label": "Nine voters, a Condorcet winner behind",
                 "kind": "ranking",
                 "profile": [{"count": 2, "rank": "A C B"}, {"count": 2, "rank": "B A C"}, {"count": 2, "rank": "B C A"},
                             {"count": 3, "rank": "C B A"}],
                 "expect": {"voWinner": "B", "voIIA": "violated (remove A)"}},
                {"id": "dictator", "label": "One voter alone",
                 "kind": "ranking",
                 "profile": [{"count": 1, "rank": "B C A"}],
                 "expect": {"voWinner": "B", "voIIA": "holds"}},
            ],
            "panel_title": "Test independence by removal",
            "panel_intro": "The independence tile compares the winner with everyone standing to the winner after each losing candidate "
                           "is struck out. Choose a candidate under Remove a candidate to see the profile without them.",
        }),
        "steps_title": "Testing independence on a profile",
        "steps_intro": "Five moves. The first four are the removal test and the last relates it to the theorem.",
        "steps": [
            ("Find the winner with everyone standing",
             "Use the rule you are testing and write the winner down. A candidate who wins cannot be the one removed."),
            ("Pick a loser and strike it from every ballot",
             "Delete it from each ranking and close the gap. Everyone else keeps their relative order, so every voter's view of every remaining "
             "pair is unchanged."),
            ("Recount under the same rule",
             "The counts, and for Borda the points, are recomputed from the shortened ballots."),
            ("Compare the winners",
             "If the new winner differs, independence fails on this profile, and no voter changed their mind about the pair that now "
             "ranks differently. If every loser's removal leaves the winner alone, the test passes on this profile only."),
            ("Ask which condition the rule gave up",
             "A rule that fails the test is one of the rules the theorem says must give something up. It does not contradict the theorem, "
             "and it does not show that a better rule is missing from the profile."),
        ],
        "worked": {
            "title": "Striking C from nine ballots",
            "intro": ["Four voters rank A B C, three B C A, two C B A, under plurality."],
            "lines": [
                "with C:     A 4, B 3, C 2       -> A wins",
                "strike C:   A B 4, B A 3 and 2  -> A 4, B 5",
                "without C:  B wins",
                "A over B:   4 voters, before and after",
                "B over A:   5 voters, before and after",
            ],
            "after": [
                "The group's ranking of A and B reversed, and the voters' rankings of A and B did not move. The failure is a property "
                "of the rule applied to the whole ballot, which is what independence forbids.",
            ],
        },
        "quiz_title": "Conditions and removals",
        "quiz": [
            {"q": "Four voters rank A B C, three B C A and two C B A. Strike C from every ballot and run plurality. Who wins?",
             "a": ["A, with 4 against 3",
                   "B, with 5 against 4",
                   "C, with 2 first places",
                   "A and B tie"],
             "c": 1,
             "why": "The two C B A ballots become B A, so B has 3 + 2 = 5 first places and A keeps 4. C is no longer on the ballot, "
                    "and neither a win for A nor a tie follows from the counts."},
            {"q": "Which condition says that the group's ranking of A and B depends only on how each voter ranks A and B?",
             "a": ["Unanimity",
                   "Non-dictatorship",
                   "Independence of irrelevant alternatives",
                   "Transitivity of the group ranking"],
             "c": 2,
             "why": "That is the statement of independence. Unanimity concerns the case where every voter agrees, non-dictatorship "
                    "concerns whether one voter always prevails, and transitivity is a property the group ranking must have, not "
                    "a condition on what it depends on."},
            {"q": "Which of these does Arrow's theorem say?",
             "a": ["With three or more candidates, no rule that ranks every profile satisfies unanimity, independence and non-dictatorship",
                   "No election can be fair",
                   "Majority rule between two candidates violates independence",
                   "Plurality is the only rule that satisfies unanimity"],
             "c": 0,
             "why": "The first statement is the theorem. It does not condemn all elections, and with two candidates majority rule meets all "
                    "three conditions. Plurality is not the only rule that respects unanimity, since Borda does too."},
            {"q": "Nine voters rank the candidates two A C B, two B A C, two B C A and three C B A, and plurality elects B. Strike A, who loses. What follows?",
             "a": ["B still wins, so independence holds",
                   "A wins, which shows a voter changed their mind",
                   "The election is a tie, 4 to 4",
                   "C wins, 5 to 4, though no voter's ranking of B and C changed"],
             "c": 3,
             "why": "Without A, the two A C B ballots become C B and the two B A C ballots become B C, so C has 2 + 3 = 5 first places "
                    "against B's 4. Each voter ranks B and C as before. A tie would need equal counts and there are none, and "
                    "A is no longer on the ballot."},
        ],
        "mistakes": [
            ("Believing that Arrow proved democracy impossible",
             "The theorem is about rules that turn every profile of rankings into a full group ranking and satisfy three stated "
             "conditions. With two candidates, majority rule satisfies all three. With more, each real rule gives up something "
             "visible: plurality and Borda give up independence, as the removal of one loser above shows, and majority rule gives "
             "up always producing a ranking, as the cycle did. What the theorem forbids is getting everything at once."),
            ("Reading an independence failure as a voter changing their mind",
             "When C is struck from the nine-voter profile, the same 4 voters still rank A above B and the same 5 still rank B above "
             "A. The group's verdict reversed because the rule gave the voters who ranked C first to B, and no one's view of "
             "A or B moved. The failure belongs to the rule."),
            ("Hearing “dictator” as a tyrant",
             "Non-dictatorship rules out a voter whose ranking is the group's on every profile. The dictator need not be powerful or "
             "malicious: a rule that copies the first voter's ballot and ignores the rest is a dictatorship by the definition. "
             "With one voter alone, as in the last preset, every rule here is one."),
        ],
        "standard": ("Finish when you can test independence by removing a loser and state what Arrow's theorem says and does not say.",
                     "Given a profile and a rule, strike a losing candidate, recount, and report whether the winner changed; then state the "
                     "three conditions and the theorem, and name two things the theorem does not claim."),
        "note": "Set the rule to Borda on the first preset and strike each candidate in turn: the Borda winner is B, and the removal test "
                "passes on that profile. Independence fails on a profile, not for a rule in general, and the lab can show you only the "
                "profiles you type.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "strategic-voting-and-manipulation",
        "title": "Strategic Voting and Manipulation",
        "module": "Collective choice",
        "one_line": "A voter can sometimes do better by reporting a ranking they do not hold.",
        "summary": (
            "A rule is manipulable at a profile when some voters can get a result they prefer by reporting a ranking other than their "
            "own. Under the Borda count, voters who rank a rival second can bury it at the bottom, and under plurality voters whose "
            "favourite cannot win can vote for their second choice. The Gibbard&ndash;Satterthwaite theorem says that with three or "
            "more candidates every non-dictatorial rule that can elect any candidate is manipulable somewhere. "
            "The wrong model is that strategic voting is lying about facts."
        ),
        "key": [
            "manipulation: a false ranking that pays",
            "bury a rival and its Borda total falls",
            "two candidates: no misreport can pay",
            "3+ candidates: some profile can be gamed",
        ],
        "key_label": "When a lie pays",
        "concepts_intro": (
            "Every rule so far has been run on the voters' real rankings. This lesson asks what happens when the voters know the rule "
            "and know one another's rankings."
        ),
        "concepts": [
            ("A misreport is a ranking, not a fact",
             "Voters are asked for a ranking of the candidates, which only they hold. A misreport is a submitted ranking that "
             "differs from that private one. No fact about the world is stated falsely, and nobody else can check it."),
            ("A gain is measured by the voters' true ranking",
             "A group of voters gains from a misreport when the winner it produces is ranked above the sincere winner by those "
             "voters' true rankings. The question is always asked of the true ranking, never of the submitted one."),
            ("The lab searches blocs",
             "The lab takes each group of voters who share a ranking, lets them change together to every other ranking, and reports the "
             "first change that elects someone they rank above the sincere winner. It searches blocs, and a lone voter is a "
             "smaller case."),
        ],
        "read_title": "Burying a rival",
        "read_intro": "A profile where the Borda count can be gamed, a profile where plurality can, and the one setting in which "
                      "no misreport helps.",
        "body": [
            ("p", "A voting rule is a procedure, and a procedure invites the question of whether it can be used against its own "
                  "purpose. If the rule is run on the ballots the voters hand in, a voter who knows the rule and the likely "
                  "ballots of the others can choose a ballot to get the best result, and the best ballot is not always the true one."),
            ("p", "Take seven voters: two rank the candidates `A B C`, two rank them `B C A`, and three rank them `C B A`. Under the "
                  "Borda count, with `2`, `1` and `0` points, `A` gets `4`, `B` gets `9` and `C` gets `8`, so `B` wins. "
                  "The three voters who rank `C` first prefer `C` to `B`, and `C` is `1` point short."),
            ("p", "Suppose they report `C A B`, not `C B A`. They still give `C` its `2` points, but they now give `B` nothing and give "
                  "`A` a point. If two of the three do this, `B` falls to `7`, `A` rises to `6` and `C` keeps `8`, so `C` wins; "
                  "if all three do it, which is the switch the lab tries, the totals are `7`, `6` and `8` and the winner is the "
                  "same. Nothing about `C`'s support increased; `B`'s total was lowered by ranking it where it did not belong. "
                  "This is <strong>burying</strong>, and the lab reports it as voters ranking `C B A` who gain by `C A B`."),
            ("def", ("Manipulation",
                     "A rule is <strong>manipulable</strong> at a profile when some group of voters can get an outcome they "
                     "prefer, by their true rankings, by reporting rankings other than their true ones.")),
            ("p", "Burying works because the Borda count takes every position into account, and a voter controls where the "
                  "rival is placed on their own ballot. Plurality offers a different route. Take seven voters: two rank the candidates "
                  "`A C B`, three `B C A` and two `C B A`. Plurality elects `B` with `3` first "
                  "places. The two voters who rank `A` first prefer `C` to `B`. Their favourite cannot win, but by "
                  "reporting `C A B` they give `C` four first places and elect it, which they prefer to `B`."),
            ("p", "That is the spoiler voter's dilemma: voting for your favourite and getting your worst, or voting for your second "
                  "choice. The lab shows it when you set the rule to plurality on that profile. Under the Borda count the same profile "
                  "elects `C` without any misreport, and the lab finds a different bloc that gains."),
            ("h3", "The one safe setting"),
            ("p", "With two candidates there is nothing to bury and no one to switch to. A voter who ranks `A` above `B` can report "
                  "that, or the reverse, and the reverse can only help `B`. With three voters at `A B` and two at `B A`, the "
                  "lab finds no group that gains by misreporting, under any rule."),
            ("h3", "The theorem"),
            ("thm", ("The Gibbard–Satterthwaite theorem",
                     "Suppose there are at least three candidates, and a rule picks one winner from every profile of rankings. "
                     "If every candidate can win under some profile, and no one voter is a dictator, then there is some "
                     "profile at which some voter gains by reporting a ranking other than their own.")),
            ("p", "The theorem is the companion of Arrow's, and its proof is not reproduced here. "
                  "It says that manipulability is not a defect of plurality or Borda in particular. What it leaves "
                  "open is how often a profile is manipulable, how much information the manipulators need, and how costly "
                  "the manipulation is to find. The lab assumes the manipulators know every ballot, which is the "
                  "assumption most favourable to the manipulators."),
            ("p", "A note about reading the tile. &ldquo;None found&rdquo; means that no bloc of identical voters, switching "
                  "together to any other ranking, elects a candidate they rank above the sincere winner on this one profile. "
                  "It does not say the rule is safe."),
        ],
        "lab": ("choicekit", {
            "mode": "vote", "rule": "borda",
            "preset": "borda-manip",
            "presets": [
                {"id": "borda-manip", "label": "Seven voters, three rank C first",
                 "kind": "ranking",
                 "profile": [{"count": 2, "rank": "A B C"}, {"count": 2, "rank": "B C A"}, {"count": 3, "rank": "C B A"}],
                 "expect": {"voWinner": "B", "voManip": "voters ranking C B A gain by C A B"}},
                {"id": "plurality-manip", "label": "Seven voters, two rank A first",
                 "kind": "ranking",
                 "profile": [{"count": 2, "rank": "A C B"}, {"count": 3, "rank": "B C A"}, {"count": 2, "rank": "C B A"}],
                 "expect": {"voWinner": "C", "voManip": "voters ranking B C A gain by B A C"}},
                {"id": "safe", "label": "Five voters, two candidates",
                 "kind": "ranking",
                 "profile": [{"count": 3, "rank": "A B"}, {"count": 2, "rank": "B A"}],
                 "expect": {"voWinner": "A", "voManip": "none found"}},
            ],
            "panel_title": "Search for a profitable misreport",
            "panel_intro": "The manipulation tile names the first group of voters, by their true ranking, who gain by reporting another, "
                           "and the ranking they report. Change the rule to see the same ballots under plurality.",
        }),
        "steps_title": "Finding a profitable misreport",
        "steps_intro": "Five moves for a small profile. The method is a search, and the lab does the same search over every ranking.",
        "steps": [
            ("Find the sincere winner under the rule",
             "Count the true ballots. This is the outcome that any manipulating group has to beat."),
            ("Pick a group of voters who share a ranking",
             "Choose those who rank the sincere winner below another candidate. A group that already has its favourite elected has nothing to gain."),
            ("Choose a ranking for them to report instead",
             "Try the obvious ones: under Borda, push the sincere winner to the bottom; under plurality, put a second choice first."),
            ("Recount with the changed ballots",
             "Leave every other group's ballot as it was. If the new winner is one the group ranks above the sincere winner by "
             "their true ranking, they have gained."),
            ("Check the gain against the true ranking",
             "Compare the new winner with the sincere one in the group's true order, not the reported one. A misreport "
             "that changes the winner to someone the group likes less is not a manipulation."),
        ],
        "worked": {
            "title": "Burying B under Borda",
            "intro": ["Two voters rank A B C, two B C A, three C B A. Borda gives 2, 1 and 0."],
            "lines": [
                "sincere:   A 4, B 9, C 8              -> B wins",
                "C B A voters prefer C to B",
                "two report C A B: B 7, A 6, C 8       -> C wins",
                "their true ranking puts C above B",
                "so voters ranking C B A gain by C A B",
            ],
            "after": [
                "No one stated a false fact. The voters submitted a ranking they did not hold, and the rule treated it as sincere. "
                "One of the three alone cannot do it, because B would still tie C at 8; two of the three suffice.",
            ],
        },
        "quiz_title": "Misreports and results",
        "quiz": [
            {"q": "Two voters rank A B C, two B C A and three C B A. Under the Borda count with 2, 1 and 0 points, who wins on the sincere ballots?",
             "a": ["A",
                   "C",
                   "B and C tie",
                   "B"],
             "c": 3,
             "why": "A gets 4 points, B gets 9 and C gets 8. C has the most first places, 3, but a Borda count adds every position, "
                    "and B's second places from the C B A voters carry it ahead. There is no tie, since 9 and 8 differ."},
            {"q": "In that profile, why do the voters who rank C B A gain by reporting C A B?",
             "a": ["It raises C's Borda total",
                   "It lowers B's total and leaves C's alone, so C overtakes B",
                   "It makes their real ranking C A B",
                   "It makes A the winner, whom they prefer"],
             "c": 1,
             "why": "C is first on both rankings, so C's points from those voters do not change. B drops from 1 point to 0, which lowers B's "
                    "total, and C overtakes it. Their real ranking is unchanged by what they submit, and A does not win."},
            {"q": "Which statement is the Gibbard–Satterthwaite theorem?",
             "a": ["With two candidates every rule can be manipulated",
                   "Every voter gains by misreporting under every rule",
                   "With three or more candidates, a non-dictatorial rule that can elect each candidate is manipulable at some profile",
                   "Strategic voting makes elections impossible"],
             "c": 2,
             "why": "The third is the theorem. With two candidates majority rule cannot be gamed, so the first statement is false. "
                    "The theorem promises a profile where someone can gain, not that everyone always does, and says nothing about "
                    "elections being impossible."},
            {"q": "Three voters rank A B and two rank B A. The lab reports no manipulation. Why?",
             "a": ["With two candidates a misreport can only help the candidate the voter ranks lower",
                   "The lab only searches profiles with three candidates",
                   "The vote is tied",
                   "Voters cannot misreport with two candidates"],
             "c": 0,
             "why": "A voter who ranks A above B can only change the ranking to B above A, which helps B, whom they rank lower. "
                    "The vote is 3 to 2, not a tie, voters can misreport in a two-candidate profile, and the lab "
                    "searches it like any other."},
        ],
        "mistakes": [
            ("Treating strategic voting as lying about facts",
             "A voter who reports C A B when they hold C B A states no false fact about the world. They hand in a ranking, which is the "
             "voter's own and unobservable, and the rule counts it as given. The question is whether the rule rewards the "
             "misreport, as the Borda count does for the three voters in the seven-voter profile, and that is a property of the "
             "rule and the profile."),
            ("Assuming that voting sincerely is always safe",
             "Under plurality in the second preset, the two voters who rank A first and vote sincerely elect B, whom they rank last. "
             "If they report C A B instead, C wins, whom they prefer. Sincerity is the best report only for a rule that cannot be gamed "
             "at that profile, and the theorem says that with three or more candidates no reasonable rule is safe at every profile."),
            ("Taking “none found” as proof that a rule resists manipulation",
             "The tile covers one profile and only blocs of identical voters moving together. A rule can show none found at one profile "
             "and be gamed at the next. Only the two-candidate case, in which the only other report helps the rival, "
             "is safe at every profile."),
        ],
        "standard": ("Finish when you can find a group of voters who gain by misreporting and state the Gibbard–Satterthwaite theorem.",
                     "Given a profile and a rule, name a group whose true ranking puts another candidate above the sincere winner, "
                     "give the ranking they report to elect that candidate, and state what the theorem guarantees."),
        "note": "Move one voter from C B A to B C A in the first preset. The Borda winner is still B, and the manipulation tile now reads "
                "none found: the two voters left who rank C first cannot lower B's total enough to lift C past it. "
                "Whether a rule can be gamed depends on the profile, and the lab can report only on the one in front of it.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "the-discursive-dilemma",
        "title": "The Discursive Dilemma",
        "module": "Collective choice",
        "one_line": "A court can accept each premise by majority and reject, by majority, the conclusion they imply.",
        "summary": (
            "Three judges rule on two premises and on a conclusion that is true exactly when both premises are. Each judge is consistent, "
            "and the majority accepts each premise, yet the majority rejects the conclusion. A premise-based procedure and a "
            "conclusion-based procedure then give opposite verdicts. The wrong model is that if a majority accepts each premise "
            "it accepts the conclusion."
        ),
        "key": [
            "a majority can accept p and accept q",
            "and still reject p ∧ q",
            "each judge is consistent, the court is not",
            "premise-based or conclusion-based verdict",
        ],
        "key_label": "A court that contradicts itself",
        "concepts_intro": (
            "The Condorcet paradox combined consistent rankings into a cycle. The same thing happens to judgments, and the "
            "way out of it forces a choice about what the group's reasons are."
        ),
        "concepts": [
            ("Judgments are linked by logic",
             "A judge decides whether `p` is true, whether `q` is true, and whether the conclusion `p ∧ q` is, and a consistent "
             "judge accepts the conclusion exactly when they accept both premises. The three questions are one agenda."),
            ("Two procedures, one set of judgments",
             "The <strong>premise-based</strong> procedure takes the majority on each premise and derives the conclusion from them. "
             "The <strong>conclusion-based</strong> procedure takes the majority on the conclusion and ignores the premises."),
            ("A consistent court is the exception",
             "The majority's accepted set can be inconsistent even though every member of the court is consistent. "
             "The lab's court shows such a case, and the other presets show a court whose procedures agree and "
             "one whose procedures differ the other way."),
        ],
        "read_title": "Three judges, three questions",
        "read_intro": "A court whose majorities contradict one another, a court that agrees with itself, and a disjunction where the "
                      "premise-based verdict is the one that fails.",
        "body": [
            ("p", "A group is often asked for more than a choice. A court gives a verdict and reasons for it; a committee decides a "
                  "proposal and the facts on which it rests. When the reasons are decided by vote, the question is whether the group's "
                  "reasons and its verdict agree."),
            ("p", "A court of three judges decides whether a defendant is liable. Liability requires two things: `p`, that there "
                  "was a valid contract, and `q`, that the defendant breached it. The conclusion is `p ∧ q`, that both hold. "
                  "Each judge is consistent: they accept the conclusion exactly when they accept both premises."),
            ("math", [
                "              p     q     p ∧ q",
                "     judge 1  yes   yes   yes",
                "     judge 2  yes   no    no",
                "     judge 3  no    yes   no",
            ]),
            ("p", "Count each column. The premise `p` is accepted by judges one and two, so it carries `2` to `1`. The premise `q` is "
                  "accepted by judges one and three, so it carries `2` to `1`. The conclusion `p ∧ q` is accepted only by judge one, "
                  "so it fails `1` to `2`. The court's majority judgments are that `p` is true, that `q` is true, and that "
                  "`p ∧ q` is false, and those three cannot all be true together."),
            ("def", ("The discursive dilemma",
                     "The <strong>discursive dilemma</strong> is the situation in which a group's majority judgments on a set of "
                     "logically connected propositions are inconsistent, though every member's judgments are consistent.")),
            ("h3", "Two procedures, two verdicts"),
            ("p", "The court has to say something about liability. The <strong>premise-based</strong> procedure accepts "
                  "what the majority accepts on `p` and on `q`, and derives that the defendant is liable. The "
                  "<strong>conclusion-based</strong> procedure counts the votes on liability itself and finds that "
                  "the defendant is not. The lab prints both: premise-based true, conclusion-based false."),
            ("p", "Each has a cost. The premise-based verdict holds the defendant liable though two of the three judges, "
                  "judges two and three, would not. The conclusion-based verdict ignores the court's reasons and leaves it "
                  "saying that a contract existed, that it was breached, and that no liability follows. Choosing between them is a "
                  "choice about whether a group's verdict should follow its reasons or its votes."),
            ("h3", "It is the Condorcet paradox again"),
            ("p", "Three voters, three propositions, each voter consistent, a majority on each proposition that does not cohere. "
                  "The shape is that of the cycle in “Majority Rule and the Condorcet Paradox”, with truth values in place of "
                  "rankings. As there, no judge is at fault, and no tie-break repairs it."),
            ("p", "The court is Kornhauser and Sager's, who called the pattern the doctrinal paradox; Pettit gave it the name used "
                  "here when he showed that any group which votes on connected propositions can meet it, courts or not. "
                  "List and Pettit then proved that, for an agenda like this one, no way of aggregating judgments satisfies all of: "
                  "accepting any consistent judgments from the judges, returning a consistent and complete set, treating every judge "
                  "alike, and deciding every proposition by the same rule applied to its own votes. The premise-based procedure gives "
                  "up the last of these, since it treats the conclusion differently. The theorem is stated, not proved, here."),
            ("p", "The direction of the disagreement is not fixed. If the conclusion is the disjunction `p ∨ q`, take judges who "
                  "accept `p` only, `q` only, and neither. Each premise is accepted by one judge in three, so the premise-based "
                  "procedure rejects both and rejects the disjunction; but two judges accept the disjunction, and the conclusion-based "
                  "procedure accepts it. The third preset shows that case."),
            ("p", "The lab takes an odd number of judges so that no majority ties, and a conclusion made from the premises with "
                  "and, or, not and if-then. It takes each judge's verdicts as given. It cannot say whether a premise is true, "
                  "which is the part the court is there to decide."),
        ],
        "lab": ("choicekit", {
            "mode": "vote",
            "preset": "court",
            "presets": [
                {"id": "court", "label": "Three judges, a conjunction",
                 "kind": "judgment", "atoms": ["p", "q"], "formula": "p&q",
                 "voters": [[1, 1, 1], [1, 0, 0], [0, 1, 0]],
                 "expect": {"voWinner": "premise-based: T; conclusion-based: F", "voCondorcet": "premises T, T; conclusion F"}},
                {"id": "consistent-court", "label": "Three judges who largely agree",
                 "kind": "judgment", "atoms": ["p", "q"], "formula": "p&q",
                 "voters": [[1, 1, 1], [1, 1, 1], [0, 1, 0]],
                 "expect": {"voWinner": "premise-based: T; conclusion-based: T", "voCondorcet": "premises T, T; conclusion T"}},
                {"id": "disjunction", "label": "Three judges, a disjunction",
                 "kind": "judgment", "atoms": ["p", "q"], "formula": "p|q",
                 "voters": [[1, 0, 1], [0, 1, 1], [0, 0, 0]],
                 "expect": {"voWinner": "premise-based: F; conclusion-based: T", "voCondorcet": "premises F, F; conclusion T"}},
            ],
            "panel_title": "Aggregate the judges",
            "panel_intro": "A judgment profile names the premises and then the conclusion, and gives one row per judge: the verdict on "
                           "each premise, and optionally the conclusion. The last row of the table is the majority in each column.",
        }),
        "steps_title": "Aggregating a court's judgments",
        "steps_intro": "Five moves for any set of judges. The last one is the choice the lab cannot make for you.",
        "steps": [
            ("Write each judge's verdicts as a row",
             "One column per premise and one for the conclusion. Check that each judge's conclusion follows from their premises, "
             "since a judge who is inconsistent is a different problem."),
            ("Take the majority in every column",
             "Count the judges who accept the proposition. More than half carries it. An odd number of judges means there are no ties."),
            ("Derive the conclusion from the majority premises",
             "Apply the connective to the majority verdicts on the premises. This is the premise-based verdict."),
            ("Compare it with the majority on the conclusion",
             "That is the conclusion-based verdict. If the two differ, the court's majority judgments are inconsistent."),
            ("Decide which procedure to adopt, and say what it costs",
             "The first follows the reasons and may overrule the majority on the verdict. The second follows the verdict and leaves the "
             "reasons unexplained. The lab computes both and does not pick."),
        ],
        "worked": {
            "title": "Three columns, three majorities",
            "intro": ["Judge 1 accepts p, q and p and q; judge 2 accepts p only; judge 3 accepts q only."],
            "lines": [
                "p        yes, yes, no      -> carries 2 to 1",
                "q        yes, no, yes      -> carries 2 to 1",
                "p and q  yes, no, no       -> fails 1 to 2",
                "premise-based: p, q hold   -> liable",
                "conclusion-based: 1 of 3   -> not liable",
            ],
            "after": [
                "Every judge is consistent, and the court is not. The failure is in the combination of the three consistent sets "
                "of judgments, not in any one of them.",
            ],
        },
        "quiz_title": "Reading a court",
        "quiz": [
            {"q": "In the court of three judges, how many judges accept the premise q?",
             "a": ["1",
                   "3",
                   "2",
                   "0"],
             "c": 2,
             "why": "Judges one and three accept q and judge two rejects it, so q carries 2 to 1. The number 1 is the count of judges "
                    "who accept the conclusion p and q, which is a different column."},
            {"q": "What does the conclusion-based procedure give for the court, and why?",
             "a": ["Liable, because both premises carry",
                   "Not liable, because only one judge in three accepts p and q together",
                   "No verdict, because the majorities are inconsistent",
                   "Liable, because two judges accept p"],
             "c": 1,
             "why": "The conclusion-based procedure counts votes on the conclusion itself, and only judge one accepts it, so it fails 1 to 2. "
                    "The first answer is the premise-based verdict. The procedure does give a verdict, since the conclusion has a majority, "
                    "and the number of judges accepting p alone is not what it counts."},
            {"q": "What does the court show?",
             "a": ["One judge must have reasoned badly",
                   "Three judges are too few for a court",
                   "The premises should be decided by unanimity",
                   "Each judge is consistent, yet the majority judgments on p, q and p and q cannot all be true together"],
             "c": 3,
             "why": "Each row of the table is consistent, and the majorities are yes, yes and no on p, q and their conjunction, which cannot all "
                    "hold. Every judge reasoned correctly, so none is at fault, and the same pattern arises with larger courts. "
                    "Unanimity is one way to avoid it and is a different claim."},
            {"q": "Three judges give verdicts on p and q as 1 0, 0 1 and 0 0, with p or q as the conclusion. What do the two procedures give?",
             "a": ["Premise-based: false; conclusion-based: true",
                   "Premise-based: true; conclusion-based: false",
                   "Both true",
                   "Both false"],
             "c": 0,
             "why": "One judge in three accepts p, and one in three accepts q, so the premise-based procedure rejects both and rejects "
                    "p or q. Judges one and two each accept at least one premise, so two judges accept the conclusion and the "
                    "conclusion-based procedure accepts it. The two procedures disagree, in the opposite direction from the court."},
        ],
        "mistakes": [
            ("Believing that if a majority accepts each premise, a majority accepts the conclusion",
             "In the court, p carries 2 to 1 and q carries 2 to 1, and p and q together fails 1 to 2. The majorities are taken "
             "column by column and a conjunction is not a column that follows the others. The belief would hold if the majorities "
             "were unanimous, and with the court's disagreement it fails."),
            ("Blaming a judge",
             "Each of the three judges accepts the conclusion exactly when they accept both premises, so each is consistent. The "
             "inconsistency appears only when the three sets of verdicts are combined by majority. As with the cycle of "
             "rankings, the fault is in the combining."),
            ("Treating the premise-based procedure as the correct one",
             "In the disjunction preset it rejects both premises, so it rejects the conclusion, though two of the three judges accept "
             "it. The premise-based procedure follows the reasons the majority accepted, and the conclusion-based procedure follows the "
             "verdicts. Which to prefer depends on whether the group is answerable for its reasons or its result."),
        ],
        "standard": ("Finish when you can aggregate a court's judgments on two premises and a conclusion and name the two procedures.",
                     "Given three judges' verdicts, compute the majority on each premise and on the conclusion, derive the "
                     "premise-based verdict, report whether it agrees with the conclusion-based one, and give a profile in which it does not."),
        "note": "Change one judge's row in the court and watch when the contradiction disappears. With three judges and a conjunction it "
                "needs one judge who accepts only p, one who accepts only q, and one who accepts both; change any of the three and the "
                "two procedures agree.",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "the-condorcet-jury-theorem",
        "title": "The Condorcet Jury Theorem",
        "module": "Democracy",
        "one_line": "A majority of voters who are each right more than half the time is right more often than any of them.",
        "summary": (
            "If n independent voters are each right with probability p about a question that has a correct answer, the probability "
            "that a majority is right can be computed exactly. It rises with n when p exceeds one half, falls when p is below one half, "
            "and stays at one half when p equals it. The probability that a single vote decides the outcome shrinks as the electorate "
            "grows. The wrong model is that a large electorate is wise whatever its voters' competence."
        ),
        "key": [
            "majority right = P(more than half are right)",
            "p above 1/2: more voters, better majority",
            "p below 1/2: more voters, worse majority",
            "pivotal: the others split exactly evenly",
        ],
        "key_label": "A majority's chance of being right",
        "concepts_intro": (
            "The earlier lessons treated votes as expressions of preference. This one treats them as estimates of a fact, and asks "
            "what a majority of estimates is worth."
        ),
        "concepts": [
            ("Competence is a probability of being right",
             "Each voter answers a yes-or-no question that has a correct answer, and is right with probability `p`, independently of "
             "the others. The theorem is silent on questions of taste, where there is no answer to be right about."),
            ("The majority is right when more than half are",
             "With an odd number `n` of voters the majority is right exactly when at least `(n + 1)/2` of them are, and the "
             "probability is the sum of the exact probabilities of each such count."),
            ("A vote is pivotal when the others split evenly",
             "One voter decides the result only if the other `n − 1` voters divide exactly half and half. The probability "
             "of that is small, and it falls as the electorate grows."),
        ],
        "read_title": "Three voters, then eleven",
        "read_intro": "The majority's chance of being right, worked out for three voters, compared with eleven, with voters below one half, "
                      "and with the probability that one vote is the one that counts.",
        "body": [
            ("p", "Condorcet's question was whether a group votes better than a person. The case that makes it computable is a "
                  "jury deciding a question of fact, such as whether the accused did it. Suppose each of `n` jurors is right with "
                  "probability `p`, whatever the others think, and the verdict is whatever more than half of them say."),
            ("p", "Take three jurors, each right with probability `3/5`. The majority is right when at least two of them are. All "
                  "three are right with probability `(3/5)·(3/5)·(3/5)`, which is `27/125`. Exactly two are right in three ways, "
                  "according to which juror is wrong, and each way has probability `(3/5)·(3/5)·(2/5)`, so together "
                  "they have probability `54/125`."),
            ("math", [
                "     all three right     (3/5)·(3/5)·(3/5)         27/125",
                "     exactly two right   3·(3/5)·(3/5)·(2/5)       54/125",
                "     majority right      27/125 + 54/125           81/125",
            ]),
            ("p", "So the majority of three is right with probability `81/125`, which is `0.648`, while a single juror is right with "
                  "`3/5`, which is `75/125`. The jury is better than its members, by a little. The lab prints the exact "
                  "fraction and works for any number of jurors up to `101`."),
            ("h3", "More voters"),
            ("p", "With eleven jurors, still each right with probability `3/5`, the majority is right with probability "
                  "`36791901/48828125`, about `0.75`. The gain from the size of the jury has been "
                  "substantial. The pattern is general: if `p` is above `1/2`, the probability that the majority is right "
                  "increases with every added pair of jurors, and tends to certainty."),
            ("p", "The pattern reverses on the other side. Three jurors each right with probability `2/5` produce a majority that is "
                  "right with probability `44/125`, which is less than `2/5`. Eleven such jurors produce `12036224/48828125`, about "
                  "`0.25`. With probability below `1/2` each, the crowd does worse than its members, and the larger the crowd, the worse it "
                  "does. At exactly `1/2` the crowd gains nothing: eleven jurors, each a coin flip, are right with probability `1/2`."),
            ("def", ("The Condorcet jury theorem",
                     "If voters answer a yes-or-no question independently, each right with the same probability `p`, then the "
                     "probability that a majority is right increases with the number of voters when `p` is above `1/2`, "
                     "decreases when it is below, and stays at `1/2` when it equals `1/2`.")),
            ("h3", "What the theorem needs"),
            ("p", "Two assumptions carry the result, and both are strong. The first is independence: each voter's chance of being right "
                  "does not depend on how the others voted. Voters who read the same newspaper are not independent; if each follows a "
                  "newspaper that is right with probability `3/5`, a million voters are right together with probability `3/5` and not "
                  "higher. “Testimony and Independent Witnesses” made the same point about witnesses."),
            ("p", "The second is that there is a fact to be right about, and that voters are better than chance at finding it. A "
                  "vote on a tax rate or a way of life is not an estimate of anything. The theorem's weight rests on the question "
                  "being of the first kind."),
            ("h3", "The pivotal voter"),
            ("p", "The probability that one juror decides the verdict is a different quantity. With three jurors, a given juror "
                  "decides the result only if the other two split, one right and one wrong, which can happen in two ways: "
                  "`2·(3/5)·(2/5)`, which is `12/25`. In general, for odd `n`, the others must divide exactly "
                  "evenly, and the lab prints that probability."),
            ("p", "With eleven jurors at `3/5` it is `1959552/9765625`, about `0.20`; with eleven coin-flipping jurors, `63/256`, about "
                  "`0.25`. The probability shrinks as the electorate grows, and in a national election it is very small. "
                  "That is the paradox of the pivotal voter: the benefit from any one vote is the probability that it decides, "
                  "multiplied by whatever is at stake, and the first factor is tiny. The lab computes the first factor and "
                  "not the second, and what the stakes are worth is a question about welfare, not about probability."),
        ],
        "lab": ("choicekit", {
            "mode": "vote",
            "preset": "three",
            "presets": [
                {"id": "three", "label": "Three jurors, each right with 3/5",
                 "kind": "jury", "n": 3, "p": "3/5",
                 "expect": {"voJury": "81/125", "voPivot": "12/25"}},
                {"id": "eleven", "label": "Eleven jurors, each right with 3/5",
                 "kind": "jury", "n": 11, "p": "3/5",
                 "expect": {"voJury": "36791901/48828125", "voPivot": "1959552/9765625"}},
                {"id": "incompetent", "label": "Three jurors, each right with 2/5",
                 "kind": "jury", "n": 3, "p": "2/5",
                 "expect": {"voJury": "44/125", "voPivot": "12/25"}},
                {"id": "incompetent-eleven", "label": "Eleven jurors, each right with 2/5",
                 "kind": "jury", "n": 11, "p": "2/5",
                 "expect": {"voJury": "12036224/48828125", "voPivot": "1959552/9765625"}},
                {"id": "coin", "label": "Eleven jurors, each right with 1/2",
                 "kind": "jury", "n": 11, "p": "1/2",
                 "expect": {"voJury": "1/2", "voPivot": "63/256"}},
            ],
            "panel_title": "Compute a jury",
            "panel_intro": "A jury reads n=3 p=3/5, with an odd n up to 101 and p a fraction between 0 and 1. The table gives the "
                           "majority's exact probability of being right.",
        }),
        "steps_title": "Computing a jury's majority",
        "steps_intro": "Five moves for an odd number of jurors. The first four give the majority and the last gives the pivotal vote.",
        "steps": [
            ("State the question and the competence",
             "The question has a correct answer and each voter is right with probability `p`, independently. Write down `n` and `p`."),
            ("List the counts that give a majority",
             "For three voters the majority is right when two or three are. In general it is every count of right voters from `(n + 1)/2` to `n`."),
            ("Find the probability of each count",
             "A given set with `k` right and the rest wrong has probability `p` to the power `k` times `1 − p` to the power `n − k`, "
             "and there are as many such sets as ways to choose which `k` are right."),
            ("Add and compare with `p`",
             "The sum is the probability that the majority is right. If it exceeds `p`, the jury has improved on its members."),
            ("Find the pivotal probability",
             "The others must split exactly evenly, `(n − 1)/2` right and `(n − 1)/2` wrong, in as many ways as there are ways to "
             "choose which are right. Multiply by that count."),
        ],
        "worked": {
            "title": "Three jurors, each right with 3/5",
            "intro": ["The majority is right when at least two of the three are."],
            "lines": [
                "all three right:    (3/5)·(3/5)·(3/5)    = 27/125",
                "exactly two right:  3·(3/5)·(3/5)·(2/5)  = 54/125",
                "majority right:     27/125 + 54/125      = 81/125",
                "single juror:       3/5                  = 75/125",
                "pivotal juror:      2·(3/5)·(2/5)        = 12/25",
            ],
            "after": [
                "The majority is right more often than a juror, and the margin is small: 81 against 75 out of 125. The pivotal "
                "probability is 12/25 for three jurors and is already 1959552/9765625 for eleven.",
            ],
        },
        "quiz_title": "Juries and probabilities",
        "quiz": [
            {"q": "Three independent jurors are each right with probability 3/5. What is the probability that a majority is right?",
             "a": ["3/5",
                   "27/125",
                   "54/125",
                   "81/125"],
             "c": 3,
             "why": "Three right gives 27/125 and exactly two right gives 54/125, and the majority is right in either case: 81/125. "
                    "The probability 3/5 is a single juror's, 27/125 counts only the unanimous case, and 54/125 only the case of exactly two."},
            {"q": "Each juror is right with probability 2/5. What happens to the majority's chance of being right as the jury grows?",
             "a": ["It rises toward 1",
                   "It falls toward 0",
                   "It stays at 2/5",
                   "It goes to 1/2"],
             "c": 1,
             "why": "When p is below 1/2 the theorem runs the other way: three jurors give 44/125, below 2/5, and eleven give about 0.25. "
                    "The value 2/5 is only the one-juror case, and 1/2 is the limit only when p equals 1/2."},
            {"q": "A million voters each copy one newspaper, which is right with probability 3/5. How likely is the majority to be right?",
             "a": ["About 1, since the jury is large",
                   "About 0",
                   "3/5, the newspaper's probability",
                   "1/2"],
             "c": 2,
             "why": "If every voter copies the newspaper, the majority is the newspaper's verdict, right exactly when it is right, with "
                    "probability 3/5. The independence assumption is what lets a large jury approach certainty, and it fails here."},
            {"q": "Three jurors are each right with probability 3/5. The probability that a given juror is pivotal is 12/25. What event has that probability?",
             "a": ["That the juror is right",
                   "That the other two are both right",
                   "That the majority is right",
                   "That exactly one of the other two is right"],
             "c": 3,
             "why": "A juror decides the result only if the other two split. That happens when one is right and the other wrong, in two "
                    "ways, and 2·(3/5)·(2/5) is 12/25. Both others right has probability 9/25, and the majority being right is 81/125."},
        ],
        "mistakes": [
            ("Believing that a large electorate is wise whatever its voters' competence",
             "With each voter right with probability 2/5, three voters give a majority right with probability 44/125, less than "
             "2/5, and eleven give about 0.25. With each a coin flip, eleven give exactly 1/2. The size of the electorate "
             "magnifies whatever the voters' competence already is, upward above 1/2 and downward below it."),
            ("Reading the theorem as being about preferences",
             "The result concerns a question with a correct answer, about which each voter has a probability of being right. A vote "
             "for a tax rate has no answer to be right about, and the theorem does not apply to it. It is a claim about "
             "estimating a fact, and the impossibility results of the earlier lessons are claims about combining preferences."),
            ("Concluding from a small pivotal probability that a vote is worthless",
             "The value of a vote is the probability that it decides times the stakes. At eleven jurors at 3/5 the first factor is about "
             "0.20, and for a very large electorate it is far smaller, but it is multiplied by a stake that may be shared among millions. "
             "The lab computes only the first factor, so the conclusion needs a second premise about the stakes, the question "
             "“Public Goods and Free-Riding” asks of one contribution among many."),
        ],
        "standard": ("Finish when you can compute a majority's probability of being right and a voter's chance of being pivotal.",
                     "Given n and p, write the probability that a majority is right as a sum, evaluate it for three voters, say which "
                     "way it moves as n grows when p is above, at and below one half, and compute the pivotal probability."),
        "note": "Try n = 1 and see that the majority of one is the voter. Then compare the pivotal probabilities of the two eleven-juror "
                "presets at 3/5 and 2/5: they are the same, because a juror who is wrong with probability 3/5 "
                "decides the verdict with the same chance as one who is right with probability 3/5.",
    },
]
