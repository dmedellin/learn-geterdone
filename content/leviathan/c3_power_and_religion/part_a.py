"""Power, Manners and Religion, lessons 1-5 -- Leviathan, Part I, Chapters 10-12.

Every quotation is copied from the operator's copy of the 1651 text and checked
against the page image; the comment beside each lesson gives its chapter, the
1651 page and the PDF page of that copy. Italics are dropped, small capitals
(WORTH, DIGNITY) are printed as capitals, and nothing else is changed.

Lessons 1 and 2 use the levkit lab; lessons 3, 4 and 5 use choicekit and argkit.
"""

# ---------------------------------------------------------------- 01
# Leviathan ch. 10, 1651 p. 41 (opening) and p. 42 (worth); PDF pp. 158-159 of the operator's copy.
POWER_AND_WORTH = {
    "slug": "power-and-worth",
    "title": "Power and Worth",
    "module": "Chapter 10 · Of Power, Worth, Dignity, Honour, and Worthinesse",
    "one_line": "A man's power is his present means to some future good, and his worth is what a buyer would give for it, so no ranking of men is absolute.",
    "summary": (
        "Hobbes opens Chapter 10 by defining power, splitting it into natural power and "
        "the instrumental powers those make possible, and then defines a man's worth as "
        "his price: not what he thinks he is worth, but what another would give for the "
        "use of his power. Price four men's powers for three buyers with different needs "
        "and see why no man comes out on top for every buyer."
    ),
    "key": [
        "power: present means to a future good",
        "natural: strength, prudence, eloquence",
        "instrumental: riches, reputation, friends",
        "worth = price = what a buyer would give",
        "price = sum of need × amount of each power",
    ],
    "key_label": "Power and worth in five lines",
    "concepts_intro": (
        "Chapter 10 begins with two definitions, and the second depends on the first. "
        "Power comes first, then the price of power."
    ),
    "concepts": [
        ("Power as present means",
         "Power, &ldquo;to take it Universally&rdquo;, is a man's present means to "
         "obtain some future apparent good. It is not a feeling or a right. It is what "
         "he can bring to bear now, and it is counted by what it can get him."),
        ("Natural and instrumental power",
         "Natural power is the eminence of the faculties of body or mind: strength, "
         "form, prudence, eloquence. Instrumental powers are acquired by these or by "
         "fortune and are themselves means to acquire more: riches, reputation, friends, "
         "and what men call good luck. Power breeds power."),
        ("Worth as price",
         "A man's value is, like that of any other thing, his price: what would be "
         "given for the use of his power. It depends on the buyer's need and judgement, "
         "so it is not absolute, and it is the buyer, not the seller, who sets it."),
    ],
    "read_title": "The passage first, then the chapter line by line",
    "read_intro": (
        "Hobbes's definition of power comes first. The definition of worth, a page "
        "later, is quoted in the middle of the lesson, where it is needed."
    ),
    "body": [
        ("p", "<strong>Chapter 10.</strong> &ldquo;The POWER of a Man, (to take it "
              "Universally,) is his present means, to obtain some future apparent Good. "
              "And is either Originall, or Instrumentall.&rdquo;"),
        ("p", "Think of the last time you were asked what you could do. A job interview "
              "is the plain case: you list the things you can do now and the interviewer "
              "wonders what those will fetch. That is more or less the shape of Hobbes's "
              "definition. Each word is doing something. &ldquo;present means&rdquo; says "
              "power is what you have in hand today, not what you hope to have. &ldquo;some "
              "future apparent Good&rdquo; says it is aimed at a good that seems so to the "
              "person who wants it, which is how Hobbes has defined good since the passions "
              "of Chapter 6. And &ldquo;Universally&rdquo; says he is defining power in "
              "general, for any man in any condition, before any commonwealth exists."),
        ("p", "He then divides it. &ldquo;Naturall Power, is the eminence of the Faculties "
              "of Body, or Mind: as extraordinary Strength, Forme, Prudence, Arts, "
              "Eloquence, Liberality, Nobility.&rdquo; Notice the list runs from the body "
              "(strength, good looks) through the mind (prudence, skill, speech) to "
              "something half-social, nobility, which Hobbes says a few lines later is "
              "power only &ldquo;in those Commonwealths, where it has Priviledges&rdquo;. "
              "The instrumental powers are the ones &ldquo;which acquired by these, or by "
              "fortune, are means and Instruments to acquire more: as Riches, Reputation, "
              "Friends&rdquo;, together with what he calls the &ldquo;secret working of "
              "God&rdquo; that men name good luck."),
        ("p", "The reason for the second kind is in the next sentence. &ldquo;For the "
              "nature of Power, is in this point, like to Fame, increasing as it "
              "proceeds&rdquo;, and like falling bodies, which go faster the further they "
              "go. Money buys friends, friends bring protection, protection lets you earn "
              "more. Keep that image in mind, because Chapter 11 will turn it into a "
              "claim about every human being: that no one stops."),
        ("p", "Hobbes then walks through what counts as power, and the list is a short "
              "tour of his picture of society. To have servants is power, and to have "
              "friends is power, &ldquo;for they are strengths united&rdquo;. Riches are "
              "power only when joined with liberality, because generosity buys friends, "
              "and otherwise they merely expose a man &ldquo;to Envy, as a Prey&rdquo;. "
              "Reputation of power is power, since it draws the adherence of those who need "
              "protection. Eloquence is power because it is seeming prudence, and the "
              "sciences are only &ldquo;small Power&rdquo;, since few can recognise them. "
              "The greatest human power is &ldquo;compounded of the Powers of most men, "
              "united by consent, in one person&rdquo;: a commonwealth, or a faction. Hobbes "
              "had left England in 1640 and watched the Civil War from Paris, so he had "
              "seen what united strengths could do to a king."),
        ("p", "Now the definition of worth, which is the part this lesson computes. "
              "<strong>Chapter 10.</strong> &ldquo;The Value, or WORTH of a man, is as of "
              "all other things, his Price; that is to say, so much as would be given for "
              "the use of his Power: and therefore is not absolute; but a thing dependant "
              "on the need and judgement of another.&rdquo;"),
        ("def", ("Worth (Hobbes's word: value)",
                 "What would be given for the use of a man's power. It is set by the "
                 "buyer's need and judgement, not by the man, and so it changes from one "
                 "buyer to another.")),
        ("p", "Hobbes gives his own two examples straight away. &ldquo;An able conductor "
              "of Souldiers, is of great Price in time of War present, or imminent; but in "
              "Peace not so. A learned and uncorrupt Judge, is much Worth in time of Peace; "
              "but not so much in War.&rdquo; The men did not change between the two "
              "sentences and neither did their powers. The buyer changed, or rather the "
              "buyer's need did, and the price went with it. Then the sentence that does "
              "the most work: &ldquo;not the seller, but the buyer determines the "
              "Price&rdquo;, and a man who rates himself as high as he can finds that "
              "&ldquo;their true Value is no more than it is esteemed by others&rdquo;."),
        ("p", "The lab makes this a sum. Four men, each with an amount of four powers: "
              "the general has strength 8, prudence 5, eloquence 2 and riches 1; the "
              "judge, 1, 8, 4 and 2; the orator, 1, 3, 9 and 1; the merchant, 2, 4, 2 "
              "and 8. These amounts are invented for the lesson, as are the buyers: a "
              "city at war, which needs strength 3, prudence 2, eloquence 1 and riches 1; "
              "a city at peace, 0, 3, 2 and 1; and a faction hunting for support, "
              "1, 0, 3 and 2. A buyer's price for a man is the sum, over the four powers, "
              "of the buyer's need times the man's amount. The three-buyers preset prices "
              "everyone for all three: the war buyer pays 37 for the general and 19 for "
              "the orator, the peace buyer pays 34 for the judge and 20 for the general, "
              "and the faction pays 30 for the orator and 16 for the general. Three buyers, "
              "three different men at the top, and the merchant, who is never best, is "
              "priced 24 by every one of them."),
        ("p", "Hobbes's own contrast is the shifted-need preset. Let the war buyer's "
              "need change to 1, 2, 1 and 1, which is a buyer who has stopped wanting "
              "strength and wants cool heads. The general falls from 37 to 21 and the "
              "judge, though he too falls, from 25 to 23, is now the top-priced man. The "
              "one-buyer preset leaves only the war buyer, and shows what an ordinary "
              "ranking looks like when there is just one set of needs: perfectly "
              "definite, and for that buyer alone."),
        ("p", "There is a fair objection to the whole idea, and the next lesson takes it "
              "up. Immanuel Kant wrote in 1785 that whatever has a price can be replaced "
              "by an equivalent, while a person has a dignity above all price. To price "
              "a person, on that view, treats as replaceable what has no equivalent. "
              "Hobbes defines worth as price and then, in the sentences that follow, "
              "defines a different word, dignity, for what the commonwealth sets. The "
              "next lesson, <em>Honour, Dignity and Worthiness</em>, "
              "takes up what honour is and how the commonwealth's valuation can differ "
              "from every buyer's."),
    ],
    "lab": ("levkit", {
        "mode": "worth",
        "view": "price",
        "preset": "three-buyers",
        "presets": [
            {"id": "three-buyers", "label": "Four men priced by a city at war, a city at peace and a faction",
             "powers": ["strength", "prudence", "eloquence", "riches"],
             "persons": [
                 ["general", 8, 5, 2, 1],
                 ["judge", 1, 8, 4, 2],
                 ["orator", 1, 3, 9, 1],
                 ["merchant", 2, 4, 2, 8],
             ],
             "buyers": [
                 ["war", 3, 2, 1, 1],
                 ["peace", 0, 3, 2, 1],
                 ["faction", 1, 0, 3, 2],
             ],
             "expect": {"lwoPrices": "war: general 37, judge 25, orator 19, merchant 24; peace: general 20, judge 34, orator 28, merchant 24; faction: general 16, judge 17, orator 30, merchant 24", "lwoTop": "war: general; peace: judge; faction: orator", "lwoSame": "no: on general and judge, war ranks general above judge and peace ranks judge above general"}},
            {"id": "shifted-need", "label": "The war buyer now wants prudence, 1, 2, 1, 1",
             "powers": ["strength", "prudence", "eloquence", "riches"],
             "persons": [
                 ["general", 8, 5, 2, 1],
                 ["judge", 1, 8, 4, 2],
                 ["orator", 1, 3, 9, 1],
                 ["merchant", 2, 4, 2, 8],
             ],
             "buyers": [
                 ["war", 1, 2, 1, 1],
                 ["peace", 0, 3, 2, 1],
                 ["faction", 1, 0, 3, 2],
             ],
             "expect": {"lwoPrices": "war: general 21, judge 23, orator 17, merchant 20; peace: general 20, judge 34, orator 28, merchant 24; faction: general 16, judge 17, orator 30, merchant 24", "lwoTop": "war: judge; peace: judge; faction: orator", "lwoSame": "no: on general and orator, war ranks general above orator and peace ranks orator above general"}},
            {"id": "one-buyer", "label": "Only the city at war",
             "powers": ["strength", "prudence", "eloquence", "riches"],
             "persons": [
                 ["general", 8, 5, 2, 1],
                 ["judge", 1, 8, 4, 2],
                 ["orator", 1, 3, 9, 1],
                 ["merchant", 2, 4, 2, 8],
             ],
             "buyers": [
                 ["war", 3, 2, 1, 1],
             ],
             "expect": {"lwoPrices": "war: general 37, judge 25, orator 19, merchant 24", "lwoTop": "war: general", "lwoSame": "one buyer only: nothing to compare"}},
        ],
        "panel_title": "What four men are worth to three buyers",
        "panel_intro": (
            "Each buyer's need for each power and each man's amount of it go in; the lab "
            "multiplies, adds, and ranks the men for each buyer. Change one need and watch "
            "which man moves."
        ),
    }),
    "steps_title": "Pricing a man for a buyer",
    "steps_intro": "Four steps, the same for any number of men and buyers.",
    "steps": [
        ("List each man's powers",
         "Write the amount of each power he has. Count the instrumental ones, riches "
         "and friends, as well as the natural ones."),
        ("State the buyer's need",
         "For each power, say how much this buyer wants it. A need of zero means the "
         "buyer would pay nothing for that power however much of it a man has."),
        ("Price the man",
         "Multiply the buyer's need by the man's amount for each power, and add. The "
         "total is what this buyer would give for the use of his power."),
        ("Rank, then compare buyers",
         "Order the men by price for each buyer. If two buyers order any pair "
         "differently, no ranking of the men is absolute: it depends on who is buying."),
    ],
    "worked": {
        "title": "The general and the judge, priced by war and by peace",
        "intro": [
            "Take the first preset. The war buyer needs strength 3, prudence 2, eloquence "
            "1 and riches 1. The general has 8, 5, 2 and 1; the judge 1, 8, 4 and 2.",
        ],
        "lines": [
            "war buyer, general:  3·8 + 2·5 + 1·2 + 1·1 = 37",
            "war buyer, judge:  3·1 + 2·8 + 1·4 + 1·2 = 25",
            "peace buyer, general:  0·8 + 3·5 + 2·2 + 1·1 = 20",
            "peace buyer, judge:  0·1 + 3·8 + 2·4 + 1·2 = 34",
        ],
        "after": [
            "The war buyer puts the general twelve above the judge, and the peace buyer "
            "puts the judge fourteen above the general. Neither is mistaken: they need "
            "different things. This is Hobbes's conductor of soldiers and learned judge "
            "with numbers in place of adjectives.",
        ],
    },
    "quiz_title": "Price set by the buyer",
    "quiz": [
        {"q": "In the three-buyers preset the war buyer needs strength 3, prudence 2, "
              "eloquence 1 and riches 1. The judge has 1, 8, 4 and 2. What does the war "
              "buyer give for the judge?",
         "a": ["34", "17", "25", "30"],
         "c": 2,
         "why": "`3·1 + 2·8 + 1·4 + 1·2 = 3 + 16 + 4 + 2 = 25`. Thirty-four is the peace "
                "buyer's price for the same judge, seventeen is the faction's, and thirty "
                "is the faction's price for the orator."},
        {"q": "On Hobbes's account, what settles a man's worth?",
         "a": ["His own estimate of himself",
               "The amount of power he has, whoever is buying",
               "What a buyer, by need and judgement, would give for the use of his power",
               "How much he deserves by his conduct"],
         "c": 2,
         "why": "Worth is his price, &ldquo;dependant on the need and judgement of "
                "another&rdquo;. His own estimate does not count, since &ldquo;not the "
                "seller, but the buyer determines the Price&rdquo;. The amount of power "
                "is one input, and Hobbes separates worth from merit and desert later in "
                "the chapter."},
        {"q": "Which of these is an instrumental power in Hobbes's list, as opposed to a "
              "natural power?",
         "a": ["Extraordinary strength", "Prudence", "Eloquence", "Friends"],
         "c": 3,
         "why": "Friends are among the powers &ldquo;acquired by these, or by "
                "fortune&rdquo; that are &ldquo;means and Instruments to acquire "
                "more&rdquo;, with riches and reputation. Strength, prudence and "
                "eloquence are on his list of natural powers."},
        {"q": "Which statement follows from the three-buyers figures?",
         "a": ["The general is priced highest by every buyer",
               "No man is priced highest by all three buyers",
               "The merchant is priced lowest by every buyer",
               "The buyers who rank differently must have mistaken the prices"],
         "c": 1,
         "why": "The general tops the war buyer's list, the judge the peace buyer's and "
                "the orator the faction's, so no one is first for all three. The "
                "merchant is never lowest (the orator is for war, the general for peace "
                "and for the faction), and the buyers set the prices by their needs, so there "
                "is no mistake to find."},
    ],
    "mistakes": [
        ("Thinking a man's worth is a quality in him, the same for everyone",
         "Hobbes says the opposite: worth &ldquo;is not absolute&rdquo;. In the "
         "three-buyers preset the same judge is worth 25, 34 and 17 depending on who is "
         "buying, and the general is worth 37 to one buyer and 16 to another. Nothing "
         "about either man changed."),
        ("Counting only strength and skill as power",
         "Hobbes's list of what counts as power runs well past strength and skill: "
         "riches (with liberality), reputation, "
         "friends, popularity, good success, affability. In the lab, the merchant's riches "
         "are what make him worth 24 to a faction hunting for support, though no one "
         "would call him strong."),
        ("Reading a high price as a verdict on the man",
         "Worth is price, and a price says what a buyer needs. Hobbes keeps merit and "
         "worthiness for other ideas, and the next lesson reaches them. A man the war "
         "buyer prices at 37 may be a worse man than one priced at 19, and the table "
         "has nothing to say about it."),
    ],
    "standard": (
        "Finish when you can price a man for a buyer and say whether two buyers rank "
        "the same.",
        "Given the powers of several men and the needs of several buyers, compute each "
        "buyer's price for each man, rank them, and say whether the buyers' rankings "
        "agree and which pair first disagrees."
    ),
    "note": (
        "The lab adds need times amount for each power, and so assumes that a buyer's "
        "needs are fixed numbers and that powers can be added; Hobbes states neither. "
        "He says worth is a price and depends on need and judgement, which the sum "
        "illustrates and does not prove. The men and the buyers are invented, and "
        "the lab cannot say whether any person's worth, in a sense a person would "
        "recognise, is a price at all."
    ),
}

