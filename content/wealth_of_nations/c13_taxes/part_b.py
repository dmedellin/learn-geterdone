"""Taxes and Public Debts, lessons 5-7 -- Book V, Chapter 2, Article 4, and Chapter 3.

Taxes upon consumable commodities, the public debts, and the end of the chapter and of
the book: the debasement of the coin and the empire.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt
(the Electronic Classics Series edition of Smith's text, Pennsylvania State University,
2005); the comment beside each lesson gives its line numbers. Page numbers and running
heads of the extraction are left out of the quotations, and Smith's spelling is kept.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    # PSU text l. 28418-28423 (the two kinds); l. 28425-28442 (capitation);
    # l. 28505-28538 (necessaries and luxuries); l. 28539-28560 (necessaries
    # raise wages); l. 28561-28602 (luxuries); l. 28603-28630 (who pays);
    # l. 28637-28672 (salt, leather, soap, candles, coals); l. 28851-28900
    # (customs and the mercantile system, Swift); l. 28901-28917 (the accounts
    # of the customs, 1755); l. 28934-28960 (excise and customs); l. 29700-29716
    # (France: salt and tobacco); l. 29764-29795 (Britain and France compared).
    {
        "slug": "taxes-upon-consumable-commodities",
        "title": "Taxes upon Consumable Commodities",
        "module": "Book V, Chapter 2, Part 2, Article 4 · Taxes upon Consumable Commodities",
        "one_line": "A tax on the necessaries of life acts like a tax on wages, a tax on luxuries is paid by whoever buys them, and a duty that is too high can bring in less than a lower one.",
        "summary": (
            "The state cannot tax revenue directly without an inquisition, so it taxes what "
            "people spend. Smith separates necessaries from luxuries, follows each tax "
            "to whoever finally pays it, and then looks at the customs, where heavy duties "
            "meant for monopoly produce smuggling. Compute a duty schedule in which doubling "
            "the duty halves the revenue."
        ),
        "key": [
            "revenue = duty × quantity that pays it",
            "a higher duty can bring in less",
            "taxed necessaries: wages rise, others pay",
            "taxed luxuries: the consumer pays",
            "heavy customs duties breed smuggling",
            "necessaries: what decency requires",
        ],
        "key_label": "Taxes on commodities in six lines",
        "concepts_intro": (
            "This is the longest Article, and it is mostly a catalogue of British, French and "
            "Dutch taxes. The lesson reads it for three ideas, and says where it leaves the "
            "catalogue out."
        ),
        "concepts": [
            ("Necessaries and luxuries",
             "By necessaries Smith means not only what life needs but &ldquo;whatever the "
             "custom of the country renders it indecent for creditable people, even of the "
             "lowest order, to be without&rdquo;. A linen shirt, leather shoes in England. "
             "All other things he calls luxuries, &ldquo;without meaning, by this appellation, "
             "to throw the smallest degree of reproach upon the temperate use of them&rdquo;. "
             "Beer, ale and wine are luxuries; tobacco, tea and sugar have become luxuries "
             "of the poor."),
            ("Who finally pays",
             "A tax on necessaries raises the price of what a labourer must buy, so wages rise, "
             "and the consumers of manufactures and the landlords pay, with an overcharge. A "
             "tax on luxuries need not raise wages, and is paid by the consumers of the "
             "taxed goods, out of any of the three sources of revenue."),
            ("Revenue is not the rate",
             "The revenue from a duty is the rate times the quantity that pays it. A heavy "
             "duty can cut the quantity so far, by discouraging consumption and tempting to "
             "smuggling, that revenue falls. Smith borrows Swift's saying that in the "
             "arithmetic of the customs two and two sometimes make only one."),
        ],
        "read_title": "The Article, from capitations to the customs",
        "read_intro": (
            "Smith begins with the poll-tax, which he dismisses, then takes taxes on "
            "commodities, necessaries first, and spends the last third on the customs and "
            "the excise. He ends with a comparison of France and Britain."
        ),
        "body": [
            ("p", "<strong>Book V, Chapter 2, Part II, Article IV.</strong> The taxes meant "
                  "to fall indifferently on every sort of revenue are of two kinds, capitation "
                  "taxes and taxes upon consumable commodities, and they &ldquo;must be paid "
                  "indifferently, from whatever revenue the contributors may possess; from "
                  "the rent of their land, from the profits of their stock, or from the wages "
                  "of their labour&rdquo;."),
            ("p", "The poll-tax dilemma takes one sentence: &ldquo;if it is attempted to "
                  "render them equal, become altogether arbitrary and uncertain; and if it is "
                  "attempted to render them certain and not arbitrary, become altogether "
                  "unequal.&rdquo; A man's fortune varies from day to day and can be guessed "
                  "only by an inquisition. If the tax goes by rank, it is certain, but "
                  "fortunes differ within a rank: the poll-taxes of William III's reign "
                  "rated dukes, earls and esquires by their degree, and some who were "
                  "first assessed by fortune were afterwards put in as gentlemen. Smith says "
                  "of the lower ranks that capitations on them are direct taxes on "
                  "wages, with the inconveniences of those, and they are common "
                  "where the comfort of the poor is little attended to."),
            ("p", "The state cannot tax revenue directly and proportionably, so it taxes "
                  "expense instead, which it supposes will in most cases be nearly in "
                  "proportion to revenue. Hence the commodities, and Smith's two classes. His "
                  "definition of a necessary is the passage to read slowly: not only what "
                  "nature requires but what custom does. &ldquo;The Greeks and Romans lived, I "
                  "suppose, very comfortably, though they had no linen&rdquo;, but a "
                  "creditable day-labourer in his time would be ashamed to be seen without a "
                  "shirt. &ldquo;Custom, in the same manner, has rendered leather shoes a "
                  "necessary of life in England.&rdquo; In Scotland they are a necessary to "
                  "men of the lowest order and not to women, and in France to neither. The "
                  "definition is relative to a society, and Smith knows it."),
            ("p", "A tax on necessaries goes the way of a tax on wages. He says it plainly: "
                  "&ldquo;It is thus that a tax upon the necessaries of life operates exactly in "
                  "the same manner as a direct tax upon the wages of labour.&rdquo; The "
                  "dealer advances the tax and must get it back with a profit, so the price of the "
                  "necessary rises by more than the tax, the labourer's wage rises with it, "
                  "and the last lesson's sum applies. The manufacturer who employs him "
                  "charges the rise to his goods, and the farmer cuts the rent. His "
                  "advice to the middling and superior ranks follows: &ldquo;The middling and "
                  "superior ranks of people, if they understood their own interest, ought "
                  "always to oppose all taxes upon the necessaries of life&rdquo;, since the "
                  "final payment falls on themselves, always with a considerable "
                  "overcharge. The landlord pays twice, as landlord in a smaller rent and as "
                  "rich consumer in dearer goods. The taxes pile up in the price: you pay "
                  "for the tax on your own shoes, and a share of the tax on the shoemaker's "
                  "salt and soap and candles, and on the leather the saltmaker consumes."),
            ("p", "Luxuries are different. &ldquo;Taxes upon luxuries are finally paid by "
                  "the consumers of the commodities taxed, without any retribution.&rdquo; "
                  "Tobacco is a luxury even of the poor and is taxed in England at three times "
                  "its original price, and in France at fifteen times, with no effect on wages. "
                  "A tax of three shillings on the barrel of strong beer has not raised the "
                  "wages of common labour in London, &ldquo;eighteen pence or twenty pence a-day "
                  "before the tax, and they are not more now&rdquo;. Smith then argues that such "
                  "taxes may even do some good, since the sober and industrious poor will "
                  "be forced to be frugal, and the dissolute, who seldom rear numerous "
                  "families, would not much diminish the useful population. That is a moral view, and a "
                  "reader may reasonably find it harsh, or doubt the counting of who is "
                  "sober and who is not, but it is in the chapter, and this lesson "
                  "does not need it for the sums."),
            ("p", "Smith's list of British taxes on necessaries is salt at three shillings and "
                  "fourpence the bushel, about three times its original price; leather "
                  "and soap at three halfpence a pound and candles at a penny, which on the "
                  "original price come to between about eight and twenty-five per cent; and "
                  "coals carried coastways, at three shillings and threepence a ton, "
                  "which is more than sixty per cent of the price at the pit. Such "
                  "taxes, he grants, raise the price of subsistence and so the wages of "
                  "labour, but afford a considerable revenue which might not be easy to get "
                  "otherwise, and there may be good reason to keep them. He sets the "
                  "bounty on exported corn and the high duties on imported corn in the "
                  "other column: the same bad effects as taxes on necessaries, and no revenue."),
            ("p", "Then the customs, which is where the arithmetic is. The mercantile system, "
                  "which Book IV examined, has laid heavy duties on imports to discourage "
                  "them, and the result for the revenue is that they have served only to "
                  "encourage smuggling and have reduced the revenue below what more moderate "
                  "duties would have afforded. &ldquo;The saying of Dr. Swift, that in the "
                  "arithmetic of the customs, two and two, instead of making four, make "
                  "sometimes only one, holds perfectly true with regard to such heavy "
                  "duties.&rdquo; Such duties &ldquo;never could have been imposed, had not the "
                  "mercantile system taught us, in many cases, to employ taxation as an "
                  "instrument, not of revenue, but of monopoly&rdquo;."),
            ("p", "The lab shows the saying as a schedule written for this lesson, in pence "
                  "a pound weight of an imported luxury. In the swift preset a duty of 3d "
                  "sells 120,000 pounds weight, 6d sells 100,000, 9d sells 60,000, 12d "
                  "sells 25,000 and 15d sells 8,000. The revenue is 360,000, 600,000, 540,000, "
                  "300,000 and 120,000 pence: it peaks at 6d, and the 12d duty, double the "
                  "6d, brings in half as much. Between 6d and 9d the revenue falls "
                  "while the duty rises. In the moderate preset the duty is 1d to 4d, "
                  "quantity barely falls, and revenue rises each time, from 100,000 to "
                  "360,000. Where the hump comes is the whole question: economists now "
                  "draw it as the Laffer curve and argue about where on it a given "
                  "economy stands, and the lab cannot say."),
            ("p", "Smith's own figures for the customs are a different kind of arithmetic. In "
                  "the year to 5 January 1755 the gross produce was £5,068,000. Bounties were "
                  "£167,806 and drawbacks £2,156,800, together, he says, £2,324,600, which "
                  "leaves £2,743,400, and the cost of management was £287,900, so the "
                  "neat revenue came to £2,455,500. Management is between five and six per "
                  "cent of the gross and a little over ten per cent of what remained "
                  "after the bounties and drawbacks. The bounties and drawbacks, he adds, "
                  "gave occasion to a smuggling more destructive of the revenue than "
                  "any other: goods shipped out for the drawback and landed again somewhere else."),
            ("p", "The excise is clearer than the customs, which depend on a book of rates "
                  "so full of articles that it is uncertain under which a particular "
                  "good falls, and Smith would confine the customs to a few articles of "
                  "general consumption. In France he describes the farm of salt and tobacco, "
                  "where exorbitant taxes and a farmer's officers sent several hundred people "
                  "to the galleys every year: &ldquo;Those who consider the blood of the people "
                  "as nothing, in comparison with the revenue of the prince, may, perhaps, "
                  "approve of this method of levying taxes.&rdquo; Near the end of the chapter he makes "
                  "with a comparison. Britain levies ten millions on less than eight millions of "
                  "people &ldquo;without its being possible to say that any particular order "
                  "is oppressed&rdquo;, while France, with three times the people and better "
                  "soil, raised under fifteen millions sterling and oppressed its people more. "
                  "The comparison is his, from imperfect accounts. What the lesson leaves "
                  "out is the long review of the other duties of the excise, of malt and "
                  "spirits, and the table of the French revenue."),
            ("p", "A last note on the standard objection. Later economists call taxes on "
                  "consumption regressive, because the poor spend a larger share of what they "
                  "have, and Smith's own sentence about housing gives the ground: &ldquo;The "
                  "necessaries of life occasion the great expense of the poor.&rdquo; His "
                  "answer is the one this lesson has followed: where a necessary is taxed, "
                  "wages rise to keep the labourer whole, so the burden is passed up to "
                  "landlords and consumers. That answer holds only if wages do rise, which "
                  "is the condition the last lesson set, and the lab computes revenue and "
                  "not incidence."),
            ("p", "The next lesson, <em>Public Debts</em>, takes up the state that has run out of "
                  "proper subjects of taxation and borrows."),
        ],
        "lab": ("wonkit", {
            "mode": "tax",
            "view": "arithmetic",
            "money_unit": "d",
            "qty_unit": "lb",
            "preset": "swift",
            "presets": [
                {"id": "swift", "label": "A duty schedule in which smuggling takes over, written for this lesson",
                 "rows": "3, 120000; 6, 100000; 9, 60000; 12, 25000; 15, 8000",
                 "expect": {"wtxRevenues": "3 d: 360,000 d; 6 d: 600,000 d; 9 d: 540,000 d; 12 d: 300,000 d; 15 d: 120,000 d", "wtxBest": "6 d, yielding 600,000 d"}},
                {"id": "moderate", "label": "A moderate schedule with little smuggling, written for this lesson",
                 "rows": "1, 100000; 2, 98000; 3, 95000; 4, 90000",
                 "expect": {"wtxRevenues": "1 d: 100,000 d; 2 d: 196,000 d; 3 d: 285,000 d; 4 d: 360,000 d", "wtxBest": "4 d, yielding 360,000 d", "wtxFalls": "0: none"}},
            ],
            "panel_title": "What a duty brings in at each rate",
            "panel_intro": (
                "Each row is a duty and the quantity that still pays it. The lab gives the "
                "revenue of each, the highest, and the rows where a higher duty brings "
                "in less than a lower one. Run the swift preset first."
            ),
        }),
        "steps_title": "Working out who pays and what a duty yields",
        "steps_intro": "Four steps, for any tax on a commodity.",
        "steps": [
            ("Sort the commodity",
             "Is it a necessary, one that custom makes indecent to be without, or a "
             "luxury? The answer sets whether wages follow the price."),
            ("Follow the price",
             "A dealer advances the tax and charges it back with a profit. For a necessary, "
             "wages rise with the price and the employers pass the rise on. For a luxury "
             "the consumer pays."),
            ("Compute the revenue at each rate",
             "Multiply the duty by the quantity that still pays it. Do this for each "
             "rate you can state a quantity for, and look for the highest."),
            ("Check for the hump",
             "A row where a higher duty yields less than a lower one means the duty is "
             "past the peak. That is Swift's saying: past the peak a duty costs "
             "the treasury revenue and the traders their trade."),
        ],
        "worked": {
            "title": "A duty past its peak, and a year's customs",
            "intro": [
                "Take the swift schedule, and then Smith's accounts of the customs for the "
                "year to January 1755.",
            ],
            "lines": [
                "duty 6d:  6 · 100,000 = 600,000 pence",
                "duty 12d:  12 · 25,000 = 300,000 pence, half of the 6d revenue",
                "customs 1755:  5,068,000 − 2,324,600 = £2,743,400",
                "net of management:  2,743,400 − 287,900 = £2,455,500",
                "management on the gross:  287,900 / 5,068,000, about 5.7 per cent",
            ],
            "after": [
                "Twice the duty gave half the revenue, which is Swift's two and two making "
                "one. Smith's own accounts show a gross of five million falling to under two "
                "and a half before the treasury has it, with smuggling, drawbacks and "
                "management taking the difference.",
            ],
        },
        "quiz_title": "Duties, wages and revenue",
        "quiz": [
            {"q": "In the swift preset the duty is 6d on 100,000 pounds weight, and 12d on "
                  "25,000. What is the effect on revenue of doubling the duty from 6d to 12d?",
             "a": ["It doubles", "It halves", "It stays the same", "It rises by a quarter"],
             "c": 1,
             "why": "Revenue at 6d is 600,000 pence and at 12d is `12 · 25,000 = 300,000`, "
                    "half as much. Doubling the rate quarters the quantity, which is the "
                    "customs arithmetic where two and two make only one."},
            {"q": "Smith's customs accounts for the year to January 1755: gross £5,068,000, "
                  "bounties and drawbacks £2,324,600, and the cost of management £287,900. "
                  "What was the neat revenue?",
             "a": ["£2,743,400", "£4,780,100", "£2,455,500", "£2,612,000"],
             "c": 2,
             "why": "Gross less bounties and drawbacks is £2,743,400, and the cost of "
                    "management comes off that, leaving £2,455,500. £2,743,400 is before "
                    "management, and £4,780,100 takes management from the gross and leaves "
                    "the drawbacks in."},
            {"q": "Which of these taxes does Smith say will raise the wages of labour?",
             "a": ["A tax on tobacco", "A tax on strong beer by the barrel",
                   "A tax on tea and sugar", "A tax on salt, leather, soap and candles"],
             "c": 3,
             "why": "Salt, leather, soap and candles are real necessaries of life, and a tax "
                    "on them operates as a tax on wages. Tobacco, beer, tea and sugar are "
                    "luxuries, even of the poor, and taxes on them did not raise wages."},
            {"q": "A poll-tax is assessed by each person's rank, as duke, earl, esquire, "
                  "gentleman. What does Smith say is wrong with it?",
             "a": ["It is unequal, because fortunes differ within a rank",
                   "It is arbitrary, because the assessors judge each man's fortune",
                   "It is too costly to collect",
                   "It falls only on landlords"],
             "c": 0,
             "why": "A tax by rank is certain but &ldquo;altogether unequal; the degrees of "
                    "fortune being frequently unequal in the same degree of rank&rdquo;. "
                    "The arbitrary form is the one assessed on supposed fortune. Smith says "
                    "capitations are levied at little expense, and on the lower ranks "
                    "they are taxes on wages."},
        ],
        "mistakes": [
            ("Thinking a higher duty always brings in more",
             "Revenue is the duty times the quantity that still pays it. In the swift preset "
             "the 9d duty brings in 540,000 pence and the lower 6d duty 600,000. Smith's "
             "heavy customs duties encouraged smuggling and cut the revenue below what "
             "moderate ones would have afforded."),
            ("Treating taxes on necessaries and on luxuries alike",
             "A tax on a necessary raises wages and so the cost of everything made by "
             "labour, and falls on landlords and rich consumers with an overcharge. A "
             "tax on a luxury falls on the consumer of that luxury and nothing more."),
            ("Assuming a tax on necessaries is paid by the poor who buy them",
             "Smith argues the labourer is compensated by a rise in wages, so the tax "
             "falls finally on landlords and on the consumers of manufactured goods. "
             "He adds that without the rise the poor would be less able to bring up "
             "families, and that is where the harm to the poor would come."),
        ],
        "standard": (
            "Finish when you can compute what a duty yields and say who pays it.",
            "Given duties and the quantities that pay them, compute the revenue at each, "
            "find where a higher duty yields less, and say for a necessary and for a "
            "luxury who finally pays."
        ),
        "note": (
            "The duty schedules are written for the lesson, and the lab cannot say where "
            "any real duty stood. Smith's figures for the customs of 1755 are his, "
            "from the books of the revenue. That taxes on necessaries are paid by "
            "landlords and consumers depends on his account of wages, which the last "
            "lesson tested, and that a tax on luxuries does not raise them is an "
            "observation about London in the 1770s."
        ),
    },
    # ---------------------------------------------------------------- 06
    # PSU text l. 29828-29834 (the rude state); l. 29921-29922 (want of
    # parsimony); l. 29935-29975 (the ability and the willingness to lend);
    # l. 29980 (the duty of saving); l. 30031-30052 (anticipation and funding);
    # l. 30090-30140 (the general mortgages, perpetual funding); l. 30147-30170
    # (the sinking fund); l. 30353-30460 (the debt in peace and in war); l. 30452
    # (chimerical); l. 30463-30540 (funding against the revenue within the
    # year); l. 30540-30639 (the right hand and the left; funding has
    # enfeebled every state).
    {
        "slug": "public-debts",
        "title": "Public Debts",
        "module": "Book V, Chapter 3 · Of Public Debts",
        "one_line": "A commercial state finds it easy to borrow and so does not save, and Smith's figures show that the sinking fund never keeps up with the next war.",
        "summary": (
            "In a rude state the sovereign hoards. In a commercial one he spends, and in war "
            "he borrows. Smith follows the debt from anticipations to perpetual funding, "
            "through the sinking fund, to the figures of its growth, and argues that funding "
            "destroys capital year by year. Run a debt of £129 million at three per cent with "
            "a million a year paid beyond interest, and then add a war."
        ),
        "key": [
            "debt next year = debt + interest − payment",
            "anticipation repays; funding pays interest",
            "sinking fund from lower interest: 6% to 5%",
            "a payment under interest never pays off",
            "funding spends capital that employed labour",
        ],
        "key_label": "Public debt in five lines",
        "concepts_intro": (
            "The chapter is half history and half argument. The history is a list of "
            "British funds and acts, which the lesson reads in outline; the argument has "
            "three parts."),
        "concepts": [
            ("Why a commercial state borrows",
             "In a rude state, sovereigns hoard, because nobody would lend to them and nothing "
             "tempts them to spend. In a commercial state the sovereign, like his nobles, "
             "spends on luxuries, so that his ordinary expense equals his ordinary revenue. When war "
             "comes, with an expense three or four times that of peace, and with taxes that "
             "take ten or twelve months to produce anything, there is no resource but "
             "borrowing. And the merchants whose capital passes through their hands several "
             "times a year are able and willing to lend."),
            ("Anticipation and perpetual funding",
             "A debt raised by anticipation is charged on a tax for a term of years, enough "
             "to repay both principal and interest. A debt raised by funding is charged on "
             "a tax in perpetuity, to pay the interest only, with the government free to "
             "redeem the principal. Governments overloaded the first and so drifted into "
             "the second."),
            ("The sinking fund",
             "A sinking fund is a surplus kept for paying off principal. Smith says it "
             "arose in Britain not from surplus taxes but from lower interest: when the "
             "rate fell from six to five per cent, one-sixth of each annuity was "
             "released. He says it has been misapplied to other expenses of the "
             "state in every peace."),
        ],
        "read_title": "The chapter in outline, with its figures",
        "read_intro": (
            "The chapter has four movements: why the state borrows, how, what has "
            "happened to the sinking fund, and what funding does to the country. The "
            "list of general mortgages of 1697 to 1717 and the paragraphs on annuities for "
            "lives and tontines are mentioned only."
        ),
        "body": [
            ("p", "<strong>Book V, Chapter 3.</strong> &ldquo;The want of parsimony, in time "
                  "of peace, imposes the necessity of contracting debt in time of war.&rdquo;"),
            ("p", "The chapter begins from Book III. In the rude state of society before "
                  "commerce and manufactures, a great revenue is a command of the "
                  "necessaries of life, and its owner can use it only to feed and clothe as "
                  "many people as it will feed and clothe. Hospitality of that kind seldom "
                  "ruins anyone, and so ancient sovereigns hoarded, as Tartar chiefs do now. "
                  "It was convenient to hoard in disorderly times, and nobody would lend to "
                  "a prince who might plunder him."),
            ("p", "A commercial state is different on both sides. The sovereign has the same "
                  "frivolous passions as the rich men of his dominions, and spends his "
                  "revenue as they do, so that &ldquo;His ordinary expense becomes equal to his "
                  "ordinary revenue, and it is well if it does not frequently exceed it.&rdquo; "
                  "In war he needs three or four times the peace revenue at once, and the "
                  "new taxes will not begin to yield for ten or twelve months, while the "
                  "army must be raised and the fleet fitted out in the moment of "
                  "danger. And the subjects are able to lend, because a merchant's capital "
                  "and credit may pass through his hands &ldquo;two, three, or four times in a "
                  "year&rdquo; where a gentleman's revenue passes once. They are also willing, "
                  "since they trust the justice of the government, and since the security is "
                  "transferable and commonly sells for more than they gave. The merchant, "
                  "Smith says, increases his capital by lending, and thinks it a favour to "
                  "be admitted to the first subscription. The conclusion is his bluntest line "
                  "about the state itself: &ldquo;It foresees the facility of borrowing, and "
                  "therefore dispenses itself from the duty of saving.&rdquo;"),
            ("p", "He then gives the progress, which has been &ldquo;pretty uniform&rdquo;. "
                  "First, personal credit: the unfunded debt of unpaid army and navy "
                  "accounts and of navy and exchequer bills. Then the assignment of a "
                  "particular fund, in two ways. &ldquo;When money was raised in the one way, "
                  "it was said to be raised by anticipation; when in the other, by perpetual "
                  "funding, or, more shortly, by funding.&rdquo; Britain anticipates its land "
                  "and malt taxes every year, &ldquo;Like an improvident spendthrift, whose "
                  "pressing occasions will not allow him to wait for the regular payment of "
                  "his revenue, the state is in the constant practice of borrowing of its own "
                  "factors and agents, and of paying interest for the use of its own "
                  "money.&rdquo;"),
            ("p", "Anticipation would have cleared the revenue in a few years if nobody "
                  "had overloaded it. &ldquo;But the greater part of European governments have "
                  "been incapable of those attentions&rdquo;, and anticipated again before the "
                  "first fund was clear. The funds then could not pay both principal and "
                  "interest, and it became necessary to charge them with the interest only. "
                  "The attraction is that a greater sum can always be raised by funding, and "
                  "&ldquo;To relieve the present exigency, is always the object which "
                  "principally interests those immediately concerned in the administration of "
                  "public affairs. The future liberation of the public revenue they leave to the "
                  "care of posterity.&rdquo; Smith's list of the successive general mortgages, "
                  "from £5,160,459 charged on the first of 1697 to the South Sea company's "
                  "£9,177,967 advanced in 1711, is the record of that drift, and the lesson only "
                  "mentions it."),
            ("p", "The sinking fund came from a different quarter. Early in Queen Anne's reign the "
                  "market rate fell from six to five per cent, and the creditors of the public "
                  "accepted five, which was a saving of one per cent on the capital, or a sixth "
                  "of the annuities. The surplus laid &ldquo;the foundation of what has since been "
                  "called the sinking fund&rdquo;, which in 1717 amounted to £523,454, and the "
                  "later reductions to four and to three per cent added to it. But &ldquo;A "
                  "sinking fund, though instituted for the payment of old, facilitates very much the "
                  "contracting of new debts&rdquo;, because it is a fund always at hand to "
                  "mortgage in aid of any other, and in peace it is the easy source of money "
                  "for the unexpected expense, since a new tax is felt and a diversion of "
                  "the sinking fund is not."),
            ("p", "The figures are the chapter's strongest argument. At the end of 1697 the debts, "
                  "funded and unfunded, were £21,515,742. A good deal had been on short "
                  "anticipations and annuities for lives, and in less than four years "
                  "£5,121,041 was paid off or fell in, so the debt was £16,394,701, a "
                  "reduction which has never been equalled in so short a time. The war that "
                  "ended at Utrecht took it to £53,681,076 at the end of 1714, and by "
                  "the end of 1739, seventeen years of the most profound peace having paid "
                  "off no more than £8,328,554, it stood at £46,954,623. The war of 1739 "
                  "brought it by 1748 to £78,293,313, which is about £31.3 million added in "
                  "less than nine years. At the peace of 1763 the funded debt was "
                  "£122,603,336, and on 5 January 1775 the whole debt was £129,146,322. In the "
                  "eleven peaceful years since, only £10,415,476 had been paid, and Smith "
                  "reckons that out of the ordinary revenue less than half a million a year. "
                  "&ldquo;It would be altogether chimerical, therefore, to expect that the public "
                  "debt should ever be completely discharged, by any savings which are "
                  "likely to be made from that ordinary revenue as it stands at present.&rdquo;"),
            ("p", "The lab runs his case in round millions, written for this lesson on his "
                  "figures: a debt of 129 at three per cent, the rate to which most of "
                  "the public funds had fallen. The interest is 3.87 a year. In the "
                  "million preset the payment is 4.87, that is the interest and the "
                  "&ldquo;million, perhaps&rdquo; that Smith thinks might be spared, if peace "
                  "continued, out of the sinking fund. The debt falls by one million in the "
                  "first year, a little more each year after that as the interest falls, and "
                  "is paid off in the 54th year, with nothing borrowed in the meantime. The "
                  "half preset pays only half a million beyond the interest, 4.37, and "
                  "takes 74 years. In the war preset the million of the first preset "
                  "is paid for six years and then a war adds 100, the sum of Smith's footnote "
                  "on the war that began in 1775, at the end of the sixth year. The debt is "
                  "then about 222.5, and its interest, about 6.68, is more than the whole payment, and the debt grows and is never paid off. That is the "
                  "chapter's argument as a sum: the paying-down is slow and arithmetically "
                  "easy to undo, and the next war is not a matter of whether but when."),
            ("p", "What does funding do to the country? Smith's answer is that the capital lent "
                  "to the government was, from the moment it was advanced, &ldquo;a certain "
                  "portion of the annual produce, turned away from serving in the function of a "
                  "capital, to serve in that of a revenue&rdquo;. Its owners were repaid by "
                  "an annuity which they could sell or borrow on, but the new capital they "
                  "got by doing so was withdrawn from other employments, and the country has "
                  "one capital where it would have had two. When the expense is met by taxes "
                  "within the year, private people's spending is turned from one unproductive "
                  "use to another and no capital is destroyed. &ldquo;When the public expense is "
                  "defrayed by funding, it is defrayed by the annual destruction of some "
                  "capital which had before existed in the country&rdquo;. He gives funding its "
                  "due. Taxes are lighter in war, so people can still save, and funding "
                  "does less harm to accumulation in the short run. But in the long run the "
                  "taxes that pay the interest burden peace as well, and under the other "
                  "system &ldquo;Wars would, in general, be more speedily concluded, and less "
                  "wantonly undertaken&rdquo;, since the people would feel the whole burden."),
            ("p", "The best known objection to him he states and answers: &ldquo;In the "
                  "payment of the interest of the public debt, it has been said, it is the "
                  "right hand which pays the left.&rdquo; The money does not leave the country. "
                  "He calls this &ldquo;the sophistry of the mercantile system&rdquo;, and he adds "
                  "that part of the debt is held abroad. But &ldquo;though the whole debt were "
                  "owing to the inhabitants of the country, it would not, upon that account, be "
                  "less pernicious&rdquo;: the interest is taken from the owners of land and "
                  "of capital stock, who have an interest in their own estates and "
                  "businesses, and paid to creditors who have none in any particular portion. "
                  "The objection has had a long life. Ricardo, who disliked the funding "
                  "system, argued in his <em>Principles</em> that whether a war is paid by "
                  "taxes or by loan comes to the same thing for the economy, since the "
                  "taxes that will pay the loan's interest are worth as much as the sum "
                  "itself, though he doubted that people see it so; Robert Barro revived "
                  "the argument in 1974, and it has since been called Ricardian equivalence. In the 1940s Abba Lerner argued that a debt "
                  "owed within a nation is owed to ourselves, and that what matters is "
                  "the real resources a government uses. Smith's reply is about who is taxed and "
                  "who receives, and the three do not answer each other; they are different "
                  "questions."),
            ("p", "He closes with the question &ldquo;Is it likely that, in Great Britain alone, a "
                  "practice, which has brought either weakness or dissolution into every "
                  "other country, should prove altogether innocent?&rdquo; and with a "
                  "caution that cuts both ways. Britain has borne the burden with ease, "
                  "and her agriculture and trade flourished at the end of the late war, so "
                  "&ldquo;Great Britain seems to support with ease, a burden which, half a "
                  "century ago, nobody believed her capable of supporting&rdquo;. Yet &ldquo;Let us not, "
                  "however, upon this account, rashly conclude that she is capable of "
                  "supporting any burden&rdquo;. Karl Marx, in Capital, names the national "
                  "debt as one of the levers of primitive accumulation, and <em>Genesis of the "
                  "Industrial Capitalist</em>, in the Capital Subject, takes that up. Here the next "
                  "lesson, <em>Bankruptcy Disguised as Debasement</em>, takes up what Smith "
                  "says happens to such debts in the end."),
        ],
        "lab": ("wonkit", {
            "mode": "debt",
            "view": "sinking",
            "money_unit": "£m",
            "preset": "million",
            "presets": [
                {"id": "million", "label": "Smith's debt in round millions, 3 per cent, a million a year beyond interest, written for this lesson",
                 "debt": 129, "interest": 3, "payment": "4.87", "years": 100, "expect": {"wdbFirst": "3.87 £m", "wdbOff": "in year 54", "wdbInterest": "≈ 131.84 £m"}},
                {"id": "half", "label": "The same debt with half a million a year beyond interest, written for this lesson",
                 "debt": 129, "interest": 3, "payment": "4.37", "years": 100, "expect": {"wdbFirst": "3.87 £m", "wdbOff": "in year 74", "wdbInterest": "≈ 191.52 £m"}},
                {"id": "war", "label": "The million a year, then a war adding 100 in the sixth year, written for this lesson",
                 "debt": 129, "interest": 3, "payment": "4.87", "years": 100,
                 "borrow": "6, 100", "expect": {"wdbOff": "not paid off within 100 years", "wdbBorrowed": "100 £m", "wdbEnd": "≈ 1,131.24 £m after 100 years"}},
            ],
            "panel_title": "A debt with interest and a yearly payment",
            "panel_intro": (
                "A debt, a rate of interest and a yearly payment go in, with any war loans. "
                "The lab gives the debt year by year, the years to pay it off, and the interest "
                "paid. Run the million preset, then the half, then the war."
            ),
        }),
        "steps_title": "Following a debt year by year",
        "steps_intro": "Four steps, the same for any debt and payment.",
        "steps": [
            ("Compute the year's interest",
             "Multiply the debt by the rate. The payment must cover this first, or the "
             "debt grows and the lab refuses it."),
            ("Pay the interest, then the principal",
             "What is left of the payment after interest is the sinking fund for the year. "
             "It comes off the debt."),
            ("Add any new loans",
             "A war loan adds to the debt in its year, and from then on the interest is "
             "charged on the larger sum."),
            ("Read off the result",
             "Note the year the debt reaches zero, if it does, the interest paid in total, "
             "and whether a new loan has made the payment too small to cover the "
             "interest."),
        ],
        "worked": {
            "title": "A debt of 129 and a million a year beyond interest",
            "intro": [
                "A debt of £129 million at three per cent, with a yearly payment of £4.87 "
                "million, which is the first year's interest and one million more.",
            ],
            "lines": [
                "interest, year 1:  3/100 · 129 = 3.87",
                "principal paid, year 1:  4.87 − 3.87 = 1.00",
                "debt, end of year 1:  129 − 1 = 128",
                "interest, year 2:  3/100 · 128 = 3.84",
                "principal paid, year 2:  4.87 − 3.84 = 1.03",
                "debt after six payments:  ≈ 122.53",
                "war loan of 100:  ≈ 222.53, interest ≈ 6.68 > 4.87",
            ],
            "after": [
                "Each year the interest is a little smaller and the principal a little "
                "larger. The million preset is cleared in the 54th year. After a war loan "
                "of 100 the interest on the larger debt is above the payment, and the "
                "sinking fund is gone.",
            ],
        },
        "quiz_title": "Debts, funds and their arithmetic",
        "quiz": [
            {"q": "Interest on the public debt falls from six to five per cent. What "
                  "fraction of each annuity does the saving come to?",
             "a": ["One-fifth", "One-half", "One-sixtieth", "One-sixth"],
             "c": 3,
             "why": "An annuity of six on each hundred falls to five, a saving of one, and "
                    "`1/6` of six. Smith says &ldquo;one-sixth of the greater part of the "
                    "annuities&rdquo;. One-fifth is the saving as a share of the new annuity."},
            {"q": "The debt stood at £46,954,623 at the end of 1739 and £78,293,313 at the "
                  "end of 1748. About how much did the war add?",
             "a": ["About £8.3 million", "About £46.9 million",
                   "About £31.3 million", "About £125.2 million"],
             "c": 2,
             "why": "The difference is £31,338,690, about £31.3 million. £8.3 million is the "
                    "sum paid off in the seventeen years of peace, £46.9 million is the debt "
                    "before the war and £125.2 million adds the two debts together."},
            {"q": "In the million preset, a debt of 129 at three per cent is paid 4.87 a "
                  "year. What happens?",
             "a": ["It is paid off in about 54 years",
                   "It is paid off in 129 years, a million a year",
                   "It is paid off in about 26 years",
                   "It is never paid off, because the interest grows"],
             "c": 0,
             "why": "The payment covers the interest and a million more, and the interest "
                    "falls as the debt does, so the debt is cleared in the 54th year. 129 "
                    "years would be right if there were no interest, and 26 would be right "
                    "if the payment were all principal. The debt does not grow, because the "
                    "payment exceeds the first year's interest."},
            {"q": "On Smith's account, why do governments prefer perpetual funding to "
                  "anticipation once they are used to it?",
             "a": ["A greater sum can be raised by it in the present exigency",
                   "It repays the principal sooner",
                   "It needs no taxes to be set aside for the interest",
                   "Lenders prefer it because it carries no risk of default"],
             "c": 0,
             "why": "&ldquo;a greater sum can, in all cases, be raised by this new practice "
                    "than by the old one of anticipation&rdquo;. It puts off the liberation of "
                    "the revenue to a time so indefinite that it may never come, and it "
                    "does need taxes for the interest."},
        ],
        "mistakes": [
            ("Expecting a sinking fund to keep pace with the debt",
             "Smith's figures say otherwise: seventeen years of peace paid £8.3 million "
             "against a war's £31.3 million, and the sinking fund is in peace the "
             "easiest money to divert. The war preset shows the arithmetic: one new loan "
             "of 100 turns a debt that was being paid down into one that grows."),
            ("Treating perpetual funding as a loan that falls due",
             "A funded debt is charged with the interest only, and the principal is "
             "redeemable at the government's option. Nothing falls due, which is the "
             "attraction and the danger. An anticipation is repaid, in principle, in a "
             "term of years."),
            ("Reading Smith's reply to the right-hand-and-left objection as being about money leaving the country",
             "He does say part of the debt is held abroad, but he also says it would be "
             "pernicious &ldquo;though the whole debt were owing to the inhabitants of the "
             "country&rdquo;. His point is that interest is taxed from those who care for "
             "their own estates and paid to those who do not."),
        ],
        "standard": (
            "Finish when you can follow a debt year by year and say what a loan does to it.",
            "Given a debt, a rate and a yearly payment, compute the interest and principal "
            "paid each year, the year the debt is cleared, and the effect of a new loan, "
            "and explain why Smith thinks a sinking fund cannot be relied on."
        ),
        "note": (
            "The preset figures are Smith's rounded to millions, with the payments written "
            "for the lesson, and the three per cent is a simplification of a debt that "
            "carried several rates. The lab shows what the chapter's arithmetic implies: "
            "a payment above the interest clears a debt, a loan above it undoes the payment. "
            "Whether funding destroys capital, as Smith holds, or merely transfers it, as "
            "Ricardo and the equivalence writers say, is a matter of argument which no "
            "sum here settles."
        ),
    },
    # ---------------------------------------------------------------- 07
    # PSU text l. 30640-30646 (no single instance of a debt fairly paid);
    # l. 30647-30685 (the sixpence raised to a shilling; the juggling trick);
    # l. 30684-30722 (the Roman as); l. 30723-30763 (adulteration and
    # augmentation); l. 30764-30790 (liberation needs more revenue or less
    # expense); l. 30795-30809 (the empire as a Utopia); l. 30936-30950 (the
    # arithmetic of the revenue of the empire); l. 31172-31186 (the debt
    # contracted in defence of all the provinces); l. 31247-31304 (the
    # expense of the colonies; the project of an empire).
    {
        "slug": "the-debasement-of-the-coin",
        "title": "Bankruptcy Disguised as Debasement",
        "module": "Book V, Chapter 3 · Of Public Debts (the end of the chapter and of the book)",
        "one_line": "Smith says a debt is hardly ever fairly paid, that states disguise bankruptcy by lightening the coin, and that the last way left for Britain is to enlarge the revenue or lay down the empire.",
        "summary": (
            "The chapter and the book end together. Smith shows how raising the denomination of "
            "the coin pays a debt in name only, from the sixpence called a shilling to the "
            "Roman as. He then asks what Britain can do instead: more revenue, from a union "
            "with Ireland and the colonies, or less expense, which means giving up an "
            "empire he says exists only in the imagination. Work the debasement sums on his "
            "figures."
        ),
        "key": [
            "metal paid = debt × new metal / old metal",
            "the creditor loses 1 − new/old",
            "sixpence called a shilling: half the silver",
            "the Roman as, 12 to 2 ounces: one-sixth",
            "open raising is violence; adulteration, fraud",
        ],
        "key_label": "The end of the book in five lines",
        "concepts_intro": (
            "The last part of the chapter has two jobs, and the lesson takes them in turn: "
            "what states do to avoid paying, and what Smith thinks Britain might do instead."
        ),
        "concepts": [
            ("A pretended payment",
             "If the denomination of the coin is raised, so that a smaller weight of silver "
             "carries the old name, a debt can be paid in the old sum and the new coin. "
             "The sum is the same and the silver is less. Smith calls it a real public "
             "bankruptcy disguised as a payment."),
            ("Augmentation and adulteration",
             "Raising the denomination is an open operation: pieces of smaller weight are "
             "called by the name of larger ones. Adulteration puts more alloy in the coin and "
             "keeps its appearance, and is generally concealed. Smith calls the first an "
             "injustice of open violence and the second of treacherous fraud."),
            ("What is left to Britain",
             "The public revenue can be freed only by a very considerable increase of the "
             "revenue or a similar reduction of the expense. For the first, Smith "
             "proposes a fairer land tax and house tax and reforms of the customs and "
             "excise, and then a union with Ireland and the colonies under one system of "
             "taxation, with representation. For the second he proposes that the colonies, "
             "if they will not contribute, be given up."),
        ],
        "read_title": "The end of the chapter, then the end of the book",
        "read_intro": (
            "The debasement passage is a few pages and is arithmetic throughout. The "
            "pages that follow are a plan for the empire, which this lesson reads in "
            "outline: they close the book."
        ),
        "body": [
            ("p", "<strong>Book V, Chapter 3.</strong> &ldquo;When national debts have once been "
                  "accumulated to a certain degree, there is scarce, I believe, a single "
                  "instance of their having been fairly and completely paid. The liberation of "
                  "the public revenue, if it has ever been brought about at all, has always "
                  "been brought about by a bankruptcy; sometimes by an avowed one, though "
                  "frequently by a pretended payment.&rdquo;"),
            ("p", "The last lesson ended with a debt that could not be paid by saving. Smith's next "
                  "step is historical and blunt. &ldquo;The raising of the denomination of the "
                  "coin has been the most usual expedient by which a real public bankruptcy has "
                  "been disguised under the appearance of a pretended payment.&rdquo; His "
                  "example is the sixpence. Suppose a sixpence is, by proclamation, raised to the "
                  "denomination of a shilling, and twenty sixpences to that of a pound. A man who "
                  "borrowed twenty shillings, &ldquo;or near four ounces of silver&rdquo;, would "
                  "repay it with twenty sixpences, &ldquo;or with something less than two "
                  "ounces&rdquo;. A national debt of about a hundred and twenty-eight millions, near "
                  "the funded and unfunded debt of Great Britain, would be paid with about "
                  "sixty-four. &ldquo;It would, indeed, be a pretended payment only, and the "
                  "creditors of the public would really be defrauded of ten shillings in the "
                  "pound of what was due to them.&rdquo;"),
            ("p", "The sixpence preset runs it, with the old pound at 4 ounces and the new one at "
                  "2, on a debt of 128 million. The silver owed is 512 million ounces, the "
                  "silver paid is 256 million, and the creditor loses a half. Smith rounds, "
                  "since the pound's weight is a little under four ounces, and the lab takes his "
                  "round numbers. He goes on to the harm, which is wider than the "
                  "creditors of the public. Every private creditor suffers proportionally, and "
                  "since the public creditors are mostly wealthy people who are creditors rather "
                  "than debtors in their dealings with others, they cannot recover by paying "
                  "their own debts in the same coin. The result is &ldquo;enriching, in most "
                  "cases, the idle and profuse debtor, at the expense of the industrious and "
                  "frugal creditor&rdquo;. If bankruptcy must come, &ldquo;a fair, open, and "
                  "avowed bankruptcy, is always the measure which is both least dishonourable to "
                  "the debtor, and least hurtful to the creditor&rdquo;, and a state that covers "
                  "its disgrace by &ldquo;a juggling trick of this kind, so easily seen through, "
                  "and at the same time so extremely pernicious&rdquo; has poorly provided "
                  "for its honour."),
            ("p", "He has the ancient precedent. The Romans, at the end of the first Punic war, "
                  "&ldquo;reduced the As, the coin or denomination by which they computed the "
                  "value of all their other coins, from containing twelve ounces of copper, to "
                  "contain only two ounces&rdquo;, and so paid their debts with &ldquo;the sixth "
                  "part of what it really owed&rdquo;. The as preset puts the 128 million "
                  "through that: twelve ounces to two is a sixth, so £21,333,333 6s 8d, the "
                  "figure Smith gives. In the second Punic war the as fell to one ounce and then "
                  "to half an ounce, the twenty-fourth part of the original, and the as-half "
                  "preset compounds the three operations in one: £5,333,333 6s 8d, in the "
                  "lab 5⅓ million. Smith adds that the law was probably popular. The poor "
                  "citizens were constantly in debt to the rich and great, who lent "
                  "at exorbitant interest to secure their votes, and what they called "
                  "new tables, a law to pay debts in part, was what the reduction of the "
                  "coin amounted to. The rich consented partly for the same reason and partly "
                  "to restore vigour to the government they directed."),
            ("p", "Debasement can be done by weight or by fineness. &ldquo;An augmentation, or "
                  "a direct raising of the denomination of the coin, always is, and from its "
                  "nature must be, an open and avowed operation.&rdquo; Adulteration, mixing "
                  "more alloy into pieces of the same appearance, &ldquo;has generally been a "
                  "concealed operation&rdquo;. Smith's sum for it: if a pound weight of coin "
                  "had eight ounces of alloy in twelve, a pound sterling of it would be worth "
                  "little more than six shillings and eightpence of the present money. The "
                  "adulteration preset takes a third, and a debt of 128 would be paid with "
                  "about 42⅔. He judges the two by their moral character: &ldquo;Both operations "
                  "are unjust. But a simple augmentation is an injustice of open violence; "
                  "whereas an adulteration is an injustice of treacherous fraud.&rdquo; The "
                  "coin, after any considerable augmentation, has seldom been brought back "
                  "to its former weight, but after the greatest adulterations it has almost "
                  "always been brought back to its former fineness, because the fury of the "
                  "people could be appeased no other way. He lists the English coin at the "
                  "end of Henry VIII's reign, and the Scottish in James VI's minority, and "
                  "says the practice has been common in most countries."),
            ("p", "What is Britain to do instead? Smith first tries the home revenue: "
                  "a more equal land tax and house tax, and the alterations in customs and excise "
                  "he has already described, which would raise a considerable augmentation "
                  "without increasing the burden of most people. It would not be enough. So "
                  "he turns to the empire, and says so himself: it may be &ldquo;a new Utopia, "
                  "less amusing, certainly, but no more useless and chimerical than the old "
                  "one&rdquo;. The proposal is that the British system of taxation, land tax, "
                  "stamp duties, customs and excise, be extended to Ireland and the American "
                  "colonies, with a union of the customs laws and a fair and equal "
                  "representation in Parliament."),
            ("p", "His estimate is a short sum. Britain levies ten millions on under eight "
                  "millions of people. Ireland has over two millions and the American provinces, "
                  "by the congress's own accounts, over three; he allows only three for the "
                  "colonies of America and the West Indies together, so the empire has "
                  "thirteen million inhabitants. At the same "
                  "rate per head, ten millions on eight is 1.25 each, and thirteen millions "
                  "would yield £16,250,000. Take a million for the civil governments of Ireland "
                  "and the plantations, and £15,250,000 remains for the general expense and "
                  "the debt. If Britain could spare a million out of its own ten for the debt "
                  "in peace, the empire could spare £6,250,000, which is the fifteen and a "
                  "quarter less the nine millions of Britain's ordinary expense. A sinking "
                  "fund that large, with the interest of what it has paid off added to it each "
                  "year, would clear the debt in a few years and permit the abolition of the "
                  "taxes on necessaries. The sum is his, from his own assumptions, and he "
                  "says that the revenue cannot be ascertained with tolerable exactness, and "
                  "that new provinces would need indulgence."),
            ("p", "He argues that it is just. &ldquo;It is not contrary to justice, that both "
                  "Ireland and America should contribute towards the discharge of the public debt "
                  "of Great Britain.&rdquo; The debt was contracted in defence of all the "
                  "provinces, and the last war, he says, in defence of America above all. He "
                  "also takes the Americans' objection that without gold and silver there is "
                  "no paying taxes, and says their scarcity of metal is choice and not "
                  "poverty: paper money serves their domestic business, and the "
                  "colonial governments, Massachusetts in 1747, have more than once paid "
                  "their debts in depreciated paper. That passage, and a sentence about the "
                  "enslaved people who are the greater part of the inhabitants of the "
                  "southern colonies and the West Indies, whose consumption he reckons "
                  "from their masters' interest in feeding them well, is Smith reasoning "
                  "from revenue and not from the people, and it reads coldly now."),
            ("p", "Then the other side of the choice. If no considerable revenue can be drawn "
                  "from the empire, the only resource left is a diminution of expense, and "
                  "the largest expense is the colonies. The last war, he says, undertaken "
                  "altogether on their account, cost upwards of ninety millions, and the "
                  "Spanish war of 1739 and the French war that followed upwards of forty, "
                  "&ldquo;much more than double the sum which the national debt amounted to "
                  "before the commencement of the first of them&rdquo;. Countries that "
                  "contribute neither revenue nor military force &ldquo;cannot be considered as "
                  "provinces&rdquo;; they are, at most, &ldquo;a sort of splendid and shewy "
                  "equipage of the empire&rdquo;. Then the paragraph that ends the book."),
            ("p", "<strong>Book V, Chapter 3, the last page.</strong> &ldquo;It has hitherto "
                  "been, not an empire, but the project of an empire; not a gold mine, but the "
                  "project of a gold mine; a project which has cost, which continues to cost, "
                  "and which, if pursued in the same way as it has been hitherto, is likely to "
                  "cost, immense expense, without being likely to bring any profit.&rdquo; "
                  "Smith's alternatives are two, and he does not pick for his rulers: realize "
                  "the golden dream, which means union and shared taxes, or awake from it and "
                  "give up what cannot be made to contribute. The last sentence says it "
                  "is time for Great Britain to &ldquo;endeavour to accommodate her future "
                  "views and designs to the real mediocrity of her circumstances&rdquo;. The "
                  "book appeared in March 1776 and the fighting had begun. He proposed a union "
                  "and it did not happen, and what followed is for historians, who still "
                  "dispute what the colonies cost and what they brought, and whether "
                  "the monopoly of the colony trade was the loss he says. Smith died in 1790 and "
                  "cannot answer them."),
            ("p", "That is the end of the Wealth of Nations, and of this course. Thirteen "
                  "courses have gone the way he went: from a pin factory and the division of "
                  "labour, through money, price, wages, profit and rent, the stock that "
                  "puts labour in motion, the course of opulence, the mercantile system and the "
                  "colonies, to what a sovereign must spend and how he can raise it. At each step "
                  "the labs have computed what Smith's reasoning implies for stated figures, "
                  "his own where he gave them, and none of them can say whether that reasoning "
                  "describes any economy, then or now. That is what the book argued, and what "
                  "its critics still dispute. Capital, the next read-along on the shelf, "
                  "takes up his definitions by name, in <em>Former Discussions: Quesnay and "
                  "Smith</em> and <em>The Physiocrats and Adam Smith on Fixed Capital</em>."),
        ],
        "lab": ("wonkit", {
            "mode": "debt",
            "view": "debase",
            "money_unit": "£m",
            "silver_unit": "million oz of metal",
            "preset": "sixpence",
            "presets": [
                {"id": "sixpence", "label": "Smith's sixpence called a shilling: near four ounces of silver to two, on 128 million",
                 "debt": 128, "old": 4, "new": 2, "expect": {"wdbOwed": "512 million oz of metal", "wdbSilver": "256 million oz of metal", "wdbLoss": "50% (256 million oz of metal)", "wdbPretended": "128 £m paid in name, worth 64 £m in the old coin"}},
                {"id": "as", "label": "Smith's Roman as: twelve ounces of copper to two, on 128 million",
                 "debt": 128, "old": 12, "new": 2, "expect": {"wdbSilver": "256 million oz of metal", "wdbLoss": "≈ 83.33% (1,280 million oz of metal)", "wdbPretended": "128 £m paid in name, worth 64/3 £m ≈ 21.33 £m in the old coin"}},
                {"id": "as-half", "label": "Smith's three Roman operations in one: twelve ounces to half an ounce, on 128 million",
                 "debt": 128, "old": 12, "new": "1/2", "expect": {"wdbSilver": "64 million oz of metal", "wdbLoss": "≈ 95.83% (1,472 million oz of metal)", "wdbPretended": "128 £m paid in name, worth 16/3 £m ≈ 5.33 £m in the old coin"}},
                {"id": "adulteration", "label": "A coin of a third of its silver, after Smith's six and eightpence, on 128 million",
                 "debt": 128, "old": 1, "new": "1/3", "expect": {"wdbSilver": "128/3 ≈ 42.67 million oz of metal", "wdbLoss": "≈ 66.67% (256/3 ≈ 85.33 million oz of metal)", "wdbPretended": "128 £m paid in name, worth 128/3 £m ≈ 42.67 £m in the old coin"}},
            ],
            "panel_title": "A debt paid in lighter coin",
            "panel_intro": (
                "A debt, the metal in a unit of the old coin and the metal in a unit of the new go "
                "in. The lab gives the metal owed, the metal paid, and the share the creditor "
                "loses. Run the sixpence preset, then the Roman as, then the adulteration."
            ),
        }),
        "steps_title": "Working out a pretended payment",
        "steps_intro": "Four steps, for any lightening of the coin.",
        "steps": [
            ("Fix the metal in a unit of the old coin",
             "How much silver, or copper, was in a pound, a shilling or an as before? "
             "Smith's round numbers are near four ounces to the pound."),
            ("Fix the metal in a unit of the new",
             "After the denomination is raised, or the alloy mixed in, how much is in the "
             "same name? Twenty sixpences of the old coin hold under two ounces."),
            ("Compute the metal owed and the metal paid",
             "Owed is the debt times the old weight. Paid is the same nominal debt times "
             "the new weight. Their ratio is new over old."),
            ("Read the creditor's loss",
             "The creditor loses one minus new over old of what he was owed in metal. "
             "A half for the sixpence, five-sixths for the as, and so on."),
        ],
        "worked": {
            "title": "The same debt through three operations",
            "intro": [
                "A national debt of 128 million, and three ways of paying it in coin that "
                "carries less metal: Smith's sixpence, the Roman as, and the as twice more.",
            ],
            "lines": [
                "sixpence called a shilling:  128 · 2/4 = 64 million",
                "first Roman as, twelve ounces to two:  128 · 2/12 = 64/3 = 21⅓ million",
                "as to half an ounce:  128 · (1/2)/12 = 16/3 = 5⅓ million",
                "creditor's loss at the sixpence:  1 − 2/4 = 1/2",
                "revenue of the empire:  (10/8) · 13 = 16.25 million",
            ],
            "after": [
                "Smith's £21,333,333 6s 8d and £5,333,333 6s 8d are the second and third lines, "
                "his sixty-four millions the first. The last line is the other half of the "
                "chapter: what the same taxes would bring from thirteen million people.",
            ],
        },
        "quiz_title": "Debasement and the empire's revenue",
        "quiz": [
            {"q": "The Roman as fell from twelve ounces of copper to two. A debt of 128 million "
                  "is paid with the new as. What does it come to in the old sums?",
             "a": ["£64 million", "£21⅓ million", "£5⅓ million", "£42⅔ million"],
             "c": 1,
             "why": "Two twelfths is a sixth, `128/6 = 64/3`, or £21⅓ million, the sum Smith "
                    "gives. £64 million is the sixpence case, a half, £5⅓ million is after "
                    "the further reductions to half an ounce, and £42⅔ million is a third."},
            {"q": "A sixpence is proclaimed a shilling, and a debt of 128 million, owed in "
                  "twenty shillings to the pound, is paid in twenty sixpences to the pound. What "
                  "does the creditor lose, in silver?",
             "a": ["Half of what he was owed", "A sixth", "A quarter",
                   "Nothing, because the nominal sum is paid"],
             "c": 0,
             "why": "The pound now holds half the silver, so he is paid half in silver: "
                    "Smith's &ldquo;ten shillings in the pound&rdquo;. The nominal sum is paid in "
                    "full, which is the pretence, and a sixth is the Roman case."},
            {"q": "How does Smith characterise a simple raising of the denomination of the coin "
                  "against an adulteration of its standard?",
             "a": ["Open violence, against treacherous fraud",
                   "Treacherous fraud, against open violence",
                   "A fair, open, and avowed bankruptcy, against a pretended payment",
                   "Both just, if the state is in need"],
             "c": 0,
             "why": "&ldquo;a simple augmentation is an injustice of open violence; whereas an "
                    "adulteration is an injustice of treacherous fraud&rdquo;. He says &ldquo;Both "
                    "operations are unjust&rdquo;, so the last option is false. The "
                    "avowed bankruptcy is the course he thinks least dishonourable and "
                    "least hurtful."},
            {"q": "Great Britain levies ten million pounds on under eight million people. At "
                  "the same rate per head, what would the empire raise on thirteen million?",
             "a": ["£13 million", "£15.25 million", "£6.25 million", "£16.25 million"],
             "c": 3,
             "why": "`(10/8) · 13 = 16.25`. £15.25 million is what remains after a million "
                    "for the civil government of Ireland and the plantations, and £6.25 "
                    "million is what Smith says might be spared for the debt out of that "
                    "after Britain's own expense."},
        ],
        "mistakes": [
            ("Thinking debasement pays the debt",
             "It pays the debt in name. In the sixpence preset the debtor hands over "
             "256 million ounces against 512 million owed, and the creditor is defrauded of "
             "half. Smith adds that the harm runs on to every private creditor, and "
             "without advantage to the public."),
            ("Reading a fair, open and avowed bankruptcy as his advice",
             "He says that if a state must be bankrupt, an open bankruptcy is the least "
             "dishonourable and least hurtful, which is a ranking of bad courses. His "
             "own proposals are to raise more revenue or spend less, so that it "
             "need not come to that."),
            ("Taking the last page as a forecast",
             "Smith offers two ways out, a union with fair representation or giving up what "
             "will not contribute, and says the empire has so far been only the "
             "project of an empire. He wrote as the war began and could not know the outcome, "
             "and historians do not agree on his costs."),
        ],
        "standard": (
            "Finish when you can work out what a debasement does to a debt in metal.",
            "Given a nominal debt and the metal in a unit of the old and new coin, compute the "
            "metal owed, the metal paid and the creditor's loss, and say why Smith calls the "
            "result a pretended payment."
        ),
        "note": (
            "The lab applies new over old to a debt and nothing else. Smith's figures for the "
            "pound, the as and the alloy are his own and rounded, and the revenue of the empire "
            "is his estimate from assumed populations. Whether a union could have worked "
            "politically, whether the colonies cost what he says and whether the whole book "
            "describes any economy are not questions this arithmetic reaches. The labs "
            "show what the reasoning implies for stated figures, and the argument goes on "
            "past them."
        ),
    },
]
