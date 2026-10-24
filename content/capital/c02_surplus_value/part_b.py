"""From Money to Surplus Value, lessons 6-10 -- Volume I, Chapters 9 to 11.

Every quotation is copied from /mnt/project-files/capital-texts/volume-1-kerr.txt
(the Kerr edition of Volume I); the comment beside each lesson gives its line
numbers. Footnote numerals in the text are left out of the quotations, a
drop capital ("THE", "IT") is printed as an ordinary capital, and the
translator's double quotation marks inside a quotation are printed as single
curly quotes. Nothing else is changed.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    # Kerr vol. 1, l. 1929 (an exact expression for the degree of
    # exploitation); l. 1998 (16 lbs. of yarn); l. 1895, 1901, 1917, 1925,
    # 1932, 1940, 1984, 2008, 2024-2026 (figures and phrases).
    {
        "slug": "the-rate-of-surplus-value",
        "title": "The Rate of Surplus Value",
        "module": "Chapter 9 · The Rate of Surplus-Value",
        "one_line": "Surplus value is measured against the variable capital that produced it, s/v, which is the same ratio as surplus labour to necessary labour.",
        "summary": (
            "Marx sets the constant capital to zero, keeps the value newly created, and "
            "divides the surplus by the variable capital: £90 on £90 is 100%, not 90/500. "
            "Compute s/v from c, v and s, divide Marx's 20 lb of yarn into the parts that "
            "carry c, v and s, and see what the rate becomes when the whole capital is "
            "wrongly counted as v."
        ),
        "key": [
            "value of product = c + v + s",
            "value newly created = v + s",
            "rate of surplus value = s / v",
            "s / v = surplus labour / necessary labour",
            "s / (c + v) is the rate of profit instead",
        ],
        "key_label": "One ratio, two readings",
        "concepts_intro": (
            "Chapter 9 turns the last two chapters into a measure. Its first two sections "
            "are about how to compute it and how to see it in the product itself."
        ),
        "concepts": [
            ("Value product",
             "The product's value is c + v + s, but only v + s was created in the process; "
             "c reappears. So Marx puts c equal to zero, the way a cotton industry's profits "
             "are reckoned after deducting the cotton bought abroad."),
            ("The rate of surplus value",
             "s/v, the surplus measured against the part of capital whose change it is. The "
             "same ratio is surplus labour over necessary labour: the two halves of the "
             "working day."),
            ("The product in parts",
             "Because the whole value is in the product, each component can be shown as a "
             "share of it: so many pounds of yarn carry the constant capital, so many the "
             "wages, so many the surplus."),
        ],
        "read_title": "Marx's definition, then the yarn in parts",
        "read_intro": (
            "The first passage closes section 1 with the sentence that gives the ratio its "
            "second name. The second, from section 2, divides the yarn."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 9, §1.</strong> &ldquo;The rate of surplus-value "
                  "is therefore an exact expression for the degree of exploitation of "
                  "labour-power by capital, or of the labourer by the capitalist.&rdquo;"),
            ("p", "Every company report gives its profit as a percentage of the capital "
                  "employed, and that is the first way anyone would measure a surplus. Marx's "
                  "point in this chapter is that, for the question he is asking, it is the "
                  "wrong denominator. Take his figures. A capital of £500 is laid out as £410 of "
                  "constant capital and £90 of variable. At the end the product is worth £410 + "
                  "£90 + £90 = £590, and the surplus is £90."),
            ("p", "Two steps follow. First, only what is consumed counts. If the machinery is "
                  "worth £1,054 and wears £54 in the period, only £54 is in the £410; counting "
                  "the other £1,000 on both sides would give £1,500 and £1,590, and the surplus "
                  "would still be £90. Second, the constant capital only reappears. The value "
                  "actually created is v + s, £180, not £590. So Marx sets c equal to zero, "
                  "which is &ldquo;merely an application of a mathematical rule&rdquo; and what "
                  "anyone does who reckons England's cotton profits after deducting what was "
                  "paid for American and Indian cotton."),
            ("def", ("Rate of surplus value",
                     "The ratio s/v of surplus value to the variable capital advanced. On "
                     "Marx's figures, 90/90 = 100%.")),
            ("p", "Now the second reading. The worker spends part of the day producing the "
                  "value of his own labour-power, which Marx calls necessary labour-time, and "
                  "the rest producing surplus value, surplus labour-time. Since v is the value "
                  "of the labour-power and s is the product of the surplus part, s/v equals "
                  "surplus labour over necessary labour. One ratio counts materialised labour, "
                  "the other living labour. What distinguishes a slave society from a wage "
                  "society, Marx adds, is &ldquo;the mode in which this surplus-labour is in "
                  "each case extracted&rdquo;, not whether it is."),
            ("p", "Hence the line that gives this lesson its misconception. Reckoned in the "
                  "usual way, £90 on £500 is 18%, &ldquo;a rate so low as possibly to cause a "
                  "pleasant surprise to Mr. Carey and other harmonisers&rdquo;: Henry Carey, "
                  "the American economist who argued that the interests of capital and labour "
                  "are in harmony. But the rate is &ldquo;not 90/500 but 90/90 or 100%&rdquo;. "
                  "The 18% is a real ratio too, the rate of profit, and Volume III is built on "
                  "it. It is not the measure of how the working day is divided."),
            ("p", "The method, then, in Marx's summary: take the value of the product, set the "
                  "constant part to zero, and what is left is the value created; split it into "
                  "v and s; divide. He works two examples. A mill of 10,000 spindles in 1871 "
                  "spends £378 a week on cotton, wear, rent, coal, gas and oil and £52 on wages, "
                  "and sells "
                  "its yarn for £510: s is £80, and s/v is 80/52, or 153 11/13%. And an English "
                  "acre of wheat in 1815, from the economist William Jacob's figures, yields £3 "
                  "11s of surplus against £3 10s of wages, a little over 100%."),
            ("p", "Section 2 shows the same proportions in the product itself. Go back to the "
                  "twelve-hour day of “The Labour Process and the Production of Surplus "
                  "Value”: 20 lb of yarn worth 30s, of which 24s is constant capital, 3s "
                  "variable, 3s surplus."),
            ("p", "<strong>Volume I, Chapter 9, §2.</strong> &ldquo;If the value of 30s. is "
                  "contained in 20 lbs. of yarn, then 8/10ths of this value, or the 24s. that "
                  "form its constant part, is contained in 8/10ths of the product or in 16 lbs. "
                  "of yarn.&rdquo;"),
            ("p", "So 16 lb of the yarn carry the constant capital, 13 1/3 lb for the cotton "
                  "and 2 2/3 lb for the wear; 2 lb carry the wages; 2 lb carry the surplus. Of "
                  "course every pound was spun, and every pound contains cotton. The division "
                  "is of value, not of fibre. Marx's image is that the spinner might as well "
                  "have spun the last 4 lb &ldquo;out of air&rdquo;: all the value of the cotton "
                  "and the wear is concentrated in the other 16."),
            ("p", "The manufacturer reads the same division in time: in the first 8 hours the "
                  "spinner produces yarn equal in value to the day's cotton, in the next hour "
                  "and 36 minutes the wear, in the next hour and 12 minutes his wages, and in "
                  "the last hour and 12 minutes the surplus. That is &ldquo;a perfectly correct "
                  "method&rdquo;, Marx says, and an easy step from it to a very wrong belief, "
                  "which is the next lesson. The 2 lb that carry the surplus he names surplus "
                  "produce."),
            ("p", "The word &ldquo;exploitation&rdquo; is where most readers stop and argue, "
                  "and fairly. In Marx's sense it is a defined ratio, surplus labour to "
                  "necessary labour, and it implies that the surplus is unpaid labour only if "
                  "labour alone creates value. An economist who credits capital with a "
                  "productive contribution reads the same 100% as a division of income between "
                  "two factors and sees nothing that needs the word. The arithmetic is "
                  "common ground; the name is the dispute."),
            ("p", "The lab divides any c, v and s. Marx's yarn gives 100% and 16, 2 and 2 lb. "
                  "The second preset makes the misreading concrete: all 27s advanced entered as "
                  "if it were v, which gives 1/9, about 11%, the same number the status line "
                  "prints as s over the whole capital for the yarn. The third is the six-hour "
                  "day of the same mill, where s is zero and the 10 lb of yarn split 8 and 2."),
            ("p", "Marx's spinner in the time-reckoning makes the surplus in the last hour and "
                  "12 minutes. The next lesson, on Senior's “last hour”, follows a professor "
                  "who took that literally."),
        ],
        "lab": ("capkit", {
            "mode": "surplus",
            "view": "rate",
            "money_unit": "s",
            "qty_unit": "lb",
            "preset": "yarn",
            "presets": [
                {"id": "yarn", "label": "Marx's 20 lb of yarn: 24s of c, 3s of v, 3s of s",
                 "c": 24, "v": 3, "s": 3, "output": 20, "expect": {"suRate": "1 = 100%", "suParts": "c: 16 lb, v: 2 lb, s: 2 lb"}},
                {"id": "whole-capital", "label": "The misreading: all 27s advanced counted as v",
                 "c": 0, "v": 27, "s": 3, "output": 20, "expect": {"suRate": "1/9 = 11.11%", "suParts": "c: 0 lb, v: 18 lb, s: 2 lb"}},
                {"id": "six", "label": "The six-hour day: 12s of c, 3s of v, no surplus",
                 "c": 12, "v": 3, "s": 0, "output": 10, "expect": {"suRate": "0 = 0%", "suParts": "c: 8 lb, v: 2 lb, s: 0 lb"}},
            ],
            "panel_title": "The rate, and the product in parts",
            "panel_intro": (
                "Type c, v and s in shillings and the weight of the product. The lab divides "
                "s by v and splits the product in proportion to c, v and s. The status line "
                "also prints s over the whole capital, so you can see the two ratios side by "
                "side."
            ),
        }),
        "steps_title": "Computing the rate of surplus value",
        "steps_intro": "Marx's own method, in four steps.",
        "steps": [
            ("Take the value of the product",
             "Write it as c + v + s, counting in c only the means of production actually "
             "consumed."),
            ("Set c to zero",
             "What remains, v + s, is the value created in the process. If s is given, v is "
             "the remainder, and the other way round."),
            ("Divide s by v",
             "The quotient is the rate of surplus value. The same figure is surplus labour-time "
             "over necessary labour-time."),
            ("Split the product if asked",
             "Each part of the value is carried by the same share of the product: c/(c + v + s) "
             "of the weight for c, and so on."),
        ],
        "worked": {
            "title": "£90 on £90, and 20 lb of yarn",
            "intro": [
                "Take Marx's two cases. A capital of £500 is £410 of c and £90 of v, and "
                "yields £90 of s. A day's yarn is 20 lb worth 30s, made of 24s of c, 3s of v "
                "and 3s of s. You want both rates and the yarn in parts.",
            ],
            "lines": [
                "value created:  £90 + £90 = £180",
                "s/v = 90/90 = 100%   (s/C = 90/500 = 18%)",
                "yarn:  s/v = 3/3 = 100%",
                "c:  20 · 24/30 = 16 lb",
                "v:  20 · 3/30 = 2 lb;  s:  20 · 3/30 = 2 lb",
            ],
            "after": [
                "Both rates are 100%: the worker in each case works half the day for himself "
                "and half for the capitalist. The 18% is a different ratio, and it hides that "
                "half.",
            ],
        },
        "quiz_title": "Measuring the surplus",
        "quiz": [
            {"q": "On Marx's figures c = £410, v = £90 and s = £90. What is the rate of "
                  "surplus value?",
             "a": ["18%", "About 22%", "100%", "50%"],
             "c": 2,
             "why": "s/v is `90/90`, 100%. 18% is s over the whole capital, about 22% is s over "
                    "c, and 50% is s over the value created, v + s. Each is a real ratio and "
                    "none of them is s/v."},
            {"q": "Twenty pounds of yarn are worth 30s: 24s of c, 3s of v and 3s of s. How "
                  "many pounds of the yarn represent the surplus value?",
             "a": ["2 lb", "3 lb", "4 lb", "16 lb"],
             "c": 0,
             "why": "The surplus is `3/30` of the value, so it is carried by `3/30` of the "
                    "weight, `20 · 1/10 = 2` lb. Four pounds carry v and s together; 16 lb "
                    "carry c; 3 is the surplus in shillings, not in pounds of yarn."},
            {"q": "What does setting c equal to zero do in Marx's method?",
             "a": ["Shows that the means of production have no value",
                   "Leaves the value created in the process, v + s, from which s/v is computed",
                   "Removes the surplus value from the calculation",
                   "Assumes the capitalist owns no machinery"],
             "c": 1,
             "why": "Constant capital only reappears in the product, so dropping it leaves the "
                    "new value. It does not deny that c has value, it keeps s in the "
                    "calculation, and it says nothing about what the capitalist owns."},
            {"q": "If the rate of surplus value is 100%, what share of the working day is "
                  "surplus labour?",
             "a": ["A quarter", "Half", "All of it", "It depends on how long the day is"],
             "c": 1,
             "why": "s/v is surplus labour over necessary labour, so 100% means the two are "
                    "equal, each half the day, whatever its length. The length fixes how many "
                    "hours each half is, not the share."},
        ],
        "mistakes": [
            ("Dividing the surplus by the whole capital",
             "It is the usual way to reckon a return, and it gives £90 on £500, 18%. Marx's "
             "point is that this mixes in the constant capital, which only reappears. The "
             "whole-capital preset shows the same error on the yarn: all 27s entered as v "
             "gives about 11%, against 100% for s/v. The working day is still divided half and "
             "half."),
            ("Taking the value of the product for the value created",
             "The yarn is worth 30s, but only 6s was created in the twelve hours; the other "
             "24s was already in the cotton and the spindle. In Marx's £ example the product "
             "is £590 and the value created £180."),
            ("Reading the 16 lb as yarn the spinner did not spin",
             "Every pound of the 20 was spun and contains cotton. The 16 lb are the share of "
             "the product whose value equals the constant capital: a division of value, which "
             "Marx shows in weight to make it visible."),
        ],
        "standard": (
            "Finish when you can compute s/v and split a product into its parts.",
            "Given c, v and s, compute the rate of surplus value and the value created, "
            "distinguish s/v from s over the whole capital, and compute the share of a "
            "product that carries each of c, v and s."
        ),
        "note": (
            "The chapter's examples assume, as Marx says of Jacob's acre, that the price of "
            "the product is the same as its value; the 1871 mill's s is read from its prices "
            "on that assumption. Whether s/v measures exploitation, rather than a division of "
            "income between labour and capital, depends on the labour theory of value. The "
            "yarn and the £410, £90 and £90 are Marx's figures; the money unit is lab-wide, so "
            "the lab carries the yarn and the £ example is done in the worked lines."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Kerr vol. 1, l. 2030 (Senior summoned to Manchester); l. 2034 (the
    # whole net profit is derived from the last hour); l. 2037-2047
    # (Marx's reply, 5¾ hours, 126 2/23%, "82 14/32%", "all bosh").
    {
        "slug": "seniors-last-hour",
        "title": "Senior's “Last Hour”",
        "module": "Chapter 9 · The Rate of Surplus-Value",
        "one_line": "Senior claimed the whole net profit came from the last hour of an 11½-hour day; on Marx's reckoning an hour less still leaves a rate of surplus value of about 83%.",
        "summary": (
            "In 1836 the Oxford economist Nassau Senior argued against shorter hours that "
            "a mill's net profit is made in the last hour of the day. Compute the rate of "
            "surplus value on his 11½-hour day, after one hour is cut, after an hour and a "
            "half, and on the 13-hour day he said would double the profit, and see where his "
            "arithmetic went wrong."
        ),
        "key": [
            "Senior: the last hour of 11½ is all profit",
            "Marx: 5¾ h necessary, 5¾ h surplus",
            "an hour cut: 4¾ / 5¾ = 19/23",
            "13 hours: 7¼ / 5¾ = 29/23, not double",
            "c goes over by quality, not by hours",
        ],
        "key_label": "The last hour, recomputed",
        "concepts_intro": (
            "Section 3 of Chapter 9 is a story with a sum in it. The sum is wrong in an "
            "instructive way."
        ),
        "concepts": [
            ("Senior's claim",
             "Of 23 half-hours, 20 replace the capital, 1 replaces the wear on the mill, and "
             "the last 2 produce the net profit. Cut an hour and the profit vanishes."),
            ("The lumping",
             "Senior put machinery, raw material and wages in one sum, so it looked as if "
             "the worker spent most of the day replacing the cotton and the mill."),
            ("Marx's correction",
             "Separate c from v. Suppose, as Marx does, that the separated account keeps the "
             "manufacturers' story and shows wages and net profit equal: then the day is half "
             "necessary and half surplus labour, and an hour off the day takes an hour off the "
             "surplus, not all of it."),
        ],
        "read_title": "The scene, then Senior's analysis and Marx's reply",
        "read_intro": (
            "Marx opens section 3 like the start of a tale, and then quotes Senior at "
            "length. The lesson reads both."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 9, §3.</strong> &ldquo;One fine morning, in the "
                  "year 1836, Nassau W. Senior, who may be called the bel-esprit of English "
                  "economists, well known, alike for his economical &lsquo;science,&rsquo; and "
                  "for his beautiful style, was summoned from Oxford to Manchester, to learn in "
                  "the latter place the political economy that he taught in the "
                  "former.&rdquo;"),
            ("p", "Nassau William Senior was the first Drummond Professor of Political Economy "
                  "at Oxford and a serious economist, the author of the abstinence theory of "
                  "profit that Marx's capitalist borrowed in “The Labour Process and the "
                  "Production of Surplus Value”. The Factory Act of 1833 had limited the hours "
                  "of young persons, and the movement for a ten-hour day was growing. The "
                  "Manchester mill-owners wanted an economist on their side, and Senior wrote "
                  "up what they taught him as Letters on the Factory Act, published in 1837. "
                  "Under the Act, he wrote, a mill employing anyone under 18 could work 11½ "
                  "hours a day, and then:"),
            ("p", "<strong>Volume I, Chapter 9, §3.</strong> &ldquo;Now the following "
                  "analysis (!) will show that in a mill so worked, the whole net profit is "
                  "derived from the last hour.&rdquo;"),
            ("p", "The exclamation mark is Marx's. Senior's figures: a manufacturer invests "
                  "£100,000, £80,000 in the mill and machinery and £20,000 in raw material and "
                  "wages. With gross profits of 15% the year's product is worth £115,000. Divide "
                  "that among the twenty-three half-hours of the day: twenty half-hours replace "
                  "the £100,000 of capital, one replaces the £5,000 of wear on the mill, and "
                  "the last two produce the net profit of 10%. Cut the day by one hour and the "
                  "net profit is destroyed; by an hour and a half and even the gross profit "
                  "goes. Lengthen it to thirteen hours and the net profit is more than "
                  "doubled."),
            ("p", "Marx's first answer is short. If the workers really spend most of the day "
                  "reproducing the cotton, the coal and the machinery, then a shorter day uses "
                  "less cotton, coal and machinery in proportion: &ldquo;You gain just as much "
                  "as you lose.&rdquo; Then he takes the analysis seriously, and asks Senior to "
                  "do what he did not: put the constant capital on one side of the account and "
                  "the wages on the other."),
            ("p", "Senior's figures put wages in one sum with the raw material, so they cannot "
                  "show this by themselves. Marx supposes that the separated account keeps the "
                  "manufacturers' story: the worker reproduces his wages in the product of the "
                  "last hour but one and the net profit in the product of the last. Wages and net "
                  "profit are then equal in value. But the worker adds value only by "
                  "working, and only in proportion to the hours, so of his 11½ hours, 5¾ "
                  "reproduce his wages and 5¾ produce the net profit. The rate of surplus value "
                  "is 100%."),
            ("p", "How, then, can the yarn of a single hour be worth 5¾ hours? Because 4¾ of "
                  "them were already in the cotton and the machinery it used up, and the spinner "
                  "added 1. &ldquo;The truth is that he performs no such miracle.&rdquo; The "
                  "spinner does not spend part of his day replacing the cotton. The cotton's "
                  "value goes over into the yarn because he spins it, which is the quality of "
                  "his labour from “Constant Capital and Variable Capital”, not its quantity."),
            ("p", "So Marx recomputes Senior's two predictions. Thirteen hours instead of 11½, "
                  "with the extra hour and a half all surplus: 7¼ hours of surplus on 5¾ "
                  "necessary, 126 2/23%, not &ldquo;more than doubled&rdquo;. One hour less: "
                  "4¾ on 5¾, which is 19/23, about 82.6%. This edition prints that figure as "
                  "&ldquo;82 14/32%&rdquo;, a misprint for 82 14/23%; the lab's 19/23 is the "
                  "correct value. And the last hour itself, about which the manufacturers had "
                  "&ldquo;invented more stories than have the millenarians about the day of "
                  "judgment&rdquo;, is &ldquo;all bosh&rdquo;."),
            ("p", "One more thing in the text deserves a careful reader. Marx introduces the "
                  "cut as &ldquo;a reduction of the hours of labour from 11½ to 10&rdquo;, which "
                  "is an hour and a half, and then computes 4¾ hours of surplus, which is the "
                  "one-hour cut Senior first named. The lab does both: an hour off gives 19/23, "
                  "an hour and a half gives 4¼ on 5¾, 17/23, about 73.9%. Senior said the "
                  "second would destroy even the gross profit."),
            ("p", "The cry outlived its author. Marx notes that in 1848 James Wilson, founder "
                  "of The Economist, raised it again against the Ten Hours' Bill. Marx ends his "
                  "reply to the manufacturers with advice: whenever &ldquo;your &lsquo;last hour&rsquo; strikes in earnest, think on the Oxford "
                  "Professor.&rdquo;"),
            ("p", "Senior's position has a stronger form than the one Marx demolishes, and it "
                  "is fair to state it. Much of a mill's capital loses value with time, through "
                  "interest and through machines going out of date, whether or not they run. "
                  "Spread over fewer hours, those costs weigh more on each pound of yarn, and a "
                  "shorter day can cut profit by more than the hours alone suggest. Marx's "
                  "reckoning assumes the wear is proportional to the hours worked, and he takes "
                  "up the other kind of depreciation himself in the machinery chapter. The "
                  "question of whether the arithmetic of the last hour is right is settled; "
                  "the question of how much a shorter day costs is not."),
            ("p", "The lab computes the rate on any day and again with one hour taken off. "
                  "Senior's day gives 100% and, an hour shorter, 19/23, with Senior's prediction "
                  "of zero beside it. Thirteen hours give 29/23. The ten-hour preset is the cut "
                  "of an hour and a half."),
            ("p", "The working day can be cut, then, and the surplus with it, in proportion. "
                  "The next lesson, “The Working Day: Its Limits and the Greed for Surplus "
                  "Labour”, asks what decides how long it is."),
        ],
        "lab": ("capkit", {
            "mode": "surplus",
            "view": "senior",
            "money_unit": "s",
            "preset": "senior",
            "presets": [
                {"id": "senior", "label": "Marx's reading of Senior: 11½ hours, 5¾ necessary",
                 "hours": "23/2", "necessary_hours": "23/4", "expect": {"suRate": "1 = 100%", "suLastHour": "19/23 = 82.61% (Senior: 0)"}},
                {"id": "thirteen", "label": "Senior's 13 hours, the extra 1½ all surplus",
                 "hours": 13, "necessary_hours": "23/4", "expect": {"suRate": "29/23 = 126.09%", "suLastHour": "25/23 = 108.7% (Senior: 0)"}},
                {"id": "ten", "label": "The ten-hour day: 1½ hours cut",
                 "hours": 10, "necessary_hours": "23/4", "expect": {"suRate": "17/23 = 73.91%", "suLastHour": "13/23 = 56.52% (Senior: 0)"}},
            ],
            "panel_title": "Senior's mill, separated into c and v",
            "panel_intro": (
                "The day and the necessary hours go in. The first tile is the rate of surplus "
                "value on that day; the second is the rate after one more hour is cut, beside "
                "Senior's prediction that it would be nothing."
            ),
        }),
        "steps_title": "Testing a claim about the last hour",
        "steps_intro": "Four steps that turn Senior's figures into Marx's.",
        "steps": [
            ("Separate c from v",
             "Take the constant capital out of the account. Its value goes into the product "
             "and takes none of the worker's hours."),
            ("Split the day by value",
             "Find the ratio of wages to surplus in the figures given. The day's hours divide "
             "in the same ratio, because value is added in proportion to time."),
            ("Change the day",
             "Shorten or lengthen the day by the hours stated, taking them from or adding them "
             "to the surplus part."),
            ("Recompute the rate",
             "Divide the new surplus hours by the unchanged necessary hours, and compare the "
             "result with the prediction."),
        ],
        "worked": {
            "title": "An hour off Senior's day",
            "intro": [
                "Senior's mill works 11½ hours. Take Marx's supposition that, once the constant "
                "capital is set aside, wages and net profit are equal. You want the rate of surplus value now, after an hour is cut, and on "
                "the 13-hour day he wanted.",
            ],
            "lines": [
                "necessary = surplus = 11½ / 2 = 5¾ h",
                "now:  5¾ / 5¾ = 1 = 100%",
                "an hour off:  4¾ / 5¾ = 19/23 = 82.61%",
                "13 hours:  7¼ / 5¾ = 29/23 = 126.09%",
            ],
            "after": [
                "Senior said the first cut would leave nothing and the longer day would more "
                "than double the profit. On Marx's reckoning the cut leaves more than four "
                "fifths of the rate, and the longer day raises it by about a quarter.",
            ],
        },
        "quiz_title": "Senior's arithmetic",
        "quiz": [
            {"q": "On an 11½-hour day with 5¾ hours necessary, what is the rate of surplus "
                  "value after the day is cut by one hour?",
             "a": ["0%", "19/23, about 82.61%", "100%", "23/19, about 121%"],
             "c": 1,
             "why": "The surplus falls from 5¾ to 4¾ hours and the necessary time is unchanged, "
                    "so the rate is `19/23`. Zero is Senior's prediction; 100% is the rate "
                    "before the cut; `23/19` divides the wrong way."},
            {"q": "On Marx's reading, with wages and net profit equal in value, how many of the "
                  "11½ hours reproduce the value of the wages?",
             "a": ["One hour, the last hour but one", "Half an hour",
                   "5¾ hours", "10½ hours"],
             "c": 2,
             "why": "Wages and net profit are equal in value, and labour adds value only in "
                    "proportion to time, so each takes half the day. The yarn of the last hour "
                    "but one is worth the wages, but most of its value was already in the "
                    "cotton and machinery."},
            {"q": "Why can the yarn spun in a single hour be worth 5¾ hours of labour?",
             "a": ["The spinner works faster in the last hours",
                   "The machinery adds 4¾ hours of new value",
                   "The yarn is sold above its value",
                   "Its cotton and machinery already contained 4¾ hours, and the spinner added 1"],
             "c": 3,
             "why": "The value of the means of production passes into the yarn because it is "
                    "spun; the spinner adds only the hour he works. Machinery transfers value "
                    "and adds none, and nothing in the argument depends on price or speed."},
            {"q": "Senior predicted that a 13-hour day would more than double the net profit. "
                  "On Marx's reckoning, what rate of surplus value does it give?",
             "a": ["200%", "29/23, about 126.09%", "150%", "100%"],
             "c": 1,
             "why": "The extra hour and a half is all surplus, so `7¼ / 5¾ = 29/23`. Doubling "
                    "would need 200%, which on 5¾ necessary hours is a day of 17¼ hours."},
        ],
        "mistakes": [
            ("Thinking the last hour produces the whole profit",
             "Senior's analysis says so, and it seems to follow from his 23 half-hours. The lab "
             "refutes it: cut an hour from his day and the rate of surplus value is 19/23, "
             "about 82.61%, not zero. The profit is made in every surplus hour, and a shorter "
             "day removes the hours it removes, no more."),
            ("Lumping constant and variable capital together",
             "Senior divided the whole value of the product among the hours, as if the "
             "worker's time had to replace the mill and the cotton. Once c is set aside, the "
             "hours divide only the value the worker adds, v + s."),
            ("Thinking the worker spends hours replacing the machinery",
             "The value of the cotton and the machine goes into the yarn by the act of "
             "spinning, a matter of the kind of labour, not of its duration. The worker spends "
             "no separate time on it."),
        ],
        "standard": (
            "Finish when you can recompute Senior's claim.",
            "Given the length of a working day and the ratio of wages to surplus value, "
            "compute the rate of surplus value, the rate after a stated cut or extension of "
            "the day, and compare it with the prediction that the profit vanishes."
        ),
        "note": (
            "The lab assumes, with Marx, that the wear on the means of production is in "
            "proportion to the hours they run. Costs that accrue with calendar time, interest "
            "and obsolescence, are left out, and they are the strongest part of the "
            "manufacturers' case. Senior's 11½ hours and his predictions are his own; the "
            "equality of wages and net profit is Marx's supposition about what the "
            "manufacturers' figures would show with wages separated, and the 100% rests on "
            "it. The Kerr text's &ldquo;82 14/32%&rdquo; is a "
            "misprint for 82 14/23%."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Kerr vol. 1, l. 2091 (capital is dead labour); l. 2103 (right against
    # right); l. 2077, 2081, 2083-2085, 2099-2101, 2114, 2122, 2128, 2166,
    # 2186-2188, 2203, 2262, 2268, 2305 (figures and phrases).
    {
        "slug": "the-working-day-and-surplus-labour",
        "title": "The Working Day: Its Limits and the Greed for Surplus Labour",
        "module": "Chapter 10 · The Working Day",
        "one_line": "The necessary part of the day is fixed by the value of labour-power; the rest is fixed by nothing in the exchange, and capital pushes it as far as it can.",
        "summary": (
            "Chapter 10 begins with a line cut in two: necessary labour, fixed, and surplus "
            "labour, which can grow. Compute the rate of surplus value for days of 7, 12, 15 "
            "and 18 hours with 6 hours necessary, find the length that doubles it, and read "
            "Marx's account of what capital did with the hours no law yet limited."
        ),
        "key": [
            "working day = necessary + surplus labour",
            "necessary: fixed by labour-power's value",
            "surplus: fixed by nothing in exchange",
            "s / v = (working day − necessary) / necessary",
            "6 h necessary: 12 h → 100%, 18 h → 200%",
        ],
        "key_label": "A line with one end loose",
        "concepts_intro": (
            "The first four sections of Chapter 10 ask what a working day is, and answer "
            "with a line, a speech and the reports of the factory inspectors."
        ),
        "concepts": [
            ("A variable quantity",
             "The working day is necessary labour plus surplus labour. The first part is "
             "given by the value of labour-power; the second is not given at all. The day is "
             "&ldquo;determinable, but is, per se, indeterminate&rdquo;."),
            ("Two limits",
             "The day cannot fall to the necessary time under capitalist production, and it "
             "cannot pass the physical and moral limits of the worker. Both limits are very "
             "elastic."),
            ("Right against right",
             "The buyer has a right to use what he bought; the seller has a right to sell it "
             "again tomorrow. The law of exchange supports both, and settles neither."),
        ],
        "read_title": "Capital's view of the day, and the worker's",
        "read_intro": (
            "The passage is Marx's image for capital's side of the question. The second "
            "passage, later in the body, states the deadlock it leads to."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 10, §1.</strong> &ldquo;Capital is dead labour, "
                  "that vampire-like, only lives by sucking living labour, and lives the more, "
                  "the more labour it sucks. The time during which the labourer works, is the "
                  "time during which the capitalist consumes the labour-power he has purchased "
                  "of him.&rdquo;"),
            ("p", "Most people's working day is set by a contract, a law and a habit, and so it "
                  "feels like a fixed quantity, like the length of an hour. Chapter 10 begins by "
                  "showing that it is not. Draw the necessary labour-time as a line A to B, 6 "
                  "hours long. Extend it to C by 1, 3 or 6 hours and you have three working "
                  "days, of 7, 9 and 12 hours. The surplus part B to C is 1/6, 3/6 and 6/6 of "
                  "the necessary part, so the rate of surplus value is 16 2/3, 50 and 100%."),
            ("p", "One end of the line is fixed by the value of labour-power. The other end is "
                  "fixed by nothing in the sale. So the day is &ldquo;determinable, but is, per "
                  "se, indeterminate&rdquo;. It has a minimum in principle, the necessary time "
                  "itself, which capitalist production never reaches, and a maximum set by the "
                  "body's need for sleep and food and by the worker's &ldquo;intellectual and "
                  "social wants&rdquo;. Both are elastic, &ldquo;So we find working days of 8, "
                  "10, 12, 14, 16, 18 hours&rdquo;."),
            ("p", "Read the passage now. Capital is &ldquo;dead labour&rdquo;: the past labour "
                  "embodied in the means of production, which can keep its value and grow only "
                  "by absorbing the labour of the living. The capitalist, as capital "
                  "personified, wants the day as long as possible because each hour of it is "
                  "an hour of the labour-power he has bought. Marx follows with a single line "
                  "that is the capitalist's whole view: &ldquo;If the labourer consumes his "
                  "disposable time for himself, he robs the capitalist.&rdquo;"),
            ("p", "Then the worker speaks, and Marx gives him the logic of the market. You "
                  "bought my labour-power for a day, and I must be able to sell it again "
                  "tomorrow. &ldquo;What you gain in labour I lose in substance.&rdquo; If an "
                  "average worker can work for 30 years, a day's pay is one 10,950th of the "
                  "whole; work him out in 10 years and you pay one 10,950th for what is now "
                  "one 3,650th, only a third of a day's value. &ldquo;I demand the normal "
                  "working day because I, like every other seller, demand the value of my "
                  "commodity.&rdquo;"),
            ("p", "<strong>Volume I, Chapter 10, §1.</strong> &ldquo;There is here, therefore, "
                  "an antinomy, right against right, both equally bearing the seal of the law "
                  "of exchanges. Between equal rights force decides.&rdquo;"),
            ("p", "Section 2 says that capital did not invent surplus labour. Wherever a part "
                  "of society monopolises the means of production, workers add surplus time "
                  "for its owners, Athenian, Roman, Norman baron or Wallachian boyar. The "
                  "difference is visibility. A Wallachian peasant under the corvée worked his "
                  "own field on some days and his lord's on others, so the division was there "
                  "to be seen; Marx shows how the code that the Russian general Kisseleff "
                  "proclaimed in 1831, dictated, he says, by the boyars themselves, turned a nominal "
                  "14 days of corvée into 56, a rate of 56/84, 66 2/3%. In a factory, necessary "
                  "and surplus labour &ldquo;glide one into the other&rdquo;, minute by "
                  "minute."),
            ("p", "So the English factory inspectors counted minutes. Under the Act of 1850 the "
                  "legal week was 60 hours. A mill that started a quarter of an hour early, "
                  "stopped a quarter late and nibbled ten minutes from breakfast and twenty from "
                  "dinner gained 5 hours 40 minutes a week, which over 50 weeks is 27 working "
                  "days a year. The inspectors called it &ldquo;petty pilfering of "
                  "minutes&rdquo;; the workers called it &ldquo;nibbling and cribbling at meal "
                  "times&rdquo;; a master told an inspector that ten minutes' overtime a day "
                  "put a thousand a year in his pocket. &ldquo;Moments are the elements of "
                  "profit.&rdquo;"),
            ("p", "Section 3 turns to trades with no legal limit, and the evidence is hard to "
                  "read. Children of nine or ten in Nottingham's lace trade at work from two, "
                  "three or four in the morning until ten, eleven or twelve at night; William Wood, who began running moulds "
                  "in the Staffordshire potteries at 7 years and 10 months, working from 6 a.m. "
                  "to 9 p.m.; London bakers who rarely reached 42; Mary Anne Walkley, a "
                  "milliner of 20, dead after 26½ hours of unbroken work on gowns for a ball. "
                  "Marx quotes a doctor's figure for the blacksmith: made to do a quarter more "
                  "work a day, &ldquo;he dies at 37 for 50&rdquo;."),
            ("p", "Section 4 is the relay system: two sets of workers, day and night, so that "
                  "the furnaces and rolling mills never stand idle. The ironmasters' evidence, "
                  "which Marx quotes at length, is frank that the objection to stopping boys' "
                  "night work is cost: furnaces and rolling mills that stand idle at night are "
                  "capital absorbing no labour, and so, in the employers' reckoning, a loss."),
            ("p", "The objection to the chapter is serious. Economists then and since have "
                  "argued that hours are chosen by workers who trade leisure for income, and "
                  "that the very long days of the 1860s reflected low productivity: people "
                  "too poor to buy leisure worked long, and as wages rose, hours fell. Marx "
                  "does not deny that workers agreed to long days. His claim is that the "
                  "agreement was compelled, by having nothing else to sell, and that the "
                  "exchange itself contains no rule for where the day should end."),
            ("p", "The lab holds the necessary time at Marx's 6 hours and moves the end of the "
                  "line. Seven hours give 1/6; twelve give 100%; fifteen, 150%; eighteen, 200%. "
                  "The rate doubles when the surplus part doubles, which a 12-hour day does at "
                  "18 hours, not at 24."),
            ("p", "Between equal rights, force decides. The next lesson, “The Struggle for a "
                  "Normal Working Day”, tells how it decided in England, and computes what a "
                  "legal limit does to the rate."),
        ],
        "lab": ("capkit", {
            "mode": "workday",
            "view": "absolute",
            "money_unit": "hours",
            "preset": "six-six",
            "presets": [
                {"id": "seven", "label": "Marx's working day I: 7 hours, 6 necessary",
                 "day": 7, "necessary": 6, "expect": {"wdSurplus": "1 h", "wdRate": "1/6 = 16.67%"}},
                {"id": "six-six", "label": "Marx's working day III: 12 hours, 6 necessary",
                 "day": 12, "necessary": 6, "expect": {"wdSurplus": "6 h", "wdRate": "1 = 100%"}},
                {"id": "fifteen", "label": "A 15-hour day, 6 necessary",
                 "day": 15, "necessary": 6, "expect": {"wdSurplus": "9 h", "wdRate": "3/2 = 150%"}},
                {"id": "eighteen", "label": "An 18-hour day, 6 necessary",
                 "day": 18, "necessary": 6, "expect": {"wdSurplus": "12 h", "wdRate": "2 = 200%"}},
            ],
            "panel_title": "The working day as a line",
            "panel_intro": (
                "The bar is the day, cut at the necessary labour-time. Lengthen the day and "
                "only the surplus part grows; the tiles give its hours and the rate of "
                "surplus value."
            ),
        }),
        "steps_title": "Reading a working day",
        "steps_intro": "Four steps for any day and any value of labour-power.",
        "steps": [
            ("Fix the necessary time",
             "Find the hours that reproduce the value of a day's labour-power. They do not "
             "change with the length of the day."),
            ("Subtract",
             "The surplus labour-time is the length of the day less the necessary time."),
            ("Divide",
             "The rate of surplus value is surplus time over necessary time."),
            ("Find the day for a target rate",
             "To reach a rate r, the surplus time must be r times the necessary time, so the "
             "day is the necessary time times one plus r."),
        ],
        "worked": {
            "title": "Twelve hours, then eighteen",
            "intro": [
                "Labour-power is worth 6 hours a day. You want the rate of surplus value on a "
                "12-hour day, and the length of day at which it doubles.",
            ],
            "lines": [
                "12 h:  surplus 12 − 6 = 6 h",
                "rate:  6 / 6 = 100%",
                "double the rate:  surplus 2 · 6 = 12 h",
                "day:  6 + 12 = 18 h  (rate 12 / 6 = 200%)",
            ],
            "after": [
                "The day grows by half and the rate doubles, because only the surplus part "
                "moves. Fifteen hours, a quarter longer than twelve, give 150%.",
            ],
        },
        "quiz_title": "The limits of the day",
        "quiz": [
            {"q": "With 6 hours necessary, what working day gives a rate of surplus value of "
                  "50%?",
             "a": ["12 hours", "9 hours", "3 hours", "7 hours"],
             "c": 1,
             "why": "The surplus must be half the necessary time, 3 hours, so the day is `6 + 3 "
                    "= 9`. Twelve hours gives 100% and 7 hours 1/6; 3 hours is the surplus "
                    "alone."},
            {"q": "A 12-hour day with 6 hours necessary gives 100%. How long must the day be "
                  "to double the rate, with the same necessary time?",
             "a": ["24 hours", "15 hours", "18 hours", "13 hours"],
             "c": 2,
             "why": "200% needs 12 surplus hours on 6 necessary, a day of 18. Doubling the whole "
                    "day to 24 would give 300%; 15 hours gives 150%."},
            {"q": "Why does Marx call the working day &ldquo;determinable, but &hellip; per se, "
                  "indeterminate&rdquo;?",
             "a": ["Its necessary part is fixed by the value of labour-power, but nothing in the "
                   "exchange fixes its surplus part",
                   "No law had ever limited it anywhere",
                   "It changes with the price of the product",
                   "Each worker chooses freely how long to work"],
             "c": 0,
             "why": "One end of the line is given by what labour-power costs; the other is "
                    "contested, within elastic physical and moral bounds. Laws had limited it, "
                    "as the next lesson shows; prices do not enter; and the chapter's point is "
                    "that the worker's choice is constrained."},
            {"q": "In the worker's speech, labour-power that should last 30 years is used up "
                  "in 10. What fraction of its true daily value is he paid?",
             "a": ["2/3", "1/10", "1/3", "3 times"],
             "c": 2,
             "why": "He is paid one 10,950th of the whole a day when each day now uses one "
                    "3,650th, so he receives `3,650/10,950 = 1/3` of the day's value and is "
                    "robbed, he says, of the other 2/3."},
        ],
        "mistakes": [
            ("Thinking the length of the day is fixed by nature or contract",
             "Hours feel given, by custom or by the contract. The chapter's first sum shows "
             "that only the necessary part is given. The lab holds it at 6 hours and moves "
             "the day: 7 hours give 1/6, 12 give 100%, 18 give 200%. Every hour added is an "
             "hour of surplus labour, which is why the length of the day is fought over."),
            ("Thinking the rate rises in proportion to the length of the day",
             "From 12 to 15 hours the day grows by a quarter and the rate by half, from 100% "
             "to 150%, because the extra hours all fall on the surplus side."),
            ("Taking the corvée for a different kind of exploitation",
             "Marx's comparison says the opposite: three days' surplus labour a week is the "
             "same quantity whether it is done on the lord's field or hidden in every minute "
             "of a factory day. What differs is that one can be seen."),
        ],
        "standard": (
            "Finish when you can compute the rate for any length of day.",
            "Given the length of a working day and the necessary labour-time, compute the "
            "surplus labour-time and the rate of surplus value, and compute the length of day "
            "that gives a stated rate."
        ),
        "note": (
            "The lab holds the value of labour-power fixed while the day lengthens. The "
            "chapter itself shows that it is not fixed in the long run: a day that wears the "
            "worker out faster raises the value of labour-power, as the worker's speech "
            "argues, and the lab does not compute that. The 7 and 12-hour days are Marx's; the "
            "15 and 18 are illustrative."
        ),
    },
    # ---------------------------------------------------------------- 09
    # Kerr vol. 1, l. 2337 (centuries of struggle); l. 2505 (a protracted
    # civil war); l. 2341-2357, 2377-2381, 2397-2399, 2411-2417, 2461,
    # 2465-2467, 2471-2473, 2509-2518 (history and phrases).
    {
        "slug": "the-struggle-for-a-normal-working-day",
        "title": "The Struggle for a Normal Working Day",
        "module": "Chapter 10 · The Working Day",
        "one_line": "English law first lengthened the day and then shortened it; cutting a 12-hour day to 10 at the same value of labour-power cuts the rate of surplus value by a third.",
        "summary": (
            "Sections 5 to 7 of Chapter 10 tell how the length of the day was settled in "
            "England, from the Statutes of Labourers to the Ten Hours' Act and the relay "
            "system that evaded it. Compute what a legal limit does to the rate of surplus "
            "value at a fixed value of labour-power, what the relay system did to the limit, "
            "and what the compromise of 1850 left."
        ),
        "key": [
            "1349–1700s: law lengthens the day",
            "1833–1850: Factory Acts shorten it",
            "12 h → 10 h, 6 necessary: 100% → 2/3",
            "relays: a limit no one can check",
            "1850: 10½ h, 6 a.m. to 6 p.m.: 75%",
        ],
        "key_label": "A limit, and its evasion",
        "concepts_intro": (
            "The end of Chapter 10 is history, and Marx tells it as a struggle with "
            "dates. The arithmetic is short; the dates matter."
        ),
        "concepts": [
            ("Two opposed tendencies",
             "From the 14th century to the 18th, English statutes tried to make labourers "
             "work longer. From 1833 the Factory Acts made the working day shorter. Both were "
             "the state fixing the day."),
            ("The ten-hour day",
             "The Act of 1847 limited young persons and women to 11 hours from July 1847 and "
             "to 10 from 1 May 1848. At a fixed value of labour-power, every hour cut is an "
             "hour of surplus labour."),
            ("The relay system",
             "With a legal factory day of 15 hours, employers could shuffle workers in and "
             "out so that no inspector could tell how long anyone had worked. A limit that "
             "cannot be checked does not bind."),
        ],
        "read_title": "Marx's two verdicts on the history",
        "read_intro": (
            "The first passage opens the history in section 5; the second draws its "
            "conclusion in section 7."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 10, §5.</strong> &ldquo;The establishment of a "
                  "normal working day is the result of centuries of struggle between capitalist "
                  "and labourer.&rdquo;"),
            ("p", "The struggle ran in two directions. The first Statute of Labourers, in 1349, "
                  "after the Black Death had made labour scarce, fixed wages and the length of "
                  "the day by law, and later statutes set the summer day from 5 in the morning "
                  "to 7 or 8 at night. What capital &ldquo;in embryo&rdquo; asked the state for "
                  "then was more hours, because it could not yet get them by economic pressure "
                  "alone. By 1770 a pamphleteer was proposing an &ldquo;ideal work-house&rdquo; "
                  "for paupers, a &ldquo;House of Terror&rdquo; with twelve hours of net "
                  "labour. A few years later, Marx says, it was built for the industrial worker "
                  "himself: &ldquo;It is called the Factory.&rdquo;"),
            ("p", "With machinery, in the last third of the 18th century, &ldquo;All bounds of "
                  "morals and nature, age and sex, day and night, were broken down.&rdquo; "
                  "Parliament passed five labour laws between 1802 and 1833 and voted no money "
                  "to enforce them. The Act of 1833 is where a normal working day for modern "
                  "industry begins: within a factory day from 5.30 in the morning to 8.30 at "
                  "night, young persons from 13 to 18 could work 12 hours and children from 9 "
                  "to 13 eight. Its own commissioners proposed working &ldquo;double sets of "
                  "children&rdquo; to keep adults' hours untouched, and the relay system was "
                  "born."),
            ("p", "The Act of 1844 brought women over 18 under the same 12-hour limit, the first "
                  "time the law controlled adult labour directly, and tried to close the relay "
                  "loophole: hours were to be counted from when a young person first started, "
                  "by a public clock. Then came 1846 and 1847, the repeal of the Corn Laws and "
                  "the height of the Chartist and ten-hours agitation, and the Ten Hours' Bill "
                  "passed: 11 hours from 1 July 1847, 10 from 1 May 1848. The manufacturers "
                  "answered with wage cuts of at least 25% and petitions in the workers' names; "
                  "when the inspector Leonard Horner asked the workers, about 70% were for ten "
                  "hours."),
            ("p", "After the revolutions of 1848 the employers revolted. The Act left the legal "
                  "factory day at 15 hours, and inside it they moved young persons and women "
                  "&ldquo;now for 30 minutes, now for an hour&rdquo; from room to room and mill "
                  "to mill until each had done ten hours, while the mill ran 13½ or 15. Horner "
                  "reported that no system of supervision could prevent overwork under it. In "
                  "Marx's summary, the masters &ldquo;paid 10 hours' wages for 12 or 15 hours' "
                  "lordship over labour-power.&rdquo; Local magistrates who were themselves "
                  "cotton-spinners acquitted their colleagues, and on 8 February 1850 the Court "
                  "of Exchequer found a form of words in the Act that rendered it meaningless."),
            ("p", "The workers' answer, in meetings across Lancashire and Yorkshire, led to the "
                  "compromise Act of 5 August 1850: young persons and women would work 10½ hours "
                  "on weekdays and 7½ on Saturday, all between 6 a.m. and 6 p.m., with common "
                  "meal times. That ended the relay system &ldquo;once for all&rdquo;, at the "
                  "price of half an hour a day. From 1860 the Factory Acts reached dye-works, "
                  "bleach-works, lace, potteries and match-making, and an Act of 1863 reached "
                  "the bakeries."),
            ("p", "<strong>Volume I, Chapter 10, §7.</strong> &ldquo;The creation of a normal "
                  "working day is, therefore, the product of a protracted civil war, more or "
                  "less dissembled, between the capitalist class and the working class.&rdquo;"),
            ("p", "The isolated worker, Marx argues, &ldquo;succumbs without any power of "
                  "resistance&rdquo;; only as a class could workers compel a law. France got a "
                  "12-hour law from the February revolution of 1848. In the United States, "
                  "after the Civil War, a labour congress at Baltimore in 1866 demanded eight "
                  "hours, and the International Working Men's Association at Geneva the same "
                  "year proposed eight hours as the legal limit. In place of &ldquo;the pompous "
                  "catalogue of the &lsquo;inalienable rights of man&rsquo;&rdquo; comes "
                  "&ldquo;the modest Magna Charta of a legally limited working-day&rdquo;, which "
                  "says when the time the worker sells ends and his own begins."),
            ("p", "Marx is careful about motives, and they belong in the story. Some "
                  "manufacturers who obeyed the 1833 Act petitioned against rivals who did not; "
                  "Tory landowners backed the Ten Hours' Bill partly in revenge for the repeal "
                  "of the Corn Laws. Historians have added more: rising productivity that let "
                  "employers concede hours, and a public alarmed by the inspectors' reports. "
                  "The chapter's claim is not that the workers acted alone, but that without "
                  "their pressure none of these motives would have produced a law that held."),
            ("p", "The lab applies a limit to a day with 6 hours necessary, the value of "
                  "labour-power held fixed. A 12-hour day cut to 10 takes the surplus from 6 "
                  "hours to 4 and the rate from 100% to 2/3. Under relays the only limit that "
                  "can be checked is the 15-hour factory day, so the 12-hour day comes back. "
                  "The 1850 compromise, 10½ hours, gives 3/4."),
            ("p", "Holding the value of labour-power fixed is a real simplification here. The "
                  "manufacturers cut wages when the hours fell, and a wage below the value of "
                  "labour-power changes the necessary time the lab treats as given. Marx's "
                  "point stands for the case he states: at the same value of labour-power, a "
                  "shorter day is a lower rate."),
            ("p", "So the day can be lengthened only so far, and the law can shorten it. The "
                  "next lesson, “Rate and Mass of Surplus Value”, asks what that means for the "
                  "total a capitalist can extract, when the number of workers can change too."),
        ],
        "lab": ("capkit", {
            "mode": "workday",
            "view": "limit",
            "money_unit": "hours",
            "preset": "before",
            "presets": [
                {"id": "before", "label": "The 12-hour limit of 1844, 6 hours necessary",
                 "day": 12, "necessary": 6, "limit": 12, "expect": {"wdSurplus": "6 h", "wdRate": "1 = 100%"}},
                {"id": "ten-hours", "label": "The Act of 1847: ten hours from May 1848",
                 "day": 12, "necessary": 6, "limit": 10, "expect": {"wdSurplus": "4 h", "wdRate": "2/3 = 66.67%"}},
                {"id": "relay-dodge", "label": "Relays: only the 15-hour factory day can be checked",
                 "day": 12, "necessary": 6, "limit": 15, "expect": {"wdSurplus": "6 h", "wdRate": "1 = 100%"}},
                {"id": "act-1850", "label": "The compromise of 1850: 10½ hours",
                 "day": 12, "necessary": 6, "limit": "21/2", "expect": {"wdSurplus": "9/2 h", "wdRate": "3/4 = 75%"}},
            ],
            "panel_title": "A legal limit on a 12-hour day",
            "panel_intro": (
                "The employer wants a 12-hour day; the law allows the limit; the day worked is "
                "the shorter of the two. Necessary labour stays at 6 hours throughout, which "
                "is the assumption that the value of labour-power does not change."
            ),
        }),
        "steps_title": "Computing the effect of a legal limit",
        "steps_intro": "Four steps for any limit on hours.",
        "steps": [
            ("Find the day worked",
             "The day worked is the shorter of the day the employer wants and the limit that "
             "can actually be enforced."),
            ("Hold the necessary time",
             "At an unchanged value of labour-power, the necessary labour-time does not move."),
            ("Recompute the surplus",
             "Surplus labour-time is the day worked less the necessary time. Every hour the "
             "limit removes comes off it."),
            ("Recompute the rate",
             "Divide the new surplus time by the necessary time and compare with the rate "
             "before the limit."),
        ],
        "worked": {
            "title": "Ten hours, and then ten and a half",
            "intro": [
                "A mill works 12 hours with 6 hours necessary. The Ten Hours' Act cuts the day "
                "to 10; the compromise of 1850 sets it at 10½. You want the rate in each case.",
            ],
            "lines": [
                "12 h:  (12 − 6) / 6 = 1 = 100%",
                "10 h:  (10 − 6) / 6 = 2/3 = 66.67%",
                "10½ h:  (10½ − 6) / 6 = 3/4 = 75%",
            ],
            "after": [
                "Cutting two hours of twelve takes a third off the rate, because both hours "
                "were surplus labour. The half-hour conceded in 1850 was surplus labour too, "
                "and it raised the rate from 2/3 to 3/4.",
            ],
        },
        "quiz_title": "What the law did to the day",
        "quiz": [
            {"q": "A 12-hour day with 6 hours necessary is cut by law to 10 hours, the value of "
                  "labour-power unchanged. What is the new rate of surplus value?",
             "a": ["100%", "5/6, about 83.33%", "2/3, about 66.67%", "2/5, 40%"],
             "c": 2,
             "why": "The surplus falls from 6 hours to 4 on the same 6 necessary, so the rate is "
                    "`4/6 = 2/3`. 5/6 is the ratio of the two days; 40% is surplus over the "
                    "whole day; 100% is the rate before the cut."},
            {"q": "How did the relay system of 1848 to 1850 defeat the ten-hour limit?",
             "a": ["By paying the workers by the piece instead of by time",
                   "By moving workers in and out within a 15-hour factory day, so that no "
                   "inspector could tell how long anyone had worked",
                   "By lengthening the working week to seven days",
                   "By raising wages so that the workers would waive the limit"],
             "c": 1,
             "why": "The Act limited each young person and woman to ten hours but left a "
                    "15-hour legal day, and shuffling the shifts inside it made the limit "
                    "impossible to check. Wages were cut, not raised, and Sunday work and piece "
                    "rates are not the mechanism Marx describes."},
            {"q": "What did the Act of 1850 settle?",
             "a": ["An eight-hour day for all workers",
                   "A 12-hour day for children under 13",
                   "The abolition of night work for adult men",
                   "A 10½-hour weekday for young persons and women, between 6 a.m. and 6 p.m., "
                   "with common meal times"],
             "c": 3,
             "why": "The compromise raised the weekday from 10 to 10½ hours and in return "
                    "fixed it within 6 a.m. to 6 p.m., which ended the relays. Eight hours was "
                    "the American and International demand of 1866, and the Act did not touch "
                    "adult men's night work."},
            {"q": "Which two tendencies does Marx contrast in the history of English labour "
                  "law?",
             "a": ["Statutes from the 14th century on that lengthened the day by compulsion, "
                   "and Factory Acts that shortened it",
                   "Laws that raised wages, and laws that lowered them",
                   "Laws for agriculture, and laws for manufacture",
                   "Laws made by Parliament, and laws made by the courts"],
             "c": 0,
             "why": "Capital in embryo needed the state to get it more hours; grown, it had "
                    "hours taken from it by the state. The early statutes did fix wages too, "
                    "but the contrast Marx draws is over the length of the day."},
        ],
        "mistakes": [
            ("Thinking a legal limit leaves the rate of surplus value where it was",
             "If the limit only shortened the day, the proportion might seem to stay the same. "
             "It does not, because the hours removed are all surplus hours. At 6 hours "
             "necessary the ten-hours preset takes a 12-hour day from 100% to 2/3: two hours "
             "fewer, a third less surplus labour."),
            ("Dating the ten-hour day to 1847",
             "The Act passed in June 1847, but the day fell to 11 hours that July and to 10 "
             "only on 1 May 1848. Within two years the relay system and the Court of Exchequer "
             "had emptied it, and the Act of 1850 replaced it with 10½ hours."),
            ("Taking the limit on paper for the limit in the mill",
             "A limit binds only if it can be checked. Under relays the enforceable limit was "
             "the 15-hour factory day, and the relay preset shows the 12-hour day and its 100% "
             "coming back with the Act still in force."),
        ],
        "standard": (
            "Finish when you can compute what a legal limit does to the rate.",
            "Given a working day, the necessary labour-time and a legal limit, compute the "
            "day worked, the surplus labour-time and the rate of surplus value before and "
            "after the limit, at an unchanged value of labour-power."
        ),
        "note": (
            "The lab holds the value of labour-power fixed, and the history did not: wages "
            "were cut by a quarter as the hours fell. The relay preset models evasion as a "
            "limit that falls back to the 15-hour factory day, which is the lab's simplification "
            "of Horner's reports. The dates and hours are Marx's; the 12-hour day with 6 "
            "necessary is his running example, not a figure for any mill."
        ),
    },
    # ---------------------------------------------------------------- 10
    # Kerr vol. 1, l. 2534 (the mass of surplus-value); l. 2546 (the absolute
    # limit of the average working day); l. 2528-2532, 2540-2544, 2550-2552,
    # 2556, 2560-2562, 2576 (figures and phrases).
    {
        "slug": "rate-and-mass-of-surplus-value",
        "title": "Rate and Mass of Surplus Value",
        "module": "Chapter 11 · Rate and Mass of Surplus-Value",
        "one_line": "The mass of surplus value is the variable capital times the rate; fewer workers can be made to yield as much, but only up to the limit of the day.",
        "summary": (
            "Chapter 11 states three laws about the total surplus value a capital produces. "
            "Compute the mass from the value of a labour-power, the number of workers and the "
            "rate, check Marx's case in which half the workers at twice the rate give the "
            "same 150s, and find where that compensation stops: at a day that can never reach "
            "24 hours."
        ),
        "key": [
            "mass = variable capital × rate of s",
            "variable capital = workers × wage",
            "half the workers at twice the rate: same",
            "compensation stops short of a 24-hour day",
            "mass varies with v, whatever c is",
        ],
        "key_label": "Three laws of the mass",
        "concepts_intro": (
            "Until now the lessons have followed one worker. Chapter 11 multiplies, and "
            "finds that the product has a ceiling."
        ),
        "concepts": [
            ("The mass of surplus value",
             "The total surplus value a capital produces in a period: the surplus from one "
             "worker times the number of workers, or the variable capital times the rate of "
             "surplus value."),
            ("Compensation",
             "A fall in one factor can be made up by a rise in the other. Fewer workers at a "
             "higher rate, or a lower rate on more workers, can give the same mass."),
            ("The limit",
             "The rate can be raised by lengthening the day only until the day reaches its "
             "limit, always less than 24 hours. Past that, fewer workers cannot be made to "
             "give as much."),
        ],
        "read_title": "The first law, then its limit",
        "read_intro": (
            "The first passage states the law; the second, a few paragraphs on, states "
            "the limit Marx calls absolute."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 11.</strong> &ldquo;the mass of the surplus-value "
                  "produced is equal to the amount of the variable capital advanced, multiplied "
                  "by the rate of surplus-value; in other words: it is determined by the "
                  "compound ratio between the number of labour-powers exploited simultaneously "
                  "by the same capitalist and the degree of exploitation of each individual "
                  "labour-power.&rdquo;"),
            ("p", "Begin with one worker on the chapter's assumptions. Necessary labour is 6 "
                  "hours, embodied in 3s, so a day's labour-power is worth 3s and that is the "
                  "variable capital advanced for one worker. At a rate of 100% he yields 3s of "
                  "surplus value, 6 hours of surplus labour. A capitalist who employs 100 such "
                  "workers advances 300s and gets 300s. That is the whole of the first law: the "
                  "mass is the variable capital times the rate, or the number of workers times "
                  "the value of one labour-power times the rate."),
            ("math", "mass of surplus value = variable capital × s/v"),
            ("math", "variable capital = workers × value of one labour-power"),
            ("p", "Read the passage's last clause again: a &ldquo;compound ratio&rdquo; of "
                  "two factors, how many workers and how hard each is exploited. Because it is "
                  "a product, either factor can make up for the other. Marx's example: 100 "
                  "workers at a rate of 50%, a day stretched from 6 hours to 9, advance 300s and "
                  "yield 150s. Halve the variable capital to 150s, 50 workers, and double the "
                  "rate by stretching the day to 12 hours: still 150s. &ldquo;Within certain "
                  "limits therefore the supply of labour exploitable by capital is independent "
                  "of the supply of labourers.&rdquo;"),
            ("p", "Within certain limits. Here is the second law:"),
            ("p", "<strong>Volume I, Chapter 11.</strong> &ldquo;The absolute limit of the "
                  "average working-day&mdash;this being by Nature always less than 24 "
                  "hours&mdash;sets an absolute limit to the compensation of a reduction of "
                  "variable capital by a higher rate of surplus-value, or of the decrease of the "
                  "number of labourers exploited by a higher degree of exploitation of "
                  "labour-power.&rdquo;"),
            ("p", "Marx's figures: 500 workers at 100% on a 12-hour day give 1,500s a day, 3,000 "
                  "hours of surplus labour. A capital of 300s employing 100 workers at 200%, an "
                  "18-hour day, gives only 600s, and however long the day, 100 workers can never "
                  "produce a total value of 1,200s, which is 24 hours each. So a capital that "
                  "cuts its workforce cannot always win the surplus back by lengthening the day. "
                  "Marx says this &ldquo;palpable law&rdquo; will explain a great deal later, "
                  "when capital tends to reduce the number of workers it employs while still "
                  "wanting the greatest mass of surplus value."),
            ("p", "The third law follows from the first. With the rate and the value of "
                  "labour-power given, the masses of surplus value produced by different "
                  "capitals vary as their variable capitals, whatever their constant capital. A "
                  "spinner who employs much machinery and few hands should make less surplus "
                  "value per pound of capital than a baker who employs many hands and little "
                  "equipment. Marx says at once that &ldquo;This law clearly contradicts all "
                  "experience based on appearance&rdquo;: in fact capitals of the same size earn "
                  "about the same profit wherever they are invested. He compares the missing "
                  "steps to the algebra needed to see that 0/0 can stand for a real quantity, "
                  "and says only that many intermediate terms are still wanting. They are "
                  "supplied in Volume III."),
            ("p", "That deferral is where the sharpest criticism of Capital lands. Eugen von "
                  "Böhm-Bawerk argued in 1896 that Volume III's solution, prices of production "
                  "that depart systematically from values, contradicts Volume I's theory "
                  "instead of completing it. Marx's defenders reply that Volume I was always an "
                  "account at the level of the whole capital, where the totals still agree. "
                  "This course reads Volume I on its own terms, and the course Average Profit "
                  "and Its Fall takes up the dispute when the book does."),
            ("p", "Two consequences close the chapter. Treat a society's labour as one working "
                  "day, a million workers at 10 hours each being ten million hours: with the day "
                  "fixed, the mass of surplus value can grow only with the working population. "
                  "And a sum of money becomes capital only above a minimum. If a worker needs 8 "
                  "hours for himself and works 4 more, his employer needs two workers merely to "
                  "live as one worker does, and eight times that minimum to live twice as well "
                  "and still accumulate. Marx calls on Hegel's law that &ldquo;merely "
                  "quantitative differences beyond a certain point pass into qualitative "
                  "changes&rdquo;."),
            ("p", "His last example is a Paisley thread manufacturer who wrote to a Glasgow "
                  "paper in 1849 that a ten-hour law would make &ldquo;every 12 machines or "
                  "spindles in his establishment shrink to 10&rdquo;, so that a sixth would be "
                  "deducted from the value of every factory. To him the spindles' power to absorb "
                  "two extra hours of other people's labour was part of what they were worth: "
                  "dead labour that employs the living, rather than the other way round."),
            ("p", "The lab multiplies. Marx's 100 workers at 50% and his 50 workers at 100% "
                  "both give 150s. A hundred workers at 100% give 300s; to get 300s from 50, the "
                  "rate must be 200%, an 18-hour day, and the next step up would need a day "
                  "longer than 24 hours, which the lab refuses."),
            ("p", "That is where this course ends. Absolute surplus value has a ceiling, the "
                  "length of the day, and the factory acts were lowering it. The next course, "
                  "Relative Surplus Value, opens with the other way to enlarge the surplus: "
                  "leave the day alone and shorten the necessary part of it."),
        ],
        "lab": ("capkit", {
            "mode": "surplus",
            "view": "mass",
            "money_unit": "s",
            "preset": "marx-hundred",
            "presets": [
                {"id": "marx-hundred", "label": "Marx's 100 workers at 3s, a 9-hour day (50%)",
                 "wage": 3, "workers": 100, "hours": 9, "necessary_hours": 6, "expect": {"suMass": "150s", "suRate": "1/2 = 50%"}},
                {"id": "marx-fifty", "label": "Marx's 50 workers at 3s, a 12-hour day (100%)",
                 "wage": 3, "workers": 50, "hours": 12, "necessary_hours": 6, "expect": {"suMass": "150s", "suRate": "1 = 100%"}},
                {"id": "hundred", "label": "100 workers at 3s, a 12-hour day",
                 "wage": 3, "workers": 100, "hours": 12, "necessary_hours": 6, "expect": {"suMass": "300s", "suRate": "1 = 100%"}},
                {"id": "limit", "label": "50 workers made to give 300s: an 18-hour day",
                 "wage": 3, "workers": 50, "hours": 18, "necessary_hours": 6, "expect": {"suMass": "300s", "suRate": "2 = 200%"}},
            ],
            "panel_title": "The mass of surplus value",
            "panel_intro": (
                "Type the value of one labour-power, the number of workers and the day. The "
                "lab computes the rate from the day and multiplies. Try 50 workers and keep "
                "lengthening the day: past 24 hours the lab refuses."
            ),
        }),
        "steps_title": "Computing the mass of surplus value",
        "steps_intro": "Four steps, and a check against the limit.",
        "steps": [
            ("Compute the variable capital",
             "Multiply the value of one day's labour-power by the number of workers employed "
             "at once."),
            ("Compute the rate",
             "From the length of the day and the necessary time, the rate is surplus time over "
             "necessary time."),
            ("Multiply",
             "The mass of surplus value is the variable capital times the rate."),
            ("Check the limit",
             "To get a mass from fewer workers, find the rate needed and the day that gives "
             "it. A day of 24 hours or more is impossible, and the compensation fails."),
        ],
        "worked": {
            "title": "Fewer workers, a longer day",
            "intro": [
                "Labour-power is worth 3s a day, 6 hours. A capitalist with 100 workers on a "
                "12-hour day wants to keep his surplus while employing only 50. You want the "
                "mass now, and the day the 50 must work.",
            ],
            "lines": [
                "now:  100 · 3s = 300s;  rate 6/6 = 100%",
                "mass:  300s · 1 = 300s",
                "50 workers:  50 · 3s = 150s",
                "rate needed:  300 / 150 = 2 = 200%",
                "day:  6 + 2 · 6 = 18 h",
            ],
            "after": [
                "Eighteen hours is possible, barely. Halve the workforce again, to 25, and the "
                "rate needed is 400%, a day of 30 hours, which no compensation can reach.",
            ],
        },
        "quiz_title": "Rate, number and mass",
        "quiz": [
            {"q": "A capitalist employs 40 workers whose labour-power is worth 3s a day, at a "
                  "rate of surplus value of 100%. What is the daily mass of surplus value?",
             "a": ["40s", "3s", "120s", "240s"],
             "c": 2,
             "why": "The variable capital is `40 · 3s = 120s`, and at 100% the mass equals it. "
                    "3s is one worker's surplus, 40s counts workers as shillings, and 240s adds "
                    "the variable capital to the surplus."},
            {"q": "Marx's 100 workers at a rate of 50% give 150s a day. At the same value of "
                  "labour-power, what rate must 50 workers be worked at to give the same "
                  "150s?",
             "a": ["25%", "50%", "200%", "100%"],
             "c": 3,
             "why": "Half the variable capital needs twice the rate, 100%: `50 · 3s · 1 = "
                    "150s`. 25% halves the rate instead of doubling it; 200% would give 300s."},
            {"q": "Labour-power is worth 6 hours a day. Why can 100 workers never give as much "
                  "surplus labour as 500 workers at 100% on a 12-hour day?",
             "a": ["The law forbids more than 12 hours",
                   "No day reaches 24 hours, so 100 workers give less than 100 · 18 = 1,800 "
                   "surplus hours, against 3,000",
                   "Their wages would rise if the day were longer",
                   "The constant capital cannot be increased"],
             "c": 1,
             "why": "500 workers at 6 surplus hours each give 3,000 hours; 100 workers would "
                    "need 30 surplus hours each, a 36-hour day. The chapter's limit is natural, "
                    "not legal, and it holds whatever happens to wages or machinery."},
            {"q": "On the chapter's third law, which change raises the mass of surplus value "
                  "when the rate and the value of labour-power are held fixed?",
             "a": ["Adding more machinery for each worker",
                   "Raising the price of the raw material",
                   "Employing more workers",
                   "Selling the product more quickly"],
             "c": 2,
             "why": "With the rate and the value of labour-power fixed, the mass varies only "
                    "with the variable capital, that is with the number of workers. Machinery "
                    "and materials are constant capital, and the speed of sale is a question of "
                    "Volume II."},
        ],
        "mistakes": [
            ("Thinking more workers always means more surplus value",
             "More workers at the same rate do give more. But the mass is a product of two "
             "factors, and the two Marx presets show 100 workers at 50% and 50 workers at 100% "
             "giving the same 150s. A capital that employs fewer workers more intensely can "
             "match one that employs more, until the day runs out."),
            ("Thinking the compensation has no limit",
             "Every halving of the workforce needs a doubling of the rate. From 100 workers at "
             "100% to 50 needs 200% and 18 hours; to 25 needs 400% and 30 hours, which is "
             "impossible. The limit is the length of a day."),
            ("Thinking the mass depends on the constant capital",
             "On the chapter's law it does not: machinery and materials transfer value and "
             "make none. That a capital heavy in machinery seems to earn as much as one heavy "
             "in wages is the contradiction Marx names here and resolves only in Volume III."),
        ],
        "standard": (
            "Finish when you can compute the mass of surplus value and its limit.",
            "Given the value of a day's labour-power, the number of workers and the length of "
            "the day, compute the variable capital, the rate and the mass of surplus value, "
            "and compute the day a smaller workforce needs to yield the same mass."
        ),
        "note": (
            "The lab assumes every worker is an average worker and the value of labour-power "
            "stays put as the day lengthens. Marx makes both assumptions, and notes exceptional "
            "cases where the mass does not grow in proportion to the number of workers, which "
            "are cases where the value of labour-power has changed. The third law's "
            "conflict with observed profits is left for Volume III. The 100 and 50 workers at "
            "3s are Marx's; the 18-hour case is his 200% applied to the same 50 workers."
        ),
    },
]
