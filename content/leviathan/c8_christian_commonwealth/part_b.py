"""Course 8, lessons 5-8 -- Part III, Chapters 37 to 43.

Every quotation is copied from the operator's copy of the 1651 text (Tuck's
Cambridge edition keeps Hobbes's spelling); the comment beside each lesson
gives its chapter and page. Italics are dropped, nothing else is changed.
"""

def _case(name, values, verdict):
    return {"name": name, "values": values, "verdict": verdict}


# ------------------------------------------------------------------ 05
# Leviathan ch. 37, 1651 p. 235; PDF p. 399 of the operator's copy.
L5 = {
    "slug": "miracles-and-their-use",
    "title": "Miracles and Their Use",
    "module": "Chapter 37 · Of Miracles, and their Use",
    "one_line": "A miracle is strange and has no known natural cause, it is relative to the spectator, and a wonder alone cannot tell you whether it was God, a trick or a mistake.",
    "summary": (
        "Chapter 37 defines a miracle, says what makes men wonder, shows that the same "
        "event may be a miracle to one man and not to another, and warns how easily "
        "men are deceived by wonders. Treat a reported wonder as a choice between "
        "three explanations, miracle, trick and honest mistake, and see what witnesses "
        "do and do not change."
    ),
    "key": [
        "miracle: strange, no natural cause known",
        "a miracle is relative to the spectator",
        "its end: to credit God's messenger",
        "a witness who says it either way: factor 1",
        "the sovereign's church judges, not each man",
    ],
    "key_label": "Miracles in five lines",
    "concepts_intro": (
        "The chapter gives a definition and then works out what it implies for anyone "
        "who is told of a wonder."
    ),
    "concepts": [
        ("What makes a wonder",
         "Two things make men wonder at an event: that it is strange, so that the like "
         "has never or very rarely been produced, and that we cannot imagine it done by "
         "natural means but only by the immediate hand of God. A speaking horse is a "
         "miracle; a man begetting his like is not, though we know no more how it is "
         "done. The first rainbow was a miracle, and the rainbow today is not."),
        ("Relative to the spectator",
         "Wonder follows knowledge and experience, so the same thing may be a miracle to "
         "one man and not to another. Eclipses were supernatural to people who could "
         "not foretell them. And what is done by art, if we know how, we count no "
         "miracle. The definition is therefore about the work and the one who beholds "
         "it together."),
        ("Credit for messengers, and the danger of being deceived",
         "A miracle is wrought to give credit to God's messengers, so that men know "
         "they are sent. The magicians of Egypt, Hobbes argues, deceived and did "
         "not enchant anything: ventriloquists, jugglers and confederates can deceive "
         "men who are ignorant of natural causes. The caution is the one from "
         "Chapter 32, and the judge is the lawful head of the church."),
    ],
    "read_title": "The passage first, then the chapter line by line",
    "read_intro": (
        "The definition is Hobbes's own, and it is stricter than the word in "
        "everyday use: a miracle is not only a wonder but a wonder with a purpose."
    ),
    "body": [
        ("p", "<strong>Chapter 37.</strong> &ldquo;A MIRACLE, is a work of God, (besides "
              "his operation by the way of Nature, ordained in the Creation,) done, for the "
              "making manifest to his elect, the mission of an extraordinary Minister for "
              "their salvation.&rdquo;"),
        ("p", "Ask a friend whether they believe in miracles and you will usually hear about "
              "wonders: a recovery nobody expected, a coincidence too good to be chance. "
              "Hobbes starts there and then tightens the word. By miracles, he says, are "
              "signified the admirable works of God, which is why they are also called "
              "wonders, and signs when they accompany a commandment. To know what one "
              "is, we must know what men wonder at, and &ldquo;there be but two things "
              "which make men wonder at any event&rdquo;: that it is strange, and that "
              "we cannot imagine a natural means for it."),
        ("p", "The examples show how much the definition leaves to the observer. "
              "&ldquo;if a Horse, or Cow should speak, it were a Miracle&rdquo;, because "
              "the thing is strange and the natural cause hard to imagine. A man "
              "begetting a man is not, though we know no more how that is done, because "
              "it is usual. A man turned into a stone is a miracle and a piece of wood "
              "turned into stone is not, because we see it often. &ldquo;The first "
              "Rainbow that was seen in the world, was a Miracle, because the "
              "first&rdquo;, a sign to assure God's people there would be no more "
              "universal flood; rainbows now are not. Hobbes draws the conclusion "
              "himself: &ldquo;the same thing, may be a Miracle to one, and not to "
              "another&rdquo;. The ignorant take an eclipse for a supernatural work "
              "while those who can foretell the hour do not."),
        ("p", "Then the purpose. A miracle is wrought to procure credit for God's "
              "messengers, so that men know they are sent and are the better inclined to "
              "obey. For that reason the creation and the flood were admirable works, "
              "and not miracles in his sense, because they were not done to credit any "
              "prophet. He gives the plagues of Egypt as a standard case, and says "
              "the end of miracles was always to beget belief, not in all men, but in the "
              "elect: Pharaoh was not persuaded by them, he was forced by the plagues. "
              "Hence the definition you read first. Two consequences follow from it. "
              "The work is not the effect of any virtue in the prophet, since it is "
              "the immediate hand of God; and no devil, angel or other created spirit "
              "can do one, since what they do is by natural science or enchantment and "
              "so is not the immediate hand of God."),
        ("p", "That brings Hobbes to the passages that look as if enchanters can do "
              "wonders: the magicians who turned rods into serpents, waters to blood, and "
              "brought up frogs. His answer is that Scripture never says what "
              "enchantment is, and that words have no effect on anyone who does not "
              "understand them, and then only to signify intentions or passions. So "
              "when a rod seems a serpent, &ldquo;not the Rod, nor the Water, nor any "
              "other thing is enchanted&rdquo;; it is the spectator who is wrought upon. "
              "&ldquo;all the Miracle consisteth in this, that the Enchanter has "
              "deceived a man; which is no Miracle, but a very easie matter to "
              "doe.&rdquo; He lists the means: knowing the course of the stars before "
              "others do, a juggler's trinkets, ventriloquism, the confessions one man "
              "makes to another. And then the sharpest sentence in the chapter: "
              "&ldquo;there is nothing how impossible soever to be done, that is "
              "impossible to bee beleeved&rdquo;, if the impostures are done by "
              "confederacy. Two men conspiring, one to seem lame and the other to cure "
              "him, deceive many; many conspiring, with the rest to bear witness, "
              "deceive many more."),
        ("p", 'That is where the lab begins. A wonder is reported. Behind the '
              'report there may be a miracle, a trick or an honest mistake. '
              'Give each a share of all the reports there are: the lesson '
              'supposes, for illustration, one in a hundred a miracle, '
              'forty-nine in a hundred a trick and half mistakes. Now one '
              'witness says he saw it. If the three explanations would lead a '
              'witness to say so about equally often, the report cannot tell '
              'them apart. The preset <em>one-witness</em> has the miracle and '
              'the trick both producing a witness nine times in ten, and a '
              "mistake producing one only one time in ten. The miracle's share "
              'rises only from 1/100 to 9/500: what has been ruled out is the '
              'honest mistake, not the trick. Three witnesses do the same '
              "again, since the trick's witnesses are as many as the miracle's; "
              'and where the trick is by confederacy and its witnesses always '
              "say so, the miracle loses ground to the trick. That is Hobbes's "
              'point about confederacy put as a calculation. None of the rates '
              'is his, and he gives no probabilities.'),
        ("p", "Hobbes's advice follows. The caution God prescribed is the one from "
              "Deuteronomy: take for prophets none who teach another religion than the "
              "one that God's lieutenant has established, nor any whose prediction we "
              "do not see come to pass. Before we credit a pretended miracle we must "
              "both see it done and &ldquo;use all means possible to consider, whether "
              "it be really done&rdquo;, and whether it is such as no man could do by "
              "natural power. In every doubtful case we go to God's lieutenant, the head "
              "of the church. His example is aimed at the Roman doctrine of the mass: a "
              "man who says that after certain words a piece of bread is no longer "
              "bread but a God or a man, though it looks as like bread as it ever did, "
              "gives us no reason to think it done, until we inquire of the lieutenant. "
              "Hobbes goes on, &ldquo;If he say &rsquo;tis done, then he is not to "
              "contradict it&rdquo;, so that in a Catholic commonwealth the lieutenant's "
              "answer settles the matter. A Catholic reader would say the doctrine concerns what is not "
              "perceptible by the senses, and that is a fair statement of the other "
              "side; Hobbes's reply is that the test he gives requires the thing to "
              "be seen."),
        ("p", "The last lines carry the political weight. In these days, he says, he knows "
              "no one who has seen a wonder that a man of mediocre reason would think "
              "supernatural, so &ldquo;the question is no more, whether what wee see "
              "done, be a Miracle&rdquo; but &ldquo;whether the report be true, or a "
              "lye&rdquo;, and on that we are not each to follow our own private "
              "reason but &ldquo;the Publique Reason, that is, the reason of Gods "
              "Supreme Lieutenant&rdquo;. A private man keeps a liberty: &ldquo;A "
              "private man has alwaies the liberty, (because thought is free,) to "
              "beleeve, or not beleeve in his heart&rdquo;, though when it comes to "
              "confession, private reason submits to the public. A critic can say "
              "that this makes the sovereign the judge of what God has done. Hobbes "
              "says we have made him judge already by giving him the power to do what "
              "is needed for peace and defence. Later writers argued the matter on "
              "testimony instead: Hume, a century afterward, said no testimony is enough "
              "unless its being false would be more miraculous than what it reports. "
              "That is a different argument from Hobbes's, and a Bayesian would put "
              "the point in the prior, which in the lab is a number you can change."),
        ("p", 'The next lesson, <em>Eternal Life and the Church</em>, moves '
              'from what is to be believed about wonders to what Hobbes says '
              'Scripture means by eternal life and a church.'),
        ("p", 'The presets keep the same three explanations and add witnesses. In one- '
              'witness a single witness says he saw it, and the chance of a miracle is '
              '9/500, or 1.8%, because the trick and the mistake together are so much more '
              'likely at the start. In three-witnesses three independent witnesses raise it '
              'only to 729/36500, about 2%, since a trick produces witnesses as readily as '
              'a miracle does. In confederates the trick is made to produce witnesses every '
              'time, which favours the trick a little more, and the chance of '
              'a miracle falls to 81/5531, about 1.5%.'),
    ],
    "lab": ("choicekit", {
        "mode": "update",
        "preset": "one-witness",
        "presets": [
            {"id": "one-witness", "label": "one witness says he saw it",
             "hyps": ["miracle", "trick", "mistake"], "prior": ["1/100", "49/100", "1/2"],
             "outcomes": ["saw-it", "did-not"],
             "lik": [["9/10", "1/10"], ["9/10", "1/10"], ["1/10", "9/10"]],
             "data": ["saw-it"], "payoffs": None,
             "expect": {"upPost": "9/500", "upBF": "891/491", "upConf": "Confirms"}},
            {"id": "three-witnesses", "label": "three independent witnesses say they saw it",
             "hyps": ["miracle", "trick", "mistake"], "prior": ["1/100", "49/100", "1/2"],
             "outcomes": ["saw-it", "did-not"],
             "lik": [["9/10", "1/10"], ["9/10", "1/10"], ["1/10", "9/10"]],
             "data": ["saw-it", "saw-it", "saw-it"], "payoffs": None,
             "expect": {"upPost": "729/36500", "upBF": "72171/35771", "upConf": "Confirms"}},
            {"id": "confederates", "label": "three witnesses, and a trick whose witnesses are all confederates",
             "hyps": ["miracle", "trick", "mistake"], "prior": ["1/100", "49/100", "1/2"],
             "outcomes": ["saw-it", "did-not"],
             "lik": [["9/10", "1/10"], ["1", "0"], ["1/10", "9/10"]],
             "data": ["saw-it", "saw-it", "saw-it"], "payoffs": None,
             "expect": {"upPost": "81/5531", "upBF": "8019/5450", "upConf": "Confirms"}},
        ],
        "panel_title": "A reported wonder: miracle, trick or mistake",
        "panel_intro": (
            "The prior says how often, of all reports of a wonder, each explanation lies "
            "behind it; the likelihoods say how often each would lead a witness to say "
            "he saw it. All of it is the lesson's illustration. The menu at the foot of "
            "the controls chooses which explanation the tiles report; it starts on the "
            "miracle."
        ),
    }),
    "steps_title": "Weighing a reported wonder",
    "steps_intro": "Five steps, the same for any report.",
    "steps": [
        ("List the explanations",
         "Hobbes gives three: the immediate hand of God, deception by art or "
         "confederacy, and the ordinary ignorance and credulity of men. Name each."),
        ("Give each a prior",
         "Say how often, among the reports of wonders you have heard, each explanation "
         "was the true one. These figures are not in the chapter; they are the "
         "assumption you are testing."),
        ("Ask what each would produce",
         "For the report you have, say how likely each explanation would make it. A "
         "trick is designed to be reported, so its likelihood is high."),
        ("Update",
         "Multiply each prior by its likelihood and divide by the total. Compare the "
         "miracle's new share with its old one."),
        ("Ask what would separate them",
         "A report that all three explanations produce equally often leaves the shares "
         "where they were. Hobbes's remedy is a test that only one can pass: whether "
         "the thing can be done by natural power at all."),
    ],
    "worked": {
        "title": "One witness",
        "intro": [
            "Take the first preset. A report of a wonder is a miracle one time in a "
            "hundred, a trick 49 in a hundred, and a mistake the rest. A witness says he "
            "saw it.",
        ],
        "lines": [
            "miracle:  (1/100)·(9/10) = 9/1000",
            "trick:  (49/100)·(9/10) = 441/1000",
            "mistake:  (1/2)·(1/10) = 50/1000",
            "total:  500/1000 = 1/2",
            "miracle share:  (9/1000)/(1/2) = 9/500",
        ],
        "after": [
            "The miracle has gone from 1/100 to 9/500, which is 1.8 in a hundred; it is "
            "nearly where it began, and the trick has risen from 49 to 88.2 in a hundred. "
            "The witness removed the honest mistake, as the lab shows, and left the "
            "other two as they were in proportion.",
        ],
    },
    "quiz_title": "What a witness changes",
    "quiz": [
        {"q": "In the one-witness preset, why does the miracle's share barely move?",
         "a": [
               'Witnesses are never reliable',
               'A trick would produce a witness as often as a miracle would',
               'A miracle cannot be witnessed',
               'The prior for a miracle was zero',
         ],
         "c": 1,
         "why": 'The miracle and the trick each produce the witness nine times in ten, '
                'so the report does not separate them; only the mistake is made less '
                'likely. The other answers are not what the numbers say: the prior was '
                '1/100, and witnesses are reliable in the miracle row.'},
        {"q": 'Which of these does Hobbes say is needed beyond seeing a pretended '
              'miracle?',
         "a": [
               "To take the witness's word for it",
               'To pray for a sign',
               'To wait for a second prophet',
               'To consider whether it was really done and whether no man could do the like by natural power',
         ],
         "c": 3,
         "why": 'He says we must both see it done and use all means possible to '
                'consider whether it be really done, and whether it is such that no man '
                'could do the like by his natural power, and in doubtful cases to '
                "consult God's lieutenant. The others are not in the chapter."},
        {"q": "What is the difference, in Hobbes's definition, between a miracle and "
              'the creation of the world?',
         "a": [
               'A miracle is done to make manifest the mission of a minister of God',
               'A miracle is smaller',
               'Creation is not a work of God',
               "A miracle is always done by a prophet's own power",
         ],
         "c": 0,
         "why": 'He says the creation and the flood were admirable but not miracles in '
                'his sense, since not done to procure credit to any prophet. He also '
                'says a miracle is not the effect of any virtue in the prophet.'},
        {"q": 'How does Hobbes explain the works of the magicians of Egypt?',
         "a": [
               'As real miracles done by devils',
               "As done by a prophet's own power",
               'As deception of the spectator, not an enchanting of the thing',
               'As unrelated to the story of Moses',
         ],
         "c": 2,
         "why": "He says that if it is not to the edification of God's people, it is "
                'the spectator who is wrought upon, and all the miracle consists in the '
                'enchanter having deceived a man. He also denies that any devil can do '
                'a miracle.'},
    ],
    "mistakes": [
        ("Calling any wonder a miracle",
         "In Hobbes's definition a miracle is a work of God done to make manifest the "
         "mission of an extraordinary minister, so a coincidence or a natural rarity "
         "that nobody has explained is not one, and a thing known to be done by art "
         "is not one either."),
        ("Thinking more witnesses make a miracle likely",
         "Three witnesses remove the honest mistake and do nothing against a trick "
         "that produces witnesses. In the confederates preset the trick's share "
         "goes from 49/100 to nearly all, because its witnesses always say yes."),
        ("Reading the lab's probabilities as Hobbes's",
         "He says nothing of priors. He says wonders are relative to the spectator, "
         "that men are easily deceived and that the judgment belongs to the public "
         "reason. The numbers show the shape of that caution, and different priors "
         "give different results."),
    ],
    "standard": (
        "Finish when you can say what a witness does and does not change.",
        "Given priors for miracle, trick and mistake and the chance each would produce a "
        "witness, compute the posterior for each, and say which explanations the report "
        "fails to separate."
    ),
    "note": (
        "The priors and likelihoods are the lesson's, and the result is the whole of what "
        "the lab says. It cannot say how often real wonders are reported, whether a "
        "miracle's prior should be small, or whether the sovereign's judgement should "
        "settle what a subject professes; Hume, the Church of Rome and the "
        "Presbyterians would each answer those differently."
    ),
}

