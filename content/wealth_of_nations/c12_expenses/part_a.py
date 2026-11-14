"""The Expenses of the Sovereign, lessons 1-3 -- Book V, Chapter 1, Parts I and II
and the first section of Part III, Article I.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt
(the Electronic Classics Series edition, Pennsylvania State University, 2005); the
comment beside each lesson gives its line numbers. Smith's spelling is kept inside
quotations. Money is in pounds sterling; where a figure is Smith's the lesson says so,
and where it is written for the lesson the lesson says that.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # PSU text l. 22509-23096 (Book V, Chapter 1, Part I). Opening l. 22511-22513;
    # shepherds l. 22559-22560; manufacturers l. 22643-22647; one hundredth part
    # l. 22680-22682; militia and standing army l. 22760-22769; firearms l. 23071-23073
    # and l. 23090-23096.
    {
        "slug": "the-expense-of-defence",
        "title": "The Expense of Defence",
        "module": "Book V, Chapter 1, Part 1 · Of the Expense of Defence",
        "one_line": "The soldier of a rude people costs the sovereign nothing, and the soldier of a rich one must be paid by everyone else, which is why Smith says not more than one in a hundred can be spared.",
        "summary": (
            "Book V opens by asking what the sovereign must pay for, and the first duty is "
            "defence. Smith runs through hunters, shepherds, husbandmen and manufacturers "
            "and shows the cost of a soldier rising at each step, until the nation that "
            "pays him can afford only a small share of its people under arms. Work out how "
            "many soldiers a population supports at Smith's fraction, and what they cost."
        ),
        "key": [
            "hunter, shepherd: each man his own soldier",
            "the artificer must be maintained by others",
            "soldiers = population × share under arms",
            "yearly cost = soldiers × cost of one",
            "Smith: one in a hundred, not many more",
        ],
        "key_label": "Defence, from the tribe to the standing army",
        "concepts_intro": (
            "Part I is a history of one cost. It starts at nothing and ends at the largest "
            "item in a modern budget, and the argument is about why the figure moves."
        ),
        "concepts": [
            ("Who pays for the soldier",
             "Among hunters and shepherds every man is a warrior and maintains himself in "
             "the field as at home, so the sovereign pays nothing. Husbandmen can be spared "
             "between seedtime and harvest. But an artificer who leaves his workhouse has "
             "no income at all, and a long war of several campaigns a year takes even the "
             "farmer from his fields. From then on the public must maintain the army."),
            ("A number the nation can afford",
             "In a civilised society the soldiers are kept by the labour of everyone who "
             "is not a soldier, so their number is limited by what the rest can spare. "
             "Smith gives the figures: a fourth or a fifth of the people in the ancient "
             "agrarian states, and in modern Europe not more than one in a hundred."),
            ("Militia and standing army",
             "In a militia the soldier keeps his other trade and drills now and then; in "
             "a standing army soldiering is the whole occupation and the state pays for "
             "it. Smith holds that the division of labour has to reach war, as it reaches "
             "every art, and that a well-regulated standing army always beats a militia."),
        ],
        "read_title": "The passage first, then Part I a stage at a time",
        "read_intro": (
            "Part I is about six hundred lines long and goes through four stages of "
            "society. The lesson reads it in the same order: the opening claim, the "
            "stages, the arithmetic, and then the argument over militias."
        ),
        "body": [
            ("p", "<strong>Book V, Chapter 1, Part 1.</strong> &ldquo;that of protecting the "
                  "society from the violence and invasion of other independent societies, can "
                  "be performed only by means of a military force.&rdquo; Smith is describing "
                  "the first of the sovereign's three duties, and adds at once that the cost "
                  "of preparing a force in peace and employing it in war &ldquo;is very "
                  "different in the different states of society&rdquo;."),
            ("p", "Book V is where the book turns from how wealth is made to how a "
                  "government is paid for, and Chapter 1 counts the costs before Chapter 2 "
                  "finds the money. Think of a household budget written in the order of what "
                  "has to be paid for, with the biggest and least avoidable item first. For "
                  "a sovereign that item is the army."),
            ("p", "The first stage costs nothing. Among hunters, such as the native tribes "
                  "of North America, &ldquo;every man is a warrior, as well as a hunter&rdquo;, "
                  "and he maintains himself in the field by his own labour, as at home. "
                  "Smith's account of these peoples comes from travellers' reports, not from "
                  "his own observation, and the lesson reads it as his model: a stage in an "
                  "argument, not a field study. Among shepherds, the next stage, the herds "
                  "and flocks go to war with the men. A Tartar chief &ldquo;is at no sort of "
                  "expense in preparing him for the field; and when he is in it, the chance of "
                  "plunder is the only pay which he either expects or requires&rdquo;."),
            ("p", "Husbandmen come next, and here the cost begins to appear. A farmer can "
                  "take the field after seedtime and be home for harvest, because &ldquo;Nature "
                  "does herself the greater part of the work&rdquo; of the farm in the meantime; "
                  "so a short campaign costs the sovereign little. The Greeks served this way "
                  "until after the second Persian war, and the Romans until the siege of Veii. Then two causes "
                  "make it impossible, Smith says: the progress of manufactures and the "
                  "improvement of the art of war."),
            ("p", "The first is the smith or the weaver. &ldquo;Nature does nothing for him; "
                  "he does all for himself.&rdquo; The moment he leaves his workhouse his "
                  "income stops, so he &ldquo;must necessarily be maintained by the public&rdquo;. "
                  "The second is the length of the war. Once a contest is spun out over "
                  "several campaigns, each lasting most of the year, no private man can bear "
                  "the cost, and Athens, Rome and the feudal lords each ended up paying for "
                  "their armies."),
            ("def", ("Militia and standing army",
                     "In a militia &ldquo;the character of the labourer, artificer, or "
                     "tradesman, predominates over that of the soldier&rdquo;; in a standing "
                     "army &ldquo;that of the soldier predominates over every other "
                     "character&rdquo;. The difference is which occupation feeds the man: the "
                     "militiaman's living comes from some other trade, the regular's from "
                     "the state.")),
            ("p", "Now the arithmetic the lab does. In ancient Greece, Smith says, a fourth "
                  "or a fifth of the people thought of themselves as soldiers, and in every "
                  "nation the men of military age amount to about that share. Among modern "
                  "Europeans &ldquo;not more than the one hundredth part of the inhabitants of "
                  "any country can be employed as soldiers, without ruin to the country which "
                  "pays the expense of their service&rdquo;. Take a state of 100,000 people "
                  "(a number written for the lesson). At `1/5` that is 20,000 soldiers, the "
                  "Greek preset, which leaves the cost blank because a citizen of such a "
                  "state served without pay in a short campaign. A country of 1,000,000 at `1/100` supports 10,000, the "
                  "modern preset. Put a yearly cost on each, which Smith does not give, "
                  "and the figure is the budget: at £20 a head, a number written for "
                  "this lesson, those 10,000 cost £200,000 a year, or four shillings for "
                  "each of the million people, with 99 others at work for every "
                  "soldier. The overreach preset, which is not Smith's, puts one in twenty "
                  "of the same million under arms: 50,000 soldiers, £1,000,000 a year, 19 "
                  "others at work for each, and a pound a head."),
            ("p", "Smith's reason for the ceiling is not that the arithmetic needs it but "
                  "that the others must work to feed the soldiers and also feed "
                  "&ldquo;themselves and the other officers of government and law&rdquo;. "
                  "The share follows from what the rest can spare. A reader who finds one in "
                  "a hundred too small or too large is arguing with a remark of Smith's about "
                  "the Europe of his day, which he says is &ldquo;commonly computed&rdquo;, "
                  "and which the lab takes as a figure to compute with."),
            ("p", "Smith then gives a second argument, from the division of labour. A "
                  "wealthy, industrious nation, he says, &ldquo;is of all nations the most "
                  "likely to be attacked&rdquo;, and its people have no leisure for drill: a "
                  "shepherd has a great deal, a husbandman some, and an artificer none. A "
                  "state has two courses: force the citizens to practise arms alongside their "
                  "trades, or make soldiering a separate trade. That second course takes "
                  "more than private interest, since a private man who drilled all day "
                  "&ldquo;would not promote his own interest&rdquo;, and so &ldquo;it is the "
                  "wisdom of the state only, which can render the trade of a soldier a "
                  "particular trade&rdquo;."),
            ("p", "His verdict goes to the standing army and he gives it at length: Philip "
                  "of Macedon's army beat the Greek militias, Hannibal's standing army beat "
                  "Rome's militia at the Trebia, Thrasymenus and Cannae, and Rome in turn "
                  "became a standing army. The one exception he allows is a militia that "
                  "&ldquo;becomes in every respect a standing army&rdquo; after a few "
                  "campaigns, and he suggests that the American militia might do so against the "
                  "British regulars, in the war then going on as he wrote. He also "
                  "notes the best militias are the Tartars', who follow chiefs they obey in "
                  "peace."),
            ("p", "The standing army had a critic in Smith's own day, and the objection "
                  "deserves a hearing. Men of republican principles, Smith concedes, "
                  "&ldquo;have been jealous of a standing army, as dangerous to liberty&rdquo;, "
                  "and he grants the examples of Caesar and Cromwell: it is dangerous wherever the "
                  "generals' interest is not tied to the constitution. His friend Adam "
                  "Ferguson argued for a citizen militia, on the ground of civic liberty, and "
                  "Smith's answer, that where the sovereign is himself the general and the "
                  "nobility and gentry the officers an army can never threaten liberty, "
                  "depends on a particular constitution. It is a claim about Britain, not a "
                  "theorem. Smith returns to the question in Article II, where he asks the "
                  "state to keep up the martial spirit of the whole people so that a smaller "
                  "standing army would do."),
            ("p", "The last stage is the cost of the weapons. &ldquo;A musket is a more "
                  "expensive machine than a javelin or a bow and arrows; a cannon or a "
                  "mortar, than a balista or a catapulta.&rdquo; Powder spent in a review is "
                  "lost for good, where javelins could be picked up again. Smith concludes "
                  "that the cost of firearms favours the rich: &ldquo;In ancient times, the "
                  "opulent and civilized found it difficult to defend themselves against the "
                  "poor and barbarous nations. In modern times, the poor and barbarous find "
                  "it difficult to defend themselves against the opulent and civilized.&rdquo; "
                  "Historians still argue about how much gunpowder, standing armies and "
                  "the rise of the state had to do with one another, and Smith's one-way "
                  "story is a short version of a long dispute. The lesson skips his long "
                  "narrative of Greece, Rome and the Tartars, which is the evidence for the "
                  "militia argument and which a reader can take in the book."),
            ("p", "Part I settles who has to be paid for, and Part II turns to the second "
                  "duty, where the cost depends on property: in the next lesson, "
                  "<em>The Expense of Justice</em>, you will see why a sovereign could "
                  "once make money from his courts."),
        ],
        "lab": ("wonkit", {
            "mode": "public",
            "view": "soldiers",
            "money_unit": "£",
            "preset": "greece",
            "presets": [
                {"id": "greece",
                 "label": "A state of 100,000 at Smith's fifth under arms (population written for this lesson)",
                 "population": 100000, "share": "1/5", "cost": "-", "expect": {
                    "wpbSoldiers": "20,000",
                    "wpbOthers": "4",
                    "wpbCost": "no cost given",
                    "wpbPerHead": "no cost given",
                }},
                {"id": "modern",
                 "label": "A country of 1,000,000 at Smith's one in a hundred (population and £20 a soldier written for this lesson)",
                 "population": 1000000, "share": "1/100", "cost": 20, "expect": {
                    "wpbSoldiers": "10,000",
                    "wpbOthers": "99",
                    "wpbCost": "£200,000 a year",
                    "wpbPerHead": "£0.2 a head a year",
                }},
                {"id": "overreach",
                 "label": "The same country at one in twenty (written for this lesson, to see what Smith says it cannot bear)",
                 "population": 1000000, "share": "1/20", "cost": 20, "expect": {
                    "wpbSoldiers": "50,000",
                    "wpbOthers": "19",
                    "wpbCost": "£1,000,000 a year",
                    "wpbPerHead": "£1 a head a year",
                }},
            ],
            "panel_title": "How many soldiers, and at what cost",
            "panel_intro": (
                "Enter a population, the share of it under arms and, if you like, a yearly "
                "cost for one soldier. The lab multiplies. Try the Greek preset, which is "
                "Smith's fraction, then the modern one, then the third, which is not "
                "Smith's but shows the ceiling at work."
            ),
        }),
        "steps_title": "Pricing an army",
        "steps_intro": "Four steps, for any population and any share.",
        "steps": [
            ("Fix the share under arms",
             "Write it as a fraction of the whole people: `1/5` for the Greek states, "
             "`1/100` for Smith's modern Europe. A fraction keeps the arithmetic exact."),
            ("Multiply for the soldiers",
             "The number under arms is the population times the share, so a million "
             "people at `1/100` is 10,000 men."),
            ("Price them",
             "Multiply the soldiers by what one costs in a year. Smith gives no such "
             "figure for the army, so this number is always the reader's own."),
            ("Spread it over the people",
             "Divide the yearly cost by the population to see what each head pays. "
             "That is the sum the next chapter will have to find."),
        ],
        "worked": {
            "title": "A million people at one in a hundred",
            "intro": [
                "Take the modern preset: 1,000,000 people, a hundredth under arms, and "
                "£20 a year for one soldier (a figure written for this lesson).",
            ],
            "lines": [
                "soldiers:  1,000,000 × 1/100 = 10,000",
                "yearly cost:  10,000 × 20 = £200,000",
                "per head:  200,000 / 1,000,000 = £1/5",
            ],
            "after": [
                "A fifth of a pound is four shillings each. The overreach preset at one "
                "in twenty puts 50,000 men under arms and raises the bill to £1,000,000, "
                "or £1 a head: five times the cost, which is Smith's point that the share "
                "cannot be raised at will, because the rest must pay.",
            ],
        },
        "quiz_title": "Who pays for the soldier",
        "quiz": [
            {"q": "On Smith's account of shepherd nations such as the Tartars, why does the "
                  "chief spend nothing preparing a man for war and nothing keeping him in the field?",
             "a": ["The herds and flocks travel with the army and feed it, and the pastimes of shepherd life already exercise him",
                   "The chief pays each man a wage in kind after every campaign",
                   "Shepherd nations have no chief or sovereign to pay anyone",
                   "Their campaigns last only between seedtime and harvest"],
             "c": 0,
             "why": "Smith says the Tartar &ldquo;is maintained by his own herds and flocks, "
                    "which he carries with him&rdquo;, and that the ordinary "
                    "life of a Tartar or Arab &ldquo;prepares him sufficiently for war&rdquo;. He "
                    "states that those nations &ldquo;have all chiefs or sovereigns&rdquo;. "
                    "The seedtime-to-harvest limit belongs to the husbandmen, and the "
                    "plunder is the only pay, not a wage."},
            {"q": "Which two causes does Smith give for the public having to maintain "
                  "the soldier in a more advanced society?",
             "a": ["Growing population and the pressure on land",
                   "The fall in the rate of interest and the rise in rents",
                   "The progress of manufactures and the improvement in the art of war",
                   "The invention of paper money and the growth of banks"],
             "c": 2,
             "why": "Smith writes that &ldquo;two different causes contribute to render it "
                    "altogether impossible that they who take the field should maintain "
                    "themselves at their own expense. Those two causes are, the progress of "
                    "manufactures, and the improvement in the art of war.&rdquo; The other "
                    "pairs are not in Part I."},
            {"q": "A country of 2,400,000 people keeps one in a hundred under arms, at a "
                  "yearly cost of £15 a soldier (a figure written for this question). "
                  "What does the army cost in a year?",
             "a": ["£36,000", "£3,600,000", "£360,000", "£24,000"],
             "c": 2,
             "why": "The soldiers are `2,400,000 × 1/100 = 24,000`, and `24,000 × 15 = "
                    "360,000`, so £360,000. £36,000 would be one in a thousand. £3,600,000 "
                    "would be one in ten, and £24,000 is the number of men, not the cost."},
            {"q": "On Smith's account, what is the essential difference between a militia "
                  "and a standing army?",
             "a": ["Whether the troops carry firearms",
                   "Whether soldiering is the soldier's principal occupation and the state's pay his principal subsistence",
                   "Whether the troops are citizens or foreigners",
                   "Whether the force fights at home or abroad"],
             "c": 1,
             "why": "Smith says the practice of arms is &ldquo;the sole or principal "
                    "occupation&rdquo; of a standing army's soldiers, whose pay is &ldquo;the "
                    "principal and ordinary fund of their subsistence&rdquo;, and only an "
                    "occasional one for a militia's. Armies of both kinds can be citizens, "
                    "can have firearms and can fight abroad."},
        ],
        "mistakes": [
            ("Reading one in a hundred as a law",
             "Smith writes that it is &ldquo;commonly computed&rdquo;, as a remark about the "
             "Europe of his time, and sets it beside the fourth or fifth of the ancient "
             "agrarian states. It is the largest share the rest of the people can "
             "feed, and the lab treats it as a figure to compute with, not a measured "
             "limit of any economy, then or now."),
            ("Thinking a militia is weak because its soldiers are amateurs",
             "Smith's claim is narrower: a militia exercised once a week cannot match men "
             "exercised daily, but a militia kept in the field for several campaigns "
             "&ldquo;becomes in every respect a standing army&rdquo;. He ranks the Tartar "
             "militia, which goes to war under the chiefs it obeys in peace, as the best of all."),
            ("Taking Smith's hunters and shepherds for field reports",
             "His account of North American hunters and Asian shepherds is second-hand and "
             "serves the stages of his argument, from hunting to pasture, to farming and "
             "to manufactures. Read the stages as his model of how the cost of defence "
             "rises, and not as ethnography."),
        ],
        "standard": (
            "Finish when you can say why the soldier's cost passes to the public, and compute it.",
            "Given a population, a share under arms and a yearly cost for one soldier, "
            "compute the number of soldiers, the yearly cost and the cost per head, and "
            "state the two causes Smith gives for the public having to maintain the army."
        ),
        "note": (
            "The lab multiplies a population by a fraction and by a cost. It cannot tell "
            "you whether one in a hundred was ever the right share, what a soldier cost in "
            "1776, or whether a militia would have served Britain better than a standing "
            "army: Ferguson and Smith disagreed on the last, and the answer depends on a "
            "constitution and not on a sum. The populations and the £20 a soldier are written "
            "for the lesson. Only the fractions are Smith's."
        ),
    },
    # ---------------------------------------------------------------- 02
    # PSU text l. 23097-23523 (Part II). Property and government l. 23102-23140
    # and l. 23245-23258; four causes l. 23142-23244; justice as revenue
    # l. 23259-23290 and l. 23327-23372; Toulouse l. 23377-23384; fees of court
    # l. 23353-23376; separation of powers l. 23480-23523.
    {
        "slug": "the-expense-of-justice",
        "title": "The Expense of Justice",
        "module": "Book V, Chapter 1, Part 2 · Of the Expense of Justice",
        "one_line": "Government grows with property, and the courts, which first earned the sovereign money, should be paid for by those who use them and kept apart from the executive.",
        "summary": (
            "The second duty is protecting each member of society from the injustice of "
            "every other, and Smith finds that its cost depends on property. He traces "
            "four sources of authority, shows how justice was once a revenue to the "
            "sovereign, and argues for fees of court paid to the judges only when a case "
            "is decided, with the judicial power kept apart from the executive. Compare "
            "what a judge earns from his salary and from his fees."
        ),
        "key": [
            "no property, little government",
            "rank: gifts, age, fortune and birth",
            "justice once earned the sovereign money",
            "fees paid when the case is decided",
            "judges kept apart from the executive",
        ],
        "key_label": "Justice in five lines",
        "concepts_intro": (
            "Part II has two arguments in one. The first is a theory of why government "
            "exists and what holds up rank, and the second is a question about how to "
            "pay judges."
        ),
        "concepts": [
            ("Property brings government",
             "Hunters, who own at most two or three days' labour, need no magistrate. "
             "Great property means great inequality, and the owner can sleep a night in "
             "peace only under the civil magistrate. Smith's sentence about this is among "
             "the book's best-known: government is, in the end, there to protect those who "
             "have something against those who have nothing."),
            ("Four causes of subordination",
             "Before any law, men are ranked by personal qualities, by age, by fortune and "
             "by birth. Smith ranks them: qualities are invisible and disputed, age plain, "
             "and fortune and birth are the two great sources of distinction. Authority is "
             "greatest among shepherds, where a chief with a thousand dependants is both "
             "their general and their judge."),
            ("Paying the judge",
             "Justice began as a revenue: litigants brought presents and the guilty paid "
             "amercements. Corruption followed, and when the sovereign no longer needed it "
             "the judges got salaries. Smith does not think salaries the answer. He prefers "
             "fees paid in one lump to a cashier and shared among the judges only after the "
             "case, so that the pay follows the work without any judge being bribed."),
        ],
        "read_title": "The passage first, then Part II line by line",
        "read_intro": (
            "Part II is about four hundred lines. The first two thirds are the theory of "
            "authority and the history of the courts as a revenue, and the last third "
            "is the proposal for fees and the argument for separating the judge from the "
            "executive."
        ),
        "body": [
            ("p", "<strong>Book V, Chapter 1, Part 2.</strong> &ldquo;Where there is no "
                  "property, or at least none that exceeds the value of two or three days "
                  "labour, civil government is not so necessary.&rdquo; A hunter can only "
                  "wrong another in his person or his name, and the wrong brings the "
                  "wrongdoer no gain. Smith puts the difference with property carefully: "
                  "&ldquo;The benefit of the person who does the injury is often equal to the "
                  "loss of him who suffers it.&rdquo; Envy and malice come only "
                  "occasionally; &ldquo;avarice and ambition in the rich, in the poor the hatred "
                  "of labour and the love of present ease and enjoyment&rdquo; never rest."),
            ("p", "Everyone locks a door at night for the same reason. Smith's rich man "
                  "&ldquo;is at all times surrounded by unknown enemies, whom, though he never "
                  "provoked, he can never appease&rdquo;, and so he needs the magistrate. The "
                  "most quoted sentence of the Part follows from this: &ldquo;Civil "
                  "government, so far as it is instituted for the security of property, is, "
                  "in reality, instituted for the defence of the rich against the poor, or of "
                  "those who have some property against those who have none at all.&rdquo; "
                  "Smith states it as the consequence of a stage of society and does not "
                  "reason it into a defence or an attack. The reader can judge how much "
                  "weight to put on it."),
            ("p", "Before rank is settled by law, he says, four circumstances sort men. "
                  "Personal qualifications come first and give the least: they are "
                  "&ldquo;invisible qualities; always disputable, and generally "
                  "disputed&rdquo;. Age is better, because &ldquo;Age is a plain and "
                  "palpable quality, which admits of no dispute.&rdquo; Fortune is greater "
                  "still, and Smith's example is the pastoral chief: &ldquo;A Tartar chief, "
                  "the increase of whose flocks and herds is sufficient to maintain a "
                  "thousand men&rdquo;, cannot use it in any other way than to maintain a "
                  "thousand men, who obey him in war and submit to his judgment in peace. "
                  "In a rich society it is different: a man &ldquo;may possess a much "
                  "greater fortune, and yet not be able to command a dozen of people&rdquo;, "
                  "because everyone pays for what he gets. Birth is fortune's inheritance: "
                  "it &ldquo;supposes an ancient superiority of fortune in the family&rdquo;."),
            ("p", "The next stretch is history, and it is the part of Part II that bears on "
                  "money. &ldquo;The judicial authority of such a sovereign, however, far "
                  "from being a cause of expense, was, for a long time, a source of revenue "
                  "to him.&rdquo; Suitors brought presents, the guilty paid an amercement "
                  "for breaking the king's peace, and Henry II's circuit judges were "
                  "&ldquo;a sort of itinerant factors&rdquo; sent to levy the king's revenue. "
                  "Smith sees the flaw at once: &ldquo;The person who applied for justice with "
                  "a large present in his hand, was likely to get something more than "
                  "justice; while he who applied for it with a small one was likely to get "
                  "something less.&rdquo;"),
            ("def", ("Fees of court (epices)",
                     "A payment made by the parties to a case for the court's work, in "
                     "Smith's scheme fixed by law, paid at once into the hands of a "
                     "cashier, and divided among the judges only after the case is "
                     "decided. The French parliaments called theirs &ldquo;epices and "
                     "vacations&rdquo;.")),
            ("p", "When the sovereign needed taxes for defence, he gave up the "
                  "presents and paid judges salaries, and &ldquo;Justice was then said to be "
                  "administered gratis.&rdquo; Smith's reply is dry: &ldquo;Justice, however, "
                  "never was in reality administered gratis in any country.&rdquo; Lawyers and "
                  "attorneys are paid by the parties, and their fees are a much greater sum "
                  "than the judges' salaries. The salaries, he says, prevented corruption "
                  "but did not make the case cost less. The whole expense of justice, he says, is only a very "
                  "small part of the whole expense of government, and it &ldquo;might easily be "
                  "defrayed by the fees of court&rdquo;."),
            ("p", "His design has three safeguards. The fees are regulated by law, paid "
                  "all at once at a stated stage into a cashier's hands, and handed to the "
                  "judges only after the case is decided, so no suitor can buy a "
                  "judge. And the judges' shares could track the hours each has given, so "
                  "that, in his words, &ldquo;Public services are never better performed, than "
                  "when their reward comes only in consequence of their being performed, and "
                  "is proportioned to the diligence employed in performing them.&rdquo;"),
            ("p", "He gives a real example, the only figure in this Part. A counsellor "
                  "in the parliament of Toulouse, one of the French provincial courts, "
                  "had a salary that, after deductions, &ldquo;amounts only to 150 livres, "
                  "about £6:11s. sterling a-year&rdquo;, which seven years before was the wage "
                  "of a common footman in the same town. A word on the money, which this "
                  "course will use throughout: there are twelve pence to a shilling and "
                  "twenty shillings to a pound, so £6 11s is `131/20` of a pound, or £6.55. "
                  "Smith adds that the epices were shared by diligence: &ldquo;A diligent "
                  "judge gains a comfortable, though moderate revenue, by his office; an "
                  "idle one gets little more than his salary.&rdquo; He gives no figure "
                  "for the epices themselves."),
            ("p", "The lab shows the arithmetic with exactly that structure and a made-up "
                  "caseload. In the toulouse preset two counsellors have Smith's salary of "
                  "£6.55 and differ only in how many causes they decide, at a fee of ten "
                  "shillings each, both numbers written for the lesson: a diligent "
                  "one deciding 120 causes earns £60 in fees and £66.55 in all, an idle one "
                  "deciding 8 earns £4 in fees and £10.55. In the salary-only preset three "
                  "judges earn the same £6.55 whatever they decide, so one more case "
                  "adds nothing to any of them. In the fees-only preset two judges have no "
                  "salary and get £60 and £4, all of it from fees, so that each is "
                  "100 per cent. dependent on the cases. The tiles show each person's income, the share from "
                  "fees, and the gain from one more case, which is simply the fee."),
            ("p", "Smith's proposal has opponents. Fees paid by the litigants put a price on "
                  "the very thing the state is there to give, and the price falls most "
                  "heavily on those least able to pay; Smith's own list of abuses, "
                  "from presents to the multiplying of words by clerks paid by the page, "
                  "shows how fees invite delay and swelling. Jeremy Bentham, in his "
                  "<em>Protest against Law Taxes</em> of the 1790s, argued that charges on "
                  "going to law fall hardest on the poor and can shut them out of justice."
                  " Smith's defence is "
                  "in the Conclusion, where he says fees may be paid by those who give "
                  "occasion to the expense, by their injustice, or by those it restores to "
                  "their rights, and that only criminals without means need the general "
                  "revenue."),
            ("p", "The last argument is the most lasting: &ldquo;When the judicial is united "
                  "to the executive power, it is scarce possible that justice should not "
                  "frequently be sacrificed to what is vulgarly called politics.&rdquo; "
                  "Smith says the separation arose from business: the consul had no time "
                  "and appointed a praetor. For liberty it is not enough, he says, that the "
                  "judicial be separated; it must be &ldquo;rendered as much as possible "
                  "independent of that power&rdquo;, and &ldquo;The regular payment of his "
                  "salary should not depend upon the good will, or even upon the good "
                  "economy of that power.&rdquo; Smith's own example suggests a fund of "
                  "its own, such as the rent of lands or the interest of a sum, though he "
                  "doubts the interest, which is liable to change."),
            ("p", "Part II ends the second duty. The third, public works and institutions, "
                  "begins with the roads that earn their own keep: the next lesson, "
                  "<em>Public Works and Tolls</em>, takes up the toll and the weight of "
                  "a carriage."),
        ],
        "lab": ("wonkit", {
            "mode": "public",
            "view": "fees",
            "money_unit": "£",
            "pupil_word": "cases",
            "preset": "toulouse",
            "presets": [
                {"id": "toulouse",
                 "label": "Two counsellors of Toulouse on Smith's £6.55 salary (causes decided and the fee written for this lesson)",
                 "people": "diligent-counsellor, 6.55, 120, 1/2; idle-counsellor, 6.55, 8, 1/2",
                 "expect": {
                    "wpbFees": "diligent-counsellor £60; idle-counsellor £4",
                    "wpbIncome": "diligent-counsellor £66.55; idle-counsellor £10.55",
                    "wpbShare": "diligent-counsellor ≈ 90.16%; idle-counsellor ≈ 37.91%",
                    "wpbMore": "diligent-counsellor +£0.5; idle-counsellor +£0.5",
                    "wpbMost": "diligent-counsellor (≈ 90.16% from fees)",
                }},
                {"id": "salary-only",
                 "label": "Three judges on salary alone (written for this lesson)",
                 "people": "judge-a, 6.55, 0, 0; judge-b, 6.55, 0, 0; judge-c, 6.55, 0, 0",
                 "expect": {
                    "wpbFees": "judge-a £0; judge-b £0; judge-c £0",
                    "wpbIncome": "judge-a £6.55; judge-b £6.55; judge-c £6.55",
                    "wpbShare": "judge-a 0%; judge-b 0%; judge-c 0%",
                    "wpbMore": "judge-a £0; judge-b £0; judge-c £0",
                    "wpbMost": "judge-a, judge-b, judge-c (0% from fees)",
                }},
                {"id": "fees-only",
                 "label": "Two judges paid by fees alone (written for this lesson)",
                 "people": "judge-a, 0, 120, 1/2; judge-b, 0, 8, 1/2",
                 "expect": {
                    "wpbFees": "judge-a £60; judge-b £4",
                    "wpbIncome": "judge-a £60; judge-b £4",
                    "wpbShare": "judge-a 100%; judge-b 100%",
                    "wpbMore": "judge-a +£0.5; judge-b +£0.5",
                    "wpbMost": "judge-a, judge-b (100% from fees)",
                }},
            ],
            "panel_title": "What a judge earns, from salary and from fees",
            "panel_intro": (
                "Each row is one person: a salary, a number of cases decided and a fee "
                "for each. The lab adds the two kinds of income and shows how much depends "
                "on doing the work. Start with the toulouse preset, whose salary is "
                "Smith's, then try the salary-only one."
            ),
        }),
        "steps_title": "Splitting a judge's income",
        "steps_intro": "Four steps, for any person paid partly by salary and partly by fees.",
        "steps": [
            ("Read the salary",
             "The fixed part, which does not change with the work. Smith's Toulouse "
             "figure is 150 livres, £6 11s, or £6.55."),
            ("Multiply cases by the fee",
             "Fees are the number of cases decided times the fee on each. This is "
             "the part that follows the work."),
            ("Add and take the share",
             "Total income is salary plus fees, and the share from fees is fees "
             "divided by total. A judge whose share is near zero lives on the "
             "salary, whatever he does."),
            ("Find what one more case adds",
             "One more case adds one fee. On salary alone it adds nothing, and that "
             "is the point at issue between Smith and the salaried judge."),
        ],
        "worked": {
            "title": "A diligent and an idle counsellor",
            "intro": [
                "Take the toulouse preset: each has Smith's £6.55 salary; the diligent one "
                "decides 120 causes at ten shillings each, the idle one 8 (numbers written "
                "for this lesson).",
            ],
            "lines": [
                "diligent fees:  120 × 1/2 = £60",
                "diligent income:  6.55 + 60 = £66.55",
                "idle fees:  8 × 1/2 = £4,  income 6.55 + 4 = £10.55",
                "share from fees:  60 / 66.55 and 4 / 10.55",
            ],
            "after": [
                "The diligent counsellor draws about nine tenths of his income from fees "
                "and the idle one nearly two fifths, which is Smith's &ldquo;comfortable, "
                "though moderate revenue&rdquo; against &ldquo;little more than his "
                "salary&rdquo;. The salary is Smith's, and the caseload and the fee are not.",
            ],
        },
        "quiz_title": "Who pays, and when",
        "quiz": [
            {"q": "Why does Smith say that civil government grows up with the acquisition of "
                  "valuable property?",
             "a": ["Property makes men more virtuous and so easier to govern",
                   "A man with great property is exposed to the avarice and envy of those "
                   "who have none, and can sleep securely only under a magistrate",
                   "Landowners are the only people who can raise an army",
                   "Property needs courts because contracts cannot otherwise be written"],
             "c": 1,
             "why": "Smith writes that the owner of valuable property &ldquo;can sleep a single "
                    "night in security&rdquo; only under the civil magistrate, since he is "
                    "&ldquo;at all times surrounded by unknown enemies&rdquo;. He does not say "
                    "property makes men virtuous, and the courts' work is protection, not "
                    "contracts. Armies come in Part I."},
            {"q": "Which of Smith's four causes of subordination does he say is greatest among "
                  "nations of shepherds?",
             "a": ["Superiority of age", "Superiority of personal qualifications",
                   "Superiority of fortune, with birth following it",
                   "Superiority of learning"],
             "c": 2,
             "why": "&ldquo;There is no period&rdquo;, he says, &ldquo;in which the "
                    "superiority of fortune gives so great authority to those who possess "
                    "it&rdquo;, and birth &ldquo;always does&rdquo; take place among them. Age "
                    "is the sole foundation of rank among hunters, and learning is not "
                    "among the four."},
            {"q": "A judge has a salary of £6.55 and decides 50 causes at a fee of ten shillings "
                  "each (figures written for this question). What is his income, and what share "
                  "of it comes from fees?",
             "a": ["£31.55, about four fifths from fees", "£56.55, about nine tenths from fees",
                   "£31.55, about one fifth from fees", "£25 in all, all from fees"],
             "c": 0,
             "why": "Fees are `50 × 1/2 = 25` pounds, so income is `6.55 + 25 = 31.55`, and "
                    "the share from fees is `25/31.55`, about 79 per cent, four fifths. "
                    "£56.55 would be 100 causes. One fifth is the salary's share, and "
                    "£25 leaves out the salary."},
            {"q": "Why does Smith want the fees paid at one stated stage into a cashier's "
                  "hands and shared among the judges only after the case is decided?",
             "a": ["It makes the judges' pay depend on how the case comes out",
                   "It lets the sovereign take his share of the fees",
                   "It keeps the reward tied to diligence without letting a suitor buy a judge",
                   "It makes justice free to the parties"],
             "c": 2,
             "why": "Smith says fees so paid carry &ldquo;no more danger of corruption than "
                    "when such fees are prohibited altogether&rdquo; and still give "
                    "&ldquo;some incitement to the diligence of the court&rdquo;. Pay is not "
                    "tied to the verdict, only to the case being decided. He opposes the "
                    "sovereign sharing in them, and says justice is never free."},
        ],
        "mistakes": [
            ("Reading the sentence about the rich and the poor as the whole of Smith's view of government",
             "It is his account of what government does for the owners of property, "
             "inside a history of stages. The same Part asks for judges independent of "
             "the executive and paid so that the poor suitor is not served worse than "
             "the rich one. Quote the sentence and also what follows it."),
            ("Believing that salaries made justice free",
             "Smith's point is that &ldquo;Justice, however, never was in reality "
             "administered gratis&rdquo;. The salaries only moved the payment to lawyers and "
             "attorneys, whose fees are much larger, and were meant to prevent corruption, "
             "not to cut the cost."),
            ("Treating the epices as the same as the old presents",
             "The old presents were paid to a judge before the case, in amounts he "
             "could raise by hints. Smith's fees are fixed by law, lodged with a cashier "
             "and divided only after judgment. The point of the design is that the "
             "judge's reward follows the work and the suitor's offer cannot move it."),
        ],
        "standard": (
            "Finish when you can compute a judge's two incomes and say what Smith wants of the courts.",
            "Given a salary, a number of cases and a fee, compute income from each, the "
            "share from fees and the gain from one more case, and state Smith's three "
            "provisions for fees of court and his argument for separating the judicial "
            "from the executive power."
        ),
        "note": (
            "The lab adds a salary to a number of cases times a fee. It cannot say whether "
            "fees make a judge diligent, or whether the diligence they buy is the kind a "
            "litigant wants, and it cannot weigh Bentham's objection that a price on "
            "justice shuts out the poor. Only the Toulouse salary is Smith's; he gives no "
            "figure for the epices, and the caseloads and fees are written for the lesson."
        ),
    },
    # ---------------------------------------------------------------- 03
    # PSU text l. 23524-23824 (Part III, Article I, first section). Opening
    # l. 23524-23547; tolls l. 23560-23597; Languedoc l. 23610-23625; turnpikes
    # l. 23634-23720; France and China l. 23722-23800; local works l. 23801-23815.
    {
        "slug": "public-works-and-tolls",
        "title": "Public Works and Tolls",
        "module": "Book V, Chapter 1, Part 3, Article 1 · Of the Public Works Which Facilitate Commerce",
        "one_line": "A road, a bridge or a canal can be paid for by a toll in proportion to the weight carried, and Smith thinks it should be: the user pays, and still gains.",
        "summary": (
            "The third duty is the works that no one could profitably build for himself. "
            "Smith holds that roads, bridges, canals and harbours can usually pay their own "
            "way through tolls in proportion to weight, argues that the consumer who pays "
            "them gains more than he loses, and objects to turning the tolls into a "
            "general revenue. Compute who pays a toll and how much."
        ),
        "key": [
            "a toll in proportion to weight",
            "each carriage pays for the wear it makes",
            "the consumer pays, and gains by the road",
            "a toll on weight falls on coarse, bulky goods",
            "local works, local revenue",
        ],
        "key_label": "Tolls in five lines",
        "concepts_intro": (
            "This first section of the third duty is about one idea, that a public work "
            "can be charged to its users, and three objections to getting it wrong."
        ),
        "concepts": [
            ("The works that pay for themselves",
             "The third duty covers works so useful that no individual could be repaid for "
             "building them. Smith adds that the greater part of the ones that help "
             "commerce can be built and kept up by a small toll on the carriages that use "
             "them, a port duty on the shipping, or the seignorage on coin, and he says "
             "that works built this way can be made only where the commerce needs them."),
            ("A toll by weight",
             "A carriage that pays in proportion to its weight pays in proportion to the "
             "wear it causes. The toll is advanced by the carrier and paid in the end by "
             "the consumer, but the road lowers the price of carriage by more than the toll "
             "raises it, so the consumer gains. Smith adds a tilt: tax coaches somewhat "
             "higher than carts, and the vanity of the rich relieves the poor."),
            ("Why not make it a general revenue",
             "Some ministers saw the turnpike tolls as a source of half a million for "
             "the state. Smith has three objections: the tolls would be raised until they "
             "choked inland trade; a toll by weight falls on coarse and bulky goods, so "
             "the poor would pay; and a government with the money would care less about "
             "the road."),
        ],
        "read_title": "The passage first, then the section line by line",
        "read_intro": (
            "This section runs to about three hundred lines. The lesson takes the "
            "principle, then the objections, then the comparison with France and China, "
            "and leaves out the second half of the Article, on works for particular trades, "
            "which is the next lesson."
        ),
        "body": [
            ("p", "<strong>Book V, Chapter 1, Part 3, Article 1.</strong> The third duty is "
                  "to erect and maintain works &ldquo;which though they may be in the highest "
                  "degree advantageous to a great society, are, however, of such a nature, "
                  "that the profit could never repay the expense to any individual, or small "
                  "number of individuals&rdquo;. Smith then names the two kinds that concern "
                  "trade and instruction, and the Article opens with trade. &ldquo;The expense "
                  "of making and maintaining the public roads of any country must evidently "
                  "increase with the annual produce of the land and labour of that country.&rdquo;"),
            ("p", "His first suggestion is that most such works need not touch the "
                  "general revenue: a highway, bridge or canal &ldquo;may, in most cases, "
                  "be both made&rdquo; and kept by &ldquo;a small toll upon the carriages "
                  "which make use of them&rdquo;. Compare a toll bridge that charges "
                  "whoever crosses with a bridge paid out of everyone's rates, and notice "
                  "that the toll bridge has a built-in test of whether anyone wants it."),
            ("p", "Then the argument for weight. When carriages pay &ldquo;in proportion to "
                  "their weight or their tonnage, they pay for the maintenance of those public "
                  "works exactly in proportion to the wear and tear which they occasion of "
                  "them&rdquo;. His conclusion is flat: &ldquo;It seems scarce possible to "
                  "invent a more equitable way of maintaining such works.&rdquo; The toll "
                  "ends up on the consumer, who has paid it in the price of the goods; and "
                  "since carriage is cheaper, &ldquo;The person who finally pays this tax, "
                  "therefore, gains by the application more than he loses by the payment of "
                  "it.&rdquo;"),
            ("p", "Here is the turnpike preset, written for this lesson. A waggon of three tons "
                  "makes 100 trips a year over a turnpike at a toll of a shilling a ton a "
                  "trip, which is `1/20` of a pound. It pays `3 × 100 × 1/20` pounds, which "
                  "is £15. A coach of one ton making 200 trips pays £10. The heavier "
                  "vehicle pays per ton exactly as the lighter does, and that is what "
                  "&ldquo;equitable&rdquo; means to Smith: each pays for what it wears. "
                  "The waggon carries 300 ton-trips and the coach 200, so the waggon "
                  "pays three fifths of the road's tolls and the coach two fifths, in "
                  "proportion to tons carried and not to the number of vehicles. The "
                  "total is £25 on 500 tons, which is £0.05 a ton, the toll itself: that "
                  "is what a toll by weight means. In the doubled preset the toll is "
                  "`1/10` and the same traffic pays £20 and £30, £50 in all, and the "
                  "waggon's share stays at 60 per cent."),
            ("p", "The heavy-trade preset, also written for the lesson, shows the second "
                  "of Smith's objections at work. A coach on 100 trips pays £5, a waggon "
                  "of three tons on 100 trips pays £15, and a coal-cart of two tons on 400 "
                  "trips pays £40, £60 in all on 1,200 tons carried. The lab's "
                  "heaviest-carriage tile names the waggon, at 25 per cent. of the "
                  "total, but the coal-cart pays two thirds of it. A toll by weight bears "
                  "on whoever moves the most tons, and what moves the most tons is coarse, "
                  "bulky stuff."),
            ("def", ("Toll",
                     "A payment for using a road, bridge or canal, charged by the weight or "
                     "tonnage of the carriage, advanced by the carrier, and, Smith argues, "
                     "paid in the end by the consumer in the price of what is carried.")),
            ("p", "Smith adds his tilt: when the toll on carriages of luxury, &ldquo;upon "
                  "coaches, post-chaises, etc.&rdquo; is made somewhat higher in proportion "
                  "to their weight than on carts and waggons, &ldquo;the indolence and "
                  "vanity of the rich is made to contribute, in a very easy manner, to the "
                  "relief of the poor&rdquo;. The lab charges one toll per ton, so it "
                  "cannot show this tilt, and the lesson says so; a reader can try two "
                  "tolls in two presets."),
            ("p", "He also says who should hold the tolls. A canal's tolls can be a private "
                  "property: the canal of Languedoc cost &ldquo;upwards of thirteen millions "
                  "of livres&rdquo; and then the tolls were given to its engineer, Riquet, "
                  "whose family had &ldquo;a great interest to keep the work in constant "
                  "repair&rdquo;. A canal that decays stops carrying anything, so the owner's "
                  "interest is plain. A road, though, &ldquo;though entirely neglected, does "
                  "not become altogether impassable, though a canal does&rdquo;, so a road's "
                  "tolls belong with trustees. He grants that British turnpike trustees had "
                  "committed &ldquo;abuses&rdquo;, and calls the system new."),
            ("p", "Then he takes up a proposal in the air. Ministers had thought that "
                  "government, working the turnpikes itself and using soldiers for labour, "
                  "could gain &ldquo;half a million, perhaps&rdquo;; in a note added after "
                  "the first two editions, he writes that he has &ldquo;good reasons to believe "
                  "that all the turnpike tolls levied in Great Britain do not produce a neat "
                  "revenue that amounts to half a million&rdquo;. His three objections "
                  "follow. First, a revenue is something to raise, and the tolls would "
                  "go up with the state's needs until inland trade was choked. Second, "
                  "&ldquo;as the turnpike toll raises the price of goods in proportion to their "
                  "weight and not to their value&rdquo;, spent on anything but the road it "
                  "falls &ldquo;at the expense of the poor, not of the rich&rdquo;. Third, a "
                  "government rich enough from tolls would find it harder to be made to "
                  "repair the road."),
            ("p", "Two later criticisms of the toll bear on the first section. Jules Dupuit, "
                  "the French engineer who wrote in the 1840s, pointed out that a toll "
                  "keeps off people who would gain from the bridge by less than the toll, "
                  "though the bridge costs almost nothing extra for them to cross. Road "
                  "engineers in the twentieth century found that damage to a pavement rises "
                  "much faster than weight, roughly with the fourth power of the load on an "
                  "axle, so that a toll in proportion to weight undercharges the heaviest "
                  "axle loads. Smith's reply is not in the chapter. A reader can note that his "
                  "argument is about who ought to pay, and that the wear is a physical fact "
                  "he took as proportional."),
            ("p", "His comparison with France is about who holds the money. In France the "
                  "highway funds were under the intendant, and the great post-roads between "
                  "the principal towns were in good order while &ldquo;the far greater part of "
                  "the roads in the country&rdquo;, the cross roads, were neglected, for a "
                  "minister takes pleasure in &ldquo;a work of splendour and magnificence&rdquo; "
                  "that the nobility will see. He also thinks the corvée, the forced days of "
                  "labour on the roads, an instrument of tyranny in the intendant's hands. "
                  "China, where he suspects the accounts were drawn up by &ldquo;weak and "
                  "wondering travellers&rdquo;, is a case where he grants that the sovereign has "
                  "a direct interest, since &ldquo;the revenue of the sovereign arises almost "
                  "altogether from a land tax or land rent, which rises or falls with the rise "
                  "and fall of the annual produce of the land&rdquo;; in Europe that link is "
                  "weaker."),
            ("p", "He ends the section with local works. Lighting and paving London from the "
                  "treasury would not go as well as it does now, and the cost would fall on "
                  "everyone, &ldquo;of whom the greater part derive no sort of benefit&rdquo; "
                  "from it. The principle is the same as the toll's: let those who benefit "
                  "pay, and let the money be managed near them. The Conclusion of the chapter "
                  "will say it as a general rule."),
            ("p", "Roads and canals are the works that help trade in general. The next "
                  "lesson, <em>Regulated and Joint-Stock Companies</em>, takes the "
                  "works that help particular trades, and the companies that tried to "
                  "build the forts."),
        ],
        "lab": ("wonkit", {
            "mode": "public",
            "view": "tolls",
            "money_unit": "£",
            "preset": "turnpike",
            "presets": [
                {"id": "turnpike",
                 "label": "A coach and a waggon at a shilling a ton a trip (all figures written for this lesson)",
                 "toll": "1/20",
                 "carriages": "coach, 1, 200; waggon, 3, 100",
                 "expect": {
                    "wpbTolls": "coach £10; waggon £15",
                    "wpbTotal": "£25 a year",
                    "wpbHeaviest": "waggon £15 (60% of the total)",
                    "wpbTons": "500 tons",
                    "wpbPerTon": "£0.05 a ton",
                }},
                {"id": "doubled",
                 "label": "The same traffic with the toll doubled, as Smith's ministers might have done (written for this lesson)",
                 "toll": "1/10",
                 "carriages": "coach, 1, 200; waggon, 3, 100",
                 "expect": {
                    "wpbTolls": "coach £20; waggon £30",
                    "wpbTotal": "£50 a year",
                    "wpbHeaviest": "waggon £30 (60% of the total)",
                    "wpbTons": "500 tons",
                    "wpbPerTon": "£0.1 a ton",
                }},
                {"id": "heavy-trade",
                 "label": "A road carrying mostly coarse goods (written for this lesson)",
                 "toll": "1/20",
                 "carriages": "coach, 1, 100; waggon, 3, 100; coal-cart, 2, 400",
                 "expect": {
                    "wpbTolls": "coach £5; waggon £15; coal-cart £40",
                    "wpbTotal": "£60 a year",
                    "wpbHeaviest": "waggon £15 (25% of the total)",
                    "wpbTons": "1,200 tons",
                    "wpbPerTon": "£0.05 a ton",
                }},
            ],
            "panel_title": "Who pays a toll by weight",
            "panel_intro": (
                "Enter a toll for a ton on one trip and, for each carriage, its weight in "
                "tons and its trips in a year. The lab prices each carriage and the whole "
                "road. Smith's tilt, a higher toll for coaches, is not in the lab; its "
                "figures are all written for this lesson."
            ),
        }),
        "steps_title": "Computing a toll",
        "steps_intro": "Four steps, for any set of carriages.",
        "steps": [
            ("Fix the toll per ton",
             "Choose a toll for one ton on one trip, as a fraction of a pound: a "
             "shilling is `1/20`."),
            ("Price each carriage",
             "Each carriage pays toll times its weight in tons times its trips in the "
             "year, so a three-ton waggon on 100 trips pays `3 × 100 × 1/20`."),
            ("Add up the road",
             "The road's revenue is the sum over every carriage. Per ton it is "
             "always the toll, which is what a toll by weight means."),
            ("Find who bears most",
             "Divide each carriage's toll by the total: whoever moves the most tons "
             "pays the largest share. Smith's second objection is that this falls on bulky goods."),
        ],
        "worked": {
            "title": "A coach and a waggon on the turnpike",
            "intro": [
                "Take the turnpike preset: a coach of one ton on 200 trips and a waggon of "
                "three tons on 100 trips, at `1/20` of a pound a ton a trip. The figures "
                "are written for this lesson.",
            ],
            "lines": [
                "coach:  1 × 200 × 1/20 = £10",
                "waggon:  3 × 100 × 1/20 = £15",
                "road total:  10 + 15 = £25",
                "waggon's share:  15 / 25 = 3/5",
            ],
            "after": [
                "The waggon pays three fifths of a road it wears three fifths of, and "
                "the coach two fifths. Double the toll, as in the doubled preset, and "
                "every figure doubles and no one's share moves. Smith's first objection "
                "is that the revenue would then be raised again and again.",
            ],
        },
        "quiz_title": "Who pays for the road",
        "quiz": [
            {"q": "On Smith's argument, why does the consumer who finally pays a toll still "
                  "gain from the road?",
             "a": ["The government repays the toll out of the general revenue",
                   "The road lowers the cost of carriage by more than the toll raises the price",
                   "The toll is paid only by the carrier and never reaches the consumer",
                   "Roads make land rents rise"],
             "c": 1,
             "why": "The goods &ldquo;come cheaper to the consumer than they could otherwise "
                    "have done, their price not being so much raised by the toll, as it is "
                    "lowered by the cheapness of the carriage&rdquo;. Smith says the toll is "
                    "&ldquo;finally paid by the consumer&rdquo;, so it is not the carrier's "
                    "alone, and no public money repays it."},
            {"q": "A waggon of 4 tons makes 50 trips a year at a toll of a shilling a ton a trip "
                  "(`1/20` of a pound; figures written for this question). What toll does it pay in a year?",
             "a": ["£200", "£20", "£10", "£5"],
             "c": 2,
             "why": "`4 × 50 × 1/20 = 10`, so £10. £200 forgets the shilling is a twentieth "
                    "of a pound, £20 uses a toll of `1/10`, and £5 counts only 25 trips."},
            {"q": "Which of these is one of Smith's objections to using the turnpike tolls as "
                  "a source of general revenue?",
             "a": ["A toll by weight falls mainly on the consumers of coarse and bulky goods, "
                   "so a general revenue raised this way would fall on the poor",
                   "A toll cannot be collected without a new class of officers",
                   "The tolls are too small to be worth collecting",
                   "Roads are better paid for by the owners of the land beside them"],
             "c": 0,
             "why": "Smith writes that such a toll &ldquo;raises the price of goods in "
                    "proportion to their weight and not to their value&rdquo;, and so would "
                    "supply the state &ldquo;at the expense of the poor, not of the rich&rdquo;. "
                    "He says the tolls could be raised &ldquo;without the appointment of a "
                    "single new officer&rdquo;, and his worry is that they would be raised too "
                    "far, not that they are small."},
            {"q": "Why does Smith think a canal's tolls can be left to a private owner, "
                  "while a road's should go to trustees?",
             "a": ["Canals earn more than roads, so private owners are attracted",
                   "A road cannot be owned privately under English law",
                   "Canals are more often built by the state",
                   "A canal that is not kept up stops carrying anything, so the owner must "
                   "repair it, but a neglected road can still be used"],
             "c": 3,
             "why": "&ldquo;A high-road, though entirely neglected, does not become altogether "
                    "impassable, though a canal does.&rdquo; The owner of a canal's tolls "
                    "has a plain interest in repair, and the owner of a road's tolls might "
                    "&ldquo;neglect altogether the repair of the road, and yet continue to "
                    "levy very nearly the same tolls&rdquo;. The other answers are not his reasons."},
        ],
        "mistakes": [
            ("Thinking Smith wants a toll at every public work",
             "He lists the works that can pay their own way (highways, bridges, canals, "
             "harbours, the coinage and the post-office) and then, in the next breath, works "
             "whose benefit is local and which should be paid by a local revenue. "
             "The Conclusion adds that roads benefit the whole society and may "
             "&ldquo;without any injustice&rdquo; be paid from the general contributions, "
             "though the toll is better."),
            ("Taking a toll by weight for a toll by value",
             "A toll by weight charges a ton of coal and a ton of lace alike, so it "
             "bears most heavily on cheap bulk. This is the very reason Smith gives for "
             "not using it as a general revenue. The lab, like his scheme, has one toll "
             "for every ton."),
            ("Assuming the tolls Smith praises were well run",
             "He reports that turnpike tolls in some places were &ldquo;more than double "
             "of what is necessary&rdquo; and the work &ldquo;sometimes not executed at "
             "all&rdquo;. His claim is that the toll is the right principle and that "
             "trustees need courts of inspection and account, which in 1776 had not "
             "yet been set up."),
        ],
        "standard": (
            "Finish when you can compute what each carriage pays and say why Smith calls it equitable.",
            "Given a toll per ton and each carriage's weight and trips, compute each "
            "carriage's toll, the road's total and the heaviest user's share, and state "
            "Smith's three objections to making the tolls a general revenue."
        ),
        "note": (
            "The lab multiplies a toll by tons and trips. It cannot tell you whether a "
            "toll by weight matches the wear on a road, whether a toll keeps off people "
            "whose gain from the road is smaller than the toll, or what any turnpike "
            "trust actually collected: Smith himself changed his sums in a note. Every "
            "figure in the presets is written for the lesson, and the lab cannot show "
            "the higher toll for coaches."
        ),
    },
]
