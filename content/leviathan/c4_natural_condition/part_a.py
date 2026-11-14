"""The Natural Condition and the Laws of Nature, lessons 1-4 -- Chapter 13 and Chapter 14 to the end of 'merit'.

Every quotation is from the text of 1651 as the operator's copy prints it, in its
original spelling; the comment beside each lesson gives the chapter, the 1651 page
(Tuck prints it in the margin in square brackets) and the PDF page of the copy.
Italics are dropped, a long s is printed as s, and nothing else is changed.

The two lessons whose lab is `levkit` (equality-of-ability, contracts-and-covenants)
are marked LEVKIT: their cfg is drafted from docs/leviathan/PLAN.md section D.1 and
is corrected against docs/leviathan/kit-report.md once the kit is registered.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Leviathan ch. 13, 1651 p. 60-61; PDF p. 182-183 of the operator's copy.
    # LEVKIT: equality / coalition.
    {
        "slug": "equality-of-ability",
        "title": "Equality of Ability",
        "module": "Chapter 13 · Of the Naturall Condition of Mankind",
        "one_line": "Hobbes starts the war with a claim about strength: the weakest man can kill the strongest by a plot or with allies, so no one's strength entitles him to more than others claim.",
        "summary": (
            "Chapter 13 opens with equality, not with fear. Hobbes grants that one man is sometimes manifestly "
            "stronger or quicker than another and says the difference is not great enough to give him a claim "
            "that others may not make as well, because the weakest can kill the strongest by secret machination "
            "or by confederacy. Six men's strengths are added up to find who can be overcome, by how few, and "
            "how large a difference would break the claim."
        ),
        "key": [
            "weakest can kill strongest: plot or allies",
            "equal ability gives equal hope",
            "equal hope, one object: they become enemies",
            "a coalition beats anyone it outweighs",
            "a giant who outweighs all the rest is safe",
        ],
        "key_label": "The first step of the war, in five lines",
        "concepts_intro": (
            "The chapter's first two paragraphs are an argument in three steps, from what men are able to do to "
            "what they come to hope for and from there to what they do to one another."
        ),
        "concepts": [
            ("Equality of body",
             "Hobbes does not say men are equally strong. He says that when all is reckoned together the "
             "difference between man and man is not so considerable that one can claim a benefit another may not "
             "pretend to as well, because the weakest has strength enough to kill the strongest, either by secret "
             "machination or by confederacy with others who are in the same danger."),
            ("Equality of mind",
             "He finds an even greater equality of mind, setting aside the arts grounded on words and science, "
             "which very few have. Prudence is only experience, which equal time bestows equally on all men in "
             "the things they equally apply themselves to. What makes this seem incredible is a vain conceit of "
             "one's own wisdom."),
            ("From equal ability to enmity",
             "From equality of ability comes equality of hope in attaining our ends. If two men want the same "
             "thing and cannot both enjoy it, they become enemies and try to destroy or subdue one another. An "
             "invader who fears only one man's single power finds others coming with united forces against the "
             "man who plants and builds, and the invader is in the like danger of another."),
        ],
        "read_title": "The passage first, then equality of strength, of mind and of hope",
        "read_intro": (
            "Hobbes's opening paragraph is one long sentence of concessions followed by a claim. The lesson reads "
            "it whole, then goes through what he grants and what he denies."
        ),
        "body": [
            ("p", "<strong>Chapter 13.</strong> &ldquo;Nature hath made men so equall, in the faculties of body, and "
                  "mind; as that though there bee found one man sometimes manifestly stronger in body, or of quicker "
                  "mind then another; yet when all is reckoned together, the difference between man, and man, is not "
                  "so considerable, as that one man can thereupon claim to himselfe any benefit, to which another may "
                  "not pretend, as well as he. For as to the strength of body, the weakest has strength enough to "
                  "kill the strongest, either by secret machination, or by confederacy with others, that are in the "
                  "same danger with himselfe.&rdquo;"),
            ("p", "Leviathan came out in London in 1651. Two years before, a king had been tried and beheaded in "
                  "the same city, and Hobbes, who had left England for Paris in 1640, wrote the book in exile while "
                  "the quarrel that killed him was still being fought. The chapter people remember is this one, the "
                  "chapter of the war of every man against every man, and it is worth noticing where it starts. It "
                  "does not start with fear, or greed, or wickedness. It starts with a claim about arithmetic: how "
                  "much stronger can one man be than another."),
            ("p", "Read the sentence for what Hobbes gives away. He allows that one man is &ldquo;sometimes "
                  "manifestly stronger in body, or of quicker mind&rdquo; than another. What he denies is that the "
                  "difference is enough to found a title. The test is in the words &ldquo;when all is reckoned "
                  "together&rdquo; (in Chapter 5 he had said that reason is nothing but reckoning, adding and "
                  "subtracting) and in the phrase &ldquo;any benefit, to which another may not pretend, as well as "
                  "he&rdquo;. Equality here means equality of claim: no man's superiority is so large that the rest "
                  "have no ground to say <em>and why not I</em>."),
            ("p", "Then the proof for the body, in two ways. By &ldquo;secret machination&rdquo; the weakest "
                  "overcomes the strongest because the strongest sleeps, or looks away, or does not know. By "
                  "&ldquo;confederacy with others, that are in the same danger with himselfe&rdquo; he overcomes "
                  "him by adding strengths. The lab does the second as a sum. Six men, whose strengths are the "
                  "lesson's own figures and nothing Hobbes gives, have `10`, `8`, `7`, `6`, `5` and `3`. In an open "
                  "fight (the open preset) the strongest, Aldo, cannot be beaten by Bea alone, who has `8`, but can "
                  "be beaten by Bea and Cato together, who have `15`, so two others are enough. Everyone else is "
                  "beaten by Aldo alone, who outweighs each of them, so all six men can be overcome by two or fewer."),
            ("p", "Secret machination goes into the lab as a factor on the attacker's strength: a sleeping victim "
                  "is as good as a weaker one. In the machination preset the factor is `4`, so Finn, the weakest, "
                  "has `3 × 4 = 12`, which is more than Aldo's `10`, and Hobbes's claim in its first form holds: "
                  "the weakest has strength enough to kill the strongest. The lab keeps the claim honest by "
                  "showing what would break it. In the giant preset Aldo has `24`, and the others must all but "
                  "gather to beat him: Bea, Cato, Dara and Edo together have `26`, so four of the five are needed. "
                  "In the beyond preset he has `30`, and the other five together reach only `29`: he is beyond "
                  "every coalition. Hobbes's premise is therefore a premise about size. It says that the "
                  "strongest man is never so far ahead that all the rest together cannot match him, and it "
                  "leaves to the reader whether men are like that."),
            ("p", "Now the mind. Hobbes says he finds &ldquo;a greater equality amongst men, than that of "
                  "strength&rdquo;, and takes out two exceptions at once: &ldquo;the arts grounded upon "
                  "words&rdquo; and science, which &ldquo;very few have, and but in few things&rdquo;. What is left "
                  "is prudence, and &ldquo;Prudence, is but Experience; which equall time, equally bestowes on all "
                  "men, in those things they equally apply themselves unto&rdquo;. Then comes his most sardonic "
                  "paragraph. What makes this equality hard to believe is &ldquo;a vain conceipt of ones owne "
                  "wisdome&rdquo;, since every man will grant that others are more witty, more eloquent, or more "
                  "learned, yet &ldquo;will hardly believe there be many so wise as themselves&rdquo;, for &ldquo;they "
                  "see their own wit at hand, and other mens at a distance&rdquo;. And he turns the vanity into the "
                  "proof: there is no greater sign of an equal distribution of anything than that every man is "
                  "contented with his share."),
            ("p", "The third paragraph is where equality starts to do harm. &ldquo;From this equality of ability, "
                  "ariseth equality of hope in the attaining of our Ends.&rdquo; If two men want the same thing and "
                  "cannot both have it, they become enemies, and the end each pursues is &ldquo;principally their "
                  "owne conservation, and sometimes their delectation only&rdquo;. Notice that the ends are modest. "
                  "Then the invader enters. Where an invader fears no more than one man's single power, someone who "
                  "plants, sows or builds may expect others to come &ldquo;prepared with forces united&rdquo;, to "
                  "take from him &ldquo;not only of the fruit of his labour, but also of his life, or liberty&rdquo;. And "
                  "&ldquo;the Invader again is in the like danger of another.&rdquo; The weakest may kill the "
                  "strongest, so everybody has reason to fear everybody, and fear is the next lesson's subject."),
            ("p", "Two objections suggest themselves, and the book has something to say to each. Aristotle, whom Hobbes "
                  "names in Chapter 15, had held that some men are by nature fitter to command and others to serve. "
                  "Hobbes answers that this is against experience as well as reason, since the wise in their own "
                  "conceit do not often win when they contend by force with men who distrust their own wisdom. The "
                  "second objection is that the weak do not combine so easily. Allies in &ldquo;the same "
                  "danger&rdquo; have a motive to join, and the lab supposes they do. Whether each would trust the "
                  "others to stay in is a different question, and Chapter 14's covenants are where the book comes to "
                  "it. The lab adds strengths and stops there."),
            ("p", "So far the chapter has said what men can do to each other. The next lesson, &ldquo;The War of "
                  "Every Man Against Every Man&rdquo;, reads what Hobbes concludes from it: the three causes of "
                  "quarrel, the condition he calls war, and the claim that in it nothing is unjust."),
        ],
        # LEVKIT: cfg drafted from PLAN D.1; corrected against kit-report.md in phase B.
        "lab": ("levkit", {
            "mode": "equality",
            "view": "coalition",
            "preset": "open",
            "presets": [
                {"id": "open", "label": "Six men in an open fight",
                 "persons": [["Aldo", 10], ["Bea", 8], ["Cato", 7], ["Dara", 6], ["Edo", 5], ["Finn", 3]],
                 "machination": 1, "rule": "exceed", "expect": {"leqFewest": "Aldo: 2 (Bea + Cato); Bea: 1 (Aldo); Cato: 1 (Aldo); Dara: 1 (Aldo); Edo: 1 (Aldo); Finn: 1 (Aldo)", "leqWeakAlone": "no: Finn, 3, does not exceed Aldo, 10", "leqByTwo": "6 of 6"}},
                {"id": "machination", "label": "A plot against a sleeping man: attackers count four times",
                 "persons": [["Aldo", 10], ["Bea", 8], ["Cato", 7], ["Dara", 6], ["Edo", 5], ["Finn", 3]],
                 "machination": 4, "rule": "exceed", "expect": {"leqWeakAlone": "yes: Finn, 3 × 4 = 12, exceeds Aldo, 10", "leqByTwo": "6 of 6"}},
                {"id": "giant", "label": "Aldo has 24",
                 "persons": [["Aldo", 24], ["Bea", 8], ["Cato", 7], ["Dara", 6], ["Edo", 5], ["Finn", 3]],
                 "machination": 1, "rule": "exceed", "expect": {"leqFewest": "Aldo: 4 (Bea + Cato + Dara + Edo); Bea: 1 (Aldo); Cato: 1 (Aldo); Dara: 1 (Aldo); Edo: 1 (Aldo); Finn: 1 (Aldo)", "leqBeyond": "0: none", "leqByTwo": "5 of 6"}},
                {"id": "beyond", "label": "Aldo has 30",
                 "persons": [["Aldo", 30], ["Bea", 8], ["Cato", 7], ["Dara", 6], ["Edo", 5], ["Finn", 3]],
                 "machination": 1, "rule": "exceed", "expect": {"leqFewest": "Aldo: no coalition; Bea: 1 (Aldo); Cato: 1 (Aldo); Dara: 1 (Aldo); Edo: 1 (Aldo); Finn: 1 (Aldo)", "leqBeyond": "1: Aldo", "leqByTwo": "5 of 6"}},
            ],
            "panel_title": "Who can be overcome, and by how few",
            "panel_intro": (
                "Six men's strengths go in, with a factor for secret machination. For each man the lab finds the "
                "fewest others whose strengths, added and multiplied by the factor, exceed his. Start with the "
                "open fight, then change Aldo's strength and watch the figure for the fewest others who overcome each man."
            ),
        }),
        "steps_title": "Testing Hobbes's equality for a stated group",
        "steps_intro": "Four steps, the same for any set of strengths.",
        "steps": [
            ("List each man's strength as one number",
             "The lab takes strength to be a single figure that adds. That is a model of Hobbes's body, "
             "and the figures are the lesson's, not the book's."),
            ("Fix the factor for the attack",
             "Use `1` for an open fight. Use a larger factor where the attacker has the advantage of a plot, "
             "a surprise or a sleeping victim, and say which."),
            ("Find the fewest attackers",
             "For each man, add the other men's strengths from the strongest down, each multiplied by the "
             "factor, until the sum exceeds his. The number added is the smallest coalition."),
            ("Read the result against the claim",
             "If even the strongest is overcome by a few, no man's strength is a title to more than others "
             "claim. If someone is beyond every coalition, the claim fails for him on these figures."),
        ],
        "worked": {
            "title": "Aldo at ten, at twenty-four and at thirty",
            "intro": [
                "Six men have `10`, `8`, `7`, `6`, `5` and `3`. Who can beat Aldo, who has `10`, and what does a "
                "plot do for Finn, who has `3`?",
            ],
            "lines": [
                "open fight, Aldo 10:  Bea 8 is not enough",
                "Bea and Cato:  8 + 7 = 15, more than 10",
                "fewest attackers:  2",
                "plot, factor 4:  Finn alone has 3 · 4 = 12",
                "12 is more than 10:  the weakest beats the strongest",
                "Aldo 30:  8 + 7 + 6 + 5 + 3 = 29, not more than 30",
            ],
            "after": [
                "At `24` the other five must still combine: `8 + 7 + 6 + 5 = 26` is the first sum above `24`, so "
                "four men are needed. At `30` no coalition is large enough, and Hobbes's sentence would not be "
                "true of a man like that.",
            ],
        },
        "quiz_title": "Strength added up",
        "quiz": [
            {"q": "Six men have strengths 10, 8, 7, 6, 5 and 3, and the lab uses an open fight with a factor of 1. "
                  "What is the fewest number of the others that can overcome the strongest?",
             "a": ["One, because the second-strongest is nearly as strong",
                   "Two, because 8 alone is not more than 10 but 8 and 7 together are",
                   "Three, because only the three strongest others together are enough",
                   "None, because he is stronger than any one of them"],
             "c": 1,
             "why": "Bea's `8` does not exceed `10`, and `8 + 7 = 15` does, so the fewest is two. One fails by "
                    "the lab's rule, which needs a strictly greater sum. Three is more than the smallest "
                    "coalition, and the lab asks for the smallest. The strongest being stronger than each "
                    "other man alone is true and is the reason he needs a coalition to beat."},
            {"q": "In the plot preset every attacker's strength counts four times. What does that give Finn, "
                  "who has 3, against Aldo, who has 10?",
             "a": ["Nothing, because 3 is still less than 10",
                   "A tie, because 3 and 10 are both in the same group",
                   "Enough alone, because 12 is more than 10",
                   "Enough only if two more men join him"],
             "c": 2,
             "why": "The factor multiplies the attacker's strength, so Finn's `3` counts as `12`, which exceeds "
                    "`10`. This is Hobbes's &ldquo;secret machination&rdquo; in the lab's terms: the weakest has "
                    "strength enough to kill the strongest without any allies."},
            {"q": "Which of these makes Hobbes's claim fail for the strongest man, on the lab's model?",
             "a": ["He is stronger than the second-strongest man",
                   "He has more than the average strength of the group",
                   "He has three times the strength of the weakest man",
                   "He has more strength than all the other men together"],
             "c": 3,
             "why": "If his strength exceeds the sum of every other man's, even the whole group at a factor of "
                    "`1` cannot overcome him, which is the case of the `30` preset. The other three are true of "
                    "Aldo at `10`, who can still be beaten by Bea and Cato."},
            {"q": "What does Hobbes say may make the equality of mind seem incredible?",
             "a": ["The arts grounded upon words",
                   "A vain conceit of one's own wisdom",
                   "The strength of the strongest man",
                   "The scarcity of experience in the world"],
             "c": 1,
             "why": "The text names &ldquo;a vain conceipt of ones owne wisdome&rdquo;. The arts grounded on words "
                    "and science are the exceptions he sets aside, not what makes the equality hard to believe. "
                    "Experience, he says, is the one thing time gives equally to all."},
        ],
        "mistakes": [
            ("Thinking Hobbes says men are equally strong and equally clever",
             "He says the opposite at the start: &ldquo;manifestly stronger in body, or of quicker mind&rdquo;. What he "
             "claims is that the difference is not so considerable that one man may claim a benefit another may "
             "not. He also takes science and the arts of words out of the comparison, and in the lab Aldo has "
             "`10` where Finn has `3`."),
            ("Reading the equality as a compliment",
             "The chapter does not praise men for being alike. Equal ability yields equal hope, equal hope for "
             "one thing yields enmity, and the weakest being able to kill the strongest is a reason for the "
             "strongest to be afraid. Equality is the premise of the danger."),
            ("Thinking the lab predicts that the weak will band together",
             "The figure says only that a coalition of that size would have strength enough. Whether the allies "
             "would find one another and stay in is a question about trust, and the lab does not touch it. "
             "Hobbes's phrase is &ldquo;confederacy with others, that are in the same danger with himselfe&rdquo;, "
             "which gives them a motive and no more."),
        ],
        "standard": (
            "Finish when you can say who can be overcome and by how few.",
            "Given six men's strengths and a factor for machination, compute for the strongest and the weakest "
            "the fewest others that can overcome them, say whether any man is beyond every coalition, and say "
            "what that does to Hobbes's claim."
        ),
        "note": (
            "Strength is a single number in the lab, and it adds. A real contest is not a sum, and Hobbes's "
            "&ldquo;when all is reckoned together&rdquo; is a judgement about men that no figure here can make. "
            "The lab shows how large a difference would break his premise, and whether men differ by that much is "
            "what the premise states and a critic may dispute."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Leviathan ch. 13, 1651 p. 62-63; PDF p. 184-186 of the operator's copy.
    # choicekit/game; names the Philosophy lesson "Hobbes and the State of Nature".
    {
        "slug": "the-war-of-every-man",
        "title": "The War of Every Man Against Every Man",
        "module": "Chapter 13 · Of the Naturall Condition of Mankind",
        "one_line": "Hobbes's war is a standing disposition to fight, not a battle: competition, diffidence and glory each make a man strike first, and where there is no common power nothing is unjust.",
        "summary": (
            "From equal ability and equal hope Hobbes derives three causes of quarrel, which make men invade for "
            "gain, for safety and for reputation, and a condition he calls war, which lies in a known disposition "
            "to fight over a stretch of time. The chapter draws the incommodities of that condition, tests the "
            "inference against what everyone does when he locks his door, and concludes that where there is no "
            "common power nothing can be unjust. Three small games show competition, diffidence, and a mixed pair "
            "in which one man's pleasure in conquest is enough to bring the other in."
        ),
        "key": [
            "competition for gain, diffidence for safety",
            "glory for reputation, even for a smile",
            "war is a known disposition, not a battle",
            "anticipation is the reasonable defence",
            "no common power, no law, no injustice",
        ],
        "key_label": "Three causes, one condition",
        "concepts_intro": (
            "The passage runs from the causes of quarrel to the condition they produce and then to what follows "
            "in it. Three ideas carry it."
        ),
        "concepts": [
            ("Three causes of quarrel",
             "Competition makes men invade for gain, diffidence for safety and glory for reputation. Diffidence is "
             "the one Hobbes calls reasonable: the best way to secure oneself is anticipation, mastering the "
             "persons of all the men one can until no other power is great enough to endanger one."),
            ("War is a disposition",
             "War does not consist in battle only. It is a tract of time in which the will to contend by battle is "
             "sufficiently known, as foul weather lies not in a shower or two but in an inclination to rain over many "
             "days. In that condition there is no industry, no arts, no letters, no society and continual fear."),
            ("Nothing is unjust",
             "Where there is no common power there is no law, and where there is no law there is no injustice. "
             "Right and wrong, justice and injustice, and the distinction of mine and thine have no place, and "
             "force and fraud are in war the two cardinal virtues."),
        ],
        "read_title": "The causes, the condition, the evidence and what follows",
        "read_intro": (
            "The lesson reads the sentence that names the condition, then takes the argument in the order Hobbes "
            "gives it. The Philosophy course already has a lesson, &ldquo;Hobbes and the State of Nature&rdquo; in "
            "Games and the Social Contract, that writes this argument as two tables and a sovereign's fine. This "
            "one reads the text of the chapter and does not repeat that lesson."
        ),
        "body": [
            ("p", "<strong>Chapter 13.</strong> &ldquo;Hereby it is manifest, that during the time men live without a "
                  "common Power to keep them all in awe, they are in that condition which is called Warre; and such "
                  "a warre, as is of every man, against every man.&rdquo;"),
            ("p", "Most people know this chapter by its last phrase about the life of man, and most take it for a "
                  "picture of the past, a prehistory of brutes. Read in order, it is an argument, and the "
                  "argument has steps. The steps begin before the sentence above, in the paragraph on anticipation, "
                  "which is where the last lesson's diffidence leads. &ldquo;From this diffidence of one another, "
                  "there is no way for any man to secure himselfe, so reasonable, as Anticipation&rdquo;, that is, "
                  "&ldquo;by force, or wiles, to master the persons of all men he can, so long, till he see no other "
                  "power great enough to endanger him&rdquo;. And Hobbes adds that this &ldquo;is no more than his "
                  "own conservation requireth, and is generally allowed&rdquo;."),
            ("p", "Then he brings in the men who are not modest. Some take pleasure &ldquo;in contemplating their "
                  "own power in the acts of conquest&rdquo;, and pursue it &ldquo;farther than their security "
                  "requires&rdquo;. Others, who would otherwise be &ldquo;glad to be at ease within modest "
                  "bounds&rdquo;, cannot then stand only on their defence for long, so they too must increase their "
                  "power by invasion. His conclusion is that such augmentation of dominion &ldquo;being necessary "
                  "to a mans conservation, it ought to be allowed him&rdquo;. This is the argument's cleverest "
                  "step: one man who enjoys conquest is enough to make the rest act as he does, whatever they want."),
            ("p", "Glory has a second form, which is touchier. Every man looks that his companion should value "
                  "him at the rate he sets on himself, and &ldquo;upon all signes of contempt, or undervaluing, "
                  "naturally endeavours, as far as he dares&rdquo;, to extort a greater value from those who slight "
                  "him. So the chapter names &ldquo;three principall causes of quarrell. First, Competition; "
                  "Secondly, Diffidence; Thirdly, Glory&rdquo;, and sums them: the first makes men invade for gain, "
                  "the second for safety, and the third for reputation, over &ldquo;trifles, as a word, a smile, a "
                  "different opinion&rdquo;. That is the list a modern reader finds hardest to dismiss, since "
                  "anyone who has seen a fight start over a look knows Hobbes was not describing a remote people."),
            ("p", "Now the sentence we began with, and the definition. War &ldquo;consisteth not in Battell onely, "
                  "or the act of fighting; but in a tract of time, wherein the Will to contend by Battell is "
                  "sufficiently known&rdquo;, and Hobbes borrows an image from weather: &ldquo;the nature of Foule "
                  "weather, lyeth not in a showre or two of rain; but in an inclination thereto of many dayes "
                  "together&rdquo;. So it is with war, which is &ldquo;the known disposition thereto, during all "
                  "the time there is no assurance to the contrary&rdquo;. It follows that a man can be at war and "
                  "at home in bed. What is missing is assurance, and that is the thing the three causes take away."),
            ("p", "What follows is the best-known passage in English political philosophy. In such a condition "
                  "&ldquo;there is no place for Industry; because the fruit thereof is uncertain&rdquo;, and so no "
                  "culture of the earth, no navigation, no commodious building, no arts, no letters, no society, and "
                  "&ldquo;which is worst of all, continuall feare, and danger of violent death; And the life of man, "
                  "solitary, poore, nasty, brutish, and short.&rdquo; Notice that the list is a list of what "
                  "industry makes possible, and what the war takes away is the safety that makes building worth "
                  "the trouble."),
            ("p", "He knows the reader will doubt it, and offers an experiment that costs nothing. When a man takes "
                  "a journey he arms himself and goes well accompanied, when he goes to sleep he locks his doors, "
                  "and in his house he locks his chests, and he does all this &ldquo;when he knowes there bee Lawes, "
                  "and publike Officers, armed, to revenge all injuries shall bee done him&rdquo;. &ldquo;Does he not "
                  "there as much accuse mankind by his actions, as I do by my words?&rdquo; Hobbes then adds the "
                  "sentence that stops the argument from being a slander: &ldquo;But neither of us accuse mans "
                  "nature in it.&rdquo; The desires and passions of man &ldquo;are in themselves no Sin&rdquo;, and "
                  "neither are the actions that proceed from them &ldquo;till they know a Law that forbids "
                  "them&rdquo;. A law cannot be known before it is made, nor made until men have agreed on the person "
                  "who shall make it."),
            ("p", "Was there ever such a time? Hobbes says he believes the war &ldquo;was never generally so, over "
                  "all the world&rdquo;, but that there are many places where men live so now, and he names the "
                  "&ldquo;savage people in many places of America&rdquo;, who have no government but that of small "
                  "families. He adds two nearer cases: civil war, which shows what men degenerate into, and "
                  "sovereigns, who are always &ldquo;in the state and posture of Gladiators&rdquo;, with their forts "
                  "and spies pointed at each other, though because they uphold the industry of their subjects the "
                  "misery of particular men does not follow. John Locke, writing the <em>Second Treatise</em> "
                  "some forty years later, held that the state of nature and the state of war are as far apart as "
                  "peace and enmity, and Rousseau in the next century argued that Hobbes had put into natural man "
                  "the passions of men already living in society. Both are objecting to this step, from the "
                  "disposition of men with a long history to the condition of men with none."),
            ("p", "The last consequence is the one the chapter turns on. &ldquo;Where there is no common Power, "
                  "there is no Law: where no Law, no Injustice. Force, and Fraud, are in warre the two Cardinall "
                  "vertues.&rdquo; Hobbes's reason is a short argument about what justice is. It is not a faculty of "
                  "body or mind, for if it were it &ldquo;might be in a man that were alone in the world, as well as "
                  "his Senses, and Passions&rdquo;, but are &ldquo;Qualities, that relate to men in Society, not "
                  "in Solitude&rdquo;. So there is no propriety, no dominion, and nothing is any man's but "
                  "&ldquo;that to be every mans, that he can get; and for so long, as he can keep it&rdquo;. The chapter ends on the way out, which is "
                  "partly in the passions, &ldquo;Feare of Death&rdquo; among them, and partly in reason, which "
                  "&ldquo;suggesteth convenient Articles of Peace&rdquo;. Those articles, he says, are the laws of "
                  "nature, and the next two chapters take them."),
            ("h3", "Three tables"),
            ("p", "The lab writes three of the chapter's cases as two-person games, with numbers the lesson chooses. "
                  "In <strong>competition</strong>, peace with peace pays `4` each, attacking a peaceful man pays "
                  "`6` and leaves him `0`, and two attackers get `1` each. Attacking pays more whatever the other "
                  "does, so both attack and each gets `1` where peace would have given `4`. In "
                  "<strong>diffidence</strong> nobody gains by attacking a peaceful man: peace with peace pays "
                  "`5` each, a lone attacker takes only `4`, and two attackers get `2`. Attacking now pays more only "
                  "if the other will probably attack, and the lab's mixed equilibrium figure gives the point of change at `2/3`: "
                  "peace is worth keeping if the other keeps it with a chance above two in three. The game has "
                  "two equilibria, peace with peace and attack with attack, which is why a quarrel can start "
                  "among people who want nothing from one another."),
            ("p", "The third table, the <strong>pair</strong> preset, is the paragraph on the immoderate few. The "
                  "column player takes pleasure in conquest: attacking a peaceful man pays him `6`, and being "
                  "attacked while at peace pays him `0`. The row player is content: peace with peace pays him `4`, "
                  "attacking first pays him `3`, and meeting an attack pays him `2` if he fights and `0` if he does "
                  "not. Attack is the conqueror's best move whatever the other does, and the content man's best "
                  "reply to an attacker is to attack, so the one equilibrium is attack with attack, though one of "
                  "the two would have kept the peace. This is the chapter's point that a few are enough, and the lab "
                  "reaches it with a single player for whom attack beats peace. What the tables leave out is "
                  "glory over a smile, which has no payoff to attach to it, and the time that makes war a "
                  "disposition: the games are played once."),
            ("p", "The next lesson, &ldquo;The Right and the Law of Nature&rdquo;, reads Chapter 14 and the "
                  "question the war leaves: what right has a man in such a condition, and what rule of reason "
                  "points out of it."),
        ],
        "lab": ("choicekit", {
            "mode": "game",
            "view": "best",
            "preset": "competition",
            "presets": [
                {"id": "competition", "label": "Competition: attacking a peaceful man pays 6",
                 "rows": ["Peace", "Attack"], "cols": ["Peace", "Attack"],
                 "payoffs": [[[4, 4], [0, 6]], [[6, 0], [1, 1]]], "expect": {"gaPure": "(Attack, Attack)", "gaDom": "Attack dominates for both", "gaPareto": "(Attack, Attack) is dominated by (Peace, Peace)"}},
                {"id": "diffidence", "label": "Diffidence: a lone attacker takes only 4",
                 "rows": ["Peace", "Attack"], "cols": ["Peace", "Attack"],
                 "payoffs": [[[5, 5], [0, 4]], [[4, 0], [2, 2]]], "expect": {"gaPure": "(Peace, Peace); (Attack, Attack)", "gaDom": "none", "gaMixed": "row Peace: 2/3, col Peace: 2/3"}},
                {"id": "pair", "label": "One man enjoys conquest, the other would keep the peace",
                 "rows": ["Peace", "Attack"], "cols": ["Peace", "Attack"],
                 "payoffs": [[[4, 4], [0, 6]], [[3, 0], [2, 2]]], "expect": {"gaPure": "(Attack, Attack)", "gaDom": "Attack dominates for column", "gaPareto": "(Attack, Attack) is dominated by (Peace, Peace)"}},
            ],
            "panel_title": "Three causes of quarrel as games",
            "panel_intro": (
                "Each preset is a two-person game with payoffs the lesson chose. Read the pure equilibria, then "
                "ask what the first man would have to believe about the second for peace to be his best reply."
            ),
        }),
        "steps_title": "Turning a cause of quarrel into a game",
        "steps_intro": "Four steps, for any of the three causes.",
        "steps": [
            ("Name the two moves",
             "Peace or attack. Hobbes's argument runs on these two, so a third has to be argued for."),
            ("Write what an attacker gets from a peaceful man",
             "If it is more than peace pays, the cause is competition. If it is less, so that attacking is only "
             "a defence against attack, the cause is diffidence."),
            ("Add the man who enjoys conquest",
             "Give one player a larger payoff for attacking a peaceful man and a lower one for being attacked, "
             "and leave the other's payoffs as they were."),
            ("Find the equilibria and compare them with peace",
             "For each player check whether the other's move changes his best reply. An equilibrium that pays "
             "both less than peace is the lab's picture of the war."),
        ],
        "worked": {
            "title": "Diffidence and the point of change",
            "intro": [
                "Peace with peace pays `5` each, a lone attacker takes `4` and leaves the other `0`, and two "
                "attackers get `2` each. Let `q` be the chance one man gives to the other keeping the peace.",
            ],
            "lines": [
                "peace pays:  5 · q + 0 · (1 − q) = 5q",
                "attack pays:  4 · q + 2 · (1 − q) = 2 + 2q",
                "equal when 5q = 2 + 2q, so q = 2/3",
                "above 2/3 peace is the better reply;  below, attack",
                "equilibria:  (peace, peace) and (attack, attack)",
            ],
            "after": [
                "Nothing in the table makes either man greedy. A man who thinks the other will probably attack "
                "does better to attack first, and the other, thinking the same, does likewise. This is Hobbes's "
                "diffidence, and it is the cause he calls reasonable.",
            ],
        },
        "quiz_title": "Three causes in three tables",
        "quiz": [
            {"q": "In the pair preset, why does the man who would keep the peace attack?",
             "a": ["Attacking pays him more than peace whatever the other does",
                   "He enjoys conquest as much as the other does",
                   "He expects the other to attack, and against an attack attacking pays him 2 where peace pays 0",
                   "Peace with peace pays him less than attacking first"],
             "c": 2,
             "why": "The conqueror's attack beats peace in both columns, so the content man expects an attack, "
                    "and against an attack his best move is to attack. Attacking does not beat peace in both "
                    "columns for him: against a peaceful man peace pays `4` and attacking `3`. And peace with peace "
                    "pays him more than attacking first, which is why he would keep it."},
            {"q": "Hobbes compares war to the weather. What does the comparison say?",
             "a": ["War, like foul weather, lies in an inclination over many days, not in a shower or two",
                   "War, like foul weather, comes in seasons that can be predicted",
                   "War is as hard to prevent as a storm",
                   "War, like weather, ends of itself"],
             "c": 0,
             "why": "The text says the nature of foul weather &ldquo;lyeth not in a showre or two of rain; but in "
                    "an inclination thereto of many dayes together&rdquo;, so war lies in a known disposition to "
                    "fight and not in actual fighting. The other three are not in the passage."},
            {"q": "In the diffidence preset, peace pays 5q and attack pays 2 + 2q, where q is the chance the "
                  "other keeps the peace. When is peace the better reply?",
             "a": ["When q is above 1/3",
                   "Whenever q is above 1/2",
                   "Only when q is 1",
                   "When q is above 2/3"],
             "c": 3,
             "why": "Peace beats attack when `5q` exceeds `2 + 2q`, that is when `3q` exceeds `2`, so when `q` exceeds "
                    "`2/3`. At `1/2` the two payoffs are `5/2` and `3`, and attack is still better. At `1/3` the "
                    "payoffs are `5/3` and `8/3`."},
            {"q": "According to Hobbes, what is true of justice in the condition of war?",
             "a": ["Everything done in it is unjust",
                   "Nothing can be unjust, because without a common power there is no law",
                   "It remains a faculty of the mind in every man",
                   "Only force is just"],
             "c": 1,
             "why": "&ldquo;Where there is no common Power, there is no Law: where no Law, no Injustice.&rdquo; "
                    "Calling everything unjust would need a law to break. Force and fraud are called the "
                    "cardinal virtues of war, but not just. And justice, he argues, is no faculty of the mind: "
                    "it would then be found in a man alone in the world."},
        ],
        "mistakes": [
            ("Thinking Hobbes calls men wicked",
             "He says the opposite: &ldquo;The Desires, and other Passions of man, are in themselves no "
             "Sin&rdquo;. In the diffidence table nobody gains from attacking, and attack with attack is still an "
             "equilibrium. In the pair table only one man enjoys conquest, and it is enough."),
            ("Thinking war means constant fighting",
             "War is &ldquo;the known disposition thereto, during all the time there is no assurance to the "
             "contrary&rdquo;. A town where every door is locked and no blow is struck is in the condition he "
             "describes, and the lab's equilibrium is a disposition, never a battle."),
            ("Reading the tables as Hobbes's whole case",
             "The payoffs are the lesson's own choice, two men stand for any number, and glory over a smile has no "
             "number here. The tables show that the argument can be put as incentives. They do not show "
             "that the incentives are as Hobbes says."),
        ],
        "standard": (
            "Finish when you can say what makes the war an equilibrium in each table.",
            "Write competition, diffidence and the mixed pair as two-by-two games, find each equilibrium, state "
            "the chance of the other's peace above which peace is the better reply in the diffidence table, and "
            "say what the tables leave out of the chapter."
        ),
        "note": (
            "The games are played once and by two men, where Hobbes's war lasts over time and is among many. "
            "Glory, the third cause, has no payoff the lab can give it and is left out. And whether men in fact "
            "have the payoffs written in a table, in particular whether one man who enjoys conquest can set off "
            "the others, is the premise that Locke and Rousseau denied and the lab leaves to the reader."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Leviathan ch. 14, 1651 p. 64-66; PDF p. 187-189 of the operator's copy.
    # argkit/validity.
    {
        "slug": "right-and-law-of-nature",
        "title": "The Right and the Law of Nature",
        "module": "Chapter 14 · Of the first and second Naturall Lawes, and of Contracts",
        "one_line": "A right is a liberty and a law is an obligation, and from the first law (seek peace) Hobbes derives the second: lay down your right to all things, when others do too.",
        "summary": (
            "Chapter 14 begins by separating two things that writers confuse, the right of nature, which is a "
            "liberty to use one's own power to preserve one's life, and a law of nature, a rule of reason that "
            "binds. In war every man has a right to everything, even to another's body, so reason forbids what "
            "destroys life and Hobbes derives a first law, to seek peace, and a second, to lay down the right to all "
            "things when others do too. The derivation is written as an argument and checked for validity."
        ),
        "key": [
            "right: liberty to do or to forbear",
            "law: obligation, bound to one of the two",
            "first law: seek peace, else use war",
            "second law: lay down the right, if others do",
            "renouncing or transferring is laying down",
        ],
        "key_label": "Right, law and the second law",
        "concepts_intro": (
            "Chapter 14 opens with definitions and the first of its arguments. The lesson reads them in the order "
            "the chapter gives them."
        ),
        "concepts": [
            ("Right and law differ as liberty and obligation",
             "The right of nature is the liberty each man has to use his own power for the preservation of his "
             "own nature, his life. Liberty is the absence of external impediments. A law of nature is a precept "
             "found out by reason forbidding what destroys life. Right consists in liberty to do or forbear, "
             "law binds to one of them, and in one and the same matter the two are inconsistent."),
            ("The first law",
             "In war every man has a right to everything, even to one another's body, so no man, however strong "
             "or wise, has security. The rule of reason that follows is that every man ought to endeavour peace as "
             "far as he has hope of obtaining it, and when he cannot, may use all the helps and advantages of war. "
             "The first branch is the fundamental law of nature; the second is the sum of the right of nature."),
            ("The second law, and laying down a right",
             "From the first law Hobbes derives a second: that a man be willing, when others are so too, to lay "
             "down his right to all things and be content with as much liberty against others as he would allow "
             "them against himself. A right is laid down by renouncing it or by transferring it, and whoever has "
             "done so is bound not to hinder those who benefit, which Hobbes calls duty, and doing otherwise "
             "injustice."),
        ],
        "read_title": "Right, law, and the derivation of the second law",
        "read_intro": (
            "The lesson starts with the second law, which is the chapter's first conclusion, then goes back "
            "through the definitions it rests on and the argument that gets there."
        ),
        "body": [
            ("p", "<strong>Chapter 14.</strong> &ldquo;From this Fundamentall Law of Nature, by which men are "
                  "commanded to endeavour Peace, is derived this second Law; That a man be willing, when others are "
                  "so too, as farre-forth, as for Peace, and defence of himselfe he shall think it necessary, to lay "
                  "down this right to all things; and be contented with so much liberty against other men, as he "
                  "would allow other men against himselfe.&rdquo;"),
            ("p", "Hobbes has just finished describing the war. Chapter 14 begins with a distinction that his "
                  "readers used carelessly, and it takes up two Latin terms to make it. &ldquo;The Right of "
                  "Nature, which Writers commonly call <em>Jus Naturale</em>, is the Liberty each man hath, to use "
                  "his own power, as he will himselfe, for the preservation of his own Nature&rdquo;, and Hobbes "
                  "adds that this means his own life and &ldquo;doing any thing, which in his own Judgement, and "
                  "Reason, hee shall conceive to be the aptest means thereunto&rdquo;. The right is a "
                  "liberty, and liberty is &ldquo;the absence of externall Impediments&rdquo;, which &ldquo;may oft "
                  "take away part of a mans power&rdquo; but cannot stop him using &ldquo;the power left him&rdquo;."),
            ("p", "Think of an ordinary evening. You are at liberty to go out or stay in, and nobody is bound by "
                  "that to help you either way. A curfew is a different thing: it does not leave you free to do "
                  "either, it binds you to one. That is the contrast Hobbes draws. A law of nature "
                  "is &ldquo;a Precept, or generall Rule, found out by Reason, by which a man is forbidden to do, "
                  "that, which is destructive of his life&rdquo;, and so &ldquo;Law, and Right, differ as much, as "
                  "Obligation, and Liberty; which in one and the same matter are inconsistent&rdquo;. A right does "
                  "not bind any other man to anything. It only says that nobody has taken the liberty away."),
            ("p", "In the war every man is his own judge of what helps him, and so every man has a right to "
                  "everything: &ldquo;even to one anothers body&rdquo;. Hobbes does not say this is a good state. "
                  "He says its consequence is that there &ldquo;can be no security to any man, (how strong or wise "
                  "soever he be,) of living out the time, which Nature ordinarily alloweth men to live&rdquo;, and "
                  "the words are an echo of the last lesson's equality. From that Reason draws a rule in two "
                  "halves, that every man &ldquo;ought to endeavour Peace, as farre as he has hope of obtaining "
                  "it; and when he cannot obtain it, that he may seek, and use, all helps, and advantages of "
                  "Warre&rdquo;. The first half is the fundamental law of nature, &ldquo;to seek Peace, and follow "
                  "it&rdquo;, and the second is &ldquo;the summe of the Right of Nature; which is, By all means we can, "
                  "to defend our selves&rdquo;."),
            ("p", "Now the derivation. While every man holds his right to everything, Hobbes says, &ldquo;so long are all men in the "
                  "condition of Warre&rdquo;. So a man who endeavours peace must be willing to lay his right down. "
                  "But, says Hobbes, &ldquo;if other men will not lay down their Right, as well as he; then there "
                  "is no Reason for any one, to devest himselfe of his: For that were to expose himselfe to Prey, "
                  "(which no man is bound to) rather than to dispose himselfe to Peace&rdquo;. That is why the "
                  "second law has a condition in it, &ldquo;when others are so too&rdquo;, and why the condition is "
                  "part of the law, not an afterthought. Hobbes ties it to two maxims, the Gospel's &ldquo;Whatsoever "
                  "you require that others should do to you, that do ye to them&rdquo;, and the Latin <em>Quod tibi "
                  "fieri non vis, alteri ne feceris</em>, which says the same thing in the negative."),
            ("p", "The lab sets the derivation out as an argument, with the lesson's letters and the lesson's "
                  "reading of Hobbes, not his. Let `h` be that the man has hope of peace, `e` that he endeavours "
                  "peace, `l` that he is willing to lay down his right and `o` that others are willing to lay down "
                  "theirs. The premises are: if others are willing, he has hope (`o -> h`); if he has hope, he "
                  "endeavours peace (`h -> e`, the first law); and if he endeavours peace, he is willing to lay "
                  "down his right (`e -> l`, from the sentence about all men holding the right). The conclusion "
                  "is the second law: if others are willing, he is (`o -> l`). The lab finds it valid in the derivation preset, "
                  "with sixteen rows and no counterexample."),
            ("p", "Take away the first premise, the one that ties hope to the others (the no-link preset), and "
                  "it fails: the others may be willing while he has no hope, and nothing then says he lays down "
                  "his right, so one row refutes it. The unconditional preset puts the conclusion in "
                  "unconditional form, <em>he is willing to lay down his right</em>, and that fails too, because the premises are all "
                  "conditionals and none of them says the others are willing. This is Hobbes's point about "
                  "&ldquo;when others are so too&rdquo; in a table: the law is conditional, because a man in "
                  "war who disarmed alone would be prey. The premise that carries it is the one the lab marks "
                  "first, `o -> h`."),
            ("p", "Having laid down a right, what has happened? &ldquo;To lay downe a mans Right to any thing, is to "
                  "devest himselfe of the Liberty, of hindring another of the benefit of his own Right to the "
                  "same.&rdquo; He gives the other no new right, since before there was &ldquo;nothing to which every "
                  "man had not Right by Nature&rdquo;, and only &ldquo;standeth out of his way&rdquo;. A right is "
                  "laid down by simply renouncing it, &ldquo;when he cares not to whom the benefit thereof "
                  "redoundeth&rdquo;, or by transferring it, &ldquo;when he intendeth the benefit thereof to some "
                  "certain person, or persons&rdquo;. Whoever has done either is &ldquo;Obliged, or Bound, not to "
                  "hinder&rdquo; them, and to hinder is &ldquo;Injustice, and Injury&rdquo;: &ldquo;voluntarily to "
                  "undo that, which from the beginning he had voluntarily done.&rdquo; Hobbes compares it to the "
                  "absurdity of the schools, which is to contradict what one maintained at the beginning."),
            ("p", "Not every right can be laid down, and the exceptions are the heart of what follows. "
                  "First, &ldquo;a man cannot lay down the right of resisting them, that assault him by force, to take away "
                  "his life; because he cannot be understood to ayme thereby, at any Good to himself.&rdquo; The "
                  "same goes for wounds, chains and imprisonment, because the end of laying a right down is "
                  "&ldquo;the security of a mans person, in his life&rdquo;. A man who seems by his words to give "
                  "that up is not to be understood as meaning it, but as ignorant of how his words were to be "
                  "interpreted. And Hobbes says plainly that the "
                  "bonds that hold a man to what he has laid down get their strength not from their own nature, "
                  "&ldquo;for nothing is more easily broken than a mans word&rdquo;, but &ldquo;from Feare of some "
                  "evill consequence upon the rupture&rdquo;. The next two lessons are about exactly that."),
            ("p", "A reader may ask whether a law found out by reason and a right that binds nobody can "
                  "make a duty without a lawgiver. Hobbes raises that himself at the end of Chapter 15, where he "
                  "says the dictates of reason are called laws but &ldquo;improperly&rdquo;, being &ldquo;but "
                  "Conclusions, or Theoremes concerning what conduceth to the conservation and defence "
                  "of themselves&rdquo;, and properly laws only as delivered in the word of God. The last "
                  "lesson of the course reads that passage. For now the lab shows that the second law follows "
                  "from the first and is conditional. It cannot show that reason delivers the first law."),
            ("p", "The next lesson, &ldquo;Contracts and Covenants&rdquo;, follows the second law into practice, "
                  "to the question of what happens when a right is transferred and the other party has not yet "
                  "performed."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "preset": "derivation",
            "show": "all",
            "presets": [
                {"id": "derivation", "label": "If others will, I hope; if I hope, I endeavour; if I endeavour, I lay down; so if others will, I lay down",
                 "premises": ["o -> h", "h -> e", "e -> l"], "conclusion": "o -> l",
                 "expect": {"vaRows": "16", "vaCounter": "0", "vaVerdict": "Valid"}},
                {"id": "no-link", "label": "Without the premise that ties hope to the others",
                 "premises": ["h -> e", "e -> l"], "conclusion": "o -> l",
                 "expect": {"vaRows": "16", "vaCounter": "1", "vaVerdict": "Invalid"}},
                {"id": "unconditional", "label": "The second law with its condition left out",
                 "premises": ["o -> h", "h -> e", "e -> l"], "conclusion": "l",
                 "expect": {"vaRows": "16", "vaCounter": "1", "vaVerdict": "Invalid"}},
            ],
            "panel_title": "The second law as an argument",
            "panel_intro": (
                "h: he has hope of peace; e: he endeavours peace; l: he lays down his right; o: others are willing "
                "to lay down theirs. The lab lists every assignment of true and false and marks the rows that make "
                "every premise true and the conclusion false. Compare the three presets."
            ),
        }),
        "steps_title": "Checking a derivation of a law of nature",
        "steps_intro": "Four steps, the same for any derivation in the chapter.",
        "steps": [
            ("Write each sentence as a conditional",
             "Give each simple sentence a letter and write the rule as if-then. Hobbes's rules are all of the "
             "form: if this, then that is to be done."),
            ("Mark the premise that carries the condition",
             "Find the sentence that makes the conclusion depend on others. In the second law it is the one that "
             "ties hope of peace to the others' willingness."),
            ("List the rows that refute",
             "A row that makes every premise true and the conclusion false is a counterexample. If there is "
             "none, the conclusion follows."),
            ("Say what the check leaves open",
             "Validity shows that the conclusion follows from the premises. Whether reason does deliver the "
             "first law, and whether the premises are true, is the question the chapter argues."),
        ],
        "worked": {
            "title": "The derivation, with and without its first link",
            "intro": [
                "Let `h`, `e`, `l` and `o` be hope, endeavour, laying down, and the others being willing.",
            ],
            "lines": [
                "premises:  o -> h,  h -> e,  e -> l",
                "conclusion:  o -> l  (the second law)",
                "counterexample rows:  none, so valid",
                "drop o -> h:  o true, h false, e false, l false",
                "that row makes h -> e and e -> l true, and o -> l false",
            ],
            "after": [
                "Without the first link the others' willingness never reaches the man's own. The condition is the "
                "work that premise does, and the second law has it written into it as &ldquo;when others are so "
                "too&rdquo;.",
            ],
        },
        "quiz_title": "Right, law and the second law",
        "quiz": [
            {"q": "According to Hobbes, how do right and law differ?",
             "a": ["Law is the greater liberty and right the lesser",
                   "Right is a duty to others and law a duty to oneself",
                   "Right is what the sovereign grants and law is what nature grants",
                   "Right is liberty to do or forbear and law binds to one of them, so they differ as liberty and obligation"],
             "c": 3,
             "why": "&ldquo;RIGHT, consisteth in liberty to do, or to forbeare; Whereas Law, determineth, and bindeth "
                    "to one of them&rdquo;. The other answers reverse or invent the distinction: neither says "
                    "anything about a sovereign, and right in this sense is no duty to anyone."},
            {"q": "In the derivation, which premise carries the words &ldquo;when others are so too&rdquo;?",
             "a": ["If others are willing to lay down their rights, he has hope of peace",
                   "If he has hope of peace, he endeavours peace",
                   "If he endeavours peace, he lays down his right",
                   "He is willing to lay down his right"],
             "c": 0,
             "why": "It is the one that makes hope depend on the others. The other conditionals concern only what "
                    "he does once he hopes, and the last is the unconditional conclusion the lab shows does not "
                    "follow."},
            {"q": "Why does the preset that drops the hope premise fail?",
             "a": ["Because the conclusion is false in the world",
                   "Because the argument has too many premises",
                   "Because there is a row where the others are willing, he has no hope, and he does not lay down his right",
                   "Because laying down a right is impossible"],
             "c": 2,
             "why": "With `o` true and `h`, `e` and `l` all false, both remaining premises are true and the "
                    "conclusion is false. Validity is a matter of that row. The lab says nothing about whether "
                    "the conclusion is false in the world."},
            {"q": "Which of these rights does Hobbes say a man cannot lay down?",
             "a": ["The right to everything",
                   "The right of resisting those who assault him by force to take away his life",
                   "The right to the use of his own land",
                   "The right to speak"],
             "c": 1,
             "why": "Hobbes says &ldquo;a man cannot lay down the right of resisting them, that assault him by force, to take "
                    "away his life&rdquo;, since laying a right down is only for some good to himself. The right to "
                    "everything is exactly the one the second law asks him to lay down."},
        ],
        "mistakes": [
            ("Taking a right to everything for a licence",
             "A right in Hobbes's sense is a liberty and binds no one. That every man has it is the reason there "
             "is no security. He calls it a consequence of the war, not a thing to be proud of."),
            ("Dropping the condition from the second law",
             "The law is &ldquo;when others are so too&rdquo;. A man who laid down his right alone would "
             "&ldquo;expose himselfe to Prey&rdquo;, which Hobbes says no man is bound to. In the third preset the "
             "unconditional conclusion is the one that fails."),
            ("Thinking the lab proves the laws of nature",
             "A valid argument shows that the conclusion follows. It says nothing about whether reason delivers "
             "the first law, and the letters are the lesson's reading of Hobbes, not his own."),
        ],
        "standard": (
            "Finish when you can show the second law follows from the first and say what carries its condition.",
            "Write the derivation of the second law as three conditionals and a conclusion, check it for validity, "
            "name the premise that carries &ldquo;when others are so too&rdquo;, and show what happens to the "
            "argument without it."
        ),
        "note": (
            "The lab checks a classical argument whose letters and premises are the lesson's reading of Hobbes "
            "and may not be the only fair one. It cannot say whether reason really yields a duty to seek peace, "
            "or whether a rule with no lawgiver behind it is a law, which Hobbes himself calls improper in the "
            "last paragraph of Chapter 15."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Leviathan ch. 14, 1651 p. 66-68; PDF p. 190-192 of the operator's copy.
    # LEVKIT: covenant / perform.
    {
        "slug": "contracts-and-covenants",
        "title": "Contracts and Covenants",
        "module": "Chapter 14 · Of the first and second Naturall Lawes, and of Contracts",
        "one_line": "A contract is a mutual transfer of right, a covenant is a contract in which one side is trusted to perform later, and the one who performs first merits what he is to receive.",
        "summary": (
            "Hobbes separates transferring a right from delivering the thing, calls the mutual transfer of right a "
            "contract and a contract with one side still to perform a covenant or pact, and separates both from "
            "free gift, in which nothing is exchanged. Words of the present transfer a right, bare words of the "
            "future do not, and the one who performs first merits what the other is to give. A covenant in which "
            "the buyer must pay later is worked as a payoff problem: what each side gets by keeping and by "
            "breaking, and whether the one who must go first has reason to."
        ),
        "key": [
            "contract: right passes both ways",
            "covenant: one side performs, one is trusted",
            "gift passes by words of the present",
            "first to perform merits, has it as due",
            "break pays when keeping costs something",
        ],
        "key_label": "Contract, covenant, gift and merit",
        "concepts_intro": (
            "The pages that follow the second law are definitions. They matter because the next lesson's argument "
            "about trust depends on exactly where each one draws its line."
        ),
        "concepts": [
            ("Contract and covenant",
             "The mutual transferring of right is a contract. The right to a thing is one matter and delivery "
             "of the thing another: one party may deliver and leave the other to perform later and be trusted, and "
             "the contract on his part is then a pact or covenant. The trusted party's performance is keeping "
             "faith, and his voluntary failure is violation of faith."),
            ("Free gift and its signs",
             "When the transfer is not mutual, and a man gives in hope of friendship, service, a name for charity, "
             "relief from the pain of compassion or reward in heaven, it is not contract but free gift or grace. "
             "Words of the present or past transfer a right; bare words of the future do not, unless there are "
             "other signs of will. In a contract a promise is equivalent to a covenant."),
            ("Merit",
             "He that performs first in a contract merits what he is to receive by the other's performance, and has "
             "it as due. A prize propounded to many is a free gift, but the winner merits it and may claim it "
             "as due. In contract the merit lies in one's own power and the contractor's need, and in gift in the "
             "giver's benignity."),
        ],
        "read_title": "The passage first, then the definitions in order",
        "read_intro": (
            "The lesson reads the definition of a covenant first, since the next lesson turns on it, then goes "
            "back to contract, gift, signs and merit."
        ),
        "body": [
            ("p", "<strong>Chapter 14.</strong> &ldquo;Again, one of the Contractors, may deliver the Thing contracted "
                  "for on his part, and leave the other to performe his part at some determinate time after, and in "
                  "the mean time be trusted; and then the Contract on his part, is called Pact, or Covenant: Or both "
                  "parts may contract now, to performe hereafter: in which cases, he that is to performe in time to "
                  "come, being trusted, his performance is called Keeping of Promise, or Faith; and the fayling of "
                  "performance (if it be voluntary) Violation of Faith.&rdquo;"),
            ("p", "Think of buying a concert ticket months ahead, or paying a deposit on a room. You hand over your "
                  "money now, and the other party's side of the bargain is still to come. You are being trusted "
                  "less than you are trusting, and you know it: it is the position the chapter is about. Hobbes "
                  "begins one step earlier. &ldquo;The mutuall transferring of Right, is that which men call "
                  "Contract.&rdquo; And a contract can be done with two different time-tables, since there is a "
                  "&ldquo;difference, between transferring of Right to the Thing; and transferring, or tradition, "
                  "that is, delivery of the Thing it selfe&rdquo;. The right can pass in the same moment as the thing, as "
                  "&ldquo;in buying and selling with ready mony&rdquo;, or the thing may be delivered &ldquo;some time "
                  "after&rdquo;. So the passage above is about a contract with a gap in it, and the gap is where "
                  "the trouble will be."),
            ("p", "The second half of the definition names the person in the gap. Whoever has "
                  "&ldquo;to performe in time to come&rdquo; is being trusted, and his performance is "
                  "&ldquo;Keeping of Promise, or Faith&rdquo;. Notice the parenthesis: failing is violation of "
                  "faith only &ldquo;if it be voluntary&rdquo;."),
            ("p", "Then the contrast. When the transferring is not mutual, &ldquo;but one of the parties "
                  "transferreth, in hope to gain thereby friendship, or service from another, or from his friends; "
                  "or in hope to gain the reputation of Charity, or Magnanimity; or to deliver his mind from the "
                  "pain of compassion; or in hope of reward in heaven&rdquo;, this is &ldquo;not Contract, but "
                  "Gift, Free-Gift, Grace&rdquo;. It is a list with a dry edge: every motive on it is some good to the "
                  "giver, from a friend's service to relief from the pain of compassion to a reward in heaven."),
            ("p", "The signs matter because a right passes by what the giver signifies. &ldquo;Signes of Contract, "
                  "are either Expresse, or by Inference&rdquo;: express signs are words of the present or past "
                  "(&ldquo;I Give, I Grant, I have Given, I have Granted, I will that this be yours&rdquo;), and "
                  "words of the future are promises. By inference a sign can be words, silence, actions or "
                  "forbearing, and &ldquo;generally a signe by Inference, of any Contract, is whatsoever "
                  "sufficiently argues the will of the Contractor&rdquo;. Bare words of the future in a free gift "
                  "fail to transfer anything: &ldquo;To morrow I will Give&rdquo; is &ldquo;a signe I have not "
                  "given yet, and consequently that my right is not transferred&rdquo;. Whereas words of the "
                  "present, &ldquo;I have given, or do give to be delivered to morrow&rdquo;, give away "
                  "tomorrow's right today. He puts the Latin side by side to make it visible: <em>Volo hoc tuum "
                  "esse cras</em>, I will that this be thine tomorrow, transfers, and <em>Cras dabo</em>, I will "
                  "give it thee tomorrow, does not."),
            ("p", "There are two exceptions. If there are other signs of a will to transfer, the right may pass by "
                  "words of the future even in a free gift: the man who offers a prize to the first to finish "
                  "a race has given it, &ldquo;for if he would not have his words so understood, he should not have "
                  "let them runne&rdquo;. And in a contract the rule is reversed. A promise is as binding as a "
                  "covenant, because the man who promises only after he has received the benefit must be "
                  "understood as intending the right to pass, since &ldquo;unlesse he had been content to have his "
                  "words so understood, the other would not have performed his part first&rdquo;."),
            ("p", "Last, merit. &ldquo;He that performeth first in the case of a Contract, is said to Merit that "
                  "which he is to receive by the performance of the other; and he hath it as Due.&rdquo; The prize "
                  "is also merited by the one who wins it, though it is a free gift, and the right passed when it "
                  "was propounded. Hobbes then marks the difference: &ldquo;In Contract, I Merit by vertue of my own "
                  "power, and the Contractors need&rdquo;; in the gift, only &ldquo;by the benignity of the "
                  "Giver&rdquo;. He gives his reading of the schools' distinction between merit <em>ex congruo</em> "
                  "and <em>ex condigno</em>, and then declines to affirm what they meant, since "
                  "&ldquo;Disputers do not agree upon the signification of their own termes of Art, longer than it "
                  "serves their turn&rdquo;."),
            ("p", "The lab takes the performer who goes first and asks what a covenant is worth to him. Three "
                  "covenants of the lesson's own, with plain figures: a sale, in which a seller delivers grain "
                  "now and the buyer is to pay later; a hire, in which a worker labours now and the master is "
                  "to pay later; and a loan, in which a lender hands over money now and the borrower is to repay. "
                  "In the sale the seller gives up grain that is worth `5` to him and gets `8` if he is paid. The "
                  "buyer values the grain at `9` and pays `8`, so if he keeps the covenant he is ahead by `1`. If "
                  "he breaks it he is ahead by `9`, since he has the grain and has paid nothing, and in the "
                  "lab there is no sanction here. Breaking pays more than keeping, so the seller, who performs "
                  "first, is left with `−5`, where not performing leaves him with `0`. The lab says he is not "
                  "reasonable to go first. The hire and the loan have the same shape. In the hire preset the master "
                  "values the labour at `12` and owes `9`, so keeping pays him `3` and breaking `12`, and the worker "
                  "who laboured first is left with `−6`. In the loan preset the borrower has `14` of use from the "
                  "money and owes `11`, so keeping pays him `3` and breaking `14`, and the lender who handed it "
                  "over is left with `−10`."),
            ("p", "That is a result about the incentives of a man who counts only his own gain. What Hobbes "
                  "does with it, in the section the next lesson reads, is to say that in the condition of mere "
                  "nature such a covenant is void on reasonable suspicion, and valid when there is a common power. "
                  "What the lab leaves out is the generosity he mentions later and calls too rare to presume "
                  "on, and the time that lets a man's future dealings depend on his word. Both come back, and "
                  "the lab at the end of this course puts the second one in."),
            ("p", "The next lesson, &ldquo;Covenants Made Void and Kept&rdquo;, reads the page of Chapter 14 "
                  "where Hobbes says when a covenant of mutual trust is void, and what a sword does to the "
                  "payoffs."),
        ],
        # LEVKIT: cfg drafted from PLAN D.1; corrected against kit-report.md in phase B.
        "lab": ("levkit", {
            "mode": "covenant",
            "view": "perform",
            "preset": "sale",
            "presets": [
                {"id": "sale", "label": "A sale: the seller delivers grain first, the buyer pays later",
                 "first": "seller", "second": "buyer",
                 "cost1": 5, "gain1": 8, "cost2": 8, "gain2": 9, "sanction": 0, "certainty": 1,
                 "expect": {"lcvKeep": "1", "lcvBreak": "9", "lcvChoice": "buyer breaks: 9 against 1", "lcvFirst": "−5, since buyer breaks", "lcvReasonable": "no: −5 against 0 for not performing", "lcvLeast": "8 (cost2 ÷ certainty)"}},
                {"id": "hire", "label": "A hire: the worker labours first, the master pays later",
                 "first": "worker", "second": "master",
                 "cost1": 6, "gain1": 9, "cost2": 9, "gain2": 12, "sanction": 0, "certainty": 1,
                 "expect": {"lcvKeep": "3", "lcvBreak": "12", "lcvChoice": "master breaks: 12 against 3", "lcvFirst": "−6, since master breaks"}},
                {"id": "loan", "label": "A loan: the lender hands over money first, the borrower repays",
                 "first": "lender", "second": "borrower",
                 "cost1": 10, "gain1": 11, "cost2": 11, "gain2": 14, "sanction": 0, "certainty": 1,
                 "expect": {"lcvKeep": "3", "lcvBreak": "14", "lcvChoice": "borrower breaks: 14 against 3", "lcvFirst": "−10, since borrower breaks"}},
            ],
            "panel_title": "What the second party gains by keeping and by breaking",
            "panel_intro": (
                "The first party performs, the second is to perform later. The lab computes the second's gain "
                "from keeping and from breaking, whether the second does better to keep, and what the first "
                "gets by going first. There is no sanction here."
            ),
        }),
        "steps_title": "Working out a covenant between two parties",
        "steps_intro": "Four steps, the same for a sale, a hire or a loan.",
        "steps": [
            ("Name who performs first",
             "The first party delivers or labours or lends now. The second is to perform later and is "
             "trusted in the meantime."),
            ("Write what each side gets and gives up",
             "For the first: what performing costs him and what he gets if the second keeps faith. For the "
             "second: what the first's performance is worth to him and what keeping costs him."),
            ("Compare the second party's two choices",
             "If he keeps, he has what he got less what he gave. If he breaks, he has what he got, and "
             "nothing else is taken from him while there is no sanction."),
            ("Decide what the first party does",
             "If the second does better to break, the first who performs gets only his loss. If not "
             "performing leaves him with nothing, he does better not to go first."),
        ],
        "worked": {
            "title": "The seller who goes first",
            "intro": [
                "A seller gives up grain worth `5` to him and is to be paid `8`. The buyer values the grain at "
                "`9`. No sanction.",
            ],
            "lines": [
                "buyer keeps:  9 − 8 = 1",
                "buyer breaks:  9 − 0 = 9",
                "breaking is better by  9 − 1 = 8",
                "seller performs first and buyer breaks:  −5",
                "seller does not perform:  0",
            ],
            "after": [
                "The `8` by which breaking beats keeping is the price the buyer saves, and it is also the "
                "smallest sanction that would make the buyer indifferent, the figure the next lesson finds. "
                "Until something takes it from him, the seller's best choice is not to go first.",
            ],
        },
        "quiz_title": "Contract, covenant and gift",
        "quiz": [
            {"q": "Which of these words, standing alone in a free gift, transfers the right at once?",
             "a": ["I will give it thee tomorrow",
                   "Tomorrow I may give it",
                   "I will that this be thine tomorrow",
                   "I intend to give it to you someday"],
             "c": 2,
             "why": "Words of the present will, like <em>Volo hoc tuum esse cras</em>, transfer a future right. "
                    "<em>Cras dabo</em>, I will give it thee tomorrow, is a promise of an act of will to come and "
                    "&ldquo;transferre nothing&rdquo;, where there are no other signs. The other two are weaker "
                    "still."},
            {"q": "Which is a covenant, in Hobbes's sense?",
             "a": ["A sale paid for in ready money",
                   "A contract in which one party has delivered and the other is to perform later, in the meantime trusted",
                   "A gift made in hope of friendship",
                   "A promise made to a beast"],
             "c": 1,
             "why": "A covenant or pact is a contract on the part of the one who has delivered when the other is "
                    "trusted to perform at a time after. A sale in ready money has no gap, the gift is no contract "
                    "since nothing is received, and a promise to a beast is no covenant at all because a beast "
                    "does not understand or accept a transfer of right."},
            {"q": "In the sale preset, what does the buyer gain by breaking the covenant rather than keeping it, "
                  "with no sanction?",
             "a": ["Nothing, because he must still pay later",
                   "5 more, because the seller loses 5",
                   "1 more, because keeping already pays him 1",
                   "8 more, because he keeps the grain and does not pay the price"],
             "c": 3,
             "why": "Keeping pays him `9 − 8 = 1` and breaking pays him `9`, so breaking is better by `8`, the price "
                    "he does not pay. The seller's loss does not enter the buyer's payoff."},
            {"q": "What does Hobbes say the one who performs first in a contract merits?",
             "a": ["That which he is to receive by the other's performance, as his due",
                   "Whatever the other chooses to give him as a favour",
                   "A reward from the commonwealth",
                   "Nothing, since the other has not yet performed"],
             "c": 0,
             "why": "&ldquo;He that performeth first in the case of a Contract, is said to Merit that which he is to "
                    "receive by the performance of the other; and he hath it as Due.&rdquo; Merit by favour is the "
                    "other kind, which belongs to a free gift."},
        ],
        "mistakes": [
            ("Treating a promise as a transfer",
             "Words of the future alone, in a free gift, transfer nothing: <em>Cras dabo</em> is only a promise. "
             "The right passes by words of the present, or by other signs of will, or because the one who "
             "promises has already received the benefit."),
            ("Thinking a covenant needs both sides to deliver at once",
             "That is a contract with ready money. A covenant is a contract with a gap in it, in which one "
             "party has delivered and is trusting the other, and the whole of the next lesson is about the gap."),
            ("Reading the lab as saying covenants never bind",
             "The lab computes what a second party gains by keeping and by breaking when nothing is taken from "
             "him. Whether the covenant binds him is what Hobbes decides in the pages the next lesson reads, "
             "where the answer depends on whether there is a common power."),
        ],
        "standard": (
            "Finish when you can say what a covenant is and work out whether the one who goes first has reason to.",
            "Given what each party gives up and gets in a covenant with no sanction, compute the second party's "
            "gain from keeping and from breaking, say which is better for him, and say what the first party "
            "gets by performing first."
        ),
        "note": (
            "The lab's second party counts only his own gain and looks only at this one covenant. Hobbes "
            "allows two things that can hold a man to his word besides fear, glory in not needing to break it "
            "and the fear of what unseen powers will do, and the figures here include neither. The three "
            "covenants are the lesson's examples and no numbers are Hobbes's."
        ),
    },
]
