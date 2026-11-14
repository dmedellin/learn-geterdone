"""Wages and Profit in Different Employments, lessons 1-5 -- Book I, Chapter 10.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt
(the Electronic Classics Series edition of the Inquiry); the comment beside each
lesson gives its line numbers. Smith's spelling is kept inside quotations. Where
the extraction jams or breaks a word across a line, the word is joined as a
printed book would print it.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # PSU text l. 3241-3251 (the whole of the advantages), l. 3266-3273 (the
    # five circumstances), l. 3282-3287 (honour, the butcher), l. 3306-3316
    # (the expensive machine), l. 3367-3380 (masons), l. 3396-3416 (colliers
    # and coal-heavers), l. 3421-3430 (trust).
    {
        "slug": "the-five-circumstances",
        "title": "The Five Circumstances",
        "module": "Book I, Chapter 10, Part I · Inequalities from the Nature of the Employments",
        "one_line": "Wages differ from trade to trade, Smith says, because five circumstances make up for a small money gain in one trade and cancel a large one in another.",
        "summary": (
            "Chapter 10 opens with a claim: in one neighbourhood, with men free to choose, "
            "the whole of the advantages of different employments tends to equality, while "
            "their money wages are far from equal. Part I names the five circumstances that "
            "explain the gap. Take four trades with very different pay, add what each one "
            "costs or gives besides money, and see how the net advantages come out level."
        ),
        "key": [
            "money wage = wage a day × days worked",
            "learning, a year = cost / years + profit",
            "whole advantage = wage − learning + other",
            "free choice tends to level net advantage",
            "a high wage may be pay for a bad circumstance",
        ],
        "key_label": "The first four circumstances in five lines",
        "concepts_intro": (
            "The chapter is long and most of it is examples. Its argument is short, and the "
            "examples are there to make you believe it."
        ),
        "concepts": [
            ("The whole of the advantages",
             "Smith does not say wages are equal. He says that the whole of the advantages "
             "and disadvantages of different employments, money and everything else that "
             "belongs to a trade, must in one neighbourhood be equal or tending to equality, "
             "because people move out of the worse and into the better. The equality is of "
             "the whole, and the money is one part of it."),
            ("Five circumstances",
             "What the money has to make up for: how agreeable the work is, how costly it "
             "is to learn, how steady it is, how much trust it needs, and how likely you "
             "are to succeed at it. The first four are in this lesson; the fifth has the "
             "next lesson to itself."),
            ("Education as an expensive machine",
             "A man trained at length to a skilled trade is, Smith says, like an expensive "
             "machine: the work he does must replace what his training cost, and the "
             "ordinary profit on that sum, within a reasonable time. That is why the pay "
             "of skilled labour exceeds the pay of common labour, and by about that much."),
        ],
        "read_title": "The chapter's opening claim, then the first four circumstances",
        "read_intro": (
            "The opening sentence is the whole chapter in one line. Read it, then read the "
            "list of five, and notice that Smith says he is reporting what he has been able "
            "to observe."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 10.</strong> Smith's first sentence says that the whole "
                  "of the advantages &ldquo;and disadvantages of the different employments of "
                  "labour and stock, must, in the same neighbourhood, be either perfectly "
                  "equal, or continually tending to equality.&rdquo;"),
            ("p", "Smith gives the reason at once, and it is the mechanism of the whole "
                  "chapter. If one employment were evidently better than the rest, &ldquo;so "
                  "many people would crowd into it in the one case, and so many would desert "
                  "it in the other, that its advantages would soon return to the level of "
                  "other employments.&rdquo; That is a claim about a society left to follow "
                  "its natural course, &ldquo;where there was perfect liberty&rdquo;, and every "
                  "man free to choose his trade and change it. He admits in the next breath "
                  "that money wages and profits in Europe are in fact &ldquo;extremely "
                  "different&rdquo;. The chapter explains the difference in two parts: the "
                  "circumstances in the employments themselves, which this course reads in "
                  "its first three lessons, and the policy of Europe, which it reads in the "
                  "last two."),
            ("p", "The five circumstances are those which make up for a small money gain in "
                  "some employments and counterbalance a great one in others, &ldquo;either "
                  "really, or at least in the imagination of men&rdquo;. The phrase matters. "
                  "A trade can be paid more because it is worse, or because people think it "
                  "worse, and the pay does not ask which. Smith lists them: "
                  "&ldquo;the agreeableness or disagreeableness of the employments "
                  "themselves; secondly, the easiness and cheapness, or the difficulty and "
                  "expense of learning them; thirdly, the constancy or inconstancy of "
                  "employment in them; fourthly, the small or great trust which must be "
                  "reposed in those who exercise them; and, fifthly, the probability or "
                  "improbability of success in them.&rdquo;"),
            ("p", "First, how the work feels. A journeyman tailor earns less than a journeyman "
                  "weaver because his work is easier; a weaver earns less than a smith because "
                  "the smith's is dirtier; a blacksmith &ldquo;seldom earns so much in twelve "
                  "hours, as a collier, who is only a labourer, does in eight&rdquo;, because "
                  "the collier's work is dirtier and more dangerous. Honour pays in a different "
                  "coin: &ldquo;Honour makes a great part of the reward of all honourable "
                  "professions&rdquo;, so that in money they are under-recompensed. Disgrace "
                  "does the opposite. &ldquo;The trade of a butcher is a brutal and an odious "
                  "business; but it is in most places more profitable than the greater part "
                  "of common trades.&rdquo; And work that other people do for pleasure, "
                  "hunting and fishing, becomes in an advanced society the occupation of the "
                  "very poor, because the natural taste for it crowds in more people than "
                  "can live by it."),
            ("p", "Second, what the trade costs to learn. Here Smith reaches for a machine. "
                  "&ldquo;A man educated at the expense of much labour and time to any of those "
                  "employments which require extraordinary dexterity and skill, may be "
                  "compared to one of those expensive machines.&rdquo; The work he learns to "
                  "do &ldquo;will replace to him the whole expense of his education, with at "
                  "least the ordinary profits of an equally valuable capital&rdquo;, and it "
                  "must do so in a reasonable time, since human life is less certain than a "
                  "machine's. A watchmaker's pay has to cover what a watchmaker cost to make."),
            ("def", ("Net advantage (this lab's term)",
                     "The yearly money a trade pays, less each year's share of what learning "
                     "it cost and the ordinary profit on that sum, plus or minus a stated "
                     "money value for the trade's other circumstances. Smith never adds these "
                     "up; he says they balance. The lab adds them so that you can see the "
                     "balance, and it takes the money values of agreeableness and risk from "
                     "you, because no chapter can supply them.")),
            ("p", "Third, how steady the work is. A mason or bricklayer cannot work in hard "
                  "frost or foul weather, and the rest of the time depends on his customers. "
                  "&ldquo;What he earns, therefore, while he is employed, must not only "
                  "maintain him while he is idle, but make him some compensation for those "
                  "anxious and desponding moments which the thought of so precarious a "
                  "situation must sometimes occasion.&rdquo; Smith's figures are weekly: "
                  "&ldquo;where the former earn six, the latter often earn nine and ten&rdquo;, "
                  "labourers against masons. Masons are not more skilled. &ldquo;No species of "
                  "skilled labour, however, seems more easy to learn than that of masons and "
                  "bricklayers.&rdquo; He concludes: &ldquo;The high wages of those workmen, therefore, are "
                  "not so much the recompence of their skill, as the compensation for the "
                  "inconstancy of their employment.&rdquo; The same logic runs the other way. "
                  "London journeymen tailors, called on and dismissed from day to day, earn "
                  "half a crown where eighteen pence is common labour's wage; in small towns "
                  "they scarcely equal it. And where hard, dirty work is also irregular, as "
                  "with the London coal-heavers, whose work depends on the arrival of coal "
                  "ships, an inquiry Smith cites found earnings of six to ten shillings a day, "
                  "and six shillings alone is about four times common labour in London. He says it ought not to seem unreasonable, since "
                  "if the pay exceeded what the disagreeableness required, &ldquo;there would "
                  "soon be so great a number of competitors&rdquo; that it would fall."),
            ("p", "Fourth, trust. Goldsmiths and jewellers are paid more than workmen of equal "
                  "or higher ingenuity because of the precious materials they handle. "
                  "&ldquo;We trust our health to the physician, our fortune, and sometimes our "
                  "life and reputation, to the lawyer and attorney.&rdquo; Such confidence could "
                  "not be given to people of mean condition, so the reward has to give them a "
                  "rank. Add the long, dear education these trades need, and the price of "
                  "their labour is raised again."),
            ("p", "The lab turns the list into a sum. In the equal preset, written for this "
                  "lesson, there are four trades. A labourer earns 1 shilling a day for 300 "
                  "days, 300 shillings. A mason earns 3/2 of a shilling a day for only 200 "
                  "days, because of the weather, and also gets 300. A collier earns 2 "
                  "shillings, double the labourer, for 300 days, 600 shillings, but the "
                  "preset puts the dirt and danger at 300 shillings a year, so his net is "
                  "300 too. A craftsman paid 6/5 of a shilling for 300 days earns 360, and his "
                  "400 shillings of learning, replaced over 20 working years with 10 percent "
                  "profit on the sum, cost him 60 a year, so he nets 300. Four very different "
                  "wage bills, one net advantage: that is Smith's claim as arithmetic. The "
                  "learning preset keeps the craftsman at the labourer's wage of 1 shilling a "
                  "day. His net falls to 240, and the lab shows what Smith's mechanism would "
                  "do next: nobody would take up the trade until its wage rose. The "
                  "smith-mason preset uses Smith's own weekly figures, 6 shillings for the "
                  "labourer and 9 for the mason, as 1 and 3/2 of a shilling a day; the days "
                  "worked, 312 and 208, are the lesson's, chosen so that the two years' "
                  "earnings match."),
            ("p", "Smith adds two remarks that keep the lesson honest. Skill is not what "
                  "most of the policy of Europe says it is: its laws treat every mechanic as "
                  "skilled and every country labourer as common, and Smith says he will "
                  "show that this is wrong, which the fourth lesson reads. And of the five "
                  "circumstances, he says later, two only affect the profits of stock, so "
                  "profit varies far less across trades than wages do. That is the third "
                  "lesson. The next lesson takes the fifth circumstance, which Smith spends "
                  "the most words on: success."),
        ],
        "lab": ("wonkit", {
            "mode": "advantage",
            "view": "net",
            "money_unit": "s",
            "preset": "equal",
            "presets": [
                {"id": "equal", "label": "Four trades, written for this lesson, whose net comes out level",
                 "profit": 10,
                 "employments": "labourer, 1, 300, 0, 1, 0; mason, 3/2, 200, 0, 1, 0; collier, 2, 300, 0, 1, -300; craftsman, 6/5, 300, 400, 20, 0",
                 "expect": {
                           "wadAnnual": "labourer 300s; mason 300s; collier 600s; craftsman 360s",
                           "wadLearnYear": "labourer 0s; mason 0s; collier 0s; craftsman 60s",
                           "wadNet": "labourer 300s; mason 300s; collier 300s; craftsman 300s",
                           "wadSpread": "0s: every employment nets the same"}},
                {"id": "learning", "label": "The craftsman paid no more than a labourer, written for this lesson",
                 "profit": 10,
                 "employments": "labourer, 1, 300, 0, 1, 0; craftsman, 1, 300, 400, 20, 0",
                 "expect": {
                           "wadLearnYear": "labourer 0s; craftsman 60s",
                           "wadNet": "labourer 300s; craftsman 240s",
                           "wadSpread": "60s (labourer over craftsman)"}},
                {"id": "smith-mason", "label": "Smith's six and nine shillings a week, days worked written for this lesson",
                 "profit": 0,
                 "employments": "labourer, 1, 312, 0, 1, 0; mason, 3/2, 208, 0, 1, 0",
                 "expect": {
                           "wadAnnual": "labourer 312s; mason 312s",
                           "wadSpread": "0s: every employment nets the same"}},
            ],
            "panel_title": "What a trade pays, and what it costs",
            "panel_intro": (
                "Each trade's wage a day, days worked, cost of learning, working years over "
                "which the learning is replaced, and a signed money value for its other "
                "circumstances go in. The lab adds up a year's net advantage for each. Compare "
                "the equal preset with learning, and notice which tile moves when only the "
                "craftsman's wage changes."
            ),
        }),
        "steps_title": "Netting a trade's advantages",
        "steps_intro": "Four steps, the same for any trade you can put figures to.",
        "steps": [
            ("Find the year's money wage",
             "Multiply the wage a day by the days actually worked in a year. A trade that "
             "stands idle for part of the year gets the idle days into the sum here, by "
             "the days it leaves out."),
            ("Charge the learning",
             "Divide what learning cost by the working years over which it is replaced, "
             "and add the ordinary profit on that sum. Smith's machine must replace its cost "
             "and earn profit too."),
            ("Add the other circumstances",
             "Put a signed money value on the dirt, danger, disgrace or honour. It is a "
             "judgment, and the preset must say whose; Smith offers no table of them."),
            ("Compare",
             "Net advantage is the year's wage, less the year's learning, plus or minus "
             "the other circumstances. If one trade is far above the rest, Smith's "
             "mechanism says people will crowd into it and its wage will fall."),
        ],
        "worked": {
            "title": "What the craftsman must earn",
            "intro": [
                "Take the equal preset. A craftsman spends 400 shillings learning, over 20 "
                "working years, at 10 percent profit. What wage a day keeps him level with "
                "a labourer who earns 300 a year?",
            ],
            "lines": [
                "learning replaced a year:  400 / 20 = 20",
                "profit on the learning:  10% of 400 = 40",
                "learning charged a year:  20 + 40 = 60",
                "wage needed:  300 + 60 = 360 a year",
                "wage a day:  360 / 300 = 6/5 of a shilling",
            ],
            "after": [
                "At 6/5 of a shilling a day the craftsman nets 300, the same as the labourer. "
                "Pay him less and the learning does not repay; pay him more and, in Smith's "
                "world, more young men will learn the trade until the pay comes back down.",
            ],
        },
        "quiz_title": "Why one trade pays more than another",
        "quiz": [
            {"q": "On Smith's account, why can London coal-heavers earn four or five times the "
                  "wages of common labour when colliers earn double or triple?",
             "a": ["Their work is as dirty and hard as the collier's, and the arrival of the "
                   "coal ships also makes it very inconstant",
                   "They need a longer apprenticeship than colliers",
                   "They hold an exclusive privilege that keeps competitors out",
                   "They are trusted with more valuable goods"],
             "c": 0,
             "why": "Smith ranks the coal-heavers' trade with the colliers' for hardship, "
                    "dirtiness and disagreeableness, and adds that &ldquo;the employment of "
                    "the greater part of them is necessarily very inconstant&rdquo;. Neither "
                    "an apprenticeship nor a trust is mentioned, and he says the trade "
                    "&ldquo;has no exclusive privilege&rdquo;."},
            {"q": "In the equal preset a mason earns 3/2 of a shilling a day for 200 days and "
                  "a labourer 1 shilling a day for 300. What does the lab show?",
             "a": ["The mason is better off by half",
                   "The labourer is better off by 100 shillings a year",
                   "They earn the same in the year, so the higher day wage pays for the idle days",
                   "The mason earns 100 shillings more because masons are skilled"],
             "c": 2,
             "why": "The mason's year is `3/2 × 200 = 300` and the labourer's `1 × 300 = 300`. "
                    "Smith's point is that the higher day wage is not a reward of skill, "
                    "since masonry is easy to learn; it is the compensation for the days "
                    "the weather and the customers leave him idle."},
            {"q": "A craftsman's learning costs 400 shillings, replaced over 20 working years "
                  "with 10 percent profit on the 400. What does the lab charge him a year?",
             "a": ["20 shillings", "40 shillings", "420 shillings", "60 shillings"],
             "c": 3,
             "why": "Replacing the 400 over 20 years is `400 / 20 = 20` a year, and the "
                    "profit on it is `10% of 400 = 40`, so `20 + 40 = 60`. Twenty alone "
                    "leaves out the profit Smith says the machine must earn; forty alone "
                    "leaves out the replacement."},
            {"q": "How does Smith describe a man trained at length to a skilled trade?",
             "a": ["As a lottery ticket whose price is the cost of his education",
                   "As a debtor whose master is owed seven years' service",
                   "As a machine whose work must replace the cost of his education with at "
                   "least the ordinary profits of an equally valuable capital",
                   "As the owner of a monopoly that he bought with his apprenticeship"],
             "c": 2,
             "why": "The comparison is to &ldquo;one of those expensive machines&rdquo;. "
                    "The lottery is the fifth circumstance, probability of success, and "
                    "the monopoly belongs to the policy of Europe in Part II."},
        ],
        "mistakes": [
            ("Reading Smith as saying that wages are equal",
             "He says the whole of the advantages is equal, or tending to it, and begins "
             "by saying that money wages are &ldquo;extremely different&rdquo;. In the "
             "equal preset the four trades' wage bills run from 300 to 600 shillings and "
             "their net advantage is 300 each. Look for the equality in the last tile, "
             "not the first."),
            ("Taking a high wage as the reward of skill",
             "Masons are paid from half as much again to double what labourers get, and "
             "Smith says that is not for skill but for idle days. A high wage may pay for "
             "skill, for dirt, for danger, for idleness, for trust or for risk. The "
             "question is which, and the lab's rows are there to be asked it of."),
            ("Treating the equality as a law that holds anywhere",
             "The mechanism needs people free to choose and to move. Part I adds three "
             "conditions even then, which the third lesson reads, and Part II reads what "
             "the policy of Europe does to the mechanism. Equality of the whole of the "
             "advantages is what the chapter says would happen if the movement were free, "
             "not a report of what it found."),
        ],
        "standard": (
            "Finish when you can net a trade's advantages from its wage, days and learning.",
            "Given a trade's wage a day, days worked, cost and years of learning, the "
            "ordinary profit and a money value for its other circumstances, compute its "
            "net advantage, and say what Smith expects to happen to a trade whose net "
            "is above the others'."
        ),
        "note": (
            "Net advantage is this lab's sum. Smith gives no way to put a money value on "
            "dirt, danger or honour, so the lab asks you for one, and the equality in the "
            "first preset is built in by choosing the numbers. What the arithmetic cannot "
            "settle is whether free choice does level the whole of the advantages. John "
            "Stuart Mill argued in 1848 that the hardest and most disagreeable work is "
            "often the worst paid, the reverse of compensation, because those who do it "
            "have no choice, and J. E. Cairnes in 1874 that labour falls into non-competing groups between which people do not move "
            "freely, so that the pay of one grade is not held down by the supply of "
            "another. Capital's lesson <em>The Twofold Character of Labour</em> "
            "meets the pay of skilled work from a different side. Smith's own answer, in "
            "Part II, is that where wages differ more than the five circumstances "
            "explain, the policy of Europe is usually the cause."
        ),
    },
    # ---------------------------------------------------------------- 02
    # PSU text l. 3436-3467 (the lottery of the law), l. 3468-3531 (conceit and
    # lotteries), l. 3532-3562 (insurers), l. 3563-3617 (soldiers and sailors),
    # l. 3480-3500 (players, opera-singers).
    {
        "slug": "the-lottery-of-the-professions",
        "title": "The Lottery of the Professions",
        "module": "Book I, Chapter 10, Part I · Probability of Success",
        "one_line": "A profession where twenty fail for one who succeeds should pay the one what the twenty lost, and Smith says the law does not.",
        "summary": (
            "The fifth circumstance is the chance of success. Smith treats a profession as "
            "a lottery, asks whether its prizes repay its tickets, and answers that the "
            "liberal professions, soldiering and the sea do not, because people overvalue "
            "their chance of gain and undervalue their chance of loss. Work the fair prize "
            "for Smith's twenty to one, and compare a trade where almost everyone succeeds."
        ),
        "key": [
            "chance of success = winners / entrants",
            "prizes = winners × prize a year × years",
            "tickets = entrants × cost each",
            "a fair lottery: prizes equal tickets",
            "fair prize = tickets / (winners × years)",
        ],
        "key_label": "A profession as a lottery",
        "concepts_intro": (
            "Smith's tool here is one he borrows from the street: the lottery. It lets him "
            "ask of any trade what a fair reward for its risk would be, and then notice "
            "that people do not demand it."
        ),
        "concepts": [
            ("A fair lottery",
             "In a perfectly fair lottery, those who draw the prizes gain all that is lost "
             "by those who draw blanks. Applied to a profession: whoever succeeds should "
             "earn, over and above the ordinary reward, what all the failures spent on the "
             "attempt, as well as what he did."),
            ("Over-valued gain, under-valued loss",
             "Smith observes that the chance of gain is overvalued by nearly everyone and "
             "the chance of loss undervalued, from tickets that sell above their worth to "
             "uninsured houses. It is why a profession whose prizes do not repay its tickets "
             "can still be crowded."),
            ("Reward in the imagination",
             "Part of the prize is not money. Public admiration is a large part of the "
             "reward in physic, a larger in law, and in poetry and philosophy &ldquo;almost "
             "the whole&rdquo;. The money may then fall short without anyone being a fool."),
        ],
        "read_title": "The lottery of the law, then the conceit that fills it",
        "read_intro": (
            "Smith's argument comes in three moves: the arithmetic of a fair lottery, a "
            "claim that the professions fall short of it, and an explanation of why men "
            "join them anyway. Read them in that order."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 10, Part I.</strong> &ldquo;The probability that "
                  "any particular person shall ever be qualified for the employments to which "
                  "he is educated, is very different in different occupations. In the greatest "
                  "part of mechanic trades success is almost certain; but very uncertain in "
                  "the liberal professions.&rdquo;"),
            ("p", "His example is a father choosing a trade for his son. &ldquo;Put your son "
                  "apprentice to a shoemaker, there is little doubt of his learning to make a "
                  "pair of shoes; but send him to study the law&rdquo;, and it is &ldquo;at "
                  "least twenty to one if he ever makes such proficiency as will enable him "
                  "to live by the business&rdquo;. That is a lottery with twenty blanks to a prize, and "
                  "Smith does the sum in words. &ldquo;In a profession, where twenty fail for "
                  "one that succeeds, that one ought to gain all that should have been gained "
                  "by the unsuccessful twenty.&rdquo; The counsellor who begins to make "
                  "something at forty ought to receive the repayment not only of his own "
                  "tedious and expensive education &ldquo;but of that of more than twenty "
                  "others, who are never likely to make any thing by it&rdquo;."),
            ("p", "Then the claim. &ldquo;How extravagant soever the fees of counsellors at "
                  "law may sometimes appear, their real retribution is never equal to "
                  "this.&rdquo; Smith's test is aggregate. Compute, in any place, what all "
                  "the shoemakers or weavers gain in a year and what they spend, and the "
                  "gains exceed the spending. Do the same for the counsellors and students "
                  "of the Inns of Court and &ldquo;you will find that their annual gains bear "
                  "but a very small proportion to their annual expense&rdquo;. His verdict is "
                  "that the lottery of the law is &ldquo;very far from being a perfectly fair "
                  "lottery&rdquo;, and that it, like other liberal professions, is "
                  "&ldquo;in point of pecuniary gain, evidently under-recompensed&rdquo;."),
            ("p", "The lab works Smith's twenty to one. In the fair preset, a lottery written "
                  "for this lesson, 21 young men enter a profession and 1 succeeds. Each "
                  "entrant's education costs 200 pounds, so the tickets cost 4,200. The one "
                  "who succeeds works for 20 years; he must earn, above what common "
                  "labour would have given him, 210 pounds a year for the prizes to equal "
                  "the tickets, `210 × 20 = 4,200`. That is the fair prize. The short preset "
                  "pays him 120 a year, so the prizes are 2,400 against tickets of 4,200, a "
                  "shortfall of 1,800, and the prizes spread over the 21 "
                  "entrants come to about 114 each against the 200 each spent. In the shoemaker preset, also written "
                  "for this lesson, 19 of 20 apprentices succeed at 1 pound a year above a "
                  "labourer's pay for 20 years, against an education that costs 18 each: the "
                  "prizes, 380, exceed the tickets, 360. Smith's point is exactly this "
                  "contrast. In the common trade the gains exceed the spending; in the law "
                  "they do not."),
            ("def", ("Prize (this lab's term)",
                     "The yearly income of one who succeeds over and above what common "
                     "labour would have earned him. A fair profession pays the prize that "
                     "makes all the winners' extra income, over their working years, equal "
                     "all the entrants' education costs. Smith states the principle in "
                     "words; the sums here are the lab's.")),
            ("p", "If the law is so poor a lottery, why is it full? Smith has two answers. "
                  "&ldquo;First, the desire of the reputation which attends upon superior "
                  "excellence in any of them; and, secondly, the natural confidence which "
                  "every man has, more or less, not only in his own abilities, but in his own "
                  "good fortune.&rdquo; Of the first he says that to excel where few arrive "
                  "even at mediocrity &ldquo;is the most decisive mark of what is called "
                  "genius&rdquo;, and the public admiration is a part of the reward. Of the "
                  "second he is blunter. &ldquo;The over-weening conceit which the greater "
                  "part of men have of their own abilities, is an ancient evil remarked by "
                  "the philosophers and moralists of all ages. Their absurd presumption in "
                  "their own good fortune has been less taken notice of. It is, however, if "
                  "possible, still more universal.&rdquo;"),
            ("p", "Smith finds the same habit in the street. State lottery tickets &ldquo;are "
                  "really not worth the price which is paid by the original subscribers, and "
                  "yet commonly sell in the market for twenty, thirty, and sometimes forty per "
                  "cent. advance&rdquo;, and he adds that there is not &ldquo;a more certain "
                  "proposition in mathematics, than that the more tickets you adventure upon, "
                  "the more likely you are to be a loser&rdquo;. On the other side he reads "
                  "the undervaluing of loss from the modest profits of insurers: of houses, "
                  "&ldquo;nineteen houses in twenty, or rather, perhaps, ninety-nine in a "
                  "hundred, are not insured from fire&rdquo;."),
            ("p", "Then the soldiers and sailors. The common soldier's pay is less than a "
                  "labourer's and his fatigues greater, and young men enlist most readily "
                  "at the start of a war: &ldquo;These romantic hopes make the whole price "
                  "of their blood.&rdquo; The sea is a different lottery from the army. "
                  "Because its great prizes are smaller, &ldquo;the smaller ones must be more "
                  "numerous&rdquo;, and common sailors more often get some fortune. Even so a "
                  "London sailor's pay in peace, from a guinea to about seven-and-twenty "
                  "shillings the calendar month, is below what a London labourer at nine or "
                  "ten shillings a week earns in a month, forty to five-and-forty shillings. "
                  "The sailor is also supplied with provisions, but Smith reckons their "
                  "value need not exceed the difference, and he cannot share them with the "
                  "family he supports at home. Smith adds a passage on the pleasure of "
                  "danger. The distant prospect of hazards we hope to escape by courage does "
                  "not raise wages; unwholesome trades, where courage is no use, always pay "
                  "remarkably well."),
            ("p", "The profit of stock follows the same rule, a little weakened. The rate of "
                  "profit &ldquo;always rises more or less with the risk&rdquo;, but not "
                  "&ldquo;in proportion to it&rdquo;. The smuggler's trade, when the venture "
                  "succeeds the most profitable, is &ldquo;the infallible road to "
                  "bankruptcy&rdquo;. And of the five circumstances, Smith concludes, only "
                  "two touch profit: the pleasantness of the business, in which most "
                  "employments of stock differ very little, and the risk or security of the "
                  "return. Wages should therefore differ more across trades than profits do, "
                  "and he says they do. The next lesson shows how some of the apparent "
                  "difference in profits disappears when the apothecary's wages are taken out "
                  "of it."),
        ],
        "lab": ("wonkit", {
            "mode": "advantage",
            "view": "lottery",
            "money_unit": "£",
            "preset": "fair",
            "presets": [
                {"id": "fair", "label": "Twenty blanks to a prize, the prize made fair, written for this lesson",
                 "entrants": 21, "succeed": 1, "prize": 210, "years": 20, "cost": 200,
                 "expect": {
                           "wadChance": "1/21 ≈ 4.8%",
                           "wadPrizes": "£4,200",
                           "wadTickets": "£4,200",
                           "wadFair": "fair: the prizes exactly repay the tickets",
                           "wadNeeded": "£210 a year (against £210)"}},
                {"id": "short", "label": "The same lottery, the prize cut to 120 a year, written for this lesson",
                 "entrants": 21, "succeed": 1, "prize": 120, "years": 20, "cost": 200,
                 "expect": {
                           "wadPrizes": "£2,400",
                           "wadExpected": "≈ £114.29 an entrant (against £200 a ticket)",
                           "wadFair": "short by £1,800: the prizes repay 4/7 ≈ 57.1% of the tickets"}},
                {"id": "shoemaker", "label": "A common trade where 19 of 20 succeed, written for this lesson",
                 "entrants": 20, "succeed": 19, "prize": 1, "years": 20, "cost": 18,
                 "expect": {
                           "wadChance": "19/20 = 95%",
                           "wadPrizes": "£380",
                           "wadTickets": "£360",
                           "wadFair": "over by £20: the prizes repay 19/18 ≈ 105.6% of the tickets"}},
            ],
            "panel_title": "Do the prizes repay the tickets?",
            "panel_intro": (
                "Entrants, winners, the prize a year, working years and each entrant's cost "
                "go in. The lab compares the prizes with the tickets and says what the prize "
                "would have to be to repay them. Change only the prize between the first "
                "two presets and watch the fair-or-short tile."
            ),
        }),
        "steps_title": "Testing a profession as a lottery",
        "steps_intro": "Five steps, for any trade where some who enter fail.",
        "steps": [
            ("Count winners and entrants",
             "The chance of success is winners divided by entrants. Smith's twenty to one "
             "is one winner in twenty-one entrants."),
            ("Add up the tickets",
             "Multiply the entrants by what each spent on education and preparation. "
             "Losers' costs count as much as winners'."),
            ("Add up the prizes",
             "Multiply the winners by the yearly income they earn over common labour and "
             "by their working years."),
            ("Compare",
             "If the prizes equal the tickets the lottery is fair; if they fall short, "
             "the profession is under-recompensed, in Smith's word; if they exceed them, "
             "as in the shoemaker preset, the trade pays more than its cost."),
            ("Ask what the prize would need to be",
             "Divide the tickets by the winners and the years. That is the yearly prize "
             "which would make the lottery fair."),
        ],
        "worked": {
            "title": "What the one in twenty-one must earn",
            "intro": [
                "Take the fair preset. Twenty-one students enter, one succeeds, each "
                "education costs 200 pounds and the successful one works 20 years. What yearly "
                "income above common labour makes the lottery fair?",
            ],
            "lines": [
                "tickets:  21 · 200 = 4,200",
                "winners' working years:  1 · 20 = 20",
                "fair prize a year:  4,200 / 20 = 210",
                "check:  1 · 210 · 20 = 4,200",
                "chance of success:  1 in 21",
            ],
            "after": [
                "A winner paid 120 a year, as in the short preset, collects 2,400 against "
                "4,200 spent. Smith says the law's fees, however extravagant they appear, "
                "never reach the first figure; the lab only does the division.",
            ],
        },
        "quiz_title": "Fair tickets and unfair professions",
        "quiz": [
            {"q": "Twenty-one students enter a profession, one succeeds, each education costs "
                  "200 pounds and the winner works 20 years. What prize a year, above common "
                  "labour, makes the lottery fair?",
             "a": ["10 pounds", "200 pounds", "4,200 pounds", "210 pounds"],
             "c": 3,
             "why": "The tickets cost `21 × 200 = 4,200` and the winner has 20 years to repay "
                    "them, `4,200 / 20 = 210`. Two hundred is one student's cost, which "
                    "repays only his own education, and `10` is `200 / 20`, the same mistake "
                    "at yearly rate. The whole 4,200 would be the prize if the winner had "
                    "only one year."},
            {"q": "In the shoemaker preset, 19 of 20 apprentices succeed at 1 pound a year "
                  "above a labourer for 20 years, and each education costs 18. What does "
                  "the lab say?",
             "a": ["The prizes, 380, exceed the tickets, 360",
                   "The prizes are 380 against tickets of 380, a fair lottery",
                   "The prizes, 20, are far short of the tickets",
                   "The prizes are 360 and the tickets are 380"],
             "c": 0,
             "why": "Prizes are `19 × 1 × 20 = 380` and tickets `20 × 18 = 360`. Smith's "
                    "claim is that in a common trade the gains exceed the spending, and "
                    "the preset is built to show it."},
            {"q": "Why, on Smith's account, do people keep entering a profession whose "
                  "prizes do not repay its tickets?",
             "a": ["Every profession is protected by a corporation that keeps wages up",
                   "They overvalue their own chance of gain, and the reputation counts "
                   "as part of the reward",
                   "The law obliges each family to put one son to a profession",
                   "The sums are better than they look because losers earn the same as winners"],
             "c": 1,
             "why": "He gives two causes: the desire of reputation and &ldquo;the natural "
                    "confidence which every man has&rdquo; in his own abilities and fortune. "
                    "Corporations belong to Part II, Smith names no law that sends sons to "
                    "the professions, and the losers' earnings are exactly what Smith says "
                    "are too small."},
            {"q": "How does Smith explain why the profit of stock does not rise in "
                  "proportion to the risk of a trade?",
             "a": ["Insurers set profits by law",
                   "Stock is never at risk, only labour is",
                   "The presumptuous hope of success draws so many adventurers into hazardous "
                   "trades that competition reduces the profit below what covers the risk",
                   "Bankruptcies are rarer in risky trades, because merchants take more care"],
             "c": 2,
             "why": "The passage says &ldquo;presumptuous hope of success seems to act "
                    "here as upon all other occasions&rdquo;, and that bankruptcies are "
                    "&ldquo;most frequent in the most hazardous trades&rdquo;. The other "
                    "three options each contradict it."},
        ],
        "mistakes": [
            ("Thinking Smith says the professions should be rich",
             "He says a fair lottery would pay the winner for the losers too, and that the "
             "professions fall short of it. The chapter is about what a fair reward would be "
             "and why the real one is smaller. The short preset is the sort of case it "
             "describes."),
            ("Counting only the winners",
             "The cost of the education of those who fail is part of the tickets. A "
             "profession where 20 fail for 1 that succeeds has 21 educations to pay for. "
             "Leave the 20 out and the fair prize looks 21 times too small."),
            ("Treating the lottery as an argument that gambling is irrational",
             "Smith's claim is narrower: the chance of gain is overvalued by nearly "
             "everyone, and that shows in what people do with tickets, insurance and "
             "careers. Reputation is a real part of the prize. A reader who values it at "
             "more than the money can reasonably join a profession the lab shows as short."),
        ],
        "standard": (
            "Finish when you can test whether a profession's prizes repay its tickets.",
            "Given the entrants, winners, prize a year, working years and each entrant's "
            "cost, compute the chance of success, the total prizes and tickets, and the "
            "prize a year that would make the lottery fair."
        ),
        "note": (
            "The lab treats a prize as a plain yearly sum, and it has no place for the "
            "reputation Smith counts as part of the reward, nor for risk preferences. The "
            "figures are the lesson's; Smith gives the twenty to one and no others. Later "
            "economists have asked whether this part of the argument fits the evidence. "
            "The overvaluing of chance he describes is close to what later writers on "
            "choice under risk call a weighting of small probabilities, and what the "
            "arithmetic cannot settle is whether the professions in fact pay less than a "
            "fair lottery would, which is a question of what lawyers earned, not of "
            "arithmetic. His figures for sailors' and labourers' pay are his reports, and "
            "the lesson takes them as stated."
        ),
    },
    # ---------------------------------------------------------------- 03
    # PSU text l. 3632-3666 (profit, two of five), l. 3670-3703 (apothecary,
    # grocer), l. 3704-3731 (capital and small town), l. 3765-3927 (the three
    # conditions).
    {
        "slug": "the-apothecary-and-the-grocer",
        "title": "The Apothecary and the Grocer",
        "module": "Book I, Chapter 10, Part I · The Equality of Profit, and Its Conditions",
        "one_line": "A profit of a thousand per cent may be the reasonable wages of the man who earns it, and the equality holds only for trades that are known, ordinary and the trader's main business.",
        "summary": (
            "Smith says profit varies much less across trades than wages do, and meets the "
            "objection that apothecaries' profit is a byword. His answer is that the great "
            "part of it is wages in the garb of profit. Take the apothecary's drugs and the "
            "grocer's stock, subtract the wages of the trader's own labour, and see what "
            "profit is left. Then read the three conditions under which the equality of the "
            "whole holds."),
        "key": [
            "apparent profit = sales − cost of stock",
            "wages of the trader come out of it",
            "true profit = apparent profit − wages",
            "rate = profit / stock",
            "wages share = wages / apparent profit",
        ],
        "key_label": "Profit, and the wages inside it",
        "concepts_intro": (
            "This lesson has two halves. The first is an accounting point about what "
            "profit is; the second is a list of what the equality of advantages needs."
        ),
        "concepts": [
            ("Wages in the garb of profit",
             "A trader who works in his own business receives one sum for two things: the "
             "profit on his stock, and the wages of his labour. The takings do not say "
             "which is which. Smith's apothecary, a man of skill and trust, charges for "
             "his labour &ldquo;in the only way in which he can charge them, upon the price "
             "of his drugs&rdquo;."),
            ("Why profits are more level than wages",
             "Of the five circumstances only two touch profit, the pleasantness of the "
             "business and its risk. The other three, learning, constancy and trust, "
             "attach to the person and to the labour, not to the stock. So the ordinary "
             "rate of profit in different trades is more nearly level than the wages of "
             "different sorts of labour."),
            ("Three conditions",
             "The equality of the whole of the advantages needs the employments to be "
             "well known and long established, in their ordinary or natural state, and "
             "the sole or principal employment of those who follow them. Where one of "
             "these fails, Smith expects an unevenness, and gives examples."),
        ],
        "read_title": "Apparent profit, then real wages",
        "read_intro": (
            "Smith first argues the profits of stock should be more level than wages. "
            "Then he goes straight to the case where they seem least so."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 10, Part I.</strong> Having run through the five "
                  "circumstances, Smith draws a conclusion about stock. Of the five, "
                  "&ldquo;two only affect the profits of stock; the agreeableness or "
                  "disagreeableness of the business, and the risk or security with which it "
                  "is attended.&rdquo; Most employments of stock differ little in "
                  "agreeableness, and profit does not rise fully with risk. &ldquo;It should "
                  "follow from all this, that, in the same society or neighbourhood, the "
                  "average and ordinary rates of profit in the different employments of "
                  "stock should be more nearly upon a level than the pecuniary wages of the "
                  "different sorts of labour.&rdquo; And he asserts that they are."),
            ("p", "The obvious objection comes at once. Apothecaries' profit is a byword for "
                  "extravagance. Smith's reply is the most useful sentence in the chapter "
                  "for anyone who has run a small business: &ldquo;The greater part of the "
                  "apparent profit is real wages disguised in the garb of profit.&rdquo; The "
                  "skill of an apothecary is &ldquo;a much nicer and more delicate matter "
                  "than that of any artificer whatever&rdquo;, and he is the physician of the "
                  "poor, so his reward ought to suit it. It arises from the price of his "
                  "drugs. &ldquo;But the whole drugs which the best employed apothecary in a "
                  "large market-town, will sell in a year, may not perhaps cost him above "
                  "thirty or forty pounds. Though he should sell them, therefore, for three "
                  "or four hundred, or at a thousand per cent. profit, this may frequently "
                  "be no more than the reasonable wages of his labour.&rdquo;"),
            ("p", "Run it in the lab. In the apothecary preset, written for this lesson, "
                  "drugs cost 40 pounds and sell for 440: an apparent profit of 400, a "
                  "thousand per cent on the stock. Suppose the apothecary's own skilled "
                  "labour is worth 396 pounds a year, a figure Smith does not give and the "
                  "preset chooses to make the point. Then the profit that is left is 4 "
                  "pounds, 10 percent of the stock, which is an ordinary rate, and 396 of "
                  "the 400, 99 percent, was wages. A thousand per cent in the books, and 10 "
                  "percent in the economics."),
            ("p", "Smith's second example gives the figures himself. &ldquo;In a small "
                  "sea-port town, a little grocer will make forty or fifty per cent. upon a "
                  "stock of a single hundred pounds, while a considerable wholesale merchant "
                  "in the same place will scarce make eight or ten per cent. upon a stock of "
                  "ten thousand.&rdquo; The grocer must read, write and account, and judge "
                  "perhaps fifty or sixty sorts of goods, their prices and the cheapest "
                  "markets: &ldquo;Thirty or forty pounds a year cannot be considered as too "
                  "great a recompence for the labour of a person so accomplished. Deduct "
                  "this from the seemingly great profits of his capital, and little more "
                  "will remain, perhaps, than the ordinary profits of stock.&rdquo; The "
                  "grocer preset takes the upper figures: stock 100, sales 150, an apparent "
                  "profit of 50 percent, and wages of 40. What is left is 10 pounds, 10 "
                  "percent."),
            ("p", "Smith adds how the same man looks in a city. The apparent profits of the "
                  "retail trade are nearer the wholesale merchant's in the capital than in a "
                  "small town, because where ten thousand pounds can be employed in the "
                  "grocery trade &ldquo;the wages of the grocer's labour must be a very "
                  "trifling addition to the real profits of so great a stock&rdquo;. The "
                  "city grocer preset, written for this lesson with Smith's 40 pounds of "
                  "wages, shows it: stock 10,000, sales 11,000, an apparent profit of 10 "
                  "percent. Take out the 40 and 9.6 percent is left, and wages are 4 percent "
                  "of the apparent profit where the village grocer's were 80. It is why "
                  "groceries are generally as cheap or cheaper in the capital: the prime "
                  "cost is the same, and the profit charged is least. Bread and butcher's "
                  "meat are about as cheap in either place because there the extent of the "
                  "market also raises the prime cost, as corn and cattle come from further "
                  "away. Smith notes that the village grocer's rate of profit may be high "
                  "yet the sum can never be great, since trade there cannot be extended as "
                  "stock extends."),
            ("def", ("Apparent profit and true profit (this lab's terms)",
                     "Apparent profit is the sales less the stock laid out. True profit is "
                     "what remains after the wages the trader's own labour would have "
                     "earned. Smith's expression is &ldquo;real wages disguised in the garb "
                     "of profit&rdquo;. The wage figure is always an input you supply, "
                     "because the books of a trader do not state it.")),
            ("p", "Then Smith turns to the conditions. The five circumstances, he says, "
                  "&ldquo;though they occasion considerable inequalities in the wages of "
                  "labour and profits of stock, occasion none in the whole of the advantages "
                  "and disadvantages, real or imaginary, of the different employments of "
                  "either.&rdquo; But &ldquo;three things are requisite, even where there is "
                  "the most perfect freedom&rdquo;. First, the employments must be well known "
                  "and long established in the neighbourhood. Wages are higher in new trades, "
                  "because a projector must entice workmen from others, and profits in a new "
                  "undertaking are extraordinary when it succeeds and often the opposite, "
                  "until the competition levels them. Birmingham deals in fashion and "
                  "Sheffield in use, and wages are said to suit the difference."),
            ("p", "Second, the employments must be in their ordinary or natural state. Hay "
                  "time and harvest raise country wages; war takes forty or fifty thousand "
                  "sailors into the navy and merchant seamen's wages rise from a guinea and "
                  "seven-and-twenty shillings to forty shillings and three pounds a month. "
                  "Profit follows price, and prices of corn, wine, hops, sugar and tobacco "
                  "swing with the harvest, so the speculative merchant, who &ldquo;enters "
                  "into every trade, when he foresees that it is likely to lie more than "
                  "commonly profitable&rdquo;, lives on exactly these."),
            ("p", "Third, the employment must be the sole or principal one of the people in "
                  "it. The Scottish cottar, with his house, his cow's grass and his two pecks "
                  "of oatmeal for the days he works, will work other hours for less. "
                  "Shetland stockings come to Leith at five to seven pence a pair, although "
                  "common labour at Lerwick is tenpence a day, and a good Scottish spinner "
                  "&ldquo;can earn twentypence a-week&rdquo;. Smith adds that this logic "
                  "makes writers who collect the wages of ancient times misread them, "
                  "because the cottar's daily or weekly recompence &ldquo;was evidently not "
                  "the whole price of their labour&rdquo;. He ends with London lodgings, "
                  "cheap because the tradesman who lets his middle storeys is paying part "
                  "of the rent and does not live by his lodgers. Part II, which the next "
                  "lesson opens, turns from these natural unevennesses to the ones the "
                  "policy of Europe makes."),
        ],
        "lab": ("wonkit", {
            "mode": "advantage",
            "view": "profit",
            "money_unit": "£",
            "preset": "apothecary",
            "presets": [
                {"id": "apothecary", "label": "Drugs costing 40 sold for 440, wages written for this lesson",
                 "sales": 440, "cost": 40, "wages": 396,
                 "expect": {
                           "wadApparent": "+£400",
                           "wadApparentRate": "+10 = +1,000% on £40",
                           "wadTrue": "+£4",
                           "wadTrueRate": "+1/10 = +10% on £40",
                           "wadWageShare": "99/100 = 99%"}},
                {"id": "grocer", "label": "Smith's village grocer: stock 100, forty or fifty per cent, wages of 40",
                 "sales": 150, "cost": 100, "wages": 40,
                 "expect": {
                           "wadApparent": "+£50",
                           "wadApparentRate": "+1/2 = +50% on £100",
                           "wadTrue": "+£10",
                           "wadTrueRate": "+1/10 = +10% on £100",
                           "wadWageShare": "4/5 = 80%"}},
                {"id": "city-grocer", "label": "The grocer's stock at 10,000, written for this lesson",
                 "sales": 11000, "cost": 10000, "wages": 40,
                 "expect": {
                           "wadApparent": "+£1,000",
                           "wadTrue": "+£960",
                           "wadTrueRate": "+12/125 = +9.6% on £10,000",
                           "wadWageShare": "1/25 = 4%"}},
            ],
            "panel_title": "Profit with the trader's wages taken out",
            "panel_intro": (
                "The sales, the stock laid out and the wages the trader's own labour would "
                "earn go in. The lab gives the apparent profit and its rate, the profit "
                "that is left and its rate, and the share of the apparent profit that was "
                "wages. Move from the village grocer to the city grocer and watch the "
                "wages share fall."
            ),
        }),
        "steps_title": "Finding the profit inside a trader's takings",
        "steps_intro": "Four steps, for any trader who works in his own business.",
        "steps": [
            ("Find the apparent profit",
             "Take the sales and subtract the stock laid out. Its rate is that sum over "
             "the stock."),
            ("Put a price on the trader's labour",
             "Ask what the same skill and trust would earn as wages. That is a judgment "
             "the books do not supply."),
            ("Subtract it",
             "True profit is the apparent profit less those wages, and its rate is "
             "over the same stock."),
            ("Compare with the ordinary rate",
             "If the true rate is near the ordinary profit of stock, the apparent profit "
             "was mostly wages, and the wages' share of it says how mostly."),
        ],
        "worked": {
            "title": "The village grocer's profit",
            "intro": [
                "Take the grocer preset. His stock is 100 pounds, his sales 150, and "
                "Smith values the labour of so accomplished a person at 40 pounds a year.",
            ],
            "lines": [
                "apparent profit:  150 − 100 = 50",
                "apparent rate:  50 / 100 = 50%",
                "true profit:  50 − 40 = 10",
                "true rate:  10 / 100 = 10%",
                "wages' share of the apparent profit:  40 / 50 = 80%",
            ],
            "after": [
                "A rate of 50 percent became 10 percent once his labour was paid for, which "
                "is in Smith's range of eight or ten for the wholesale merchant. "
                "The same arithmetic on the apothecary's thousand per cent leaves the same "
                "kind of remainder.",
            ],
        },
        "quiz_title": "Wages in the garb of profit",
        "quiz": [
            {"q": "In the grocer preset, stock is 100 pounds, sales 150 and the wages of the "
                  "grocer's labour 40. What is the profit left on the stock?",
             "a": ["50 percent", "40 percent", "10 percent", "90 percent"],
             "c": 2,
             "why": "The apparent profit is `150 − 100 = 50`; taking out `40` leaves `10`, "
                    "which is `10/100 = 10%`. Fifty percent is the apparent rate before "
                    "wages, and 40 percent is the wages themselves as a rate on the stock."},
            {"q": "On what ground does Smith say profit should be more nearly level across "
                  "trades than wages?",
             "a": ["Only two of the five circumstances, agreeableness and risk, affect "
                   "the profits of stock",
                   "Profits are fixed by law in every trade",
                   "Every trade employs about the same amount of stock",
                   "Capitalists are more skilled than workmen at judging employments"],
             "c": 0,
             "why": "He says &ldquo;two only affect the profits of stock&rdquo;. His own "
                    "grocer and wholesale merchant employ a hundred pounds and ten thousand; "
                    "he says nothing about the skills of capitalists, and profits are not "
                    "fixed by law."},
            {"q": "What does Smith say a trade must be for the whole of its advantages to "
                  "tend to equality with others?",
             "a": ["Protected by a corporation, in a large town, and of long standing",
                   "Well known and long established, in its ordinary state, and the sole or "
                   "principal employment of those who follow it",
                   "Skilled, steady and honourable",
                   "New, fashionable and well paid"],
             "c": 1,
             "why": "These are the three requisites. A corporation is what breaks the "
                    "equality in Part II. Skill, steadiness and honour are among the five "
                    "circumstances, not the conditions, and Smith says wages are higher in "
                    "new trades, which is why newness is a departure."},
            {"q": "Why does Smith say Shetland stockings reach Leith at five to seven pence "
                  "a pair when common labour in Lerwick earns tenpence a day?",
             "a": ["Shetland labour is unskilled and cannot knit better stockings",
                   "The knitters live by another employment and knit in their spare time "
                   "for less than the work would otherwise fetch",
                   "Leith merchants take the knitters' profit as wages",
                   "The stockings are made by apprentices who are not paid"],
             "c": 1,
             "why": "The third condition: the work is &ldquo;the work of servants and "
                    "labourers who derive the principal part of their subsistence from "
                    "some other employment&rdquo;. The same islands knit worsted stockings "
                    "worth a guinea a pair, which rules out unskilled knitters."},
        ],
        "mistakes": [
            ("Reading apparent profit as the profit of capital",
             "An apothecary's thousand per cent is on the price of his drugs. Part of it is "
             "payment for what he knows and the trust he is given, and Smith says it is the "
             "greater part. In the apothecary preset 99 percent of it is wages."),
            ("Assuming the wage figures are Smith's",
             "He gives the grocer's 30 or 40 pounds and the apothecary's 30 or 40 pounds of "
             "drugs, not the apothecary's wages. The preset says which figures are written "
             "for the lesson, and the apothecary's 396 is one. The conclusion is about "
             "the method, not that figure."),
            ("Supposing the equality is a prediction for any market",
             "Smith attaches three conditions even under perfect liberty: well known "
             "and long established, ordinary, and a principal employment. A new "
             "manufacture, a dear season and a cottar's spare time are each outside them, "
             "and he lists them as exceptions he expects."),
        ],
        "standard": (
            "Finish when you can separate a trader's wages from his profit.",
            "Given a trader's sales, stock and the wages his own labour would earn, "
            "compute the apparent and true profit and their rates, and the share of the "
            "apparent profit that is wages."
        ),
        "note": (
            "The lab can say how much of a trader's takings would be wages at a stated "
            "wage; it cannot say what the wage should be, and the answer depends on "
            "it entirely. Smith gives the grocer's figure, not the apothecary's. The "
            "argument that profit tends to a common rate is one Ricardo and Marx later "
            "build on, and the Capital lesson <em>The General Rate of Profit and Prices "
            "of Production</em> takes it up; whether "
            "profits in fact level, and over what time, is an empirical question the "
            "chapter answers with observation, not figures. The lesson treats each "
            "preset as a sum on the stated numbers."
        ),
    },
    # ---------------------------------------------------------------- 04
    # PSU text l. 3928-3951 (Part II, restraining competition), l. 3952-4020
    # (apprenticeship laws), l. 4021-4092 (sacred property, long apprenticeships
    # unnecessary), l. 4093-4125 (why corporations), l. 4262-4297 (conspiracy,
    # discipline), l. 4298-4447 (scholarships, curates, men of letters).
    {
        "slug": "apprenticeship-and-corporations",
        "title": "Apprenticeship and Corporations",
        "module": "Book I, Chapter 10, Part II · Inequalities Occasioned by the Policy of Europe",
        "one_line": "Corporations and apprenticeship laws restrict how many may enter a trade, and in Smith's account that keeps its wage above the rest at the expense of the country.",
        "summary": (
            "Part II turns from what nature does to what law does. The first way is to "
            "restrain competition in some employments to fewer than would enter: by "
            "limiting apprentices, by a long term of apprenticeship, and by incorporation. "
            "Smith's case is that this is a restraint on the property a man has in his own "
            "labour, and that the town's advantage over the country is its fruit. Work "
            "what a long apprenticeship does to a trade's wage and what a cap on entrants "
            "does to it."
        ),
        "key": [
            "a long apprenticeship raises learning cost",
            "learning charged a year = cost/years + profit",
            "wage must rise by what learning costs",
            "a cap on entry lifts pay above the rest",
            "gap = net advantage of capped trade − others",
        ],
        "key_label": "What restricting entry does",
        "concepts_intro": (
            "Part I's mechanism was free movement between trades. Part II asks what "
            "happens when law and bye-law interfere with it, and does it trade by trade."
        ),
        "concepts": [
            ("Restraining competition",
             "A corporation limits the number of apprentices a master may have, which "
             "restrains competition directly, and sets a long term of years, which does it "
             "&ldquo;more indirectly, but as effectually, by increasing the expense of "
             "education&rdquo;. Either way fewer enter the trade than otherwise would."),
            ("The town against the country",
             "Smith's economic point is about who pays. The town draws its subsistence "
             "and materials from the country, paying in manufactures; a regulation that "
             "raises the price of the town's goods lets the town buy more of the country's "
             "labour with less of its own. Landlords, farmers and labourers pay."),
            ("Combination and the corporation",
             "Tradesmen in a town can easily meet and combine. A corporation lets a "
             "majority bind the rest. In a free trade, Smith says, an effectual "
             "combination needs every trader's consent and lasts only while every one "
             "agrees; a corporation's bye-law is durable."),
        ],
        "read_title": "Three ways the policy of Europe restrains entry",
        "read_intro": (
            "Smith first says what the policy of Europe does, then gives the evidence of "
            "the apprenticeship laws, then his argument against them. The passage on "
            "combinations is the most quoted in the chapter."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 10, Part II.</strong> The policy of Europe, "
                  "Smith says, &ldquo;by not leaving things at perfect liberty, occasions "
                  "other inequalities of much greater importance&rdquo; than those of "
                  "Part I. It does so in three ways, and this lesson takes the first and "
                  "second, the third being the last lesson's subject: &ldquo;First, by "
                  "restraining the competition in some employments to a smaller number "
                  "than would otherwise be disposed to enter into them; secondly, by "
                  "increasing it in others beyond what it naturally would be; and, "
                  "thirdly, by obstructing the free circulation of labour and stock&rdquo;."),
            ("p", "The first means is the corporation. &ldquo;The limitation of the number "
                  "of apprentices restrains it directly. A long term of apprenticeship "
                  "restrains it more indirectly, but as effectually, by increasing the "
                  "expense of education.&rdquo; Smith's evidence is a list. &ldquo;In "
                  "Sheffield, no master cutler can have more than one apprentice at a time, "
                  "by a bye-law of the corporation.&rdquo; In Norfolk and Norwich no master "
                  "weaver may have more than two, under pain of forfeiting five pounds a "
                  "month to the king, and the same limit holds for hatters anywhere in "
                  "England. The silk-weavers of London, incorporated scarcely a year, "
                  "enacted a bye-law of two, and it took an act of parliament to rescind it. "
                  "Seven years was anciently the usual term all over Europe, and the "
                  "5th of Elizabeth, the Statute of Apprenticeship, made it the law of "
                  "all trades in England's market towns. Smith's examples of how absurd "
                  "this can be are coachmakers, who may not make their own wheels because "
                  "wheelwrights were an old trade, while a wheelwright may make coaches."),
            ("p", "Smith adds a small history that the word &ldquo;university&rdquo; "
                  "illustrates: &ldquo;All such incorporations were anciently called "
                  "universities&rdquo;, and the seven years of study for a master of arts "
                  "&ldquo;appears evidently to have been copied from the term of "
                  "apprenticeship in common trades&rdquo;. He also says that in Scotland "
                  "&ldquo;I know of no country in Europe, in which corporation laws are so "
                  "little oppressive&rdquo;, where three years is common and a small fine "
                  "buys much of the rest."),
            ("p", "Then the argument against. &ldquo;The property which every man has in his "
                  "own labour, as it is the original foundation of all other property, so it "
                  "is the most sacred and inviolable.&rdquo; To hinder a poor man from "
                  "employing his hands as he thinks proper &ldquo;is a plain violation of "
                  "this most sacred property&rdquo;. It is a restraint on the employers too: "
                  "&ldquo;To judge whether he is fit to be employed, may surely be trusted "
                  "to the discretion of the employers, whose interest it so much "
                  "concerns.&rdquo; A long apprenticeship gives no security against bad work, "
                  "since the sterling mark on plate and the stamps on cloth do the job and "
                  "nobody asks whether the workman served seven years. It does not teach "
                  "industry either: &ldquo;An apprentice is likely to be idle, and almost "
                  "always is so, because he has no immediate interest to be otherwise.&rdquo; "
                  "The arts of making clocks and watches, he says, need only the lessons of "
                  "a few weeks, &ldquo;those of a few days might certainly be sufficient&rdquo; "
                  "in the common mechanic trades."),
            ("p", "Why then do they exist? Smith's answer is the interest of the trade. If "
                  "apprentices were paid by the piece from the start, &ldquo;the work of all "
                  "artificers coming in this way much cheaper to market&rdquo;, the master "
                  "would lose the wages of the apprentice, the trade would have more "
                  "competitors, and its wages and profits would fall. &ldquo;The trades, the "
                  "crafts, the mysteries, would all be losers. But the public would be a "
                  "gainer.&rdquo; The lab reads this with a free trade and a restricted one. "
                  "In the weeks preset, written for this lesson, a craftsman's learning "
                  "costs 20 shillings, replaced over 20 working years with 10 percent profit "
                  "on the sum, which charges 3 shillings a year, so a wage of 1.01 a day for "
                  "300 days keeps him level with a labourer at 1 a day. In the seven-years "
                  "preset the learning is 700 shillings, a premium and seven years of "
                  "keeping, which charges 105 a year and needs a wage of 1.35 a day for "
                  "the same net of 300. The difference, 102 shillings a year in the wage "
                  "bill, is what the long apprenticeship adds to the price of the trade's "
                  "work, and it is what the public pays. The capped preset keeps the "
                  "few-weeks trade and adds Sheffield's rule of one apprentice at a time, "
                  "with the pay rise the cap brings put at 20 percent, a figure written for "
                  "this lesson. The cutler's wage goes from 1.01 to about 1.21 shillings a "
                  "day, and his net advantage from 300 to 360.60, which is 60.60 above the "
                  "labourer's. The capped preset's other tiles show the trade before the cap, "
                  "the weeks preset again, so its spread there is still nothing; the limit "
                  "tile and the ranking under it show the trade after. Smith's claim is that "
                  "the cap does this; the 20 percent is only a way of showing its size."),
            ("def", ("A cap on entry (this lab's term)",
                     "A limit on how many may enter a trade, with a stated rise in its pay "
                     "that the limit is supposed to bring. The rise is the lesson's "
                     "assumption: Smith says the cap restrains competition and keeps "
                     "wages above their level, and gives no figure.")),
            ("p", "The corporate trade is, he says, a bargain among tradesmen. Each class "
                  "&ldquo;was eager to establish regulations proper for this purpose, and, "
                  "provided it was allowed to do so, was willing to consent that every other "
                  "class should do the same.&rdquo; Within the town it is &ldquo;as broad "
                  "as long&rdquo;, as they say. The gain is in dealing with the country. "
                  "&ldquo;The price which the town really pays for the provisions and "
                  "materials annually imported into it, is the quantity of manufactures and "
                  "other goods annually exported from it. The dearer the latter are sold, "
                  "the cheaper the former are bought.&rdquo; He supports it with an "
                  "observation: in every country of Europe &ldquo;at least a hundred "
                  "people&rdquo; acquire great fortunes from small beginnings in trade and "
                  "manufactures for one who does so by farming. He then argues that the "
                  "ploughman is not the dullard he is taken for, since farming demands "
                  "more judgment than a mechanic's work, and says that in China and "
                  "Indostan country labourers are said to rank above artificers."),
            ("p", "The most quoted sentence follows. &ldquo;People of the same trade seldom "
                  "meet together, even for merriment and diversion, but the conversation "
                  "ends in a conspiracy against the public, or in some contrivance to raise "
                  "prices.&rdquo; Smith does not propose to stop them meeting, which he says "
                  "no law could do consistent with liberty and justice, but says that the "
                  "law &ldquo;ought to do nothing to facilitate such assemblies, much less "
                  "to render them necessary&rdquo;: a public register of the trade facilitates "
                  "them, a common fund for the poor, sick, widows and orphans renders them "
                  "necessary, and an incorporation makes the majority bind the whole. He "
                  "also denies the pretence that corporations discipline workmen. The real "
                  "discipline is the customer's, and in incorporated towns tolerable work "
                  "has to be done in the suburbs and smuggled in."),
            ("p", "The second way of unequalising is the reverse: increasing competition by "
                  "bursaries and scholarships. Churchmen are mostly educated at public or "
                  "pious expense, so the church is crowded with people willing to accept "
                  "less than their education would otherwise earn, and &ldquo;the "
                  "competition of the poor takes away the reward of the rich&rdquo;. Smith "
                  "compares a curate's pay with a mason's under the Statute of Labourers "
                  "and finds the curate's was lower, and says that in law and physic, if an "
                  "equal share of students were educated at the public expense, the "
                  "professions would fall. Men of letters, the &ldquo;unprosperous race&rdquo;, "
                  "are in that case already. He closes the point with an observation "
                  "that cuts against what a reader might expect: this inequality is, "
                  "&ldquo;upon the whole, perhaps rather advantageous than hurtful to the "
                  "public&rdquo;, because cheap education outweighs the lowered rank of the "
                  "teacher. The next lesson reads the third way, the obstruction of the "
                  "movement of labour from place to place."),
        ],
        "lab": ("wonkit", {
            "mode": "advantage",
            "view": "net",
            "money_unit": "s",
            "preset": "weeks",
            "presets": [
                {"id": "weeks", "label": "A trade learned in a few weeks, written for this lesson",
                 "profit": 10,
                 "employments": "labourer, 1, 300, 0, 1, 0; cutler, 101/100, 300, 20, 20, 0",
                 "expect": {
                           "wadAnnual": "labourer 300s; cutler 303s",
                           "wadLearnYear": "labourer 0s; cutler 3s",
                           "wadNet": "labourer 300s; cutler 300s"}},
                {"id": "seven-years", "label": "The same trade with seven years' apprenticeship, written for this lesson",
                 "profit": 10,
                 "employments": "labourer, 1, 300, 0, 1, 0; cutler, 27/20, 300, 700, 20, 0",
                 "expect": {
                           "wadAnnual": "labourer 300s; cutler 405s",
                           "wadLearnYear": "labourer 0s; cutler 105s",
                           "wadNet": "labourer 300s; cutler 300s"}},
                {"id": "capped", "label": "Sheffield's one apprentice at a time, the rise written for this lesson",
                 "profit": 10,
                 "employments": "labourer, 1, 300, 0, 1, 0; cutler, 101/100, 300, 20, 20, 0",
                 "limit": "cutler, 1, 20",
                 "expect": {
                           "wadLimited": "cutler (entry capped at 1): wage 1.01s → ≈ 1.21s a day, net 300s → 360.60s",
                           "wadRankAfter": "cutler > labourer"}},
            ],
            "panel_title": "What a long apprenticeship and a cap on entry do to pay",
            "panel_intro": (
                "A labourer and a cutler, netted as the trades of the first lesson were, "
                "with the cost of learning pushed up by a long apprenticeship, or with entry capped. Watch "
                "the cutler's yearly learning charge in the second preset and his net "
                "advantage in the third."
            ),
        }),
        "steps_title": "Pricing a restraint on entry",
        "steps_intro": "Four steps, for a trade whose entry the law has narrowed.",
        "steps": [
            ("Find the learning charge without the restraint",
             "Use the short learning cost and the same working years and profit. This is "
             "the baseline wage that keeps the trade level with common labour."),
            ("Raise the cost of learning",
             "A longer apprenticeship adds the premium, the keeping and the years' "
             "forgone pay to the learning cost. Charge the larger sum the same way."),
            ("Find the wage that restores the net",
             "Add the new yearly charge to what common labour earns, and divide by the "
             "days worked. The difference from the baseline is the extra the public "
             "pays for the same work."),
            ("Compare with a cap",
             "A cap does not raise the cost of learning; it raises the trade's pay "
             "directly by keeping entrants out. The net advantage of the capped trade "
             "above the others' is what the lab shows as the gap."),
        ],
        "worked": {
            "title": "What seven years add",
            "intro": [
                "Take the seven-years preset. The learning, a premium and seven years of "
                "keeping, is 700 shillings, replaced over 20 working years with 10 percent "
                "profit. A labourer earns 300 shillings in a year.",
            ],
            "lines": [
                "learning replaced a year:  700 / 20 = 35",
                "profit on the learning:  10% of 700 = 70",
                "learning charged a year:  35 + 70 = 105",
                "wage needed:  300 + 105 = 405 a year",
                "wage a day:  405 / 300 = 27/20",
            ],
            "after": [
                "The weeks preset needs only 303 a year for the same net: 3 for the "
                "learning and 300 to match the labourer. The seven years add 102 shillings "
                "to the wage bill of a trade whose work, Smith says, needs a few weeks of "
                "teaching at most, and the buyer of the work pays them.",
            ],
        },
        "quiz_title": "Who pays for restraining entry",
        "quiz": [
            {"q": "Which of these is a way in which, on Smith's account, a long term of "
                  "apprenticeship restrains competition?",
             "a": ["It forbids masters from taking any apprentices",
                   "It raises the expense of education, so fewer can afford to enter",
                   "It forces apprentices to move to other towns",
                   "It makes the trade harder to learn than it otherwise would be"],
             "c": 1,
             "why": "&ldquo;A long term of apprenticeship restrains it more indirectly, but "
                    "as effectually, by increasing the expense of education.&rdquo; The "
                    "limitation of the number of apprentices is the direct restraint, and "
                    "Smith argues the trades can be learned in weeks, so the term does "
                    "not make learning harder."},
            {"q": "In the seven-years preset the learning is 700 shillings over 20 working "
                  "years at 10 percent profit, and a labourer earns 300 a year. What yearly "
                  "wage keeps the cutler level with the labourer?",
             "a": ["300", "335", "405", "1,000"],
             "c": 2,
             "why": "The learning charges `700 / 20 + 10% of 700 = 35 + 70 = 105` a year, "
                    "so `300 + 105 = 405`. Three hundred ignores the learning, and 335 "
                    "leaves out the profit on it."},
            {"q": "Why does Smith say incorporated trades in a town can raise their prices "
                  "without making themselves poorer?",
             "a": ["Each trade pays more for what it buys from the others but charges "
                   "more for its own, so within the town it is as broad as long",
                   "The king takes a share of every fine",
                   "The country has no competitors, so the town can charge what it likes "
                   "to every other town",
                   "Corporations pay their journeymen less"],
             "c": 0,
             "why": "&ldquo;so far it was as broad as long, as they say&rdquo;. The gain is "
                    "in dealing with the country, where the dearer the town's goods sell "
                    "the cheaper its provisions are bought; it is not a claim about "
                    "journeymen's wages."},
            {"q": "On what ground does Smith say the law should not make tradesmen "
                  "register their names and abodes in a public list?",
             "a": ["It would make them pay a fine to the crown",
                   "It would give guilds a revenue",
                   "It would let workmen compare each other's wages",
                   "It would facilitate the assemblies in which they conspire to raise prices"],
             "c": 3,
             "why": "A public register &ldquo;connects individuals who might never "
                    "otherwise be known to one another, and gives every man of the trade a "
                    "direction where to find every other man of it&rdquo;. It is the "
                    "lowest of the three steps in his list, below a common fund and "
                    "incorporation."},
        ],
        "mistakes": [
            ("Reading Smith as saying all training is waste",
             "Part I says skilled labour must replace the cost of its education, and the "
             "preset gives the craftsman a wage that does. What Part II attacks is a "
             "term set by law at more than the trade needs, which he says is a few days "
             "in a common mechanic trade. He grants that dexterity of hand needs practice."),
            ("Taking the quote about conspiracy as a call to ban meetings",
             "He says no law could prevent such meetings consistent with liberty and "
             "justice. His point is that the law should not facilitate or require them, "
             "and he lists the three steps from a register to an incorporation."),
            ("Treating Smith's account of corporations as the whole story",
             "He writes against the corporation as it stood in 1776. Later historians "
             "of the guilds, writing after him, have argued that apprenticeship also "
             "secured training and that guilds did more than restrain trade. The chapter "
             "gives the case against, at length, and the lesson reports it so."),
        ],
        "standard": (
            "Finish when you can price what a long apprenticeship adds to a trade's wage.",
            "Given a trade's cost and years of learning, the ordinary profit and the "
            "pay of common labour, compute the yearly learning charge and the wage "
            "that keeps the trade level, and the extra a longer apprenticeship adds."
        ),
        "note": (
            "The arithmetic assumes the seven years' cost is all lost to the learner, "
            "which is Smith's case against them and not a finding. The 20 percent rise "
            "in the capped preset is the lesson's. Historians of the guilds divide: "
            "Sheilagh Ogilvie has argued the Smithian case against guild restrictions at "
            "length, while S. R. Epstein and others have argued that guilds also trained "
            "workers and vouched for quality; the lab does not decide between them. Capital's "
            "lesson <em>Bloody Legislation and the Forcing Down of Wages</em> reads "
            "the statutes of labourers that Smith mentions in passing."
        ),
    },
    # ---------------------------------------------------------------- 05
    # PSU text l. 4448-4500 (third way, the poor laws), l. 4501-4585
    # (settlement statutes), l. 4586-4633 (certificates), l. 4634-4667 (unequal
    # price of labour, natural liberty), l. 4668-4727 (assessed wages, the
    # assize of bread, conclusion).
    {
        "slug": "the-law-of-settlements",
        "title": "The Law of Settlements",
        "module": "Book I, Chapter 10, Part II · The Free Circulation of Labour",
        "one_line": "The third way the policy of Europe unequalises employments is to stop labour moving, and in England the law of settlements does it more than a boundary of the sea.",
        "summary": (
            "Smith's last complaint in the chapter is that the policy of Europe obstructs "
            "the free circulation of labour and stock, from trade to trade and from place "
            "to place. The apprenticeship laws do the first; in England the law of "
            "settlements, which sends a poor man back to his own parish, does the second. "
            "Compare two neighbouring parishes whose wages differ because workers may not "
            "cross between them, and see what wages do when the barrier is lifted."
        ),
        "key": [
            "pay gap = wage in B − wage in A",
            "a year's pay = wage a day × days worked",
            "free movement tends to equal net pay",
            "a barrier keeps the gap open",
            "spread = highest net − lowest net",
        ],
        "key_label": "A barrier between two parishes",
        "concepts_intro": (
            "The last piece of the chapter is the one that most plainly brings the mechanism "
            "of the whole chapter home: if free movement levels wages, a barrier "
            "to movement should show up as a difference in them."
        ),
        "concepts": [
            ("The third way",
             "The Statute of Apprenticeship obstructs the movement of labour from one "
             "employment to another in the same place; the exclusive privileges of "
             "corporations obstruct it from one place to another in the same employment. "
             "The poor laws, peculiar to England, obstruct even common labour's movement "
             "from parish to parish."),
            ("Settlement",
             "Under the Elizabethan poor law each parish had to keep its own poor. Who "
             "belonged to which parish therefore mattered, and statute after statute "
             "made it harder for a poor man to gain a new settlement. A newcomer who "
             "might become chargeable could be removed unless he rented a ten-pound "
             "tenement or gave security."),
            ("Certificates",
             "A certificate from the home parish, signed and allowed, obliged any other "
             "parish to take him until he became actually chargeable. Smith's source, "
             "Dr Burn, says officers had reason to grant them seldom."),
        ],
        "read_title": "The third restraint, and the English poor man's boundary",
        "read_intro": (
            "Smith's account is a history of statutes, and its point is in two sentences "
            "at the end. Read the statutes quickly and the conclusion carefully."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 10, Part II.</strong> &ldquo;Thirdly, the policy "
                  "of Europe, by obstructing the free circulation of labour and stock, both "
                  "from employment to employment, and from place to place, occasions, in "
                  "some cases, a very inconvenient inequality in the whole of the "
                  "advantages and disadvantages of their different employments.&rdquo; The "
                  "apprenticeship statute obstructs movement between trades in one place, "
                  "and the privileges of corporations obstruct it between places in one "
                  "trade."),
            ("p", "His picture of the first is a town with two manufactures, one "
                  "advancing and one declining, the advancing one paying high wages and "
                  "the declining one bare subsistence, each unable to lend the other "
                  "hands. The arts of weaving plain linen and plain silk are almost the "
                  "same, he says, and a linen or silk weaver &ldquo;might become a tolerable "
                  "workman in a very few days&rdquo; at plain woollen. Without the statute "
                  "&ldquo;their wages would neither rise too high in the thriving, nor "
                  "sink too low in the decaying manufacture&rdquo;. With it, the weavers of "
                  "a decaying trade have no choice but to become common labourers, for "
                  "which their habits fit them worse, and &ldquo;They generally, "
                  "therefore, chuse to come upon the parish&rdquo;. Corporation laws "
                  "obstruct stock less than labour: &ldquo;It is everywhere much easier "
                  "for a wealthy merchant to obtain the privilege of trading in a "
                  "town-corporate, than for a poor artificer to obtain that of working "
                  "in it.&rdquo;"),
            ("p", "Then the English peculiarity. The obstruction by corporation laws "
                  "&ldquo;is common, I believe, to every part of Europe. That which is "
                  "given to it by the poor laws is, so far as I know, peculiar to "
                  "England.&rdquo; He gives the history in steps. After the monasteries "
                  "were destroyed, the 43rd of Elizabeth made every parish provide for "
                  "its own poor. Who counted as a parish's poor therefore became a question, "
                  "and the 13th and 14th of Charles II answered that forty days' "
                  "undisturbed residence gave a settlement, but that within the forty days "
                  "two justices could remove any new inhabitant unless he rented a "
                  "tenement of ten pounds a year or gave security. Later statutes closed "
                  "the loopholes, so that the forty days were counted from a notice read "
                  "in church on Sunday, and the other four ways of gaining a settlement, "
                  "by being taxed to parish rates, by serving a year in a parish office, "
                  "by apprenticeship and by being hired for a year, were each shut to "
                  "anyone with nothing but his labour: nobody gains the first two without "
                  "the vote of the whole parish, and no married man can easily gain the "
                  "last two."),
            ("p", "The security a justice could require was left to discretion, but "
                  "&ldquo;they cannot well require less than thirty pounds&rdquo;, a "
                  "sum &ldquo;which scarce any man who lives by labour can give&rdquo;. "
                  "Certificates were the invention to restore movement, and Smith quotes "
                  "Dr Burn on why parishes would grant them seldom, because it is far "
                  "more than an equal chance that the parish will have the certificated "
                  "person back, in a worse condition. Smith's own moral: certificates "
                  "&ldquo;ought always to be required by the parish where any poor man comes "
                  "to reside, and that they ought very seldom to be granted by that which "
                  "he purposes to leave&rdquo;. A certificate carries no testimonial, says "
                  "Burn, and it is discretionary to grant it."),
            ("p", "Then the claim that makes the chapter's mechanism testable. &ldquo;The "
                  "very unequal price of labour which we frequently find in England, in "
                  "places at no great distance from one another, is probably owing to the "
                  "obstruction which the law of settlements gives to a poor man who would "
                  "carry his industry from one parish to another without a "
                  "certificate.&rdquo; In Scotland, where there is no such difficulty, "
                  "wages may rise a little near a great town and fall gradually as the "
                  "distance grows, but there are no &ldquo;sudden and unaccountable "
                  "differences in the wages of neighbouring places&rdquo;. In England "
                  "&ldquo;it is often more difficult for a poor man to pass the "
                  "artificial boundary of a parish, than an arm of the sea, or a ridge of "
                  "high mountains&rdquo;."),
            ("p", "The lab models two parishes as two employments in the same trade, "
                  "common labour, one on each side of the boundary. In the settlement "
                  "preset, written for this lesson, the labourer in parish A earns 1 "
                  "shilling a day and in parish B 3/2, over 312 days. The year's money "
                  "wage is 312 in A and 468 in B, a spread of 156 shillings, and the "
                  "ranking puts B first by a half. If a man could simply walk from A to B, "
                  "Smith's mechanism says A's labourers would go until the two wages "
                  "met. The free preset sets both at 5/4 of a shilling, 390 a year, and "
                  "the spread is nothing. Smith's mechanism and the lab agree about what "
                  "has to happen. What they leave open is how long it takes, and how many "
                  "of A's labourers are needed."),
            ("p", "He ends with a remark on whether the common people felt it. They have, "
                  "he says, &ldquo;for more than a century together&rdquo; suffered this "
                  "&ldquo;without a remedy&rdquo;, and though men of reflection have "
                  "complained of it, it has never been the object of a general clamour, "
                  "such as that against general warrants. &ldquo;There is scarce a poor "
                  "man in England, of forty years of age, I will venture to say, who has "
                  "not, in some part of his life, felt himself most cruelly oppressed by "
                  "this ill-contrived law of settlements.&rdquo; To remove a man who has "
                  "committed no misdemeanour from the parish where he chooses to reside "
                  "is, he writes, &ldquo;an evident violation of natural liberty and "
                  "justice&rdquo;."),
            ("p", "The chapter's last pages are on a smaller matter that bears on the same "
                  "theme: the law's attempts to fix wages. Parliament had stopped assessing "
                  "them by general laws and by the justices' orders, but still tried "
                  "now and then in particular trades. The 8th of George III forbids master "
                  "tailors in and round London to give, or their men to accept, more than "
                  "two shillings and sevenpence halfpenny a day except in general mourning. "
                  "&ldquo;Whenever the legislature attempts to regulate the differences "
                  "between masters and their workmen, its counsellors are always the "
                  "masters.&rdquo; When the regulation favours the workmen, as the law that "
                  "they be paid in money and not in goods does, it is just; when it favours "
                  "the masters, it is not always. The statute does what masters sometimes "
                  "try by private bond, and if the law dealt impartially the workmen's "
                  "combination, which it punishes severely, would be treated like the "
                  "masters'. The closing sentence of the chapter says the proportions "
                  "between the rates of wages and profit in different employments are "
                  "little affected by whether the society is rich or poor, advancing, "
                  "stationary or declining: such revolutions &ldquo;must, in the end, "
                  "affect them equally in all different employments&rdquo;. The next "
                  "chapter, on the rent of land, turns from the two shares that have "
                  "occupied the book so far to the third."),
        ],
        "lab": ("wonkit", {
            "mode": "advantage",
            "view": "net",
            "money_unit": "s",
            "preset": "settlement",
            "presets": [
                {"id": "settlement", "label": "Two parishes a mile apart, wages written for this lesson",
                 "profit": 0,
                 "employments": "parish-a, 1, 312, 0, 1, 0; parish-b, 3/2, 312, 0, 1, 0",
                 "expect": {
                           "wadAnnual": "parish-a 312s; parish-b 468s",
                           "wadSpread": "156s (parish-b over parish-a)"}},
                {"id": "free", "label": "The same two parishes with labour free to move, written for this lesson",
                 "profit": 0,
                 "employments": "parish-a, 5/4, 312, 0, 1, 0; parish-b, 5/4, 312, 0, 1, 0",
                 "expect": {
                           "wadAnnual": "parish-a 390s; parish-b 390s",
                           "wadSpread": "0s: every employment nets the same"}},
            ],
            "panel_title": "Two parishes, one boundary",
            "panel_intro": (
                "Each parish is a row: the common labourer's wage a day and the days "
                "worked in a year, with no learning to charge. The lab shows each "
                "parish's year and the spread between them. Compare the settlement preset "
                "with the free one."
            ),
        }),
        "steps_title": "Reading a wage gap as a barrier",
        "steps_intro": "Four steps, for two places whose wages differ.",
        "steps": [
            ("Put the two places side by side",
             "Take the same sort of labour in each and the days worked, and find each "
             "year's money wage."),
            ("Find the spread",
             "Subtract the lower from the higher. It is what a worker would gain by "
             "moving, if moving cost nothing."),
            ("Ask what keeps it open",
             "If there is no difference in the work, the pleasantness of the place or "
             "the steadiness of the job, Smith's mechanism says workers will move until "
             "the spread closes. A spread that lasts needs an explanation."),
            ("Name the barrier",
             "Smith's candidate is the law of settlements. A fair reader asks for the "
             "other explanations the figures cannot rule out: cost of travel, local "
             "demand for labour, ties of family."),
        ],
        "worked": {
            "title": "A mile apart",
            "intro": [
                "Take the settlement preset. A labourer in parish A earns 1 shilling a "
                "day, in B 3/2, and both work 312 days.",
            ],
            "lines": [
                "parish A:  1 · 312 = 312",
                "parish B:  3/2 · 312 = 468",
                "spread:  468 − 312 = 156",
                "B above A by:  156 / 312 = 1/2",
                "free preset:  5/4 · 312 = 390 in both, spread 0",
            ],
            "after": [
                "A labourer who could move would gain 156 shillings a year by crossing the "
                "boundary. The free preset is not a forecast of where wages would settle, "
                "only the case in which they have met.",
            ],
        },
        "quiz_title": "Wages and the boundaries of parishes",
        "quiz": [
            {"q": "In the settlement preset, parish A pays 1 shilling a day and parish B "
                  "3/2, both for 312 days. What is the spread in the year's money wage?",
             "a": ["156 shillings", "312 shillings", "468 shillings", "1/2 a shilling"],
             "c": 0,
             "why": "A's year is 312 and B's is `3/2 × 312 = 468`, so the spread is "
                    "`468 − 312 = 156`. The other options are A's year, B's year and "
                    "the difference in the daily wage."},
            {"q": "On Smith's account, what explains the very unequal price of labour in "
                  "neighbouring English parishes?",
             "a": ["Differences in the cost of food",
                   "The obstruction the law of settlements gives to a poor man who would "
                   "carry his industry from one parish to another",
                   "The statute that obliged masters to pay in money, not goods",
                   "The assize of bread"],
             "c": 1,
             "why": "&ldquo;is probably owing to the obstruction which the law of "
                    "settlements gives to a poor man&rdquo; who would move without a "
                    "certificate. The law about paying in money Smith praises as just, "
                    "and the assize of bread he says caused no sensible advantage."},
            {"q": "What does Smith say about the law of 8 George III that bars London master "
                  "tailors from paying more than 2s 7½d a day?",
             "a": ["It protects journeymen against their masters",
                   "It enforces by law what masters sometimes try by private bond, and is "
                   "in favour of the masters",
                   "It is equally just to masters and men, since both are bound",
                   "It was repealed as unworkable"],
             "c": 1,
             "why": "&ldquo;the 8th of George III. is in favour of the masters&rdquo;. He "
                    "says it enforces the regulation masters sometimes attempt to "
                    "establish by combinations, and that the workmen's complaint, that it "
                    "puts the ablest on a footing with the ordinary, &ldquo;seems perfectly "
                    "well founded&rdquo;. Smith does not say it was repealed."},
            {"q": "Why does Smith say corporation laws obstruct the movement of labour "
                  "more than that of stock?",
             "a": ["Stock cannot move at all",
                   "Merchants are exempt from every corporation law",
                   "Labour is cheaper to carry",
                   "It is everywhere much easier for a wealthy merchant to obtain the "
                   "privilege of trading in a town-corporate than for a poor artificer to "
                   "obtain that of working in it"],
             "c": 3,
             "why": "That is his sentence. Stock can move, so the other options are "
                    "wrong about what he says: merchants are not exempt, only better "
                    "placed to get a privilege."},
        ],
        "mistakes": [
            ("Reading a wage gap as proof of a barrier",
             "Smith infers the settlement law as the likely cause of unequal wages in "
             "neighbouring parishes, because he sees no other. The lab shows the spread "
             "and what would close it; it cannot show that a boundary is what keeps it "
             "open. Costs of travel, local demand and family are all other candidates."),
            ("Supposing Smith's complaint is about the poor laws as such",
             "He says the obstruction by the poor laws is peculiar to England and that "
             "it consists in the difficulty of gaining a settlement, which he calls "
             "perhaps the greatest disorder in the police of England. He does not argue here against "
             "relief for the poor. The 43rd of Elizabeth is the relief; the settlement "
             "statutes that followed are the obstruction."),
            ("Taking the closing paragraph as a law of wages",
             "The last sentence says the proportions between rates in different "
             "employments are little affected by a society's riches or poverty. It is a "
             "claim about proportions, not levels, and it refers back to the whole "
             "chapter's argument; the previous course reads what happens to the levels."),
        ],
        "standard": (
            "Finish when you can read a wage gap between two places as a spread.",
            "Given the wage and days worked in two places, compute each year's money wage, "
            "the spread between them, and say what Smith's mechanism predicts if labour "
            "could move freely."
        ),
        "note": (
            "A spread is a gap in the figures; whether it is caused by the law of "
            "settlements is Smith's inference, which the lab neither supports nor "
            "refutes. Historians of the poor law have disputed how far the settlement "
            "laws in practice obstructed movement, some finding removals rarer than the "
            "statutes allowed and others the barrier real. The lesson's wages are written "
            "for it. Smith's own figures for common labour at no great distance are in "
            "Chapter 8: eighteen pence a day in London and fourteen or fifteen a few miles "
            "off, a difference he says is not always enough to move a man from one parish "
            "to another."
        ),
    },
]