# ------------------------------------------------------------------ 06
# Leviathan ch. 39, 1651 p. 248; PDF p. 417 of the operator's copy.
L6 = {
    "slug": "eternal-life-and-the-church",
    "title": "Eternal Life and the Church",
    "module": "Chapters 38 and 39 · Of Eternall Life, Hell, Salvation, and of the Word Church",
    "one_line": "Hobbes reads eternal life as life on a restored earth and defines a church as a company of Christians united in one sovereign, so a Christian commonwealth and a church are one thing.",
    "summary": (
        'Chapter 38 asks what Scripture means by eternal life, hell, salvation '
        'and redemption, and places them mostly on earth after the '
        'resurrection. Chapter 39 lists the senses of church and defines one '
        'that can act as a person: a company of Christians united in one '
        'sovereign. Test that definition against a table of cases and see which '
        'it admits and which formula would fit.'
    ),
    "key": [
        "church = Christians + sovereign + authority",
        "no universal church that all are bound to obey",
        "a church that can act is a commonwealth",
        "eternal life: on earth, after the resurrection",
        "hell: a metaphor; the second death",
    ],
    "key_label": "Church and eternal life in five lines",
    "concepts_intro": (
        "These two chapters answer, in turn, what rewards and punishments are at "
        "stake in Christian obedience and what body can command it."
    ),
    "concepts": [
        ("Eternal life and torment, and why they are political",
         "Hobbes begins with an argument about sovereignty: a commonwealth cannot "
         "stand where anyone but the sovereign can give greater rewards than life or "
         "inflict greater punishments than death. Eternal life is a greater reward and "
         "eternal torment a greater punishment, so what Scripture means by them "
         "matters for obedience. He reads Scripture to say that Adam would have lived "
         "for ever on earth, that Christ recovered that life for believers at the "
         "resurrection, and that the kingdom of God will be on earth."),
        ("Hell and salvation",
         "The place of the damned is described in Scripture by the company of those "
         "once destroyed, by fire and by darkness, which Hobbes takes as metaphors "
         "for destruction and grief. He finds no text that gives a wicked man an "
         "eternal life in torment; what is promised is a second death. Salvation is "
         "deliverance from the evils that sin brought, and redemption is a ransom "
         "God was pleased to accept, not one he was bound to."),
        ("What a church is",
         "Church in Scripture means a house, an assembly called by authority, all "
         "Christians dispersed, a part of them, the elect, or a congregation of "
         "professors. Only in the last sense can a church be one person that wills "
         "and commands, and then Hobbes defines it as a company of Christians "
         "united in one sovereign, who calls them together. So there is no universal "
         "church that all must obey, and a church that can act is the same thing as "
         "a Christian commonwealth."),
    ],
    "read_title": "The passage first, then the chapters line by line",
    "read_intro": (
        "The definition comes after Hobbes has said what must be true of anything "
        "that can will and act as one person. The reasoning before it is part of the "
        "passage."
    ),
    "body": [
        ("p", "<strong>Chapter 39.</strong> &ldquo;According to this sense, I define a "
              "CHURCH to be, A company of men professing Christian Religion, united in the "
              "person of one Soveraign; at whose command they ought to assemble, and "
              "without whose authority they ought not to assemble.&rdquo;"),
        ("p", "Hobbes could not have written that sentence in 1640. It answers a "
              "dispute in which preachers and bishops, a Parliament, a king, and the "
              "Scottish Presbyterians had each claimed to speak for the church, and it "
              "was written in exile with the Church of England abolished and Charles I "
              "dead. The Scots, in the tradition of Andrew Melville, held that Scotland "
              "had two kingdoms, and that in the church the king was a member and "
              "not a master. Chapter 39 makes the opposite case, and Chapter 38, which "
              "comes first, explains why it matters."),
        ("p", "It begins with a claim about rewards. The commonwealth depends on justice, "
              "justice on the power of life and death and lesser rewards and "
              "punishments, so &ldquo;It is impossible a Common-wealth should stand, "
              "where any other than the Soveraign, hath a power of giving greater "
              "rewards than Life; and of inflicting greater punishments than "
              "Death.&rdquo; Eternal life is greater than the present life, eternal "
              "torment greater than natural death, so it is, he says, worth considering "
              "what Scripture means by them, and for which offences and by whom."),
        ("p", "His own reading is distinctive and he says so. Adam, he argues, was created "
              "to live for ever in Eden, as the tree of life shows, and &ldquo;Adam if he "
              "had not sinned, had had an Eternall Life on Earth&rdquo;. Christ "
              "recovered that life for believers; the texts about Zion, the new "
              "Jerusalem and the reign of Christ place it on earth; the dead wait until "
              "the resurrection. He says he only propounds this, maintaining "
              "nothing, while he waits for the end of &ldquo;that dispute of the "
              "sword&rdquo; to decide which authority approves doctrine, and he "
              "submits it &ldquo;to the interpretation of the Bible "
              "authorized by the Common-wealth, whose Subject I am&rdquo;. Of the "
              "wicked he writes that he finds &ldquo;none that affirm there shall bee "
              "an Eternall Life therein of any individuall person&rdquo;: Scripture "
              "speaks of a second death. The fire, the worm and the darkness are "
              "metaphors, each tied to a place or an event: the valley of Hinnom for "
              "Gehenna, Sodom for the lake of fire, Egypt's three days of darkness. "
              "Satan, devil and Abaddon are appellatives, he says, and mean the "
              "enemy, the accuser and the destroyer."),
        ("p", "None of this is mockery in the text, and it should not be in the lesson. "
              "Hobbes's critics took it as a denial of the immortal soul and of eternal "
              "punishment as the Church of England taught them. Bishop Bramhall, with "
              "whom Hobbes had argued about free will in the 1640s, wrote against "
              "Leviathan in 1658, and Clarendon wrote a long survey of its errors in "
              "1676. Hobbes's defence is in the text: he says that texts show a second "
              "death and not an immortal soul, and that the interpretation belongs to "
              "the sovereign. His reading has also been held by Christians who needed "
              "no political reason for it, on the ground of Scripture alone."),
        ("p", "In Chapter 39 he turns to the word. A church, from the Greek "
              "<em>ecclesia</em>, meant in the Greek commonwealths an assembly of "
              "citizens called forth to hear the magistrate. Called by lawful authority "
              "it was a lawful church; called by tumult, a confused one. In Scripture it "
              "means sometimes the house, sometimes all Christians, sometimes a part, "
              "sometimes the elect and sometimes a congregation of professors. Only in "
              "the last can a church be one person: without authority from a lawful "
              "congregation, whatever is done in a crowd is the act of each present and "
              "not of all together. Hence the definition."),
        ("p", "Two things follow, and the second is what Hobbes was after. First, "
              "&ldquo;there is on Earth, no such universall Church, as all Christians "
              "are bound to obey&rdquo;, since there is no power on earth to which all "
              "commonwealths are subject and every Christian is subject to the one he "
              "belongs to. Second, &ldquo;a Church, such a one as is capable to "
              "Command, to Judge, Absolve, Condemn, or do any other act, is the same "
              "thing with a Civil Common-wealth, consisting of Christian men&rdquo;: a "
              "civil state because its subjects are men, a church because they are "
              "Christians. And so &ldquo;Temporall and Spirituall Government, are but two "
              "words brought into the world, to make men see double, and mistake their "
              "Lawfull Soveraign&rdquo;. A Catholic, a Presbyterian or an Independent "
              "would reply that the definition settles by word what is in dispute: that "
              "the church is a company with its own head and discipline whatever "
              "sovereigns do, as the first Christians were a church under pagan emperors."),
        ("p", "The lab takes the definition as a rule with three conditions: the "
              "company professes Christianity (C), all its members are one commonwealth "
              "under one sovereign (S), and it acts by that sovereign's authority (W). "
              "A case table gives the verdict Hobbes's text implies for each case. A "
              "congregation that meets against the sovereign's prohibition he still calls "
              "a church, but an unlawful assembly, so the table does not use it. The "
              "lab checks the definition against it, lists the first case it gets "
              "wrong and says whether it is too broad or too narrow. The case "
              "verdicts are the lesson's readings of the chapter. One of the presets "
              "puts the Roman reading of the universal church in the table, which "
              "shows that the dispute is over the verdicts and not over the logic."),
        ("p", "The next lesson, <em>The Sovereigns of Israel and the Office of Christ</em>, "
              "begins with Abraham."),
        ("p", 'The three presets test the definition against four cases. In hobbes, '
              "Hobbes's definition agrees with his verdicts in all four, so it is adequate. "
              'In any-christians the definition is only that a company are Christians, and '
              'it agrees in only 2 of the 4: it is too broad, since it admits the '
              'crowd acting with no authority from a lawful congregation. In roman the universal '
              'church is counted as a church, and the definition then agrees in 3 of the 4 '
              'and is too narrow, since a company of all Christians under a pope has no one '
              'sovereign.'),
    ],
    "lab": ("argkit", {
        "mode": "analysis",
        "search": "pairs",
        "preset": "hobbes",
        "presets": [
            {"id": "hobbes", "label": "Hobbes's definition against Hobbes's verdicts",
             "conditions": ["C", "S", "W"], "target": "is a church", "definition": "C & S & W",
             "cases": [
                 _case("a Christian commonwealth under its sovereign", [1, 1, 1], 1),
                 _case("a crowd of Christians acting with no authority from a lawful congregation", [1, 1, 0], 0),
                 _case("all Christians, under a pope claiming every realm", [1, 0, 0], 0),
                 _case("a heathen commonwealth and its assemblies", [0, 1, 1], 0),
             ],
             "expect": {"anAgree": "4 / 4", "anFail": "none", "anVerdict": "Adequate"}},
            {"id": "any-christians", "label": "Any company of Christians",
             "conditions": ["C", "S", "W"], "target": "is a church", "definition": "C",
             "cases": [
                 _case("a Christian commonwealth under its sovereign", [1, 1, 1], 1),
                 _case("a crowd of Christians acting with no authority from a lawful congregation", [1, 1, 0], 0),
                 _case("all Christians, under a pope claiming every realm", [1, 0, 0], 0),
                 _case("a heathen commonwealth and its assemblies", [0, 1, 1], 0),
             ],
             "expect": {"anAgree": "2 / 4", "anFail": "a crowd of Christians acting with no authority from a lawful congregation: too broad", "anVerdict": "Too broad"}},
            {"id": "roman", "label": "The universal church counted as a church",
             "conditions": ["C", "S", "W"], "target": "is a church", "definition": "C & S & W",
             "cases": [
                 _case("a Christian commonwealth under its sovereign", [1, 1, 1], 1),
                 _case("a crowd of Christians acting with no authority from a lawful congregation", [1, 1, 0], 0),
                 _case("all Christians, under a pope claiming every realm", [1, 0, 0], 1),
                 _case("a heathen commonwealth and its assemblies", [0, 1, 1], 0),
             ],
             "expect": {"anAgree": "3 / 4", "anFail": "all Christians, under a pope claiming every realm: too narrow", "anVerdict": "Too narrow"}},
        ],
        "panel_title": "Test the definition of a church",
        "panel_intro": (
            'C means the company professes Christianity, S that its members are '
            'one commonwealth under one sovereign, W that it acts by that '
            "sovereign's authority. The verdicts in the table are the lesson's "
            'readings of Chapter 39. Type another formula over C, S and W and '
            'the lab reports how many verdicts it matches; with pairs it also '
            'lists two-letter formulas that fit.'
        ),
    }),
    "steps_title": "Testing a definition against cases",
    "steps_intro": "Four steps, the same for any definition.",
    "steps": [
        ("Turn each clause into a letter",
         "Write each condition of the definition as a letter: here professing "
         "Christianity, unity under one sovereign, and acting by his authority."),
        ("Fix the verdict for each case first",
         "Write down, from the text, whether each case is or is not a church before "
         "you try the formula. Otherwise the formula marks its own work."),
        ("Compare formula and verdict",
         "A case the formula admits but the verdict refuses shows it is too broad; a "
         "case the verdict admits and the formula refuses shows it is too narrow."),
        ("Ask what else would fit",
         "More than one formula may fit a small table. A clause that is already "
         "implied by another, as acting by his authority implies a sovereign, cannot be tested "
         "until a case separates them."),
    ],
    "worked": {
        "title": 'Why Christians alone is too broad',
        "intro": [
            "Take the second preset. The definition is only that the company professes "
            "Christianity.",
        ],
        "lines": [
            "case 1:  C = 1, verdict 1: agrees",
            "case 2 (crowd with no authority):  C = 1, verdict 0: too broad",
            "case 3 (all Christians under a pope):  C = 1, verdict 0",
            "case 4 (heathen commonwealth):  C = 0, verdict 0: agrees",
            "agreement:  2 of 4",
        ],
        "after": [
            "The first preset's three-clause definition agrees with all four. The "
            "search also finds that a two-letter formula, C and W, agrees with all four. "
            "That is because W, acting by the sovereign's authority, already presupposes S, so "
            "no case in the table can show that S is needed. The roman preset changes "
            "one verdict and the same definition is then too narrow on that case.",
        ],
    },
    "quiz_title": "A definition against its cases",
    "quiz": [
        {"q": "On the lesson's verdicts, why is a company of Christians alone "
              'too broad?',
         "a": [
               'It excludes a Christian commonwealth',
               'It admits a heathen commonwealth',
               'It admits a crowd of Christians acting with no authority from a lawful congregation',
               'It is too narrow, not too broad',
         ],
         "c": 2,
         "why": 'The crowd is a company of Christians, so the formula '
                'admits it while the verdict refuses it. It does not exclude the '
                'commonwealth, and it refuses the heathen one. The last answer is the '
                "reverse of the lab's verdict."},
        {"q": 'Which sentence of the chapter makes the universal church a non-church?',
         "a": [
               'The church is the elect only',
               'A church is a house of prayer',
               'There is no power on earth to which all other commonwealths are subject',
               'Christ is head of the church',
         ],
         "c": 2,
         "why": 'He argues that there is no power on earth to which all commonwealths '
                'are subject, so each Christian is subject to his own, and there is no '
                'universal church that all must obey. The others are other senses of '
                'the word that he lists, in which a church is not one person.'},
        {"q": "What would the Roman reading in the third preset make of Hobbes's "
              'definition?',
         "a": [
               'Too narrow: it refuses a case counted as a church',
               'Too broad: it admits a case counted as no church',
               'Adequate on every case',
               'Insignificant',
         ],
         "c": 0,
         "why": 'With the universal church counted as a church, the definition refuses '
                'it and so fails on that case; the verdict, not the logic, is what the '
                'Roman reading changes.'},
        {"q": 'What does Hobbes say about eternal life for the wicked?',
         "a": [
               'That they are tormented for ever and never die',
               'That they are saved after a time in purgatory',
               'That Scripture is silent about the wicked',
               'He finds no text that gives any individual one, only a second death',
         ],
         "c": 3,
         "why": 'He writes that he finds none that affirm an eternal life of any '
                'individual in the fire, and that what Scripture gives is a second '
                'death. He denies that anyone is tormented for ever without dying. '
                'Purgatory is not in his reading.'},
    ],
    "mistakes": [
        ("Thinking Hobbes's definition covers any Christian assembly",
         "It covers a company united in one sovereign, who calls it together. The "
         "second preset shows what happens when only Christianity is required: a "
         "crowd with no lawful authority counts as a church. A congregation that meets "
         "against the sovereign's prohibition Hobbes still calls a church, but an "
         "unlawful assembly."),
        ("Reading the hell chapter as a denial that sin is punished",
         "Hobbes says the wicked suffer, bodily and in grief, and then a second death. "
         "What he denies is that Scripture promises them an eternal life of torment. "
         "He says so with submission to the Bible as the commonwealth authorizes it."),
        ("Thinking the table settles the dispute",
         "The verdicts are the lesson's readings of Chapter 39. The roman preset "
         "changes one and the definition fails. A lab can show a definition agrees with "
         "its cases; it cannot show the cases are right."),
    ],
    "standard": (
        "Finish when you can test a definition of a church against cases.",
        "Given a definition and a table of cases with verdicts, count the agreements, "
        "name the first case it gets wrong and say whether it is too broad or too narrow."
    ),
    "note": (
        "The lab checks the formula against the verdicts the lesson writes down, which "
        "are readings of Hobbes. It cannot decide whether a church is a commonwealth, "
        "whether Scripture teaches a second death, or what a church that has no "
        "sovereign should be called; those are the disputes Chapters 38 and 39 enter."
    ),
}

