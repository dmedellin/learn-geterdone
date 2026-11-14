"""Dominion, Liberty and the Parts of a Commonwealth, lessons 1-4 -- Chapters 20 to 23.

Every quotation is from Hobbes's text of 1651 as printed in the operator's copy
(Tuck's Cambridge edition, 1996), in its original spelling; the comment beside
each lesson gives the chapter, the 1651 page and the PDF page. Hobbes's
marginal notes are his; Tuck's footnotes are not used.

All four labs are levkit labs. Their cfg is drafted from docs/leviathan/PLAN.md
section D.1 with expect {} and is corrected against docs/leviathan/kit-report.md
in phase B.
"""

# The covenant lab's one set of numbers: victor first, vanquished second.
# Invented for the lesson; Hobbes gives none.
_VICTOR = {"first": "victor", "second": "vanquished",
           "cost1": "5", "gain1": "60", "cost2": "20", "gain2": "100"}

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Leviathan ch. 20, 1651 p. 104; PDF p. 237 of the operator's copy.
    {
        "slug": "dominion-paternal-and-despotical",
        "title": "Dominion Paternal and Despotical",
        "module": "Chapter 20 · Of Dominion Paternall, and Despoticall",
        "one_line": "A conqueror's right comes from the vanquished man's covenant and not from the victory, and a covenant made from fear still binds.",
        "summary": (
            "Chapter 20 adds a second way to make a commonwealth, by acquisition, and "
            "finds its rights the same as by institution. A child's dominion comes from "
            "consent, and a conquered man is a servant only after he covenants. Test "
            "the vanquished man's covenant with a victor who performs first: with no "
            "sword behind it breaking pays, and with one that falls often enough keeping does."
        ),
        "key": [
            "dominion by consent, not by begetting",
            "no contract: the child is the mother's",
            "victory alone binds no one",
            "the vanquished's covenant makes a servant",
            "keep = gain − cost; break = gain − odds·fine",
        ],
        "key_label": "Dominion in five lines",
        "concepts_intro": (
            "Chapter 20 is short, and it does three jobs: it says what kind of "
            "commonwealth a conquest makes, where a parent's power comes from, and what "
            "turns a prisoner into a servant."
        ),
        "concepts": [
            ("Commonwealth by acquisition",
             "A commonwealth by acquisition is one where men, for fear of death or "
             "bonds, authorise the actions of the man or assembly that has their lives "
             "and liberty in his power. It differs from one by institution only in whom "
             "they fear, and the rights of the sovereign are the same in both."),
            ("Paternal dominion",
             "A parent's dominion over a child does not come from begetting it. It comes "
             "from the child's consent, and in the state of nature, with no marriage law, "
             "it belongs to the mother unless the parents contract otherwise."),
            ("Despotical dominion",
             "A master's dominion over a servant is acquired when the vanquished, to avoid "
             "the stroke of death, covenants that while his life and bodily liberty are "
             "left him the victor may use them as he pleases. A captive in bonds has made "
             "no such covenant and owes nothing."),
        ],
        "read_title": "The passage first, then the chapter line by line",
        "read_intro": (
            "The passage is the chapter's turning point, where Hobbes says what a "
            "victory does and does not do. The chapter is worth taking in its own order."
        ),
        "body": [
            ("p", "<strong>Chapter 20.</strong> &ldquo;It is not therefore the Victory, "
                  "that giveth the right of Dominion over the Vanquished, but his own "
                  "Covenant. Nor is he obliged because he is Conquered; that is to say, "
                  "beaten, and taken, or put to flight; but because he commeth in, and "
                  "Submitteth to the Victor;&rdquo;"),
            ("p", "Consider how odd that sounds the first time. A man has been beaten, his "
                  "life is in the winner's hands, and Hobbes says the winner's right does "
                  "not come from winning. It comes from something the beaten man does "
                  "afterwards. The sentence only makes sense once you remember what the "
                  "last three chapters built: for Hobbes every obligation comes from an act "
                  "of the person obliged, and being overpowered is not an act of his."),
            ("p", "The chapter begins by joining two kinds of commonwealth. Chapters 17 to "
                  "19 described one made by institution, where a multitude agree among "
                  "themselves to authorise a sovereign. Now Hobbes defines the other: &ldquo;A "
                  "Common-wealth by Acquisition, is that, where the Soveraign Power is "
                  "acquired by Force&rdquo;. "
                  "The two differ, he says, &ldquo;onely in this&rdquo;: that in the first men "
                  "choose their sovereign &ldquo;for fear of one another, and not of him "
                  "whom they Institute&rdquo;, while in the second they submit to the man "
                  "they are afraid of. &ldquo;In both cases they do it for fear&rdquo;."),
            ("p", "That sentence answers an objection already waiting for him: that a promise "
                  "squeezed out by fear is void. Hobbes says that if this were true, &ldquo;no man, in any "
                  "kind of Common-wealth, could be obliged to Obedience&rdquo;, "
                  "since everyone obeys for fear of the law. A promise made under threat "
                  "does fail to oblige, he allows, when the thing promised is contrary to the "
                  "laws, but the reason is &ldquo;not, because it was made upon fear, but "
                  "because he that promiseth, hath no right in the thing promised&rdquo;."),
            ("p", "Then comes the family. Dominion over children, he says, is called "
                  "paternal, but it is &ldquo;not so derived from the Generation, as if "
                  "therefore the Parent had Dominion over his Child because he begat "
                  "him&rdquo;. It comes from the child's consent, &ldquo;either expresse, or "
                  "by other sufficient arguments declared&rdquo;. The view he rejects "
                  "was held by patriarchal royalists, Sir Robert Filmer the best known, who rooted "
                  "kingship in the fatherhood of Adam, so that a king's power over his "
                  "subjects was a father's power over his children. Hobbes defends "
                  "monarchy as hard as any of them, but not on that ground; he has "
                  "argued from covenant since Chapter 14, and he keeps to it here."),
            ("p", "His next move is the one readers remember. Two parents are always "
                  "involved, so the dominion would have to belong equally to both, and "
                  "&ldquo;no man can obey two Masters&rdquo;. Those who give it to the "
                  "father because of his &ldquo;more excellent Sex&rdquo; &ldquo;misreckon "
                  "in it&rdquo;, since the two are not always unequal in strength or "
                  "prudence. In a commonwealth civil law settles it, and usually for the "
                  "father, because commonwealths were mostly erected by fathers. In the "
                  "state of nature, where there is no marriage law, the parents either "
                  "contract or they do not, and &ldquo;If there be no Contract, the "
                  "Dominion is in the Mother&rdquo;, because only she can declare who the "
                  "father is and she may nourish the infant or expose it. If another finds "
                  "and nourishes it, the dominion is his: every man is supposed to "
                  "promise obedience &ldquo;to him, in whose power it is to save, or "
                  "destroy him&rdquo;."),
            ("p", "That last clause is the hinge to the rest of the chapter. Preservation of "
                  "life is the end for which one man becomes subject to another, and Hobbes "
                  "now applies it to the vanquished. He distinguishes a captive from a "
                  "servant. A captive is &ldquo;kept in prison, or bonds&rdquo;, and such men "
                  "&ldquo;have no obligation at all; but may break their bonds, or the "
                  "prison; and kill, or carry away captive their Master, justly&rdquo;. A "
                  "servant is one who, being taken, has bodily liberty allowed him and, "
                  "on a promise not to run away or do violence, is trusted. The "
                  "vanquished is a servant &ldquo;and not before&rdquo; he has covenanted."),
            ("p", "Quarter works the same way. A man who asks quarter, Hobbes says, does "
                  "not have his life given but &ldquo;deferred till farther "
                  "deliberation&rdquo;; it is not a yielding on condition of life, &ldquo;but "
                  "to discretion&rdquo;. His life is in security, and his service due, "
                  "&ldquo;when the Victor hath trusted him with his corporall "
                  "liberty&rdquo;. Notice who goes first. The victor extends the trust, and "
                  "the vanquished then owes obedience."),
            ("p", "The lab turns that into a sum. The victor spends something to spare "
                  "and keep him and gets his service in return; the vanquished gets his "
                  "life and liberty and pays in service. The figures are invented for the "
                  "lesson: the victor gives up 5 and gains 60, the vanquished gives up 20 "
                  "and gains 100. With the first preset, <em>no-sanction</em>, nothing "
                  "stands behind the promise: keeping is worth 80 to the servant and "
                  "breaking 100, so he does better to break, and the victor who "
                  "performs first loses his 5. In <em>half-certain</em> the victor's sword "
                  "is a fine of 100 applied half the time, so breaking is worth 50 and "
                  "keeping wins. In <em>tenth-certain</em> it is applied one time in ten, "
                  "breaking is worth 90, and the servant breaks again; the least fine "
                  "that would hold him at that certainty is 200. What the sum shows is "
                  "why Hobbes says trust is needed and a sword behind it."),
            ("p", "Hobbes's rule that fear does not void a covenant has had critics from "
                  "the start. Locke, writing in the 1680s, set paternal, political and "
                  "despotical power side by side in one chapter and gave another to "
                  "conquest, and argued that a conqueror in an unjust war gets no right "
                  "over those he beats: a power to kill is not a right to rule. His "
                  "ground is that rights come from consent that is free, and Hobbes's "
                  "reply is already on the page: if fear voided consent, there would "
                  "be no obligation anywhere. The question mattered in England in 1651, "
                  "when men who had lived under a king were being asked what they owed to "
                  "those who had beaten him. The lab cannot decide between them. It "
                  "shows only what keeping and breaking are worth once the covenant is made."),
            ("p", "Then Hobbes sums up. The rights of the master and the parent are "
                  "&ldquo;the very same with those of a Soveraign by Institution&rdquo;, "
                  "and a monarch who rules one nation by institution and another by "
                  "conquest who asks more of the conquered one &ldquo;is an act of "
                  "ignorance of the Rights of Soveraignty&rdquo;, since the sovereign "
                  "&ldquo;is absolute over both alike; or else there is no Soveraignty at "
                  "all&rdquo;. A large family not part of any commonwealth is a little "
                  "monarchy; if it is too weak to be safe from an army, each member may "
                  "&ldquo;use his own reason in time of danger, to save his own life&rdquo;."),
            ("p", "The rest of the chapter reads Scripture for the same conclusion. "
                  "Hobbes takes God's description of the king Israel asked for, who will "
                  "take your sons and your fields and tithes, as a statement of the "
                  "king's right, summed up in the words &ldquo;you shall be his "
                  "servants&rdquo;. Others read the passage as a warning against "
                  "wanting a king. Both readings had readers in 1651, and it is "
                  "Hobbes's you will meet again in Part III. His own conclusion is "
                  "that sovereign power is &ldquo;as great, as possibly men can be "
                  "imagined to make it&rdquo;, and that the ills of the want of it "
                  "are much worse. The next lesson, <em>Liberty and Necessity</em>, "
                  "asks what is left to a subject under a power that great."),
        ],
        "lab": ("levkit", {
            "mode": "covenant",
            "view": "perform",
            "preset": "no-sanction",
            "presets": [
                dict(_VICTOR, id="no-sanction",
                     label="The victor performs first, with no sword behind the promise",
                     sanction="0", certainty="1", expect={
                    "lcvChoice": "vanquished breaks: 100 against 80",
                    "lcvReasonable": "no: −5 against 0 for not performing",
                    "lcvLeast": "20 (cost2 ÷ certainty)"}),
                dict(_VICTOR, id="half-certain",
                     label="A fine of 100, applied half the time",
                     sanction="100", certainty="1/2", expect={
                    "lcvChoice": "vanquished keeps: 80 against 50",
                    "lcvFirst": "55, since vanquished keeps",
                    "lcvLeast": "40 (cost2 ÷ certainty)"}),
                dict(_VICTOR, id="tenth-certain",
                     label="The same fine, applied one time in ten",
                     sanction="100", certainty="1/10", expect={
                    "lcvChoice": "vanquished breaks: 90 against 80",
                    "lcvBreak": "90",
                    "lcvLeast": "200 (cost2 ÷ certainty)"}),
            ],
            "panel_title": "Does the vanquished man keep his covenant?",
            "panel_intro": (
                "A figure computed from what the lesson states. The victor performs first and trusts the vanquished man; the lab compares what he gets by keeping the covenant with what he gets by breaking it, at the penalty and chance given, and says whether the victor does well to go first. Whether men reason this way is what the book argues."
            ),
        }),
        "steps_title": "Testing a covenant where one side goes first",
        "steps_intro": "Four steps, the same for any covenant where trust is given before performance.",
        "steps": [
            ("Name who performs first",
             "Say which party trusts the other. Here the victor spares and releases; "
             "the vanquished owes service only after that, as a servant and not a captive."),
            ("Price both sides",
             "For each party write what performing costs and what the other's performing "
             "gains. The figures are the lesson's, not Hobbes's."),
            ("Compare keeping with breaking for the second party",
             "Keeping is gain minus cost. Breaking is gain minus the penalty times the "
             "chance it is applied. He keeps when keeping is at least as good."),
            ("Ask whether going first is reasonable",
             "The first party gains service if the second keeps and loses his outlay "
             "if not. Going first is reasonable when the first case is the one that follows."),
            ("Find the least penalty",
             "The penalty that makes keeping at least as good is the second party's cost "
             "of performing divided by the chance the penalty is applied."),
        ],
        "worked": {
            "title": "The vanquished man's choice at even odds",
            "intro": [
                "Take the second preset. The victor spares the vanquished man, which costs "
                "him 5 and gains him 60 in service. The vanquished gets his life and "
                "liberty, worth 100 to him, and serving costs him 20. The fine for "
                "breaking is 100 and is applied half the time.",
            ],
            "lines": [
                "keep:  100 − 20 = 80",
                "break:  100 − 100/2 = 50",
                "80 > 50, so he keeps",
                "victor goes first:  60 − 5 = 55 > 0",
                "least fine at even odds:  20 / (1/2) = 40",
            ],
            "after": [
                "Make the odds one in ten and breaking is worth 90, more than 80, so the "
                "victor who goes first loses his 5. The least fine at those odds is "
                "20 / (1/10) = 200, twice the fine in force.",
            ],
        },
        "quiz_title": "Where dominion comes from",
        "quiz": [
            {"q": "On Hobbes's account in Chapter 20, what gives the victor dominion over "
                  "the vanquished?",
             "a": ["The victory itself, which puts the loser in his power",
                   "The vanquished man's covenant to serve, made to save his life",
                   "The victor's decision to spare his life, whether or not he covenants",
                   "The vanquished man's capture, once he is held in chains"],
             "c": 1,
             "why": "&ldquo;It is not therefore the Victory, that giveth the right of "
                    "Dominion over the Vanquished, but his own Covenant.&rdquo; A man kept "
                    "in bonds has made no covenant and is no servant, and quarter only "
                    "defers his life."},
            {"q": "In the lab's second preset the vanquished man's keeping is worth 80 and "
                  "his breaking is worth 50. What does he do, and why?",
             "a": ["Breaks, because breaking pays him 100",
                   "Breaks, because the fine applies only half the time",
                   "Keeps, because 80 is more than 50",
                   "Keeps, because a covenant made from fear is void"],
             "c": 2,
             "why": "Breaking is `100 − 100/2 = 50`, less than the 80 for keeping. The "
                    "figure 100 is breaking with no fine, as in the first preset. Hobbes "
                    "says fear does not void such a covenant, so the last answer's "
                    "reason is false as well."},
            {"q": "Two people in the state of nature have a child and make no contract "
                  "about it. Whose is the dominion over the child?",
             "a": ["The mother's, since she can nourish or expose it and only she can "
                   "declare who the father is",
                   "The father's, because the man is the more excellent sex",
                   "Both parents equally, since both begat the child",
                   "Whoever first sees the child after its birth"],
             "c": 0,
             "why": "Hobbes: &ldquo;If there be no Contract, the Dominion is in the "
                    "Mother.&rdquo; He rejects the father's claim from sex, and dominion "
                    "to both is impossible because no man can obey two masters."},
            {"q": "A prisoner is kept in chains and has made no promise. What does "
                  "Hobbes say he owes his master?",
             "a": ["Service, because he was beaten in war",
                   "Service, because the master has spared his life",
                   "Obedience for as long as the chains hold",
                   "Nothing: he may break out and kill his master, justly"],
             "c": 3,
             "why": "Such men &ldquo;have no obligation at all; but may break their "
                    "bonds, or the prison; and kill, or carry away captive their Master, "
                    "justly&rdquo;. A servant is a different case: he has covenanted "
                    "and been trusted with his bodily liberty."},
        ],
        "mistakes": [
            ("Thinking the victor's right comes from the victory",
             "It is the commonest reading and Hobbes rules it out in the passage the "
             "lesson opens with. A man beaten and taken is not obliged &ldquo;because he is "
             "Conquered&rdquo;; he is obliged because he &ldquo;commeth in, and Submitteth "
             "to the Victor&rdquo;. Without the covenant he is a captive, and a captive may "
             "escape and kill his master, justly."),
            ("Thinking a covenant made from fear is void",
             "Hobbes raises this himself and says that if it were true, no one in any "
             "commonwealth could be bound, since all obey for fear of something. "
             "Institution too is made for fear, of one another. A promise to do what the "
             "law forbids does not bind, but not because it was made from fear."),
            ("Thinking a father has dominion because he begat the child",
             "Dominion is not &ldquo;derived from the Generation&rdquo;. It comes from the "
             "child's consent, and in the state of nature, with no marriage law and no "
             "contract, it falls to the mother, who may nourish or expose the infant. "
             "In a commonwealth civil law decides, and mostly for the father."),
        ],
        "standard": (
            "Finish when you can test a covenant made by a beaten man.",
            "Given the figures for a victor who performs first and a vanquished man who "
            "serves, compute what keeping and breaking are worth to the second party at a "
            "stated penalty and certainty, say whether the first party does well to go "
            "first, and find the least penalty that holds the covenant."
        ),
        "note": (
            "The sum treats keeping a covenant as a comparison of payoffs. Hobbes's "
            "claim is also about obligation: that the vanquished man is bound by his "
            "own covenant, whatever he gains by breaking it. The lab can show when "
            "breaking pays, not whether he ought to keep faith. All the figures are "
            "invented for the lesson, and whether a promise made to save one's life binds "
            "at all is what Hobbes and Locke disagree about."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Leviathan ch. 21, 1651 p. 107; PDF p. 241 of the operator's copy.
    {
        "slug": "liberty-and-necessity",
        "title": "Liberty and Necessity",
        "module": "Chapter 21 · Of the Liberty of Subjects",
        "one_line": "Liberty is the absence of external impediments, consistent with fear and with necessity, and a subject's liberty lies where the law is silent.",
        "summary": (
            "Hobbes defines liberty as the absence of external impediments to motion. "
            "On that definition a man who acts from fear is free, and so is a man whose "
            "every act has a cause. A subject's liberty lies in what the laws leave "
            "alone. Sort a set of actions under three laws into commanded, forbidden "
            "and free, and watch a statute shrink the free part."
        ),
        "key": [
            "liberty = no external impediment",
            "fear and liberty are consistent",
            "liberty and necessity are consistent",
            "civil laws are artificial chains",
            "free = neither commanded nor forbidden",
        ],
        "key_label": "Liberty in five lines",
        "concepts_intro": (
            "Chapter 21 begins from the word itself and works up to what a subject may "
            "do. Three ideas carry the first half."
        ),
        "concepts": [
            ("Liberty as the absence of impediment",
             "A free man is one who in the things he is able to do is not hindered from "
             "doing what he has a will to. An impediment must be external: a stone that "
             "lies still lacks the power to move, not the liberty."),
            ("Fear, necessity and the chain of causes",
             "A man who throws goods overboard to save a sinking ship acts freely, for he "
             "might refuse. Every act of will also has a cause, and that another, so "
             "liberty and necessity are consistent, as water has both in descending the "
             "channel."),
            ("Artificial chains and the silence of the law",
             "Civil laws are artificial chains men fasten from the sovereign's lips to "
             "their own ears. No laws cover every action, so a subject is free in "
             "whatever the laws leave out, and that varies with place and time."),
        ],
        "read_title": "The passage first, then the chapter line by line",
        "read_intro": (
            "Hobbes starts from a word everyone uses and shows that his definition is the "
            "ordinary one. Then he turns it on the claims made in its name."
        ),
        "body": [
            ("p", "<strong>Chapter 21.</strong> &ldquo;LIBERTY, or FREEDOME, signifieth "
                  "(properly) the absence of Opposition; (by Opposition, I mean "
                  "externall Impediments of motion;) and may be applyed no lesse to "
                  "Irrationall, and Inanimate creatures, than to Rationall.&rdquo;"),
            ("p", "Think of water in a channel, or a dog on a lead. We say the water is "
                  "not at liberty to spread out while the banks hold it, and the dog is "
                  "not at liberty to run while it is tied. Hobbes says that is the whole "
                  "idea, and that it works the same for men: &ldquo;A FREE-MAN, is he, that "
                  "in those things, which by his strength and wit he is able to do, is "
                  "not hindred to doe what he has a will to&rdquo;. A stone that lies "
                  "still, or a man fastened to his bed by sickness, lacks &ldquo;the Power "
                  "to move&rdquo; and not the liberty, because what stops them is in "
                  "their own constitution. The impediment has to come from outside."),
            ("p", "He is quick to say what follows. Applied to anything but bodies the words "
                  "are abused. &ldquo;The way is Free&rdquo; means that those who walk it are "
                  "not stopped; a gift is free because the giver was not bound; and the "
                  "words &ldquo;Free-will&rdquo; tell us about the man, who finds no stop in "
                  "doing what he wills, and nothing about a liberty of the will."),
            ("p", "Then two claims that made him enemies. First, &ldquo;Feare, and Liberty "
                  "are consistent&rdquo;. The man who throws his goods into the sea does it "
                  "&ldquo;very willingly, and may refuse to doe it if he will&rdquo;; so does "
                  "the man who pays a debt for fear of prison, and generally &ldquo;all "
                  "actions which men doe in Common-wealths, for feare of the law, are "
                  "actions, which the doers had liberty to omit&rdquo;. Second, &ldquo;Liberty, "
                  "and Necessity are consistent&rdquo;: every act of will proceeds from a "
                  "cause, and that from another, in a chain whose first link &ldquo;is in "
                  "the hand of God the first of all causes&rdquo;."),
            ("p", "The second claim had a history with a person in it. In Paris in the "
                  "mid-1640s, among the royalist exiles, Hobbes debated free will with "
                  "John Bramhall, the exiled Bishop of Derry, and the papers "
                  "later circulated in print. Bramhall held that if every act is "
                  "necessitated, praise and blame and the justice of punishment fall "
                  "apart, and God becomes the author of sin. Hobbes's reply in this "
                  "chapter is brief. Men may do many things God does not command, he says, "
                  "&ldquo;nor is therefore Author of them&rdquo;, yet no appetite exists "
                  "that God's will is not the cause of. Whether that answers the bishop "
                  "is something Hobbes's readers have argued about since; later "
                  "philosophers call his position compatibilism, and it has never been "
                  "without opponents."),
            ("p", "Now the political turn. Men made an artificial man, the commonwealth, and so, he says, "
                  "also &ldquo;Artificiall Chains, called Civill Lawes&rdquo;, fastened "
                  "at one end to the lips of the sovereign and at the other to their own "
                  "ears. The chains are weak in themselves, but they hold &ldquo;by the "
                  "danger, though not by the difficulty of breaking them&rdquo;. So the "
                  "liberty of subjects is a liberty from those chains, and since no "
                  "commonwealth has rules enough for every action, &ldquo;in all kinds "
                  "of actions, by the laws praetermitted, men have the Liberty, of "
                  "doing what their own reasons shall suggest, for the most profitable "
                  "to themselves&rdquo;. His list is ordinary: to buy and sell and contract "
                  "with one another, to choose one's abode, diet and trade, and to bring "
                  "up one's children as one thinks fit."),
            ("p", "That is what the lab computes. Eight actions, seven taken from Hobbes's "
                  "examples and paying tax added, go in, with the laws a commonwealth has made. In "
                  "<em>england-before</em> a tax law commands paying tax and a "
                  "marriage law forbids many wives; six of the eight are free, 75 percent. "
                  "Hobbes's own example is that there was a time when in England a man "
                  "might enter his own land by force and dispossess a wrongful occupier, "
                  "until a statute took that liberty away. <em>after-statute</em> adds "
                  "the statute: forcible entry is forbidden, and five of eight are left "
                  "free. The third preset, <em>elsewhere</em>, drops the marriage law: "
                  "Hobbes says that in some places men have the liberty of many wives "
                  "and in others not, and the lab shows six free again, but not the "
                  "same six."),
            ("p", "He is careful about what this liberty does not do. It does not abolish "
                  "or limit the sovereign's power of life and death, since nothing the "
                  "sovereign does to a subject can be an injury to him: every subject is "
                  "author of every act the sovereign does. David killing Uriah wronged God, "
                  "Hobbes says, and not Uriah, because the right to do what he pleased "
                  "was given him by Uriah himself. Athens banished men by oyster-shell "
                  "without asking what they had done, and yet &ldquo;a man cannot say, the "
                  "Soveraign People of Athens wanted right to banish them&rdquo;."),
            ("p", "The last part of the chapter's first half takes on a prize word. The "
                  "liberty praised in the histories of the Greeks and Romans, he says, "
                  "&ldquo;is not the Libertie of Particular men; but the Libertie of the "
                  "Common-wealth&rdquo;. He points to the word LIBERTAS written on the "
                  "towers of Lucca, and says no one can infer from it that a man in Lucca "
                  "has more immunity from the service of the commonwealth than one in "
                  "Constantinople. Whether a commonwealth be monarchical or popular, the "
                  "freedom is the same. He adds that men have drunk this from Aristotle "
                  "and Cicero, who lived in popular states, and have got from it a habit "
                  "of favouring tumults."),
            ("p", "Here Hobbes has opponents with a serious case. The republicans of his "
                  "day, such as James Harrington, argued that there is a real difference "
                  "between a city governed by laws that its citizens make and one ruled "
                  "by a master's will, and that the first is free in a sense the "
                  "second is not, even if each subject is equally bound. Hobbes's answer "
                  "is the definition he began with: liberty is the absence of "
                  "external impediment, and both the citizen of Lucca and the subject "
                  "of the Sultan meet the same sort of chain. The lab can count only "
                  "what is left unregulated; it cannot say whether who makes the "
                  "chains ought to matter."),
            ("p", "That count is the first half of the chapter's political half. The "
                  "second, <em>The True Liberty of Subjects</em>, asks what a subject "
                  "may refuse even when the sovereign commands it."),
        ],
        "lab": ("levkit", {
            "mode": "law",
            "view": "silence",
            "preset": "england-before",
            "presets": [
                {"id": "england-before",
                 "label": "A tax law and a marriage law",
                 "actions": "buy-and-sell choose-abode choose-diet choose-trade educate-children forcible-entry many-wives pay-tax",
                 "laws": "tax-law, pay-tax, -; marriage-law, -, many-wives",
                 "expect": {
                    "llwFree": "6: buy-and-sell, choose-abode, choose-diet, choose-trade, educate-children, forcible-entry",
                    "llwShareFree": "6 of 8: 3/4 = 75%"}},
                {"id": "after-statute",
                 "label": "The same laws and a statute against forcible entry",
                 "actions": "buy-and-sell choose-abode choose-diet choose-trade educate-children forcible-entry many-wives pay-tax",
                 "laws": "tax-law, pay-tax, -; marriage-law, -, many-wives; entry-statute, -, forcible-entry",
                 "expect": {
                    "llwForbidden": "2: forcible-entry, many-wives",
                    "llwShareFree": "5 of 8: 5/8 = 62.5%"}},
                {"id": "elsewhere",
                 "label": "A place with the tax law and the statute but no marriage law",
                 "actions": "buy-and-sell choose-abode choose-diet choose-trade educate-children forcible-entry many-wives pay-tax",
                 "laws": "tax-law, pay-tax, -; entry-statute, -, forcible-entry",
                 "expect": {
                    "llwFree": "6: buy-and-sell, choose-abode, choose-diet, choose-trade, educate-children, many-wives",
                    "llwShareFree": "6 of 8: 3/4 = 75%"}},
            ],
            "panel_title": "What the laws leave free",
            "panel_intro": (
                "A figure computed from what the lesson states. The lab sorts a set of actions, under the laws given, into commanded, forbidden and free, and lists any that two laws contradict. Whether Hobbes’s definition of liberty is the right one is what the book argues."
            ),
        }),
        "steps_title": "Finding a subject's liberty in a set of laws",
        "steps_intro": "Four steps, the same for any list of actions and any set of laws.",
        "steps": [
            ("List the actions",
             "Write down the things a person might do that are in question, one name each."),
            ("Mark what each law commands and forbids",
             "Go through the laws one at a time and note which actions each commands "
             "and which it forbids."),
            ("Check for a contradiction",
             "An action both commanded and forbidden is a fault in the laws, and "
             "the lab lists it separately. Settle those before counting."),
            ("Count what is left",
             "An action neither commanded nor forbidden is free, by the silence of the "
             "law. The free share is the free actions over all of them."),
        ],
        "worked": {
            "title": "Eight actions under two laws, then three",
            "intro": [
                "Take the first preset. The eight actions are to buy and sell, choose "
                "an abode, a diet and a trade, educate one's children, enter land by "
                "force, take many wives and pay the tax. The tax law commands the last "
                "and the marriage law forbids the second to last.",
            ],
            "lines": [
                "commanded:  pay-tax = 1",
                "forbidden:  many-wives = 1",
                "free:  8 − 1 − 1 = 6",
                "free share:  6/8 = 75%",
                "with the statute:  8 − 1 − 2 = 5, 5/8 = 62.5%",
            ],
            "after": [
                "The statute against forcible entry takes one action out of the free "
                "set. Drop the marriage law instead, as in the third preset, and many "
                "wives is free again while forcible entry stays forbidden: six free "
                "and a different six.",
            ],
        },
        "quiz_title": "Liberty by the definition",
        "quiz": [
            {"q": "A man throws his goods into the sea to save a sinking ship. On Hobbes's "
                  "definition, is the act free?",
             "a": ["Yes, because no one hindered him and he could have refused",
                   "No, because fear of drowning compelled it",
                   "No, because every act has a cause and so is necessary",
                   "Yes, but only because the ship is his own"],
             "c": 0,
             "why": "&ldquo;Feare, and Liberty are consistent&rdquo;: he does it &ldquo;very "
                    "willingly, and may refuse to doe it if he will&rdquo;. Liberty is the "
                    "absence of external impediment, and fear is not one. Necessity of "
                    "causes does not remove it either, and ownership plays no part."},
            {"q": "In the lab's first preset, how many of the eight actions are free, and "
                  "what share is that?",
             "a": ["6 of 8, 75%", "5 of 8, 62.5%", "7 of 8, 87.5%", "8 of 8, 100%"],
             "c": 0,
             "why": "One action is commanded and one forbidden, so `8 − 1 − 1 = 6` are "
                    "free, `6/8 = 75%`. Five is the count after the statute against "
                    "forcible entry is added, and seven would leave out one of the laws."},
            {"q": "What does Hobbes say the word LIBERTAS on the towers of Lucca shows "
                  "about a Lucchese's liberty?",
             "a": ["That a man in Lucca has more immunity from the commonwealth's service "
                   "than one in Constantinople",
                   "That Lucca's citizens, being free, may resist their own magistrates",
                   "That the liberty is the commonwealth's, and that no man can infer "
                   "from it a particular man's greater liberty",
                   "That a republic is freer than a monarchy"],
             "c": 2,
             "why": "&ldquo;Whether a Common-wealth be Monarchicall, or Popular, the "
                    "Freedome is still the same.&rdquo; The word names the liberty of the "
                    "commonwealth to resist or invade other peoples, not of its "
                    "individual men."},
            {"q": "Where, according to Chapter 21, does a subject's liberty lie?",
             "a": ["In the exemption of subjects from every law the sovereign makes",
                   "In what the laws command, since obeying them is rational",
                   "In the sovereign's covenant not to harm his subjects",
                   "In the things the sovereign has left unregulated"],
             "c": 3,
             "why": "&ldquo;The Liberty of a Subject, lyeth therefore only in those things, "
                    "which in regulating their actions, the Soveraign hath praetermitted&rdquo;. "
                    "Exemption from laws would let all other men be masters of one's life, "
                    "and the sovereign covenants nothing with his subjects."},
        ],
        "mistakes": [
            ("Thinking fear takes liberty away",
             "Hobbes says the opposite: the man who acts from fear acts freely, as "
             "the debtor does who pays to avoid prison. What would take liberty is a "
             "bodily impediment, such as chains or a locked door. Under Hobbes's "
             "definition a person coerced by a threat is still free to refuse."),
            ("Thinking liberty and necessity cannot both be true of one act",
             "Hobbes holds that an act is free because it proceeds from the actor's will "
             "and necessary because the will has its own causes, as water both "
             "descends of its own channel and must. Bramhall and other opponents denied "
             "that this keeps a place for responsibility; Hobbes thought it did."),
            ("Reading the liberty praised by the Greeks and Romans as each man's liberty",
             "Hobbes says it is the liberty of the commonwealth, which every "
             "commonwealth has against its neighbours, monarchical or popular. A "
             "particular man at Lucca, where LIBERTAS is written on the towers, "
             "has no more immunity from the service of the commonwealth than one "
             "at Constantinople."),
        ],
        "standard": (
            "Finish when you can sort a list of actions under a set of laws.",
            "Given a list of actions and the laws a commonwealth has made, state which "
            "actions are commanded, forbidden and free, find any that are both commanded "
            "and forbidden, and say how a new law changes the free share."
        ),
        "note": (
            "The lab counts only what the laws leave unregulated. It cannot say whether "
            "Hobbes's definition of liberty is the right one, which is what the "
            "republicans disputed, or whether acting from necessity can still be "
            "praised or blamed, which is what Bramhall disputed. The eight actions come "
            "from Hobbes's examples (paying tax is added) and the laws are invented for the lesson."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Leviathan ch. 21, 1651 pp. 111-112 (the marker [112] falls at the passage's last line); PDF p. 247 of the operator's copy.
    {
        "slug": "the-true-liberties-of-subjects",
        "title": "The True Liberty of Subjects",
        "module": "Chapter 21 · Of the Liberty of Subjects",
        "one_line": "A subject keeps the liberty to refuse what no covenant could transfer, such as killing himself, and his obligation lasts as long as the sovereign can protect him.",
        "summary": (
            "Chapter 21 goes on to what a subject may refuse though commanded, and "
            "finds it by asking what rights men gave up in making a sovereign. A man "
            "need not kill himself or accuse himself, and the obligation to obey lasts "
            "as long as protection does. Run a set of commands through the law lab with "
            "the inalienable liberties marked, and see which commands a subject may "
            "still refuse."
        ),
        "key": [
            "obligation comes from an act of the subject",
            "what no covenant can transfer, he keeps",
            "no duty to kill or accuse himself",
            "a volunteer soldier may not run",
            "obedience lasts as long as protection",
        ],
        "key_label": "The true liberties in five lines",
        "concepts_intro": (
            "The chapter's second half asks the question that was left open: what may a "
            "subject refuse? Three ideas answer it."
        ),
        "concepts": [
            ("Liberty is found in the act of submission",
             "No one is obliged except by his own act, so the liberty of a subject is "
             "inferred from the words of submission, &lsquo;I authorise all his actions&rsquo;, "
             "or from the end for which he submits: peace within and defence against an "
             "enemy."),
            ("What no covenant can transfer",
             "Covenants not to defend one's own body are void, so a subject may refuse "
             "an order to kill or wound himself, not to resist those who assault him, or "
             "to go without food, air or medicine, even if justly condemned; and since "
             "no one can be obliged to accuse himself, he need not confess his own "
             "crime without assurance of pardon."),
            ("Obligation lasts as long as protection",
             "The end of obedience is protection. When the sovereign can no longer "
             "protect a subject, the subject's obligation ends, because the right of "
             "self-defence can by no covenant be relinquished."),
        ],
        "read_title": "The passage first, then the chapter line by line",
        "read_intro": (
            "Hobbes has made the sovereign absolute. Here he shows what he keeps for "
            "the subject, and the passage is the first of those liberties."
        ),
        "body": [
            ("p", "<strong>Chapter 21.</strong> &ldquo;If the Soveraign command a man "
                  "(though justly condemned,) to kill, wound, or mayme himselfe; or not "
                  "to resist those that assault him; or to abstain from the use of food, "
                  "ayre, medicine, or any other thing, without which he cannot live; "
                  "yet hath that man the Liberty to disobey.&rdquo;"),
            ("p", "You can see the shape of the argument by asking how a limit on a "
                  "sovereign who is absolute could be derived at all. Hobbes does not "
                  "reach for a bill of rights. He says that to find what a subject may "
                  "refuse we must consider &ldquo;what Rights we passe away, when we make a "
                  "Common-wealth&rdquo;, since &ldquo;in the act of our Submission, consisteth "
                  "both our Obligation, and our Liberty&rdquo;. No one is bound except by "
                  "an act of his own. So the limit has to be read from the words of the "
                  "submission, or from its end."),
            ("p", "The first answer is the passage. Chapter 14 showed that covenants "
                  "not to defend a man's own body are void, and from this Hobbes draws "
                  "the liberties in the opening sentence. He draws a second from the "
                  "same chapter: a man questioned about a crime of his own &ldquo;is not "
                  "bound (without assurance of Pardon) to confesse it&rdquo;. And he "
                  "reads the words of authorisation closely. To say &lsquo;Kill me, or my "
                  "fellow, if you please&rsquo; is not to say &lsquo;I will kill my selfe, "
                  "or my fellow&rsquo;. &ldquo;No man is bound by the words themselves, "
                  "either to kill himselfe, or any other man&rdquo;."),
            ("p", "Then he qualifies, and the qualification is the other half of the "
                  "argument. A duty to do a dangerous or dishonourable office, he says, "
                  "depends on the intention behind the submission, &ldquo;which is to be "
                  "understood by the End thereof. When therefore our refusall to obey, "
                  "frustrates the End for which the Soveraignty was ordained; then there "
                  "is no Liberty to refuse: otherwise there is.&rdquo; The soldier is the "
                  "example. He may often refuse without injustice, for instance when he "
                  "puts a sufficient substitute in his place, and allowance is to be made "
                  "&ldquo;for naturall timorousnesse&rdquo;, since armies on one side or both "
                  "run away, and when it is fear and not treachery it is not unjust "
                  "but dishonourable. But &ldquo;he that inrowleth himselfe a Souldier, or "
                  "taketh imprest mony, taketh away the excuse of a timorous nature&rdquo;, "
                  "and when the whole commonwealth is in danger every man able to bear "
                  "arms is obliged."),
            ("p", "Two more cases sharpen the line. A man has no liberty to resist the "
                  "sword of the commonwealth in defence of another, guilty or innocent, "
                  "because that would take from the sovereign the means of protecting "
                  "us. But many men who have already rebelled may join to defend one "
                  "another, since they only defend their lives, until the sovereign "
                  "offers pardon, which takes away their plea of self-defence. The rule "
                  "throughout is the one the lab uses: some liberties are inalienable "
                  "because the right behind them cannot be covenanted away, and "
                  "the others are given up because the end of the commonwealth needs them."),
            ("p", "This is the lab. Five actions go in: paying tax, serving in the war, "
                  "killing oneself, confessing one's own crime, and buying and selling. "
                  "In <em>four-commands</em> four laws command the first four, and two "
                  "of those, killing oneself and confessing, are marked inalienable with "
                  "the reasons Hobbes gives. The lab lists them as commands a subject "
                  "may still refuse, and the one action left silent, buying and "
                  "selling, is the only one free: 20 percent. In <em>ordinary-laws</em> "
                  "only the tax law and the muster law are in force, neither command "
                  "touches an inalienable liberty, and no command is refusable on those "
                  "grounds; killing oneself and confessing are then simply free, so three "
                  "of the five actions, 60 percent, are. The lab is not offering a verdict on the soldier: Hobbes's "
                  "own account is that he may refuse in some cases and not in others, "
                  "which is why the muster law is not marked inalienable."),
            ("p", "What of the liberties the sovereign grants? Hobbes handles a "
                  "familiar worry. A subject with a quarrel against the sovereign about a "
                  "debt or a piece of land, grounded on a previous law, &ldquo;hath the "
                  "same Liberty to sue for his right&rdquo; as against any subject, since "
                  "the sovereign who sues by a former law requires no more than the law "
                  "gives. But if the sovereign takes something &ldquo;by pretence of "
                  "his Power&rdquo;, there is no action at law. And a grant of liberty "
                  "that leaves him unable to provide for their safety is void, unless "
                  "he renounces the sovereignty openly."),
            ("p", "The last pages state a principle that was dangerous to say in 1651. "
                  "&ldquo;The Obligation of Subjects to the Soveraign, is understood to "
                  "last as long, and no longer, than the power lasteth, by which he is "
                  "able to protect them.&rdquo; The end of obedience, Hobbes says, is "
                  "protection, &ldquo;which, wheresoever a man seeth it, either in his "
                  "own, or in anothers sword, Nature applyeth his obedience to it&rdquo;. "
                  "He lists the cases in which a subject is freed: a prisoner who is "
                  "given his life on condition of becoming the captor's subject; a "
                  "monarch who gives up the sovereignty for himself and his heirs; "
                  "banishment; a monarch who becomes subject to the victor. The section "
                  "rests on an image from the Introduction, where sovereignty was the "
                  "artificial soul: &ldquo;The Soveraignty is the Soule of the "
                  "Common-wealth; which once departed from the Body, the members doe no "
                  "more receive their motion from it.&rdquo;"),
            ("p", "Readers on both sides took the principle as a warrant, which is why it "
                  "matters. A royalist could read Chapter 20 as a defence of royal "
                  "power and be unsettled to find that a king who could no longer "
                  "protect his subjects was owed nothing more; a supporter of "
                  "Parliament could find in it a reason to submit to the power that "
                  "had beaten the King. Hobbes returns to the "
                  "question in the Review and Conclusion, at the end of the book. "
                  "Critics from Locke on have argued that making obedience turn "
                  "on protection leaves a subject with too little against a "
                  "protector who protects and oppresses. Hobbes's own reply is at the "
                  "end of Chapter 20: whoever thinks sovereign power too great and "
                  "would make it less &ldquo;must subject himselfe, to the Power, that "
                  "can limit it; that is to say, to a greater&rdquo;."),
            ("p", "The next lesson turns from the whole commonwealth to its parts: "
                  "<em>Systems Subject and Public Ministers</em>."),
        ],
        "lab": ("levkit", {
            "mode": "law",
            "view": "silence",
            "preset": "four-commands",
            "presets": [
                {"id": "four-commands",
                 "label": "Four commands, two of them against the inalienable liberties",
                 "actions": "pay-tax serve-in-war kill-self confess-own-crime buy-and-sell",
                 "laws": "tax-law, pay-tax, -; muster-law, serve-in-war, -; execution-order, kill-self, -; inquiry-order, confess-own-crime, -",
                 "inalienable": "kill-self, no covenant can transfer defence of the body; confess-own-crime, no man can be obliged by covenant to accuse himself",
                 "expect": {
                    "llwCommanded": "4: pay-tax, serve-in-war, kill-self, confess-own-crime",
                    "llwRefusable": "2: kill-self (no covenant can transfer defence of the body), confess-own-crime (no man can be obliged by covenant to accuse himself)",
                    "llwShareFree": "1 of 5: 1/5 = 20%"}},
                {"id": "ordinary-laws",
                 "label": "A tax law and a muster law only",
                 "actions": "pay-tax serve-in-war kill-self confess-own-crime buy-and-sell",
                 "laws": "tax-law, pay-tax, -; muster-law, serve-in-war, -",
                 "inalienable": "kill-self, no covenant can transfer defence of the body; confess-own-crime, no man can be obliged by covenant to accuse himself",
                 "expect": {
                    "llwRefusable": "0: none",
                    "llwShareFree": "3 of 5: 3/5 = 60%"}},
            ],
            "panel_title": "Commands a subject may still refuse",
            "panel_intro": (
                "A figure computed from what the lesson states. The laws and actions go in as before, with the liberties a subject keeps whatever is commanded; the lab marks any command that falls on one. Whether the list of liberties is right is what the book argues."
            ),
        }),
        "steps_title": "Finding what a subject may refuse",
        "steps_intro": "Four steps, the same for any set of commands.",
        "steps": [
            ("List the commands",
             "Write down what each law commands, one action at a time."),
            ("List what no covenant could transfer",
             "Mark the actions that a covenant cannot oblige a man to do, with Hobbes's "
             "reason: defending his own body, and accusing himself."),
            ("Test each command against the list",
             "A command that falls on a marked action may be refused whatever the "
             "sovereign's right to punish. Any other command binds."),
            ("Check the end of the commonwealth",
             "A refusal that would defeat the end of the commonwealth, such as the "
             "enrolled soldier's, is not a liberty. This step is judgement, and the "
             "lab does not do it."),
        ],
        "worked": {
            "title": "Four commands and two liberties",
            "intro": [
                "Take the first preset. Four laws command paying tax, serving in the "
                "war, killing oneself and confessing one's own crime. Buying and "
                "selling is left alone. Two of the commanded actions are marked "
                "inalienable.",
            ],
            "lines": [
                "commanded:  4 of 5",
                "may still be refused:  kill-self, confess-own-crime = 2",
                "free by silence:  buy-and-sell = 1 of 5 = 20%",
            ],
            "after": [
                "In the second preset the same two actions are marked inalienable but "
                "no law commands them, so no command can be refused on those grounds. "
                "The lab does not mark the muster law, because on Hobbes's account a man "
                "commanded to fight may sometimes refuse, with a sufficient substitute, and "
                "one who has enrolled may not, and which case holds is a judgement the "
                "lab does not make.",
            ],
        },
        "quiz_title": "What a subject keeps",
        "quiz": [
            {"q": "Why, on Hobbes's account, may a man condemned to death refuse an order "
                  "to kill himself?",
             "a": ["Because the sovereign has no power of life and death",
                   "Because the sentence was unjust",
                   "Because the command is contrary to the law of the land",
                   "Because a covenant not to defend one's own body is void, so he "
                   "never gave up the liberty"],
             "c": 3,
             "why": "Chapter 14 shows such covenants void, and &ldquo;No man is bound by "
                    "the words themselves, either to kill himselfe, or any other "
                    "man&rdquo;. Hobbes keeps the sovereign's power of life and death and "
                    "says the man is &ldquo;justly condemned&rdquo;."},
            {"q": "In the lab's first preset, how many actions are commanded and how "
                  "many of those commands may a subject still refuse?",
             "a": ["Four commanded, none refusable", "Four commanded, two refusable",
                   "Five commanded, two refusable", "Two commanded, four refusable"],
             "c": 1,
             "why": "Four laws command four of the five actions, and two of those, "
                    "kill-self and confess-own-crime, are marked inalienable. Only "
                    "buying and selling is left free."},
            {"q": "A man has enrolled as a soldier and taken the King's pay. May he run from "
                  "the battle?",
             "a": ["Yes, for naturall timorousnesse is always an excuse",
                   "Yes, because no covenant can oblige a man to risk his life",
                   "No: he has taken away the excuse of a timorous nature and may "
                   "not run without his captain's leave",
                   "Only if the army is losing"],
             "c": 2,
             "why": "Hobbes says that &ldquo;he that inrowleth himselfe a Souldier, or taketh imprest "
                    "mony, taketh away the excuse of a timorous nature&rdquo;. The "
                    "excuse is for the man who did not enrol. Hobbes does not make "
                    "the soldier's duty depend on whether the army is winning."},
            {"q": "How long does a subject's obligation to the sovereign last?",
             "a": ["For as long as the sovereign lives",
                   "For ever, since the covenant was made for ever",
                   "For as long as the sovereign's right is acknowledged by the Church",
                   "As long as, and no longer than, the power by which he can protect them"],
             "c": 3,
             "why": "&ldquo;The Obligation of Subjects to the Soveraign, is understood "
                    "to last as long, and no longer, than the power lasteth, by which "
                    "he is able to protect them.&rdquo; Hobbes does call sovereignty "
                    "immortal in the intention of the makers, but not in its nature."},
        ],
        "mistakes": [
            ("Thinking a subject must obey every command",
             "The sovereign's power over his subjects is not limited by their rights, "
             "but a subject's obligation has edges. Because no one can covenant away the "
             "defence of his own body, the sovereign cannot oblige a man to kill himself, "
             "accuse himself, or go without food, and the man &ldquo;hath the Liberty to "
             "disobey&rdquo; even when justly condemned."),
            ("Thinking a subject's liberties are limits on the sovereign's right",
             "Hobbes says that nothing the sovereign does to a subject can be an "
             "injury to him, and the refusals are not a right to resist the sovereign's "
             "sword in defence of another. They are the places where the covenant never "
             "reached, and the sovereign may still punish the refusal."),
            ("Thinking the soldier's case is a liberty to refuse war",
             "He may refuse in many cases, but not when he has enrolled, or when "
             "the defence of the commonwealth needs every man able to bear arms, since "
             "&ldquo;otherwise the Institution of the Common-wealth, which they have "
             "not the purpose, or courage to preserve, was in vain&rdquo;."),
        ],
        "standard": (
            "Finish when you can say which commands a subject may refuse.",
            "Given a set of commands and the liberties no covenant can transfer, "
            "state which commands may be refused, which may not, and what Hobbes "
            "says ends a subject's obligation."
        ),
        "note": (
            "The lab marks which commands fall on a liberty you tell it is "
            "inalienable. It cannot say whether the list is right, whether the soldier's "
            "case is on the right side of the line, or whether obedience should "
            "turn on protection, which is what Hobbes's critics from Locke onward "
            "contest. The actions and laws are invented for the lesson."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Leviathan chs. 22-23, 1651 p. 117; PDF p. 253 of the operator's copy.
    {
        "slug": "systems-and-public-ministers",
        "title": "Systems Subject and Public Ministers",
        "module": "Chapters 22 and 23 · Of Systemes Subject, and of Publique Ministers",
        "one_line": "A body politic is limited by its letters, and when its assembly decrees what the letters do not warrant, only those who voted for it are answerable.",
        "summary": (
            "Chapter 22 sorts the parts of a commonwealth that are groups of men: regular "
            "and irregular, political and private, lawful and unlawful. A body politic "
            "is limited by its letters, and an unwarranted decree binds only those who "
            "voted for it. Chapter 23 turns to the public ministers. Count an assembly's "
            "voices on a motion to borrow, and see who is answerable for the debt."
        ),
        "key": [
            "a body politic is limited by its letters",
            "unwarranted: the act of those who voted",
            "the absent and the dissenters are excused",
            "private leagues of subjects are factions",
            "a public minister serves the public person",
        ],
        "key_label": "Systems and ministers in five lines",
        "concepts_intro": (
            "The two chapters take the commonwealth apart as one takes a body apart: "
            "first the similar parts, the systems, then the organs, the ministers."
        ),
        "concepts": [
            ("Systems, regular and irregular",
             "A system is any number of men joined in one interest or business. It is "
             "regular when one man or assembly represents it, irregular otherwise. A "
             "regular system under the sovereign is political if made by his authority, "
             "private if made by subjects or a stranger."),
            ("Letters and liability",
             "The power of a body politic's representative is always limited, by its "
             "letters from the sovereign and by the law. What an assembly decrees "
             "beyond them is the act of those who voted for it, not of dissenters or "
             "absentees. A debt to a stranger is owed only by those who voted for the "
             "borrowing, whatever the letters say, since no letters could make the "
             "members pay without making the representative sovereign."),
            ("Public ministers",
             "A public minister is employed by the sovereign in affairs with authority "
             "to represent the person of the commonwealth. A counsellor who only "
             "advises, and a steward of the monarch's household, are not public "
             "ministers."),
        ],
        "read_title": "The passage first, then the two chapters in order",
        "read_intro": (
            "The passage comes from the middle of Chapter 22, where Hobbes asks who "
            "pays when a body politic runs into debt. The chapters run from classifying "
            "groups to naming the organs that serve the sovereign."
        ),
        "body": [
            ("p", "<strong>Chapter 22.</strong> &ldquo;But when the Representative is an "
                  "Assembly, and the debt to a stranger; all they, and onely they are "
                  "responsible for the debt, that gave their votes to the borrowing of it, "
                  "or to the Contract that made it due, or to the fact for which the Mulct "
                  "was imposed; because every one of those in voting did engage himselfe "
                  "for the payment:&rdquo;"),
            ("p", "Imagine a town council that votes to borrow money for a new market. "
                  "Two members spoke and voted against it, one was away, and the lender "
                  "now wants repayment. Who owes? Hobbes's answer is a rule about "
                  "authorship, which you met in Chapter 16: you are bound by what "
                  "you have authorised. He gets there through a classification that "
                  "takes some patience, and it is worth setting out."),
            ("p", "The two chapters follow a comparison the book has been using since "
                  "its Introduction: the commonwealth is an artificial man. Chapter 22 "
                  "is about the &ldquo;Systemes&rdquo;, which &ldquo;resemble the similar "
                  "parts, or Muscles of a Body naturall&rdquo;, and defines them as "
                  "&ldquo;any numbers of men joyned in one Interest, or one Businesse&rdquo;. "
                  "They are Regular where one man or assembly represents the whole "
                  "number and Irregular otherwise. The only absolute regular system is "
                  "a commonwealth. The rest are subordinate, and either Political, made "
                  "by authority of the sovereign, or Private, made by subjects among "
                  "themselves or by a stranger's authority; the private ones are "
                  "lawful if the commonwealth allows them and unlawful otherwise."),
            ("p", "Then the principle that makes the rest work. In a body politic, "
                  "&ldquo;the power of the Representative is alwaies Limited&rdquo;, and "
                  "the limits are set by the sovereign, because &ldquo;Power Unlimited, is "
                  "absolute Soveraignty&rdquo;. To give a subordinate body an absolute "
                  "representative would divide the dominion, which is contrary to peace. "
                  "The bounds are found in two things, the body's writ or letters patent "
                  "from the sovereign and the law of the commonwealth. Where one man "
                  "represents the body and acts beyond both, the act is his own: beyond "
                  "his letters &ldquo;he representeth no mans person, but his own&rdquo;. "
                  "If he borrows from a stranger, he alone owes the debt, since no letters "
                  "need limit borrowing and letters that let him make the members pay "
                  "would make him their sovereign; he pays out of the common stock if "
                  "there is one and otherwise out of his own estate."),
            ("p", "Where the representative is an assembly, the same rule runs by "
                  "votes. A decree not warranted by the letters or the laws is the act "
                  "of the assembly and &ldquo;the act of every one by whose Vote the Decree "
                  "was made; but not the act of any man that being present Voted to the "
                  "contrary; nor of any man absent, unlesse he Voted it by procuration&rdquo;. "
                  "The assembly itself may be punished, by dissolution, or by fine out of "
                  "a common stock; those who did not vote are innocent, since the assembly "
                  "cannot represent any man in things beyond its letters. And each "
                  "voter for the borrowing is answerable for the whole debt, though "
                  "when any one pays it he is discharged. That last part is the "
                  "answer to the council: the two dissenters and the absentee owe "
                  "nothing, and each of the others is liable for all of it."),
            ("p", "The lab counts this. It takes an assembly's voices on a motion, "
                  "decides whether it passes, and with <em>liable</em> set, names "
                  "who is answerable and who is excused. Take six members, four yes and "
                  "two no. In <em>borrow</em> the motion passes four to two, the four "
                  "yes voters are answerable and the two others excused. If the debt is "
                  "120, each of the four is liable to the lender for the whole 120; "
                  "if they settle it between themselves equally, 30 each, which is "
                  "the lesson's example and not Hobbes's. In <em>even-split</em> three "
                  "members vote yes and three no: the assembly is mute, as Chapter 16 says an "
                  "even assembly oftentimes is, "
                  "nothing is decreed, and nobody is liable. In <em>seven-members</em> "
                  "three say yes, two no and two abstain, and with the greater number "
                  "of voices given the motion passes three to two and three are "
                  "answerable. The lab reads an abstention as not voting for the motion, "
                  "and Hobbes says that those who gave not their vote are innocent; "
                  "only the counting of a pass among abstentions is the lab's own. The <em>absolute</em> preset keeps "
                  "the same votes but needs more than half of all seven, and "
                  "three of seven is not that, so the motion fails."),
            ("p", "Hobbes draws the working conclusion himself. In a subordinate body "
                  "it is sometimes &ldquo;not onely lawfull, but expedient, for a "
                  "particular man to make open protestation against the decrees of the "
                  "Representative Assembly, and cause their dissent to be Registred&rdquo;, "
                  "because otherwise he may be obliged to pay for what others did. In "
                  "a sovereign assembly that liberty is taken away, since he who "
                  "protests there denies their sovereignty. The distinction is the "
                  "one between a subject of the sovereign and a member of a body that is "
                  "subject to him."),
            ("p", "The chapter then runs through the variety of bodies. A province "
                  "governed by an assembly, which the Romans never did and the English "
                  "did not do with Virginia or the Somers Isles, where each plantation "
                  "had one governor, is treated as Hobbes treats every assembly of "
                  "this kind. Merchants' corporations come next, and he is "
                  "sharp about them: to grant a company of merchants a corporation "
                  "is &ldquo;to grant them a double Monopoly&rdquo;, sole buyers and sole "
                  "sellers, ill for the people at home and the foreigner abroad, though "
                  "he allows it would profit the commonwealth if the merchants "
                  "were bound together abroad and free at home. Since their end is "
                  "each adventurer's own gain, every member should sit in the assembly; "
                  "and here Hobbes departs from the general rule: a debt to a stranger "
                  "falls on every member for the whole, because a stranger takes no "
                  "notice of their private laws."),
            ("p", "Then the private systems. Families are lawful regular bodies, in "
                  "which the father or master orders the whole and the Law limits "
                  "his power. Corporations of beggars and thieves, and of men who "
                  "by authority from a foreign person unite in another's dominion to "
                  "spread doctrines, are unlawful. Irregular systems, mere leagues or "
                  "crowds, are lawful or not by each man's design. A league between "
                  "commonwealths is lawful and profitable, since there is no common power "
                  "above them; but leagues of subjects of one commonwealth are "
                  "unnecessary, since each can get his right from the sovereign, and "
                  "&ldquo;go commonly by the name of Factions, or Conspiracies&rdquo;. "
                  "Writing in 1651, with the memory of the Parliamentary and "
                  "royalist parties, the Presbyterians and Independents, behind "
                  "him, Hobbes lists factions for religion and for the state alike as "
                  "&ldquo;a taking of the Sword out of the hand of the Soveraign&rdquo;. "
                  "He closes with the crowd: a thousand men may petition, but if a "
                  "thousand come to present it, it is a tumultuous assembly, because "
                  "one or two would do, as the town clerk of Ephesus said of Demetrius "
                  "and the silversmiths."),
            ("p", "Chapter 23 passes from the muscles to the organs. A public minister "
                  "is he who, employed by the sovereign in any affairs, has authority "
                  "&ldquo;to represent in that employment, the Person of the "
                  "Common-wealth&rdquo;. Every sovereign has two capacities, natural "
                  "and political, and those who serve him in the first, such as ushers "
                  "and chamberlains, are not public ministers. There are ministers of "
                  "general administration, like a regent or a viceroy, and of special "
                  "administration: of the treasure, of the militia, of teaching the "
                  "people their duty, of judging, and of executing the judgements, "
                  "most of them compared to a part of the body, nerves, hands, the organs of "
                  "voice. Abroad, ambassadors and heralds are public ministers."),
            ("p", "Two features of that chapter bear on the argument. A judge, being "
                  "the sovereign's minister, gives the sovereign's sentence, and no "
                  "man can be judge in his own cause, so Hobbes holds the defendant "
                  "agrees to his judges when he may except against them and then "
                  "does not; he praises the English practice of the twelve men for "
                  "this reason. And a counsellor, who gives advice to the sovereign "
                  "and no more, is not a public person, because the advice is addressed "
                  "to the sovereign only, &ldquo;whose person cannot in his own "
                  "presence, be represented to him, by another&rdquo;. Counsel, and "
                  "what it requires of the counsellor, is the subject of Chapter 25 "
                  "in the next course. That course, <em>Wealth, Counsel, Law and the "
                  "Office of the Sovereign</em>, begins with the commonwealth's nourishment."),
        ],
        "lab": ("levkit", {
            "mode": "assembly",
            "view": "voices",
            "rule": "greater",
            "liable": "yes",
            "preset": "borrow",
            "presets": [
                {"id": "borrow",
                 "label": "Six members vote on a loan: four yes, two no",
                 "members": "Ashe, yes; Bell, yes; Cole, yes; Dunn, yes; Eyre, no; Ford, no",
                 "expect": {
                    "lasDecision": "passes: 4 to 2 by the greater number of voices given",
                    "lasLiable": "4: Ashe, Bell, Cole, Dunn",
                    "lasExcused": "2: Eyre, Ford"}},
                {"id": "even-split",
                 "label": "The same six, three against three",
                 "members": "Ashe, yes; Bell, yes; Cole, yes; Dunn, no; Eyre, no; Ford, no",
                 "expect": {
                    "lasDecision": "mute: 3 to 3, an even split of the voices",
                    "lasLiable": "none: no decree was made"}},
                {"id": "seven-members",
                 "label": "Seven members: three yes, two no, two abstaining",
                 "members": "Ashe, yes; Bell, yes; Cole, yes; Dunn, no; Eyre, no; Ford, abstain; Gray, abstain",
                 "expect": {
                    "lasDecision": "passes: 3 to 2 by the greater number of voices given",
                    "lasLiable": "3: Ashe, Bell, Cole",
                    "lasExcused": "4: Dunn, Eyre, Ford, Gray"}},
                {"id": "absolute",
                 "label": "The same seven where a majority of all members is needed",
                 "rule": "absolute",
                 "members": "Ashe, yes; Bell, yes; Cole, yes; Dunn, no; Eyre, no; Ford, abstain; Gray, abstain",
                 "expect": {
                    "lasDecision": "fails: 3 of 7 members say yes, not more than half",
                    "lasLiable": "none: no decree was made"}},
            ],
            "panel_title": "Who answers for what the assembly decreed",
            "panel_intro": (
                "A figure computed from what the lesson states. An assembly’s voices on a motion go in; the lab says whether it passes, fails or is mute, and which members are answerable for it. Whether they should be is what the book argues."
            ),
        }),
        "steps_title": "Finding who is answerable for a decree",
        "steps_intro": "Four steps, the same for any assembly and any motion.",
        "steps": [
            ("Count the voices",
             "Count yes, no and abstentions, and note who is absent."),
            ("Apply the rule",
             "On the greater number of voices given, the motion passes if yes "
             "exceeds no, fails if no exceeds yes, and is mute if they are equal. On "
             "the absolute rule it passes only with more than half of all members."),
            ("Name those who voted for it",
             "If the motion passes, those who voted for it are answerable: for a debt to "
             "a stranger always, and for any other decree when it is beyond the "
             "letters. Dissenters and the absent are excused."),
            ("Fix what each owes",
             "To a stranger each yes-voter is liable for the whole debt, and one "
             "payment discharges all. To a member, the body alone owes, from its "
             "common stock."),
        ],
        "worked": {
            "title": "A loan voted four to two",
            "intro": [
                "Take the first preset. Six members vote on a loan of 120 from a "
                "stranger. Ashe, Bell, Cole and Dunn vote yes; Eyre and Ford vote no. "
                "The lender is a stranger to the body.",
            ],
            "lines": [
                "yes 4, no 2, abstain 0",
                "greater number of voices: 4 > 2, so it passes by 2",
                "answerable:  Ashe, Bell, Cole, Dunn = 4",
                "excused:  Eyre, Ford = 2",
                "each of the four owes the lender 120; equal sharing: 120/4 = 30",
            ],
            "after": [
                "Make it three to three and the assembly is mute: nothing is decreed, so "
                "no one is liable. The sharing of 30 each is the lesson's assumption; "
                "Hobbes says only that each is liable for the whole until one pays.",
            ],
        },
        "quiz_title": "Who owes what an assembly decreed",
        "quiz": [
            {"q": "A town's governing assembly votes four to two, with none absent, to borrow "
                  "from a stranger. Who is answerable for the debt?",
             "a": ["All six members, since the assembly decreed it",
                   "Only the two who voted against it",
                   "Only the four who voted for it",
                   "Only the assembly's chairman"],
             "c": 2,
             "why": "Hobbes says that &ldquo;all they, and onely they are responsible for the debt, that "
                    "gave their votes to the borrowing of it&rdquo;. Those who voted "
                    "contrary are innocent. The chairman is not singled out: a debt "
                    "falls on one man alone only where the representative is one man."},
            {"q": "In the lab's even-split preset, three yes and three no on the "
                  "greater-number rule, what is the decision?",
             "a": ["Passes, because the chairman breaks a tie",
                   "Passes, by the three yes voters' number",
                   "Fails, because the three no voters outnumber the yes voters",
                   "Mute: an even split decides nothing, and no one is liable"],
             "c": 3,
             "why": "Neither side has the greater number, and the lab calls such an assembly "
                    "mute, as Chapter 16 does; Hobbes adds that in some questions an even "
                    "vote still decides (&ldquo;not to condemne, is to absolve&rdquo;). "
                    "Either way nothing is decreed and no one is liable."},
            {"q": "One man represents a body politic, and borrows from a stranger. Who owes "
                  "the debt?",
             "a": ["The representative himself, out of the common stock or his own estate",
                   "Every member, since he acted in the name of the body",
                   "The sovereign, who gave him the letters",
                   "No one, because the loan is void"],
             "c": 0,
             "why": "&ldquo;No member therefore is obliged to pay the debt so borrowed, "
                    "but the Representative himselfe&rdquo;. The lender, "
                    "&ldquo;being a stranger to the Letters&rdquo;, takes for his debtor "
                    "only the man who engaged himself."},
            {"q": "Which of these is a public minister, by Chapter 23?",
             "a": ["A steward of the monarch's household",
                   "An usher who waits on a sovereign assembly",
                   "A counsellor who only gives advice when asked",
                   "A governor of a province for the sovereign"],
             "c": 3,
             "why": "He has charge of a general administration and represents the person "
                    "of the commonwealth. Stewards and ushers serve in the natural "
                    "capacity and are not public ministers, and a counsellor with no "
                    "authority of judicature or command is not a public person."},
        ],
        "mistakes": [
            ("Thinking an assembly's decree binds every member",
             "An unwarranted decree is the act of the assembly and of &ldquo;every one by "
             "whose Vote the Decree was made&rdquo;, and not of &ldquo;any man that being "
             "present Voted to the contrary&rdquo; or absent. In the first preset "
             "the two who voted no owe nothing, and each of the four who voted yes "
             "owes the stranger the whole 120."),
            ("Thinking a body politic's power is as wide as the sovereign's",
             "The representative's power is always limited by its letters and the law. "
             "To grant it absolute power would divide the sovereignty, which Hobbes "
             "says the sovereign cannot be understood to have done unless he "
             "plainly discharges them of their subjection."),
            ("Counting every servant of the sovereign as a public minister",
             "Only those who serve him in the administration of public business, and "
             "so represent the commonwealth, are public ministers. Stewards, ushers "
             "and a counsellor with no authority of judicature or command serve the "
             "man or give advice and do not."),
        ],
        "standard": (
            "Finish when you can say who answers for an assembly's decree.",
            "Given an assembly's voices on a motion and the rule, state whether it "
            "passes, fails or is mute, name who is answerable for it and who is "
            "excused, and say who owes a debt to a stranger and to a member."
        ),
        "note": (
            "The lab counts voices and names those who voted yes. It cannot tell you "
            "whether a decree other than a debt is beyond the body's letters, which is a question of "
            "the letters and the law, or whether holding the yes-voters liable is "
            "just, which is what Hobbes argues from the notion of authorship. The "
            "counting of a pass among abstentions is the lab's own, and the assembly and the "
            "amounts are invented for the lesson."
        ),
    },
]
