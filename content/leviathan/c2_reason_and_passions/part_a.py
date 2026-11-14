"""Reason, Science and the Passions, lessons 1-4 -- Chapters 5 and 6.

Every quotation is Hobbes's text of 1651 as printed in the operator's copy;
the comment beside each lesson gives the chapter, the 1651 page and the PDF page.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Leviathan ch. 5, 1651 p. 18; PDF p. 127 of the operator's copy (opening
    # quotation, which runs on to PDF p. 128); the definition of reason is on
    # 1651 p. 18-19 (PDF p. 128), the arbitrator on PDF pp. 128-129.
    {
        "slug": "reason-is-reckoning",
        "title": "Reason Is Reckoning",
        "module": "Chapter 5 · Of Reason, and Science",
        "one_line": "Hobbes says to reason is to add and subtract names, a syllogism is two affirmations added, and no one's reasoning is right reason because he is the one doing it.",
        "summary": (
            "Chapter 5 begins with a definition that sounds like a slogan and is meant "
            "as a method: reasoning is reckoning with general names, as arithmetic is "
            "reckoning with numbers. Test a valid and an invalid syllogism two ways, "
            "Hobbes's way by adding the names and the lab's way by counting the regions "
            "a premise leaves open, and see why he thinks the agreed reckoner, not the "
            "confident one, settles a dispute."
        ),
        "key": [
            "reasoning = adding and subtracting names",
            "two names make an affirmation",
            "two affirmations make a syllogism",
            "valid: no case keeps premises, drops it",
            "no one's reason is right reason",
        ],
        "key_label": "Chapter 5, first half, in five lines",
        "concepts_intro": (
            "The chapter opens by making reason sound like a trade skill, and then "
            "spends several pages on who is entitled to say that a reckoning is right."
        ),
        "concepts": [
            ("Reasoning as reckoning",
             "A man who reasons &ldquo;does nothing else&rdquo; than conceive a sum from "
             "the addition of parcels, or a remainder from the subtraction of one sum "
             "from another. Done in words, it runs from the names of the parts to the "
             "name of the whole, or from the whole and one part to the other part. "
             "Multiplication and division are the same two operations repeated."),
            ("The ladder of reckoning",
             "Two names added make an affirmation, two affirmations added make a "
             "syllogism, and many syllogisms added make a demonstration. Politics and "
             "law are reckoning too: Hobbes says writers of politics add pacts to find "
             "men's duties, and lawyers add laws and facts to find what is right and "
             "wrong."),
            ("Right reason without a judge",
             "Reason itself is always right, as arithmetic is infallible, but no one "
             "person's reasoning, and no number of people's, is therefore right. Where "
             "there is a dispute the parties must agree on an arbitrator, or the "
             "dispute ends in blows or is left undecided."),
        ],
        "read_title": "The passage first, then the chapter line by line",
        "read_intro": (
            "The chapter opens on the sentence that gives the whole book its method. "
            "After that Hobbes widens it, defines reason, and turns on the people who "
            "claim to have it."
        ),
        "body": [
            ("p", "<strong>Chapter 5.</strong> &ldquo;When a man Reasoneth, hee does "
                  "nothing else but conceive a summe totall, from Addition of parcels; or "
                  "conceive a Remainder, from Substraction of one summe from another&rdquo;"),
            ("p", "You have done this at a restaurant table. The bill comes, someone "
                  "adds it up, someone else checks the addition, and in the end it either "
                  "comes to the same total or it does not. Hobbes thinks that is what "
                  "thinking is, all of it, once it is done in words. It is a very "
                  "deflating claim. Reason on this account is not a light in the mind or "
                  "a window onto the way things are. It is bookkeeping, and the books are "
                  "kept in names."),
            ("p", "Read the rest of his sentence slowly. Done in words, reckoning is "
                  "conceiving of the consequence &ldquo;from the names of all the parts, "
                  "to the name of the whole&rdquo;, or from the whole and one part to the "
                  "name of the other. A square is a figure with four sides, right angles "
                  "and equal sides, so from the three names you reach the one, and from "
                  "<em>square</em> and <em>four-sided</em> you may subtract your way back "
                  "to the right angles and the equal sides. And Hobbes does not stop at "
                  "numbers: &ldquo;Multiplication, is but Adding together of things "
                  "equall&rdquo;, and the same two operations run in lines and angles, in "
                  "force and power. &ldquo;Writers of Politiques, adde together "
                  "Pactions, to find mens duties&rdquo;. That sentence is a plan for the "
                  "rest of the book, which adds covenants to find duties."),
            ("p", "Then comes the definition, and each phrase of it does a job. "
                  "Reason is &ldquo;Reckoning (that is, Adding and Substracting) of the "
                  "Consequences of generall names agreed upon, for the marking and "
                  "signifying of our thoughts&rdquo;. The reckoning is of "
                  "<em>consequences</em>, what follows from what, not of facts. The names "
                  "are <em>general</em>, so reasoning is about kinds and not about this "
                  "man or that. And they are &ldquo;agreed upon&rdquo;: the reckoning is "
                  "only as good as the settled meanings it starts from, which is why the "
                  "next lesson is about what goes wrong when they are not settled. The "
                  "last clause says what the reckoning is for. When you reason alone you "
                  "are &ldquo;marking&rdquo; your thoughts, and when you reason with "
                  "others you are &ldquo;signifying&rdquo; them, showing your sums so that "
                  "they can be checked."),
            ("def", ("Syllogism, as two affirmations added",
                     "Hobbes says two affirmations are added; the cancelling of the middle name is the lab's picture of it, not his. In <em>All Greeks are men</em> and <em>All "
                     "men are mortal</em> the name <em>man</em> comes at the end of the "
                     "first and the start of the second; add them and it drops out, and "
                     "what is left is <em>All Greeks are mortal</em>.")),
            ("p", "The lab checks syllogisms by a method that is not Hobbes's but "
                  "agrees with him about every case in this lesson. Each statement says "
                  "that some region of a Venn diagram is empty or occupied, and an "
                  "argument is valid if no way of filling the diagram keeps the premises "
                  "and loses the conclusion. Take the barbara preset, which is the Greek "
                  "example: all men are mortal, all Greeks are men, so all Greeks are "
                  "mortal. No filling of the diagram keeps both premises and puts a Greek "
                  "outside the mortals, so it is valid, and the form is the one the "
                  "textbooks call Barbara. The celarent preset, no reptiles are "
                  "warm-blooded and all snakes are reptiles, so no snakes are "
                  "warm-blooded, is the negative form of the same sum, and the darii "
                  "preset puts a <em>some</em> in the second premise: all poets are "
                  "vain, some kings are poets, so some kings are vain."),
            ("p", "Now the failure. In the undistributed preset the premises are all "
                  "cats are mammals and all dogs are mammals, and the offered conclusion is "
                  "that all dogs are cats. Both premises are true, and the argument is "
                  "plainly bad: the lab finds a filling of the diagram in which dogs sit "
                  "outside the cats. In Hobbes's terms the two affirmations share a name, "
                  "<em>mammal</em>, but it stands at the end of both, so there is nothing "
                  "to cancel and no sum to take. And his remark about subtraction can be turned to explain "
                  "why the failure tempts people: from a conclusion and one premise a "
                  "logician may &ldquo;substract one Proposition, to finde the other&rdquo;, "
                  "but what the subtraction finds is the premise that would be needed, not "
                  "one that follows. Take the conclusion all Greeks are mortal and the "
                  "premise all cats are mortal, hunt for the missing step, and you are "
                  "tempted by all Greeks are cats."),
            ("p", "Hobbes's own caution comes straight after the definition, and it is "
                  "the part of the chapter with a story behind it. By 1651 England had "
                  "had a civil war, a king tried and beheaded, and a good many parties "
                  "each certain that the right thing was plain to anyone who reasoned "
                  "properly. Hobbes grants that Reason is always right, &ldquo;as well as "
                  "Arithmetique is a certain and infallible Art&rdquo;. But &ldquo;no one "
                  "mans Reason, nor the Reason of any one number of men, makes the "
                  "certaintie&rdquo;, any more than an account is well cast up because a "
                  "great many men have unanimously approved it. A disputed account is "
                  "settled when the parties &ldquo;set up for right Reason, the Reason of "
                  "some Arbitrator, or Judge&rdquo;; if they will not, they come to blows or "
                  "leave it undecided. And the man who demands right reason as judge, "
                  "while meaning only his own, is doing what a card player does who uses "
                  "&ldquo;for trump on every occasion, that suite whereof they have most "
                  "in their hand&rdquo;. He is calling his passions reason, and the claim "
                  "itself, Hobbes says, betrays his want of it."),
            ("p", "There are two standard objections, and both have strength. The "
                  "first comes from the natural-law tradition he was writing against: "
                  "that reason is the same faculty in every person and gives each of us "
                  "access to what is right without anyone's say-so, so that an arbitrator "
                  "is a convenience and not a source of authority. Hobbes's answer is in his "
                  "own comparison: reason is not at fault, but a reckoner may cast up "
                  "false, and only a judge the parties have agreed on can say which sum "
                  "stands. The second is an objection to reasoning as "
                  "reckoning: in 1847 Augustus De Morgan pointed out that the old "
                  "syllogism cannot show that if a horse is an animal then the head of a "
                  "horse is the head of an animal, because the argument turns on a "
                  "relation and not on one name containing another. The lab shares that "
                  "limit, since it can only count regions of kinds."),
            ("p", "Hobbes closes the point by separating two ways of going wrong. "
                  "<strong>Error</strong> is &ldquo;a deception, in presuming that somewhat "
                  "is past, or to come&rdquo;, when it might have been otherwise: you "
                  "expected rain and it stayed dry. <strong>Absurdity</strong> is what "
                  "happens when a general assertion is not true, for then, as he puts "
                  "it, &ldquo;the possibility of it is unconceivable&rdquo;; he speaks of "
                  "&ldquo;a round Quadrangle&rdquo; and says such a man is not mistaken but "
                  "has said nothing. Words &ldquo;whereby we conceive nothing but the "
                  "sound&rdquo; are the ones he calls absurd, insignificant and "
                  "nonsense. He adds a barb about the people who ought to know better. "
                  "Cicero said, and Hobbes agrees, that &ldquo;there can be nothing so "
                  "absurd, but may be found in the books of Philosophers&rdquo;, because, "
                  "he says, not one of them begins from definitions, as geometers do."),
            ("p", "A last point makes the arithmetic honest. The master of a family "
                  "who adds up all the bills of expense without checking how each was "
                  "made up, Hobbes says, &ldquo;advantages himself no more, than if he "
                  "allowed the account in grosse&rdquo;. A conclusion is certain only if "
                  "every affirmation under it is, which is why he tells the reader to go "
                  "back to the definitions. The next lesson, <em>Absurdity and "
                  "Science</em>, lists the seven ways he thinks philosophers lose their "
                  "footing, and gives you a vocabulary with which to say which names "
                  "cannot be added."),
        ],
        "lab": ("argkit", {
            "mode": "syllogism",
            "preset": "barbara",
            "import": "boolean",
            "presets": [
                {"id": "barbara", "label": "All men are mortal; all Greeks are men",
                 "premises": ["All men are mortal", "All Greeks are men"],
                 "conclusion": "All Greeks are mortal", "expect": {"syVerdict": "Valid", "syForm": "AAA-1 Barbara", "syModels": "16", "syCounter": "none"}},
                {"id": "celarent", "label": "No reptiles are warm-blooded; all snakes are reptiles",
                 "premises": ["No reptiles are warm-blooded", "All snakes are reptiles"],
                 "conclusion": "No snakes are warm-blooded", "expect": {"syVerdict": "Valid", "syForm": "EAE-1 Celarent", "syModels": "16", "syCounter": "none"}},
                {"id": "darii", "label": "All poets are vain; some kings are poets",
                 "premises": ["All poets are vain", "Some kings are poets"],
                 "conclusion": "Some kings are vain", "expect": {"syVerdict": "Valid", "syForm": "AII-1 Darii", "syModels": "32", "syCounter": "none"}},
                {"id": "undistributed", "label": "All cats are mammals; all dogs are mammals",
                 "premises": ["All cats are mammals", "All dogs are mammals"],
                 "conclusion": "All dogs are cats", "expect": {"syVerdict": "Invalid", "syForm": "AAA-2 (no name)", "syModels": "32", "syCounter": "D+M"}},
            ],
            "panel_title": "Is the sum of the two affirmations the conclusion?",
            "panel_intro": (
                "Each preset gives two affirmations and a conclusion. The lab asks "
                "whether any way of filling a Venn diagram keeps both premises and "
                "loses the conclusion. Run the four presets in order, then retype a "
                "term in the invalid one and see what it takes to make it valid."
            ),
        }),
        "steps_title": "Testing a syllogism",
        "steps_intro": "Four steps, whether you add the names or draw the regions.",
        "steps": [
            ("Name the three terms",
             "A syllogism has a subject, a predicate and a middle term that appears in "
             "both premises and not in the conclusion. Write each as a plain word."),
            ("Add the premises through the middle",
             "The middle term must end one affirmation and begin the other, or be "
             "contained in a way that lets it drop out. If it ends both, or begins "
             "both, there is nothing to cancel."),
            ("Read off what the sum says",
             "Say in a sentence what joining the premises tells you about the subject "
             "and predicate, and compare it with the conclusion offered."),
            ("Look for a case that keeps the premises and loses the conclusion",
             "Describe a world in which both premises are true and the conclusion is "
             "false. If you can, the argument is invalid. If you cannot, it is valid."),
        ],
        "worked": {
            "title": "Greeks, men and mortals, and then cats and dogs",
            "intro": [
                "Take the two stock examples side by side, the valid first and the "
                "invalid second. In each, work from the premises to what they add up to.",
            ],
            "lines": [
                "All Greeks are men, all men are mortal",
                "man ends the first and starts the second: it drops out",
                "the sum: All Greeks are mortal",
                "All cats are mammals, all dogs are mammals",
                "mammal ends both: nothing drops out, no sum",
                "the offered All dogs are cats: no reason, so invalid",
            ],
            "after": [
                "The lab confirms both by counting. In the second argument it shows a "
                "diagram in which every cat and every dog is a mammal, and the dogs sit "
                "outside the cats.",
            ],
        },
        "quiz_title": "Reasoning as reckoning",
        "quiz": [
            {"q": "How does Hobbes define reason in Chapter 5?",
             "a": ["A faculty by which each person sees what is right without anyone's say-so",
                   "The reckoning of the consequences of general names agreed upon",
                   "The ability to remember what has happened and presume what will",
                   "The agreement of the greater number of men on a conclusion"],
             "c": 1,
             "why": "Reason is adding and subtracting the consequences of general "
                    "names agreed upon. Remembering and presuming from experience is "
                    "what he calls prudence, and he insists that no number of men's "
                    "agreement makes a reckoning right."},
            {"q": "In the undistributed preset, both premises are true. What is wrong "
                  "with the argument?",
             "a": ["The middle term ends both premises, so nothing cancels and the "
                   "conclusion does not follow",
                   "One of the premises must be false, since cats are not dogs",
                   "The conclusion is true but the premises are too general",
                   "A syllogism may not have two premises that begin with All"],
             "c": 0,
             "why": "Validity is about whether the conclusion follows, not whether the "
                    "premises are true. All cats are mammals and all dogs are mammals "
                    "are both true. And the barbara preset has two premises that begin "
                    "with All and is valid."},
            {"q": "Two parties dispute an account and each is sure it has reasoned "
                  "correctly. On Hobbes's account, what settles it?",
             "a": ["Whichever party has the greater number of supporters",
                   "Whichever party is the more careful reasoner, since reason is never wrong",
                   "An arbitrator whose reason they both agree to stand by",
                   "Nothing can settle it, because arithmetic cannot be checked"],
             "c": 2,
             "why": "He says the parties must by their own accord set up the reason "
                    "of an arbitrator or judge, or come to blows or leave it "
                    "undecided. Numbers of supporters do not make certainty, and even "
                    "the ablest reasoners may deceive themselves."},
            {"q": "One man predicts that the harvest will be good and it fails. "
                  "Another says there is a round quadrangle on the table. On Hobbes's "
                  "terms, what are they?",
             "a": ["Both are errors",
                   "Both are absurdities",
                   "The first is an absurdity and the second an error",
                   "The first is an error and the second an absurdity"],
             "c": 3,
             "why": "Error is a deception about what is past or to come, where nothing "
                    "was impossible. A round quadrangle is a thing he names as a case "
                    "of absurd speech, words with no meaning. The other pairings swap "
                    "or merge the two."},
        ],
        "mistakes": [
            ("Taking your own conviction for right reason",
             "It is easy to think that because reason itself is infallible, "
             "whatever you have reasoned out is the infallible result. Hobbes grants "
             "the first and denies the second: the ablest men may &ldquo;deceive "
             "themselves, and inferre false Conclusions&rdquo;, and a man who demands "
             "right reason as judge, meaning his own, is playing his longest suit as "
             "trump. The cure he proposes is an agreed arbitrator, not more "
             "confidence."),
            ("Thinking a valid argument has a true conclusion",
             "A valid argument guarantees its conclusion only if its premises are "
             "true, and a valid argument with a false premise may have a false "
             "conclusion. Hobbes says there can be no certainty of the last conclusion without a certainty of every "
             "affirmation on which it was grounded."),
            ("Treating absurdity as a bigger error",
             "An error is a wrong presumption about what is past or to come: it "
             "might have been so. An absurdity is a general assertion of which, "
             "unless it is true, the possibility is unconceivable. You can be "
             "corrected out of an error by looking, and out of an absurdity only by "
             "asking what the words mean."),
        ],
        "standard": (
            "Finish when you can test a two-premise syllogism and say what Hobbes "
            "means by reason.",
            "Given two categorical premises and a conclusion, say whether the "
            "conclusion is the sum of the premises, name a case that defeats it if "
            "not, and say in his terms why one person's confident reasoning is not "
            "right reason."
        ),
        "note": (
            "The lab judges syllogisms by regions of a Venn diagram, which is a later "
            "method, and it treats <em>All S are P</em> as true when there are no S, as "
            "modern logic does and the schools did not always. It tests whether a "
            "conclusion follows, and cannot say whether the premises are true or whether "
            "anyone's reasoning is right. The sample arguments are written for this "
            "lesson, and the Greeks and mortals are the textbooks', not Hobbes's."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Leviathan ch. 5, 1651 p. 20; PDF p. 130 of the operator's copy (the first
    # cause); the other six causes are 1651 pp. 20-21 (PDF p. 131); science,
    # prudence and sapience, 1651 pp. 21-23 (PDF pp. 131-133).
    {
        "slug": "absurdity-and-science",
        "title": "Absurdity and Science",
        "module": "Chapter 5 · Of Reason, and Science",
        "one_line": "Hobbes lists seven ways to say nothing while sounding learned, and holds that what is left when they are avoided is science: knowledge of consequences, not of fact.",
        "summary": (
            "The second half of Chapter 5 turns the definition into a test. Seven causes "
            "make reckoning with names go wrong, and most of them are one mistake, joining "
            "names that cannot be joined. Classify eight claims against a small vocabulary "
            "as true, false, absurd or insignificant, and see what Hobbes means when he says "
            "science is the knowledge of consequences."
        ),
        "key": [
            "a claim adds its two names",
            "true: the predicate's parts are all there",
            "false: some part is missing, nothing clashes",
            "absurd: the sum joins names that clash",
            "insignificant: a name stands for nothing",
        ],
        "key_label": "Four verdicts on a claim",
        "concepts_intro": (
            "After the definition Hobbes counts the ways it is abused, and then says what "
            "he thinks the practice is good for."
        ),
        "concepts": [
            ("The seven causes of absurdity",
             "No definitions to start from; names of bodies given to accidents, or the "
             "reverse; the accidents of things outside us given to our own bodies; names "
             "of bodies given to names; names of accidents given to names; metaphors in "
             "place of proper words; and names learned by rote that signify nothing. Four "
             "of them, the second to the fifth, are the same fault, a name of one kind put "
             "where a name of another belongs."),
            ("Science",
             "Reason is not born with us, nor got by experience alone, but "
             "&ldquo;attayned by Industry&rdquo;, by imposing names well and proceeding "
             "in order from names to assertions to syllogisms. What results is science, "
             "&ldquo;the knowledge of Consequences, and dependance of one fact upon "
             "another&rdquo;, as against sense and memory, which are knowledge of fact."),
            ("Prudence and sapience",
             "Much experience is prudence and much science is sapience. A man with a "
             "natural skill with his weapons is to a man who has also learned the "
             "science of fencing as prudence is to sapience: both useful, but the latter "
             "infallible. Signs of science can be certain, because a scientist can teach "
             "it; signs of prudence are all uncertain."),
        ],
        "read_title": "The seven causes, and then what they are for",
        "read_intro": (
            "The passage is the first of the seven. Hobbes's reasons are easiest to see "
            "once you try the names yourself, so the lab comes early."
        ),
        "body": [
            ("p", "<strong>Chapter 5.</strong> &ldquo;The first cause of Absurd "
                  "conclusions I ascribe to the want of Method; in that they begin not "
                  "their Ratiocination from Definitions; that is, from settled "
                  "significations of their words: as if they could cast account, without "
                  "knowing the value of the numerall words, one, two, and three.&rdquo;"),
            ("p", "Imagine a bookkeeper who is handed a ledger whose columns are headed "
                  "with words he has never been told the meaning of. He can add the "
                  "figures all day and the total will be a number, and it will tell him "
                  "nothing. Hobbes's first cause is that. Philosophers, he says, never "
                  "begin from the definitions of the names they use, which is a method "
                  "&ldquo;used onely in Geometry&rdquo; and the reason geometry's "
                  "conclusions are indisputable. He shows how much he thinks it matters "
                  "through Cicero, who said, and Hobbes agrees, that "
                  "&ldquo;there can be nothing so absurd, but may be found in the books "
                  "of Philosophers&rdquo;."),
            ("p", "The next four causes are the heart of the matter, and they are all "
                  "one thing. A name belongs to a kind: bodies, the accidents of bodies "
                  "(their qualities, such as being round or hot), and names themselves. "
                  "Put a name of one kind in a place that wants another and you get nonsense. "
                  "The second cause, giving names of bodies to accidents or the reverse, "
                  "is the man who says that faith is infused or inspired &ldquo;when "
                  "nothing can be powred, or breathed into any thing, but body&rdquo;. "
                  "The third gives the accidents of bodies outside us to the accidents of "
                  "our own bodies, as when someone says &ldquo;the colour is in the body; "
                  "the sound is in the ayre&rdquo;, which is the argument of the first "
                  "chapters again. The fourth gives names of bodies to names, as when "
                  "&ldquo;a living creature is Genus&rdquo;, and the fifth gives names of "
                  "accidents to names, as in &ldquo;the nature of a thing is its "
                  "definition&rdquo; or &ldquo;a mans command is his will&rdquo;."),
            ("p", "This is the picture the lab draws. It holds a small vocabulary in "
                  "which every name is defined as the sum of simpler names, down to "
                  "simple names that are admitted without definition, and a list of "
                  "pairs of simple names that cannot be added. Then it takes claims of "
                  "the form <em>this is that</em> and gives each one of four verdicts. "
                  "A claim is <strong>true</strong> when every simple name in the "
                  "predicate is already in the subject, which is Hobbes's account of an "
                  "affirmation as the adding of two names. It is <strong>false</strong> "
                  "when some part is missing and nothing clashes. It is "
                  "<strong>absurd</strong> when the two names, added, would join a pair "
                  "that cannot be joined. And it is <strong>insignificant</strong> when a "
                  "name in it is neither defined nor admitted, so that it stands for "
                  "nothing at all."),
            ("p", "One caution before you run it: these four verdicts are the lab's "
                  "sorting, not Hobbes's. He does not keep false and absurd apart "
                  "where a general claim is concerned. When we reason in words of "
                  "general signification and fall upon a general inference that is "
                  "false, he says, &ldquo;though it be commonly called Error, it is "
                  "indeed an Absurdity, or senslesse Speech&rdquo;. So on his account "
                  "<em>an animal is a man</em>, a false general claim, is absurd as "
                  "well. The lab's <em>absurd</em> marks only one kind, a clash among "
                  "the stated names, and its <em>false</em> a missing part; the "
                  "separation lets you see which fault a claim has."),
            ("p", "Run the causes preset. Man is defined as body, living, sensible and "
                  "rational, and animal as the first three, so <em>a man is an "
                  "animal</em> is true and <em>an animal is a man</em> is false: rational "
                  "is missing, but nothing clashes. <em>A circle is a quadrangle</em> is "
                  "Hobbes's round quadrangle, absurd because round and quadrangle are an "
                  "opposed pair. <em>Faith is poured</em>, <em>extension is body</em> and "
                  "<em>a creature is a genus</em> are his second cause twice and his fourth: faith is an accident and pouring needs a body, extension is "
                  "an accident, and a genus is a name, and body, accident and name are "
                  "three kinds that cannot be added. <em>A substance is immaterial</em> "
                  "is absurd on the definition that substance is body, and "
                  "<em>a man is transubstantiate</em> is insignificant, because the "
                  "word is on nobody's list of defined names."),
            ("p", "That last claim is his seventh cause. Hobbes lists "
                  "&ldquo;transubstantiate, consubstantiate, eternal-Now&rdquo; among the "
                  "names learned by rote from the Schools, &ldquo;and the like canting of "
                  "Schoole-men&rdquo;, and here he is aiming at the schoolmen, who "
                  "defended the doctrine that in the Mass the bread and wine become the "
                  "body and blood while keeping their appearances. He is also on "
                  "contested ground, for the sentence in which he defines absurdity "
                  "names &ldquo;A free Subject; A free-will&rdquo; among its examples, "
                  "and he allows the word <em>free</em> only for what is free from being "
                  "hindered. Bishop John Bramhall, with whom he had argued about liberty "
                  "in Paris, answered him in print later; Bramhall held that a man is "
                  "free only if he could have willed otherwise, and thought Hobbes had "
                  "redefined the word, not refuted anything."),
            ("p", "Notice how much each verdict depends on the definition chosen. The "
                  "verdict on <em>a substance is immaterial</em> follows from "
                  "<em>substance</em> meaning body. Descartes, and in England Henry More, "
                  "said a substance is whatever has properties of its own, and that "
                  "there are two kinds, body and mind; for them the claim is not a contradiction in names "
                  "but false, since some substances are not bodies. The lab computes what follows from "
                  "Hobbes's definition and cannot say whose definition is right, and "
                  "that is the dispute, put honestly. The seventh is about names that "
                  "signify nothing, and the sixth, metaphor, he treats gently: it is "
                  "&ldquo;lawfull&rdquo; to say the way goes to London, but &ldquo;in "
                  "reckoning, and seeking of truth, such speeches are not to be "
                  "admitted&rdquo;."),
            ("p", "Now the positive side. For anyone who can avoid the seven, Hobbes "
                  "says, it is not easy to fall into absurdity, &ldquo;unlesse it be by "
                  "the length of an account; wherein he may perhaps forget what went "
                  "before&rdquo;, because &ldquo;all men by nature reason alike, and "
                  "well, when they have good principles&rdquo;. What good principles "
                  "give you is science, and he says what that is by contrast: "
                  "&ldquo;Sense and Memory are but knowledge of Fact, which is a thing "
                  "past, and irrevocable&rdquo;, while &ldquo;Science is the knowledge of "
                  "Consequences, and dependance of one fact upon another&rdquo;. The lab "
                  "shows the idea in miniature in the science preset. From the "
                  "definitions alone it follows that a man is a creature, that a man is "
                  "a body, and that an animal is a creature, and that a creature is a man "
                  "does not follow. None of that is learned by looking at anyone. The "
                  "no-definitions preset shows what the first cause costs: take the "
                  "causes claims, leave pouring and genus undefined, and two more "
                  "turn insignificant, three in all, like the bookkeeper's total."),
            ("p", "That knowledge is what lets a person plan. Because we see how a "
                  "thing comes about, he says, &ldquo;when the like causes come into our "
                  "power, wee see how to make it produce the like effects&rdquo;. Most "
                  "people, he adds with some severity, never get that far: "
                  "&ldquo;Geometry they have thought Conjuring&rdquo;, and "
                  "&ldquo;Children therefore are not endued with Reason at all, till "
                  "they have attained the use of Speech&rdquo;. Yet he does not "
                  "despise the unlearned. Those who have no science, he says, are in "
                  "&ldquo;better, and nobler condition with their naturall Prudence&rdquo; "
                  "than men who rely on the rules of an author who reasons wrong, "
                  "because ignorance of causes does not set a man so far from his way "
                  "as relying on false rules."),
            ("p", "His example of the difference is a fencing match. One man has a "
                  "natural skill with his weapons; another has that and has also "
                  "learned from a master of fence where he can offend or be offended in "
                  "every posture. The first is prudent and the second has science, as "
                  "&ldquo;Prudence to Sapience; both usefull; but the later "
                  "infallible&rdquo;. And the signs differ. A man's science is certain "
                  "when he can teach it, when he can demonstrate it to another; "
                  "&ldquo;Signes of prudence are all uncertain&rdquo;, because no one can "
                  "remember every circumstance that might alter the result. The "
                  "line from the chapter to remember: &ldquo;The Light of "
                  "humane minds is Perspicuous Words, but by exact definitions first "
                  "snuffed, and purged from ambiguity&rdquo;."),
            ("p", "Hobbes is hard on his opponents here, and a reader should keep one "
                  "question open: is science, as he describes it, available to a "
                  "politician or a moralist at all, or only to a geometer? He thinks it "
                  "is, and builds the rest of Leviathan on the claim. A critic can reply "
                  "that definitions of <em>justice</em> and <em>power</em> are exactly the "
                  "names that fail his first test, because they are contested in the "
                  "way a triangle is not. Hobbes had said as much at the end of "
                  "Chapter 4, of the names of virtues and vices, which one man will "
                  "use for what another names differently. The next lesson, &ldquo;The "
                  "Passions&rdquo;, takes up where they come from."),
        ],
        "lab": ("levkit", {
            "mode": "reckon",
            "view": "names",
            "preset": "causes",
            "presets": [
                {"id": "causes", "label": "Hobbes's examples, with definitions",
                 "simple": ["body", "accident", "name", "living", "sensible", "rational",
                            "figure", "round", "quadrangle", "extended", "moved", "believing",
                            "incorporeal", "general"],
                 "defs": [
                     ["man", "body living sensible rational"],
                     ["animal", "body living sensible"],
                     ["creature", "body living"],
                     ["circle", "figure round"],
                     ["faith", "accident believing"],
                     ["poured", "body moved"],
                     ["extension", "accident extended"],
                     ["substance", "body"],
                     ["immaterial", "incorporeal"],
                     ["genus", "name general"],
                 ],
                 "opposed": [
                     ["body", "accident"], ["body", "name"],
                     ["accident", "name"], ["round", "quadrangle"],
                     ["body", "incorporeal"],
                 ],
                 "claims": [
                     ["a-man-is-an-animal", "man", "animal"],
                     ["an-animal-is-a-man", "animal", "man"],
                     ["a-circle-is-a-quadrangle", "circle", "quadrangle"],
                     ["faith-is-poured", "faith", "poured"],
                     ["extension-is-body", "extension", "body"],
                     ["a-creature-is-a-genus", "creature", "genus"],
                     ["a-substance-is-immaterial", "substance", "immaterial"],
                     ["a-man-is-transubstantiate", "man", "transubstantiate"],
                 ],
                 "expect": {"lrkCounts": "1 true, 1 false, 5 absurd, 1 insignificant", "lrkVerdicts": "a-man-is-an-animal true; an-animal-is-a-man false; a-circle-is-a-quadrangle absurd; faith-is-poured absurd; extension-is-body absurd; a-creature-is-a-genus absurd; a-substance-is-immaterial absurd; a-man-is-transubstantiate insignificant"}},
                {"id": "no-definitions", "label": "The same claims, two names left undefined",
                 "simple": ["body", "accident", "name", "living", "sensible", "rational",
                            "figure", "round", "quadrangle", "extended", "moved", "believing",
                            "incorporeal", "general"],
                 "defs": [
                     ["man", "body living sensible rational"],
                     ["animal", "body living sensible"],
                     ["creature", "body living"],
                     ["circle", "figure round"],
                     ["faith", "accident believing"],
                     ["extension", "accident extended"],
                     ["substance", "body"],
                     ["immaterial", "incorporeal"],
                 ],
                 "opposed": [
                     ["body", "accident"], ["body", "name"],
                     ["accident", "name"], ["round", "quadrangle"],
                     ["body", "incorporeal"],
                 ],
                 "claims": [
                     ["a-man-is-an-animal", "man", "animal"],
                     ["an-animal-is-a-man", "animal", "man"],
                     ["a-circle-is-a-quadrangle", "circle", "quadrangle"],
                     ["faith-is-poured", "faith", "poured"],
                     ["extension-is-body", "extension", "body"],
                     ["a-creature-is-a-genus", "creature", "genus"],
                     ["a-substance-is-immaterial", "substance", "immaterial"],
                     ["a-man-is-transubstantiate", "man", "transubstantiate"],
                 ],
                 "expect": {"lrkCounts": "1 true, 1 false, 3 absurd, 3 insignificant", "lrkVerdicts": "a-man-is-an-animal true; an-animal-is-a-man false; a-circle-is-a-quadrangle absurd; faith-is-poured insignificant; extension-is-body absurd; a-creature-is-a-genus insignificant; a-substance-is-immaterial absurd; a-man-is-transubstantiate insignificant"}},
                {"id": "science", "label": "What follows from the definitions alone",
                 "simple": ["body", "living", "sensible", "rational"],
                 "defs": [
                     ["man", "body living sensible rational"],
                     ["animal", "body living sensible"],
                     ["creature", "body living"],
                 ],
                 "opposed": [],
                 "claims": [
                     ["a-man-is-a-creature", "man", "creature"],
                     ["a-man-is-a-body", "man", "body"],
                     ["an-animal-is-a-creature", "animal", "creature"],
                     ["a-creature-is-a-man", "creature", "man"],
                 ],
                 "expect": {"lrkCounts": "3 true, 1 false, 0 absurd, 0 insignificant", "lrkVerdicts": "a-man-is-a-creature true; a-man-is-a-body true; an-animal-is-a-creature true; a-creature-is-a-man false"}},
            ],
            "panel_title": "Which claims survive the definitions?",
            "panel_intro": (
                "Each claim is checked against the definitions in the preset: the "
                "predicate's simple names must all be in the subject, no opposed pair "
                "may be joined, and every name must be defined or admitted. Run the "
                "three presets in order, then retype a definition and watch which "
                "verdicts move."
            ),
        }),
        "steps_title": "Classifying a claim",
        "steps_intro": "Four steps; the order matters, because a name with no meaning cannot be tested for anything else.",
        "steps": [
            ("Check every name",
             "Each name in the claim must be either defined in terms of simpler names "
             "or admitted as simple. A name that is neither stands for nothing, and the "
             "claim is insignificant; stop there."),
            ("Expand both names to simple names",
             "Replace each defined name by the simple names it is the sum of, "
             "repeating until only simple names are left."),
            ("Look for a clash",
             "Add the two expansions. If the sum contains both names of an opposed "
             "pair, the claim is absurd, whatever else is true of it."),
            ("Compare the parts",
             "Otherwise ask whether every simple name of the predicate is among those "
             "of the subject. If so the claim is true by the definitions; if not it is "
             "false."),
        ],
        "worked": {
            "title": "Faith is poured",
            "intro": [
                "Take the second of Hobbes's causes, with faith defined as an accident "
                "of believing and pouring as a moving of a body.",
            ],
            "lines": [
                "faith expands to: accident, believing",
                "poured expands to: body, moved",
                "the sum holds accident and body",
                "accident and body cannot be added: absurd",
            ],
            "after": [
                "Notice that the claim was not tested against the facts about faith. "
                "It fails before that, because the two names cannot be added. Compare "
                "an animal is a man, which adds without a clash and is false in the lab's sorting, "
                "since rational is missing; Hobbes would call a false general claim "
                "absurd too.",
            ],
        },
        "quiz_title": "Absurd, false and insignificant",
        "quiz": [
            {"q": "What does Hobbes give as the first cause of absurd conclusions?",
             "a": ["Using metaphors in place of proper words",
                   "Giving the names of bodies to accidents",
                   "Not beginning reasoning from definitions, that is from settled significations of words",
                   "Trusting the books of ancient authors"],
             "c": 2,
             "why": "The first cause is want of method, beginning without definitions. "
                    "Metaphor is the sixth, and the second is giving names of bodies to "
                    "accidents. Trusting authors is a fault he describes elsewhere in the "
                    "chapter, but it is not one of his seven."},
            {"q": "In the lab's vocabulary man is body, living, sensible and rational, "
                  "and animal is body, living and sensible. What is the verdict on "
                  "<em>an animal is a man</em>?",
             "a": ["True, because every man is an animal",
                   "Absurd, because animal and man cannot be added",
                   "Insignificant, because animal is not a simple name",
                   "False, because rational is not among the parts of animal"],
             "c": 3,
             "why": "The predicate man has a part, rational, that the subject animal "
                    "lacks, and no opposed pair is joined, so the lab's verdict is false and "
                    "not absurd, though Hobbes would call a false general claim absurd too. The converse, a man is an animal, is the true one."},
            {"q": "On Hobbes's account, what is the difference between science and "
                  "sense and memory?",
             "a": ["Science is knowledge of consequences, sense and memory of fact",
                   "Science is knowledge of fact, sense and memory of consequences",
                   "Science is born with us, sense and memory are attained by industry",
                   "Science is uncertain, sense and memory are infallible"],
             "c": 0,
             "why": "Sense and memory are knowledge of fact, a thing past and "
                    "irrevocable; science is knowledge of consequences and the "
                    "dependence of one fact on another. He says reason, and so science, "
                    "is attained by industry and not born with us."},
            {"q": "Which of these does Hobbes say is true of the signs of science and "
                  "of prudence?",
             "a": ["Both are certain whenever a man has had enough practice",
                   "The signs of science are always uncertain and those of prudence certain",
                   "The signs of science can be certain, but the signs of prudence are all uncertain",
                   "Neither can be a sign of anything, since both are in the mind"],
             "c": 2,
             "why": "A man's science is certain when he can teach it and demonstrate it "
                    "to another. The signs of prudence are all uncertain, because no one "
                    "can observe and remember every circumstance that may alter the "
                    "outcome."},
        ],
        "mistakes": [
            ("Taking the lab's four verdicts for Hobbes's",
             "In the lab an animal is a man is false, because a part is missing, and a "
             "circle is a quadrangle is absurd, because two names clash. That sorting "
             "is the lab's. Hobbes says that a false general inference, though "
             "commonly called error, &ldquo;is indeed an Absurdity, or senslesse "
             "Speech&rdquo;, so he would call both claims absurd. What he does keep "
             "apart is error about what is past or to come, where nothing was "
             "impossible, and absurdity in general words."),
            ("Reading the sixth cause as a ban on metaphor",
             "Hobbes does not forbid it. He allows that it is &ldquo;lawfull&rdquo; to "
             "say in common speech that the way goes hither or thither; what he "
             "excludes is metaphor &ldquo;in reckoning, and seeking of truth&rdquo;, "
             "where a figure of speech can be taken for a premise."),
            ("Thinking Hobbes despises those without science",
             "He says that people with no science are &ldquo;in better, and nobler "
             "condition with their naturall Prudence&rdquo; than men who trust false "
             "general rules. The contempt in the chapter is for the learned who reason "
             "from names they have not defined, and for those who rely on their "
             "writings without checking."),
        ],
        "standard": (
            "Finish when you can classify a claim from a stated vocabulary.",
            "Given definitions, simple names and a list of opposed pairs, expand a claim "
            "and say whether it is true, false, absurd or insignificant, and name the "
            "missing part, the clash or the empty name that decides it."
        ),
        "note": (
            "The lab's rule is a model of Hobbes's account of affirmation as the adding "
            "of names, and the vocabulary is written for this lesson. It decides what "
            "follows from the definitions as stated and cannot say whether the "
            "definitions are right: that a substance is a body, or that an accident "
            "cannot be a body, are the claims his opponents deny. A verdict of "
            "absurd means only that the definitions given make the claim unsayable. "
            "The four verdicts are the lab's own sorting. Hobbes uses absurd and "
            "insignificant for the same fault, and holds that a false general "
            "affirmation is absurd too; the split between a clash, a missing part and "
            "an empty name is the lab's, made so that you can see which is which."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Leviathan ch. 6, 1651 p. 25; PDF p. 137 of the operator's copy (the
    # simple passions and their compounds); motion and endeavour, 1651 pp. 23-24
    # (PDF pp. 133-134); good and evil, 1651 p. 24 (PDF p. 135).
    {
        "slug": "the-passions",
        "title": "The Passions",
        "module": "Chapter 6 · Of the Interiour Beginnings of Voluntary Motions; commonly called the Passions",
        "one_line": "Hobbes defines the passions as motions toward and away from things, and names the rest by adding opinion, so that anger turns out to be sudden courage.",
        "summary": (
            "Chapter 6 begins from the body: voluntary motion starts in imagination, as a "
            "small beginning of motion called endeavour, and endeavour toward a thing is "
            "appetite while endeavour from it is aversion. Then Hobbes builds many named "
            "passions by adding an opinion, a degree or an object. Compute "
            "which names a case falls under, and find the case that falls under more than "
            "one."
        ),
        "key": [
            "endeavour toward a thing: appetite",
            "endeavour from a thing: aversion",
            "hope = appetite + opinion of attaining",
            "fear = aversion + opinion of hurt",
            "anger = sudden courage",
        ],
        "key_label": "The passions as sums",
        "concepts_intro": (
            "Hobbes begins from the body and ends with a dictionary, and the dictionary "
            "is built, like a syllogism, by adding."
        ),
        "concepts": [
            ("Endeavour, appetite and aversion",
             "Voluntary motions begin in imagination; the small beginnings of motion "
             "inside the body, before they show in walking or striking, are called "
             "endeavour. Endeavour toward what causes it is appetite or desire, and "
             "endeavour away from something is aversion. What is neither wanted nor "
             "hated is contemned."),
            ("Good and evil are relative to the person",
             "Whatever a man desires, he calls good for his part, and what he hates, "
             "evil. There is no common rule of good and evil to be taken from the "
             "objects themselves, only from the person of the man where there is no "
             "commonwealth, or from the person that represents it where there is, or "
             "from an arbitrator the disputing parties set up."),
            ("Compounds named by opinion",
             "The simple passions, appetite, desire, love, aversion, hate, joy and "
             "grief, get new names when they succeed one another, from the opinion of "
             "attaining, from the object, from many of them together, and from their "
             "alteration. Appetite with an opinion of attaining is hope, and without it "
             "despair; aversion with an opinion of hurt is fear, and so on."),
        ],
        "read_title": "From endeavour to the dictionary of the passions",
        "read_intro": (
            "The passage is a run of definitions, so read it once as a list and then see "
            "what they can be made to do."
        ),
        "body": [
            ("p", "<strong>Chapter 6.</strong> &ldquo;For Appetite with an opinion of "
                  "attaining, is called Hope. The same, without such opinion, Despaire. "
                  "Aversion, with opinion of Hurt from the object, Feare. The same, with "
                  "hope of avoyding that Hurt by resistence, Courage. Sudden courage, "
                  "Anger.&rdquo;"),
            ("p", "Think of standing at the top of a high diving board. You want to be "
                  "in the water and you do not want to fall, and what you feel at any "
                  "moment depends on what you believe about the next second. Hobbes's "
                  "claim is that this is all there is to it: a feeling is a motion "
                  "toward or away from something, and its name comes from the opinion "
                  "that goes with it. Fear is not a separate stuff. It is aversion with "
                  "an opinion of hurt, and add the hope of getting through by "
                  "resisting and it is courage. Add suddenness, and the person who has "
                  "just been pushed in the queue is not afraid and brave in turn but "
                  "angry, which Hobbes defines as &ldquo;Sudden courage&rdquo;."),
            ("p", "The ground for this is in the first page of the chapter. There "
                  "are two motions peculiar to animals: the vital motion of blood, "
                  "pulse and breath, which needs no imagination, and the voluntary one, "
                  "&ldquo;as is first fancied in our minds&rdquo;, hence the claim "
                  "that &ldquo;Imagination is the first internall beginning of all "
                  "Voluntary Motion&rdquo;. A motion too small to see is still a "
                  "motion: &ldquo;These small beginnings of Motion, within the body of "
                  "Man, before they appear in walking, speaking, striking, and other "
                  "visible actions, are commonly called Endeavour&rdquo;. When the "
                  "endeavour is &ldquo;toward something which causes it&rdquo; it is "
                  "appetite or desire, and when it is fromward something, aversion; the "
                  "Latin words mean approaching and retiring. He says the schools, who "
                  "found no actual motion in mere appetite and called it metaphorical, "
                  "spoke what &ldquo;is but an absurd speech&rdquo;, since words may be "
                  "metaphorical, but bodies and motions cannot."),
            ("p", "Now the step that matters politically. If what moves a man is "
                  "appetite, then good is only a name for what is wanted. &ldquo;whatsoever "
                  "is the object of any mans Appetite or Desire; that is it, which he for "
                  "his part calleth Good&rdquo;, and the object of his hate, evil. These "
                  "words are &ldquo;ever used with relation to the person that useth "
                  "them&rdquo;: there is &ldquo;nothing simply and absolutely so; nor any "
                  "common Rule of Good and Evill, to be taken from the nature of the "
                  "objects themselves&rdquo;. Where there is a commonwealth, the rule "
                  "comes from the person that represents it; where there is not, from "
                  "&ldquo;the Person of the man&rdquo;. You can see here the shape of "
                  "the argument of Part II: if each man's good is his own, men "
                  "disagree, and what ends the disagreement is an arbitrator they set up."),
            ("p", "The older tradition he was arguing with held the opposite, that "
                  "some things are good in their own nature and reason can see which. "
                  "The Cambridge Platonist Ralph Cudworth wrote against Hobbes on "
                  "exactly this point, that good and evil are not made by appetite. "
                  "Hobbes's own remedy, in the passage, is the arbitrator, a standard "
                  "that disagreeing men set up by consent. The lab does not take a "
                  "side. It takes his definitions of the passions as given."),
            ("p", "The lab works like the one in the last lesson. Each passion is a "
                  "name defined as the sum of simpler names. Fear is aversion and an "
                  "opinion of hurt, and courage is fear and the hope of avoiding the "
                  "hurt, so courage expands to aversion, opinion of hurt and hope of "
                  "avoiding. Anger is courage and suddenness, so it holds everything "
                  "courage holds. Confidence is constant hope, and diffidence constant "
                  "despair; jealousy is the passion of love, &ldquo;Love of one "
                  "singularly, with desire to be singularly beloved&rdquo;, with "
                  "&ldquo;fear that the love is not mutuall&rdquo;. Covetousness and "
                  "ambition are the desire of riches and of office. Run the ladder "
                  "preset and you get what the definitions imply. Anger is courage, "
                  "and since courage contains fear, anger is fear, which "
                  "sounds odd until you look at what he has put in it. Courage is not "
                  "anger, because suddenness is missing. Confidence is hope, and hope "
                  "is not confidence."),
            ("p", "And <em>diffidence is hope</em> is absurd in the lab's sense, not merely false: "
                  "diffidence is despair, which is appetite without the opinion of "
                  "attaining, and hope is appetite with it, and no one can have both "
                  "at once about one thing. The ladder also gives jealousy as fear, "
                  "and as the passion of love, since it is that passion with fear "
                  "added. Hobbes tells you in advance that a name can be built this "
                  "way: the simple passions &ldquo;have their names for divers "
                  "considerations diversified&rdquo;."),
            ("p", "The cases preset turns it round. Here a situation is given as "
                  "its parts, and the question is which names it falls under. The "
                  "charge is a soldier's rush with aversion, an opinion of hurt, a "
                  "hope of getting through and suddenness; it is anger, courage and "
                  "fear all at once, and not indignation, which needs great hurt done "
                  "to another, thought injury. The wait is a gambler's patient "
                  "appetite with an opinion that he will get it: it is confidence and "
                  "it is hope, and it is not despair, which would be absurd. The "
                  "lost cause has constant appetite with no opinion of attaining, "
                  "so it is diffidence and cannot be hope. A case that is two "
                  "passions at once, then, is not a muddle. Hobbes's names overlap by "
                  "construction, because one is built on another."),
            ("p", "The rest of the list reads best as a cold view of ordinary "
                  "life. Sudden glory is the passion whose grimace is laughter, and &ldquo;much "
                  "Laughter at the defects of others, is a signe of "
                  "Pusillanimity&rdquo;. Pity is grief for another's calamity, "
                  "&ldquo;from the imagination that the like calamity may befall "
                  "himselfe&rdquo;. And cruelty, he says, comes from security of one's "
                  "own fortune, for &ldquo;that any man should take pleasure in other "
                  "mens great harmes, without other end of his own, I do not conceive "
                  "it possible&rdquo;. Each of these gives the passion a comparison "
                  "with someone else, a point that returns in Chapter 10, on power "
                  "and honour, and in Chapter 13, on the war of all against all."),
            ("p", "The standard objection is to the reduction. In 1726 Joseph "
                  "Butler, later a bishop, preached against the view, which he ascribed to "
                  "Hobbes, that pity and benevolence are only disguised self-love, "
                  "arguing that compassion is a real regard for the other person "
                  "and not a fear for oneself. Hobbes's definition says that pity "
                  "arises from imagining the same misfortune befalling oneself, and "
                  "the disagreement is over whether that makes it self-love. The lab "
                  "sees only the names. Whether his list is the right way to cut "
                  "the passions up, it cannot say."),
            ("p", "The chapter's second half stays with the same motions but asks "
                  "what happens when appetite and aversion pull in turn about one "
                  "action. The next lesson, <em>Deliberation and the Will</em>, "
                  "defines the will as the last of them."),
        ],
        "lab": ("levkit", {
            "mode": "reckon",
            "view": "names",
            "preset": "ladder",
            "presets": [
                {"id": "ladder", "label": "Hobbes's passions, compared with each other",
                 "simple": ["appetite", "aversion", "opinion-of-attaining", "no-opinion-of-attaining",
                            "opinion-of-hurt", "hope-of-avoiding", "sudden", "constant",
                            "hurt-to-another", "conceived-as-injury", "good-to-another",
                            "singular", "wish-to-be-loved", "riches", "office"],
                 "defs": [
                     ["hope", "appetite opinion-of-attaining"],
                     ["despair", "appetite no-opinion-of-attaining"],
                     ["fear", "aversion opinion-of-hurt"],
                     ["courage", "fear hope-of-avoiding"],
                     ["anger", "courage sudden"],
                     ["confidence", "hope constant"],
                     ["diffidence", "despair constant"],
                     ["indignation", "anger hurt-to-another conceived-as-injury"],
                     ["benevolence", "appetite good-to-another"],
                     ["covetousness", "appetite riches"],
                     ["ambition", "appetite office"],
                     ["passion-of-love", "appetite singular wish-to-be-loved"],
                     ["jealousy", "passion-of-love fear"],
                 ],
                 "opposed": [["opinion-of-attaining", "no-opinion-of-attaining"]],
                 "claims": [
                     ["anger-is-courage", "anger", "courage"],
                     ["courage-is-anger", "courage", "anger"],
                     ["anger-is-fear", "anger", "fear"],
                     ["confidence-is-hope", "confidence", "hope"],
                     ["hope-is-confidence", "hope", "confidence"],
                     ["diffidence-is-hope", "diffidence", "hope"],
                     ["jealousy-is-the-passion-of-love", "jealousy", "passion-of-love"],
                     ["jealousy-is-fear", "jealousy", "fear"],
                     ["anger-is-laughter", "anger", "laughter"],
                 ],
                 "expect": {"lrkCounts": "5 true, 2 false, 1 absurd, 1 insignificant", "lrkVerdicts": "anger-is-courage true; courage-is-anger false; anger-is-fear true; confidence-is-hope true; hope-is-confidence false; diffidence-is-hope absurd; jealousy-is-the-passion-of-love true; jealousy-is-fear true; anger-is-laughter insignificant"}},
                {"id": "cases", "label": "Three cases, and the names each falls under",
                 "simple": ["appetite", "aversion", "opinion-of-attaining", "no-opinion-of-attaining",
                            "opinion-of-hurt", "hope-of-avoiding", "sudden", "constant",
                            "hurt-to-another", "conceived-as-injury"],
                 "defs": [
                     ["hope", "appetite opinion-of-attaining"],
                     ["despair", "appetite no-opinion-of-attaining"],
                     ["fear", "aversion opinion-of-hurt"],
                     ["courage", "fear hope-of-avoiding"],
                     ["anger", "courage sudden"],
                     ["confidence", "hope constant"],
                     ["diffidence", "despair constant"],
                     ["indignation", "anger hurt-to-another conceived-as-injury"],
                     ["the-charge", "aversion opinion-of-hurt hope-of-avoiding sudden"],
                     ["the-wait", "appetite opinion-of-attaining constant"],
                     ["the-lost-cause", "appetite no-opinion-of-attaining constant"],
                 ],
                 "opposed": [["opinion-of-attaining", "no-opinion-of-attaining"]],
                 "claims": [
                     ["the-charge-is-anger", "the-charge", "anger"],
                     ["the-charge-is-courage", "the-charge", "courage"],
                     ["the-charge-is-fear", "the-charge", "fear"],
                     ["the-charge-is-indignation", "the-charge", "indignation"],
                     ["the-wait-is-confidence", "the-wait", "confidence"],
                     ["the-wait-is-hope", "the-wait", "hope"],
                     ["the-wait-is-despair", "the-wait", "despair"],
                     ["the-lost-cause-is-diffidence", "the-lost-cause", "diffidence"],
                     ["the-lost-cause-is-hope", "the-lost-cause", "hope"],
                 ],
                 "expect": {"lrkCounts": "6 true, 1 false, 2 absurd, 0 insignificant", "lrkVerdicts": "the-charge-is-anger true; the-charge-is-courage true; the-charge-is-fear true; the-charge-is-indignation false; the-wait-is-confidence true; the-wait-is-hope true; the-wait-is-despair absurd; the-lost-cause-is-diffidence true; the-lost-cause-is-hope absurd"}},
            ],
            "panel_title": "Which names does a passion, or a case, fall under?",
            "panel_intro": (
                "Each passion is the sum of simpler names, as Hobbes defines it. A claim "
                "is true when everything in the predicate is in the subject, absurd when "
                "the two would join an opposed pair, and insignificant when a name has no "
                "definition. Run the two presets, then change a definition and see which "
                "verdicts move."
            ),
        }),
        "steps_title": "Naming a passion from a case",
        "steps_intro": "Four steps, taking the case apart before naming it.",
        "steps": [
            ("List the motions in the case",
             "Say whether the motion is toward the thing or away from it, and so "
             "whether the basis is appetite or aversion."),
            ("List the opinions that go with it",
             "Note whether the person thinks he will attain what he wants, expects "
             "hurt, hopes to resist it, and whether the passion is sudden or constant."),
            ("Match against Hobbes's definitions",
             "Each definition is a sum. A case falls under a name when every part of "
             "that name's definition is present in the case."),
            ("Expect more than one name",
             "Because compounds are built on simpler ones, a case that is anger is also "
             "courage and fear. Take the most specific name as the answer and the rest "
             "as what it contains."),
        ],
        "worked": {
            "title": "The charge",
            "intro": [
                "A soldier runs at the line, afraid of being hurt, hoping to get through "
                "by fighting, and moving at once. Take his case apart as the lab does.",
            ],
            "lines": [
                "case: aversion, opinion of hurt, hope of avoiding, sudden",
                "fear: aversion with opinion of hurt: present",
                "courage: fear with hope of avoiding: present",
                "anger: courage that is sudden: present",
                "indignation: anger with hurt to another: missing",
            ],
            "after": [
                "The charge falls under fear, courage and anger, nested, and not under "
                "indignation. That is not four feelings, only one case read at four "
                "levels of definition.",
            ],
        },
        "quiz_title": "Hobbes's passions as sums",
        "quiz": [
            {"q": "Which passion does Hobbes define as aversion with an opinion of "
                  "hurt from the object?",
             "a": ["Despair", "Fear", "Anger", "Courage"],
             "c": 1,
             "why": "Fear is aversion with opinion of hurt. Despair is appetite without "
                    "the opinion of attaining, courage is fear with hope of avoiding the "
                    "hurt by resistance, and anger is sudden courage."},
            {"q": "In the lab's vocabulary, is <em>anger is fear</em> true?",
             "a": ["True: anger is sudden courage, and courage is fear with hope of resisting",
                   "False, because anger and fear are opposite passions",
                   "Absurd, because anger and fear cannot be added",
                   "Insignificant, because anger is not a simple name"],
             "c": 0,
             "why": "Anger expands to everything courage holds, and courage holds fear, so "
                    "the predicate's parts are all in the subject. Nothing in the "
                    "vocabulary makes aversion and an opinion of hurt clash with "
                    "suddenness, and anger is defined, so it is not insignificant."},
            {"q": "What does Hobbes say good is?",
             "a": ["A property of things that reason can see in them",
                   "Whatever a majority of men desire",
                   "What God commands in Scripture",
                   "The object of a man's appetite, for his part, with no common rule in "
                   "the objects themselves"],
             "c": 3,
             "why": "Whatever is the object of a man's appetite or desire is what he for "
                    "his part calls good. There is no common rule of good and evil to be "
                    "taken from the nature of the objects themselves, only from the "
                    "person, or in a commonwealth from the one who represents it."},
            {"q": "What is the difference between desire and love, according to Hobbes?",
             "a": ["Desire is a motion toward a thing and love a motion away from it",
                   "Love is desire joined with a hope of attaining",
                   "They are the same thing, but desire signifies the absence of the "
                   "object and love most commonly its presence",
                   "Desire is the passion of the body and love of the mind"],
             "c": 2,
             "why": "He writes that desire and love are the same thing, save that by "
                    "desire we always signify the absence of the object and by love most "
                    "commonly its presence. A motion away from a thing is aversion, and "
                    "hope is appetite with an opinion of attaining."},
        ],
        "mistakes": [
            ("Taking good to be a property of the thing",
             "It is natural to say that some things are good, full stop. Hobbes says "
             "the word is &ldquo;ever used with relation to the person that useth "
             "them&rdquo;, and the rule of good comes from the person, from the "
             "representative of a commonwealth, or from an arbitrator. The "
             "dispute with the opposite view is real, and the lab only takes his "
             "definitions as given."),
            ("Thinking courage is the absence of fear",
             "In the definitions courage contains fear. It is &ldquo;The same, with "
             "hope of avoyding that Hurt by resistence&rdquo;: aversion with an "
             "opinion of hurt, plus a hope. Anger, being sudden courage, contains it "
             "too, which is why <em>anger is fear</em> comes out true."),
            ("Treating each name as a separate feeling with a separate cause",
             "Hobbes says the simple passions &ldquo;have their names for divers "
             "considerations diversified&rdquo;: the same motions are named differently "
             "according to the opinion of attaining, the object, several together, and "
             "the alteration. The cases preset shows one situation falling under "
             "several names, and that is the point."),
        ],
        "standard": (
            "Finish when you can name the passions a case falls under.",
            "Given a case as appetite or aversion with its opinions, name every passion "
            "in Hobbes's list that the case falls under, and say which part is missing "
            "when it does not fall under a nearby one."
        ),
        "note": (
            "The vocabulary here follows Hobbes's definitions of about a dozen of the "
            "passions and writes his opinions as simple names, which is a choice: he "
            "does not say that an opinion is a simple name, and a reader may think "
            "hope involves more than appetite and a belief. The lab computes what "
            "follows from the definitions and cannot say whether they cut the passions "
            "at the joints, or whether good is relative as he says. The cases are "
            "written for this lesson. The four verdicts are the lab's own sorting, "
            "not Hobbes's: he counts a false general affirmation absurd too, and the "
            "lab's <em>absurd</em> marks only a clash among the names stated."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Leviathan ch. 6, 1651 p. 28; PDF p. 140 of the operator's copy
    # (deliberation and the will); the schools' definition, inclination and
    # voluntary action, 1651 pp. 28-29 (PDF pp. 140-141); apparent good and
    # felicity, 1651 pp. 29-30 (PDF p. 142).
    {
        "slug": "deliberation-and-will",
        "title": "Deliberation and the Will",
        "module": "Chapter 6 · Of the Interiour Beginnings of Voluntary Motions; commonly called the Passions",
        "one_line": "Hobbes says deliberation is the whole sum of appetites, aversions, hopes and fears about one action, and the will is only the last of them before the act or its omission.",
        "summary": (
            "The rest of Chapter 6 asks what happens when the passions of the last "
            "lesson pull in turn on one action. Deliberation is the whole alternation, "
            "and the will is not a faculty but the last appetite or aversion in it. "
            "Run a deliberation step by step, find the will, and count how many of "
            "the earlier stops would have given the opposite will."
        ),
        "key": [
            "deliberation = the whole alternation",
            "will = the last appetite or aversion",
            "earlier appetites are inclinations only",
            "an act done from fear is voluntary",
            "ends when the thing is done or impossible",
        ],
        "key_label": "Deliberation and the will in five lines",
        "concepts_intro": (
            "This half of the chapter makes three moves: a definition of "
            "deliberation, a definition of the will that discards the schools' one, "
            "and a short account of what makes an act voluntary."
        ),
        "concepts": [
            ("Deliberation",
             "When appetites and aversions, hopes and fears about one thing arise "
             "alternately, and good and evil consequences of doing or omitting it come "
             "into the mind in turn, the whole sum, continued until the thing is done or "
             "thought impossible, is deliberation. It puts an end to the liberty we had "
             "of doing or omitting, and beasts deliberate too."),
            ("The will",
             "The last appetite or aversion immediately adhering to the action or to "
             "its omission is the will, the act and not the faculty of willing. The "
             "schools' definition, a rational appetite, is not good, because it would "
             "leave no voluntary act against reason. Earlier appetites, even strong "
             "ones, are inclinations."),
            ("Voluntary action",
             "A voluntary act is one that proceeds from the will. It does not matter "
             "whether the last appetite is covetousness, ambition or lust, or an "
             "aversion or fear of what follows from omitting: all these actions are "
             "voluntary."),
        ],
        "read_title": "The sum of the alternation",
        "read_intro": (
            "Hobbes defines deliberation in one long sentence, and the will in a few "
            "paragraphs on. The lab runs the sentence."
        ),
        "body": [
            ("p", "<strong>Chapter 6.</strong> &ldquo;In Deliberation, the last "
                  "Appetite, or Aversion, immediately adhaering to the action, or to "
                  "the omission thereof, is that wee call the Will; the Act, (not the "
                  "faculty,) of Willing.&rdquo;"),
            ("p", "A friend asks to borrow money. You are fond of him and sorry for "
                  "his trouble, and then you remember the last time. You think of what "
                  "his gratitude would be worth, and then you hear that others have "
                  "lent to him already. Over an afternoon you have wanted to lend and "
                  "wanted not to several times, and at some point you either did or did "
                  "not. Hobbes calls the whole afternoon deliberation, &ldquo;the whole "
                  "summe of Desires, Aversions, Hopes and Fears, continued till the "
                  "thing be either done, or thought impossible&rdquo;. And he calls "
                  "your will not the person who decided, nor a power of the mind that "
                  "stands above the afternoon, but only the last of the wantings."),
            ("p", "Take the words of his sentence one at a time. The sum is made of "
                  "appetites, aversions, hopes and fears, the passions of the last "
                  "lesson, and they arise alternately. It is a deliberation about "
                  "&ldquo;one and the same thing&rdquo;, a doing or an omitting. It ends "
                  "when the thing is done, or when it is thought impossible: "
                  "&ldquo;of things past, there is no Deliberation&rdquo;, and none of "
                  "things known to be impossible, though &ldquo;of things impossible, "
                  "which we think possible, we may Deliberate; not knowing it is in "
                  "vain&rdquo;. He derives the word with a flourish: it is called "
                  "deliberation &ldquo;because it is a putting an end to the Liberty we "
                  "had of doing, or omitting, according to our own Appetite, or "
                  "Aversion&rdquo;. And then he adds that this succession is no less in "
                  "other creatures, &ldquo;and therefore Beasts also Deliberate&rdquo;."),
            ("p", "The next sentence is the one in the passage. The will is the last "
                  "appetite or aversion adhering to the act or the omission, and Hobbes "
                  "adds at once that &ldquo;The Definition of the Will, given commonly "
                  "by the Schooles, that it is a Rationall Appetite, is not good. For if "
                  "it were, then could there be no Voluntary Act against Reason&rdquo;. A "
                  "voluntary act is one that proceeds from the will, so a man who acts "
                  "against his better judgement, as we all do, would have acted "
                  "involuntarily. He offers a repair: put &ldquo;an Appetite resulting from a "
                  "precedent Deliberation&rdquo; in place of &ldquo;Rationall "
                  "Appetite&rdquo;, and the schools' definition becomes his own. "
                  "&ldquo;Will therefore is the last Appetite in Deliberating&rdquo;."),
            ("p", "So what of the times when you meant to lend? He answers that "
                  "&ldquo;a man had a Will once to do a thing, that neverthelesse he "
                  "forbore to do&rdquo; is said in common talk, &ldquo;yet that is "
                  "properly but an Inclination, which makes no Action Voluntary; because "
                  "the action depends not of it, but of the last Inclination, or "
                  "Appetite&rdquo;. And he gives an argument for it: if the intervening "
                  "appetites made an action voluntary, then by the same reason the "
                  "intervening aversions would make it involuntary, so that &ldquo;one "
                  "and the same action, should be both Voluntary &amp; "
                  "Involuntary&rdquo;. That is the argument the lab lets you check by "
                  "counting."),
            ("p", "Here is the lab. A deliberation is a list of steps, each an "
                  "appetite or an aversion directed at doing the thing or omitting it. "
                  "The lab reports how many steps there are, how often the direction "
                  "changes, the will, which is the last step read as a will to do or to "
                  "omit, and the outcome. And it asks what Hobbes's definition "
                  "implies for the earlier steps: had the deliberation stopped after "
                  "each of them, what would the will have been, and in how many of "
                  "those cases the opposite of what it was. In the lend preset the five "
                  "steps are pity, fear of loss, hope of gratitude, a rumour of other "
                  "debts and a confirmation of the rumour. The last is an aversion to "
                  "lending, so the will is to omit and the loan is not made, and two "
                  "of the four earlier stops, after pity and after hope, would have "
                  "given the opposite will."),
            ("p", "The reversed preset keeps the same five motions in a different "
                  "order. The rumour and its confirmation come first, and pity and "
                  "hope of gratitude last, so the will is to lend and he lends. Nothing "
                  "about the friend or the money has changed, and the will is the "
                  "opposite. That is what &ldquo;last&rdquo; means in his definition, "
                  "and it is why the schools' rational appetite has no place in "
                  "his definition: what decides is the order in which the passions "
                  "come, not which is wiser."),
            ("p", "The storm preset is a case Hobbes himself uses, though not until Chapter 21. A shipmaster, in "
                  "a gale, deliberates whether to throw the cargo overboard: the "
                  "cargo is his year's profit, the ship may founder, the owners "
                  "will be angry, the next wave is higher. The last step is a fear of "
                  "what follows if he omits it, and so the will is to throw it, which he does. "
                  "Hobbes says plainly that such acts are voluntary: &ldquo;not onely "
                  "actions that have their beginning from Covetousnesse, Ambition, Lust, "
                  "or other Appetites to the thing propounded; but also those that have "
                  "their beginning from Aversion, or Feare of those consequences that "
                  "follow the omission, are voluntary actions&rdquo;. In Chapter 21 he "
                  "gives it: &ldquo;Feare, and Liberty are "
                  "consistent&rdquo;, for a man who throws his goods into the sea for "
                  "fear the ship should sink does it &ldquo;very willingly&rdquo;. The "
                  "impossible "
                  "preset is the lend deliberation with the friend gone abroad: it "
                  "has an end, because the thing is thought impossible, and the lab "
                  "still finds a last appetite, but no act."),
            ("p", "A critic has three things to say. The first is that the "
                  "definition makes the will the winner by stipulation: whichever "
                  "appetite happens to come last is the will, however idle. Hobbes "
                  "simply defines it so, and the dispute is over whether anything else "
                  "could count as a will. The second comes from Bishop "
                  "Bramhall, who held that the will is a power that can choose among "
                  "the motions that press on it, so that the last appetite is "
                  "its result, not its identity, and that if it is only "
                  "the last of a chain of causes there is no liberty. Hobbes "
                  "says in Chapter 21 that liberty is &ldquo;the absence of "
                  "Opposition&rdquo;, a point for a later course. The third is the beasts: "
                  "a reader may think that to give animals a will empties the "
                  "word, though Hobbes says plainly that beasts that deliberate "
                  "must also have will."),
            ("p", "The chapter ends with three things the lab leaves alone. Hobbes "
                  "says the passions are expressed in speech in forms that are not "
                  "affirmations: deliberation in the subjunctive, &ldquo;If this be "
                  "done, then this will follow&rdquo;, and desire and aversion in the "
                  "imperative. He says that the good or evil of an action depends on "
                  "&ldquo;the foresight of a long chain of consequences, of which very "
                  "seldome any man is able to see to the end&rdquo;, and that he who "
                  "has &ldquo;the greatest and surest prospect of Consequences, "
                  "Deliberates best himselfe&rdquo;. And he defines felicity as "
                  "&ldquo;Continuall successe in obtaining those things which a man from "
                  "time to time desireth&rdquo;, for there is no perpetual tranquillity "
                  "of mind while we live, &ldquo;because Life it selfe is but Motion, "
                  "and can never be without Desire, nor without Feare&rdquo;."),
            ("p", "Chapter 7 moves from deliberation about what to do to the search "
                  "for what is true. The next lesson, <em>The Ends of "
                  "Discourse</em>, shows him treating the two as parallel chains, "
                  "the last appetite being the will and the last opinion being the "
                  "judgement."),
        ],
        "lab": ("levkit", {
            "mode": "deliberate",
            "view": "will",
            "preset": "lend",
            "presets": [
                {"id": "lend", "label": "Whether to lend a friend money: five steps",
                 "action": "lend",
                 "steps": [
                     ["pity-for-his-trouble", "appetite", "do"],
                     ["fear-of-losing-the-money", "aversion", "do"],
                     ["hope-of-his-gratitude", "appetite", "do"],
                     ["a-rumour-of-other-debts", "aversion", "do"],
                     ["the-rumour-is-confirmed", "aversion", "do"],
                 ],
                 "expect": {"ldeWill": "to omit (the-rumour-is-confirmed: aversion toward doing)", "ldeOutcome": "lend omitted", "ldeOpposite": "2 of 4: pity-for-his-trouble, hope-of-his-gratitude", "ldeAlternations": "3"}},
                {"id": "reversed", "label": "The same five motions in another order",
                 "action": "lend",
                 "steps": [
                     ["a-rumour-of-other-debts", "aversion", "do"],
                     ["the-rumour-is-confirmed", "aversion", "do"],
                     ["fear-of-losing-the-money", "aversion", "do"],
                     ["pity-for-his-trouble", "appetite", "do"],
                     ["hope-of-his-gratitude", "appetite", "do"],
                 ],
                 "expect": {"ldeWill": "to do (hope-of-his-gratitude: appetite toward doing)", "ldeOutcome": "lend done", "ldeOpposite": "3 of 4: a-rumour-of-other-debts, the-rumour-is-confirmed, fear-of-losing-the-money", "ldeAlternations": "1"}},
                {"id": "storm", "label": "A shipmaster in a gale: throw the cargo overboard",
                 "action": "jettison",
                 "steps": [
                     ["the-cargo-is-the-whole-profit", "aversion", "do"],
                     ["the-ship-may-founder", "fear", "omit"],
                     ["the-owners-will-be-angry", "aversion", "do"],
                     ["the-next-wave-is-higher", "fear", "omit"],
                 ],
                 "expect": {"ldeWill": "to do (the-next-wave-is-higher: fear toward omitting, an aversion)", "ldeOutcome": "jettison done", "ldeOpposite": "2 of 3: the-cargo-is-the-whole-profit, the-owners-will-be-angry", "ldeAlternations": "3"}},
                {"id": "impossible", "label": "Lending, until the friend has left the country",
                 "action": "lend",
                 "steps": [
                     ["pity-for-his-trouble", "appetite", "do"],
                     ["fear-of-losing-the-money", "aversion", "do"],
                     ["hope-of-his-gratitude", "appetite", "do"],
                 ],
                 "end": "impossible",
                 "expect": {"ldeWill": "to do (hope-of-his-gratitude: appetite toward doing)", "ldeOutcome": "lend not done: thought impossible", "ldeOpposite": "1 of 2: fear-of-losing-the-money", "ldeAlternations": "2"}},
            ],
            "panel_title": "Where does the will fall?",
            "panel_intro": (
                "Each step is an appetite or an aversion toward doing or omitting the act, "
                "in the order it arose. The lab takes the last as the will, and then asks "
                "what the will would have been had the deliberation stopped at each "
                "earlier step. Run the four presets, then add or remove a step."
            ),
        }),
        "steps_title": "Finding the will in a deliberation",
        "steps_intro": "Four steps, in the order they arise.",
        "steps": [
            ("Write the steps in order",
             "List each appetite, aversion, hope or fear as it came, and mark each as "
             "directed at doing the thing or at omitting it."),
            ("Read each as a lean toward doing or omitting",
             "An appetite for doing and an aversion from omitting both lean toward "
             "doing; an aversion from doing and an appetite for omitting both lean "
             "toward omitting."),
            ("Take the last",
             "The will is the last step, read as a will to do or a will to omit. Count "
             "the changes of direction along the way as the alternation."),
            ("Test each earlier stop",
             "Ask what the will would have been had it ended at that step. Each earlier "
             "step that leans the other way was an inclination and not the will."),
        ],
        "worked": {
            "title": "The lend deliberation",
            "intro": [
                "The five steps of the first preset, with the direction each leans.",
            ],
            "lines": [
                "1 pity: do   2 fear of loss: omit   3 hope: do",
                "4 rumour: omit   5 confirmed: omit",
                "last step: aversion from doing, so the will is to omit",
                "earlier stops leaning to do: after 1 and after 3",
                "2 of the 4 earlier stops would have given the opposite will",
            ],
            "after": [
                "Pity and hope were inclinations, in Hobbes's word, and the loan was "
                "not made. The direction changed three times between the first step "
                "and the fourth.",
            ],
        },
        "quiz_title": "What the will is",
        "quiz": [
            {"q": "How does Hobbes define the will?",
             "a": ["The strongest appetite in the mind",
                   "The last appetite or aversion in deliberation, immediately adhering to the act or its omission",
                   "A rational appetite",
                   "The first appetite felt about a thing"],
             "c": 1,
             "why": "The will is the last appetite or aversion immediately adhering to "
                    "the action or to its omission. He rejects the schools' rational "
                    "appetite because it would leave no voluntary act against reason. "
                    "Strength is not mentioned: an earlier appetite, however strong, is "
                    "an inclination."},
            {"q": "In the lend preset, how many of the four earlier stops would have "
                  "given the opposite will, had the deliberation ended there?",
             "a": ["None", "One", "Two", "Four"],
             "c": 2,
             "why": "The last step is an aversion from lending, so the will is to omit. "
                    "Stopping after pity or after hope of gratitude would have given a "
                    "will to lend, and stopping after fear or the rumour would have given "
                    "a will to omit."},
            {"q": "A shipmaster throws his cargo overboard in a storm out of fear of "
                  "drowning. On Hobbes's account, is the act voluntary?",
             "a": ["No, because it was done from fear and not from desire",
                   "No, because he would rather have kept the cargo",
                   "Yes, because it proceeds from the last aversion, fear of what follows "
                   "from omitting it",
                   "Only if he first reasoned about it calmly"],
             "c": 2,
             "why": "Actions that begin from aversion or fear of the consequences of "
                    "omitting are voluntary actions, since the will is the last "
                    "appetite or aversion whatever its source. The earlier aversion to "
                    "losing the cargo was an inclination, and no calm reasoning is "
                    "required, since the will is not a rational appetite."},
            {"q": "Why does Hobbes say deliberation is so called?",
             "a": ["Because it is the weighing of reasons by a free will",
                   "Because it puts an end to the liberty we had of doing or omitting "
                   "according to our appetite or aversion",
                   "Because only men and not beasts can do it",
                   "Because it ends when we reach the right answer"],
             "c": 1,
             "why": "His derivation is that deliberation is a putting an end to the "
                    "liberty we had. He says beasts also deliberate, and a deliberation "
                    "ends when the thing is done or thought impossible, not when the "
                    "answer is right."},
        ],
        "mistakes": [
            ("Thinking an earlier strong wish was the will",
             "Common speech says a man had a will once to do a thing that he did not "
             "do. Hobbes calls that &ldquo;properly but an Inclination&rdquo;. In the "
             "lend preset pity and hope of gratitude both lean toward lending, and "
             "neither was the will, because the action did not depend on them but on "
             "the last step."),
            ("Making the will a rational power that overrules appetite",
             "That is the schools' definition, and Hobbes rejects it because it would "
             "make acting against reason impossible. The will is an appetite, the last "
             "one. A reader who wants the will to be a faculty above the passions is "
             "taking the side of Bishop Bramhall, a side the lab neither takes nor "
             "refutes."),
            ("Treating an act done from fear as involuntary",
             "Hobbes says that acts that begin from aversion or fear of the "
             "consequences of omitting are voluntary. The shipmaster who jettisons his "
             "cargo wills to jettison it: his last step is a fear that leans toward "
             "doing."),
        ],
        "standard": (
            "Finish when you can find the will in a deliberation and say what the "
            "earlier stops would have given.",
            "Given a deliberation as a list of appetites and aversions toward doing or "
            "omitting, name the will, say whether the act was done or omitted, and "
            "count the earlier stops that would have given the opposite will."
        ),
        "note": (
            "The lab applies Hobbes's definition of the will to deliberations written "
            "for this lesson. It cannot say whether the last appetite is a free choice, "
            "which is the question he and Bramhall argued, or whether people deliberate "
            "in the clean alternation the steps show. The reading of fear as an "
            "aversion that leans toward the opposite act is a convention of the lab."
        ),
    },
]
