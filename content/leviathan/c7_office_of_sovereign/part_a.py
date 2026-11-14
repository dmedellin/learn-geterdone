"""Wealth, Counsel, Law and the Office of the Sovereign, lessons 1-4: Chapters 24-27.

Every quotation is copied from the operator's copy of the 1651 text of Leviathan
(Tuck's edition, which keeps Hobbes's spelling); the comment beside each lesson
gives the chapter, the 1651 page and the PDF page. Italics are dropped, and a
quotation that starts or ends inside a sentence is not capitalised or punctuated
to look like a whole one.

Lessons 1 and 4 use levkit, which may not be registered while this is drafted;
their cfg follows docs/leviathan/PLAN.md section D.1 and is corrected against
docs/leviathan/kit-report.md.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Leviathan ch. 24, 1651 p. 127; PDF p. 267 of the operator's copy
    {
        "slug": "nutrition-and-procreation",
        "title": "The Nutrition and Procreation of a Commonwealth",
        "module": "Chapter 24 · Of the Nutrition, and Procreation of a Common-wealth",
        "one_line": "Hobbes feeds his artificial man: plenty comes from labour, property comes from the sovereign, and a tenth set apart is still a share.",
        "summary": (
            "Chapter 24 follows the body of the artificial man into its digestion. Hobbes "
            "says plenty depends on labour and industry, that the division of land and goods "
            "is the sovereign's act, that money is the blood of the commonwealth, and that "
            "colonies are its children. Divide a harvest by the shares Hobbes gives the "
            "twelve portions of Canaan and the tenth set apart for the Levites, and see "
            "every share come out exact."
        ),
        "key": [
            "plenty: nature gives, labour receives",
            "distribution is propriety, and the sovereign's",
            "set apart first, then divide the rest",
            "share = (total - set apart) · weight / weights",
            "money is the blood of a commonwealth",
        ],
        "key_label": "Chapter 24 in five lines",
        "concepts_intro": (
            "Chapter 24 is the first of the chapters on what a commonwealth does. It keeps "
            "the picture of the commonwealth as a body, and takes it through eating, "
            "digesting and having children."
        ),
        "concepts": [
            ("Nutrition: plenty and distribution",
             "The nutrition of a commonwealth is the plenty of what supports life and its "
             "distribution. Nature limits plenty to what land and sea give, and Hobbes "
             "says it depends, next to God's favour, on the labour and industry of men. "
             "A territory that lacks something can import it, and a man's labour is itself "
             "a commodity that can be exchanged."),
            ("Propriety belongs to the sovereign",
             "Hobbes calls the distribution of the materials of nourishment the "
             "constitution of mine, thine and his, in one word propriety. Where there is "
             "no commonwealth, whatever a man can get and keep by force is his, which is "
             "neither property nor common ownership but uncertainty. So the division of "
             "land, the rules of foreign trade and the forms of contract are all the "
             "sovereign's to appoint."),
            ("Money, and the children of a commonwealth",
             "Gold, silver and coined money turn what is not consumed now into something "
             "of equal value that can be carried anywhere, and Hobbes calls this the "
             "sanguification of the commonwealth: blood made of the fruits of the earth, "
             "circulating to nourish every member. Its procreation is the colonies, "
             "numbers of men sent out under a governor to inhabit a foreign country."),
        ],
        "read_title": "The passage first, then the chapter in order",
        "read_intro": (
            "The sentence that carries the chapter's central claim comes first. The "
            "chapter then goes through the body's functions one at a time, as Hobbes "
            "promised in his Introduction."
        ),
        "body": [
            ("p", "<strong>Chapter 24.</strong> &ldquo;The Distribution of the Materials of "
                  "this Nourishment, is the constitution of Mine, and Thine, and His; that "
                  "is to say, in one word Propriety, and belongeth in all kinds of "
                  "Common-wealth to the Soveraign Power.&rdquo;"),
            ("p", "Hobbes has spent the previous chapters on how a commonwealth is made, "
                  "who may represent it and what its parts are. Chapter 24 asks how it "
                  "lives, and he answers with the body he began with in the Introduction. "
                  "A body eats. The artificial man's food is &ldquo;Animals, Vegetals, and "
                  "Minerals&rdquo;, which God &ldquo;hath freely layd&rdquo; before us near "
                  "the surface of the earth, so that there &ldquo;needeth no more but the "
                  "labour, and industry of receiving them&rdquo;. Plenty, he concludes, "
                  "depends &ldquo;next to Gods favour&rdquo; on that labour and industry "
                  "alone. It sets up "
                  " the argument to come: if wealth comes from labour, what the "
                  "sovereign owns is not the food but the rules about who may have which "
                  "portion."),
            ("p", "Now go through the sentence you have just read. &ldquo;Mine, and Thine, "
                  "and His&rdquo; is the whole of property, and Hobbes says it is "
                  "constituted, made by an act, not found in nature. His reason comes from "
                  "Chapter 13: where there is no commonwealth, &ldquo;every thing is his "
                  "that getteth it, and keepeth it by force; which is neither Propriety, "
                  "nor Community, but Uncertainty&rdquo;. He then calls Cicero as a witness, "
                  "a man he describes as a passionate defender of liberty, who said that if "
                  "the civil law were abandoned no man could be sure of what he would "
                  "receive from his ancestor or leave to his children. And since only the "
                  "person who represents the commonwealth can act for it, the introduction "
                  "of property is &ldquo;the act onely of the Soveraign&rdquo;, made in the "
                  "laws. The Greeks, Hobbes adds, called law <em>nomos</em>, distribution."),
            ("p", "His example is the land of Canaan. The children of Israel were a "
                  "commonwealth in the wilderness, but they &ldquo;wanted the commodities "
                  "of the Earth&rdquo; until they were masters of the Promised Land, and "
                  "then it was divided &ldquo;not by their own discretion, but by the "
                  "discretion of Eleazar the Priest, and Joshua their Generall&rdquo;. "
                  "There were thirteen tribes once Joseph's was subdivided, yet Joshua made "
                  "&ldquo;but twelve portions of the Land&rdquo;, and gave the tribe of Levi "
                  "no land but &ldquo;the Tenth part of the whole fruits&rdquo;. Hobbes's "
                  "verdict is that this division &ldquo;was therefore Arbitrary&rdquo;, "
                  "meaning that it followed the discretion of those who held the "
                  "sovereignty, and that is how he reads William the Conqueror's "
                  "distribution of England too."),
            ("p", "The lab does the sum on this example. Take a harvest of twelve hundred "
                  "measures, a sample figure, since Hobbes gives no quantities. The tenth "
                  "goes to Levi first, 120 measures, and the remaining 1,080 are divided "
                  "among the twelve portions. In the canaan preset every portion has the "
                  "same weight and gets 90. In the no-tenth preset nothing is set apart and "
                  "each portion gets 100. In the unequal preset Judah's portion carries "
                  "weight 2 and the others weight 1, so the weights total 13 and a share is "
                  "no longer a whole number: each ordinary portion gets `1080/13` and "
                  "Judah's gets `2160/13`, printed as fractions because the lab never "
                  "rounds. Hobbes does not say the portions were equal, and neither is the "
                  "model his: it only shows what an arbitrary distribution looks like once "
                  "somebody has written the shares down."),
            ("p", "Hobbes draws a hard consequence. A subject's property is &ldquo;a right "
                  "to exclude all other subjects from the use of them; and not to exclude "
                  "their Soveraign&rdquo;. He is also firm that the commonwealth should not "
                  "be given public land to live on, because &ldquo;Common-wealths can "
                  "endure no Diet&rdquo;: their expense is set by the appetites of their "
                  "neighbours and by accidents, so no fixed revenue can be enough, and a "
                  "sovereign who can sell or give it away will. Weigh this against its "
                  "critics. John Locke, writing a generation later, held that property is "
                  "made by labour before any government exists, and that a government "
                  "which takes it without consent breaks its trust. Hobbes's reply, in his "
                  "own terms, is the Uncertainty sentence above: the labour is "
                  "unprotected until someone has the power to say whose it is."),
            ("p", "Then the rest of the body. Foreign trade, and the places and "
                  "commodities of it, belong to the sovereign too, because private men "
                  "would be drawn by gain to arm the enemy or to import things that "
                  "please appetite and do them harm. So do the laws of transferring "
                  "propriety: how buying, selling, lending and hiring are made valid. "
                  "Money does the work that digestion does. It reduces what is not "
                  "consumed to something of equal value and portable, so that a man may "
                  "have &ldquo;such Nourishment as the place affordeth&rdquo; wherever he "
                  "goes, and Hobbes says this &ldquo;Concoction, is as it were the "
                  "Sanguification of the Common-wealth&rdquo;. The collectors and "
                  "treasurers are the veins and arteries."),
            ("p", "The last function is procreation. Colonies are children, and Hobbes's "
                  "account of what they owe is as brisk as the rest. A colony that is "
                  "settled either becomes a commonwealth of itself, and then the mother "
                  "city asks of it no more than a father asks of an emancipated child, "
                  "honour and friendship, or it stays united to its metropolis as the "
                  "Roman colonies did and is then a province, a part of the commonwealth "
                  "that sent it. Which of the two it is depends, he says, wholly on the "
                  "licence or letters by which the sovereign authorised it to plant. The "
                  "next lesson, <em>Of Counsel</em>, turns from the body to the mind "
                  "of the artificial man and asks who should be listened to."),
        ],
        "lab": ("levkit", {
            "mode": "tax",
            "view": "shares",
            "preset": "canaan",
            "presets": [
                {"id": "canaan", "label": "Twelve equal portions, a tenth set apart for Levi",
                 "total": 1200,
                 "parties": [["Reuben", 1], ["Simeon", 1], ["Judah", 1], ["Issachar", 1],
                             ["Zebulun", 1], ["Dan", 1], ["Gad", 1], ["Asher", 1],
                             ["Naphtali", 1], ["Benjamin", 1], ["Ephraim", 1], ["Manasseh", 1]],
                 "setaside": [["Levi", "1/10"]], "expect": {"ltxSetAside": "Levi 1/10 = 0.1 of the total: 120", "ltxRemainder": "1,080", "ltxShares": "Reuben 90; Simeon 90; Judah 90; Issachar 90; Zebulun 90; Dan 90; Gad 90; Asher 90; Naphtali 90; Benjamin 90; Ephraim 90; Manasseh 90", "ltxSum": "1,200, the whole total"}},
                {"id": "no-tenth", "label": "The same twelve portions, nothing set apart",
                 "total": 1200,
                 "parties": [["Reuben", 1], ["Simeon", 1], ["Judah", 1], ["Issachar", 1],
                             ["Zebulun", 1], ["Dan", 1], ["Gad", 1], ["Asher", 1],
                             ["Naphtali", 1], ["Benjamin", 1], ["Ephraim", 1], ["Manasseh", 1]],
                 "setaside": [], "expect": {"ltxSetAside": "none set apart", "ltxShares": "Reuben 100; Simeon 100; Judah 100; Issachar 100; Zebulun 100; Dan 100; Gad 100; Asher 100; Naphtali 100; Benjamin 100; Ephraim 100; Manasseh 100"}},
                {"id": "unequal", "label": "Judah's portion twice the weight of each other",
                 "total": 1200,
                 "parties": [["Reuben", 1], ["Simeon", 1], ["Judah", 2], ["Issachar", 1],
                             ["Zebulun", 1], ["Dan", 1], ["Gad", 1], ["Asher", 1],
                             ["Naphtali", 1], ["Benjamin", 1], ["Ephraim", 1], ["Manasseh", 1]],
                 "setaside": [["Levi", "1/10"]], "expect": {"ltxWeight": "13", "ltxShares": "Reuben 1,080/13; Simeon 1,080/13; Judah 2,160/13; Issachar 1,080/13; Zebulun 1,080/13; Dan 1,080/13; Gad 1,080/13; Asher 1,080/13; Naphtali 1,080/13; Benjamin 1,080/13; Ephraim 1,080/13; Manasseh 1,080/13", "ltxNotWhole": "12: Reuben, Simeon, Judah, Issachar, Zebulun, Dan, Gad, Asher, Naphtali, Benjamin, Ephraim, Manasseh"}},
            ],
            "panel_title": "Divide a harvest by stated shares",
            "panel_intro": (
                "The total, the portions with their weights and any part set apart first go "
                "in. The lab takes the set-aside part off the total, then divides the "
                "remainder by weight, exactly."
            ),
        }),
        "steps_title": "Dividing a total by stated shares",
        "steps_intro": "Four steps, the same for any division in which something is set apart first.",
        "steps": [
            ("Take what is set apart off the top",
             "Multiply the total by each set-aside fraction. These portions are fixed "
             "before anyone else's share is worked out, as the Levites' tenth was."),
            ("Find the remainder",
             "Subtract the set-aside portions from the total. Only the remainder is "
             "divided."),
            ("Add the weights",
             "Add the weights of the parties that share the remainder. Equal portions "
             "have equal weights; a larger portion has a larger one."),
            ("Divide by weight and keep it exact",
             "A party's share is the remainder times its weight, over the sum of weights. "
             "If that is not a whole number, write it as a fraction. Rounding would make "
             "the shares add up to something other than the total."),
        ],
        "worked": {
            "title": "A harvest of 1,200 among twelve portions",
            "intro": [
                "Take the unequal preset: a tenth to Levi, then twelve portions of which "
                "Judah's weighs twice the others.",
            ],
            "lines": [
                "set apart:  1200 · 1/10 = 120",
                "remainder:  1200 - 120 = 1080",
                "weights:  11 · 1 + 1 · 2 = 13",
                "an ordinary portion:  1080 · 1/13 = 1080/13",
                "Judah:  1080 · 2/13 = 2160/13",
                "check:  120 + 11 · 1080/13 + 2160/13 = 1200",
            ],
            "after": [
                "The shares add back to the total because none was rounded. That is the "
                "only thing this arithmetic proves. That the sovereign may divide as he "
                "judges equitable is Hobbes's claim, and no sum can test it.",
            ],
        },
        "quiz_title": "Shares and the sovereign's part",
        "quiz": [
            {"q": "On Hobbes's account, from whom does a subject's property in his land "
                  "originally proceed?",
             "a": ["From the arbitrary distribution of the sovereign",
                   "From the labour he put into it, before any commonwealth",
                   "From the first man to occupy it",
                   "From an agreement among the subjects themselves"],
             "c": 0,
             "why": "Hobbes says the distribution of land is the sovereign's act, and the "
                    "division of Canaan, made by Eleazar and Joshua, is his proof. Where "
                    "there is no commonwealth, whoever gets and keeps a thing by force "
                    "has it, which is uncertainty and not property. The other three are "
                    "the views he is arguing against or says nothing for."},
            {"q": "Chapter 24 says Joshua made twelve portions of the land and gave Levi "
                  "no land. What did Levi receive?",
             "a": ["Half a portion",
                   "A portion by lot, like the others",
                   "The tenth part of the whole fruits",
                   "A city in each of the twelve portions"],
             "c": 2,
             "why": "Hobbes's words are that Levi was assigned &ldquo;the Tenth part of "
                    "the whole fruits&rdquo;. He does not say the portions were drawn by "
                    "lot; he says they were divided by the discretion of Eleazar and "
                    "Joshua."},
            {"q": "In the lab, a harvest of 1,200 has a tenth set apart and the rest is "
                  "shared among twelve portions of equal weight. What does each portion get?",
             "a": ["100", "120", "90", "1080/13"],
             "c": 2,
             "why": "The tenth is 120, which leaves 1,080, and 1,080 over twelve equal "
                    "portions is 90. A hundred is the share if nothing is set apart. 120 "
                    "is the set-aside part itself. `1080/13` is the share when one "
                    "portion has weight 2."},
            {"q": "Why does Hobbes say it is in vain to give the commonwealth public lands "
                  "for its support?",
             "a": ["Because lands cannot be taxed",
                   "Because a commonwealth's expense is set by outside accidents and "
                   "neighbours' appetites, not by its own, so no fixed revenue is enough",
                   "Because the sovereign has no right to own anything",
                   "Because subjects would refuse to work on public land"],
             "c": 1,
             "why": "His words are that commonwealths &ldquo;can endure no Diet&rdquo;: "
                    "their expense is not limited by their own appetite, so the public "
                    "riches cannot be limited either. He does not say the sovereign may "
                    "not own land; he says a fixed portion will be sold, given away or "
                    "found insufficient, and the Conqueror's taxes proved it."},
        ],
        "mistakes": [
            ("Thinking the sovereign's share and the subjects' shares are separate pots",
             "Hobbes's subject has property against every other subject and not against "
             "the sovereign. The lab sets Levi's tenth aside before anything else is "
             "worked out, and the twelve portions share what is left, so the whole "
             "thing is one distribution made by one will. It is not an agreement among "
             "equals."),
            ("Reading <em>arbitrary</em> as <em>unjust</em>",
             "Hobbes calls the division of Canaan arbitrary because it followed the "
             "discretion of Eleazar and Joshua and not the judgement of any subject. He "
             "says the sovereign distributes &ldquo;agreeable to Equity, and the Common "
             "Good&rdquo;. Arbitrary here means by his will, and whether a particular "
             "distribution was equitable is a separate question."),
            ("Rounding a share that does not divide",
             "Twelve hundred measures cannot be shared whole among weights summing to "
             "13 after a tenth is taken off. Rounding each share makes the total wrong "
             "and hides who got more. The lab prints the exact fraction."),
        ],
        "standard": (
            "Finish when you can divide a total by stated weights after a set-aside part.",
            "Given a total, a set-aside fraction and a list of weights, compute the part "
            "set apart, the remainder and each share as an exact figure, and say where "
            "Hobbes puts the power to make the division."
        ),
        "note": (
            "The harvest and the weights are written for this lesson; Hobbes gives no "
            "quantities, and says the division was arbitrary, not that it was equal. The "
            "lab shows what follows from the shares stated, on Hobbes's definitions, and "
            "cannot say whether property is made by the sovereign, as he argues, or "
            "precedes government, as Locke argued."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Leviathan ch. 25, 1651 p. 135; PDF p. 277 of the operator's copy
    {
        "slug": "counsel",
        "title": "Of Counsel",
        "module": "Chapter 25 · Of Counsell",
        "one_line": "Command is for the commander's benefit and counsel for the counselled, and a sovereign is better advised by men heard apart than by an assembly.",
        "summary": (
            "Hobbes separates counsel from command and from exhortation, lists what makes a "
            "good counsellor and argues that counsellors should be heard apart, not "
            "in an assembly. A majority of independent counsellors, each right with a stated "
            "chance, is right more often than any one of them; the lab computes it, and then "
            "shows what happens when the counsellors are not independent."
        ),
        "key": [
            "command: for the commander's benefit",
            "counsel: for the counselled man's benefit",
            "heard apart: every man's own advice",
            "right if more than n/2 are right",
            "this assumes the votes are independent",
        ],
        "key_label": "Counsel in five lines",
        "concepts_intro": (
            "Chapter 25 is a short chapter of definitions followed by one argument about "
            "how many counsellors to hear and how."
        ),
        "concepts": [
            ("Command and counsel",
             "Command says do this without any reason but the will of the speaker, so the "
             "commander pretends his own benefit, and a man may be obliged to obey it. "
             "Counsel gives reasons from the benefit of the man advised, so he cannot be "
             "obliged to follow it, because the hurt of not following it is his own."),
            ("Exhortation",
             "Exhortation and dehortation are counsel pressed with vehemence, using "
             "similitudes, metaphors and examples, so as to move the passions. Hobbes says "
             "this shows the speaker's own benefit, so that those who exhort when asked "
             "for counsel are corrupt counsellors."),
            ("The marks of a good counsellor",
             "His ends must not be inconsistent with the ends of the man he counsels; he "
             "must speak so that the truth appears, with firm reasoning and without "
             "metaphor; he must have experience and study in the business at hand; and "
             "for matters touching another state he must know its letters and treaties."),
        ],
        "read_title": "The passage first, then the argument for hearing counsellors apart",
        "read_intro": (
            "The passage is the first of Hobbes's reasons for hearing counsellors "
            "apart. The rest of the chapter has led up to it."
        ),
        "body": [
            ("p", "<strong>Chapter 25.</strong> &ldquo;Supposing the number of Counsellors "
                  "equall, a man is better Counselled by hearing them apart, then in an "
                  "Assembly; and that for many causes. First, in hearing them apart, you "
                  "have the advice of every man; but in an Assembly many of them deliver "
                  "their advise with I, or No, or with their hands, or feet, not moved by "
                  "their own sense, but by the eloquence of another, or for feare of "
                  "displeasing some that have spoken, or the whole Assembly, by "
                  "contradiction&rdquo;"),
            ("p", "Think of the last time you asked three friends what to do about "
                  "something, one at a time, and the time you asked them all at once in a "
                  "group chat. Hobbes thinks you got more out of the first. His chapter "
                  "begins by noticing that &ldquo;Doe this&rdquo; is said by the man who "
                  "commands, by the man who advises and by the man who exhorts, and that "
                  "people mistake one for another according to what they want to "
                  "conclude. He fixes the words. &ldquo;COMMAND is, where a man saith, Doe "
                  "this, or Doe not this, without expecting other reason than the Will of "
                  "him that sayes it&rdquo;; &ldquo;COUNSELL, is where a man saith, Doe, or "
                  "Doe not this, and deduceth his reasons from the benefit that arriveth "
                  "by it to him to whom he saith it&rdquo;. From these come three "
                  "differences. Command is to the commander's benefit and counsel to the "
                  "other man's; a man may be obliged to do what he is commanded but not "
                  "what he is counselled, because if he covenants to follow counsel it "
                  "has turned into command; and no man may claim a right to be of "
                  "another's counsel."),
            ("p", "His examples are from Scripture. &ldquo;Kill not&rdquo; and &ldquo;Honour "
                  "thy Parents&rdquo; are commands, because the reason is the will of God "
                  "our King. &ldquo;Sell all thou hast; give it to the poore; and follow "
                  "me&rdquo; is counsel, because the reason offered is our own treasure in "
                  "heaven, and so is &ldquo;Repent, and be Baptized&rdquo;, because God "
                  "&ldquo;shall still be King in what manner soever we rebell&rdquo;. A "
                  "counsellor also has a protection: he who asks counsel is its author, "
                  "and so cannot punish it. Hobbes adds that a counsellor to the sovereign "
                  "cannot in equity be punished for what he said when asked."),
            ("p", "Then the good counsellor. Since counsel is &ldquo;but the Speech "
                  "whereby that experience is made known to another&rdquo;, the virtues of "
                  "a counsellor are the intellectual virtues of Chapter 8, and to the "
                  "artificial man his counsellors serve &ldquo;in the place of Memory, and "
                  "Mentall Discourse&rdquo;. But there is a difference from the natural "
                  "man, whose experience comes from objects that work upon him without "
                  "passion or interest of their own. A counsellor to a commonwealth has "
                  "his own ends. So the first condition of a good counsellor is that his "
                  "ends and interest be not inconsistent with those of the man he counsels, "
                  "and the second, third and fourth are the marks of a mind able to "
                  "reason clearly, long experienced in the business and informed of "
                  "foreign affairs."),
            ("p", "Now go back to the fifth condition, the one quoted at the top. "
                  "Hobbes gives four reasons for hearing counsellors apart. In an "
                  "assembly men vote with &ldquo;I, or No&rdquo;, moved by another's "
                  "eloquence or by fear of looking duller than the others. Some will have "
                  "interests contrary to the public, and &ldquo;Passion eloquent&rdquo; "
                  "draws others to the same advice, as many brands enflame one another. "
                  "Apart, one may interrupt and examine a man's reasons, which cannot be "
                  "done in an assembly where a man is &ldquo;astonied, and dazled with "
                  "the variety of discourse&rdquo;, and where there is always somebody "
                  "after applause for his orations. And the counsels of many are dangerous "
                  "where secrecy is needed. He closes with the tennis image: a man does "
                  "best with able seconds placed each in his proper station, worst of all "
                  "when carried in a frame heavy of itself, like a man taken to the ball "
                  "in a wheelbarrow."),
            ("p", "There is a famous argument on the other side. In 1785 the Marquis de "
                  "Condorcet showed that if each member of a group is right with a chance "
                  "greater than one half, and their votes are independent, the majority is "
                  "right more often than any one member, and the more members the better. "
                  "Hobbes could not have known it, and the lab computes it: with three "
                  "counsellors each right with `3/5` the majority is right with `81/125`, "
                  "about 65 per cent, in the apart-three preset, and with eleven in "
                  "apart-eleven it is `36791901/48828125`, about 75 per cent. Hearing "
                  "more counsellors apart helps."),
            ("p", "But look at what the figure assumes. It assumes the votes are "
                  "independent, and every one of Hobbes's four reasons is a reason they "
                  "are not: men follow an orator, fear the room, catch one another's "
                  "passions. Take the extreme case. If ten of eleven always vote as the "
                  "first speaker did, the assembly is one man's opinion eleven times "
                  "over, and the one-voice preset (n = 1) gives `3/5`, no better than the "
                  "orator alone. The theorem is also a theorem of competence: with each "
                  "counsellor right only `2/5` of the time the poor preset gives "
                  "`12036224/48828125`, about 25 per cent, and a bigger body is wrong "
                  "more often. Hobbes's point about interests is a doubt about "
                  "competence as well, and the lab cannot tell which case is the real "
                  "one."),
            ("p", "Hobbes also says something the theorem does not. &ldquo;many eys see "
                  "more then one; yet it is not to be understood of many Counsellours; but "
                  "then only, when the finall Resolution is in one man.&rdquo; The "
                  "counsellors advise and one man decides, so the lab's majority "
                  "vote is not Hobbes's institution: he does not tally votes, he hears "
                  "reasons. The model shows only that his preference for hearing apart "
                  "can be read as a preference for independent evidence, and that is a "
                  "reading, not his claim. The next lesson, <em>Of Civil Laws</em>, "
                  "takes up the sovereign's own relation to the laws."),
        ],
        "lab": ("choicekit", {
            "mode": "vote",
            "preset": "apart-three",
            "presets": [
                {"id": "apart-three", "label": "Three counsellors heard apart, each right with 3/5",
                 "kind": "jury", "n": 3, "p": "3/5", "expect": {"voJury": "81/125", "voPivot": "12/25"}},
                {"id": "apart-eleven", "label": "Eleven counsellors heard apart, each right with 3/5",
                 "kind": "jury", "n": 11, "p": "3/5", "expect": {"voJury": "36791901/48828125", "voPivot": "1959552/9765625"}},
                {"id": "one-voice", "label": "An assembly that votes as one man, right with 3/5",
                 "kind": "jury", "n": 1, "p": "3/5", "expect": {"voJury": "3/5", "voPivot": "1"}},
                {"id": "poor", "label": "Eleven counsellors, each right with 2/5",
                 "kind": "jury", "n": 11, "p": "2/5", "expect": {"voJury": "12036224/48828125", "voPivot": "1959552/9765625"}},
            ],
            "panel_title": "Compute a majority of counsellors",
            "panel_intro": (
                "A group reads n=3 p=3/5: an odd number of independent counsellors, each "
                "right with the chance p. The tile gives the chance their majority is "
                "right. It follows from those two numbers; whether counsellors in a real "
                "assembly are independent is what Hobbes denies."
            ),
        }),
        "steps_title": "Computing the majority of independent counsellors",
        "steps_intro": "Four steps, for an odd number of counsellors.",
        "steps": [
            ("State the question and the chance",
             "The question has a right answer, and each counsellor is right with the same "
             "chance `p`, independently of the others. Write down `n` and `p`."),
            ("List the counts that win",
             "The majority is right when more than half are right: from `(n + 1)/2` up to "
             "`n` counsellors."),
            ("Find the chance of each count",
             "A particular set of `k` right counsellors has chance `p` to the power `k` "
             "times `1 - p` to the power `n - k`, and there are as many such sets as "
             "ways to choose them."),
            ("Add, and compare with `p`",
             "The sum is the chance the majority is right. If it is above `p`, hearing "
             "them together has beaten hearing one. Then ask whether the independence "
             "the sum assumes is true of these counsellors."),
        ],
        "worked": {
            "title": "Three counsellors, each right with 3/5",
            "intro": ["The majority is right when two or three of the three are."],
            "lines": [
                "exactly two right:  3 · (3/5)² · (2/5) = 54/125",
                "all three right:  (3/5)³ = 27/125",
                "majority right:  54/125 + 27/125 = 81/125",
                "one counsellor alone:  3/5 = 75/125",
            ],
            "after": [
                "`81/125` is 6/125 above `75/125`. The gain is real and small, and it "
                "exists only if the three do not copy one another.",
            ],
        },
        "quiz_title": "Counsel, command and the majority",
        "quiz": [
            {"q": "Which of these, on Hobbes's definitions, makes what a man says counsel "
                  "and not command?",
             "a": ["It is spoken in the imperative mood",
                   "It binds the hearer, if he has covenanted to follow it",
                   "It gives reasons drawn from the benefit of the man advised",
                   "It is spoken by someone who gains if it is followed"],
             "c": 2,
             "why": "Counsel &ldquo;deduceth his reasons from the benefit that arriveth "
                    "by it to him to whom he saith it&rdquo;. The imperative mood is shared "
                    "by command, counsel and exhortation, which is why Hobbes defines "
                    "them. A covenant to follow turns counsel into command, and a "
                    "speaker who pursues his own benefit is, by the definition, "
                    "commanding or exhorting."},
            {"q": "Three counsellors, independent, each right with 3/5. What is the chance "
                  "that their majority is right?",
             "a": ["3/5", "81/125", "27/125", "54/125"],
             "c": 1,
             "why": "Two right is `54/125` and three right is `27/125`, and the majority is "
                    "right in either case: `81/125`. `3/5` is one counsellor, `27/125` is "
                    "only the case of all three, and `54/125` is only exactly two."},
            {"q": "Eleven counsellors, each right with 3/5 alone, vote as one man because "
                  "ten follow the first speaker. What is the chance the assembly is right?",
             "a": ["36791901/48828125", "1/2", "2/5", "3/5"],
             "c": 3,
             "why": "If ten simply repeat the first speaker, the vote is right exactly "
                    "when he is, with chance `3/5`. The first answer is the independent "
                    "case."},
            {"q": "Hobbes says many assembly members vote &ldquo;not moved by their own "
                  "sense, but by the eloquence of another&rdquo;. Which assumption of the "
                  "majority figure does that deny?",
             "a": ["That the counsellors' votes are independent",
                   "That the number of counsellors is odd",
                   "That each counsellor is right more often than not",
                   "That the question has a right answer"],
             "c": 0,
             "why": "Following another's eloquence makes one vote depend on another, which "
                    "is what independence rules out. Hobbes's remarks on interests bear on "
                    "competence, and his remark here bears on independence."},
        ],
        "mistakes": [
            ("Thinking more counsellors always make better counsel",
             "The majority figure rises with the number of counsellors only if each is "
             "right more than half the time and they are independent. At `2/5` it falls "
             "(the poor preset), and if the group copies one voice it is flat at the "
             "one counsellor's chance."),
            ("Taking the majority theorem for Hobbes's argument",
             "Hobbes does not recommend counting votes. He recommends that a man hear each "
             "counsellor apart, examine his reasons, and decide, so that the final "
             "resolution is in one man. The lab reads one of his reasons as a claim about "
             "independence; the rest of his case, such as examining a man's reasons by "
             "interruption, the lab cannot see."),
            ("Treating command and counsel as differing in tone",
             "Hobbes says they differ in whose benefit the reason names. A kindly worded "
             "command remains a command, and Hobbes allows a father or a general to "
             "sweeten commands &ldquo;in the tune and phrase of Counsell&rdquo;, but "
             "then they are commands and no longer counsels."),
        ],
        "standard": (
            "Finish when you can compute a majority and say what it assumes.",
            "Given the number of counsellors and the chance each is right, compute the "
            "chance their majority is right, compare it with one counsellor, and name the "
            "assumption that Hobbes's reasons for hearing them apart call into question."
        ),
        "note": (
            "The jury figure is Condorcet's, of 1785, applied to Hobbes's chapter; it "
            "is not in the text. It treats each counsellor as right with a fixed chance "
            "and independent of the rest, and the chapter's four reasons are exactly "
            "the claim that in assemblies they are not. The lab can show what follows if "
            "they are, and cannot say how far any real assembly was."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Leviathan ch. 26, 1651 pp. 137-138; PDF p. 280 of the operator's copy
    {
        "slug": "civil-laws",
        "title": "Of Civil Laws",
        "module": "Chapter 26 · Of Civill Lawes",
        "one_line": "A law is a command of the sovereign, so the sovereign, who can repeal it, is not bound by it.",
        "summary": (
            "Hobbes defines civil law as the rules the commonwealth has commanded a "
            "subject to use for the distinction of right and wrong, and derives from the "
            "definition that the sovereign is the only legislator and is not subject to "
            "the civil laws. Set that argument out as premises and a conclusion, check that "
            "it is valid, and find the premise a common lawyer would deny."),
        "key": [
            "law is command, not counsel",
            "only the sovereign legislates",
            "who can repeal a law is free of it",
            "valid: no case with true premises, false end",
            "valid is not true: test the premises",
        ],
        "key_label": "Civil law in five lines",
        "concepts_intro": (
            "Chapter 26 is long. Hobbes gives a definition, deduces from it a list of "
            "consequences, and then turns to interpretation, the kinds of law and the "
            "difference between a law and a right."
        ),
        "concepts": [
            ("The definition",
             "Law is not counsel but command, and not the command of any man to any man "
             "but of him whose command is addressed to one already obliged to obey him. "
             "Civil law adds only the name of the person commanding, the person of the "
             "commonwealth. It is the set of rules the commonwealth has commanded, by "
             "word, writing or sufficient sign, for the distinction of right and wrong."),
            ("Law of nature and civil law",
             "Hobbes says the law of nature and the civil law &ldquo;contain each other, "
             "and are of equall extent&rdquo;. In the condition of mere nature the laws of "
             "nature are not properly laws, but qualities that dispose men to peace. In a "
             "commonwealth they are laws, because they are then the sovereign's "
             "commands; and obedience to the civil law is itself a part of the law of "
             "nature, because justice is the performance of covenant."),
            ("Interpretation",
             "A law's authority is the sovereign's command, and its meaning is his "
             "intention. Interpreters are those the sovereign appoints, and a judge's "
             "sentence is law only to the parties pleading, because &ldquo;No mans "
             "error becomes his own Law&rdquo;. Commentaries on the law are not "
             "interpretation either."),
        ],
        "read_title": "The passage first, then the argument as premises",
        "read_intro": (
            "The passage is the second of the consequences Hobbes draws from his "
            "definition. Then it is written as a short argument the lab can check."
        ),
        "body": [
            ("p", "<strong>Chapter 26.</strong> &ldquo;The Soveraign of a Common-wealth, "
                  "be it an Assembly, or one Man, is not Subject to the Civill Lawes. For "
                  "having power to make, and repeale Lawes, he may when he pleaseth, free "
                  "himselfe from that subjection, by repealing those Lawes that trouble "
                  "him, and making of new; and consequently he was free before. For he is "
                  "free, that can be free when he will: Nor is it possible for any person "
                  "to be bound to himselfe; because he that can bind, can release; and "
                  "therefore he that is bound to himselfe onely, is not bound.&rdquo;"),
            ("p", "Think of a club that has a rule against being late. The committee can "
                  "change the rule at its next meeting. Is the committee bound by the rule "
                  "in the meantime? Hobbes's answer is that it is not, or not really: a "
                  "rule that those who made it can unmake at will is a rule they apply to "
                  "others. The sentence above is the sharpest form of that thought, and "
                  "it is the most quarrelled-over sentence in the chapter. Before "
                  "looking at it, read how Hobbes gets there. He defines civil law as "
                  "&ldquo;those Rules, which the Common-wealth hath Commanded him, by Word, "
                  "Writing, or other sufficient Sign of the Will, to make use of, for the "
                  "Distinction of Right, and Wrong&rdquo;, and says &ldquo;Law in generall, "
                  "is not Counsell, but Command&rdquo;. He then says that whatever follows "
                  "from the definition by necessary consequence ought to be acknowledged "
                  "for truth, and starts to deduce."),
            ("p", "The first consequence is that the sovereign is the only legislator, "
                  "because the commonwealth has no capacity to act except through its "
                  "representative, and a law is abrogated only by another law forbidding "
                  "it to be put in execution. The second is the passage at the top. "
                  "Put it in order. The sovereign has the power to make and repeal laws. "
                  "So he can free himself from any law whenever he likes. Whoever can free "
                  "himself whenever he likes is free. So he is free of the laws, and "
                  "&ldquo;consequently he was free before&rdquo;. The last sentence adds "
                  "that a man cannot be bound to himself, because he who can bind can "
                  "release. The lab writes this with three sentence letters: p, the "
                  "sovereign can repeal any civil law when he pleases; q, he can free "
                  "himself from any civil law when he pleases; r, he is free from the "
                  "civil laws."),
            ("p", "In the hobbes preset the premises are `p`, `p → q` and `q → r`, and the "
                  "conclusion is `r`. There are eight rows of true and false, and no row "
                  "makes the premises true and `r` false, so the argument is valid. Take "
                  "away the first premise, in the coke preset, and the lab finds one "
                  "counterexample: `p`, `q` and `r` all false, where both conditionals are "
                  "true and the conclusion is not. And in the bare preset, with `p` and "
                  "`p → q` but no `q → r`, the conclusion `r` has a counterexample row "
                  "with `p` and `q` true. Each premise is needed, and the lab shows "
                  "which one is doing which work."),
            ("p", "What would a common lawyer deny? Hobbes had them in view: in the "
                  "chapter he answers the saying that &ldquo;the Common Law, hath no "
                  "Controuler but the Parlament&rdquo;, and Sir Edward Coke, the great "
                  "judge and writer of the law of England, who died in 1634 after "
                  "defending the common law against James I and Charles I. Hobbes writes "
                  "that it is not right to say law is any &ldquo;Artificiall perfection "
                  "of Reason, gotten by long study, observation, and experience&rdquo;, as "
                  "Coke made it; it is &ldquo;the Reason of this our Artificiall Man the "
                  "Common-wealth, and his Command, that maketh Law&rdquo;. For the lawyers "
                  "the law is something older and wiser than any ruler's will, and a king "
                  "cannot repeal it because he did not make it. They deny the first "
                  "premise, that the law is what the sovereign can repeal at will. The "
                  "coke preset is that denial: with it gone, the other two premises, "
                  "which Hobbes and his critics might both grant, no longer deliver "
                  "the conclusion."),
            ("p", "Weigh the two sides fairly. Hobbes's argument has a clean structure "
                  "and is hard to escape if you accept his definition: if all law is "
                  "command and the commander can recall it, the commander is not "
                  "commanded. His reason, given in Chapter 29, is that a law above the "
                  "sovereign sets a judge above him, and a judge above that judge, "
                  "&ldquo;and so continually without end&rdquo;. The lawyers' "
                  "answer, and later Locke's, is that a ruler may be under a law he "
                  "cannot himself repeal, such as the terms on which he was trusted. "
                  "Neither is shown to be right by the lab. The checker says whether "
                  "the conclusion follows, and that is all."),
            ("p", "The rest of the chapter works out what the definition implies. Custom "
                  "is law only by the sovereign's silence, since &ldquo;it is not the "
                  "Length of Time that maketh the Authority, but the Will of the "
                  "Soveraign&rdquo;. A law not made known is no law to the man who could "
                  "not know it, and the laws of nature, which every man can know by his "
                  "reason, are the only unwritten laws. Hobbes distinguishes law from "
                  "right in one line: &ldquo;Lex and Jus, are as different as Obligation "
                  "and Liberty.&rdquo; The next lesson, <em>Crimes, Excuses and "
                  "Extenuations</em>, begins from the same definition and asks what "
                  "follows when a law is broken."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "preset": "hobbes",
            "show": "all",
            "presets": [
                {"id": "hobbes", "label": "p, p → q and q → r, so r",
                 "premises": ["p", "p -> q", "q -> r"], "conclusion": "r", "expect": {"vaRows": "8", "vaCounter": "0", "vaVerdict": "Valid"}},
                {"id": "coke", "label": "p removed: p → q and q → r, so r",
                 "premises": ["p -> q", "q -> r"], "conclusion": "r", "expect": {"vaRows": "8", "vaCounter": "1", "vaVerdict": "Invalid"}},
                {"id": "bare", "label": "q → r removed: p and p → q, so r",
                 "premises": ["p", "p -> q"], "conclusion": "r", "expect": {"vaRows": "8", "vaCounter": "1", "vaVerdict": "Invalid"}},
            ],
            "panel_title": "Which cases would break the argument",
            "panel_intro": (
                "Each row is a case: a true or false for p, q and r. A row is "
                "highlighted when every premise is true and the conclusion false. "
                "The lab tests the form only. Whether the premises are true of "
                "sovereigns is what Hobbes and his critics argue."
            ),
        }),
        "steps_title": "Testing an argument from a definition",
        "steps_intro": "Five steps, in this order. The last is the one the checker cannot do.",
        "steps": [
            ("Find the claim being deduced",
             "Here the conclusion is that the sovereign is not subject to the civil "
             "laws. Write it as one sentence."),
            ("List the steps as premises",
             "Hobbes's &ldquo;for&rdquo; and &ldquo;consequently&rdquo; mark the steps. "
             "Give each a letter and write the links as conditionals."),
            ("Check the form",
             "Run the premises and conclusion through the checker. A highlighted row is a "
             "case where the premises hold and the conclusion fails."),
            ("Remove each premise in turn",
             "If the argument stops being valid, that premise was needed. If it stays "
             "valid, the premise was padding."),
            ("Ask who denies which premise",
             "A valid argument gives its critic nowhere to go except to deny a premise. "
             "Say which one, and why."),
        ],
        "worked": {
            "title": "Hobbes's argument, row by row",
            "intro": ["Premises p, p → q, q → r; conclusion r. Take the case with p true."],
            "lines": [
                "p true, q true, r true:  premises true, r true",
                "p true, q true, r false:  q → r false, so no counterexample",
                "p true, q false, r any:  p → q false, so no counterexample",
                "p false:  p is false, so no counterexample",
            ],
            "after": [
                "Every row where all three premises are true has `r` true, so none is a "
                "counterexample. The same check, run on a premise-set without `p`, finds "
                "the row where `p`, `q` and `r` are false.",
            ],
        },
        "quiz_title": "Law as command",
        "quiz": [
            {"q": "In the lab, remove premise p (the sovereign can repeal any law at will) "
                  "and keep p → q and q → r. What does the checker find?",
             "a": ["Valid, because the conditionals chain",
                   "Invalid, with one counterexample in which p, q and r are all false",
                   "Invalid, with a counterexample in which p is true and r is false",
                   "Valid, because r is true in every row"],
             "c": 1,
             "why": "With `p` gone, a row with `p`, `q` and `r` all false makes both "
                    "conditionals true and `r` false. Chaining the conditionals gives `p → "
                    "r`, which is not `r`. A row with `p` true and `r` false would "
                    "falsify one of the conditionals."},
            {"q": "What does Hobbes say Sir Edward Coke made the reason of the law, in "
                  "the passage in which he says law is never against reason?",
             "a": ["The will of the sovereign",
                   "The consent of every subject",
                   "The length of time a custom has been used",
                   "An artificial perfection of reason, gotten by long study, "
                   "observation and experience"],
             "c": 3,
             "why": "Hobbes writes that law is not that, &ldquo;as Sr. Ed. Coke makes it&rdquo;, "
                    "&ldquo;an Artificiall perfection of Reason, gotten by long study, "
                    "observation, and experience&rdquo;; the reason that makes law is that of the "
                    "commonwealth and his command. The sovereign's will is Hobbes's own "
                    "answer, and length of time is a ground of custom he rejects."},
            {"q": "How does Hobbes say Lex and Jus differ?",
             "a": ["Lex is as different from Jus as Obligation from Liberty",
                   "Lex is written law and Jus unwritten",
                   "Lex is divine law and Jus human law",
                   "They do not differ; the learned use them for one thing"],
             "c": 0,
             "why": "Hobbes says the learned use them promiscuously, which they ought "
                    "not: right is liberty, the liberty the civil law leaves us, and law "
                    "is an obligation that takes away the liberty of nature, so &ldquo;Lex "
                    "and Jus, are as different as Obligation and Liberty&rdquo;."},
            {"q": "Hobbes's argument that the sovereign is free of the civil laws is "
                  "valid in the lab. What follows?",
             "a": ["Its premises are all true",
                   "A critic must accept it",
                   "Its conclusion is true if every premise is true",
                   "Its conclusion is true"],
             "c": 2,
             "why": "Validity means no case has true premises and a false conclusion. "
                    "The conclusion is therefore guaranteed only if the premises are "
                    "true. A critic who denies the premise that law is command, as the "
                    "common lawyers did, is not refuted by a valid argument."},
        ],
        "mistakes": [
            ("Thinking a valid argument settles the question",
             "The checker finds no row with true premises and a false conclusion in "
             "Hobbes's argument, and that is all it finds. The coke preset shows how "
             "easily the conclusion fails when the first premise is not granted. The "
             "dispute between Hobbes and the lawyers lives in that premise."),
            ("Reading <em>not subject to the civil laws</em> as <em>above all "
                  "law</em>",
             "Hobbes keeps the sovereign under the laws of nature, which &ldquo;be "
             "Divine, and cannot by any man, or Common-wealth be abrogated&rdquo; "
             "(Chapter 29). The conclusion is about the civil laws only, the laws "
             "the commonwealth makes."),
            ("Treating custom as a rival source of law",
             "Hobbes says long use obtains the authority of law only by the sovereign's "
             "silence, which he allows may be consent. Custom is therefore a law "
             "while he does not forbid it, and no longer."),
        ],
        "standard": (
            "Finish when you can set out the argument and test it.",
            "Write Hobbes's argument that the sovereign is not subject to the civil laws "
            "as premises and a conclusion, test it with the checker, name each premise "
            "that is needed, and say which one the common lawyers would deny."
        ),
        "note": (
            "The lab checks form. It treats p, q and r as plain sentences and cannot say "
            "whether Hobbes's definition of law as command is right, or whether Coke's "
            "account of the common law as reason is. The premise that carries the "
            "dispute is the premise on which the lab is silent."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Leviathan ch. 27, 1651 p. 153; PDF p. 299 of the operator's copy
    {
        "slug": "crimes-excuses-and-extenuations",
        "title": "Crimes, Excuses and Extenuations",
        "module": "Chapter 27 · Of Crimes, Excuses, and Extenuations",
        "one_line": "A crime is a sin that can be shown to a judge, and a punishment too small to outweigh the gain invites the crime.",
        "summary": (
            "Hobbes separates sin from crime, finds the source of every crime in a defect of "
            "understanding, an error of reasoning or the force of the passions, and lists "
            "what excuses and what only extenuates. Among the passions, hope of impunity does "
            "the most work. Put a gain, a penalty and a chance of being punished into the "
            "lab and see when a crime pays."
        ),
        "key": [
            "sin: any breach, even in intention",
            "crime: a sin a judge can be shown",
            "source: understanding, reasoning, passions",
            "expected penalty = chance · penalty",
            "a crime pays when expected penalty < gain",
        ],
        "key_label": "Chapter 27 in five lines",
        "concepts_intro": (
            "Chapter 27 sorts what breaks the law by what is in the breaker's mind, and "
            "then ranks it."
        ),
        "concepts": [
            ("Sin and crime",
             "A sin is any transgression of a law and any contempt of the legislator, "
             "including the intention to transgress. A crime is a sin that consists in "
             "doing what the law forbids or omitting what it commands. Every crime is a sin "
             "and not every sin a crime, since an intention that never appears in word or "
             "deed cannot be accused before a human judge."),
            ("The sources of crime",
             "Hobbes finds the source of every crime in some defect of understanding "
             "(ignorance of the law, the sovereign or the penalty), some error in "
             "reasoning (false principles, false teachers, wrong inferences) or some "
             "sudden force of the passions: vain-glory, anger, hate, lust, ambition, "
             "covetousness, and fear."),
            ("Excuse and extenuation",
             "An excuse takes away the nature of a crime; an extenuation only makes it "
             "less. What excuses is whatever takes away the obligation of the law, such as "
             "having no means to know it or acting under present fear of death. Crimes "
             "are not all of one weight, so Hobbes rejects the Stoic claim that to kill "
             "a hen is as great a crime as to kill a father."),
        ],
        "read_title": "The passage first, then the chapter's reasoning",
        "read_intro": (
            "The passage comes from Hobbes's remarks on ignorance of the penalty. It "
            "is the only place in the chapter where he puts the offender's reasoning "
            "as a comparison of two sizes."
        ),
        "body": [
            ("p", "<strong>Chapter 27.</strong> &ldquo;For the punishment foreknown, if it "
                  "be not great enough to deterre men from the action, is an invitement to "
                  "it: because when men compare the benefit of their Injustice, with the "
                  "harm of their punishment, by necessity of Nature they choose that which "
                  "appeareth best for themselves&rdquo;"),
            ("p", "The chapter begins with a distinction so useful it has stayed in "
                  "ordinary speech. A sin &ldquo;is not onely a Transgression of a Law, "
                  "but also any Contempt of the Legislator&rdquo;, and so may consist in "
                  "the &ldquo;purpose to transgresse&rdquo;. But &ldquo;every Crime is a "
                  "sinne; but not every sinne a Crime&rdquo;. A crime needs a deed or a "
                  "word that a judge can be shown. Hobbes is gentle about the borderline: "
                  "to be pleased in imagining what would please one if it were real is "
                  "a passion so natural that to make it a sin &ldquo;were to make Sinne of "
                  "being a man&rdquo;. A man is sinful when he resolves to act, and a "
                  "criminal when he does. And where there is no civil law there is no "
                  "crime, because there is no one to accuse; there is still sin, because "
                  "the law of nature is eternal."),
            ("p", "Then the sources. &ldquo;The source of every Crime, is some defect of "
                  "the Understanding; or some errour in Reasoning; or some sudden force of "
                  "the Passions.&rdquo; Ignorance of the law of nature excuses no man, "
                  "since every man who has the use of reason is supposed to know that he "
                  "should not do to another what he would not have done to himself; "
                  "ignorance of the civil law excuses only where the law has not been "
                  "declared as a man could know it if he wished; ignorance of the "
                  "sovereign excuses no one, for he ought to know the power that protects "
                  "him; and ignorance of the penalty excuses no one either, but here "
                  "comes the passage you have just read."),
            ("p", "Read it slowly. Hobbes first says a man who breaks a law with no "
                  "penalty named takes the arbitrary penalty, and a man who breaks one "
                  "with a penalty named is excused any greater penalty. Then he says "
                  "why. The penalty, foreknown, is part of the offender's reasoning: he "
                  "compares &ldquo;the benefit of their Injustice, with the harm of their "
                  "punishment&rdquo;, and chooses what &ldquo;appeareth best&rdquo;. So a "
                  "penalty too small to outweigh the benefit does not deter but "
                  "&ldquo;is an invitement&rdquo;, and a man is excused any penalty heavier than "
                  "the law named, because &ldquo;it is the "
                  "Law that tempted, and deceiveth them&rdquo;. A thief who is given a "
                  "choice between a fine below what he will gain and none is not choosing "
                  "wickedness over virtue. He is doing a sum."),
            ("p", "The lab does that sum, with one addition that is not Hobbes's but "
                  "is hinted at by him. The offender is not sure to be punished. Hobbes "
                  "says covetousness and ambition are &ldquo;perpetually incumbent, and "
                  "pressing&rdquo;, whereas reason is not always present, and so "
                  "&ldquo;whensoever the hope of impunity appears, their effects "
                  "proceed&rdquo;. The lab gives the hope a number: the chance that the "
                  "penalty is inflicted. Take a fraud that gains 100, with a penalty of "
                  "150. In the always preset the offender is sure to be punished, the "
                  "expected penalty is 150, and the crime does not pay. In the half preset "
                  "he is caught one time in two, the expected penalty is 75, below the "
                  "gain, and it pays; the lab's tile for the figure a penalty must "
                  "exceed to deter at that chance reads 200. In the rich preset, for a man who "
                  "can corrupt the court and is caught one time in four, the expected "
                  "penalty of 150 is only `75/2`, 37.50, and a penalty above 400 would be needed."),
            ("p", "Hobbes sees this. Of the passions that cause crime the first he names is "
                  "vain-glory, the foolish over-rating of one's own worth, "
                  "from which comes the presumption that the penalties extended to all "
                  "subjects ought not to be inflicted on oneself with the same rigour as "
                  "on the poor, so that &ldquo;such as value themselves by the greatnesse "
                  "of their wealth, adventure on Crimes, upon hope of escaping punishment, "
                  "by corrupting publique Justice, or obtaining Pardon by Mony&rdquo;. "
                  "That is the rich preset in words. He also says those who deceive "
                  "&ldquo;upon hope of not being observed&rdquo; deceive themselves, being "
                  "&ldquo;no wiser than Children, that think all hid, by hiding their own "
                  "eyes&rdquo;. That is Hobbes's judgement of the sum and not part of it: "
                  "the lab takes the chance as given and cannot say whether the "
                  "offender's hope is reasonable."),
            ("p", "The chapter ends with degrees. A crime is greater when its source "
                  "is presumption of strength, riches or friends than hope of escape; "
                  "greater when committed against conscience; less when the error came "
                  "from a publicly authorised teacher; greater when it injures many and "
                  "when, by example, it will injure in the future; greater against the "
                  "commonwealth than against a private man; and, among private injuries, "
                  "greater where the damage is most sensible, killing above maiming "
                  "above theft. He admits &ldquo;all Crimes doe equally deserve the name of "
                  "Injustice, as all deviation from a strait line is equally "
                  "crookednesse&rdquo; but they are not all equally unjust. The next "
                  "lesson, <em>Punishments and Rewards</em>, defines punishment and "
                  "asks what is not one."),
        ],
        "lab": ("levkit", {
            "mode": "law",
            "view": "deter",
            "preset": "half",
            "presets": [
                {"id": "always", "label": "A fraud gaining 100, a penalty of 150, always inflicted",
                 "gain": 100, "penalty": 150, "certainty": 1, "expect": {"llwExpected": "150", "llwDeters": "yes: 150 is more than the gain 100"}},
                {"id": "half", "label": "The same fraud, punished one time in two",
                 "gain": 100, "penalty": 150, "certainty": "1/2", "expect": {"llwExpected": "75", "llwDeters": "no: 75 is less than the gain 100", "llwLeast": "more than 200"}},
                {"id": "rich", "label": "The same fraud, a man who can corrupt the court, one time in four",
                 "gain": 100, "penalty": 150, "certainty": "1/4", "expect": {"llwExpected": "75/2 = 37.50", "llwLeast": "more than 400"}},
            ],
            "panel_title": "When a crime pays",
            "panel_intro": (
                "The benefit of the crime, the penalty and the chance the penalty is "
                "inflicted go in. The lab multiplies the chance by the penalty and compares "
                "the result with the benefit."
            ),
        }),
        "steps_title": "Testing whether a punishment deters",
        "steps_intro": "Four steps, for a crime with a stated gain.",
        "steps": [
            ("State the gain and the penalty",
             "Write the benefit the offender gets and the harm the law ordains, in the "
             "same units."),
            ("State the chance",
             "Write the chance the penalty is inflicted, from 0 to 1. This is the "
             "hope of impunity, made a number."),
            ("Multiply and compare",
             "The expected penalty is the chance times the penalty. If it is less than "
             "the gain, the offender who compares the two does better to offend."),
            ("Find the figure a penalty must exceed",
             "Divide the gain by the chance. A penalty above that has an expected "
             "value above the gain, and one at or below it does not."),
        ],
        "worked": {
            "title": "A fraud gaining 100, a penalty of 150",
            "intro": ["Compare the half preset with the always preset."],
            "lines": [
                "always:  1 · 150 = 150, which exceeds 100",
                "one in two:  1/2 · 150 = 75, which does not exceed 100",
                "one in four:  1/4 · 150 = 75/2, which does not exceed 100",
                "penalty must exceed, one in two:  100 / (1/2) = 200",
                "penalty must exceed, one in four:  100 / (1/4) = 400",
            ],
            "after": [
                "Every halving of the chance of being punished doubles the penalty needed "
                "to deter. That is the sum a legislator would do, and Hobbes puts the "
                "same point as a remark about corrupted justice.",
            ],
        },
        "quiz_title": "Sin, crime and the penalty",
        "quiz": [
            {"q": "On Hobbes's definitions, which of these is a sin but not a crime?",
             "a": ["Stealing, proved before a judge",
                   "Resolving to steal, never shown in word or deed",
                   "Wounding to death a man who assaults you, when you see no other escape",
                   "Doing what the sovereign himself commands against a former law"],
             "c": 1,
             "why": "&ldquo;To intend to steale, or kill, is a sinne, though it never "
                    "appeare in Word, or Fact&rdquo;, and it is not a crime because a human "
                    "judge cannot accuse an intention that never appears. Theft before a "
                    "judge is a crime and a sin. The last two Hobbes "
                    "treats under excuses, where the act is no crime at all."},
            {"q": "A fraud gains 100. The penalty is 150 and is inflicted one time in two. "
                  "On the lab's model, does the penalty exceed the gain in expectation?",
             "a": ["Yes, because 150 exceeds 100",
                   "No, because the expected penalty is 75",
                   "Yes, because 1/2 · 150 exceeds 100",
                   "No, because the expected penalty is 200"],
             "c": 1,
             "why": "The expected penalty is `1/2 · 150 = 75`, which is below the gain of "
                    "100. 200 is the figure a penalty must exceed to deter at that "
                    "chance, not the expected penalty."},
            {"q": "At a chance of one in four, a penalty must exceed what figure for its "
                  "expected value to exceed the gain of 100?",
             "a": ["25", "100", "200", "400"],
             "c": 3,
             "why": "`100 / (1/4) = 400`. At 400 the expected penalty is exactly 100, "
                    "the gain, and the lab counts equal as not deterring, so the penalty "
                    "must be more. 200 is the figure for one in two."},
            {"q": "Which of these does Hobbes say excuses no man?",
             "a": ["Ignorance of the law of nature",
                   "Fear of present death, from which a man cannot escape but by the act",
                   "Captivity in the power of an enemy, without the man's own fault",
                   "Having no means to know the civil law"],
             "c": 0,
             "why": "Ignorance of the law of nature excuses no man, because every man who "
                    "has the use of reason is supposed to know it. The other three "
                    "totally excuse: the obligation of the law ceases or never began."},
        ],
        "mistakes": [
            ("Thinking a harsher penalty always deters",
             "The tile compares the expected penalty with the gain. A very harsh penalty "
             "applied one time in a hundred can still fall below a large gain. Hobbes "
             "says the law should make the penalty exceed the benefit, and the lab shows "
             "that the chance counts as much as the size."),
            ("Taking the chance of punishment as a fact about the offender",
             "The chance is what the offender believes, and Hobbes says those who "
             "believe they will go unseen deceive themselves. The lab computes with the "
             "chance it is given, and cannot say whether the belief is true."),
            ("Reading <em>crime</em> as <em>a sin that is also a harm</em>",
             "Hobbes defines a crime by the civil law forbidding it, not by the harm: "
             "where the civil law ceases, crimes cease, though the sin does not. The "
             "lab's gain and penalty say nothing about whether the act is a crime."),
        ],
        "standard": (
            "Finish when you can say when a crime pays.",
            "Given a gain, a penalty and a chance the penalty is inflicted, compute the "
            "expected penalty, say whether it deters on the model, and find the figure a "
            "penalty must exceed to deter."
        ),
        "note": (
            "The multiplication by a chance is the lab's and not Hobbes's. He compares the "
            "benefit with the harm and speaks of hope of impunity without a number. A "
            "man who weighs nothing, or who counts honour and fear of God, is not "
            "modelled, and Hobbes's own list of sources shows he did not think every "
            "crime a sum."
        ),
    },
]