# ---------------------------------------------------------------- 02
# Leviathan ch. 10, 1651 pp. 42-44 (dignity, honour, Mordecai) and p. 47 (worthiness); PDF pp. 159-161 and 165 of the operator's copy.
HONOUR_AND_DIGNITY = {
    "slug": "honour-and-dignity",
    "title": "Honour, Dignity and Worthiness",
    "module": "Chapter 10 · Of Power, Worth, Dignity, Honour, and Worthinesse",
    "one_line": "Honour is the sign of the value we set on a man, dignity is the value the commonwealth sets, and neither is the same as his worth or his worthiness.",
    "summary": (
        "The rest of Chapter 10 sorts out four words that ordinary speech runs "
        "together: honour, dignity, worth and worthiness. Honouring is the outward sign "
        "of a valuation, dignity is the valuation the commonwealth makes by office and "
        "title, and worthiness is fitness for a charge. Put a dignity beside the men's "
        "prices from the last lesson and see who the commonwealth honours above or "
        "below what any buyer would give."
    ),
    "key": [
        "honour: the sign of the value set on a man",
        "dignity: public worth, set by the sovereign",
        "civil honour depends on the sovereign's will",
        "honour consists in the opinion of power",
        "worthiness: fitness, not worth or merit",
    ],
    "key_label": "Four words kept apart",
    "concepts_intro": (
        "Chapter 10 ends by separating words that are used for one another. Each is "
        "defined, and each is tied back to power."
    ),
    "concepts": [
        ("Honour",
         "&ldquo;The manifestation of the Value we set on one another&rdquo; is "
         "honouring and dishonouring. To value a man highly is to honour him, and to "
         "value him low is to dishonour him, measured against the rate he sets on "
         "himself. Obeying him, praying to him and giving him great gifts are all "
         "honours, because each is a sign that he is thought to have power."),
        ("Dignity",
         "The public worth of a man is the value the commonwealth sets on him, and men "
         "call it dignity. It is shown by offices of command, judicature and public "
         "employment, and by names and titles made for distinguishing such value. Its "
         "fountain is the sovereign's will."),
        ("Worthiness",
         "Worthiness is a different thing from worth and from merit: a particular "
         "ability or fitness for what a man is said to be worthy of. A man may be worthy "
         "of an office and yet have no right to it, and then he does not merit it."),
    ],
    "read_title": "The passage first, then the chapter line by line",
    "read_intro": (
        "The definition of dignity opens the lesson. The scene of the King of Persia "
        "and the account of worthiness are quoted where the lesson reaches them."
    ),
    "body": [
        ("p", "<strong>Chapter 10.</strong> &ldquo;The publique worth of a man, which is "
              "the Value set on him by the Common-wealth, is that which men commonly call "
              "DIGNITY. And this Value of him by the Common-wealth, is understood, by "
              "offices of Command, Judicature, publike Employment; or by Names and Titles, "
              "introduced for distinction of such Value.&rdquo;"),
        ("p", "In the last lesson the buyers were private: a city, a faction. Here the "
              "buyer is the commonwealth itself, which can set a value on a man that no "
              "one else's need would give him, and can set it by a stroke of the pen. "
              "Think of a title or a rank: it costs the man nothing to be addressed by it "
              "and it changes what everyone around him does. That is why Hobbes "
              "calls dignity a man's <em>public</em> worth: a worth, but one set by a single "
              "buyer whose valuation binds everyone."),
        ("p", "Before it, though, he has defined honour, and the order matters. "
              "&ldquo;The manifestation of the Value we set on one another, is that "
              "which is commonly called Honouring, and Dishonouring.&rdquo; Honour is "
              "the sign. And it is measured relatively: &ldquo;high, and low, in this "
              "case, is to be understood by comparison to the rate that each man setteth "
              "on himselfe.&rdquo; Praise a man at exactly the rate he sets on himself "
              "and you have neither honoured nor insulted him."),
        ("p", "Then comes a long list of ways of honouring, and its logic is the same "
              "every time. &ldquo;To pray to another, for ayde of any kind, is to "
              "HONOUR; because a signe we have an opinion he has power to help&rdquo;. "
              "&ldquo;To obey, is to Honour; because no man obeyes them, whom they think "
              "have no power to help, or hurt them.&rdquo; Great gifts honour, because "
              "they buy protection; little gifts dishonour, because they are alms. "
              "To give way, to agree, to imitate, to trust, to hearken to counsel are all "
              "honours, and the opposites are all dishonours. Each is read as a signal of "
              "an opinion about power, which is why the chapter defines honourable "
              "things the way it does: &ldquo;Honourable is whatsoever possession, action, "
              "or quality, is an argument and signe of Power.&rdquo;"),
        ("p", "It follows, and Hobbes says so plainly, that honour has nothing to do "
              "with justice. &ldquo;Nor does it alter the case of Honour, whether an action "
              "(so it be great and difficult, and consequently a signe of much power,) be "
              "just or unjust: for Honour consisteth onely in the opinion of Power.&rdquo; "
              "His examples are the adulteries of Jupiter, piracy, a lawful trade "
              "among the Greeks and other nations before great commonwealths, and the duel in his own day. It is among the harder passages of the "
              "chapter, and it is worth noticing that he describes what men honour, "
              "not what they should."),
        ("p", "Then the commonwealth's own honours, and his best scene. &ldquo;The King "
              "of Persia, Honoured Mordecay, when he appointed he should be conducted "
              "through the streets in the Kings Garment, upon one of the Kings Horses, "
              "with a Crown on his head, and a Prince before him, proclayming, Thus shall "
              "it be done to him that the King will honour&rdquo;. (It is from the Book of "
              "Esther.) Another King of Persia, to a man who asked to wear one of the "
              "royal robes, gave leave &ldquo;but with this addition, that he should weare "
              "it as the Kings foole; and then it was Dishonour.&rdquo; The same robe, the "
              "same horse. What made the difference was what the sovereign meant by it, "
              "and Hobbes draws the moral: &ldquo;So that of Civill Honour, the Fountain is "
              "in the person of the Common-wealth, and dependeth on the Will of the "
              "Soveraigne&rdquo;."),
        ("p", "That is dignity, and the lab shows the difference between it and worth. "
              "The same four men are here, with the same buyers. Now the commonwealth "
              "sets each man a dignity: 40 for the general, who has been made a duke; 34 "
              "for the judge; 10 for the orator, who holds no office; 15 for the merchant. "
              "These are invented figures, as the prices were. The titles preset puts them "
              "beside the three prices of each man. The general's dignity is above every "
              "buyer's price for him; the judge's is above two and equal to the third, "
              "the peace buyer's 34; the orator's and the merchant's are below. "
              "Everyone's dignity but the judge's differs from all three prices."),
        ("p", "The raised-orator preset has the commonwealth raise the orator to 30. "
              "That equals what the faction would give for him, and is above the "
              "war buyer's 19 and the peace buyer's 28. The market preset sets every man's "
              "dignity at what the peace buyer would pay, 20, 34, 28 and 24, and nothing "
              "then differs from that buyer's price. Hobbes is not saying the "
              "commonwealth should do either. He says dignity is an act of the sovereign, "
              "so it can fall anywhere."),
        ("p", "One word is left, and Hobbes keeps it apart from the others, in the "
              "short passage that closes the chapter. &ldquo;WORTHINESSE, is a thing "
              "different from the worth, or value of a man; and also from his merit, or "
              "desert&rdquo;. It is fitness: he is worthiest to be a commander who is "
              "best fitted with the qualities the command requires. A man may be worthy "
              "of riches or office and yet have no claim to it, and then he cannot be "
              "said to merit it, &ldquo;For Merit, praesupposeth a right, and that the "
              "thing deserved is due by promise&rdquo;, a matter Hobbes defers to the "
              "chapters on contracts. So there are four things: what a buyer would pay, "
              "what the sovereign has declared, what the man is fit for, and what he is "
              "owed. A single table cannot show the last two, and the lab does not try."),
        ("p", "The objection from the last lesson comes back here. Kant objects to "
              "worth as price: to price a person is to treat as replaceable what has no "
              "equivalent, and what a person has instead is a dignity that no price or "
              "title can add to or take away. Hobbes uses the word for nearly the "
              "reverse, a public valuation that the sovereign can raise or lower at "
              "will. The reply open to him, and the one his chapter bears out, is that "
              "he describes how men value one another, and says that honour consists "
              "only in the opinion of power; he does not say how they ought to. Whether "
              "a person can be priced at all is the question between them, and the "
              "lab cannot answer it."),
        ("p", "Chapter 10 ends there. The next lesson, <em>The Difference of "
              "Manners</em>, moves to Chapter 11, where Hobbes asks what all this "
              "reckoning of power does to the desires of the men who do it."),
    ],
    "lab": ("levkit", {
        "mode": "worth",
        "view": "price",
        "preset": "titles",
        "presets": [
            {"id": "titles", "label": "The commonwealth sets dignity: 40, 34, 10, 15",
             "powers": ["strength", "prudence", "eloquence", "riches"],
             "persons": [
                 ["general", 8, 5, 2, 1],
                 ["judge", 1, 8, 4, 2],
                 ["orator", 1, 3, 9, 1],
                 ["merchant", 2, 4, 2, 8],
             ],
             "buyers": [
                 ["war", 3, 2, 1, 1],
                 ["peace", 0, 3, 2, 1],
                 ["faction", 1, 0, 3, 2],
             ],
             "dignity": [
                 ["general", 40], ["judge", 34],
                 ["orator", 10], ["merchant", 15],
             ],
             "expect": {"lwoPrices": "war: general 37, judge 25, orator 19, merchant 24; peace: general 20, judge 34, orator 28, merchant 24; faction: general 16, judge 17, orator 30, merchant 24", "lwoDignity": "general 40: above war, above peace, above faction; judge 34: above war, equal to peace, above faction; orator 10: below war, below peace, below faction; merchant 15: below war, below peace, below faction", "lwoApart": "3: general, orator, merchant"}},
            {"id": "raised-orator", "label": "The commonwealth raises the orator to 30",
             "powers": ["strength", "prudence", "eloquence", "riches"],
             "persons": [
                 ["general", 8, 5, 2, 1],
                 ["judge", 1, 8, 4, 2],
                 ["orator", 1, 3, 9, 1],
                 ["merchant", 2, 4, 2, 8],
             ],
             "buyers": [
                 ["war", 3, 2, 1, 1],
                 ["peace", 0, 3, 2, 1],
                 ["faction", 1, 0, 3, 2],
             ],
             "dignity": [
                 ["general", 40], ["judge", 34],
                 ["orator", 30], ["merchant", 15],
             ],
             "expect": {"lwoPrices": "war: general 37, judge 25, orator 19, merchant 24; peace: general 20, judge 34, orator 28, merchant 24; faction: general 16, judge 17, orator 30, merchant 24", "lwoDignity": "general 40: above war, above peace, above faction; judge 34: above war, equal to peace, above faction; orator 30: above war, above peace, equal to faction; merchant 15: below war, below peace, below faction", "lwoApart": "2: general, merchant"}},
            {"id": "market", "label": "Dignity set equal to the peace buyer's price",
             "powers": ["strength", "prudence", "eloquence", "riches"],
             "persons": [
                 ["general", 8, 5, 2, 1],
                 ["judge", 1, 8, 4, 2],
                 ["orator", 1, 3, 9, 1],
                 ["merchant", 2, 4, 2, 8],
             ],
             "buyers": [
                 ["war", 3, 2, 1, 1],
                 ["peace", 0, 3, 2, 1],
                 ["faction", 1, 0, 3, 2],
             ],
             "dignity": [
                 ["general", 20], ["judge", 34],
                 ["orator", 28], ["merchant", 24],
             ],
             "expect": {"lwoPrices": "war: general 37, judge 25, orator 19, merchant 24; peace: general 20, judge 34, orator 28, merchant 24; faction: general 16, judge 17, orator 30, merchant 24", "lwoDignity": "general 20: below war, equal to peace, above faction; judge 34: above war, equal to peace, above faction; orator 28: above war, equal to peace, below faction; merchant 24: equal to war, equal to peace, equal to faction", "lwoApart": "0: none"}},
        ],
        "panel_title": "Dignity beside what a buyer would give",
        "panel_intro": (
            "The prices are the same as before; the commonwealth's dignity for each man "
            "is added, and the lab says whether it stands above, equal to or below each "
            "buyer's price. Change one dignity and see which comparisons move."
        ),
    }),
    "steps_title": "Comparing dignity with price",
    "steps_intro": "Four steps, starting from prices already computed.",
    "steps": [
        ("Price each man for each buyer",
         "Do the sum of the last lesson: need times amount for each power, added."),
        ("Write the dignity the commonwealth sets",
         "One number for each man. It comes from the sovereign's office or title, not "
         "from any buyer's need."),
        ("Compare, buyer by buyer",
         "For each man and each buyer, say whether the dignity is above, equal to or "
         "below the price."),
        ("Find the men the commonwealth values differently from everyone",
         "These are the men whose dignity equals none of the buyers' prices. Their "
         "public worth is an act of the sovereign, not a reflection of any market."),
    ],
    "worked": {
        "title": "The orator, with and without a title",
        "intro": [
            "The orator has strength 1, prudence 3, eloquence 9 and riches 1, and the "
            "buyers' prices for him are 19, 28 and 30. In the first preset the "
            "commonwealth has given him dignity 10.",
        ],
        "lines": [
            "war buyer:  10 against 19, below",
            "peace buyer:  10 against 28, below",
            "faction:  10 against 30, below",
            "after the raise, dignity 30:  above 19, above 28, equal to 30",
        ],
        "after": [
            "Raised to 30, the orator is honoured above what two buyers would give and "
            "exactly at the third's price. Nothing about his powers has changed, only "
            "the sovereign's valuation, which is the point of the passage about "
            "Mordecai.",
        ],
    },
    "quiz_title": "Four words kept apart",
    "quiz": [
        {"q": "In Hobbes's definition, who sets a man's dignity?",
         "a": ["The commonwealth, by offices and titles",
               "The man himself, by what he rates himself at",
               "Whichever buyer needs him most",
               "God, by the man's merit"],
         "c": 0,
         "why": "Dignity is &ldquo;the Value set on him by the Common-wealth&rdquo;, "
                "understood by offices and titles. The man's own rating is what honour "
                "is measured against, a buyer's need sets his worth, and merit is a "
                "separate idea, which presupposes a right."},
        {"q": "Why, on Hobbes's account, is it an honour to obey a man?",
         "a": ["Because obeying shows love of him",
               "Because it is a sign that he is thought to have power to help or hurt",
               "Because obedience is always just",
               "Because the one obeyed has deserved it"],
         "c": 1,
         "why": "&ldquo;To obey, is to Honour; because no man obeyes them, whom they "
                "think have no power to help, or hurt them.&rdquo; Honour is a sign of "
                "an opinion of power. Hobbes says it does not depend on whether the "
                "action is just, and merit is a separate matter."},
        {"q": "In the titles preset the judge's dignity is 34 and the peace buyer pays "
              "34 for him. What does the lab's comparison show?",
         "a": ["The commonwealth and the peace buyer value him equally",
               "The commonwealth honours him below the peace buyer",
               "The commonwealth must have copied the peace buyer's need",
               "The judge is worthy of his office"],
         "c": 0,
         "why": "The two figures are equal. That is all the lab shows. It does not show "
                "that the commonwealth copied anything, and worthiness is fitness for a "
                "charge, which no price or dignity measures."},
        {"q": "What is the difference between worthiness and merit, on the chapter's "
              "account?",
         "a": ["There is none; Hobbes uses them for one thing",
               "Merit is fitness for a charge; worthiness presupposes a right",
               "Worthiness is fitness for a charge; merit presupposes a right and a "
               "promise",
               "Worthiness is what the commonwealth sets; merit is what a buyer pays"],
         "c": 2,
         "why": "Worthiness &ldquo;consisteth in a particular power, or ability&rdquo; "
                "for what the man is said to be worthy of, which Hobbes calls fitness. "
                "Merit &ldquo;praesupposeth a right, and that the thing deserved is due "
                "by promise&rdquo;. A man can be worthy and not merit, as he says."},
    ],
    "mistakes": [
        ("Treating honour as a verdict on a man's goodness",
         "Hobbes says honour &ldquo;consisteth onely in the opinion of Power&rdquo;, and "
         "whether an action is just or unjust does not alter it. The piracy and the "
         "adulteries he lists were honoured. He is describing what men honour and why; "
         "the chapter does not say that they are right to."),
        ("Merging dignity with worth",
         "Worth is what buyers would give, which differs from buyer to buyer. Dignity "
         "is one figure set by the commonwealth and it can sit anywhere against the "
         "prices. In the titles preset the orator's dignity of 10 is below all three "
         "buyers' prices, while the general's 40 is above all three."),
        ("Reading worthiness as a high price",
         "Worthiness is fitness for a particular charge. A man may be worthy of an "
         "office and priced low by every buyer, or priced high and unfit for it. "
         "Hobbes takes care to say that it differs from worth and from merit."),
    ],
    "standard": (
        "Finish when you can set a dignity beside a buyer's price and say which is "
        "higher.",
        "Given each man's price for several buyers and the dignity the commonwealth sets, "
        "state for each man whether it is above, equal to or below each price, and name "
        "the men whose dignity equals no buyer's price."
    ),
    "note": (
        "The lab compares two numbers. Hobbes's dignity is set by a sovereign's will "
        "and shown by offices and titles, and the figures here are invented to show "
        "what the comparison looks like. The lab cannot say what a title is worth to the "
        "man who bears it, whether the Persian king's robe honoured or mocked him, "
        "or what a man deserves."
    ),
}