# ------------------------------------------------------------------ 07
# Leviathan ch. 40, 1651 p. 250; PDF p. 420 of the operator's copy.
L7 = {
    "slug": "the-sovereigns-of-israel-and-christ",
    "title": "The Sovereigns of Israel and the Office of Christ",
    "module": "Chapters 40 and 41 · Of the Rights of the Kingdome of God; of the Office of our Blessed Saviour",
    "one_line": "Hobbes argues that Moses ruled Israel by the people's promise to obey him, that every later sovereign of Israel held religion with the sword, and that Christ's kingdom begins at his return.",
    "summary": (
        "Chapter 40 goes through the kingdom of God from Abraham to the captivity and "
        "finds civil and religious authority in one hand each time. Chapter 41 sets out "
        "the three parts of Christ's office, redeemer, teacher and king to come. Put the "
        "argument that Moses's authority rests on the people's consent into premises "
        "and find which premise carries it."
    ),
    "key": [
        "Abraham: his household took God's word",
        "Moses: obeyed by the people's promise",
        "Israel's religion was the king's to order",
        "Christ's offices: redeemer, teacher, king",
        "his kingdom begins when he returns",
    ],
    "key_label": "Israel and Christ in five lines",
    "concepts_intro": (
        "These chapters are a history with an argument in it, and the argument is "
        "that nowhere in Scripture before Christ is religion separated from "
        "government."
    ),
    "concepts": [
        ("Abraham and Moses",
         "God spoke only to Abraham, so his household took God's commands from him, "
         "and Hobbes draws three points: those to whom God has not spoken take God's "
         "positive commands from their sovereign; a private spirit against the "
         "sovereign's religion may be punished; and only the sovereign is the "
         "interpreter of what God said. Moses stood where Abraham did, but could not "
         "claim by inheritance, and Hobbes argues his authority rested on the "
         "people's promise to obey him."),
        ("The priests, the judges and the kings",
         "After Moses the sovereignty was in the high priest, then in the judges "
         "in practice though not in right, and then, after Israel asked for a king, in "
         "the kings. Hobbes cites Solomon removing a high priest, dedicating the "
         "temple and blessing the people, and Josiah's inquiry of Huldah, as marks of "
         "supremacy in religion. Prophets controlled kings, he allows, but that does "
         "not make them heads of the church."),
        ("The office of Christ",
         "Three parts: redeemer by sacrifice, teacher who proclaims himself the Christ, "
         "and king, but under his Father, as Moses and the high priests were. His "
         "kingdom is of the world to come, so by his first coming he did nothing "
         "against the civil right of the Jews or of Caesar."),
    ],
    "read_title": "The passage first, then the chapters line by line",
    "read_intro": (
        "The passage is the heart of Chapter 40. It is an argument by elimination, "
        "and it is worth reading slowly to see which grounds Hobbes sets aside."
    ),
    "body": [
        ("p", "<strong>Chapter 40.</strong> &ldquo;For it could not be the commandement "
              "of God that could oblige them; because God spake not to them immediately, "
              "but by the mediation of Moses himself: And our Saviour saith of himself, "
              "If I bear witnesse of my self, my witnesse is not true; much lesse if "
              "Moses bear witnesse of himselfe, (especially in a claim of Kingly power over "
              "Gods people) ought his testimony to be received. His authority therefore, "
              "as the authority of all other Princes, must be grounded on the Consent of "
              "the People, and their Promise to obey him.&rdquo;"),
        ("p", "Why would anyone obey Moses? The Israelites had come out of Egypt, "
              "seen the plagues and stood at Sinai. It seems plain enough that they "
              "obeyed because God had chosen him. Hobbes sees a problem that "
              "later readers have often admired and sometimes resisted: they had to "
              "know that God had chosen him, and the only one who said so was Moses. "
              "The argument that follows is a model of how Hobbes reads Scripture "
              "as political history."),
        ("p", "The chapter begins with Abraham, &ldquo;The Father of the Faithfull, and "
              "first in the Kingdome of God by Covenant&rdquo;. God spoke only to him; his "
              "family's wills were involved in his, and so, Hobbes says, he had lawful "
              "power to make them perform what he covenanted for them. From this three "
              "points: that those to whom God has not spoken must take God's "
              "commandments from their sovereign; that Abraham might lawfully punish a "
              "subject who pretended a private vision against what he forbade, as a "
              "sovereign may now; and that &ldquo;none but the Soveraign in a Christian "
              "Common-wealth, can take notice what is, or what is not the Word of "
              "God&rdquo;. Inward belief, he adds, is not voluntary and falls under no "
              "law; the obligation is to the external acts and profession of religion."),
        ("p", "Moses is harder, and that is the argument you have read. Abraham's "
              "power was a father's and descended; Moses had no such claim, so his "
              "authority &ldquo;depended yet merely upon the opinion they had of his "
              "Sanctity&rdquo; and the truth of his miracles, and if that opinion changed "
              "they were no more obliged to take anything he said for the law of God. "
              "So he looks for another ground. It cannot be God's command, since God spoke "
              "through Moses, and not to them. It cannot be Moses's own say-so, since "
              "even Christ said his own witness was not true. It is therefore the "
              "people's consent, which Hobbes finds at Sinai, where they said to Moses, "
              "speak thou with us and we will hear, but let not God speak with us lest "
              "we die. Here was their promise, and by it they obliged themselves to obey "
              "whatever he should deliver as the commandment of God."),
        ("p", "It is an elimination and its force is in its premises. The first is that "
              "there were only a few possible grounds for obligation: God's direct "
              "command, inheritance, Moses's own witness, or the people's consent. A "
              "careful reader will ask about miracles. Hobbes does not give them a "
              "separate ground; he folds them into the opinion that might change, and the "
              "lab shows what would happen if they stood alone. Exodus has Moses "
              "alone called up the mountain, Aaron left aside, and later the earth "
              "swallowing Korah, Dathan and Abiram, who said all the congregation was "
              "holy. For Hobbes this shows Moses alone had, under God, the sovereignty, "
              "&ldquo;not onely in causes of Civill Policy, but also of Religion&rdquo;. "
              "And so he reads Scripture itself by Moses's pattern: since God now "
              "speaks in it, &ldquo;the Scriptures since God now speaketh in them, are "
              "the Mount Sinai&rdquo;, with bounds set by the laws of those who represent "
              "God's person. To look is allowed; to interpret, and judge whether the "
              "sovereign governs as God commands, is to gaze irreverently."),
        ("p", "The rest of the chapter follows the sovereignty through Israel's "
              "history. After Moses it descended to Eleazar the high priest by the "
              "covenant; under the judges Israel &ldquo;did that which was right in "
              "his own eyes&rdquo;, which Hobbes reads as having no sovereign in "
              "exercise though the right was still the high priest's. When the people "
              "asked for a king like the nations, they deposed the high priest of royal "
              "authority, and God consented. From then to the captivity, he concludes, "
              "&ldquo;the Supremacy of Religion, was in the same hand with that of the "
              "Civill Soveraignty&rdquo; and the priest's office was ministerial. His "
              "evidence is Solomon, who thrust out Abiathar from the priesthood, "
              "dedicated the temple and blessed the people, and Josiah, who sent the "
              "priest to ask Huldah the prophetess about the book of the law. &ldquo;Is "
              "not this full Power, both Temporall and spirituall, as they call it, "
              "that would divide it?&rdquo;"),
        ("p", "A Presbyterian reader answered at once: prophets rebuked kings, "
              "Isaiah rebuked Hezekiah, and a king who ordered the worship of Baal "
              "was not obeyed by faithful priests. Hobbes saw that and says in the "
              "text that &ldquo;none of them were uncontrolled in the use of it&rdquo;, "
              "and that the people never understood the right and revolted whenever "
              "their governors displeased them. But he says from the practice there "
              "can no argument be drawn that the right was in the prophets, "
              "unless one concludes that Isaiah was head of the church because Hezekiah "
              "was answered through him. Others used the covenant for opposite "
              "conclusions: Samuel Rutherford's <em>Lex, Rex</em> in 1644 argued from "
              "the same history that kings hold power by a covenant with the people and "
              "under God's law. The disagreement is about what the history shows, and "
              "it was the disagreement of the Civil War."),
        ("p", "Chapter 41 takes Christ's office as a Moses-like one. &ldquo;We find in "
              "Holy Scripture three parts of the Office of the Messiah&rdquo;: "
              "redeemer, teacher and an eternal king under his Father. The redeemer "
              "pays the ransom of sin, which is death, as the scapegoat and the "
              "sacrificed goat did together; the teacher proclaims himself the Christ "
              "and prepares men by teaching and miracles; the king reigns in the world "
              "to come. During his stay on earth, Hobbes argues, he was not king, since "
              "his kingdom was not of this world; the time of his preaching was a "
              "regeneration and not a reign. He told men to obey those who sat in "
              "Moses's seat and to pay tribute to Caesar. And so nothing he taught "
              "&ldquo;tendeth to the diminution of the Civill Right of the Jewes, or of "
              "Caesar&rdquo;. The consequence, drawn in the next chapter, is that his "
              "ministers have no power to command now."),
        ("p", 'The lab turns the Moses argument into premises. R says the '
              "people were obliged to obey Moses; D that God's direct command "
              "obliged them; H that they were obliged as heirs to Abraham's "
              "right; W that Moses's own witness obliged them; C that their "
              'consent and promise did. The argument is valid; whether it is '
              'sound depends on the premise that these are the only grounds, '
              'which is the one a critic would reject. The next lesson, '
              '<em>Power Ecclesiastical and What Is Necessary for '
              'Salvation</em>, takes up what follows for ministers and for '
              'subjects.'),
        ("p", 'The three presets are the same argument with its premises changed. In moses, '
              "God did not command it, inheritance gave no title, and Moses's own witness "
              "did not bind, so with the obligation given the people's consent follows: 32 "
              'rows, none a counterexample, valid. In inheritance the premise that excludes '
              'inheritance is dropped, and one row is a counterexample, so the argument is '
              'invalid. In signs a different ground, signs and wonders, takes the place of inheritance '
              'in the list, and again one row is a counterexample.'),
    ],
    "lab": ("argkit", {
        "mode": "validity",
        "preset": "moses",
        "show": "all",
        "presets": [
            {"id": "moses", "label": "Moses's authority by elimination (R obliged, D God's command, H inheritance, W his own witness, C consent)",
             "premises": ["R -> (D | H | W | C)", "~D", "~H", "~W", "R"], "conclusion": "C",
             "expect": {"vaRows": "32", "vaCounter": "0", "vaVerdict": "Valid"}},
            {"id": "inheritance", "label": "Inheritance not excluded",
             "premises": ["R -> (D | H | W | C)", "~D", "~W", "R"], "conclusion": "C",
             "expect": {"vaRows": "32", "vaCounter": "1", "vaVerdict": "Invalid"}},
            {"id": "signs", "label": "Signs and wonders as a further ground (M)",
             "premises": ["R -> (D | W | C | M)", "~D", "~W", "R"], "conclusion": "C",
             "expect": {"vaRows": "32", "vaCounter": "1", "vaVerdict": "Invalid"}},
        ],
        "panel_title": "Moses by elimination",
        "panel_intro": (
            "This lab computes classical propositional logic, which nothing here "
            "disputes: it lists every row of true and false and marks the rows that make "
            "every premise true and the conclusion false. In the first preset the first "
            "premise says that if they were obliged, it was by one of four grounds. Drop a "
            "premise, or add a ground, and read the counterexample. What it cannot "
            "decide is whether the premises are true."
        ),
    }),
    "steps_title": "An argument by elimination",
    "steps_intro": "Four steps, in the order the chapter does them.",
    "steps": [
        ("List the possible grounds",
         "Write the first premise: if they were obliged, it was by one of a stated list "
         "of grounds. This is the premise on which everything rests."),
        ("Cross out each ground with a reason",
         "Add one premise per ground you deny: God did not speak to them directly, "
         "Moses had no inheritance, his witness of himself does not bind."),
        ("State the fact to explain",
         "Add that they were obliged. Without it the conclusion cannot be drawn."),
        ("Test, then test the list",
         "Check validity. Then ask whether the list is complete: a ground you "
         "forgot, such as a sign, gives a counterexample row."),
    ],
    "worked": {
        "title": "Why the list of grounds carries the argument",
        "intro": [
            "Take the third preset: miracles added as a ground M, and nothing to "
            "exclude it.",
        ],
        "lines": [
            "premises:  R → (D or W or C or M);  not D;  not W;  R",
            "five letters:  2·2·2·2·2 = 32 rows",
            "conclusion C false, premises true: need M true",
            "that row: R, M true;  D, W, C false",
            "one counterexample,  verdict: invalid",
        ],
        "after": [
            "In the first preset the four grounds are all crossed out but one, and the "
            "argument is valid with no counterexample in 32 rows. Hobbes's text deals "
            "with miracles by saying the people's opinion of them could change, which "
            "is a reason to treat them as no separate ground; the lab only shows that "
            "this must be said, or the conclusion does not follow.",
        ],
    },
    "quiz_title": "Moses by elimination",
    "quiz": [
        {"q": 'In the first preset, which premise does a critic dispute who says '
              'miracles alone obliged Israel to obey Moses?',
         "a": [
               'That God spoke to Moses',
               'That Moses wrote Deuteronomy',
               'That the people were afraid',
               'That the four listed grounds are the only ones',
         ],
         "c": 3,
         "why": 'A critic who offers a further ground denies that the list is complete, '
                'which is the first premise. The others are not premises of the '
                'argument.'},
        {"q": "Why does Hobbes say Moses's own witness cannot oblige the people?",
         "a": [
               'Moses was a stranger to Israel',
               'Christ said that if he bore witness of himself his witness was not true',
               'Witness is never evidence of authority',
               'Aaron was the true leader',
         ],
         "c": 1,
         "why": "He cites John 5.31 and adds that much less ought Moses's testimony to "
                'be received in a claim of kingly power. The others are not his '
                'reasons; he says Moses was sovereign all his own time, Aaron not.'},
        {"q": 'What does Hobbes conclude about the supremacy of religion in the '
              'kingdom of God from the first institution to the captivity?',
         "a": [
               'It was always with the priests, apart from the kings',
               'It was with the prophets, who controlled the kings',
               'It was never settled',
               'It was in the same hand as the civil sovereignty',
         ],
         "c": 3,
         "why": "He says from the first institution of God's kingdom to the captivity "
                'the supremacy of religion was in the same hand as the civil '
                'sovereignty. He allows that the people did not understand it and that '
                'prophets controlled kings, but denies that this puts the right in the '
                'prophets.'},
        {"q": "When does Hobbes say Christ's kingdom begins?",
         "a": [
               'At his baptism',
               'At his coming again, in the world to come',
               'At his crucifixion',
               'At Pentecost',
         ],
         "c": 1,
         "why": 'He says his kingdom was not of this world and is not to begin till the '
                'general resurrection, when he comes in glory; his first coming was to '
                'redeem and to teach.'},
    ],
    "mistakes": [
        ("Thinking Hobbes says Moses was a fraud",
         "He says Moses spoke with God, that his miracles were real, and that the "
         "kingdom of God was truly set up. His point is what bound the people, and he "
         "says it was their promise, since no one could show the commandment to "
         "anyone but through Moses."),
        ("Treating validity as truth",
         "The lab says the conclusion follows if the premises are true; the first "
         "preset has no counterexample, and the second shows how it fails if "
         "inheritance is allowed. Whether the grounds were exhaustive is the question."),
        ("Thinking Christ's kingdom was here and now",
         'Hobbes argues from the words <em>my kingdom is not of this world</em> '
         'and from the time of the preaching, which he calls a regeneration, '
         'that the kingdom begins when he comes again, and that he therefore '
         'took nothing from Caesar.'),
    ],
    "standard": (
        "Finish when you can say which premise carries an elimination.",
        "Given an argument that one ground remains after the others are excluded, "
        "write it as premises, find the counterexample when a ground is added or a "
        "denial dropped, and name the premise doing the work."
    ),
    "note": (
        "The lab shows that the conclusion follows from the premises as written. It "
        "cannot decide whether the list of grounds is complete, whether the people really "
        "promised what Hobbes says, or whether Israel's history shows what a Christian "
        "commonwealth should do; Rutherford, Presbyterians and Hobbes read it "
        "differently."
    ),
}

