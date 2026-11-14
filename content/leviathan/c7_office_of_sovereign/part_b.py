"""Wealth, Counsel, Law and the Office of the Sovereign, lessons 5-8: Chapters 28-31.

Quotations are copied from the operator's copy of the 1651 text (Tuck's edition,
which keeps Hobbes's spelling); the comment beside each lesson gives the chapter,
the 1651 page and the PDF page. Italics are dropped.

Lessons 5 and 7 use levkit; their cfg follows docs/leviathan/PLAN.md section D.1
and is corrected against docs/leviathan/kit-report.md.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    # Leviathan ch. 28, 1651 p. 161; PDF p. 310 of the operator's copy
    {
        "slug": "punishments-and-rewards",
        "title": "Punishments and Rewards",
        "module": "Chapter 28 · Of Punishments, and Rewards",
        "one_line": "A punishment is an evil inflicted by public authority to dispose men to obey, and a harm below the gain, or beyond the law, is something else.",
        "summary": (
            "Hobbes defines punishment, says where the right to punish comes from, and then "
            "draws eleven consequences that say what is not a punishment. Two of them are "
            "arithmetic: a harm less than the benefit of the crime is rather a price, and "
            "whatever is inflicted beyond what the law prescribed is hostility. Test three "
            "cases against them, and meet the name of the book."
        ),
        "key": [
            "punishment: evil by public authority",
            "its end: to dispose men to obey",
            "harm below the gain: a price, not a punishment",
            "harm above the law's: the excess is hostility",
            "reward: salary by contract, or grace",
        ],
        "key_label": "Chapter 28 in five lines",
        "concepts_intro": (
            "Chapter 28 defines punishment and reward, the two nerves of a "
            "commonwealth, and spends most of its length on what the definition leaves out."
        ),
        "concepts": [
            ("The right to punish",
             "Hobbes asks by what door the right to punish came in, since no man covenants "
             "not to resist violence and so cannot give another a right to lay hands on "
             "him. His answer is that the subjects did not give it. Before the "
             "commonwealth every man had a right to everything, and in laying down theirs "
             "they strengthened the sovereign to use his own: it was left to him, entire "
             "except for the limits of the law of nature."),
            ("What is not punishment",
             "From the definition he infers that private revenge, a denial of preferment, "
             "harm without public condemnation, harm by usurped power, harm with no "
             "intent to dispose men to obey, natural consequences, harm for a fact before "
             "the law, harm to the representative and harm to a declared enemy are not "
             "punishments. Two inferences concern size. A harm less than the benefit of the "
             "crime is rather a price, and a harm beyond one the law prescribed is "
             "hostility in its excess."),
            ("Reward",
             "A reward is either a salary, by contract, benefit due for service performed "
             "or promised, or a grace, given to encourage or enable men to serve. Benefits "
             "a sovereign gives to a subject because he fears the subject's power to hurt "
             "are neither: they are rather sacrifices, and they teach further extortion."),
        ],
        "read_title": "The definition first, then what follows from it",
        "read_intro": (
            "The definition is one sentence. Hobbes says that before he infers anything "
            "from it there is a question to answer, and the answer is the most "
            "important thing in the chapter."
        ),
        "body": [
            ("p", "<strong>Chapter 28.</strong> &ldquo;A PUNISHMENT, is an Evill inflicted "
                  "by publique Authority, on him that hath done, or omitted that which is "
                  "Judged by the same Authority to be a Transgression of the Law; to the "
                  "end that the will of men may thereby the better be disposed to "
                  "obedience.&rdquo;"),
            ("p", "Take the sentence piece by piece, as Hobbes does. An evil, so that "
                  "being left out of favour does not count. Inflicted by public authority, "
                  "so that a neighbour's revenge does not count either. On a man who has "
                  "done what the same authority has judged a transgression, so that harm "
                  "first and judgement afterwards is not punishment. And &ldquo;to the end "
                  "that the will of men may thereby the better be disposed to obedience&rdquo;, "
                  "which makes punishment a tool with a purpose, and the purpose is the "
                  "future. Hobbes says so in plain words later in the chapter: the aim of "
                  "punishment is &ldquo;not a revenge, but terrour&rdquo;. A reader "
                  "brought up on Kant will want to stop here. Kant held that a man may "
                  "be punished only because he has committed a crime, never as a "
                  "means to some other good, and that deterrence cannot be the ground. "
                  "That is the main objection to Hobbes's account, and the chapter "
                  "does not answer it except by showing how much of what we want from "
                  "punishment the definition keeps."),
            ("p", "Before inferring anything, Hobbes answers a question &ldquo;of much "
                  "importance&rdquo;: where did the right to punish come from? Not from "
                  "the subjects. &ldquo;In the making of a Common-wealth, every man giveth "
                  "away the right of defending another; but not of defending himselfe&rdquo;, "
                  "and a man cannot give another a right to hurt him that he never had "
                  "to give. The sovereign's right is the right of nature every man had before, "
                  "which the subjects, by laying down theirs, left to him: it was &ldquo;not "
                  "given, but left to him, and to him onely&rdquo;. So the sovereign's "
                  "right to punish is as wide as the right of nature, limited only by "
                  "natural law. A critic would say this takes the sting out of the word "
                  "right: if he may do whatever he thinks necessary, what is it for?"),
            ("p", "Then the inferences. There are eleven, beginning with private revenges "
                  "and ending with harm to a declared enemy, and two of them are sums. "
                  "The seventh: &ldquo;If the harm inflicted be lesse than the benefit, or "
                  "contentment that naturally followeth the crime committed, that harm is "
                  "not within the definition&rdquo;, and is &ldquo;rather the Price, or "
                  "Redemption, than the Punishment of a Crime&rdquo;, because it fails of "
                  "its end and &ldquo;worketh a contrary effect&rdquo;. The eighth: if a "
                  "penalty is prescribed in the law and a greater is inflicted after the "
                  "crime, &ldquo;the excesse is not Punishment, but an act of "
                  "hostility&rdquo;, because the terror of a great punishment unknown is "
                  "taken away by the declaration of a lesser, and &ldquo;the unexpected "
                  "addition is no part of the Punishment&rdquo;."),
            ("p", "The lab tests them. In each preset the crime gains 100 and is "
                  "punished for certain, so the comparison is exactly Hobbes's. In the "
                  "price preset the law prescribes 60 and 60 is inflicted. The penalty "
                  "does not exceed the gain, and by the seventh inference it is "
                  "the price of the crime, not a punishment. In the punishment preset the "
                  "law prescribes 150 and 150 is inflicted; it exceeds the gain, and "
                  "nothing was added. In the excess preset the law prescribes 150 and "
                  "400 is inflicted; the 250 above 150 is, by the eighth, an act of "
                  "hostility. Make the chance of being punished less than certain and the "
                  "lab, but not Hobbes, multiplies it in, as in the last lesson."),
            ("p", "Hobbes closes with the long list: harm for a fact done before the "
                  "law is hostility, since before the law there is no transgression; "
                  "hurt to the representative is hostility, since only he can "
                  "authorise punishment; harm to a declared enemy is not punishment, "
                  "and a subject who &ldquo;wittingly, and deliberatly deny the authority "
                  "of the Representative&rdquo; suffers as an enemy, at the "
                  "representative's will, which is why rebellion, &ldquo;but warre "
                  "renewed&rdquo;, can lawfully be avenged to the third and fourth "
                  "generation. That last point is the hardest in the chapter, and "
                  "Hobbes does not soften it. The punishment of innocent subjects, by "
                  "contrast, he calls contrary to three laws of nature: that revenge "
                  "look only at a future good, that ingratitude be forbidden and "
                  "that equity be kept."),
            ("p", "Then the kinds of punishment (corporal, pecuniary, ignominy, "
                  "imprisonment, exile) and reward. A pecuniary penalty made to gather "
                  "money is &ldquo;the Price of priviledge, and exemption from the Law&rdquo;, "
                  "unless the law is natural or part of religion. A benefit given to a "
                  "subject because he is feared is not a reward; it is a sacrifice, and "
                  "the sovereign who makes it teaches others to extort. And the chapter "
                  "ends with the name of the book. Punishment and reward are &ldquo;the "
                  "Nerves and Tendons, that move the limbes and joynts of a "
                  "Common-wealth&rdquo;; and Hobbes, having shown the nature of man, whose "
                  "pride compelled him to government, turns to the &ldquo;great power of "
                  "his Governour, whom I compared to Leviathan&rdquo;, from the last two "
                  "verses of Job 41, where God calls that creature King of the Proud. "
                  "Because the governour is mortal, the next chapter goes on to his "
                  "diseases, which the next lesson, <em>The Dissolution of a "
                  "Commonwealth</em>, takes up."),
        ],
        "lab": ("levkit", {
            "mode": "law",
            "view": "deter",
            "preset": "price",
            "presets": [
                {"id": "price", "label": "A crime gaining 100, the law prescribes 60 and 60 is inflicted",
                 "gain": 100, "penalty": 60, "certainty": 1, "prescribed": 60, "inflicted": 60,
                 "expect": {"llwDeters": "no: 60 is less than the gain 100", "llwPrice": "yes: the prescribed 60 is less than the gain 100, rather the price of the crime than a punishment"}},
                {"id": "punishment", "label": "The law prescribes 150 and 150 is inflicted",
                 "gain": 100, "penalty": 150, "certainty": 1, "prescribed": 150, "inflicted": 150,
                 "expect": {"llwDeters": "yes: 150 is more than the gain 100", "llwPrice": "no: the prescribed 150 is not less than the gain 100", "llwHostility": "no: the inflicted 150 is within the prescribed 150"}},
                {"id": "excess", "label": "The law prescribes 150 and 400 is inflicted",
                 "gain": 100, "penalty": 150, "certainty": 1, "prescribed": 150, "inflicted": 400,
                 "expect": {"llwHostility": "yes: the excess, 250, is not punishment but an act of hostility", "llwPrice": "no: the prescribed 150 is not less than the gain 100"}},
            ],
            "panel_title": "Punishment, price or hostility",
            "panel_intro": (
                "The benefit of the crime, the penalty the law prescribed and the penalty "
                "inflicted go in, with the chance of punishment. The lab compares them by "
                "Hobbes's seventh and eighth inferences."
            ),
        }),
        "steps_title": "Sorting a harm by Hobbes's definition",
        "steps_intro": "Four questions, in this order. The first two the lab cannot answer.",
        "steps": [
            ("Was it inflicted by public authority after a public judgement?",
             "If not, it is not a punishment however severe. This is a matter of who "
             "acted and how, and no figure shows it."),
            ("Was there a law made before the act?",
             "Harm for a fact done before the law forbade it is hostility."),
            ("Compare the harm with the benefit",
             "A harm less than the benefit of the crime is the price of it, not a "
             "punishment. State both in the same units."),
            ("Compare what was inflicted with what was prescribed",
             "If more was inflicted than the law named, the excess is hostility. If "
             "nothing was prescribed, whatever is inflicted has the nature of punishment."),
        ],
        "worked": {
            "title": "Three cases, one gain",
            "intro": ["A crime gains 100. Compare what the law prescribed with what was inflicted."],
            "lines": [
                "price:  60 against a gain of 100; 60 < 100, so a price",
                "punishment:  150 against 100; 150 > 100, and 150 = 150",
                "excess:  400 inflicted, 150 prescribed; 400 - 150 = 250 over",
                "hostility is the 250, not the 150",
            ],
            "after": [
                "In the excess case the first 150 is punishment and the rest is hostility. "
                "Hobbes does not say the whole harm turns into hostility, only the "
                "excess.",
            ],
        },
        "quiz_title": "Punishment and its limits",
        "quiz": [
            {"q": "Which of these is a punishment, on Hobbes's definition?",
             "a": ["A private man's revenge for an injury",
                   "An evil inflicted by usurped power",
                   "Sickness that follows an unlawful act",
                   "A sentence of the sovereign's court, after a hearing, for a breach "
                   "of a law made before the act"],
             "c": 3,
             "why": "It is an evil inflicted by public authority after public judgement "
                    "on a transgression of the law. A private revenge is no punishment "
                    "because it does not come from public authority, and harm by usurped "
                    "power is hostility. Hobbes calls the natural hurt of an unlawful "
                    "act a divine punishment but not one among men."},
            {"q": "A crime gains 100 and the law prescribes a penalty of 60, inflicted for "
                  "certain. What does Hobbes's seventh inference call that penalty?",
             "a": ["A punishment, because the law prescribed it",
                   "Rather the price or redemption of the crime",
                   "An act of hostility",
                   "A satisfaction to the injured party"],
             "c": 1,
             "why": "Harm less than the benefit of the crime is &ldquo;rather the Price, or "
                    "Redemption, than the Punishment of a Crime&rdquo;, since it does not "
                    "dispose men to obey. Hostility is the word for excess or for harm "
                    "without authority, and a satisfaction to the injured is a separate "
                    "pecuniary matter in the same chapter."},
            {"q": "The law prescribes 150 and 400 is inflicted. What does Hobbes call the "
                  "part above the prescribed penalty?",
             "a": ["An act of hostility",
                   "A just punishment, since the crime was proved",
                   "The price of the crime",
                   "A grace"],
             "c": 0,
             "why": "Hobbes says &ldquo;the excesse is not Punishment, but an act of hostility&rdquo;, "
                    "because the declared penalty has taken away the terror of a greater "
                    "one, and the unexpected addition is no part of the punishment. "
                    "Where the law named no penalty, whatever is inflicted has the nature "
                    "of punishment, which is not this case."},
            {"q": "A sovereign gives a benefit to a powerful subject because he fears the "
                  "subject's power to hurt. What does Hobbes say it is?",
             "a": ["A salary, by contract",
                   "A grace, to encourage service",
                   "A sacrifice, made to appease the subject",
                   "A punishment, deferred"],
             "c": 2,
             "why": "Such a benefit is &ldquo;not properly Reward&rdquo;: it is not a salary, "
                    "since there is no contract, and not a grace, since fear extorts it. "
                    "Hobbes calls these &ldquo;Sacrifices&rdquo;, and says they encourage "
                    "the continuance of further extortion."},
        ],
        "mistakes": [
            ("Thinking any penalty the law names is a punishment",
             "In the price preset the law names 60, it is inflicted, and it is still "
             "not a punishment, because it is below the gain of 100 and so does not "
             "dispose men to obey. The word the law uses does not decide it; the "
             "relation to the benefit does."),
            ("Thinking the whole harm becomes hostility when it exceeds the law",
             "Hobbes says the excess is not punishment but hostility. In the excess "
             "preset the 150 the law prescribed is punishment and the 250 added after "
             "is hostility."),
            ("Reading <em>hostility</em> as <em>wrong</em>",
             "Hobbes means a harm that is not punishment. Against a declared enemy "
             "&ldquo;all infliction of evill is lawfull&rdquo;. Inflicted on a subject "
             "beyond the law, it falls outside the definition, and the delinquent is "
             "excused from it."),
        ],
        "standard": (
            "Finish when you can sort a harm into punishment, price or hostility.",
            "Given a crime's benefit, the penalty prescribed and the penalty inflicted, "
            "say which part is punishment, which is the price of the crime and which "
            "is hostility, by Hobbes's seventh and eighth inferences."
        ),
        "note": (
            "The lab compares two numbers. Whether a harm was inflicted by public "
            "authority after a public judgement, which Hobbes puts first, no figure shows. "
            "It also cannot decide the disagreement with those who hold, with Kant, that "
            "punishment is for desert and not for effect: it follows the definition as "
            "Hobbes states it."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Leviathan ch. 29, 1651 p. 171; PDF p. 323 of the operator's copy
    {
        "slug": "the-diseases-of-a-commonwealth",
        "title": "The Dissolution of a Commonwealth",
        "module": "Chapter 29 · Of those things that Weaken, or tend to the Dissolution of a Common-wealth",
        "one_line": "Hobbes lists the diseases a commonwealth dies of, and the worst is divided sovereignty, a kingdom divided in itself.",
        "summary": (
            "Chapter 29 treats the commonwealth's mortality as a physician would. Men, not "
            "the matter, are at fault; the diseases are imperfect institution, six seditious "
            "doctrines, imitation of neighbours and of the ancients, divided sovereignty "
            "and the rest. Model two powers that each claim the last word as a game of "
            "chicken and see why a divided sovereignty has no stable peace."
        ),
        "key": [
            "dissolution comes from the makers' fault",
            "six doctrines, among them divided power",
            "two powers, one subject: two commonwealths",
            "chicken: two pure equilibria, one mixed",
            "a sword behind one claim leaves one",
        ],
        "key_label": "Chapter 29 in five lines",
        "concepts_intro": (
            "Chapter 29 is Hobbes the physician. After the foundation, the parts and "
            "the functions of the artificial man, he lists what kills it."
        ),
        "concepts": [
            ("The fault is in the makers",
             "Hobbes says that if men had the use of the reason they pretend to, their "
             "commonwealths might be secured, at least, from perishing by internal "
             "diseases, since they are designed to live as long as mankind or the laws "
             "of nature or justice. When they dissolve from within, the fault is in men as "
             "makers and orderers, who lack the art of making fit laws and the humility "
             "to let their present greatness be trimmed."),
            ("Imperfect institution and false doctrine",
             "The first disease is imperfect institution: a man who takes a kingdom for "
             "less power than peace and defence require will find that resuming it "
             "looks like injustice. The second is a set of six seditious doctrines: that "
             "every private man is judge of good and evil; that whatever a man does against "
             "his conscience is sin; that faith and sanctity come by inspiration; that the "
             "sovereign is subject to the civil laws; that a man's property excludes the "
             "sovereign's right; and that the sovereign power may be divided."),
            ("Divided power",
             "A commonwealth is weakened by imitating neighbours and the ancients, by "
             "a spiritual power set against the civil, by mixed government that is "
             "really three factions, by want of money, monopolies, popular men, great "
             "towns, and the liberty of disputing against absolute power. Hobbes treats "
             "the division of sovereignty as the most dangerous."),
        ],
        "read_title": "The passage first, then the diseases in order",
        "read_intro": (
            "The passage is Hobbes's conclusion about the spiritual power set against "
            "the civil. It states the case on which the lab is built."
        ),
        "body": [
            ("p", "<strong>Chapter 29.</strong> &ldquo;where one is Soveraign, another "
                  "Supreme; where one can make Lawes, and another make Canons; there must "
                  "needs be two Common-wealths, of one &amp; the same Subjects; which is a "
                  "Kingdome divided in it selfe, and cannot stand.&rdquo;"),
            ("p", "Hobbes opens by saying that &ldquo;nothing can be immortall, which "
                  "mortals make&rdquo;, and then adds a hope: the commonwealth could at "
                  "least be spared the diseases that come from within. They come, he says, "
                  "from men as makers and not as matter, who &ldquo;cannot without the "
                  "help of a very able Architect, be compiled, into any other than a "
                  "crasie building&rdquo;. The word <em>architect</em> is the book's "
                  "own ambition. The diseases come in a long list, and he calls them in "
                  "turn the infirmities of a natural body, which is the figure the whole "
                  "book rests on."),
            ("p", "First, imperfect institution, where a man takes a crown with less "
                  "power than peace requires, as the Barons whom William Rufus had "
                  "strengthened to help him to the throne were afterwards supported in "
                  "rebellion by the French, and as Becket was supported by the Pope. It "
                  "is not only monarchy. The style of the ancient Roman commonwealth was "
                  "&ldquo;The Senate, and People of Rome&rdquo;, and neither pretended to "
                  "the whole power, which brought the Gracchi, Marius and Sylla, Pompey "
                  "and Caesar. Second, six seditious doctrines. The fourth, that the "
                  "sovereign is subject to the civil laws, is the one <em>Of Civil Laws</em> "
                  "answers; the sixth is &ldquo;That the Soveraign Power may be "
                  "divided&rdquo;, for what is it, he asks, &ldquo;but to Dissolve "
                  "it? for Powers divided mutually destroy each other&rdquo;."),
            ("p", "Then imitation. The Jews asked Samuel for a king after the manner of "
                  "the nations, the little Greek cities were torn between Spartan and "
                  "Athenian factions, and Hobbes doubts not that many were content to see "
                  "the late troubles in England out of imitation of the Low Countries. And "
                  "reading the Greek and Roman writers on politics, which makes tyrannicide "
                  "look laudable, is compared to the bite of a mad dog, which brings the "
                  "thirst for water together with the horror of it: a monarchy bitten by "
                  "democratical writers, he says, comes to fear being strongly governed, and "
                  "so abhors the strong monarch it most needs."),
            ("p", "Now back to the passage. The quarrel is the one Hobbes had watched "
                  "since the 1640s: the claim of the clergy, whether of Rome or of "
                  "Presbyters, to a supremacy that is not the sovereign's. If the spiritual "
                  "power declares what is sin, he says, it declares by consequence what is "
                  "law, since sin is nothing but transgression of the law; and if the "
                  "civil power declares it too, &ldquo;every Subject must obey two "
                  "Masters, who both will have their Commands be observed as Law; which "
                  "is impossible&rdquo;. Either the civil is subordinate to the ghostly "
                  "and there is no sovereignty but the ghostly, or the ghostly to the "
                  "temporal and there is no supremacy but the temporal. The danger is "
                  "worse than it looks, for the civil authority draws a considerable "
                  "party by being plain, but the spiritual, though it &ldquo;stand in "
                  "the darknesse of Schoole distinctions&rdquo;, cannot want one either, "
                  "&ldquo;because the fear of Darknesse, and Ghosts, is greater than "
                  "other fears&rdquo;."),
            ("p", "The lab turns this into a table. Call the two powers the Crown and "
                  "the Church, each of which may yield or insist on the last word. "
                  "The payoffs are written for the lesson, and Hobbes gives none. If "
                  "both yield they share the field and each does fairly well, 3. If one "
                  "insists and the other yields, the insister gets 5 and the yielder 1. If "
                  "both insist there is civil war, 0 each. That is the game of chicken, and "
                  "the chicken preset shows two pure equilibria, one where the Crown "
                  "insists and the Church yields and one the other way, and a third, "
                  "mixed, in which each insists two times in three. Hobbes's point is "
                  "visible in it: nothing in the table says which equilibrium will occur "
                  "or that the equilibrium will be reached, and at the mixed one civil "
                  "war happens with probability `4/9`, the square of two-thirds."),
            ("p", "Now change the rules. In the sword preset the Church's insisting "
                  "against an insisting Crown costs it 2 and not 0, and the Crown, with a "
                  "sword behind its claim, gets 4 and not 0. Now the Crown's insisting "
                  "dominates: against a yielding Church 5 beats 3, against an insisting "
                  "one 4 beats 1. The Church's best answer to an insisting Crown is to "
                  "yield, 1 against -2. Hobbes's remedy is exactly that, a single "
                  "sovereign whose will no rival may resist, and the table has one "
                  "equilibrium. In the cheap-war preset the opposite: if civil war costs "
                  "little, 2 each against 3 for both yielding, insisting dominates "
                  "for both and the only equilibrium is war, which is worse for both "
                  "than peace. That is a prisoner's dilemma, and it is the lesson's picture, "
                  "not Hobbes's. Of mixed government he says only that its three "
                  "independent factions endanger the commonwealth for want of consent "
                  "to good laws and, most often, for want of money."),
            ("p", "The rest of the chapter is a physician's list: want of money is an "
                  "ague, monopolies a pleurisy, a popular subject a witchcraft, "
                  "great towns and corporations worms in the entrails, the liberty of "
                  "disputing against absolute power the little worms called ascarides. "
                  "He ends with the final dissolution, when an enemy's victory leaves "
                  "no protection and every man may protect himself, and adds that the "
                  "obligation of the members, not the right of a sovereign monarch, is "
                  "what ends. The next lesson, <em>The Office of the Sovereign "
                  "Representative</em>, asks what the sovereign owes the people in "
                  "return."),
        ],
        "lab": ("choicekit", {
            "mode": "game",
            "view": "best",
            "preset": "chicken",
            "presets": [
                {"id": "chicken", "label": "Both yield 3, one insists 5 against 1, both insist 0",
                 "rows": ["Yield", "Insist"], "cols": ["Yield", "Insist"],
                 "payoffs": [[[3, 3], [1, 5]], [[5, 1], [0, 0]]], "expect": {"gaPure": "(Yield, Insist); (Insist, Yield)", "gaMixed": "row Yield: 1/3, col Yield: 1/3"}},
                {"id": "sword", "label": "A sword behind the Crown: if both insist, the Crown gets 4 and the Church -2",
                 "rows": ["Yield", "Insist"], "cols": ["Yield", "Insist"],
                 "payoffs": [[[3, 3], [1, 5]], [[5, 1], [4, -2]]], "expect": {"gaPure": "(Insist, Yield)", "gaDom": "Insist dominates for row"}},
                {"id": "cheap-war", "label": "War costs little: both insisting pays 2 each",
                 "rows": ["Yield", "Insist"], "cols": ["Yield", "Insist"],
                 "payoffs": [[[3, 3], [1, 5]], [[5, 1], [2, 2]]], "expect": {"gaPure": "(Insist, Insist)", "gaDom": "Insist dominates for both", "gaPareto": "(Insist, Insist) is dominated by (Yield, Yield)"}},
            ],
            "panel_title": "Two powers, one subject",
            "panel_intro": (
                "The row player is the Crown and the column player the Church; each "
                "yields or insists on the last word. A tile lists the pure equilibria, "
                "the mixed one, the dominance and the Pareto verdict, all from the "
                "payoffs written here, not from any Hobbesian figure."
            ),
        }),
        "steps_title": "Reading a divided sovereignty as a game",
        "steps_intro": "Five steps, in this order.",
        "steps": [
            ("Name the two powers and their two moves",
             "Each may yield to the other on the last word or insist on its own."),
            ("Write the four outcomes",
             "Say what each power gets if both yield, if one insists, and if both insist. "
             "Hobbes says war is the worst of them, so give it the lowest payoff."),
            ("Mark each power's best reply",
             "For each of the other's moves, find which of its own is better. A cell "
             "where both are best replies is a pure equilibrium."),
            ("Look for dominance",
             "If one move is better against every move of the other, a power will take "
             "it. A power with such a move leaves the other only its best reply."),
            ("Ask what changes the table",
             "A sword behind one claim, or a cheaper war, changes the payoffs. That is "
             "the lesson's version of Hobbes's remedy and of his diagnosis."),
        ],
        "worked": {
            "title": "The mixed equilibrium of chicken",
            "intro": ["Let t be the chance the other power insists. Make a power indifferent."],
            "lines": [
                "yield:  3 · (1 - t) + 1 · t = 3 - 2t",
                "insist:  5 · (1 - t) + 0 · t = 5 - 5t",
                "equal when:  3 - 2t = 5 - 5t, so t = 2/3",
                "both insist, chance:  2/3 · 2/3 = 4/9",
                "each gets, in expectation:  3 - 2 · 2/3 = 5/3",
            ],
            "after": [
                "At the mixed equilibrium each power expects `5/3`, which is below the 3 each "
                "of both yielding. At a pure equilibrium the insister gets 5 and the "
                "yielder 1."
            ],
        },
        "quiz_title": "Chicken and the divided kingdom",
        "quiz": [
            {"q": "In the chicken preset, which cells are pure equilibria?",
             "a": ["Both yield",
                   "Both insist",
                   "The Crown insists and the Church yields, or the reverse",
                   "All four cells"],
             "c": 2,
             "why": "At both-yield each power does better by insisting, 5 against 3. At "
                    "both-insist each does better by yielding, 1 against 0. At either "
                    "cell where one insists and the other yields, neither wants to "
                    "switch: the insister would get 3 instead of 5, and the yielder 0 "
                    "instead of 1."},
            {"q": "In the chicken preset's mixed equilibrium, with what chance does each "
                  "power insist?",
             "a": ["1/3", "2/3", "1/2", "1"],
             "c": 1,
             "why": "Indifference gives `3 - 2t = 5 - 5t`, so `t = 2/3`. One third is the "
                    "chance of yielding. At one half the other power would strictly "
                    "prefer to insist, and at 1 it would strictly prefer to yield."},
            {"q": "What does Hobbes say follows where one power is sovereign and another "
                  "supreme, one makes laws and another canons?",
             "a": ["The two powers will settle into a mixed government",
                   "There must needs be two commonwealths of one and the same subjects, "
                   "a kingdom divided in itself",
                   "The spiritual power will always yield to the civil",
                   "The subject may choose the master he likes"],
             "c": 1,
             "why": "Hobbes's words are that there must needs be &ldquo;two "
                    "Common-wealths, of one &amp; the same Subjects; which is a Kingdome "
                    "divided in it selfe, and cannot stand&rdquo;. He does not predict "
                    "which side yields, only that the kingdom cannot stand."},
            {"q": "In the cheap-war preset, where both insisting pays 2 each, what does "
                  "the lab show?",
             "a": ["Insisting dominates for both, and the equilibrium is worse for both "
                   "than both yielding",
                   "Yielding dominates for both",
                   "There are two pure equilibria, as in chicken",
                   "There is no equilibrium"],
             "c": 0,
             "why": "Insisting beats yielding against either move: 5 against 3, and 2 "
                    "against 1. So both insist, and the 2 each is below the 3 each of both "
                    "yielding. That is a dilemma, a picture the lesson draws and Hobbes "
                    "does not."},
        ],
        "mistakes": [
            ("Thinking Hobbes predicts the table's outcome",
             "The table has several equilibria, and which holds depends on payoffs "
             "written here, not in the text. What the table shares with Hobbes is the "
             "diagnosis: with two independent claimants the peace is unstable."),
            ("Reading the sword preset as a proof that one sovereign is best",
             "The sword preset has one equilibrium because the payoffs were chosen to "
             "give it one. It illustrates Hobbes's remedy and does not argue for it."),
            ("Reading the chapter as one cause of dissolution",
             "Hobbes names many: imperfect institution, six doctrines, imitation, "
             "mixed government, want of money, monopolies, popular men, great towns, "
             "disputation, over-extension and defeat. Divided power is the one the lab "
             "models."),
        ],
        "standard": (
            "Finish when you can read a divided sovereignty as a game.",
            "Given payoffs for two powers that may each yield or insist, find the pure "
            "equilibria, the mixed one and any dominance, and say how a change in one "
            "payoff changes the result."
        ),
        "note": (
            "The payoffs are the lesson's, and Hobbes gives none. Chicken is one way to "
            "write a divided sovereignty, and a repeated game or a game with commitment "
            "would give other answers. The lab shows what follows from the table, on "
            "Hobbes's picture of two claimants, and cannot say whether churches and "
            "crowns behave like the players."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Leviathan ch. 30, 1651 p. 181; PDF p. 334 of the operator's copy
    {
        "slug": "the-office-of-the-sovereign",
        "title": "The Office of the Sovereign Representative",
        "module": "Chapter 30 · Of the Office of the Soveraign Representative",
        "one_line": "The sovereign's office is the safety of the people, and equal taxation means equal charge on what each consumes, not on what each owns.",
        "summary": (
            "Hobbes says the sovereign's duty is the safety of the people, which means all "
            "the contentments of life, to be secured by instruction and good laws. Among "
            "the things he asks is equal justice, and in it equal imposition of taxes on "
            "what men consume and not what they have. Raise a revenue from five people "
            "by each rule and see who pays more."
        ),
        "key": [
            "the office: the safety of the people",
            "teach the rights, and equal justice",
            "equal tax: on what each consumes",
            "rate on riches = revenue / total riches",
            "rate on consumption = revenue / total used",
        ],
        "key_label": "Chapter 30 in five lines",
        "concepts_intro": (
            "Chapter 30 reads as a list of what a sovereign must do, and the list is "
            "long."
        ),
        "concepts": [
            ("Safety, and what it is",
             "The sovereign's office consists in the end for which he was trusted, the "
             "safety of the people, to which he is obliged by the law of nature and for "
             "which he must account to God alone. By safety Hobbes means not bare "
             "preservation but all other contentments of life a man may gain by lawful "
             "industry without hurt to the commonwealth."),
            ("Instruction",
             "A sovereign must keep his essential rights whole and must see the people "
             "taught the grounds of them, because they cannot be maintained by civil law "
             "or fear of punishment alone. The people are to be taught not to love "
             "another government, not to follow popular men, not to dispute the sovereign's "
             "power, to set aside days for instruction, to honour parents and to avoid "
             "injury. Hobbes argues that this depends on the teaching of the universities."),
            ("Equal justice, taxes and good laws",
             "Justice is to be equal to all degrees. Impositions are to be equal, by "
             "what is consumed. The impotent are to be provided for by law and the "
             "strong made to work. Good laws are needful for the good of the people and "
             "perspicuous. Punishments and rewards are to be applied for the good of "
             "the commonwealth, and counsellors are to be chosen for ability."),
        ],
        "read_title": "The passage first, then the office in order",
        "read_intro": (
            "The passage is Hobbes's account of equal taxation, which is the part of "
            "the chapter with a number in it."
        ),
        "body": [
            ("p", "<strong>Chapter 30.</strong> &ldquo;To Equall Justice, appertaineth "
                  "also the Equall imposition of Taxes; the Equality whereof dependeth not "
                  "on the Equality of riches, but on the Equality of the debt, that every "
                  "man oweth to the Common-wealth for his defence.&rdquo;"),
            ("p", "Hobbes begins the chapter by saying what a sovereign is for. His "
                  "office &ldquo;consisteth in the end, for which he was trusted with the "
                  "Soveraign Power, namely the procuration of the safety of the "
                  "people&rdquo;, and he is answerable for it to God and to no one else. "
                  "Then the sentence people forget: by safety, he says, is not meant &ldquo;a bare "
                  "Preservation, but also all other Contentments of life&rdquo; that a man "
                  "gets by lawful industry. Not by care applied to individuals, but by "
                  "&ldquo;a generall Providence&rdquo; of public instruction and good laws. "
                  "That is a great deal more than a night-watchman, though the "
                  "account he gives of it is to God and not to any subject."),
            ("p", "Most of the chapter is instruction. The sovereign must not give up "
                  "any of the essential rights of Chapter 18, nor let his people be "
                  "ignorant of their grounds. To those who say the people are not capable, "
                  "Hobbes answers that the people are &ldquo;like clean paper&rdquo; "
                  "unless tainted by the dependence on the potent or the opinions of "
                  "their doctors, and that if whole nations were brought to believe the "
                  "mysteries of the church, they can be taught the plainer duties of "
                  "subjects. He takes the Ten Commandments as the outline of the teaching "
                  "and then turns on the universities, which until late in Henry VIII's "
                  "reign upheld the pope against the commonwealth. Whether he will teach "
                  "the universities he declines to say: &ldquo;any man that sees what I am "
                  "doing, may easily perceive what I think.&rdquo;"),
            ("p", "Then equal justice. The great should have &ldquo;no greater hope of "
                  "impunity&rdquo; than the meaner sort, because &ldquo;Impunity maketh "
                  "Insolence; Insolence Hatred&rdquo;. And so to the passage: equality of "
                  "taxes depends not on the equality of riches but on the equality of "
                  "the debt every man owes for his defence. The impositions are &ldquo;the "
                  "Wages, due to them that hold the publique Sword&rdquo;, and each man "
                  "has the same protection from the commonwealth, so the debt is the "
                  "same, &ldquo;saving that the rich, who have the service of the poor, "
                  "may be debtors not onely for their own persons, but for many "
                  "more&rdquo;. From which he concludes that equality of imposition "
                  "consists rather in the equality of what is consumed. Why should he who "
                  "labours much, and sparing the fruits of his labour consumes little, be "
                  "charged more than the man who lives idly, gets little and spends all "
                  "he gets, when the one has no more protection than the other?"),
            ("p", "The lab does the sum. Five people, a sample written for the lesson, "
                  "have riches and consumption: the frugal 500 and 50, the idle 100 and "
                  "100, the lord 1,000 and 200 (he keeps a household), the poor 60 and 60, "
                  "the merchant 340 and 90. Total riches are 2,000 and total consumption "
                  "500. In the sample preset the revenue is 100: a rate on riches of "
                  "`1/20`, 5 per cent, charges the frugal 25 and the idle 5; a rate on "
                  "consumption of `1/5`, 20 per cent, charges the frugal 10 and the idle "
                  "20. The idle, the poor and the merchant pay more under the tax "
                  "on consumption, and the frugal and the lord pay less. In the war preset "
                  "the revenue doubles to 200 and so does every tax; the proportions "
                  "do not change. In the pair preset the labourer, with riches 180 and "
                  "consumption 20, and the idler, with 20 and 30, raise a revenue of "
                  "20: on riches the labourer pays 18 and the idler 2, on consumption "
                  "8 and 12. The man who spares pays less, which is Hobbes's pair."),
            ("p", "The standard objection is also in the figures. The poor man, with "
                  "60 and 60, spends everything he has, so a tax on consumption is a "
                  "charge on all he has: 12 of his 60, against 3 under a rate on riches. "
                  "Later writers made ability to pay the test, and a tax on "
                  "consumption can fall hardest on those who consume the largest share of what "
                  "they have. Hobbes's answer, in his own terms, is that the "
                  "tax is a wage for protection, and protection is of life, which is "
                  "equally dear to rich and poor. Whether protection is what taxes buy, "
                  "or what a fair tax should be measured by, is what the lab leaves open."),
            ("p", "The chapter goes on to public charity (the impotent are to be provided "
                  "for by law and not left to uncertain charity), the compulsion of the "
                  "idle and the planting of colonies, and to good laws. &ldquo;By a Good "
                  "Law, I mean not a Just Law: for no Law can be Unjust.&rdquo; A good "
                  "law is &ldquo;Needfull, for the Good of the People, and withall "
                  "Perspicuous&rdquo;, as hedges are set, he says, not to stop travellers "
                  "but to keep them in the way. Punishments are to be severe against "
                  "crimes most dangerous to the public, and lenient to the seduced; rewards "
                  "are for service and never bought from popular men; and counsellors are "
                  "chosen for knowledge, heard apart, and not by birth. The last chapter "
                  "of the course, <em>The Kingdom of God by Nature</em>, closes Part "
                  "II by asking by what right God himself rules."),
        ],
        "lab": ("levkit", {
            "mode": "tax",
            "view": "impose",
            "preset": "sample",
            "presets": [
                {"id": "sample", "label": "Five people, a revenue of 100",
                 "persons": [["frugal", 500, 50], ["idle", 100, 100], ["lord", 1000, 200],
                             ["poor", 60, 60], ["merchant", 340, 90]],
                 "revenue": 100, "expect": {"ltxRateRiches": "1/20 = 5%", "ltxRateConsumption": "1/5 = 20%", "ltxOnRiches": "frugal 25; idle 5; lord 50; poor 3; merchant 17", "ltxOnConsumption": "frugal 10; idle 20; lord 40; poor 12; merchant 18", "ltxMore": "3: idle, poor, merchant"}},
                {"id": "war", "label": "The same five people, a revenue of 200",
                 "persons": [["frugal", 500, 50], ["idle", 100, 100], ["lord", 1000, 200],
                             ["poor", 60, 60], ["merchant", 340, 90]],
                 "revenue": 200, "expect": {"ltxRateRiches": "1/10 = 10%", "ltxRateConsumption": "2/5 = 40%", "ltxOnConsumption": "frugal 20; idle 40; lord 80; poor 24; merchant 36"}},
                {"id": "pair", "label": "A labourer and an idler, a revenue of 20",
                 "persons": [["labourer", 180, 20], ["idler", 20, 30]],
                 "revenue": 20, "expect": {"ltxOnRiches": "labourer 18; idler 2", "ltxOnConsumption": "labourer 8; idler 12", "ltxMore": "1: idler"}},
            ],
            "panel_title": "Raise a revenue two ways",
            "panel_intro": (
                "Each person's riches and consumption go in, with the revenue to be raised. "
                "The lab finds the rate that raises it on riches and the rate that raises "
                "it on consumption, and each person's tax under each."
            ),
        }),
        "steps_title": "Raising a revenue by two rules",
        "steps_intro": "Four steps, for any list of persons.",
        "steps": [
            ("Add the bases",
             "Total the riches and total the consumption of everyone charged."),
            ("Find each rate",
             "Divide the revenue by the total riches for the rate on riches, and by the "
             "total consumption for the rate on consumption."),
            ("Charge each person",
             "A person's tax is the rate times his own riches, or times his own "
             "consumption."),
            ("Compare the two lists",
             "Subtract the first from the second for each person. Whoever has a positive "
             "difference pays more under the tax on consumption."),
        ],
        "worked": {
            "title": "Five people, a revenue of 100",
            "intro": ["The sample preset, with the idle man's tax found both ways."],
            "lines": [
                "riches:  500 + 100 + 1000 + 60 + 340 = 2000",
                "consumption:  50 + 100 + 200 + 60 + 90 = 500",
                "rate on riches:  100 / 2000 = 1/20",
                "rate on consumption:  100 / 500 = 1/5",
                "idle on riches:  100 · 1/20 = 5",
                "idle on consumption:  100 · 1/5 = 20",
            ],
            "after": [
                "The idle man pays 15 more under a tax on consumption, and the frugal "
                "man 15 less. Each list adds to 100 because every share is exact.",
            ],
        },
        "quiz_title": "Equal taxes and a good law",
        "quiz": [
            {"q": "On what does Hobbes say the equality of imposition consist?",
             "a": ["The equality of riches",
                   "The equality of what is consumed",
                   "The equality of the services each has rendered",
                   "The equality of the land each holds"],
             "c": 1,
             "why": "He says it &ldquo;consisteth rather in the Equality of that which is "
                    "consumed, that of the riches of the persons that consume the "
                    "same&rdquo;, since each has the same protection and so owes the same "
                    "debt. The first answer is the rule he rejects."},
            {"q": "In the sample preset, the idle man (riches 100, consumption 100) pays "
                  "5 on a rate on riches. What does he pay on a rate on consumption?",
             "a": ["5", "10", "20", "40"],
             "c": 2,
             "why": "The rate on consumption is `100/500 = 1/5`, and `100 · 1/5 = 20`. "
                    "Five is his tax on riches. Forty is the lord's tax on consumption "
                    "and ten the frugal man's."},
            {"q": "In the pair preset, how much does the labourer (riches 180, "
                  "consumption 20) pay on a rate on consumption?",
             "a": ["18", "2", "12", "8"],
             "c": 3,
             "why": "The consumption total is 50, so the rate is `2/5`, and "
                    "`20 · 2/5 = 8`. Eighteen is his tax on riches; 2 and 12 are the idler's "
                    "taxes on riches and consumption."},
            {"q": "What does Hobbes mean by a Good Law?",
             "a": ["One that is just",
                   "One that is needful for the good of the people and perspicuous",
                   "One that benefits the sovereign",
                   "One that forbids voluntary actions that harm a man's own interest"],
             "c": 1,
             "why": "He says &ldquo;A good Law is that, which is Needfull, for the Good of "
                    "the People, and withall Perspicuous&rdquo;, and that he does not mean a "
                    "just law, since no law can be unjust. He rejects the law that "
                    "serves the sovereign alone, since their good cannot be separated, "
                    "and the law that binds from all voluntary actions."},
        ],
        "mistakes": [
            ("Thinking an equal tax means an equal sum from everyone",
             "Hobbes's equal tax is one rate on what each consumes. The lord, who "
             "keeps a household, pays four times what the frugal man does on "
             "consumption of 200 and 50, and Hobbes says the rich may be debtors for "
             "many more than themselves."),
            ("Thinking a tax on consumption always charges the rich more",
             "In the sample preset the lord pays 50 on riches and 40 on consumption, "
             "and the idle man and the poor man pay more under consumption. Who pays "
             "more depends on how much of what each has he spends."),
            ("Reading the office as only the sovereign's convenience",
             "Hobbes says the safety of the people means all the contentments of "
             "life a man may gain by lawful industry, and that the sovereign must "
             "account for it to God. The lab's taxes say nothing about it."),
        ],
        "standard": (
            "Finish when you can raise a revenue by each rule.",
            "Given each person's riches and consumption and a revenue, compute the rate "
            "on riches, the rate on consumption and each person's tax under each, and "
            "say who pays more under the tax Hobbes recommends."
        ),
        "note": (
            "The five people and their figures are written for this lesson, and Hobbes "
            "gives none. The lab computes what each rule charges and cannot say which "
            "rule is fairer: that depends on whether taxes are wages for protection, as "
            "Hobbes says, or are to be set by ability to pay, as his critics hold."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Leviathan ch. 31, 1651 p. 187; PDF p. 342 of the operator's copy
    {
        "slug": "the-kingdom-of-god-by-nature",
        "title": "The Kingdom of God by Nature",
        "module": "Chapter 31 · Of the Kingdome of God by Nature",
        "one_line": "God reigns over men by nature because his power is irresistible, not because he made them or is good, and this closes Part II.",
        "summary": (
            "Chapter 31 turns from the commonwealth to the kingdom of God, and derives God's "
            "right to rule from his irresistible power and not from creation or "
            "goodness. Write the argument as premises, check that it is valid, and see which "
            "premise a reader who grounds the right in creation would deny."
        ),
        "key": [
            "a kingdom is rule by word, reward, penalty",
            "God's right comes from irresistible power",
            "not from creating men, nor from goodness",
            "Job is answered by power, not by sin",
            "valid, so the dispute is over the premises",
        ],
        "key_label": "Chapter 31 in five lines",
        "concepts_intro": (
            "Chapter 31 closes Part II and opens the way to Part III. It asks what the "
            "laws of God are, so that a subject knows when the commonwealth commands "
            "against them."
        ),
        "concepts": [
            ("Why the question is needed",
             "Hobbes says he has proved that subjects owe simple obedience in all "
             "things not repugnant to the laws of God. What is left, for the entire "
             "knowledge of civil duty, is to know what those laws are, else a man "
             "offends God by too much civil obedience or the commonwealth through fear "
             "of offending God."),
            ("The natural kingdom and its right",
             "A kingdom is properly one in which a ruler governs subjects by his word, with "
             "promise of rewards and threat of punishment. God declares his laws in "
             "three ways: by natural reason, by revelation and by the voice of a prophet "
             "whom he gives credit by miracles. So he has a natural kingdom and a "
             "prophetic one. Hobbes says the right of nature by which God reigns "
             "derives from his irresistible power."),
            ("Honour, worship and natural punishment",
             "Honour is the opinion of another's power and goodness, and worship its outward "
             "signs. Hobbes lists the attributes it is honour to give God (existence, "
             "infinity, incomprehensibility), says disputing his nature dishonours "
             "him, and holds that obedience to his laws is the greatest worship. Public "
             "worship is the commonwealth's, and uniform."),
        ],
        "read_title": "The passage first, then the argument as premises",
        "read_intro": (
            "The passage states the central claim of the chapter. The reasoning behind "
            "it is a few lines later, and the lab sets it out."
        ),
        "body": [
            ("p", "<strong>Chapter 31.</strong> &ldquo;The Right of Nature, whereby God "
                  "reigneth over men, and punisheth those that break his Lawes, is to be "
                  "derived, not from his Creating them as if he required obedience, as of "
                  "Gratitude for his benefits; but from his Irresistible Power.&rdquo;"),
            ("p", "Think of the ways you might say a ruler has a right to rule. Because "
                  "he made us, as a father; because he is good, as a benefactor; because "
                  "we agreed to it, as a contract; or because nothing could stop him. "
                  "Hobbes has spent much of the book on the third for human rulers. For "
                  "God, he takes the fourth, and the reason is in the text. Having "
                  "shown &ldquo;how the Soveraign Right ariseth from Pact&rdquo;, he "
                  "says, to show how it may arise from nature &ldquo;requires no more, but "
                  "to shew in what case it is never taken away&rdquo;."),
            ("p", "Here is the case, step by step. By nature all men had a right to "
                  "everything, so each had a right to reign over all the rest. But "
                  "this &ldquo;Right could not be obtained by force&rdquo;, so for the "
                  "safety of every one they laid it down and set up sovereigns by "
                  "consent. &ldquo;whereas if there had been any man of Power Irresistible; "
                  "there had been no reason, why he should not by that Power have ruled&rdquo;. "
                  "So, to whoever's power is irresistible &ldquo;the dominion of all men "
                  "adhaereth naturally by their excellence of Power&rdquo;. God's is, so "
                  "the kingdom belongs to him &ldquo;not as Creator, and Gracious; but as "
                  "Omnipotent&rdquo;."),
            ("p", "The lab writes this with two letters. Let p be: God's power over men is "
                  "irresistible. Let q be: God has the right to reign over men and to "
                  "afflict them at his pleasure. The conditional `p → q` carries the "
                  "reasoning of the last paragraph, the claim that a being with irresistible "
                  "power has no reason to lay down his natural right, and so keeps it. In "
                  "the power preset, with `p` and `p → q`, the conclusion `q` has four "
                  "rows and no counterexample, so the argument is valid. In the strip "
                  "preset the conditional is removed: `p` alone has one counterexample, "
                  "where `p` is true and `q` false, so the conditional is doing the "
                  "work."),
            ("p", "Now the rival. Let c be: God created men. The argument of the "
                  "creation preset, `c` and `c → q`, is equally valid: if creating "
                  "gives a right to rule and God created us, then he has it. Validity "
                  "does not choose between them. Each has a premise to be defended, "
                  "and Hobbes denies the conditional `c → q`: God does not rule because he "
                  "required obedience as gratitude for his benefits. A reader who grounds "
                  "the right in creation or in goodness, as many of Hobbes's readers did, "
                  "will grant `p` and deny `p → q`, holding that irresistible power by itself "
                  "gives no right, only a fact. That reader's case, God with the power and without the "
                  "right, is the strip preset's row, `p` true and `q` false. The mixed "
                  "preset shows the other half of the reader's view: power joined only "
                  "to the creation link, `p` and `c → q`, does not yield `q`. Its one "
                  "counterexample has `c` false, so on that view the power does no work "
                  "and the right rests on creation."),
            ("p", "Hobbes also has the text on his side, which is why the chapter "
                  "carries the example of Job. Job's friends argued from his affliction to "
                  "his sin, and Job defended himself by his innocence. God settled it "
                  "&ldquo;not by arguments derived from Job's Sinne, but his own "
                  "Power&rdquo;, saying &ldquo;Where wast thou when I layd the foundations "
                  "of the earth&rdquo;, and approved Job's innocence while reproving his "
                  "friends' doctrine. The right of afflicting, Hobbes concludes, is not "
                  "always derived from men's sin, but from God's power. Whether that is a "
                  "right in the sense a human sovereign has one, or only an answer to "
                  "the question why good men suffer, the lab leaves to the reader."),
            ("p", "The rest of the chapter works out the consequences. Subjects of "
                  "God's kingdom are only those who believe that God governs, has given "
                  "precepts and propounds rewards and punishments; &ldquo;all the rest, are "
                  "to be understood as Enemies&rdquo;. The laws he gives by natural reason "
                  "are those of Chapters 14 and 15, and the rest concern honour. Hobbes "
                  "lists what it dishonours God to say: that he is finite, has "
                  "parts, is in a place, or that there are many gods. To dispute "
                  "his nature is to dishonour him, for &ldquo;we are not to consider "
                  "the signification of Philosophicall Truth; but the signification of "
                  "Pious Intention&rdquo;. A commonwealth, being one person, owes God "
                  "one worship, which is why public worship is uniform, and what the "
                  "sovereign ordains as signs of honour, among actions indifferent by "
                  "nature, private men must take as such, "
                  "so that &ldquo;It is better to obey God than men&rdquo; has its place "
                  "in the kingdom of God by pact, not by nature."),
            ("p", "Part II ends on a note of doubt and hope. Hobbes is &ldquo;at the point "
                  "of believing this my labour, as uselesse, as the Common-wealth of "
                  "Plato&rdquo;, who held that the troubles of states end only when "
                  "sovereigns are philosophers. But the science of natural justice "
                  "is the only science necessary to sovereigns, and he recovers some "
                  "hope that the writing may fall into the hands of a sovereign who "
                  "will, without any interested interpreter, convert &ldquo;this Truth "
                  "of Speculation, into the Utility of Practice&rdquo;. The next course, "
                  "<em>Of a Christian Commonwealth</em>, begins Part III with the "
                  "question this chapter has left open: what the supernatural word of "
                  "God, in Scripture and the prophets, adds to natural reason."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "preset": "power",
            "show": "all",
            "presets": [
                {"id": "power", "label": "p and p → q, so q",
                 "premises": ["p", "p -> q"], "conclusion": "q", "expect": {"vaRows": "4", "vaCounter": "0", "vaVerdict": "Valid", "vaForm": "modus ponens"}},
                {"id": "creation", "label": "c and c → q, so q",
                 "premises": ["c", "c -> q"], "conclusion": "q", "expect": {"vaRows": "4", "vaCounter": "0", "vaVerdict": "Valid"}},
                {"id": "mixed", "label": "p and c → q, so q",
                 "premises": ["p", "c -> q"], "conclusion": "q", "expect": {"vaRows": "8", "vaCounter": "1", "vaVerdict": "Invalid"}},
                {"id": "strip", "label": "p alone, so q",
                 "premises": ["p"], "conclusion": "q", "expect": {"vaRows": "4", "vaCounter": "1", "vaVerdict": "Invalid"}},
            ],
            "panel_title": "What follows from the ground of God's right",
            "panel_intro": (
                "Each row is a case: a true or false for every letter. A row is "
                "highlighted when every premise is true and the conclusion false. The "
                "lab tests the form only; whether the premises are true is what Hobbes "
                "and his critics dispute."
            ),
        }),
        "steps_title": "Testing a ground of right",
        "steps_intro": "Four steps, for any argument of the form: this is why he has the right.",
        "steps": [
            ("State the ground and the right",
             "Write the ground (irresistible power, creation, goodness) as one sentence "
             "and the right it is said to give as another."),
            ("Write the link as a conditional",
             "The link says that whoever has the ground has the right. This is the "
             "premise the dispute is about."),
            ("Check the form",
             "Run the ground, the link and the right through the checker. The "
             "argument from any ground, with its link, will be valid."),
            ("Test the link, not the form",
             "Ask whether the link is true of rulers generally. The checker is silent on "
             "that, so the answer comes from arguments about rule, not from logic."),
        ],
        "worked": {
            "title": "The mixed case, row by row",
            "intro": ["Premises p and c → q; conclusion q. Look for a row with both premises true."],
            "lines": [
                "p true, c true, q true:  q true, no counterexample",
                "p true, c true, q false:  c → q false, no counterexample",
                "p true, c false, q false:  c → q true, p true, q false: counterexample",
                "p true, c false, q true:  q true, no counterexample",
                "p false, any:  p false, no counterexample",
            ],
            "after": [
                "One row breaks it: `p` true, `c` false, `q` false. With only the creation "
                "link, power proves nothing unless creation is granted too. The creation "
                "reader's objection to Hobbes, power without right, is the strip preset's "
                "row.",
            ],
        },
        "quiz_title": "From power to right",
        "quiz": [
            {"q": "On what does Hobbes derive God's right to reign over men by nature?",
             "a": ["From his creating them",
                   "From his goodness to them",
                   "From their gratitude for his benefits",
                   "From his irresistible power"],
             "c": 3,
             "why": "He says it is derived &ldquo;not from his Creating them as if he "
                    "required obedience, as of Gratitude for his benefits; but from his "
                    "Irresistible Power&rdquo;, and later &ldquo;not as Creator, and "
                    "Gracious; but as Omnipotent&rdquo;."},
            {"q": "In the strip preset, p alone is offered for q. What does the lab find?",
             "a": ["Valid, since q is true whenever p is",
                   "Valid, since p is a tautology",
                   "Invalid, with a counterexample where p is true and q false",
                   "Invalid, with no counterexample"],
             "c": 2,
             "why": "With no link between p and q there is a row in which `p` is true and "
                    "`q` is false, and that row is the counterexample. Nothing makes q true "
                    "whenever p is, and an invalid argument always has a counterexample."},
            {"q": "How does Hobbes say God answered Job?",
             "a": ["By justifying the affliction from his own power, and approving Job's "
                   "innocence",
                   "By pointing to Job's secret sin",
                   "By promising that the wicked would be punished in this life",
                   "By telling Job that his friends were right"],
             "c": 0,
             "why": "&ldquo;God himselfe taketh up the matter, and having justified the "
                    "Affliction by arguments drawn from his Power&rdquo; both approved Job's "
                    "innocence and reproved the doctrine of his friends. The friends are "
                    "the ones who argued from affliction to sin."},
            {"q": "Whom does Hobbes say are subjects of the natural kingdom of God?",
             "a": ["Every creature, since all are subject to his power",
                   "Those who believe there is a God who governs, has given precepts "
                   "and propounds rewards and punishments",
                   "Only the Jews",
                   "Only those who have heard a prophet"],
             "c": 1,
             "why": "A kingdom is properly rule by word with reward and punishment, so "
                    "bodies inanimate and creatures irrational are not subjects, and "
                    "neither are atheists: &ldquo;all the rest, are to be understood as "
                    "Enemies&rdquo;. The Jews are the subjects of the prophetic kingdom."},
        ],
        "mistakes": [
            ("Thinking a valid argument shows God's right comes from power",
             "The creation preset is equally valid. Validity shows that each ground "
             "yields its conclusion when its link is granted, and the dispute is over "
             "the link, which the lab does not test."),
            ("Reading Hobbes as saying God is not good",
             "He says goodness is not the ground of God's right. He still says "
             "honour consists in the opinion of God's power and goodness, and that "
             "&ldquo;Good, Just, Liberall&rdquo; are natural signs of honour."),
            ("Taking Job as a proof of Hobbes's whole claim",
             "Hobbes cites Job to show that God justified the affliction from his "
             "power and not from Job's sin. A critic may say that only shows why good "
             "men suffer. It does not show that power is the source of a right to rule."),
        ],
        "standard": (
            "Finish when you can set out the argument and say which premise decides it.",
            "Write Hobbes's argument for God's right to reign by nature as premises, "
            "test it, and say which premise a reader who grounds the right in creation "
            "or goodness would deny."
        ),
        "note": (
            "The lab tests the form of an argument whose premises are about God. It "
            "shows that from irresistible power and the link the right follows, and that "
            "from creation and its link the right follows, and it cannot say which "
            "link is true. Whether power gives a right is a question of moral "
            "philosophy and of theology that the book argues and the lab cannot settle."
        ),
    },
]