# ---------------------------------------------------------------- 03
# Leviathan ch. 11, 1651 p. 48; PDF p. 166 of the operator's copy.
RESTLESS_DESIRE = {
    "slug": "a-restless-desire-of-power",
    "title": "The Difference of Manners",
    "module": "Chapter 11 · Of the difference of Manners",
    "one_line": "Hobbes says every man wants power after power, not always out of greed, but because he cannot be sure of what he has without more.",
    "summary": (
        "Chapter 11 sets out what Hobbes means by manners, the qualities that concern "
        "men living together in peace, and finds at the root of them a restless "
        "desire of power after power. Its cause, he says, is not always that men cannot be "
        "content with a moderate power but that they cannot assure what they have. Play "
        "that reasoning as a table for two neighbours who may hold or add to their means "
        "and see what the equilibria are."
    ),
    "key": [
        "manners: qualities for living in peace",
        "felicity: a continual progress of desire",
        "power after power, ceasing only in death",
        "the cause: no assurance without more",
        "competition: war; ease and fear: obedience",
    ],
    "key_label": "The difference of manners in five lines",
    "concepts_intro": (
        "Chapter 11 is long and loosely arranged. Three of its ideas carry the rest."
    ),
    "concepts": [
        ("Felicity as progress",
         "Hobbes denies that there is any &ldquo;Finis ultimus&rdquo; or &ldquo;Summum "
         "Bonum&rdquo;, as the old moral philosophers had it. Happiness is a continual "
         "progress of desire from one object to another, the getting of the first being "
         "only the way to the next."),
        ("Power after power",
         "So he puts for a general inclination of all mankind a perpetual and restless "
         "desire of power after power that ceases only in death. The cause is not always that a "
         "man hopes for a greater delight, or cannot be content with moderate power, but "
         "that he cannot assure the power he has without acquiring more."),
        ("Manners that follow",
         "Competition for riches, honour or command inclines to contention and war. "
         "Desire of ease and fear of death incline to obey a common power, and so do the "
         "desire of knowledge and the arts of peace. Ignorance of causes makes men "
         "credulous and reliant on others."),
    ],
    "read_title": "The passage first, then the chapter line by line",
    "read_intro": (
        "The passage is the claim the whole chapter turns on. The lesson then goes "
        "through what Hobbes builds on it."
    ),
    "body": [
        ("p", "<strong>Chapter 11.</strong> &ldquo;So that in the first place, I put for "
              "a generall inclination of all mankind, a perpetuall and restlesse desire "
              "of Power after power, that ceaseth onely in Death. And the cause of this, "
              "is not alwayes that a man hopes for a more intensive delight, than he has "
              "already attained to; or that he cannot be content with a moderate power: "
              "but because he cannot assure the power and means to live well, which he "
              "hath present, without the acquisition of more.&rdquo;"),
        ("p", "You have likely met this feeling in miniature: a savings account you "
              "think is large enough, until you imagine something going wrong. Hobbes "
              "starts a step earlier. By manners he means &ldquo;those qualities of "
              "man-kind, that concern their living together in Peace, and Unity&rdquo;, "
              "not how to salute a neighbour or pick one's teeth before company, and "
              "he begins with what a person is trying to get out of life. There is "
              "none of the repose the old philosophers promised. &ldquo;Felicity is a "
              "continuall progresse of the desire, from one object to another; the "
              "attaining of the former, being still but the way to the later.&rdquo; "
              "And a man whose desires have ended is as little alive as one whose "
              "&ldquo;Senses and Imaginations are at a stand&rdquo;."),
        ("p", "From that he draws the passage above, and it repays a slow reading. "
              "The claim is about every man, in general. The desire is for power "
              "after power, and it ends only in death. And then comes the clause that "
              "most readers pass over. Hobbes has been taken to say that men are "
              "greedy, and here he says it is not necessarily so. A man may be content "
              "with a moderate power and still seek more, because power is only a "
              "means, and he &ldquo;cannot assure the power and means to live well, which "
              "he hath present, without the acquisition of more&rdquo;. He gives the "
              "example of kings: &ldquo;Kings, whose power is greatest, turn their "
              "endeavours to the assuring it at home by Lawes, or abroad by Wars&rdquo;, "
              "and when that is done a new desire for fame, ease or admiration "
              "succeeds it."),
        ("p", "The lab turns that clause into a table for two neighbours. Each may "
              "hold, keeping to what he has, or add, arming or extending his reach. "
              "Payoffs are the lesson's own: higher is better, the first number is "
              "the row neighbour's. The greedy preset is the first kind of man. If both "
              "hold each gets 3, if both add each gets 1, and a neighbour who adds "
              "against one who holds gets 4 while the holder gets 0. Adding is the best "
              "reply to anything, so the only equilibrium is both adding, and it leaves "
              "each worse off than both holding."),
        ("p", "The moderate preset is Hobbes's clause. Here each neighbour prefers "
              "to hold if the other holds (3 against 2), and prefers to add only "
              "if the other adds (1 against 0), because a holder against an adder "
              "loses what he has. That is a man who could be content with a moderate "
              "power and cannot assure it. The table then has two equilibria: both "
              "hold, and both add. Fear alone, with no greed, is enough to make "
              "the second one stable. Which of the two a pair reaches the table "
              "does not say."),
        ("p", "The one-greedy preset pairs the two kinds: the row neighbour is moderate, "
              "the column neighbour greedy, one who prefers to add whatever the "
              "row does. Given that, the row neighbour does better "
              "to add, and the only equilibrium is both adding. One greedy neighbour "
              "is enough to drag the moderate man with him. This is the "
              "reasoning Chapter 13 will turn into the three causes of quarrel, "
              "and the tables here are not that argument yet."),
        ("p", "The rest of the chapter reads the same disposition through "
              "particular desires. &ldquo;Competition of Riches, Honour, Command, or other "
              "power enclineth to Contention, Enmity, and War&rdquo;, since one competitor "
              "gets his end by killing, subduing or repelling the other. But &ldquo;Desire "
              "of Ease, and sensuall Delight, disposeth men to obey a common Power&rdquo;, "
              "and &ldquo;Fear of Death, and Wounds, disposeth to the same&rdquo;. So "
              "the same restless creature is drawn both ways, and the manners of a "
              "society depend on which desires prevail. Needy and hardy men, he adds, "
              "and all who are ambitious of military command, are inclined to stir up "
              "trouble, &ldquo;for there is no honour Military but "
              "by warre; nor any such hope to mend an ill game, as by causing a new "
              "shuffle&rdquo;."),
        ("p", "Hobbes has an eye for the small cruelties of obligation. &ldquo;For "
              "benefits oblige; and obligation is thraldome; and unrequitable obligation, "
              "perpetuall thraldome; which is to ones equall, hatefull.&rdquo; Someone "
              "who has been helped more than he can repay may come to hate the helper. "
              "Benefits from a superior do not have this effect, since nothing is "
              "depressed by them, and a grateful acceptance is itself an honour paid. "
              "It is one of the lightest touches in a heavy chapter, and he means it "
              "seriously."),
        ("p", "The second half of the chapter is about ignorance. &ldquo;Want of "
              "Science, that is, Ignorance of causes, disposeth, or rather constraineth a "
              "man to rely on the advise, and authority of others.&rdquo; &ldquo;Ignorance "
              "of naturall causes disposeth a man to Credulity&rdquo;, and since men like "
              "to be listened to, it leads them to lie as well: &ldquo;Ignorance it selfe "
              "without Malice, is able to make a man both to believe lyes, and tell "
              "them&rdquo;. The disputes over right and wrong, he says, go on by pen and "
              "sword because they cross men's ambition, profit or lust, where the "
              "doctrine of lines and figures does not. If the angles of a triangle "
              "conflicted with a ruler's interest, he writes, books of geometry "
              "would be burned."),
        ("p", "The chapter ends, as the next begins, on the cause of causes, and the "
              "next lesson, <em>The Natural Seeds of Religion</em>, picks it "
              "up: what an anxious creature who cannot see causes does with the "
              "future."),
    ],
    "lab": ("choicekit", {
        "mode": "game",
        "view": "best",
        "preset": "greedy",
        "presets": [
            {"id": "greedy", "label": "Two greedy neighbours: hold or add",
             "rows": ["Hold", "Add"], "cols": ["Hold", "Add"],
             "payoffs": [[[3, 3], [0, 4]], [[4, 0], [1, 1]]],
             "expect": {"gaPure": "(Add, Add)", "gaDom": "Add dominates for both", "gaPareto": "(Add, Add) is dominated by (Hold, Hold)"}},
            {"id": "moderate", "label": "Two moderate neighbours who fear the other's gain",
             "rows": ["Hold", "Add"], "cols": ["Hold", "Add"],
             "payoffs": [[[3, 3], [0, 2]], [[2, 0], [1, 1]]],
             "expect": {"gaPure": "(Hold, Hold); (Add, Add)", "gaMixed": "row Hold: 1/2, col Hold: 1/2", "gaDom": "none"}},
            {"id": "one-greedy", "label": "A moderate row neighbour, a greedy column neighbour",
             "rows": ["Hold", "Add"], "cols": ["Hold", "Add"],
             "payoffs": [[[3, 2], [0, 4]], [[2, 1], [1, 3]]],
             "expect": {"gaPure": "(Add, Add)", "gaDom": "Add dominates for column", "gaPareto": "every equilibrium is efficient"}},
        ],
        "panel_title": "Hold or add: two neighbours",
        "panel_intro": (
            "Each cell holds the row neighbour's payoff first. An asterisk marks the "
            "player for whom that cell is a best reply. Change a payoff and watch the "
            "marks move; the first tile lists the cells where both marks fall."
        ),
    }),
    "steps_title": "Reading the reasoning as a table",
    "steps_intro": "Four steps, from Hobbes's sentence to a payoff table.",
    "steps": [
        ("State what each neighbour can do",
         "Here: hold to what he has, or add to it. The choices are the lesson's "
         "stand-ins for Hobbes's &ldquo;acquisition of more&rdquo;."),
        ("Write what each outcome is worth to each",
         "Put the row neighbour's payoff first. This is where a claim about "
         "temperament goes: a greedy man scores adding highest whatever the other does; "
         "a moderate one scores it highest only against an adder."),
        ("Mark each neighbour's best reply to each choice of the other",
         "Fix one choice of the other neighbour and take the larger payoff. A cell "
         "marked for both is an equilibrium."),
        ("Ask what the equilibria show",
         "Whether adding is best against everything, whether the equilibria are good "
         "for both, and whether fear alone, with no greed, can keep a pair in them."),
    ],
    "worked": {
        "title": "Why moderate neighbours can still arm",
        "intro": [
            "Take the moderate preset. Payoffs are row first. Holding against holding "
            "pays 3 each; adding against holding pays the adder 2 and the holder 0; "
            "adding against adding pays 1 each.",
        ],
        "lines": [
            "column holds:  row Hold 3, row Add 2  ->  Hold",
            "column adds:  row Hold 0, row Add 1  ->  Add",
            "row holds:  column Hold 3, column Add 2  ->  Hold",
            "row adds:  column Hold 0, column Add 1  ->  Add",
            "marked by both:  (Hold, Hold) and (Add, Add)",
        ],
        "after": [
            "Both neighbours prefer holding to adding if the other holds, so neither is "
            "greedy. Yet (Add, Add) is also an equilibrium, because each would lose what "
            "he has by holding against an adder. That is the clause Hobbes adds to the "
            "usual account of ambition.",
        ],
    },
    "quiz_title": "Power after power",
    "quiz": [
        {"q": "According to the passage, why does a man who could be content with a "
              "moderate power still seek more?",
         "a": ["Because he hopes for a more intensive delight",
               "Because he has no other way to be admired",
               "Because he cannot assure the power he has without acquiring more",
               "Because only death can satisfy him"],
         "c": 2,
         "why": "Hobbes says the cause &ldquo;is not alwayes that a man hopes for a more "
                "intensive delight&rdquo;, nor that he cannot be content with a moderate "
                "power, &ldquo;but because he cannot assure the power and means to live "
                "well, which he hath present, without the acquisition of more&rdquo;. "
                "Death is where the desire ends, not what it seeks."},
        {"q": "In the greedy preset, what is the equilibrium?",
         "a": ["Both Hold", "Both Add", "Row Add, column Hold", "There is none"],
         "c": 1,
         "why": "Adding pays more than holding against either choice of the other "
                "(4 against 3, and 1 against 0), so each adds, and (Add, Add) is the "
                "only cell marked for both. Both would do better at (Hold, Hold), which "
                "pays 3 each."},
        {"q": "What does the moderate preset show that the greedy preset does not?",
         "a": ["That moderate men never arm",
               "That fear alone, without greed, can keep both neighbours adding",
               "That arming always pays the most",
               "That holding is the only equilibrium"],
         "c": 1,
         "why": "In the moderate preset (Hold, Hold) is an equilibrium and so is "
                "(Add, Add): neither neighbour wants more, and each adds only to avoid "
                "being the one who holds. Moderate men can arm, but they need not, "
                "since the other equilibrium is also there."},
        {"q": "Which of these does Hobbes name as inclining men to obey a common power?",
         "a": ["Competition for honour",
               "Ambition of military command",
               "Fear of death and wounds",
               "A restless desire of power after power"],
         "c": 2,
         "why": "&ldquo;Fear of Death, and Wounds, disposeth to the same&rdquo;, with "
                "desire of ease and sensual delight. Competition and military ambition "
                "incline to contention and war, and the restless desire is the general "
                "inclination from which the manners follow."},
    ],
    "mistakes": [
        ("Reading Hobbes as saying men are greedy",
         "The passage says the cause is &ldquo;not alwayes&rdquo; a hope of more "
         "delight and not that a man &ldquo;cannot be content with a moderate "
         "power&rdquo;. In the moderate preset neither neighbour wants more than he has. "
         "What Hobbes adds is that holding is not safe against someone who adds."),
        ("Taking the tables as Hobbes's own argument for war",
         "They show one clause of Chapter 11 as a payoff table with invented numbers. "
         "Chapter 13 gives the three causes of quarrel, and the Philosophy lesson "
         "<em>Hobbes and the State of Nature</em> works its games. These "
         "tables do not stand in for either."),
        ("Thinking the equilibrium is what the neighbours want",
         "In the greedy and moderate presets (Add, Add) pays 1 each and (Hold, Hold) "
         "pays 3 each. An equilibrium is a cell neither would leave alone, not one "
         "they would choose together."),
    ],
    "standard": (
        "Finish when you can say what each equilibrium of a hold-or-add table is.",
        "Given a two-by-two table of payoffs for two neighbours, mark each one's best "
        "replies, name the equilibria, and say whether a moderate temperament can end "
        "in the adding equilibrium."
    ),
    "note": (
        "The payoffs are invented to give shape to one sentence of Chapter 11. The "
        "tables compare cells, and cannot say whether men are as restless as Hobbes "
        "says, whether power is what they want, or whether a neighbour's adding really "
        "costs a holder all he has. Those are claims about men, and the book argues them."
    ),
}

