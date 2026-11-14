"""Wages and Profits, lessons 1-5 -- Book I, Chapters 8 and 9.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt
(the Electronic Classics Series edition); the comment beside each lesson gives
its line numbers. A drop capital in the text ("THE PRODUCE OF LABOUR") is not
quoted. Smith's spelling is kept inside quotations.

Money: Smith reckons in pounds, shillings and pence, twelve pence to the
shilling and twenty shillings to the pound. Figures in a preset are either
Smith's, and the preset's label says so, or written for the lesson, and the
label says that.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # PSU text l. 2093-2123 (the original state and improvements); l. 2124-2158
    # (rent and profit as deductions); l. 2159-2212 (the contract and the
    # combinations); l. 2213-2241 (the lowest rate; Cantillon, l. 2219-2238).
    # The figures for the preset are from later in the chapter: Hales, l.
    # 2521-2534 (ten shillings a week, six persons, twenty pence a head);
    # the wages of l. 2441-2445 and l. 2500-2505.
    {
        "slug": "the-masters-and-the-workmen",
        "title": "The Masters and the Workmen",
        "module": "Book I, Chapter 8 · Of the Wages of Labour",
        "one_line": "Wages are fixed by a contract between parties whose interests differ, and the masters can wait longer; the floor is what keeps the labourer and his family alive.",
        "summary": (
            "Smith begins from the first state of things, where the whole produce is the "
            "labourer's, and shows how rent and then profit take their deductions. What "
            "is left is settled by a bargain between workmen and masters in which, he "
            "says, the masters have the advantage. Below it is a floor: wages must keep "
            "the labourer and bring up a family. Set a family's weekly needs, from "
            "figures he reports, against three wages."
        ),
        "key": [
            "first state: the whole produce is wages",
            "rent, then profit, are deductions from it",
            "wages follow the contract; masters can wait",
            "the floor: the family's maintenance, plus",
        ],
        "key_label": "The first part of Chapter 8",
        "concepts_intro": (
            "The chapter begins with a state of things Smith says has already ended, and "
            "then describes the bargain that took its place."
        ),
        "concepts": [
            ("Wages as the whole produce",
             "In the original state of things, before land is owned or stock accumulated, the "
             "labourer has &ldquo;neither landlord nor master to share with him&rdquo;. "
             "Wages would then be the whole produce of labour, and would have grown with "
             "every improvement in its productive powers. That state, Smith says, could "
             "not last beyond the first appropriation of land and accumulation of stock."),
            ("The contract",
             "In practice twenty workmen serve a master for one who is independent, and "
             "their wages depend on a contract between parties &ldquo;whose interests are "
             "by no means the same&rdquo;. Smith holds that the masters generally have the "
             "advantage: they are fewer, easier to combine, favoured by the law, and able "
             "to hold out longer."),
            ("The lowest rate",
             "Below the bargain there is a floor. A man's wages must at least maintain him, "
             "and on most occasions somewhat more, or the race of such workmen could not "
             "last beyond the first generation. Smith reports Cantillon's guess at the "
             "proportion and says he will not decide it."),
        ],
        "read_title": "The deductions, the bargain and the floor",
        "read_intro": (
            "Chapter 8 is long, and this lesson reads its first third, up to the "
            "sentence that names the lowest rate consistent with common humanity."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 8.</strong> &ldquo;In that original state of "
                  "things which precedes both the appropriation of land and the accumulation "
                  "of stock, the whole produce of labour belongs to the labourer. He has "
                  "neither landlord nor master to share with him.&rdquo;"),
            ("p", "The chapter's first sentence says that the produce of labour &ldquo;"
                  "constitutes the natural recompence or wages of labour&rdquo;, and the "
                  "first thing Smith does with the idea is to say it has not lasted. Had "
                  "it continued, wages would have risen with every improvement the division "
                  "of labour brought, and all things would have become cheaper in reality. "
                  "He adds a point about real and apparent prices that the course on money "
                  "and the measure of value prepared: if a day's labour makes ten times as "
                  "much in most trades and only twice as much in one, a pound of that one "
                  "will exchange for five times as much of the others as before and yet be "
                  "half as hard to get, for it will cost half the labour. But this state, "
                  "&ldquo;could not last beyond the first introduction of the appropriation "
                  "of land and the accumulation of stock&rdquo;, and so there is no use "
                  "following it further."),
            ("p", "What replaces it is a series of deductions. &ldquo;His rent makes the "
                  "first deduction from the produce of the labour which is employed upon "
                  "land.&rdquo; The man who tills the ground seldom has enough to maintain "
                  "himself until harvest, so a farmer advances it, and &ldquo;This profit "
                  "makes a second deduction from the produce of the labour which is employed "
                  "upon land.&rdquo; In arts and manufactures it is the same: the master "
                  "advances materials, wages and maintenance and takes his profit from the "
                  "value the workmen add. The independent workman who has stock enough for "
                  "both is the exception, &ldquo;in every part of Europe twenty workmen serve "
                  "under a master for one that is independent&rdquo;. The previous course "
                  "gave the arithmetic of those deductions."),
            ("p", "What the wage then is depends, Smith says, on a bargain. &ldquo;The "
                  "workmen desire to get as much, the masters to give as little, as "
                  "possible.&rdquo; He foresees which side will win on ordinary occasions, "
                  "and gives reasons that are short and easy to check. The masters are "
                  "fewer and combine more easily. The law authorises, or at least does not "
                  "prohibit, their combinations while it prohibits the workmen's: &ldquo;We "
                  "have no acts of parliament against combining to lower the price of work, "
                  "but many against combining to raise it.&rdquo; And the masters can wait. "
                  "&ldquo;Many workmen could not subsist a week, few could subsist a "
                  "month, and scarce any a year, without employment.&rdquo; He grants that "
                  "&ldquo;In the long run, the workman may be as necessary to his master as "
                  "his master is to him; but the necessity is not so immediate.&rdquo;"),
            ("p", "The next claim is the one critics have asked for evidence of. We "
                  "rarely hear of the masters combining, Smith says, and people take that "
                  "to mean they rarely do: &ldquo;Masters are always and everywhere in a "
                  "sort of tacit, but constant and uniform, combination, not to raise the "
                  "wages of labour above their actual rate.&rdquo; We do not hear of it "
                  "&ldquo;because it is the usual, and, one may say, the natural state of "
                  "things, which nobody ever hears of.&rdquo; An argument from silence is "
                  "exactly what a sceptic will hesitate over, and Smith supplies no "
                  "figures; what he offers is an account of how a market with few "
                  "buyers of labour and many sellers would behave. He gives the workmen's "
                  "side with equal plainness: their combinations are loud, sometimes "
                  "violent, and &ldquo;generally end in nothing but the punishment or ruin "
                  "of the ringleaders&rdquo;. He praises neither."),
            ("def", ("Natural wages and the lowest rate",
                     "Smith's <em>natural</em> wage in this chapter is the usual one, as "
                     "in the last: what the contract commonly gives. The lowest rate is a "
                     "floor beneath it, the wage that just maintains the labourer and "
                     "his family.")),
            ("p", "There is a floor. &ldquo;A man must always live by his work, and his "
                  "wages must at least be sufficient to maintain him.&rdquo; More, because "
                  "he must bring up a family. Smith then reports, in the third person, a "
                  "guess by the Irish-French banker Richard Cantillon: that the lowest "
                  "common labourers &ldquo;must everywhere earn at least double their own "
                  "maintenance&rdquo;, so that one with another they can raise two children, "
                  "the wife's labour being no more than enough for herself. Since half the "
                  "children die before manhood, four must be borne to rear two, and four "
                  "children cost about as much as one man. Smith keeps his distance: "
                  "&ldquo;I shall not take upon me to determine&rdquo; the proportion. "
                  "What he will say is that wages in the circumstances he goes on to describe "
                  "can rise &ldquo;considerably above this rate, evidently the lowest which "
                  "is consistent with common humanity&rdquo;."),
            ("p", "The lab sets the figures against each other, and the figures are in "
                  "pence a week. Smith reports later in the chapter (l. 2521 to 2534) that "
                  "Lord Chief Justice Hales reckoned the expense of a labourer's family of "
                  "six, the father and mother, two children able to do something and two "
                  "not able, at ten shillings a week, which is 120 pence, and that both he "
                  "and Gregory King, in 1688, supposed the weekly expense to be &ldquo;about "
                  "twenty-pence a-head&rdquo;. In the lab's three presets that is the "
                  "family's need: 20 pence for the father, 20 for the mother, 40 for the two "
                  "children who can do something and 40 for the two who cannot. The "
                  "Cantillon check uses 20 pence as one man's maintenance, which is the "
                  "lesson's assumption, and a multiple of two. Three wages follow. The "
                  "highland preset has Smith's &ldquo;Three shillings a-week&rdquo;, 36 pence, "
                  "still paid in some parts of the Highlands. The lowland preset has eight "
                  "pence a day, the usual wage in the Low country of Scotland, and the london "
                  "preset eighteen pence a day, which Smith calls the common price in London "
                  "and its neighbourhood; both are taken at six days, an assumption of the "
                  "lesson, so 48 and 108 pence. The wage is the labourer's alone, so the "
                  "shortfall against the whole family is what his wife and children "
                  "would have to earn."),
            ("p", "On the highland wage, 36 pence against 120, the shortfall is 84 pence, "
                  "and against Cantillon's minimum of 40 it is 4 pence short. On the lowland "
                  "wage of 48 the family is short by 72 and Cantillon's minimum is covered "
                  "with 8 to spare. On the london wage of 108 the family is short by only "
                  "12 and the minimum is covered by 68. Two cautions. Hales wrote in the "
                  "time of Charles II, and Smith says that both the income and the expense "
                  "of such families have increased considerably since, so his 120 pence is "
                  "an older figure set against wages of the 1770s. And the same family's "
                  "needs are used in all three places, which the lab does not price "
                  "separately: the presets compare each wage with one stated need, not the "
                  "cost of living in the Highlands, the Lowlands and London."),
            ("p", "Later economists made the floor into something firmer than Smith "
                  "does. Ricardo, in 1817, held that the natural price of labour is the "
                  "price that enables labourers to subsist and to perpetuate their race, "
                  "and that wages tend to it; Malthus supplied the population mechanism "
                  "behind that. Marx, in the Capital lesson <em>The Buying and Selling of "
                  "Labour-Power</em>, makes the worker's means of subsistence the measure of "
                  "the value of labour-power, with a historical and moral element. Smith's "
                  "own sentence leaves more room than any of them: the floor is the lowest "
                  "the wage can be, not the wage, and the rest of the chapter argues that "
                  "in a country advancing in wealth it is a good deal above it."),
            ("p", "The next lesson, <em>The Funds Destined for Maintaining Labour</em>, "
                  "asks what lifts the wage above the floor."),
        ],
        "lab": ("wonkit", {
            "mode": "wages",
            "view": "subsistence",
            "money_unit": "d",
            "period": "week",
            "preset": "highland",
            "presets": [
                {"id": "highland", "label": "Hales's family at Smith's Highland wage, three shillings a week",
                 "items": [["father", 20], ["mother", 20],
                           ["two-children-able-to-work", 40],
                           ["two-children-not-able", 40]],
                 "wage": 36, "maintenance": 20, "multiple": 2, "expect": {
                    "wwgFamily": "120d a week",
                    "wwgCover": "falls short by 84d",
                    "wwgMinimum": "40d a week (2 × 20d)",
                    "wwgCoverMin": "falls short by 4d",
                 }},
                {"id": "lowland", "label": "The same family at eight pence a day for six days",
                 "items": [["father", 20], ["mother", 20],
                           ["two-children-able-to-work", 40],
                           ["two-children-not-able", 40]],
                 "wage": 48, "maintenance": 20, "multiple": 2, "expect": {
                    "wwgFamily": "120d a week",
                    "wwgCover": "falls short by 72d",
                    "wwgMinimum": "40d a week (2 × 20d)",
                    "wwgCoverMin": "covers it, with 8d over",
                 }},
                {"id": "london", "label": "The same family at eighteen pence a day for six days",
                 "items": [["father", 20], ["mother", 20],
                           ["two-children-able-to-work", 40],
                           ["two-children-not-able", 40]],
                 "wage": 108, "maintenance": 20, "multiple": 2, "expect": {
                    "wwgFamily": "120d a week",
                    "wwgCover": "falls short by 12d",
                    "wwgMinimum": "40d a week (2 × 20d)",
                    "wwgCoverMin": "covers it, with 68d over",
                 }},
            ],
            "panel_title": "A wage against a family's needs",
            "panel_intro": (
                "A family's weekly needs and one wage go in, with a man's own maintenance and "
                "Cantillon's multiple. The lab totals the needs, sets the wage beside them, "
                "and sets it beside the multiple of one man's maintenance."
            ),
        }),
        "steps_title": "Setting a wage against a subsistence",
        "steps_intro": "Four steps, for any family whose needs are listed.",
        "steps": [
            ("List the needs for one period",
             "Put a cost on each person or item for the same week. Smith's source gives "
             "about twenty pence a head, so the family of six costs 120 pence a week."),
            ("Compare the wage",
             "Subtract the total from the wage. A positive answer is what covers the family; "
             "a negative one is what others in the household must earn."),
            ("Find Cantillon's minimum",
             "Multiply one man's maintenance by Cantillon's multiple, two. With 20 pence, "
             "that is 40 pence a week."),
            ("Compare the wage with it",
             "A wage above the minimum leaves the labourer able, on Cantillon's reasoning, to "
             "rear two children to manhood. Below it he is short of the lowest "
             "rate he gave."),
        ],
        "worked": {
            "title": "A Highland wage against Hales's family",
            "intro": [
                "Take the highland preset: the wage is Smith's three shillings a week, which "
                "is 36 pence.",
            ],
            "lines": [
                "family:  20 + 20 + 40 + 40 = 120 d a week",
                "wage:  3 · 12 = 36 d",
                "short by:  120 − 36 = 84 d",
                "Cantillon's minimum:  2 · 20 = 40 d",
                "wage against it:  36 − 40 = −4 d",
            ],
            "after": [
                "The wage is 4 pence under the minimum and 84 under the whole family's needs. "
                "In the lowland preset the wage of 48 pence is above the minimum by 8, and "
                "in the london preset by 68, though the whole family's needs are still not "
                "met by the father's wage alone.",
            ],
        },
        "quiz_title": "Wages, masters and the floor",
        "quiz": [
            {"q": "On Cantillon's guess as Smith reports it, a labourer whose own maintenance "
                  "is 20 pence a week must earn at least how much?",
             "a": ["20 pence", "40 pence", "80 pence", "120 pence"],
             "c": 1,
             "why": "&ldquo;at least double their own maintenance&rdquo;, so 2 · 20 = 40 pence. "
                    "20 pence maintains the man alone and leaves nothing for children. 120 "
                    "pence is Hales's figure for the whole family of six, a different "
                    "estimate, and 80 is not in the passage."},
            {"q": "Hales put a labourer's family of six at ten shillings a week. What is that "
                  "a head, in pence?",
             "a": ["10", "12", "60", "20"],
             "c": 3,
             "why": "Ten shillings is 120 pence, and 120 / 6 = 20, which is the &ldquo;about "
                    "twenty-pence a-head&rdquo; Smith says Hales and Gregory King both "
                    "supposed. Ten is the shillings, and 12 is the pence in one shilling."},
            {"q": "Why, in Smith's account, do we seldom hear of the masters' combination?",
             "a": ["Because masters never combine",
                   "Because the law forbids it and so it is kept secret",
                   "Because it is the usual and natural state of things, which nobody ever hears of",
                   "Because the masters are too few to combine"],
             "c": 2,
             "why": "&ldquo;We seldom, indeed, hear of this combination, because it is the "
                    "usual, and, one may say, the natural state of things, which nobody ever "
                    "hears of.&rdquo; Smith says the law authorises, or at least does not "
                    "prohibit, the masters' combinations, and that the masters are fewer in "
                    "number, which is why they can combine more easily."},
            {"q": "Which of these does Smith give as a reason why masters have the advantage "
                  "in a dispute about wages?",
             "a": ["A master could generally live a year or two on stock already acquired, while "
                   "few workmen could subsist a month",
                   "The masters are paid in coin and the workmen in goods",
                   "Workmen are forbidden to work for another master",
                   "The masters own the cottages the workmen live in"],
             "c": 0,
             "why": "&ldquo;A landlord, a farmer, a master manufacturer, or merchant, though "
                    "they did not employ a single workman, could generally live a year or "
                    "two upon the stocks, which they have already acquired.&rdquo; The other "
                    "answers are not reasons he gives."},
        ],
        "mistakes": [
            ("Reading the floor as the wage",
             "Smith calls the subsistence rate &ldquo;evidently the lowest which is "
             "consistent with common humanity&rdquo;, and goes on to argue that in Great "
             "Britain wages are well above it. The chapter is about what raises "
             "them above it, so the floor is where it starts."),
            ("Thinking Smith takes the workmen's side",
             "He says the masters have the advantage and the law favours them, and he also "
             "says the workmen's combinations are violent and usually end in ruin for "
             "their leaders. What he asserts is a description of the bargain, with both "
             "parties' faults in it."),
            ("Setting a family's whole needs against a man's wage",
             "The lab compares the wage with the whole family's needs, which is the "
             "comparison Hales makes, but the wife's and the children's earnings are "
             "part of the household's income. Cantillon's multiple is a rule for the man's "
             "wage alone, and the two checks answer different questions."),
        ],
        "standard": (
            "Finish when you can set a wage against a family's needs and against Cantillon's minimum.",
            "Given a family's weekly needs, a wage, one man's maintenance and a multiple, "
            "compute the shortfall or surplus against the whole family and against the "
            "minimum, and say which of the two Smith's text speaks of."
        ),
        "note": (
            "The twenty pence a head, the six working days and the assumption that a man's "
            "maintenance is one head's share are not Smith's own sums: the first is "
            "Hales's and King's as he reports them, the other two are written for the "
            "lesson. The lab cannot say what any real household earned or spent, whether "
            "masters in fact combined as Smith says, or whether Cantillon's reasoning is "
            "sound. Those are what Smith, Ricardo, Malthus and Marx dispute."
        ),
    },
    # ---------------------------------------------------------------- 02
    # PSU text l. 2242-2265 (the funds); l. 2266-2315 (North America); l.
    # 2316-2367 (China); l. 2368-2389 (Bengal); l. 2390-2396 (the symptom).
    {
        "slug": "the-funds-destined-for-maintaining-labour",
        "title": "The Funds Destined for Maintaining Labour",
        "module": "Book I, Chapter 8 · Of the Wages of Labour",
        "one_line": "Wages rise with the increase of the funds that employ labour, not with their size: the thriving poor country pays more than the stationary rich one.",
        "summary": (
            "What raises wages above the floor is a demand for labour that keeps "
            "growing, and Smith says that demand grows with the funds destined for the "
            "payment of wages: revenue over what maintains its owner, and stock over what "
            "employs its master. A rich country that stands still pays little; a poor one "
            "that grows pays much. Compute a wage as a fund divided by a number of "
            "workers, over years, for a country that stands, grows, crowds or declines."
        ),
        "key": [
            "demand for labour follows the funds for wages",
            "not the size of wealth, its increase",
            "wage = fund / workers, in the lab",
            "standing: low; thriving: high; declining: bare",
        ],
        "key_label": "What raises wages",
        "concepts_intro": (
            "Smith's answer to what lifts the wage above the floor is short, and he "
            "spends the rest of the section on three countries to show it."
        ),
        "concepts": [
            ("The funds destined for wages",
             "The demand for those who live by wages can increase only as the funds "
             "destined to pay them increase. Smith names two: the revenue over what "
             "maintains its owner, which a landlord or annuitant spends on servants, and the "
             "stock over what employs its master, with which a weaver takes on "
             "journeymen."),
            ("Increase, not size",
             "&ldquo;It is not the actual greatness of national wealth, but its continual "
             "increase, which occasions a rise in the wages of labour.&rdquo; England is "
             "richer than North America, and pays less. China is richer still, and pays "
             "the least."),
            ("Progressive, stationary, declining",
             "Wages are liberal in a country that is growing, scanty in one that is at a "
             "stand and bare in one that is going backwards. Smith takes North America, "
             "China and Bengal as the three cases."),
        ],
        "read_title": "Three countries and one rule",
        "read_intro": (
            "This is the middle third of Chapter 8, and every paragraph is an example of "
            "the sentence that opens it."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 8.</strong> &ldquo;The demand for those who "
                  "live by wages, it is evident, cannot increase but in proportion to the "
                  "increase of the funds which are destined to the payment of "
                  "wages.&rdquo;"),
            ("p", "Smith has just said what happens when the demand for such people is "
                  "continually increasing: the masters bid against one another and break "
                  "through their tacit combination, so that the workmen have no need to "
                  "combine. Now he says where the demand comes from. The funds are of two "
                  "kinds, &ldquo;first, the revenue which is over and above what is "
                  "necessary for the maintenance; and, secondly, the stock which is over "
                  "and above what is necessary for the employment of their masters.&rdquo; "
                  "A landlord with a revenue larger than he needs for his family employs "
                  "menial servants with the surplus. A weaver or shoemaker with more stock "
                  "than he needs to buy his materials and keep himself until the work sells "
                  "takes on journeymen with it. Increase the surplus and he increases the "
                  "number. So the demand for those who live by wages increases with the "
                  "revenue and stock of the country and cannot increase without it."),
            ("p", "And then the sentence the lesson is named for: &ldquo;It is not the "
                  "actual greatness of national wealth, but its continual increase, which "
                  "occasions a rise in the wages of labour.&rdquo; North America is the first "
                  "case. It is poorer than England, but &ldquo;The wages of labour, however, "
                  "are much higher in North America than in any part of England.&rdquo; Smith "
                  "gives figures from the province of New York in 1773: common labourers "
                  "earned &ldquo;three shillings and sixpence currency, equal to two "
                  "shillings sterling, a-day&rdquo;, above the London price, with provisions "
                  "much cheaper than in England, so that the real wage is higher still in "
                  "proportion. And the population there doubles in twenty or five-and-twenty "
                  "years, where in Great Britain it is not supposed to double in less than "
                  "five hundred. The next lesson takes that up."),
            ("p", "The stationary case is China. &ldquo;Though the wealth of a country "
                  "should be very great, yet if it has been long stationary, we must not "
                  "expect to find the wages of labour very high in it.&rdquo; The funds may "
                  "be of the greatest extent, but if they have stayed of much the same size "
                  "for centuries the labourers already employed could easily supply the "
                  "number wanted next year. &ldquo;The hands, on the contrary, would, in this "
                  "case, naturally multiply beyond their employment,&rdquo; and the labourers "
                  "would bid against one another, until wages sank to the lowest rate "
                  "consistent with common humanity. China, he says, is one of the "
                  "richest countries and has been long stationary; &ldquo;The accounts of "
                  "all travellers, inconsistent in many other respects, agree in the low wages "
                  "of labour&rdquo;. He is relying on travellers, Marco Polo among them, and "
                  "the picture he draws of the poverty of the lower ranks is a harrowing one."),
            ("p", "The third case is the declining one, and Smith's example is Bengal. "
                  "Where the funds for maintaining labour are decaying, each year's demand "
                  "for servants and labourers is less than the year before. People bred to "
                  "the superior classes seek work in the lowest, which is already full, and "
                  "the competition drives wages to the most miserable subsistence; many "
                  "cannot find work even on those terms, and &ldquo;Want, famine, and "
                  "mortality, would immediately prevail in that class&rdquo; until the "
                  "number of the people is reduced to what the remaining revenue and stock "
                  "can maintain. &ldquo;This, perhaps, is nearly the present state of Bengal&rdquo;, "
                  "and he adds that in a fertile country where &ldquo;three or four hundred "
                  "thousand people die of hunger in one year&rdquo; the funds for the labouring "
                  "poor must be fast decaying. He puts the difference between North America and Bengal down "
                  "to the government of each, the British constitution against the mercantile "
                  "company that &ldquo;oppresses and domineers in the East Indies&rdquo;. "
                  "&ldquo;The liberal reward of labour, therefore, as it is the necessary "
                  "effect, so it is the natural symptom of increasing national "
                  "wealth.&rdquo;"),
            ("p", "The lab turns the rule into a sum, and the sum is the lab's: it takes the "
                  "wage in a year to be the fund divided by the number of workers, which "
                  "Smith never writes. A fund in pounds a year and a number of workers "
                  "go in, with a rate of growth for each, and the lab runs them for a number "
                  "of years. Each year's number of workers is not rounded to a whole person, "
                  "since the lab treats it as a rate of population. In the still preset a "
                  "rich country has a fund of £10,000 a year and 1,000 workers and neither "
                  "grows, so the wage is £10 in every one of thirty years. In the thriving "
                  "preset a poorer country has £600 and 100 workers, a wage of £6, and the "
                  "fund grows five per cent a year against three for the workers. After "
                  "thirty years the wage is about £10.68, above the rich country's £10. "
                  "In the crowded preset the fund stays at £1,000 and the 100 workers grow "
                  "two per cent a year: after ten years the wage is about £8.20. In the "
                  "declining preset the fund of £1,000 falls four per cent a year while "
                  "the 100 workers still grow one per cent, as a people goes on multiplying "
                  "for a time after the funds begin to decay and the lowest class fills "
                  "with the overflow of the others: after ten years the fund is about "
                  "£664.83 and the wage about £6.02. All four are written for the lesson, "
                  "and nothing here is Smith's figure."),
            ("p", "What the lab leaves out matters. Smith's wage is not a quotient. He says "
                  "the demand for labour determines what the masters have to offer, as "
                  "when they bid against each other, and in the stationary case the "
                  "competition of the labourers drives it down to a floor that he names. "
                  "The lab has no floor, so the crowded and declining wages go on falling "
                  "for as many years as you run them, which is a reason to read them as "
                  "the direction of a force and not a forecast. Later economists made the "
                  "quotient into a doctrine. John Stuart Mill, in 1848, took the wages fund "
                  "as the share of capital destined to pay labour, a quantity fixed at "
                  "any moment, so that a rise in one group's wages must come out of "
                  "another's. Francis Longe and William Thornton attacked it in the 1860s, "
                  "and Mill gave it up in a review of Thornton's book in 1869. Marx, in the "
                  "Capital lesson <em>The Reserve Army of Labour</em>, argues that "
                  "the demand for labour does not rise in step with accumulation."),
            ("p", "His evidence also has critics. Smith's China is the China of "
                  "travellers' reports, and historians since, Kenneth Pomeranz among them, "
                  "have argued that its economy was in important ways not stationary. His "
                  "Bengal is a few years after the famine of 1770, which he does not name. "
                  "The lesson does not decide either point. It reads Smith's argument, "
                  "which is that the wage follows the increase of the funds."),
            ("p", "The next lesson, <em>The Liberal Reward of Labour</em>, reads "
                  "the rest of Chapter 8: what the liberal reward does to the number "
                  "and the industry of the people."),
        ],
        "lab": ("wonkit", {
            "mode": "wages",
            "view": "fund",
            "money_unit": "£",
            "preset": "thriving",
            "presets": [
                {"id": "still", "label": "A rich country that stands still, written for this lesson",
                 "fund": 10000, "workers": 1000, "fund_growth": 0, "worker_growth": 0,
                 "years": 30, "expect": {
                    "wwgWageFirst": "£10 a worker",
                    "wwgWageLast": "£10 a worker (year 30)",
                    "wwgTrend": "the wage holds: the fund and the workers grow at the same rate",
                    "wwgFundLast": "£10,000",
                 }},
                {"id": "thriving", "label": "A poorer country growing at five and three per cent, written for this lesson",
                 "fund": 600, "workers": 100, "fund_growth": 5, "worker_growth": 3,
                 "years": 30, "expect": {
                    "wwgWageFirst": "£6 a worker",
                    "wwgWageLast": "≈ £10.68 a worker (year 30)",
                    "wwgTrend": "the wage rises every year: the fund grows faster than the workers",
                    "wwgFundLast": "≈ £2,593.17",
                 }},
                {"id": "crowded", "label": "A stationary fund and multiplying hands, written for this lesson",
                 "fund": 1000, "workers": 100, "fund_growth": 0, "worker_growth": 2,
                 "years": 10, "expect": {
                    "wwgWageFirst": "£10 a worker",
                    "wwgWageLast": "≈ £8.20 a worker (year 10)",
                    "wwgTrend": "the wage falls every year: the workers grow faster than the fund",
                    "wwgFundLast": "£1,000",
                 }},
                {"id": "declining", "label": "A fund falling four per cent a year while the workers still grow one, written for this lesson",
                 "fund": 1000, "workers": 100, "fund_growth": -4, "worker_growth": 1,
                 "years": 10, "expect": {
                    "wwgWageFirst": "£10 a worker",
                    "wwgWageLast": "≈ £6.02 a worker (year 10)",
                    "wwgTrend": "the wage falls every year: the workers grow faster than the fund",
                    "wwgFundLast": "≈ £664.83",
                 }},
            ],
            "panel_title": "A wage from a fund and a number of workers",
            "panel_intro": (
                "The fund for maintaining labour, the number of workers and the yearly "
                "growth of each go in. The lab prints each year's fund, workers and wage "
                "and says whether the wage rises, holds or falls."
            ),
        }),
        "steps_title": "Following a wage over the years",
        "steps_intro": "Five steps, with the lab's rule that the wage is the fund per worker.",
        "steps": [
            ("Enter the fund and the workers",
             "The fund is what the country sets aside a year to maintain labour, and the "
             "workers are those it employs. The first year's wage is the one over the other."),
            ("Enter the two growth rates",
             "A percentage a year for the fund and one for the workers. A negative rate is "
             "a decline."),
            ("Multiply each year",
             "The fund and the workers are each multiplied by one plus their rate, once a "
             "year, with no rounding."),
            ("Divide",
             "Each year's wage is that year's fund divided by that year's workers."),
            ("Compare first and last",
             "The wage rises when the fund grows faster than the workers, holds when they "
             "grow alike, and falls when the workers grow faster. The size of the fund does "
             "not enter the comparison."),
        ],
        "worked": {
            "title": "A crowded country, ten years",
            "intro": [
                "Take the crowded preset: the fund stays at £1,000 and 100 workers grow two "
                "per cent a year. The wage is shown to two places.",
            ],
            "lines": [
                "year 0:  1000 / 100 = 10",
                "year 1:  1000 / (100 · 1.02) = 9.80",
                "year 2:  1000 / (100 · 1.02 · 1.02) = 9.61",
                "year 10:  1000 / (100 · 1.02^10) = 8.20",
            ],
            "after": [
                "The fund never changed, and the wage fell by about a fifth in ten years. Make "
                "the fund grow two per cent as well and the wage stays at £10: the comparison "
                "is between the growth rates, not between the amounts.",
            ],
        },
        "quiz_title": "The funds for maintaining labour",
        "quiz": [
            {"q": "In the thriving preset the fund grows five per cent a year and the workers "
                  "three per cent. What happens to the wage?",
             "a": ["It falls, because there are more workers",
                   "It stays at £6, because the fund is small",
                   "It rises, because the fund grows faster than the workers",
                   "It cannot be known without the size of the fund"],
             "c": 2,
             "why": "Wage = fund / workers, so it rises when the fund's growth rate exceeds "
                    "the workers'. The lab's wage goes from £6 to about £10.68 in thirty "
                    "years. The size of the fund is what the answer does not depend on, and "
                    "the number of workers growing does not make the wage fall when the "
                    "fund is growing faster."},
            {"q": "Which of these does Smith give as the two kinds of fund destined for the "
                  "payment of wages?",
             "a": ["Rent and taxes",
                   "Revenue over what maintains its owner, and stock over what employs its master",
                   "Gold and silver in circulation",
                   "The produce of the land and of the sea"],
             "c": 1,
             "why": "&ldquo;first, the revenue which is over and above what is necessary for "
                    "the maintenance; and, secondly, the stock which is over and above what "
                    "is necessary for the employment of their masters.&rdquo; The "
                    "others are not in the passage."},
            {"q": "Smith says wages are higher in North America than in England. What does "
                  "he give as the reason?",
             "a": ["North America is the richer country",
                   "North America is poorer, so labour is scarce",
                   "North American masters are more generous",
                   "North America is the more thriving, advancing faster to further riches"],
             "c": 3,
             "why": "&ldquo;though North America is not yet so rich as England, it is much "
                    "more thriving, and advancing with much greater rapidity to the further "
                    "acquisition of riches.&rdquo; England is the richer, and he does not "
                    "say the Americans are kinder."},
            {"q": "What does Smith say of the wages of labour in a country that has long been "
                  "stationary, however great its wealth?",
             "a": ["We must not expect to find them very high",
                   "They are the highest in the world",
                   "They are fixed by law",
                   "They rise slowly with its size"],
             "c": 0,
             "why": "&ldquo;Though the wealth of a country should be very great, yet if it "
                    "has been long stationary, we must not expect to find the wages of labour "
                    "very high in it.&rdquo; His example is China."},
        ],
        "mistakes": [
            ("Taking a rich country to pay high wages",
             "Smith's sentence is that the actual greatness of national wealth does not "
             "raise wages, its continual increase does. In the lab the still preset's fund "
             "is nearly seventeen times the thriving preset's, and its wage in thirty years "
             "is lower."),
            ("Reading wage = fund / workers as Smith's own formula",
             "He writes that the demand for labour follows the funds and that the "
             "competition of masters and of labourers settles the wage. The quotient is the "
             "lab's way of showing the direction. It has no floor, no bargaining and "
             "no time lag, and a later school made it a doctrine that Mill himself gave up."),
            ("Reading China and Bengal as measured facts",
             "China is Smith's from travellers' accounts and Bengal from the reports of his "
             "own day, which he does not cite, and later historians have disputed the first and said more about "
             "the second. The lesson reports the argument Smith builds on them."),
        ],
        "standard": (
            "Finish when you can say whether a wage rises, holds or falls from a fund and a number of workers.",
            "Given a fund and a number of workers with their yearly growth rates, compute "
            "the wage each year and say whether it rises, holds or falls, and what in "
            "Smith's text the comparison stands for."
        ),
        "note": (
            "All four countries are written for the lesson. The lab shows only what the "
            "quotient does when two rates differ; it has no floor, no population "
            "response, and it cannot say whether the funds of a real country grew at the "
            "rates in a preset. Whether wages follow the funds as Smith says, and what "
            "the funds are, is the argument the wages-fund controversy took up."
        ),
    },
    # ---------------------------------------------------------------- 03
    # PSU text l. 2397-2403 (wages in Britain above the lowest); l. 2404-2445
    # (the four symptoms); l. 2486-2571 (the last century, Hales, King, real
    # wages); l. 2572-2582 (advantage to society); l. 2583-2638 (poverty and
    # population); l. 2639-2664 (freemen and slaves); l. 2665-2723 (industry,
    # overwork); l. 2724-2813 (dear and cheap years: skipped in outline);
    # l. 2814-2869 (the two circumstances; the closing paragraph).
    {
        "slug": "the-liberal-reward-of-labour",
        "title": "The Liberal Reward of Labour",
        "module": "Book I, Chapter 8 · Of the Wages of Labour",
        "one_line": "A liberal reward of labour is the effect of increasing wealth and the cause of increasing population, and it makes the people industrious.",
        "summary": (
            "In the last third of Chapter 8 Smith asks what high wages do. They let the "
            "poor rear more of the children they bear, so that the number of people follows "
            "the demand for them; they raise the industry of the common people, or "
            "sometimes overwork it; and they raise some prices while the improvements they "
            "bring lower others. Work the doubling of a population at Smith's twenty or "
            "five-and-twenty years, and at the pace he gives for Europe."
        ),
        "key": [
            "demand for men regulates the making of men",
            "liberal wages are effect and cause of wealth",
            "population doubles in 2^(years / doubling)",
            "wages encourage industry, until they overwork",
        ],
        "key_label": "The liberal reward in four lines",
        "concepts_intro": (
            "Smith turns from the cause of high wages to their consequences, and his "
            "argument is a circle he means to be read as a virtuous one."
        ),
        "concepts": [
            ("Population follows demand",
             "Poverty does not prevent births but kills the children, and every species "
             "multiplies in proportion to its means of subsistence. A liberal reward lets "
             "more children grow up, and Smith says it does so as nearly as possible in "
             "the proportion the demand for labour requires, so demand for men regulates "
             "their production like any other commodity's."),
            ("Effect and cause",
             "High wages are the effect of increasing wealth and the cause of increasing "
             "population and industry. &ldquo;To complain of it, is to lament over the "
             "necessary cause and effect of the greatest public prosperity.&rdquo;"),
            ("Industry and its limits",
             "Good pay animates and strengthens, and Smith says workmen are more active "
             "where wages are high. Paid by the piece, they can overwork themselves; "
             "moderation, he says, gets the most in the year."),
        ],
        "read_title": "What a liberal reward does",
        "read_intro": (
            "This is a long stretch of the chapter, and it moves among evidence, "
            "argument and moral judgment. The lesson takes the argument about population "
            "in full and the rest in outline."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 8.</strong> &ldquo;It is in this manner that "
                  "the demand for men, like that for any other commodity, necessarily "
                  "regulates the production of men, quickens it when it goes on too slowly, "
                  "and stops it when it advances too fast.&rdquo;"),
            ("p", "The sentence closes an argument that starts well before it. Smith has "
                  "first shown, from a long run of evidence, that wages in Great Britain "
                  "are above the lowest rate. Summer wages, when the family is cheapest to "
                  "keep, are always highest; the money wage of labour does not follow the "
                  "price of provisions from year to year, nor from place to place, so that "
                  "in London it is eighteen pence a day and a few miles off fourteen or "
                  "fifteen. The Scottish day-wage has risen from sixpence in summer and "
                  "fivepence in winter in the last century to eightpence now, and he "
                  "adds that the real recompence has risen more than the money one, "
                  "as potatoes, turnips and coarse cloth have grown cheaper. He asks "
                  "whether this improvement is good for society and answers at once: "
                  "&ldquo;No society can surely be flourishing and happy, of which the far "
                  "greater part of the members are poor and miserable.&rdquo; The lesson "
                  "does not follow the long list of evidence, which is the proof "
                  "that British wages stand above the floor."),
            ("p", "Now the argument. &ldquo;Poverty, though it no doubt discourages, does "
                  "not always prevent, marriage.&rdquo; It may even favour births: "
                  "&ldquo;A half-starved Highland woman frequently bears more than twenty "
                  "children, while a pampered fine lady is often incapable of bearing any&rdquo;. "
                  "But poverty is hard on the rearing of them. &ldquo;It is not "
                  "uncommon, I have been frequently told, in the Highlands of Scotland, for a "
                  "mother who has born twenty children not to have two alive.&rdquo; "
                  "These are anecdotes, with a few reports of officers and foundling "
                  "hospitals behind them, and Smith says that he has been told them, but "
                  "they carry his claim: &ldquo;Every species of animals naturally multiplies "
                  "in proportion to the means of their subsistence, and no species can ever "
                  "multiply beyond it.&rdquo; In a civilised society only the lowest ranks "
                  "meet that limit, and the limit works by destroying children."),
            ("p", "A liberal reward moves the limit, because it lets the poor provide "
                  "better for their children and so bring up more of them. And it does so, "
                  "Smith says, in the proportion that the demand requires. If the reward is "
                  "too low, the shortage of hands raises it; if too high, the excessive "
                  "multiplication lowers it. The market is understocked with labour in "
                  "the one case and overstocked in the other, &ldquo;as would soon force "
                  "back its price to that proper rate which the circumstances of the society "
                  "required.&rdquo; That is why the demand regulates propagation in "
                  "North America, where it is rapidly progressive, in Europe, where it is "
                  "slow, and in China, where it is stationary. It is the same argument as "
                  "Chapter 7's, applied to people: a quantity brought to market, a natural "
                  "rate, a reward that calls more or fewer into being."),
            ("p", "The lab does the arithmetic of the doubling. Smith says the "
                  "British colonies in North America &ldquo;double in twenty or "
                  "five-and-twenty years&rdquo; and that Great Britain and most of Europe "
                  "&ldquo;are not supposed to double in less than five hundred years&rdquo;. "
                  "A population that doubles every <em>d</em> years is multiplied by two "
                  "for each <em>d</em> years, so after <em>t</em> years it has been multiplied by "
                  "2 raised to the power <em>t</em>/<em>d</em>. The lab insists that <em>t</em> be a whole "
                  "multiple of <em>d</em>, because a part of a doubling needs a root it "
                  "does not take. The colonies preset takes 100,000 people, an arbitrary "
                  "starting figure written for the lesson, over a hundred years at the "
                  "two doubling times: at 25 years that is four doublings and a "
                  "factor of 16, 1,600,000 people; at 20 years it is five doublings and a "
                  "factor of 32, 3,200,000. The europe preset takes the same 100,000 over "
                  "two hundred years. The lab will not take a doubling time over 200 years, "
                  "so it cannot enter Smith's five hundred; at 200 years there is one "
                  "doubling and a factor of 2, 200,000 people, and at 25 years there are "
                  "eight doublings and a factor of 256, which is 25,600,000 people. That is "
                  "not a prediction, and Smith makes none; it is why he ties the rate to "
                  "the demand for labour and not to nature alone."),
            ("p", "Malthus, writing in 1798 after Smith's death, took the same facts "
                  "and drew the opposite warning. He argued that population, when unchecked, "
                  "doubles every twenty-five years, that subsistence cannot be made to grow "
                  "so fast, and that a rise of wages that raises marriage therefore raises "
                  "numbers until want brings it back. Smith has the doubling in twenty or "
                  "five-and-twenty years, and he has the check, but he describes "
                  "an adjustment that regulates itself, where Malthus sees a pressure. "
                  "Marx, in the Capital lesson <em>The Reserve Army of Labour</em>, "
                  "argues that each historical mode of production has its own law of "
                  "population."),
            ("p", "Smith's other claims in this stretch take the argument into the "
                  "workplace. Free labour, he says, comes cheaper in the end than slaves': "
                  "the fund for replacing a slave's wear and tear is managed by a "
                  "&ldquo;negligent master or careless overseer&rdquo;, and the one for a "
                  "freeman by the freeman himself, so &ldquo;the work done by freemen comes "
                  "cheaper in the end than that performed by slaves&rdquo;. It is a claim "
                  "about cost, and economic historians since, Robert Fogel and Stanley "
                  "Engerman among them, have argued that the record of the American "
                  "plantations does not bear it out. He adds that a progressive society is the "
                  "happiest: &ldquo;The progressive state is, in reality, the cheerful and the "
                  "hearty state to all the different orders of the society; the stationary "
                  "is dull; the declining melancholy.&rdquo;"),
            ("p", "On industry, Smith holds that &ldquo;The wages of labour are the "
                  "encouragement of industry, which, like every other human quality, "
                  "improves in proportion to the encouragement it receives.&rdquo; Workmen "
                  "are more active in England than Scotland and near great towns than in "
                  "remote places. Then he qualifies it. Paid liberally by the piece they "
                  "overwork themselves: &ldquo;A carpenter in London, and in some other "
                  "places, is not supposed to last in his utmost vigour above eight "
                  "years&rdquo;, and soldiers set to piece-work had to be stopped from earning "
                  "above a certain sum a day. The idleness of the three days is, he "
                  "says, the result of too much on the other four: &ldquo;Excessive "
                  "application, during four days of the week, is frequently the real cause "
                  "of the idleness of the other three, so much and so loudly complained "
                  "of.&rdquo; The master who is wise will moderate, because &ldquo;the man "
                  "who works so moderately, as to be able to work constantly, not only "
                  "preserves his health the longest, but, in the course of the year, "
                  "executes the greatest quantity of work.&rdquo;"),
            ("p", "He then spends some pages on the old belief that workmen are more "
                  "industrious in dear years than in cheap ones. He says it is "
                  "commended by masters, who make better bargains in dear years, and by "
                  "landlords and farmers, whose rents and profits rise with the price of "
                  "provisions. He cites the French author Messance, whose figures from the "
                  "registers of three stationary French manufactures show more goods made in "
                  "cheap years than in dear, and finds no sensible connection either way in "
                  "the growing manufactures of Scotland and Yorkshire. The lesson passes this over: "
                  "it is evidence for a question the lab does not take, and the full "
                  "argument is on the pages."),
            ("p", "The chapter ends by joining wages back to prices. The money price of "
                  "labour is regulated by two circumstances, &ldquo;the demand for labour, and "
                  "the price of the necessaries and conveniencies of life&rdquo;, and a "
                  "rise in wages raises the prices of many commodities. But the same "
                  "increase of stock that raises wages makes labour more productive, "
                  "through divisions of employment and better machinery, so that many "
                  "commodities come to be produced by so much less labour that &ldquo;the "
                  "increase of its price is more than compensated by the diminution of its "
                  "quantity&rdquo;. Chapter 9 takes up profit, and its last pages take up "
                  "Smith's claim that a rise of profit raises prices more than a rise of "
                  "wages, which is the fifth lesson of this course."),
            ("p", "The next lesson, <em>The Profits of Stock</em>, reads Chapter 9, "
                  "which asks the same questions of profit that this chapter asked of "
                  "wages."),
        ],
        "lab": ("wonkit", {
            "mode": "wages",
            "view": "growth",
            "preset": "colonies",
            "presets": [
                {"id": "colonies", "label": "100,000 people over a hundred years, doubling in 25 or in 20; population written for this lesson",
                 "population": 100000, "doubling": 25, "doubling2": 20, "years": 100,
                 "expect": {
                    "wwgDoublings": "4",
                    "wwgAfter": "1,600,000",
                    "wwgTimes": "16×",
                    "wwgCompare": "in 100 years: every 25 years 16×, every 20 years 32× (3,200,000); the second ends 2× the first",
                 }},
                {"id": "europe", "label": "100,000 people over two hundred years, doubling in 200 (the lab's slowest) or in 25; population written for this lesson",
                 "population": 100000, "doubling": 200, "doubling2": 25, "years": 200,
                 "expect": {
                    "wwgDoublings": "1",
                    "wwgAfter": "200,000",
                    "wwgTimes": "2×",
                    "wwgCompare": "in 200 years: every 200 years 2×, every 25 years 256× (25,600,000); the second ends 128× the first",
                 }},
            ],
            "panel_title": "A population that doubles",
            "panel_intro": (
                "A population, a time to double and a number of years go in; the years must be "
                "a whole multiple of the doubling time. A second doubling time may be added "
                "for comparison."
            ),
        }),
        "steps_title": "Counting doublings",
        "steps_intro": "Four steps, for any doubling time that divides the years.",
        "steps": [
            ("Enter the doubling time and the years",
             "Smith gives the time as twenty or five-and-twenty years for the colonies and "
             "five hundred for Europe. The years must be a whole multiple of it."),
            ("Count the doublings",
             "Doublings = years / doubling time. A hundred years at 25 is four."),
            ("Multiply",
             "The factor is two multiplied by itself that many times: 2^4 = 16."),
            ("Compare a second doubling time",
             "The same years at twenty give five doublings and 32; the ratio of the two "
             "populations is two to the difference of the doublings."),
        ],
        "worked": {
            "title": "A hundred years in the colonies",
            "intro": [
                "Take the colonies preset: 100,000 people, doubling in 25 years or in 20, "
                "over 100 years.",
            ],
            "lines": [
                "doublings at 25:  100 / 25 = 4",
                "factor:  2^4 = 16",
                "population:  100000 · 16 = 1600000",
                "doublings at 20:  100 / 20 = 5",
                "population:  100000 · 2^5 = 3200000",
            ],
            "after": [
                "The five-year difference in the doubling time makes the population twice as "
                "large in a century. The lab does not say what makes a population double "
                "in 20 or 25 years; Smith says it is the demand for labour.",
            ],
        },
        "quiz_title": "The reward of labour and the numbers of the people",
        "quiz": [
            {"q": "A population of 100,000 doubles every 25 years. How many are there after "
                  "100 years?",
             "a": ["400,000", "800,000", "1,600,000", "3,200,000"],
             "c": 2,
             "why": "100 years is four doublings, and 2^4 = 16, so 1,600,000. 400,000 is "
                    "only two doublings and 800,000 three, and 3,200,000 is the answer if "
                    "the population doubles every 20 years."},
            {"q": "In Smith's account, what happens if the reward of labour is at any time "
                  "more than the demand for labour requires?",
             "a": ["The excessive multiplication of labourers soon lowers it",
                   "Masters at once raise it further",
                   "Wages are fixed by law",
                   "Nothing, for wages and numbers are not connected"],
             "c": 0,
             "why": "&ldquo;If the reward should at any time be less than what was requisite "
                    "for this purpose, the deficiency of hands would soon raise it; and if "
                    "it should at any time be more, their excessive multiplication would "
                    "soon lower it to this necessary rate.&rdquo;"},
            {"q": "Which sentence is Smith's verdict on complaints about the high wages of the "
                  "poor?",
             "a": ["They show that luxury has spread to the lowest ranks and should be taxed",
                   "They are justified only for workmen paid by the piece",
                   "They are justified when provisions are cheap",
                   "To complain of it is to lament over the necessary cause and effect of the "
                   "greatest public prosperity"],
             "c": 3,
             "why": "&ldquo;To complain of it, is to lament over the necessary cause and "
                    "effect of the greatest public prosperity.&rdquo; He reports the complaint "
                    "that luxury reaches the lowest ranks, and counts it as evidence that "
                    "real wages have risen, not as a ground for a tax."},
            {"q": "What does Smith say about workmen paid liberally by the piece?",
             "a": ["They are the most idle of all",
                   "They are apt to overwork themselves and ruin their health in a few years",
                   "They work the same hours as day-workers",
                   "They are always content with a smaller wage"],
             "c": 1,
             "why": "Workmen paid liberally by the piece &ldquo;are very apt to overwork "
                    "themselves, and to ruin their health and "
                    "constitution in a few years&rdquo;. The London carpenter, he says, is "
                    "not supposed to last in his utmost vigour above eight years."},
        ],
        "mistakes": [
            ("Reading the doubling time as a law of nature",
             "Smith gives it as what has been found in the colonies and says it follows "
             "from the liberal reward. The europe preset's eight doublings in two hundred "
             "years show what a rate of 25 years does when held fixed: a figure "
             "nobody takes for a forecast."),
            ("Thinking Smith says high wages make people idle",
             "He says the reverse: they raise industry. What he warns of is overwork, when "
             "the pay is by the piece, and the pretence that dear years make the poor "
             "industrious, which he does not accept."),
            ("Taking his anecdotes for statistics",
             "The Highland mother, the officers' drums and fifes, the carpenter who lasts "
             "eight years, are things he says he has been told. They carry his case "
             "but are not measurements, and later demography has replaced them."),
        ],
        "standard": (
            "Finish when you can compute a population after a number of doublings.",
            "Given a population, a doubling time and a number of years, count the "
            "doublings, compute the population after them, and compare two doubling "
            "times, and say what in Smith's text sets the doubling time."
        ),
        "note": (
            "The population in the lab is written for the lesson, and the doubling times "
            "are Smith's as reports of what had been found. The lab can count doublings "
            "but cannot say whether the demand for labour regulates population as Smith "
            "says, or whether it rests on poverty's mortality as he describes; that is "
            "what Malthus, and later demographers and Marx, take up. His claims about "
            "slaves, about industry and about dear years are not computed at all."
        ),
    },
    # ---------------------------------------------------------------- 04
    # PSU text l. 2870-2898 (profit hard to know); l. 2899-2924 (interest as
    # the index; the legal rates, l. 2909-2917); l. 2925-3014 (Scotland,
    # France, Holland); l. 3015-3096 (colonies, new territory, Bengal);
    # l. 3097-3150 (full complement of riches; China; the law and interest);
    # l. 3151-3203 (clear profit; double interest, l. 3187-3198).
    {
        "slug": "the-profits-of-stock",
        "title": "The Profits of Stock",
        "module": "Book I, Chapter 9 · Of the Profits of Stock",
        "one_line": "Profit is too fluctuating to measure, so Smith reads it from the rate of interest, and finds it falling as a country's stock grows.",
        "summary": (
            "Chapter 9 asks of profit what Chapter 8 asked of wages. Smith says the rise and "
            "fall of profit depend on the same causes, though they act on it the other way: "
            "the increase of stock that raises wages tends to lower profit. Since profit "
            "cannot be known, he follows the interest of money, and reports the legal rate "
            "at 10, 8, 6 and 5 per cent. Compute what double interest, the merchants' rule "
            "of thumb, implies about profit at each rate."
        ),
        "key": [
            "stock grows: wages tend up, profit down",
            "profit is unknowable; interest is its index",
            "legal rates followed the market rate",
            "double interest: a reasonable profit",
        ],
        "key_label": "The profits of stock",
        "concepts_intro": (
            "Three ideas hold the chapter: a method, a trend and a rule of proportion."
        ),
        "concepts": [
            ("Interest as the index of profit",
             "Profit varies &ldquo;not only from year to year, but from day to day, and almost from hour "
             "to hour&rdquo;, and no one can tell you his own average. Interest is a "
             "plain figure, and Smith lays down that where a great deal can be made by "
             "the use of money a great deal will commonly be given for it, so that "
             "the interest of money and the profits of stock rise and sink together."),
            ("Stock and the falling rate",
             "&ldquo;The increase of stock, which raises wages, tends to lower "
             "profit.&rdquo; When many rich merchants turn their stocks into the same "
             "trade their competition lowers its profit, and when the same happens in all "
             "trades it lowers profit in all. High wages and high profits scarcely "
             "ever go together, except in new colonies."),
            ("Clear profit and double interest",
             "Smith distinguishes the gross profit from the clear profit that is left "
             "after the occasional losses of any employment. Interest can be afforded only "
             "out of the clear. The merchants' rule is that double interest is a "
             "reasonable profit, so about half of it goes to the lender."),
        ],
        "read_title": "Interest first, then what it says of profit",
        "read_intro": (
            "This is most of Chapter 9: the first three-quarters on how profit moves and the "
            "last on how it divides. The long comparisons among Scotland, France, Holland "
            "and the colonies are read in outline."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 9.</strong> &ldquo;It may be laid down as a "
                  "maxim, that wherever a great deal can be made by the use of money, a great "
                  "deal will commonly be given for the use of it&rdquo;."),
            ("p", "He needs the maxim because the thing he wants to measure cannot be "
                  "measured. &ldquo;Profit is so very fluctuating, that the person who carries "
                  "on a particular trade, cannot always tell you himself what is the average "
                  "of his annual profit.&rdquo; The average of all the trades of a "
                  "kingdom must be harder, and the profits of a remote period he calls "
                  "&ldquo;altogether impossible&rdquo; to judge. But the rate of interest is "
                  "known, and as it varies we may be assured that profit varies with it. "
                  "Smith then traces the rate through the statutes. Interest above ten "
                  "per cent was made unlawful in the reign of Henry VIII; ten per cent "
                  "continued to be the legal rate until James I, when it was restricted to "
                  "eight; soon after the Restoration it was reduced to six; under Queen Anne "
                  "to five. He does not read them as the laws acting on the market. "
                  "&ldquo;All these different statutory regulations seem to have been made "
                  "with great propriety. They seem to have followed, and not to have gone "
                  "before, the market rate of interest.&rdquo; Before the late war, he adds, "
                  "the government borrowed at three per cent."),
            ("p", "Over that same period, he says, the wealth and revenue of the country "
                  "have been advancing faster and faster, and the wages of labour have "
                  "risen while in the greater part of the different branches of trade and "
                  "manufactures &ldquo;the profits of stock have been diminishing&rdquo;. The reason is "
                  "the one in the second concept above: the competition of larger and "
                  "larger stocks. He sees it between town and country too, where a great "
                  "town needs a greater stock to carry on any trade, and the wages are "
                  "higher and the profit lower than in a remote village."),
            ("p", "The lab applies the merchants' rule to those four rates. The legal preset "
                  "has Smith's four legal rates of interest, 10, 8, 6 and 5 per cent, and "
                  "multiplies each by two. The multiplication is the lab's. Smith reports "
                  "double interest as what merchants call reasonable and does not apply "
                  "it to the older rates or to any other. If it held, the profit implied is "
                  "20, 16, 12 and 10 per cent, a fall of 10 points, half of the first. That "
                  "is an illustration of what the rule would say about the series, and "
                  "Smith does not state the series himself."),
            ("p", "He is not, though, offering a theory of how fast profit falls. Holland "
                  "is his example of a country far along: &ldquo;the Dutch, it is well "
                  "known, trade upon lower profits than any people in Europe.&rdquo; The "
                  "government there borrows at two per cent and private people of good "
                  "credit at three. When Dutch merchants complain that trade decays he "
                  "answers that &ldquo;the diminution of profit is the natural effect of its "
                  "prosperity, or of a greater stock being employed in it than before&rdquo;, "
                  "and points to their large lending abroad as a sign that stock has "
                  "outgrown the business at home and not that the business has shrunk. A "
                  "great stock with small profits, he says, generally grows faster than a "
                  "small stock with great profits: &ldquo;Money, says the proverb, makes "
                  "money.&rdquo;"),
            ("p", "The exceptions are worth the space they take. In the colonies, he "
                  "says, &ldquo;High wages of labour and high profits of stock, however, are "
                  "things, perhaps, which scarce ever go together, except in the peculiar "
                  "circumstances of new colonies&rdquo;, where land is cheap and stock is "
                  "scarce, interest runs from six to eight per cent, and the planter must "
                  "bid high for hands. New territory or a new branch of trade may raise "
                  "profits for a time in a country that is growing rich, by drawing stock "
                  "from other trades and lessening competition in them. And where stock is "
                  "falling, wages fall and profits rise: in Bengal &ldquo;money is "
                  "frequently lent to the farmers at forty, fifty, and sixty per cent.&rdquo;, "
                  "and in China twelve per cent &ldquo;is said to be the common interest "
                  "of money&rdquo;, because the oppression of the poor establishes the monopoly of "
                  "the rich. The rule of the chapter is a rule of tendency, with reasons "
                  "for each case when it fails."),
            ("p", "At the end Smith separates clear profit from gross. &ldquo;The lowest "
                  "ordinary rate of profit must always be something more than what is "
                  "sufficient to compensate the occasional losses to which every employment "
                  "of stock is exposed. It is this surplus only which is neat or clear "
                  "profit.&rdquo; Interest can be afforded only out of the clear. Then the "
                  "merchants' rule: &ldquo;Double interest is in Great Britain reckoned what "
                  "the merchants call a good, moderate, reasonable profit; terms which, I "
                  "apprehend, mean no more than a common and usual profit.&rdquo; He applies "
                  "it with a limit: &ldquo;In a country where the ordinary rate of clear "
                  "profit is eight or ten per cent. it may be reasonable that one half of it "
                  "should go to interest&rdquo;, since the borrower runs the risk and takes "
                  "the trouble, and four or five per cent may be enough for both. The "
                  "half preset has those two cases, interest 5 against a profit of 10 and "
                  "interest 4 against a profit of 8, and leaves 5 and 4 per cent for the "
                  "borrower. The lesson puts them in that order, as one country whose clear "
                  "profit falls from ten to eight per cent as its stock grows, so the "
                  "first-to-last tile reads interest 5% → 4% (−1 point) against implied "
                  "profit 10% → 8% (−2 points): with half to the lender, interest falls by "
                  "half as many points as profit. The order is the lesson's; Smith gives "
                  "the two rates as alternatives. He adds at once that the proportion &ldquo;might not be the "
                  "same in countries where the ordinary rate of profit was either a good deal "
                  "lower, or a good deal higher.&rdquo; Bengal, at forty per cent interest, is "
                  "not a case of double interest."),
            ("p", "David Hume had argued in 1752 that the rate of interest depends on the "
                  "rate of profit and not on the quantity of money, and Smith builds on that. "
                  "The Capital lesson <em>The Rate of Interest</em> argues that no law "
                  "fixes where interest lies between nothing and profit, which is a "
                  "point against taking either rate as the index of the other. Ricardo "
                  "agreed that profit falls as stock increases, but gave a different reason: "
                  "that the cost of food rises as worse land is tilled, and wages take more "
                  "of the produce. Marx's own account of a falling rate of profit is the "
                  "Capital lesson <em>The Falling Rate of Profit: The Law as Such</em>. "
                  "Smith's reason, competition among stocks, is the one the others "
                  "set aside."),
            ("p", "The lesson passes over the long comparisons among Scotland, France and "
                  "Holland beyond what is said above, the French reductions of interest "
                  "between 1720 and 1766, and the paragraphs on the lender in the Roman "
                  "provinces and the effect of the law on usury. The next lesson, "
                  "<em>High Profits Raise Prices More than High Wages</em>, reads the last "
                  "page of the chapter."),
        ],
        "lab": ("wonkit", {
            "mode": "interest",
            "view": "profit",
            "preset": "legal",
            "presets": [
                {"id": "legal", "label": "Smith's legal rates of interest; double interest is the lab's rule",
                 "rows": [["Henry-VIII", 10, 2],
                          ["James-I", 8, 2],
                          ["after-the-Restoration", 6, 2],
                          ["Queen-Anne", 5, 2]],
                 "expect": {
                    "witImplied": "Henry-VIII 10% × 2 = 20%; James-I 8% × 2 = 16%; after-the-Restoration 6% × 2 = 12%; Queen-Anne 5% × 2 = 10%",
                    "witFall": "interest 10% → 5% (−5 points); implied profit 20% → 10% (−10 points)",
                 }},
                {"id": "half", "label": "Smith's ten or eight per cent profit with half to interest, taken as a fall (the order written for this lesson)",
                 "rows": [["profit-ten-per-cent", 5, 2, 10],
                          ["profit-eight-per-cent", 4, 2, 8]],
                 "expect": {
                    "witImplied": "profit-ten-per-cent 5% × 2 = 10%; profit-eight-per-cent 4% × 2 = 8%",
                    "witLeft": "profit-ten-per-cent 10% − 5% = 5%; profit-eight-per-cent 8% − 4% = 4%",
                    "witFall": "interest 5% → 4% (−1 point); implied profit 10% → 8% (−2 points)",
                 }},
            ],
            "panel_title": "What interest implies about profit",
            "panel_intro": (
                "Each period's rate of interest goes in, with the multiple that gives "
                "profit (two for double interest) and, where it is known, a stated "
                "profit. The lab prints the implied profit, what is left after interest, "
                "and the fall from the first period to the last."
            ),
        }),
        "steps_title": "Reading profit from interest",
        "steps_intro": "Four steps, with the merchants' rule as the lab applies it.",
        "steps": [
            ("List the rates of interest",
             "Take them in order of time or place. Smith's legal rates are 10, 8, 6 and 5 "
             "per cent."),
            ("Apply the multiple",
             "Implied profit = interest · multiple. Double interest gives a multiple of two."),
            ("Subtract interest from a stated profit",
             "Where a profit is stated, what is left after interest is the profit minus the "
             "interest. With 8 per cent profit and 4 per cent interest, 4 is left."),
            ("Compare the first with the last",
             "The fall is the first implied profit minus the last, in points, and the same "
             "as a share of the first."),
        ],
        "worked": {
            "title": "Double interest on the legal rates",
            "intro": [
                "Take the legal preset: four rates of interest and a multiple of two.",
            ],
            "lines": [
                "Henry VIII:  2 · 10 = 20 per cent",
                "James I:  2 · 8 = 16 per cent",
                "Restoration:  2 · 6 = 12 per cent",
                "Anne:  2 · 5 = 10 per cent",
                "fall:  20 − 10 = 10 points, half of the first",
            ],
            "after": [
                "The implied profit falls by half over the series. The result is only as "
                "good as the multiple of two, which Smith says is what merchants call "
                "reasonable and applies only to countries where profit is eight or ten per "
                "cent.",
            ],
        },
        "quiz_title": "Profit, interest and stock",
        "quiz": [
            {"q": "On the merchants' rule of double interest, what profit does the legal rate "
                  "of five per cent under Queen Anne imply?",
             "a": ["5 per cent", "10 per cent", "12 per cent", "20 per cent"],
             "c": 1,
             "why": "Implied profit = 2 · 5 = 10 per cent. Five is the interest itself, 12 "
                    "is the implied profit at the 6 per cent of the Restoration, and 20 is "
                    "the implied profit at the 10 per cent of Henry VIII."},
            {"q": "What does Smith say the increase of stock does to wages and to profit?",
             "a": ["Raises both",
                   "Lowers both",
                   "Raises wages and tends to lower profit",
                   "Lowers wages and raises profit"],
             "c": 2,
             "why": "&ldquo;The increase of stock, which raises wages, tends to lower "
                    "profit.&rdquo; The reverse holds when the funds for maintaining industry "
                    "diminish: &ldquo;as it lowers the wages of labour, so it raises the "
                    "profits of stock&rdquo;."},
            {"q": "Where does Smith say high wages and high profits are found together?",
             "a": ["In Holland", "In China", "In Bengal", "In new colonies"],
             "c": 3,
             "why": "&ldquo;High wages of labour and high profits of stock, however, are "
                    "things, perhaps, which scarce ever go together, except in the peculiar "
                    "circumstances of new colonies.&rdquo; Holland has high wages and low "
                    "profits; China and Bengal have low wages and high profits."},
            {"q": "In a country where the ordinary rate of clear profit is eight or ten per "
                  "cent, how much of it does Smith say it may be reasonable to give to "
                  "interest?",
             "a": ["One half of it", "All of it", "One tenth of it", "Twice as much as the profit"],
             "c": 0,
             "why": "&ldquo;it may be reasonable that one half of it should go to interest, "
                    "wherever business is carried on with borrowed money&rdquo;, which is four "
                    "or five per cent. He adds that the proportion might differ where profit "
                    "was a good deal lower or higher."},
        ],
        "mistakes": [
            ("Treating double interest as a law",
             "Smith reports it as what merchants call a reasonable profit, and applies it only "
             "where clear profit is eight or ten per cent. The lab's multiple is a parameter "
             "you can change; at the forty per cent of Bengal Smith himself says the "
             "interest eats up most of the profit."),
            ("Reading falling profit as decay",
             "He says the opposite: &ldquo;the diminution of profit is the natural effect of "
             "its prosperity&rdquo;. Merchants who complain that trade decays when profits "
             "fall are mistaking a sign of growth for one of decline."),
            ("Thinking the statutes set the rate",
             "The statutes of 10, 8, 6 and 5 per cent &ldquo;followed, and not to have gone "
             "before, the market rate of interest&rdquo;. The lab's series is the legal rate "
             "because the legal rate is what Smith lists, and he takes it as evidence of the "
             "market."),
        ],
        "standard": (
            "Finish when you can read an implied profit and a share left to the borrower from a rate of interest.",
            "Given rates of interest and a multiple, compute the implied profit for each "
            "and its fall over the series, and with a stated profit compute what is left "
            "after interest."
        ),
        "note": (
            "Smith's legal rates are his; the lab's double interest is applied to them "
            "for illustration, and he does not apply it. The lab cannot say whether profit "
            "and interest move together as he assumes, whether profit in fact fell, "
            "or why: Hume, Ricardo and Marx each answer that differently."
        ),
    },
    # ---------------------------------------------------------------- 05
    # PSU text l. 3204-3208 (low profit compensates high wages); l.
    # 3209-3237 (high profits raise the price of work more than high wages).
    {
        "slug": "high-profits-raise-prices",
        "title": "High Profits Raise Prices More Than High Wages",
        "module": "Book I, Chapter 9 · Of the Profits of Stock",
        "one_line": "A rise of wages adds to a price like simple interest; a rise of profit, charged on the price at every stage, adds like compound interest.",
        "summary": (
            "In the last page of Chapter 9 Smith answers the masters who blame high wages "
            "for dear goods. Through the stages of a linen manufacture a rise of wages "
            "raises the price by the sum of the rises, but a rise of profit is charged on "
            "everything advanced, including earlier profits, and so raises it faster. Run "
            "a four-stage chain with a wage rise, a profit rise and both."
        ),
        "key": [
            "wage rise: adds, like simple interest",
            "profit rise: compounds through the stages",
            "profit is charged on the price advanced",
            "merchants blame wages and not profit",
        ],
        "key_label": "A page in four lines",
        "concepts_intro": (
            "The page is short, and its whole argument is the contrast of two kinds of "
            "interest."
        ),
        "concepts": [
            ("Wages rise in arithmetical proportion",
             "If every working person in the linen manufacture is paid twopence a day more, "
             "the price of a piece rises by the number of people who worked on it times "
             "the number of days. The part of price that is wages rises by that sum and "
             "no more."),
            ("Profit rises in geometrical proportion",
             "If every employer's profit is raised by five per cent, each requires the "
             "five per cent on the whole value of what he advanced, which already "
             "includes the profits of those before him. Each stage's rise sits on the "
             "last."),
            ("The merchants' complaint",
             "Masters complain that high wages raise prices and lessen sales. They are "
             "silent, Smith says, about the effect of high profits, which are their "
             "own."),
        ],
        "read_title": "Simple interest and compound interest",
        "read_intro": (
            "The page is one example. Read it slowly, because every phrase counts "
            "something."),
        "body": [
            ("p", "<strong>Book I, Chapter 9.</strong> &ldquo;In reality, high profits tend "
                  "much more to raise the price of work than high wages.&rdquo;"),
            ("p", "Smith has just said that in countries fast advancing to riches the low "
                  "rate of profit may, in the price of many commodities, &ldquo;compensate the "
                  "high wages of labour, and enable those countries to sell as cheap as their "
                  "less thriving neighbours, among whom the wages of labour may be "
                  "lower.&rdquo; Now he gives the reason for the claim, in one example. "
                  "Suppose, in the linen manufacture, that the wages of the flax-dressers, "
                  "the spinners and the weavers should all be advanced twopence a day. "
                  "&ldquo;it would be necessary to heighten the price of a piece of linen "
                  "only by a number of twopences equal to the number of people that had "
                  "been employed about it, multiplied by the number of days during which "
                  "they had been so employed.&rdquo; In his words, the part of the price "
                  "that resolved itself into wages would &ldquo;rise only in arithmetical "
                  "proportion to this rise of wages&rdquo;."),
            ("p", "Now raise the profits of all the employers by five per cent instead. "
                  "&ldquo;The employer of the flax dressers would, in selling his flax, "
                  "require an additional five per cent. upon the whole value of the "
                  "materials and wages which he advanced to his workmen.&rdquo; The employer "
                  "of the spinners would require it on the advanced price of the flax, which "
                  "now includes the flax-dresser's extra, and on the spinners' wages. The "
                  "weaver's employer would require it on the advanced price of the yarn "
                  "and on the weavers' wages. So the part that resolves itself into profit "
                  "would &ldquo;rise in geometrical proportion to this rise of profit&rdquo;. "
                  "He puts the contrast as an image of debt: &ldquo;In raising the price of "
                  "commodities, the rise of wages operates in the same manner as simple "
                  "interest does in the accumulation of debt. The rise of profit operates like "
                  "compound interest.&rdquo;"),
            ("p", "The lab runs the same sort of chain, with figures written for the "
                  "lesson. It has four stages: a flax-grower, who pays £100 in wages and "
                  "£40 in rent, then the flax-dresser at £30 in wages, the spinner at £60 "
                  "and the weaver at £90, all at ten per cent profit. In the base preset "
                  "the price after the weaver is about £416.50 (exactly £416.504), of which the "
                  "wages are £280, the rent £40 and the profit about £96.50. The lab raises "
                  "wages by a percentage and profit by a number of points, and it does not use "
                  "Smith's twopence a day. A ten per cent rise in every wage, in the wages "
                  "preset, adds £28 to the wages and makes the price about £452.30, a rise of "
                  "about £35.79. A five-point rise in profit, in the profit preset, from ten "
                  "to fifteen per cent, leaves the wages at £280 and makes the price about "
                  "£473.34, a rise of about £56.83. Both together, in the both preset, make about £513.67, a rise "
                  "of about £97.17. That the profit rise is the bigger here depends on the "
                  "numbers chosen for the lesson: it is not what Smith claims. What he claims "
                  "is the shape. The lab splits the profit rise in two. Charged on the "
                  "old advances of the four stages, five points come to about £48.25. The "
                  "other £8.58 or so is profit charged on the extra profits of the stages "
                  "before, which is the compounding. The wage rise is added once; the profit "
                  "rise is added at every stage on top of what came before, so the longer the "
                  "chain, the more it compounds."),
            ("p", "There is a wrinkle in the arithmetic that Smith does not stop on. In the "
                  "lab, a rise in wages does more than add its own amount: in the wages preset "
                  "the wages part rises by £28, from £280 to £308, and the price by about £35.79, "
                  "because the employer also reckons his ordinary profit on the extra wages "
                  "he has to advance. The difference, about £7.79, is that extra profit, and it "
                  "belongs to the profit part of the price, not to the wages part. Smith's "
                  "sentence about arithmetical proportion is about the wages part only, "
                  "so it holds on the lab's own figures: £28 added once. But it leaves "
                  "open what a wage rise does to the whole price."),
            ("p", "He ends the chapter with the merchants. &ldquo;Our merchants "
                  "and master manufacturers complain much of the bad effects of high wages "
                  "in raising the price, and thereby lessening the sale of their goods, "
                  "both at home and abroad. They say nothing concerning the bad effects of "
                  "high profits; they are silent with regard to the pernicious effects of "
                  "their own gains; they complain only of those of other people.&rdquo; It is "
                  "one of the sentences in the book where Smith does not hide on which "
                  "side his suspicion falls: the interest of the people who live by profit "
                  "is not that of the public, as Book I will say again at the end of its "
                  "last chapter. The lesson only says what it says. Whether the merchants of "
                  "1776 did or did not complain in the way he describes is a question the "
                  "lab cannot answer."),
            ("p", "Ricardo challenged the conclusion. He held, in 1817, that a general rise "
                  "of wages does not raise the prices of commodities, since their values "
                  "depend on the labour they cost, and falls instead on profit. The Capital "
                  "lesson <em>Wage Changes and Prices of Production</em> works Marx's "
                  "version of the question, in which a general wage rise lowers the general "
                  "rate of profit and moves prices differently in different lines. Smith "
                  "is not answering either, since he died in 1790, but the question they "
                  "ask is the one his page leaves: whether a price can be a sum of parts "
                  "that are free to move one at a time."),
            ("p", "The next course, <em>Wages and Profit in Different Employments</em>, "
                  "reads Chapter 10, which asks why wages and profits differ from one "
                  "trade to another."),
        ],
        "lab": ("wonkit", {
            "mode": "price",
            "view": "parts",
            "money_unit": "£",
            "preset": "base",
            "presets": [
                {"id": "base", "label": "A linen chain at ten per cent, written for this lesson",
                 "stages": [["flax-grower", 100, 40, 10],
                            ["flax-dresser", 30, 0, 10],
                            ["spinner", 60, 0, 10],
                            ["weaver", 90, 0, 10]],
                 "wage_rise": 0, "profit_rise": 0, "expect": {
                    "wprFinal": "≈ £416.50",
                 }},
                {"id": "wages", "label": "Every wage up ten per cent",
                 "stages": [["flax-grower", 100, 40, 10],
                            ["flax-dresser", 30, 0, 10],
                            ["spinner", 60, 0, 10],
                            ["weaver", 90, 0, 10]],
                 "wage_rise": 10, "profit_rise": 0, "expect": {
                    "wprFinal": "≈ £416.50",
                    "wprWageRise": "≈ £416.50 → ≈ £452.30: ≈ +£35.79 (+1,627/18,932 ≈ +8.6%); wages paid +£28",
                 }},
                {"id": "profit", "label": "Every rate of profit up five points",
                 "stages": [["flax-grower", 100, 40, 10],
                            ["flax-dresser", 30, 0, 10],
                            ["spinner", 60, 0, 10],
                            ["weaver", 90, 0, 10]],
                 "wage_rise": 0, "profit_rise": 5, "expect": {
                    "wprFinal": "≈ £416.50",
                    "wprProfitRise": "≈ £416.50 → ≈ £473.34: ≈ +£56.83 (+454,665/3,332,032 ≈ +13.6%); profit on the old advances ≈ +£48.25",
                 }},
                {"id": "both", "label": "Wages up ten per cent and profit up five points",
                 "stages": [["flax-grower", 100, 40, 10],
                            ["flax-dresser", 30, 0, 10],
                            ["spinner", 60, 0, 10],
                            ["weaver", 90, 0, 10]],
                 "wage_rise": 10, "profit_rise": 5, "expect": {
                    "wprFinal": "≈ £416.50",
                    "wprWageRise": "≈ £416.50 → ≈ £452.30: ≈ +£35.79 (+1,627/18,932 ≈ +8.6%); wages paid +£28",
                    "wprProfitRise": "≈ £416.50 → ≈ £473.34: ≈ +£56.83 (+454,665/3,332,032 ≈ +13.6%); profit on the old advances ≈ +£48.25",
                    "wprBothRise": "≈ £416.50 → ≈ £513.67: ≈ +£97.17 (+1,554,733/6,664,064 ≈ +23.3%)",
                 }},
            ],
            "panel_title": "A wage rise and a profit rise through the stages",
            "panel_intro": (
                "The stages of a price, as in the lesson Wages, Profit and Rent, here a "
                "linen chain written for this lesson, with a rise in wages (a percentage) "
                "and a rise in the rate of profit (points) applied to every stage. The lab prints the new price and the rise that each causes."
            ),
        }),
        "steps_title": "Comparing a wage rise with a profit rise",
        "steps_intro": "Four steps, on the same chain of stages.",
        "steps": [
            ("Price the chain as it stands",
             "Stage price = (price bought + wages + rent) · (1 + rate), stage by stage, as "
             "in the lesson Wages, Profit and Rent."),
            ("Raise the wages",
             "Raise every stage's wages by the same percentage and price the chain again. "
             "The wages part rises by that percentage of the wage total."),
            ("Raise the rate of profit",
             "Add the same number of points to every stage's rate and price the chain "
             "again. Each stage charges the extra on everything it bought and advanced."),
            ("Compare the rises",
             "Set the rise caused by each against the base price. The wage rise adds once; "
             "the profit rise adds at each stage on the stage before, so it grows with "
             "the number of stages."),
        ],
        "worked": {
            "title": "A five-point rise in profit, stage by stage",
            "intro": [
                "Take the profit preset: the rate goes from 10 to 15 per cent at every stage "
                "of the linen chain.",
            ],
            "lines": [
                "grower:  (0 + 100 + 40) · 1.15 = 161",
                "dresser:  (161 + 30) · 1.15 = 219.65",
                "spinner:  (219.65 + 60) · 1.15 = 321.5975",
                "weaver:  (321.5975 + 90) · 1.15 = 473.337125",
                "rise:  473.337125 − 416.504 = 56.833125",
            ],
            "after": [
                "Wages are still £280, and the whole rise is in the profit part, which "
                "goes from £96.504 to £153.337125. The extra five per cent is charged "
                "on a larger price at each stage.",
            ],
        },
        "quiz_title": "Simple and compound",
        "quiz": [
            {"q": "Why does Smith say a rise of profit operates like compound interest?",
             "a": ["Because profit is always larger than wages",
                   "Because masters agree among themselves to raise prices",
                   "Because profits are paid yearly",
                   "Because each employer's extra profit is charged on the whole advanced price, "
                   "which already holds the extra profits of those before him"],
             "c": 3,
             "why": "The employer of the spinners would require his additional five per "
                    "cent on the advanced price of the flax as well as on the wages of "
                    "the spinners, and the price of the flax already includes the "
                    "flax-dresser's extra. The size of profit relative to wages does not "
                    "enter the argument."},
            {"q": "On the lab's linen chain, which raises the final price more: every wage "
                  "up ten per cent, or every rate of profit up five points?",
             "a": ["The wage rise, by about £35.79",
                   "The profit rise, by about £56.83",
                   "Both raise it by the same",
                   "Neither changes it"],
             "c": 1,
             "why": "The wage rise takes the price from £416.504 to £452.298, which is "
                    "£35.794 more. The profit rise takes it to £473.337125, which is "
                    "£56.833125 more. This depends on the chain's figures, which are written "
                    "for the lesson, and not on a general rule."},
            {"q": "Smith says a rise of wages raises the part of the price that resolves "
                  "itself into wages in what way?",
             "a": ["In arithmetical proportion", "In geometrical proportion",
                   "Not at all", "By more than the rise of profit would"],
             "c": 0,
             "why": "&ldquo;That part of the price of the commodity which resolved itself "
                    "into the wages, would, through all the different stages of the "
                    "manufacture, rise only in arithmetical proportion to this rise of "
                    "wages.&rdquo; Geometrical is his word for the rise of profit."},
            {"q": "What does Smith say of the complaints of merchants and master manufacturers?",
             "a": ["They complain of high profits but not of wages",
                   "They complain of both equally",
                   "They complain of the bad effects of high wages and say nothing of those "
                   "of high profits",
                   "They never complain"],
             "c": 2,
             "why": "&ldquo;They say nothing concerning the bad effects of high profits; "
                    "they are silent with regard to the pernicious effects of their own "
                    "gains; they complain only of those of other people.&rdquo;"},
        ],
        "mistakes": [
            ("Saying Smith denies that high wages raise prices",
             "He says they do, by increasing the part of price that resolves itself into "
             "wages; the same page says that high wages are compensated by low profit in "
             "a thriving country. His claim is that profit raises prices more, in "
             "the way each is added."),
            ("Taking the lab's comparison as a general result",
             "In the lab the profit rise is larger because of the figures: wages of £280 "
             "in a chain of four stages, and a rise of five points. Choose a short chain or "
             "a small profit rise and the comparison can reverse. The shape, adding against "
             "compounding, is what holds."),
            ("Equating the lab's ten per cent with Smith's twopence a day",
             "Smith's rise is a flat sum for every working person; the lab raises each "
             "wage by a percentage, so the stages with larger wages rise more. It "
             "illustrates the argument without reproducing the example."),
        ],
        "standard": (
            "Finish when you can price a chain of stages with a wage rise and with a profit rise.",
            "Given the wages, rent and rate of profit at each stage, compute the price "
            "with a rise of wages, with a rise of the rate of profit and with both, and "
            "say which part of the price rises in arithmetical and which in geometrical "
            "proportion."
        ),
        "note": (
            "The chain's figures are written for the lesson and the rises are the lab's. "
            "The lab cannot say whether a general rise of wages in fact raises prices or "
            "falls on profit, which is where Ricardo and Marx part from the page, nor "
            "what happened to the merchants' complaints. It shows only what the rule of "
            "the chapter does to a price built by it."
        ),
    },
]
