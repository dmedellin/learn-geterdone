"""The Progress of Opulence, lessons 1-4 -- Book III, Chapters 1 to 4.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt
(the Electronic Classics Series edition of the Inquiry); the comment beside each
lesson gives its line numbers. Smith's spelling is kept inside quotations. Where
the extraction jams or breaks a word across a line, the word is joined as a
printed book would print it. Book III is a history, and each lesson says which
of its narratives it reads in outline.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # PSU text l. 12236-12273 (the great commerce), l. 12274-12306 (subsistence
    # prior, the order of things), l. 12329-12344 (North America), l. 12369-12386
    # (the natural order, and its inversion).
    {
        "slug": "the-natural-progress-of-opulence",
        "title": "The Natural Progress of Opulence",
        "module": "Book III, Chapter 1 · Of the Natural Progress of Opulence",
        "one_line": "The great commerce of a society is between town and country, and in the natural course of things its capital goes first to agriculture, then to manufactures, and last to foreign commerce.",
        "summary": (
            "Book III begins by asking why nations grow rich in different orders. Smith's "
            "first answer is a picture of what would happen if nothing interfered: the "
            "country supplies the town with food and materials, the town repays it in "
            "manufactures, both gain, and capital goes first to the land. Work the gain "
            "from the exchange for a farmer and a weaver, and read why Smith says Europe "
            "has gone the other way round."
        ),
        "key": [
            "alone: each makes both goods in equal parts",
            "each makes the good that costs it less",
            "trade between them gives more of each",
            "the town buys from the surplus of the country",
            "capital goes land, then works, then trade",
        ],
        "key_label": "The natural order in five lines",
        "concepts_intro": (
            "Chapter 1 is two pages of reasoning from nature, and the rest of Book III "
            "reads as the history of why Europe departed from it. The reasoning is worth "
            "having whole before the history."
        ),
        "concepts": [
            ("The great commerce",
             "Between the inhabitants of the town and those of the country, an exchange of "
             "rude for manufactured produce. The country supplies subsistence and "
             "materials, the town repays with manufactured goods. Neither loses by it; "
             "the division of labour between them benefits both."),
            ("Subsistence comes first",
             "Because the town lives on the surplus of the country, what is over and above "
             "the maintenance of the cultivators, the town can grow only as that surplus "
             "grows. So cultivation of the land must, in the nature of things, come "
             "before the increase of the town."),
            ("The natural order of capital",
             "Upon equal profits, Smith says, most men prefer to put capital in land, then "
             "in manufactures, then in foreign trade, because each is more under their "
             "view and command than the next and so is safer. This is a statement about "
             "choice under equal profits, not about what any country in fact did."),
        ],
        "read_title": "The great commerce, and the order of things",
        "read_intro": (
            "Smith's first paragraph states the exchange, his second says why it must "
            "run in the order it does, and his last two say what happened in Europe. "
            "Read the first aloud: it is the plainest statement of the division of "
            "labour in the book."
        ),
        "body": [
            ("p", "<strong>Book III, Chapter 1.</strong> The great commerce, Smith begins, "
                  "&ldquo;of every civilized society is that carried on between the "
                  "inhabitants of the town and those of the country.&rdquo; Smith has finished the theory of "
                  "stock in Book II, and begins the third Book, on the different progress "
                  "of opulence in different nations, with this exchange: rude produce "
                  "for manufactured, directly or through money or paper."),
            ("p", "The town, he says, may &ldquo;very properly be said to gain its whole "
                  "wealth and subsistence from the country&rdquo;, because nothing is "
                  "reproduced there. A reader might conclude that the town's gain is the "
                  "country's loss. He denies it. &ldquo;The gains of both are mutual and "
                  "reciprocal, and the division of labour is in this, as in all other cases, "
                  "advantageous to all the different persons employed in the various "
                  "occupations into which it is subdivided.&rdquo; And he gives the country's "
                  "side first: &ldquo;The inhabitants of the country purchase of the town a "
                  "greater quantity of manufactured goods with the produce of a much smaller "
                  "quantity of their own labour, than they must have employed had they "
                  "attempted to prepare them themselves.&rdquo; The town in turn &ldquo;affords "
                  "a market for the surplus produce of the country&rdquo;, and the larger "
                  "the town the wider the market."),
            ("p", "The lab does that sum. In the town-country preset, written for this "
                  "lesson, a farmer and a weaver each have 1,200 hours. The farmer needs 2 "
                  "hours for a unit of corn and 6 for a unit of cloth, the weaver 6 and 2. "
                  "Each, working alone for himself, puts equal numbers of units of both "
                  "into the year: the farmer `1,200 / (2 + 6) = 150` of each, the weaver "
                  "150 of each, 300 of corn and 300 of cloth in all. Now each sticks to "
                  "the good that costs him less. The farmer makes 600 units of corn, the "
                  "weaver 600 of cloth, and they swap half each way: each ends the year "
                  "with 300 of corn and 300 of cloth, twice what he made alone. The sharp "
                  "preset makes the trades more unlike, a farmer needing 1 hour for corn "
                  "and 7 for cloth and a weaver the reverse. Alone each makes 150 of each, "
                  "and together 1,200 of each good is on offer, gaining 900 of each over "
                  "300. The rule the lab uses to decide who makes what is the "
                  "relative cost, hours per unit of one good against hours per unit of the "
                  "other, which is Ricardo's rule of 1817 and comes after Smith. In these "
                  "presets each is better at one good, and the two rules agree. The "
                  "first course's lesson <em>The Propensity to Truck, Barter and "
                  "Exchange</em> has the full version."),
            ("p", "Smith adds the position of the land near a town. Corn from a mile away "
                  "sells for the same price as corn from twenty, but the price of the "
                  "latter must pay for its carriage as well. The nearby proprietors "
                  "&ldquo;gain, in the price of what they sell, the whole value of the "
                  "carriage of the like produce that is brought from more distant "
                  "parts&rdquo;, and they save the same on what they buy. He draws a "
                  "dry conclusion about the balance of trade: &ldquo;Among all the absurd "
                  "speculations that have been propagated concerning the balance of trade, "
                  "it has never been pretended that either the country loses by its "
                  "commerce with the town, or the town by that with the country which "
                  "maintains it.&rdquo;"),
            ("p", "Then the order. &ldquo;As subsistence is, in the nature of things, prior "
                  "to conveniency and luxury, so the industry which procures the former, "
                  "must necessarily be prior to that which ministers to the latter.&rdquo; "
                  "It is the surplus of the country, &ldquo;what is over and above the "
                  "maintenance of the cultivators&rdquo;, that feeds the town. And this "
                  "necessity is, he says, promoted in each country by natural inclination. "
                  "&ldquo;Upon equal, or nearly equal profits, most men will choose to employ "
                  "their capitals, rather in the improvement and cultivation of land, than "
                  "either in manufactures or in foreign trade.&rdquo; The man who puts his "
                  "capital in land &ldquo;has it more under his view and command&rdquo;, and "
                  "the trader is obliged to commit his to &ldquo;the winds and the waves&rdquo; "
                  "and to the uncertain elements of human folly and injustice. To this he "
                  "adds the charms of the country, and that to cultivate the ground was "
                  "&ldquo;the original destination of man&rdquo;."),
            ("p", "Farmers need smiths, carpenters, wheelwrights, masons, tanners, "
                  "shoemakers and tailors, who need one another and settle near; the "
                  "butcher, brewer and baker join them, and a village is a town. &ldquo;The "
                  "inhabitants of the town, and those of the country, are mutually the "
                  "servants of one another.&rdquo; Their employment can grow only as the "
                  "country's demand for their finished work grows, and that only as "
                  "cultivation spreads. Where land is to be had cheaply, Smith says, "
                  "this is plain. In North America, an artificer who has saved a little "
                  "does not set up a manufacture for distant sale; &ldquo;From artificer he "
                  "becomes planter&rdquo;, because he &ldquo;feels that an artificer is the "
                  "servant of his customers&rdquo;, but a planter who lives from the labour "
                  "of his own family &ldquo;is really a master, and independent of all the "
                  "world&rdquo;. Where there is no land to be had, every artificer who "
                  "has saved more than the neighbourhood's jobs need prepares work for "
                  "distant sale."),
            ("def", ("The natural order of capital",
                     "First to agriculture, afterwards to manufactures, last of all to "
                     "foreign commerce. Smith derives it from security and attachment: "
                     "each next employment is farther from the owner's eye. He says it "
                     "has in some degree been observed in every society with territory, "
                     "and he does not call it a law.")),
            ("p", "He draws it out. &ldquo;According to the natural course of things, "
                  "therefore, the greater part of the capital of every growing society is, "
                  "first, directed to agriculture, afterwards to manufactures, and, last of "
                  "all, to foreign commerce.&rdquo; Foreign commerce, by this account, matters "
                  "less than it seems whose capital carries it. If a society has not enough "
                  "stock to cultivate all its land and manufacture its produce, there is "
                  "&ldquo;even a considerable advantage&rdquo; in a foreign capital carrying "
                  "the rude produce abroad, so that the society's own stock can be put to "
                  "more useful purposes. His examples are ancient Egypt, China and Indostan, "
                  "which became opulent with most of the export trade carried by foreigners."),
            ("p", "Then the departure. The natural order, he says, has &ldquo;in all the "
                  "modern states of Europe, been in many respects entirely inverted&rdquo;. "
                  "The foreign commerce of some cities introduced their finer manufactures, "
                  "and manufactures and foreign commerce together gave birth to the "
                  "principal improvements of agriculture. The manners and customs of the "
                  "original governments, which remained after the governments were altered, "
                  "&ldquo;necessarily forced them into this unnatural and retrograde "
                  "order&rdquo;. The next three lessons explain how: the laws of "
                  "inheritance and of land tenure, the rise of towns after the fall of "
                  "Rome, and what the commerce of towns did to the country."),
            ("p", "A reader should hold Smith's word &ldquo;natural&rdquo; at arm's length. "
                  "It is partly a claim about what people would choose and partly a story "
                  "of what happened in a few places, and economic historians since have "
                  "asked how much of Europe's history it fits. Smith himself says Italy, "
                  "cultivated through foreign commerce, was the exception. The lab does not "
                  "decide the question. It shows only that a farmer and a weaver with "
                  "different skills each get more by trading, which is the part of the "
                  "argument that does not depend on the order. The next lesson reads how "
                  "the great estates of post-Roman Europe held back the cultivation the "
                  "natural order needed."),
        ],
        "lab": ("wonkit", {
            "mode": "division",
            "view": "exchange",
            "goods": ["corn", "cloth"],
            "preset": "town-country",
            "presets": [
                {"id": "town-country", "label": "A farmer and a weaver, each better at one thing, written for this lesson",
                 "producers": "farmer, 1200, 2, 6; weaver, 1200, 6, 2",
                 "expect": {
                           "wdvSelfTotal": "corn 300; cloth 300",
                           "wdvSpecTotal": "corn 600; cloth 600",
                           "wdvGain": "corn +300; cloth +300"}},
                {"id": "sharp", "label": "The trades made more unlike, written for this lesson",
                 "producers": "farmer, 1200, 1, 7; weaver, 1200, 7, 1",
                 "expect": {
                           "wdvSelfTotal": "corn 300; cloth 300",
                           "wdvSpecTotal": "corn 1,200; cloth 1,200",
                           "wdvGain": "corn +900; cloth +900"}},
            ],
            "panel_title": "What town and country gain from the exchange",
            "panel_intro": (
                "Each producer's hours in the year and the hours a unit of corn and of "
                "cloth costs him go in. The lab shows what each makes if he works for "
                "himself, what each makes if he keeps to the cheaper good, and the gain in "
                "each good. Compare the two presets and see which tile the unlike "
                "trades move."
            ),
        }),
        "steps_title": "Working the gain from keeping to one trade",
        "steps_intro": "Four steps, for any two producers who can swap.",
        "steps": [
            ("Make each alone",
             "A producer who makes equal units of both goods with his hours, at a hours "
             "for the first and b for the second, makes his hours divided by a + b "
             "of each. Add the two producers' units."),
            ("Find each one's cheaper good",
             "Compare hours per unit of the first good against hours per unit of the "
             "second, for each producer. The one for whom the first is relatively "
             "cheaper makes the first; the other makes the second."),
            ("Let each make only that good",
             "Each puts all his hours into his cheaper good: hours divided by the "
             "hours a unit takes."),
            ("Compare the totals",
             "The gain in each good is what is on offer after specialising, less what "
             "was made alone. If there is a gain in both, each can end the year with "
             "more of both by swapping."),
        ],
        "worked": {
            "title": "A farmer, a weaver and 1,200 hours each",
            "intro": [
                "Take the town-country preset. The farmer needs 2 hours for corn and 6 "
                "for cloth, the weaver 6 for corn and 2 for cloth, and each has 1,200 "
                "hours.",
            ],
            "lines": [
                "farmer alone:  1,200 / (2 + 6) = 150 of each",
                "weaver alone:  1,200 / (6 + 2) = 150 of each",
                "together alone:  300 corn, 300 cloth",
                "farmer on corn:  1,200 / 2 = 600",
                "weaver on cloth:  1,200 / 2 = 600",
                "gain:  600 − 300 = 300 of each",
            ],
            "after": [
                "If they swap half of each output, each ends with 300 of corn and 300 of "
                "cloth, twice what he made alone. Smith's claim in the passage is the "
                "first half of this: the countryman gets the town's goods for much less "
                "of his own labour.",
            ],
        },
        "quiz_title": "Who gains from the great commerce",
        "quiz": [
            {"q": "In the town-country preset, how much of each good do the farmer and "
                  "the weaver together make if each works only for himself?",
             "a": ["600 of each", "150 of each", "1,200 of each", "300 of each"],
             "c": 3,
             "why": "Each makes `1,200 / (2 + 6) = 150` of each good, so the two make 300 of "
                    "each. Six hundred is what they make after specialising, 150 is what "
                    "one makes, and 1,200 is the farmer's hours."},
            {"q": "On Smith's account, what does the country get from the town?",
             "a": ["A market for its surplus produce, and manufactured goods for much "
                   "less of its own labour than it would spend making them",
                   "Its subsistence and the materials of its manufactures",
                   "Money, which the country cannot produce",
                   "Nothing, since the town lives only on the country"],
             "c": 0,
             "why": "&ldquo;The town affords a market for the surplus produce of the "
                    "country&rdquo;, and its people buy manufactured goods &ldquo;with the "
                    "produce of a much smaller quantity of their own labour&rdquo;. The "
                    "second option is what the town gets from the country, and Smith says "
                    "explicitly that the town's gain is not the country's loss."},
            {"q": "On Smith's account, why does he say the natural order puts capital in "
                  "agriculture first?",
             "a": ["Farmers are more skilled than manufacturers",
                   "Land pays a higher profit than manufactures",
                   "Upon equal profits the capital in land is more under the owner's view "
                   "and command, and so is safer",
                   "Law forbids manufacturers from owning land"],
             "c": 2,
             "why": "He says &ldquo;upon equal, or nearly equal profits&rdquo; and "
                    "gives the reason as security: the landowner has his capital under "
                    "his view and command, the trader must commit his to the winds, the waves "
                    "and distant debtors. He does not say land pays more."},
            {"q": "What does Smith say about the order of capital in the modern states of "
                  "Europe?",
             "a": ["It followed the natural order exactly",
                   "It has been in many respects entirely inverted, by manners and "
                   "customs left over from the original governments",
                   "It followed the natural order everywhere except Italy",
                   "It cannot be known, because no records survive"],
             "c": 1,
             "why": "He says it has &ldquo;in all the modern states of Europe, been in "
                    "many respects entirely inverted&rdquo;, forced by the manners and "
                    "customs of the original governments. Italy he treats as a case where "
                    "foreign commerce cultivated the whole country, in the last "
                    "chapter of Book III, not as the one that kept the natural order."},
        ],
        "mistakes": [
            ("Reading the natural order as a law of history",
             "Smith says the order has in some degree been observed in every society with "
             "territory and that Europe inverted it. The claim is about what most men "
             "would choose upon equal profits. It is a standard to measure Europe "
             "against, and the three chapters after this one are his account of why "
             "Europe fell short."),
            ("Supposing the town lives off the country at its expense",
             "Smith says it gains its whole subsistence from the country, and says "
             "at once that the gains of both are mutual and reciprocal. In the preset "
             "each producer ends with twice as much of each good. Whether real trade "
             "between town and country is always so fair is a different question, and "
             "Smith himself argues, in <em>Apprenticeship and Corporations</em>, that "
             "town corporations can tilt it."),
            ("Reading the lab's rule as Smith's",
             "The lab decides who makes what by relative cost, Ricardo's rule of 1817. "
             "Smith's own case is the simpler one in which each producer is better at "
             "one good, as here. When one is better at both, the two rules can come "
             "apart; Smith has nothing to say about that case."),
        ],
        "standard": (
            "Finish when you can work the gain from keeping to one trade.",
            "Given two producers' hours and the hours a unit of each good costs them, "
            "compute what each makes alone and what the two make after each keeps to "
            "his cheaper good, and the gain in each good."
        ),
        "note": (
            "The lab shows a gain from specialisation for stated hours; it does not show "
            "that town and country in any real society traded on such terms, or that "
            "the natural order is what capital would do. Later writers have disputed the "
            "natural order itself: the economic historians who find that long-distance "
            "trade and towns came first in much of Europe, and Marx, who in Capital "
            "treats the freeing of a labouring class from the land as the condition of "
            "capital rather than a consequence of farming. The numbers are written for "
            "the lesson and Smith gives none for this chapter."
        ),
    },
    # ---------------------------------------------------------------- 02
    # PSU text l. 12387-12470 (primogeniture and entails), l. 12479-12513 (the
    # great proprietor), l. 12514-12621 (slaves and metayers), l. 12622-12676
    # (farmers and leases), l. 12698-12747 (the taille; the farmer a borrower),
    # l. 12748-12762 (the policy of Europe). The history of the German and
    # Scythian conquest and of the church of Rome is read in outline.
    {
        "slug": "primogeniture-entails-and-tenants",
        "title": "Primogeniture, Entails and Tenants",
        "module": "Book III, Chapter 2 · Of the Discouragement of Agriculture in the Ancient State of Europe",
        "one_line": "Great estates kept whole by primogeniture and entail, worked by slaves, then metayers, then farmers on short leases, gave nobody the reason to improve the land.",
        "summary": (
            "After Rome fell, Smith says, the land of Western Europe was engrossed by a few "
            "great proprietors, and the laws of primogeniture and entail kept it so. He "
            "then goes through the ways land was occupied, slaves, metayers who farm "
            "for half the produce, and farmers who rent for a fixed sum, and asks of "
            "each whether the occupier had a reason to improve. Work that question as "
            "arithmetic: an improvement that costs a sum and adds a yearly produce, "
            "under four tenures and three terms."
        ),
        "key": [
            "gain = share × added × years − cost borne",
            "improves only if the gain is above zero",
            "years to repay = cost / (share × added)",
            "halving the share doubles the years",
        ],
        "key_label": "When an improvement pays the one who makes it",
        "concepts_intro": (
            "The chapter's argument is that the land of Europe stayed unimproved because "
            "of who held it and on what terms. The lab can ask the question Smith asks of "
            "each kind of holder: does the improvement pay the man who must make it?"
        ),
        "concepts": [
            ("Primogeniture and entail",
             "When land was power, it was kept whole by descending to one heir, the eldest "
             "son, and entails bound it to a line. Smith says the reasons vanished when "
             "the lords stopped being petty princes and the laws stayed, and that a great "
             "proprietor &ldquo;seldom&rdquo; improves, having neither the leisure, "
             "the inclination, nor the habit of small savings and gains."),
            ("Who bears the cost, who gets the return",
             "A slave acquires nothing but his maintenance; a metayer keeps half the "
             "produce, and the landlord, who lays out nothing, takes the other half; a "
             "tenant farmer on a lease keeps all the produce for the term but pays "
             "the cost of improving. Each holder's reason to improve is what he gets "
             "back from it."),
            ("Security of the lease",
             "A farmer improves only if the lease is long enough to repay him. Smith "
             "praises England, where the tenant's security is equal to the proprietor's, "
             "and finds a French lease of nine years, lately lengthened to twenty-seven, "
             "too short."),
        ],
        "read_title": "Great estates, and who occupied them",
        "read_intro": (
            "The chapter opens with the engrossing of land and goes through the laws, "
            "the proprietors and four kinds of occupier. This lesson reads it in outline, "
            "leaving out the history of the conquest and of the church, and goes "
            "slowly over the tenures."
        ),
        "body": [
            ("p", "<strong>Book III, Chapter 2.</strong> When the German and Scythian "
                  "nations overran the western provinces of the Roman empire, the land "
                  "was engrossed &ldquo;by a few great proprietors&rdquo;. It might have "
                  "been a transitory evil, divided again by succession or sale. &ldquo;The "
                  "law of primogeniture hindered them from being divided by succession; "
                  "the introduction of entails prevented their being broke into small "
                  "parcels by alienation.&rdquo; The old Roman law divided land among all "
                  "the children, like moveables. Primogeniture came when land meant "
                  "&ldquo;power and protection&rdquo;: every great landlord was a petty "
                  "prince, his tenants his subjects, and &ldquo;To divide it was to ruin "
                  "it&rdquo;."),
            ("p", "His comment on the later survival is one of the book's best-known "
                  "sentences. &ldquo;Laws frequently continue in force long after the "
                  "circumstances which first gave occasion to them, and which could alone "
                  "render them reasonable, are no more.&rdquo; In the present state of "
                  "Europe the owner of one acre is as secure as the owner of 100,000, and "
                  "primogeniture survives as &ldquo;the fittest to support the pride of "
                  "family distinctions&rdquo;. Entails he finds &ldquo;completely "
                  "absurd&rdquo;, resting on &ldquo;the supposition that every successive "
                  "generation of men have not an equal right to the earth, and to all that "
                  "it possesses; but that the property of the present generation should "
                  "be restrained and regulated according to the fancy of those who died, "
                  "perhaps five hundred years ago&rdquo;. In Scotland &ldquo;more than one "
                  "fifth, perhaps more than one third part of the whole lands in the "
                  "country, are at present supposed to be under strict entail&rdquo;."),
            ("p", "What follows is the economic point. &ldquo;It seldom happens, however, "
                  "that a great proprietor is a great improver.&rdquo; In disorderly times "
                  "he had no leisure, and later no inclination and &ldquo;almost always "
                  "the requisite abilities&rdquo;. To improve land profitably &ldquo;like "
                  "all other commercial projects, requires an exact attention to small "
                  "savings and small gains, of which a man born to a great fortune, even "
                  "though naturally frugal, is very seldom capable&rdquo;. He embellishes "
                  "four or five hundred acres near his house at ten times what the land is "
                  "worth, and would be bankrupt before he finished a tenth of the rest."),
            ("p", "Then those who occupied the land. In the ancient state of Europe "
                  "&ldquo;the occupiers of land were all tenants at will. They were all, "
                  "or almost all, slaves&rdquo;, and whatever they improved was improved "
                  "at the master's expense and for his benefit. Smith's judgment on "
                  "slave labour is flat: &ldquo;The experience of all ages and nations, "
                  "I believe, demonstrates that the work done by slaves, though it appears "
                  "to cost only their maintenance, is in the end the dearest of any.&rdquo; "
                  "The reason he gives is incentive: &ldquo;A person who can acquire no "
                  "property can have no other interest but to eat as much and to labour "
                  "as little as possible.&rdquo; He says slavery then survived only where "
                  "the crop could bear its expense, sugar and tobacco but not corn, a "
                  "statement about what the planters of the 1770s found profitable and "
                  "not a defence of it; he adds that the pride of man makes him love to "
                  "domineer, and prefer slaves wherever the law and the work allow."),
            ("p", "The next occupier is the metayer, the coloni partiarii of the Latin "
                  "authors. The proprietor supplied the seed, cattle and instruments, "
                  "the produce was divided equally after the stock was made good, and the "
                  "metayer, being a freeman, had &ldquo;a plain interest that the whole "
                  "produce should be as great as possible, in order that their own "
                  "proportion may be so&rdquo;. It was a gain over slavery. But he could "
                  "not improve at his own expense: &ldquo;It could never, however, be the "
                  "interest even of this last species of cultivators, to lay out, in the "
                  "further improvement of the land, any part of the little stock which "
                  "they might save from their own share of the produce; because the "
                  "landlord, who laid out nothing, was to get one half of whatever it "
                  "produced.&rdquo; The tithe, a mere tenth, is &ldquo;a very great "
                  "hindrance to improvement&rdquo;, so a tax of one half must have been "
                  "&ldquo;an effectual bar&rdquo;. In France, Smith says, five parts out "
                  "of six of the kingdom were still so occupied, and the proprietors "
                  "complained that metayers used their masters' cattle for carriage, where "
                  "they kept the whole profit, rather than for cultivation, where they "
                  "shared it."),
            ("p", "Last came farmers properly so called, who cultivated with their own "
                  "stock and paid a rent certain. &ldquo;When such farmers have a lease for "
                  "a term of years, they may sometimes find it for their interest to lay "
                  "out part of their capital in the further improvement of the farm; "
                  "because they may sometimes expect to recover it, with a large profit, "
                  "before the expiration of the lease.&rdquo; But their possession was "
                  "long precarious: a new purchaser could oust them, and until the action "
                  "of ejectment, invented about the 14th of Henry VII, a tenant turned out "
                  "had only damages. &ldquo;In England, therefore the security of the "
                  "tenant is equal to that of the proprietor.&rdquo; Smith adds that a "
                  "lease for life of forty shillings a year made a tenant a freeholder with "
                  "a vote, which made the yeomanry respectable to their landlords, and "
                  "that those laws and customs &ldquo;have perhaps contributed more to the "
                  "present grandeur of England, than all their boasted regulations of "
                  "commerce taken together&rdquo;. Elsewhere security was short: in France "
                  "a lease was good against a purchaser for only &ldquo;nine years from "
                  "the commencement of the lease&rdquo;, lately extended to twenty-seven, "
                  "&ldquo;a period still too short to encourage the tenant to make the "
                  "most important improvements&rdquo;."),
            ("def", ("Gain from an improvement (this lab's term)",
                     "What the occupier gets back from an improvement over the years he "
                     "holds it: his share of the added produce times the added produce "
                     "times the years, less the part of the cost he bears. Smith argues "
                     "from interest, in words. The lab puts his argument into arithmetic "
                     "with one stated cost and one stated yield, both written for the "
                     "lesson.")),
            ("p", "The lab takes an improvement that costs 90 pounds and adds 15 pounds of "
                  "produce a year, figures written for this lesson, and asks four holders "
                  "the question. The slave bears no cost and keeps no share, so his gain "
                  "is nothing and he does not improve. The metayer bears the whole cost and "
                  "keeps half, 7 pounds 10 shillings a year. The farmer on a lease bears "
                  "the whole cost and keeps all 15. A farmer who also pays a tithe keeps "
                  "nine tenths, 13 pounds 10 shillings. In the nine-years preset, "
                  "France's term, the farmer gains `15 × 9 − 90 = 45`, the farmer paying "
                  "tithe `(9/10) × 15 × 9 − 90 = 31.50`, and the metayer's half share makes "
                  "`(1/2) × 15 × 9 − 90 = −22.50`, a loss, so he does not improve. In "
                  "the five-years preset no one improves, because even the farmer's 75 "
                  "does not repay 90. In the twenty-seven-years "
                  "preset all of them do, the metayer with a gain of 112.50. The number of "
                  "years that repays an improvement is the cost divided by the "
                  "yearly return the occupier keeps, 6 years for the farmer and 12 for the "
                  "metayer. Halve the share and the term doubles."),
            ("p", "Smith closes the tenants with two more grievances: arbitrary services "
                  "in the lease and the purveyors who took horses, carriages and "
                  "provisions at the king's price. And the taille, still in France, a tax "
                  "on the supposed profits of the farmer, which they estimate from the "
                  "stock he has on the farm: &ldquo;It is his interest, therefore, to appear "
                  "to have as little as possible, and consequently to employ as little as "
                  "possible in its cultivation, and none in its improvement.&rdquo; The "
                  "farmer who borrows his land is, in Smith's comparison, like a "
                  "merchant trading with borrowed money, whose stock must improve more "
                  "slowly than that of one who trades with his own, since a large share of "
                  "the profits is consumed by interest. After small proprietors, he "
                  "says, rich and great farmers are in every country the principal "
                  "improvers. And the older policy of Europe, prohibiting the export of "
                  "corn and punishing engrossers, regraters and forestallers, did the "
                  "rest. The next lesson turns to the other half of the story: how the "
                  "towns came to be free."),
        ],
        "lab": ("wonkit", {
            "mode": "rent",
            "view": "tenure",
            "money_unit": "£",
            "preset": "nine-years",
            "presets": [
                {"id": "five-years", "label": "A five-year lease, improvement figures written for this lesson",
                 "cost": 90, "added": 15, "years": 5,
                 "tenures": "slave, 0, 0; metayer, 1/2, 1; farmer, 1, 1; farmer-with-tithe, 9/10, 1",
                 "expect": {
                           "wreGain": "slave £0; metayer −£52.50; farmer −£15; farmer-with-tithe −£22.50",
                           "wreImproves": "0: none"}},
                {"id": "nine-years", "label": "France's nine years, Smith's term; improvement figures written for this lesson",
                 "cost": 90, "added": 15, "years": 9,
                 "tenures": "slave, 0, 0; metayer, 1/2, 1; farmer, 1, 1; farmer-with-tithe, 9/10, 1",
                 "expect": {
                           "wreGain": "slave £0; metayer −£22.50; farmer +£45; farmer-with-tithe +£31.50",
                           "wreImproves": "2: farmer, farmer-with-tithe"}},
                {"id": "twenty-seven-years", "label": "France's twenty-seven years, Smith's term; improvement figures written for this lesson",
                 "cost": 90, "added": 15, "years": 27,
                 "tenures": "slave, 0, 0; metayer, 1/2, 1; farmer, 1, 1; farmer-with-tithe, 9/10, 1",
                 "expect": {
                           "wreGain": "slave £0; metayer +£112.50; farmer +£315; farmer-with-tithe +£274.50",
                           "wreImproves": "3: metayer, farmer, farmer-with-tithe"}},
            ],
            "panel_title": "Does the improvement pay the one who makes it?",
            "panel_intro": (
                "The cost of an improvement, the produce it adds a year, the years the "
                "occupier holds, and each tenure's share of the added produce and share "
                "of the cost go in. The lab shows each occupier's gain over the years and "
                "which of them would improve. Change only the years between the presets "
                "and see which tenures cross from loss to gain."
            ),
        }),
        "steps_title": "Testing whether an occupier would improve",
        "steps_intro": "Four steps, for any tenure and any term.",
        "steps": [
            ("State the improvement",
             "Its cost and the extra produce it adds in a year. Both are the lesson's figures; "
             "Smith gives no table."),
            ("Find what the occupier keeps",
             "Multiply the extra produce by the occupier's share, then by the years he "
             "holds."),
            ("Subtract what he bears",
             "Multiply the cost by the share of it the occupier pays. The remainder is "
             "his gain; if it is above nothing, he would improve."),
            ("Find the term that just pays",
             "Divide the cost he bears by what he keeps in a year. A smaller share "
             "needs a longer term, in proportion."),
        ],
        "worked": {
            "title": "The metayer and the farmer, nine years",
            "intro": [
                "Take the nine-years preset: an improvement costing 90 pounds and adding 15 "
                "a year, on a nine-year term. The metayer bears the cost and keeps a "
                "half share; the farmer bears it and keeps all.",
            ],
            "lines": [
                "farmer keeps:  1 · 15 · 9 = 135",
                "farmer's gain:  135 − 90 = 45",
                "metayer keeps:  (1/2) · 15 · 9 = 67.5",
                "metayer's gain:  67.5 − 90 = −22.5",
                "metayer's break-even:  90 / ((1/2) · 15) = 12 years",
            ],
            "after": [
                "The farmer improves and the metayer does not, on the same land, the same "
                "improvement and the same term. Give the metayer twenty-seven years and "
                "he gains 112.50, which is why Smith writes that it could never be his "
                "interest to improve at his own expense: the share, not the land, is what "
                "stops him, and the term has to be long to make up for it.",
            ],
        },
        "quiz_title": "Who has a reason to improve",
        "quiz": [
            {"q": "An improvement costs 90 and adds 15 a year. A farmer who keeps all of it "
                  "and bears all the cost holds the land for 9 years. What does he gain?",
             "a": ["135", "45", "90", "−22.50"],
             "c": 1,
             "why": "He keeps `15 × 9 = 135` and pays 90, so he gains `135 − 90 = 45`. "
                    "A hundred and thirty-five is what he keeps before the cost, 90 is "
                    "the cost, and −22.50 is the metayer's result on the same figures."},
            {"q": "On the same figures, a metayer keeps half the added produce and bears the "
                  "whole cost. How many years must he hold the land for the improvement to "
                  "repay him?",
             "a": ["6 years", "12 years", "9 years", "18 years"],
             "c": 1,
             "why": "He keeps `(1/2) × 15 = 7.5` a year, so `90 / 7.5 = 12`. Six years is "
                    "what the full-share farmer needs; 18 would be a third of the "
                    "produce."},
            {"q": "Why does Smith say the work of slaves is in the end the dearest of any?",
             "a": ["Slaves must be bought, and prices of slaves rise",
                   "A person who can acquire no property has no interest but to eat as much "
                   "and labour as little as possible",
                   "Slaves are less skilled than freemen at every task",
                   "Slave owners are prevented by law from improving their land"],
             "c": 1,
             "why": "That is his reason, in his words. He says nothing in the passage "
                    "about the price of slaves or about the skill of the enslaved, and the "
                    "owners' power over the land is the opposite of a restraint."},
            {"q": "What does Smith say of the security of the tenant in England compared "
                  "with France?",
             "a": ["In England the tenant's security is equal to the proprietor's; in "
                   "France a lease held for nine years from its start, lately lengthened "
                   "to twenty-seven, was still too short",
                   "Both countries secured tenants for life",
                   "In France the tenant's security was equal to the proprietor's",
                   "In England a lease was good against purchasers for nine years"],
             "c": 0,
             "why": "The passage says &ldquo;In England, therefore the security of the "
                    "tenant is equal to that of the proprietor&rdquo; and that in France "
                    "the term was limited &ldquo;to nine years from the commencement of "
                    "the lease&rdquo;, since extended to twenty-seven, still too short to "
                    "encourage the most important improvements."},
        ],
        "mistakes": [
            ("Thinking the argument is about land rather than about who holds it",
             "In the lab the improvement, its cost and its yield are the same for every "
             "tenure. Only the share and the term differ. Smith's claim is that the "
             "holder's reason to improve depends on what he is left with, and the "
             "four rows show it."),
            ("Reading Smith as saying slavery is unprofitable everywhere",
             "He says its work is dearest in the end, and then says it can bear the "
             "expense of sugar and tobacco and not of corn. The lesson reports his claim "
             "about corn and about what the planters found. Historians of the "
             "American South and of the West Indies have since argued about how "
             "profitable slavery was; the lab has nothing to say on it."),
            ("Treating the cost and the yield as Smith's",
             "The 90 pounds and the 15 are written for the lesson. The nine and "
             "twenty-seven years are Smith's, for France. The point of the preset is "
             "the form of the comparison, not the amounts."),
        ],
        "standard": (
            "Finish when you can tell whether an occupier would improve.",
            "Given an improvement's cost and yearly return, the years the occupier "
            "holds, and his shares of the produce and of the cost, compute his gain "
            "and the term that just repays him."
        ),
        "note": (
            "The lab assumes the occupier sees the whole return, with no risk, no "
            "discount and no chance of being turned out sooner. Smith's own argument "
            "is looser and richer, and covers ornament, pride, habit and the "
            "disposition of the great. Later writers have asked how well it fits the "
            "evidence. Historians of agrarian change have found great estates that "
            "improved and small holders who did not, and the sharecropping literature "
            "of the twentieth century, from Alfred Marshall's discussion of the metayer "
            "to later work on incentives, takes up this passage. Capital's lesson "
            "<em>Genesis of the Capitalist Farmer</em> reads the farmer's rise from the "
            "other side."
        ),
    },
    # ---------------------------------------------------------------- 03
    # PSU text l. 12768-12815 (the early towns), l. 12816-12876 (the farm of the
    # town), l. 12877-12963 (why the sovereign granted it), l. 12964-12987
    # (order and good government in cities), l. 13004-13035 (Italy and the first
    # manufactures), l. 13049-13133 (the two sorts of manufactures). The
    # narratives of the cities of Italy and Germany are read in outline.
    {
        "slug": "the-rise-of-towns",
        "title": "The Rise of Towns",
        "module": "Book III, Chapter 3 · Of the Rise and Progress of Cities and Towns",
        "one_line": "Towns got liberty and good order before the country did, because the sovereign let them farm their own dues for a fixed sum and so made allies of them against the lords.",
        "summary": (
            "Smith tells how the towns of Europe, first peopled by men almost servile, "
            "became free: the king let the burghers farm the revenue arising from their "
            "town for a rent certain, then in fee for ever, and gave them magistrates and "
            "walls. He finds it extraordinary that a sovereign should fix for ever the "
            "branch of his revenue most likely to grow. Work what a fixed farm costs the "
            "one who lets it, as the town grows, and what it costs the farmers if the "
            "town declines."
        ),
        "key": [
            "farm = a fixed sum, whatever the dues",
            "dues − farm = what the king gives up",
            "farm / dues falls as the dues grow",
            "a fixed farm costs the farmer if dues fall",
            "farm in fee: the sum never rises",
        ],
        "key_label": "A fixed farm in five lines",
        "concepts_intro": (
            "This chapter is a story, and a rich one. The lesson takes one thread of it, "
            "the farm of the town, and the arithmetic that thread contains."
        ),
        "concepts": [
            ("The farm of the town",
             "The king's revenue from a town, the dues and poll-taxes, was at first let "
             "to the sheriff or another farmer for a term. The burghers themselves got "
             "credit enough to take the farm, jointly and severally answerable for "
             "the sum. In time it was granted in fee, for ever, at a rent certain never "
             "afterwards to be augmented."),
            ("An alliance against the lords",
             "The lords despised the burghers and plundered them; the king feared the "
             "lords. Mutual interest therefore disposed them to support one another. "
             "Granting the town its own magistrates, walls and militia gave it the means "
             "of security the king could not give."),
            ("Liberty first in the towns",
             "Order and good government, and with them the liberty and security of the "
             "individual, were established in cities while the occupiers of land were "
             "exposed to every sort of violence. Industry that aims beyond subsistence "
             "needs security, and so it began in towns."),
        ],
        "read_title": "How the towns got free, and why a king would sell his growth",
        "read_intro": (
            "Smith's narrative runs from the almost servile hawkers of the early towns "
            "to the cities of Italy and the free burghs of France and England. This "
            "lesson follows the money and leaves the political history in outline."
        ),
        "body": [
            ("p", "<strong>Book III, Chapter 3.</strong> After the fall of Rome, the "
                  "proprietors of land lived in fortified castles among their tenants, "
                  "and &ldquo;The towns were chiefly inhabited by tradesmen and mechanics, "
                  "who seem, in those days, to have been of servile, or very nearly of "
                  "servile condition&rdquo;. The privileges the old charters grant them, "
                  "to give their daughters in marriage without the lord's consent, to "
                  "leave their goods to their children, to make a will, show by being "
                  "privileges what they had lacked. They travelled from fair to fair like "
                  "pedlars, and taxes were levied on them at manors, bridges and booths, "
                  "under the names of passage, pontage, lastage and stallage. A king or a "
                  "great lord would exempt particular traders, who paid a poll-tax in "
                  "return and were called free traders."),
            ("p", "Yet the towns came to liberty first. &ldquo;it appears evidently, that "
                  "they arrived at liberty and independency much earlier than the "
                  "occupiers of land in the country.&rdquo; The step that did it was "
                  "financial. The king's revenue from such poll-taxes in a town was let "
                  "to farm for a term of years, and the burghers themselves &ldquo;frequently "
                  "got credit enough to be admitted to farm the revenues of this sort&rdquo; "
                  "that arose out of their own town, &ldquo;they becoming jointly and "
                  "severally answerable for the whole rent&rdquo;. They paid it to the exchequer by "
                  "their own bailiff, collecting it their own way, &ldquo;being thus "
                  "altogether freed from the insolence of the king's officers&rdquo;. In "
                  "process of time the farm was granted in fee, &ldquo;reserving a rent "
                  "certain, never afterwards to be augmented&rdquo;. Because the payment "
                  "was perpetual, the exemptions it paid for became perpetual too, and "
                  "ceased to be personal: they belonged to the burghers of a free burgh. "
                  "They were erected into a corporation with magistrates, a council, "
                  "bye-laws and walls, and with the duty of watch and ward."),
            ("p", "Smith then stops to say that this is odd. &ldquo;it must seem "
                  "extraordinary, that the sovereigns of all the different countries of "
                  "Europe should have exchanged in this manner for a rent certain, never "
                  "more to be augmented, that branch of their revenue, which was, "
                  "perhaps, of all others, the most likely to be improved by the natural "
                  "course of things, without either expense or attention of their own.&rdquo; "
                  "He gives two reasons. A sovereign who could not protect the weak "
                  "from the great lords needed allies, and the lords hated the burghers: "
                  "&ldquo;The lords despised the burghers, whom they considered not only as "
                  "a different order, but as a parcel of emancipated slaves.&rdquo; So "
                  "&ldquo;Mutual interest, therefore, disposed them to support the king, "
                  "and the king to support them against the lords.&rdquo; And a farm in "
                  "fee took away all ground for suspicion that the king would later raise "
                  "the rent or let it to someone else. Princes on the worst terms with "
                  "their barons were the most liberal in these grants: King John in "
                  "England, Lewis the Fat in France, the Suabian emperors in Germany."),
            ("p", "The lab does the sum that Smith finds extraordinary. In the growing "
                  "preset, written for this lesson, a town's dues are worth 100 pounds a "
                  "year when the king grants the farm, and he fixes the farm at 100 for "
                  "ever. Smith gives no figures, and the dues are the lesson's: 125 after "
                  "twenty years, 160 after forty, 200 after sixty, 260 after eighty and 320 "
                  "after a hundred. At the end the town pays 100 when its dues are worth "
                  "320, the king is giving up 220 a year, and the farm is 31.25 percent of "
                  "what the dues would yield; across the six years the lab lists, the "
                  "fixed farm raises 600 where the dues would have raised 1,165. It started at 100 percent. In the still "
                  "preset the town does not grow and the farm costs the king nothing. "
                  "In the declining preset the dues fall to 60 and the same fixed "
                  "100 is now more than the town can raise, so the loss is on the burghers, "
                  "who are jointly and severally answerable for the whole rent, and the "
                  "lab, which adds the six years it lists as a sample, shows the "
                  "difference as negative: the fixed farm raises 600 against 480 from "
                  "the dues themselves. Smith's wonder is at the "
                  "first case: nothing in a fixed farm protects the sovereign from "
                  "the growth he did not expect, and he took the rent for a good he "
                  "valued more, the allies and the security."),
            ("def", ("A fixed farm (this lab's term)",
                     "A sum owed every year that does not change as the yield it was "
                     "taken against changes. The lab's land-tax view calls it a "
                     "valuation: the same arithmetic works for an English land tax on a "
                     "valuation of 1692, which the course on taxes reads. Smith is "
                     "describing a rent certain; the lab compares it with what the same "
                     "dues would have yielded at the rate stated.")),
            ("p", "Good government followed security. &ldquo;Order and good government, "
                  "and along with them the liberty and security of individuals, were in "
                  "this manner established in cities, at a time when the occupiers of land "
                  "in the country, were exposed to every sort of violence.&rdquo; Men in a "
                  "defenceless state &ldquo;naturally content themselves with their "
                  "necessary subsistence&rdquo;, since to acquire more might only tempt "
                  "their oppressors, and when secure of the fruits of "
                  "their industry &ldquo;they naturally exert it to better their "
                  "condition&rdquo;. A villain who saved a little would hide it and run "
                  "to a town, where, if he could conceal himself &ldquo;from the pursuit "
                  "of his lord for a year, he was free for ever&rdquo;. So stock took "
                  "refuge in cities, &ldquo;as the only sanctuaries in which it could be "
                  "secure to the person that acquired it&rdquo;."),
            ("p", "A city on the sea or a navigable river need not live off its "
                  "neighbours. It can draw its subsistence from the remote corners of "
                  "the world, and it may grow rich while all the countries it trades to "
                  "are poor. Smith's examples are the Greek empire and the Saracens, and "
                  "above all the Italian cities, raised by commerce in the centre of the "
                  "civilised world. The crusades, which wasted Europe, made Venice, Genoa and "
                  "Pisa the commissaries of the armies: &ldquo;the most destructive frenzy "
                  "that ever befel the European nations, was a source of opulence to those "
                  "republics&rdquo;. The wool of England went for the wines of France in "
                  "this period, and the taste for finer manufactures, once introduced, "
                  "made merchants set up their own to save the carriage."),
            ("p", "He ends by sorting manufactures for distant sale into two kinds. Some "
                  "are the offspring of foreign commerce, imitations established by "
                  "particular merchants' stock, in imported materials: the silk of Lucca, "
                  "which in 1310 drove nine hundred families into exile and so sent "
                  "thirty-one to Venice to begin the manufacture with three hundred "
                  "workmen, the fine cloths of Flanders, the silk of Lyons and "
                  "Spitalfields. Others grow up naturally, by the gradual refinement of "
                  "household manufactures upon the produce of the country, in inland places "
                  "where a fertile soil gives a surplus of provisions that is hard to "
                  "carry to the water. Workmen settle where provisions are cheap, give the "
                  "surplus a new value, and the cultivators are encouraged to grow more. "
                  "Fine cloth is the case: &ldquo;contains in it the price, not only of "
                  "eighty pounds weight of wool, but sometimes of several thousand weight "
                  "of corn&rdquo;, so that the corn is virtually exported in the cloth. "
                  "&ldquo;Such manufactures are the offspring of agriculture&rdquo;, and "
                  "the manufactures of Leeds, Halifax, Sheffield, Birmingham and "
                  "Wolverhampton are of this sort; in the modern history of Europe they "
                  "came after those that were the offspring of foreign commerce. The "
                  "last chapter of the book says how the commerce of towns improved the "
                  "country that had been left behind."),
        ],
        "lab": ("wonkit", {
            "mode": "tax",
            "view": "land",
            "money_unit": "£",
            "preset": "growing",
            "presets": [
                {"id": "growing", "label": "A fixed farm of 100 on dues that grow to 320, dues written for this lesson",
                 "valuation": 100, "rate": 100,
                 "rents": "1, 100; 20, 125; 40, 160; 60, 200; 80, 260; 100, 320",
                 "expect": {
                           "wtxShares": "1 100%; 20 80%; 40 62.5%; 60 50%; 80 ≈ 38.46%; 100 31.25%",
                           "wtxTotals": "fixed £600, on the actual rent £1,165, over 6 years",
                           "wtxDifference": "+£565: the tax on the actual rent raises more"}},
                {"id": "still", "label": "A town whose dues stand still, written for this lesson",
                 "valuation": 100, "rate": 100,
                 "rents": "1, 100; 20, 100; 40, 100; 60, 100; 80, 100; 100, 100",
                 "expect": {
                           "wtxShares": "1 100%; 20 100%; 40 100%; 60 100%; 80 100%; 100 100%",
                           "wtxDifference": "none: the two raise the same"}},
                {"id": "declining", "label": "A town whose dues fall to 60, written for this lesson",
                 "valuation": 100, "rate": 100,
                 "rents": "1, 100; 20, 95; 40, 85; 60, 75; 80, 65; 100, 60",
                 "expect": {
                           "wtxShares": "1 100%; 20 ≈ 105.26%; 40 ≈ 117.65%; 60 ≈ 133.33%; 80 ≈ 153.85%; 100 ≈ 166.67%",
                           "wtxTotals": "fixed £600, on the actual rent £480, over 6 years",
                           "wtxDifference": "−£120: the tax on the actual rent raises less"}},
            ],
            "panel_title": "A rent certain against what the dues would yield",
            "panel_intro": (
                "The fixed sum, the rate at which the dues would otherwise be taken and "
                "the dues in each year go in. The lab shows what the fixed sum is as a "
                "share of the dues each year and what the sovereign gives up, or what the "
                "farmers lose when the dues fall. Compare the growing preset with "
                "the declining one in the last row."
            ),
        }),
        "steps_title": "Pricing a rent certain",
        "steps_intro": "Four steps, for any fixed payment against a yield that moves.",
        "steps": [
            ("Fix the sum",
             "The farm is a number that does not change with the years. At the rate of "
             "100 percent the fixed sum is itself the yearly payment."),
            ("Read each year's dues",
             "These are what the king would have collected had he kept the revenue."),
            ("Find the share",
             "Divide the fixed sum by the year's dues. It is 100 percent when they "
             "are equal and shrinks as the dues grow."),
            ("Find the difference",
             "Dues less the fixed sum is what the sovereign gives up when positive, "
             "and what falls on the burghers when negative."),
        ],
        "worked": {
            "title": "A hundred years of a fixed farm",
            "intro": [
                "Take the growing preset: a farm of 100 pounds a year fixed for ever, "
                "on dues that are 100 in the first year and 320 in the hundredth.",
            ],
            "lines": [
                "first year:  100 / 100 = 100% of the dues",
                "year 60:  100 / 200 = 50%; given up 200 − 100 = 100",
                "year 100:  100 / 320 = 31.25%",
                "given up in year 100:  320 − 100 = 220",
                "the declining town, year 100:  100 / 60 = 166.67%; 40 over",
            ],
            "after": [
                "The same fixed 100 is a third of the dues in one town and more than all "
                "of them in another. Smith's wonder is at the first sort of town, whose "
                "natural growth the king gave away, and the second is the risk the "
                "burghers took in being jointly answerable.",
            ],
        },
        "quiz_title": "A rent certain",
        "quiz": [
            {"q": "In the growing preset the fixed farm is 100 a year. In the year the "
                  "dues have reached 200, what share of them is the farm?",
             "a": ["200 percent", "100 percent", "31.25 percent", "50 percent"],
             "c": 3,
             "why": "`100 / 200 = 1/2`, which is 50 percent, and the sovereign gives up "
                    "`200 − 100 = 100`. A hundred percent is the first year, 31.25 is the "
                    "last year's share, and 200 percent would be the farm twice the dues."},
            {"q": "What does Smith find extraordinary about the farm in fee?",
             "a": ["That towns paid a poll-tax at all",
                   "That sovereigns exchanged for a rent certain, never more to be "
                   "augmented, the branch of their revenue most likely to be improved "
                   "by the natural course of things",
                   "That burghers were made answerable jointly and severally",
                   "That the rent was paid to the exchequer by the town's own bailiff"],
             "c": 1,
             "why": "&ldquo;it must seem extraordinary&rdquo; is his own phrase for it. "
                    "The other three are details of how the farm worked, which he "
                    "treats as unremarkable and, in the case of the bailiff, as of the "
                    "greatest importance to the burghers at the time."},
            {"q": "Why, on Smith's account, did the king grant towns magistrates, "
                  "walls and the farm in fee?",
             "a": ["The towns paid more than the king could otherwise raise",
                   "The towns had bought the privileges from the church",
                   "The king and the burghers had a common enemy in the lords, and the "
                   "grants made the burghers secure and independent of them",
                   "Roman law required it"],
             "c": 2,
             "why": "&ldquo;Mutual interest, therefore, disposed them to support the king, "
                    "and the king to support them against the lords.&rdquo; Smith "
                    "stresses the weakness of the sovereign, who could not protect the "
                    "weaker part of his subjects, and says nothing of purchase from "
                    "the church or of Roman law."},
            {"q": "On Smith's account, why did stock and industry flourish in towns before "
                  "the country?",
             "a": ["The soil near towns was more fertile",
                   "Towns had more capital to start with",
                   "Towns had better roads to market",
                   "Order and good government, with liberty and security, were established "
                   "there while the occupiers of land were exposed to every sort of violence"],
             "c": 3,
             "why": "That is the sentence. Men who are secure of the fruit of their "
                    "industry exert it to better their condition; those who are not "
                    "&ldquo;naturally content themselves with their necessary "
                    "subsistence&rdquo;. He does not rest the case on the soil, on a "
                    "prior stock, or on roads."},
        ],
        "mistakes": [
            ("Thinking the figures are Smith's",
             "He gives no numbers for any town's farm or dues. The 100, 320 and 60 are "
             "written for the lesson to show what a rent certain does when the yield "
             "changes. Smith's evidence is Domesday Book, Madox's <em>Firma Burgi</em> and "
             "the charters, which the lesson only cites."),
            ("Reading the farm as a gift to the towns alone",
             "The farm was a bargain, the burghers paying a rent and taking on the "
             "collection and a joint liability. In the declining preset they would be "
             "worse off. Smith's wonder is at what the king gave away on one side of "
             "a bargain whose terms he had every reason to think fair."),
            ("Supposing Smith says towns made the country poor",
             "He says the opposite in Chapter 1 and again at the end of Chapter 3: the "
             "manufactures that are the offspring of agriculture improved the land. "
             "The point of this chapter is the order, towns first, which he calls "
             "contrary to the natural course."),
        ],
        "standard": (
            "Finish when you can price a fixed farm against the dues it replaced.",
            "Given a fixed yearly sum and a series of yearly dues, compute the fixed "
            "sum as a share of each year's dues and what the sovereign gives up, or "
            "the burghers lose, each year."
        ),
        "note": (
            "The lab's fixed sum is a fixed valuation, and the same arithmetic prices a "
            "land tax on an old assessment. It shows what a rent certain gives up when a "
            "yield grows; it cannot say that the king should not have granted it, "
            "since the grant bought him an ally. Historians of the medieval town have "
            "disputed Smith's story of the farm in fee and of the alliance with the "
            "king, finding more variety than a single account allows, and the Italian "
            "cities he treats as a case of commerce first. Capital's lesson "
            "<em>Genesis of the Capitalist Farmer</em> reads a fixed money rent from "
            "the farmer's side, in the sixteenth century, when prices rose."
        ),
    },
    # ---------------------------------------------------------------- 04
    # PSU text l. 13137-13181 (three ways), l. 13182-13232 (hospitality and
    # dependence), l. 13281-13323 (the feudal law; diamond buckles), l.
    # 13324-13386 (the £10,000 a year; long leases), l. 13409-13430 (the
    # revolution; Europe and America), l. 13431-13574 (small proprietors; the
    # state of England, France, Italy; precarious capital). The accounts of the
    # feudal institutions and of the Lochiel rising are read in outline.
    {
        "slug": "how-commerce-improved-the-country",
        "title": "How Commerce Improved the Country",
        "module": "Book III, Chapter 4 · How the Commerce of the Towns Contributed to the Improvement of the Country",
        "one_line": "A great lord who spent his rents on a pair of diamond buckles instead of a thousand retainers dissolved his own power, and no one meant it to.",
        "summary": (
            "Smith says the commerce of towns improved the country in three ways: by a "
            "market for its produce, by merchants who bought land and improved it, and, "
            "most important and least observed, by bringing order and good government "
            "and with them liberty. Work the third: a revenue of £10,000 that once "
            "maintained a thousand dependants, and now pays a hundred trades a tiny "
            "share of each worker's maintenance."
        ),
        "key": [
            "retainers kept = revenue / maintenance",
            "a trade's share = pay per maker / upkeep",
            "a share of 1: wholly the lord's man",
            "makers kept in part can far exceed retainers",
            "every share below 1: independent of him",
        ],
        "key_label": "Dependence, as a share of upkeep",
        "concepts_intro": (
            "This is the chapter Smith says contains the most important of commerce's "
            "effects, and says it is the one least observed, except by Hume. It is also "
            "the one where an arithmetic of shares explains the claim."
        ),
        "concepts": [
            ("Three effects",
             "A ready market for the produce of the country, which benefits first the "
             "land nearest; merchants buying land, who make the best improvers because "
             "they are used to profitable projects; and order and good government, with "
             "the liberty and security of individuals. The third, Smith says, is by far "
             "the most important."),
            ("Dependence is a share",
             "A man is dependent on whoever maintains him. A retainer fed at the lord's "
             "table gets all of his maintenance from one man. A tradesman who serves a "
             "thousand customers gets a thousandth from each, and can be maintained "
             "without any one of them."),
            ("An unintended revolution",
             "Smith says the great proprietors acted from &ldquo;the most childish "
             "vanity&rdquo; and the merchants from their own interest, and that "
             "neither had &ldquo;knowledge or foresight&rdquo; of what they were "
             "bringing about."),
        ],
        "read_title": "The diamond buckles, and what they bought",
        "read_intro": (
            "The chapter's central pages describe what a great proprietor did with his "
            "rents before and after commerce gave him something to buy. Read them as "
            "the story of a man who is better off, and a country that is freer, by "
            "accident."
        ),
        "body": [
            ("p", "<strong>Book III, Chapter 4.</strong> The commerce of towns, Smith says, "
                  "contributed to the improvement of the country in three ways. First, "
                  "&ldquo;by affording a great and ready market for the rude produce of "
                  "the country, they gave encouragement to its cultivation and further "
                  "improvement&rdquo;, most of all to their own neighbourhood, where the "
                  "produce is charged with less carriage. Second, the wealth of the cities "
                  "was often employed in buying land, and &ldquo;Merchants are commonly "
                  "ambitious of becoming country gentlemen, and, when they do, they are "
                  "generally the best of all improvers&rdquo;, because a merchant is "
                  "accustomed to employ his money in profitable projects, a country "
                  "gentleman chiefly in expense. The merchant is &ldquo;commonly a bold, a "
                  "country gentleman a timid undertaker&rdquo;."),
            ("p", "The third is the one he cares for. &ldquo;Thirdly, and lastly, commerce "
                  "and manufactures gradually introduced order and good government, and "
                  "with them the liberty and security of individuals, among the "
                  "inhabitants of the country, who had before lived almost in a continual "
                  "state of war with their neighbours, and of servile dependency upon "
                  "their superiors. This, though it has been the least observed, is by far "
                  "the most important of all their effects. Mr Hume is the only writer "
                  "who, so far as I know, has hitherto taken notice of it.&rdquo;"),
            ("p", "He explains it from a rich man's table. In a country with neither "
                  "foreign commerce nor fine manufactures, a great proprietor &ldquo;having "
                  "nothing for which he can exchange the greater part of the produce of "
                  "his lands which is over and above the maintenance of the cultivators, "
                  "consumes the whole in rustic hospitality at home&rdquo;. If the surplus "
                  "can maintain a hundred or a thousand men, he can use it in no other "
                  "way. His retainers have nothing to give in return, and so &ldquo;must "
                  "obey him, for the same reason that soldiers must obey the prince who "
                  "pays them&rdquo;. The picture is vivid: Westminster Hall as the dining "
                  "room of William Rufus, the Earl of Warwick said to have fed 30,000 "
                  "people a day at his manors, an Arabian chief dining in the street and "
                  "inviting beggars to join. The tenants were as dependent as the "
                  "retainers: a crown, half a crown, a sheep or a lamb was in the "
                  "Highlands a common rent for land that maintained a family."),
            ("p", "On that dependence, Smith says, rested the power of the barons. They "
                  "became judges in peace and leaders in war because each could turn the "
                  "force of all his dwellers against any one. He gives a late example, "
                  "Cameron of Lochiel, a Highland gentleman whose rent never exceeded "
                  "£500 a year and who nevertheless took 800 of his own people into "
                  "the rebellion of 1745. The feudal law, he says, "
                  "tried to moderate this and could not, because it could not alter the "
                  "state of property and manners. Commerce did instead what it could not: &ldquo;what all the violence of the "
                  "feudal institutions could never have effected, the silent and "
                  "insensible operation of foreign commerce and manufactures gradually "
                  "brought about.&rdquo;"),
            ("p", "What brought it about was something to buy. These &ldquo;gradually "
                  "furnished the great proprietors with something for which they could "
                  "exchange the whole surplus produce of their lands, and which they "
                  "could consume themselves, without sharing it either with tenants or "
                  "retainers. All for ourselves, and nothing for other people, seems, in "
                  "every age of the world, to have been the vile maxim of the masters of "
                  "mankind.&rdquo; And so: &ldquo;For a pair of diamond buckles, perhaps, "
                  "or for something as frivolous and useless, they exchanged the "
                  "maintenance, or, what is the same thing, the price of the maintenance "
                  "of 1000 men for a year, and with it the whole weight and authority "
                  "which it could give them.&rdquo; With the judges who were to determine "
                  "the preference, the difference was decisive: the buckles were to be "
                  "all their own, whereas in the older way they must have shared with at "
                  "least 1000 people."),
            ("def", ("A share of maintenance (this lab's term)",
                     "What a purchase pays one maker, divided by what that maker needs to be "
                     "maintained for a year. When every share is under one, no maker "
                     "depends on the purchaser for his livelihood; at one, he is wholly "
                     "the purchaser's. Smith writes of a tenth, a hundredth, a thousandth; "
                     "the lab computes the fraction from the figures you enter.")),
            ("p", "Smith does the sum himself. &ldquo;In a country where there is no "
                  "foreign commerce, nor any of the finer manufactures, a man of £10,000 "
                  "a-year cannot well employ his revenue in any other way than in "
                  "maintaining, perhaps, 1000 families, who are all of them necessarily "
                  "at his command. In the present state of Europe, a man of £10,000 "
                  "a-year can spend his whole revenue, and he generally does so, without "
                  "directly maintaining twenty people.&rdquo; He maintains more, but "
                  "indirectly: &ldquo;Its great price generally arises from the wages of "
                  "their labour, and the profits of all their immediate employers.&rdquo; "
                  "And what he contributes to each is small, &ldquo;to a very few, "
                  "perhaps, not a tenth, to many not a hundredth, and to some not a "
                  "thousandth, or even a ten thousandth part of their whole annual "
                  "maintenance&rdquo;. So &ldquo;they are all more or less independent of "
                  "him, because generally they can all be maintained without him&rdquo;."),
            ("p", "The lab takes Smith's £10,000 and 1,000 families, and so £10 as one "
                  "family's yearly keep, a figure that is the lesson's inference from "
                  "his two numbers. In the old-way preset the lord's £10,000 goes to 1,000 "
                  "retainers: the share each draws of his maintenance is "
                  "`10,000 / 1,000 / 10 = 1`, and every one is wholly his. In the "
                  "new-way preset, written for this lesson, he spends the same £10,000 "
                  "in four trades: broadcloth £4,000 across 4,000 makers, wine £3,000 "
                  "across 6,000, silk and lace £2,000 across 10,000, and jewels and "
                  "buckles £1,000 across 10,000. The shares are 1/10, 1/20, 1/50 and "
                  "1/100, none of them one. He keeps in part 30,000 people and wholly "
                  "none. The half preset keeps half the revenue in the old way, "
                  "£5,000 on 500 retainers, and shows what Smith's account predicts: "
                  "those 500 are still wholly his, so the lab reports that someone "
                  "depends on him, and 8,000 people are kept in part or whole. The new "
                  "independence is only partial."),
            ("p", "Then the consequences. Retainers were dismissed, tenants enlarged "
                  "into farms, and the unnecessary mouths removed; the lord, wanting more "
                  "to spend, demanded the full value of the farm, and could get it only "
                  "by granting security. &ldquo;The expensive vanity of the landlord made "
                  "him willing to accept of this condition; and hence the origin of long "
                  "leases.&rdquo; A tenant with a long lease is altogether independent, "
                  "and his landlord &ldquo;must not expect from him even the most trifling "
                  "service&rdquo;. The great proprietors, &ldquo;Having sold their "
                  "birth-right, not like Esau, for a mess of pottage in time of hunger "
                  "and necessity, but, in the wantonness of plenty, for trinkets and "
                  "baubles, fitter to be the playthings of children than the serious "
                  "pursuits of men&rdquo;, became as insignificant as a burgher, and "
                  "regular government was established in the country as in the city."),
            ("p", "He sums the matter as an irony of motives. &ldquo;A revolution of the "
                  "greatest importance to the public happiness, was in this manner "
                  "brought about by two different orders of people, who had not the "
                  "least intention to serve the public.&rdquo; Vanity moved the "
                  "proprietors, and the merchants acted &ldquo;from a view to their own "
                  "interest, and in pursuit of their own pedlar principle of turning a "
                  "penny wherever a penny was to be got&rdquo;. Readers "
                  "have often compared it with the invisible hand of Book IV, Chapter 2, "
                  "though Smith does not use the phrase here. He adds a warning: the "
                  "order was against nature, and so slow. The people of Europe, he "
                  "says, were not supposed to double in less than five hundred years, "
                  "against twenty or five-and-twenty in several North American "
                  "colonies, whose wealth is founded wholly in agriculture."),
            ("p", "The last pages compare countries. England, well placed for commerce, "
                  "has favoured both, and the yeomanry as secure as law can make them, "
                  "yet its land is far from fully improved. France had foreign "
                  "commerce a century before England, and has an inferior agriculture. "
                  "Italy alone was cultivated by means of commerce and manufactures for "
                  "distant sale. And the chapter ends on the warning that the capital "
                  "acquired by commerce is &ldquo;always a very precarious and uncertain "
                  "possession, till some part of it has been secured and realized in the "
                  "cultivation and improvement of its lands&rdquo;: a merchant is not "
                  "necessarily the citizen of any country, and no vestige remains of "
                  "the wealth said to have belonged to the Hanse Towns. Book IV turns "
                  "from how Europe got its order to the systems of political economy "
                  "that grew from it. The next course reads the first of them, the "
                  "mercantile system."),
        ],
        "lab": ("wonkit", {
            "mode": "stock",
            "view": "spend",
            "money_unit": "£",
            "preset": "old-way",
            "presets": [
                {"id": "old-way", "label": "Smith's £10,000 on 1,000 families; one family's £10 inferred from them",
                 "revenue": 10000, "maintenance": 10,
                 "purchases": "retainers-and-tenants, 10000, 1000",
                 "expect": {
                           "wstRetainers": "1,000 people",
                           "wstShares": "retainers-and-tenants 100%",
                           "wstPeople": "1,000 people",
                           "wstDependent": "1: retainers-and-tenants (each maker wholly maintained by the purchase)"}},
                {"id": "new-way", "label": "The same £10,000 spent in four trades, written for this lesson",
                 "revenue": 10000, "maintenance": 10,
                 "purchases": "broadcloth, 4000, 4000; wine, 3000, 6000; silk-and-lace, 2000, 10000; jewels-and-buckles, 1000, 10000",
                 "expect": {
                           "wstShares": "broadcloth 10%; wine 5%; silk-and-lace 2%; jewels-and-buckles 1%",
                           "wstPeople": "30,000 people",
                           "wstDependent": "no one: every maker’s share is under one maintenance"}},
                {"id": "half", "label": "Half kept in the old way, half spent in two trades, written for this lesson",
                 "revenue": 10000, "maintenance": 10,
                 "purchases": "retainers, 5000, 500; broadcloth, 2500, 2500; wine, 2500, 5000",
                 "expect": {
                           "wstShares": "retainers 100%; broadcloth 10%; wine 5%",
                           "wstPeople": "8,000 people",
                           "wstDependent": "1: retainers (each maker wholly maintained by the purchase)"}},
            ],
            "panel_title": "Who depends on the great lord's spending",
            "panel_intro": (
                "The revenue, one person's yearly maintenance, and what the lord spends on "
                "each trade and how many makers it comes from go in. The lab shows how many "
                "retainers the revenue could keep directly, the share of each maker's "
                "maintenance each purchase pays, and whether anyone is wholly dependent. "
                "Compare the old-way preset with the new-way one."
            ),
        }),
        "steps_title": "Measuring a dependence",
        "steps_intro": "Four steps, for any revenue spent among people.",
        "steps": [
            ("Count the retainers the revenue could keep",
             "Divide the revenue by one person's yearly maintenance. It is the most "
             "people the lord could feed at his own table."),
            ("Find what one purchase pays each maker",
             "Divide the amount spent on a trade by the number of makers it buys from."),
            ("Turn it into a share of maintenance",
             "Divide that payment by one person's yearly maintenance. A share of 1 is a "
             "wholly dependent maker; a share of 1/100 is one who lives almost "
             "entirely on someone else."),
            ("Ask who is wholly dependent",
             "If no purchase has a share of 1 the lord commands no one's livelihood; "
             "the number of makers partly maintained, added up, shows how much wider "
             "his spending reaches."),
        ],
        "worked": {
            "title": "Broadcloth and diamond buckles",
            "intro": [
                "Take the new-way preset. A lord spends £4,000 on broadcloth made by "
                "4,000 people and £1,000 on jewels and buckles made by 10,000. One "
                "person needs £10 a year.",
            ],
            "lines": [
                "broadcloth, pay each:  4,000 / 4,000 = £1",
                "broadcloth, share of keep:  1 / 10 = 1/10",
                "jewels and buckles, pay each:  1,000 / 10,000 = £1/10",
                "jewels and buckles, share:  (1/10) / 10 = 1/100",
                "kept in part:  4,000 + 6,000 + 10,000 + 10,000 = 30,000",
            ],
            "after": [
                "The same £10,000 that kept 1,000 people wholly now keeps 30,000 in part, "
                "and no one is wholly kept. Smith's words are that the lord indirectly "
                "maintains &ldquo;as great, or even a greater number&rdquo; than before, "
                "and that each of them is independent of him.",
            ],
        },
        "quiz_title": "A revenue spent two ways",
        "quiz": [
            {"q": "On Smith's figures a man of £10,000 a year could once maintain about "
                  "1,000 families. If one family's yearly keep is £10, what share of "
                  "its maintenance does a retainer draw from the lord?",
             "a": ["1/10", "1/1,000", "All of it, a share of 1", "1/100"],
             "c": 2,
             "why": "`10,000 / 1,000 = 10` each, which is a family's whole £10, so the "
                    "share is `10 / 10 = 1`. The other shares are the sort of figure "
                    "Smith gives for what the lord pays tradesmen, not retainers."},
            {"q": "In the new-way preset £2,000 is spent on silk and lace made by 10,000 "
                  "people, and a person needs £10 a year. What share of a maker's "
                  "maintenance does the purchase pay?",
             "a": ["1/20", "1/50", "1/100", "1/10"],
             "c": 1,
             "why": "Each maker gets `2,000 / 10,000 = 1/5` of a pound, and "
                    "`(1/5) / 10 = 1/50`. A twentieth is wine's share, a hundredth "
                    "jewels', and a tenth is broadcloth's."},
            {"q": "Why does Smith say the great proprietors lost their power as they "
                  "spent on the products of commerce?",
             "a": ["Merchants lent them money and took their land",
                   "Their tenants rose against them in the name of liberty",
                   "The king passed laws taking their jurisdictions",
                   "Each could now spend the whole revenue on himself, so retainers were "
                   "dismissed and tenants, given long leases, became independent"],
             "c": 3,
             "why": "Smith says &ldquo;what all the violence of the feudal institutions could never "
                    "have effected, the silent and insensible operation of foreign "
                    "commerce and manufactures gradually brought about.&rdquo; He credits "
                    "neither the king's laws nor a rising of the tenants."},
            {"q": "How does Smith describe the motives of the two orders who brought "
                  "about this revolution?",
             "a": ["The proprietors acted from the most childish vanity and the "
                   "merchants from their own interest; neither intended to serve the public",
                   "Both acted from a view to the public good",
                   "The merchants were moved by vanity and the proprietors by profit",
                   "Both acted from a plan to reduce the king's power"],
             "c": 0,
             "why": "&ldquo;To gratify the most childish vanity was the sole motive of the "
                    "great proprietors. The merchants and artificers, much less "
                    "ridiculous, acted merely from a view to their own interest.&rdquo; "
                    "Neither &ldquo;had either knowledge or foresight of that great "
                    "revolution&rdquo;."},
        ],
        "mistakes": [
            ("Reading the chapter as praise of vanity",
             "Smith calls the proprietors' motive childish, mean and sordid, and the "
             "buckles frivolous. His point is that a revolution &ldquo;of the "
             "greatest importance to the public happiness&rdquo; came from motives "
             "that did not aim at it, which is a claim about consequences and not about "
             "the worth of the motives."),
            ("Supposing the lab's numbers are history",
             "Only the £10,000 and the thousand families are Smith's, and the "
             "£10 is inferred from them. The four trades, their makers and the half "
             "preset are written for the lesson. The point is the form of the "
             "comparison, shares rather than headcounts."),
            ("Treating independence as equality",
             "In the new-way preset no maker is wholly the lord's, and the lord is "
             "still a great proprietor with great rents. Smith's claim is that the "
             "power to command followers, not the wealth, was what went."),
        ],
        "standard": (
            "Finish when you can measure how far a spender's customers depend on him.",
            "Given a revenue, one person's yearly maintenance, and what is spent on each "
            "trade and how many makers it comes from, compute the retainers it could "
            "keep and each purchase's share of a maker's maintenance, and say whether "
            "anyone is wholly dependent."
        ),
        "note": (
            "Dependence in the lab is arithmetic: a share of a maker's keep. Smith's "
            "argument is about authority, which the lab cannot measure, and a maker "
            "who sells to a single lord at a tenth of his keep may still live in fear "
            "of him. Historians have asked how much of the decline of the feudal "
            "lords it explains, with taxation, firearms and royal courts competing as "
            "causes, and Capital's lesson <em>Expropriation of the Agricultural "
            "Population</em> reads the breaking up of the retainers' bands as the first "
            "stage of driving the peasantry off the land, where Smith traces the loss of "
            "the lords' power."
        ),
    },
]