# ---------------------------------------------------------------- 04
# Leviathan ch. 12, 1651 pp. 54-55; PDF pp. 174-175 of the operator's copy.
SEEDS_OF_RELIGION = {
    "slug": "the-seeds-of-religion",
    "title": "The Natural Seeds of Religion",
    "module": "Chapter 12 · Of Religion",
    "one_line": "Hobbes derives religion from four seeds in human nature: belief in ghosts, ignorance of second causes, devotion toward what men fear, and taking chance events for prognostics.",
    "summary": (
        "Chapter 12 asks where religion comes from and answers from the nature of the "
        "creature that has it: a man who looks ahead, cannot see the causes of his good "
        "and evil fortune, and fears what he cannot see. The fourth seed is mistaking "
        "chance events for signs. Update a prudent man's credence in a sign on one and "
        "two observations and on a base rate that makes the sign worthless."
    ),
    "key": [
        "religion belongs to man alone",
        "anxiety for the future, in the dark",
        "four seeds: ghosts, second causes, fear, signs",
        "a prognostic taken from one or two cases",
        "posterior = prior × likelihood, renormalised",
    ],
    "key_label": "The seeds of religion in five lines",
    "concepts_intro": (
        "Chapter 12 is Hobbes's natural history of religion, written before he says "
        "anything about revealed religion. It comes in three moves."
    ),
    "concepts": [
        ("Anxiety about causes",
         "Man alone enquires into causes, and observes how one event produces "
         "another. He is assured that everything has a cause, and cannot see the causes "
         "of his good and evil fortune, so he lives in perpetual solicitude of the time "
         "to come, like Prometheus bound to the hill with an eagle at his liver."),
        ("Invisible powers",
         "That fear, always accompanying mankind in the ignorance of causes, must have "
         "an object, and when there is nothing to be seen it falls on some power or agent "
         "invisible. The first God of the Gentiles, Hobbes says, was made by human fear; "
         "the one eternal God can be reached more easily by following causes to a first."),
        ("The four seeds",
         "Opinion of ghosts, ignorance of second causes, devotion toward what men "
         "fear, and taking things casual for prognostics make up the natural seed of "
         "religion. The fourth is a mistake about evidence: from one or two encounters "
         "men conclude the like encounter ever after."),
    ],
    "read_title": "The passage first, then the chapter line by line",
    "read_intro": (
        "The passage gives the four seeds together. The line-by-line reading takes the "
        "fourth, the one this lesson works as a sum, in Hobbes's own words."
    ),
    "body": [
        ("p", "<strong>Chapter 12.</strong> &ldquo;And in these foure things, Opinion of "
              "Ghosts, Ignorance of second causes, Devotion towards what men fear, and "
              "Taking of things Casuall for Prognostiques, consisteth the Naturall seed "
              "of Religion&rdquo;."),
        ("p", "Hobbes wrote Leviathan in a Europe that had spent more than a century "
              "killing one another over religion, and he begins Chapter 12 by "
              "asking where it comes from, as he might ask where a river does. "
              "&ldquo;Seeing there are no signes, nor fruit of Religion, but in Man "
              "onely&rdquo;, there must be something peculiar to man in which its seed "
              "consists. He finds it in three things: that man is curious about causes; "
              "that, seeing anything begin, he thinks it had a cause that fixed "
              "the moment; and that, unlike beasts, he remembers how one event "
              "produced another and so looks ahead."),
        ("p", "The look ahead is the trouble. &ldquo;it is impossible for a man, who "
              "continually endeavoureth to secure himselfe against the evill he feares, "
              "and procure the good he desireth, not to be in a perpetuall solicitude of "
              "the time to come&rdquo;. He compares such a man to Prometheus, whose name "
              "Hobbes glosses as the prudent man, chained to the Caucasus with an eagle "
              "eating his liver each day. Anyone who has lain awake at night "
              "turning over what might go wrong knows the creature. And this fear, he "
              "says, &ldquo;must needs have for object something&rdquo;. When nothing "
              "is to be seen there is nothing to blame for good or bad luck &ldquo;but "
              "some Power, or Agent Invisible&rdquo;, and so, perhaps, the old poets said "
              "&ldquo;the Gods were at first created by humane Feare&rdquo;. Of the "
              "many gods of the Gentiles, he adds, that is very true; the one eternal "
              "God is reached differently, by following causes back to &ldquo;one First "
              "Mover&rdquo;."),
        ("p", "He then goes through the seeds in turn: the thought that invisible "
              "agents are spirits, thin bodies like the dream-image or the face in "
              "the looking-glass; the ignorance of second causes, which makes "
              "men attribute fortune to a stander by, a lucky place or words spoken, and "
              "leaves them guessing at causes by what they have seen go before like "
              "effects. So the Athenians, for their war at Lepanto, asked for &ldquo;another "
              "Phormio&rdquo;, and the Pompeians for another Scipio; they &ldquo;expect the "
              "like things to come; and hope for good or evill luck, superstitiously, from "
              "things that have no part at all in the causing of it&rdquo;. Third comes the "
              "worship men give, which can be no more than what they would show to men, "
              "gifts, petitions, thanks and submission. The fourth is the one the lab "
              "takes up. Where, he asks, do men think these powers foretell the future?"),
        ("p", "<strong>Chapter 12.</strong> &ldquo;Lastly, concerning how these "
              "Invisible Powers declare to men the things which shall hereafter come to "
              "passe&rdquo;, men are at a stand &ldquo;save that using to conjecture of "
              "the time to come, by the time past, they are very apt, not onely to take "
              "casuall things, after one or two encounters, for Prognostiques of the like "
              "encounter ever after, but also to believe the like Prognostiques from "
              "other men, of whom they have once conceived a good opinion.&rdquo;"),
        ("p", "That is an observation about evidence, and a sharp one. Men use the "
              "past to guess the future, which is just what he called prudence in "
              "Chapter 3, and they do it from too few cases."),
        ("p", "The lab asks how far one or two cases should move a prudent man. Let "
              "the sign be something you notice before an event, a crow on the roof "
              "before news. Two hypotheses: the sign foretells the event, or it is "
              "unconnected. Before any case the man thinks it likely enough to foretell "
              "that he gives it 1 in 10. If it foretells, the event follows nine times in "
              "ten. If it does not, the event follows half the time anyway. These are "
              "the lesson's own numbers, not Hobbes's. The one-encounter preset sees "
              "the event follow once. The man's credence in the sign goes from 1/10 to "
              "1/6, and the Bayes factor is 9/5. The two-encounters preset sees it follow "
              "twice, and the credence reaches 9/34, a little over a quarter, with a "
              "factor of 81/25. Two coincidences, in other words, make the sign a "
              "better bet than before and still far from the &ldquo;ever after&rdquo; "
              "Hobbes complains of."),
        ("p", "The third preset makes the same point from the other side. Let the event "
              "be one that follows nine times in ten whether or not there is a sign. "
              "The likely-anyway preset then has a factor of 1: seeing the event follow "
              "tells you nothing, and the credence stays where it was. That is the "
              "kind of case in which, Hobbes says, men take &ldquo;casuall things&rdquo; "
              "for prognostics. The sign was there before the event, and so was everything "
              "else."),
        ("p", "Two things must be kept apart. The first is what Hobbes says, a "
              "claim about men: they leap from one or two cases to always. The second "
              "is what the lab computes, a rule of evidence that Hobbes did not "
              "have, since Bayes's theorem was published after his death. The sum shows "
              "what one and two cases ought to do on stated numbers. It does not "
              "show that men in fact do otherwise, nor that religion is nothing but "
              "this mistake. Hobbes says the seed has other roots, and when he comes to "
              "the founders of religions in the next lesson he is careful to treat "
              "revealed religion separately."),
        ("p", "The next lesson, <em>Religion and Policy</em>, turns from where "
              "religion comes from to what men have done with it: the two sorts of "
              "men who cultivated the seeds, and what makes a religion lose its hold."),
    ],
    "lab": ("choicekit", {
        "mode": "update",
        "preset": "one-encounter",
        "presets": [
            {"id": "one-encounter", "label": "A sign seen before the event, once",
             "hyps": ["foretells", "unconnected"], "prior": ["1/10", "9/10"],
             "outcomes": ["follows", "fails"], "lik": [["9/10", "1/10"], ["1/2", "1/2"]],
             "data": ["follows"], "payoffs": None, "expect": {"upPost": "1/6", "upBF": "9/5", "upConf": "Confirms", "upPred": "17/30"}},
            {"id": "two-encounters", "label": "The same sign, twice",
             "hyps": ["foretells", "unconnected"], "prior": ["1/10", "9/10"],
             "outcomes": ["follows", "fails"], "lik": [["9/10", "1/10"], ["1/2", "1/2"]],
             "data": ["follows", "follows"], "payoffs": None, "expect": {"upPost": "9/34", "upBF": "81/25", "upConf": "Confirms", "upPred": "103/170"}},
            {"id": "likely-anyway", "label": "An event that follows nine times in ten anyway",
             "hyps": ["foretells", "unconnected"], "prior": ["1/10", "9/10"],
             "outcomes": ["follows", "fails"], "lik": [["9/10", "1/10"], ["9/10", "1/10"]],
             "data": ["follows"], "payoffs": None, "expect": {"upPost": "1/10", "upBF": "1", "upConf": "Neutral", "upPred": "9/10"}},
        ],
        "panel_title": "What one or two encounters should change",
        "panel_intro": (
            "Each row of the likelihoods is one hypothesis and must sum to 1. Type "
            "follows follows follows and watch the credence climb; then choose the "
            "likely-anyway preset and see why it does not."
        ),
    }),
    "steps_title": "Weighing a sign",
    "steps_intro": "Five steps, the same for any sign and any number of cases.",
    "steps": [
        ("State the two hypotheses and the credence before any case",
         "The sign foretells the event, or it is unconnected with it. The first credence "
         "is yours before the first encounter."),
        ("Say how likely the event is on each hypothesis",
         "If the sign foretells, the event follows at some rate. If it does not, "
         "the event still follows at its ordinary rate. This second figure is the one "
         "casual prognostics forget."),
        ("Multiply and renormalise for each encounter",
         "Multiply each credence by the likelihood of what you saw, and divide each "
         "product by their sum. Use the result as the credence for the next case."),
        ("Read the Bayes factor",
         "The ratio of the two likelihoods is how much a case moves the odds. If "
         "it is 1, the case tells you nothing."),
        ("Compare the credence with &ldquo;ever after&rdquo;",
         "A credence of 1 would be certainty. How far one or two cases bring you "
         "from your starting point is what the lab computes."),
    ],
    "worked": {
        "title": "One encounter with a sign",
        "intro": [
            "Take the first preset. The credence in the sign is 1/10 to begin. If it "
            "foretells, the event follows with chance 9/10; if it is unconnected, with "
            "chance 1/2. The event follows.",
        ],
        "lines": [
            "foretells:  1/10 · 9/10 = 9/100",
            "unconnected:  9/10 · 1/2 = 45/100",
            "total:  9/100 + 45/100 = 54/100",
            "credence in the sign:  9/54 = 1/6",
            "Bayes factor:  (9/10) / (1/2) = 9/5",
        ],
        "after": [
            "One encounter nearly doubles the odds, from 1 to 9 to 1 to 5, and the man "
            "still thinks the sign more likely idle than real. In the likely-anyway "
            "preset both likelihoods are 9/10, the factor is 1, and the credence "
            "stays at 1/10.",
        ],
    },
    "quiz_title": "Casual things taken for signs",
    "quiz": [
        {"q": "Which four things does Hobbes say make up the natural seed of religion?",
         "a": ["Fear of death, ambition, love of ease and credulity",
               "Opinion of ghosts, ignorance of second causes, devotion toward what "
               "men fear, and taking casual things for prognostics",
               "Miracles, prophecy, revelation and Scripture",
               "Anxiety, desire of knowledge, curiosity and the love of praise"],
         "c": 1,
         "why": "The passage names them: &ldquo;Opinion of Ghosts, Ignorance of second "
                "causes, Devotion towards what men fear, and Taking of things Casuall "
                "for Prognostiques&rdquo;. The other lists mix in ideas from Chapter 11, "
                "or from later chapters on revealed religion."},
        {"q": "In the one-encounter preset the sign has prior credence 1/10, the event "
              "follows at 9/10 if the sign foretells and at 1/2 if not, and the event "
              "follows. What is the credence in the sign afterwards?",
         "a": ["9/10", "1/2", "1/6", "9/34"],
         "c": 2,
         "why": "`(1/10·9/10) / (1/10·9/10 + 9/10·1/2) = 9/54 = 1/6`. Nine tenths is "
                "the likelihood, not the credence. One half is the likelihood on the "
                "other hypothesis, and 9/34 is the credence after two encounters."},
        {"q": "Why does the likely-anyway preset leave the credence at 1/10?",
         "a": ["Because the event happened only once",
               "Because the event is as likely without the sign as with it, so the "
               "Bayes factor is 1",
               "Because the prior was too low to move",
               "Because the sign cannot foretell a likely event"],
         "c": 1,
         "why": "Both hypotheses give the event the same chance, 9/10, so seeing it "
                "tells nothing and the factor is 1. The prior was 1/10 and could "
                "have moved, as it does in the first two presets, and a sign could "
                "in principle foretell a likely event; seeing the event is just not "
                "evidence about it here."},
    ],
    "mistakes": [
        ("Taking Hobbes for a Bayesian",
         "The sum is the lesson's, not his. He says men are &ldquo;very apt&rdquo; to take "
         "casual things for prognostics after one or two encounters. The lab shows "
         "what one or two encounters should do on stated numbers; it does not say how "
         "much men do in fact move, which is a question about men."),
        ("Counting the sign's hits and forgetting how often the event comes anyway",
         "A sign seen before nine events in ten looks impressive until you ask how "
         "often the event comes without it. In the likely-anyway preset the sign "
         "was present before an event that comes nine times in ten regardless, and "
         "the credence does not move at all."),
        ("Thinking that two coincidences settle it",
         "Even in the favourable second preset two encounters raise the credence in the "
         "sign only from 1/10 to 9/34. Hobbes's complaint is the jump to &ldquo;ever "
         "after&rdquo;, and the lab shows how small the warranted step is."),
    ],
    "standard": (
        "Finish when you can update a credence on one or two cases and read the factor.",
        "Given a prior, the chance of the event if the sign foretells and if it does "
        "not, and a number of observed cases, compute the credence in the sign and "
        "its Bayes factor, and say when the sign is no evidence."
    ),
    "note": (
        "The prior, the 9/10 and the 1/2 are invented, and the lab's rule of evidence "
        "is later than Hobbes. The sum shows how far a sign's coincidences should carry "
        "a man on stated numbers. It cannot say that religion arises from this error, "
        "or that it does not, and Hobbes names three other seeds."
    ),
}

