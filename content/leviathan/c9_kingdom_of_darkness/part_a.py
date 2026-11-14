"""The Kingdom of Darkness, and the Review and Conclusion: five lessons.

Every quotation is from the operator's copy of the 1651 text (Tuck's edition,
which keeps Hobbes's spelling); the comment beside each lesson gives the
chapter, the 1651 page and the PDF page. Italics are dropped, a long s is
printed as s, and nothing else is changed. LESSONS holds the lesson that uses
argkit; LEVKIT_LESSONS holds the four that use levkit, joined in __init__.
"""


def _reckon(presets):
    """levkit/reckon presets written as records of names, shipped as the text the
    kit's boxes hold: 'name, parts; name, parts'."""
    out = []
    for p in presets:
        q = dict(p)
        q["defs"] = "; ".join("%s, %s" % (d["name"], d["parts"]) for d in p["defs"])
        q["opposed"] = "; ".join("%s, %s" % (o["a"], o["b"]) for o in p["opposed"])
        q["claims"] = "; ".join("%s, %s, %s" % (c["claim"], c["subject"], c["predicate"])
                                for c in p["claims"])
        out.append(q)
    return out

def _benefit(presets):
    """levkit/canon benefit presets: doctrines as 'doctrine, parties; ...'."""
    out = []
    for p in presets:
        q = dict(p)
        q["doctrines"] = "; ".join("%s, %s" % (d["doctrine"], d["benefits"]) for d in p["doctrines"])
        out.append(q)
    return out


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Leviathan ch. 44, 1651 pp. 333-334; PDF pp. 513-514 of the operator's copy
    # (the opening quotation); ch. 44, 1651 p. 335, PDF p. 515 (the main abuse).
    {
        "slug": "spiritual-darkness",
        "title": "Spiritual Darkness from Misinterpretation of Scripture",
        "module": "Chapter 44 · Of Spirituall Darknesse from Misinterpretation of Scripture",
        "one_line": "Hobbes calls the kingdom of darkness a confederacy of deceivers, and says its chief error is to take the present church for the kingdom of God.",
        "summary": (
            "Part IV opens with a kingdom nobody can see, and Hobbes means it politically: "
            "men who want dominion over other men and get it by false doctrine. Set out his "
            "argument that the present church is not the kingdom of God as three premises and a "
            "conclusion, test it for validity, and find the one premise that does all the work "
            "and that his Catholic and Presbyterian opponents would not grant."
        ),
        "key": [
            "k: the present church is God's kingdom",
            "k → c: then the kingdom has come",
            "c → s: it comes with the second coming",
            "no second coming, so no c, so not k",
            "drop c → s and the argument fails",
        ],
        "key_label": "The chapter's chief argument in five lines",
        "concepts_intro": (
            "Chapter 44 begins the last Part of the book. Three ideas carry the first "
            "chapter of it."
        ),
        "concepts": [
            ("The kingdom of darkness",
             "Hobbes reads the Scripture's rulers of the darkness of this world, Satan and "
             "Beelzebub, prince of the phantasms of the air, as an allegory with a "
             "meaning here and now. The kingdom of darkness is a confederacy of deceivers who "
             "use dark and erroneous doctrines to win dominion over men, and so put out the "
             "light of nature and of the Gospel."),
            ("The kingdom of God, strictly taken",
             "On Hobbes's account in Chapter 35, God's kingdom by pact was instituted by "
             "Moses over the Jews alone and ended when they asked Samuel for a king like the "
             "other nations. Since then God reigns over all creatures by his power, but he has "
             "no kingdom by pact until Christ comes again. Meanwhile Christians are in the "
             "kingdom of grace, which is a promise, and their only kings are their civil "
             "sovereigns."),
            ("Consecration and conjuration",
             "To consecrate is to set a person or thing apart from common use for God, which "
             "changes the use and not the nature of the thing. Words that pretend to change "
             "its nature are, on Hobbes's reckoning, an incantation. The same chapter "
             "treats eternal life as a gift of grace to the faithful and not a property of "
             "every soul."),
        ],
        "read_title": "The passage first, then the chapter's argument",
        "read_intro": (
            "The passage defines the kingdom of darkness. The lesson goes back to why Hobbes "
            "adds a fourth Part, reads his case against the present church as the kingdom of "
            "God, tests it in the lab, and then reads the other two errors he names."
        ),
        "body": [
            ("p", "<strong>Chapter 44.</strong> &ldquo;This considered, the Kingdome of "
                  "Darknesse, as it is set forth in these, and other places of the Scripture, "
                  "is nothing else but a Confederacy of Deceivers, that to obtain dominion "
                  "over men in this present world, endeavour by dark, and erroneous Doctrines, "
                  "to extinguish in them the Light, both of Nature, and of the Gospell; and so "
                  "to dis-prepare them for the Kingdome of God to come.&rdquo;"),
            ("p", "Three Parts of the book have gone to building a commonwealth with one "
                  "sovereign, and then to showing, from Scripture, that a Christian "
                  "commonwealth is no different. You might think the work is finished. It is not, "
                  "because there is a claim abroad that makes two sovereigns of one, and in the "
                  "England of 1651, after a civil war fought partly over bishops and "
                  "presbyters, you did not have to look far for it. Hobbes wrote the book in "
                  "exile in Paris. When he asks why Christendom has had, &ldquo;almost from "
                  "the time of the Apostles&rdquo;, so much jostling by foreign and civil war, "
                  "his answer is that it is &ldquo;Night amongst us, or at least a "
                  "Mist&rdquo;, and that &ldquo;wee are therefore yet in the Dark&rdquo;."),
            ("p", "Notice what the darkness is made of. Scripture speaks of Satan as prince of "
                  "the power of the air and of Beelzebub as prince of demons, which Hobbes takes "
                  "to mean prince of phantasms, the appearances that fill the air. The "
                  "children of darkness, the demons and the spirits of illusion, he says, "
                  "&ldquo;signifie allegorically the same thing&rdquo;. So the kingdom is not "
                  "a place. It is people, and what they want is dominion. He says the "
                  "enemy has been at work in four ways, sowing tares in &ldquo;the Night of "
                  "our naturall Ignorance&rdquo;: by abusing the Scriptures, by bringing in "
                  "the demonology of the heathen poets, by mixing in the vain philosophy of the "
                  "Greeks, Aristotle above all, and by false or uncertain traditions and "
                  "feigned history. Chapter 44 takes the first. The next two lessons take the "
                  "second and third, and the fourth lesson takes up who gained by all four."),
            ("p", "The first abuse comes with a claim that Hobbes ranks above the rest. "
                  "&ldquo;The greatest, and main abuse of Scripture, and to which almost all "
                  "the rest are either consequent, or subservient,&rdquo; he writes, &ldquo;is "
                  "the wresting of it, to prove that the Kingdome of God, mentioned so often "
                  "in the Scripture, is the present Church&rdquo;. His reply has three steps, "
                  "all on one page. The kingdom of God &ldquo;was first instituted by the "
                  "Ministery of Moses, over the Jews onely&rdquo; and ended when they chose "
                  "Saul. Since then God has been king only as he always was, of all creatures "
                  "&ldquo;by his infinite Power&rdquo;. And God promised through the prophets "
                  "to restore his government, and to send his Son. Then comes the sentence the "
                  "lab is built on: &ldquo;Which second coming not yet being, the Kingdome of "
                  "God is not yet come, and wee are not now under any other Kings by Pact, but "
                  "our Civill Soveraigns&rdquo;."),
            ("p", "That is an argument, so write it as one. Let k be the claim under test, that "
                  "the present church is the kingdom of God. Let c be that the kingdom of God "
                  "has come, and s that Christ's second coming has happened. If the church is "
                  "the kingdom, the kingdom has come: k → c. The kingdom comes only with the "
                  "second coming: c → s. And the second coming has not happened: ¬s, read "
                  "<em>not s</em>. From those three, not k. The lab's <em>hobbes</em> "
                  "preset tests exactly this. It is valid: of the eight rows of truth values "
                  "for k, c and s, only one makes all three premises true, the row where all "
                  "three letters are false, and there the conclusion is true. There is no "
                  "counterexample."),
            ("p", "Validity is cheap, though, so ask which premise earns it. Take away c → s "
                  "and run the <em>no-link</em> preset, with only k → c and ¬s. The "
                  "argument is now invalid, and the lab finds the row: the church is the "
                  "kingdom, the kingdom has come, and the second coming has not. Nothing in "
                  "those two premises rules it out. Take away k → c instead, in "
                  "<em>no-bridge</em>, and it fails again, with one counterexample: the "
                  "kingdom has not come, and the church is the kingdom anyway. Each premise is "
                  "needed. But k → c is hardly in dispute, since it only says that a kingdom "
                  "that is present has come. The premise that does the work is the middle "
                  "one, and it is the one Hobbes's opponents deny."),
            ("p", "Who were they? Cardinal Robert Bellarmine, the Jesuit whose texts for the "
                  "present kingdom of God, administered by the pope, Hobbes says he has "
                  "already answered, held that Christ's kingdom is the church now on "
                  "earth. Theodore Beza, who followed Calvin "
                  "at Geneva, read Christ's words in Mark 9 about some who would not taste "
                  "death before they saw the kingdom of God come with power as saying that it "
                  "began at the Resurrection. Hobbes does not say what Beza meant it to "
                  "entitle: whether the Presbytery of Geneva to supreme ecclesiastical power, "
                  "or princes. He observes that the Presbytery has claimed power to "
                  "excommunicate its own kings, &ldquo;no lesse than the Pope challengeth it "
                  "universally&rdquo;. Both deny c → s, and for both the church's present "
                  "authority is what hangs on denying it."),
            ("p", "Hobbes answers Beza from the Gospels. Before the Ascension the apostles ask "
                  "&ldquo;Wilt thou at this time restore again the Kingdome to Israel&rdquo;, "
                  "and are told that it is not for them to know the times. St. Paul says "
                  "Christians were to wait for the Son from heaven, and Christians pray "
                  "&ldquo;Let thy Kingdome Come&rdquo;, which would be pointless if the "
                  "kingdom were already here. The words in Mark he reads, with some hesitation, "
                  "as fulfilled in the Transfiguration, a vision. That is the weak point a "
                  "critic would press: all of it depends on taking <em>kingdom</em> as a "
                  "kingdom in the ordinary sense, with a king and a time of beginning. If "
                  "Christ's kingdom is a spiritual rule over the faithful, as Bellarmine and "
                  "Beza each in their own way held, then c → s is not obviously true and the "
                  "lab cannot decide between them."),
            ("p", "Hobbes then lists what follows from the error. Someone must speak for Christ, "
                  "now in heaven, and the pope claims to. A Christian king must be crowned by a "
                  "bishop. The Fourth Lateran Council under Innocent III, as Hobbes reports "
                  "it, released the subjects of a king from obedience if he would not purge his "
                  "kingdom of heresy after excommunication. The result, he says, is "
                  "&ldquo;such a Mist&rdquo; that subjects &ldquo;know not a stranger that "
                  "thrusteth himself into the throne of their lawfull Prince, from him whom "
                  "they had themselves placed there&rdquo;. Then the clergy take their name from "
                  "the Levites' inheritance, and with it the tithe, which he says is double "
                  "what an Athenian king, counted a tyrant, took to pay for the whole "
                  "commonwealth. And there is canon law beside civil law, and priests exempt "
                  "from the civil tribunals. You can see why he calls the first error the "
                  "main one: each of these is the church acting as a second government."),
            ("p", "The second abuse is the turning of consecration into conjuration. His "
                  "definition is plain. To consecrate is to separate a thing from common use "
                  "to God, &ldquo;to change, not the thing Consecrated, but onely the use of "
                  "it&rdquo;. A bishop who consecrates a church changes its use. A priest who "
                  "says that the bread is no longer bread, though no one sees any "
                  "difference, is, for Hobbes, in the same case as the Egyptian magicians, "
                  "only without the show. He takes &ldquo;This is my Body&rdquo; to be "
                  "&ldquo;aequivalent&rdquo; to &ldquo;This signifies, or represents my "
                  "Body&rdquo;, a figure of speech. Catholic theologians answered that the "
                  "doctrine itself says the senses see nothing change, because substance "
                  "is one thing and the appearances another. Hobbes's reply to that is in "
                  "Chapter 46, where the distinction itself is what he attacks, and the "
                  "third lesson of this course comes to it."),
            ("p", "The third error is about eternal life. Hobbes reads Genesis as saying that "
                  "Adam lived on condition he did not sin, that Christ's passion restores "
                  "eternal life to the faithful, and that the doctrine that every man has "
                  "eternity by nature, because his soul is immortal, is later and wrong. For "
                  "him &ldquo;the Soule in Scripture, signifieth alwaies, either the Life, or "
                  "the Living Creature&rdquo;, and God, who raised dust and clay into a living "
                  "creature, can as easily raise a dead body. From the rejected doctrine, he "
                  "says, come eternal torments, purgatory, ghosts that walk, exorcism, "
                  "prayers to the dead and indulgences. He goes through Bellarmine's texts one "
                  "by one and finds none that proves purgatory. He is also candid about "
                  "what he cannot explain. On Christ's saying that a sin against the Holy Ghost "
                  "will not be forgiven in this world or the next, he writes that it is "
                  "&ldquo;very hardly to bee reconciled with all the Doctrines now "
                  "unanimously received&rdquo;, and adds that it is not &ldquo;any shame, to "
                  "confesse the profoundnesse of the Scripture&rdquo;. He offers his own "
                  "readings of it only &ldquo;to the consideration of more learned "
                  "Divines&rdquo;. On eternal torment he is as plain as he is on purgatory: "
                  "he can &ldquo;find no where that any man shall live in torments "
                  "Everlastingly&rdquo;."),
            ("p", "The hinge of the whole Part is this. If the church were the kingdom of God, "
                  "the clergy would be its officers and every Christian a subject of two "
                  "governments, and if eternal torment waited on the favour of the priests, "
                  "nobody could afford to disobey them. Hobbes is arguing that the "
                  "authority of Scripture, properly read, leaves the civil sovereign as the "
                  "only king on earth. Whether the premise c → s is true is a question about the "
                  "texts, and the lab can only tell you how much hangs on it. The next lesson, "
                  "<em>Demonology and the Relics of the Gentiles</em>, follows the "
                  "second of the four causes, the heathen poets' ghosts and demons."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "preset": "hobbes",
            "show": "all",
            "presets": [
                {"id": "hobbes",
                 "label": "Hobbes: k → c, c → s, no s, so not k",
                 "premises": ["k -> c", "c -> s", "~s"], "conclusion": "~k",
                 "expect": {"vaRows": "8", "vaCounter": "0", "vaVerdict": "Valid"}},
                {"id": "no-link",
                 "label": "Without c → s: k → c and no s, so not k",
                 "premises": ["k -> c", "~s"], "conclusion": "~k",
                 "expect": {"vaRows": "8", "vaCounter": "1", "vaVerdict": "Invalid"}},
                {"id": "no-bridge",
                 "label": "Without k → c: c → s and no s, so not k",
                 "premises": ["c -> s", "~s"], "conclusion": "~k",
                 "expect": {"vaRows": "8", "vaCounter": "1", "vaVerdict": "Invalid"}},
            ],
            "panel_title": "Does the present church fail to be God's kingdom",
            "panel_intro": (
                "This lab tests whether premises force a conclusion, row by row over every "
                "assignment of true and false. Here k is that the present church is the "
                "kingdom of God, c that the kingdom of God has come, and s that Christ's "
                "second coming has happened. The logic is undisputed; whether each premise is "
                "true is what Hobbes, Bellarmine and Beza argue about."
            ),
        }),
        "steps_title": "Setting out an argument about a kingdom",
        "steps_intro": "Five steps; the lab does the fourth and cannot do the fifth.",
        "steps": [
            ("Give each claim a letter",
             "Write down what each letter means and keep it fixed: k for the present church "
             "being the kingdom of God, c for the kingdom having come, s for the second "
             "coming having happened."),
            ("Write each premise as a conditional or a denial",
             "State the premises as Hobbes's sentences allow: k → c, c → s, ¬s. Find the "
             "sentence in the chapter each one comes from, and drop any premise you cannot "
             "find."),
            ("Test the whole for validity",
             "Look for a row in which every premise is true and the conclusion false. If "
             "there is none, the argument is valid."),
            ("Remove one premise at a time",
             "Rerun the test without each premise. A premise whose removal leaves a "
             "counterexample is needed; here all three are, and the middle one is the one "
             "a reader can contest."),
            ("Ask who would deny the premise, and on what text",
             "Valid is not sound. For c → s the deniers are the ones who say the kingdom is "
             "the church now on earth, and the text they cite is Mark 9."),
        ],
        "worked": {
            "title": "Counting the rows by hand",
            "intro": [
                "Take the first preset and list the rows for k, c and s. There are eight, "
                "and you want the ones where every premise is true.",
            ],
            "lines": [
                "premise ¬s needs s false: 4 rows left",
                "premise c → s with s false needs c false: 2 rows",
                "premise k → c with c false needs k false: 1 row",
                "that row is k, c, s all false: ¬k is true",
                "no row has the premises true and ¬k false",
            ],
            "after": [
                "Now drop c → s. The rows with s false and k → c true are k and c both "
                "false, c alone true, and both true: three rows, and in the last of them "
                "¬k is false. That is the one counterexample the <em>no-link</em> preset "
                "reports.",
            ],
        },
        "quiz_title": "What the argument needs",
        "quiz": [
            {"q": "In the lab's argument, which premise says the kingdom of God comes only "
                  "with Christ's second coming?",
             "a": ["k → c", "c → s", "¬s", "¬k"],
             "c": 1,
             "why": "c → s says that if the kingdom has come, the second coming has happened. "
                    "k → c says that if the church is the kingdom, the kingdom has come. ¬s "
                    "says the second coming has not happened, and ¬k is the conclusion."},
            {"q": "Remove c → s from the argument and run it. What does the lab report?",
             "a": ["Still valid, because ¬s and k → c are enough",
                   "Valid, but no longer sound",
                   "Invalid: one row makes the premises true and the church the kingdom",
                   "Invalid because it has no premises"],
             "c": 2,
             "why": "With k and c true and s false, k → c and ¬s are both true while ¬k is "
                    "false, so there is a counterexample. The two premises that remain say "
                    "nothing about when the kingdom comes."},
            {"q": "According to Hobbes, when did the kingdom of God by pact with the Jews "
                  "end?",
             "a": ["At the death of Moses",
                   "At the destruction of the Temple",
                   "At the Resurrection of Christ",
                   "When they chose Saul to be king like the nations"],
             "c": 3,
             "why": "Chapter 44 says the kingdom was instituted by Moses over the Jews and "
                    "ceased in the election of Saul, when they would not be governed by God "
                    "any more. The Resurrection is the date Beza gave for its beginning."},
            {"q": "What does Hobbes say consecration changes?",
             "a": ["The use of the thing, from common to holy",
                   "The nature of the thing",
                   "The thing's price",
                   "Nothing at all, since it is only a ceremony"],
             "c": 0,
             "why": "To consecrate is to change &ldquo;not the thing Consecrated, but onely "
                    "the use of it&rdquo;, from profane and common to holy. Pretending that "
                    "words change the nature of the thing is what he calls conjuration."},
        ],
        "mistakes": [
            ("Thinking the argument is good because the lab calls it valid",
             "The <em>hobbes</em> preset has no counterexample, and that shows only that "
             "the conclusion follows if the three premises are true. The middle premise is "
             "the whole quarrel: Bellarmine and Beza each deny that the kingdom comes only "
             "at the second coming, and the lab, which sees letters, treats their denial "
             "and Hobbes's assertion alike."),
            ("Thinking Hobbes denies that God reigns now",
             "He says God &ldquo;ever was, is, and shall be King, of all men, and of all "
             "creatures&rdquo;, by his power. What has lapsed is God's kingdom by pact, "
             "which began with Moses and ended with Saul and will be restored at Christ's "
             "return. Christians are meanwhile in the kingdom of grace, which is a "
             "promise."),
            ("Reading the chapter as a denial of resurrection or of eternal life",
             "Hobbes affirms both for the faithful. His claim is that eternal life is a gift "
             "of grace restored by Christ, so that it is not a natural property of every "
             "soul, and that Scripture's soul means the life or the living creature. The "
             "doctrines he rejects, torments without end, purgatory and ghosts, are the ones "
             "he says rest on the immortal soul."),
        ],
        "standard": (
            "Finish when you can test the chapter's argument and name the premise it rests on.",
            "Write Hobbes's argument against the present church as the kingdom of God in "
            "letters, test it for validity, remove each premise in turn, and say which "
            "premise carries it and who would deny it."
        ),
        "note": (
            "The truth table is exact and the logic undisputed. What the lab cannot settle is "
            "whether any premise is true, above all c → s, which depends on reading "
            "<em>kingdom</em> as Hobbes does in Chapter 35. The lesson reports his "
            "arguments about Scripture and the use they had in 1651, and does not judge "
            "them as theology."
        ),
    },
]

