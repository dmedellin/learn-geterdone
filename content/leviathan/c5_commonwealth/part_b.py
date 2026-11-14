"""Persons and the Generation of a Commonwealth, lessons 4-6 -- Chapters 18 and 19.

Quotations are copied from the operator's copy of the 1651 text and checked
against the page image, as in part_a. Lesson 6 is a levkit lesson: its cfg is
drafted from docs/leviathan/PLAN.md section D.1 and corrected against
docs/leviathan/kit-report.md when the kit is registered.
"""

LESSONS = [
    # ---------------------------------------------------------------- 04
    # Leviathan ch. 18, 1651 p. 89; PDF p. 218 of the operator's copy (the second
    # right and the first); PDF p. 219 (no precedent covenant); PDF p. 220
    # (no injury); PDF p. 223-224 (indivisible; the comparison of miseries).
    {
        "slug": "the-rights-of-sovereigns",
        "title": "The Rights of Sovereigns by Institution",
        "module": "Chapter 18 · Of the Rights of Soveraignes by Institution",
        "one_line": "From the covenant of every man with every man Hobbes derives twelve rights of the sovereign, among them that the sovereign cannot breach a covenant he never made, so no subject is freed by his breach.",
        "summary": (
            "Chapter 18 draws the consequences of an instituted commonwealth, one by one, "
            "and the second of them is the one that has been disputed ever since: because "
            "the sovereign is not a party to the covenant, he cannot break it, and no "
            "subject is released by a pretence of forfeiture. Check that argument as "
            "premises, see that it is valid, and find the premise a later critic would deny."
        ),
        "key": [
            "instituted: all authorise the major part",
            "twelve rights follow, First to Lastly",
            "no covenant made by the sovereign",
            "so no breach, and no forfeiture",
            "valid; the premise at stake is: no covenant",
        ],
        "key_label": "The sovereign and the covenant",
        "concepts_intro": (
            "Chapter 18 is a list, and the list is an argument: each right is derived from "
            "the way the commonwealth was made."
        ),
        "concepts": [
            ("Institution",
             "A commonwealth is instituted when a multitude agree and covenant, every one "
             "with every one, that to whatever man or assembly the major part gives the "
             "right to present the person of them all, every one, as well he that voted "
             "for it as he that voted against it, shall authorise all that person's "
             "actions and judgements as if they were his own."),
            ("The rights that follow",
             "The chapter counts the rights in order, from First to Lastly: twelve. "
             "They are the rights of judging the means of peace, of regulating doctrine, "
             "of making law and judging by it, of war and peace, of choosing officers, of "
             "reward and punishment, and of honour, together with the consequences for "
             "subjects of having authorised him."),
            ("Indivisible",
             "Hobbes calls these rights &ldquo;incommunicable, and inseparable&rdquo;. "
             "Hold some of them and give the rest away, and the ones you give "
             "away will undo the ones you keep; that, he says, is what happened in England."),
        ],
        "read_title": "The passage first, then the twelve in order",
        "read_intro": (
            "The passage is the second of the twelve, since it is the one the lab checks. "
            "The twelve are then taken in the order the chapter gives them."
        ),
        "body": [
            ("p", "<strong>Chapter 18.</strong> &ldquo;Secondly, Because the Right of "
                  "bearing the Person of them all, is given to him they make Soveraigne, by "
                  "Covenant onely of one to another, and not of him to any of them; there "
                  "can happen no breach of Covenant on the part of the Soveraigne; and "
                  "consequently none of his Subjects, by any pretence of forfeiture, can be "
                  "freed from his Subjection.&rdquo;"),
            ("p", "Begin with what Hobbes means by instituted. In Chapter 17 a multitude "
                  "authorised one person; Chapter 18 says how it is done in the ordinary "
                  "case. They covenant, every one with every one, that whoever the major "
                  "part gives the right to present the person of them all shall be "
                  "authorised, &ldquo;every one, as well he that Voted for it, as he that "
                  "Voted against it&rdquo;, in all his actions and judgements, as if they "
                  "were his own. Chapter 16's authors and actors are carrying the weight: "
                  "the sovereign is the actor, the subjects are the authors, and what he "
                  "does in their name is theirs."),
            ("ul", [
                "First: the subjects cannot change the form of government, nor transfer their person to another, without his leave.",
                "Second: the sovereign power cannot be forfeited.",
                "Third: no man can without injustice protest against the sovereign the major part declared.",
                "Fourth: what the sovereign does cannot be an injury to any subject.",
                "Fifth: he cannot justly be put to death or punished by his subjects.",
                "Sixth: he judges what opinions and doctrines are averse to peace and who may teach them.",
                "Seventh: he makes the rules of property, what each man may enjoy and do.",
                "Eighth: he has the right of judicature, to hear and decide controversies.",
                "Ninth: he makes war and peace with other nations.",
                "Tenth: he chooses all counsellors, ministers, magistrates and officers.",
                "Eleventh: he rewards and punishes, by law or where there is none as he judges best.",
                "Lastly: he gives titles of honour and orders each man's place.",
            ]),
            ("p", "Take the second, whose argument is the chapter's most daring. Suppose "
                  "the sovereign had made a covenant with his subjects beforehand, that he "
                  "would rule well, and could be deposed if he did not. With whom? Not "
                  "with the whole multitude as one party, Hobbes says, because &ldquo;as "
                  "yet they are not one Person&rdquo;. Then with each severally; but "
                  "after he has the sovereignty those covenants are void, because any act "
                  "alleged as a breach is the act of every one of them, since it was done "
                  "in the person and by the right of each. And if one claims a breach and "
                  "another denies it, &ldquo;there is in this case, no Judge to decide the "
                  "controversie: it returns therefore to the Sword again&rdquo;, which is "
                  "the war the covenant was made to end. It is &ldquo;therefore in vain to "
                  "grant Soveraignty by way of precedent Covenant&rdquo;, since "
                  "covenants &ldquo;being but words, and breath, have no force to oblige, "
                  "contain, constrain, or protect any man, but what it has from the "
                  "publique Sword&rdquo;."),
            ("p", "He adds a test you can run on your own intuitions. In a sovereign "
                  "assembly, no one imagines a covenant: &ldquo;no man is so dull as to "
                  "say, for example, the People of Rome, made a Covenant with the "
                  "Romans&rdquo;, on conditions which, if not kept, allowed the Romans to "
                  "depose the Roman people. That we think otherwise of a monarch, he says, "
                  "comes from the ambition of those who are kinder to the government of an "
                  "assembly, in which they may hope to share, than to monarchy."),
            ("p", "Write the argument down and it is short. Let `c` be <em>the "
                  "sovereign is a party to a covenant with his subjects</em>, `b` be "
                  "<em>the sovereign breaches a covenant with his subjects</em> and "
                  "`f` be <em>the subjects are freed from subjection by forfeiture</em>. "
                  "Hobbes's premises are that the sovereign is a party to no such covenant, "
                  "`~c`; that a breach needs a covenant, `b -> c`; and that forfeiture needs "
                  "a breach, `f -> b`. The conclusion is that no one is freed, `~f`. In the "
                  "preset <em>hobbes</em> the lab finds the argument valid: there is no row "
                  "in which the three premises are true and `~f` is false."),
            ("p", "That is a verdict on the form of the argument, not on the argument. "
                  "John Locke, in the Two Treatises of Government, written in the "
                  "Exclusion Crisis and published after the revolution of 1688, held that those who hold the power of a government "
                  "hold it in trust, for ends the people set, and that when the trust "
                  "is abused the people may remove them. That puts a covenant, or something "
                  "like it, between the people and the holders of power: `c` is true. The "
                  "preset <em>trust</em> changes the first premise to `c` and keeps "
                  "the other two. The lab finds the conclusion no longer follows, and "
                  "exactly one row breaks it: `c`, `b` and `f` all true. The third preset, "
                  "<em>other-release</em>, drops Hobbes's third premise and keeps `~c` and "
                  "`b -> c`; subjects might then be freed by something short of a breach, "
                  "such as the sovereign's failing to protect them, and the lab again "
                  "finds one row in which the conclusion fails. Hobbes's own answer to a "
                  "claimed trust is in the passage itself: with no judge between the "
                  "parties, a trust that can be declared broken by those who gave it is "
                  "the sword again. Locke's reply was that the people shall be judge, and "
                  "that where there is no judge on earth the appeal lies to heaven: he "
                  "accepted the risk that Hobbes would not."),
            ("p", "The remaining rights are the second right's company. The fourth runs "
                  "on Chapter 16: because every subject is author of what the sovereign "
                  "does, &ldquo;he that complaineth of injury from his Soveraigne, "
                  "complaineth of that whereof he himselfe is Author&rdquo;. Hobbes does not "
                  "conclude that the sovereign can do no wrong: &ldquo;It is true that they "
                  "that have Soveraigne power, may commit Iniquity; but not Injustice, or "
                  "Injury in the proper signification.&rdquo; The sixth, to judge doctrines, "
                  "rests on his claim that actions proceed from opinions, so that the "
                  "governing of opinions is the governing of actions."),
            ("p", "The rights are indivisible, which is the chapter's practical lesson. If "
                  "the sovereign gives away the militia he keeps judicature in vain, for "
                  "want of execution; if he gives away the power of raising money the "
                  "militia is in vain; and if he gives away the government of doctrines, "
                  "&ldquo;men will be frighted into rebellion with the feare of "
                  "Spirits&rdquo;. And he points to England: &ldquo;If there had not first "
                  "been an opinion received of the greatest part of England, that these "
                  "Powers were divided between the King, and the Lords, and the House of "
                  "Commons, the people had never been divided, and fallen into this Civill "
                  "Warre&rdquo;."),
            ("p", "He ends with the objection that subjects of such a power are miserable, "
                  "and answers it by comparison: the greatest that can happen to the "
                  "people in general in any form of government &ldquo;is scarce sensible, "
                  "in respect of the miseries, and horrible calamities, that accompany a "
                  "Civill Warre&rdquo;. A reader may take or leave the comparison; it is "
                  "the premise on which his answer to the objection rests, and the lab "
                  "cannot weigh it. "
                  "The next lesson, &ldquo;The Several Kinds of Commonwealth&rdquo;, takes "
                  "Chapter 19 and asks which person it is best to give the rights to."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "show": "all",
            "preset": "hobbes",
            "presets": [
                {"id": "hobbes", "label": "Hobbes: the sovereign is party to no covenant",
                 "premises": ["~c", "b -> c", "f -> b"], "conclusion": "~f",
                 "expect": {"vaVerdict": "Valid", "vaCounter": "0"}},
                {"id": "trust", "label": "A trust: the sovereign is party to a covenant",
                 "premises": ["c", "b -> c", "f -> b"], "conclusion": "~f",
                 "expect": {"vaVerdict": "Invalid", "vaCounter": "1"}},
                {"id": "other-release", "label": "Subjects may be freed short of a breach",
                 "premises": ["~c", "b -> c"], "conclusion": "~f",
                 "expect": {"vaVerdict": "Invalid", "vaCounter": "1"}},
            ],
            "panel_title": "Can a subject be freed by the sovereign's breach?",
            "panel_intro": (
                "c: the sovereign is party to a covenant with his subjects. b: he breaches "
                "it. f: the subjects are freed by forfeiture. Find the premise whose "
                "change makes the conclusion fail, and the row in which it fails."
            ),
        }),
        "steps_title": "Testing an argument about forfeiture",
        "steps_intro": "Four steps, the last of which is the one a critic takes.",
        "steps": [
            ("Name the three claims",
             "Say in one sentence each what it is for the sovereign to be party to a "
             "covenant, to breach it, and for subjects to be freed by that breach."),
            ("Write the premises",
             "State that there is no such covenant, that a breach needs a covenant, and "
             "that forfeiture needs a breach. Put them into the lab as premises."),
            ("Check the form",
             "Ask whether the conclusion follows. A valid argument has no row in which "
             "the premises hold and the conclusion fails."),
            ("Find the premise at stake",
             "If you reject the conclusion, change one premise and see whether the "
             "argument becomes invalid. The premise whose change does it is where your "
             "disagreement lies."),
        ],
        "worked": {
            "title": "Hobbes and the argument from trust",
            "intro": [
                "The two presets differ in one premise. The letters are `c`, `b` and `f`.",
            ],
            "lines": [
                "Hobbes: not c; b needs c; f needs b; so not f",
                "not c and b needs c give not b; f needs b gives not f",
                "valid: no row has all premises true and f true",
                "trust: c holds instead of not c",
                "row c, b, f all true: premises true, conclusion false",
                "so with a covenant, the argument no longer follows",
            ],
            "after": [
                "Valid does not mean true. Hobbes's argument is valid, and so is the "
                "reasoning of anyone who denies his first premise and draws a different "
                "conclusion from it. The disagreement is over whether the sovereign is "
                "party to a covenant, and over that premise the lab has nothing to say.",
            ],
        },
        "quiz_title": "The covenant that is not made",
        "quiz": [
            {"q": "Counting the ordinals from &ldquo;First&rdquo; to &ldquo;Lastly&rdquo;, how "
                  "many rights of the sovereign does Chapter 18 list?",
             "a": ["Seven", "Ten", "Eleven", "Twelve"],
             "c": 3,
             "why": "First through Eleventhly are eleven, and the chapter's twelfth, the "
                    "right to give titles of honour, is introduced with &ldquo;Lastly&rdquo;."},
            {"q": "Why does Hobbes say no breach of covenant can happen on the sovereign's "
                  "part?",
             "a": ["He is above the laws of nature",
                   "He is not a party to the covenant: it is made only of each with each",
                   "Subjects have promised never to judge him",
                   "A sovereign's covenants are made with God and not with men"],
             "c": 1,
             "why": "The right is given &ldquo;by Covenant onely of one to another, and "
                    "not of him to any of them&rdquo;. Hobbes does not say the sovereign "
                    "is above the laws of nature, since he may &ldquo;commit "
                    "Iniquity&rdquo;, nor does he say subjects promise never to judge him."},
            {"q": "In the trust preset the premises are `c`, `b -> c` and `f -> b`, and "
                  "the conclusion is `~f`. Which row makes every premise true and the "
                  "conclusion false?",
             "a": ["`c` true, `b` false, `f` false",
                   "`c` false, `b` true, `f` true",
                   "`c` true, `b` true, `f` true",
                   "`c` false, `b` false, `f` false"],
             "c": 2,
             "why": "The conclusion `~f` is false only when `f` is true, which needs `b` "
                    "true, which needs `c` true. In that row `c`, `b -> c` and `f -> b` "
                    "are all true. The other rows have `f` false, or make a premise false."},
            {"q": "On Hobbes's account, what may a sovereign who rules harshly commit?",
             "a": ["Injustice and injury, which subjects may charge him with",
                   "Neither iniquity nor injustice, since the sovereign can do no wrong",
                   "Iniquity, but not injustice or injury in the proper signification",
                   "Injury, but not iniquity"],
             "c": 2,
             "why": "&ldquo;they that have Soveraigne power, may commit Iniquity; but not "
                    "Injustice, or Injury in the proper signification.&rdquo; Because every "
                    "subject is author of what he does, a complaint of injury is "
                    "a complaint against oneself."},
        ],
        "mistakes": [
            ("Thinking that the sovereign promises to rule well and may be deposed if he fails",
             "In Hobbes's argument he can make no such covenant: not with the multitude, "
             "who are not yet one person, and not with each severally, since any claimed "
             "breach would be the act of every one of them. The lab's first preset "
             "shows the conclusion following once that premise stands. That is why a "
             "critic who wants a right of removal denies the premise instead."),
            ("Thinking that a valid argument is a sound one",
             "The lab finds Hobbes's argument valid, and it finds the trust argument "
             "invalid. That tells you which premise carries the dispute, `c`, and "
             "nothing about which side is right."),
            ("Reading no injury as no wrong",
             "The fourth right says the sovereign cannot do injury to a subject, because "
             "the subject is author of his acts. Hobbes writes in the same sentence that "
             "he may commit iniquity, which is wrong done against the laws of nature, "
             "though not against a subject in the proper sense."),
        ],
        "standard": (
            "Finish when you can set out the argument from the covenant and say what denies it.",
            "Write the argument that the sovereign cannot forfeit his power as premises, "
            "show that it is valid, and name the premise that a critic who allows "
            "removal would deny."
        ),
        "note": (
            "The lab checks form, and Hobbes's argument is valid. Whether the sovereign "
            "is party to a covenant, whether a trust is a covenant, and whether "
            "the miseries of a sovereign's rule are less than those of civil war are "
            "what the book argues and Locke and others disputed, and no table settles "
            "them."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Leviathan ch. 19, 1651 p. 95 (not shown in the margin); PDF p. 225 (the
    # three kinds); PDF p. 226 (tyranny and oligarchy); PDF p. 227-228 (the
    # comparison); PDF p. 230 (limited kings).
    {
        "slug": "kinds-of-commonwealth",
        "title": "The Several Kinds of Commonwealth",
        "module": "Chapter 19 · Of the severall Kinds of Common-wealth",
        "one_line": "There are three kinds of commonwealth, by who holds the sovereignty, and Hobbes ranks them not by power but by their aptitude to produce peace, preferring monarchy for reasons that include an assembly's inconstancy from number.",
        "summary": (
            "Chapter 19 sorts commonwealths by their representative, one, all or a part, "
            "treats tyranny and oligarchy as names of dislike, and compares monarchy with "
            "assemblies. Hobbes's inconstancy of assemblies is about who happens to be "
            "present; a majority vote can also depend on the order of the questions, which "
            "a later writer found, and the lab shows the second on a stated profile of "
            "nine voters."
        ),
        "key": [
            "kinds: representer one, all, or a part",
            "tyranny, oligarchy: names of dislike",
            "the kinds differ in aptitude, not power",
            "assemblies: inconstancy from number",
            "a cycle: the winner depends on the order",
        ],
        "key_label": "Three kinds, and why not four",
        "concepts_intro": (
            "The first half of Chapter 19 does two things: it sorts, and it ranks."
        ),
        "concepts": [
            ("Three kinds",
             "The difference of commonwealths is the difference of the sovereign. The "
             "representative is one man, or an assembly of all who will come together, or "
             "an assembly of a part. These are monarchy, democracy and aristocracy, and "
             "Hobbes says there can be no other kind."),
            ("Names of dislike",
             "Tyranny, oligarchy and anarchy are not other forms: they are monarchy, "
             "aristocracy and democracy as seen by those displeased with them. The "
             "same form is called by one name when it is liked and another when it is not."),
            ("Convenience, not power",
             "The three do not differ in power, since sovereignty is the same wherever "
             "it lies, but in aptitude to produce peace and security. On that Hobbes "
             "compares monarchy with assemblies under six heads."),
        ],
        "read_title": "The passage first, then the comparison point by point",
        "read_intro": (
            "The classification comes first. Hobbes then explains away the other names, "
            "and gives six comparisons, two of which the lab takes up."
        ),
        "body": [
            ("p", "<strong>Chapter 19.</strong> &ldquo;When the Representative is One man, "
                  "then is the Common-wealth a MONARCHY: when an Assembly of All that will "
                  "come together, then it is a DEMOCRACY, or Popular Common-wealth: when an "
                  "Assembly of a Part onely, then it is called an ARISTOCRACY. Other kind of "
                  "Common-wealth there can be none: for either One, or More, or All, must "
                  "have the Soveraign Power (which I have shewn to be indivisible) "
                  "entire.&rdquo;"),
            ("p", "The proof is short, and it uses what Chapter 18 has just established. "
                  "If the sovereignty is indivisible, it is held by one man or by more, and "
                  "if by more, by all who may enter or by some only. Aristotle had made "
                  "six kinds, three right and three corrupt; Hobbes keeps three names, "
                  "monarchy, aristocracy and democracy, and treats tyranny, oligarchy and "
                  "anarchy as the same three misliked: &ldquo;they are not the names of other Formes "
                  "of Government, but of the same Formes misliked&rdquo;. Those discontented "
                  "under monarchy call it tyranny, and &ldquo;they that are displeased with "
                  "Aristocracy, called it Oligarchy&rdquo;, and those grieved under a "
                  "democracy call it anarchy, though he thinks no man believes that want "
                  "of government is a new kind of government. You know the pattern from "
                  "ordinary life: the same colleague is decisive when you agree with "
                  "him and bossy when you do not."),
            ("p", "The same rule dissolves the mixed forms. A king whose power is limited "
                  "is not sovereign, &ldquo;he that is not superiour, is not supreme; that "
                  "is to say not Soveraign&rdquo;, and the sovereignty was always with "
                  "whoever had the right to limit him, as in Sparta, where the kings led "
                  "the armies and the Ephori held the sovereignty. An elective king is "
                  "either a hereditary one, if he may name his successor, or a minister "
                  "of whoever can. In 1642 the king's own answer to Parliament's Nineteen "
                  "Propositions had described England's government as a mixture of king, "
                  "lords and commons, and Chapter 18 has told you what Hobbes thought "
                  "had come of believing it."),
            ("p", "He says the three differ not in power but &ldquo;in the difference of "
                  "Convenience, or Aptitude to produce the Peace, and Security of the "
                  "people&rdquo;, and compares monarchy with assemblies, in six points. The "
                  "first is interest: whoever bears the person of the people also bears "
                  "his own natural person, and where the public and private interest "
                  "are &ldquo;most closely united, there is the publique most "
                  "advanced&rdquo;, which in a monarchy they are, since a king is rich only "
                  "when his subjects are. The second is counsel: a monarch hears whom he "
                  "pleases, and an assembly only its own members. The fifth and sixth are "
                  "favourites and infant kings. The third and fourth are the ones the "
                  "lab takes, since they are about numbers."),
            ("p", "The third: the resolutions of a monarch are subject to no inconstancy "
                  "but that of human nature, while &ldquo;in Assemblies, besides that of "
                  "Nature, there ariseth an Inconstancy from the Number&rdquo;. The "
                  "mechanism he gives is attendance: the absence of a few who would keep "
                  "the resolution firm, or the diligent appearance of a few of the "
                  "contrary opinion, &ldquo;undoes to day, all that was concluded "
                  "yesterday&rdquo;. Nine members vote five to four for a motion on Monday. "
                  "On Tuesday two of the five are away, and the same motion fails, three to "
                  "four. That is a counting fact about any body that votes."),
            ("p", "The fourth is that &ldquo;a Monarch cannot disagree with himselfe, out "
                  "of envy, or interest; but an Assembly may&rdquo;, to the height of civil "
                  "war. Here is a different way for an assembly to disagree with itself, "
                  "which Hobbes does not describe, and which the Marquis de Condorcet "
                  "found a century and a third later. Take nine voters on three proposals, "
                  "a wall, a fleet and an army. Four of them want the wall first, then the "
                  "fleet, then the army; three want the fleet first, then the army, then the "
                  "wall; two want the army first, then the wall, then the fleet. In the "
                  "preset <em>cycle</em> the lab finds that the wall beats the fleet six "
                  "to three, the fleet beats the army seven to two, and the army beats "
                  "the wall five to four. No proposal beats both of the others."),
            ("p", "What is the assembly's will then? It depends on the order in which "
                  "the questions are put. Vote wall against fleet first, and the winner "
                  "against the army: the wall wins the first round and loses to the army. "
                  "Vote fleet against army first and then the winner against the wall: "
                  "the fleet wins the first and loses to the wall. Vote army against wall "
                  "first, then the winner against the fleet: the army wins the first and "
                  "loses to the fleet. Each proposal wins under one of the three orders, "
                  "and whoever sets the agenda picks the outcome. This is the lab's finding, "
                  "not Hobbes's, and in his chapter the inconstancy is the attendance "
                  "kind. The preset <em>settled</em> changes the "
                  "rankings of two of the nine voters, and now the fleet beats each of the "
                  "others and is the winner whatever the order. The panel's rule menu "
                  "shows that the rule matters as well: on the cycle profile, plurality "
                  "gives the wall, with four first places to the fleet's three and the "
                  "army's two, and the Borda count ties the wall and the fleet at ten "
                  "points each."),
            ("p", "A reader who prefers assemblies has an answer to each of these points, "
                  "and republicans of Hobbes's own time, Milton among them, "
                  "gave it: rule by one man leaves a nation at the mercy of one man's "
                  "will, and an assembly of many is the safer trustee. Hobbes's reply is in "
                  "his first point: the passions of men are &ldquo;commonly more potent "
                  "than their Reason&rdquo;, so it matters where public and private "
                  "interest are joined. The lab counts votes and cannot say which of "
                  "them is right."),
            ("p", "So the three kinds are fixed, and every commonwealth, mortal like "
                  "the men who govern it, needs a way to continue. The next lesson, "
                  "&ldquo;The Right of Succession&rdquo;, takes the second half of "
                  "Chapter 19, and the question of who comes after a monarch."),
        ],
        "lab": ("choicekit", {
            "mode": "vote",
            "rule": "condorcet",
            "preset": "cycle",
            "presets": [
                {"id": "cycle", "label": "Nine voters, three proposals, a cycle",
                 "kind": "ranking",
                 "profile": [
                     {"count": 4, "rank": "wall fleet army"},
                     {"count": 3, "rank": "fleet army wall"},
                     {"count": 2, "rank": "army wall fleet"},
                 ],
                 "expect": {"voWinner": "none", "voCondorcet": "cycle: army > wall > fleet > army"}},
                {"id": "settled", "label": "Two voters change their order, and a winner appears",
                 "kind": "ranking",
                 "profile": [
                     {"count": 4, "rank": "wall fleet army"},
                     {"count": 3, "rank": "fleet army wall"},
                     {"count": 2, "rank": "army fleet wall"},
                 ],
                 "expect": {"voWinner": "fleet", "voCondorcet": "fleet"}},
            ],
            "panel_title": "What nine voters' majorities say",
            "panel_intro": (
                "Each row is a group of voters and their ranking from best to worst. The "
                "lab compares every pair of proposals by majority. Change the rule to "
                "plurality or Borda, or remove a proposal, and see whether the winner "
                "depends on the way the votes are taken."
            ),
        }),
        "steps_title": "Telling whether an assembly's resolution is stable",
        "steps_intro": "Four steps, in this order.",
        "steps": [
            ("List the voters' rankings",
             "Write each group of voters with the proposals in the order they prefer, "
             "best first, and the number in the group."),
            ("Compare each pair by majority",
             "For two proposals, count the voters who put one above the other. The "
             "larger count wins that pair."),
            ("Look for a proposal that beats every other",
             "If one does, it wins whatever the order. If none does, and each is "
             "beaten by another, the winner depends on the order of the questions."),
            ("Compare with absence",
             "Hobbes's inconstancy is that the same voters, differently present, give "
             "a different answer. Remove a member or two and recount."),
        ],
        "worked": {
            "title": "A wall, a fleet and an army",
            "intro": [
                "Nine voters in three groups, as in the preset <em>cycle</em>. The "
                "figures are an example written for the lesson.",
            ],
            "lines": [
                "wall over fleet: 4 + 2 = 6 against 3",
                "fleet over army: 4 + 3 = 7 against 2",
                "army over wall: 3 + 2 = 5 against 4",
                "wall, fleet, army, wall: no winner beats both",
                "order fleet-army, then wall: wall wins",
                "order wall-fleet, then army: army wins",
            ],
            "after": [
                "Each of the three proposals wins under one of the three possible orders of "
                "voting. Hobbes's own point is the simpler one, that two absences can turn "
                "5 to 4 into 3 to 4, and the cycle is a second way that a majority "
                "can contradict itself.",
            ],
        },
        "quiz_title": "Kinds and inconstancy",
        "quiz": [
            {"q": "On Hobbes's account, what is oligarchy?",
             "a": ["A fourth kind of commonwealth, in which the few rule for their own gain",
                   "Aristocracy, as those displeased with it call it",
                   "Monarchy, as those discontented under it call it",
                   "Democracy, as those grieved under it call it"],
             "c": 1,
             "why": "&ldquo;they that are displeased with Aristocracy, called it "
                    "Oligarchy.&rdquo; Tyranny is monarchy misliked, and anarchy is democracy "
                    "misliked. Hobbes denies any fourth kind."},
            {"q": "In the preset cycle, which proposal beats the wall in a straight vote "
                  "of the nine?",
             "a": ["The army, five to four", "The fleet, six to three",
                   "Both the fleet and the army", "Neither"],
             "c": 0,
             "why": "Groups of 3 and 2 put the army above the wall, which is five against "
                    "the 4 of the first group. The wall beats the fleet, so the fleet "
                    "does not beat the wall, and the army beats it."},
            {"q": "In the same preset, the fleet and the army are voted on first, and the "
                  "winner is then voted against the wall. Which proposal is chosen?",
             "a": ["The fleet", "The army", "No proposal", "The wall"],
             "c": 3,
             "why": "The fleet beats the army seven to two, and the wall then beats the "
                    "fleet six to three. With the other two orders the army or the fleet "
                    "wins, so the order decides."},
            {"q": "What is the inconstancy of assemblies that Hobbes names?",
             "a": ["Members' rankings of the proposals form a cycle",
                   "An assembly always takes longer than a monarch to reach a decision",
                   "A sovereign assembly may be dissolved by its members at pleasure",
                   "The absence of a few, or the diligent appearance of a few of "
                   "the contrary opinion, undoes to day what was concluded yesterday"],
             "c": 3,
             "why": "Hobbes: &ldquo;the absence of a few&rdquo; or &ldquo;the diligent "
                    "appearance of a few of the contrary opinion, undoes to day, all that "
                    "was concluded yesterday&rdquo;. The cycle is a later finding, and "
                    "Hobbes does not say the other two."},
        ],
        "mistakes": [
            ("Thinking that tyranny and oligarchy are further kinds of commonwealth",
             "Hobbes says they are the same forms misliked, and that they do not "
             "differ in power from the forms they name. A commonwealth is one of "
             "three kinds by where the sovereignty is, whatever its subjects feel "
             "about it."),
            ("Thinking that Hobbes's inconstancy is the cycle",
             "His inconstancy &ldquo;from the Number&rdquo; is about who is present. The cycle "
             "in the lab is a different failure, in which the same voters give no single "
             "winner and the order of voting settles the outcome. They are alike in "
             "showing a majority is not a stable will, and the lesson keeps them apart."),
            ("Thinking a cycle shows that assemblies are worse than monarchs",
             "The lab shows that a cycle can occur in a body of three groups. It does not "
             "show how often, nor that a monarch's will is more stable in the ways "
             "that matter: Hobbes's other points, interest, counsel and favourites, are "
             "not counted here."),
        ],
        "standard": (
            "Finish when you can tell whether a set of rankings gives an assembly a winner.",
            "Given the rankings of a small assembly on three proposals, compare each pair "
            "by majority, say whether one proposal beats both others, and if none does, "
            "show two orders of voting with different winners."
        ),
        "note": (
            "The cycle is a feature of the profile this lesson wrote, and the lab does not "
            "say how often real assemblies face one. Hobbes's inconstancy is of attendance, "
            "and the comparison of monarchy with assemblies rests on points about "
            "interest and counsel that no count of votes can settle."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Leviathan ch. 19, 1651 p. 100-101; PDF p. 231 (the artificial eternity,
    # who disposes); PDF p. 232 (words or testament); PDF p. 233 (custom and
    # the presumptions).
    {
        "slug": "the-right-of-succession",
        "title": "The Right of Succession",
        "module": "Chapter 19 · Of the severall Kinds of Common-wealth",
        "one_line": "The present monarch disposes of the succession, by express words, by testament or by tacit signs, and where he has left none the law of nature presumes his own child, then his nearer kin.",
        "summary": (
            "Hobbes calls the right of succession an artificial eternity, without which "
            "every commonwealth would fall back into war at its sovereign's death. Given a "
            "royal family, compute who succeeds with and without a testament, with and "
            "without a custom, and who is next if the heir dies, on Hobbes's presumptions "
            "as the lab states them."
        ),
        "key": [
            "succession: the commonwealth's eternity",
            "the present monarch disposes of it",
            "words and testament first, then custom",
            "then: own child, male before female",
            "then: the nearer in blood before the remoter",
        ],
        "key_label": "Who comes after the king",
        "concepts_intro": (
            "The second half of Chapter 19 answers a question the first half leaves "
            "open: when a sovereign dies, what keeps the commonwealth from dying with him?"
        ),
        "concepts": [
            ("An artificial eternity",
             "A commonwealth is an artificial man, and since its matter is mortal it "
             "needs an &ldquo;Artificiall Eternity&rdquo;, which men call the right of "
             "succession. Without it a people governed by one man would fall back into "
             "the condition of war when he dies."),
            ("The present sovereign disposes of it",
             "If the right lay in any other man or private assembly it would be in a "
             "subject, and could be taken by the sovereign. If it lay with the "
             "multitude it would be a return to war. So in a monarchy the disposing "
             "of the successor is always left to the judgment and will of the present "
             "possessor."),
            ("How his will is known",
             "By express words or testament; failing that, by a custom he has not "
             "controlled, since what a man could forbid with a word and does not he "
             "is taken to allow; failing both, by natural presumption."),
        ],
        "read_title": "The passage first, then the right of succession in order",
        "read_intro": (
            "The presumptions come first, because they are the part the lab computes. "
            "The paragraphs before them say why the right belongs to the present monarch "
            "and how he declares it."
        ),
        "body": [
            ("p", "<strong>Chapter 19.</strong> &ldquo;But where neither Custome, nor "
                  "Testament hath preceded, there it is to be understood, First, that a "
                  "Monarchs will is, that the government remain Monarchicall; because he "
                  "hath approved that government in himselfe. Secondly, that a Child of "
                  "his own, Male, or Female, be preferred before any other; because men "
                  "are presumed to be more enclined by nature, to advance their own "
                  "children, than the children of other men; and of their own, rather a "
                  "Male than a Female; because men, are naturally fitter than women, for "
                  "actions of labour and danger.&rdquo;"),
            ("p", "That is the last step of a ladder, and the ladder starts a page "
                  "earlier with the problem. Governments are mortal, &ldquo;so that not "
                  "onely Monarchs, but also whole Assemblies dy&rdquo;, and as there was "
                  "order taken for an artificial man, so there must be order taken for "
                  "&ldquo;an Artificiall Eternity of life&rdquo;. Think of it as a "
                  "company's articles saying who runs the firm when the founder dies. "
                  "In a democracy the question does not arise, since the whole assembly "
                  "cannot fail unless the multitude fails. In an aristocracy, when a "
                  "member dies the assembly elects another, as the sovereign that "
                  "chooses all its officers. The &ldquo;greatest difficultie&rdquo; is in "
                  "monarchy, where it is not manifest who appoints the successor, nor "
                  "many times whom he has appointed, and &ldquo;there is required a more "
                  "exact ratiocination, than every man is accustomed to use&rdquo;."),
            ("p", "Who appoints? Either the present holder has the right, or it returns "
                  "to the dissolved multitude. The second cannot be, Hobbes argues: the "
                  "death of the sovereign &ldquo;leaves the Multitude without any "
                  "Soveraign at all&rdquo;, so they are without any representative and "
                  "incapable of any one action, with &ldquo;every man having equall right "
                  "to submit himselfe to such as he thinks best able to protect him&rdquo;, "
                  "which is the war of every man against every man again. &ldquo;Therefore "
                  "it is manifest, that by the Institution of Monarchy, the disposing of "
                  "the Successor, is alwaies left to the Judgment and Will of the present "
                  "Possessor.&rdquo; His first sentence on the question says as much: "
                  "&ldquo;There is no perfect forme of Government, where the disposing of "
                  "the Succession is not in the present Soveraign.&rdquo;"),
            ("p", "How is the will known? First, by express words or testament, declared "
                  "in his life, by word of mouth or by writing, as the first emperors of "
                  "Rome declared who should be their heirs. And the word heir &ldquo;does "
                  "not of it selfe imply the Children, or nearest Kindred of a man&rdquo;, "
                  "but whomever he declares. Second, where there is no testament, by "
                  "custom: where it is that the next of kindred succeeds, the next of kindred "
                  "has the right, because the monarch could have declared otherwise in his "
                  "life; &ldquo;whatsoever Custome a man may by a word controule, and does "
                  "not, it is a naturall signe he would have that Custome stand&rdquo;. The "
                  "same goes for a custom of the male line, and for one that advances the "
                  "female."),
            ("p", "Only when neither has preceded do the presumptions apply, and "
                  "they are three, as the opening passage and the sentence after it "
                  "give them. The government stays a monarchy. A child of his own, "
                  "male or female, is preferred to anyone else, and of his own rather a "
                  "male than a female. And where his own issue fails, &ldquo;rather a "
                  "Brother than a stranger; and so still the neerer in bloud, rather than "
                  "the more remote&rdquo;, because the nearer of kin is presumed the nearer "
                  "in affection. The reasons are Hobbes's, and a modern reader will "
                  "weigh the one about men and women for what it is, an opinion of 1651 "
                  "stated as a presumption about what a monarch would have wanted. The "
                  "lab applies the order and does not endorse the reason."),
            ("p", "The lab has to add two things Hobbes does not say in this passage, "
                  "and says that it has. Among a monarch's children it puts the elder "
                  "before the younger of the same sex, and where a child has died it "
                  "lets that child's own children stand in his place before the next "
                  "child. These are the kit's reading of what natural affection "
                  "implies, not Hobbes's words, and the lesson's quiz stays with what "
                  "he wrote."),
            ("p", "Take a royal family. The king has a brother, the duke, who has a son; "
                  "the king has three children, a prince, a princess and a younger son. In "
                  "the preset <em>no-testament</em> there is no testament and no custom, "
                  "and the lab names the prince, the king's eldest male child, then the "
                  "younger son, then the princess, then the duke, the king's brother, then "
                  "the duke's son. In <em>testament</em> the king has named his nephew, the "
                  "duke's son, in writing: the lab names the nephew and the rule, express "
                  "words, over the king's own children. In <em>eldest-dead</em> the prince "
                  "has died without issue and the younger son succeeds, because a male "
                  "child is preferred to a female."),
            ("p", "The last two presets use a second family, in which the king has a daughter "
                  "and a brother and no son. In <em>daughter-only</em> there is neither "
                  "custom nor testament, and the daughter succeeds: a child of his own, "
                  "male or female, is preferred to any other. In <em>male-line</em> the "
                  "kingdom has the custom that only males succeed, through males, and the "
                  "king has not controlled it, so the brother succeeds, which is "
                  "Hobbes's rule that a custom the monarch might forbid and does not "
                  "stands."),
            ("p", "At the end of the chapter Hobbes anticipates the usual objection, "
                  "that if a monarch may give the kingdom by testament he may give it to "
                  "a stranger, who will oppress the people, since strangers &ldquo;commonly "
                  "undervalue one another&rdquo;. He answers that this arises not from "
                  "subjection to a stranger but from the unskilfulness of governors, and "
                  "that the same may come by marriage, which all men account lawful. He "
                  "points to the Romans, who took the sting from conquest by giving "
                  "the conquered the name of Romans, and says this was what &ldquo;our "
                  "most wise King James&rdquo; aimed at in seeking the union of England and "
                  "Scotland. In 1651 the question of "
                  "succession was not a seminar. Charles I had been executed two years "
                  "before, and his son had been crowned in Scotland that January."),
            ("p", "The lab computes who succeeds on the order Hobbes gives, and the "
                  "text itself says the order can be overridden at any moment by the "
                  "monarch's word. It cannot tell you whether a monarch should "
                  "prefer his own children, or whether the reasons Hobbes gives are "
                  "good ones. Part II goes on from here to Chapter 20, and the "
                  "next course, &ldquo;Dominion, Liberty and the Parts of a "
                  "Commonwealth&rdquo;, begins with the second way a commonwealth is "
                  "made, by acquisition."),
        ],
        "lab": ("levkit", {
            "mode": "succession",
            "view": "heir",
            "preset": "no-testament",
            "monarch": "king",
            "people": (
                "father, -, m, 1, no; king, father, m, 2, yes; duke, father, m, 3, yes; "
                "prince, king, m, 4, yes; princess, king, f, 5, yes; "
                "cadet, king, m, 6, yes; nephew, duke, m, 7, yes"
            ),
            "presets": [
                {"id": "no-testament", "label": "A king, three children and a brother, with no testament",
                 "expect": {"lsuSuccessor": "prince", "lsuRule": "presumption: the monarch's own issue", "lsuLine": "1 prince; 2 cadet; 3 princess; 4 duke; 5 nephew"}},
                {"id": "testament", "label": "The king names his nephew in writing",
                 "named": "nephew", "expect": {"lsuSuccessor": "nephew", "lsuRule": "testament: named by express words", "lsuWithout": "prince"}},
                {"id": "eldest-dead", "label": "The eldest son has died without issue",
                 "people": (
                     "father, -, m, 1, no; king, father, m, 2, yes; duke, father, m, 3, yes; "
                     "prince, king, m, 4, no; princess, king, f, 5, yes; "
                     "cadet, king, m, 6, yes; nephew, duke, m, 7, yes"
                 ),
                 "expect": {"lsuSuccessor": "cadet", "lsuLine": "1 cadet; 2 princess; 3 duke; 4 nephew"}},
                {"id": "daughter-only", "label": "A king with a daughter and a brother, no son",
                 "people": (
                     "father, -, m, 1, no; king, father, m, 2, yes; duke, father, m, 3, yes; "
                     "princess, king, f, 4, yes"
                 ),
                 "expect": {"lsuSuccessor": "princess", "lsuLine": "1 princess; 2 duke"}},
                {"id": "male-line", "label": "The same family, with a custom that only males succeed",
                 "people": (
                     "father, -, m, 1, no; king, father, m, 2, yes; duke, father, m, 3, yes; "
                     "princess, king, f, 4, yes"
                 ),
                 "custom": "male-line", "expect": {"lsuSuccessor": "duke", "lsuRule": "custom (male-line): the first male of the blood through males", "lsuPresumption": "princess"}},
            ],
            "panel_title": "Who succeeds the king",
            "panel_intro": (
                "Each line names a person, the parent, the sex, the birth order (smaller is "
                "elder) and whether he or she is alive. The lab applies a testament if there "
                "is one, then a custom, then Hobbes's presumptions, and lists the line of "
                "succession."
            ),
        }),
        "steps_title": "Finding the successor",
        "steps_intro": "Four questions in Hobbes's order. The first that answers decides.",
        "steps": [
            ("Is there express word or testament?",
             "If the monarch declared an heir, by speech or writing, that person "
             "succeeds, whoever he is."),
            ("Is there a custom he has not controlled?",
             "A custom that the next of kindred succeeds, or the next of the male "
             "kindred, stands because he could have forbidden it with a word."),
            ("Apply the presumptions",
             "A child of his own before any other, a male before a female, and "
             "where his issue fails, the nearer in blood before the more remote."),
            ("Check who is alive",
             "Strike anyone who has died, and see who the same rules then name."),
        ],
        "worked": {
            "title": "A king, his children and his brother",
            "intro": [
                "A king has a prince, a princess and a younger son, and a brother with a son. "
                "The family is an example written for the lesson.",
            ],
            "lines": [
                "no testament, no custom: presumptions",
                "his own children before any other: the three",
                "male before female: the princes before the princess",
                "the prince, the king's elder son, succeeds",
                "prince dies without issue: the younger son",
                "no children at all: his brother, then the nephew",
            ],
            "after": [
                "The first four lines are the preset <em>no-testament</em>, the fifth is "
                "<em>eldest-dead</em>. If the king had named the nephew in writing, the "
                "list above would not matter: the testament comes first. The last line "
                "is not a preset, but you reach it by marking the king's children dead "
                "in the box.",
            ],
        },
        "quiz_title": "Words, custom and presumption",
        "quiz": [
            {"q": "A king has a daughter and a living brother, has left no testament, and "
                  "there is no custom. On Hobbes's presumptions, who succeeds?",
             "a": ["His brother, who is a man",
                   "Nobody: a daughter cannot succeed",
                   "Whoever the people choose",
                   "The daughter, because a child of his own is preferred before any other"],
             "c": 3,
             "why": "&ldquo;a Child of his own, Male, or Female, be preferred before "
                    "any other&rdquo;: the preference for a male is among his own children, "
                    "not between his children and his brother."},
            {"q": "A king has a son and names his nephew heir in writing. Who succeeds?",
             "a": ["The nephew, because the word heir does not of itself imply the "
                   "children, but whomever the monarch declares",
                   "The son, because natural affection overrides a testament",
                   "Whichever the nobles prefer",
                   "Nobody, because the succession returns to the multitude"],
             "c": 0,
             "why": "Hobbes: &ldquo;the word Heire does not of it selfe imply the "
                    "Children, or nearest Kindred of a man; but whomsoever a man shall any "
                    "way declare&rdquo;. The presumptions apply only where neither custom "
                    "nor testament has preceded."},
            {"q": "Why does Hobbes say the right to dispose of the succession belongs to the "
                  "present monarch?",
             "a": ["Because monarchs are chosen by God",
                   "Because a monarch's son is always the best ruler",
                   "Because otherwise the right falls to the dissolved multitude, which can "
                   "do no act and returns to the war of every man against every man",
                   "Because assemblies cannot be trusted to hold elections"],
             "c": 2,
             "why": "The death of a sovereign leaves the multitude &ldquo;without any "
                    "Soveraign at all&rdquo;, incapable of electing, so the right "
                    "has to be in the present holder. The chapter does not argue from "
                    "God's choice, from a son's merit or from the untrustworthiness "
                    "of assemblies."},
            {"q": "There is a custom that the next of the male kindred succeeds, and "
                  "the monarch has never controlled it. Why does Hobbes say the next "
                  "male kin has the right?",
             "a": ["Because custom is law whatever the monarch thinks",
                   "Because males are naturally fitter for actions of labour and danger",
                   "Because a custom a man could control with a word and does not "
                   "is a natural sign he would have it stand",
                   "Because the multitude has accepted it"],
             "c": 2,
             "why": "&ldquo;whatsoever Custome a man may by a word controule, and does not, "
                    "it is a naturall signe he would have that Custome stand.&rdquo; The "
                    "fitness of males is the reason for a presumption when no custom exists, "
                    "not for a custom."},
        ],
        "mistakes": [
            ("Thinking that the eldest son has a right independent of the king's will",
             "On Hobbes's account the succession is always left to the judgment and will "
             "of the present monarch. The presumptions, a child before any other, "
             "male before female, are what his will is taken to be when he has "
             "left no words and no custom. A testament naming the nephew overrides "
             "them all."),
            ("Reading the presumptions as a law of primogeniture",
             "The text says a child of his own, male or female, before any other, and of "
             "his own rather a male than a female, and then the nearer in blood. It "
             "does not say elder before younger in this passage; the lab adds that, and "
             "says so."),
            ("Thinking Hobbes gives the people a share in choosing the successor",
             "He argues the reverse: if it were left to a new choice, the "
             "commonwealth would be dissolved and the right would be in whoever can "
             "get it, contrary to the intention of those who instituted it for "
             "perpetual security."),
        ],
        "standard": (
            "Finish when you can name the successor and the rule that chose him.",
            "Given a royal family, a monarch, and whether there is a testament or a "
            "custom, name the successor and say whether the testament, the custom or "
            "a presumption chose him, and who follows if he dies."
        ),
        "note": (
            "The lab applies the order Hobbes states, with two additions it names, to a "
            "family written for the lesson. It cannot say whether the reasons he gives "
            "for the presumptions are good, and the one about men and women is an opinion "
            "of its time stated as a presumption about what a king would want."
        ),
    },
]