# ------------------------------------------------------------------ 08
# Leviathan ch. 43, 1651 p. 322; PDF p. 499 of the operator's copy.
L8 = {
    "slug": "power-ecclesiastical-and-salvation",
    "title": "Power Ecclesiastical and What Is Necessary for Salvation",
    "module": "Chapters 42 and 43 · Of Power Ecclesiasticall; of what is Necessary for a Mans Reception into the Kingdome of Heaven",
    "one_line": "Hobbes says Christ's ministers teach and do not command, answers Cardinal Bellarmine, and argues that faith that Jesus is the Christ and obedience to the laws are all that salvation requires.",
    "summary": (
        "Chapter 42 asks what power the church has and says it is the power to "
        "teach, with no coercive power except what a sovereign gives; it answers "
        "Bellarmine at length. Chapter 43 asks how a man can obey both God and "
        "the sovereign, and answers that all that is necessary to salvation is "
        "faith that Jesus is the Christ and obedience. Put the argument that a "
        "Christian need not disobey the sovereign to be saved into premises and "
        "find the premise a Covenanter would deny."
    ),
    "key": [
        "ministers are schoolmasters, not commanders",
        "faith cannot be commanded or taken away",
        "one article necessary: Jesus is the Christ",
        "salvation: faith and obedience, no more",
        "Naaman: the act is the sovereign's, not his",
    ],
    "key_label": "Power and salvation in five lines",
    "concepts_intro": (
        "Chapter 42 is the longest in the book, and Chapter 43 is the shortest answer "
        "to its biggest problem. The two belong together."
    ),
    "concepts": [
        ("The power to teach",
         'Before kings were Christian the power ecclesiastical was in the '
         'apostles and those ordained by the laying on of hands. Hobbes argues '
         'from the commission to preach, teach and baptize that it is a power '
         "of proclaiming and persuading: Christ's kingdom is not of this world, "
         "faith cannot be commanded, and Christ's ministers are "
         '<em>fishers</em>, not <em>hunters</em>, of men. After kings become '
         "Christian, the power to order the church is the sovereign's."),
        ("Bellarmine answered",
         "The Jesuit Cardinal Robert Bellarmine had argued that the pope's power is "
         "monarchical and coercive, and Hobbes takes him as the strongest defender "
         "of the papal claim. He answers that the first question, the best form "
         "of government, concerns sovereigns and not pastors, that Peter's rock was "
         "the one article of faith, and that from the power to teach no power over "
         "kings follows."),
        ("What is necessary for salvation",
         "Two virtues: faith in Christ and obedience to laws. Obedience is the "
         "serious endeavour to obey, since God accepts the will for the deed. Faith "
         "is the one article that Jesus is the Christ, on which the rest are founded, "
         "and Hobbes brings five arguments from Scripture. So a Christian who obeys "
         "his sovereign loses neither, and where the sovereign is an infidel, "
         "his faith is inward and he has the licence of Naaman."),
    ],
    "read_title": "The passage first, then the chapters line by line",
    "read_intro": (
        "The sentence is short, and the whole of Chapter 43 is the proof of it. "
        "Read it first as the claim, then follow how Hobbes defends it."
    ),
    "body": [
        ("p", "<strong>Chapter 43.</strong> &ldquo;All that is NECESSARY to Salvation, is "
              "contained in two Vertues, Faith in Christ, and Obedience to "
              "Laws.&rdquo;"),
        ("p", "Imagine the position of a Christian in the England of the 1640s. The "
              "king says one thing, the Parliament another, the preacher in the "
              "pulpit a third, and each claims God's authority. Hobbes begins Chapter "
              "43 with the difficulty: &ldquo;The most frequent praetext of Sedition, and "
              "Civill Warre, in Christian Common-wealths hath a long time proceeded "
              "from a difficulty, not yet sufficiently resolved, of obeying at once, "
              "both God, and Man&rdquo;. When two commands conflict and one is God's, "
              "God's must be obeyed. The trouble is knowing which is God's. His "
              "remedy is to ask what is necessary for salvation, because if the "
              "sovereign's command can be obeyed &ldquo;without the forfeiture of life "
              "Eternall; not to obey it is unjust&rdquo;."),
        ("p", "Chapter 42 prepares the ground by saying what a church's ministers may "
              "do. For the time between the Ascension and the conversion of kings the "
              "power was in the apostles and those they ordained by laying on of hands, "
              "in imitation of Moses and Joshua. Hobbes gives the doctrine of the "
              "Trinity in terms of representation: one God represented by Moses, by "
              "Christ and by the apostles, three persons in the sense of three "
              "representers. Readers have objected, then and since, that this makes the "
              "persons successive roles rather than the co-eternal persons of the "
              "creeds. He moves on. His question is whether the power is "
              "monarchical, aristocratical or democratical, as Bellarmine asks, and he "
              "says all of those are sovereign and coercive. If it appears that Christ "
              "left no coercive power, &ldquo;the Apostles, and other Ministers of the "
              "Gospel, are our Schoolmasters, and not our Commanders, and their Precepts "
              "not Laws, but wholesome Counsells&rdquo;, then all that dispute was in "
              "vain."),
        ("p", "He argues it from five directions. The commission was to preach, teach "
              "and baptize, and &ldquo;Preachers therefore have not Magisteriall, but "
              "Ministeriall power&rdquo;. Christ's kingdom is not of this world, so his "
              "ministers cannot demand obedience in his name: the time between is a "
              "regeneration, compared to fishing and sowing and leaven, by which "
              "compulsion is excluded. Faith depends on arguments and not on commands; "
              "Paul says in so many words, &ldquo;Wee have no Dominion over your "
              "Faith&rdquo;. Scripture tells Christians to obey infidel masters and "
              "princes in all things. And so, he says, no minister has any authority "
              "to command, unless he has civil authority too."),
        ("p", "The hard case comes next. What if a sovereign forbids belief in Christ? "
              "Hobbes answers that such a prohibition has no effect, since faith is a "
              "gift of God, which man &ldquo;can neither give, nor take away by promise "
              "of rewards, or menaces of torture&rdquo;. What if a sovereign commands "
              "you to say with your tongue what you do not believe? Profession "
              "is an external thing, like any gesture of obedience, and the Christian "
              "has the liberty that Elisha allowed Naaman the Syrian, who was told to go "
              "in peace when he bowed in the house of Rimmon. Hobbes says that "
              "&ldquo;that action is not his, but his Soveraigns&rdquo;. He tests "
              "this by a case of a Muslim ordered to attend Christian worship: if he "
              "may disobey on pain of death, so may every private man for any "
              "religion, true or false. The martyrs are those who witness to the "
              "resurrection, and a martyr in the proper sense, he says, can only be "
              "one who saw Christ risen; one sent to preach it who had not seen him is a "
              "martyr only in a second sense. This is the passage "
              "that most infuriated his opponents, and it should be read as it is: it "
              "does not say conscience is nothing, it says conscience is inward and "
              "the outward act belongs to the one who commands it."),
        ("p", 'The rest of the chapter is Bellarmine. Hobbes takes him as the '
              "writer by whom the Pope's claim has been &ldquo;maintained "
              'chiefly, and I think as strongly as is possible&rdquo;, and '
              'follows his five books on the supreme pontiff, answering the '
              'first, on the best form of government and on Peter as monarch of '
              'the church, the second, on Peter as bishop of Rome and the popes '
              'as his successors, and the others in turn. He reads the text on '
              'which the Peter claim rests, <em>thou art Peter, and upon this '
              "rock</em>, as a play on Peter's name, the rock being the article "
              'that Jesus is the Christ. And of the argument that a pastor must '
              'feed his flock and so may compel kings, he says it would make '
              'the pope, as pastor of Christian men, &ldquo;King of '
              'Kings&rdquo;, which Christian kings ought either to confess or '
              'take upon themselves the supreme pastoral charge, each in his '
              "own dominion. For Bellarmine's examples he says that examples "
              "prove nothing. A reader on Bellarmine's side would say that "
              'Hobbes treats a claim about the order of souls as if it were a '
              'claim about the order of states, and that is the premise they '
              'would deny.'),
        ("p", "Chapter 43 then gives the answer that the whole of Part III has been "
              "building. Obedience is &ldquo;a serious Endeavour to Obey him&rdquo;, "
              "since God accepts the will for the deed; the laws of God are the laws "
              "of nature, whose principal is to keep faith, which means obeying civil "
              "sovereigns, and the Bible is law only where the civil sovereign has made "
              "it so. Faith has its causes, chiefly hearing, as Paul says, by lawful "
              "pastors, and Hobbes holds that Christians do not know but believe the "
              "Scripture to be the word of God. Then the article: &ldquo;Onely Article of "
              "Faith, which the Scripture maketh simply Necessary to Salvation, is "
              "this, that JESUS IS THE CHRIST&rdquo;. He proves it by the scope of the "
              "evangelists, the sermons of the apostles, the ease of Christian faith, "
              "plain texts, and the places where it is made the foundation, and shows "
              "that other articles, such as that God is omnipotent or that Christ is "
              "risen, are contained in it."),
        ("p", "Then he draws the conclusion for obedience. A Christian sovereign "
              "allows belief in that article and requires obedience to the civil law, "
              "which contains the laws of nature, so &ldquo;Whosoever therefore "
              "obeyeth his Christian Soveraign, is not thereby hindred, neither from "
              "beleeving, nor from obeying God&rdquo;; and &ldquo;There can therefore "
              "be no contradiction between the Laws of God, and the Laws of a "
              "Christian Common-wealth&rdquo;. If he errs in drawing a consequence, "
              "Hobbes asks who is to judge, a private man, the pope, an apostle, who "
              "might also err, since Paul withstood Peter to his face? Under an infidel "
              "sovereign, the subject's faith is inward and invisible; he may suffer for "
              "it, but he should not make war. He closes the book's Third Part with a "
              "disclaimer: that he pretends &ldquo;not to advance any Position of my "
              "own&rdquo;, only to show the consequences that seem deducible from "
              "Scripture."),
        ("p", 'That is the argument the Scottish Covenanters would not accept. '
              'For them Christ was head of the church and the king bound to him '
              'by covenant; to obey a king who commanded what the covenant '
              'forbade was to sin, and faith was not only an inward article. '
              'The lab puts the argument in premises so that the point of '
              'disagreement is visible. The next course, <em>The Kingdom of '
              'Darkness, and the Review and Conclusion</em>, turns to what '
              'Hobbes says goes wrong when Scripture is misread.'),
        ("p", 'The four presets set the argument against its critics. In hobbes, salvation '
              'needs faith and obedience, a man has the faith, and so if he obeys he is '
              'saved: 8 rows, no counterexample, valid. In naaman the premise is added that '
              'a commanded act of obedience keeps the faith, and a man who is commanded and '
              'obeys is saved: 16 rows, valid. In covenanter that premise is dropped and '
              'one row has the faith lost, so the argument is invalid. In more-articles a '
              'further article is required for salvation and again one row is a '
              'counterexample.'),
    ],
    "lab": ("argkit", {
        "mode": "validity",
        "preset": "hobbes",
        "show": "all",
        "presets": [
            {"id": "hobbes", "label": "Faith and obedience suffice (S saved, F faith, G obeys the sovereign)",
             "premises": ["S <-> (F & G)", "F"], "conclusion": "G -> S",
             "expect": {"vaRows": "8", "vaCounter": "0", "vaVerdict": "Valid"}},
            {"id": "naaman", "label": "Commanded to bow, as Naaman was (C commanded, and the faith is kept)",
             "premises": ["S <-> (F & G)", "(C & G) -> F", "C", "G"], "conclusion": "S",
             "expect": {"vaRows": "16", "vaCounter": "0", "vaVerdict": "Valid"}},
            {"id": "covenanter", "label": "Drop the Naaman premise",
             "premises": ["S <-> (F & G)", "C", "G"], "conclusion": "S",
             "expect": {"vaRows": "16", "vaCounter": "1", "vaVerdict": "Invalid"}},
            {"id": "more-articles", "label": "A further article M also required",
             "premises": ["S <-> (F & G & M)", "F"], "conclusion": "G -> S",
             "expect": {"vaRows": "16", "vaCounter": "1", "vaVerdict": "Invalid"}},
        ],
        "panel_title": "Obedience and salvation",
        "panel_intro": (
            "This lab computes classical propositional logic, which nothing here "
            "disputes. S means he is saved, F that he holds the faith that Jesus is the "
            "Christ, G that he obeys his sovereign, C that the sovereign commands an "
            "outward act, M a further article. The first premise, S if and only if F and "
            "G, is the lesson's reading of Chapter 43. The lab cannot say whether any "
            "premise is true."
        ),
    }),
    "steps_title": "Testing a claim about obedience and salvation",
    "steps_intro": "Four steps, in the order Chapter 43 argues.",
    "steps": [
        ("State what salvation needs",
         "Write the necessary and sufficient conditions as one sentence: saved if and "
         "only if the faith and the obedience hold. Any other article would go in here."),
        ("State what the command touches",
         "Say whether the command reaches the faith or only the outward act. Hobbes "
         "says belief cannot be commanded, and that the act is the sovereign's."),
        ("Draw the conclusion",
         "If the faith is held, then obeying leaves salvation as it was: obeying implies "
         "saved."),
        ("Find the premise that could fail",
         "Drop one premise at a time. Each row the lab then shows is a case a critic "
         "would claim: a further article, or a command that does reach the faith."),
    ],
    "worked": {
        "title": "Bowing in the house of Rimmon",
        "intro": [
            "Take the second preset. The sovereign commands an outward act (C), the "
            "Christian obeys (G), and obeying such a command leaves the faith (F) "
            "untouched, as Naaman's did.",
        ],
        "lines": [
            "premises:  S iff (F and G);  (C and G) → F;  C;  G",
            "from C and G:  F",
            "from F and G:  S",
            "letters S, F, G, C: 16 rows, counterexamples 0",
            "verdict: valid",
        ],
        "after": [
            "Without the premise about faith (the third preset), one row survives: "
            "C and G true, F false, S false, which is a man who obeyed the command and "
            "has not the faith; the lab cannot say whether he lost it by obeying or never "
            "had it. A Covenanter says it is lost, because on his view to confess before "
            "men is part of faith. Hobbes's premise says it is not.",
        ],
    },
    "quiz_title": "Obedience and salvation",
    "quiz": [
        {"q": 'Which premise does the Covenanter preset leave out?',
         "a": [
               'That salvation needs faith and obedience',
               'That obeying a command to an outward act leaves the faith',
               'That the sovereign commanded something',
               'That the Christian obeyed',
         ],
         "c": 1,
         "why": 'The third preset keeps the rule, the command and the obedience and '
                'drops the premise about faith, and then one row has the faith lost. '
                'The others are all still premises.'},
        {"q": 'What does the more articles preset show?',
         "a": [
               'Obedience is never enough',
               'Faith in Christ is not necessary',
               'If a further article is required, faith and obedience no longer suffice',
               'The sovereign is wrong',
         ],
         "c": 2,
         "why": 'With M a further condition, the row where F and G hold and M fails '
                "leaves S false, so G does not imply S. Hobbes's five arguments are all "
                'for the claim that no further article is necessary.'},
        {"q": 'What does Hobbes say is the one article necessary to salvation?',
         "a": [
               'That Jesus is the Christ',
               'That the Pope is the head of the church',
               'That the Trinity is three persons',
               'That the Scripture is the word of God',
         ],
         "c": 0,
         "why": 'He says the only article of faith the Scripture makes simply necessary '
                'is that Jesus is the Christ. He says Christians do not know but '
                'believe the Scripture to be the word of God, and he treats the others '
                'as contained in the one.'},
        {"q": 'What does Hobbes say of a minister of Christ who is not also a '
              'sovereign?',
         "a": [
               'He has the power to excommunicate on his own authority',
               'He has the power to teach and persuade, not to command',
               'He has the power to depose kings',
               'He has no power at all',
         ],
         "c": 1,
         "why": 'He says preachers have not magisterial but ministerial power, that '
                'they are schoolmasters and not commanders, and that the power of '
                'excommunication has force only from the civil sovereign. He does not '
                'say they have no power: they teach.'},
    ],
    "mistakes": [
        ("Thinking Hobbes says a Christian must give up conscience",
         "He says belief cannot be commanded and does not follow commands, and that "
         "what a subject does outwardly under the sovereign's law is the sovereign's "
         "act. The lab's second preset keeps the faith while obeying. What he asks "
         "is that the outward act and the inward belief be kept apart."),
        ("Thinking the argument shows the sovereign cannot err",
         "He says a Christian king may draw false consequences from the one "
         "article, and that the subject who teaches by command or believes his teacher "
         "may still be saved. His point is that nobody else may judge, not that "
         "the king cannot be wrong."),
        ("Reading validity as the Covenanters' defeat",
         "The first preset is valid. The Covenanter denies a premise: that no further "
         "article is needed, or that the outward act leaves the faith. The lab "
         "shows where; it does not choose."),
    ],
    "standard": (
        "Finish when you can name the premise a critic would deny.",
        "Given the argument that obeying the sovereign never costs salvation, write it "
        "as premises, show it valid, and find the counterexample that appears when each "
        "of two premises is dropped."
    ),
    "note": (
        "The lab shows that the conclusion follows from premises written for the "
        "lesson. It cannot say whether faith is only an inward article, whether "
        "outward profession can be commanded without sin, or whether the apostles' "
        "successors have power to command; those are the questions on which Hobbes, "
        "Bellarmine and the Covenanters divided."
    ),
}

LESSONS = [L5, L6, L7, L8]