LEVKIT_LESSONS = [
    # ---------------------------------------------------------------- 02
    # Leviathan ch. 45, 1651 p. 359; PDF p. 544 of the operator's copy.
    {
        "slug": "demonology-and-images",
        "title": "Demonology and the Relics of the Gentiles",
        "module": "Chapter 45 · Of Daemonology, and other Reliques of the Religion of the Gentiles",
        "one_line": "Hobbes says the demons of the Gentiles are images in the brain taken for beings in the air, and that worshipping an image is the same mistake in wood or stone.",
        "summary": (
            "Chapter 45 goes back to the pressed eye of Chapter 1: an image is a seeming, and "
            "men who did not know it took seemings for ghosts. Define body, phantasm, image "
            "and spirit as the chapter does, and compute which affirmations about demons, "
            "ghosts and spirits are true, false or absurd on them, under the Gentiles' "
            "definition of a demon, Hobbes's, and Scripture's spirit."
        ),
        "key": [
            "an image: a seeming of something visible",
            "a phantasm: a seeming in the brain",
            "a body has dimension; so does a spirit",
            "absurd: names that cannot be added",
            "no image of God, of the soul or of spirits",
            "worship: signs of fear to offend",
        ],
        "key_label": "Images, demons and worship in six lines",
        "concepts_intro": (
            "The chapter has two halves. The first is about what a demon is, and the second "
            "about what it is to worship an image, and one definition does most of the work "
            "of both."
        ),
        "concepts": [
            ("Image and phantasm",
             "The strict sense of image is the resemblance of something visible: the "
             "show of a man in water, of the sun by refraction, anything that depends on the "
             "fancy and on the organ. These are what the Greeks called ideas, idols and "
             "phantasms. There can be an image only of a visible body, so none of God, of the "
             "soul or of spirits."),
            ("Demon",
             "The Gentiles took the phantasms they dreamed or saw for beings outside "
             "them, ghosts in the air, and so named them demons. Hobbes holds that they are "
             "&ldquo;Idols, or Phantasms of the braine&rdquo;. In Scripture he finds good "
             "and evil angels and spirits, but never one that is incorporeal."),
            ("Worship and idolatry",
             "Worship is every word or act that signs fear to offend or desire to please, "
             "and it is civil or divine according to what the worshipper believes he is "
             "honouring. To worship an image is idolatry when the worshipper takes the "
             "image, or the fancy it stands for, to be a god or to have a god in it."),
        ],
        "read_title": "The passage first, then the chapter's two halves",
        "read_intro": (
            "The passage is Hobbes's definition of what an image can be an image of. The "
            "lesson starts where the chapter does, with sight, then follows the demons, "
            "defines the names in the lab, and reads his account of idolatry and of the "
            "relics of the Gentiles in the church."
        ),
        "body": [
            ("p", "<strong>Chapter 45.</strong> &ldquo;It is also evident, that there can be no "
                  "Image of a thing Infinite: for all the Images, and Phantasmes that are made "
                  "by the Impression of things visible, are figured: but Figure is a quantity "
                  "every way determined: And therefore there can bee no Image of God; nor of the "
                  "Soule of Man; nor of Spirits; but onely of Bodies Visible, that is, Bodies "
                  "that have light in themselves, or are by such enlightened.&rdquo;"),
            ("p", "The chapter opens on something you may remember from the first lesson of "
                  "Course 1: press your eye hard and a light appears outside it, before you, "
                  "which nobody else can see, because &ldquo;there is indeed no such thing "
                  "without him, but onely a motion in the interiour organs&rdquo;. That is "
                  "sight in miniature. Light from bodies reaches the eye, and what it makes in "
                  "the creature is an imagination of the object that &ldquo;seemeth not to "
                  "bee a meer Imagination, but the Body it selfe without us&rdquo;. When the "
                  "object goes the motion goes on, and we call it imagination and memory, or, "
                  "asleep, a dream. The ancients, Hobbes says, never found this out, so it was "
                  "hard for them to think of those images other than as things really "
                  "outside us."),
            ("p", "Then two schools of explanation arose. Some said the images are absolutely "
                  "incorporeal, forms without matter, colour and figure without a coloured or "
                  "figured body, which could put on airy bodies like a garment to be seen. "
                  "Others said they are bodies and living creatures, made of air or of some "
                  "subtler matter, condensed when they will be seen. Both agreed on one name, "
                  "demons. Hobbes is unsparing about the reasoning: it is as if the dead of whom "
                  "they dreamed were not &ldquo;Inhabitants of their own Brain, but of the Air, "
                  "or of Heaven, or Hell&rdquo;, and as if you saw your own ghost in a looking "
                  "glass. People feared them as things of unlimited power, he says, and the "
                  "rulers of the heathen commonwealths, who saw how useful the fear was, "
                  "regulated it into a demonology run by the poets, making some demons good, "
                  "&ldquo;a Spurre to the Observance&rdquo;, and others evil, &ldquo;Reines to "
                  "withhold them from the Violation of the Laws&rdquo;."),
            ("p", "The Greeks carried this into Asia, Egypt and Italy with their language, and "
                  "so to the Jews, who used the word only of evil spirits and called good "
                  "ones the Spirit of God. Anyone strange in speech or behaviour, mad, "
                  "epileptic, or fasting oddly like John the Baptist, was said to have a devil. "
                  "Why, a reader of the Gospels will ask, did Christ not correct it, and "
                  "why does he speak to devils? Hobbes has answers. &ldquo;A spirit hath not "
                  "flesh and bone&rdquo; does not say a spirit is no body, since air is a body "
                  "too. A command to a madness to depart is no odder than rebuking a fever or "
                  "the sea. Satan entering Judas is the hostile design itself, since it is "
                  "&ldquo;hard to say, that the Devill was entred into Judas, before he had any "
                  "such hostile designe&rdquo;. And the question why Christ did not teach "
                  "otherwise is, he says, &ldquo;more curious, than necessary for a Christian "
                  "mans Salvation&rdquo;. His summary is careful: &ldquo;I find in Scripture "
                  "that there be Angels, and Spirits, good and evill; but not that they are "
                  "Incorporeall&rdquo;."),
            ("p", "You can see here how a lab of the names helps. Take the definitions. A "
                  "body has dimension. A phantasm is a seeming in the brain. An image is a "
                  "phantasm of something visible. A spirit, as Scripture speaks of it, is a "
                  "body that is subtle and invisible. Dimension and incorporeal cannot be "
                  "added, nor can visible and invisible. The Gentiles' demon is a phantasm "
                  "taken to be incorporeal. Hobbes's demon is a phantasm and nothing more. "
                  "The lab states each definition and then gives a verdict on eight "
                  "affirmations, using the rule of Chapter 5: true if every part of the "
                  "predicate is in the subject, absurd if the sum of the two contains names "
                  "that cannot be added, otherwise false."),
            ("p", "The <em>gentiles</em> preset gives the demon the Gentiles' definition. "
                  "<em>A demon is a phantasm</em> and <em>a demon is incorporeal</em> "
                  "come out true, and the demon is a body comes out absurd, since it would "
                  "add dimension to what was defined as incorporeal. Four claims are true, one "
                  "false and three absurd. Switch to <em>hobbes</em>, where the demon is a "
                  "phantasm only, and the same claim, a demon is a body, is now false and "
                  "not absurd. Nothing in the definition says the demon is incorporeal, so "
                  "there is no clash, only a missing part. And a demon is incorporeal is false "
                  "too. Three claims true, three false, two absurd. Under <em>scripture</em>, "
                  "where a demon is a spirit in the chapter's sense, the demon is a body is "
                  "true, and incorporeal is absurd: three true, two false, three absurd. "
                  "The point to take is Hobbes's about the Gentiles' demon: define it as "
                  "incorporeal and then say anything bodily of it, and the names you have "
                  "used contradict one another."),
            ("p", "A caution before you trust the labels. The lab's four verdicts, true, false, "
                  "absurd and insignificant, are the lab's own sorting, not Hobbes's. He holds "
                  "that of absurd and false affirmations, if they are universal, there can be "
                  "no understanding, so a false universal affirmation is itself absurd to "
                  "him, and he counts both names with no definition and names that contradict "
                  "one another as insignificant speech. The lab's <em>absurd</em> therefore "
                  "marks only a contradiction among the names the lesson states, and its "
                  "<em>false</em> means no more than not borne out by these definitions. "
                  "A claim it marks false, if it were a universal affirmation, Hobbes would "
                  "call absurd too. The lesson's definitions are also simpler than his: a "
                  "phantasm is defined here without dimension, where Hobbes takes it to be "
                  "a motion in the organs."),
            ("p", "The second half is about worship. Honour, Hobbes says, is to value another's "
                  "power, and is inward and secret; the outward signs are worship, &ldquo;all "
                  "words and actions that betoken Fear to Offend, or Desire to Please&rdquo;. "
                  "Worship offered to one we take for a man is civil, and to one we take for "
                  "God it is divine, whatever the words, and the difference lies in "
                  "&ldquo;the intention of the Worshipper&rdquo;. He rejects the old "
                  "distinction between two Greek words for service, because both are "
                  "used of our service to God. This was a live point. Defenders of images, "
                  "Catholic theologians especially, had distinguished the veneration of an image "
                  "from the adoration due to God alone, and Hobbes will not let the "
                  "distinction rest on words."),
            ("p", "Idolatry, then, is to worship an image by signs of inward honour to the "
                  "matter of it, or to the phantasm it stands for, or to both. To take your "
                  "hat off before a throne honours the prince and not the stool. To suppose the "
                  "prince's soul is in the stool, or to petition it, would be divine worship "
                  "and idolatry. And Hobbes adds a point of his own: if a "
                  "king compels a man by the terror of death to worship him, it is &ldquo;no "
                  "Worship; and therefore no Idolatry&rdquo;. The act is a sign of fear for "
                  "oneself and not of inward honour, and it gives no scandal, since it is the "
                  "sovereign's act and not the man's. Honour done to an idol for fear is not "
                  "idolatry either. But a pastor, or a man whose knowledge others follow, who "
                  "does it without making his fear as plain as the worship gives scandal, a "
                  "sin of its own. He does not condemn "
                  "pictures: &ldquo;to draw a Picture after a fancy&rdquo; is no sin, "
                  "but to hold it for a representation of God is. A portrait of a dead friend, "
                  "as a monument, is fine. He asks that Christian sovereigns do what Hezekiah "
                  "did to the brazen serpent when the people burned incense to it, and break "
                  "down the images their subjects worship."),
            ("p", "The chapter closes with a list of the relics of the Gentiles in the church of "
                  "his day: the canonizing of saints, which began in Rome with Romulus on the "
                  "word of Julius Proculus; the name and power of Pontifex Maximus, which the "
                  "popes took over from the emperors; processions, wax candles, holy water, "
                  "wakes and carnivals and maypoles. Hobbes calls them &ldquo;old empty "
                  "Bottles of Gentilisme&rdquo;, which the doctors of Rome have filled with new "
                  "wine. The church's defenders answered that it had baptised the customs it "
                  "found and had not been taken over by them. The "
                  "lab belongs to the first half, though: Hobbes's argument is that a demon "
                  "is a name for a phantasm, and the rest of the chapter is built on "
                  "that."),
            ("p", "The third cause of darkness is in the next lesson, <em>Vain Philosophy "
                  "and Fabulous Traditions</em>: the schoolmen's terms, where the names "
                  "themselves are said to signify nothing."),
        ],
        "lab": ("levkit", {
            "mode": "reckon",
            "view": "names",
            "preset": "gentiles",
            "presets": _reckon([
                {"id": "gentiles",
                 "label": "The Gentiles' demon: a phantasm taken to be incorporeal",
                 "simple": "dimension seeming brain visible invisible incorporeal subtle",
                 "opposed": [{"a": "dimension", "b": "incorporeal"},
                             {"a": "visible", "b": "invisible"}],
                 "defs": [{"name": "body", "parts": "dimension"},
                          {"name": "phantasm", "parts": "seeming brain"},
                          {"name": "image", "parts": "phantasm visible"},
                          {"name": "ghost", "parts": "phantasm"},
                          {"name": "fairy", "parts": "phantasm"},
                          {"name": "spirit", "parts": "body subtle invisible"},
                          {"name": "demon", "parts": "phantasm incorporeal"}],
                 "claims": [{"claim": "demon-phantasm", "subject": "demon", "predicate": "phantasm"},
                            {"claim": "demon-body", "subject": "demon", "predicate": "body"},
                            {"claim": "demon-incorporeal", "subject": "demon", "predicate": "incorporeal"},
                            {"claim": "spirit-body", "subject": "spirit", "predicate": "body"},
                            {"claim": "spirit-incorporeal", "subject": "spirit", "predicate": "incorporeal"},
                            {"claim": "spirit-image", "subject": "spirit", "predicate": "image"},
                            {"claim": "ghost-body", "subject": "ghost", "predicate": "body"},
                            {"claim": "fairy-ghost", "subject": "fairy", "predicate": "ghost"}],
                 "expect": {"lrkCounts": "4 true, 1 false, 3 absurd, 0 insignificant", "lrkVerdicts": "demon-phantasm true; demon-body absurd; demon-incorporeal true; spirit-body true; spirit-incorporeal absurd; spirit-image absurd; ghost-body false; fairy-ghost true"}},
                {"id": "hobbes",
                 "label": "Hobbes's demon: an idol of the brain and nothing more",
                 "simple": "dimension seeming brain visible invisible incorporeal subtle",
                 "opposed": [{"a": "dimension", "b": "incorporeal"},
                             {"a": "visible", "b": "invisible"}],
                 "defs": [{"name": "body", "parts": "dimension"},
                          {"name": "phantasm", "parts": "seeming brain"},
                          {"name": "image", "parts": "phantasm visible"},
                          {"name": "ghost", "parts": "phantasm"},
                          {"name": "fairy", "parts": "phantasm"},
                          {"name": "spirit", "parts": "body subtle invisible"},
                          {"name": "demon", "parts": "phantasm"}],
                 "claims": [{"claim": "demon-phantasm", "subject": "demon", "predicate": "phantasm"},
                            {"claim": "demon-body", "subject": "demon", "predicate": "body"},
                            {"claim": "demon-incorporeal", "subject": "demon", "predicate": "incorporeal"},
                            {"claim": "spirit-body", "subject": "spirit", "predicate": "body"},
                            {"claim": "spirit-incorporeal", "subject": "spirit", "predicate": "incorporeal"},
                            {"claim": "spirit-image", "subject": "spirit", "predicate": "image"},
                            {"claim": "ghost-body", "subject": "ghost", "predicate": "body"},
                            {"claim": "fairy-ghost", "subject": "fairy", "predicate": "ghost"}],
                 "expect": {"lrkCounts": "3 true, 3 false, 2 absurd, 0 insignificant", "lrkVerdicts": "demon-phantasm true; demon-body false; demon-incorporeal false; spirit-body true; spirit-incorporeal absurd; spirit-image absurd; ghost-body false; fairy-ghost true"}},
                {"id": "scripture",
                 "label": "A demon taken as Scripture's spirit: a subtle, invisible body",
                 "simple": "dimension seeming brain visible invisible incorporeal subtle",
                 "opposed": [{"a": "dimension", "b": "incorporeal"},
                             {"a": "visible", "b": "invisible"}],
                 "defs": [{"name": "body", "parts": "dimension"},
                          {"name": "phantasm", "parts": "seeming brain"},
                          {"name": "image", "parts": "phantasm visible"},
                          {"name": "ghost", "parts": "phantasm"},
                          {"name": "fairy", "parts": "phantasm"},
                          {"name": "spirit", "parts": "body subtle invisible"},
                          {"name": "demon", "parts": "spirit"}],
                 "claims": [{"claim": "demon-phantasm", "subject": "demon", "predicate": "phantasm"},
                            {"claim": "demon-body", "subject": "demon", "predicate": "body"},
                            {"claim": "demon-incorporeal", "subject": "demon", "predicate": "incorporeal"},
                            {"claim": "spirit-body", "subject": "spirit", "predicate": "body"},
                            {"claim": "spirit-incorporeal", "subject": "spirit", "predicate": "incorporeal"},
                            {"claim": "spirit-image", "subject": "spirit", "predicate": "image"},
                            {"claim": "ghost-body", "subject": "ghost", "predicate": "body"},
                            {"claim": "fairy-ghost", "subject": "fairy", "predicate": "ghost"}],
                 "expect": {"lrkCounts": "3 true, 2 false, 3 absurd, 0 insignificant", "lrkVerdicts": "demon-phantasm false; demon-body true; demon-incorporeal absurd; spirit-body true; spirit-incorporeal absurd; spirit-image absurd; ghost-body false; fairy-ghost true"}},
            ]),
            "panel_title": "Which affirmations about demons hold on the definitions",
            "panel_intro": (
                "Each name is defined as the sum of simpler names, with two pairs that cannot be "
                "added. The lab expands each name and gives a verdict on each claim: true when "
                "every part of the predicate is in the subject, absurd when the two together "
                "contain names that cannot be added, otherwise false. The definitions are "
                "the lesson's rendering of Chapter 45, and a different definition of demon "
                "changes the verdicts."
            ),
        }),
        "steps_title": "Testing affirmations about demons and spirits",
        "steps_intro": "Four steps, the same for any vocabulary.",
        "steps": [
            ("Define each name as a sum",
             "Write every name as the simpler names it is made of, down to names that need no "
             "definition, such as dimension or seeming."),
            ("Mark the names that cannot be added",
             "List the pairs that cannot meet in one thing, here dimension with "
             "incorporeal and visible with invisible."),
            ("Read each claim by the rule",
             "True if every part of the predicate is in the subject. Absurd if the subject, "
             "the predicate or the two together contain a pair that cannot be added. Otherwise "
             "false."),
            ("Change one definition and run it again",
             "Alter what a demon is and see which verdicts move. Those that do not move "
             "were settled by the other names."),
        ],
        "worked": {
            "title": "A demon is a body, under two definitions",
            "intro": [
                "Take the claim a demon is a body, and expand each name by hand.",
            ],
            "lines": [
                "body = dimension",
                "Gentiles: demon = seeming, brain, incorporeal",
                "dimension is not among the parts: not true",
                "sum has dimension and incorporeal: absurd",
                "Hobbes: demon = seeming, brain; sum has no clash: false",
            ],
            "after": [
                "The two definitions give two different verdicts on one claim, which is why "
                "the lab asks you to read the definition before the verdict.",
            ],
        },
        "quiz_title": "True, false and absurd",
        "quiz": [
            {"q": "In the preset where a demon is a phantasm and nothing more, what is the "
                  "verdict on the claim that a demon is a body?",
             "a": ["True", "Absurd", "False, but not absurd", "Insignificant"],
             "c": 2,
             "why": "Body has the part dimension, which a phantasm lacks, so the claim is "
                    "not true. Nothing in a phantasm is incorporeal, so the two together do "
                    "not contain a pair that cannot be added, and it is not absurd. Every "
                    "name in it is defined, so it is not insignificant."},
            {"q": "A man prostrates himself before a king, believing him a man. On Hobbes's "
                  "account this is:",
             "a": ["Idolatry, because prostration is a sign of divine honour",
                   "Divine worship, whatever he believes",
                   "A sin of scandal in every case",
                   "Civil worship, because the difference lies in what the worshipper "
                   "believes he is honouring"],
             "c": 3,
             "why": "Hobbes says to fall prostrate before a king, in him that thinks him but "
                    "a man, is civil worship. He rejects distinctions drawn from the "
                    "Greek words for service, and puts the difference in the intention of "
                    "the worshipper."},
            {"q": "Why, on Hobbes's account, were there many demoniacs in the primitive church "
                  "and few madmen, while now we hear of many madmen and few demoniacs?",
             "a": ["Because nature changed after the apostles",
                   "Because the change is one of names, not of nature",
                   "Because demons ceased to act after the Reformation",
                   "Because the sick used to be more numerous"],
             "c": 1,
             "why": "He says it &ldquo;proceeds not from the change of Nature; but of "
                    "Names&rdquo;. The same disorders were then called possession and are "
                    "now called madness. His explanation of the lost gift of casting out "
                    "devils is a different one, that the gifts were given while men trusted "
                    "wholly to Christ."},
        ],
        "mistakes": [
            ("Taking the lab's four verdicts for Hobbes's",
             "The lab sorts claims into true, false, absurd and insignificant. Its false is "
             "only not borne out by the definitions, like a ghost is a body. Its absurd is a "
             "contradiction among the stated names, like a demon is a body when demon was "
             "defined as incorporeal. Hobbes does not draw the line there: a false universal "
             "affirmation is absurd to him as well, so the lab's false is not his "
             "<em>merely wrong</em>."),
            ("Thinking Hobbes denies that there are angels or spirits",
             "He says he finds in Scripture &ldquo;Angels, and Spirits, good and evill&rdquo;. "
             "What he does not find is that they are incorporeal, or that any man's body was "
             "possessed by one. He thinks spirits are subtle, invisible bodies."),
            ("Thinking images and pictures are what he condemns",
             "He says outright that he does not call it a sin to draw a picture after a fancy. "
             "What he condemns is worship of the image as if God or a saint were in it, and "
             "he allows images as monuments to friends and to men worth remembering."),
        ],
        "standard": (
            "Finish when you can say which affirmations about demons and spirits are absurd "
            "on a given set of definitions.",
            "Given definitions of body, phantasm, image, spirit and demon, classify each "
            "affirmation as true, false or absurd, and say which definition of demon makes "
            "a demon is a body absurd."
        ),
        "note": (
            "The lab shows what follows on the lesson's definitions of image, phantasm "
            "and spirit, which are Hobbes's as the lesson renders them. Whether a "
            "demon, an angel or a soul is as those definitions say is the question the chapter "
            "argues from Scripture and that Christian traditions have answered differently, "
            "and the lab cannot settle it."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Leviathan ch. 46, 1651 p. 372; PDF p. 561 of the operator's copy (the opening
    # quotation); ch. 46, 1651 p. 367, PDF p. 554 (the definition of philosophy).
    {
        "slug": "vain-philosophy",
        "title": "Vain Philosophy and Fabulous Traditions",
        "module": "Chapter 46 · Of Darknesse from Vain Philosophy, and Fabulous Traditions",
        "one_line": "Hobbes defines philosophy as reasoning from causes to effects, and says the schoolmen's separated essences are names that stand for nothing.",
        "summary": (
            "Chapter 46 defines philosophy, tells how the schools began in leisure, and goes "
            "through the terms of the Aristotelian schools that Hobbes says signify nothing: "
            "essences, abstract and separated, and the standing now of eternity. Give a small "
            "vocabulary its definitions and compute which of the schoolmen's affirmations are "
            "insignificant because a name has no definition, which are absurd, and which "
            "change when the schoolmen's definition of the soul does."
        ),
        "key": [
            "philosophy: reasoning from cause to effect",
            "leisure is the mother of philosophy",
            "is: a sign of consequence, not a thing",
            "entity and essence name nothing",
            "insignificant: a name with no definition",
            "absurd: names that cannot be added",
        ],
        "key_label": "Vain philosophy in six lines",
        "concepts_intro": (
            "This is Hobbes's longest chapter in the last Part, and its argument is about "
            "words. Three ideas carry it."
        ),
        "concepts": [
            ("Philosophy",
             "The knowledge got by reasoning from the way a thing is generated to its "
             "properties, or from its properties to some possible way of generating it, so "
             "that we can produce the effects human life requires. Experience, false "
             "conclusions, revelation and what is taken on the authority of books are not "
             "philosophy."),
            ("Names that stand for nothing",
             "The word <em>is</em>, Hobbes says, is no name of a thing. It signs that the "
             "name after it follows from the name before. Entity, essence and the terms "
             "derived from them are therefore not names of things, and a name that stands for "
             "nothing makes the speech that uses it insignificant."),
            ("Vain philosophy",
             "Hobbes's label for what the schoolmen made of Aristotle's metaphysics: separated "
             "essences, the standing now, forms poured into bodies, and a physics that explains "
             "heavy things falling by their endeavour to be below. He says it matters to "
             "government because those who hold it can be frightened out of obeying the laws."),
        ],
        "read_title": "The passage first, then the chapter",
        "read_intro": (
            "The passage is the center of Hobbes's argument about the word <em>is</em>. The "
            "lesson goes back to his definition of philosophy and the schools, follows the "
            "argument about essences, runs the names in the lab and then reads what he says "
            "follows for morals and politics."
        ),
        "body": [
            ("p", "<strong>Chapter 46.</strong> &ldquo;They are therefore no Names of Things; but "
                  "Signes, by which wee make known, that wee conceive the Consequence of one name "
                  "or Attribute to another: as when we say, a Man, is, a living Body, wee mean "
                  "not that the Man is one thing, the Living Body another, and the Is, or Beeing "
                  "a third: but that the Man, and the Living Body, is the same thing; because "
                  "the Consequence, If hee bee a Man, hee is a living Body, is a true "
                  "Consequence, signified by that word Is&rdquo;."),
            ("p", "Hobbes starts with a definition, as he always does. &ldquo;By PHILOSOPHY, is "
                  "understood the Knowledge acquired by Reasoning, from the Manner of the "
                  "Generation of any thing, to the Properties; or from the Properties, to some "
                  "possible Way of Generation of the same&rdquo;, so as to produce &ldquo;such "
                  "Effects, as humane life requireth&rdquo;. The geometer, who goes from the "
                  "construction of a figure to its properties, is his model, and the "
                  "astronomer. It follows that experience, which is what the prudent man has "
                  "and animals have, is not philosophy, nor is a false conclusion, since "
                  "&ldquo;he that Reasoneth aright in words he understandeth, can never conclude "
                  "an Error&rdquo;, nor what is known by revelation, nor what is got from "
                  "books, which is &ldquo;not Knowledg, but Faith&rdquo;. And he tells where "
                  "philosophy comes from. It needs time, and for most of history men "
                  "lacked it: &ldquo;Leasure is the mother of Philosophy, and Common-wealth, the "
                  "mother of Peace, and Leasure&rdquo;."),
            ("p", "The Greek schools, he says, began when Athens, grown rich at sea, had "
                  "idle men with nothing to do but to tell and hear news, or discourse on "
                  "philosophy to the youth. Plato taught in the Academy, Aristotle in the "
                  "walk of the Lyceum, Zeno under the Stoa, and the word <em>school</em> comes "
                  "from a Greek word that means leisure, and a disputation was a "
                  "&ldquo;Passing of the time&rdquo;. Hobbes asks what use they were. Geometry, "
                  "which he calls the mother of all natural science, owes nothing to them, and "
                  "Plato would not admit anyone to his school who was not already some "
                  "geometer. Their natural philosophy was &ldquo;rather a Dream than "
                  "Science&rdquo;, their moral philosophy &ldquo;but a description of their own "
                  "Passions&rdquo;, their logic &ldquo;Captions of Words&rdquo;. He was not "
                  "alone in 1651: Bacon, Galileo and Descartes had each attacked the schools, "
                  "and Hobbes is picking a side in a quarrel that was already old. His own "
                  "reasons are his own, and the universities, in his account, kept philosophy as "
                  "a handmaid to the Roman religion. What was taught there was "
                  "&ldquo;Aristotelity&rdquo;, not philosophy, since philosophy does not "
                  "depend on authors."),
            ("p", "Then he goes to the term. He does not reject first philosophy: there is "
                  "&ldquo;a certain Philosophia prima, on which all other Philosophy ought to "
                  "depend&rdquo;, and it consists in right limiting of the meanings of the "
                  "most universal names, &ldquo;commonly called Definitions&rdquo;, of body, "
                  "time, place, matter, form, essence, substance, accident and the like. That is "
                  "what Chapter 4 said about definitions. But what the schools call "
                  "metaphysics, he says, is books taken as of supernatural philosophy, and "
                  "so far from being understood that whoever thinks there is something to "
                  "understand in them &ldquo;must needs think it supernaturall&rdquo;."),
            ("p", "Now the argument of the passage. The universe is the whole mass of "
                  "things, it is body, and has length, breadth and depth. Every part of it is "
                  "body, so what is not body is no part of the universe, and if it is no part "
                  "of the universe it is &ldquo;Nothing; and consequently no where&rdquo;. "
                  "Spirits, he adds, are not nothing, because they have dimensions and are "
                  "bodies. The word <em>incorporeal</em>, which the schools apply to them, is "
                  "&ldquo;a name of more honour&rdquo; and so fitter for God, since it is "
                  "devised to honour Him and not to describe Him. Then the passage. The "
                  "verb to be only couples two names: in the man is a living body, the "
                  "<em>is</em> says that if he is a man he is a living body, and nothing more. "
                  "A language with no such verb, he says, would reason as well. So entity, "
                  "essence and essentiality, which come from it, are not the names of "
                  "things, and neither are to be a body, corporeity, walking or life taken "
                  "as things: they are, he says, &ldquo;the names of Nothing&rdquo;."),
            ("p", "That is a reckoning, and the lab can do it. Give the vocabulary three "
                  "defined names: a body is a dimension that is in one place, a man is a "
                  "body that lives, a soul, as Scripture uses the word, is life. Say "
                  "dimension and incorporeal cannot be added, nor one place and many places. "
                  "Then run eight affirmations. In the <em>hobbes</em> preset, a man is a "
                  "body and a soul is life are true. A soul is a body is false: life is not "
                  "dimension, and nothing clashes. A body is in many places is absurd, and so "
                  "is a man is incorporeal. And three are insignificant: a man is an entity, a "
                  "soul is a separated essence, and eternity is a nunc-stans, because "
                  "<em>entity</em>, <em>separated essence</em> and <em>nunc-stans</em> were "
                  "never given a definition. Two true, one false, two absurd, three "
                  "insignificant."),
            ("p", "A caution first. The lab's four verdicts are the lab's sorting, not Hobbes's. "
                  "He says that of absurd and false affirmations, if they are universal, there "
                  "can be no understanding, so for him a false universal affirmation is "
                  "absurd too, and names with no definition and names that contradict each "
                  "other are alike insignificant speech. Here <em>absurd</em> marks only a "
                  "contradiction among the names the lesson states, and <em>false</em> only a "
                  "claim these definitions do not bear out."),
            ("p", "Now give the soul the schoolmen's definition, life that is incorporeal, "
                  "in the <em>schoolmen</em> preset. <em>A soul is a body</em> is now absurd and "
                  "not just false, since the soul includes the incorporeal and the body "
                  "includes dimension. Two true, none false, three absurd, three "
                  "insignificant. Hobbes's remark about the soul that is in the whole body and "
                  "in each part, and no more in the whole than in a finger, comes from this "
                  "definition: having made the soul incorporeal, the schools must say it is not "
                  "in a place circumscriptively but <em>definitive</em>, terms he calls "
                  "&ldquo;meer Words&rdquo;, and insignificant. Then the "
                  "third preset, <em>many-places</em>, lets a body be in many places by "
                  "defining it so. The claim a body is in many places is then true: three "
                  "true, two absurd, three insignificant. That shows something awkward for "
                  "both sides. A definition can make the claim true, which is Hobbes's own "
                  "lesson about starting from definitions, and what the schoolmen have then "
                  "done is change what a body is. Hobbes's complaint is that the doctrine is "
                  "offered &ldquo;as if it were an acknowledgement of the Divine Power, to "
                  "say, that which is, is not&rdquo;."),
            ("p", "The rest of the chapter is examples. The standing now is the schoolmen's "
                  "eternity, &ldquo;which neither they, nor any else understand&rdquo;. "
                  "For heaviness, Aristotle's school says heavy bodies sink because of their "
                  "heaviness, and heaviness is &ldquo;an endeavour to goe to the center of "
                  "the Earth&rdquo;, so the cause of falling is an endeavour to be below, "
                  "&ldquo;as much as to say, that bodies descend, or ascend, because they "
                  "doe&rdquo;. A soul is created by pouring in and poured in by creation. The "
                  "will is the cause of willing, and fortune of what happens, which is "
                  "ignorance disguised. What would be the use of all this subtlety in a work "
                  "on government and obedience, he asks himself, and answers: so that men "
                  "are not frightened from the laws &ldquo;with empty names; as men fright "
                  "Birds from the Corn with an empty doublet, a hat, and a crooked "
                  "stick&rdquo;. If virtue is poured into a man from heaven, who will try to "
                  "obey the laws? Or who will not obey a priest who can make God, rather than "
                  "his sovereign?"),
            ("p", "He carries it into morals and politics. Aristotle and the heathens "
                  "defined good and evil by appetite, and that was well enough in the "
                  "condition of men with no law but their own appetites, but in a commonwealth "
                  "&ldquo;this measure is false&rdquo;: the measure is the law. All governments "
                  "but the popular were called tyranny, which Chapter 19 had said is only a "
                  "name for the sovereignty of one with a hatred added. And it is an error "
                  "that men, not laws, should govern. &ldquo;What man, that has his naturall "
                  "Senses&rdquo;, he asks, &ldquo;does not find himself governed by them he "
                  "fears&rdquo;? He adds errors that he says Aristotle never taught, and "
                  "that came into the church: to extend the law to men's consciences by "
                  "inquisition, to let private men interpret the law by their own spirit, and "
                  "to reserve preaching to an order where the law has left it free. These are "
                  "Hobbes's arguments. The Aristotelians answered that terms like essence and "
                  "substance answer real questions and look empty only to those who have not "
                  "learned what they answer, and that is the quarrel the lab can show but "
                  "not decide."),
            ("p", "The chapter ends with fabulous traditions, the legends of the saints and "
                  "the stories of ghosts and apparitions used to prove purgatory, and "
                  "with the suppression of true philosophy: those who held that there are "
                  "antipodes, or that the year is set by the earth's motion, were punished by "
                  "the church. His question to the punishers is a fair one: is it because it is "
                  "contrary to true religion? That cannot be &ldquo;if they be true&rdquo;. "
                  "The next lesson asks the question that all four causes of darkness raise: "
                  "<em>Of the Benefit That Proceedeth from Such Darkness</em>, who gained "
                  "by it."),
        ],
        "lab": ("levkit", {
            "mode": "reckon",
            "view": "names",
            "preset": "hobbes",
            "presets": _reckon([
                {"id": "hobbes",
                 "label": "Hobbes's reading: a soul is life",
                 "simple": "dimension one-place many-places life incorporeal",
                 "opposed": [{"a": "dimension", "b": "incorporeal"},
                             {"a": "one-place", "b": "many-places"}],
                 "defs": [{"name": "body", "parts": "dimension one-place"},
                          {"name": "man", "parts": "body life"},
                          {"name": "soul", "parts": "life"}],
                 "claims": [{"claim": "man-body", "subject": "man", "predicate": "body"},
                            {"claim": "soul-life", "subject": "soul", "predicate": "life"},
                            {"claim": "soul-body", "subject": "soul", "predicate": "body"},
                            {"claim": "body-many-places", "subject": "body", "predicate": "many-places"},
                            {"claim": "man-entity", "subject": "man", "predicate": "entity"},
                            {"claim": "soul-separated-essence", "subject": "soul", "predicate": "separated-essence"},
                            {"claim": "eternity-nunc-stans", "subject": "eternity", "predicate": "nunc-stans"},
                            {"claim": "man-incorporeal", "subject": "man", "predicate": "incorporeal"}],
                 "expect": {"lrkCounts": "2 true, 1 false, 2 absurd, 3 insignificant", "lrkEmpty": "3: man-entity, soul-separated-essence, eternity-nunc-stans"}},
                {"id": "schoolmen",
                 "label": "The schoolmen's soul: life that is incorporeal",
                 "simple": "dimension one-place many-places life incorporeal",
                 "opposed": [{"a": "dimension", "b": "incorporeal"},
                             {"a": "one-place", "b": "many-places"}],
                 "defs": [{"name": "body", "parts": "dimension one-place"},
                          {"name": "man", "parts": "body life"},
                          {"name": "soul", "parts": "life incorporeal"}],
                 "claims": [{"claim": "man-body", "subject": "man", "predicate": "body"},
                            {"claim": "soul-life", "subject": "soul", "predicate": "life"},
                            {"claim": "soul-body", "subject": "soul", "predicate": "body"},
                            {"claim": "body-many-places", "subject": "body", "predicate": "many-places"},
                            {"claim": "man-entity", "subject": "man", "predicate": "entity"},
                            {"claim": "soul-separated-essence", "subject": "soul", "predicate": "separated-essence"},
                            {"claim": "eternity-nunc-stans", "subject": "eternity", "predicate": "nunc-stans"},
                            {"claim": "man-incorporeal", "subject": "man", "predicate": "incorporeal"}],
                 "expect": {"lrkCounts": "2 true, 0 false, 3 absurd, 3 insignificant", "lrkEmpty": "3: man-entity, soul-separated-essence, eternity-nunc-stans"}},
                {"id": "many-places",
                 "label": "The schoolmen, and a body that may be in many places",
                 "simple": "dimension one-place many-places life incorporeal",
                 "opposed": [{"a": "dimension", "b": "incorporeal"},
                             {"a": "one-place", "b": "many-places"}],
                 "defs": [{"name": "body", "parts": "dimension many-places"},
                          {"name": "man", "parts": "body life"},
                          {"name": "soul", "parts": "life incorporeal"}],
                 "claims": [{"claim": "man-body", "subject": "man", "predicate": "body"},
                            {"claim": "soul-life", "subject": "soul", "predicate": "life"},
                            {"claim": "soul-body", "subject": "soul", "predicate": "body"},
                            {"claim": "body-many-places", "subject": "body", "predicate": "many-places"},
                            {"claim": "man-entity", "subject": "man", "predicate": "entity"},
                            {"claim": "soul-separated-essence", "subject": "soul", "predicate": "separated-essence"},
                            {"claim": "eternity-nunc-stans", "subject": "eternity", "predicate": "nunc-stans"},
                            {"claim": "man-incorporeal", "subject": "man", "predicate": "incorporeal"}],
                 "expect": {"lrkCounts": "3 true, 0 false, 2 absurd, 3 insignificant", "lrkEmpty": "3: man-entity, soul-separated-essence, eternity-nunc-stans"}},
            ]),
            "panel_title": "Which of the schoolmen's affirmations say nothing",
            "panel_intro": (
                "Each defined name is the sum of simpler names, two pairs cannot be added, and "
                "any name in a claim with no definition and no place among the simple names "
                "stands for nothing. The lab gives each claim a verdict: insignificant, absurd, "
                "true or false. The definitions and the pairs that cannot be added are the "
                "lesson's rendering of Chapter 46; with other definitions the verdicts "
                "change."
            ),
        }),
        "steps_title": "Finding the claims that say nothing",
        "steps_intro": "Four steps, in this order, because the first test settles the rest.",
        "steps": [
            ("List the defined names and the bare ones",
             "Write which names have a definition, which are simple, and which a claim uses "
             "without either."),
            ("Name the pairs that cannot be added",
             "State them, with the reason: here dimension with incorporeal, from the "
             "universe being body, and one place with many."),
            ("Look for the insignificant claims first",
             "A claim with a name that is neither defined nor simple says nothing, whatever "
             "else it says, and has no further verdict."),
            ("Then test the rest as absurd, true or false",
             "Absurd if the two names together contain a pair that cannot be added. True if "
             "every part of the predicate is in the subject. Otherwise false."),
        ],
        "worked": {
            "title": "A soul is a body, under two definitions",
            "intro": [
                "Take the claim a soul is a body, and expand by hand.",
            ],
            "lines": [
                "body = dimension, one-place",
                "Hobbes: soul = life; sum has no clash",
                "dimension is not in the soul: false",
                "schoolmen: soul = life, incorporeal",
                "sum has dimension and incorporeal: absurd",
            ],
            "after": [
                "The only change is one part of one definition, which is why Hobbes presses "
                "the schoolmen to define their terms before they affirm anything with them.",
            ],
        },
        "quiz_title": "Insignificant, absurd and false",
        "quiz": [
            {"q": "In the preset with Hobbes's reading, what is the verdict on a man is an entity, "
                  "where entity is neither defined nor simple?",
             "a": ["Insignificant", "False", "Absurd", "True"],
             "c": 0,
             "why": "A name that is neither defined nor simple stands for nothing in this "
                    "vocabulary, so the claim is insignificant, not false. False would mean "
                    "the claim says something that the definitions do not bear out."},
            {"q": "What, on Hobbes's account in the passage, does the word is do?",
             "a": ["It names a third thing, being, added to the man and the living body",
                   "It names the substance underneath the man",
                   "It signs that the second name follows from the first, and names nothing",
                   "It names the soul"],
             "c": 2,
             "why": "&ldquo;They are therefore no Names of Things; but Signes&rdquo; of "
                    "consequence. In a man is a living body he does not mean the man is one "
                    "thing, the living body another, and the being a third."},
            {"q": "The claim a soul is a body is false when a soul is life, but absurd when a soul "
                  "is life that is incorporeal. Why?",
             "a": ["Because life is opposed to dimension",
                   "Because a soul is then a name with no definition",
                   "Because the soul now contains a part that cannot be added to dimension, "
                   "which body contains",
                   "Because absurd means false in more than one way"],
             "c": 2,
             "why": "Incorporeal and dimension are the pair the lab cannot add. The first "
                    "definition has no incorporeal part, so the claim is only untrue. The "
                    "second puts incorporeal into the soul and dimension is in the body."},
            {"q": "What does Hobbes say of Aristotle's measure of good and evil by the "
                  "appetite of men?",
             "a": ["True in every condition of men",
                   "False in every condition of men",
                   "True in a commonwealth, false in the state of nature",
                   "Well enough for men with no law but their own appetites, false in a "
                   "commonwealth, where the law is the measure"],
             "c": 3,
             "why": "He says it is well enough for men governed each by his own law, but in a "
                    "commonwealth the measure is the law, which is the will and appetite of "
                    "the state, and not the appetite of private men."},
        ],
        "mistakes": [
            ("Taking insignificant for false",
             "A false claim says something that the definitions do not bear out, a soul is a "
             "body on Hobbes's reading. An insignificant claim uses a name that stands for "
             "nothing, like a man is an entity, and so has no truth value at all. The lab "
             "counts them apart, with three insignificant claims in each preset. The "
             "line between its false and its absurd is the lab's own sorting, and Hobbes "
             "would call a false universal affirmation absurd too."),
            ("Thinking Hobbes rejects philosophy, or all of Aristotle",
             "He gives a definition of philosophy that he is happy to use, accepts "
             "first philosophy as the work of right definitions, and calls Plato the best "
             "philosopher of the Greeks. What he attacks are Aristotle's metaphysics and "
             "much of his politics and ethics, and the schools' use of them."),
            ("Reading the lab as proof that incorporeal is meaningless",
             "The lab treats incorporeal and dimension as a pair that cannot be added because "
             "the lesson says so, on Hobbes's premise that the universe is body. Someone "
             "who defines incorporeal otherwise gets other verdicts, and whether the "
             "premise is true is what the schoolmen and Hobbes dispute."),
        ],
        "standard": (
            "Finish when you can say which of a vocabulary's claims are insignificant and "
            "which are absurd.",
            "Given a vocabulary with definitions, two pairs of names that cannot be added "
            "and a list of claims, classify each as true, false, absurd or insignificant, "
            "and say how a changed definition of the soul alters the verdicts."
        ),
        "note": (
            "The lab applies one rule to the lesson's definitions. It cannot say whether "
            "the pairs it treats as incompatible are, or that a name with no definition here "
            "has none anywhere: a schoolman would give essence a definition, and the claims "
            "would then be tested on it. Whether the schools' terms signify anything is "
            "what Hobbes and they argue."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Leviathan ch. 47, 1651 p. 381; PDF p. 570 of the operator's copy (the opening
    # quotation); ch. 47, 1651 pp. 382-386, PDF pp. 571-578.
    {
        "slug": "who-benefits-from-darkness",
        "title": "Of the Benefit That Proceedeth from Such Darkness",
        "module": "Chapter 47 · Of the Benefit that proceedeth from such Darknesse",
        "one_line": "Hobbes asks cui bono of the doctrines of Part IV, lists a dozen that served the Roman clergy and the pope, and says whom he thinks their authors were.",
        "summary": (
            "Chapter 47 applies a judge's question to the doctrines the last three chapters "
            "found dark: who profits? List Hobbes's doctrines against the parties he names, "
            "count what each doctrine benefits, and see which party is served by the most, "
            "and what changes when the list is cut to the twelve he says serve to keep power or "
            "to the two that begin it."
        ),
        "key": [
            "cui bono: who gained by the act?",
            "benefit is a presumption of authorship",
            "count the doctrines each party gains by",
            "the party with the most is named first",
            "the sovereigns suffered and were accessaries",
            "three knots tied, then untied in England",
        ],
        "key_label": "Cui bono in six lines",
        "concepts_intro": (
            "The chapter is short and sharp. It rests on one rule of evidence and two "
            "stories."
        ),
        "concepts": [
            ("Cui bono",
             "A Roman judge, Cassius, asked of an accused man what profit, honour or other "
             "contentment he had got or expected by the deed. Hobbes takes it as a rule: "
             "among presumptions, none shows the author so plainly as the benefit of the "
             "act. It is a presumption, and the chapter does not claim more."),
            ("The doctrines that keep possession",
             "After the root doctrine, that the church now on earth is the kingdom of God, "
             "Hobbes goes through twelve more, from the infallibility of the pope to the "
             "universities' Aristotle, each of which he says serves to hold the power the "
             "root doctrine gave. The lab counts them against the parties."),
            ("The three knots",
             "The pontifical power was tied in three knots on the liberty of Christians, "
             "and England has since untied them in the opposite order. The sovereigns "
             "who let it be tied are, he says, accessaries to their own damage."),
        ],
        "read_title": "The passage first, then the chapter",
        "read_intro": (
            "The passage is the rule. The lesson reads how Hobbes applies it, runs the "
            "count in the lab, reads the three knots, and then the comparison of the "
            "papacy with the kingdom of fairies that closes the chapter and the "
            "last Part."
        ),
        "body": [
            ("p", "<strong>Chapter 47.</strong> &ldquo;Cicero maketh honorable mention of one of "
                  "the Cassii, a severe Judge amongst the Romans, for a custome he had, in "
                  "Criminall causes, (when the testimony of the witnesses was not sufficient,) "
                  "to ask the Accusers, Cui bono; that is to say, what Profit, Honor, or other "
                  "Contentment, the accused obtained, or expected by the Fact. For amongst "
                  "Praesumptions, there is none that so evidently declareth the Author, as doth "
                  "the BENEFIT of the Action.&rdquo;"),
            ("p", "If you have ever read a detective story you know the method. Someone is "
                  "dead, and the question is not only who could have done it but who is better off. "
                  "Hobbes has spent three chapters on doctrines he thinks false, "
                  "and now asks the judge's question of them: &ldquo;who they may be, that "
                  "have possessed the People so long in this part of Christendome, with these "
                  "Doctrines, contrary to the Peaceable Societies of Mankind&rdquo;. Notice "
                  "his wording. It is a presumption, and the best of those there are, "
                  "not a proof."),
            ("p", "The first doctrine is the one the first lesson was about, that the church "
                  "now on earth is the kingdom of God. Its benefits, he says, are worldly: the "
                  "pastors have a right of governing the church and, because church and "
                  "commonwealth are the same persons, of governing the commonwealth. By this "
                  "title the pope made the subjects of Christian princes believe that to "
                  "disobey him was to disobey Christ, which Hobbes calls in effect &ldquo;an "
                  "universall Monarchy over all Christendome&rdquo;. He tells how it grew: "
                  "the popes were first supreme teachers under Christian emperors by the "
                  "title of Pontifex Maximus, and when the empire dissolved they found "
                  "another title, the right of St. Peter. And it was not only Rome. Where the "
                  "Presbytery took the office, many of Rome's doctrines were forbidden, "
                  "&ldquo;yet this Doctrine, that the Kingdome of Christ is already come, and "
                  "that it began at the Resurrection of our Saviour, was still retained&rdquo;. "
                  "Cui bono? The same, he says, as the popes expected, &ldquo;a Soveraign "
                  "Power over the People&rdquo;, shown in the power to excommunicate a "
                  "lawful king. Hobbes concludes: &ldquo;The Authors therefore of this Darknesse in Religion, "
                  "are the Romane, and the Presbyterian Clergy&rdquo;."),
            ("p", "Then the dozen. He says: first, that the pope in his public capacity cannot "
                  "err; second, that all bishops hold their right from the pope and not "
                  "from their sovereigns, so that every state has powerful men who depend on a "
                  "foreign prince; third, the exemption of priests, monks and friars from the "
                  "civil laws and the public expense; fourth, calling priests <em>sacerdotes</em> "
                  "and the Lord's Supper a sacrifice, so that the pope has the power Moses and "
                  "Aaron had; fifth, marriage a sacrament, which gives the clergy the judging of "
                  "who is legitimate and so of succession to kingdoms; sixth, the denial of marriage "
                  "to priests, because a king who is a priest cannot marry and pass on a "
                  "kingdom; seventh, auricular confession, which gives better intelligence of "
                  "princes' designs; eighth, the canonizing of saints and martyrs; ninth, the "
                  "power of every priest to make Christ, to enjoin penance and to remit sins; "
                  "tenth, purgatory, indulgences and justification by outward works, by which "
                  "the clergy is enriched; eleventh, demonology and exorcism; and last, the "
                  "metaphysics, ethics and politics of Aristotle and the schoolmen, taught in "
                  "universities set up by the pope's authority, which keep these errors from "
                  "being found out."),
            ("p", "That is a table, and you can count it. The lab has four parties: the "
                  "pope, the Roman clergy, the Presbytery and the sovereigns, and fourteen "
                  "doctrines, the root one, the Presbyterian version of it, and the twelve. "
                  "Each doctrine is given the parties it benefits, and the lab counts. The "
                  "coding is the lesson's reading of Hobbes's sentences, and a doctrine "
                  "he says serves <em>them</em> or <em>the Clergy</em> goes to "
                  "the Roman clergy, one that he says serves the pope's power goes to the "
                  "pope, and a doctrine that serves both goes to both. Run the "
                  "<em>all</em> preset: the pope is served by 7 doctrines, the Roman "
                  "clergy by 9, the Presbytery by 1 and the sovereigns by none. The most "
                  "served is the Roman clergy."),
            ("p", "Change the list and the answer moves. In <em>held</em> the root doctrine "
                  "and its Presbyterian form are left out and only the twelve are counted: "
                  "pope 6, Roman clergy 8, Presbytery 0, sovereigns 0. In <em>root</em> only "
                  "the two root doctrines are counted: Rome's form, which serves the pope and "
                  "the Roman clergy, and the form kept by the Presbytery, which serves the "
                  "Presbytery. The three parties tie at 1 each, which is Hobbes's own "
                  "pairing, &ldquo;the Romane, and the Presbyterian Clergy&rdquo;. That is "
                  "the point of counting by party, and of counting by party, and "
                  "also its limit. The count weighs a doctrine as one, however large "
                  "its benefit, and it depends on how you code the parties. It cannot tell "
                  "you whether a benefit shows authorship."),
            ("p", "Here the ordinary objection is the strongest one. A doctrine can profit "
                  "someone without having been invented to do so, and the defenders of the "
                  "church held that its doctrines were developed by councils and "
                  "theologians who believed them, and that whether they are true has to be "
                  "settled by Scripture and reason. Hobbes would agree about the test, since he "
                  "spends the last three chapters on Scripture and reason, and his rule is for "
                  "naming suspects. And a reader may put his question to his own book: "
                  "the doctrine that the civil sovereign is supreme in religion benefits "
                  "sovereigns. The lab can count that too. Hobbes does not spare the "
                  "sovereigns who let it happen either. They suffered it for want of "
                  "foresight, but &ldquo;may neverthelesse bee esteemed accessaries to their "
                  "own, and the Publique dammage&rdquo;, and once the people were possessed "
                  "there was &ldquo;no humane remedy&rdquo;."),
            ("p", "He then tells how the web was woven and how it unravels, &ldquo;the way is "
                  "the same, but the order is inverted&rdquo;. It began with the apostles, "
                  "obeyed &ldquo;out of Reverence, not by Obligation&rdquo;, whose "
                  "consciences were free. The first knot: the presbyters, as the flocks "
                  "grew, met to decide what to teach, bound themselves to teach nothing "
                  "against their decrees, and refused the company of the disobedient, which "
                  "was then called excommunication. The second: the presbyters of the chief "
                  "city of a province took authority over the others and the name of bishops. "
                  "The third and last: the bishop of Rome, by the imperial city, by the "
                  "emperors' wills and the title of Pontifex Maximus, and at last by the "
                  "privileges of St. Peter, took authority over all other bishops of the "
                  "empire. In England, he says, the knots came undone from the last: "
                  "Queen Elizabeth dissolved the pope's power, and the bishops thereafter "
                  "acted in the right of the queen, though they still said <em>jure "
                  "divino</em>. Then the Presbyterians put down episcopacy, and then their "
                  "power was taken from them, and &ldquo;we are reduced to the Independency "
                  "of the Primitive Christians to follow Paul, or Cephas, or Apollos, every "
                  "man as he liketh best&rdquo;. That, if without contention, he says, is "
                  "&ldquo;perhaps the best&rdquo;, since there should be no power over "
                  "consciences but the Word itself, and it is &ldquo;unreasonable in them, "
                  "who teach there is such danger in every little Errour, to require of a "
                  "man endued with Reason of his own, to follow the Reason of any other "
                  "man&rdquo;. When he wrote this, in the year of the book's printing, "
                  "England had been a Commonwealth since 1649, and the army that won the war "
                  "was largely Independent."),
            ("p", "And now the chapter's famous joke, which is the one light remark the Part "
                  "allows. The hierarchy, he says, may be compared &ldquo;not unfitly to the "
                  "Kingdome of Fairies&rdquo;, and the papacy &ldquo;is no other, than the "
                  "Ghost of the deceased Romane Empire, sitting crowned upon the grave "
                  "thereof&rdquo;. The Latin of the church is the ghost of the Roman language. "
                  "The fairies have one universal king, Oberon, whom Scripture calls "
                  "Beelzebub, and the ecclesiastics have one, the pope. Fairies inhabit "
                  "darkness, solitudes and graves, and ecclesiastics walk in obscurity of "
                  "doctrine, in monasteries and churchyards. Fairies cannot be brought to "
                  "answer for the hurt they do, and clergy vanish from the civil tribunals. "
                  "The fairies take cream from the dairies, and the clergy take donations and "
                  "tithes. He means it as an argument: as the fairies have no existence "
                  "but in the fancies of ignorant people, so the pope's spiritual power outside "
                  "his own dominion &ldquo;consisteth onely in the Fear that Seduced people "
                  "stand in, of their Excommunication&rdquo;. Whether you take it as satire "
                  "or as a summary of his case, the target is the hierarchy of Rome, and "
                  "that is why his Catholic readers did not find it funny."),
            ("p", "He ends the chapter with a warning, and it is not only about Rome. "
                  "That Henry VIII and Elizabeth cast the spirit out was &ldquo;not therefore "
                  "a very difficult matter&rdquo;, but it may return, or &ldquo;an Assembly "
                  "of Spirits worse than he&rdquo; may enter &ldquo;this clean swept "
                  "house&rdquo;, for it is not the Roman clergy only that pretends the "
                  "kingdom of God to be of this world. The next lesson, <em>A Review, and "
                  "Conclusion</em>, is the book's last."),
        ],
        "lab": ("levkit", {
            "mode": "canon",
            "view": "benefit",
            "preset": "all",
            "presets": _benefit([
                {"id": "all",
                 "label": "All fourteen doctrines",
                 "parties": "pope roman-clergy presbytery sovereign",
                 "doctrines": [{"doctrine": "church-is-kingdom", "benefits": "pope roman-clergy"},
                            {"doctrine": "resurrection-kingdom", "benefits": "presbytery"},
                            {"doctrine": "infallibility", "benefits": "pope"},
                            {"doctrine": "bishops-from-pope", "benefits": "pope"},
                            {"doctrine": "clergy-exemption", "benefits": "pope roman-clergy"},
                            {"doctrine": "sacerdotes-sacrifice", "benefits": "pope"},
                            {"doctrine": "marriage-sacrament", "benefits": "roman-clergy"},
                            {"doctrine": "priests-unmarried", "benefits": "pope"},
                            {"doctrine": "confession", "benefits": "roman-clergy"},
                            {"doctrine": "canonization", "benefits": "pope roman-clergy"},
                            {"doctrine": "priest-makes-christ", "benefits": "roman-clergy"},
                            {"doctrine": "purgatory-indulgences", "benefits": "roman-clergy"},
                            {"doctrine": "exorcism", "benefits": "roman-clergy"},
                            {"doctrine": "schoolmen", "benefits": "roman-clergy"}],
                 "expect": {"lcnCounts": "pope 7; roman-clergy 9; presbytery 1; sovereign 0", "lcnMost": "roman-clergy, 9 of 14 doctrines"}},
                {"id": "held",
                 "label": "The twelve doctrines that keep possession",
                 "parties": "pope roman-clergy presbytery sovereign",
                 "doctrines": [{"doctrine": "infallibility", "benefits": "pope"},
                            {"doctrine": "bishops-from-pope", "benefits": "pope"},
                            {"doctrine": "clergy-exemption", "benefits": "pope roman-clergy"},
                            {"doctrine": "sacerdotes-sacrifice", "benefits": "pope"},
                            {"doctrine": "marriage-sacrament", "benefits": "roman-clergy"},
                            {"doctrine": "priests-unmarried", "benefits": "pope"},
                            {"doctrine": "confession", "benefits": "roman-clergy"},
                            {"doctrine": "canonization", "benefits": "pope roman-clergy"},
                            {"doctrine": "priest-makes-christ", "benefits": "roman-clergy"},
                            {"doctrine": "purgatory-indulgences", "benefits": "roman-clergy"},
                            {"doctrine": "exorcism", "benefits": "roman-clergy"},
                            {"doctrine": "schoolmen", "benefits": "roman-clergy"}],
                 "expect": {"lcnCounts": "pope 6; roman-clergy 8; presbytery 0; sovereign 0", "lcnMost": "roman-clergy, 8 of 12 doctrines"}},
                {"id": "root",
                 "label": "The two doctrines that begin it",
                 "parties": "pope roman-clergy presbytery sovereign",
                 "doctrines": [{"doctrine": "church-is-kingdom", "benefits": "pope roman-clergy"},
                            {"doctrine": "resurrection-kingdom", "benefits": "presbytery"}],
                 "expect": {"lcnCounts": "pope 1; roman-clergy 1; presbytery 1; sovereign 0", "lcnMost": "pope and roman-clergy and presbytery, 1 of 2 doctrines each (a tie)"}},
            ]),
            "panel_title": "Which party do the doctrines serve",
            "panel_intro": (
                "Each doctrine is listed with the parties it benefits, as the lesson reads "
                "Hobbes's sentences. The lab counts the doctrines for each party and names the "
                "party served by the most. A count is not a measure of guilt, and a benefit "
                "is, for Hobbes, a presumption and not a proof."
            ),
        }),
        "steps_title": "Counting who a set of doctrines serves",
        "steps_intro": "Four steps, with one judgement in the first.",
        "steps": [
            ("Code the doctrines against the parties",
             "For each doctrine, write the parties Hobbes's sentence says it benefits. This "
             "is a reading, and a different reading gives a different table."),
            ("Count for each party",
             "Add one for every doctrine that names the party. Every doctrine weighs the "
             "same, however large the benefit."),
            ("Find the most served",
             "The party with the largest count comes first. List ties, and list any doctrine "
             "that benefits no one."),
            ("Say what the count is for",
             "It names a suspect. Whether a doctrine was devised for its benefit is a "
             "question of fact, and whether it is true is a question for Scripture and "
             "reason."),
        ],
        "worked": {
            "title": "Counting the twelve by hand",
            "intro": [
                "Take the <em>held</em> preset and count the pope's doctrines, then the Roman "
                "clergy's.",
            ],
            "lines": [
                "pope: infallibility, bishops, exemption",
                "pope, continued: sacerdotes, no marriage, canonization: 6",
                "clergy: exemption, marriage sacrament: 2",
                "clergy: confession, canonization, priest makes Christ: 5",
                "clergy: purgatory, exorcism, schoolmen: 8",
            ],
            "after": [
                "Exemption of the clergy from the civil laws is counted for both, since "
                "Hobbes says it serves the clergy and the pope's universal monarchy, and "
                "so is canonization, which he says assures their power by the pope's "
                "excommunication. Twelve doctrines produce fourteen entries for the two "
                "parties.",
            ],
        },
        "quiz_title": "What the count says and does not say",
        "quiz": [
            {"q": "On Hobbes's rule, what does benefit give you about who authored an act?",
             "a": ["Conclusive proof of who authored it",
                   "Nothing, since benefit is no evidence",
                   "A presumption, which he calls the plainest there is",
                   "Proof that the doctrine is false"],
             "c": 2,
             "why": "He says that among presumptions none so evidently declares the author as "
                    "the benefit of the action. A presumption is not proof, and it says "
                    "nothing yet about whether the doctrine is true."},
            {"q": "In the all preset, which party is served by the most doctrines?",
             "a": ["The pope", "The Roman clergy", "The Presbytery", "The sovereigns"],
             "c": 1,
             "why": "The Roman clergy are served by 9 of the fourteen, the pope by 7, the "
                    "Presbytery by 1 and the sovereigns by none. The count is on the "
                    "lesson's coding."},
            {"q": "What does the root preset report?",
             "a": ["A three-way tie: pope, Roman clergy and Presbytery, 1 each",
                   "The Presbytery, 2",
                   "The Roman clergy, 2",
                   "No party"],
             "c": 0,
             "why": "Rome's form of the doctrine serves the pope and the Roman clergy, and the "
                    "form kept by the Presbytery serves the Presbytery. That makes one each, "
                    "which is Hobbes's pairing of the two clergies."},
            {"q": "Which of Hobbes's three knots was tied last, and so, in his account of "
                  "England, was untied first?",
             "a": ["The presbyters' power to excommunicate",
                   "The title of bishop for the presbyters of a chief city",
                   "The Bishop of Rome's authority over all other bishops",
                   "The independency of the primitive Christians"],
             "c": 2,
             "why": "The third and last knot was the bishop of Rome's authority over other "
                    "bishops, and the first to be untied in England was the pope's power, "
                    "dissolved totally by Queen Elizabeth."},
        ],
        "mistakes": [
            ("Treating cui bono as proof of authorship",
             "Hobbes calls benefit a presumption. The count in the lab names who the doctrines "
             "served, and a doctrine can serve someone and be true. He also blames the "
             "sovereigns who let it happen, as accessaries, for want of foresight, which "
             "is a different charge from authorship."),
            ("Thinking the count shows that Hobbes spares the Presbytery",
             "The Presbytery's count, 1, is small in the <em>all</em> preset because the twelve "
             "doctrines he lists are Rome's. He names the Presbyterian clergy, with the "
             "Roman, as authors of the darkness, and says the same doctrine of the kingdom "
             "was kept where they took the office."),
            ("Reading the count as a measure of guilt",
             "Every doctrine weighs one, whatever its benefit, and the table is the lesson's "
             "reading of Hobbes's sentences, not his. He does not count. The figure shows "
             "how his list divides among the parties, and the weights are for the reader to "
             "argue."),
        ],
        "standard": (
            "Finish when you can count a list of doctrines against the parties it serves.",
            "Given a list of doctrines and the parties each benefits, count the doctrines "
            "for each party, name the party served by the most, and say what the count does "
            "and does not show."
        ),
        "note": (
            "The count follows from the coding the lesson makes of Hobbes's sentences, and "
            "from nothing else. It cannot say that a benefit shows authorship, which is "
            "Hobbes's presumption, or that the doctrines are false, which he argues from "
            "Scripture, and the defenders of the church argued otherwise."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Leviathan, A Review, and Conclusion, 1651 p. 390; PDF p. 580 of the operator's
    # copy (the opening quotation); 1651 pp. 389-396, PDF pp. 579-587.
    {
        "slug": "review-and-conclusion",
        "title": "A Review, and Conclusion",
        "module": "A Review, and Conclusion",
        "one_line": "Hobbes adds a law of nature, that every man must protect in war the authority that protects him in peace, and ends the book on protection and obedience.",
        "summary": (
            "The Review and Conclusion answers the charge that no man can have the faculties civil "
            "duty needs, adds a last law of nature, says when a subject may submit to a "
            "conqueror and what conquest is, and ends where the book began, on the mutual "
            "relation between protection and obedience. Compute it as a covenant in which the "
            "sovereign performs first, with a stated sword behind it: when the subject does "
            "better to obey, the least sword that makes it so, and what changes when "
            "protection fails."
        ),
        "key": [
            "added law: protect in war who protects you",
            "keep = protection − cost of obeying",
            "break = protection − chance × penalty",
            "least penalty = cost of obeying / chance",
            "conquered: submitted, for life and liberty",
            "no protection, no obligation to obey",
        ],
        "key_label": "Protection and obedience in six lines",
        "concepts_intro": (
            "The Review has the loose form of a postscript, and three ideas carry it."
        ),
        "concepts": [
            ("The added law of nature",
             "To the laws of Chapter 15 Hobbes would add that every man is bound by nature, as "
             "much as in him lies, to protect in war the authority by which he is himself "
             "protected in peace. His reason is that to claim a right of nature to preserve "
             "his own body and a right to destroy the one by whose strength it is preserved "
             "is a contradiction."),
            ("Conquest and submission",
             "Conquest is not the victory, but the right over persons that the victor "
             "acquires by it. He who is slain is overcome and not conquered, and so is he "
             "who is chained. He who has his life and liberty allowed him on a promise of "
             "obedience is conquered and a subject. A subject may submit when he has liberty "
             "to, which is when the means of his life are within the enemy's guards and "
             "garrisons."),
            ("The contrary faculties",
             "Some had argued that no one man can have all that civil duty needs, judgment "
             "and fancy, reason and eloquence, courage and fear of the laws. Hobbes grants "
             "the difficulties and denies the impossibility: education and discipline "
             "reconcile them, in turns, as the end requires."),
        ],
        "read_title": "The passage first, then the Review",
        "read_intro": (
            "The passage is the added law. The lesson reads the Review in Hobbes's order, "
            "computes the covenant of protection and obedience in the lab, and then reads "
            "what he says about conquest, about the book and about the universities, and "
            "ends with the book's last sentence."
        ),
        "body": [
            ("p", "<strong>A Review, and Conclusion.</strong> &ldquo;To the Laws of Nature, "
                  "declared in the 15. Chapter, I would have this added, That every man is "
                  "bound by Nature, as much as in him lieth, to protect in Warre, the "
                  "Authority, by which he is himself protected in time of Peace. For he that "
                  "pretendeth a Right of Nature to preserve his owne body, cannot pretend a "
                  "Right of Nature to destroy him, by whose strength he is preserved: It is a "
                  "manifest contradiction of himselfe.&rdquo;"),
            ("p", "Hobbes begins the Review with an objection, not with the law. From the "
                  "contrariety of the natural faculties of the mind and of the passions, "
                  "&ldquo;there has been an argument taken, to inferre an impossibility that "
                  "any one man should be sufficiently disposed to all sorts of Civill duty&rdquo;. "
                  "Severity of judgment makes men censorious and slow to pardon, and quickness of "
                  "fancy makes thought unsteady. Reason is needed in every deliberation, and "
                  "eloquence to carry it, and they are contrary, one resting on truth and the "
                  "other on opinion and passion. Courage inclines to private revenge, and "
                  "timorousness to desert the public defence. And the business of the world is "
                  "a perpetual contention for honour, riches and authority. His answer: these "
                  "are &ldquo;great difficulties, but not Impossibilities&rdquo;, for by "
                  "education and discipline they are sometimes reconciled. Judgment and fancy "
                  "may share a man by turns, like the Israelites in Egypt, some days fixed to "
                  "making bricks and others ranging to gather straw. And he gives an instance: "
                  "his friend Sidney Godolphin, in whom he saw clear judgment with a wide "
                  "fancy, strong reason with graceful speech, courage for war and a fear for "
                  "the laws, &ldquo;who hating no man, nor hated of any, was unfortunately "
                  "slain in the beginning of the late Civill warre&rdquo;."),
            ("p", "Now the law. He says it may be drawn by consequence from the laws already "
                  "given, &ldquo;yet the Times require to have it inculcated, and "
                  "remembered&rdquo;. Read it as a covenant. In Chapter 17 the subjects covenant "
                  "with one another to give their power to a sovereign, who in return protects. "
                  "Protection and obedience are the two sides, and Hobbes's last sentences of "
                  "the book will name them so. If the sovereign protects first, the subject's "
                  "question is whether obeying is worth what it costs him, and whether "
                  "the sword makes it so."),
            ("p", "The lab is a covenant between the sovereign, who performs first, and a subject. "
                  "Protection is worth 10 to the subject, and obeying costs him 3, in contributions "
                  "and service. It costs the sovereign 4 to protect, and he gets 6 from "
                  "obedience. The sword is a penalty of 6 applied with a chance of one in two. "
                  "That is the <em>protected</em> preset. Keeping is 10 minus 3, which is 7. "
                  "Breaking is 10 minus half of 6, which is 7: the subject keeps the "
                  "protection and pays the penalty on average half the time, so the lab "
                  "calls it level and keeps, by its rule for ties. The least penalty "
                  "that makes keeping at least as good is 3 divided by one half, which is 6. "
                  "And the sovereign, who gets 6 and pays 4, is 2 ahead for protecting first."),
            ("p", "Weaken the sword and the answer turns. In <em>weak-sword</em> the penalty is 4 "
                  "at the same chance. Breaking is 10 minus 2, which is 8, against 7 for "
                  "keeping, so the subject does better to break, and the sovereign who "
                  "protected first and was not obeyed is 4 behind. This is the old argument "
                  "of Chapter 17, with the sovereign in the place of the first party to "
                  "perform: without a power that makes breach cost more than keeping, "
                  "covenants are but words. And in <em>failed</em> the protection has "
                  "gone, worth nothing to the subject, while the sword is as before but "
                  "reaches him one time in ten. Keeping is minus 3, breaking is minus "
                  "three fifths, and the least penalty that would make him obey is 30. "
                  "That is the case Hobbes treats: &ldquo;he hath no longer Protection from "
                  "him, but is protected by the adverse party for his Contribution&rdquo;. The "
                  "lab does not say he is released, only that obeying has become a cost and "
                  "nothing more. Hobbes's word is that he has then the liberty to submit. The "
                  "sovereign's tiles still show him paying 4 for protection that is worth "
                  "nothing to the subject: that is the lab's way of saying the first "
                  "performance has failed, and why the subject's obligation is in question."),
            ("p", "That was the question of the day. Hobbes writes that he finds by many English "
                  "books lately printed that the civil wars &ldquo;have not yet sufficiently "
                  "taught men, in what point of time it is, that a Subject becomes obliged to "
                  "the Conquerour&rdquo;. After the king's execution in 1649 the new "
                  "republic asked men, in 1650, to promise to be faithful to it, and printed "
                  "books argued over whether a man could in conscience. Hobbes's "
                  "answer is the point in time &ldquo;wherein having liberty to submit to "
                  "him, he consenteth, either by expresse words, or by other sufficient "
                  "sign, to be his Subject&rdquo;. A man has the liberty when he has no "
                  "obligation to his former sovereign beyond that of an ordinary subject and "
                  "&ldquo;the means of his life is within the Guards and Garrisons of the "
                  "Enemy&rdquo;. A soldier, who has taken a new obligation, has not that "
                  "liberty while his old sovereign keeps the field and gives him his "
                  "subsistence, but when that fails &ldquo;a Souldier also may seek his "
                  "Protection wheresoever he has most hope to have it&rdquo;. And what he then "
                  "promises he must keep: &ldquo;a Contract lawfully made, cannot lawfully be "
                  "broken&rdquo;."),
            ("p", "What conquest is, he then says, is a matter of definition. &ldquo;Conquest, is "
                  "not the Victory it self; but the Acquisition by Victory, of a Right, over "
                  "the persons of men.&rdquo; He who is slain is overcome but not conquered, "
                  "and a man in chains is still an enemy and may save himself if he can. "
                  "The Romans said a province was pacified when its people promised to do what "
                  "the Roman people commanded. A man who lives openly under the "
                  "victor's protection is understood to submit, and one who lives there "
                  "secretly may justly be put to death as a spy, though Hobbes adds that he does "
                  "no injustice, for acts of open hostility do not bear that name. His "
                  "definition: the right of sovereignty by victory, acquired in the people's "
                  "submission, &ldquo;by which they contract with the Victor, promising "
                  "Obedience, for Life and Liberty&rdquo;. This is the covenant of Chapter 20, "
                  "and it is the lab's covenant too: protection, for the vanquished, is life "
                  "and liberty, and obeying is the cost. The numbers are the lesson's; "
                  "Hobbes's claim is that an obligation made from fear is an obligation."),
            ("p", "He adds two more cautions in the same spirit. Sovereignties, he says, "
                  "weaken when their holders rest their right on the justice of the war that "
                  "won it, and not on possession, or require approval of all they did, because "
                  "then they justify every later rebellion that is successful: &ldquo;there is scarce a Common-wealth in the world, "
                  "whose beginnings can in conscience be justified&rdquo;. And to tolerate "
                  "a professed hatred of tyranny is to tolerate a hatred of commonwealth in "
                  "general, since tyranny is only the name of sovereignty said by someone "
                  "angry with it. Both are arguments that the right of a sovereign "
                  "rests on possession and submission, not on the goodness of the cause, and "
                  "that is where his critics from both sides, those who held the king's "
                  "right to be from God and those who held the people's to be from their "
                  "consent, parted from him."),
            ("p", "Then the Review looks back at Part III. He had left out who were to "
                  "execute capital punishments in the kingdom of God, and says that the law "
                  "in Israel was that the people should stone the convicted, the witnesses "
                  "throwing first. It was a law that appointed the executioners, not a license for "
                  "anyone to throw before conviction and sentence, and he goes through the "
                  "texts, the Levites and the golden calf, Phinehas, the blasphemer kept in "
                  "custody, to show that none supports a private right of zeal. Of the manner "
                  "in which God spoke to Moses he says only that the difference from other "
                  "prophets is not declared, unless it lies in the clearness of the "
                  "vision."),
            ("p", "And then Hobbes judges his own book. &ldquo;I see not yet, but the "
                  "Principles of it are true and proper; and the Ratiocination solid&rdquo;, "
                  "since he grounds the civil right of sovereigns and the duty and liberty of "
                  "subjects on the known natural inclinations of mankind and the laws "
                  "of nature, and the sovereign's ecclesiastical power on texts evident in "
                  "themselves. A reader who wants only to be informed will be, he says. Those "
                  "who have engaged themselves to contrary opinions, &ldquo;it is naturall "
                  "for men, at one and the same time, both to proceed in reading, and to "
                  "lose their attention, in the search of objections&rdquo;. He admits the "
                  "doctrines in Part III are new, and that in a state where the contrary was "
                  "settled it would be wrong for a subject to teach them without leave, but "
                  "now, when men call for truth as well as peace, to offer them is &ldquo;to "
                  "offer New Wine, to bee put into New Cask, that both may be preserved "
                  "together&rdquo;."),
            ("p", "He apologises for something else, and gives reasons. He has not decorated "
                  "his book with quotations from the ancients, as was the fashion, and he "
                  "says why in eight points, among them that truth depends on reason or "
                  "Scripture, which give credit to many writers and receive it from none, "
                  "that the ancients contradict each other, and that quotations unchewed "
                  "are a sign of indigestion. And the last: &ldquo;if we will reverence the "
                  "Age, the Present is the Oldest&rdquo;, and the praise of ancient authors "
                  "&ldquo;proceeds not from the reverence of the Dead, but from the "
                  "competition, and mutuall envy of the Living&rdquo;."),
            ("p", "He thinks the book might &ldquo;profitably&rdquo; be taught in the "
                  "universities, if those who judge of it agree, because the universities are "
                  "the fountains of civil and moral doctrine, and there should be great care "
                  "to have it pure &ldquo;both from the Venime of Heathen Politicians, and "
                  "from the Incantation of Deceiving Spirits&rdquo;. Then the last "
                  "paragraph: his discourse of civil and ecclesiastical government, "
                  "&ldquo;occasioned by the disorders of the present time&rdquo;, was written "
                  "&ldquo;without partiality, without application, and without other "
                  "designe, than to set before mens eyes the mutuall Relation between "
                  "Protection and Obedience&rdquo;. He goes back to his interrupted "
                  "speculation of natural bodies, hoping that its novelty will please as "
                  "much as that of the artificial body has offended: &ldquo;For such Truth, as "
                  "opposeth no mans profit, nor pleasure, is to all men welcome&rdquo;. "
                  "The book was printed in London that year, and Hobbes came home from Paris "
                  "at the end of it."),
            ("p", "That is where Hobbes stops, and where the read-along stops with him. In "
                  "nine courses every figure was a figure of what follows from a "
                  "definition, a payoff or a count that a lesson stated: what a name is the sum "
                  "of, what a covenant is worth with and without a sword, what an assembly's "
                  "voices decide, who a doctrine serves. None of them said whether men "
                  "are as Hobbes says they are, and the last lab is no different. The "
                  "book's own final claim is that protection and obedience stand or fall "
                  "together, and that is for each reader to weigh against the commonwealths "
                  "he knows."),
        ],
        "lab": ("levkit", {
            "mode": "covenant",
            "view": "perform",
            "preset": "protected",
            "presets": [
                {"id": "protected",
                 "first": "sovereign", "second": "subject",
                 "label": "Protection worth 10, obeying costs 3, a penalty of 6 at one chance in two",
                 "cost1": 4, "gain1": 6, "cost2": 3, "gain2": 10,
                 "sanction": 6, "certainty": "1/2",
                 "expect": {"lcvKeep": "7", "lcvBreak": "7", "lcvChoice": "subject keeps: 7 against 7 (equal; the tie rule keeps)", "lcvLeast": "6 (cost2 ÷ certainty)"}},
                {"id": "weak-sword",
                 "first": "sovereign", "second": "subject",
                 "label": "The same, with a penalty of only 4",
                 "cost1": 4, "gain1": 6, "cost2": 3, "gain2": 10,
                 "sanction": 4, "certainty": "1/2",
                 "expect": {"lcvKeep": "7", "lcvBreak": "8", "lcvChoice": "subject breaks: 8 against 7", "lcvLeast": "6 (cost2 ÷ certainty)"}},
                {"id": "failed",
                 "first": "sovereign", "second": "subject",
                 "label": "Protection has failed: worth nothing, the penalty reaches one time in ten",
                 "cost1": 4, "gain1": 6, "cost2": 3, "gain2": 0,
                 "sanction": 6, "certainty": "1/10",
                 "expect": {"lcvKeep": "−3", "lcvBreak": "−3/5 = −0.60", "lcvChoice": "subject breaks: −3/5 = −0.60 against −3", "lcvLeast": "30 (cost2 ÷ certainty)"}},
            ],
            "panel_title": "When does the subject do better to obey",
            "panel_intro": (
                "A covenant between a sovereign who protects first and a subject who obeys. The "
                "lab compares the subject's payoff for keeping with his payoff for breaking, "
                "given the penalty and the chance it is applied, and says whether the sovereign "
                "does well to protect first. The numbers are the lesson's, not Hobbes's."
            ),
        }),
        "steps_title": "Computing protection against obedience",
        "steps_intro": "Five steps, the same for any covenant in which one party performs first.",
        "steps": [
            ("State what each side gives and gets",
             "Write what protection is worth to the subject, what obeying costs him, and "
             "what protecting costs the sovereign and brings him."),
            ("State the sword",
             "Write the penalty for breach and the chance it is applied. With no penalty "
             "the covenant is in the condition of mere nature."),
            ("Compare keeping with breaking",
             "Keeping pays protection minus the cost of obeying. Breaking pays protection "
             "minus the chance times the penalty. Say how ties go."),
            ("Find the least penalty",
             "The cost of obeying divided by the chance gives the least penalty that makes "
             "keeping at least as good. It does not exist when the chance is zero."),
            ("Set protection to nothing",
             "Run the same sword with protection gone and see what obeying is then worth. "
             "This is the case Hobbes treats as the liberty to submit."),
        ],
        "worked": {
            "title": "The protected case by hand",
            "intro": [
                "Take the first preset: protection 10, obeying costs 3, penalty 6, chance one "
                "in two, and the sovereign's cost 4 against a return of 6.",
            ],
            "lines": [
                "keep:  10 − 3 = 7",
                "break:  10 − (1/2)(6) = 7, level",
                "least penalty:  3 / (1/2) = 6",
                "sovereign protects first:  6 − 4 = 2",
                "penalty 4:  break 8 against keep 7",
            ],
            "after": [
                "At a penalty of 6 the subject is indifferent, and the lab's rule for a "
                "tie keeps. Anything below 6 at this chance makes breach the better choice, "
                "and the sovereign loses by protecting first.",
            ],
        },
        "quiz_title": "Protection, obedience and conquest",
        "quiz": [
            {"q": "In the first preset obeying costs 3 and a penalty is applied with chance "
                  "one half. What is the least penalty that makes keeping at least as good as "
                  "breaking?",
             "a": ["3", "4", "6", "10"],
             "c": 2,
             "why": "The least penalty is the cost of obeying divided by the chance, "
                    "3 / (1/2) = 6. At 3 the expected penalty is only 3/2, which is "
                    "less than the cost of obeying. At 4, the expected penalty is 2, still short."},
            {"q": "According to Hobbes, when does a man become subject to a conqueror?",
             "a": ["When, having liberty to submit, he consents by express words or "
                   "other sufficient sign",
                   "As soon as the conqueror has won the battle",
                   "When he is taken prisoner and put in chains",
                   "When he is slain"],
             "c": 0,
             "why": "Conquest is not the victory but the acquisition by victory of a right "
                    "over persons. He that is slain is overcome and not conquered, and a "
                    "prisoner in chains is still an enemy."},
            {"q": "Why does Hobbes say every man is bound by nature to protect in war "
                  "the authority that protects him in peace?",
             "a": ["Because the sovereign is God's lieutenant",
                   "Because to claim a right of nature to preserve his body and a right to "
                   "destroy him by whose strength it is preserved is a contradiction",
                   "Because the sword always makes obedience pay",
                   "Because the law of nature is written in Scripture"],
             "c": 1,
             "why": "The reason he gives is the contradiction in &ldquo;a Right of Nature to "
                    "preserve his owne body&rdquo; together with a right to destroy the one by "
                    "whose strength it is preserved. He gives no reason from the sword or "
                    "from Scripture."},
        ],
        "mistakes": [
            ("Thinking a subject owes obedience to whoever wins",
             "Conquest is the acquisition of a right over persons by victory, and it is "
             "made in the people's submission, not in the fighting. The slain are overcome "
             "and not conquered, a prisoner is still an enemy, and the lab's covenant is "
             "the promise of obedience for life and liberty."),
            ("Reading the added law as making obedience unconditional",
             "The law binds a man to protect the authority that protects him. When the "
             "means of his life are within the enemy's garrisons and his sovereign no longer "
             "protects him, the ordinary subject has liberty to submit, and the lab's "
             "<em>failed</em> preset shows obeying then a bare cost. A soldier keeps his "
             "obligation while his old sovereign keeps the field and supports him."),
            ("Reading the lab's numbers as Hobbes's account of men",
             "Protection worth 10, obedience costing 3 and a penalty of 6 are the lesson's. "
             "They show how the covenant divides when its figures are those. Hobbes gives no "
             "figures, and says the obligation rests on the contradiction in claiming the "
             "benefit of protection while destroying the protector."),
        ],
        "standard": (
            "Finish when you can say when a subject does better to obey and what failed "
            "protection changes.",
            "Given what protection is worth, what obeying costs and a stated penalty and "
            "chance, say whether the subject does better to keep or break, find the "
            "least penalty that makes keeping at least as good, and say what happens when "
            "protection is worth nothing."
        ),
        "note": (
            "The lab compares two payoffs on figures the lesson invents. It cannot say "
            "whether obligation is a matter of payoff, which Hobbes denies, or what a subject "
            "should do when the sovereign's claim and his protection part, which the "
            "Engagement made a live question and which he answers for his own time. Whether "
            "the book's claim, that protection and obedience stand together, holds for any "
            "commonwealth is what it argues and its critics dispute."
        ),
    },
]
