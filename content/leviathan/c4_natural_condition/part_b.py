"""The Natural Condition and the Laws of Nature, lessons 5-7 -- Chapter 14 from mutual trust, and Chapter 15.

Every quotation is from the text of 1651 as the operator's copy prints it, in its
original spelling; the comment beside each lesson gives the chapter, the 1651 page
(Tuck prints it in the margin in square brackets) and the PDF page of the copy.
Italics are dropped, a long s is printed as s, and nothing else is changed.

The two lessons whose lab is `levkit` (covenants-and-the-sword, justice-and-the-fool)
are marked LEVKIT: their cfg is drafted from docs/leviathan/PLAN.md section D.1 and
is corrected against docs/leviathan/kit-report.md once the kit is registered.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    # Leviathan ch. 14, 1651 p. 68-71; PDF p. 192-195 of the operator's copy.
    # LEVKIT: covenant / perform, with a sanction.
    {
        "slug": "covenants-and-the-sword",
        "title": "Covenants Made Void and Kept",
        "module": "Chapter 14 · Of the first and second Naturall Lawes, and of Contracts",
        "one_line": "In mere nature a covenant of trust is void on reasonable suspicion, under a power that can compel performance it holds, and what can strengthen a promise besides is fear, or an oath that adds fear.",
        "summary": (
            "A covenant in which one side must perform first is void, Hobbes says, on any reasonable suspicion in "
            "the condition of mere nature, and not void where a common power can compel performance. Covenants "
            "extorted by fear still bind; a covenant not to defend oneself never does. Words are too weak to hold "
            "men, and the helps are fear of the consequence, or glory in not needing to break one's word, which is "
            "too rare to count on. The sale of the last lesson is run again with a sanction applied with a stated "
            "chance, to find the least sanction that makes keeping the better choice."
        ),
        "key": [
            "no sword: first performer betrays himself",
            "sword sufficient to compel: covenant stands",
            "fear's extortion does not void a covenant",
            "no covenant not to defend one's life",
            "least sanction = cost of keeping / chance",
        ],
        "key_label": "When a covenant is void and when it holds",
        "concepts_intro": (
            "Hobbes's pages on covenants divide into the rule, the cases it leaves alone, and what can hold a man "
            "when no one can compel him."
        ),
        "concepts": [
            ("Void in mere nature, valid under a sword",
             "A covenant of mutual trust made in the condition of mere nature is void upon any reasonable "
             "suspicion, since the bonds of words are too weak to bridle the passions without fear of a coercive "
             "power. Where a common power with right and force enough to compel performance is set over both, "
             "it is not void, and he who is to perform first is obliged to."),
            ("Fear does not void a covenant, nor can a man covenant away his life",
             "A covenant entered into by fear in mere nature is obligatory: a prisoner released on trust is bound "
             "to pay his ransom. But a covenant not to defend oneself by force against force is always void, "
             "because no man can lay down the right to save himself from death, wounds and imprisonment."),
            ("What can hold a man to his word",
             "Words alone are too weak. The two imaginable helps are fear of the consequence of breaking one's "
             "word, and glory or pride in appearing not to need to break it, which is too rarely found to be "
             "presumed on. Where there is no civil power the fear is of invisible spirits, and the oath, a form of "
             "words added to a promise, calls that fear in. It adds nothing to the obligation."),
        ],
        "read_title": "The rule first, then the cases and the helps",
        "read_intro": (
            "The passage is the rule. The lesson reads it, then goes through Hobbes's reasons, the qualification "
            "he adds, the cases that look like exceptions and what he says can hold a promise when no one else will."
        ),
        "body": [
            ("p", "<strong>Chapter 14.</strong> &ldquo;If a Covenant be made, wherein neither of the parties "
                  "performe presently, but trust one another; in the condition of meer Nature, (which is a condition "
                  "of Warre of every man against every man,) upon any reasonable suspition, it is Voyd: But if there "
                  "be a common Power set over them both, with right and force sufficient to compell performance; it "
                  "is not Voyd.&rdquo;"),
            ("p", "This is a sentence about promises that carries a great deal of the book's argument. Take the sale of the last lesson, in which a seller delivers grain and trusts the "
                  "buyer to pay. Hobbes states the rule for a covenant in which neither party has yet performed, and "
                  "his reason is about the one who must go first, which is the case the lab takes. The reason, in the next "
                  "lines: &ldquo;he that performeth first, has no assurance the other will performe after; because "
                  "the bonds of words are too weak to bridle mens ambition, avarice, anger, and other Passions, "
                  "without the feare of some coércive Power&rdquo;, and in mere nature such a power &ldquo;cannot "
                  "possibly be supposed&rdquo;, since there &ldquo;all men are equall, and judges of the justnesse "
                  "of their own fears&rdquo;. The equality of Chapter 13 comes back: nobody there is strong "
                  "enough to be trusted to enforce. So the man who performs first &ldquo;does but betray himselfe "
                  "to his enemy; contrary to the Right (he can never abandon) of defending his life&rdquo;."),
            ("p", "The lab runs the sale again with the numbers of the last lesson: the seller gives up grain "
                  "worth `5` to him, expects `8`, and the buyer values the grain at `9` and owes `8`. In the "
                  "none preset there is no sanction, and the buyer is `1` ahead by keeping and `9` ahead by "
                  "breaking, so he breaks, and the seller who goes first is left with `−5`. That is the reasoning "
                  "Hobbes calls reasonable suspicion, written as a sum."),
            ("p", "Now a sword. &ldquo;But in a civill estate, where there is a Power set up to constrain those that "
                  "would otherwise violate their faith, that feare is no more reasonable; and for that cause, he "
                  "which by the Covenant is to perform first, is obliged so to do.&rdquo; Add to the buyer's "
                  "breaking a penalty that is certain to fall. In the sword preset it is `9`, and breaking now "
                  "pays `9 − 9 = 0`, which is less than `1`, so the buyer keeps and the seller who goes first "
                  "gains `3`. The tie preset gives the smallest sanction that works, `8`, which is the whole price "
                  "the buyer saves: breaking then pays `1`, as keeping does, and the lab's rule for a tie is that "
                  "the buyer keeps. A sword is not enough because it is large. If it falls only half the time, "
                  "as in the misses preset, a penalty of `9` is expected to cost `9/2`, breaking pays `9/2`, "
                  "which is more than `1`, and the buyer breaks again. At half the certainty the least sanction "
                  "that works is not `8` but `16`. Hobbes asks for &ldquo;right and force sufficient to compell "
                  "performance&rdquo;; the lab adds that force which sometimes misses counts for less."),
            ("p", "Hobbes qualifies the rule with a sentence that is easy to skip. &ldquo;The cause of feare, "
                  "which maketh such a Covenant invalid, must be alwayes something arising after the Covenant "
                  "made; as some new fact, or other signe of the Will not to performe: else it cannot make the "
                  "Covenant voyd. For that which could not hinder a man from promising, ought not to be admitted "
                  "as a hindrance of performing.&rdquo; So being in the war is not enough on its own to void "
                  "a covenant of trust that was made knowingly: something must have changed since. How this "
                  "fits with the first statement, which voids a covenant in mere nature on &ldquo;any reasonable "
                  "suspition&rdquo;, the lesson does not settle. The lab shows only why the suspicion is reasonable "
                  "in the abstract, and cannot tell a new sign from an old fear."),
            ("p", "A reader will think a promise extorted by fear must be void. Hobbes says the opposite. "
                  "&ldquo;Covenants entred into by fear, in the condition of meer Nature, are obligatory.&rdquo; "
                  "If I covenant to pay a ransom for my life, I am bound, for it is a contract in which one "
                  "receives the benefit of life and the other is to receive money; prisoners of war trusted with "
                  "their ransom are obliged to pay it; and a weaker prince who makes a disadvantageous peace with "
                  "a stronger, for fear, is bound to keep it, unless some new and just cause of fear arises. Even "
                  "in a commonwealth, a man who has promised a thief money to be let go is bound to pay "
                  "&ldquo;till the Civill Law discharge me&rdquo;. His reason: &ldquo;whatsoever I may lawfully "
                  "do without Obligation, the same I may lawfully Covenant to do through feare: and what I "
                  "lawfully Covenant, I cannot lawfully break.&rdquo; A reader in 1651 who had been asked to promise "
                  "loyalty to a government he had not chosen had reason to ask what such a promise was worth, and "
                  "could read this page as about promises of exactly that kind. Notice that the lab does not agree or disagree: "
                  "the ransomed prisoner has the same incentive to break as the buyer, and Hobbes is saying that "
                  "it is a different question whether he may."),
            ("p", "Other covenants are void whatever the circumstances. &ldquo;A Covenant not to defend my selfe "
                  "from force, by force, is alwayes voyd&rdquo;, since no man can lay down the right to save himself "
                  "from death, wounds and imprisonment, which the last lesson found the end of laying down any "
                  "right. The distinction is fine and Hobbes draws it exactly: a man may covenant &ldquo;Unlesse I "
                  "do so, or so, kill me&rdquo;, but not &ldquo;Unlesse I do so, or so, I will not resist you, when "
                  "you come to kill me&rdquo;, because &ldquo;man by nature chooseth the lesser evill, which is "
                  "danger of death in resisting; rather than the greater, which is certain and present death in "
                  "not resisting&rdquo;. Criminals are led to execution by armed men although they consented to "
                  "the law that condemns them. A covenant to accuse oneself without assurance of pardon is void "
                  "for the same reason, and so are a later covenant that contradicts an earlier one, a "
                  "covenant with a beast, which cannot understand or accept a transfer of right, and a vow "
                  "contrary to a law of nature."),
            ("p", "What, then, can hold a man when no one can compel him? &ldquo;The force of Words, being (as I "
                  "have formerly noted) too weak to hold men to the performance of their Covenants; there are in "
                  "mans nature, but two imaginable helps to strengthen it. And those are either a Feare of the "
                  "consequence of breaking their word; or a Glory, or Pride in appearing not to need to breake "
                  "it.&rdquo; The second, he says, &ldquo;is a Generosity too rarely found to be presumed "
                  "on&rdquo;, and concludes: &ldquo;The Passion to be reckoned upon, is Fear&rdquo;. The fear is of two "
                  "things: invisible powers, or the men a man would offend. Of these the first is the greater "
                  "power, but the fear of the second is commonly the greater fear, and it has no place before "
                  "civil society because &ldquo;the inequality of Power is not discerned, but by the event of "
                  "Battell&rdquo;. All that can be done between two men not subject to a civil power is to put one "
                  "another to swear by the god he fears."),
            ("p", "The oath is &ldquo;a Forme of Speech, added to a Promise&rdquo;, by which the swearer means that "
                  "unless he performs, &ldquo;he renounceth the mercy of his God, or calleth to him for vengeance "
                  "on himselfe&rdquo;, as in the heathen form, &ldquo;Let Jupiter kill me else, as I kill this "
                  "Beast&rdquo;. It must be by the swearer's own god and rite, or it is no oath, and it &ldquo;addes "
                  "nothing to the Obligation&rdquo;, since a lawful covenant binds in the sight of God without it. "
                  "What it adds is fear, and a fear is a sanction with a certainty that depends on how firmly he "
                  "believes it. In the oath preset a man who thinks the penalty is `20` and as likely as not "
                  "has an expected cost of `10`, which exceeds the `8` he saves, so breaking pays `−1` against "
                  "keeping's `1` and he keeps. Hobbes gives no numbers, and the lab's are the lesson's, but the "
                  "arithmetic shows how the oath works on a man's reckoning and why it would fail one who "
                  "believed less."),
            ("p", "The next lesson, &ldquo;Justice and the Fool&rdquo;, reads the chapter that follows, in "
                  "which Hobbes turns these results into a third law and answers a man who says there is no "
                  "such thing as justice."),
        ],
        # LEVKIT: cfg drafted from PLAN D.1; corrected against kit-report.md in phase B.
        "lab": ("levkit", {
            "mode": "covenant",
            "view": "perform",
            "preset": "none",
            "presets": [
                {"id": "none", "label": "No sword: the sale of the last lesson",
                 "first": "seller", "second": "buyer",
                 "cost1": 5, "gain1": 8, "cost2": 8, "gain2": 9, "sanction": 0, "certainty": 1,
                 "expect": {"lcvKeep": "1", "lcvBreak": "9", "lcvChoice": "buyer breaks: 9 against 1", "lcvFirst": "−5, since buyer breaks", "lcvLeast": "8 (cost2 ÷ certainty)"}},
                {"id": "tie", "label": "A sanction of 8, certain",
                 "first": "seller", "second": "buyer",
                 "cost1": 5, "gain1": 8, "cost2": 8, "gain2": 9, "sanction": 8, "certainty": 1,
                 "expect": {"lcvKeep": "1", "lcvBreak": "1", "lcvChoice": "buyer keeps: 1 against 1 (equal; the tie rule keeps)", "lcvFirst": "3, since buyer keeps"}},
                {"id": "sword", "label": "A sanction of 9, certain",
                 "first": "seller", "second": "buyer",
                 "cost1": 5, "gain1": 8, "cost2": 8, "gain2": 9, "sanction": 9, "certainty": 1,
                 "expect": {"lcvKeep": "1", "lcvBreak": "0", "lcvChoice": "buyer keeps: 1 against 0", "lcvFirst": "3, since buyer keeps", "lcvReasonable": "yes: 3 against 0 for not performing"}},
                {"id": "misses", "label": "A sanction of 9, applied half the time",
                 "first": "seller", "second": "buyer",
                 "cost1": 5, "gain1": 8, "cost2": 8, "gain2": 9, "sanction": 9, "certainty": "1/2",
                 "expect": {"lcvBreak": "9/2 = 4.50", "lcvChoice": "buyer breaks: 9/2 = 4.50 against 1", "lcvLeast": "16 (cost2 ÷ certainty)"}},
                {"id": "oath", "label": "An oath: a penalty of 20 the swearer thinks as likely as not",
                 "first": "seller", "second": "buyer",
                 "cost1": 5, "gain1": 8, "cost2": 8, "gain2": 9, "sanction": 20, "certainty": "1/2",
                 "expect": {"lcvExpected": "10", "lcvBreak": "−1", "lcvChoice": "buyer keeps: 1 against −1"}},
            ],
            "panel_title": "What a sanction does to the buyer's choice",
            "panel_intro": (
                "The sale of the last lesson, with a penalty for breaking and the chance the penalty is "
                "applied. The lab gives the buyer's payoff from keeping and from breaking, whether he keeps, "
                "what the seller gets by going first, and the least sanction that would make keeping at least "
                "as good. Start with none, then raise the sanction."
            ),
        }),
        "steps_title": "Finding what makes a covenant safe to perform first",
        "steps_intro": "Four steps, for any covenant with a sanction.",
        "steps": [
            ("Write the second party's payoff from keeping",
             "It is what he gets from the first party's performance less what keeping costs him."),
            ("Write his payoff from breaking",
             "It is what he gets from the first party's performance, less the sanction multiplied by the chance "
             "it is applied."),
            ("Compare, and apply the tie rule",
             "He keeps when keeping pays at least as much. State the rule for a tie, since the lab's depends on "
             "a choice made in advance."),
            ("Find the least sanction",
             "It is what keeping costs him divided by the chance of the sanction. If the chance is zero no "
             "sanction is enough."),
        ],
        "worked": {
            "title": "A penalty of nine that falls half the time",
            "intro": [
                "The seller gives up grain worth `5` and expects `8`. The buyer values the grain at `9` and owes "
                "`8`. A penalty of `9` is applied with chance `1/2`.",
            ],
            "lines": [
                "buyer keeps:  9 − 8 = 1",
                "buyer breaks:  9 − (1/2) · 9 = 9/2",
                "9/2 is more than 1:  the buyer breaks",
                "least sanction:  8 / (1/2) = 16",
                "check at 16:  9 − (1/2) · 16 = 1, equal to keeping",
            ],
            "after": [
                "Halving the chance doubles the sanction needed, from `8` to `16`. A power that is large and "
                "usually absent does less than a small one that is always there.",
            ],
        },
        "quiz_title": "Void, valid and sanctioned",
        "quiz": [
            {"q": "On Hobbes's account, what is true of a prisoner of war who has been released on trust to pay his "
                  "ransom?",
             "a": ["He is bound to pay it, though it was made through fear",
                   "He is free of it, because a promise made through fear is void",
                   "He is bound only if he swore an oath",
                   "He is free of it, because there was no common power to enforce it"],
             "c": 0,
             "why": "&ldquo;Prisoners of warre, if trusted with the payment of their Ransome, are obliged to pay "
                    "it&rdquo;. A covenant entered into by fear in mere nature is obligatory, and an oath adds nothing "
                    "to the obligation of a lawful one. The lack of a common power voids covenants of mutual trust "
                    "on suspicion, and Hobbes does not treat this one so."},
            {"q": "In the sale numbers (the buyer values the grain at 9 and owes 8), a sanction is applied with "
                  "chance 1/2. What is the least sanction that makes keeping at least as good as breaking?",
             "a": ["8", "9", "16", "4"],
             "c": 2,
             "why": "Keeping pays `1` and breaking pays `9 − (1/2)·s`. They are equal when `(1/2)·s = 8`, so `s = 16`. "
                    "A sanction of `8` is enough only if certain, and at chance `1/2` it is expected to cost "
                    "`4`. The preset's `9` costs `9/2` in expectation, too little."},
            {"q": "Which covenant does Hobbes say is always void?",
             "a": ["A covenant to pay a ransom for one's life",
                   "A promise of money to a thief to be let go",
                   "A covenant by a weaker prince to keep a disadvantageous peace",
                   "A covenant not to resist, when he comes to kill me"],
             "c": 3,
             "why": "&ldquo;A Covenant not to defend my selfe from force, by force, is alwayes voyd.&rdquo; The "
                    "other three are covenants Hobbes says bind, even though they were made through fear."},
            {"q": "What does Hobbes say an oath adds to a lawful covenant?",
             "a": ["A new obligation the covenant did not have",
                   "Nothing to the obligation, though it adds fear of the swearer's god",
                   "The right to enforce it by force",
                   "A guarantee that the other party will perform first"],
             "c": 1,
             "why": "Hobbes writes that &ldquo;the Oath addes nothing to the Obligation.&rdquo; A lawful covenant binds in the sight of "
                    "God without it. What the oath adds is the fear that the swearer calls on himself."},
        ],
        "mistakes": [
            ("Thinking a covenant extorted by fear is void",
             "Hobbes says the opposite for the condition of mere nature: such covenants are obligatory, and he "
             "gives the ransom, the weaker prince's peace and the thief. What is void on reasonable suspicion is "
             "a covenant of mutual trust, in which one side must perform first and has no assurance."),
            ("Thinking any sword makes a covenant safe",
             "The lab's sanction counts only as its chance multiplied by its size. A penalty of `9` that "
             "falls half the time costs the buyer less than the `8` he saves, so he breaks. Hobbes asks for "
             "a power with &ldquo;right and force sufficient to compell performance&rdquo;."),
            ("Reading the lab's keep and break as what Hobbes says a man ought to do",
             "The lab says what pays. Hobbes's discussion of validity says what binds. The two meet in the next "
             "lesson, where he answers a man who says that what pays is the only question."),
        ],
        "standard": (
            "Finish when you can find what makes the one who goes first safe to do so.",
            "Given a covenant's gains and costs and a sanction with a stated chance, compute the second party's "
            "payoff from keeping and from breaking, say which he chooses and what the first gets by performing "
            "first, and find the least sanction that makes keeping at least as good."
        ),
        "note": (
            "The lab's buyer reckons one covenant and no future dealings, and the oath is modelled as a "
            "penalty with a chance, which Hobbes does not do. The figures are the lesson's. And the lab cannot tell "
            "a covenant void for reasonable suspicion from one that merely pays less to keep, nor how Hobbes's "
            "two statements of the rule are to be fitted together."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Leviathan ch. 15, 1651 p. 71-75; PDF p. 196-200 of the operator's copy.
    # LEVKIT: covenant / fool.
    {
        "slug": "justice-and-the-fool",
        "title": "Justice and the Fool",
        "module": "Chapter 15 · Of other Lawes of Nature",
        "one_line": "The third law is to keep covenants made, and Hobbes answers the Fool, who says it can be reasonable to break one, by saying a man cannot reasonably count on the errors of others.",
        "summary": (
            "Chapter 15 opens with the third law of nature, that men perform their covenants made, and finds in it "
            "the fountain of justice and, with the commonwealth, of propriety. Then comes the Fool, who says there "
            "is no justice, and that breaking a covenant is not against reason when it serves one's benefit. "
            "Hobbes grants that the question lies where one side has performed or a power can compel, and answers "
            "that it is against reason, because a man who breaks a covenant is received into society only by the "
            "errors of others, which he cannot reasonably reckon upon. The Fool's calculation is run with a gain, a "
            "loss and a chance of being cast out."
        ),
        "key": [
            "third law: perform the covenants made",
            "injustice is the not performance of covenant",
            "no common power, no propriety, no injustice",
            "the Fool: breaking pays when it serves one",
            "break only if gain beats chance times loss",
        ],
        "key_label": "The third law and the Fool",
        "concepts_intro": (
            "The chapter's first pages turn the last chapter's results into a definition of justice, and the Fool "
            "is its test."
        ),
        "concepts": [
            ("Justice is keeping covenant",
             "The third law is that men perform their covenants made, without which covenants are empty words and "
             "all men still have a right to all things. Injustice is the not performance of covenant, and "
             "whatever is not unjust is just. But covenants of trust are invalid until the cause of fear is "
             "removed, so injustice can begin only with a coercive power, and propriety begins with it."),
            ("The Fool's challenge",
             "The Fool says there is no such thing as justice, since every man's conservation is committed to his "
             "own care, and so to keep or not to keep covenants is not against reason when it conduces to one's "
             "benefit. He does not deny that covenants exist or that breach may be called injustice. He asks "
             "whether injustice may not sometimes stand with the reason that dictates every man his own good."),
            ("Hobbes's reply",
             "The question lies only where one side has performed or a power can make him perform, and Hobbes says "
             "it is not against reason. A man cannot hope to defend himself without confederates, and one who "
             "breaks his covenant can be received into society only by the errors of others, which he cannot "
             "reasonably reckon upon as the means of his security."),
        ],
        "read_title": "The third law, the Fool, and what is said to him",
        "read_intro": (
            "The lesson reads the Fool's speech as the passage, because it is the chapter's centre, and goes "
            "back through the third law that sets it up and forward to the reply."
        ),
        "body": [
            ("p", "<strong>Chapter 15.</strong> &ldquo;The Foole hath sayd in his heart, there is no such thing as "
                  "Justice; and sometimes also with his tongue; seriously alleaging, that every mans conservation, "
                  "and contentment, being committed to his own care, there could be no reason, why every man might "
                  "not do what he thought conduced thereunto: and therefore also to make, or not make; keep, or "
                  "not keep Covenants, was not against Reason, when it conduced to ones benefit.&rdquo;"),
            ("p", "Before the Fool, the law that sets him up. &ldquo;From that law of Nature, by which we are "
                  "obliged to transferre to another, such Rights, as being retained, hinder the peace of Mankind, "
                  "there followeth a Third; which is this, That men performe their Covenants made: without which, "
                  "Covenants are in vain, and but Empty words.&rdquo; In this law, Hobbes says, &ldquo;consisteth "
                  "the Fountain and Originall of Justice&rdquo;. Where no covenant has been made no right has "
                  "been transferred and every man has a right to everything, so no action can be unjust. When a "
                  "covenant is made, to break it is unjust, and &ldquo;the definition of Injustice, is no other "
                  "than the not Performance of Covenant. And whatsoever is not Unjust, is Just.&rdquo;"),
            ("p", "He then draws the consequence of the last lesson. Covenants of mutual trust are invalid while "
                  "there is fear of non-performance, so &ldquo;Injustice actually there can be none, till the "
                  "cause of such feare be taken away&rdquo;, and that cannot be done in the natural condition of "
                  "war. &ldquo;Therefore before the names of Just, and Unjust can have place, there must be some "
                  "coércive Power, to compell men equally to the performance of their Covenants, by the terrour of "
                  "some punishment, greater than the benefit they expect by the breach of their "
                  "Covenant.&rdquo; Notice the standard: a punishment greater than the benefit, which is the "
                  "Fool's own calculation turned round. The same power is the beginning of propriety, since the "
                  "schools define justice as &ldquo;the constant Will of giving to every man his own&rdquo;, and "
                  "&ldquo;where there is no Own, that is, no Propriety, there is no Injustice&rdquo;."),
            ("p", "Then the Fool. The opening words echo Psalm 14, &ldquo;The fool hath said in his heart, There is no God&rdquo;, and "
                  "Hobbes makes the link himself: &ldquo;the same Foole hath said in his heart there is no "
                  "God&rdquo;. His case is put with some care. He does not deny that there are covenants, or that "
                  "&ldquo;such breach of them may be called Injustice, and the observance of them Justice&rdquo;. "
                  "What he &ldquo;questioneth&rdquo; is &ldquo;whether Injustice, taking away the feare of God&rdquo; "
                  "may not &ldquo;sometimes stand with that Reason, which dictateth to every man his own good; "
                  "and particularly then, when it conduceth to such a benefit, as shall put a man in a condition, "
                  "to neglect not onely the dispraise, and revilings, but also the power of other men&rdquo;. "
                  "That last clause is the heart of it: the Fool is not talking about the petty thief. He means the "
                  "case where the gain is so great that its holder need fear no one."),
            ("p", "Hobbes gives him examples to make him stronger. &ldquo;The Kingdome of God is gotten by "
                  "violence: but what if it could be gotten by unjust violence?&rdquo; Saturn was deposed by his son "
                  "Jupiter, and the heathen believed in Jupiter as the avenger of injustice. Coke's "
                  "<em>Commentaries on Littleton</em> held that if the right heir of the crown be attainted of "
                  "treason, the crown shall descend to him and the attainder be void at that instant. From such "
                  "instances, Hobbes says, a man will be very prone to infer that if the heir apparent kills the "
                  "king in possession, though his father, it can never be against reason, &ldquo;seeing all the "
                  "voluntary actions of men tend to the benefit of themselves&rdquo;. He adds: &ldquo;From such "
                  "reasoning as this, Successfull wickednesse hath obtained the name of Vertue&rdquo;. In 1651 "
                  "that was not a remote worry: Englishmen had just seen a king deposed and executed by men "
                  "who called it justice."),
            ("p", "The reply begins by drawing a boundary. &ldquo;This specious reasoning is neverthelesse "
                  "false. For the question is not of promises mutuall, where there is no security of performance on "
                  "either side; as when there is no Civill Power erected over the parties promising; for such "
                  "promises are no Covenants&rdquo;, so that is not where the Fool lives. It is &ldquo;either where "
                  "one of the parties has performed already; or where there is a Power to make him performe; there "
                  "is the question whether it be against reason, that is, against the benefit of the other to "
                  "performe, or not. And I say it is not against reason.&rdquo; Notice what Hobbes concedes: the "
                  "test of reason is benefit, and he means to meet the Fool on his own ground."),
            ("p", "He then argues in two steps. First, a man who does a thing which, &ldquo;notwithstanding any "
                  "thing can be foreseen, and reckoned on, tendeth to his own destruction, howsoever some accident "
                  "which he could not expect, arriving, may turne it to his benefit; yet such events do not make it "
                  "reasonably or wisely done&rdquo;. Reason judges by what can be reckoned on, not by what luck "
                  "turns out. Second, in a condition of war no man can hope &ldquo;by his own strength, or wit, to "
                  "defend himselfe from destruction, without the help of Confederates&rdquo;, and every one expects "
                  "from the confederation what any one else does. Therefore &ldquo;he which declares he thinks it "
                  "reason to deceive those that help him, can in reason expect no other means of safety, than what "
                  "can be had from his own single Power&rdquo;. Such a man &ldquo;cannot be received into any "
                  "Society, that unite themselves for Peace and Defence, but by the errour of them that receive "
                  "him; nor when he is received, be retayned in it, without seeing the danger of their errour; "
                  "which errours a man cannot reasonably reckon upon as the means of his security&rdquo;. If he is "
                  "cast out he perishes, and if he lives in society it is by errors he could not foresee, so it is "
                  "against the reason of his preservation, and those who do not destroy him &ldquo;forbear him "
                  "onely out of ignorance of what is good for themselves&rdquo;."),
            ("p", "The lab does the Fool's sum and then asks what Hobbes's reply does to its inputs. It has three "
                  "numbers: what breaking now gains, what being cast out of the confederacy costs, and the "
                  "chance of being found out and cast out. Breaking pays when `gain − chance · loss` is more than "
                  "keeping's `0`, so it pays when the chance is below `gain / loss`. In the ruin preset the gain is "
                  "`10` and the loss `100`, and the threshold is `1/10`: at a chance of `1/20` breaking is worth "
                  "`5`, at `1/10` nothing, at `1/5` it is worth `−10`. In the perish preset the loss is `1000`, "
                  "Hobbes's &ldquo;he perisheth&rdquo; counted as something large, the threshold falls to `1/100`, "
                  "and the Fool profits only if the chance is below one in a hundred. The Fool's best case is the kingdom "
                  "preset, with a gain of `100` against a loss of `20`: the threshold is `5`, above any chance, "
                  "and breaking pays even if he is certain to be caught. That is his &ldquo;benefit, as shall put "
                  "a man in a condition, to neglect&rdquo; the power of others."),
            ("p", "Hobbes's reply does not deny any of this arithmetic. It attacks the inputs. Reason, he says, judges an act by "
                  "what &ldquo;can be foreseen, and reckoned on&rdquo;; a lucky turn of events does &ldquo;not make "
                  "it reasonably or wisely done&rdquo;. And the breaker &ldquo;declareth that he thinks he may with "
                  "reason do so&rdquo;, so he can be kept in society only by others' errors, &ldquo;which errours a "
                  "man cannot reasonably reckon upon&rdquo;. In the lab's terms the Fool may not count on escaping at "
                  "all: the breach is itself the declaration, so the chance he may reckon with is `1`, and breaking "
                  "is worth the gain minus the loss. In the ruin preset that is `10 − 100 = −90`. And the kingdom's gain is the one Hobbes meets directly: of sovereignty gained by "
                  "rebellion he says that &ldquo;because it cannot reasonably be expected, but rather the contrary; "
                  "and because by gaining it so, others are taught to gain the same in like manner, the attempt "
                  "thereof is against reason&rdquo;. As for heaven, to be gained by breach of faith, it is "
                  "&ldquo;frivolous&rdquo;, since the one way imaginable is keeping covenant. So &ldquo;Justice "
                  "therefore, that is to say, Keeping of Covenant, is a Rule of Reason, by which we are forbidden "
                  "to do any thing destructive to our life; and consequently a Law of Nature.&rdquo;"),
            ("p", "The reply has been argued over ever since. David Hume, in the "
                  "<em>Enquiry concerning the Principles of Morals</em> of 1751, has a sensible knave who is "
                  "often read beside the Fool, though Hume never mentions Hobbes there: a man who thinks he may "
                  "profit by a breach that goes unseen. Hume answered that such a man loses the inward satisfaction "
                  "of an honest character, which Hume thought worth more than the gain. Hobbes's own reply is "
                  "different in kind. It does not say the breaker will be caught, and it does not rest on "
                  "character. It says that a man may not reckon on escaping, because that would depend on "
                  "errors he cannot foresee, and that a gain like a kingdom cannot reasonably be expected. "
                  "Whether that settles the matter is the point on which readers still divide."),
            ("p", "Hobbes closes the discussion of justice with a distinction that answers the Fool in another "
                  "way. A man is called just, he says, if he takes all the care he can that his actions may be "
                  "just, and does not lose the title by one or a few unjust actions that come from sudden passion "
                  "or mistake. What gives actions &ldquo;the relish of Justice&rdquo; is &ldquo;a certain "
                  "Noblenesse or Gallantnesse of courage, (rarely found,) by which a man scorns to be beholding for "
                  "the contentment of his life, to fraud, or breach of promise&rdquo;. He calls it rare, and does "
                  "not rely on it. Just actions, he adds, make a man not just but &ldquo;Guiltlesse&rdquo;."),
            ("p", "The next lesson, &ldquo;The Other Laws of Nature&rdquo;, reads the rest of Chapter 15, from "
                  "gratitude to the claim that the laws are theorems, and asks what a tournament of conditional "
                  "co-operators can and cannot show about them."),
        ],
        # LEVKIT: cfg drafted from PLAN D.1; corrected against kit-report.md in phase B.
        "lab": ("levkit", {
            "mode": "covenant",
            "view": "fool",
            "preset": "ruin",
            "presets": [
                {"id": "ruin", "label": "Gain 10, loss 100: chances from 0 to 1",
                 "gain": 10, "loss": 100, "chances": ["0", "1/20", "1/10", "1/5", "1/2", "1"],
                 "expect": {"lcvThreshold": "1/10 = 10%", "lcvValues": "0 = 0%: 10; 1/20 = 5%: 5; 1/10 = 10%: 0; 1/5 = 20%: −10; 1/2 = 50%: −40; 1 = 100%: −90", "lcvBreakAt": "2: 0 = 0%; 1/20 = 5%"}},
                {"id": "perish", "label": "Gain 10, loss 1000: being cast out is ruin",
                 "gain": 10, "loss": 1000, "chances": ["0", "1/200", "1/100", "1/20", "1/2"],
                 "expect": {"lcvThreshold": "1/100 = 1%", "lcvBreakAt": "2: 0 = 0%; 1/200 = 0.5%", "lcvKeepAt": "2: 1/20 = 5%; 1/2 = 50%"}},
                {"id": "kingdom", "label": "A kingdom: gain 100, loss 20",
                 "gain": 100, "loss": 20, "chances": ["0", "1/10", "1/2", "1"],
                 "expect": {"lcvThreshold": "5 = 500%, above certainty: breaking pays at every chance", "lcvValues": "0 = 0%: 100; 1/10 = 10%: 98; 1/2 = 50%: 90; 1 = 100%: 80", "lcvKeepAt": "0: none"}},
            ],
            "panel_title": "The Fool's calculation",
            "panel_intro": (
                "What breaking gains, what being cast out costs and the chances of being found out go in. For "
                "each chance the lab gives the Fool's expected gain from breaking against keeping's zero, and the "
                "threshold chance below which breaking pays."
            ),
        }),
        "steps_title": "Working out whether the Fool's calculation pays",
        "steps_intro": "Four steps, for any gain and loss.",
        "steps": [
            ("Set the gain, the loss and the chance",
             "The gain is what breaking brings now. The loss is what being cast out costs. The chance is how "
             "likely he is to be found out and cast out."),
            ("Compute breaking's expected value",
             "It is the gain minus the chance multiplied by the loss. Keeping is worth nothing more in this "
             "model, so breaking pays when its value is above zero."),
            ("Find the threshold",
             "Breaking pays below the chance that is the gain divided by the loss. If the gain exceeds the loss "
             "the threshold is more than one and breaking pays at every chance."),
            ("Ask what the chance can honestly be",
             "Hobbes's reply is that a man may reckon only on what can be foreseen, and others' errors "
             "cannot be, so the reasonable chance is certainty."),
        ],
        "worked": {
            "title": "Gain ten against a loss of a hundred",
            "intro": [
                "Breaking gains `10`. Being cast out costs `100`. The chances are `1/20`, `1/10` and `1/5`.",
            ],
            "lines": [
                "chance 1/20:  10 − (1/20) · 100 = 5",
                "chance 1/10:  10 − (1/10) · 100 = 0",
                "chance 1/5:  10 − (1/5) · 100 = −10",
                "threshold:  10 / 100 = 1/10",
                "breaking pays only below 1/10",
            ],
            "after": [
                "The Fool must therefore be more than nine times as sure of escaping as not. On Hobbes's reply "
                "he may not count on escaping at all: his breach declares him, and only others' errors could "
                "keep him in. At chance `1` breaking is worth `10 − 100 = −90`.",
            ],
        },
        "quiz_title": "The Fool's sum and Hobbes's reply",
        "quiz": [
            {"q": "In the ruin preset breaking gains 10 and being cast out costs 100. At what chance of being cast out "
                  "does breaking stop paying?",
             "a": ["1/5", "1/2", "1/20", "1/10"],
             "c": 3,
             "why": "Breaking pays `10 − chance · 100`, which is zero at `10/100 = 1/10` and negative above it. "
                    "At `1/20` it still pays `5`, and at `1/5` it costs `10`. The point of change is the gain over "
                    "the loss."},
            {"q": "What does the Fool say about covenants?",
             "a": ["That covenants do not exist",
                   "That breach of covenant is not called injustice by anyone",
                   "That keeping or not keeping covenants is not against reason when it conduces to one's benefit",
                   "That there is no God, and so no punishment"],
             "c": 2,
             "why": "The Fool does not deny that covenants exist or that breach is called injustice. His claim is "
                    "that to make or not make, keep or not keep covenants &ldquo;was not against Reason, when it "
                    "conduced to ones benefit&rdquo;. Hobbes does say that the same Fool has said in his heart "
                    "there is no God, but that is not his claim about covenants."},
            {"q": "Which of these is Hobbes's reason that breaking a covenant is against reason?",
             "a": ["A man who breaks it can be received into society only by the errors of others, which he cannot reasonably reckon upon",
                   "A man who breaks it will always be found out by the sovereign",
                   "A man who breaks it has sworn by God and will be punished after death",
                   "A man who breaks it has no right to anything"],
             "c": 0,
             "why": "The reply is that he &ldquo;cannot be received into any Society, that unite themselves for "
                    "Peace and Defence, but by the errour of them that receive him&rdquo;, and errors &ldquo;a man "
                    "cannot reasonably reckon upon as the means of his security&rdquo;. Hobbes does not say he will "
                    "always be found out. The hope of heaven he calls frivolous."},
            {"q": "In the kingdom preset the gain is 100 and the loss is 20. What does the lab show?",
             "a": ["Breaking pays only if the chance is below 1/5",
                   "Breaking pays at every chance of being cast out, even a certain one",
                   "Breaking never pays, since a kingdom cannot be gained by breach",
                   "Breaking pays at a chance of 1/2 but not at 1"],
             "c": 1,
             "why": "The threshold is `100/20 = 5`, and a chance cannot exceed `1`, so the Fool's expected gain is "
                    "positive at every chance, `80` when it is certain. That is the case Hobbes answers by "
                    "saying the gain itself cannot reasonably be expected."},
        ],
        "mistakes": [
            ("Thinking the Fool is a fool in the ordinary sense",
             "He is arguing from benefit, as Hobbes does, and his case is put so that Hobbes must answer on "
             "benefit. Hobbes calls the reasoning &ldquo;specious&rdquo; and false, and meets it with a reply "
             "about reckoning, not a rebuke."),
            ("Reading the Fool's lab as Hobbes's reply",
             "The table is the Fool's sum, and it shows when breaking pays for a stated gain, loss and chance. "
             "Hobbes's reply is that reason may reckon only on what can be foreseen, so the Fool may not count "
             "on escaping; the table only shows what follows at each chance. It cannot say whether he is right."),
            ("Thinking the sovereign is what makes keeping reasonable",
             "In the reply there is no sovereign. The reason is the confederacy a man needs and the errors he "
             "would have to rely on. The coercive power is what makes promises into covenants and justice possible, "
             "as the start of the chapter says, but the Fool's case is put where such a power exists or a "
             "side has already performed."),
        ],
        "standard": (
            "Finish when you can work out the Fool's sum and say what Hobbes replies to it.",
            "Given a gain, a loss and a chance of being cast out, compute the expected value of breaking, find the "
            "threshold chance, and say which input Hobbes's reply challenges and why."
        ),
        "note": (
            "The lab takes the chance as given and the loss as a number, which is what the Fool does, and "
            "Hobbes's reply is a claim about what the chance and the gain can honestly be reckoned at. Whether "
            "breakers are in fact found out is an empirical question the lab cannot decide, and the sensible "
            "knave, read beside the Fool, is the doubt that it matters."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Leviathan ch. 15, 1651 p. 75-80; PDF p. 201-207 of the operator's copy.
    # choicekit/iterated.
    {
        "slug": "the-other-laws-of-nature",
        "title": "The Other Laws of Nature",
        "module": "Chapter 15 · Of other Lawes of Nature",
        "one_line": "Gratitude, complaisance, pardon on caution and revenge only for the future follow from the first law, and the laws bind to a desire always and to the act when there is security.",
        "summary": (
            "The rest of Chapter 15 runs through sixteen further laws of nature, from gratitude to witnesses, each "
            "derived as a means to peace, and sums them in the one rule not to do to another what you would not have "
            "done to yourself. Hobbes says they oblige in the court of conscience always and in act only when there "
            "is security, that they are easy, eternal and the whole of moral philosophy, and that they are not "
            "properly laws but theorems until delivered in the word of God. A repeated dilemma with strategies that "
            "reward, forgive and retaliate is played, and what its tournament does and does not show is read off it."
        ),
        "key": [
            "gratitude, so that benevolence can begin",
            "pardon on caution of the future",
            "revenge looks to the good to follow",
            "bound to a desire always, to act with security",
            "theorems of reason, laws as God's word",
        ],
        "key_label": "Sixteen more laws, in five lines",
        "concepts_intro": (
            "Hobbes does not rest after the Fool. The rest of the chapter derives the laws of nature one by one, and "
            "in its last pages says what kind of thing they are."
        ),
        "concepts": [
            ("Gratitude, complaisance, pardon and revenge",
             "Gratitude depends on antecedent grace and is the fourth law: a man who is given a benefit endeavours "
             "that the giver have no reasonable cause to repent. Complaisance is the fifth, to accommodate oneself to "
             "the rest. The sixth is to pardon past offences, upon caution of the future, of those who repent, and the "
             "seventh is that in revenge men look to the greatness of the good to follow."),
            ("Equals, equity, lots and judges",
             "The eighth law is against signs of hatred or contempt, the ninth is to acknowledge every man for "
             "one's equal by nature, the tenth against reserving a right one would not leave to others, and the "
             "later ones are equity, common use, lot, safe conduct for mediators, submission to an arbitrator and "
             "rules for judges and witnesses. Hobbes counts nineteen in all."),
            ("What kind of thing a law of nature is",
             "The laws are summed in the rule not to do to another what you would not have done to yourself. They "
             "oblige in foro interno, to a desire that they take place, and in foro externo, to act, not always. "
             "They are eternal and easy, their science is moral philosophy, and they are properly theorems of "
             "reason, called laws only as the word of God."),
        ],
        "read_title": "Four laws, the rest, and what Hobbes says they are",
        "read_intro": (
            "The lesson reads the sixth law as its passage, because pardon is where the laws most plainly "
            "reach beyond the last two chapters, and goes back through the others to the chapter's close."
        ),
        "body": [
            ("p", "<strong>Chapter 15.</strong> &ldquo;A sixth Law of Nature, is this, That upon caution of the Future "
                  "time, a man ought to pardon the offences past of them that repenting, desire it. For Pardon, is "
                  "nothing but granting of Peace; which though granted to them that persevere in their hostility, be "
                  "not Peace, but Feare; yet not granted to them that give caution of the Future time, is signe of "
                  "an aversion to Peace; and therefore contrary to the Law of Nature.&rdquo;"),
            ("p", "The chain so far is short. The first law is to seek peace, the second to lay down one's right "
                  "when others will, and the third to keep the covenants made. Chapter 15 now goes on, and Hobbes "
                  "derives each further law the same way, by showing that without it men would remain in war, which is "
                  "against the first. His marginal notes number nineteen, and the lesson takes them in groups. "
                  "Gratitude is the fourth: as justice depends on antecedent covenant, gratitude depends on "
                  "&ldquo;Antecedent Grace&rdquo;, and the law is that a man who receives a benefit &ldquo;of meer "
                  "Grace, Endeavour that he which giveth it, have no reasonable cause to repent him of his good "
                  "will&rdquo;. The reason: &ldquo;of all Voluntary Acts, the Object is to every man his own Good; "
                  "of which if men see they shall be frustrated, there will be no beginning of benevolence, or trust; "
                  "nor consequently of mutuall help&rdquo;, and so they remain in war. Its breach is ingratitude."),
            ("p", "The fifth is complaisance, and Hobbes finds an image for it in builders: a stone that by its "
                  "&ldquo;asperity, and irregularity of Figure, takes more room from others, than it selfe "
                  "fills&rdquo; is cast away as troublesome, and so is the man who holds on to things that are "
                  "superfluous to him and necessary to others. The sixth is the passage above. The seventh follows "
                  "from it: &ldquo;in Revenges, (that is, retribution of Evil for Evil,) Men look not at the "
                  "greatnesse of the evill past, but the greatnesse of the good to follow.&rdquo; We are forbidden "
                  "to punish &ldquo;with any other designe, than for correction of the offender, or direction of "
                  "others&rdquo;, since revenge with no eye to the example and profit to come is &ldquo;a triumph, "
                  "or glorying in the hurt of another, tending to no end&rdquo;, and so a kind of vain-glory. It "
                  "is the glory of Chapter 13, the quarrel over a smile, turned into a law against it."),
            ("p", "The lab is a repeated dilemma. Each round two players choose to help or to refuse; helping "
                  "pays `3` each if both do, a refusal against a helper pays `5` and leaves the helper `0`, and "
                  "two refusers get `1` each. The strategies are the lab's seven, among them the man who always "
                  "helps (ALLC), who always refuses (ALLD), tit for tat (TFT), which helps first and then copies, "
                  "and tit for two tats (TF2T), which refuses only after two refusals in a row. Nothing in the "
                  "lab is Hobbes's, and the strategies are the lesson's stand-ins for dispositions: the lab "
                  "shows what each does to a pair, and the reader must judge whether the disposition is the law."),
            ("p", "In the gratitude preset two tit-for-tat players meet for ten rounds. Each helps first and each "
                  "copies, so both help every round and each gets `30`, where two refusers would get `10`. "
                  "A benefit answered by a benefit starts a run of benevolence and trust, which is exactly what "
                  "Hobbes says the law is for. In the echo preset a tit-for-tat player meets a suspicious one who "
                  "refuses first. Each copies the other's last move, the refusal passes back and forth, and each "
                  "ends with `25`. In the pardon preset the player is tit for two tats, which lets one refusal "
                  "pass: the pair settle into helping from the second round, the pardoner gets `27` where echo gave "
                  "`25`, and the offender `32` where echo gave him `25`. The sixth law is the argument for "
                  "taking `27` over `25`, in a table."),
            ("p", "The prey preset is Hobbes's own warning. A man who helps every round meets one who refuses "
                  "every round: the helper gets `0` in ten rounds and the refuser `50`. This is the case at the "
                  "end of the chapter of the man who &ldquo;should be modest, and tractable, and performe all he "
                  "promises, in such time, and place, where no man els should do so&rdquo; and so &ldquo;should "
                  "but make himselfe a prey to others, and procure his own certain ruine&rdquo;. The once preset "
                  "is a single round of tit for tat against a refuser, which is the hardest case for the laws: "
                  "tit for tat gets `0`, the refuser `5`, and nothing follows the round."),
            ("p", "What the tournament does show is in the round-robin winner figure, in which each of the seven strategies meets "
                  "all seven, itself included, and the totals are added. In ten rounds the winner is tit for two "
                  "tats with `185`, tit for tat has `184`, the always-helper has `177`, and the always-refuser has "
                  "`146`. In one round the always-refuser and the suspicious tit for tat tie at `27`, and every helper has `15`. Robert Axelrod ran computer "
                  "tournaments of this kind about 1980 and reported that tit for tat scored best; here, with a "
                  "different field, it comes second by a point, which shows how much depends on who is in the "
                  "tournament. The result Hobbes needs is smaller than a winner: that where there will be another "
                  "meeting, reward, pardon and a limit on revenge beat refusing, and where there will not, they do "
                  "not. The always-helper's third place also shows the other half of his claim: in a field of "
                  "mostly conditional helpers a man who always helps is preyed upon only by the two strategies that refuse, and still finishes third."),
            ("p", "The rest of the nineteen are prescriptions for a world of equals and neighbours. The eighth is "
                  "against signs of hatred or contempt, which provoke to fight, and its breach is contumely. The "
                  "ninth is that every man acknowledge another for his equal by nature, and its breach is pride. "
                  "Here he takes on Aristotle, who made some men by nature fitter to command and some to serve, "
                  "&ldquo;as if Master and Servant were not introduced by consent of men, but by difference of "
                  "Wit: which is not only against reason; but also against experience&rdquo;. Hobbes's argument is "
                  "a dilemma: &ldquo;If Nature therefore have made men equall; that equalitie is to be acknowledged: or if Nature "
                  "have made men unequall; yet because men that think themselves equall, will not enter into "
                  "conditions of Peace, but upon Equall termes, such equalitie must be admitted.&rdquo; That is "
                  "the equality of the first lesson, turned from a premise into a law. The tenth is that no one "
                  "reserve a right he would not leave to every other; the eleventh is equity, that a judge deal "
                  "equally between parties; then common use of what cannot be divided, lot where it cannot be "
                  "shared, first possession or first birth where it falls to a lot, safe conduct for those who "
                  "mediate, submission to an arbitrator, no man a judge in his own cause or where he profits by "
                  "one side's victory, and witnesses, with a third or fourth to be believed where two disagree."),
            ("p", "Before the fourth law he had paused on justice of actions to revise a school distinction. Writers divide it into "
                  "commutative and distributive, the first in arithmetical proportion and the second in "
                  "geometrical. Hobbes says the value of things contracted for is &ldquo;measured by the Appetite of "
                  "the Contractors: and therefore the just value, is that which they be contented to give&rdquo;. So "
                  "commutative justice is only the keeping of covenant in buying and selling, hiring, lending and "
                  "the like, and distributive justice is the justice of an arbitrator, &ldquo;more properly "
                  "Equity&rdquo;. The laws of nature, he adds, are those that dictate peace &ldquo;for a means of the "
                  "conservation of men in multitudes&rdquo;, and he leaves out drunkenness and the like, which "
                  "destroy only particular men."),
            ("p", "The laws are then compressed. They seem &ldquo;too subtile a deduction&rdquo; for the most "
                  "part of mankind, who are too busy getting food, so they have been contracted into one sum, "
                  "&ldquo;Do not that to another, which thou wouldest not have done to thy selfe&rdquo;. The man who "
                  "weighs another's actions against his own and finds them too heavy is to put them in the other "
                  "scale and his own in their place, &ldquo;that his own passions, and selfe-love, may adde nothing "
                  "to the weight&rdquo;. And then comes the sentence that answers the prey: &ldquo;The Lawes of "
                  "Nature oblige in foro interno; that is to say, they bind to a desire they should take place: but "
                  "in foro externo; that is, to the putting them in act, not alwayes.&rdquo; A man who kept them "
                  "where no one else did would make himself a prey, but one who, having &ldquo;sufficient "
                  "Security&rdquo; that others will, does not observe them &ldquo;seeketh not Peace, but War&rdquo;. "
                  "They are &ldquo;Immutable and Eternall; For Injustice, Ingratitude, Arrogance, Pride, Iniquity, "
                  "Acception of persons, and the rest, can never be made lawfull. For it can never be that Warre shall "
                  "preserve life, and Peace destroy it.&rdquo; And they are easy, since they require only "
                  "&ldquo;an unfeigned and constant endeavour&rdquo;."),
            ("p", "Their science is &ldquo;the true and onely Moral Philosophy&rdquo;. Good and evil are names of "
                  "appetites and aversions, and different in different men, so that as long as private appetite is "
                  "the measure a man is in mere nature, in war. But all men agree that peace is good, and so are the "
                  "means to it, &ldquo;Justice, Gratitude, Modesty, Equity, Mercy, &amp; the rest of the Laws of "
                  "Nature&rdquo;. The writers of moral philosophy, he says, agree on the same virtues but not seeing "
                  "why they are good, &ldquo;place them in a mediocrity of passions: as if not the Cause, but the "
                  "Degree of daring, made Fortitude&rdquo;. A virtue, for Hobbes, is a means to peace, not a "
                  "mean between extremes."),
            ("p", "The last paragraph is a qualification many readers miss. &ldquo;These dictates of Reason, men use "
                  "to call by the name of Lawes, but improperly: for they are but Conclusions, or Theoremes "
                  "concerning what conduceth to the conservation and defence of themselves; wheras Law, properly "
                  "is the word of him, that by right hath command over others. But yet if we consider the same "
                  "Theoremes, as delivered in the word of God, that by right commandeth all things; then are they "
                  "properly called Lawes.&rdquo; Readers have taken this in two ways. A. E. Taylor and Howard "
                  "Warrender, in the twentieth century, held that Hobbes means the laws to bind as God's commands, "
                  "apart from any interest; others read the theorems as rules of prudence for staying alive, "
                  "as the word &ldquo;conduceth&rdquo; and the whole run of the argument suggest. The lab agrees "
                  "with the second only in that it needs no command. It does not decide between them."),
            ("p", "That is the end of Part I's argument about men. The next course, &ldquo;Persons and the "
                  "Generation of a Commonwealth&rdquo;, begins with Chapter 16, &ldquo;Persons, Authors and "
                  "Actors&rdquo;, and with the question of how a multitude of men who are bound to desire peace "
                  "come to be bound to act."),
        ],
        "lab": ("choicekit", {
            "mode": "iterated",
            "preset": "gratitude",
            "a": "TFT",
            "b": "TFT",
            "rounds": 10,
            "presets": [
                {"id": "gratitude", "label": "Gratitude: two tit-for-tat players, ten rounds",
                 "R": 3, "S": 0, "T": 5, "P": 1, "a": "TFT", "b": "TFT", "rounds": 10, "delta": "9/10",
                 "expect": {"itScoreA": "30", "itScoreB": "30", "itWinner": "TF2T: 185", "itThresh": "GRIM 1/2, TFT 2/3: δ = 9/10 sustains"}},
                {"id": "echo", "label": "Echo: tit for tat meets a player who refuses first",
                 "R": 3, "S": 0, "T": 5, "P": 1, "a": "TFT", "b": "STFT", "rounds": 10, "delta": "9/10",
                 "expect": {"itScoreA": "25", "itScoreB": "25"}},
                {"id": "pardon", "label": "Pardon: tit for two tats meets a player who refuses first",
                 "R": 3, "S": 0, "T": 5, "P": 1, "a": "TF2T", "b": "STFT", "rounds": 10, "delta": "9/10",
                 "expect": {"itScoreA": "27", "itScoreB": "32"}},
                {"id": "prey", "label": "Prey: the always-helper meets the always-refuser",
                 "R": 3, "S": 0, "T": 5, "P": 1, "a": "ALLC", "b": "ALLD", "rounds": 10, "delta": "9/10",
                 "expect": {"itScoreA": "0", "itScoreB": "50"}},
                {"id": "once", "label": "Once: one round, tit for tat against a refuser",
                 "R": 3, "S": 0, "T": 5, "P": 1, "a": "TFT", "b": "ALLD", "rounds": 1, "delta": "1/4",
                 "expect": {"itScoreA": "0", "itScoreB": "5", "itWinner": "ALLD, STFT: 27", "itThresh": "GRIM 1/2, TFT 2/3: δ = 1/4 does not"}},
            ],
            "panel_title": "Reward, pardon and retaliation in a repeated dilemma",
            "panel_intro": (
                "Player A and player B each follow a rule for the number of rounds shown. The two totals are "
                "their scores; the last two figures give the winner of a round robin of all seven rules for the same "
                "number of rounds and the continuation chance help needs. Try the pardon preset against echo."
            ),
        }),
        "steps_title": "Reading a repeated dilemma against the laws",
        "steps_intro": "Four steps, for any pair of strategies.",
        "steps": [
            ("Set the payoffs and the number of rounds",
             "Use a dilemma in which a refusal beats help and mutual help beats mutual refusal, and say how "
             "many times the pair meet."),
            ("Pick the rule each player follows",
             "Name what it plays first and what it plays after help and after refusal. Reward, pardon and "
             "limited revenge are rules of this kind."),
            ("Play the rounds and add the scores",
             "Total each player's payoffs over all rounds, and compare the totals with those of the same "
             "players refusing throughout."),
            ("Ask what the result shows",
             "It shows what the rules do to a pair or a field of the lab's choosing. Whether a rule is a law "
             "of nature, or a dictate of reason at all, is the chapter's question."),
        ],
        "worked": {
            "title": "Echo and pardon over ten rounds",
            "intro": [
                "Payoffs `3`, `0`, `5`, `1`. A player who refuses first meets tit for tat, then tit for two tats.",
            ],
            "lines": [
                "tit for tat copies, the refusal passes back and forth",
                "scores over 10 rounds:  5 + 0 + 5 + 0 ... = 25 each",
                "tit for two tats lets one refusal pass",
                "round 1:  refuser 5, pardoner 0;  rounds 2 to 10:  3 each",
                "pardoner:  0 + 9 · 3 = 27;  refuser:  5 + 9 · 3 = 32",
            ],
            "after": [
                "Pardon is worth `2` more to the one who pardons than echo is, and `7` more to the offender, "
                "who is forgiven for what he began. That is why Hobbes asks for caution of the future: in the "
                "lab the offender's repentance is that he copies help, and nothing else would make `27` better "
                "than `25`.",
            ],
        },
        "quiz_title": "Sixteen laws and what they are",
        "quiz": [
            {"q": "Why, on Hobbes's account, does gratitude matter for peace?",
             "a": ["It is owed to the giver by covenant",
                   "Without it men would see their gifts frustrated, so there would be no beginning of benevolence or trust, and war would remain",
                   "The sovereign commands it",
                   "It makes the receiver richer than the giver"],
             "c": 1,
             "why": "Gratitude depends on antecedent grace, not on covenant. Hobbes says that if givers are "
                    "frustrated &ldquo;there will be no beginning of benevolence, or trust; nor consequently of "
                    "mutuall help&rdquo;, and they remain in the condition of war, which the first law forbids."},
            {"q": "In the prey preset the always-helper meets the always-refuser for ten rounds. What does the "
                  "helper score?",
             "a": ["50", "30", "10", "0"],
             "c": 3,
             "why": "Every round he helps and is refused, which pays him `0`, so his total is `0`, while the refuser "
                    "collects `5` ten times for `50`. It is the man Hobbes says would &ldquo;make himselfe a "
                    "prey&rdquo;."},
            {"q": "What does the seventh law of nature say punishment is for?",
             "a": ["Correction of the offender or direction of others, and nothing else",
                   "Repaying evil with an equal evil",
                   "Satisfying the offended man's honour",
                   "Making the offender pay for the greatness of the evil past"],
             "c": 0,
             "why": "Men are to &ldquo;look not at the greatnesse of the evill past, but the greatnesse of the good to "
                    "follow&rdquo;, and are forbidden to inflict punishment &ldquo;with any other designe, than for "
                    "correction of the offender, or direction of others&rdquo;. The other answers look to the past, "
                    "which the law forbids."},
            {"q": "What does Hobbes mean when he says the laws of nature oblige in foro interno?",
             "a": ["They bind only in thought and never in act",
                   "They bind only within a commonwealth",
                   "They bind to a desire that they should take place, and to act only when there is security",
                   "They bind only men who have sworn"],
             "c": 2,
             "why": "&ldquo;They bind to a desire they should take place: but in foro externo; that is, to the putting "
                    "them in act, not alwayes.&rdquo; Where one would be prey to others, acting is not required, and "
                    "where one has sufficient security, not acting seeks war. The laws are not confined to thought, "
                    "to a commonwealth or to oaths."},
        ],
        "mistakes": [
            ("Thinking tit for tat is Hobbes's law of nature",
             "In the lab's field of seven the ten-round winner is tit for two tats, with `185` against tit for "
             "tat's `184`, and a single round is won by the refusers. The result depends on the field and the "
             "length, so a tournament cannot name the law. What it shows is that reward and pardon beat "
             "refusing where the pair will meet again."),
            ("Reading in foro interno as the laws being in the mind only",
             "They bind to a desire always. In act they bind when there is security, and where there is, not "
             "acting is seeking war. Hobbes says outright that keeping them where nobody else will makes a man a "
             "prey."),
            ("Taking the laws of nature as commands",
             "Hobbes says that to call these dictates laws is improper. They are conclusions or theorems of what "
             "conduces to preservation, and laws only as delivered in the word of God, who by right commands all "
             "things. How much that qualification takes back is a question about the whole book, which the "
             "next course starts to answer."),
        ],
        "standard": (
            "Finish when you can play the repeated dilemma and say what Hobbes's laws are.",
            "Given a pair of strategies for a stated number of rounds, compute each player's score, say which of "
            "Hobbes's laws of gratitude, pardon and revenge the pair illustrates, and say what the sentence about foro "
            "interno and foro externo adds."
        ),
        "note": (
            "The strategies are the lab's seven, and the payoffs and the number of rounds are the lesson's. "
            "A round robin shows how rules fare against one another in a stated field, not that men have such "
            "rules or that a rule that scores well is a law of nature. Whether the laws are commands or "
            "theorems is a question about Hobbes's text, and the lab does not touch it."
        ),
    },
]