# ---------------------------------------------------------------- 05
# Leviathan ch. 12, 1651 p. 58; PDF p. 180 of the operator's copy.
RELIGION_AND_POLICY = {
    "slug": "religion-and-policy",
    "title": "Religion and Policy",
    "module": "Chapter 12 · Of Religion",
    "one_line": "Hobbes says the founders of religions used the seeds to make men obedient, and that a religion loses its hold when its teachers lose their reputation for wisdom, sincerity or love.",
    "summary": (
        "The second half of Chapter 12 turns from where religion comes from to what men "
        "have done with it. Founders of commonwealths among the Gentiles made religion "
        "a part of policy; God himself planted religion among the Jews. Religion "
        "changes when its teachers are suspected of ignorance, insincerity or private "
        "ends, or cannot show miracles. Set the first of these out as an argument "
        "and see which premise does the work."
    ),
    "key": [
        "two cultivators: men, and God",
        "religion of the Gentiles a part of policy",
        "contradictions discredit the teacher",
        "so do scandal, private ends, no miracles",
        "c -> g, g -> d, so c -> d",
    ],
    "key_label": "Religion and policy in five lines",
    "concepts_intro": (
        "Three ideas carry the second half of Chapter 12: who cultivated the seeds, "
        "what the cultivation was for, and what ruins it."
    ),
    "concepts": [
        ("Two sorts of cultivators",
         "The seeds have been tended by two sorts of men: those who ordered them by "
         "their own invention, and those who did it by God's command. Both aimed to make "
         "the men who relied on them more apt to obedience, laws, peace, charity and "
         "civil society. The first sort's religion is a part of human politics; the "
         "second's is divine politics."),
        ("Religion as policy",
         "The first founders of commonwealths among the Gentiles took care that "
         "their precepts seemed to come from a god, that the things forbidden by law "
         "seemed displeasing to the gods, and that ceremonies seemed to appease "
         "them. Hence people blamed neglected ceremonies for misfortune, not "
         "their rulers."),
        ("Why a religion changes",
         "A religion rests on the faith a multitude has in one person, whom they take to "
         "be wise, sincere, loving and called by God. When the wisdom, sincerity "
         "or love of those who govern it is suspected, or no token of divine calling "
         "can be shown, the religion is suspected too."),
    ],
    "read_title": "The passage first, then the chapter line by line",
    "read_intro": (
        "The passage is the first of Hobbes's causes of change in religion. The "
        "lesson then goes back to the founders, to see what the argument is set against."
    ),
    "body": [
        ("p", "<strong>Chapter 12.</strong> &ldquo;That which taketh away the reputation of "
              "Wisedome, in him that formeth a Religion, or addeth to it when it is "
              "allready formed, is the enjoyning of a beliefe of contradictories: For "
              "both parts of a contradiction cannot possibly be true: and therefore to "
              "enjoyne the beliefe of them, is an argument of ignorance; which detects "
              "the Author in that; and discredits him in all things else he shall "
              "propound as from relevation supernaturall; which revelation a man may "
              "indeed have of many things above, but of nothing against naturall "
              "reason.&rdquo;"),
        ("p", "That is the end of a story, so begin with the beginning. Hobbes says "
              "the seeds of religion &ldquo;have received culture from two sorts of "
              "men&rdquo;. &ldquo;One sort have been they, that have nourished, and "
              "ordered them, according to their own invention. The other, have done it, "
              "by Gods commandement, and direction: but both sorts have done it, with a "
              "purpose to make those men that relyed on them, the more apt to Obedience, "
              "Lawes, Peace, Charity, and civill Society.&rdquo; The first sort, he "
              "adds, includes &ldquo;all the founders of Common-wealths, and the "
              "Law-givers of the Gentiles&rdquo;; the second, Abraham, Moses and Christ. "
              "He says plainly that &ldquo;the Religion of the former sort, is a part of "
              "humane Politiques&rdquo;, and the later is &ldquo;Divine Politiques&rdquo;."),
        ("p", "Then he spends a good many pages on the Gentiles: the gods of Chaos, "
              "the winds and the planets, the onion and the leek, the demons of the woods, "
              "the Muses who were men's own wit and the Furies who were their own rage. "
              "That list is Hobbes enjoying himself, and it is worth reading for "
              "the sheer range of what men have made into gods. Its point comes "
              "afterwards. The founders of such religions, &ldquo;whose ends were only "
              "to keep the people in obedience, and peace&rdquo;, took three cares. They "
              "made it believed that their precepts came from a god or spirit. "
              "&ldquo;So Numa Pompilius pretended to receive the Ceremonies he instituted "
              "amongst the Romans&rdquo; from the nymph Egeria, the first king of Peru "
              "&ldquo;pretended himselfe and his wife to be the children of the "
              "Sunne&rdquo;, and &ldquo;Mahomet, to set up his new Religion, pretended to "
              "have conferences with the Holy Ghost, in forme of a Dove&rdquo;. They made "
              "it believed that what the laws forbade displeased the gods. And they "
              "prescribed ceremonies by which the gods' anger might be appeased, so "
              "that misfortune could be put down to neglected worship."),
        ("p", "&ldquo;And thus you see how the Religion of the Gentiles was a part of "
              "their Policy.&rdquo; The Romans, he notes, tolerated any religion in the "
              "city &ldquo;unlesse it had somthing in it, that could not consist with "
              "their Civill Government&rdquo;, and he can find none forbidden &ldquo;but "
              "that of the Jewes&rdquo;, who thought it unlawful to acknowledge a mortal "
              "king. Where God himself planted religion, by contrast, he made a peculiar "
              "kingdom: &ldquo;the Policy, and lawes Civill, are a part of "
              "Religion&rdquo;, and the distinction of temporal and spiritual domination "
              "has no place. Hobbes says he will speak of that later, and in Part III he "
              "does."),
        ("p", "It was a delicate subject in 1651. Hobbes "
              "is not saying that Christianity was invented by a lawgiver; he puts "
              "Abraham, Moses and Christ in the second class and says their religion "
              "contains divine precepts. But the account of the first class, with "
              "its Numa and its Mahomet, struck contemporaries as an account of "
              "religion in general, and John Bramhall, Bishop of Derry, among others, "
              "attacked the book as undermining it. A reader today can fairly ask "
              "where the line falls, and Hobbes answers it with his tests of a true "
              "calling, the subject of Part III."),
        ("p", "Now the passage. Hobbes asks what makes a religion fall, and his answer "
              "starts from the fact that all formed religion &ldquo;is founded at first, "
              "upon the faith which a multitude hath in some one person&rdquo;, believed "
              "wise, labouring for their happiness, and holy. When those who govern "
              "religion have their wisdom, sincerity or love suspected, or can show "
              "no probable token of divine revelation, the religion is suspected too, "
              "and, &ldquo;without the feare of the Civill Sword&rdquo;, rejected. So "
              "there are four causes of change. Wisdom is lost by &ldquo;the "
              "enjoyning of a beliefe of contradictories&rdquo;, which is the passage. "
              "Sincerity is lost by &ldquo;the doing, or saying of such things, as "
              "appeare to be signes, that what they require other men to believe, is not "
              "believed by themselves&rdquo;, Hobbes's scandals: injustice, cruelty, "
              "profaneness, avarice and luxury. Love is lost by &ldquo;the being "
              "detected of private ends&rdquo;. And the testimony of a divine calling "
              "&ldquo;can be no other, than the operation of Miracles; or true "
              "Prophecy, (which also is a Miracle;) or extraordinary Felicity&rdquo;."),
        ("p", "The first cause is an argument, and the lab sets it out. Let `c` stand for: the "
              "founder enjoins belief of contradictories; `g`: his ignorance is detected; "
              "`d`: he is discredited in all else he propounds as revelation. "
              "Hobbes's reasoning is: "
              "if `c`, then `g`; and if `g`, then `d`; so if `c`, then `d`. The chain "
              "preset has exactly those two premises and that conclusion, and the lab "
              "finds it valid: of the eight possible cases, none makes both premises "
              "true and the conclusion false. That is a hypothetical syllogism."),
        ("p", "Both links are needed. The second carries one detected error into "
              "&ldquo;all things else&rdquo;: drop it, leaving only `c -> g`, as the "
              "missing-link preset does, and the lab finds a case with the premise true "
              "and the conclusion false, a founder shown ignorant yet still believed "
              "on the rest. Drop the first instead and a counterexample opens too. "
              "The defender of a mystery attacks neither link. A Catholic or Anglican "
              "defender of the Trinity, say, grants the chain and denies `c`, because the "
              "doctrine is above reason and not against it. Hobbes's own sentence grants "
              "that line, &ldquo;of many things above, but of nothing against naturall "
              "reason&rdquo;, and the quarrel is over which side of it a doctrine lies."),
        ("p", "One more preset shows what the argument does not say. In the "
              "run-backwards preset the premises are the chain and the fact that "
              "the founder is discredited, and the conclusion is that he enjoined "
              "contradictories. The lab finds it invalid, with two cases to the "
              "contrary. Hobbes does not say discredit comes only that way; "
              "he lists three other causes."),
        ("p", "He ends the chapter with examples, and they are the kind of thing "
              "a prudent reader would check. Israel, with Moses absent forty days, "
              "made a golden calf: &ldquo;So that Miracles fayling, Faith also "
              "failed.&rdquo; Samuel's sons took bribes, and the people asked for a "
              "king: &ldquo;So that Justice fayling, Faith also fayled&rdquo;. And of "
              "the Church of Rome in England he says that &ldquo;the fayling of Vertue "
              "in the Pastors, maketh Faith faile in the People&rdquo;, and that "
              "bringing Aristotle into religion produced contradictions that brought "
              "the clergy into &ldquo;a reputation both of Ignorance, and of "
              "Fraudulent intention&rdquo;. That is a controversial thing to say, "
              "and it was meant to be."),
        ("p", "That closes Part I's account of manners and religion. The next "
              "course, <em>The Natural Condition and the Laws of Nature</em>, "
              "begins with Chapter 13 and the claim for which the whole of Part I has been "
              "preparing the ground: what men would be like with no common power over "
              "them."),
    ],
    "lab": ("argkit", {
        "mode": "validity",
        "preset": "chain",
        "show": "all",
        "presets": [
            {"id": "chain", "label": "c, then g; g, then d; so c, then d",
             "premises": ["c -> g", "g -> d"], "conclusion": "c -> d", "expect": {"vaVerdict": "Valid", "vaCounter": "0", "vaForm": "hypothetical syllogism"}},
            {"id": "missing-link", "label": "c, then g; so c, then d",
             "premises": ["c -> g"], "conclusion": "c -> d", "expect": {"vaVerdict": "Invalid", "vaCounter": "1"}},
            {"id": "run-backwards", "label": "c, then g; g, then d; d; so c",
             "premises": ["c -> g", "g -> d", "d"], "conclusion": "c", "expect": {"vaVerdict": "Invalid", "vaCounter": "2"}},
        ],
        "panel_title": "Does a contradiction discredit the teacher?",
        "panel_intro": (
            "Each row is a case: a true or false for each of c, g and d. A row is "
            "highlighted when every premise is true and the conclusion false. Choose "
            "missing-link first and find the one highlighted row, then choose "
            "run-backwards."
        ),
    }),
    "steps_title": "Setting out Hobbes's argument about a teacher",
    "steps_intro": "Four steps, the last of which is the one to argue over.",
    "steps": [
        ("Name the three claims",
         "One letter for each: a contradiction is enjoined, the ignorance is "
         "detected, the teacher is discredited in all else."),
        ("Write the premises as conditionals",
         "Hobbes's &ldquo;and therefore&rdquo; and &ldquo;which&rdquo; become "
         "<em>if</em> links in a chain. State each link on its own."),
        ("Run the lab",
         "A row where all premises are true and the conclusion false is a counterexample. "
         "No such row means the conclusion follows."),
        ("Ask which premise carries the weight",
         "Delete each in turn: each deletion opens a counterexample, so the argument "
         "needs both. Then ask what an opponent denies, a premise or the claim that "
         "`c` is true of his doctrine."),
    ],
    "worked": {
        "title": "Why the second link matters",
        "intro": [
            "Take the missing-link preset: the only premise is that if contradictories "
            "are enjoined, ignorance is detected. The conclusion is that if contradictories "
            "are enjoined, the teacher is discredited in all else.",
        ],
        "lines": [
            "c true, g true, d false:  c -> g is true",
            "same case:  c -> d is false",
            "so the premise is true and the conclusion false",
            "add  g -> d:  that case is ruled out",
        ],
        "after": [
            "The case is a teacher who has been shown ignorant and is still believed on "
            "everything else. The added premise, that detected ignorance discredits in "
            "all things, is exactly what rules it out. A defender of a mystery need not "
            "deny it, only that his doctrine is a contradiction.",
        ],
    },
    "quiz_title": "A teacher who contradicts himself",
    "quiz": [
        {"q": "According to Hobbes, which of these takes away a religion's founder's "
              "reputation for sincerity?",
         "a": ["Enjoining belief of contradictories",
               "The being detected of private ends",
               "Doing or saying what seem signs that he does not believe it himself",
               "Failing to work a miracle"],
         "c": 2,
         "why": "&ldquo;That which taketh away the reputation of Sincerity, is the "
                "doing, or saying of such things, as appeare to be signes, that what "
                "they require other men to believe, is not believed by themselves&rdquo;. "
                "Contradictories hurt his reputation for wisdom, private ends for love, "
                "and lack of miracles for the proof of his calling."},
        {"q": "In the chain preset the premises are c -> g and g -> d. What does the lab "
              "find about the conclusion c -> d?",
         "a": ["Invalid: one case has true premises and a false conclusion",
               "Valid: no case has true premises and a false conclusion",
               "Valid, but only if c is true",
               "Invalid: there are eight such cases"],
         "c": 1,
         "why": "No case makes both premises true and the conclusion false, so the "
                "argument is valid, a hypothetical syllogism. It does not need c to be "
                "true, since the conclusion is itself a conditional, and there are eight "
                "cases in all, none of them a counterexample."},
        {"q": "Why is the run-backwards preset invalid?",
         "a": ["Because the premises are inconsistent",
               "Because a teacher may be discredited without having enjoined "
               "contradictories",
               "Because d is false",
               "Because it has three premises"],
         "c": 1,
         "why": "In the counterexample cases c is false and d true: the teacher is "
                "discredited by some other cause, and Hobbes lists three. The premises "
                "are jointly satisfiable, and three premises are no fault in "
                "an argument."},
        {"q": "What does Hobbes say about revelation in the passage?",
         "a": ["It may be had of nothing above reason",
               "It may be had of many things above reason and nothing against it",
               "It may be had of things against natural reason, as mysteries",
               "It cannot be had at all"],
         "c": 1,
         "why": "&ldquo;which revelation a man may indeed have of many things above, but "
                "of nothing against naturall reason&rdquo;. That is why a contradiction "
                "cannot be defended as a mystery in his account, and why defenders of "
                "the mysteries deny that theirs is a contradiction."},
    ],
    "mistakes": [
        ("Thinking Hobbes says all religions were invented to control people",
         "He divides the cultivators in two. The founders of Gentile commonwealths "
         "ordered the seeds by their own invention; Abraham, Moses and Christ did it "
         "by God's command. Both aimed at obedience and peace, and the second class's "
         "religion he calls divine politics."),
        ("Treating contradictions as the only way a religion loses its hold",
         "Hobbes lists four: lost wisdom (contradictories), lost sincerity (scandal), "
         "lost love (private ends) and want of miracles. The run-backwards preset "
         "shows the argument cannot be turned round: a teacher can be discredited "
         "without having enjoined a contradiction."),
        ("Believing the lab can say which doctrines are contradictions",
         "The chain is valid however `c` is filled in. Whether any doctrine, the Trinity "
         "or the Real Presence, is a contradiction or only above reason is the "
         "dispute, and no table settles it."),
    ],
    "standard": (
        "Finish when you can set out a chain of conditionals and show what it needs.",
        "Given Hobbes's argument that enjoining contradictories discredits a teacher, "
        "write it as premises and a conclusion, say whether it is valid, show that it "
        "needs both premises, and say where a defender of a mystery resists it."
    ),
    "note": (
        "The lab checks the form of the chain and nothing else. It cannot say whether "
        "a given doctrine is a contradiction, whether detected ignorance does discredit "
        "a man in all else, or whether Hobbes's account of the founders is fair "
        "to any religion. His claims about Numa, Peru and Mahomet are claims about "
        "history and belief that the argument leaves untested."
    ),
}

LESSONS = [POWER_AND_WORTH, HONOUR_AND_DIGNITY, RESTLESS_DESIRE, SEEDS_OF_RELIGION, RELIGION_AND_POLICY]
