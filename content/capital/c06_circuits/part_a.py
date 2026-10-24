"""The Circuits of Capital, lessons 1-6 -- Volume II, Part I, Chapters 1-6, one lesson per chapter.

Every quotation is copied from /mnt/project-files/capital-texts/volume-2-kerr.txt
(Untermann's translation of Volume II, Kerr edition); the comment beside each
lesson gives its line numbers. Footnote numerals in the text are left out of
the quotations, and the translator's double quotation marks inside a quotation
are printed as single curly quotes. Marx's formulas inside a quotation are
printed as the Kerr text prints them, with its hyphens or dashes, its three
dots and its apostrophe for the prime (M-C...P...C'-M'); the lessons' own
prose writes them M–C…P…C′–M′. Nothing else is changed.

Untermann translates Marx's Kreislauf as "circulation" in the titles of
Chapters 1 and 3 and as "rotation" in Chapter 2. The module names keep his
chapter titles, as PLAN §E.3 requires; the lesson titles and prose say
"circuit", and the first lesson says why once.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 2, l. 353 (the formula); l. 615 (the most one-sided form).
    # Inline: l. 414 (the class relation in M-L), l. 482 (change of form,
    # not of magnitude), l. 492 (7,440 and 8,440 lb), l. 597 (the feverish
    # attempt), l. 483-484 and l. 533 (M' as a sum of money).
    {
        "slug": "the-circuit-of-money-capital",
        "title": "The Circuit of Money Capital",
        "module": "Chapter 1 · The Circulation of Money-Capital",
        "one_line": "Money buys means of production and labour-power, production makes a product worth more, and the sale turns it back into more money; the increase is made in the middle, not at the end.",
        "summary": (
            "Volume II opens by following one capital round its whole path: money buys means "
            "of production and labour-power, production turns them into a commodity of greater "
            "value, and the sale turns that commodity back into money. Trace Marx's spinner "
            "through the three stages, give the capital's value in each form, compute the "
            "surplus value from M and M′, and then sell less than the whole product to see what "
            "the money at the end does and does not show."
        ),
        "key": [
            "M–C…P…C′–M′: buy, produce, sell",
            "M = Pm + L: £422 = £372 + £50",
            "C′ = C + c: £500 = £422 + £78",
            "s = M′ − M, once all of C′ is sold",
            "a sale changes form, not magnitude",
        ],
        "key_label": "The first circuit in five lines",
        "concepts_intro": (
            "Volume I went inside the factory and assumed the buying and selling around it. "
            "Chapter 1 puts the buying and selling back and follows the capital through all of it."
        ),
        "concepts": [
            ("Three stages, three forms",
             "In the first stage the capital is money and buys; in the second it is means of "
             "production and labour-power at work; in the third it is a product to be sold. "
             "Marx calls the three forms money capital, productive capital and commodity "
             "capital."),
            ("Industrial capital",
             "The capital that passes through all three forms and drops each in turn is "
             "industrial capital, and &ldquo;industrial&rdquo; covers every branch run on a "
             "capitalist basis. The three forms are its functions, not three kinds of "
             "capital."),
            ("Produced and realised",
             "Surplus value is produced in the second stage and exists in the product before "
             "anything is sold. The sale realises it: turns it, with the capital-value, into "
             "money. The two are different events, and the lab separates them."),
        ],
        "read_title": "The formula first, then the three stages in order",
        "read_intro": (
            "The chapter states its formula on its first page. Its verdict on that formula comes "
            "near the end, after Marx has walked the spinner's £422 through every stage."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 1.</strong> &ldquo;Hence the formula for the "
                  "circulation process of money capital is: M-C...P...C'-M', the dots indicating "
                  "the points where the process of circulation was interrupted, and C' and M' "
                  "designating C and M increased by surplus value.&rdquo;"),
            ("p", "Volume I followed capital into the factory and assumed everything around it: "
                  "that the capitalist could find labour-power and cotton for sale, and that the "
                  "yarn would sell. Volume II takes those assumptions one at a time. It begins "
                  "with the shape of the whole movement, `M–C…P…C′–M′`, read as money, "
                  "commodities, production, more commodities, more money. A word on the "
                  "translation first: Untermann calls this the &ldquo;circulation&rdquo; of money "
                  "capital, and in the next chapter the &ldquo;rotation&rdquo; of productive "
                  "capital. Both render one German word, <em>Kreislauf</em>, which later "
                  "translations give as <em>circuit</em>, and these lessons use that word."),
            ("p", "The first stage is `M–C`, a purchase, and Marx's figures are the ones the "
                  "chapter keeps throughout: £422, of which £372 buys means of production and £50 "
                  "buys labour-power. Marx writes the two purchases `M–Pm` and `M–L`, Pm for the "
                  "means of production and L for labour-power, and the lessons keep his letters. "
                  "The split is not arbitrary. The cotton, coal and wear of the "
                  "spindles must be enough to soak up the whole of the labour bought, surplus "
                  "labour included; too little and some of the labour cannot be used, too much "
                  "and some of the cotton sits unspun. And the purchase of labour-power is "
                  "different in kind from the purchase of cotton. &ldquo;The class relation "
                  "between the capitalist and the wage laborer is therefore established from the "
                  "moment that they meet in the act M-L&rdquo;, because money can buy labour-power "
                  "only where the people who own it have nothing else to sell."),
            ("p", "Marx has a story about that. After the emancipation of the serfs in 1861, "
                  "Russian landowners who now had to hire their labour complained of two things. "
                  "They were short of ready money to pay wages before the harvest was sold. And "
                  "even with money, they could not find enough labourers, because a peasant who "
                  "still held a share of the village land was not yet a &ldquo;free&rdquo; "
                  "wage-worker. The second complaint is the more telling one: `M–C` presupposes "
                  "a class with nothing to sell but its labour-power."),
            ("p", "The second stage is `…P…`, production, and the dots mean that circulation has "
                  "stopped. The spinners transfer the £372 of means of production into the yarn "
                  "and add £128 of new value, so 10,000 lb of yarn are worth £500. Of the £128, "
                  "£50 replaces the wages and £78 is surplus value, &ldquo;representing an "
                  "exploitation of 156 per cent&rdquo;, which you can check: `78/50 = 156/100`. "
                  "All of the increase happens here. Nothing has been sold yet."),
            ("p", "The third stage is `C′–M′`, a sale. Marx asks what makes this ordinary sale "
                  "a function of capital, and answers that nothing happens inside it: the yarn's "
                  "value &ldquo;has not experienced any change of magnitude, but only of "
                  "form&rdquo;. What makes the yarn commodity capital is where it came from. "
                  "It is worth £500 against £422 laid out, and the £78 sits in it already, as "
                  "1,560 lb of the 10,000."),
            ("p", "Marx then does the arithmetic of a partial sale. Sell 7,440 lb at their value "
                  "and the capitalist has £372 back, only his constant capital. &ldquo;If he "
                  "sells 8,440 pounds of yarn, he recovers only the value of his total "
                  "capital.&rdquo; Only the whole 10,000 lb bring the £78 home. The lab runs "
                  "these sales: the money returned is the product's value times the share sold, "
                  "and `M′ − M` is zero at 8,440 lb and negative below it. The marx preset sells "
                  "everything, £500 back and £78 realised; the partly preset sells 8,440 lb, £422 "
                  "back and £0 realised; the constant preset sells 7,440 lb, £372 back and −£50; "
                  "and the unsold preset sells nothing, £0 back and −£422. A negative figure here "
                  "is not a loss of value. It is capital-value still sitting in the warehouse as "
                  "yarn."),
            ("p", "Once the sale is made, the result looks different from how it was made. In "
                  "the yarn, the capital and the surplus were distinct parts of a product that "
                  "came out of production. In £500 of money they are just £422 and £78 side by "
                  "side, and nothing in the coins says which is which. Marx's smaller example: of "
                  "£110, any £10 is `1/11` of the sum and also `1/10` of the £100 advanced, and "
                  "the money carries no mark of either. That is why he calls commodity capital "
                  "&ldquo;more rational and less difficult to understand than money-capital, in "
                  "which every trace of this process has disappeared&rdquo;."),
            ("p", "<strong>Volume II, Chapter 1.</strong> &ldquo;The circulation of "
                  "money-capital is therefore the most one-sided, and thus the most convincing "
                  "and typical form of the circulation of industrial capital. Its aim and "
                  "compelling motive, the utilization of value, the making and accumulation of "
                  "money, is thus most clearly revealed. Buying in order to sell dearer is its "
                  "slogan.&rdquo;"),
            ("p", "One-sided, because it starts and ends in money and so shows only the end in "
                  "view, more money, with production as the passage in between. Typical, for the "
                  "same reason: it is how the capitalist sees his own business. Marx's dry aside "
                  "is that this is how whole economies sometimes see it too: &ldquo;All nations "
                  "with a capitalist mode of production are seized periodically by a feverish "
                  "attempt to make money without the mediation of the process of "
                  "production.&rdquo;"),
            ("p", "The formula invites a reading Marx wants to block. The earliest mercantilist "
                  "writers, of the seventeenth century, measured a nation's gain by the gold its "
                  "trade brought in, and Marx says their &ldquo;so-called monetary system&rdquo; "
                  "read `M–C–M′` as &ldquo;a movement which takes place exclusively in the "
                  "circulation&rdquo;, so that it &ldquo;cannot explain the two phases M-C and C-M' "
                  "in any other way than by declaring that C is sold above its value&rdquo;. It is "
                  "a fair reading of `M…M′` alone that the gain is made in selling, by selling "
                  "dear; the later mercantilists, he adds, at least put production inside the "
                  "formula. The chapter's answer is the yarn: it "
                  "was worth £500 before it left the mill, and a sale at value turns £500 of yarn "
                  "into £500 of money. Whether value comes from labour at all is a separate "
                  "dispute, set out in Commodities and Money; here the claim is narrower, that on "
                  "Marx's definitions the sale adds nothing."),
            ("p", "One industry fits the formula differently, and it matters later. Transport "
                  "sells a change of place, which is used up as it is produced, so its circuit is "
                  "`M–C…P–M′`, with no product waiting to be sold. The next lesson, “The Circuit "
                  "of Productive Capital”, starts the same movement from production instead of "
                  "money and asks what that makes visible."),
        ],
        "lab": ("capkit", {
            "mode": "circuit",
            "view": "stages",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's spinner: £422 = £372 + £50, all 10,000 lb of yarn sold at £500",
                 "M": 422, "mp": 372, "lp": 50, "product": 500, "sold_share": 1, "expect": {"ciMprime": "£500", "ciS": "£78"}},
                {"id": "partly", "label": "Marx's figures: 8,440 lb of the 10,000 sold",
                 "M": 422, "mp": 372, "lp": 50, "product": 500, "sold_share": "211/250", "expect": {"ciMprime": "£422", "ciS": "£0"}},
                {"id": "constant", "label": "Marx's figures: 7,440 lb of the 10,000 sold",
                 "M": 422, "mp": 372, "lp": 50, "product": 500, "sold_share": "93/125", "expect": {"ciMprime": "£372", "ciS": "−£50"}},
                {"id": "unsold", "label": "The yarn is spun and none of it is sold yet",
                 "M": 422, "mp": 372, "lp": 50, "product": 500, "sold_share": 0, "expect": {"ciMprime": "£0", "ciS": "−£422"}},
            ],
            "panel_title": "One capital through three stages",
            "panel_intro": (
                "The money advanced, its split into means of production and labour-power, the "
                "value of the product and the share of it sold go in. The table gives the capital's "
                "value in each form; the tiles give the money returned and M′ − M. Compare the "
                "unsold preset's table with its tiles: the product is worth £500 either way."
            ),
        }),
        "steps_title": "Tracing a capital round its circuit",
        "steps_intro": "Four steps, the same for any industrial capital.",
        "steps": [
            ("Split M",
             "Divide the money advanced into the part that buys means of production and the "
             "part that buys labour-power. The two must add up to M; the lab refuses otherwise."),
            ("Value the product",
             "The product's value is the means of production transferred plus the new value the "
             "labour adds. Subtract M from it for the surplus value produced."),
            ("Sell",
             "M′ is the product's value times the share sold, on the chapter's assumption that "
             "everything sells at its value."),
            ("Compare M′ with M",
             "M′ − M is the surplus value realised. Below the break-even share it is negative: "
             "that much capital-value is still in commodity form, not lost."),
        ],
        "worked": {
            "title": "Marx's spinner, one week",
            "intro": [
                "Take Marx's own figures. You want the capital's value in each of its forms and "
                "the surplus value, first produced and then realised.",
            ],
            "lines": [
                "M–C:  £422 = £372 (means of production) + £50 (L)",
                "…P…:  £372 transferred + £128 new value = £500",
                "new value:  £128 = £50 (v) + £78 (s)",
                "C′–M′:  10,000 lb sold for £500",
                "M′ − M:  £500 − £422 = £78",
            ],
            "after": [
                "Sell 8,440 lb instead and M′ is £422, so M′ − M is £0, though the £78 of surplus "
                "value is still there in the 1,560 lb unsold. It was produced in the second line "
                "and is only realised in the last.",
            ],
        },
        "quiz_title": "Where the increase happens",
        "quiz": [
            {"q": "Marx's spinner advances £422 and his week's yarn, 10,000 lb, is worth £500. He "
                  "sells 8,440 lb at their value. How much surplus value has he realised in money?",
             "a": ["£0", "£78", "£422", "£500"],
             "c": 0,
             "why": "8,440 lb at a shilling a pound bring in £422, exactly M, so `M′ − M = 0`. The "
                    "£78 is the surplus value produced, still held in the 1,560 lb unsold. £422 "
                    "is the capital recovered, not a surplus, and £500 is what the whole lot "
                    "would fetch."},
            {"q": "On the chapter's account, in which stage of the circuit does the capital-value "
                  "grow from £422 to £500?",
             "a": ["M–C, because labour-power is bought below its value",
                   "The production stage, P",
                   "C′–M′, because the yarn is sold for more than it cost",
                   "None of them; the £78 is the capitalist's own wage"],
             "c": 1,
             "why": "The chapter assumes everything is bought and sold at its value, so neither "
                    "purchase nor sale changes the magnitude. The yarn is worth £500 when it "
                    "leaves the mill. The last option is the view Marx is arguing against, and "
                    "the chapter gives the capitalist no wage."},
            {"q": "Marx notes that £10 of a sum of £110 is 1/11 of the sum and also 1/10 of the "
                  "£100 advanced. What is the point about M′?",
             "a": ["That the rate of surplus value is 1/11",
                   "That nothing in a sum of money shows which part was advanced and which was added",
                   "That money loses a tenth of its value in circulation",
                   "That the capitalist can spend only 1/11 of his receipts"],
             "c": 1,
             "why": "Money is homogeneous, so the distinction between capital and surplus inside "
                    "M′ is only a mental one. The rate of surplus value is not computed from that "
                    "example, and nothing in the chapter says money loses value or limits "
                    "spending."},
            {"q": "In M–C the spinner's £422 divides into £372 for means of production and £50 for "
                  "labour-power. What fixes that proportion, according to the chapter?",
             "a": ["The prices the sellers happen to ask",
                   "The quantity of labour, surplus labour included, that the means of production must absorb",
                   "The capitalist's taste for machinery",
                   "The rate of interest on the money advanced"],
             "c": 1,
             "why": "Marx says the means of production must be enough to absorb the whole of the "
                    "labour bought, surplus labour included, and no more. Prices enter only through "
                    "the values, which the chapter takes as given; taste and interest play no part."},
        ],
        "mistakes": [
            ("Thinking the money at the end is where the surplus is made",
             "It is the natural reading of `M…M′`, and the monetary system Marx names made it: "
             "the gain is made by selling dear. The unsold preset refutes it. With nothing sold, the table "
             "still shows a product worth £500 against £422 advanced, while the tile for money "
             "returned is £0. The £78 was produced in the mill; the sale, at value, only changes "
             "its form, and at 8,440 lb sold none of it has been realised yet."),
            ("Treating money, productive and commodity capital as three kinds of business",
             "They are the forms one industrial capital takes in turn, &ldquo;special functions "
             "of industrial capital, assumed by it seriatim&rdquo;. The spinner's £422 is money "
             "capital on Monday and productive capital once the cotton and the spinners are in "
             "the mill. Banks and merchants come later, as these functions made independent."),
            ("Reading M–L as only a money transaction",
             "Paying wages is a purchase like any other in form. Marx's point is that money can "
             "buy labour-power on a social scale only where workers are separated from the means "
             "of production, which is why the Russian landowners could have money and still find "
             "no hands. The relation is in the conditions, not in the money."),
        ],
        "standard": (
            "Finish when you can trace a capital round M–C…P…C′–M′ and compute s from M and M′.",
            "Given the money advanced, its split into means of production and labour-power, the "
            "product's value and the share sold, give the capital's value in each of its three "
            "forms, compute M′ and M′ − M, and state whether the surplus value has been "
            "produced, realised, or both."
        ),
        "note": (
            "The lab assumes, as the chapter does, that every commodity sells at its value and "
            "that no value changes while the capital circulates, so a part of the yarn sold "
            "fetches exactly its share of £500. An unsold stock in fact often ends in a sale "
            "below value; the lab does not model that, and the chapter sets it aside on its "
            "first page. The spinner's figures are Marx's."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 2, l. 652 (the formula); l. 809 (the minimum for m).
    # Inline: l. 676 (spent, not advanced), l. 693 (480 or 500), l. 753
    # (no overproduction), l. 763 (a crisis comes), l. 839 (classical economy).
    {
        "slug": "the-circuit-of-productive-capital",
        "title": "The Circuit of Productive Capital",
        "module": "Chapter 2 · The Rotation of Productive Capital",
        "one_line": "Start the same movement from production and the money becomes a passing form, the surplus value leaves the circuit as revenue, and growth must wait for a sum large enough to invest.",
        "summary": (
            "Chapter 2 starts the spinner's circuit from production: P…C′–M′–C…P. Run it under "
            "simple reproduction, where the surplus value is spent and production restarts at "
            "£422, and under accumulation, where part of it re-enters and production restarts "
            "larger. Then hold the surplus value back as money until it reaches the least sum "
            "that can be invested, and compute the capital that re-enters P and the hoard that "
            "waits."
        ),
        "key": [
            "P…C′–M′–C…P: produce, sell, buy back",
            "simple: m spent, P restarts at £422",
            "enlarged: P′ = P + the s capitalised",
            "m below the minimum waits as a hoard",
            "a hoard is latent capital: it makes no s",
        ],
        "key_label": "The second circuit in five lines",
        "concepts_intro": (
            "The movement is the same as in Chapter 1. What changes is where you stand to watch "
            "it, and so what comes into view."
        ),
        "concepts": [
            ("Circulation between two productions",
             "In `P…P` the whole of circulation, the sale and the purchase back, sits between "
             "one production and the next. Money appears only in the middle and is dropped as "
             "soon as it appears. The movement has the shape `C–M–C`, buying in order to use."),
            ("Simple and enlarged reproduction",
             "If the surplus value is all spent as revenue, production restarts at the same "
             "size: simple reproduction. If some of it is laid out as capital, production "
             "restarts larger, `P′`: reproduction on an enlarged scale."),
            ("The hoard as latent capital",
             "A spindle cannot be bought by halves. Surplus value meant for investment that is "
             "smaller than the least useful addition is kept as money until it is big enough. "
             "Meanwhile it is capital only in waiting, and produces nothing."),
        ],
        "read_title": "The formula, and the money that must wait",
        "read_intro": (
            "The chapter's first sentence states the circuit. The passage on the minimum sum "
            "comes from its third section, where accumulation meets the plain fact that "
            "machines come in whole units."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 2.</strong> &ldquo;The rotation of productive "
                  "capital has the general formula P...C'-M'-C...P. It signifies the periodical "
                  "renewal of the function of productive capital, in other words its "
                  "reproduction, or its process of production as a reproductive process "
                  "generating surplus-value.&rdquo;"),
            ("p", "Same spinner, same £422, same £500 of yarn. But begin the story in the mill. "
                  "Then the sale and the purchase back, `C′–M′–C`, come in the middle, and their "
                  "only job is to turn this week's yarn into next week's cotton and labour-power. "
                  "Money is a form the capital takes for a moment and drops. Marx puts it "
                  "sharply: in `M…M′` money is where capital starts and ends; in `P…P` the "
                  "capital &ldquo;is just as anxious to assume this form in C' as it is to "
                  "discard it&rdquo;."),
            ("p", "Take simple reproduction first. The yarn sells for £500. £422 of it, the money "
                  "form of 8,440 lb, goes back into cotton, coal, wear and wages, and next week "
                  "starts as this one did. The other £78, the money form of 1,560 lb, leaves the "
                  "circuit altogether and goes on the capitalist's household, piece by piece. Of "
                  "that money Marx says: &ldquo;This money is not advanced, but spent.&rdquo; The "
                  "lab's simple preset shows the result: the capital at the end is £422, exactly "
                  "the capital at the start."),
            ("p", "That equality is what makes `P…P` easy to misread. Both ends are the same "
                  "productive capital, the surplus value shows up only as revenue walking out of "
                  "the circuit, and the whole thing looks like producing in order to consume. "
                  "Jean-Baptiste Say and James Mill built a famous argument on that look: every "
                  "sale is also a purchase, money only passes products from hand to hand, and so "
                  "there can never be more goods in general than buyers for them. Marx does not "
                  "name them in this chapter; his comment is one sentence, &ldquo;some economists "
                  "use this sort of exchange as a proof that there can be no "
                  "overproduction&rdquo;, and his answer is the money stage they treat as a "
                  "veil."),
            ("p", "The answer runs like this. Once the yarn is sold to a merchant, the "
                  "spinner's circuit goes on, whether or not anyone has yet used the yarn. "
                  "Production can grow, wages and the capitalists' spending can grow with it, and "
                  "much of the product can still be lying unsold in dealers' warehouses. Then the "
                  "next wave of goods arrives, the old bills fall due, and dealers sell at any "
                  "price to pay them. &ldquo;Then a crisis comes.&rdquo; It shows first, Marx "
                  "says, not in what households buy but in the exchange of capital for capital."),
            ("p", "Now let part of the surplus value stay in the circuit. Marx's own figure: the "
                  "capital may continue &ldquo;for instance as 480 pounds sterling or 500 pounds "
                  "sterling&rdquo;, that is, with £58 or all £78 of the surplus value added. The "
                  "accumulate preset adds £58 of the £78, so the next week's productive capital "
                  "is `£422 + £58 = £480`, and the original £422 is now `211/240` of it. The "
                  "circuit becomes `P…P′`."),
            ("p", "<strong>Volume II, Chapter 2, §3.</strong> &ldquo;In order to carry this out, "
                  "the surplus-value must have reached a considerable figure (one pound sterling "
                  "per spindle is generally assumed for new installations). So long as m does not "
                  "reach this figure, the cycle of the original capital must be repeated several "
                  "times, until the sum of the successively produced surplus-values m can take "
                  "part in the functions of M, in the process M'—C'.&rdquo;"),
            ("p", "This is the arithmetic of the hoard preset. Suppose the least useful "
                  "addition to the mill, spindles with the carding and preparing machines they "
                  "need, costs £200; the figure is illustrative. The spinner saves the whole £78 "
                  "each week. After one week he has £78 in hand and the capital at work is still "
                  "£422. Move the periods slider to 3: the hoard is £156 after two weeks and £234 "
                  "after three, which clears £200, so the whole £234 goes in and the capital "
                  "becomes £656. Until then the money is &ldquo;latent&rdquo; capital, Marx's "
                  "word: it adds nothing, and it grows only because other money is thrown into the "
                  "same safe."),
            ("p", "A hoard has a second use. If the yarn is slow to sell, or cotton has risen by "
                  "the time the money comes back, the capitalist can draw on it to keep the mill "
                  "running. Then it serves as a reserve fund. Marx keeps the two apart: money held "
                  "between purchases is part of the £422 doing its job, while a reserve comes out "
                  "of the £78 and enters the circuit only when conditions change."),
            ("p", "The chapter ends by naming whose view this circuit is: &ldquo;The cycle of "
                  "productive capital is that form, under which classical political economy "
                  "discusses the rotation process of industrial capital.&rdquo; Adam Smith and "
                  "David Ricardo thought about capital as stock that is used up and replaced year "
                  "by year, which is `P…P`, and they were right about what it shows. Marx's claim "
                  "is that it hides what `M…M′` shows, that the point of the whole movement is "
                  "more value."),
            ("p", "Two circuits, then, and a third is already implied in them, since the yarn "
                  "that ends one is where another begins. The next lesson, “The Circuit of "
                  "Commodity Capital”, starts there."),
        ],
        "lab": ("capkit", {
            "mode": "accumulate",
            "view": "expand",
            "money_unit": "£",
            "periods": 1,
            "preset": "simple",
            "presets": [
                {"id": "simple", "label": "Simple reproduction: all £78 of s spent as revenue",
                 "capital": 422, "c_v": "186/25", "s_rate": "39/25", "accumulate_share": 0,
                 "invest_threshold": 0, "expect": {"acCapital": "£422", "acHoard": "£0"}},
                {"id": "accumulate", "label": "Marx's figure: £58 of the £78 re-enters P",
                 "capital": 422, "c_v": "186/25", "s_rate": "39/25", "accumulate_share": "29/39",
                 "invest_threshold": 0, "expect": {"acCapital": "£480", "acHoard": "£0"}},
                {"id": "hoard", "label": "All of s saved, but nothing under £200 can be invested",
                 "capital": 422, "c_v": "186/25", "s_rate": "39/25", "accumulate_share": 1,
                 "invest_threshold": 200, "expect": {"acCapital": "£422", "acHoard": "£78"}},
            ],
            "panel_title": "What re-enters production",
            "panel_intro": (
                "The spinner's £422 at Marx's composition, £372 to £50, and rate of surplus "
                "value, £78 on £50, written as fractions. Choose how much of s is laid out again "
                "and the least sum that can be invested; a period is a week. The lab ships one "
                "week. Move the slider to 3 with the hoard preset to see the saved money go in."
            ),
        }),
        "steps_title": "Restarting production",
        "steps_intro": "Four steps for any week of the productive circuit.",
        "steps": [
            ("Sell C′ and split M′",
             "M′ is the capital-value M plus the surplus value m. At Marx's figures £500 is "
             "£422 plus £78."),
            ("Decide what m does",
             "The part of m spent as revenue leaves the circuit. The part meant for accumulation "
             "stays as money for now."),
            ("Compare with the minimum",
             "Add the part meant for accumulation to any hoard already held. If the total reaches "
             "the least sum that can be invested, all of it goes in; otherwise it waits."),
            ("Restart P",
             "The next productive capital is M plus whatever was invested. Under simple "
             "reproduction it is M again."),
        ],
        "worked": {
            "title": "Three ways to restart the spinner",
            "intro": [
                "The week's yarn has sold for £500. You want next week's productive capital "
                "under three decisions about the £78.",
            ],
            "lines": [
                "C′–M′:  £500 = £422 (M) + £78 (m)",
                "simple:  m spent, P restarts at £422",
                "accumulate:  £422 + £58 = £480",
                "hoard:  £78 < £200, P restarts at £422",
                "week 3:  3 · £78 = £234 ≥ £200, so £422 + £234",
            ],
            "after": [
                "Under the hoard, the capital at work in weeks 1 to 3 is £422 each week, and the "
                "fourth week starts at £656. The money waited two weeks in the safe and produced "
                "nothing while it waited.",
            ],
        },
        "quiz_title": "Producing, selling and starting again",
        "quiz": [
            {"q": "Under simple reproduction the spinner sells his yarn for £500. With what "
                  "productive capital does the next week begin?",
             "a": ["£422", "£500", "£78", "£578"],
             "c": 0,
             "why": "All £78 of surplus value is spent as revenue, so only the capital-value, "
                    "£422, re-enters production. £500 would mean all of s was capitalised, £78 is "
                    "the revenue itself, and £578 adds the surplus value twice."},
            {"q": "He lays out £58 of his £78 of surplus value as capital and spends the rest. "
                  "What is next week's productive capital?",
             "a": ["£480", "£500", "£442", "£422"],
             "c": 0,
             "why": "`£422 + £58 = £480`, Marx's own figure. £500 would capitalise all of it, "
                    "£442 adds the £20 spent instead of the £58 invested, and £422 is simple "
                    "reproduction."},
            {"q": "The spinner saves all £78 of surplus value each week, but nothing under £200 "
                  "can be invested. After which week's sale is the saved money first large "
                  "enough to invest?",
             "a": ["The first", "The second", "The third", "Never"],
             "c": 2,
             "why": "The hoard is £78, then £156, then £234, and £234 is the first sum to reach "
                    "£200, so it is laid out after the third week's sale and the fourth week starts "
                    "at £656. It would never be large enough only if nothing were saved."},
            {"q": "Why do the two ends of P…P show no difference in value under simple "
                  "reproduction?",
             "a": ["Because no surplus value was produced",
                   "Because the surplus value leaves the circuit as the capitalist's revenue",
                   "Because the yarn sold below its value",
                   "Because wages rose by £78"],
             "c": 1,
             "why": "£78 of surplus value was produced and the yarn sold at its value, but the £78 "
                    "was spent outside the circuit, so production restarts at £422. Wages are "
                    "£50 throughout."},
        ],
        "mistakes": [
            ("Taking the productive circuit for the money circuit started at a different point",
             "The movements are the same; what the two formulas show is not. `M…M′` runs from "
             "£422 to £500 and makes the increase its whole point. `P…P` under simple "
             "reproduction runs from £422 to £422, as the simple preset's tile shows: the "
             "surplus value appears only as revenue leaving the circuit, money is a passing "
             "form, and production for consumption is what it looks like. That is why the "
             "classical economists, who reasoned from it, could miss what the first form shows."),
            ("Counting a hoard as capital at work",
             "In the hoard preset £78 is held and the capital is still £422. Saved surplus value "
             "is capital only in intention until it is laid out; Marx calls it latent and sterile "
             "money capital. It grows only by additions, never by working."),
            ("Thinking a sale to a merchant means the product has been consumed",
             "The spinner's circuit continues as soon as the merchant pays, whatever becomes of "
             "the yarn. Sales between capitals can run ahead of final use for a long time, and "
             "Marx locates the start of a crisis in exactly that gap."),
        ],
        "standard": (
            "Finish when you can compute the capital that re-enters production and the money held back.",
            "Given the capital, its composition, the rate of surplus value, the share of surplus "
            "value laid out as capital and the least sum that can be invested, compute next "
            "period's productive capital and the hoard held, under simple and under enlarged "
            "reproduction."
        ),
        "note": (
            "The lab lays out the whole capital each week at the same composition and rate of "
            "surplus value, so capital added works exactly like the old. Marx warns that growth "
            "usually changes the composition, which is why he writes P′ and not L′ and Pm′. The "
            "£200 minimum is illustrative; the chapter's only figure is a pound a spindle."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 2, l. 847-853 (the formula and C''); l. 995 (the aggregate
    # capital). Inline: l. 861, l. 883-889 and l. 903-946 (the three lots and
    # the printed totals), l. 948 (the buyer), l. 1005 (avances and reprises),
    # l. 1013 (Quesnay).
    {
        "slug": "the-circuit-of-commodity-capital",
        "title": "The Circuit of Commodity Capital",
        "module": "Chapter 3 · The Circulation of Commodity-Capital",
        "one_line": "Starting from the product, already swollen with surplus value, shows the whole of what a capital puts on the market and how little of it is anyone's income.",
        "summary": (
            "The third circuit starts with the finished product, capital-value and surplus value "
            "together, and so it is the one that shows the whole product of a capital and, added "
            "up, of a society. Split Marx's 10,000 lb of yarn, and each of the three lots he "
            "sells it in, into the parts that replace means of production, that pay wages and "
            "that are surplus value, and see that most of the product is nobody's income."
        ),
        "key": [
            "C′–M′–C…P…C′: start from the product",
            "C′ = c + v + s, in money and in yarn",
            "£500 of yarn: c £372, v £50, s £78",
            "7,440 lb must buy back means of production",
            "only v + s, £128, is anyone's income",
        ],
        "key_label": "The third circuit in five lines",
        "concepts_intro": (
            "Chapter 3 is short and does one thing the first two circuits cannot: it starts from "
            "what the capital actually puts on the market."
        ),
        "concepts": [
            ("A circuit that starts swollen",
             "`M…M′` and `P…P` start from capital-value still to be valorised. `C′…C′` starts "
             "from the product, which already contains the surplus value, so it must be written "
             "with C′ at the start even when it repeats on the same scale."),
            ("The product in parts",
             "Every part of the product, down to a single pound of yarn, divides in the same "
             "proportions as the whole: so much replaces constant capital, so much variable, "
             "so much is surplus value."),
            ("The social product",
             "Because it starts from commodities, this circuit needs other capitals' commodities "
             "on the market to continue. Added up over all capitals it is the movement of a "
             "society's whole annual product."),
        ],
        "read_title": "The formula, then the product taken apart",
        "read_intro": (
            "The chapter opens with its formula. The passage on the aggregate capital, near the "
            "end, says why this circuit points beyond the single business."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 3.</strong> &ldquo;The general formula for the "
                  "cycle of commodity-capital is: C'—M'—C...P...C'. &hellip; If reproduction "
                  "takes place on an enlarged scale, then the final C' is greater than the "
                  "initial C' and we shall then call the final one C''.&rdquo;"),
            ("p", "Start from the yarn. It is not the capital that was advanced, it is that "
                  "capital plus what production added: in Marx's words this circuit opens "
                  "&ldquo;with augmented capital-value in the form of commodities&rdquo;. So "
                  "from its first step it carries two movements at once, the capital-value's and "
                  "the surplus value's, and they part company at the sale. That is why the "
                  "formula keeps the prime at both ends. The money circuit restarts as plain M, "
                  "even if it is now £500; this one restarts as C′, a product with surplus value "
                  "already in it."),
            ("p", "Marx then does the sum the circuit invites, and he does it in pounds of yarn. "
                  "At a shilling a pound, 10,000 lb are worth £500, which is £372 of constant "
                  "capital, £50 of variable and £78 of surplus value, or 7,440 lb, 1,000 lb and "
                  "1,560 lb of yarn. If the yarn sells in lots, each lot divides the same way. "
                  "His first lot is the 7,440 lb whose value equals the constant capital: of "
                  "those, 5,535.36 lb replace the constant capital used up in them, 744 lb their "
                  "wages and 1,160.64 lb are surplus product. The second lot, 1,000 lb, divides "
                  "into 744, 100 and 156; the third, 1,560 lb, into 1,160.64, 156 and 243.36. "
                  "The lab's four presets are these: marx is the whole 10,000 lb, and lot-1, lot-2 "
                  "and lot-3 are the 7,440 lb, 1,000 lb and 1,560 lb lots."),
            ("p", "Check his totals and you will find slips in the Kerr text's tables: the "
                  "first lot's surplus product printed as 1,160.740 lb, the third lot's as "
                  "343.360 lb a few lines after it was given as 243.360, and the grand total of "
                  "constant capital as 7,450 lb. The lab adds the lots exactly. Constant capital: "
                  "`5,535.36 + 744 + 1,160.64 = 7,440` lb. Surplus product: "
                  "`1,160.64 + 156 + 243.36 = 1,560` lb. Marx's conclusion stands; three sales "
                  "give the same result as one."),
            ("p", "None of this, Marx adds, is the buyer's business. A weaver buying the yarn "
                  "cares about the price, a shilling a pound, and how much yarn his own mill "
                  "needs. If he analyses the seller's costs during the haggling, &ldquo;he does so "
                  "simply with the malignant intention of proving that it can be sold at less "
                  "than 1 sh. per pound and still leave a fair profit to the seller.&rdquo; The "
                  "division into c, v and s matters only inside the circuit of the capital that "
                  "made the yarn."),
            ("p", "<strong>Volume II, Chapter 3.</strong> &ldquo;It is not merely a common mobile "
                  "form of all industrial capitals, but also the sum of all industrial capitals "
                  "in action. It is a movement of the aggregate capital of the capitalist class, "
                  "in which every individual capital appears only as a part whose movements "
                  "intermingle with those of the others and are conditioned on them.&rdquo;"),
            ("p", "Here is why. The spinner's C′–M′–C needs coal, cotton and machinery on the "
                  "market when his money comes back, and those are other capitals' C′. His "
                  "workers need bread and clothing on the market, which are others' C′ again. "
                  "Follow every capital's product at once and you are following a whole "
                  "society's annual product: which part of it replaces means of production used "
                  "up, which part feeds the workers, which part is consumed or accumulated by "
                  "capitalists."),
            ("p", "Adam Smith, whose <em>Wealth of Nations</em> of 1776 Marx argues with "
                  "throughout this volume, held that the price of every commodity resolves, "
                  "finally, into wages, profit and rent. His reasoning is strong: the cotton was "
                  "grown with paid labour, the spindle was made with paid labour, and if you "
                  "trace each input back far enough you find only incomes. Marx's reply fills "
                  "Volume II, Chapter 19, read in Reproduction of the Social Capital as “Former "
                  "Presentations: Quesnay and Smith”; this chapter's arithmetic already shows "
                  "the difficulty. In this year's £500 of yarn, £372 must buy back this year's "
                  "means of production, and only `£50 + £78 = £128` is income for anyone."),
            ("p", "Marx credits one economist with seeing this first. François Quesnay, court "
                  "physician at Versailles, drew his <em>Tableau Économique</em> in 1758 to show "
                  "a year's harvest passing between farmers, landlords and artisans. "
                  "&ldquo;C'...C' is the basis of Quesnay's Tableau Economique, and it shows "
                  "great discrimination on his part that he selected this form instead of P...P "
                  "as opposed to M...M' (which is the isolated formula retained by the "
                  "mercantilists).&rdquo; In the language of Quesnay's school, the second circuit "
                  "starts from the advances, the sowing, and the third from the returns, the "
                  "harvest."),
            ("p", "One consequence closes the chapter. If production is to grow next year, the "
                  "part of this year's surplus product to be capitalised must already exist as "
                  "cotton, spindles and food, not just as value. The next lesson, “The Three "
                  "Formulas of the Circuit”, sets the three circuits side by side and asks how "
                  "one capital can be in all of them at once."),
        ],
        "lab": ("capkit", {
            "mode": "surplus",
            "view": "parts",
            "money_unit": "£",
            "qty_unit": "lb",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: all 10,000 lb of yarn, £372 c + £50 v + £78 s",
                 "c": 372, "v": 50, "s": 78, "output": 10000, "expect": {"suProduct": "£500", "suParts": "c: 7,440 lb, v: 1,000 lb, s: 1,560 lb"}},
                {"id": "lot-1", "label": "Marx's first lot: 7,440 lb worth £372",
                 "c": "34596/125", "v": "186/5", "s": "7254/125", "output": 7440, "expect": {"suProduct": "£372", "suParts": "c: 138,384/25 lb, v: 744 lb, s: 29,016/25 lb"}},
                {"id": "lot-2", "label": "Marx's second lot: 1,000 lb worth £50",
                 "c": "186/5", "v": 5, "s": "39/5", "output": 1000, "expect": {"suProduct": "£50", "suParts": "c: 744 lb, v: 100 lb, s: 156 lb"}},
                {"id": "lot-3", "label": "Marx's third lot: 1,560 lb worth £78",
                 "c": "7254/125", "v": "39/5", "s": "1521/125", "output": 1560, "expect": {"suProduct": "£78", "suParts": "c: 29,016/25 lb, v: 156 lb, s: 6,084/25 lb"}},
            ],
            "panel_title": "The yarn taken apart",
            "panel_intro": (
                "A lot of yarn's value parts and its weight go in; the lab gives its value and "
                "the pounds of yarn that carry each part. The lots' values are Marx's decimals "
                "written as fractions, £276.768 as 34596/125, and the tiles print fractions too: "
                "138,384/25 lb is 5,535.36 lb. Add the three lots' tiles and compare them with "
                "the whole."
            ),
        }),
        "steps_title": "Dividing a product into its value parts",
        "steps_intro": "Four steps for any lot of a product made by a capital.",
        "steps": [
            ("Total the value",
             "The value of the lot is c + v + s. Divide by the output for the value of one unit."),
            ("Take each part's share",
             "Each part's share of the value is that part over the total: for the whole yarn, "
             "372/500, 50/500 and 78/500."),
            ("Convert to units",
             "Multiply the output by each share. The units carrying c, v and s add back to the "
             "output."),
            ("Send each part where it goes",
             "The units carrying c must buy back means of production. Those carrying v are paid "
             "out as wages; those carrying s are the capitalist's to consume or accumulate."),
        ],
        "worked": {
            "title": "Ten thousand pounds of yarn in three parts",
            "intro": [
                "Take the whole product, valued at a shilling a pound. You want the pounds of "
                "yarn that carry each part of its value, and the part that is anyone's income.",
            ],
            "lines": [
                "value:  £372 + £50 + £78 = £500",
                "c:  10,000 · 372/500 = 7,440 lb",
                "v:  10,000 · 50/500 = 1,000 lb",
                "s:  10,000 · 78/500 = 1,560 lb",
                "income:  £50 + £78 = £128 of £500",
            ],
            "after": [
                "Run the three lot presets and add their tiles: 5,535.36 + 744 + 1,160.64 lb of "
                "c come to 7,440, and the v and s parts come to 1,000 and 1,560. The lots "
                "rebuild the whole exactly.",
            ],
        },
        "quiz_title": "The product in parts",
        "quiz": [
            {"q": "Of the spinner's 10,000 lb of yarn, worth £500, how many pounds of yarn carry "
                  "the constant capital of £372?",
             "a": ["7,440 lb", "8,440 lb", "1,560 lb", "5,535.36 lb"],
             "c": 0,
             "why": "`10,000 · 372/500 = 7,440`. 8,440 lb carry c and v together, 1,560 lb carry "
                    "the surplus value, and 5,535.36 lb is the constant capital inside the first "
                    "lot only."},
            {"q": "Marx's first lot is 7,440 lb of yarn worth £372. How many pounds of it are "
                  "surplus product?",
             "a": ["1,160.64 lb", "1,560 lb", "744 lb", "5,535.36 lb"],
             "c": 0,
             "why": "The lot divides like the whole: `7,440 · 78/500 = 1,160.64`. 1,560 lb is the "
                    "surplus product of the whole 10,000 lb, 744 lb is the lot's variable part "
                    "and 5,535.36 lb its constant part."},
            {"q": "How much of the £500 of yarn is income for anyone, worker or capitalist, once "
                  "the means of production used up are replaced?",
             "a": ["£500", "£128", "£78", "£372"],
             "c": 1,
             "why": "Wages and surplus value, `£50 + £78 = £128`. £78 is the capitalist's part "
                    "alone. £372 must buy back means of production, and £500 is Adam Smith's "
                    "answer, which leaves nothing to replace the cotton and the spindles."},
            {"q": "Why must the circuit of commodity capital be written with C′ at its start even "
                  "when it repeats on the same scale?",
             "a": ["Because the yarn is sold above its value",
                   "Because it starts from a product that already contains surplus value",
                   "Because the capital grows every time it turns",
                   "Because money never appears in it"],
             "c": 1,
             "why": "It opens with capital-value plus surplus value in commodity form. The yarn "
                    "sells at its value, the capital need not grow under simple reproduction, and "
                    "money does appear, as M′ in the middle."},
        ],
        "mistakes": [
            ("Treating the whole product as revenue to be consumed",
             "Adam Smith's version is the strongest: trace every input back and you find only "
             "wages, profit and rent. The marx preset answers for one year's product: of 10,000 "
             "lb, 7,440 lb carry £372 that must buy back cotton, coal and wear, or next year's "
             "spinning cannot happen. Only 2,560 lb, `£128`, are anyone's income."),
            ("Thinking only a divisible product can be split into its parts",
             "Yarn can be cut into lots; a machine cannot. The division still holds in value: "
             "Marx notes that London builders, working on credit, drew advances against stages "
             "of a house that were each an ideal fraction of it. The proportions are the same; "
             "only the separate sale is impossible."),
            ("Reading the seller's composition into the buyer's purchase",
             "How much yarn a weaver buys depends on his own mill, not on the spinner's c, v and "
             "s. The division into parts is internal to the circuit of the capital that made the "
             "product, and the buyer meets only the price."),
        ],
        "standard": (
            "Finish when you can split a product into the parts that return as means of production, wages and surplus value.",
            "Given a lot's constant capital, variable capital, surplus value and output, compute "
            "its value and the units that carry each part, and state which part must buy back "
            "means of production and which parts are income."
        ),
        "note": (
            "The lab divides a product in the proportions of its value. It cannot say who will "
            "buy each part, or whether the means of production the £372 must buy will be on the "
            "market; that is the question of the reproduction schemes, in Reproduction of the "
            "Social Capital. Every figure here is Marx's."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 2, l. 1049 (the unity of the three cycles); l. 1053 (one
    # part in each form). Inline: l. 1041 (the Chinese artisan), l. 1065 (a
    # thing in motion), l. 1071 (Bailey), l. 1154 (sells dearer).
    {
        "slug": "the-three-formulas-of-the-circuit",
        "title": "The Three Formulas of the Circuit",
        "module": "Chapter 4 · The Three Diagrams of the Process of Circulation",
        "one_line": "A continuous business is in all three circuits at once, with part of its capital in each form at every moment, and the share in each form is the share of the circuit's time spent in it.",
        "summary": (
            "So far the spinner's £422 moved in one lump, so production stopped while the yarn "
            "was on the market. Chapter 4 makes the business continuous: the capital is divided, "
            "and at any moment one part is money, one is at work and one is waiting to be sold. "
            "Compute how a capital divides among the three forms when each stage takes a stated "
            "number of weeks, and see what a slow sale does to the division."
        ),
        "key": [
            "M…M′, P…P, C′…C′: three circuits, one capital",
            "continuity: every form at every moment",
            "share in a form = its weeks / all weeks",
            "4, 4, 4 weeks: a third in each form",
            "slow sale: more capital as commodities",
        ],
        "key_label": "Three circuits at once",
        "concepts_intro": (
            "Chapter 4 adds nothing new to the circuit. It adds time, and the fact that a real "
            "business does not stop."
        ),
        "concepts": [
            ("Three circuits, one capital",
             "Each formula is the same movement seen from a different starting point. A "
             "continuous capital describes all three at once, because some part of it is always "
             "starting from each point."),
            ("Succession becomes simultaneity",
             "Every part of the capital goes through the stages one after another. Because the "
             "parts are staggered, the capital as a whole is in every stage at the same time."),
            ("Value in motion",
             "Capital is value that keeps its identity through changes of form and compares "
             "itself, at the end, with what it was at the start. It is a movement, and cannot be "
             "understood at rest."),
        ],
        "read_title": "The unity of the three circuits",
        "read_intro": (
            "The passage comes from the middle of the chapter, where Marx turns from the "
            "capital that moves in one piece to the capital that is always in motion."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 4.</strong> &ldquo;The actual rotation of "
                  "industrial capital in its continuity is therefore not alone the unity of the "
                  "processes of production and circulation, but also the unity of its three "
                  "cycles. But it can be such a unity only, if every individual part of capital "
                  "can go successively through the various stages of the rotation, pass from one "
                  "phase and from one functional form to another, so that the industrial capital, "
                  "being the aggregate of all these parts, is found simultaneously in its various "
                  "phases and functions and describes all three cycle at the same time.&rdquo;"),
            ("p", "Marx writes the three formulas in one line each, with Tc for the whole "
                  "process of circulation: `M–C…P…C′–M′`, then `P…Tc…P`, then `Tc…P (C′)`. "
                  "Up to now the £422 went round in one piece: all money, then all at work, then "
                  "all yarn. Taken literally, that means the mill stands idle while the yarn is "
                  "on the market and while the money buys cotton. Marx's example of a business "
                  "that really works this way is a Chinese artisan who works only for private "
                  "customers and waits, between orders, for the next one."),
            ("p", "A factory does not wait. While this week's 10,000 lb of yarn are being sold, "
                  "last week's money is buying cotton, and the cotton bought before that is being "
                  "spun. The capital has been divided, and the division is what makes the "
                  "continuity:"),
            ("p", "<strong>Volume II, Chapter 4.</strong> &ldquo;One part of capital, continually "
                  "changing, continually reproduced, exists as a commodity-capital which is "
                  "converted into money; another as money-capital converted into productive "
                  "capital; and a third as productive capital converted into "
                  "commodity-capital.&rdquo;"),
            ("p", "How big is each part? If production runs evenly, each part's share of the "
                  "capital is the share of the circuit's time spent in that form. Four weeks "
                  "buying, four producing and four selling make a 12-week circuit, and at any "
                  "moment a third of the capital is in each form, `4/12 = 1/3`: the even preset. "
                  "In the slow-sale preset selling takes eight weeks and the circuit is 16 weeks, with half of the capital in "
                  "commodity form, `8/16 = 1/2`, and only a quarter at work. The fast preset, "
                  "two weeks buying, six producing, two selling, has `6/10 = 3/5` of its capital "
                  "producing at any time."),
            ("p", "The price of continuity is that every interruption spreads. If one batch of "
                  "yarn cannot be sold, the money to replace its cotton never comes, and the "
                  "batches behind it &ldquo;find the conversion of their function blocked by "
                  "their predecessors&rdquo;. The simultaneity is only the result of the "
                  "succession; stop the succession and the whole capital stops."),
            ("p", "Marx draws a large conclusion. Capital, &ldquo;as a value creating more "
                  "value&rdquo;, can be understood &ldquo;only as a thing in motion, not as a "
                  "thing at rest&rdquo;. It is value that stays identical with itself through "
                  "money, means of production and yarn, and keeps comparing its present size "
                  "with its starting size. When prices of cotton or coal change during the "
                  "circuit, the same £422 may no longer buy back the same means of production, "
                  "and money capital is tied up or set free."),
            ("p", "This is where he answers Samuel Bailey, the Sheffield writer whose 1825 "
                  "<em>Critical Dissertation</em> was the sharpest attack on Ricardo's theory of "
                  "value. Bailey argued that value is nothing but a ratio of exchange: &ldquo;value "
                  "is a relation between contemporary commodities, because such only admit of "
                  "being exchanged with each other.&rdquo; On that view, comparing a value now "
                  "with a value last year is meaningless, and modern economics largely agrees "
                  "with him that value is a relative price. Marx's reply is that a capital does "
                  "exactly that comparison on every circuit: £422 laid out in March is measured "
                  "against £500 back in June, and capital exists only as that comparison."),
            ("p", "One more line from the chapter belongs with the first lesson. The capitalist "
                  "does &ldquo;sell dearer than he has bought&rdquo;, Marx concedes, but "
                  "&ldquo;He sells dearer, not because he gets more than the value of his "
                  "commodity, but because his commodity contains a greater value than that "
                  "contained in the natural elements of its production.&rdquo;"),
            ("p", "Time has now entered the circuit as weeks in each stage. The next lesson, "
                  "“The Time of Circulation”, asks what the weeks spent buying and selling "
                  "produce."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "phases",
            "preset": "even",
            "presets": [
                {"id": "even", "label": "4 weeks buying, 4 producing, 4 selling",
                 "stage_weeks": [4, 4, 4], "expect": {"tuMoney": "1/3 = 33.33%", "tuProductive": "1/3 = 33.33%", "tuCommodity": "1/3 = 33.33%"}},
                {"id": "slow-sale", "label": "Selling slows to 8 weeks",
                 "stage_weeks": [4, 4, 8], "expect": {"tuMoney": "1/4 = 25%", "tuProductive": "1/4 = 25%", "tuCommodity": "1/2 = 50%"}},
                {"id": "fast", "label": "2 weeks buying, 6 producing, 2 selling",
                 "stage_weeks": [2, 6, 2], "expect": {"tuMoney": "1/5 = 20%", "tuProductive": "3/5 = 60%", "tuCommodity": "1/5 = 20%"}},
            ],
            "panel_title": "Where the capital is at any moment",
            "panel_intro": (
                "The weeks a part of the capital spends as money capital, as productive capital "
                "and as commodity capital go in, in that order. For a business that runs evenly, "
                "the tiles are the shares of its capital in each form at any moment. Compare the "
                "even and slow-sale presets: only the selling time changes."
            ),
        }),
        "steps_title": "Dividing a continuous capital",
        "steps_intro": "Four steps for any business that runs without stopping.",
        "steps": [
            ("List the stages",
             "Write the weeks a batch spends as money being turned into means of production and "
             "labour-power, in production, and as commodities waiting to be sold."),
            ("Add for one circuit",
             "The circuit time is the sum of the three. A batch begins again only after all "
             "three."),
            ("Divide each by the circuit",
             "Each stage's weeks over the circuit's weeks gives the share of time spent in that "
             "form. The three shares add to 1."),
            ("Read the shares as capital",
             "If production is even, those are the shares of the capital held in each form at "
             "any moment. A longer stage holds more of the capital."),
        ],
        "worked": {
            "title": "A third in each form",
            "intro": [
                "A business takes 4 weeks to buy its inputs, 4 to produce and 4 to sell, and "
                "never stops. You want the share of its capital in each form, then the same when "
                "selling slows to 8 weeks.",
            ],
            "lines": [
                "circuit:  4 + 4 + 4 = 12 weeks",
                "money:  4/12 = 1/3",
                "productive:  4/12 = 1/3",
                "commodity:  4/12 = 1/3",
                "slow sale:  4 + 4 + 8 = 16; commodity 8/16 = 1/2",
            ],
            "after": [
                "With the slow sale only `4/16 = 1/4` of the capital is at work at any moment, "
                "against a third before. To keep the same production going, the business would "
                "need a larger capital.",
            ],
        },
        "quiz_title": "One capital in three forms",
        "quiz": [
            {"q": "A business spends 2 weeks buying, 6 producing and 2 selling, and runs evenly "
                  "without stopping. What share of its capital is productive capital at any "
                  "moment?",
             "a": ["3/5", "1/5", "1/3", "2/5"],
             "c": 0,
             "why": "`6/(2 + 6 + 2) = 3/5`. One fifth is the share in either money or commodity "
                    "form, a third would need equal stages, and two fifths is the money and "
                    "commodity forms together."},
            {"q": "Selling slows from 4 weeks to 8 while buying and producing stay at 4 weeks "
                  "each. What share of the capital is now commodity capital?",
             "a": ["1/3", "1/2", "2/3", "1/4"],
             "c": 1,
             "why": "`8/(4 + 4 + 8) = 1/2`. A third was the share before the slowdown, a quarter "
                    "is now the share in each of the other two forms, and two thirds counts the "
                    "selling weeks against the other eight."},
            {"q": "Samuel Bailey held that value is a relation between commodities exchanged at "
                  "the same time. What does Marx say this misses?",
             "a": ["That market prices fluctuate from day to day",
                   "That capital is value compared with itself across the successive stages of its circuit",
                   "That gold has a value of its own",
                   "That labour-power is bought before it is paid"],
             "c": 1,
             "why": "Capital exists as value measured at the end against its own size at the "
                    "start, months apart. The other three are true statements that the chapter "
                    "does not use against Bailey."},
            {"q": "Which of the three circuits does a continuous industrial capital describe?",
             "a": ["Only M…M′, since every capital starts as money",
                   "Only P…P, since its production never stops",
                   "All three at once, through different parts of the capital",
                   "None of them, since continuity removes the stages"],
             "c": 2,
             "why": "Some part of the capital is always starting from each of money, production "
                    "and the product, so all three circuits run side by side. Continuity does "
                    "not remove the stages; it staggers them."},
        ],
        "mistakes": [
            ("Thinking a capital is in one form at a time",
             "It is true of a capital that moves in one lump, and then production stops "
             "whenever the product is on the market, like the artisan who works to order. A "
             "continuous business is never like that. In the even preset a third of the "
             "capital is in each form at every moment, and in the slow-sale preset half of it "
             "is unsold product while a quarter is at work."),
            ("Taking the three formulas for three kinds of capitalist",
             "A banker, a manufacturer and a merchant are not the three circuits. All three "
             "circuits belong to one industrial capital; they are three points from which its "
             "single movement can be read."),
            ("Thinking the division is the capitalist's choice",
             "The shares follow from the times. A capitalist can choose to hold a larger stock, "
             "but if selling takes eight weeks the slow-sale preset's half in commodity form is "
             "forced on him, whatever he would prefer."),
        ],
        "standard": (
            "Finish when you can divide a continuous capital among its three forms.",
            "Given the weeks a capital spends as money, productive and commodity capital, "
            "compute the circuit time and the share of the capital in each form at any moment, "
            "and state how the shares move when one stage lengthens."
        ),
        "note": (
            "The lab reads the share of time spent in a form as the share of capital held in "
            "it. That holds only when production runs evenly and every batch carries the same "
            "value, and it counts the capital-value advanced, not the surplus value that the "
            "commodity stage also holds. The weeks are illustrative; Marx gives none in this "
            "chapter."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Kerr vol. 2, l. 1233 (the two times exclude one another); l. 1235
    # (circulation time limits production time). Inline: l. 1237 (the
    # negative taken for positive), l. 1247 (the sale more important),
    # l. 1251 (breweries, dairies).
    {
        "slug": "the-time-of-circulation",
        "title": "The Time of Circulation",
        "module": "Chapter 5 · The Time of Circulation",
        "one_line": "Time spent buying and selling is time in which the capital produces nothing, so the turnover is production time plus circulation time, and circulation time is a limit, not a source.",
        "summary": (
            "A capital spends part of its life producing and part of it being sold and bought "
            "back. Compute the turnover time as production time plus circulation time, and the "
            "share of the turnover spent in circulation, for a spinner selling near home, one "
            "whose sale takes as long as production, and one shipping to a distant market. "
            "Chapter 5's claim is that the second share produces nothing at all."
        ),
        "key": [
            "turnover = production + circulation",
            "circulation share = circulation / turnover",
            "6 + 6 weeks: 12 weeks, half circulating",
            "circulation time produces no value",
            "only the sale realises s, not the purchase",
        ],
        "key_label": "Two times that exclude each other",
        "concepts_intro": (
            "Chapter 5 is short and introduces the measure the rest of Volume II is built on: "
            "time."
        ),
        "concepts": [
            ("Time of production",
             "The time the capital spends in the sphere of production. It includes the labour "
             "time and more besides: nights, stocks waiting to be used, and natural processes "
             "such as fermenting or drying."),
            ("Time of circulation",
             "The time the capital spends as commodities being sold and as money being turned "
             "back into means of production and labour-power. During it the capital produces "
             "neither products nor surplus value."),
            ("A negative limit",
             "Circulation time does not make value. It limits the part of a capital that can be "
             "producing, and the longer it is, the tighter the limit."),
        ],
        "read_title": "Two times that exclude one another",
        "read_intro": (
            "The passage is the chapter's turning point: after defining both times, Marx says "
            "what one of them does to the other."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 5.</strong> &ldquo;The time of circulation and "
                  "time of production mutually exclude one another. During its time of "
                  "circulation, capital does not perform the functions of productive capital and "
                  "therefore produces neither commodities nor surplus-value.&rdquo;"),
            ("p", "The chapter gives no figures, so the lab supplies them. A spinner's yarn "
                  "takes six weeks from raw cotton to finished stock; selling it and buying back "
                  "cotton and labour-power takes another six. The capital's turnover, the time "
                  "until the value advanced is back in its starting form, is `6 + 6 = 12` weeks, "
                  "the slow-sale preset. Half of those weeks, `6/12`, the capital is not in "
                  "production at all. The spinning preset sells faster, in 2 weeks: an 8-week "
                  "turnover with a quarter of it in circulation."),
            ("p", "First, what counts as production time. It is longer than the labour time. "
                  "The mill stands at night with its machines still in it; cotton waits in "
                  "store so that spinning need not depend on each day's deliveries; grain lies in "
                  "the ground and wine in the cellar with no one working on them. All of that is "
                  "time in the sphere of production. Marx's point is that only the part in which "
                  "labour is actually applied creates value, and that capitalists therefore try "
                  "to close the gap, which is why mills ran at night. That difference has its own "
                  "lesson, “The Time of Production”, in The Turnover of Capital; here the "
                  "production time is taken whole."),
            ("p", "Circulation time is the rest. If the whole capital moves in one lump, "
                  "production simply stops while it lasts. If the capital is divided, as in the "
                  "last lesson, production can continue, but the part of the capital in "
                  "production must be smaller, the longer the other parts spend on the market."),
            ("p", "<strong>Volume II, Chapter 5.</strong> &ldquo;In short, the time of "
                  "circulation of a certain capital limits its time of production and the process "
                  "of creating surplus-value. And this limitation is proportional to the duration "
                  "of the time of circulation.&rdquo;"),
            ("p", "So why does it look otherwise to the people who run businesses? Marx says "
                  "political economy &ldquo;takes this negative effect for a positive one, because "
                  "its results are positive&rdquo;, and gives three reasons. Capitals with longer "
                  "circulation times end up charging higher prices when profits are equalised, "
                  "which Volume III explains. The circulation time is folded into the turnover, "
                  "so effects of the whole turnover are credited to it. And accumulation turns "
                  "money into extra wages during circulation, so growth seems to happen there."),
            ("p", "Of the two parts of circulation, selling is usually the longer and always the "
                  "more important. Buying cotton converts value from one form to another. "
                  "Selling yarn does that and also realises the surplus value in it: the sale is "
                  "the moment the £78 becomes money, while the purchase is only &ldquo;the "
                  "intimation of its production, not its after-effect&rdquo;."),
            ("p", "The sale also has an absolute limit in the commodity's body. Use-values "
                  "spoil, and a product that must be consumed soon after it is made has a short "
                  "circulation time and a local market. Marx notes that concentrating such "
                  "production near large towns can still create big markets for it, &ldquo;such "
                  "as the product of large beer-breweries, dairies, etc.&rdquo; The "
                  "distant-market preset goes the other way: a product that keeps, shipped to a "
                  "market twenty weeks away, spends `20/26 = 10/13` of its turnover in "
                  "circulation."),
            ("p", "The strongest objection comes from economists who make time itself "
                  "productive. Eugen von Böhm-Bawerk argued in the 1880s that roundabout methods "
                  "of production yield more, that waiting for their yield is a real sacrifice, "
                  "and that interest is its price; later theories of the time value of money "
                  "build on the same thought. On that view, capital tied up for longer has earned "
                  "more. Marx's answer, on his definitions, is that waiting adds no labour and so "
                  "no value, and that any extra a longer-waiting capital receives is a share of "
                  "value produced elsewhere."),
            ("p", "Buying and selling also need people to do them, and they must be paid. The "
                  "next lesson, “The Costs of Circulation”, asks whether what they are paid "
                  "adds anything to the value of the product."),
        ],
        "lab": ("capkit", {
            "mode": "turnover",
            "view": "time",
            "preset": "spinning",
            "presets": [
                {"id": "spinning", "label": "6 weeks of production, 2 of circulation",
                 "production_weeks": 6, "circulation_weeks": 2, "expect": {"tuTurnover": "8 weeks", "tuCirculationShare": "1/4 = 25%"}},
                {"id": "slow-sale", "label": "Circulation as long as production: 6 and 6 weeks",
                 "production_weeks": 6, "circulation_weeks": 6, "expect": {"tuTurnover": "12 weeks", "tuCirculationShare": "1/2 = 50%"}},
                {"id": "distant-market", "label": "A market 20 weeks away: 6 and 20 weeks",
                 "production_weeks": 6, "circulation_weeks": 20, "expect": {"tuTurnover": "26 weeks", "tuCirculationShare": "10/13 = 76.92%"}},
            ],
            "panel_title": "Production time, circulation time, turnover",
            "panel_intro": (
                "The weeks in production and in circulation go in; the year is 52 weeks. The "
                "lab adds them for the turnover and gives the share of it spent circulating. "
                "Working time is left equal to production time, and no capital is stated, so "
                "the value-turned-over tile stays blank; both belong to The Turnover of Capital."
            ),
        }),
        "steps_title": "Measuring a turnover",
        "steps_intro": "Four steps for any capital, divided or not.",
        "steps": [
            ("Measure the production time",
             "Count every week the capital spends in the sphere of production, stocks and "
             "pauses included, not only the weeks of labour."),
            ("Measure the circulation time",
             "Count the weeks the product takes to sell and the money takes to be turned back "
             "into means of production and labour-power."),
            ("Add for the turnover",
             "The turnover time is the sum. A year of 52 weeks divided by it gives the "
             "turnovers a year."),
            ("Divide for the circulation share",
             "Circulation time over turnover time is the share of the capital's life in which "
             "it produces nothing."),
        ],
        "worked": {
            "title": "Six weeks of each",
            "intro": [
                "A capital spends 6 weeks in production and 6 in circulation. You want its "
                "turnover time, the share of it spent circulating, and the turnovers in a year.",
            ],
            "lines": [
                "turnover:  6 + 6 = 12 weeks",
                "circulating:  6/12 = 1/2",
                "turnovers a year:  52/12 = 13/3",
                "distant market:  6 + 20 = 26 weeks; 20/26 = 10/13",
            ],
            "after": [
                "Shorten circulation to 2 weeks and the turnover is 8 weeks, with only a quarter "
                "of it circulating: the same production time now fills three quarters of the "
                "capital's life.",
            ],
        },
        "quiz_title": "Producing and circulating",
        "quiz": [
            {"q": "Production takes 6 weeks, and selling and buying back take 2. What share of "
                  "the turnover is circulation time?",
             "a": ["1/4", "1/3", "3/4", "1/8"],
             "c": 0,
             "why": "`2/(6 + 2) = 1/4`. A third divides circulation by production time instead of "
                    "by the turnover, three quarters is production's share, and an eighth divides "
                    "one week by the turnover."},
            {"q": "A capital needs 6 weeks of production and 20 of circulation. How many times "
                  "does it turn over in a 52-week year?",
             "a": ["2", "26/3", "4", "1"],
             "c": 0,
             "why": "The turnover is `6 + 20 = 26` weeks, and `52/26 = 2`. 26/3 ignores the "
                    "circulation time, and 4 and 1 match no turnover in the question."},
            {"q": "On the chapter's argument, what does a capital produce during its time of "
                  "circulation?",
             "a": ["Neither commodities nor surplus value",
                   "Surplus value but no commodities",
                   "Commodities but no surplus value",
                   "Surplus value in proportion to the time"],
             "c": 0,
             "why": "Marx's sentence is that during circulation capital &ldquo;produces neither "
                    "commodities nor surplus-value&rdquo;. The other three each credit "
                    "circulation with something it does not do on his account."},
            {"q": "Why is the sale, C′–M′, more important to an industrial capital than the "
                  "purchase, M–C?",
             "a": ["The sale realises the surplus value in the commodity; the purchase does not",
                   "The sale always takes less time than the purchase",
                   "Money spoils if it is not spent",
                   "The purchase is made on credit and the sale is not"],
             "c": 0,
             "why": "Both convert value from one form to another, but only the sale turns the "
                    "surplus value into money. The sale usually takes longer, not less time; "
                    "money does not spoil; and credit is set aside in this volume."},
        ],
        "mistakes": [
            ("Thinking a capital produces value for as long as it is tied up",
             "Tied up is not the same as at work. In the distant-market preset the capital is "
             "tied up for 26 weeks and producing for 6 of them; the tile shows `10/13` of the "
             "turnover in circulation, in which, on the chapter's argument, no value and no "
             "surplus value is produced."),
            ("Crediting a long circulation time with the profit it seems to bring",
             "When profits are equalised, a capital that circulates slowly does charge more, and "
             "this is the appearance Marx says political economy took for a cause. On his "
             "account the extra is a share of surplus value produced in other capitals' "
             "production time, redistributed, not made by waiting."),
            ("Equating production time with labour time",
             "Production time includes nights, stocks on hand and natural processes in which no "
             "one works. Only the labour time within it creates value; the difference matters in "
             "The Turnover of Capital, and this lesson's lab sets the two equal."),
        ],
        "standard": (
            "Finish when you can compute a turnover and the share of it spent in circulation.",
            "Given production and circulation times, compute the turnover time, the turnovers "
            "in a year, and the share of the turnover spent in circulation, and state what the "
            "capital produces in that share."
        ),
        "note": (
            "The lab takes the circulation time as given. What makes it long or short, distance, "
            "transport, credit and the state of the market, is outside the arithmetic, and "
            "Volume II, Chapter 14 returns to it. The weeks are illustrative; the chapter gives "
            "none."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Kerr vol. 2, l. 1398 (the general law); l. 1406 (transport adds
    # value). Inline: l. 1267 and l. 1269 (Greek meets Greek; combustion),
    # l. 1271 (transubstantiation), l. 1278 (the clerk's 10 hours), l. 1296
    # (bookkeeping), l. 1338 (Adam Smith), l. 1371-1373 (the buyer), l. 1390,
    # l. 1414 (railway magnates).
    {
        "slug": "the-costs-of-circulation",
        "title": "The Costs of Circulation",
        "module": "Chapter 6 · The Expenses of Circulation",
        "one_line": "Costs that only change the form of value, buying, selling, book-keeping and money itself, add nothing and come out of surplus value; storage that preserves a product and transport that moves it add value.",
        "summary": (
            "Every business pays for things that do not make its product: clerks, book-keepers, "
            "warehouses, carters. Chapter 6 sorts them. Classify circulation costs as pure costs, "
            "which only change the form of value and are deducted from surplus value, or as "
            "costs that add value, transport and necessary storage, and compute what is left of "
            "a surplus value of £100 after each."
        ),
        "key": [
            "pure costs: buying, selling, books, money",
            "pure costs are paid out of surplus value",
            "necessary storage and transport add value",
            "s after costs = s − pure costs",
            "£100 of s less a £10 clerk: £90",
        ],
        "key_label": "Which costs add value",
        "concepts_intro": (
            "The chapter's three sections are three kinds of cost, and the line between them is "
            "the line between changing value's form and doing something to the product."
        ),
        "concepts": [
            ("Pure costs of circulation",
             "The labour and materials spent on buying, selling, keeping accounts, and the gold "
             "used as money. They change the form of value and add none. Marx calls them dead "
             "expenses: from the point of view of the capitalist class they are deductions from "
             "surplus value."),
            ("Storage",
             "Keeping a stock costs buildings, labour and losses. A stock the flow of trade "
             "requires preserves the product's use-value, and its cost enters the value. A stock "
             "piled up because it will not sell adds nothing and is a loss."),
            ("Transport",
             "Moving a product to where it is consumed is production continued inside "
             "circulation. The labour and wear of carriage add value to the goods carried."),
        ],
        "read_title": "The general law, then its exception",
        "read_intro": (
            "The passage that states the rule comes at the start of the section on transport, "
            "where Marx sums up the two before it. The exception follows straight after."
        ),
        "body": [
            ("p", "<strong>Volume II, Chapter 6, §3.</strong> &ldquo;The general law is that "
                  "all expenses of circulation, which arise only from changes of form, do not add "
                  "any value to the commodities. They are merely expenses required for the "
                  "realization of value, or for its conversion from one form into another. The "
                  "capital invested in those expenses (including the labor employed by it) "
                  "belongs to the dead expenses of capitalist production. They must be made up "
                  "out of the surplus-product and are, from the point of view of the entire "
                  "capitalist class, a deduction from the surplus-value or surplus "
                  "product&rdquo;."),
            ("p", "Think of the price of almost anything you buy. Some of it paid for making the "
                  "thing, some for moving it to the shop, and some for advertising, sales staff, "
                  "accounts, card fees and the shop's own margin. Ordinary accounting treats all "
                  "of those as costs that the price must cover. Marx draws a line through them. "
                  "On one side are costs that do something to the product: move it, keep it from "
                  "spoiling. On the other are costs that do nothing to the product and only "
                  "change who holds the value and in what form."),
            ("p", "Start with buying and selling. Marx quotes the old line &ldquo;When Greek "
                  "meets Greek, then comes the tug of war&rdquo;: each side tries to get the "
                  "better of the other, the haggling takes time, and none of that time adds "
                  "value, &ldquo;any more than the work done in a civil process increases the "
                  "value of the object of contention&rdquo;. His image is combustion: the work "
                  "of breaking up the coal is necessary for it to burn, and produces no heat."),
            ("p", "Hand the job to a specialist and nothing changes. Marx calls the opposite "
                  "belief a &ldquo;miracle of transsubstantiation&rdquo;. His arithmetic is about "
                  "a hired salesman who is paid the value of eight hours and works ten. His two "
                  "unpaid hours produce no surplus value, because his ten hours produce no value "
                  "at all. What they do is make the employer's cost of circulation smaller: ten "
                  "hours of a necessary but unproductive function bought for the price of "
                  "eight."),
            ("p", "Book-keeping is the same kind of cost, with a twist Marx stops to note: it "
                  "is &ldquo;more necessary in capitalist production than in scattered handicraft "
                  "and agricultural production, and still more necessary in co-operative than in "
                  "capitalist production&rdquo;. Money itself is the third: the gold kept in "
                  "circulation and replaced as it wears is social labour tied up in a machine for "
                  "exchanging."),
            ("p", "Storage is in between. A stock is needed for trade to flow at all: cotton "
                  "in the mill's store, yarn at the dealer's, bread in the shop. The cost of "
                  "keeping a necessary stock preserves the product and enters its value. But if "
                  "the stock is there because it will not sell, the cost is a loss, as a buyer "
                  "would tell the seller: &ldquo;So much the worse for you,&rdquo; &ldquo;Here "
                  "is another seller, whose articles were completed the day before "
                  "yesterday.&rdquo; Marx is careful about the first kind too. The costs of a "
                  "necessary stock &ldquo;enter in part into the value of the commodities&rdquo;, "
                  "which is what separates them from buying and selling, and yet from society's "
                  "side they are still &ldquo;dead expenses&rdquo;, labour spent keeping wealth "
                  "rather than making it; the lab keeps only the first half of that, the line "
                  "between a cost that enters the value and one that does not. Adam Smith thought "
                  "keeping a stock belonged to commercial society; Marx answers that every society "
                  "keeps one, and that capitalism changes its form into a stock of commodities."),
            ("p", "<strong>Volume II, Chapter 6, §3.</strong> &ldquo;The productive capital "
                  "invested in this industry adds value to the transported products, partly by "
                  "transferring value from the means of transportation, partly by adding value "
                  "through the labor-power used in transportation.&rdquo;"),
            ("p", "Transport is the exception because a product's use is where it is consumed. "
                  "Yarn in Manchester is not yet yarn on a loom in Bombay, and the carriage is "
                  "production continued after the product leaves the mill. Marx is sardonic "
                  "about the railways' freight tables, which turned the fragility of glass into "
                  "an excuse for higher rates: in sorting goods into classes, he writes, "
                  "&ldquo;the railroad magnates show a greater talent for inventing fantastic "
                  "species than botanists and zoologists.&rdquo;"),
            ("p", "The lab's presets put the line in figures. A capital of £400 produces goods "
                  "worth £500, a surplus value of £100. In the clerks preset a book-keeper paid £10 is a pure cost: "
                  "surplus value after costs is `£100 − £10 = £90`. In the transport preset a carter paid £10 adds £10 "
                  "to the value delivered, so the goods are worth £510 against £410 laid out, and "
                  "the surplus value is still £100. In the stockpile preset, store goods for £5 that a normal stock "
                  "needs, and another £5 because they would not sell, and £95 is left."),
            ("p", "This line is among the most argued-over in the book. The national accounts "
                  "of every modern economy count a shop's margin, a bank's fees and an "
                  "advertising agency's work as value added, and from Jean-Baptiste Say onward "
                  "economists have held that any service people will pay for is production. "
                  "Marxist economists disagree among themselves about where Marx's line falls; "
                  "Anwar Shaikh and Ahmet Tonak's 1994 attempt to remeasure national accounts "
                  "on his categories is one well-known answer. This lesson computes the line as "
                  "the chapter draws it."),
            ("p", "That ends Part I: the forms capital takes, and the time and the costs of "
                  "passing between them. The next course, The Turnover of Capital, measures "
                  "that time over a year and asks how much capital it takes to keep production "
                  "going."),
        ],
        "lab": ("capkit", {
            "mode": "circuit",
            "view": "costs",
            "money_unit": "£",
            "preset": "clerks",
            "presets": [
                {"id": "clerks", "label": "A book-keeper paid £10: a pure cost",
                 "M": 400, "product": 500, "pure_costs": 10, "value_adding_costs": 0, "expect": {"ciS": "£100", "ciSNet": "£90"}},
                {"id": "transport", "label": "A carter paid £10: a cost that adds value",
                 "M": 400, "product": 500, "pure_costs": 0, "value_adding_costs": 10, "expect": {"ciS": "£100", "ciSNet": "£100"}},
                {"id": "stockpile", "label": "£5 of necessary storage and £5 for goods that would not sell",
                 "M": 400, "product": 500, "pure_costs": 5, "value_adding_costs": 5, "expect": {"ciS": "£100", "ciSNet": "£95"}},
            ],
            "panel_title": "What is left of the surplus value",
            "panel_intro": (
                "The capital laid out in production and its product go in, with the costs of "
                "circulation sorted into pure costs and costs that add value. The table shows "
                "what each cost puts in and gets back; the tiles show surplus value before and "
                "after the pure costs. The figures are illustrative."
            ),
        }),
        "steps_title": "Sorting the costs of circulation",
        "steps_intro": "Four steps for any cost a business pays outside production.",
        "steps": [
            ("Find the surplus value",
             "Subtract the capital laid out in production from the value of the product."),
            ("Ask what the cost does",
             "A cost that only changes the form of value, buying, selling, accounts, money, is "
             "pure. A cost that moves the product to its use, or keeps a necessary stock from "
             "spoiling, adds value. Storage of goods that cannot be sold is pure."),
            ("Add value-adding costs to both sides",
             "A cost that adds value is laid out and comes back in the product's value, so it "
             "leaves the surplus value as it was."),
            ("Deduct pure costs from surplus value",
             "A pure cost comes back from nowhere in the product. It is paid out of surplus "
             "value, and what remains is surplus value after costs."),
        ],
        "worked": {
            "title": "A book-keeper and a carter",
            "intro": [
                "A capital of £400 produces goods worth £500. You want the surplus value left "
                "after paying a book-keeper £10, and after paying a carter £10 instead.",
            ],
            "lines": [
                "s:  £500 − £400 = £100",
                "book-keeper, pure:  £100 − £10 = £90",
                "carter, adds value:  £510 − £410 = £100",
                "stockpile:  £100 − £5 = £95",
            ],
            "after": [
                "The two £10 payments look the same in the cash book. One takes £10 from the "
                "surplus value; the other is returned in the value of goods that have been moved "
                "to where they will be used.",
            ],
        },
        "quiz_title": "Pure costs and costs that add value",
        "quiz": [
            {"q": "A capital of £400 produces goods worth £500 and pays a book-keeper £10. On the "
                  "chapter's classification, how much surplus value is left?",
             "a": ["£90", "£100", "£110", "£80"],
             "c": 0,
             "why": "Book-keeping is a pure cost, paid out of surplus value: `£100 − £10 = £90`. "
                    "£100 treats it as adding its own value, £110 as adding a profit, and £80 "
                    "deducts it twice."},
            {"q": "Which of these costs adds value to the commodity, on the chapter's argument?",
             "a": ["A salesman's wages",
                   "Carriage of the goods to the market where they are consumed",
                   "A book-keeper's wages",
                   "Warehouse rent for goods that cannot find a buyer"],
             "c": 1,
             "why": "Transport continues production inside circulation and adds value. Selling "
                    "and book-keeping only change the form of value, and storing goods that "
                    "will not sell is a loss, not an addition."},
            {"q": "A carter is paid £10 to deliver goods worth £500 that cost £400 to produce. "
                  "What is the surplus value, on the lab's accounting?",
             "a": ["£100", "£90", "£110", "£510"],
             "c": 0,
             "why": "The £10 is laid out and comes back in the value delivered, £510 against "
                    "£410, so the surplus value stays £100. £90 treats carriage as a pure cost, "
                    "£110 counts the £10 as surplus, and £510 is the value delivered."},
            {"q": "Marx's salesman is paid the value of 8 hours and works 10. What do his 2 "
                  "unpaid hours do, on the chapter's account?",
             "a": ["Reduce his employer's costs of circulation",
                   "Add 2 hours of value to the goods sold",
                   "Produce surplus value for his employer",
                   "Raise the price the buyer pays"],
             "c": 0,
             "why": "His labour creates no value, so its unpaid part creates no surplus value; it "
                    "makes ten hours of a necessary function cost the price of eight. Prices are "
                    "taken at value throughout, so the buyer pays no more."},
        ],
        "mistakes": [
            ("Thinking everything a business must pay for adds to the value of its product",
             "Every cost must be covered by the price, which makes this look obvious. The clerks "
             "preset separates covering from adding: the goods are worth £500 with or without "
             "the book-keeper, so his £10 can only come out of the £100 of surplus value, and "
             "the tile shows £90 left. Necessary is not the same as productive of value."),
            ("Thinking a cost becomes productive when a specialist takes it over",
             "Merchants, clerks and bank messengers do full-time what producers once did in "
             "spare hours. The division of labour makes the work cheaper and faster; it does "
             "not change what the work does to the product, which is nothing."),
            ("Treating all storage alike",
             "A stock that trade needs preserves use-value and adds value; a stock that piles "
             "up because it will not sell does not. In the stockpile preset the first £5 leaves "
             "the surplus value whole and the second £5 takes it to £95."),
        ],
        "standard": (
            "Finish when you can classify circulation costs and compute what is left of surplus value.",
            "Given the capital, the product's value and a list of circulation costs, classify "
            "each as a pure cost or a cost that adds value, and compute the surplus value before "
            "and after the pure costs."
        ),
        "note": (
            "The lab returns a value-adding cost at exactly its outlay, so the carter here adds "
            "value but no surplus value. On Marx's account carriage, like any wage-labour, also "
            "adds surplus value; the lab leaves that out to keep the one distinction in view. "
            "The figures are illustrative."
        ),
    },
]
